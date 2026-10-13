# Translator's notes: `model-selection.ipynb`

German original `model-selection.ipynb` (the filename is the same in both editions, per
`sync/filemap.json`), **46 cells, 92 blocks → 92 blocks**. **No drops**: this chapter is one
of the few with no HHU Mediathek link under the H1, so there was nothing to drop and no
`sync/drops/model-selection.ipynb.json` was created. No `sync/additions` entry, and no
`sync/check-ignore` entry – `check_english.py` reports zero findings.

`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass, and
`grep -c '{,}'` is `0` (it was already `0` in the German – the notebook has no German decimal
commas anywhere, in prose or in code).

The notebook was **not** re-executed. The stored outputs of cell 14 (`Anzahl Cluster:` /
`Anzahl Klassen:`) and cell 39 (`f1_macro (Kreuzvalidierung auf der Teilstichprobe) =`) still
carry the German `print` strings, and the stored figures of cells 24 and 26 still have the
German axis labels `Blütenblattbreite (gemessen)` / `(vorhergesagt)` baked into the PNG.
That is the expected state before the central re-execution pass; it takes roughly four
minutes for this notebook, and cell 29 downloads the four Fashion-MNIST files on first run.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | Note |
|---|---|---|
| Modell-Auswahl | model selection | already in `TERMINOLOGY.md`; recorded because it is this chapter's title |
| Training, Test und neue Daten | Training, test and new data | the `##` heading – see *Decisions* 1 |
| Training, Validation und Test | Training, validation and test | the `###` heading |
| k-fold Cross Validation | k-fold cross-validation | heading; the German is already English but German-capitalised and unhyphenated – see *Decisions* 2 |
| Zeitreihen-sensible Kreuzvalidierung | Time-series-aware cross-validation | heading; see *Decisions* 3 |
| Visualisierung der Kreuzvalidierungsstrategien | Visualising the cross-validation strategies | heading |
| Bewertung (der Modellperformance / von Clustering / einer Regression) | assessing | the three `Bewertung …` headings become *Assessing model performance*, *Assessing a clustering*, *Assessing a regression*; "evaluation" was the alternative – see *Decisions* 4 |
| Bewertungsfunktion | scoring function | what `scoring=` takes; "evaluation function" reads less like scikit-learn |
| Hyperparametersuche | hyperparameter search | the `##` heading |
| Gittersuche | grid search | the `###` heading; matches `GridSearchCV` |
| Randomisierte Suche | Randomised search | house `-ise` spelling, even though the class is `RandomizedSearchCV` |
| Anwendungsbeispiel | an example application | the `##` heading *An example application: Fashion MNIST*; `TERMINOLOGY.md` has *Durchgerechnetes Beispiel* → *a worked example*, which is a different German phrase |
| Fold, Falte | fold | the German uses the English *folds* in c4.3/c6.1 and the German *Falte* in c38.1; one English word |
| stratifizierte k-fache Kreuzvalidierung | stratified k-fold cross-validation |  |
| leaken, Information Leakage, Informationsleck | to leak, information leakage | the German glosses the English with the German *ein Informationsleck*; the gloss collapses – see *Decisions* 5 |
| Test-Datensatz, Trainings-Datensatz, Validation-Datensatz | test set, training set, validation set | follows `descriptive-statistics.md`'s *Testdatensatz-Performance* → *performance on the test set*; `TERMINOLOGY.md` already binds *Testdaten/Trainingsdaten* → *test data / training data*, which is used where the German says *Daten* |
| gelabelt / ungelabelt | labelled / unlabelled | British double-l; *Label* → *label* was settled in `titanic-eda-numpy.ipynb` |
| generalisieren, verallgemeinern | to generalise | the German uses both verbs for the same thing |
| Homogenität / Vollständigkeit (Completeness) | homogeneity / completeness | the German switches between *Vollständigkeit* and the English *Completeness*; English has one word, which is also the scikit-learn name |
| V-Maß | V-measure | `v_measure_score` |
| normalisierte gemeinsame Information | normalised mutual information | `TERMINOLOGY.md` binds *gemeinsame Information* → *mutual information* (from `relative-entropy.md`); "normalised" in house spelling, even though the scorer is `normalized_mutual_info_score` |
| permutationsinvariant | permutation-invariant |  |
| Klassifikationsgüte | classification quality | follows the glossary's *Güte* → *quality* |
| Ground Truth | ground truth | lower case, as `sync/notes/titanic-eda-numpy.ipynb.md` asked this chapter to do |
| F1-Score | F1 score | two words, no hyphen, as `titanic-eda-numpy.ipynb` asked; the scikit-learn output column `f1-score` in block c19.0 stays literal because it is program output |
| Summe der Residuenquadrate | residual sum of squares | `TERMINOLOGY.md` has *Residuen* → *residuals* only |
| Bestimmtheitsmaß / $R^2$-Wert | $R^2$ value | the chapter only uses *$R^2$-Wert*; `linear-regression.ipynb` (still German) carries *Bestimmtheitsmaß* and will need *coefficient of determination* |
| Kernel-Ridge-Regression | kernel ridge regression | no hyphens in English; `KernelRidge` |
| Kernelbreite | kernel width | the RBF $\gamma$ |
| Regularisierungskonstante / Regularisierungsparameter | regularisation constant / regularisation parameter | the German distinguishes the two words, so English does too |
| Hauptkomponenten | principal components | `TERMINOLOGY.md` has *Hauptkomponentenanalyse* → PCA, not the components |
| Einheitsvarianz | unit variance | `StandardScaler` |
| log-gleichverteilt | log-uniformly | `loguniform`; the glossary's *Gleichverteilung* → *uniform distribution* |
| Teilstichprobe | subsample | one word; the glossary's *Stichprobe* → *sample* |
| Pixelsummen | pixel sums |  |
| Hyperparameter-Finetuning | hyperparameter fine-tuning |  |
| Black Box | black box | two words in English |
| Support Vector Classification | support vector classification | lower case in running prose; `SVC` and `SVM` stay upper case |
| drop-in Ersatz | drop-in replacement |  |
| Suchstrategie | search strategy |  |
| Setting | setting | the German already uses the English word |
| Treibhausgase | greenhouse gases |  |
| T-Shirts, Hosen | T-shirts, trousers | British "trousers" |
| Lader | loader | the code comment in cell 28 |

Reused unchanged from the already-translated chapters: *Kreuzvalidierung* →
**cross-validation**, *Overfitting* → **overfitting**, *Konfusionsmatrix* → **confusion
matrix**, *Kennzahlen* → **summary measures**, *Merkmale* → **features**,
*Target-Variable* → **target variable**, *Blütenblattbreite* → **petal width**,
*Instanz* → **instance**, *Klassifikator* → **classifier**, *Teildatensatz* → **subset of
the data**, *Relative Entropie* → **[Relative entropy](relative-entropy.md)**, *Beispiel*
(admonition) → **Example**.

Cross-chapter link text: `[Relative Entropie](relative-entropy.md)` →
`[Relative entropy](relative-entropy.md)`, and `[Titanic EDA](titanic-eda-numpy.ipynb)` keeps
its short form (the English chapter's H1 is *Titanic EDA, a first pass*, but the German
already dropped the subtitle in the link text, so nothing changed there). Both link targets
already pointed at the English filenames. "siehe Kapitel Kernel-Methoden" → "see the chapter
Kernel methods" – that is plain prose, not a link, and `kernel-methods.ipynb` is still German,
so no target was invented.

## Code changes

### Identifiers renamed

**None.** Every identifier in this notebook was already English: `x_reg`, `y_reg`,
`param_grid`, `param_dist`, `grid_search`, `random_search`, `est`, `reg`, `pipe`, `dims`,
`small_x`, `small_y`, `best`, `train_i`, `test_i`, `test_x`, `test_y`, `pca`, `pca2`,
`x_train_pc`, `x_test_pc`, `x_train_pc2`, `x_test_pc2`, `svc`, `y_pred`, `imscatter`,
`artists`, `results`, `y_wrong_indices`, `y_wrong`, `x_wrong`. The German invents no
DataFrame column names either – the only column names in the code are the scikit-learn ones
(`param_svc__C`, `param_svc__gamma`, `mean_test_score`) and the keys of `param_grid` /
`param_dist`, which are scikit-learn parameter names and had to stay byte for byte.

### Strings, comments and figure text

* **`print` strings**: cell 14 (`"Anzahl Cluster:"` → `"Number of clusters:"`,
  `"Anzahl Klassen:"` → `"Number of classes:"`) and cell 39
  (`"f1_macro (Kreuzvalidierung auf der Teilstichprobe) ="` →
  `"f1_macro (cross-validation on the subsample) ="`). Every other `print` in the notebook
  (`"mean of class label:"`, `"The following %d numbers should be quite similar:"`,
  `"Homogeneity:"`, `"Completeness:"`, `"best parameters:"`, `"r2 ="`, `"NMI = %.2f"`) was
  already English.
* **Comments**: cell 24 (`# Regression: Blütenblattbreite (Spalte 3) aus den drei anderen
  Merkmalen`), cell 28 (the three-line note about the loader) and cell 43
  (`# Pipeline mit den besten Parametern`). `# trim down some more dimensions to speed this
  up:` in cell 33 and `# plot every 2nd:` in cell 37 were already English.
* **Figure text**: the axis labels in cells 24 and 26,
  `"Blütenblattbreite (gemessen)"` → `"petal width (measured)"` and
  `"Blütenblattbreite (vorhergesagt)"` → `"petal width (predicted)"` – four occurrences, the
  same pair in both cells, all grepped. The titles in cells 35 and 44 (`"Correct labels"`,
  `"SVM result"`, `"Wrong class"`) were already English. These figures are generated by the
  notebook, so they need no entry in `images/README.md`; they will be correct after the
  re-execution pass.
* **Image markdown**: in block c1.4 the alt text became `Hyperparameter tuning` and the
  *title* attribute (the tooltip, which is visible to the reader) was translated:
  `"Splitten der Daten zur Bewertung von Modellen"` → `"Splitting the data in order to
  assess models"`. The four PNGs themselves – `grid_search_workflow.png` and the three
  `sphx_glr_plot_cv_indices_*.png` – come from the scikit-learn documentation and carry
  English text already, so nothing needs redrawing. The alt texts `KFold`,
  `StratifiedKFold`, `TimeSeriesSplit` and `Fashion MNIST` are code and product names and
  stayed as they are.
* **Maths**: the two display-math blocks (c10.3, c21.3) contain no German;
  `\texttt{mean}` is a function name and was left alone.
* **`scikit-learn`** is spelled lower case in all four places (blocks c1.5, c8.4, c9.1 and
  the one in c23.2's neighbourhood), including where the German capitalises it
  (`Scikit-Learn-Dokumentation`, `Mit Scikit-learn`). This follows
  `titanic-eda-numpy.ipynb`.

## Decisions and doubts

**1. `## Training, Test und neue Daten` → `## Training, test and new data`.** This is the
heading `titanic-eda-numpy.ipynb` was asked about: its block c22.1 sends the reader to this
chapter "under *train-test split*", and `sync/notes/titanic-eda-numpy.ipynb.md` §4 noted that
no section of that name exists and asked whether this translation would create one. **I did
not.** The German heading names three things (training, test, *and new data*) and the whole
point of the section is the third one – the unlabelled data that arrive after training – so
renaming it "Train-test split" would have thrown away the part of the heading that carries
the section's argument. The concept *train-test split* is introduced inside this section
(block c1.3, `train_test_split`), so the cross-reference is not broken; it just names a
concept rather than a heading. **If a human prefers a re-pointable target**, the cheapest fix
is to leave this heading alone and change `titanic-eda-numpy.ipynb` c22.1 to point at
*Training, test and new data*. That is a one-block edit in the other chapter and I did not
make it, since I may touch only my own notebook.

**2. `### k-fold Cross Validation` → `### k-fold cross-validation`.** The German heading is
already English, but with German noun capitalisation and no hyphen. `TERMINOLOGY.md` binds
*Kreuzvalidierung* → *cross-validation* with the hyphen, and the body of the same cell says
*k-fache Kreuzvalidierung*, so leaving the heading as "Cross Validation" would have the
chapter spelling the same word two ways on consecutive lines. Same for
`### Stratified k-fold Cross Validation`. The lower-case `k` is the German's own and matches
`kmeans.ipynb`'s `# k-Means`.

**3. `### Zeitreihen-sensible Kreuzvalidierung` → `### Time-series-aware
cross-validation`.** *sensibel* here means "that takes account of", not "sensitive to";
"time-series-sensitive" would read as the opposite (a method that is *affected* by the time
order rather than one that *respects* it). "Cross-validation for time series" was the other
candidate and is smoother English, but it loses the German's point that it is the method
which is aware, not the data which are special. Flagged for the style pass.

**4. *Bewertung* → "assessing", not "evaluation".** The three headings become *Assessing
model performance*, *Assessing a clustering*, *Assessing a regression*, and
*Bewertungsfunktion* → *scoring function*. "Evaluation" is what the machine-learning
literature says, and a reader coming from scikit-learn will meet "model evaluation" in the
user guide. I chose "assessing" because `TERMINOLOGY.md` already binds *Güte* → *quality*
and the book's own voice in `statistical-models.md` says "criteria for the quality of
models"; "assess the quality" then reads as one book. **A human may reasonably overrule
this**: it is five headings plus two prose occurrences, and if "evaluation" wins,
*Bewertungsfunktion* should stay *scoring function* regardless, because that is what
`scoring=` is called.

**5. The *Information Leakage / Informationsleck* doublet collapses (block c3.1).** The
German writes "dass der Test-Datensatz **leakt** (Information Leakage, ein Informationsleck)"
– the English term of art, then a German gloss of it. In English the bracket would read
"(information leakage, an information leak)", which says the same thing twice, so it became
"(information leakage)". This follows the *Störvariable/Confounder* precedent in
`descriptive-statistics.md` and the *Accuracy (Treffergenauigkeit)* precedent in
`titanic-eda-numpy.ipynb`. Nothing crossed a block boundary.

**6. *Die Vorlesung "Einführung in Deep Learning"* (block c3.4) keeps its German name and
gained a gloss.** TRANSLATION.md §3 keeps lecture titles in German, and `landing-page.md` and
`intro-python.ipynb` both keep *Einführung in Python* that way. So: "The lecture course
*Einführung in Deep Learning* (introduction to deep learning) takes … as known." No link
exists in the German, so no "(in German)" marker was needed.

**7. `60000` → `60,000` (block c38.1).** The German writes the figure without a separator;
TRANSLATION.md §6 asks for the English thousands comma, so the English reads "all 60,000
images". The `60000`/`10000` inside `fashion_mnist.py`'s docstring are in a file I may not
touch (see below).

**8. `fashion_mnist.py` still contains German and I did not touch it.** Two places, both
docstrings, both visible to a reader who runs `help(load_mnist)` or opens the file from the
notebook's own comment in cell 28:

* the module docstring, all four lines: *"Fashion-MNIST laden (gemeinsam genutzt von
  model-selection.ipynb und expectation-maximization.ipynb). Die vier Dateien werden nur
  beim ersten Aufruf heruntergeladen (per https vom GitHub-Repository von Zalando Research)
  und danach aus dem Arbeitsverzeichnis gelesen. Format: IDX, siehe …"*
* the `load_mnist` docstring: *"kind: 'train' (60000 Bilder) oder 't10k' (10000 Bilder). Gibt
  (images, labels) zurück."*

Suggested English, for whoever owns that file – it is shared with
`expectation-maximization.ipynb`, so one of us has to do it and neither should do it twice:
"Load Fashion-MNIST (shared by model-selection.ipynb and expectation-maximization.ipynb). The
four files are downloaded on the first call only (over https from Zalando Research's GitHub
repository) and after that read from the working directory. Format: IDX, see …" and
"kind: 'train' (60,000 images) or 't10k' (10,000 images). Returns (images, labels)."
No identifier in the file is German (`load_mnist`, `load_mnist_images`, `load_mnist_labels`,
`_fetch`, `BASEURL`), so the notebook's `from fashion_mnist import load_mnist` is unaffected
either way.

**9. `## Anwendungsbeispiel: Fashion MNIST` → `## An example application: Fashion MNIST`.**
`TERMINOLOGY.md` has *Durchgerechnetes Beispiel* → *a worked example* from
`descriptive-statistics.md`, and it was tempting to reuse it. But the German word here is a
different one, and this section is not a worked calculation – it is the chapter's methods
applied to a real dataset. "An example application" keeps that distinction.

**10. Two small liberties inside blocks, both deliberate.** In c10.2's first bullet the
German's long "Bei gleicher Zuordnung der Label, also wenn … dann haben wir verglichen" got
an em-dash-free parenthetical with spaced en dashes, which is what TRANSLATION.md §6 asks
for; and c19.0's "nur je Klasse statt einmal" became "only one set per class instead of one
overall", because the bare "instead of once" is opaque in English. Both stayed inside their
blocks.

**11. For the human reviewer, in order of risk:** (a) decision 1 – whether this chapter
should grow a heading called "Train-test split" so that `titanic-eda-numpy.ipynb` can point
at it, or whether that chapter's sentence should be re-pointed at *Training, test and new
data* instead; (b) decision 4, *assessing* versus *evaluation*, which sets five headings;
(c) the German in `fashion_mnist.py` (decision 8), which belongs to nobody at present;
(d) the stored outputs of cells 14 and 39 and the figures of cells 24 and 26 are still
German, so the re-execution pass must actually reach this notebook – it needs network access
on the first run, because cell 29 downloads four files from GitHub.
