# Approximation

In 1894, Paul Bachmann introduced a notation in his *Analytische Zahlentheorie* for bounding the error in number-theoretic estimates: big-$O$. Edmund Landau adopted and systematized it, and it became the standard language of analytic number theory. Seventy years later, Donald Knuth brought it into computer science, where it became *the* way programmers talk about algorithmic efficiency. If you've ever said "this algorithm is $O(n \log n)$," you're using Bachmann-Landau notation. This chapter covers the full family of symbols that let you talk precisely about approximation.

## 1. Approximate equality of numbers

There are many notations used to capture the concept of being approximately equal. The simplest, and in our opinion the best, is $\approx$. For example, $\pi\approx 3.14$. People use a variety of other symbols for approximate equality including $\doteq$, $\cong$, $\sim$, and $\simeq$.

A more precise way to express approximate equality is to write $\pi=3.14\pm 0.002$ which is shorthand for

$$3.14-0.002\leq\pi\leq 3.14+0.002.$$

## 2. Asymptotic relations

A variety of notations exist to show the approximate equality of algebraic expressions (functions), to abbreviate "unimportant" terms, and to measure the quality of the approximation.

For example, one may write: when $x$ is small, $e^{x}\sim 1+x+\frac{1}{2}x^{2}$ or when $n$ is large, $\binom{n}{3}\sim n^{3}/6$. The symbol $\sim$ means *is asymptotic to* and asserts that the limit of the ratio of the two expressions approaches 1.

To be precise, suppose $f, g$ are functions of $x$.

- When $x$ is small, $f(x)\sim g(x)$ means

$$\lim_{x\to 0}\frac{f(x)}{g(x)}=1.$$

- When $x$ is large, $f(x)\sim g(x)$ means

$$\lim_{x\to\infty}\frac{f(x)}{g(x)}=1.$$

### Proportionality

The expression $f(x)\propto g(x)$ indicates that the two functions are proportional to each other. Strictly speaking, this means there is a positive number $k$ such that $f(x)=kg(x)$. However, $\propto$ can also be used in the approximate sense in which lower order terms are neglected, e.g., $\binom{n}{3}\propto n^{3}$. In this case $f(x)\propto g(x)$ means that $f(x)/g(x)$ tends to a finite, nonzero limit as $x\to\infty$.

### Asymptotic equivalence ($\asymp$)

The symbol $\asymp$ expresses a similar, but even less restrictive, notion of approximate equality. The ratio between the two expressions need not tend to a limit; all that is required is that the ratio be bounded away from 0 and $\infty$.

More precisely, let $f,g:\mathbb{R}\to \mathbb{R}_{+}$. The expression $f\asymp g$ means that there are positive numbers $t, a$, and $b$ such that for all $x\geq t$, $a\leq f(x) / g(x)\leq b$. Using quantifier notation:

$$\exists\, t, a, b > 0,\; \forall\, x \geq t,\quad a \leq \frac{f(x)}{g(x)} \leq b.$$

This can also be expressed: when $x$ is sufficiently large, $a \leq \frac{f(x)}{g(x)} \leq b$.

In some cases, the expression $f(x) \asymp g(x)$ may be applied to functions that return negative values. In that case, we mean that $a \leq |f(x) / g(x)| \leq b$ when $x$ is sufficiently large.

## 3. Big-$O$ notation and its relatives

This is the notation that every programmer knows, even if they don't realize it has a formal mathematical definition. When you say "binary search is $O(\log n)$," you are making a precise asymptotic claim: the number of comparisons grows no faster than some constant times $\log n$ for sufficiently large $n$.

The formal statement $f \in O(g)$ is exactly the claim "this function grows at most as fast as $g$, up to a constant factor." The table below summarizes the full Bachmann-Landau family:

| Notation | Name | Meaning | Analogy |
| --- | --- | --- | --- |
| $f = O(g)$ | Big-O | $\|f\| \leq c\|g\|$ eventually | $\leq$ (up to constant) |
| $f = \Omega(g)$ | Big-Omega | $\|f\| \geq c\|g\|$ eventually | $\geq$ (up to constant) |
| $f = \Theta(g)$ | Big-Theta | $c_1\|g\| \leq \|f\| \leq c_2\|g\|$ | $=$ (up to constant) |
| $f = o(g)$ | Little-o | $f/g \to 0$ | $<$ (strictly slower) |
| $f = \omega(g)$ | Little-omega | $f/g \to \infty$ | $>$ (strictly faster) |

### Big-$O$

The big-$O$ notation of Landau is a useful shorthand for giving an approximate bound for a function or for indicating (relatively) unimportant terms in an expression.

For example, $\binom{n}{3} = \frac{1}{6} n^3 - \frac{1}{2} n^2 + \frac{1}{3} n$. However, the behavior of $\binom{n}{3}$ for $n$ large is dominated by the first term, $\frac{1}{6} n^3$. The remaining terms are "on the order of" $n^2$ (or smaller). Thus we may write $\binom{n}{3} = \frac{1}{6} n^3 + O(n^2)$. We may also write $\binom{n}{3} = O(n^3)$ to indicate that $\binom{n}{3}$ is "of the order" $n^3$ (or smaller).

Another example: For $x$ near 0, $e^x$ is approximately 1. More precisely, $e^x = 1 + x + O(x^2)$. The remaining terms are "of the order" $x^2$ (or smaller).

The meaning of the notation $f(x) = O(g(x))$ depends on the context: is $x$ near zero or is $x$ large?

- In the case of $x$ near 0, the notation $f(x) = O(g(x))$ means there are positive numbers $\epsilon$ and $b$ such that for all $x$ between $-\epsilon$ and $\epsilon$ we have

$$\left| \frac{f(x)}{g(x)} \right| \leq b.$$

More informally, we say: when $x$ is sufficiently small, $|f(x) / g(x)|$ is bounded by $b$.

- In the case of large $x$, the notation $f(x) = O(g(x))$ means something similar: there are positive numbers $t$ and $b$ so that for all $x \geq t$ we have

$$\left| \frac{f(x)}{g(x)} \right| \leq b.$$

An expression such as $e^x = 1 + x + O(x^2)$ means $e^x - 1 - x = O(x^2)$.

One rarely (if ever) sees the big-$O$ on the left side of an equation.

An equation of the form $\binom{n}{3} = O(n^3)$ is mildly illogical. The equal sign ought to mean that the two surrounding expressions are the same, and in this case they are not really the same thing. It is more proper to write $\binom{n}{3} \in O(n^3)$ and understand $O(n^3)$ as the set of all functions that are asymptotically bounded by $n^3$. In practice, most people use the equal sign and tacitly understand not to interpret it in a strict sense.

Some people use a fancy, calligraphic $\mathcal{O}$ for the big-$O$ notation.

### Big-$O$ in SymPy

SymPy's `series()` function produces big-$O$ terms automatically -- the same notation, made computational. When you expand $\sin(x)$ as a Taylor series, the truncation error is an `O(x^n)` object you can inspect, manipulate, and strip away:

<!-- include: code/mathematical-notation/10 - Approximation/01_python.py -->

This is exactly the $e^x = 1 + x + O(x^2)$ from the definition above, but now the computer carries the error bound for you.

### Big-$\Omega$ and Big-$\Theta$

The notation $f(x) = O(g(x))$ is an implicit *upper* bound on $|f(x)|$. It asserts that $|f(x)| \leq b|g(x)|$ where $b$ is some positive number. Thus it is correct to write $\binom{n}{3} = O(n^4)$.

The notation $f(x) = \Omega(g(x))$ is a *lower* bound on $f(x)$. The precise meaning depends on whether we are considering small or large values of $x$:

- In the case of $x$ near 0, the notation $f(x) = \Omega(g(x))$ means there are positive numbers $\epsilon$ and $b$ such that for all $x$ between $-\epsilon$ and $\epsilon$ we have

$$\left| \frac{f(x)}{g(x)} \right| \geq b.$$

- In the case of large $x$, the notation $f(x) = \Omega(g(x))$ means something similar: there are positive numbers $t$ and $b$ so that for all $x \geq t$ we have

$$\left| \frac{f(x)}{g(x)} \right| \geq b.$$

Because $\Omega$ represents a lower bound, it is correct to write $\binom{n}{3} = \Omega(n^2)$.

Finally, the notation $f(x) = \Theta(g(x))$ means that both $f(x) = O(g(x))$ and $f(x) = \Omega(g(x))$ hold. That is, there are positive constants $a$ and $b$ so that for all sufficiently large (or small) $x$ we have

$$a \leq \left| \frac{f(x)}{g(x)} \right| \leq b.$$

Note that

$$f(x) = \Theta(g(x)) \iff f(x) \asymp g(x) \iff g(x) = \Theta(f(x)).$$

Thus it is correct to write $\binom{n}{3} = \Theta(n^3)$ but it is incorrect to write $\binom{n}{3} = \Theta(n^k)$ for any $k \neq 3$.

### Little-$o$ and Little-$\omega$

The notation $f(x) = o(g(x))$ indicates that $f(x)$ is very much smaller than $g(x)$ in the sense that their ratio tends to zero. As with other notation we've seen, the precise meaning depends on context: small $x$ or large $x$. In the appropriate case, $f(x) = o(g(x))$ means one of the following:

$$\lim_{x \to 0} \frac{f(x)}{g(x)} = 0 \qquad \text{or} \qquad \lim_{x \to \infty} \frac{f(x)}{g(x)} = 0.$$

For example, when $x$ is small, $\cos x = 1 - \frac{1}{2}x^2 + o(x^3)$, and when $n$ is large, $n! = o(n^n)$.

A $o(1)$ term in an expression stands for a quantity that tends to 0.

The notation $f(x) = \omega(g(x))$ has the opposite meaning; that is, $f(x)$ is much larger than $g(x)$. Concisely,

$$f(x) = \omega(g(x)) \iff g(x) = o(f(x)).$$

In other words, depending on context, $f(x) = \omega(g(x))$ means one of the following:

$$\lim_{x \to 0} \left| \frac{f(x)}{g(x)} \right| = \infty \qquad \text{or} \qquad \lim_{x \to \infty} \left| \frac{f(x)}{g(x)} \right| = \infty.$$

In an expression, $\omega(1)$ represents a term that is tending to infinity.

### The $\ll$ and $\gg$ shorthand

Alternative ways to express the relations $f(x) = o(g(x))$ and $f(x) = \omega(g(x))$ are, respectively, $f(x) \ll g(x)$ and $f(x) \gg g(x)$. The relation $\ll$ expresses the notion of *much less than* and $\gg$ indicates *much greater than*.

For example, for $n$ large, we have $n^5 \ll 2^n$ and $n^n \gg n!$ because

$$\lim_{n \to \infty} \frac{n^{5}}{2^{n}} = 0 \qquad \text{and} \qquad \lim_{n \to \infty} \frac{n^{n}}{n!} = \infty.$$

### Bridge to programming

If you've done any algorithm analysis, you already use this notation daily:

| Code pattern | Time complexity | What the notation means |
| --- | --- | --- |
| `for i in range(n)` | $O(n)$ | linear scan |
| binary search | $O(\log n)$ | halving each step |
| nested loops | $O(n^2)$ | all pairs |
| mergesort | $O(n \log n)$ | divide-and-conquer |
| Fibonacci (naive) | $O(2^n)$ | exponential blowup |

The formal definition is the same one above: mergesort does at most $c \cdot n\log n$ comparisons for some constant $c$ and all sufficiently large $n$. When you say "$O(n \log n)$" in a code review, you are invoking Landau's 1909 notation.
