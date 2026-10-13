# Translator's notes: `dimensionality-reduction.ipynb`

German original `dimensionsreduktion.ipynb`, 36 cells, 89 blocks, 1 declared drop (the HHU
lecture recording link under the H1, block `c0.1`), 88 translated blocks. No further drops,
no `sync/additions` entry, no `sync/check-ignore` entry – all four checks (`nbtext.py
check`, `nbtext.py syntax`, `sync.py align`, `check_english.py`) pass with zero findings,
and `grep -c '{,}'` is 0.

The chapter references three images – `images/case_a_dual_proj.png`,
`images/case_b_dual_proj.png` and `images/pca-variation.gif`. **None needs redrawing**: the
two PNGs already carry English legends ("Original 3D", "Proj to XY (Z=0)", "Variance
difference: 2.28 - 2.27 = 0.01"), and the GIF has no text at all beyond the numeric axis
ticks. Nothing to add to `images/README.md`.

The chapter continues `covariance.md` and `multivariate-normal.ipynb` and takes their rows
over unchanged: inner product (not "scalar product"), covariance matrix, eigenvalues /
eigenvectors, eigendecomposition, change of basis, positive (semi)definite, bivariate
normal distribution, cloud of points, derivation, stretching, scatter plot, target variable,
summary measure, mutual information, Simpson's paradox.

## New terminology

| German | English | Note |
|---|---|---|
| Anwendungsbeispiel (as an `###` heading) | Application example | rendered with a colon, *Application example: MNIST* / *Application example: Wine*; the German juxtaposes without punctuation, which English will not do |
| Auswählen / Projizieren | Selecting / Projecting | two of the five bolded steps; follows the mvn pattern *Verschieben / Skalieren / Drehen → Shifting / Scaling / Rotating* |
| Berechnung (as an `###` heading) | Computation | and *Berechnung mit Scikit-learn* → *Computation with Scikit-learn* |
| charakteristisches Polynom | characteristic polynomial |  |
| Diagonalmatrix, Diagonaleintrag | diagonal matrix, diagonal entry |  |
| Dimensionsreduktion in fünf Schritten | Dimensionality reduction in five steps | section heading; the glossary already fixes the term |
| Einheitsbasisvektor | standard basis vector | not "unit basis vector" |
| Eigenraumzerlegung | eigenspace decomposition | the German's own parenthetical name for $C = TC'T^{-1}$; distinct from *Eigenzerlegung → eigendecomposition*, which `multivariate-normal.ipynb` already has |
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

## Code changes

German identifiers renamed (grepped across the whole notebook afterwards – the only
survivor is inside a **stored output**, which the re-execution pass will replace):

| German | English | cells |
|---|---|---|
| `werte` | `values` | 7 |
| `vektoren` | `vectors` | 7 |
| `neue_koordinaten` | `new_coordinates` | 7 |
| `kumuliert` | `cumulative` | 19 |

`values` / `vectors` are the names `multivariate-normal.ipynb` already chose for exactly
this pair, so the two chapters agree. Everything else was already English (`eigenvalues`,
`eigenvectors`, `pca_x`, `new_x`, `newer_x`, `new_C`, `scores`, `update_scores`, `ratio`,
`dummycenters`, `dummycovs`, `dummydata`, `dummymu`, `scaledmu`, `original_labels`,
`unscaled_pca`, `scaled_kmeans`, …). Library names and keyword arguments are untouched.

Translated strings:

* **Plot titles.** Cell 9: `"Standardnormalverteilung"` → `"Standard normal distribution"`,
  `"Transformierte Stichprobe"` → `"Transformed sample"`, `"Rücktransformiert"` →
  `"Back-transformed"`. Cells 12 and 14: `"Die ersten zwei/drei Hauptkomponenten des
  Iris-Datensatzes"` → `"The first two/three principal components of the Iris dataset"`.
  Cell 27: `"Unten: Standardskaliert"` → `"Bottom: standard-scaled"`, `"Oben:
  Ausgangsdaten"` → `"Top: original data"`. Cells 30 and 33: `"Links: Labels von k-Means"` →
  `"Left: labels from k-means"`, `"Rechts: ursprüngliche Klassen"` → `"Right: original
  classes"`, `"Oben: Unskaliert PCA,\n Unten: Standardskaliert PCA"` → `"Top: PCA
  unscaled,\n Bottom: PCA standard-scaled"` (the leading space after `\n` is the German's
  own and was kept).
* **Axis labels and legend.** Cell 19: `"Anzahl Komponenten"` → `"number of components"`,
  `"erklärte Varianz (kumuliert)"` → `"explained variance (cumulative)"`. Cell 27:
  `label="Mittelwert"` → `label="mean"`.
* **`print` labels.** Cell 4: `"die Transformation T ist in diesem Beispiel:"` → `"in this
  example the transformation T is:"`. Cell 7: `"Eigenwerte:"` → `"eigenvalues:"`,
  `" erklärte Varianz der 1. HK:"` → `" explained variance of the 1st PC:"` (*HK* =
  *Hauptkomponente*), `"neue Koordinaten:"` → `"new coordinates:"`. Cell 19: `"Komponenten
  für 90% der Varianz:"` → `"components for 90% of the variance:"` and the trailing `"von"`
  → `"out of"`. Cell 35: the long `%f` sentence → `"The scaled version, with a similarity of
  %f to the 'true' class, is better than the unscaled version with a similarity of only
  %f"`; the `%f` placeholders and the single quotes around *true* are unchanged.
* **Comments.** Cells 4 and 20, all of them. `# zum Beispiel!` → `# for example!`; the
  `eigh` explanation; `# absteigend, wie bei der SVD` → `# descending, as in the SVD`; the
  sign-ambiguity note; `# Schritt 5: Skalarprodukte mit v_1, v_2` → `# step 5: inner
  products with v_1, v_2` (glossary: *Skalarprodukt* → inner product); `# Jetzt schmeissen
  wir Dimensionen weg, / # und analysieren wie dadurch die Klassifikation leidet:` → `# Now
  we throw dimensions away / # and analyse how the classification suffers as a result:`.
  Cells 9 and 26 had one German comment each (`# eine willkürliche Transformation:` → `# an
  arbitrary transformation:`); the rest of cells 21, 26, 27, 29 and 30 were already English
  and are unchanged.

No logic was touched, no cell added, removed, merged or retyped, and no whitespace moved
except where a renamed identifier shifted a trailing aligned comment. The code was **not**
re-executed, per instructions; `nbtext.py syntax` confirms every cell still compiles.

**For the re-execution pass:** every stored output is still the German one.

* German stream output: cells **4** ("die Transformation T ist in diesem Beispiel"), **7**
  ("Eigenwerte", "erklärte Varianz der 1. HK", "neue Koordinaten"), **19** ("Komponenten für
  90% der Varianz … von"), **35** (the whole sentence).
* PNGs with German text baked in: cells **9**, **12** (two figures), **14**, **19** (axis
  labels), **27**, **30**, **33**.
* Cells **17** and **23** have no text in their figures and are harmless either way.

## Decisions and doubts

**1. `k-Means` → `k-means`, and what to do with `10-Means`.** The German capitalises the
second half throughout (*k-Means*, *10-Means-Performance*). English writes **k-means**, and
that is also what the already-translated chapters use – `descriptive-statistics.md` once and
`statistical-models.md` four times, against one stray *k-Means* there. So every occurrence
in this chapter is lower-cased, including the plot titles ("Left: labels from k-means"). The
compound *10-Means-Performance* cannot survive as a compound: it became "the performance of
10-means as a classifier". If a consistency pass ever settles on *k-Means* instead, the
single leftover in `statistical-models.md` is the one to look at, not this chapter.

**2. *Unterscheidung* in the LDA paragraph (block c24.1).** The German says the groups'
optimal *Unterscheidung*, and then names the method *Linear Discriminant Analysis*. The
obvious English word is "discrimination", which would make the link to LDA explicit – but
"discrimination" in a data-science text reads first as the social sense, and the sentence
already carries the method's name two clauses later. I used **separation** ("for an optimal
separation of the groups", "the direction that allows the best separation") and let the name
*linear discriminant analysis* make the connection by itself. The pun the German does not
have is not lost; a pun the German *does* have is slightly muted. A human should decide
whether that trade is right.

**3. The three-step list (block c1.3) mixes method names and a translated noun.** Items 1
and 2 are **fit** and **transform** – they are Scikit-learn's method names, and the very next
paragraph says so (`PCA().fit(x)`, `pca.transform(x)`). Item 3 is **Dimensionsreduktion**,
which is not a method name but the thing `n_components` does. So the list ends up with two
untranslated English verbs and one translated noun, **dimensionality reduction**, exactly as
the German has two English verbs and one German noun. The mild oddity is the original's; I
kept it rather than inventing a fake API name for item 3 or translating `fit` and
`transform` into something Scikit-learn does not call them.

Smaller calls, for the record:

* **"die Identität, also die Einheitsmatrix"** (block c2.0) is a German doublet that English
  collapses into one word twice over. I wrote "was the identity map, that is, the identity
  matrix", which keeps two nouns where the German has two. "Identity, that is, the identity
  matrix" would have been a tautology on the page.
* **Scikit-Learn vs Scikit-learn.** The German spells it both ways – `Scikit-Learn` in
  blocks c1.4, c1.9, c2.17 and c25.5, `Scikit-learn` in c13.0, c13.1 and c18.0. I preserved
  each occurrence as the German has it rather than silently normalising; if the book wants
  one spelling, that is a whole-book decision, not a chapter one. (The library's own name is
  `scikit-learn`, all lower case.)
* **"MNIST" is not MNIST.** Block c16.1 and cell 17 call the data *the MNIST dataset of
  handwritten digits*, but the code loads `datasets.load_digits()`, which is the 8×8 UCI
  digits set, not the 28×28 MNIST. That is an error in the original and I translated it
  faithfully, heading included (*Application example: MNIST*). **A human should decide**
  whether the English edition quietly fixes it; if so, the `###` heading, the last sentence
  of c16.1 and nothing else need to change.
* **"eine Singulärwertzerlegung (die Zerlegung $C = TC' T^{-1}$)"** (block c2.17) calls an
  eigendecomposition an SVD. For a symmetric positive definite $C$ the two coincide, so the
  sentence is not wrong here, only loose; translated as is. Same for the claim that LAPACK
  "carries it out in two steps".
* **Maths left alone.** `Ker(M - \alpha Id)`, `\det(M - X Id)`, `Cov(X,Y)` and the `:name:`
  labels (`pca-case-a`, `pca-case-b`, `pca-variation`) are untranslated per TRANSLATION.md
  §3. `95\%` and `80\,\%` keep the source's spacing per §6.
* **Mechanical things.** Ten em dashes (blocks c1.3, c1.7, c1.8, c1.9, c6.2, c6.3, c15.1,
  c15.4) and five hyphen-as-dash cases (` - ` in c2.15, c13.1, c16.1, c24.1, c31.1) all
  became spaced en dashes. Four `{,}` decimal commas (`0{,}1^2`, `0{,}01`, `2{,}28` in the
  figure captions, `2{,}83` in block c6.3) became points. The German quotation marks around
  „Quadratische Abweichung" (block c15.1) became plain `"…"` and the section name became the
  English heading `expectation-variance.md` actually carries, *Squared deviation*. `d.h.` →
  "that is"; `z.B.` → "for example". The single-quoted German coinages – 'Standardisierung',
  'Normalisierung', 'Feature Scaling', 'rückgängig', 'Erfolgsbeispiel', 'echte' – keep their
  single quotes, which are already plain ASCII in the source.
* **Cross-reference link texts.** `[Multivariate Normalverteilung]` → **[Multivariate normal
  distribution]** (matches that chapter's translated H1 exactly), `[Erwartungswert und
  Varianz]` → **[Expected value and variance]** (likewise), `[Relative Entropie]` →
  **[Relative entropy]** (likewise). `[linearen Regression](linear-regression.ipynb)` →
  **[linear regression]**: that chapter is still German and its H1 is *Regressionsanalyse*,
  so a consistency pass should re-check this one once `linear-regression.ipynb` is
  translated – the glossary's row is *Regressionsanalyse → regression analysis*, and the
  German link text was already the short name, so I kept it short.

## Style pass

Markdown cells only; every code cell is byte-identical to `HEAD` (`check_untouched.py` passes
"prose only (with reordering)" – one sentence in the Definition block c2.3 now puts the
quantifier after the inequality, "**positive definite** if $v^\top C v > 0$ for all vectors
$v \neq 0$", which moves two formulas without changing either). `sync.py align`,
`check_english.py`, `nbtext.py check` and `nbtext.py syntax` are all clean. 45 of 69 non-code
blocks changed; no block merged, split or reordered. This chapter had the most German left in its
sentence shape, which is why the count is high; most edits are small.

Kinds of change:

* **German sentence shape.** "an unsupervised method in which a coordinate transformation is
  carried out on the data, so that the new coordinate axes are ordered according to where the data
  show the higher variance" → "an unsupervised method that applies a coordinate transformation to
  the data so that the new coordinate axes are ordered by how much variance the data show along
  them"; "To determine this matrix $\Sigma$ there is a very simple way if …" → "There is a very
  simple way to find this matrix $\Sigma$ if …"; "Suppose we had determined such a decomposition
  (one also says: …), then we can" → "Suppose we have found such a decomposition (also called …).
  Then we can"; "In the top row one can clearly see that" → "The top row clearly shows that";
  "Inductively we can now carry on and determine a matrix $M$" → "Carrying on inductively, we
  obtain a matrix $M$"; "These examples lead us to picture which matrix" → "These examples suggest
  asking which matrix".
* **"one" → "you".** "one rescales every variable … Likewise one shifts" → "you rescale … and
  likewise shift"; "one has to know the classes already – so, supervised learning" → "you have to
  know the classes already – which makes it supervised learning"; "the quantity with which one
  later decides" → "the quantity you later use to decide"; "first one determines the eigenvalues
  … and for every eigenvalue $\alpha$ one determines" → "first find the eigenvalues …, then for
  every eigenvalue $\alpha$ find"; "one would first have to cluster" → "you would first have to
  cluster".
* **Nominalisations and padding.** "We do not even have to go to the trouble of computing" → "We
  do not even have to compute"; "we have not yet established how" → "have not yet said how";
  "the inverse map … is then a transformation" kept; "which the code below also exploits" → "which
  the code below exploits too"; "it merely fluctuates very little" → "it just varies very little";
  "PCA turns this into a quantitative statement" → "PCA makes this quantitative"; "the fictitious
  covariance matrix" → "the made-up covariance matrix"; "So we have all the ingredients together"
  → "So we have all the ingredients"; "In the end the assumption of normality" → "In the end, the
  normality assumption" (the glossary's row from `expectation-maximization.ipynb`).
* **Clause order for English stress.** "here it is the *perpendicular* distance to the line that
  is minimised, whereas in regression it is the vertical distance in the direction of the target
  variable" → "…the vertical distance, in the direction of the target variable"; "rearranged
  therefore $C T = T C'$" → "or, rearranged, $C T = T C'$"; "Their share of the total variance
  $\operatorname{tr}(C) = \dots$, here therefore $2.75/4.25 \approx 65\%$ …, is called" → "…
  – here $2.75/4.25 \approx 65\%$ … – is called".
* **Terminology untouched.** *Principal component analysis* / *principal components* / *principal
  axes*, *change of basis*, *inner product*, *orthonormal basis*, *orthogonal complement*,
  *standard basis vector*, *eigenspace decomposition*, *eigendecomposition*, *explained
  variance*, *total variance*, *Gaussian elimination*, *characteristic polynomial*, *Rayleigh
  quotient*, *centre of mass*, *Centring*, *standardisation* / *normalisation* / *feature scaling*
  in the German's single quotes, *distortion* (c25.2, kept as the noun), *back-transformation*,
  *compress / stretch / shear*, *k-means* lower case, *linear discriminant analysis (LDA)*,
  *Gaussian mixture models* – all as the glossary fixes them. Scikit-Learn / Scikit-learn kept
  per occurrence as the German has it.

Noticed but not touched:

* **MNIST** (heading c16.0 and the last sentence of c16.1) is still "the MNIST dataset of
  handwritten digits" for data that are `load_digits()`. Recorded in `UPSTREAM-NOTES.md`; not
  fixed here, per the brief.
* **"we can draw a circle around the 95\% quantile"** (c1.14) has a LaTeX-escaped per cent
  sign *outside* maths mode. CommonMark swallows the backslash, so it renders correctly, but it
  is a TeX habit in prose and `TRANSLATION.md` §6 wants a bare `95%` there. The German has it the
  same way; left for a human to decide, since the translator chose to keep the source's spacing.
* **"rotate about any axis by an angle"** (c1.9) is a slightly odd quantifier; "by any angle"
  would be the natural English, but it is a (harmless) strengthening of the German, so left.
* **"the Iris data"** (c24.1) is capitalised where `kmeans.ipynb` writes "the iris data" in
  prose; the plot titles in both chapters say "Iris dataset". A whole-book consistency call.
* **c2.17** still calls the eigendecomposition "a singular value decomposition", and **c1.15**
  says "the symmetric situation is all we need" – both loose rather than wrong, as the
  translation notes already say.
