<!-- Example output, kept on purpose. This is a *replay*: the pinned commit
compared against an older ds-skript commit, to show what a real staleness
report looks like and to prove the tool works on actual history. -->

# Upstream changes c7247a99 → 0ea4466

## landing-page.md → landing-page.md

### delete – German block `28` – English block(s) **28**

Current English block 28:

```md
**Folien**
Die Folien zu jeder Sitzung stehen als PDF unter [Vorlesungsfolien](slides.md), jeweils mit dem Kapitel, zu dem sie gehören.
```

### replace – German block `30`, `31` – English block(s) **30**, **31**

German now reads:

```md
Dieses Vorlesungsskript steht unter der [Creative Commons Namensnennung Lizenz 4.0 (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). <a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png" height="20"/></a> Jeglicher Code außerdem unter der GPL3.
```

Current English block 30:

```md
Dieses Vorlesungsskript steht unter der [Creative Commons Lizenz Namensnennung – Weitergabe unter gleichen Bedingungen 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.de). <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.de"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a> Jeglicher Code außerdem unter der GPL3.
```

Current English block 31:

```md
Davon ausgenommen sind gekennzeichnete Fremdinhalte, die unter ihrer jeweils eigenen Lizenz stehen: die eingebundenen xkcd-Comics (CC BY-NC 2.5), das Venn-Diagramm von Drew Conway (CC BY-NC 3.0) und der Melbourne-Housing-Datensatz von Anthony Pino (CC BY-NC-SA 4.0). Bei jedem dieser Inhalte steht die Quelle an Ort und Stelle. Die [Vorlesungsfolien](slides.md) enthalten weitere Fremdbilder; sie sind in der README des Folienordners im Repositorium aufgeführt.
```


## was-ist-data-science.md → what-is-data-science.md

### delete – German block `1` – _dropped from this edition: link to the German HHU lecture recording_

### replace – German block `3` – English block(s) **2**

What changed in the German:

```diff
- Im Jahr 2010 veröffentlichten die Harvard-Ökonomen Carmen Reinhart und Kenneth Rogoff eine Auswertung von zwei Jahrhunderten Staatsschulden und Wirtschaftswachstum {cite}`reinhart2010`. Ihr Befund: Sobald die Schulden eines Landes 90 % seiner Wirtschaftsleistung übersteigen, schrumpft die Wirtschaft im [-Mittel-] um 0,1 % pro Jahr. Die Zahl machte Karriere. Sie stand im Haushaltsentwurf des US-Kongresses, der EU-Währungskommissar zitierte sie, und sie war ein Argument für die Sparpolitik in Europa nach der Finanzkrise.
+ Im Jahr 2010 veröffentlichten die Harvard-Ökonomen Carmen Reinhart und Kenneth Rogoff eine Auswertung von zwei Jahrhunderten Staatsschulden und Wirtschaftswachstum {cite}`reinhart2010`. Ihr Befund: Sobald die Schulden eines Landes 90 % seiner Wirtschaftsleistung übersteigen, schrumpft die Wirtschaft im {+Mittel,+} um 0,1 % pro Jahr. Die Zahl machte Karriere. Sie stand im Haushaltsentwurf des US-Kongresses, der EU-Währungskommissar zitierte sie, und sie war ein Argument für die Sparpolitik in Europa nach der Finanzkrise.
```

German now reads:

```md
Im Jahr 2010 veröffentlichten die Harvard-Ökonomen Carmen Reinhart und Kenneth Rogoff eine Auswertung von zwei Jahrhunderten Staatsschulden und Wirtschaftswachstum {cite}`reinhart2010`. Ihr Befund: Sobald die Schulden eines Landes 90 % seiner Wirtschaftsleistung übersteigen, schrumpft die Wirtschaft im Mittel, um 0,1 % pro Jahr. Die Zahl machte Karriere. Sie stand im Haushaltsentwurf des US-Kongresses, der EU-Währungskommissar zitierte sie, und sie war ein Argument für die Sparpolitik in Europa nach der Finanzkrise.
```

Current English block 2:

```md
In 2010 the Harvard economists Carmen Reinhart and Kenneth Rogoff published an analysis of two centuries of public debt and economic growth {cite}`reinhart2010`. Their finding: as soon as a country's debt exceeds 90% of its economic output, the economy shrinks by an average of 0.1% per year. The number went places. It appeared in the US Congress budget proposal, the EU monetary affairs commissioner quoted it, and it was an argument for austerity policy in Europe after the financial crisis.
```

### replace – German block `21` – English block(s) **20**

What changed in the German:

```diff
- Drei [-Dinge, die man dafür außerdem braucht,-] lernt man in keiner Vorlesung: Geduld, Übung und Fachkenntnisse über das Anwendungsgebiet. Ob ein Blutdruckwert von $400$ ein Messfehler ist oder ein Alter von $0$ ein fehlender Wert, steht in keinem Datenformat — das weiß nur, wer das Gebiet kennt oder jemanden fragt, der es kennt. Auch im maschinellen Lernen, etwa beim Deep Learning, kann man durch Pflegen der Trainingsdaten erheblich bessere Ergebnisse erzielen.
+ Drei {+Punkte dieser Liste+} lernt man {+allerdings+} in keiner Vorlesung: Geduld, Übung und Fachkenntnisse über das Anwendungsgebiet. Ob ein Blutdruckwert von $400$ ein Messfehler ist oder ein Alter von $0$ ein fehlender Wert, steht in keinem Datenformat — das weiß nur, wer das Gebiet kennt oder jemanden fragt, der es kennt. Auch im maschinellen Lernen, etwa beim Deep Learning, kann man durch Pflegen der Trainingsdaten erheblich bessere Ergebnisse erzielen.
```

German now reads:

```md
Drei Punkte dieser Liste lernt man allerdings in keiner Vorlesung: Geduld, Übung und Fachkenntnisse über das Anwendungsgebiet. Ob ein Blutdruckwert von $400$ ein Messfehler ist oder ein Alter von $0$ ein fehlender Wert, steht in keinem Datenformat — das weiß nur, wer das Gebiet kennt oder jemanden fragt, der es kennt.
Auch im maschinellen Lernen, etwa beim Deep Learning, kann man durch Pflegen der Trainingsdaten erheblich bessere Ergebnisse erzielen.
```

Current English block 20:

```md
Three further things you need for it are taught in no lecture: patience, practice, and domain knowledge about the field of application. Whether a blood pressure reading of $400$ is a measurement error, or an age of $0$ a missing value, is written in no data format – only someone who knows the field, or who asks someone who does, can tell.
In machine learning too, in deep learning for instance, considerably better results can be had by taking care of the training data.
```


## intro-stochastik.md → intro-probability.md

### delete – German block `1` – English block(s) **1**

Current English block 1:

```md
[Vorlesungsaufzeichnung Wahrscheinlichkeitsmaß (VL 2, erster Teil)](https://media.hhu.de/channel/video/data-science-vl-2-wahrscheinlichkeitsmass-zufallsvariable-pmf-2025/d5149a6bce20e827dc30685847505f16/167)
```

### replace – German block `11` – English block(s) **11**

What changed in the German:

```diff
- Statistische Modelle erweitern diese Alles-oder-nichts-Logik nun um verschiedene Grade von Plausibilität: wenn der Rasen nass ist, ist es [-plausibel,-] anzunehmen, dass es vor kurzem regnete. Es ist ebenso plausibel, anzunehmen, dass jemand den Rasen gewässert hat mit einem Gartenschlauch. Was wir plausibler finden, hängt davon ab, was wir sonst über die Realität wissen. Durch längere Beobachtung des Rasens können wir feststellen, welche Gründe wie oft zu einem nassen Rasen führen, und daran unser Modell schärfen.
+ Statistische Modelle erweitern diese Alles-oder-nichts-Logik nun um verschiedene Grade von Plausibilität: wenn der Rasen nass ist, ist es {+plausible,+} anzunehmen, dass es vor kurzem regnete. Es ist ebenso plausibel, anzunehmen, dass jemand den Rasen gewässert hat mit einem Gartenschlauch. Was wir plausibler finden, hängt davon ab, was wir sonst über die Realität wissen. Durch längere Beobachtung des Rasens können wir feststellen, welche Gründe wie oft zu einem nassen Rasen führen, und daran unser Modell schärfen.
```

German now reads:

```md
Statistische Modelle erweitern diese Alles-oder-nichts-Logik nun um verschiedene Grade von Plausibilität: wenn der Rasen nass ist, ist es plausible, anzunehmen, dass es vor kurzem regnete. Es ist ebenso plausibel, anzunehmen, dass jemand den Rasen gewässert hat mit einem Gartenschlauch. Was wir plausibler finden, hängt davon ab, was wir sonst über die Realität wissen. Durch längere Beobachtung des Rasens können wir feststellen, welche Gründe wie oft zu einem nassen Rasen führen, und daran unser Modell schärfen.
```

Current English block 11:

```md
Statistische Modelle erweitern diese Alles-oder-nichts-Logik nun um verschiedene Grade von Plausibilität: wenn der Rasen nass ist, ist es plausibel, anzunehmen, dass es vor kurzem regnete. Es ist ebenso plausibel, anzunehmen, dass jemand den Rasen gewässert hat mit einem Gartenschlauch. Was wir plausibler finden, hängt davon ab, was wir sonst über die Realität wissen. Durch längere Beobachtung des Rasens können wir feststellen, welche Gründe wie oft zu einem nassen Rasen führen, und daran unser Modell schärfen.
```

### replace – German block `27` – English block(s) **27**

What changed in the German:

```diff
- Wenn man diese Forderungen präzisiert, kann man das [Cox-Jaynes-Theorem](https://en.wikipedia.org/wiki/Cox%27s_theorem) beweisen, [-das-] besagt, dass es eine mathematische Abbildung $cj$ von den reellen Zahlen in das geschlossene Intervall $[0,1]$ gibt, die Plausibilitäten auf "Wahrscheinlichkeiten" abbildet, sodass (fast) alle Regeln der klassischen Wahrscheinlichkeitstheorie erfüllt sind. So erfüllt $P := cj \circ p \colon [-\mathcal{A}-] \to [0,1]$ die Regeln 1. $P(WAHR) = 1$ und $P(FALSCH) = 0$. 1. Wenn $A_1,\dots,A_n$ eine endliche Menge paarweise unvereinbarer (sich gegenseitig ausschließender) Aussagen sind, dann gilt endliche Additivität: $ [-P(A_1 \vee \dots \vee A_n)-] = \sum_{i=1}^n P(A_i) $
+ Wenn man diese Forderungen präzisiert, kann man das [Cox-Jaynes-Theorem](https://en.wikipedia.org/wiki/Cox%27s_theorem) beweisen, {+dass+} besagt, dass es eine mathematische Abbildung $cj$ von den reellen Zahlen in das geschlossene Intervall $[0,1]$ gibt, die Plausibilitäten auf "Wahrscheinlichkeiten" abbildet, sodass (fast) alle Regeln der klassischen Wahrscheinlichkeitstheorie erfüllt sind. So erfüllt $P := cj \circ p \colon {+X+} \to [0,1]$ die Regeln 1. $P(WAHR) = 1$ und $P(FALSCH) = 0$. 1. Wenn $A_1,\dots,A_n$ eine endliche Menge paarweise unvereinbarer (sich gegenseitig ausschließender) Aussagen sind, dann gilt endliche Additivität: $ {+P\left( \bigcup_{i=1} A_i \right)+} = \sum_{i=1}^n P(A_i) $
```

German now reads:

```md
Wenn man diese Forderungen präzisiert, kann man das [Cox-Jaynes-Theorem](https://en.wikipedia.org/wiki/Cox%27s_theorem) beweisen, dass besagt, dass es eine mathematische Abbildung $cj$ von den reellen Zahlen in das geschlossene Intervall $[0,1]$ gibt, die Plausibilitäten auf "Wahrscheinlichkeiten" abbildet, sodass (fast) alle Regeln der klassischen Wahrscheinlichkeitstheorie erfüllt sind. So erfüllt $P := cj \circ p \colon X \to [0,1]$ die Regeln
1. $P(WAHR) = 1$ und $P(FALSCH) = 0$.
1. Wenn $A_1,\dots,A_n$ eine endliche Menge paarweise unvereinbarer (sich gegenseitig ausschließender) Aussagen sind, dann gilt endliche Additivität:
$ P\left( \bigcup_{i=1} A_i \right) = \sum_{i=1}^n P(A_i) $
```

Current English block 27:

```md
Wenn man diese Forderungen präzisiert, kann man das [Cox-Jaynes-Theorem](https://en.wikipedia.org/wiki/Cox%27s_theorem) beweisen, das besagt, dass es eine mathematische Abbildung $cj$ von den reellen Zahlen in das geschlossene Intervall $[0,1]$ gibt, die Plausibilitäten auf "Wahrscheinlichkeiten" abbildet, sodass (fast) alle Regeln der klassischen Wahrscheinlichkeitstheorie erfüllt sind. So erfüllt $P := cj \circ p \colon \mathcal{A} \to [0,1]$ die Regeln
1. $P(WAHR) = 1$ und $P(FALSCH) = 0$.
1. Wenn $A_1,\dots,A_n$ eine endliche Menge paarweise unvereinbarer (sich gegenseitig ausschließender) Aussagen sind, dann gilt endliche Additivität:
$ P(A_1 \vee \dots \vee A_n) = \sum_{i=1}^n P(A_i) $
```

### replace – German block `44` – English block(s) **44**

What changed in the German:

```diff
- Man kann nun zeigen, dass die klassische $\epsilon$-$\delta$-Definition von Stetigkeit äquivalent ist zu: $f \colon X \to Y$ heißt *stetig* wenn die Urbilder offener Mengen $U \subseteq Y$ auch offene Mengen $f^{-1}(U) \subseteq [-X$-] sind.
+ Man kann nun zeigen, dass die klassische $\epsilon$-$\delta$-Definition von Stetigkeit äquivalent ist zu: $f \colon X \to Y$ heißt *stetig* wenn die Urbilder offener Mengen $U \subseteq Y$ auch offene Mengen $f^{-1}(U) \subseteq {+M$+} sind.
```

German now reads:

```md
Man kann nun zeigen, dass die klassische $\epsilon$-$\delta$-Definition von Stetigkeit äquivalent ist zu: $f \colon X \to Y$ heißt *stetig* wenn die Urbilder offener Mengen $U \subseteq Y$ auch offene Mengen $f^{-1}(U) \subseteq M$ sind.
```

Current English block 44:

```md
Man kann nun zeigen, dass die klassische $\epsilon$-$\delta$-Definition von Stetigkeit äquivalent ist zu: $f \colon X \to Y$ heißt *stetig* wenn die Urbilder offener Mengen $U \subseteq Y$ auch offene Mengen $f^{-1}(U) \subseteq X$ sind.
```

### replace – German block `70` – English block(s) **70**

What changed in the German:

```diff
- Bleiben wir beim nassen Rasen. Wir setzen $\Omega = \{R, G, T\}$ [-(die Buchstaben stehen jetzt für Ergebnisse, nicht mehr wie oben für Ereignisse)-] für die drei Erklärungen „es hat geregnet“, „jemand hat gegossen“, „es war Tau“, und als $\sigma$-Algebra nehmen wir die Potenzmenge $\mathcal{F} = \mathcal{P}(\Omega)$. Die einelementigen Ereignisse $\{R\}, \{G\}, \{T\}$ heißen **Elementarereignisse**; auf einer endlichen Menge legen ihre Wahrscheinlichkeiten bereits das ganze Maß fest, denn jedes andere Ereignis ist eine disjunkte Vereinigung von ihnen.
+ Bleiben wir beim nassen Rasen. Wir setzen $\Omega = \{R, G, T\}$ für die drei Erklärungen „es hat geregnet“, „jemand hat gegossen“, „es war Tau“, und als $\sigma$-Algebra nehmen wir die Potenzmenge $\mathcal{F} = \mathcal{P}(\Omega)$. Die einelementigen Ereignisse $\{R\}, \{G\}, \{T\}$ heißen **Elementarereignisse**; auf einer endlichen Menge legen ihre Wahrscheinlichkeiten bereits das ganze Maß fest, denn jedes andere Ereignis ist eine disjunkte Vereinigung von ihnen.
```

German now reads:

```md
Bleiben wir beim nassen Rasen. Wir setzen $\Omega = \{R, G, T\}$ für die drei Erklärungen „es hat geregnet“, „jemand hat gegossen“, „es war Tau“, und als $\sigma$-Algebra nehmen wir die Potenzmenge $\mathcal{F} = \mathcal{P}(\Omega)$. Die einelementigen Ereignisse $\{R\}, \{G\}, \{T\}$ heißen **Elementarereignisse**; auf einer endlichen Menge legen ihre Wahrscheinlichkeiten bereits das ganze Maß fest, denn jedes andere Ereignis ist eine disjunkte Vereinigung von ihnen.
```

Current English block 70:

```md
Bleiben wir beim nassen Rasen. Wir setzen $\Omega = \{R, G, T\}$ (die Buchstaben stehen jetzt für Ergebnisse, nicht mehr wie oben für Ereignisse) für die drei Erklärungen „es hat geregnet“, „jemand hat gegossen“, „es war Tau“, und als $\sigma$-Algebra nehmen wir die Potenzmenge $\mathcal{F} = \mathcal{P}(\Omega)$. Die einelementigen Ereignisse $\{R\}, \{G\}, \{T\}$ heißen **Elementarereignisse**; auf einer endlichen Menge legen ihre Wahrscheinlichkeiten bereits das ganze Maß fest, denn jedes andere Ereignis ist eine disjunkte Vereinigung von ihnen.
```

### replace – German block `80` – English block(s) **80**

What changed in the German:

```diff
- Auf einer endlichen Menge $\Omega$ von Kardinalität $N := |\Omega|$ (also Anzahl der Elemente $N$) ist mit $\mathcal{F} := \mathcal{P}(\Omega)$ und $P(A) := |A| / N$ ein Wahrscheinlichkeitsmaß definiert, [-das-] wir *Gleichverteilung* nennen.
+ Auf einer endlichen Menge $\Omega$ von Kardinalität $N := |\Omega|$ (also Anzahl der Elemente $N$) ist mit $\mathcal{F} := \mathcal{P}(\Omega)$ und $P(A) := |A| / N$ ein Wahrscheinlichkeitsmaß definiert, {+dass+} wir *Gleichverteilung* nennen.
```

German now reads:

```md
Auf einer endlichen Menge $\Omega$ von Kardinalität $N := |\Omega|$ (also Anzahl der Elemente $N$) ist mit $\mathcal{F} := \mathcal{P}(\Omega)$ und $P(A) := |A| / N$ ein Wahrscheinlichkeitsmaß definiert, dass wir *Gleichverteilung* nennen.
```

Current English block 80:

```md
Auf einer endlichen Menge $\Omega$ von Kardinalität $N := |\Omega|$ (also Anzahl der Elemente $N$) ist mit $\mathcal{F} := \mathcal{P}(\Omega)$ und $P(A) := |A| / N$ ein Wahrscheinlichkeitsmaß definiert, das wir *Gleichverteilung* nennen.
```

### replace – German block `93` – English block(s) **93**

What changed in the German:

```diff
- 1. $1 = P(\Omega) = P(\emptyset \cup \Omega) = P(\emptyset) + P(\Omega) = P(\emptyset) + 1$ 1. $P(A \cup B) = P(A \cup (B [-\setminus-] A)) = P(A) + P(B [-\setminus-] A)$ und $P(B [-\setminus-] A) + P(A \cap B) = P((B [-\setminus-] A) \cup (A \cap B)) = P(B)$ also $P(A \cup B) + P(A \cap B) = P(A) + P(B [-\setminus-] A) + P(A \cap B) = P(A) + P(B)$ 1. $A \subseteq B \implies B = A \cup (B [-\setminus-] A)$ $\phantom{A \subseteq B} \implies P(A) \leq P(A) + P(B [-\setminus-] A) = P(A \cup (B [-\setminus-] A)) = P(B)$ 1. den Leser\*innen als Übung überlassen.
+ 1. $1 = P(\Omega) = P(\emptyset \cup \Omega) = P(\emptyset) + P(\Omega) = P(\emptyset) + 1$ 1. $P(A \cup B) = P(A \cup (B {+-+} A)) = P(A) + P(B {+-+} A)$ und $P(B {+-+} A) + P(A \cap B) = P((B {+-+} A) \cup (A \cap B)) = P(B)$ also $P(A \cup B) + P(A \cap B) = P(A) + P(B {+-+} A) + P(A \cap B) = P(A) + P(B)$ 1. $A \subseteq B \implies B = A \cup (B {+-+} A)$ $\phantom{A \subseteq B} \implies P(A) \leq P(A) + P(B {+-+} A) = P(A \cup (B {+-+} A)) = P(B)$ 1. den Leser\*innen als Übung überlassen.
```

German now reads:

```md
1. $1 = P(\Omega) = P(\emptyset \cup \Omega) = P(\emptyset) + P(\Omega) = P(\emptyset) + 1$
1. $P(A \cup B) = P(A \cup (B - A)) = P(A) + P(B - A)$ und
   $P(B - A) + P(A \cap B) = P((B - A) \cup (A \cap B)) = P(B)$ also
   $P(A \cup B) + P(A \cap B) = P(A) + P(B - A) + P(A \cap B) = P(A) + P(B)$
1. $A \subseteq B \implies B = A \cup (B - A)$
   $\phantom{A \subseteq B} \implies P(A) \leq P(A) + P(B - A) = P(A \cup (B - A)) = P(B)$
1. den Leser\*innen als Übung überlassen.
```

Current English block 93:

```md
1. $1 = P(\Omega) = P(\emptyset \cup \Omega) = P(\emptyset) + P(\Omega) = P(\emptyset) + 1$
1. $P(A \cup B) = P(A \cup (B \setminus A)) = P(A) + P(B \setminus A)$ und
   $P(B \setminus A) + P(A \cap B) = P((B \setminus A) \cup (A \cap B)) = P(B)$ also
   $P(A \cup B) + P(A \cap B) = P(A) + P(B \setminus A) + P(A \cap B) = P(A) + P(B)$
1. $A \subseteq B \implies B = A \cup (B \setminus A)$
   $\phantom{A \subseteq B} \implies P(A) \leq P(A) + P(B \setminus A) = P(A \cup (B \setminus A)) = P(B)$
1. den Leser\*innen als Übung überlassen.
```


## intro-python.ipynb → intro-python.ipynb

### replace – German block `c0.1` – English block(s) **c0.1**

What changed in the German:

```diff
- [-[Vorlesungsaufzeichnung Python-] in [-der REPL](https://media.hhu.de/channel/video/data-science-python-in-der-repl/1383cd1ccc36f42479354b1c8c0dd373/167)-]
+ {+[Aufzeichnung zur Einführung+} in {+Python](https://media.hhu.de/channel/video/data-science-python-in-der-repl/1383cd1ccc36f42479354b1c8c0dd373/167)+}
```

German now reads:

```md
[Aufzeichnung zur Einführung in Python](https://media.hhu.de/channel/video/data-science-python-in-der-repl/1383cd1ccc36f42479354b1c8c0dd373/167)
```

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Python in der REPL](https://media.hhu.de/channel/video/data-science-python-in-der-repl/1383cd1ccc36f42479354b1c8c0dd373/167)
```

### replace – German block `c0.5` – English block(s) **c0.5**

What changed in the German:

```diff
- Mit Python lassen sich funktionale Programmierparadigmen verwenden wie in R oder Haskell, aber auch objektorientierte Paradigmen wie in C# oder Java. Anders als diese Sprachen ist Python [-*dynamisch* getypt: Der Typ hängt am Wert, nicht am Namen.-] So kann ein Variablenname einmal einen String zugewiesen bekommen, direkt danach einen Boolean und danach einen Integer. Wer striktere Typen bevorzugt, kann mittlerweile mit [-Type Annotations-] und speziellen Lintern [-(etwa `mypy`) arbeiten; der Interpreter selbst prüft sie nicht.-]
+ Mit Python lassen sich funktionale Programmierparadigmen verwenden wie in R oder Haskell, aber auch objektorientierte Paradigmen wie in C# oder Java. Anders als diese Sprachen ist Python {+zwar auch statisch getypt, aber dynamisch gebunden.+} So kann ein Variablenname einmal einen String zugewiesen bekommen, direkt danach einen Boolean und danach einen Integer. Wer striktere Typen bevorzugt, kann mittlerweile mit {+type annotations+} und speziellen Lintern {+arbeiten.+}
```

German now reads:

```md
Mit Python lassen sich funktionale Programmierparadigmen verwenden wie in R oder Haskell, aber auch objektorientierte Paradigmen wie in C# oder Java.
Anders als diese Sprachen ist Python zwar auch statisch getypt, aber dynamisch gebunden. So kann ein Variablenname einmal einen String zugewiesen bekommen, direkt danach einen Boolean und danach einen Integer. Wer striktere Typen bevorzugt, kann mittlerweile mit type annotations und speziellen Lintern arbeiten.
```

Current English block c0.5:

```md
Mit Python lassen sich funktionale Programmierparadigmen verwenden wie in R oder Haskell, aber auch objektorientierte Paradigmen wie in C# oder Java.
Anders als diese Sprachen ist Python *dynamisch* getypt: Der Typ hängt am Wert, nicht am Namen. So kann ein Variablenname einmal einen String zugewiesen bekommen, direkt danach einen Boolean und danach einen Integer. Wer striktere Typen bevorzugt, kann mittlerweile mit Type Annotations und speziellen Lintern (etwa `mypy`) arbeiten; der Interpreter selbst prüft sie nicht.
```

### replace – German block `c1.1` – English block(s) **c1.1**

What changed in the German:

```diff
- Die Wahl ist weder zufällig noch Geschmackssache. Python ist seit Jahren eine der meistgenutzten Programmiersprachen überhaupt — in den großen Entwicklerbefragungen taucht es regelmäßig hinter JavaScript und HTML/CSS auf, und im TIOBE-Index steht es seit [-Oktober 2021-] auf Platz eins. Wichtiger als die Popularität ist aber, was daraus entstanden ist.
+ Die Wahl ist weder zufällig noch Geschmackssache. Python ist seit Jahren eine der meistgenutzten Programmiersprachen überhaupt — in den großen Entwicklerbefragungen taucht es regelmäßig hinter JavaScript und HTML/CSS auf, und im TIOBE-Index steht es seit {+2025+} auf Platz eins. Wichtiger als die Popularität ist aber, was daraus entstanden ist.
```

German now reads:

```md
Die Wahl ist weder zufällig noch Geschmackssache. Python ist seit Jahren eine der meistgenutzten Programmiersprachen überhaupt — in den großen Entwicklerbefragungen taucht es regelmäßig hinter JavaScript und HTML/CSS auf, und im TIOBE-Index steht es seit 2025 auf Platz eins. Wichtiger als die Popularität ist aber, was daraus entstanden ist.
```

Current English block c1.1:

```md
Die Wahl ist weder zufällig noch Geschmackssache. Python ist seit Jahren eine der meistgenutzten Programmiersprachen überhaupt — in den großen Entwicklerbefragungen taucht es regelmäßig hinter JavaScript und HTML/CSS auf, und im TIOBE-Index steht es seit Oktober 2021 auf Platz eins. Wichtiger als die Popularität ist aber, was daraus entstanden ist.
```

### replace – German block `c1.5` – English block(s) **c1.5**

What changed in the German:

```diff
- Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: [-Der gezeigte Code kommt mit-] **Python [-3.11** aus und benutzt keine neueren Sprachfeatures; gebaut und getestet wird das Skript mit Python 3.13-] oder [-3.14, weil die Paketversionen in `pyproject.toml` das verlangen. `uv sync` installiert das passende Python selbst, wenn es fehlt.-]
+ Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: **Python {+3.11+} oder {+neuer**. Wer eine ältere Version hat, bekommt einen Teil der hier benutzten Syntax nicht zum Laufen.+}
```

German now reads:

```md
Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: **Python 3.11 oder neuer**. Wer eine ältere Version hat, bekommt einen Teil der hier benutzten Syntax nicht zum Laufen.
```

Current English block c1.5:

```md
Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: Der gezeigte Code kommt mit **Python 3.11** aus und benutzt keine neueren Sprachfeatures; gebaut und getestet wird das Skript mit Python 3.13 oder 3.14, weil die Paketversionen in `pyproject.toml` das verlangen. `uv sync` installiert das passende Python selbst, wenn es fehlt.
```

### replace – German block `c4.1` – English block(s) **c4.1**

What changed in the German:

```diff
- Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript [-wird mit Python 3.13 oder 3.14 gebaut und getestet; der gezeigte Code kommt-] mit Python 3.11 [-aus.-]
+ Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript {+wurde+} mit Python 3.11 {+(Debian 12) und Python 3.13 (Debian 13) getestet.+}
```

German now reads:

```md
Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript wurde mit Python 3.11 (Debian 12) und Python 3.13 (Debian 13) getestet.
```

Current English block c4.1:

```md
Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript wird mit Python 3.13 oder 3.14 gebaut und getestet; der gezeigte Code kommt mit Python 3.11 aus.
```

### replace – German block `c6` – English block(s) **c6**

What changed in the German:

```diff
- print("23 ist", type(23), "und 23.0 ist", type(23.0)) print("und 23+2j ist", type(23+2j)) print("Addieren wir int und floats gibt's", type(23+23.0)) print("Division von Ganzzahlen ergibt float, also ist 5/2 =", 5/2) print("Wenn wir das nicht wollen, können wir rechnen 5//2 =", 5//2) print("kein Overflow:", 2**100) print("IEEE 754:", 0.1 + 0.2 == 0.3, "denn 0.1+0.2 =", 0.1 + 0.2) print("Modulo [-hat das Vorzeichen des Divisors:",-] 7 % 3, -7 % 3, "und dazu passt", -7 // 3)
+ print("23 ist", type(23), "und 23.0 ist", type(23.0)) print("und 23+2j ist", type(23+2j)) print("Addieren wir int und floats gibt's", type(23+23.0)) print("Division von Ganzzahlen ergibt float, also ist 5/2 =", 5/2) print("Wenn wir das nicht wollen, können wir rechnen 5//2 =", 5//2) print("kein Overflow:", 2**100) print("IEEE 754:", 0.1 + 0.2 == 0.3, "denn 0.1+0.2 =", 0.1 + 0.2) print("Modulo {+ist nie negativ:",+} 7 % 3, -7 % 3, "und dazu passt", -7 // 3)
```

German now reads:

```md
print("23 ist", type(23), "und 23.0 ist", type(23.0))
print("und 23+2j ist", type(23+2j))
print("Addieren wir int und floats gibt's", type(23+23.0))
print("Division von Ganzzahlen ergibt float, also ist 5/2 =", 5/2)
print("Wenn wir das nicht wollen, können wir rechnen 5//2 =", 5//2)

print("kein Overflow:", 2**100)
print("IEEE 754:", 0.1 + 0.2 == 0.3, "denn 0.1+0.2 =", 0.1 + 0.2)
print("Modulo ist nie negativ:", 7 % 3, -7 % 3, "und dazu passt", -7 // 3)
```

Current English block c6:

```md
print("23 ist", type(23), "und 23.0 ist", type(23.0))
print("und 23+2j ist", type(23+2j))
print("Addieren wir int und floats gibt's", type(23+23.0))
print("Division von Ganzzahlen ergibt float, also ist 5/2 =", 5/2)
print("Wenn wir das nicht wollen, können wir rechnen 5//2 =", 5//2)

print("kein Overflow:", 2**100)
print("IEEE 754:", 0.1 + 0.2 == 0.3, "denn 0.1+0.2 =", 0.1 + 0.2)
print("Modulo hat das Vorzeichen des Divisors:", 7 % 3, -7 % 3, "und dazu passt", -7 // 3)
```

### insert – German block after `c12.0` – **new** – decide whether it belongs in this edition

German now reads:

```md
Unter der Haube ist ein Dictionary eine **Hash-Map**: Der Schlüssel wird zu einer Zahl verrechnet, und die zeigt auf den Platz, an dem der Wert liegt. Deshalb ist der Zugriff unabhängig von der Größe des Dictionaries schnell — und deshalb dürfen nur **unveränderliche** Objekte Schlüssel sein. Ein Schlüssel, der sich nachträglich ändert, läge am falschen Platz. Zahlen, Strings und Tupel gehen also, Listen und Dictionaries nicht.
```

### delete – German block `c14.0` – English block(s) **c14.0**

Current English block c14.0:

```md
Unter der Haube ist ein Dictionary eine **Hash-Map**: Der Schlüssel wird zu einer Zahl verrechnet, und die zeigt auf den Platz, an dem der Wert liegt. Deshalb ist der Zugriff unabhängig von der Größe des Dictionaries schnell — und deshalb dürfen nur **unveränderliche** Objekte Schlüssel sein. Ein Schlüssel, der sich nachträglich ändert, läge am falschen Platz. Zahlen, Strings und Tupel gehen also, Listen und Dictionaries nicht; genau das zeigen die letzten beiden Zeilen oben.
```

### replace – German block `c19.0` – English block(s) **c19.0**

What changed in the German:

```diff
- **Listen** sind geordnet und können verlängert werden. Unter der Haube [-ist-] eine [-Liste in CPython ein Array von Zeigern, das bei Bedarf durch ein größeres ersetzt wird.-] Als Anwender merkt man davon nichts und es ist für Performancefragen in der Regel irrelevant. Eine list comprehension ist eine Art, über eine Liste zu iterieren um eine weitere zu erstellen.
+ **Listen** sind geordnet und können verlängert werden. Unter der Haube {+verwendet Python je nach Länge und Implementierung des jeweiligen Interpreters oder Compilers dann einen Array mit fester Länge (der dann notfalls getauscht wird, wenn die Liste wächst) oder+} eine {+linked List oder so.+} Als Anwender merkt man davon nichts und es ist für Performancefragen in der Regel irrelevant. Eine list comprehension ist eine Art, über eine Liste zu iterieren um eine weitere zu erstellen.
```

German now reads:

```md
**Listen** sind geordnet und können verlängert werden. Unter der Haube verwendet Python je nach Länge und Implementierung des jeweiligen Interpreters oder Compilers dann einen Array mit fester Länge (der dann notfalls getauscht wird, wenn die Liste wächst) oder eine linked List oder so. Als Anwender merkt man davon nichts und es ist für Performancefragen in der Regel irrelevant. Eine list comprehension ist eine Art, über eine Liste zu iterieren um eine weitere zu erstellen.
```

Current English block c19.0:

```md
**Listen** sind geordnet und können verlängert werden. Unter der Haube ist eine Liste in CPython ein Array von Zeigern, das bei Bedarf durch ein größeres ersetzt wird. Als Anwender merkt man davon nichts und es ist für Performancefragen in der Regel irrelevant. Eine list comprehension ist eine Art, über eine Liste zu iterieren um eine weitere zu erstellen.
```

### replace – German block `c23.0` – English block(s) **c23.0**

What changed in the German:

```diff
- **Generatoren** sind Objekte, die Listen in einer Hinsicht verallgemeinern: man kann sich das nächste Element geben lassen. Es muss aber keine ganze Liste im Speicher gehalten werden (und auch nicht im voraus berechnet werden), daher sind Generator-Ausdrücke an vielen Stellen die richtige Wahl für Datenverarbeitungs-Pipelines innerhalb Python. [-Über-] jede [-Liste,-] jedes Tupel und [-jedes `range`-Objekt kann man genauso iterieren; `range` ist dabei kein Generator, sondern eine „faule“ Sequenz,-] die [-ihre Elemente ebenfalls erst bei Bedarf erzeugt.-]
+ **Generatoren** sind Objekte, die Listen in einer Hinsicht verallgemeinern: man kann sich das nächste Element geben lassen. Es muss aber keine ganze Liste im Speicher gehalten werden (und auch nicht im voraus berechnet werden), daher sind Generator-Ausdrücke an vielen Stellen die richtige Wahl für Datenverarbeitungs-Pipelines innerhalb Python. {+Man kann+} jede {+Liste und+} jedes Tupel {+als Generator verwenden+} und {+auch+} die {+range-Objekte sind Generatoren.+}
```

German now reads:

```md
**Generatoren** sind Objekte, die Listen in einer Hinsicht verallgemeinern: man kann sich das nächste Element geben lassen. Es muss aber keine ganze Liste im Speicher gehalten werden (und auch nicht im voraus berechnet werden), daher sind Generator-Ausdrücke an vielen Stellen die richtige Wahl für Datenverarbeitungs-Pipelines innerhalb Python.
Man kann jede Liste und jedes Tupel als Generator verwenden und auch die range-Objekte sind Generatoren.
```

Current English block c23.0:

```md
**Generatoren** sind Objekte, die Listen in einer Hinsicht verallgemeinern: man kann sich das nächste Element geben lassen. Es muss aber keine ganze Liste im Speicher gehalten werden (und auch nicht im voraus berechnet werden), daher sind Generator-Ausdrücke an vielen Stellen die richtige Wahl für Datenverarbeitungs-Pipelines innerhalb Python.
Über jede Liste, jedes Tupel und jedes `range`-Objekt kann man genauso iterieren; `range` ist dabei kein Generator, sondern eine „faule“ Sequenz, die ihre Elemente ebenfalls erst bei Bedarf erzeugt.
```

### replace – German block `c31.1` – English block(s) **c31.1**

What changed in the German:

```diff
- Schleifen und Verzweigungen sehen in Python so [-aus wie unten;-] eine Bedingung braucht keine [-Klammern.-]
+ Schleifen und Verzweigungen sehen in Python so {+aus. Blöcke werden durch Einrückung gebildet, nicht durch Klammern, und+} eine Bedingung braucht keine {+Klammern:+}
```

German now reads:

```md
Schleifen und Verzweigungen sehen in Python so aus. Blöcke werden durch Einrückung gebildet, nicht durch Klammern, und eine Bedingung braucht keine Klammern:
```

Current English block c31.1:

```md
Schleifen und Verzweigungen sehen in Python so aus wie unten; eine Bedingung braucht keine Klammern.
```

### replace – German block `c31.3` – English block(s) **c31.3**

What changed in the German:

```diff
- Die `for`-Schleife ist immer ein *for-each*: Sie läuft über die Elemente einer Sequenz, nie über einen Zähler. Wer einen Zähler braucht, erzeugt sich mit `range(n)` eine Sequenz von Zahlen und iteriert darüber — das ist der Grund, warum `range` in Python so allgegenwärtig ist. Über ein Dictionary iteriert man mit `.items()`, dann bekommt man Schlüssel und Wert [-zugleich:-]
+ Die `for`-Schleife ist immer ein *for-each*: Sie läuft über die Elemente einer Sequenz, nie über einen Zähler. Wer einen Zähler braucht, erzeugt sich mit `range(n)` eine Sequenz von Zahlen und iteriert darüber — das ist der Grund, warum `range` in Python so allgegenwärtig ist. Über ein Dictionary iteriert man mit `.items()`, dann bekommt man Schlüssel und Wert {+zugleich.+}
```

German now reads:

```md
Die `for`-Schleife ist immer ein *for-each*: Sie läuft über die Elemente einer Sequenz, nie über einen Zähler. Wer einen Zähler braucht, erzeugt sich mit `range(n)` eine Sequenz von Zahlen und iteriert darüber — das ist der Grund, warum `range` in Python so allgegenwärtig ist. Über ein Dictionary iteriert man mit `.items()`, dann bekommt man Schlüssel und Wert zugleich.
```

Current English block c31.3:

```md
Die `for`-Schleife ist immer ein *for-each*: Sie läuft über die Elemente einer Sequenz, nie über einen Zähler. Wer einen Zähler braucht, erzeugt sich mit `range(n)` eine Sequenz von Zahlen und iteriert darüber — das ist der Grund, warum `range` in Python so allgegenwärtig ist. Über ein Dictionary iteriert man mit `.items()`, dann bekommt man Schlüssel und Wert zugleich:
```

### replace – German block `c56.1` – English block(s) **c56.1**

What changed in the German:

```diff
- [-Randall-] Munroe, [-[xkcd 353 „Python“](https://xkcd.com/353/) (CC BY-NC 2.5)-]
+ {+[Link zum Comic (Randall+} Munroe, {+CC-BY-NC 2.5)](https://xkcd.com/353)+}
```

German now reads:

```md
[Link zum Comic (Randall Munroe, CC-BY-NC 2.5)](https://xkcd.com/353)
```

Current English block c56.1:

```md
Randall Munroe, [xkcd 353 „Python“](https://xkcd.com/353/) (CC BY-NC 2.5)
```


## stochastik-programmieren.ipynb → programming-probability.ipynb

### replace – German block `c1.1` – English block(s) **c1.1**

What changed in the German:

```diff
- Verwendete Python-Konstrukte: [Module/import](https://docs.python.org/3/tutorial/modules.html), [Methoden/def](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [Länge/len](https://docs.python.org/3/library/functions.html#len), [Mengen/set](https://docs.python.org/3/tutorial/datastructures.html#sets), [Generator-Ausdruck](https://docs.python.org/3/tutorial/classes.html#generator-expressions), [Range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function), [-[Assertion/assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement), [Zählen/Counter](https://docs.python.org/3/library/collections.html#collections.Counter)-]
+ Verwendete Python-Konstrukte: [Module/import](https://docs.python.org/3/tutorial/modules.html), [Methoden/def](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [Länge/len](https://docs.python.org/3/library/functions.html#len), [Mengen/set](https://docs.python.org/3/tutorial/datastructures.html#sets), [Generator-Ausdruck](https://docs.python.org/3/tutorial/classes.html#generator-expressions), [Range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function), {+[Assertion/assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)+}
```

German now reads:

```md
Verwendete Python-Konstrukte: [Module/import](https://docs.python.org/3/tutorial/modules.html), [Methoden/def](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [Länge/len](https://docs.python.org/3/library/functions.html#len), [Mengen/set](https://docs.python.org/3/tutorial/datastructures.html#sets), [Generator-Ausdruck](https://docs.python.org/3/tutorial/classes.html#generator-expressions), [Range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function), [Assertion/assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
```

Current English block c1.1:

```md
Verwendete Python-Konstrukte: [Module/import](https://docs.python.org/3/tutorial/modules.html), [Methoden/def](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), [Länge/len](https://docs.python.org/3/library/functions.html#len), [Mengen/set](https://docs.python.org/3/tutorial/datastructures.html#sets), [Generator-Ausdruck](https://docs.python.org/3/tutorial/classes.html#generator-expressions), [Range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function), [Assertion/assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement), [Zählen/Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
```

### replace – German block `c7.1` – English block(s) **c7.1**

What changed in the German:

```diff
- [-Randall-] Munroe, [-[xkcd 221 „Random Number“](https://xkcd.com/221/) (CC BY-NC 2.5)-]
+ {+[Link zum Comic (Randall+} Munroe, {+CC-BY-NC 2.5)](https://xkcd.com/221)+}
```

German now reads:

```md
[Link zum Comic (Randall Munroe, CC-BY-NC 2.5)](https://xkcd.com/221)
```

Current English block c7.1:

```md
Randall Munroe, [xkcd 221 „Random Number“](https://xkcd.com/221/) (CC BY-NC 2.5)
```

### delete – German block `c9.0`, `c10` – English block(s) **c9.0**, **c10**

Current English block c9.0:

```md
Zählen wir, wie oft jede Augenzahl gefallen ist. Die *relative Häufigkeit* ist die Anzahl geteilt durch $N$:
```

Current English block c10:

```md
from collections import Counter

häufigkeiten = Counter(würfe)
for augenzahl in range(1, 7):
    print(augenzahl, "fiel", häufigkeiten[augenzahl], "mal, relative Häufigkeit", häufigkeiten[augenzahl] / N)
```


## zufallsvariablen-verteilungen.md → random-variables-distributions.md

### replace – German block `74` – English block(s) **74**

What changed in the German:

```diff
- Wir können auch die ganze Nachricht als eine einzige Zufallsvariable auffassen: XYZ. Dabei kann es nun passieren, dass gewisse Buchstabenfolgen wahrscheinlicher sind, als ihre Bestandteile. Wenn $X=s$ und $Y=o$ sind, dann ist $Z=s$ sicher wahrscheinlicher, als wenn wir beliebige Werte für $X$ und $Y$ haben. Insgesamt ist $XYZ=sos$ wahrscheinlicher als das Produkt der [-Wahrscheinlichkeiten von-] $X=s$, [-$Y=o$ und-] $Z=s$. Wenn wir, wie üblich, die pmf von $XYZ$ mit $p(x,y,z)$ notieren, so heißt das:
+ Wir können auch die ganze Nachricht als eine einzige Zufallsvariable auffassen: XYZ. Dabei kann es nun passieren, dass gewisse Buchstabenfolgen wahrscheinlicher sind, als ihre Bestandteile. Wenn $X=s$ und $Y=o$ sind, dann ist $Z=s$ sicher wahrscheinlicher, als wenn wir beliebige Werte für $X$ und $Y$ haben. Insgesamt ist $XYZ=sos$ wahrscheinlicher als das Produkt der {+Ereignisse+} $X=s$, {+$Y=o$,+} $Z=s$. Wenn wir, wie üblich, die pmf von $XYZ$ mit $p(x,y,z)$ notieren, so heißt das:
```

German now reads:

```md
Wir können auch die ganze Nachricht als eine einzige Zufallsvariable auffassen: XYZ.
Dabei kann es nun passieren, dass gewisse Buchstabenfolgen wahrscheinlicher sind, als ihre Bestandteile.
Wenn $X=s$ und $Y=o$ sind, dann ist $Z=s$ sicher wahrscheinlicher, als wenn wir beliebige Werte für $X$ und $Y$ haben.
Insgesamt ist $XYZ=sos$ wahrscheinlicher als das Produkt der Ereignisse $X=s$, $Y=o$, $Z=s$.
Wenn wir, wie üblich, die pmf von $XYZ$ mit $p(x,y,z)$ notieren, so heißt das:
```

Current English block 74:

```md
Wir können auch die ganze Nachricht als eine einzige Zufallsvariable auffassen: XYZ.
Dabei kann es nun passieren, dass gewisse Buchstabenfolgen wahrscheinlicher sind, als ihre Bestandteile.
Wenn $X=s$ und $Y=o$ sind, dann ist $Z=s$ sicher wahrscheinlicher, als wenn wir beliebige Werte für $X$ und $Y$ haben.
Insgesamt ist $XYZ=sos$ wahrscheinlicher als das Produkt der Wahrscheinlichkeiten von $X=s$, $Y=o$ und $Z=s$.
Wenn wir, wie üblich, die pmf von $XYZ$ mit $p(x,y,z)$ notieren, so heißt das:
```

### replace – German block `78` – English block(s) **78**

What changed in the German:

```diff
- ### [-Induzierte pmf-]
+ ### {+Induziertes Wahrscheinlichkeitsmaß+}
```

German now reads:

```md
### Induziertes Wahrscheinlichkeitsmaß
```

Current English block 78:

```md
### Induzierte pmf
```

### delete – German block `96` – English block(s) **96**

Current English block 96:

```md
Eine so durch $p \in \Delta_n$ gegebene Verteilung heißt auch *kategoriale Verteilung*; wir treffen sie im Kapitel [Wichtigste diskrete Verteilungen](important-discrete-distributions.ipynb) wieder, wo wir auch ihren Erwartungswert und ihre Varianz ausrechnen. Ihr einfachster Fall hat einen eigenen Namen.
```

### insert – German block after `103` – **new** – decide whether it belongs in this edition

German now reads:

```md
Eine so gegebene Verteilung heißt auch *kategoriale Verteilung*; wir treffen sie im Kapitel
[Wichtigste diskrete Verteilungen](wichtigste-diskrete-verteilungen.ipynb) wieder, wo wir auch
ihren Erwartungswert und ihre Varianz ausrechnen.
```

### replace – German block `131` – English block(s) **131**

What changed in the German:

```diff
- Wenn wir die Stichprobe betrachten, können wir $e := [-\sum_{i=1}^N-] x_i$, die Anzahl der Erfolge, berechnen. Dann ist $N-e$ die Anzahl der Misserfolge und $\hat{\pi} := \frac{e}{N}$ eine Schätzung für die Erfolgswahrscheinlichkeit $\pi$, wenn wir davon ausgehen, dass immer die selbe Münze geworfen wurde.
+ Wenn wir die Stichprobe betrachten, können wir $e := {+\sum_{i=1}^n+} x_i$, die Anzahl der Erfolge, berechnen. Dann ist $N-e$ die Anzahl der Misserfolge und $\hat{\pi} := \frac{e}{N}$ eine Schätzung für die Erfolgswahrscheinlichkeit $\pi$, wenn wir davon ausgehen, dass immer die selbe Münze geworfen wurde.
```

German now reads:

```md
Wenn wir die Stichprobe betrachten, können wir $e := \sum_{i=1}^n x_i$, die Anzahl der Erfolge, berechnen.
Dann ist $N-e$ die Anzahl der Misserfolge und $\hat{\pi} := \frac{e}{N}$ eine Schätzung für die Erfolgswahrscheinlichkeit $\pi$,
wenn wir davon ausgehen, dass immer die selbe Münze geworfen wurde.
```

Current English block 131:

```md
Wenn wir die Stichprobe betrachten, können wir $e := \sum_{i=1}^N x_i$, die Anzahl der Erfolge, berechnen.
Dann ist $N-e$ die Anzahl der Misserfolge und $\hat{\pi} := \frac{e}{N}$ eine Schätzung für die Erfolgswahrscheinlichkeit $\pi$,
wenn wir davon ausgehen, dass immer die selbe Münze geworfen wurde.
```

### replace – German block `140` – English block(s) **140**

What changed in the German:

```diff
- Ziehen Sie $1000$ synthetische Farbwerte zur Modellverteilung $p = \left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)$ und bestimmen Sie die Verteilung der so erzeugten Daten. Wie weit weicht sie von $p$ ab, und wie ändert sich das bei nur $10$ gezogenen Werten? In der Standardbibliothek zieht `random.choices(werte, weights=..., k=1000)`, in Numpy `rng.choice(werte, size=1000, p=...)` [-(`random.choices` im Kapitel-] [Stochastik [-programmieren](stochastik-programmieren.ipynb), `rng.choice` im Kapitel [Numpy](numpy.ipynb), Abschnitt *Wahrscheinlichkeitsvektoren*).-]
+ Ziehen Sie $1000$ synthetische Farbwerte zur Modellverteilung $p = \left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)$ und bestimmen Sie die Verteilung der so erzeugten Daten. Wie weit weicht sie von $p$ ab, und wie ändert sich das bei nur $10$ gezogenen Werten? In der Standardbibliothek zieht `random.choices(werte, weights=..., k=1000)`, in Numpy `rng.choice(werte, size=1000, p=...)` {+(siehe+} [Stochastik {+programmieren](stochastik-programmieren.ipynb)).+}
```

German now reads:

```md
Ziehen Sie $1000$ synthetische Farbwerte zur Modellverteilung $p = \left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)$ und bestimmen Sie die Verteilung der so erzeugten Daten. Wie weit weicht sie von $p$ ab, und wie ändert sich das bei nur $10$ gezogenen Werten? In der Standardbibliothek zieht `random.choices(werte, weights=..., k=1000)`, in Numpy `rng.choice(werte, size=1000, p=...)` (siehe [Stochastik programmieren](stochastik-programmieren.ipynb)).
```

Current English block 140:

```md
Ziehen Sie $1000$ synthetische Farbwerte zur Modellverteilung $p = \left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)$ und bestimmen Sie die Verteilung der so erzeugten Daten. Wie weit weicht sie von $p$ ab, und wie ändert sich das bei nur $10$ gezogenen Werten? In der Standardbibliothek zieht `random.choices(werte, weights=..., k=1000)`, in Numpy `rng.choice(werte, size=1000, p=...)` (`random.choices` im Kapitel [Stochastik programmieren](programming-probability.ipynb), `rng.choice` im Kapitel [Numpy](numpy.ipynb), Abschnitt *Wahrscheinlichkeitsvektoren*).
```

### replace – German block `143` – English block(s) **143**

German now reads:

```md
Damit ist der Weg abgesteckt, den der Rest des Kurses geht, und der sich auch in {numref}`ds-prozess-modell` wiederfindet: einen Ausschnitt der Welt wählen, Daten erheben, sie putzen ([Daten putzen](data-cleaning.ipynb)) und in brauchbare Merkmale übersetzen — man sagt **Features** —, daraus Modelle bilden und die Modelle an den Daten messen. Alles Weitere ist die Ausarbeitung dieser fünf Schritte.
Nun werden wir Daten selten in Form von Bitfolgen mit völlig unabhängigen Bits interpretieren.
Zum Beispiel die menschliche Körpergröße, gemessen in Zentimetern, ist eine reelle Zahl größer $0$.
Gegeben eine Meßreihe, also eine Stichprobe der Größe $N$ von Körpergrößen, können wir ein statistisches Modell bilden.
Dabei reden wir hier nicht über Kausalität oder Korrelationen mit anderen Daten, wie z.B. Geschlecht oder Alter.
Trotzdem können wir Modelle bilden, die uns eine gewisse Vorhersage erlauben.
Ein Ansatz ist die zusammenfassende Statistik, die aus der Stichprobe eine einzelne Zahl extrahiert, die uns die Daten verlustbehaftet komprimieren lässt.
Welche Zahl die richtige ist, um Daten zusammenzufassen / zu modellieren, hängt von unserem Ziel ab.
Daher wollen wir uns im Folgenden mit Erwartungswert und Varianz aus einer datenzentrierten Perspektive befassen.
```

Current English block 143:

```md
Damit ist der Weg abgesteckt, den der Rest des Kurses geht, und der sich auch in {numref}`ds-prozess-modell` wiederfindet: einen Ausschnitt der Welt wählen, Daten erheben, sie putzen ([Daten putzen](data-cleaning.ipynb)) und in brauchbare Merkmale übersetzen — man sagt **Features** —, daraus Modelle bilden und die Modelle an den Daten messen. Alles Weitere ist die Ausarbeitung dieser fünf Schritte. Das nächste Kapitel beginnt mit dem letzten dieser Schritte: dem Vergleich von Daten und Modell in einer einzigen Zahl.
```


## erwartungswert.md → expectation-variance.md

### replace – German block `4` – English block(s) **4**

What changed in the German:

```diff
- Gegeben zwei Vektoren [-$v,w-] \in \mathbb{R}^n$ (wir stellen uns vor: [-$v$-] sind unsere Daten, [-$w$-] das, was wir erwarten), ist die mittlere Abweichung interessant: [-$\sum_{i=1}^n \frac{v_i-] - [-w_i}{n}$.-] Ein Problem dieser Größe ist, dass sich positive mit negativen Abweichungen herauskürzen.
+ Gegeben zwei Vektoren {+$x,y+} \in \mathbb{R}^n$ (wir stellen uns vor: {+$x$+} sind unsere Daten, {+$y$+} das, was wir erwarten), ist die mittlere Abweichung interessant: {+$\sum \frac{x_i+} - {+y_i}{n}$.+} Ein Problem dieser Größe ist, dass sich positive mit negativen Abweichungen herauskürzen.
```

German now reads:

```md
Gegeben zwei Vektoren $x,y \in \mathbb{R}^n$ (wir stellen uns vor: $x$ sind unsere Daten, $y$ das, was wir erwarten),
ist die mittlere Abweichung interessant: $\sum \frac{x_i - y_i}{n}$.
Ein Problem dieser Größe ist, dass sich positive mit negativen Abweichungen herauskürzen.
```

Current English block 4:

```md
Gegeben zwei Vektoren $v,w \in \mathbb{R}^n$ (wir stellen uns vor: $v$ sind unsere Daten, $w$ das, was wir erwarten),
ist die mittlere Abweichung interessant: $\sum_{i=1}^n \frac{v_i - w_i}{n}$.
Ein Problem dieser Größe ist, dass sich positive mit negativen Abweichungen herauskürzen.
```

### replace – German block `29` – English block(s) **29**

What changed in the German:

```diff
- $\texttt{median}(v) := \arg\min_{c \in \mathbb{R}} \texttt{mae}(v,c)$ ist [-„der“-] *Median* von $v$.
+ $\texttt{median}(v) := \arg\min_{c \in \mathbb{R}} \texttt{mae}(v,c)$ ist {+\`\`der''+} *Median* von $v$.
```

German now reads:

```md
$\texttt{median}(v) := \arg\min_{c \in \mathbb{R}} \texttt{mae}(v,c)$ ist \`\`der'' *Median* von $v$.
```

Current English block 29:

```md
$\texttt{median}(v) := \arg\min_{c \in \mathbb{R}} \texttt{mae}(v,c)$ ist „der“ *Median* von $v$.
```

### replace – German block `50` – English block(s) **50**

What changed in the German:

```diff
- Der $\texttt{mse}$ hat gegenüber dem $\texttt{mae}$ die Einheit zum Quadrat — bei Körpergrößen in Zentimetern also Quadratzentimeter, was sich schlecht interpretieren lässt. Deshalb zieht man am Ende meist die Wurzel; [-für-] das [-konstante Modell $w = \texttt{mean}(v)$-] ist [-das-] die Sample-Standardabweichung im nächsten Unterabschnitt.
+ Der $\texttt{mse}$ hat gegenüber dem $\texttt{mae}$ die Einheit zum Quadrat — bei Körpergrößen in Zentimetern also Quadratzentimeter, was sich schlecht interpretieren lässt. Deshalb zieht man am Ende meist die Wurzel; das ist die Sample-Standardabweichung im nächsten Unterabschnitt.
```

German now reads:

```md
Der $\texttt{mse}$ hat gegenüber dem $\texttt{mae}$ die Einheit zum Quadrat — bei Körpergrößen in Zentimetern also Quadratzentimeter, was sich schlecht interpretieren lässt. Deshalb zieht man am Ende meist die Wurzel; das ist die Sample-Standardabweichung im nächsten Unterabschnitt.
```

Current English block 50:

```md
Der $\texttt{mse}$ hat gegenüber dem $\texttt{mae}$ die Einheit zum Quadrat — bei Körpergrößen in Zentimetern also Quadratzentimeter, was sich schlecht interpretieren lässt. Deshalb zieht man am Ende meist die Wurzel; für das konstante Modell $w = \texttt{mean}(v)$ ist das die Sample-Standardabweichung im nächsten Unterabschnitt.
```

### insert – German block after `128` – **new** – decide whether it belongs in this edition

German now reads:

```md
:::{admonition} Beispiel
Der Erwartungswert einer Gleichverteilung auf $\Omega = \{1,\dots,n\}$ ist $\sum_{i=1}^n \frac{i}{n}$, also $\frac{n(n+1)}{2n} = \frac{n+1}{2}$.
:::
```

### replace – German block `146` – English block(s) **146**

What changed in the German:

```diff
- Wenn die $X_i$ nun unabhängig und identisch verteilt sind [-(kurz *iid*: jedes $X_i$ hat dieselbe Verteilung wie ein-] festes [-$X$, wir schreiben $X_i \sim X$)-] mit existierendem Erwartungswert $\mathbb{E}(X)$, dann genügen die $X_i$ einem starken Gesetz der großen Zahlen, d.h. dann konvergiert $\overline{X_n^\ast} = \overline{X_n} - \mathbb{E}X$, die Abweichung des arithmetischen Mittels einer Stichprobe von $X$ der Größe $n$ vom Erwartungswert, $P$-fast sicher gegen $0$. Das bedeutet umgekehrt auch: Die Wahrscheinlichkeit, dass das Stichprobenmittel für beliebig große $n$ vom Erwartungswert abweicht, ist $0$.
+ Wenn die $X_i$ nun unabhängig und identisch verteilt sind {+($X_i = X$ für+} festes {+$X$)+} mit existierendem Erwartungswert $\mathbb{E}(X)$, dann genügen die $X_i$ einem starken Gesetz der großen Zahlen, d.h. dann konvergiert $\overline{X_n^\ast} = \overline{X_n} - \mathbb{E}X$, die Abweichung des arithmetischen Mittels einer Stichprobe von $X$ der Größe $n$ vom Erwartungswert, $P$-fast sicher gegen $0$. Das bedeutet umgekehrt auch: Die Wahrscheinlichkeit, dass das Stichprobenmittel für beliebig große $n$ vom Erwartungswert abweicht, ist $0$.
```

German now reads:

```md
Wenn die $X_i$ nun unabhängig und identisch verteilt sind ($X_i = X$ für festes $X$) mit existierendem Erwartungswert $\mathbb{E}(X)$,
dann genügen die $X_i$ einem starken Gesetz der großen Zahlen, d.h.
dann konvergiert $\overline{X_n^\ast} = \overline{X_n} - \mathbb{E}X$, die Abweichung des arithmetischen Mittels einer Stichprobe von $X$ der Größe $n$ vom Erwartungswert, $P$-fast sicher gegen $0$.
Das bedeutet umgekehrt auch: Die Wahrscheinlichkeit, dass das Stichprobenmittel für beliebig große $n$ vom Erwartungswert abweicht, ist $0$.
```

Current English block 146:

```md
Wenn die $X_i$ nun unabhängig und identisch verteilt sind (kurz *iid*: jedes $X_i$ hat dieselbe Verteilung wie ein festes $X$, wir schreiben $X_i \sim X$) mit existierendem Erwartungswert $\mathbb{E}(X)$,
dann genügen die $X_i$ einem starken Gesetz der großen Zahlen, d.h.
dann konvergiert $\overline{X_n^\ast} = \overline{X_n} - \mathbb{E}X$, die Abweichung des arithmetischen Mittels einer Stichprobe von $X$ der Größe $n$ vom Erwartungswert, $P$-fast sicher gegen $0$.
Das bedeutet umgekehrt auch: Die Wahrscheinlichkeit, dass das Stichprobenmittel für beliebig große $n$ vom Erwartungswert abweicht, ist $0$.
```

### replace – German block `148` – English block(s) **148**

What changed in the German:

```diff
- Aus der $P$-fast sicheren Konvergenz folgt auch die stochastische Konvergenz: $\lim_{n\to\infty} [-P\left(|\overline{X_n^\ast}| \geq \epsilon \right) = \lim_{n\to\infty} P\left(|\overline{X_n} - \mathbb{E}X|-] \geq \epsilon \right) = 0$ für jedes $\epsilon > 0$.
+ Aus der $P$-fast sicheren Konvergenz folgt auch die stochastische Konvergenz: $\lim_{n\to\infty} {+P\left(|\overline{X_n}|+} \geq \epsilon \right) = 0$ für jedes $\epsilon > 0$.
```

German now reads:

```md
Aus der $P$-fast sicheren Konvergenz folgt auch die stochastische Konvergenz:
$\lim_{n\to\infty} P\left(|\overline{X_n}| \geq \epsilon \right) = 0$ für jedes $\epsilon > 0$.
```

Current English block 148:

```md
Aus der $P$-fast sicheren Konvergenz folgt auch die stochastische Konvergenz:
$\lim_{n\to\infty} P\left(|\overline{X_n^\ast}| \geq \epsilon \right) = \lim_{n\to\infty} P\left(|\overline{X_n} - \mathbb{E}X| \geq \epsilon \right) = 0$ für jedes $\epsilon > 0$.
```

### replace – German block `153` – English block(s) **153**

What changed in the German:

```diff
- [-1. Linearität:-] Der Erwartungswert ist linear in $X$, also für $\alpha,\beta \in \mathbb{R}$ und $X,Y \colon \Omega \to \mathbb{R}$ Zufallsvariable ist
+ {+0 .+} Der Erwartungswert ist linear in $X$, also für $\alpha,\beta \in \mathbb{R}$ und $X,Y \colon \Omega \to \mathbb{R}$ Zufallsvariable ist
```

German now reads:

```md
0 . Der Erwartungswert ist linear in $X$, also für $\alpha,\beta \in \mathbb{R}$ und $X,Y \colon \Omega \to \mathbb{R}$ Zufallsvariable ist
```

Current English block 153:

```md
1. Linearität: Der Erwartungswert ist linear in $X$, also für $\alpha,\beta \in \mathbb{R}$ und $X,Y \colon \Omega \to \mathbb{R}$ Zufallsvariable ist
```

### replace – German block `155`, `156`, `157` – English block(s) **155**, **156**, **157**

What changed in the German:

```diff
- [-2. Monotonie:-] Der Erwartungswert ist monoton in $X$, also für $X \leq Y$ ist $\mathbb{E}X \leq \mathbb{E}Y$.
+ {+1.+} Der Erwartungswert ist monoton in $X$, also für $X \leq Y$ ist $\mathbb{E}X \leq \mathbb{E}Y$.
- [-3.-] $\sigma$-Additivität: für eine Folge $X_i \geq 0$ ist $\mathbb{E}(\sum_{i \geq 1} X_i) = \sum_{i \geq 1} \mathbb{E}(X_i)$.
+ {+2.+} $\sigma$-Additivität: für eine Folge $X_i \geq 0$ ist $\mathbb{E}(\sum_{i \geq 1} X_i) = \sum_{i \geq 1} \mathbb{E}(X_i)$.
- [-4.-] Produktregel: Sind $X$ und $Y$ unabhängig, so ist $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$.
+ {+3.+} Produktregel: Sind $X$ und $Y$ unabhängig, so ist $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$.
```

German now reads:

```md
1. Der Erwartungswert ist monoton in $X$, also für $X \leq Y$ ist $\mathbb{E}X \leq \mathbb{E}Y$.
2. $\sigma$-Additivität: für eine Folge $X_i \geq 0$ ist $\mathbb{E}(\sum_{i \geq 1} X_i) = \sum_{i \geq 1} \mathbb{E}(X_i)$.
3. Produktregel: Sind $X$ und $Y$ unabhängig, so ist $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$.
```

Current English block 155:

```md
2. Monotonie: Der Erwartungswert ist monoton in $X$, also für $X \leq Y$ ist $\mathbb{E}X \leq \mathbb{E}Y$.
```

Current English block 156:

```md
3. $\sigma$-Additivität: für eine Folge $X_i \geq 0$ ist $\mathbb{E}(\sum_{i \geq 1} X_i) = \sum_{i \geq 1} \mathbb{E}(X_i)$.
```

Current English block 157:

```md
4. Produktregel: Sind $X$ und $Y$ unabhängig, so ist $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$.
```

### replace – German block `176` – English block(s) **176**

What changed in the German:

```diff
- Man nennt allgemein auch $\mathbb{E}(X^n)$ das $n$-te *Moment* und $\mathbb{E}((X - \mathbb{E}X)^n)$ das $n$-te *zentrale Moment*. Der Erwartungswert ist also das erste Moment und die Varianz das zweite zentrale Moment. Das dritte zentrale [-Moment, geteilt durch $\sigma^3$,-] heißt *Schiefe* [-(skewness),-] das [-vierte, geteilt durch $\sigma^4$,-] *Wölbung* [-(kurtosis); durch das Teilen werden beide einheitenlos und skalenunabhängig.-] Die Schiefe ist ein Maß dafür, wie symmetrisch die Verteilung um den Erwartungswert ist. Man nennt $\sigma(X) := \sqrt{\mathbb{V}(X)}$ die *Standardabweichung* von X.
+ Man nennt allgemein auch $\mathbb{E}(X^n)$ das $n$-te *Moment* und $\mathbb{E}((X - \mathbb{E}X)^n)$ das $n$-te *zentrale Moment*. Der Erwartungswert ist also das erste Moment und die Varianz das zweite zentrale Moment. Das dritte zentrale {+Moment+} heißt {+auch+} *Schiefe* {+(skewness) und+} das {+vierte+} *Wölbung* {+(kurtosis).+} Die Schiefe ist ein Maß dafür, wie symmetrisch die Verteilung um den Erwartungswert ist. Man nennt $\sigma(X) := \sqrt{\mathbb{V}(X)}$ die *Standardabweichung* von X.
```

German now reads:

```md
Man nennt allgemein auch $\mathbb{E}(X^n)$ das $n$-te *Moment* und $\mathbb{E}((X - \mathbb{E}X)^n)$ das $n$-te *zentrale Moment*.
Der Erwartungswert ist also das erste Moment und die Varianz das zweite zentrale Moment.
Das dritte zentrale Moment heißt auch *Schiefe* (skewness) und das vierte *Wölbung* (kurtosis).
Die Schiefe ist ein Maß dafür, wie symmetrisch die Verteilung um den Erwartungswert ist.
Man nennt $\sigma(X) := \sqrt{\mathbb{V}(X)}$ die *Standardabweichung* von X.
```

Current English block 176:

```md
Man nennt allgemein auch $\mathbb{E}(X^n)$ das $n$-te *Moment* und $\mathbb{E}((X - \mathbb{E}X)^n)$ das $n$-te *zentrale Moment*.
Der Erwartungswert ist also das erste Moment und die Varianz das zweite zentrale Moment.
Das dritte zentrale Moment, geteilt durch $\sigma^3$, heißt *Schiefe* (skewness), das vierte, geteilt durch $\sigma^4$, *Wölbung* (kurtosis); durch das Teilen werden beide einheitenlos und skalenunabhängig.
Die Schiefe ist ein Maß dafür, wie symmetrisch die Verteilung um den Erwartungswert ist.
Man nennt $\sigma(X) := \sqrt{\mathbb{V}(X)}$ die *Standardabweichung* von X.
```

### replace – German block `202` – English block(s) **202**

What changed in the German:

```diff
- Daran sehen wir: Abweichungen von $2\sigma$ haben eine Wahrscheinlichkeit $\leq \frac{1}{4}$, und Abweichungen von $3\sigma$ bereits nur noch $\leq \frac{1}{9}$. Wenn wir also Abweichungen in Vielfachen von $\sigma$ messen, so ist die Wahrscheinlichkeit für so große Abweichungen näherungsweise umgekehrt quadratisch proportional (so steht's ja oben schon in der Ungleichung). Damit haben wir auch ein Kriterium zur Hand, um in Daten fehlerhafte Datenpunkte auszusortieren - wenn [-Abweichungen-] größer $k\sigma$ mit $k > 1$ häufiger als erwartet zu sehen sind, dann gehören diese Datenpunkte zumindest nicht zu der Verteilung, die man erwartet.
+ Daran sehen wir: Abweichungen von $2\sigma$ haben eine Wahrscheinlichkeit $\leq \frac{1}{4}$, und Abweichungen von $3\sigma$ bereits nur noch $\leq \frac{1}{9}$. Wenn wir also Abweichungen in Vielfachen von $\sigma$ messen, so ist die Wahrscheinlichkeit für so große Abweichungen näherungsweise umgekehrt quadratisch proportional (so steht's ja oben schon in der Ungleichung). Damit haben wir auch ein Kriterium zur Hand, um in Daten fehlerhafte Datenpunkte auszusortieren - wenn {+Abweichung+} größer $k\sigma$ mit $k > 1$ häufiger als erwartet zu sehen sind, dann gehören diese Datenpunkte zumindest nicht zu der Verteilung, die man erwartet.
```

German now reads:

```md
Daran sehen wir: Abweichungen von $2\sigma$ haben eine Wahrscheinlichkeit $\leq \frac{1}{4}$, und Abweichungen von $3\sigma$ bereits nur noch $\leq \frac{1}{9}$. Wenn wir also Abweichungen in Vielfachen von $\sigma$ messen, so ist die Wahrscheinlichkeit für so große Abweichungen näherungsweise umgekehrt quadratisch proportional (so steht's ja oben schon in der Ungleichung). Damit haben wir auch ein Kriterium zur Hand, um in Daten fehlerhafte Datenpunkte auszusortieren - wenn Abweichung größer $k\sigma$ mit $k > 1$ häufiger als erwartet zu sehen sind, dann gehören diese Datenpunkte zumindest nicht zu der Verteilung, die man erwartet.
```

Current English block 202:

```md
Daran sehen wir: Abweichungen von $2\sigma$ haben eine Wahrscheinlichkeit $\leq \frac{1}{4}$, und Abweichungen von $3\sigma$ bereits nur noch $\leq \frac{1}{9}$. Wenn wir also Abweichungen in Vielfachen von $\sigma$ messen, so ist die Wahrscheinlichkeit für so große Abweichungen näherungsweise umgekehrt quadratisch proportional (so steht's ja oben schon in der Ungleichung). Damit haben wir auch ein Kriterium zur Hand, um in Daten fehlerhafte Datenpunkte auszusortieren - wenn Abweichungen größer $k\sigma$ mit $k > 1$ häufiger als erwartet zu sehen sind, dann gehören diese Datenpunkte zumindest nicht zu der Verteilung, die man erwartet.
```

### replace – German block `219` – English block(s) **219**

What changed in the German:

```diff
- Wendet man das Gesetz der großen Zahlen auf die Zufallsvariable ${\left(X-\mathbb{E}(X)\right)}^2$ an, so sieht man, dass auch die [-Sample-Standardabweichung-] gegen die [-Standardabweichung-] konvergiert. Damit ist also die Sample-Standardabweichung ein guter Ersatz, wenn sich die wahre Varianz der Zufallsvariable nicht bestimmen lässt.
+ Wendet man das Gesetz der großen Zahlen auf die Zufallsvariable ${\left(X-\mathbb{E}(X)\right)}^2$ an, so sieht man, dass auch die {+Standardabweichung+} gegen die {+Sample-Standardabweichung+} konvergiert. Damit ist also die Sample-Standardabweichung ein guter Ersatz, wenn sich die wahre Varianz der Zufallsvariable nicht bestimmen lässt.
```

German now reads:

```md
Wendet man das Gesetz der großen Zahlen auf die Zufallsvariable ${\left(X-\mathbb{E}(X)\right)}^2$ an, so sieht man, dass auch die Standardabweichung gegen die Sample-Standardabweichung konvergiert. Damit ist also die Sample-Standardabweichung ein guter Ersatz, wenn sich die wahre Varianz der Zufallsvariable nicht bestimmen lässt.
```

Current English block 219:

```md
Wendet man das Gesetz der großen Zahlen auf die Zufallsvariable ${\left(X-\mathbb{E}(X)\right)}^2$ an, so sieht man, dass auch die Sample-Standardabweichung gegen die Standardabweichung konvergiert. Damit ist also die Sample-Standardabweichung ein guter Ersatz, wenn sich die wahre Varianz der Zufallsvariable nicht bestimmen lässt.
```

### replace – German block `257` – English block(s) **257**

What changed in the German:

```diff
- $$ \begin{aligned} H(X) := \mathbb{E}\left( I(X) \right) &= \sum_{\omega' \in \Omega'} [--\log_b\big(P_X(\{X(\omega')\})\big)\, P_{\Omega'}(\{\omega'\})-] \\ &= - \sum_{\omega \in \Omega} \log_b(P(\{\omega\}))P(\{\omega\}). \end{aligned} $$
+ $$ \begin{aligned} H(X) := \mathbb{E}\left( I(X) \right) &= \sum_{\omega' \in \Omega'} {+-\log_b(P(\{X(\omega')\})P(X(\omega'))+} \\ &= - \sum_{\omega \in \Omega} \log_b(P(\{\omega\}))P(\{\omega\}). \end{aligned} $$
```

German now reads:

```md
$$
\begin{aligned}
H(X) := \mathbb{E}\left( I(X) \right) &= \sum_{\omega' \in \Omega'} -\log_b(P(\{X(\omega')\})P(X(\omega')) \\
                                      &= - \sum_{\omega \in \Omega} \log_b(P(\{\omega\}))P(\{\omega\}).
\end{aligned}
$$
```

Current English block 257:

```md
$$
\begin{aligned}
H(X) := \mathbb{E}\left( I(X) \right) &= \sum_{\omega' \in \Omega'} -\log_b\big(P_X(\{X(\omega')\})\big)\, P_{\Omega'}(\{\omega'\}) \\
                                      &= - \sum_{\omega \in \Omega} \log_b(P(\{\omega\}))P(\{\omega\}).
\end{aligned}
$$
```

### replace – German block `265` – English block(s) **265**

What changed in the German:

```diff
- Bei einer Gleichverteilung auf $\Omega = \{1,\dots,n\}$ ist für $x\in\Omega$ stets $P(\{x\}) = \frac{1}{n}$, also $I(x) = -\log_2(P(\{x\})) = -\log_2\frac{1}{n} = \log_2(n)$ und somit $H(X) = \sum_{i=1}^n \frac{\log_2(n)}{n} = \log_2(n)$. Diese Zahl verrät uns, dass wir im Mittel $\log_2(n)$ [-bit-] brauchen, um [-ein einzelnes Ergebnis von $X$ mitzuteilen, wenn Sender und Empfänger die Verteilung kennen;-] ein Sample der Größe [-$N$ kostet dann $N \log_2(n)$ bit.-] Es gibt andere Verteilungen, [-bei denen-] im Mittel weniger Information [-je Ergebnis genügt.-] Genau genommen sogar jede, denn die Gleichverteilung hat maximale Entropie unter allen diskreten Verteilungen. Sie korrespondiert dazu, dass wir maximal wenig wissen und daher alle Ergebnisse als gleich wahrscheinlich annehmen.
+ Bei einer Gleichverteilung auf $\Omega = \{1,\dots,n\}$ ist für $x\in\Omega$ stets $P(\{x\}) = \frac{1}{n}$, also $I(x) = -\log_2(P(\{x\})) = -\log_2\frac{1}{n} = \log_2(n)$ und somit $H(X) = \sum_{i=1}^n \frac{\log_2(n)}{n} = \log_2(n)$. Diese Zahl verrät uns, dass wir im Mittel $\log_2(n)$ {+bits an Information+} brauchen, um ein Sample der Größe {+$n$ zu rekonstruieren, wenn wir die Verteilung von $X$ kennen.+} Es gibt andere Verteilungen, {+die es erlauben mit+} im Mittel weniger Information {+ein Sample zu rekonstruieren.+} Genau genommen sogar jede, denn die Gleichverteilung hat maximale Entropie unter allen diskreten Verteilungen. Sie korrespondiert dazu, dass wir maximal wenig wissen und daher alle Ergebnisse als gleich wahrscheinlich annehmen.
```

German now reads:

```md
Bei einer Gleichverteilung auf $\Omega = \{1,\dots,n\}$ ist für $x\in\Omega$ stets $P(\{x\}) = \frac{1}{n}$,
also $I(x) = -\log_2(P(\{x\})) = -\log_2\frac{1}{n} = \log_2(n)$ und somit
$H(X) = \sum_{i=1}^n \frac{\log_2(n)}{n} = \log_2(n)$.
Diese Zahl verrät uns, dass wir im Mittel $\log_2(n)$ bits an Information brauchen, um ein Sample der Größe $n$ zu rekonstruieren, wenn wir die Verteilung von $X$ kennen. Es gibt andere Verteilungen, die es erlauben mit im Mittel weniger Information ein Sample zu rekonstruieren. Genau genommen sogar jede, denn die Gleichverteilung hat maximale Entropie unter allen diskreten Verteilungen. Sie korrespondiert dazu, dass wir maximal wenig wissen und daher alle Ergebnisse als gleich wahrscheinlich annehmen.
```

Current English block 265:

```md
Bei einer Gleichverteilung auf $\Omega = \{1,\dots,n\}$ ist für $x\in\Omega$ stets $P(\{x\}) = \frac{1}{n}$,
also $I(x) = -\log_2(P(\{x\})) = -\log_2\frac{1}{n} = \log_2(n)$ und somit
$H(X) = \sum_{i=1}^n \frac{\log_2(n)}{n} = \log_2(n)$.
Diese Zahl verrät uns, dass wir im Mittel $\log_2(n)$ bit brauchen, um ein einzelnes Ergebnis von $X$ mitzuteilen, wenn Sender und Empfänger die Verteilung kennen; ein Sample der Größe $N$ kostet dann $N \log_2(n)$ bit. Es gibt andere Verteilungen, bei denen im Mittel weniger Information je Ergebnis genügt. Genau genommen sogar jede, denn die Gleichverteilung hat maximale Entropie unter allen diskreten Verteilungen. Sie korrespondiert dazu, dass wir maximal wenig wissen und daher alle Ergebnisse als gleich wahrscheinlich annehmen.
```

### replace – German block `277` – English block(s) **277**

What changed in the German:

```diff
- Am besten versteht man die Entropie als eine relative Größe, und das werden wir später noch tun. Im weiteren Verlauf des Kurses begegnet sie uns an [-zwei-] Stellen: beim Aufstellen statistischer Modelle — das Maximum-Entropie-Prinzip im Kapitel [Normalverteilung](normalverteilung.ipynb) und das eng verwandte Maximum-Likelihood-Prinzip im Kapitel [Statistische Modelle und Schätzer](statistische-modelle.md) — und bei der Bewertung der Modellgüte, wo Kreuzentropie und relative Entropie im Kapitel [Relative Entropie](relative-entropie.md) die Werkzeuge sind.
+ Am besten versteht man die Entropie als eine relative Größe, und das werden wir später noch tun. Im weiteren Verlauf des Kurses begegnet sie uns an {+drei+} Stellen: {+beim Zusammenführen von Datensätzen (wie viel Information kommt durch eine weitere Spalte wirklich hinzu?),+} beim Aufstellen statistischer Modelle — das Maximum-Entropie-Prinzip im Kapitel [Normalverteilung](normalverteilung.ipynb) und das eng verwandte Maximum-Likelihood-Prinzip im Kapitel [Statistische Modelle und Schätzer](statistische-modelle.md) — und {+schließlich+} bei der Bewertung der Modellgüte, wo Kreuzentropie und relative Entropie im Kapitel [Relative Entropie](relative-entropie.md) die Werkzeuge sind.
```

German now reads:

```md
Am besten versteht man die Entropie als eine relative Größe, und das werden wir später noch tun. Im weiteren Verlauf des Kurses begegnet sie uns an drei Stellen: beim Zusammenführen von Datensätzen (wie viel Information kommt durch eine weitere Spalte wirklich hinzu?), beim Aufstellen statistischer Modelle — das Maximum-Entropie-Prinzip im Kapitel [Normalverteilung](normalverteilung.ipynb) und das eng verwandte Maximum-Likelihood-Prinzip im Kapitel [Statistische Modelle und Schätzer](statistische-modelle.md) — und schließlich bei der Bewertung der Modellgüte, wo Kreuzentropie und relative Entropie im Kapitel [Relative Entropie](relative-entropie.md) die Werkzeuge sind.
```

Current English block 277:

```md
Am besten versteht man die Entropie als eine relative Größe, und das werden wir später noch tun. Im weiteren Verlauf des Kurses begegnet sie uns an zwei Stellen: beim Aufstellen statistischer Modelle — das Maximum-Entropie-Prinzip im Kapitel [Normalverteilung](normal-distribution.ipynb) und das eng verwandte Maximum-Likelihood-Prinzip im Kapitel [Statistische Modelle und Schätzer](statistical-models.md) — und bei der Bewertung der Modellgüte, wo Kreuzentropie und relative Entropie im Kapitel [Relative Entropie](relative-entropy.md) die Werkzeuge sind.
```

### replace – German block `319` – English block(s) **319**

What changed in the German:

```diff
- Klar: [-Für $P(B) > 0$ sind-] $A$ und $B$ unabhängig voneinander genau [-dann,-] wenn $P(A | B) = P(A)$. Im Bonbon-Beispiel oben ist $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/6}{1/3} = \frac12$, und das ist nicht $P(B) = \frac13$ — so sieht Abhängigkeit in Zahlen aus. Bedingte Wahrscheinlichkeiten treten also stets dann auf (bzw. sind besonders interessant), wenn zwei Ereignisse (bzw. Zufallsvariablen) nicht unabhängig sind.
+ Klar: $A$ und $B$ {+sind+} unabhängig voneinander genau {+dann+} wenn $P(A | B) = P(A)$. Im Bonbon-Beispiel oben ist $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/6}{1/3} = \frac12$, und das ist nicht $P(B) = \frac13$ — so sieht Abhängigkeit in Zahlen aus. Bedingte Wahrscheinlichkeiten treten also stets dann auf (bzw. sind besonders interessant), wenn zwei Ereignisse (bzw. Zufallsvariablen) nicht unabhängig sind.
```

German now reads:

```md
Klar: $A$ und $B$ sind unabhängig voneinander genau dann wenn $P(A | B) = P(A)$.
Im Bonbon-Beispiel oben ist $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/6}{1/3} = \frac12$, und das ist nicht $P(B) = \frac13$ — so sieht Abhängigkeit in Zahlen aus.
Bedingte Wahrscheinlichkeiten treten also stets dann auf (bzw. sind besonders interessant), wenn zwei Ereignisse (bzw. Zufallsvariablen) nicht unabhängig sind.
```

Current English block 319:

```md
Klar: Für $P(B) > 0$ sind $A$ und $B$ unabhängig voneinander genau dann, wenn $P(A | B) = P(A)$.
Im Bonbon-Beispiel oben ist $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/6}{1/3} = \frac12$, und das ist nicht $P(B) = \frac13$ — so sieht Abhängigkeit in Zahlen aus.
Bedingte Wahrscheinlichkeiten treten also stets dann auf (bzw. sind besonders interessant), wenn zwei Ereignisse (bzw. Zufallsvariablen) nicht unabhängig sind.
```

### replace – German block `323` – English block(s) **323**

What changed in the German:

```diff
- Das zweite Maß erfasst Abhängigkeit beliebiger Form: die **relative Entropie** zwischen der gemeinsamen Verteilung und dem Produkt der Einzelverteilungen, auch *Transinformation* [-oder *gemeinsame Information* $I(X;Y)$-] genannt (Kapitel [Relative Entropie](relative-entropie.md)). Sie ist genau dann $0$, wenn die beiden Zufallsvariablen unabhängig sind — sie misst also wirklich Abhängigkeit und nicht nur ihren linearen Anteil. Der Preis dafür: Man braucht die gemeinsame Verteilung, und die zu schätzen ist deutlich aufwendiger, als eine Kovarianz auszurechnen.
+ Das zweite Maß erfasst Abhängigkeit beliebiger Form: die **relative Entropie** zwischen der gemeinsamen Verteilung und dem Produkt der Einzelverteilungen, auch *Transinformation* genannt (Kapitel [Relative Entropie](relative-entropie.md)). Sie ist genau dann $0$, wenn die beiden Zufallsvariablen unabhängig sind — sie misst also wirklich Abhängigkeit und nicht nur ihren linearen Anteil. Der Preis dafür: Man braucht die gemeinsame Verteilung, und die zu schätzen ist deutlich aufwendiger, als eine Kovarianz auszurechnen.
```

German now reads:

```md
Das zweite Maß erfasst Abhängigkeit beliebiger Form: die **relative Entropie** zwischen der gemeinsamen Verteilung und dem Produkt der Einzelverteilungen, auch *Transinformation* genannt (Kapitel [Relative Entropie](relative-entropie.md)). Sie ist genau dann $0$, wenn die beiden Zufallsvariablen unabhängig sind — sie misst also wirklich Abhängigkeit und nicht nur ihren linearen Anteil. Der Preis dafür: Man braucht die gemeinsame Verteilung, und die zu schätzen ist deutlich aufwendiger, als eine Kovarianz auszurechnen.
```

Current English block 323:

```md
Das zweite Maß erfasst Abhängigkeit beliebiger Form: die **relative Entropie** zwischen der gemeinsamen Verteilung und dem Produkt der Einzelverteilungen, auch *Transinformation* oder *gemeinsame Information* $I(X;Y)$ genannt (Kapitel [Relative Entropie](relative-entropy.md)). Sie ist genau dann $0$, wenn die beiden Zufallsvariablen unabhängig sind — sie misst also wirklich Abhängigkeit und nicht nur ihren linearen Anteil. Der Preis dafür: Man braucht die gemeinsame Verteilung, und die zu schätzen ist deutlich aufwendiger, als eine Kovarianz auszurechnen.
```

### replace – German block `339` – English block(s) **339**

What changed in the German:

```diff
- Sind $X$ und $Y$ unabhängig, so ist der Klammerausdruck nach der Produktregel gleich $0$. Der allgemeine Fall folgt [-genauso durch Ausmultiplizieren: Alle gemischten Terme $\mathbb{E}(X_iX_j) - \mathbb{E}X_i\,\mathbb{E}X_j$ mit $i \neq j$ verschwinden, und dafür genügt paarweise Unabhängigkeit (Kapitel [Kovarianz](kovarianz.md)).-]
+ Sind $X$ und $Y$ unabhängig, so ist der Klammerausdruck nach der Produktregel gleich $0$. Der allgemeine Fall folgt {+per Induktion über $n$.+}
```

German now reads:

```md
Sind $X$ und $Y$ unabhängig, so ist der Klammerausdruck nach der Produktregel gleich $0$.
Der allgemeine Fall folgt per Induktion über $n$.
```

Current English block 339:

```md
Sind $X$ und $Y$ unabhängig, so ist der Klammerausdruck nach der Produktregel gleich $0$.
Der allgemeine Fall folgt genauso durch Ausmultiplizieren: Alle gemischten Terme $\mathbb{E}(X_iX_j) - \mathbb{E}X_i\,\mathbb{E}X_j$ mit $i \neq j$ verschwinden, und dafür genügt paarweise Unabhängigkeit (Kapitel [Kovarianz](covariance.md)).
```


## numpy.ipynb → numpy.ipynb

### replace – German block `c12.0`, `c13` – English block(s) **c12.0**, **c13**

What changed in the German:

```diff
- Der Grund dafür, dass das Array den Namen `ndarray` trägt, ist, dass es für [-„$n$-dimensional array“-] steht. Wenn man in Python eine Matrix speichern möchte, würde man das als Liste der Zeilenvektoren (oder der Spaltenvektoren) tun, etwa
+ Der Grund dafür, dass das Array den Namen `ndarray` trägt, ist, dass es für {+\`\`$n$-dimensional array''+} steht. Wenn man in Python eine Matrix speichern möchte, würde man das als Liste der Zeilenvektoren (oder der Spaltenvektoren) tun, etwa
- matrix = [[1,0,0], [0,1,0], [0,0,1]] # Einheitsmatrix print(matrix, type(matrix)) quarkix = [-matrix[:]-] # eine [-"Kopie" per Slicing-] print(quarkix[0][0]) quarkix[0][0] = 0 # wir ändern den oberen linken Eintrag print(matrix[0][0])
+ matrix = [[1,0,0], [0,1,0], [0,0,1]] # Einheitsmatrix print(matrix, type(matrix)) quarkix = {+matrix+} # eine {+Kopie+} print(quarkix[0][0]) quarkix[0][0] = 0 # wir ändern den oberen linken Eintrag print(matrix[0][0])
```

German now reads:

```md
Der Grund dafür, dass das Array den Namen `ndarray` trägt, ist, dass es für \`\`$n$-dimensional array'' steht.
Wenn man in Python eine Matrix speichern möchte, würde man das als Liste der Zeilenvektoren (oder der Spaltenvektoren) tun, etwa
matrix = [[1,0,0], [0,1,0], [0,0,1]]  # Einheitsmatrix
print(matrix, type(matrix))
quarkix = matrix      # eine Kopie
print(quarkix[0][0])
quarkix[0][0] = 0     # wir ändern den oberen linken Eintrag
print(matrix[0][0])
```

Current English block c12.0:

```md
Der Grund dafür, dass das Array den Namen `ndarray` trägt, ist, dass es für „$n$-dimensional array“ steht.
Wenn man in Python eine Matrix speichern möchte, würde man das als Liste der Zeilenvektoren (oder der Spaltenvektoren) tun, etwa
```

Current English block c13:

```md
matrix = [[1,0,0], [0,1,0], [0,0,1]]  # Einheitsmatrix
print(matrix, type(matrix))
quarkix = matrix[:]   # eine "Kopie" per Slicing
print(quarkix[0][0])
quarkix[0][0] = 0     # wir ändern den oberen linken Eintrag
print(matrix[0][0])
```

### replace – German block `c20.0` – English block(s) **c20.0**

What changed in the German:

```diff
- In klassischem Python-Code würden wir auf einen Eintrag einer Matrix zugreifen mit `matrix[x][y]`, und das funktioniert so auch in Numpy. Allerdings wird dabei zunächst ein weiteres [-Array-Objekt-] `matrix[x]` erzeugt [-(eine View, siehe unten)-] und dann darauf `[y]` aufgerufen. Es ist daher grundsätzlich effizienter, direkt Numpy's `[x,y]` zu verwenden.
+ In klassischem Python-Code würden wir auf einen Eintrag einer Matrix zugreifen mit `matrix[x][y]`, und das funktioniert so auch in Numpy. Allerdings wird dabei zunächst ein weiteres {+Listenobjekt+} `matrix[x]` erzeugt {+(beim Slicing auch zusätzlicher Speicher dafür belegt)+} und dann darauf `[y]` aufgerufen. Es ist daher grundsätzlich effizienter, direkt Numpy's `[x,y]` zu verwenden.
```

German now reads:

```md
In klassischem Python-Code würden wir auf einen Eintrag einer Matrix zugreifen mit `matrix[x][y]`, und das funktioniert so auch in Numpy. Allerdings wird dabei zunächst ein weiteres Listenobjekt `matrix[x]` erzeugt (beim Slicing auch zusätzlicher Speicher dafür belegt) und dann darauf `[y]` aufgerufen. Es ist daher grundsätzlich effizienter, direkt Numpy's `[x,y]` zu verwenden.
```

Current English block c20.0:

```md
In klassischem Python-Code würden wir auf einen Eintrag einer Matrix zugreifen mit `matrix[x][y]`, und das funktioniert so auch in Numpy. Allerdings wird dabei zunächst ein weiteres Array-Objekt `matrix[x]` erzeugt (eine View, siehe unten) und dann darauf `[y]` aufgerufen. Es ist daher grundsätzlich effizienter, direkt Numpy's `[x,y]` zu verwenden.
```

### replace – German block `c30.1` – English block(s) **c30.1**

What changed in the German:

```diff
- Ein Vergleich wie `a > 2` wird elementweise ausgewertet und liefert ein Array aus `True`/`False`, eine **Maske**. Eine Maske kann man als Index verwenden: Man bekommt genau die Einträge, an denen `True` steht, und kann diesen Einträgen auch etwas zuweisen. Das ist das Werkzeug, mit dem wir im nächsten Kapitel Daten filtern ("alle Passagiere unter 13", "alle Zeilen ohne fehlenden [-Wert").-] Mit `np.where(bedingung, a, b)` wählt man elementweise aus zwei Arrays aus: dort, wo die Bedingung wahr ist, den Eintrag aus `a`, sonst den aus `b`. So ersetzt man eine `if`-Abfrage pro Element durch eine einzige Array-Operation:
+ Ein Vergleich wie `a > 2` wird elementweise ausgewertet und liefert ein Array aus `True`/`False`, eine **Maske**. Eine Maske kann man als Index verwenden: Man bekommt genau die Einträge, an denen `True` steht, und kann diesen Einträgen auch etwas zuweisen. Das ist das Werkzeug, mit dem wir im nächsten Kapitel Daten filtern ("alle Passagiere unter 13", "alle Zeilen ohne fehlenden {+Wert")).+} Mit `np.where(bedingung, a, b)` wählt man elementweise aus zwei Arrays aus: dort, wo die Bedingung wahr ist, den Eintrag aus `a`, sonst den aus `b`. So ersetzt man eine `if`-Abfrage pro Element durch eine einzige Array-Operation:
```

German now reads:

```md
Ein Vergleich wie `a > 2` wird elementweise ausgewertet und liefert ein Array aus `True`/`False`, eine **Maske**. Eine Maske kann man als Index verwenden: Man bekommt genau die Einträge, an denen `True` steht, und kann diesen Einträgen auch etwas zuweisen. Das ist das Werkzeug, mit dem wir im nächsten Kapitel Daten filtern ("alle Passagiere unter 13", "alle Zeilen ohne fehlenden Wert")). Mit `np.where(bedingung, a, b)` wählt man elementweise aus zwei Arrays aus: dort, wo die Bedingung wahr ist, den Eintrag aus `a`, sonst den aus `b`. So ersetzt man eine `if`-Abfrage pro Element durch eine einzige Array-Operation:
```

Current English block c30.1:

```md
Ein Vergleich wie `a > 2` wird elementweise ausgewertet und liefert ein Array aus `True`/`False`, eine **Maske**. Eine Maske kann man als Index verwenden: Man bekommt genau die Einträge, an denen `True` steht, und kann diesen Einträgen auch etwas zuweisen. Das ist das Werkzeug, mit dem wir im nächsten Kapitel Daten filtern ("alle Passagiere unter 13", "alle Zeilen ohne fehlenden Wert"). Mit `np.where(bedingung, a, b)` wählt man elementweise aus zwei Arrays aus: dort, wo die Bedingung wahr ist, den Eintrag aus `a`, sonst den aus `b`. So ersetzt man eine `if`-Abfrage pro Element durch eine einzige Array-Operation:
```

### replace – German block `c35.1` – English block(s) **c35.1**

What changed in the German:

```diff
- Numpy und andere Bibliotheken des Scientific Computing in Python sind groß, man kann kaum alle Funktionen kennen. [-Für dieses-] Skript liefert [-ein Durchlauf über-] die [-Code-Zellen aller Notebooks (`grep -ohE "np\.[a-z_]+(\.[a-z_]+)?"-] *.ipynb | sort [--u`, händisch bereinigt)-] diese vollständige [-Liste, Stand September 2026. Sie-] muss nicht auswendig gelernt werden, gibt aber eine klare Abschätzung nach [-oben:-] Mehr muss man definitiv auf keinen Fall können! [-**Fett** gedruckt sind die Funktionen, die man wirklich im Kopf haben sollte, weil man sie ständig tippt; der Rest ist Nachschlagewerk.-] Außerdem sollte man bedenken, dass diese Liste für das gesamte Skript gilt, und wir vieles davon noch nicht kennen gelernt haben.
+ Numpy und andere Bibliotheken des Scientific Computing in Python sind groß, man kann kaum alle Funktionen kennen. {+In diesem+} Skript liefert die {+händisch bereinigte Ausgabe von `cat+} *.ipynb | {+egrep -o "np\.([^(]+)" |+} sort {+| uniq`+} diese vollständige {+Liste. Diese+} muss nicht auswendig gelernt werden, gibt aber eine klare Abschätzung nach {+oben.+} Mehr muss man definitiv auf keinen Fall können! Außerdem sollte man bedenken, dass diese Liste für das gesamte Skript gilt, und wir vieles davon noch nicht kennen gelernt haben.
```

German now reads:

```md
Numpy und andere Bibliotheken des Scientific Computing in Python sind groß, man kann kaum alle Funktionen kennen.
In diesem Skript liefert die händisch bereinigte Ausgabe von `cat *.ipynb | egrep -o "np\.([^(]+)" | sort | uniq` diese vollständige Liste. Diese muss nicht auswendig gelernt werden, gibt aber eine klare Abschätzung nach oben. Mehr muss man definitiv auf keinen Fall können! Außerdem sollte man bedenken, dass diese Liste für das gesamte Skript gilt, und wir vieles davon noch nicht kennen gelernt haben.
```

Current English block c35.1:

```md
Numpy und andere Bibliotheken des Scientific Computing in Python sind groß, man kann kaum alle Funktionen kennen.
Für dieses Skript liefert ein Durchlauf über die Code-Zellen aller Notebooks (`grep -ohE "np\.[a-z_]+(\.[a-z_]+)?" *.ipynb | sort -u`, händisch bereinigt) diese vollständige Liste, Stand September 2026. Sie muss nicht auswendig gelernt werden, gibt aber eine klare Abschätzung nach oben: Mehr muss man definitiv auf keinen Fall können! **Fett** gedruckt sind die Funktionen, die man wirklich im Kopf haben sollte, weil man sie ständig tippt; der Rest ist Nachschlagewerk. Außerdem sollte man bedenken, dass diese Liste für das gesamte Skript gilt, und wir vieles davon noch nicht kennen gelernt haben.
```

### replace – German block `c36.0` – English block(s) **c36.0**

What changed in the German:

```diff
- * [-**abs**-] * [-**all**-] * [-**allclose**-] * [-append-] * [-**arange**-] * [-**argmin** * **array**-] * atleast_1d * [-bincount *-] byte [-* c_-] * column_stack * [-**concatenate**-] * [-**copy**-] * [-**corrcoef**-] * cos * [-**cov**-] * [-**cumsum**-] * [-diag * **diff** * **dot**-] * dstack * equal * [-**exp**-] * [-**eye**-] * float64 * [-**full**-] * genfromtxt * heaviside * [-**hstack**-] * identity * [-**isclose**-] * [-**isnan** * linalg.det-] * linalg.eig * [-linalg.eigh-] * [-**linalg.inv** * **linalg.norm**-] * linalg.svd * [-**linspace**-] * [-**log**-] * [-log2-] * [-logspace-] * [-**matmul** * **max** * **maximum**-] * may_share_memory * [-**mean**-] * [-**median**-] * [-**meshgrid**-] * mgrid * [-**min**-] * [-**minimum** * **nan**-] * nansum * [-**ones**-] * ones_like * outer * [-**pi**-] * power * ptp * [-**random.choice** * **random.default_rng**-] * random.multivariate_normal * random.permutation * random.rand * random.randint * random.randn * random.random * [-**random.seed**-] * random.uniform * [-**round** * searchsorted * set_printoptions-] * sin * size * [-**sort**-] * [-**sqrt**-] * [-**square**-] * [-**stack**-] * [-**std**-] * [-**sum**-] * [-**unique**-] * [-**var**-] * [-**vstack**-] * [-**where**-] * [-**zeros**-] * zeros_like
+ * {+abs+} * {+all+} * {+allclose+} * {+arange+} * {+argmin+} * {+array+} * atleast_1d * byte * column_stack * {+concatenate+} * {+copy+} * {+corrcoef+} * cos * {+cov+} * {+diff+} * {+dot+} * dstack * equal * {+exp+} * {+eye+} * float64 * {+frombuffer * full+} * genfromtxt * heaviside * {+hstack+} * identity * {+isclose+} * {+isnan+} * linalg.eig * {+linalg.inv+} * {+linalg.norm+} * linalg.svd * {+linspace+} * {+log+} * {+matmul+} * {+max+} * {+maximum+} * may_share_memory * {+mean+} * {+median+} * {+meshgrid+} * mgrid * {+min+} * {+minimum+} * nansum * {+ones+} * ones_like * outer * {+pi+} * power * ptp * {+random.choice+} * random.multivariate_normal * random.permutation * random.rand * random.randint * random.randn * random.random * {+random.seed+} * random.uniform * {+round+} * sin * size * {+sort+} * {+sqrt+} * {+square+} * {+stack+} * {+std+} * {+sum+} * {+uint8+} * {+unique+} * {+var+} * {+vstack+} * {+zeros+} * zeros_like
```

German now reads:

```md
 * abs
 * all
 * allclose
 * arange
 * argmin
 * array
 * atleast_1d
 * byte
 * column_stack
 * concatenate
 * copy
 * corrcoef
 * cos
 * cov
 * diff
 * dot
 * dstack
 * equal
 * exp
 * eye
 * float64
 * frombuffer
 * full
 * genfromtxt
 * heaviside
 * hstack
 * identity
 * isclose
 * isnan
 * linalg.eig
 * linalg.inv
 * linalg.norm
 * linalg.svd
 * linspace
 * log
 * matmul
 * max
 * maximum
 * may_share_memory
 * mean
 * median
 * meshgrid
 * mgrid
 * min
 * minimum
 * nansum
 * ones
 * ones_like
 * outer
 * pi
 * power
 * ptp
 * random.choice
 * random.multivariate_normal
 * random.permutation
 * random.rand
 * random.randint
 * random.randn
 * random.random
 * random.seed
 * random.uniform
 * round
 * sin
 * size
 * sort
 * sqrt
 * square
 * stack
 * std
 * sum
 * uint8
 * unique
 * var
 * vstack
 * zeros
 * zeros_like
```

Current English block c36.0:

```md
 * **abs**
 * **all**
 * **allclose**
 * append
 * **arange**
 * **argmin**
 * **array**
 * atleast_1d
 * bincount
 * byte
 * c_
 * column_stack
 * **concatenate**
 * **copy**
 * **corrcoef**
 * cos
 * **cov**
 * **cumsum**
 * diag
 * **diff**
 * **dot**
 * dstack
 * equal
 * **exp**
 * **eye**
 * float64
 * **full**
 * genfromtxt
 * heaviside
 * **hstack**
 * identity
 * **isclose**
 * **isnan**
 * linalg.det
 * linalg.eig
 * linalg.eigh
 * **linalg.inv**
 * **linalg.norm**
 * linalg.svd
 * **linspace**
 * **log**
 * log2
 * logspace
 * **matmul**
 * **max**
 * **maximum**
 * may_share_memory
 * **mean**
 * **median**
 * **meshgrid**
 * mgrid
 * **min**
 * **minimum**
 * **nan**
 * nansum
 * **ones**
 * ones_like
 * outer
 * **pi**
 * power
 * ptp
 * **random.choice**
 * **random.default_rng**
 * random.multivariate_normal
 * random.permutation
 * random.rand
 * random.randint
 * random.randn
 * random.random
 * **random.seed**
 * random.uniform
 * **round**
 * searchsorted
 * set_printoptions
 * sin
 * size
 * **sort**
 * **sqrt**
 * **square**
 * **stack**
 * **std**
 * **sum**
 * **unique**
 * **var**
 * **vstack**
 * **where**
 * **zeros**
 * zeros_like
```


## explorative-analyse-mit-numpy.ipynb → titanic-eda-numpy.ipynb

### replace – German block `c14.0` – English block(s) **c14.0**

What changed in the German:

```diff
- ## Visualisierung: [-Überleben nach Geschlecht-]
+ ## Visualisierung: {+Survival by Sex+}
```

German now reads:

```md
## Visualisierung: Survival by Sex
```

Current English block c14.0:

```md
## Visualisierung: Überleben nach Geschlecht
```

### replace – German block `c21` – English block(s) **c21**

What changed in the German:

```diff
- acc, prec, rec = kennzahlen((sex == 'female') | (~missing & (age < [-13)))-] print(f"Frauen und Kinder Accuracy {acc:.3f} Precision {prec:.3f} Recall {rec:.3f}")
+ acc, prec, rec = kennzahlen((sex == 'female') | (~missing & (age < {+15)))+} print(f"Frauen und Kinder Accuracy {acc:.3f} Precision {prec:.3f} Recall {rec:.3f}")
```

German now reads:

```md
acc, prec, rec = kennzahlen((sex == 'female') | (~missing & (age < 15)))
print(f"Frauen und Kinder  Accuracy {acc:.3f}   Precision {prec:.3f}   Recall {rec:.3f}")
```

Current English block c21:

```md
acc, prec, rec = kennzahlen((sex == 'female') | (~missing & (age < 13)))
print(f"Frauen und Kinder  Accuracy {acc:.3f}   Precision {prec:.3f}   Recall {rec:.3f}")
```


## stetige-verteilungen.md → continuous-distributions.md

### replace – German block `7`, `8` – English block(s) **7**, **8**

What changed in the German:

```diff
- [-Der *Träger* von $X$ ist-] die kleinste [-**abgeschlossene**-] Menge $A [-\subseteq-] \mathbb{R}$ mit $P(X \in [-A) = 1$,-]
+ {+Man nennt+} die kleinste Menge $A {+\subset+} \mathbb{R}$ mit $P(X \in {+A)=1$ den *Träger* von $X$ und schreibt auch+}
- $$ \operatorname{supp}(X) = [-\bigcap-] \{ A \subseteq \mathbb{R} [-\text{ abgeschlossen}-] : P(X \in A) = 1 [-\}.-] $$
+ $$ \operatorname{supp}(X) = {+\overline{\bigcap+} \{ A \subseteq \mathbb{R} : P(X \in A) = 1 {+\}}+} $$
```

German now reads:

```md
Man nennt die kleinste Menge $A \subset \mathbb{R}$ mit $P(X \in A)=1$ den *Träger* von $X$ und schreibt auch
$$
\operatorname{supp}(X) = \overline{\bigcap \{ A \subseteq \mathbb{R} : P(X \in A) = 1 \}}
$$
```

Current English block 7:

```md
Der *Träger* von $X$ ist die kleinste **abgeschlossene** Menge $A \subseteq \mathbb{R}$ mit $P(X \in A) = 1$,
```

Current English block 8:

```md
$$
\operatorname{supp}(X) = \bigcap \{ A \subseteq \mathbb{R} \text{ abgeschlossen} : P(X \in A) = 1 \}.
$$
```

### replace – German block `10` – English block(s) **10**

What changed in the German:

```diff
- [-Das Wort *abgeschlossen*-] ist [-dabei-] keine [-Dekoration. Ohne es wäre der Schnitt für jede Verteilung mit Dichte leer: Für $X \sim U([0,1])$ hat $[0,1] \setminus \{x\}$ für jedes einzelne $x$ noch-] Wahrscheinlichkeit [-$1$ (einzelne Punkte sind Nullmengen, dazu gleich mehr), also läge kein Punkt in allen diesen Mengen. Verlangt man abgeschlossene Mengen, kommt $[0,1]$ heraus, wie es sein soll. (Dass der Schnitt selbst wieder Wahrscheinlichkeit $1$ hat, weil man mit abzählbar vielen der $A$ auskommt, benutzen wir nicht weiter.)-]
+ {+In der Formel steckt ein Querstrich: $\overline{M}$+} ist {+der *Abschluss* von $M$, die kleinste abgeschlossene Menge, die $M$ enthält. Er steht da, damit der Träger nicht an Randpunkten hängen bleibt, die einzeln+} keine Wahrscheinlichkeit {+tragen.+}
```

German now reads:

```md
In der Formel steckt ein Querstrich: $\overline{M}$ ist der *Abschluss* von $M$, die kleinste abgeschlossene Menge, die $M$ enthält. Er steht da, damit der Träger nicht an Randpunkten hängen bleibt, die einzeln keine Wahrscheinlichkeit tragen.
```

Current English block 10:

```md
Das Wort *abgeschlossen* ist dabei keine Dekoration. Ohne es wäre der Schnitt für jede Verteilung mit Dichte leer: Für $X \sim U([0,1])$ hat $[0,1] \setminus \{x\}$ für jedes einzelne $x$ noch Wahrscheinlichkeit $1$ (einzelne Punkte sind Nullmengen, dazu gleich mehr), also läge kein Punkt in allen diesen Mengen. Verlangt man abgeschlossene Mengen, kommt $[0,1]$ heraus, wie es sein soll. (Dass der Schnitt selbst wieder Wahrscheinlichkeit $1$ hat, weil man mit abzählbar vielen der $A$ auskommt, benutzen wir nicht weiter.)
```

### replace – German block `15`, `16`, `17` – English block(s) **15**, **16**, **17**

What changed in the German:

```diff
- Für eine diskrete Verteilung mit pmf $p$ [-und endlich vielen Werten-] vereinfacht sich der Träger zu
+ Für eine diskrete Verteilung mit pmf $p$ vereinfacht sich der Träger zu
- $$ [-\operatorname{supp}(X)-] = \{\, x \ \mid\ p(x) > 0 \,\}, $$
+ $$ {+\operatorname{supp}(P)+} = \{\, x \ \mid\ p(x) > 0 \,\}, $$
- also zu der Menge der Werte, die überhaupt vorkommen [-können (bei unendlich vielen Werten kommen noch deren Häufungspunkte dazu, denn der Träger ist abgeschlossen).-]
+ also zu der Menge der Werte, die überhaupt vorkommen {+können.+}
```

German now reads:

```md
Für eine diskrete Verteilung mit pmf $p$ vereinfacht sich der Träger zu
$$
\operatorname{supp}(P) = \{\, x \ \mid\ p(x) > 0 \,\},
$$
also zu der Menge der Werte, die überhaupt vorkommen können.
```

Current English block 15:

```md
Für eine diskrete Verteilung mit pmf $p$ und endlich vielen Werten vereinfacht sich der Träger zu
```

Current English block 16:

```md
$$
\operatorname{supp}(X) = \{\, x \ \mid\ p(x) > 0 \,\},
$$
```

Current English block 17:

```md
also zu der Menge der Werte, die überhaupt vorkommen können (bei unendlich vielen Werten kommen noch deren Häufungspunkte dazu, denn der Träger ist abgeschlossen).
```

### replace – German block `22` – English block(s) **22**

What changed in the German:

```diff
- Der Träger ist auch für diskrete reelle Zufallsvariablen definiert - der offensichtliche Unterschied ist, dass [-der-] Träger [-einer diskreten Zufallsvariable-] kein Intervall [-enthält.-]
+ Der Träger ist auch für diskrete reelle Zufallsvariablen definiert - der offensichtliche Unterschied ist, dass {+per definitionem diskrete Zufallsvariablen einen diskreten+} Träger {+haben (d.h. eine Menge reeller Zahlen, die keinen Häufungspunkt hat, insbesondere+} kein Intervall {+enthält).+}
```

German now reads:

```md
Der Träger ist auch für diskrete reelle Zufallsvariablen definiert - der offensichtliche Unterschied ist, dass per definitionem diskrete Zufallsvariablen einen diskreten Träger haben (d.h. eine Menge reeller Zahlen, die keinen Häufungspunkt hat, insbesondere kein Intervall enthält).
```

Current English block 22:

```md
Der Träger ist auch für diskrete reelle Zufallsvariablen definiert - der offensichtliche Unterschied ist, dass der Träger einer diskreten Zufallsvariable kein Intervall enthält.
```

### replace – German block `30` – English block(s) **30**

What changed in the German:

```diff
- $$ \int_{X^{-1}(A)} [-dP(\omega)-] = P(X \in A) = P_X(A) = \int_A f(x) dx $$
+ $$ \int_{X^{-1}(A)} {+d\omega+} = P(X \in A) = P_X(A) = \int_A f(x) dx $$
```

German now reads:

```md
$$
\int_{X^{-1}(A)} d\omega = P(X \in A) = P_X(A) = \int_A f(x) dx
$$
```

Current English block 30:

```md
$$
\int_{X^{-1}(A)} dP(\omega) = P(X \in A) = P_X(A) = \int_A f(x) dx
$$
```

### replace – German block `34` – English block(s) **34**

What changed in the German:

```diff
- $$ \mathbb{E}(X) = \int_\Omega [-X(\omega)\, dP(\omega)-] = \int_D x f(x) dx $$
+ $$ \mathbb{E}(X) = \int_\Omega {+X(\omega) d \omega+} = \int_D x f(x) dx $$
```

German now reads:

```md
$$
\mathbb{E}(X) = \int_\Omega X(\omega) d \omega = \int_D x f(x) dx
$$
```

Current English block 34:

```md
$$
\mathbb{E}(X) = \int_\Omega X(\omega)\, dP(\omega) = \int_D x f(x) dx
$$
```

### replace – German block `36` – English block(s) **36**

What changed in the German:

```diff
- $$ \mathbb{V}(X) = \int_\Omega \left(X(\omega)-\mathbb{E}(X)\right)^2 [-dP(\omega)-] = \int_D \left(x-\mathbb{E}(X)\right)^2 f(x) dx $$
+ $$ \mathbb{V}(X) = \int_\Omega \left(X(\omega)-\mathbb{E}(X)\right)^2 {+d \omega+} = \int_D \left(x-\mathbb{E}(X)\right)^2 f(x) dx $$
```

German now reads:

```md
$$
\mathbb{V}(X) = \int_\Omega \left(X(\omega)-\mathbb{E}(X)\right)^2 d \omega = \int_D \left(x-\mathbb{E}(X)\right)^2 f(x) dx
$$
```

Current English block 36:

```md
$$
\mathbb{V}(X) = \int_\Omega \left(X(\omega)-\mathbb{E}(X)\right)^2 dP(\omega) = \int_D \left(x-\mathbb{E}(X)\right)^2 f(x) dx
$$
```


## normalverteilung.ipynb → normal-distribution.ipynb

### replace – German block `c4.3` – English block(s) **c4.3**

What changed in the German:

```diff
- Was uns für Binomialkoeffizienten direkt liefert: $\binom{n}{k} [-\approx-] \frac{\sqrt{n}}{\sqrt{2\pi}\sqrt{k}\sqrt{n-k} } \frac{n^n}{k^k {\left(n-k\right)}^{(n-k)} }$
+ Was uns für Binomialkoeffizienten direkt liefert: $\binom{n}{k} {+=+} \frac{\sqrt{n}}{\sqrt{2\pi}\sqrt{k}\sqrt{n-k} } \frac{n^n}{k^k {\left(n-k\right)}^{(n-k)} }$
```

German now reads:

```md
Was uns für Binomialkoeffizienten direkt liefert: $\binom{n}{k} = \frac{\sqrt{n}}{\sqrt{2\pi}\sqrt{k}\sqrt{n-k} }  \frac{n^n}{k^k {\left(n-k\right)}^{(n-k)} }$
```

Current English block c4.3:

```md
Was uns für Binomialkoeffizienten direkt liefert: $\binom{n}{k} \approx \frac{\sqrt{n}}{\sqrt{2\pi}\sqrt{k}\sqrt{n-k} }  \frac{n^n}{k^k {\left(n-k\right)}^{(n-k)} }$
```

### replace – German block `c6.1` – English block(s) **c6.1**

What changed in the German:

```diff
- Diese Approximation ist insofern hilfreich, als dass wir nun die Funktion $e^{-\frac{x^2}{2}}$ tabellieren können und konkrete Werte für gewisse $n,p$ ablesen können. Das ist wesentlich effizienter, als Binomialkoeffizienten auszurechnen. Die ganze Beobachtung heißt auch **Satz** von [-de Moivre-Laplace-] und soll uns zunächst als Motivation dienen, die Funktion $e^{-\frac{x^2}{2}}$ näher zu untersuchen.
+ Diese Approximation ist insofern hilfreich, als dass wir nun die Funktion $e^{-\frac{x^2}{2}}$ tabellieren können und konkrete Werte für gewisse $n,p$ ablesen können. Das ist wesentlich effizienter, als Binomialkoeffizienten auszurechnen. Die ganze Beobachtung heißt auch **Satz** von {+deMoivre-Laplace+} und soll uns zunächst als Motivation dienen, die Funktion $e^{-\frac{x^2}{2}}$ näher zu untersuchen.
```

German now reads:

```md
Diese Approximation ist insofern hilfreich, als dass wir nun die Funktion $e^{-\frac{x^2}{2}}$ tabellieren können und konkrete Werte für gewisse $n,p$ ablesen können. Das ist wesentlich effizienter, als Binomialkoeffizienten auszurechnen. Die ganze Beobachtung heißt auch **Satz** von deMoivre-Laplace und soll uns zunächst als Motivation dienen, die Funktion $e^{-\frac{x^2}{2}}$ näher zu untersuchen.
```

Current English block c6.1:

```md
Diese Approximation ist insofern hilfreich, als dass wir nun die Funktion $e^{-\frac{x^2}{2}}$ tabellieren können und konkrete Werte für gewisse $n,p$ ablesen können. Das ist wesentlich effizienter, als Binomialkoeffizienten auszurechnen. Die ganze Beobachtung heißt auch **Satz** von de Moivre-Laplace und soll uns zunächst als Motivation dienen, die Funktion $e^{-\frac{x^2}{2}}$ näher zu untersuchen.
```

### replace – German block `c10` – English block(s) **c10**

What changed in the German:

```diff
- x = np.linspace(20,60,100) plt.hist(binom_samples, bins=40, density=True) plt.plot(x, [-norm(loc=40, scale=np.sqrt(24)).pdf(x),-] color="red") [-# Erwartungswert n p = 40, Varianz n p (1-p) = 24-] plt.ylabel('Dichte') plt.title('Normalverteilungs-Dichte (rot) und Binomial-Histogramm (blau)') plt.show()
+ x = np.linspace(20,60,100) plt.hist(binom_samples, bins=40, density=True) plt.plot(x, {+norm(loc=40.5, scale=5).pdf(x),+} color="red") plt.ylabel('Dichte') plt.title('Normalverteilungs-Dichte (rot) und Binomial-Histogramm (blau)') plt.show()
```

German now reads:

```md
x = np.linspace(20,60,100)
plt.hist(binom_samples, bins=40, density=True)
plt.plot(x, norm(loc=40.5, scale=5).pdf(x), color="red")
plt.ylabel('Dichte')
plt.title('Normalverteilungs-Dichte (rot) und Binomial-Histogramm (blau)')
plt.show()
```

Current English block c10:

```md
x = np.linspace(20,60,100)
plt.hist(binom_samples, bins=40, density=True)
plt.plot(x, norm(loc=40, scale=np.sqrt(24)).pdf(x), color="red")   # Erwartungswert n p = 40, Varianz n p (1-p) = 24
plt.ylabel('Dichte')
plt.title('Normalverteilungs-Dichte (rot) und Binomial-Histogramm (blau)')
plt.show()
```

### delete – German block `c11.9` – English block(s) **c11.9**

Current English block c11.9:

```md
Nach derselben Substitution $x \to x + \mu$ und Ausmultiplizieren von $(x+\mu)^2$ bleibt $\frac{1}{\sigma\sqrt{2\pi}} \int x^2 e^{-x^2/2\sigma^2}\,dx$ übrig (der gemischte Term ist wieder ungerade, der $\mu^2$-Term hebt sich weg), und partielle Integration mit $u = x$, $v' = x e^{-x^2/2\sigma^2}$ liefert dafür $\sigma^2$; die Details überlassen wir Ihnen.
```

### replace – German block `c12.21` – English block(s) **c12.21**

What changed in the German:

```diff
- Außerdem nutzen wir, dass die Summe von unabhängigen Zufallsvariablen mit Dichten $f,g$ selbst wieder eine Dichte hat, nämlich die *Faltung* $f \ast g$. Anstatt das rigoros einzuführen und zu beweisen, [-halten-] wir [-nur das Ergebnis-] für [-Normalverteilungen fest, das man mit der Faltung nachrechnen kann.-]
+ Außerdem nutzen wir, dass die Summe von unabhängigen Zufallsvariablen mit Dichten $f,g$ selbst wieder eine Dichte hat, nämlich die *Faltung* $f \ast g$. Anstatt das rigoros einzuführen und zu beweisen, {+benutzen+} wir {+es weiter unten+} für {+die Summe zweier Normalverteilungen.+}
```

German now reads:

```md
Außerdem nutzen wir, dass die Summe von unabhängigen Zufallsvariablen mit Dichten $f,g$ selbst wieder eine Dichte hat, nämlich die *Faltung* $f \ast g$. Anstatt das rigoros einzuführen und zu beweisen, benutzen wir es weiter unten für die Summe zweier Normalverteilungen.
```

Current English block c12.21:

```md
Außerdem nutzen wir, dass die Summe von unabhängigen Zufallsvariablen mit Dichten $f,g$ selbst wieder eine Dichte hat, nämlich die *Faltung* $f \ast g$. Anstatt das rigoros einzuführen und zu beweisen, halten wir nur das Ergebnis für Normalverteilungen fest, das man mit der Faltung nachrechnen kann.
```

### replace – German block `c12.34` – English block(s) **c12.34**

What changed in the German:

```diff
- Die Steckbriefe der drei stetigen Verteilungen stehen im Kapitel [Wichtigste stetige Verteilungen](wichtigste-stetige-verteilungen.ipynb), die diskrete Gleichverteilung im Kapitel [-[Wichtigste diskrete Verteilungen](wichtigste-diskrete-verteilungen.ipynb).-] Die gestutzte Normalverteilung ist genau das, wonach es klingt: eine Normalverteilung, deren Dichte außerhalb von $[a,b]$ auf $0$ gesetzt und innerhalb neu normiert wird. Man braucht sie, wenn eine Größe von Natur aus beschränkt ist — Anteile zwischen $0$ und $1$, Messwerte an der Anzeigegrenze eines Geräts — und ein Normalverteilungsmodell sonst Wahrscheinlichkeitsmasse dort verteilen würde, wo es gar keine Werte geben kann.
+ Die Steckbriefe der drei stetigen Verteilungen stehen im Kapitel [Wichtigste stetige Verteilungen](wichtigste-stetige-verteilungen.ipynb), die diskrete Gleichverteilung im Kapitel {+[Erwartungswert und Varianz](erwartungswert.md).+} Die gestutzte Normalverteilung ist genau das, wonach es klingt: eine Normalverteilung, deren Dichte außerhalb von $[a,b]$ auf $0$ gesetzt und innerhalb neu normiert wird. Man braucht sie, wenn eine Größe von Natur aus beschränkt ist — Anteile zwischen $0$ und $1$, Messwerte an der Anzeigegrenze eines Geräts — und ein Normalverteilungsmodell sonst Wahrscheinlichkeitsmasse dort verteilen würde, wo es gar keine Werte geben kann.
```

German now reads:

```md
Die Steckbriefe der drei stetigen Verteilungen stehen im Kapitel [Wichtigste stetige Verteilungen](wichtigste-stetige-verteilungen.ipynb), die diskrete Gleichverteilung im Kapitel [Erwartungswert und Varianz](erwartungswert.md). Die gestutzte Normalverteilung ist genau das, wonach es klingt: eine Normalverteilung, deren Dichte außerhalb von $[a,b]$ auf $0$ gesetzt und innerhalb neu normiert wird. Man braucht sie, wenn eine Größe von Natur aus beschränkt ist — Anteile zwischen $0$ und $1$, Messwerte an der Anzeigegrenze eines Geräts — und ein Normalverteilungsmodell sonst Wahrscheinlichkeitsmasse dort verteilen würde, wo es gar keine Werte geben kann.
```

Current English block c12.34:

```md
Die Steckbriefe der drei stetigen Verteilungen stehen im Kapitel [Wichtigste stetige Verteilungen](important-continuous-distributions.ipynb), die diskrete Gleichverteilung im Kapitel [Wichtigste diskrete Verteilungen](important-discrete-distributions.ipynb). Die gestutzte Normalverteilung ist genau das, wonach es klingt: eine Normalverteilung, deren Dichte außerhalb von $[a,b]$ auf $0$ gesetzt und innerhalb neu normiert wird. Man braucht sie, wenn eine Größe von Natur aus beschränkt ist — Anteile zwischen $0$ und $1$, Messwerte an der Anzeigegrenze eines Geräts — und ein Normalverteilungsmodell sonst Wahrscheinlichkeitsmasse dort verteilen würde, wo es gar keine Werte geben kann.
```


## wichtigste-stetige-verteilungen.ipynb → important-continuous-distributions.ipynb

### delete – German block `c0.1` – English block(s) **c0.1**

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Stetige Verteilungen in SciPy (VL 9, erste 40 Minuten)](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167)
[Fortsetzung (VL 10, erste 40 Minuten)](https://media.hhu.de/channel/video/data-science-vl-10-skalenniveaus-2025/9b824315922a75d933e081f31c1da388/167)
```

### replace – German block `c11.2` – English block(s) **c11.2**

What changed in the German:

```diff
- * Parameter $\mu,\sigma$, Notation $\mathcal{N}(\mu,\sigma^2)$ * Dichte $\phi(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ * Erwartungswert $\mu$ * Varianz $\sigma^2$ * [-Alle ungeraden zentralen-] Momente sind $0$ [-(die Dichte ist symmetrisch;-] ein [-ungerades Moment $\neq 0$ ist deshalb ein Zeichen von Asymmetrie)-] * Maximale Entropie bei festem Erwartungswert und fester Varianz und Träger ganz $\mathbb{R}$ * [-Zentraler Grenzwertsatz: Für-] iid [-$X_i$ mit Erwartungswert $\mu$ und Varianz $\sigma^2$ ist die standardisierte Summe $Z_N = \frac{1}{\sigma\sqrt{N}} \sum_{i=1}^N (X_i - \mu)$ für große $N$ näherungsweise $\mathcal{N}(0,1)$-verteilt, gleichbedeutend $\frac{1}{N}\sum_{i=1}^N-] X_i [-\approx \mathcal{N}\!\left(\mu, \frac{\sigma^2}{N}\right)$ (Kapitel [Normalverteilung](normalverteilung.ipynb))-] * Anwendungsbeispiele: * Messfehler in physikalischen Systemen * Fertigungsgenauigkeit * Biologische Größen (Körperlänge etc.)
+ * Parameter $\mu,\sigma$, Notation $\mathcal{N}(\mu,\sigma^2)$ * Dichte $\phi(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ * Erwartungswert $\mu$ * Varianz $\sigma^2$ * {+Höhere ungerade zentrale+} Momente sind {+alle+} $0$ {+\ (daher sind ungerade Momente+} ein {+Maß für nicht-Normalität)+} * Maximale Entropie bei festem Erwartungswert und fester Varianz und Träger ganz $\mathbb{R}$ * {+ZGWS: Folge+} iid {+Zufallsvariablen $X_i$, dann $\sum_{i=1}^N+} X_i {+\xrightarrow{N \to \infty} \mathcal{N}(\mu,\sigma^2)$+} * Anwendungsbeispiele: * Messfehler in physikalischen Systemen * Fertigungsgenauigkeit * Biologische Größen (Körperlänge etc.)
```

German now reads:

```md
* Parameter $\mu,\sigma$, Notation $\mathcal{N}(\mu,\sigma^2)$
* Dichte $\phi(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
* Erwartungswert $\mu$
* Varianz $\sigma^2$
* Höhere ungerade zentrale Momente sind alle $0$ \
  (daher sind ungerade Momente ein Maß für nicht-Normalität)
* Maximale Entropie bei festem Erwartungswert und fester Varianz und Träger ganz $\mathbb{R}$
* ZGWS: Folge iid Zufallsvariablen $X_i$, dann $\sum_{i=1}^N X_i \xrightarrow{N \to \infty} \mathcal{N}(\mu,\sigma^2)$
* Anwendungsbeispiele:
  * Messfehler in physikalischen Systemen
  * Fertigungsgenauigkeit
  * Biologische Größen (Körperlänge etc.)
```

Current English block c11.2:

```md
* Parameter $\mu,\sigma$, Notation $\mathcal{N}(\mu,\sigma^2)$
* Dichte $\phi(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
* Erwartungswert $\mu$
* Varianz $\sigma^2$
* Alle ungeraden zentralen Momente sind $0$ (die Dichte ist symmetrisch; ein ungerades Moment $\neq 0$ ist deshalb ein Zeichen von Asymmetrie)
* Maximale Entropie bei festem Erwartungswert und fester Varianz und Träger ganz $\mathbb{R}$
* Zentraler Grenzwertsatz: Für iid $X_i$ mit Erwartungswert $\mu$ und Varianz $\sigma^2$ ist die standardisierte Summe $Z_N = \frac{1}{\sigma\sqrt{N}} \sum_{i=1}^N (X_i - \mu)$ für große $N$ näherungsweise $\mathcal{N}(0,1)$-verteilt, gleichbedeutend $\frac{1}{N}\sum_{i=1}^N X_i \approx \mathcal{N}\!\left(\mu, \frac{\sigma^2}{N}\right)$ (Kapitel [Normalverteilung](normal-distribution.ipynb))
* Anwendungsbeispiele:
  * Messfehler in physikalischen Systemen
  * Fertigungsgenauigkeit
  * Biologische Größen (Körperlänge etc.)
```

### replace – German block `c13` – English block(s) **c13**

What changed in the German:

```diff
- X = st.norm(loc=3, scale=2) Xsamples = X.rvs(size=10000) plt.hist(Xsamples, bins=200, density=True) plt.xlabel("10000 Samples von [-N(3, 2²),-] in 200 Bins") plt.ylabel("Dichte") plt.show()
+ X = st.norm(loc=3, scale=2) Xsamples = X.rvs(size=10000) plt.hist(Xsamples, bins=200, density=True) plt.xlabel("10000 Samples von {+N(3,2),+} in 200 Bins") plt.ylabel("Dichte") plt.show()
```

German now reads:

```md
X = st.norm(loc=3, scale=2)
Xsamples = X.rvs(size=10000)
plt.hist(Xsamples, bins=200, density=True)
plt.xlabel("10000 Samples von N(3,2), in 200 Bins")
plt.ylabel("Dichte")
plt.show()
```

Current English block c13:

```md
X = st.norm(loc=3, scale=2)
Xsamples = X.rvs(size=10000)
plt.hist(Xsamples, bins=200, density=True)
plt.xlabel("10000 Samples von N(3, 2²), in 200 Bins")
plt.ylabel("Dichte")
plt.show()
```

### replace – German block `c15` – English block(s) **c15**

What changed in the German:

```diff
- name = [-"0.6·N(0,1)-] + [-0.4·N(2, 0.5²)"-] def f(x, epsilon=0.6, mu1=0, sigma1=1, mu2=2, sigma2=0.5): norm1 = st.norm(loc=mu1, scale=sigma1) norm2 = st.norm(loc=mu2, scale=sigma2) return epsilon*norm1.pdf(x) + (1-epsilon)*norm2.pdf(x) x = np.linspace(-3,3,100) plt.plot(x, f(x)) plt.ylabel('Dichte') plt.title(f"PDF von {name}") plt.show()
+ name = {+"0.6*N(0,1)+} + {+0.4*N(2,0.5)"+} def f(x, epsilon=0.6, mu1=0, sigma1=1, mu2=2, sigma2=0.5): norm1 = st.norm(loc=mu1, scale=sigma1) norm2 = st.norm(loc=mu2, scale=sigma2) return epsilon*norm1.pdf(x) + (1-epsilon)*norm2.pdf(x) x = np.linspace(-3,3,100) plt.plot(x, f(x)) plt.ylabel('Dichte') plt.title(f"PDF von {name}") plt.show()
```

German now reads:

```md
name = "0.6*N(0,1) + 0.4*N(2,0.5)"
def f(x, epsilon=0.6, mu1=0, sigma1=1, mu2=2, sigma2=0.5):
    norm1 = st.norm(loc=mu1, scale=sigma1)
    norm2 = st.norm(loc=mu2, scale=sigma2)
    return epsilon*norm1.pdf(x) + (1-epsilon)*norm2.pdf(x)

x = np.linspace(-3,3,100)
plt.plot(x, f(x))
plt.ylabel('Dichte')
plt.title(f"PDF von {name}")
plt.show()
```

Current English block c15:

```md
name = "0.6·N(0,1) + 0.4·N(2, 0.5²)"
def f(x, epsilon=0.6, mu1=0, sigma1=1, mu2=2, sigma2=0.5):
    norm1 = st.norm(loc=mu1, scale=sigma1)
    norm2 = st.norm(loc=mu2, scale=sigma2)
    return epsilon*norm1.pdf(x) + (1-epsilon)*norm2.pdf(x)

x = np.linspace(-3,3,100)
plt.plot(x, f(x))
plt.ylabel('Dichte')
plt.title(f"PDF von {name}")
plt.show()
```

### replace – German block `c16.1` – English block(s) **c16.1**

What changed in the German:

```diff
- * Parameter $\xi$, Notation $\delta(\xi)$ * Ohne Dichte, aber $P(X = \xi) = 1$ * Erwartungswert $\xi$ * Varianz $0$ * Entropie $0$ [-(als diskrete Verteilung gelesen; eine differentielle Entropie hat sie nicht)-] * Anwendungsbeispiele: * 'Dichtefunktionen' im stetigen Sinne für diskrete Verteilungen hinschreiben * Fotos vom Sternenhimmel (z.B. mit Hubble) - jeder Stern ist ein verschmierter Pixelhaufen (normalverteilt), aber die 'eigentliche' Verteilung der Sterne dahinter ist eine Summe von Dirac-Maßen, denn jeder Stern ist an genau einem Punkt (die tatsächliche Ausdehnung des Sterns ist aufgrund der Entfernung irrelevant). Mit dieser Modellierung arbeiten manche Superresolution-Techniken.
+ * Parameter $\xi$, Notation $\delta(\xi)$ * Ohne Dichte, aber $P(X = \xi) = 1$ * Erwartungswert $\xi$ * Varianz $0$ * Entropie $0$ * Anwendungsbeispiele: * 'Dichtefunktionen' im stetigen Sinne für diskrete Verteilungen hinschreiben * Fotos vom Sternenhimmel (z.B. mit Hubble) - jeder Stern ist ein verschmierter Pixelhaufen (normalverteilt), aber die 'eigentliche' Verteilung der Sterne dahinter ist eine Summe von Dirac-Maßen, denn jeder Stern ist an genau einem Punkt (die tatsächliche Ausdehnung des Sterns ist aufgrund der Entfernung irrelevant). Mit dieser Modellierung arbeiten manche Superresolution-Techniken.
```

German now reads:

```md
* Parameter $\xi$, Notation $\delta(\xi)$
* Ohne Dichte, aber $P(X = \xi) = 1$
* Erwartungswert $\xi$
* Varianz $0$
* Entropie $0$
* Anwendungsbeispiele:
  * 'Dichtefunktionen' im stetigen Sinne für diskrete Verteilungen hinschreiben
  * Fotos vom Sternenhimmel (z.B. mit Hubble) - jeder Stern ist ein verschmierter Pixelhaufen (normalverteilt), aber die 'eigentliche' Verteilung der Sterne dahinter ist eine Summe von Dirac-Maßen, denn jeder Stern ist an genau einem Punkt (die tatsächliche Ausdehnung des Sterns ist aufgrund der Entfernung irrelevant). Mit dieser Modellierung arbeiten manche Superresolution-Techniken.
```

Current English block c16.1:

```md
* Parameter $\xi$, Notation $\delta(\xi)$
* Ohne Dichte, aber $P(X = \xi) = 1$
* Erwartungswert $\xi$
* Varianz $0$
* Entropie $0$ (als diskrete Verteilung gelesen; eine differentielle Entropie hat sie nicht)
* Anwendungsbeispiele:
  * 'Dichtefunktionen' im stetigen Sinne für diskrete Verteilungen hinschreiben
  * Fotos vom Sternenhimmel (z.B. mit Hubble) - jeder Stern ist ein verschmierter Pixelhaufen (normalverteilt), aber die 'eigentliche' Verteilung der Sterne dahinter ist eine Summe von Dirac-Maßen, denn jeder Stern ist an genau einem Punkt (die tatsächliche Ausdehnung des Sterns ist aufgrund der Entfernung irrelevant). Mit dieser Modellierung arbeiten manche Superresolution-Techniken.
```

### replace – German block `c17` – English block(s) **c17**

What changed in the German:

```diff
- name = "Dirac-Verteilung bei ξ=0" plt.plot(x, np.heaviside(x, 1)) [-plt.ylabel('F(x) = P(X ≤ x)')-] plt.title("CDF von "+name) plt.show()
+ name = "Dirac-Verteilung bei ξ=0" plt.plot(x, np.heaviside(x, 1)) {+plt.ylabel('Dichte')+} plt.title("CDF von "+name) plt.show()
```

German now reads:

```md
name = "Dirac-Verteilung bei ξ=0"
plt.plot(x, np.heaviside(x, 1))
plt.ylabel('Dichte')
plt.title("CDF von "+name)
plt.show()
```

Current English block c17:

```md
name = "Dirac-Verteilung bei ξ=0"
plt.plot(x, np.heaviside(x, 1))
plt.ylabel('F(x) = P(X ≤ x)')
plt.title("CDF von "+name)
plt.show()
```

### replace – German block `c18.1` – English block(s) **c18.1**

What changed in the German:

```diff
- * Parameter $a,b$, Notation [-$U([a,b])$-] * Dichte $\frac{1}{b-a}$ * Erwartungswert $\frac{a+b}{2}$ * Varianz $\frac{(a-b)^2}{12}$ * Maximale Entropie unter allen Verteilungen mit Träger $[a,b]$ * Anwendungsbeispiele: * Wenn ein Bus an Ihrer Haltestelle extrem pünktlich jede Stunde kommt, Sie aber nicht wissen, wann er das letzte Mal gefahren ist, so ist [-Ihre-] Wartezeit an der Haltestelle in Minuten gleichverteilt in $[0,60]$. * Die Temperatur [-Ihrer-] CPU ab der dritten Nachkommastelle `(T * 100 - int(T * 100))` ist annähernd gleichverteilt.
+ * Parameter $a,b$, Notation {+$Uni(a,b)$+} * Dichte $\frac{1}{b-a}$ * Erwartungswert $\frac{a+b}{2}$ * Varianz $\frac{(a-b)^2}{12}$ * Maximale Entropie unter allen Verteilungen mit Träger $[a,b]$ * Anwendungsbeispiele: * Wenn ein Bus an Ihrer Haltestelle extrem pünktlich jede Stunde kommt, Sie aber nicht wissen, wann er das letzte Mal gefahren ist, so ist {+ihre+} Wartezeit an der Haltestelle in Minuten gleichverteilt in $[0,60]$. * Die Temperatur {+ihrer+} CPU ab der dritten Nachkommastelle `(T * 100 - int(T * 100))` ist annähernd gleichverteilt.
```

German now reads:

```md
* Parameter $a,b$, Notation $Uni(a,b)$
* Dichte $\frac{1}{b-a}$
* Erwartungswert $\frac{a+b}{2}$
* Varianz $\frac{(a-b)^2}{12}$
* Maximale Entropie unter allen Verteilungen mit Träger $[a,b]$
* Anwendungsbeispiele:
  * Wenn ein Bus an Ihrer Haltestelle extrem pünktlich jede Stunde kommt, Sie aber nicht wissen, wann er das letzte Mal gefahren ist, so ist ihre Wartezeit an der Haltestelle in Minuten gleichverteilt in $[0,60]$.
  * Die Temperatur ihrer CPU ab der dritten Nachkommastelle `(T * 100 - int(T * 100))` ist annähernd gleichverteilt.
```

Current English block c18.1:

```md
* Parameter $a,b$, Notation $U([a,b])$
* Dichte $\frac{1}{b-a}$
* Erwartungswert $\frac{a+b}{2}$
* Varianz $\frac{(a-b)^2}{12}$
* Maximale Entropie unter allen Verteilungen mit Träger $[a,b]$
* Anwendungsbeispiele:
  * Wenn ein Bus an Ihrer Haltestelle extrem pünktlich jede Stunde kommt, Sie aber nicht wissen, wann er das letzte Mal gefahren ist, so ist Ihre Wartezeit an der Haltestelle in Minuten gleichverteilt in $[0,60]$.
  * Die Temperatur Ihrer CPU ab der dritten Nachkommastelle `(T * 100 - int(T * 100))` ist annähernd gleichverteilt.
```

### replace – German block `c22.1`, `c23` – English block(s) **c22.1**, **c23**

What changed in the German:

```diff
- * Parameter $\mu, \sigma$, Notation $Lognormal(\mu,\sigma^2)$ * Dichte $\frac{1}{x\sigma\sqrt{2\pi}} [-e^{-\frac{(\log(x)-\mu)^2}{2\sigma^2}}$-] * Erwartungswert $e^{\mu + \frac{\sigma^2}{2}}$ aber [-$\mathbb{E}(\log-] X) = \mu$ * Varianz $(e^{\sigma^2}-1)e^{2\mu + \sigma^2}$ aber [-$\mathbb{V}(\log-] X) = \sigma^2$ * Maximale Entropie unter allen Verteilungen mit Träger $(0,\infty)$ und $\mathbb{E}(\log X) = \mu$ und $\mathbb{V}(\log X) = \sigma^2$ * Anwendungsbeispiele: * Die Länge eines Schachspiels ist log-normalverteilt * Viele (!) weitere Beispiele hat die [Wikipedia zur Lognormalverteilung](https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications)
+ * Parameter $\mu, \sigma$, Notation $Lognormal(\mu,\sigma^2)$ * Dichte $\frac{1}{x\sigma\sqrt{2\pi}} {+e^{-\frac{(log(x)-\mu)^2}{2\sigma^2}}$+} * Erwartungswert $e^{\mu + \frac{\sigma^2}{2}}$ aber {+$\mathbb{E}(log+} X) = \mu$ * Varianz $(e^{\sigma^2}-1)e^{2\mu + \sigma^2}$ aber {+$\mathbb{V}(log+} X) = \sigma^2$ * Maximale Entropie unter allen Verteilungen mit Träger $(0,\infty)$ und $\mathbb{E}(\log X) = \mu$ und $\mathbb{V}(\log X) = \sigma^2$ * Anwendungsbeispiele: * Die Länge eines Schachspiels ist log-normalverteilt * Viele (!) weitere Beispiele hat die [Wikipedia zur Lognormalverteilung](https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications)
- name = "Log-normalverteilung" mu, sigma = 1, 2 X = st.lognorm(s=sigma, scale = np.exp(mu)) x = [-np.linspace(0, 12, 1000)-] plotX(x,X,name,(mu, sigma))
+ name = "Log-normalverteilung" mu, sigma = 1, 2 X = st.lognorm(s=sigma, scale = np.exp(mu)) x = {+np.linspace(0,2,1000)+} plotX(x,X,name,(mu, sigma))
```

German now reads:

```md
* Parameter $\mu, \sigma$, Notation $Lognormal(\mu,\sigma^2)$
* Dichte $\frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(log(x)-\mu)^2}{2\sigma^2}}$
* Erwartungswert $e^{\mu + \frac{\sigma^2}{2}}$ aber $\mathbb{E}(log X) = \mu$
* Varianz $(e^{\sigma^2}-1)e^{2\mu + \sigma^2}$ aber $\mathbb{V}(log X) = \sigma^2$
* Maximale Entropie unter allen Verteilungen mit Träger $(0,\infty)$ und $\mathbb{E}(\log X) = \mu$ und $\mathbb{V}(\log X) = \sigma^2$
* Anwendungsbeispiele:
  * Die Länge eines Schachspiels ist log-normalverteilt
  * Viele (!) weitere Beispiele hat die [Wikipedia zur Lognormalverteilung](https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications)
name = "Log-normalverteilung"
mu, sigma = 1, 2
X = st.lognorm(s=sigma, scale = np.exp(mu))
x = np.linspace(0,2,1000)
plotX(x,X,name,(mu, sigma))
```

Current English block c22.1:

```md
* Parameter $\mu, \sigma$, Notation $Lognormal(\mu,\sigma^2)$
* Dichte $\frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\log(x)-\mu)^2}{2\sigma^2}}$
* Erwartungswert $e^{\mu + \frac{\sigma^2}{2}}$ aber $\mathbb{E}(\log X) = \mu$
* Varianz $(e^{\sigma^2}-1)e^{2\mu + \sigma^2}$ aber $\mathbb{V}(\log X) = \sigma^2$
* Maximale Entropie unter allen Verteilungen mit Träger $(0,\infty)$ und $\mathbb{E}(\log X) = \mu$ und $\mathbb{V}(\log X) = \sigma^2$
* Anwendungsbeispiele:
  * Die Länge eines Schachspiels ist log-normalverteilt
  * Viele (!) weitere Beispiele hat die [Wikipedia zur Lognormalverteilung](https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications)
```

Current English block c23:

```md
name = "Log-normalverteilung"
mu, sigma = 1, 2
X = st.lognorm(s=sigma, scale = np.exp(mu))
x = np.linspace(0, 12, 1000)
plotX(x,X,name,(mu, sigma))
```

### replace – German block `c24.1` – English block(s) **c24.1**

What changed in the German:

```diff
- * Parameter $\lambda>0, k>0$, Notation $Weibull(\lambda,k)$ * Dichte $f(x) = \dfrac{k}{\lambda} {\left(\frac{x}{\lambda}\right)}^{k-1} e^{-{\left(\frac{x}{\lambda}\right)}^k}$ für $x \geq 0$ \ und $f(x)=0$ für $x < 0$ * Erwartungswert $\lambda \Gamma(1+\frac{1}{k})$ (wobei $\Gamma(n+1) = n!$) * [-Varianz $\lambda^2 \left[ \Gamma(1+\frac{2}{k}) - \Gamma(1+\frac{1}{k})^2 \right]$ *-] Maximale Entropie unter allen Verteilungen mit [-Träger $[0,\infty)$, festem $\mathbb{E}(X^k)$-] und [-festem-] $\mathbb{E}(\log [-X)$ — der Formparameter $k$ sagt also, welches Moment festgehalten wird-] * Anwendungsbeispiele: * Wie lange läuft eine Wärmepumpe, bis sie kaputt geht? * Wie hoch ist die Windgeschwindigkeit? * Was ist die höchste Niederschlagsmenge an einem einzelnen Tag im Jahr?
+ * Parameter $\lambda>0, k>0$, Notation $Weibull(\lambda,k)$ * Dichte $f(x) = \dfrac{k}{\lambda} {\left(\frac{x}{\lambda}\right)}^{k-1} e^{-{\left(\frac{x}{\lambda}\right)}^k}$ für $x \geq 0$ \ und $f(x)=0$ für $x < 0$ * Erwartungswert $\lambda \Gamma(1+\frac{1}{k})$ (wobei $\Gamma(n+1) = n!$) * Maximale Entropie unter allen Verteilungen mit {+einer Bedingung an alle Momente: $\mathbb{E}(X^n) = \lambda^n$+} und {+einer Bedingung an+} $\mathbb{E}(\log {+X)$.+} * Anwendungsbeispiele: * Wie lange läuft eine Wärmepumpe, bis sie kaputt geht? * Wie hoch ist die Windgeschwindigkeit? * Was ist die höchste Niederschlagsmenge an einem einzelnen Tag im Jahr?
```

German now reads:

```md
* Parameter $\lambda>0, k>0$, Notation $Weibull(\lambda,k)$
* Dichte $f(x) = \dfrac{k}{\lambda}   {\left(\frac{x}{\lambda}\right)}^{k-1}    e^{-{\left(\frac{x}{\lambda}\right)}^k}$ für $x \geq 0$ \
  und $f(x)=0$ für $x < 0$
* Erwartungswert $\lambda \Gamma(1+\frac{1}{k})$ (wobei $\Gamma(n+1) = n!$)
* Maximale Entropie unter allen Verteilungen mit einer Bedingung an alle Momente: $\mathbb{E}(X^n) = \lambda^n$ und einer Bedingung an $\mathbb{E}(\log X)$.
* Anwendungsbeispiele:
  * Wie lange läuft eine Wärmepumpe, bis sie kaputt geht?
  * Wie hoch ist die Windgeschwindigkeit?
  * Was ist die höchste Niederschlagsmenge an einem einzelnen Tag im Jahr?
```

Current English block c24.1:

```md
* Parameter $\lambda>0, k>0$, Notation $Weibull(\lambda,k)$
* Dichte $f(x) = \dfrac{k}{\lambda}   {\left(\frac{x}{\lambda}\right)}^{k-1}    e^{-{\left(\frac{x}{\lambda}\right)}^k}$ für $x \geq 0$ \
  und $f(x)=0$ für $x < 0$
* Erwartungswert $\lambda \Gamma(1+\frac{1}{k})$ (wobei $\Gamma(n+1) = n!$)
* Varianz $\lambda^2 \left[ \Gamma(1+\frac{2}{k}) - \Gamma(1+\frac{1}{k})^2 \right]$
* Maximale Entropie unter allen Verteilungen mit Träger $[0,\infty)$, festem $\mathbb{E}(X^k)$ und festem $\mathbb{E}(\log X)$ — der Formparameter $k$ sagt also, welches Moment festgehalten wird
* Anwendungsbeispiele:
  * Wie lange läuft eine Wärmepumpe, bis sie kaputt geht?
  * Wie hoch ist die Windgeschwindigkeit?
  * Was ist die höchste Niederschlagsmenge an einem einzelnen Tag im Jahr?
```


## deskriptive-statistik.md → descriptive-statistics.md

### replace – German block `1` – English block(s) **1**

What changed in the German:

```diff
- [Vorlesungsaufzeichnung Deskriptive [-Statistik (VL 9, ab Minute 54)](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167?t=3244) [Vorlesungsaufzeichnung Skalenniveaus und Plots (VL 10, ab Minute 49)](https://media.hhu.de/channel/video/data-science-vl-10-skalenniveaus-2025/9b824315922a75d933e081f31c1da388/167?t=2940) [Vorlesungsaufzeichnung Simpson-Paradoxon (VL 12)](https://media.hhu.de/channel/video/data-science-vl-12-simpsons-und-pandas-2025/5a80e62a517e312ab8bf8f9155b91bf1/167)-]
+ [Vorlesungsaufzeichnung Deskriptive {+Statistik](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167?t=3244)+}
```

German now reads:

```md
[Vorlesungsaufzeichnung Deskriptive Statistik](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167?t=3244)
```

Current English block 1:

```md
[Vorlesungsaufzeichnung Deskriptive Statistik (VL 9, ab Minute 54)](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167?t=3244)
[Vorlesungsaufzeichnung Skalenniveaus und Plots (VL 10, ab Minute 49)](https://media.hhu.de/channel/video/data-science-vl-10-skalenniveaus-2025/9b824315922a75d933e081f31c1da388/167?t=2940)
[Vorlesungsaufzeichnung Simpson-Paradoxon (VL 12)](https://media.hhu.de/channel/video/data-science-vl-12-simpsons-und-pandas-2025/5a80e62a517e312ab8bf8f9155b91bf1/167)
```

### replace – German block `3` – English block(s) **3**

What changed in the German:

```diff
- ```{figure} images/ds-process-oneill.png :width: 480px :align: center :name: ds-process Der "Data Science [-Prozess". Abbildung nach {cite}`dds`, S. 41 (Cathy O'Neil und Rachel Schutt, O'Reilly 2013).-] ```
+ ```{figure} images/ds-process-oneill.png :width: 480px :align: center :name: ds-process Der "Data Science {+Prozess"+} ```
```

German now reads:

```md
```{figure} images/ds-process-oneill.png
:width: 480px
:align: center
:name: ds-process

Der "Data Science Prozess"
```
```

Current English block 3:

```md
```{figure} images/ds-process-oneill.png
:width: 480px
:align: center
:name: ds-process

Der "Data Science Prozess". Abbildung nach {cite}`dds`, S. 41 (Cathy O'Neil und Rachel Schutt, O'Reilly 2013).
```
```

### replace – German block `12` – English block(s) **12**

What changed in the German:

```diff
- Man kann die verschiedenen Kulturen des Modellierens noch etwas feiner aufschlüsseln, wie es C. Molnar in dem Buch [-„Modeling-] Mindsets: The Many Cultures Of Learning From [-Data“-] getan hat {cite}`molnarmindsets`; dazu ist es aber hilfreich, bereits den Maximum-Likelihood-Ansatz und den Satz von Bayes zu kennen.
+ Man kann die verschiedenen Kulturen des Modellierens noch etwas feiner aufschlüsseln, wie es C. Molnar in dem Buch {+``Modeling+} Mindsets: The Many Cultures Of Learning From {+Data''+} getan hat {cite}`molnarmindsets`; dazu ist es aber hilfreich, bereits den Maximum-Likelihood-Ansatz und den Satz von Bayes zu kennen.
```

German now reads:

```md
Man kann die verschiedenen Kulturen des Modellierens noch etwas feiner aufschlüsseln, wie es C. Molnar in dem Buch ``Modeling Mindsets: The Many Cultures Of Learning From Data'' getan hat {cite}`molnarmindsets`; dazu ist es aber hilfreich, bereits den Maximum-Likelihood-Ansatz und den Satz von Bayes zu kennen.
```

Current English block 12:

```md
Man kann die verschiedenen Kulturen des Modellierens noch etwas feiner aufschlüsseln, wie es C. Molnar in dem Buch „Modeling Mindsets: The Many Cultures Of Learning From Data“ getan hat {cite}`molnarmindsets`; dazu ist es aber hilfreich, bereits den Maximum-Likelihood-Ansatz und den Satz von Bayes zu kennen.
```

### replace – German block `42` – English block(s) **42**

What changed in the German:

```diff
- [Für eine kurze lockere Übersicht über einen Teil der Frage [-„Was-] sind eigentlich [-Daten“,-] insb. der Frage der Skalen, gibt es ein Video vom HeiCAD-Programm [-„KI-] für [-Alle“](https://www.youtube.com/watch?v=hJVOudzjnEI).-]
+ [Für eine kurze lockere Übersicht über einen Teil der Frage {+``Was+} sind eigentlich {+Daten'',+} insb. der Frage der Skalen, gibt es ein Video vom HeiCAD-Programm {+``KI+} für {+Alle''](https://www.youtube.com/watch?v=hJVOudzjnEI).+}
```

German now reads:

```md
[Für eine kurze lockere Übersicht über einen Teil der Frage ``Was sind eigentlich Daten'', insb. der Frage der Skalen, gibt es ein Video vom HeiCAD-Programm ``KI für Alle''](https://www.youtube.com/watch?v=hJVOudzjnEI).
```

Current English block 42:

```md
[Für eine kurze lockere Übersicht über einen Teil der Frage „Was sind eigentlich Daten“, insb. der Frage der Skalen, gibt es ein Video vom HeiCAD-Programm „KI für Alle“](https://www.youtube.com/watch?v=hJVOudzjnEI).
```

### replace – German block `74` – English block(s) **74**

What changed in the German:

```diff
- :class: dropdown Über alle Pflanzen hinweg ist der Zusammenhang schwach negativ (Korrelationskoeffizient etwa $-0{,}12$): breitere Kelchblätter gehen mit kürzeren einher. Innerhalb jeder Spezies ist er deutlich positiv (setosa etwa $0{,}74$, versicolor $0{,}53$, virginica $0{,}46$). Die Spezies ist der Confounder: *setosa* hat kurze, breite Kelchblätter, die anderen beiden lange, schmale. Wer die Spezies nicht kennt, sieht einen Trend, der in keiner Gruppe gilt. Wie man die Zahlen berechnet, steht [-in der Bemerkung *Für Daten*-] im Kapitel [Kovarianz](kovarianz.md).
+ :class: dropdown Über alle Pflanzen hinweg ist der Zusammenhang schwach negativ (Korrelationskoeffizient etwa $-0{,}12$): breitere Kelchblätter gehen mit kürzeren einher. Innerhalb jeder Spezies ist er deutlich positiv (setosa etwa $0{,}74$, versicolor $0{,}53$, virginica $0{,}46$). Die Spezies ist der Confounder: *setosa* hat kurze, breite Kelchblätter, die anderen beiden lange, schmale. Wer die Spezies nicht kennt, sieht einen Trend, der in keiner Gruppe gilt. Wie man die Zahlen berechnet, steht im Kapitel [Kovarianz](kovarianz.md).
```

German now reads:

```md
:class: dropdown
Über alle Pflanzen hinweg ist der Zusammenhang schwach negativ (Korrelationskoeffizient etwa $-0{,}12$): breitere Kelchblätter gehen mit kürzeren einher. Innerhalb jeder Spezies ist er deutlich positiv (setosa etwa $0{,}74$, versicolor $0{,}53$, virginica $0{,}46$). Die Spezies ist der Confounder: *setosa* hat kurze, breite Kelchblätter, die anderen beiden lange, schmale. Wer die Spezies nicht kennt, sieht einen Trend, der in keiner Gruppe gilt. Wie man die Zahlen berechnet, steht im Kapitel [Kovarianz](kovarianz.md).
```

Current English block 74:

```md
:class: dropdown
Über alle Pflanzen hinweg ist der Zusammenhang schwach negativ (Korrelationskoeffizient etwa $-0{,}12$): breitere Kelchblätter gehen mit kürzeren einher. Innerhalb jeder Spezies ist er deutlich positiv (setosa etwa $0{,}74$, versicolor $0{,}53$, virginica $0{,}46$). Die Spezies ist der Confounder: *setosa* hat kurze, breite Kelchblätter, die anderen beiden lange, schmale. Wer die Spezies nicht kennt, sieht einen Trend, der in keiner Gruppe gilt. Wie man die Zahlen berechnet, steht in der Bemerkung *Für Daten* im Kapitel [Kovarianz](covariance.md).
```

### replace – German block `77` – English block(s) **77**

German now reads:

```md
Wozu visualisieren?
Ein zweiter Grund, immer zu plotten, ist das Simpson-Paradoxon von oben: Eine Kennzahl über alle Daten kann das Gegenteil von dem sagen, was in jeder Gruppe gilt, und im Plot sieht man die Gruppen.
[Alberto Cairo hat den 'Datasaurus' erfunden](http://www.thefunctionalart.com/2016/08/download-datasaurus-never-trust-summary.html) um auf den Unterschied zwischen zusammenfassender Statistik und Visualisierung hinzuweisen:
```

Current English block 77:

```md
Wozu visualisieren? Der erste Grund: Zusammenfassende Zahlen können lügen, ohne dass man es ihnen ansieht. [Alberto Cairo hat den 'Datasaurus' erfunden](http://www.thefunctionalart.com/2016/08/download-datasaurus-never-trust-summary.html) um auf den Unterschied zwischen zusammenfassender Statistik und Visualisierung hinzuweisen:
```

### replace – German block `80`, `81` – English block(s) **80**, **81**

German now reads:

```md
```{figure} images/AllDinosGrey_1.png
:width: 480px
:align: center
:name: datasaurus-dozen

The Datasaurus Dozen, inspiriert von Anscombe's Quartett.
```
```

Current English block 80:

```md
```{figure} images/AllDinosGrey_1.png
:width: 480px
:align: center
:name: datasaurus-dozen

The Datasaurus Dozen, inspiriert von Anscombe's Quartett. Abbildung: Justin Matejka und George Fitzmaurice, Autodesk Research 2017 {cite}`matejka2017`.
```
```

Current English block 81:

```md
Der zweite Grund, immer zu plotten, ist das Simpson-Paradoxon von oben: Eine Kennzahl über alle Daten kann das Gegenteil von dem sagen, was in jeder Gruppe gilt, und im Plot sieht man die Gruppen.
```

### replace – German block `83` – English block(s) **83**

What changed in the German:

```diff
- * Histogramme
+ * Histogramme {+("historical diagram")+}
```

German now reads:

```md
  * Histogramme ("historical diagram")
```

Current English block 83:

```md
  * Histogramme
```

### replace – German block `95` – English block(s) **95**

What changed in the German:

```diff
- [-Zeigt Median, Quartile und Ausreißer einer Verteilung in einem Bild: Der Kasten reicht von $Q_1$ bis $Q_3$, die „Whiskers“ bis zum letzten Wert innerhalb von $1{,}5$ Interquartilsabständen, alles dahinter wird als einzelner Punkt gezeichnet. In Matplotlib `plt.boxplot(x)`;-] das [-Kapitel [Daten putzen](data-cleaning.ipynb) benutzt dieselbe Regel für Ausreißer.-]
+ {+Werden wir beim Thema Konfidenzintervalle kennen lernen, denn+} das {+(und Quantile) kann man damit gut darstellen.+}
```

German now reads:

```md
    Werden wir beim Thema Konfidenzintervalle kennen lernen, denn das (und Quantile) kann man damit gut darstellen.
```

Current English block 95:

```md
    Zeigt Median, Quartile und Ausreißer einer Verteilung in einem Bild: Der Kasten reicht von $Q_1$ bis $Q_3$, die „Whiskers“ bis zum letzten Wert innerhalb von $1{,}5$ Interquartilsabständen, alles dahinter wird als einzelner Punkt gezeichnet. In Matplotlib `plt.boxplot(x)`; das Kapitel [Daten putzen](data-cleaning.ipynb) benutzt dieselbe Regel für Ausreißer.
```

### replace – German block `97` – English block(s) **97**

What changed in the German:

```diff
- Wenn man eine oder mehrere Funktionsgraphen plottet (so wie wir es mit den PDF getan haben), sind das [-Linienplots.-] Man kann ebenso Daten auf Kardinalskalen mit einem Linienplot darstellen, aber das Verbinden von Punkten suggeriert eine Datenfülle, die nicht unbedingt vorliegt.
+ Wenn man eine oder mehrere Funktionsgraphen plottet (so wie wir es mit den PDF getan haben), sind das {+Lininenplots.+} Man kann ebenso Daten auf Kardinalskalen mit einem Linienplot darstellen, aber das Verbinden von Punkten suggeriert eine Datenfülle, die nicht unbedingt vorliegt.
```

German now reads:

```md
    Wenn man eine oder mehrere Funktionsgraphen plottet (so wie wir es mit den PDF getan haben), sind das Lininenplots. Man kann ebenso Daten auf Kardinalskalen mit einem Linienplot darstellen, aber das Verbinden von Punkten suggeriert eine Datenfülle, die nicht unbedingt vorliegt.
```

Current English block 97:

```md
    Wenn man eine oder mehrere Funktionsgraphen plottet (so wie wir es mit den PDF getan haben), sind das Linienplots. Man kann ebenso Daten auf Kardinalskalen mit einem Linienplot darstellen, aber das Verbinden von Punkten suggeriert eine Datenfülle, die nicht unbedingt vorliegt.
```

### replace – German block `102` – English block(s) **102**

What changed in the German:

```diff
- Generell [-gilt: Wo-] ein Tortendiagramm [-geht, geht-] auch [-ein Balkendiagramm, und das ist lesbarer.-] Tortendiagramme haben daher vor allem einen Wert, wenn man einen Text auflockern will, ohne wesentlich auf die dargestellte Statistik einzugehen. Grundsätzlich geeignet sind nominal- oder ordinalskalierte Merkmale, denn die Torte stellt die Anteile der einzelnen Ausprägungen an einem Ganzen dar — sie ist ein ungewöhnlich gezeichnetes Balkendiagramm.
+ Generell {+hat sich herausgestellt, dass sich immer dann, wenn man+} ein Tortendiagramm {+verwenden kann,+} auch {+einen Barplot machen kann, der lesbarer ist.+} Tortendiagramme haben daher vor allem einen Wert, wenn man einen Text auflockern will, ohne wesentlich auf die dargestellte Statistik einzugehen. Grundsätzlich geeignet sind nominal- oder ordinalskalierte Merkmale, denn die Torte stellt die Anteile der einzelnen Ausprägungen an einem Ganzen dar — sie ist ein ungewöhnlich gezeichnetes Balkendiagramm.
```

German now reads:

```md
    Generell hat sich herausgestellt, dass sich immer dann, wenn man ein Tortendiagramm verwenden kann, auch einen Barplot machen kann, der lesbarer ist. Tortendiagramme haben daher vor allem einen Wert, wenn man einen Text auflockern will, ohne wesentlich auf die dargestellte Statistik einzugehen. Grundsätzlich geeignet sind nominal- oder ordinalskalierte Merkmale, denn die Torte stellt die Anteile der einzelnen Ausprägungen an einem Ganzen dar — sie ist ein ungewöhnlich gezeichnetes Balkendiagramm.
```

Current English block 102:

```md
    Generell gilt: Wo ein Tortendiagramm geht, geht auch ein Balkendiagramm, und das ist lesbarer. Tortendiagramme haben daher vor allem einen Wert, wenn man einen Text auflockern will, ohne wesentlich auf die dargestellte Statistik einzugehen. Grundsätzlich geeignet sind nominal- oder ordinalskalierte Merkmale, denn die Torte stellt die Anteile der einzelnen Ausprägungen an einem Ganzen dar — sie ist ein ungewöhnlich gezeichnetes Balkendiagramm.
```

### replace – German block `135` – English block(s) **135**

German now reads:

```md
    Zweitens die Betrachter\*innen selbst: Etwa jeder zwölfte Mann und jede zweihundertste Frau nimmt Farben anders wahr als die Mehrheit, am häufigsten Rot und Grün. In einer Vorlesung mit zweihundert Zuhörenden sitzen also typischerweise mehrere Menschen, für die eine Rot-Grün-Skala keine Skala ist. Das ist häufig genug, um es zur Gewohnheit zu machen und nicht zur Ausnahme:
```{figure} images/color-blind-friendly-palette-13.jpg
:width: 480px
:align: center
:name: color-friendly

Simulation der Farbwahrnehmung bei verschiedenen Arten der 'Sichtigkeit'
```
```

Current English block 135:

```md
    Zweitens die Betrachter\*innen selbst: Etwa jeder zwölfte Mann und jede zweihundertste Frau nimmt Farben anders wahr als die Mehrheit, am häufigsten Rot und Grün. In einer Vorlesung mit zweihundert Zuhörenden sitzen also typischerweise mehrere Menschen, für die eine Rot-Grün-Skala keine Skala ist. Das ist häufig genug, um es zur Gewohnheit zu machen und nicht zur Ausnahme.
```

### delete – German block `138`, `139`, `140` – English block(s) **138**, **139**, **140**

Current English block 138:

```md
Dass sie funktioniert, kann man nachrechnen: Farbsehschwächen lassen sich als lineare Abbildung im Farbraum simulieren, und angewandt auf die acht Farben oben sieht das so aus.
```

Current English block 139:

```md
```{figure} images/farbwahrnehmung-simulation.png
:width: 560px
:align: center
:name: color-friendly

Dieselbe Palette, simuliert für Normalsicht und die drei Arten der Dichromasie (Verfahren nach Viénot, Brettel und Mollon 1999). Die Farben bleiben in allen vier Feldern unterscheidbar — das ist die Eigenschaft, auf die es ankommt.
```
```

Current English block 140:

```md
Zwei Dinge sieht man daran. Erstens: Die Palette verliert zwar ihre Buntheit, aber keine zwei Felder fallen zusammen — jede Farbe behält eine eigene Helligkeit. Zweitens: Eine Palette, die Rot und Grün gegeneinanderstellt, würde hier zusammenfallen, und genau das passiert bei der verbreiteten Ampel-Kodierung.
```


## explorative-analyse-beispiele.ipynb → eda-examples.ipynb

### replace – German block `c0.0`, `c0.1` – English block(s) **c0.0**, **c0.1**

What changed in the German:

```diff
- # Explorative [-Analyse: Beispiele-]
+ # Explorative {+Datenanalyse+}
- [-[Vorlesungsaufzeichnung Beispiele für EDA](https://media.hhu.de/channel/video/data-science-beispiele-fuer-eda/e31e1c56fa7d6ba40773bacdfac54758/167)-]
+ {+[Aufzeichnung Explorative Datenanalyse](https://media.hhu.de/channel/video/data-science-beispiele-fuer-eda/e31e1c56fa7d6ba40773bacdfac54758/167)+}
```

German now reads:

```md
# Explorative Datenanalyse
[Aufzeichnung Explorative Datenanalyse](https://media.hhu.de/channel/video/data-science-beispiele-fuer-eda/e31e1c56fa7d6ba40773bacdfac54758/167)
```

Current English block c0.0:

```md
# Explorative Analyse: Beispiele
```

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Beispiele für EDA](https://media.hhu.de/channel/video/data-science-beispiele-fuer-eda/e31e1c56fa7d6ba40773bacdfac54758/167)
```

### replace – German block `c2.1`, `c2.2` – English block(s) **c2.1**, **c2.2**

What changed in the German:

```diff
- Den Anfang macht ein alter Datensatz, den man z.B. beim [UC Irvine Machine Learning [-Repository](https://archive.ics.uci.edu/)-] herunterladen kann:
+ Den Anfang macht ein alter Datensatz, den man z.B. beim [UC Irvine Machine Learning {+Repository](https://archive-beta.ics.uci.edu/)+} herunterladen kann:
- [Wine. (1991). UCI Machine Learning [-Repository.](https://archive.ics.uci.edu/dataset/109/wine)-]
+ [Wine. (1991). UCI Machine Learning {+Repository.](https://archive-beta.ics.uci.edu/ml/datasets/wine)+}
```

German now reads:

```md
Den Anfang macht ein alter Datensatz, den man z.B. beim [UC Irvine Machine Learning Repository](https://archive-beta.ics.uci.edu/) herunterladen kann:
[Wine. (1991). UCI Machine Learning Repository.](https://archive-beta.ics.uci.edu/ml/datasets/wine)
```

Current English block c2.1:

```md
Den Anfang macht ein alter Datensatz, den man z.B. beim [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/) herunterladen kann:
```

Current English block c2.2:

```md
[Wine. (1991). UCI Machine Learning Repository.](https://archive.ics.uci.edu/dataset/109/wine)
```

### replace – German block `c23.1` – English block(s) **c23.1**

What changed in the German:

```diff
- Wünschenswert wäre natürlich ein Koordinaten-unabhängiges Verfahren, die Klassen zu trennen (sodass wir also nicht von Hand 2 Variablen auswählen müssen). Das wird uns später mit der [-Hauptachsentransformation-] (principal component analysis, PCA) möglich sein.
+ Wünschenswert wäre natürlich ein Koordinaten-unabhängiges Verfahren, die Klassen zu trennen (sodass wir also nicht von Hand 2 Variablen auswählen müssen). Das wird uns später mit der {+Hauptachsentranformation+} (principal component analysis, PCA) möglich sein.
```

German now reads:

```md
Wünschenswert wäre natürlich ein Koordinaten-unabhängiges Verfahren, die Klassen zu trennen (sodass wir also nicht von Hand 2 Variablen auswählen müssen). Das wird uns später mit der Hauptachsentranformation (principal component analysis, PCA) möglich sein.
```

Current English block c23.1:

```md
Wünschenswert wäre natürlich ein Koordinaten-unabhängiges Verfahren, die Klassen zu trennen (sodass wir also nicht von Hand 2 Variablen auswählen müssen). Das wird uns später mit der Hauptachsentransformation (principal component analysis, PCA) möglich sein.
```

### replace – German block `c35.0` – English block(s) **c35.0**

What changed in the German:

```diff
- Man kann fast Deutschland erkennen, vor allem aber, dass die y-Achse skaliert werden sollte. Wir informieren uns also über die Skalierung des RADKLIM-Gitters und erfahren, dass jeder Gitterpunkt genau [-$1 \times 1\,\mathrm{km}^2$-] entspricht. Also muss der Plot nur quadratisch sein. Damit wir etwas mehr von der Verteilung sehen können, machen wir noch jeden Punkt teiltransparent. So werden große Anhäufungen sichtbar:
+ Man kann fast Deutschland erkennen, vor allem aber, dass die y-Achse skaliert werden sollte. Wir informieren uns also über die Skalierung des RADKLIM-Gitters und erfahren, dass jeder Gitterpunkt genau {+$1\times 1 km^2$+} entspricht. Also muss der Plot nur quadratisch sein. Damit wir etwas mehr von der Verteilung sehen können, machen wir noch jeden Punkt teiltransparent. So werden große Anhäufungen sichtbar:
```

German now reads:

```md
Man kann fast Deutschland erkennen, vor allem aber, dass die y-Achse skaliert werden sollte. Wir informieren uns also über die Skalierung des RADKLIM-Gitters und erfahren, dass jeder Gitterpunkt genau $1\times 1 km^2$ entspricht.
Also muss der Plot nur quadratisch sein.
Damit wir etwas mehr von der Verteilung sehen können, machen wir noch jeden Punkt teiltransparent. So werden große Anhäufungen sichtbar:
```

Current English block c35.0:

```md
Man kann fast Deutschland erkennen, vor allem aber, dass die y-Achse skaliert werden sollte. Wir informieren uns also über die Skalierung des RADKLIM-Gitters und erfahren, dass jeder Gitterpunkt genau $1 \times 1\,\mathrm{km}^2$ entspricht.
Also muss der Plot nur quadratisch sein.
Damit wir etwas mehr von der Verteilung sehen können, machen wir noch jeden Punkt teiltransparent. So werden große Anhäufungen sichtbar:
```

### replace – German block `c50` – English block(s) **c50**

What changed in the German:

```diff
- # Wir überspringen die erste Zeile und tun so, # als würde der Name aus zwei Spalten bestehen. data = np.genfromtxt("titanic.csv", delimiter=",", skip_header=1, [-usecols=(1,2,5,6,7,8),-] dtype="i8,i8,S10,i8,i8,i8", names=("Survived","Pclass","Sex", "Age","SibSp","Parch")) data[:4]
+ # Wir überspringen die erste Zeile und tun so, # als würde der Name aus zwei Spalten bestehen. data = np.genfromtxt("titanic.csv", delimiter=",", skip_header=1, {+usecols=(1,2,5,6,7,8,9),+} dtype="i8,i8,S10,i8,i8,i8", names=("Survived","Pclass","Sex", "Age","SibSp","Parch")) data[:4]
```

German now reads:

```md
# Wir überspringen die erste Zeile und tun so,
#   als würde der Name aus zwei Spalten bestehen.
data = np.genfromtxt("titanic.csv",
                     delimiter=",", skip_header=1,
                     usecols=(1,2,5,6,7,8,9),
                     dtype="i8,i8,S10,i8,i8,i8",
                     names=("Survived","Pclass","Sex",
                            "Age","SibSp","Parch"))
data[:4]
```

Current English block c50:

```md
# Wir überspringen die erste Zeile und tun so,
#   als würde der Name aus zwei Spalten bestehen.
data = np.genfromtxt("titanic.csv",
                     delimiter=",", skip_header=1,
                     usecols=(1,2,5,6,7,8),
                     dtype="i8,i8,S10,i8,i8,i8",
                     names=("Survived","Pclass","Sex",
                            "Age","SibSp","Parch"))
data[:4]
```

### replace – German block `c66.0` – English block(s) **c66.0**

What changed in the German:

```diff
- [-Der zweite Rückgabewert-] `pvalue` [-ist ein *p-Wert*:-] die Wahrscheinlichkeit, [-bei-] zwei [-tatsächlich unkorrelierten-] Variablen [-einen Korrelationskoeffizienten zu sehen, der mindestens so weit von $0$ entfernt liegt wie unser $r$. Hier-] ist [-er $0{,}92$, ein solches-] $r$ [-wäre bei unkorrelierten Daten also ganz gewöhnlich: Die Stichprobe kann die winzige Abweichung von $0$ nicht von einem Stichprobenfehler unterscheiden. Mehr sagt der p-Wert nicht, insbesondere nicht, wie wahrscheinlich es ist, dass Geschlecht und Alter unkorreliert *sind*. Was ein p-Wert ist und was nicht, klärt das Kapitel [Statistische Tests](statistische-tests.md).-]
+ {+Laut Dokumentation von Scipy Stats ist diese+} `pvalue` die Wahrscheinlichkeit, {+dass+} zwei {+unkorrelierte+} Variablen {+den Pearson-Korrelationskoeffizient $r$ haben. In unserem Fall+} ist {+also die Erklärung, dass die Daten unkorreliert sind, sehr plausibel. Zudem ist+} $r$ {+sehr klein, sodass eine vermutete Korrelation ebenfalls sehr klein dürfte.+}
```

German now reads:

```md
Laut Dokumentation von Scipy Stats ist diese `pvalue` die Wahrscheinlichkeit, dass zwei unkorrelierte Variablen den Pearson-Korrelationskoeffizient $r$ haben. In unserem Fall ist also die Erklärung, dass die Daten unkorreliert sind, sehr plausibel. Zudem ist $r$ sehr klein, sodass eine vermutete Korrelation ebenfalls sehr klein dürfte.
```

Current English block c66.0:

```md
Der zweite Rückgabewert `pvalue` ist ein *p-Wert*: die Wahrscheinlichkeit, bei zwei tatsächlich unkorrelierten Variablen einen Korrelationskoeffizienten zu sehen, der mindestens so weit von $0$ entfernt liegt wie unser $r$. Hier ist er $0{,}92$, ein solches $r$ wäre bei unkorrelierten Daten also ganz gewöhnlich: Die Stichprobe kann die winzige Abweichung von $0$ nicht von einem Stichprobenfehler unterscheiden. Mehr sagt der p-Wert nicht, insbesondere nicht, wie wahrscheinlich es ist, dass Geschlecht und Alter unkorreliert *sind*. Was ein p-Wert ist und was nicht, klärt das Kapitel [Statistische Tests](statistical-tests.md).
```


## pandas.ipynb → pandas.ipynb

### replace – German block `c0.1` – English block(s) **c0.1**

What changed in the German:

```diff
- [Vorlesungsaufzeichnung [-Pandas (VL 12, ab Minute 62)](https://media.hhu.de/channel/video/data-science-vl-12-simpsons-und-pandas-2025/5a80e62a517e312ab8bf8f9155b91bf1/167?t=3720)-]
+ [Vorlesungsaufzeichnung {+Daten putzen](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167?t=3244)+}
```

German now reads:

```md
[Vorlesungsaufzeichnung Daten putzen](https://media.hhu.de/channel/video/data-science-vl-9-stetige-verteilungen-2025/39016f5414ef3b8edd0dff941f802314/167?t=3244)
```

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Pandas (VL 12, ab Minute 62)](https://media.hhu.de/channel/video/data-science-vl-12-simpsons-und-pandas-2025/5a80e62a517e312ab8bf8f9155b91bf1/167?t=3720)
```

### replace – German block `c52.0`, `c52.1` – English block(s) **c52.0**, **c52.1**

What changed in the German:

```diff
- Fehlende Werte erkennt man mit `isna`. Man kann sie verwerfen (`dropna`) oder ersetzen (`fillna`), zum Beispiel durch den Median. [-Wie man fehlende Werte, Ausreißer, Textfelder-] und [-Datumsangaben systematisch behandelt, ist Thema des Kapitels [Daten putzen](data-cleaning.ipynb).-]
+ Fehlende Werte erkennt man mit `isna`. Man kann sie verwerfen (`dropna`) oder ersetzen (`fillna`), zum Beispiel durch den Median. {+Schiefe+} und {+Wölbung aus dem Kapitel über Erwartungswerte sind ebenfalls eingebaut; `kurt` liefert die Exzess-Kurtosis, also die Wölbung minus $3$:+}
- [-Schiefe-] und [-Wölbung aus dem Kapitel über Erwartungswerte sind ebenfalls eingebaut; `kurt` liefert die Exzess-Kurtosis, also die Wölbung minus $3$:-]
+ {+Wie man fehlende Werte, Ausreißer, Textfelder+} und {+Datumsangaben systematisch behandelt, ist Thema des Kapitels [Daten putzen](data-cleaning.ipynb).+}
```

German now reads:

```md
Fehlende Werte erkennt man mit `isna`. Man kann sie verwerfen (`dropna`) oder ersetzen (`fillna`), zum Beispiel durch den Median. Schiefe und Wölbung aus dem Kapitel über Erwartungswerte sind ebenfalls eingebaut; `kurt` liefert die Exzess-Kurtosis, also die Wölbung minus $3$:
Wie man fehlende Werte, Ausreißer, Textfelder und Datumsangaben systematisch behandelt, ist Thema des Kapitels [Daten putzen](data-cleaning.ipynb).
```

Current English block c52.0:

```md
Fehlende Werte erkennt man mit `isna`. Man kann sie verwerfen (`dropna`) oder ersetzen (`fillna`), zum Beispiel durch den Median. Wie man fehlende Werte, Ausreißer, Textfelder und Datumsangaben systematisch behandelt, ist Thema des Kapitels [Daten putzen](data-cleaning.ipynb).
```

Current English block c52.1:

```md
Schiefe und Wölbung aus dem Kapitel über Erwartungswerte sind ebenfalls eingebaut; `kurt` liefert die Exzess-Kurtosis, also die Wölbung minus $3$:
```


## data-cleaning.ipynb → data-cleaning.ipynb

### replace – German block `c2` – English block(s) **c2**

What changed in the German:

```diff
- import numpy as np import pandas as pd import matplotlib.pyplot as plt import zipfile, urllib.request, pathlib [-basis-] = [-"https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/" station-] = [-"01078" # Düsseldorf ordner = pathlib.Path(basis.replace("https://",-] "")) # lokale Kopie, gleicher Pfad wie im Netz [-# Der Dateiname enthält das Enddatum und ändert sich jedes Jahr, sobald der DWD ein weiteres # Jahr anhängt. Deshalb suchen wir ihn: erst lokal, sonst im Verzeichnislisting des Servers. lokal = sorted(ordner.glob(f"tageswerte_KL_{station}_*_hist.zip"))-] if [-lokal: pfad = lokal[-1] else: import re listing = urllib.request.urlopen(basis).read().decode("utf-8") dateiname = re.search(rf"tageswerte_KL_{station}_\d{{8}}_\d{{8}}_hist\.zip", listing).group(0) pfad = ordner / dateiname ordner.mkdir(parents=True,-] exist_ok=True) [-urllib.request.urlretrieve(basis + pfad.name,-] pfad) with zipfile.ZipFile(pfad) as archiv: datendatei = [name for name in archiv.namelist() if name.startswith("produkt_klima_tag")][0] roh = pd.read_csv(archiv.open(datendatei), sep=";", skipinitialspace=True, na_values=-999) roh.columns = roh.columns.str.strip() # Spaltennamen haben führende Leerzeichen roh = roh.drop(columns="eor") # "end of record", inhaltsleer print(roh.shape) roh.tail(3)
+ import numpy as np import pandas as pd import matplotlib.pyplot as plt import zipfile, urllib.request, pathlib {+url+} = {+("https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/" "tageswerte_KL_01078_19520101_20251231_hist.zip") pfad+} = {+pathlib.Path(url.replace("https://",+} "")) # lokale Kopie, gleicher Pfad wie im Netz if {+not pfad.exists(): pfad.parent.mkdir(parents=True,+} exist_ok=True) {+urllib.request.urlretrieve(url,+} pfad) with zipfile.ZipFile(pfad) as archiv: datendatei = [name for name in archiv.namelist() if name.startswith("produkt_klima_tag")][0] roh = pd.read_csv(archiv.open(datendatei), sep=";", skipinitialspace=True, na_values=-999) roh.columns = roh.columns.str.strip() # Spaltennamen haben führende Leerzeichen roh = roh.drop(columns="eor") # "end of record", inhaltsleer print(roh.shape) roh.tail(3)
```

German now reads:

```md
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile, urllib.request, pathlib

url = ("https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"
       "tageswerte_KL_01078_19520101_20251231_hist.zip")
pfad = pathlib.Path(url.replace("https://", ""))     # lokale Kopie, gleicher Pfad wie im Netz
if not pfad.exists():
    pfad.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, pfad)

with zipfile.ZipFile(pfad) as archiv:
    datendatei = [name for name in archiv.namelist() if name.startswith("produkt_klima_tag")][0]
    roh = pd.read_csv(archiv.open(datendatei), sep=";", skipinitialspace=True, na_values=-999)

roh.columns = roh.columns.str.strip()                   # Spaltennamen haben führende Leerzeichen
roh = roh.drop(columns="eor")                           # "end of record", inhaltsleer
print(roh.shape)
roh.tail(3)
```

Current English block c2:

```md
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import zipfile, urllib.request, pathlib

basis = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"
station = "01078"                                     # Düsseldorf
ordner = pathlib.Path(basis.replace("https://", ""))  # lokale Kopie, gleicher Pfad wie im Netz

# Der Dateiname enthält das Enddatum und ändert sich jedes Jahr, sobald der DWD ein weiteres
# Jahr anhängt. Deshalb suchen wir ihn: erst lokal, sonst im Verzeichnislisting des Servers.
lokal = sorted(ordner.glob(f"tageswerte_KL_{station}_*_hist.zip"))
if lokal:
    pfad = lokal[-1]
else:
    import re
    listing = urllib.request.urlopen(basis).read().decode("utf-8")
    dateiname = re.search(rf"tageswerte_KL_{station}_\d{{8}}_\d{{8}}_hist\.zip", listing).group(0)
    pfad = ordner / dateiname
    ordner.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(basis + pfad.name, pfad)

with zipfile.ZipFile(pfad) as archiv:
    datendatei = [name for name in archiv.namelist() if name.startswith("produkt_klima_tag")][0]
    roh = pd.read_csv(archiv.open(datendatei), sep=";", skipinitialspace=True, na_values=-999)

roh.columns = roh.columns.str.strip()                   # Spaltennamen haben führende Leerzeichen
roh = roh.drop(columns="eor")                           # "end of record", inhaltsleer
print(roh.shape)
roh.tail(3)
```


## kovarianz.md → covariance.md

### replace – German block `1` – English block(s) **1**

What changed in the German:

```diff
- [-[Vorlesungsaufzeichnung Kovarianz und Korrelation (VL 11)](https://media.hhu.de/channel/video/data-science-vl-11-kovarianz-korrelation-2025/92283e63495a6413e5e1b55a17ed31fb/167)-]
+ {+[Vortragsaufzeichnung Kovarianz, Korrelation](https://media.hhu.de/channel/video/data-science-vl-11-kovarianz-korrelation-2025/92283e63495a6413e5e1b55a17ed31fb/167)+}
```

German now reads:

```md
[Vortragsaufzeichnung Kovarianz, Korrelation](https://media.hhu.de/channel/video/data-science-vl-11-kovarianz-korrelation-2025/92283e63495a6413e5e1b55a17ed31fb/167)
```

Current English block 1:

```md
[Vorlesungsaufzeichnung Kovarianz und Korrelation (VL 11)](https://media.hhu.de/channel/video/data-science-vl-11-kovarianz-korrelation-2025/92283e63495a6413e5e1b55a17ed31fb/167)
```

### replace – German block `13` – English block(s) **13**

What changed in the German:

```diff
- Zu einer Zufallsvariable $X \colon \Omega \to \mathbb{R}^n$ können wir $X = (X_1,\dots,X_n)$ schreiben mit $X_i \colon \Omega \to \mathbb{R}$ gegeben als $\pi_i \circ X$, wobei $\pi_i \colon \mathbb{R}^n \to \mathbb{R}$ die $i$-te Koordinatenprojektion ist. Die [-Verteilungen der-] $X_i$ heißen **Randverteilungen** oder [-**Marginalverteilungen** von $X$.-]
+ Zu einer Zufallsvariable $X \colon \Omega \to \mathbb{R}^n$ können wir $X = (X_1,\dots,X_n)$ schreiben mit $X_i \colon \Omega \to \mathbb{R}$ gegeben als $\pi_i \circ X$, wobei $\pi_i \colon \mathbb{R}^n \to \mathbb{R}$ die $i$-te Koordinatenprojektion ist. Die {+Zufallsvariablen+} $X_i$ heißen **Randverteilungen** oder {+**Marginalverteilungen**.+}
```

German now reads:

```md
Zu einer Zufallsvariable $X \colon \Omega \to \mathbb{R}^n$ können wir $X = (X_1,\dots,X_n)$ schreiben mit $X_i \colon \Omega \to \mathbb{R}$ gegeben als $\pi_i \circ X$, wobei $\pi_i \colon \mathbb{R}^n \to \mathbb{R}$ die $i$-te Koordinatenprojektion ist.
Die Zufallsvariablen $X_i$ heißen **Randverteilungen** oder **Marginalverteilungen**.
```

Current English block 13:

```md
Zu einer Zufallsvariable $X \colon \Omega \to \mathbb{R}^n$ können wir $X = (X_1,\dots,X_n)$ schreiben mit $X_i \colon \Omega \to \mathbb{R}$ gegeben als $\pi_i \circ X$, wobei $\pi_i \colon \mathbb{R}^n \to \mathbb{R}$ die $i$-te Koordinatenprojektion ist.
Die Verteilungen der $X_i$ heißen **Randverteilungen** oder **Marginalverteilungen** von $X$.
```

### replace – German block `18` – English block(s) **18**

What changed in the German:

```diff
- Zu einer Zufallsvariable $(X,Y) \colon \Omega \to \mathbb{R}^2$ können wir die Verteilung von $Y$ berechnen als $P(Y \in A) = \sum_{x \in X(\Omega)} P((X,Y) \in \{x\} \times A)$ im diskreten Fall (und mit einem entsprechenden Integral im stetigen Fall), wobei wir [-$\pi_2^{-1}(A)-] = X(\Omega)\times A$ in disjunkte Teilmengen zerlegt haben.
+ Zu einer Zufallsvariable $(X,Y) \colon \Omega \to \mathbb{R}^2$ können wir die Verteilung von $Y$ berechnen als $P(Y \in A) = \sum_{x \in X(\Omega)} P((X,Y) \in \{x\} \times A)$ im diskreten Fall (und mit einem entsprechenden Integral im stetigen Fall), wobei wir {+$\pi_1^{-1}(A)+} = X(\Omega)\times A$ in disjunkte Teilmengen zerlegt haben.
```

German now reads:

```md
Zu einer Zufallsvariable $(X,Y) \colon \Omega \to \mathbb{R}^2$ können wir die Verteilung von $Y$ berechnen als
$P(Y \in A) = \sum_{x \in X(\Omega)} P((X,Y) \in \{x\} \times A)$ im diskreten Fall (und mit einem entsprechenden Integral im stetigen Fall), wobei wir $\pi_1^{-1}(A) = X(\Omega)\times A$ in disjunkte Teilmengen zerlegt haben.
```

Current English block 18:

```md
Zu einer Zufallsvariable $(X,Y) \colon \Omega \to \mathbb{R}^2$ können wir die Verteilung von $Y$ berechnen als
$P(Y \in A) = \sum_{x \in X(\Omega)} P((X,Y) \in \{x\} \times A)$ im diskreten Fall (und mit einem entsprechenden Integral im stetigen Fall), wobei wir $\pi_2^{-1}(A) = X(\Omega)\times A$ in disjunkte Teilmengen zerlegt haben.
```

### replace – German block `47` – English block(s) **47**

What changed in the German:

```diff
- $P(A|B)$ ist eben nicht $P(B|A)$, sondern $P(B|A)$ *mal* das Verhältnis $P(A)/P(B)$, und $P(B)$ wird von der großen Gruppe der Gesunden dominiert. Wer die beiden bedingten Wahrscheinlichkeiten verwechselt, begeht den *Basisratenfehler* — der ist so häufig, dass er einen eigenen Namen hat. Bei der Titanic-Regel „Frauen überleben“ lagen Recall $0{,}68$ und Precision $0{,}74$ nahe beieinander, weil Überlebende und Frauen ähnlich häufig sind; hier liegt zwischen $0{,}99$ und $0{,}09$ eine Basisrate von einem Promille. (Woher der Nenner kommt, klärt der [-Satz von der totalen Wahrscheinlichkeit unten.)-]
+ $P(A|B)$ ist eben nicht $P(B|A)$, sondern $P(B|A)$ *mal* das Verhältnis $P(A)/P(B)$, und $P(B)$ wird von der großen Gruppe der Gesunden dominiert. Wer die beiden bedingten Wahrscheinlichkeiten verwechselt, begeht den *Basisratenfehler* — der ist so häufig, dass er einen eigenen Namen hat. Bei der Titanic-Regel „Frauen überleben“ lagen Recall $0{,}68$ und Precision $0{,}74$ nahe beieinander, weil Überlebende und Frauen ähnlich häufig sind; hier liegt zwischen $0{,}99$ und $0{,}09$ eine Basisrate von einem Promille. (Woher der Nenner kommt, klärt der {+nächste Satz.)+}
```

German now reads:

```md
$P(A|B)$ ist eben nicht $P(B|A)$, sondern $P(B|A)$ *mal* das Verhältnis $P(A)/P(B)$, und $P(B)$ wird von der großen Gruppe der Gesunden dominiert. Wer die beiden bedingten Wahrscheinlichkeiten verwechselt, begeht den *Basisratenfehler* — der ist so häufig, dass er einen eigenen Namen hat. Bei der Titanic-Regel „Frauen überleben“ lagen Recall $0{,}68$ und Precision $0{,}74$ nahe beieinander, weil Überlebende und Frauen ähnlich häufig sind; hier liegt zwischen $0{,}99$ und $0{,}09$ eine Basisrate von einem Promille. (Woher der Nenner kommt, klärt der nächste Satz.)
```

Current English block 47:

```md
$P(A|B)$ ist eben nicht $P(B|A)$, sondern $P(B|A)$ *mal* das Verhältnis $P(A)/P(B)$, und $P(B)$ wird von der großen Gruppe der Gesunden dominiert. Wer die beiden bedingten Wahrscheinlichkeiten verwechselt, begeht den *Basisratenfehler* — der ist so häufig, dass er einen eigenen Namen hat. Bei der Titanic-Regel „Frauen überleben“ lagen Recall $0{,}68$ und Precision $0{,}74$ nahe beieinander, weil Überlebende und Frauen ähnlich häufig sind; hier liegt zwischen $0{,}99$ und $0{,}09$ eine Basisrate von einem Promille. (Woher der Nenner kommt, klärt der Satz von der totalen Wahrscheinlichkeit unten.)
```

### replace – German block `79` – English block(s) **79**

What changed in the German:

```diff
- $$ \text{Posterior} = \dfrac{ \text{Likelihood} [-\cdot-] \text{Prior} }{ \text{Evidenz} }. $$
+ $$ \text{Posterior} = \dfrac{ \text{Likelihood} {+*+} \text{Prior} }{ \text{Evidenz} }. $$
```

German now reads:

```md
$$
\text{Posterior} = \dfrac{ \text{Likelihood} * \text{Prior} }{ \text{Evidenz} }.
$$
```

Current English block 79:

```md
$$
\text{Posterior} = \dfrac{ \text{Likelihood} \cdot \text{Prior} }{ \text{Evidenz} }.
$$
```

### replace – German block `90` – English block(s) **90**

What changed in the German:

```diff
- $$ \operatorname{Cov}(X,Y) := \mathbb{E}\left( \left( X - \mathbb{E}X \right) \left( Y - \mathbb{E}Y \right) [-\right).-] $$
+ $$ \operatorname{Cov}(X,Y) := \mathbb{E}\left( \left( X - \mathbb{E}X \right) \left( Y - \mathbb{E}Y \right) {+\right),+} $$
```

German now reads:

```md
$$
\operatorname{Cov}(X,Y) := \mathbb{E}\left( \left( X - \mathbb{E}X \right) \left( Y - \mathbb{E}Y \right) \right),
$$
```

Current English block 90:

```md
$$
\operatorname{Cov}(X,Y) := \mathbb{E}\left( \left( X - \mathbb{E}X \right) \left( Y - \mathbb{E}Y \right) \right).
$$
```

### replace – German block `92` – English block(s) **92**

What changed in the German:

```diff
- [-Insbesondere ist-] $\mathbb{V}(X) = \operatorname{Cov}(X,X)$.
+ {+also auch+} $\mathbb{V}(X) = \operatorname{Cov}(X,X)$.
```

German now reads:

```md
also auch $\mathbb{V}(X) = \operatorname{Cov}(X,X)$.
```

Current English block 92:

```md
Insbesondere ist $\mathbb{V}(X) = \operatorname{Cov}(X,X)$.
```

### delete – German block `99`, `100`, `101`, `102`, `103`, `104` – English block(s) **99**, **100**, **101**, **102**, **103**, **104**

Current English block 99:

```md
:::
```

Current English block 100:

```md
:::{admonition} Bemerkung
```

Current English block 101:

```md
**Für Daten.** Liegen $x, y \in \mathbb{R}^n$ als zwei Spalten einer Tabelle vor, so ersetzt man in den Definitionen den Erwartungswert durch den Mittelwert und erhält die *empirische Kovarianz* und den *empirischen Korrelationskoeffizienten*
```

Current English block 102:

```md
$$
\operatorname{Cov}(x,y) := \frac{1}{n} \sum_{i=1}^n (x_i - \bar x)(y_i - \bar y) = \frac{1}{n}\, \tilde x \cdot \tilde y, \qquad r := \frac{\operatorname{Cov}(x,y)}{\sigma(x)\,\sigma(y)} = \frac{\tilde x \cdot \tilde y}{\lVert \tilde x \rVert \, \lVert \tilde y \rVert},
$$
```

Current English block 103:

```md
mit den zentrierten Vektoren $\tilde x, \tilde y$ aus dem Kapitel [Erwartungswert und Varianz](expectation-variance.md). Der Korrelationskoeffizient von Daten ist also wörtlich der Kosinus des Winkels zwischen den zentrierten Spalten. Das ist die Zahl, die `np.corrcoef(x, y)[0, 1]` im Kapitel [Titanic EDA](titanic-eda-numpy.ipynb) ausgibt; `np.cov(x, y, ddof=0)` liefert die Kovarianzmatrix in der $n$-Version (ohne `ddof=0` teilt Numpy hier, anders als bei `np.var`, durch $n-1$). Für die Iris-Aufgabe aus dem Kapitel [Deskriptive Statistik](descriptive-statistics.md) rechnet man einmal über alle Zeilen und einmal je Spezies:
```

Current English block 104:

```md
```python
x = datasets.load_iris().data; y = datasets.load_iris().target
print(np.corrcoef(x[:, 0], x[:, 1])[0, 1])                          # -0.118
for s in range(3):
    print(s, np.corrcoef(x[y == s, 0], x[y == s, 1])[0, 1])         # 0.743, 0.526, 0.457
```
```

### replace – German block `135` – English block(s) **135**

What changed in the German:

```diff
- Damit verhält sich die Kovarianz wie ein Skalarprodukt — allerdings nur „modulo Konstanten“, denn konstante Zufallsvariablen haben Kovarianz $0$ mit allem, auch mit sich selbst. Man kann das rigoros machen, und die Kovarianz als Skalarprodukt in einem $\mathcal{L}^2$-Raum von Zufallsvariablen auffassen, in dem man zwei Zufallsvariablen identifiziert, die sich nur um eine Konstante unterscheiden. Der Korrelationskoeffizient spielt dann die Rolle des Kosinus des Winkels zwischen zwei Zufallsvariablen. [-Für Daten-] ist es [-wörtlich so (siehe die Bemerkung *Für Daten* oben); die-] im maschinellen Lernen [-verbreitete-] 'cosine similarity' [-ist derselbe Kosinus, nur ohne das Zentrieren.-]
+ Damit verhält sich die Kovarianz wie ein Skalarprodukt — allerdings nur „modulo Konstanten“, denn konstante Zufallsvariablen haben Kovarianz $0$ mit allem, auch mit sich selbst. Man kann das rigoros machen, und die Kovarianz als Skalarprodukt in einem $\mathcal{L}^2$-Raum von Zufallsvariablen auffassen, in dem man zwei Zufallsvariablen identifiziert, die sich nur um eine Konstante unterscheiden. Der Korrelationskoeffizient spielt dann die Rolle des Kosinus des Winkels zwischen zwei Zufallsvariablen. {+Im diskreten Fall+} ist es {+genau das, weshalb+} im maschinellen Lernen {+oft auch+} 'cosine similarity' {+als Maß für die Korrelation angegeben wird.+}
```

German now reads:

```md
Damit verhält sich die Kovarianz wie ein Skalarprodukt — allerdings nur „modulo Konstanten“, denn konstante Zufallsvariablen haben Kovarianz $0$ mit allem, auch mit sich selbst. Man kann das rigoros machen, und die Kovarianz als Skalarprodukt in einem $\mathcal{L}^2$-Raum von Zufallsvariablen auffassen, in dem man zwei Zufallsvariablen identifiziert, die sich nur um eine Konstante unterscheiden. Der Korrelationskoeffizient spielt dann die Rolle des Kosinus des Winkels zwischen zwei Zufallsvariablen. Im diskreten Fall ist es genau das, weshalb im maschinellen Lernen oft auch 'cosine similarity' als Maß für die Korrelation angegeben wird.
```

Current English block 135:

```md
Damit verhält sich die Kovarianz wie ein Skalarprodukt — allerdings nur „modulo Konstanten“, denn konstante Zufallsvariablen haben Kovarianz $0$ mit allem, auch mit sich selbst. Man kann das rigoros machen, und die Kovarianz als Skalarprodukt in einem $\mathcal{L}^2$-Raum von Zufallsvariablen auffassen, in dem man zwei Zufallsvariablen identifiziert, die sich nur um eine Konstante unterscheiden. Der Korrelationskoeffizient spielt dann die Rolle des Kosinus des Winkels zwischen zwei Zufallsvariablen. Für Daten ist es wörtlich so (siehe die Bemerkung *Für Daten* oben); die im maschinellen Lernen verbreitete 'cosine similarity' ist derselbe Kosinus, nur ohne das Zentrieren.
```


## multivariate-normalverteilung.ipynb → multivariate-normal.ipynb

### replace – German block `c0.1` – English block(s) **c0.1**

What changed in the German:

```diff
- [-[Vorlesungsaufzeichnung Multivariate Normalverteilung (VL 13)](https://media.hhu.de/channel/video/data-science-vl-13-multivariate-normalverteilung-2025/caa8a4203ac6ef5db3cd928ecad06918/167)-]
+ {+[Vortragsaufzeichnung zur multivariaten Normalverteilung](https://media.hhu.de/channel/video/data-science-vl-13-multivariate-normalverteilung-2025/caa8a4203ac6ef5db3cd928ecad06918/167)+}
```

German now reads:

```md
[Vortragsaufzeichnung zur multivariaten Normalverteilung](https://media.hhu.de/channel/video/data-science-vl-13-multivariate-normalverteilung-2025/caa8a4203ac6ef5db3cd928ecad06918/167)
```

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Multivariate Normalverteilung (VL 13)](https://media.hhu.de/channel/video/data-science-vl-13-multivariate-normalverteilung-2025/caa8a4203ac6ef5db3cd928ecad06918/167)
```

### replace – German block `c1.2` – English block(s) **c1.2**

What changed in the German:

```diff
- Wenn wir das auf zwei Dimensionen verallgemeinern wollen, also eine Zufallsvariable $(X,Y)$ mit Werten in $\mathbb{R}^2$, dann ist $P(X < c, Y < d) = \int_{-\infty}^c \int_{-\infty}^d [-f(x,y)\,dy\,dx$.-]
+ Wenn wir das auf zwei Dimensionen verallgemeinern wollen, also eine Zufallsvariable $(X,Y)$ mit Werten in $\mathbb{R}^2$, dann ist $P(X < c, Y < d) = \int_{-\infty}^c \int_{-\infty}^d {+f(x,y)dx dy$.+}
```

German now reads:

```md
Wenn wir das auf zwei Dimensionen verallgemeinern wollen, also eine Zufallsvariable $(X,Y)$ mit Werten in $\mathbb{R}^2$, dann ist $P(X < c, Y < d) = \int_{-\infty}^c \int_{-\infty}^d f(x,y)dx dy$.
```

Current English block c1.2:

```md
Wenn wir das auf zwei Dimensionen verallgemeinern wollen, also eine Zufallsvariable $(X,Y)$ mit Werten in $\mathbb{R}^2$, dann ist $P(X < c, Y < d) = \int_{-\infty}^c \int_{-\infty}^d f(x,y)\,dy\,dx$.
```

### replace – German block `c7.4` – English block(s) **c7.4**

What changed in the German:

```diff
- $$ \phi(x) = \dfrac{1}{\sqrt{(2\pi)^{n}\det(\Sigma)}} [-\exp\left(-] -\dfrac{ (x-\mu)^T \Sigma^{-1}(x-\mu) }{ 2 } \right) $$
+ $$ \phi(x) = \dfrac{1}{\sqrt{(2\pi)^{n}\det(\Sigma)}} {+exp\left(+} -\dfrac{ (x-\mu)^T \Sigma^{-1}(x-\mu) }{ 2 } \right) $$
```

German now reads:

```md
$$
\phi(x) = \dfrac{1}{\sqrt{(2\pi)^{n}\det(\Sigma)}} exp\left( -\dfrac{ (x-\mu)^T \Sigma^{-1}(x-\mu) }{ 2 } \right)
$$
```

Current English block c7.4:

```md
$$
\phi(x) = \dfrac{1}{\sqrt{(2\pi)^{n}\det(\Sigma)}} \exp\left( -\dfrac{ (x-\mu)^T \Sigma^{-1}(x-\mu) }{ 2 } \right)
$$
```

### replace – German block `c14.6` – English block(s) **c14.6**

German now reads:

```md
Man kann die Kovarianzmatrix als Drehstreckung interpretieren - sie kodiert genau, wie die Ellipse aus einem perfekten Kreis hervorgeht. Der Kreis entspricht der Identität (Einheitsmatrix) als Kovarianzmatrix. Wenn $\Sigma$ in die eine Richtung dreht, dreht $\Sigma^{-1}$ genau in die Gegenrichtung.
Sie können sich ja vorstellen, was aus dem gewöhnlichen Skalarprodukt wird, wenn man einen der beiden Vektoren vor dem Einsetzen einer Drehstreckung unterwirft.
```

Current English block c14.6:

```md
Die Kovarianzmatrix kodiert genau, wie die Ellipse aus einem perfekten Kreis hervorgeht. Der Kreis entspricht der Einheitsmatrix als Kovarianzmatrix, und $\Sigma = R D^2 R^\top$ aus der Herleitung oben sagt, in welche Richtungen (die Spalten von $R$) und wie stark (die Quadrate der Einträge von $D$) gestreckt wird. $\Sigma$ selbst dreht nichts, es ist symmetrisch; $\Sigma^{-1}$ hat dieselben Eigenvektoren und staucht dort, wo $\Sigma$ streckt. Genau deshalb macht $\Sigma^{-1}$ in der Dichte die Streckung wieder rückgängig und misst den Abstand zu $\mu$ in Einheiten der Streuung.
```

### replace – German block `c23.1` – English block(s) **c23.1**

What changed in the German:

```diff
- Ein Zufallsvektor $X = (X_1,\dots,X_n)$ (d.h. eine multivariate Verteilung) ist multivariat normalverteilt genau dann wenn jede mögliche Linearkombination [-$\sum_{i=1}^n-] \lambda_i X_i$ univariat normalverteilt ist.
+ Ein Zufallsvektor $X = (X_1,\dots,X_n)$ (d.h. eine multivariate Verteilung) ist multivariat normalverteilt genau dann wenn jede mögliche Linearkombination {+$\sum_{i=1}+} \lambda_i X_i$ univariat normalverteilt ist.
```

German now reads:

```md
Ein Zufallsvektor $X = (X_1,\dots,X_n)$ (d.h. eine multivariate Verteilung) ist multivariat normalverteilt genau dann wenn jede mögliche Linearkombination $\sum_{i=1} \lambda_i X_i$ univariat normalverteilt ist.
```

Current English block c23.1:

```md
Ein Zufallsvektor $X = (X_1,\dots,X_n)$ (d.h. eine multivariate Verteilung) ist multivariat normalverteilt genau dann wenn jede mögliche Linearkombination $\sum_{i=1}^n \lambda_i X_i$ univariat normalverteilt ist.
```


## relative-entropie.md → relative-entropy.md

### replace – German block `18`, `19` – English block(s) **18**, **19**

What changed in the German:

```diff
- Seien [-$n,k,m-] \in \mathbb{N}$ sodass [-$2^{m-1}-] \leq n^k \leq [-2^m$.-] Aus der Monotonie folgt dann
+ Seien {+$n,k,l+} \in \mathbb{N}$ sodass {+$2^{l-1}+} \leq n^k \leq {+2^l$.+} Aus der Monotonie folgt dann
- $$ [-f(2^{m-1})-] \leq f(n^k) \leq [-f(2^m)-] $$
+ $$ {+f(2^{l-1})+} \leq f(n^k) \leq {+f(2^l)+} $$
```

German now reads:

```md
Seien $n,k,l \in \mathbb{N}$ sodass $2^{l-1} \leq n^k \leq 2^l$.
Aus der Monotonie folgt dann
$$
f(2^{l-1}) \leq f(n^k) \leq f(2^l)
$$
```

Current English block 18:

```md
Seien $n,k,m \in \mathbb{N}$ sodass $2^{m-1} \leq n^k \leq 2^m$.
Aus der Monotonie folgt dann
```

Current English block 19:

```md
$$
f(2^{m-1}) \leq f(n^k) \leq f(2^m)
$$
```

### replace – German block `21` – English block(s) **21**

What changed in the German:

```diff
- $$ [-(m-1)f(2)-] \leq kf(n) \leq [-mf(2)-] $$
+ $$ {+(l-1)f(2)+} \leq kf(n) \leq {+lf(2)+} $$
```

German now reads:

```md
$$
(l-1)f(2) \leq kf(n) \leq lf(2)
$$
```

Current English block 21:

```md
$$
(m-1)f(2) \leq kf(n) \leq mf(2)
$$
```

### replace – German block `23` – English block(s) **23**

What changed in the German:

```diff
- $$ [--mg(2)-] \leq -kg(n) \leq [--(m-1)g(2).-] $$
+ $$ {+-lg(2)+} \leq -kg(n) \leq {+-(l-1)g(2).+} $$
```

German now reads:

```md
$$
-lg(2) \leq -kg(n) \leq -(l-1)g(2).
$$
```

Current English block 23:

```md
$$
-mg(2) \leq -kg(n) \leq -(m-1)g(2).
$$
```

### replace – German block `29` – English block(s) **29**

What changed in the German:

```diff
- Wenn eine stetige Funktion $F \colon \mathbb{R} \to \mathbb{R}$ die Funktionalgleichung $F(xy) = xF(y) + F(x)y$ erfüllt und [-$F(x)/x$ monoton wachsend ist,-] so existiert eine Konstante $c \in \mathbb{R}$ sodass $F(x) = -x\log(x)c$.
+ Wenn eine stetige Funktion $F \colon \mathbb{R} \to \mathbb{R}$ die Funktionalgleichung $F(xy) = xF(y) + F(x)y$ erfüllt und {+schneller wächst als $x$,+} so existiert eine Konstante $c \in \mathbb{R}$ sodass $F(x) = -x\log(x)c$.
```

German now reads:

```md
Wenn eine stetige Funktion $F \colon \mathbb{R} \to \mathbb{R}$ die Funktionalgleichung $F(xy) = xF(y) + F(x)y$ erfüllt und schneller wächst als $x$, so existiert eine Konstante $c \in \mathbb{R}$ sodass $F(x) = -x\log(x)c$.
```

Current English block 29:

```md
Wenn eine stetige Funktion $F \colon \mathbb{R} \to \mathbb{R}$ die Funktionalgleichung $F(xy) = xF(y) + F(x)y$ erfüllt und $F(x)/x$ monoton wachsend ist, so existiert eine Konstante $c \in \mathbb{R}$ sodass $F(x) = -x\log(x)c$.
```

### replace – German block `32` – English block(s) **32**

What changed in the German:

```diff
- Die Funktion $g(x) := F(x)/x$ erfüllt $g(xy) = g(x) + g(y)$ und [-ist nach Voraussetzung-] monoton, also gibt es $c'$ mit $g(x) = c'\log(x)$, und $c:=-c'$ funktioniert.
+ Die Funktion $g(x) := F(x)/x$ erfüllt $g(xy) = g(x) + g(y)$ und {+wächst+} monoton, also gibt es $c'$ mit $g(x) = c'\log(x)$, und $c:=-c'$ funktioniert.
```

German now reads:

```md
Die Funktion $g(x) := F(x)/x$ erfüllt $g(xy) = g(x) + g(y)$ und wächst monoton, also gibt es $c'$ mit $g(x) = c'\log(x)$, und $c:=-c'$ funktioniert.
```

Current English block 32:

```md
Die Funktion $g(x) := F(x)/x$ erfüllt $g(xy) = g(x) + g(y)$ und ist nach Voraussetzung monoton, also gibt es $c'$ mit $g(x) = c'\log(x)$, und $c:=-c'$ funktioniert.
```

### replace – German block `35` – English block(s) **35**

What changed in the German:

```diff
- Wir sehen also, dass [-der Entropie-Beitrag $-p\log(p)$ eines Ergebnisses mit Wahrscheinlichkeit $p$-] eine sehr natürliche Größe ist. [-(Die *Information* $I(x) = -\log P(\{x\})$ aus dem Kapitel [Erwartungswert und Varianz](erwartungswert.md) ist der Faktor hinter dem $p$.)-]
+ Wir sehen also, dass {+die Information $I(x) = -x\log(x)$+} eine sehr natürliche Größe ist.
```

German now reads:

```md
Wir sehen also, dass die Information $I(x) = -x\log(x)$ eine sehr natürliche Größe ist.
```

Current English block 35:

```md
Wir sehen also, dass der Entropie-Beitrag $-p\log(p)$ eines Ergebnisses mit Wahrscheinlichkeit $p$ eine sehr natürliche Größe ist. (Die *Information* $I(x) = -\log P(\{x\})$ aus dem Kapitel [Erwartungswert und Varianz](expectation-variance.md) ist der Faktor hinter dem $p$.)
```

### replace – German block `54` – English block(s) **54**

What changed in the German:

```diff
- ## [-Definition und Eigenschaften-]
+ ## {+Relative Entropie+}
```

German now reads:

```md
## Relative Entropie
```

Current English block 54:

```md
## Definition und Eigenschaften
```

### replace – German block `75`, `76`, `77`, `78`, `79` – English block(s) **75**, **76**, **77**, **78**, **79**

German now reads:

```md
Die relative Entropie ist nicht symmetrisch und kann durchaus unendlich groß werden:
$$
H\left(u_2 \big\Vert  \begin{pmatrix} t \\ 1-t \end{pmatrix} \right) = \frac{1}{2} \log \left( \frac{1}{2t} \right) + \frac{1}{2}\log \left(\frac{1}{2(1-t)}\right) \xrightarrow{t \to 0} \log(\infty) = \infty.
$$
Wie zuvor besprochen ist $H\left( \begin{pmatrix} t \\ 1-t \end{pmatrix} \big\Vert  u_2 \right) = \log(n) - H\left( \begin{pmatrix} t \\ 1-t \end{pmatrix} \right)$
und
$$
H(u_2) = t\log(t) - (1-t)\log(1-t) \xrightarrow{t \to 0} 0 - 1\log(1) = 0
$$
```

Current English block 75:

```md
Die relative Entropie ist nicht symmetrisch und kann unendlich groß werden. Sei $p_t := (t,\ 1-t)$ für $0 < t < 1$, eine Münze, die für kleines $t$ fast sicher auf $1$ fällt. In der einen Richtung ist
```

Current English block 76:

```md
$$
H\left(u_2 \,\Vert\, p_t\right) = \frac{1}{2} \log \frac{1}{2t} + \frac{1}{2}\log \frac{1}{2(1-t)} \xrightarrow{t \to 0} \infty,
$$
```

Current English block 77:

```md
denn der erste Summand wächst wie $-\frac12\log t$ über alle Grenzen. In der anderen Richtung liefert die Proposition oben
```

Current English block 78:

```md
$$
H\left(p_t \,\Vert\, u_2\right) = \log(2) - H(p_t), \qquad H(p_t) = -t\log t - (1-t)\log(1-t) \xrightarrow{t \to 0} 0,
$$
```

Current English block 79:

```md
also $H(p_t \Vert u_2) \to \log 2$: endlich, zur Basis $2$ genau ein Bit. Wer die fast sichere Münze $p_t$ für fair hält, zahlt höchstens ein Bit; wer umgekehrt die faire Münze für $p_t$ hält, wird von der Seite, die er für unmöglich hielt, unendlich überrascht.
```

### replace – German block `105` – English block(s) **105**

What changed in the German:

```diff
- Die *gemeinsame Information* [-(auch *Transinformation*, englisch *mutual information*)-] von zwei Zufallsvariablen $X,Y$ ist definiert als
+ Die *gemeinsame Information* von zwei Zufallsvariablen $X,Y$ ist definiert als
```

German now reads:

```md
Die *gemeinsame Information* von zwei Zufallsvariablen $X,Y$ ist definiert als
```

Current English block 105:

```md
Die *gemeinsame Information* (auch *Transinformation*, englisch *mutual information*) von zwei Zufallsvariablen $X,Y$ ist definiert als
```

### replace – German block `114` – English block(s) **114**

What changed in the German:

```diff
- Wenn $X,Y$ unabhängig sind, ist [-$I(X;Y)-] = H(X) + H(Y) - (H(X) + H(Y)) = 0$.
+ Wenn $X,Y$ unabhängig sind, ist {+$I(X,Y)+} = H(X) + H(Y) - (H(X) + H(Y)) = 0$.
```

German now reads:

```md
Wenn $X,Y$ unabhängig sind, ist $I(X,Y) = H(X) + H(Y) - (H(X) + H(Y)) = 0$.
```

Current English block 114:

```md
Wenn $X,Y$ unabhängig sind, ist $I(X;Y) = H(X) + H(Y) - (H(X) + H(Y)) = 0$.
```

### replace – German block `127` – English block(s) **127**

What changed in the German:

```diff
- ```{figure} images/1920px-Entropy-mutual-information-relative-entropy-relation-diagram.svg.png :width: 480px :align: center :name: entropy-diagram Entropie, bedingte Entropie, Verbundentropie und gemeinsame Information in einem Venn-Diagramm. [-Abbildung: [Wikimedia Commons, Benutzer KonradVoelkel](https://commons.wikimedia.org/wiki/File:Entropy-mutual-information-relative-entropy-relation-diagram.svg) (2010, gemeinfrei).-] ```
+ ```{figure} images/1920px-Entropy-mutual-information-relative-entropy-relation-diagram.svg.png :width: 480px :align: center :name: entropy-diagram Entropie, bedingte Entropie, Verbundentropie und gemeinsame Information in einem Venn-Diagramm. ```
```

German now reads:

```md
```{figure} images/1920px-Entropy-mutual-information-relative-entropy-relation-diagram.svg.png
:width: 480px
:align: center
:name: entropy-diagram

Entropie, bedingte Entropie, Verbundentropie und gemeinsame Information in einem Venn-Diagramm.
```
```

Current English block 127:

```md
```{figure} images/1920px-Entropy-mutual-information-relative-entropy-relation-diagram.svg.png
:width: 480px
:align: center
:name: entropy-diagram

Entropie, bedingte Entropie, Verbundentropie und gemeinsame Information in einem Venn-Diagramm. Abbildung: [Wikimedia Commons, Benutzer KonradVoelkel](https://commons.wikimedia.org/wiki/File:Entropy-mutual-information-relative-entropy-relation-diagram.svg) (2010, gemeinfrei).
```
```

### replace – German block `129`, `130` – English block(s) **129**, **130**

What changed in the German:

```diff
- Die *Kreuzentropie* von $X$ (verteilt nach $p \in [-\Delta_n$)-] und $Y$ (verteilt nach $r \in [-\Delta_n$)-] ist
+ Die *Kreuzentropie* von $X$ (verteilt nach $p \in {+\Delta^n$)+} und $Y$ (verteilt nach $r \in {+\Delta^n$)+} ist
- $$ H(X; Y) = \mathbb{E}_X I(Y) = -\sum_{i,\ [-p_i-] > 0}^n p_i \log r_i \in \mathbb{R} \cup \{\infty\}. $$
+ $$ H(X; Y) = \mathbb{E}_X I(Y) = -\sum_{i,\ {+r_i+} > 0}^n p_i \log r_i \in \mathbb{R} \cup \{\infty\}. $$
```

German now reads:

```md
Die *Kreuzentropie* von $X$ (verteilt nach $p \in \Delta^n$) und $Y$ (verteilt nach $r \in \Delta^n$) ist
$$
H(X; Y) = \mathbb{E}_X I(Y) = -\sum_{i,\ r_i > 0}^n p_i \log r_i \in \mathbb{R} \cup \{\infty\}.
$$
```

Current English block 129:

```md
Die *Kreuzentropie* von $X$ (verteilt nach $p \in \Delta_n$) und $Y$ (verteilt nach $r \in \Delta_n$) ist
```

Current English block 130:

```md
$$
H(X; Y) = \mathbb{E}_X I(Y) = -\sum_{i,\ p_i > 0}^n p_i \log r_i \in \mathbb{R} \cup \{\infty\}.
$$
```

### delete – German block `132` – English block(s) **132**

Current English block 132:

```md
Ein Summand mit $p_i > 0$ und $r_i = 0$ hat dabei den Wert $\infty$ (mit $\log 0 = -\infty$): Ein Ereignis, das nach $r$ unmöglich ist, aber nach $p$ vorkommt, kostet unendlich viel.
```

### replace – German block `154` – English block(s) **154**

What changed in the German:

```diff
- Jaynes hat vorgeschlagen, sich immer feiner werdende Histogramme vorzustellen, also eine Menge von $N$ diskreten Punkten $\{x_i\}$, dann schreiben wir $M(a,b) = \lim_{N \to \infty} [-\frac{1}{N}-] (\text{Anzahl } x_i : a < x_i < b)$ und eine Dichte $m$ mit $M(a,b) = \int_a^b m(x) dx$ nennen wir *invariantes Maß*. Damit schreiben wir nun
+ Jaynes hat vorgeschlagen, sich immer feiner werdende Histogramme vorzustellen, also eine Menge von $N$ diskreten Punkten $\{x_i\}$, dann schreiben wir $M(a,b) = \lim_{N \to \infty} {+\frac{1}{n}+} (\text{Anzahl } x_i : a < x_i < b)$ und eine Dichte $m$ mit $M(a,b) = \int_a^b m(x) dx$ nennen wir *invariantes Maß*. Damit schreiben wir nun
```

German now reads:

```md
Jaynes hat vorgeschlagen, sich immer feiner werdende Histogramme vorzustellen, also eine Menge von $N$ diskreten Punkten $\{x_i\}$,
dann schreiben wir
$M(a,b) = \lim_{N \to \infty} \frac{1}{n} (\text{Anzahl } x_i : a < x_i < b)$
und eine Dichte $m$ mit $M(a,b) = \int_a^b m(x) dx$ nennen wir *invariantes Maß*.
Damit schreiben wir nun
```

Current English block 154:

```md
Jaynes hat vorgeschlagen, sich immer feiner werdende Histogramme vorzustellen, also eine Menge von $N$ diskreten Punkten $\{x_i\}$,
dann schreiben wir
$M(a,b) = \lim_{N \to \infty} \frac{1}{N} (\text{Anzahl } x_i : a < x_i < b)$
und eine Dichte $m$ mit $M(a,b) = \int_a^b m(x) dx$ nennen wir *invariantes Maß*.
Damit schreiben wir nun
```

### replace – German block `159` – English block(s) **159**

What changed in the German:

```diff
- Wenn man vom theoretischen Standpunkt analysiert, was $h(X)$ und $H(X)$ sind, so kommt man zur allgemeinen relativen Entropie $H(P,Q)$, sodass $h(X) = [--H(f\lambda \,\Vert\,-] \lambda)$ mit $\lambda$ dem Lebesgue-Maß und $f$ einer Dichte von $X$.
+ Wenn man vom theoretischen Standpunkt analysiert, was $h(X)$ und $H(X)$ sind, so kommt man zur allgemeinen relativen Entropie $H(P,Q)$, sodass $h(X) = {+H(f\lambda |+} \lambda)$ mit $\lambda$ dem Lebesgue-Maß und $f$ einer Dichte von $X$.
```

German now reads:

```md
Wenn man vom theoretischen Standpunkt analysiert, was $h(X)$ und $H(X)$ sind, so kommt man zur allgemeinen relativen Entropie $H(P,Q)$, sodass $h(X) = H(f\lambda | \lambda)$ mit $\lambda$ dem Lebesgue-Maß und $f$ einer Dichte von $X$.
```

Current English block 159:

```md
Wenn man vom theoretischen Standpunkt analysiert, was $h(X)$ und $H(X)$ sind, so kommt man zur allgemeinen relativen Entropie $H(P,Q)$, sodass $h(X) = -H(f\lambda \,\Vert\, \lambda)$ mit $\lambda$ dem Lebesgue-Maß und $f$ einer Dichte von $X$.
```

### replace – German block `165` – English block(s) **165**

What changed in the German:

```diff
- Das wollen wir jetzt auch nicht weiter diskutieren, sondern lieber festhalten, dass das für $P$ und $R$ mit Dichtefunktionen $p,r \colon \mathbb{R}^n \to [-[0,\infty)$-] einfacher aussieht:
+ Das wollen wir jetzt auch nicht weiter diskutieren, sondern lieber festhalten, dass das für $P$ und $R$ mit Dichtefunktionen $p,r \colon \mathbb{R}^n \to {+[0,1]$+} einfacher aussieht:
```

German now reads:

```md
Das wollen wir jetzt auch nicht weiter diskutieren, sondern lieber festhalten, dass das für $P$ und $R$ mit Dichtefunktionen $p,r \colon \mathbb{R}^n \to [0,1]$ einfacher aussieht:
```

Current English block 165:

```md
Das wollen wir jetzt auch nicht weiter diskutieren, sondern lieber festhalten, dass das für $P$ und $R$ mit Dichtefunktionen $p,r \colon \mathbb{R}^n \to [0,\infty)$ einfacher aussieht:
```


## datenschutz.md → data-protection.md

### replace – German block `6` – English block(s) **6**

What changed in the German:

```diff
- Auch [-**pseudonymisierte**-] oder [-**verschlüsselte** Daten-] fallen unter den Schutz der [-DSGVO, ebenso vermeintlich **anonymisierte** Daten, sobald sich der Personenbezug mit vertretbarem Aufwand wiederherstellen lässt (Erwägungsgrund 26).-]
+ Auch {+**pseudonymisierte**, **verschlüsselte**+} oder {+**anonymisierte Daten**, die wieder einer Person zugeordnet werden können,+} fallen unter den Schutz der {+DSGVO.+}
```

German now reads:

```md
Auch **pseudonymisierte**, **verschlüsselte** oder **anonymisierte Daten**, die wieder einer Person zugeordnet werden können, fallen unter den Schutz der DSGVO.
```

Current English block 6:

```md
Auch **pseudonymisierte** oder **verschlüsselte** Daten fallen unter den Schutz der DSGVO, ebenso vermeintlich **anonymisierte** Daten, sobald sich der Personenbezug mit vertretbarem Aufwand wiederherstellen lässt (Erwägungsgrund 26).
```

### delete – German block `8`, `9`, `10` – English block(s) **8**, **9**, **10**

Current English block 8:

```md
## Vorgeschichte der DSGVO
```

Current English block 9:

```md
Die DSGVO ist 2018 nicht aus dem Nichts entstanden. Vier Stationen erklären, warum sie so aussieht, wie sie aussieht:
```

Current English block 10:

```md
- **Recht auf informationelle Selbstbestimmung**: Das Bundesverfassungsgericht entwickelte es im *Volkszählungsurteil* vom 15. Dezember 1983 (1 BvR 209/83 u. a.) aus dem allgemeinen Persönlichkeitsrecht. Der Kernsatz ist bis heute die beste Kurzfassung des Schutzzwecks: Mit dem Selbstbestimmungsrecht wäre eine Gesellschaftsordnung nicht vereinbar, „in der Bürger nicht mehr wissen können, wer was wann und bei welcher Gelegenheit über sie weiß“. Anlass war eine geplante Volkszählung — ein Datenschutzproblem entsteht also nicht erst durch Computer, sondern durch Zusammenführung.
- **Bundesdatenschutzgesetz (BDSG)**: 1977 erstmals erlassen, 1990 grundlegend neu gefasst, um das Volkszählungsurteil umzusetzen. Es gilt bis heute, seit 2018 aber nur noch ergänzend zur DSGVO, dort wo diese den Mitgliedstaaten Spielraum lässt (etwa beim Beschäftigtendatenschutz).
- **Richtlinie 95/46/EG** vom 24. Oktober 1995: die unmittelbare Vorläuferin der DSGVO. Sie enthielt bereits die Grundsätze, die Rechtsgrundlagen und die Betroffenenrechte, war als Richtlinie aber auf Umsetzung in nationales Recht angewiesen — mit entsprechend unterschiedlichen Ergebnissen in den Mitgliedstaaten. Die DSGVO hob sie auf und regelte dasselbe als unmittelbar geltende Verordnung.
- **ePrivacy-Richtlinie 2002/58/EG**: Sonderregeln für elektronische Kommunikation, Nachfolgerin der Richtlinie 97/66/EG, geändert durch 2009/136/EG. Aus ihr stammt die Pflicht, über die Speicherung von Informationen auf Endgeräten zu informieren und eine Ablehnung zu ermöglichen — also das, was heute jede Website als *Cookie-Banner* anzeigt. Eine ablösende ePrivacy-Verordnung wird seit 2017 verhandelt.
```

### replace – German block `12` – English block(s) **12**

What changed in the German:

```diff
- [-- **Anwendungsbereich** (Art. 2 Abs. 1 DSGVO): Die Verordnung gilt für die ganz oder teilweise automatisierte Verarbeitung personenbezogener Daten sowie für die nichtautomatisierte Verarbeitung solcher Daten, die in einem Dateisystem gespeichert sind oder gespeichert werden sollen. Der Zettelkasten fällt also darunter, der einzelne Notizzettel nicht.-] - **Verarbeitung**: Jeder Vorgang im Zusammenhang mit personenbezogenen Daten – von der Erhebung über Speicherung und Nutzung bis zur Löschung. - **Verantwortlicher**: Die Stelle, die über Zwecke und Mittel der Datenverarbeitung entscheidet. - **Auftragsverarbeiter**: Eine dritte Partei, die im Auftrag des Verantwortlichen Daten verarbeitet – z. B. ein externer Dienstleister. [-Der Auftragsverarbeiter ist an die Weisungen des Verantwortlichen gebunden, und das Verhältnis muss in einem **Auftragsverarbeitungsvertrag (AVV)** nach Art. 28 DSGVO schriftlich festgehalten werden: Gegenstand, Dauer, Art und Zweck der Verarbeitung, Kategorien betroffener Personen, Pflichten und Rechte beider Seiten.-] - **Einwilligung**: Eine freiwillige, informierte und eindeutige Zustimmung der betroffenen Person zur Datenverarbeitung. Freiwillig heißt auch: ohne Abhängigkeitsverhältnis. Eine Schule in Skellefteå ließ Schüler\*innen per Gesichtserkennung die Anwesenheit erfassen, mit Einwilligung der Eltern; die schwedische Aufsicht hielt die Einwilligung wegen des Machtgefälles zwischen Schule und Familien für unwirksam ([ETid-67](https://www.enforcementtracker.com/ETid-67), 2019, rund 18.600 €). Die Telefonliste des Kindergartens dagegen ist mit Einwilligung der Eltern in Ordnung.
+ - **Verarbeitung**: Jeder Vorgang im Zusammenhang mit personenbezogenen Daten – von der Erhebung über Speicherung und Nutzung bis zur Löschung. - **Verantwortlicher**: Die Stelle, die über Zwecke und Mittel der Datenverarbeitung entscheidet. - **Auftragsverarbeiter**: Eine dritte Partei, die im Auftrag des Verantwortlichen Daten verarbeitet – z. B. ein externer Dienstleister. - **Einwilligung**: Eine freiwillige, informierte und eindeutige Zustimmung der betroffenen Person zur Datenverarbeitung. Freiwillig heißt auch: ohne Abhängigkeitsverhältnis. Eine Schule in Skellefteå ließ Schüler\*innen per Gesichtserkennung die Anwesenheit erfassen, mit Einwilligung der Eltern; die schwedische Aufsicht hielt die Einwilligung wegen des Machtgefälles zwischen Schule und Familien für unwirksam ([ETid-67](https://www.enforcementtracker.com/ETid-67), 2019, rund 18.600 €). Die Telefonliste des Kindergartens dagegen ist mit Einwilligung der Eltern in Ordnung.
```

German now reads:

```md
- **Verarbeitung**: Jeder Vorgang im Zusammenhang mit personenbezogenen Daten – von der Erhebung über Speicherung und Nutzung bis zur Löschung.
- **Verantwortlicher**: Die Stelle, die über Zwecke und Mittel der Datenverarbeitung entscheidet.
- **Auftragsverarbeiter**: Eine dritte Partei, die im Auftrag des Verantwortlichen Daten verarbeitet – z. B. ein externer Dienstleister.
- **Einwilligung**: Eine freiwillige, informierte und eindeutige Zustimmung der betroffenen Person zur Datenverarbeitung. Freiwillig heißt auch: ohne Abhängigkeitsverhältnis. Eine Schule in Skellefteå ließ Schüler\*innen per Gesichtserkennung die Anwesenheit erfassen, mit Einwilligung der Eltern; die schwedische Aufsicht hielt die Einwilligung wegen des Machtgefälles zwischen Schule und Familien für unwirksam ([ETid-67](https://www.enforcementtracker.com/ETid-67), 2019, rund 18.600 €). Die Telefonliste des Kindergartens dagegen ist mit Einwilligung der Eltern in Ordnung.
```

Current English block 12:

```md
- **Anwendungsbereich** (Art. 2 Abs. 1 DSGVO): Die Verordnung gilt für die ganz oder teilweise automatisierte Verarbeitung personenbezogener Daten sowie für die nichtautomatisierte Verarbeitung solcher Daten, die in einem Dateisystem gespeichert sind oder gespeichert werden sollen. Der Zettelkasten fällt also darunter, der einzelne Notizzettel nicht.
- **Verarbeitung**: Jeder Vorgang im Zusammenhang mit personenbezogenen Daten – von der Erhebung über Speicherung und Nutzung bis zur Löschung.
- **Verantwortlicher**: Die Stelle, die über Zwecke und Mittel der Datenverarbeitung entscheidet.
- **Auftragsverarbeiter**: Eine dritte Partei, die im Auftrag des Verantwortlichen Daten verarbeitet – z. B. ein externer Dienstleister. Der Auftragsverarbeiter ist an die Weisungen des Verantwortlichen gebunden, und das Verhältnis muss in einem **Auftragsverarbeitungsvertrag (AVV)** nach Art. 28 DSGVO schriftlich festgehalten werden: Gegenstand, Dauer, Art und Zweck der Verarbeitung, Kategorien betroffener Personen, Pflichten und Rechte beider Seiten.
- **Einwilligung**: Eine freiwillige, informierte und eindeutige Zustimmung der betroffenen Person zur Datenverarbeitung. Freiwillig heißt auch: ohne Abhängigkeitsverhältnis. Eine Schule in Skellefteå ließ Schüler\*innen per Gesichtserkennung die Anwesenheit erfassen, mit Einwilligung der Eltern; die schwedische Aufsicht hielt die Einwilligung wegen des Machtgefälles zwischen Schule und Familien für unwirksam ([ETid-67](https://www.enforcementtracker.com/ETid-67), 2019, rund 18.600 €). Die Telefonliste des Kindergartens dagegen ist mit Einwilligung der Eltern in Ordnung.
```

### replace – German block `15`, `16` – English block(s) **15**, **16**

German now reads:

```md
1. **Rechtmäßigkeit, Transparenz**
2. **Zweckbindung** – Nutzung nur zu legitim festgelegten Zwecken
3. **Datenminimierung** – nur so viel wie nötig
4. **Richtigkeit** – unrichtige Daten sind zu berichtigen
5. **Speicherbegrenzung** – Daten nur solange wie erforderlich speichern
6. **Integrität & Vertraulichkeit** – Schutz vor unbefugtem Zugriff und Verlust
```

Current English block 15:

```md
1. **Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz** (Art. 5 Abs. 1 lit. a) – „auf rechtmäßige Weise, nach Treu und Glauben und in einer für die betroffene Person nachvollziehbaren Weise“
2. **Zweckbindung** (lit. b) – Nutzung nur zu „festgelegten, eindeutigen und legitimen Zwecken“
3. **Datenminimierung** (lit. c) – „dem Zweck angemessen und erheblich sowie auf das notwendige Maß beschränkt“
4. **Richtigkeit** (lit. d) – „sachlich richtig und erforderlichenfalls auf dem neuesten Stand“; unrichtige Daten sind zu berichtigen oder zu löschen
5. **Speicherbegrenzung** (lit. e) – in identifizierbarer Form nur so lange, „wie es für die Zwecke … erforderlich ist“
6. **Integrität und Vertraulichkeit** (lit. f) – Schutz vor „unbefugter oder unrechtmäßiger Verarbeitung und vor unbeabsichtigtem Verlust“
```

Current English block 16:

```md
Dazu kommt in Art. 5 Abs. 2 die **Rechenschaftspflicht**: Der Verantwortliche muss die Einhaltung dieser Grundsätze nicht nur gewährleisten, sondern auch nachweisen können. Das ist der Grund, warum Datenschutz in der Praxis so viel Dokumentation bedeutet.
```

### replace – German block `24` – English block(s) **24**

What changed in the German:

```diff
- - **Privacy by [-Design** (Art. 25 Abs. 1):-] Datenschutz muss schon bei der Konzeption von Systemen mitgedacht [-werden, nicht nachträglich angebaut. Drei Leitsätze fassen zusammen, was das praktisch heißt: 1. Was technisch unmöglich gemacht wird, muss nicht überwacht-] werden. [-Ein Feld, das es nicht gibt, kann nicht missbraucht werden. 2. Geschäftsabläufe funktional trennen und so früh wie möglich anonymisieren — je später im Prozess ein Personenbezug besteht, desto kleiner ist der Kreis derer, die ihn sehen. 3. Die Architektur datenschutzfreundlich auslegen, physisch wie elektronisch: getrennte Systeme, getrennte Zugriffsrechte, getrennte Räume.-] - **Privacy by [-Default** (Art. 25 Abs. 2): Die Voreinstellungen müssen die datensparsamen sein. Der Grund ist empirisch und nicht juristisch: Menschen setzen ihren erklärten Datenschutzwunsch im Alltag oft nicht um — aus Bequemlichkeit, Unkenntnis oder weil sie im Einzelfall anders abwägen. Wer bei jedem Cookie-Banner „alle akzeptieren“ klickt, hat damit nicht seine Präferenz geäußert, sondern den Weg des geringsten Widerstands genommen. Deshalb entscheidet die Voreinstellung faktisch über das Ergebnis.-]
+ - **Privacy by {+Design**:+} Datenschutz muss schon bei der Konzeption von Systemen mitgedacht werden. - **Privacy by {+Default**: Systeme sollen standardmäßig datensparsame Einstellungen haben.+}
```

German now reads:

```md
- **Privacy by Design**: Datenschutz muss schon bei der Konzeption von Systemen mitgedacht werden.
- **Privacy by Default**: Systeme sollen standardmäßig datensparsame Einstellungen haben.
```

Current English block 24:

```md
- **Privacy by Design** (Art. 25 Abs. 1): Datenschutz muss schon bei der Konzeption von Systemen mitgedacht werden, nicht nachträglich angebaut. Drei Leitsätze fassen zusammen, was das praktisch heißt:
  1. Was technisch unmöglich gemacht wird, muss nicht überwacht werden. Ein Feld, das es nicht gibt, kann nicht missbraucht werden.
  2. Geschäftsabläufe funktional trennen und so früh wie möglich anonymisieren — je später im Prozess ein Personenbezug besteht, desto kleiner ist der Kreis derer, die ihn sehen.
  3. Die Architektur datenschutzfreundlich auslegen, physisch wie elektronisch: getrennte Systeme, getrennte Zugriffsrechte, getrennte Räume.
- **Privacy by Default** (Art. 25 Abs. 2): Die Voreinstellungen müssen die datensparsamen sein. Der Grund ist empirisch und nicht juristisch: Menschen setzen ihren erklärten Datenschutzwunsch im Alltag oft nicht um — aus Bequemlichkeit, Unkenntnis oder weil sie im Einzelfall anders abwägen. Wer bei jedem Cookie-Banner „alle akzeptieren“ klickt, hat damit nicht seine Präferenz geäußert, sondern den Weg des geringsten Widerstands genommen. Deshalb entscheidet die Voreinstellung faktisch über das Ergebnis.
```

### replace – German block `26`, `27` – English block(s) **26**, **27**

What changed in the German:

```diff
- ## [-Datenminimierung in der Praxis-]
+ ## {+Datensparsamkeit+}
- [-Datenminimierung (Art. 5 Abs. 1 lit. c;-] im [-alten BDSG hieß dasselbe Prinzip *Datensparsamkeit*, § 3a BDSG a.F.) bedeutet praktisch:-] - Keine Erhebung irrelevanter Daten - Verzicht auf optionale Angaben (z. B. Alter bei Bestellung, wenn nicht erforderlich) - Hinweis auf Freiwilligkeit und Voreinstellung auf "nicht erheben"
+ {+Ein zentrales Prinzip+} im {+Datenschutz. Es bedeutet:+} - Keine Erhebung irrelevanter Daten - Verzicht auf optionale Angaben (z. B. Alter bei Bestellung, wenn nicht erforderlich) - Hinweis auf Freiwilligkeit und Voreinstellung auf "nicht erheben"
```

German now reads:

```md
## Datensparsamkeit
Ein zentrales Prinzip im Datenschutz. Es bedeutet:
- Keine Erhebung irrelevanter Daten
- Verzicht auf optionale Angaben (z. B. Alter bei Bestellung, wenn nicht erforderlich)
- Hinweis auf Freiwilligkeit und Voreinstellung auf "nicht erheben"
```

Current English block 26:

```md
## Datenminimierung in der Praxis
```

Current English block 27:

```md
Datenminimierung (Art. 5 Abs. 1 lit. c; im alten BDSG hieß dasselbe Prinzip *Datensparsamkeit*, § 3a BDSG a.F.) bedeutet praktisch:
- Keine Erhebung irrelevanter Daten
- Verzicht auf optionale Angaben (z. B. Alter bei Bestellung, wenn nicht erforderlich)
- Hinweis auf Freiwilligkeit und Voreinstellung auf "nicht erheben"
```

### replace – German block `30`, `31` – English block(s) **30**, **31**

German now reads:

```md
- **Pseudonymisierung**: Verarbeitung in einer Weise, dass Daten ohne zusätzliche Informationen nicht einer Person zugeordnet werden können.
- **Rechte Betroffener**: z. B. Auskunft, Löschung, Berichtigung, Widerspruch. Das Auskunftsrecht (Art. 15) umfasst auch Videoaufnahmen: Die ungarische Tochter von Deichmann verweigerte einer Kundin die Herausgabe der Aufnahmen aus dem Laden und zahlte 54.800 € ([ETid-430](https://www.enforcementtracker.com/ETid-430), 2020).
- **Meldepflicht bei Datenpannen** (Art. 33): Verletzungen des Schutzes personenbezogener Daten sind innerhalb von 72 Stunden der Aufsicht zu melden. Twitter meldete eine Panne zu spät und unvollständig, 450.000 € ([ETid-485](https://www.enforcementtracker.com/ETid-485), 2020); Knuddels (oben) meldete sofort und wurde dafür milder behandelt.
- **Datenübermittlung in Drittländer**: Nur bei angemessenem Datenschutzniveau zulässig. Die Geschichte dazu ist eine Posse in mehreren Akten: Das *Safe-Harbor*-Abkommen mit den USA kippte der EuGH 2015 auf Klage von Max Schrems, das Nachfolgeabkommen *Privacy Shield* 2020 (Schrems II), jeweils weil US-Behörden auf die Daten zugreifen können. Meta übertrug Facebook-Daten trotzdem weiter in die USA und bekam mit 1,2 Mrd. € das bisher höchste DSGVO-Bußgeld ([ETid-1844](https://www.enforcementtracker.com/ETid-1844), 2023). Die von Schrems gegründete Organisation [noyb](https://noyb.eu) erreichte außerdem, dass die österreichische Aufsicht 2022 den Einsatz von Google Analytics als rechtswidrig einstufte, ohne Bußgeld, aber mit Folgen für fast jede Website. Wer Daten in eine US-Cloud legt, muss diese Geschichte kennen.
```

Current English block 30:

```md
- **Pseudonymisierung**: Verarbeitung in einer Weise, dass Daten ohne zusätzliche Informationen nicht einer Person zugeordnet werden können.
- **Selbstgenerierter Code** (Längsschnittstudien): Bei Mehrfachbefragungen will man die Antworten derselben Person über mehrere Erhebungen zusammenführen, ohne sie der Person zuordnen zu können. Die befragte Person bildet dazu aus stabilen persönlichen Merkmalen selbst einen Code — etwa dem ersten und letzten Buchstaben der Vornamen der Eltern und dem Tag des eigenen Geburtsdatums — und gespeichert wird nur dessen Hash. Weil dieselbe Person denselben Code reproduzieren kann, lassen sich die Wellen verknüpfen; weil die Erhebenden den Code nicht kennen, können sie ihn nicht zurückrechnen. Die Verfahren und ihre Fehlerquoten sind gut untersucht {cite}`poege2011`. Ein Pseudonym bleibt es trotzdem: Wer die Bildungsregel und genug Hintergrundwissen über die Befragten hat, kann Kandidaten durchprobieren — gehashte Daten sind also nicht automatisch anonym.
- **Rechte Betroffener**: Kapitel III der DSGVO gibt der betroffenen Person sieben Rechte, die der Verantwortliche auf Verlangen erfüllen muss — in der Regel binnen eines Monats und unentgeltlich:
  - **Auskunft** (Art. 15): Welche Daten werden verarbeitet, zu welchem Zweck, woher stammen sie, an wen gehen sie, wie lange werden sie gespeichert — nebst einer Kopie der Daten. Das umfasst auch Videoaufnahmen: Die ungarische Tochter von Deichmann verweigerte einer Kundin die Herausgabe der Aufnahmen aus dem Laden und zahlte 54.800 € ([ETid-430](https://www.enforcementtracker.com/ETid-430), 2020).
  - **Berichtigung** (Art. 16): unrichtige Daten korrigieren, unvollständige vervollständigen.
  - **Löschung** (Art. 17), auch „Recht auf Vergessenwerden“: etwa wenn der Zweck entfallen ist oder die Einwilligung widerrufen wurde.
  - **Einschränkung der Verarbeitung** (Art. 18): der Mittelweg, solange etwa die Richtigkeit der Daten geprüft wird — die Daten bleiben gespeichert, dürfen aber nicht weiterverwendet werden.
  - **Mitteilungspflicht** (Art. 19): Berichtigung, Löschung und Einschränkung muss der Verantwortliche allen Empfängern mitteilen, an die er die Daten weitergegeben hat.
  - **Datenübertragbarkeit** (Art. 20): die eigenen Daten in einem gängigen maschinenlesbaren Format erhalten und zu einem anderen Anbieter mitnehmen.
  - **Widerspruch** (Art. 21): gegen eine Verarbeitung, die auf berechtigtem Interesse beruht; bei Direktwerbung ohne jede Abwägung und jederzeit.
```

Current English block 31:

```md
  Dazu kommt die **Haftung** (Art. 82): Wer durch einen Verstoß einen materiellen oder immateriellen Schaden erleidet, hat Anspruch auf Schadenersatz. Der Verantwortliche entlastet sich nur, wenn er nachweist, dass er in keinerlei Hinsicht für den Schaden verantwortlich ist.
- **Meldepflicht bei Datenpannen** (Art. 33): Verletzungen des Schutzes personenbezogener Daten sind innerhalb von 72 Stunden der Aufsicht zu melden. Twitter meldete eine Panne zu spät und unvollständig, 450.000 € ([ETid-485](https://www.enforcementtracker.com/ETid-485), 2020); Knuddels (oben) meldete sofort und wurde dafür milder behandelt.
- **Datenübermittlung in Drittländer**: Nur bei angemessenem Datenschutzniveau zulässig. Der einfachste Weg dorthin ist ein **Angemessenheitsbeschluss** der Kommission nach Art. 45: Stellt sie für ein Land ein angemessenes Schutzniveau fest, darf man dorthin übermitteln wie innerhalb der EU. Für die USA ist das eine Posse in mehreren Akten:
  - **Safe Harbor** (Entscheidung der Kommission vom 26.7.2000) — vom EuGH im Urteil *Schrems I* am 6.10.2015 für ungültig erklärt.
  - **EU-US Privacy Shield** (Durchführungsbeschluss (EU) 2016/1250) — vom EuGH im Urteil *Schrems II* am 16.7.2020 für ungültig erklärt, jeweils weil US-Behörden auf die Daten zugreifen können und Betroffene aus der EU dagegen keinen wirksamen Rechtsbehelf haben.
  - **EU-U.S. Data Privacy Framework** (Durchführungsbeschluss (EU) 2023/1795, seit Juli 2023) — der dritte Anlauf, rechtlich von Anfang an umstritten. Er steht und fällt mit der Unabhängigkeit der US-Aufsicht; Stand September 2026 ist genau die wieder fraglich, und eine erneute Klage ist angekündigt. Wer heute eine US-Cloud einplant, sollte also einkalkulieren, dass die Grundlage wieder wegfallen kann. Meta übertrug Facebook-Daten trotzdem weiter in die USA und bekam mit 1,2 Mrd. € das bisher höchste DSGVO-Bußgeld ([ETid-1844](https://www.enforcementtracker.com/ETid-1844), 2023). Die von Schrems gegründete Organisation [noyb](https://noyb.eu) erreichte außerdem, dass die österreichische Aufsicht 2022 den Einsatz von Google Analytics als rechtswidrig einstufte, ohne Bußgeld, aber mit Folgen für fast jede Website. Wer Daten in eine US-Cloud legt, muss diese Geschichte kennen.
```

### replace – German block `33`, `34`, `35`, `36` – English block(s) **33**, **34**, **35**, **36**

German now reads:

```md
Die Neuerung der DSGVO gegenüber der Richtlinie von 1995 sind weniger die Grundsätze als die Sanktionen: bis zu 20 Mio. € oder 4 % des weltweiten Jahresumsatzes (Art. 83), und die Aufsichtsbehörden dürfen Verarbeitungen untersagen (Art. 58). Zwei Missverständnisse sind damit erledigt: Datenschutz ist weder zu kompliziert, um sich damit zu befassen, noch folgenlos, wenn man ihn ignoriert. Zugleich gilt: Die kleinen Bußgelder kosten kein Startup das Leben. Mercedes zahlte in Spanien 3.000 € für mangelnde Kooperation mit der Aufsicht ([ETid-885](https://www.enforcementtracker.com/ETid-885), 2021); das interessiert einen Konzern erst, weil frühere Verstöße das nächste Bußgeld erhöhen.
```

Current English block 33:

```md
Die Neuerung der DSGVO gegenüber der Richtlinie von 1995 sind weniger die Grundsätze als die Sanktionen. Durchgesetzt wird sie von unabhängigen **Aufsichtsbehörden** (Art. 51 ff.) — in Deutschland je eine pro Bundesland plus die Bundesbeauftragte. Ihr Katalog an **Abhilfebefugnissen** (Art. 58 Abs. 2) reicht weit über Geld hinaus: Warnung vor geplanten Verarbeitungen, Verwarnung nach einem Verstoß, Anweisung, Anträgen betroffener Personen zu entsprechen, Anordnung von Berichtigung oder Löschung, Widerruf einer Zertifizierung, Aussetzung von Übermittlungen in Drittländer — und, als schärfstes Mittel, die vorübergehende oder endgültige **Beschränkung oder das Verbot** einer Verarbeitung. Für ein datengetriebenes Geschäftsmodell ist das die eigentliche Drohung; ein Bußgeld ist bezahlbar, ein Verarbeitungsverbot nicht.
```

Current English block 34:

```md
**Geldbußen** (Art. 83) sollen „wirksam, verhältnismäßig und abschreckend“ sein und kommen in zwei Stufen: bis 10 Mio. € oder 2 % des weltweiten Vorjahresumsatzes für Verstöße gegen Pflichten des Verantwortlichen (etwa Art. 25 Privacy by Design, Art. 33 Meldepflicht), bis 20 Mio. € oder 4 % für Verstöße gegen die Grundsätze, die Betroffenenrechte oder die Regeln zur Drittlandübermittlung — jeweils der höhere Betrag. Bei der Zumessung zählen unter anderem Art, Schwere und Dauer des Verstoßes, Vorsatz oder Fahrlässigkeit, ergriffene Abhilfemaßnahmen, frühere Verstöße und der Grad der Zusammenarbeit mit der Aufsicht.
```

Current English block 35:

```md
Neben der Aufsicht steht die Selbstregulierung: **Verhaltensregeln** (Art. 40) sind branchenspezifische Regelwerke, die Verbände ausarbeiten und von der Aufsicht genehmigen lassen. Wer sich daran hält, hat es leichter, die Rechenschaftspflicht aus Art. 5 Abs. 2 zu erfüllen.
```

Current English block 36:

```md
Zwei Missverständnisse sind damit erledigt: Datenschutz ist weder zu kompliziert, um sich damit zu befassen, noch folgenlos, wenn man ihn ignoriert. Zugleich gilt: Die kleinen Bußgelder kosten kein Startup das Leben. Mercedes zahlte in Spanien 3.000 € für mangelnde Kooperation mit der Aufsicht ([ETid-885](https://www.enforcementtracker.com/ETid-885), 2021); das interessiert einen Konzern erst, weil frühere Verstöße das nächste Bußgeld erhöhen.
```

### delete – German block `45`, `46`, `47`, `48` – English block(s) **45**, **46**, **47**, **48**

Current English block 45:

```md
## Rechtsrahmen der EU jenseits der DSGVO
```

Current English block 46:

```md
Die DSGVO schützt personenbezogene Daten. Seit 2020 verfolgt die EU mit der **Europäischen Datenstrategie** (Mitteilung der Kommission vom 19. Februar 2020) ein zweites, ergänzendes Ziel: Daten sollen innerhalb Europas leichter geteilt und genutzt werden können, und zwar unter europäischen Regeln. Daraus ist eine Reihe von Verordnungen entstanden, die nebeneinander gelten und die man auseinanderhalten sollte — grob nach drei Stoßrichtungen: Schutz der Betroffenen (DSGVO), Regeln für Märkte und Plattformen (DMA, DSA), Zugang zu und Teilen von Daten (DGA, Data Act) — und quer dazu der AI Act als Produktregulierung für KI-Systeme.
```

Current English block 47:

```md
- **KI-Verordnung / AI Act** ([Verordnung (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)): erster umfassender Rechtsrahmen für KI-Systeme, vorgeschlagen im April 2021, verabschiedet 2024. Der Ansatz ist risikobasiert — verbotene Praktiken (etwa Social Scoring durch Behörden), Hochrisiko-Anwendungen mit umfangreichen Pflichten (Medizin, Personalauswahl, Strafverfolgung), Transparenzpflichten für den Rest. Wer ein Modell in ein Produkt einbaut, wird hier selbst zum Adressaten.
- **Digital Markets Act (DMA)** ([Verordnung (EU) 2022/1925](https://eur-lex.europa.eu/eli/reg/2022/1925/oj)): Pflichten für sehr große Plattformen, die als *Gatekeeper* benannt sind — etwa Interoperabilität von Messengern und das Verbot, eigene Dienste zu bevorzugen.
- **Digital Services Act (DSA)** ([Verordnung (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)): Verantwortung für Inhalte, Meldewege, Transparenz von Empfehlungssystemen und Werbung.
- **Data Governance Act (DGA)** ([Verordnung (EU) 2022/868](https://eur-lex.europa.eu/eli/reg/2022/868/oj)): Rahmen für die Weiterverwendung geschützter Daten der öffentlichen Hand, für Datenvermittlungsdienste und für *Datenaltruismus* — also das freiwillige Bereitstellen eigener Daten für gemeinwohlorientierte Zwecke.
- **Data Act** ([Verordnung (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)): Zugang zu den Daten, die vernetzte Geräte erzeugen — wer eine Maschine kauft, soll auch an ihre Daten kommen und den Anbieter wechseln können.
```

Current English block 48:

```md
Für die tägliche Arbeit mit Daten bleibt die DSGVO der Maßstab; die übrigen Verordnungen entscheiden darüber, welche Daten überhaupt verfügbar sind und unter welchen Bedingungen ein Modell in Verkehr gebracht werden darf.
```

### replace – German block `50` – English block(s) **50**

What changed in the German:

```diff
- - [DSGVO in einfachen Worten](https://eu-datenschutz-grundverordnung.net/eu-dsgvo/) - [Volltext der DSGVO (EUR-Lex)](http://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679) - [Checkliste für technische & organisatorische Maßnahmen (BayLDA)](https://www.lda.bayern.de/media/checkliste/baylda_checkliste_tom.pdf) - [Film: *Democracy – Im Rausch der Daten* (bpb)](https://www.bpb.de/mediathek/254194/democracy-im-rausch-der-daten) [-- [GDPR Enforcement Tracker](https://www.enforcementtracker.com) der Kanzlei CMS: alle in diesem Kapitel genannten Bußgeldfälle mit Datum, Betrag und Quelle (CC BY-NC-SA 4.0) - Alfred Spector, Peter Norvig, Chris Wiggins, Jeannette M. Wing: *Data Science in Context* {cite}`spector2022` — Data Science ohne Formeln und ohne Code, dafür sehr gut über das, was um die Technik herum passiert; Ethik ist darin kein Anhang, sondern ein durchgehendes Thema.-]
+ - [DSGVO in einfachen Worten](https://eu-datenschutz-grundverordnung.net/eu-dsgvo/) - [Volltext der DSGVO (EUR-Lex)](http://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679) - [Checkliste für technische & organisatorische Maßnahmen (BayLDA)](https://www.lda.bayern.de/media/checkliste/baylda_checkliste_tom.pdf) - [Film: *Democracy – Im Rausch der Daten* (bpb)](https://www.bpb.de/mediathek/254194/democracy-im-rausch-der-daten)
```

German now reads:

```md
- [DSGVO in einfachen Worten](https://eu-datenschutz-grundverordnung.net/eu-dsgvo/)
- [Volltext der DSGVO (EUR-Lex)](http://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679)
- [Checkliste für technische & organisatorische Maßnahmen (BayLDA)](https://www.lda.bayern.de/media/checkliste/baylda_checkliste_tom.pdf)
- [Film: *Democracy – Im Rausch der Daten* (bpb)](https://www.bpb.de/mediathek/254194/democracy-im-rausch-der-daten)
```

Current English block 50:

```md
- [DSGVO in einfachen Worten](https://eu-datenschutz-grundverordnung.net/eu-dsgvo/)
- [Volltext der DSGVO (EUR-Lex)](http://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX:32016R0679)
- [Checkliste für technische & organisatorische Maßnahmen (BayLDA)](https://www.lda.bayern.de/media/checkliste/baylda_checkliste_tom.pdf)
- [Film: *Democracy – Im Rausch der Daten* (bpb)](https://www.bpb.de/mediathek/254194/democracy-im-rausch-der-daten)
- [GDPR Enforcement Tracker](https://www.enforcementtracker.com) der Kanzlei CMS: alle in diesem Kapitel genannten Bußgeldfälle mit Datum, Betrag und Quelle (CC BY-NC-SA 4.0)
- Alfred Spector, Peter Norvig, Chris Wiggins, Jeannette M. Wing: *Data Science in Context* {cite}`spector2022` — Data Science ohne Formeln und ohne Code, dafür sehr gut über das, was um die Technik herum passiert; Ethik ist darin kein Anhang, sondern ein durchgehendes Thema.
```


## kmeans.ipynb → kmeans.ipynb

### replace – German block `c0.1` – English block(s) **c0.1**

What changed in the German:

```diff
- [-[Vorlesungsaufzeichnung k-Means (VL 16)](https://media.hhu.de/channel/video/data-science-vl-16-k-means-2025/4d7a11c94e56a89a8bd8acdeb03a7a0d/167)-]
+ {+[Vortragsaufzeichnung zu k-Means](https://media.hhu.de/channel/video/data-science-vl-16-k-means-2025/4d7a11c94e56a89a8bd8acdeb03a7a0d/167)+}
```

German now reads:

```md
[Vortragsaufzeichnung zu k-Means](https://media.hhu.de/channel/video/data-science-vl-16-k-means-2025/4d7a11c94e56a89a8bd8acdeb03a7a0d/167)
```

Current English block c0.1:

```md
[Vorlesungsaufzeichnung k-Means (VL 16)](https://media.hhu.de/channel/video/data-science-vl-16-k-means-2025/4d7a11c94e56a89a8bd8acdeb03a7a0d/167)
```

### replace – German block `c1.4` – English block(s) **c1.4**

What changed in the German:

```diff
- | Aufgabe | Label | Beispiel in diesem Buch | Kapitel | |---|---|---|---| | Klassifikation | nominal, bekannt | Iris-Spezies aus vier Blattmaßen vorhersagen [-(Beispiel unten); Kleidungsstücke auf Fashion-MNIST erkennen-] | [-Modell-Auswahl,-] Kernel-Methoden | | Regression | stetig, bekannt | Hauspreis in Melbourne aus Lage und Größe vorhersagen | Regressionsanalyse | | Clustering | keins, wird erfunden | Iris-Instanzen ohne Spezies in drei Gruppen einteilen | dieses Kapitel, Expectation Maximization |
+ | Aufgabe | Label | Beispiel in diesem Buch | Kapitel | |---|---|---|---| | Klassifikation | nominal, bekannt | Iris-Spezies aus vier Blattmaßen vorhersagen | {+Modell-Auswahl (Fashion-MNIST),+} Kernel-Methoden | | Regression | stetig, bekannt | Hauspreis in Melbourne aus Lage und Größe vorhersagen | Regressionsanalyse | | Clustering | keins, wird erfunden | Iris-Instanzen ohne Spezies in drei Gruppen einteilen | dieses Kapitel, Expectation Maximization |
```

German now reads:

```md
| Aufgabe | Label | Beispiel in diesem Buch | Kapitel |
|---|---|---|---|
| Klassifikation | nominal, bekannt | Iris-Spezies aus vier Blattmaßen vorhersagen | Modell-Auswahl (Fashion-MNIST), Kernel-Methoden |
| Regression | stetig, bekannt | Hauspreis in Melbourne aus Lage und Größe vorhersagen | Regressionsanalyse |
| Clustering | keins, wird erfunden | Iris-Instanzen ohne Spezies in drei Gruppen einteilen | dieses Kapitel, Expectation Maximization |
```

Current English block c1.4:

```md
| Aufgabe | Label | Beispiel in diesem Buch | Kapitel |
|---|---|---|---|
| Klassifikation | nominal, bekannt | Iris-Spezies aus vier Blattmaßen vorhersagen (Beispiel unten); Kleidungsstücke auf Fashion-MNIST erkennen | Modell-Auswahl, Kernel-Methoden |
| Regression | stetig, bekannt | Hauspreis in Melbourne aus Lage und Größe vorhersagen | Regressionsanalyse |
| Clustering | keins, wird erfunden | Iris-Instanzen ohne Spezies in drei Gruppen einteilen | dieses Kapitel, Expectation Maximization |
```

### replace – German block `c5.0` – English block(s) **c5.0**

What changed in the German:

```diff
- Zunächst gehen wir in Pseudocode die Idee durch, am Beispiel der Spalten [-Blütenblattlänge und Blütenblattbreite der Iris-Daten, also-] in $\mathbb{R}^d$ mit $d=2$: 1. Wir legen ein $k$ fest, die Anzahl an Clustern. Im Beispiel Iris: 3 2. Wir legen $k$ verschiedene Punkte $c_1,\dots,c_k \in \mathbb{R}^d$ fest, die 'Zentroide'. Es ist möglich, sich auf Punkte aus dem Datensatz zu beschränken und diese Wahl einfach gleichverteilt zufällig zu treffen. 3. Zu jedem weiteren Punkt $x \in \mathbb{R}^d$ berechnen wir, welches Zentroid $c_i$ den geringsten Abstand hat und ordnen $x$ der Gruppe $i$ zu. 4. Dann updaten wir das $i$-te Zentroid als Mittelwert aller Punkte aus der Gruppe $i$. Wenn sich dabei nichts (bzw. wenig genug) ändert, sind wir fertig.
+ Zunächst gehen wir in Pseudocode die Idee durch, am Beispiel der {+ersten zwei+} Spalten {+Iris-Daten+} in $\mathbb{R}^d$ mit $d=2$: 1. Wir legen ein $k$ fest, die Anzahl an Clustern. Im Beispiel Iris: 3 2. Wir legen $k$ verschiedene Punkte $c_1,\dots,c_k \in \mathbb{R}^d$ fest, die 'Zentroide'. Es ist möglich, sich auf Punkte aus dem Datensatz zu beschränken und diese Wahl einfach gleichverteilt zufällig zu treffen. 3. Zu jedem weiteren Punkt $x \in \mathbb{R}^d$ berechnen wir, welches Zentroid $c_i$ den geringsten Abstand hat und ordnen $x$ der Gruppe $i$ zu. 4. Dann updaten wir das $i$-te Zentroid als Mittelwert aller Punkte aus der Gruppe $i$. Wenn sich dabei nichts (bzw. wenig genug) ändert, sind wir fertig.
```

German now reads:

```md
Zunächst gehen wir in Pseudocode die Idee durch, am Beispiel der ersten zwei Spalten Iris-Daten in $\mathbb{R}^d$ mit $d=2$:
1. Wir legen ein $k$ fest, die Anzahl an Clustern. Im Beispiel Iris: 3
2. Wir legen $k$ verschiedene Punkte $c_1,\dots,c_k \in \mathbb{R}^d$ fest, die 'Zentroide'. Es ist möglich, sich auf Punkte aus dem Datensatz zu beschränken und diese Wahl einfach gleichverteilt zufällig zu treffen.
3. Zu jedem weiteren Punkt $x \in \mathbb{R}^d$ berechnen wir, welches Zentroid $c_i$ den geringsten Abstand hat und ordnen $x$ der Gruppe $i$ zu.
4. Dann updaten wir das $i$-te Zentroid als Mittelwert aller Punkte aus der Gruppe $i$. Wenn sich dabei nichts (bzw. wenig genug) ändert, sind wir fertig.
```

Current English block c5.0:

```md
Zunächst gehen wir in Pseudocode die Idee durch, am Beispiel der Spalten Blütenblattlänge und Blütenblattbreite der Iris-Daten, also in $\mathbb{R}^d$ mit $d=2$:
1. Wir legen ein $k$ fest, die Anzahl an Clustern. Im Beispiel Iris: 3
2. Wir legen $k$ verschiedene Punkte $c_1,\dots,c_k \in \mathbb{R}^d$ fest, die 'Zentroide'. Es ist möglich, sich auf Punkte aus dem Datensatz zu beschränken und diese Wahl einfach gleichverteilt zufällig zu treffen.
3. Zu jedem weiteren Punkt $x \in \mathbb{R}^d$ berechnen wir, welches Zentroid $c_i$ den geringsten Abstand hat und ordnen $x$ der Gruppe $i$ zu.
4. Dann updaten wir das $i$-te Zentroid als Mittelwert aller Punkte aus der Gruppe $i$. Wenn sich dabei nichts (bzw. wenig genug) ändert, sind wir fertig.
```

### replace – German block `c29.2` – English block(s) **c29.2**

What changed in the German:

```diff
- * Die durchschnittliche Laufzeitkomplexität ist in $O(k*n*T)$ mit $n$ der Samplegröße und $T$ die Anzahl an Iterationen. * Die Worst-Case-Komplexität ist in $O(n^{(k+2/d)})$ wobei $d$ die Anzahl Variablen (die Dimension) ist. [Arthur, Vassilvitskii: ‘How slow is the k-means method?’, 2006](https://theory.stanford.edu/~sergei/papers/kMeans-socg.pdf) * Was passiert theoretisch? Die sogenannte **Trägheit** (inertia), das ist die Summe der *quadrierten* Abstände aller Punkte zu ihren nächsten Zentroiden, $J(c_1,\dots,c_k) = \sum_i \min_j \lVert x_i - c_j \rVert^2$, wird minimiert. Das zeigt auch das größte Problem auf: wenn die Cluster nicht konvex und homogen sind, ist das eine weniger sinnvolle Optimierungsgröße. Hier greift der Fluch der Dimensionalität (curse of dimensionality): in hochdimensionalen Räumen verhalten sich Abstände unintuitiv, z.B. sind in einer [-Kugel-] gleichverteilte Punkte mehr nahe am Rand als nahe der Mitte. Wieder ein Grund mehr, um Hauptachsentransformation zu lernen. * Variante **bisecting k-means**: Zunächst 2-means, dann wird iterativ einer der größten Cluster aufgeteilt mit 2-means usw. bis insgesamt k Cluster da sind. * Variante **mini-batch k-means**: Ein Kompromiss aus unserer ersten Variante (mit der Animation) und der letzten Variante. Hat große Vorteile bei online-Datenverarbeitung (streaming) und generell großen Datenmengen. * Die Voraussetzung, damit k-means-Verfahren erfolgreich sein können, sind Daten die in Cluster von etwa Ellipsoider Form mit ähnlicher Varianz fallen. [Beispiele, wo es schief gehen kann, sind in der scikit-learn-Dokumentation geplottet](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py). * Das **Elbow Kriterium** ist nicht sinnvoll. Details und Alternativen werden seit Jahren in der Literatur diskutiert {cite}`Schubert2023`.
+ * Die durchschnittliche Laufzeitkomplexität ist in $O(k*n*T)$ mit $n$ der Samplegröße und $T$ die Anzahl an Iterationen. * Die Worst-Case-Komplexität ist in $O(n^{(k+2/d)})$ wobei $d$ die Anzahl Variablen (die Dimension) ist. [Arthur, Vassilvitskii: ‘How slow is the k-means method?’, 2006](https://theory.stanford.edu/~sergei/papers/kMeans-socg.pdf) * Was passiert theoretisch? Die sogenannte **Trägheit** (inertia), das ist die Summe der *quadrierten* Abstände aller Punkte zu ihren nächsten Zentroiden, $J(c_1,\dots,c_k) = \sum_i \min_j \lVert x_i - c_j \rVert^2$, wird minimiert. Das zeigt auch das größte Problem auf: wenn die Cluster nicht konvex und homogen sind, ist das eine weniger sinnvolle Optimierungsgröße. Hier greift der Fluch der Dimensionalität (curse of dimensionality): in hochdimensionalen Räumen verhalten sich Abstände unintuitiv, z.B. sind in einer {+Sphäre+} gleichverteilte Punkte mehr nahe am Rand als nahe der Mitte. Wieder ein Grund mehr, um Hauptachsentransformation zu lernen. * Variante **bisecting k-means**: Zunächst 2-means, dann wird iterativ einer der größten Cluster aufgeteilt mit 2-means usw. bis insgesamt k Cluster da sind. * Variante **mini-batch k-means**: Ein Kompromiss aus unserer ersten Variante (mit der Animation) und der letzten Variante. Hat große Vorteile bei online-Datenverarbeitung (streaming) und generell großen Datenmengen. * Die Voraussetzung, damit k-means-Verfahren erfolgreich sein können, sind Daten die in Cluster von etwa Ellipsoider Form mit ähnlicher Varianz fallen. [Beispiele, wo es schief gehen kann, sind in der scikit-learn-Dokumentation geplottet](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py). * Das **Elbow Kriterium** ist nicht sinnvoll. Details und Alternativen werden seit Jahren in der Literatur diskutiert {cite}`Schubert2023`.
```

German now reads:

```md
* Die durchschnittliche Laufzeitkomplexität ist in $O(k*n*T)$ mit $n$ der Samplegröße und $T$ die Anzahl an Iterationen.
* Die Worst-Case-Komplexität ist in $O(n^{(k+2/d)})$ wobei $d$ die Anzahl Variablen (die Dimension) ist. [Arthur, Vassilvitskii: ‘How slow is the k-means method?’, 2006](https://theory.stanford.edu/~sergei/papers/kMeans-socg.pdf)
* Was passiert theoretisch?
  Die sogenannte **Trägheit** (inertia), das ist die Summe der *quadrierten* Abstände aller Punkte zu ihren nächsten Zentroiden, $J(c_1,\dots,c_k) = \sum_i \min_j \lVert x_i - c_j \rVert^2$, wird minimiert. Das zeigt auch das größte Problem auf: wenn die Cluster nicht konvex und homogen sind, ist das eine weniger sinnvolle Optimierungsgröße. Hier greift der Fluch der Dimensionalität (curse of dimensionality): in hochdimensionalen Räumen verhalten sich Abstände unintuitiv, z.B. sind in einer Sphäre gleichverteilte Punkte mehr nahe am Rand als nahe der Mitte. Wieder ein Grund mehr, um Hauptachsentransformation zu lernen.
* Variante **bisecting k-means**:
  Zunächst 2-means, dann wird iterativ einer der größten Cluster aufgeteilt mit 2-means usw. bis insgesamt k Cluster da sind.
* Variante **mini-batch k-means**:
  Ein Kompromiss aus unserer ersten Variante (mit der Animation) und der letzten Variante. Hat große Vorteile bei online-Datenverarbeitung (streaming) und generell großen Datenmengen.
* Die Voraussetzung, damit k-means-Verfahren erfolgreich sein können, sind Daten die in Cluster von etwa Ellipsoider Form mit ähnlicher Varianz fallen. [Beispiele, wo es schief gehen kann, sind in der scikit-learn-Dokumentation geplottet](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py).
* Das **Elbow Kriterium** ist nicht sinnvoll. Details und Alternativen werden seit Jahren in der Literatur diskutiert {cite}`Schubert2023`.
```

Current English block c29.2:

```md
* Die durchschnittliche Laufzeitkomplexität ist in $O(k*n*T)$ mit $n$ der Samplegröße und $T$ die Anzahl an Iterationen.
* Die Worst-Case-Komplexität ist in $O(n^{(k+2/d)})$ wobei $d$ die Anzahl Variablen (die Dimension) ist. [Arthur, Vassilvitskii: ‘How slow is the k-means method?’, 2006](https://theory.stanford.edu/~sergei/papers/kMeans-socg.pdf)
* Was passiert theoretisch?
  Die sogenannte **Trägheit** (inertia), das ist die Summe der *quadrierten* Abstände aller Punkte zu ihren nächsten Zentroiden, $J(c_1,\dots,c_k) = \sum_i \min_j \lVert x_i - c_j \rVert^2$, wird minimiert. Das zeigt auch das größte Problem auf: wenn die Cluster nicht konvex und homogen sind, ist das eine weniger sinnvolle Optimierungsgröße. Hier greift der Fluch der Dimensionalität (curse of dimensionality): in hochdimensionalen Räumen verhalten sich Abstände unintuitiv, z.B. sind in einer Kugel gleichverteilte Punkte mehr nahe am Rand als nahe der Mitte. Wieder ein Grund mehr, um Hauptachsentransformation zu lernen.
* Variante **bisecting k-means**:
  Zunächst 2-means, dann wird iterativ einer der größten Cluster aufgeteilt mit 2-means usw. bis insgesamt k Cluster da sind.
* Variante **mini-batch k-means**:
  Ein Kompromiss aus unserer ersten Variante (mit der Animation) und der letzten Variante. Hat große Vorteile bei online-Datenverarbeitung (streaming) und generell großen Datenmengen.
* Die Voraussetzung, damit k-means-Verfahren erfolgreich sein können, sind Daten die in Cluster von etwa Ellipsoider Form mit ähnlicher Varianz fallen. [Beispiele, wo es schief gehen kann, sind in der scikit-learn-Dokumentation geplottet](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py).
* Das **Elbow Kriterium** ist nicht sinnvoll. Details und Alternativen werden seit Jahren in der Literatur diskutiert {cite}`Schubert2023`.
```

### replace – German block `c31` – English block(s) **c31**

What changed in the German:

```diff
- from sklearn.cluster import KMeans # Ist natürlich viel schneller, weil mit C parallelisiert: kmeans_result = KMeans(n_clusters=3).fit(iris.data) print(kmeans_result.cluster_centers_) print(kmeans_result.labels_) print(iris.target) from sklearn import metrics [-print("NMI-] = [-I(P;C) / mean(H(P), H(C)) zwischen Vorhersage P und Klasse C:",-] metrics.normalized_mutual_info_score(iris.target, kmeans_result.labels_))
+ from sklearn.cluster import KMeans # Ist natürlich viel schneller, weil mit C parallelisiert: kmeans_result = KMeans(n_clusters=3).fit(iris.data) print(kmeans_result.cluster_centers_) print(kmeans_result.labels_) print(iris.target) from sklearn import metrics {+print("P+} = {+Predicted, C = Class, H(P, C)/mean(H(P),H(C)) =",+} metrics.normalized_mutual_info_score(iris.target, kmeans_result.labels_))
```

German now reads:

```md
from sklearn.cluster import KMeans
# Ist natürlich viel schneller, weil mit C parallelisiert:
kmeans_result = KMeans(n_clusters=3).fit(iris.data)
print(kmeans_result.cluster_centers_)
print(kmeans_result.labels_)
print(iris.target)
from sklearn import metrics
print("P = Predicted, C = Class, H(P, C)/mean(H(P),H(C)) =",
      metrics.normalized_mutual_info_score(iris.target, kmeans_result.labels_))
```

Current English block c31:

```md
from sklearn.cluster import KMeans
# Ist natürlich viel schneller, weil mit C parallelisiert:
kmeans_result = KMeans(n_clusters=3).fit(iris.data)
print(kmeans_result.cluster_centers_)
print(kmeans_result.labels_)
print(iris.target)
from sklearn import metrics
print("NMI = I(P;C) / mean(H(P), H(C)) zwischen Vorhersage P und Klasse C:",
      metrics.normalized_mutual_info_score(iris.target, kmeans_result.labels_))
```


## statistische-modelle.md → statistical-models.md

### delete – German block `1` – English block(s) **1**

Current English block 1:

```md
[Vorlesungsaufzeichnung Statistische Modelle und Maximum Likelihood (VL 17)](https://media.hhu.de/channel/video/data-science-vl-17-maximum-likelihood-2025/edefe4fe4cf095537fbe80bf1a401b21/167)
```

### replace – German block `11` – English block(s) **11**

What changed in the German:

```diff
- Wenn man statistische Modelle formal definiert hat, kann man auch sehr gut über Konfidenzintervalle und Hypothesentests sprechen, was [-das Kapitel [Statistische Tests](statistische-tests.md) erledigt.-] Konfidenzintervalle erweitern des Ansatz des bloßen Schätzens einer Statistik um die Information, welchen Fehlerbereich man dieser Schätzung beimisst. Hypothesentests erweitern den Ansatz darum, schließlich zu Entscheidungen zu kommen. Bei der Diskussion um Hypothesentests ist es unvermeidlich, auch über den problematischen Begriff der **Signifikanz** zu sprechen. Aber eins nach dem anderen!
+ Wenn man statistische Modelle formal definiert hat, kann man auch sehr gut über Konfidenzintervalle und Hypothesentests sprechen, was {+wir dann gleich im Anschluss erledigen.+} Konfidenzintervalle erweitern des Ansatz des bloßen Schätzens einer Statistik um die Information, welchen Fehlerbereich man dieser Schätzung beimisst. Hypothesentests erweitern den Ansatz darum, schließlich zu Entscheidungen zu kommen. Bei der Diskussion um Hypothesentests ist es unvermeidlich, auch über den problematischen Begriff der **Signifikanz** zu sprechen. Aber eins nach dem anderen!
```

German now reads:

```md
Wenn man statistische Modelle formal definiert hat, kann man auch sehr gut über Konfidenzintervalle und Hypothesentests sprechen, was wir dann gleich im Anschluss erledigen. Konfidenzintervalle erweitern des Ansatz des bloßen Schätzens einer Statistik um die Information, welchen Fehlerbereich man dieser Schätzung beimisst. Hypothesentests erweitern den Ansatz darum, schließlich zu Entscheidungen zu kommen. Bei der Diskussion um Hypothesentests ist es unvermeidlich, auch über den problematischen Begriff der **Signifikanz** zu sprechen. Aber eins nach dem anderen!
```

Current English block 11:

```md
Wenn man statistische Modelle formal definiert hat, kann man auch sehr gut über Konfidenzintervalle und Hypothesentests sprechen, was das Kapitel [Statistische Tests](statistical-tests.md) erledigt. Konfidenzintervalle erweitern des Ansatz des bloßen Schätzens einer Statistik um die Information, welchen Fehlerbereich man dieser Schätzung beimisst. Hypothesentests erweitern den Ansatz darum, schließlich zu Entscheidungen zu kommen. Bei der Diskussion um Hypothesentests ist es unvermeidlich, auch über den problematischen Begriff der **Signifikanz** zu sprechen. Aber eins nach dem anderen!
```

### replace – German block `25` – English block(s) **25**

What changed in the German:

```diff
- Wenn die Stichprobenmenge $\mathcal{X}$ diskret ist (höchstens abzählbar), und $\mathcal{F} = [-\mathcal{P}(\mathcal{X})$,-] nennt man das Modell **diskret** und in dem Fall haben alle $P_\theta$ eine Zähldichte $p_\theta$, d.h. $p_\theta(x) = [-P_\theta(\{x\})$.-]
+ Wenn die Stichprobenmenge $\mathcal{X}$ diskret ist (höchstens abzählbar), und $\mathcal{F} = {+\mathcal{P}(X)$,+} nennt man das Modell **diskret** und in dem Fall haben alle $P_\theta$ eine Zähldichte $p_\theta$, d.h. $p_\theta(x) = {+P_\theta({x})$.+}
```

German now reads:

```md
Wenn die Stichprobenmenge $\mathcal{X}$ diskret ist (höchstens abzählbar), und $\mathcal{F} = \mathcal{P}(X)$, nennt man das Modell **diskret** und in dem Fall haben alle $P_\theta$ eine Zähldichte $p_\theta$, d.h. $p_\theta(x) = P_\theta({x})$.
```

Current English block 25:

```md
Wenn die Stichprobenmenge $\mathcal{X}$ diskret ist (höchstens abzählbar), und $\mathcal{F} = \mathcal{P}(\mathcal{X})$, nennt man das Modell **diskret** und in dem Fall haben alle $P_\theta$ eine Zähldichte $p_\theta$, d.h. $p_\theta(x) = P_\theta(\{x\})$.
```

### replace – German block `35` – English block(s) **35**

What changed in the German:

```diff
- Wir modellieren einen Würfelwurf eines potentiell unfairen Würfels mit einem diskreten Modell: $\mathcal{X} = \{1,\dots,6\}$ und $\Theta = \Delta_6$, die Menge aller möglichen diskreten Verteilungen auf einer sechselementigen Menge (geschrieben als Wahrscheinlichkeitsvektoren in $\mathbb{R}^6$), und $P_\theta(k) = \theta_k$. Konkret für $\theta = [-(\theta_1,\dots,\theta_6)$-] ist also die Wahrscheinlichkeit, eine $6$ zu werfen im Modell mit Parameter $\theta$ gegeben durch $P_\theta(6) = \theta_6$.
+ Wir modellieren einen Würfelwurf eines potentiell unfairen Würfels mit einem diskreten Modell: $\mathcal{X} = \{1,\dots,6\}$ und $\Theta = \Delta_6$, die Menge aller möglichen diskreten Verteilungen auf einer sechselementigen Menge (geschrieben als Wahrscheinlichkeitsvektoren in $\mathbb{R}^6$), und $P_\theta(k) = \theta_k$. Konkret für $\theta = {+(\theta_1,\dots,\theta_n)$+} ist also die Wahrscheinlichkeit, eine $6$ zu werfen im Modell mit Parameter $\theta$ gegeben durch $P_\theta(6) = \theta_6$.
```

German now reads:

```md
Wir modellieren einen Würfelwurf eines potentiell unfairen Würfels mit einem diskreten Modell: $\mathcal{X} = \{1,\dots,6\}$ und $\Theta = \Delta_6$, die Menge aller möglichen diskreten Verteilungen auf einer sechselementigen Menge (geschrieben als Wahrscheinlichkeitsvektoren in $\mathbb{R}^6$), und $P_\theta(k) = \theta_k$. Konkret für $\theta = (\theta_1,\dots,\theta_n)$ ist also die Wahrscheinlichkeit, eine $6$ zu werfen im Modell mit Parameter $\theta$ gegeben durch $P_\theta(6) = \theta_6$.
```

Current English block 35:

```md
Wir modellieren einen Würfelwurf eines potentiell unfairen Würfels mit einem diskreten Modell: $\mathcal{X} = \{1,\dots,6\}$ und $\Theta = \Delta_6$, die Menge aller möglichen diskreten Verteilungen auf einer sechselementigen Menge (geschrieben als Wahrscheinlichkeitsvektoren in $\mathbb{R}^6$), und $P_\theta(k) = \theta_k$. Konkret für $\theta = (\theta_1,\dots,\theta_6)$ ist also die Wahrscheinlichkeit, eine $6$ zu werfen im Modell mit Parameter $\theta$ gegeben durch $P_\theta(6) = \theta_6$.
```

### replace – German block `41` – English block(s) **41**

What changed in the German:

```diff
- Wir können auch modellieren, ob beim zweifachen Wurf ein Pasch gewürfelt wurde oder nicht - und somit $\mathcal{X} = \{\text{Pasch}, \text{Keinpasch}\}$ als Stichprobenraum betrachten. Dabei können wir einfach den Parameterraum $\Theta = \Delta_6$ beibehalten, das ist ein mögliches statistisches Modell. Wir sehen allerdings, dass [-$P_\theta^{\otimes 2}(k,k)-] = \theta_k^2$ ist, also ist $P_\theta(\text{Pasch}) = \sum_{k=1}^6 \theta_k^2$, also genügt uns eigentlich der Parameter $s = \sum_{k=1}^6 \theta_k^2$ und wir könnten uns also einen kleineren Parameterraum vorstellen. Dann stellt sich allerdings die Frage, welche Verteilung $P_s$ wir dem Parameter $s$ zuordnen wollen. Eine konkret sinnvolle Wahl ist dabei die Verteilung $\theta$ mit maximaler Entropie, also eine Verteilung möglichst nah an der Gleichverteilung. Das wird nicht eindeutig, weil Permutationen von $\{1,\dots,6\}$ den Parameter $s$ und die Entropie $H(\theta)$ nicht ändern. Will man trotzdem ein irgendwie kanonisches Modell wählen, kann man z.B. eine Anordnung auf den $\theta$ fordern, also $\theta_k \geq \theta_{k+1}$. Wir sehen hier also: ein 'zu großer' Parameterraum ist manchmal das einfachere Modell.
+ Wir können auch modellieren, ob beim zweifachen Wurf ein Pasch gewürfelt wurde oder nicht - und somit $\mathcal{X} = \{\text{Pasch}, \text{Keinpasch}\}$ als Stichprobenraum betrachten. Dabei können wir einfach den Parameterraum $\Theta = \Delta_6$ beibehalten, das ist ein mögliches statistisches Modell. Wir sehen allerdings, dass {+$P_\theta^{\otimes}(k,k)+} = \theta_k^2$ ist, also ist $P_\theta(\text{Pasch}) = \sum_{k=1}^6 \theta_k^2$, also genügt uns eigentlich der Parameter $s = \sum_{k=1}^6 \theta_k^2$ und wir könnten uns also einen kleineren Parameterraum vorstellen. Dann stellt sich allerdings die Frage, welche Verteilung $P_s$ wir dem Parameter $s$ zuordnen wollen. Eine konkret sinnvolle Wahl ist dabei die Verteilung $\theta$ mit maximaler Entropie, also eine Verteilung möglichst nah an der Gleichverteilung. Das wird nicht eindeutig, weil Permutationen von $\{1,\dots,6\}$ den Parameter $s$ und die Entropie $H(\theta)$ nicht ändern. Will man trotzdem ein irgendwie kanonisches Modell wählen, kann man z.B. eine Anordnung auf den $\theta$ fordern, also $\theta_k \geq \theta_{k+1}$. Wir sehen hier also: ein 'zu großer' Parameterraum ist manchmal das einfachere Modell.
```

German now reads:

```md
Wir können auch modellieren, ob beim zweifachen Wurf ein Pasch gewürfelt wurde oder nicht - und somit $\mathcal{X} = \{\text{Pasch}, \text{Keinpasch}\}$ als Stichprobenraum betrachten.
Dabei können wir einfach den Parameterraum $\Theta = \Delta_6$ beibehalten, das ist ein mögliches statistisches Modell.
Wir sehen allerdings, dass $P_\theta^{\otimes}(k,k) = \theta_k^2$ ist, also ist $P_\theta(\text{Pasch}) = \sum_{k=1}^6 \theta_k^2$,
also genügt uns eigentlich der Parameter $s = \sum_{k=1}^6 \theta_k^2$ und wir könnten uns also einen kleineren Parameterraum vorstellen.
Dann stellt sich allerdings die Frage, welche Verteilung $P_s$ wir dem Parameter $s$ zuordnen wollen. Eine konkret sinnvolle Wahl ist dabei die Verteilung $\theta$ mit maximaler Entropie, also eine Verteilung möglichst nah an der Gleichverteilung. Das wird nicht eindeutig, weil Permutationen von $\{1,\dots,6\}$ den Parameter $s$ und die Entropie $H(\theta)$ nicht ändern. Will man trotzdem ein irgendwie kanonisches Modell wählen, kann man z.B. eine Anordnung auf den $\theta$ fordern, also $\theta_k \geq \theta_{k+1}$.
Wir sehen hier also: ein 'zu großer' Parameterraum ist manchmal das einfachere Modell.
```

Current English block 41:

```md
Wir können auch modellieren, ob beim zweifachen Wurf ein Pasch gewürfelt wurde oder nicht - und somit $\mathcal{X} = \{\text{Pasch}, \text{Keinpasch}\}$ als Stichprobenraum betrachten.
Dabei können wir einfach den Parameterraum $\Theta = \Delta_6$ beibehalten, das ist ein mögliches statistisches Modell.
Wir sehen allerdings, dass $P_\theta^{\otimes 2}(k,k) = \theta_k^2$ ist, also ist $P_\theta(\text{Pasch}) = \sum_{k=1}^6 \theta_k^2$,
also genügt uns eigentlich der Parameter $s = \sum_{k=1}^6 \theta_k^2$ und wir könnten uns also einen kleineren Parameterraum vorstellen.
Dann stellt sich allerdings die Frage, welche Verteilung $P_s$ wir dem Parameter $s$ zuordnen wollen. Eine konkret sinnvolle Wahl ist dabei die Verteilung $\theta$ mit maximaler Entropie, also eine Verteilung möglichst nah an der Gleichverteilung. Das wird nicht eindeutig, weil Permutationen von $\{1,\dots,6\}$ den Parameter $s$ und die Entropie $H(\theta)$ nicht ändern. Will man trotzdem ein irgendwie kanonisches Modell wählen, kann man z.B. eine Anordnung auf den $\theta$ fordern, also $\theta_k \geq \theta_{k+1}$.
Wir sehen hier also: ein 'zu großer' Parameterraum ist manchmal das einfachere Modell.
```

### replace – German block `75` – English block(s) **75**

What changed in the German:

```diff
- Eine Folge von Schätzern $T_n \colon \mathcal{X}^n \to \Sigma$ für $\tau$ in $n$-fachen Produktmodellen heißt **konsistent** wenn für $n\to\infty$ der Schätzer stochastisch gegen $\tau$ konvergiert: [-$T_n-] \xrightarrow{P_\theta} \tau(\theta)$. Stochastische Konvergenz (auch: Konvergenz in Wahrscheinlichkeit) heißt $\forall \epsilon > 0 : \lim_{n\to\infty} P(|T_n - \tau(\theta)| > \epsilon) = 0$.
+ Eine Folge von Schätzern $T_n \colon \mathcal{X}^n \to \Sigma$ für $\tau$ in $n$-fachen Produktmodellen heißt **konsistent** wenn für $n\to\infty$ der Schätzer stochastisch gegen $\tau$ konvergiert: {+$\lim_{n\to\infty} T_n+} \xrightarrow{P_\theta} \tau(\theta)$. Stochastische Konvergenz (auch: Konvergenz in Wahrscheinlichkeit) heißt $\forall \epsilon > 0 : \lim_{n\to\infty} P(|T_n - \tau(\theta)| > \epsilon) = 0$.
```

German now reads:

```md
Eine Folge von Schätzern $T_n \colon \mathcal{X}^n \to \Sigma$ für $\tau$ in $n$-fachen Produktmodellen heißt **konsistent** wenn für $n\to\infty$
der Schätzer stochastisch gegen $\tau$ konvergiert: $\lim_{n\to\infty} T_n \xrightarrow{P_\theta} \tau(\theta)$. Stochastische Konvergenz (auch: Konvergenz in Wahrscheinlichkeit) heißt $\forall \epsilon > 0 : \lim_{n\to\infty} P(|T_n - \tau(\theta)| > \epsilon) = 0$.
```

Current English block 75:

```md
Eine Folge von Schätzern $T_n \colon \mathcal{X}^n \to \Sigma$ für $\tau$ in $n$-fachen Produktmodellen heißt **konsistent** wenn für $n\to\infty$
der Schätzer stochastisch gegen $\tau$ konvergiert: $T_n \xrightarrow{P_\theta} \tau(\theta)$. Stochastische Konvergenz (auch: Konvergenz in Wahrscheinlichkeit) heißt $\forall \epsilon > 0 : \lim_{n\to\infty} P(|T_n - \tau(\theta)| > \epsilon) = 0$.
```

### replace – German block `95` – English block(s) **95**

What changed in the German:

```diff
- Im Allgemeinen ist es sehr schwer, gleichmäßig beste erwartungstreue Schätzer zu bestimmen (es gibt sie im Allgemeinen nicht). Ausblick: Die [-*Cramér-Rao-Ungleichung*-] für *reguläre* statistische Modelle liefert eine Abschätzung der Varianz eines Schätzers durch die *Fisher-Information* (eine Größe, die sich auch aus der relativen Entropie berechnen lässt) und erlaubt so, gleichmäßig beste Schätzer daran zu erkennen, dass sie diese Varianzschranke nicht überschreiten. Für einen erwartungstreuen Schätzer $T$ eines reellen Parameters $\theta$ lautet sie
+ Im Allgemeinen ist es sehr schwer, gleichmäßig beste erwartungstreue Schätzer zu bestimmen (es gibt sie im Allgemeinen nicht). Ausblick: Die {+*Cramer-Rao-Ungleichung*+} für *reguläre* statistische Modelle liefert eine Abschätzung der Varianz eines Schätzers durch die *Fisher-Information* (eine Größe, die sich auch aus der relativen Entropie berechnen lässt) und erlaubt so, gleichmäßig beste Schätzer daran zu erkennen, dass sie diese Varianzschranke nicht überschreiten. Für einen erwartungstreuen Schätzer $T$ eines reellen Parameters $\theta$ lautet sie
```

German now reads:

```md
Im Allgemeinen ist es sehr schwer, gleichmäßig beste erwartungstreue Schätzer zu bestimmen (es gibt sie im Allgemeinen nicht). Ausblick: Die *Cramer-Rao-Ungleichung* für *reguläre* statistische Modelle liefert eine Abschätzung der Varianz eines Schätzers durch die *Fisher-Information* (eine Größe, die sich auch aus der relativen Entropie berechnen lässt) und erlaubt so, gleichmäßig beste Schätzer daran zu erkennen, dass sie diese Varianzschranke nicht überschreiten. Für einen erwartungstreuen Schätzer $T$ eines reellen Parameters $\theta$ lautet sie
```

Current English block 95:

```md
Im Allgemeinen ist es sehr schwer, gleichmäßig beste erwartungstreue Schätzer zu bestimmen (es gibt sie im Allgemeinen nicht). Ausblick: Die *Cramér-Rao-Ungleichung* für *reguläre* statistische Modelle liefert eine Abschätzung der Varianz eines Schätzers durch die *Fisher-Information* (eine Größe, die sich auch aus der relativen Entropie berechnen lässt) und erlaubt so, gleichmäßig beste Schätzer daran zu erkennen, dass sie diese Varianzschranke nicht überschreiten. Für einen erwartungstreuen Schätzer $T$ eines reellen Parameters $\theta$ lautet sie
```

### replace – German block `103` – English block(s) **103**

What changed in the German:

```diff
- Wenn wir also Daten $x$ gegeben haben, drückt die Likelihood-Funktion zu $x$ für jeden Parameter $\theta$ aus, wie die Wahrscheinlichkeitsdichte an der Stelle $x$ von $P_\theta$ ausfällt. Ist die Dichte groß, so ist $x$ eine Beobachtung, die unter dem Parameter $\theta$ wahrscheinlich ist. Ist die Dichte klein, so ist $x$ unter $\theta$ unwahrscheinlich. Zur Erinnerung: Wenn wir die Hypothese $H = ( \theta$ ist der wahre Parameter $)$ haben, und $D=x$ (für Daten) schreiben, so ist $P(D|H) = L_x(\theta) = f_\theta(x)$ die Likelihood (vgl. den Satz von [-Bayes, Fassung 3, im Kapitel [Kovarianz und Abhängigkeit](kovarianz.md)).-]
+ Wenn wir also Daten $x$ gegeben haben, drückt die Likelihood-Funktion zu $x$ für jeden Parameter $\theta$ aus, wie die Wahrscheinlichkeitsdichte an der Stelle $x$ von $P_\theta$ ausfällt. Ist die Dichte groß, so ist $x$ eine Beobachtung, die unter dem Parameter $\theta$ wahrscheinlich ist. Ist die Dichte klein, so ist $x$ unter $\theta$ unwahrscheinlich. Zur Erinnerung: Wenn wir die Hypothese $H = ( \theta$ ist der wahre Parameter $)$ haben, und $D=x$ (für Daten) schreiben, so ist $P(D|H) = L_x(\theta) = f_\theta(x)$ die Likelihood (vgl. {+Abschnitt über+} den Satz von {+Bayes).+}
```

German now reads:

```md
Wenn wir also Daten $x$ gegeben haben, drückt die Likelihood-Funktion zu $x$ für jeden Parameter $\theta$ aus, wie die Wahrscheinlichkeitsdichte an der Stelle $x$ von $P_\theta$ ausfällt. Ist die Dichte groß, so ist $x$ eine Beobachtung, die unter dem Parameter $\theta$ wahrscheinlich ist. Ist die Dichte klein, so ist $x$ unter $\theta$ unwahrscheinlich. Zur Erinnerung: Wenn wir die Hypothese $H = ( \theta$ ist der wahre Parameter $)$ haben, und $D=x$ (für Daten) schreiben, so ist $P(D|H) = L_x(\theta) = f_\theta(x)$ die Likelihood (vgl. Abschnitt über den Satz von Bayes).
```

Current English block 103:

```md
Wenn wir also Daten $x$ gegeben haben, drückt die Likelihood-Funktion zu $x$ für jeden Parameter $\theta$ aus, wie die Wahrscheinlichkeitsdichte an der Stelle $x$ von $P_\theta$ ausfällt. Ist die Dichte groß, so ist $x$ eine Beobachtung, die unter dem Parameter $\theta$ wahrscheinlich ist. Ist die Dichte klein, so ist $x$ unter $\theta$ unwahrscheinlich. Zur Erinnerung: Wenn wir die Hypothese $H = ( \theta$ ist der wahre Parameter $)$ haben, und $D=x$ (für Daten) schreiben, so ist $P(D|H) = L_x(\theta) = f_\theta(x)$ die Likelihood (vgl. den Satz von Bayes, Fassung 3, im Kapitel [Kovarianz und Abhängigkeit](covariance.md)).
```

### replace – German block `122` – English block(s) **122**

What changed in the German:

```diff
- Anstatt die Likelihood von $x$ über alle möglichen $\theta$ zu maximieren, kann man auch den Logarithmus der Likelihood bilden, die sogenannte **log-Likelihood** $\log \rho(x,\theta)$ und diese maximieren. [-Weil-] der Logarithmus [-streng monoton wächst, haben Likelihood und-] log-Likelihood [-dieselben Maximalstellen.-]
+ Anstatt die Likelihood von $x$ über alle möglichen $\theta$ zu maximieren, kann man auch den Logarithmus der Likelihood bilden, die sogenannte **log-Likelihood** $\log \rho(x,\theta)$ und diese maximieren. {+Wegen+} der {+Konkavität des+} Logarithmus {+ist ein Maximum der+} log-Likelihood {+auch ein Maximum der Likelihood.+}
```

German now reads:

```md
Anstatt die Likelihood von $x$ über alle möglichen $\theta$ zu maximieren, kann man auch den Logarithmus der Likelihood bilden, die sogenannte **log-Likelihood** $\log \rho(x,\theta)$ und diese maximieren. Wegen der Konkavität des Logarithmus ist ein Maximum der log-Likelihood auch ein Maximum der Likelihood.
```

Current English block 122:

```md
Anstatt die Likelihood von $x$ über alle möglichen $\theta$ zu maximieren, kann man auch den Logarithmus der Likelihood bilden, die sogenannte **log-Likelihood** $\log \rho(x,\theta)$ und diese maximieren. Weil der Logarithmus streng monoton wächst, haben Likelihood und log-Likelihood dieselben Maximalstellen.
```

### replace – German block `134` – English block(s) **134**

What changed in the German:

```diff
- Wenn $\theta_0$ der 'wahre' Parameter für $X$ ist (mit dem $x$ gesampelt wurde), so konvergiert der Maximum-Likelihood-Schätzwert $\hat{\theta}$ für eine Stichprobe der Größe $n$ gegen den Wert $\theta$, für den die relative Entropie zwischen $P_{\theta_0}$ und $P_{\theta}$ minimiert wird (wenn das Modell gut aufgesetzt ist, ist dieses Minimum genau $0$). Um das einzusehen, benutzt man den zuvor erwähnten Trick und das Gesetz der großen Zahlen und den Zusammenhang, dass der Erwartungswert der log-Likelihood gleich der negativen Kreuzentropie [-$-H(P_{\theta_0}; P_\theta)$-] ist.
+ Wenn $\theta_0$ der 'wahre' Parameter für $X$ ist (mit dem $x$ gesampelt wurde), so konvergiert der Maximum-Likelihood-Schätzwert $\hat{\theta}$ für eine Stichprobe der Größe $n$ gegen den Wert $\theta$, für den die relative Entropie zwischen $P_{\theta_0}$ und $P_{\theta}$ minimiert wird (wenn das Modell gut aufgesetzt ist, ist dieses Minimum genau $0$). Um das einzusehen, benutzt man den zuvor erwähnten Trick und das Gesetz der großen Zahlen und den Zusammenhang, dass der Erwartungswert der log-Likelihood gleich der negativen Kreuzentropie {+$-H(x;P_{\theta_0})$+} ist.
```

German now reads:

```md
Wenn $\theta_0$ der 'wahre' Parameter für $X$ ist (mit dem $x$ gesampelt wurde), so konvergiert der Maximum-Likelihood-Schätzwert $\hat{\theta}$ für eine Stichprobe der Größe $n$ gegen den Wert $\theta$, für den die relative Entropie zwischen $P_{\theta_0}$ und $P_{\theta}$ minimiert wird (wenn das Modell gut aufgesetzt ist, ist dieses Minimum genau $0$). Um das einzusehen, benutzt man den zuvor erwähnten Trick und das Gesetz der großen Zahlen und den Zusammenhang, dass der Erwartungswert der log-Likelihood gleich der negativen Kreuzentropie $-H(x;P_{\theta_0})$ ist.
```

Current English block 134:

```md
Wenn $\theta_0$ der 'wahre' Parameter für $X$ ist (mit dem $x$ gesampelt wurde), so konvergiert der Maximum-Likelihood-Schätzwert $\hat{\theta}$ für eine Stichprobe der Größe $n$ gegen den Wert $\theta$, für den die relative Entropie zwischen $P_{\theta_0}$ und $P_{\theta}$ minimiert wird (wenn das Modell gut aufgesetzt ist, ist dieses Minimum genau $0$). Um das einzusehen, benutzt man den zuvor erwähnten Trick und das Gesetz der großen Zahlen und den Zusammenhang, dass der Erwartungswert der log-Likelihood gleich der negativen Kreuzentropie $-H(P_{\theta_0}; P_\theta)$ ist.
```

### replace – German block `137` – English block(s) **137**

German now reads:

```md
Angenommen, wir betrachten Server-Logfiles einer Web-Anwendung, insbesondere die Zeitstempel. Daraus können wir die konsekutiven Abstände berechnen, also die Wartezeit zwischen zwei Aufrufen. Wir möchten gerne wissen, mit welcher Wartezeit wir im Mittel rechnen können (um zusammen mit der durchschnittlichen Laufzeit eines Aufrufs zu einer Einschätzung zu kommen, welche Last wir erwarten können). Die Wartezeiten sind exponentialverteilt mit Parameter $\lambda > 0$, den wir schätzen wollen. zur Erinnerung: Die Dichte einer Exponentialverteilung ist $f(x) = \lambda e^{-\lambda x}$ und der Erwartungswert ist $\frac{1}{\lambda}$.
Die Likelihood für eine Stichprobe der Größe $N$ ist $L_x(\lambda) = \prod_{i=1}^N \lambda e^{-\lambda x_i}$ und die log-Likelihood ist demnach
$$
l_x(\lambda) := \log L_x(\lambda) = \left( \sum_{i=1}^N \log\lambda - \lambda x_i\right) = n \left( \log\lambda - \lambda \texttt{mean}(x) \right).
$$
Die Ableitung nach $\lambda$ ist einfach $\frac{n}{\lambda} - n \texttt{mean}(x)$, eine Nullstelle liegt bei $\hat{\lambda} = \frac{1}{\texttt{mean}(x)}$. Die zweite Ableitung von $l_x$ ist $-\frac{n}{\lambda^2}$, was bei $\hat{\lambda}$ den Wert $-n{\texttt{mean}(x)}^2 < 0$ annimmt, also ist $\hat{\lambda}$ ein Maximum und wir haben den Maximum-Likelihood-Schätzer bestimmt.
Wir rechnen also mit einer mittleren Wartezeit zwischen den Server-Aufrufen von $\texttt{mean}(x)$, wenn $x$ die beobachteten Wartezeiten sind.
```

Current English block 137:

```md
**Anwendung: Server-Logfiles.** Aus den Zeitstempeln einer Web-Anwendung berechnen wir die Abstände zwischen zwei Aufrufen, also Wartezeiten $x_1,\dots,x_n$. Um zusammen mit der mittleren Laufzeit eines Aufrufs die zu erwartende Last abzuschätzen, modellieren wir sie als $\operatorname{Exp}(\lambda)$-verteilt und schätzen $\lambda$ wie im Beispiel oben: $\hat\lambda = 1/\texttt{mean}(x)$. Wir rechnen also mit einer mittleren Wartezeit von $\texttt{mean}(x)$ zwischen zwei Aufrufen, und für die Anzahl der Aufrufe je Zeiteinheit mit der Poissonverteilung zum selben $\lambda$ (Kapitel [Wichtigste diskrete Verteilungen](important-discrete-distributions.ipynb)).
```


## dimensionsreduktion.ipynb → dimensionality-reduction.ipynb

### delete – German block `c0.1` – English block(s) **c0.1**

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Hauptkomponentenanalyse (VL 18)](https://media.hhu.de/channel/video/data-science-vl-18-pca-2025/2348ef1c85dcb2e560e6199d7303db63/167)
```

### replace – German block `c1.8` – English block(s) **c1.8**

What changed in the German:

```diff
- ```{figure} images/case_b_dual_proj.png :width: 600px :align: center :name: pca-case-b Fall (b): $z \sim \mathcal{N}(1,\ [-0{,}1^2)$.-] Jetzt geht bei der Projektion etwas verloren, aber nur $0{,}01$ von einer Gesamtvarianz von $2{,}28$ — weniger als ein halbes Prozent. ```
+ ```{figure} images/case_b_dual_proj.png :width: 600px :align: center :name: pca-case-b Fall (b): $z \sim \mathcal{N}(1,\ {+0{,}1)$.+} Jetzt geht bei der Projektion etwas verloren, aber nur $0{,}01$ von einer Gesamtvarianz von $2{,}28$ — weniger als ein halbes Prozent. ```
```

German now reads:

```md
```{figure} images/case_b_dual_proj.png
:width: 600px
:align: center
:name: pca-case-b

Fall (b): $z \sim \mathcal{N}(1,\ 0{,}1)$. Jetzt geht bei der Projektion etwas verloren, aber nur $0{,}01$ von einer Gesamtvarianz von $2{,}28$ — weniger als ein halbes Prozent.
```
```

Current English block c1.8:

```md
```{figure} images/case_b_dual_proj.png
:width: 600px
:align: center
:name: pca-case-b

Fall (b): $z \sim \mathcal{N}(1,\ 0{,}1^2)$. Jetzt geht bei der Projektion etwas verloren, aber nur $0{,}01$ von einer Gesamtvarianz von $2{,}28$ — weniger als ein halbes Prozent.
```
```

### replace – German block `c1.15` – English block(s) **c1.15**

What changed in the German:

```diff
- ```{admonition} Beispiel Wenn eine beliebige invertierbare Matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ auf ein Sample einer bivariaten Standardnormalverteilung angewendet wird, dann können wir die Richtungen mit größter Varianz bestimmen als die Richtungen, die von $M$ am stärksten gestreckt werden. [-Für symmetrisches $M$ ist das-] ein Vektor $v$ mit $Mv = \lambda v$ für das größte solche [-$\lambda$ (für beliebiges $M$ wäre es die Richtung des größten Singulärwerts; wir werden gleich sehen, dass uns die symmetrische Situation genügt).-] ```
+ ```{admonition} Beispiel Wenn eine beliebige invertierbare Matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ auf ein Sample einer bivariaten Standardnormalverteilung angewendet wird, dann können wir die Richtungen mit größter Varianz bestimmen als die Richtungen, die von $M$ am stärksten gestreckt werden. {+Das wäre+} ein Vektor $v$ mit $Mv = \lambda v$ für das größte solche {+$\lambda$.+} ```
```

German now reads:

```md
```{admonition} Beispiel
Wenn eine beliebige invertierbare Matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ auf ein Sample einer bivariaten Standardnormalverteilung angewendet wird, dann können wir die Richtungen mit größter Varianz bestimmen als die Richtungen, die von $M$ am stärksten gestreckt werden. Das wäre ein Vektor $v$ mit $Mv = \lambda v$ für das größte solche $\lambda$.
```
```

Current English block c1.15:

```md
```{admonition} Beispiel
Wenn eine beliebige invertierbare Matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ auf ein Sample einer bivariaten Standardnormalverteilung angewendet wird, dann können wir die Richtungen mit größter Varianz bestimmen als die Richtungen, die von $M$ am stärksten gestreckt werden. Für symmetrisches $M$ ist das ein Vektor $v$ mit $Mv = \lambda v$ für das größte solche $\lambda$ (für beliebiges $M$ wäre es die Richtung des größten Singulärwerts; wir werden gleich sehen, dass uns die symmetrische Situation genügt).
```
```

### replace – German block `c15.0` – English block(s) **c15.0**

What changed in the German:

```diff
- Ein ganz anderer Zugang zum [-Finden-] der Richtung maximaler Varianz ist es, die Summe der quadrierten Abstände der Punkte zu einer Geraden zu minimieren.
+ Ein ganz anderer Zugang zum {+finden+} der Richtung maximaler Varianz ist es, die Summe der quadrierten Abstände der Punkte zu einer Geraden zu minimieren.
```

German now reads:

```md
Ein ganz anderer Zugang zum finden der Richtung maximaler Varianz ist es, die Summe der quadrierten Abstände der Punkte zu einer Geraden zu minimieren.
```

Current English block c15.0:

```md
Ein ganz anderer Zugang zum Finden der Richtung maximaler Varianz ist es, die Summe der quadrierten Abstände der Punkte zu einer Geraden zu minimieren.
```

### replace – German block `c15.4` – English block(s) **c15.4**

What changed in the German:

```diff
- ```{figure} images/pca-variation.gif :width: 600px :align: center :name: pca-variation [-Die Gerade dreht sich, bis die Summe der quadrierten Abstände minimal wird — das ist dieselbe Richtung, die die größte Varianz hat.-] ```
+ ```{figure} images/pca-variation.gif :width: 600px :align: center :name: pca-variation ```
```

German now reads:

```md
```{figure} images/pca-variation.gif
:width: 600px
:align: center
:name: pca-variation


```
```

Current English block c15.4:

```md
```{figure} images/pca-variation.gif
:width: 600px
:align: center
:name: pca-variation

Die Gerade dreht sich, bis die Summe der quadrierten Abstände minimal wird — das ist dieselbe Richtung, die die größte Varianz hat.
```
```

### replace – German block `c34.0` – English block(s) **c34.0**

What changed in the German:

```diff
- Statt hier nur auf das Bild zu achten, ist es besser, auch eine Kennzahl auszurechnen. Wie zuvor verwenden wir dazu ein Entropie-basiertes Maß, die [-*gemeinsame Information* $I(X;Y)$-] der beiden [-Klassenvariablen (Kapitel [Relative Entropie](relative-entropie.md)),-] normiert auf den Mittelwert [-ihrer beiden Entropien:-]
+ Statt hier nur auf das Bild zu achten, ist es besser, auch eine Kennzahl auszurechnen. Wie zuvor verwenden wir dazu ein Entropie-basiertes Maß, die {+gemeinsame Entropie+} der beiden {+Klassenverteilungen,+} normiert auf den Mittelwert {+der Entropien der einzelnen Klassenverteilungen:+}
```

German now reads:

```md
Statt hier nur auf das Bild zu achten, ist es besser, auch eine Kennzahl auszurechnen. Wie zuvor verwenden wir dazu ein Entropie-basiertes Maß, die gemeinsame Entropie der beiden Klassenverteilungen, normiert auf den Mittelwert der Entropien der einzelnen Klassenverteilungen:
```

Current English block c34.0:

```md
Statt hier nur auf das Bild zu achten, ist es besser, auch eine Kennzahl auszurechnen. Wie zuvor verwenden wir dazu ein Entropie-basiertes Maß, die *gemeinsame Information* $I(X;Y)$ der beiden Klassenvariablen (Kapitel [Relative Entropie](relative-entropy.md)), normiert auf den Mittelwert ihrer beiden Entropien:
```


## lineare-regression.ipynb → linear-regression.ipynb

### delete – German block `c0.1` – English block(s) **c0.1**

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Regression (VL 19)](https://media.hhu.de/channel/video/data-science-vl-19-regression-2025/df00fcd2038eb5b297b77bb5369bb960/167)
[Regression und Regularisierung (VL 20, ohne Ton)](https://media.hhu.de/channel/video/data-science-vl-20-regression-und-regularisierung-2025/f308330baee63f83093c7d4068502840/167)
```

### replace – German block `c4.2` – English block(s) **c4.2**

What changed in the German:

```diff
- Der kleinste-Quadrate-Schätzer ist ein [-Maximum-Likelihood-Schätzer, wenn man die Störgrößen als normalverteilt annimmt (das Modell dazu steht am Ende des Abschnitts *Lineare Regression*).-]
+ Der kleinste-Quadrate-Schätzer ist ein {+Maximum-Likelihood-Schätzer.+}
```

German now reads:

```md
Der kleinste-Quadrate-Schätzer ist ein Maximum-Likelihood-Schätzer.
```

Current English block c4.2:

```md
Der kleinste-Quadrate-Schätzer ist ein Maximum-Likelihood-Schätzer, wenn man die Störgrößen als normalverteilt annimmt (das Modell dazu steht am Ende des Abschnitts *Lineare Regression*).
```

### replace – German block `c4.8` – English block(s) **c4.8**

What changed in the German:

```diff
- Teilt man Zähler und Nenner durch $N$, stehen dort zwei Größen, die wir schon kennen: oben die empirische Kovarianz von $x$ und $y$, unten die empirische Varianz von $x$ (beide in der $n$-Version, siehe [-die Bemerkung *Für Daten* im Kapitel [Kovarianz](kovarianz.md)).-] Die Steigung der Ausgleichsgeraden ist also
+ Teilt man Zähler und Nenner durch $N$, stehen dort zwei Größen, die wir schon kennen: oben die empirische Kovarianz von $x$ und $y$, unten die empirische Varianz von $x$ (beide in der $n$-Version, siehe {+[Deskriptive Statistik](deskriptive-statistik.md)).+} Die Steigung der Ausgleichsgeraden ist also
```

German now reads:

```md
Teilt man Zähler und Nenner durch $N$, stehen dort zwei Größen, die wir schon kennen: oben die empirische Kovarianz von $x$ und $y$, unten die empirische Varianz von $x$ (beide in der $n$-Version, siehe [Deskriptive Statistik](deskriptive-statistik.md)). Die Steigung der Ausgleichsgeraden ist also
```

Current English block c4.8:

```md
Teilt man Zähler und Nenner durch $N$, stehen dort zwei Größen, die wir schon kennen: oben die empirische Kovarianz von $x$ und $y$, unten die empirische Varianz von $x$ (beide in der $n$-Version, siehe die Bemerkung *Für Daten* im Kapitel [Kovarianz](covariance.md)). Die Steigung der Ausgleichsgeraden ist also
```

### insert – German block after `c20.1` – **new** – decide whether it belongs in this edition

German now reads:

```md
Machen Sie sich klar, dass die zweite Definition keine Verallgemeinerung der ersten Definition ist.
```

### replace – German block `c21.1` – English block(s) **c21.1**

What changed in the German:

```diff
- Man nennt den Fall $w = (w_0, w_1)$ eine **einfache lineare Regression** und den allgemeineren Fall dann eine [-**multiple lineare-] Regression**, weil dabei dann eine multivariate unabhängige Variable $X$ als Regressor verwendet wird. Die lineare Regression von Scipy.stats kann nur eine einfache lineare Regression!
+ Man nennt den Fall $w = (w_0, w_1)$ eine **einfache lineare Regression** und den allgemeineren Fall dann eine {+**multilineare+} Regression**, weil dabei dann eine multivariate unabhängige Variable $X$ als Regressor verwendet wird. Die lineare Regression von Scipy.stats kann nur eine einfache lineare Regression!
```

German now reads:

```md
Man nennt den Fall $w = (w_0, w_1)$ eine **einfache lineare Regression** und den allgemeineren Fall dann eine **multilineare Regression**, weil dabei dann eine multivariate unabhängige Variable $X$ als Regressor verwendet wird. Die lineare Regression von Scipy.stats kann nur eine einfache lineare Regression!
```

Current English block c21.1:

```md
Man nennt den Fall $w = (w_0, w_1)$ eine **einfache lineare Regression** und den allgemeineren Fall dann eine **multiple lineare Regression**, weil dabei dann eine multivariate unabhängige Variable $X$ als Regressor verwendet wird. Die lineare Regression von Scipy.stats kann nur eine einfache lineare Regression!
```

### replace – German block `c26.0` – English block(s) **c26.0**

What changed in the German:

```diff
- ```{admonition} Beispiel Die Nutzung der Basisfunktion $\phi(x) = (1,x,x^2,x^3,\dots,x^d)$ mit $d > 0$ nennt man **polynomiale Regression**. Konkret für $d=2$ bedeutet [-das,-] dass $f(x,w) = w_0 + w_1x + w_2x^2$ ist. Wir sehen nochmal deutlich: $f$ ist linear in $w$, nicht in $x$. ```
+ ```{admonition} Beispiel Die Nutzung der Basisfunktion $\phi(x) = (1,x,x^2,x^3,\dots,x^d)$ mit $d > 0$ nennt man **polynomiale Regression**. Konkret für $d=2$ bedeutet {+dass,+} dass $f(x,w) = w_0 + w_1x + w_2x^2$ ist. Wir sehen nochmal deutlich: $f$ ist linear in $w$, nicht in $x$. ```
```

German now reads:

```md
```{admonition} Beispiel
Die Nutzung der Basisfunktion $\phi(x) = (1,x,x^2,x^3,\dots,x^d)$ mit $d > 0$ nennt man **polynomiale Regression**.
Konkret für $d=2$ bedeutet dass, dass $f(x,w) = w_0 + w_1x + w_2x^2$ ist. Wir sehen nochmal deutlich: $f$ ist linear in $w$, nicht in $x$.
```
```

Current English block c26.0:

```md
```{admonition} Beispiel
Die Nutzung der Basisfunktion $\phi(x) = (1,x,x^2,x^3,\dots,x^d)$ mit $d > 0$ nennt man **polynomiale Regression**.
Konkret für $d=2$ bedeutet das, dass $f(x,w) = w_0 + w_1x + w_2x^2$ ist. Wir sehen nochmal deutlich: $f$ ist linear in $w$, nicht in $x$.
```
```

### replace – German block `c33.1` – English block(s) **c33.1**

What changed in the German:

```diff
- Wir betrachten den [Melbourne Housing Market Datensatz von Anthony [-Pino](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market). Er steht unter-] CC BY-NC-SA [-4.0 und ist damit von der Lizenz dieses Skripts ausgenommen: Weiterverwendung nur nicht-kommerziell und unter denselben Bedingungen.-]
+ Wir betrachten den [Melbourne Housing Market Datensatz von Anthony {+Pino](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market),+} CC BY-NC-SA {+4.0.+}
```

German now reads:

```md
Wir betrachten den [Melbourne Housing Market Datensatz von Anthony Pino](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market), CC BY-NC-SA 4.0.
```

Current English block c33.1:

```md
Wir betrachten den [Melbourne Housing Market Datensatz von Anthony Pino](https://www.kaggle.com/datasets/anthonypino/melbourne-housing-market). Er steht unter CC BY-NC-SA 4.0 und ist damit von der Lizenz dieses Skripts ausgenommen: Weiterverwendung nur nicht-kommerziell und unter denselben Bedingungen.
```

### replace – German block `c39.0` – English block(s) **c39.0**

What changed in the German:

```diff
- ```{admonition} Definition $$ R^2 = [-1 --] \dfrac{\sum_{i=1}^N {\left( [-y_i-] - [-f(x_i,\beta)-] \right)}^2}{\sum_{i=1}^N {\left( y_i - \texttt{mean}(y) \right)}^2} $$ Die Größe $R^2$ wird auch **Bestimmtheitsmaß**, en. **Coefficient of determination** genannt. [-Im Zähler steht die Residuenquadratsumme des Modells, im Nenner die des besten konstanten Modells $\texttt{mean}(y)$; $R^2$ misst also, welchen Anteil der Streuung von $y$ das Modell gegenüber der Konstanten wegerklärt. Für kleinste Quadrate mit Achsenabschnitt ist das auf den Trainingsdaten dasselbe wie $\sum (f(x_i,\beta) - \texttt{mean}(y))^2 / \sum (y_i - \texttt{mean}(y))^2$, der Anteil der „erklärten“ Varianz; auf Testdaten wie oben gilt nur die erste Form, und dort kann $R^2$ auch negativ werden (Kapitel [Modell-Auswahl](model-selection.ipynb)).-] ```
+ ```{admonition} Definition $$ R^2 = \dfrac{\sum_{i=1}^N {\left( {+f(x_i,\beta)+} - {+\texttt{mean}(y)+} \right)}^2}{\sum_{i=1}^N {\left( y_i - \texttt{mean}(y) \right)}^2} $$ Die Größe $R^2$ wird auch **Bestimmtheitsmaß**, en. **Coefficient of determination** genannt. ```
```

German now reads:

```md
```{admonition} Definition
$$
R^2 = \dfrac{\sum_{i=1}^N {\left( f(x_i,\beta) - \texttt{mean}(y) \right)}^2}{\sum_{i=1}^N {\left( y_i - \texttt{mean}(y) \right)}^2}
$$

Die Größe $R^2$ wird auch **Bestimmtheitsmaß**, en. **Coefficient of determination** genannt.
```
```

Current English block c39.0:

```md
```{admonition} Definition
$$
R^2 = 1 - \dfrac{\sum_{i=1}^N {\left( y_i - f(x_i,\beta) \right)}^2}{\sum_{i=1}^N {\left( y_i - \texttt{mean}(y) \right)}^2}
$$

Die Größe $R^2$ wird auch **Bestimmtheitsmaß**, en. **Coefficient of determination** genannt. Im Zähler steht die Residuenquadratsumme des Modells, im Nenner die des besten konstanten Modells $\texttt{mean}(y)$; $R^2$ misst also, welchen Anteil der Streuung von $y$ das Modell gegenüber der Konstanten wegerklärt. Für kleinste Quadrate mit Achsenabschnitt ist das auf den Trainingsdaten dasselbe wie $\sum (f(x_i,\beta) - \texttt{mean}(y))^2 / \sum (y_i - \texttt{mean}(y))^2$, der Anteil der „erklärten“ Varianz; auf Testdaten wie oben gilt nur die erste Form, und dort kann $R^2$ auch negativ werden (Kapitel [Modell-Auswahl](model-selection.ipynb)).
```
```

### insert – German block after `c41.1` – **new** – decide whether it belongs in this edition

German now reads:

```md
Wir schauen uns noch Plots zur linearen Regression in den Variablen Distanz und Alter an:
```

### delete – German block `c44.2` – English block(s) **c44.2**

Current English block c44.2:

```md
Zum Schluss dieses Anwendungsbeispiels noch zwei Bilder zur linearen Regression in den Variablen Distanz und Alter, erst eine, dann beide:
```

### delete – German block `c55.1` – English block(s) **c55.1**

Current English block c55.1:

```md
Eine Regression ist ein Modell $Y = f(X,\beta) + \epsilon$; *linear* heißt linear in den Parametern, weshalb Basisfunktionen und One-Hot-Spalten das Modell nicht verlassen. Die Methode der kleinsten Quadrate liefert $\beta_1 = \operatorname{Cov}(x,y)/\sigma^2(x)$ und ist Maximum Likelihood bei normalverteilten Störgrößen; Residuenplots prüfen diese Annahme. Regularisierung (Ridge, Lasso) bestraft große Koeffizienten und ist das Mittel gegen Overfitting bei zu vielen Basisfunktionen.
```

### insert – German block after `c55.2` – **new** – decide whether it belongs in this edition

German now reads:

```md
from IPython.display import YouTubeVideo
YouTubeVideo('WWqE7YHR4Jc')
```


## kernel-methoden.ipynb → kernel-methods.ipynb

### delete – German block `c0.1` – English block(s) **c0.1**

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Kernel-Trick (VL 21, erste 32 Minuten)](https://media.hhu.de/channel/video/data-science-vl-21-kernel-trick-und-signifikanz-bei-tests-2025/742bea567f5ae6e6a2d2a1b1fb8115c7/167)
```

### replace – German block `c14.8` – English block(s) **c14.8**

What changed in the German:

```diff
- sodass [-wir-] für eine Abstandsmessung im transformierten Raum eigentlich gar nicht $Ma$ und $Mb$ ausrechnen müssen, sondern 'nur' $M^TM$ ziemlich oft anwenden. Wenn wir Glück haben, ist das einfacher.
+ sodass für eine Abstandsmessung im transformierten Raum eigentlich gar nicht $Ma$ und $Mb$ ausrechnen müssen, sondern 'nur' $M^TM$ ziemlich oft anwenden. Wenn wir Glück haben, ist das einfacher.
```

German now reads:

```md
sodass für eine Abstandsmessung im transformierten Raum eigentlich gar nicht $Ma$ und $Mb$ ausrechnen müssen, sondern 'nur' $M^TM$ ziemlich oft anwenden. Wenn wir Glück haben, ist das einfacher.
```

Current English block c14.8:

```md
sodass wir für eine Abstandsmessung im transformierten Raum eigentlich gar nicht $Ma$ und $Mb$ ausrechnen müssen, sondern 'nur' $M^TM$ ziemlich oft anwenden. Wenn wir Glück haben, ist das einfacher.
```

### replace – German block `c14.19`, `c14.20` – English block(s) **c14.19**, **c14.20**

What changed in the German:

```diff
- ### [-Gausssche-] Kernel
+ ### {+Gaussche+} Kernel
- ```{admonition} Definition Kernel der Form $$ \kappa(x,y) = e^{\left(-\dfrac{\lVert x - y \rVert^2}{2\sigma^2}\right)} $$ heißen **Gauss-Kernel** mit Parameter $\gamma = [-\frac{1}{2\sigma^2}$.-] Alternativ spricht man auch vom **quadrierten Exponentialkernel** oder dem **quadratischen Exponentialkernel** oder dem **radialen Basisfunktionskernel**. ```
+ ```{admonition} Definition Kernel der Form $$ \kappa(x,y) = e^{\left(-\dfrac{\lVert x - y \rVert^2}{2\sigma^2}\right)} $$ heißen **Gauss-Kernel** mit Parameter $\gamma = {+1/2\sigma^2$.+} Alternativ spricht man auch vom **quadrierten Exponentialkernel** oder dem **quadratischen Exponentialkernel** oder dem **radialen Basisfunktionskernel**. ```
```

German now reads:

```md
### Gaussche Kernel
```{admonition} Definition
Kernel der Form

$$
\kappa(x,y) = e^{\left(-\dfrac{\lVert x - y \rVert^2}{2\sigma^2}\right)}
$$

heißen **Gauss-Kernel** mit Parameter $\gamma = 1/2\sigma^2$.
Alternativ spricht man auch vom **quadrierten Exponentialkernel** oder dem **quadratischen Exponentialkernel** oder dem **radialen Basisfunktionskernel**.
```
```

Current English block c14.19:

```md
### Gausssche Kernel
```

Current English block c14.20:

```md
```{admonition} Definition
Kernel der Form

$$
\kappa(x,y) = e^{\left(-\dfrac{\lVert x - y \rVert^2}{2\sigma^2}\right)}
$$

heißen **Gauss-Kernel** mit Parameter $\gamma = \frac{1}{2\sigma^2}$.
Alternativ spricht man auch vom **quadrierten Exponentialkernel** oder dem **quadratischen Exponentialkernel** oder dem **radialen Basisfunktionskernel**.
```
```


## statistische-tests.md → statistical-tests.md

### replace – German block `1`, `2` – English block(s) **1**, **2**

German now reads:

```md
Bei der explorativen Datenanalyse kommen wir zu Hypothesen, welche Zusammenhänge in den Daten stecken. Bei der Implementierung von Systemen mit maschinellem Lernen müssen wir zahlreiche Entscheidungen treffen, etwa ob wir eine Variable als Normalverteilt annehmen können, ob die Verteilung für zwei Gruppen oder Cluster etwa gleich oder sehr verschieden ist.
```

Current English block 1:

```md
[Vorlesungsaufzeichnung Tests und Signifikanz (VL 21, ab Minute 34)](https://media.hhu.de/channel/video/data-science-vl-21-kernel-trick-und-signifikanz-bei-tests-2025/742bea567f5ae6e6a2d2a1b1fb8115c7/167?t=2040)
```

Current English block 2:

```md
Bei der explorativen Datenanalyse kommen wir zu Hypothesen, welche Zusammenhänge in den Daten stecken. Bei der Implementierung von Systemen mit maschinellem Lernen müssen wir zahlreiche Entscheidungen treffen, etwa ob wir eine Variable als normalverteilt annehmen können, ob die Verteilung für zwei Gruppen oder Cluster etwa gleich oder sehr verschieden ist.
```

### replace – German block `15`, `16` – English block(s) **15**, **16**

What changed in the German:

```diff
- ```{figure} images/likelihood-scale.png :width: 560px :align: center :name: likelihood-scale [-Die *Likelihood scale* der-] IPCC [-Calibrated Language {cite}`sr15`.-] ```
+ ```{figure} images/likelihood-scale.png :width: 560px :align: center :name: likelihood-scale IPCC {+Likelihood scale+} ```
- Nun sehen wir, dass es sich beim grau schattierten Bereich um den Bereich handelt, in dem mit mind. $2/3$ Wahrscheinlichkeit die tatsächlichen Messwerte liegen werden (laut Modell). Anhand dieser Information kann man deutlich besser einschätzen, welche zukünftigen Erwärmungen zu erwarten sind, selbst wenn wir 'Glück haben' oder auch wie schlimm es werden könnte, wenn wir 'Pech haben'. Der grau schattierte Bereich ist genau genommen ein **Prognoseintervall**, in dem der tatsächliche Wert in Zukunft mit hoher Wahrscheinlichkeit vermutet wird. Eng verwandt ist ein [-**Konfidenzintervall** für einen Parameter: ein aus-] der [-Stichprobe berechnetes Intervall, das so konstruiert-] ist, [-dass es-] in (z.B.) [-95 % aller Stichproben den wahren Parameter überdeckt.-]
+ Nun sehen wir, dass es sich beim grau schattierten Bereich um den Bereich handelt, in dem mit mind. $2/3$ Wahrscheinlichkeit die tatsächlichen Messwerte liegen werden (laut Modell). Anhand dieser Information kann man deutlich besser einschätzen, welche zukünftigen Erwärmungen zu erwarten sind, selbst wenn wir 'Glück haben' oder auch wie schlimm es werden könnte, wenn wir 'Pech haben'. Der grau schattierte Bereich ist genau genommen ein **Prognoseintervall**, in dem der tatsächliche Wert in Zukunft mit hoher Wahrscheinlichkeit vermutet wird. Eng verwandt ist ein {+**Konfidenzintervall**, welches+} der {+Bereich+} ist, {+in dem der tatsächliche Wert+} in (z.B.) {+95\% der erwarteten Beobachtungen vermutet wird.+}
```

German now reads:

```md
```{figure} images/likelihood-scale.png
:width: 560px
:align: center
:name: likelihood-scale

IPCC Likelihood scale
```
Nun sehen wir, dass es sich beim grau schattierten Bereich um den Bereich handelt, in dem mit mind. $2/3$ Wahrscheinlichkeit die tatsächlichen Messwerte liegen werden (laut Modell). Anhand dieser Information kann man deutlich besser einschätzen, welche zukünftigen Erwärmungen zu erwarten sind, selbst wenn wir 'Glück haben' oder auch wie schlimm es werden könnte, wenn wir 'Pech haben'. Der grau schattierte Bereich ist genau genommen ein **Prognoseintervall**, in dem der tatsächliche Wert in Zukunft mit hoher Wahrscheinlichkeit vermutet wird. Eng verwandt ist ein **Konfidenzintervall**, welches der Bereich ist, in dem der tatsächliche Wert in (z.B.) 95\% der erwarteten Beobachtungen vermutet wird.
```

Current English block 15:

```md
```{figure} images/likelihood-scale.png
:width: 560px
:align: center
:name: likelihood-scale

Die *Likelihood scale* der IPCC Calibrated Language {cite}`sr15`.
```
```

Current English block 16:

```md
Nun sehen wir, dass es sich beim grau schattierten Bereich um den Bereich handelt, in dem mit mind. $2/3$ Wahrscheinlichkeit die tatsächlichen Messwerte liegen werden (laut Modell). Anhand dieser Information kann man deutlich besser einschätzen, welche zukünftigen Erwärmungen zu erwarten sind, selbst wenn wir 'Glück haben' oder auch wie schlimm es werden könnte, wenn wir 'Pech haben'. Der grau schattierte Bereich ist genau genommen ein **Prognoseintervall**, in dem der tatsächliche Wert in Zukunft mit hoher Wahrscheinlichkeit vermutet wird. Eng verwandt ist ein **Konfidenzintervall** für einen Parameter: ein aus der Stichprobe berechnetes Intervall, das so konstruiert ist, dass es in (z.B.) 95 % aller Stichproben den wahren Parameter überdeckt.
```

### replace – German block `44`, `45` – English block(s) **44**, **45**

German now reads:

```md
**Münzwurf:**
Der $n$-fach wiederholte Münzwurf einer unfairen Münze mit Erfolgswahrscheinlichkeit $p$ lässt sich modellieren mit dem **Binomialmodell** (siehe [Wichtigste diskrete Verteilungen](wichtigste-diskrete-verteilungen.ipynb)): $\mathcal{X} = \{1,\dots,n\}$ ist die Anzahl der Erfolge, der unbekannte Parameter ist $\theta = p \in \Theta = [0,1]$ und $P_\theta = Bin(n,\theta)$ (und $\tau = id$, also schätzen wir den Parameter $\theta$).
Wir bestimmen den Maximum-Likelihood-Schätzer für $\theta$:
$$
\begin{aligned}
L_x(\theta) &= P_\theta(x|n) = \binom{n}{x} \theta^x (1-\theta)^{n-x} \\
l_x(\theta) &= \log L_x(\theta) = \log\binom{n}{x} + x\log(\theta) + (n-x)\log(1-\theta) \\
l_x'(\theta) &= \dfrac{x}{\theta} - \dfrac{n-x}{1-\theta} \\
l_x'(\theta) &= 0 \implies x(1-\theta) = (n-x)\theta \\
             & \qquad \implies x - \theta x = \theta n - \theta x \\
             & \qquad \implies x = \theta n \\
             & \qquad \implies \theta = \frac{x}{n}.
\end{aligned}
$$
Ganz konkret: werfen wir die Münze $100$ mal und es kommt $45$ mal Zahl, so schätzen wir $\theta$ als $\frac{45}{100}$ (also insbesondere, dass die Münze wirklich unfair ist).
```

Current English block 44:

```md
**Münzwurf:**
Der $n$-fach wiederholte Münzwurf einer unfairen Münze mit Erfolgswahrscheinlichkeit $p$ lässt sich modellieren mit dem **Binomialmodell** (siehe [Wichtigste diskrete Verteilungen](important-discrete-distributions.ipynb)): $\mathcal{X} = \{0,\dots,n\}$ ist die Anzahl der Erfolge, der unbekannte Parameter ist $\theta = p \in \Theta = [0,1]$ und $P_\theta = \operatorname{Bin}(n,\theta)$ (und $\tau = id$, also schätzen wir den Parameter $\theta$).
```

Current English block 45:

```md
Den Maximum-Likelihood-Schätzer für $\theta$ haben wir dort schon berechnet: $\hat\theta = \frac{x}{n}$, der Anteil der Erfolge. Ganz konkret: werfen wir die Münze $100$ mal und es kommt $45$ mal Zahl, so schätzen wir $\theta$ als $\frac{45}{100}$ (also insbesondere, dass die Münze wirklich unfair ist).
```

### replace – German block `53` – English block(s) **53**

What changed in the German:

```diff
- Wir wollen natürlich gerne $c=\epsilon$ verwenden, und das $\epsilon$ in Abhängigkeit von $\alpha$ so wählen, dass auf der rechten Seite der Ungleichung nur noch $\alpha$ steht. Es ist $\mathbb{V}T = [-\mathbb{V}\!\left(\frac{x}{n}\right) = \frac{\theta(1-\theta)}{n}$,-] was dummerweise noch von $\theta$ abhängt, welches wir ja nicht kennen!
+ Wir wollen natürlich gerne $c=\epsilon$ verwenden, und das $\epsilon$ in Abhängigkeit von $\alpha$ so wählen, dass auf der rechten Seite der Ungleichung nur noch $\alpha$ steht. Es ist $\mathbb{V}T = {+n\theta(1-\theta)$,+} was dummerweise noch von $\theta$ abhängt, welches wir ja nicht kennen!
```

German now reads:

```md
Wir wollen natürlich gerne $c=\epsilon$ verwenden, und das $\epsilon$ in Abhängigkeit von $\alpha$ so wählen, dass auf der rechten Seite der Ungleichung nur noch $\alpha$ steht. Es ist $\mathbb{V}T = n\theta(1-\theta)$, was dummerweise noch von $\theta$ abhängt, welches wir ja nicht kennen!
```

Current English block 53:

```md
Wir wollen natürlich gerne $c=\epsilon$ verwenden, und das $\epsilon$ in Abhängigkeit von $\alpha$ so wählen, dass auf der rechten Seite der Ungleichung nur noch $\alpha$ steht. Es ist $\mathbb{V}T = \mathbb{V}\!\left(\frac{x}{n}\right) = \frac{\theta(1-\theta)}{n}$, was dummerweise noch von $\theta$ abhängt, welches wir ja nicht kennen!
```

### replace – German block `62` – English block(s) **62**

What changed in the German:

```diff
- setzen wir noch $\alpha = 0.05$ ein, ergibt sich, dass die Stichprobe größer als $2000$ sein sollte, um verwerfen zu können, dass die Münze fair ist. Wenn wir ein clevereres Verfahren zur [-Bestimmung-] kleinerer Konfidenzintervalle hätten, würde uns allerdings eine kleinere Stichprobe ausreichen.
+ setzen wir noch $\alpha = 0.05$ ein, ergibt sich, dass die Stichprobe größer als $2000$ sein sollte, um verwerfen zu können, dass die Münze fair ist. Wenn wir ein clevereres Verfahren zur {+bestimmung+} kleinerer Konfidenzintervalle hätten, würde uns allerdings eine kleinere Stichprobe ausreichen.
```

German now reads:

```md
setzen wir noch $\alpha = 0.05$ ein, ergibt sich, dass die Stichprobe größer als $2000$ sein sollte, um verwerfen zu können, dass die Münze fair ist. Wenn wir ein clevereres Verfahren zur bestimmung kleinerer Konfidenzintervalle hätten, würde uns allerdings eine kleinere Stichprobe ausreichen.
```

Current English block 62:

```md
setzen wir noch $\alpha = 0.05$ ein, ergibt sich, dass die Stichprobe größer als $2000$ sein sollte, um verwerfen zu können, dass die Münze fair ist. Wenn wir ein clevereres Verfahren zur Bestimmung kleinerer Konfidenzintervalle hätten, würde uns allerdings eine kleinere Stichprobe ausreichen.
```

### replace – German block `71` – English block(s) **71**

What changed in the German:

```diff
- Die Zufallsvariable 'Stichprobenvarianz' $S^\ast(X)^2$ ist so verteilt, dass [-$\dfrac{n-1}{\sigma(Z)^2}-] S^\ast(X)^2$ einer sogenannten **$\chi^2$-Verteilung** [-mit $n-1$ Freiheitsgraden-] folgt (ein Spezialfall der Gamma-Verteilung).
+ Die Zufallsvariable 'Stichprobenvarianz' $S^\ast(X)^2$ ist so verteilt, dass {+$\dfrac{n-1}{\sigma(Z)}+} S^\ast(X)^2$ einer sogenannten **$\chi^2$-Verteilung** folgt (ein Spezialfall der Gamma-Verteilung).
```

German now reads:

```md
Die Zufallsvariable 'Stichprobenvarianz' $S^\ast(X)^2$ ist so verteilt, dass $\dfrac{n-1}{\sigma(Z)} S^\ast(X)^2$ einer sogenannten **$\chi^2$-Verteilung** folgt (ein Spezialfall der Gamma-Verteilung).
```

Current English block 71:

```md
Die Zufallsvariable 'Stichprobenvarianz' $S^\ast(X)^2$ ist so verteilt, dass $\dfrac{n-1}{\sigma(Z)^2} S^\ast(X)^2$ einer sogenannten **$\chi^2$-Verteilung** mit $n-1$ Freiheitsgraden folgt (ein Spezialfall der Gamma-Verteilung).
```

### replace – German block `84` – English block(s) **84**

What changed in the German:

```diff
- Zu $\alpha$ wählen wir nun $t$ als das [-$(1-\frac{\alpha}{2})$-*Quantil*-] der $t$-Verteilung [-mit-] $n-1$ [-Freiheitsgraden, also die Zahl $t > 0$ mit-] $P(T \leq [-t) = 1 - \frac{\alpha}{2}$; wegen der Symmetrie der Verteilung ist dann $P(|T| \leq t) = 1 - \alpha$.-] So etwas hat man früher in Tabellen nachgeschlagen, heute benutzen wir einen [-Rechner (`scipy.stats.t.ppf(1 - alpha/2, n - 1)`).-] Dann ist mit $\epsilon := [-t\frac{S^\ast(x)}{\sqrt{n}}$-] ein Konfidenzintervall für $\mu(Z)$ gegeben durch
+ Zu $\alpha$ wählen wir nun $t$ als das {+$\frac{\alpha}{2}$-*Quantil*+} der $t$-Verteilung {+(mit+} $n-1$ {+Freiheitsgraden), das ist genau das kleinste $t$ sodass+} $P(T {+< t)+} \leq {+\frac{\alpha}{2}$ ist.+} So etwas hat man früher in Tabellen nachgeschlagen, heute benutzen wir einen {+Rechner.+} Dann ist mit $\epsilon := {+t\frac{\sigma^\ast(x)}{\sqrt{n}}$+} ein Konfidenzintervall für $\mu(Z)$ gegeben durch
```

German now reads:

```md
Zu $\alpha$ wählen wir nun $t$ als das $\frac{\alpha}{2}$-*Quantil* der $t$-Verteilung (mit $n-1$ Freiheitsgraden), das ist genau das kleinste $t$ sodass $P(T < t) \leq \frac{\alpha}{2}$ ist. So etwas hat man früher in Tabellen nachgeschlagen, heute benutzen wir einen Rechner.
Dann ist mit $\epsilon := t\frac{\sigma^\ast(x)}{\sqrt{n}}$ ein Konfidenzintervall für $\mu(Z)$ gegeben durch
```

Current English block 84:

```md
Zu $\alpha$ wählen wir nun $t$ als das $(1-\frac{\alpha}{2})$-*Quantil* der $t$-Verteilung mit $n-1$ Freiheitsgraden, also die Zahl $t > 0$ mit $P(T \leq t) = 1 - \frac{\alpha}{2}$; wegen der Symmetrie der Verteilung ist dann $P(|T| \leq t) = 1 - \alpha$. So etwas hat man früher in Tabellen nachgeschlagen, heute benutzen wir einen Rechner (`scipy.stats.t.ppf(1 - alpha/2, n - 1)`).
Dann ist mit $\epsilon := t\frac{S^\ast(x)}{\sqrt{n}}$ ein Konfidenzintervall für $\mu(Z)$ gegeben durch
```

### replace – German block `132` – English block(s) **132**

What changed in the German:

```diff
- Warum heißt $R(x)$ [-Likelihood-Quotient?-] Weil $f_1(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_1)$ ist und $f_0(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_0)$ ist, also ist $R$ der Quotient der Likelihoods. Wenn $f_0(x)=0$ ist, setzt man einfach $R = \infty$.
+ Warum heißt $R(x)$ {+Likelihoood-Quotient?+} Weil $f_1(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_1)$ ist und $f_0(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_0)$ ist, also ist $R$ der Quotient der Likelihoods. Wenn $f_0(x)=0$ ist, setzt man einfach $R = \infty$.
```

German now reads:

```md
Warum heißt $R(x)$ Likelihoood-Quotient? Weil $f_1(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_1)$ ist und $f_0(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_0)$ ist, also ist $R$ der Quotient der Likelihoods. Wenn $f_0(x)=0$ ist, setzt man einfach $R = \infty$.
```

Current English block 132:

```md
Warum heißt $R(x)$ Likelihood-Quotient? Weil $f_1(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_1)$ ist und $f_0(x)$ ein Maß für die Wahrscheinlichkeit $P(D|H_0)$ ist, also ist $R$ der Quotient der Likelihoods. Wenn $f_0(x)=0$ ist, setzt man einfach $R = \infty$.
```

### replace – German block `141` – English block(s) **141**

What changed in the German:

```diff
- Wenn man Daten hat, deren einzelne Datenpunkte unabhängig (und identisch verteilt) sind (also etwa als Stichprobe einer Zufallsvariable), die einer Normalverteilung folgen, und [-man-] die [-Standardabweichung $\sigma$ kennt,-] dann kann man einen **z-Test** (auch **Gauß-Test**) machen. Das ist die 'einfachere' Variante vom t-Test [-(s.u.). Kennt-] man [-$\sigma$ nicht und setzt die Stichprobenstandardabweichung ein, ist das bei großem $n$ noch vertretbar, weil die-] t-Verteilung [-dann praktisch eine-] Normalverteilung [-ist; die verbreitete Faustregel „$n > 30$“ ist dafür allerdings so grob, wie im Kapitel [Normalverteilung](normalverteilung.ipynb) unter *Der $N \ge 30$-Mythos* beschrieben.-]
+ Wenn man Daten hat, deren einzelne Datenpunkte unabhängig (und identisch verteilt) sind (also etwa als Stichprobe einer Zufallsvariable), die einer Normalverteilung folgen, und die {+Stichprobengröße $n$ ist deutlich über $30$,+} dann kann man einen **z-Test** (auch **Gauß-Test**) machen. Das ist die 'einfachere' Variante vom t-Test {+(s.u.), bei der+} man {+aufgrund der Größe der Stichprobe anstelle einer Student+} t-Verteilung {+mit einer+} Normalverteilung {+arbeitet.+}
```

German now reads:

```md
Wenn man Daten hat, deren einzelne Datenpunkte unabhängig (und identisch verteilt) sind (also etwa als Stichprobe einer Zufallsvariable), die einer Normalverteilung folgen, und die Stichprobengröße $n$ ist deutlich über $30$, dann kann man einen **z-Test** (auch **Gauß-Test**) machen. Das ist die 'einfachere' Variante vom t-Test (s.u.), bei der man aufgrund der Größe der Stichprobe anstelle einer Student t-Verteilung mit einer Normalverteilung arbeitet.
```

Current English block 141:

```md
Wenn man Daten hat, deren einzelne Datenpunkte unabhängig (und identisch verteilt) sind (also etwa als Stichprobe einer Zufallsvariable), die einer Normalverteilung folgen, und man die Standardabweichung $\sigma$ kennt, dann kann man einen **z-Test** (auch **Gauß-Test**) machen. Das ist die 'einfachere' Variante vom t-Test (s.u.). Kennt man $\sigma$ nicht und setzt die Stichprobenstandardabweichung ein, ist das bei großem $n$ noch vertretbar, weil die t-Verteilung dann praktisch eine Normalverteilung ist; die verbreitete Faustregel „$n > 30$“ ist dafür allerdings so grob, wie im Kapitel [Normalverteilung](normal-distribution.ipynb) unter *Der $N \ge 30$-Mythos* beschrieben.
```

### replace – German block `151` – English block(s) **151**

What changed in the German:

```diff
- | | z-Test | t-Test | |---|---|---| | $\sigma$ | bekannt (bei großem $n$: $\sigma^\ast(x)$ eingesetzt) | unbekannt, wird mitgeschätzt | | Verteilung der Statistik unter $H_0$ | Standardnormalverteilung | Student t-Verteilung mit $n-1$ Freiheitsgraden | | wann | [-$\sigma$ bekannt, sonst nur bei großem-] $n$ | [-immer; bei großem-] $n$ [-praktisch derselbe Test-] | | SciPy | `norm.ppf` | `t.ppf`, `ttest_1samp` |
+ | | z-Test | t-Test | |---|---|---| | $\sigma$ | bekannt (bei großem $n$: $\sigma^\ast(x)$ eingesetzt) | unbekannt, wird mitgeschätzt | | Verteilung der Statistik unter $H_0$ | Standardnormalverteilung | Student t-Verteilung mit $n-1$ Freiheitsgraden | | wann | $n$ {+groß (Faustregel: $n > 30$)+} | $n$ {+klein (funktioniert aber für jedes $n$)+} | | SciPy | `norm.ppf` | `t.ppf`, `ttest_1samp` |
```

German now reads:

```md
| | z-Test | t-Test |
|---|---|---|
| $\sigma$ | bekannt (bei großem $n$: $\sigma^\ast(x)$ eingesetzt) | unbekannt, wird mitgeschätzt |
| Verteilung der Statistik unter $H_0$ | Standardnormalverteilung | Student t-Verteilung mit $n-1$ Freiheitsgraden |
| wann | $n$ groß (Faustregel: $n > 30$) | $n$ klein (funktioniert aber für jedes $n$) |
| SciPy | `norm.ppf` | `t.ppf`, `ttest_1samp` |
```

Current English block 151:

```md
| | z-Test | t-Test |
|---|---|---|
| $\sigma$ | bekannt (bei großem $n$: $\sigma^\ast(x)$ eingesetzt) | unbekannt, wird mitgeschätzt |
| Verteilung der Statistik unter $H_0$ | Standardnormalverteilung | Student t-Verteilung mit $n-1$ Freiheitsgraden |
| wann | $\sigma$ bekannt, sonst nur bei großem $n$ | immer; bei großem $n$ praktisch derselbe Test |
| SciPy | `norm.ppf` | `t.ppf`, `ttest_1samp` |
```

### replace – German block `164` – English block(s) **164**

What changed in the German:

```diff
- [-Für den Zwei-Stichproben-Fall gibt es außerdem-] die [-Variante, die nur Kennzahlen braucht:-]
+ {+Intern verwendet SciPy+} die {+Methode+}
```

German now reads:

```md
Intern verwendet SciPy die Methode
```

Current English block 164:

```md
Für den Zwei-Stichproben-Fall gibt es außerdem die Variante, die nur Kennzahlen braucht:
```

### replace – German block `187` – English block(s) **187**

What changed in the German:

```diff
- ```{figure} images/xkcd-significant.png :width: 300px :align: center :name: xkcd-significant [-Randall Munroe, [xkcd 882 „Significant“](https://xkcd.com/882/) (CC BY-NC 2.5)-] (So, uh, we did the green study again and got no link. It was probably a-- "RESEARCH CONFLICTED ON GREEN JELLY BEAN/ACNE LINK; MORE STUDY RECOMMENDED!") ```
+ ```{figure} images/xkcd-significant.png :width: 300px :align: center :name: xkcd-significant {+XKCD 882: Significant+} (So, uh, we did the green study again and got no link. It was probably a-- "RESEARCH CONFLICTED ON GREEN JELLY BEAN/ACNE LINK; MORE STUDY RECOMMENDED!") ```
```

German now reads:

```md
```{figure} images/xkcd-significant.png
:width: 300px
:align: center
:name: xkcd-significant

XKCD 882: Significant (So, uh, we did the green study again and got no link. It was probably a-- "RESEARCH CONFLICTED ON GREEN JELLY BEAN/ACNE LINK; MORE STUDY RECOMMENDED!")
```
```

Current English block 187:

```md
```{figure} images/xkcd-significant.png
:width: 300px
:align: center
:name: xkcd-significant

Randall Munroe, [xkcd 882 „Significant“](https://xkcd.com/882/) (CC BY-NC 2.5) (So, uh, we did the green study again and got no link. It was probably a-- "RESEARCH CONFLICTED ON GREEN JELLY BEAN/ACNE LINK; MORE STUDY RECOMMENDED!")
```
```

### replace – German block `199` – English block(s) **199**

What changed in the German:

```diff
- Stellen wir uns vor, wir hätten ein neues Medikament gefunden, von dem wir glauben, dass es schlauer macht. Um das zu zeigen, gehen wir so vor: wir konstruieren ein Experiment, mit dem sich widerlegen lässt, dass unser Medikament schlauer macht. Dazu operationalisieren wir "schlauer werden" z.B. über eine Prüfungssituation mit kognitiven Aufgaben. Die [-Probanden-] werden zufällig in zwei Gruppen aufgeteilt. Eine Gruppe bekommt ein Placebo, die andere das Medikament, sonst ist alles gleich und niemand (auch die Durchführenden nicht) weiß, wer in welcher Gruppe ist. Danach wertet man die Daten aus - Performance in der Prüfung ist eine Variable, Gruppenzugehörigkeit die andere.
+ Stellen wir uns vor, wir hätten ein neues Medikament gefunden, von dem wir glauben, dass es schlauer macht. Um das zu zeigen, gehen wir so vor: wir konstruieren ein Experiment, mit dem sich widerlegen lässt, dass unser Medikament schlauer macht. Dazu operationalisieren wir "schlauer werden" z.B. über eine Prüfungssituation mit kognitiven Aufgaben. Die {+Probanden, wenigstens 30 an der Zahl,+} werden zufällig in zwei Gruppen aufgeteilt. Eine Gruppe bekommt ein Placebo, die andere das Medikament, sonst ist alles gleich und niemand (auch die Durchführenden nicht) weiß, wer in welcher Gruppe ist. Danach wertet man die Daten aus - Performance in der Prüfung ist eine Variable, Gruppenzugehörigkeit die andere.
```

German now reads:

```md
Stellen wir uns vor, wir hätten ein neues Medikament gefunden, von dem wir glauben, dass es schlauer macht. Um das zu zeigen, gehen wir so vor: wir konstruieren ein Experiment, mit dem sich widerlegen lässt, dass unser Medikament schlauer macht. Dazu operationalisieren wir "schlauer werden" z.B. über eine Prüfungssituation mit kognitiven Aufgaben. Die Probanden, wenigstens 30 an der Zahl, werden zufällig in zwei Gruppen aufgeteilt. Eine Gruppe bekommt ein Placebo, die andere das Medikament, sonst ist alles gleich und niemand (auch die Durchführenden nicht) weiß, wer in welcher Gruppe ist. Danach wertet man die Daten aus - Performance in der Prüfung ist eine Variable, Gruppenzugehörigkeit die andere.
```

Current English block 199:

```md
Stellen wir uns vor, wir hätten ein neues Medikament gefunden, von dem wir glauben, dass es schlauer macht. Um das zu zeigen, gehen wir so vor: wir konstruieren ein Experiment, mit dem sich widerlegen lässt, dass unser Medikament schlauer macht. Dazu operationalisieren wir "schlauer werden" z.B. über eine Prüfungssituation mit kognitiven Aufgaben. Die Probanden werden zufällig in zwei Gruppen aufgeteilt. Eine Gruppe bekommt ein Placebo, die andere das Medikament, sonst ist alles gleich und niemand (auch die Durchführenden nicht) weiß, wer in welcher Gruppe ist. Danach wertet man die Daten aus - Performance in der Prüfung ist eine Variable, Gruppenzugehörigkeit die andere.
```

### replace – German block `203` – English block(s) **203**

What changed in the German:

```diff
- Man sieht diese Nicht-Vertauschbarkeit auch bei der natürlichsprachlich formulierten Hypothese: "das Medikament wirkt nicht" ist eigentlich die Aussage "das Medikament einzunehmen oder nicht hat keinen Einfluss auf die Testperformance". [-Wie-] formalisiert man "hat einen Einfluss auf die Testperformance" mathematisch?
+ Man sieht diese Nicht-Vertauschbarkeit auch bei der natürlichsprachlich formulierten Hypothese: "das Medikament wirkt nicht" ist eigentlich die Aussage "das Medikament einzunehmen oder nicht hat keinen Einfluss auf die Testperformance". {+Wir+} formalisiert man "hat einen Einfluss auf die Testperformance" mathematisch?
```

German now reads:

```md
Man sieht diese Nicht-Vertauschbarkeit auch bei der natürlichsprachlich formulierten Hypothese: "das Medikament wirkt nicht" ist eigentlich die Aussage "das Medikament einzunehmen oder nicht hat keinen Einfluss auf die Testperformance". Wir formalisiert man "hat einen Einfluss auf die Testperformance" mathematisch?
```

Current English block 203:

```md
Man sieht diese Nicht-Vertauschbarkeit auch bei der natürlichsprachlich formulierten Hypothese: "das Medikament wirkt nicht" ist eigentlich die Aussage "das Medikament einzunehmen oder nicht hat keinen Einfluss auf die Testperformance". Wie formalisiert man "hat einen Einfluss auf die Testperformance" mathematisch?
```

### replace – German block `210` – English block(s) **210**

What changed in the German:

```diff
- * Pearson's Korrelation: $H_0$: Die zwei Samples sind [-unkorreliert ($\rho = 0$)-] Voraussetzung: beide Samples sind iid und [-gemeinsam-] normalverteilt `scipy.stats.pearsonr` * Chi-Quadrat: $H_0$: Die zwei Samples sind unabhängig Voraussetzung: die untersuchte Variable ist kategoriell, [-erwartete Häufigkeit von-] wenigstens [-$5$-] in [-jedem Feld-] der Kontingenztabelle `scipy.stats.chi2_contingency`
+ * Pearson's Korrelation: $H_0$: Die zwei Samples sind {+unabhängig+} Voraussetzung: beide Samples sind iid und normalverteilt {+mit gleicher Varianz+} `scipy.stats.pearsonr` * Chi-Quadrat: $H_0$: Die zwei Samples sind unabhängig Voraussetzung: die untersuchte Variable ist kategoriell, wenigstens {+25 Instanzen pro Eintrag+} in der Kontingenztabelle `scipy.stats.chi2_contingency`
```

German now reads:

```md
* Pearson's Korrelation:
  $H_0$: Die zwei Samples sind unabhängig
  Voraussetzung: beide Samples sind iid und normalverteilt mit gleicher Varianz
  `scipy.stats.pearsonr`
* Chi-Quadrat:
  $H_0$: Die zwei Samples sind unabhängig
  Voraussetzung: die untersuchte Variable ist kategoriell, wenigstens 25 Instanzen pro Eintrag in der Kontingenztabelle
  `scipy.stats.chi2_contingency`
```

Current English block 210:

```md
* Pearson's Korrelation:
  $H_0$: Die zwei Samples sind unkorreliert ($\rho = 0$)
  Voraussetzung: beide Samples sind iid und gemeinsam normalverteilt
  `scipy.stats.pearsonr`
* Chi-Quadrat:
  $H_0$: Die zwei Samples sind unabhängig
  Voraussetzung: die untersuchte Variable ist kategoriell, erwartete Häufigkeit von wenigstens $5$ in jedem Feld der Kontingenztabelle
  `scipy.stats.chi2_contingency`
```


## model-selection.ipynb → model-selection.ipynb

### replace – German block `c1.5` – English block(s) **c1.5**

What changed in the German:

```diff
- (Grafik aus der [-[Scikit-Learn-Dokumentation](https://scikit-learn.org/stable/modules/cross_validation.html), BSD-3-Clause)-]
+ (Grafik aus der {+Scikit-Learn-Dokumentation)+}
```

German now reads:

```md
(Grafik aus der Scikit-Learn-Dokumentation)
```

Current English block c1.5:

```md
(Grafik aus der [Scikit-Learn-Dokumentation](https://scikit-learn.org/stable/modules/cross_validation.html), BSD-3-Clause)
```

### replace – German block `c4.3` – English block(s) **c4.3**

What changed in the German:

```diff
- Bei der **k-fachen Kreuzvalidierung** versucht man diese beiden Probleme zu lösen, indem man mehrfach, nämlich k mal, das ML-System laufen lässt, jeweils mit einer anderen Aufteilung in Trainings- und Testdaten. Dazu teilt man den Trainings-Datensatz in k gleiche Teile ein (genannt *folds*), und verwendet [-im $i$-ten-] der [-$k$-] Durchläufe den [-$i$-ten-] Teil als Test (und lässt [-ihn-] beim Training weg).
+ Bei der **k-fachen Kreuzvalidierung** versucht man diese beiden Probleme zu lösen, indem man mehrfach, nämlich k mal, das ML-System laufen lässt, jeweils mit einer anderen Aufteilung in Trainings- und Testdaten. Dazu teilt man den Trainings-Datensatz in k gleiche Teile ein (genannt *folds*), und verwendet {+bei jedem+} der {+k+} Durchläufe den {+k-ten+} Teil als Test (und lässt {+diesem+} beim Training weg).
```

German now reads:

```md
Bei der **k-fachen Kreuzvalidierung** versucht man diese beiden Probleme zu lösen, indem man mehrfach, nämlich k mal, das ML-System laufen lässt, jeweils mit einer anderen Aufteilung in Trainings- und Testdaten. Dazu teilt man den Trainings-Datensatz in k gleiche Teile ein (genannt *folds*), und verwendet bei jedem der k Durchläufe den k-ten Teil als Test (und lässt diesem beim Training weg).
```

Current English block c4.3:

```md
Bei der **k-fachen Kreuzvalidierung** versucht man diese beiden Probleme zu lösen, indem man mehrfach, nämlich k mal, das ML-System laufen lässt, jeweils mit einer anderen Aufteilung in Trainings- und Testdaten. Dazu teilt man den Trainings-Datensatz in k gleiche Teile ein (genannt *folds*), und verwendet im $i$-ten der $k$ Durchläufe den $i$-ten Teil als Test (und lässt ihn beim Training weg).
```

### replace – German block `c9.1` – English block(s) **c9.1**

What changed in the German:

```diff
- Auszug [aus der [-Scikit-learn-Dokumentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualizing-cross-validation-behavior-in-scikit-learn) (BSD-3-Clause):-]
+ Auszug [aus der {+Scikit-learn-Dokumentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualizing-cross-validation-behavior-in-scikit-learn):+}
```

German now reads:

```md
Auszug [aus der Scikit-learn-Dokumentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualizing-cross-validation-behavior-in-scikit-learn):
```

Current English block c9.1:

```md
Auszug [aus der Scikit-learn-Dokumentation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#visualizing-cross-validation-behavior-in-scikit-learn) (BSD-3-Clause):
```

### replace – German block `c10.3`, `c10.4` – English block(s) **c10.3**, **c10.4**

German now reads:

```md
$$
NMI(U, V) = \dfrac{ H(U,V) }{ \texttt{mean}( H(U), H(V)) }
$$
```

Current English block c10.3:

```md
$$
NMI(U, V) = \dfrac{ I(U;V) }{ \texttt{mean}\big( H(U), H(V) \big) }, \qquad I(U;V) = H(U) + H(V) - H(U,V)
$$
```

Current English block c10.4:

```md
mit der *gemeinsamen Information* $I(U;V)$ aus dem Kapitel [Relative Entropie](relative-entropy.md): Sie ist $0$, wenn Clustering und Klassen nichts miteinander zu tun haben, und gleich $H(U) = H(V)$, wenn das eine das andere bestimmt; der Nenner normiert auf $[0,1]$.
```

### replace – German block `c11.1` – English block(s) **c11.1**

What changed in the German:

```diff
- [-Kennt man die wahren Klassen, kann man-] bewerten, ob die Cluster jeweils nur Samples einer Klasse enthalten bzw. wie stark das Clustering davon abweicht (Homogenität) und wir können bewerten, ob alle Samples einer Klasse auch nur zu einem Cluster zugeordnet sind:
+ {+Im supervised learning können wir+} bewerten, ob die Cluster jeweils nur Samples einer Klasse enthalten bzw. wie stark das Clustering davon abweicht (Homogenität) und wir können bewerten, ob alle Samples einer Klasse auch nur zu einem Cluster zugeordnet sind:
```

German now reads:

```md
Im supervised learning können wir bewerten, ob die Cluster jeweils nur Samples einer Klasse enthalten bzw. wie stark das Clustering davon abweicht (Homogenität) und wir können bewerten, ob alle Samples einer Klasse auch nur zu einem Cluster zugeordnet sind:
```

Current English block c11.1:

```md
Kennt man die wahren Klassen, kann man bewerten, ob die Cluster jeweils nur Samples einer Klasse enthalten bzw. wie stark das Clustering davon abweicht (Homogenität) und wir können bewerten, ob alle Samples einer Klasse auch nur zu einem Cluster zugeordnet sind:
```


## expectation-maximization.ipynb → expectation-maximization.ipynb

### delete – German block `c0.1` – English block(s) **c0.1**

Current English block c0.1:

```md
[Vorlesungsaufzeichnung Expectation Maximization (VL 23)](https://media.hhu.de/channel/video/data-science-vl-23-expectation-maximization-2025/e3186d8384176340f294ecf2b52c1025/167)
[Anwendung von EM (VL 24)](https://media.hhu.de/channel/video/data-science-vl-24-anwendung-von-em-2025/5997aad6bc586be623998b7954f5449c/167)
```

### replace – German block `c1.0` – English block(s) **c1.0**

What changed in the German:

```diff
- ```{admonition} Beispiel Formuliert als Expectation-Maximization-Verfahren ist das k-Means-Verfahren: 1. Initialisierung (Clustermittelpunkte festlegen) 2. Iterativ bis zur Konvergenz der Clustermittelpunkte: a. (E-Schritt): Punkte dem jeweils nächsten Clustermittelpunkt zuteilen und so zu einer Klasseneinteilung kommen b. (M-Schritt): Neue Clustermittelpunkte als Mittelwert aller Elemente einer Klasse festlegen Der E-Schritt (Expectation) heißt so, weil wir unsere Erwartung über den Wert der latenten Variable updaten. Der M-Schritt (Maximization) heißt so, weil wir eine Fitness-Funktion maximieren - konkret minimieren wir die Summe [-der quadrierten Abstände-] der Punkte zu den ihnen zugeteilten Clustermittelpunkten. ```
+ ```{admonition} Beispiel Formuliert als Expectation-Maximization-Verfahren ist das k-Means-Verfahren: 1. Initialisierung (Clustermittelpunkte festlegen) 2. Iterativ bis zur Konvergenz der Clustermittelpunkte: a. (E-Schritt): Punkte dem jeweils nächsten Clustermittelpunkt zuteilen und so zu einer Klasseneinteilung kommen b. (M-Schritt): Neue Clustermittelpunkte als Mittelwert aller Elemente einer Klasse festlegen Der E-Schritt (Expectation) heißt so, weil wir unsere Erwartung über den Wert der latenten Variable updaten. Der M-Schritt (Maximization) heißt so, weil wir eine Fitness-Funktion maximieren - konkret minimieren wir die Summe {+aller Entferungen+} der Punkte zu den ihnen zugeteilten Clustermittelpunkten. ```
```

German now reads:

```md
```{admonition} Beispiel
Formuliert als Expectation-Maximization-Verfahren ist das k-Means-Verfahren:

1. Initialisierung (Clustermittelpunkte festlegen)
2. Iterativ bis zur Konvergenz der Clustermittelpunkte:
   a. (E-Schritt): Punkte dem jeweils nächsten Clustermittelpunkt zuteilen und so zu einer Klasseneinteilung kommen
   b. (M-Schritt): Neue Clustermittelpunkte als Mittelwert aller Elemente einer Klasse festlegen

Der E-Schritt (Expectation) heißt so, weil wir unsere Erwartung über den Wert der latenten Variable updaten.

Der M-Schritt (Maximization) heißt so, weil wir eine Fitness-Funktion maximieren - konkret minimieren wir die Summe aller Entferungen der Punkte zu den ihnen zugeteilten Clustermittelpunkten.
```
```

Current English block c1.0:

```md
```{admonition} Beispiel
Formuliert als Expectation-Maximization-Verfahren ist das k-Means-Verfahren:

1. Initialisierung (Clustermittelpunkte festlegen)
2. Iterativ bis zur Konvergenz der Clustermittelpunkte:
   a. (E-Schritt): Punkte dem jeweils nächsten Clustermittelpunkt zuteilen und so zu einer Klasseneinteilung kommen
   b. (M-Schritt): Neue Clustermittelpunkte als Mittelwert aller Elemente einer Klasse festlegen

Der E-Schritt (Expectation) heißt so, weil wir unsere Erwartung über den Wert der latenten Variable updaten.

Der M-Schritt (Maximization) heißt so, weil wir eine Fitness-Funktion maximieren - konkret minimieren wir die Summe der quadrierten Abstände der Punkte zu den ihnen zugeteilten Clustermittelpunkten.
```
```

### replace – German block `c2.1` – English block(s) **c2.1**

What changed in the German:

```diff
- Wenn wir von Daten in $\mathbb{R}^d$ Einteilungen in $k$ Klassen (Label) gegeben haben, können wir für jeden Teildatensatz aller Punkte einer Klasse die Sample-Kovarianz und den Sample-Erwartungswert ausrechnen und damit eine [-$d$-variate-] Normalverteilung aufstellen, die diesen Teildatensatz modelliert.
+ Wenn wir von Daten in $\mathbb{R}^d$ Einteilungen in $k$ Klassen (Label) gegeben haben, können wir für jeden Teildatensatz aller Punkte einer Klasse die Sample-Kovarianz und den Sample-Erwartungswert ausrechnen und damit eine {+$n$-variate+} Normalverteilung aufstellen, die diesen Teildatensatz modelliert.
```

German now reads:

```md
Wenn wir von Daten in $\mathbb{R}^d$ Einteilungen in $k$ Klassen (Label) gegeben haben, können wir für jeden Teildatensatz aller Punkte einer Klasse die Sample-Kovarianz und den Sample-Erwartungswert ausrechnen und damit eine $n$-variate Normalverteilung aufstellen, die diesen Teildatensatz modelliert.
```

Current English block c2.1:

```md
Wenn wir von Daten in $\mathbb{R}^d$ Einteilungen in $k$ Klassen (Label) gegeben haben, können wir für jeden Teildatensatz aller Punkte einer Klasse die Sample-Kovarianz und den Sample-Erwartungswert ausrechnen und damit eine $d$-variate Normalverteilung aufstellen, die diesen Teildatensatz modelliert.
```

### replace – German block `c8.1` – English block(s) **c8.1**

What changed in the German:

```diff
- $$ \begin{aligned} P(Y = j\ |\ \theta) =& p_j \\ P(X=x\ |\ Y=j, \theta) =& f_j(x,\ \mu_j,\Sigma_j) \\ P(X=x\ |\ \theta) =& \sum_{j=1}^k P(X=x,\ Y=j\ |\ \theta) \\ =& \sum_{j=1}^k P(Y = [-j\ |\ \theta)\,-] P(X=x\ |\ Y=j, \theta). \end{aligned} $$
+ $$ \begin{aligned} P(Y = j\ |\ \theta) =& p_j \\ P(X=x\ |\ Y=j, \theta) =& f_j(x,\ \mu_j,\Sigma_j) \\ P(X=x\ |\ \theta) =& \sum_{j=1}^k P(X=x,\ Y=j\ |\ \theta) \\ =& \sum_{j=1}^k P(Y = {+j, \theta)+} P(X=x\ |\ Y=j, \theta). \end{aligned} $$
```

German now reads:

```md
$$
\begin{aligned}
P(Y = j\ |\ \theta)      =& p_j \\
P(X=x\   |\ Y=j, \theta) =& f_j(x,\ \mu_j,\Sigma_j) \\
P(X=x\   |\ \theta)      =& \sum_{j=1}^k P(X=x,\ Y=j\ |\ \theta) \\
                         =& \sum_{j=1}^k P(Y = j, \theta) P(X=x\ |\ Y=j, \theta).
\end{aligned}
$$
```

Current English block c8.1:

```md
$$
\begin{aligned}
P(Y = j\ |\ \theta)      =& p_j \\
P(X=x\   |\ Y=j, \theta) =& f_j(x,\ \mu_j,\Sigma_j) \\
P(X=x\   |\ \theta)      =& \sum_{j=1}^k P(X=x,\ Y=j\ |\ \theta) \\
                         =& \sum_{j=1}^k P(Y = j\ |\ \theta)\, P(X=x\ |\ Y=j, \theta).
\end{aligned}
$$
```

### replace – German block `c9.2` – English block(s) **c9.2**

What changed in the German:

```diff
- $$ \begin{aligned} \ell(\theta) =& \log P(X=x\ |\ \theta) \\ =& \log \left( \sum_{j=1}^k P(X=x, Y=j\ |\ \theta) \right) \\ =& \log \left( \sum_{j=1}^k p_j f_j(x\ |\ [-\theta_j)-] \right) \end{aligned} $$
+ $$ \begin{aligned} \ell(\theta) =& \log P(X=x\ |\ \theta) \\ =& \log \left( \sum_{j=1}^k P(X=x, Y=j\ |\ \theta) \right) \\ =& \log \left( \sum_{j=1}^k p_j f_j(x\ |\ {+\theta_i)+} \right) \end{aligned} $$
```

German now reads:

```md
$$
\begin{aligned}
\ell(\theta) =& \log P(X=x\ |\ \theta) \\
             =& \log \left( \sum_{j=1}^k P(X=x, Y=j\ |\ \theta)  \right) \\
             =& \log \left( \sum_{j=1}^k p_j f_j(x\ |\ \theta_i) \right)
\end{aligned}
$$
```

Current English block c9.2:

```md
$$
\begin{aligned}
\ell(\theta) =& \log P(X=x\ |\ \theta) \\
             =& \log \left( \sum_{j=1}^k P(X=x, Y=j\ |\ \theta)  \right) \\
             =& \log \left( \sum_{j=1}^k p_j f_j(x\ |\ \theta_j) \right)
\end{aligned}
$$
```

### replace – German block `c9.6` – English block(s) **c9.6**

What changed in the German:

```diff
- $$ \ell(\theta) \geq \sum_{j=1}^k p_j \log f_j(x\ |\ [-\theta_j)-] $$
+ $$ \ell(\theta) \geq \sum_{j=1}^k p_j \log f_j(x\ |\ {+\theta_i)+} $$
```

German now reads:

```md
$$
\ell(\theta) \geq \sum_{j=1}^k p_j \log f_j(x\ |\ \theta_i)
$$
```

Current English block c9.6:

```md
$$
\ell(\theta) \geq \sum_{j=1}^k p_j \log f_j(x\ |\ \theta_j)
$$
```

### replace – German block `c11.2` – English block(s) **c11.2**

What changed in the German:

```diff
- Die vollständigen Daten sind also $(x_i,y_i)$, was [-wir-] mit $(X,Y)$ modellieren.
+ Die vollständigen Daten sind also $(x_i,y_i)$, was {+mir+} mit $(X,Y)$ modellieren.
```

German now reads:

```md
Die vollständigen Daten sind also $(x_i,y_i)$, was mir mit $(X,Y)$ modellieren.
```

Current English block c11.2:

```md
Die vollständigen Daten sind also $(x_i,y_i)$, was wir mit $(X,Y)$ modellieren.
```

### replace – German block `c11.5` – English block(s) **c11.5**

What changed in the German:

```diff
- $$ \begin{aligned} \ell_c(\theta) = \log P((X,Y)|\theta) =& \sum_{i=1}^n \log P(X=x_i, Y=y_i\ |\ \theta) \\ & \sum_{i=1}^n \log \prod_{j=1}^k {P(X=x_i, [-Y=j\-] |\ \theta)}^{Y_{ij}} \\ & \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \log P(X=x_i, [-Y=j\-] |\ \theta) \end{aligned} $$
+ $$ \begin{aligned} \ell_c(\theta) = \log P((X,Y)|\theta) =& \sum_{i=1}^n \log P(X=x_i, Y=y_i\ |\ \theta) \\ & \sum_{i=1}^n \log \prod_{j=1}^k {P(X=x_i, {+Y=y_i\+} |\ \theta)}^{Y_{ij}} \\ & \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \log P(X=x_i, {+Y=y_i\+} |\ \theta) \end{aligned} $$
```

German now reads:

```md
$$
\begin{aligned}
\ell_c(\theta) = \log P((X,Y)|\theta) =& \sum_{i=1}^n \log P(X=x_i, Y=y_i\ |\ \theta) \\
                                       & \sum_{i=1}^n \log \prod_{j=1}^k {P(X=x_i, Y=y_i\ |\ \theta)}^{Y_{ij}} \\
                                       & \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \log P(X=x_i, Y=y_i\ |\ \theta)
\end{aligned}
$$
```

Current English block c11.5:

```md
$$
\begin{aligned}
\ell_c(\theta) = \log P((X,Y)|\theta) =& \sum_{i=1}^n \log P(X=x_i, Y=y_i\ |\ \theta) \\
                                       & \sum_{i=1}^n \log \prod_{j=1}^k {P(X=x_i, Y=j\ |\ \theta)}^{Y_{ij}} \\
                                       & \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \log P(X=x_i, Y=j\ |\ \theta)
\end{aligned}
$$
```

### replace – German block `c11.12` – English block(s) **c11.12**

What changed in the German:

```diff
- $$ \begin{aligned} \mathbb{E}_{Y \sim q} \ell_c(\theta) =& \mathbb{E}_{Y \sim q} \left( \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \left( \log p_{y_i} + \log f_{y_i}(x_i\ |\ [-\theta_{y_i})-] \right) \right) \\ =& \sum_{i=1}^n \sum_{j=1}^k \mathbb{E}_{Y \sim q} Y_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ [-\theta_j)-] \right) \\ =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ [-\theta_j)-] \right). \end{aligned} $$
+ $$ \begin{aligned} \mathbb{E}_{Y \sim q} \ell_c(\theta) =& \mathbb{E}_{Y \sim q} \left( \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \left( \log p_{y_i} + \log f_{y_i}(x_i\ |\ {+\theta_i)+} \right) \right) \\ =& \sum_{i=1}^n \sum_{j=1}^k \mathbb{E}_{Y \sim q} Y_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ {+\theta_i)+} \right) \\ =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ {+\theta_i)+} \right). \end{aligned} $$
```

German now reads:

```md
$$
\begin{aligned}
\mathbb{E}_{Y \sim q} \ell_c(\theta) =& \mathbb{E}_{Y \sim q} \left( \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \left( \log p_{y_i} + \log f_{y_i}(x_i\ |\ \theta_i) \right) \right) \\
 =& \sum_{i=1}^n \sum_{j=1}^k \mathbb{E}_{Y \sim q} Y_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ \theta_i) \right) \\
 =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ \theta_i) \right).
\end{aligned}
$$
```

Current English block c11.12:

```md
$$
\begin{aligned}
\mathbb{E}_{Y \sim q} \ell_c(\theta) =& \mathbb{E}_{Y \sim q} \left( \sum_{i=1}^n \sum_{j=1}^k Y_{ij} \left( \log p_{y_i} + \log f_{y_i}(x_i\ |\ \theta_{y_i}) \right) \right) \\
 =& \sum_{i=1}^n \sum_{j=1}^k \mathbb{E}_{Y \sim q} Y_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ \theta_j) \right) \\
 =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij} \left( \log p_{j} + \log f_{j}(x_i\ |\ \theta_j) \right).
\end{aligned}
$$
```

### replace – German block `c11.18` – English block(s) **c11.18**

What changed in the German:

```diff
- Das ist für $\theta=\vartheta$ die erwartete vollständige-Daten log-Likelihood unter unserer Annahme $q$ an die Verteilung der latenten Variable $Y$. Wir bemerken noch, dass der andere Term $\log P(X=x_i, Y=j) = \left( \log p_{j} + \log f_{j}(x_i\ |\ [-\theta_j)-] \right)$ von $\theta$ abhängt, nicht von $\vartheta$.
+ Das ist für $\theta=\vartheta$ die erwartete vollständige-Daten log-Likelihood unter unserer Annahme $q$ an die Verteilung der latenten Variable $Y$. Wir bemerken noch, dass der andere Term $\log P(X=x_i, Y=j) = \left( \log p_{j} + \log f_{j}(x_i\ |\ {+\theta_i)+} \right)$ von $\theta$ abhängt, nicht von $\vartheta$.
```

German now reads:

```md
Das ist für $\theta=\vartheta$ die erwartete vollständige-Daten log-Likelihood unter unserer Annahme $q$ an die Verteilung der latenten Variable $Y$.
Wir bemerken noch, dass der andere Term $\log P(X=x_i, Y=j) = \left( \log p_{j} + \log f_{j}(x_i\ |\ \theta_i) \right)$ von $\theta$ abhängt, nicht von $\vartheta$.
```

Current English block c11.18:

```md
Das ist für $\theta=\vartheta$ die erwartete vollständige-Daten log-Likelihood unter unserer Annahme $q$ an die Verteilung der latenten Variable $Y$.
Wir bemerken noch, dass der andere Term $\log P(X=x_i, Y=j) = \left( \log p_{j} + \log f_{j}(x_i\ |\ \theta_j) \right)$ von $\theta$ abhängt, nicht von $\vartheta$.
```

### replace – German block `c11.27`, `c11.28`, `c11.29`, `c11.30` – English block(s) **c11.27**, **c11.28**, **c11.29**, **c11.30**

What changed in the German:

```diff
- $$ \begin{aligned} \ell(\theta) \geq& L(\theta, q) = \sum_{j=1}^k q(j) \log \left( \frac{P(X=x, Y=j\ |\ \theta)}{q(j)} \right) \\ & = \sum_{j=1}^k q(j) \log \left( \frac{ P(Y=j\ |\ X=x, \theta) P(X=x\ |\ \theta) }{q(j)} \right) \\ & = \sum_{j=1}^k q(j) \log \left( \frac{P(Y=j\ |\ X=x, \theta)}{q(j)} \right) \qquad + \sum_{j=1}^k q(j) \log\left( P(X=x\ |\ \theta) \right) \\ & = [--H\big(q \,\Vert\, P(Y \mid X=x, \theta)\big)-] + \ell(\theta). \end{aligned} $$
+ $$ \begin{aligned} \ell(\theta) \geq& L(\theta, q) = \sum_{j=1}^k q(j) \log \left( \frac{P(X=x, Y=j\ |\ \theta)}{q(j)} \right) \\ & = \sum_{j=1}^k q(j) \log \left( \frac{ P(Y=j\ |\ X=x, \theta) P(X=x\ |\ \theta) }{q(j)} \right) \\ & = \sum_{j=1}^k q(j) \log \left( \frac{P(Y=j\ |\ X=x, \theta)}{q(j)} \right) \qquad + \sum_{j=1}^k q(j) \log\left( P(X=x\ |\ \theta) \right) \\ & = {+-H(q\ |\ Y_{|X=x}, \theta)+} + \ell(\theta). \end{aligned} $$
- Die Differenz zwischen $\ell(\theta)$ und $L(\theta,q)$ ist also genau die relative Entropie der geschätzten Verteilung $q$ zur tatsächlichen Verteilung [-$P(Y \mid X=x, \theta)$ (in der Notation des Kapitels [Relative Entropie](relative-entropie.md)):-]
+ Die Differenz zwischen $\ell(\theta)$ und $L(\theta,q)$ ist also genau die relative Entropie der geschätzten Verteilung $q$ zur tatsächlichen Verteilung {+$Y_{|X=x}$:+}
- $$ \ell(\theta) - L(\theta, q) = [-H\big(q \,\Vert\, P(Y \mid X=x, \theta)\big)-] $$
+ $$ \ell(\theta) - L(\theta, q) = {+H(q\ |\ Y_{|X=x}, \theta)+} $$
- Damit ist auch $\ell(\theta) - Q(\theta,\theta) = [-H\big(q \,\Vert\, P(Y \mid X=x, \theta)\big)-] + H(q)$, wir verstehen also ganz genau, inwiefern sich $\ell(\theta)$ mit $Q(\theta,\theta)$ maximieren lässt.
+ Damit ist auch $\ell(\theta) - Q(\theta,\theta) = {+H(q\ |\ Y_{|X=x}, \theta)+} + H(q)$, wir verstehen also ganz genau, inwiefern sich $\ell(\theta)$ mit $Q(\theta,\theta)$ maximieren lässt.
```

German now reads:

```md
$$
\begin{aligned}
\ell(\theta) \geq& L(\theta, q) = \sum_{j=1}^k q(j) \log \left( \frac{P(X=x, Y=j\ |\ \theta)}{q(j)} \right) \\
                 & = \sum_{j=1}^k q(j) \log \left( \frac{ P(Y=j\ |\ X=x, \theta) P(X=x\ |\ \theta) }{q(j)} \right) \\
                 & = \sum_{j=1}^k q(j) \log \left( \frac{P(Y=j\ |\ X=x, \theta)}{q(j)} \right) \qquad + \sum_{j=1}^k q(j) \log\left( P(X=x\ |\ \theta) \right) \\
                 & = -H(q\ |\ Y_{|X=x}, \theta) + \ell(\theta).
\end{aligned}
$$
Die Differenz zwischen $\ell(\theta)$ und $L(\theta,q)$ ist also genau die relative Entropie der geschätzten Verteilung $q$ zur tatsächlichen Verteilung $Y_{|X=x}$:
$$
\ell(\theta) - L(\theta, q) = H(q\ |\ Y_{|X=x}, \theta)
$$
Damit ist auch $\ell(\theta) - Q(\theta,\theta) = H(q\ |\ Y_{|X=x}, \theta) + H(q)$, wir verstehen also ganz genau, inwiefern sich $\ell(\theta)$ mit $Q(\theta,\theta)$ maximieren lässt.
```

Current English block c11.27:

```md
$$
\begin{aligned}
\ell(\theta) \geq& L(\theta, q) = \sum_{j=1}^k q(j) \log \left( \frac{P(X=x, Y=j\ |\ \theta)}{q(j)} \right) \\
                 & = \sum_{j=1}^k q(j) \log \left( \frac{ P(Y=j\ |\ X=x, \theta) P(X=x\ |\ \theta) }{q(j)} \right) \\
                 & = \sum_{j=1}^k q(j) \log \left( \frac{P(Y=j\ |\ X=x, \theta)}{q(j)} \right) \qquad + \sum_{j=1}^k q(j) \log\left( P(X=x\ |\ \theta) \right) \\
                 & = -H\big(q \,\Vert\, P(Y \mid X=x, \theta)\big) + \ell(\theta).
\end{aligned}
$$
```

Current English block c11.28:

```md
Die Differenz zwischen $\ell(\theta)$ und $L(\theta,q)$ ist also genau die relative Entropie der geschätzten Verteilung $q$ zur tatsächlichen Verteilung $P(Y \mid X=x, \theta)$ (in der Notation des Kapitels [Relative Entropie](relative-entropy.md)):
```

Current English block c11.29:

```md
$$
\ell(\theta) - L(\theta, q) = H\big(q \,\Vert\, P(Y \mid X=x, \theta)\big)
$$
```

Current English block c11.30:

```md
Damit ist auch $\ell(\theta) - Q(\theta,\theta) = H\big(q \,\Vert\, P(Y \mid X=x, \theta)\big) + H(q)$, wir verstehen also ganz genau, inwiefern sich $\ell(\theta)$ mit $Q(\theta,\theta)$ maximieren lässt.
```

### replace – German block `c13.4` – English block(s) **c13.4**

What changed in the German:

```diff
- $$ f_j(x) = f_j(x, \mu_j, \sigma_j) = [-\dfrac{1}{\sqrt{2\pi}\,\sigma_j}\,-] e^{-\frac{(x-\mu_j)^2}{2\sigma_j^2}}. $$
+ $$ f_j(x) = f_j(x, \mu_j, \sigma_j) = {+\dfrac{1}{\sqrt{2\pi \sigma_j}}+} e^{-\frac{(x-\mu_j)^2}{2\sigma_j^2}}. $$
```

German now reads:

```md
$$
f_j(x) = f_j(x, \mu_j, \sigma_j) = \dfrac{1}{\sqrt{2\pi \sigma_j}} e^{-\frac{(x-\mu_j)^2}{2\sigma_j^2}}.
$$
```

Current English block c13.4:

```md
$$
f_j(x) = f_j(x, \mu_j, \sigma_j) = \dfrac{1}{\sqrt{2\pi}\,\sigma_j}\, e^{-\frac{(x-\mu_j)^2}{2\sigma_j^2}}.
$$
```

### replace – German block `c13.11`, `c13.12` – English block(s) **c13.11**, **c13.12**

What changed in the German:

```diff
- $$ \begin{aligned} \frac{d}{d\mu_j} \log f_j(x_i) =& - [-\frac{\frac{d}{d\mu_j}(x_i-\mu_j)^2}{2\sigma_j^2}-] = [-\frac{x_i-\mu_j}{\sigma_j^2}-] \\ \frac{d}{d\mu_j} Q(\theta, \theta^{(t)}) =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij}(\vartheta) \frac{d}{d\mu_j} \log f_{j}(x_i\ |\ \theta_j) \\ =& \sum_{i=1}^n \tau_{ij}(\vartheta) [-\frac{x_i-\mu_j}{\sigma_j^2}.-] \end{aligned} $$
+ $$ \begin{aligned} \frac{d}{d\mu_j} \log f_j(x_i) =& - {+\frac{\frac{d}{d\mu_j}(x_i-\mu_j)^2}{2\sigma_j}+} = {+\frac{2(x_i-\mu_j)}{2\sigma_j}+} \\ \frac{d}{d\mu_j} Q(\theta, \theta^{(t)}) =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij}(\vartheta) \frac{d}{d\mu_j} \log f_{j}(x_i\ |\ \theta_j) \\ =& \sum_{i=1}^n \tau_{ij}(\vartheta) {+\frac{2(x-\mu_j)}{2\sigma_j}.+} \end{aligned} $$
- Wir können mit [-$\sigma_j^2$-] durchmultiplizieren und nach $\mu_j$ umstellen, dann erhalten wir die geschlossene Formel
+ Wir können mit {+$2\sigma_j$+} durchmultiplizieren und nach $\mu_j$ umstellen, dann erhalten wir die geschlossene Formel
```

German now reads:

```md
$$
\begin{aligned}
\frac{d}{d\mu_j} \log f_j(x_i) =& - \frac{\frac{d}{d\mu_j}(x_i-\mu_j)^2}{2\sigma_j} = \frac{2(x_i-\mu_j)}{2\sigma_j} \\
\frac{d}{d\mu_j} Q(\theta, \theta^{(t)}) =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij}(\vartheta) \frac{d}{d\mu_j} \log f_{j}(x_i\ |\ \theta_j) \\
 =& \sum_{i=1}^n \tau_{ij}(\vartheta) \frac{2(x-\mu_j)}{2\sigma_j}.
\end{aligned}
$$
Wir können mit $2\sigma_j$ durchmultiplizieren und nach $\mu_j$ umstellen, dann erhalten wir die geschlossene Formel
```

Current English block c13.11:

```md
$$
\begin{aligned}
\frac{d}{d\mu_j} \log f_j(x_i) =& - \frac{\frac{d}{d\mu_j}(x_i-\mu_j)^2}{2\sigma_j^2} = \frac{x_i-\mu_j}{\sigma_j^2} \\
\frac{d}{d\mu_j} Q(\theta, \theta^{(t)}) =& \sum_{i=1}^n \sum_{j=1}^k \tau_{ij}(\vartheta) \frac{d}{d\mu_j} \log f_{j}(x_i\ |\ \theta_j) \\
 =& \sum_{i=1}^n \tau_{ij}(\vartheta) \frac{x_i-\mu_j}{\sigma_j^2}.
\end{aligned}
$$
```

Current English block c13.12:

```md
Wir können mit $\sigma_j^2$ durchmultiplizieren und nach $\mu_j$ umstellen, dann erhalten wir die geschlossene Formel
```

### replace – German block `c13.15` – English block(s) **c13.15**

What changed in the German:

```diff
- $$ \begin{aligned} \frac{d}{d\sigma_j} \log f_j(x_i) =& -\frac{1}{\sigma_j} + \frac{(x_i-\mu_j)^2}{\sigma_j^3} \\ \frac{d}{d\sigma_j} Q(\theta, \theta^{(t)}) =& [-\sum_{i=1}^n-] \tau_{ij} \left( \frac{(x_i-\mu_j)^2}{\sigma_j^3} -\frac{1}{\sigma_j} \right). \end{aligned} $$
+ $$ \begin{aligned} \frac{d}{d\sigma_j} \log f_j(x_i) =& -\frac{1}{\sigma_j} + \frac{(x_i-\mu_j)^2}{\sigma_j^3} \\ \frac{d}{d\sigma_j} Q(\theta, \theta^{(t)}) =& {+\sum_{i=1}^N+} \tau_{ij} \left( \frac{(x_i-\mu_j)^2}{\sigma_j^3} -\frac{1}{\sigma_j} \right). \end{aligned} $$
```

German now reads:

```md
$$
\begin{aligned}
\frac{d}{d\sigma_j} \log f_j(x_i) =& -\frac{1}{\sigma_j} + \frac{(x_i-\mu_j)^2}{\sigma_j^3} \\
\frac{d}{d\sigma_j} Q(\theta, \theta^{(t)}) =& \sum_{i=1}^N \tau_{ij} \left( \frac{(x_i-\mu_j)^2}{\sigma_j^3} -\frac{1}{\sigma_j} \right).
\end{aligned}
$$
```

Current English block c13.15:

```md
$$
\begin{aligned}
\frac{d}{d\sigma_j} \log f_j(x_i) =& -\frac{1}{\sigma_j} + \frac{(x_i-\mu_j)^2}{\sigma_j^3} \\
\frac{d}{d\sigma_j} Q(\theta, \theta^{(t)}) =& \sum_{i=1}^n \tau_{ij} \left( \frac{(x_i-\mu_j)^2}{\sigma_j^3} -\frac{1}{\sigma_j} \right).
\end{aligned}
$$
```

### replace – German block `c13.17` – English block(s) **c13.17**

What changed in the German:

```diff
- $${\left(\sigma_j^{(t+1)}\right)}^2 = [-\frac{\sum_{i=1}^n \tau_{ij}(x_i-\mu_j)^2}{\sum_{i=1}^n-] \tau_{ij}}$$
+ $${\left(\sigma_j^{(t+1)}\right)}^2 = {+\frac{\sum_{i=1}^N \tau_{ij}(x_i-\mu_j)^2}{\sum_{i=1}^N+} \tau_{ij}}$$
```

German now reads:

```md
$${\left(\sigma_j^{(t+1)}\right)}^2 = \frac{\sum_{i=1}^N \tau_{ij}(x_i-\mu_j)^2}{\sum_{i=1}^N \tau_{ij}}$$
```

Current English block c13.17:

```md
$${\left(\sigma_j^{(t+1)}\right)}^2 = \frac{\sum_{i=1}^n \tau_{ij}(x_i-\mu_j)^2}{\sum_{i=1}^n \tau_{ij}}$$
```

### replace – German block `c14.4`, `c14.5` – English block(s) **c14.4**, **c14.5**

What changed in the German:

```diff
- $$ \begin{aligned} \mu_j^{(t+1)} =& \frac{\sum_{i=1}^n \widetilde{\tau_{ij}} x_i }{ \sum_{i=1}^n \widetilde{\tau_{ij}}} \\ =& [-\frac{1}{n_j} \sum_{i:\ y_i = j} x_i, \qquad n_j := \sum_{i=1}^n-] \widetilde{\tau_{ij}} [-= \big|\{ i : y_i = j \}\big|,-] \end{aligned} $$
+ $$ \begin{aligned} \mu_j^{(t+1)} =& \frac{\sum_{i=1}^n \widetilde{\tau_{ij}} x_i }{ \sum_{i=1}^n \widetilde{\tau_{ij}}} \\ =& {+\frac{\sum_{i=1}^n+} \widetilde{\tau_{ij}} {+x_i }{n} \\ =& \sum_{i=1, y_i=j}^n \frac{x_i}{n}+} \end{aligned} $$
- [-wobei $y_i$ die Klasse ist, der $x_i$ hart zugewiesen wurde.-] Das ist genau das arithmetische Mittel der [-$n_j$ Punkte-] $x_i$, die in Klasse $j$ liegen. Verwendet man stattdessen das soft assignment, ist es ein gewichtetes Mittel der $x_i$, das denjenigen Punkten mit ungewisserer Zuteilung weniger Gewicht gibt- auch eine offensichtliche Optimierung gegenüber klassischem k-Means.
+ Das ist genau das arithmetische Mittel der $x_i$, die in Klasse $j$ liegen. Verwendet man stattdessen das soft assignment, ist es ein gewichtetes Mittel der $x_i$, das denjenigen Punkten mit ungewisserer Zuteilung weniger Gewicht gibt- auch eine offensichtliche Optimierung gegenüber klassischem k-Means.
```

German now reads:

```md
$$
\begin{aligned}
\mu_j^{(t+1)} =& \frac{\sum_{i=1}^n \widetilde{\tau_{ij}} x_i }{ \sum_{i=1}^n \widetilde{\tau_{ij}}} \\
              =& \frac{\sum_{i=1}^n \widetilde{\tau_{ij}} x_i }{n} \\
              =& \sum_{i=1, y_i=j}^n \frac{x_i}{n}
\end{aligned}
$$
Das ist genau das arithmetische Mittel der $x_i$, die in Klasse $j$ liegen. Verwendet man stattdessen das soft assignment, ist es ein gewichtetes Mittel der $x_i$, das denjenigen Punkten mit ungewisserer Zuteilung weniger Gewicht gibt- auch eine offensichtliche Optimierung gegenüber klassischem k-Means.
```

Current English block c14.4:

```md
$$
\begin{aligned}
\mu_j^{(t+1)} =& \frac{\sum_{i=1}^n \widetilde{\tau_{ij}} x_i }{ \sum_{i=1}^n \widetilde{\tau_{ij}}} \\
              =& \frac{1}{n_j} \sum_{i:\ y_i = j} x_i, \qquad n_j := \sum_{i=1}^n \widetilde{\tau_{ij}} = \big|\{ i : y_i = j \}\big|,
\end{aligned}
$$
```

Current English block c14.5:

```md
wobei $y_i$ die Klasse ist, der $x_i$ hart zugewiesen wurde. Das ist genau das arithmetische Mittel der $n_j$ Punkte $x_i$, die in Klasse $j$ liegen. Verwendet man stattdessen das soft assignment, ist es ein gewichtetes Mittel der $x_i$, das denjenigen Punkten mit ungewisserer Zuteilung weniger Gewicht gibt- auch eine offensichtliche Optimierung gegenüber klassischem k-Means.
```

### replace – German block `c22` – English block(s) **c22**

What changed in the German:

```diff
- import matplotlib.animation as animation from IPython import display as ipydisplay import io, base64 from sklearn.cluster import KMeans def init_theta(samples): pis = np.ones(2) / 2 mus = np.random.random(2) * 2*np.std(samples)\ + np.mean(samples) # a better way would be: #mus = KMeans(2).fit(samples.reshape(-1,1)).cluster_centers_ sigmas = np.ones(2) return pis, mus, sigmas def em_iteration_draw(run_nr, ax, samples, history): pis, mus, sigmas, taus = history[run_nr][0:4] ys = np.zeros_like(samples, dtype=bool) if(len(taus) == len(samples)): for i in range(len(samples)): if(taus[i,1] > 0.5): ys[i] = 1 ax.clear() ax.set_ylim(0, 0.2) ax.hist(samples, bins=51, density=True, alpha=0.5, label="Daten") if(len(taus) == len(samples)): ax.scatter(samples[ys], np.zeros_like(samples[ys]), alpha=0.4, c=taus[ys][:,0], label="Als 0 klassifiziert") xmin, xmax = ax.get_xlim() norm_pdf_domain = np.linspace(xmin, xmax, 100) ax.plot(norm_pdf_domain, pis[0]*norm.pdf(norm_pdf_domain, mus[0], sigmas[0]) + pis[1]*norm.pdf(norm_pdf_domain, mus[1], sigmas[1]), color='blue', label="Schätzung Nr. %d" % (run_nr)) ax.plot(norm_pdf_domain, pi *norm.pdf(norm_pdf_domain, real_mu_1, real_sigma_1) + (1-pi)*norm.pdf(norm_pdf_domain, real_mu_2, real_sigma_2), color='red', label="Echte Verteilung") ax.set_xlabel("$x$") ax.set_ylabel("Dichte") ax.legend() def plot_ani(samples, history): fig, ax = plt.subplots(figsize=(10, 10)) ani = animation.FuncAnimation(fig, em_iteration_draw, fargs=(ax, samples, history), interval=1000, frames=len(history)) video = ani.to_html5_video() # Zusätzlich das letzte Bild als PNG ausgeben: der Web-Export zeigt das Video, # der PDF-Export (der kein HTML kann) verwendet das Standbild. png = io.BytesIO() fig.savefig(png, format='png') ipydisplay.display({'text/html': video, 'image/png': base64.b64encode(png.getvalue()).decode('ascii')}, raw=True) plt.close() max_iter = 210 tol = 0.01 pis, mus, sigmas = init_theta(mixture_samples) taus = [-np.zeros((len(mixture_samples),-] len(pis))) # record all values in each iteration step for plotting: history = [(pis, mus, sigmas, taus, 0)] for i in range(max_iter): pis, mus, sigmas = history[-1][0:3] history += [EM(mixture_samples, pis, mus, sigmas)] if np.abs(history[-1][-1] - history[-2][-1]) < tol: break plot_ani(mixture_samples, history)
+ import matplotlib.animation as animation from IPython import display as ipydisplay import io, base64 from sklearn.cluster import KMeans def init_theta(samples): pis = np.ones(2) / 2 mus = np.random.random(2) * 2*np.std(samples)\ + np.mean(samples) # a better way would be: #mus = KMeans(2).fit(samples.reshape(-1,1)).cluster_centers_ sigmas = np.ones(2) return pis, mus, sigmas def em_iteration_draw(run_nr, ax, samples, history): pis, mus, sigmas, taus = history[run_nr][0:4] ys = np.zeros_like(samples, dtype=bool) if(len(taus) == len(samples)): for i in range(len(samples)): if(taus[i,1] > 0.5): ys[i] = 1 ax.clear() ax.set_ylim(0, 0.2) ax.hist(samples, bins=51, density=True, alpha=0.5, label="Daten") if(len(taus) == len(samples)): ax.scatter(samples[ys], np.zeros_like(samples[ys]), alpha=0.4, c=taus[ys][:,0], label="Als 0 klassifiziert") xmin, xmax = ax.get_xlim() norm_pdf_domain = np.linspace(xmin, xmax, 100) ax.plot(norm_pdf_domain, pis[0]*norm.pdf(norm_pdf_domain, mus[0], sigmas[0]) + pis[1]*norm.pdf(norm_pdf_domain, mus[1], sigmas[1]), color='blue', label="Schätzung Nr. %d" % (run_nr)) ax.plot(norm_pdf_domain, pi *norm.pdf(norm_pdf_domain, real_mu_1, real_sigma_1) + (1-pi)*norm.pdf(norm_pdf_domain, real_mu_2, real_sigma_2), color='red', label="Echte Verteilung") ax.set_xlabel("$x$") ax.set_ylabel("Dichte") ax.legend() def plot_ani(samples, history): fig, ax = plt.subplots(figsize=(10, 10)) ani = animation.FuncAnimation(fig, em_iteration_draw, fargs=(ax, samples, history), interval=1000, frames=len(history)) video = ani.to_html5_video() # Zusätzlich das letzte Bild als PNG ausgeben: der Web-Export zeigt das Video, # der PDF-Export (der kein HTML kann) verwendet das Standbild. png = io.BytesIO() fig.savefig(png, format='png') ipydisplay.display({'text/html': video, 'image/png': base64.b64encode(png.getvalue()).decode('ascii')}, raw=True) plt.close() max_iter = 210 tol = 0.01 pis, mus, sigmas = init_theta(mixture_samples) taus = {+np.zeros((len(xs),+} len(pis))) # record all values in each iteration step for plotting: history = [(pis, mus, sigmas, taus, 0)] for i in range(max_iter): pis, mus, sigmas = history[-1][0:3] history += [EM(mixture_samples, pis, mus, sigmas)] if np.abs(history[-1][-1] - history[-2][-1]) < tol: break plot_ani(mixture_samples, history)
```

German now reads:

```md
import matplotlib.animation as animation
from IPython import display as ipydisplay
import io, base64
from sklearn.cluster import KMeans

def init_theta(samples):
    pis = np.ones(2) / 2
    mus = np.random.random(2) * 2*np.std(samples)\
          + np.mean(samples)
    # a better way would be:
    #mus = KMeans(2).fit(samples.reshape(-1,1)).cluster_centers_
    sigmas =  np.ones(2)
    return pis, mus, sigmas

def em_iteration_draw(run_nr, ax, samples, history):
    pis, mus, sigmas, taus = history[run_nr][0:4]
    ys = np.zeros_like(samples, dtype=bool)
    if(len(taus) == len(samples)):
        for i in range(len(samples)):
            if(taus[i,1] > 0.5):
                ys[i] = 1
    ax.clear()
    ax.set_ylim(0, 0.2)
    ax.hist(samples, bins=51,
            density=True, alpha=0.5,
            label="Daten")
    if(len(taus) == len(samples)):
        ax.scatter(samples[ys], np.zeros_like(samples[ys]),
                   alpha=0.4, c=taus[ys][:,0],
                   label="Als 0 klassifiziert")
    xmin, xmax = ax.get_xlim()
    norm_pdf_domain = np.linspace(xmin, xmax, 100)
    ax.plot(norm_pdf_domain,
            pis[0]*norm.pdf(norm_pdf_domain,
                            mus[0], sigmas[0]) +
            pis[1]*norm.pdf(norm_pdf_domain,
                            mus[1], sigmas[1]),
            color='blue',
            label="Schätzung Nr. %d" % (run_nr))
    ax.plot(norm_pdf_domain,
            pi    *norm.pdf(norm_pdf_domain,
                            real_mu_1, real_sigma_1) +
            (1-pi)*norm.pdf(norm_pdf_domain,
                            real_mu_2, real_sigma_2),
            color='red',
            label="Echte Verteilung")
    ax.set_xlabel("$x$")
    ax.set_ylabel("Dichte")
    ax.legend()

def plot_ani(samples, history):
    fig, ax = plt.subplots(figsize=(10, 10))
    ani = animation.FuncAnimation(fig, em_iteration_draw,
                                  fargs=(ax, samples, history),
                                  interval=1000,
                                  frames=len(history))
    video = ani.to_html5_video()
    # Zusätzlich das letzte Bild als PNG ausgeben: der Web-Export zeigt das Video,
    # der PDF-Export (der kein HTML kann) verwendet das Standbild.
    png = io.BytesIO()
    fig.savefig(png, format='png')
    ipydisplay.display({'text/html': video,
                        'image/png': base64.b64encode(png.getvalue()).decode('ascii')},
                       raw=True)
    plt.close()


max_iter = 210
tol = 0.01
pis, mus, sigmas = init_theta(mixture_samples)
taus = np.zeros((len(xs), len(pis)))
# record all values in each iteration step for plotting:
history = [(pis, mus, sigmas, taus, 0)]

for i in range(max_iter):
    pis, mus, sigmas = history[-1][0:3]
    history += [EM(mixture_samples,
                   pis,
                   mus,
                   sigmas)]
    if np.abs(history[-1][-1] - history[-2][-1]) < tol:
        break

plot_ani(mixture_samples, history)
```

Current English block c22:

```md
import matplotlib.animation as animation
from IPython import display as ipydisplay
import io, base64
from sklearn.cluster import KMeans

def init_theta(samples):
    pis = np.ones(2) / 2
    mus = np.random.random(2) * 2*np.std(samples)\
          + np.mean(samples)
    # a better way would be:
    #mus = KMeans(2).fit(samples.reshape(-1,1)).cluster_centers_
    sigmas =  np.ones(2)
    return pis, mus, sigmas

def em_iteration_draw(run_nr, ax, samples, history):
    pis, mus, sigmas, taus = history[run_nr][0:4]
    ys = np.zeros_like(samples, dtype=bool)
    if(len(taus) == len(samples)):
        for i in range(len(samples)):
            if(taus[i,1] > 0.5):
                ys[i] = 1
    ax.clear()
    ax.set_ylim(0, 0.2)
    ax.hist(samples, bins=51,
            density=True, alpha=0.5,
            label="Daten")
    if(len(taus) == len(samples)):
        ax.scatter(samples[ys], np.zeros_like(samples[ys]),
                   alpha=0.4, c=taus[ys][:,0],
                   label="Als 0 klassifiziert")
    xmin, xmax = ax.get_xlim()
    norm_pdf_domain = np.linspace(xmin, xmax, 100)
    ax.plot(norm_pdf_domain,
            pis[0]*norm.pdf(norm_pdf_domain,
                            mus[0], sigmas[0]) +
            pis[1]*norm.pdf(norm_pdf_domain,
                            mus[1], sigmas[1]),
            color='blue',
            label="Schätzung Nr. %d" % (run_nr))
    ax.plot(norm_pdf_domain,
            pi    *norm.pdf(norm_pdf_domain,
                            real_mu_1, real_sigma_1) +
            (1-pi)*norm.pdf(norm_pdf_domain,
                            real_mu_2, real_sigma_2),
            color='red',
            label="Echte Verteilung")
    ax.set_xlabel("$x$")
    ax.set_ylabel("Dichte")
    ax.legend()

def plot_ani(samples, history):
    fig, ax = plt.subplots(figsize=(10, 10))
    ani = animation.FuncAnimation(fig, em_iteration_draw,
                                  fargs=(ax, samples, history),
                                  interval=1000,
                                  frames=len(history))
    video = ani.to_html5_video()
    # Zusätzlich das letzte Bild als PNG ausgeben: der Web-Export zeigt das Video,
    # der PDF-Export (der kein HTML kann) verwendet das Standbild.
    png = io.BytesIO()
    fig.savefig(png, format='png')
    ipydisplay.display({'text/html': video,
                        'image/png': base64.b64encode(png.getvalue()).decode('ascii')},
                       raw=True)
    plt.close()


max_iter = 210
tol = 0.01
pis, mus, sigmas = init_theta(mixture_samples)
taus = np.zeros((len(mixture_samples), len(pis)))
# record all values in each iteration step for plotting:
history = [(pis, mus, sigmas, taus, 0)]

for i in range(max_iter):
    pis, mus, sigmas = history[-1][0:3]
    history += [EM(mixture_samples,
                   pis,
                   mus,
                   sigmas)]
    if np.abs(history[-1][-1] - history[-2][-1]) < tol:
        break

plot_ani(mixture_samples, history)
```

### replace – German block `c25.0`, `c25.1` – English block(s) **c25.0**, **c25.1**

What changed in the German:

```diff
- [-##-] Anwendungsbeispiele
+ {+#+} Anwendungsbeispiele
- [-###-] Aufenthaltsorte
+ {+##+} Aufenthaltsorte
```

German now reads:

```md
# Anwendungsbeispiele
## Aufenthaltsorte
```

Current English block c25.0:

```md
## Anwendungsbeispiele
```

Current English block c25.1:

```md
### Aufenthaltsorte
```

### replace – German block `c32.0` – English block(s) **c32.0**

What changed in the German:

```diff
- [-###-] Iris-Klassifikation
+ {+##+} Iris-Klassifikation
```

German now reads:

```md
## Iris-Klassifikation
```

Current English block c32.0:

```md
### Iris-Klassifikation
```

### replace – German block `c40.0` – English block(s) **c40.0**

What changed in the German:

```diff
- [-###-] Handgeschriebene Ziffern
+ {+##+} Handgeschriebene Ziffern
```

German now reads:

```md
## Handgeschriebene Ziffern
```

Current English block c40.0:

```md
### Handgeschriebene Ziffern
```

### replace – German block `c53.0` – English block(s) **c53.0**

What changed in the German:

```diff
- [-###-] Fashion-MNIST
+ {+##+} Fashion-MNIST
```

German now reads:

```md
## Fashion-MNIST
```

Current English block c53.0:

```md
### Fashion-MNIST
```


