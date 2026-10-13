# Translator's notes: `expectation-maximization.ipynb`

German original `expectation-maximization.ipynb` (ds-skript `c7247a9`), 65 cells, 185 blocks,
1 declared drop (the two HHU lecture recording links under the H1, block `c0.1`),
184 translated blocks. No further drops, no `sync/additions` entry, one `sync/check-ignore`
entry (a false positive, see below).

Checks: `nbtext.py check` round-trips cleanly, `sync.py align` reports 184 blocks aligned,
`check_english.py` is clean, `grep -c '{,}'` is `0`. `nbtext.py syntax` reports two cells
that do not compile – **this is pre-existing and not caused by the translation**; see
*Decisions and doubts* §1.

The chapter references no images, so there is nothing to redraw. It shares
`fashion_mnist.py` with `model-selection.ipynb`; that file is already entirely English
(docstrings, comments, the `load_mnist` docstring) and needs no change.

## New terminology

The chapter builds on `statistical-models.md` and `multivariate-normal.ipynb`, whose rows
(EM algorithm, expectation maximization algorithm, mixture model, mixture distribution,
maximum likelihood estimator/principle, likelihood function, log-likelihood, latent
variable, centroid, exponential family, closed formula, covariance matrix, inner product,
homoscedasticity, convex combination, relative entropy, cross-entropy, loss function,
quality of the model, subset of the data, one-hot encoding, rule of thumb) I took over
unchanged. New decisions:

| German | English | Note |
|---|---|---|
| Aufenthaltsort | whereabouts | the GPS dataset's heading *Aufenthaltsorte* → *Whereabouts*; "die längeren Aufenthaltsorte" → "the places where the longer stays happened" |
| Anwendungsbeispiele | Example applications | the `##` heading before the three datasets |
| Bayessches Informationskriterium (BIC) | Bayesian information criterion (BIC) | the German adjective is *Bayessch*, not *Bayes'sch*; English has the standard name |
| Clustermittelpunkt, Clusterzentrum | cluster centre | British spelling; distinct from *Zentroid* → centroid, which the same cell also uses |
| Entstehungsprozess | generative process | "one can picture the generative process like this"; follows *datenerzeugende Verteilung → data-generating distribution* in `covariance.md` |
| erwartete vollständige-Daten log-Likelihood | expected complete-data log-likelihood | $Q(\theta,\theta)$ |
| fette $1$ | fat $1$ | the trick of multiplying in a cleverly written $1$; twice, blocks c9.8 and c11.6 – see *Decisions* |
| Fitness-Funktion | fitness function |  |
| Hauptachsentransformation | principal axis transformation | the glossary has *Hauptkomponentenanalyse → principal component analysis*, which is not the same word |
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

Cross-reference link texts: `[Relative Entropie](relative-entropy.md)` → **[Relative entropy]**,
matching that chapter's translated H1 exactly. That is the chapter's only internal link; the
one external link (the GPS blog post) is English already.

## Code changes

**German identifiers renamed: none.** Every identifier in the notebook was already English
(`EM`, `EMmulti`, `taus`, `pis`, `mus`, `sigmas`, `Npis`, `component1_sample`,
`mixture_samples`, `norm_pdf_domain`, `init_theta`, `em_iteration_draw`, `plot_ani`,
`history`, `max_iter`, `tol`, `real_mu_1`, `plot_digits`, `so_many_rows`,
`new_data_in_old_coordinates`, `gm`, `gm7`, `vargoal`, `show_fashion_image`,
`fashion_data`, `draw_gm_sample`, `highres_pca`, `highres_data`, `highres_gm`,
`x_wrongs`, `y_pred_bestperm`, `best_accuracy`). Library names and keyword arguments are
untouched. Nothing to grep for, and nothing survives: a scan for ä/ö/ü/ß over the whole
export comes back empty.

What changed in code is comments and strings only, in cells 17, 19, 20, 21, 22, 24, 26, 28,
33, 37, 39, 43 and 54. A cell-by-cell diff against the German export confirms that no
statement, expression, argument or line of logic was altered, and the only whitespace change
is none at all – the trailing whitespace the German code carries was restored line for line.

* **Comments.** Cell 17: `# Variante für univariate Gausssche Mischungen, / # nicht-vektorisiert
  (für das bessere Verständnis)` → `# version for univariate Gaussian mixtures, / # not
  vectorised (for the sake of understanding)`; `#(E)-Schritt` / `#(M)-Schritt` → `#(E) step` /
  `#(M) step` (cell 24 has the spaced variant `# (E)-Schritt` → `# (E) step`, kept spaced as
  the German has it). Cell 20: `# Initiale theta aufstellen:` → `# set up the initial theta:`.
  Cell 21: `# Darstellung der echten Parameter vs. die initialen:` → `# the true parameters
  vs. the initial ones:`. Cell 22: the two-line comment about the PNG still image → `# Output
  the last frame as a PNG as well: the web export shows the video, / # the PDF export (which
  cannot do HTML) uses the still image.` Cell 33: `# Zum Darstellen in Hauptkomponenten
  transformieren:` → `# transform to principal components for plotting:`; `# Fit mit
  E-M-Algorithmus:` → `# fit with the EM algorithm:`. Cell 39: `# Wir betrachten direkt die
  Marginalverteilungen / # in den ersten 2 Hauptkomponenten:` → `# we look directly at the
  marginal distributions / # in the first 2 principal components:`. Cell 54: the three-line
  comment about `fashion_mnist.py` (its wording now matches that file's own English
  docstring).
* **Already-English comments left alone**, per the brief: `# work in principal components, to
  plot later in the first two:` and `# for simplicty, take only first 2 PCs here:` (cell 4,
  typo and all), `# compute new log-likelihood:` (17), `# a better way would be:` and
  `# record all values in each iteration step for plotting:` (22), the `"""vectorized E-M for
  multivariate Gaussian mixtures"""` docstring (24, American `-ize` kept), `# keep so much of
  variance` (41), `#im.set_clim(0, 16)` (45), `#im.set_clim(0, 255) # gets computed by
  matplotlib anyway` (56).
* **Legend entries and axis labels.** Cell 19: `"gewichtete Summe"` → `"weighted sum"`,
  `"Komponente 1"/"Komponente 2"` → `"component 1"/"component 2"`, `"Dichte"` → `"density"`.
  Cell 21: `"Daten"` → `"data"`, `"Schätzung Mischung"` → `"mixture estimate"`,
  `'wahres $\mu_1$'/'wahres $\mu_2$'` → `'true $\mu_1$'/'true $\mu_2$'`, `"Dichte"` →
  `"density"`. Cell 22: `"Daten"` → `"data"`, `"Als 0 klassifiziert"` → `"classified as 0"`,
  `"Schätzung Nr. %d"` → `"estimate no. %d"`, `"Echte Verteilung"` → `"true distribution"`,
  `"Dichte"` → `"density"`. Cell 39: `'Daten'` → `'data'`, `'Fehlklassifiziert'` →
  `'misclassified'`. Cell 43: `"Anzahl Komponenten k"` → `"number of components k"`,
  `"BIC (kleiner ist besser)"` → `"BIC (smaller is better)"`.
* **Plot titles.** Cell 26: `"Zu clusternde Daten"` → `"data to be clustered"`. Cell 28:
  `"Zu clusternde Daten in Hauptkomponenten"` → `"data to be clustered, in principal
  components"` (lower case following the German's own sentence case elsewhere in the
  notebook, and the comma added because the English reads as a list without it).
* **`print` strings.** Cell 37: `"Genauigkeit: %2.f%%"` → `"Accuracy: %2.f%%"`. Cell 43:
  `"kleinstes BIC bei k ="` → `"smallest BIC at k ="`. The `print`s in cells 33, 41 and 59
  were English already.

The code was **not** re-executed, per instructions.

**For the re-execution pass:** the stored outputs are still the German ones and *must* be
regenerated. German stream output survives in cells 37 (`Genauigkeit: …`) and 43
(`kleinstes BIC bei k = …`), and German text is baked into the figures of cells 19, 21, 22
(the HTML5 video *and* the PNG still), 26, 28, 43 and 39. Cells 30, 45, 46, 48, 50, 52, 61
and 63 have no text in their figures. Expect this notebook to be among the slowest: cells
58, 60, 62 and 63 fit PCA and 50–90-component Gaussian mixtures on 60,000 Fashion-MNIST
images, and cell 22 renders an HTML5 video of up to 210 EM iterations (`ffmpeg` needed).

## Decisions and doubts

**1. `nbtext.py syntax` reports two cells that do not compile – pre-existing, not mine.**
Cells 58 and 63 fail with `invalid syntax`:

```
cell 58: invalid syntax (line 3)      # %timeit pca.fit(x_train)
cell 63: invalid syntax (line 2)      # %time highres_gm.fit(highres_data[y_train == 1])
```

These are IPython line magics. `nbtext.py syntax` skips a cell only when its *first*
non-whitespace character is `%` or `!`; in both of these cells the magic sits on a later
line, after an ordinary assignment, so the cell is handed to `compile()` and rightly
rejected. Running the same check on the German original
(`git -C ../ds-skript show c7247a9:expectation-maximization.ipynb`) prints the **identical
two findings**, so the translation introduced nothing: the notebook is valid IPython and
invalid plain Python, exactly as it was. I did not touch those lines, and I did not touch
`tools/`. **A human has to decide** whether `syntax()` should strip magic lines before
compiling (one-line change: skip lines matching `^\s*[%!]`), or whether these two cells
should be listed as known exceptions somewhere. As it stands, this chapter can never make
all four checks print zero.

**2. *Klasseneinteilung* (11 occurrences, blocks c1.0, c3.2, c5.1, c5.2, c5.3, c5.4, c14.3) → "division into classes".** German has one noun
for "the partition of the data into classes", and English has no single idiomatic word:
"classification" is taken (the chapter uses *Klassifikation* separately, for predicting a
label), "clustering" is the glossary's word for *Klassenbildung*, "class assignment"
collides with the **soft/hard assignment** pair that block c14.3 makes a term of art, and
"labelling" imports an idea the German does not have here. So: "division into classes"
throughout, which is clunky but stable and never ambiguous – "a new division into classes",
"the division into classes which the mixture model lets us compute", "quantifying how
certain we are about the division into classes". The one exception is block c14.3, "für
jede mögliche Klasseneinteilung eines Punktes $x_i$", where the German means the class of a
single point, not a partition of the dataset: there it reads "for every possible class of a
point $x_i$". A style pass may want to shorten the other ten; if so they should move
together, and the glossary row above should move with them.

**3. *Sample-Erwartungswert* → "sample expected value" (block c2.1).** The German writes
*Sample-Kovarianz und Sample-Erwartungswert* for what is plainly the empirical mean and the
empirical covariance of a subset of the data. Three renderings were available and all three
are already in the book: `multivariate-normal.ipynb` says "empirical mean", the glossary
binds *Stichprobenmittel* → **sample mean**, and `expectation-variance.md` has
*Sample-Standardabweichung* → **sample standard deviation**. I followed the last of these,
because it is the same `Sample-` prefix and because the glossary binds *Erwartungswert* →
**expected value**, so "sample expected value" is the composition of two binding rows. It
reads a shade stiffer than "sample mean" would. If a human prefers readability here,
"sample mean" is the alternative, and it would then be worth a glossary row saying that
*Sample-Erwartungswert* and *Stichprobenmittel* both land on it.

Smaller calls, for the record:

* **`## Auxiliary Functions` left verbatim.** The German heading is already English, in title
  case, and the brief says to leave already-English code and text alone. Every other heading
  in this notebook is sentence case, so this one sticks out. Normalising it to *Auxiliary
  functions* would be a one-character improvement to the original; I did not make it.
* **`ax.set_title("mixed Gaussian model, sklearn EM-fit")` left verbatim** (cell 39), for the
  same reason: it was already English in the German. It is the one place in the chapter that
  says "mixed Gaussian model" where the prose everywhere else says "Gaussian mixture model".
  Worth a consistency fix by a human, not by me.
* ***Iversen-Bracket* → "Iverson bracket"** (block c11.3). The German misspells Kenneth
  Iverson's name. A proper name is not translated but it is also not a place to preserve a
  typo, so I corrected it silently; flagging it here in case the German should be fixed
  upstream too.
* ***responsibilites oder Verantwortlichkeiten* → "the responsibilities"** (block c11.13).
  The German introduces the term with the English loanword (misspelled) *and* its German
  equivalent, and the following clause plays on the German one ("denn sie sind …
  verantwortlich für"). In English the doublet collapses to one word and the pun survives
  intact: "we call the terms denoted $\tau_{ij}$ the **responsibilities**, for in our model
  they are responsible for the division of the points $x_i$ into classes". Later mentions in
  blocks c12.3 and c12.4, where the German alternates between the two words, are both
  "responsibilities".
* **"fat $1$"** for *fette $1$* (blocks c9.8 and c11.6). The German idiom is the
  mathematician's "multiply in a cleverly written 1". English lecturers say "a fancy 1", "a
  sneaky 1", or just "multiply by $q(j)/q(j)$". I kept the German's own adjective because it
  is used twice and the second use ("in the first step we inserted a fat $1$") refers back to
  the first; losing the word would lose the callback. If a human finds it too German, both
  occurrences change together.
* **"stopgap"** for *behelfsmäßig so zu tun als sei* (block c10.1). The German adverb says
  "as a makeshift"; "we can try a stopgap: pretend that $\theta$ is constant…" keeps that
  apologetic note, which the whole section then earns back.
* **Mechanical things.** `d.h.` → "that is" / "which is to say"; `z.B.` → "say" / "for
  instance" (post-posed); `bzw.` → "or rather" / "and … alike", depending on which of its two
  senses is meant. Six hyphens-as-dashes (` - ` in blocks c1.0, c5.1, c6.0 twice, c12.5, c25.2, plus the
  unspaced `gibt- auch` in block c14.5) and one `--` (block c3.1) became spaced en dashes per
  `TRANSLATION.md` §6; the range `0--9` in block
  c47.0 became `0–9`, matching the ranges in `descriptive-statistics.md`. The German hard line
  breaks (trailing double spaces) in the cell 1 admonition are preserved exactly.
  `Vorlesung *Einführung in Deep Learning*` → "the course *Introduction to Deep Learning*",
  matching `numpy.ipynb` and `multivariate-normal.ipynb`. `Skript` → "these notes", per the
  glossary. `Scikit-learn` → `scikit-learn` (the project's own spelling). `Ausblick (nicht
  klausurrelevant)` → "Looking ahead (not part of the course proper)", and the trailing "wird
  im Kurs nicht abgefragt" → "is not needed in the course", matching the parallel `:::{note}`
  in `statistical-models.md`.
* **One `check_english.py` finding, recorded in `sync/check-ignore/`.** Block c25.2, "German
  function word": the licence name **MIT** in "the data come under the MIT licence" matches
  the German *mit* case-insensitively. A proper name, so it stays.
