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

The card URL is read back out of the page's own og:image rather than hardcoded, because
MyST fingerprints asset filenames and the hash changes whenever the card is regenerated.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

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

    # ensure_ascii so the payload survives any encoding surprise in transit; "</" is split
    # because a literal </script> inside a script element would close it early.
    payload = json.dumps(data, ensure_ascii=True, indent=2).replace("</", "<\\/")
    block = f'<script type="application/ld+json">{payload}</script>'

    if "</head>" not in html:
        print(f"✗ {target} has no </head>")
        return 1
    target.write_text(html.replace("</head>", block + "</head>", 1), encoding="utf-8")
    print(f"✓ structured data added to {target} ({len(payload)} bytes, image {data['image'].split('/')[-1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
