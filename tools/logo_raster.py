#!/usr/bin/env python3
"""Render the navbar logo from its SVG source to the raster the site actually serves.

    python3 tools/logo_raster.py            # re-render images/logo-wide.png
    python3 tools/logo_raster.py --verify   # what CI checks

`images/logo-wide.svg` is **437 kB** -- one of its seventeen paths is 117 kB of
coordinates on its own -- and it loaded on all thirty pages. After the figure work of
2026-10-16 that made it the largest single asset on the site and about a quarter of
`descriptive-statistics`'s on-load image payload.

It is a drawing of an open book. It renders in the navigation at **72 x 36 CSS pixels**,
and nowhere else and at no other size: the theme fixes `height: 36px`, and that was
measured at desktop and mobile widths and with the mobile menu open. 437 kB of Bezier
curves to fill a thumbnail.

So the SVG becomes what it should always have been -- the *source* -- and the site is
served a raster of it. It stays in the repository, and this tool is the link between
them. 437,307 bytes to 18,150.

**On the wire that is 122,702 to 18,150 -- 105 kB and 85% off every page, not 96%.** An
SVG is text and GitHub Pages serves it gzipped, so the figure to quote is the compressed
one; the PNG is already compressed and gzip does nothing for it. Confirmed against the
live site rather than computed: the on-load image payload of descriptive-statistics fell
by 107,477 bytes across the change, which is this and nothing else.


Why 216 x 108
-------------

Three times the 72 x 36 it renders at, which is crisp on any display anyone has: a
3x-DPR phone maps one image pixel to one device pixel exactly. The aspect ratio is the
SVG's own 2:1 (`viewBox="0 0 30 15"`), **not** the tighter framing of the previous
`logo-wide.png`, which was an unreferenced 609 x 417 crop of the same artwork. Handing
the theme a differently-framed image would have changed the logo's rendered width from
72 px to 53, since the height is what is pinned -- a layout change dressed up as an
optimisation.

A `srcset` with 1x/2x/3x would save a few kilobytes on low-DPI screens. Not done: the
theme writes a plain `<img>`, so it would mean yet more post-processing of the built
HTML, to save single-digit kilobytes off an 18 kB file.


Why PNG, and why not the smaller palette
----------------------------------------

The logo sits on a navbar whose colour changes with the reader's light/dark setting, so
its transparency is load-bearing. Four encodings were measured by compositing each over
white *and* over the dark navbar colour and diffing against the same composite of the
SVG render:

    png RGBA        18,150   exact on both
    png palette      5,868   up to 36/255 off
    webp lossless   13,890   exact on both

The palette version is a third of the size and keeps a working alpha channel, but it
moves colours by up to 36 levels, and this drawing has gradients -- the globe is three
radial gradients -- which is where that shows as banding. For the one image that is the
book's mark, on every page, exactness is worth twelve kilobytes. WebP lossless is also
exact and 4 kB smaller again; PNG is chosen over it because this file is the obvious
thing to reach for when something else needs the logo, and PNG is what everything reads.

`tools/optimize_images.py` leaves this file alone of its own accord, with no entry in its
GENERATED set: the alpha channel is genuinely in use, so it never reaches the palette
branch, and plain recompression gains less than that tool's floor.


Why --verify and not --check
----------------------------

`tools/social_card.py` draws the same distinction and for the same reason, which is worth
restating rather than re-deriving. This file is *rendered*, by librsvg or Inkscape,
against whatever versions of cairo and the system fonts a machine happens to have. A
byte-exact comparison in CI would be a check that fails for reasons having nothing to do
with the logo. So CI asserts the properties that actually matter and that no renderer can
disagree about -- that the file is there, that it is a 216 x 108 PNG, that its PNG colour
type can hold transparency at all, and that its aspect still matches the SVG's viewBox.
An undersized, flattened or wrongly-shaped logo is the bug this guards. It reads the IHDR
with the standard library, because CI runs this before anything installs Pillow.

`tools/course_diagram.py` keeps a byte-exact `--check` because it *writes* its SVG as
text rather than rendering it, so it is reproducible anywhere. The three tools differ in
which check they can honestly make, not in how careful they are.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import subprocess
import sys

SVG = pathlib.Path("images/logo-wide.svg")
PNG = pathlib.Path("images/logo-wide.png")

# The theme pins height: 36px, so the logo renders at 72x36 CSS pixels. 3x of that.
DISPLAY = (72, 36)
SCALE = 3
WIDTH, HEIGHT = DISPLAY[0] * SCALE, DISPLAY[1] * SCALE


def svg_aspect(path: pathlib.Path) -> float:
    m = re.search(r'viewBox="([\d.\s-]+)"', path.read_text(encoding="utf-8"))
    if not m:
        sys.exit(f"::error::{path} has no viewBox; cannot check the aspect ratio")
    _, _, w, h = (float(v) for v in m.group(1).split())
    return w / h


def render() -> None:
    if not SVG.exists():
        sys.exit(f"::error::{SVG} is missing; it is the source this is rendered from")

    aspect = svg_aspect(SVG)
    if abs(aspect - WIDTH / HEIGHT) > 0.01:
        sys.exit(
            f"::error::{SVG} is {aspect:.3f}:1 but the raster is {WIDTH / HEIGHT:.3f}:1. "
            "Pinning the height means a different aspect changes the rendered width; "
            "adjust DISPLAY in this file rather than squashing the drawing."
        )

    if shutil.which("rsvg-convert"):
        cmd = ["rsvg-convert", "-w", str(WIDTH), "-h", str(HEIGHT), "-o", str(PNG), str(SVG)]
    elif shutil.which("inkscape"):
        cmd = ["inkscape", "-w", str(WIDTH), "-h", str(HEIGHT), "-o", str(PNG), str(SVG)]
    else:
        sys.exit(
            "::error::no SVG renderer found. Install librsvg2-bin (rsvg-convert) or "
            "inkscape. This tool is not run in CI -- the PNG is committed -- so this "
            "only needs to hold on the machine regenerating the logo."
        )

    subprocess.run(cmd, check=True, capture_output=True)

    from PIL import Image

    with Image.open(PNG) as im:
        im = im.convert("RGBA")
        im.save(PNG, "PNG", optimize=True)

    print(
        f"✓ {PNG} rendered from {SVG} at {WIDTH}x{HEIGHT} "
        f"({PNG.stat().st_size:,} bytes, from {SVG.stat().st_size:,} as SVG) "
        f"using {cmd[0]}"
    )


def png_header(data: bytes) -> tuple[int, int, int]:
    """(width, height, colour type) from the IHDR, with the standard library only.

    Pillow is not imported on this path on purpose. `tools/social_card.py --verify` set
    the rule and gives the reason: CI runs these checks before anything installs Pillow,
    and a guard that needs a dependency in order to say "the file is the right shape" is
    a guard that reports its own setup instead of the artwork.
    """
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    if data[12:16] != b"IHDR":
        raise ValueError("no IHDR where a PNG must have one")
    w = int.from_bytes(data[16:20], "big")
    h = int.from_bytes(data[20:24], "big")
    return w, h, data[25]


def verify() -> None:
    if not PNG.exists():
        sys.exit(f"::error::{PNG} is missing; run tools/logo_raster.py")

    data = PNG.read_bytes()
    try:
        w, h, colour_type = png_header(data)
    except ValueError as exc:
        sys.exit(f"::error::{PNG}: {exc}")

    if (w, h) != (WIDTH, HEIGHT):
        sys.exit(
            f"::error::{PNG} is {w}x{h}, expected {WIDTH}x{HEIGHT} -- the navbar renders "
            f"it at {DISPLAY[0]}x{DISPLAY[1]}, so a smaller file is visibly soft on a "
            "high-DPI screen"
        )

    # Colour types 4 and 6 carry an alpha channel; 3 (palette) can carry transparency in
    # a tRNS chunk. Types 0 and 2 cannot be transparent at all, which is what flattening
    # produces -- and a flattened logo is a white block on the dark navbar. This says the
    # file *can* be transparent, not that every pixel is right; proving the latter needs
    # a decoder, and the failure actually worth catching is the flatten.
    if colour_type not in (4, 6) and not (colour_type == 3 and b"tRNS" in data[:4096]):
        sys.exit(
            f"::error::{PNG} has PNG colour type {colour_type}, which cannot hold "
            "transparency. The navbar changes colour with the reader's light/dark "
            "setting, so a flattened logo shows as a block of background in one of them."
        )

    if SVG.exists():
        aspect = svg_aspect(SVG)
        if abs(aspect - WIDTH / HEIGHT) > 0.01:
            sys.exit(
                f"::error::{SVG} is now {aspect:.3f}:1 but {PNG} is {WIDTH / HEIGHT:.3f}:1. "
                "The source has been redrawn at a different shape; re-render the raster."
            )

    print(f"✓ {PNG} is a {WIDTH}x{HEIGHT} PNG that can hold transparency ({len(data):,} bytes)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="check the committed raster; render nothing")
    args = ap.parse_args()
    verify() if args.verify else render()


if __name__ == "__main__":
    main()
