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

## Models, estimators and likelihood

First needed in `statistical-models.md`.

| German | English | Note |
|---|---|---|
| Approximations-Algorithmus | approximation algorithm |  |
| asymptotisch erwartungstreu | asymptotically unbiased |  |
| Aufruf (einer Web-Anwendung) | request | "gaps between two requests", "requests per unit of time" |
| Beobachtungswert | observed value | $L_x$ is the likelihood "for the observed value $x$" |
| bias, $\mathbb{B}_\theta(T)$ | bias | the German already uses the English word, lower case |
| Cramér-Rao-Ungleichung | Cramér–Rao inequality | en dash in the name, as with *Radon–Nikodym* |
| diskretes / stetiges Modell | discrete / continuous model |  |
| einparametriges Modell | one-parameter model |  |
| EM-Algorithmus | EM algorithm | link text into `expectation-maximization.ipynb` |
| Ereignisraum | event space | the set $\Sigma$ with a $\sigma$-algebra on it |
| Erwartungstreue | unbiasedness | the section heading; the glossary has only the adjective *erwartungstreu → unbiased* |
| Expectation Maximization Algorithmus | expectation maximization algorithm | the `-ize` stays: it is the algorithm's name and the chapter's title |
| Exponentialfamilie | exponential family |  |
| Fehlerbereich | margin of error | what a confidence interval adds to a point estimate |
| Fisher-Information | Fisher information | no hyphen in English |
| gemischtes Modell | mixture model | the k-means example; the glossary has *Mischverteilung → mixture distribution* for the distribution |
| gleichmäßig bester erwartungstreuer Schätzer | uniformly best unbiased estimator | see *Decisions* |
| Hypothesentest | hypothesis test | the glossary has *Hypothese*, not the test |
| kategorielle Variable | categorical variable | the German spells it *kategoriell* here, *kategorial* elsewhere; one English word |
| Kenngröße | characteristic quantity | the value $\tau(\theta)$ an estimator aims at – see *Decisions* |
| Kunstgriff | move | "the crucial move is in the last row" – "artifice" and "sleight of hand" both oversell it |
| Likelihood-Funktion | likelihood function | the glossary has the *estimator* and the *principle*, not the function |
| log-Likelihood | log-likelihood | hyphenated, lower case |
| Maximalstellen | the places where the maximum is attained | rendered as "attain their maxima in the same places" |
| Niveaumenge | level set | of a continuous function |
| parametrisches Modell | parametric model |  |
| Pasch / Keinpasch | doubles / no doubles | also inside maths: `\text{Pasch}` → `\text{doubles}`, `\text{Keinpasch}` → `\text{no doubles}` |
| Produktmodell | product model | $\mathcal{X}^N$, the $N$-fold repetition |
| Punktschätzer | point estimator | the German's own parenthetical second name |
| Server-Logfiles | server log files | three words in the English edition |
| Signifikanz | significance | the notion the tests chapter calls problematic |
| Standardmodell | standard model | discrete or continuous |
| Statistik (die Abbildung) | statistic | the countable noun, not the field; *Statistik* the field stays *statistics* |
| statistisches Modell | statistical model | the chapter's central object; the glossary had only *Modell-Auswahl* and *Modellverteilung* |
| Stichprobenraum, Stichprobenmenge | sample space | $\mathcal{X}$; collides with the glossary's *Ergebnisraum → sample space* ($\Omega$) – see *Decisions* |
| umgangssprachlich / formal (table header) | in everyday terms / formally | the map table before the definitions |
| verzerrt (biased) | biased | the German glosses itself with the English word; the doublet collapses |
| Wartezeit | waiting time | the exponential-distribution example |
| Zentroid | centroid | plural *centroids* |

## Hypothesis testing

First needed in `statistical-tests.md`.

| German | English | Note |
|---|---|---|
| $\chi^2$-Verteilung, Chi-Quadrat-Verteilung | $\chi^2$ distribution, chi-squared distribution | the spelled-out form only in the figure caption, as in the German |
| Befragte | respondents | also in the code's `print` strings and their output |
| beidseitiger / einseitiger Test | two-sided / one-sided test |  |
| Bereichsschätzer | set estimator | the general non-point estimator, heading *From set estimator to test* |
| Bootstrap | bootstrap | lower case in running English prose |
| Bundestagswahl | German federal election | *Bundestag* and *Bündnis Sahra Wagenknecht* / *BSW* stay as proper names |
| effektives Niveau | effective level |  |
| einfache Hypothesen | simple hypotheses |  |
| Entscheidungsregel | decision rule |  |
| erwartete Häufigkeit | expected frequency |  |
| Fehler erster / zweiter Art | type I error / type II error | the standard English names; "error of the first kind" reads as translated German |
| Formparameter | shape parameter | see *Decisions* |
| Fünf-Prozent-Frage | five-per-cent question | section heading; British "per cent" |
| gleichmäßig bester Test zum Niveau $\alpha$ | uniformly best test at level $\alpha$ | kept literal – see *Decisions* |
| Gütefunktion | power function | $G_\phi(\theta) = \mathbb{E}_\theta(\phi)$ – this really is what English calls the power function |
| Homoskedastizität, Varianzhomogenität | homoscedasticity, homogeneity of variance | British `-sc-`; the German's own gloss is kept because it explains the Greek |
| Intervallschätzer | interval estimator | the special case the chapter actually uses |
| Irrtumsniveau | error level | "confidence region for $\tau$ at error level $\alpha$"; distinct from *Signifikanzniveau* → significance level, already in the glossary |
| Kennzahl | summary measure | follows the glossary's *Maßzahl → summary measure*; "summary statistic" was avoided because the chapter also has *Statistik* in the technical sense |
| Konfidenzbereich | confidence region | the set-valued version; *Konfidenzintervall* stays the interval |
| Kontingenztabelle | contingency table | the glossary has *Kontingenztafel* under *Kreuztabelle*; same word, same translation |
| Lemma von Stein | Stein's lemma | genitive, as for *Satz von Bayes → Bayes' theorem* |
| Likelihood-Quotient | likelihood ratio | not "likelihood quotient" |
| Macht, Stärke | power | the German glosses itself, "Macht (oder Stärke, engl. power)"; the doublet collapses to the one English word, which the glossary already has for *Teststärke* |
| Neyman-Pearson-Test, -Lemma | Neyman–Pearson test, lemma | en dash in the name, as for *Radon–Nikodym* |
| nichtrandomisiert / randomisiert | non-randomised / randomised | house `-ise` spelling |
| Niveau (eines Tests) | level | "a test of level $\alpha$" |
| Nullhypothese / Alternative | null hypothesis / alternative | the glossary has the null hypothesis only |
| p-value hacking | p-value hacking | the German already uses the English |
| p-Wert | p-value |  |
| Pearson's Korrelation | Pearson correlation | the German's apostrophe-s is not English usage here |
| Prognoseintervall | prediction interval | the section heading; the same paragraph contrasts it with *Konfidenzintervall* → confidence interval, which is already in the glossary |
| Prozentpunkte | percentage points |  |
| Publikationsbias | publication bias |  |
| Punktschätzung, Punktschätzer | point estimate, point estimator |  |
| Quantiltransformation | quantile transformation |  |
| Residuen | residuals |  |
| Schwellwert | threshold |  |
| sehr signifikant / hochsignifikant | very significant / highly significant |  |
| Shapiro-Wilk | Shapiro–Wilk | en dash |
| Signifikanz, statistisch signifikant | significance, statistically significant |  |
| Standardfehler | standard error |  |
| Stichprobenfehler, Samplingfehler | sampling error | the German uses both words, English has one |
| Student t-Test | Student t-test | the section heading *The Student t-test* |
| Student t-Verteilung | Student t distribution | no apostrophe and no hyphen, mirroring the German's own *Student t-Verteilung* |
| Teststatistik | test statistic |  |
| Umfrageinstitut | (polling) institute |  |
| Verteilungsfreiheit | distribution-free | rendered adjectivally – see *Decisions* |
| Vorregistrierung (von Studien) | pre-registration |  |
| z-Statistik, t-Statistik | z-statistic, t-statistic |  |
| z-Test, Gauß-Test | z-test, Gauss test |  |
| z-Wert | z-value |  |
| Zufallsstichprobe | random sample |  |
| Zweitstimme | second vote (the party vote) | glossed once on first use; the German system needs the gloss for a reader outside Germany |

## Data protection law (GDPR and BDSG)

First needed in `data-protection.md`.

| German | English | Note |
|---|---|---|
| a.F. (alte Fassung) | in the version then in force | kept as `a.F.` so the citation can be looked up, with the gloss after it |
| Abhilfebefugnisse | corrective powers | Art. 58(2) |
| Airgap | air gap | two words in English |
| allgemeines Persönlichkeitsrecht | general right of personality | the standard rendering of the Art. 2(1) GG right |
| Angemessenheitsbeschluss | adequacy decision | Art. 45 |
| Anwendungsbereich | scope | Art. 2 |
| AOK | AOK, a statutory health insurer | likewise glossed |
| Aufsichtsbehörde, die Aufsicht | supervisory authority | the GDPR's term; "the supervisory authority" also where the German shortens to *die Aufsicht* |
| Auftragsverarbeitung | processing on a controller's behalf | the activity; see `Auftragsverarbeitungsvertrag` for the contract |
| Auftragsverarbeitungsvertrag (AVV) | data processing agreement (AVV) | Art. 28; the GDPR itself says only "contract or other legal act", so the industry term is used and the German abbreviation kept |
| Auskunft | access | Art. 15; the glossary's *Auskunftsrecht* → right of access |
| Berichtigung | rectification | Art. 16; not "correction" |
| Beschränkung oder Verbot einer Verarbeitung | limitation or ban on processing | Art. 58(2)(f) |
| Beschäftigtendatenschutz | employee data protection | the BDSG's remaining room under Art. 88 |
| besondere Kategorien personenbezogener Daten | special categories of personal data | Art. 9; "sensitive data" only as the colloquial gloss the German also gives |
| Betroffenenrechte, Rechte Betroffener | rights of the data subject | Chapter III |
| Bundesgerichtshof (BGH) | Federal Court of Justice | German name in brackets; the dashcam case |
| Bundesverfassungsgericht | Federal Constitutional Court | German name in brackets on first use |
| Dateisystem (DSGVO Art. 2) | filing system | **not** "file system" – this is the official English wording, and the German *Dateisystem* is a false friend here |
| Datenaltruismus | data altruism | DGA |
| Datenpanne | data breach | the colloquial German for *Verletzung des Schutzes personenbezogener Daten* |
| Datenschutz (chapter title) | Data protection | matches `myst.yml` |
| Datensparsamkeit | data parsimony | the pre-2018 BDSG principle, § 3a BDSG a.F.; quoted in German and glossed, since it is a term the GDPR dropped |
| Datenvermittlungsdienst | data intermediation service | DGA's official English |
| Datenübertragbarkeit | data portability | Art. 20 |
| Drittland, Drittlandübermittlung | third country, transfer to a third country | the GDPR's own English term |
| Durchführungsbeschluss | Implementing Decision | the official English name |
| Einschränkung der Verarbeitung | restriction of processing | Art. 18 |
| Erhebung (eine Welle) / Welle | wave | of a repeated survey; the glossary's *Erhebung* → data collection stays for the activity |
| Erwägungsgrund | recital | the official name for the GDPR's preamble numbers |
| EuGH | Court of Justice of the European Union | spelled out on first use, "Court of Justice" thereafter |
| Europäische Datenstrategie | European data strategy | the 2020 Commission communication |
| Geldbuße, Bußgeld | administrative fine, fine | Art. 83 |
| Gewinnspiel | prize draw | the AOK case |
| Grundprinzipien (Art. 5) | basic principles | the six principle names all follow the official English: lawfulness/fairness/transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality |
| grundsätzlich untersagt | prohibited in principle | *grundsätzlich* is not "fundamentally" here – the next clause says the prohibition is not absolute |
| Haftung | liability | Art. 82 |
| Hochrisiko-Anwendung | high-risk application |  |
| in Verkehr bringen | place on the market | AI Act product-regulation language |
| Kanzlei | law firm | CMS, who keep the Enforcement Tracker |
| KI-System | AI system | the AI Act's own English term |
| KI-Verordnung | AI Act | the German name in brackets; the English name is the one in use |
| Lagemaß (exercise) | measure of location | already in `TERMINOLOGY.md`; recorded here because the exercise is the only place this chapter uses a statistics term |
| Längsschnittbefragung, Längsschnittstudie | longitudinal survey, longitudinal study |  |
| Löschung | erasure | Art. 17; "right to be forgotten" as the quoted second name |
| Machtgefälle | imbalance of power | the Skellefteå consent case |
| materieller / immaterieller Schaden | material / non-material damage | the official English pair |
| Meldepflicht bei Datenpannen | notification of data breaches | Art. 33 |
| meldepflichtig | notifiable | of a breach |
| Mitteilung der Kommission | Commission communication |  |
| Mitteilungspflicht | notification obligation | Art. 19 |
| Personalauswahl | personnel selection |  |
| Rechenschaftspflicht | accountability | Art. 5(2) |
| Recht auf informationelle Selbstbestimmung | right to informational self-determination | the *Volkszählungsurteil* term |
| Rechtsbehelf | remedy | "no effective remedy" in *Schrems I/II* |
| Rechtsgrundlage fehlt / fehlende Rechtsgrundlage | missing legal basis |  |
| Richtigkeit | accuracy | Art. 5(1)(d); not "correctness" |
| Richtlinie 95/46/EG | Directive 95/46/EC | EG → EC in the official English citation |
| Rundmail | circular email |  |
| Schadenersatz | compensation | Art. 82 |
| Schufa | Schufa, the German credit agency | glossed, since the name means nothing outside Germany |
| Selbstgenerierter Code | self-generated code | the longitudinal-study technique |
| Selbstregulierung | self-regulation |  |
| Speicherbegrenzung | storage limitation | Art. 5(1)(e) |
| Strafverfolgung | law enforcement |  |
| Verarbeitung nach Treu und Glauben | fairness | the official English of Art. 5(1)(a); the German phrase is quoted and glossed "in good faith" |
| verbotene Praktiken | prohibited practices |  |
| Verhaltensregeln | codes of conduct | Art. 40 |
| Verordnung (EU) 2024/1689 | Regulation (EU) 2024/1689 | likewise for all five regulations in the last section |
| Verwarnung / Warnung | reprimand / warning | two different Art. 58(2) powers, and English keeps them apart |
| Volkszählungsurteil | census judgment | German name in brackets, italicised |
| Vorsatz oder Fahrlässigkeit | intentional or negligent | Art. 83(2)(b) |
| Weiterverwendung geschützter Daten der öffentlichen Hand | re-use of protected public sector data | DGA |
| Widerspruch | objection | Art. 21; not "contradiction", not "appeal" |
| Worum es ging (table header) | What it was about |  |
| Zettelkasten | card index | the non-automated example of a filing system |
| Zugangsdaten | login details | the phishing example |
| Zumessung | fixing the amount | of a fine |

## Numpy and arrays

First needed in `numpy.ipynb`.

| German | English | Note |
|---|---|---|
| Achse | axis | plural *axes*; `axis=` stays as the keyword |
| Array-orientierte Programmierung | array-oriented programming | the chapter's own framing; links to the English Wikipedia article, which was already the target |
| automatische Ableitung | automatic differentiation | not "automatic derivative" |
| Datentyp | data type | `dtype` stays `dtype` |
| Einheitsmatrix | identity matrix | code comment in cells 13 and 15 |
| Einsteigerkapitel | beginners' chapter | of the Numpy documentation |
| elementweise | element by element, element-wise | adverbially "element by element", attributively "element-wise" |
| Fallunterscheidung | case distinction |  |
| Fancy Indexing | fancy indexing | the Numpy term of art, lower case in English |
| Gerätezuordnung | device assignment | the PyTorch tensor's CPU/GPU placement |
| gezinkter Würfel | loaded die | code comment, cell 33; `Würfe` → *rolls* |
| Hauptspeicher / Grafikkarte | main memory / graphics card |  |
| Infix-Operator | infix operator | the `@` operator |
| Maske, maskieren | mask | `## Masken und Fancy Indexing` → `## Masks and fancy indexing`; cross-referenced from block c1.4 |
| Matrizenkalkül | matrix algebra | see *Decisions* – not "matrix calculus" |
| Matrizenmultiplikation / Matrixmultiplikation | matrix multiplication / matrix product | the German uses both spellings; `np.matmul`'s result is the *matrix product* |
| Nachschlagewerk | reference work |  |
| normieren (einen Vektor) | to normalise | here: dividing by the sum so that $p \in \Delta_6$ |
| relative Häufigkeiten | relative frequencies |  |
| Sichtweise (auf den Speicher) | view | the Numpy word; the German says *View* in the same cell |
| Skript (das Vorlesungsskript) | these notes | matches `intro-python.ipynb`, which already uses this |
| Speicherbereich | region of memory | `np.may_share_memory` |
| Spickzettel | cheat sheet |  |
| Stand September 2026 | as of September 2026 | the date the function list was harvested |
| Vektorisierung, vektorisieren | vectorisation, to vectorise | house `-ise` spelling; the German glosses *Array-orientierte Programmierung* with it |
| verzweigungsfrei schreiben | to write branch-free code | the chapter's bolded working rule; `Verzweigung` → *branch* |
| Was muss man kennen? | What do you need to know? | section heading, block c35.0 |
| Zeilenvektor / Spaltenvektor | row vector / column vector |  |

## Pandas and tabular data

First needed in `pandas.ipynb`.

| German | English | Note |
|---|---|---|
| Abfragesprache | query language | "the standard query language for relational database systems" |
| Art der Daten | kind of data | table header |
| Attribut | attribute | the columns of a relation |
| Attributschreibweise | attribute notation | `df.sepal_width` as against `df["sepal_width"]` |
| Befehl (SQL) | command | the table of `SELECT`, `INSERT INTO`, … |
| Datenbankschema | database schema | the Definition admonition |
| dünn besetzte Spalte | sparse column |  |
| Erster Blick auf einen Datensatz | A first look at a dataset | section heading |
| Full Outer Join | full outer join | likewise |
| Ganzzahl | integer |  |
| Gesamtmittelwert, Gesamtmittel | overall mean | not "total mean" – it is the mean over all observations |
| gewichtetes Mittel | weighted mean | the glossary has *arithmetisches Mittel → arithmetic mean*; this is the weighted version |
| Gruppengröße | group size | the weights |
| Gruppenmittel, Gruppenmittelwert | group mean |  |
| Handarbeit | handwork | "still handwork with Numpy in the Titanic notebook" |
| Inner Join | inner join | lower case in English running prose; bold kept |
| Intervall | interval |  |
| kategoriale Werte | categorical values |  |
| Left / Right Outer Join | left / right outer join | likewise |
| Primärschlüssel / Fremdschlüssel | primary key / foreign key |  |
| record array | record array | stays, it is the Numpy term |
| Reihenfolge (der Zeilen) | order | "the row order after a `merge` is not guaranteed" |
| Relation | relation |  |
| Relationsschema | relation schema | plural *relation schemas*, not *schemata* |
| Schlüssel | key |  |
| Spaltenname | column name |  |
| Suchschlüssel | search key | the `CREATE / DROP INDEX` row |
| Tupel / Entität | tuple / entity | the rows of a relation |
| Wahrheitswert | truth value | as in `intro-python.ipynb` |
| Wertebereich (relational) | domain | **collides** with the existing glossary row *Wertebereich → range, set of values* (that one is 𝒳, the range of a random variable). The relational sense is *domain*, and the German already glossed itself "(domain)" |
| Zeichenkette | string |  |
| Zeilenindex | row index | the thing `index=False` keeps out of the CSV |
| Zeitpunkt / Zeitdauer / Zeitraum | point in time / duration / period | three German words that English keeps apart as `Timestamp` / `Timedelta` / `Period` |
| Zeitstempel | timestamp |  |

## Probability in code

First needed in `programming-stochastics.ipynb`.

| German | English | Note |
|---|---|---|
| Ausblick (as an `##` heading) | Looking ahead | `TRANSLATION.md` §5 fixes this for admonition titles; `expectation-variance.md` already uses it for a heading too |
| Größere Stichproben | Larger samples | section heading |
| irgendwie geartet | some … or other | "some probability measure or other is defined on $\Omega'$" |
| Kürzel | shorthand | `randint` is a *Kürzel* for `randrange` |
| paarweise verschieden | pairwise distinct | the glossary has *paarweise unabhängig* → pairwise independent |
| relative Häufigkeit | relative frequency | `descriptive-statistics.md` already has *Häufigkeitsverteilung* → frequency distribution, but not this one |
| Schnittstelle | interface | of the `random` module |
| Urne | urn | the standard image, kept |
| Verwendete Python-Konstrukte | Python constructs used | the link list under the H1 |
| Würfelaugen | numbers of pips | the plural of the glossary's *Augenzahl* → number of pips; used in a `print` label |
| Würfelwurf | throw of a die | matches `intro-stochastics.md` ("A single throw of the die"); not "roll", not "dice throw" |
| Zufall importieren | Importing randomness | section heading; follows the `Zufall` → *randomness* row from `random-variables-distributions.md` |
| Zufallsexperiment | random experiment | first cell; not previously in the glossary |

## Two German words, one English word

Recorded because a translator will otherwise think one of them is wrong:

* *Ergebnisraum* (Ω, the space of outcomes) and *Stichprobenraum* (𝒳, the space a
  measurement takes values in) are both the **sample space** in English. The German keeps
  them apart with two words; English does not, and `statistical-models.md` says so in the
  text where it matters.

* *mittlere absolute / quadratische Abweichung* are the **mean absolute / squared error**,
  not "deviation", because the book's own code calls them `mae`, `mse` and `rmse`.

* *gleichmäßig bester Test* and *gleichmäßig bester erwartungstreuer Schätzer* stay literal
  (**uniformly best test**, **uniformly best unbiased estimator**) rather than becoming UMP
  and UMVUE. The German is un-abbreviated and spells out what "best" means; handing the
  reader the acronym is material the original does not have. Both chapters agree; if that
  is ever revisited, they move together.

