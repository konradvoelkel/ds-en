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

In this text we assume that we have all taken three semesters of foundational mathematics and know what a vector is, what a matrix is, and what the derivative of a function of several real variables is. We have also all learned a programming language already and are familiar with basic data structures.

You may well have had a first brush with probability and statistics at school. We will introduce the foundations systematically, so that no prior knowledge beyond "mathematics for computer scientists" should be necessary, but we will do so at the brisk pace that mathematicians and computer scientists are used to. If you would like an overview first of what you could have learned at school, the [Online Mathematik Brückenkurs Plus](https://www.ombplus.de/ombplus/link/OmbpluModuleStocha/Ueberb) is an excellent address for it (free, in German, didactically sound, and in the same notation as these notes).

## Aims

Our aim is an introduction to "data science".
It should give orientation and an overview, and make first applications possible in descriptive, exploratory and inferential data analysis, with a particular eye on machine learning.
Along the way we take care of the necessary theoretical background in probability and some practical exercises in Python.
Building on that, one could then go deeper into artificial intelligence. HHU has the [master's programme "Artificial Intelligence and Data Science"](https://www.heicad.hhu.de/lehre/masters-programme-ai-and-data-science) for that.

If you want to be able to work as a data scientist across the full breadth of the field, then in addition to this course you should also know the content of courses on statistics, databases and machine learning, and have some practice on concrete projects. Depending on where you end up, you will also need knowledge of algorithms for distributed systems (Data Science 2) or of deep learning. To be able to work flexibly on other people's projects you should be able to read R code (and Julia may well become more important in future); for deepening the programming itself there is the course *Einführung in Python* with notes of its own, [Einführung in Python](https://eipy-skript-7dd28c.pages.cs.uni-duesseldorf.de/) (in German, under construction).
None of that is yet necessary for "junior data analyst" jobs, which are essentially about applying simple statistics when producing reports and dashboards – for those you learn the tools of the trade in this course and need only pick up and practise the particular software packages your application calls for.

We will keep coming across additional sources for going deeper into individual topics or looking at them from another angle.
In the first session we gave ourselves an overview of what data science is and what we are going to do.


**Competencies**
After completing the course, students should be able to apply basic concepts of probability competently, should have acquired competencies in the foundations of probability for machine learning, should be able to work out a machine learning problem in detail and to apply basic machine learning algorithms. After successfully completing this module they should be in a position to
1. analyse a dataset exploratorily,
1. transform data for further processing,
1. select subsets of the data for further processing,
1. merge suitable datasets,
1. describe and visualise findings in data,
1. set up statistical models from data,
1. assess the quality of models,
1. and use them for classifying and predicting further data.

On top of that, you are familiar with how these tasks can be solved with Python.

**Wider aims.** Behind that list stands a simpler picture of what you should be able to do at the end: pick up a dataset and immediately be able to formulate questions about it *and* answer them. Generating research questions is precisely part of exploratory data analysis. Added to that is being able to read specialist articles and reports that argue statistically – and to recognise when something in them does not add up.

Professionally this opens several doors. The obvious one is an application as a "junior data scientist" or "junior data analyst"; the second is the master's programme [Artificial Intelligence and Data Science](https://www.heicad.hhu.de/lehre/masters-programme-ai-and-data-science), which this course prepares you for. The third is often overlooked: data science techniques are useful in places where nobody carries that job title too – in product development (*data-driven design*), in optimising running systems from log files, in performance comparisons as a basis for decisions (*data-driven decision making*), in quality control, and everywhere a machine learning component is to be built into a larger system.

**What this course is not**
This course does not deal with data science on distributed systems; that is the subject of Data Science 2. It is not an introduction to deep learning, for which there is the course "Introduction to Deep Learning". It does not introduce R/RStudio or other tools. It does not reduce data science to calling `model.fit()`: we reimplement estimators and algorithms ourselves in order to understand what happens in them. And it is not a programming course, although no prior knowledge of Python is assumed; what we need is in the chapter [Introduction to Python](intro-python.ipynb).

Selecting and processing data, and assessing models, also raise ethical questions. Of these, these notes treat the legal framework of data protection in a chapter of its own, as a glossary of the most important terms; the wider ethical discussion is not part of the book.


## How the course is built

The course rests on three pillars. The first is the *background from statistics*: probability spaces, random variables and distributions, expected value and variance, estimators and tests. Without this language there is no saying what a statistical model claims and when it may be trusted.

The second pillar is *programming practice with Python*. We work with toy data small enough to take in completely, and learn Numpy, Scipy, Matplotlib, Pandas and Scikit-Learn on it. The exercise sheets are where reading turns into being able.

The third pillar is *algorithms and data structures*: we reimplement the most important estimators and learning algorithms ourselves, so that we understand what happens when you call `model.fit()`.

The chapters follow this order; the table of contents below lists them individually. As a second view, the following diagram shows how the parts build on one another.

```{mermaid}
flowchart TB
  subgraph E["Introduction"]
    direction LR
    E1["What is Data Science?"] --> E2["Probability"] --> E3["Python"]
  end
  subgraph D["Discrete probability and Numpy"]
    direction LR
    D1["Random variables, distributions,<br/>expected value"] --> D2["Numpy"] --> D3["Discrete distributions,<br/>first exploration"]
  end
  subgraph S["Continuous probability and Scipy"]
    direction LR
    S1["Continuous distributions,<br/>normal distribution, Scipy"]
  end
  subgraph X["Exploratory data analysis"]
    direction LR
    X1["Descriptive statistics,<br/>examples, Iris"] --> X2["Pandas, data cleaning"]
  end
  subgraph M["Multivariate probability"]
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

All the mathematical foundations you need for working on the exercises are contained in these notes (or in the entry requirements of the course).

**Why notes at all**
one might also ask. Mainly the notes serve us as a reference and a guide for the exercises. There are indeed excellent MOOCs (massive open online courses) freely available on the web, especially if your English is good. Unlike a MOOC, though, these notes accompany a taught course with exercises. Working on the exercises with commitment, and exchanging ideas freely with fellow students, is decisive for success in learning. Teachers can only teach; the learning students still have to do themselves.

**AI tools**
On the exercise sheets you may use AI tools such as chatbots and code assistants, but you have to declare it: say with your submission which tool you used for what. In the exam and the midterm, AI tools are not allowed. The reason is the same one that the exercises exist for in the first place: try it yourself first, otherwise the only one learning is the chatbot.


## Licence

These lecture notes are under the [Creative Commons Attribution–ShareAlike 4.0 licence (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png" height="20"/></a> All code additionally under the GPL3.

Excepted from this is third-party content, marked as such, which is under its own licence in each case: the xkcd comics included (CC BY-NC 2.5), Drew Conway's Venn diagram (CC BY-NC 3.0) and Anthony Pino's Melbourne housing dataset (CC BY-NC-SA 4.0). For each of these the source is given on the spot.

## Table of contents

```{tableofcontents}
```

## Sources

Nothing in this book is new, apart from the order and certainly the odd typo.
The main sources for these notes are {cite}`georgii2015stochastik` for probability theory
and {cite}`joelgrusdsfs` for the Python part.
Both books contain material for more than one course, and their target audiences do not coincide with ours.
A complementary book worth reading, with some further mathematical foundations (linear algebra in particular), is {cite}`Deisenroth2020`.
If you do not enjoy rummaging in package documentation, you may be happier for Numpy, Pandas and Matplotlib with Jake VanderPlas's book, which can even be read online for free {cite}`pythondsh`.
