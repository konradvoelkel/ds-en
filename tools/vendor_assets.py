#!/usr/bin/env python3
"""Serve the theme's three third-party stylesheets from this origin instead of two CDNs.

    python3 tools/vendor_assets.py <html-dir> [--base BASE_URL]

Every page fetched three render-blocking stylesheets from `cdn.jsdelivr.net` and
`cdnjs.cloudflare.com`, and any page with mathematics fetched up to twenty font files from
jsdelivr on top of them -- nine on expectation-variance alone, pulled by the KaTeX
stylesheet relative to its own URL. That is a third party holding the IP address of every
reader of a book with a GDPR chapter, which is the argument `_site/fonts/PROVENANCE.txt`
already makes about the Google Fonts `@import`.

The difference is whose markup it is. The `@import` was line 3 of our own stylesheet and
could simply be deleted. These `<link>` tags are the MyST book theme's, so they are
rewritten after the build -- which is this tool. The files themselves are committed in
`_site/vendor/`, unmodified, with hashes and licences.


The part that makes this more than a sed
----------------------------------------

**The URLs are in the client JavaScript as well as in the HTML.** Remix renders `<head>`
links from route modules, so the bundle carries the same three URLs; `root-*.js` and two
shared chunks contain them. Rewriting only the server-rendered markup would have the page
load correctly and then, on hydration, re-add the CDN links -- fetching both copies, which
is worse than before the change and invisible unless you look at the network panel.

This is the same trap `head_meta.py` hit with the title, found the same way: by loading
the rewritten page rather than grepping it. So the rewrite covers `.html` and `.js` alike,
and the deploy guard greps the whole artifact rather than the HTML.


Why it fails instead of falling back
------------------------------------

Each URL is matched by a pattern that allows *any* version, so a MyST upgrade that bumps
KaTeX is reported as exactly that -- "the theme asks for katex@0.16.0, _site/vendor has
0.15.2" -- instead of as a string that could not be found. It then exits non-zero.

That is deliberate. The tempting behaviour is to leave an unknown version pointing at the
CDN so the build keeps working; that silently restores the thing this directory exists to
remove, and the guard in `pages.yml` would catch it only because it greps for the CDN
hostnames at all. Better to stop and be re-vendored.


What this does *not* remove, and must not claim to
--------------------------------------------------

After this runs the two CDN hostnames still appear in three files, and that is correct:

    thebe-lite.min.js   https://cdn.jsdelivr.net/pyodide/v0.27.0/full/pyodide.js
    thebe-core.min.js   cdnjs .../mathjax/2.7.5, .../require.js/2.3.6, cdn.jsdelivr.net/npm/
    build/_shared/chunk-LS4ALTVG.js   the same three

That is thebe's runtime -- the in-browser Python kernel and the loader for Jupyter widget
packages -- and it is fetched only when a reader presses the button that makes a notebook
live. Pyodide alone is tens of megabytes before any package; vendoring it is not on the
table, and a reader who has asked to run Python in their browser has asked for a network
fetch by definition.

So the accurate claim is narrow and worth stating narrowly: **reading the book now
contacts no third party. Running the code in it still does.** The deploy guard therefore
greps for the three stylesheet URLs rather than for the hostnames -- a guard that failed
on any mention of jsdelivr could only be satisfied by deleting thebe.

(`vendor/PROVENANCE.txt` also quotes all three URLs, being the file that explains them.
It is published with the licences, as the OFL requires for the Font Awesome face, and is
not rewritten: only `.html` and `.js` are.)


`integrity` and `crossorigin` are dropped
-----------------------------------------

The theme emits the KaTeX link with an SRI hash and `crossorigin="anonymous"`. The hash
would in fact still validate -- the vendored file is byte-exact, which was confirmed
*against that very hash* at vendor time -- but it is removed anyway, with the attribute
that goes with it. A hash pinned to one version of a file that now lives in this
repository is a tripwire for whoever next updates it: the stylesheet would not fail
loudly, it would simply be blocked, and the site would lose its mathematics typesetting
with nothing in the build log. Same-origin assets here are covered by the repository, not
by SRI.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import sys

# Each entry: a regex matching the theme's URL with any version, the version actually
# vendored, and the path the rewrite points at (relative to the site root).
ASSETS = [
    (
        r"https://cdn\.jsdelivr\.net/npm/katex@([\d.]+)/dist/katex\.min\.css",
        "0.15.2",
        "vendor/katex/katex.min.css",
    ),
    (
        r"https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/([\d.]+)/css/font-awesome\.css",
        "4.7.0",
        "vendor/font-awesome/css/font-awesome.css",
    ),
    (
        r"https://cdn\.jsdelivr\.net/npm/jupyter-matplotlib@([\d.]+)/css/mpl_widget\.css",
        "0.11.3",
        "vendor/jupyter-matplotlib/mpl_widget.css",
    ),
]

VENDOR_SRC = pathlib.Path("_site/vendor")


def strip_integrity(doc: str, local: str) -> str:
    """Drop integrity= and crossorigin= from a <link> now pointing at a local file."""

    def fix(m: re.Match) -> str:
        tag = m.group(0)
        if local not in tag:
            return tag
        tag = re.sub(r'\s+integrity="[^"]*"', "", tag)
        tag = re.sub(r'\s+crossorigin="[^"]*"', "", tag)
        return tag

    return re.sub(r"<link\b[^>]*>", fix, doc)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("html_dir")
    ap.add_argument("--base", default="", help="BASE_URL, the path the site is served from")
    args = ap.parse_args()

    root = pathlib.Path(args.html_dir)
    if not (root / "index.html").exists():
        sys.exit(f"::error::{root}/index.html does not exist; run this after the HTML build")
    if not VENDOR_SRC.is_dir():
        sys.exit(f"::error::{VENDOR_SRC} is missing; it holds the committed stylesheets")

    shutil.copytree(VENDOR_SRC, root / "vendor", dirs_exist_ok=True)
    vendored = sum(1 for p in (root / "vendor").rglob("*") if p.is_file())

    files = [p for p in root.rglob("*") if p.suffix in (".html", ".js") and p.is_file()]
    counts = {local: 0 for _, _, local in ASSETS}
    referenced = {local: False for _, _, local in ASSETS}

    for f in files:
        try:
            doc = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        before = doc
        for pattern, want, local in ASSETS:
            for version in set(re.findall(pattern, doc)):
                if version != want:
                    sys.exit(
                        f"::error::{f} asks for version {version} of {local.split('/')[1]}, "
                        f"but _site/vendor has {want}. The theme has been upgraded: refetch "
                        f"that stylesheet and its fonts, check the hashes, and update "
                        f"_site/vendor/PROVENANCE.txt and ASSETS in this file."
                    )
            doc, n = re.subn(pattern, f"{args.base}/{local}", doc)
            counts[local] += n
            if f"{args.base}/{local}" in doc:
                referenced[local] = True
        if doc != before:
            if f.suffix == ".html":
                for _, _, local in ASSETS:
                    doc = strip_integrity(doc, local)
            f.write_text(doc, encoding="utf-8")

    # Postconditions, not a tally of this run's edits: running twice is a legitimate
    # no-op that must still pass, while a theme that stopped loading one of these -- or
    # started loading it from a URL these patterns miss -- must fail.
    missing = [local for local, ok in referenced.items() if not ok]
    if missing:
        sys.exit(
            "::error::nothing in the build references these, before or after the "
            f"rewrite: {', '.join(missing)}. Either the theme stopped loading them -- in "
            "which case drop them from ASSETS and from _site/vendor -- or it now loads "
            "them from a URL these patterns do not match, and the CDN is still being hit."
        )

    # Every vendored file must be reachable at the path the rewrite now names.
    for _, _, local in ASSETS:
        if not (root / local).is_file():
            sys.exit(f"::error::rewrote references to /{local}, which is not in the artifact")

    breakdown = ", ".join(f"{local.split('/')[1]}={counts[local]}" for _, _, local in ASSETS)
    print(
        f"vendor_assets: {vendored} files copied to /vendor, {sum(counts.values())} CDN "
        f"references rewritten across {len(files)} html/js files ({breakdown})"
    )


if __name__ == "__main__":
    main()
