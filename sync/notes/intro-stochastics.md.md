# Translator's notes: `intro-stochastics.md`

## Style pass

39 of 114 blocks touched; block count, order and alignment unchanged (`sync.py align` and
`check_english.py` both pass). No maths, code, admonition titles, link texts, figure names
or terminology changed. "Stochastics" stays as the name of the field throughout; the two
optional digressions keep their discursive pacing – only sentence shapes were changed there.

Kinds of change:

* **German verb-final and topic-first word order undone**: "From the section of reality to
  the models leads **modelling**" → "**Modelling** leads from the section of reality to the
  models" (and the same for prediction); "A subset of Ω to which we assign a probability we
  call an event" → "… is called an event"; "A very practical definition for any set M … is
  this:" → "Here is a very practical definition for any set M …".
* **Calques replaced by the English idiom**: "Two things can be seen from this example" →
  "The example shows two things"; "the σ stands for the fact that" → "the σ signals that";
  "'set' is simply what is meant" → "it simply means 'set'"; "it should not go unmentioned
  that" → "it should be said that"; "read over the σ-algebra part" → "read past the
  σ-algebra part"; "as one might at first think" → "as it might first appear".
* **Nominalisations turned into verbs**: "different routes to determining the plausibility
  of a statement" → "different routes to the plausibility of a statement"; "we therefore know
  how a measure can be assigned to the open sets" → "we know how to assign a measure to the
  open sets"; "the Riemann integral is formed by approximating with" → "the Riemann integral
  approximates with"; "the non-measurable subsets are not constructible" → "cannot be
  constructed".
* **Long sentences re-hinged or split** (blocks 1, 11, 19, 32, 33, 45, 101, 102, 109, 110):
  the "while it is possible to define … it is not possible to do so uniquely" sentence
  became "can be defined non-constructively – but not uniquely"; the measure-theory
  paragraph (block 102) was turned round so the sentence states what is worth recording
  before giving the reason; the Lebesgue/universality paragraph (block 109) was joined on a
  dash where it had restarted with "It is also how".
* **"One"/"we" where English prefers "you"**: "as soon as one wants to calculate" → "as soon
  as you want to calculate"; "which we already know and have mastered" → "which we already
  know our way around".
* **Padding cut**: "a mathematical map cj" → "a map cj"; "With that we have all the
  ingredients together" → "all the ingredients"; "in such a way that" → "so that" (block 34).

Noticed but not touched (meaning, not style):

* Block 1's last clause – "here it is enough to take away when we are allowed to read past
  them" – is still thin in English; the German presumably says something like "what we take
  away is *when* we may skip these notions". It is now grammatical, but a human may want to
  make the point more directly.
* Block 24: "20 rainy days out of 30 become 2/3, whether you count for a month or for a
  year" – the "out of 30" already fixes a month, so the "or for a year" sits oddly. The
  German says the same, I assume.
* Block 33: "one that can be implemented on a computer just as well as the computer is a
  Turing machine" – I rendered "just as well as" as "insofar as", which is what the sentence
  means; please check it against the German.
* Block 60 calls Ω = {1,…,6} the die's "state space" while every other block (and
  TERMINOLOGY.md) says "sample space". If the German says *Zustandsraum* here the word is
  deliberate; if it says *Ergebnisraum* it should be "sample space". Not changed, because it
  is a terminology question.
* Blocks 35 and 37 (the two unnumbered display formulas written as `$…$` on their own line
  in the measure-problem digression) are prose blocks in `segment.py`'s eyes, not maths
  blocks. Harmless, but it means a change to those formulas upstream would be reported as a
  prose change.
