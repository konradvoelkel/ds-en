#!/usr/bin/env python3
"""Date every page and every sitemap entry with when it last actually changed.

    python3 tools/freshness.py <html-dir> [--check]

Run after the HTML build and **before** `inject_jsonld.py`, which reads the date back out
of the page rather than computing it twice -- the same arrangement by which it already
reads the preview card back out of `og:image`.

Ported from ds-skript `tools/freshness.py` (commit e229a9d, 2026-10-16), which was written
there first in response to a GEO assessment of both live editions. The design decisions
below are that file's; what differs here is recorded under "The date is this edition's".


Why at all
----------

The book is maintained continuously and **not one page said so**. Measured against the
live site on 2026-10-16, before this: no `article:modified_time` on any of the 30 pages,
`<lastmod>` in **zero of 30** sitemap entries, and no `dateModified` in the landing page's
structured data. Recency is one of the strongest selection signals for AI answer systems,
and this edition had it and was giving it away.

It weighs more here than in the German edition: this is the translation that is supposed
to travel, and the domain has only served since 2026-10-15, so there is no history for a
crawler to infer a cadence from.


Where the date comes from
-------------------------

From `git log` of the **source file**, never from the build clock. A build on Tuesday does
not make a chapter from 2024 fresh, and a date asserting that it does is worse than no
date at all -- it is the same failure as the sitemap that pointed at localhost: a
confident, checkable, wrong claim.

So there is deliberately **no fallback to the clock**. If git has nothing for a file, this
script stops rather than inventing something plausible.

Which means the job needs the **full history**, and `fetch-depth: 0` in `pages.yml` is
mandatory. How a shallow clone fails here is worth knowing precisely, because it is not
how the original says: `actions/checkout` fetches exactly one commit, and against a commit
with no parent git reports every file as modified by it, so `git log` answers for all
thirty files -- with HEAD's timestamp. Nothing is missing, so nothing aborts; every page
simply claims to have changed at the moment of the deploy. `refuse_shallow()` below
therefore asserts the depth directly rather than inferring it from a missing answer.


The date is this edition's, not the original's
----------------------------------------------

In ds-en the git date is the date of the **translation** commit, not of the German commit
it renders. That is a decision, not an inevitability, and it is this one deliberately:

* `article:modified_time` and `<lastmod>` describe *this document at this URL*. The
  English page changed on the day it was written or revised. That is simply true.
* `<lastmod>` tells a crawler when to come back for *this* URL. The German date would
  announce a change to a page that did not change, and would sometimes date an English
  page to before it existed.
* It needs no cross-repository plumbing. The alternative -- carrying the original's dates
  across `sync/filemap.json` -- is buildable, and would make this edition's dates depend
  on a server that CI already cannot reach reliably (see `checks.yml` on why the German
  clone was removed from it).

The honest cost: a commit that changes only this edition -- today's KaTeX fix to the
degree symbol, say -- refreshes the date although the substance did not move. It is still
not a false claim; the page did change. The opposite error, a page that silently keeps a
date from before it was rewritten, is the one worth avoiding.


The toc comes from config.json, not myst.yml
---------------------------------------------

Kept from the original, where the reason was that its `pages` job runs on
python:3.13-alpine without PyYAML. That reason does not apply here -- this workflow
installs PyYAML for `llms_txt.py` already -- but config.json is the better source anyway:
it is the build's own description of what it built, so a drift between the toc and the
artifact shows up as the mismatch it is, and this step needs no dependency at all. It is
also the same toc, so the two editions stay comparable.


--stamp-source: the visible date, on the landing page only
----------------------------------------------------------

    python3 tools/freshness.py --stamp-source      # before the build, not after

Everything above writes into the *built* HTML. A date a reader can see cannot be done that
way: the theme re-renders the page header from the hydration payload, so a line written
into the markup is gone after hydration -- the trap documented at length in
`tools/head_meta.py`. This edition recorded that as a reason to have no visible date at
all; ds-skript found the way round it in `dedfd0b` and this is the port, which is the
first thing to travel in that direction on its own merits rather than as a correction.

The route is the *source*: write `date:` into the landing page's frontmatter before MyST
runs, and the theme renders it like any other frontmatter field -- through the payload,
so hydration keeps it.

**The landing page only**, which is the decision worth preserving. A project-level `date`
in `myst.yml` would print the same day on all 30 pages, and most of them would then
assert a date their source does not support. On the title page "as of" is a true statement
about the edition as a whole, so that page gets the newest date in the book and no other
page gets one.

Run before `myst build`, and before the PDF export too -- here that is automatic, since
the PDF is built first in the same job, so one call covers both.

One cost ds-skript paid consciously and this edition does not pay at all: the theme
formats the date in hard-coded English ("October 16, 2026"), `language: de` does not change
it, and a German string is silently discarded. For an English edition that is simply the
right format.

It edits a tracked file, so a local run leaves `landing-page.md` dirty. In CI that is the
point; locally, `git checkout landing-page.md` afterwards.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META = '<meta property="article:modified_time" content="{date}"/>'


def _git(args: list[str]) -> subprocess.CompletedProcess:
    """Run git, turning "git is not here at all" into one message, in one place.

    Both callers below need this: refuse_shallow() runs first, so without it a missing git
    dies there with a bare FileNotFoundError naming nothing useful -- which is exactly the
    outage ds-skript had in 5b7818b, where python:3.13-alpine ships no git.
    """
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    except FileNotFoundError:
        raise SystemExit(
            "::error::git is not installed, so no date can be read from the history. "
            "ubuntu-latest ships git; a slim container image may not, and then this step "
            "needs it installed before it runs."
        )


def refuse_shallow() -> None:
    """Stop if the repository is a shallow clone, before reading a single date.

    This check is **not** in the original, and it is the one thing here that had to be
    added rather than ported. Upstream relies on `git log` returning *nothing* for a file
    that a shallow clone cannot see -- which is what happens under GitLab's default
    `GIT_DEPTH: 20`, where a file untouched for twenty commits has no entry in the
    truncated history.

    `actions/checkout` is shallow in a different way: `fetch-depth: 1` fetches exactly one
    commit, and against a commit with no parent git reports *every* file as modified by
    it. So `git log -1 -- <file>` answers for all thirty, with HEAD's timestamp, and the
    script sails through and reports success.

    Measured, in a `git clone --depth 1` of this repository: **all 30 pages dated
    2026-10-16T10:18:10, the deploy commit's own second**, where the real dates span three
    days. That is precisely the build-time date this file exists to refuse, arrived at by
    the one route the upstream guard does not cover -- and silent, because the output
    looks exactly like a correct run.

    So the depth is asserted directly instead of being inferred from a missing answer.
    Reported back in UPSTREAM-NOTES.md.
    """
    if _git(["rev-parse", "--is-shallow-repository"]).stdout.strip() == "true":
        raise SystemExit(
            "::error::this is a shallow clone, so git would report HEAD's date for every\n"
            "  file and every page would claim to have changed at the moment of the\n"
            "  deploy. The job needs\n"
            "      - uses: actions/checkout@v4\n"
            "        with:\n"
            "          fetch-depth: 0\n"
            "  Nothing is invented here: a build-time date would claim a chapter is fresh\n"
            "  because the build is."
        )


def toc_files(toc) -> list[str]:
    """Every file of the table of contents, in reading order."""
    out: list[str] = []
    for entry in toc:
        if "file" in entry:
            out.append(entry["file"])
        for child in entry.get("children", []):
            out.extend(toc_files([child]))
    return out


def project(html: Path) -> dict:
    cfg = json.loads((html / "config.json").read_text(encoding="utf-8"))
    return cfg["projects"][0]


def git_date(name: str) -> str:
    """ISO-8601 date of the last commit that touched this file.

    Three distinct failures, kept distinct: git absent (in `_git`), git erroring, and git
    simply not knowing the file. Adopted from ds-skript `5b7818b`, which separated them
    after the first version cost half an hour of looking in the wrong direction: in its CI
    container a *permissions* error was reported as "shallow clone", advice pointing the
    opposite way. Here that would be worse still, now that refuse_shallow() has already
    ruled the shallow case out -- a second, contradictory shallow-clone message would be
    actively misleading.
    """
    res = _git(["log", "-1", "--format=%cI", "--", name])
    if res.returncode != 0:
        raise SystemExit(f"::error::git failed for {name}:\n  {res.stderr.strip()}")
    date = res.stdout.strip()
    if not date:
        raise SystemExit(
            f"::error::git has no date for {name}.\n"
            f"  With a shallow clone that is the normal case, and actions/checkout is\n"
            f"  shallow by default. The job needs\n"
            f"      - uses: actions/checkout@v4\n"
            f"        with:\n"
            f"          fetch-depth: 0\n"
            f"  Nothing is invented here: a build-time date would claim a chapter is\n"
            f"  fresh because the build is."
        )
    return date


def pages(html: Path) -> list[tuple[str, Path, str]]:
    """(slug, index.html, date) per page. The first toc entry is the landing page."""
    out = []
    for n, name in enumerate(toc_files(project(html)["toc"])):
        slug = "" if n == 0 else Path(name).stem
        target = html / "index.html" if n == 0 else html / slug / "index.html"
        if not target.exists():
            raise SystemExit(f"::error::{target} is missing; the toc and the build disagree")
        out.append((slug, target, git_date(name)))
    return out


def book_date(html: Path) -> str:
    """The newest page date -- the date of the work as a whole."""
    return max(date for _, _, date in pages(html))


def stamp_html(entries) -> int:
    done = 0
    for _, target, date in entries:
        page = target.read_text(encoding="utf-8")
        if "article:modified_time" in page:
            continue
        target.write_text(
            page.replace("</head>", META.format(date=date) + "</head>", 1), encoding="utf-8"
        )
        done += 1
    return done


def stamp_sitemap(html: Path, entries) -> int:
    """Write <lastmod> into every <url> block, matched on the last path segment.

    On the path rather than the full URL so that this step does not care whether the
    origin rewrite in the job runs before or after it.
    """
    path = html / "sitemap.xml"
    xml = path.read_text(encoding="utf-8")
    if "<lastmod>" in xml:
        return 0
    by_slug = {slug: date for slug, _, date in entries}
    hits = 0

    def add(match: re.Match) -> str:
        nonlocal hits
        block, loc = match.group(0), match.group(1)
        slug = loc.rstrip("/").rsplit("/", 1)[-1]
        # A <loc> that is the site root has no slug left after stripping; it is the
        # landing page, which is keyed "".
        date = by_slug.get(slug if slug in by_slug else "")
        if date is None:
            return block
        hits += 1
        return block.replace("</loc>", f"</loc><lastmod>{date}</lastmod>", 1)

    path.write_text(re.sub(r"<url>\s*<loc>([^<]+)</loc>", add, xml), encoding="utf-8")
    return hits


def stamp_source() -> int:
    """Write the edition's date into the landing page's frontmatter, before the build."""
    import yaml  # only this path needs it, and only before the build exists

    refuse_shallow()
    cfg = yaml.safe_load((ROOT / "myst.yml").read_text(encoding="utf-8"))
    files = toc_files(cfg["project"]["toc"])
    # The day, not the second: a timestamp on a title page is noise, and the figure a
    # reader cares about is "which week is this".
    date = max(git_date(f) for f in files)[:10]

    landing = ROOT / files[0]
    text = landing.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"::error::{landing.name} has no frontmatter to put a date in")
    end = text.find("\n---", 4)
    if end < 0:
        raise SystemExit(f"::error::{landing.name}: frontmatter is not closed")

    head, rest = text[:end], text[end:]
    if re.search(r"(?m)^date:", head):
        head = re.sub(r"(?m)^date:.*$", f"date: {date}", head)
    else:
        head = head.rstrip("\n") + f"\ndate: {date}"
    landing.write_text(head + rest, encoding="utf-8")
    print(f"✓ {landing.name}: edition dated {date}")
    return 0


def main() -> int:
    if "--stamp-source" in sys.argv:
        return stamp_source()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    html = Path(args[0])
    refuse_shallow()
    entries = pages(html)

    if "--check" in sys.argv:
        without = [
            str(t) for _, t, _ in entries
            if "article:modified_time" not in t.read_text(encoding="utf-8")
        ]
        stamps = (html / "sitemap.xml").read_text(encoding="utf-8").count("<lastmod>")
        if without or stamps != len(entries):
            print(
                f"::error::{len(without)} pages without a date, "
                f"{stamps} of {len(entries)} sitemap entries with <lastmod>"
            )
            for p in without[:5]:
                print(f"    {p}")
            return 1
        print(f"✓ {len(entries)} pages dated, {stamps} sitemap entries with <lastmod>")
        return 0

    n_html, n_map = stamp_html(entries), stamp_sitemap(html, entries)
    print(
        f"✓ {n_html} pages dated, {n_map} sitemap entries with <lastmod>; "
        f"newest change {book_date(html)[:10]}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
