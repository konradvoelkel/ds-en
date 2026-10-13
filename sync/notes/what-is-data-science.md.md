# Translator's notes: `what-is-data-science.md`

## Style pass

Second pass (Fable), prose only. 10 of the 25 prose blocks were touched. Not a word was
changed inside the two verbatim English quotations (Bowne-Anderson, block 15; DJ Patil,
block 17) or in the two translated Goos quotations (blocks 7 and 8), which are definitions
and read cleanly. The figure directive, the `(ein-bunter-mix)=` target, every link text and
every `{cite}` key are untouched. `sync.py align`: 32 blocks aligned; `check_english.py`:
clean, with the two existing `check-ignore` entries (the Goos book title, the typographic
quotes inside the Patil quotation) still in force.

Kinds of change:

* **A grammatical slip in the Conway paragraph** (block 13): "someone who can read in data,
  turn a method loose on it and finds the results plausible … will believe those results" –
  the verbs did not agree. Now "someone who can read data in, turn a method loose on it and
  find the results plausible for their field will believe them, without being able to judge
  whether they are anything more than chance." Also "what makes data science" (*was Data
  Science ausmacht*) → "what data science consists of", which is what the German means, and
  "the domain knowledge you will bring later, from the field you end up working in" → "you
  will bring yourself, later, from whatever field you end up working in".
* **"the so-called"** (*das sogenannte*, block 19) dropped: "preparing data, the so-called
  'data scrubbing'" → "preparing data – 'data scrubbing'". "A lot of classical programming
  technique goes into it" → "A good deal of classical programming craft goes into it"; "the
  deviations from those standards that turn up in practice" → "the ways practice departs from
  them".
* **Subject-verb separation undone** (block 20): "Whether a blood pressure reading of $400$
  is a measurement error, or an age of $0$ a missing value, is written in no data format –
  only someone who knows the field, or who asks someone who does, can tell" → "No data format
  tells you whether … – only someone who knows the field can, or someone who asks a person
  who does." The passive "considerably better results can be had by taking care of the
  training data" → "taking care of the training data buys considerably better results".
* **Rhythm** in the Reinhart–Rogoff story (block 3): "found in it a selected range of cells
  that was five rows too short" → "found a selected cell range that was five rows short";
  "redo the numbers" → "recompute the numbers"; "With all three corrections" → "With all
  three corrected". Block 2: "it was an argument for austerity policy" → "it served as an
  argument for austerity", matching the section heading.
* **Smaller**: "a context for assigning meaning to the bit strings it contains" → "for
  giving meaning to the bit strings in it"; "Most of that context we never consciously
  notice" → "never registers consciously"; "we therefore have to fall back on the coding
  table" → "we have to go back to it"; "An hour of podcast" → "An hour-long podcast"; the
  Loukides paragraph (block 29) now puts "2010" before the link rather than dangling after
  it, "a simple hype" → "a passing hype", "a global trend that has been developing for more
  than ten years" → "more than ten years in the making", and the final "yet there is no
  doubt" → "; what is beyond doubt is".

Noticed but not touched:

* The DJ Patil quotation (block 17) ends without a full stop ("… the 'real' problem") and
  uses bullets as "•" characters inside a blockquote. It is quoted verbatim from the PDF and
  stays as it is; if the source has a full stop there, a human may add it.
* Block 4 ("Everything this course is about is in that story…") and block 31 ("What comes
  next") were already the best English in the file and were left alone.
* "Numpy, Pandas" capitalisation follows the book's convention, not the packages' own.
