# Statistical tests

Exploratory data analysis brings us to hypotheses about which relationships are hidden in the data. When we implement systems with machine learning we have to make a great many decisions: whether we may treat a variable as normally distributed, say, or whether the distribution for two groups or clusters is roughly the same or very different.

Tests appear here in two quite different roles, and it helps to keep them apart. In **exploratory analysis** they are one tool among many and answer questions such as "Is this attribute normally distributed?", "Do samples A and B have the same distribution for this attribute? The same mean?" – the answer then decides the next step of the analysis, for instance whether a method that presupposes normality may be used at all. In **communicating results**, by contrast, they are the argument itself: "The test shows that the groups have different distributions, so we use a mixture model" (see [Expectation Maximization](expectation-maximization.ipynb)). In the first role you may test generously, in the second you may not – why that is, is settled by the section [Significance](#signifikanz) at the end of this chapter.

Strictly speaking, statistical tests do not belong to the field of "machine learning", but in the running order of the lecture course they fit nicely here.

A test can be read as an estimator that estimates not a single value but a whole range of possible values, followed by a decision rule that interprets the estimate with respect to a hypothesis. Before we treat the subject superficially – just far enough to judge what a test might achieve, and where the limits of statistical tests lie – we look at what the difference between single values and ranges of values means for communicating scientific results, or data science results.

## Prediction intervals

By way of motivation we look at the figure {ref}`warming-without-confidence` and then relate it to {ref}`warming-with-confidence`


```{figure} images/global_warming_without_confidence.png
:width: 280px
:align: center
:name: warming-without-confidence

Global warming, projection (A2r scenario at 970 ppmv, IIASA 2009)
```

Shown is the projection of a statistical model for predicting global warming (given here as the temperature change relative to the pre-industrial level, which is defined as the mean temperature of the years 1850 to 1900), on the assumption that the CO2 content of the atmosphere rises to 970 ppmv (parts per million by volume) (compare 30 May 2022: 421 ppmv, and 1900: 296 ppmv).
Context: the Paris climate agreement fixes a limit of 1.5°C or 2°C – not by 2040, but by 2100.

Let us look at this figure with data science eyes: what is there to criticise about it?

A common objection to models and figures of this kind is that things could turn out this way, but just as easily quite differently, since after all these are only theoretical models. The figure expresses a great certainty about the course of the curve that cannot possibly be there – which makes the claim "this is how it will be" implausible from the outset. Granted: what is meant to be communicated is "this is how it could be", but on its own that is about as useful as "it might rain or it might stay dry".

To be able to make decisions on the basis of a statistical prediction, we also have to know how plausible the prediction is. For comparison, look at {ref}`warming-with-confidence`, a figure from the IPCC report SR15, Summary for Policymakers, Figure 1 a) {cite}`sr15`:

```{figure} images/global_warming_with_confidence.png
:width: 480px
:align: center
:name: warming-with-confidence

Global warming, projection (IPCC SR15, Fig. 1)
```

To read this figure properly we also need to know the *IPCC Calibrated Language*, strictly speaking the *Likelihood scale* (AR4 and AR5 here refer to the 'assessment reports' that appeared before the special report on 1.5°C):

```{figure} images/likelihood-scale.png
:width: 560px
:align: center
:name: likelihood-scale

The *Likelihood scale* of the IPCC Calibrated Language {cite}`sr15`.
```

Now we see that the grey shaded area is the area in which the actual measurements will lie with probability at least $2/3$ (according to the model). With that information one can judge far better which future warming is to be expected, even if we 'get lucky', and also how bad it could get if we 'are unlucky'. Strictly speaking, the grey shaded area is a **prediction interval**: the range in which the actual future value is presumed to lie with high probability. Closely related is a **confidence interval** for a parameter: an interval computed from the sample and constructed so that in (say) 95% of all samples it covers the true parameter.

For the mathematical theory of set estimators and confidence intervals we refer you to lectures on statistics. In what follows our aim is above all to understand the notion of a test well enough to judge whether a claimed interpretation of a statistical test is serious. Once we can do that, we also want to be able to identify the situations in which a hypothesis test can deliver useful insight. For that it will be above all important to discuss the notion of significance.


## From the sample to the population

Before we define tests, let us be clear about what we actually want. Every summary measure from the exploratory analysis – mean, proportion, median, correlation coefficient – is computed on a **sample**. What we are interested in is the **population** the sample came from: all passengers, all customers, all the measurements one could have made. A different sample would have yielded a different number. Inferring from the sample to the population therefore always consists of three steps:

1. **Estimate:** compute the summary measure from the sample (the proportion, the mean, the difference of two means).
2. **State the uncertainty:** an interval in which the population's summary measure plausibly lies. A number without an interval is not an inference about the population but a description of the sample.
3. **Decide:** measure the question you had against the interval. "Is the coin fair?" means: does $\frac12$ lie in the interval? "Do women survive more often?" means: does $0$ lie in the interval for the difference?

There are two routes to step 2.

**The standard error.** By the [central limit theorem](normal-distribution.ipynb) the mean of a sample of size $n$ is approximately normally distributed with standard deviation $\sigma/\sqrt{n}$, the *standard error*. In $95\,\%$ of samples the population mean then lies in the interval

$$
\texttt{mean}(x) \pm 1.96 \cdot \dfrac{\sigma}{\sqrt{n}},
$$

where one replaces $\sigma$ by the sample standard deviation. For a proportion $\hat p$ we have $\sigma = \sqrt{\hat p(1-\hat p)}$. Coin-toss example: with $45$ successes in $100$ tosses, $\hat p = 0.45$ and the standard error is $\sqrt{0.45 \cdot 0.55/100} \approx 0.05$, so the interval is roughly $[0.35,\ 0.55]$. The $\frac12$ lies inside it, so the coin could be fair. To reject that, the interval would have to become narrower, and it shrinks only with $\sqrt{n}$: for an interval of half the width you need four times the sample. (With the cruder Chebyshev inequality instead of the normal approximation one arrives at an interval of $\pm 0.22$ and a required sample of over $2000$ tosses; that calculation is in the section looking ahead, below.)

**The bootstrap.** For summary measures that have no formula, or whose formula one does not know, one pretends that the sample is the population: one draws from it, *with replacement*, a new sample of the same size, computes the measure, and repeats that many thousands of times. The spread of these bootstrap measures is an estimate of the spread of the measure across real samples, and the $2.5$ and $97.5$ percentiles give a 95% interval. With the arrays `survived` and `sex` from the chapter [Titanic EDA](titanic-eda-numpy.ipynb):

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

**What the recipe assumes.** Both routes assume that the sample is a *random sample* from the population, that is, that every row of the population had the same chance of ending up in the sample. The Titanic list is that for exactly one population: the passengers of that ship (and even there only the Kaggle extract). About other shipping disasters the interval says nothing, however narrow it is. Anyone who runs a survey on campus and wants to infer something about all students has the same problem, and no sample size in the world cures it.

A statistical **test**, the subject of this chapter, is step 3 in formalised form: a rule fixed in advance that decides, from the sample, whether a hypothetical value is still plausible. The z-test and the t-test below are precisely the standard-error calculation from above, only read the other way round: instead of asking whether $\mu_0$ lies in the interval around $\texttt{mean}(x)$, they ask how many standard errors $\texttt{mean}(x)$ is away from $\mu_0$.

## Looking ahead: confidence intervals

:::{note}
**Looking ahead (not part of the course proper):** this section and the two sections *From set estimator to test* and *Best simple tests* are background for a better understanding of statistical tests. They explain where the tests come from, and taken on their own they are not part of the course proper. Anyone who skips them can read straight on at the section *Tests* and then at *The z-test*.
:::

:::{admonition} Definition
Let $(\mathcal{X}, P_\theta : \theta \in \Theta)$ be a statistical model, $\Sigma$ an arbitrary set and $\tau \colon \Theta \to \Sigma$ a quantity to be estimated that depends on the parameter $\theta$. Let $0 < \alpha < 1$ be a real number.
A map $C \colon \mathcal{X} \to \mathcal{P}(\Sigma)$ that assigns to every possible observation $x \in \mathcal{X}$ a set $C(x) \subseteq \Sigma$ is called a **confidence region for $\tau$ at error level $\alpha$** if

$$
\inf_{\theta \in \Theta} P_{\theta}\left( x \in \mathcal{X} \colon \tau(\theta) \in C(x) \right) \geq 1 - \alpha.
$$

If in addition $\Sigma = \mathbb{R}$ and every $C(x)$ is an interval, one speaks of a **confidence interval**.
:::

:::{admonition} Example
**The trivial case:**
The constant confidence region $C(x) := \Sigma$ always satisfies $\tau(\theta) \in C(x)$ for every $\theta$, so $P_\theta\left(x \in \mathcal{X} : \tau(\theta) \in C(x)\right) = 1 \geq 1 - \alpha$ for every $\alpha$.
We can read this as: we are certain that the 'right' estimate lies in the range of $\tau$.
Of course this is not a particularly useful confidence region, but it makes clear that the region is quite allowed to be 'too big'. It is in our interest to find a $C$ for which the $C(x)$ are as small as possible, because only then does the statement become interesting.
:::

:::{admonition} Example
**Coin toss:**
The $n$-fold repeated toss of an unfair coin with success probability $p$ can be modelled with the **binomial model** (see [The most important discrete distributions](important-discrete-distributions.ipynb)): $\mathcal{X} = \{0,\dots,n\}$ is the number of successes, the unknown parameter is $\theta = p \in \Theta = [0,1]$ and $P_\theta = \operatorname{Bin}(n,\theta)$ (and $\tau = id$, so we are estimating the parameter $\theta$ itself).

We have already computed the maximum likelihood estimator for $\theta$ there: $\hat\theta = \frac{x}{n}$, the proportion of successes. Concretely: if we toss the coin $100$ times and get tails $45$ times, we estimate $\theta$ as $\frac{45}{100}$ (and in particular that the coin really is unfair).
:::

But what is our confidence (our trust)? Do we also regard values far away from $\frac{x}{n}$ as halfway plausible, or can we pin down a very narrow range around $\frac{x}{n}$ that we hold to be plausible? In the concrete example with the estimate $\theta = \frac{45}{100}$, would $\theta = \frac{1}{2}$ also be halfway plausible?

What we now want is to construct intervals $C(x) = (\frac{x}{n} - \epsilon, \frac{x}{n} + \epsilon)$ with $\epsilon > 0$ as small as possible such that the confidence-region condition from the definition is satisfied:

$$
\begin{aligned}
 & \inf_{\theta \in \Theta} P_{\theta}\left( x \in \mathcal{X} \colon \tau(\theta) \in C(x) \right) \geq 1 - \alpha \\
 \Leftrightarrow & \inf_{\theta \in [0,1]} P_{\theta}\left( x \in \mathcal{X} \colon \left|\theta - \frac{x}{n}\right| < \epsilon \right) \geq 1 - \alpha \\
  \Leftrightarrow & \inf_{\theta \in [0,1]} P_{\theta}\left( x \in \mathcal{X} \colon \left|\theta - \frac{x}{n}\right| \geq \epsilon \right) \leq \alpha \\
\end{aligned}
$$

Translated: $\epsilon$ is to be determined (as a function of $\alpha$, and as small as possible) so that $\left|\theta - \frac{x}{n}\right| \geq \epsilon$ holds for fewer than a proportion $\alpha$ of the possible samples $x$. If $\alpha = 0.05$ concretely (a common choice), that means our estimation error exceeds $\epsilon$ in only 5% of samples.

The shape of the inequality may remind us of Chebyshev's inequality, which we looked at right after introducing the variance. Here, for the estimator $T(x) = \frac{x}{n}$, it tells us

$$
 P_{\theta}\left( \left|\mathbb{E}(T) - T\right| \geq c \right) \leq \dfrac{\mathbb{V}T}{c^2}
$$

Naturally we would like to use $c=\epsilon$, and to choose $\epsilon$ as a function of $\alpha$ in such a way that nothing but $\alpha$ is left on the right-hand side of the inequality. We have $\mathbb{V}T = \mathbb{V}\!\left(\frac{x}{n}\right) = \frac{\theta(1-\theta)}{n}$, which annoyingly still depends on $\theta$ – which is exactly what we do not know!

So we bound $\theta(1-\theta) \leq \frac{1}{4}$ (clear enough: at $\theta = \frac{1}{2}$ there is equality, otherwise the inequality is strict).

All in all we obtain: $\epsilon$ is well chosen if

$$
\begin{aligned}
           & \dfrac{\mathbb{V}T}{\epsilon^2} \leq \alpha \\
\Leftarrow & \frac{1}{4 n \epsilon^2} \leq \alpha \\
\Leftrightarrow & \frac{1}{4 n \alpha} \leq \epsilon^2 \\
\Leftrightarrow & \frac{1}{2 \sqrt{n \alpha}} \leq \epsilon \\
\Leftarrow & \frac{1}{2 \sqrt{n \alpha}} =: \epsilon.
\end{aligned}
$$

In the concrete example with $\alpha = 0.05$ and $n=100$, then, $\epsilon := \frac{1}{2\sqrt{5}} \approx 0.2236$ meets our wishes.
For us that means: for the concrete observation $k=45$ it is not only the point estimate $\frac{45}{100}$ that is plausible; we also regard roughly $\frac{23}{100}$ and $\frac{67}{100}$ as plausible. So the coin could well be fair and we have merely caught an unlucky observation.

This shows us that determining confidence intervals with Chebyshev's inequality yields very large intervals. There are several better (considerably more complicated!) methods for obtaining smaller intervals.

But we also see a simple relationship between $\epsilon, n$ and $\alpha$: if we make $\alpha$ smaller (that is, want to be even more certain), $\epsilon$ gets bigger. If we make $n$ bigger (that is, take larger samples), $\epsilon$ gets smaller.

With that one can compute, for instance, how large the sample has to be in order to say with certainty at least $1-\alpha$ that our coin is not fair. Again we assume concretely that for one sample we have estimated $\theta = 0.45$.

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

putting in $\alpha = 0.05$, it follows that the sample should be larger than $2000$ in order to be able to reject that the coin is fair. If we had a cleverer procedure for determining smaller confidence intervals, a smaller sample would suffice.



:::{admonition} Example
**A sample from a normal distribution:**
Suppose the real-valued random variable $Z$ is normally distributed with unknown expected value $\mu$ and unknown variance $\sigma^2$.
We sample $Z$ independently and identically distributed $n$ times and obtain a random variable $X$ with values in $\mathbb{R}^n$, that is $X = (X_1,\dots,X_n)$, where $X_i \sim Z$.

We write $\texttt{mean}(X) = \sum_{i=1}^n \frac{X_i}{n}$ for the sample mean (careful: this is now a random variable, computed from the random sample $X$) and $S^\ast(X)^2 := \frac{1}{n-1} \sum_{i=1}^n (X_i - \texttt{mean}(X))^2$ for the sample variance (with the Bessel correction, i.e. $n-1$ in the denominator, so that there is no bias).
:::

We now want to know how well we can estimate $\mu(Z)$ with $\texttt{mean}(X)$ – where does our confidence (our trust) lie?

The random variable $\texttt{mean}(X)$ is normally distributed, with mean $\mu(Z)$ and standard deviation $\dfrac{\sigma(Z)}{\sqrt{n}}$.
The estimation error, measured in the 'unit' standard deviation of $\texttt{mean}(X)$, is

$$
\dfrac{\texttt{mean}(X) - \mu(Z)}{\sigma(Z)/\sqrt{n}}
$$

and that is therefore standard normally distributed. This quantity still has the problem that we do not actually know $\sigma(Z)$, while we would nonetheless like to look at the error of our estimate of $\mu(Z)$. So we have to replace $\sigma(Z)$ by our estimate $S^\ast(X)$.

The random variable 'sample variance' $S^\ast(X)^2$ is distributed in such a way that $\dfrac{n-1}{\sigma(Z)^2} S^\ast(X)^2$ follows a so-called **$\chi^2$ distribution** with $n-1$ degrees of freedom (a special case of the gamma distribution).

The probability density function of the $\chi^2$ distribution is of no concern to us at the moment (and in particular is not part of the course proper); for the sake of completeness:

$$
f(x) = \dfrac{1}{2^{\frac{k}{2}} \Gamma\left( \frac{k}{2} \right)} x^{ \frac{k}{2}-1}e^{-\frac{x}{2}}
$$


```{figure} images/chi-squared-distributions.png
:width: 420px
:align: center
:name: chiquadrat

Chi-squared distributions with various parameters (degrees of freedom)
```

The difference between the estimated mean and the actual expected value, measured in the 'unit' sample standard deviation, is the estimated estimation error $T$, a statistic that we now consider:

$$
T = \dfrac{\texttt{mean}(X) - \mu(Z)}{S^\ast(X)/\sqrt{n}}.
$$

The random variable $T$ follows a so-called **Student t distribution**, which at first glance at least resembles a normal distribution but has heavier *tails*, that is, takes values further from the expected value with higher probability. The only parameter of a Student t distribution is the number of degrees of freedom $\nu > 0$, here $\nu = n-1$. For $\nu$ at least $3$ the expected value is $0$ and the variance $\nu / (\nu - 2)$.

The probability density function of the Student t distribution is not that important for us to begin with; for the sake of completeness, here is what it looks like:

$$
f(t) = \dfrac{1}{\sqrt{\nu} B\left(\frac{1}{2}, \frac{\nu}{2}\right)} {\left( 1 + \dfrac{t^2}{\nu} \right)}^{-\frac{(\nu+1)}{2}}
$$

where $B(x,y) = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$ is the beta function, and the gamma function $\Gamma$ is defined on all of $\mathbb{R}$ and interpolates $\Gamma(n+1)=n!$ in such a way that $\Gamma(x)x = \Gamma(x+1)$ always holds (which we may promptly forget again).

As $n \to \infty$ the Student t distribution converges to the standard normal distribution. So the deviation of the t distribution from a normal distribution encodes exactly the uncertainty that comes with a small sample size.

```{figure} images/student-t-distributions.png
:width: 420px
:align: center
:name: studentt

Student t distributions with various parameters (degrees of freedom)
```

We are now interested in where the probability of a large estimation error
$T = \dfrac{\texttt{mean}(X) - \mu(Z)}{S^\ast(X)/\sqrt{n}}$
is small. Now this estimation error does not depend on $\mu(Z)$; more precisely, $T$ is independent of $\mu(Z)$. That may be counter-intuitive, because $\mu(Z)$ appears in the formula, but it is true all the same. One says that the statistic is **distribution-free**.

For a given $\alpha$ we now choose $t$ as the $(1-\frac{\alpha}{2})$-*quantile* of the $t$ distribution with $n-1$ degrees of freedom, that is, the number $t > 0$ with $P(T \leq t) = 1 - \frac{\alpha}{2}$; by the symmetry of the distribution we then have $P(|T| \leq t) = 1 - \alpha$. This used to be looked up in tables; today we use a computer (`scipy.stats.t.ppf(1 - alpha/2, n - 1)`).
Then, with $\epsilon := t\frac{S^\ast(x)}{\sqrt{n}}$, a confidence interval for $\mu(Z)$ is given by

$$
C(x) = (\texttt{mean}(x) - \epsilon, \texttt{mean}(x) + \epsilon).
$$

So we see that things can get complicated quickly when one wants to construct a confidence region. On the other hand the procedure described here (with the standardisation and the quantile transformation) carries over to other situations as well (which we would rather leave to the statisticians).

With the approximation of the binomial distribution by a normal distribution and the method discussed here for arriving at confidence intervals for a normal distribution, one can also find better confidence intervals for a binomial distribution – although more complicated procedures again yield considerably better intervals.

It should be enough for us that we now know where the $\chi^2$ distribution and the Student t distribution come from, and with that we may forget the concrete probability density again – fortunately the statisticians have worked it out for us and implemented it in our Python packages. What matters above all is that the naive assumption that the estimation error is again normally distributed does not hold in general. We will meet these distributions again in the discussion of statistical tests, which in a sense build on the construction of confidence intervals.


## Tests

:::{admonition} Definition
Let $(\mathcal{X}, P_\theta : \theta \in \Theta)$ be a statistical model and $\Theta = \Theta_0 \cup \Theta_1$ a disjoint decomposition of the parameter space into the **null hypothesis** $\theta \in \Theta_0$ and the **alternative** $\theta \in \Theta_1$.
Every statistic $\phi \colon \mathcal{X} \to [0,1]$ (which we read as a decision rule) is called a **test** of $\Theta_0$ against $\Theta_1$.
A test is called **non-randomised** if $\phi(x)=0$ or $\phi(x)=1$ for all $x \in \mathcal{X}$, and **randomised** otherwise.
:::

:::{admonition} Example
**Weighing apples.** A supplier promises apples of at least $150\,\mathrm{g}$ on average; we assume the weights to be normally distributed and weigh a sample $x$. Three tests for the same sort of question:

1. $\Theta_0 = (-\infty, 150]$ ("the apples weigh at most $150\,\mathrm{g}$ on average"), $\Theta_1 = (150, \infty)$. One test: $\phi(x) = 1$ if $\texttt{mean}(x) > 150$, otherwise $0$.
2. The same hypothesis, but a more cautious test: $\phi(x) = 1$ only once $\texttt{mean}(x) > 160$. It rejects less often, so it errs less often when $\Theta_0$ is true, and overlooks more often when $\Theta_1$ is true.
3. $\Theta_0 = \{150\}$ ("exactly $150\,\mathrm{g}$"), $\Theta_1 = \mathbb{R} \setminus \{150\}$. One test: $\phi(x) = 0$ if $150$ lies in the interval $\texttt{mean}(x) \pm 1.96\,\sigma/\sqrt{n}$ from the section *From the sample to the population*, otherwise $1$.

The next definition gives names to the two errors from version 2; version 3 is the z-test from below.
:::

:::{admonition} Definition
The probability of a **type I error**, meaning rejection of the null hypothesis (that is, $\phi(x)=1$) even though the true parameter is $\theta \in \Theta_0$, is $\sup_ {\theta \in \Theta_0} \mathbb{E}_\theta(\phi)$ and is also called the **effective level** of the test.
For an $\alpha$ greater than or equal to the effective level one also speaks of a test of level $\alpha$.

The function $G_\phi \colon \Theta \to [0,1]$ given by $G_\phi(\theta) = \mathbb{E}_\theta(\phi)$ is called the **power function** of the test.
$1 - G_\phi(\theta)$ is the probability of a **type II error**, meaning acceptance of the null hypothesis (that is, $\phi(x) < 1$) even though the true parameter is $\theta \in \Theta_1$.
For $\theta \in \Theta_1$, $G_\phi(\theta)$ is also called the **power** of $\phi$ at $\theta$.
:::

In the apple example the test with threshold $160$ has a smaller effective level, but also less power than the one with threshold $150$.

:::{admonition} Definition
A test $\phi$ is called a **uniformly best test at level $\alpha$** if it is of level $\alpha$ and every other test of level $\alpha$ has smaller or equal power.
:::

So such a uniformly best test has at most probability $\alpha$ of a type I error and, among all such tests, the smallest probability of a type II error.


## Looking ahead: from set estimator to test

:::{note}
Looking ahead, not part of the course proper (see the note at *Confidence intervals*).
:::

We already saw, when discussing a confidence interval for the binomial model, that this can help us reach a decision (concretely: should I regard a coin with $45/100$ successes as 'unfair', or is the deviation from $50/100$ explained by a sampling error? Or indeed: how many further samples do I need to settle this question unambiguously?)

One can systematise this relationship and, using the vocabulary of the shape parameter, construct a set estimator from any test. Here we look only at the other direction, namely how a test is constructed from a set estimator.

The starting point is to be (for simplicity) a parametric statistical model $(\mathcal{X}, P_\theta : \theta \in \Theta)$ and an interval estimator (i.e. a confidence interval at level $1-\alpha$) $C \colon \mathcal{X} \to \mathcal{P}(\Theta)$ for the parameter $\theta$. In addition we have a hypothetical parameter value $\theta_0 \in \Theta$ which does *not* come from the data but from another source: for instance $\theta_0 = \frac{1}{2}$ for the claim 'the coin is fair', or a value from the literature or from an earlier experiment.

The hypothesis is now that $\theta_0$ is the true parameter.
While it is clear that in the strict sense this hypothesis is probably always false, we are nevertheless interested in when the hypothesis can be rejected with *certainty*. So we set $\Theta_0 := \{\theta_0\}$ and $\Theta_1 := \Theta - \{\theta_0\}$.

From this we construct the test $T_C \colon \mathcal{X} \to [0,1]$ by

$$
T_C := 1_{\{ x \in \mathcal{X} | \theta_0 \notin C(x) \}} \text{ (indicator function)} 
$$

$$
T_C(x) = \begin{cases} 0 & \theta_0 \in C(x) \\ 1 & \theta_0 \notin C(x) \end{cases}
$$

The procedure is thus: from the data $x \in \mathcal{X}$ we compute the confidence interval $C(x)$ and ask whether $\theta_0$ lies in it. If it does, we hold on to the hypothesis '$\theta_0$ is the true parameter'; otherwise we conclude '$\theta_0$ cannot be the true parameter'. Since $C$ is a confidence interval at level $1-\alpha$, we have $P_{\theta_0}(\theta_0 \notin C(x)) \leq \alpha$, so the test $T_C$ has level $\alpha$.

What matters is that $\theta_0$ was not itself estimated from the same data: a point estimator $\hat{\theta}(x)$, the midpoint of $C(x)$ say, always lies in $C(x)$, and the test would then never reject. The test is interesting precisely when we have an independent source for $\theta_0$, for example when we ask whether the data are uniformly or normally distributed, or not.

## Looking ahead: best simple tests

:::{note}
Looking ahead, not part of the course proper (see the note at *Confidence intervals*).
:::

We have already seen the definition of level and power, and the usual procedure of looking for the most powerful test at a fixed level.

:::{admonition} Definition
If there are only two possible parameters (one speaks of **simple hypotheses**), that is $\Theta_0 = \{\theta_0\}$ and $\Theta_1 = \{\theta_1\}$,
and $f_0$ and $f_1$ are the density functions of the distributions belonging to these parameters, then

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

Why is $R(x)$ called the likelihood ratio? Because $f_1(x)$ is a measure of the probability $P(D|H_1)$ and $f_0(x)$ is a measure of the probability $P(D|H_0)$, so $R$ is the ratio of the likelihoods. If $f_0(x)=0$, one simply sets $R = \infty$.

The case $R(x) = c$ usually has probability $0$, but it can also be handled separately (with a suitable value for $\phi(x)$ between $0$ and $1$).

The **Neyman–Pearson lemma** says that for every simple hypothesis (that is, $\Theta$ with two elements) and every level $\alpha$ there is a Neyman–Pearson test (i.e. a suitable $c \in \mathbb{R}$) that exhausts the level fully (i.e. has effective level $\alpha$), and that every such test is a uniformly best test at level $\alpha$.

**Stein's lemma** says something about how useful additional samples are for making a test more informative. Fix a level $\alpha$. For a series of observations with, for each $n$, a Neyman–Pearson test $\phi_n$ of level $\alpha$ that depends only on the first $n$ observations, the power of $\phi_n$ tends to $1$ as the observations accumulate (that is, as $n \to \infty$), and does so at exponential speed. More precisely:

$$
\lim_{n \to \infty} \frac{1}{n} \log\left( 1 - \mathbb{E}_1(\phi_n) \right) = -H(P_0 \Vert P_1)
$$

So the higher the relative entropy $H(P_0 \Vert P_1)$ of the two possible distributions, the more power each single additional sample delivers.

The connection lies in the definition of Neyman–Pearson tests and of relative entropy – the expression $-f_0(x) \log R(x) = f_0(x)\log \left( \frac{f_0(x)}{f_1(x)} \right)$ occurs in the definition of the continuous relative entropy.

The take-home message is: for simple hypotheses there are always best tests, and relative entropy lets us quantify how we can push down the probability of a type II error by enlarging the sample.

## The z-test

If you have data whose individual data points are independent (and identically distributed) – a sample of a random variable, say – that follow a normal distribution, and you know the standard deviation $\sigma$, then you can do a **z-test** (also **Gauss test**). It is the 'simpler' variant of the t-test (see below). If you do not know $\sigma$ and put in the sample standard deviation, that is still defensible for large $n$, because the t distribution is then practically a normal distribution; the widespread rule of thumb "$n > 30$" is as crude for this as described in the chapter [The normal distribution](normal-distribution.ipynb) under *The "$N \ge 30$" myth*.

In this test one wants to find out whether a sample $x$ follows a normal distribution with mean $\mu_0$. For $\mu_0 = \texttt{mean}(x)$ (the maximum likelihood estimator) there is nothing to test – we conclude at once that $\mu = \mu_0$ is plausible. But what about values $\neq \texttt{mean}(x)$? Suppose our sample *almost* follows a standard normal distribution – then it would make sense to run a test of whether the hypothesis of a standard normal distribution should be accepted or rejected, even if the maximum likelihood estimator estimates something other than $0$ for $\mu$.

The **z-statistic** is

$$
Z(x) = \dfrac{\texttt{mean}(x) - \mu_0}{\sigma/\sqrt{n}}
$$

In the z-test, $\sigma$ is treated as known; for large samples one puts the sample standard deviation $\sigma^\ast(x)$ in its place. What is unknown is $\mu$, and the null hypothesis reads $H_0$: $\mu = \mu_0$. In the t-test below, by contrast, $\sigma$ is treated as unknown, and the estimation error incurred in estimating $\sigma$ is accounted for in the distribution of the test statistic.
The random variable $Z$ is standard normally distributed.

In a two-sided z-test the null hypothesis is $H_0 := (\mu = \mu_0)$, which corresponds to $\Theta_0 = \{\mu_0\}$, and the alternative is $H_1 = (\mu \neq \mu_0)$, which corresponds to $\Theta_1 = \mathbb{R} \setminus \{\mu_0\}$.

We choose a level $\alpha$, for example $\alpha = 0.05$.
Since we want a two-sided test, we look at the z-value of $1 - \alpha/2$ (from a table of z-values, say, or with the quantile function `scipy.stats.norm.ppf(1 - alpha/2)`). For $\alpha = 0.05$ the z-value is $\pm 1.96$.
The z-value $z(p)$ is the $p$-quantile of a standard normal distribution, so $P(Z \leq z(p)) = p$,
here concretely $P(Z \leq 1.96) = 0.975$.
Since the standard normal distribution is symmetric, $P(Z \geq -1.96) = 0.975$ and $P(-1.96 \leq Z \leq 1.96) = 0.95$ hold as well.

So we compute the z-statistic of our sample and compare the result with the z-value $1.96$. If we are in between, that is $-1.96 \leq Z(x) \leq 1.96$, then we cannot reject the null hypothesis (which does not mean that we accept it, see [Significance](#signifikanz) below). If the z-statistic lies outside $[-1.96, 1.96]$, we reject the hypothesis.

## The Student t-test

The two tests compared:

| | z-test | t-test |
|---|---|---|
| $\sigma$ | known (for large $n$: $\sigma^\ast(x)$ put in) | unknown, estimated along the way |
| distribution of the statistic under $H_0$ | standard normal distribution | Student t distribution with $n-1$ degrees of freedom |
| when | $\sigma$ known, otherwise only for large $n$ | always; for large $n$ practically the same test |
| SciPy | `norm.ppf` | `t.ppf`, `ttest_1samp` |

With small samples the bias of the estimated parameters of a normal distribution makes itself felt, and one has to work with the actual distribution of the **t-statistic**. So if $\mu_0$ is the parameter one wants to test for, one considers

$$
t(x) = \dfrac{\texttt{mean}(x) - \mu_0}{\sigma^\ast(x)/\sqrt{n}}
$$

Here $\sigma^\ast(x)$ is the unbiased estimator for $\sigma$.

As discussed earlier in the construction of confidence intervals, $t$ follows a Student t distribution. To carry out the test at a level $\alpha$ we therefore have to look up the t-value for that level in a table, or compute it with Python via `scipy.stats.t.ppf(p, n-1)` (ppf is the **percent point function**, which gives us the p-quantile of the t distribution with $n-1$ degrees of freedom).

We compute the t-statistic on the data $x$ and compare it with the previously computed 'critical' t-value. If the t-statistic lies between $\pm$ the critical t-value, we cannot reject the hypothesis (that $\mu_0$ is the expected value of the distribution); if it lies outside, we reject it.

We can also have SciPy compute this two-sided t-test directly:
`scipy.stats.ttest_1samp(x, mu)`

Strictly speaking this t-test can do more: instead of comparing the distribution of $x$ with a normal distribution with mean $\mu$ and the same variance as $x$, we can also compare two samples $x,y$ (which need not be of equal size) as to whether their means agree (on the assumption that both samples are normally distributed with equal variance, and that the two samples are independent of each other) with `scipy.stats.ttest_ind(x, y)`. Of this, $y = \texttt{mu}$ is a special case (but the call with $y$ substituted will only return `NaN`s – because the variance of a one-element sample is $0$; hence `ttest_1samp`).

The return value of `scipy.stats.ttest_1samp(x, mu)` is a `TtestResult` object with the attributes `statistic`, `pvalue` and `df` (the number of degrees of freedom, that is $n-1$) as well as the method `confidence_interval(level=0.95)`. (Older SciPy versions returned a `namedtuple` with only `statistic` and `pvalue`; those two attributes are unchanged.)
The return value `statistic` is the computed t-statistic (since no $\alpha$ was involved yet, one would still have to compare it by hand with the critical t-value to arrive at the test result).
The return value `pvalue` is the **p-value** (also: the **significance**) of the test result, that is, the probability, under $H_0$, of observing a test statistic at least as extreme as the one actually observed – so for the two-sided test $p = P(|T| \geq |t_{\text{obs}}| \,|\, H_0)$. In particular the p-value is *not* the probability of the concrete observation (which for continuous distributions would always be $0$), nor the probability $P(H_0 | D)$ that the null hypothesis is true.
The name comes from 'probabilitas', and the word 'significance' naturally raises certain associations.
If $p < \alpha$ we reject the null hypothesis, otherwise we cannot reject it; that is not the same as accepting it, because a high p-value only says that the sample cannot tell the deviation apart from a sampling error (see the second warning in the section [Significance](#signifikanz) below).

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

The p-value is below $0.05$, so we reject $\mu_0 = 150$; fittingly, the $150$ does not lie in the confidence interval. `confidence_interval()` is exactly the interval from the section *From the sample to the population*, $\texttt{mean}(x) \pm t \cdot \sigma^\ast(x)/\sqrt{n}$, only with the quantile $t = \texttt{t.ppf}(0.975, 39) \approx 2.02$ of the t distribution in place of $1.96$.

For the two-sample case there is in addition the variant that needs only summary measures:
```python
ttest_ind_from_stats(mean1, std1, nobs1,
                     mean2, std2, nobs2,
                     equal_var=True,
                     alternative="two-sided")
```

and `alternative` encodes whether a two-sided or a one-sided (`less` or `greater`) test is to be carried out. The variable `nobs` is the number of observations. If `equal_var` is set to `False`, the assumption of equal variance is dropped, and what is carried out is then not an ordinary t-test but Welch's t-test, in which the number of degrees of freedom is computed differently.

If the basic assumption of equal variance does not hold for two samples, a transformation of the scale (by a logarithm, for instance) can sometimes bring that state about (at least approximately) and so make the t-test useful in these cases too. If the variances differ markedly, you should also keep your hands off the t-test, because it is not informative.

## Looking ahead: ANOVA

A generalisation of the t-test to more than $2$ sample groups is ANOVA, which stands for **Analysis of Variance**. Its assumptions are the same as for the t-test:

* The observations are independent of one another
* The residuals (these are the differences $x_i-\texttt{mean}(x)$, an estimate of the actual sampling error) are normally distributed
* Homoscedasticity – that means homogeneity of variance, that is, that the variances of the sample groups are equal.

It is usually applied to a categorical variable with $k$ levels; one then splits a sample into $k$ groups (according to the level) and considers ANOVA for these groups. If a significant deviation shows up (that is, a p-value smaller than $0.05$), we reject the null hypothesis that the groups have equal expected values – and conclude from that that the categorical variable probably has an influence on the expected value.

If no significant deviation shows up (p-value greater than or equal to $0.05$), then we may well see a deviation between the various means, but only as much as a sampling error already explains well – an influence of the categorical variable cannot be seen this way.

Careful: that does not mean that the categorical variable has no influence on the means! It only means that our sample is not able to tell such an influence apart from a sampling error.
'We know that we know nothing'.

In Python we use `scipy.stats.f_oneway`.

(signifikanz)=
## Significance

Of all the notions in this chapter this is the most important, because it leaves statistics behind and turns up in newspapers, studies and meetings. There it is almost always used as though there were a number behind it. There is not.

:::{admonition} Definition
A result of a statistical test is called **statistically significant** if the sample data deviate from the null hypothesis so strongly that this assumption is rejected according to a rule *fixed in advance*.
:::

:::{admonition} Remark
There is no number in this definition. The rule may be arbitrarily strict or arbitrarily silly; "significant" only says that it was triggered. Whether that means anything can only be judged once you know the rule, the level and the null hypothesis. Anyone who says "the difference is significant" has therefore thought up a context in which that sentence is permitted; without the context the sentence is empty. From now on, use the word the way you use the word "continuous": only in its technical sense.
:::

The usual rule is "$p < \alpha$" with the level $\alpha = 0.05$. That is a convention of the journals, not a constant of nature. It does at least have a justification: a normally distributed quantity deviates from its expected value by more than a shade under two standard deviations ($1.96\,\sigma$) with probability only $5\,\%$, so a result beyond that boundary is "conspicuous". For delicate questions one demands more: $p \leq 0.01$ is called **very significant**, $p \leq 0.001$ **highly significant** (about three standard deviations). Particle physics counts in standard deviations outright and demands five of them for a discovery.

Three warnings belong to the definition:

1. **Rejecting $H_0$ does not mean accepting $H_1$.** The test has only said that the data are improbable under $H_0$; about the alternative it has said nothing, and certainly nothing about whether $H_1$ is the only other explanation.
2. **A high p-value says nothing.** "Not significant" only means that the sample cannot tell the deviation apart from a sampling error. It does not mean that there is no deviation (see the remark on ANOVA above).
3. **Without a cleverly chosen null hypothesis the p-value has no meaning.** Anyone who chooses $H_0$ so that nobody believes it anyway gets a significant result for free. Which hypothesis one formulates as $H_0$ is the subject of the next section.

As a reminder once more: a **type I error** is a false rejection of the null hypothesis. Small p-values thus tempt one into a type I error, and anyone who runs many tests will eventually find a significant one:

```{figure} images/xkcd-significant.png
:width: 300px
:align: center
:name: xkcd-significant

Randall Munroe, [xkcd 882 "Significant"](https://xkcd.com/882/) (CC BY-NC 2.5) (So, uh, we did the green study again and got no link. It was probably a-- "RESEARCH CONFLICTED ON GREEN JELLY BEAN/ACNE LINK; MORE STUDY RECOMMENDED!")
```

For publication in important journals, studies often have to show significant results. That is problematic, because

* significant results too can be entirely accidental (the comic),
* there are tricks for systematically shrinking the p-value without learning anything more about the question (**p-value hacking**, cf. {ref}`pvalue-hacking`): testing many hypotheses and reporting only the significant one, extending the sample until $p$ falls below $0.05$, removing outliers after the fact,
* non-significant results too can be scientifically relevant, but are published less often (**publication bias**),
* the p-value is very often misinterpreted, and not only by students: in the survey of {cite}`haller`, most of the methodology lecturers too got at least one of six statements about the meaning of a significant result wrong.

**Most Published Research Findings Are False**

[Ioannidis JPA (2005) Why Most Published Research Findings Are False.
PLOS Medicine 2(8): e124.](https://doi.org/10.1371/journal.pmed.0020124)

> "the probability that a research finding is indeed true depends on the prior probability of it being true (before doing the study), the statistical power of the study, and the level of statistical significance"

The less plausible the hypothesis (low prior probability), the higher the probability that an exciting finding turns out to be a false alarm, independently of the p-value.

A very important building block for stopping p-value hacking is the pre-registration of studies: hypothesis, level and analysis are fixed before the data are there. That is exactly what the definition above demands with "rule fixed in advance".

```{figure} images/pvalue-hacking.png
:width: 600px
:align: center
:name: pvalue-hacking

[Compilation by Uri Simonsohn, 2015](http://datacolada.org/41)
```

## What to formulate as hypothesis, what as alternative?

The usual procedure is that one formulates the scientific insight one would like to establish as the rejection of the null hypothesis. It makes a difference which statement one formulates as the hypothesis and which as the alternative, because we defined best tests in such a way that the type I and type II errors play different roles – we hold the type I error exactly at the level $\alpha$ and minimise the type II error subject to that constraint.

:::{admonition} Example
Imagine we had found a new drug that we believe makes people cleverer. To show this, we proceed as follows: we construct an experiment with which it can be refuted that our drug makes people cleverer. To that end we operationalise "becoming cleverer" by, say, an examination situation with cognitive tasks. The participants are randomly split into two groups. One group gets a placebo, the other the drug; everything else is the same, and nobody (not even the people running the study) knows who is in which group. Afterwards one analyses the data – performance in the examination is one variable, group membership the other.

The null hypothesis is now: the drug has no effect. The alternative is that the drug makes people cleverer. If we assume performance to be normally distributed, we can run a two-sample t-test. If $p < 0.05$ we reject the null hypothesis, and so conclude that this observation cannot be chance, but that the variable 'group membership' has a significant influence on performance.
:::

If $p < 0.05$, a type I error can of course still occur, because $0.05 \neq 0$.
The null hypothesis was $\mu_1 = \mu_2$, where the $\mu_i$ are the means of the two groups. The alternative is $\mu_1 \neq \mu_2$. In our derivation of the t-test we set up the t-statistic and in doing so compared the mean of the sample with a fixed $\mu_0$. And in that, the roles of hypothesis and alternative cannot be swapped!

One can see this non-interchangeability in the hypothesis formulated in ordinary language too: "the drug has no effect" is really the statement "whether or not you take the drug has no influence on test performance". How does one formalise "has an influence on test performance" mathematically?

What one can do instead is test for an explicitly described relationship, for example the hypothesis that after taking the drug one scores exactly 10 points more in the test, that is, the equation $\mu_1 + 10 = \mu_2$. Note that this is again an equation, whereas $\mu_1 \neq \mu_2$ cannot be tested in the same way.



## Looking ahead: applying further useful tests

We could still need a whole series of tests, and their assumptions, and how to carry them out with Python on a pandas dataset. The applications lie in exploratory data analysis (how is a variable distributed?), in data cleaning (where are the outliers? which variables are so strongly correlated that I keep only one of them?), in data analysis (which statistical dependencies can be modelled?) and in prediction (can I express one variable – the target variable – through the others? that is supervised learning).

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

In the German federal election of 23 February 2025 the Bündnis Sahra Wagenknecht won $4.981\,\%$ of the second votes (the party vote). It was [9,529 votes](https://www.bundeswahlleiterin.de/info/presse/mitteilungen/bundestagswahl-2025/29_25_endgueltiges-ergebnis.html) (in German) short of entering the Bundestag, out of some 49 million. In the last week before the election [twelve polls](https://www.wahlrecht.de/umfragen/) (in German), each with 1000 to 2500 respondents, had put the BSW between $4$ and $6\,\%$. Afterwards it was said that the polls had got it wrong. Had they?

Let us check with the recipe. A proportion $\hat p = 0.05$ has, with $n$ respondents, the standard error $\sqrt{\hat p (1 - \hat p)/n}$:

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

So a poll with $2000$ respondents that reports $5\,\%$ is saying: somewhere between $4$ and $6$. All twelve polls lay in that range, and so did the election result. None of them "got it wrong"; they answered a question nobody had asked, namely whether the BSW stands at three per cent or at seven. The question that was asked was whether it lies above or below $5.000\,\%$, with a true value of $4.981\,\%$. To resolve two hundredths of a point, the interval would have to shrink to $\pm 0.02$ points, and because it shrinks only with $\sqrt{n}$ one would need

$$
n \geq \left( \dfrac{1.96 \cdot \sqrt{0.05 \cdot 0.95}}{0.0002} \right)^2 \approx 4.6 \text{ million respondents},
$$

almost one in every ten eligible voters. That is no longer a poll, that is an election.

The recipe delivers only the *lower* bound on the uncertainty, the pure sampling error. On top of that comes everything that violates the assumption of a random sample: whoever answers the telephone or sits in an online panel is not a random selection of the electorate, and the institutes therefore weight the raw data by age, region and past voting behaviour, each by its own method. Someone who says "BSW" on Tuesday may vote differently on Sunday, or not at all. And the question is "Who would you vote for if there were an election on Sunday?", not "Who did you vote for?". The spread from $4$ to $6$ between the institutes in the same week is partly sampling error and partly these differences of method; the two can only be told apart once you know how the institute weighted. That is exactly the context without which the number "5%" does not become a datum.

What remains for reading polls is this: a value without an error statement is incomplete, the error statement for $1000$ respondents and small parties is about $\pm 1.4$ points, and a question whose answer is finer than that interval cannot be answered by any poll, however reputable the institute.
