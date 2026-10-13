# Statistical models and estimators

In the data science process, the road from the data to a product (be it a report, a prediction or new and interesting data), we model the data. Strictly speaking we model partial aspects, sections of the data (just as the data themselves are only a section of reality).
In doing so we may be interested in how the data came about, but we may equally be driven by the wish to be able to say something particular about them, or to do something particular with them. So it helps to be clear about what kind of information one wants to coax out of the data, and then to tune the models to that.
Often several approaches are available for computing the same kind of information. The results may well differ, and frequently (in unsupervised learning) we cannot compare the computed results with the "right" result. All that is left then is to compare the information content of the models (to compute the entropy), to examine every model assumption for plausibility, and to develop general criteria for the quality of models. The last of these is what we now set about.

The classical approach – classical in the sense of historically oldest – begins by formalising the models and the aspects one wants to compute from the data with them.
One speaks of a **statistical model**, of a **statistic**, and of various **estimators** for a statistic which can then be compared with one another. One criterion is whether an estimator lands near the "right" result at least for very large samples. But hold on – if we do not know the right result, how can we say anything of the sort?

The solution is to restrict ourselves to those statistical models in which we can describe the rough structure of the right result for an estimator well enough that statements such as "in the limit this estimator estimates the expected value of that statistic on the data" become available after all. And then one can talk about how good the values look away from the limit, for somewhat smaller samples. Along the way we meet a notion that matters a great deal to data science and machine learning: the **maximum likelihood** principle.

A very concrete example first. Given data that come as a vector $x$ of length $n$ of real numbers ($\texttt{float}$), of which we know that they arose as a sample of a one-dimensional normally distributed random variable $X$ with expected value $\mu(X)$ and variance $\sigma^2(X)$, we want to estimate the standard deviation $\sigma(X)$. For this the books offer two different formulas, $\sigma(x)$ and $\sigma^\ast(x)$, which differ only in their denominator:

$$
\sigma(x)^2 = \dfrac{1}{n} \sum_{i=1}^n (x_i-\mu)^2,\qquad \sigma^\ast(x)^2 = \dfrac{1}{n-1} \sum_{i=1}^n (x_i-\mu)^2
$$

Quite concretely, for a sample of $n = 48$ values that really were drawn from a normal distribution:

```python
import numpy as np

x = np.array([6.5281, 3.8003, 4.9575, 7.4818, 6.7351, 1.0454, 4.9002, 2.6973,
              2.7936, 3.8212, 3.2881, 5.9085, 4.5221, 3.2434, 3.8877, 3.6673,
              5.9882, 2.5897, 3.6261, 1.2918, -2.1060, 4.3072, 4.7289, 1.5157,
              7.5395, 0.0913, 3.0915, 2.6256, 6.0656, 5.9387, 3.3099, 3.7563,
              1.2244, -0.9616, 2.3042, 3.3127, 5.4606, 5.4048, 2.2253, 2.3954,
              0.9029, 0.1600, -0.4125, 6.9016, 1.9807, 2.1239, 0.4944, 4.5550])

print(np.mean(x))            # 3.3689...
print(np.var(x))             # 5.0037...  denominator n
print(np.var(x, ddof=1))     # 5.1102...  denominator n-1
print(np.std(x))             # 2.2369...
print(np.std(x, ddof=1))     # 2.2606...
```

So the two formulas deliver noticeably different numbers – a good two per cent apart in the variance, and that at $n = 48$. Which is the right one? And in passing: that we may replace $\mu(X)$ by $\texttt{mean}(x)$ at all is something we have so far only taken to be plausible; the justification is the example "the sample mean is unbiased" in the section *Unbiasedness* below.

With these formulas one has to be a little careful when implementing them in practice – because what is $\mu$?
In an application I do not know $\mu(X)$ and must therefore use $\mu(x)$. But then it turns out that the information in $\{x_i-\mu(x)\}_{i=1}^{n-1}$ suffices to compute $x_n - \mu(x)$, since by the definition of $\mu(x)$ we have $x_n - \mu(x) = \sum_{i=1}^{n-1} (\mu(x) - x_i)$. In a sense, then, using $\mu(x)$ in place of $\mu(X)$ leaves us one degree of freedom fewer than $n$. We shall see in a moment how that affects the properties of these two estimators for $\sigma(X)$.

Once statistical models have been defined formally, one can also talk very well about confidence intervals and hypothesis tests, which is what the chapter [Statistical tests](statistical-tests.md) does. Confidence intervals extend the bare estimation of a statistic by the information on what margin of error one attaches to that estimate. Hypothesis tests extend it by arriving at decisions in the end. In discussing hypothesis tests it is unavoidable to speak also about the problematic notion of **significance**. But one thing at a time!

As a map for the definitions that follow – on the left what one talks about, on the right what it formally becomes:

| in everyday terms | formally |
|---|---|
| a family of distributions from which we want to pick one | **statistical model** $(\mathcal{X}, P_\theta : \theta \in \Theta)$ |
| the quantity we want to estimate (say $\mu$ or $\sigma$) | map $\tau \colon \Theta \to \Sigma$ |
| the sample we are holding in our hands | an element $x \in \mathcal{X}$ – or, as long as it has not been drawn yet, a random variable with values in $\mathcal{X}$ |
| the procedure that turns the sample into a number | **statistic**, or **estimator**, $T \colon \mathcal{X} \to \Sigma$ |

The sample space $\mathcal{X}$ here is not the space of a single measured value but the space of all samples: with $n$ real measurements $\mathcal{X} = \mathbb{R}^n$, so a sample is a single point in a fairly large space.

The crucial move is in the last row. Because the sample is a random variable and the estimation procedure is a map on it, the result of estimating is again a random variable. That lets us speak of its expected value and its variance – and that is exactly what we need in order to be able to say at all what a *good* estimator is: bias, consistency and mean squared error are all formulated in this language.

## Statistical models

:::{admonition} Definition
A statistical model is a triple $(\mathcal{X}, \mathcal{F}, P_\theta : \theta \in \Theta)$
consisting of a **sample space** $\mathcal{X}$, a $\sigma$-algebra $\mathcal{F}$ on $\mathcal{X}$ and a class $\{P_\theta\}_{\theta \in \Theta}$ of probability measures on $(\mathcal{X}, \mathcal{F})$ that contains at least two elements, that is $|\Theta| > 1$.
We often simply write $(\mathcal{X}, P_\theta : \theta \in \Theta)$.
:::

:::{admonition} Remark
A statistical model is therefore not yet the 'finished model' with which we want to classify or make predictions in the data science sense, but a whole class of models parametrised by the set $\Theta$. This set $\Theta$ may be as wild as you like; it should only have at least two elements, so that in the case $\Theta = \{\theta\}$ the notion does not shrink to 'the sample space with one probability measure on it'.
When speaking of expected values (and hence, say, of variances) in the context of a statistical model, one has to be careful, and it is best to carry the $\theta$ along in the notation: $\mathbb{E}_\theta(Y)$ for the expected value of a random variable $Y : \mathcal{X} \to \mathbb{R}$, because that value depends on $\theta$.
:::

:::{admonition} Definition
A statistical model is called a **parametric model** if the parameter set $\Theta$ is a subset of some $\mathbb{R}^d$ for a $d \in \mathbb{N}$. For $d=1$ one also says **one-parameter model**.

If the sample space $\mathcal{X}$ is discrete (at most countable) and $\mathcal{F} = \mathcal{P}(\mathcal{X})$, the model is called **discrete**, and in that case every $P_\theta$ has a discrete density $p_\theta$, that is $p_\theta(x) = P_\theta(\{x\})$.

If the sample space $\mathcal{X}$ is a (Borel) measurable subset of $\mathbb{R}^n$ (an open set, say, or the level set of a continuous function), if $\mathcal{F}$ is a restriction of the Borel $\sigma$-algebra of $\mathbb{R}^n$, and if moreover every $P_\theta$ has a density function $f_\theta$, then the statistical model is called a **continuous model**.

A statistical model that is either discrete or continuous is also called a **standard model**.
:::

:::{admonition} Remark
To a first approximation we can picture the sample space as the set of possible outcomes at sample size $1$ (the population $\Omega$ sends its regards). But: one can also relabel the repeated running of an experiment as really-one-experiment, call a sequence of individual outcomes a single outcome, and so model sample sizes greater than $1$. For every statistical model the **product model** can be constructed:

$$
(\mathcal{X}^N, \mathcal{F}^{\otimes N}, P_{\theta}^{\otimes N} : \theta \in \Theta).
$$

The projections $X_i \colon \mathcal{X}^N \to \mathcal{X}$ are then independent, identically distributed random variables with respect to every distribution $P_\theta$. The notation $\mathcal{F}^{\otimes N}$ denotes the obvious way of defining a $\sigma$-algebra on $\mathcal{X}^N$ (you may ignore it, as usual), and $P_\theta^{\otimes N}$ assigns to an event in $\mathcal{X}^N$ of the form $A_1 \times \cdots \times A_N$ the product $\prod_{i=1}^N P_\theta(A_i)$. With that the $N$-fold repetition is modelled.
:::

:::{admonition} Example
We model the throw of a potentially unfair die with a discrete model: $\mathcal{X} = \{1,\dots,6\}$ and $\Theta = \Delta_6$, the set of all possible discrete distributions on a six-element set (written as probability vectors in $\mathbb{R}^6$), with $P_\theta(k) = \theta_k$. Concretely, for $\theta = (\theta_1,\dots,\theta_6)$ the probability of throwing a $6$ in the model with parameter $\theta$ is given by $P_\theta(6) = \theta_6$.
:::

:::{admonition} Example
The twice-repeated throw of the die we therefore model with $\mathcal{X}^2$ (outcomes are pairs of numbers of pips) and $\Theta = \Delta_6$ (since the second throw is to be modelled as identically distributed to the first). Here $P_\theta^{\otimes 2}(5,6) = P_\theta(5)P_\theta(6) = \theta_5\theta_6$, as one expects of independent events.
:::

:::{admonition} Example
We can also model whether the two throws came up as doubles or not – and so take $\mathcal{X} = \{\text{doubles}, \text{no doubles}\}$ as the sample space.
Here we can simply keep the parameter space $\Theta = \Delta_6$; that is one possible statistical model.
We do see, though, that $P_\theta^{\otimes 2}(k,k) = \theta_k^2$, so that $P_\theta(\text{doubles}) = \sum_{k=1}^6 \theta_k^2$,
and hence the parameter $s = \sum_{k=1}^6 \theta_k^2$ really suffices and we could imagine a smaller parameter space.
But then the question arises which distribution $P_s$ we want to assign to the parameter $s$. One concretely sensible choice is the distribution $\theta$ with maximal entropy, that is, a distribution as close to the uniform distribution as possible. This does not become unique, because permutations of $\{1,\dots,6\}$ change neither the parameter $s$ nor the entropy $H(\theta)$. If one nevertheless wants to pick a model that is canonical in some way, one can for instance demand an ordering on the $\theta$, that is $\theta_k \geq \theta_{k+1}$.
So we see here: a 'too large' parameter space is sometimes the simpler model.
:::

:::{admonition} Example
Imagine this. We have found some data $x$ in the wild (read: on the web), now believe that all instances $x_i$ are samples of a random variable $X$ with values in $\Omega$,
and so model with $\mathcal{X} = \Omega^n$.
If we notice that the values of $x$ are `float`s of some kind, we can look at the histogram. Perhaps we do not get much out of it and cannot really tell whether $X$ is a variable uniformly distributed on $[-1,1]$, or a normal distribution centred at $0$, or even an exponential distribution. In reality that could happen, for instance, when $n$ is very small. The parameter space would then be

$$
\Theta = \{\text{uni}\} \times \{0\} \cup \{\text{norm}\} \times \{\sigma > 0\} \cup \{\text{exp}\} \times \{\lambda > 0\}.
$$

The first component of $\Theta$ is the type of the distribution, $\{\text{uni, norm, exp}\}$, the second then a possible parameter. Such a model is not a parametric model! We can, though, make one out of it in an unnatural way, by encoding the categorical variable $\{\text{uni, norm, exp}\}$ as the numbers $\{1,2,3\}$ and thus representing $\Theta$ as a subset of $\mathbb{R}^2$.
:::

:::{admonition} Example
$\mathcal{X}=\mathbb{R}^N$ with $\Theta = \mathbb{R} \times \mathbb{R}_{> 0}$ and $P_{\theta}^{\otimes N} = P_{\mu,\sigma}^{\otimes N}$ a univariate normal distribution is the standard model of a sample of size $N$ of a univariate random variable that is normally distributed.
:::

:::{admonition} Definition
Let $(\mathcal{X}, P_\theta : \theta \in \Theta)$ be a statistical model and $\Sigma$ a further event space (that is, a set $\Sigma$ with a $\sigma$-algebra defined on it). Then any random variable $S \colon \mathcal{X} \to \Sigma$ is called a **statistic** of the statistical model.
:::

:::{admonition} Remark
As with the notion of a random variable itself, the question arises why we introduce a new name, given that a statistic is nothing but a random variable, which in turn is nothing but a measurable map – in the discrete case, then, statistic = random variable = map.
We have seen very plainly by now that we handle random variables differently from maps we call maps. It is exactly the same with a statistic: we use a random variable differently when we use this word for it. It is like an API wrapper around the same data structure, so that one can more easily do different things with it without mixing them up. Just think how `String`s and `float`s are also, in a way, nothing but an API wrapper around bit strings. It works so well that we want to do it again straight away!
:::

## Estimators

:::{admonition} Definition
Let $(\mathcal{X}, P_\theta : \theta \in \Theta)$ be a statistical model and $\Sigma$ a further event space.
Let $\tau \colon \Theta \to \Sigma$ be an arbitrary map that assigns to every $\theta \in \Theta$ a characteristic quantity $\tau(\theta) \in \Sigma$.
Then we call every statistic $T \colon \mathcal{X} \to \Sigma$ an **estimator** (also a **point estimator**) for $\tau$.
:::

:::{admonition} Remark
Nobody said that $T$ has to be a sensible, good estimator – in fact $T$ need have nothing to do with $\tau$ at first, beyond domain and range having to fit the statistical model and $\tau$ respectively. That gives us the flexibility to compare good estimators with miserable ones. The identity is of course admissible as $\tau$, that is $\tau = id \colon \Theta \to \Theta$, $\tau(\theta)=\theta$, and the estimators for $\tau$ under consideration are then estimators of the parameter $\theta \in \Theta$.
:::

:::{admonition} Example
In the standard model of a univariate normal distribution with sample size $N$, the projection $\Theta \to \mathbb{R}$ onto the first component, that is onto the expected value $\mu$, is a map $\tau$ whose estimators interest us.
One possible estimator is the statistic $c \colon \mathbb{R}^N \to \mathbb{R}$ that is constantly $0$ (a very conservative estimate).
Another possible estimator is the arithmetic mean $\texttt{mean} \colon \mathbb{R}^N \to \mathbb{R}$, for which it really does hold that $\texttt{mean}(x)$ comes arbitrarily close to $\mu(X)$ for large $N$, where $X$ is the normally distributed random variable that was sampled.
:::

:::{admonition} Example
In most statistical models we can consider the map $\sigma \colon \Theta \to \mathbb{R}_{\geq 0}$ that assigns to a parameter $\theta$ the standard deviation $\sigma(P_\theta)$ of the distribution $P_\theta$ (it only fails when the second moment does not exist, that is when $\mathbb{V}(P_\theta)=\infty$ occurs). For it we know the two estimators $\sigma,\ \sigma^\ast \colon \mathcal{X} \to \mathbb{R}_{\geq 0}$. The two are related by $\sigma^\ast(x) = \sqrt{\frac{n}{n-1}}\,\sigma(x)$, equivalently $\sigma^\ast(x)^2 = \frac{n}{n-1}\,\sigma(x)^2$; this factor is called the **Bessel correction** (cf. [Descriptive statistics](descriptive-statistics.md)). Which of the two estimators is the better one is settled by the next section.
:::

### Unbiasedness

:::{admonition} Definition
An estimator $T \colon \mathcal{X} \to \Sigma$ for $\tau \colon \Theta \to \Sigma$ is called **unbiased** if $\mathbb{E}_{\theta}( T ) = \tau(\theta)$ holds for all $\theta \in \Theta$. If it does not, the estimator is called **biased**, and the difference is the **bias** $\mathbb{B}_\theta(T) := \mathbb{E}_{\theta}( T ) - \tau(\theta)$.

The **mean squared error** of the estimator against the value to be estimated is

$$
\texttt{mse}(T,\theta) := \mathbb{E}_\theta\left ( (T-\tau(\theta))^2 \right ) = \mathbb{V}_\theta(T) + (\mathbb{B}_\theta(T))^2
$$

A sequence of estimators $T_n \colon \mathcal{X}^n \to \Sigma$ for $\tau$ in $n$-fold product models is called **consistent** if for $n\to\infty$
the estimator converges to $\tau$ in probability: $T_n \xrightarrow{P_\theta} \tau(\theta)$. Convergence in probability means $\forall \epsilon > 0 : \lim_{n\to\infty} P(|T_n - \tau(\theta)| > \epsilon) = 0$.

The sequence $T_n$ is called **asymptotically unbiased** if $\lim_{n\to\infty} \mathbb{E}_{\theta}(T_n) = \tau(\theta)$.
:::

:::{admonition} Example
In the standard model of an $N$-fold repeated univariate normal distribution, the sample mean $\texttt{mean}$ is an unbiased estimator for the parameter $\mu$.
:::

:::{admonition} Example
For the variance the estimator $\sigma_N^2 = \frac{1}{N} \sum_{i=1}^N (X_i - \texttt{mean}(X_j))^2$ is not unbiased, since $\mathbb{E}(\sigma_N^2) = \frac{N-1}{N}\sigma^2(X)$. The bias is therefore $-\frac{\sigma^2(X)}{N}$, which vanishes as $N\to\infty$. So the estimator is asymptotically unbiased.

The estimator adjusted by the *Bessel correction*, $\frac{N}{N-1} \sigma_N^2 = \frac{1}{N-1} \sum_{i=1}^N (X_i - \texttt{mean}(X_j))^2$, is unbiased. So we say: $\sigma_N^2$ is asymptotically unbiased, the corrected estimator even unbiased (free of bias).

The bias arises solely from the fact that $\mu$ is estimated along with everything else. If the expected value $\mu(X)$ is known, then already

$$
\dfrac{1}{N} \sum_{i=1}^N {\left(X_i - \mu(X)\right)}^2
$$

is unbiased, since $\mathbb{E}\left((X_i-\mu(X))^2\right) = \sigma^2(X)$ holds for each individual $i$ and the expected value is linear. Only putting $\texttt{mean}(x)$ in place of $\mu(X)$ costs the degree of freedom that the introduction to this chapter spoke of – and it is exactly that one degree of freedom which the factor $\frac{N}{N-1}$ wins back.
:::

:::{admonition} Definition
An estimator $S$ with finite variance that is unbiased for a function $\tau \colon \Theta \to \mathbb{R}$ to be estimated is called a **uniformly best unbiased estimator** for $\tau$ if for every further unbiased estimator $T$ for $\tau$ with finite variance and for all $\theta \in \Theta$:
$\mathbb{V}_\theta(S) \leq \mathbb{V}_\theta(T)$
:::

Such an estimator therefore has the smallest spread around the value to be estimated among all unbiased estimators.

:::{note}
**Looking ahead (not part of the course proper):** the Cramér–Rao inequality and the Fisher information in this section are background for why best estimators can exist at all. They are not needed in the course in order to use the results.
:::

In general it is very hard to determine uniformly best unbiased estimators (in general there are none). Looking ahead: the *Cramér–Rao inequality* for *regular* statistical models bounds the variance of an estimator from below by the *Fisher information* (a quantity that can also be computed from the relative entropy), and so lets us recognise uniformly best estimators by the fact that they do not exceed this variance bound. For an unbiased estimator $T$ of a real parameter $\theta$ it reads

$$
\mathbb{V}_\theta(T) \geq \frac{1}{I(\theta)}, \qquad I(\theta) := \mathbb{E}_\theta\left[\left(\frac{\partial}{\partial\theta} \log p_\theta(X)\right)^2\right],
$$

where $I(\theta)$ is the *Fisher information*. An unbiased estimator that attains this bound is therefore a uniformly best estimator. For distributions from a so-called *exponential family* (in a certain sense a common generalisation of the normal distribution, the binomial distribution, the gamma distribution and so on), the uniformly best estimators can be described directly in this way.

For many models that matter in practice, though, there is no closed formula for a good estimator at all – the [contaminated normal distribution](important-continuous-distributions.ipynb) is the example that still awaits us in the course. What one needs then is a principle that yields, instead of a formula, an optimisation problem whose solution can be approximated numerically. That is exactly what the maximum likelihood principle does, and the iterative procedure that goes with it is the [EM algorithm](expectation-maximization.ipynb).


### Maximum likelihood

:::{admonition} Definition
Given a statistical standard model $(\mathcal{X}, P_\theta : \theta \in \Theta)$ with density $f_\theta$ for $P_\theta$, the map $\rho \colon \mathcal{X} \times \Theta \to \mathbb{R}_{\geq 0}$ with $\rho(x, \theta) := L_x(\theta) := f_\theta(x)$ is called the **likelihood function**, and for fixed $x$ the map $L_x =\rho(x, \cdot) \colon \Theta \to \mathbb{R}_{\geq 0}$ is called the **likelihood** function for the observed value $x$.
:::

So if we are given data $x$, the likelihood function for $x$ expresses, for every parameter $\theta$, how the probability density of $P_\theta$ comes out at the point $x$. If the density is large, then $x$ is an observation that is probable under the parameter $\theta$. If the density is small, then $x$ is improbable under $\theta$. As a reminder: if we take the hypothesis $H = ( \theta$ is the true parameter $)$ and write $D=x$ (for data), then $P(D|H) = L_x(\theta) = f_\theta(x)$ is the likelihood (cf. Bayes' theorem, version 3, in the chapter [Covariance and dependence](covariance.md)).

:::{admonition} Definition
An estimator $T \colon \mathcal{X} \to \Theta$ for the parameter $\theta$ is called a **maximum likelihood estimator** (MLE) if for all $x \in \mathcal{X}$:

$$
L_x(T(x)) = \max_{\theta \in \Theta} L_x(\theta),
$$

that is, if $T(x)$ maximises the likelihood of $x$, and does so for every $x$. One also writes this as

$$
T(x) = \operatorname*{argmax}_{\theta \in \Theta} L_x(\theta).
$$
:::

We have already worked out a first example of this without using the name: in the chapter
[The most important discrete distributions](important-discrete-distributions.ipynb) we determined, for $k$ successes
in $n$ trials, the $p$ under which that observation is most probable, and obtained
$\hat p = \frac{k}{n}$. In the language of this chapter that is the maximum likelihood estimator
in the binomial model $\mathcal{X} = \{0,\dots,n\}$, $\Theta = [0,1]$, $P_p = \operatorname{Bin}(n,p)$.

:::{admonition} Example
In the $N$-fold univariate normally distributed model, $x \mapsto (\texttt{mean}(x), \sigma(x))$ is a maximum likelihood estimator for the parameter $(\mu(X), \sigma(X))$. The estimator $\sigma^\ast$, on the other hand, is not a maximum likelihood estimator for $\sigma(X)$. So unbiasedness and the maximum likelihood principle can rule each other out.
:::

:::{admonition} Remark
With the help of the relative entropy one can prove that under weak assumptions ($\Theta$ an interval, the $P_\theta$ pairwise distinct, and a somewhat technical condition) a sequence of maximum likelihood estimators is always consistent.

That means: if one estimates a distribution so that the probability of the observation under the estimated distribution is maximal (the maximum likelihood principle), then the estimate converges in probability to the actual distribution (as the sample size grows).
:::

:::{admonition} Remark
So for a family of distributions $P_\theta$ with densities $f_\theta$ we are interested in maximising the likelihood $f_\theta(x)$ of an observation $x$ in $\theta$. To maximise functions we like to look at the derivative (for which $f$ should be differentiable in $\theta$). Already in the example of the univariate normal density $\phi_{\mu,\sigma}$ we see that the derivative $\frac{d}{d\mu} \phi_{\mu,\sigma}(x) =\frac{(x-\mu)}{\sigma^2} \phi_{\mu,\sigma}(x)$ vanishes at $x=\mu$. So $\hat\mu = x$ is the maximum likelihood estimator for $\mu$ for a sample of size $1$ – which one believes without any calculation: if you observe exactly one value, the normal distribution under which that value is most probable is the one whose expected value sits at exactly that point. That this is a maximum and not a minimum can be seen from the fact that $\phi_{\mu,\sigma}(x)$ tends to $0$ as $\mu \to \pm\infty$.
In general, though, the likelihood is harder to compute (think of an $n$-fold product model!), and one can help oneself with a simple trick:
:::

**Trick**

Instead of maximising the likelihood of $x$ over all possible $\theta$, one can also take the logarithm of the likelihood, the so-called **log-likelihood** $\log \rho(x,\theta)$, and maximise that. Because the logarithm is strictly increasing, likelihood and log-likelihood attain their maxima in the same places.

If, for instance, $\rho$ has the form $e^{A}e^{B}$ (as in a $2$-fold product model), then $\log\rho$ has the form $A+B$ and setting derivatives to $0$ becomes a great deal easier. Even with this trick, however, no closed analytic solution can be found in general – which is where computer science gets to shine with approximation algorithms, such as the *expectation maximization algorithm*, which we take up later in the course.

:::{admonition} Example
**Maximum likelihood for the exponential distribution.**
We observe $n$ independent waiting times $x_1,\dots,x_n \geq 0$ and model them as
$\operatorname{Exp}(\lambda)$-distributed, with density $f_\lambda(x) = \lambda e^{-\lambda x}$.
Because of the independence the likelihood is the product of the individual densities:

$$
L(\lambda) = \prod_{i=1}^n \lambda e^{-\lambda x_i} = \lambda^n e^{-\lambda \sum_{i=1}^n x_i}.
$$

Here the trick pays off at once – the product turns into a sum:

$$
\ell(\lambda) := \log L(\lambda) = n\log\lambda - \lambda \sum_{i=1}^n x_i.
$$

Differentiating and setting equal to $0$ gives

$$
\ell'(\lambda) = \frac{n}{\lambda} - \sum_{i=1}^n x_i \overset{!}{=} 0
\qquad\Longleftrightarrow\qquad
\hat\lambda = \frac{n}{\sum_{i=1}^n x_i} = \frac{1}{\texttt{mean}(x)}.
$$

Since $\ell''(\lambda) = -\frac{n}{\lambda^2} < 0$, this really is a maximum.
The result is intuitive again: the exponential distribution has expected value
$\frac{1}{\lambda}$, so we estimate $\frac{1}{\lambda}$ by the sample mean.
For the observations $1, 2, 3, 4$, say, $\texttt{mean}(x) = 2.5$ and hence $\hat\lambda = 0.4$.
:::

:::{admonition} Proposition
If $\theta_0$ is the 'true' parameter for $X$ (the one $x$ was sampled with), then the maximum likelihood estimate $\hat{\theta}$ for a sample of size $n$ converges to the value $\theta$ for which the relative entropy between $P_{\theta_0}$ and $P_{\theta}$ is minimised (if the model is set up well, that minimum is exactly $0$). To see this, one uses the trick just mentioned together with the law of large numbers and the fact that the expected value of the log-likelihood equals the negative cross-entropy $-H(P_{\theta_0}; P_\theta)$.
:::

:::{admonition} Example
**An application: server log files.** From the timestamps of a web application we compute the gaps between two requests, that is, waiting times $x_1,\dots,x_n$. In order to estimate the load to be expected, together with the mean running time of a request, we model them as $\operatorname{Exp}(\lambda)$-distributed and estimate $\lambda$ as in the example above: $\hat\lambda = 1/\texttt{mean}(x)$. So we reckon with a mean waiting time of $\texttt{mean}(x)$ between two requests, and for the number of requests per unit of time with the Poisson distribution for the same $\lambda$ (chapter [The most important discrete distributions](important-discrete-distributions.ipynb)).
:::

:::{admonition} Example
The k-means algorithm (see the chapter [k-Means](kmeans.ipynb)) can be read as an estimator:
the statistical model is $\mathcal{X} = \mathbb{R}^{nN}$, where $n$ is the dimension of the data (so with $4$ real variables, as in the Iris dataset, $n=4$) and $N$ the sample size (for Iris, $N=150$).

The parameter space is $\mathbb{R}^{nk}$, and the distribution belonging to a parameter $\theta = (c_1,\dots,c_k) \in \mathbb{R}^{nk}$ (with $c_i \in \mathbb{R}^n$) is a mixture model of multivariate normal distributions with expected value $c_i$ and the $n\times n$ identity matrix as covariance matrix.

The 'perfect' k-means solution, that is the centroids $(c_1,\dots,c_k)$ that the k-means algorithm tries to determine, are those for which the sum of the squared Euclidean distances from every point $x_i$ of a sample $x \in \mathcal{X}$ to its nearest centroid is minimal. These are exactly the centroids for which the likelihood of the data under the corresponding mixture distribution becomes maximal.
:::

That leads us to an obvious generalisation of the k-means procedure: we could allow more complicated covariance matrices and so push the likelihood up further. The problem that then arises, however, is that no closed form can be determined for the log-likelihood either, and that one has to think up a new algorithm for the estimation!
