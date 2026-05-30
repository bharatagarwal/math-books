# Probability

*Bradfield session 2 · Thursday 18 June · pre-work: LL chapter 7 ·
post-work: MCS 17.2–17.4*

Last session we learned to count a set we'd described indirectly. This session
turns that skill into **probability**, and the connection is almost embarrassingly
direct: a probability is **a count with a denominator.** The outline frames it
exactly this way — probability is "counting the states from which a choice is
randomly made." If every outcome is equally likely, the chance of an event is just
*how many outcomes make it true* over *how many outcomes there are.* The whole of
the previous chapter is the numerator and the denominator of this one.

Lovász (our **LL** text, the *Discrete Mathematics* book in this reader) makes a
deliberate, narrow choice in his chapter 7: he does not try to build all of
probability theory. He builds *just enough* — uniform spaces, events,
independence, repeated trials — to reach one genuinely deep result, the **Law of
Large Numbers**, and to show it is "not a mysterious force, but a simple
consequence of the properties of binomial coefficients." That arc is the spine of
this chapter, and we will follow it: uniform spaces as counting → events and
independence → independent repetition and the binomial distribution → the Law of
Large Numbers (the climax) → gambler's ruin. Expectation and variance we fold in
as the supporting machinery.

For us as programmers there is a second advantage. Every probability has **two
faces** — an *exact* value you compute by reasoning, and an *empirical* value you
get by running the experiment a million times. We hold the two against each other
throughout. When they agree, we believe the model; when they disagree, one of them
has a bug, and finding which is the whole skill.

## Sample spaces, events, and uniform probability

Following LL §7.1: an experiment whose outcome depends on chance has a set $S$ of
possible outcomes — the **sample space**. Tossing a coin gives $S=\{H,T\}$; rolling
a die gives $S=\{1,2,3,4,5,6\}$. Every *subset* of $S$ is an **event** (the event
that the outcome lands in that subset): for a die, $\{2,4,6\}$ is "even." Two
events are **exclusive** when they cannot co-occur, i.e. $A\cap B=\emptyset$.

To make it a **probability space** we give each outcome a weight $P(s_i)\ge 0$ with
$\sum_i P(s_i)=1$, and the probability of an event is the total weight of its
outcomes. LL restricts attention (and so do we) to the **uniform** space, where
every outcome is equally likely. There the probability of an event is pure
counting:
$$P(A)=\frac{|A|}{|S|}.$$
That is literally "count the favorable states, divide by all the states" — which
is why the previous chapter was the prerequisite. Roll two fair dice: $S$ has $36$
equally likely outcomes, and $P(\text{sum}=7)=6/36=1/6$ because six of them sum to
seven. We build the space, compute the exact distribution with `Fraction` (no
rounding error to hide behind), and confirm it against a Monte Carlo run:

```python
<!-- include: code/bradfield/02-probability/01_sample_spaces.py -->
```

LL's §7.1 exercises are not really about one die — they are claims about *every*
uniform space (the probability of any event is at most $1$; the complement rule
$P(\bar A)=1-P(A)$; exclusive events add; and $P(A\cap B)+P(A\cup B)=P(A)+P(B)$).
That "for every space" shape is exactly what a **property-based tester** is for:
rather than check one example by hand, throw hundreds of random spaces and events
at each axiom and let it hunt for a counterexample. The companion to this chapter
in the source itself (LL ch 7, Exercise 7.2–7.5) is verified that way; here we
take the same spirit forward with the worked examples below.

### The birthday paradox: count the complement

A theme that pays off constantly, and the first place the "two faces" view earns
its keep: when an event is awkward to count head-on, count its **complement**,
$P(E)=1-P(\bar E)$ (LL's complement rule from §7.1).

"Among $k$ people, do *some two* share a birthday?" is horrible directly — there
are so many ways a collision can happen. But "*all $k$ distinct*" is a clean
product, one shrinking factor per person:
$$P(\text{all distinct})=\frac{365}{365}\cdot\frac{364}{365}\cdots
\frac{365-k+1}{365},$$
and the answer is one minus that. The famously counter-intuitive result: just
$23$ people already pushes the chance of a shared birthday past $50\%$. (The same
math is why hash collisions appear far sooner than the table size suggests — the
"birthday bound" $\approx\sqrt{N}$.) We compute the exact rational and confirm by
simulation:

```python
<!-- include: code/bradfield/02-probability/02_birthday.py -->
```

## Independence: an arithmetic accident, not a feeling

LL §7.2 introduces the single most important — and most abused — notion in the
chapter. Two events $A$ and $B$ are **independent** when
$$P(A\cap B)=P(A)\,P(B).$$
Informally, learning whether $A$ happened tells you nothing about $B$. But the
definition is not a feeling; it is an *arithmetic coincidence* — the joint
probability happening to equal the product of the parts. The only way to know is
to compute both sides.

So let's **discover** it the way the definition demands. LL Exercise 7.6 names four
events on a die roll — $E$ (even), $O$ (odd), $T$ (divisible by three), $L$
("better than average," i.e. larger than three) — and asks which pairs are
independent and which are exclusive. Rather than reason it out, we build the
contingency table and read the answer off: for each pair, put $P(A\cap B)$ next to
$P(A)P(B)$ and see where they coincide.

```python
<!-- include: code/bradfield/02-probability/08_independence_explorer.py -->
```

The table makes the surprises visible. $E$ and $T$ *are* independent —
$E\cap T=\{6\}$ so $P(E\cap T)=1/6=\tfrac12\cdot\tfrac13=P(E)P(T)$ — even though
"even" and "multiple of three" feel related; the arithmetic, not the intuition,
decides. Meanwhile $E$ and $O$ are **exclusive** (disjoint), and the demo confirms
the trap that follows: exclusive events with nonzero probability are exactly *not*
independent, since their joint probability is $0$ but the product of their
margins is not. Exclusive and independent are nearly opposite ideas, and conflating
them is a classic bug. The independent pairs the demo finds are $E\,T$, $O\,T$, and
$T\,L$.

## Independent repetition and the binomial distribution

Now the move that opens up the whole chapter (LL §7.2, "independent repetition").
Repeat an experiment $n$ times and treat the whole run as *one* big experiment: an
outcome is a length-$n$ sequence over $S$, the big sample space is $S^n$, it has
$k^n$ outcomes, and we make it uniform — each sequence has probability $1/k^n$.
Tossing a coin twice gives $\{HH,HT,TH,TT\}$, each with probability $1/4$. This is
the product rule from the counting chapter, now wearing a probabilistic costume,
and it is the mathematical model of "the trials don't influence each other."

The headline question: in $n$ independent trials, each a success with probability
$p$, what is the chance of **exactly $k$ successes**? Count it. A specific
sequence with $k$ successes and $n-k$ failures has probability $p^k(1-p)^{n-k}$,
and there are $\binom{n}{k}$ ways to choose *which* trials succeed. So
$$P(\text{exactly }k\text{ successes})=\binom{n}{k}\,p^k(1-p)^{n-k}.$$
This is the **binomial distribution**, and it is the counting chapter's binomial
coefficients made into probabilities. The whole distribution must sum to $1$ —
which it does, because these are exactly the terms of the binomial theorem applied
to $(p+(1-p))^n=1^n$. We reproduce LL's two headline numbers (the $\sim 8\%$
chance of exactly $50$ heads in $100$ tosses; exactly three sixes in ten rolls)
and check the sum-to-one symbolically:

```python
<!-- include: code/bradfield/02-probability/05_binomial_distribution.py -->
```

That $\sim 8\%$ figure is worth dwelling on, because it is the seed of the Law of
Large Numbers. Fifty heads is the **single most likely** outcome of $100$ tosses —
and yet it happens less than one time in twelve. The expected value and the *exact*
value pull apart. To see why, and to feel what is coming, let's **build the
distribution and look at its shape.** The probabilities $P(k\text{ heads})=
\binom{n}{k}/2^n$ are just one normalized row of Pascal's triangle, so we print
that row as a histogram and watch what happens to its mass as $n$ grows:

```python
<!-- include: code/bradfield/02-probability/09_binomial_shape.py -->
```

The $n=20$ row prints as a clean bell, symmetric about its peak at $k=10$ (Pascal's
symmetry $\binom{n}{k}=\binom{n}{n-k}$, and the peak sits at the expected count
$n/2$). The concentration table is the punchline that sets up the next section: as
$n$ grows, the peak $P(\text{exactly }n/2)$ **shrinks** toward $0$ (from $0.18$ at
$n=20$ to $0.006$ at $n=20{,}000$), while the mass in the central band
$|k/n-\tfrac12|\le 0.1$ **grows** toward $1$ (from $0.74$ at $n=20$ to
essentially $1$ by $n=2000$). Mass leaks away from the exact center but stays
*near* it. "Close to half" wins; "exactly half" loses. That tension is the Law of
Large Numbers in embryo.

### Expectation and the indicator method

Before the climax, the one tool we'll keep reaching for. A **random variable** $X$
assigns a number to each outcome; its **expectation** is the weighted average
$$\mathbb{E}[X]=\sum_{\omega\in S}X(\omega)\,P(\omega)=\sum_v v\,P(X=v).$$
A fair die has $\mathbb{E}[X]=3.5$. The deepest elementary fact about expectation
is **linearity**:
$$\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y],$$
which holds **always — even when $X$ and $Y$ are dependent.** That is what powers
the *indicator method*: to find the expected count of something, write it as a sum
of $0/1$ indicators, take each expectation, and add.

The showpiece: a random permutation of $n$ items has, on average, exactly **one**
fixed point — for *every* $n$. Let $X_i$ indicate that position $i$ is fixed; then
$P(X_i=1)=1/n$, so $\mathbb{E}[\text{fixed points}]=\sum_{i=1}^n \tfrac1n=1$. The
indicators are highly dependent (if the first $n-1$ are fixed, the last must be);
linearity does not care. We confirm it by brute force for small $n$ and by
simulation at $n=50$:

```python
<!-- include: code/bradfield/02-probability/03_expectation.py -->
```

### Variance: how far from expected?

Expectation locates the center; **variance** measures the spread:
$$\operatorname{Var}(X)=\mathbb{E}\!\big[(X-\mathbb{E}[X])^2\big]
=\mathbb{E}[X^2]-\mathbb{E}[X]^2.$$
And here independence finally *buys* us something concrete. Unlike expectation,
variance adds only **when the variables are independent**:
$$\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)
\quad\text{(independent }X,Y\text{)}.$$
For one fair die $\operatorname{Var}=35/12$; for the sum of two independent dice it
is $35/6$, exactly double. We verify independence outcome-by-outcome, compute both
variances exactly, and cross-check numerically:

```python
<!-- include: code/bradfield/02-probability/04_variance_independence.py -->
```

This is more than an aside. The reason a *sum* of $n$ independent trials
concentrates — the reason the bell in the previous demo narrows in *relative*
terms as $n$ grows — is that its variance grows like $n$ while its mean grows like
$n$, so the *relative* spread shrinks like $1/\sqrt{n}$. That $1/\sqrt{n}$ is the
quantitative engine behind the Law of Large Numbers, and behind the $10\sqrt{m}$
band we are about to meet.

## The Law of Large Numbers (the climax)

This is what LL §7.3 builds the entire chapter toward. The folk statement is "toss
a coin many times and heads will be about as common as tails." LL makes it precise
for $n=2m$ tosses, in the simplest form of the law:

**Theorem 7.1 (LL).** *Let $0\le t\le m$. The probability that, out of $2m$
independent coin tosses, the number of heads is less than $m-t$ or greater than
$m+t$ is at most $m/t^2$.*

The bound is useless for small $t$ (if $t<\sqrt m$ it exceeds $1$), but choosing
$t=10\sqrt m$ gives the memorable corollary:

**Corollary 7.1 (LL).** *With probability at least $0.99$, the number of heads
among $2m$ tosses lies between $m-10\sqrt m$ and $m+10\sqrt m$.*

For $m=1{,}000{,}000$ the half-width $10\sqrt m=10{,}000=m/100$, so with
probability $\ge 99\%$ the head count is **within one percent** of $m=n/2$. Large
numbers tame the chaos.

We can *watch* this happen before proving anything. The Monte-Carlo simulation
flips the coin and tracks the running fraction of heads as $n$ grows; the fraction
drifts steadily toward $1/2$. The same file also resolves the apparent paradox we
spotted earlier — that $P(\text{exactly }n/2\text{ heads})\to 0$ — by computing,
side by side, that single fading peak against the *band* probability
$P(|\text{frac}-\tfrac12|\le\varepsilon)$, which climbs to $1$:

```python
<!-- include: code/bradfield/02-probability/06_law_of_large_numbers.py -->
```

The table prints the two limits marching in opposite directions. At $n=10$ they
happen to coincide at $\approx 0.25$: the $\pm 5\%$ window $[4.75, 5.25]$ contains
only the single count $k=5$, so the band *is* the exact-half outcome there. But as
$n$ grows they split decisively — by $n=1000$ the band already holds $\approx
0.999$ while the exact-half peak has fallen to $\approx 0.025$, and by $n=10{,}000$
the peak is under $0.01$ while the band captures essentially all the mass.
"Exactly half" is one outcome and fades; "close to half" is a widening crowd of
outcomes and grows to certainty.

**Why it is true — Pascal, not magic.** LL's proof is the chapter's payoff,
because it shows the law is pure combinatorics. Let $A_k$ be the event "exactly
$k$ heads." These events are mutually exclusive and exhaust the space, and (the
binomial count from two sections ago)
$$P(A_k)=\frac{\binom{2m}{k}}{2^{2m}}.$$
The probability of landing outside $[m-t,m+t]$ is therefore a sum of two tails of
a Pascal row. LL bounds each tail using a Pascal-triangle estimate (his Theorem
5.2) and the triangle's symmetry, and the two tails together come to less than
$m/t^2$ — which is the theorem. The Law of Large Numbers is *the Pascal triangle
concentrating around its middle*, exactly the shrinking-peak / growing-band picture
demo `09` drew. Using exact rational arithmetic we reproduce $P(A_k)$, check the
$A_k$ sum to $1$ (probability axiom (b)), and verify Theorem 7.1's bound for
several $(m,t)$ pairs — including the Corollary's $m/t^2=1/100$ at
$m=1{,}000{,}000,\ t=10{,}000$:

```python
<!-- include: code/bradfield/02-probability/05_binomial_distribution.py -->
```

(The binomial file above does double duty: its sum-to-one check is precisely
probability axiom (b) for the head-count distribution, $\sum_k P(A_k)=1$. The
tail-bound numbers and the convergence are what demos `06` and `09` exhibit
directly.)

## Gambler's ruin

LL §7.4 closes the chapter with a story that turns the machinery loose on a real
question. Two players: $A$ starts with $\$a$, $B$ with $\$b$, and each round a
fair coin moves one dollar between them. Play until someone is broke. What is the
chance $A$ ends up with everything?

The slick argument LL gives leans on the very tools we just built. The game is
**fair**, so $A$'s expected fortune never changes — it stays at the starting $a$.
At the end $A$ holds either $a+b$ (probability $q$, the win) or $0$. Expectation is
linear and unchanged, so $q\,(a+b)+ (1-q)\cdot 0 = a$, giving
$$q=\frac{a}{a+b}.$$
We confirm it by simulation across several starting splits:

```python
<!-- include: code/bradfield/02-probability/07_gamblers_ruin.py -->
```

The moral is the one LL draws, and it is a genuinely useful piece of real-world
intuition: **against a much richer opponent, even a perfectly fair game ruins you
with high probability.** Starting with $\$1$ against an opponent's $\$999$, you
take it all only $1$ time in $1000$ — not because the game is rigged, but because
your tiny bankroll has far more chances to hit zero first. The house edge is often
just a bigger pile of chips.

## Working the problem set, and where to go deeper

The post-class problems live in **MCS 17.2–17.4** (chapters 17–21 in this reader),
which repackage the same ideas with more named machinery; LL chapter 7 is the
gentle on-ramp we just walked. The checklist worth carrying forward:

- **Uniform probability is counting with a denominator.** $P(A)=|A|/|S|$. The hard
  part is the count — which is the previous chapter.
- **Complement** when "at least one" is ugly: $P(E)=1-P(\bar E)$ (birthdays, hash
  collisions).
- **Independence is $P(A\cap B)=P(A)P(B)$ — check it, never assume it**, and never
  confuse it with *exclusive* ($A\cap B=\emptyset$), which is nearly the opposite.
- **Repeated independent trials give the binomial** $\binom{n}{k}p^k(1-p)^{n-k}$,
  a normalized row of Pascal.
- **Linearity of expectation** always holds (indicator method); **variance adds
  only under independence**, and the resulting $1/\sqrt n$ relative spread is the
  engine of concentration.
- **The Law of Large Numbers** is the Pascal triangle piling up around its center:
  the exact-center peak fades, the central band grows to certainty.

For a beautiful interactive build of this intuition, work through
[Seeing Theory](https://seeing-theory.brown.edu/); for a proper textbook,
Bertsekas & Tsitsiklis's *Introduction to Probability*. The next session sharpens
the *conditional* story — what happens to a probability once you learn something —
which is where Bayes' rule lives.
