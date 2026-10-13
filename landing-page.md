# Lecture notes

:::{note}
**About this edition.** This is an English edition of a book that was written in German:
the *Data Science* lecture notes by Konrad Völkel for the Bachelor's programme in Computer
Science at Heinrich Heine University Düsseldorf. The German original is the authoritative
version and is published at
[voelkel.pages.cs.uni-duesseldorf.de/ds-skript](https://voelkel.pages.cs.uni-duesseldorf.de/ds-skript/).

The translation was produced with a large language model and reviewed afterwards – an
experiment in keeping a translated edition alive alongside a book that keeps changing.
Where this edition and the German original disagree, the original is right. If something
reads oddly, or a formula or a figure looks wrong, it is worth checking against it.
:::

## Prerequisites

In this text we assume that we have all been through three semesters of foundational mathematics: we know what a vector is, what a matrix is, and what the derivative of a function of several real variables is. We have also all learned a programming language before and know the basic data structures.

You may well have had a first brush with stochastics, statistics and probability theory at school. We introduce the foundations systematically, so that nothing beyond "mathematics for computer scientists" should be needed – but we do it at the brisk pace that mathematicians and computer scientists are used to. If you would first like an overview of what school could have taught you, the [Online Mathematik Brückenkurs Plus](https://www.ombplus.de/ombplus/link/OmbpluModuleStocha/Ueberb) is an excellent place to start (free, in German, didactically sound, and in the same notation as these notes).

## Aims

Our aim is an introduction to "data science".
It should give you orientation and an overview, and get you to first applications in descriptive, exploratory and inferential data analysis, with a particular eye on machine learning.
Along the way we cover the theoretical background in stochastics that this needs, and do some practical exercises in Python.
From there you could go deeper into artificial intelligence; HHU has the [master's programme "Artificial Intelligence and Data Science"](https://www.heicad.hhu.de/lehre/masters-programme-ai-and-data-science) for that.

If you want to work as a data scientist across the full breadth of the field, then beyond this course you should also know the content of courses on statistics, databases and machine learning, and have some practice on concrete projects. Depending on where you end up, you will also need algorithms for distributed systems (Data Science 2) or deep learning. To move easily between other people's projects you should be able to read R code (and Julia may yet become more important); to go deeper into the programming itself there is the course *Einführung in Python*, which has notes of its own, [Einführung in Python](https://eipy-skript-7dd28c.pages.cs.uni-duesseldorf.de/) (in German, under construction).
None of that is needed yet for "junior data analyst" jobs, which essentially come down to applying simple statistics in reports and dashboards – for those, this course teaches you the tools of the trade, and all you need to add is practice with whichever software packages your application calls for.

Along the way we will keep meeting further sources that go deeper into individual topics or look at them from another angle.
The first session gave us an overview of what data science is and what we are going to do.


**Competencies**
After completing the course, students should be able to apply the basic concepts of probability competently, should have a working grasp of the probability foundations that machine learning rests on, and should be able to work a machine learning problem out in detail and apply basic machine learning algorithms. After successfully completing this module they should be in a position to
1. analyse a dataset exploratorily,
1. transform data for further processing,
1. select subsets of the data for further processing,
1. merge suitable datasets,
1. describe and visualise findings in data,
1. set up statistical models from data,
1. assess the quality of models,
1. and use them for classifying and predicting further data.

On top of that, you will know how to carry these tasks out in Python.

**Wider aims.** Behind that list is a simpler picture of what you should be able to do at the end: pick up a dataset and straight away be able to ask questions of it *and* answer them. Coming up with research questions is very much part of exploratory data analysis. Beyond that, you should be able to read specialist articles and reports that argue with statistics – and notice when something in them does not add up.

Professionally, this opens several doors. The obvious one is applying for a job as a "junior data scientist" or "junior data analyst"; the second is the master's programme [Artificial Intelligence and Data Science](https://www.heicad.hhu.de/lehre/masters-programme-ai-and-data-science), which this course prepares you for. The third is easy to overlook: data science techniques are useful in plenty of places where nobody carries that job title – in product development (*data-driven design*), in optimising running systems from their log files, in performance comparisons that feed decisions (*data-driven decision making*), in quality control, and wherever a machine learning component has to be built into a larger system.

**What this course is not**
This course does not deal with data science on distributed systems; that is the subject of Data Science 2. It is not an introduction to deep learning, for which there is the course "Introduction to Deep Learning". It does not introduce R/RStudio or other tools. It does not reduce data science to calling `model.fit()`: we reimplement estimators and algorithms ourselves so that we understand what goes on inside them. And it is not a programming course, even though it assumes no prior knowledge of Python; what we need is in the chapter [Introduction to Python](intro-python.ipynb).

Selecting and processing data, and assessing models, raise ethical questions too. Of these, the notes treat the legal framework of data protection in a chapter of its own, written as a glossary of the most important terms; the wider ethical discussion is not part of the book.


## How the course is built

The course rests on three pillars. The first is the *background from statistics*: probability spaces, random variables and distributions, expected value and variance, estimators and tests. Without this language there is no saying what a statistical model claims and when it may be trusted.

The second pillar is *programming practice with Python*. We work with toy data small enough to take in completely, and learn Numpy, Scipy, Matplotlib, Pandas and Scikit-Learn on it. The exercise sheets are where what you have read becomes something you can do.

The third pillar is *algorithms and data structures*: we reimplement the most important estimators and learning algorithms ourselves, so that we understand what happens when you call `model.fit()`.

The chapters follow this order; the table of contents below lists them one by one. The diagram that follows gives a second view: how the parts build on one another.

```{mermaid}
flowchart TB
  subgraph E["Introduction"]
    direction LR
    E1["What is Data Science?"] --> E2["Stochastics"] --> E3["Python"]
  end
  subgraph D["Discrete stochastics and Numpy"]
    direction LR
    D1["Random variables, distributions,<br/>expected value"] --> D2["Numpy"] --> D3["Discrete distributions,<br/>first exploration"]
  end
  subgraph S["Continuous stochastics and Scipy"]
    direction LR
    S1["Continuous distributions,<br/>normal distribution, Scipy"]
  end
  subgraph X["Exploratory data analysis"]
    direction LR
    X1["Descriptive statistics,<br/>examples, Iris"] --> X2["Pandas, data cleaning"]
  end
  subgraph M["Multivariate stochastics"]
    direction LR
    M1["Covariance, multivariate<br/>normal distribution, relative entropy"]
  end
  subgraph P["Data protection"]
    direction LR
    P1["Data protection glossary"]
  end
  subgraph L["Machine learning"]
    direction LR
    L1["Clustering,<br/>dimensionality reduction"] --> L2["Statistical models,<br/>regression, kernels"] --> L3["Tests, model selection,<br/>expectation maximization"]
  end
  E --> D --> S --> X --> M --> P --> L
```

## The notes and the course

Every piece of mathematics you need for the exercises is in these notes (or among the course's entry requirements).

**Why notes at all**, you might ask. Mainly, the notes serve us as a reference and as a guide to the exercises. There are excellent MOOCs (massive open online courses) freely available on the web – but unlike a MOOC, these notes accompany a taught course with exercises. Working through the exercises in earnest, and talking them over freely with fellow students, is what decides whether the learning succeeds. Teachers can only teach; the learning, students still have to do themselves.


## Licence

These lecture notes are published under the [Creative Commons Attribution–ShareAlike 4.0 licence (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a> All code is additionally under the GPL3.

The exception is third-party content, marked as such, each item under its own licence: the xkcd comics (CC BY-NC 2.5), Drew Conway's Venn diagram (CC BY-NC 3.0) and Anthony Pino's Melbourne housing dataset (CC BY-NC-SA 4.0). The source of each is given where it appears.

## Table of contents

```{tableofcontents}
```

## Sources

Nothing in this book is new, apart from the order and, no doubt, the odd typo.
The main sources for these notes are {cite}`georgii2015stochastik` for probability theory
and {cite}`joelgrusdsfs` for the Python part.
Both books hold material for more than one course, and neither is aimed at quite our audience.
A complementary book worth reading, with some further mathematical foundations (linear algebra in particular), is {cite}`Deisenroth2020`.
If rummaging through package documentation is not your idea of fun, you may be happier with Jake VanderPlas's book for Numpy, Pandas and Matplotlib, which can even be read online for free {cite}`pythondsh`.
