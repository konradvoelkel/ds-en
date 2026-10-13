# Terminology

Binding for every chapter. If a term is missing and you had to think about it, add it in
the same commit you used it in. Grown chapter by chapter, so entries carry the chapter
that first needed them.

## The one that has no translation

**Stochastik** — covers probability theory *and* statistics and has no English equivalent.
Never "stochastics". Translate what is meant: "probability", "probability and statistics",
or, where the German means the mathematical field as a whole, "probability theory and
statistics". `Stochastik programmieren` → "programming with probability".

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
