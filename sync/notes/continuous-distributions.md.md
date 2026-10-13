# Translator's notes: `continuous-distributions.md`

German original `stetige-verteilungen.md`, 93 blocks, 1 declared drop (the HHU lecture
recording link), 92 translated blocks. `tools/sync.py align` and `tools/check_english.py`
both pass; no `check-ignore` entries were needed.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | note |
|---|---|---|
| Träger (einer Verteilung / Zufallsvariable) | support | `\operatorname{supp}(X)`; the chapter's opening definition |
| abgeschlossen (Menge) | closed | topological sense, defined in the chapter |
| Abschluss (einer Menge) | closure | |
| Nullmenge | null set | the chapter's Remark defines it; `covariance.md` also uses the word and will need the same choice |
| Häufungspunkt | accumulation point | "limit point" is equally standard; picked one and used it once |
| Dichtefunktion (chapter heading *Dichtefunktionen*) | density function | heading rendered "Density functions"; running prose stays with "density" per the glossary |
| Wahrscheinlichkeitsdichtefunktion | probability density function | pdf; glossary has only "Dichte → density" |
| Lebesgue-Maß | Lebesgue measure | |
| Riemann-integrierbar | Riemann integrable | |
| Transformationsformel (the `\mathbb{E}(g(X))` theorem) | transformation formula | admonition title "Theorem (transformation formula)"; see Decisions |
| Transformationssatz für Integrale | change-of-variables theorem for integrals | the thing the proof would appeal to |
| Stammfunktion | antiderivative | |
| Hauptsatz der Differential- und Integralrechnung | fundamental theorem of calculus | |
| Mischverteilung | mixture distribution | |
| kontaminierte Normalverteilung | contaminated normal distribution | cross-reference to `important-continuous-distributions.ipynb` |
| Dirac-Verteilung | Dirac distribution | `intro-stochastics.md` already has "Dirac measure" for *Dirac-Maß*; both occur |
| einpunktige Menge | one-point set | |
| Distributionen (Funktionalanalysis) | distributions / generalised functions | see Decisions – collides with *Verteilung* in English |
| überabzählbar / abzählbar | uncountable / countable | |
| Teilintervall | subinterval | |
| Knobelaufgabe | puzzle | the chapter's aside in the `\mathbb{Q} \cap [0,1]` example |
| $k$-tes Moment | $k$-th moment | glossary has "Momente → moments" only |

## Figures

None. `continuous-distributions.md` references no figure and no image; it has no
`{figure}` directive and no `![...]`. Nothing for `images/README.md` from this chapter.

## Decisions and doubts

**1. *Distributionen* vs *Verteilungen* (block 68).** The German sentence plays on two
words that English collapses into one: "zur Theorie der Distributionen aus der
Funktionalanalysis greifen … Es gibt auch Verteilungen, da genügt auch keine Distribution."
Translated word for word this becomes unreadable ("there are distributions for which no
distribution is enough"). I glossed it once – "the theory of distributions from functional
analysis – generalised functions, which English unhelpfully calls by the same word as
probability distributions; physicists know them" – and then used "generalised function" for
the second half. It is a sentence of added gloss inside one block, no block added. Worth a
human eye: if the book would rather not comment on its own English, the fix is to use
"generalised functions" throughout and drop the aside.

**2. The admonition title "Satz (Transformationsformel)" (block 40).** English probability
texts usually call $\mathbb{E}(g(X)) = \int g f$ the *law of the unconscious statistician*,
or just fold it into the definition of expectation; "transformation formula" is a German
habit. I kept the German's own name ("Theorem (transformation formula)") because the next
block refers back to the *Transformationssatz für Integrale*, and the pair of names is the
point. If the glossary would rather have the English idiom, change both blocks together.

**3. The threefold name for the cdf (block 80).** The German gives three names –
*kumulative Wahrscheinlichkeitsverteilungsfunktion*, *Verteilungsfunktion*, *cdf* – where
the second and third are the same words in English. I kept three ("cumulative probability
distribution function, or distribution function, or cdf for short") so the reader meets the
long form once and the acronym is motivated, rather than collapsing them and losing the
"(cumulative distribution function)" gloss the German block carries.

**Cross-chapter link texts I had to guess.** Both chapters are still untranslated, so the
link text is my best guess at their eventual English titles; please align when they land.

* `[Expected value and variance](expectation-variance.md)` for *Erwartungswert und Varianz*
  (blocks 39) – follows the glossary's "Erwartungswert → expected value".
* `[The most important continuous distributions](important-continuous-distributions.ipynb)`
  for *Wichtigste stetige Verteilungen* (blocks 75, 92).
* `[Deriving the mathematical formalism of stochastics](intro-stochastics.md)` (block 60) is
  taken verbatim from the already-translated chapter's H1, so that one is solid.

**Typography.** Two spaced-hyphen/em-dash parentheticals in the German (blocks 22 and 36)
became spaced en dashes. One decimal comma in maths, `6{,}5` in block 73, became `6.5`.
Four `\text{...}` payloads were German (`abgeschlossen`, `für … Ereignis`, `wenn`, `sonst`)
and were translated; block 26's `\text{für } A \subseteq D \text{ Ereignis } P(A) := …` was
rephrased as `\text{for an event } A \subseteq D \colon \quad P(A) := …`, which is the same
statement in readable English maths.

**One wording I am not certain about.** Block 10's "Das Wort *abgeschlossen* ist dabei keine
Dekoration" – I used "is not decoration here". The German is a lecturer's aside and I wanted
to keep that register rather than flatten it to "is essential".
