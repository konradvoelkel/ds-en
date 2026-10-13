# Translator's notes: `pandas.ipynb`

German original `pandas.ipynb`, 56 cells, 80 blocks, one declared drop (block `c0.1`, the
HHU Mediathek recording link), 79 translated blocks. `nbtext.py check`, `nbtext.py syntax`,
`sync.py align` and `check_english.py` all pass. No `check-ignore` entries were needed and
no `sync/additions` entry either – nothing was added, nothing further dropped.

The notebook was **not** re-executed, as instructed: the stored outputs are still the German
run and now disagree with the sources in every renamed column (see *Decisions and doubts*,
item 11).

## New terminology

The chapter's vocabulary is mostly relational-database vocabulary, which `TERMINOLOGY.md`
did not yet have.

### Relational databases and SQL

| German | English | note |
|---|---|---|
| Abfragesprache | query language | "the standard query language for relational database systems" |
| Befehl (SQL) | command | the table of `SELECT`, `INSERT INTO`, … |
| Datenbankschema | database schema | the Definition admonition |
| Relationsschema | relation schema | plural *relation schemas*, not *schemata* |
| Relation | relation | |
| Tupel / Entität | tuple / entity | the rows of a relation |
| Attribut | attribute | the columns of a relation |
| Wertebereich (relational) | domain | **collides** with the existing glossary row *Wertebereich → range, set of values* (that one is 𝒳, the range of a random variable). The relational sense is *domain*, and the German already glossed itself "(domain)" |
| Schlüssel | key | |
| Primärschlüssel / Fremdschlüssel | primary key / foreign key | |
| Suchschlüssel | search key | the `CREATE / DROP INDEX` row |
| Inner Join | inner join | lower case in English running prose; bold kept |
| Left / Right Outer Join | left / right outer join | likewise |
| Full Outer Join | full outer join | likewise |
| Reihenfolge (der Zeilen) | order | "the row order after a `merge` is not guaranteed" |

### Pandas and the dtype table

| German | English | note |
|---|---|---|
| Spaltenname | column name | |
| Attributschreibweise | attribute notation | `df.sepal_width` as against `df["sepal_width"]` |
| Zeilenindex | row index | the thing `index=False` keeps out of the CSV |
| Art der Daten | kind of data | table header |
| Zeitpunkt / Zeitdauer / Zeitraum | point in time / duration / period | three German words that English keeps apart as `Timestamp` / `Timedelta` / `Period` |
| Intervall | interval | |
| Ganzzahl | integer | |
| kategoriale Werte | categorical values | |
| dünn besetzte Spalte | sparse column | |
| Zeichenkette | string | |
| Wahrheitswert | truth value | as in `intro-python.ipynb` |
| Zeitstempel | timestamp | |
| record array | record array | stays, it is the Numpy term |

### Grouping and the first look at a dataset

| German | English | note |
|---|---|---|
| Gruppenmittel, Gruppenmittelwert | group mean | |
| Gesamtmittelwert, Gesamtmittel | overall mean | not "total mean" – it is the mean over all observations |
| gewichtetes Mittel | weighted mean | the glossary has *arithmetisches Mittel → arithmetic mean*; this is the weighted version |
| Gruppengröße | group size | the weights |
| Erster Blick auf einen Datensatz | A first look at a dataset | section heading |
| Handarbeit | handwork | "still handwork with Numpy in the Titanic notebook" |

### Terms taken over from the existing glossary rather than re-decided

`Bitmaske → bitmask`, `Matrikelnummer → student number`, `Ausprägung → level`,
`Maßzahl/Kennzahl → summary measure`, `Exzess → excess kurtosis`, `Schiefe → skewness`,
`Wölbung → kurtosis`, `Beobachtung → observation`, `Merkmal → feature`,
`Datensatz → dataset`, `Simpson-Paradoxon → Simpson's paradox`,
`Kelchblatt/Breite → sepal/width`.

## Code changes

Every identifier and every column name the notebook invents. Nothing that comes out of a
data file was touched.

### Variables and file names

| old | new | cell |
|---|---|---|
| `spalten` | `columns` | 3 |
| `"beispiel.csv"` | `"example.csv"` | 7 (three occurrences: `to_csv`, `read_csv`, `os.remove`) |
| `wieder_da` | `back_again` | 7 |
| `klein` | `small` | 27 |
| `gruppenmittel` | `group_means` | 27 |
| `groessen` | `sizes` | 27 |
| `spezies` (DataFrame) | `species` | 30 |
| `breite` (DataFrame) | `width` | 30 |
| `alter` | `age` | 53 |

`is_dinner`, `sorted_tips`, `df1`, `df2`, `tips`, `titanic`, `url`, `df` were already
English and are unchanged.

### Column names

| old | new | invented or data? |
|---|---|---|
| `"spezies"` | `"species"` | **invented** – cell 3 builds the DataFrame from a literal dict written in the notebook; no file is read. Cell 30 rebuilds the same two columns, also from literals |
| `"kelchblattbreite"` | `"sepal_width"` | **invented**, same two cells. *Kelchblatt* → sepal, *Breite* → width per the botany section of `TERMINOLOGY.md` |
| `"Nr"` | `"No"` | **invented** – the key column of the two toy tables in cell 30, written as a literal dict. See doubt 1 |
| `"Gruppe"` | `"Group"` | **invented** – cell 27's five-row example DataFrame is a literal |
| `"Wert"` | `"Value"` | **invented**, same cell |

Left alone because the data file has them that way:

* `tips.csv` (downloaded from the pandas test data in cell 11): `total_bill`, `tip`,
  `smoker`, `day`, `time`, `size`, `sex`. These appear in the SQL comments too, where they
  are literal SQL and must match the file.
* `titanic.csv` (cell 47): `Sex`, `Age`, `Embarked`, `Pclass`.
* `df1` / `df2` in cell 32 use `key` and `value`, invented but already English.
* `"Petal.Width"` in the SQL snippet in cell 9 – a column of the iris table as a database
  would hold it, i.e. data, and inside a quoted SQL identifier at that.
* `tip_rate`, the computed column in cell 17, is invented but already English, and the SQL
  comment above it names it.

I grepped each new name across the whole notebook afterwards (`sepal_width`, `species`,
`No`, `Group`, `Value`, `small`, `group_means`, `sizes`, `age`, `width`, `back_again`,
`example.csv`) and each one is used consistently in every cell that mentions it. There is
no cell left referring to a German name.

### Comments and strings

All translated: `# dasselbe`, `# hier sieht man, dass Numpy dahintersteckt`,
`# Bitmaske`, `# tips.groupby("sex").count() wäre falsch, …`,
`# richtig: mit den Gruppengroessen gewichten`,
`# ueber den Schluessel Nr zusammengefuehrt, Reihenfolge egal:`, `# eine frische UUID`,
`# inner join ist der default`, `# Zustand vor der Änderung:`,
`# Zustand vor der nächsten Änderung:`, `# fehlende Werte mitzählen`, and the three
`print` strings in cells 13, 27 and 53 (`"Das ist ja gar nicht sortiert! …"`,
`"Mittel der Gruppenmittel:"` / `"Gesamtmittel:"` / `"gewichtet:"`,
`"Schiefe:"` / `"Exzess-Kurtosis:"`).

The SQL comments (`# SELECT * FROM tips WHERE …`) are code in another language and stay
verbatim – they are the whole point of the chapter's two-column structure.

There are no plots in this chapter, so no titles, axis labels, legends or tick labels.

## Decisions and doubts

**1. `Nr` → `No` (cell 30).** This is the one rename I am not sure of. *Nr* is the German
abbreviation of *Nummer*, and `No` is its direct English counterpart, which is how a
printed table would head such a column. `ID` would read more naturally to a programmer and
matches what the surrounding prose is about (a key that identifies a row), but it is a
different word, not a translation, and the prose explicitly says the key "can be a plain
number". I went with `No`. If a human prefers `ID`, it occurs three times in cell 30 and in
one comment, and nowhere else in the book.

**2. Column-name style (cells 3, 27, 30).** The German's invented columns are inconsistent:
the iris ones are lower-case single words (`spezies`, `kelchblattbreite`), the toy
group/value ones are capitalised (`Gruppe`, `Wert`). I kept the asymmetry –
`species`/`sepal_width` lower case with an underscore (as the brief specifies, and as every
iris dataset in the wild spells it), `Group`/`Value` capitalised. Tidying it would be a
change to the original's code style rather than a translation.

**3. `spalten` → `columns` (cell 3).** The plain translation. Note that `columns` is also an
attribute of `DataFrame`, so there is a faint risk of a reader confusing the local dict with
`df.columns`. `column_data` would be safer but is no longer a translation of the German
word. Left as `columns`; flagging it because the very next markdown cell talks about
attribute access and shadowing, which makes the coincidence slightly unfortunate.

**4. *Wertebereich* (domain) (cell 9, Definition admonition and the comparison table).** The
German glosses its own term with the English one: "ihren **Wertebereich** (domain)". In
English that gloss has nothing to gloss, so it collapses to "its **domain**" and the table
row becomes "| domain | the `dtype` of the column |". This is the same collapse the glossary
already records for *Merkmale / Features* and *Störvariable, Confounder*. It does mean the
English loses a word the German reader was being taught; nothing can be done about that
without padding the block. **Note the glossary collision**: `TERMINOLOGY.md` has
*Wertebereich → range, set of values* for 𝒳, the range of a random variable. Both are right
in their own chapter; the glossary should carry the relational sense as a second row rather
than have one override the other.

**5. Join names in lower case.** German capitalises *Inner Join*, *Left Outer Join* and so
on because they are nouns. English does not, so they are "the **inner join**", "the **left
outer join**". The bold is kept, since in each case the block is introducing the term.

**6. The "–" cells in the dtype table (cell 8).** The German table uses `—` as a
"no such thing" marker in the *Skalar* and *pandas-Datentyp* columns. That is not the
parenthetical dash of TRANSLATION.md §6, so "a spaced en dash" does not quite describe it;
I used a bare en dash `–`, which is the English typographic convention for an empty table
cell and also keeps `check_english.py`'s em-dash check quiet. Five rows are affected.

**7. Print alignment in cell 27.** The German pads its three labels with spaces so the
numbers line up (`"Gesamtmittel:            "`). The English labels have different lengths,
so I re-measured the padding: `"mean of the group means:"` is 24 characters, and the other
two are padded to 24. Worth a glance after the central re-execution, since this is exactly
the kind of thing that looks fine in the source and ragged in the output.

**8. Cross-reference link texts.** The targets already point at the English filenames; the
texts were German and I translated them, matching what other chapters already use:
`[Explorative Analyse]` → **[Exploratory analysis]** (cell 2; the chapter's own title is
*Explorative Analyse: Beispiele* and is rendered elsewhere as *Exploratory analysis:
examples*, but the German abbreviates it here, so I abbreviated too),
`[Regressionsanalyse]` → **[Regression analysis]** (cell 8, which is what
`linear-regression.ipynb` is called in the already-translated text – note that
`[Linear regression]` is also in use somewhere in the book and the consistency pass should
pick one), `[Putzen der Daten]` → **[Data cleaning]** (cell 8), `[Daten putzen]` →
**[Data cleaning]** (cell 52), `[Simpson-Paradoxon]` → **[Simpson's paradox]** (cell 26).
`[Relational data]` (cell 29) was already English and points out of the book. Nothing in the
book links to a *section* inside this chapter, so my two renamed headings
("From SQL to Pandas", "A first look at a dataset") break no anchors.

**9. Quotation marks (cell 46).** The German's `'kaputte'` is single-quoted, not „…“, so
TRANSLATION.md §6 does not apply; I kept single quotes for `'broken'`, which is also what
the translated `descriptive-statistics.md` does with `'data science'`.

**10. One sentence re-punctuated (cell 46).** The German has a double colon in one sentence
("`info` zeigt …: Vergleichen Sie mit dem Titanic-Notebook …: Dort haben wir …"). English
cannot carry two colons in one sentence, so the second became a full stop: "… compare this
with the Titanic notebook from the chapter on Numpy. There we converted …". Still one
block, still one paragraph; only the internal punctuation changed.

## What a human must check

* **Re-execution is mandatory, not cosmetic, for this chapter.** Five column names changed,
  so the stored outputs do not merely contain German prose – they contain *wrong column
  headers* (`kelchblattbreite`, `Gruppe`, `Nr`, …) next to code that no longer produces
  them. Until the central re-execution pass runs, cells 3–7, 27 and 30 read as
  self-contradictory.
* Cell 25 and cell 28 pass `np.size` to `agg`. That is the German original's code and it
  still compiles, but it is deprecated in current pandas and may warn or fail at the
  re-execution. Not a translation issue; flagging it because the re-execution will be the
  first time anyone notices.
* `Nr` → `No` (doubt 1) and the `Wertebereich` glossary collision (doubt 4) are the two
  decisions I would most like a second opinion on.
