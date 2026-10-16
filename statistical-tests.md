---
title: "Statistical tests: the z-test, the t-test and the p-value"
short_title: "Statistical tests"
description: "Prediction and confidence intervals, the inference from sample to population, how tests are built, the z-test and Student's t-test, with a look at ANOVA."
---

Exploratory data analysis leaves us with hypotheses about which relationships are hidden in the data. When we build systems with machine learning we have a great many decisions to make: whether we may treat a variable as normally distributed, say, or whether two groups or clusters have roughly the same distribution or very different ones.

Tests appear here in two quite different roles, and it helps to keep them apart. In **exploratory analysis** they are one tool among many and answer questions such as "Is this attribute normally distributed?", "Do samples A and B have the same distribution for this attribute? The same mean?" – the answer then decides the next step of the analysis, for instance whether a method that presupposes normality may be used at all. In **communicating results**, by contrast, they are the argument itself: "The test shows that the groups have different distributions, so we use a mixture model" (see [Expectation Maximization](expectation-maximization.ipynb)). In the first role you may test generously, in the second you may not; the section [Significance](#signifikanz) at the end of this chapter explains why.

Strictly speaking, statistical tests are not part of "machine learning", but in the running order of the lecture course this is where they fit naturally.

A test can be read as an estimator that estimates not a single value but a whole range of possible values, followed by a decision rule that interprets the estimate in the light of a hypothesis. We will treat the subject only superficially – just far enough to judge what a test can achieve and where the limits of statistical tests lie – but before that we look at what the difference between single values and ranges of values means for communicating scientific results, data science results included.

## Prediction intervals

By way of motivation we look at the figure {ref}`warming-without-confidence` and then set it against {ref}`warming-with-confidence`.


```{figure} images/global_warming_without_confidence.png
:width: 280px
:align: center
:name: warming-without-confidence

Global warming, projection (A2r scenario at 970 ppmv, IIASA 2009)
```

The figure shows the projection of a statistical model for global warming – given here as the temperature change relative to the pre-industrial level, defined as the mean temperature of the years 1850 to 1900 – on the assumption that the CO2 content of the atmosphere rises to 970 ppmv (parts per million by volume; for comparison, 30 May 2022: 421 ppmv, and 1900: 296 ppmv).
For context: the Paris climate agreement sets a limit of 1.5°C or 2°C – not by 2040, but by 2100.

Let us look at this figure with a data scientist's eyes: what is there to criticise?

A common objection to models and figures of this kind is that things could turn out this way, but just as easily quite differently – these are only theoretical models, after all. The figure expresses a certainty about the course of the curve that cannot possibly exist, which makes the claim "this is how it will be" implausible from the outset. Granted, what it means to say is "this is how it could be", but on its own that is about as useful as "it might rain or it might stay dry".

To make decisions on the basis of a statistical prediction we also need to know how plausible it is. For comparison, look at {ref}`warming-with-confidence`, a figure from the IPCC report SR15, Summary for Policymakers, Figure 1 a) {cite}`sr15`:

```{figure} images/global_warming_with_confidence.png
:width: 480px
:align: center
:name: warming-with-confidence

Global warming, projection (IPCC SR15, Fig. 1)
```

To read this figure properly we also need to know the *IPCC Calibrated Language*, or more precisely the *Likelihood scale* (AR4 and AR5 here refer to the 'assessment reports' that appeared before the special report on 1.5°C):

```{figure} images/likelihood-scale.png
:width: 560px
:align: center
:name: likelihood-scale

The *Likelihood scale* of the IPCC Calibrated Language {cite}`sr15`.
```

Now we can see that the grey shaded area is where the actual measurements will lie with probability at least $2/3$ (according to the model). With that information we can judge far better what warming to expect even if we 'get lucky', and how bad it could get if we 'are unlucky'. Strictly speaking, the grey shaded area is a **prediction interval**: the range in which the actual future value is presumed to lie with high probability. Closely related is the **confidence interval** for a parameter: an interval computed from the sample and constructed so that in (say) 95% of all samples it covers the true parameter.

For the mathematical theory of set estimators and confidence intervals we refer you to the statistics lectures. In what follows our main aim is to understand the notion of a test well enough to judge whether a claimed interpretation of a statistical test is serious. Once we can do that, we also want to recognise the situations in which a hypothesis test can deliver useful insight. Above all, that means getting clear about the notion of significance.


## From the sample to the population

Before we define tests, let us be clear about what we actually want. Every summary measure from the exploratory analysis – mean, proportion, median, correlation coefficient – is computed on a **sample**. What we are interested in is the **population** the sample came from: all passengers, all customers, all the measurements that could have been made. A different sample would have yielded a different number. Inferring from the sample to the population therefore always takes three steps:

1. **Estimate:** compute the summary measure from the sample (the proportion, the mean, the difference of two means).
2. **State the uncertainty:** an interval in which the population's summary measure plausibly lies. A number without an interval is not an inference about the population but a description of the sample.
3. **Decide:** hold the question you had up against the interval. "Is the coin fair?" means: does $\frac12$ lie in the interval? "Do women survive more often?" means: does $0$ lie in the interval for the difference?

There are two routes to step 2.

**The standard error.** By the [central limit theorem](normal-distribution.ipynb) the mean of a sample of size $n$ is approximately normally distributed with standard deviation $\sigma/\sqrt{n}$, the *standard error*. In $95\,\%$ of samples the population mean then lies in the interval

$$
\texttt{mean}(x) \pm 1.96 \cdot \dfrac{\sigma}{\sqrt{n}},
$$

where $\sigma$ is replaced by the sample standard deviation. For a proportion $\hat p$ we have $\sigma = \sqrt{\hat p(1-\hat p)}$. Coin-toss example: with $45$ successes in $100$ tosses, $\hat p = 0.45$ and the standard error is $\sqrt{0.45 \cdot 0.55/100} \approx 0.05$, so the interval is roughly $[0.35,\ 0.55]$. The $\frac12$ lies inside it, so the coin could be fair. To reject that, the interval would have to be narrower, and it shrinks only with $\sqrt{n}$: halving the width takes four times the sample. (With the cruder Chebyshev inequality in place of the normal approximation one gets an interval of $\pm 0.22$ and a required sample of over $2000$ tosses; that calculation is in the section *Looking ahead: confidence intervals* below.)

**The bootstrap.** For summary measures that have no formula, or whose formula you do not know, you pretend that the sample is the population: draw from it, *with replacement*, a new sample of the same size, compute the measure, and repeat many thousands of times. The spread of these bootstrap measures estimates the spread of the measure across real samples, and the $2.5$ and $97.5$ percentiles give a 95% interval. With the arrays `survived` and `sex` from the chapter [Titanic EDA](titanic-eda-numpy.ipynb):

```python
rng = np.random.default_rng(0)
f = survived[sex == 'female']
m = survived[sex == 'male']
difference = f.mean() - m.mean()
bootstrap = np.array([rng.choice(f, len(f)).mean() - rng.choice(m, len(m)).mean()
                      for _ in range(10000)])
print(difference, np.percentile(bootstrap, [2.5, 97.5]))
```

```
0.553  [0.495 0.609]
```

The women's survival rate is $55$ percentage points above the men's, and even at the unfavourable end of the interval still $50$. The $0$ lies far outside: the difference is no accident of the sample. `scipy.stats.bootstrap` does the same thing in one line, with better-corrected percentiles.

**What the recipe assumes.** Both routes assume that the sample is a *random sample* from the population, that is, that every row of the population had the same chance of ending up in the sample. The Titanic list is a random sample of exactly one population: the passengers of that ship (and even then only the Kaggle extract). About other shipping disasters the interval says nothing, however narrow it is. Anyone who runs a survey on campus and wants to draw conclusions about all students has the same problem, and no sample size in the world cures it.

A statistical **test**, the subject of this chapter, is step 3 made formal: a rule, fixed in advance, that decides from the sample whether a hypothetical value is still plausible. The z-test and the t-test below are exactly the standard-error calculation above, read the other way round: instead of asking whether $\mu_0$ lies in the interval around $\texttt{mean}(x)$, they ask how many standard errors $\texttt{mean}(x)$ is away from $\mu_0$.

## Looking ahead: confidence intervals

:::{note}
**Looking ahead (not part of the course proper):** this section and the two sections *From set estimator to test* and *Best simple tests* are background that helps make sense of statistical tests. They explain where the tests come from, and taken on their own they are not part of the course proper. If you skip them, read straight on at the section *Tests* and then at *The z-test*.
:::

:::{admonition} Definition
Let $(\mathcal{X}, P_\theta : \theta \in \Theta)$ be a statistical model, $\Sigma$ an arbitrary set and $\tau \colon \Theta \to \Sigma$ a quantity to be estimated that depends on the parameter $\theta$. Let $0 < \alpha < 1$ be a real number.
A map $C \colon \mathcal{X} \to \mathcal{P}(\Sigma)$ that assigns to every possible observation $x \in \mathcal{X}$ a set $C(x) \subseteq \Sigma$ is called a **confidence region for $\tau$ at error level $\alpha$** if

$$
\inf_{\theta \in \Theta} P_{\theta}\left( x \in \mathcal{X} \colon \tau(\theta) \in C(x) \right) \geq 1 - \alpha.
$$

If in addition $\Sigma = \mathbb{R}$ and every $C(x)$ is an interval, we speak of a **confidence interval**.
:::

:::{admonition} Example
**The trivial case:**
The constant confidence region $C(x) := \Sigma$ always satisfies $\tau(\theta) \in C(x)$ for every $\theta$, so $P_\theta\left(x \in \mathcal{X} : \tau(\theta) \in C(x)\right) = 1 \geq 1 - \alpha$ for every $\alpha$.
Read: we are certain that the 'right' estimate lies in the range of $\tau$.
That is not a particularly useful confidence region, of course, but it makes clear that the region is perfectly allowed to be 'too big'. It is in our interest to find a $C$ whose $C(x)$ are as small as possible, because only then does the statement become interesting.
:::

:::{admonition} Example
**Coin toss:**
$n$ repeated tosses of an unfair coin with success probability $p$ can be modelled with the **binomial model** (see [The most important discrete distributions](important-discrete-distributions.ipynb)): $\mathcal{X} = \{0,\dots,n\}$ is the number of successes, the unknown parameter is $\theta = p \in \Theta = [0,1]$ and $P_\theta = \operatorname{Bin}(n,\theta)$ (and $\tau = id$, so we are estimating the parameter $\theta$ itself).

We have already computed the maximum likelihood estimator for $\theta$ there: $\hat\theta = \frac{x}{n}$, the proportion of successes. Concretely, if we toss the coin $100$ times and get tails $45$ times, we estimate $\theta$ as $\frac{45}{100}$ (and in particular that the coin really is unfair).
:::

But what is our confidence – our trust – in this? Do we still regard values far from $\frac{x}{n}$ as halfway plausible, or can we pin down a very narrow range around $\frac{x}{n}$ that we hold to be plausible? In the concrete example with the estimate $\theta = \frac{45}{100}$, would $\theta = \frac{1}{2}$ still be halfway plausible?

We now want to construct intervals $C(x) = (\frac{x}{n} - \epsilon, \frac{x}{n} + \epsilon)$ with $\epsilon > 0$ as small as possible, such that the condition on a confidence region from the definition is satisfied:

$$
\begin{aligned}
 & \inf_{\theta \in \Theta} P_{\theta}\left( x \in \mathcal{X} \colon \tau(\theta) \in C(x) \right) \geq 1 - \alpha \\
 \Leftrightarrow & \inf_{\theta \in [0,1]} P_{\theta}\left( x \in \mathcal{X} \colon \left|\theta - \frac{x}{n}\right| < \epsilon \right) \geq 1 - \alpha \\
  \Leftrightarrow & \inf_{\theta \in [0,1]} P_{\theta}\left( x \in \mathcal{X} \colon \left|\theta - \frac{x}{n}\right| \geq \epsilon \right) \leq \alpha \\
\end{aligned}
$$

In words: we are to determine $\epsilon$ (as a function of $\alpha$, and as small as possible) so that $\left|\theta - \frac{x}{n}\right| \geq \epsilon$ holds for fewer than a proportion $\alpha$ of the possible samples $x$. With $\alpha = 0.05$, say (a common choice), that means our estimation error exceeds $\epsilon$ in only 5% of samples.

The shape of this inequality may remind you of Chebyshev's inequality, which we met right after introducing the variance. For the estimator $T(x) = \frac{x}{n}$ it says

$$
 P_{\theta}\left( \left|\mathbb{E}(T) - T\right| \geq c \right) \leq \dfrac{\mathbb{V}T}{c^2}
$$

Naturally we would like to take $c=\epsilon$ and choose $\epsilon$ as a function of $\alpha$ so that nothing but $\alpha$ is left on the right-hand side. We have $\mathbb{V}T = \mathbb{V}\!\left(\frac{x}{n}\right) = \frac{\theta(1-\theta)}{n}$, which annoyingly still depends on $\theta$ – exactly the thing we do not know!

So we bound $\theta(1-\theta) \leq \frac{1}{4}$ (easy to check: equality at $\theta = \frac{1}{2}$, strict inequality everywhere else).

Putting it all together, $\epsilon$ is well chosen if

$$
\begin{aligned}
           & \dfrac{\mathbb{V}T}{\epsilon^2} \leq \alpha \\
\Leftarrow & \frac{1}{4 n \epsilon^2} \leq \alpha \\
\Leftrightarrow & \frac{1}{4 n \alpha} \leq \epsilon^2 \\
\Leftrightarrow & \frac{1}{2 \sqrt{n \alpha}} \leq \epsilon \\
\Leftarrow & \frac{1}{2 \sqrt{n \alpha}} =: \epsilon.
\end{aligned}
$$

In our concrete example, with $\alpha = 0.05$ and $n=100$, $\epsilon := \frac{1}{2\sqrt{5}} \approx 0.2236$ does what we want.
For us that means: for the concrete observation $k=45$, not only the point estimate $\frac{45}{100}$ is plausible; we also regard roughly $\frac{23}{100}$ and $\frac{67}{100}$ as plausible. So the coin could well be fair, and we have merely caught an unlucky observation.

So confidence intervals obtained from Chebyshev's inequality are very wide. There are several better (and considerably more complicated!) methods for obtaining narrower ones.

But we also see a simple relationship between $\epsilon, n$ and $\alpha$: making $\alpha$ smaller (that is, demanding more certainty) makes $\epsilon$ bigger; making $n$ bigger (taking larger samples) makes $\epsilon$ smaller.

With that we can compute, for instance, how large the sample has to be before we can say with certainty at least $1-\alpha$ that our coin is not fair. Again, concretely, suppose one sample has given us the estimate $\theta = 0.45$.

$$
\begin{aligned}
 & 0.45 + \epsilon < 0.5 \\
\Leftrightarrow & 0.45 + \frac{1}{2 \sqrt{n \alpha}} < 0.5 \\
\Leftrightarrow & \frac{1}{2 \sqrt{n \alpha}} < 0.05 \\
\Leftrightarrow & 2 \sqrt{n \alpha} > \frac{100}{5} \\
\Leftrightarrow & \sqrt{n \alpha} > 10 \\
\Leftrightarrow & n \alpha > 100 \\
\Leftrightarrow & n > \frac{100}{\alpha}
\end{aligned}
$$

and putting in $\alpha = 0.05$, the sample has to be larger than $2000$ before we can reject the claim that the coin is fair. With a cleverer procedure for determining narrower confidence intervals, a smaller sample would do.



:::{admonition} Example
**A sample from a normal distribution:**
Suppose the real-valued random variable $Z$ is normally distributed with unknown expected value $\mu$ and unknown variance $\sigma^2$.
We draw $n$ independent, identically distributed samples of $Z$ and obtain a random variable $X$ with values in $\mathbb{R}^n$, that is $X = (X_1,\dots,X_n)$, where $X_i \sim Z$.

We write $\texttt{mean}(X) = \sum_{i=1}^n \frac{X_i}{n}$ for the sample mean (careful: this is now a random variable, computed from the random sample $X$) and $S^\ast(X)^2 := \frac{1}{n-1} \sum_{i=1}^n (X_i - \texttt{mean}(X))^2$ for the sample variance (with the Bessel correction, i.e. $n-1$ in the denominator, so that the estimate is unbiased).
:::

We now want to know how well $\texttt{mean}(X)$ estimates $\mu(Z)$ – how far does our confidence, our trust, reach?

The random variable $\texttt{mean}(X)$ is normally distributed, with mean $\mu(Z)$ and standard deviation $\dfrac{\sigma(Z)}{\sqrt{n}}$.
The estimation error, measured with the standard deviation of $\texttt{mean}(X)$ as the 'unit', is

$$
\dfrac{\texttt{mean}(X) - \mu(Z)}{\sigma(Z)/\sqrt{n}}
$$

and is therefore standard normally distributed. The trouble with this quantity is that we do not actually know $\sigma(Z)$, and yet we would like to look at the error of our estimate of $\mu(Z)$. So we have to replace $\sigma(Z)$ by its estimate $S^\ast(X)$.

The random variable 'sample variance' $S^\ast(X)^2$ is distributed so that $\dfrac{n-1}{\sigma(Z)^2} S^\ast(X)^2$ follows a **$\chi^2$ distribution** with $n-1$ degrees of freedom (a special case of the gamma distribution).

The probability density function of the $\chi^2$ distribution need not concern us at the moment (and in particular is not part of the course proper); for completeness, here it is:

$$
f(x) = \dfrac{1}{2^{\frac{k}{2}} \Gamma\left( \frac{k}{2} \right)} x^{ \frac{k}{2}-1}e^{-\frac{x}{2}}
$$


```{figure} images/chi-squared-distributions.png
:width: 420px
:align: center
:name: chiquadrat

Chi-squared distributions with various parameters (degrees of freedom)
```

The difference between the estimated mean and the actual expected value, measured with the sample standard deviation as the 'unit', is the estimated estimation error $T$, the statistic we look at next:

$$
T = \dfrac{\texttt{mean}(X) - \mu(Z)}{S^\ast(X)/\sqrt{n}}.
$$

The random variable $T$ follows a **Student t distribution**, which at first glance looks like a normal distribution but has heavier *tails*: it takes values far from the expected value with higher probability. Its only parameter is the number of degrees of freedom $\nu > 0$, here $\nu = n-1$. For $\nu$ of at least $3$ the expected value is $0$ and the variance is $\nu / (\nu - 2)$.

The probability density function of the Student t distribution matters little to us for now; for completeness, this is what it looks like:

$$
f(t) = \dfrac{1}{\sqrt{\nu} B\left(\frac{1}{2}, \frac{\nu}{2}\right)} {\left( 1 + \dfrac{t^2}{\nu} \right)}^{-\frac{(\nu+1)}{2}}
$$

where $B(x,y) = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$ is the beta function and the gamma function $\Gamma$, defined on all of $\mathbb{R}$, interpolates $\Gamma(n+1)=n!$ so that $\Gamma(x)x = \Gamma(x+1)$ always holds (all of which we may promptly forget again).

As $n \to \infty$ the Student t distribution converges to the standard normal distribution. So the gap between the t distribution and the normal distribution encodes exactly the uncertainty that a small sample brings with it.

```{figure} images/student-t-distributions.png
:width: 420px
:align: center
:name: studentt

Student t distributions with various parameters (degrees of freedom)
```

We are now interested in where the probability of a large estimation error
$T = \dfrac{\texttt{mean}(X) - \mu(Z)}{S^\ast(X)/\sqrt{n}}$
is small. Now this estimation error does not depend on $\mu(Z)$ – more precisely, $T$ is independent of $\mu(Z)$. That may seem counter-intuitive, since $\mu(Z)$ appears in the formula, but it is true all the same. The statistic is said to be **distribution-free**.

For a given $\alpha$ we now choose $t$ as the $(1-\frac{\alpha}{2})$-*quantile* of the $t$ distribution with $n-1$ degrees of freedom, that is, the number $t > 0$ with $P(T \leq t) = 1 - \frac{\alpha}{2}$; by the symmetry of the distribution we then have $P(|T| \leq t) = 1 - \alpha$. This used to be looked up in a table; today we ask the computer (`scipy.stats.t.ppf(1 - alpha/2, n - 1)`).
Then, with $\epsilon := t\frac{S^\ast(x)}{\sqrt{n}}$, a confidence interval for $\mu(Z)$ is given by

$$
C(x) = (\texttt{mean}(x) - \epsilon, \texttt{mean}(x) + \epsilon).
$$

So we see that constructing a confidence region can get complicated quickly. On the other hand, the procedure described here (standardise, then apply the quantile transformation) carries over to other situations as well – which we would rather leave to the statisticians.

By approximating the binomial distribution with a normal distribution and then applying the method just discussed for confidence intervals of a normal distribution, one also gets better confidence intervals for a binomial distribution – though here again more complicated procedures yield considerably better ones.

It is enough for us to know where the $\chi^2$ distribution and the Student t distribution come from; the concrete probability densities we may forget again – fortunately the statisticians have worked them out for us and put them into our Python packages. What matters above all is that the naive assumption that the estimation error is in turn normally distributed does not hold in general. We will meet these distributions again when we discuss statistical tests, which in a sense build on the construction of confidence intervals.


## Tests

:::{admonition} Definition
Let $(\mathcal{X}, P_\theta : \theta \in \Theta)$ be a statistical model and $\Theta = \Theta_0 \cup \Theta_1$ a disjoint decomposition of the parameter space into the **null hypothesis** $\theta \in \Theta_0$ and the **alternative** $\theta \in \Theta_1$.
Every statistic $\phi \colon \mathcal{X} \to [0,1]$ (which we read as a decision rule) is called a **test** of $\Theta_0$ against $\Theta_1$.
A test is called **non-randomised** if $\phi(x)=0$ or $\phi(x)=1$ for all $x \in \mathcal{X}$, and **randomised** otherwise.
:::

:::{admonition} Example
**Weighing apples.** A supplier promises apples of at least $150\,\mathrm{g}$ on average; we assume the weights to be normally distributed and weigh a sample $x$. Three tests for the same sort of question:

1. $\Theta_0 = (-\infty, 150]$ ("the apples weigh at most $150\,\mathrm{g}$ on average"), $\Theta_1 = (150, \infty)$. One test: $\phi(x) = 1$ if $\texttt{mean}(x) > 150$, otherwise $0$.
2. The same hypothesis, but a more cautious test: $\phi(x) = 1$ only once $\texttt{mean}(x) > 160$. It rejects less often, so it errs less often when $\Theta_0$ is true and misses more often when $\Theta_1$ is true.
3. $\Theta_0 = \{150\}$ ("exactly $150\,\mathrm{g}$"), $\Theta_1 = \mathbb{R} \setminus \{150\}$. One test: $\phi(x) = 0$ if $150$ lies in the interval $\texttt{mean}(x) \pm 1.96\,\sigma/\sqrt{n}$ from the section *From the sample to the population*, otherwise $1$.

The next definition gives names to the two errors in version 2; version 3 is the z-test described below.
:::

:::{admonition} Definition
The probability of a **type I error** – rejecting the null hypothesis (that is, $\phi(x)=1$) even though the true parameter is $\theta \in \Theta_0$ – is $\sup_ {\theta \in \Theta_0} \mathbb{E}_\theta(\phi)$ and is also called the **effective level** of the test.
For any $\alpha$ greater than or equal to the effective level, the test is also called a test of level $\alpha$.

The function $G_\phi \colon \Theta \to [0,1]$ given by $G_\phi(\theta) = \mathbb{E}_\theta(\phi)$ is called the **power function** of the test.
$1 - G_\phi(\theta)$ is the probability of a **type II error** – accepting the null hypothesis (that is, $\phi(x) < 1$) even though the true parameter is $\theta \in \Theta_1$.
For $\theta \in \Theta_1$, $G_\phi(\theta)$ is also called the **power** of $\phi$ at $\theta$.
:::

In the apple example the test with threshold $160$ has a smaller effective level than the one with threshold $150$, but also less power.

:::{admonition} Definition
A test $\phi$ is called a **uniformly best test at level $\alpha$** if it is of level $\alpha$ and every other test of level $\alpha$ has smaller or equal power.
:::

So a uniformly best test has probability at most $\alpha$ of a type I error and, among all tests with that property, the smallest probability of a type II error.


## Looking ahead: from set estimator to test

:::{note}
Looking ahead, not part of the course proper (see the note at *Confidence intervals*).
:::

When we discussed a confidence interval for the binomial model we already saw that it can help us reach a decision (concretely: should I regard a coin with $45/100$ successes as 'unfair', or does sampling error explain the deviation from $50/100$? Or indeed: how many more samples do I need to settle the question for good?)

This relationship can be systematised: using the vocabulary of the shape parameter, a set estimator can be constructed from any test. Here we look only at the other direction, how a test is constructed from a set estimator.

Our starting point is (for simplicity) a parametric statistical model $(\mathcal{X}, P_\theta : \theta \in \Theta)$ and an interval estimator (that is, a confidence interval at level $1-\alpha$) $C \colon \mathcal{X} \to \mathcal{P}(\Theta)$ for the parameter $\theta$. In addition we have a hypothetical parameter value $\theta_0 \in \Theta$ that does *not* come from the data but from somewhere else: $\theta_0 = \frac{1}{2}$ for the claim 'the coin is fair', say, or a value from the literature or from an earlier experiment.

The hypothesis is now that $\theta_0$ is the true parameter.
Strictly speaking, this hypothesis is of course probably always false; what interests us is when it can be rejected with *certainty*. So we set $\Theta_0 := \{\theta_0\}$ and $\Theta_1 := \Theta - \{\theta_0\}$.

From this we construct the test $T_C \colon \mathcal{X} \to [0,1]$ by

$$
T_C := 1_{\{ x \in \mathcal{X} | \theta_0 \notin C(x) \}} \text{ (indicator function)} 
$$

$$
T_C(x) = \begin{cases} 0 & \theta_0 \in C(x) \\ 1 & \theta_0 \notin C(x) \end{cases}
$$

So the procedure is: from the data $x \in \mathcal{X}$ we compute the confidence interval $C(x)$ and ask whether $\theta_0$ lies in it. If it does, we keep the hypothesis '$\theta_0$ is the true parameter'; if not, we conclude '$\theta_0$ cannot be the true parameter'. Since $C$ is a confidence interval at level $1-\alpha$, we have $P_{\theta_0}(\theta_0 \notin C(x)) \leq \alpha$, so the test $T_C$ has level $\alpha$.

What matters is that $\theta_0$ was not itself estimated from the same data: a point estimator $\hat{\theta}(x)$ – the midpoint of $C(x)$, say – always lies in $C(x)$, and such a test would never reject. The test is interesting precisely when $\theta_0$ comes from an independent source, for example when we ask whether or not the data are uniformly or normally distributed.

## Looking ahead: best simple tests

:::{note}
Looking ahead, not part of the course proper (see the note at *Confidence intervals*).
:::

We have already seen the definition of level and power, and the usual procedure of looking for the most powerful test at a fixed level.

:::{admonition} Definition
If there are only two possible parameters (one then speaks of **simple hypotheses**), that is $\Theta_0 = \{\theta_0\}$ and $\Theta_1 = \{\theta_1\}$,
and $f_0$ and $f_1$ are the density functions of the distributions that belong to these parameters, then

$$
R(x) := \dfrac{f_1(x)}{f_0(x)}
$$

is called the **likelihood ratio**, and a test $\phi \colon \mathcal{X} \to [0,1]$ of the form

$$
\phi(x) = \begin{cases}
           0 & R(x) < c \\
           1 & R(x) > c
\end{cases}
$$

with $c \in \mathbb{R}$ is called a **Neyman–Pearson test** with threshold $c$.
:::

Why is $R(x)$ called the likelihood ratio? Because $f_1(x)$ is a measure of the probability $P(D|H_1)$ and $f_0(x)$ is a measure of the probability $P(D|H_0)$, so $R$ is the ratio of the two likelihoods. If $f_0(x)=0$, we simply set $R = \infty$.

The case $R(x) = c$ usually has probability $0$, but it can be handled separately if need be (with a suitable value of $\phi(x)$ between $0$ and $1$).

The **Neyman–Pearson lemma** says that for every simple hypothesis (that is, every $\Theta$ with two elements) and every level $\alpha$ there is a Neyman–Pearson test (that is, a suitable $c \in \mathbb{R}$) that uses up the level in full (has effective level $\alpha$), and that every such test is a uniformly best test at level $\alpha$.

**Stein's lemma** says something about how much additional samples help to make a test more informative. Fix a level $\alpha$. Take a sequence of observations and, for each $n$, a Neyman–Pearson test $\phi_n$ of level $\alpha$ that depends only on the first $n$ of them. Then the power of $\phi_n$ tends to $1$ as the observations accumulate (that is, as $n \to \infty$), and it does so exponentially fast. More precisely:

$$
\lim_{n \to \infty} \frac{1}{n} \log\left( 1 - \mathbb{E}_1(\phi_n) \right) = -H(P_0 \Vert P_1)
$$

So the higher the relative entropy $H(P_0 \Vert P_1)$ between the two possible distributions, the more power every single additional sample buys.

The connection runs through the definitions of the Neyman–Pearson test and of relative entropy: the expression $-f_0(x) \log R(x) = f_0(x)\log \left( \frac{f_0(x)}{f_1(x)} \right)$ appears in the definition of continuous relative entropy.

The take-home message: for simple hypotheses best tests always exist, and relative entropy quantifies how far enlarging the sample pushes down the probability of a type II error.

## The z-test

If your data points are independent (and identically distributed) – a sample of a random variable, say – and normally distributed, and you know the standard deviation $\sigma$, you can run a **z-test** (also called the **Gauss test**). It is the 'simpler' variant of the t-test (see below). If you do not know $\sigma$ and put in the sample standard deviation instead, that is still defensible for large $n$, because the t distribution is then practically a normal distribution; how crude the widespread rule of thumb "$n > 30$" is for this purpose is described in the chapter [The normal distribution](normal-distribution.ipynb) under *The "N ≥ 30" myth*.

The test asks whether a sample $x$ follows a normal distribution with mean $\mu_0$. For $\mu_0 = \texttt{mean}(x)$ (the maximum likelihood estimator) there is nothing to test – we conclude at once that $\mu = \mu_0$ is plausible. But what about values $\neq \texttt{mean}(x)$? Suppose our sample *almost* follows a standard normal distribution; then it would make sense to test whether the hypothesis of a standard normal distribution should be accepted or rejected, even though the maximum likelihood estimator gives something other than $0$ for $\mu$.

The **z-statistic** is

$$
Z(x) = \dfrac{\texttt{mean}(x) - \mu_0}{\sigma/\sqrt{n}}
$$

In the z-test $\sigma$ is treated as known; for large samples the sample standard deviation $\sigma^\ast(x)$ takes its place. The unknown is $\mu$, and the null hypothesis reads $H_0$: $\mu = \mu_0$. In the t-test below, by contrast, $\sigma$ is treated as unknown, and the error made in estimating $\sigma$ is built into the distribution of the test statistic.
The random variable $Z$ is standard normally distributed.

In a two-sided z-test the null hypothesis is $H_0 := (\mu = \mu_0)$, which corresponds to $\Theta_0 = \{\mu_0\}$, and the alternative is $H_1 = (\mu \neq \mu_0)$, which corresponds to $\Theta_1 = \mathbb{R} \setminus \{\mu_0\}$.

We choose a level $\alpha$, say $\alpha = 0.05$.
Since we want a two-sided test, we look up the z-value for $1 - \alpha/2$ (in a table of z-values, say, or with the quantile function `scipy.stats.norm.ppf(1 - alpha/2)`). For $\alpha = 0.05$ the z-value is $\pm 1.96$.
The z-value $z(p)$ is the $p$-quantile of the standard normal distribution, so $P(Z \leq z(p)) = p$,
here concretely $P(Z \leq 1.96) = 0.975$.
Because the standard normal distribution is symmetric, we also have $P(Z \geq -1.96) = 0.975$ and $P(-1.96 \leq Z \leq 1.96) = 0.95$.

So we compute the z-statistic of our sample and compare it with the z-value $1.96$. If it lies in between, that is $-1.96 \leq Z(x) \leq 1.96$, we cannot reject the null hypothesis (which does not mean we accept it; see [Significance](#signifikanz) below). If the z-statistic lies outside $[-1.96, 1.96]$, we reject the hypothesis.

## The Student t-test

The two tests side by side:

| | z-test | t-test |
|---|---|---|
| $\sigma$ | known (for large $n$: $\sigma^\ast(x)$ substituted) | unknown, estimated along the way |
| distribution of the statistic under $H_0$ | standard normal distribution | Student t distribution with $n-1$ degrees of freedom |
| when | $\sigma$ known, otherwise only for large $n$ | always; for large $n$ practically the same test |
| SciPy | `norm.ppf` | `t.ppf`, `ttest_1samp` |

With small samples the bias in the estimated parameters of a normal distribution makes itself felt, and we have to work with the actual distribution of the **t-statistic**. So if $\mu_0$ is the parameter we want to test for, we consider

$$
t(x) = \dfrac{\texttt{mean}(x) - \mu_0}{\sigma^\ast(x)/\sqrt{n}}
$$

Here $\sigma^\ast(x)$ is the unbiased estimator of $\sigma$.

As we saw when constructing confidence intervals, $t$ follows a Student t distribution. To carry out the test at level $\alpha$ we therefore look up the t-value for that level in a table, or compute it in Python with `scipy.stats.t.ppf(p, n-1)` (ppf stands for **percent point function**; it gives us the p-quantile of the t distribution with $n-1$ degrees of freedom).

We compute the t-statistic on the data $x$ and compare it with the 'critical' t-value computed beforehand. If the t-statistic lies within $\pm$ the critical t-value, we cannot reject the hypothesis (that $\mu_0$ is the expected value of the distribution); if it lies outside, we reject it.

We can also have SciPy compute this two-sided t-test directly:
`scipy.stats.ttest_1samp(x, mu)`

Strictly speaking the t-test can do more: instead of comparing the distribution of $x$ with a normal distribution of mean $\mu$ and the same variance as $x$, we can compare two samples $x,y$ (not necessarily of equal size) and ask whether their means agree, with `scipy.stats.ttest_ind(x, y)` – assuming both samples are normally distributed with equal variance and independent of each other. The case $y = \texttt{mu}$ is a special case of this (but calling it with that $y$ only returns `NaN`s, because the variance of a one-element sample is $0$; hence `ttest_1samp`).

The return value of `scipy.stats.ttest_1samp(x, mu)` is a `TtestResult` object with the attributes `statistic`, `pvalue` and `df` (the number of degrees of freedom, that is $n-1$) as well as the method `confidence_interval(level=0.95)`. (Older SciPy versions returned a `namedtuple` with only `statistic` and `pvalue`; those two attributes are unchanged.)
The attribute `statistic` is the computed t-statistic (no $\alpha$ has been involved yet, so you would still have to compare it by hand with the critical t-value to get the test result).
The attribute `pvalue` is the **p-value** (also called the **significance**) of the test result: the probability, under $H_0$, of observing a test statistic at least as extreme as the one actually observed – for the two-sided test, $p = P(|T| \geq |t_{\text{obs}}| \,|\, H_0)$. In particular the p-value is *not* the probability of the concrete observation (which for continuous distributions would always be $0$), nor the probability $P(H_0 | D)$ that the null hypothesis is true.
The name comes from 'probabilitas', and the word 'significance' naturally carries certain associations.
If $p < \alpha$ we reject the null hypothesis; otherwise we cannot reject it, which is not the same as accepting it: a high p-value only says that the sample cannot tell the deviation apart from a sampling error (see the second warning in the section [Significance](#signifikanz) below).

For the apple example from the section *Tests*, with a simulated sample of $40$ normally distributed weights and the null hypothesis $\mu_0 = 150$ as in the third test there:

```python
from scipy.stats import ttest_1samp, norm
x = norm.rvs(155, 20, size=40, random_state=0)
res = ttest_1samp(x, 150)
res.statistic, res.pvalue, res.df, res.confidence_interval()
```

```
(3.3007, 0.00207, 39, ConfidenceInterval(low=154.36, high=168.15))
```

The p-value is below $0.05$, so we reject $\mu_0 = 150$; fittingly, $150$ lies outside the confidence interval. `confidence_interval()` is exactly the interval from the section *From the sample to the population*, $\texttt{mean}(x) \pm t \cdot \sigma^\ast(x)/\sqrt{n}$, except that the quantile $t = \texttt{t.ppf}(0.975, 39) \approx 2.02$ of the t distribution replaces $1.96$.

For the two-sample case there is also a variant that needs only the summary measures:
```python
ttest_ind_from_stats(mean1, std1, nobs1,
                     mean2, std2, nobs2,
                     equal_var=True,
                     alternative="two-sided")
```

where `alternative` says whether a two-sided or a one-sided (`less` or `greater`) test is to be run, and `nobs` is the number of observations. If `equal_var` is set to `False`, the assumption of equal variance is dropped, and what runs is then not the ordinary t-test but Welch's t-test, which computes the degrees of freedom differently.

If two samples do not satisfy the basic assumption of equal variance, a transformation of the scale (taking logarithms, for instance) can sometimes bring it about, at least approximately, and so make the t-test useful in these cases too. If the variances differ markedly, keep your hands off the t-test altogether: it is not informative.

## Looking ahead: ANOVA

ANOVA, short for **Analysis of Variance**, generalises the t-test to more than $2$ sample groups. Its assumptions are the same as for the t-test:

* The observations are independent of one another
* The residuals (the differences $x_i-\texttt{mean}(x)$, an estimate of the actual sampling error) are normally distributed
* Homoscedasticity, that is, homogeneity of variance: the variances of the sample groups are equal.

It is usually applied to a categorical variable with $k$ levels: the sample is split into $k$ groups by level and ANOVA is run on these groups. If a significant deviation shows up (that is, a p-value below $0.05$), we reject the null hypothesis that the groups have equal expected values – and conclude that the categorical variable probably influences the expected value.

If no significant deviation shows up (p-value of $0.05$ or more), we may well see differences between the various means, but no larger than a sampling error already explains well – no influence of the categorical variable can be seen this way.

Careful: that does not mean the categorical variable has no influence on the means! It only means that our sample cannot tell such an influence apart from a sampling error.
'We know that we know nothing'.

In Python we use `scipy.stats.f_oneway`.

(signifikanz)=
## Significance

Of all the notions in this chapter this is the most important, because it leaves statistics behind and turns up in newspapers, studies and meetings. There it is almost always used as though there were a number behind it. There is not.

:::{admonition} Definition
The result of a statistical test is called **statistically significant** if the sample data deviate from the null hypothesis so strongly that, by a rule *fixed in advance*, that assumption is rejected.
:::

:::{admonition} Remark
There is no number in this definition. The rule may be arbitrarily strict or arbitrarily silly; "significant" only says that it was triggered. Whether that means anything can only be judged once you know the rule, the level and the null hypothesis. So anyone who says "the difference is significant" has thought up a context in which that sentence is permitted; without it, the sentence is empty. From now on, use the word the way you use "continuous": only in its technical sense.
:::

The usual rule is "$p < \alpha$" with level $\alpha = 0.05$. That is a convention of the journals, not a constant of nature. It does at least have a rationale: a normally distributed quantity deviates from its expected value by more than just under two standard deviations ($1.96\,\sigma$) with probability only $5\,\%$, so a result beyond that line is "conspicuous". For delicate questions more is demanded: $p \leq 0.01$ is called **very significant**, $p \leq 0.001$ **highly significant** (about three standard deviations). Particle physics counts in standard deviations outright and demands five of them for a discovery.

Three warnings go with the definition:

1. **Rejecting $H_0$ does not mean accepting $H_1$.** The test has only said that the data are improbable under $H_0$; it has said nothing about the alternative, and certainly nothing about whether $H_1$ is the only other explanation.
2. **A high p-value says nothing.** "Not significant" only means that the sample cannot tell the deviation apart from a sampling error. It does not mean that there is no deviation (see the remark on ANOVA above).
3. **Without a well-chosen null hypothesis the p-value means nothing.** Anyone who picks an $H_0$ that nobody believes anyway gets a significant result for free. Which hypothesis to formulate as $H_0$ is the subject of the next section.

Once more, as a reminder: a **type I error** is a false rejection of the null hypothesis. Small p-values thus tempt you into a type I error, and anyone who runs enough tests will eventually find a significant one:

```{figure} images/xkcd-significant.png
:width: 300px
:align: center
:name: xkcd-significant

Randall Munroe, [xkcd 882 "Significant"](https://xkcd.com/882/) (CC BY-NC 2.5) (So, uh, we did the green study again and got no link. It was probably a-- "RESEARCH CONFLICTED ON GREEN JELLY BEAN/ACNE LINK; MORE STUDY RECOMMENDED!")
```

To be published in important journals, studies often have to show significant results. That is a problem, because

* significant results, too, can be pure accident (the comic),
* there are tricks for shrinking the p-value systematically without learning anything more about the question (**p-value hacking**, cf. {ref}`pvalue-hacking`): testing many hypotheses and reporting only the significant one, extending the sample until $p$ drops below $0.05$, removing outliers after the fact,
* non-significant results can be scientifically relevant too, but are published less often (**publication bias**),
* the p-value is very often misread, and not only by students: in the survey of {cite}`haller`, even most of the methodology lecturers got at least one of six statements about the meaning of a significant result wrong.

**Most Published Research Findings Are False**

[Ioannidis JPA (2005) Why Most Published Research Findings Are False.
PLOS Medicine 2(8): e124.](https://doi.org/10.1371/journal.pmed.0020124)

> "the probability that a research finding is indeed true depends on the prior probability of it being true (before doing the study), the statistical power of the study, and the level of statistical significance"

The less plausible the hypothesis (the lower its prior probability), the more likely an exciting finding is to turn out a false alarm, regardless of the p-value.

A very important safeguard against p-value hacking is the pre-registration of studies: hypothesis, level and analysis are fixed before the data exist. That is exactly what the definition above demands with its "rule fixed in advance".

```{figure} images/pvalue-hacking.png
:width: 600px
:align: center
:name: pvalue-hacking

[Compilation by Uri Simonsohn, 2015](http://datacolada.org/41)
```

## What to formulate as hypothesis, what as alternative?

The usual procedure is to formulate the scientific insight you would like to establish as the rejection of the null hypothesis. It makes a difference which statement becomes the hypothesis and which the alternative, because we defined best tests so that the type I and type II errors play different roles: the type I error is held exactly at the level $\alpha$, and the type II error is minimised subject to that constraint.

:::{admonition} Example
Imagine we have found a new drug that we believe makes people cleverer. To show this, we proceed as follows: we design an experiment in which the claim that our drug makes people cleverer could be refuted. To that end we operationalise "becoming cleverer" by, say, an examination situation with cognitive tasks. The participants are randomly split into two groups. One group gets a placebo, the other the drug; everything else is the same, and nobody (not even the people running the study) knows who is in which group. Afterwards the data are analysed – performance in the examination is one variable, group membership the other.

The null hypothesis is now: the drug has no effect. The alternative: the drug makes people cleverer. If we assume performance to be normally distributed, we can run a two-sample t-test. If $p < 0.05$ we reject the null hypothesis and conclude that the observation cannot be chance – that the variable 'group membership' has a significant influence on performance.
:::

Even with $p < 0.05$ a type I error can of course still occur, because $0.05 \neq 0$.
The null hypothesis was $\mu_1 = \mu_2$, where the $\mu_i$ are the means of the two groups; the alternative is $\mu_1 \neq \mu_2$. When we derived the t-test we set up the t-statistic by comparing the sample mean with a fixed $\mu_0$. And there the roles of hypothesis and alternative cannot be swapped!

You can see that the two cannot be swapped in the ordinary-language version of the hypothesis too: "the drug has no effect" really means "whether or not you take the drug has no influence on test performance". How would you formalise "has an influence on test performance" mathematically?

What you can do instead is test for an explicitly described relationship, for example the hypothesis that after taking the drug you score exactly 10 points more in the test – that is, the equation $\mu_1 + 10 = \mu_2$. Note that this is again an equation, whereas $\mu_1 \neq \mu_2$ cannot be tested in the same way.



## Looking ahead: applying further useful tests

There is a whole series of further tests we might need, along with their assumptions and how to run them in Python on a pandas dataset. The applications lie in exploratory data analysis (how is a variable distributed?), in data cleaning (where are the outliers? which variables are so strongly correlated that I keep only one of them?), in data analysis (which statistical dependencies can be modelled?) and in prediction (can I express one variable – the target variable – through the others? that is supervised learning).

**Examining one sample**

* Shapiro–Wilk:
  $H_0$: the sample is normally distributed
  Assumption: the sample is iid
  `scipy.stats.shapiro`

**Comparing two samples**

* Pearson correlation:
  $H_0$: the two samples are uncorrelated ($\rho = 0$)
  Assumption: both samples are iid and jointly normally distributed
  `scipy.stats.pearsonr`
* Chi-squared:
  $H_0$: the two samples are independent
  Assumption: the variable under investigation is categorical, with an expected frequency of at least $5$ in every cell of the contingency table
  `scipy.stats.chi2_contingency`

## Digression: could a poll have answered the five-per-cent question?

:::{note}
**Digression (not part of the course proper):** an application of the section *From the sample to the population* to a question everybody was asking in February 2025.
:::

In the German federal election of 23 February 2025 the Bündnis Sahra Wagenknecht won $4.981\,\%$ of the second votes (the party vote). It was [9,529 votes](https://www.bundeswahlleiterin.de/info/presse/mitteilungen/bundestagswahl-2025/29_25_endgueltiges-ergebnis.html) (in German) short of entering the Bundestag, out of some 49 million. In the last week before the election [twelve polls](https://www.wahlrecht.de/umfragen/) (in German), each with 1000 to 2500 respondents, had put the BSW between $4$ and $6\,\%$. Afterwards, the polls were said to have got it wrong. Had they?

Let us check with the recipe. With $n$ respondents, a proportion $\hat p = 0.05$ has standard error $\sqrt{\hat p (1 - \hat p)/n}$:

```python
import numpy as np
p = 0.05
for n in [1000, 2000]:
    se = np.sqrt(p * (1 - p) / n)
    print(n, "respondents: standard error", round(100 * se, 2), "points,",
          "95% interval ±", round(196 * se, 2), "points")
```

```
1000 respondents: standard error 0.69 points, 95% interval ± 1.35 points
2000 respondents: standard error 0.49 points, 95% interval ± 0.96 points
```

So a poll with $2000$ respondents that reports $5\,\%$ is saying: somewhere between $4$ and $6$. All twelve polls lay in that range, and so did the election result. None of them "got it wrong"; they answered a question nobody had asked, namely whether the BSW stood at three per cent or at seven. The question people were asking was whether it lay above or below $5.000\,\%$, with a true value of $4.981\,\%$. To resolve two hundredths of a point the interval would have to shrink to $\pm 0.02$ points, and because it shrinks only with $\sqrt{n}$ that would take

$$
n \geq \left( \dfrac{1.96 \cdot \sqrt{0.05 \cdot 0.95}}{0.0002} \right)^2 \approx 4.6 \text{ million respondents},
$$

almost one in every ten eligible voters. That is no longer a poll, that is an election.

The recipe gives only the *lower* bound on the uncertainty, the pure sampling error. On top of that comes everything that violates the random-sample assumption: the people who answer the telephone or sit in an online panel are not a random selection of the electorate, so the institutes weight the raw data by age, region and past voting behaviour, each by its own method. Someone who says "BSW" on Tuesday may vote differently on Sunday, or not at all. And the question is "Who would you vote for if there were an election on Sunday?", not "Who did you vote for?". The spread from $4$ to $6$ between the institutes in the same week is partly sampling error and partly these differences of method, and the two can only be told apart once you know how the institute weighted. That is exactly the context without which the number "5%" is not yet a datum.

What this leaves for reading polls is this: a value without an error statement is incomplete; the error statement for $1000$ respondents and small parties is about $\pm 1.4$ points; and a question whose answer is finer than that interval cannot be answered by any poll, however reputable the institute.
