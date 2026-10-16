"""Insert the JSON-LD description of the book into the built landing page.

    python3 tools/inject_jsonld.py <site-url> <html-file>

Run from the deploy workflow, after the origin has been written into the build. MyST
emits no structured data of its own, and the block cannot live in `landing-page.md`: a
`{raw} html` directive there would be an extra block and break the block alignment with
the German original (TRANSLATION.md section 1). So it is added to the built HTML instead.

Only the landing page gets it. The entity is the book as a whole; repeating it per chapter
would assert 30 books.

Deliberately *not* claimed, though an external critique proposed them: `Course`,
`hasCourseInstance` and `"provider": HHU`. The English edition is not a course offered by
the university -- it is a translated book. The author's affiliation is a different claim,
and that one is true, so it stays.

Two values are read back out of the page rather than recomputed here:

* the card URL, from `og:image`, because MyST fingerprints asset filenames and the hash
  changes whenever the card is regenerated;
* the presence of the `article:modified_time` that `tools/freshness.py` wrote just
  before -- which is what ties this script to the order of the job: freshness.py first,
  this second.

The date itself is taken from `freshness.book_date()`, the newest change anywhere in the
book, because the entity described here is the book and not the landing page. See the
comment at the point of use.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import freshness  # noqa: E402  (same directory; imported for book_date)

TEMPLATE = Path(__file__).resolve().parent / "structured-data.json"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    site, target = sys.argv[1].rstrip("/"), Path(sys.argv[2])

    html = target.read_text(encoding="utf-8")
    if "application/ld+json" in html:
        print(f"✓ {target} already carries structured data; left alone")
        return 0

    data = json.loads(TEMPLATE.read_text(encoding="utf-8").replace("__SITE__", site))

    card = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    if not card:
        print(f"✗ {target} has no og:image to point the structured data at")
        return 1
    if not card.group(1).startswith("http"):
        print(f"✗ {target} still has a relative og:image: {card.group(1)}")
        return 1
    data["image"] = card.group(1)

    # freshness.py must have run: its stamp is the proof, and its absence is the clearest
    # symptom of the two being out of order in the job.
    if not re.search(r'<meta property="article:modified_time" content="([^"]+)"', html):
        print(f"✗ {target} has no article:modified_time -- did freshness.py run first?")
        return 1

    # ...but the date written here is the *book's*, not this page's. The entity is the
    # work as a whole (@type Book, @id .../#work), and a chapter revised today makes the
    # book modified today even though landing-page.md has not been touched since the 15th.
    # Taking the landing page's own stamp -- which is what ds-skript does, and is why its
    # book_date() is computed and then used only in a log line -- dates the whole book by
    # one of its thirty pages. Reported back in UPSTREAM-NOTES.md.
    data["dateModified"] = freshness.book_date(target.parent)

    # ensure_ascii so the payload survives any encoding surprise in transit; "</" is split
    # because a literal </script> inside a script element would close it early.
    payload = json.dumps(data, ensure_ascii=True, indent=2).replace("</", "<\\/")
    block = f'<script type="application/ld+json">{payload}</script>'

    if "</head>" not in html:
        print(f"✗ {target} has no </head>")
        return 1
    target.write_text(html.replace("</head>", block + "</head>", 1), encoding="utf-8")
    print(
        f"✓ structured data added to {target} ({len(payload)} bytes, "
        f"image {data['image'].split('/')[-1]}, as of {data['dateModified'][:10]})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
