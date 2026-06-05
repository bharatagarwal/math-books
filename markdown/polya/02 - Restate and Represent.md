# Restate and Represent

Understanding a problem is not the same as being ready to solve it. You may know the unknown, the data, and the condition—and still be stuck, because the problem is stated in a form that resists work. The next move is to change the form.

Restating a problem, unpacking its definitions, choosing notation, drawing a figure, separating the condition into parts—this is representational work. It does not look like solving. It looks like preparation. But it is often the main intellectual contribution of the understanding phase. A problem restated well is half solved.

## Going back to definitions

Pascal stated the rule: *Substitute mentally the defining facts for the defined terms.*

Every technical term in a problem is a compressed package of structure. When you unpack it, new elements and new relations enter your picture of the problem. That is why going back to definitions works—not because it clarifies language, but because it changes what you can see.

In our running example, the problem says: *How many subsets does a set with $n$ elements have?* The word "subset" is doing all the work. Go back to its definition. A subset $T$ of $S = \{a_1, a_2, \ldots, a_n\}$ is a set such that every element of $T$ is also an element of $S$. Restate this: for each element $a_i$, either $a_i \in T$ or $a_i \notin T$. A subset is a sequence of $n$ independent binary decisions.

That restatement—from "subset" to "sequence of binary choices"—is the key insight that will later give us $2^n$. It came from nothing more than unpacking a definition.

Going back to definitions is not a sign of weakness. It is a standard move, and it is more powerful than it looks. "When we have to solve a proposed problem involving some derived notion... and we wish to go back to its definition, we may have a choice among various definitions. Much may depend in such a case on choosing the definition that fits the case."

### Choosing among definitions

A concept may have more than one definition. A graph is a set of vertices and edges—or an adjacency matrix—or a collection of adjacency lists. Each definition foregrounds different structure. When you are stuck, try a different definition of the same object. The right definition for this problem may not be the one you learned first.

### Definition as discovery tool

Pascal emphasized that going back to definitions helps in *checking* arguments—you verify that each essential term was actually used. Hadamard added the complementary observation: going back to definitions is equally important in *devising* arguments. When you are stuck, the act of unpacking a definition often reveals the next step. It is not just a verification tool; it is a discovery tool.

## Restating the problem

If you can say the same thing in two different ways, you understand it better than if you can say it in only one.

A restatement that uses different words, or that unpacks a definition, can transform an opaque problem into a transparent one. The subset problem becomes the binary-string problem. A problem about divisibility becomes a problem about prime factorizations. A problem about paths in a graph becomes a problem about matrix powers.

Ask yourself:

*Could you restate the problem? Could you restate it still differently?*

Each restatement is a new angle of attack. Some restatements are lateral—they express the same structure in a different language. Others are reductive—they replace an unfamiliar object with a familiar one. Both are valuable. The goal is to find the form of the problem that makes the solution visible.

## Notation

If you want to feel the importance of notation, try adding a few numbers in Roman numerals: MMMXC + MDXCVI + MDCXLVI + MDCCLXXXI + MDCCCLXXXVII. The difficulty is not mathematical—it is notational. "We can scarcely overestimate the importance of mathematical notation."

Choosing notation is part of understanding. A well-chosen symbol makes the logic transparent; a badly-chosen one obscures it. "An important step in solving a problem is to choose the notation. It should be done carefully. The time we spend now on choosing the notation may be well repaid by the time we save later by avoiding hesitation and confusion."

Good notation has four properties:

1. **Unambiguous.** The same symbol never means two different things in the same problem.
2. **Easy to remember.** Initials help: $n$ for the number of elements, $S$ for the set.
3. **Mirrors the problem's structure.** "The order and connection of signs should suggest the order and connection of things." Related quantities get related names; different roles get different names.
4. **Pregnant.** A notation is "pregnant" when it expresses more than the bare minimum. The notation $\triangle ABC \sim \triangle EFG$ tells you not only that the triangles are similar but which vertices correspond: $A \leftrightarrow E$, $B \leftrightarrow F$, $C \leftrightarrow G$.

Symbols also carry connotations from repeated use. The letter $e$ means the base of natural logarithms; $\pi$ means the ratio of circumference to diameter. Using these for other purposes invites confusion. Conversely, standing notation—conventions like $n$ for a count, $i$ for an index—gains power from familiarity. Formulas remembered are formulas available.

### Notation for the running example

For our subset-counting problem:

- $S = \{a_1, a_2, \ldots, a_n\}$ for the set
- $\mathcal{P}(S)$ for the collection of all subsets
- $|\mathcal{P}(S)|$ for the count we seek

But the restatement suggested a second representation: each subset as a binary string of length $n$, position $i$ being $1$ if $a_i$ is included and $0$ if not.

| Subset of $\{a, b, c\}$ | Binary string |
|---|---|
| $\emptyset$ | $000$ |
| $\{a\}$ | $100$ |
| $\{b\}$ | $010$ |
| $\{a, b\}$ | $110$ |
| $\{c\}$ | $001$ |
| $\{a, c\}$ | $101$ |
| $\{b, c\}$ | $011$ |
| $\{a, b, c\}$ | $111$ |

This table is a figure of sorts—not a geometric diagram, but a structured picture of the data. It makes visible what the abstract statement hides: the subsets of a $3$-element set are in exact correspondence with the $2^3 = 8$ binary strings of length $3$.

## Figures beyond geometry

Figures are not only for geometry. "Figures are not only the object of geometric problems but also an important help for all sorts of problems in which there is nothing geometric at the outset." Any representation that lets you see the structure—a table, a tree, a graph, a grid, a state diagram—counts as a figure. The purpose is the same: offload part of the problem from working memory onto paper, where you can examine it at leisure.

"To find a lucid geometric representation for your nongeometrical problem could be an important step toward the solution."

A few practical notes:

1. **The figure should not suggest unwarranted special cases.** A table for $n = 3$ is a special case. Do not assume properties that hold only for small $n$.
2. **Figures are aids to reasoning, not substitutes for it.** The table above suggests a bijection between subsets and binary strings, but it does not prove one.
3. **Use the figure to check your understanding.** Can you point to the unknown in your figure? Can you point to each datum? If not, the figure is incomplete.
4. **Vary the figure.** A second figure from a different viewpoint protects against false conclusions.

## Separating the parts of the condition

When the condition of a problem has several parts, separate them. Consider each part by itself. Then consider them together again.

This is the move Polya calls *decomposing.* It sounds trivial, but it is often the step that makes a problem tractable. "Find all integers $n$ such that (I) $n$ divides $2^n - 2$ and (II) $n$ is prime." Each clause restricts the unknown in a different way. Separating them lets you explore each restriction independently and then find their intersection.

The method generalizes into a powerful pattern. Keep only one part of the condition and drop the other. The unknown is no longer fully determined—you get a set of candidates satisfying one constraint. Do the same for the other constraint. Then look for the intersection. The move is always the same: separate, explore each part, recombine.

A subtlety: decomposition can go too far. If you break a condition into too many tiny pieces, you lose sight of how they interact. Decompose as far as you need to, but no further. The goal is clarity, not atomization.

*Separate the various parts of the condition. Can you write them down?*

Writing them down is not pedantry. It is a check on your understanding. If you cannot write the condition in parts, you may not have fully grasped it.

## Questions to keep

- *Could you restate the problem? Could you restate it still differently?* Go back to definitions.
- *What notation makes this problem's structure visible?*
- *Separate the various parts of the condition. Can you write them down?*
