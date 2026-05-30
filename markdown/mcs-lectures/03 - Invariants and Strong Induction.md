# Lecture 3: Invariants and Strong Induction

Lectures 1 and 2 gave us three proof techniques: direct proof, proof by contradiction, and ordinary induction. Today we add two more — invariants and strong induction — and together they'll handle a wide class of problems in discrete math and computer science.

But first: what separates a proof that works from a proof that's *good*?

## Seven Virtues of a Good Proof

A good proof has seven characteristics. It should be **correct** (obviously), **complete** (all key steps present), **clear** (the reader can follow the reasoning), and **brief** — you don't want to crush somebody with unnecessary detail. Ideally it's **elegant**: crisp, clever, short, to the point. Elegance is the mathematician's notion of beauty, the highest compliment one mathematician can pay another, and like all aesthetic judgments, there's real debate about what qualifies. It should be **well-organized**, using lemmas the way you'd use subroutines in code. And it should be **in order** — start from what you know and work toward what you're proving, never the reverse.

The "in order" point trips people up. A common high school technique is to start with what you're trying to prove — say, $a = b$ — do some algebra, and arrive at $1 = 1$. Check mark, we're done! But this is backwards. You're starting from the conclusion and deriving a known truth. That's logically valid only if every step is reversible (an "if and only if"), and most people don't check. Better to start from $1 = 1$ and work forward to $a = b$. Top down. In order.

Good proofs are very much like good code. And we care about teaching you to write good proofs because someday you'll need to prove that your programs do what they're supposed to do. The consequences of getting it wrong are not abstract.

The Airbus A300 was one of the first commercial jets fully operated by software — takeoff, flight, and landing, all automated. On one early flight, a bug caused the rear door to open just before landing. The plane crashed. First commercial crash in history caused by a software defect.

The Therac-25 was a radiation therapy machine for cancer patients. A race condition occasionally caused the device to slam patients with massive overdoses. It killed people.

In the 2000 US election, a software bug in electronic voting machines gave Al Gore *negative* 16,000 votes in one Florida county. He had enough problems with hanging chads; losing 16,000 votes to a bug certainly didn't help.

A single faulty command in the computer systems used by United and American Airlines grounded the entire fleets of both airlines for close to a day.

One-third of all published mathematical proofs are estimated to contain bugs — flaws that render the proof incorrect. If the world's best mathematicians routinely make mistakes, what hope do the rest of us have?

This is going to sound scary, but someday — maybe 20 or 30 years from now — it's possible that your life will depend on software that someone in this course writes. Look at the person sitting next to you. Imagine that in 25 years, your life depends on whether their code does what it's supposed to do.

That's why we're motivated to help you make rock-solid arguments.

## The Top 10 Proof Techniques You Should Never Use

Rigor is hard. Even famous mathematicians get lazy. Gauss wrote his PhD thesis in 1799 — usually cited as the first rigorous proof of the Fundamental Theorem of Algebra. But his thesis contains this passage:

> "If a branch of an algebraic curve enters a bounded region, it must necessarily leave again. Nobody, to my knowledge, has ever doubted this fact. But if anybody desires it, then on another occasion, I intend to give a demonstration which will leave no doubt."

Warning buzzers should be going off in your brain. Gauss is using an unproven claim and deferring the proof to "another occasion." As the Fields medalist Stephen Smale later wrote, this was "an immense gap in the proof" — a gap not filled until 1920, more than a century later. Gauss never could give the proof.

Remember the Poincaré Conjecture from Lecture 1? In 1900, Poincaré called it a simple fact. Four years later, he demoted his claim to the status of a conjecture. That conjecture took another century to solve.

So to really bring home the point, here's a top 10 list of proof techniques you should never use:

**10. Proof by throwing in the kitchen sink.** Write down every theorem known to mankind and add a few more for good measure. When questioned: "Look, the proof contains all the key facts. They're all here."

**9. Proof by example.** Give the case $n = 2$ and suggest it contains most of the ideas of the general proof.

**8. Proof by vigorous hand-waving.** Wave your hands emphatically. It must be true.

**7. Proof by cumbersome notation.** The reader gets hopelessly confused, gives up, and says OK. (There was once a grad student known as "the encryptor" — he could take the simplest proof and so encrypt it in notation that you could never figure out if it was right or wrong.)

**6. Proof by exhaustion.** The reader, not the cases.

**5. Proof by omission.** "The reader may easily supply the details. The other cases are analogous. Trivial." Experts use this all the time. Every once in a while, it turns out not to be so trivial.

**4. Proof by picture.** We saw one of those go wrong in Lecture 2 — the "proof" that $90 > 92$.

**3. Proof by vehement assertion.** The more forceful the argument, the higher the voice, the more intimidating the delivery. Doesn't make it more true.

**2. Proof by appeal to intuition.** "Any moron knows that." Well, now you're reluctant to question it.

**1. Proof by reference to eminent authority.** "I saw Fermat on the elevator and he said he had a proof."

That last one deserves elaboration. Fermat's Last Theorem — the claim that $x^n + y^n = z^n$ has no positive integer solutions for $n > 2$ — is perhaps the most famous assertion in mathematics. In 1637, Fermat wrote in the margin of a book that he had discovered a proof, but the margin was too small to contain it. He never supplied the details. It took 350 years and hundreds of pages for Andrew Wiles, who essentially locked himself in a room for a decade, to finally prove it. Fermat was right about one thing: the proof would not fit in a margin.

## The Eight Puzzle

Here's a puzzle that was enormously popular in the 1880s. You have a $3 \times 3$ grid with tiles labeled $a$ through $h$ and one blank space. Tiles slide into the adjacent blank — up, down, left, or right. No diagonal moves, no lifting tiles.

Starting position:

$$\begin{array}{|c|c|c|}
\hline
a & b & c \\
\hline
d & e & f \\
\hline
\_ & h & g \\
\hline
\end{array}$$

Target position (alphabetical order):

$$\begin{array}{|c|c|c|}
\hline
a & b & c \\
\hline
d & e & f \\
\hline
g & h & \_ \\
\hline
\end{array}$$

Everything is in order except $g$ and $h$ are swapped. It doesn't look hard. Just shuffle a few tiles around. Give it three minutes.

You won't solve it. It's impossible. But it *feels* solvable — you keep getting close, then everything scrambles again. Let's prove it can't be done.

**Theorem.** There is no sequence of legal moves that transforms the starting position into the target position.

## Invariants: Proving the Impossible

To prove a system can never reach a particular state, we find an **invariant** — a property with three characteristics:

1. It holds in the initial state
2. Every legal move preserves it
3. It does *not* hold in the target state

If the property holds at the start and is preserved by every transition, then every reachable state has the property. If the target lacks it, the target is unreachable.

The trick is always the same: finding the right property.

## Hunting for the Invariant

To figure out the invariant, we need to look at what happens during a move. There are two kinds: row moves and column moves.

Number the cells 1 through 9 in reading order:

$$\begin{array}{|c|c|c|}
\hline
1 & 2 & 3 \\
\hline
4 & 5 & 6 \\
\hline
7 & 8 & 9 \\
\hline
\end{array}$$

**Lemma 1.** A row move does not change the relative order of any pair of items.

Proof — well, it's obvious.

No. You can't let me get away with that — I'm not going to let you get away with it on homework either. Let's be careful. In a row move, a tile slides from cell $i$ to cell $i - 1$ or $i + 1$. Nothing else moves. Everything else occupies cells $\leq i-2$ or $\geq i+2$. So no relative orderings change. $\square$

That needed only a sentence more than "it's obvious," but "it's obvious" is the start of a slippery slope. If we only had row moves, the puzzle would be trivial — nothing ever changes. Column moves are where things get interesting.

**Lemma 2.** A column move changes the relative order of exactly two pairs of items.

**Proof.** A column move slides a tile from cell $i$ to cell $i - 3$ or $i + 3$. The tile jumps over exactly two other cells. Its relative order with those two items reverses; its order with everything else stays the same. $\square$

Let's see this with examples. If $g$ moves up from cell 8 to cell 5, it passes over cells 6 and 7. Before: $g$ was after the items in those cells. After: $g$ is before them. Two pairs changed.

Now watch: when we say "don't do proof by example," we don't mean don't *try* examples. By trying examples, you find out what you're trying to prove. The examples are how we discovered that column moves flip exactly two pairs — the lemma came from playing with specific cases.

## Inversions and Parity

An **inversion** is a pair of letters $(L_1, L_2)$ where $L_1$ precedes $L_2$ in the alphabet but appears *after* $L_2$ in the puzzle.

In the starting position $a, b, c, d, e, f, h, g$: only the pair $(g, h)$ is inverted. One inversion — **odd**.

In the target position $a, b, c, d, e, f, g, h$: everything is in order. Zero inversions — **even**.

So if moves can only change the inversion count by an even number, we're done.

**Lemma 3.** During any move, the number of inversions increases by 2, decreases by 2, or stays the same.

**Proof.** By cases.

*Row move:* No pairs change order (Lemma 1). Inversion count unchanged.

*Column move:* Exactly two pairs change order (Lemma 2). Three sub-cases:

- *Both pairs were in order.* They become inverted. Inversions increase by 2.
- *Both pairs were inverted.* They become ordered. Inversions decrease by 2.
- *One of each.* One new inversion, one removed. Net change: 0. $\square$

**Corollary.** The parity of the number of inversions does not change during any move.

*Proof.* Adding or subtracting 2 doesn't change whether a number is even or odd. $\square$

We can verify this computationally — apply 100,000 random moves and check that parity never flips:

```python
# uv run python
import random

def inversions(tiles):
    """Count inversions: pairs where alphabetically earlier letter appears later in puzzle."""
    count = 0
    letters = [t for t in tiles if t != '_']
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters[i] > letters[j]:
                count += 1
    return count

def neighbors(pos, size=3):
    """Cells adjacent to position pos in a size×size grid."""
    r, c = pos // size, pos % size
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < size and 0 <= nc < size:
            yield nr * size + nc

def random_move(tiles):
    blank = tiles.index('_')
    targets = list(neighbors(blank))
    swap = random.choice(targets)
    tiles[blank], tiles[swap] = tiles[swap], tiles[blank]

start = list('abcdef_hg')
parity = inversions(start) % 2  # 1 (odd)

for _ in range(100_000):
    random_move(start)
    assert inversions(start) % 2 == parity, "Parity changed!"

print(f"After 100,000 random moves: parity={'odd' if parity else 'even'}")
print("Parity never changed.")
```

Random testing builds confidence, but it can't check every possible move sequence. **Z3** can go further. Instead of simulating moves, we ask a direct question: "Does there exist a sorted permutation of the tiles with an odd number of inversions?" If the answer is `unsat`, no such arrangement exists.

```python
# uv run --with z3-solver python
from z3 import *

# Tiles as integers: a=0, b=1, ..., h=7
tiles = [Int(f't{i}') for i in range(8)]
s = Solver()

# tiles must be a valid permutation of 0..7
s.add(Distinct(tiles))
for t in tiles:
    s.add(And(t >= 0, t < 8))

# Target state: sorted order
for i in range(8):
    s.add(tiles[i] == i)

# Invariant from start state: odd number of inversions
inv_pairs = [If(tiles[i] > tiles[j], 1, 0)
             for i in range(8) for j in range(i + 1, 8)]
s.add(Sum(inv_pairs) % 2 == 1)

print(s.check())  # unsat
```

Z3 returns `unsat`: no sorted permutation has an odd number of inversions. The lemmas prove every reachable state has odd parity. Z3 proves the target has even parity. The target is unreachable.

## The Proof

Now we assemble everything into a formal proof. The invariant is the parity of inversions.

**Theorem.** The target state is unreachable from the starting state.

**Proof.** By induction on $n$, the number of moves.

Let $P(n)$ be: "After any sequence of $n$ moves from the starting state, the parity of the number of inversions is odd."

**Base case:** $P(0)$. Zero moves means we're still in the start state. One inversion. Odd. $\checkmark$

**Inductive step:** Assume $P(n)$. Consider any sequence of $n + 1$ moves $M_1, \ldots, M_{n+1}$. By $P(n)$, the parity after moves $M_1, \ldots, M_n$ is odd. By the Corollary, move $M_{n+1}$ doesn't change the parity. So the parity after all $n + 1$ moves is still odd. $P(n+1)$ holds.

The target state has 0 inversions (even parity). By the invariant, it is never reached. $\square$

The proof of the theorem was short — because we did the real work in the lemmas and corollary beforehand. That's the power of good organization: lemmas are subroutines.

The 15-puzzle — the same problem on a $4 \times 4$ grid — was offered with a \$1,000 prize in the 1880s (worth perhaps \$250,000 today). Same invariant, one extra lemma. Nobody collected.

## Why Invariants Matter

The eight puzzle is a toy. The technique is not. If you're building software for a nuclear reactor, there's a state you'd like to avoid: meltdown. If you can find an invariant that holds at startup, is preserved by every control action, and is absent from the meltdown state — you've proven your reactor can't melt down. Same for airplane software (no crash state) or radiation devices (no "fry the patient" state).

The three-part structure — initial condition, preservation, excluded state — is the same whether you're sliding tiles or preventing catastrophes:

| Domain | Initial Condition | Preservation | Excluded State |
|--------|-------------------|--------------|----------------|
| Puzzle | Start has odd inversions | Moves preserve parity | Target has even inversions |
| Reactor | All rods inserted | Control law maintains margins | Meltdown |
| Lock-free queue | Queue consistent | Each CAS preserves consistency | Data corruption |
| Loop invariant | Precondition | Loop body maintains invariant | Postcondition violated |

## Strong Induction

For the rest of the lecture, we'll talk about a different kind of induction. **Strong induction** is similar to ordinary induction but easier to use for certain problems.

**Ordinary induction:** Assume $P(n)$, prove $P(n+1)$.

**Strong induction:** Assume $P(0), P(1), \ldots, P(n)$ — all of them — prove $P(n+1)$.

You get to assume the predicate holds for *every* value up to $n$, not just $n$ itself. It's a more generous starting point for the inductive step. Any proof by ordinary induction is also a proof by strong induction (just ignore the extra assumptions). But in practice, some proofs become dramatically easier when you can reach back to earlier cases.

The strong induction axiom:

$$\bigl[P(0) \;\wedge\; \forall n.\; (P(0) \wedge P(1) \wedge \cdots \wedge P(n)) \Rightarrow P(n+1)\bigr] \;\Rightarrow\; \forall n.\; P(n)$$

Now in fact, anything you can prove with strong induction you can prove with ordinary induction — it might just be harder. Strong induction doesn't let you prove *more*; it makes proofs *easier*. We're about to see a problem where the proof is much easier by getting to assume all of $P(0)$ through $P(n)$.

## The Unstacking Game

Start with a stack of $n$ blocks. On each turn, split one stack into two non-empty sub-stacks. If you split a stack of size $a + b$ into stacks of size $a$ and $b$, you score $a \times b$ points. Keep splitting until every stack has height 1. Your total score is the sum across all splits.

The goal: get the most points.

Imagine a competition. Team A goes first with 8 blocks: they split 8 into 4 and 4 — that's $4 \times 4 = 16$ points. Maximum first move, smart play. They continue splitting and end with a total of 28.

Team B takes a different approach — they peel off one block at a time. Their first move is a pathetic $8 \to 7 + 1$ for 7 points. They look like they're losing badly. But they keep peeling: $7 \to 6 + 1$ for 6, then 5, 4, 3, 2, 1.

Total: $7 + 6 + 5 + 4 + 3 + 2 + 1 = 28$.

It's a tie. Team A went for maximum first moves; Team B used the worst possible strategy at every step. Same score. Is it possible that every strategy gives 28?

Yes. Every strategy gives 28. And you can't beat 28, and you can't do worse. The game is rigged — the score is always the same regardless of how you play.

Let's verify before we prove:

```python
# uv run --with hypothesis python
import random
from hypothesis import given, settings, strategies as st

def random_unstack(n: int) -> int:
    """Play the unstacking game with a random strategy. Return total score."""
    if n <= 1:
        return 0
    stacks = [n]
    score = 0
    while any(s > 1 for s in stacks):
        big = [i for i, s in enumerate(stacks) if s > 1]
        idx = random.choice(big)
        s = stacks.pop(idx)
        k = random.randint(1, s - 1)
        score += k * (s - k)
        stacks.extend([k, s - k])
    return score

@given(st.integers(min_value=1, max_value=100))
@settings(max_examples=500)
def test_unstacking_score(n):
    for _ in range(5):  # try 5 random strategies per n
        assert random_unstack(n) == n * (n - 1) // 2

test_unstacking_score()
print("All strategies give n*(n-1)/2 — verified for n=1..100 with random splits.")
```

**Theorem.** Every strategy for the $n$-block unstacking game produces the same score: $S(n) = \frac{n(n-1)}{2}$.

**Proof.** By strong induction on $n$.

Let $P(n)$ be: "Every strategy for the $n$-block game scores exactly $\frac{n(n-1)}{2}$."

**Base case:** $P(1)$. One block, no moves, score is 0. And $\frac{1 \cdot 0}{2} = 0$. $\checkmark$

**Inductive step:** Assume $P(1), P(2), \ldots, P(n)$. Consider the $(n+1)$-block game. The first move splits the stack into two parts of size $k$ and $n + 1 - k$, for some $1 \leq k \leq n$.

The score for this move is $k(n + 1 - k)$.

Now here's where strong induction earns its keep. For Team B's peeling strategy, $k$ is always 1 — we'd only need $P(n)$, and ordinary induction would suffice. But for a *general* strategy, $k$ could be anything. We need $P(k)$ for every $k \leq n$. That's exactly what strong induction gives us.

By $P(k)$: the left sub-game scores $\frac{k(k-1)}{2}$.

By $P(n+1-k)$: the right sub-game scores $\frac{(n+1-k)(n-k)}{2}$.

Total:
$$S(n+1) = k(n+1-k) + \frac{k(k-1)}{2} + \frac{(n+1-k)(n-k)}{2}$$

I've got $k$ in every single term. The score *looks* like it depends on the split. So I'm stuck. Does this depend on $k$?

Combining over a common denominator of 2:

$$= \frac{2k(n+1-k) + k(k-1) + (n+1-k)(n-k)}{2}$$

Expanding:

$$2k(n+1-k) = 2kn + 2k - 2k^2$$
$$k(k-1) = k^2 - k$$
$$(n+1-k)(n-k) = n^2 + n - 2kn - k + k^2$$

Summing the numerator:

$$2kn + 2k - 2k^2 + k^2 - k + n^2 + n - 2kn - k + k^2$$

Now watch the $k$'s disappear: $2kn - 2kn = 0$. $-2k^2 + k^2 + k^2 = 0$. $2k - k - k = 0$.

What remains: $n^2 + n = n(n+1)$.

$$S(n+1) = \frac{n(n+1)}{2}$$

The $k$ is gone. The score doesn't depend on how you split. $\square$

The Dafny verifier can confirm this — strong induction maps directly to a recursive function with a decreasing argument:

```dafny
function UnstackScore(n: nat): nat
  ensures UnstackScore(n) == n * (n - 1) / 2
  decreases n
{
  if n <= 1 then 0
  else
    // Any split gives the same answer, so pick the simplest one.
    (n - 1) + UnstackScore(n - 1)
}
```

Dafny's verifier checks the postcondition `UnstackScore(n) == n * (n - 1) / 2` for all `n`. The `decreases n` annotation proves termination.

## When You're Stuck: Strengthen the Hypothesis

We nearly failed this proof. The first attempt — $P(n)$: "every strategy gives the same score" — got stuck because we couldn't cancel $k$ without knowing *what* the score actually was.

The fix: a stronger hypothesis. $P(n)$: "every strategy scores exactly $\frac{n(n-1)}{2}$." This gives us a formula to substitute, and the algebra cancels.

What do you do when you're stuck with an induction proof? Make the hypothesis *stronger*. It sounds paradoxical — you're trying to prove *more* — but a stronger hypothesis gives you more to work with in the inductive step. We saw the same principle with the tiling problem in Lecture 2: "any missing square can be tiled" was harder to state than "center missing can be tiled," but the stronger version made the recursive step work.

If at first you don't succeed, try something harder.

## Summary

| Technique | What It Proves | Structure |
|-----------|---------------|-----------|
| **Invariant** | A state is unreachable | Property holds initially, preserved by transitions, absent in target |
| **Strong induction** | $P(n)$ for all $n$ | Assume $P(0) \ldots P(n)$ to prove $P(n+1)$ |

Both are induction in disguise. An invariant proof *is* an induction proof where $P(n)$ = "the property holds after $n$ transitions." Strong induction *is* ordinary induction with a more generous assumption.

| Proof Technique | Programming Pattern |
|-----------------|---------------------|
| Invariant | Loop invariant, state machine safety property |
| Strong induction | Recursive function with variable-sized sub-problems |
| Strengthening the hypothesis | Strengthening preconditions to make recursion work |
| Inversions (disorder measure) | Sorting metrics, progress functions |

These tools sit at different points on a spectrum, from quickest to most rigorous:

| Tool | Method | Guarantee | Effort |
|------|--------|-----------|--------|
| **Hypothesis** | Random test inputs | "No bugs found in $N$ samples" | Write a `@given` test |
| **Z3** | Constraint solving (SMT) | `sat`/`unsat` — existence proof | Encode as constraints |
| **Dafny** | Full formal verification | "Proven correct for all inputs" | Write spec in Dafny |
| **Lean4** | Proof assistant | "Mathematically proven" | Construct a formal proof |

For the unstacking game, we used Hypothesis as a quick sanity check, then Dafny to verify the algorithm. For the 8-puzzle, we used random simulation, then Z3 to prove unsatisfiability, then induction for the full mathematical proof.

## Further Reading

- [15 Puzzle Solvability](https://en.wikipedia.org/wiki/15_puzzle#Solvability) — The $4 \times 4$ version uses the same parity invariant with one extra twist
- [Loop Invariants in Dafny](https://dafny.org/dafny/OnlineTutorial/guide) — Writing and verifying loop invariants
- [Strong Induction on Brilliant](https://brilliant.org/wiki/strong-induction/) — More examples of when strong induction simplifies proofs
- [TLA+ and Invariant Checking](https://lamport.azurewebsites.net/tla/tla.html) — Leslie Lamport's specification language for verifying system invariants
- [Lean4 Induction Tactics](https://lean-lang.org/theorem_proving_in_lean4/induction_and_recursion.html) — Strong induction and well-founded recursion in Lean4
