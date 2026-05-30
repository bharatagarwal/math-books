# Lecture 4: Number Theory and the GCD

Number theory — the study of the integers — is one of the oldest mathematical disciplines. For most of its history, it was pure and impractical: beautiful patterns in the integers, studied for their own sake. Only about 40 years ago did anyone realize these patterns had staggering practical applications, mainly in cryptography — the art of hiding information.

Your medical records stored in the cloud, your bank transactions, your private messages: all protected by the same number theory we're about to study. We'll get to cryptography next lecture. Today, number theory is going to help us save New York City.

## Die Hard 3

In *Die Hard with a Vengeance*, Bruce Willis and Samuel L. Jackson find themselves in a city park, staring at a bomb. The villain phones in the rules: there's a 5-gallon jug and a 3-gallon jug on the fountain. Fill one with *exactly* 4 gallons and place it on the scale, or the bomb detonates. One ounce more or less — detonation. You have five minutes.

They fumble. "Obviously we can't fill the 3-gallon jug with 4 gallons." "Obviously." They try filling it partway — but the villain said *exactly*. No eyeballing.

Now imagine what's under this table is a bomb. Each tennis ball is one gallon. We have the 5-gallon jug and the 3-gallon jug. You have to save 6042. Who has an idea?

Fill the 3-gallon jug. Pour it into the 5-gallon jug. Now we have 0 in the small, 3 in the big.

Fill the 3-gallon jug again and pour. Only 2 more gallons fit in the big jug, leaving 1 gallon in the small jug.

Empty the big jug. Pour that 1 gallon over. Fill the small jug once more and pour it in.

We have exactly 4 gallons. 6042 is saved. Thank God. So we can continue.

This is pretty amazing. How do you get exactly 4 gallons from a 3-gallon jug and a 5-gallon jug? And if you change the problem slightly, things fall apart. Replace the 5-gallon jug with a 6-gallon jug — can you still get 4?

No. Everything has to be a multiple of 3. The small jug is $1 \times 3$, the big jug is $2 \times 3$. Filling, emptying, and pouring only ever produce multiples of 3 in each jug. And 4 is not a multiple of 3.

That argument feels right, but it's informal. To make it rigorous, we need to model the problem precisely and prove the property holds.

## Divisibility

We say $m$ **divides** $a$, written $m \mid a$, if there exists an integer $k$ such that $a = km$.

So $3 \mid 6$ because $6 = 2 \cdot 3$. And $5 \mid 0$ because $0 = 0 \cdot 5$. In fact, every integer divides 0 — just take $k = 0$. This seemingly trivial fact is exactly what makes the base case of our invariant proof work.

A key property we'll use repeatedly: if $m \mid a$ and $m \mid b$, then $m$ divides any linear combination of $a$ and $b$. That is, $m \mid (sa + tb)$ for any integers $s, t$. (Why? If $a = k_1 m$ and $b = k_2 m$, then $sa + tb = (sk_1 + tk_2)m$.)

## Modeling the Jug Problem

To analyze the jug problem precisely, we model it as a state machine — the same tool we used for the 8-puzzle in Lecture 3. Suppose we have an $a$-gallon jug and a $b$-gallon jug, with $a \leq b$.

**States:** Pairs $(x, y)$ where $x$ is the gallons in the $a$-jug and $y$ is the gallons in the $b$-jug.

**Start state:** $(0, 0)$.

**Transitions** — from any state $(x, y)$:

| Action | Result | Condition |
|--------|--------|-----------|
| Empty $a$-jug | $(0, y)$ | |
| Empty $b$-jug | $(x, 0)$ | |
| Fill $a$-jug | $(a, y)$ | |
| Fill $b$-jug | $(x, b)$ | |
| Pour $a$ into $b$ (fits) | $(0,\; x + y)$ | $x + y \leq b$ |
| Pour $a$ into $b$ (overflow) | $(x + y - b,\; b)$ | $x + y > b$ |
| Pour $b$ into $a$ (fits) | $(x + y,\; 0)$ | $x + y \leq a$ |
| Pour $b$ into $a$ (overflow) | $(a,\; x + y - a)$ | $x + y > a$ |

The pour rules are the interesting ones. If there's room in the target jug, pour everything over. If there isn't, fill the target to capacity and keep the remainder. This is what happened when we poured the 5-gallon jug into the 3-gallon jug and had 2 gallons left over.

For $a = 3$, $b = 5$, here's the trace that produces 4 gallons:

$$(0,0) \xrightarrow{\text{fill }b} (0,5) \xrightarrow{b \to a} (3,2) \xrightarrow{\text{empty }a} (0,2) \xrightarrow{b \to a} (2,0) \xrightarrow{\text{fill }b} (2,5) \xrightarrow{b \to a} (3,4)$$

Six moves. Each arrow is a legal transition from our table. The state machine fully captures everything you can do with two jugs and a fountain.

We can find this path automatically — a breadth-first search through the state machine:

```python
# uv run python
from collections import deque

def solve_jugs(a, b, target):
    """BFS through the jug state machine. Returns the shortest path."""
    start = (0, 0)
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        (x, y), path = queue.popleft()
        if x == target or y == target:
            return path

        moves = [
            (0, y), (x, 0),
            (a, y), (x, b),
            (max(0, x+y-b), min(x+y, b)),
            (min(x+y, a), max(0, x+y-a)),
        ]
        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

path = solve_jugs(3, 5, 4)
print("Die Hard 3 — jugs (3, 5), target 4:")
for i, (x, y) in enumerate(path):
    print(f"  Step {i}: ({x}, {y})")
print(f"Solution in {len(path) - 1} moves.\n")

result = solve_jugs(3, 6, 4)
print(f"Jugs (3, 6), target 4: {'impossible' if result is None else 'found'}")
```

The BFS explores every reachable state. For (3, 5) it finds a 6-move solution. For (3, 6) it exhausts the entire reachable space and reports: impossible. But *why* is it impossible? The BFS searched everywhere and failed — it can't tell us why no path exists. For that, we need an invariant.

## The Divisibility Invariant

**Theorem.** If $m \mid a$ and $m \mid b$, then $m \mid x$ and $m \mid y$ for every state $(x, y)$ reachable from $(0, 0)$.

In words: if $m$ is a common divisor of the jug capacities, then $m$ divides the contents of both jugs at every step, no matter what moves you make. The "multiples of 3" intuition from the (3, 6) case is a special instance with $m = 3$.

**Proof.** By induction on $n$, the number of transitions.

Let $P(n)$: "If $(x, y)$ is the state after $n$ transitions, then $m \mid x$ and $m \mid y$."

**Base case.** $P(0)$: the state is $(0, 0)$. Since $m \mid 0$ for any integer $m$, the property holds. $\checkmark$

**Inductive step.** Assume $P(n)$: we're in state $(x, y)$ with $m \mid x$ and $m \mid y$. We also have $m \mid a$ and $m \mid b$ by assumption.

After one more transition, each jug contains one of:

$$0, \quad a, \quad b, \quad x, \quad y, \quad x + y, \quad x + y - a, \quad x + y - b$$

We know $m$ divides $0$, $a$, $b$, $x$, and $y$. And any linear combination of values divisible by $m$ is also divisible by $m$. So $m$ divides every value in this list: $x + y$ is a linear combination of $x$ and $y$; $x + y - a$ is a linear combination of $x$, $y$, and $a$; and so on.

Therefore $m$ divides the contents of both jugs after the $(n+1)$-th transition. $P(n+1)$ holds. $\square$

## Die Hard 5

Die Hard 4 came out fine. But the rumors about Die Hard 5 were troubling. The props department had ordered a 33-gallon jug and a 55-gallon jug. Bruce was in training — you can imagine pouring 55 gallons of water. But was he training the right muscles?

The villain demands exactly 4 gallons. Can it be done?

Both 33 and 55 are divisible by 11. By our theorem with $m = 11$: every reachable state $(x, y)$ has $11 \mid x$ and $11 \mid y$. Since $11 \nmid 4$, exactly 4 gallons is unreachable.

The entire cast gets blown up. No Die Hard 6.

**Z3** can verify this mechanically. Our theorem tells us any reachable amount must be a linear combination of the jug sizes. So the question "can I reach 4 gallons?" reduces to "do integers $s, t$ exist such that $sa + tb = 4$?"

```python
# uv run --with z3-solver python
from z3 import *

s, t = Ints('s t')

# Die Hard 3: 3-gallon and 5-gallon jugs
solver = Solver()
solver.add(s * 3 + t * 5 == 4)
print("Die Hard 3 — can 3s + 5t = 4?", solver.check())
m = solver.model()
print(f"  Solution: {m[s]}×3 + {m[t]}×5 = 4")

# Die Hard 5: 33-gallon and 55-gallon jugs
solver2 = Solver()
solver2.add(s * 33 + t * 55 == 4)
print(f"\nDie Hard 5 — can 33s + 55t = 4? {solver2.check()}")
print("  No integers exist: 33s + 55t = 11(3s + 5t), always a multiple of 11.")
```

Z3 returns `sat` for (3, 5) and finds the coefficients. For (33, 55) it returns `unsat` — a mechanical proof that no integer solution exists. This isn't just a search failure; it's an exhaustive proof over all integers. The underlying reason: $33s + 55t = 11(3s + 5t)$, which is always a multiple of 11.

## The Greatest Common Divisor

The number 11 in the Die Hard 5 problem isn't just *a* common divisor of 33 and 55 — it's the *greatest* common divisor.

The **greatest common divisor** of $a$ and $b$, written $\gcd(a, b)$, is the largest integer that divides both.

$$\gcd(3, 5) = 1 \qquad \gcd(52, 44) = 4 \qquad \gcd(33, 55) = 11$$

For $\gcd(52, 44)$: since $52 = 4 \times 13$ and $44 = 4 \times 11$, the largest common factor is 4.

When $\gcd(a, b) = 1$, we say $a$ and $b$ are **relatively prime**. The numbers 3 and 5 are relatively prime — they share no common factor besides 1. This is the case that makes the Die Hard puzzle solvable: since the GCD is 1, it divides every positive integer, so *any* target amount is achievable.

**Corollary.** $\gcd(a, b)$ divides every reachable result.

*Proof.* The GCD divides both $a$ and $b$. By the invariant theorem, it divides the contents of both jugs in every reachable state. $\square$

This tells us what we *can't* reach — anything that isn't a multiple of the GCD is off limits. But what *can* we reach?

## Any Linear Combination Can Be Reached

**Theorem.** Any linear combination $L = sa + tb$ with $0 \leq L \leq b$ can be reached.

The proof is constructive — it gives an algorithm. The key trick: if $s$ is negative, rewrite the linear combination. You can add $nb \cdot a$ and subtract $na \cdot b$ without changing the value, but making the coefficient of $a$ positive. Call the positive version $s'$.

Then the algorithm is simple:

1. Repeat $s'$ times: fill the $a$-jug, pour it into the $b$-jug
2. Whenever the $b$-jug fills up, empty it and continue pouring
3. What remains in the $b$-jug is exactly $L$ gallons

For our example, $4 = (-2) \times 3 + 2 \times 5$. That has $s = -2$, which is negative. Rewrite: add $1 \times 5 \times 3 = 15$ and subtract $1 \times 3 \times 5 = 15$. We get $4 = 3 \times 3 + (-1) \times 5$, so $s' = 3$.

Now repeat the fill-and-pour cycle 3 times:

| Loop | Start | Fill $a$ | Pour → $b$ | Empty $b$? | Continue | End |
|------|-------|----------|-----------|------------|----------|-----|
| 1 | (0, 0) | (3, 0) | — | — | (0, 3) | (0, 3) |
| 2 | (0, 3) | (3, 3) | (1, 5) | (1, 0) | (0, 1) | (0, 1) |
| 3 | (0, 1) | (3, 1) | — | — | (0, 4) | **(0, 4)** |

After 3 fills, the big jug holds exactly 4 gallons. The accounting: we poured in $3 \times 3 = 9$ gallons total, emptied the big jug once ($5$ gallons out). Remainder: $9 - 5 = 4 = L$. $\checkmark$

**Why it always works:** After $s'$ fills and $u$ empties, the remainder in the $b$-jug is $r = s'a - ub$. Since $L = s'a + t'b$, we get $r - L = -(t' + u)b$. Both $r$ and $L$ lie in $[0, b)$, so their difference has absolute value less than $b$. The only multiple of $b$ with absolute value less than $b$ is 0. Therefore $t' + u = 0$ and $r = L$. $\square$

## Euclid's Algorithm

How do you compute $\gcd(a, b)$? You could factor both numbers — but factoring large integers is hard. That difficulty is the entire basis of modern cryptography. Euclid found a dramatically better way, 2,300 years ago.

**Lemma.** $\gcd(a, b) = \gcd\bigl(\operatorname{rem}(b, a),\; a\bigr)$

where $\operatorname{rem}(b, a)$ is the remainder when dividing $b$ by $a$.

The idea: replace the pair $(a, b)$ with $(\operatorname{rem}(b, a),\; a)$. The GCD doesn't change. Repeat until one value hits 0 — the other is the GCD. The textbook calls this **The Pulverizer**: it grinds the numbers down to their greatest common divisor.

**Example.** $\gcd(105, 224)$:

$$\gcd(105, 224) = \gcd(14, 105) \quad \text{because } 224 = 2 \times 105 + 14$$
$$= \gcd(7, 14) \quad \text{because } 105 = 7 \times 14 + 7$$
$$= \gcd(0, 7) \quad \text{because } 14 = 2 \times 7 + 0$$
$$= 7$$

Three steps. At each step, the remainder is strictly smaller. When it hits 0, we're done.

**Proof of the Lemma.** We show the common divisors of $(a, b)$ and $(\operatorname{rem}(b, a), a)$ are exactly the same set.

Forward: if $m \mid a$ and $m \mid b$, then since $\operatorname{rem}(b, a) = b - qa$ for quotient $q$, we have $m \mid (b - qa)$. So $m$ divides both $\operatorname{rem}(b, a)$ and $a$.

Backward: if $m \mid \operatorname{rem}(b, a)$ and $m \mid a$, then since $b = qa + \operatorname{rem}(b, a)$, we have $m \mid b$. So $m$ divides both $a$ and $b$.

Same set of common divisors means same *greatest* common divisor. $\square$

**Dafny** can verify the algorithm mechanically. The recursive structure maps cleanly — each call strictly reduces the arguments, and the `decreases` clause proves the recursion terminates:

```dafny
// dafny verify euclid.dfy
function Gcd(a: nat, b: nat): nat
  requires a > 0 || b > 0
  ensures Gcd(a, b) > 0
  decreases a + b
{
  if a == 0 then b
  else if b == 0 then a
  else if a <= b then Gcd(a, b % a)
  else Gcd(b, a % b)
}
```

`decreases a + b` tells Dafny: prove that $a + b$ gets smaller on every recursive call. When we call `Gcd(a, b % a)` with $a \leq b$, the new sum is $a + (b \bmod a)$. Since $b \bmod a < a \leq b$, the new sum is strictly less than $a + b$. Dafny checks this mechanically — no hand-waving about termination.

The `ensures Gcd(a, b) > 0` postcondition guarantees the result is always positive. In the base cases, we return the nonzero argument (guaranteed by the precondition `a > 0 || b > 0`). In the recursive cases, the postcondition follows inductively. Dafny verifies the whole chain.

## Bézout's Identity

Euclid's algorithm does more than compute the GCD. If you track the algebra at each step, you can express the GCD as a **linear combination** of the original inputs.

From our example:

$$7 = 105 - 7 \times 14$$

But $14 = 224 - 2 \times 105$, so substituting:

$$7 = 105 - 7(224 - 2 \times 105) = 15 \times 105 + (-7) \times 224$$

Check: $15 \times 105 = 1575$ and $7 \times 224 = 1568$. Indeed $1575 - 1568 = 7$. $\checkmark$

This is **Bézout's identity**: for any positive integers $a, b$, there exist integers $s, t$ such that

$$sa + tb = \gcd(a, b)$$

The extended Euclidean algorithm computes these coefficients alongside the GCD — it recurses the same way Euclid's algorithm does, but carries the linear combination coefficients along for the ride. **Hypothesis** can test this identity for hundreds of random pairs:

```python
# uv run --with hypothesis python
from math import gcd
from hypothesis import given, settings, strategies as st

def extended_gcd(a, b):
    """Return (g, s, t) such that s*a + t*b = g = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, s1, t1 = extended_gcd(b, a % b)
    return g, t1, s1 - (a // b) * t1

@given(st.integers(min_value=1, max_value=10000),
       st.integers(min_value=1, max_value=10000))
@settings(max_examples=1000)
def test_bezout(a, b):
    g, s, t = extended_gcd(a, b)
    assert g == gcd(a, b), f"GCD wrong: got {g}, expected {gcd(a, b)}"
    assert s * a + t * b == g, f"Bézout failed: {s}*{a} + {t}*{b} != {g}"
    assert a % g == 0 and b % g == 0, f"GCD {g} doesn't divide inputs"

test_bezout()
print("Bézout's identity verified for 1000 random pairs.")

g, s, t = extended_gcd(105, 224)
print(f"\ngcd(105, 224) = {g}")
print(f"  {s}×105 + {t}×224 = {s * 105 + t * 224}")
```

Hypothesis tests three properties across 1000 random pairs: the GCD matches Python's `math.gcd`, Bézout's equation $sa + tb = g$ actually holds, and $g$ divides both inputs. No failures — the identity works every time.

## The Smallest Positive Linear Combination

Now we combine everything. We've proved three things:

1. **Invariant:** $\gcd(a, b)$ divides every reachable result
2. **Reachability:** Any linear combination $0 \leq sa + tb \leq b$ can be reached
3. **Bézout:** $\gcd(a, b)$ is itself a linear combination of $a$ and $b$

These three fit together like puzzle pieces:

**Theorem.** $\gcd(a, b)$ is the smallest positive linear combination of $a$ and $b$.

*Proof.* The GCD is a linear combination (Bézout). Any linear combination that fits in the jug can be reached (Reachability). The GCD divides all reachable values (Invariant), so every other positive reachable value is a multiple of $\gcd(a, b)$ — and therefore at least as large.

So $\gcd(a, b)$ is the smallest positive value reachable, which is the smallest positive linear combination. $\square$

This is a remarkable result. The GCD is defined as the *greatest* common divisor — a property about what divides *into* $a$ and $b$. Yet it equals the *smallest* positive linear combination — a property about what $a$ and $b$ can *build together*. Two completely different perspectives, one number. The bridge between them is Euclid's algorithm.

## Summary

| Concept | Definition |
|---------|-----------|
| $m \mid a$ | $\exists k.\; a = km$ |
| $\gcd(a, b)$ | Largest integer dividing both $a$ and $b$ |
| Relatively prime | $\gcd(a, b) = 1$ |
| Bézout's identity | $\exists s, t.\; sa + tb = \gcd(a, b)$ |

| Theorem | What It Says |
|---------|-------------|
| **Divisibility invariant** | If $m \mid a$ and $m \mid b$, then $m$ divides every reachable jug state |
| **Reachability** | Any linear combination $0 \leq sa + tb \leq b$ is reachable |
| **Bézout** | $\gcd(a, b)$ is a linear combination of $a$ and $b$ |
| **GCD characterization** | $\gcd(a, b)$ is the smallest positive linear combination |

| Tool | What It Did | Why It Earned Its Keep |
|------|------------|----------------------|
| **Python BFS** | Found the jug-pouring solution path | Models the state machine directly; shows *what* is reachable |
| **Z3** | Proved (33, 55) → 4 gallons is impossible | Mechanical proof via integer constraints; `unsat` over all integers |
| **Dafny** | Verified Euclid's algorithm terminates and returns positive | `decreases a + b` proves termination; `ensures > 0` proves correctness |
| **Hypothesis** | Tested Bézout's identity across 1000 random pairs | Builds confidence in a surprising identity before the formal proof |

## Further Reading

- [Bézout's Identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity) — The theorem that $\gcd(a, b)$ is the smallest positive linear combination
- [Extended Euclidean Algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) — Computing the Bézout coefficients alongside the GCD
- [RSA Cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) — Where this number theory meets cryptography (coming in a later lecture)
- [Dafny Termination Proofs](https://dafny.org/dafny/DafnyRef/DafnyRef#sec-decreases-clause) — Verifying that recursive algorithms terminate
- [MCS Chapter 9: Number Theory](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) — The textbook treatment of GCD, Bézout, and The Pulverizer
