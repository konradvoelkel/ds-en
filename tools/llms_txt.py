#!/usr/bin/env python3
"""Publish the book's sources as Markdown, and index them in llms.txt.

    python3 tools/llms_txt.py <site-url> <html-dir>

Run from the deploy workflow, after the origin has been written into the build. It does
three things to the built site:

  * writes each chapter's source as Markdown to `<slug>.md` and `<slug>/index.md`
    (notebooks are flattened: markdown cells verbatim, code cells in ```python fences,
    outputs dropped -- they are images and long tables, and no use to a reader of source);
  * adds `<link rel="alternate" type="text/markdown">` to each page's <head>, so a tool
    holding the HTML can find the source without guessing;
  * writes `/llms.txt` (a short index, in reading order) and `/llms-full.txt` (the whole
    book in one file, for a long-context window).

Why not inline shell in the workflow: the chapter titles live in YAML frontmatter, not in
a leading `# ` line, so grepping for a heading yields nothing; the landing page's source is
`landing-page.md` while its URL is the site root; and a `sed` of a multi-kilobyte payload
into `</head>` is fragile. All three are easy here and were wrong in the suggestion this
was written from.

The order comes from `myst.yml`'s toc, which is the same order as the sitemap and the
printed book.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing. Run with: uv run --with pyyaml python tools/llms_txt.py …")

ROOT = Path(__file__).resolve().parent.parent

HEADER = """# {title}

> {description}

An open textbook by {author} ({affiliation}), CC BY-SA 4.0. It begins with probability
and statistics and ends with machine learning without leaving a gap in between: the
estimators and learning algorithms are reimplemented in Python rather than called.

Archived at https://doi.org/10.5281/zenodo.23444644 — the concept DOI, which always
resolves to the newest version, and the one to cite.

Each chapter below links to its Markdown source. The whole book in one file is at
{site}/llms-full.txt

## Chapters
"""


def toc_files(toc) -> list[str]:
    out = []
    for entry in toc:
        if "file" in entry:
            out.append(entry["file"])
        for child in entry.get("children", []):
            out.extend(toc_files([child]))
    return out


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    return text[end + 4:].lstrip("\n") if end >= 0 else text


def as_markdown(path: Path) -> tuple[str, str]:
    """(title, markdown body) for one chapter source."""
    if path.suffix == ".ipynb":
        nb = json.loads(path.read_text(encoding="utf-8"))
        cells = nb.get("cells", [])
        fm = frontmatter("".join(cells[0].get("source", []))) if cells else {}
        parts = []
        for i, cell in enumerate(cells):
            src = "".join(cell.get("source", ""))
            if cell.get("cell_type") == "markdown":
                parts.append(strip_frontmatter(src) if i == 0 else src)
            elif cell.get("cell_type") == "code" and src.strip():
                parts.append("```python\n" + src.rstrip() + "\n```")
        body = "\n\n".join(p for p in parts if p.strip())
    else:
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        body = strip_frontmatter(text)
    title = str(fm.get("title") or path.stem)
    return title, body


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    site, html = sys.argv[1].rstrip("/"), Path(sys.argv[2])

    cfg = yaml.safe_load((ROOT / "myst.yml").read_text(encoding="utf-8"))
    project = cfg["project"]
    files = toc_files(project["toc"])

    author = project["authors"][0]["name"]
    affiliation = project["authors"][0]["affiliations"][0]

    index_lines, full_parts, written = [], [], 0

    for n, name in enumerate(files):
        src = ROOT / name
        if not src.exists():
            print(f"✗ {name} is in the toc but not on disk")
            return 1
        title, body = as_markdown(src)

        # The first toc entry is the site root; every other file gets its stem as slug.
        if n == 0:
            page_url, md_rel, page_html = f"{site}/", "index.md", html / "index.html"
        else:
            slug = src.stem
            page_url, md_rel = f"{site}/{slug}/", f"{slug}/index.md"
            page_html = html / slug / "index.html"

        md_text = f"# {title}\n\n{body}".rstrip() + "\n"
        md_url = f"{site}/{md_rel}"
        out = html / md_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(md_text, encoding="utf-8")
        # A second copy at /<slug>.md, because that is the shape a tool guesses first.
        if n > 0:
            (html / f"{src.stem}.md").write_text(md_text, encoding="utf-8")

        if page_html.exists():
            page = page_html.read_text(encoding="utf-8")
            if 'type="text/markdown"' not in page:
                tag = f'<link rel="alternate" type="text/markdown" href="{md_url}"/>'
                page_html.write_text(page.replace("</head>", tag + "</head>", 1), encoding="utf-8")
        else:
            print(f"✗ {page_html} does not exist; the toc and the build disagree")
            return 1

        index_lines.append(f"- [{title}]({md_url})")
        full_parts.append(
            "=" * 80 + f"\nURL: {page_url}\nSOURCE: {md_url}\n" + "=" * 80 + f"\n\n{md_text}"
        )
        written += 1

    # The descriptive title of the book, not the navigation title: llms.txt is read by
    # something deciding whether this document answers a question.
    book_title, _ = as_markdown(ROOT / files[0])
    head = HEADER.format(
        title=book_title, description=project["description"],
        author=author, affiliation=affiliation, site=site,
    )
    (html / "llms.txt").write_text(head + "\n".join(index_lines) + "\n", encoding="utf-8")
    (html / "llms-full.txt").write_text(head + "\n".join(index_lines) + "\n\n"
                                        + "\n\n".join(full_parts), encoding="utf-8")

    size = (html / "llms-full.txt").stat().st_size
    print(f"✓ {written} chapters as Markdown, llms.txt indexed, "
          f"llms-full.txt {size // 1024} KiB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
