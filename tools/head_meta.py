#!/usr/bin/env python3
"""Trim the title tags, add the OpenGraph tags MyST omits, preload the fonts, and
lazy-load the figures below the fold.

    python3 tools/head_meta.py <site-url> <html-dir> [--base BASE_URL]

Four things, all of them post-processing on the built HTML, because none of them can
be said in myst.yml or in a chapter's frontmatter.


1. The title tags
-----------------

MyST writes `<title>{page} - {project}</title>`, and this project's title is
`Data Science Lecture Notes from Konrad Voelkel` -- 45 characters, so the suffix costs
48 of the roughly 60 that Google renders. Measured on the live site on 2026-10-16:
**on 29 of 30 pages the suffix was truncated away entirely**. It was paying nothing and
spending two thirds of the line to do it, which also invites Google to rewrite the title
rather than show it.

(It was *not* what truncated the four longest chapter titles. Those are over 60
characters on their own, and the chapter title comes first, so the suffix cannot push it
out -- it can only fail to fit after it. Leaving those four as they are is Konrad's
decision of 2026-10-15, recorded in SEO-NOTES.md section 4, and this changes nothing
about it.)

So chapter pages lose the suffix and keep their own title, which is the half that
carries the search terms and which was written to stand alone. The landing page keeps
the full project title, because there it *is* the title rather than a suffix.

The brand is not lost by this. Google derives the site name for the result header from
og:site_name and the structured data, both of which say it -- which is the other reason
og:site_name is added below.

**The suffix is read out of the landing page, never hardcoded.** index.html's title is
the project title on its own, so renaming the book in myst.yml keeps this working and
cannot leave a stale string behind. Same reasoning as the CNAME being derived from
SITE_ORIGIN in pages.yml.

Editing the markup is only half of it, because the theme re-renders the title from the
hydration payload -- see `strip_payload_title` below, which is the half that makes the
change survive in a browser, and so in Google.

`site.title` in myst.yml is a real alternative for the suffix and was tested: it sets
the HTML title independently of `project.title`, so it would not touch the PDF. It is
not used because it is one string for both jobs -- it becomes the chapter suffix *and*
the landing page's entire title -- and the two want different lengths.


2. og:url and og:site_name
--------------------------

MyST emits og:title, og:description and og:image but neither og:url nor og:site_name.
og:url is what a platform treats as the canonical identity of a shared link, so without
it two spellings of the same URL become two cards with two comment threads; og:site_name
is what puts the book's name on the card and feeds Google's site-name signal.

og:url gets the same URL the canonical does -- with the trailing slash, the form that
answers 200.


3. The font preload
-------------------

The two woff2 files are same-origin since 2026-10-16, but a font referenced from a
stylesheet is still discovered only after that stylesheet has been fetched and parsed.
The preload moves them to depth one. `crossorigin` is required even though they are
same-origin: font requests are made in CORS mode, and a preload whose mode does not
match the eventual request is fetched twice instead of once -- the one mistake that
turns this optimisation into a pessimisation.


4. loading="lazy" on the figures -- and the preloads that would have cancelled it
---------------------------------------------------------------------------------

226 images across the 30 pages, none of them lazy. descriptive-statistics loads 6.4 MB
of them before the load event, for a page whose figures are nearly all below the fold.

The first image inside <main> stays eager, because lazy-loading the LCP element delays
exactly the paint that is being measured. Everything after it gets `loading="lazy"` and
`decoding="async"`. The navigation logo is outside <main> and is never touched.

**The attribute on its own would have done nothing.** MyST emits a
`<link rel="preload" as="image">` in the head for *every* image on the page -- twelve of
them on kmeans, and that is the real reason a chapter pulls its whole figure set before
the load event. A preloaded image is fetched at once whatever `loading` says; the two
tags contradict each other and the preload wins. So the preload is removed for exactly
the images that were made lazy, and kept for the two that should have it: the logo,
which is outside <main>, and the first figure, which is the LCP candidate. Pairing the
removal to the set of lazied URLs rather than dropping all preloads is what keeps those
two.

Only the <main> slice is rewritten. The rest of the document holds MyST's hydration
payload -- the whole page again as JSON inside a <script> -- and a regex let loose on
that would edit strings the browser parses as data.


Running it twice
----------------

It is idempotent, and it checks postconditions rather than its own edits: every page
must end up with an og:url, and no chapter title may still carry the suffix. A second
run is a no-op that still passes, while markup MyST has moved under us fails -- which
is the case the check is actually for.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys

FONTS = ("inter-latin.woff2", "jetbrains-mono-latin.woff2")


def page_url(site: str, rel: pathlib.PurePath) -> str:
    """The URL that answers 200: with the trailing slash, as the canonical has it."""
    return f"{site}/" if str(rel) == "." else f"{site}/{rel}/"


def project_title(index_html: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", index_html, re.S | re.I)
    if not m:
        sys.exit("::error::the landing page has no <title>; cannot derive the suffix")
    title = m.group(1).strip()
    if not title:
        sys.exit("::error::the landing page's <title> is empty")
    return title


def trim_titles(doc: str, suffix: str) -> tuple[str, bool]:
    """Drop ' - <project>' from <title> and og:title. Returns (doc, changed)."""
    changed = False

    def title_sub(m: re.Match) -> str:
        nonlocal changed
        inner = m.group(1)
        if inner.strip().endswith(suffix):
            changed = True
            return f"<title>{inner.strip()[: -len(suffix)].strip()}</title>"
        return m.group(0)

    doc = re.sub(r"<title[^>]*>(.*?)</title>", title_sub, doc, count=1, flags=re.S | re.I)

    # og:title carries the same suffix, attribute-escaped. Escape the suffix the same
    # way before matching, or a title holding an & or a quote silently fails to trim.
    esc = html.escape(suffix, quote=True)

    def og_sub(m: re.Match) -> str:
        nonlocal changed
        content = m.group(1)
        if content.endswith(esc):
            changed = True
            return m.group(0).replace(content, content[: -len(esc)].strip())
        return m.group(0)

    doc = re.sub(
        r'<meta property="og:title" content="([^"]*)"\s*/?>', og_sub, doc, count=1
    )
    return doc, changed


def strip_payload_title(doc: str, name: str) -> tuple[str, bool]:
    """Blank the project title inside the hydration payload, for chapter pages.

    Editing <title> in the markup is only half the job. The page is a Remix app: the
    whole document is also serialised into `window.__remixContext`, and on hydration the
    theme re-renders the title from *that*, putting the suffix straight back. The
    server-rendered head and the hydrated head then disagree, and since Google renders
    the page before indexing it, the one that loses is the one we edited.

    Measured here first: with `project.title` blanked in the payload the hydrated title
    is the chapter title alone, and the logo, the sidebar, the part names and the
    previous/next labels in the footer all still render -- those come from their own
    fields (`short_title`, `footer.navigation.*`), not from this one.

    Only the chapters. The landing page's title *is* the book's title.
    """
    key = "window.__remixContext = "
    i = doc.find(key)
    if i < 0:
        return doc, False
    start = i + len(key)
    try:
        payload, length = json.JSONDecoder().raw_decode(doc, start)
    except ValueError:
        return doc, False

    changed = False
    for route in (payload.get("state", {}).get("loaderData") or {}).values():
        if not isinstance(route, dict):
            continue
        for holder in ("project", "config"):
            node = route.get(holder)
            if isinstance(node, dict) and node.get("title") == name:
                node["title"] = ""
                changed = True
    if not changed:
        return doc, False

    # Re-serialised compactly. The two replacements keep the JSON safe *as a JavaScript
    # literal inside a <script>*: a literal "<" could close the tag early, and U+2028 /
    # U+2029 are ordinary characters in JSON but line terminators in JavaScript. Both
    # are written as \u escapes, which JSON reads back as the same characters.
    out = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    out = out.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return doc[:start] + out + doc[start + length :], True


def head_tags(
    url: str, site_name: str, base: str, lang: str, is_landing: bool
) -> list[tuple[str, str]]:
    """The tags as (marker, tag): the marker says whether the page already has it.

    Checked **per tag**, not once for all of them. A single gate on og:url -- which is
    what stood here until 2026-10-16 -- means that the moment a new tag is added, every
    artifact an earlier version already processed silently misses it, and the
    postcondition then fails with no further run able to heal it. ds-skript hit exactly
    that adding these card tags (7f0bac4) and fixed it the same way; this is the port,
    made before adding the tags rather than after.
    """
    # de -> de_DE: OpenGraph wants the underscore locale code, not the language subtag.
    locale = {"de": "de_DE", "en": "en_US"}.get(lang, lang)
    alternate = "de_DE" if locale == "en_US" else "en_US"
    tags = [
        (
            'property="og:url"',
            f'<meta property="og:url" content="{html.escape(url, quote=True)}"/>',
        ),
        (
            'property="og:site_name"',
            f'<meta property="og:site_name" content="{html.escape(site_name, quote=True)}"/>',
        ),
        # "book" on the title page, "article" on the chapters. With no og:type at all a
        # platform assumes "website", which is what a shop's front page would be.
        (
            'property="og:type"',
            f'<meta property="og:type" content="{"book" if is_landing else "article"}"/>',
        ),
        ('property="og:locale"', f'<meta property="og:locale" content="{locale}"/>'),
        # The card's counterpart to the hreflang pair: it tells a platform the same thing
        # exists in German, as tools/hreflang.py tells search engines.
        (
            'property="og:locale:alternate"',
            f'<meta property="og:locale:alternate" content="{alternate}"/>',
        ),
    ]
    tags += [
        (
            f'href="{base}/fonts/{f}"',
            f'<link rel="preload" href="{base}/fonts/{f}" as="font" '
            f'type="font/woff2" crossorigin/>',
        )
        for f in FONTS
    ]
    return tags


# The card tags every page must end up with, for the postcondition below.
CARD_MARKERS = (
    'property="og:url"',
    'property="og:site_name"',
    'property="og:type"',
    'property="og:locale"',
    'property="og:locale:alternate"',
)


def lazy_load_figures(doc: str) -> tuple[str, set[str]]:
    """Lazy-load every <img> inside <main> but the first.

    Returns the document and the set of src URLs that were made lazy, so the caller can
    drop the matching preloads -- without which the attribute has no effect at all.
    """
    m = re.search(r"<main\b[^>]*>.*?</main>", doc, re.S | re.I)
    if not m:
        return doc, set()

    main = m.group(0)
    lazied: set[str] = set()
    seen = 0

    def img_sub(tag: re.Match) -> str:
        nonlocal seen
        seen += 1
        t = tag.group(0)
        if seen == 1:  # the LCP candidate stays eager, and keeps its preload
            return t
        src = re.search(r'\bsrc="([^"]*)"', t, re.I)
        if src:
            lazied.add(src.group(1))
        if re.search(r"\bloading=", t, re.I):
            return t
        return t[:-1].rstrip() + ' loading="lazy" decoding="async"' + t[-1]

    main_new = re.sub(r"<img\b[^>]*?/?>", img_sub, main, flags=re.I)
    return doc[: m.start()] + main_new + doc[m.end() :], lazied


def drop_image_preloads(doc: str, srcs: set[str]) -> tuple[str, int]:
    """Remove `<link rel="preload" as="image">` for images that are now lazy."""
    if not srcs:
        return doc, 0
    n = 0

    def link_sub(m: re.Match) -> str:
        nonlocal n
        tag = m.group(0)
        if 'as="image"' not in tag:
            return tag
        href = re.search(r'\bhref="([^"]*)"', tag)
        if href and href.group(1) in srcs:
            n += 1
            return ""
        return tag

    doc = re.sub(r'<link\b[^>]*rel="preload"[^>]*/?>', link_sub, doc, flags=re.I)
    return doc, n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("html_dir")
    ap.add_argument("--base", default="", help="BASE_URL, the path the site is served from")
    ap.add_argument("--lang", default="en", help="the edition's language, for og:locale")
    args = ap.parse_args()

    site = args.site.rstrip("/")
    root = pathlib.Path(args.html_dir)
    index = root / "index.html"
    if not index.exists():
        sys.exit(f"::error::{index} does not exist; run this after the HTML build")

    name = project_title(index.read_text(encoding="utf-8"))
    suffix = f" - {name}"

    pages = sorted(root.rglob("index.html"))
    trimmed = n_lazy = n_preload = n_tags = 0
    chapters = 0

    for f in pages:
        rel = f.parent.relative_to(root)
        url = page_url(site, rel)
        doc = f.read_text(encoding="utf-8")

        # The landing page's title *is* the project title; only chapters carry it as
        # a suffix.
        if str(rel) != ".":
            chapters += 1
            doc, changed = trim_titles(doc, suffix)
            trimmed += changed
            doc, _ = strip_payload_title(doc, name)

        missing = [
            tag
            for marker, tag in head_tags(url, name, args.base, args.lang, str(rel) == ".")
            if marker not in doc
        ]
        if missing:
            if "</head>" not in doc:
                sys.exit(f"::error::{f} has no </head>")
            doc = doc.replace("</head>", "".join(missing) + "</head>", 1)
            n_tags += len(missing)

        doc, lazied = lazy_load_figures(doc)
        doc, dropped = drop_image_preloads(doc, lazied)
        n_lazy += len(lazied)
        n_preload += dropped

        f.write_text(doc, encoding="utf-8")

    # Postconditions, not a tally of this run's edits: a second run is a legitimate
    # no-op, while markup that has moved under us must still fail.
    for f in pages:
        doc = f.read_text(encoding="utf-8")
        rel = f.parent.relative_to(root)
        for marker in CARD_MARKERS:
            if marker not in doc:
                sys.exit(f"::error::{f} still has no {marker}")
        title = re.search(r"<title[^>]*>(.*?)</title>", doc, re.S | re.I)
        if str(rel) != "." and title and title.group(1).strip().endswith(suffix):
            sys.exit(f"::error::{f} still carries the title suffix")
        # The markup being right is not enough: hydration re-renders the title from the
        # payload, so a project title left in there would undo this in the browser --
        # and in Google, which renders before it indexes.
        if str(rel) != "." and re.search(
            r'"(?:project|config)":\{[^{}]*"title":"' + re.escape(name), doc
        ):
            sys.exit(f"::error::{f} would get its title suffix back on hydration")

    print(
        f"head_meta: {len(pages)} pages, {trimmed}/{chapters} titles trimmed "
        f'(suffix "{suffix.strip()}"), {n_tags} card tags added, '
        f"{n_lazy} figures lazy-loaded, {n_preload} image preloads dropped"
    )


if __name__ == "__main__":
    main()
