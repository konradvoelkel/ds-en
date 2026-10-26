#!/usr/bin/env python3
"""Generate the book cover: images/cover.svg, and the raster that ships from it.

    python3 tools/cover.py                  # write images/cover.svg + images/cover.png
    python3 tools/cover.py --check          # fail if the committed SVG is out of date
    python3 tools/cover.py --verify         # shape only, stdlib: what CI can rely on
    python3 tools/cover.py --png-width 900  # a different raster, same source

Why a cover at all
------------------

This is a web book; it has never had one. But a cover is what an answer engine reaches
for when it decides whether a thing is a *book*: ChatGPT, Perplexity and Google's book
panels all want a portrait image at the end of `Book.image`, and a landscape social card
is not that shape. SEO-NOTES.md §21 is the case where this went wrong in the other
direction -- an answer engine filled the empty slot with other people's book covers.

It is also, if the thing is ever printed, the file to start from. Hence 2:3 and vector.

Why 1400 x 2100
---------------

2:3 is the trade-paperback proportion, and the one a reader recognises as a book at
thumbnail size, which is the only size that matters here. The draft this is built from
was 1375 x 2000 (0.6875), close enough to look right and odd enough to be nobody's paper
size. Everything is expressed against `W` and `H`, so a different format is a different
pair of numbers, not a redraw: `--png-width` re-rasters, and for print, 6 x 9 inches at
300 dpi is `--png-width 1800`.

Where the drawing comes from
----------------------------

The open book is not redrawn here: it is `images/logo-wide.svg`, the site's own mark,
inlined minus its `<text>` elements -- the logo has "DATA SCIENCE" lettered across the
left page, which on a cover whose title says exactly that would be said twice. Dropping
`<text>` is also the only edit that can be made blind: everything else in that file is
geometry, and geometry has no opinion about where it is used.

**Except the globe, which is redrawn.** Six paths in `logo-wide.svg` -- a traced,
six-tone shaded sphere -- are 421 kB of its 437 kB. Inlined, they would make a 440 kB
cover whose weight is entirely one ornament, and at cover size the shading reads as a
grey smudge. It is replaced by a wireframe of one circle and nine ellipses, about 600
bytes, which is what that drawing looks like anyway at any size anyone will see. If the
original is ever wanted back, it is still in `logo-wide.svg`; nothing here edits that
file. `strip_logo()` fails loudly if the six paths are not where it expects them, on the
`thebe_gate.py` principle: a patch against someone else's shape says so when the shape
moves, rather than quietly producing something else.

Text is text, not outlines
--------------------------

The `<text>` elements name Inter, which means rendering this file needs Inter installed
(statics, not the variable build -- see `fonts/` in the repository notes). That is the
right trade for a source file: the title stays editable and searchable, and the artifact
that ships is the PNG, rendered once here. If the SVG itself ever has to render on a
machine that is not this one -- a print shop, say -- convert the text to paths first
(`inkscape --export-text-to-path`), and keep this file as the thing that generated it.

Why --check and --verify
------------------------

`tools/course_diagram.py` sets the rule: a file *written* as text is reproducible
anywhere, so it gets a byte-exact `--check`. A file *rendered* is at the mercy of cairo,
freetype and the installed fonts, so it gets `--verify`, which asserts the properties no
renderer can disagree about -- the PNG is there, it is the right size, and it is still
portrait 2:3. An undersized or landscape cover is the bug this guards: both make the
image stop being read as a book cover, which is the entire point of the file.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGO = ROOT / "images" / "logo-wide.svg"
SVG = ROOT / "images" / "cover.svg"
PNG = ROOT / "images" / "cover.png"

W, H = 1400, 2100
PNG_WIDTH = 1000

# From the draft (fake-book.xcf), sampled rather than guessed.
PAPER = "#b5cbd6"      # the board
INK = "#101418"        # the title: near-black, not black, so it sits on the board
NAVY = "#003964"       # subtitle and tagline
SLATE = "#45596b"      # the byline, quieter than the subtitle
FLASH = "#831990"      # the corner band
FLASH_FG = "#2edc17"   # and its lettering
GLOBE = "#4a5578"      # the wireframe, the mid-tone of the six it replaces

MARGIN = 118           # one left margin for every line of type on the cover
TITLE = "Data Science"
SUBTITLE = ["from stochastics to", "machine learning", "with Python"]
TAGLINE = "a free open textbook"
BYLINE = "Konrad Völkel · 2026"
LICENCE = "CC BY-SA 4.0"
IMPRINT = "datascience.konradvoelkel.com"
BAND = "now in English!"

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def strip_logo() -> str:
    """`images/logo-wide.svg` as inlinable markup: no `<text>`, no shaded globe.

    Returns the children of its root, serialised, with the globe group removed. The
    globe's own `<g>` is found by the fill of its first path rather than by position,
    and the count is asserted, so a redrawn logo stops this tool instead of silently
    losing an ornament or inlining 421 kB of one.
    """
    if not LOGO.exists():
        sys.exit(f"::error::{LOGO} is missing; it is the drawing this cover is built on")

    tree = ET.parse(LOGO)
    root = tree.getroot()

    for parent in root.iter():
        for child in list(parent):
            if child.tag == f"{{{SVG_NS}}}text":
                parent.remove(child)

    globes = [
        (parent, child)
        for parent in root.iter()
        for child in list(parent)
        if child.tag == f"{{{SVG_NS}}}g"
        and any(p.get("fill") == "#cccfdb" for p in child.findall(f"{{{SVG_NS}}}path"))
    ]
    if len(globes) != 1:
        sys.exit(
            f"::error::expected exactly one shaded-globe group in {LOGO.name}, found "
            f"{len(globes)}. The logo has been redrawn; look at what replaced the six "
            "paths filled #cccfdb .. #323e6f and decide whether the cover still wants "
            "a wireframe in their place."
        )
    parent, group = globes[0]
    paths = group.findall(f"{{{SVG_NS}}}path")
    if len(paths) != 6:
        sys.exit(
            f"::error::the globe group in {LOGO.name} has {len(paths)} paths, expected 6"
        )
    parent.remove(group)

    out = []
    for child in root:
        xml = ET.tostring(child, encoding="unicode")
        xml = xml.replace(f' xmlns:ns0="{SVG_NS}"', "").replace("ns0:", "")
        out.append(xml.strip())
    return "\n".join(out)


def wireframe_globe(cx: float, cy: float, r: float, sw: float) -> str:
    """A globe in ten elements, in the logo's own user units.

    Placement is the bounding box Inkscape reports for the group it replaces:
    x 16.60, y 1.26, 5.34 x 5.37 in `logo-wide.svg`'s viewBox.
    """
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r:.3f}"/>',
        f'<ellipse cx="{cx}" cy="{cy}" rx="{r:.3f}" ry="{r * 0.30:.3f}"/>',
    ]
    for f in (0.30, 0.66):                                   # meridians
        parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r * f:.3f}" ry="{r:.3f}"/>')
    parts.append(f'<line x1="{cx}" y1="{cy - r:.3f}" x2="{cx}" y2="{cy + r:.3f}"/>')
    for f in (0.52, 0.86):                                   # parallels
        dy, rx = r * f, r * (1 - f * f) ** 0.5
        for sign in (-1, 1):
            parts.append(
                f'<ellipse cx="{cx}" cy="{cy + sign * dy:.3f}" rx="{rx:.3f}" '
                f'ry="{rx * 0.30:.3f}"/>'
            )
    inner = "\n      ".join(parts)
    return (
        f'<g fill="none" stroke="{GLOBE}" stroke-width="{sw}" opacity=".85">\n'
        f"      {inner}\n    </g>"
    )


def build() -> str:
    art_scale = 23.0                       # logo units -> cover units
    art_w = 30 * art_scale
    art_x, art_y = (W - art_w) / 2, 1205

    band_fs = 54                           # the corner flash
    band_w = 186                           # the band's own width
    band_reach = 900                       # its length; both ends are clipped off
    # How far down the diagonal the band starts. The canvas cuts it to a chord of
    # 2*depth, so a band too near the corner is narrower than its own lettering and
    # loses both ends; at 150 the chord under the text is ~480 against ~390 of type.
    corner_inset = 150

    svg = f"""<svg xmlns="{SVG_NS}" width="{W}" height="{H}" viewBox="0 0 {W} {H}"
     role="img" aria-label="Book cover: {esc(TITLE)} — {esc(' '.join(SUBTITLE))}. \
{esc(TAGLINE)} by {esc(BYLINE)}.">
  <title>{esc(TITLE)} — {esc(" ".join(SUBTITLE))}</title>
  <desc>Cover of the open textbook "{esc(TITLE)}" by Konrad Völkel, 2026. An open book \
is drawn below the title, a wireframe globe and the Python logo on its right-hand page. \
A band across the top-right corner reads "{esc(BAND)}". Licensed {esc(LICENCE)}.</desc>

  <defs>
    <clipPath id="cover-edge"><rect width="{W}" height="{H}"/></clipPath>
  </defs>

  <rect width="{W}" height="{H}" fill="{PAPER}"/>

  <!-- The corner flash. A rotated band clipped to the board, not a filled triangle:
       a triangle has no inner edge, and the inner edge is what makes it read as a
       sticker on a cover rather than a corner that has been coloured in. -->
  <g clip-path="url(#cover-edge)">
    <g transform="translate({W} 0) rotate(45)">
      <rect x="-{band_reach / 2}" y="{corner_inset}" width="{band_reach}"
            height="{band_w}" fill="{FLASH}"/>
      <text x="0" y="{corner_inset + band_w / 2 + band_fs * 0.35:.0f}"
            text-anchor="middle"
            font-family="Inter Display, Inter, sans-serif" font-weight="700"
            font-size="{band_fs}" fill="{FLASH_FG}"
            font-style="italic">{esc(BAND)}</text>
    </g>
  </g>

  <!-- Title. Inter Display is the optical size cut for large type: tighter spacing and
       smaller apertures than Inter, which is drawn for body text and looks loose here.
       The negative tracking is Inter Display's own recommendation above ~48 px. -->
  <text x="{MARGIN}" y="610" font-family="Inter Display, Inter, sans-serif"
        font-weight="800" font-size="186" letter-spacing="-5" fill="{INK}">\
{esc(TITLE)}</text>

  <text x="{MARGIN}" y="800" font-family="Inter Display, Inter, sans-serif"
        font-weight="300" font-size="104" letter-spacing="-1.5" fill="{NAVY}">
"""
    for i, line in enumerate(SUBTITLE):
        svg += f'    <tspan x="{MARGIN}" dy="{0 if i == 0 else 126}">{esc(line)}</tspan>\n'

    svg += f"""  </text>

  <g transform="translate({art_x:.1f} {art_y}) scale({art_scale})">
{strip_logo()}
    {wireframe_globe(19.27, 3.94, 2.67, 0.085)}
  </g>

  <!-- A hairline, which is the cheapest thing on a cover that says someone set it:
       it closes the drawing and opens the imprint block under it. -->
  <line x1="{MARGIN}" y1="1700" x2="{W - MARGIN}" y2="1700"
        stroke="{NAVY}" stroke-width="2" opacity=".35"/>

  <text x="{MARGIN}" y="1800" font-family="Inter, sans-serif" font-weight="500"
        font-size="58" fill="{NAVY}">{esc(TAGLINE)}</text>

  <text x="{MARGIN}" y="1930" font-family="Inter, sans-serif" font-weight="300"
        font-size="58" fill="{SLATE}">{esc(BYLINE)}</text>

  <!-- The imprint line. A cover without one looks like a poster; this book's
       publisher is its address. -->
  <text x="{MARGIN}" y="2010" font-family="Inter, sans-serif" font-weight="400"
        font-size="38" letter-spacing="1" fill="{SLATE}" opacity=".8">{esc(IMPRINT)}</text>

  <!-- The licence, set rather than badged. The official button is 267 x 50 of raster
       whose three glyphs are illegible below about 120 px wide, and a cover is read at
       300 px tall; the words survive that and the glyphs do not. -->
  <g transform="translate({W - MARGIN} 1930)">
    <rect x="-296" y="-56" width="296" height="78" rx="12" fill="{NAVY}" opacity=".92"/>
    <text x="-148" y="-1" text-anchor="middle" font-family="Inter, sans-serif"
          font-weight="600" font-size="40" letter-spacing=".5"
          fill="{PAPER}">{esc(LICENCE)}</text>
  </g>
</svg>
"""
    return svg


def render(png_width: int) -> None:
    SVG.write_text(build(), encoding="utf-8")

    height = round(png_width * H / W)
    if shutil.which("rsvg-convert"):
        cmd = ["rsvg-convert", "-w", str(png_width), "-h", str(height),
               "-o", str(PNG), str(SVG)]
    elif shutil.which("inkscape"):
        cmd = ["inkscape", "-w", str(png_width), "-h", str(height),
               "-o", str(PNG), str(SVG)]
    else:
        sys.exit(
            "::error::no SVG renderer found. Install librsvg2-bin (rsvg-convert) or "
            "inkscape. Like tools/logo_raster.py, this is not run in CI -- the PNG is "
            "committed -- so it only needs to hold on the machine regenerating the cover."
        )
    subprocess.run(cmd, check=True, capture_output=True)

    print(
        f"✓ {SVG.relative_to(ROOT)} written ({SVG.stat().st_size:,} bytes) and rendered "
        f"to {PNG.relative_to(ROOT)} at {png_width}x{height} "
        f"({PNG.stat().st_size:,} bytes) using {cmd[0]}"
    )


def check() -> None:
    if not SVG.exists():
        sys.exit(f"::error::{SVG} is missing; run tools/cover.py")
    if SVG.read_text(encoding="utf-8") != build():
        sys.exit(
            f"::error::{SVG.relative_to(ROOT)} is not what tools/cover.py writes today. "
            "Re-run it, or move the edit into the generator -- a cover edited by hand is "
            "a cover that cannot be regenerated at another size."
        )
    print(f"✓ {SVG.relative_to(ROOT)} is byte-identical to what tools/cover.py writes")


def png_header(data: bytes) -> tuple[int, int]:
    """Width and height from the IHDR, standard library only.

    The reason is tools/social_card.py's: CI runs this before anything installs Pillow,
    and a guard that needs a dependency to say "the file is the right shape" reports its
    own setup rather than the artwork.
    """
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("not a PNG, or no IHDR where a PNG must have one")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def verify() -> None:
    if not PNG.exists():
        sys.exit(f"::error::{PNG} is missing; run tools/cover.py")
    try:
        w, h = png_header(PNG.read_bytes())
    except ValueError as exc:
        sys.exit(f"::error::{PNG}: {exc}")

    if w < 600:
        sys.exit(
            f"::error::{PNG.relative_to(ROOT)} is {w}px wide. A cover below ~600px is "
            "soft in the one place it is used, a preview card on a high-DPI screen."
        )
    if abs(h / w - H / W) > 0.01:
        sys.exit(
            f"::error::{PNG.relative_to(ROOT)} is {w}x{h}, a ratio of {h / w:.3f}:1, but "
            f"the cover is {H / W:.3f}:1. Portrait 2:3 is what makes an answer engine "
            "read the image as a book cover rather than a banner; a squashed or "
            "landscape re-export silently gives that up."
        )
    print(f"✓ {PNG.relative_to(ROOT)} is {w}x{h}, portrait {h / w:.3f}:1")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="fail if images/cover.svg is out of date")
    ap.add_argument("--verify", action="store_true",
                    help="stdlib-only shape check of images/cover.png")
    ap.add_argument("--png-width", type=int, default=PNG_WIDTH,
                    help=f"raster width in pixels (default {PNG_WIDTH})")
    args = ap.parse_args()

    if args.check:
        check()
    elif args.verify:
        verify()
    else:
        render(args.png_width)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
