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

Four values are read out of the built page instead of being recomputed here, which is
what ties this script to its place in the job:

* the card URL, from `og:image`, because MyST fingerprints asset filenames and the hash
  changes whenever the card is regenerated -- and because `head_meta.py` may have
  *replaced* it with the generic card for a page whose figure is too small to be one
  (its section 6);
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
`@id` -- so markup MyST has moved under us fails even on a run that wrote nothing.
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


def landing_graph(site: str, root: Path, doc: str, book: dict) -> dict | None:
    """The book node, with the preview card and the date of the newest change in it."""
    card = re.search(r'<meta property="og:image" content="([^"]+)"', doc)
    if not card:
        print(f"✗ {root / 'index.html'} has no og:image to point the structured data at")
        return None
    if not card.group(1).startswith("http"):
        print(f"✗ the landing page still has a relative og:image: {card.group(1)}")
        return None
    book["image"] = card.group(1)
    # ...but the date written here is the *book's*, not this page's. See the docstring.
    book["dateModified"] = freshness.book_date(root)
    return book


def script(payload: dict) -> str:
    """The block, serialised.

    ensure_ascii so the payload survives any encoding surprise in transit; "</" is split
    because a literal </script> inside a script element would close it early.
    """
    text = json.dumps(payload, ensure_ascii=True, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json">{text}</script>'


def check(root: Path, pages: list[tuple[str, str | None]], book: dict) -> int:
    """Postconditions on all thirty pages, not a tally of this run's edits.

    It also hands the book's `dateModified` back through `book`, because on a run that
    wrote nothing -- every page already carrying a block -- nothing else here has read it,
    and a summary line reporting "as of ?" about a site that is correctly dated says the
    wrong thing about the one value the whole ordering with freshness.py exists for.
    """
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
            if payload.get("@id") != book["@id"]:
                print(f"✗ the landing page's node is not {book['@id']}")
                return 1
            book["dateModified"] = payload.get("dateModified", "?")
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
            payload = landing_graph(site, root, doc, book)
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

    if rc := check(root, pages, book):
        return rc
    print(
        f"✓ structured data on {len(pages)} pages: {written} written, {skipped} already "
        f"had a block; one Book ({book['@id']}), {len(pages) - 1} chapters, one author "
        f"({book['author']['@id']}), as of {book.get('dateModified', '?')[:10]}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
