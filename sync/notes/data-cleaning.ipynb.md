# Translator's notes: `data-cleaning.ipynb`

German original `data-cleaning.ipynb`, 43 cells (24 markdown, 19 code), 82 blocks, one
declared drop (block `c0.1`, the HHU Mediathek recording link), 81 translated blocks.
`nbtext.py check`, `nbtext.py syntax`, `sync.py align` and `check_english.py` all pass.

No `sync/additions` entry – nothing was added. No further drops. **No
`sync/check-ignore/data-cleaning.ipynb.json` either**, which was unexpected: the chapter
keeps a good deal of German, but every piece of it sits inside backticks, inside double
quotes, inside a URL or inside a code cell, and `check_english.py` masks all four. The
check reports `clean` with zero findings, so there was nothing to record. The list of
German that deliberately survives is in *Code changes* below, so a later style pass can see
at a glance what must not be "tidied" – in particular, nothing in that list may be taken
out of its backticks, because that is what keeps the residue check honest.

The notebook was **not** re-executed, as instructed. The stored outputs are still the
German run; see *What a human must check*.

## New terminology

### Cleaning, logging and the chapter's own vocabulary

| German | English | note |
|---|---|---|
| Daten schrubben | data scrubbing | the German quotes the English already; `what-is-data-science.md` uses the same word |
| Protokollieren (rule 1) | log it | the imperative heading of the Principle admonition |
| Protokoll | log | "the table of assignments belongs in the log"; "three columns that are nothing but the log". Chosen because `what-is-data-science.md` already promises a chapter that "insists on logging every change made to the data" |
| Zielmetrik | target metric | the glossary has *Zielgröße → target variable*, not this |
| Verfälschung, verfälschen | distortion, to distort | the chapter's central verb: "every act of cleaning distorts the data" |
| Imputation | imputation | bold on first use, as in the German |
| Ausreißer | outlier | and *Ausreißer erkennen* → *spotting outliers* |
| Z-Score | z-score | lower case, matching the glossary's *z-Wert → z-value*, *z-Test → z-test* |
| Augenschein | – | "the first step is always to look"; there is no English noun that is not stilted |
| Messfehler / Vorzeichenfehler | measurement error / sign error |  |
| Lücke (in einer Spalte) | gap | not "hole", not "missing value" – the chapter contrasts genuine gaps with the ones it creates |
| Ersatzwert | substitute value | what `fillna` inserts |
| Maske | mask | already in the glossary from `numpy.ipynb`; the chapter's logging columns are masks |
| Metadatendatei | metadata file |  |
| Niederschlagshöhe | amount of precipitation | DWD's `RSK`, "in mm" |
| Sonnenscheindauer | duration of sunshine | DWD's `SDK` |
| sprechende Namen | telling names |  |

### Encoding and categorical values

| German | English | note |
|---|---|---|
| Encoding, Kodierung | encoding | one English word for the German's two |
| Dezimaltrenner | decimal separator | TRANSLATION.md §6 already calls it that |
| Tausendertrennzeichen | thousands separator |  |
| Freitextfeld | free-text field |  |
| Schreibweise (einer Stadt) | spelling | "seven spellings become two cities" |
| Übersetzungstabelle | mapping table | "translation table" would be confusing in a translated book, and a `dict` passed to `replace` is a mapping |
| Editierdistanz (Levenshtein-Distanz) | edit distance (Levenshtein distance) |  |
| Einfüge-, Lösch-, Ersetzungsschritte | insertions, deletions, substitutions |  |

### Regular expressions

| German | English | note |
|---|---|---|
| Baustein | building block | table header and running prose |
| Schreibweise (Tabellenkopf) | notation | table header; distinct from *Schreibweise* = spelling above, which is why both are recorded |
| passt auf (Tabellenkopf) | matches |  |
| Alternative | alternation | the operator, not "alternative" |
| Verkettung | concatenation | the glossary has *Verkettung (von Abbildungen) → composition*; for strings and regexes it is concatenation |
| Wiederholung | repetition |  |
| Zeichenklasse, negierte Zeichenklasse | character class, negated character class |  |
| Anker | anchor |  |
| Gruppe | group | and *Rückwärtsreferenz* below |
| Gier, gierig / faul | greed, greedy / lazy | the standard regex names; the German uses the same metaphor |
| Rückwärtsreferenz | backreference | one word in English |
| negativer / positiver Lookahead | negative / positive lookahead | the German keeps the English word too |
| Raw-String | raw string | two words |
| endlicher Automat | finite automaton | plural *automata*; "Vorlesung über formale Sprachen" → "the course on formal languages" |
| schwach / stark bindend | binding weakly / binding strongly | operator precedence, the axis the table is sorted on |
| Rechtschreibprüfer | spell checker |  |
| Anrede (Titanic) | title | the Mr/Mrs/Miss field; also the column name, see *Code changes* |
| Rettungsreihenfolge | the order in which people were rescued | rendered as a clause; "rescue order" reads as a product name |
| Überlebensrate | survival rate |  |
| Feature Engineering | feature engineering | lower case in English running prose |
| Beispielaufgabe (admonition title) | Example exercise | TRANSLATION.md §5 fixes *Übung / Aufgabe → Exercise*; this is the compound |

### Date, time and time zones

| German | English | note |
|---|---|---|
| naiv / bewusst (Zeitstempel) | naive / aware | Python's own pair, which is what the German is translating |
| Sommerzeit-Umstellung | daylight-saving change | `what-is-data-science.md` already says "daylight saving changes" |
| Zeitzonendatenbank | time zone database | "the *tz database* (also called the IANA time zone database)" |
| Ortszeit | local time |  |
| Unix-Zeitstempel | Unix timestamp | the glossary has *Zeitstempel → timestamp* |
| Einzeiler | one-liner |  |
| Zusammenfassen auf Monate | aggregating up to months | what `resample("MS")` does |
| Wochentag | day of the week |  |

### Terms taken over from the glossary rather than re-decided

`Daten putzen → Data cleaning` (the H1 and every one of the nine incoming links),
`Bereinigung → cleaning`, `Faustregel → rule of thumb`, `Grundsatz → Principle`,
`Lösung → Solution`, `Take-Home-Message → Take-home message`,
`Interquartilsabstand → interquartile range`, `Boxplot → boxplot`,
`mittlerer absoluter Fehler → mean absolute error`, `Kürzel → shorthand`,
`Merkmal → feature`, `Datensatz → dataset`, `Postleitzahl → postcode`,
`Zusammenhang → relationship`, `Streuung/Standardabweichung → standard deviation`,
`Skalenniveau → level of measurement`, `One-Hot-Encoding → one-hot encoding`,
`Zeichenkette → string`, `Erwartungswert und Varianz → Expected value and variance`
(link text), `Deskriptive Statistik → Descriptive statistics` (link text).

## Code changes

### Variables renamed

| old | new | cell |
|---|---|---|
| `basis` | `base` | 2 (the DWD base URL) |
| `ordner` | `folder` | 2 |
| `lokal` | `local` | 2 (the list of already-downloaded files) |
| `pfad` | `path` | 2 |
| `dateiname` | `filename` | 2 |
| `archiv` | `archive` | 2 |
| `datendatei` | `data_file` | 2 |
| `roh` | `raw` | 2 |
| `wetter` | `weather` | 4 |
| `wahrheit` | `truth` | 6, 14 |
| `geloescht` | `deleted` | 6, 14 |
| `kaputt` | `broken` | 6, 8 |
| `fehlerhaft` | `faulty` | 8, 10, 12 |
| `spalte` | `column` | 10, 14 |
| `ausreisser` | `outliers` | 10, 12 (a boolean mask over many rows, hence the plural) |
| `bereinigt` | `cleaned` | 12, 14, 16, 35, 37, 41 |
| `monat` | `month` | 14 |
| `strategien` | `strategies` | 14 |
| `ersatz` | `replacement` | 14 (comprehension variable) |
| `ergebnis` | `result` | 14, 20 |
| `wort` | `word` | 18 |
| `stadt` | `city` | 20 |
| `normalisiert` | `normalised` | 20 (house `-ise` spelling) |
| `tabelle` | `table` | 20 |
| `bekannt` | `known` | 20 |
| `naechste` | `closest` | 20 (the function; "nearest" would do as well) |
| `treffer` | `matches` | 20 (`get_close_matches` returns a list) |
| `muster` | `pattern` | 23 |
| `doppelt` | `doubled` | 27 |
| `zusammen` | `combine` | 31 (the dict handed to `replace`) |
| `monatlich` | `monthly` | 37 |
| `zeiten` | `times` | 39 |
| `lokal` | `local` | 39 (a different variable from the one in cell 2, as in the German) |
| `fehler` | `error` | 39 (the caught exception) |

`rng`, `station`, `fig`, `axs`, `z`, `utf8`, `latin1`, `urls`, `html`, `titanic`, `w`,
`s`, `name` were already English or neutral and are unchanged.

### Column names invented by the notebook, renamed

All of these are the *right-hand* side of `rename`, i.e. names this notebook chooses:

| old | new |
|---|---|
| `datum_roh` | `date_raw` |
| `temp_mittel` | `temp_mean` |
| `niederschlag` | `precipitation` |
| `sonne` | `sunshine` |
| `luftdruck` | `pressure` |
| `feuchte` | `humidity` |
| `temp_mittel_fehlt` | `temp_mean_missing` |
| `temp_mittel_ausreisser` | `temp_mean_outlier` |
| `temp_mittel_imputiert` | `temp_mean_imputed` |
| `datum` | `date` |
| `Anrede` (Titanic) | `Title` |

`temp_max` and `temp_min` were already English. The three logging columns
(`temp_mean_missing`, `temp_mean_outlier`, `temp_mean_imputed`) are named in the prose of
cells 15 and 40 and in the final table of cell 41 as well; each new name was grepped across
the whole notebook, and no cell refers to a German name any more.

### What stayed German because it is data

* **The DWD column names**, which are what the file contains and what the metadata
  document: `STATIONS_ID`, `MESS_DATUM`, `TMK`, `TXK`, `TNK`, `RSK`, `SDK`, `PM`, `UPM`,
  `eor`. They appear as `rename` keys in cell 4 and as backticked abbreviations in the
  prose of cell 3, where the *explanation* is translated and the name is not.
* **The DWD URL, the archive path and the filename matching** in cell 2, untouched: the
  base URL, `pathlib.Path(base.replace("https://", ""))` (so the local copy keeps the
  server's path), the glob `tageswerte_KL_{station}_*_hist.zip`, the regex
  `rf"tageswerte_KL_{station}_\d{{8}}_\d{{8}}_hist\.zip"` searched in the directory
  listing, and the member prefix `produkt_klima_tag`. A translated pattern here would
  break the chapter silently at re-execution, which is exactly the failure mode the brief
  warns about.
* **The misspelled city names** in cell 20 – `"Düsseldorf"`, `"Duesseldorf"`,
  `"düsseldorf "`, `"Dusseldorf"`, `"Köln"`, `"Koeln"`, `"Kln"` – and with them the
  normalisation that only makes sense for German: `.str.replace("ue", "ü")`,
  `.str.replace("oe", "ö")`, the mapping table `{"dusseldorf": "düsseldorf"}` and the
  target list `["düsseldorf", "köln"]`. These are the subject matter of the section:
  umlaut transcription (*ue* for *ü*) is a German data-entry habit, and an English reader
  needs to see it rather than a sanitised equivalent. The prose around them says what they
  are ("seven spellings become two cities"), and `Kln` / `köln` are discussed by name.
* **`"Düsseldorf"`** in cell 18, whose umlaut is the whole point of the UTF-8/Latin-1
  demonstration, and the mojibake `DÃ¼sseldorf` quoted in the prose of cell 19.
* **`k.A.`** in cell 17 – a German data-entry string for "no information", kept in
  backticks with that gloss added in brackets, because the paragraph is about exactly the
  junk that turns a numeric column into `object`.
* **The German date format `15.01.2025`** in cell 34's list of formats. It stands next to
  `01/15/2025`, and the sentence after it ("with the date `01/02/2025` guessing is a matter
  of luck") depends on both conventions being on the table.
* **`a(ffe|de)+`** in cell 33, the example pattern handed to the regex visualiser. It is a
  German word game (*Affe* / *Ade*), but it is also just a regex whose `+` loop the tool
  draws, and the sentence talks only about where the loop sits. Left as it is rather than
  invented afresh.
* **The URLs in cell 23**, including `https://www.hhu.de/studium` and
  `https://voelkel.pages.cs.uni-duesseldorf.de/ds-skript/` (the German edition's own
  address). They are the input of a URL regex; changing a URL is never a translation.

### German strings that were translated, with reasons

* `JJJJMMTT` → `YYYYMMDD` (prose of cell 3, comment in cell 14). This is notation that
  explains the layout of the date to the reader, not data. The actual format string handed
  to `to_datetime` is `"%Y%m%d"` and is unchanged.
* The HTML toy string in cell 25:
  `'<a href="eins.html">Eins</a> und <a href="zwei.html">Zwei</a>'` →
  `'<a href="one.html">One</a> and <a href="two.html">Two</a>'`. It is an invented
  demonstration of greedy versus lazy matching, not data from anywhere, and the pattern
  `<a href="(.*)">` matches it unchanged. See doubt 2.
* The doubled-word example in cell 27: `"Sie ist die die beste"` → `"She is the the best"`,
  with the comment `# 'die'` → `# 'the'`. The point is the backreference `\1`, which is
  language-neutral, and a doubled "the" is the same classic typo. See doubt 2.
* The merged Titanic categories in cell 31: the values `"Rang"` → `"Rank"` and `"Adel"` →
  `"Nobility"`. These are labels the notebook invents. Their **keys** (`Mlle`, `Ms`, `Mme`,
  `Dr`, `Rev`, `Col`, `Major`, `Capt`, `Sir`, `Lady`, `the Countess`, `Don`, `Jonkheer`)
  come out of `titanic.csv` and are untouched, as are `Name` and `Survived`.
* The strategy labels in cell 14, which become the index of the printed Series:
  `"Konstante 0"` → `"constant 0"`, `"globaler Mittelwert"` → `"global mean"`,
  `"globaler Median"` → `"global median"`, `"Monatsmittel"` → `"monthly mean"`,
  `"letzter Wert (ffill)"` → `"last value (ffill)"`, `"lineare Interpolation"` →
  `"linear interpolation"`. The padding was re-measured so the dict still lines up;
  `name="MAE in °C"` is unchanged.
* The display column labels in cell 20's `pd.DataFrame({...})`: `"roh"` → `"raw"`,
  `"normalisiert"` → `"normalised"`, `"zugeordnet"` → `"assigned"`. Invented, and printed.

### Comments, `print` strings, plot titles

All translated. Every inline comment in cells 2, 6, 8, 10, 14, 20, 23, 25, 27, 30 and 39,
including the three comments inside the `re.VERBOSE` pattern in cell 23 (which are part of
the regex source and were the one place where translating a comment changes a pattern –
harmlessly, since `re.VERBOSE` discards everything after `#`).

Every `print` label: `"\nFehlende Werte je Spalte:"`, the f-string
`f"{geloescht.sum()} von {len(wetter)} Tagesmitteln entfernt"`, `"Mittelwert mit Fehlern:"`
/ `" ohne Fehler:"`, `"Mittelwert nach Bereinigung:"`, the "values … are not measured but
inserted" sentence, the four encoding lines in cell 18, `"gierig:"` / `"faul:  "`,
`"Wochentag des ersten Eintrags:"`, `"Tage zwischen erstem und letztem Eintrag:"`,
`"lokal:"`, `"Unix-Zeitstempel:"`, `"Fehler:"`, `"Typ der neuen Spalte:"`. Where the German
padded a label so the output lines up (`"UTC:  "`, `"lazy:  "`), the padding was kept or
re-measured.

The two plot titles in cell 8: `"Temperaturmittel je Tag, mit Fehlern"` → `"Daily mean
temperature, with errors"` and `"Histogramm"` → `"Histogram"`. There are no axis labels,
legends or tick labels in this chapter.

## Decisions and doubts

**1. `Kennzahl` means two different things in this chapter, and I split it.** In the
Principle admonition it is the evaluation metric ("the metric with which you will later
measure the success of the whole pipeline"), and rule 3's heading *An der Zielmetrik
messen* confirms that reading. In cell 13 it is a descriptive summary figure ("most summary
measures, `mean` among them, simply leave `NaN` out"). `TERMINOLOGY.md` binds
*Kennzahl → summary measure* (from `statistical-tests.md`), which is right for the second
occurrence and wrong for the first – "the summary measure with which you measure the
success of the pipeline" is not English. So: **metric** in the Principle and in cell 13's
last sentence (*Zielmetrik* → *target metric*), **summary measure** for the `mean`-and-
friends sense. This is the decision I would most like a second opinion on, and the
glossary should probably carry *Zielmetrik → target metric* as its own row.

**2. Two German example strings that are not data, and that I translated.** The HTML
snippet in cell 25 and the doubled word in cell 27. Neither comes from a file; both are
invented one-off illustrations, in the same category as a plot title. An English reader
needs "the the" to see the typo the backreference catches, and needs to read
`<a href="one.html">One</a>` to follow which `>` the greedy `.*` ran past. I am confident
about cell 27 and slightly less so about cell 25, where `eins.html` / `zwei.html` could
have been left alone at no cost to comprehension. Flagging it because it is the one place
where I changed a string that a strict reading of "keep the German examples German" might
have protected. Nothing in the surrounding prose names either string, so both are
self-contained.

**3. `Anrede` → `Title`, and what that does to the exercise.** *Anrede* is a form of
address; in the Titanic literature the extracted Mr/Mrs/Miss field is universally the
*title*, so the invented column became `Title` and the prose says "extract the title into a
new column". The clash to watch for: *Titel* in the sense of a book title does not occur in
this chapter, and the prose of cell 29 spells out the record layout as
`Surname, Title. Forenames`, which is a description of the format and so was translated.
`Name` itself is a column of `titanic.csv` and stays.

**4. "Distinct values before: … after:" for `Ausprägungen vorher / nachher` (cell 20).**
The glossary has *Ausprägung → value, level*. As a `print` label, "Levels before:" is
opaque – the reader of the output has no way to know that "level" is the categorical
sense – so I used "Distinct values", which is what `nunique` returns and what the sentence
means. The prose nearby ("seven spellings become two cities") carries the point anyway.
This is a deliberate deviation from the glossary inside a string, not in the prose.

**5. `ausreisser` → `outliers`, plural.** The German name is number-neutral; the thing is a
boolean mask selecting two rows. English forces a choice, and the plural reads correctly in
`faulty.loc[outliers, …]`. The derived column, however, is `temp_mean_outlier` singular,
because for each row it says whether *that* value is an outlier – which mirrors the
German's own `temp_mittel_ausreisser`.

**6. `base` for `basis` (cell 2).** `base` is the plain translation and reads fine next to
`base + path.name`, but it is a slightly bare name for a URL. `base_url` would be clearer
and is a word the German does not have. Left as `base`.

**7. The German weather service's name (cell 0).** The German links "Open-Data-Portal des
Deutschen Wetterdienstes" and then uses "DWD" from cell 1 onwards without ever expanding
it. In English the link text became "open data portal of the German weather service
(DWD)", which both translates the German and introduces the abbreviation the rest of the
chapter relies on. The alternative – keeping *Deutscher Wetterdienst* as a proper name
under TRANSLATION.md §3 and glossing it – puts a German noun phrase in the reader's way on
the chapter's third paragraph for no gain, since every later mention is the abbreviation.
The URL is unchanged. A human should confirm the house preference here; nine chapters link
to this one, but none of them names the DWD.

**8. `Protokollieren` → "Log it."** Rule 1's heading is a bare infinitive in German, as are
rules 2 and 3 (*Hinterher hinschauen*, *An der Zielmetrik messen*). English bare
infinitives ("To log.") do not work as headings, so all three became imperatives: **Log
it.** / **Look again afterwards.** / **Measure against the target metric.** The noun
*Protokoll* then had to be the matching "log", which is also the word
`what-is-data-science.md` already uses when it points at this chapter.

**9. "binding weakly / binding strongly" (cell 29).** The regex table is sorted by operator
precedence, and the German says *schwach bindend* / *stark bindend*. English texts usually
say "lowest precedence" to "highest precedence", which is the clearer phrase – but it is a
different metaphor, and the German's own one survives translation intelligibly. Kept
literal.

**10. External links.** None needed an "(in German)" marker: regexone.com and the regex
visualiser are English, and the DWD opendata URL is a bare directory listing. The tool's
name keeps its American spelling as "regex visualizer" (TRANSLATION.md §6: American
spellings that are part of a name stay).

**11. Headings and anchors.** The seven `##` headings became "Loading the data and a first
look", "Outliers", "Missing values", "Data types, encoding and categorical values",
"Regular expressions", "Date, time and time zones", "Summary". Nothing in the book links to
a section inside this chapter – all seven incoming links are plain file links – so no
anchor breaks. The nine chapters that link here all call it *Data cleaning*, which is the
H1, and `titanic-eda-numpy.ipynb` still has the German link text `[Daten putzen]`; that is
not my file, but whoever translates it should land on *Data cleaning*.

## What a human must check

* **Re-execution is not cosmetic here.** Eleven column names changed, so the stored
  outputs do not just contain German prose – cells 2, 4, 6, 8, 10, 12, 14, 16, 20, 30, 31,
  35, 37, 41 display German column headers and German index labels next to code that no
  longer produces them. Cell 41's five-column log table is the worst of it.
* **The download happens at re-execution.** Cell 2 fetches a directory listing from
  `opendata.dwd.de` and downloads a ZIP on first run, into `opendata.dwd.de/...` under the
  working directory. I did not run it (and did not download anything), so the
  filename-matching path is untested in this edition. It is byte-for-byte the German
  original's, which is the strongest guarantee available without executing it.
* **The DWD data moves.** The archive is "historical" and gets another year appended
  annually; the filename regex is written for that, but cell 5's claim that the duration of
  sunshine "is missing on almost every day of 2025" is a statement about one particular
  download, and cell 15's ranking of the six imputation strategies is a statement about one
  particular random seed over that data. If the file has changed since the German run, the
  prose of cells 5 and 15 may no longer describe the output. That is inherited, not
  introduced, but the re-execution pass is when it would surface.
* **Doubt 1 (`Kennzahl` split into *metric* and *summary measure*) and doubt 2 (translating
  the two German example strings)** are the two I would most like reviewed.
* Cell 25's comments end with an unterminated double quote (`# takes up to the last ">`),
  copied from the German. Harmless inside a comment, and deliberate: the comment is
  pointing at the `">` in the pattern. Left alone so the diff stays a translation.

## Style pass

Markdown cells only; every code cell is byte-identical to the translated version
(`check_untouched.py HEAD` reports *prose only*). 41 of the 81 blocks changed, spread over
24 of the 24 markdown cells. `sync.py align`, `check_english.py`, `nbtext.py check`,
`nbtext.py syntax` and `check_untouched.py` all pass. Not re-executed.

**Nothing on the "what stayed German because it is data" list above was touched.** The DWD
codes, `k.A.`, `DÃ¼sseldorf`, `15.01.2025`, `a(ffe|de)+`, `Kln` / `köln` / `"Kln"`, the
`ue`→`ü` normalisation, the URLs and `YYYYMMDD` all stand exactly as the translator left
them, inside their backticks or quotes. The glossary's own coinages (*telling names*,
*mapping table*, *substitute value*, *gap*, *summary measure* / *metric*, *binding weakly /
binding strongly*, *log*) were kept even where a synonym would have read more smoothly.

Kinds of change:

* **German sentence shape undone.** Fronted objects and verb-final clauses turned round:
  "Which of the two it is, the number itself will not tell you" → "The number itself will
  not tell you which"; "Why, the data file does not say" → "The data file does not say why";
  "More robust is the variant with…" → "The variant built on…, is more robust".
* **"Anyone who…" / "one" → "you" or imperative** where the German was giving advice:
  "Anyone who works with them regularly should read" → "If you work with them regularly,
  read"; "anyone who needs something more exact takes" → "if you need something more exact,
  use"; "You should state the format, though, instead of letting it be guessed" → "State the
  format, though, rather than letting it be guessed". Rule 1 of the Principle now says what
  it means in English: "Every change goes into code, where it can be reproduced".
* **Nominalisations and padding cut.** "the largest part of a data scientist's daily work is
  not modelling" → "most of a data scientist's working day goes not on modelling"; "That is
  as it should be." folded into the previous sentence as "– as it should"; "the loop sits
  that the `+` creates" → "the loop created by the `+` sits".
* **Calques replaced.** "stands in the data at 6 o'clock" → "the data have sunrise at 6
  o'clock"; "the clock jumped" → "the clocks jumped"; "brings `difflib` along" → "ships
  `difflib`"; "goes backwards" (the automaton) → "backing up"; "That is wanted" → "That is
  intended"; "worth the trouble" → "worth learning".
* **Rhythm.** The time-zone paragraph's last sentence became one conditional ("Confuse the
  two and every time shifts by an hour or two – which nobody notices until…"); the Solution's
  survival rates are now one sentence with the percentages carried by "for `Mrs` and
  `Miss`…, for `Master`…, for `Mr`" rather than a colon-list.

Noticed but not touched:

* **c28.2 and c29.0 were edited and then put back verbatim.** `check_untouched.py` extracts
  maths with `\$\$?[^$]*\$\$?` and does not mask fenced code or backticks, so the `$` anchor
  in the fenced pattern `r"^<([a-z]+?)>(.*)</([a-z]+?)>$"` (c28.1) opens a "formula" that
  runs through c28.2, c29.0 and the regex table up to the `` `$` `` in the anchor row. Any
  prose change in that stretch is reported as *changed maths*. The two paragraphs therefore
  keep their translation-pass wording ("and then comes the next counterexample", "The lesson
  from this is well known and still holds unchanged"), which is slightly stiffer than the rest
  of the chapter. A human can either accept that or teach the checker to skip fenced blocks.
* **"70 to 80 per cent" / "above 50 per cent" in the Solution** are left spelled out, as the
  translator wrote them. TRANSLATION.md §6 fixes `78 %` → `78%` for figures with a sign; the
  German here is presumably words, so nothing was changed. Worth one glance for house
  consistency.
* **"binding weakly / binding strongly"** reads as a calque; the glossary binds it, so it
  stays. "lowest to highest precedence" is what an English regex text would say.
* The translator's doubts 1 (*Kennzahl* split), 2 (two translated example strings) and 7
  (the DWD's name in the link text) are untouched and still open.
