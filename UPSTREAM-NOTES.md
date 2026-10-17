# Findings for the German original

Things noticed while translating ds-skript that are **not** translation problems: they are
in the German book too. Nothing here has been fixed in the English edition unless the entry
says so, because an English edition that quietly corrects its original stops being a
translation of it. Collected for whoever picks ds-skript up when it unfreezes in February
2027.

Ordered roughly by how much they cost a reader.

## The PDF export silently loses content

`latexmk` runs in force mode, so `myst build --pdf` reports errors and produces a PDF
anyway, and nobody notices.

* **Figures inside an admonition are dropped.** MyST renders an admonition as a `framed`
  box and still emits `\begin{figure}[!htbp]` for a figure inside it. A float cannot live
  in a box: xelatex says "Not in outer par mode" and the figure does not appear. In
  `erwartungswert.md` this loses all four gas-container figures from the entropy
  digression.
* **An interrupted numbered list restarts at 1.** MyST emits `\begin{enumerate}[resume]`
  where a list is interrupted by a display formula and continues after it. Without the
  `enumitem` package that option is an error, and the numbering starts over — which the
  rules-of-calculation list in `erwartungswert.md` does.

*Fixed in this edition* (`templates/tex/ds-en/template.tex`): figures become non-floating
`[H]` boxes, and `enumitem` is loaded.

**Fixed upstream too**, in ds-skript `b7f8209` (2026-10-14), which is the first thing this
edition gave back to the original. That commit also sharpens the second diagnosis: without
`enumitem`, `article` does not error on `[resume]` at all — it typesets the word as literal
text, the resumed item loses its number, and the items after it run into one unnumbered
paragraph. Silent, so a non-forced build would not have caught it either.

## Factual slips

* **`dimensionsreduktion.ipynb`**: the text calls the dataset "der MNIST-Datensatz
  handgeschriebener Ziffern", but the code calls `datasets.load_digits()`, which is the
  8×8 UCI digits set, not MNIST. A heading and one sentence.
* **`explorative-analyse-beispiele.ipynb`**: block c4.5 calls the three wine classes "die
  drei Hersteller von Wein" (the three producers). The `wine.names` quotation two blocks
  above, in the same cell, says "three different cultivars", and
  `deskriptive-statistik.md` says the colour carries the grape variety. Three places, two
  stories.
* **`statistische-tests.md`**, section *Ausblick: vom Bereichsschätzer zum Test*: "mit der
  Begrifflichkeit des Formparameters aus jedem Test einen Bereichsschätzer konstruieren".
  Inverting a test into a confidence set does not go through a shape parameter.
* **`explorative-analyse-mit-numpy.ipynb`** points at "das Kapitel Modell-Auswahl, unter
  *train-test split*". `model-selection.ipynb` has no section of that name; the heading is
  *Training, Test und neue Daten*.

## Two German words for one thing

* **`intro-stochastik.md`** calls Ω the *Ergebnisraum* in one place and the *Zustandsraum*
  of a die in another. They are the same thing; the English says "sample space" and "state
  space" to match, because a translation that silently harmonises its original stops being
  one. (*Ereignisraum*, the third word in that chapter, is genuinely a different thing: the
  pair (Ω, F).)

## Cosmetic and housekeeping

* **`images/normalmarginal.png`** has an empty default axes in the bottom-left panel — a
  leftover from building a 2×2 grid without disabling the unused subplot.
* **`stochastik-programmieren.ipynb`** calls the sample space `W` in code while the prose of
  the same cell writes it $\Omega$, and passes it as the `Omega` parameter of `P`.
  *Changed in this edition*, since the code had to be touched anyway.
* **`stochastik-programmieren.ipynb`**: `transform_unit_to_dice` returns one die's pips, so
  the name wants to be `transform_unit_to_die`. Left alone here: the name is already
  English, and renaming it is an edit to the German book, not a translation.
* **`kernel-methoden.ipynb`**: a missing space in block c14.12 (`und${\lVert b \rVert}`,
  which renders as "und$\lVert b\rVert$"), and block c14.18 is ungrammatical.
* **Scikit-Learn / Scikit-learn** are spelled both ways across the book.
* **`pandas.ipynb` and `data-cleaning.ipynb`** pass `np.size` to `agg`, which is deprecated
  in current pandas.
* **`kmeans.ipynb`** block c13.0 is an HTML comment holding a link to
  `kmeans-in-action.mp4`, a file that is not in the repository.
* **Three notebooks are unseeded** where the others are seeded (`kernel-methoden.ipynb`:
  the sample, `KMeans(n_init=1)`, `train_test_split`), so their figures change on every
  re-execution. The repo's stated convention is that seeds are left as they are, which
  reads as a decision about existing seeds rather than about these.

## Six formulae that do not render, in both editions

`deskriptive-statistik.md` / `descriptive-statistics.md`: six occurrences of
`$20\,^\circ\text{C}$` and its siblings render on the **live site** as raw LaTeX behind
a warning triangle, in the interval-scale bullet and in the geometric-mean paragraph.
KaTeX reports *"Got group of unknown type: 'internal'"*: `\,` is a spacing node, so the
`^` after it has no base to attach to. LaTeX proper accepts this, KaTeX does not, and MyST
renders the failure as the source text.

Measured on the German page on 2026-10-16: **6 failed spans, same error**. It is not a
translation artefact.

Reproduced against katex 0.15.2, the version both editions load:

    20\,^\circ\text{C}        FAIL  Got group of unknown type: 'internal'
    20\,^{\circ}\text{C}      FAIL  braces on the \circ do not give ^ a base
    20\,{}^\circ\text{C}      OK    20 °C
    20^\circ\,\text{C}        OK    20° C, wrong spacing

*Fixed in this edition* as `\,{}^\circ` — the form that keeps the SI spelling, a thin
space between number and unit with `°C` as one unit. The other form that parses moves the
space inside the unit. Six occurrences, two lines, and nothing else changes.

Fixed here rather than only reported because it is a rendering defect that makes the
sentence unreadable, the same class as the `alpha=0.02` figures rather than a content
change.

## A note the other way round: `dateModified` dates the book by one page

Not a bug in the German book, a remark on `tools/freshness.py` and `tools/inject_jsonld.py`
as of ds-skript `e229a9d` — the direction of this file is usually the other way, hence the
heading.

`freshness.py` computes `book_date()`, the newest page date, and then uses it only in its
own log line. `inject_jsonld.py` sets `dateModified` from the landing page's own
`article:modified_time` instead. But the entity that block describes is the work as a whole
(`@type: Book`, `@id: …/#work`), so a chapter revised today leaves the *book* dated to
whenever the landing page was last touched.

Here that was visible immediately on the first run: the landing page last changed
2026-10-15, nineteen chapters changed on the 16th, and the book's structured data said the
15th. *Changed in this edition*: `inject_jsonld.py` imports `freshness.book_date()` and
dates the book by the newest change in it. The per-page `article:modified_time` is
untouched and still each page's own date — that one is a per-document claim and correct as
it stands.

`book_date()` being computed and then used only for a log line reads as the same
intention, arrived at and not wired up.

## And another: a shallow clone does not abort, it fabricates one date for everything

`tools/freshness.py` guards the shallow-clone case by treating an empty `git log` as the
signal, and its error message says so. That is correct for GitLab: under the default
`GIT_DEPTH: 20`, a file untouched for twenty commits genuinely has no entry in the
truncated history, the script stops, and the message points at `GIT_DEPTH: "0"`.

**It does not hold for a depth-1 clone**, which is what `actions/checkout` does by default.
Tested in a real `git clone --depth 1` of the English repository: against a commit with no
parent, git reports *every* file as modified by it, so `git log -1 -- <file>` answers for
all thirty — with HEAD's timestamp. The script then reports

    ✓ 30 pages dated, 30 sitemap entries with <lastmod>; newest change 2026-10-16

with all thirty pages carrying the deploy commit's own second, where the real dates span
three days. The build-time date the file exists to refuse, arrived at silently, by the one
route the guard does not cover.

*Added in this edition*: `refuse_shallow()` asserts
`git rev-parse --is-shallow-repository` before reading any date, and names the
`fetch-depth: 0` fix. Both directions are tested.

ds-skript is not exposed to this today — GitLab's depth-20 does produce the missing-entry
case the guard expects. It would be exposed the moment that job moved to GitHub Actions, or
if GitLab's default depth ever became 1. Asserting the depth is cheap and does not depend
on which shape the shallowness takes, so it is worth having in both.

## Things that are not errors but surprised a translator

* `Die Gausssche Normalverteilung` is the H1 of `normalverteilung.ipynb`, but three
  chapters link to it as plain `Normalverteilung`. Title and link text differ in the
  original; this edition keeps the asymmetry.
* The German varies its link texts on purpose (`Kovarianz` vs `Kovarianz und Abhängigkeit`,
  `Daten putzen` vs `Putzen der Daten`). `tools/check_links.py` is built around that:
  fewer English labels than German is fine, more is a bug.

## The web edition's preview cards and alt text

Found while acting on an external SEO critique of the English edition, 2026-10-15. All
three are in the German original too; none is fixed there.

* **MyST picks the CC BY-SA button as the preview image.** There is no site-wide
  OpenGraph image in MyST: it takes the first image of a page, and where a page has none
  it falls back to the first image of the project — which, in both editions, is the
  Creative Commons badge in the landing page's licence section. The result is that most
  chapters offer a 267 x 50 licence button as their social preview card. That is below
  the 200 x 200 that Facebook and LinkedIn require, so the card does not render at all.
  The English edition fixed this by declaring a project-level `thumbnail` (a 1200 x 630
  card generated by `tools/social_card.py`); pages with a figure of their own keep it.
  The same one-line `thumbnail:` in `myst.yml` would fix the German edition.
  *Note for whoever reads the German assessment `todo/seo-kritik-bewertung.md`: it calls
  this image "das Logo". It is not — the logo is `logo-wide.svg` and was never the
  fallback.*
* **The licence badge has no `alt` text.** Raw HTML in the landing page's licence
  paragraph: `<img src="…by-sa.png" height="20"/>`. A screen reader reads nothing where
  the licence is stated. One attribute.
* **The navbar logo has no `alt` text.** The book theme offers a `logo_alt` option and
  neither edition sets it.
* **Mermaid diagrams are invisible without JavaScript.** The landing page's course
  diagram renders as `<figure class=""></figure>` in the static HTML; the diagram source
  travels in the page's JSON payload and is drawn in the browser. There is no static
  fallback and no caption — the `mermaid` directive rejects `:caption:`. Not fixable in
  the source as things stand; a MyST limitation worth watching.

## The web edition's weight, and a GDPR problem in the GDPR book

Found auditing the English edition on 2026-10-16. **Each of the six was checked against
the live German site that same day, not inferred** — the German edition has all of them,
and the logo is the byte-identical file. The first is the one to fix regardless of
anything else.

* **`custom-style.css` embeds Google Fonts from Google's servers.** Line 3 of both
  editions' stylesheet is
  `@import url('https://fonts.googleapis.com/css2?family=Inter…&family=JetBrains+Mono…')`,
  and it is still there in `ds-skript`'s served `myst-theme.css`. It costs three things.
  It is a render-blocking chain three deep, because an `@import` nested inside a
  stylesheet can be discovered only after that stylesheet has been fetched and parsed,
  and cannot be preloaded. It puts a third party on every page view. And it hands that
  third party every reader's IP address — which is what LG München I ruled on in its
  judgment of 20 January 2022 (3 O 17493/20), awarding damages against a site operator
  for embedding Google Fonts without consent. The book has a chapter on the GDPR that
  cites the noyb complaints and the 2022 Google Analytics findings; it is served from
  fonts.googleapis.com.

  *Fixed in this edition* (2026-10-16): the two files are committed in `_site/fonts/`
  with their hashes and OFL licences in `PROVENANCE.txt`, declared as `@font-face`, and
  copied into the artifact by `pages.yml`, with a CI guard that fails the deploy if a
  `https://fonts.googleapis.com` reference ever returns. Two files cover all four
  weights, because both families are variable fonts and Google was already answering
  both weights of each with the same URL. **The fix is about 20 lines and needs no
  translation**, which is why it is first in this list.

* **Matplotlib's figures are RGBA, and PNG compresses four channels badly.** `savefig`
  writes an opaque white background and an alpha channel nobody uses. A sampled German
  figure (`5a741bbf…png`, 602×582) is 245,739 bytes and becomes 102,382 — **58% smaller**
  — stored as a 256-colour palette PNG, which for a plot is at worst a tenth of a grey
  level different and often exactly identical. Across the English edition this was 9.0 MB
  of 23.2 MB. The German edition's figures are the same plots from the same seeds, so the
  same proportion is there.

  *Fixed in this edition*: `tools/optimize_images.py`, run over the build in `pages.yml`
  and over the committed `images/` with a `--check` gate in `checks.yml`. It measures
  before it quantises and refuses anything that moves a pixel it cannot account for, and
  it leaves the four figures whose alpha channel is genuinely in use alone — flattening
  one of those onto white would look right in the build and wrong in dark mode.

* **MyST preloads every figure on the page, so nothing is deferred.** `ds-skript/kmeans/`
  ships 12 `<link rel="preload" as="image">` and zero `loading="lazy"`, which is why a
  chapter pulls its entire figure set before the load event — on the English
  `descriptive-statistics` that was 6.4 MB. Adding `loading="lazy"` alone does nothing:
  a preloaded image is fetched whatever `loading` says, and the preload wins. Both have
  to move together, and the first figure must keep both, being the LCP element.

  *Fixed in this edition* in `tools/head_meta.py`.

* **The theme loads thebe on every page, including pages with nothing to compute.**
  `thebe-core.min.js` is 359 kB on the wire and 1,278 kB decoded, and both editions fetch
  it on every page. Checked against the live German site on 2026-10-17, not inferred:
  `ds-skript/erwartungswert/` has no executed cell on it, and loads
  `/ds-skript/thebe-core.min.js` and `thebe-core-VKVHG5VY.css` anyway — the same hash as
  this edition's, i.e. the same bundle. It is not in the markup: `myst-theme`'s
  execute-scope provider renders a component whose only effect is

      useEffect(() => { core || loading || load() }, [core, load, loading])

  and `load()` appends the script to `document.head`. The gate it is missing is one the
  theme already computes for itself three lines earlier —
  `state.pages[slug].computable`, i.e. `computables.length > 0 || kind === Notebook`.
  Twelve of the thirty pages here are Markdown chapters where it is false, and the
  landing page, the commonest search entry point, is one of them.

  The theme's root `links()` has the same shape of problem one size down: it declares
  `thebe-core.css` (87 kB) and `mpl_widget.css` unconditionally, and because Remix's
  `links()` cannot see loader data, a page that needs neither cannot say so. Removing the
  tags from the built HTML only defers them — the client re-adds both after hydration.

  *Worked around in this edition* (2026-10-17): `tools/thebe_gate.py` patches that one
  expression in the built client chunk, and `tools/head_meta.py` drops the two
  stylesheets from pages with no jupyter output, which at least takes them off the
  critical path. Both are post-processing on a vendored bundle, which is the wrong place
  for it; the right place is a `start` prop or a `canCompute` check in `myst-theme`, and
  it would be a two-line change there. **This is the best candidate yet for an upstream
  issue**, since it costs every mystmd book-theme site on the web the same 359 kB.

* **No `og:url` and no `og:site_name`** on either edition. MyST writes `og:title`,
  `og:description` and `og:image` and stops. Without `og:url` a platform has no canonical
  identity for a shared link, so two spellings of one URL become two cards with two
  comment threads. *Added in this edition*, same tool.

* **`logo-wide.svg` is 437 kB and renders at 72 × 36.** Both editions serve the
  byte-identical file — 437,307 bytes, one of its seventeen paths being 117 kB of
  coordinates on its own — on every page, to fill a thumbnail. The book theme pins
  `height: 36px`, so it is 72 × 36 at every viewport width and with the mobile menu open;
  there is no size at which the vector detail is reachable.

  *Fixed in this edition* (2026-10-16): the SVG stays as the source, `tools/logo_raster.py`
  renders it to a 216 × 108 PNG (3×, so a 3×-DPR phone is pixel-exact), and `myst.yml`
  points `site.options.logo` at that. 437,307 → 18,150 bytes on disk, and — the figure
that matters — **122,702 → 18,150 on the wire, about 105 kB off every page**, since an
SVG is served gzipped and a PNG is already compressed. Two
  cautions for whoever ports it. The raster must keep the *SVG's* 2:1 viewBox and not the
  framing of the stale `logo-wide.png` that sits in both repositories unreferenced — that
  one is 609 × 417, the same drawing cropped tighter, and since the height is what is
  pinned it would have narrowed the rendered logo from 72 px to 53. And the transparency
  is load-bearing: the navbar is transparent over a background that changes with the
  reader's light/dark setting, so a logo flattened onto white is a white block in dark
  mode. A palette PNG is a third the size but shifts colours by up to 36/255, which the
  globe's three radial gradients show as banding; plain RGBA is exact.

* **The theme's own three stylesheets come from two CDNs**, on every page of both
  editions — verified on the live German site, which serves the identical three URLs with
  the identical KaTeX SRI hash:

      cdn.jsdelivr.net/npm/katex@0.15.2/dist/katex.min.css
      cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css
      cdn.jsdelivr.net/npm/jupyter-matplotlib@0.11.3/css/mpl_widget.css

  All three render-blocking, none preloadable, and on any page with mathematics up to
  twenty KaTeX font files from jsdelivr behind them — pulled relative to that stylesheet's
  own URL, so they are invisible in the HTML. Same GDPR argument as the Google Fonts
  `@import` above, and the same chapter it sits awkwardly beside.

  *Fixed in this edition* (2026-10-16): committed in `_site/vendor/` and rewritten after
  the build by `tools/vendor_assets.py`. Three cautions, each of which cost something to
  learn. **Font Awesome must not be deleted** even though no built page has a single `fa-`
  class and the browser reports the face as `unloaded`: the client bundle applies
  `fa-play`, `fa-stop` and five more to thebe's notebook controls, which appear only once
  a reader makes a notebook live, so deleting it leaves blank squares in exactly that
  feature. **The URLs are in the client bundles too**, so rewriting only the HTML means
  hydration re-adds the CDN links and the page fetches both copies. And the KaTeX
  stylesheet **names its fonts relative to itself**, so vendoring the CSS without the
  twenty woff2 files beside it silently sets the mathematics in a fallback font.

  What it does not fix, in either edition: thebe's runtime still fetches Pyodide, MathJax
  and require.js from those hosts when a reader starts a kernel. Pyodide is tens of
  megabytes; that one is not vendorable. Reading contacts no third party, running code
  does.

One thing that is **not** in the German edition: its title suffix is
`- Data Science Vorlesungsskript`, 31 characters against this edition's 48, so the
truncation finding behind `head_meta.py`'s title trimming is much milder there. Worth
knowing before someone ports that part across — the mechanism is identical, the
measurement is not.
