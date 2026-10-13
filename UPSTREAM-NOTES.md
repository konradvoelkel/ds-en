# Findings for the German original

Things noticed while translating ds-skript that are **not** translation problems: they are
in the German book too. Nothing here has been fixed in the English edition unless the entry
says so, because an English edition that quietly corrects its original stops being a
translation of it. Collected for whoever picks ds-skript up when it unfreezes in February
2027.

Ordered roughly by how much they cost a reader.

## The PDF export silently loses content

`latexmk` runs in force mode, so `myst build --pdf` reports errors and produces a PDF
anyway, and nobody notices.

* **Figures inside an admonition are dropped.** MyST renders an admonition as a `framed`
  box and still emits `\begin{figure}[!htbp]` for a figure inside it. A float cannot live
  in a box: xelatex says "Not in outer par mode" and the figure does not appear. In
  `erwartungswert.md` this loses all four gas-container figures from the entropy
  digression.
* **An interrupted numbered list restarts at 1.** MyST emits `\begin{enumerate}[resume]`
  where a list is interrupted by a display formula and continues after it. Without the
  `enumitem` package that option is an error, and the numbering starts over — which the
  rules-of-calculation list in `erwartungswert.md` does.

*Fixed in this edition* (`templates/tex/ds-en/template.tex`): figures become non-floating
`[H]` boxes, and `enumitem` is loaded. Both fixes are three lines and apply unchanged to
ds-skript.

## Factual slips

* **`dimensionsreduktion.ipynb`**: the text calls the dataset "der MNIST-Datensatz
  handgeschriebener Ziffern", but the code calls `datasets.load_digits()`, which is the
  8×8 UCI digits set, not MNIST. A heading and one sentence.
* **`explorative-analyse-beispiele.ipynb`**: block c4.5 calls the three wine classes "die
  drei Hersteller von Wein" (the three producers). The `wine.names` quotation two blocks
  above, in the same cell, says "three different cultivars", and
  `deskriptive-statistik.md` says the colour carries the grape variety. Three places, two
  stories.
* **`statistische-tests.md`**, section *Ausblick: vom Bereichsschätzer zum Test*: "mit der
  Begrifflichkeit des Formparameters aus jedem Test einen Bereichsschätzer konstruieren".
  Inverting a test into a confidence set does not go through a shape parameter.
* **`explorative-analyse-mit-numpy.ipynb`** points at "das Kapitel Modell-Auswahl, unter
  *train-test split*". `model-selection.ipynb` has no section of that name; the heading is
  *Training, Test und neue Daten*.

## Cosmetic and housekeeping

* **`images/normalmarginal.png`** has an empty default axes in the bottom-left panel — a
  leftover from building a 2×2 grid without disabling the unused subplot.
* **`stochastik-programmieren.ipynb`** calls the sample space `W` in code while the prose of
  the same cell writes it $\Omega$, and passes it as the `Omega` parameter of `P`.
  *Changed in this edition*, since the code had to be touched anyway.
* **`stochastik-programmieren.ipynb`**: `transform_unit_to_dice` returns one die's pips, so
  the name wants to be `transform_unit_to_die`. Left alone here: the name is already
  English, and renaming it is an edit to the German book, not a translation.
* **`kernel-methoden.ipynb`**: a missing space in block c14.12 (`und${\lVert b \rVert}`,
  which renders as "und$\lVert b\rVert$"), and block c14.18 is ungrammatical.
* **Scikit-Learn / Scikit-learn** are spelled both ways across the book.
* **`pandas.ipynb` and `data-cleaning.ipynb`** pass `np.size` to `agg`, which is deprecated
  in current pandas.
* **`kmeans.ipynb`** block c13.0 is an HTML comment holding a link to
  `kmeans-in-action.mp4`, a file that is not in the repository.
* **Three notebooks are unseeded** where the others are seeded (`kernel-methoden.ipynb`:
  the sample, `KMeans(n_init=1)`, `train_test_split`), so their figures change on every
  re-execution. The repo's stated convention is that seeds are left as they are, which
  reads as a decision about existing seeds rather than about these.

## Things that are not errors but surprised a translator

* `Die Gausssche Normalverteilung` is the H1 of `normalverteilung.ipynb`, but three
  chapters link to it as plain `Normalverteilung`. Title and link text differ in the
  original; this edition keeps the asymmetry.
* The German varies its link texts on purpose (`Kovarianz` vs `Kovarianz und Abhängigkeit`,
  `Daten putzen` vs `Putzen der Daten`). `tools/check_links.py` is built around that:
  fewer English labels than German is fine, more is a bug.
