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
