# Translator's notes: `kernel-methods.ipynb`

German original `kernel-methoden.ipynb`, **25 cells, 54 blocks → 53 in the English
edition**. One drop, already declared in `sync/drops/kernel-methoden.ipynb.json`: block
`c0.1`, the HHU Mediathek link under the H1 (*Vorlesungsaufzeichnung Kernel-Trick, VL 21*).
No further drops were needed, no `sync/additions` entry, and `check_english.py` comes up
clean, so no `sync/check-ignore` entry either.

`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass;
`grep -c '{,}'` is 0, and so is the em-dash count. The notebook was **not** re-executed, as
instructed. The stored outputs are the German run, but they contain no German text at all
(they are figures, an HTML5 video, a still PNG and the `rbf_kernel` array repr), so nothing
in the outputs is stale in the translation sense.

The animation mechanism in cell 5 – `to_html5_video()` plus a `savefig` PNG handed to
`ipydisplay.display(..., raw=True)` so that the web export can show the video and the PDF
export the still – is untouched; only its two-line German comment was translated.

## New terminology

| German | English | note |
|---|---|---|
| Kernel-Trick | kernel trick | the chapter's central notion; the glossary had only *Kernel-Methoden → kernel methods* |
| Kernel-Methode (singular) | kernel method | "one speaks of the **kernel method** when…"; the chapter title stays the plural *Kernel methods* |
| Kernel-Funktion, Kernelfunktion | kernel function | the German spells it both ways; one English spelling |
| Mercer-Kernel | Mercer kernel | no hyphen in English, as with *Shannon entropy* |
| Satz von Mercer | Mercer's theorem | genitive, as for *Satz von Bayes → Bayes' theorem* |
| Feature-Raum | feature space | $F$; also used (in German) by `expectation-maximization.ipynb` and `kmeans.ipynb` |
| Feature-Abbildung | feature map | $\phi$; not "feature mapping" |
| Feature-Vektor | feature vector |  |
| radiale Basisfunktion | radial basis function | the first section heading; `rbf_kernel` keeps its name |
| radialer Basisfunktionskernel | radial basis function kernel |  |
| Gausssche Kernel, Gauss-Kernel | Gaussian kernels | see *Decisions* 1 |
| quadrierter / quadratischer Exponentialkernel | squared / quadratic exponential kernel | the German offers both; so does the English |
| Abstandsbegriff | notion of distance | not "concept of distance" – the chapter means which inner product you measure with |
| Abstandsmessung | measurement of distance | "rest on nothing but measurements of distance" |
| translations- und rotationsinvariant | invariant under translation and rotation | the German compound does not survive as one word |
| bis auf Translation und Rotation | up to translation and rotation |  |
| rechenintensiv | expensive to compute |  |
| Hauptachsentransformation | principal axis transformation | see *Decisions* 2 – `dimensionality-reduction.ipynb` and `kmeans.ipynb` own this word and are not translated yet |
| Beobachtungsraum | observation space | where the first principal component is a curve, not a line |
| Eigenvektor | eigenvector |  |
| Vektorraum mit Skalarprodukt | vector space with an inner product | follows the glossary's *Skalarprodukt → inner product* |
| Ridge-Regularisierung | ridge regularisation | house `-ise`; `KernelRidge` keeps its name |
| k-Nearest Neighbours | k-nearest neighbours | lower case in English running prose, as with *k-means* |
| Support Vector Machines | support vector machines | likewise lower case |
| normierte Vektoren | normalised vectors | the glossary's *normieren → to normalise* |
| Normierung | normalisation | the one a Gaussian density would carry and a kernel does not |
| Standbild | still image | the PDF fallback in the cell 5 comment |
| Nebenbemerkung | an aside | *Bemerkung → Remark* is fixed for admonition titles; this is running prose |
| Datum (ein einzelnes) | datum | see *Decisions* 3 |

Headings, for the record: `## Motivation: radiale Basisfunktion` → **Motivation: the radial
basis function**, `### Eine geometrische Transformation` → **A geometric transformation**,
`### k-Means im transformierten Raum` → **k-means in the transformed space**, `### Was wir
wirklich brauchten` → **What we actually needed**, `## Daten durch Abstände beschreiben` →
**Describing data by distances**, `## Kernel` → **Kernels**, `### Gausssche Kernel` →
**Gaussian kernels**, `## Kernel PCA` unchanged. Sentence case throughout, as in
`numpy.ipynb`.

Reused unchanged from the existing glossary: *Skalarprodukt* → **inner product**,
*Zusammenhang* → **relationship**, *positiv definit* → **positive definite**,
*Kovarianzmatrix* → **covariance matrix**, *Hauptkomponente* → **principal component**,
*Datensatz* → **dataset**, *Merkmal/Feature* → **feature**, *Klassifikation* →
**classification**. `k-Means` is **k-means** in running prose, lower case, as
`statistical-models.md` already writes it – and `2-Means` is **2-means** by the same rule.

## Code changes

Only one German identifier existed, and the rest of the code was already English
(`sample`, `secondsample`, `radius`, `ticks`, `frames`, `rbf_surface_in_time`, `init`,
`update_surface`, `update_data`, `plot_ani`, `radial`, `kmeans_fit`, `smaller_sample`,
`remainder_sample`, `clf`, `y_pred`, `sample_pca`, `sample_kernel_pca`).

| old | new | where |
|---|---|---|
| `ringe` | `rings` | cell 1, defined and called; grepped across the whole notebook, two occurrences, both changed |

`radial` was left as it is: it is an English word already, and the docstring explains it as
one coordinate of the feature map.

Translated alongside it:

* cell 5, the two-line comment about the PNG fallback: "Also output the last frame as a
  PNG: the web export shows the video, the PDF export (which cannot do HTML) uses the still
  image." The code it sits in is unchanged.
* cell 9, the `radial` docstring: "Squared distance from (x,y) to the origin: a single
  coordinate of the feature map φ, which we introduce in general further below." The
  literal `φ` is kept – it is the same symbol the prose below uses as `$\phi$`.

Comments in cells 1, 4, 15, 17, 20 and 22 were already English in the original and are
untouched. The chapter has **no** `print` strings, no plot titles, no axis labels, no legend
entries and no tick labels: `ax.set_zticklabels([])` in cell 5 deliberately removes the only
labels there would have been. Nothing in the code needed a decimal-point fix; `grep '{,}'`
finds nothing.

## Decisions and doubts

**1. *Gauss-Kernel* → "Gaussian kernels", collapsing the German's two names (blocks c14.19,
c14.20).** The German heading says *Gausssche Kernel* and the definition then names the
object *Gauss-Kernel*. English has one idiomatic name, "Gaussian kernel", and I used it in
both places, so the bold defining term now repeats the heading. The alternative was "Gauss
kernel" for the bold term, which would have matched `statistical-tests.md`'s *Gauß-Test* →
**Gauss test** row, but "Gauss kernel" is not what the literature calls this and the reader
would meet the real name nowhere in the chapter – while the three alternative names the
definition goes on to list (squared exponential, quadratic exponential, radial basis
function kernel) are exactly the ones in use. The glossary's own rule ("Gaussian where the
German says Gaußsch") points the same way. **Worth a human eye**, because it is the one
place where this chapter and the tests chapter treat the name Gauss differently.

**2. *Hauptachsentransformation* → "principal axis transformation" (block c19.1), and it
needs coordinating.** The glossary has *Hauptkomponentenanalyse* → **principal component
analysis** but not this word, which the German book uses as a near-synonym – `kmeans.ipynb`
and `eda-examples.ipynb` both gloss it as "(principal component analysis, PCA)", while
`dimensionality-reduction.ipynb` builds a whole section on *Hauptachsen* → principal axes.
I kept the German's distinction: the eigenvector computation itself is the "principal axis
transformation", and *Hauptkomponente* stays **principal component** in the same cell and in
c24.0. If `dimensionality-reduction.ipynb` (not translated yet, and the chapter that owns
the term) decides to flatten everything to "principal component analysis", this one block
should follow it – it is a single sentence.

**3. *das Datum des Abstands* → "the single datum of the distance" (blocks c14.1, c14.2).**
Both Examples hinge on *Datum* in its rare singular-of-data sense: the one number you keep
instead of the coordinates. English "datum" carries that, but barely, and a reader may trip
on it. I added "single" in the two-point case to force the reading and left the plural case
as "the datum of the distances $d(A,B), d(B,C), d(A,C)$", which is how the German has it. If
a style pass wants the trip removed, "remember just the distance $d(A, B)$" is the natural
rewrite and loses only the German's insistence that a distance *is* a piece of data – which
is, however, the whole point the two Examples are making.

**4. `## Kernel` → `## Kernels` (block c14.14).** German *Kernel* is both singular and
plural; the section defines the notion and then discusses several, so the English heading is
plural, matching `### Gaussian kernels` below it. Nothing links to this heading (I grepped
the repository: only `myst.yml` names the file, and `landing-page.md` says "kernels" in its
mermaid diagram).

**5. A German typo fixed inside block c14.12.** The original has `und${\lVert b \rVert} =
1$` with no space before the maths, which renders as "und$\lVert b\rVert$". The English
reads "and ${\lVert b \rVert} = 1$". Nothing else in the maths was changed anywhere in the
chapter.

**6. Block c14.18 is ungrammatical in the German and I did not reproduce the breakage.**
"…dass er nur mit den Skalarprodukten der Feature-Vektoren arbeitet und ersetzt dann dieses
durch eine Kernelfunktion" – *ersetzt* hangs off the wrong clause and *dieses* is singular
after a plural. I turned the second half passive: "…so that it works only with the inner
products of the feature vectors, and these are then replaced by a kernel function." Same
sentence count, same block.

**7. Address: *man* became "one", not "you".** The second half of the chapter is written
almost entirely in impersonal *man* ("man muss nicht kennen", "man spricht von", "man
beachte") and is doing mathematics; "you" would have made it chatty just where it is being
precise. The *wir* passages ("we can also let only the k-means computation take place…")
stay "we", per TRANSLATION.md §6. This is the opposite choice from `numpy.ipynb`, which
standardised on "you" – defensible, I think, because that chapter is a tutorial and this one
is a definition section, but a style pass may want to unify them.

**8. Re-execution will change the figures, and that is not my doing.** Cell 1 draws the
sample without a seed (`st.multivariate_normal(...).rvs`, `st.uniform.rvs`), cell 9's
`KMeans(n_init=1)` is unseeded, and cell 22's `train_test_split` has no `random_state`. The
central re-execution pass will therefore produce different-looking (statistically identical)
rings, colourings and kernel-PCA plots. Nothing in the prose quotes a number from any
output, so no text depends on it.

**9. What the chapter promises and does not deliver.** Block c13.2 mentions support vector
machines as something "neither of which we have discussed", and the chapter indeed never
returns to them; the English says so just as plainly. Worth knowing for whoever writes the
English edition's cross-references: this chapter is not where a reader learns SVMs.
