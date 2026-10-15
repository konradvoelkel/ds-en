# HHU Data Science course — English edition

**Read it at <https://datascience.konradvoelkel.com/>**

English edition of the lecture notes for the course "Data Science" at
Heinrich Heine University Düsseldorf, 4th semester of the BSc in Computer Science.

The German original lives in a separate repository, **ds-skript**
(`gitlab.cs.uni-duesseldorf.de/voelkel/ds-skript`), and remains the source of truth.
This repository mirrors the Jupyter Book part of it — the Markdown chapters and the
notebooks — in English. Slides, exercise sheets and exams are not mirrored.

## How this translation is maintained

All 30 chapters are translated. Translation is done chapter by chapter and reviewed, not
generated on the fly, so the English text can be written as English rather than as
transposed German.
What *is* automated is noticing when the German original changes:

* `sync/upstream.json` pins the ds-skript commit this edition corresponds to.
* `sync/filemap.json` maps every German file to its English counterpart.
* `sync/segments/` records a hash per source block (paragraph, admonition, notebook cell).
* `tools/` holds the segmentation and the staleness check that turns an upstream diff
  into a list of English passages that need re-translating.

What it does *not* notice is everything outside the mirrored chapters: the original's CI
configuration, its `myst.yml`, its tooling. Those have to be followed by hand — see
`TRANSLATION.md` §9, which exists because that gap once left this site serving a sitemap
full of `localhost` URLs.

English and German text are kept in **strict block alignment**: same number of
paragraphs and notebook cells, same order. Translators and style passes may restructure
freely *within* a block, never across block boundaries. That invariant is what lets the
staleness check point at an exact paragraph instead of a whole chapter.

See `TRANSLATION.md` for the conventions and `TERMINOLOGY.md` for the glossary that
keeps terms consistent across chapters. `UPSTREAM-NOTES.md` collects what translating the
book turned up *about the German original* — slips, a PDF export that silently drops
figures, and housekeeping — none of it fixed here unless the entry says so.

## Build

Same toolchain as the original: [MyST](https://mystmd.org) (`mystmd`, Jupyter Book 2).

```
uv sync
uv run myst build --html     # -> _build/html
uv run myst build --pdf      # -> exports/ds-en.pdf (needs TeX, latexmk, imagemagick)
```

Publishing is automatic: every push to `main` builds the site and deploys it to GitHub
Pages (`.github/workflows/pages.yml`), served under the custom domain
`datascience.konradvoelkel.com`. Origin and base path are the two `env:` lines at the top
of that workflow, and everything that names the site — canonical URLs, sitemap, structured
data, preview cards — is derived from them at build time. The workflow refuses to deploy
if any of that comes out wrong, because every one of those failures is silent in a browser.

Two more workflows run in CI: `checks.yml` on every push (block alignment against the
German original, the leftover-German scan, notebook round-trips, and the build), and
`upstream.yml` weekly, which opens an issue when ds-skript has changed in a way that makes
part of this edition stale.

Notebooks are **not** executed by MyST; their outputs are committed. After changing code
in a notebook, re-execute and commit the result:

```
uv run --with jupyter jupyter nbconvert --execute --inplace <notebook>
```

## Licence

The notes are under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
all code additionally under the GPL3 (see `LICENSE`), following the German original.
This translation is a derivative work of ds-skript by Dr. Konrad Völkel and is
distributed under the same licence.

Third-party content keeps its own licence and is marked as such in the text:

* `Melbourne_housing_FULL.csv` — Melbourne Housing Market, Anthony Pino, **CC BY-NC-SA 4.0**
  (https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market). The file is kept in
  the repository for reproducibility; it is **not** part of the CC-BY-SA licensed work and in
  particular may not be reused commercially.
* `images/xkcd-*.png`, `images/random_number.png` — Randall Munroe, xkcd, CC BY-NC 2.5
* `images/conway_data_science_venn_diagram.png` — Drew Conway, CC BY-NC 3.0
