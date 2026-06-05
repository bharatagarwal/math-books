# Looking Back

You have solved the problem. You have checked each step, written the argument, reached the answer. Now shut the book and move on.

Do not do this. You are about to miss the most instructive phase of the work.

By looking back at the completed solution—reconsidering the result and the path that led to it—you consolidate your knowledge and develop your ability to solve problems. No problem is completely exhausted. There remains always something to do; with sufficient study and penetration, you could improve any solution, and in any case you can always improve your understanding of the solution.

This is the fourth phase. It asks three questions.


## Can you check the result?

Each check gives you what Polya called "experimental evidence"—confidence from a *different source* than the derivation itself. You were convinced before because you derived it carefully. After checking, your gain in confidence comes from independent verification, "like perceiving an object through two different senses."

**Test special cases.** Substitute simple values. For the subset formula $2^n$: does $n = 0$ give $1$? Does $n = 1$ give $2$? Does $n = 3$ give $8$?

**Test boundary cases.** What happens at the extremes? Does the formula degenerate gracefully? The number of edges in $K_n$ is $\binom{n}{2}$. For $n = 0$: zero edges. For $n = 1$: zero edges. For $n = 2$: one edge. Each makes sense.

**Check symmetry.** If the problem is symmetric in its data, the answer should be too. Choosing which $k$ elements to include is the same as choosing which $n - k$ to exclude, so $\binom{n}{k}$ must equal $\binom{n}{n-k}$. If your formula lacked this symmetry, something would be wrong.

**Check dimensions or types.** A count must be a non-negative integer. A probability must lie in $[0, 1]$. A graph on $n$ vertices has at most $\binom{n}{2}$ edges. Polya devoted careful attention to this: if the period $T$ of a pendulum depends only on length $l$ and gravitational acceleration $g$, then purely from dimensional requirements, $T = c\sqrt{l/g}$. In discrete math the analogue is type-checking.

**Verify that you used all the data.** If some datum does not appear in the answer, either the datum was redundant or you dropped it. This question checks both the result and the argument.

**Check monotonicity.** Does the answer increase when you expect it to? Adding one element to a set should roughly double the subset count, and indeed $2^{n+1} = 2 \cdot 2^n$.

**Brute-force a small case.** For $n = 3$, list all subsets of $\{1, 2, 3\}$: $\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}$. Eight subsets. $2^3 = 8$. Good.

These checks are fast. None is a proof. But a result that passes all of them is almost certainly correct, and a result that fails any of them is certainly wrong.


## Can you derive the result differently?

"In order to convince ourselves of the presence or of the quality of an object, we like to see and to touch it. And as we prefer perception through two different senses, so we prefer conviction by two different proofs."

For the subset count, we have three proofs:

- **Bijection with binary strings.** Each subset maps to a unique $n$-bit string; there are $2^n$ such strings.
- **Induction.** Each new element doubles the number of subsets.
- **Multiplication principle.** For each of $n$ elements, you make an independent binary choice. $2 \times 2 \times \cdots \times 2 = 2^n$.

Three arguments, each self-contained, each illuminating a different facet. The bijection shows *why* the answer is a power of two. The induction shows *how* the count grows. The multiplication principle shows *where* the count comes from.

We prefer a short and intuitive argument to a long and heavy one. *Can you see it at a glance?* The multiplication principle gives the most compact proof. A proof you can see at a glance is a proof you can reconstruct from memory—a proof you own rather than merely recall.

The question is not idle curiosity. Each new proof you find for a known result strengthens a different connection and prepares you for a different class of future problems.


## Can you use the result, or the method, for some other problem?

This is where understanding consolidates into knowledge. The solution you do not examine is the solution you cannot reuse.

The binary-string representation of subsets is not a one-problem trick. It is a general technique. Here are immediate consequences:

1. **Subsets of a given size.** The number of $k$-element subsets of an $n$-element set equals the number of $n$-bit strings with exactly $k$ ones. This is $\binom{n}{k}$.

2. **The binomial sum.** Summing over all sizes: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$. The same result, seen from another angle.

3. **Inclusion-exclusion.** Subsets avoiding element $j$ correspond to strings with bit $j$ set to $0$. There are $2^{n-1}$ such subsets. The representation makes this obvious.

4. **Characteristic functions.** The binary string for a subset $S$ is its characteristic function $\chi_S : \{1, \ldots, n\} \to \{0, 1\}$. This generalizes: functions to a $k$-element set correspond to $k$-colorings, and there are $k^n$ of them. The subset result is the special case $k = 2$.

The method of the proof—establishing a bijection to a simpler set—is even more reusable than the result. Every time you want to count a complicated set, ask: is there a simpler set in bijection with it?

Looking back at the method, you extract a transferable skill. Looking back at the result, you see connections. Both strengthen your ability to solve future problems.


## The mushroom principle

Polya described the future mathematician looking back: "Surveying the course of his work and the final shape of the solution, he may find an unending variety of things to observe. He may meditate upon the difficulty of the problem and about the decisive idea; he may try to see what hampered him and what helped him finally."

This is not an advanced activity reserved for professionals. It is how understanding works. If you have made an honest effort at a problem and solved it, you are naturally eager to see what else you could accomplish, and how you could do equally well another time. That eagerness is the engine of looking back.

"Look around when you have got your first mushroom or made your first discovery; they grow in clusters."

Problems are not isolated. The connections between them are where mathematical understanding lives. You have a natural opportunity to investigate those connections when looking back at the solution. Check it, rederive it, connect it. Then move on.


## Questions to keep

- *Can you check the result?*—special cases, boundary cases, symmetry, types.
- *Can you derive the result differently?*—a second proof from a different direction.
- *Can you use the result, or the method, for some other problem?*—the mushroom principle.
