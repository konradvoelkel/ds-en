# Translator's notes: `expectation-variance.md`

German original `erwartungswert.md`, 343 blocks, 2 declared drops, 341 blocks translated.

## New terminology

Terms I had to decide on that are not yet in `TERMINOLOGY.md`.

| German | English | note |
|---|---|---|
| Abweichung | deviation | the chapter's running word; "error" only inside the names `mae`/`mse`/`rmse` |
| mittlere absolute Abweichung | mean absolute error | German glosses itself with the English ("mean absolute error"); the two collapse into one in English, so the gloss is gone |
| mittlere quadratische Abweichung | mean squared error | same collapse |
| Verschiebungssatz | shift theorem | $\mathbb{E}(X^2)-(\mathbb{E}X)^2$; see "Decisions and doubts" |
| Sample-Standardabweichung | sample standard deviation | written `rmse` / $\sigma(v)$ in the text |
| zentriertes Sample / zentrierte Zufallsvariable | centred sample / centred random variable | |
| normiertes Sample | normalised sample | mean $0$, sample standard deviation $1$ |
| Lagemaße zentraler Tendenz | measures of central tendency | section heading |
| Modus | mode | |
| Zählfehler | counting error | the loss that counts every deviation equally (0–1 loss); the mode minimises it |
| Informationsgehalt | information content | |
| idealisiertes Sample | idealised sample | the chapter's own coinage, bold on first use |
| Stichprobenmittel | sample mean | |
| Mittelwert-Abweichungs-Zufallsvariable | mean-deviation random variable | $\overline{X_n^\ast}$ |
| stochastische Konvergenz | convergence in probability | the standard English name; "stochastic convergence" would be a Germanism |
| $P$-fast sicher | $P$-almost surely | |
| starkes / schwaches Gesetz der großen Zahlen | strong / weak law of large numbers | |
| Markov-Ungleichung | Markov's inequality | |
| Tschebyscheff-Ungleichung | Chebyshev's inequality | transliteration changes; the German spelling is not kept |
| Indikatorfunktion | indicator function | |
| zentrales Moment | central moment | |
| Schiefe | skewness | German glosses itself; collapses |
| Wölbung | kurtosis | same |
| St.-Petersburg-Paradoxon | St Petersburg paradox | British style, no full stops |
| Rechenregeln | rules of calculation | matches `intro-stochastics.md` |
| Produktregel | product rule | for $\mathbb{E}(XY)=\mathbb{E}X\,\mathbb{E}Y$ under independence |
| Einschub | interlude | section heading `### Interlude: the logarithm` |
| Exkurs | digression | matches `intro-stochastics.md` |
| dekadischer Logarithmus | common logarithm | base 10; "decadic" is not English |
| binärer Logarithmus | binary logarithm | |
| Basiswechselformel | change-of-base formula | |
| Binärstelle / Dezimalstelle | binary digit / decimal digit | |
| bit / nat | bit / nat | plural "bits", "nats" in running prose; unit names stay lowercase |
| Selbstinformation | self-information | |
| Makrozustand / Mikrozustand | macrostate / microstate | |
| zweiter Hauptsatz der Thermodynamik | second law of thermodynamics | |
| Trennwand | partition | the physical wall in the gas figures, not a set partition |
| Kreuzentropie | cross-entropy | |
| Transinformation, gemeinsame Information | transinformation, mutual information | English really only has "mutual information"; I kept both names because the German offers two |
| gemeinsame Verteilung | joint distribution | |
| Einzelverteilung | individual distribution | the marginals, but the German avoids "Randverteilung", so I avoided "marginal" |
| Ziehen mit/ohne Zurücklegen | drawing with/without replacement | |
| paarweise unabhängig | pairwise independent | |
| Mini-Batch | mini-batch | stays |
| stochastischer Gradientenabstieg | stochastic gradient descent | |

## Figures

My chapter references five images.

* `images/entropie-gas-hoch.png`, `entropie-gas-niedrig.png`, `entropie-gas-hoch-geteilt.png`,
  `entropie-gas-niedrig-geteilt.png` – **all four rows in `images/README.md` can be struck.**
  I opened each file: they are pure line drawings of a box with blue particle blobs (and, in the
  "geteilt" pair, a vertical divider). There is **no text of any kind** baked into any of them,
  German or otherwise, so nothing needs redrawing. The README lists them under
  "used in: relative-entropy" with "labels to check"; `relative-entropy.md`'s translator should
  not re-inspect them. I did not edit `images/README.md`, since it is outside my file list.
* `images/xkcd-password-strength.png` – the xkcd strip, English in the original, no row in the
  README table, nothing to do. Its caption in my file is translated apart from the strip's own
  English title, which stays verbatim.

## Decisions and doubts

1. **`Verschiebungssatz` → "shift theorem".** This is the hardest one, and the one I would most
   like a human to confirm. The identity $\mathbb{V}(X)=\mathbb{E}(X^2)-(\mathbb{E}X)^2$ has no
   settled English name: textbooks variously call it the computational/shortcut formula for the
   variance, or the König–Huygens identity. None of those is a *name* the way "Verschiebungssatz"
   is, and the chapter uses the name three times as a cross-reference ("that is the shift theorem
   with $m=0$"; "this is the counterpart of the shift theorem … for samples"), so it needs to be a
   name. "Shift theorem" is a literal rendering that is in use in English and keeps the
   cross-references readable. If you prefer "computational formula", it occurs at blocks 75, 93,
   167 and 174 of the English file and nowhere else.
2. **Self-glossing terms.** German repeatedly names a thing and then glosses it with the English
   technical term: *mittlere absolute Abweichung* (mean absolute error), *mittlere quadratische
   Abweichung* (mean squared error), *Schiefe* (skewness), *Wölbung* (kurtosis). In English the
   two halves are the same word, so I dropped the parenthesis rather than inventing a second name.
   The one place I did keep both is *Transinformation*/*mutual information*, because the German
   there is offering two genuinely different names rather than a translation.
3. **The "erwartungsvoll" pun** (block 149). "um erwartungsvoll eine Stichprobe zu analysieren"
   puns *Erwartungswert* against *erwartungsvoll* ("full of expectation"). I rendered it
   "for analysing a sample expectantly", which keeps the joke's shape but is thinner than the
   German. Worth a second opinion.
4. **German-specific examples kept as German.** The letter-frequency entropy (4.06 bits/character,
   {cite}`fox2008`), the "sch" trigram, and the password example `kabelkanal` are all facts about
   German, not about English. I kept them and said "German texts" / "a German word" explicitly, so
   the numbers stay true. The alternative – swapping in English figures – would have invalidated
   the citation. Flagging it because an English-edition reader may find it odd.
5. **`nicht klausurrelevant`** became "not part of the course proper" per TRANSLATION.md §2, twice
   (blocks 134 and 237).
6. **Thousands separators.** German wrote `32\,768` and `65\,000` with thin spaces. I used
   `32{,}768` and `65{,}000`, the British convention. Both sit inside inline maths, so
   `check_english.py` masks them and no ignore entry was needed – but note that the `{,}` spelling
   *would* be flagged as a decimal comma if it ever appeared outside maths.
7. **"Probe aufs Exempel"** (block 115) became "the acid test". "Sanity check" was the other
   candidate; "acid test" matches the register better.
8. **Section cross-reference by name.** Block 210 points forward to "section *Rules of calculation
   for the variance*". That is a plain-text reference, not a MyST target, so it has to match the
   heading at block 325 exactly – it does. If anyone retitles that section, both places move.
9. **`Bonbons` → "sweets"** (British, per TRANSLATION.md §6). "Candies" would be American.
10. **Figure captions** are translated; `:name:` labels and `{cite}` keys are untouched, as are all
    chapter link targets (the German file already pointed at the English filenames).
11. **No check-ignore entries and no additions** were needed: `sync/check-ignore/` and
    `sync/additions/` have no file for this chapter. `sync/drops/erwartungswert.md.json` was used
    unchanged (blocks 1 and 235, both lecture-recording links).

## Style pass

Block structure untouched (341 blocks, `sync.py align` clean, `check_english.py` clean); every
`$…$` / `$$…$$` string byte-identical before and after. 77 of the 172 prose blocks changed; the
formal furniture (definitions, theorem statements, most proofs) was left alone except where a
sentence of connective prose sat inside the admonition.

Kinds of change:

* **German sentence shape.** Fronted or split long subject–verb-separated sentences:
  "If the random variable is not uniformly distributed, however, but on the numbers … follows,
  say, the frequency …" → "Suppose instead that the random variable is not uniform but
  follows … the frequency …, say. Then …"; the strong-law statement now has a full stop after
  "satisfy a strong law of large numbers" and the apposition set off with dashes instead of
  commas; the "rack our brains" paragraph split into two sentences at "Instead".
* **Nominalisations and calques to verbs/idiom.** "the mean deviation is of interest" → "the
  natural quantity to look at is the mean deviation"; "turn the direction of view around" →
  "reverse the point of view"; "What can be recorded is this" → "What we can say is this";
  "a popular source of error" → "a frequent source of errors"; "a question of the unit of
  measurement and not of the matter itself" → "a question of units, not of substance";
  "does not hang on" → "depends not on"; "the detour was not one" → "the detour was no detour";
  "Substantively it is clear" / "That is right substantively too" → "Here it is obvious
  anyway" / "That makes sense too"; "the goodness of a model" → "how good a model is".
* **"one" → "you"/"we".** "one puts … and calls" → "we write … and call" (two adjacent
  blocks, kept consistent); "One therefore extends … and agrees that" → "So we extend … and
  set"; "to base $2$ one measures" → "you measure"; "one says that this sequence satisfies" →
  "is said to satisfy"; "So one usually takes the square root" → passive.
* **Connectives.** "From this we see:" → "So"; "Conversely, then," → "Put the other way
  round:"; "The converse reads the same way:" → "Read the other way round:"; "Checking:" →
  "Check:"; "In this connection another notion comes up" → "Another notion comes up … in this
  connection"; "Anyone wanting to halve the error" → "To halve the error you".
* **Padding cut.** "in the same way", "at all", "any more", "also", "only", "really" where they
  carried nothing; "a single outcome only" → "just one outcome"; "the question of the minimum,
  and it has, as we shall see in a moment," reordered so the parenthetical does not split the
  verb from its object.
* **Typography.** `'the' median` → `"the" median` (TRANSLATION.md §6, matches the definition
  block just above). "It's not a bug, it's a feature" → "That is not a bug, it is a feature":
  the chapter has no other contractions.

Noticed but deliberately not touched:

1. **`TERMINOLOGY.md` says "shift theorem" for *Verschiebungssatz*; the chapter says "Shortcut
   formula"** (lemma and proposition lead-ins, and "shortcut formula" three times in prose).
   One of the two has been changed since the translator's notes above were written. Terminology
   is out of scope for the style pass; someone needs to decide which is right and fix the other.
2. **"information (also the self-information)" vs. `TERMINOLOGY.md` row "Information,
   Selbstinformation → surprisal"**, whose note says this chapter "defines it and has to
   agree". It currently does not. Same remark: a terminology decision, not mine.
3. **`$\sigma(X) := \sqrt{\mathbb{V}(X)}$ is called the *standard deviation* of X.`** – the
   trailing X is bare, not `$X$`. Left as is because wrapping it adds a maths span; a one-key
   fix for whoever edits the definition next.
4. **"(independently of the pmfs in the discrete case)"** after "We have not yet explained what
   *independent* means". The German is "(unabhängig von den pmf im diskreten Fall)", a pun on
   *unabhängig* that does not survive and leaves the parenthesis opaque in both languages. Kept
   verbatim; a human may want to drop or rephrase it upstream.
5. **"the probability of deviations that large is roughly inversely proportional to the
   square"** after Chebyshev. "Roughly" sits oddly next to an exact bound; the German has it, so
   it stays.
6. **"with $1$ for "a", $26$ for "z" and so on"** – "and so on" after the last item. German
   habit; kept.
7. The "expectantly" pun and the German-language entropy examples: see "Decisions and doubts"
   above; nothing new.

## Title lengthened (2026-10-16)

The chapter title diverges from the German original, deliberately. Both editions had
left this one thin; this edition lengthened it, the original did not (checked at
`2784f10`). `sync.py check` hashes the German side, so the divergence is invisible to it:
if this block ever comes back as stale, re-translate the German sentence and then
re-apply the longer title rather than restoring the short one.

The constraint that shaped the wording is that a chapter title is also the printed
heading in the PDF, so it had to read as a heading and not as a search phrase -- the same
call the original made for its own twelve titles (`todo/seo-kritik-bewertung.md`,
[SEO-8], Variante 2). `short_title` keeps the sidebar short.
