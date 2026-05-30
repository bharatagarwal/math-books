# Induction and Recursive Data Types

Induction is the proof technique that makes discrete mathematics tick, and it is the same idea a programmer already uses every day: a recursive function works because it works on the base case and because each call reduces to a smaller call that also works. MCS puts it bluntly — induction's use "is a defining characteristic of discrete, as opposed to continuous, mathematics." This chapter follows Lovász & Vesztergombi (*Discrete Mathematics*, "LL") chapter 3, which introduces induction through a sequence of concrete summation examples, and the MIT *Mathematics for Computer Science* ("MCS") chapter 5, which gives the formal template, strong induction, and the structural-induction flavor that connects directly to recursive data types.

## Discovering a pattern: the sum of odd numbers

LL does not open with the principle; it opens with a surprise. Add up the first few odd numbers and watch what comes out:

$$
\begin{aligned}
1 &= 1 \\
1+3 &= 4 \\
1+3+5 &= 9 \\
1+3+5+7 &= 16 \\
1+3+5+7+9 &= 25.
\end{aligned}
$$

Those right-hand sides are the perfect squares. Before proving anything, it is worth feeling the discovery the way LL stages it — compute the running sums and *notice* they are squares. This intuition demo prints the partial sums and their square roots without assuming the answer:

```python
<!-- include: code/bradfield/06-induction/00_discover_odd_sums.py -->
```

The running sums come out `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` and their square roots are `[1, 2, 3, ..., 10]` exactly. So we are led to the conjecture

$$1 + 3 + 5 + \cdots + (2n-1) = n^2.$$

LL is careful here: we now have an *infinite* family of statements, one per $n$. Checking any finite number of them never settles the next one. That gap is exactly what induction closes.

### Why it works: the gnomon

There is a reason the odd numbers build squares, and you can see it. To grow an $(n-1)\times(n-1)$ square into an $n\times n$ square you add an L-shaped border — a *gnomon* — running down the new right column and along the new bottom row. That border has $n + n - 1 = 2n-1$ cells: the $n$-th odd number. So passing from $(n-1)^2$ to $n^2$ costs exactly $2n-1$, which *is* the inductive step, made geometric. This demo builds the grid layer by layer and confirms each gnomon has $2k-1$ cells:

```python
<!-- include: code/bradfield/06-induction/02_gnomon_squares.py -->
```

Running it labels each cell with the layer it joined, drawing the nested L's, and asserts `added == 2k - 1` for every layer. The final grid makes the argument visible:

```
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
```

## The induction principle

LL states the idea informally; MCS gives it as a principle worth memorizing.

**The Induction Principle.** Let $P(n)$ be a predicate. If

- $P(0)$ is true (the **base case**), and
- for all $n \in \mathbb{N}$, $P(n)$ implies $P(n+1)$ (the **inductive step**),

then $P(n)$ is true for all $n \in \mathbb{N}$.

The picture MCS uses is dominoes, or a magic chocolate bar handed down the row: $P(0)$ tips the first domino, and the step says each domino knocks over the next. For the odd-sum conjecture, take $P(n)$ to be "$1 + 3 + \cdots + (2n-1) = n^2$." The base case $P(1)$ reads $1 = 1^2$. For the step, assume $P(n_0)$ and add the next odd number, $2n_0 + 1$:

$$
\underbrace{1 + 3 + \cdots + (2n_0 - 1)}_{n_0^2} + (2n_0+1) = n_0^2 + 2n_0 + 1 = (n_0+1)^2,
$$

which is $P(n_0+1)$. The chain is complete.

MCS distills proofs like this into a five-part **template**:

1. State that the proof is by induction.
2. Define the predicate $P(n)$ explicitly.
3. Prove the base case.
4. Prove the inductive step: assume $P(n)$, derive $P(n+1)$.
5. Conclude $P(n)$ holds for all $n$.

## Little Gauss and the other closed forms

LL's running example is the schoolboy-Gauss sum. Told to add the integers from $1$ to $100$, Gauss wrote the sum forwards and backwards and added columnwise:

$$
\begin{aligned}
S &= 1 + 2 + \cdots + 99 + 100 \\
S &= 100 + 99 + \cdots + 2 + 1,
\end{aligned}
$$

so each of the $100$ columns sums to $101$, giving $2S = 100 \cdot 101$ and $S = 5050$. In general,

$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}.$$

The same induction proves it: assuming the formula for $n_0$, adding $n_0+1$ gives $\frac{n_0(n_0+1)}{2} + (n_0+1) = \frac{(n_0+1)(n_0+2)}{2}$. LL then chains on two more closed forms — the sum of squares,

$$1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6},$$

(harder to *guess* from the values $1, 5, 14, 30, 55, \dots$, but easy to *prove* once stated), and the sum of powers of two,

$$1 + 2 + 4 + \cdots + 2^n = 2^{n+1} - 1$$

(e.g. $1+2+4+8 = 15 = 16-1$). This verification demo checks all four LL closed forms two ways: by brute summation for many $n$, and symbolically with sympy, which evaluates each $\Sigma$ to a closed form and confirms it equals LL's:

```python
<!-- include: code/bradfield/06-induction/01_induction_sums.py -->
```

The numeric pass covers $n = 0\ldots49$, and sympy reports `sum of odds = n**2`, `little Gauss = n*(n+1)/2`, `sum of squares = n*(n+1)*(2*n+1)/6`, and `powers of two = 2**(n+1) - 1` — the four formulas, derived rather than asserted.

### The loop invariant is the inductive hypothesis

The clearest place a programmer meets induction is the **loop invariant**: a statement that is true before the loop, preserved by every iteration, and therefore true at the end. That is literally base case plus inductive step. Dafny lets us make it machine-checked. Here the little-Gauss sum is computed by a loop whose invariant says "`s` already holds $1+2+\cdots+(i-1) = (i-1)i/2$"; Dafny proves the invariant holds initially, is preserved each step, and — combined with the loop guard — yields the postcondition `s == n*(n+1)/2`. The same file also gives a recursive `SumTo` with a lemma proved by recursion, which is ordinary induction expressed directly:

```dafny
<!-- include: code/bradfield/06-induction/03_gauss_sum.dfy -->
```

Running `dafny verify` reports `2 verified, 0 errors`: the loop method and the recursive lemma both pass. Note Dafny discharges the base case of the lemma automatically and only needs the recursive call `GaussClosedForm(n-1)` — the inductive hypothesis — to close the step.

## Subset counting, revisited by induction

In the counting chapter we found that an $n$-element set has $2^n$ subsets by the doubling argument. LL gives a second proof, by induction, to show the technique generalizes. For $n=0$ the empty set has exactly one subset (itself) and $2^0 = 1$. For $n > 0$, pick an element $x$ of an $n$-set $S$. Subsets split into those *not* containing $x$ — exactly the subsets of $S \setminus \{x\}$, of which there are $2^{n-1}$ by hypothesis — and those *containing* $x$, each obtained by adding $x$ to a subset of $S \setminus \{x\}$, again $2^{n-1}$. Adding the disjoint cases gives $2^{n-1} + 2^{n-1} = 2^n$. The induction hypothesis does the same work the "double on each new element" argument did, now stated as a chain.

## Strong induction

Sometimes $P(n)$ depends not just on $P(n-1)$ but on *several* earlier cases. MCS gives the stronger principle for exactly this.

**The Strong Induction Principle.** Let $P(n)$ be a predicate. If

- $P(0)$ is true, and
- for all $n$, the assumptions $P(0), P(1), \ldots, P(n)$ together imply $P(n+1)$,

then $P(n)$ holds for all $n \in \mathbb{N}$.

It proves exactly the same kinds of statements as ordinary induction; it just lets the step reach back to *all* smaller cases at once. MCS gives two textbook examples, and we check both.

**Products of primes.** Every integer $n > 1$ is a product of primes. Base case: $2$ is prime. Step: if $n+1$ is prime we are done; otherwise $n+1 = a\cdot b$ with $1 < a, b < n+1$, and by the strong hypothesis both $a$ and $b$ are products of primes, hence so is $n+1$. Ordinary induction would not suffice — we need the result for $a$ and $b$, which are *somewhere* below $n+1$, not specifically at $n$.

**Postage stamps.** With $3$- and $5$-cent stamps, every postage of $8$ cents or more is makeable. Base cases $8 = 3+5$, $9 = 3+3+3$, $10 = 5+5$; for $n \ge 11$, $n-3 \ge 8$ is makeable by hypothesis, so add a $3$-cent stamp. This verification demo checks both theorems — the postage claim for $n = 8\ldots199$ (and confirms the only gaps below $8$ are $1, 2, 4, 7$), and the prime-product claim for $n = 2\ldots499$ by factoring each and multiplying back:

```python
<!-- include: code/bradfield/06-induction/04_strong_induction.py -->
```

It prints `all postage >= 8 makeable; gaps below 8 are 1,2,4,7` and `every n in 2..499 is a product of primes`. The factorization function mirrors the proof: it peels off the smallest factor and recurses on a strictly smaller number that the hypothesis already handles.

## Structural induction and recursive data types

The form of induction closest to programming is **structural induction**, which MCS previews at the end of chapter 5. Instead of inducting on a number, we induct on the *structure* of a recursively defined object. A type is defined by base constructors and construction rules; you prove a property by proving it for the base constructors and proving that each rule preserves it. That is ordinary induction with "smaller" meaning "structurally simpler."

Take full binary trees, defined recursively:

$$\text{Tree} = \text{Leaf} \;\mid\; \text{Node}(\text{Tree}, \text{Tree}).$$

A natural conjecture: in any such tree, the number of leaves equals the number of internal nodes plus one. Rather than assert it, this intuition demo builds random trees and prints the two counts side by side — discovery first — then turns the observation into a check over thousands of random shapes:

```python
<!-- include: code/bradfield/06-induction/05_structural_trees.py -->
```

The table comes out with `leaves == internal + 1` `True` in every row (e.g. `11` leaves and `10` internal nodes), and the invariant holds for all `5000 random trees`. The structural-induction proof is short and matches the constructors exactly:

- **Base case (Leaf):** one leaf, zero internal nodes; $1 = 0 + 1$. ✓
- **Inductive step (Node):** a node joins two subtrees with leaf/internal counts $(L_1, I_1)$ and $(L_2, I_2)$, each satisfying $L_i = I_i + 1$ by hypothesis. The combined tree has $L_1 + L_2$ leaves and $1 + I_1 + I_2$ internal nodes, and indeed $L_1 + L_2 = (I_1+1) + (I_2+1) = (1 + I_1 + I_2) + 1$. ✓

This is the bridge MCS points at: a recursive data type comes with its own induction principle, one case per constructor, and proving a property about every value of the type is exactly proving it constructor by constructor.

## A word of caution

LL closes with the famous bogus proof that "all horses are the same color." The inductive step quietly assumes that two overlapping subgroups of horses share a horse — true for large groups, but it fails precisely at $n_0 = 1 \to 2$, where the two singletons do not overlap. The lesson, which the gnomon and the tree proofs both respect: the inductive step must hold for *every* $n_0$ down to the smallest, and the base case must actually be covered. A single gap breaks the whole chain — the same way one missing iteration breaks a loop invariant.

## Working the problem set

The post-session problems are MCS chapter 5: **5.1** (a direct sum identity, the odd-sum/little-Gauss style — set up $P(n)$ and grind the step), **5.4** and **5.7** (more summation and divisibility inductions), **5.8** (a strong-induction argument in the products-of-primes/postage family — identify why ordinary induction is not enough), **5.13** (an inductive inequality), and the stretch **5.21**. The demos here are the computational rehearsal: for each, *discover* the pattern numerically first (like `00_discover_odd_sums.py`), then state $P(n)$, then check the closed form both by brute force and symbolically before writing the formal step.

## Where to go deeper

- **LL chapter 3** develops induction entirely through concrete sums — odd numbers, little Gauss, squares, powers of two — plus the subset-count re-proof and the all-horses caution.
- **MCS chapter 5** gives the formal templates for ordinary and strong induction, the products-of-primes and postage examples, and the structural-induction preview that leads into recursive data types.
- The connection to programming is the **loop invariant** (verified here in Dafny) and the **recursive datatype**, where structural induction becomes the proof method that matches your `match`/`case` code one branch at a time.
