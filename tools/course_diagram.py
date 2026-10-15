#!/usr/bin/env python3
"""Generate images/course-structure.svg, the overview on the landing page.

    python3 tools/course_diagram.py            # write the SVG
    python3 tools/course_diagram.py --check    # fail if the committed file is out of date

Why not mermaid: MyST renders a ```{mermaid} block in the browser. The static HTML holds
an empty <figure></figure>, so a crawler, a reader without JavaScript and a screen reader
all get nothing, and the directive takes no :caption: (tested -- "unexpected option").
Pre-rendering with mermaid-cli would pull headless Chromium into the build for one
picture. The structure is small and regular enough to draw directly, which also buys a
caption, alt text, the book's own brand colour and a diagram that follows the reader's
light/dark setting.

The content is the same as the mermaid source it replaces, and must stay in step with the
part titles in myst.yml.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images" / "course-structure.svg"

# (part title, [node, ...]); a node is a list of lines.
PARTS: list[tuple[str, list[list[str]]]] = [
    ("Introduction", [["What is Data Science?"], ["Stochastics"], ["Python"]]),
    ("Discrete stochastics and Numpy",
     [["Random variables, distributions,", "expected value"], ["Numpy"],
      ["Discrete distributions,", "first exploration"]]),
    ("Continuous stochastics and Scipy",
     [["Continuous distributions,", "normal distribution, Scipy"]]),
    ("Exploratory data analysis",
     [["Descriptive statistics,", "examples, Iris"], ["Pandas, data cleaning"]]),
    ("Multivariate stochastics",
     [["Covariance, multivariate", "normal distribution, relative entropy"]]),
    ("Data protection", [["Data protection glossary"]]),
    ("Machine learning",
     [["Clustering,", "dimensionality reduction"], ["Statistical models,", "regression, kernels"],
      ["Tests, model selection,", "expectation maximization"]]),
]

W = 920
PAD = 18           # band padding
LABEL_H = 24       # part title strip
LINE_H = 17
NODE_PAD_Y = 11
NODE_PAD_X = 16
GAP_X = 42         # between nodes, holds the arrow
GAP_Y = 30         # between bands, holds the arrow
CHAR_W = 6.55      # 12.5px DejaVu/Inter average advance; measured, not guessed


def text_w(lines: list[str]) -> float:
    return max(len(line) for line in lines) * CHAR_W


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build() -> str:
    bands, y = [], PAD
    for title, nodes in PARTS:
        widths = [text_w(n) + 2 * NODE_PAD_X for n in nodes]
        heights = [len(n) * LINE_H + 2 * NODE_PAD_Y for n in nodes]
        row_h = max(heights)
        band_h = LABEL_H + row_h + 2 * PAD
        total = sum(widths) + GAP_X * (len(nodes) - 1)
        x = (W - total) / 2
        placed = []
        for node, w, h in zip(nodes, widths, heights):
            placed.append((x, y + LABEL_H + PAD + (row_h - h) / 2, w, h, node))
            x += w + GAP_X
        bands.append((title, y, band_h, placed))
        y += band_h + GAP_Y
    height = y - GAP_Y + PAD

    p: list[str] = []
    p.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height:.0f}" '
        f'width="{W}" height="{height:.0f}" role="img" '
        f'aria-labelledby="ttl dsc">'
    )
    p.append('<title id="ttl">How the parts of the course build on one another</title>')
    p.append(
        '<desc id="dsc">Seven parts in sequence, each leading to the next: '
        + "; ".join(f"{t} ({', '.join(' '.join(n) for n in ns)})" for t, ns in PARTS)
        + ".</desc>"
    )
    p.append("""<style>
  :root { color-scheme: light dark; }
  .band  { fill: #f2fbfb; stroke: #bfe4e4; }
  .node  { fill: #ffffff; stroke: #007d7e; stroke-width: 1.5; }
  .ptitle{ fill: #006364; font-weight: 600; }
  .ntext { fill: #1a1a1a; }
  .arrow { stroke: #007d7e; stroke-width: 2; fill: none; }
  .head  { fill: #007d7e; }
  text { font-family: Inter, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; }
  @media (prefers-color-scheme: dark) {
    .band  { fill: #16211f; stroke: #2a3d3c; }
    .node  { fill: #1b2225; stroke: #2cc5c5; }
    .ptitle{ fill: #6fdcdc; }
    .ntext { fill: #e9ecef; }
    .arrow { stroke: #2cc5c5; }
    .head  { fill: #2cc5c5; }
  }
</style>""")
    p.append('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto-start-reverse">'
             '<path class="head" d="M0,0 L10,5 L0,10 z"/></marker></defs>')

    for title, by, bh, placed in bands:
        p.append(f'<rect class="band" x="{PAD}" y="{by:.0f}" width="{W - 2 * PAD}" '
                 f'height="{bh:.0f}" rx="10"/>')
        p.append(f'<text class="ptitle" x="{PAD + 16}" y="{by + 19:.0f}" font-size="13.5">'
                 f'{esc(title)}</text>')
        for i, (nx, ny, nw, nh, lines) in enumerate(placed):
            p.append(f'<rect class="node" x="{nx:.1f}" y="{ny:.1f}" width="{nw:.1f}" '
                     f'height="{nh:.1f}" rx="7"/>')
            first = ny + NODE_PAD_Y + LINE_H - 5
            for k, line in enumerate(lines):
                p.append(f'<text class="ntext" x="{nx + nw / 2:.1f}" '
                         f'y="{first + k * LINE_H:.1f}" font-size="12.5" '
                         f'text-anchor="middle">{esc(line)}</text>')
            if i + 1 < len(placed):
                nx2 = placed[i + 1][0]
                cy = ny + nh / 2
                p.append(f'<path class="arrow" marker-end="url(#a)" '
                         f'd="M{nx + nw + 7:.1f},{cy:.1f} H{nx2 - 8:.1f}"/>')

    for (t1, y1, h1, _), (t2, y2, _, _) in zip(bands, bands[1:]):
        p.append(f'<path class="arrow" marker-end="url(#a)" '
                 f'd="M{W / 2:.0f},{y1 + h1 + 4:.0f} V{y2 - 5:.0f}"/>')

    p.append("</svg>")
    return "\n".join(p) + "\n"


def main() -> int:
    svg = build()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != svg:
            print(f"✗ {OUT.relative_to(ROOT)} is out of date; run tools/course_diagram.py")
            return 1
        print(f"✓ {OUT.relative_to(ROOT)} matches tools/course_diagram.py")
        return 0
    OUT.write_text(svg, encoding="utf-8")
    print(f"✓ wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
