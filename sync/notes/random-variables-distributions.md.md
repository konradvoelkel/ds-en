# Notes from the translation of `random-variables-distributions.md`

German original: `zufallsvariablen-verteilungen.md`. 144 German blocks, 1 declared drop
(the HHU lecture-recording link), 143 blocks in the English file. `tools/sync.py align`
and `tools/check_english.py` both pass; no `check-ignore` entries were needed.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`. Please merge.

| German | English | note |
|---|---|---|
| Zufall | randomness | the chapter's section heading is *Wo kommt der Zufall her?* → *Where does the randomness come from?*; "chance" reads too colloquial once the section argues that randomness is a modelling decision |
| Pseudozufall | pseudo-randomness | hyphenated; `Seed` stays *seed* |
| Startwert (eines Generators) | starting value | with *seed* given as the technical name right after |
| Weltausschnitt | section of the world | follows the existing `Ausschnitt` → *section* row; `Weltzustand` → *world state* |
| Weltzustand | world state | the elements of $\Omega$ in the die example |
| Bereinigung (von Rohdaten) | cleaning | the noun; the chapter title stays *Data cleaning* per the glossary |
| induziertes Wahrscheinlichkeitsmaß | induced probability measure | section heading; `induzierte pmf` → *induced pmf* |
| Verteilung der Daten | distribution of the data | the book's own term, kept literal; *empirische Verteilung* → *empirical distribution* |
| Modellverteilung | model distribution | |
| synthetische Daten | synthetic data | plural verb: "synthetic data are" |
| Zähldichte | discrete density | see *Decisions* below – I did not keep the German word |
| Wahrscheinlichkeitsvektor | probability vector | section heading; `Bitmaske` → *bitmask* |
| Elementarereignis | elementary event | already in the glossary via `intro-stochastics.md`, repeated here for the proof in example (b) |
| kategoriale Verteilung | categorical distribution | |
| Bernoulli-Verteilung zum Parameter $\pi$ | Bernoulli distribution with parameter $\pi$ | not "to the parameter" |
| Erfolg / Misserfolg | success / failure | in the coin-toss estimate |
| Erfolgswahrscheinlichkeit | success probability | |
| Population | population | the German uses the Latinate word too |
| Prior | prior | stays, lower case in English running prose |
| Augenzahl | number of pips | matches `intro-stochastics.md` |
| Parität | parity | |
| Verkettung (von Abbildungen) | composition | "composing maps yields new random variables" for *Verketten liefert neue Zufallsvariablen* |
| Urbild | preimage | as in `intro-stochastics.md` |
| Rechenvorschrift | rule for calculating | |
| Zeichenvorrat | character set | |
| Strecke (geometrisch) | line segment | $\Delta_2$; "segment" alone on repeat mentions |
| Eckpunkt / Ecke (eines Simplex) | vertex | plural *vertices* |
| gefülltes Dreieck / Tetraeder | filled triangle / tetrahedron | |
| Tschebyscheff-Ungleichung | Chebyshev's inequality | the usual English transliteration; `expectation-variance.md` will need the same |
| Güte des Modells | quality of the model | the glossary's `Güte` row already covers it; not "goodness of fit" here |
| Maximum-Likelihood-Prinzip | maximum likelihood principle | no hyphens in English |
| Merkmale / Features | features | the German glosses *Merkmale* with the English loanword *Features*; in English the gloss collapses to one word |

Chapter link texts I used, for consistency when those chapters are translated:

| German link text | English used here |
|---|---|
| Stochastik programmieren | Programming with stochastics (as in `intro-stochastics.md`) |
| Formalismus der Stochastik | The formalism of stochastics |
| Erwartungswert und Varianz | Expected value and variance |
| Wichtigste diskrete Verteilungen | The most important discrete distributions |
| Statistische Modelle und Schätzer | Statistical models and estimators |
| Statistische Tests | Statistical tests |
| Relative Entropie | Relative entropy |
| Daten putzen | Data cleaning (glossary) |
| Numpy, Abschnitt *Wahrscheinlichkeitsvektoren* | Numpy, section *Probability vectors* |

## Figures

The chapter uses three figures, all of them with German text baked into the PNG. I opened
all three; `images/README.md` has them listed under "Used in: descriptive-statistics",
which is wrong – a grep over the whole repository finds them only in this chapter. The
German text, as actually rendered:

| File | German text in the image | English it should carry |
|---|---|---|
| `dsprozess-simplified-1.png` | globe → `Ausschnitt` → `Rohdaten` → `Daten` | Section → Raw data → Data |
| `dsprozess-simplified-2.png` | globe → `Daten` → `Modell` → `Synthetische Daten` | Data → Model → Synthetic data |
| `dsprozess-simplified-3.png` | globe → `Daten` → `Transformierte Daten` → `Zielgröße` | Data → Transformed data → Target variable |

So the README's row for `-2.png` ("as above, plus Modell") is slightly off as well: that
figure does *not* contain `Ausschnitt`/`Rohdaten`, it contains `Daten`, `Modell` and
`Synthetische Daten`. All three are the same four-box diagram (a globe and three labelled
boxes joined by arrows) and would be trivial to regenerate from a small matplotlib or
graphviz script; the box widths differ slightly between them, which is the only reason
`Transformierte Daten` and `Synthetische Daten` wrap onto two lines.

The three English captions I wrote are "Data collection: from the world via a section and
raw data to the data.", "Modelling: from the data to the model and back to synthetic
data." and "Analysis: from the data via transformed data to the target variable."; the
`:name:` labels stay German (`ds-prozess-erhebung`, `ds-prozess-modell`,
`ds-prozess-zielgroesse`) per TRANSLATION §3, and `{numref}` in the last block of the
chapter references `ds-prozess-modell`.

## Decisions and doubts

**1. The jumper-colour letters $\{r,g,b,s\}$ (blocks 43, 44, 64, 65, 84).** The German
example maps each child to *the initial letter of its jumper colour*: rot, gelb, blau,
schwarz → $r,g,b,s$. Read in English those letters are actively misleading ($g$ looks like
green, $s$ like nothing, and $b$ with $10$ children versus $g$ with $5$ invites exactly the
wrong reading). I changed the symbols to $\{r,y,b,k\}$ – red, yellow, blue, black, with $k$
for black as in CMYK – and rewrote the sentence so that it no longer claims these are
initial letters: "the map that sends each child to the letter standing for the colour of
its jumper ($r$ red, $y$ yellow, $b$ blue, $k$ black)". This touches maths blocks, which
TRANSLATION §3 normally leaves alone, but the letters are German words in disguise and
block 44 ($P_X(\{b,r\}) = 20/30$) is unaffected either way. **A human should confirm the
$k$.** The alternative is to leave $\{r,g,b,s\}$ standing and gloss it as German, which I
think is worse for a reader who never sees the German. Nothing else in the repository uses
these letters.

**2. "Zähldichte" (block 66).** The German offers *Zähldichte* as a second name for the
pmf. There is no settled English equivalent; the literature that bothers at all says
*discrete density* (or *discrete density function*), so that is what I wrote. The other
option was to keep the German term in italics with a gloss, as TRANSLATION §3 allows for
quoted German – but this is not an example of German usage the reader needs, it is just a
synonym, and a German synonym is of no use in an English book. Flagging it because it is
the one place where I dropped a German word rather than rendering it.

**3. "Auf Englisch fragt man *how likely is that?*" (block 142).** The German explains the
word *Likelihood* by pointing at the English question behind it. In English that
explanation has nothing to explain, so the sentence becomes simply "One asks *how likely is
that?*, and the number that answers it is called the **likelihood**". The rhetorical move
survives, the meta-comment about English does not. Same shape as the *Merkmale/Features*
gloss in the final block, which I collapsed to plain "features".

Smaller things, for the record:

* `\text{}` contents inside maths were translated: `gerade`/`ungerade` → `even`/`odd`,
  `nein` → `no`, `sonst` → `otherwise`, `für ein` → `for some`, `für alle` → `for all`,
  `und` → `and`.
* Identifiers in code were translated where the notebook invents them:
  `np.bincount(daten) / len(daten)` → `np.bincount(data) / len(data)`,
  `random.choices(werte, …)` → `random.choices(values, …)`,
  `rng.choice(werte, …)` → `rng.choice(values, …)`. The `rng.choice` keyword `p=` and
  `weights=` are library API and stay.
* "Sie" in the Exercise became "you" (imperative "Draw $1000$ synthetic colour values …").
* All German em dashes became spaced en dashes; German quotes („Kopf", „nein", „die
  Zufallsvariable Parität des Wurfs") became plain double quotes.
* "Pulli" is translated as *jumper*, not *sweater*, to stay inside the book's British
  spelling.
* Block 2 keeps the German's single quotes around 'interface' and block 129 the single
  quotes around the quoted question; both are the original's own typography, not German
  quotation marks.
* Block 33 ("Das ist tatsächlich immer ein Wahrscheinlichkeitsmaß.") I rendered as "This
  really is a probability measure, always." – the German's word order puts the emphasis on
  *immer*, and the trailing "always" is the only way I found to keep it in a sentence this
  short without padding.
