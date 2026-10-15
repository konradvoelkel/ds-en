#!/usr/bin/env python3
"""Check that the PDF export's article list still matches the project's toc.

Why this exists: `myst.yml` holds the structure of the book twice. Once as `project.toc`,
which drives the web edition, and once as `project.exports[].articles`, which drives the
PDF. The duplication is not pretty but it is forced: without an explicit article list MyST
takes the whole toc and merely drops its first entry, and there is no way to exclude a
*single* page from the PDF (not by frontmatter, not by `exclude`, and removing a page from
the toc means it is not built for the web either). Once the article list is set, the part
headings have to be rebuilt by hand with `title`/`level`, or the PDF loses its structure.

The danger is the one that has already hit the German original twice: the PDF silently
loses content, and nobody notices, because nobody holds the PDF against the web edition. A
new chapter in the toc that is missing from `articles` is exactly that case. So this
comparison runs in CI and fails the build rather than waving it through.

Ported from ds-skript's `tools/check_pdf_articles.py` (2026-10-15). The upstream version
has two web-only pages; this edition has one, because `orga.md` is not mirrored here at
all (see `sync/filemap.json`).

    python3 tools/check_pdf_articles.py
"""

import pathlib
import sys

try:
    import yaml
except ImportError:
    sys.exit(
        "PyYAML is missing. Run: uv run --with pyyaml python tools/check_pdf_articles.py\n"
        "(that is how CI runs it too; the book itself gains no dependency for a check script)."
    )

# Pages that deliberately exist only in the web edition:
#   landing-page.md  the opening, the table of contents and the licence. MyST would drop it
#                    as the first toc entry anyway; the book's own licence notice therefore
#                    lives in the LaTeX template, not here.
WEB_ONLY = {"landing-page.md"}


def toc_files(toc):
    for entry in toc:
        if "file" in entry:
            yield entry["file"]
        for child in entry.get("children", []):
            yield from toc_files([child])


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    cfg = yaml.safe_load((root / "myst.yml").read_text(encoding="utf-8"))
    project = cfg["project"]

    from_toc = list(toc_files(project["toc"]))
    expected = [f for f in from_toc if f not in WEB_ONLY]

    pdf = [e for e in project.get("exports", []) if e.get("format") == "pdf"]
    if len(pdf) != 1:
        sys.exit(f"ERROR: expected exactly one PDF export, found {len(pdf)}.")
    articles = pdf[0].get("articles")
    if not articles:
        sys.exit(
            "ERROR: the PDF export has no articles list. Without one MyST takes the whole "
            "toc, and the part headings are lost."
        )

    have = [a["file"] for a in articles if "file" in a]

    problems = []
    only_toc = [f for f in expected if f not in have]
    if only_toc:
        problems.append(
            "These pages are in the toc but missing from the PDF export -- they would be "
            "invisible in the printed book:\n  " + "\n  ".join(only_toc)
        )
    only_export = [f for f in have if f not in from_toc]
    if only_export:
        problems.append(
            "These pages are in the PDF export but not in the toc:\n  " + "\n  ".join(only_export)
        )
    forbidden = [f for f in have if f in WEB_ONLY]
    if forbidden:
        problems.append(
            "These pages are meant to be web-only but appear in the PDF export:\n  "
            + "\n  ".join(forbidden)
        )
    if have != expected and not problems:
        problems.append(
            "The order in the PDF differs from the toc:\n  toc:    "
            + ", ".join(expected)
            + "\n  export: "
            + ", ".join(have)
        )

    # The part headings have to be maintained alongside, or the PDF is flat.
    parts_toc = [e["title"] for e in project["toc"] if "children" in e]
    parts_exp = [a["title"] for a in articles if "title" in a]
    if parts_toc != parts_exp:
        problems.append(
            "The part headings do not match:\n  toc:    "
            + ", ".join(parts_toc)
            + "\n  export: "
            + ", ".join(parts_exp)
        )

    if problems:
        print("myst.yml: the toc and the PDF export do not agree.\n")
        for p in problems:
            print(p + "\n")
        print(
            "Adding or reordering a chapter has to happen in both places. If a page is "
            "meant to be web-only, it belongs in WEB_ONLY in this script."
        )
        return 1

    print(
        f"myst.yml is consistent: {len(have)} chapters in the same order in toc and PDF, "
        f"{len(parts_toc)} part headings, web-only: {', '.join(sorted(WEB_ONLY))}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
