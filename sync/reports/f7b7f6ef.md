# Upstream changes 2a52229b → f7b7f6ef

## intro-python.ipynb → intro-python.ipynb

### replace – German block `c1.5` – English block(s) **c1.5**

What changed in the German:

```diff
- Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: Der gezeigte Code kommt mit **Python [-3.11**-] aus und benutzt keine neueren Sprachfeatures; gebaut und getestet wird das Skript mit Python 3.13 oder 3.14, weil die Paketversionen in `pyproject.toml` das verlangen. `uv sync` installiert das passende Python selbst, wenn es fehlt.
+ Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: Der gezeigte Code kommt mit **Python {+3.12**+} aus und benutzt keine neueren Sprachfeatures; gebaut und getestet wird das Skript mit Python 3.13 oder 3.14, weil die Paketversionen in `pyproject.toml` das verlangen. {+Die Untergrenze lag bis Oktober 2026 bei 3.11 und ist mitgewandert, weil Numpy ab 2.5 und Scipy ab 1.18 kein Python 3.11 mehr unterstützen.+} `uv sync` installiert das passende Python selbst, wenn es fehlt.
```

German now reads:

```md
Diese Pakete stimmen ihre Versionen untereinander ab: Nach [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) beziehungsweise [SPEC 0](https://scientific-python.org/specs/spec-0000/) unterstützen sie jede Python-Version für etwa drei Jahre. Für dieses Buch heißt das: Der gezeigte Code kommt mit **Python 3.12** aus und benutzt keine neueren Sprachfeatures; gebaut und getestet wird das Skript mit Python 3.13 oder 3.14, weil die Paketversionen in `pyproject.toml` das verlangen. Die Untergrenze lag bis Oktober 2026 bei 3.11 und ist mitgewandert, weil Numpy ab 2.5 und Scipy ab 1.18 kein Python 3.11 mehr unterstützen. `uv sync` installiert das passende Python selbst, wenn es fehlt.
```

Current English block c1.5:

```md
These packages coordinate their versions with one another: under [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) and [SPEC 0](https://scientific-python.org/specs/spec-0000/) respectively, each supports a given Python version for about three years. For this book that means the code shown gets by with **Python 3.11** and uses no newer language features, while the notes themselves are built and tested with Python 3.13 or 3.14, because the package versions in `pyproject.toml` demand it. If the right Python is missing, `uv sync` installs that as well.
```

### replace – German block `c4.1` – English block(s) **c4.1**

What changed in the German:

```diff
- Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript wird mit Python 3.13 oder 3.14 gebaut und getestet; der gezeigte Code kommt mit Python [-3.11-] aus.
+ Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript wird mit Python 3.13 oder 3.14 gebaut und getestet; der gezeigte Code kommt mit Python {+3.12+} aus.
```

German now reads:

```md
Natürlich gibt es zu Python mittlerweile viel Material. Da die Sprache sehr lebendig ist, lohnt es sich, darauf zu achten, dass man mit python3 arbeitet. Die aktuellste Version, während diese Zeilen geschrieben werden, ist Python 3.14. Dieses Skript wird mit Python 3.13 oder 3.14 gebaut und getestet; der gezeigte Code kommt mit Python 3.12 aus.
```

Current English block c4.1:

```md
There is, of course, no shortage of material on Python by now. Since the language is very much alive, make sure you are working with python3. The latest version at the time of writing is Python 3.14. These notes are built and tested with Python 3.13 or 3.14; the code shown gets by with Python 3.11.
```


## landing-page.md → landing-page.md

### replace – German block `7` – English block(s) **7**

What changed in the German:

```diff
- [-```{mermaid} flowchart TB subgraph E["Einführung"] direction LR E1["Was-] ist Data [-Science?"] --> E2["Stochastik"] --> E3["Python"] end subgraph D["Diskrete-] Stochastik und [-Numpy"] direction LR D1["Zufallsvariablen, Verteilungen,<br/>Erwartungswert"] --> D2["Numpy"] --> D3["Diskrete Verteilungen,<br/>erste Exploration"] end subgraph S["Stetige-] Stochastik und [-Scipy"] direction LR S1["Stetige Verteilungen,<br/>Normalverteilung, Scipy"] end subgraph X["Explorative Datenanalyse"] direction LR X1["Deskriptive Statistik,<br/>Beispiele, Iris"] --> X2["Pandas,-] Daten [-putzen"] end subgraph M["Multivariate Stochastik"] direction LR M1["Kovarianz, multivariate<br/>Normalverteilung,-] relative [-Entropie"] end subgraph P["Datenschutz"] direction LR P1["Datenschutz-Glossar"] end subgraph L["Maschinelles Lernen"] direction LR L1["Clustering,<br/>Dimensionsreduktion"] --> L2["Statistische Modelle,<br/>Regression, Kernel"] --> L3["Tests, Modellwahl,<br/>Expectation Maximization"] end E --> D --> S --> X --> M --> P --> L-] ```
+ {+```{figure} images/course-structure.svg :alt: Sieben Teile nacheinander, jeder führt zum nächsten: Einführung (Was+} ist Data {+Science?, Stochastik, Python); Diskrete+} Stochastik und {+Numpy (Zufallsvariablen, Verteilungen, Erwartungswert; Numpy; Diskrete Verteilungen, erste Exploration); Stetige+} Stochastik und {+Scipy (Stetige Verteilungen, Normalverteilung, Scipy); Explorative Datenanalyse (Deskriptive Statistik, Beispiele, Iris; Pandas,+} Daten {+putzen); Multivariate Stochastik (Kovarianz, multivariate Normalverteilung,+} relative {+Entropie); Datenschutz (Datenschutz-Glossar); Maschinelles Lernen (Clustering, Dimensionsreduktion; Statistische Modelle, Regression, Kernel; Tests, Modellwahl, Expectation Maximization). :width: 100% Wie die Teile der Vorlesung aufeinander aufbauen.+} ```
```

German now reads:

```md
```{figure} images/course-structure.svg
:alt: Sieben Teile nacheinander, jeder führt zum nächsten: Einführung (Was ist Data Science?, Stochastik, Python); Diskrete Stochastik und Numpy (Zufallsvariablen, Verteilungen, Erwartungswert; Numpy; Diskrete Verteilungen, erste Exploration); Stetige Stochastik und Scipy (Stetige Verteilungen, Normalverteilung, Scipy); Explorative Datenanalyse (Deskriptive Statistik, Beispiele, Iris; Pandas, Daten putzen); Multivariate Stochastik (Kovarianz, multivariate Normalverteilung, relative Entropie); Datenschutz (Datenschutz-Glossar); Maschinelles Lernen (Clustering, Dimensionsreduktion; Statistische Modelle, Regression, Kernel; Tests, Modellwahl, Expectation Maximization).
:width: 100%

Wie die Teile der Vorlesung aufeinander aufbauen.
```
```

Current English block 7:

```md
```{figure} images/course-structure.svg
:alt: Seven parts in sequence, each leading to the next: Introduction (what is data science, stochastics, Python); Discrete stochastics and Numpy; Continuous stochastics and Scipy; Exploratory data analysis; Multivariate stochastics; Data protection; Machine learning.
:width: 100%

How the parts of the course build on one another.
```
```


## numpy.ipynb → numpy.ipynb

### replace – German block `c1.6` – English block(s) **c1.6**

What changed in the German:

```diff
- Wir verwenden Numpy in einer Version größergleich [-2,-] wozu [-wenigstens-] Python [-3.11-] (oder höher) [-empfohlen wird.-] Der Code in diesem Skript sollte allerdings größtenteils auch mit Numpy 1.26 laufen. Für weitere Informationen zur Versionskompatibilität gibt es die [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html).
+ Wir verwenden Numpy in einer Version größergleich {+2.5,+} wozu Python {+3.12+} (oder höher) {+nötig ist.+} Der Code in diesem Skript sollte allerdings größtenteils auch mit Numpy 1.26 laufen. Für weitere Informationen zur Versionskompatibilität gibt es die [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html).
```

German now reads:

```md
Wir verwenden Numpy in einer Version größergleich 2.5, wozu Python 3.12 (oder höher) nötig ist. Der Code in diesem Skript sollte allerdings größtenteils auch mit Numpy 1.26 laufen. Für weitere Informationen zur Versionskompatibilität gibt es die [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html).
```

Current English block c1.6:

```md
We use Numpy version 2 or higher, for which Python 3.11 or above is recommended. Most of the code in these notes should run under Numpy 1.26 as well, though. [NEP 29](https://numpy.org/neps/nep-0029-deprecation_policy.html) has more on version compatibility.
```

### replace – German block `c19` – English block(s) **c19**

What changed in the German:

```diff
- zahlen = list(range(1,10)) npmatrix = np.array(zahlen) print("not in shape:", npmatrix) [-npmatrix.shape-] = [-(3,3)-] print("in much better shape:\n"+ str(npmatrix)) print("Zeilenvektor Zeile 0:", npmatrix[0]) print("Spaltenvektor Spalte 0:", npmatrix[:,0]) print("Spalten 1-2:\n"+ str(npmatrix[:,1:])) print("Alle Zeilen, Schrittweite 2\n"+ str(npmatrix[0::2]))
+ zahlen = list(range(1,10)) npmatrix = np.array(zahlen) print("not in shape:", npmatrix) {+npmatrix+} = {+npmatrix.reshape(3, 3)+} print("in much better shape:\n"+ str(npmatrix)) print("Zeilenvektor Zeile 0:", npmatrix[0]) print("Spaltenvektor Spalte 0:", npmatrix[:,0]) print("Spalten 1-2:\n"+ str(npmatrix[:,1:])) print("Alle Zeilen, Schrittweite 2\n"+ str(npmatrix[0::2]))
```

German now reads:

```md
zahlen = list(range(1,10))
npmatrix = np.array(zahlen)
print("not in shape:", npmatrix)
npmatrix = npmatrix.reshape(3, 3)
print("in much better shape:\n"+ str(npmatrix))
print("Zeilenvektor Zeile 0:", npmatrix[0])
print("Spaltenvektor Spalte 0:", npmatrix[:,0])
print("Spalten 1-2:\n"+ str(npmatrix[:,1:]))
print("Alle Zeilen, Schrittweite 2\n"+ str(npmatrix[0::2]))
```

Current English block c19:

```md
numbers = list(range(1,10))
npmatrix = np.array(numbers)
print("not in shape:", npmatrix)
npmatrix.shape = (3,3)
print("in much better shape:\n"+ str(npmatrix))
print("row vector, row 0:", npmatrix[0])
print("column vector, column 0:", npmatrix[:,0])
print("columns 1-2:\n"+ str(npmatrix[:,1:]))
print("all rows, step 2\n"+ str(npmatrix[0::2]))
```


