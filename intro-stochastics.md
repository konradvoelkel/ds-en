# Deriving the mathematical formalism of stochastics

You have already met the basics of (discrete) probability theory in Mathematics for Computer Scientists 3. We will go over them again, as far as we need them. In this course we will mostly use the notions of the probability mass function (for discrete random variables) and the probability density function (for continuous random variables), both of which build on the notion of a probability measure. At this point there is a short digression to explain why it is done exactly this way, and how one might arrive at the notion of a probability measure. The notions of a sigma-algebra ($\sigma$-algebra) and of measurable functions are essential for carrying out proofs in probability theory, and also for introducing more complex notions (such as those needed in mathematical finance or in the theory of machine learning) – here we can content ourselves with taking away when we are allowed to read over these notions.

Stochastics can be understood as an umbrella term for probability theory and statistics. Statistics is concerned with probabilistic models developed from observations, and draws conclusions from them. Probability theory is concerned with investigating those models and the theory behind them.

```{figure} images/stochastik-statistik-wtheorie.png
:width: 480px
:align: center
:name: stochastik-uebersicht

Stochastics as the umbrella term: statistics works on a section of reality, probability theory works on the models.
```

The two arrows in the middle are what the picture is really saying, and they run in opposite directions. From the section of reality to the models leads **modelling**: you observe, collect data and set up a model that fits. From the models back to reality leads **prediction**: you calculate within the model and assert something about the world that can be checked. Both directions are needed, and this book walks each of them several times.

As always in computer science, one essential aim is to model a section of reality with a model, that is, to abstract away from that section, to use the model to predict a piece of reality, and to test the model against reality.

We already know logical models of reality: if it rains, the lawn gets wet. If I am hungry and then eat a lot, I am no longer hungry afterwards.

In the notation of propositional logic, the first model is written as an implication. With $N$ for "the lawn is wet", $R$ for "it has rained" and $G$ for "somebody watered it", it reads

$$
N \Rightarrow R \vee G,
$$

or, as you would write it in a programming language, `(!N) || R || G`. The model is useful, but it does not answer the question that actually occupies us when we look at the wet lawn: which of the two was it? Does it rain here often? Has anybody ever watered this lawn at all? Propositional logic can only answer "at least one of the two".

Statistical models now extend this all-or-nothing logic by degrees of plausibility: if the lawn is wet, it is plausible to assume that it rained recently. It is equally plausible to assume that somebody watered the lawn with a garden hose. Which we find more plausible depends on what else we know about reality. By watching the lawn for longer we can establish how often each reason leads to a wet lawn, and sharpen our model accordingly.

To be able to calculate with plausibility exactly as we do with Boolean logic, and finally to implement it on a computer, we have to attach numbers to the plausibility values. A suitable abstraction is the real numbers, since the reals are the only Archimedean ordered complete field containing the rationals (and the subalgebra of computable reals inside them has already served us well).

:::{admonition} Example
A first, naive attempt: we simply count. Last month it rained on $20$ days, and on $5$ days somebody watered. So we set $plaus(R) = 20$ and $plaus(G) = 5$.

How plausible, then, is "it rained or somebody watered"? The obvious answer $25$ is wrong as soon as there was even one day on which both happened – that day would be counted twice. The correct answer is

$$
plaus(R \vee G) = plaus(R) + plaus(G) - plaus(R \wedge G),
$$

and to work it out we need to know whether anybody ever watered into the rain.
:::

Two things can be seen from this example. First, calculating with plausibilities is not as naive as one might at first think; it needs rules. Second, the numbers $20$ and $5$ are unwieldy, because they depend on the observation period: with two months of observation they would read $40$ and $10$, without anything having changed about the matter itself.

We also want plausibility logic to be compatible with classical logic, that is, logically equivalent statements should be equally plausible, and different routes to determining the plausibility of a statement should arrive at the same result (consistency).
To put that into mathematics, let us call a finite set of statements whose plausibility we want to assess $\mathcal{A}$, and the assignment of plausibility is a map $p \colon \mathcal{A} \to \mathbb{R}$.

Two rules we want in any case. The first is the formula from the example, so-called *inclusion–exclusion*: whoever adds two possibilities counts their overlap twice and has to subtract it once,

$$
plaus(A \vee B) = plaus(A) + plaus(B) - plaus(A \wedge B).
$$

The second fixes the problem with the observation period. We normalise so that the plausibility of a statement and that of its negation add up to $1$,

$$
plaus(A) + plaus(\neg A) = 1,
$$

since exactly one of the two holds. Every plausibility then lies between $0$ and $1$, and the absolute length of the observation period drops out: $20$ rainy days out of $30$ become $\frac{2}{3}$, whether you count for a month or for a year.

Is that already enough to call these numbers "probability"? Not quite – but almost.

If these requirements are made precise, one can prove [Cox's theorem](https://en.wikipedia.org/wiki/Cox%27s_theorem), which says that there is a mathematical map $cj$ from the real numbers into the closed interval $[0,1]$ taking plausibilities to "probabilities" in such a way that (almost) all the rules of classical probability theory are satisfied. Thus $P := cj \circ p \colon \mathcal{A} \to [0,1]$ satisfies the rules
1. $P(TRUE) = 1$ and $P(FALSE) = 0$.
1. If $A_1,\dots,A_n$ is a finite set of pairwise incompatible (mutually exclusive) statements, then finite additivity holds:
$ P(A_1 \vee \dots \vee A_n) = \sum_{i=1}^n P(A_i) $

We will now approach the modern version of the notion of probability. The notion of a sigma-algebra is only to be mentioned here; afterwards you may (for this course) forget it again.

## Digression (optional): the measure problem

:::{note}
This digression and the next are pure background reading and **not part of the course proper**. They explain why the definitions in the section *Formalism* look the way they do. If you skip them, you can carry straight on at the section *Formalism*.
:::

For a die or a coin it is reasonably clear how we model the probability and how we can set up a statistical model that we can also implement. In theory, though, the question soon arises of what happens with, say, an experiment repeated infinitely often. That is not a purely theoretical question, because we are interested in the asymptotics, that is, in how an experiment repeated sufficiently often behaves approximately.

Coin tosses repeated infinitely often can be written down as an infinite sequence of $0$s and $1$s, and on closer inspection this also gives us a representation of the real numbers in the unit interval $[0,1]$, one that can be implemented on a computer just as well as the computer is a Turing machine (in reality the tape is finite, but we can always extend it – or rather, the memory of our computers is bounded but not bounded by a fixed value).

We would now like to assign a probability to every outcome (every result of the infinitely repeated coin toss) in such a way that $P(\Omega)=1$, where $\Omega = \{0,1\}^{\mathbb{N}}$ is the sample space.
Moreover, finite additivity should hold for pairwise disjoint subsets $A_i \subseteq \Omega$:

$P\left( \bigcup_{i=1}^n A_i \right) = \sum_{i=1}^n P(A_i)$

A further natural requirement is flip invariance, that is, that it makes no difference to the probability if I flip exactly the $n$-th coin toss (the $n$-th bit). This can be formalised by an operator $F_n \colon \Omega \to \Omega$ with

$F_n(\omega_1,\dots,\omega_{n-1},\omega_n,\omega_{n+1},\dots) =
     (\omega_1,\dots,\omega_{n-1},1-\omega_n,\omega_{n+1},\dots)$

We then expect $P(F_n A) = P(A)$ to hold for every subset $A \subseteq \Omega$.

In 1923 Banach proved, using the axiom of choice, that while it is possible to define such a probability $P$ non-constructively, it is not possible to do so uniquely!

If we tighten one of our requirements, going from finite additivity to $\sigma$-additivity (one says sigma-additivity or countable additivity), then [Vitali had already proved in 1905](https://en.wikipedia.org/wiki/Non-measurable_set) that no such map $P$ exists at all, so that it is impossible to assign probabilities to infinite coin tosses in this way. Why is that, and what has it to do with $\sigma$-additivity?

## Digression (optional): measuring open sets

A very practical definition for any set $M$ on which there is a notion of distance (more precisely: $M$ a metric space) is this:
a set $U \subseteq M$ is called *open* if around every point $u \in U$ there is a distance $\epsilon > 0$ such that all points $x \in M$ at distance $d(x,u) < \epsilon$ already lie entirely in $U$, that is $x \in U$. For $M=\mathbb{R}$, finite unions of open intervals are such open sets, which is where the name comes from.

One can now show that the classical $\epsilon$-$\delta$ definition of continuity is equivalent to this: $f \colon X \to Y$ is called *continuous* if the preimages of open sets $U \subseteq Y$ are open sets $f^{-1}(U) \subseteq X$ as well.

If we want to define a uniform distribution on the numbers in the interval $[0,1]$ (as in the infinite coin-toss example), or indeed on all the reals, then we already know exactly how we want to treat intervals: for an interval $[a,b]$ the probability, the measure, should simply be $b-a$.

Since every open set in $\mathbb{R}$ can be written as a countable union of intervals, we therefore know how a measure can be assigned to the open sets: as the countable sum of the lengths of exactly those intervals. It turns out that a uniform distribution can indeed be defined this way, only that one cannot then determine a probability value for arbitrary subsets of $\mathbb{R}$ or $[0,1]$. One says that there are *non-measurable sets*.

From this observation we now derive the requirement that our probability $P$ should not merely be finitely additive, but $\sigma$-additive. Following Vitali's theorem we accept that not every subset of $\mathbb{R}$ is measurable, and content ourselves with singling out a subalgebra of $\mathcal{P}(\mathbb{R})$, the *measurable sets*.

## Formalism

So far we have pinned plausibilities to *statements*: "it rained", "somebody watered". Statements are the right object for logic, but they are unwieldy as soon as one wants to calculate – even the question of how many different statements there are leads astray. The trick of modern probability theory is to replace every statement by the set of situations in which it holds.

To that end we imagine a set $\Omega$ of all **outcomes** $\omega$ under consideration – in the lawn example, say, all the states the world could be in this morning. Every statement about the world splits this set in two: the states in which it is true, and the rest. The statement "the lawn is wet" thus becomes the subset $N \subseteq \Omega$ of all world states with a wet lawn, "it rained" becomes $R \subseteq \Omega$ and "somebody watered" becomes $G \subseteq \Omega$. Instead of a plausibility for the statement, we are now after a number for the subset.

The gain: the logical connectives become set operations, which we already know and have mastered.

| Propositional logic | Set logic |
|---|---|
| $A$ or $B$, $A \vee B$ | $A \cup B$ |
| $A$ and $B$, $A \wedge B$ | $A \cap B$ |
| not $A$, $\neg A$ | $A^c := \Omega \setminus A$ |

The question of how plausible "it rained or somebody watered" is thus becomes the question of $P(R \cup G)$, and "it neither rained nor was watered" is $R^c \cap G^c$, that is, the complement of $R \cup G$.

A subset of $\Omega$ to which we assign a probability we call an **event**. Now it would be convenient to admit every subset of $\Omega$ as an event, and for finite $\Omega$ that works. In general – this was the lesson of the measure problem – it does not. We therefore single out a system $\mathcal{F}$ of "interesting" subsets and only require it to be closed under the same operations we have just translated: along with $A$ and $B$, the sets $A \cup B$, $A \cap B$ and $A^c$ should lie in $\mathcal{F}$, and $\emptyset$ and $\Omega$ in any case. The probability is then a map $P \colon \mathcal{F} \to [0,1]$.

In mathematical language such a system of sets is called a $\sigma$-algebra – the $\sigma$ stands for the fact that *countably infinite* unions are allowed too, which we need for passing to the limit. With that we have all the ingredients together and can write the definitions down.

:::{admonition} Definition
Let $\Omega$ be a set. Then a system of sets $\mathcal{F} \subseteq \mathcal{P}(\Omega)$ is called a *$\sigma$-algebra* if
1. $\Omega \in \mathcal{F}$ "TRUE is measurable"
1. $A \in \mathcal{F} \implies A^c := \Omega \setminus A \in \mathcal{F}$ "logical NOT"
1. $A_1,\dots \in \mathcal{F} \implies \bigcup_{i\geq 1} A_i \in \mathcal{F}$ "logical OR"

Terminology: we call the elements of $\Omega$ the *outcomes* and the elements of $\mathcal{F}$ the measurable subsets, or *events*. The pair $(\Omega,\mathcal{F})$ is an *event space*.
:::

:::{admonition} Example
An ordinary die has state space $\Omega = \{1,2,3,4,5,6\}$, and the power set $\mathcal{P}(\Omega)$ is already a $\sigma$-algebra (so there are no non-measurable sets – this always works for finite $\Omega$). A single throw of the die yields an outcome, the number of pips. The statement "the number of pips is even" is a logical statement corresponding to the event $\{2,4,6\} \subseteq \Omega$. In very many cases we are (of necessity) not interested in concrete outcomes but in particular events.
:::

Rule of thumb: if it is unclear what the $\sigma$-algebra is supposed to be, it is $\mathcal{P}(\Omega)$; in other words, if it is unclear what a "measurable set" is supposed to be, "set" is simply what is meant.

:::{admonition} Definition
A function $P \colon \mathcal{F} \to [0,1]$ from a $\sigma$-algebra on a set $\Omega$ into the unit interval is called a *probability measure* if
1. $P(\Omega) = 1$ (normalisation) and
1. for pairwise disjoint events $A_i \in \mathcal{F}$, $\sigma$-additivity holds:
$P \left( \bigcup_{i\geq 1} A_i \right) = \sum_{i\geq 1} P(A_i)$

The triple $(\Omega, \mathcal{F}, P)$ is called a *probability space*.
:::

Compare this with Definition 12.2.5 and Remark 12.2.8 in the German lecture notes "Mathematik für Informatik", where the special case $\mathcal{F} = \mathcal{P}(\Omega)$ with finite $\Omega$ is assumed.

:::{admonition} Example
Let us stay with the wet lawn. We set $\Omega = \{R, G, T\}$ (the letters now stand for outcomes, no longer for events as above) for the three explanations "it rained", "somebody watered", "it was dew", and as the $\sigma$-algebra we take the power set $\mathcal{F} = \mathcal{P}(\Omega)$. The one-element events $\{R\}, \{G\}, \{T\}$ are called **elementary events**; on a finite set their probabilities already fix the whole measure, since every other event is a disjoint union of them.

A first attempt: $P(\{R\}) = \frac23$, $P(\{G\}) = \frac16$, $P(\{T\}) = \frac13$. This is not a probability measure. For $\sigma$-additivity gives

$$
P(\Omega) = P(\{R\}) + P(\{G\}) + P(\{T\}) = \dfrac{2}{3} + \dfrac{1}{6} + \dfrac{1}{3} = \dfrac{7}{6} > 1,
$$

contradicting the normalisation $P(\Omega) = 1$. With $P(\{R\}) = \frac12$ instead of $\frac23$ the sum works out, and we have a probability measure.

A second objection weighs more heavily and concerns not the numbers but the model. A probability measure on $\{R, G, T\}$ implicitly claims that the three explanations are mutually exclusive – that it cannot rain *and* somebody water. That is plainly false. Anyone who wants to allow both has to choose the outcomes more finely, for instance

$$
\Omega' = \{ R\,G,\ R\,\overline{G},\ \overline{R}\,G,\ \overline{R}\,\overline{G} \},
$$

that is, all four combinations of "rained yes/no" and "watered yes/no". The event "it rained" is then no longer an elementary event but the two-element set $\{R\,G,\ R\,\overline{G}\}$.

This shows where the real work of modelling lies: not in distributing the numbers, but in the choice of $\Omega$. The outcomes have to be pairwise exclusive and together cover everything that can happen.
:::

:::{admonition} Example
On a finite set $\Omega$ of cardinality $N := |\Omega|$ (that is, with $N$ elements), $\mathcal{F} := \mathcal{P}(\Omega)$ together with $P(A) := |A| / N$ defines a probability measure, which we call the *uniform distribution*.

The fair die is the case $\Omega = \{1,\dots,6\}$: the event "even number of pips" is $\{2,4,6\}$ and has probability $P(\{2,4,6\}) = \frac{3}{6} = \frac12$. This can also be checked in code, see [Programming with stochastics](programming-stochastics.ipynb).
:::

:::{admonition} Example
For an arbitrary event space $(\Omega,\mathcal{F})$ and a fixed element $\xi \in \Omega$,

$\delta_\xi := A \mapsto \begin{cases} 1 & \xi \in A,\\ 0 & \text{otherwise} \end{cases}$

defines a probability measure, the *Dirac measure* with unit mass at the point $\xi$.

This is the maximally unfair die: a die that always shows a six has distribution $\delta_6$. For it, $P(\{2,4,6\}) = 1$ and $P(\{1,2,3\}) = 0$ – the event "even number of pips" occurs with certainty, the event "at most three" never. Between these two extremes, the uniform distribution and the Dirac measure, lie all the other dice.
:::

:::{admonition} Proposition
**Rules of calculation** for probability measures:
for every probability space $(\Omega,\mathcal{F},P)$ with $A,B \in \mathcal{F}$:
1. $P(\emptyset) = 0$
1. Finite additivity: $P(A \cup B) + P(A \cap B) = P(A) + P(B)$
1. Monotonicity: $A \subseteq B \implies P(A) \leq P(B)$
1. $\sigma$-subadditivity: $P \left( \bigcup_{i\geq 1} A_i \right) \leq \sum_{i\geq 1} P(A_i)$
   (where the $A_i \in \mathcal{F}$ need not be disjoint)
:::

:::{admonition} Proof
1. $1 = P(\Omega) = P(\emptyset \cup \Omega) = P(\emptyset) + P(\Omega) = P(\emptyset) + 1$
1. $P(A \cup B) = P(A \cup (B \setminus A)) = P(A) + P(B \setminus A)$ and
   $P(B \setminus A) + P(A \cap B) = P((B \setminus A) \cup (A \cap B)) = P(B)$, hence
   $P(A \cup B) + P(A \cap B) = P(A) + P(B \setminus A) + P(A \cap B) = P(A) + P(B)$
1. $A \subseteq B \implies B = A \cup (B \setminus A)$
   $\phantom{A \subseteq B} \implies P(A) \leq P(A) + P(B \setminus A) = P(A \cup (B \setminus A)) = P(B)$
1. left to the reader as an exercise.
:::

:::{admonition} Definition
A function $f \colon \Omega \to \Omega'$ between probability spaces $\Omega$ and $\Omega'$ (we no longer write the $\sigma$-algebras and probability measures out separately) is called *measurable*, or a *random variable*, if for measurable sets $U \subseteq \Omega'$ the preimages $f^{-1}(U) \subseteq \Omega$ are measurable as well.
:::

Rule of thumb: if it is unclear what the $\sigma$-algebras are supposed to be, we picture every map (= function) as measurable. Strictly speaking that is usually false as soon as we deal with continuous random variables – and it will not trouble us in practice all the same.

:::{admonition} Example
If we define the uniform distribution on $[0,1]$ by declaring the interval length to be the probability measure on open intervals, then every continuous function $f \colon [0,1] \to [0,1]$ is measurable as well.
:::

The term random variable is highly misleading: there is neither a variable nor randomness here. While the notion of a measurable map makes sense outside probability theory too, the notion of a random variable has a different typical use and different syntactic habits. We may picture this overloading of the term as an API wrapper that gives us extra syntactic sugar – a map that comes dressed as a random variable can be used like a variable taking random values. We will lean on this perspective more heavily and practise it.

In what follows we do not want to get further into measure theory, which takes a certain amount of effort to define, say, the general Lebesgue integral. Because of the applications in computer science, and in machine learning in particular, we do want to record one thing: whereas the Riemann integral is formed by approximating with the areas of rectangles, the Lebesgue integral is formed by approximating the function itself by step functions.

:::{admonition} Definition
A step function is a measurable function taking only finitely many different values.
:::

:::{admonition} Theorem
For every $\sigma$-algebra on $\Omega$ and every measurable function $f \colon \Omega \to \mathbb{R}$ there is a sequence of step functions $t_n \colon \Omega \to \mathbb{R}$ converging to $f$: $t_n \to f$.
:::

This allows a great many statements to be proved by proving them for step functions (the construction of the Lebesgue integral among them). Far-reaching universality statements can also be built from it whenever a model of computation is able to approximate step functions to arbitrary accuracy. It is also how the universality of neural networks can be seen; the course *Introduction to Deep Learning* works this out (universal approximation).

Finally, it should not go unmentioned that there is a legitimate objection to this formalism: on a computer only constructive mathematics can be implemented, and the law of the excluded middle and the axiom of choice are not implementable. In that logic, though (the constructivist, so-called intuitionistic one), all sets of a metric space $X$ may be called measurable, precisely because the non-measurable subsets are not constructible. That makes some things easier, but also a great many things impossible. So we content ourselves with knowing how to read texts that use the usual formalism, and with having a good excuse at hand for why we will not engage with the formalism any longer.

So you can now pick up a probability textbook, find a theorem there saying "let X be a set with a $\sigma$-algebra ..." and read over the $\sigma$-algebra part for the time being, since in practice you will not run into non-measurable sets (that is, into those that are not part of the system of sets called a $\sigma$-algebra). In other words: as a first approximation, imagine that "measurable" is no restriction at all. What we should take away from this chapter at the very least is the notion of a random variable, the rules of calculation for probability measures $P$, and the important example of the uniform distribution.

If you would like to approach stochastics through interactive playthings as the course goes on, [Random Services](
https://randomservices.org/random/prob/index.html) is just the thing for you.
If you prefer things elegant and visual, [Seeing Theory](https://seeing-theory.brown.edu/) will accompany you through the stochastics part of the course.

[If you would like the throw of a die (the uniform distribution, also called a Laplace experiment) explained to you again by somebody else in six minutes, you can find that on YouTube on the channel musstewissen Mathe](https://www.youtube.com/watch?v=zPcjFWQa6Uc) (in German).
