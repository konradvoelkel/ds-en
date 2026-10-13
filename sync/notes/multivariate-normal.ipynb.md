# Translator's notes: `multivariate-normal.ipynb`

German original `multivariate-normalverteilung.ipynb`, 26 cells, 72 blocks, 1 declared drop
(the HHU lecture recording link under the H1, block `c0.1`), 71 translated blocks. No
further drops, no `sync/additions` entry, no `sync/check-ignore` entry – all four checks
(`nbtext.py check`, `nbtext.py syntax`, `sync.py align`, `check_english.py`) pass with zero
findings.

The chapter references no images, so there is nothing to redraw.

## New terminology

Terms I had to decide on that are not in `TERMINOLOGY.md` yet. The chapter leans heavily on
`covariance.md`, whose rows (inner product, covariance matrix, marginal distribution,
contour line, cloud of points, jointly normally distributed, uncorrelated, positive
(semi)definite, bivariate normal distribution, spread) I took over unchanged.

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
| Streckfaktor | stretch factor | also in a `print` string; the factors $\sqrt{\lambda_i}$ |
| Strecken, Streckung | stretching | the verb for $D$; *Skalieren* → *scaling* is the operation's bolded name in the list |
| Strahl (von $\mu$ weg) | ray |  |
| univariat normalverteilt | univariate normally distributed | and *multivariat normalverteilt* → multivariate normally distributed |
| Variational Autoencoder | variational autoencoder | lower case in English running prose; the German capitalises it as a noun |
| Verschieben / Skalieren / Drehen | Shifting / Scaling / Rotating | the three bolded operations in the derivation; the code comments use the same three words |

## Code changes

German identifiers renamed (grepped across the whole notebook afterwards – no survivors):

| German | English | cells |
|---|---|---|
| `kandidaten` | `candidates` | 3 |
| `dichte` (loop variable) | `density` | 3 |
| `werte` | `values` | 5, 17 |
| `vektoren` | `vectors` | 5, 17 |

Everything else was already English (`getmvn_by_rho`, `samplexy`, `plotalot`, `plotalot2`,
`plot_by_rho`, `plot3dangles`, `Sigma`, `Sigma_inv`, `levels_Q`, `levels_pdf`, `samplesize`,
`rng`, `mu`, `phi`). Library names and keyword arguments are untouched.

Translated strings:

* **Plot titles.** Cell 3 dict keys, which are the three subplot titles: `"Normal ×
  Gleichverteilung"` → `"Normal × uniform"`, `"Normal × Exponential"` → `"Normal ×
  exponential"`, `"Normal × Normal"` → `"Normal × normal"` (the column alignment of the
  dict was re-flowed to the new key lengths). Cell 5: `"z: Standardnormalverteilung"` →
  `"z: standard normal distribution"`; `"x = A z + µ"` unchanged. Cell 15: `"Levelsets der
  Dichte der bivariaten Normalverteilung mit Kovarianz Σ"` → `"Level sets of the density of
  the bivariate normal distribution with covariance Σ"`, and `"Levelsets der quadratischen
  Form zu Σ invers"` → `"Level sets of the quadratic form belonging to Σ inverse"`.
* **`print` labels.** Cell 5: `"empirische Kovarianzmatrix der Stichprobe:"` → `"empirical
  covariance matrix of the sample:"`, `"Wurzeln der Eigenwerte:"` + `"-- das sind die
  Streckfaktoren 1/2 und 2"` → `"square roots of the eigenvalues:"` + `"-- these are the
  stretch factors 1/2 and 2"`. Cell 17: `"Eigenwerte:"` → `"Eigenvalues:"`,
  `"Eigenvektoren (Spalten):"` → `"Eigenvectors (columns):"`.
* **Comments and the one docstring.** All of them, in cells 3, 5, 9, 10, 12, 13, 15, 17, 19.
  The docstring in cell 15 keeps its Σ: `"""Quadratic form v^T Σ^{-1} v for v = (x, y)"""`.
  `# meshgrid` and `# plot the weirdo sample:` were already English and are unchanged.

No logic was touched; no cell was added, removed or retyped; the only whitespace change is
the re-alignment of the cell 3 dict. The code was **not** re-executed, per instructions.

**For the re-execution pass:** the stored outputs are still the German ones and *must* be
regenerated. Cells 5 and 17 have German stream output ("empirische Kovarianzmatrix der
Stichprobe", "Wurzeln der Eigenwerte", "Eigenwerte", "Eigenvektoren (Spalten)"), and the
PNGs of cells 3, 5 and 15 have German titles baked into the image. Cells 12, 13, 20, 21 and
24 have no text in their figures and are harmless either way.

## Decisions and doubts

**1. Cross-reference link texts, two of which point at chapters not yet translated.** The
German link *texts* are short names, not full chapter titles, so I translated the names:

| German | English used here | target's state |
|---|---|---|
| `[Normalverteilung]` | **[Normal distribution]** | `normal-distribution.ipynb` still German, H1 *Die Gausssche Normalverteilung* |
| `[Relative Entropie]` | **[Relative entropy]** | matches the translated H1 exactly |
| `[Kovarianz]` | **[Covariance]** | `covariance.md`'s H1 is *Multivariate statistics: covariance and dependence*; the German link text was the short name and I kept it short |
| `[Dimensionsreduktion]` | **[Dimensionality reduction]** | `dimensionality-reduction.ipynb` still German; the glossary already fixes the term |
| `[Expectation-Maximization]` | **[Expectation Maximization]** | already English in the German; I only dropped the hyphen to match that chapter's H1 |

The first and the fourth are the ones to re-check once those chapters are translated. If the
`normal-distribution.ipynb` translator keeps "Gaussian" in the title, a consistency pass may
want **[The Gaussian normal distribution]** here instead.

**2. *Drehstreckung* (block c4.9).** German has one word for the composite map $A = RD$, and
it is not the *Drehstreckung* of elementary complex analysis (a spiral similarity, where the
stretch is isotropic) – here the stretch factors differ per axis. "Rotation-dilation" and
"spiral similarity" would both be wrong, and "rotation-scaling map" reads like a coinage. So
the single German noun becomes the pair it actually names: "$\Sigma^{-1}$ in the exponent
**undoes the rotation and the stretching**", and "because the rotation and stretching
enlarges areas". That also lets the three bolded operations – Shifting, Scaling, Rotating –
be the words the rest of the block and the code comments reuse. It costs the German's
compactness; I think the clarity is worth it, but a style pass may want to tighten it.

**3. "Sieht ein zweidimensionales Histogramm zwei Gipfel" (block c14.4).** The German makes
the histogram the subject that *sees* two peaks, which is a liveliness English will not
carry: "If a histogram sees two peaks" reads as an error, not as a figure of speech. I wrote
"If a two-dimensional histogram shows two peaks". The agent of the seeing is lost; the claim
is unchanged. This is the one place where I deliberately flattened the voice.

Three smaller calls, for the record:

* **`print` label capitalisation.** I followed the German's own case: cell 5's labels start
  lower case ("empirical covariance matrix of the sample:", "square roots of the
  eigenvalues:") because the German adjectives there are lower case, while cell 17's start
  upper case ("Eigenvalues:", "Eigenvectors (columns):") because the German nouns are. The
  result is an inconsistency inside one notebook that the German also has. If a human would
  rather have one rule, capitalise all four.
* **"X+Y=0" is left outside maths mode** in block c23.4, exactly as the German leaves it,
  even though the same block has `$X+Y$` in maths two clauses earlier. Fixing it would be an
  improvement to the original, not a translation.
* **Mechanical things.** Two em dashes in block c14.4 became spaced en dashes; the two
  hyphen-as-dash cases (` - ` in blocks c14.0 and c23.4) became spaced en dashes too.
  `d.h.` → "that is" / "which is to say", `Z.B.` → "say" (post-posed), `Vorlesung
  *Einführung in Deep Learning*` → "the course *Introduction to Deep Learning*", matching
  `numpy.ipynb`. "Machen Sie sich klar" → "Convince yourself", matching
  `expectation-variance.md`. The bolded `**Achtung**` became `**Careful**`; it is a bare
  bolded line, not an admonition title, so `TRANSLATION.md` §5 does not settle it – worth a
  glossary row if another chapter has one.
