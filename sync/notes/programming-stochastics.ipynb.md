# programming-stochastics.ipynb

German original: `stochastik-programmieren.ipynb` (upstream `c7247a9`).
15 cells, 24 blocks. No drops, no additions, no check-ignore entries.

Note for the record: this chapter has **no** HHU Mediathek recording link under its H1, so the
drop that `intro-python.ipynb` and the `.md` chapters declare does not apply here. That is why
`sync/drops/stochastik-programmieren.ipynb.json` does not exist and has not been created.

## New terminology

Proposed for merging into `TERMINOLOGY.md`. Everything the glossary already settles
(*Ergebnisraum* → sample space, *Ereignis* → event, *Augenzahl* → number of pips,
*Gleichverteilung* → uniform distribution, *Stichprobe* → sample, *Pseudozufall* →
pseudo-randomness, *Seed* → seed, *Ziehen mit/ohne Zurücklegen* → drawing with/without
replacement, *Definitionsbereich* → domain, *Verkettung* → composition,
*Wahrscheinlichkeitsmassefunktion* → probability mass function, *Schätzung* → estimate,
*Population* → population, *Gewichte* → weights) was used as declared and is not repeated here.

| German | English | Note |
|---|---|---|
| Stochastik programmieren | Programming with stochastics | the H1; already fixed by `TERMINOLOGY.md` and by the cross-reference in `intro-stochastics.md` |
| Zufallsexperiment | random experiment | first cell; not previously in the glossary |
| Würfelwurf | throw of a die | matches `intro-stochastics.md` ("A single throw of the die"); not "roll", not "dice throw" |
| Würfelaugen | numbers of pips | the plural of the glossary's *Augenzahl* → number of pips; used in a `print` label |
| relative Häufigkeit | relative frequency | `descriptive-statistics.md` already has *Häufigkeitsverteilung* → frequency distribution, but not this one |
| Zufall importieren | Importing randomness | section heading; follows the `Zufall` → *randomness* row from `random-variables-distributions.md` |
| Größere Stichproben | Larger samples | section heading |
| Ausblick (as an `##` heading) | Looking ahead | `TRANSLATION.md` §5 fixes this for admonition titles; `expectation-variance.md` already uses it for a heading too |
| Verwendete Python-Konstrukte | Python constructs used | the link list under the H1 |
| Schnittstelle | interface | of the `random` module |
| Kürzel | shorthand | `randint` is a *Kürzel* for `randrange` |
| Urne | urn | the standard image, kept |
| paarweise verschieden | pairwise distinct | the glossary has *paarweise unabhängig* → pairwise independent |
| irgendwie geartet | some … or other | "some probability measure or other is defined on $\Omega'$" |

## Code changes

Every identifier renamed, grepped across the whole notebook afterwards. The code was run
outside the notebook (sources extracted and executed) and produces the expected output; the
notebook itself was **not** re-executed, so the stored outputs are still German — in
particular cell 4's output still reads `Wahrscheinlichkeit für gerade Augenzahl: 1/2`. That
is the single remaining German string in the file and the central re-execution pass will
clear it.

| old | new | where |
|---|---|---|
| `W` | `Omega` | cell 4 (definition), cell 4 (`P(even, Omega)`) |
| `gerade` | `even` | cell 4, three uses |
| `würfe` | `throws` | cell 8 (definition and `print`), cell 10 (`Counter(throws)`) |
| `häufigkeiten` | `frequencies` | cell 10, three uses |
| `augenzahl` | `pips` | cell 10, four uses (loop variable and three subscripts) |

Unchanged identifiers, deliberately:

| identifier | why |
|---|---|
| `P`, `A`, `Omega` (the parameters of `P`) | already the mathematical names of `intro-stochastics.md`; the German notebook had them in English/Greek from the start |
| `transform_unit_to_dice` | already English, and quoted verbatim in the prose of cell 11. See *Decisions*. |
| `very_random`, `r`, `N`, `x`, `n` | already English or neutral |
| `Fraction`, `Counter`, `floor`, `random.seed`, `random.sample`, `weights=`, `cum_weights=`, `k=` | library names and keyword arguments |

Strings and comments translated: the docstring of `P`, and the four `print` labels
(`"Even numbers of pips:"`, `"Probability of an even number of pips:"`, `"came up"`,
`"times, relative frequency"`). The `print("1", …)` … `print("5", …)` labels in cell 6 are
bare numerals and were already language-free.

Links handled per `TRANSLATION.md` §3: `de.wikipedia.org/wiki/Mersenne-Twister` →
`en.wikipedia.org/wiki/Mersenne_Twister`, and
`de.wikipedia.org/wiki/Komposition_(Mathematik)` → `en.wikipedia.org/wiki/Function_composition`
(link text *Verknüpfung* → *composition*, per the glossary). Both English counterparts exist, so
neither link needed a "(in German)" marker. The eight `docs.python.org` links keep their
targets; only their German labels were translated.

## Decisions and doubts

**1. `W` → `Omega`, not a short Latin letter.** This was the hardest call. In the German,
`W` (presumably *Würfel*, or *Wahrscheinlichkeitsraum*) holds `{1,2,3,4,5,6}` and is passed
as the `Omega` argument of `P` — so the code already disagreed with itself, and it disagrees
with the prose of cell 11, which writes the very same set as $\Omega := \{1,2,3,4,5,6\}$.
Naming the global `Omega` makes code, parameter and prose say one thing, which is the point of
this chapter. The cost is that the module-level `Omega` and the parameter `Omega` of `P` now
share a name; they do not collide (the parameter shadows), and the shadowing is arguably the
pedagogical point — the argument you pass *is* the $\Omega$ of the formalism. A human should
confirm they are happy with that over, say, `S` or `die_faces`, both of which would re-open
the gap between code and prose.

**2. `transform_unit_to_dice` left alone.** "Dice" is the plural; the function returns one
die's worth of pips, so `transform_unit_to_die` would be better English. It was not renamed:
the name is already English, so translating it is not this pass's job, the prose quotes it
verbatim in two places, and the German original has the same infelicity. Flagging it as a
candidate for a later editorial pass on the *German* side, where it should be fixed first so
the two editions stay in step.

**3. *Methode* → "function", against the `intro-python.ipynb` precedent.** The German calls
`random.random`, `random.sample` and `random.choices` *Methoden*. They are module-level
functions, not methods, and in English that distinction is not loose usage but an error — a
reader who goes looking for the method on an object will not find it. So all three became
"function", and the link label *Methoden/def* became "Functions/def" (its target is the
tutorial's *Defining Functions*). `intro-python.ipynb` keeps "method" where the German says
*Methode*, but it does so while describing a `def` inside a class, where the word is correct.
Worth a consistency check if a later pass wants one word throughout.

**4. Minor, for completeness.** The German gloss "Stichproben (en. Samples)" collapses to the
single word "samples". The `-` in cells 11 and 13 became the book's spaced en dash. German
quotation marks around the xkcd title became plain ones. The single quotes around
'Augenzahl' / 'number of pips' in the last cell are the German's own single quotes and were
kept as single quotes rather than promoted to double — they mark a name being introduced, not
a quotation.

## For a human to check

* Decision 1 above (`W` → `Omega`) — the only rename with a real design choice in it.
* The notebook needs the central re-execution pass; cell 4's stored output is still German.
* Cell 14 says "In the next chapter …", and in this edition's TOC the next chapter really is
  `random-variables-distributions.md`, which does introduce the pmf. The German does not link
  it and neither does the translation, so nothing to fix — just confirming the claim survives
  the reordering, if any.
