# Try Small Cases

You have a problem about $n$ objects, or $n$ steps, or $n$-element sets. You do not see the answer for general $n$. So you try $n = 1$. Then $n = 2$. Then $n = 3$. You write down what happens. You look at what you wrote down.

This is specialization—the experimentalist's move. You do not yet know whether the general statement is true, so you test it. You do not yet see how to solve the general problem, so you solve a special case and look for a pattern. Polya calls it "passing from a set to a smaller set, or to a single object." It is the most concrete thing you can do when the abstract problem gives you nothing to hold onto.

## Compute, then look

The first step is computation. Not clever computation—brute computation. List every case. Count by hand. The point is not efficiency; the point is *data*.

To count the subsets of an $n$-element set, start with small values:

| $n$ | subsets | count |
|---|---|---|
| $0$ | $\{\emptyset\}$ | $1$ |
| $1$ | $\emptyset, \{1\}$ | $2$ |
| $2$ | $\emptyset, \{1\}, \{2\}, \{1,2\}$ | $4$ |
| $3$ | (all eight) | $8$ |

The pattern $1, 2, 4, 8$ suggests $2^n$. You did not need insight to produce the table. You needed patience, and a willingness to start with the trivial case $n = 0$.

The second step is looking. The table is not the answer—the table is the raw material. Stare at the numbers. Compute differences. Compute ratios. Write the sequence in a different form. The pattern is in there; your job is to see it.

## The table as instrument

A table does three things for you. First, it externalizes memory. You no longer need to hold all the cases in your head; they are in front of you, organized. Second, it invites comparison. Numbers in a column beg to be compared—you see growth, you see repetition, you see anomalies. Third, it creates a commitment. Once you have filled in five rows, you feel the pull to fill in the sixth, and the sixth row may be the one that breaks the pattern open.

Polya's sum-of-cubes discovery runs entirely on this mechanism:

$$
\begin{aligned}
1^3 &= 1 = 1^2 \\
1^3 + 2^3 &= 9 = 3^2 \\
1^3 + 2^3 + 3^3 &= 36 = 6^2 \\
1^3 + 2^3 + 3^3 + 4^3 &= 100 = 10^2 \\
1^3 + 2^3 + 3^3 + 4^3 + 5^3 &= 225 = 15^2.
\end{aligned}
$$

The sums are squares. That alone is interesting. But look at the bases of the squares: $1, 3, 6, 10, 15$. The differences between consecutive bases are $2, 3, 4, 5$. So the bases are triangular numbers—partial sums $1 + 2 + \cdots + n$. The conjecture:

$$1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2.$$

None of this required any technique beyond computing five cases and looking at the results twice—once at the sums, once at their square roots.

## What to look for in small cases

Not every pattern announces itself. Here are the things worth checking when you have a column of numbers:

- **Differences.** If the sequence is $1, 2, 4, 7, 11$, the first differences are $1, 2, 3, 4$—an arithmetic progression. That tells you the original sequence is quadratic in $n$.
- **Ratios.** If consecutive terms double, you are looking at an exponential. The subset counts $1, 2, 4, 8$ have constant ratio $2$.
- **Factorizations.** Write each term in terms of $n$. The sequence $1, 1, 3, 16, 125$ for labeled trees on $n$ vertices becomes $1^0, 1^0, 3^1, 4^2, 5^3$—which is $n^{n-2}$.
- **Known sequences.** Do the numbers match something you have seen before? Triangular numbers, Catalan numbers, Fibonacci numbers, powers of $2$?

The act of checking these is itself a form of specialization. You are not solving the problem; you are interrogating the data.

## Extreme and degenerate cases

Small cases shade into extreme cases. What happens at the boundary? When the parameter is $0$, or $1$, or as large as it can be?

You conjecture that $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. Before attempting a proof, check:

- $k = 0$: one way to choose nothing. $\binom{n}{0} = \frac{n!}{0! \cdot n!} = 1$. Good.
- $k = n$: one way to choose everything. $\binom{n}{n} = 1$. Good.
- $k = 1$: $n$ ways to choose one element. $\binom{n}{1} = n$. Good.

These checks are fast. Any formula that fails one of them is certainly wrong. And they do more than test—they *constrain*. The correct formula must give $1$ at both ends and $n$ when $k = 1$. These boundary values narrow the space of plausible guesses.

Extreme cases are particularly instructive, Polya notes, because they are apt to be overlooked by the inventors of conjectures. If your guess survives an extreme case, the inductive evidence is strong—precisely because the prospect of refutation was high.

## Specialization as stepping stone

Sometimes you solve a small case not to find a pattern but to find a *mechanism*. You want a proof strategy for general $n$, and the small case shows you the moving parts.

You want to show that in any sequence of $n^2 + 1$ distinct real numbers, there is an increasing subsequence of length $n + 1$ or a decreasing one of length $n + 1$. Try $n = 2$: any sequence of $5$ distinct numbers must contain a monotone subsequence of length $3$.

The case is small enough to examine by hand. Assign to each element the length of the longest increasing subsequence ending there. If any element gets length $3$, you are done. If not, every element gets length $1$ or $2$—only two possible values for five elements. By pigeonhole, three elements share the same value. Those three, having equal longest-increasing-subsequence lengths, must form a decreasing subsequence.

The mechanism—pigeonhole on subsequence lengths—is the proof for general $n$. You found it by making the problem small enough to see all the parts at once.

## The recurring example

Return to subsets of $\{1, 2, \ldots, n\}$. You built the table, saw the pattern $2^n$, and proved it by the binary-string bijection. Now specialize differently: count only subsets of size exactly $k$.

Fix $n = 4$ and build a table by $k$:

| $k$ | subsets of $\{1,2,3,4\}$ with $k$ elements | count |
|---|---|---|
| $0$ | $\emptyset$ | $1$ |
| $1$ | $\{1\}, \{2\}, \{3\}, \{4\}$ | $4$ |
| $2$ | $\{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\}$ | $6$ |
| $3$ | $\{1,2,3\}, \{1,2,4\}, \{1,3,4\}, \{2,3,4\}$ | $4$ |
| $4$ | $\{1,2,3,4\}$ | $1$ |

The row of counts is $1, 4, 6, 4, 1$. You recognize Pascal's triangle. The count for size $k$ is $\binom{4}{k}$.

Now the small-cases move links two results: the total number of subsets is $\sum_{k=0}^{n} \binom{n}{k}$, and you already know the total is $2^n$. So $\sum_{k=0}^{n} \binom{n}{k} = 2^n$, which is the binomial theorem at $x = 1$. A table for a single value of $n$ connected three ideas: the subset count, binomial coefficients, and the binomial theorem.

## When small cases mislead

Small cases are evidence, not proof. The sequence $1, 2, 4, 8, 16$ for the number of regions defined by $n$ points on a circle continues with $31$, not $32$. If you had only computed five terms, you would have guessed $2^n$ and been wrong.

The defense is not to stop using small cases. The defense is to compute *enough* cases, and to remember that the pattern you see is a conjecture until proved. Small cases generate hypotheses. They do not settle them.

## Questions to keep

- *What happens for $n = 0, 1, 2, 3$?* Can I compute each case by hand?
- *What pattern do the small cases suggest?* Differences, ratios, factorizations—what structure is hiding in the numbers?
- *Does the conjecture survive the extreme cases?* What happens when a parameter vanishes, or equals its maximum?
- *Did the small case reveal a mechanism I can generalize?*
