"""Insert the JSON-LD description of the book, and of each of its chapters, into the
built HTML.

    python3 tools/inject_jsonld.py <site-url> <html-dir>

Run from the deploy workflow, after the origin has been written into the build and after
`freshness.py` and `head_meta.py` -- see "What is read back" below. MyST emits no
structured data of its own, and the block cannot live in `landing-page.md`: a `{raw} html`
directive there would be an extra block and break the block alignment with the German
original (TRANSLATION.md section 1). So it is added to the built HTML instead.


One book, twenty-nine chapters, one author
------------------------------------------

Until 2026-10-17 only the landing page got a block, for the reason that stood here:
*"the entity is the book as a whole; repeating it per chapter would assert 30 books."*
That is still true, and it was an argument against the wrong fix. Twenty-nine pages
carrying no structured data at all was the largest single gap the SEO audit of
2026-10-17 found (`datascience.konradvoelkel.com-audit/findings/schema.md`).

A chapter does not get a second `Book`. It gets a `["Chapter","LearningResource"]` with
an `@id` of its own (`.../<slug>/#chapter`) and an `isPartOf` pointing at the one book
node, which already has a stable `@id` of `.../#work`. The author is the same move one
level down: the `Person` is written out once, on the landing page, with an `@id` of
`.../#author`, and each chapter references that `@id` instead of repeating the name,
the six `sameAs` profiles and the affiliation thirty times.

So the graph says what the site is -- one work, twenty-nine parts of it, one author --
and every chapter becomes an entity an answer engine can cite by URL rather than an
anonymous page inside a book.

A chapter's `author` is deliberately the bare `{"@id": ...}` reference, with no `@type`
or `name` beside it. Google reads one document at a time, so on a chapter page that
reference asserts an identity and nothing else; the properties are a fetch of the
landing page away. That is the trade: it is the identity that has to be shared, and
restating `"@type": "Person", "name": ...` in the stub would be the first step back
towards the thirty copies this avoids.

Deliberately *not* claimed, though an external critique proposed them: `Course`,
`hasCourseInstance` and `"provider": HHU`. The English edition is not a course offered by
the university -- it is a translated book. The author's affiliation is a different claim,
and that one is true, so it stays.


Three works, one author
-----------------------

Asked in October 2026 how many sets of lecture notes Konrad Völkel had written, ChatGPT
answered that it "could not verify a reliable total" and, once pushed, produced the right
three with a caveat attached. It had one source for the claim: the sibling-notes paragraph
on this landing page, in prose, in one edition. The two German works it named carry no
structured data at all, and nothing anywhere stated the set.

So the landing page is now a `@graph` rather than the bare book node, and the two other
works are in it: `tools/sibling-works.json`, each a `["Book","LearningResource"]` whose
`author` is the same `{"@id": .../#author}` reference the chapters use. Nothing else about
them is claimed here beyond what their own `myst.yml` already asserts -- title, language,
CC BY-SA, undergraduate lecture notes -- because this site is not their publisher and a
description it invents would be the kind of unverifiable claim the rest of this file
avoids.

Their `@id`s are `<their-url>/#work`, the pattern this site uses for its own book. When
those two sites grow structured data of their own they will mint the same `@id`, and the
two halves become one entity instead of two descriptions of a URL.

The German edition of *this* book is not in that list: it is the same work in another
language, and it is already named, correctly, by the book node's `translationOfWork`.

A `Person` has no "works" property in schema.org, which is why this reads from the works'
side rather than the author's. That is also why it is not an `ItemList`: a list of three
is a claim about a page's contents, three nodes sharing an `author` is a claim about the
world, and the second one is the one being made.


Who it is for, who publishes it, and what it is made of
-------------------------------------------------------

Three properties on the book node, adopted from ds-skript `a0ba57d` (2026-10-20) in the
review TRANSLATION.md section 9 asks for; SEO-NOTES.md §30 has the measurement and the two
places this edition differs. Two are template constants in `structured-data.json`, one is
generated:

* `audience`: an `EducationalAudience` with `educationalRole: student`. Beside the
  `educationalLevel` that was already there, it says *whom* the book is for.
* `publisher`: a reference to `#author`, **not** to the university. The critique behind
  the German commit proposed the HHU; that would be false. The book is self-published --
  `llms.txt` says so in as many words -- and a `publisher: Heinrich Heine University`
  would claim an editorial role nobody holds: no editing, no ISBN, no sign-off. The
  author's `affiliation` is the claim about the university that is true, and it is
  already there. Same line as the `Course`/`provider` not claimed above.
* `hasPart`: the twenty-nine chapters, each a reference to the `Chapter` node its own
  page already carries -- the `@id` `.../<slug>/#chapter` -- with `position`, `name` and
  `url` beside the reference, so that a consumer reading this one document learns the
  reading order without fetching twenty-nine more.

`hasPart` is the inverse of the `isPartOf` every chapter already states, and like
`position` it is **read from the build, not maintained**: the order from the toc in
`config.json`, and each chapter's `name` from the `og:title` of its built page, which is
the tag the chapter's own node is named from. Not from `config.json`'s `title`, which is
where the German reads it: two documents naming one `@id` from two sources is two claims
about one entity the moment the sources disagree, and reading both from the same tag makes
that impossible rather than merely unlikely. The postcondition compares the list against
the chapter pages, not against the toc and not against itself, so a chapter the toc has
dropped or renamed fails here instead of standing.

`position` in the list is the chapter node's own -- 2 to 30, the landing page being page
1 of the book -- for the same reason: one entity, one number.

Not carried: the chapters' `description`s. Each stands on its own page as the meta
description and in that page's `Chapter` node, and twenty-nine copies on the landing page
would be 4.4 kB (measured in config.json, 2026-10-27) that say nothing a crawler does not
find at the URL beside them. The list itself grows the landing page's block from 5.9 to
15.1 kB of pretty-printed JSON, which is 1.1 kB more on the wire once gzipped -- measured
on the built page, old tool against new, same day.


The cover
---------

`Book.image` was the social card -- 1200 x 630, landscape, read back out of `og:image`.
That is the right image for a Twitter or LinkedIn preview and the wrong one for the slot
it was in: what an answer engine reaches for in `Book.image` is a *cover*, and a cover is
portrait. SEO-NOTES.md §21 is the case where that mattered -- asked about this author's
books, an answer engine attached other people's book covers, because the pages it cited
offered it nothing of the right shape.

So `image` is now `images/cover.png`, an `ImageObject` with `width` 1000, `height` 1500
and the absolute URL, written in `structured-data.json` rather than read back out of the
page. The contrast with the card is the whole reason it can be a template constant: the
card is an asset MyST fingerprints, so its URL changes on every regeneration and has to
be discovered; the cover is copied to a fixed path by `pages.yml` precisely so that its
URL is stable enough to be an `@id` (`.../#cover`) and a committed string.

The card is not demoted, it is unmoved: `og:image` and `twitter:image` are where every
social preview actually reads, `head_meta.py` still pins them to the card on all thirty
pages, and nothing here touches them. Only the node that a *book* panel reads changed.

`thumbnailUrl` is deliberately not set beside it. schema.org defines it as "a thumbnail
image relevant to the Thing" and expects a bare `URL`, so it cannot carry `width` and
`height`; and Google's Book documentation names neither `image` nor `thumbnailUrl` in its
required or recommended properties -- its book feature is a feed of editions with ISBNs
and `potentialAction`, which this book is not. There is exactly one cover raster, so a
`thumbnailUrl` today would be the same 1000 x 1500 file under a second property, i.e. a
second URL for a consumer to choose between and no new information. If a genuinely
smaller raster is ever committed (`tools/cover.py --png-width` already writes one), the
property has something true to say and goes in then.


The chapters do not carry the cover
-----------------------------------

A chapter's node restates `inLanguage`, `isAccessibleForFree` and `license` from the book,
and that is not inconsistency: those are true *of the chapter*. The cover is not. It
depicts the work, and the chapter's route to the work is the `isPartOf` it already has.

The argument the other way is real -- Google reads one document at a time, so an engine
citing one chapter sees no portrait image at all -- and it is the same argument this file
already answered for `author`, with the same answer: the identity is shared, the
properties are a fetch of the landing page away. Putting the cover on twenty-nine Chapter
nodes would assert twenty-nine times that this picture is a picture of that chapter, which
is the "thirty books" mistake one property down. A chapter page is not imageless either:
`og:image` is the card, which is the shape a link preview of a chapter wants.


BreadcrumbList
--------------

Book -> chapter, from the `toc`. One of the few structured-data types Google still
renders visibly, in place of the raw URL.


The part is not in the breadcrumb
----------------------------------

The audit asked for book -> part -> chapter, and the seven part names are right there in
the `toc`. It is two items instead, and this is measured rather than argued:

* a `ListItem` with a `name` and no `item` is valid schema.org -- the Schema Markup
  Validator passes the three-item version with no errors and no warnings -- but Google's
  Rich Results Test answers **"1 invalid item detected"** for the Breadcrumbs, and
  "invalid items are not eligible for Google Search's rich results". Google's
  documentation says `item` is required except on the last element. So the three-item
  trail does not render a breadcrumb at all; it renders nothing, and the point of this
  type is that it renders.
* there is no page for a part on this site, and the sidebar's part headings are not
  addressable, so there is no honest URL to give the middle item. Minting
  `.../#part-multivariate-stochastics` would satisfy the validator with a fragment that
  is not an anchor on any page -- the same class of mistake as a sitemap full of
  redirects, a checkable claim that does not hold.

The hierarchy is not lost: the `Chapter` node says `isPartOf` the one book and carries
its `position` in it, and the sidebar says the part to a reader on every page. If a part
ever gets a page of its own -- an `/exploratory-data-analysis/` index, say -- the middle
item has a URL and goes straight back in, which is why `chapter_graph` still takes the
part name.


What is read back, rather than computed twice
---------------------------------------------

Four things are read out of the built page instead of being recomputed here, which is
what ties this script to its place in the job. Three of them go into the markup; the
first used to, and is now kept as the check it also always was:

* the card URL, from `og:image` -- which until the cover arrived *was* the book's `image`,
  because MyST fingerprints asset filenames and the hash changes whenever the card is
  regenerated, and because `head_meta.py` may have *replaced* it with the generic card
  for a page whose figure is too small to be one (its section 6). It is now read as a
  precondition rather than copied into the node: see "The cover". An absolute `og:image`
  on the landing page is this page's equivalent of the trimmed title suffix below -- the
  proof that `head_meta.py` and the origin rewrite have both run;
* `article:modified_time`, which `freshness.py` wrote from `git log` of the chapter's
  source file, as the chapter's `dateModified`;
* `og:title` as the chapter's `name` and `og:description` as its `description`, both as
  `head_meta.py` left them -- i.e. the title with the project suffix already trimmed off,
  which is the form that was written to stand alone.

The last of those fixes the order of the job twice over, and both are checked rather than
assumed: a missing `article:modified_time` means `freshness.py` has not run, and an
`og:title` still ending in " - <project title>" means `head_meta.py` has not run. Either
is reported as that, instead of silently shipping a stale name or no date.

The book's own `dateModified` is the newest change anywhere in the book,
`freshness.book_date()`, not the landing page's own stamp: the entity described there is
the work as a whole, and a chapter revised today makes the book modified today even
though `landing-page.md` has not been touched since the 15th. Taking the landing page's
own stamp -- which is what ds-skript does, and is why its `book_date()` is computed and
then used only in a log line -- dates the whole book by one of its thirty pages. Reported
back in UPSTREAM-NOTES.md.

`position` counts the pages of the book in reading order with the landing page as page 1,
so the first chapter is 2 and the last is 30. It is the order of the `toc`, read out of
the build's own `config.json` rather than out of `myst.yml`, for the same reason
`freshness.py` reads it there: it is the table of contents the build actually used.


Running it twice
----------------

Idempotent per page: a page that already carries a `ld+json` block is left alone, so a
second run is a no-op. The postconditions at the end are checked on all thirty pages
either way -- exactly one block each, every chapter's `isPartOf` resolving to the book's
`@id`, the book's `hasPart` naming exactly the chapters that were built -- so markup MyST
has moved under us fails even on a run that wrote nothing.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import freshness  # noqa: E402  (same directory; imported for book_date and project)

TEMPLATE = Path(__file__).resolve().parent / "structured-data.json"
SIBLINGS = Path(__file__).resolve().parent / "sibling-works.json"


def meta(doc: str, kind: str, name: str) -> str | None:
    """The content of one <meta>, HTML-unescaped, or None if the page has no such tag.

    Unescaped because the value goes into JSON, where `&#x27;` is six characters and not
    an apostrophe. Every description in this book has one.
    """
    m = re.search(rf'<meta {kind}="{re.escape(name)}" content="([^"]*)"', doc)
    return html.unescape(m.group(1)) if m else None


def toc_pages(toc) -> list[tuple[str, str | None]]:
    """(slug, part title) per page in reading order. The landing page's slug is "".

    Same walk as `freshness.toc_files`, carrying the part down into the children -- which
    is the one thing that function throws away and this one needs.
    """
    out: list[tuple[str, str | None]] = []

    def walk(entries, part: str | None) -> None:
        for entry in entries:
            if "file" in entry:
                out.append((Path(entry["file"]).stem, part))
            if entry.get("children"):
                walk(entry["children"], entry.get("title", part))

    walk(toc, None)
    if not out:
        print("✗ the toc in config.json lists no files")
        return []
    out[0] = ("", None)  # the first entry is the landing page; it is served from the root
    return out


def book_node(site: str) -> dict:
    return json.loads(TEMPLATE.read_text(encoding="utf-8").replace("__SITE__", site))


def sibling_nodes(site: str, book: dict) -> list[dict]:
    """The author's other two sets of lecture notes. See "Three works, one author"."""
    nodes = json.loads(SIBLINGS.read_text(encoding="utf-8").replace("__SITE__", site))
    for node in nodes:
        # The reference has to resolve inside this same document, or the graph says
        # "some author" three times instead of "this author" three times.
        if node["author"]["@id"] != book["author"]["@id"]:
            raise SystemExit(
                f"✗ {SIBLINGS.name}: {node['name']} credits {node['author']['@id']}, "
                f"which is not the book's author {book['author']['@id']}"
            )
        if node["@id"] == book["@id"]:
            raise SystemExit(f"✗ {SIBLINGS.name}: {node['name']} reuses the book's @id")
    return nodes


def part_nodes(
    site: str, root: Path, pages: list[tuple[str, str | None]], suffix: str | None
) -> list[dict]:
    """The chapters as the book's `hasPart`, each a reference to the node its own page
    carries. See "Who it is for, who publishes it, and what it is made of".

    The name is read from the chapter page's og:title -- the same tag `chapter_graph`
    names the chapter's own node from -- and not from config.json, so the two documents
    cannot disagree about what the entity is called. That ties this to the job order the
    same way the chapter nodes are tied: head_meta.py has to have trimmed the suffix.
    """
    nodes: list[dict] = []
    for position, (slug, _) in enumerate(pages, 1):
        if not slug:
            continue  # the landing page is the book, not a part of it
        target = root / slug / "index.html"
        if not target.exists():
            raise SystemExit(f"✗ the toc names {slug}, but {target} is not built")
        name = meta(target.read_text(encoding="utf-8"), "property", "og:title")
        if not name:
            raise SystemExit(f"✗ {target} has no og:title to name the chapter with")
        if suffix and name.endswith(suffix):
            raise SystemExit(
                f'✗ {target} still has the title suffix "{suffix.strip()}" in its '
                f"og:title -- did head_meta.py run first?"
            )
        url = f"{site}/{slug}/"
        nodes.append({
            "@type": "Chapter",
            "@id": f"{url}#chapter",
            "position": position,
            "name": name,
            "url": url,
        })
    if not nodes:
        raise SystemExit("✗ the toc names no chapter besides the landing page")
    return nodes


def chapter_graph(
    site: str, slug: str, part: str | None, position: int, doc: str, book: dict
) -> dict:
    """The two nodes a chapter page carries, in one @graph with one @context."""
    url = f"{site}/{slug}/"
    name = meta(doc, "property", "og:title")
    chapter = {
        "@type": ["Chapter", "LearningResource"],
        "@id": f"{url}#chapter",
        "url": url,
        "name": name,
        "description": meta(doc, "property", "og:description"),
        "isPartOf": {"@id": book["@id"]},
        "position": position,
        # From the book node, not restated: one place says the book is free, English and
        # CC BY-SA, and a chapter cannot drift away from it.
        "inLanguage": book["inLanguage"],
        "isAccessibleForFree": book["isAccessibleForFree"],
        "license": book["license"],
        "author": {"@id": book["author"]["@id"]},
        "dateModified": meta(doc, "property", "article:modified_time"),
    }
    # Two items, not three. See "The part is not in the breadcrumb" in the docstring:
    # `part` is carried this far so that the day a part has a page of its own, the trail
    # is one line away -- and so that the reason it is missing is visible here.
    crumbs = [
        {"@type": "ListItem", "position": 1, "name": book["name"], "item": f"{site}/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": url},
    ]
    breadcrumbs = {"@type": "BreadcrumbList", "itemListElement": crumbs}
    return {"@context": "https://schema.org", "@graph": [chapter, breadcrumbs]}


def cover_file(root: Path, book: dict, site: str) -> Path | None:
    """The built file the book node's `image` claims, or None with the reason printed.

    The claim is `<site>/images/cover.png` and it is made in the template, so the only
    thing that can be wrong here is that the file is not in the artifact -- which is
    exactly the failure a schema change cannot be trusted not to have: valid markup
    pointing at a 404. Derived from the node rather than hardcoded, so moving the cover
    is one line in structured-data.json plus the copy step in pages.yml.
    """
    url = book.get("image", {}).get("url", "")
    if not url.startswith(f"{site}/"):
        print(f"✗ the book node's image is {url!r}, not a URL on {site}")
        return None
    path = root / url[len(site) + 1:]
    if not path.exists():
        print(
            f"✗ the book node claims a cover at {url}, but {path} is not in the build "
            f"-- the step in pages.yml that copies images/cover.png has not run"
        )
        return None
    return path


def landing_graph(
    site: str,
    root: Path,
    doc: str,
    book: dict,
    pages: list[tuple[str, str | None]],
    suffix: str | None,
) -> dict | None:
    """The book node, with the date of the newest change in it and its chapters in
    `hasPart`, and beside it the author's other two works. See "Three works, one
    author", "The cover" and "Who it is for, who publishes it, and what it is made of"."""
    # The card is *checked* here and no longer written into the node -- see "The cover"
    # in the docstring for why the book's `image` is the portrait cover instead. It stays
    # checked because an absolute og:image on this page is the proof that head_meta.py
    # vetted the card and that the origin was written into the build, and because the
    # cost of keeping the check is two comparisons.
    card = re.search(r'<meta property="og:image" content="([^"]+)"', doc)
    if not card:
        print(f"✗ {root / 'index.html'} has no og:image -- did head_meta.py run first?")
        return None
    if not card.group(1).startswith("http"):
        print(f"✗ the landing page still has a relative og:image: {card.group(1)}")
        return None
    if cover_file(root, book, site) is None:
        return None
    # The chapters, read from their built pages; publisher and audience are template
    # constants and already in `book`.
    book["hasPart"] = part_nodes(site, root, pages, suffix)
    # ...but the date written here is the *book's*, not this page's. See the docstring.
    book["dateModified"] = freshness.book_date(root)
    # The context moves up to the graph, as it does on a chapter page; a node inside a
    # @graph carrying its own is legal and is noise.
    book.pop("@context", None)
    return {
        "@context": "https://schema.org",
        "@graph": [book, *sibling_nodes(site, book)],
    }


def script(payload: dict) -> str:
    """The block, serialised.

    ensure_ascii so the payload survives any encoding surprise in transit; "</" is split
    because a literal </script> inside a script element would close it early.
    """
    text = json.dumps(payload, ensure_ascii=True, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json">{text}</script>'


def check(site: str, root: Path, pages: list[tuple[str, str | None]], book: dict) -> int:
    """Postconditions on all thirty pages, not a tally of this run's edits.

    It also hands the book's `dateModified` back through `book`, because on a run that
    wrote nothing -- every page already carrying a block -- nothing else here has read it,
    and a summary line reporting "as of ?" about a site that is correctly dated says the
    wrong thing about the one value the whole ordering with freshness.py exists for.
    """
    parts: list | None = None  # the landing page's hasPart, compared after the loop
    seen: list[dict] = []      # what the chapter pages actually carry
    for position, (slug, _) in enumerate(pages, 1):
        target = root / "index.html" if not slug else root / slug / "index.html"
        doc = target.read_text(encoding="utf-8")
        blocks = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', doc, re.S
        )
        if len(blocks) != 1:
            print(f"✗ {target} carries {len(blocks)} ld+json blocks, expected exactly 1")
            return 1
        try:
            payload = json.loads(blocks[0].replace("<\\/", "</"))
        except ValueError as exc:
            print(f"✗ {target} carries ld+json that does not parse: {exc}")
            return 1
        if not slug:
            # A @graph since "Three works, one author": the book node first, then the
            # author's other two works. The book is found by @id rather than by position,
            # so the order of the graph is not load-bearing.
            graph = payload.get("@graph", [payload])
            found = next((n for n in graph if n.get("@id") == book["@id"]), None)
            if not found:
                print(f"✗ the landing page's graph has no node {book['@id']}")
                return 1
            others = [n for n in graph if n is not found]
            expected = sibling_nodes(site, book)
            if len(others) != len(expected):
                print(
                    f"✗ the landing page names {len(others)} other works, "
                    f"{SIBLINGS.name} lists {len(expected)}"
                )
                return 1
            for node in others:
                if node.get("author", {}).get("@id") != book["author"]["@id"]:
                    print(f"✗ {node.get('name')} on the landing page is not credited to "
                          f"{book['author']['@id']}")
                    return 1
            # The cover, checked on the page rather than on the template: a block written
            # by an earlier run of this script, or a template edit that dropped the node,
            # both land here. Portrait is the property the image exists for -- see
            # tools/cover.py -- so it is asserted and not assumed from the file's name.
            img = found.get("image")
            if not isinstance(img, dict) or img.get("@type") != "ImageObject":
                print(f"✗ the landing page's book node has no ImageObject image: {img!r}")
                return 1
            if img.get("height", 0) <= img.get("width", 0):
                print(
                    f"✗ the book's cover is declared {img.get('width')}x"
                    f"{img.get('height')}, which is not portrait; a landscape image in "
                    f"Book.image is the banner this node exists to stop being used"
                )
                return 1
            if cover_file(root, found, site) is None:
                return 1
            # Self-published, for students, made of these chapters: the three claims
            # adopted from ds-skript a0ba57d. The first two are template constants and
            # are checked on the page all the same -- a block written by an earlier run
            # of this script predates them. hasPart is collected here and compared once
            # every chapter page has been read, below.
            publisher = found.get("publisher")
            if not isinstance(publisher, dict) or publisher.get("@id") != book["author"]["@id"]:
                print(
                    f"✗ the book's publisher is {publisher!r}; expected a reference to "
                    f"{book['author']['@id']} -- the book is self-published"
                )
                return 1
            audience = found.get("audience")
            if not isinstance(audience, dict) or audience.get("@type") != "EducationalAudience":
                print(f"✗ the book node's audience is {audience!r}, not an EducationalAudience")
                return 1
            parts = found.get("hasPart")
            if not isinstance(parts, list):
                print(f"✗ the book node has no hasPart list: {parts!r}")
                return 1
            book["dateModified"] = found.get("dateModified", "?")
            continue
        nodes = {
            tuple(n["@type"]) if isinstance(n["@type"], list) else n["@type"]: n
            for n in payload.get("@graph", [])
        }
        chapter = nodes.get(("Chapter", "LearningResource"))
        if not chapter:
            print(f"✗ {target} has no Chapter node")
            return 1
        if chapter["isPartOf"]["@id"] != book["@id"]:
            print(f"✗ {target} is part of {chapter['isPartOf']['@id']}, not {book['@id']}")
            return 1
        if chapter["author"]["@id"] != book["author"]["@id"]:
            print(f"✗ {target} credits {chapter['author']['@id']}, not the book's author")
            return 1
        if chapter["position"] != position:
            print(
                f"✗ {target} says position {chapter['position']}, "
                f"the toc says {position}"
            )
            return 1
        if "BreadcrumbList" not in nodes:
            print(f"✗ {target} has no BreadcrumbList")
            return 1
        for field in ("name", "description", "dateModified"):
            if not chapter.get(field):
                print(f"✗ {target} has an empty {field} -- did head_meta.py run first?")
                return 1
        seen.append({
            "@type": "Chapter",
            "@id": chapter["@id"],
            "position": chapter["position"],
            "name": chapter["name"],
            "url": chapter["url"],
        })
    # The book's hasPart against the chapter pages -- not against the toc, and not
    # against itself: each entry has to be the node its chapter page carries, same @id,
    # same position, same name, or the landing page and the chapters describe two books.
    if parts is None:
        print("✗ the landing page was not among the pages checked; its hasPart is unverified")
        return 1
    if parts != seen:
        have = {p.get("@id") for p in parts}
        want = {s["@id"] for s in seen}
        missing, extra = sorted(want - have), sorted(have - want)
        print(
            f"✗ the book's hasPart names {len(parts)} chapters, the build has {len(seen)}"
            + (f"; missing {missing[:3]}" if missing else "")
            + (f"; not in the build {extra[:3]}" if extra else "")
            + ("; same chapters, but a position or a name differs from the chapter's own page"
               if not missing and not extra else "")
        )
        return 1
    book["hasPart"] = parts
    return 0


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    site, root = sys.argv[1].rstrip("/"), Path(sys.argv[2])
    if not (root / "index.html").exists():
        print(f"✗ {root / 'index.html'} does not exist; run this after the HTML build")
        return 1

    book = book_node(site)
    pages = toc_pages(freshness.project(root)["toc"])
    if not pages:
        return 1

    # The suffix head_meta.py trims, derived the same way it derives it: from the landing
    # page's own <title>, which *is* the project title. A chapter whose og:title still
    # ends in it is the clearest symptom of the two being out of order in the job.
    landing_title = re.search(
        r"<title[^>]*>(.*?)</title>",
        (root / "index.html").read_text(encoding="utf-8"),
        re.S | re.I,
    )
    suffix = f" - {landing_title.group(1).strip()}" if landing_title else None

    written = skipped = 0
    for position, (slug, part) in enumerate(pages, 1):
        target = root / "index.html" if not slug else root / slug / "index.html"
        if not target.exists():
            print(f"✗ {target} is missing; the toc and the build disagree")
            return 1
        doc = target.read_text(encoding="utf-8")
        if "application/ld+json" in doc:
            skipped += 1
            continue

        # freshness.py must have run: its stamp is the proof, and its absence is the
        # clearest symptom of the two being out of order in the job.
        if not meta(doc, "property", "article:modified_time"):
            print(f"✗ {target} has no article:modified_time -- did freshness.py run first?")
            return 1

        if not slug:
            payload = landing_graph(site, root, doc, book, pages, suffix)
            if payload is None:
                return 1
        else:
            name = meta(doc, "property", "og:title")
            if not name:
                print(f"✗ {target} has no og:title to name the chapter with")
                return 1
            if suffix and name.endswith(suffix):
                print(
                    f'✗ {target} still has the title suffix "{suffix.strip()}" in its '
                    f"og:title -- did head_meta.py run first?"
                )
                return 1
            if not meta(doc, "property", "og:description"):
                print(f"✗ {target} has no og:description to describe the chapter with")
                return 1
            payload = chapter_graph(site, slug, part, position, doc, book)

        if "</head>" not in doc:
            print(f"✗ {target} has no </head>")
            return 1
        target.write_text(
            doc.replace("</head>", script(payload) + "</head>", 1), encoding="utf-8"
        )
        written += 1

    if rc := check(site, root, pages, book):
        return rc
    print(
        f"✓ structured data on {len(pages)} pages: {written} written, {skipped} already "
        f"had a block; one Book ({book['@id']}) with its {len(pages) - 1} chapters in "
        f"hasPart and its author as publisher, "
        f"{len(sibling_nodes(site, book))} further works by the same author "
        f"({book['author']['@id']}), cover {book['image']['width']}x"
        f"{book['image']['height']} at {book['image']['url']}, "
        f"as of {book.get('dateModified', '?')[:10]}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
