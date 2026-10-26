---
title: "Data Science: from stochastics to machine learning with Python"
short_title: "Lecture notes"
description: "Lecture notes on data science: probability spaces, distributions, estimators and tests, with Numpy, Pandas and Scikit-learn, and the algorithms implemented."
thumbnail: images/social-card.png
---

These notes are an introduction to data science that begins with stochastics and ends with machine learning, without leaving a gap in between. What separates them from a tools course is the third pillar below: the methods here are not called, they are reimplemented. If you want to know what `model.fit()` actually does, you write it once yourself – k-means, principal component analysis, regression, the EM algorithm. Everything you need for that is in this book.

## How the course is built

The course rests on three pillars. The first is the *background from statistics*: probability spaces, random variables and distributions, expected value and variance, estimators and tests. Without this language there is no saying what a statistical model claims and when it may be trusted.

The second pillar is *programming practice with Python*. We work with toy data small enough to take in completely, and learn Numpy, Scipy, Matplotlib, Pandas and Scikit-Learn on it. The exercise sheets are where what you have read becomes something you can do.

The third pillar is *algorithms and data structures*: we reimplement the most important estimators and learning algorithms ourselves, so that we understand what happens when you call `model.fit()`.

The chapters follow this order; the table of contents below lists them one by one. The diagram that follows gives a second view: how the parts build on one another.

```{figure} images/course-structure.svg
:alt: Seven parts in sequence, each leading to the next: Introduction (what is data science, stochastics, Python); Discrete stochastics and Numpy; Continuous stochastics and Scipy; Exploratory data analysis; Multivariate stochastics; Data protection; Machine learning.
:width: 100%

How the parts of the course build on one another.
```

## What you will be able to do

Our aim is an introduction to "data science".
It should give you orientation and an overview, and get you to first applications in descriptive, exploratory and inferential data analysis, with a particular eye on machine learning.
Along the way we cover the theoretical background in stochastics that this needs, and do some practical exercises in Python.
From there you could go deeper into artificial intelligence, for which a master's programme in AI or data science is the usual next step.

Behind any list of formal competencies lies a simpler picture of what you should be able to do at the end: pick up a dataset and straight away be able to ask questions of it *and* answer them. Coming up with research questions is very much part of exploratory data analysis. Beyond that, you should be able to read specialist articles and reports that argue with statistics – and notice when something in them does not add up.

Professionally, this opens several doors. The obvious one is applying for a job as a "junior data scientist" or "junior data analyst"; the second is a master's programme in artificial intelligence or data science, for which this book covers much of the expected background. The third is easy to overlook: data science techniques are useful in plenty of places where nobody carries that job title – in product development (*data-driven design*), in optimising running systems from their log files, in performance comparisons that feed decisions (*data-driven decision making*), in quality control, and wherever a machine learning component has to be built into a larger system.

## What this course is not

This course does not deal with data science on distributed systems, and it is not an introduction to deep learning; each of those is a course in its own right. It does not introduce R/RStudio or other tools. It does not reduce data science to calling `model.fit()`: we reimplement estimators and algorithms ourselves so that we understand what goes on inside them. And it is not a programming course, even though it assumes no prior knowledge of Python; what we need is in the chapter [Introduction to Python](intro-python.ipynb).

Selecting and processing data, and assessing models, raise ethical questions too. Of these, the notes treat the legal framework of data protection in a chapter of its own, written as a glossary of the most important terms; the wider ethical discussion is not part of the book.

## Prerequisites

In this text we assume the foundational mathematics of an undergraduate degree in computer science or a related subject: we know what a vector is, what a matrix is, and what the derivative of a function of several real variables is. We have also all learned a programming language before and know the basic data structures.

You may well have had a first brush with stochastics, statistics and probability theory at school. We introduce the foundations systematically, so that nothing beyond "mathematics for computer scientists" should be needed – but we do it at the brisk pace that mathematicians and computer scientists are used to. If you would first like an overview of what school could have taught you, any solid pre-university course in probability will do; readers of German have one in the [Online Mathematik Brückenkurs Plus](https://www.ombplus.de/ombplus/link/OmbpluModuleStocha/Ueberb), which is free, didactically sound and in the same notation as these notes.

Every piece of mathematics you need for the exercises is in these notes, or among the prerequisites above.

## Reading these notes

You are reading the web edition. The same book is also available as a [PDF to
download](https://datascience.konradvoelkel.com/ds-en.pdf).

These are one of three sets of lecture notes by [Konrad
Völkel](https://www.konradvoelkel.com/), all free to read. The other two are in German:
[Einführung in Python](https://eipy-skript-7dd28c.pages.cs.uni-duesseldorf.de/), which
introduces Python as a second programming language, and [Einführung in Deep
Learning](https://eidl-skript-131e30.pages.cs.uni-duesseldorf.de/), which follows on from
these notes. All three are listed, with their PDF editions and the lecture recordings, on
his [teaching page](https://www.konradvoelkel.com/teaching/).

Along the way we will keep meeting further sources that go deeper into individual topics or look at them from another angle.
The opening chapter gives an overview of what data science is and what we are going to do.

## Table of contents

```{tableofcontents}
```

## How to cite

These notes are archived at Zenodo. Please cite the DOI rather than the address: it
outlives any move, and the one below always resolves to the newest version.

> Völkel, Konrad (2026). *Data Science: from stochastics to machine learning with
> Python.* Zenodo. ``doi:10.5281/zenodo.23444644``

```bibtex
@book{voelkel2026datascience,
  author    = {Völkel, Konrad},
  title     = {Data Science: from stochastics to machine learning with Python},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.23444644},
  url       = {https://datascience.konradvoelkel.com/},
}
```

To cite one particular version rather than the book as a whole, Zenodo mints a separate
DOI for each; they are listed on the record.

## Licence

Written by [Dr. Konrad Völkel](https://www.konradvoelkel.com/), Heinrich Heine University Düsseldorf.

These lecture notes are published under the [Creative Commons Attribution–ShareAlike 4.0 licence (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20" alt="Creative Commons Attribution-ShareAlike 4.0 licence badge"/></a> All code is additionally under the GPL3.

The exception is third-party content, marked as such, each item under its own licence: the xkcd comics (CC BY-NC 2.5), Drew Conway's Venn diagram (CC BY-NC 3.0) and Anthony Pino's Melbourne housing dataset (CC BY-NC-SA 4.0). The source of each is given where it appears.

## Sources

Nothing in this book is new, apart from the order and, no doubt, the odd typo.
The main sources for these notes are {cite}`georgii2015stochastik` for probability theory
and {cite}`joelgrusdsfs` for the Python part.
Both books hold material for more than one course, and neither is aimed at quite our audience.
A complementary book worth reading, with some further mathematical foundations (linear algebra in particular), is {cite}`Deisenroth2020`.
If rummaging through package documentation is not your idea of fun, you may be happier with Jake VanderPlas's book for Numpy, Pandas and Matplotlib, which can even be read online for free {cite}`pythondsh`.

:::{note}

**About this edition.** This is an English edition of a book that was written in German:
the *Data Science* lecture notes by Konrad Völkel for the Bachelor's programme in Computer
Science at Heinrich Heine University Düsseldorf. The German original is published at
[voelkel.pages.cs.uni-duesseldorf.de/ds-skript](https://voelkel.pages.cs.uni-duesseldorf.de/ds-skript/).

The translation was produced with a large language model and reviewed afterwards – an
experiment in keeping a translated edition alive alongside a book that keeps changing.

:::
