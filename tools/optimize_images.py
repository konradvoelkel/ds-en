#!/usr/bin/env python3
"""Re-encode the book's PNGs in place, and cap the size of the oversized sources.

    python3 tools/optimize_images.py images/ --max-width 1600
    python3 tools/optimize_images.py _build/html/build       # CI: re-encode only
    python3 tools/optimize_images.py images/ --max-width 1600 --check

Measured on the live site, 2026-10-16: 197 distinct images, **21.3 MB**. One chapter
(descriptive-statistics) shipped 6.4 MB of figures and its LCP was 2712 ms against a
2500 ms budget, with the LCP element a 5.79 MB PNG displayed at 480 px wide.


Why there is anything to win at all
-----------------------------------

Matplotlib saves RGBA. A plot has no transparency to speak of -- `savefig` writes an
opaque white background -- but the fourth channel is there anyway, and PNG's filters
compress four channels much worse than one. Worse, a plot is a handful of flat colours
and some anti-aliased text: one chapter's 790 kB figure has **232 distinct colours**.
Stored as a palette image that is not an approximation, it is the same picture in a
byte per pixel instead of four.

So the transform is: drop the alpha channel when it is provably unused, then store as a
256-colour palette when that is either exactly lossless or close enough to measure.
Typically 50-60% off, and nothing else about the file changes -- same name, same
dimensions, same pixels to the eye.


What is never touched
---------------------

**Images whose alpha channel is actually in use.** Four of them, the hand-drawn
diagrams. The site follows the reader's light/dark setting, and a figure with a
transparent background is one that was *drawn* to sit on either. Flattening it onto
white would look fine in the build and wrong on half the machines that opened it. These
get the downscale and nothing else.

That distinction is measured, not assumed: the alpha channel's minimum is 255 or it is
not, and only the first case is flattened.


The quality gate
----------------

A picture with 256 colours or fewer converts to a palette *exactly*, and the tool
asserts it -- it compares every pixel and refuses the result if a single one moved. No
threshold, no judgement.

Above 256 colours the conversion is an approximation, so it is measured and gated: mean
absolute error <= 1.5/255 and 99.9th-percentile error <= 40/255, over all three
channels. Real figures come in around 0.2-0.8 mean, far inside it; a smooth colourmap
that would band noticeably comes in above it and keeps its full-colour encoding. A
candidate that fails the gate, or that is not actually smaller, is discarded and the
original is re-encoded losslessly instead.


--max-width, and why only for the sources
-----------------------------------------

`images/` holds hand-made figures at whatever size they were drawn or scanned:
ds-process-oneill.png is 3678x2259, and the page shows it at 480. Capping the width
costs nothing anyone can see on screen and is still far above what the PDF needs -- 1600
px across a text-width figure is over 300 dpi in print.

Notebook output does **not** get a cap. Matplotlib already wrote those at the figure
size the notebook asked for, so they arrive at roughly display size; downscaling them
would be re-rendering a plot badly rather than compressing a picture well.


--check
-------

Reports what would be saved and exits 1 if anything still can be. That is the CI guard
for the committed `images/`: it does not re-encode the repository behind your back, it
fails and tells you to run the tool. On the build directory CI simply runs the
optimisation, because that output is generated and not reviewed.


Why not WebP, which would be better
-----------------------------------

WebP at q82 measured **89%** off the same figure, against 57% here. It is not done
because the filename would have to change, and the filename appears twice in each page:
once in the <img> and once inside `window.__remixContext`, the hydration payload that
holds the whole page again as JSON. Rewriting both is possible; getting it wrong means
the server-rendered page is right and the hydrated one 404s every figure, which is
invisible to a crawler and obvious to a reader. The safe half of the win needs no
reference rewriting at all, so it goes first. The other half is a separate change with
its own guard, if it is ever wanted.
"""

from __future__ import annotations

import argparse
import io
import pathlib
import re
import sys

import numpy as np
from PIL import Image

MAE_LIMIT = 1.5
P999_LIMIT = 40.0
MAX_COLOURS = 256

# A re-encode has to earn its commit. Running the palette conversion over an image that
# is already a palette image shaves a handful of bytes -- the adaptive palette comes out
# in a slightly different order -- and without a floor the tool would rewrite every file
# on every run and `--check` would never go green, which is a guard that cannot be
# satisfied and so teaches people to ignore it. Below the floor the file is left exactly
# as it is, which is also what makes the tool idempotent.
MIN_GAIN_BYTES = 2048
MIN_GAIN_RATIO = 0.02

# Artwork that a generator owns, and that a generator checks byte for byte.
#
# social_card.py --check compares the committed card against a freshly rendered one, so
# re-encoding the card here makes that check report the card as out of date, and the
# obvious response -- re-running the generator -- silently undoes the optimisation. The
# card would have gone from 40 kB to 18 kB; the generator staying the single source of
# truth for its own output is worth more than 22 kB, and a check that cries wolf is
# worth less than nothing. (CI runs --verify, which only asserts 1200x630 and would not
# have caught this; it showed up in --check, which is local-only.)
#
# cover.png is the same arrangement one step looser, and the arithmetic is bigger: the
# palette pass takes it from 161 kB to 52 kB, five times the card's saving. It is still
# left alone, and the reason it is an easier call rather than a harder one is who pays.
# No page loads the cover -- it is referenced only from the landing page's JSON-LD and
# from llms.txt, i.e. fetched once by a crawler that went looking for it -- while the
# card is fetched by every link preview. So the 109 kB is not on any reader's path, and
# tools/cover.py --check stays the thing that says whether the committed cover is the
# cover the generator writes. If the 109 kB is ever wanted, it belongs inside cover.py's
# render step, where the next regeneration keeps it. (SEO-NOTES.md §26.)
#
# course-structure.svg and cover.svg have the same arrangement but are not PNGs, so they
# never arrive here in the first place.
GENERATED = {"social-card.png", "cover.png"}


def unfingerprint(name: str) -> str:
    """'social-card-<32 hex>.png' -> 'social-card.png'; anything else unchanged."""
    return re.sub(r"-[0-9a-f]{32}(\.png)$", r"\1", name)


def encode(im: Image.Image) -> bytes:
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def alpha_is_used(im: Image.Image) -> bool:
    if im.mode not in ("RGBA", "LA", "PA"):
        return False
    if im.mode == "PA":
        return True
    return im.getchannel("A").getextrema()[0] < 255


def best_encoding(im: Image.Image) -> tuple[bytes, str]:
    """Smallest acceptable PNG for this image, and a word for what was done."""
    keep_alpha = alpha_is_used(im)
    base = im if keep_alpha else im.convert("RGB")
    candidates = [(encode(base), "recompressed")]

    if not keep_alpha:
        pal = base.convert("P", palette=Image.ADAPTIVE, colors=MAX_COLOURS)
        before = np.asarray(base, dtype=np.int16)
        after = np.asarray(pal.convert("RGB"), dtype=np.int16)
        diff = np.abs(before - after)

        colours = base.getcolors(maxcolors=MAX_COLOURS)
        if colours is not None:
            # <= 256 colours: the palette holds every one of them, so this must be
            # pixel-for-pixel identical. If it is not, something is wrong with the
            # assumption and the result is thrown away rather than trusted.
            if not diff.any():
                candidates.append((encode(pal), "palette (lossless)"))
        elif diff.mean() <= MAE_LIMIT and np.percentile(diff, 99.9) <= P999_LIMIT:
            candidates.append((encode(pal), f"palette (mae {diff.mean():.2f})"))

    return min(candidates, key=lambda c: len(c[0]))


def process(path: pathlib.Path, max_width: int | None, dry_run: bool) -> tuple[int, int, str]:
    """Returns (bytes before, bytes after, note)."""
    before = path.stat().st_size
    with Image.open(path) as im:
        im.load()
        note = ""

        if max_width and im.width > max_width:
            h = round(im.height * max_width / im.width)
            im = im.resize((max_width, h), Image.LANCZOS)
            note = f"{max_width}px"

        data, how = best_encoding(im)

    note = f"{note}, {how}" if note else how
    gain = before - len(data)
    if gain < MIN_GAIN_BYTES or gain < before * MIN_GAIN_RATIO:
        return before, before, note  # not worth rewriting the file for
    if not dry_run:
        path.write_bytes(data)
    return before, len(data), note


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--max-width", type=int, default=None)
    ap.add_argument(
        "--check",
        action="store_true",
        help="report and exit 1 if anything could still be saved; change nothing",
    )
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    files: list[pathlib.Path] = []
    for p in args.paths:
        path = pathlib.Path(p)
        files += sorted(path.rglob("*.png")) if path.is_dir() else [path]

    # MyST fingerprints asset filenames, so the card is social-card.png in images/ and
    # social-card-<32 hex>.png in the build. Both are the same generated file.
    skipped = [f for f in files if unfingerprint(f.name) in GENERATED]
    files = [f for f in files if unfingerprint(f.name) not in GENERATED]
    for f in skipped:
        print(f"  skipping {f.name}: generated artwork, see GENERATED in this file")

    total_before = total_after = 0
    shrunk: list[tuple[str, int, int, str]] = []

    for f in files:
        try:
            before, after, note = process(f, args.max_width, args.check)
        except Exception as exc:  # a corrupt or exotic PNG must not fail the build
            print(f"::warning::{f}: {exc}")
            continue
        total_before += before
        total_after += after
        if after < before:
            shrunk.append((str(f), before, after, note))

    if not args.quiet:
        for name, b, a, note in sorted(shrunk, key=lambda r: r[1] - r[2], reverse=True)[:12]:
            print(f"  {b:>9,} -> {a:>9,}  ({100 - 100 * a / b:>2.0f}%)  {note:24} {name}")

    saved = total_before - total_after
    verb = "could save" if args.check else "saved"
    print(
        f"optimize_images: {len(files)} PNGs, {len(shrunk)} improved, "
        f"{verb} {saved / 1048576:.1f} MB of {total_before / 1048576:.1f} MB "
        f"({100 * saved / total_before:.0f}%)"
        if total_before
        else "optimize_images: no PNGs found"
    )

    if args.check and shrunk:
        print(
            "::error::images are not optimised; run "
            f"`python3 tools/optimize_images.py {' '.join(args.paths)}"
            + (f" --max-width {args.max_width}" if args.max_width else "")
            + "` and commit the result"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
