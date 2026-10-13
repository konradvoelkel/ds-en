# Continuous distributions

:::{admonition} Definition
Let $X \colon \Omega \to \mathbb{R}$ be a random variable, that is, let $\Omega$ be a probability space (a set $\Omega$ together with a probability measure $P_\Omega$) and let $X$ be a map such that $P(X \in A) := P_\Omega(X^{-1}(A))$ is defined for all events $A \subseteq \mathbb{R}$.

If $\Omega$ is not a discrete probability space (because $\Omega$ is uncountably infinite, say $\Omega = \mathbb{R}^n$), if $X$ takes uncountably many possible values, and if the distribution of $X$ has a *density* (defined in the next section), then we call $X$ a *continuous random variable*. A random variable with uncountably many values but no density – a mixture of a Dirac and a normal distribution, for instance – is therefore neither discrete nor continuous.
:::

:::{admonition} Definition
The *support* of $X$ is the smallest **closed** set $A \subseteq \mathbb{R}$ with $P(X \in A) = 1$,

$$
\operatorname{supp}(X) = \bigcap \{ A \subseteq \mathbb{R} \text{ closed} : P(X \in A) = 1 \}.
$$
:::

The word *closed* is not decoration here. Without it the intersection would be empty for every distribution with a density: for $X \sim U([0,1])$ the set $[0,1] \setminus \{x\}$ still has probability $1$ for every single $x$ (individual points are null sets – more on that shortly), so no point at all would lie in all of these sets. Insist on closed sets and $[0,1]$ comes out, as it should. (That the intersection itself has probability $1$ again, because countably many of the $A$ already suffice, is something we will not need.)

:::{admonition} Definition
A set $M \subseteq \mathbb{R}^n$ is called *closed* if it contains the limits of its own convergent sequences: if a sequence $(x_k)$ lies entirely in $M$ and converges to $x$, then $x \in M$ as well.
:::

Every interval of the form $[a,b]$ is closed, for instance, as is all of $\mathbb{R}$ and every finite set. The interval $(0,1]$, by contrast, is not: the sequence $\frac1k$ lies in it, its limit $0$ does not. The closure of $(0,1]$ is $[0,1]$.

For a discrete distribution with pmf $p$ and finitely many values, the support simplifies to

$$
\operatorname{supp}(X) = \{\, x \ \mid\ p(x) > 0 \,\},
$$

that is, to the set of values that can occur at all (with infinitely many values, their accumulation points come along too, since the support is closed).

:::{admonition} Example
The uniform distribution on $\Omega = \{1,\dots,n\}$, read as a distribution *on $\Omega$*, has support $\Omega$ itself – every element of it is possible.

The same distribution can also be read as a distribution on $\mathbb{R}$, by giving every other real number probability $0$. Then the support is $\{1,\dots,n\} \subset \mathbb{R}$, a finite and hence closed subset of the reals. So the support depends not only on the distribution, but also on *what* you read it as a distribution on.
:::

The support is defined for discrete real random variables too – the obvious difference being that the support of a discrete random variable contains no interval.

## Density functions

:::{admonition} Definition
Let $D \subseteq \mathbb{R}^n$ and let $f \colon D \to [0,\infty)$ be an integrable function (with respect to the Lebesgue measure on $\mathbb{R}^n$; Riemann integrability suffices) with $\int_D f(x) dx = 1$. Then a probability measure on $D$ is defined by:

$$
\text{for an event } A \subseteq D \colon \quad P(A) := \int_A f(x) dx
$$

Whenever a probability measure $P$ can be written in this way, we call the function $f$ a *probability density function* (pdf), or a *density* for short (not to be confused with the probability mass function, pmf, of the discrete case).
:::

So for a real random variable $X \colon \Omega \to \mathbb{R}$ whose distribution $P_X$ has a density $f$, we have for $A \subseteq \mathbb{R}$

$$
\int_{X^{-1}(A)} dP(\omega) = P(X \in A) = P_X(A) = \int_A f(x) dx
$$

The integral on the right is now an integral over the range of $X$.
In the same way we can also compute the expected value and the variance:

:::{admonition} Definition
Let $X$ be a continuous random variable whose distribution is given by a density $f \colon D \to [0,\infty)$. Then

$$
\mathbb{E}(X) = \int_\Omega X(\omega)\, dP(\omega) = \int_D x f(x) dx
$$

is called the *expected value* of $X$, and

$$
\mathbb{V}(X) = \int_\Omega \left(X(\omega)-\mathbb{E}(X)\right)^2 dP(\omega) = \int_D \left(x-\mathbb{E}(X)\right)^2 f(x) dx
$$

the *variance* of $X$, provided these integrals exist. For $D = \mathbb{R}$, for example, $\mathbb{E}(X) = \int_{-\infty}^{\infty} x f(x) dx$.
:::

This is the continuous counterpart of the sum over the probability mass function in the chapter [Expected value and variance](expectation-variance.md): the density takes the place of the pmf, the integral the place of the sum. That other functions of $X$ may be integrated in the same way is what the following theorem says.

:::{admonition} Theorem (transformation formula)
Let $X$ be a continuous random variable with density $f \colon D \to [0,\infty)$ and let $g \colon D \to \mathbb{R}$ be a (measurable) function. Then

$$
\mathbb{E}(g(X)) = \int_D g(x) f(x) dx,
$$

provided the integral exists. For a discrete random variable with pmf $p$, the same statement reads $\mathbb{E}(g(X)) = \sum_x g(x)\, p(x)$.
:::

We do not prove the theorem (it follows from the change-of-variables theorem for integrals), but we use it constantly: the definition of the variance is precisely the special case $g(x) = (x - \mathbb{E}(X))^2$, and with $g(x) = x^2$ we obtain, as in the discrete case,

$$
\mathbb{V}(X) = \mathbb{E}(X^2) - {\left( \mathbb{E}(X) \right)}^2 = \int_D x^2 f(x) dx - {\left( \mathbb{E}(X) \right)}^2.
$$

In general, $\mathbb{E}(X^k) = \int_D x^k f(x) dx$ is called the *$k$-th moment* of $X$.

:::{admonition} Example
Let $a < b \in \mathbb{R}$. Take $D = \mathbb{R}$ and $f \colon \mathbb{R} \to [0,\infty)$ given by

$$
f(x) = \begin{cases} \frac{1}{b-a}, & \text{ if } x \in [a,b] \\ 0 & \text{ otherwise} \end{cases}
$$

This $f$ defines a probability measure on $\mathbb{R}$, the *continuous uniform distribution* on the interval $[a,b]$.
Let $X$ be a random variable with this distribution; we write $X \sim U([a,b])$.
Its expected value (using $\int x dx = \frac{x^2}{2}$) is $\mathbb{E}(X) =$

$$
\int_{-\infty}^{\infty} xf(x) dx = \int_a^b \frac{xdx}{b-a} = \frac{1}{b-a} \left[\frac{x^2}{2}\right]_a^b = \frac{b^2 -a^2}{2(b-a)} = \frac{(b+a)(b-a)}{2(b-a)} = \frac{a+b}{2}
$$

The second moment is

$$
\mathbb{E}(X^2) = \int_{-\infty}^\infty x^2 f(x)dx = \left[ \frac{x^3}{3(b-a)} \right]_a^b = \frac{b^3-a^3}{3(b-a)} = \frac{a^2+ab+b^2}{3}
$$

The variance is

$$
\mathbb{V}(X) = \mathbb{E}(X^2) - {\left(\mathbb{E}(X)\right)}^2 =  \frac{a^2+ab+b^2}{3} - \frac{(a+b)^2}{4} = \frac{(a-b)^2}{12}
$$
:::

:::{admonition} Remark
**Null sets.** For $X \sim U([a,b])$ and $a \leq c < d \leq b$ we have $P(c \leq X \leq d) = \int_c^d \frac{dx}{b-a} = \frac{d-c}{b-a}$, and the same integral comes out for $P(c < X < d)$, $P(c \leq X < d)$ and $P(c < X \leq d)$: whether or not the endpoints belong to the interval makes no difference to the integral. In particular $P(X = c) = \int_c^c f(x) dx = 0$ for every single point $c$, even though $f(c) = \frac{1}{b-a} \neq 0$.

This holds for every distribution with a density: individual points have probability $0$; by finite additivity so does every finite set; and by the $\sigma$-additivity from the chapter [Deriving the mathematical formalism of stochastics](intro-stochastics.md) so does every countable set $A = \{a_1, a_2, \dots\}$, since $P(X \in A) = \sum_{i} P(X = a_i) = 0$. Sets with probability $0$ are called *null sets*. Change a density $f$ on a null set (at finitely many points, say) and not one integral $\int_A f(x) dx$ changes – and so neither does the probability measure it defines.
:::

:::{admonition} Example
The set $\mathbb{Q} \cap [0,1]$ of rational numbers between $0$ and $1$ is countable, and hence a null set for $X \sim U([0,1])$: a uniformly distributed random number from $[0,1]$ is irrational with probability $1$. A puzzle: is there any distribution on $[0,1]$ at all that gives every single point positive probability? (No: for each $k$ there are at most $k$ points with probability at least $\frac{1}{k}$, so at most countably many points in all with positive probability.)
:::

:::{admonition} Example
Not every probability measure can be represented by a density:
consider the distribution on $\mathbb{R}$ with

$$
P(A) = \begin{cases} 1 & \text{ if } 0 \in A \\ 0 & \text{ otherwise} \end{cases}
$$

This distribution is called the *Dirac distribution* with mass at $0$. There can be no density $f$ for it: the one-point set $\{0\}$ is a null set for every density, so we would have $\int_{\{0\}} f(x) dx = 0 \neq 1 = P(\{0\})$. The same argument hits every discrete distribution on $\mathbb{R}$: it concentrates its whole mass $1$ on its countable support, and that is a null set for every density. If you go to great lengths to build something density-like anyway, you end up in the theory of distributions – generalised functions – from functional analysis (physicists know them). And there are probability distributions for which not even a generalised function will do.
:::

:::{admonition} Example
Conversely, a continuous distribution is easily built out of a discrete one. Let $Y$ be a discrete random variable with values in $\{5,6,7\}$ and $P(Y=5) = \frac{4}{7}$, $P(Y=6) = \frac{2}{7}$, $P(Y=7) = \frac{1}{7}$, and let $Z \sim U([0,1))$ be independent of $Y$ (formally: $\Omega = \{5,6,7\} \times [0,1)$ with the product measure, $X(y,z) = y + z$). Then $X := Y + Z$ is a continuous random variable with values in $[5,8)$ and density

$$
f(x) = \begin{cases} \frac{4}{7}, & \text{ if } x \in [5,6) \\ \frac{2}{7}, & \text{ if } x \in [6,7) \\ \frac{1}{7}, & \text{ if } x \in [7,8) \\ 0 & \text{ otherwise,} \end{cases}
$$

since for $x \in [5,6)$ we have $P(5 \leq X \leq x) = P(Y = 5) \cdot P(Z \leq x - 5) = \frac{4}{7}(x-5)$, and likewise on the other two subintervals. The density integrates to $\frac{4}{7} + \frac{2}{7} + \frac{1}{7} = 1$; what value $f$ takes at the points $6$ and $7$ does not matter, by the remark on null sets. For example $P(5 \leq X \leq 6) = \int_5^6 f(x) dx = \frac{4}{7}$ and $P(6 \leq X \leq 6.5) = \frac{2}{7} \cdot \frac{1}{2} = \frac{1}{7}$. The expected value is

$$
\mathbb{E}(X) = \int_5^8 x f(x) dx = \frac{4}{7} \cdot \frac{11}{2} + \frac{2}{7} \cdot \frac{13}{2} + \frac{1}{7} \cdot \frac{15}{2} = \frac{85}{14} = 6 + \frac{1}{14},
$$

since on every subinterval $[k, k+1)$ we have $\int_k^{k+1} x\, dx = k + \frac{1}{2}$ (the same comes out of $\mathbb{E}(Y) + \mathbb{E}(Z) = \frac{39}{7} + \frac{1}{2}$). A distribution like this – a discrete choice first, then a continuous one within the chosen class – is called a *mixture distribution*; another example is the contaminated normal distribution in the chapter [The most important continuous distributions](important-continuous-distributions.ipynb), where this very distribution on $[5,8)$ is simulated too.
:::

:::{admonition} Definition
Let $(\Omega, P)$ be a probability space. Then for a random variable $X \colon \Omega \to \mathbb{R}$ we call the function

$$
F \colon \mathbb{R} \to [0,1],\qquad x \mapsto P(X \leq x)
$$

the *cumulative probability distribution function*, or *distribution function*, or *cdf* for short. Unlike the density (pdf), it always exists.
:::

:::{admonition} Example
If $P_X$ has a density $f \colon \mathbb{R} \to [0,\infty)$,
so that $P(a \leq X \leq b) = \int_a^b f(x)dx$, then

$$
F(x) = \int_{-\infty}^{x} f(t)dt.
$$

Whether you write $P(X \leq x)$ or $P(X < x)$ here makes no difference, by the remark on null sets; some books define the cdf with $P(X < x)$, and for distributions with a density that is the same function.
:::

:::{admonition} Theorem
If $P_X$ has a density $f$, then the distribution function $F$ is an antiderivative of $f$: by the fundamental theorem of calculus, $F$ is differentiable at every point $x$ at which $f$ is continuous, with $F'(x) = f(x)$. For every random variable (with or without a density) the cdf also gives the probability of intervals,

$$
P(a < X \leq b) = F(b) - F(a),
$$

and with a density that is precisely $\int_a^b f(t)dt$.
:::

So the cdf climbs steeply exactly where the density is large. In the chapter [The most important continuous distributions](important-continuous-distributions.ipynb) the pdf and the cdf are always plotted together; look out for it there.
