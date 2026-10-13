# Translator's notes: `numpy.ipynb`

German original `numpy.ipynb` (same filename, per `sync/filemap.json`), **37 cells, 58
blocks**. **No drops**: this chapter is one of the few that carries no HHU Mediathek link
under its H1, and nothing else in it is courseware-specific, so `sync/drops/numpy.ipynb.json`
was not created. No `sync/additions` entry either – nothing was added. No
`sync/check-ignore` entry was needed.

`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass.
The notebook was **not** re-executed, so the stored outputs are still the German run
(cells 19, 21, 26, 31, 33 print German strings in their outputs); that is expected and
waits for the central re-execution pass.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | note |
|---|---|---|
| Array-orientierte Programmierung | array-oriented programming | the chapter's own framing; links to the English Wikipedia article, which was already the target |
| Vektorisierung, vektorisieren | vectorisation, to vectorise | house `-ise` spelling; the German glosses *Array-orientierte Programmierung* with it |
| verzweigungsfrei schreiben | to write branch-free code | the chapter's bolded working rule; `Verzweigung` → *branch* |
| Fallunterscheidung | case distinction |  |
| Maske, maskieren | mask | `## Masken und Fancy Indexing` → `## Masks and fancy indexing`; cross-referenced from block c1.4 |
| Fancy Indexing | fancy indexing | the Numpy term of art, lower case in English |
| Matrizenkalkül | matrix algebra | see *Decisions* – not "matrix calculus" |
| Matrizenmultiplikation / Matrixmultiplikation | matrix multiplication / matrix product | the German uses both spellings; `np.matmul`'s result is the *matrix product* |
| elementweise | element by element, element-wise | adverbially "element by element", attributively "element-wise" |
| Infix-Operator | infix operator | the `@` operator |
| Achse | axis | plural *axes*; `axis=` stays as the keyword |
| Zeilenvektor / Spaltenvektor | row vector / column vector |  |
| Einheitsmatrix | identity matrix | code comment in cells 13 and 15 |
| Speicherbereich | region of memory | `np.may_share_memory` |
| Sichtweise (auf den Speicher) | view | the Numpy word; the German says *View* in the same cell |
| Datentyp | data type | `dtype` stays `dtype` |
| Gerätezuordnung | device assignment | the PyTorch tensor's CPU/GPU placement |
| automatische Ableitung | automatic differentiation | not "automatic derivative" |
| Hauptspeicher / Grafikkarte | main memory / graphics card |  |
| gezinkter Würfel | loaded die | code comment, cell 33; `Würfe` → *rolls* |
| normieren (einen Vektor) | to normalise | here: dividing by the sum so that $p \in \Delta_6$ |
| relative Häufigkeiten | relative frequencies |  |
| Spickzettel | cheat sheet |  |
| Nachschlagewerk | reference work |  |
| Einsteigerkapitel | beginners' chapter | of the Numpy documentation |
| Was muss man kennen? | What do you need to know? | section heading, block c35.0 |
| Stand September 2026 | as of September 2026 | the date the function list was harvested |
| Skript (das Vorlesungsskript) | these notes | matches `intro-python.ipynb`, which already uses this |

Already settled elsewhere and reused unchanged: *Einführung in Deep Learning* →
**Introduction to Deep Learning** (the spelling used in `intro-python.ipynb`,
`intro-stochastics.md` and five other translated files), *Wahrscheinlichkeitsvektoren* →
**Probability vectors** (the section name `random-variables-distributions.md` and
`statistical-models.md` already point at), *Wichtigste diskrete Verteilungen* → **The most
important discrete distributions** (cited in a code comment in cell 6), *diskrete
Gleichverteilung* → **discrete uniform distribution**.

## Code changes

German identifiers renamed. Everything else in the code cells was already English
(`sample`, `myRange`, `ordinary_list`, `sort_array`, `real_copy`, `candidates`, `matrix`,
`npmatrix`, `E`, `A`, `v`, `p`, `rng`, `a`).

| old | new | where |
|---|---|---|
| `zahlen` | `numbers` | cell 19 |
| `maske` | `mask` | cell 31 |
| `quarkix` | `shamtrix` | cell 13 – see *Decisions* |
| `npquarkix` | `npshamtrix` | cell 15 |
| `wuerfe` | `rolls` | cell 33 |
| `bedingung` | `condition` | block c30.1, inside the inline code `np.where(condition, a, b)` |

Translated alongside them, cell by cell: every code comment (cells 6, 13, 15, 21, 31, 33),
and the German `print` strings in cells 19 (`"Zeilenvektor Zeile 0:"` → `"row vector, row
0:"`, `"Spaltenvektor Spalte 0:"` → `"column vector, column 0:"`, `"Spalten 1-2:"` →
`"columns 1-2:"`, `"Alle Zeilen, Schrittweite 2"` → `"all rows, step 2"`) and 26
(`"= A*v (aber nicht die Matrixmultiplikation)"` → `"= A*v (but not the matrix product)"`).
The column alignment of the aligned `print` blocks in cells 6 and 31 is preserved. The
HTML comment in cell 2 (an author's note pointing at a German Numpy tutorial) was
translated and the link marked "(in German)" per TRANSLATION.md §3. No plot titles, axis
labels or legends occur in this chapter – it produces no figures.

## Decisions and doubts

**1. `quarkix` → `shamtrix` (cells 13 and 15).** The German's joke name is a pun on
`matrix` with *Quark* ("nonsense, rubbish"): the variable is a slicing "copy" that turns out
not to be a copy at all. I translated the pun rather than the word, with *sham* for *Quark*,
because the cell's punchline depends on the reader noticing that the name is derisive, and
because the contrasting `real_copy` three lines later is already in English. **This is the
one change in the chapter a human should sign off on.** If `shamtrix` reads as too cute, the
plain alternative is `fake_copy` / `npfake_copy`, which pairs with `real_copy` and loses
only the pun; nothing else in the notebook refers to these names, so the substitution is
local to two cells.

**2. The chapter's opening joke is gone (block c1.0).** The German calls the Numpy
fundamentals "eine längere und bessere (und englischere) Fassung" – longer, better, *and
more English*, a dig at its own Germanness. In an English edition the parenthesis is simply
false, so I dropped it inside the block: "A longer and better version of it is the [Numpy
fundamentals] …". Nothing was dropped at block level and the sentence count is unchanged.

**3. *Matrizenkalkül* → "matrix algebra" (blocks c27.0 and c29.0).** "Matrix calculus" is
the literal cognate but in English names the differentiation of matrix-valued functions,
which is not what the chapter means: it means computing with matrix products rather than
element by element. "Matrix algebra" says that. The opposition the two blocks set up is
therefore "matrix algebra" versus "element by element", where the German has
*Matrizenkalkül* versus *elementweise*. Worth putting in the glossary before
`linear-regression.ipynb` and `dimensionality-reduction.ipynb` need the same word.

**4. Heading case.** `## Masken und Fancy Indexing` → `## Masks and fancy indexing` and
`## Was muss man kennen?` → `## What do you need to know?`, i.e. sentence case, following
`intro-python.ipynb` ("Where Python sits", "Four things to remember", "Further reading").
`## Arrays`, `## Broadcasting`, `## ufuncs` are unchanged. **The *Masks and fancy indexing*
heading is cross-referenced from block c1.4 in the same notebook**, and the two now agree;
if a style pass retitles the section, it has to change both. Nothing outside this notebook
links to it (I grepped).

**5. The *deprecated (veraltet)* gloss collapses (block c27.0).** The German writes
"als `deprecated` (veraltet) markiert" – the English loanword plus its German translation.
In English the gloss is redundant and I wrote "marked as `deprecated`". Same pattern as the
*Störvariable/Confounder* row in `descriptive-statistics.md`.

**6. *Man* and *Sie*.** The chapter is written almost entirely in impersonal *man*
("man kann", "man nutzt", "man muss"). Per TRANSLATION.md §6 the single *Sie* (block c1.0,
"die Sie am besten im Anschluss überfliegen sollten") became "you", and I used "you" for
most of the *man* clauses too, keeping "one" only where a sentence would otherwise have had
three "you"s in a row (blocks c27.0, c35.1). If the style pass wants one pronoun
throughout, "you" is the one to standardise on.

**7. `np.where(bedingung, a, b)` in prose (block c30.1).** The German puts a German
parameter name inside inline code in running text. Numpy's actual signature is
`np.where(condition, x, y)`; I translated the name to `condition` but left the second and
third arguments as the German's `a, b`, because the code cell directly below uses `a` as
its array name and the two should read together. A reader comparing with the Numpy
documentation will see `x, y` there instead.

**8. Outputs are still German.** Cells 19, 21, 26, 31 and 33 have stored outputs
containing the old German `print` strings, and cell 3's output pins an older Numpy
version. This is the expected state before the central re-execution pass; I did not
re-execute, as instructed. Worth noting that cell 33 is seeded (`default_rng(1)`), so its
numbers will not move, and cell 10's `timeit` numbers will.
