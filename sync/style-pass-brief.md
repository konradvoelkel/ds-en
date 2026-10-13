# Style pass brief (Fable)

You are improving the English of an already-translated chapter of a textbook, in
/home/konrad/Sciebo/hhu/ds2026/ds-en. The translation is sound; what it sometimes still
has is the *shape* of German — long subject-verb-separated sentences, nouns where English
wants verbs, "one" where English says "you", and connectives translated one-for-one.

## Read first

1. `TRANSLATION.md` — binding. Section 1 (block alignment) and section 6 (typography)
   constrain you absolutely.
2. `TERMINOLOGY.md` — binding. 1069 rows. **Never change a term it fixes**, however much a
   synonym would read better. Consistency across 30 chapters is worth more than any single
   sentence.

## What you may change

Sentence shape, rhythm, word order, punctuation, paragraph-internal flow. Break up a
sentence that runs too long. Turn a nominalisation into a verb. Cut padding. Replace a
calque with the English idiom.

## What you may not change

* **Block structure.** Never merge, split or reorder paragraphs. The English is held in
  strict block alignment with the German so that a change upstream can be traced to the
  exact English paragraph. `python3 tools/segment.py <file>` shows the blocks.
* **Terminology** fixed by `TERMINOLOGY.md`.
* **Maths.** Not one character inside `$…$` or `$$…$$`.
* **Code.** In a notebook, change markdown cells only. Leave every code cell exactly as it
  is — the notebooks have been executed and their stored outputs match the current code.
* **Meaning.** You are not editing the book. If a sentence seems wrong, say so in your
  notes; do not fix it.
* **Admonition titles, link texts, figure names, MyST targets, citation keys.**

## Notebooks

Use the tool, with your own scratch path:

    python3 tools/nbtext.py export <nb> -o /tmp/<chapter>-style.txt
    # edit markdown cells only, keeping every "@@@ cell N kind @@@" marker
    python3 tools/nbtext.py import <nb> /tmp/<chapter>-style.txt

## When you are done

    python3 tools/sync.py align    <file>
    python3 tools/check_english.py <file>
    python3 tools/nbtext.py check  <file>   # notebooks only
    python3 tools/nbtext.py syntax <file>   # notebooks only

Then append to `sync/notes/<file>.md` a section **Style pass** listing the kinds of change
you made and anything you noticed but did not touch.

## Rules of engagement

No git commands, no commits, no building the book. Do not edit `TERMINOLOGY.md`,
`TRANSLATION.md` or `sync/progress.json`.
