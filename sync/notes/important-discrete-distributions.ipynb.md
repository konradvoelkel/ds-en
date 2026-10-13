# Translator's notes: `important-discrete-distributions.ipynb`

German original `wichtigste-diskrete-verteilungen.ipynb`, **26 cells, 99 blocks** –
98 after the one declared drop. One drop, already declared in
`sync/drops/wichtigste-diskrete-verteilungen.ipynb.json` before I started: block **c0.1**,
the HHU Mediathek link under the H1 (`TRANSLATION.md` §2). Nothing else was dropped and
nothing was added, so `sync/additions/` has no entry for this file. `check_english.py`
reports no findings, so `sync/check-ignore/` has no entry either.

`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass.

The notebook was **not** re-executed. The code was extracted and run outside the notebook
(`matplotlib` on the Agg backend) and every cell runs and prints the expected numbers; the
stored outputs are still from the German run, so cells 7, 9, 14, 19 and 24 still print
`erwartet:`, `nachgerechnet:`, `zum Vergleich, Gleichverteilung auf 4 Werten` and `bit`.
That is expected and waits for the central re-execution pass.

A note on the brief: the chapter does **not** contain a hypergeometric distribution. It
covers the discrete uniform, categorical, Bernoulli, binomial, Poisson binomial, Poisson and
geometric distributions, plus the binary entropy function and a worked maximum-likelihood
derivation for the binomial parameter.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | note |
|---|---|---|
| Achtung (admonition title) | Caution | not in the fixed table of `TRANSLATION.md` §5; `:class: warning` is kept |
| Annäherung an eine Verteilung | approaching a distribution | plot title in cell 20 |
| Aufruf (einer Methode) | call | table header *gesucht \| Aufruf* → *wanted \| call*; a different sense from the glossary's *Aufruf (einer Web-Anwendung)* → request |
| Ausfallwahrscheinlichkeit | failure probability | the Poisson binomial example |
| Ausgaberaum | output space | $\Delta_n$ as the output of a classifier |
| Bauteil | component | the defective-components running example; not "part" |
| binäre Entropiefunktion | binary entropy function | $h(p)$; the `###` heading |
| Chance (englisch *odds*) | odds | the German glosses itself with the English word, so the doublet collapses – see *Decisions* |
| Charge | batch | "components from different batches" |
| Der Vollständigkeit halber | For completeness | section heading |
| diskrete Gleichverteilung | discrete uniform distribution | already used in a code comment in `numpy.ipynb` |
| Exponentialreihe | exponential series | $\sum \lambda^k/k! = e^\lambda$ |
| Fehlerquelle | source of error | "the most frequent source of error" |
| Fehlversuch | failure | the geometric distribution's two conventions: trials up to the first success vs. failures before it |
| gedächtnislos | memoryless | and *Gedächtnislosigkeit* would be *memorylessness* |
| geometrische Verteilung | geometric distribution |  |
| Grenzfall | limiting case |  |
| Grenzübergang | passage to the limit | also the comment in cell 20 |
| höchstens abzählbar | at most countable | matches `random-variables-distributions.md` and `expectation-variance.md` |
| Indexverschiebung | index shift | in the Poisson expected-value computation |
| Ja/Nein-Merkmal | yes/no feature | follows the glossary's *Merkmal* → feature |
| Klassifikationsverfahren | classification algorithm | follows the glossary's *Lernverfahren* → learning algorithm |
| Kosmetik (nicht nur Kosmetik) | not merely cosmetic | rendered adjectivally |
| Leitfrage | guiding question |  |
| logistische Regression | logistic regression |  |
| logistische Sigmoidfunktion | logistic sigmoid function |  |
| Logit | logit | lower case in English running prose |
| Maximum-Entropie-Verteilung | maximum entropy distribution | unhyphenated attributively |
| Maximum-Likelihood-Schätzung | maximum likelihood estimation | the glossary has the *estimator* and the *principle*, not the act |
| Münzwurf | coin toss | cf. the glossary's *Würfelwurf* → throw of a die |
| Muster (von Erfolgen und Misserfolgen) | pattern | the combinatorial argument for the binomial pmf |
| Nullstelle | zero | "the only zero is at $p = \frac12$"; not "root" |
| Ohne Beweis | Without proof | the bolded last line of the limit theorem |
| Poisson-Binomialverteilung | Poisson binomial distribution | no hyphen in English |
| Poissonverteilung | Poisson distribution |  |
| Potenzmenge | power set | matches `intro-stochastics.md` |
| Präparat (radioaktives) | specimen | **not** "sample" – see *Decisions* |
| Rückblick | Looking back | section heading; mirrors the glossary's *Ausblick* → Looking ahead |
| Summenformel | summation formula | $\sum i^2$ |
| Tippfehler | typo | plural *typos* |
| Überlebensfunktion | survival function | the German glosses the English term with a German one; collapses – see *Decisions* |
| Verbindungsversuch | connection attempt |  |
| Versuch, Bernoulli-Versuch | trial, Bernoulli trial | "one probability per trial", "$n$ independent Bernoulli trials" |
| Zufallszahlengenerator | random number generator |  |
| σ-Algebra | σ-algebra | the source uses the bare σ character here rather than `$\sigma$`; kept as it stands |
| Satz von de Moivre-Laplace | de Moivre–Laplace theorem | en dash in the name, as for *Radon–Nikodym* and *Cramér–Rao* |

Already settled elsewhere and reused unchanged: *Wichtigste diskrete Verteilungen* → **The
most important discrete distributions** (the title `numpy.ipynb` and
`random-variables-distributions.md` already cite), *Zähldichte* → **discrete density**,
*Wahrscheinlichkeitsmassefunktion* → **probability mass function**, *kategoriale Verteilung*
→ **categorical distribution**, *Erfolg / Misserfolg* → **success / failure**,
*Erfolgswahrscheinlichkeit* → **success probability**, *Träger* → **support**, *Urne* →
**urn**, *Ziehen mit Zurücklegen* → **drawing with replacement**, *Wartezeit* → **waiting
time**, *Exkurs* → **digression**, *Ausblick* → **Looking ahead**, *Rechenregeln* → **rules
of calculation**, *Ecke (eines Simplex)* → **vertex**, *Pullover-Farben* → **jumper
colours** (the word `random-variables-distributions.md` uses), *Einführung in Deep Learning*
→ **Introduction to Deep Learning**.

Cross-reference link texts follow the titles the translated chapters already use:
*Zufallsvariablen und Verteilungen* → **Random variables and distributions**,
*Erwartungswert und Varianz* → **Expected value and variance**, *Stetige Verteilungen* →
**Continuous distributions**, *Statistische Modelle* → **Statistical models**,
*Wichtigste stetige Verteilungen* → **The most important continuous distributions**,
*Normalverteilung* → **The normal distribution**, and the section link
*Rechenregeln für die Varianz* → **Rules of calculation for the variance** (the heading that
is actually in `expectation-variance.md`). The section reference "Abschnitt Entropie" →
"section Entropy" likewise matches the heading there.

## Code changes

German identifiers renamed, each grepped across the whole notebook afterwards.

| old | new | where |
|---|---|---|
| `plotXdiskret` | `plotXdiscrete` | cell 3 (definition), cells 7, 9, 14, 22, 24 (calls) |
| `beschriftung` | `description` | cell 3, twice (assignment and the pmf title) |
| `wert` | `value` | cell 3, the comprehension variable |
| `werte` | `values` | cell 9, four uses, and quoted in the prose of cell 8 – see *Decisions* |
| `wahrscheinlichkeit` | `probability` | cell 16, twice |
| `kandidat` | `candidate` | cell 16, three uses |
| `h_strich` | `h_prime` | cell 12, twice |
| `verteilung` | `distribution` | cell 19, five uses inside `poisson_binomial_pmf` |
| `ohne_erfolg` | `without_success` | cell 19, twice |
| `mit_erfolg` | `with_success` | cell 19, twice |

Unchanged identifiers, deliberately: `poisson_binomial_pmf`, `ps`, `pmf`, `k`, `n`, `p`,
`lam`, `X`, `h`, `fig`, `ax`, `axs` – already English or neutral; and all library names and
keyword arguments (`basefmt=`, `where=`, `values=`, `size=`, `mu=`, `alpha=`, `label=`,
`linestyle=`, `color=`, `textcoords=`, `xytext=`, `ha=`, `figsize=`, `basefmt=`).

Strings and comments translated:

* The four comments in `plotXdiscrete` (cell 3), including the one explaining
  `tight_layout`, and the comment on `st.randint`'s exclusive upper bound (cell 7), the
  `# scipy rechnet in nat` note (cell 9) and the limit comment in cell 20. The German
  cell-20 comment is written without umlauts (`Grenzuebergang`, `waechst`); that quirk
  disappears with the translation.
* The docstring of `poisson_binomial_pmf` (cell 19), both paragraphs.
* Every `print` label: `erwartet:` → `expected:`, `nachgerechnet:` → `recomputed:`,
  `zum Vergleich, Gleichverteilung auf 4 Werten:` → `for comparison, uniform distribution on
  4 values:`, `Summe der pmf` → `sum of the pmf`, `bei p=0.2:` → `at p=0.2:`,
  `<- das Maximum` → `<- the maximum`, `(beide gleich lambda)` → `(both equal to lambda)`,
  `von Hand:` → `by hand:`, and `"bit"` → `"bits"` (three places).
* Every plot title, axis label, annotation and legend entry:
  `pmf von {name} mit {beschriftung}` → `pmf of the {name} with {description}`,
  `cdf von {name}` → `cdf of the {name}`,
  `Entropie einer Münze mit Erfolgswahrscheinlichkeit $p$` → `Entropy of a coin with success
  probability $p$`, `Ableitung: das Negative des Logits` → `Derivative: the negative of the
  logit`, `Maximum: 1 bit` → `maximum: 1 bit`, `$h(p)$ in bit` → `$h(p)$ in bits`,
  `Wie wahrscheinlich ist die Beobachtung $k=…$ bei $n=…$, je nach $p$?` → `How likely is the
  observation $k=…$ for $n=…$, depending on $p$?`,
  `Poisson-Binomialverteilung mit $p_i$ = …` → `Poisson binomial distribution with $p_i$ = …`,
  `Annäherung an die Poissonverteilung, $\lambda = …$` → `Approaching the Poisson
  distribution, $\lambda = …$`. The two legend entries in cell 20 are pure LaTeX
  (`\operatorname{Bin}`, `\operatorname{Pois}`) and needed nothing.
* The distribution names handed to `plotXdiscrete` as its `name` argument – they end up
  inside the title f-string – became `discrete uniform distribution`, `categorical
  distribution`, `binomial distribution`, `Poisson distribution`, `geometric distribution`.

`(f"$p$ = 1/6",)` in cell 24 is an f-string without a placeholder in the German too; left as
it stands rather than quietly tidied.

## Decisions and doubts

**`werte` → `values` next to the `values=` keyword.** Cell 9 reads
`st.rv_discrete(values=(values, p))`, and the prose of cell 8 quotes that call verbatim, so
the identifier and the quotation have to agree. `values` is the honest translation of
*Werte* and is what the surrounding prose calls them ("a sample of size $n$", "uniform
distribution on 4 values"); the repetition is legal Python and unambiguous, since the keyword
and the local name live in different namespaces. I considered `outcomes` (collides with
*Ergebnisse*, which this book uses for the elements of $\Omega$) and `support` (introduces a
technical word the German does not use at that point). Flagging it because a reviewer may
prefer the eye-comfort of a different name; if it changes, it has to change in cell 8's prose
and in cell 9's two other uses at the same time.

**The title f-string and the German dative.** The German builds
`f"pmf von {name} mit {beschriftung}"` and passes dative noun phrases in
(`"diskreter Gleichverteilung"`, `"kategorialer Verteilung"`, `"geometrischer Verteilung"`),
which is how German inflects after *von*. English has no such inflection, so the names become
plain lowercase noun phrases and the template takes the article: `f"pmf of the {name} with
{description}"` and `f"cdf of the {name}"`. That puts one word of English grammar into the
template rather than into the five call sites, which is also what keeps `Poisson distribution`
capitalised correctly while the others are not. The alternative, dropping the article
("pmf of discrete uniform distribution"), reads like a machine.

**`Achtung` → Caution, `Hinweis` → Note.** Neither title is in `TRANSLATION.md` §5's fixed
table, and no translated chapter has set a precedent yet (both appear only in
not-yet-translated notebooks). I took the two names that match the `:class:` already on the
blocks – `:class: warning` for *Achtung*, `:class: note` for *Hinweis* – and that read as
ordinary English admonition titles. If the book later wants "Warning" and "Note", or
"Caution" everywhere, these are the two rows to add to §5; there are four of them in this
chapter (two *Achtung*, one *Hinweis*, and the *Bemerkung* → Remark cases, which §5 already
settles).

**`Präparat` → specimen, not sample.** "Wie viele Atomkerne eines Präparats zerfallen in
einer Minute?" is about a lump of radioactive material. English would normally say "sample",
but this book spends four chapters on *Stichprobe* → **sample** and the very same cell is
about counting; "specimen" costs nothing and avoids the collision.

**Two German doublets that collapse.** Block c4.2 is
"Das `sf` steht für *survival function*, gelegentlich auch *Überlebensfunktion* genannt." –
the German glosses an English term with a German one, which is exactly the material an English
reader has no use for. The block becomes the single clause "The `sf` stands for *survival
function*.", shorter than the original but not merged with anything. Likewise the *Ausblick*
in cell 11: "Der Bruch $\frac{p}{1-p}$ heißt *Chance* (englisch *odds*)" becomes "the fraction
$\frac{p}{1-p}$ is called the *odds*". Both are the pattern the glossary's closing section
records, and neither crosses a block boundary.

**`bit` → `bits`.** The German writes the unit in the singular after a number
(`1{,}68 bit`); the glossary's *bit / nat* row says the English plural is used in running
prose. So the `print` strings and the $h(p)$ axis label say "bits", while the sentence "the
fair coin toss has the maximal entropy, namely $h(\frac12) = 1$ bit" stays singular because
the number is 1.

**Decimal commas.** Eleven of them, all converted per `TRANSLATION.md` §6, including the ones
inside display maths in cell 15 (`0{,}2^3 \cdot 0{,}8^7 = 0{,}008 \cdot 0{,}2097\ldots`) and
the $3{,}5$ / $2{,}92$ in the die bullet of cell 6. Worth a human glance: the `{,}`
spelling means `check_english.py` would not have caught a survivor inside `$…$`, since it
masks maths before searching.

**Terminology a human should confirm.** *Annäherung* → "Approaching" in a plot title is a
judgement call (the German noun, the English participle); "Convergence to" would be more
precise and less faithful, since the theorem on the preceding block is the convergence
statement and the plot is only the picture. And *Rückblick* → "Looking back" is built by
symmetry with *Ausblick* → "Looking ahead" rather than from precedent – "In summary" or
"Taking stock" would both be defensible, but the symmetry seemed worth more.
