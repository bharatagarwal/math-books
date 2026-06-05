# Generalize

Generalization is passing from one object to a set containing it, or from a restricted set to a more comprehensive one. In problem-solving it serves two purposes. The first is to reveal structure behind a particular fact. The second is stranger: it can make a problem *easier*.

## From one observation to a pattern

Start with a single numerical fact:

$$1^3 + 2^3 + 3^3 + 4^3 = 100 = 10^2.$$

A sum of cubes turns out to be a perfect square. Coincidence? You generalize: consider $1^3 + 2^3 + \cdots + n^3$. Then you specialize, computing small cases to see whether the pattern holds:

$$
\begin{aligned}
1 &= 1^2 \\
1 + 8 &= 9 = 3^2 \\
1 + 8 + 27 &= 36 = 6^2 \\
1 + 8 + 27 + 64 &= 100 = 10^2 \\
1 + 8 + 27 + 64 + 125 &= 225 = 15^2.
\end{aligned}
$$

Every sum is a square. The bases are $1, 3, 6, 10, 15$. Look at the differences between successive bases: $2, 3, 4, 5$. You recognize these bases as the triangular numbers:

$$
\begin{aligned}
1 &= 1 \\
3 &= 1 + 2 \\
6 &= 1 + 2 + 3 \\
10 &= 1 + 2 + 3 + 4 \\
15 &= 1 + 2 + 3 + 4 + 5.
\end{aligned}
$$

If the regularity is general, the conjecture takes a precise form:

$$1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2.$$

You arrived here by generalizing a single observation, specializing to compute cases, noticing a pattern among the cases, and generalizing again to state it precisely. The interplay between generalization and specialization is what drives discovery. (The proof by induction is a separate matter, treated in the chapter on Proof and Review.)

## The inventor's paradox

Now notice something about the conjecture you just formed. Your first observation was vague: "sums of cubes tend to be squares." That statement is almost useless. You cannot prove by induction that "the sum is some square" because you have no way to connect the square at step $n$ to the square at step $n + 1$. The vague statement has no handles.

The precise conjecture — that the sum equals $\left(\frac{n(n+1)}{2}\right)^2$ — is *stronger*. It says more. And yet it is easier to prove, because the inductive step has something concrete to verify. You check that if the identity holds for $n$, it holds for $n + 1$, and the algebra goes through cleanly.

This is the **inventor's paradox**. "The more ambitious plan may have more chances of success" — provided it is not based on mere pretension but on some vision of the things beyond those immediately present.

The paradox arises because a stronger statement carries more structure. The weaker statement is too shapeless to work with; the stronger one gives you enough grip to complete the argument. You are not making the problem harder. You are making it *more precise*, and precision is what proof needs.

## A second example: even and odd subsets

You want to show that among the subsets of $\{1, 2, \ldots, n\}$, exactly half have an even number of elements and half have an odd number (for $n \geq 1$). Counting each side separately leads to sums of binomial coefficients that are awkward to compare.

Generalize instead. Consider the stronger identity:

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0.$$

This says the alternating sum of all binomial coefficients vanishes — which implies the even-odd equality, since the positive terms sum to the same value as the negative terms. And the stronger statement yields immediately: it is $(1 - 1)^n = 0$ by the binomial theorem. The weaker statement resisted direct attack; the stronger one fell to a known identity.

The pattern is the same as with the sum of cubes. The more precise claim was easier to prove than the vaguer one.

## Replacing numbers with letters

A common and useful form of generalization: substitute variables for specific values. "Find the number of subsets of a $5$-element set" becomes "find the number of subsets of an $n$-element set." The problem in letters is more general, but it is also more *testable*. You can check the formula for $n = 0, 1, 2, 3$ before committing to it. The small cases may suggest the proof. And the algebraic form exposes structure that specific numbers obscure.

"How many ways can you distribute 12 identical balls into 4 distinct boxes?" Replace $12$ with $n$ and $4$ with $k$. Now you have the general stars-and-bars problem. The answer $\binom{n+k-1}{k-1}$ is easier to discover and prove than the specific numerical answer, because the general formulation reveals the combinatorial structure — choosing $k - 1$ dividers among $n + k - 1$ positions — that the specific numbers hide.

This move, simple as it sounds, gains access to new procedures: you can vary the data continuously, check boundary cases, and use algebraic identities. It transforms a single problem into a family of problems, and the family is often easier to understand than any single member.

## When to generalize

Not every problem benefits from generalization. The inventor's paradox applies when the specific case feels "too special" — when the particulars are getting in the way of the structure. Signs that generalization might help:

- A direct proof of a specific claim keeps failing, but you suspect a pattern behind the specific case.
- You are trying to prove something by induction, but the inductive hypothesis is too weak to carry the inductive step.
- The problem involves specific numbers that play no essential role. Replacing them with variables might expose the real mechanism.
- You have a conjecture that works for every case you test, but the statement is too vague to prove. Making it more precise (which usually means more general) may give it enough structure for a proof.

The risk of generalization is real: if you generalize in the wrong direction, you get a harder problem that is *also* shapeless. The inventor's paradox works only when the generalization is guided by "some vision of the things beyond those immediately present." Blind ambition is pretension. Guided ambition — informed by computed cases, noticed patterns, and structural intuition — is the paradox in action.

## Questions to keep

- *Is the specific case getting in the way?* Would a more general statement be easier to prove?
- *Is my inductive hypothesis strong enough?* Does it carry enough information to complete the inductive step, or do I need a more precise conjecture?
- *Can I replace numbers with letters?* Does the algebraic form expose structure that the specific values hide?
- *Am I generalizing with vision or with pretension?* Do I have evidence — computed cases, a noticed pattern — that the general statement is true?
