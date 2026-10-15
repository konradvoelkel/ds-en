#!/usr/bin/env python3
"""Link each chapter to its German counterpart with hreflang.

    python3 tools/hreflang.py <site-url> <german-site-url> <html-dir>
    python3 tools/hreflang.py --verify <site-url> <german-site-url>

The pairing is not guessed: `sync/filemap.json` already maps every German source file
to its English counterpart, it is what the staleness tooling runs on, and CI checks it.
A chapter-to-chapter hreflang is exactly that mapping, rendered as link tags. Slugs differ
between the editions (`kovarianz` / `covariance`), which is precisely the case hreflang
exists for.

Three tags per page: the German counterpart, a self-reference (required -- a cluster
whose members do not name themselves is ignored), and `x-default`. x-default points at
the English edition: with no language-selector page to send it to, it should name the
edition that serves the widest audience of readers whose language matches neither.

**A one-sided hreflang is ignored.** The German edition has to carry the mirror image of
these tags, or none of this counts. CI here can only check this edition's half; `--verify`
fetches the German pages and checks the other half, which is the thing to run once
ds-skript has landed its side.
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is missing. Run with: uv run --with pyyaml python tools/hreflang.py …")

ROOT = Path(__file__).resolve().parent.parent


def pairs() -> list[tuple[str, str]]:
    """(English file, German file) in the book's reading order."""
    fmap = json.loads((ROOT / "sync" / "filemap.json").read_text())["map"]
    inverse = {en: de for de, en in fmap.items() if en}
    cfg = yaml.safe_load((ROOT / "myst.yml").read_text(encoding="utf-8"))

    def walk(toc):
        for entry in toc:
            if "file" in entry:
                yield entry["file"]
            for child in entry.get("children", []):
                yield from walk([child])

    out = []
    for en in walk(cfg["project"]["toc"]):
        if en not in inverse:
            raise SystemExit(
                f"{en} is in the toc but has no German counterpart in sync/filemap.json. "
                "Either add the mapping or this page must not claim an alternate."
            )
        out.append((en, inverse[en]))
    return out


def urls(en_file: str, de_file: str, site: str, de_site: str, first: bool) -> tuple[str, str]:
    """The first toc entry is each edition's site root; every other page is its stem."""
    if first:
        return f"{site}/", f"{de_site}/"
    return f"{site}/{Path(en_file).stem}/", f"{de_site}/{Path(de_file).stem}/"


def tags(en_url: str, de_url: str) -> str:
    return (
        f'<link rel="alternate" hreflang="en" href="{en_url}"/>'
        f'<link rel="alternate" hreflang="de" href="{de_url}"/>'
        f'<link rel="alternate" hreflang="x-default" href="{en_url}"/>'
    )


def inject(site: str, de_site: str, html: Path) -> int:
    seen_de: dict[str, str] = {}
    for n, (en_file, de_file) in enumerate(pairs()):
        en_url, de_url = urls(en_file, de_file, site, de_site, n == 0)
        if de_url in seen_de:
            print(f"✗ {de_url} is claimed by both {seen_de[de_url]} and {en_file}")
            return 1
        seen_de[de_url] = en_file

        page = html / ("index.html" if n == 0 else f"{Path(en_file).stem}/index.html")
        if not page.exists():
            print(f"✗ {page} does not exist; the toc and the build disagree")
            return 1
        text = page.read_text(encoding="utf-8")
        if "hreflang" in text:
            continue
        # The self-reference must be the URL the page actually calls canonical, or the
        # cluster names a page that does not consider itself a member.
        canonical = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        if not canonical:
            print(f"✗ {page} has no canonical yet; hreflang must run after it")
            return 1
        if canonical.group(1) != en_url:
            print(f"✗ {page}: canonical is {canonical.group(1)}, hreflang would say {en_url}")
            return 1
        page.write_text(text.replace("</head>", tags(en_url, de_url) + "</head>", 1),
                        encoding="utf-8")
    print(f"✓ hreflang on {len(seen_de)} pages, paired with {de_site}")
    return 0


def verify(site: str, de_site: str) -> int:
    """Fetch the German pages and check they name the English ones back."""
    bad = 0
    for n, (en_file, de_file) in enumerate(pairs()):
        en_url, de_url = urls(en_file, de_file, site, de_site, n == 0)
        try:
            with urllib.request.urlopen(de_url, timeout=30) as r:
                body = r.read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001 -- any failure is the same answer here
            print(f"✗ {de_url}: {exc}")
            bad += 1
            continue
        back = re.findall(r'<link rel="alternate" hreflang="en" href="([^"]+)"', body)
        if not back:
            print(f"✗ {de_url} carries no hreflang=\"en\" -- the pair is one-sided and ignored")
            bad += 1
        elif en_url not in back:
            print(f"✗ {de_url} points at {back[0]}, expected {en_url}")
            bad += 1
    total = len(pairs())
    print(f"-- {total - bad}/{total} pairs are bidirectional")
    return 1 if bad else 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--verify" in sys.argv:
        if len(args) != 2:
            print(__doc__)
            return 2
        return verify(args[0].rstrip("/"), args[1].rstrip("/"))
    if len(args) != 3:
        print(__doc__)
        return 2
    return inject(args[0].rstrip("/"), args[1].rstrip("/"), Path(args[2]))


if __name__ == "__main__":
    raise SystemExit(main())
