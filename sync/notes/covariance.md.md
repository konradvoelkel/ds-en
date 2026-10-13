# Translator's notes: `covariance.md`

German original `kovarianz.md`, 140 blocks, 1 declared drop (the HHU lecture recording
link, block 1), 139 translated blocks. `tools/sync.py align` and `tools/check_english.py`
both pass; no `check-ignore` entries were needed, and no `sync/additions` entry either –
nothing was added, nothing further dropped.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | note |
|---|---|---|
| gemeinsame Verteilung | joint distribution | the chapter's first section heading |
| gemeinsame Dichte / gemeinsame pmf | joint density / joint pmf | |
| Randverteilung, Marginalverteilung | marginal distribution, margin | two German words, one English one – see Decisions |
| Randhistogramm | marginal histogram | figure caption |
| Diagonalabbildung | diagonal map | |
| Koordinatenprojektion | coordinate projection | $\pi_i$ |
| Definitionsbereich (einer Zufallsvariablen) | domain | not "domain of definition" |
| Produktregel | product rule | $p_{X,Y} = p_{Y\mid X}\,p_X$ |
| Summenregel | sum rule | summing out the nuisance variable |
| Satz von Bayes | Bayes' theorem | see Decisions on the admonition |
| Satz von der totalen Wahrscheinlichkeit | law of total probability | not "theorem of total probability" |
| Fassung (eines Satzes) | version | "Bayes' theorem, version 2/3/4" |
| Zerlegung (in disjunkte Ereignisse) | decomposition | |
| Basisrate | base rate | |
| Basisratenfehler | base rate fallacy | the standard English name; literally it is an "error" |
| Sensitivität | sensitivity | glossed as the classifier's recall |
| Falsch-Positiv-Rate | false positive rate | |
| Prior, a priori Wahrscheinlichkeit | prior, a priori probability | |
| Posterior, a posteriori Wahrscheinlichkeit | posterior, a posteriori probability | |
| Evidenz | evidence | also inside maths: `\text{Evidenz}` → `\text{Evidence}` |
| Bayessches Updaten | Bayesian updating | |
| datenerzeugende Verteilung | data-generating distribution | |
| Modellverteilung | model distribution | |
| Maximum-Likelihood-Prinzip | maximum likelihood principle | glossary has the *estimator*, not the principle |
| Korrelationskoeffizient (Pearsonscher) | (Pearson) correlation coefficient | $\rho$ for random variables, $r$ for data |
| empirische Kovarianz | empirical covariance | and *empirischer Korrelationskoeffizient* → empirical correlation coefficient |
| positiv / negativ korreliert | positively / negatively correlated | |
| antikorreliert | anticorrelated | unhyphenated |
| unkorreliert | uncorrelated | |
| Zusammenhang (statistischer) | relationship | not "connection", not "association" |
| skalenabhängig | scale-dependent | rendered in prose as "it depends on the scale" |
| Rechenregeln | rules of calculation | matches `intro-stochastics.md`, which already uses this for $P$ |
| bilinear | bilinear | |
| positiv (semi)definit | positive (semi)definite | |
| fast sicher | almost surely | "almost surely constant", "almost surely $0$" |
| fast überall | almost everywhere | |
| Nullmenge | null set | same choice as the `continuous-distributions.md` translator |
| Skalarprodukt | inner product | see Decisions |
| Streudiagramm, Scatterplot | scatter plot | the German uses both words; English has one |
| Punktwolke | cloud of points | |
| Höhenlinie | contour line | |
| bivariate Normalverteilung | bivariate normal distribution | |
| gemeinsam normalverteilt | jointly normally distributed | |
| Simpson-Paradoxon | Simpson's paradox | link text into `descriptive-statistics.md` |
| Spezies (Iris) | species | |
| Promille | one in a thousand | see Decisions |

## Figures

The chapter references exactly one image, `images/normalmarginal.png`.

**`normalmarginal.png` is clean – no German text, nothing to redraw.** I opened it: it is a
2×2 matplotlib panel with a scatter plot of a bivariate normal sample (top right) and the
two marginal histograms (top left, rotated; bottom right). There are no axis labels, no
titles, no legend and no tick text other than numerals (`-4 … 4`, `0 … 300`). The row in
`images/README.md` that says "labels to check" for `normalmarginal.png` can be struck – I
have not edited that file, as instructed.

One cosmetic point for a human, unrelated to language: the **bottom-left panel is an empty
default axes** (a blank box with ticks running $0.0$ to $1.0$), left over from building the
2×2 grid without turning the unused subplot off. It is in the German original too. If the
figure is ever regenerated, `ax.set_axis_off()` on that subplot would tidy it. Not a
translation issue, so I changed nothing.

## Decisions and doubts

**1. *Randverteilungen* oder *Marginalverteilungen* (block 13).** German has two
interchangeable names and the definition block introduces both in bold. English has
essentially one, "marginal distribution". Dropping the second name would have thinned the
block, so I wrote "the **marginal distributions**, or **margins**, of $X$" – "margins" is
real usage (and is what pandas/R call them) but it is noticeably less common than the
German pair suggests. If the glossary would rather have one name only, delete ", or
**margins**," and nothing else moves.

**2. The Bayes admonitions (blocks 41, 54, 62, 68, 78).** The German splits the theorem's
name across the admonition title and the body: `:::{admonition} Satz` followed by bold
"**von Bayes:**", which reads "Theorem – of Bayes". English cannot do that, so the body now
carries the full name: "Theorem" + "**Bayes' theorem.**", and likewise "**The law of total
probability.**", "**Bayes' theorem, version 2/3/4.**". That is mildly redundant with the
admonition label. The alternative – "**(Bayes)**" in parentheses, as English maths texts
often do – would be tighter but would lose the German's declarative tone. I would like a
human to pick one and apply it book-wide, since `statistical-tests.md` and
`statistical-models.md` will hit the same pattern.

**3. *Skalarprodukt* → "inner product" (block 135).** Both "inner product" and "scalar
product" are defensible. I chose "inner product" because the block goes on to an
$\mathcal{L}^2$ space and to the cosine of an angle, which is the inner-product-space
idiom in English; "scalar product" reads as a physicist's word for the dot product on
$\mathbb{R}^n$. Worth fixing in the glossary before `dimensionality-reduction.ipynb` and
`kernel-methods.ipynb` need it – kernel methods will use this word constantly.

**4. The illness metaphor (block 93).** "Die Kovarianz hat die gleiche *Krankheit* wie die
Varianz … Zur *Heilung* normiert man" became "The covariance suffers from the same
*complaint* as the variance … The *cure* is to normalise". A literal "disease"/"to cure it"
sounded melodramatic in English, and "complaint/cure" keeps the joke. Note the metaphor now
sits two blocks away from an actual disease example (the base-rate test), which it also
does in the German.

**5. *Wahrscheinlichkeit(sdichte)* (block 73).** The German compound packs "probability or
probability density" into one word with a parenthesis. English happens to allow the same
trick: "the probability (density) of seeing exactly these $n$ values". It survives
unchanged, but it is a construction a style pass might want to spell out.

**6. *Promille* (block 84).** "aus einem Promille erst neun Prozent und dann einundneunzig"
became "turn one in a thousand first into nine per cent and then into ninety-one". English
has no everyday word for ‰, and "0.1 per cent" would have broken the sentence's rhythm of
three spoken numbers. The same choice is made in block 47 ("a base rate of one in a
thousand").

**7. *aus einer Population* (block 87).** German "einer" is article-or-numeral ambiguous. In
context – the Simpson's-paradox warning, which is precisely about data falling into groups
– it has to mean *one* population, so I wrote "comes from a single population". Please
confirm; it changes what the warning claims.

**8. Cross-reference link texts.** The German link targets already point at the English
filenames, but the link *texts* were German and I translated them:
`[Erwartungswert und Varianz]` → **[Expected value and variance]** (6 occurrences),
`[Deskriptive Statistik]` → **[Descriptive statistics]** (3),
`[Stetige Verteilungen]` → **[Continuous distributions]** (1),
`[Statistische Modelle und Schätzer]` → **[Statistical models and estimators]** (1),
`[Statistische Modelle]` → **[Statistical models]** (1 – the German is itself inconsistent
and I kept the inconsistency), `[Simpson-Paradoxon]` → **[Simpson's paradox]** (1).
`[Titanic EDA]` (2) was already English. **These must match whatever titles the
`expectation-variance.md`, `descriptive-statistics.md` and `statistical-models.md`
translators settle on** – a job for the consistency pass, not for me.

**9. The section cross-reference *Unabhängigkeit* (blocks 34 and 125).** Rendered
*Independence*. It names a section heading inside `expectation-variance.md`, which is being
translated in parallel; if that translator calls the section something else, both of these
need to follow. (The German italicises it in block 34 and does not in block 125; I kept
that asymmetry rather than silently tidying it.)

**10. Mechanical things, for the record.** Seven decimal commas in display maths became
decimal points (`0{,}99` → `0.99` and friends); three em dashes became spaced en dashes;
`„krank“`/`„Test positiv“` and the single-quoted `'bekannt'`, `'sehen'`, `'cosine
similarity'`, `'Guess the Correlation'` all became plain double quotes per TRANSLATION.md
§6. Inside maths, only `\text{Evidenz}` and `\text{mit }` contained German; both were
translated. The Python block has no German in it and is untouched, outputs included.
