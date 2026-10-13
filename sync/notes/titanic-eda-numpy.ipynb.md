# Translator's notes: `titanic-eda-numpy.ipynb`

German original `explorative-analyse-mit-numpy.ipynb` (per `sync/filemap.json`),
**27 cells, 42 German blocks → 41 English blocks**. One declared drop, already present in
`sync/drops/explorative-analyse-mit-numpy.ipynb.json`: block **c0.1**, the HHU Mediathek
link to the German lecture recording *Datenexploration mit Numpy* (TRANSLATION.md §2). No
further drops were needed, no `sync/additions` entry, and no `sync/check-ignore` entry –
`check_english.py` reports zero findings.

`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass.
The notebook was **not** re-executed: the stored outputs of cells 11, 13, 17, 19, 21 and 23
still carry the German `print` strings, and the figure in cell 15 still has the German plot
title baked into the PNG. That is the expected state before the central re-execution pass.
`titanic.csv` and `titanic.tsv` were not touched (checksums unchanged), and cell 5 still
writes exactly the same TSV: the loop only copies fields through `csv.reader`, so the header
row and every value come from `titanic.csv` verbatim.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`:

| German | English | Note |
|---|---|---|
| erster Anlauf (chapter title *Titanic EDA, erster Anlauf*) | a first pass | see *Decisions* – "a first attempt" is the literal reading |
| Überlebensquote, Überlebensanteil, Überlebensrate | survival rate | the German uses all three; English has one, and the notebook's own function is `survival_rate` |
| Anteil (in the grouped `print` labels and the $y$-axis label) | rate | the cell's own third loop was already English and said `Rate:`; see *Decisions* |
| Klassifikator | classifier |  |
| Label | label | the German already uses the English word; bold on first use is kept |
| Ground Truth | ground truth | lower case and italic in English running prose; `model-selection.ipynb` capitalises it in German and will have to follow |
| Konfusionsmatrix | confusion matrix | already in `TERMINOLOGY.md` under *Verwirrungsmatrix, Konfusionsmatrix* |
| Accuracy (Treffergenauigkeit) | accuracy | the German glosses the English word; the gloss collapses, as with *Störvariable/Confounder* |
| Precision (Genauigkeit) | precision | likewise |
| Recall (Trefferquote) | recall | likewise; the German's second gloss *in der Medizin Sensitivität* is informative and was kept, and it matches the glossary's `Sensitivität → sensitivity` |
| F1-Score | F1 score | two words, no hyphen; see *Decisions* |
| Fehlklassifikationsrate | misclassification rate | the thing the mode minimises; `expectation-variance.md` calls the same loss the *counting error* |
| Basisrate | base rate | already in `TERMINOLOGY.md` from `covariance.md` |
| Train-Test-Split | train-test split | lower case, italic; see *Decisions* |
| Umrechnung, Umrechnungsfaktor | conversion, conversion factor | the Bayes factor between precision and recall |
| Überschriftzeile, "die mit Überschriften daher kommt" | header row |  |
| Trennzeichen | separator | of a CSV/TSV field |
| Anführungszeichen | quotation marks | in the CSV-parser sense |
| Rettungsboote planen | planning lifeboats | the recall-versus-precision example |
| Losung ("Frauen und Kinder zuerst") | maxim | "women and children first" is the established English form of the order |
| Zeile (einer Datei) / Zeile (einer Tabelle) | line / row | two senses in this chapter: `file.readline()` output is a *line* (c2.0, c2.1), a data record is a *row* |
| Daten verfälschen | to distort the data |  |
| protokollieren | to put on record |  |
| Instanz | instance | already in `TERMINOLOGY.md` under *Beobachtung, Instanz* |
| Auszug (aus der Passagierliste) | extract |  |
| Spam aussortieren | sorting out spam |  |

Reused unchanged from the already-translated chapters: *Daten putzen* → **[Data
cleaning](data-cleaning.ipynb)**, *Deskriptive Statistik* → **[Descriptive
statistics](descriptive-statistics.md)**, *Erwartungswert und Varianz* → **[Expected value
and variance](expectation-variance.md)**, *Kovarianz und Abhängigkeit* → **[Covariance and
dependence](covariance.md)**, *Satz von Bayes* → **[Bayes'
theorem](covariance.md)**, *Modell-Auswahl* → **[Model
selection](model-selection.ipynb)**, *Maßzahl/Kennzahl* → **summary measure**, *Merkmal* →
**feature**, *Modus* → **mode**, *Korrelationskoeffizient* → **correlation coefficient**,
*Maske* → **mask**, *explorative Datenanalyse* → **exploratory data analysis (EDA)**. All
link targets in the German already pointed at the English filenames; only the link text
changed.

## Code changes

### Names that are data and were therefore **not** translated

Every one of these is read out of `titanic.csv` / `titanic.tsv` by `np.genfromtxt(...,
names=True)`, so the string in the code has to match the file byte for byte:

* the column names `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`,
  `Fare`, `Cabin`, `Embarked` – in the `data['...']` lookups of cell 9 and in the
  `used_columns` set literal there;
* the values inside the data: `'female'` and `'male'` in cells 17, 19, 21, 23 and 26, and
  the `Embarked` levels `S`/`C`/`Q`, which the notebook never writes out but which appear
  in the stored output of cell 7.

`titanic.tsv` is committed and read by `pandas.ipynb` and `data-cleaning.ipynb`, so cell 5's
output had to stay byte-identical; translating a column name would have silently rewritten a
shared data file.

Three further names look translatable but are **not** German, so they were left alone:

* the bin labels `'Unknown'`, `'Adult'`, `'Child'`, `'Senior'` in cell 13 are invented by
  the notebook but were already English in the original;
* `survival_rate`, `age_filled`, `non_nan_age`, `used_columns`, `all_columns`,
  `unused_columns`, `age_group`, `missing`, `prediction`, `truth`, `tp`/`fp`/`fn`/`tn`,
  `is_female`, `is_male`, `corf`, `corm`, `labels`, `rates` – all already English;
* `Age Group`, `Total`, `Survived`, `Rate` in the third `print` of cell 13, and the whole of
  cells 1, 3, 6, 7, 9 and 26, which carried no German at all.

### Identifiers renamed, old → new

| old | new | where |
|---|---|---|
| `quelle` | `source` | cell 5 |
| `ziel` | `target` | cell 5 |
| `zeile` | `row` | cell 5 (loop variable over `csv.reader`) |
| `feld` | `field` | cell 5 (comprehension variable in the `assert`) |
| `kennzahlen` | `summary_measures` | cells 19 (definition) and 21 (call) – see *Decisions* |
| `p_ueberlebt_wenn_frau` | `p_survived_if_female` | cell 23 |
| `p_frau_wenn_ueberlebt` | `p_female_if_survived` | cell 23 |
| `p_frau` | `p_female` | cell 23 |
| `p_ueberlebt` | `p_survived` | cell 23 |

Each rename was grepped across the whole notebook; no occurrences were left behind and no
other file in the repository refers to these names (they are notebook-local).

### Strings, comments and figure text

* **Comments**: cell 5 (both), cell 11, cell 13 (`# neues Feature`, `# Gruppieren nach
  Sex`, `# Gruppieren nach Passenger Class`, the `# Binning` line's trailing note), cell 17
  (all six), cell 19 (the `precision` guard), cell 23 (all four). `# Binning` itself was
  already English.
* **`print` strings**: cell 11 (two), cell 13 (the `Sex:` and `Pclass:` lines), cell 17
  (the three-line confusion-matrix table), cell 19 (the two classifier names and the
  summary line), cell 21, cell 23 (three lines, the last one split across two f-strings).
* **Column alignment preserved.** The confusion-matrix table in cell 17 was re-laid-out so
  the two numeric columns still sit under their headings: `"predicted: died  survived"`
  with the `{:4d}` fields ending in the same columns. The `{name:18s}` field in cell 19
  still accommodates the longest label (`nobody survives`, 15 characters), and cell 21's
  literal label `Women and children ` is 19 characters wide, exactly matching cell 19's
  18-wide field plus its separating space, so the three lines of that little table still
  line up.
* **Figure text**: cell 15, `plt.title('Überlebensanteil nach Geschlecht')` → `'Survival
  rate by sex'` and `plt.ylabel('Anteil')` → `'Rate'`. This is the chapter's only figure
  and it is generated by the notebook, so it needs no entry in `images/README.md` – it will
  be correct after the re-execution pass.
* **Maths text translated**: `$P(\text{überlebt} \mid \text{vorhergesagt})$` →
  `$P(\text{survived} \mid \text{predicted})$` and the mirrored one in block c18.2,
  following the `\text{Evidenz} → \text{Evidence}` precedent in `covariance.md`.
  `$1 - \text{Accuracy}$` in block c20.1 was left exactly as it stood – it was already
  English – even though running prose now says "accuracy" lower case.
* **`scikit-learn`** is spelled lower case in both places (blocks c0.2 and c22.0). The
  German capitalises it at the start of a parenthesis in c0.2 and lower-cases it in c22.0;
  TRANSLATION.md §6 keeps a library's own spelling, and `intro-python.ipynb` uses
  `Scikit-Learn` in a bulleted list of library names, which is a different context.

## Decisions and doubts

**1. `kennzahlen` → `summary_measures` (cells 19 and 21).** `TERMINOLOGY.md` binds both
*Maßzahl* and *Kennzahl* to **summary measure** (and explicitly rejected "summary
statistic"), so blocks c18.0 and c22.0 say "summary measure". The function name follows the
prose rather than Python habit; the idiomatic alternative in this exact context is
`metrics`, which is what a reader coming from scikit-learn expects and what the
`classification_report` of `model-selection.ipynb` effectively prints. **This is the one
identifier a human should sign off on.** If `metrics` is preferred, the change is local to
two cells (one definition, two call sites) and "metrics" would then want a glossary row of
its own, because *Kennzahl* already has one.

**2. *Anteil* → "rate", not "proportion" (cells 13 and 15).** The German's own cell 13 is
inconsistent: two loops print `Anzahl / Überlebt / Anteil` and the third already printed
`Total / Survived / Rate` in English. I made all three read `Total / Survived / Rate`,
which agrees with the function `survival_rate` and with "survival rate" in the prose, and
set the figure's $y$-axis label to `Rate` to match. The German's internal inconsistency
thus disappears; everything happened inside single code cells, so no block was merged or
split. In the markdown, *Anteil* in the sense "proportion of correct predictions",
"proportion of survivors among the women" stays **proportion** – there it is a share of a
set, not a rate attached to a group.

**3. The chapter title, `# Titanic EDA, erster Anlauf` → `# Titanic EDA, a first pass`.**
*Anlauf* is a run-up or an attempt; "a first attempt" is the literal rendering and "a first
go" the colloquial one. I chose "a first pass" because in English "a first pass over the
data" is exactly what this chapter is, and because "attempt" hints at failure, which the
chapter is not. `model-selection.ipynb` links here as `[Titanic EDA]`, i.e. with the subtitle
dropped, so nothing else depends on the wording. Flagged for the style pass.

**4. *Train-Test-Split* (block c22.1).** The German sends the reader to the chapter
*Modell-Auswahl* "unter *Train-Test-Split*", but `model-selection.ipynb` has no section of
that name – its heading is `## Training, Test und neue Daten`. So the italics name a concept,
not a target, and I rendered it as lower-case italic *train-test split*. If the translator
of `model-selection.ipynb` gives that chapter a section actually called "Train-test split",
this sentence should be re-pointed at it.

**5. *F1-Score* → *F1 score* (block c22.0).** Two words, no hyphen, which is the usual
English form. Note that `model-selection.ipynb` (still German) writes both `F1-Score` in
prose and `f1-score` as a scikit-learn output column; the second is literal program output
and must stay, the first should become "F1 score" when that chapter is translated.

**6. The English-term-plus-German-gloss doublets in block c18.1 collapse.** The German
writes `**Accuracy** (Treffergenauigkeit)`, `**Precision** (Genauigkeit)` and `**Recall**
(Trefferquote, in der Medizin *Sensitivität*)` – the English term of art, bolded, with a
German translation in brackets for the reader who does not know it. In English the first two
brackets are empty of content and were dropped, following the `Störvariable/Confounder`
precedent in `descriptive-statistics.md`. The third bracket keeps its second half, "in
medicine *sensitivity*", which tells the reader something the English word does not. The
bullet count and order are unchanged, so the block still aligns.

**7. *Zeile* is two different words here.** Blocks c2.0 and c2.1 and cell 3 talk about
lines of a text file (`file.readline()`); blocks c16.1, c18.0, c20.0 and cell 5 talk about
rows of a table. German uses *Zeile* for both. I translated by sense: "line 2 contains more
variables than the header row" in c2.0 – where the German's single word in fact does carry
both senses in one sentence, which is precisely the bug the cell is about.

**8. `\text{Accuracy}` keeps its capital (block c20.1).** The surrounding prose now reads
"accuracy" lower case, so `$1 - \text{Accuracy}$` is mildly inconsistent. I left it because
it is not German and because churning maths markup risks nothing in return. A style pass may
want to lower-case it; if so, it is one token in one block.

**9. Nothing in this chapter needed a translator's note or an addition**, and no block was
dropped beyond the declared lecture-recording link. Course-specific material is absent: the
chapter has no exercise, no "nicht klausurrelevant" marker and no slide reference.

**10. For the human reviewer, in order of risk:** (a) the `summary_measures` versus
`metrics` choice above; (b) the stored outputs and the cell-15 PNG are still German and the
re-execution pass must actually reach this notebook, otherwise the chapter reads English and
prints German; (c) cell 5 rewrites `titanic.tsv` on execution – the file is committed and
other chapters read it, and re-execution must leave its checksum unchanged
(`8fe78c34662af87d054287d94336515c` as of this translation).

## Style pass

Markdown cells only; every code cell is byte-identical to `HEAD` (`check_untouched.py`
passes, as do `sync.py align`, `check_english.py`, `nbtext.py check` and `nbtext.py syntax`).
**16 of 41 blocks changed**: c0.1, c0.3, c2.1, c4.0, c10.1, c16.1, c18.0, c18.2, c20.0,
c20.1, c20.2, c22.0, c22.1, c22.3, c24.0, c25.1. No block merged, split or reordered; no
maths, link, directive or column name touched.

Kinds of change:

* **German future and "shall" → English present or "will".** "we shall naively load" →
  "we naively load"; "which we shall meet later" → "which we will meet later"; "we shall
  quickly have the so-called correlation coefficient computed all the same" → "let us
  quickly compute the so-called correlation coefficient all the same" (c25.1).
* **"Whoever … wants" → "If you are … you want".** The *wer … will* construction in c22.0
  ("Whoever plans lifeboats wants to overlook no survivor") is a German relative idiom;
  English says "If you are planning lifeboats you want to overlook no survivor". The
  glossary's *planning lifeboats* / *sorting out spam* are kept verbatim.
* **Nominalisations and passives → verbs.** "We print the first two lines for manual
  inspection" → "Let us print the first two lines and inspect them by hand" (c2.1); "How
  data are held back so that …" → "How to hold data back so that …" (c22.1); "how such a
  decision is taken systematically and put on record" → "how to take such decisions
  systematically and put them on record" (c10.1).
* **One sentence split.** c10.1: "Whether you replace missing values by the median or leave
  those rows out is a decision that distorts the data; how …" → "Replacing missing values
  with the median or dropping those rows: either is a decision that distorts the data. How
  …". Same block, same two statements.
* **Calques replaced.** "takes more of the dead for survivors" (*hält … für*) → "mistakes
  more of the dead for survivors"; "the data we thought it up on" → "the data we dreamt it
  up on"; "it is right in 62% of cases" → "it is right 62% of the time"; "nothing other
  than" → "nothing more than"; "is something we shall meet again with Bayes' theorem" →
  "… will meet again under Bayes' theorem".
* **Clause order.** c16.1 "The label is the column we want to predict and which is known for
  the rows we have, the *ground truth*" → "The label is the column we want to predict; for
  the rows we already have it is known, and that is the *ground truth*", so that *ground
  truth* lands on the thing it names. c20.0 "for every row it predicts the most frequent
  class" → "it predicts the most frequent class for every row".
* **Punctuation.** A comma after the fronted chapter reference in c20.1; a semicolon between
  the two parallel clauses in c22.3; the parenthetical dash before "following the maxim" in
  c22.0 so the example reads as an aside, as in the German *etwa nach der Losung*.

Left alone on purpose:

* `$1 - \text{Accuracy}$` in c20.1 keeps its capital (translator's doubt 8). It is maths and
  `check_untouched.py` would flag it; the one-token inconsistency with lower-case "accuracy"
  in the prose stands and is a human's call.
* `summary_measures` versus `metrics` (translator's doubt 1) is a code question, outside this
  pass.
* "must never be repeated later on" (c22.1) keeps the German's *später*; it is slightly
  redundant in English but it is the author's emphasis.
* The chapter title "a first pass" (translator's doubt 3) reads well and was not revisited.

Noticed, not touched: c0.1 calls the chapter "a discrete analysis of the Kaggle Titanic
dataset". *Diskret* is the German's word and "discrete" is its translation, but the analysis
is not about discrete variables in the technical sense – the author may have meant something
like "a modest analysis". Meaning, so not mine to change.
