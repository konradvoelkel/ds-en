# Multivariate statistics: covariance and dependence

## Joint distribution and Bayes

:::{admonition} Definition
If $X \colon \Omega_1 \to \mathbb{R}$ and $Y \colon \Omega_2 \to \mathbb{R}$ are two random variables, we can form the **product**:

$$
X \times Y \colon \Omega_1 \times \Omega_2 \to \mathbb{R}^2,\ (a,b) \mapsto (X(a),Y(b)).
$$
:::

:::{admonition} Definition
If $X,Y \colon \Omega \to \mathbb{R}$ are two random variables with the same domain, we can form the **joint distribution**:

$$
(X, Y) := (X \times Y) \circ \Delta \colon \Omega \to \mathbb{R}^2,\ a \mapsto (X(a),Y(a)).
$$

Here $\Delta \colon \Omega \to \Omega \times \Omega$ is the *diagonal map* $a \mapsto (a,a)$.
:::

:::{admonition} Definition
For a random variable $X \colon \Omega \to \mathbb{R}^n$ we can write $X = (X_1,\dots,X_n)$ with $X_i \colon \Omega \to \mathbb{R}$ given as $\pi_i \circ X$, where $\pi_i \colon \mathbb{R}^n \to \mathbb{R}$ is the $i$-th coordinate projection.
The distributions of the $X_i$ are called the **marginal distributions**, or **margins**, of $X$.
:::

More generally, $(X_1,X_3,X_9)$ is called a marginal distribution of $X$ too, as is any composition of $X$ with a linear projection $\pi \colon \mathbb{R}^n \to \mathbb{R}^m$, not necessarily onto the coordinate (hyper)plane(s) of the standard basis of $\mathbb{R}^n$.

:::{admonition} Remark
The distribution of $X_i$ is $P(X_i \in A) = P(X \in \pi_i^{-1}(A))$.

For a random variable $(X,Y) \colon \Omega \to \mathbb{R}^2$ we can compute the distribution of $Y$ as
$P(Y \in A) = \sum_{x \in X(\Omega)} P((X,Y) \in \{x\} \times A)$ in the discrete case (and with a corresponding integral in the continuous case), where we have decomposed $\pi_2^{-1}(A) = X(\Omega)\times A$ into disjoint subsets.
:::

:::{admonition} Remark
For a random variable $(X,Y) \colon \Omega \to \mathbb{R}^2$,

$$
P((X,Y) = (x,y)) = P(X = x, Y=y) = P(Y = y | X = x)P(X = x)
$$

by the definition of conditional probability.

In the pmf notation we also write

$$
p(x,y) = p(y|x)p(x)
$$

where this is to be read as a definition:

$$
p(y|x) = \frac{p(x,y)}{p(x)}
$$

More precisely, one writes the distributions with their random variables as subscripts when several are in play:

$$
p_{X,Y}(x,y) = p_{Y|X}(y \mid x)\, p_X(x),
$$

where, for each fixed $x$ with $p_X(x) > 0$, the function $p_{Y|X}(\cdot \mid x)$ is the pmf of the conditional distribution of $Y$ (likewise in the continuous case, with densities instead of pmfs). This formula is called the **product rule**; the **sum rule** is the remark before it, the summing over the variable we are not interested in.
:::

:::{admonition} Proposition
Let $X, Y \colon \Omega \to \mathbb{R}$ be discrete random variables. Then the following are equivalent:

1. $X$ and $Y$ are independent (in the sense of the chapter [Expected value and variance](expectation-variance.md), section *Independence*);
2. the joint pmf factorises: $p_{X,Y}(x,y) = p_X(x)\, p_Y(y)$ for all $x,y$;
3. conditioning changes nothing: $p_{Y|X}(y \mid x) = p_Y(y)$ for all $x$ with $p_X(x) > 0$ and all $y$.
:::

:::{admonition} Proof
The independence of $X$ and $Y$ means $P(X = x, Y = y) = P(X = x)\,P(Y = y)$ for all $x,y$, and that is literally statement 2. For the equivalence of 2 and 3 we substitute the definition $p_{Y|X}(y \mid x) = \frac{p_{X,Y}(x,y)}{p_X(x)}$: if 2 holds, then $p_X(x) > 0$ cancels and $p_{Y|X}(y\mid x) = p_Y(y)$ is left. If conversely 3 holds, then $p_{X,Y}(x,y) = p_{Y|X}(y\mid x)\,p_X(x) = p_Y(y)\,p_X(x)$ for all $x$ with $p_X(x) > 0$; for $x$ with $p_X(x) = 0$ both sides are $0$.
:::

Statement 3 is the generalisation of $P(A \mid B) = P(A)$ from the chapter [Expected value and variance](expectation-variance.md): knowing about $X$ does not shift the distribution of $Y$. In the continuous case the same equivalence holds with densities, but only "almost everywhere" – densities are after all determined only up to null sets (see [Continuous distributions](continuous-distributions.md)).

:::{admonition} Theorem
**Bayes' theorem.**
Given two events $A,B \subseteq \Omega$,

$$
P(A|B) = \dfrac{P(B|A)P(A)}{P(B)}.
$$
:::

:::{admonition} Example
**Why the base rate matters.** A test detects a rare disease reliably: $99\,\%$ of those who have it are detected, and only $1\,\%$ of the healthy get a false positive result. Even so, after a positive test the probability of actually having the disease is small. The reason is the *base rate* $P(A)$: if only one person in a thousand is ill, then for every correctly detected ill person there are about ten falsely positive healthy ones – the small error rate of $1\,\%$ acts on a group a thousand times larger. In the language of the confusion matrix from the chapter [Titanic EDA](titanic-eda-numpy.ipynb): the test is a classifier, the $99\,\%$ are its recall (the *sensitivity*), the $1\,\%$ its false positive rate, and what we are after is its precision, the proportion of ill people among those who test positive. With $A$ = "ill" and $B$ = "test positive", Bayes' theorem works out exactly this weighting:

$$
P(A|B) = \dfrac{0.99 \cdot 0.001}{0.99 \cdot 0.001 + 0.01 \cdot 0.999} = \dfrac{0.00099}{0.00099 + 0.00999} \approx 0.09.
$$

$P(A|B)$ is precisely not $P(B|A)$, but $P(B|A)$ *times* the ratio $P(A)/P(B)$, and $P(B)$ is dominated by the large group of the healthy. Anyone who confuses the two conditional probabilities commits the *base rate fallacy* – which is common enough to have a name of its own. For the Titanic rule "women survive", recall $0.68$ and precision $0.74$ lay close together, because survivors and women are about equally frequent; here a base rate of one in a thousand lies between $0.99$ and $0.09$. (Where the denominator comes from is settled by the law of total probability below.)
:::

:::{admonition} Proof
The definition of conditional probability is
$P(A|B) = \dfrac{P(A \cap B)}{P(B)}$
and we apply it with the roles of $A$ and $B$ swapped as well.
:::

To work out the denominator $P(B)$, the following theorem often helps:

:::{admonition} Theorem
**The law of total probability.**
If $\Omega = A_1 \cup \dots \cup A_n$ is a decomposition into pairwise disjoint events with $P(A_i) > 0$, then for every event $B$

$$
P(B) = \sum_{i=1}^n P(B|A_i)\,P(A_i).
$$
:::

:::{admonition} Proof
The sets $B \cap A_i$ are pairwise disjoint and their union is $B$, so $P(B) = \sum_i P(B \cap A_i)$ (finite additivity), and by the definition of conditional probability $P(B \cap A_i) = P(B|A_i)\,P(A_i)$.
:::

In Bayes' theorem you can therefore replace the denominator by $P(B) = P(B|A)P(A) + P(B|A^c)P(A^c)$ when all you know is $A$ and its opposite.

:::{admonition} Theorem
**Bayes' theorem, version 2.**
Given two random variables $X,Y \colon \Omega \to \mathbb{R}^n$,

$$
P(X=x | Y=y) = \dfrac{ P(Y=y|X=x)P(X=x) }{P(Y=y)}.
$$
:::

We often apply this as follows: $Y$ is "known" and $X$ is the provisional model.
Here we call $Y=y$ the *data* $D$ and $X=x$ the *hypothesis* $H$.

Given data and hypothesis we thus obtain

:::{admonition} Theorem
**Bayes' theorem, version 3.**

$$
P(H|D) = \dfrac{ P(D|H) P(H) }{ P(D) }
$$

Here $P(H)$ is called the **prior** (the a priori probability of the hypothesis),
$P(D)$ the **evidence**, $P(D|H)$ the **likelihood** and $P(H|D)$ the **posterior** (the a posteriori probability of the hypothesis). A way to remember it: the likelihood answers the question "how probable are the data, supposing the hypothesis were true?".
Unlike $P(H)$, the likelihood $P(D|H)$ is at least in principle computable.
:::

:::{admonition} Example
**How to work out a likelihood.** So far $H$ and $D$ have been events with finitely many outcomes. In practice the hypothesis is usually a whole distribution. Suppose we have $n$ measurements $D = (x_1,\dots,x_n)$ and work with normal distributions: the hypothesis $H$ says that the data come from an $\mathcal{N}(\mu,\sigma^2)$ with $\mu = 0$ and $\sigma = 2$. The likelihood $P(D \mid H)$ is then the probability (density) of seeing exactly these $n$ values if the hypothesis is right – and because the measurements are meant to be independent, the joint density factorises into a product by the proposition above:

$$
P(D \mid H) = \prod_{i=1}^n p_{\mu,\sigma}(x_i) = \prod_{i=1}^n \dfrac{1}{\sqrt{2\pi}\,\sigma} \exp\left( -\dfrac{(x_i - \mu)^2}{2\sigma^2} \right) \quad \text{with } \mu = 0,\ \sigma = 2.
$$

Three roles have to be kept cleanly apart here: the *data-generating distribution*, which exists in the world and which we do not know; the *observed data* $D$, which we have; and the *model distribution*, which we declare to be the hypothesis. The likelihood compares the second with the third. If we let $\mu$ and $\sigma$ vary instead of holding them fixed, the number turns into a function $L(\mu,\sigma) := \prod_{i=1}^n p_{\mu,\sigma}(x_i)$, and looking for the parameters that maximise it is the maximum likelihood principle – see [Statistical models and estimators](statistical-models.md), where taking logarithms turns the product into a sum.
:::

:::{admonition} Theorem
**Bayes' theorem, version 4.**

$$
\text{Posterior} = \dfrac{ \text{Likelihood} \cdot \text{Prior} }{ \text{Evidence} }.
$$
:::

:::{admonition} Example
**Bayesian updating.** Today's posterior is tomorrow's prior. In the disease-test example the probability of being ill after a positive test was about $0.09$. If the test is done a second time, independently of the first, then $0.09$ is now the prior $P(H)$, the likelihood of a positive result stays $0.99$ for the ill and $0.01$ for the healthy, and the evidence is again worked out with total probability:

$$
P(H|D) = \dfrac{0.99 \cdot 0.09}{0.99 \cdot 0.09 + 0.01 \cdot 0.91} \approx 0.91.
$$

Two positive tests in a row turn one in a thousand first into nine per cent and then into ninety-one. Every new observation pushes the posterior further along, and the result depends on the first prior: start at $P(H) = 0.001$ and you need two tests; start at $0.5$ (because there are symptoms already, say) and one test puts you at $0.99$. This process is called *Bayesian updating*; the chapter [Statistical models](statistical-models.md) turns the likelihood into a general estimation procedure.
:::

## Covariance

First a warning we already know from the chapter [Descriptive statistics](descriptive-statistics.md): covariance and correlation measure a relationship across *all* the data points. If the data fall apart into groups, the relationship inside each group can carry the opposite sign – see [Simpson's paradox](descriptive-statistics.md). So the numbers in this chapter only tell you something once you know that the sample comes from a single population.

:::{admonition} Definition
Given two random variables $X,Y \colon \Omega \to \mathbb{R}$, the **covariance**
is defined as

$$
\operatorname{Cov}(X,Y) := \mathbb{E}\left( \left( X - \mathbb{E}X \right) \left( Y - \mathbb{E}Y \right) \right).
$$
:::

In particular, $\mathbb{V}(X) = \operatorname{Cov}(X,X)$.

The covariance suffers from the same complaint as the variance: it depends on the scale. The cure is to normalise by the standard deviations:

:::{admonition} Definition
The (Pearson) **correlation coefficient** is

$$
\rho(X,Y) := \dfrac{\operatorname{Cov}(X,Y)}{\sigma(X)\sigma(Y)}.
$$

Clearly $\rho(X,Y)=0$ exactly when $\operatorname{Cov}(X,Y)=0$.

One says that $X$ and $Y$ are **positively correlated** if $\rho(X,Y) > 0$,
**negatively correlated** (or anticorrelated) if $\rho(X,Y) < 0$,
and **uncorrelated** if $\rho(X,Y)=0$.
:::

:::{admonition} Remark
**For data.** If $x, y \in \mathbb{R}^n$ are given as two columns of a table, you replace the expected value in the definitions by the mean and obtain the *empirical covariance* and the *empirical correlation coefficient*

$$
\operatorname{Cov}(x,y) := \frac{1}{n} \sum_{i=1}^n (x_i - \bar x)(y_i - \bar y) = \frac{1}{n}\, \tilde x \cdot \tilde y, \qquad r := \frac{\operatorname{Cov}(x,y)}{\sigma(x)\,\sigma(y)} = \frac{\tilde x \cdot \tilde y}{\lVert \tilde x \rVert \, \lVert \tilde y \rVert},
$$

with the centred vectors $\tilde x, \tilde y$ from the chapter [Expected value and variance](expectation-variance.md). The correlation coefficient of data is thus literally the cosine of the angle between the centred columns. It is the number that `np.corrcoef(x, y)[0, 1]` prints in the chapter [Titanic EDA](titanic-eda-numpy.ipynb); `np.cov(x, y, ddof=0)` gives the covariance matrix in the $n$-version (without `ddof=0` Numpy divides by $n-1$ here, unlike `np.var`). For the Iris exercise from the chapter [Descriptive statistics](descriptive-statistics.md) you compute once across all the rows and once per species:

```python
x = datasets.load_iris().data; y = datasets.load_iris().target
print(np.corrcoef(x[:, 0], x[:, 1])[0, 1])                          # -0.118
for s in range(3):
    print(s, np.corrcoef(x[y == s, 0], x[y == s, 1])[0, 1])         # 0.743, 0.526, 0.457
```
:::

:::{admonition} Proposition
The covariance is symmetric: $\operatorname{Cov}(X,Y) = \operatorname{Cov}(Y,X)$

The covariance is bilinear: $\operatorname{Cov}(aX+bY, Z) = a\operatorname{Cov}(X,Z) + b\operatorname{Cov}(Y,Z)$ for $a,b \in \mathbb{R}$.

The covariance is positive (semi)definite: $\operatorname{Cov}(X,X) = \mathbb{V}(X) \geq 0$, and $\operatorname{Cov}(X,X) = 0$ holds exactly when $X$ is almost surely constant.
:::

:::{admonition} Proof
Symmetry and semidefiniteness can be read straight off the definition ($\operatorname{Cov}(X,X) = \mathbb{E}((X-\mathbb{E}X)^2) \geq 0$). For bilinearity, $aX + bY - \mathbb{E}(aX+bY) = a(X - \mathbb{E}X) + b(Y - \mathbb{E}Y)$ by linearity of the expected value; multiplying out with $(Z - \mathbb{E}Z)$ and using linearity once more gives the claim. For the case of equality: $\mathbb{E}((X-\mathbb{E}X)^2) = 0$ means that the non-negative random variable $(X-\mathbb{E}X)^2$ has expected value $0$, and so is almost surely $0$.
:::

Symmetry and bilinearity give us the rules of calculation that are needed constantly in practice:

:::{admonition} Proposition
**Rules of calculation for the covariance.** For random variables $X, Y$ and a constant $\beta \in \mathbb{R}$,

1. $\mathbb{V}(X+Y) = \mathbb{V}(X) + \mathbb{V}(Y) + 2\operatorname{Cov}(X,Y)$,
2. $\operatorname{Cov}(X, \beta) = 0$,
3. $\operatorname{Cov}(X+\beta, Y) = \operatorname{Cov}(X,Y)$,
4. $\operatorname{Cov}(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X)\,\mathbb{E}(Y)$.
:::

:::{admonition} Proof
(1) $\mathbb{V}(X+Y) = \operatorname{Cov}(X+Y, X+Y) = \operatorname{Cov}(X,X) + \operatorname{Cov}(X,Y) + \operatorname{Cov}(Y,X) + \operatorname{Cov}(Y,Y)$ by bilinearity, and the two middle terms are equal by symmetry.
(2) The constant random variable $\beta$ has expected value $\beta$, so $\beta - \mathbb{E}\beta = 0$ and $\operatorname{Cov}(X,\beta) = \mathbb{E}((X - \mathbb{E}X) \cdot 0) = 0$.
(3) Bilinearity and (2): $\operatorname{Cov}(X+\beta, Y) = \operatorname{Cov}(X,Y) + \operatorname{Cov}(\beta, Y) = \operatorname{Cov}(X,Y)$.
(4) Multiplying out the definition, and linearity of the expected value:

$$
\mathbb{E}\big(XY - X\,\mathbb{E}Y - Y\,\mathbb{E}X + \mathbb{E}X\,\mathbb{E}Y\big) = \mathbb{E}(XY) - 2\,\mathbb{E}X\,\mathbb{E}Y + \mathbb{E}X\,\mathbb{E}Y = \mathbb{E}(XY) - \mathbb{E}X\,\mathbb{E}Y.
$$

Rule (4) is the counterpart of the formula $\mathbb{V}(X) = \mathbb{E}(X^2) - (\mathbb{E}X)^2$ from the chapter [Expected value and variance](expectation-variance.md); for $X = Y$ the two coincide. From (1) it also follows that $\mathbb{V}(X_1 + \dots + X_n) = \sum_i \mathbb{V}(X_i)$ as soon as the $X_i$ are pairwise uncorrelated.
:::

:::{admonition} Theorem
**Independent random variables are uncorrelated.** If $X$ and $Y$ are independent (in the sense of the chapter [Expected value and variance](expectation-variance.md), section Independence) and have finite variance, then $\mathbb{E}(XY) = \mathbb{E}(X)\,\mathbb{E}(Y)$ and hence $\operatorname{Cov}(X,Y) = 0$.
:::

:::{admonition} Proof
In the discrete case the joint pmf is a product, because of the independence, $p(x,y) = p_X(x)\,p_Y(y)$, and the double sum splits:

$$
\mathbb{E}(XY) = \sum_{x}\sum_{y} x\,y\,p_X(x)\,p_Y(y) = \Big(\sum_x x\,p_X(x)\Big)\Big(\sum_y y\,p_Y(y)\Big) = \mathbb{E}(X)\,\mathbb{E}(Y).
$$

In the continuous case the sums are replaced by integrals over the joint density $p(x,y) = p_X(x)\,p_Y(y)$ (joint densities we introduce in the next chapter); the calculation is the same. With rule (4) it follows that $\operatorname{Cov}(X,Y) = \mathbb{E}(XY) - \mathbb{E}X\,\mathbb{E}Y = 0$.
:::

:::{admonition} Remark
The converse does not hold: uncorrelated random variables can be dependent. An example is $X$ uniformly distributed on $[-1,1]$ and $Y = X^2$: then $\mathbb{E}(XY) = \mathbb{E}(X^3) = 0 = \mathbb{E}X\,\mathbb{E}Y$, so $\operatorname{Cov}(X,Y) = 0$, and yet $Y$ is a function of $X$. The covariance measures *linear* relationships only. For jointly normally distributed $(X,Y)$, on the other hand, the converse does hold, as we shall see in the next chapter.
:::

The covariance therefore behaves like an inner product – but only "modulo constants", since constant random variables have covariance $0$ with everything, themselves included. This can be made rigorous, reading the covariance as an inner product on an $\mathcal{L}^2$ space of random variables in which two random variables that differ only by a constant are identified. The correlation coefficient then plays the role of the cosine of the angle between two random variables. For data it is literally that (see the remark *For data* above); the "cosine similarity" widespread in machine learning is the same cosine, just without the centring.

You can get some practice at "seeing" the correlation coefficient in a scatter plot of two variables,
for instance with the game ["Guess the Correlation" by Omar Wagih](https://www.guessthecorrelation.com).

```{figure} images/normalmarginal.png
:width: 480px
:align: center
:name: bivariate-randhistogramme

A sample from a bivariate normal distribution, with the two marginal histograms.
```

The picture shows why the correlation cannot be read off the individual variables. Each of the two marginal histograms is an unremarkable bell curve; they would look exactly the same if the correlation had the opposite sign, or if it were $0$, because the marginal distributions do not depend on it. The relationship becomes visible only in the joint scatter plot, in the tilt of the cloud of points. This is the same observation as the one above about the joint distribution: the joint distribution cannot be reconstructed from the individual ones.

What covariance and correlation mean geometrically we will see in the next chapter, with the multivariate normal distribution: there the covariance matrix describes the shape and position of the ellipses that are the contour lines of the density.
