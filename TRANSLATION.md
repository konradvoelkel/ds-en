# How this edition is translated

Rules, not suggestions. Everyone translating a chapter — human or agent — follows these,
because the sync machinery and the consistency of the book both depend on them.

## 1. Block alignment

English and German are kept in **strict block alignment**. A block is what
`tools/segment.py` says it is: a paragraph, a heading, a fenced code block, a display-math
block, a `:::` delimiter line, a notebook cell.

* Never merge two source blocks into one, never split one into two, never reorder them.
* Inside a block, rewrite as freely as good English requires. Sentence order, sentence
  count and phrasing are the translator's business.
* A block that is **deliberately absent** from the English edition (see §2) is recorded as
  `"dropped"` in `sync/segments/<german-file>.json`. Dropping a block is a decision, not a
  side effect: it has to be written down there, or the alignment check fails.
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
* Nothing else. Course organisation, module competencies and exam references stay —
  they are part of what these notes are, and a reader is entitled to know the context
  they were written in.

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

`:::{note}` keeps its meaning from the original: "optional, not examinable".

## 6. Typography and conventions

* **Decimal separator**: German `0,25` becomes `0.25`. This applies in prose, in maths and
  in figure captions. Watch for thousands separators going the other way: `1.000` → `1,000`.
* **Quotation marks**: `„…“`, `,,…''` and `»…«` all become plain `"…"`.
* **Dashes**: German `--` / `—` as a parenthetical dash becomes an em dash without spaces
  or an en dash with spaces; pick one per chapter and keep it.
* **Genderstern**: `Teilnehmer\*innen` has no English equivalent and needs none —
  "participants". Never "participants (m/f)".
* **Address**: the German "Sie" becomes "you"; the German "wir" stays "we". The book's
  voice is a lecturer thinking alongside the reader, and that survives translation.
* **Dates**: `25.09.2026` → `25 September 2026`.
* **Spelling**: British or American, but one of them. This edition uses **British**
  spelling (`behaviour`, `modelling`, `centre`) with `-ize` endings (`normalize`), i.e.
  Oxford spelling, because the maths and ML literature the reader will go on to read is
  mixed and `-ize` is the safer habit.

## 7. Terminology

`TERMINOLOGY.md` is binding. If a term is not in it and you had to think about it for more
than a moment, add it there in the same commit — that is how the glossary grows into
something the later chapters can rely on.

Specifically: the German "Stochastik" covers probability theory *and* statistics and has no
English equivalent. Translate what is meant, never "stochastics".

## 8. Review passes

1. **Translation** (Opus, one agent per chapter) — against `TERMINOLOGY.md`, obeying §1.
2. **Consistency** — terminology actually used as declared; cross-references intact.
3. **Style** (Fable) — English that reads as English. Still obeying §1: no merging or
   splitting of blocks.
4. **Mechanical checks** — `tools/check_align.py`, the build, the link check and a
   leftover-German scan.
5. **Human review.**
