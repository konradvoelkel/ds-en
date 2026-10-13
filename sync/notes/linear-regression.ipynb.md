# linear-regression.ipynb

German original: `lineare-regression.ipynb` (ds-skript `c7247a9`). 56 cells, 117 blocks
after the declared drop. H1 *Regressionsanalyse* → **Regression analysis**, which is the
link text the other chapters already use.

## New terminology

Proposed for `TERMINOLOGY.md`, section heading *Regression and regularisation*.

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
| einfache / multiple lineare Regression | simple / multiple linear regression | |
| Einflussgröße | explanatory variable | the counterpart of the glossary's *Zielgröße* → target variable; "regressor" is reserved for the German's own parenthetical *(Regressor)* |
| Formfaktor | shape factor | petal area as length × width "up to a shape factor" |
| Gerade minimalen Abstands | Line of minimal distance | plot legend, kept literal; the prose word is *line of best fit* |
| kleinste Quadrate, kleinste-Quadrate-Schätzer | least squares, least squares estimator | `## Kleinste Quadrate` → `## Least squares` |
| L1-/L2-Regularisierung, L1-/L2-Norm | L1 / L2 regularisation, L1 / L2 norm | no hyphen before the numeral in English |
| Lasso-Regularisierung | lasso regularisation | lower case in running prose, as with *bootstrap* in `statistical-tests.md` |
| Link-Funktion | link function | logistic regression's $\sigma$ |
| One-Hot-Encoding | one-hot encoding | already in `descriptive-statistics.md`; recorded again because it is an `###` heading here |
| polynomiale Regression | polynomial regression | |
| Referenzkategorie | reference category | the level `drop_first=True` leaves out |
| Regressand | regressand | stays; paired with *Regressor* → regressor |
| Regressionsgerade / Regressionskurve | regression line / regression curve | plot legends |
| Regularisierung | regularisation | `##` heading; house `-ise` spelling |
| Reihenhaus / Wohnung (`Type`) | townhouse / unit | the Melbourne `Type` codes; *unit* glossed once as "that is a flat", since the Australian word is not obvious |
| Residuenquadratsumme | residual sum of squares | not "sum of squared residuals"; `Residuen` → residuals is already in the glossary |
| Ridge-Regression | ridge regression | lower case in running prose |
| Störgröße | error term | the unobservable $\epsilon$, as against the observable residual – see *Decisions* |
| Strafterm, Strafe | penalty term, penalty | `Die L1-Strafe` → "the L1 penalty" |
| Stützstelle | support point | see *Decisions* |
| weight decay | weight decay | the German already uses the English |
| Zusammenfassung | Summary | `##` heading; matches the translated notebooks |

Reused without change, for the record: *Punktwolke* → cloud of points, *Faustregel* → rule
of thumb, *Ecke (des L1-Balls)* → vertex, *Ausprägung* → level, *nominalskaliert* → on a
nominal scale, *Skalenniveau* → level of measurement, *Overfitten* → overfitting,
*Gewichte* → weights, *Zusammenhang* → relationship, *Zentroid* → centroid.

Cross-reference link texts follow the ones already in the book: `[Covariance](covariance.md)`,
`[Covariance and dependence](covariance.md)`, `[Descriptive statistics](descriptive-statistics.md)`,
`[Model selection](model-selection.ipynb)`.

## Code changes

Identifiers renamed (each grepped across the whole notebook; none is used outside its own cell):

| German | English | cell |
|---|---|---|
| `iris_daten` | `iris_data` | 1 |
| `gerade` | `line` | 1 |
| `flaeche` | `petal_area` | 18 |
| `kelchlaenge` | `sepal_length` | 18 |
| `ergebnis` | `result` | 18 |

`petal_length`, `petal_width`, `beta_0`, `beta_1`, `x_centered`, `y_centered`,
`regressor_columns`, `poly_fit`, `phi` and the rest were already English.

Strings and comments translated:

* axis labels `"Blütenblattlänge (cm)"` / `"Blütenblattbreite (cm)"` →
  `"Petal length (cm)"` / `"Petal width (cm)"`, capitalised as in `kmeans.ipynb`;
  `"Blütenblattfläche (cm²)"` → `"Petal area (cm²)"`, `"Kelchblattlänge (cm)"` →
  `"Sepal length (cm)"`.
* `"Einflussgröße (Regressor)"` → `"Explanatory variable (regressor)"`,
  `"abhängige Zielgröße (Regressand)"` → `"Dependent target variable (regressand)"`
  (cells 6, 10, 28).
* legends: `"Daten"` → `"Data"`, `"Residuen"` → `"Residuals"`, `"Modell"` → `"Model"`,
  `"Gerade minimalen Abstands"` → `"Line of minimal distance"`,
  `"Regressionsgerade"` → `"Regression line"`, `"Regressionskurve"` → `"Regression curve"`,
  `"Faustregel: Breite = Länge/2 - 1"` → `"rule of thumb: width = length/2 - 1"`.
* `set_title("Polynomiale Regression von Grad %d")` → `"Polynomial regression of degree %d"`.
* `"Distanz zum Zentrum"` → `"Distance to the centre"` (British spelling), `"Preis"` → `"Price"`.
* `print` labels in cells 14, 18: Steigung/Achsenabschnitt/Korrelationskoeffizient/p-Wert/
  Standardfehler der Steigung → Slope/Intercept/Correlation coefficient/p-value/
  Standard error of the slope.
* cell 36: `"R^2 = %f%% der Varianz wird durch das lineare Modell erklärt"` →
  `"R^2 = %f%% of the variance is explained by the linear model"`.
* cell 43: `"R^2 ohne Type: "` / `"R^2 mit Type:  "` → `"R^2 without Type: "` /
  `"R^2 with Type:    "`; the padding was re-set so the two numbers still line up.
* cell 54: `"Ridge-Koeffizienten:"` / `"Lasso-Koeffizienten:"` → `"Ridge coefficients:"` /
  `"Lasso coefficients:"`; `"Bei Lasso exakt 0:", …, "von", …, "Koeffizienten"` →
  `"Exactly 0 under Lasso:", …, "of", …, "coefficients"`.
* comments: `# dieselbe Zahl als Kovarianz durch Varianz (ddof=0: n-Version, wie np.var)`
  → `# the same number as covariance over variance (ddof=0: the n-version, as in np.var)`;
  `# Bluetenblattlaenge mal -breite` → `# petal length times petal width`;
  `# 'string' für pandas >= 3` → `# 'string' for pandas >= 3`;
  `# das angepasste Modell am Ende der Pipeline` → `# the fitted model at the end of the pipeline`.

Library names, keyword arguments, DataFrame column names that come from the CSV
(`Type`, `Distance`, `Age`, `Price`, `BuildingArea`, `Landsize`, `Bedroom2`, `Suburb`,
`Lattitude`/`Longtitude` including the dataset's own misspellings) and the
`Coefficients` column label are untouched. `python3 tools/nbtext.py syntax` passes.

**Not re-executed**, as instructed. The stored outputs of cells 14, 18, 36 and 54 therefore
still carry the German `print` labels ("Steigung: …", "R^2 = … der Varianz wird durch das
lineare Modell erklärt", "Ridge-Koeffizienten: …", "Bei Lasso exakt 0: 5 von 8
Koeffizienten"), and the three plot-bearing cells still render German axis labels. The
central re-execution pass fixes all of it; until then a leftover-German scan over outputs
will hit this notebook.

## Decisions and doubts

**1. `Störgröße` → "error term", not "disturbance".** This is the chapter's load-bearing
distinction: $\epsilon$ is the unobservable random variable, the residual is what becomes
visible of it once a $\beta$ is fixed. English regression writing says *error term* for the
former and *residual* for the latter, and the pairing "residuals are the estimates of the
errors" is the standard way to state exactly the point cell 2 makes. "Disturbance" is the
econometric word and would read as a second technical term where the book has one. The
glossary's *Abweichung* → deviation row does not apply: that is `expectation-variance.md`'s
word for a different thing. Note the knock-on in the summary and in cells 3, 4 and 37, where
"die Störgrößen normalverteilt" became "the error terms … normally distributed".

**2. `Einflussgröße` → "explanatory variable".** German pairs *Einflussgröße* with
*Zielgröße*, and the glossary already fixes *Zielgröße* → target variable. English has four
candidates (predictor, explanatory variable, independent variable, regressor), and two of
them are spoken for in the same sentence: the German writes "eine ($k$-variate)
'unabhängige' Variable, die *Einflussgröße*" and then glosses the axis label
"Einflussgröße (Regressor)". So *independent variable* and *regressor* were unavailable and
*explanatory variable* carries the slot. If a reviewer prefers "predictor", it changes three
prose blocks and two axis labels and nothing else.

**3. Thousands separators were left as thin spaces.** `TRANSLATION.md` §6 says
`1.000` → `1,000`, but the German here does not use a point: it writes `$178\,000$` and
`$67\,000$` inside maths, with the SI thin space, which is equally correct English maths
typesetting. Converting them would have required `{,}` — the one token this chapter must not
contain — so they stand as `178\,000` / `67\,000`. The chapter's other money figures,
`$6081$` and `$27377$`, are ungrouped in the German and were left ungrouped. **A human should
decide** whether the book wants `$178{,}000$` here; if so, the §6 rule and the `{,}` grep
need to be reconciled, because they currently point in opposite directions.

**4. `Stützstelle` → "support point"** (cell 49: "nur wenige Stützstellen in den
Trainingsdaten"). The word is the interpolation term, and the chapter means "few data points
to pin the curve down". "Support point" is used in English numerical analysis and keeps the
image; "knot" belongs to splines and "sample point" would collide with *Stichprobe* → sample.
Low confidence, easy to revisit — it occurs once.

**5. `multilineare Regression` collapsed into "multiple linear regression".** Cell 21
defines *multiple lineare Regression* and then, one paragraph later, announces
"die multilineare Regression mit Scikit-learn". Two German words, one thing; English has one
name and the block had just introduced it, so the second mention reuses it. The block
boundary is untouched.

**6. `Bestimmtheitsmaß, en. Coefficient of determination`** (cell 39) is a German
self-gloss of exactly the kind `TERMINOLOGY.md` records as collapsing: the English reads
"The quantity $R^2$ is also called the **coefficient of determination**." The same happened
to "die **Gewichte** (weights)" in cell 12 and to "verzerrt (biased)"-style doublets
elsewhere in the book.

**7. The German lecture title stayed German.** Cell 51's "(Vorlesung *Einführung in Deep
Learning*)" became "(the German lecture course *Einführung in Deep Learning*)", following
`TRANSLATION.md` §3 on lecture titles and the precedent in `statistical-models.md`, which
writes 'the German lecture notes "Mathematik für Informatik"'. It is the only German left in
the prose; `check_english.py` does not flag it, so no `check-ignore` entry was needed.

**8. Section pointer into `descriptive-statistics.md`.** Cell 42's "Abschnitt Skalenniveau"
became "section Level of measurement". The actual heading there is "Level of measurement and
permissible summary measures"; the short form was kept because the German is short too, but
it is a loose pointer rather than a target and **a human may want it tightened** if that
chapter's headings get MyST targets.

**9. `Anwendungsbeispiel` → "An example application".** No translated chapter had set a
precedent (the other `Anwendungsbeispiel` headings are in notebooks not yet translated:
`dimensionality-reduction.ipynb`, `kernel-methods.ipynb`, `model-selection.ipynb`). Whoever
takes those should either follow this or propose one form for all four.

**10. Decimal commas.** Seven lines carried the LaTeX German decimal comma, 18 occurrences in
total: `0{,}5` ×3, `0{,}416`, `0{,}363`, `0{,}167`, `0{,}042` (cell 2); `2{,}5` ×2,
`3{,}5` ×2, `1{,}4` ×3 (cell 4); `0{,}872` (cell 19). All are plain points now and
`grep -c '{,}'` is 0. The thin-space percentage `$95\,\%$` in cell 15 was left as the source
has it, per §6.

**11. Drops.** Only the declared one: block `c0.1`, the two HHU Mediathek lecture-recording
links under the H1 (`sync/drops/lineare-regression.ipynb.json`, reason already recorded).
No further drops and no additions, so `sync/additions/linear-regression.ipynb.json` was not
created. 118 German blocks → 117 English ones.

## Style pass

Markdown cells only; every code cell is byte-identical to before (`check_untouched.py HEAD`
confirms "prose only") and the stored outputs therefore still match. 27 of the 32 markdown
cells were touched, 59 of 107 markdown paragraphs; block count unchanged at 117 and
`sync.py align` passes. Every `$…$` / `$$…$$` span was compared before and after – all 196
are byte-identical. No term from `TERMINOLOGY.md` was changed; *error term* (the
unobservable $\epsilon$), *residual* (the observable $y_i - f(x_i,\beta)$) and *explanatory
variable* appear exactly where they did before, and the error-term/residual passage in cell
2 was only tightened ("what becomes visible of the error terms" → "all we ever see of the
error terms"), not restated.

Kinds of change:

* **Calques replaced by the English idiom.** "Please note that" (*Man beachte*) → "Note
  that"; "what stands there are two quantities" (*da steht*) → "you are looking at two
  quantities"; "Widespread, by contrast, is the way of speaking in which …" → "The
  widespread usage, by contrast, is …"; "keep account of it" → "keep track of it"; "build
  ourselves a new regressor" → "build a new regressor"; "In advance:" → "To anticipate:".
* **Nominalisations turned into verbs.** "the central question … becomes the setting up of
  the model, and in particular of the basis function, from the data" → "becomes how to set
  up the model – and in particular the basis function – from the data"; "consists in
  minimising a penalty term" → "minimises a penalty term"; "The trick of regularisation now
  consists in not fitting" → "is not to fit"; "The use of the basis function … is called" →
  "Using the basis function … is called"; "If in a regression model one minimises …, one
  speaks of an estimate known as" → "Minimising … in a regression model yields an estimate
  known as".
* **"one" → "you" or an agentless verb** where the chapter is tutorial rather than
  definitional (cells 4, 15, 49): "one shifts the data" → "you shift the data"; "if one were
  to repeat the whole experiment" → "if you were to repeat"; "one is all the more prone to
  overfitting" → "overfitting becomes all the more likely"; "then one needs other ideas" →
  "then other ideas are needed". The Definition admonitions keep their impersonal form.
* **Sentence shape.** Subject-verb-object restored in a dozen long sentences ("In linear
  regression it is not the distances … that are minimised but the residuals" → "Linear
  regression minimises not the distances … but the residuals"); two fronted connectives
  moved ("Outside this chapter, its words are often used more narrowly"); one pair of
  sentences in cell 51 merged inside its paragraph (L1 regularisation / lasso). Punctuation:
  comma splice in "None of these narrowings is wrong, you only have to know" → semicolon;
  "that is" set off with commas in the two bullet points of cell 2.
* **Padding cut.** "A basis function expansion is simply not the better regressor
  automatically, just because" → "is not automatically the better regressor just because";
  "a pipeline for computing the polynomial regression" → "a pipeline to compute it";
  "can do nothing but a simple linear regression!" → "can only do the simple kind!".

Noticed but not touched – for a human:

1. **Cell 32 says "the normally distributed errors $\epsilon_i$"** where the rest of the
   chapter says *error terms* for $\epsilon_i$. It is not wrong – $\epsilon$ is the error –
   and it does not blur the error-term/residual line, but it is the one place the fixed term
   is not used for the fixed object. If the German says *Fehler* there, it is a translation
   decision, not a style one, so I left it.
2. **Cell 44 ends "which go beyond this course"** (and cell 51 cites a German lecture
   course). `TRANSLATION.md` §2 says the English edition is a standalone book; "this
   course" may want to become "this book" – but that is a meaning change and belongs to the
   translator or the author.
3. **Cell 12: "the bias of an estimator from the previous chapter".** The estimator's bias
   is in `statistical-models.md`; whether that is "the previous chapter" in the English
   book's order depends on `myst.yml`. Pointer, not prose, so untouched.
4. **Cell 11 "the green bars"**: the residual bars in the stored plot are whatever colour
   matplotlib's third cycle entry is (green in the default cycle). Fine as long as the
   outputs are the ones stored; a re-execution with a different style would orphan the word.
5. **Cell 2, "the residuals are its instances"** is slightly loose mathematically – they are
   realisations of the residual random variables, which approximate the errors – but it is
   the German's own phrasing of the error-term/residual distinction and I kept it exactly.
