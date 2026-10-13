# normal-distribution.ipynb

German original: `normalverteilung.ipynb` (upstream `c7247a9`).
18 cells, 121 German blocks → 120 English blocks. One declared drop (`c0.1`, the HHU Mediathek
recording link, already in `sync/drops/normalverteilung.ipynb.json`), no additions, no
check-ignore entries. `nbtext.py check`, `nbtext.py syntax`, `sync.py align` and
`check_english.py` all pass clean.

## The "$N \ge 30$" heading

`statistical-tests.md` (line 381) links into this chapter with

> … as crude for this as described in the chapter [The normal distribution](normal-distribution.ipynb) under *The "$N \ge 30$" myth*.

The German heading is `## Praxisbeispiel: Der „$N \ge 30$“-Mythos`. It is now

```
## A practical example: The "$N \ge 30$" myth
```

so that the italicised section name in `statistical-tests.md` appears **verbatim** as a
substring of the heading, with the capital "The" and the plain ASCII quotation marks it uses,
and with `\ge` (not `\geq`) and the same spacing inside the maths. The German's
*Praxisbeispiel:* prefix is kept and translated rather than discarded – dropping it would have
made the heading match the reference as a whole, but it would also have thrown away content
the original has, and the reference is prose, not a MyST label, so a substring match is
exactly what it needs. If anyone later wants heading and reference to be character-for-character
identical, the right move is to change `statistical-tests.md` to quote the full heading, not to
amputate the heading.

The in-text mentions of the rule in cell 15 (`$N \ge 30$`-Regel → "the $N \ge 30$ rule") and
the phrase in the German title were kept in the same `\ge` notation throughout, so a reader
searching the page for the string finds every occurrence.

## New terminology

Proposed for merging into `TERMINOLOGY.md`. Everything the glossary already settles
(*Normalverteilung* → normal distribution and *Gaußsch* → Gaussian, *Binomialverteilung* →
binomial distribution, *Dichte* → density, *Verteilungsfunktion* → cumulative distribution
function, *Erwartungswert* → expected value, *Varianz* → variance, *Standardabweichung* →
standard deviation, *Zentraler Grenzwertsatz* → central limit theorem, *Faltung* →
convolution, *Träger* → support, *Stammfunktion* → antiderivative, *Stichprobe* → sample,
*Stichprobenumfang* → sample size, *Standardfehler* → standard error, *Stichprobenmittel* →
sample mean, *Tschebyscheff-Ungleichung* → Chebyshev's inequality, *rechtsschief* → skewed to
the right, *Schiefe* → skewness, *Merkmal* → feature, *Prozentpunkte* → percentage points,
*Faustregel* → rule of thumb, *Rechenregeln* → rules of calculation, *gemeinsam normalverteilt*
→ jointly normally distributed, *$k$-tes Moment* → $k$-th moment, *Take-Home-Message* →
take-home message, *Population* → population) was used as declared and is not repeated here.

| German | English | Note |
|---|---|---|
| Approximation der Binomialverteilung | Approximating the binomial distribution | section heading; the German noun phrase reads better as a gerund in a heading |
| Auswertungsvorschrift | analysis protocol | the documents that fix how a study's data are to be evaluated |
| Bauteil | component | the industrial-manufacturing example |
| de Moivre-Laplace | de Moivre–Laplace | en dash in the two-name theorem, as for *Radon–Nikodym* and *Berry–Esseen* |
| dreiecksverteilt | triangularly distributed | the sum of two uniforms |
| Ein Integral | An integral | section heading |
| Fehlerquelle | source of error | plural *sources of error*; distinct from *Abweichung* → deviation, already in the glossary |
| gestutzte Normalverteilung | truncated normal distribution | `scipy.stats.truncnorm`, last row of the maximum-entropy table |
| Glockenkurve, Glockenform | bell curve, bell shape |  |
| Konvergenz in Verteilung | convergence in distribution | the mode of convergence in the central limit theorem; the glossary already has *stochastische Konvergenz* → convergence in probability, which is a different thing |
| Laplace-Bedingung | the Laplace condition | $Np \ge 10$ and $N(1-p) \ge 10$; bolded lead-in inside the *Rule of thumb* admonition |
| Momenterzeugendenfunktion | moment generating function | no hyphens in English |
| Nebenbedingung | constraint | the maximum-entropy side condition |
| Nebenbemerkung | aside | rendered as the bolded lead-in `**Aside**:`, as the German has it; distinct from *Bemerkung* → Remark (the admonition), *Exkurs* → digression and *Einschub* → interlude |
| Normalapproximation | normal approximation | legend entry in cell 16 and running prose in cell 17 |
| Normalverteiltheit | normality | "normality is preserved under affine-linear transformations"; see *Decisions* |
| Ortsbestimmung | position fixing | the GNSS example |
| Praxisbeispiel (as an `##` heading) | A practical example | see the section above on the heading |
| Satz von Berry–Esseen | Theorem (Berry–Esseen) | admonition title; see *Decisions* |
| Satz von de Moivre-Laplace | theorem of de Moivre–Laplace | in running prose the German bolds only `**Satz**`, and so does the translation |
| stabil unter Faltung | stable under convolution |  |
| Standardisierung | standardisation | house `-ise` spelling; the noun for the map $X \mapsto (X-\mu)/\sigma$ |
| standardnormalverteilt | standard normally distributed | the adjective; *Standardnormalverteilung* → standard normal distribution |
| Steckbrief (einer Verteilung) | profile | the per-distribution summary pages of `important-continuous-distributions.ipynb`; that chapter is not translated yet and should use the same word |
| Stirling-Formel | Stirling's formula | genitive, as for *Satz von Bayes* → Bayes' theorem |
| Störeinfluss, Störung | disturbance | the independent error sources that sum to a normal distribution; not *Störvariable* → confounder, which the glossary already has |
| technosozial | techno-social | hyphenated |
| Verhältnis (von Schiefe und Umfang) | ratio |  |

## Code changes

Three code cells (3, 10, 16). No identifier was renamed: every name in this notebook was
already English or a bare mathematical letter (`binom_samples`, `x`, `xs`, `k`, `n`, `p`,
`fig`, `ax1`, `ax2`, `np_text`). Library names and keyword arguments (`binom.rvs`, `norm`,
`density=`, `bins=`, `loc=`, `scale=`, `color=`, `label=`, `alpha=`, `figsize=`) are untouched
per `TRANSLATION.md` §3. What changed is strings and one comment:

| cell | old | new |
|---|---|---|
| 3 | `plt.xlabel("$x$ binomialverteilt")` | `plt.xlabel("$x$ binomially distributed")` |
| 3 | `plt.ylabel("Dichte")` | `plt.ylabel("Density")` |
| 10 | `# Erwartungswert n p = 40, Varianz n p (1-p) = 24` | `# expected value n p = 40, variance n p (1-p) = 24` |
| 10 | `plt.ylabel('Dichte')` | `plt.ylabel('Density')` |
| 10 | `plt.title('Normalverteilungs-Dichte (rot) und Binomial-Histogramm (blau)')` | `plt.title('Normal density (red) and binomial histogram (blue)')` |
| 16 | `label="Binomialverteilung"` | `label="Binomial distribution"` |
| 16 | `label="Normalapproximation"` | `label="Normal approximation"` |
| 16 | `np_text = f"{n * p:g}".replace(".", "{,}")` | `np_text = f"{n * p:g}"` |
| 16 | `ax.set_title(f"$N = {n}$, $p = 0{{,}}01$   ($Np = {np_text}$)")` | `ax.set_title(f"$N = {n}$, $p = 0.01$   ($Np = {np_text}$)")` |
| 16 | `ax.set_xlabel("Anzahl der Erfolge")` | `ax.set_xlabel("Number of successes")` |

The two cell-16 lines are the only real code change rather than a string swap: the German
`.replace(".", "{,}")` existed *solely* to turn Python's decimal point into a German decimal
comma for the subplot title, and the hard-coded `0{{,}}01` did the same for $p$. Under
`TRANSLATION.md` §6 the English edition wants the point, so the replacement call is gone and
`np_text` now holds the plain `f"{n * p:g}"`. The titles it produces are
`$N = 30$, $p = 0.01$   ($Np = 0.3$)` and `$N = 1000$, $p = 0.01$   ($Np = 10$)`. The
`np_text` variable was kept rather than inlined so the diff against the German stays one line
per change. (`check_english.py` skips code cells, so the `{,}` would not have been caught
mechanically — worth remembering for the remaining notebooks.)

The axis label *Dichte* → *Density* is capitalised, matching the one existing notebook
precedent in the edition (`iris.ipynb`: `ylabel('Rate')`, `title('Survival rate by sex')` –
sentence-case titles, capitalised one-word labels).

All three code cells were extracted and executed outside the notebook and run without error,
producing the expected English labels. The notebook itself was **not** re-executed, as
instructed: the three stored outputs are PNG figures with German axis labels, titles and
legends baked in, and the central re-execution pass has to clear them. There are no
`text/plain` outputs in this notebook, so the images are the only German left in the file.

## Decisions and doubts

**1. The H1: "The Gaussian normal distribution", not "The normal distribution".** The German
H1 is `# Die Gausssche Normalverteilung`, and `TERMINOLOGY.md` settles *Gaußsch* → *Gaussian*,
so the faithful rendering keeps "Gaussian". The awkwardness is that three already-translated
cross-references – two in `expectation-variance.md`, one in `statistical-tests.md` – all use
the shorter link text `[The normal distribution](normal-distribution.ipynb)`, which will now
differ from the TOC entry and the page title. Nothing dangles (MyST resolves the file, not the
title), and a shortened link text is legitimate English prose, so I left both sides alone
rather than either dropping "Gaussian" from the chapter title or editing three files I am not
allowed to touch. **A human should decide** whether the edition prefers title and link text to
coincide; if so, the cheap fix is to lengthen the three link texts, not to shorten the title.

**2. `:::{admonition} Satz von Berry–Esseen` → `Theorem (Berry–Esseen)`.** `TRANSLATION.md` §5
fixes *Satz* → *Theorem* and forbids moving a theorem's name across a block boundary, but says
nothing about a name the German already puts *inside* the title. Two candidates: the natural
English name "Berry–Esseen theorem", or the parenthetical form. I chose the parenthetical,
because the sibling chapter `continuous-distributions.md` has already set that precedent with
`:::{admonition} Theorem (transformation formula)`, and because it keeps the fixed word
"Theorem" in first position where every other admonition in the book has it – which matters
for a reader skimming for the mathematical furniture. The name itself keeps the en dash the
German already uses.

**3. `Normalverteiltheit` → "normality".** The German coins an abstract noun from the
participle ("Die Normalverteiltheit bleibt also unter affin-linearen Transformationen
erhalten"). A literal "the property of being normally distributed is preserved" is
unobjectionable and dull; "normality" is the standard English term (as in "test for
normality", which is exactly the sense `statistical-tests.md` uses when it reaches for
Shapiro–Wilk). The risk is that "normality" in English also carries the everyday sense, and
that the glossary does not yet have the word. I used it, recorded it above, and flag it as the
one place where I chose the idiomatic English term over the transparent one. The same sentence
pattern recurs two blocks later for the sum of two normals, where the German says "die *Form*
bleibt erhalten" and the translation accordingly says "the *shape* is preserved" – deliberately
*not* "normality", because there the German has changed its own word.

**4. Smaller calls, for completeness.**

* *"alles andere überlässt man dem Zufall"* → "everything else you leave to chance", against
  the glossary's `Zufall` → *randomness* (from `random-variables-distributions.md`). "Leave to
  chance" is a fixed English idiom and the sentence is an aphorism, not a technical claim;
  "leave to randomness" is not English. The glossary row's own note says "chance" reads too
  colloquial *where the section argues that randomness is a modelling decision*, which is a
  different context from this one. Flagging it so the consistency pass can see the deviation
  was deliberate.
* *Transformationsformel* here means the density-transformation rule
  $p_Y(y) = \frac{1}{|a|} p_X(\frac{y-b}{a})$, **not** the $\mathbb{E}(g(X))$ theorem that
  `continuous-distributions.md` registered in `TERMINOLOGY.md` under the same German word. The
  German reuses the word; so does the translation ("the transformation formula"). The glossary
  row should probably gain a second line noting the two senses.
* `Satz` the admonition title is "Theorem"; `**Satz**` in the running prose of cell 6 ("die
  ganze Beobachtung heißt auch **Satz** von de Moivre-Laplace") stays bolded and lower case in
  the same position the German bolds it, per §1 on not relocating material.
* Both links to `multivariate-normal.ipynb` (not yet translated) got link texts consistent
  with that chapter's likely title: "The multivariate normal distribution" where the German
  capitalises a chapter name, "multivariate normal distribution" where it uses the inflected
  lower-case form. Whoever translates `multivariate-normalverteilung.ipynb` should check these
  two against the H1 they choose.
* `Praxisbeispiel`, `Nebenbemerkung`, `Steckbrief` and `Auswertungsvorschrift` are the four
  words in this chapter that the glossary had no answer for and that a later chapter is likely
  to meet again; they are in the table above.
* Typography: five em dashes (cells 12, 13, 15, 17) and one bare ` - ` (cell 13, the Lego
  sentence) became the book's spaced en dash; the German quotation marks in cells 12, 15 and
  17 became plain ones; the maths decimal commas `0{,}41`, `0{,}48`, `1{,}96`, `74{,}2`,
  `0{,}742`, `0{,}258`, `0{,}025`, `0{,}5`, `0{,}44`, `0{,}08`, `0{,}01`, `9{,}85`, `0{,}79`,
  `0{,}14` became points. `95\,\%` and `75\,\%` keep the thin space inside maths, per §6.
  `\text{ für }` and `\text{und}` inside display maths were translated.

## For a human to check

* Decision 1 – the H1 against the three existing cross-reference link texts. The only choice
  in this chapter with consequences outside it.
* Decision 3 – "normality".
* The notebook needs the central re-execution pass: all three stored figures still carry German
  axis labels, titles and legend entries.
* The heading section at the top of this file: confirm that a substring match is what the
  `statistical-tests.md` reference needs, and that keeping *A practical example:* was right.
