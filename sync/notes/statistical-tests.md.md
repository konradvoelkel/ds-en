# Translator's notes: `statistical-tests.md`

German original `statistische-tests.md`, 224 blocks, one declared drop (block 1, the HHU
Mediathek recording link), 223 blocks in the English file. No additions, no further drops.
`tools/sync.py align statistical-tests.md` and `tools/check_english.py statistical-tests.md`
both pass; `check_english` reports nothing, so there is no
`sync/check-ignore/statistical-tests.md.json`.

## New terminology

Everything below was decided in this chapter and is not yet in `TERMINOLOGY.md`.

### Interval estimation

| German | English | note |
|---|---|---|
| Prognoseintervall | prediction interval | the section heading; the same paragraph contrasts it with *Konfidenzintervall* → confidence interval, which is already in the glossary |
| Konfidenzbereich | confidence region | the set-valued version; *Konfidenzintervall* stays the interval |
| Bereichsschätzer | set estimator | the general non-point estimator, heading *From set estimator to test* |
| Intervallschätzer | interval estimator | the special case the chapter actually uses |
| Irrtumsniveau | error level | "confidence region for $\tau$ at error level $\alpha$"; distinct from *Signifikanzniveau* → significance level, already in the glossary |
| Punktschätzung, Punktschätzer | point estimate, point estimator | |
| Standardfehler | standard error | |
| Bootstrap | bootstrap | lower case in running English prose |
| Zufallsstichprobe | random sample | |
| Stichprobenfehler, Samplingfehler | sampling error | the German uses both words, English has one |
| Prozentpunkte | percentage points | |
| Kennzahl | summary measure | follows the glossary's *Maßzahl → summary measure*; "summary statistic" was avoided because the chapter also has *Statistik* in the technical sense |
| Quantiltransformation | quantile transformation | |

### Tests

| German | English | note |
|---|---|---|
| Nullhypothese / Alternative | null hypothesis / alternative | the glossary has the null hypothesis only |
| Entscheidungsregel | decision rule | |
| nichtrandomisiert / randomisiert | non-randomised / randomised | house `-ise` spelling |
| Niveau (eines Tests) | level | "a test of level $\alpha$" |
| effektives Niveau | effective level | |
| Fehler erster / zweiter Art | type I error / type II error | the standard English names; "error of the first kind" reads as translated German |
| Gütefunktion | power function | $G_\phi(\theta) = \mathbb{E}_\theta(\phi)$ – this really is what English calls the power function |
| Macht, Stärke | power | the German glosses itself, "Macht (oder Stärke, engl. power)"; the doublet collapses to the one English word, which the glossary already has for *Teststärke* |
| gleichmäßig bester Test zum Niveau $\alpha$ | uniformly best test at level $\alpha$ | kept literal – see *Decisions* |
| einfache Hypothesen | simple hypotheses | |
| Likelihood-Quotient | likelihood ratio | not "likelihood quotient" |
| Neyman-Pearson-Test, -Lemma | Neyman–Pearson test, lemma | en dash in the name, as for *Radon–Nikodym* |
| Lemma von Stein | Stein's lemma | genitive, as for *Satz von Bayes → Bayes' theorem* |
| Schwellwert | threshold | |
| Teststatistik | test statistic | |
| z-Test, Gauß-Test | z-test, Gauss test | |
| z-Statistik, t-Statistik | z-statistic, t-statistic | |
| z-Wert | z-value | |
| beidseitiger / einseitiger Test | two-sided / one-sided test | |
| Student t-Verteilung | Student t distribution | no apostrophe and no hyphen, mirroring the German's own *Student t-Verteilung* |
| Student t-Test | Student t-test | the section heading *The Student t-test* |
| $\chi^2$-Verteilung, Chi-Quadrat-Verteilung | $\chi^2$ distribution, chi-squared distribution | the spelled-out form only in the figure caption, as in the German |
| Verteilungsfreiheit | distribution-free | rendered adjectivally – see *Decisions* |
| p-Wert | p-value | |
| Signifikanz, statistisch signifikant | significance, statistically significant | |
| sehr signifikant / hochsignifikant | very significant / highly significant | |
| p-value hacking | p-value hacking | the German already uses the English |
| Publikationsbias | publication bias | |
| Vorregistrierung (von Studien) | pre-registration | |
| Homoskedastizität, Varianzhomogenität | homoscedasticity, homogeneity of variance | British `-sc-`; the German's own gloss is kept because it explains the Greek |
| Residuen | residuals | |
| Kontingenztabelle | contingency table | the glossary has *Kontingenztafel* under *Kreuztabelle*; same word, same translation |
| erwartete Häufigkeit | expected frequency | |
| Shapiro-Wilk | Shapiro–Wilk | en dash |
| Pearson's Korrelation | Pearson correlation | the German's apostrophe-s is not English usage here |
| Formparameter | shape parameter | see *Decisions* |

### The polling digression

| German | English | note |
|---|---|---|
| Befragte | respondents | also in the code's `print` strings and their output |
| Zweitstimme | second vote (the party vote) | glossed once on first use; the German system needs the gloss for a reader outside Germany |
| Bundestagswahl | German federal election | *Bundestag* and *Bündnis Sahra Wagenknecht* / *BSW* stay as proper names |
| Fünf-Prozent-Frage | five-per-cent question | section heading; British "per cent" |
| Umfrageinstitut | (polling) institute | |

## Figures

Both of my chapter's figures are listed in `images/README.md` as "labels to check". I opened
both with the Read tool. **Both have German text baked in and still need redrawing.** I did
not touch `images/README.md` (shared file) – the two rows need updating by whoever redraws
them.

`images/chi-quadrat-verteilungen.png` (used at `:name: chiquadrat`), a matplotlib line plot
of three densities on a white ground:

* suptitle: `χ²-Verteilungen mit verschiedenen Parametern`
* legend, three entries: `4 Freiheitsgrade`, `8 Freiheitsgrade`, `16 Freiheitsgrade`
* axes carry numeric ticks only (x from 0 to 30, y from 0.000 to 0.175); no axis labels.

English replacements would be `χ² distributions with various parameters` and
`4 / 8 / 16 degrees of freedom`.

`images/student-t-verteilungen.png` (used at `:name: studentt`), same style:

* suptitle: `Student t-Verteilung mit verschiedenen Parametern und Standardnormalverteilung`
  (note the German's own inconsistency: singular *Verteilung* in the title, plural in the
  caption I translated)
* legend, four entries: `4 Freiheitsgrade`, `8 Freiheitsgrade`, `16 Freiheitsgrade`,
  `Standardnormalverteilung` (the dashed black curve)
* numeric ticks only (x from −6 to 6, y from 0.00 to 0.40); no axis labels.

English replacements would be `Student t distributions with various parameters and the
standard normal distribution`, `4 / 8 / 16 degrees of freedom`, `standard normal
distribution`.

Both are plain `scipy.stats` density plots and would be two short functions in
`images/make_figures.py`. The captions in the chapter are already translated; the file names
stay until the figures are actually redrawn, per `images/README.md`.

The chapter's other figures need nothing: `global_warming_without_confidence.png`,
`global_warming_with_confidence.png` and `likelihood-scale.png` are IPCC/IIASA material and
already English (`likelihood-scale.png` is still marked "to do" in `images/README.md` but is
attributed to `statistical-models` there – it is used here, and it is English; the row can be
struck), `xkcd-significant.png` and `pvalue-hacking.png` are English third-party images.

## Decisions and doubts

**"nicht klausurrelevant", six occurrences.** Handled per TRANSLATION.md §2, never as
"not examinable":

* the long `:::{note}` under *Looking ahead: confidence intervals* –
  "**Looking ahead (not part of the course proper):**". Its second sentence,
  "werden für sich genommen nicht in der Klausur abgefragt", is the same statement again and
  became "taken on their own they are not part of the course proper". Its last sentence
  points the reader at two other sections, not at an exam, so it stays.
* the two short notes under *From set estimator to test* and *Best simple tests* –
  "Looking ahead, not part of the course proper (see the note at *Confidence intervals*)."
* "insbesondere nicht klausurrelevant" about the $\chi^2$ density –
  "and in particular is not part of the course proper".
* the `:::{note}` opening the polling digression –
  "**Digression (not part of the course proper):**", matching
  `expectation-variance.md`'s "**Digression (not part of the course proper):**".
* "für uns erstmal nicht so wichtig" about the t density carries no marker and was left as
  the plain sentence it is.

The three `## Ausblick:` headings became `## Looking ahead:` (TRANSLATION.md §5), and
`## Exkurs:` became `## Digression:` (the glossary's choice from `expectation-variance.md`).

**The three hardest decisions.**

1. **`Macht` / `Gütefunktion` / `gleichmäßig bester Test`.** The German has three words where
   English has a tangle. *Macht (oder Stärke, engl. power)* glosses itself with the English
   word, so it collapses to **power**; *Gütefunktion* is then **power function**, which is
   both the literal thing ($G_\phi(\theta) = \mathbb{E}_\theta(\phi)$) and the standard
   English name, so that one is free. The hard one is *gleichmäßig bester Test*: English
   almost always says **uniformly most powerful** (UMP), and a reader who has met the subject
   before will expect that phrase. I translated it literally as **uniformly best test**
   anyway, for two reasons: the definition in the block immediately above spells out what
   "best" means here, and `statistical-models.md` (still German) has the parallel
   *gleichmäßig bester erwartungstreuer Schätzer*, which will want "uniformly best unbiased
   estimator" – changing one and not the other would break the pair. **Worth a human
   decision**: if the book would rather use UMP, both chapters have to move together.
2. **`Verteilungsfreiheit`.** The property the German names is that $T$'s distribution does
   not depend on the unknown $\mu(Z)$. The exact English term for that is *pivotal quantity*;
   *distribution-free* is normally reserved for non-parametric procedures. The German has
   picked the looser word, and inventing "pivotal" here would be translating the statistics
   rather than the book, so I kept the German's choice and made it adjectival: "One says that
   the statistic is **distribution-free**." ("Distribution-freeness" is not a word anyone
   should have to read.) **Worth a human decision** if the course wants the precise term.
3. **`Fehler erster Art` → "type I error".** The literal "error of the first kind" exists in
   English but reads as translated German, and the chapter uses the phrase six times,
   including in the bolded reminder before the xkcd strip. "Type I / type II error" is what
   an English reader has met everywhere else, so I used it throughout, lower-case "type",
   Roman numerals. The German *2ter Art* in the take-home message likewise became "type II
   error".

**Other decisions.**

* `Bereichsschätzer` → **set estimator**, `Intervallschätzer` → **interval estimator**,
  `Konfidenzbereich` → **confidence region**. The German keeps all three apart and so does
  the English; the heading *From set estimator to test* has to match the forward reference in
  the long note, and it does.
* `gemischtes Modell` (block 3, in the sentence that links to Expectation Maximization) →
  **mixture model**, not "mixed model": the link is to the EM chapter, and "mixed model" is a
  different animal in English (random effects). The glossary's *Mischverteilung → mixture
  distribution* supports it.
* `Irrtumsniveau` → **error level**, kept distinct from the glossary's *Signifikanzniveau →
  significance level*, because the chapter later uses plain *Niveau* for the level of a test
  and the reader needs the three to stay apart.
* `Formparameter` (in "mit der Begrifflichkeit des Formparameters aus jedem Test einen
  Bereichsschätzer konstruieren") → **shape parameter**. The German sentence is obscure to
  me: the usual way to invert a test into a confidence set does not go through a shape
  parameter. I translated it literally rather than repair it. **A human who knows what was
  meant should check this sentence**; if it is a slip in the German, that is an upstream fix.
* `differenz` in the bootstrap cell → `difference` (TRANSLATION.md §4: German variable names
  invented by the notebook are translated). The German `print` strings in the polling cell
  were translated too, and the fenced output block below them was updated to match; I
  re-derived the four numbers by hand (`se` for $n=1000$ is $0.006892$, so $0.69$ and
  $1.35$; for $n=2000$, $0.004873$, so $0.49$ and $0.96$) and they are unchanged from the
  German, only the words around them differ. **The cells are not executed** – this chapter is
  Markdown, not a notebook, so nothing was re-run.
* `|t_{\text{beob}}|` → `|t_{\text{obs}}|`. German inside `\text{}`, exactly the trap the
  brief warned about. The other `\text{}` hits were `\text{ (Indikatorfunktion)}` →
  `\text{ (indicator function)}` and `\text{ Millionen Befragte}` →
  `\text{ million respondents}`.
* Decimal commas: `1{,}96`, `0{,}05`, `4{,}981\,\%`, `5{,}000\,\%`, `0{,}0002`, `4{,}6`,
  `1{,}4` and friends all became points. The thousands separator went the other way:
  `9.529 Stimmen` → `9,529 votes`. The thin space inside maths (`$5\,\%$`, `$1.96\,\sigma$`)
  stays, per TRANSLATION.md §6; bare prose percentages close up (`95 %` → `95%`).
* German links marked "(in German)": `bundeswahlleiterin.de` (the official result) and
  `wahlrecht.de` (the poll archive). Both are German-only and have no English counterpart.
  `datacolada.org`, `xkcd.com`, the PLOS Medicine DOI and the IPCC citation are English and
  were left alone.
* The MyST target `(signifikanz)=` keeps its German spelling (TRANSLATION.md §3), and the two
  in-text references read `[Significance](#signifikanz)`. `check_english.py` does not flag
  it, so no `check-ignore` entry was needed. Note that the target line and the `## Significance`
  heading are a single block (no blank line between them) – do not separate them.
* The xkcd caption quotes the comic's last panel verbatim; it is already English in the
  German original and was left verbatim, with `„Significant“` normalised to `"Significant"`.
  Likewise the Ioannidis block quotation, which was already English.
* `Methodik-Dozent\*innen` → "methodology lecturers" (TRANSLATION.md §6).
* `Weltklimarat` – the German's gloss of "IPCC" – was dropped: IPCC *is* the English name,
  and glossing it with its own expansion would be noise.
* "Wir wissen, dass wir nichts wissen" → "'We know that we know nothing'", kept in quotes as
  the aside it is.
* `Der $N \ge 30$-Mythos` is a cross-reference into `normal-distribution.ipynb`, which is
  still German. I translated the section name as *The "$N \ge 30$" myth*. **A human must
  re-check this once that notebook is translated** – if the heading there lands differently,
  this reference goes stale silently.
* Link texts follow the already-translated chapters: *The most important discrete
  distributions*, *The normal distribution*, *Titanic EDA*, and *Expectation Maximization*
  (which the German original already writes in English).
