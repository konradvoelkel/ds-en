---
title: "Data protection and the GDPR: a glossary"
short_title: "Data protection"
description: "The terms of data protection law that genuinely come up when working with data: personal data, the principles of Art. 5, legal bases, privacy by design."
---

In computer science, **handling personal data responsibly** is a central concern – legally as much as ethically. This chapter gives an overview of the most important terms and principles of data protection in the context of the European General Data Protection Regulation (GDPR; in German *Datenschutz-Grundverordnung*, DSGVO).

The chapter sits here because from the next chapter on we train models on real datasets, and before personal data serve as training material the terms that govern how such data may be handled ought to be clear. It is deliberately a glossary, with no mathematics and no code. Each term comes with examples and with real cases; the fine cases are all taken from the [GDPR Enforcement Tracker](https://www.enforcementtracker.com) kept by the law firm CMS and linked there by number, so that every one of them can be checked for date, amount and source.

## Personal data

**Personal data** are any information relating to an identified or identifiable natural person. A person counts as identifiable if they can be identified directly or indirectly – by a name, by location data or by an online identifier, for instance.

**Pseudonymised** and **encrypted** data enjoy the protection of the GDPR as well, and so do supposedly **anonymised** data, as soon as the link to a person can be restored with reasonable effort (recital 26).

Examples:
- Your favourite colour of gummy bear is not a personal datum. The same answer in a table beside a student number is one.
- A longitudinal survey in schools wants to link the answers of the same children across years without storing any names. A code built from the initial letters of the parents' names, or a hash of the name with a fixed prefix, is a **pseudonym**: anyone who knows the rule can work backwards, so the data remain personal. A number handed to the children is a number nobody brings back the following year, and a link with the number encoded in it destroys the very trust in anonymity that it was meant to protect.
- Whether data are anonymous is a question of information, not of names: anyone who has collected enough bits about a person (postcode, date of birth and sex are enough for most people) holds personal data, names or no names. That is the [entropy](expectation-variance.md) from the stochastics part of this book in legal dress.

## How the GDPR came about

The GDPR did not appear out of nowhere in 2018. Four stages explain why it looks the way it does:

- **The right to informational self-determination** (*informationelle Selbstbestimmung*): the Federal Constitutional Court (Bundesverfassungsgericht) derived it from the general right of personality in its census judgment (*Volkszählungsurteil*) of 15 December 1983 (1 BvR 209/83 and others). Its central sentence is still the best short account of what the protection is for: a social order "in which citizens can no longer know who knows what about them, when, and on what occasion" would be incompatible with the right of self-determination. The occasion was a planned census – which is to say, a data protection problem does not begin with computers but with bringing data together.
- **The Federal Data Protection Act** (*Bundesdatenschutzgesetz*, BDSG): first enacted in 1977, fundamentally recast in 1990 in order to implement the census judgment. It is still in force, but since 2018 only as a supplement to the GDPR, wherever the GDPR leaves the member states room of their own (employee data protection, for example).
- **Directive 95/46/EC** of 24 October 1995: the GDPR's immediate predecessor. It already contained the principles, the legal bases and the rights of the data subject, but as a directive it had to be transposed into national law – with correspondingly different results from one member state to the next. The GDPR repealed it and covered the same ground as a directly applicable regulation.
- **The ePrivacy Directive 2002/58/EC**: special rules for electronic communications, successor to Directive 97/66/EC and amended by 2009/136/EC. From it comes the duty to tell people when information is stored on their devices and to let them refuse – which is what every website today puts on screen as a *cookie banner*. A replacement ePrivacy Regulation has been under negotiation since 2017.

## The central terms

- **Scope** (Art. 2 Abs. 1 GDPR – article citations keep the German form the reader will need in order to look them up: *Abs.* is a paragraph, *lit.* a point): the Regulation applies to the processing of personal data wholly or partly by automated means, and to the non-automated processing of such data where they form part of a filing system or are intended to. A card index therefore falls under it; a single sheet of notes does not.
- **Processing**: any operation performed on personal data – from collection through storage and use to erasure.
- **Controller** (*Verantwortlicher*): the body that decides on the purposes and means of the processing.
- **Processor** (*Auftragsverarbeiter*): a third party that processes data on the controller's behalf – an external service provider, say. The processor is bound by the controller's instructions, and the relationship has to be set down in writing in a **data processing agreement** (*Auftragsverarbeitungsvertrag*, AVV) under Art. 28 GDPR: the subject matter and duration of the processing, its nature and purpose, the categories of data subject, and the obligations and rights of both sides.
- **Consent**: a freely given, informed and unambiguous agreement by the data subject to the processing. Freely given also means that there must be no relationship of dependence. A school in Skellefteå had pupils' attendance recorded by facial recognition, with their parents' consent; the Swedish supervisory authority held the consent ineffective because of the imbalance of power between a school and the families ([ETid-67](https://www.enforcementtracker.com/ETid-67), 2019, around €18,600). A nursery's telephone list, by contrast, is perfectly in order once the parents have consented.

An example of controller and processor: an online shop is the controller for its customer data; the parcel service that receives the delivery address and the cloud provider whose servers hold the database are processors. Both need a contract with the shop, and the shop remains the party under the obligation.

## The GDPR's basic principles (Art. 5)

1. **Lawfulness, fairness and transparency** (Art. 5 Abs. 1 lit. a) – "lawfully, fairly and in a transparent manner in relation to the data subject"; the German text says "nach Treu und Glauben", in good faith, where the English says "fairly"
2. **Purpose limitation** (lit. b) – use only for "specified, explicit and legitimate purposes"
3. **Data minimisation** (lit. c) – "adequate, relevant and limited to what is necessary"
4. **Accuracy** (lit. d) – "accurate and, where necessary, kept up to date"; inaccurate data are to be rectified or erased
5. **Storage limitation** (lit. e) – in identifiable form only for as long "as is necessary for the purposes …"
6. **Integrity and confidentiality** (lit. f) – protection "against unauthorised or unlawful processing and against accidental loss"

Art. 5 Abs. 2 adds **accountability** to these: the controller must not only ensure that the principles are complied with but also be able to demonstrate it. That is why data protection in practice means so much documentation.

Examples of the principles:
- *Purpose limitation:* asking for a surname in order to generate an AI portrait serves no purpose. Sending someone a discount code on their birthday does need the date of birth – but not as a mandatory field on every order.
- *Data minimisation:* a recommender algorithm needs purchase histories, not addresses; those belong in a separate system, in the extreme case on a machine with no network connection (*air gap*). Less data stored also means less data to leak when something goes wrong.
- *Accuracy:* an incorrect entry at Schufa, the German credit agency, has to be rectified on request; the right to that is Art. 16.
- *Integrity and confidentiality:* the chat platform Knuddels stored passwords in clear text, was hacked, and received a fine of €20,000 – kept deliberately low because the breach was reported and dealt with in exemplary fashion ([ETid-25](https://www.enforcementtracker.com/ETid-25), 2018). AOK Baden-Württemberg, a statutory health insurer, used the data of prize-draw entrants for advertising without a clean check of consent in its systems: €1.24 million ([ETid-306](https://www.enforcementtracker.com/ETid-306), 2020).

## Legal bases (Art. 6) and special categories (Art. 9)

- **Legal basis**: processing personal data is lawful only if at least one of the six conditions in Art. 6 Abs. 1 GDPR is met:
  1. consent of the data subject,
  2. performance of a contract with the data subject (or pre-contractual steps at their request),
  3. compliance with a legal obligation,
  4. protection of vital interests,
  5. performance of a task carried out in the public interest or in the exercise of official authority,
  6. legitimate interest (*berechtigtes Interesse*) of the controller or of a third party, unless the interests or fundamental rights of the data subject override it.

  Consent, then, is only *one* of six possible bases. An online shop needs no separate consent for the delivery address, because processing it is necessary to perform the contract – and so is passing it on to the parcel service. Keeping invoices for ten years is a legal obligation under tax law, and on that ground a request for erasure may be refused.

  The most expensive German cases arose from a missing legal basis for data on a company's own staff: at a service centre in Nuremberg, H&M kept and evaluated notes on employees' private circumstances and illnesses – €35.3 million ([ETid-405](https://www.enforcementtracker.com/ETid-405), 2020). notebooksbilliger.de kept its staff under permanent video surveillance; the supervisory authority imposed €10.4 million, which the court cut to €900,000 ([ETid-519](https://www.enforcementtracker.com/ETid-519), 2021). Individuals are held to account too: a police officer who took a witness's telephone number from a case file and used it for private messages paid €1,400 ([ETid-50](https://www.enforcementtracker.com/ETid-50), 2019).

- **Special categories of personal data** (Art. 9 GDPR, colloquially "sensitive data"): data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs or trade union membership, together with genetic data, biometric data for the purpose of uniquely identifying a person, data concerning health, and data concerning sex life or sexual orientation. Processing them is **prohibited in principle** (Art. 9 Abs. 1) – but not absolutely: Art. 9 Abs. 2 sets out an exhaustive list of exceptions, among them explicit consent, obligations arising from employment and social security law, data the data subject has manifestly made public themselves, health care, and scientific research under safeguards. Religious affiliation may therefore be processed if one of these exceptions applies; without such an exception, none of the six legal bases in Art. 6 is enough either.

## Privacy by Design and by Default

- **Privacy by Design** (Art. 25 Abs. 1): data protection has to be thought about when a system is conceived, not bolted on afterwards. Three maxims sum up what that means in practice:
  1. What is made technically impossible needs no supervision. A field that does not exist cannot be misused.
  2. Separate business processes functionally and anonymise as early as you can – the later in a process a link to a person survives, the smaller the circle of people who get to see it.
  3. Lay out the architecture for privacy, physically as much as electronically: separate systems, separate access rights, separate rooms.
- **Privacy by Default** (Art. 25 Abs. 2): the default settings must be the data-sparing ones. The reason is empirical rather than legal: people often fail, in everyday life, to act on the wish for privacy they profess – out of convenience, out of ignorance, or because in the particular case they weigh things differently. Clicking "accept all" on every cookie banner is not an expression of preference but the path of least resistance. So in practice the default setting decides the outcome.

Examples: defaults must not permit unnecessary collection of data. A cookie banner that arrives with every box already ticked breaches privacy by default. TikTok set children's accounts to public by default and was fined €345 million for it ([ETid-2032](https://www.enforcementtracker.com/ETid-2032), 2023).

## Data minimisation in practice

Data minimisation (Art. 5 Abs. 1 lit. c; in the old BDSG the same principle went by the name "Datensparsamkeit", data parsimony, § 3a BDSG a.F., in the version then in force) means in practice:
- Collect no irrelevant data
- Do without optional entries (age on an order, say, where it is not needed)
- Say that an entry is voluntary, and default it to "do not collect"

The practical rule for data science projects: for every field holding personal data, ask why you have to store it. If there is no answer, leave it out. If there is one, write it down – that is your legal basis. For everything else, obtain consent.


## Further terms and concepts

- **Pseudonymisation**: processing in such a way that the data can no longer be attributed to a person without additional information.
- **Self-generated code** (longitudinal studies): in repeated surveys you want to bring together the answers of the same person across several waves without being able to attribute them to that person. So the respondents build a code themselves out of stable personal attributes – the first and last letters of their parents' first names and the day of their own date of birth, say – and only its hash is stored. Because the same person reproduces the same code, the waves can be linked; because those collecting the data do not know the code, they cannot work backwards from it. The methods and their error rates are well studied {cite}`poege2011`. It remains a pseudonym all the same: anyone who knows the construction rule and enough about the respondents can run through candidate codes – so hashed data are not automatically anonymous.
- **Rights of the data subject**: Chapter III of the GDPR gives the data subject seven rights that the controller must satisfy on request – as a rule within one month and free of charge:
  - **Access** (Art. 15): which data are being processed, for what purpose, where they came from, who they go to, how long they are stored – along with a copy of the data. That covers video recordings too: Deichmann's Hungarian subsidiary refused a customer the footage from its shop and paid €54,800 ([ETid-430](https://www.enforcementtracker.com/ETid-430), 2020).
  - **Rectification** (Art. 16): correct inaccurate data, complete incomplete data.
  - **Erasure** (Art. 17), also the "right to be forgotten": when the purpose no longer exists, for instance, or consent has been withdrawn.
  - **Restriction of processing** (Art. 18): the middle way, while the accuracy of the data is being checked, say – the data stay stored but may not be used further.
  - **Notification obligation** (Art. 19): the controller must communicate any rectification, erasure or restriction to every recipient the data were disclosed to.
  - **Data portability** (Art. 20): receive your own data in a commonly used machine-readable format and take them with you to another provider.
  - **Objection** (Art. 21): against processing that rests on legitimate interest; against direct marketing at any time and with no balancing of interests at all.

  Added to these is **liability** (Art. 82): anyone who suffers material or non-material damage through an infringement has a claim to compensation. The controller escapes it only by proving that it is not in any way responsible for the damage.
- **Notification of data breaches** (Art. 33): breaches of the protection of personal data are to be reported to the supervisory authority within 72 hours. Twitter reported a breach late and incompletely: €450,000 ([ETid-485](https://www.enforcementtracker.com/ETid-485), 2020); Knuddels (above) reported at once and was treated more leniently for it.
- **Transfers of data to third countries**: permitted only where the level of data protection is adequate. The simplest route is an **adequacy decision** of the Commission under Art. 45: if it finds that a country offers an adequate level of protection, data may be transferred there as if within the EU. For the United States this has been a farce in several acts:
  - **Safe Harbor** (Commission decision of 26 July 2000) – declared invalid by the Court of Justice of the European Union in its judgment in *Schrems I* on 6 October 2015.
  - **EU-US Privacy Shield** (Implementing Decision (EU) 2016/1250) – declared invalid by the Court of Justice in its judgment in *Schrems II* on 16 July 2020, in both cases because US authorities can gain access to the data and data subjects in the EU have no effective remedy against that.
  - **EU-U.S. Data Privacy Framework** (Implementing Decision (EU) 2023/1795, in force since July 2023) – the third attempt, legally contested from the outset. It stands or falls with the independence of the US oversight bodies; as of September 2026 exactly that is in doubt again, and a fresh challenge has been announced. Anyone planning a US cloud today should therefore expect the basis for it to fall away once more. Meta transferred Facebook data to the United States regardless and received the highest GDPR fine so far, €1.2 billion ([ETid-1844](https://www.enforcementtracker.com/ETid-1844), 2023). [noyb](https://noyb.eu), the organisation Schrems founded, also got the Austrian supervisory authority to find the use of Google Analytics unlawful in 2022 – no fine, but consequences for almost every website. Anyone who puts data into a US cloud needs to know this history.

## Fines and enforcement

What the GDPR added to the directive of 1995 is less the principles than the sanctions. It is enforced by independent **supervisory authorities** (Art. 51 ff.) – in Germany one per federal state plus the Federal Commissioner. Their catalogue of **corrective powers** (Art. 58 Abs. 2) reaches well beyond money: warnings about intended processing, reprimands after an infringement, orders to comply with a data subject's requests, orders to rectify or erase, withdrawal of a certification, suspension of transfers to third countries – and, as the sharpest instrument, a temporary or definitive **limitation or ban** on processing. For a data-driven business model that is the real threat; a fine can be paid, a ban on processing cannot.

**Administrative fines** (Art. 83) are to be "effective, proportionate and dissuasive" and come in two tiers: up to €10 million or 2% of worldwide annual turnover in the preceding year for breaches of the controller's own obligations (Art. 25 privacy by design or Art. 33 notification, say), and up to €20 million or 4% for breaches of the principles, of the rights of data subjects or of the rules on transfers to third countries – whichever amount is the higher. What counts in fixing the amount includes the nature, gravity and duration of the infringement, whether it was intentional or negligent, the remedial measures taken, earlier infringements, and the degree of cooperation with the supervisory authority.

Alongside supervision there is self-regulation: **codes of conduct** (Art. 40) are sector-specific rulebooks that associations draw up and have approved by the supervisory authority. Keeping to one makes it easier to discharge the accountability obligation of Art. 5 Abs. 2.

That disposes of two misunderstandings: data protection is neither too complicated to engage with nor free of consequences if you ignore it. At the same time, the small fines do not cost a startup its life. Mercedes paid €3,000 in Spain for a lack of cooperation with the supervisory authority ([ETid-885](https://www.enforcementtracker.com/ETid-885), 2021); a corporation cares about that only because earlier infringements raise the next fine.

| Case | Year | Amount | What it was about | Tracker |
|---|---|---|---|---|
| Meta Platforms Ireland | 2023 | €1.2 billion | data transferred to the USA with no valid basis | [ETid-1844](https://www.enforcementtracker.com/ETid-1844) |
| TikTok | 2023 | €345 million | children's accounts public by default | [ETid-2032](https://www.enforcementtracker.com/ETid-2032) |
| H&M, Nuremberg | 2020 | €35.3 million | notes on employees' private lives and illnesses | [ETid-405](https://www.enforcementtracker.com/ETid-405) |
| AOK Baden-Württemberg | 2020 | €1.24 million | prize-draw data used for advertising without clean consent | [ETid-306](https://www.enforcementtracker.com/ETid-306) |
| notebooksbilliger.de | 2021 | €900,000 (after court) | permanent video surveillance of staff | [ETid-519](https://www.enforcementtracker.com/ETid-519) |
| Twitter | 2020 | €450,000 | data breach reported too late | [ETid-485](https://www.enforcementtracker.com/ETid-485) |
| Deichmann, Hungary | 2020 | €54,800 | access to video footage refused | [ETid-430](https://www.enforcementtracker.com/ETid-430) |
| Knuddels | 2018 | €20,000 | passwords in clear text, exemplary reporting | [ETid-25](https://www.enforcementtracker.com/ETid-25) |
| School in Skellefteå | 2019 | €18,600 | facial recognition with ineffective consent | [ETid-67](https://www.enforcementtracker.com/ETid-67) |
| Police officer, Baden-Württemberg | 2019 | €1,400 | a witness's telephone number used privately | [ETid-50](https://www.enforcementtracker.com/ETid-50) |
| Mercedes, Spain | 2021 | €3,000 | lack of cooperation with the supervisory authority | [ETid-885](https://www.enforcementtracker.com/ETid-885) |

Some everyday cases with no fine attached that are worth knowing: dashcam footage may be used in evidence, according to the Federal Court of Justice (Bundesgerichtshof, 2018), yet recording the traffic permanently remains unlawful. A circular email to all customers with the recipients visible instead of in BCC is a notifiable data breach. A phone call from "PayPal" asking for login details is not a data protection problem but fraud; data protection and IT security overlap, but they are not the same thing. The [Düsseldorf open data portal](https://opendata.duesseldorf.de) shows how to publish data without giving people away.

:::{admonition} Exercise: the Enforcement Tracker as a dataset
:class: tip
The Enforcement Tracker is itself a table with over 3,000 rows: country, authority, date, amount, company, sector, articles infringed, type of infringement, source. Load the table (the site offers an export; failing that, a small script that reads the data embedded in the page will do) and answer, with the tools from the chapter [Pandas](pandas.ipynb): which countries impose the most fines, and which the highest? How has the number of cases per year developed? Which type of infringement is the most frequent, and which the most expensive on average? And is the mean or the median the right measure of location for fine amounts?
:::

:::{admonition} Hint
:class: dropdown
The amounts are extremely skewed to the right (a few cases above €100 million, most of them below €50,000), so the median is the more informative measure of location, and a histogram needs a logarithmic axis. By count Spain leads by a wide margin; by total it is Ireland, because of the proceedings against the US corporations based there. The most frequent type of infringement is "Insufficient legal basis for data processing" – Art. 6, that is.
:::

## The EU's legal framework beyond the GDPR

The GDPR protects personal data. Since 2020 the EU has pursued a second, complementary aim with its **European data strategy** (Commission communication of 19 February 2020): data should be easier to share and use within Europe, under European rules. Out of that has come a series of regulations that apply side by side and are worth keeping apart – roughly along three lines: protection of the data subject (GDPR), rules for markets and platforms (DMA, DSA), access to and sharing of data (DGA, Data Act) – and, cutting across all of them, the AI Act as product regulation for AI systems.

- **AI Act** (*KI-Verordnung*, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)): the first comprehensive legal framework for AI systems, proposed in April 2021 and adopted in 2024. The approach is risk-based – prohibited practices (social scoring by public authorities, for instance), high-risk applications with extensive obligations (medicine, personnel selection, law enforcement), transparency obligations for the rest. Build a model into a product and you yourself become an addressee of this regulation.
- **Digital Markets Act (DMA)** ([Regulation (EU) 2022/1925](https://eur-lex.europa.eu/eli/reg/2022/1925/oj)): obligations for very large platforms designated as *gatekeepers* – interoperability of messengers, say, and a ban on favouring one's own services.
- **Digital Services Act (DSA)** ([Regulation (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)): responsibility for content, reporting channels, transparency of recommender systems and of advertising.
- **Data Governance Act (DGA)** ([Regulation (EU) 2022/868](https://eur-lex.europa.eu/eli/reg/2022/868/oj)): a framework for the re-use of protected public sector data, for data intermediation services, and for *data altruism* – voluntarily making your own data available for purposes in the general interest.
- **Data Act** ([Regulation (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)): access to the data that connected devices generate – whoever buys a machine should be able to get at its data too, and to switch supplier.

For everyday work with data the GDPR remains the yardstick; the other regulations decide which data are available at all, and on what conditions a model may be placed on the market.

## Further resources

- [The GDPR in plain words](https://eu-datenschutz-grundverordnung.net/eu-dsgvo/) (in German)
- [Full text of the GDPR (EUR-Lex)](http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679)
- [Checklist of technical and organisational measures (BayLDA)](https://www.lda.bayern.de/media/checkliste/baylda_checkliste_tom.pdf) (in German)
- [Film: *Democracy – Im Rausch der Daten* (bpb)](https://www.bpb.de/mediathek/254194/democracy-im-rausch-der-daten) (in German)
- [GDPR Enforcement Tracker](https://www.enforcementtracker.com) of the law firm CMS: every fine case named in this chapter, with its date, amount and source (CC BY-NC-SA 4.0)
- Alfred Spector, Peter Norvig, Chris Wiggins, Jeannette M. Wing: *Data Science in Context* {cite}`spector2022` – data science without formulas and without code, but very good on what goes on around the technology; ethics in it is not an appendix but a running theme.
