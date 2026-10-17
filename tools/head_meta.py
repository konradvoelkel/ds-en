#!/usr/bin/env python3
"""Trim the title tags, add the OpenGraph tags MyST omits, preload the fonts, lazy-load
the figures below the fold, drop the jupyter stylesheets from pages with no jupyter
output, and refuse a preview card too small to be one.

    python3 tools/head_meta.py <site-url> <html-dir> [--base BASE_URL]

Six things, all of them post-processing on the built HTML, because none of them can
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


5. The jupyter stylesheets on pages that have no jupyter output
--------------------------------------------------------------

Twelve of the thirty pages are Markdown chapters with no executed cell on them, and all
thirty load `thebe-core-<hash>.css` -- 87 kB of render-blocking stylesheet for cell
output, run buttons and kernel status that those twelve pages do not contain -- plus
`vendor/jupyter-matplotlib/mpl_widget.css`, which styles the ipympl widget. Both are
dropped where there is nothing for them to style.

The marker is MyST's own `myst-jp` class prefix, which the theme puts on every notebook
block and every output. It is 0 on exactly the twelve Markdown chapters and non-zero on
all eighteen notebook pages, and it is the same partition as MyST's internal
`computable` flag (`computables.length > 0 || kind === Notebook`).

**Not `jp-CodeCell`,** which the SEO audit of 2026-10-17 classified the pages by: thebe
adds that class when it attaches to a cell, and this site configures no kernel server, so
nothing ever attaches. Measured: zero occurrences in all thirty built pages, and zero in
the hydrated DOM of a notebook page as well.

**What this does and does not buy.** The two stylesheets leave the *critical path*: they
are no longer in the document the browser parses before its first paint. They are not
gone from the page. The theme's root route declares them in a Remix `links()` export,
which is a static array with no access to the page's data -- Remix's `links()` cannot see
loader data at all -- so after hydration the client re-adds both tags and fetches them.
Measured on the built site: on a Markdown chapter they are now the last two requests of
the load, after every script, instead of being render-blocking in the head. The
re-insertion is also why this cannot be done for the eighteen notebook pages in reverse,
and why the honest fix is upstream; it is recorded in UPSTREAM-NOTES.md.

This is the half of the audit's item 1.2 that can be done from the markup at all. The
other half -- `thebe-core.min.js`, 359 kB transfer and 1278 kB decoded, which the audit
measured on all thirty pages -- is **not a tag in the document**. It is appended to
document.head at runtime by thebe-react's loader, from an effect with no gate on whether
the page has anything computable, so there is nothing here to strip. That one is
`tools/thebe_gate.py`, and the reasoning is in its docstring.


6. The preview card, and the figures that are not one
-----------------------------------------------------

Every page declares `twitter:card=summary_large_image`, which wants 1200x630. MyST fills
og:image with the page's *first figure* and only falls back to the project thumbnail --
the real card, from `tools/social_card.py` -- when a page has none. Measured on the live
site on 2026-10-17: eleven pages shipped an arbitrary figure as their card, among them
`statistical-tests` at 400x528 (portrait, two thirds under the minimum width),
`expectation-variance` at 555x329, `intro-python` at 518x588 and
`important-continuous-distributions` at 1226x1648. A card under the minimum is cropped,
padded or dropped entirely depending on the platform, and a portrait one is cropped
hardest exactly where a figure carries its caption.

myst.yml already documents the rule for the fallback case ("267x50, under the 200x200
Facebook and LinkedIn need"). It is applied here per page: a figure stays the card only
if it is at least 1200x630 **and** landscape; otherwise the page gets the generic card,
which is 1200x630 by construction and checked as such by `social_card.py --verify` and by
checks.yml.

One more condition, on bytes rather than pixels: `descriptive-statistics` passed the size
rule with a 1600x983 figure that is **1.2 MB**, thirty times the generic card, for an
image that renders at 1200x630 either way. Over 500 kB the figure loses to the card. The
threshold is a judgement and is set where it catches that page and nothing else: the next
largest card on the site is 461 kB, and the honest fix for both is WebP output
(ACTION-PLAN item 3.2), after which the big figures can come back.

The card's own URL is not hardcoded, and neither is its origin. The filename is read off
the landing page, which has no figure of its own and so already carries the project
thumbnail: MyST fingerprints the name, and it emits that one file *twice* under two
hashes of identical bytes, so there is nothing to glob for. The URL written into a page
is then built from the prefix that page's *own* image tag already uses, so this works
both before and after the step in pages.yml that makes og:image absolute, and cannot
invent a second spelling of the origin. Same reasoning as the title suffix being read out
of the landing page.

`<meta name="image">` is rewritten alongside og:image. It is MyST's own generic tag,
carrying the same value, and leaving the two disagreeing about which image describes the
page would be worse than either answer.

And the hydration payload is rewritten alongside both, for the same reason section 1 has
to: the theme re-renders og:image from `page.frontmatter.thumbnail` on hydration, so
markup alone puts the rejected figure back in the rendered DOM. Measured here before the
payload pass existed -- `statistical-tests` served the card and hydrated to the 400x528
figure. A card is read from the markup by every platform that draws one, none of which
runs the script, so this half changes nothing for them; it is Google, which renders
before it indexes, that would have seen the contradiction.


Running it twice
----------------

It is idempotent, and it checks postconditions rather than its own edits: every page must
end up with an og:url, no chapter title may still carry the suffix, no page with no
jupyter output may still link a jupyter stylesheet, and every og:image must be a card
that passes the rule above. A second run is a no-op that still passes, while markup MyST
has moved under us fails -- which is the case the check is actually for.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys

from PIL import Image

FONTS = ("inter-latin.woff2", "jetbrains-mono-latin.woff2")

# The jupyter stylesheets, and the class prefix whose absence says the page has no
# jupyter output for them to style. See section 5.
JUPYTER_MARKER = "myst-jp"
JUPYTER_CSS = re.compile(
    r'<link\b[^>]*href="[^"]*(?:thebe-core[^"]*\.css|jupyter-matplotlib/mpl_widget\.css)"'
    r"[^>]*/?>",
    re.I,
)

# The preview card floor: 1200x630 is what summary_large_image renders, and a card has to
# be landscape to survive the crop. The byte ceiling is argued in section 6.
CARD_MIN_WIDTH, CARD_MIN_HEIGHT = 1200, 630
CARD_MAX_BYTES = 500 * 1024


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


def read_payload(doc: str):
    """The hydration payload, with where it begins and ends. None if there is none.

    The page is a Remix app: the whole document is serialised a second time into
    `window.__remixContext`, and on hydration the theme re-renders the head from *that*.
    Anything edited in the markup that the payload also says has to be edited in both, or
    the server-rendered head and the hydrated head disagree -- and since Google renders
    the page before indexing it, the one that loses is the one we edited.
    """
    key = "window.__remixContext = "
    i = doc.find(key)
    if i < 0:
        return None
    start = i + len(key)
    try:
        # raw_decode returns the index in `doc` where the JSON *ends*, not how many
        # characters it consumed. Treating it as a length and slicing doc[start + end:]
        # overshoots by `start` -- past the end of the document, so the tail silently
        # becomes "". That shipped: every page of this edition ended mid-payload, 85 kB
        # short, with no </script>, no </body> and no </html>, and without the module
        # script that boots the client. Browsers paper over unclosed tags, so nothing
        # looked wrong; what was missing was the whole client runtime.
        payload, end = json.JSONDecoder().raw_decode(doc, start)
    except ValueError:
        return None
    return payload, start, end


def routes(payload: dict):
    """The loaderData routes, which is where every value this file edits lives."""
    for route in (payload.get("state", {}).get("loaderData") or {}).values():
        if isinstance(route, dict):
            yield route


def edit_payload(doc: str, mutate) -> tuple[str, bool]:
    """Hand the payload to `mutate`, and write it back if it says it changed anything."""
    found = read_payload(doc)
    if found is None:
        return doc, False
    payload, start, end = found
    if not mutate(payload):
        return doc, False

    # Re-serialised compactly. The two replacements keep the JSON safe *as a JavaScript
    # literal inside a <script>*: a literal "<" could close the tag early, and U+2028 /
    # U+2029 are ordinary characters in JSON but line terminators in JavaScript. Both
    # are written as \u escapes, which JSON reads back as the same characters.
    out = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    out = out.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return doc[:start] + out + doc[end:], True


def strip_payload_title(doc: str, name: str) -> tuple[str, bool]:
    """Blank the project title inside the hydration payload, for chapter pages.

    Editing <title> in the markup is only half the job: the hydrated head is re-rendered
    from the payload, and the suffix comes straight back. See `read_payload`.

    Measured here first: with `project.title` blanked in the payload the hydrated title
    is the chapter title alone, and the logo, the sidebar, the part names and the
    previous/next labels in the footer all still render -- those come from their own
    fields (`short_title`, `footer.navigation.*`), not from this one.

    Only the chapters. The landing page's title *is* the book's title.
    """

    def mutate(payload: dict) -> bool:
        changed = False
        for route in routes(payload):
            for holder in ("project", "config"):
                node = route.get(holder)
                if isinstance(node, dict) and node.get("title") == name:
                    node["title"] = ""
                    changed = True
        return changed

    return edit_payload(doc, mutate)


def payload_card(doc: str) -> str | None:
    """The card the hydrated head would name: the current page's frontmatter thumbnail.

    `thumbnailOptimized` first, because that is the order the theme's meta() reads them.
    """
    found = read_payload(doc)
    if found is None:
        return None
    for route in routes(found[0]):
        page = route.get("page")
        front = page.get("frontmatter") if isinstance(page, dict) else None
        if isinstance(front, dict):
            card = front.get("thumbnailOptimized") or front.get("thumbnail")
            if isinstance(card, str):
                return card
    return None


def set_payload_card(doc: str, card: str) -> tuple[str, bool]:
    """Point the payload's own copy of the card at the card the markup now names.

    The same trap as the title, one tag down: the theme's meta() builds og:image from
    `page.frontmatter.thumbnailOptimized || page.frontmatter.thumbnail`, so a page whose
    markup was corrected in section 6 and whose payload was not shows the rejected figure
    again the moment it hydrates. Social platforms never execute the script and would
    never have seen it; Google renders before it indexes, and would.

    **Only `page.frontmatter`.** The payload also carries `config.projects[0].pages[]`
    and `project.pages[]`, one entry per page of the book with a `thumbnail` of its own,
    and those are not card metadata: the theme renders them as the little preview that
    pops up when a reader hovers an internal link. A 400x528 figure is a perfectly good
    hover preview, and rewriting all thirty of them to the one generic card would make
    every preview in the book identical.
    """

    def mutate(payload: dict) -> bool:
        changed = False
        for route in routes(payload):
            page = route.get("page")
            front = page.get("frontmatter") if isinstance(page, dict) else None
            if not isinstance(front, dict):
                continue
            for key in ("thumbnail", "thumbnailOptimized"):
                url = front.get(key)
                if isinstance(url, str) and "/build/" in url and not url.endswith(card):
                    front[key] = f"{url.rsplit('/build/', 1)[0]}/build/{card}"
                    changed = True
        return changed

    return edit_payload(doc, mutate)


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


def drop_jupyter_css(doc: str) -> tuple[str, int]:
    """Drop the jupyter stylesheets from a page with no jupyter output.

    The page is left exactly as it is when there *is* output on it: this is 87 kB of
    stylesheet that the eighteen notebook pages genuinely need.
    """
    if JUPYTER_MARKER in doc:
        return doc, 0
    return JUPYTER_CSS.subn("", doc)


def social_card(root: pathlib.Path, index_html: str) -> str:
    """The filename of the built preview card, read off the landing page.

    MyST fingerprints asset names, so the hash changes whenever the card is regenerated
    by tools/social_card.py -- and it emits the project thumbnail twice, under two
    hashes of identical bytes, so globbing build/social-card-*.png and taking "the one"
    is not available. The landing page has no figure of its own, so MyST falls back there
    to the project thumbnail, which *is* the card: taking it from that page both finds
    the right hash and keeps this in step with the rest of the file, which derives the
    title suffix from the landing page for the same reason.

    If the landing page ever acquires a figure of its own, MyST will put that in og:image
    instead and this stops rather than guessing: whether that figure is the book's card
    is a decision, and it belongs in myst.yml next to `thumbnail`.
    """
    m = re.search(r'<meta property="og:image" content="([^"]+)"', index_html)
    if not m:
        sys.exit("::error::the landing page has no og:image; cannot find the preview card")
    name = m.group(1).rsplit("/", 1)[-1]
    if not name.startswith("social-card-"):
        sys.exit(
            f"::error::the landing page's og:image is {name}, not the social card.\n"
            f"  MyST uses project.thumbnail only for pages with no figure of their own,\n"
            f"  so the landing page has acquired one. Which image is the book's card is\n"
            f"  a decision; make it in myst.yml."
        )
    ok, why = card_ok(card_file(root, m.group(1)))
    if not ok:
        sys.exit(f"::error::the card itself fails the card rule: {why}")
    return name


def card_ok(path: pathlib.Path) -> tuple[bool, str]:
    """Whether this image can serve as a summary_large_image card, and why not."""
    with Image.open(path) as im:
        width, height = im.size
    kb = path.stat().st_size // 1024
    if width < CARD_MIN_WIDTH or height < CARD_MIN_HEIGHT:
        return False, f"{width}x{height}, under {CARD_MIN_WIDTH}x{CARD_MIN_HEIGHT}"
    if height >= width:
        return False, f"{width}x{height}, not landscape"
    if path.stat().st_size > CARD_MAX_BYTES:
        return False, f"{kb} kB, over {CARD_MAX_BYTES // 1024} kB"
    return True, f"{width}x{height}, {kb} kB"


def card_file(root: pathlib.Path, url: str) -> pathlib.Path:
    """The built file an og:image points at, whether the URL is absolute or not yet."""
    if "/build/" not in url:
        sys.exit(f"::error::og:image {url} is not a built asset; cannot check its size")
    return root / "build" / url.rsplit("/build/", 1)[1]


def vet_card(doc: str, root: pathlib.Path, card: str) -> tuple[str, str]:
    """Replace a page's card with the generic one unless its own figure can be a card.

    Returns the document and the reason, for the log. The replacement keeps whatever
    prefix the page's own og:image already carries, so it writes the same spelling of the
    origin as the rest of the build -- see section 6.
    """
    m = re.search(r'<meta property="og:image" content="([^"]+)"', doc)
    if not m:
        sys.exit("::error::a page has no og:image at all; MyST always writes one")
    url = m.group(1)
    if url.endswith(card):
        return doc, "already the card"
    ok, why = card_ok(card_file(root, url))
    if ok:
        return doc, f"kept its figure ({why})"
    # Both tags: MyST writes name="image" with the same value, and two tags naming
    # different images is worse than either of them. Each keeps *its own* prefix rather
    # than being written from one computed URL, which is what makes this work wherever it
    # runs: in the job the step that absolutises asset URLs has already rewritten both
    # tags, while in a local build neither is absolute yet, and the prefix is the only
    # place that difference lives.
    def swap(m: re.Match) -> str:
        if "/build/" not in m.group(2):
            sys.exit(f"::error::{m.group(0)} is not a built asset; cannot replace it")
        return m.group(1) + m.group(2).rsplit("/build/", 1)[0] + f"/build/{card}" + m.group(3)

    for kind, name in (("property", "og:image"), ("name", "image")):
        doc = re.sub(rf'(<meta {kind}="{name}" content=")([^"]*)(")', swap, doc)
    return doc, f"replaced ({why})"


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
    card = social_card(root, index.read_text(encoding="utf-8"))
    trimmed = n_lazy = n_preload = n_tags = n_css = n_cards = 0
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

        doc, dropped_css = drop_jupyter_css(doc)
        n_css += dropped_css

        doc, why = vet_card(doc, root, card)
        if why.startswith("replaced"):
            n_cards += 1
            # The markup is half of it; the hydrated head is re-rendered from the
            # payload, which still names the figure. Same trap as the title above.
            doc, _ = set_payload_card(doc, card)

        f.write_text(doc, encoding="utf-8")

    # Postconditions, not a tally of this run's edits: a second run is a legitimate
    # no-op, while markup that has moved under us must still fail.
    for f in pages:
        doc = f.read_text(encoding="utf-8")
        rel = f.parent.relative_to(root)
        # Completeness first. The payload edit once cut everything after the JSON:
        # 85 kB per page, including </script>, </body>, </html> and the module script
        # that boots the client. Browsers paper over unclosed tags, so nothing looked
        # wrong -- it surfaced only when the two editions were compared and this one
        # turned out to load half as many stylesheets, because it never hydrated at all.
        if not doc.rstrip().endswith("</html>"):
            sys.exit(f"::error::{f} does not end with </html> -- truncated?")
        for tag in ("</body>", "</html>"):
            if doc.count(tag) != 1:
                sys.exit(f"::error::{f} has {doc.count(tag)}x {tag}, expected exactly one")
        if doc.count("<script") != doc.count("</script>"):
            sys.exit(
                f"::error::{f} has {doc.count('<script')} <script> but "
                f"{doc.count('</script>')} </script>"
            )
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
        if JUPYTER_MARKER not in doc and JUPYTER_CSS.search(doc):
            sys.exit(f"::error::{f} has no jupyter output but still links a jupyter stylesheet")
        img = re.search(r'<meta property="og:image" content="([^"]+)"', doc)
        if not img:
            sys.exit(f"::error::{f} has no og:image")
        if not img.group(1).endswith(card):
            ok, why = card_ok(card_file(root, img.group(1)))
            if not ok:
                sys.exit(f"::error::{f} still ships a card that is {why}")
        else:
            # ...and the hydrated head must say the same thing the markup does, or the
            # rejected figure is back the moment the page hydrates.
            hydrated = payload_card(doc)
            if hydrated is not None and not hydrated.endswith(card):
                sys.exit(
                    f"::error::{f} names the card in its markup but {hydrated} in its "
                    f"hydration payload; it would get the rejected figure back"
                )

    print(
        f"head_meta: {len(pages)} pages, {trimmed}/{chapters} titles trimmed "
        f'(suffix "{suffix.strip()}"), {n_tags} card tags added, '
        f"{n_lazy} figures lazy-loaded, {n_preload} image preloads dropped, "
        f"{n_css} jupyter stylesheets dropped, "
        f"{n_cards} og:image replaced with {card}"
    )


if __name__ == "__main__":
    main()
