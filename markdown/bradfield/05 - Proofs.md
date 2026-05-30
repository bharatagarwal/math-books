# Proofs

A *proof* is a method of establishing truth by a chain of logical deductions
from a set of axioms. As a software engineer you already write things that
must be correct — but "it passed the tests" is a fundamentally different
standard from "it is true for every input." Tests check finitely many cases;
a proof covers all of them at once. This chapter is about that second
standard, and about the handful of argument shapes that produce it.

This session's pre-work is MCS chapter 1, which has no Lovász counterpart, so
the whole development here follows MCS. We start where MCS starts — with the
sobering observation that a proposition can be true for an enormous number of
cases and still be false — and then work the post-class problems: the
implication "if $a^3 > a$ then $a^5 > a$," a proof by cases on the ordering of
two reals (MCS 1.8), the irrationality of $\sqrt{2}$ (MCS 1.3), and the Well
Ordering Principle from MCS chapter 2. Each gets pencil-and-paper reasoning
with a programmatic check or discovery alongside.

## Propositions, axioms, and deduction

MCS chapter 1 defines the vocabulary precisely. A **proposition** is a
statement that is either true or false. An **axiom** is a proposition we
assume true without proof — the agreed starting point. A **logical deduction**
(or inference rule) combines axioms and already-proved statements into new
ones; the workhorse is *modus ponens*: from $P$ and $P \implies Q$, conclude
$Q$. A proof, then, is a sequence of propositions, each an axiom or a
deduction from earlier ones, ending at the statement we wanted.

A **predicate** is a proposition whose truth depends on a variable, written
$P(n)$. "$n$ is a perfect square" is a predicate: $P(4)$ is true, $P(5)$ is
false. Most interesting theorems are universal claims about predicates —
$\forall n \in \mathbb{N}.\, P(n)$ — and that universality is exactly what
testing cannot reach.

## Why testing is not proof

MCS opens with a cautionary proposition: $\forall n \in \mathbb{N}.\;
n^2 + n + 41$ is prime. Evaluate $f(n) = n^2 + n + 41$ at $n = 0, 1, 2,
\ldots$ and every value comes out prime — for a long time. A test suite that
checked the first forty cases would report success and move on. Let us watch
the streak instead of trusting it.

```python
<!-- include: code/bradfield/05-proofs/05_primes_then_fails.py -->
```

The values are prime for the unbroken run $n = 0, \ldots, 39$, and then at
$n = 40$ the proposition collapses:
$$40^2 + 40 + 41 = 40(40 + 1) + 41 = 41 \cdot 41,$$
which is not prime. No amount of testing the first thirty-nine cases would
have revealed it — and the *reason* it fails ($f(40)$ has the algebraic form
$41 \cdot 41$) is exactly the kind of structure a proof exposes and a test
suite never sees.

MCS drives the point home with conjectures whose first counterexample is
astronomically far out. Euler conjectured in 1769 that $a^4 + b^4 + c^4 = d^4$
has no positive integer solutions; it stood for over two centuries until Noam
Elkies found a counterexample in 1988. And $313(x^3 + y^3) = z^3$ has a
solution too, but the smallest one has more than a thousand digits. The next
demo confirms the scale of the problem: brute force could run essentially
forever and still "find no counterexample," which is not at all the same as
"there is none."

```python
<!-- include: code/bradfield/05-proofs/06_conjectures_that_fail.py -->
```

This is the whole reason proof exists. "No counterexample found yet" is a
statement about how long you have looked, not about truth. The rest of the
chapter is the small toolkit that lets us settle a universal claim with
certainty, in finite space, regardless of how large the cases get.

## Proving an implication: if $a^3 > a$ then $a^5 > a$

Many theorems have the form $P \implies Q$. MCS lists two standard routes:
assume $P$ and deduce $Q$ directly, or prove the contrapositive
$\lnot Q \implies \lnot P$. The first post-class problem is a direct
implication: for real $a$, if $a^3 > a$ then $a^5 > a$.

Before reaching for a proof, it pays to *discover the shape of the
hypothesis*. The condition $a^3 > a$ is the same as $a^3 - a > 0$, and
$a^3 - a$ factors as $a(a-1)(a+1)$. A sign table built from those three roots
tells us exactly where the hypothesis lives.

```python
<!-- include: code/bradfield/05-proofs/07_sign_table.py -->
```

The table shows $a^3 > a$ holding precisely on $(-1, 0) \cup (1, \infty)$, and
that on every sample in that set $a^5 > a$ holds too. Now the proof writes
itself. Assume $a^3 > a$, i.e. $a^3 - a > 0$. Since $a^2 \ge 0$, multiplying
the (positive) quantity $a^3 - a$ by $a^2$ keeps it nonnegative:
$$a^2(a^3 - a) = a^5 - a^3 \ge 0, \quad\text{so}\quad a^5 \ge a^3 > a,$$
hence $a^5 > a$. (The product $a^2(a^3 - a)$ is in fact strictly positive
unless $a = 0$, and $a = 0$ does not satisfy the hypothesis, so the chain is
clean.) We can let sympy confirm the truth sets line up exactly, turning the
hand argument into an exhaustive symbolic check.

```python
<!-- include: code/bradfield/05-proofs/02_a_cubed_a_fifth.py -->
```

sympy reports both inequalities holding on the identical region
$(-1, 0) \cup (1, \infty)$, so the truth set of the hypothesis is contained in
that of the conclusion — which is exactly what $a^3 > a \implies a^5 > a$
asserts.

## Proving an "if and only if," and proof by cases

To prove $P \iff Q$, MCS says prove both implications, $P \implies Q$ and
$Q \implies P$. A close relative is **proof by cases**: split the argument
into possibilities that are jointly *exhaustive*, prove the claim in each, and
the claim holds overall. The validity hinges entirely on the cases covering
every possibility.

The second post-class problem (MCS 1.8) is a case analysis on the ordering of
two reals. Given $r$ and $s$, exactly one of $r < s$, $r = s$, $r > s$ holds
(trichotomy), and that three-way split is the canonical exhaustive case set.
A clean claim to prove this way: $\max(r, s) + \min(r, s) = r + s$ for all
reals. In each ordering case the max and min are determined, and the identity
falls out.

```python
<!-- include: code/bradfield/05-proofs/03_proof_by_cases.py -->
```

The demo realizes the three branches as a function and checks the identity
across every ordering over a grid of integer pairs — a finite stand-in for the
case-by-case hand proof. Case $r < s$: $\max + \min = s + r$. Case $r > s$:
$r + s$. Case $r = s$: $r + r = r + s$. The cases are exhaustive by
trichotomy, so the identity holds for all reals.

## Proof by contradiction: $\sqrt{2}$ is irrational

The marquee proof of MCS chapter 1 — and the third post-class problem (MCS
1.3) — is the irrationality of $\sqrt{2}$, argued by **contradiction**. The
structure (from MCS chapter 1's proof methods) is: to prove $P$, assume
$\lnot P$, derive a logically valid but false statement, and conclude $P$.

Suppose, for contradiction, that $\sqrt{2}$ is rational. Then we can write
$\sqrt{2} = a/b$ with integers $a, b$ in lowest terms (no common factor).
Squaring gives $2 = a^2 / b^2$, so $a^2 = 2b^2$. Thus $a^2$ is even, which
forces $a$ even — because the square of an odd number is odd. Write $a = 2c$;
then $4c^2 = 2b^2$, so $b^2 = 2c^2$, making $b^2$ even and hence $b$ even. But
now $a$ and $b$ share the factor $2$, contradicting "lowest terms." The
assumption was impossible, so $\sqrt{2}$ is irrational.

The proof leans on one crucial lemma — $n^2$ is even iff $n$ is even — and on
the claim that no coprime pair satisfies $a^2 = 2b^2$. We check both: the
lemma exhaustively mod $2$, and the coprimality claim by searching small $b$.

```python
<!-- include: code/bradfield/05-proofs/01_sqrt2_irrational.py -->
```

Every integer solution the search turns up has $\gcd(a, b) > 1$ — never
coprime, never in lowest terms — which is precisely the contradiction the
proof predicts, restated as data.

## The Well Ordering Principle

MCS chapter 2 introduces a deceptively simple axiom with surprising reach:

> **Well Ordering Principle (WOP).** Every nonempty set of nonnegative
> integers has a smallest element.

It underlies a proof technique close to induction. The MCS template: to show
$P(n)$ holds for all $n \in \mathbb{N}$, let $C = \{n \mid \lnot P(n)\}$ be the
set of counterexamples; assume $C$ is nonempty; by WOP it has a least element
$n_0$; then derive a contradiction (typically by producing a *smaller*
counterexample, which $n_0$'s minimality forbids); conclude $C$ is empty.

WOP gives a second, very different proof that $\sqrt{2}$ is irrational, and
this one is worth seeing *mechanically*. Suppose $\sqrt{2} = a/b$; then the
set of positive integers $m$ with $m\sqrt{2}$ an integer is nonempty (it
contains $b$). By WOP it has a least element $m$. Consider
$$m' = m\sqrt{2} - m = m(\sqrt{2} - 1).$$
Since $0 < \sqrt{2} - 1 < 1$, we get $0 < m' < m$; and $m'\sqrt{2} = 2m -
m\sqrt{2}$ is an integer while $m'$ itself is an integer — so $m'$ is a
*smaller* positive integer with the same property, contradicting minimality.
The engine of the proof is that multiplying by $\sqrt{2} - 1$ strictly
shrinks while staying positive. Let us watch that descent run.

```python
<!-- include: code/bradfield/05-proofs/08_wop_descent.py -->
```

The sequence strictly decreases yet never reaches zero — an infinite descent
in the positive integers, which WOP says is impossible. So no least $m$ can
exist, so $\sqrt{2}$ is not a ratio of integers. The same descent structure
proves the MCS chapter 2 staple that every integer $n > 1$ has a prime
factorization: if not, the set of non-factorable integers has a least element
$n$, which cannot be prime, so $n = ab$ with $1 < a, b < n$; but $a$ and $b$
are smaller, hence factorable, hence so is $n$ — contradiction.

```python
<!-- include: code/bradfield/05-proofs/04_well_ordering.py -->
```

The demo realizes the descent directly: it peels off the least factor greater
than $1$ and recurses on the smaller quotient, exactly the move WOP licenses,
then confirms the result is genuinely a product of primes for every $n$ in the
range.

## What makes a proof good

MCS chapter 1's notes on proof method are worth internalizing, because a
correct proof can still be a bad one. State your game plan ("we argue by
contradiction"). Keep a linear flow where each step follows from the last.
Write an essay, not a wall of symbols — words are often clearer. Be wary of
"clearly" and "obviously," which tend to hide the gaps. And finish: tie the
final line back to the claim. The matching list of common mistakes is just as
useful — proving an implication by assuming its conclusion (circular),
arguing from a few examples (the very trap of the opening section), and
confusing $P \implies Q$ with its converse $Q \implies P$.

## Working the problem set

The session's post-class problems are exactly the worked examples above, so
the "problem set" here is to make sure each hand proof and its check agree:

**Problem (MCS 1.3).** $\sqrt{2}$ is irrational — proved twice, once by
contradiction (`01_sqrt2_irrational.py` checks the even-square lemma and the
no-coprime-solution claim) and once by Well Ordering descent
(`08_wop_descent.py` watches $m(\sqrt{2}-1)$ shrink).

**Problem (if $a^3 > a$ then $a^5 > a$).** Multiply the hypothesis by
$a^2 \ge 0$; `02_a_cubed_a_fifth.py` confirms the two truth sets coincide and
`07_sign_table.py` discovers that set from the factorization $a(a-1)(a+1)$.

**Problem (MCS 1.8).** Case analysis on $r < s$, $r = s$, $r > s$;
`03_proof_by_cases.py` verifies $\max + \min = r + s$ in every ordering.

The discovery demos (`05`, `06`, `07`, `08`) are the ones to revisit when a
new conjecture tempts you to "just test it" — they are calibration for how
badly that instinct can mislead.

## Where to go deeper

- **MCS ch. 1 (Intro to Proofs)** — propositions, axioms, deduction, proving
  implications and iffs, proof by cases, and the $\sqrt{2}$ proof in full.
  The cautionary conjectures (Euler's $a^4+b^4+c^4=d^4$, the prime
  polynomial, the thousand-digit cubic) all live here.
- **MCS ch. 1, Proof Methods** — the anatomy of proof by contradiction, the
  guidelines for a *good* proof, and the catalog of common mistakes.
- **MCS ch. 2 (Well Ordering Principle)** — WOP, the counterexample-set
  template, and the prime-factorization and $\sqrt{2}$ examples.
- Proof by contradiction and Well Ordering reappear constantly: WOP is the
  scaffolding under strong induction, and contradiction is the standard route
  for impossibility results throughout the rest of the curriculum.
