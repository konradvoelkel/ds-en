# Translator's notes: `relative-entropy.md`

German original `relative-entropie.md`, 173 blocks, 1 declared drop (the HHU lecture
recording link), 172 blocks in English. `tools/sync.py align` and
`tools/check_english.py` both pass; no `check-ignore` entries were needed.

## New terminology

Information theory, none of which is in `TERMINOLOGY.md` yet:

| German | English | note |
|---|---|---|
| Entropie | entropy | |
| Shannon-Entropie | Shannon entropy | no hyphen in English |
| Information, Selbstinformation | surprisal | the pointwise $I(x) = -\log P(\{x\})$; "self-information" is the other standard name. See *Decisions* – `expectation-variance.md` defines it and has to agree |
| Entropie-Beitrag | entropy contribution | the $-p\log p$ term |
| Verbundentropie | joint entropy | the section heading |
| bedingte Entropie | conditional entropy | |
| gemeinsame Information, Transinformation | mutual information | the German glosses itself with "englisch *mutual information*"; see *Decisions* |
| Kreuzentropie | cross-entropy | hyphenated, as in the ML literature |
| differentielle Entropie | differential entropy | |
| stetige Entropie | continuous entropy | the section heading |
| relative Entropie | relative entropy | already in the glossary; Kullback–Leibler divergence, en dash, where the German says so |
| KL-Divergenz | KL divergence | no hyphen in English (`KL divergence to the labels`) |
| Entropischer Satz von Bayes | entropic Bayes' theorem | |
| invariantes Maß | invariant measure | Jaynes's $m$ |
| Bezugsmaß | reference measure | |
| Lebesgue-Maß | Lebesgue measure | |
| Radon-Nikodym-Ableitung | Radon–Nikodym derivative | en dash in the name |

Mathematical furniture that came up and is worth fixing once:

| German | English | note |
|---|---|---|
| vollständig additiv | completely additive | the $l(ab) = l(a)+l(b)$ condition |
| monoton wachsend / fallend | monotonically increasing / decreasing | |
| streng monoton | strictly monotonic | |
| konkav, streng konkav | concave, strictly concave | |
| Konvexkombination | convex combination | |
| Basiswechsel | change of base | |
| Funktionalgleichung | functional equation | |
| Mittelwertsatz | mean value theorem | |
| Ungleichungskette | chain of inequalities | |
| Riemann-Summe | Riemann sum | |
| Produktverteilung | product distribution | $P_X \times P_Y$ |
| Klassenzugehörigkeit | class membership | in the clustering passage |
| Klassenbezeichnung | class name | the labels whose permutation mutual information ignores |
| Loss-Funktion | loss function | the German keeps the English word; so do we |

## Figures

The brief said this chapter uses the four `entropie-gas-*.png` figures. **It does not.**
They are used by `expectation-variance.md` (German `erwartungswert.md`), in the
`:::{note}` digression "Woher das Wort kommt" under the heading `## Entropie`, which is
where the thermodynamics passage about gas, macrostates and disorder lives – not in this
chapter. That chapter was still untranslated when I looked, so whoever has it should be
told that the gas digression is theirs. The only figure in *this* chapter is
`images/1920px-Entropy-mutual-information-relative-entropy-relation-diagram.svg.png`.

I opened all four gas images anyway, as asked:

| file | text found |
|---|---|
| `entropie-gas-hoch.png` | **none** – a grey rectangle with a blue border and ~20 blue particle glyphs spread evenly |
| `entropie-gas-niedrig.png` | **none** – same box, all particles crowded into the left-hand side |
| `entropie-gas-hoch-geteilt.png` | **none** – same box with a thick blue vertical divider, roughly equal numbers of particles each side |
| `entropie-gas-niedrig-geteilt.png` | **none** – same box with the divider, all particles left of it, right half empty |

So all four are **clean**: no labels, no captions, no units, nothing language-dependent.
They need no redrawing. (I did not edit `images/README.md`; its four "labels to check /
to do" rows for these files can be closed as "clean".) The one figure this chapter does
use is a Wikimedia Commons SVG rendered to PNG; its Venn-diagram labels are already
English ($H(X)$, $H(Y)$, $I(X;Y)$ and so on are symbols), so nothing to redraw there
either – but its *caption* was German and is translated.

## Decisions and doubts

**1. `Information` → `surprisal`.** This is the one a human should look at. Block 35
points back to the chapter *Expectation and variance*: "Die *Information* $I(x) = -\log
P(\{x\})$ aus dem Kapitel …". The German defines the quantity there as *Information*
(auch *Selbstinformation*); the exact English term is **surprisal** (or
*self-information*), and the brief lists surprisal as binding, so that is what I used.
That makes this a cross-chapter commitment: whoever translates `expectation-variance.md`
must call it *surprisal* in its definition, or the back-reference will point at a word
that chapter does not use. It also collides mildly with `I(x)` being read as
"information" in `H(X) = \mathbb{E}(I(X))` – the symbol is unchanged, only the name.

**2. "englisch *mutual information*".** The German definition reads "Die *gemeinsame
Information* (auch *Transinformation*, englisch *mutual information*)". The third item is
a German-to-English gloss and is vacuous once the text is English, so the block became
"The *mutual information* (also *transinformation*)". I kept *transinformation* because
it is a real, if rare, English term and because dropping both parentheticals would lose
the German book's habit of naming the synonyms a reader will meet elsewhere. If you would
rather have the parenthesis gone entirely, it is a one-block edit.

**3. "Die *Entropie* … von $p$ relativ zu $r$".** The definition block italicises
*Entropie*, not *relative Entropie*, and gets the word "relative" from the construction
"von $p$ relativ zu $r$". I kept that exactly: "The *entropy* (also: Kullback–Leibler
divergence $D_{KL}$) of $p$ relative to $r$ is". It reads slightly oddly in a chapter
titled *Relative entropy*, and the obvious alternative is to italicise "*relative
entropy*" instead – but that would change what the German defines, so I left it.

Smaller things:

* **Chapter title / cross-reference.** I used "Expectation and variance" for the link
  text to `expectation-variance.md` (twice) – that chapter's H1 was still German when I
  worked, so this is a guess from the filename. Check it against whatever title that
  translator settles on.
* **`\text{...}` with German inside.** Two found and fixed: `\text{ genau dann wenn }` →
  `\text{ if and only if }` (block 64) and `\text{Anzahl }` → `\text{number of }`
  (block 154).
* **`$1,2$`** in the clustering passage (cluster labels, not a decimal) became `$1$, $2$`
  – as written it reads like a German decimal comma to an English eye, and
  `check_english.py` masks maths so it would not have caught it.
* **"nicht klausurrelevant"** in the `:::{note}` opening *Continuous entropy* became
  "not part of the course proper", per TRANSLATION.md §2. The German has no bold there,
  so I added none, unlike the digressions in `intro-stochastics.md`.
* **Dashes.** The German `—` in block 3 and the `--` dashes in the first lemma became
  spaced en dashes.
* **"Entropischer Satz von Bayes"** → "Entropic Bayes' theorem". Some authors say
  "entropic chain rule"; the German coins its own name, so I translated the coinage.
* **"lassen wir den Teil einfach frech weg"** → "we cheekily drop that part". The German
  is deliberately informal at that point and the voice is worth keeping.
* **"Machine Learning Entwicklern"** (last block) → "machine learning engineers".
  "Developers" is the literal word; "engineers" is what the English-speaking industry
  calls them.
* **"$I_{X,Y}$" and "$\mathbb{E}_X I(Y)$"** in the joint-entropy and cross-entropy
  definitions are left exactly as the German has them. Both are a little loose
  notationally (the first is the surprisal of the pair, the second the expectation under
  $p$ of the surprisal under $r$), but that is the original's business, not the
  translation's.
