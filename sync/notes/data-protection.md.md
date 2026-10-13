# Translator's notes: `data-protection.md`

German original `datenschutz.md`, 51 blocks, 1 declared drop (the HHU lecture recording
link, block 1, already in `sync/drops/datenschutz.md.json`), 50 translated blocks.
`tools/sync.py align` and `tools/check_english.py` both pass. One `check-ignore` entry
(see below); no `sync/additions` entry – no English-only block was added, and nothing
further was dropped.

The chapter is a glossary of German and European data protection law. The governing
decision throughout: the law is German and European and stays that way. No UK or US
concept was substituted, nothing was softened into "in many countries", and the
GDPR's **official English vocabulary** was used rather than a literal rendering of the
German – controller, processor, data subject, processing, consent, legitimate interest,
purpose limitation, data minimisation, right of access, right to erasure. German legal
terms the reader will meet in a German context are given with the English term and the
German in brackets on first use. Article citations keep the German form
(`Art. 6 Abs. 1 lit. f`), with `GDPR` in place of `DSGVO`.

## New terminology

Only terms not already in `TERMINOLOGY.md`. The binding **Data protection** section of
the glossary covered the core vocabulary; these are the rest.

| German | English | note |
|---|---|---|
| Datenschutz (chapter title) | Data protection | matches `myst.yml` |
| Erwägungsgrund | recital | the official name for the GDPR's preamble numbers |
| Anwendungsbereich | scope | Art. 2 |
| Dateisystem (DSGVO Art. 2) | filing system | **not** "file system" – this is the official English wording, and the German *Dateisystem* is a false friend here |
| Zettelkasten | card index | the non-automated example of a filing system |
| Auftragsverarbeitung | processing on a controller's behalf | the activity; see `Auftragsverarbeitungsvertrag` for the contract |
| Auftragsverarbeitungsvertrag (AVV) | data processing agreement (AVV) | Art. 28; the GDPR itself says only "contract or other legal act", so the industry term is used and the German abbreviation kept |
| Recht auf informationelle Selbstbestimmung | right to informational self-determination | the *Volkszählungsurteil* term |
| Bundesverfassungsgericht | Federal Constitutional Court | German name in brackets on first use |
| Volkszählungsurteil | census judgment | German name in brackets, italicised |
| allgemeines Persönlichkeitsrecht | general right of personality | the standard rendering of the Art. 2(1) GG right |
| Bundesgerichtshof (BGH) | Federal Court of Justice | German name in brackets; the dashcam case |
| EuGH | Court of Justice of the European Union | spelled out on first use, "Court of Justice" thereafter |
| Richtlinie 95/46/EG | Directive 95/46/EC | EG → EC in the official English citation |
| Verordnung (EU) 2024/1689 | Regulation (EU) 2024/1689 | likewise for all five regulations in the last section |
| Durchführungsbeschluss | Implementing Decision | the official English name |
| Angemessenheitsbeschluss | adequacy decision | Art. 45 |
| Drittland, Drittlandübermittlung | third country, transfer to a third country | the GDPR's own English term |
| Rechtsbehelf | remedy | "no effective remedy" in *Schrems I/II* |
| Grundprinzipien (Art. 5) | basic principles | the six principle names all follow the official English: lawfulness/fairness/transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality |
| Verarbeitung nach Treu und Glauben | fairness | the official English of Art. 5(1)(a); the German phrase is quoted and glossed "in good faith" |
| Richtigkeit | accuracy | Art. 5(1)(d); not "correctness" |
| Speicherbegrenzung | storage limitation | Art. 5(1)(e) |
| Rechenschaftspflicht | accountability | Art. 5(2) |
| Datensparsamkeit | data parsimony | the pre-2018 BDSG principle, § 3a BDSG a.F.; quoted in German and glossed, since it is a term the GDPR dropped |
| a.F. (alte Fassung) | in the version then in force | kept as `a.F.` so the citation can be looked up, with the gloss after it |
| besondere Kategorien personenbezogener Daten | special categories of personal data | Art. 9; "sensitive data" only as the colloquial gloss the German also gives |
| grundsätzlich untersagt | prohibited in principle | *grundsätzlich* is not "fundamentally" here – the next clause says the prohibition is not absolute |
| Betroffenenrechte, Rechte Betroffener | rights of the data subject | Chapter III |
| Auskunft | access | Art. 15; the glossary's *Auskunftsrecht* → right of access |
| Berichtigung | rectification | Art. 16; not "correction" |
| Löschung | erasure | Art. 17; "right to be forgotten" as the quoted second name |
| Einschränkung der Verarbeitung | restriction of processing | Art. 18 |
| Mitteilungspflicht | notification obligation | Art. 19 |
| Datenübertragbarkeit | data portability | Art. 20 |
| Widerspruch | objection | Art. 21; not "contradiction", not "appeal" |
| Haftung | liability | Art. 82 |
| materieller / immaterieller Schaden | material / non-material damage | the official English pair |
| Schadenersatz | compensation | Art. 82 |
| Meldepflicht bei Datenpannen | notification of data breaches | Art. 33 |
| Datenpanne | data breach | the colloquial German for *Verletzung des Schutzes personenbezogener Daten* |
| meldepflichtig | notifiable | of a breach |
| Aufsichtsbehörde, die Aufsicht | supervisory authority | the GDPR's term; "the supervisory authority" also where the German shortens to *die Aufsicht* |
| Abhilfebefugnisse | corrective powers | Art. 58(2) |
| Verwarnung / Warnung | reprimand / warning | two different Art. 58(2) powers, and English keeps them apart |
| Beschränkung oder Verbot einer Verarbeitung | limitation or ban on processing | Art. 58(2)(f) |
| Geldbuße, Bußgeld | administrative fine, fine | Art. 83 |
| Zumessung | fixing the amount | of a fine |
| Vorsatz oder Fahrlässigkeit | intentional or negligent | Art. 83(2)(b) |
| Verhaltensregeln | codes of conduct | Art. 40 |
| Selbstregulierung | self-regulation |  |
| Rechtsgrundlage fehlt / fehlende Rechtsgrundlage | missing legal basis |  |
| Beschäftigtendatenschutz | employee data protection | the BDSG's remaining room under Art. 88 |
| Selbstgenerierter Code | self-generated code | the longitudinal-study technique |
| Längsschnittbefragung, Längsschnittstudie | longitudinal survey, longitudinal study |  |
| Erhebung (eine Welle) / Welle | wave | of a repeated survey; the glossary's *Erhebung* → data collection stays for the activity |
| Europäische Datenstrategie | European data strategy | the 2020 Commission communication |
| Mitteilung der Kommission | Commission communication |  |
| KI-Verordnung | AI Act | the German name in brackets; the English name is the one in use |
| KI-System | AI system | the AI Act's own English term |
| Hochrisiko-Anwendung | high-risk application |  |
| verbotene Praktiken | prohibited practices |  |
| Personalauswahl | personnel selection |  |
| Strafverfolgung | law enforcement |  |
| Datenvermittlungsdienst | data intermediation service | DGA's official English |
| Datenaltruismus | data altruism | DGA |
| Weiterverwendung geschützter Daten der öffentlichen Hand | re-use of protected public sector data | DGA |
| in Verkehr bringen | place on the market | AI Act product-regulation language |
| Machtgefälle | imbalance of power | the Skellefteå consent case |
| Gewinnspiel | prize draw | the AOK case |
| Rundmail | circular email |  |
| Zugangsdaten | login details | the phishing example |
| Airgap | air gap | two words in English |
| Schufa | Schufa, the German credit agency | glossed, since the name means nothing outside Germany |
| AOK | AOK, a statutory health insurer | likewise glossed |
| Kanzlei | law firm | CMS, who keep the Enforcement Tracker |
| Worum es ging (table header) | What it was about |  |
| Lagemaß (exercise) | measure of location | already in `TERMINOLOGY.md`; recorded here because the exercise is the only place this chapter uses a statistics term |

## Figures

**None.** The chapter has no `{figure}` directive, no `![…]`, and no reference to
anything under `images/`. Nothing to redraw, and no row to add to `images/README.md`.

## Decisions and doubts

**1. Official GDPR English, not translated German.** Every term that exists in the
official English text of the Regulation was taken from there rather than translated
afresh. The one that matters most is `Dateisystem` → **filing system** (Art. 2(1)):
translating it as "file system" would turn a rule about shoeboxes of index cards into a
rule about computers and reverse the point of the sentence that follows it ("a card index
therefore falls under it; a single sheet of notes does not"). The same applies to
*Berichtigung* → rectification (not "correction"), *Widerspruch* → objection (not
"appeal"), *Abhilfebefugnisse* → corrective powers, *Verwarnung* → reprimand as against
*Warnung* → warning, and *Verhaltensregeln* → codes of conduct. All quotations from
Art. 5, Art. 6, Art. 9, Art. 58 and Art. 83 are the official English wording, so that a
reader who opens EUR-Lex finds the same words.

**2. `nach Treu und Glauben`.** The hardest small decision in the chapter. Art. 5(1)(a)
German says *nach Treu und Glauben*, a term of art with a long history in German civil
law; the official English says simply "fairly". Substituting "fairness" silently would
hide something a reader working in a German context needs to know, so the English keeps
the official word and adds the German phrase in quotation marks with the gloss "in good
faith". The quotation marks are also what keeps `tools/check_english.py` quiet on the
`und`, which seemed better than an ignore entry: the phrase really is a quotation from
the statute. **A lawyer should look at this**: whether "in good faith" is the right gloss
for *Treu und Glauben* in this particular context is genuinely arguable, and I have no
standing to settle it.

**3. The citation-form gloss (an addition inside a block).** The German cites as
`Art. 2 Abs. 1 DSGVO`. Per the brief, that form is kept with `GDPR` for `DSGVO` – but
`Abs.` and `lit.` are opaque to an English reader, and the whole reason for keeping the
German form is that the reader will have to look the article up. I therefore added one
parenthetical clause at the first citation, in the **Scope** bullet: "article citations
keep the German form the reader will need in order to look them up: *Abs.* is a
paragraph, *lit.* a point". This is content that is not in the German. It is inside an
existing block, so block alignment is untouched and no `sync/additions` entry applies,
but **a human should confirm the addition is wanted** – the alternative is to delete the
clause and leave the abbreviations unexplained, which costs nothing else.

**4. Currency and amounts.** German puts the symbol last and abbreviates
(`35,3 Mio. €`); this edition puts the euro sign first and writes the word out:
`€35.3 million`, `€1.2 billion`, `€900,000`, `€18,600`. Thousands separators flip from
`.` to `,` per TRANSLATION.md section 6, and `2 %` / `4 %` close up to `2%` / `4%`.
`1,2 Mrd. €` becomes `€1.2 billion` on the short scale, which is what "Mrd." means and
what English-language reporting of these fines uses. This is the first chapter in the
book to carry currency amounts, so the convention is new and worth a glossary row if a
later chapter needs one.

**5. Hedging left exactly where the German put it.** Three places where the German is
deliberately uncertain, and the English is no sharper:
* The EU-U.S. Data Privacy Framework is "legally contested from the outset", "as of
  September 2026 exactly that is in doubt again, and a fresh challenge has been
  announced". No prediction was added and none was removed.
* "A replacement ePrivacy Regulation has been under negotiation since 2017" – still the
  present perfect, still no date.
* "Anyone planning a US cloud today should therefore reckon with the basis for it falling
  away once more" is advice the German gives; it stays advice about a legal risk, not
  advice about what to do. Nothing anywhere in the chapter was turned into legal advice,
  and no sentence of my own was added about compliance.

**6. Dates and judgment references.** `15. Dezember 1983` → `15 December 1983`,
`26.7.2000` → `26 July 2000`, `6.10.2015` → `6 October 2015`, `16.7.2020` →
`16 July 2020`. The docket number `1 BvR 209/83 u. a.` becomes `1 BvR 209/83 and others`
– the number itself is how the judgment is cited and stays untouched. `95/46/EG` →
`95/46/EC` and `2002/58/EG` → `2002/58/EC`, because those are the official English
citations of the same instruments.

**7. The `[Entropie]` link.** Rendered as `[entropy](expectation-variance.md)`, which is
the English title of a section in that chapter (`## Entropy`), so the link text matches
something the reader actually arrives at. The sentence it sits in is about how many bits
one has collected about a person, so `expectation-variance.md`'s "information (also
self-information)" is the related notion – but the German says *Entropie* and so does the
English.

**8. Links that stay German.** Three of the six further resources point at German-language
material and are now marked "(in German)" per TRANSLATION.md section 3: the plain-words
GDPR site, the BayLDA checklist, and the bpb documentary. The documentary title
*Democracy – Im Rausch der Daten* stays German (it is a title), which is the single
`check-ignore` entry. The EUR-Lex full-text link had `/legal-content/DE/` in its path and
was switched to `/legal-content/EN/`, since the identical English text exists at that URL –
this is the "German link replaced by its English counterpart" rule, and it is the one URL
in the chapter whose target changed. **Worth a click by a human** to confirm the EN PDF
still resolves.

**9. Glosses added for institutions, not for law.** `Schufa`, `AOK`, `Bundesgerichtshof`,
`Bundesverfassungsgericht`, `EuGH` and `Bundesbeauftragte` mean nothing to a reader
outside Germany, so each gets a short apposition on first use ("Schufa, the German credit
agency"; "AOK Baden-Württemberg, a statutory health insurer"; "the Federal Court of
Justice (Bundesgerichtshof, 2018)"). The German names are kept in brackets so the reader
can search for them. `Knuddels`, `notebooksbilliger.de` and `Deichmann` are left
unglossed: the sentences say what they are.

**10. Genderstern.** Five instances (`Schüler\*innen`, `Mitarbeiter\*innen`,
`Gewinnspielteilnehmer\*innen`, `Kund\*innen`) become plain plurals – pupils, employees,
prize-draw entrants, customers – per TRANSLATION.md section 6.

**11. `Privacy by Design` / `by Default` capitalisation.** The German uses the English
loanwords capitalised, as names. The English keeps the capitals where the German bolds
them as defined terms (the section heading and the two bullet lead-ins) and drops to lower
case in running prose ("breaches privacy by default", "Art. 25 privacy by design"), which
is what English usage does. Mildly inconsistent on purpose; flagging it in case the style
pass prefers one or the other.

**12. `Lieblingsfarbe von Gummibärchen`.** "Your favourite colour of gummy bear is not a
personal datum." The singular *datum* is deliberate: `what-is-data-science.md` quotes Goos
defining a *datum* and noting that the plural is data, so the word is already established
in this edition and the callback is free.

## Proposals for `TERMINOLOGY.md`

Not edited, as instructed. The table above is the proposal. If only a handful are merged,
the ones that would most help a later chapter are `Dateisystem` → **filing system** (the
false friend), the Art. 5 principle names, the Chapter III right names, `Aufsichtsbehörde`
→ **supervisory authority**, `Geldbuße` → **administrative fine**, and the currency
convention from Decisions 4, which belongs in TRANSLATION.md section 6 rather than in the
glossary.

## Style pass

Second pass (Fable), deliberately the most conservative of the four. 22 of the 33 prose
blocks were touched, most of them in one or two phrases; `sync.py align`: 50 blocks aligned,
`check_english.py`: clean, the single `check-ignore` entry (block 49, the bpb film title)
still stands.

Not touched, by rule: every quotation from the GDPR's official English text (the Art. 5
principles in block 14, the Art. 6 bases and Art. 9 categories in blocks 18 and 21, the
Art. 58 powers in block 32, the "effective, proportionate and dissuasive" and Art. 83(2)
criteria in block 33, the Art. 4 definitions of personal data and pseudonymisation in
blocks 4 and 29); the fixed terms (controller, processor, data subject, filing system,
supervisory authority, rectification, erasure, restriction, objection, adequacy decision);
every German term and its gloss; every ETid link, date, amount and docket number; the table.

Kinds of change in the connective prose:

* **The census-judgment sentence** (block 9): the quotation now attaches to the noun it
  qualifies – "a social order 'in which citizens can no longer know …' would be incompatible
  with the right of self-determination" – instead of hanging off the end of the clause. The
  quoted words are unchanged.
* **"To these comes …" / "To these … adds"** (blocks 15, 30), a *hinzu kommt* calque, →
  "Art. 5 Abs. 2 adds accountability to these" / "Added to these is liability".
* **Nominalisations and prepositional stacks** → verbs: "a missing legal basis towards a
  company's own staff" → "for data on a company's own staff"; "without checking the consent
  cleanly in its systems" → "without a clean check of consent in its systems"; "the duty to
  inform people about the storing of information on their devices" → "to tell people when
  information is stored on their devices"; "being a directive it depended on being
  transposed" → "as a directive it had to be transposed".
* **"one" → "you"** (blocks 29, 46), "can try candidates through" (*durchprobieren*) →
  "can run through candidate codes", "lines of attack" (*Stoßrichtungen*) → "lines",
  "the measure" (*Maßstab*) → "the yardstick", "called to account" → "held to account",
  "The practical rule … runs:" → "The practical rule …:".
* "Two misunderstandings are thereby disposed of" → "That disposes of two
  misunderstandings"; "The default setting therefore decides the outcome in fact" → "So in
  practice the default setting decides the outcome"; "The nursery's telephone list" → "A
  nursery's telephone list" (generic, as the German *die Kita* is).
* "classify … as unlawful" (block 30, the Austrian DSB and Google Analytics) → "find …
  unlawful", which is what a supervisory authority does in English.

Noticed but not touched (meaning, not style – a human should look):

* **Privacy-by-design maxim 2** (block 23): "the later in a process a link to a person
  survives, the smaller the circle of people who get to see it" reads backwards at first
  sight. It is a faithful rendering of the German ("je später im Prozess ein Personenbezug
  besteht, desto kleiner ist der Kreis derer, die ihn sehen"); if the intended sense is
  "the further downstream, the fewer people, so anonymise early", the German might say so
  more plainly.
* **The parcel service as a processor** (blocks 12 and 19). Faithful to the German. In
  German practice a parcel carrier is commonly treated as an independent controller rather
  than a processor under Art. 28; whether the example is the one the author wants is a
  lawyer's question, flagged here only because the chapter promises that every case can be
  checked.
* Decision 3 above (the *Abs.*/*lit.* gloss in block 11) is a translator's addition that
  still awaits a human yes or no; I left the clause exactly as it was.
* The capitalisation of Privacy by Design/Default (Decision 11) was left as the translator
  set it: capitals as defined terms, lower case in running prose.
