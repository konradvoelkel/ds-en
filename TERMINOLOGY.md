# Terminology

Binding for every chapter. If a term is missing and you had to think about it, add it in
the same commit you used it in. Grown chapter by chapter, so entries carry the chapter
that first needed them.

## The umbrella term

**Stochastik** → **stochastics**. Clunky in English, but it is the word, and the book needs
a name for the field that contains both probability theory and statistics – the opening
figure of `intro-stochastics.md` is precisely about that containment. So: "stochastics" for
the field, "probability theory" for *Wahrscheinlichkeitstheorie*, "statistics" for
*Statistik*, and "probability" for *Wahrscheinlichkeit* the quantity. `Stochastik
programmieren` → "programming with stochastics".

## Probability and statistics

| German | English | Note |
|---|---|---|
| Wahrscheinlichkeitsraum | probability space | |
| Ergebnisraum, Grundraum | sample space | Ω |
| Ereignis | event | |
| Elementarereignis | elementary event | |
| Zufallsvariable | random variable | X; realisation x |
| Realisierung | realisation | |
| Wertebereich | range, set of values | 𝒳 |
| Verteilung | distribution | |
| Dichte | density | |
| Wahrscheinlichkeitsmassefunktion | probability mass function | pmf |
| Verteilungsfunktion | cumulative distribution function | cdf |
| Erwartungswert | expected value | "expectation" where the German is short too |
| Varianz | variance | |
| Streuung | spread | the everyday word; "dispersion" only in a technical list |
| Standardabweichung | standard deviation | |
| Kovarianz | covariance | |
| Korrelation | correlation | |
| Unabhängigkeit | independence | |
| bedingte Wahrscheinlichkeit | conditional probability | |
| Gesetz der großen Zahlen | law of large numbers | |
| Zentraler Grenzwertsatz | central limit theorem | |
| Gleichverteilung | uniform distribution | discrete or continuous, say which |
| Normalverteilung | normal distribution | "Gaussian" where the German says Gaußsch |
| Binomialverteilung | binomial distribution | |
| Stetige Verteilung | continuous distribution | |
| Diskrete Verteilung | discrete distribution | |
| Faltung | convolution | |
| Momente | moments | |
| Quantil | quantile | |
| Simplex, Wahrscheinlichkeitssimplex | probability simplex | Δ_n |

## Statistics and inference

| German | English | Note |
|---|---|---|
| Stichprobe | sample | |
| Stichprobenumfang | sample size | N or n |
| Schätzer | estimator | |
| Schätzung | estimate | the value, not the method |
| erwartungstreu | unbiased | |
| konsistent | consistent | |
| Güte (eines Modells) | quality, goodness | "goodness of fit" only where that is meant |
| Hypothese, Nullhypothese | hypothesis, null hypothesis | |
| Signifikanzniveau | significance level | |
| Teststärke | power | |
| Konfidenzintervall | confidence interval | |
| Freiheitsgrade | degrees of freedom | |
| Likelihood | likelihood | stays |
| Maximum-Likelihood-Schätzer | maximum likelihood estimator | MLE |
| relative Entropie | relative entropy | Kullback–Leibler divergence where the German says so |
| Überanpassung | overfitting | |

## Data and machine learning

| German | English | Note |
|---|---|---|
| Daten putzen | data cleaning | the chapter title; "cleaning data" in running prose |
| Datensatz | dataset | |
| Teildatensatz | subset of the data | |
| Merkmal | feature | |
| Ausprägung | value, level | of a categorical feature |
| Beobachtung, Instanz | observation, instance | keep whichever the German uses |
| Zielgröße | target variable | |
| Erhebung | data collection | |
| Rohdaten | raw data | |
| Ausschnitt | section, slice (of reality) | in the ds-process figures: "section" |
| explorative Datenanalyse | exploratory data analysis | EDA |
| deskriptive Statistik | descriptive statistics | |
| Dimensionsreduktion | dimensionality reduction | |
| Hauptkomponentenanalyse | principal component analysis | PCA |
| Regressionsanalyse | regression analysis | |
| Kernel-Methoden | kernel methods | |
| Modell-Auswahl | model selection | |
| Kreuzvalidierung | cross-validation | |
| Klassifikation | classification | |
| Vorhersage | prediction | |
| Lernverfahren | learning algorithm | |
| Verwirrungsmatrix, Konfusionsmatrix | confusion matrix | |
| Trainingsdaten, Testdaten | training data, test data | |

## Data protection (the `data-protection.md` chapter)

The GDPR has an official English text; its vocabulary is used, with the German term in
brackets on first use where the reader may meet it in a German context.

| German | English |
|---|---|
| Datenschutz-Grundverordnung (DSGVO) | General Data Protection Regulation (GDPR) |
| Bundesdatenschutzgesetz (BDSG) | Federal Data Protection Act (BDSG) — stays BDSG |
| personenbezogene Daten | personal data |
| betroffene Person | data subject |
| Verantwortlicher | controller |
| Auftragsverarbeiter | processor |
| Einwilligung | consent |
| Verarbeitung | processing |
| Pseudonymisierung / Anonymisierung | pseudonymisation / anonymisation |
| Zweckbindung | purpose limitation |
| Datenminimierung | data minimisation |
| Rechtsgrundlage | legal basis |
| berechtigtes Interesse | legitimate interest |
| Auskunftsrecht | right of access |
| Recht auf Löschung | right to erasure |

## Botany, because of the Iris dataset

| German | English |
|---|---|
| Kelchblatt | sepal |
| Blütenblatt | petal |
| Länge / Breite | length / width |

## Notation (unchanged from the German edition)

X random variable, x realisation, 𝒳 range, Ω probability space, D domain of a density,
Δ_n probability simplex, k number of clusters (k-means) and number of regressors
(regression, said explicitly), d dimension, N or n sample size, t EM iteration index,
Z_N standardised sum. "Standard deviation" without qualification means the n-version
(the numpy default); pandas and scipy use n−1.


<!-- Everything below was proposed by the chapter translators and merged after each wave.
     Sections are named for the chapter that first needed the terms; the glossary is
     binding across the whole book regardless of where a term first appeared. -->

## Measure, integration and continuous distributions

First needed in `continuous-distributions.md`.

| German | English | Note |
|---|---|---|
| $k$-tes Moment | $k$-th moment | glossary has "Momente → moments" only |
| abgeschlossen (Menge) | closed | topological sense, defined in the chapter |
| Abschluss (einer Menge) | closure |  |
| Dichtefunktion (chapter heading *Dichtefunktionen*) | density function | heading rendered "Density functions"; running prose stays with "density" per the glossary |
| Dirac-Verteilung | Dirac distribution | `intro-stochastics.md` already has "Dirac measure" for *Dirac-Maß*; both occur |
| Distributionen (Funktionalanalysis) | distributions / generalised functions | see Decisions – collides with *Verteilung* in English |
| einpunktige Menge | one-point set |  |
| Hauptsatz der Differential- und Integralrechnung | fundamental theorem of calculus |  |
| Häufungspunkt | accumulation point | "limit point" is equally standard; picked one and used it once |
| Knobelaufgabe | puzzle | the chapter's aside in the `\mathbb{Q} \cap [0,1]` example |
| kontaminierte Normalverteilung | contaminated normal distribution | cross-reference to `important-continuous-distributions.ipynb` |
| Lebesgue-Maß | Lebesgue measure |  |
| Mischverteilung | mixture distribution |  |
| Nullmenge | null set | the chapter's Remark defines it; `covariance.md` also uses the word and will need the same choice |
| Riemann-integrierbar | Riemann integrable |  |
| Stammfunktion | antiderivative |  |
| Teilintervall | subinterval |  |
| Transformationsformel (the `\mathbb{E}(g(X))` theorem) | transformation formula | admonition title "Theorem (transformation formula)"; see Decisions |
| Transformationssatz für Integrale | change-of-variables theorem for integrals | the thing the proof would appeal to |
| Träger (einer Verteilung / Zufallsvariable) | support | `\operatorname{supp}(X)`; the chapter's opening definition |
| Wahrscheinlichkeitsdichtefunktion | probability density function | pdf; glossary has only "Dichte → density" |
| überabzählbar / abzählbar | uncountable / countable |  |

## Random variables and distributions

First needed in `random-variables-distributions.md`.

| German | English | Note |
|---|---|---|
| Augenzahl | number of pips | matches `intro-stochastics.md` |
| Bereinigung (von Rohdaten) | cleaning | the noun; the chapter title stays *Data cleaning* per the glossary |
| Bernoulli-Verteilung zum Parameter $\pi$ | Bernoulli distribution with parameter $\pi$ | not "to the parameter" |
| Eckpunkt / Ecke (eines Simplex) | vertex | plural *vertices* |
| Erfolg / Misserfolg | success / failure | in the coin-toss estimate |
| Erfolgswahrscheinlichkeit | success probability |  |
| Erwartungswert und Varianz | Expected value and variance |  |
| Formalismus der Stochastik | The formalism of stochastics |  |
| gefülltes Dreieck / Tetraeder | filled triangle / tetrahedron |  |
| German link text | English used here |  |
| Güte des Modells | quality of the model | the glossary's `Güte` row already covers it; not "goodness of fit" here |
| induziertes Wahrscheinlichkeitsmaß | induced probability measure | section heading; `induzierte pmf` → *induced pmf* |
| kategoriale Verteilung | categorical distribution |  |
| Merkmale / Features | features | the German glosses *Merkmale* with the English loanword *Features*; in English the gloss collapses to one word |
| Numpy, Abschnitt *Wahrscheinlichkeitsvektoren* | Numpy, section *Probability vectors* |  |
| Parität | parity |  |
| Population | population | the German uses the Latinate word too |
| Prior | prior | stays, lower case in English running prose |
| Pseudozufall | pseudo-randomness | hyphenated; `Seed` stays *seed* |
| Rechenvorschrift | rule for calculating |  |
| Relative Entropie | Relative entropy |  |
| Startwert (eines Generators) | starting value | with *seed* given as the technical name right after |
| Statistische Modelle und Schätzer | Statistical models and estimators |  |
| Statistische Tests | Statistical tests |  |
| Stochastik programmieren | Programming with stochastics (as in `intro-stochastics.md`) |  |
| Strecke (geometrisch) | line segment | $\Delta_2$; "segment" alone on repeat mentions |
| synthetische Daten | synthetic data | plural verb: "synthetic data are" |
| Urbild | preimage | as in `intro-stochastics.md` |
| Verkettung (von Abbildungen) | composition | "composing maps yields new random variables" for *Verketten liefert neue Zufallsvariablen* |
| Verteilung der Daten | distribution of the data | the book's own term, kept literal; *empirische Verteilung* → *empirical distribution* |
| Wahrscheinlichkeitsvektor | probability vector | section heading; `Bitmaske` → *bitmask* |
| Weltausschnitt | section of the world | follows the existing `Ausschnitt` → *section* row; `Weltzustand` → *world state* |
| Weltzustand | world state | the elements of $\Omega$ in the die example |
| Wichtigste diskrete Verteilungen | The most important discrete distributions |  |
| Zeichenvorrat | character set |  |
| Zufall | randomness | the chapter's section heading is *Wo kommt der Zufall her?* → *Where does the randomness come from?*; "chance" reads too colloquial once the section argues that randomness is a modelling decision |
| Zähldichte | discrete density | see *Decisions* below – I did not keep the German word |

## Expectation, deviation and information

First needed in `expectation-variance.md`.

| German | English | Note |
|---|---|---|
| $P$-fast sicher | $P$-almost surely |  |
| Abweichung | deviation | the chapter's running word; "error" only inside the names `mae`/`mse`/`rmse` |
| Basiswechselformel | change-of-base formula |  |
| binärer Logarithmus | binary logarithm |  |
| Binärstelle / Dezimalstelle | binary digit / decimal digit |  |
| bit / nat | bit / nat | plural "bits", "nats" in running prose; unit names stay lowercase |
| dekadischer Logarithmus | common logarithm | base 10; "decadic" is not English |
| Einschub | interlude | section heading `### Interlude: the logarithm` |
| Einzelverteilung | individual distribution | the marginals, but the German avoids "Randverteilung", so I avoided "marginal" |
| Exkurs | digression | matches `intro-stochastics.md` |
| idealisiertes Sample | idealised sample | the chapter's own coinage, bold on first use |
| Indikatorfunktion | indicator function |  |
| Informationsgehalt | information content |  |
| Kreuzentropie | cross-entropy |  |
| Lagemaße zentraler Tendenz | measures of central tendency | section heading |
| Makrozustand / Mikrozustand | macrostate / microstate |  |
| Markov-Ungleichung | Markov's inequality |  |
| Mini-Batch | mini-batch | stays |
| Mittelwert-Abweichungs-Zufallsvariable | mean-deviation random variable | $\overline{X_n^\ast}$ |
| normiertes Sample | normalised sample | mean $0$, sample standard deviation $1$ |
| paarweise unabhängig | pairwise independent |  |
| Sample-Standardabweichung | sample standard deviation | written `rmse` / $\sigma(v)$ in the text |
| Selbstinformation | self-information |  |
| St.-Petersburg-Paradoxon | St Petersburg paradox | British style, no full stops |
| starkes / schwaches Gesetz der großen Zahlen | strong / weak law of large numbers |  |
| Stichprobenmittel | sample mean |  |
| stochastische Konvergenz | convergence in probability | the standard English name; "stochastic convergence" would be a Germanism |
| stochastischer Gradientenabstieg | stochastic gradient descent |  |
| Transinformation, gemeinsame Information | transinformation, mutual information | English really only has "mutual information"; I kept both names because the German offers two |
| Trennwand | partition | the physical wall in the gas figures, not a set partition |
| Tschebyscheff-Ungleichung | Chebyshev's inequality | transliteration changes; the German spelling is not kept |
| Verschiebungssatz | shift theorem | $\mathbb{E}(X^2)-(\mathbb{E}X)^2$; see "Decisions and doubts" |
| zentrales Moment | central moment |  |
| zentriertes Sample / zentrierte Zufallsvariable | centred sample / centred random variable |  |
| Ziehen mit/ohne Zurücklegen | drawing with/without replacement |  |
| zweiter Hauptsatz der Thermodynamik | second law of thermodynamics |  |
| Zählfehler | counting error | the loss that counts every deviation equally (0–1 loss); the mode minimises it |

## Dependence, conditioning and the multivariate world

First needed in `covariance.md`.

| German | English | Note |
|---|---|---|
| antikorreliert | anticorrelated | unhyphenated |
| Basisrate | base rate |  |
| Basisratenfehler | base rate fallacy | the standard English name; literally it is an "error" |
| Bayessches Updaten | Bayesian updating |  |
| bilinear | bilinear |  |
| bivariate Normalverteilung | bivariate normal distribution |  |
| datenerzeugende Verteilung | data-generating distribution |  |
| Definitionsbereich (einer Zufallsvariablen) | domain | not "domain of definition" |
| Diagonalabbildung | diagonal map |  |
| empirische Kovarianz | empirical covariance | and *empirischer Korrelationskoeffizient* → empirical correlation coefficient |
| Evidenz | evidence | also inside maths: `\text{Evidenz}` → `\text{Evidence}` |
| Falsch-Positiv-Rate | false positive rate |  |
| Fassung (eines Satzes) | version | "Bayes' theorem, version 2/3/4" |
| fast sicher | almost surely | "almost surely constant", "almost surely $0$" |
| fast überall | almost everywhere |  |
| gemeinsam normalverteilt | jointly normally distributed |  |
| gemeinsame Dichte / gemeinsame pmf | joint density / joint pmf |  |
| gemeinsame Verteilung | joint distribution | the chapter's first section heading |
| Höhenlinie | contour line |  |
| Koordinatenprojektion | coordinate projection | $\pi_i$ |
| Korrelationskoeffizient (Pearsonscher) | (Pearson) correlation coefficient | $\rho$ for random variables, $r$ for data |
| Maximum-Likelihood-Prinzip | maximum likelihood principle | glossary has the *estimator*, not the principle |
| Modellverteilung | model distribution |  |
| positiv (semi)definit | positive (semi)definite |  |
| positiv / negativ korreliert | positively / negatively correlated |  |
| Posterior, a posteriori Wahrscheinlichkeit | posterior, a posteriori probability |  |
| Prior, a priori Wahrscheinlichkeit | prior, a priori probability |  |
| Produktregel | product rule | $p_{X,Y} = p_{Y\mid X}\,p_X$ |
| Promille | one in a thousand | see Decisions |
| Punktwolke | cloud of points |  |
| Randhistogramm | marginal histogram | figure caption |
| Randverteilung, Marginalverteilung | marginal distribution, margin | two German words, one English one – see Decisions |
| Rechenregeln | rules of calculation | matches `intro-stochastics.md`, which already uses this for $P$ |
| Satz von Bayes | Bayes' theorem | see Decisions on the admonition |
| Satz von der totalen Wahrscheinlichkeit | law of total probability | not "theorem of total probability" |
| Sensitivität | sensitivity | glossed as the classifier's recall |
| Simpson-Paradoxon | Simpson's paradox | link text into `descriptive-statistics.md` |
| Skalarprodukt | inner product | see Decisions |
| skalenabhängig | scale-dependent | rendered in prose as "it depends on the scale" |
| Spezies (Iris) | species |  |
| Streudiagramm, Scatterplot | scatter plot | the German uses both words; English has one |
| Summenregel | sum rule | summing out the nuisance variable |
| unkorreliert | uncorrelated |  |
| Zerlegung (in disjunkte Ereignisse) | decomposition |  |
| Zusammenhang (statistischer) | relationship | not "connection", not "association" |

## Entropy and information theory

First needed in `relative-entropy.md`.

| German | English | Note |
|---|---|---|
| Basiswechsel | change of base |  |
| bedingte Entropie | conditional entropy |  |
| Bezugsmaß | reference measure |  |
| differentielle Entropie | differential entropy |  |
| Entropie | entropy |  |
| Entropie-Beitrag | entropy contribution | the $-p\log p$ term |
| Entropischer Satz von Bayes | entropic Bayes' theorem |  |
| Funktionalgleichung | functional equation |  |
| gemeinsame Information, Transinformation | mutual information | the German glosses itself with "englisch *mutual information*"; see *Decisions* |
| Information, Selbstinformation | surprisal | the pointwise $I(x) = -\log P(\{x\})$; "self-information" is the other standard name. See *Decisions* – `expectation-variance.md` defines it and has to agree |
| invariantes Maß | invariant measure | Jaynes's $m$ |
| KL-Divergenz | KL divergence | no hyphen in English (`KL divergence to the labels`) |
| Klassenbezeichnung | class name | the labels whose permutation mutual information ignores |
| Klassenzugehörigkeit | class membership | in the clustering passage |
| konkav, streng konkav | concave, strictly concave |  |
| Konvexkombination | convex combination |  |
| Loss-Funktion | loss function | the German keeps the English word; so do we |
| Mittelwertsatz | mean value theorem |  |
| monoton wachsend / fallend | monotonically increasing / decreasing |  |
| Produktverteilung | product distribution | $P_X \times P_Y$ |
| Radon-Nikodym-Ableitung | Radon–Nikodym derivative | en dash in the name |
| Riemann-Summe | Riemann sum |  |
| Shannon-Entropie | Shannon entropy | no hyphen in English |
| stetige Entropie | continuous entropy | the section heading |
| streng monoton | strictly monotonic |  |
| Ungleichungskette | chain of inequalities |  |
| Verbundentropie | joint entropy | the section heading |
| vollständig additiv | completely additive | the $l(ab) = l(a)+l(b)$ condition |

## Descriptive statistics, data and visualisation

First needed in `descriptive-statistics.md`.

| German | English | Note |
|---|---|---|
| Ampel-Kodierung | traffic-light coding |  |
| arithmetisches Mittel | arithmetic mean |  |
| Balkendiagramm | bar chart |  |
| Beamer | beamer | kept: "projector" loses the German-campus flavour, and the sentence already says "projected" |
| Begriffskorrespondenz | corresponding terms |  |
| Bereichsmitte (Mid-range) | mid-range |  |
| Bessel-Korrektur | Bessel correction |  |
| binsize | bin size | two words in the English edition |
| Boxplot, Box-and-Whiskers-plot | boxplot, box-and-whiskers plot | one word for boxplot, as in the German |
| Buntheit | colourfulness |  |
| Data Mining | data mining | lower case in running English prose |
| deskriptive / beschreibende Statistik | descriptive statistics | the German doublet collapses, see *Decisions* |
| Deuteranopie / Protanopie / Tritanopie | deuteranopia / protanopia / tritanopia |  |
| Dichromasie | dichromacy |  |
| Dichteplot | density plot |  |
| Dichteschätzung | density estimation |  |
| Dummy-Variable | dummy variable |  |
| Durchgerechnetes Beispiel | a worked example | the heading |
| Eimergröße (bucket size) | bucket size |  |
| Epoche | epoch |  |
| Exzess | excess kurtosis | the German *Exzess* alone is a false friend |
| Facette, Facettenspezifikation | facet, facet specification |  |
| faktorielle Variable | factor variable |  |
| Farbpalette | colour palette |  |
| Farbsehschwäche | colour vision deficiency |  |
| Farbskala | colour scale |  |
| Fehlerfunktion (Verlustfunktion) | error function (loss function) | the doublet survives because the next entry is "loss" |
| Fitten | fitting |  |
| Form | shape |  |
| Generalisierung | generalisation |  |
| geometrisches Mittel | geometric mean |  |
| gestapelte Balken | stacked bar chart |  |
| Gewichte | weights |  |
| Glättung | smoothing |  |
| Grammatik der Grafiken | grammar of graphics |  |
| Grundgesamtheit | population | *Population* in the German is already the loan word |
| Helligkeit (einer Farbe) | lightness | not "brightness"; it is the perceptual axis |
| Häufigkeitsverteilung | frequency distribution |  |
| inferentielle / schließende Statistik | inferential statistics | likewise |
| Integer-/Ordinal-Encoding | integer / ordinal encoding |  |
| Interquartilsabstand | interquartile range | IQR |
| Intervallskala | interval scale | the table row is just "interval" |
| Kardinalskala | cardinal scale | see *Decisions* – English normally says "interval or ratio", but the book needs the umbrella |
| Kartendarstellung | map plot |  |
| Klasse (im Histogramm) | class, bin |  |
| Klassenbildung (clustering) | clustering | the German gloss disappears |
| Klassengröße | class width | not "class size" – it is the width of the interval |
| Kodierung kategorialer Merkmale | encoding categorical features |  |
| Konfusionsmatrix | confusion matrix | already in TERMINOLOGY |
| Kreuztabelle, Kontingenztafel | cross-tabulation (contingency table) |  |
| Lagemaß, Lageparameter | measure of location |  |
| latente Variable | latent variable |  |
| laufende Nummer | serial number |  |
| Likert-Skala | Likert scale |  |
| Linienplot | line plot |  |
| Matrikelnummer | student number |  |
| Maßzahl | summary measure | "summary statistic" where the German says *summarische Statistik* |
| Mischung, Mischverteilung | mixture, mixture distribution |  |
| mittlere absolute Abweichung | mean absolute error |  |
| mittlere quadratische Abweichung | mean squared error |  |
| Modus | mode |  |
| Mohs-Härte | Mohs hardness |  |
| nicht-Modus-Anteil | non-modal proportion |  |
| nominal-/ordinal-/kardinalskaliert | on a nominal / ordinal / cardinal scale | "nominally scaled" reads as translated German; prefer "on a … scale" |
| Nominalskala | nominal scale |  |
| Normalsicht | normal colour vision | not "normal sight" – it is about colour only |
| One-Hot-Encoding | one-hot encoding |  |
| Ordinalskala | ordinal scale |  |
| Perzentil | percentile |  |
| Positionsbestimmung | position adjustment | the ggplot2 term is *position adjustment* |
| Postleitzahl | postcode | British spelling, per TRANSLATION.md section 6 |
| Probe | check | as in "check: …" at the end of the worked example |
| Quartil, unteres/oberes Quartil | quartile, lower/upper quartile |  |
| rechtsschief | skewed to the right |  |
| Scatterplot | scatter plot | two words, matching `covariance.md` |
| Schicht (Layer) | layer |  |
| Schiefe | skewness |  |
| Schulnote | school grade |  |
| Signal-to-Noise-Ratio | signal-to-noise ratio |  |
| Skalenart | scale type |  |
| Skalenniveau | level of measurement | the Stevens term; "scale type" where the German says *Skalenart* |
| Spannweite | range | note the collision: *Interquartilsabstand* is also a "range" in English |
| Stichprobenstandardabweichung | sample standard deviation |  |
| Stichprobenumfang / Umfang | sample size |  |
| Stichprobenvarianz | sample variance |  |
| Streuungsmaß, Streumaß | measure of spread | "measure of dispersion" only where the German says *Dispersionsmaß* |
| Studiengang | degree programme |  |
| Störvariable, Confounder | confounder | the German gloss *(Störvariable)* disappears |
| summarische (zusammenfassende) Statistik | summary statistics |  |
| Säulendiagramm / Column chart | column chart | the German already uses the English |
| Testdatensatz-Performance | performance on the test set |  |
| Tortendiagramm | pie chart |  |
| unimodal / bimodal / multimodal | unimodal / bimodal / multimodal |  |
| Variationskoeffizient | coefficient of variation |  |
| Variationsverhältnis | variation ratio |  |
| Verhältnisskala | ratio scale | the table row is just "ratio" |
| Violinenplot | violin plot |  |
| Visualisierung | visualisation | house spelling |
| Wölbung | kurtosis |  |
| zentrale Tendenz | central tendency |  |
| Ästhetik, ästhetische Zuordnung | aesthetic, aesthetic mapping |  |

