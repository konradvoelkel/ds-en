# Random variables and distributions

The typical 'interface' to probability distributions is the random variable.
Unlike a bare distribution, a random variable also cares about which concrete values can come up as outcomes.

## Random variables

We recall the definition, now in the notation we want to use from here on:

:::{admonition} Definition
Given a set $\Omega$ with a probability measure $P_\Omega$,
a map $X \colon \Omega \to \mathcal{X}$ into a set $\mathcal{X}$ is called a
**random variable** if for every event $A \subseteq \mathcal{X}$ the preimage $X^{-1}(A) \subseteq \Omega$ is an event as well.
:::

A reminder: if $\Omega$ and $\mathcal{X}$ are finite sets, we call every subset an event. Then every such map is a random variable as well.
We will see later that the term random variable is used exactly when we are interested in expected values or in higher moments.

### Where does the randomness come from?

Before we carry on calculating, a question that is rarely asked and still more rarely answered: where in a dataset does the randomness actually come from? The short answer is that it does not occur there at all. It is a decision of ours.

A measurement that has already been taken is not random – the die has come to rest, the temperature has been read off, the row is sitting in the file. The data collection itself is a deterministic process too: a sensor writes down what it measures. Randomness is not something we *find* in the data; it is the language in which we talk about what we do not know about the data, or do not want to know. We treat the observed frequencies as if they were probabilities and draw conclusions from that model – randomness is thus a modelling tool, not a natural substance.

In three places we do meet it quite concretely all the same:

- **In the selection.** When we draw a subset from the data we have – a sample, a mini-batch, a split into training and test data – the randomness is ours. We draw at random on purpose, so that the selection brings no structure of its own that we might afterwards take for a result.
- **In sampling from a model.** Drawing from a model distribution produces synthetic data. This randomness, too, is ours.
- **On the computer, not at all.** Both of these run on a deterministic device that produces only *pseudo-randomness*: a sequence of numbers that looks random but is completely determined by its starting value, the *seed*. That is not a shortcoming but the reason analyses are reproducible (see [Programming with stochastics](programming-stochastics.ipynb)).

The path the data take along the way can be told in three pictures. First the data collection: a section of the world is chosen, raw data accrue about it, and cleaning turns the raw data into the data one actually works with.

```{figure} images/dsprozess-simplified-1.png
:width: 480px
:align: center
:name: ds-prozess-erhebung

Data collection: from the world via a section and raw data to the data.
```

Then the modelling. A model is built from the data, and from the model data can be generated again – synthetic data. Whether the model is any good is decided by whether its synthetic data resemble the real thing.

```{figure} images/dsprozess-simplified-2.png
:width: 480px
:align: center
:name: ds-prozess-modell

Modelling: from the data to the model and back to synthetic data.
```

And finally the path to the target variable, which is what we are actually after: the data are transformed, and from the transformed data the one number we wanted to know is computed.

```{figure} images/dsprozess-simplified-3.png
:width: 480px
:align: center
:name: ds-prozess-zielgroesse

Analysis: from the data via transformed data to the target variable.
```

:::{admonition} Example
**A throw of a die, spelled out in full.** The *section of the world* is a die on a table. As *raw data*, suppose a camera delivers the 3D coordinates of the eight corners at every instant, so $8 \cdot 3$ numbers per frame. Once the unusable frames have been sorted out, these are the *data*. From them we compute *transformed data*: the centre and the rotation angles of the die, so $3 + 3$ numbers, since no more than that is needed to describe how a cube is lying. Only at the end comes the *target variable* we are actually interested in: the number of pips on top, a number in $\{1,\dots,6\}$.

The whole path from the world to the target variable is exactly what we call a random variable: a map $X \colon \Omega \to \{1,\dots,6\}$, where $\Omega$ is the set of possible world states. Nothing about this map is random – it is a long but unambiguous rule for calculating. The randomness lies solely in the fact that we do not know which $\omega \in \Omega$ we are in, and therefore equip $\Omega$ with a probability measure. The statement "the die is fair" then reads

$$
P(X = 6) := P_\Omega\left( \{ \omega \in \Omega : X(\omega) = 6 \} \right) = P_\Omega\left( X^{-1}(\{6\}) \right) = \dfrac{1}{6}.
$$

The notation $P(X = 6)$ is thus an abbreviation: what is meant is the probability of the set of all world states in which the die ends up showing a six. Precisely this construction – a measure on $\Omega$ becomes, via $X$, a measure on the values of $X$ – is the content of the next section.
:::

### Induced probability measure

:::{admonition} Definition
Given a random variable $X \colon \Omega \to \mathcal{X}$,
the probability measure on $\mathcal{X}$ given by

$$P_X \colon A \mapsto P_\Omega\left( X^{-1}(A) \right)$$

is the **distribution of $X$**.
:::

:::{admonition} Proposition
This really is a probability measure, always.
:::

:::{admonition} Proof
We check the axioms:
1. We have $X^{-1}(\mathcal{X}) = \Omega$, hence $P_X(\mathcal{X}) = P_\Omega\left( X^{-1}(\mathcal{X}) \right) = P_\Omega(\Omega) = 1$.
2. Let $A_1,\dots$ be a sequence of pairwise disjoint events in $\mathcal{X}$. Then

$$X^{-1}\left(\bigcup_{i \geq 1} A_i\right) = \left\{\omega \in \Omega\ \mid\ X(\omega) \in A_i \text{ for some } i \right\} = \bigcup_{i \geq 1} X^{-1}(A_i)$$

and hence

$$P_X\left(\bigcup_{i\geq 1} A_i\right) = P_\Omega\left( X^{-1} \left(\bigcup_{i \geq 1} A_i\right) \right) = P_\Omega\left( \bigcup_{i \geq 1} X^{-1}(A_i) \right) $$

$$ = \sum_{i \geq 1} P_\Omega \left( X^{-1} A_i \right) = \sum_{i \geq 1} P_X(A_i).$$

:::

:::{admonition} Example
$30$ children are playing in a room. Of them, $10$ are wearing a blue jumper,
$10$ a red one, $5$ a yellow one and another $5$ a black one.
We model $\Omega =$ the set of children and $X \colon \Omega \to \{r,y,b,k\}$ as the map
that sends each child to the letter standing for the colour of their jumper ($r$ red, $y$ yellow, $b$ blue, $k$ black).
The distribution of $X$ is now defined; it is a probability measure on the set $\{r,y,b,k\}$.
By way of example we can compute:

$$P_X\left(\{b,r\}\right) = P_\Omega\left(X^{-1} \left(\{b,r\}\right) \right) = \frac{20}{30}$$

where we have implicitly assumed that we treat all the children alike,
that is, that we pick a child uniformly at random and look at the colour of its jumper
whenever we look at an outcome of $X$.
:::

:::{admonition} Example
**Composing maps yields new random variables.** Let $X$ be the throw of a fair die, that is, $\Omega = \{1,\dots,6\}$ with the uniform distribution and $X$ the identity.

*(a)* Let $g \colon \{1,\dots,6\} \to \{\text{even}, \text{odd}\}$ be the map that assigns to a number of pips its parity. Then

$$
P_g(\{\text{even}\}) = P_\Omega\left( g^{-1}(\{\text{even}\}) \right) = P_\Omega(\{2,4,6\}) = \dfrac{3}{6} = \dfrac{1}{2}.
$$

Here $g \circ X$ is itself a random variable again – the composition of a random variable with a map always is – and its distribution is $P_{g(X)} = P_g$. One writes $g(X)$ for short and speaks of "the random variable *parity of the throw*".

*(b)* Let $f$ be the map that says whether the number of pips is at least $5$. For the answer "no" we decompose the preimage into elementary events and use $\sigma$-additivity:

$$
P_f(\{\text{no}\}) = P_\Omega\left( \{1,2,3,4\} \right) = \sum_{i=1}^4 P_\Omega\left( \{i\} \right) = 4 \cdot \dfrac{1}{6} = \dfrac{2}{3}.
$$

That is the usual case when calculating with induced measures: you find the preimage, cut it into disjoint pieces and add up.

*(c)* Composing with $x \mapsto 2x$ gives the random variable $2X$ with values in $\{2,4,6,8,10,12\}$, each with probability $\frac16$. So one can calculate with random variables as one does with numbers – they may be doubled, added, squared – and the distribution changes along with them. How expected value and variance behave under this is settled by the chapter [Expected value and variance](expectation-variance.md) (linearity of the expected value).
:::

If only the distribution $P_X$ interests us, we can ignore $\Omega$,
since the same distribution can be obtained with other sets $\Omega$ as well,
and with distributions that are not uniform.

## Probability mass function

In everyday work one usually calculates with probabilities not through the measure $P$ on events, but through a function $p(x)$ that assigns each possible value $x$ its probability directly. In the discrete case, which is what this chapter is about, this function is called the *probability mass function*; its continuous counterpart, the density, we will meet in a later chapter:

:::{admonition} Definition
A function $p \colon \Omega \to [0,1]$ is called a *probability mass function* (*pmf*) of a distribution $P$ on $\Omega$
if $p(\omega) = P(\{\omega\})$ holds for all $\omega \in \Omega$.
:::

:::{admonition} Example
In the previous example we have $P_X(\{r\}) = \frac{10}{30}$, $P_X(\{y\}) = \frac{5}{30}$, $P_X(\{b\}) = \frac{10}{30}$, $P_X(\{k\}) = \frac{5}{30}$, and therefore

$$p(r):=\frac{10}{30},\ p(y):=\frac{5}{30},\ p(b):=\frac{10}{30},\ p(k):=\frac{5}{30}$$

is the definition of a pmf for $P_X$. One also says that $p$ is the pmf of $X$.
Another name in common use for the pmf is *discrete density*.

The pmf of the uniform distribution on $\Omega$ is $p(\omega) = \frac{1}{|\Omega|}$.

The pmf of the Dirac distribution with mass at a fixed $\xi \in \Omega$ (see [The formalism of stochastics](intro-stochastics.md)) is

$$
p(\omega) = \begin{cases} 1 & \omega = \xi,\\ 0 & \text{otherwise.} \end{cases}
$$

Both presuppose that $\Omega$ is at most countable – for uncountable $\Omega$ every single probability $P(\{\omega\})$ is typically $0$, and the density takes the place of the pmf.
:::

:::{admonition} Example
We are expecting an incoming message $3$ characters long. We model these three characters as random variables X, Y and Z.
We know in advance that each character can only come from a finite character set.
For each random variable we write this range as $\mathcal{X},\mathcal{Y}$ and $\mathcal{Z}$ respectively.
We write the pmfs as $p(x),\ p(y),\ p(z)$ with $x \in \mathcal{X}, y \in \mathcal{Y}$ and $z \in \mathcal{Z}$.

We can also regard the whole message as a single random variable: XYZ.
It can then happen that certain sequences of letters are more probable than their constituents would suggest.
If $X=s$ and $Y=o$, then $Z=s$ is surely more probable than it is for arbitrary values of $X$ and $Y$.
All in all, $XYZ=sos$ is more probable than the product of the probabilities of $X=s$, $Y=o$ and $Z=s$.
If, as usual, we write the pmf of $XYZ$ as $p(x,y,z)$, that says:

$$p(x,y,z) \neq p(x)p(y)p(z)$$

and we also put it like this: the random variables, or rather their distributions, are not independent.
:::

### Induced pmf

:::{admonition} Proposition
If $X \colon \Omega \to \mathcal{X}$ is a random variable and $P_\Omega$ has a pmf $p_\Omega \colon \Omega \to [0,1]$,
then $p_X(x) := \sum_{\omega \in X^{-1}\left(\{ x \}\right)} p_\Omega(\omega)$
is a pmf of $X$.
:::

## Probability vector

:::{admonition} Example
If we put the children's jumper colours into an order,
say $r \mapsto 1,\ y \mapsto 2,\ b\mapsto 3,\ k \mapsto 4$,
then we have thereby defined a map $c \colon \mathcal{X} = \{r,y,b,k\} \to \mathcal{C} = \{1,2,3,4\}$.
The pmf of the random variable $c$, or rather $c \circ X$, is given by $p(i)$ for $i \in \mathcal{C}$.
This information can also be read as a vector.
:::

:::{admonition} Proposition
On an ordered finite set $\Omega = \{\omega_1, \dots, \omega_n\}$ a probability measure
is already uniquely determined by the vector $p \in \mathbb{R}^n$ with $p_i := p(\omega_i)$.
:::

:::{admonition} Proposition
Let $\Delta_n := \left\{p \in \mathbb{R}^n \ \mid\ 0 \leq p_i \leq 1 \text{ for all } i=1,\dots,n,\ \text{ and } \sum_{i=1}^n p_i = 1 \right\}$
and let $\Omega = \{\omega_1, \dots, \omega_n\}$ be arbitrary.
Then every $p \in \Delta_n$ defines a probability distribution on $\Omega$.
:::

:::{admonition} Example
The uniform distribution corresponds to $p \in \Delta_n$ with $p_i = \frac{1}{n}$; that is the geometric centre of $\Delta_n$.

The Dirac distribution with mass at $\xi \in \Omega$ corresponds to $p \in \Delta_n$ with $p_i = 1$ if $\omega_i = \xi$ and $p_i=0$ otherwise.
Geometrically that is a vertex of $\Delta_n$, of which there are $n$.
:::

A distribution given in this way by $p \in \Delta_n$ is also called a *categorical distribution*; we meet it again in the chapter [The most important discrete distributions](important-discrete-distributions.ipynb), where we also work out its expected value and its variance. Its simplest case has a name of its own.

:::{admonition} Definition
The case $n = 2$ has a name of its own. On $\Omega = \{0,1\}$ a probability vector is fixed by a single number, since $p_0 + p_1 = 1$ gives $p_0 = 1 - p_1$. Writing $\pi := p_1$, the distribution belonging to it is called the **Bernoulli distribution with parameter $\pi$**, and one writes $X \sim \operatorname{Ber}(\pi)$ for a random variable with this distribution. (In the chapter [The most important discrete distributions](important-discrete-distributions.ipynb) and in the literature this parameter is usually called $p$; here we write $\pi$, because in this section $p$ is already the probability vector.)
:::

:::{admonition} Example
A coin toss is $\operatorname{Ber}(\pi)$ with $\pi$ the probability of "heads"; every yes/no feature in a dataset ("survived", "clicked", "side effect occurred") can be modelled this way. The two special cases from above turn up again: $\pi = \frac12$ is the uniform distribution, $\pi = 0$ and $\pi = 1$ are the two Dirac distributions.
:::

Geometrically $\Delta_2$ is a line segment: the one joining the two vertices $(1,0)$ and $(0,1)$, and $\pi$ says where on this segment you are. To choose a Bernoulli distribution is therefore to choose a point on a line segment.

So $\Delta_n$ is the space of all possible probability distributions on an $n$-element set. The low cases are easy to picture: $\Delta_2$ is a line segment, $\Delta_3$ a filled triangle (two-dimensional, but embedded in $\mathbb{R}^3$), $\Delta_4$ a filled tetrahedron. In general $\Delta_n$ is an $(n-1)$-dimensional object with $n$ vertices, which one calls a **simplex**. One dimension always gets lost, because the entries have to add up to $1$ – which is exactly what we exploited for the Bernoulli distribution, when two numbers became one.

:::{admonition} Remark
This very simplex $\Delta_n$ is the image of the *softmax* function, with which neural networks output class probabilities: out of $n$ arbitrary real numbers it makes a vector in $\Delta_n$. The course *Introduction to Deep Learning* builds on your knowing $\Delta_n$ as the space of distributions on $n$ values.
:::

:::{admonition} Example
If we are given a distribution on a finite set $\Omega$ by the vector $p \in \Delta_n$,
we can characterise an event $A \subseteq \Omega$ by a vector as well:
the bitmask $\chi(A) \in \{0,1\}^n$ given by $\chi(A)_i = 1$ if $\omega_i \in A$, and $\chi(A)_i = 0$ otherwise.
The probability $P(A)$ is then given by

$$P(A) = \sum_{i=1, \omega_i \in A}^n p(\omega_i) = \sum_{i=1}^n p(\omega_i) \chi(A)_i = p \cdot \chi(A).$$

:::

## From data to models

The simplest form in which data can come to us is a single number, or a sequence of $N$ numbers. We like to call that an $N$-dimensional vector, or we picture the column of a table.
In statistics one speaks of a sample of size $N$. Later we will also have to deal with tables that hold more than one column, so that the data come as more complicated rows, but for now we want to stay in the simpler one-dimensional setting.

Even a single such column carries a probability distribution with it, with no modelling assumption at all: we simply count how often each value occurs.

:::{admonition} Definition
Let $D = (x_1,\dots,x_N)$ be a dataset with values in a finite set $\Omega$. Then

$$
P(\{x\}) := \dfrac{\left| \{ i : x_i = x \} \right|}{N},
$$

that is, the relative frequency of the value $x$ in $D$, defines a probability measure on $\Omega$. We call it the **distribution of the data** (also the *empirical distribution*).
:::

That this really is a probability measure is precisely the statement that the relative frequencies add up to $1$.

:::{admonition} Example
A dataset with a single column $x$ holding a colour:

| $i$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $x_i$ | blue | red | blue | green |

Here $\Omega = \{\text{blue}, \text{red}, \text{green}\}$ and $N = 4$. The distribution of the data is $P(\{\text{blue}\}) = \frac{2}{4}$, $P(\{\text{red}\}) = \frac{1}{4}$ and $P(\{\text{green}\}) = \frac{1}{4}$, so written as a probability vector $p = \left(\frac{1}{2}, \frac{1}{4}, \frac{1}{4}\right)$.
:::

If the values are coded as numbers $0, 1, 2, \dots$, you get this vector in a single line: `np.bincount(data) / len(data)` (see [Numpy](numpy.ipynb), section *Probability vectors*).

The following example is the special case $\Omega = \{0,1\}$, in which a single number fixes the whole distribution.

:::{admonition} Example
Given a sample of $N$ coin tosses $(x_1,\dots,x_N) \in \{0,1\}^N$ we can ask the question:
'what success probability $\pi$ was behind this coin?'

One possible estimate is $\frac{1}{2}$, arrived at without looking at the data.

If we do look at the sample, we can compute $e := \sum_{i=1}^N x_i$, the number of successes.
Then $N-e$ is the number of failures and $\hat{\pi} := \frac{e}{N}$ an estimate of the success probability $\pi$,
provided we assume that the same coin was tossed throughout.

In the language used above: every single toss is $\operatorname{Ber}(\pi)$-distributed, and $\hat{\pi}$ is an estimate of the parameter of that distribution – so we are looking for a point on the line segment $\Delta_2$.
:::

With that we have already cast every role statistics has, even if we will not need the words until later: the coin, which one could toss as often as one liked, is the **population**, the $N$ tosses are a **sample** from it, and $\hat{\pi}$ is a statement about the population won from the sample. In the same way a bag of sweets is the population and a handful out of it the sample, from which one estimates the distribution of colours in the bag. What you know or suspect before you reach in (the coin looks normal, the bag is a standard mix) is later called the **prior**. That the inference from the sample to the population is never certain, and how one puts a number on one's uncertainty, is the subject of the chapters [Expected value and variance](expectation-variance.md) (Chebyshev's inequality) and [Statistical tests](statistical-tests.md).

The distribution of the data is not yet a model – it is only another way of writing the data down. A model comes about only once an assumption is added. Suppose the colour dataset from above has grown by a fifth entry:

| $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $x_i$ | blue | red | blue | green | blue |

The distribution of the data is now $\left(\frac{3}{5},\frac{1}{5},\frac{1}{5}\right)$. If, however, we assume that the colours are equally frequent apart from one that occurs twice as often, then we choose as our model the distribution $p = \left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)$ – even though the observed relative frequencies are different ones. A distribution chosen in this way is called a **model distribution**. As a rule it has fewer parameters than the dataset has entries, it is smoother, and it says something about values that do not occur in the data at all.

A model can be used in both directions. Determining a model distribution from data is the estimation problem that the chapter [Statistical models and estimators](statistical-models.md) is about. The other way round, one can draw from a model distribution and obtain **synthetic data**: a dataset that looks like a real one but is not. Synthetic data are the standard tool for testing a method of analysis – because here one knows the right answer and can check whether the method finds it.

:::{admonition} Exercise
Draw $1000$ synthetic colour values for the model distribution $p = \left(\frac{1}{2},\frac{1}{4},\frac{1}{4}\right)$ and determine the distribution of the data you have generated. How far does it deviate from $p$, and how does that change with only $10$ drawn values? In the standard library the drawing is done by `random.choices(values, weights=..., k=1000)`, in Numpy by `rng.choice(values, size=1000, p=...)` (`random.choices` in the chapter [Programming with stochastics](programming-stochastics.ipynb), `rng.choice` in the chapter [Numpy](numpy.ipynb), section *Probability vectors*).
:::

We now have two distributions on the same $\Omega$: that of the data and that of the model. The next question is the question of the quality of the model – do the data look as though they had been drawn from the model? One asks *how likely is that?*, and the number that answers it is called the **likelihood**: the probability of seeing exactly the observed data if the model is correct. A model that makes this number as large as possible is the best one according to the **maximum likelihood principle**; this principle runs through the rest of the course and gets a section of its own in the chapter [Statistical models and estimators](statistical-models.md). It is not the only way to put a number on the difference between two distributions: the chapter [Expected value and variance](expectation-variance.md) measures the distance between data and synthetic data directly in the data space, and the chapter [Relative entropy](relative-entropy.md) measures it between the distributions themselves.

That marks out the path the rest of the course takes, and it can be found again in {numref}`ds-prozess-modell`: choose a section of the world, collect data, clean it ([Data cleaning](data-cleaning.ipynb)) and translate it into usable **features**, build models from those and measure the models against the data. Everything else is the working out of these five steps. The next chapter begins with the last of them: the comparison of data and model in a single number.

