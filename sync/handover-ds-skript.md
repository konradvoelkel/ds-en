# Handover to ds-skript

Written 2026-10-16 from ds-en, for whoever works on the German original next. Hand it over
as a prompt; it is meant to be read start to finish and acted on in order.

Everything below was **measured on the live German site on 2026-10-16, after `e229a9d`**,
not inferred from reading the source. Measure again before you act — the numbers may have
moved, and this file does not get to be believed on its own authority any more than a
critique does.

The state of ds-en at the time of writing is commit `6234835`; `UPSTREAM-NOTES.md` there
carries the long form of every item, with the reasoning and the measurements.

---

## 0. First: three things about `e229a9d` itself

The freshness work was built in ds-skript first and ported to ds-en the same day. Porting
it turned up three things about the original, and they are at the top because they are
about code that just landed and is fresh in mind.

### 0a. The shallow-clone guard does not fire on a depth-1 clone — it fabricates

`tools/freshness.py` treats an empty `git log` as the shallow-clone signal, and the error
message says so. That is right for GitLab: under the default `GIT_DEPTH: 20`, a file
untouched for twenty commits genuinely has no entry, the script stops, and the message
points at `GIT_DEPTH: "0"`.

It does **not** hold for a depth-1 clone. Tested in a real `git clone --depth 1`: against a
commit with no parent, git reports *every* file as modified by it, so `git log -1 -- <file>`
answers for all of them, with HEAD's timestamp. The script then prints

```
✓ 30 Seiten datiert, 30 Sitemap-Eintraege mit <lastmod>; juengste Aenderung 2026-10-16
```

with every page carrying the deploy commit's own second, where the real dates spanned three
days. That is exactly the build-time date the file exists to refuse, reached silently, by
the one route the guard does not cover.

ds-en added `refuse_shallow()`, which asserts `git rev-parse --is-shallow-repository`
before reading any date and names the fix in its message. Both directions are tested there.

**ds-skript is not exposed today** — GitLab's depth-20 does produce the missing-entry case
the current guard expects. Worth adopting anyway: it costs four lines, it does not care
which shape the shallowness takes, and the exposure appears the moment that job moves to
GitHub Actions or GitLab's default depth changes.

### 0b. `dateModified` is taken from the landing page, but describes the book

`freshness.py` computes `book_date()` — the newest page date — and then uses it only in its
own log line. `inject_jsonld.py` sets `dateModified` from the landing page's own
`article:modified_time` instead. The entity that block describes is the work as a whole
(`@type: Book`, `@id: …/#work`), so a chapter revised today leaves the *book* dated to
whenever the landing page was last touched.

In ds-en this was visible on the first run: landing page last changed on the 15th, nineteen
chapters on the 16th, structured data saying the 15th. ds-en now imports
`freshness.book_date()` for that one field and leaves the per-page
`article:modified_time` alone, which is a per-document claim and correct as it is.

On the live German site today `dateModified` reads `2026-10-16T00:02:15+02:00` while
`e229a9d` itself is 10:06 — which may well be right, if that commit touched no chapter
source. The point is structural, not that today's value is wrong: the book is being dated
by one of its pages, and it is right only when those happen to coincide. `book_date()`
existing and feeding only a log line reads as the same conclusion, reached and not wired up.

### 0c. `llms_txt.py` reading `config.json` is the better choice, and the reason given is
the weaker one

The stated reason is that the `pages` job runs on python:3.13-alpine without PyYAML. ds-en
has PyYAML, so that constraint is absent — and ds-en's `freshness.py` still reads
`config.json`, because it is the build's own account of what it built: a drift between the
toc and the artifact then surfaces as the mismatch it is, and the step needs no dependency
at all. No action for you; recorded so that nobody "fixes" it back to `myst.yml` in either
repository on the grounds that PyYAML is available.

---

## 1. Six formulae that do not render — on the live site, in both editions

`deskriptive-statistik.md`: six occurrences of `$20\,^\circ\text{C}$` and its siblings
render as **raw LaTeX behind a warning triangle**, in the interval-scale bullet and in the
geometric-mean paragraph. Measured on the live German page today: **6 failed spans.**

KaTeX fails with `Got group of unknown type: 'internal'` because `\,` is a spacing node and
the `^` that follows it has no base to attach to. LaTeX proper accepts this; KaTeX does
not, and MyST renders the failure as the source text.

Reproduced against katex 0.15.2, the version both editions load:

```
20\,^\circ\text{C}        FAIL  Got group of unknown type: 'internal'
20\,^{\circ}\text{C}      FAIL  braces on the \circ do not give ^ a base
20\,{}^\circ\text{C}      OK    20 °C
20^\circ\,\text{C}        OK    20° C  -- moves the space inside the unit
```

Fix as `\,{}^\circ`: six occurrences on two lines, and it is the form that keeps the SI
spelling, a thin space between number and unit with `°C` as one unit. Already fixed in
ds-en; the divergence is tabulated in `sync/notes/descriptive-statistics.md.md`.

**Check whether anything else in the book fails the same way**, which is the part worth
more than this one fix. The count is over `class="text-myst-warning-text" title="` in the
built HTML — on the `title` and not on the class, because the same class is used by the
author's own `{warning}` admonitions, which carry no `title`:

```bash
find public -name index.html -exec grep -oh 'text-myst-warning-text" title="' {} + | wc -l
```

In ds-en that is **0** across all 30 pages now, and was 6. It is worth a line in CI: a
failed formula is structurally perfect — a span with text in it, no error status, nothing
absent — and `myst build` prints nothing. Four separate audits of ds-en missed these
because every one of them measured structure. Konrad found them by reading the page.

---

## 2. The Google Fonts `@import`, which is a GDPR problem in the GDPR book

**Do this one first if you do nothing else.** Still live today: `myst-theme.css` carries

```css
@import url('https://fonts.googleapis.com/css2?family=Inter…&family=JetBrains+Mono…');
```

Three costs at once. A render-blocking chain three deep, because an `@import` nested inside
a stylesheet is discovered only after that stylesheet has been fetched and parsed, and
cannot be preloaded. A third party on every page view. And the precise arrangement LG
München I awarded damages over on 20 January 2022 (3 O 17493/20) — in a book whose GDPR
chapter cites the noyb complaints and the 2022 Google Analytics findings.

ds-en's fix is about twenty lines and **needs no translation**: the two woff2 files are
committed in `_site/fonts/` with hashes, licences and the reasoning in `PROVENANCE.txt`,
declared as `@font-face`, copied into the artifact by the deploy, and a CI guard fails the
deploy if a `https://fonts.googleapis.com` reference ever returns.

Two details that are easy to get wrong:

* **One file per family covers all four weights.** Inter and JetBrains Mono are variable
  fonts, and Google was already answering both requested weights of each with the same URL.
* **The guard must match with the scheme** (`https://fonts.googleapis.com`), and only in
  files a browser loads. Without the scheme it also matches the sentence in the stylesheet
  explaining why the `@import` was removed; recursively it also matches the fingerprinted
  copies of *previous* builds that MyST leaves in `build/`. Either makes the guard fail for
  a reason that is not the bug.

---

## 3. The figure payload

Three separate causes, measured in ds-en, all present in ds-skript because the figures are
the same plots from the same seeds.

### 3a. Matplotlib writes RGBA that the plots do not use

`savefig` writes an opaque white background and an alpha channel nobody needs, and PNG
compresses four channels far worse than one. A sampled German figure
(`5a741bbf…png`, 602×582) is 245,739 bytes and becomes **102,382 — 58% smaller** — stored
as a 256-colour palette PNG. Across ds-en this was 9.0 MB of 23.2 MB.

ds-en's `tools/optimize_images.py` measures before it quantises: at ≤256 colours the
conversion is exactly lossless and it asserts that pixel by pixel, above that it gates on
mean and 99.9th-percentile error. Two things it refuses to do, both learned the hard way:

* **Figures whose alpha is genuinely in use are left alone.** Flattening one onto white
  looks right in the build and wrong in dark mode. The test is whether the alpha channel's
  minimum is 255, not whether the mode is RGBA.
* **A re-encode has to clear a floor** (2 kB and 2%). Without it, re-running the palette
  conversion over an already-palette image shaves a handful of bytes forever, every run
  rewrites every file, and a `--check` gate can never go green — a guard that cannot be
  satisfied teaches people to ignore it.

### 3b. MyST preloads every figure, so `loading="lazy"` on its own does nothing

Measured on `ds-skript/kmeans/` today: **12 `<link rel="preload" as="image">`, 0
`loading="lazy"`.** That preload, not the missing attribute, is why a chapter fetches its
whole figure set before the load event — on ds-en's `descriptive-statistics` that was
6.4 MB. A preloaded image is fetched whatever `loading` says; the two tags contradict each
other and the preload wins.

So both have to move together, and the first figure in `<main>` must keep both, being the
LCP candidate. ds-en pairs the removal to the set of URLs it made lazy, rather than
dropping all preloads, which is what keeps the logo's and the first figure's.

### 3c. The logo is 437 kB and renders at 72×36

Still the SVG today (`logo-wide-f752c24e2df337a8bdfd6f2c844d2050.svg`, 437,307 bytes,
byte-identical to ds-en's). One of its seventeen paths is 117 kB of coordinates on its own,
and the book theme pins `height: 36px`, so it is 72×36 at every viewport width and with the
mobile menu open. There is no size at which the vector detail is reachable.

ds-en keeps the SVG as the source and serves a 216×108 PNG (3×) rendered from it by
`tools/logo_raster.py`. Two cautions:

* **Keep the SVG's own 2:1 viewBox**, not the framing of the stale `logo-wide.png` that
  sits unreferenced in both repositories — that one is 609×417, the same drawing cropped
  tighter, and since the *height* is what is pinned it would narrow the rendered logo from
  72 px to 53.
* **The transparency is load-bearing**: the navbar is transparent over a background that
  follows the reader's light/dark setting, so a logo flattened onto white is a white block
  in dark mode. A palette PNG is a third the size but shifts colours by up to 36/255, which
  the globe's three radial gradients show as banding; plain RGBA is exact.

Honest about the size of the win: 437,307 → 18,150 bytes **on disk**, but an SVG is text
and is served gzipped, so on the wire it is 122,702 → 18,150 — about **105 kB and 85% off
every page**, not 96%. Quote the compressed pair.

---

## 4. `og:url` and `og:site_name` are absent

Measured today: **0 and 0** on `ds-skript/kmeans/`. MyST writes `og:title`,
`og:description` and `og:image` and stops. Without `og:url` a platform has no canonical
identity for a shared link, so two spellings of one URL become two cards with two comment
threads; `og:site_name` puts the book's name on the card and feeds Google's site-name
signal.

Two lines in the same post-processing loop that already writes the canonical, and `og:url`
should get the same URL the canonical has — the one with the trailing slash that answers
200.

---

## 5. The theme's three CDN stylesheets

Still three today, and the same three ds-en had, with the same KaTeX SRI hash:

```
cdn.jsdelivr.net/npm/katex@0.15.2/dist/katex.min.css
cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css
cdn.jsdelivr.net/npm/jupyter-matplotlib@0.11.3/css/mpl_widget.css
```

All render-blocking, none preloadable, and on any page with mathematics up to twenty KaTeX
font files from jsdelivr behind them — pulled relative to that stylesheet's own URL, so
they are invisible in the HTML. Same argument as §2, one step further out.

Three cautions, each of which cost something to find:

* **Font Awesome looks unused and is not.** Across all thirty built ds-en pages there was
  not one element with a `fa-` class, and the browser reports the face as `unloaded` on
  every page — the stylesheet is fetched and its font never is. On that evidence the
  obvious move is to delete the link. It is wrong: the client bundle applies `"fa fa-"`
  with `fa-play`, `fa-stop`, `fa-pause`, `fa-check`, `fa-times`, `fa-caret` and
  `fa-retweet` to **thebe's notebook controls**, which appear only once a reader makes a
  notebook live. Deleting it leaves blank squares in exactly that feature. Test it by
  injecting `class="fa fa-play"` into a built page rather than by reasoning about it.
* **The URLs are in the client bundles too**, not just the HTML. Rewriting only the
  server-rendered markup means hydration re-adds the CDN links and the page fetches both
  copies — worse than before, and invisible outside a network panel.
* **KaTeX names its fonts relative to itself**, so vendoring the stylesheet without the
  twenty woff2 files beside it silently sets the mathematics in a fallback font.

What it cannot fix, and should not claim to: thebe's runtime still fetches Pyodide, MathJax
and require.js from those hosts when a reader starts a kernel. Pyodide alone is tens of
megabytes. **Reading the book contacts no third party; running the code in it does.** So
the guard must match the three stylesheet URLs and not the hostnames — a hostname guard can
only ever be satisfied by deleting thebe.

---

## 6. Older items still open there

From `UPSTREAM-NOTES.md`, all re-checked as still live:

* **The CC BY-SA button is the `og:image` fallback.** MyST has no site-wide preview image:
  it takes the first image of a page, and where a page has none it reaches for the first
  image of the project — the Creative Commons badge in the landing page's licence section,
  267×50, below the 200×200 Facebook and LinkedIn require. A one-line project-level
  `thumbnail:` in `myst.yml` fixes it; ds-en generates a 1200×630 card with
  `tools/social_card.py`.
* **The licence badge has no `alt`**, in raw HTML in the landing page's licence paragraph.
  One attribute.
* **The navbar logo has no `alt`.** The theme has a `logo_alt` option and ds-skript does
  not set it.
* **Mermaid diagrams are invisible without JavaScript** — the course diagram is an empty
  `<figure></figure>` in the static HTML. ds-en draws an SVG from the same structure with
  `tools/course_diagram.py`, because the `mermaid` directive rejects `:caption:` and
  pre-rendering it would pull headless Chromium into the build for one picture.

---

## 7. One thing ds-en needs from ds-skript

`hreflang/filemap.json` is fetched from
`https://raw.githubusercontent.com/konradvoelkel/ds-en/main/sync/filemap.json`, which makes
that path and the shape of its `map` a **published interface** between the two
repositories. It is now recorded as such in ds-en's `sync/filemap.json` comment, so that
nobody there moves it without changing `FILEMAP_URL` in the same breath.

### And one decision that needs you

ds-en's `upstream check` workflow cannot clone ds-skript and never could: an anonymous
clone over HTTPS gets

```
fatal: could not read Username for 'https://gitlab.cs.uni-duesseldorf.de'
```

in under a second, because the repository is private. For a day this was misread as an
outage — the workflow retried for sixteen minutes and then blamed the network, having
itself printed "reachable but the clone failed" six times. ds-en now tells the two apart
and fails fast with the real reason, but that only improves the message.

The check itself still cannot run on a GitHub runner. Three ways out, none of them ds-en's
to pick alone:

1. A **read-only deploy token** for ds-skript in ds-en's GitHub secrets. Effective, and
   against a standing decision: that repository has no secrets at all today and
   `SEO-NOTES.md` section 3 treats keeping it that way as worth something.
2. **Make the dispatch carry what the check needs.** ds-skript already calls GitHub on
   push; if it also published the per-chapter block digests of its own text — the thing
   `sync.py check` actually diffs against — ds-en would need no clone at all. That is the
   most honest shape, since it is ds-skript that knows its own content, and the data is
   small.
3. **Accept that the check is local-only** and reduce the workflow to opening an issue
   saying "upstream moved to `<sha>`, run `tools/sync.py check` locally". That is what
   effectively happens now; it would just stop costing sixteen minutes and a wrong
   diagnosis.

Konrad's call. Worth knowing on your side because option 2 is work in ds-skript, and
because option 1 is the kind of thing that gets added quietly and then forgotten.

Nothing else to do here; stated so that both sides know the coupling exists. Note also that
`6f193c7`'s two extra `--verify` invariants — `x-default` equal to `hreflang=en`, and the
self-reference equal to the canonical — have been adopted into ds-en's deploy guard, where
they matter because two later steps rewrite the same `<head>` after hreflang has run.

---

## 8. Deliberately not suggested

* **Nothing about `robots.txt` from ds-en's side.** The GEO assessment's load-bearing
  finding is yours alone and ds-en has no equivalent: yours sits under `/ds-skript/` and
  therefore does not apply, the host root being a GitLab login redirect.
* **No `FAQPage` markup.** Google switched the FAQ rich results off on 2026-05-07.
* **No chunking of chapters into 150-word blocks.** Google's own AI guidance of 2026-05-15
  says explicitly that content need not be chunked for AI search.
* **No title-suffix trimming.** ds-en shortens its `<title>` suffix; ds-skript's is
  `- Data Science Vorlesungsskript`, 31 characters against ds-en's 48, so the measurement
  that justified it there is much milder here. It is known and decided separately.
  If it is ever done: the theme re-renders the title from the hydration payload, so editing
  `<title>` in the markup alone is undone in the browser — and Google renders before it
  indexes.
