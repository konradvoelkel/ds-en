# Translator's notes: `descriptive-statistics.md`

German original `deskriptive-statistik.md`, 146 blocks, one declared drop (block 1, the
three HHU Mediathek recording links), 145 blocks in the English file.
`tools/sync.py align` and `tools/check_english.py` both pass.

## New terminology

Everything below was decided in this chapter and is not yet in `TERMINOLOGY.md`. The
chapter is the book's vocabulary lesson, so the list is long on purpose.

### Levels of measurement

| German | English | note |
|---|---|---|
| Skalenniveau | level of measurement | the Stevens term; "scale type" where the German says *Skalenart* |
| Skalenart | scale type | |
| nominal-/ordinal-/kardinalskaliert | on a nominal / ordinal / cardinal scale | "nominally scaled" reads as translated German; prefer "on a … scale" |
| Nominalskala | nominal scale | |
| Ordinalskala | ordinal scale | |
| Intervallskala | interval scale | the table row is just "interval" |
| Verhältnisskala | ratio scale | the table row is just "ratio" |
| Kardinalskala | cardinal scale | see *Decisions* – English normally says "interval or ratio", but the book needs the umbrella |
| Ausprägung | level | TERMINOLOGY allows "value, level"; this chapter uses **level** throughout, because "value" collides with the numbers |
| Maßzahl | summary measure | "summary statistic" where the German says *summarische Statistik* |
| Lagemaß, Lageparameter | measure of location | |
| Streuungsmaß, Streumaß | measure of spread | "measure of dispersion" only where the German says *Dispersionsmaß* |
| zentrale Tendenz | central tendency | |
| Mohs-Härte | Mohs hardness | |
| Likert-Skala | Likert scale | |
| Postleitzahl | postcode | British spelling, per TRANSLATION.md section 6 |
| Studiengang | degree programme | |
| Schulnote | school grade | |
| Matrikelnummer | student number | |
| laufende Nummer | serial number | |

### Descriptive statistics

| German | English | note |
|---|---|---|
| deskriptive / beschreibende Statistik | descriptive statistics | the German doublet collapses, see *Decisions* |
| inferentielle / schließende Statistik | inferential statistics | likewise |
| summarische (zusammenfassende) Statistik | summary statistics | |
| Grundgesamtheit | population | *Population* in the German is already the loan word |
| Stichprobenumfang / Umfang | sample size | |
| arithmetisches Mittel | arithmetic mean | |
| geometrisches Mittel | geometric mean | |
| Bereichsmitte (Mid-range) | mid-range | |
| Modus | mode | |
| unimodal / bimodal / multimodal | unimodal / bimodal / multimodal | |
| Spannweite | range | note the collision: *Interquartilsabstand* is also a "range" in English |
| Interquartilsabstand | interquartile range | IQR |
| Variationsverhältnis | variation ratio | |
| nicht-Modus-Anteil | non-modal proportion | |
| Quartil, unteres/oberes Quartil | quartile, lower/upper quartile | |
| Perzentil | percentile | |
| Stichprobenvarianz | sample variance | |
| Stichprobenstandardabweichung | sample standard deviation | |
| Bessel-Korrektur | Bessel correction | |
| Variationskoeffizient | coefficient of variation | |
| Signal-to-Noise-Ratio | signal-to-noise ratio | |
| mittlere absolute Abweichung | mean absolute deviation | |
| mittlere quadratische Abweichung | mean squared deviation | |
| Schiefe | skewness | |
| rechtsschief | skewed to the right | |
| Wölbung | kurtosis | |
| Exzess | excess kurtosis | the German *Exzess* alone is a false friend |
| Form | shape | |
| Kreuztabelle, Kontingenztafel | cross-tabulation (contingency table) | |
| Konfusionsmatrix | confusion matrix | already in TERMINOLOGY |
| Störvariable, Confounder | confounder | the German gloss *(Störvariable)* disappears |
| latente Variable | latent variable | |
| Mischung, Mischverteilung | mixture, mixture distribution | |
| Simpson-Paradoxon | Simpson's paradox | possessive, not "the Simpson paradox" |
| Kodierung kategorialer Merkmale | encoding categorical features | |
| One-Hot-Encoding | one-hot encoding | |
| Integer-/Ordinal-Encoding | integer / ordinal encoding | |
| Dummy-Variable | dummy variable | |
| Durchgerechnetes Beispiel | a worked example | the heading |
| Probe | check | as in "check: …" at the end of the worked example |

### Plots, visualisation, colour

| German | English | note |
|---|---|---|
| Visualisierung | visualisation | house spelling |
| Häufigkeitsverteilung | frequency distribution | |
| Balkendiagramm | bar chart | |
| Säulendiagramm / Column chart | column chart | the German already uses the English |
| gestapelte Balken | stacked bar chart | |
| Eimergröße (bucket size) | bucket size | |
| binsize | bin size | two words in the English edition |
| Klassengröße | class width | not "class size" – it is the width of the interval |
| Klasse (im Histogramm) | class, bin | |
| Scatterplot | scatter plot | two words, matching `covariance.md` |
| Boxplot, Box-and-Whiskers-plot | boxplot, box-and-whiskers plot | one word for boxplot, as in the German |
| Linienplot | line plot | |
| Tortendiagramm | pie chart | |
| Violinenplot | violin plot | |
| Kartendarstellung | map plot | |
| Dichteplot | density plot | |
| Grammatik der Grafiken | grammar of graphics | |
| Schicht (Layer) | layer | |
| Ästhetik, ästhetische Zuordnung | aesthetic, aesthetic mapping | |
| Positionsbestimmung | position adjustment | the ggplot2 term is *position adjustment* |
| Facette, Facettenspezifikation | facet, facet specification | |
| Glättung | smoothing | |
| faktorielle Variable | factor variable | |
| Farbskala | colour scale | |
| Farbpalette | colour palette | |
| Farbsehschwäche | colour vision deficiency | |
| Dichromasie | dichromacy | |
| Normalsicht | normal colour vision | not "normal sight" – it is about colour only |
| Deuteranopie / Protanopie / Tritanopie | deuteranopia / protanopia / tritanopia | |
| Ampel-Kodierung | traffic-light coding | |
| Helligkeit (einer Farbe) | lightness | not "brightness"; it is the perceptual axis |
| Beamer | beamer | kept: "projector" loses the German-campus flavour, and the sentence already says "projected" |
| Buntheit | colourfulness | |

### Statistics vs. machine learning (the correspondence list)

| German | English | note |
|---|---|---|
| Begriffskorrespondenz | corresponding terms | |
| Gewichte | weights | |
| Fitten | fitting | |
| Testdatensatz-Performance | performance on the test set | |
| Generalisierung | generalisation | |
| Dichteschätzung | density estimation | |
| Klassenbildung (clustering) | clustering | the German gloss disappears |
| Fehlerfunktion (Verlustfunktion) | error function (loss function) | the doublet survives because the next entry is "loss" |
| Epoche | epoch | |
| Data Mining | data mining | lower case in running English prose |
| explorative Datenanalyse | exploratory data analysis | already in TERMINOLOGY; EDA on second use |

## Figures

Every image this chapter references, opened and looked at.

| File | German text? | What to do |
|---|---|---|
| `images/ds-process-oneill.png` | no | leave |
| `images/AllDinosGrey_1.png` | no | leave |
| `images/layers-einzeln.png` | no | **strike the row in `images/README.md`** |
| `images/layers-zusammen.png` | no | **strike the row in `images/README.md`** |
| `images/gute-palette.png` | no | **strike the row in `images/README.md`** |
| `images/simpson-paradoxon.png` | yes | redraw, text below |
| `images/farbwahrnehmung-simulation.png` | yes | redraw, text below |

### `images/simpson-paradoxon.png` – redraw

A matplotlib scatter plot, two coloured groups, a black regression line per group and a
red dashed line over all points. Every string in it is German:

| German in the PNG | suggested English |
|---|---|
| title: `Simpson-Paradoxon: in jeder Gruppe steigend, insgesamt fallend` | `Simpson's paradox: rising in each group, falling overall` |
| x label: `Merkmal x (z.B. Dosis)` | `Feature x (e.g. dose)` |
| y label: `Ergebnis y (z.B. Erfolg)` | `Outcome y (e.g. success)` |
| legend: `Gruppe 1 (z.B. kleine Steine)` | `Group 1 (e.g. small stones)` |
| legend: `Gruppe 2 (z.B. große Steine)` | `Group 2 (e.g. large stones)` |
| legend: `Trend über alle Punkte` | `Trend over all points` |
| legend: `Trend je Gruppe` | `Trend per group` |

The caption in the chapter is already translated and says the groups rise while the
overall trend falls, so the redraw must keep that geometry (group 1 lower left, group 2
lower right, red dashed line falling). No vector source in the German repository; a
regenerating script would be the right thing to commit next to it.

### `images/farbwahrnehmung-simulation.png` – redraw

Four panels, each showing the same eight-colour palette as vertical bars.

| German in the PNG | suggested English |
|---|---|
| suptitle: `Dieselbe Palette, wie sie bei verschiedenen Arten des Farbsehens erscheint` | `The same palette as it appears under different kinds of colour vision` |
| panel: `Normalsicht` | `Normal colour vision` |
| panel: `Deuteranopie` | `Deuteranopia` |
| panel: `Protanopie` | `Protanopia` |
| panel: `Tritanopie` | `Tritanopia` |

Panel order in the file is normal / deuteranopia (top row), protanopia / tritanopia
(bottom row). The chapter's caption names the Viénot–Brettel–Mollon 1999 method, so the
regenerating script should keep that transform.

### Not this chapter's figures, despite `images/README.md`

`images/README.md` lists `dsprozess-simplified-1/2/3.png` under "Used in:
descriptive-statistics". They are **not** referenced by this chapter; the only file that
references them is `random-variables-distributions.md`. I have not touched
`images/README.md`, but the "Used in" column wants correcting, and whoever owns
`random-variables-distributions.md` should own the redraw. Since I had them open anyway,
the exact strings are:

* `dsprozess-simplified-1.png`: globe → `Ausschnitt` → `Rohdaten` → `Daten`
  (section → raw data → data; TERMINOLOGY fixes *Ausschnitt* as "section")
* `dsprozess-simplified-2.png`: globe → `Daten` → `Modell` → `Synthetische Daten`
  (data → model → synthetic data). The README row says "as above, plus Modell", which is
  wrong: the boxes are different, and `Synthetische Daten` is missing from the row.
* `dsprozess-simplified-3.png`: globe → `Daten` → `Transformierte Daten` → `Zielgröße`
  (data → transformed data → target variable)

### A remark on `images/ds-process-oneill.png`

Not a translation problem, but worth a human's eye: the file is a photograph of a printed
book page, skewed, with the text of the reverse side showing through. It is legible but
it is the ugliest figure in the chapter. If anyone ever redraws it, the content is
Real World → Raw Data is Collected → Data is Processed → Clean Data, with Exploratory
Data Analysis and Machine Learning Algorithms / Statistical Models branching off, down to
Build Data Product and Communicate / Visualizations / Report Findings → Make Decisions.
That is attributed third-party content ({cite}`dds`, p. 41), so a redraw needs the same
attribution the caption already carries.

## Decisions and doubts

**`Kardinalskala` → "cardinal scale".** English textbooks in the Stevens tradition have no
single word for "interval or ratio"; they say "metric", "quantitative", or just spell both
out. The chapter leans on the umbrella five times ("kardinal skalierte Merkmale", "Eine
Spalte mit dem Datentyp `int` ist noch lange nicht kardinalskaliert"), and the German
explicitly introduces the interval scale as "eine Kardinalskala". I kept "cardinal scale",
introduced in that same parenthesis. If a human prefers "metric scale", it is six
occurrences and a glossary row. Flagging it as the one term in the chapter most likely to
read as translated German to a statistician.

**`Ausprägung` → "level", not "value".** `TERMINOLOGY.md` allows both. In this chapter the
word appears next to actual numeric values on every page ("auch wenn die Ausprägungen als
Zahlen gespeichert sind"), so "value" would have been ambiguous exactly where precision is
the point. "Level" is the standard English term for a level of a categorical variable and
it survives into the one-hot-encoding paragraph unchanged. Worth making binding.

**The German doublets collapse.** `beschreibende (deskriptive) Statistik` and
`schließende (inferentielle) Statistik` each put a German word next to a Latinate one; in
English there is only "descriptive" and "inferential". Same for `Klassenbildung
(clustering)` and `Störvariable / Confounder`, where the German glosses an English loan
word that needs no gloss here. Those parentheses are gone. This is the only kind of place
where the English sentence carries less than the German one, and it is unavoidable.

**`Spannweite` and `Interquartilsabstand` both become "range".** German distinguishes them
lexically, English does not (range / interquartile range). In the table of permissible
summary measures the two now sit in the same cell as "range, interquartile range", which
reads fine, but it is a distinction the English reader has to get from the modifier.

**"Such new columns are features as well" (step 4 of the EDA process).** The German says
`Solche neuen Merkmale heißen **Features**` – a genuine piece of information in German,
where *Merkmal* and *Feature* are two words. In English it would be a tautology ("such new
features are called features"). I rewrote it as "Such new columns are features as well",
which keeps the point (derived columns count as features) without the empty naming act. I
deliberately did **not** introduce "feature engineering", which the German does not say.

**Violin plot, `ausschnittsweise`.** `anstelle eines Rechtecks wird die Dichteverteilung
ausschnittsweise dargestellt` is genuinely unclear in the German – it may mean "over the
range of the data" or "as a cross-section". I wrote "in place of a rectangle the density
is drawn in outline", which is true of a violin plot and commits to neither reading. Worth
a glance from the author.

**Links.** The German Wikipedia article "Histogramm" is replaced by
`https://en.wikipedia.org/wiki/Histogram`, per TRANSLATION.md section 3. The HeiCAD video
stays where it is, keeps its German programme name "KI für Alle" in quotation marks, and
is marked "(in German)". The link to the Wikipedia article 'Central tendency' loses the
word "englische": in the German it told the reader to expect English, which is now
pointless.

**Cross-references into chapters that are not translated yet.** I had to invent English
link texts for chapters other agents are still working on. What I used:

* `[Expected value and variance](expectation-variance.md)`, section `"Quantifying
  deviation"` (German `## Abweichung quantifizieren`) – matches the link text already used
  in `covariance.md`, but the section title is my guess at what that chapter's translator
  will call it. **Check once `expectation-variance.md` lands.**
* `[Exploratory analysis: examples](eda-examples.ipynb)` (German `Explorative Analyse:
  Beispiele`) – twice.
* `[Titanic EDA](titanic-eda-numpy.ipynb)`, `[Iris](iris.ipynb)`,
  `[Data cleaning](data-cleaning.ipynb)`, `[Linear regression](linear-regression.ipynb)`,
  `[Numpy](numpy.ipynb)` – all straightforward.
* `[clustering by k-means](kmeans.ipynb)`, `[Gaussian mixture models](expectation-maximization.ipynb)`,
  `[contaminated normal distribution](important-continuous-distributions.ipynb)` – the
  last one matches the phrasing already used in `continuous-distributions.md`.
* `[Covariance](covariance.md)` and `[Covariance and dependence](covariance.md)`, and the
  remark `*For data*` in it – verified against the translated `covariance.md`, which has
  that remark under exactly that name.

**Code.** Two invented German identifiers were translated: `daten` → `data` in the scatter
plot snippet and `winkel` → `angle` in the circle snippet, along with every comment. The
printed Numpy values are untouched, so nothing needs re-executing; these are fenced
snippets in a Markdown file, not notebook cells.

**Numbers.** All decimal commas became points, in prose and in maths, including the
worked example's twenty-odd values and the correlation coefficients in the Iris exercise.
The percentages in the Simpson tables keep the German spacing (`78 %`) because that is
what the table had and it is harmless; say the word if the edition wants `78%`.

## Style pass

Fable, 14 October 2026. 73 of the 145 blocks changed; the block count, the kind sequence,
every inline maths expression, both fenced code blocks and every link text are byte-identical
to the pre-pass file. `tools/sync.py align` and `tools/check_english.py` pass; the one
entry in `sync/check-ignore/descriptive-statistics.md.json` (the German MyST target in
block 42) is untouched.

### Kinds of change

* **Verb instead of nominalisation.** "is the computing of" → "means computing";
  "computing the variance forms a sum, or an integral, over squares" → "means summing, or
  integrating, over squares"; "How to do this … is shown by the chapter" → "The chapter …
  shows how to do this".
* **"One" and inverted existentials.** "one distinguishes … one says that" → passive and
  "a feature is said to be"; "To be distinguished from the sample is the population" →
  "Distinct from the sample is the population"; "To several of the measures … there belongs
  … a measure of dispersion" → "Several of the measures … come with a measure of dispersion
  of their own"; "to every measure of spread there belongs a measure of location" → "every
  measure of spread has a measure of location that belongs to it".
* **Calques replaced by the English idiom.** "give away the information" (*verschenken*) →
  "throw away"; "infinitely often differentiable" → "infinitely differentiable";
  "fall together" (*zusammenfallen*, of colour patches) → "merge"; "there are not simply
  kidney stones" → "there is no such thing as simply "kidney stones""; "hangs on" (*hängt
  an*) → "depends on", twice; "comes about like this" → "is drawn like this"; "what the most
  suitable means of communication is always depends" → "which means of communication is
  most suitable always depends".
* **Lists de-clipped.** The grammar-of-graphics layer list ("Data – which are to be
  visualised?" → "what is to be visualised?"; "Scales – scale the values? Nominal/ordinal?"
  → "should the values be scaled? Nominal or ordinal?"), the Python-tools list, the
  measures-of-spread list ("Range: largest value minus smallest value" → "the largest value
  minus the smallest") and the boxplot/histogram/map-plot descriptions took articles and
  finite verbs. The statistics-vs-ML correspondence list and the worked example were
  left terse: the terseness is the point there.
* **Sentence surgery.** The quartile definition (two parallel "is the value such that"
  sentences) folded into one; the Datasaurus Dozen sentence lost its "out of it … a series
  of … but that look"; the histogram definition's trailing participle ("obtained by summing
  …") became a dash clause; the "Careful: two formulas" paragraph lost "This state of
  affairs".
* **Connectives and adverbs.** "just as much" → "just as readily"; "exactly when" →
  "precisely when"; "where need be" → "where necessary"; "independently of the
  parameters" → "whatever the parameters"; "First: … Second:" → "First, … Second,".
* **One word changed for sense, checked against the German.** Block 80 had "a single
  *figure* over all the data can say the opposite", which in a section about figures reads
  as "a single plot". The German is *Eine Kennzahl über alle Daten*; it is now "a single
  summary measure over all the data", the chapter's own term for *Maßzahl/Kennzahl*.

### Noticed, deliberately not touched

* **"the cloud of points on the right"** (block 65). The figure is *above* this paragraph in
  the rendered page, not to its right. The German says *Punktwolke rechts* too, so it is the
  original's own layout remark, probably from the slides. Author's call.
* **"Dispersion, spread"** (block 27 heading) and "(see Dispersion)" in block 26: the
  heading is the only place the book uses *dispersion* as a label, and the cross-reference
  depends on it, so I left the word pair alone even though "spread" is the glossary's word.
* **"a week plus a day"** (block 51): literal and slightly odd, but it is the author's joke
  about eight values and I did not want to flatten it.
* **`f (x) = x`** in the ggplot2 stat list (block 126) is set in plain text with a stray
  space, not in maths. Cosmetic; it is like that in the German.
* **Violin plot, "drawn in outline"** – still the translator's hedge for *ausschnittsweise*
  (see *Decisions* above). Not a style matter; still wants the author's eye.
* **"This is also known as the Bessel correction"** (block 31): strictly, the Bessel
  correction is the $n-1$ denominator, not the existence of two formulas. The German
  (*Dieser Sachverhalt heißt auch Bessel-Korrektur*) has the same looseness; I only
  removed "state of affairs".
* **The 78% / 83% spacing** in the Simpson tables is already closed up, so the earlier
  translator's note about `78 %` is stale.
* **"cardinal scale"** stays, per the translator's *Decisions*; nothing in this pass changes
  the case for or against "metric".
