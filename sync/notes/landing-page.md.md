# Translator's notes: `landing-page.md`

## Style pass

Second pass (Fable), prose only. 18 of the 22 prose blocks were touched; the four left
alone are the `:::{note}` written for this edition (blocks 2 and 3, already English) and
the first and third "pillar" paragraphs (blocks 19 and 21), which read as English already.
`sync.py align`: 30 blocks aligned, 4 English-only; `check_english.py`: clean. The mermaid
diagram, the table of contents directive, every link text and every `{cite}` key are
untouched.

Kinds of change:

* **Calques replaced by the idiom.** "is an excellent address for it" (*eine sehr gute
  Adresse*) → "is an excellent place to start"; "an application as a junior data scientist"
  (*eine Bewerbung als*) → "applying for a job as a junior data scientist"; "The exercise
  sheets are where reading turns into being able" (*Können*) → "where what you have read
  becomes something you can do"; "certainly the odd typo" (*sicherlich*) → "no doubt, the odd
  typo"; "Excepted from this is third-party content … For each of these the source is given
  on the spot" → "The exception is third-party content … The source of each is given where it
  appears".
* **The broken-off bold lead-in** (block 26): the German's "**Warum überhaupt ein Skript**
  / könnte man auch fragen" had become "**Why notes at all** / one might also ask", which
  renders as one run-on line. Now "**Why notes at all**, you might ask." The rest of that
  paragraph was reshaped ("Working on the exercises with commitment, and exchanging ideas
  freely with fellow students, is decisive for success in learning" → "Working through the
  exercises in earnest, and talking them over freely with fellow students, is what decides
  whether the learning succeeds").
* **"one" → "you"** (block 9: "one could then go deeper" → "you could go deeper"), and
  impersonal constructions turned round: "make first applications possible" → "get you to
  first applications"; "In the first session we gave ourselves an overview" → "The first
  session gave us an overview"; "On top of that, you are familiar with how these tasks can be
  solved with Python" → "you will know how to carry these tasks out in Python".
* **Nominalisations → verbs** in the module-competencies block (12): "should have acquired
  competencies in the foundations of probability for machine learning" → "should have a
  working grasp of the probability foundations that machine learning rests on". The eight
  numbered items are unchanged.
* **Padding cut**: "If you want to be able to work as" → "If you want to work as"; "you will
  also need knowledge of algorithms for" → "you will also need algorithms for"; "None of that
  is yet necessary" → "None of that is needed yet"; "All the mathematical foundations you
  need for working on the exercises are contained in" → "Every piece of mathematics you need
  for the exercises is in".
* Minor: "Professionally this opens" → "Professionally, this opens"; "The third is often
  overlooked" → "is easy to overlook"; "and everywhere a machine learning component is to be
  built into" → "and wherever a machine learning component has to be built into".

Noticed but not touched:

* Block 26 keeps "especially if your English is good" – a faithful rendering of "vor allem
  wenn man gut Englisch spricht", which is sensible advice to a German reader and slightly
  comic in an English edition. Whether to keep it is an editorial decision under
  TRANSLATION.md §2, not a style one.
* Block 11, "The first session gave us an overview of what data science is", and block 25,
  "(or among the course's entry requirements)", are course-organisation sentences that §2
  says to keep. They read as courseware in a standalone book; noted, not changed.
* Block 12's last list item, "and use them for classifying and predicting further data",
  carries the "and" inside the item, as the German module text does. Left, since the list
  is the module handbook's wording.
* The pillar paragraphs mix "we" and "you" ("we reimplement … so that we understand what
  happens when you call `model.fit()`"). That is the book's voice per TRANSLATION.md §6 and
  matches block 16; left.
