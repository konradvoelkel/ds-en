# How this edition is translated

Rules, not suggestions. Everyone translating a chapter – human or agent – follows these,
because the sync machinery and the consistency of the book both depend on them.

## 1. Block alignment

English and German are kept in **strict block alignment**. A block is what
`tools/segment.py` says it is: a paragraph, a heading, a fenced code block, a display-math
block, a `:::` delimiter line, a notebook cell.

* Never merge two source blocks into one, never split one into two, never reorder them.
* Inside a block, rewrite as freely as good English requires. Sentence order, sentence
  count and phrasing are the translator's business.
* A block that is **deliberately absent** from the English edition (see §2) is declared in
  `sync/drops/<german-file>.json`, with a reason. Dropping a block is a decision, not a side effect: it has
  to be written down, or the alignment check fails.
* A block that exists **only in English** – a translator's note, nothing more – is declared
  the same way in `sync/additions/<english-file>.json`. Keep these rare: this is a translation, not a
  rewrite.
* Notebook cells are never added, removed, merged or retyped. `tools/nbtext.py` refuses
  the import if they are.

This is what lets the upstream tracker say "paragraph 14 of `covariance.md` is stale"
instead of "something in this chapter changed".

## 2. What the English edition drops

This edition is a standalone book, not courseware for the Düsseldorf lecture hall.

* **Lecture recording links.** Every chapter of the German original links its HHU
  Mediathek session under the H1. The recordings are in German and are of no use to a
  reader of this edition; those blocks are dropped.
* **The slides page.** `folien.md` links PDF decks that are not mirrored here. Dropped
  from the table of contents; the landing page points at the German edition instead.
* **The exercise and exam apparatus.** Exercise sheets, midterm and exam are not part of
  this edition. The landing page's AI-tool policy, which is about submissions and the
  exam, is dropped; and the German marker "nicht klausurrelevant" ("not examinable")
  becomes a plain "not part of the course proper", which is what it means to a reader who
  will never sit the exam. Passing mentions of the course's exercises stay – they are part
  of the honest account of what these notes are – but nothing points the reader at a sheet
  they cannot have.
* **The host institution's own apparatus.** Decided 2026-10-14, and this reverses the
  earlier rule that course organisation stays. The English edition is not aimed at the
  Düsseldorf BSc: named courses of that curriculum ("Data Science 2"), its module
  handbook, its master's programme and its "three semesters" of prerequisites are
  generalised to what they actually mean — a course on distributed systems, a list of
  formal competencies, a master's in AI or data science, the mathematics of an
  undergraduate degree. The German-language bridge course stays but is offered as what it
  is, a resource for readers of German.
* Nothing else. Where the book grew up still belongs to it, and the `:::{note}` at the
  foot of the landing page says so plainly: these are lecture notes from a BSc course at
  Heinrich Heine University Düsseldorf. The point is that a reader elsewhere is never sent
  to a page, a programme or a timetable they have no access to.

## 3. What is not translated

* **Identifiers that are not prose**: `{cite}` keys, `:name:` labels on figures, explicit
  MyST targets like `(ein-bunter-mix)=`, `:::{note}` directive names. They are invisible
  to the reader and churning them risks breaking references for nothing.
* **Column names that come from the data**: `Sex`, `Age`, `Pclass`, `SibSp` and friends are
  what the file contains. Column names the text *invents* (German names assigned in the
  notebook) are translated.
* **Quoted German**: legal terms, book and lecture titles, anything shown as an example of
  German usage. Quote the German and gloss it in English where the reader needs it.
* **Proper names**, including HHU, the module name and the author.

A course title is translated when the book only mentions it (*Introduction to Deep
Learning*), and kept in German when the book links to it (*Einführung in Python*), because
there the reader has to recognise the page they land on. Sixteen mentions of the deep
learning course had drifted into four spellings before this was written down.

German-language *links*, on the other hand, are handled: a link to German Wikipedia is
replaced by its English counterpart where one exists, and a link that stays German (a German
course, a German video) is marked "(in German)" so the reader is not sent somewhere useless.

## 4. What is translated that is easy to forget

* Code comments, `print` strings, plot titles, axis labels, legend entries, tick labels.
* German variable, function and DataFrame column names invented by the notebook.
* Figure captions and admonition titles.
* Text inside images. Figures with German text baked in are redrawn; see
  `images/README.md` for which ones and how they are generated.

After touching code in a notebook, re-execute it and commit the outputs:

```
uv run --with jupyter jupyter nbconvert --execute --inplace <notebook>
```

## 5. Admonition titles

The German book uses `:::{admonition} <title>` for its mathematical furniture. Fixed
translations, no improvisation:

| German | English | | German | English |
|---|---|---|---|---|
| Definition | Definition | | Bemerkung | Remark |
| Satz | Theorem | | Beispiel | Example |
| Proposition | Proposition | | Übung / Aufgabe | Exercise |
| Lemma | Lemma | | Lösung | Solution |
| Beweis | Proof | | Lösungshinweis | Hint |
| Korollar | Corollary | | Merke | Remember |
| Grundsatz | Principle | | Ausblick | Looking ahead |
| Faustregel | Rule of thumb | | Take-Home-Message | Take-home message |
| Achtung | Caution | | Hinweis | Note |

`:::{note}` keeps its meaning from the original: "optional, not part of the course proper".

Where the German splits a theorem's name between the admonition title and a bolded lead-in
in the body – `:::{admonition} Satz` followed by `**von Bayes:**` – **keep it split the same
way**: "Theorem" in the title, "**Bayes' theorem.**" in the body. The mild redundancy is the
German's own. Do not move the name up into the title, however much tidier that looks: a name
that migrates across a block boundary is exactly what block alignment exists to prevent, and
the staleness report would then point at the wrong block.

## 6. Typography and conventions

* **Decimal separator**: German `0,25` becomes `0.25`, in prose, in maths and in figure
  captions. In maths the German spelling is `0{,}25`; the LaTeX braces go with the comma.
* **Thousands separator**: in prose, German `1.000` becomes `1,000`. **In maths it does not**:
  the German writes `$178\,000$` with a thin space, which is the scientific convention in
  English too, and `178{,}000` would reintroduce exactly the token the decimal rule exists to
  remove. Thin space inside maths, comma in prose.
* **Quotation marks**: `„…“`, `,,…''` and `»…«` all become plain `"…"`.
* **Dashes**: the German parenthetical dash (`—`, ` - `) becomes a **spaced en dash** ` – `
  throughout the book. One rule, not a per-chapter choice, so that 31 files look like one book.
* **Genderstern**: `Teilnehmer\*innen` has no English equivalent and needs none –
  "participants". Never "participants (m/f)".
* **Address**: the German "Sie" becomes "you"; the German "wir" stays "we". The book's
  voice is a lecturer thinking alongside the reader, and that survives translation.
* **Dates**: `25.09.2026` → `25 September 2026`.
* **Money**: symbol first and the scale written out. German `35,3 Mio. €` → `€35.3 million`,
  `1,2 Mrd. €` → `€1.2 billion` (short scale), `18.600 €` → `€18,600`.
* **Per cent**: German `78 %` becomes `78%`, no space, in prose and in tables. Inside maths
  the thin space stays as the source has it (`$-0.1\,\%$`), because that is the convention
  in English typesetting too.
* **Spelling**: British or American, but one of them. This edition uses **British**
  spelling throughout, with `-ise` rather than `-ize`: `visualisation`, `normalisation`,
  `optimisation`, `generalise`, `behaviour`, `modelling`. American spellings that are part
  of a name or of code stay as they are (`scikit-learn`'s `normalize`, `color=`).

## 7. Terminology

`TERMINOLOGY.md` is binding. If a term is not in it and you had to think about it for more
than a moment, add it there in the same commit – that is how the glossary grows into
something the later chapters can rely on.

Specifically: "Stochastik" is **stochastics**, clunky or not. It names the field that holds
probability theory and statistics together, and the book needs that name.

## 8. Review passes

1. **Translation** (Opus, one agent per chapter) – against `TERMINOLOGY.md`, obeying §1.
2. **Consistency** – terminology actually used as declared; cross-references intact.
3. **Style** (Fable) – English that reads as English. Still obeying §1: no merging or
   splitting of blocks.
4. **Mechanical checks** – `tools/sync.py align`, the build, the link check and a
   leftover-German scan.
5. **Human review.**

## 9. What the staleness check cannot see

`tools/sync.py` compares *blocks of mirrored content files* — the Markdown chapters and
the notebooks named in `sync/filemap.json`. Everything else about the original is
invisible to it, by construction, not by oversight:

* the build and deploy configuration (upstream `.gitlab-ci.yml`, here
  `.github/workflows/`): different platforms, so there is nothing to map and nothing to
  hash;
* `myst.yml` — the table of contents, the PDF `articles` list, the site options;
* `tools/` on either side;
* files mapped to `null` in `filemap.json` (`folien.md`, `orga.md`);
* the original's own repository documentation (`PROJECT_NOTES.md`, `BRANDING.md`,
  `TODO.md`), which is where it records *why* it changed something;
* **notebook outputs.** `segment.py` segments `source` and never `outputs`, so anything
  living in an output is invisible — including, as it turned out, the text alternative of
  every figure the book draws. MyST takes an output image's `alt` from that output's
  `text/plain`. On 2026-10-16 the original wrote descriptions into all 156 of its figures,
  touching eighteen files, and the staleness report showed five regions, all of them
  headings. This is the same blind spot as the entries above, but closer in: it is *inside*
  a mirrored file. And the descriptions themselves are kept in `alt-texts.yml`, which is
  prose that no sweep over the cells sees: ds-skript's spelling sweep of 2026-10-30
  (`17547e6`) was clean over every cell and still left four `Scikit-learn` in its built
  HTML, all four from `alt-texte.yml`. A sweep over the book's wording includes that file.

**This has already cost us once.** On 2026-10-14 the original fixed its sitemap,
`robots.txt`, canonical URLs and `og:image` (ds-skript `d929f14`, `6e75f56`, `c3e74d3`).
All four fixes lived in `.gitlab-ci.yml`. The weekly upstream check reported nothing,
correctly, and this edition went on serving a sitemap whose 30 URLs all pointed at
`http://localhost:3000` — the whole site effectively un-crawlable — until someone looked
by hand.

**The rule:** when `upstream.yml` opens a staleness issue — it is triggered by a push in
ds-skript since 2026-10-15, not by a schedule — or whenever the pin in
`sync/upstream.json` is moved, also read the original's `git log` for commits that touch
CI, `myst.yml` or `tools/`, and decide each one deliberately. Most will not apply — the
deploy targets genuinely differ. The ones that do apply are usually the ones no reader
would ever report, because they are invisible in the rendered page.

Infrastructure findings go in `SEO-NOTES.md` when they concern how the site is published,
and in `UPSTREAM-NOTES.md` when they are a problem of the original.
