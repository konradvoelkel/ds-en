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

* *Hauptachsentransformation*, *Hauptkomponentenanalyse* and *Hauptachsentheorem* are all
  **principal component analysis** where the text means the method, which in this book it
  always does. Two translators met the first word independently and rendered it "principal
  axis transformation" and "principal component analysis"; the literal one names the
  linear-algebra operation rather than the thing the sentence points the reader at.

* *gleichmäßig bester Test* and *gleichmäßig bester erwartungstreuer Schätzer* stay literal
  (**uniformly best test**, **uniformly best unbiased estimator**) rather than becoming UMP
  and UMVUE. The German is un-abbreviated and spells out what "best" means; handing the
  reader the acronym is material the original does not have. Both chapters agree; if that
  is ever revisited, they move together.

## Discrete distributions

First needed in `important-discrete-distributions.ipynb`.

| German | English | Note |
|---|---|---|
| Achtung (admonition title) | Caution | not in the fixed table of `TRANSLATION.md` §5; `:class: warning` is kept |
| Annäherung an eine Verteilung | approaching a distribution | plot title in cell 20 |
| Aufruf (einer Methode) | call | table header *gesucht \ |
| Ausfallwahrscheinlichkeit | failure probability | the Poisson binomial example |
| Ausgaberaum | output space | $\Delta_n$ as the output of a classifier |
| Bauteil | component | the defective-components running example; not "part" |
| binäre Entropiefunktion | binary entropy function | $h(p)$; the `###` heading |
| Chance (englisch *odds*) | odds | the German glosses itself with the English word, so the doublet collapses – see *Decisions* |
| Charge | batch | "components from different batches" |
| Der Vollständigkeit halber | For completeness | section heading |
| diskrete Gleichverteilung | discrete uniform distribution | already used in a code comment in `numpy.ipynb` |
| Exponentialreihe | exponential series | $\sum \lambda^k/k! = e^\lambda$ |
| Fehlerquelle | source of error | "the most frequent source of error" |
| Fehlversuch | failure | the geometric distribution's two conventions: trials up to the first success vs. failures before it |
| gedächtnislos | memoryless | and *Gedächtnislosigkeit* would be *memorylessness* |
| geometrische Verteilung | geometric distribution |  |
| Grenzfall | limiting case |  |
| Grenzübergang | passage to the limit | also the comment in cell 20 |
| höchstens abzählbar | at most countable | matches `random-variables-distributions.md` and `expectation-variance.md` |
| Indexverschiebung | index shift | in the Poisson expected-value computation |
| Ja/Nein-Merkmal | yes/no feature | follows the glossary's *Merkmal* → feature |
| Klassifikationsverfahren | classification algorithm | follows the glossary's *Lernverfahren* → learning algorithm |
| Kosmetik (nicht nur Kosmetik) | not merely cosmetic | rendered adjectivally |
| Leitfrage | guiding question |  |
| logistische Regression | logistic regression |  |
| logistische Sigmoidfunktion | logistic sigmoid function |  |
| Logit | logit | lower case in English running prose |
| Maximum-Entropie-Verteilung | maximum entropy distribution | unhyphenated attributively |
| Maximum-Likelihood-Schätzung | maximum likelihood estimation | the glossary has the *estimator* and the *principle*, not the act |
| Muster (von Erfolgen und Misserfolgen) | pattern | the combinatorial argument for the binomial pmf |
| Münzwurf | coin toss | cf. the glossary's *Würfelwurf* → throw of a die |
| Nullstelle | zero | "the only zero is at $p = \frac12$"; not "root" |
| Ohne Beweis | Without proof | the bolded last line of the limit theorem |
| Poisson-Binomialverteilung | Poisson binomial distribution | no hyphen in English |
| Poissonverteilung | Poisson distribution |  |
| Potenzmenge | power set | matches `intro-stochastics.md` |
| Präparat (radioaktives) | specimen | **not** "sample" – see *Decisions* |
| Rückblick | Looking back | section heading; mirrors the glossary's *Ausblick* → Looking ahead |
| Satz von de Moivre-Laplace | de Moivre–Laplace theorem | en dash in the name, as for *Radon–Nikodym* and *Cramér–Rao* |
| Summenformel | summation formula | $\sum i^2$ |
| Tippfehler | typo | plural *typos* |
| Verbindungsversuch | connection attempt |  |
| Versuch, Bernoulli-Versuch | trial, Bernoulli trial | "one probability per trial", "$n$ independent Bernoulli trials" |
| Zufallszahlengenerator | random number generator |  |
| Überlebensfunktion | survival function | the German glosses the English term with a German one; collapses – see *Decisions* |
| σ-Algebra | σ-algebra | the source uses the bare σ character here rather than `$\sigma$`; kept as it stands |

## A first exploratory pass

First needed in `titanic-eda-numpy.ipynb`.

| German | English | Note |
|---|---|---|
| Accuracy (Treffergenauigkeit) | accuracy | the German glosses the English word; the gloss collapses, as with *Störvariable/Confounder* |
| Anführungszeichen | quotation marks | in the CSV-parser sense |
| Anteil (in the grouped `print` labels and the $y$-axis label) | rate | the cell's own third loop was already English and said `Rate:`; see *Decisions* |
| Auszug (aus der Passagierliste) | extract |  |
| Daten verfälschen | to distort the data |  |
| erster Anlauf (chapter title *Titanic EDA, erster Anlauf*) | a first pass | see *Decisions* – "a first attempt" is the literal reading |
| Fehlklassifikationsrate | misclassification rate | the thing the mode minimises; `expectation-variance.md` calls the same loss the *counting error* |
| Instanz | instance | already in `TERMINOLOGY.md` under *Beobachtung, Instanz* |
| Klassifikator | classifier |  |
| Losung ("Frauen und Kinder zuerst") | maxim | "women and children first" is the established English form of the order |
| Precision (Genauigkeit) | precision | likewise |
| protokollieren | to put on record |  |
| Recall (Trefferquote) | recall | likewise; the German's second gloss *in der Medizin Sensitivität* is informative and was kept, and it matches the glossary's `Sensitivität → sensitivity` |
| Rettungsboote planen | planning lifeboats | the recall-versus-precision example |
| Spam aussortieren | sorting out spam |  |
| Trennzeichen | separator | of a CSV/TSV field |
| Umrechnung, Umrechnungsfaktor | conversion, conversion factor | the Bayes factor between precision and recall |
| Zeile (einer Datei) / Zeile (einer Tabelle) | line / row | two senses in this chapter: `file.readline()` output is a *line* (c2.0, c2.1), a data record is a *row* |
| Überlebensquote, Überlebensanteil, Überlebensrate | survival rate | the German uses all three; English has one, and the notebook's own function is `survival_rate` |
| Überschriftzeile, "die mit Überschriften daher kommt" | header row |  |

## The normal distribution and the central limit theorem

First needed in `normal-distribution.ipynb`.

| German | English | Note |
|---|---|---|
| Approximation der Binomialverteilung | Approximating the binomial distribution | section heading; the German noun phrase reads better as a gerund in a heading |
| Auswertungsvorschrift | analysis protocol | the documents that fix how a study's data are to be evaluated |
| de Moivre-Laplace | de Moivre–Laplace | en dash in the two-name theorem, as for *Radon–Nikodym* and *Berry–Esseen* |
| dreiecksverteilt | triangularly distributed | the sum of two uniforms |
| Ein Integral | An integral | section heading |
| gestutzte Normalverteilung | truncated normal distribution | `scipy.stats.truncnorm`, last row of the maximum-entropy table |
| Glockenkurve, Glockenform | bell curve, bell shape |  |
| Konvergenz in Verteilung | convergence in distribution | the mode of convergence in the central limit theorem; the glossary already has *stochastische Konvergenz* → convergence in probability, which is a different thing |
| Laplace-Bedingung | the Laplace condition | $Np \ge 10$ and $N(1-p) \ge 10$; bolded lead-in inside the *Rule of thumb* admonition |
| Momenterzeugendenfunktion | moment generating function | no hyphens in English |
| Nebenbedingung | constraint | the maximum-entropy side condition |
| Normalapproximation | normal approximation | legend entry in cell 16 and running prose in cell 17 |
| Normalverteiltheit | normality | "normality is preserved under affine-linear transformations"; see *Decisions* |
| Ortsbestimmung | position fixing | the GNSS example |
| Praxisbeispiel (as an `##` heading) | A practical example | see the section above on the heading |
| Satz von Berry–Esseen | Theorem (Berry–Esseen) | admonition title; see *Decisions* |
| stabil unter Faltung | stable under convolution |  |
| standardnormalverteilt | standard normally distributed | the adjective; *Standardnormalverteilung* → standard normal distribution |
| Steckbrief (einer Verteilung) | profile | the per-distribution summary pages of `important-continuous-distributions.ipynb`; that chapter is not translated yet and should use the same word |
| Stirling-Formel | Stirling's formula | genitive, as for *Satz von Bayes* → Bayes' theorem |
| Störeinfluss, Störung | disturbance | the independent error sources that sum to a normal distribution; not *Störvariable* → confounder, which the glossary already has |
| technosozial | techno-social | hyphenated |
| Verhältnis (von Schiefe und Umfang) | ratio |  |

## Continuous distributions

First needed in `important-continuous-distributions.ipynb`.

| German | English | Note |
|---|---|---|
| Fertigungsgenauigkeit | manufacturing precision | normal-distribution application bullet |
| Gaussssche Mischung | Gaussian mixture | `statistical-models.md` already has *gemischtes Modell* → mixture model; this is the named special case |
| Gaussverteilung | Gaussian distribution | the glossary's *Normalverteilung* row licenses "Gaussian" where the German says so; the chapter's opening sentence does |
| Heaviside-Step-Funktion | Heaviside step function | no hyphens in English |
| Kehrseite (stetige Kehrseite der Poissonverteilung) | flip side | "the continuous flip side of the Poisson distribution" |
| Lognormalverteilung | log-normal distribution | hyphenated and lower case in running prose, matching the English Wikipedia title the chapter links to; the heading is `## Log-normal distribution` |
| Spielzeugdaten | toy data | the wording `landing-page.md` already uses |
| Sternenhimmel | night sky | the Hubble bullet; `verschmierter Pixelhaufen` → *smeared-out heap of pixels* |
| Stetige Gleichverteilung | continuous uniform distribution | the glossary's *Gleichverteilung* row says "discrete or continuous, say which", and the heading says which |
| Superresolution-Technik | super-resolution technique | hyphenated in English |
| Weibull-Verteilung | Weibull distribution |  |
| Wärmepumpe | heat pump | the Weibull application bullet |
| Übersichtsgrafik | overview diagram | the ProbOnto figure |

## Cleaning data

First needed in `data-cleaning.ipynb`.

| German | English | Note |
|---|---|---|
| Alternative | alternation | the operator, not "alternative" |
| Anker | anchor |  |
| Anrede (Titanic) | title | the Mr/Mrs/Miss field; also the column name, see *Code changes* |
| Augenschein | – | "the first step is always to look"; there is no English noun that is not stilted |
| Ausreißer | outlier | and *Ausreißer erkennen* → *spotting outliers* |
| Baustein | building block | table header and running prose |
| Beispielaufgabe (admonition title) | Example exercise | TRANSLATION.md §5 fixes *Übung / Aufgabe → Exercise*; this is the compound |
| Daten schrubben | data scrubbing | the German quotes the English already; `what-is-data-science.md` uses the same word |
| Dezimaltrenner | decimal separator | TRANSLATION.md §6 already calls it that |
| Editierdistanz (Levenshtein-Distanz) | edit distance (Levenshtein distance) |  |
| Einfüge-, Lösch-, Ersetzungsschritte | insertions, deletions, substitutions |  |
| Einzeiler | one-liner |  |
| Encoding, Kodierung | encoding | one English word for the German's two |
| endlicher Automat | finite automaton | plural *automata*; "Vorlesung über formale Sprachen" → "the course on formal languages" |
| Ersatzwert | substitute value | what `fillna` inserts |
| Feature Engineering | feature engineering | lower case in English running prose |
| Freitextfeld | free-text field |  |
| Gier, gierig / faul | greed, greedy / lazy | the standard regex names; the German uses the same metaphor |
| Gruppe | group | and *Rückwärtsreferenz* below |
| Imputation | imputation | bold on first use, as in the German |
| Lücke (in einer Spalte) | gap | not "hole", not "missing value" – the chapter contrasts genuine gaps with the ones it creates |
| Maske | mask | already in the glossary from `numpy.ipynb`; the chapter's logging columns are masks |
| Messfehler / Vorzeichenfehler | measurement error / sign error |  |
| Metadatendatei | metadata file |  |
| naiv / bewusst (Zeitstempel) | naive / aware | Python's own pair, which is what the German is translating |
| negativer / positiver Lookahead | negative / positive lookahead | the German keeps the English word too |
| Niederschlagshöhe | amount of precipitation | DWD's `RSK`, "in mm" |
| Ortszeit | local time |  |
| passt auf (Tabellenkopf) | matches |  |
| Protokoll | log | "the table of assignments belongs in the log"; "three columns that are nothing but the log". Chosen because `what-is-data-science.md` already promises a chapter that "insists on logging every change made to the data" |
| Protokollieren (rule 1) | log it | the imperative heading of the Principle admonition |
| Raw-String | raw string | two words |
| Rechtschreibprüfer | spell checker |  |
| Rettungsreihenfolge | the order in which people were rescued | rendered as a clause; "rescue order" reads as a product name |
| Rückwärtsreferenz | backreference | one word in English |
| Schreibweise (einer Stadt) | spelling | "seven spellings become two cities" |
| Schreibweise (Tabellenkopf) | notation | table header; distinct from *Schreibweise* = spelling above, which is why both are recorded |
| schwach / stark bindend | binding weakly / binding strongly | operator precedence, the axis the table is sorted on |
| Sommerzeit-Umstellung | daylight-saving change | `what-is-data-science.md` already says "daylight saving changes" |
| Sonnenscheindauer | duration of sunshine | DWD's `SDK` |
| sprechende Namen | telling names |  |
| Tausendertrennzeichen | thousands separator |  |
| Unix-Zeitstempel | Unix timestamp | the glossary has *Zeitstempel → timestamp* |
| Verfälschung, verfälschen | distortion, to distort | the chapter's central verb: "every act of cleaning distorts the data" |
| Verkettung | concatenation | the glossary has *Verkettung (von Abbildungen) → composition*; for strings and regexes it is concatenation |
| Wiederholung | repetition |  |
| Wochentag | day of the week |  |
| Z-Score | z-score | lower case, matching the glossary's *z-Wert → z-value*, *z-Test → z-test* |
| Zeichenklasse, negierte Zeichenklasse | character class, negated character class |  |
| Zeitzonendatenbank | time zone database | "the *tz database* (also called the IANA time zone database)" |
| Zielmetrik | target metric | the glossary has *Zielgröße → target variable*, not this |
| Zusammenfassen auf Monate | aggregating up to months | what `resample("MS")` does |
| Überlebensrate | survival rate |  |
| Übersetzungstabelle | mapping table | "translation table" would be confusing in a translated book, and a `dict` passed to `replace` is a mapping |

## The multivariate normal distribution

First needed in `multivariate-normal.ipynb`.

| German | English | Note |
|---|---|---|
| Basiswechsel (linear algebra) | change of basis | **collides** with the existing row *Basiswechsel → change of base* in `relative-entropy.md`, which is about logarithms. Two different things; "an orthogonal change of basis" is the only English here |
| Dichten von multivariaten Verteilungen | Densities of multivariate distributions | section heading |
| Drehstreckung | the rotation and the stretching | rendered as a pair of nouns, not as one word – see *Decisions* |
| drehsymmetrisch | rotationally symmetric | not "rotation-symmetric" |
| Eigenzerlegung | eigendecomposition | one word, as PCA literature has it |
| Gipfel (einer Dichte) | peak | "deforms the peak into an ellipse"; not "summit" |
| Halbachse (einer Ellipse) | semi-axis | plural *semi-axes* |
| Heatmap | heatmap | the German already uses the English word; one word in the English edition |
| Herleitung | derivation | the section heading *Derivation: from the symmetry to the formula* |
| Konturplot | contour plot | distinct from *Höhenlinie/Konturlinie → contour line*, which the chapter also uses |
| Levelset, Niveaumenge | level set | two words in English; follows the `statistical-models.md` row *Niveaumenge → level set*. The German writes the English loanword as one word, "Levelsets" |
| Linearkombination | linear combination |  |
| Maximum-Entropie-Eigenschaft | maximum entropy property | unhyphenated in English |
| mehrdimensional / multivariat | multidimensional / multivariate | the German uses both for the same thing and so does the English |
| orthogonale Matrix | orthogonal matrix |  |
| quadratische Form | quadratic form |  |
| Signatur (einer Funktion) | signature | of $f \colon \mathbb{R}^n \to [0,\infty)$ |
| Strahl (von $\mu$ weg) | ray |  |
| Strecken, Streckung | stretching | the verb for $D$; *Skalieren* → *scaling* is the operation's bolded name in the list |
| Streckfaktor | stretch factor | also in a `print` string; the factors $\sqrt{\lambda_i}$ |
| univariat normalverteilt | univariate normally distributed | and *multivariat normalverteilt* → multivariate normally distributed |
| Variational Autoencoder | variational autoencoder | lower case in English running prose; the German capitalises it as a noun |
| Verschieben / Skalieren / Drehen | Shifting / Scaling / Rotating | the three bolded operations in the derivation; the code comments use the same three words |

## Clustering

First needed in `kmeans.ipynb`.

| German | English | Note |
|---|---|---|
| Ausdehnung (eines Clusters) | extent | the bolded weakness **Very different extent (variance)**; "spread" is taken by the glossary for *Streuung* |
| Bewertung (eines Verfahrens) | assessment | not "evaluation": the paragraph is about *whether you can judge the result at all*, which is what the train-test split buys you |
| bisecting k-means | bisecting k-means | the German already uses the English name; stays, and so do *mini-batch k-means* and *kmeans++* |
| Einordnung (section heading) | Where this fits | the opening heading *Einordnung: Klassifikation, Regression, Clustering*; "Classification" alone would collide with the task name in the same heading |
| Elbow-Kriterium, Elbow plot | elbow criterion, elbow plot | lower case in English running prose; `fig.suptitle("elbow plot")` was already English |
| Fluch der Dimensionalität (curse of dimensionality) | curse of dimensionality | the German glosses itself with the English; the doublet collapses |
| gemischtes Gaußsches Modell | Gaussian mixture model | follows the glossary's *gemischtes Modell → mixture model*; `descriptive-statistics.md` already links the EM chapter under this name |
| Gerade / Hyperebene | straight line / hyperplane | "a straight line", not "a line", because the point of the sentence is that the boundary is *not* curved |
| Halbebene | half-plane |  |
| Halbmond (als Clusterform) | half-moon | the scikit-learn `make_moons` shape |
| innere Varianz | inner variance | matches the code's `total_inner_variance`; the elbow score is `group_variance / total_inner_variance` |
| Konvergenz | convergence | and *konvergierende Implementierung* → *converging implementation* |
| Label | label | the German uses the English word; bolded on first use, as in `titanic-eda-numpy.ipynb` |
| Merkmalsraum | feature space | follows the glossary's *Merkmal → feature* |
| Mittelsenkrechte | perpendicular bisector | of the *Verbindungsstrecke* → *line segment joining* the two centroids |
| Samplegröße | sample size | the glossary's *Stichprobenumfang → sample size*; the German says *Samplegröße* here |
| Schwelle (auf einem Merkmal) | threshold | matches the glossary's *Schwellwert → threshold* |
| Train-Test-Split | train-test split | hyphenated, lower case; `model-selection.ipynb` will need the same |
| Trägheit (inertia) | inertia | the German glosses itself with the English; the doublet collapses. The quantity $J(c_1,\dots,c_k) = \sum_i \min_j \lVert x_i - c_j \rVert^2$ |
| Verwechslung | mix-up | the off-diagonal entries of a confusion matrix; "confusion" would read as the matrix's name |
| Voronoi-Zelle | Voronoi cell | plural *Voronoi cells* |
| Zerlegung (der Ebene) | decomposition | follows the glossary's *Zerlegung → decomposition* from `covariance.md`, even though that row is about events |
| Zuweisungsschritt | assignment step | the first half of a k-means iteration; the second is the centroid update |

## Dimensionality reduction

First needed in `dimensionality-reduction.ipynb`.

| German | English | Note |
|---|---|---|
| Anwendungsbeispiel (as an `###` heading) | Application example | rendered with a colon, *Application example: MNIST* / *Application example: Wine*; the German juxtaposes without punctuation, which English will not do |
| Auswählen / Projizieren | Selecting / Projecting | two of the five bolded steps; follows the mvn pattern *Verschieben / Skalieren / Drehen → Shifting / Scaling / Rotating* |
| Berechnung (as an `###` heading) | Computation | and *Berechnung mit Scikit-learn* → *Computation with Scikit-learn* |
| charakteristisches Polynom | characteristic polynomial |  |
| Diagonalmatrix, Diagonaleintrag | diagonal matrix, diagonal entry |  |
| Dimensionsreduktion in fünf Schritten | Dimensionality reduction in five steps | section heading; the glossary already fixes the term |
| Eigenraumzerlegung | eigenspace decomposition | the German's own parenthetical name for $C = TC'T^{-1}$; distinct from *Eigenzerlegung → eigendecomposition*, which `multivariate-normal.ipynb` already has |
| Einheitsbasisvektor | standard basis vector | not "unit basis vector" |
| erklärte Varianz | explained variance | the German glosses itself "*erklärte Varianz* (explained variance)"; the doublet collapses to one word. `explained_variance_ratio_` stays as the attribute name |
| Feature Scaling | feature scaling | lower case in English running prose; kept in the German's own single quotes |
| Gaussverfahren | Gaussian elimination | not "Gauss procedure"; the standard English name for solving $Mv = \alpha v$ by row reduction |
| gemischte Gausssche Modelle | Gaussian mixture models | the standard English name; `statistical-models.md` has *gemischtes Modell → mixture model*, and this is the Gaussian case |
| Gesamtvarianz | total variance | $\operatorname{tr}(C)$ |
| Hauptkomponente / Hauptachse | principal component / principal axis | plural *principal axes*; the glossary had only *Hauptkomponentenanalyse → principal component analysis* |
| Linear Discriminant Analysis (LDA) | linear discriminant analysis (LDA) | already English in the German; lower-cased in running prose, as with *data mining* |
| Normalisierung | normalisation | house `-ise` spelling; the rescaling to $[0,1]$, kept in the German's single quotes |
| Orthogonalkomplement | orthogonal complement |  |
| Orthonormalbasis | orthonormal basis | and *Orthonormalmatrix* → *orthonormal matrix*, the German's second name for an orthogonal matrix |
| Rayleigh-Quotient | Rayleigh quotient | no hyphen in English |
| Reskalierung, Umskalierung | rescaling | two German words, one English one |
| Rücktransformation, rücktransformiert | back-transformation, back-transformed | also a plot title, cell 9 |
| scheren | to shear | what a matrix does besides rotating; *stauchen / strecken* → *compress / stretch* |
| Schwerpunkt (eines Datensatzes) | centre of mass | British spelling; "so that the dataset has its centre of mass at $0$" |
| Singulärwert, Singulärwertzerlegung | singular value, singular value decomposition | SVD; the code comment keeps the English expansion the German already had |
| Skalenunterschiede | Differences in scale | the `##` section heading |
| Spektralsatz | spectral theorem |  |
| Standardisierung | standardisation | mean $0$, standard deviation $1$; kept in the German's single quotes |
| Standardskalierung, standardskaliert | standard scaling, standard-scaled | hyphenated attributively, in prose and in the plot titles |
| Untervektorraum | subspace | not "sub-vector space" |
| Verzerrung (einer Transformation) | distortion | here the scale effect, not statistical bias – `statistical-models.md` has *verzerrt → biased* for that |
| Zentrieren | Centring | British spelling; the first of the five bolded steps. *zentrierte Datenmatrix* → *centred data matrix*, following the glossary's *zentriertes Sample → centred sample* |

## Regression

First needed in `linear-regression.ipynb`.

| German | English | Note |
|---|---|---|
| Achtung: Begriffe anderswo | Caution: these terms elsewhere | admonition title, `:class: warning` |
| Anwendungsbeispiel | An example application | `##` heading; the Melbourne section |
| Ausgleichsgerade | line of best fit | the regression line computed by least squares |
| Basisfunktion, Basisfunktionserweiterung | basis function, basis function expansion | the standard English of Hastie et al.; "basis expansion" alone was avoided because the German names the function |
| Bestimmtheitsmaß | coefficient of determination | the German glosses itself "en. *Coefficient of determination*"; the doublet collapses to the one English word |
| Bias-Term (Achsenabschnitt) | bias term (intercept) | `w_0`; the chapter itself warns that *bias* is doubly used – the estimator's bias is in `statistical-models.md` |
| CBD | CBD | kept; the chapter explains it is what Melbourne calls its centre |
| Dummy-Falle | dummy variable trap | the standard English name is the longer one; italicised as in the German |
| einfache / multiple lineare Regression | simple / multiple linear regression |  |
| Einflussgröße | explanatory variable | the counterpart of the glossary's *Zielgröße* → target variable; "regressor" is reserved for the German's own parenthetical *(Regressor)* |
| Formfaktor | shape factor | petal area as length × width "up to a shape factor" |
| Gerade minimalen Abstands | Line of minimal distance | plot legend, kept literal; the prose word is *line of best fit* |
| kleinste Quadrate, kleinste-Quadrate-Schätzer | least squares, least squares estimator | `## Kleinste Quadrate` → `## Least squares` |
| L1-/L2-Regularisierung, L1-/L2-Norm | L1 / L2 regularisation, L1 / L2 norm | no hyphen before the numeral in English |
| Lasso-Regularisierung | lasso regularisation | lower case in running prose, as with *bootstrap* in `statistical-tests.md` |
| Link-Funktion | link function | logistic regression's $\sigma$ |
| polynomiale Regression | polynomial regression |  |
| Referenzkategorie | reference category | the level `drop_first=True` leaves out |
| Regressand | regressand | stays; paired with *Regressor* → regressor |
| Regressionsgerade / Regressionskurve | regression line / regression curve | plot legends |
| Regularisierung | regularisation | `##` heading; house `-ise` spelling |
| Reihenhaus / Wohnung (`Type`) | townhouse / unit | the Melbourne `Type` codes; *unit* glossed once as "that is a flat", since the Australian word is not obvious |
| Residuenquadratsumme | residual sum of squares | not "sum of squared residuals"; `Residuen` → residuals is already in the glossary |
| Ridge-Regression | ridge regression | lower case in running prose |
| Strafterm, Strafe | penalty term, penalty | `Die L1-Strafe` → "the L1 penalty" |
| Störgröße | error term | the unobservable $\epsilon$, as against the observable residual – see *Decisions* |
| Stützstelle | support point | see *Decisions* |
| weight decay | weight decay | the German already uses the English |
| Zusammenfassung | Summary | `##` heading; matches the translated notebooks |

## Kernel methods

First needed in `kernel-methods.ipynb`.

| German | English | Note |
|---|---|---|
| Abstandsbegriff | notion of distance | not "concept of distance" – the chapter means which inner product you measure with |
| Abstandsmessung | measurement of distance | "rest on nothing but measurements of distance" |
| Beobachtungsraum | observation space | where the first principal component is a curve, not a line |
| bis auf Translation und Rotation | up to translation and rotation |  |
| Datum (ein einzelnes) | datum | see *Decisions* 3 |
| Eigenvektor | eigenvector |  |
| Feature-Abbildung | feature map | $\phi$; not "feature mapping" |
| Feature-Raum | feature space | $F$; also used (in German) by `expectation-maximization.ipynb` and `kmeans.ipynb` |
| Feature-Vektor | feature vector |  |
| Gausssche Kernel, Gauss-Kernel | Gaussian kernels | see *Decisions* 1 |
| k-Nearest Neighbours | k-nearest neighbours | lower case in English running prose, as with *k-means* |
| Kernel-Funktion, Kernelfunktion | kernel function | the German spells it both ways; one English spelling |
| Kernel-Methode (singular) | kernel method | "one speaks of the **kernel method** when…"; the chapter title stays the plural *Kernel methods* |
| Kernel-Trick | kernel trick | the chapter's central notion; the glossary had only *Kernel-Methoden → kernel methods* |
| Mercer-Kernel | Mercer kernel | no hyphen in English, as with *Shannon entropy* |
| Nebenbemerkung | aside | *Bemerkung → Remark* is fixed for admonition titles; this is running prose |
| normierte Vektoren | normalised vectors | the glossary's *normieren → to normalise* |
| Normierung | normalisation | the one a Gaussian density would carry and a kernel does not |
| quadrierter / quadratischer Exponentialkernel | squared / quadratic exponential kernel | the German offers both; so does the English |
| radiale Basisfunktion | radial basis function | the first section heading; `rbf_kernel` keeps its name |
| radialer Basisfunktionskernel | radial basis function kernel |  |
| rechenintensiv | expensive to compute |  |
| Ridge-Regularisierung | ridge regularisation | house `-ise`; `KernelRidge` keeps its name |
| Satz von Mercer | Mercer's theorem | genitive, as for *Satz von Bayes → Bayes' theorem* |
| Standbild | still image | the PDF fallback in the cell 5 comment |
| Support Vector Machines | support vector machines | likewise lower case |
| translations- und rotationsinvariant | invariant under translation and rotation | the German compound does not survive as one word |
| Vektorraum mit Skalarprodukt | vector space with an inner product | follows the glossary's *Skalarprodukt → inner product* |

## Model selection and cross-validation

First needed in `model-selection.ipynb`.

| German | English | Note |
|---|---|---|
| Bestimmtheitsmaß / $R^2$-Wert | $R^2$ value | the chapter only uses *$R^2$-Wert*; `linear-regression.ipynb` (still German) carries *Bestimmtheitsmaß* and will need *coefficient of determination* |
| Bewertung (der Modellperformance / von Clustering / einer Regression) | assessing | the three `Bewertung …` headings become *Assessing model performance*, *Assessing a clustering*, *Assessing a regression*; "evaluation" was the alternative – see *Decisions* 4 |
| Bewertungsfunktion | scoring function | what `scoring=` takes; "evaluation function" reads less like scikit-learn |
| Black Box | black box | two words in English |
| drop-in Ersatz | drop-in replacement |  |
| Einheitsvarianz | unit variance | `StandardScaler` |
| F1-Score | F1 score | two words, no hyphen, as `titanic-eda-numpy.ipynb` asked; the scikit-learn output column `f1-score` in block c19.0 stays literal because it is program output |
| Fold, Falte | fold | the German uses the English *folds* in c4.3/c6.1 and the German *Falte* in c38.1; one English word |
| gelabelt / ungelabelt | labelled / unlabelled | British double-l; *Label* → *label* was settled in `titanic-eda-numpy.ipynb` |
| generalisieren, verallgemeinern | to generalise | the German uses both verbs for the same thing |
| Gittersuche | grid search | the `###` heading; matches `GridSearchCV` |
| Ground Truth | ground truth | lower case, as `sync/notes/titanic-eda-numpy.ipynb.md` asked this chapter to do |
| Hauptkomponenten | principal components | `TERMINOLOGY.md` has *Hauptkomponentenanalyse* → PCA, not the components |
| Homogenität / Vollständigkeit (Completeness) | homogeneity / completeness | the German switches between *Vollständigkeit* and the English *Completeness*; English has one word, which is also the scikit-learn name |
| Hyperparameter-Finetuning | hyperparameter fine-tuning |  |
| Hyperparametersuche | hyperparameter search | the `##` heading |
| k-fold Cross Validation | k-fold cross-validation | heading; the German is already English but German-capitalised and unhyphenated – see *Decisions* 2 |
| Kernel-Ridge-Regression | kernel ridge regression | no hyphens in English; `KernelRidge` |
| Kernelbreite | kernel width | the RBF $\gamma$ |
| Klassifikationsgüte | classification quality | follows the glossary's *Güte* → *quality* |
| Lader | loader | the code comment in cell 28 |
| leaken, Information Leakage, Informationsleck | to leak, information leakage | the German glosses the English with the German *ein Informationsleck*; the gloss collapses – see *Decisions* 5 |
| log-gleichverteilt | log-uniformly | `loguniform`; the glossary's *Gleichverteilung* → *uniform distribution* |
| normalisierte gemeinsame Information | normalised mutual information | `TERMINOLOGY.md` binds *gemeinsame Information* → *mutual information* (from `relative-entropy.md`); "normalised" in house spelling, even though the scorer is `normalized_mutual_info_score` |
| permutationsinvariant | permutation-invariant |  |
| Pixelsummen | pixel sums |  |
| Randomisierte Suche | Randomised search | house `-ise` spelling, even though the class is `RandomizedSearchCV` |
| Regularisierungskonstante / Regularisierungsparameter | regularisation constant / regularisation parameter | the German distinguishes the two words, so English does too |
| Setting | setting | the German already uses the English word |
| stratifizierte k-fache Kreuzvalidierung | stratified k-fold cross-validation |  |
| Suchstrategie | search strategy |  |
| Summe der Residuenquadrate | residual sum of squares | `TERMINOLOGY.md` has *Residuen* → *residuals* only |
| Support Vector Classification | support vector classification | lower case in running prose; `SVC` and `SVM` stay upper case |
| T-Shirts, Hosen | T-shirts, trousers | British "trousers" |
| Teilstichprobe | subsample | one word; the glossary's *Stichprobe* → *sample* |
| Test-Datensatz, Trainings-Datensatz, Validation-Datensatz | test set, training set, validation set | follows `descriptive-statistics.md`'s *Testdatensatz-Performance* → *performance on the test set*; `TERMINOLOGY.md` already binds *Testdaten/Trainingsdaten* → *test data / training data*, which is used where the German says *Daten* |
| Training, Test und neue Daten | Training, test and new data | the `##` heading – see *Decisions* 1 |
| Training, Validation und Test | Training, validation and test | the `###` heading |
| Treibhausgase | greenhouse gases |  |
| V-Maß | V-measure | `v_measure_score` |
| Visualisierung der Kreuzvalidierungsstrategien | Visualising the cross-validation strategies | heading |
| Zeitreihen-sensible Kreuzvalidierung | Time-series-aware cross-validation | heading; see *Decisions* 3 |

## Worked exploratory analyses

First needed in `eda-examples.ipynb`.

| German | English | Note |
|---|---|---|
| Alkoholgehalt | alcohol content |  |
| Anhäufung (im Scatterplot) | cluster | the visual pile-up that `alpha=0.1` reveals, not a clustering algorithm's cluster |
| auseinanderhalten / trennen (Klassen) | keep apart / separate |  |
| bloße Häufigkeit | bare frequency | the count on its own, before any covariate is brought in |
| Byte-String | byte string | two words; `b'D\xfcsseldorf'` |
| Colormap | colormap | one word, matplotlib's own spelling, and the German already uses it |
| Deutscher Wetterdienst (DWD) | German weather service (DWD) | the German lower-cases *deutsche* here, so it is used descriptively; the abbreviation stays |
| einstellige Zahl | single-digit number |  |
| Explorative Analyse: Beispiele | Exploratory analysis: examples | the H1; `descriptive-statistics.md` already links here under exactly this text, twice, so it was fixed before I started |
| Fachliteratur | specialist literature |  |
| Forschungsfrage | research question | `descriptive-statistics.md` already has "Formulate the research questions" in its worked procedure, and this chapter is what that step points at |
| ganze Zahl / Gleitkommazahl | integer / floating-point number | the `i8`/`f8` comment in cell 25 |
| Hauptachsentransformation | principal component analysis | the German glosses itself "(principal component analysis, PCA)"; see *Decisions* 2 |
| Hilfsvariable | auxiliary variable | the class, used to split the sample |
| Indikator (für die Klasse) | indicator | not *Indikatorfunktion*, which `expectation-variance.md` already has |
| Koordinaten-unabhängiges Verfahren | coordinate-independent procedure | the thing PCA will supply |
| Kopfzeile (einer CSV) | header row | matches `titanic-eda-numpy.ipynb` |
| menschenlesbar | human-readable |  |
| Metadaten | metadata | plural verb: "the metadata are available" |
| Niederschlag, Niederschlagsereignis | precipitation, precipitation event | `RRmean` is the *mean precipitation*; the quoted description says *starke Niederschlagsereignisse* → *heavy precipitation events* |
| Normalverteilungsdichte | normal density | "the corresponding normal densities"; the glossary has *Dichte → density* |
| Nutzungslizenz | licence | British spelling of the noun |
| Objekt-orientiertes Interface | object-oriented interface | matplotlib's own name for it |
| Originalquelle | original source | the CC-BY attribution requirement |
| Passagierklasse | passenger class | `Pclass` |
| Prolingehalt | proline content | `Proline`; the German adds *Aminosäure* → "an amino acid" |
| Proteingehalt | protein content | the German's reading of `OD280/OD315 of diluted wines` |
| Prävalenzfehler | base rate fallacy | see *Decisions* 3 – the glossary binds *Basisratenfehler* to this, and it is the same fallacy |
| RADKLIM-Gitter, Gitterpunkt | RADKLIM grid, grid point |  |
| Rückgabewert | return value |  |
| Schadenspotenzial | damage potential | in the quoted description |
| Starkregen | heavy rain | the weather, as against the catalogued *event* |
| Starkregenereignis | heavy rainfall event | the section heading *Heavy rainfall events (CatRaRE)*; CatRaRE's own expansion is "Catalogue of Radar-based heavy Rainfall Events", so this is the DWD's English, not an invention |
| Starkregengeschehen | heavy rainfall activity | in the quoted dataset description |
| teiltransparent | partly transparent | the `alpha=` argument |
| Trainings-Datensatz | training dataset | the glossary has *Trainingsdaten → training data*; this is the file |
| Volumenprozent | per cent by volume | "12 to 14.5 per cent alcohol by volume" |
| weißer Fleck (im Scatterplot) | white patch | the empty corner of the protein-proline cloud |
| Wettbewerb/'Competition' (Kaggle) | 'competition' | the German already quotes the English word; lower-cased in English running prose |
| Zeichenkette (Numpy `S10`) | string | already in `TERMINOLOGY.md` from `pandas.ipynb` |
| Äpfelsäure | malic acid | the German glosses the dataset's own English column name, so the gloss collapses |
| Überlebensquote | survival rate | as decided in `titanic-eda-numpy.ipynb` |
| Überlebensstatus | survival status |  |

## Mixture models and EM

First needed in `expectation-maximization.ipynb`.

| German | English | Note |
|---|---|---|
| Anwendungsbeispiele | Example applications | the `##` heading before the three datasets |
| Aufenthaltsort | whereabouts | the GPS dataset's heading *Aufenthaltsorte* → *Whereabouts*; "die längeren Aufenthaltsorte" → "the places where the longer stays happened" |
| Bayessches Informationskriterium (BIC) | Bayesian information criterion (BIC) | the German adjective is *Bayessch*, not *Bayes'sch*; English has the standard name |
| Clustermittelpunkt, Clusterzentrum | cluster centre | British spelling; distinct from *Zentroid* → centroid, which the same cell also uses |
| Entstehungsprozess | generative process | "one can picture the generative process like this"; follows *datenerzeugende Verteilung → data-generating distribution* in `covariance.md` |
| erwartete vollständige-Daten log-Likelihood | expected complete-data log-likelihood | $Q(\theta,\theta)$ |
| fette $1$ | fat $1$ | the trick of multiplying in a cleverly written $1$; twice, blocks c9.8 and c11.6 – see *Decisions* |
| Fitness-Funktion | fitness function |  |
| Hilfsfunktion | auxiliary function | the `##` heading is already English in the German (*Auxiliary Functions*) and was left verbatim – see *Decisions* |
| hochgestellter Index | superscript index | the $t$ of $\theta^{(t)}$ |
| Iversen-Bracket (sic) | Iverson bracket | the German misspells the name; corrected – see *Decisions* |
| Jensensche Ungleichung | Jensen's inequality | genitive, as for *Satz von Bayes → Bayes' theorem* |
| Klasseneinteilung | division into classes | the chapter's workhorse word, 11 occurrences in 7 blocks; "class" alone in the one place where it is a single point's class – see *Decisions* |
| M-M-Algorithmus, Minorisieren-Maximieren | MM algorithm, minorise–maximise | en dash in the pair, house `-ise`; *Majorisieren-Minimieren* → majorise–minimise |
| Mischkomponente, Mischungskomponente | mixture component | two German spellings, one English word |
| Mischungsparameter | mixture parameters | the $p_j^{(t)}$ inside the iteration |
| Mischverhältnis | mixing ratio | the $p_i$ at initialisation time; kept literal rather than "mixture weights" |
| Normalverteilungsannahme | normality assumption | not "normal distribution assumption" |
| Nullstellen der Ableitung bestimmen | finding the zeros of the derivative | section heading; `statistical-models.md` says "setting derivatives to $0$" in prose, but the heading needs the noun |
| Optimierungstransfer | optimisation transfer | the MM literature's own term |
| Responsibilities, Verantwortlichkeiten | responsibilities | the German offers both words (and misspells the English one as *responsibilites*); the doublet collapses – see *Decisions* |
| Sample-Erwartungswert | sample expected value | and *Sample-Kovarianz* → sample covariance – see *Decisions* |
| Schablone (für Algorithmen) | template | "the EM algorithm is really not one algorithm but a template" |
| soft assignment, hard assignment | soft assignment, hard assignment | the German glosses each with *(weiche/feste Zuweisung)*; the gloss disappears. The verb: "the class to which $x_i$ was hard-assigned" |
| Spezialfall | special case | heading *Spezialfall k-Means* → *Special case: k-means* |
| Stichprobenindex | sample index |  |
| Summen-Nummer | that sum business | colloquial; "and the logarithm does not get us out of that sum business so easily" |
| Teildatensatz der $7$er | the subset of the data consisting of the $7$s |  |
| vollständige Daten, vollständige-Daten log-Likelihood | complete data, complete-data log-likelihood | the `##` heading becomes *The complete-data log-likelihood* |
| Zeitreihenanalyse | time series analysis | the closing list of what the book does not cover |
| Zielgröße (an optimisation target) | target quantity | **collides** with the glossary's *Zielgröße → target variable*, which is the supervised-learning label. Here it is the objective being optimised, not a variable – see *Decisions* |

