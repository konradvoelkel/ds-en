# Relative entropy

## Logarithms

The elementary properties of the logarithm – definition, change of base, bit and nat – are in the digression in the chapter [Expected value and variance](expectation-variance.md). Here we are after a different question: why it is the logarithm, of all functions, that turns up in information theory, and nothing else.

:::{admonition} Lemma
Let $l \colon \{1,\dots\} = \mathbb{N}_{>0} \to \mathbb{R}$ be a function with
1. $l(ab) = l(a) + l(b)$ – "completely additive"
2. $l(n+1) \geq l(n)$ – "monotonically increasing"
Then there is a constant $c \in \mathbb{R}$ such that $l(n) = c \ln(n)$.
:::

:::{admonition} Remark
Because of the formula

$$
\ln(x) = \dfrac{\log_a(x)}{\log_a(e)}
$$

we can read the constant $c$ as $c = \log_a(e)$,
that is, the function $l$ is a logarithm to base $a$.
:::

It is equally clear that the same lemma holds for $\log_2$ in place of $\ln$ (only the constant is a different one).

So if we want to count something in such a way that the count of a product is the sum of the individual counts, then we have to do it with a logarithm.

:::{admonition} Proof
We want to show that for functions $f,g \colon \mathbb{N}_{>0} \to \mathbb{R}$ satisfying the conditions of the lemma,

$$
f(n) g(2) = f(2) g(n)
$$

always holds, since with $g = \ln$ this proves the lemma ($c=f(2)$).

Let $n,k,m \in \mathbb{N}$ be such that $2^{m-1} \leq n^k \leq 2^m$.
Monotonicity then gives

$$
f(2^{m-1}) \leq f(n^k) \leq f(2^m)
$$

and additivity gives

$$
(m-1)f(2) \leq kf(n) \leq mf(2)
$$

The same chain of inequalities holds for $g$ in place of $f$; that one we also multiply by $-1$:

$$
-mg(2) \leq -kg(n) \leq -(m-1)g(2).
$$

The sum of these two chains of inequalities now simplifies to

$$
-f(2)g(2) \leq k\left(f(n)g(2) - f(2)g(n)\right) \leq f(2)g(2)
$$

Dividing by $k$ and then letting $k \to \infty$, we see
that $f(n)g(2) - f(2)g(n) \to 0$ (as $k \to \infty$, on which it does not depend at all).
:::

:::{admonition} Lemma
If a continuous function $F \colon \mathbb{R} \to \mathbb{R}$ satisfies the functional equation $F(xy) = xF(y) + F(x)y$ and $F(x)/x$ is monotonically increasing, then there is a constant $c \in \mathbb{R}$ such that $F(x) = -x\log(x)c$.
:::

:::{admonition} Proof
The function $g(x) := F(x)/x$ satisfies $g(xy) = g(x) + g(y)$ and is monotonic by assumption, so there is a $c'$ with $g(x) = c'\log(x)$, and $c:=-c'$ does the job.
:::

:::{admonition} Remark
So we see that the entropy contribution $-p\log(p)$ of an outcome with probability $p$ is a very natural quantity. (The *self-information* $I(x) = -\log P(\{x\})$ from the chapter [Expected value and variance](expectation-variance.md) is the factor behind the $p$.)
:::

:::{admonition} Lemma
The logarithm is a *concave* function, that is, for a convex combination $\lambda x + \mu y$ (so $\lambda + \mu = 1$ and $0 \leq \lambda, \mu \leq 1$) we have

$$
\lambda \log(x) + \mu \log(y) \leq \log(\lambda x + \mu y)
$$
:::

:::{admonition} Proof
**Idea:**
The derivative of $\log(x)$ is $\frac{1}{x}$, and that is strictly decreasing on $(0,\infty)$. With the mean value theorem one can now show that $\log(x)$ must be strictly concave (so even $<$ rather than $\leq$ in the inequality above).
:::

We have already used a heuristic argument for this, but now we can prove it rigorously:

:::{admonition} Proposition
If $p = (p_1,\dots,p_n)$ describes a discrete distribution on $\Omega = \{1,\dots,n\}$, then the entropy satisfies
$H(p) \leq \log(n)$ (the entropy of the uniform distribution).
:::

:::{admonition} Proof
We use the fact that the sum in the definition of the entropy is a convex combination, and that the logarithm is concave:

$H(p) = \sum_{i=1, p_i\neq 0}^n p_i \log \frac{1}{p_i} $

$\leq \log \left( \sum_{i=1, p_i\neq 0}^n p_i \frac{1}{p_i} \right)$

$\leq \log\left( \sum_{i=1}^n 1 \right) = \log(n)$
:::


## Definition and properties

:::{admonition} Definition
Let $p,r \in \Delta_n$ (the set of probability vectors in $\mathbb{R}^n$, that is, vectors whose entries lie between $0$ and $1$ and whose entries sum to exactly $1$).
The *entropy* (also: Kullback–Leibler divergence $D_{KL}$) of $p$ relative to $r$ is

$H(p \Vert r) := \sum_{i,\ p_i > 0}^n p_i \log \left( \frac{p_i}{r_i} \right) \in \mathbb{R} \cup \{\infty\}.$
:::

:::{admonition} Proposition
Write $u_n = (\frac{1}{n}, \dots, \frac{1}{n}) \in \Delta_n$ for the uniform distribution on $\{1,\dots,n\}$.
Then

$$
H(p \Vert u_n) = H(u_n) - H(p) = \log(n) - H(p)
$$
:::

:::{admonition} Proposition
$$
H(p \Vert r) = 0 \text{ if and only if } p=r
$$
(without proof)
:::

:::{admonition} Proposition
$$
H(p \Vert r) \geq 0
$$
:::

:::{admonition} Proof
$H(p \Vert r) = \sum p_i \log \left( \dfrac{p_i}{r_i} \right) = -\sum p_i \log \left( \dfrac{r_i}{p_i} \right)$ (since $\log(a/b) = -\log(b/a)$)
$\geq - \log \left( \sum p_i \dfrac{r_i}{p_i} \right) \geq - \log \left( \sum r_i \right) = -\log 1 = 0$

where we have again used the concavity of the logarithm.
:::

:::{admonition} Example
Relative entropy is not symmetric, and it can become infinite. Let $p_t := (t,\ 1-t)$ for $0 < t < 1$, a coin that for small $t$ comes up $1$ almost surely. In one direction,

$$
H\left(u_2 \,\Vert\, p_t\right) = \frac{1}{2} \log \frac{1}{2t} + \frac{1}{2}\log \frac{1}{2(1-t)} \xrightarrow{t \to 0} \infty,
$$

since the first summand grows beyond all bounds like $-\frac12\log t$. In the other direction the proposition above gives

$$
H\left(p_t \,\Vert\, u_2\right) = \log(2) - H(p_t), \qquad H(p_t) = -t\log t - (1-t)\log(1-t) \xrightarrow{t \to 0} 0,
$$

so $H(p_t \Vert u_2) \to \log 2$: finite, and to base $2$ exactly one bit. Take the almost certain coin $p_t$ for a fair one and you pay at most one bit; take the fair coin for $p_t$, and the side you thought impossible will surprise you infinitely.
:::

## Joint entropy

:::{admonition} Definition
The *joint entropy* of two discrete random variables $X,Y$ is

$$
H(X,Y) := \mathbb{E} I_{X,Y} = -\sum_{i=1}^n \sum_{j=1}^n P(X = z_i, Y=z_j) \log P(X=z_i, Y=z_j)
$$
:::

:::{admonition} Proposition
$$
H(X) + H(Y) \geq H(X,Y) \geq \max\left( H(X), H(Y) \right)
$$
:::

:::{admonition} Example
$$
H(X,X) = H(X)
$$

since in the sum for the left-hand expression every summand off the diagonal is $0$.
:::

:::{admonition} Proposition
If $X, Y$ are independent random variables, then $H(X, Y) = H(X) + H(Y)$.
:::

:::{admonition} Proof
Independence means that for all $i,j$:

$$
P(X = z_i, Y = z_j) = P(X = z_i)\cdot P(Y = z_j)
$$

We take logarithms:

$$
\log P(X = z_i, Y = z_j) = \log P(X = z_i) + \log P(Y = z_j)
$$

and so altogether we have

\begin{align}
H(X,Y) &:= -\sum_{i=1}^n \sum_{j=1}^n P(X = z_i, Y = z_j) \log P(X = z_i, Y = z_j) \\
 &= -\sum_{i=1}^n \sum_{j=1}^n P(X = z_i)P(Y = z_j) \left( \log P(X = z_i) + \log P(Y = z_j) \right) \\
 &= -\sum_{i=1}^n \sum_{j=1}^n P(X = z_i)P(Y = z_j)\log P(X = z_i)\\
 &\phantom{=}\ \ -\sum_{i=1}^n \sum_{j=1}^n P(X = z_i)P(Y = z_j)\log P(Y = z_j) \\
 &= -\sum_{i=1}^n P(X = z_i)\log P(X = z_i)\\
 &\phantom{=}\ \ -\sum_{j=1}^n P(Y = z_j)\log P(Y = z_j) \\
 &= H(X) + H(Y)
\end{align}
:::

:::{admonition} Definition
The *mutual information* (also *transinformation*) of two random variables $X,Y$ is defined as

$$
I(X;Y) := H(X)+H(Y)-H(X,Y)= H(X,Y  \Vert X\times Y)
$$

Here $H(\cdot \Vert \cdot)$ stands for the relative entropy of the *distribution* of $(X,Y)$ with respect to the product distribution $P_X \times P_Y$, that is, the distribution $(X,Y)$ would have if $X$ and $Y$ were independent.

A very common application of mutual information is in clustering:
if we have arrived at clusters for a dataset by a method of our choice,
that is, at an estimated class membership (say $1$, $2$ or $3$ as a label),
and a classification has been carried out by hand for a subset of the data (for testing),
then we can compute the mutual information of these class variables to quantify how well the clustering worked on the test data.
The advantage here is that the concrete labels no longer matter
(that is, the method is invariant under permutation of the class names).

The *conditional entropy* of $X$ given $Y$ is defined as

$$
H(X|Y) := H(X) - I(X;Y)
$$
:::

:::{admonition} Example
The mutual information of $X$ with itself is exactly the entropy $I(X;X) = H(X)$.

If $X,Y$ are independent, then $I(X;Y) = H(X) + H(Y) - (H(X) + H(Y)) = 0$.
:::

:::{admonition} Proposition
$$
H(X|Y) = H(X,Y) - H(Y)
$$

and if $X,Y$ are independent, then $H(X|Y) = H(X)$.
:::


:::{admonition} Theorem
**Entropic Bayes' theorem**

$$
H(X|Y) = H(Y|X) + H(X) - H(Y)
$$
:::

:::{admonition} Example
If $X$ depends entirely on $Y$ (for example $Y$ a throw of a die and $X = f(Y)$ with $f = \mod 2$),
then $H(X,Y) = H(Y)$ and $H(X|Y) = 0$.
:::

```{figure} images/1920px-Entropy-mutual-information-relative-entropy-relation-diagram.svg.png
:width: 480px
:align: center
:name: entropy-diagram

Entropy, conditional entropy, joint entropy and mutual information in a Venn diagram. Figure: [Wikimedia Commons, user KonradVoelkel](https://commons.wikimedia.org/wiki/File:Entropy-mutual-information-relative-entropy-relation-diagram.svg) (2010, public domain).
```


:::{admonition} Definition
The *cross-entropy* of $X$ (distributed according to $p \in \Delta_n$) and $Y$ (distributed according to $r \in \Delta_n$) is

$$
H(X; Y) = \mathbb{E}_X I(Y) = -\sum_{i,\ p_i > 0}^n p_i \log r_i \in \mathbb{R} \cup \{\infty\}.
$$
:::

A summand with $p_i > 0$ and $r_i = 0$ has the value $\infty$ here (with $\log 0 = -\infty$): an event that is impossible under $r$ but occurs under $p$ costs infinitely much.

*Careful*: some authors unfortunately write the cross-entropy as $H(X, Y)$ as well, which is then easily confused with the joint entropy. The notation $H(X;Y)$ also resembles that of the mutual information $I(X;Y)$ above, which is something else entirely.

:::{admonition} Proposition
$$
H(X; Y) = H(X) + H(X \Vert Y)
$$
:::

If we hold $X$ fixed and vary $Y$, minimising $H(X;Y)$ and minimising $H(X \Vert Y)$ come to the same thing, which is why in machine learning one is often substituted for the other. The maximum likelihood method can be read as the minimisation of a cross-entropy, and hence as the minimisation of a relative entropy. That explains how and why entropy is relevant to machine learning.

:::{admonition} Remark
In deep learning you meet this observation under three names: *negative log-likelihood*, *cross-entropy* and *KL divergence to the labels* all refer there to the same loss function for classification problems. The difference between the last two is only the constant $H(X)$ from the proposition above, which does not depend on the model parameters. The course *Introduction to Deep Learning* takes this connection as known.
:::

Apart from that, the cross-entropy is a quantity used considerably less often in the theory than the relative entropy (which is usually called the Kullback–Leibler divergence $D_{KL}$).

## Continuous entropy

:::{note}
This section is not part of the course proper and reaches ahead to measure theory (Radon–Nikodym derivative, invariant measures), which we do not cover in this course. On a first reading it is enough to take away the core statement: in the continuous case entropy is only meaningfully defined *relative* to a reference measure, so relative entropy is the notion that is actually fundamental.
:::

One might think that the formula $H(p) = -\sum p_i \log p_i$ generalises to $H(P) = -\int \log P dP$, but like that it makes no sense. What one can do is this:

:::{admonition} Definition
Let $P$ be a continuous distribution with density function $f$ defined on a set $\Omega \subseteq \mathbb{R}^n$.
Then

$$
h(X) := \mathbb{E}\left( -\log(f(X)) \right) = - \int_\Omega f(x) \log f(x) dx
$$

is called the *differential entropy* of $X$ (likewise defined by Claude Shannon).
:::

It already has some of the pleasant properties we picture a continuous entropy having, translation invariance for instance: $h(X) = h(X - v)$ for a vector $v \in \mathbb{R}^n$.

Unfortunately the differential entropy is not invariant under arbitrary transformations, not even under isomorphisms.

Jaynes suggested picturing ever finer histograms, that is, a set of $N$ discrete points $\{x_i\}$;
we then write
$M(a,b) = \lim_{N \to \infty} \frac{1}{N} (\text{number of } x_i : a < x_i < b)$
and call a density $m$ with $M(a,b) = \int_a^b m(x) dx$ an *invariant measure*.
With that we now write

$$
\lim_{N \to \infty} \log(N) - \int p(x) \log \dfrac{p(x)}{m(x)} dx
$$

but since $\lim_{N \to \infty} \log(N) = \infty$, we cheekily drop that part, and so obtain a quantity that behaves much like $h(x)$ but is scale invariant:

$$
H(X) := - \int p(x) \log \dfrac{p(x)}{m(x)} dx
$$

The first thing to record is that the "discrete entropy" of a continuous distribution is really $\infty$.
The second is that a workable notion of entropy evidently cannot avoid referring to a further distribution (here the "invariant measure").

Analysing from a theoretical standpoint what $h(X)$ and $H(X)$ are leads to the general relative entropy $H(P,Q)$, with $h(X) = -H(f\lambda \,\Vert\, \lambda)$, where $\lambda$ is the Lebesgue measure and $f$ a density of $X$.

:::{admonition} Definition
Let $P,R$ be continuous distributions. The *relative entropy* $H(P \Vert R)$ (also: Kullback–Leibler divergence $D_{KL}(P,R)$) is

$$
H(P \Vert R) := - \int_\Omega \log \left( \dfrac{dR}{dP} \right) dP
$$

where $\dfrac{dR}{dP}$ is the Radon–Nikodym derivative of one measure with respect to another.
:::

We will not discuss that any further either, and would rather record that for $P$ and $R$ with density functions $p,r \colon \mathbb{R}^n \to [0,\infty)$ it looks simpler:

$$
H(P \Vert R) = \int_\Omega p(x) \log \frac{p(x)}{r(x)} dx
$$

This expression in turn we may evaluate (if the density functions are friendly enough) by Riemann sums.
If for instance $n=1$ and $\Omega = \mathbb{R}$, then we can look at

$H(P \Vert R) = \int_{\mathbb{R}} p(x) \log \dfrac{p(x)}{r(x)} dx$
$= \sum_{k = -\infty}^{\infty} \int_{k}^{k+1} p(x) \log \dfrac{p(x)}{r(x)}dx$

and bound the integral terms on the right by values, so as to estimate $H(P \Vert R)$.

$$
H(P \Vert R) \approx \sum_{k = -\infty}^{\infty} p(k) \log \dfrac{p(k)}{r(k)}
$$

The subdivision into intervals of length $1$ can of course be chosen as fine as we like, to make the approximation as accurate as we like. Replacing a continuous distribution by such a discrete distribution is the analogue of forming a histogram.

If you still have doubts about what relevance abstract information theory is supposed to have for the practical work of data scientists and machine learning engineers, a [trip into the Wikipedia page on applications of mutual information and conditional entropy](https://en.wikipedia.org/wiki/Mutual_information#Applications_2) is to be recommended.
