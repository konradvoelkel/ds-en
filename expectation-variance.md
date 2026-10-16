---
title: "Expected value and variance: moments, entropy and independence"
short_title: "Expected value and variance"
description: "Quantifying deviation: absolute and squared deviation, the sample standard deviation, moments, the expected value discrete and continuous. With a digression on entropy in physics."
---

## Quantifying deviation

At the end of the previous chapter two distributions stood side by side: the distribution of the data and the model distribution. The question now facing us is how to capture their difference in a single number. The exact answer is the relative entropy, and we are saving that for a later chapter. But there is a much more direct route: instead of comparing the distributions, we compare the data themselves with what the model predicts – the real data against synthetic data, in data space, point by point. That is the route this chapter takes, and because it means taking distances between numbers, from here on we work with real-valued data.

Given two vectors $v,w \in \mathbb{R}^n$ (think of $v$ as our data and $w$ as what we expect),
the natural quantity to look at is the mean deviation $\sum_{i=1}^n \frac{v_i - w_i}{n}$.
The trouble with it is that positive and negative deviations cancel each other out.

### Absolute deviation

:::{admonition} Definition
The *mean absolute error* is
$\texttt{mae}(v,w) := \sum_{i=1}^n \dfrac{\left| v_i - w_i \right|}{n}$.

For a number $c \in \mathbb{R}$ we also write $\texttt{mae}(v,c):=\texttt{mae}(v,(c)_{i=1}^n)$.
:::

:::{admonition} Example
If $v = (1,2,3,4)$ and $c=2$, then $\texttt{mae}(v,c) = \sum_{i=1}^4 \dfrac{|i-2|}{4} = \dfrac{4}{4} = 1$.
:::

The sum without the factor $\frac1n$ is the $1$-norm of the difference,

$$
d_1(v,w) := \sum_{i=1}^n \left| v_i - w_i \right| = \left\| v - w \right\|_1 = n \cdot \texttt{mae}(v,w),
$$

and the factor $\frac1n$ in the definition is exactly what makes $\texttt{mae}$ independent of the length of the vector: $d_1$ grows with $n$ even when the model is no worse, $\texttt{mae}$ does not. Since comparing is almost always what we are after, we almost always take the mean. (On the role of the various norms, see also the remark on $L_0$, $L_1$ and $L_2$ in the chapter [Descriptive statistics](descriptive-statistics.md), as well as L1 and L2 regularisation in the chapter [Regression analysis](linear-regression.ipynb).)

:::{admonition} Example
So far $w$ has been constant. It need not be: let $v$ be four measured heights in centimetres and $w$ what a model predicted for those same four people.

| $i$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $v_i$ (measured) | 178 | 160 | 155 | 174 |
| $w_i$ (predicted) | 178 | 155 | 150 | 180 |
| $v_i - w_i$ | 0 | 5 | 5 | −6 |

Here $d_1(v,w) = 0 + 5 + 5 + 6 = 16$ and hence $\texttt{mae}(v,w) = \frac{16}{4} = 4$: on average the model is four centimetres off.

The mean deviation *without* the absolute value, the one we began this section with, gives $\frac{0 + 5 + 5 - 6}{4} = 1$ instead – deceptively small, because the error on person 4 cancels against those on persons 2 and 3. That is exactly why the absolute value is there.
:::

The obvious next question, for a given vector $v$, is which vector $w$ has the smallest mean absolute error. Without further conditions on $w$, though, the answer is immediate: $w=v$. We will come back to this question later; for now we content ourselves with asking which $c \in \mathbb{R}$ minimises $\texttt{mae}(v,c)$. Graphically: put the numbers from $1$ to $n$ on the $x$-axis and plot the values $v_i$ above them. A choice of $c \in \mathbb{R}$ is then a horizontal line, and we are asking which such line has the smallest combined distance to all the points.

:::{admonition} Example
Take the constant model $c = 165$ for the heights $v = (178, 160, 155, 174)$, that is, the claim "everybody is 165 cm tall". The deviations are $v_i - c = (13, -5, -10, 9)$, so

$$
d_1(v,165) = 13 + 5 + 10 + 9 = 37, \qquad \texttt{mae}(v,165) = \dfrac{37}{4} = 9.25.
$$

Is $165$ the best choice? That is precisely the question of the minimum, and as we shall see in a moment, it has a surprisingly simple answer.
:::

:::{admonition} Definition
$\texttt{median}(v) := \arg\min_{c \in \mathbb{R}} \texttt{mae}(v,c)$ is "the" *median* of $v$.
:::

So the median is defined as a number $c \in \mathbb{R}$ at which $\texttt{mae}(v,c)$ is minimal.
That is, for all $c$ we have $\texttt{mae}(v,c) \geq \texttt{mae}(v,\texttt{median}(v))$.
Careful: defined this way, several numbers can be "the" median. That is not a bug, it is a feature.

This definition may be unfamiliar, but it has the following property:

:::{admonition} Proposition
If $n \geq 3$ and $v \in \mathbb{R}^n$ is sorted, that is $v_i < v_j$ for $i < j$, then $v' := (v_2,\dots,v_{n-1}) \in \mathbb{R}^{n-2}$ defines a new (shorter) vector such that for all $c \in \mathbb{R}$ with $v_1 \leq c \leq v_n$:

$\texttt{mae}(v,c) = \texttt{mae}(v',c) + \dfrac{v_n - v_1}{n}$.
:::

Since the second summand does not depend on $c$, it plays no part in finding the minimum.
Applying this inductively, all that remains is to determine $\texttt{mae}(v,c)$ for vectors of length $1$ and $2$.
We have $\texttt{mae}((v_1),c) = |v_1 - c|$, which is minimal for $c = v_1$,
and $\texttt{mae}((v_1,v_2),c) = \frac{v_2 - v_1}{2}$, which is minimal for every $c$ between $v_1$ and $v_2$. So the median of a sorted list depends only on the middle value, or on the two middle values. The usual definition settles the latter case by choosing $\texttt{median}((v_1,v_2)) = \dfrac{v_1+v_2}{2}$, and that is what we will do from here on.
Convince yourself that for every $c$ with $a \leq c \leq b$ the mean distance to $(a,b)$ is $\frac{b-a}{2}$, so the vector $v = (a,b)$ has many medians.

:::{admonition} Proof
$$
\begin{aligned}
\texttt{mae}(v,c) &= \phantom{\dfrac{|v_1 - c|}{n} +\ } \sum_{i=1}^{n} \dfrac{|v_i -c |}{n} \\
                  &= \dfrac{|v_1 - c|}{n} + \sum_{i=2}^{n-1} \dfrac{|v_i -c |}{n} + \dfrac{|v_n - c|}{n} \\
                  &= \sum_{i=2}^{n-1} \dfrac{|v_i -c |}{n} + \dfrac{-(v_1 - c) + (v_n - c)}{n} \\
                  &= \texttt{mae}(v',c) + \dfrac{v_n - c + c - v_1}{n}.
\end{aligned}
$$
:::

The median, then, reflects the data rather poorly – it is completely independent of most of them! – so we need a better measure.
*Idea*: square the individual error terms in the sum, so that large errors contribute a larger share of it. Conveniently, squaring also spares us the absolute value: it takes care of the sign by itself.

### Squared deviation

:::{admonition} Definition
For vectors $v,w \in \mathbb{R}^n$ the *mean squared error* is defined as

$$
\texttt{mse}(v,w) := \sum_{i=1}^n \dfrac{{\left(v_i - w_i\right)}^2}{n}
$$

and for $c \in \mathbb{R}$ we write $\texttt{mse}(v,c) := \texttt{mse}(v, (c)_{i=1}^n)$.
:::

As with the absolute deviation, the sum without $\frac1n$ is a norm, this time the squared $2$-norm:

$$
d_2(v,w)^2 := \sum_{i=1}^n {\left( v_i - w_i \right)}^2 = \left\| v - w \right\|_2^2 = n \cdot \texttt{mse}(v,w).
$$

Compared with $\texttt{mae}$, the $\texttt{mse}$ comes in the square of the unit – for heights in centimetres that is square centimetres, which is hard to interpret. So the square root is usually taken at the end; for the constant model $w = \texttt{mean}(v)$ that gives the sample standard deviation of the next subsection.

:::{admonition} Proposition
For a vector $v \in \mathbb{R}^n$, the (arithmetic) *mean* of $v$ minimises the mean squared error:

$\texttt{mean}(v) := \sum_{i=1}^n \dfrac{v_i}{n} = \arg\min_{c \in \mathbb{R}} \texttt{mse}(v,c)$.
:::

:::{admonition} Proof
We write an arbitrary $c \in \mathbb{R}$ as $c = \texttt{mean}(v) + \delta$ and show that $\texttt{mse}(v,c)$ is minimal for $\delta = 0$.
To that end we expand $(v_i - \texttt{mean}(v) - \delta)^2 = (v_i - \texttt{mean}(v))^2 - 2\delta (v_i - \texttt{mean}(v)) + \delta^2$ and split the sum accordingly:

$$
\begin{aligned}
\texttt{mse}(v,c) &= \texttt{mse}(v,\texttt{mean}(v) + \delta) = \sum_{i=1}^n \dfrac{(v_i - (\texttt{mean}(v) + \delta))^2}{n} \\
                  &= \dfrac{1}{n} \sum_{i=1}^n \left( {\left(v_i - \texttt{mean}(v)\right)}^2 - 2\delta \left(v_i - \texttt{mean}(v)\right) + \delta^2 \right) \\
                  &= \left( \dfrac{1}{n} \sum_{i=1}^n \left( (v_i - \texttt{mean}(v))^2 \right) \right) - 2\delta \left( \sum_{i=1}^n \frac{v_i}{n} - \texttt{mean}(v) \right) + \delta^2 \\
                  &= \texttt{mse}(v,\texttt{mean}(v)) - 2\delta(\texttt{mean}(v) - \texttt{mean}(v)) + \delta^2 \\
                  &= \texttt{mse}(v,\texttt{mean}(v)) + \delta^2
\end{aligned}
$$

and this expression is minimal only for $\delta=0$, because $\delta^2 \geq 0$.
:::

:::{admonition} Example
The same four heights, this time with squared errors. For the model predictions $w = (178, 155, 150, 180)$,

$$
d_2(v,w)^2 = 0^2 + 5^2 + 5^2 + (-6)^2 = 86, \qquad \texttt{mse}(v,w) = \dfrac{86}{4} = 21.5.
$$

The comparison of the constant models is more interesting. The mean is $\texttt{mean}(v) = \frac{667}{4} = 166.75$. Sorted, the vector reads $(155, 160, 174, 178)$, and by the argument above every number between $160$ and $174$ is a median; the usual convention picks the midpoint, so $\texttt{median}(v) = 167$. The two error measures really do crown different winners:

| $c$ | $\texttt{mae}(v,c)$ | $\texttt{mse}(v,c)$ |
|---|---|---|
| $165$ | $9.25$ | $93.75$ |
| $\texttt{median}(v) = 167$ | $9.25$ | $90.75$ |
| $\texttt{mean}(v) = 166.75$ | $9.25$ | $\mathbf{90.6875}$ |

The middle column says the same thing three times: every number between $160$ and $174$ minimises the $\texttt{mae}$, $165$ included – the median simply is not unique. In the right-hand column, by contrast, exactly one number wins, and that is the mean. Choosing an error measure therefore means choosing a best model.
:::


### Sample standard deviation

:::{admonition} Definition
Let $v \in \mathbb{R}^n$. We call the square root of the mean squared error about the mean the $\texttt{rmse}$ (root mean squared error, also the sample standard deviation):

$\texttt{rmse}(v) = \sqrt{\texttt{mse}\left( v, \texttt{mean}(v) \right)}$.

It is also written $\sigma(v)$, the *standard deviation* of the sample $v$. The notation matches $\sigma(X)$ for random variables further down.
:::

For computation the definition is awkward: you first have to determine the mean and then go over all the entries a second time. The following rearrangement needs only the sum of the entries and the sum of their squares:

:::{admonition} Lemma
**(Shortcut formula)**

For $v \in \mathbb{R}^n$,

$$
\texttt{rmse}(v)^2 = \texttt{mse}\left( v, \texttt{mean}(v) \right) = \texttt{mean}(v^2) - \texttt{mean}(v)^2,
$$

where $v^2 := {\left( v_i^2 \right)}_{i=1}^n$ is to be read componentwise.
:::

:::{admonition} Proof
With $m := \texttt{mean}(v)$,

$$
\texttt{mse}(v, m) = \dfrac{1}{n} \sum_{i=1}^n \left( v_i^2 - 2 m v_i + m^2 \right) = \texttt{mean}(v^2) - 2m \cdot \texttt{mean}(v) + m^2 = \texttt{mean}(v^2) - m^2.
$$
:::

:::{admonition} Proposition
For $v \in \mathbb{R}^n$, $v \neq 0$, with $\texttt{mean}(v)=0$ (a *centred* sample, for instance $v := w - (\texttt{mean}(w))_{i=1}^n$ for an arbitrary $w \in \mathbb{R}^n$)
we have $\texttt{rmse}(v)^2 = \texttt{mse}(v,0) = \frac{1}{n} \sum_{i=1}^n v_i^2$, and the vector $v' := {\left( \dfrac{v_i}{\texttt{rmse}(v)} \right)}_{i=1}^n$ satisfies $\texttt{mean}(v')=0$ and $\texttt{rmse}(v')=1$ (a *normalised* sample).
:::

:::{admonition} Proof
This is a direct calculation. That the centred $v = w - (\texttt{mean}(w))_{i=1}^n$ really has mean $0$ is just the linearity of the mean: $\texttt{mean}(v) = \texttt{mean}(w) - \texttt{mean}(w) = 0$.
Since $\texttt{mean}(v) = 0$, we have $\texttt{rmse}(v)^2 = \texttt{mse}(v, \texttt{mean}(v)) = \texttt{mse}(v, 0) = \frac{1}{n} \sum_{i=1}^n v_i^2$, which is the shortcut formula with $m = 0$.
For $v'$ put $s := \texttt{rmse}(v)$; $s > 0$ because $v \neq 0$. Then $\texttt{mean}(v') = \frac{1}{n} \sum_{i=1}^n \frac{v_i}{s} = \frac{\texttt{mean}(v)}{s} = 0$ and therefore
$\texttt{rmse}(v')^2 = \texttt{mse}(v', 0) = \frac{1}{n} \sum_{i=1}^n \frac{v_i^2}{s^2} = \frac{\texttt{rmse}(v)^2}{s^2} = 1$.
:::

:::{admonition} Remark
Centring deserves a notation of its own. For $v \in \mathbb{R}^n$ we write

$$
\tilde{v} := v - \left( \texttt{mean}(v) \right)_{i=1}^n, \qquad \text{that is, } \tilde{v}_i = v_i - \texttt{mean}(v),
$$

and call $\tilde{v}$ the *centred* $v$. With the shortcut formula from above, the sample standard deviation and the variance can then be written without a summation sign:

$$
\sigma(v) = \texttt{rmse}(v) = \dfrac{1}{\sqrt{n}} \left\| \tilde{v} \right\|, \qquad
\sigma(v)^2 = \dfrac{1}{n}\, \tilde{v} \cdot \tilde{v} = \dfrac{1}{n}\, \tilde{v}^\top \tilde{v}.
$$

In the language of linear algebra, then, the sample standard deviation is nothing but the Euclidean length of the centred vector divided by $\sqrt{n}$, and the variance is the inner product of that vector with itself divided by $n$.
:::

This view carries further than it first appears. In the chapter [Covariance and dependence](covariance.md) it will turn out that the covariance of two random variables behaves exactly like an inner product – the variance is then the special case "vector with itself", and the correlation coefficient is the cosine of the angle between two centred vectors.

### Information content

Whether a vector $v \in \mathbb{R}^n$ carries information for us depends on how much we already know about $v$.
If we know, for example, that $v$ is a sample of a random variable uniformly distributed on $\{0,1\}$, we will not be surprised when $v$ looks like one. Every entry of $v$ corresponds to exactly one bit of information. Suppose instead that the random variable is not uniform but follows, on the numbers $\{1,\dots, 26\}$, the frequency of the letters of the German language, say (with $1$ for "a", $26$ for "z" and so on). Then an entry of $v$ potentially carries less information. The "e" is so frequent that we are hardly surprised to see one. An "x", on the other hand, would surprise us a great deal – but then it does not come up very often either. The average information content is therefore lower than for a uniform distribution.

### Measures of central tendency

Median and mean are traditionally joined by the **mode**, the most frequent value. It fits the same pattern: the median is the best constant model for the absolute error, the mean for the squared one, and the mode for the *counting error*, which counts every deviation the same, however large it is. For a nominal feature, say the `Survived` column of the Titanic list, that is the only error that makes sense; the best constant model is then the most frequent class, and the proportion of the time it is right is its *accuracy* (see [Titanic EDA](titanic-eda-numpy.ipynb)).
[Here is a short explainer video from Crash Course Statistics on mean, median and mode](https://www.youtube.com/watch?v=kn83BA7cRNM&list=PL8dPuuaLjXtNM_Y-bUAhblSAdWRnmBUcr). [The video that follows it in the playlist discusses the related notions for the spread of data](https://www.youtube.com/watch?v=R4yfNi_8Kqw) (the deviation we started with).



## Moments of a random variable

### From the mean to the expected value

So far we have computed with samples: $\texttt{mean}(v)$ is a number that comes from $n$ concrete measurements. Now we reverse the point of view and ask which number belongs to a *distribution*, that is, to the model the data might have come from. The route there is short, and it explains why the expected value looks exactly the way it does.

Let $X$ be a random variable with finitely many values $y_1,\dots,y_k$ and distribution $p = (p_1,\dots,p_k)$, so $p_j = P(X = y_j)$. Suppose for a moment that the $p_j$ are rational numbers with a common denominator $N$, say $p_j = \frac{a_j}{N}$ with $a_1 + \dots + a_k = N$. Then there is a sample of size $N$ that hits this distribution *exactly*: the one in which the value $y_j$ occurs precisely $a_j$ times. We call it the **idealised sample** $\tilde{D}$ for $p$ – the sample you would get if chance kept to the probabilities perfectly, just once.

We can write down the mean of this idealised sample directly, since we know how often each value occurs:

$$
\texttt{mean}(\tilde{D}) = \dfrac{1}{N} \sum_{j=1}^k a_j y_j = \sum_{j=1}^k \dfrac{a_j}{N} y_j = \sum_{j=1}^k p_j y_j.
$$

On the right there is no sample any more, only the distribution. With that, the assumption that the $p_j$ are rational has become superfluous too: the right-hand side makes sense for every distribution, and the detour through $\tilde{D}$ served only to find the formula. This quantity is exactly what we call the expected value of $X$.

:::{admonition} Example
A fair die has $p = \left(\frac16,\dots,\frac16\right)$, so $N = 6$ and $a_j = 1$ for all $j$. The idealised sample is $\tilde{D} = (1,2,3,4,5,6)$ – every face exactly once – with

$$\texttt{mean}(\tilde{D}) = \dfrac{1+2+3+4+5+6}{6} = \dfrac{21}{6} = 3.5.$$

So the expected value of a fair die is $3.5$, a number the die itself never shows.

A loaded die with $p = \left(\frac{1}{10},\frac{1}{10},\frac{1}{10},\frac{1}{10},\frac{1}{10},\frac{5}{10}\right)$ has $N = 10$, the idealised sample $(1,2,3,4,5,6,6,6,6,6)$ and hence the expected value $\frac{45}{10} = 4.5$.
:::

The special case $k = 1$ is the acid test: a distribution that takes a single value $y_1$ with probability $1$ – the Dirac measure $\delta_{y_1}$ from the chapter [The formalism of stochastics](intro-stochastics.md) – has the idealised sample $(y_1,\dots,y_1)$ and so the expected value $y_1$. A constant model and the value it predicts are the same thing. In the language of the previous section: the best constant model for the squared error was the mean of the data – and read as a distribution, a constant model is a Dirac measure.

:::{admonition} Example
On $\Omega = \{0,1,\dots,n-1\}$ – exactly what `range(n)` enumerates in Python – let $P$ be the uniform distribution. For $Y(\omega) := \omega$,

$$\mathbb{E}(Y) = \sum_{\omega=0}^{n-1} \dfrac{\omega}{n} = \dfrac{1}{n}\cdot\dfrac{(n-1)n}{2} = \dfrac{n-1}{2},$$

whereas for $X(\omega) := \omega + 1$ we get $\mathbb{E}(X) = \mathbb{E}(Y) + 1 = \frac{n+1}{2}$ (that is the linearity we come to further down). For $n = 6$ these are $2.5$ and $3.5$: whether you start counting the faces of a die at $0$ or at $1$ makes exactly one pip of difference. In simulations this is the most common source of off-by-one errors.
:::

With that we can set the formula down as a definition. It works word for word when $\Omega$ is countably infinite; the finite sum then becomes a series, which need no longer converge.

### Expected value, discrete

:::{admonition} Definition
Let $X \colon \Omega \to \mathbb{R}$ be a discrete real random variable (so $\Omega$ a discrete probability space, at most countable). Then the *expected value* of $X$ is defined as

$$
\mathbb{E}X := \mathbb{E}(X) := \sum_{\omega \in \Omega} X(\omega) P(\{\omega\}).
$$

If you would rather not work "in $\Omega$", you can rearrange this sum and sum over all the values $\{x_i\}_{i\in I}$ that $X$ takes:
$\mathbb{E}(X) = \sum_{i \in I} x_i P(X = x_i)$.
:::

So the expected value is the mean of the values of $X$, weighted by the probabilities.

For finite $\Omega$ the sum is finite and always exists. If $\Omega$ is countably infinite, the sum is a series, and a series need not converge: there are random variables for which no expected value can be determined. An example: on $\Omega = \{1, 2, 3, \dots\}$, $P(\{k\}) := \frac{6}{\pi^2 k^2}$ defines a probability measure (because $\sum_{k \geq 1} \frac{1}{k^2} = \frac{\pi^2}{6}$), and for $X(k) := k$ the series $\sum_{k \geq 1} k \cdot \frac{6}{\pi^2 k^2} = \frac{6}{\pi^2} \sum_{k \geq 1} \frac{1}{k}$ is the harmonic series, which diverges. This random variable has no expected value.

What we can say is this: if $X$ takes only finitely many values, then not only does the expected value exist but so do all the higher moments $\mathbb{E}(X^k)$ – they are finite sums, and those always converge. With countably infinitely many values, by contrast, you have to check each time. An example that is more than a mathematical curiosity: in the *St Petersburg paradox* a coin is tossed until heads first comes up, and if that takes $k$ tosses, $2^k$ euros are paid out. The probability of that is $2^{-k}$, so the expected value is $\sum_{k \geq 1} 2^k \cdot 2^{-k} = \sum_{k \geq 1} 1 = \infty$. A game with infinite expected value – and yet nobody would pay a high stake to play it.

For continuous random variables, which take uncountably many values, an integral over a density $f$ takes the place of the sum: $\mathbb{E}(X) = \int x f(x)\,dx$. We give this definition in the chapter [Continuous distributions](continuous-distributions.md), once we know about densities. Everything we establish about the expected value in this chapter holds for continuous random variables in just the same way, with integrals in place of sums.

### Digression: the expected value in general

::::{note}
**Digression (not part of the course proper):** the sum and the density integral are two special cases of a single definition that works for arbitrary random variables.

:::{admonition} Definition
Let $X \colon \Omega \to \mathbb{R}$ be a real random variable; then the *expected value* is defined as

$\mathbb{E}X := \mathbb{E}(X) := \int_{\Omega} X dP = \int_{\Omega} X(\omega) d P(\omega) \in \mathbb{R}$

that is, as the integral of the map $X$ with respect to the measure $P$.
:::

This integral (the Lebesgue integral with respect to $P$) need not exist, which again means that there are random variables for which no expected value can be determined. For discrete $\Omega$ it reduces to the sum $\sum_{\omega \in \Omega} X(\omega) P(\{\omega\})$ from above, and if $X$ has a density $f$ it becomes the integral $\int x f(x)\,dx$. With this general definition the rules of calculation below can be proved for all random variables at once; that is why measure theory sets things up this way.
::::

The expected value and the samples of a random variable are intimately connected:

:::{admonition} Theorem
**Law of large numbers**

An infinite sequence $(X_i)_{i \in \mathbb{N}}$ of random variables $\Omega \to \mathbb{R}$ is said to satisfy a *strong law of large numbers* if the mean-deviation random variables $\overline{X_n^\ast} := \dfrac{1}{n} \sum_{i=1}^n \left( X_i - \mathbb{E}(X_i) \right)$ converge to $0$, and do so $P$-almost surely (that is, $P(\lim_{n\to\infty} \overline{X_n^\ast} = 0) = 1$).

If the $X_i$ are independent and identically distributed (*iid* for short: every $X_i$ has the same distribution as a fixed $X$, and we write $X_i \sim X$) and the expected value $\mathbb{E}(X)$ exists,
then the $X_i$ satisfy a strong law of large numbers. That is,
$\overline{X_n^\ast} = \overline{X_n} - \mathbb{E}X$ – the deviation of the arithmetic mean of a sample of $X$ of size $n$ from the expected value – converges $P$-almost surely to $0$.
Read the other way round: the probability that the sample mean deviates from the expected value for arbitrarily large $n$ is $0$.
:::

$P$-almost sure convergence also implies convergence in probability:
$\lim_{n\to\infty} P\left(|\overline{X_n^\ast}| \geq \epsilon \right) = \lim_{n\to\infty} P\left(|\overline{X_n} - \mathbb{E}X| \geq \epsilon \right) = 0$ for every $\epsilon > 0$.

In what follows we shall not rack our brains any further over the notions of convergence in stochastics (that can always be caught up on later, and depending on the application it is worth doing). Instead, in the usual tradition, we take with us the reassurance that the expected value is a suitable quantity for analysing a sample expectantly. The larger the sample, the smaller the deviation of the sample mean from the expected value should be – so the law would have it. Put the other way round: for every prescribed bound $\epsilon > 0$ there is a sample size $n$ such that the sample mean of a randomly drawn sample almost always deviates from the expected value by less than $\epsilon$.

That closes the circle back to the idealised sample at the start of the section: there we pretended that a sample kept to the probabilities exactly, just to arrive at the formula at all. The law of large numbers says that real samples do so arbitrarily well for large $n$ – so the detour was no detour.


:::{admonition} Lemma
**Rules of calculation for the expected value:**

1. Linearity: the expected value is linear in $X$, so for $\alpha,\beta \in \mathbb{R}$ and random variables $X,Y \colon \Omega \to \mathbb{R}$,

$$
\mathbb{E}\left( \alpha X + \beta Y \right) = \alpha \mathbb{E} X + \beta \mathbb{E}Y.
$$

2. Monotonicity: the expected value is monotone in $X$, so for $X \leq Y$ we have $\mathbb{E}X \leq \mathbb{E}Y$.

3. $\sigma$-additivity: for a sequence $X_i \geq 0$ we have $\mathbb{E}(\sum_{i \geq 1} X_i) = \sum_{i \geq 1} \mathbb{E}(X_i)$.

4. Product rule: if $X$ and $Y$ are independent, then $\mathbb{E}(XY) = \mathbb{E}(X)\mathbb{E}(Y)$.

**Without proof**
:::

We have not yet explained what *independent* means (independently of the pmfs in the discrete case); that comes further down.




### Variance

:::{admonition} Definition
Let $X \colon \Omega \to \mathbb{R}$ be a random variable. Then

$\mathbb{V}X := \mathbb{V}(X) := Var(X) := \mathbb{E}\left( {\left(X - \mathbb{E}X\right)}^2 \right)$ is called the *variance* of $X$.
:::

:::{admonition} Proposition
**(Shortcut formula)**

We have $\mathbb{V}(X) = \mathbb{E}\left( X^2 \right) - {\left(\mathbb{E}X\right)}^2$.
:::

:::{admonition} Proof
We have ${\left(X - \mathbb{E}X\right)}^2 = X^2 - 2X\mathbb{E}X + {\left(\mathbb{E}X\right)}^2$, and so by the linearity of the expected value

$$
\begin{aligned}
\mathbb{V}(X) &= \mathbb{E}\left( {\left(X - \mathbb{E}X\right)}^2 \right) \\
              &= \mathbb{E}\left( X^2 \right) - 2\mathbb{E}\left( X \right)\mathbb{E}\left( X \right) + {\left(\mathbb{E}X\right)}^2 \mathbb{E}\left( 1 \right) \\
              &= \mathbb{E}\left( X^2 \right) - {\left(\mathbb{E}X\right)}^2.
\end{aligned}
$$
:::

This is the counterpart of the shortcut formula $\texttt{rmse}(v)^2 = \texttt{mean}(v^2) - \texttt{mean}(v)^2$ for samples above.
For a centred random variable, one with $\mathbb{E}(X) = 0$, this simply gives $\mathbb{V}(X) = \mathbb{E}(X^2)$.

:::{admonition} Definition
More generally, $\mathbb{E}(X^n)$ is called the $n$-th *moment* and $\mathbb{E}((X - \mathbb{E}X)^n)$ the $n$-th *central moment*.
So the expected value is the first moment and the variance the second central moment.
The third central moment divided by $\sigma^3$ is the *skewness*, and the fourth divided by $\sigma^4$ the *kurtosis*; the division makes both unit-free and independent of scale.
The skewness measures how symmetric the distribution is about the expected value.
$\sigma(X) := \sqrt{\mathbb{V}(X)}$ is called the *standard deviation* of X.
:::

The variance helps us judge how probable a given deviation from the expected value is. The key is an inequality that, to begin with, uses only the expected value:

:::{admonition} Theorem
**(Markov's inequality)**

For $X$ a real random variable with $X \geq 0$, and $c > 0$,

$$
P\left( X \geq c \right) \leq \dfrac{\mathbb{E}X}{c}.
$$
:::

:::{admonition} Proof
Let $1_{\{X \geq c\}} \colon \Omega \to \{0,1\}$ be the indicator function of the event $\{X \geq c\}$, so $1$ on $\{X \geq c\}$ and $0$ elsewhere. Then $c \cdot 1_{\{X \geq c\}} \leq X$ holds pointwise: where the indicator is $1$ we have $X \geq c$, and where it is $0$ we have $X \geq 0$ by assumption. The expected value of an indicator function is the probability of the event – in the discrete case, $\mathbb{E}(1_A) = \sum_{\omega \in A} P(\{\omega\}) = P(A)$. By the linearity and monotonicity of the expected value (rules of calculation above),

$$
c \cdot P(X \geq c) = \mathbb{E}\left( c \cdot 1_{\{X \geq c\}} \right) \leq \mathbb{E}X,
$$

and dividing by $c > 0$ gives the claim.
:::

Markov's inequality is crude, but it immediately yields the inequality we actually want:

:::{admonition} Theorem
**(Chebyshev's inequality)**

For $X$ a real random variable and $c > 0$,

$$
P\left( | X - \mathbb{E} X | \geq c \right) \leq \dfrac{\mathbb{V}X}{c^2}.
$$
:::

:::{admonition} Proof
The random variable $Y := {\left( X - \mathbb{E}X \right)}^2$ is non-negative, and by the definition of the variance $\mathbb{E}Y = \mathbb{V}X$. Markov's inequality for $Y$ with the bound $c^2 > 0$ gives

$$
P\left( {\left( X - \mathbb{E}X \right)}^2 \geq c^2 \right) \leq \dfrac{\mathbb{E}Y}{c^2} = \dfrac{\mathbb{V}X}{c^2}.
$$

Because $c > 0$, we have ${\left( X - \mathbb{E}X \right)}^2 \geq c^2$ exactly when $|X - \mathbb{E}X| \geq c$. The two events are therefore the same, and that is the claim.
:::

The special case $c=\sigma$ is trivial: the right-hand side is just $1$, and every probability is $\leq 1$.
The special case $c = k\sigma$ with $k \in \mathbb{N}$, however, simplifies to

$$
P\left( | X - \mathbb{E} X | \geq k\sigma \right) \leq \dfrac{1}{k^2}.
$$

So deviations of $2\sigma$ have probability $\leq \frac{1}{4}$, and deviations of $3\sigma$ only $\leq \frac{1}{9}$. Measured in multiples of $\sigma$, then, the probability of a deviation that large is roughly inversely proportional to the square – which is just what the inequality above says. That also gives us a criterion for weeding faulty data points out of a dataset: if deviations larger than $k\sigma$ with $k > 1$ turn up more often than expected, then those data points at least do not belong to the distribution we expect.

The most important application of the inequality is to the sample mean itself. With it we can actually prove the law of large numbers from above, in a weaker form and with exactly the tools we now have:

:::{admonition} Theorem
**(Weak law of large numbers)**

Let $X_1, \dots, X_n$ be independent and identically distributed like $X$ (iid for short; every $X_i$ has the same distribution as $X$), and let $X$ have finite variance. Then for the sample mean $\overline{X_n} := \frac{1}{n} \sum_{i=1}^n X_i$ and every $c > 0$

$$
P\left( | \overline{X_n} - \mathbb{E} X | \geq c \right) \leq \dfrac{\mathbb{V}X}{n c^2} \xrightarrow{n \to \infty} 0.
$$
:::

:::{admonition} Proof
By the linearity of the expected value, $\mathbb{E}\overline{X_n} = \frac{1}{n} \sum_{i=1}^n \mathbb{E}X_i = \mathbb{E}X$, since every $X_i$ has the same expected value as $X$.
By the rules of calculation for the variance (section *Rules of calculation for the variance* further down: $\mathbb{V}(aY) = a^2\,\mathbb{V}Y$, and the variance of a sum of independent random variables is the sum of the variances),

$$
\mathbb{V}\overline{X_n} = \dfrac{1}{n^2} \mathbb{V}\left( \sum_{i=1}^n X_i \right) = \dfrac{1}{n^2} \sum_{i=1}^n \mathbb{V}X_i = \dfrac{n\,\mathbb{V}X}{n^2} = \dfrac{\mathbb{V}X}{n}.
$$

Chebyshev's inequality for $\overline{X_n}$ now gives $P(|\overline{X_n} - \mathbb{E}X| \geq c) \leq \mathbb{V}\overline{X_n} / c^2 = \mathbb{V}X / (n c^2)$, and this expression tends to $0$ as $n \to \infty$.
:::

This is exactly the convergence in probability that we deduced above from the (unproved) strong law of large numbers: the weak law is the form we can prove with the means at hand; the strong law, with its almost sure convergence, needs more machinery but does without the assumption of finite variance.

The weak law is also the law of large numbers with a number attached: the probability of a deviation by more than $c$ falls like $1/n$ – or, read differently, the typical error of the sample mean shrinks like $1/\sqrt{n}$. To halve the error you need four times the sample. The bound is crude; the chapter [The normal distribution](normal-distribution.ipynb) supplies a sharper one with the central limit theorem, and the chapter [Statistical tests](statistical-tests.md) turns that into the recipe for inferring from sample to population.

:::{admonition} Remark
In deep learning the true loss of a model is the expected value of the loss function over the distribution of the data, and it cannot be computed, because that distribution is unknown. A mini-batch of a few data points supplies a sample mean of the loss instead: cheap, but with high variance. That is exactly the situation of the weak law of large numbers, and $\mathbb{V}X / n$ says how much noise a batch of size $n$ brings with it. The course *Introduction to Deep Learning* builds on this (stochastic gradient descent).
:::

Applying the law of large numbers to the random variable ${\left(X-\mathbb{E}(X)\right)}^2$ shows that the sample standard deviation converges to the standard deviation as well. So the sample standard deviation is a good substitute when the true variance of the random variable cannot be determined.


### Interlude: the logarithm

The next section computes with logarithms throughout. Since school may be a while ago, here is what you need, in half a page.

:::{admonition} Definition
For $b > 0$, $b \neq 1$, the *logarithm to base $b$* is the inverse of exponentiation: from $b^x = y$ it follows that $x = \log_b(y)$, and conversely. It is defined for $y > 0$.

Three bases have names of their own: $\ln := \log_e$ (the *natural* logarithm, to base $e \approx 2.718$), $\operatorname{lb} := \log_2$ (the *binary* logarithm, also written $\operatorname{ld}$) and $\log_{10}$ (the *common* one).
:::

The logarithm counts orders of magnitude. To base $10$ you can read that off directly: $\log_{10}(100) = 2$ and $\log_{10}(1000) = 3$, and because the logarithm is strictly increasing, $\log_{10}(y)$ lies between $2$ and $3$ for every number $y$ between $100$ and $1000$. The number of decimal digits of a natural number $y$ is therefore $\lfloor \log_{10}(y) \rfloor + 1$ – and to base $2$, likewise, the number of binary digits.

The rules of calculation all follow from $e^{\ln(y)} = y$ and $\ln(e^x) = x$ together with the power law $(e^u)^v = e^{uv}$:

$$
\begin{aligned}
b^x &= \left( e^{\ln b} \right)^x = e^{\ln(b)\, x}, \\
\ln\left( b^x \right) &= x \ln(b), \\
\ln(y) &= \ln\left( b^{\log_b(y)} \right) = \ln(b) \log_b(y), \\
\text{so}\quad \log_b(y) &= \dfrac{\ln(y)}{\ln(b)}.
\end{aligned}
$$

The last line is the *change-of-base formula*: logarithms to different bases differ only by a constant factor. That is why the choice of base for the entropy is a question of units, not of substance – to base $2$ you measure in **bits**, to base $e$ in **nats**, and the two differ by the factor $\ln(2) \approx 0.693$.

:::{admonition} Example
The number $77$ is $1001101_2$ in binary, that is $64 + 8 + 4 + 1$, and so needs $7$ binary digits. Check: $\log_2(77) = \frac{\ln 77}{\ln 2} \approx 6.27$, and $\lfloor 6.27 \rfloor + 1$ gives the expected $7$ digits. Read the other way round: with $7$ bits you can distinguish $2^7 = 128$ different things, with $6$ bits only $64$ – too few for $77$.
:::

In numpy the three functions are called `np.log` (natural, *not* common – a frequent source of errors), `np.log2` and `np.log10`.

## Entropy

::::{note}
**Looking ahead (not part of the course proper): where the word comes from.** The notion of entropy comes from thermodynamics, and the physical picture goes a long way towards explaining why the formula below looks the way it does. You do not need this section for the course.

Picture two identical containers with the same number of gas particles in them. In the first the particles are evenly distributed, in the second they are all huddled in one corner.

```{figure} images/entropie-gas-hoch.png
:width: 360px
:align: center
:name: entropie-gas-hoch

Evenly distributed particles: high entropy.
```

```{figure} images/entropie-gas-niedrig.png
:width: 360px
:align: center
:name: entropie-gas-niedrig

All the particles in one corner: low entropy.
```

The second state surprises us; the first does not. We also know how the story continues: before long the second container will look like the first, while the first will never look like the second. That is the **second law of thermodynamics**: in a closed system, entropy cannot decrease. A fried egg cannot be turned back into a raw one.

The obvious gloss, "entropy = disorder", is misleading. More precise is the distinction between *macrostate* and *microstate*. The macrostate is what can be measured – temperature, pressure, "all the particles on the left" – and the microstate is the complete specification of where every single particle sits. A macrostate usually comprises an enormous number of microstates, and exactly that number is the measure: the macrostate "evenly distributed" comprises unimaginably more arrangements than the macrostate "all in the top left corner". Ludwig Boltzmann cast this into the formula

$$
S = k_B \ln W
$$

in which $W$ is the number of microstates belonging to the given macrostate and $k_B$ a physical constant whose only job is to get the unit right. Put a partition into both containers and the difference becomes tangible:

```{figure} images/entropie-gas-hoch-geteilt.png
:width: 360px
:align: center
:name: entropie-gas-hoch-geteilt

With a partition: there is roughly the same amount of gas on the left and on the right – this macrostate can be produced in a great many ways.
```

```{figure} images/entropie-gas-niedrig-geteilt.png
:width: 360px
:align: center
:name: entropie-gas-niedrig-geteilt

With a partition: all the gas is on the left – this macrostate admits only a few arrangements.
```

:::{admonition} Remember
Entropy is always defined *relative to a macrostate*. We count the possibilities compatible with what we know, and then take the logarithm.
:::

Carry that sentence over unchanged when you read the definition for random variables in a moment: there the macrostate is the distribution we know, and what gets counted (more precisely, weighted) are the outcomes it allows. The logarithm stays.
::::

Claude Shannon (1916–2001) carried the notion from physics into communications engineering in his 1948 paper *A Mathematical Theory of Communication* {cite}`shannon1948`, with which information theory began as a field of its own. Shannon asked how many bits are needed, at the very least, to transmit a message, and found the same quantity Boltzmann had written down for gas particles. In his honour it is also called the *Shannon entropy*.

:::{admonition} Definition
For a discrete probability space $\Omega$ and $x \in \Omega$ we call the *information* (also the *self-information*) of $x$

$$
I(x) := -\log_b(P(\{x\})).
$$

The base $b$ of the logarithm is usually $2$, but in the end it does not matter much.
For a random variable $X \colon \Omega' \to \Omega$ we can now consider the composition $I \circ X \colon \Omega' \to \mathbb{R}$,
a real random variable. Its expected value is the average information of $X$, which we also call the *entropy*

$$
\begin{aligned}
H(X) := \mathbb{E}\left( I(X) \right) &= \sum_{\omega' \in \Omega'} -\log_b\big(P_X(\{X(\omega')\})\big)\, P_{\Omega'}(\{\omega'\}) \\
                                      &= - \sum_{\omega \in \Omega} \log_b(P(\{\omega\}))P(\{\omega\}).
\end{aligned}
$$
:::

:::{admonition} Remark
The sum for $H(X)$ has a problem: for $P(\{\omega\}) = 0$, $\log_b(0)$ is undefined. So we extend the function $x \mapsto x\log x$ to $0$ by its limit,

$$
\lim_{x \to 0^+} x \log x = 0
$$

(l'Hôpital applied to $\frac{\log x}{1/x}$) and set $0 \log 0 := 0$. Summands belonging to impossible outcomes then contribute nothing, and the sum effectively runs only over the $\omega$ with $P(\{\omega\}) > 0$. That is the convention behind the sums written "over $p_i \neq 0$" in the chapter [Relative entropy](relative-entropy.md).
:::

:::{admonition} Example
For a uniform distribution on $\Omega = \{1,\dots,n\}$ we always have $P(\{x\}) = \frac{1}{n}$ for $x\in\Omega$,
so $I(x) = -\log_2(P(\{x\})) = -\log_2\frac{1}{n} = \log_2(n)$ and hence
$H(X) = \sum_{i=1}^n \frac{\log_2(n)}{n} = \log_2(n)$.
This number tells us that on average we need $\log_2(n)$ bits to communicate a single outcome of $X$, provided sender and receiver know the distribution; a sample of size $N$ then costs $N \log_2(n)$ bits. There are other distributions for which less information per outcome suffices on average – strictly speaking every other one, in fact, since the uniform distribution has maximal entropy among all discrete distributions. It corresponds to knowing as little as possible and therefore taking all outcomes to be equally probable.
:::

:::{admonition} Example
**How much information is there in a letter?** Count the frequencies of the letters in German texts, put them into the formula, and out comes an entropy of about $4.06$ bits per character {cite}`fox2008`. For comparison: if all $26$ letters were equally probable it would be $\log_2(26) \approx 4.70$ bits. The difference is exactly what the unequal frequencies of "e" and "x" save.

Take into account which letters have *gone before* as well, and the value drops to about $1.5$ bits per letter – after "sch" the next letter is hardly a surprise. Language, then, is highly redundant, which is why text compresses so well and why you can still understand a sentence with half of it missing.

What that means in practice shows up in guessing. A random string of length $10$ over the alphabet, say `pashglwnmv`, carries $10 \cdot 4.70 \approx 47$ bits – guessing it takes on the order of $2^{47}$ attempts. If the guesser knows instead that it is a German word, say `kabelkanal`, that is only $10 \cdot 1.5 = 15$ bits, or $2^{15} = 32{,}768$ attempts. That is the difference between "practically impossible" and "done in a second", and it comes not from the length of the string but from what the guesser knows about it.
:::

This very argument is at the heart of one of the best-known comics on security:

```{figure} images/xkcd-password-strength.png
:width: 480px
:align: center
:name: xkcd-password

Randall Munroe, [xkcd 936 "Password Strength"](https://xkcd.com/936/) (CC BY-NC 2.5)
```

The password `Tr0ub4dor&3` looks complicated, but it was built by a procedure an attacker knows (a word, a few of the usual substitutions, a digit, a special character) – it carries around $28$ bits. Four randomly chosen words such as `correct horse battery staple` carry around $44$ bits, so they are about $2^{16} \approx 65{,}000$ times harder to guess – and easier to remember into the bargain.

The lesson is the same as in the previous example: entropy depends not on how the outcome looks but on the **procedure that produced it**. A password is secure not because it looks cryptic but because the set of passwords it could have come from is large. That is why the question "how strong is this password?" strictly speaking has no answer for a single password – what can be answered is how strong the procedure is.

At the other end of the scale stands the Dirac distribution: if $P(\{\xi\}) = 1$ for a single $\xi \in \Omega$
and $P(\{\omega\}) = 0$ for all the others, then $I(\xi) = -\log_2(1) = 0$ and hence $H(X) = 0$
(the summands with $P(\{\omega\}) = 0$ fall under the convention $0\log 0 = 0$ from above).
That is the smallest possible value, since $H(X)$ is a sum of non-negative terms.
On a finite set $\Omega$, then, we always have $0 \leq H(X) \leq \log_2|\Omega|$,
with the minimum attained exactly by the Dirac distributions (there are $|\Omega|$ of them, one per element)
and the maximum only by the uniform distribution.

Entropy is best understood as a relative quantity, and that is how we shall treat it later on. In the rest of the course it turns up in two places: in setting up statistical models – the maximum entropy principle in the chapter [The normal distribution](normal-distribution.ipynb) and the closely related maximum likelihood principle in the chapter [Statistical models and estimators](statistical-models.md) – and in assessing how good a model is, where the tools are cross-entropy and relative entropy in the chapter [Relative entropy](relative-entropy.md).


## Independence

:::{admonition} Definition
Let $\Omega$ be a probability space. Events $A,B \subseteq \Omega$ are called *independent of each other* if

$$
P(A\cap B) = P(A) \cdot P(B).
$$

More generally, a family $(A_i)_{i\in I}$, $A_i \subseteq \Omega$, of events is called *independent* if
for every finite subset $J \subseteq I$ of indices:

$$
P\left( \bigcap_{j \in J} A_j \right) = \prod_{j\in J} P(A_j).
$$
:::

In general it makes a real difference whether a family is independent or only pairwise independent, which is why the definition in terms of families matters.

:::{admonition} Example
**Independent: two dice.** We throw two fair six-sided dice. As the probability space we take $\Omega = \{1,\dots,6\}^2$ with the uniform distribution, so $36$ equally probable outcomes $(i,j)$. Let $A$ be the event "the first die shows an even number" and $B$ the event "the second die shows a six". Then

$$
P(A) = \dfrac{18}{36} = \dfrac{1}{2}, \qquad P(B) = \dfrac{6}{36} = \dfrac{1}{6}.
$$

For the intersection we count rather than use a formula: $A \cap B = \{(2,6),(4,6),(6,6)\}$, so $P(A \cap B) = \frac{3}{36} = \frac{1}{12}$. And indeed $\frac12 \cdot \frac16 = \frac{1}{12}$, so the two events are independent.

That we counted matters: had we computed $P(A\cap B)$ as a product straight away, we would have assumed independence instead of checking it. Here it is obvious anyway, since $A$ and $B$ refer to different dice.
:::

:::{admonition} Example
**Dependent: sweets without replacement.** There are three sweets in a bag: a red one, a green one and a blue one. We draw two of them one after the other, without putting the first back. The probability space is the set of the $6$ ordered pairs of distinct colours,

$$
\Omega = \{(r,g),(r,b),(g,r),(g,b),(b,r),(b,g)\},
$$

again with the uniform distribution. Let $A$ be the event "the first sweet is red" and $B$ the event "the second sweet is green". Then $A = \{(r,g),(r,b)\}$ with $P(A) = \frac{2}{6} = \frac13$ and $B = \{(r,g),(b,g)\}$ with $P(B) = \frac{2}{6} = \frac13$. The intersection contains just one outcome, $A \cap B = \{(r,g)\}$, so

$$
P(A \cap B) = \dfrac{1}{6} \neq \dfrac{1}{9} = P(A)\,P(B).
$$

The two events are therefore *not* independent. That makes sense too: if the red sweet was drawn first, only green and blue are left, and green has suddenly become more probable on the second draw – up from $\frac13$ to $\frac12$. That number gets a name further down: it is the conditional probability $P(B \mid A)$.

Drawing without replacement is `random.sample` in Python, drawing with replacement `random.choices` (see [Programming with stochastics](programming-stochastics.ipynb)) – the difference between the two functions is exactly the difference between dependent and independent.
:::

:::{admonition} Definition
Let $\Omega$ be a probability space.
A family of random variables $(Y_i)_{i \in I}$, $Y_i \colon \Omega \to \Omega_i$, is called *independent* if
for arbitrary events $B_i \subseteq \Omega_i$ the family $\left( \{Y_i \in B_i\} \right)_{i \in I}$ is independent in $\Omega$.
:::

:::{admonition} Remark
For two random variables $X, Y \colon \Omega \to \mathbb{R}$ this reads as follows: $X$ and $Y$ are independent exactly when

$$
P(X \in A,\ Y \in B) = P(X \in A)\,P(Y \in B)
$$

holds for all events $A, B$. The left-hand side is shorthand for $P\left( (X,Y) \in A \times B \right)$ – so it is not about $X$ and $Y$ separately but about the pair $(X,Y)$, understood as *one* random variable with values in $\mathbb{R}^2$. Its distribution is called the **joint distribution** of $X$ and $Y$; we define it formally in the chapter [Covariance and dependence](covariance.md).

The direction matters: the joint distribution is the real information, and the distributions of $X$ and $Y$ separately follow from it. The other way round does *not* work – from the individual distributions alone the joint one generally cannot be reconstructed. That is exactly what independence says: it is the extra assumption under which the product $p(x)q(y)$ of the two pmfs is the joint pmf.
:::

:::{admonition} Example
For $I = \{1,\dots,n\}$ and each $\Omega_i$ discrete, $Y_1,\dots,Y_n$ are independent exactly when for all outcomes $\omega_i \in \Omega_i$:

$$
P(Y_1=\omega_1, \dots, Y_n=\omega_n) = \prod_{i=1}^n P(Y_i = \omega_i).
$$
:::

Another notion comes up very often in this connection:

:::{admonition} Definition
Let $\Omega$ be a probability space. For events $A,B \subseteq \Omega$,

$$
P(A | B) := \dfrac{P(A\cap B)}{P(B)}
$$

is called the *conditional probability* of $A$ given $B$.
:::

Clearly, for $P(B) > 0$, $A$ and $B$ are independent of each other exactly when $P(A | B) = P(A)$.
In the sweets example above, $P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{1/6}{1/3} = \frac12$, which is not $P(B) = \frac13$ – that is what dependence looks like in numbers.
Conditional probabilities therefore come up (or rather, become interesting) precisely when two events, or two random variables, are not independent.

:::{admonition} Looking ahead
Independence is an all-or-nothing property; in real data the more interesting question is *how strongly* two quantities are related. We will meet two measures for that, and it is worth keeping them apart from the start.

The first is the **covariance** and the correlation coefficient formed from it (chapter [Covariance and dependence](covariance.md)). It measures *linear* relationships. Independence implies that the covariance is $0$ – but not conversely: two quantities can depend on each other perfectly and still be uncorrelated, for instance $X$ and $X^2$ for symmetrically distributed $X$. So "correlated" is a stronger statement than "dependent", and "uncorrelated" a weaker one than "independent".

The second measure captures dependence of any shape: the **relative entropy** between the joint distribution and the product of the individual distributions, also called *transinformation* or *mutual information* $I(X;Y)$ (chapter [Relative entropy](relative-entropy.md)). It is $0$ exactly when the two random variables are independent – so it really does measure dependence and not just its linear part. The price: you need the joint distribution, and estimating that is considerably more work than computing a covariance.
:::

### Rules of calculation for the variance

The expected value is linear; the variance is not. Instead, the following two rules hold,
and we will need them constantly in the next chapter.

:::{admonition} Lemma
Let $X \colon \Omega \to \mathbb{R}$ be a random variable with finite variance.

1. For $a,b \in \mathbb{R}$, $\mathbb{V}(aX+b) = a^2\,\mathbb{V}(X)$.

2. If $X$ and $Y$ are independent, then $\mathbb{V}(X+Y) = \mathbb{V}(X) + \mathbb{V}(Y)$.
   More generally, for pairwise independent $X_1,\dots,X_n$,

$$
\mathbb{V}\left( \sum_{i=1}^n X_i \right) = \sum_{i=1}^n \mathbb{V}(X_i).
$$
:::

:::{admonition} Proof
(1) By the linearity of the expected value, $\mathbb{E}(aX+b) = a\,\mathbb{E}X + b$, so

$$
aX + b - \mathbb{E}(aX+b) = a\left( X - \mathbb{E}X \right)
$$

and hence $\mathbb{V}(aX+b) = \mathbb{E}\left( a^2 {\left( X - \mathbb{E}X \right)}^2 \right) = a^2\,\mathbb{V}(X)$.
In particular, a shift by $b$ does not change the variance.

(2) We expand and use linearity:

$$
\begin{aligned}
\mathbb{V}(X+Y) &= \mathbb{E}\left( {\left( (X - \mathbb{E}X) + (Y - \mathbb{E}Y) \right)}^2 \right) \\
                &= \mathbb{E}\left( {(X - \mathbb{E}X)}^2 \right) + \mathbb{E}\left( {(Y - \mathbb{E}Y)}^2 \right)
                   + 2\,\mathbb{E}\left( (X - \mathbb{E}X)(Y - \mathbb{E}Y) \right) \\
                &= \mathbb{V}(X) + \mathbb{V}(Y) + 2\left( \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y) \right).
\end{aligned}
$$

If $X$ and $Y$ are independent, the bracketed expression equals $0$ by the product rule.
The general case follows the same way: expand, and all the mixed terms $\mathbb{E}(X_iX_j) - \mathbb{E}X_i\,\mathbb{E}X_j$ with $i \neq j$ vanish – pairwise independence is enough for that (chapter [Covariance](covariance.md)).
:::

The term $\mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)$ that has just vanished is an interesting quantity in its own right:
it is called the *covariance* of $X$ and $Y$, and it measures how strongly the two variables are linearly related.
In the chapter [Covariance](covariance.md) we put it under the microscope and prove the rule once more there,
in its general form, without the assumption of independence.

Rule (2) is why the variance of a sum of independent repetitions of the same experiment
is so easy to compute – we use that in the chapter
[The most important discrete distributions](important-discrete-distributions.ipynb)
for the binomial distribution.
