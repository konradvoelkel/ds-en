# Translator's notes: `statistical-models.md`

German original `statistische-modelle.md`, 145 blocks, 1 declared drop (the HHU lecture
recording link, block 1), 144 translated blocks. `tools/sync.py align` and
`tools/check_english.py` both pass; no `check-ignore` entries were needed, and no
`sync/additions` entry either – nothing was added, and nothing was dropped beyond the
recording link that was already declared.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | note |
|---|---|---|
| statistisches Modell | statistical model | the chapter's central object; the glossary had only *Modell-Auswahl* and *Modellverteilung* |
| Stichprobenraum, Stichprobenmenge | sample space | $\mathcal{X}$; collides with the glossary's *Ergebnisraum → sample space* ($\Omega$) – see *Decisions* |
| Statistik (die Abbildung) | statistic | the countable noun, not the field; *Statistik* the field stays *statistics* |
| Ereignisraum | event space | the set $\Sigma$ with a $\sigma$-algebra on it |
| Kenngröße | characteristic quantity | the value $\tau(\theta)$ an estimator aims at – see *Decisions* |
| parametrisches Modell | parametric model | |
| einparametriges Modell | one-parameter model | |
| diskretes / stetiges Modell | discrete / continuous model | |
| Standardmodell | standard model | discrete or continuous |
| Produktmodell | product model | $\mathcal{X}^N$, the $N$-fold repetition |
| Niveaumenge | level set | of a continuous function |
| Punktschätzer | point estimator | the German's own parenthetical second name |
| Erwartungstreue | unbiasedness | the section heading; the glossary has only the adjective *erwartungstreu → unbiased* |
| verzerrt (biased) | biased | the German glosses itself with the English word; the doublet collapses |
| bias, $\mathbb{B}_\theta(T)$ | bias | the German already uses the English word, lower case |
| asymptotisch erwartungstreu | asymptotically unbiased | |
| gleichmäßig bester erwartungstreuer Schätzer | uniformly best unbiased estimator | see *Decisions* |
| Cramér-Rao-Ungleichung | Cramér–Rao inequality | en dash in the name, as with *Radon–Nikodym* |
| Fisher-Information | Fisher information | no hyphen in English |
| Exponentialfamilie | exponential family | |
| Likelihood-Funktion | likelihood function | the glossary has the *estimator* and the *principle*, not the function |
| log-Likelihood | log-likelihood | hyphenated, lower case |
| Beobachtungswert | observed value | $L_x$ is the likelihood "for the observed value $x$" |
| Maximalstellen | the places where the maximum is attained | rendered as "attain their maxima in the same places" |
| Hypothesentest | hypothesis test | the glossary has *Hypothese*, not the test |
| Signifikanz | significance | the notion the tests chapter calls problematic |
| Fehlerbereich | margin of error | what a confidence interval adds to a point estimate |
| kategorielle Variable | categorical variable | the German spells it *kategoriell* here, *kategorial* elsewhere; one English word |
| Pasch / Keinpasch | doubles / no doubles | also inside maths: `\text{Pasch}` → `\text{doubles}`, `\text{Keinpasch}` → `\text{no doubles}` |
| Würfelaugen | numbers of pips | plural of the glossary's *Augenzahl → number of pips* |
| gemischtes Modell | mixture model | the k-means example; the glossary has *Mischverteilung → mixture distribution* for the distribution |
| Zentroid | centroid | plural *centroids* |
| Einheitsmatrix | identity matrix | not "unit matrix" |
| Wartezeit | waiting time | the exponential-distribution example |
| Server-Logfiles | server log files | three words in the English edition |
| Aufruf (einer Web-Anwendung) | request | "gaps between two requests", "requests per unit of time" |
| Zeitstempel | timestamp | one word |
| Approximations-Algorithmus | approximation algorithm | |
| EM-Algorithmus | EM algorithm | link text into `expectation-maximization.ipynb` |
| Expectation Maximization Algorithmus | expectation maximization algorithm | the `-ize` stays: it is the algorithm's name and the chapter's title |
| Kunstgriff | move | "the crucial move is in the last row" – "artifice" and "sleight of hand" both oversell it |
| umgangssprachlich / formal (table header) | in everyday terms / formally | the map table before the definitions |

## Figures

`images/likelihood-scale.png` is listed in `images/README.md` as "labels to check". I opened
it. **It is clean: there is no German in it at all.** It is the IPCC's calibrated-language
table, reproduced in English exactly as published: a header row "Table 1. Likelihood Scale",
two columns headed "Term\*" and "Likelihood of the Outcome", seven rows pairing a term
(virtually certain, very likely, likely, about as likely as not, unlikely, very unlikely,
exceptionally unlikely) with a probability range (99-100%, 90-100%, 66-100%, 33 to 66%,
0-33%, 0-10%, 0-1% probability), and a footnote about three further terms used in the AR4
(extremely likely, more likely than not, extremely unlikely) that may also be used in the
AR5. Nothing needs redrawing.

Two things for whoever maintains `images/README.md` (I did not edit it, as instructed):

* the row for `likelihood-scale.png` can be struck through and marked **clean**;
* its "used in" column says `statistical-models`, but the figure is actually used in
  `statistical-tests.md` (block with `:name: likelihood-scale`), not in this chapter. My
  chapter has no figures at all.

The figure is a quotation from an IPCC report and carries a `{cite}` key in
`statistical-tests.md`; its text is English in the source, so it must not be "translated"
or redrawn in any case.

## Decisions and doubts

**1. `Stichprobenraum` → "sample space", colliding with `Ergebnisraum`.** `TERMINOLOGY.md`
already assigns "sample space" to *Ergebnisraum / Grundraum*, the $\Omega$ of
`intro-stochastics.md`. This chapter's $\mathcal{X}$ is a different object – the space of
whole samples, $\mathbb{R}^n$ rather than $\mathbb{R}$ – and German keeps the two apart with
two words. English statistics calls $\mathcal{X}$ the sample space too, and I could find no
second English name that a reader would recognise ("observation space" is not standard
enough to carry a definition). So both are "sample space" here. The collision is softened by
the fact that the chapter itself flags it: block 14 exists precisely to say that
$\mathcal{X}$ is not the space of a single measurement, and the product-model remark jokes
that "the population $\Omega$ sends its regards". **A human should check** that this reads
as deliberate rather than careless, and decide whether the glossary wants a row recording
the double assignment.

**2. `gleichmäßig bester erwartungstreuer Schätzer` → "uniformly best unbiased estimator".**
The established English name is *uniformly minimum variance unbiased estimator* (UMVUE).
I did not use it. The German is itself literal, offers no abbreviation, and the surrounding
text shortens it to *gleichmäßig beste Schätzer*, which "uniformly best estimators" tracks
and "UMVU estimators" does not. Adding "(UMVUE)" would have been a gloss the German does not
have, and §1 forbids smuggling new material in. **A human should decide** whether the book
wants to hand the reader the standard search term here; if so, it belongs in the German too.

**3. `stochastische Konvergenz (auch: Konvergenz in Wahrscheinlichkeit)` – the doublet
collapses.** The glossary rules that *stochastische Konvergenz* is "convergence in
probability" and that "stochastic convergence" would be a Germanism. The definition block
then offers two German names for one English one, and the parenthetical gloss has nothing
left to gloss. I dropped the parenthesis inside the block rather than inventing a second
English name. The same thing happens twice more and I handled it the same way: *verzerrt
(biased)* becomes plain "biased", and *Maximum-Likelihood-Schätzer (maximum likelihood
estimator, MLE)* becomes "maximum likelihood estimator (MLE)" – in both the German
parenthesis exists only to supply the English word.

**Other decisions, smaller:**

* **`nicht klausurrelevant`.** The `:::{note}` before the Cramér–Rao passage reads
  "**Ausblick (nicht klausurrelevant):**" and becomes "**Looking ahead (not part of the
  course proper):**", per TRANSLATION.md §2 and the §5 title table. The sentence that
  follows, "Sie werden im Kurs nicht benötigt", stays as a mention of the course: it is a
  passing reference, not a pointer at an exercise sheet the reader cannot have.
* **`:::{admonition} Satz` does not occur in this chapter.** The split-name pattern of §5
  therefore never arose. The chapter's one named result is a `:::{admonition} Proposition`
  with no name in the body, and the two lead-in bold names that do exist – "**Maximum
  likelihood for the exponential distribution.**" and "**An application: server log
  files.**" – stay in the body of their `Beispiel`/Example blocks, exactly where the German
  put them.
* **`Kenngröße` → "characteristic quantity".** Stiffer than I would like. "Quantity of
  interest" reads better but says more than the German, which is deliberately empty at this
  point: the next Remark insists that $T$ need have nothing to do with $\tau$. I kept the
  stiff literal word.
* **`Pasch` → "doubles".** The English dice term, and it survives inside `\text{...}`.
  "no doubles" for *Keinpasch* loses the German's one-word joke; English has no single word.
* **Link texts.** `Statistische Tests` → "Statistical tests", `Deskriptive Statistik` →
  "Descriptive statistics", `Kovarianz und Abhängigkeit` → "Covariance and dependence",
  `Wichtigste diskrete Verteilungen` → "The most important discrete distributions" – all
  following the glossary and the forms already used in the six translated chapters.
  `k-Means` and `EM-Algorithmus` → "k-Means" (the chapter title) and "EM algorithm".
  In running prose the algorithm is "the k-means algorithm", lower case, as English writes it.
* **Maths.** Two decimal commas became points (`2{,}5` → `2.5`, `0{,}4` → `0.4`), and the
  German inside `\text{...}` was translated (`Pasch`, `Keinpasch`). `\text{uni}`,
  `\text{norm}`, `\text{exp}` are abbreviations of the distribution names and read the same
  in both languages, so they stay. The two code comments `# Nenner n` / `# Nenner n-1`
  became `# denominator n` / `# denominator n-1`; the sampled numbers and the printed values
  are untouched, so the cell still produces exactly what the comments claim.
* **Dashes.** Five German ` - ` and six `—` became the book's spaced en dash ` – `,
  including the one inside the map table.
* **`gut zwei Prozent`** → "a good two per cent", spelled out, so the percentage rule of §6
  (`5 %` → `5%`) never bites; there is no numeral-plus-sign percentage anywhere in the
  chapter.
