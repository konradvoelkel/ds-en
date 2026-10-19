#!/usr/bin/env python3
"""Trim the title tags, add the OpenGraph tags MyST omits, preload the fonts, give every
figure its intrinsic size, lazy-load the figures below the fold, drop the jupyter
stylesheets from pages with no jupyter output, drop the empty keywords meta, and refuse a
preview card too small to be one.

    python3 tools/head_meta.py <site-url> <html-dir> [--base BASE_URL]

Eight things, all of them post-processing on the built HTML, because none of them can
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

Section 7 shares this pass, and it measured something that belongs here too: these
attributes last about 190 ms, because the client re-renders the document and the server's
`<main>` goes with it. The browser's parser has already acted on `loading="lazy"` by
then -- that is the point of the attribute, and the preload removal below is what makes it
bite -- but a figure still below the fold when the page hydrates is fetched after all.
The honest fix is upstream; the measurement is in section 7.


5. The jupyter stylesheets on pages that have no jupyter output
--------------------------------------------------------------

Twelve of the thirty pages are Markdown chapters with no executed cell on them, and all
thirty load `thebe-core-<hash>.css` -- 87 kB of render-blocking stylesheet for cell
output, run buttons and kernel status that those twelve pages do not contain -- plus
`vendor/jupyter-matplotlib/mpl_widget.css`, which styles the ipympl widget. Where there is
nothing for them to style, both are made **inert** rather than removed: the `<link>` stays
exactly where the theme put it and gains `media="not all"`.

**They used to be deleted, and that broke the page.** Until 2026-10-18 this section
removed the two tags, on the reasoning in "what this does and does not buy" below -- that
the client re-adds them anyway, so the only effect is to take them off the critical path.
The second half of that was wrong. The client does not re-add them; it *fails to find*
them. Remix's `<Links>` renders both on every page, React hydrates a
`<link rel="stylesheet">` with no `precedence` as an ordinary element and matches it on
`rel`, `href`, `crossorigin` and `title`, and a tag that is not in the document matches
nothing. React then threw **#418** on each of these twelve pages -- the landing page among
them -- discarded the entire server-rendered document and rendered it again, taking with
it every head tag this file and the workflow insert and every attribute section 4 writes.
Eighty-seven kilobytes off the critical path, paid for with all of it. `SEO-NOTES.md` §20
has the diagnosis and the measurements.

`media="not all"` keeps both sides of the bargain, and it is worth being explicit about
why it is allowed to: `media` is **not one of the four attributes React compares**, so the
tag still matches and hydration completes, while a media query that matches nothing takes
the stylesheet off the critical path and never applies it. Measured on the fixed build at
375x812: no #418, the attribute survives hydration -- React does not patch it back --
`document.styleSheets` lists both with `media: not all`, and four stylesheets remain
render-blocking instead of six.

That does lean on an attribute React's hydration matcher happens not to look at, which is
a thing to write down rather than rediscover. If a future React widens the comparison,
these twelve pages break the way they were broken before this change, and the symptom is
the one §20 describes: a document that renders and is then thrown away. The fallback is to
stop touching these two stylesheets at all and accept the 87 kB, which was never really
bought. The postcondition at the bottom of this file is what would notice: it asserts the
tags are **present and inert** on all twelve pages, not absent.

The marker is MyST's own `myst-jp` class prefix, which the theme puts on every notebook
block and every output. It is 0 on exactly the twelve Markdown chapters and non-zero on
all eighteen notebook pages, and it is the same partition as MyST's internal
`computable` flag (`computables.length > 0 || kind === Notebook`).

**Not `jp-CodeCell`,** which the SEO audit of 2026-10-17 classified the pages by: thebe
adds that class when it attaches to a cell, and this site configures no kernel server, so
nothing ever attaches. Measured: zero occurrences in all thirty built pages, and zero in
the hydrated DOM of a notebook page as well.

**What this does and does not buy.** The two stylesheets leave the *critical path*: the
browser no longer waits for them before its first paint. They are not gone from the page
and they are still fetched, at the low priority a non-matching media query gets. What is
gone is only their render-blocking cost, which was always the whole of the claim worth
making here.

Why it has to be the same tag rather than no tag is the theme's doing: its root route
declares both in a Remix `links()` export, a static array with no access to the page's
data -- `links()` cannot see loader data at all -- so there is no per-page way to tell the
client not to render them. Hence `media`, which is ours to set, on a tag whose identity is
the theme's to decide. That is also why this cannot be done for the eighteen notebook
pages in reverse, and why the honest fix is upstream; it is recorded in UPSTREAM-NOTES.md.

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


7. The intrinsic size of every figure, in two places
----------------------------------------------------

226 `<img>` across the thirty pages and not one of them declared a width or a height.
The browser therefore cannot reserve a box before the picture arrives, and the text under
it is pushed down when it does: PageSpeed Insights measured `/expectation-variance/` at
**CLS 0.278** on 2026-10-17, past Google's 0.25 "poor" boundary, and Lighthouse flagged
`unsized-images` on both pages it tested. It is the one Core Web Vital on this site that
can go from poor to good outright rather than merely improving.

196 of those images are inside `<main>`; the other thirty are the navigation logo, one per
page, which is outside it and is not touched. 193 of the 196 are given `width` and
`height` read from the file in `_build/html/build/` -- the file's own pixels, never the
size it renders at. The distinction matters here because 28 of the figures carry an
inline `style="width:360px"` from the chapter source: the attributes say 555x329 and the
style still puts it on the page at 360 px wide, which is exactly how it works. Pillow
reads the PNGs, the JPEG and the GIF; the five SVGs are read from their root element, with
the viewBox as the fallback for a size given in anything but pixels (the book's own logo is
`30mm` by `15mm`, which is the case that proves the fallback is needed).

**Three images get no attributes**, for one reason wearing two hats: their height is
already fixed by something else, and an attribute width next to a fixed height is the one
way these attributes can distort a picture -- the aspect ratio is consulted only while one
of the two dimensions is still auto. Two are the inline thumbnails in
`descriptive-statistics` that sit inside a `<p>`, where the theme's
`.article p>img{max-height:1.2em}` caps them to the text size; one is the licence badge on
the landing page, whose own style says `height:20px`.

They are not left to shift, though, which is what the first version of this did: they get
a stylesheet rule carrying the **ratio alone**, no width. The constraint then travels the
other way -- the browser takes the height it already has and computes the width from the
ratio -- so the box is reserved and nothing is stretched.

**And the attributes alone would have been theatre.** Measured in the browser against the
built site on 2026-10-17: React threw a hydration error (#418) on every page as this
repository deployed it, discarded the server-rendered DOM and rendered the document again
from the payload. (The cause was found on 2026-10-18 and was ours, not the theme's --
`tools/vendor_assets.py` and section 5 below, diagnosed in SEO-NOTES.md §20 and **both
fixed the same day**, so the paragraph that follows is now history rather than the
operative fact: the attributes survive hydration, and the stylesheet below has stopped
being the only route that works and become the one that cannot break again. It is kept
deliberately; §20 argues why, and the three ratio-only figures above are the first of the
reasons.)
`<main>` was replaced about 190 ms into the load. The lazy attributes section 4 writes --
37 of 38 in the file on `eda-examples` -- were gone from the DOM 300 ms in, and so was
every head tag this file and the workflow insert: no og:url, no canonical, no hreflang, no
font preload in the hydrated document. Whatever was written into the markup held for a
fifth of a second, while the images of this site are still loading long after that
(LCP 10.7-11.1 s). That is what the second copy below was written for, and it is why the
second copy is still here now that the first one works again.

So the same dimensions are written a second time into `myst-theme.css`, which is this
project's own stylesheet from `myst.yml`'s `style:` -- the one file of ours the theme
loads itself, through its `links()` export, so the client re-adds exactly that tag. A
rule per distinct size, `width` plus `aspect-ratio` -- or the ratio alone, for the three
above -- keyed on the fingerprinted filename.
That is what the two attributes do between them, and a stylesheet is not markup, so the
re-render cannot take it away. Measured on a hydrated page with an image that never
loads: with its rule it reserves 284x274, without one it reserves 722x28, and that second
number is the layout shift the site has today.

The block sits in a **cascade layer**, which is what keeps it from winning arguments it
should lose: an unlayered declaration beats a layered one whatever the specificity, so
every rule the theme writes still takes precedence -- including `[&_img]:w-full img`, the
utility that sizes the preview popping up when a reader hovers an internal link, which
renders these same files. Verified: inside that wrapper the image is 500 px wide and not
284. The layer leaves this block doing only what it is for, which is giving a width to the
images nothing else gives a width to.

It costs 15.3 kB on a 7.6 kB stylesheet, 5.6 kB of it after gzip, on the critical path of
every page. That is the price of the fix and it is worth paying once per visit for a
metric measured in tenths; the honest way to make it smaller is fewer and better figures,
not shorter selectors.

The rendered size of every figure was compared before and after, in the browser, over
twelve pages and 148 images: not one box changed.


8. The empty keywords meta
---------------------------

All thirty pages carried `<meta name="keywords" content="">`. Google has ignored the
keywords meta since 2009, and an empty one does not even make a claim; MyST writes it
whether or not a page has keywords, and none of these does. Only the empty form is
removed -- a page that one day says something there is making a statement, and deleting it
would not be this file's business.

Markup only, and honestly so: like everything in section 7's second half, the tag is back
in the rendered DOM a fifth of a second later, because the theme's `meta()` builds it from
the payload. What this buys is the document that is served, which is what a crawler reads
first and what the audit measured. The fix that would also hold after hydration is in the
theme.


Running it twice
----------------

It is idempotent, and it checks postconditions rather than its own edits: every page must
end up with an og:url, no chapter title may still carry the suffix, no page with no
jupyter output may still link a jupyter stylesheet, no page may still carry an empty
keywords meta, every figure that may be sized must carry the size of the file on disk --
in its attributes *and* in the stylesheet, each checked against the file rather than
against what this run computed -- and every og:image must be a card that passes the rule
above. A second run is a no-op that still passes, while markup MyST has moved under us
fails -- which is the case the check is actually for.
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

# The tag scanner for the <main> slice. Quoted attribute values are consumed as a unit, so
# a ">" inside an alt text -- there are several, in the figure descriptions -- cannot end a
# tag early. The void set is what must not be pushed on the stack; everything else that
# opens is, which is how an inline image in a <p> is told from a figure. See section 7.
TAG = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:\"[^\"]*\"|'[^']*'|[^>])*?)(/?)>", re.S)
VOID = frozenset(
    "area base br col embed hr img input link meta param source track wbr".split()
)

# An image inside a <p> or a <dd> is an inline image, and the theme caps those at 1.2em:
# `.article p>img, .article p>a img, .article dd>img, .article dd>a img
#  {display:inline-block;max-height:1.2em}`. Giving one an intrinsic width would stretch
# it, because the cap fixes the height while the width would come from the attribute. Three
# images on the site are of this kind; see section 7.
INLINE_HOSTS = frozenset(("p", "dd"))
HEIGHT_PINNED = re.compile(r"(?:^|;)\s*(?:max-)?height\s*:", re.I)

# A length an <img> can be sized by: a bare number or px. Anything else (mm, %, em) is not
# a pixel size, and then the viewBox is the honest answer. See `svg_size`.
SVG_PX = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*(?:px)?\s*$", re.I)

# The generated block in myst-theme.css, between markers so a second run replaces it
# rather than appending a second copy. Section 7 argues why it is a stylesheet at all.
CSS_BEGIN = "/* head_meta.py: intrinsic figure dimensions -- begin, generated */"
CSS_END = "/* head_meta.py: intrinsic figure dimensions -- end */"
CSS_BLOCK = re.compile(re.escape(CSS_BEGIN) + r".*?" + re.escape(CSS_END), re.S)

# The outline reservation. Section 9 argues the whole of this; the numbers are measured,
# at 375x812 on the built site, and recorded in the audit's nav-reservation-measurements.
#
# The theme ships the in-article outline's container with an empty <nav> and fills it
# after mount, on every build, healthy hydration or not. On a throttled connection first
# paint lands before the fill, and everything below the container drops by its height:
# 0.153 on the landing page and 0.278 on a chapter, which is the whole of this site's CLS.
OUTLINE_BEGIN = "/* head_meta.py: outline reservation -- begin, generated */"
OUTLINE_END = "/* head_meta.py: outline reservation -- end */"
OUTLINE_BLOCK = re.compile(re.escape(OUTLINE_BEGIN) + r".*?" + re.escape(OUTLINE_END), re.S)
# The container, as served: the only <div> in <main> whose sole child is an empty <nav>.
# Matched on that shape rather than on `class="block my-10 ..."`, which is a pile of
# utilities that a theme upgrade may reshuffle without telling anyone.
OUTLINE_CONTAINER = re.compile(r'(<div\b[^>]*?)(\sstyle="([^"]*)")?(>\s*<nav></nav>\s*</div>)', re.I)
# What the class is for: the stylesheet needs something to select, and the value itself
# travels as a custom property because it differs per page and a stylesheet is one file.
OUTLINE_CLASS = "outline-reserve"
OUTLINE_VAR = "--outline-reserve"
# One entry is 32px tall; the header, the nav's padding and the container's own box are
# 84px between them. Measured exact on five pages that have no wrapped entry: 2 -> 148,
# 8 -> 340, 12 -> 468, 13 -> 500, 15 -> 564.
OUTLINE_ROW_PX = 32
OUTLINE_CHROME_PX = 84
# Under two entries the theme renders no outline at all -- continuous-distributions has
# one h2 and a container 0px tall -- so reserving anything there would be dead space.
OUTLINE_MIN_ENTRIES = 2
# The nav's own `max-height: calc(100vh - 100px)`, plus the container's 28px, is the
# ceiling the content can ever reach. Expressed in the rule rather than computed here,
# because it depends on the viewport and this runs at build time.
OUTLINE_VIEWPORT_CAP = "calc(100vh - 72px)"
# `lg` is 1024px in this theme (17 rules at that breakpoint in the built CSS). At and
# above it the container is `lg:h-0` and sits in the margin, where it displaces nothing
# and a min-height would break the layout rather than protect it.
OUTLINE_BREAKPOINT = "1023.98px"
# Which headings become entries: h2, h3 and h4. Confirmed on expectation-maximization,
# 7 + 13 + 4, against 24 entries measured in the browser.
OUTLINE_HEADINGS = re.compile(r"<h[234]\b", re.I)

# MyST writes this on every page whether or not a page has keywords. See section 8.
EMPTY_KEYWORDS = re.compile(r'<meta\b[^>]*\bname="keywords"[^>]*\bcontent=""[^>]*/?>', re.I)

# The jupyter stylesheets, and the class prefix whose absence says the page has no
# jupyter output for them to style. See section 5.
JUPYTER_MARKER = "myst-jp"
# What makes one inert without making it unmatchable: a media query that is never true.
# `media` is not one of the four attributes React compares when it hydrates a <link>, so
# the tag still matches the one the client renders. Section 5 argues the whole of this.
JUPYTER_INERT = 'media="not all"'
# Both of them, on every page, once `vendor_assets.py` has rewritten the second one's URL
# -- which is why this step runs after it, and why the postcondition insists on two.
JUPYTER_CSS_PER_PAGE = 2
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


def with_attrs(tag: str, extra: str) -> str:
    """Add attributes to a start tag, in front of the solidus if it has one.

    `<img src="x"/>` + `width="1"` has to become `<img src="x" width="1"/>` and not
    `<img src="x"/ width="1">`, which is what appending before the ">" produces. The
    second spelling does parse -- an HTML5 tokeniser treats the stray solidus as a parse
    error and carries on reading attributes -- and it is what this file wrote until
    2026-10-17, which is how it was noticed. It is still not markup to generate on purpose.
    """
    inner = tag[1:-1].rstrip()
    if inner.endswith("/"):
        return f"<{inner[:-1].rstrip()} {extra}/>"
    return f"<{inner} {extra}>"


def inline_image(tag: str, stack: list[str]) -> str | None:
    """Why this image must not be given a width, or None if it may have one.

    Both cases are an image whose *height* is fixed by something else, and a fixed height
    plus an attribute width is the one way these attributes can distort a picture: the
    aspect ratio is only consulted while one of the two dimensions is still auto.
    """
    style = re.search(r'\bstyle="([^"]*)"', tag, re.I)
    if style and HEIGHT_PINNED.search(style.group(1)):
        return "its own style fixes the height"
    for element in stack:
        if element in INLINE_HOSTS:
            return f"inline in a <{element}>, which the theme caps at 1.2em"
    return None


def svg_size(path: pathlib.Path) -> tuple[int, int]:
    """The intrinsic pixel size of an SVG, which Pillow cannot read.

    `width`/`height` on the root element first, since that is what the browser uses, but
    only when they are pixels: the book's logo is `30mm` by `15mm`, and 30 is not its
    width in anything. The viewBox is the fallback, because its third and fourth numbers
    are the units the browser scales -- so they carry the aspect ratio even when the
    declared size is in millimetres, and the aspect ratio is what reserves the box.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    root = re.search(r"<svg\b[^>]*>", text, re.S | re.I)
    if not root:
        sys.exit(f"::error::{path} has no <svg> element; cannot read its size")
    tag = root.group(0)

    def attr(name: str) -> str | None:
        m = re.search(rf'\b{name}\s*=\s*"([^"]*)"', tag, re.I)
        return m.group(1) if m else None

    w, h = SVG_PX.match(attr("width") or ""), SVG_PX.match(attr("height") or "")
    if w and h:
        return round(float(w.group(1))), round(float(h.group(1)))
    box = (attr("viewBox") or "").replace(",", " ").split()
    if len(box) == 4:
        try:
            return round(float(box[2])), round(float(box[3]))
        except ValueError:
            pass
    sys.exit(f"::error::{path} declares neither a pixel size nor a usable viewBox")


def intrinsic_size(path: pathlib.Path) -> tuple[int, int]:
    """The size of the file on disk, which is the only size these attributes may state."""
    if path.suffix.lower() == ".svg":
        return svg_size(path)
    with Image.open(path) as im:
        return im.size


def built_asset(root: pathlib.Path, src: str) -> pathlib.Path | None:
    """The file an <img src> points at, or None when it is not this build's own asset.

    A missing built asset is an error rather than a skip: the page would be showing a
    broken image, and a tool that reads the pixel sizes of the figures is the one that
    should say so.
    """
    if "/build/" not in src:
        return None
    path = root / "build" / src.rsplit("/build/", 1)[1]
    if not path.is_file():
        sys.exit(f"::error::{src} is not in the build; {path} does not exist")
    return path


def rewrite_figures(
    doc: str, root: pathlib.Path
) -> tuple[
    str, set[str], dict[str, tuple[int, int]], dict[str, tuple[int, int]], list[tuple[str, str]]
]:
    """Size every <img> inside <main>, and lazy-load every one but the first.

    Returns
      * the document,
      * the set of src URLs made lazy, so the caller can drop the matching preloads --
        without which the attribute has no effect at all (section 4),
      * src -> (width, height) for every image that may be sized, whether this run added
        the attributes or found them already there, because the caller writes those
        dimensions into a stylesheet as well and that has to be complete on a second run
        (section 7),
      * src -> (width, height) for the images whose height is fixed elsewhere: no
        attributes for these, and a stylesheet rule carrying the ratio alone,
      * the images that could not be measured at all, with the reason, for the log.

    One scan, because both jobs want the same thing: the <img> tags inside <main>, in
    order, with their ancestors known. Only the <main> slice, for the reason section 4
    gives -- the rest of the document is the hydration payload, and a regex let loose on
    that would edit strings the browser parses as data.
    """
    m = re.search(r"<main\b[^>]*>.*?</main>", doc, re.S | re.I)
    if not m:
        return doc, set(), {}, {}, []

    main = m.group(0)
    lazied: set[str] = set()
    sized: dict[str, tuple[int, int]] = {}
    ratio_only: dict[str, tuple[int, int]] = {}
    skipped: list[tuple[str, str]] = []
    stack: list[str] = []
    out: list[str] = []
    cut = 0
    seen = 0

    for token in TAG.finditer(main):
        closing, name, attrs, solidus = (
            token.group(1),
            token.group(2).lower(),
            token.group(3),
            token.group(4),
        )

        if name != "img":
            # The stack only has to be right about <p> and <dd>, so a stray close tag is
            # popped tolerantly rather than trusted blindly.
            if closing:
                if name in stack:
                    while stack and stack.pop() != name:
                        pass
            elif name not in VOID and not solidus:
                stack.append(name)
            continue

        seen += 1
        tag = token.group(0)
        src_match = re.search(r'\bsrc="([^"]*)"', attrs, re.I)
        src = src_match.group(1) if src_match else None

        if src is None:
            skipped.append(("<img> with no src", "no src to size it by"))
        else:
            path = built_asset(root, src)
            if path is None:
                skipped.append((src, "not an asset of this build"))
            elif inline_image(tag, stack):
                # The ratio, never a width: see `figure_css`. The attributes are a width,
                # so these get none -- the stylesheet carries the whole of it.
                ratio_only[src] = intrinsic_size(path)
            else:
                size = intrinsic_size(path)
                sized[src] = size
                if not re.search(r"\b(?:width|height)\s*=", attrs, re.I):
                    tag = with_attrs(tag, f'width="{size[0]}" height="{size[1]}"')

        if seen > 1:  # the first image is the LCP candidate: eager, and it keeps its preload
            if src:
                lazied.add(src)
            if not re.search(r"\bloading\s*=", attrs, re.I):
                tag = with_attrs(tag, 'loading="lazy" decoding="async"')

        if tag != token.group(0):
            out.append(main[cut : token.start()])
            out.append(tag)
            cut = token.end()

    main_new = "".join(out) + main[cut:]
    return doc[: m.start()] + main_new + doc[m.end() :], lazied, sized, ratio_only, skipped


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


def drop_modulepreloads(doc: str) -> tuple[str, int]:
    """Remove the theme's `<link rel="modulepreload">` hints.

    Measured on the live landing page, 2026-10-19: nineteen of them, naming 1,407 KiB of
    gzipped JavaScript, against a 32 KiB document and 44 KiB of render-blocking CSS.
    `modulepreload` is fetched at *High* priority -- the same bucket as the stylesheets
    that block the first paint -- so on PageSpeed's Slow 4G profile (~200 KB/s) the four
    stylesheets queue alongside roughly seven seconds of JavaScript. FCP 8.4 s and LCP
    8.9 s are half a second apart, which says the LCP element paints as soon as anything
    paints: nothing on this page is slow except the paint itself.

    **This does not remove the JavaScript.** The module graph is still loaded, by the
    `<script type="module">` the theme emits at the end of the body; a `modulepreload` is
    a priority hint and nothing else. What changes is when it competes: after the paint
    rather than in front of it. The cost is that hydration lands later, and this
    repository has twice been caught by hydration (SEO-NOTES.md §15, §20), so the thing
    to watch is TBT, which is 0 today, and CLS, which is 0 because section 8 reserves the
    outline's height at build time rather than relying on an early hydration.

    The same argument section 4 makes for image preloads -- a preloaded image is fetched
    whatever `loading="lazy"` says -- and the same place to make it: these are link tags
    in a document this tool already rewrites. The audit of 2026-10-17 recorded the unused
    JavaScript as the theme's own bundle and out of reach, which is true of its *size* and
    not of the *priority* it is fetched at.
    """
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        n += 1
        return ""

    doc = re.sub(r'<link\b[^>]*\brel="modulepreload"[^>]*/?>', sub, doc, flags=re.I)
    return doc, n


CHROME_LABELS = {
    "myst-top-nav-menu-button": "Open the navigation menu",
    "myst-search-bar": "Search this book",
    "myst-fm-downloads-button": "Download this book",
}


def name_controls(doc: str) -> tuple[str, int]:
    """Give the theme's three unnamed buttons an `aria-label`.

    Lighthouse reports "Buttons do not have an accessible name" against the landing page,
    and the accessibility tree agrees: three of the thirteen server-rendered buttons have
    no name at all. Each contains one `<svg aria-hidden="true">` and nothing else, so
    there is no text for a screen reader -- or for an agent reading the tree -- to fall
    back on. The other ten are fine; the theme labels its "Open Folder", "Author Details"
    and theme-toggle buttons itself, which is why this is a gap rather than a policy.

    They are keyed by the stable class the theme puts on each (`myst-`-prefixed, and the
    same strings its stylesheet selects on) rather than by position, so a reordered navbar
    does not silently relabel the wrong control. A button that already carries a name --
    `aria-label`, `title` or `aria-labelledby` -- is left alone, so the day the theme adds
    its own this does nothing instead of fighting it.

    **The names are ours, not the theme's**, and that is the risk: if a later version
    renames these classes the labels stop being applied, which the postcondition in
    `main` catches, but if it renames the *controls* while keeping the classes, the labels
    would be wrong and nothing would catch it. That is the trade for not waiting on
    upstream, and it is cheap to re-check.

    These are server-rendered, so this is markup the first paint already carries. React
    leaves an attribute it did not render in place during hydration -- verified on the
    built page rather than assumed, because this repository has twice been caught out by
    hydration (SEO-NOTES.md §15, §20).
    """
    n = 0

    def sub(m: re.Match) -> str:
        nonlocal n
        tag = m.group(0)
        for cls, label in CHROME_LABELS.items():
            if cls not in tag:
                continue
            if re.search(r'\b(aria-label|title|aria-labelledby)=', tag):
                return tag
            n += 1
            return with_attrs(tag, f'aria-label="{label}"')
        return tag

    return re.sub(r"<button\b[^>]*>", sub, doc), n


def unsized_chrome(
    doc: str, root: pathlib.Path, skip: set[str]
) -> list[tuple[str, str, int, int]]:
    """The `<img>` outside the figure pass that have no usable dimensions: the navbar logo.

    `rewrite_figures` walks the `<main>` slice, because that is where the figures are and
    where the layout shift was. The navbar logo is outside it, and the theme writes
    `height="2.25rem"` on it -- the computed value of its own `h-9` class, in CSS units.
    The HTML `height` attribute takes a number of pixels and nothing else, so a browser
    discards it, and the page carries an image with no dimensions at all while *looking*
    as though it has one. That is how it survived a pass that counted 193 of 196 figures
    sized: a tag with `height=` in it reads as sized to anything that greps for one.

    **These get the ratio and not the attributes**, which is the same call section 7 makes
    for its three: the logo's height is fixed by a class, so giving it `width` and
    `height` makes the width attribute the used width and squashes it -- measured, 216x36
    where it should be 72x36, before this was changed to match. With the ratio alone the
    constraint travels the other way: the browser takes the height the class gives it and
    computes the width, and the box is reserved just the same.

    So Lighthouse's "Image elements do not have explicit width and height" still names the
    logo, as it names those three. That diagnostic does not enter the score, and a
    distorted logo would be a real defect traded for a cosmetic one. What *is* fixed is
    the attribute that was lying: the invalid `height` is removed.

    `skip` is the set of src URLs `rewrite_figures` has already ruled on, so a second pass
    cannot reverse a decision taken with measurements.

    The navbar logo is the interesting one. The theme writes `height="2.25rem"` -- the
    computed value of its own `h-9` class, in CSS units. The HTML `height` attribute takes
    a number of pixels and nothing else, so a browser discards it, and the page has an
    image with no dimensions at all while *looking* as though it has one. That is why it
    survived a pass that counted 193 of 196 figures sized: a tag with `height=` in it
    reads as sized to anything that greps.

    The other is the CC BY-SA badge in the licence section, which carries its height in an
    inline style and no attributes.

    This reports rather than rewrites, and `main` does the editing, so that the count in
    the summary line is the number of images this changed and not the number of tags it
    matched.
    """
    out: list[tuple[str, int, int]] = []
    for m in re.finditer(r"<img\b[^>]*>", doc):
        tag = m.group(0)
        w = re.search(r'\swidth="(\d+)"', tag)
        h = re.search(r'\sheight="(\d+)"', tag)
        if w and h:
            continue
        src = re.search(r'\bsrc="([^"]*)"', tag)
        if not src:
            continue
        if src.group(1) in skip:
            continue
        path = built_asset(root, src.group(1))
        if path is None:
            continue
        out.append((tag, src.group(1), *intrinsic_size(path)))
    return out


def figure_css(
    sizes: dict[str, tuple[int, int]],
    ratios: dict[str, tuple[int, int]],
    chrome: dict[str, tuple[int, int]] | None = None,
) -> str:
    """The generated block: one rule per distinct size, in a cascade layer.

    `width` *and* `aspect-ratio`, which is what the two attributes do between them: the
    width is what an unloaded image reserves, and the ratio is what turns that width into
    a height. `max-width:100%` and `height:auto` are not repeated here -- the theme's own
    preflight (`img,video{max-width:100%;height:auto}`) sets both, and that is also what
    keeps a figure wider than its column from overflowing it.

    `ratios` is the other three: the images whose height is already fixed, which must not
    be given a width (that is the one thing that would distort them) but which can have
    the **ratio alone**. Then the constraint travels the other way -- the browser takes
    the height it has and computes the width from the ratio -- and the box is reserved
    just the same. Skipping them entirely, as the first version of this did, left the
    only three images on the site that still shift.

    **In a cascade layer, so that every rule the theme writes wins over this one.** An
    unlayered declaration beats a layered one whatever the specificity, and these
    selectors are specific enough (an attribute selector and two elements) to have beaten
    the theme's own utilities otherwise -- `[&_img]:w-full img`, which sizes the preview
    that pops up when a reader hovers an internal link, is one class and one element, and
    those previews are the same files. The layer makes this block what it should be: a
    width for the images nothing else gives a width to.

    Keyed on the fingerprinted filename with its leading slash, so the block is the same
    whatever BASE_URL the site is built for, and so a shorter name cannot match the tail
    of a longer one.
    """
    chrome = chrome or {}

    def grouped(
        by_src: dict[str, tuple[int, int]], scope: str = "main "
    ) -> list[tuple[tuple[int, int], str]]:
        groups: dict[tuple[int, int], list[str]] = {}
        for src, size in by_src.items():
            groups.setdefault(size, []).append(src.rsplit("/", 1)[-1])
        return [
            (size, ",".join(f'{scope}img[src$="/{n}"]' for n in sorted(names)))
            for size, names in sorted(groups.items())
        ]

    # The chrome's one image is in the navbar, so its rule cannot carry the `main `
    # scope the figures' rules do -- which is exactly the mistake the first version of
    # section 9 made: a correct ratio on a selector that matched nothing.
    full = [f"{sel}{{width:{w}px;aspect-ratio:{w}/{h}}}" for (w, h), sel in grouped(sizes)]
    ratio_only = [f"{sel}{{aspect-ratio:{w}/{h}}}" for (w, h), sel in grouped(ratios)]
    ratio_only += [
        f"{sel}{{aspect-ratio:{w}/{h}}}" for (w, h), sel in grouped(chrome, scope="")
    ]
    return "\n".join(
        [
            CSS_BEGIN,
            f"/* {len(sizes)} figures in {len(full)} distinct sizes, and {len(ratios)} "
            f"whose height is fixed elsewhere and which get the ratio only, plus "
            f"{len(chrome)} outside <main>. "
            f"Do not edit: tools/head_meta.py section 7 writes this. */",
            "@layer figure-dimensions{",
            *full,
            *ratio_only,
            "}",
            CSS_END,
        ]
    )


def write_figure_css(
    root: pathlib.Path,
    sizes: dict[str, tuple[int, int]],
    ratios: dict[str, tuple[int, int]],
    chrome: dict[str, tuple[int, int]] | None = None,
) -> int:
    """Put the block into the one stylesheet of ours that the theme itself loads.

    Not a <style> in the head and not a <link>: both are markup, and the client throws
    the server's markup away (section 7). `myst-theme.css` is in the theme's own
    `links()`, so the client re-adds exactly that tag -- the stylesheet is loaded by the
    page either way, which is the property this needs and the markup does not have.
    """
    stylesheet = root / "myst-theme.css"
    if not stylesheet.is_file():
        sys.exit(
            f"::error::{stylesheet} does not exist. It is the stylesheet the theme loads "
            f"from myst.yml's `style:`, and the only place these rules can go that "
            f"survives hydration."
        )
    css = stylesheet.read_text(encoding="utf-8")
    block = figure_css(sizes, ratios, chrome)
    if CSS_BLOCK.search(css):
        css = CSS_BLOCK.sub(lambda _: block, css, count=1)
    else:
        css = css.rstrip("\n") + "\n\n" + block + "\n"
    stylesheet.write_text(css, encoding="utf-8")
    return len(sizes)


def read_figure_css(
    root: pathlib.Path,
) -> tuple[dict[str, tuple[int, int]], dict[str, tuple[int, int]]]:
    """What the stylesheet states, read back for the postcondition.

    Two maps, because the two kinds of rule are checked against different images: the
    ones that carry a width, and the height-fixed ones that carry the ratio alone.
    """
    css = (root / "myst-theme.css").read_text(encoding="utf-8")
    block = CSS_BLOCK.search(css)
    if not block:
        sys.exit("::error::myst-theme.css has no generated figure-dimensions block")
    sized: dict[str, tuple[int, int]] = {}
    ratios: dict[str, tuple[int, int]] = {}
    for rule in re.finditer(r"([^{}]+)\{([^{}]+)\}", block.group(0)):
        selector, body = rule.groups()
        ratio = re.search(r"aspect-ratio:(\d+)/(\d+)", body)
        if not ratio:
            sys.exit(f"::error::generated rule without an aspect-ratio: {rule.group(0)[:80]}")
        size = (int(ratio.group(1)), int(ratio.group(2)))
        width = re.search(r"width:(\d+)px", body)
        if width and int(width.group(1)) != size[0]:
            sys.exit(f"::error::{selector[:60]} states width {width.group(1)} but ratio {size}")
        into = sized if width else ratios
        for name in re.findall(r'img\[src\$="/([^"]+)"\]', selector):
            into[name] = size
    return sized, ratios


def outline_entries(doc: str) -> int:
    """How many entries the client will put in the outline: the h2, h3 and h4 in <main>.

    Counted on the <main> slice for the same reason section 4 gives: the rest of the
    document is the hydration payload, where the same headings appear again as JSON.
    """
    m = re.search(r"<main\b[^>]*>.*?</main>", doc, re.S | re.I)
    return len(OUTLINE_HEADINGS.findall(m.group(0))) if m else 0


def reserve_outline(doc: str, entries: int) -> tuple[str, int]:
    """Reserve the height the outline will take, on the container that holds it.

    Returns the document and the reserved height in px, 0 when nothing was reserved.

    The height goes in as a **custom property on the element**, not as a `min-height`:
    a custom property has no effect of its own, so the one thing this cannot do is break
    a layout. The stylesheet decides what to do with it, under a media query this cannot
    express inline, and its `var(..., 0px)` fallback means a page that somehow misses the
    property reserves nothing and behaves exactly as the site did before this existed.

    Reserving is safe in one direction only, which is why an approximation is allowed
    here at all. `min-height` is a floor: reserve too much and the box keeps its floor,
    costing dead space and shifting nothing; reserve too little and the content outgrows
    the box, which shifts. The error that matters is one-sided, and the formula's error
    is bounded -- it under-reserves 24px per entry whose text wraps to a second line.
    Three of the ten pages measured have a wrapped entry; on one of them the viewport cap
    below swallows the difference, so two end up short, the worse by 48px of 812. That
    leaves a residual CLS near 0.02 where there was 0.15 and 0.28.

    **Why the exact number is not computable here.** Whether an entry wraps depends on
    the rendered width of proportional text at a given viewport width. The build has the
    heading text but no font metrics and no layout engine, so the only exact route is to
    render all thirty pages in a headless browser -- a browser dependency in the build
    and in CI, for 24px. Measured and rejected; the audit records both sides.
    """
    if entries < OUTLINE_MIN_ENTRIES:
        return doc, 0
    reserve = OUTLINE_ROW_PX * entries + OUTLINE_CHROME_PX
    hit = OUTLINE_CONTAINER.search(doc)
    if not hit:
        sys.exit(
            "::error::no outline container found. It is the one <div> in <main> whose "
            "only child is an empty <nav>, and the reservation has nowhere to go without "
            "it. If the theme now fills the nav server-side, this whole section is "
            "obsolete and should go, not be made to match again."
        )
    open_tag, _, style, tail = hit.groups()
    if OUTLINE_VAR in (style or ""):
        return doc, reserve  # already run over this page
    declaration = f"{OUTLINE_VAR}:{reserve}px"
    merged = f"{style.rstrip(';')};{declaration}" if style else declaration
    classed = re.sub(r'(\sclass=")', rf'\1{OUTLINE_CLASS} ', open_tag, count=1)
    if classed == open_tag:
        classed = f'{open_tag} class="{OUTLINE_CLASS}"'
    return doc[: hit.start()] + f'{classed} style="{merged}"{tail}' + doc[hit.end() :], reserve


def outline_css() -> str:
    """The one rule that turns the per-page custom property into reserved space.

    Not in a cascade layer, unlike the figure block: that one is deliberately beatable
    by the theme, because the theme has its own opinions about image widths. Nothing in
    the theme sets a min-height on this container, so there is nothing to defer to, and a
    layer would only make the reservation lose to the next utility that happens to match.

    `min()` against the viewport because the nav caps itself at `calc(100vh - 100px)` and
    then scrolls: past that the content stops growing, and a floor above it would be dead
    space on short viewports rather than protection on tall ones.
    """
    return "\n".join(
        [
            OUTLINE_BEGIN,
            "/* Reserves the space the client-filled outline will occupy, so that filling "
            "it moves nothing. Per page, via the custom property the markup carries. "
            "Do not edit: tools/head_meta.py section 9 writes this. */",
            f"@media (max-width:{OUTLINE_BREAKPOINT}){{",
            f"main .{OUTLINE_CLASS}{{min-height:min(var({OUTLINE_VAR},0px),"
            f"{OUTLINE_VIEWPORT_CAP})}}",
            "}",
            OUTLINE_END,
        ]
    )


def write_outline_css(root: pathlib.Path) -> None:
    """Into the same stylesheet, for the same reason: it is the one the theme reloads."""
    stylesheet = root / "myst-theme.css"
    css = stylesheet.read_text(encoding="utf-8")
    block = outline_css()
    if OUTLINE_BLOCK.search(css):
        css = OUTLINE_BLOCK.sub(lambda _: block, css, count=1)
    else:
        css = css.rstrip("\n") + "\n\n" + block + "\n"
    stylesheet.write_text(css, encoding="utf-8")


def drop_keywords(doc: str) -> tuple[str, int]:
    """Drop `<meta name="keywords" content="">`, which all thirty pages carry.

    Only the empty one. A keywords list Google ignores is a statement about the page and
    not ours to delete; an empty one is forty bytes saying nothing, and MyST writes it
    whether or not a page has keywords -- none of the thirty does.
    """
    return EMPTY_KEYWORDS.subn("", doc)


def inert_jupyter_css(doc: str, where: str) -> tuple[str, int]:
    """Make the jupyter stylesheets inert on a page with no jupyter output.

    `media="not all"` on the tag the theme wrote, not the tag's removal: the client
    renders both links on every page and hydration matches them by `rel`, `href`,
    `crossorigin` and `title`, so a missing tag costs the whole document. Section 5.

    The page is left exactly as it is when there *is* output on it: this is 87 kB of
    stylesheet that the eighteen notebook pages genuinely need. A second run finds the
    attribute already there and changes nothing. A tag that already carries some other
    `media` is the theme having taken this over, which is a thing to stop for.
    """
    if JUPYTER_MARKER in doc:
        return doc, 0

    n = 0

    def fix(m: re.Match) -> str:
        nonlocal n
        tag = m.group(0)
        if JUPYTER_INERT in tag:
            return tag
        other = re.search(r'\bmedia="([^"]*)"', tag, re.I)
        if other:
            sys.exit(
                f'::error::{where}: a jupyter stylesheet already carries media='
                f'"{other.group(1)}", so the theme now sets it itself. Read section 5 '
                f"before overwriting it: this attribute is load-bearing for hydration, "
                f"and two of us writing it is how that breaks quietly."
            )
        n += 1
        # Inside the angle brackets, without whatever trailing slash was there, so the
        # tag comes back out in the one form MyST writes.
        return f"<{tag[1:-1].rstrip('/').rstrip()} {JUPYTER_INERT}/>"

    return JUPYTER_CSS.sub(fix, doc), n


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
    ap.add_argument(
        "--drop-modulepreload",
        action="store_true",
        help="remove the theme's modulepreload hints; see drop_modulepreloads()",
    )
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
    trimmed = n_lazy = n_preload = n_tags = n_css = n_cards = n_keywords = n_outline = 0
    n_chrome_sized = n_named = 0
    chrome_ratios: dict[str, tuple[int, int]] = {}
    n_modulepreload = 0
    chapters = 0
    outlines: dict[str, tuple[int, int]] = {}
    sizes: dict[str, tuple[int, int]] = {}
    ratios: dict[str, tuple[int, int]] = {}
    unsized: list[tuple[str, str, str]] = []

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

        doc, lazied, page_sizes, page_ratios, page_unsized = rewrite_figures(doc, root)
        doc, dropped = drop_image_preloads(doc, lazied)
        n_lazy += len(lazied)
        n_preload += dropped
        sizes.update(page_sizes)
        ratios.update(page_ratios)
        unsized += [(str(rel), src, why) for src, why in page_unsized]

        # Section 9: the chrome the figure pass never looked at, and the three controls
        # the theme leaves unnamed.
        ruled_on = set(page_sizes) | set(page_ratios)
        for tag, src, w, h in unsized_chrome(doc, root, ruled_on):
            # The invalid attribute goes; the ratio does the reserving, through the same
            # stylesheet the three ratio-only figures use.
            doc = doc.replace(tag, re.sub(r'\s(?:width|height)="[^"]*"', "", tag))
            chrome_ratios[src] = (w, h)
            n_chrome_sized += 1
        doc, named = name_controls(doc)
        n_named += named
        if args.drop_modulepreload:
            doc, dropped_mp = drop_modulepreloads(doc)
            n_modulepreload += dropped_mp

        doc, inerted_css = inert_jupyter_css(doc, str(f))
        n_css += inerted_css

        entries = outline_entries(doc)
        doc, reserved = reserve_outline(doc, entries)
        outlines[str(rel)] = (entries, reserved)
        if reserved:
            n_outline += 1

        doc, dropped_keywords = drop_keywords(doc)
        n_keywords += dropped_keywords

        doc, why = vet_card(doc, root, card)
        if why.startswith("replaced"):
            n_cards += 1
            # The markup is half of it; the hydrated head is re-rendered from the
            # payload, which still names the figure. Same trap as the title above.
            doc, _ = set_payload_card(doc, card)

        f.write_text(doc, encoding="utf-8")

    # One stylesheet for the whole book, written once the pages have been read: the same
    # figure appears on more than one page, and a rule has to exist for every page that
    # shows it. See section 7.
    write_figure_css(root, sizes, ratios, chrome_ratios)
    write_outline_css(root)

    # Postconditions, not a tally of this run's edits: a second run is a legitimate
    # no-op, while markup that has moved under us must still fail.
    declared, declared_ratios = read_figure_css(root)
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
        # Present *and* inert, which is the opposite of what this asserted before
        # 2026-10-18. A missing tag is the failure now: see section 5. Both counts are
        # checked, because a page carrying one of the two means `vendor_assets.py` has
        # not run yet -- JUPYTER_CSS only matches the ipympl URL after it is rewritten --
        # and this step would then be inerting half of what it reports.
        jupyter_tags = JUPYTER_CSS.findall(doc)
        if len(jupyter_tags) != JUPYTER_CSS_PER_PAGE:
            sys.exit(
                f"::error::{f} links {len(jupyter_tags)} jupyter stylesheets, expected "
                f"{JUPYTER_CSS_PER_PAGE}. Either this ran before vendor_assets.py, or the "
                f"theme's links() changed and section 5 needs re-reading."
            )
        if JUPYTER_MARKER not in doc:
            for tag in jupyter_tags:
                if JUPYTER_INERT not in tag:
                    sys.exit(
                        f"::error::{f} has no jupyter output but its jupyter stylesheet is "
                        f"not inert: {tag}. It must stay in the document and carry "
                        f"{JUPYTER_INERT} -- removing it costs the whole page on hydration "
                        f"(section 5, SEO-NOTES.md §20)."
                    )
        if EMPTY_KEYWORDS.search(doc):
            sys.exit(f"::error::{f} still carries an empty keywords meta")
        # The outline reservation, recomputed from the page rather than from what the
        # loop above recorded, so a page the loop skipped still fails here. What is
        # asserted is the *input*: the entry count the markup now states, against the
        # headings that are in it. The rendered pixel height cannot be asserted at build
        # time, and section 9 says why -- so this guards the thing that would actually
        # drift, which is a container that stopped matching or a page that grew headings
        # without the property following.
        entries = outline_entries(doc)
        want = OUTLINE_ROW_PX * entries + OUTLINE_CHROME_PX if entries >= OUTLINE_MIN_ENTRIES else 0
        stated = re.search(re.escape(OUTLINE_VAR) + r":(\d+)px", doc)
        if want and not stated:
            sys.exit(
                f"::error::{f} has {entries} outline entries but reserves nothing. "
                f"Either the container stopped matching OUTLINE_CONTAINER, or this ran "
                f"before the page was written."
            )
        if stated and int(stated.group(1)) != want:
            sys.exit(
                f"::error::{f} reserves {stated.group(1)}px for {entries} outline "
                f"entries, expected {want}px"
            )
        if want and f'class="{OUTLINE_CLASS} ' not in doc and f'class="{OUTLINE_CLASS}"' not in doc:
            sys.exit(f"::error::{f} carries the reservation but not .{OUTLINE_CLASS} to select it")
        # Every figure, against the file on disk rather than against what this run
        # computed: the attributes and the stylesheet both have to say what the image
        # actually is, and on a second run neither of them is written at all.
        main = re.search(r"<main\b[^>]*>.*?</main>", doc, re.S | re.I)
        stack: list[str] = []
        for token in TAG.finditer(main.group(0) if main else ""):
            name, attrs = token.group(2).lower(), token.group(3)
            if name != "img":
                if token.group(1):
                    if name in stack:
                        while stack and stack.pop() != name:
                            pass
                elif name not in VOID and not token.group(4):
                    stack.append(name)
                continue
            src = re.search(r'\bsrc="([^"]*)"', attrs, re.I)
            if not src:
                continue
            path = built_asset(root, src.group(1))
            if path is None:
                continue
            w, h = intrinsic_size(path)
            name_on_disk = src.group(1).rsplit("/", 1)[-1]
            if inline_image(token.group(0), stack):
                # Height fixed elsewhere: the ratio alone, in the stylesheet, and no
                # width anywhere -- a width is what would distort these three.
                if re.search(r"\b(?:width|height)\s*=", token.group(0), re.I):
                    sys.exit(
                        f"::error::{f}: {name_on_disk} has its height fixed by the page "
                        f"and must not carry width/height attributes"
                    )
                if declared_ratios.get(name_on_disk) != (w, h):
                    sys.exit(
                        f"::error::{f}: myst-theme.css says "
                        f"{declared_ratios.get(name_on_disk)} for {name_on_disk}, "
                        f"the file is {w}x{h}"
                    )
                continue
            got = re.search(r'\bwidth="(\d+)"[^>]*\bheight="(\d+)"', token.group(0), re.I)
            if not got:
                sys.exit(f"::error::{f}: {src.group(1)} has no width/height")
            if (int(got.group(1)), int(got.group(2))) != (w, h):
                sys.exit(
                    f"::error::{f}: {src.group(1)} says "
                    f"{got.group(1)}x{got.group(2)} but the file is {w}x{h}"
                )
            # ...and the stylesheet, which is the half that survives hydration.
            if declared.get(name_on_disk) != (w, h):
                sys.exit(
                    f"::error::{f}: myst-theme.css says {declared.get(name_on_disk)} for "
                    f"{name_on_disk}, the file is {w}x{h}"
                )
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

    # Anything that could not be measured at all, named rather than counted: today there
    # is nothing here, and something arriving in this list is something to read.
    for rel, src, why in unsized:
        print(f"  unsized: /{rel} {src.rsplit('/', 1)[-1]} -- {why}")

    heights = sorted(r for _, r in outlines.values() if r)
    span = f" ({heights[0]}-{heights[-1]}px)" if heights else ""
    print(
        f"head_meta: {len(pages)} pages, {trimmed}/{chapters} titles trimmed "
        f'(suffix "{suffix.strip()}"), {n_tags} card tags added, '
        f"{len(sizes)} figures sized, {len(ratios)} given the ratio alone "
        f"({len(unsized)} not measurable), "
        f"{n_lazy} figures lazy-loaded, {n_preload} image preloads dropped, "
        f"{n_css} jupyter stylesheets made inert, {n_keywords} empty keywords metas dropped, "
        f"{n_cards} og:image replaced with {card}, "
        f"{n_outline} outlines reserved{span}, "
        f"{n_chrome_sized} chrome images given a ratio, {n_named} controls named"
        + (f", {n_modulepreload} modulepreloads dropped" if n_modulepreload else "")
    )


if __name__ == "__main__":
    main()
