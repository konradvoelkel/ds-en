# Translator's notes: `important-continuous-distributions.ipynb`

German original `wichtigste-stetige-verteilungen.ipynb`, **31 cells, 52 blocks**; the
English file has **51 blocks** after the one declared drop. The drop was already in
`sync/drops/wichtigste-stetige-verteilungen.ipynb.json` before I started: block **c0.1**,
the pair of HHU Mediathek lecture-recording links under the H1 (one block, two links – the
German has no blank line between them). Nothing further was dropped, so the file is
unchanged. No `sync/additions` entry – nothing was added. No `sync/check-ignore` entry –
`check_english.py` comes back clean with no suppressions.

`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass.
The notebook was **not** re-executed: the stored outputs are still the German run (cells 8,
12, 13, 15, 17, 19, 21, 23, 25 and 28 carry figures with German titles, axis labels and
legend text, and cell 8's `print` output is unaffected but its figures are not). That is
expected and waits for the central re-execution pass. **Until that pass runs, the rendered
chapter shows English code producing German plots.**

One correction to the brief I was given: this chapter does **not** contain the chi-squared,
t or F distributions. Its sections are the normal, contaminated normal, Dirac, continuous
uniform, exponential, log-normal and Weibull distributions. *Freiheitsgrade* therefore never
occurs here, so there was nothing to align with `statistical-tests.md`; the
`chi-squared-distributions.png` / `student-t-distributions.png` commitment is not touched by
this file. The one cross-chapter commitment that *is* live was honoured: the H1 is **The most
important continuous distributions** and the section is **## Contaminated normal
distribution**, both as `continuous-distributions.md` links them.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | note |
|---|---|---|
| Anwendungsbeispiele | example applications | the bullet that closes every distribution's list; "examples of application" reads as translated German |
| Dirac-Verteilung | Dirac distribution | the section heading; `continuous-distributions.md` already has the term, `intro-stochastics.md` has *Dirac-Maß* → Dirac measure, and both occur in this chapter |
| Fertigungsgenauigkeit | manufacturing precision | normal-distribution application bullet |
| Gaussverteilung | Gaussian distribution | the glossary's *Normalverteilung* row licenses "Gaussian" where the German says so; the chapter's opening sentence does |
| Gaussssche Mischung | Gaussian mixture | `statistical-models.md` already has *gemischtes Modell* → mixture model; this is the named special case |
| Heaviside-Step-Funktion | Heaviside step function | no hyphens in English |
| Kehrseite (stetige Kehrseite der Poissonverteilung) | flip side | "the continuous flip side of the Poisson distribution" |
| Lognormalverteilung | log-normal distribution | hyphenated and lower case in running prose, matching the English Wikipedia title the chapter links to; the heading is `## Log-normal distribution` |
| Sternenhimmel | night sky | the Hubble bullet; `verschmierter Pixelhaufen` → *smeared-out heap of pixels* |
| Starkregenereignis | heavy-rainfall event | the DWD question |
| Spielzeugdaten | toy data | the wording `landing-page.md` already uses |
| Stetige Gleichverteilung | continuous uniform distribution | the glossary's *Gleichverteilung* row says "discrete or continuous, say which", and the heading says which |
| Superresolution-Technik | super-resolution technique | hyphenated in English |
| Weibull-Verteilung | Weibull distribution |  |
| Wärmepumpe | heat pump | the Weibull application bullet |
| Übersichtsgrafik | overview diagram | the ProbOnto figure |

Already settled elsewhere and reused unchanged: *Formparameter* → **shape parameter**
(`statistical-tests.md`), *Wartezeit* → **waiting time** and *gemischtes Modell* → **mixture
model** (`statistical-models.md`), *Träger* → **support**, *Mischverteilung* → **mixture
distribution** and *kontaminierte Normalverteilung* → **contaminated normal distribution**
(`continuous-distributions.md`), *Zentraler Grenzwertsatz* → **central limit theorem**,
*zentrales Moment* → **central moment** (`expectation-variance.md`), *Zusammenhang* →
**relationship** (`covariance.md`), *Merkmal* → **feature**, *Teilnehmer\*innen* →
**participants** (TRANSLATION.md §6).

Link texts, taken from what the already-translated chapters use rather than re-invented:
*Wichtigste diskrete Verteilungen* → **The most important discrete distributions** (2
occurrences), *Stetige Verteilungen* → **Continuous distributions**, *Normalverteilung* →
**The normal distribution**. Both of those targets are still untranslated files, so the
link text is ahead of the chapter it points at – that is the state the rest of the book is
already in.

## Code changes

**No identifiers were renamed.** Every name the notebook invents was already English or
language-neutral (`X`, `Xsamples`, `sample`, `plotX`, `name`, `params`, `first_feature`,
`iris`, `mu`, `sigma`, `norm1`, `norm2`, `epsilon`, `a`, `b`, `k`, `f`, `x`). `lamda` keeps
its deliberate misspelling – the comment next to it explains why, and that comment is now in
English. Library names and keyword arguments are untouched (`st.weibull_min`, `c=`, `loc=`,
`scale=`, `s=`, `density=`, `bins=`).

What *was* translated in the code cells:

* **Every comment**: cells 2, 3, 4, 8, 10, 12, 21, 25, 28.
* **Axis labels**: `"Häufigkeit"` → `"frequency"` (twice, cell 8; the lower case matches
  `iris.ipynb`), `"Dichte"` → `"density"` (cells 8, 12, 13, 15, 28),
  `"Erstes Feature Iris-Datensatz"` → `"first feature of the Iris dataset"` (cell 28).
  `'F(x) = P(X ≤ x)'` is already notation and stays.
* **f-string axis label**, cell 8: `Mittelwert=… (erwartet: …), Standardabweichung²=…` →
  `mean=… (expected: …), standard deviation²=…`. The `²` and the `:.4f` formats are
  unchanged.
* **xlabel**, cell 13: `"10000 Samples von N(3, 2²), in 200 Bins"` → `"10,000 samples from
  N(3, 2²), in 200 bins"` – note the thousands separator appearing, per TRANSLATION.md §6.
* **Plot titles and the `name` strings that feed them**, cells 12, 15, 17, 19, 21, 23, 25:
  `"Normalverteilung"` → `"normal distribution"`, `"Gleichverteilung"` → `"uniform
  distribution"`, `"Exponentialverteilung"` → `"exponential distribution"`,
  `"Log-normalverteilung"` → `"log-normal distribution"`, `"Weibull-verteilung"` →
  `"Weibull distribution"`, `"Dirac-Verteilung bei ξ=0"` → `"Dirac distribution at ξ=0"`.
  The mixture's `name` is a formula and is unchanged.
* **The two f-string templates in `plotX` gained a definite article**: `f"PDF von {name} mit
  Parametern {params}"` → `f"PDF of the {name} with parameters {params}"`, same for the CDF
  line; and cell 17's `"CDF von "+name` → `"CDF of the "+name`. See *Decisions* 2.

The mixture cell's own title (cell 15) is `f"PDF of {name}"` with **no** article, because
there the name is `0.6·N(0,1) + 0.4·N(2, 0.5²)`. The German has the same asymmetry
(`f"PDF von {name}"` without a preposition change), so this is the original's structure, not
a new one.

## Decisions and doubts

**1. *Geschlecht* → "gender" in the contaminated-normal example (block c14.2).** The German
says *Das Geschlecht ist (näherungsweise!) Bernoulli-verteilt* and then, two sentences later,
that every act of modelling can make a part of reality invisible that one may not want to
make invisible. English forces a choice German does not: "sex" fits a body-height model
better, "gender" is what the invisibility remark is about. I chose **gender** (and "within
the gender groups") because the paragraph's point is the social one – the sentence about
invisibility is the reason the example is in the book at all, and "sex" would blunt it.
**This is the one wording in the chapter a human should sign off on**; if the author wants
the biological reading, it is two words in one block.

**2. The `plotX` titles gained "the" (cells 12, 17).** `f"PDF von {name} mit Parametern
{params}"` with `name = "Normalverteilung"` is idiomatic German; the word-for-word English
"PDF of normal distribution with parameters (0, 1)" is not. Rather than capitalise the names
into pseudo-titles ("PDF of Normal Distribution…"), I put the article into the template and
kept the names as ordinary lower-case noun phrases, which is also what makes
`"Dirac distribution at ξ=0"` read correctly after `"CDF of the "`. It is a change to code
rather than to a string literal, so it is called out here; it affects five figure titles per
distribution-with-`plotX` and is confined to two cells.

**3. The DWD Climate Data Center link is marked "(in German)" (block c29.1).** The portal
at `cdc.dwd.de/portal/` opens in German and its dataset descriptions and `BESCHREIBUNG`
files are German, so TRANSLATION.md §3 says to mark it. It does have an English toggle,
however, so a reader is not stranded – **if the author thinks the marker oversells the
problem, it is a four-word deletion.** The two links that stay unmarked are Kaggle and the
English Wikipedia article on the log-normal distribution, which the German already pointed
at in English.

**4. `## Daten zum plotten und fitten` → `## Data to plot and fit`.** Sentence case, as in
`intro-python.ipynb` and `numpy.ipynb`. The literal "Data for plotting and fitting" is
heavier and the section is about the data, not about the activity – the paragraph under it
says "we need some toy data". Nothing links to this heading (I grepped the whole repo).

**5. Two German doublets collapse, as elsewhere in the book.** *von Hand / zu Fuß*
(block c5.0, two idioms for the same thing) becomes the single "by hand"; *Die Übersichtsgrafik
ist bereits eine gute Gedächtnisstütze* keeps its "already" as "The overview diagram alone is
already a good memory aid", because the "already" is doing work – it means you get something
out of ProbOnto before reading any of it.

## Figures

`images/ProbOnto2.5.jpg` (block c30.0) is the only image in the chapter. **I inspected it:
it is entirely English** – "Univariate", "Multivariate", "Empirical" and some 200 node
labels, all English, no German anywhere. It therefore needs no redraw. I was told not to
edit `images/README.md`; the row that should be added there (or the note that no row is
needed) is this one:

| `ProbOnto2.5.jpg` | important-continuous-distributions | none – inspected, the whole diagram is English | **clean** |

The figure's `:name: probonto-diagram` label and its CC-BY-SA caption are untranslated by
TRANSLATION.md §3 and §3's proper-names rule; the caption was already English.

## Style pass

Markdown cells only; all code cells are byte-identical to before (verified cell by cell
against a pre-pass copy), so the stored outputs still match the code. **21 of 51 blocks**
changed, no block merged, split or reordered. `sync.py align`, `check_english.py`,
`nbtext.py check`, `nbtext.py syntax` and `check_untouched.py HEAD` all pass ("prose only").

Kinds of change:

* **Calques removed**: "a *so-called* mixture model" (*sogenannt*; in English "so-called"
  casts doubt on the name) → "a *mixture model*"; "Both times $\lambda$ is the same rate"
  (*beide Male*) → "In both cases"; "have not missed the fact that several distributions can
  perfectly well be parametrised" → "have noticed that several of them can"; "we want to gain
  an overview" → "we want an overview"; "obtain through Scikit-Learn" → "get from";
  "To begin with, Numpy's built-in `np.genfromtxt` will do" → "for now, …".
* **German fronting undone**: "a differential entropy it does not have" → "it has no
  differential entropy"; "there is, after all, no density" → "there is no density, after
  all"; "For each of the distributions we will look at plots of … and of the …" → "For each
  distribution we will look at plots of … and the …".
* **Verbs for nouns, and subjects set straight**: "a great deal of data *satisfies* none of the
  distributions" → "*fits* none"; "a two-stage process in which, depending on the outcome of a
  Bernoulli experiment, a different normal distribution is sampled from" → "in which the
  outcome of a Bernoulli experiment decides which normal distribution is sampled from";
  "every act of modelling carries the potential to make a part of reality invisible that one
  may not want to make invisible at all" → "has the potential to render invisible a part of
  reality that you may not want invisible at all"; "It contains variables with a spatial
  distribution, and time series of" → "It holds spatially distributed variables and time
  series of"; "Comparing the histogram … is what shows you best how close we are" → "is the
  best way to see how close we are".
* **Sentence rhythm**: "For this we use the Python module `matplotlib.pyplot`. It emulates the
  behaviour of MATLAB." → one sentence with "which"; "toy data, which are also much
  discussed" → "much-discussed toy data"; "So that we can get a little practice in plotting
  data and fitting distributions to data (and then in turn visualising that in a plot)" →
  "To get a little practice in plotting data and fitting distributions to it (and then
  visualising the fit in a plot)"; the ProbOnto sentence's long relative clause is now set
  off with dashes; "These are mostly assembled in stages out of the simple models, though" →
  "Mostly, though, these are assembled in stages from the simple models".
* **Profile bullets**: only single-word changes, the skeleton untouched – "How high is the
  wind speed?" → "What is the wind speed?", "greatest amount of precipitation on a single day"
  → "largest amount of precipitation to fall on a single day", the bus "went" → "left",
  "an odd moment $\neq 0$ is therefore a sign" → "so an odd moment $\neq 0$ is a sign",
  "further examples are given in" → "more examples are listed in".

Kept deliberately:

* The exponential-distribution bullet "How long does it take until the next packet arrives at
  the server?" is quoted verbatim in the Poisson Remark of
  `important-discrete-distributions.ipynb`; both left word for word.
* "Python method" in c9.0. The thing defined is a plain function, and "Python function" is
  what an English reader expects, but the German says *Methode* and the fix is a correction,
  not style – **a human may want to make it**.
* "extremely punctually" in the bus example, the gender wording the translator flagged under
  *Decisions* 1, and every glossary term (Gaussian distribution, Gaussian mixture, mixture
  model, contaminated normal distribution, flip side, waiting time, shape parameter, support,
  toy data, heavy rainfall events, manufacturing precision, continuous uniform distribution,
  log-normal distribution, Dirac distribution / Dirac measures, overview diagram).

Noticed, not touched (not style):

* The profile bullets write the notation as `$Exp(\lambda)$`, `$Lognormal(\mu,\sigma^2)$`,
  `$Weibull(\lambda,k)$` (upright-less, italic), while the running prose of c20.2 and the
  discrete chapter use `\operatorname{Exp}`. Maths, so out of scope for this pass; an author
  might want `\operatorname{}` throughout.
* c16.1, the Hubble bullet: "the 'actual' distribution of the stars behind it" – "it" is the
  photograph; reads fine once seen, left.
