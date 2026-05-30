# Revision and Problem Solving

*Bradfield session 12 · Thursday 23 July · capstone · further reading: Discrete
Mathematics using a Computer; the Princeton Companions*

The final session is for consolidation — and the best way to consolidate is to
solve problems that *refuse to stay in one chapter*. The whole point of this
course is that counting, probability, logic, proof, induction, linear algebra,
graphs, and number theory are one connected subject, not twelve. The deepest
results are exactly the ones where two sessions collide: a divisibility fact that
turns out to be a *count*, a graph invariant that turns out to be a
*determinant*, a probability that turns out to hide $\pi$. Below are five
capstone problems, each deliberately straddling several sessions, and each — in
the spirit of the whole reader — *discovered* by building small cases and looking,
*then* pinned down by a verified solution. If these read as natural rather than
surprising, the course has done its job.

## Counting meets probability: the coupon collector

*Sessions tied together: 1 (Counting) · 2 (Probability).*

*How many random draws does it take to collect all $n$ distinct coupon types?*
This braids together counting (the sample space of draws) and probability
(geometric waiting times), and it leans on the technique that has paid off more
than any other in the course — **linearity of expectation** (session 2). The
naive instinct is to despair at the dependence between stages; linearity makes
that irrelevant. Split the wait into stages: while you already hold $i$ distinct
types, a fresh draw is "new" with probability $\frac{n-i}{n}$, so the number of
draws to get the next new type is *geometric* with that success probability, and
its expectation is the reciprocal $\frac{n}{n-i}$. Adding the stage expectations
(linearity does not care that the stages are dependent),
$$\mathbb{E}[\text{draws}] = \sum_{i=0}^{n-1} \frac{n}{n-i}
  = n\sum_{k=1}^{n}\frac1k = n\,H_n,$$
the $n$-th harmonic number times $n$ — and since $H_n \approx \ln n$, this is
about $n\ln n$. (That is exactly why randomized load balancing and randomized
testing need $\sim n\ln n$ trials to *cover* $n$ cases, not $n$.) The exact
closed form and a 30,000-run simulation agree:

```python
<!-- include: code/bradfield/12-revision/01_coupon_collector.py -->
```

## Counting meets number theory: consecutive products

*Sessions tied together: 1 (Counting) · 10 (Number Theory).*

*Prove that the product of any $k$ consecutive integers is divisible by $k!$.* A
direct number-theoretic argument — tracking the power of each prime in numerator
and denominator (the Legendre-formula bookkeeping of session 10) — works but is
fiddly. The elegant proof is a **counting** argument: the quotient
$$\frac{m(m+1)\cdots(m+k-1)}{k!} = \binom{m+k-1}{k}$$
is a *binomial coefficient*. A binomial coefficient **counts** a set of things
(here, the multisets of size $k$ from $m$ symbols — stars and bars, session 1), so
it is necessarily a whole number — hence $k!$ divides the product. A divisibility
fact proved by realizing a fraction *secretly counts something*: that is the
spirit of discrete math in one line. We check both halves — the divisibility and
the binomial identity — exhaustively over many $(m,k)$:

```python
<!-- include: code/bradfield/12-revision/02_consecutive_product.py -->
```

## Probability meets number theory: when are two integers coprime?

*Sessions tied together: 2 (Probability) · 10 (Number Theory) · 1 (Counting).*

Here is the capstone that surprises everyone the first time, because it produces
$\pi$ out of nowhere. *Pick two integers at random. What is the probability they
are coprime — that $\gcd(a,b)=1$?* It braids probability (a limiting ratio over a
growing sample space) with number theory (divisibility and the totient world of
session 10), and the answer is the astonishing
$$\Pr[\gcd(a,b)=1] = \frac{6}{\pi^2} \approx 0.6079.$$

True to the reader's method, we **discover** it before we explain it: grow the
range $N$, literally count the coprime ordered pairs in $\{1,\dots,N\}^2$, and
watch the fraction settle. Then we discover the *mechanism* prime by prime. A pair
fails to be coprime exactly when **some** prime divides both. A random integer is
divisible by a prime $p$ with probability $1/p$, so two independent integers are
*both* divisible by $p$ with probability $1/p^2$, and "$p$ divides neither/only
one" has probability $1 - 1/p^2$. Treating distinct primes as independent events
(the Chinese-remainder intuition from session 10) and multiplying gives an **Euler
product**:
$$\Pr[\gcd(a,b)=1] = \prod_{p \text{ prime}} \left(1 - \frac{1}{p^2}\right).$$
The demo prints the empirical fraction as $N$ grows *and* the partial products of
that prime-by-prime sieve, and both descend toward the same number:

```python
<!-- include: code/bradfield/12-revision/05_coprime_discover.py -->
```

Why is that product $6/\pi^2$? Because it is the reciprocal of one of the most
famous sums in mathematics. Euler's product formula for the Riemann zeta function
says $\prod_p \frac{1}{1 - 1/p^2} = \sum_{k\ge 1}\frac{1}{k^2} = \zeta(2)$, and
Euler also evaluated that sum exactly:
$$\zeta(2) = \sum_{k=1}^{\infty}\frac{1}{k^2} = \frac{\pi^2}{6}.$$
So the coprime probability is $1/\zeta(2) = 6/\pi^2$. The verification confirms
Euler's $\zeta(2)$ identity *symbolically* with `sympy`, checks the prime product
over the primes below $5000$ against $6/\pi^2$, and matches a direct empirical
count — three independent routes to the same constant:

```python
<!-- include: code/bradfield/12-revision/06_coprime_verify.py -->
```

That $\pi$ should govern a question about *integers* having no common factor is
the kind of cross-topic surprise this whole course is built to make feel
inevitable rather than magical.

## Graphs meet linear algebra: counting spanning trees

*Sessions tied together: 9 (Graph Theory) · 7–8 (Linear Algebra).*

*How many spanning trees does a graph have?* The answer fuses graph theory with
the determinant-and-eigenvalue machinery of sessions 7–8. **Kirchhoff's
Matrix-Tree theorem** says: form the **Laplacian** $L = D - A$ (the diagonal
degree matrix minus the adjacency matrix); then the number of spanning trees
equals **any cofactor** of $L$ — delete one matching row and column and take the
determinant — and *also* equals the **product of the nonzero eigenvalues** of $L$
divided by $n$. A purely combinatorial counting question answered both by a
*determinant* and by a *spectrum* is about as cross-disciplinary as discrete math
gets; it is the bridge that makes "spectral graph theory" a phrase. We check both
formulas against a literal enumeration of the spanning trees of a small graph:

```python
<!-- include: code/bradfield/12-revision/03_matrix_tree.py -->
```

## Logic meets graphs: coloring as constraint solving

*Sessions tied together: 4 (Logic) · 9 (Graph Theory) · 5 (Proofs).*

Finally, the loop back to where the proofs began. Graph $k$-coloring (session 9)
is naturally a **constraint-satisfaction problem** (session 4): a variable per
vertex ranging over $k$ colors, the constraint that adjacent vertices differ, and
the question of whether a satisfying assignment exists. Handing it to `z3`
reproves the **odd-cycle obstruction** from the graph chapter *by machine* — the
$5$-cycle is $3$-colorable but **not** $2$-colorable, i.e. not bipartite, because
an odd cycle cannot be two-colored — and it pins the Petersen graph's chromatic
number at $3$. Note the distinction that this entire course has been about: a
*test* could only ever report "found a coloring" or "haven't found one yet"; the
solver returns **unsat**, a *proof* that no $2$-coloring can exist (session 5).
That gap between "didn't find" and "cannot exist" is the difference between
testing and verification:

```python
<!-- include: code/bradfield/12-revision/04_z3_coloring.py -->
```

## Where to go from here

You now have the discrete-math spine — counting, probability, logic, proof,
induction, graphs, number theory — plus a working linear-algebra intuition and,
threaded throughout, the programmer's superpower of *checking* mathematics with
`sympy`, `z3`, `numpy`, `networkx`, and Dafny rather than merely believing it.
Look back at the five capstones above: not one of them lives in a single session,
and that is the real lesson. The named tricks transfer (linearity of expectation,
the bijection rule, "a fraction that counts is an integer," the
determinant-as-invariant), but more importantly the *habit* transfers — build the
small case, watch the pattern, then prove and verify.

Two books to keep going, per the original syllabus. *Discrete Mathematics using a
Computer* (Hall & O'Donnell) re-teaches this same material through short Haskell
programs — a natural next step if you enjoyed the "make the math executable"
approach here. And the 1000-plus-page *Princeton Companion to Applied
Mathematics*, with its pure-math sibling the *Princeton Companion to
Mathematics*, is the reference you might want on a desert island: short expert
essays on every topic the course touched and hundreds it didn't. Within this
reader, the **Discrete Mathematics** (Lovász) and **Mathematics for Computer
Science** books remain the deeper texts every session here points back to. The
mathematics was never the obstacle; it was always a tool — and now it is one of
yours.
