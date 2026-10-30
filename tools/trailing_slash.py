#!/usr/bin/env python3
"""Point every chapter link at the URL that answers 200: the one with the trailing slash.

    python3 tools/trailing_slash.py <html-dir> [--base BASE_URL]
    python3 tools/trailing_slash.py <html-dir> [--base BASE_URL] --check

Run in `pages.yml` after `head_meta.py` -- it is the last step that writes into the pages,
because it rewrites hrefs in the markup and in the hydration payload alike and nothing
after it should put one back -- and again with `--check` under the artifact gate, beside
`freshness.py --check`.

Ported from ds-skript `tools/trailing_slash.py` (commit de0c3bc, 2026-10-29), which found
the three places and the one limit. What differs here is the host, the hydration and the
payload parser, and each is recorded in its own section below.


Why at all
----------

MyST links a chapter as `/kmeans`. GitHub Pages serves a directory per chapter, and
answers that address with a **301** to `/kmeans/` (`cache-control: max-age=600`), the way
GitLab Pages answers ds-skript's with a 302. Measured on the live site on 2026-10-30, five
runs on one connection:

| Form | median |
|---|---|
| `/kmeans` (301, then 200) | 0.194 s |
| `/kmeans/` (200) | 0.115 s |

About **80 ms on the first click of every internal link**, then cached for ten minutes.
The served `/kmeans/` had 16 chapter hrefs, all without the slash; after hydration 14, all
without. Canonical, sitemap, `og:url` and hreflang have carried the slash since SEO-NOTES
§1 and §10, so this is not an indexing question: it is a round trip per click, paid by
every reader without JavaScript and by every crawler that follows a link rather than the
sitemap. There is no way to make the slashless form answer 200 instead -- GitHub Pages has
no `_redirects`, and ds-skript's attempt on GitLab (f7ccf9f, withdrawn in a6b7c33) found
the host resolves the directory before any rule runs -- so the links move to the form that
does.


Three places, not one
---------------------

A href fixed in the markup alone does not survive, and ds-skript measured how: with a
proxy serving an edited page against the real bundle, markup with the slash and payload
without gives a DOM **without** afterwards, because the theme renders the article from the
payload. There the hydration fails on every page (React #418) and the overwrite comes with
it. Here the hydration succeeds (SEO-NOTES §20), so the same fixture was measured again on
2026-10-30, in a browser, on a copy of this build with the slash in the markup only:

| moment | chapter hrefs on `/kmeans/` with the slash |
|---|---|
| after hydration | 14 of 14 -- React leaves the served attributes as they are |
| after the first re-render (the theme toggle) | **0 of 14** -- every href now comes from the payload |

So the window is longer here and closes on the first interaction that re-renders the
page. The slash is written in three places:

| place | what | field |
|---|---|---|
| the markup | every `href="<base>/<slug>"` outside the payload | `<a href>` in the article, the sidebar and the footer |
| the hydration payload | `window.__remixContext`, the loaderData routes | mdast `link.url`; `page.footer.navigation.{prev,next}.url` |
| the page JSON | `<slug>.json` beside each page | the same two fields |

The page JSON is **not** what a click renders. In a static build the theme gives every
Link `reloadDocument`, so a chapter click is a full document load; and nothing fetched a
`.json` on a hover or a click either (measured: the hover card is built from
`config.json`'s page entry, and Remix's prefetch on hover asks for `<slug>/?_data=routes/$`,
which this host answers with the HTML). The JSON carries the same two fields for the
readers it does have -- a cross-page reference fetches its target's `dataUrl`, and MyST's
own tooling reads these files -- and for the reason `head_meta.py` sets `page.domain` in
it too: two copies of one value can only drift.

Which payload field produces which href was measured in ds-skript with a marker per field
(`?marker=N` written into the payload, then searched for in the DOM): links in the article
from mdast `link.url`, the footer from `footer.navigation`, the sidebar from
`config.projects[].pages[].slug`. The bundle here says the same, read rather than
measured: the sidebar's `path` is `"/" + slug`.

The payload parser is `head_meta.py`'s. `read_payload` finds and decodes the context,
`edit_payload` writes it back as a `<script>`-safe literal, `routes` yields the loaderData
routes -- imported, not copied, so there is one parser and one place its `raw_decode`
lesson lives (the index-not-length trap that once truncated every page of this edition).
The markup rewrite runs **outside the payload's span only**: `href="` cannot occur inside
the JSON, where a quote is `\\"`, but the rewrite does not depend on that.


What a click costs, before and after
------------------------------------

Every Link in a static build reloads the document, and Remix prefetches the route on
hover. Measured in the server log of a local copy, served by Python's `http.server`, which
answers `/kmeans` with the same 301 GitHub Pages does:

| | hover (prefetch) | click (document) |
|---|---|---|
| before | `/x?_data=…` **301**, `/x/?_data=…` 200 | `/x` **301**, `/x/` 200 |
| after | `/x/?_data=…` 200 | `/x/` 200 |

Four requests become two, and the live host answers the four the same way (`curl`,
2026-10-30: both slashless forms 301, `max-age=600`). The prefetch is Remix's and buys
nothing on a static host either way -- it gets HTML back -- but without the slash it is a
redirect first.


The sidebar stays without the slash, and that is a decision
-----------------------------------------------------------

The slug would be the handle for the sidebar's hrefs. A slash on it reaches the DOM, and
ds-skript measured what it costs (93 slugs in all three copies of the configuration):

* **The hover cards of every link in the article are gone.** The theme finds the target
  page with `pages.find(s => s.slug === path)`, where `path` is the first segment of the
  link URL. With the slug `kmeans/` nothing is found, and the link renders as a plain
  `a.link` instead of `a.hover-link`: no title, no description, no thumbnail. All four
  internal links of the German `/kmeans/` fell out of `hover-link`.
* **The group of the current page no longer opens.** The sidebar strips a trailing slash
  from the *location* and compares with `path`, which would now have one. 11 entries
  became 3.

The bundle this edition ships does both the same way (chunk-LS4ALTVG.js: the lookup
splits the URL on `/` and compares the first segment with the slug; the sidebar's match
is `endsWith("/") ? slice(0, -1) : t` on the location). Measured here on the processed
build, 2026-10-30, `/kmeans/` in a browser:

| moment | article | footer | sidebar |
|---|---|---|---|
| after hydration | 4 of 4 with the slash | 2 of 2 | 8 of 8 |
| after the theme toggle | 4 of 4 | 2 of 2 | **0 of 8** -- back to the slug |

The four article links are `a.hover-link` before and after, and the card opens on hover
with the target's title and description, after the re-render too. So the slug is left
alone, and after the first re-render the sidebar's hrefs are the ones that fall back to
the redirecting form: 6 of 14 keep the slash where the German kept 285 of 502. That is
most of a finding and not all of it; the rest is a patch to the theme, not to the artifact.


What is deliberately left alone
-------------------------------

Only `<base>/<slug>` for a slug in the build's own `config.json` -- the same list
`freshness.py`, `head_meta.py` and `inject_jsonld.py` read -- and only when nothing
follows the slug. A slash on anything else would be a new redirect instead of a saved
one. Counted in this artifact after the deploy chain, and left as they are:

| form | why | here |
|---|---|---|
| `/not-a-chapter` | not in the chapter list; `/` would be a new 301 | 0 |
| `/kmeans#section` | a fragment; the browser requests `/kmeans` | 0 |
| `/kmeans?x=1` | a query | 0 |
| `/kmeans.md`, `/kmeans.json` | a file, not a page | `.json` in `dataUrl`, untouched |
| `https://.../kmeans/` | absolute; the canonical, hreflang, `og:url`, alternate and JSON-LD steps write these, all with the slash | 87, untouched |
| `/Kmeans` | a capital, so not a slug | 0 |

The German required a link node's `internal` flag as well. Every one of the 190 chapter
links in this build carries it, so the flag selects nothing the URL rule does not, and a
node that had the URL without the flag would be a href the markup rule fixed and the
payload rule left behind -- the one combination that does not survive the first re-render. The URL
is the condition, in all three places.


What the postcondition checks
-----------------------------

The result, not the tally of this run's edits: a second run changes nothing and must still
pass. Re-read from disk after writing, and under `--check` without writing anything:

* no `href="<base>/<slug>"` outside the payload of any page;
* no `link.url` or `footer.navigation.*.url` of the form `/<slug>` in any payload -- the
  fields are searched for the same way the writing run searched for them, on a copy that
  is thrown away;
* the same in every page JSON, and exactly one page JSON per page: a build that stops
  writing them, or writes them without an mdast, is a build to look at;
* every payload still decodes and every page still ends in `</html>`: the one edit here
  that could truncate a page is the payload write, and that failure once shipped.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

# The payload parser is head_meta.py's, not a second one -- see "Three places, not one".
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from head_meta import edit_payload, read_payload, routes  # noqa: E402

PAYLOAD_KEY = "window.__remixContext = "
HREF = re.compile(r'(\bhref=")([^"]*)(")')


def chapter_slugs(root: pathlib.Path) -> set[str]:
    """The slugs of every chapter, from the build's own `config.json`.

    The same list `freshness.py`, `head_meta.py` and `inject_jsonld.py` read. Without it
    every path would be a guess, and a slash on a guess is a new redirect, so the tool
    stops rather than proceed without the file.
    """
    cfg = root / "config.json"
    if not cfg.exists():
        sys.exit(f"::error::{cfg} is missing; without the chapter list every path is a guess")
    try:
        pages = json.loads(cfg.read_text(encoding="utf-8"))["projects"][0]["pages"]
    except (ValueError, KeyError, IndexError, TypeError) as e:
        sys.exit(f"::error::{cfg} has no projects[0].pages ({e})")
    slugs = {p["slug"] for p in pages if isinstance(p, dict) and isinstance(p.get("slug"), str)}
    if not slugs:
        sys.exit(f"::error::{cfg} names no slug at all")
    # A slug with a slash in it is not a shape this was written for: one at the end would
    # get a second slash here and lose the sidebar its hover cards (see the docstring), one
    # in the middle is a path, and MyST writes neither. Refused rather than guessed at.
    odd = sorted(s for s in slugs if "/" in s or not s)
    if odd:
        sys.exit(f"::error::{cfg} has a slug with a slash in it, or an empty one: {odd[:3]}")
    return slugs


def without_slash(url, slugs: set[str]) -> bool:
    """Exactly `/<slug>`: a chapter path with nothing after it and no slash at the end.

    Anything else -- a fragment, a query, an extension, an absolute URL, a path that is
    not a chapter -- fails the membership test, because `url[1:]` is then not a slug.
    """
    return isinstance(url, str) and url.startswith("/") and url[1:] in slugs


def fix_hrefs(text: str, base: str, slugs: set[str]) -> tuple[str, int]:
    """Every `href="<base>/<slug>"` in `text` gets its slash. Returns (text, count)."""
    n = 0

    def sub(m: re.Match[str]) -> str:
        nonlocal n
        target = m.group(2)
        if not target.startswith(base + "/") or not without_slash(target[len(base):], slugs):
            return m.group(0)
        n += 1
        return m.group(1) + target + "/" + m.group(3)

    return HREF.sub(sub, text), n


def fix_markup(doc: str, base: str, slugs: set[str]) -> tuple[str, int]:
    """The markup outside the payload's span: head, body, and the module script after it."""
    found = read_payload(doc)
    if found is None:
        return fix_hrefs(doc, base, slugs)
    _, start, end = found
    head, n_head = fix_hrefs(doc[:start], base, slugs)
    tail, n_tail = fix_hrefs(doc[end:], base, slugs)
    return head + doc[start:end] + tail, n_head + n_tail


def fix_fields(node, slugs: set[str]) -> tuple[int, int]:
    """`link.url` and `footer.navigation.{prev,next}.url`, in place. Returns (links, footer).

    Mutates `node`. The slug is not touched, on purpose -- see the docstring. Nothing else
    that carries a chapter URL is either: the context's own `url` is the location Remix
    hydrated at, and a `dataUrl` names a file.
    """
    n_link = n_footer = 0

    def walk(o) -> None:
        nonlocal n_link, n_footer
        if isinstance(o, dict):
            if o.get("type") == "link" and without_slash(o.get("url"), slugs):
                o["url"] += "/"
                n_link += 1
            nav = o.get("navigation")
            if isinstance(nav, dict):
                for k in ("prev", "next"):
                    entry = nav.get(k)
                    if isinstance(entry, dict) and without_slash(entry.get("url"), slugs):
                        entry["url"] += "/"
                        n_footer += 1
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(node)
    return n_link, n_footer


def fix_payload(doc: str, slugs: set[str]) -> tuple[str, int, int]:
    """The two fields in every loaderData route. Returns (doc, links, footer)."""
    counts = [0, 0]

    def mutate(payload: dict) -> bool:
        for route in routes(payload):
            a, b = fix_fields(route, slugs)
            counts[0] += a
            counts[1] += b
        return bool(counts[0] or counts[1])

    doc, _ = edit_payload(doc, mutate)
    return doc, counts[0], counts[1]


def page_jsons(root: pathlib.Path) -> list[tuple[pathlib.Path, dict]]:
    """MyST's `<slug>.json`, one per page: the JSON files beside the pages that carry an mdast.

    `config.json`, `public.json`, `myst.search.json` and `myst.xref.json` carry none and
    are skipped by that test, not by name.
    """
    out = []
    for f in sorted(root.glob("*.json")):
        if not f.is_file():
            continue
        data = json.loads(f.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "mdast" in data:
            out.append((f, data))
    return out


def fix_page(f: pathlib.Path, base: str, slugs: set[str]) -> tuple[int, int, int]:
    """One page, markup and payload. Returns (hrefs, links, footer)."""
    doc = f.read_text(encoding="utf-8")
    if PAYLOAD_KEY in doc and read_payload(doc) is None:
        sys.exit(f"::error::{f} has a hydration payload that does not decode")
    doc, n_href = fix_markup(doc, base, slugs)
    doc, n_link, n_footer = fix_payload(doc, slugs)
    if n_href or n_link or n_footer:
        f.write_text(doc, encoding="utf-8")
    return n_href, n_link, n_footer


def check(root: pathlib.Path, base: str, slugs: set[str]) -> tuple[int, int]:
    """The postcondition, re-read from disk. Returns (pages, page JSON) for the report.

    `fix_fields` mutates what it is given, and that is the test: whatever it still finds
    to change is what the writing run should have changed. It is given a parsed copy that
    is then thrown away; nothing is written here.
    """
    pages = sorted(root.rglob("index.html"))
    if not pages:
        sys.exit(f"::error::no index.html under {root}")
    for f in pages:
        doc = f.read_text(encoding="utf-8")
        if not doc.rstrip().endswith("</html>"):
            sys.exit(f"::error::{f} does not end with </html> -- truncated?")
        found = read_payload(doc)
        if found is None and PAYLOAD_KEY in doc:
            sys.exit(f"::error::{f} has a hydration payload that no longer decodes")
        start, end = (found[1], found[2]) if found else (len(doc), len(doc))
        for m in HREF.finditer(doc[:start] + doc[end:]):
            target = m.group(2)
            if target.startswith(base + "/") and without_slash(target[len(base):], slugs):
                sys.exit(
                    f"::error::{f} links {target} without the slash; GitHub Pages answers"
                    " that with a 301"
                )
        if found:
            n_link = n_footer = 0
            for route in routes(found[0]):
                a, b = fix_fields(route, slugs)
                n_link += a
                n_footer += b
            if n_link or n_footer:
                sys.exit(
                    f"::error::{f} has {n_link} links and {n_footer} footer entries without"
                    " the slash in its hydration payload; the DOM gets them back on the"
                    " next render"
                )
    jsons = page_jsons(root)
    if len(jsons) != len(pages):
        sys.exit(
            f"::error::{len(jsons)} page JSON carry an mdast but there are {len(pages)} pages;"
            " MyST's <slug>.json output has changed shape"
        )
    for f, data in jsons:
        n_link, n_footer = fix_fields(data, slugs)
        if n_link or n_footer:
            sys.exit(
                f"::error::{f.name} has {n_link + n_footer} chapter URLs without the slash;"
                " the next page a reader navigates to is rendered from this file"
            )
    return len(pages), len(jsons)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("html_dir")
    ap.add_argument("--base", default="", help="BASE_URL, the path the site is served from")
    ap.add_argument(
        "--check",
        action="store_true",
        help="write nothing; only check the postcondition on the built artifact",
    )
    args = ap.parse_args()

    root = pathlib.Path(args.html_dir)
    base = "/" + args.base.strip("/") if args.base.strip("/") else ""
    slugs = chapter_slugs(root)

    if args.check:
        n_pages, n_json = check(root, base, slugs)
        print(
            f"✓ trailing_slash --check: {n_pages} pages, {len(slugs)} chapters, {n_json} page"
            f" JSON; no chapter link without the slash in markup, payload or page JSON"
        )
        return

    pages = sorted(root.rglob("index.html"))
    if not pages:
        sys.exit(f"::error::no index.html under {root}")
    n_href = n_link = n_footer = 0
    for f in pages:
        a, b, c = fix_page(f, base, slugs)
        n_href += a
        n_link += b
        n_footer += c
    j_link = j_footer = 0
    for f, data in page_jsons(root):
        a, b = fix_fields(data, slugs)
        if a or b:
            # Compact, the form MyST wrote; the default separators would add kilobytes.
            f.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
        j_link += a
        j_footer += b

    n_pages, n_json = check(root, base, slugs)
    print(
        f"trailing_slash: {n_pages} pages, {len(slugs)} chapters; {n_href} hrefs in the markup,"
        f" {n_link + n_footer} fields in the payload ({n_link} links, {n_footer} footer),"
        f" {j_link + j_footer} in the {n_json} page JSON given the slash; the sidebar's slug"
        f" left alone"
    )


if __name__ == "__main__":
    main()
