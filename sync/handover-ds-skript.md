# Prompt for the ds-skript agent

Rewritten 2026-10-16 from ds-en (`492e6ac`), against ds-skript `825aef2` and its live
site. The previous version of this file was four hours old and already wrong in four
places — ds-skript had fixed them in the meantime. **Re-measure before you act on any
line below.** Every number here was taken from the live German site today, and this file
has no more authority than a critique does.

Commands assume you are in the ds-skript working tree.

---

## Already done, so that nobody redoes it

Checked live today and confirmed finished on your side: `article:modified_time` and
`<lastmod>` 32/32 · `alt` on the navbar logo and the licence badge · the mermaid diagram
(no empty `<figure>` left) · the social card, so `og:image` is no longer the CC BY-SA
button · `refuse_shallow()` and the `_git()` helper, adopted from ds-en in `dedfd0b`.

Two notes on `dedfd0b`, neither a defect:

* **`--stamp-source` and the visible date have no counterpart in ds-en**, deliberately:
  the theme re-renders the page header from the hydration payload, so a line written into
  the markup is gone after hydration. Your route through the frontmatter before the build
  is the one that actually survives, and it is better than ds-en's "wait to be asked".
  Worth porting the other way at some point.
* **Your landing page's `article:modified_time` is the newest of all pages, not its own.**
  ds-en kept that tag per-document and imports `book_date()` only for the JSON-LD. Yours
  is defensible — the landing page is the title page, and "Stand der Ausgabe" is the right
  claim there — but it is a divergence, and `article:modified_time` is normally a
  per-document claim. Flagged, not objected to.

---

## 1. Six formulae do not render, still (measured live today: 6)

`deskriptive-statistik.md` lines 65 and 84, six occurrences of `\,^\circ`:

```
20\,^\circ\text{C}        FAIL  Got group of unknown type: 'internal'
20\,^{\circ}\text{C}      FAIL  braces on \circ do not give ^ a base
20\,{}^\circ\text{C}      OK    20 °C          <- the fix
20^\circ\,\text{C}        OK    20° C          <- wrong: space moves inside the unit
```

`\,` is a spacing node, so the `^` after it has no base. LaTeX accepts it, KaTeX does not,
and MyST renders the failure as the literal source behind a warning triangle. Reproduced
against katex 0.15.2, the version you load. Fix: `sed -i 's/\\,\^\\circ/\\,{}^\\circ/g'`
on that one file, six occurrences, two lines.

**The more valuable half is the count, not the fix.** Add it to CI:

```bash
find public -name index.html -exec grep -oh 'text-myst-warning-text" title="' {} + | wc -l
```

On `title=`, not on the class — the same class styles your own `{warning}` admonitions,
which carry no `title`. ds-en went 6 → 0 and now guards it. Four separate audits of ds-en
missed these because they all measured structure, and a failed formula is structurally
perfect: a span with text in it, no error status, nothing absent, and `myst build` prints
nothing. A human found them by reading the page.

## 2. Google Fonts, which is a GDPR problem in the GDPR book (measured live: still there)

`myst-theme.css` line 3 still carries
`@import url('https://fonts.googleapis.com/css2?family=Inter…&family=JetBrains+Mono…')`.

Three costs: a render-blocking chain three deep (an `@import` nested in a stylesheet is
discovered only after that stylesheet is fetched and parsed, and cannot be preloaded); a
third party on every page view; and the exact arrangement LG München I awarded damages
over on 20 January 2022 (3 O 17493/20) — in a book whose GDPR chapter cites noyb and the
2022 Google Analytics findings.

ds-en's fix is ~20 lines and needs no translation; see `_site/fonts/PROVENANCE.txt` there.
Two things to get right:

* **One file per family covers all four weights** — Inter and JetBrains Mono are variable
  fonts, and Google was already serving both requested weights of each from one URL.
* **Guard with the scheme** (`https://fonts.googleapis.com`), and only over files a
  browser loads. Without the scheme it matches the comment explaining the removal;
  recursively it matches the fingerprinted copies of earlier builds MyST leaves in
  `build/`. Either makes the guard fail for a reason that is not the bug.

## 3. The figure payload: three causes, one of which cancels another

### 3a. Preloads, which make `loading="lazy"` a no-op (measured live: 12 preloads, 0 lazy)

MyST emits `<link rel="preload" as="image">` for **every** figure. That, not the missing
attribute, is why a chapter fetches its whole figure set before the load event. A
preloaded image is fetched whatever `loading` says. **Adding the attribute alone changes
nothing** — the two must move together, and the first figure in `<main>` keeps both, being
the LCP candidate. Pair the removal to the set of URLs you made lazy rather than dropping
all preloads, which is what keeps the logo's.

### 3b. Matplotlib writes RGBA the plots do not use

`savefig` writes an opaque white background plus an alpha channel nobody needs, and PNG
compresses four channels far worse than one. Sampled from your site: `5a741bbf…png`,
602×582, **245,739 → 102,382 bytes (58%)** as a 256-colour palette PNG. Across ds-en this
was 9.0 MB of 23.2 MB.

Two refusals worth copying from `tools/optimize_images.py`:

* **Leave figures whose alpha is genuinely in use.** Flattening one onto white looks right
  in the build and wrong in dark mode. Test the alpha channel's minimum, not the mode.
* **Give the re-encode a floor** (2 kB and 2%). Without it, re-running the palette
  conversion over an already-palette image shaves a few bytes forever, every run rewrites
  every file, and a `--check` gate can never go green — a guard that cannot be satisfied
  teaches people to ignore it.

### 3c. The logo is 437 kB and renders at 72×36 (measured live: still the SVG)

`logo-wide.svg`, 437,307 bytes, byte-identical to ds-en's; one of its seventeen paths is
117 kB of coordinates. The theme pins `height: 36px`, so it is 72×36 at every viewport
width and with the mobile menu open — there is no size at which the vector detail is
reachable. ds-en keeps the SVG as source and serves a 216×108 PNG (3×).

* **Keep the SVG's own 2:1 viewBox**, not the framing of the stale `logo-wide.png` sitting
  unreferenced in both repositories (609×417, same drawing cropped tighter). Since the
  *height* is pinned, that framing would narrow the rendered logo from 72 px to 53.
* **Transparency is load-bearing** — the navbar is transparent over a background that
  follows light/dark, so a logo flattened onto white is a white block in dark mode. A
  palette PNG is a third the size but shifts colours up to 36/255, which the globe's three
  radial gradients show as banding. Plain RGBA is exact.
* **Quote the compressed figure.** 437,307 → 18,150 on disk, but an SVG is served gzipped:
  on the wire it is 122,702 → 18,150, about **105 kB and 85% off every page**, not 96%.

## 4. `og:url` and `og:site_name` absent (measured live: 0 and 0)

MyST writes `og:title`, `og:description`, `og:image` and stops. Without `og:url` a platform
has no canonical identity for a shared link, so two spellings of one URL become two cards
with two comment threads. Two lines in the loop that already writes the canonical, and
`og:url` gets the same URL the canonical has — the one with the trailing slash that
answers 200.

## 5. Three CDN stylesheets, plus the KaTeX fonts behind them (measured live: 3)

```
cdn.jsdelivr.net/npm/katex@0.15.2/dist/katex.min.css
cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css
cdn.jsdelivr.net/npm/jupyter-matplotlib@0.11.3/css/mpl_widget.css
```

All render-blocking, none preloadable, and on any page with mathematics up to twenty KaTeX
font files behind them — pulled relative to that stylesheet's own URL, so invisible in the
HTML. Same argument as §2, one step out. Three traps, each of which cost something:

* **Font Awesome looks unused and is not.** No built page has an `fa-` class and the
  browser reports the face as `unloaded` — the stylesheet is fetched, its font never is.
  The obvious move is to delete the link, and it is wrong: the client bundle applies
  `fa-play`, `fa-stop`, `fa-pause`, `fa-check`, `fa-times`, `fa-caret`, `fa-retweet` to
  **thebe's notebook controls**, which exist only once a reader makes a notebook live.
  Test by injecting `class="fa fa-play"` into a built page, not by reasoning.
* **The URLs are in the client bundles too.** Rewriting only the server-rendered markup
  means hydration re-adds the CDN links and the page fetches both copies — worse than
  before, invisible outside a network panel.
* **KaTeX names its fonts relative to itself**, so vendoring the stylesheet without the
  twenty woff2 files beside it silently sets the mathematics in a fallback font.

What this cannot fix, and must not claim to: thebe's runtime still fetches Pyodide,
MathJax and require.js from those hosts when a reader starts a kernel. Pyodide alone is
tens of megabytes. **Reading the book contacts no third party; running the code in it
does.** So match the three stylesheet URLs, never the hostnames — a hostname guard can
only ever be satisfied by deleting thebe.

---

## 6. One decision that is partly yours

ds-en's `upstream check` workflow cannot clone ds-skript and never could: an anonymous
HTTPS clone gets `fatal: could not read Username` in under a second, because the
repository is private. For a day this was misread as an outage — the workflow retried
sixteen minutes and blamed the network while printing "reachable but the clone failed" six
times. ds-en now tells the two apart and fails fast with the real reason, but that only
improves the message; the staleness check still cannot run in CI.

Three ways out, and the second is work on your side:

1. A read-only deploy token in ds-en's GitHub secrets. Effective, and against a standing
   decision: that repository has no secrets at all today.
2. **Have the dispatch carry the per-chapter block digests of the German text** — the
   thing `sync.py check` actually diffs against. Then no clone is needed. The most honest
   shape, since ds-skript is what knows its own content, and the data is small.
3. Reduce the workflow to opening an issue saying "upstream moved to `<sha>`, run
   `tools/sync.py check` locally", which is what effectively happens now, minus the
   sixteen minutes and the wrong diagnosis.

Konrad's call. Also note that `sync/filemap.json` in ds-en is now a **published
interface**: `6f193c7` fetches it from raw.githubusercontent.com, so that path and the
shape of its `map` cannot move without changing `FILEMAP_URL` in the same breath. It is
recorded as such in that file's own comment.

---

## 7. Deliberately not suggested

* **Nothing about `robots.txt`.** That finding is yours alone and ds-en has no equivalent;
  it needs no input from here.
* **No `FAQPage` markup** — Google switched the FAQ rich results off on 2026-05-07.
* **No chunking into 150-word blocks** — Google's AI guidance of 2026-05-15 says
  explicitly that content need not be chunked for AI search.
* **No title-suffix trimming.** ds-skript's suffix is `- Data Science Vorlesungsskript`,
  31 characters against ds-en's 48, so the measurement that justified it there is much
  milder here, and `site.title` is unset so the lever exists if it is ever wanted. If it
  is done: the theme re-renders the title from the hydration payload, so editing `<title>`
  in the markup alone is undone in the browser — and Google renders before it indexes.
