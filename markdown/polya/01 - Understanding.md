# Understanding

You have to understand the problem. This sounds obvious. It is obvious. And yet most failures in problem-solving trace back to this phase — not to a lack of cleverness in phase two, not to an arithmetic slip in phase three, but to a failure right here, at the beginning, where you did not fully grasp what the problem was asking.

"It is foolish to answer a question that you do not understand." Polya says this plainly, and it needs no softening. The foolishness he describes is not rare. It is the most common mistake. You see a problem, you feel a twinge of recognition, and you start computing. You skip the phase where you make the problem yours. Twenty minutes later you have an answer to a question nobody asked.

"The worst may happen if the student embarks upon computations or constructions without having understood the problem." Polya states this as a warning about the four phases, and it applies to you directly. Of all the ways to fail, starting to compute before you understand is the most wasteful. Every other phase — devising a plan, carrying it out, looking back — depends on this one. Skip it, and you build on sand.

Understanding is not passive. It is not reading the problem statement and nodding. It is an active interrogation: you ask yourself questions, you name things, you draw pictures, you restate. The goal is to reach a state where you could set the problem aside for an hour and reconstruct it from memory — not the exact words, but the structure. If you cannot do that, you have not understood it.

The problem itself matters. If it is too hard, you will flounder. If it is too easy, you will learn nothing. If it has no natural interest, you will have no desire to solve it — and without desire, there is no sustained effort. Choose problems that genuinely engage you, and give yourself time to settle into them before reaching for techniques. Polya is specific about this: "the problem should be well chosen, not too difficult and not too easy, natural and interesting, and some time should be allowed for natural and interesting presentation." Motivation is not a luxury — it is a prerequisite.

## Start from the statement

Start from the statement of the problem. Read it. Then read it again.

Visualize the problem as a whole, as clearly and as vividly as you can. Do not concern yourself with details yet. Get the shape of it. What kind of thing is being asked? Is it a number? A set? A proof? A construction? A procedure?

Then start again from the statement. This time, you are not reading for the gist. You are reading for the parts. What exactly is given? What exactly is sought? Where does the problem's difficulty lie — in the sheer amount of data, in an unfamiliar term, in a condition that is hard to picture?

This two-pass reading — first for shape, then for parts — is what Polya's Dialogue describes as "Getting Acquainted" and then "Working for Better Understanding." In the first pass, you "visualize the problem as a whole as clearly and as vividly as you can." In the second, you "isolate the principal parts of your problem... consider them one by one, consider them in turn, consider them in various combinations, relating each detail to other details and each to the whole of the problem."

The two-pass habit is not a rule imposed from outside. It is what you do naturally when you take a problem seriously. The suggestion is only to do it deliberately, so that you do not skip it when you are impatient.

## Understanding the problem as a whole before going into detail

There is a specific danger in the understanding phase that Polya warns about: losing the forest for the trees.

"Let us, first of all, understand the problem as a whole. Having understood the problem, we shall be in a better position to judge which particular points may be the most essential. Having examined one or two essential points we shall be in a better position to judge which further details might deserve closer examination. Let us go into detail and decompose the problem gradually, but not further than we need to."

This is the graduated decomposition principle. You start with the whole, then zoom into details, but only as far as the problem requires. A very foolish and common habit is to start working at details — fiddling with a specific term, trying a computation — before grasping the problem as a whole. Resist this. The whole first, then the parts.

## Unknown, data, condition

Every problem to find has three principal parts:

- **The unknown** — what you are looking for.
- **The data** — what you are given.
- **The condition** — how the unknown is linked to the data.

Ask yourself these three questions, in this order:

*What is the unknown?*

*What are the data?*

*What is the condition?*

These questions sound mechanical. They are mechanical — and that is the point. They work on every problem, from a puzzle to a research question, because they are maximally general. Their generality is what makes them useful: they force you to name things you might otherwise leave vague. "Our problem may be algebraic or geometric, mathematical or nonmathematical, theoretical or practical, a serious problem or a mere puzzle; it makes no difference, the questions make sense and might help us to solve the problem."

**A running example.** Suppose the problem is: *How many subsets does a set with $n$ elements have?*

What is the unknown? A number — the count of subsets of an $n$-element set.

What are the data? A single positive integer $n$, the size of the set.

What is the condition? Each subset is a selection of zero or more elements from the set, and two subsets are different if they differ in at least one element.

That much is straightforward. But notice what the exercise already does: it forces you to think about what "subset" means. You need the definition. You need to know that the empty set counts (it selects zero elements) and that the full set counts (it selects all of them). If you did not pause to state the condition, you might forget one of these edge cases and be off by one or two in your count.

## Problems to find vs problems to prove

Not all problems are the same kind. Polya distinguishes two families, and the distinction matters because the questions you ask yourself are different for each.

A **problem to find** asks you to determine some object — a number, a set, a function, a configuration — satisfying a stated condition. The principal parts are the unknown, the data, and the condition.

A **problem to prove** asks you to establish the truth or falsity of a clearly stated assertion. The principal parts are the **hypothesis** (what you assume) and the **conclusion** (what you must show follows).

Our subset-counting example is a problem to find: we want a number. But once we guess that the answer is $2^n$, the problem shifts. Now we have a problem to prove: *The number of subsets of an $n$-element set is $2^n$*. The hypothesis is that we have a set with $n$ elements; the conclusion is that the count of its subsets equals $2^n$.

The shift from finding to proving happens constantly in mathematical work. You compute, you guess, you conjecture — and then you must prove. The understanding phase applies to both kinds.

For a problem to find, the questions are:

*What is the unknown? What are the data? What is the condition?*

For a problem to prove, the corresponding questions are richer than you might expect:

*What is the hypothesis? What is the conclusion?*

*Separate the various parts of the hypothesis.*

*Find the connection between the hypothesis and the conclusion.*

*Look at the conclusion! And try to think of a familiar theorem having the same or a similar conclusion.*

*Keep only a part of the hypothesis, drop the other part; is the conclusion still valid?*

*Could you derive something useful from the hypothesis?*

*Could you think of another hypothesis from which you could easily derive the conclusion?*

*Did you use the whole hypothesis?*

These prove-side questions parallel the find-side questions almost exactly. "Look at the conclusion" corresponds to "Look at the unknown." "Keep only a part of the hypothesis" corresponds to "Keep only a part of the condition." The two families of problems are structurally the same; only the vocabulary changes.

Notice in particular: "Look at the conclusion! And try to think of a familiar theorem having the same or a similar conclusion." This is the prove-side analogue of "Look at the unknown! And try to think of a familiar problem having the same or a similar unknown." Both direct you to focus on what you are trying to achieve, then search your memory for something that achieved the same kind of thing. Both are enormously productive.

If you cannot state the hypothesis and conclusion distinctly, you do not yet understand the theorem you are trying to prove. And if you cannot see the parallel between the find-questions and the prove-questions, practice both until the parallel is second nature.

## Restating and definitions

One of the most powerful moves in the understanding phase is to restate the problem. A restatement that uses different words, or that unpacks a definition, can transform an opaque problem into a transparent one.

### Going back to definitions

Pascal stated the rule: *Substitute mentally the defining facts for the defined terms.* Every unfamiliar or technical term in the problem is a candidate for this substitution.

When you encounter a term you half-remember — say, "the power set of $S$" — you know it has something to do with subsets, but the phrase sits in your mind as a lump of jargon. The moment you go back to the definition — "the power set of $S$ is the set of all subsets of $S$" — the jargon dissolves. You can now work with the actual objects instead of the label.

Going back to definitions is not a sign of weakness. It is a standard move, and it is more powerful than it looks. Here is why: when you replace a technical term by its definition, you introduce new elements and new relations into your conception of the problem. The resulting change can be important. Polya calls this procedure "elimination of technical terms" and demonstrates it with a dialogue about finding the intersection of a line and a parabola. The student knows the word "parabola" but is stuck. The teacher says: go back to the definition. The student recalls that a parabola is the locus of points equidistant from a focus and a directrix. Immediately, new elements enter the picture — the distances $PF$ and $PQ$ — and the problem transforms from "find the intersection with a parabola" into "find a point on the line equidistant from a point and a line." The unfamiliar technical terms vanish; the problem becomes solvable with basic tools.

The lesson is general: going back to definitions introduces new elements that change the problem's structure. That is why it works. It is not just a clarification — it is often the main intellectual move of the understanding phase.

### Choosing among definitions

A concept may have more than one definition, and much can depend on choosing the right one. Archimedes, faced with finding the surface area of a sphere, had a choice: the sphere as the locus of points equidistant from a center, or the sphere as the surface of revolution of a circle. He chose the second, because it naturally led to approximation by cones and frustums. The first definition, while correct, suggested no such approach.

For discrete mathematics, an analogous situation: a graph can be defined as a set of vertices and edges, or equivalently as an adjacency matrix, or as a collection of adjacency lists. Each definition foregrounds different structure. "When we have to solve a proposed problem involving some derived notion... and we wish to go back to its definition, we may have a choice among various definitions. Much may depend in such a case on choosing the definition that fits the case." When you are stuck, try a different definition of the same object. The right definition for this problem may not be the one you learned first.

### Hadamard's complementary point

Pascal emphasized that going back to definitions helps in *checking* arguments — you verify that each essential term was actually used. Hadamard added the complementary observation: going back to definitions is equally important in *devising* arguments. It is not just a verification tool; it is a discovery tool. When you are stuck, the act of unpacking a definition often reveals the next step.

### The power of restatement

In our running example, the problem says "subsets." The definition of a subset of $S = \{a_1, a_2, \ldots, a_n\}$ is: a set $T$ such that every element of $T$ is also an element of $S$. But there is another way to say this. For each element $a_i$, either $a_i \in T$ or $a_i \notin T$. A subset is a sequence of $n$ independent yes/no decisions. This restatement — from "subset" to "sequence of binary choices" — is the key insight that will later give us the answer $2^n$. And it came from nothing more than going back to the definition and restating what we found.

Restating a problem is not decoration. It is often the main intellectual work of the understanding phase. Ask yourself:

*Could you restate the problem? Could you restate it still differently?*

If you can say the same thing in two different ways, you understand it better than if you can say it in only one.

## Notation and figures

### Why notation matters

If you want to feel the importance of notation, try adding a few numbers in Roman numerals: MMMXC + MDXCVI + MDCXLVI + MDCCLXXXI + MDCCCLXXXVII. The difficulty is not mathematical — it is notational. The Arabic system, with its positional structure, makes the same computation trivial.

Polya opens his discussion of notation with exactly this exercise. The point is not historical. It is that notation is not a superficial convenience — it is a tool that shapes what you can think. "We can scarcely overestimate the importance of mathematical notation." An average modern student, equipped with standard algebraic notation, has an immense advantage over a Greek mathematician in solving problems that exercised the genius of Archimedes.

### Choosing notation

Choosing notation is part of understanding. If you have written code, you already know this: a well-named variable makes the logic transparent; a badly-named one obscures it. The mathematical version is the same phenomenon, amplified. When you name the unknown $x$ and the data $n$, you are making a commitment: you are saying that these are the objects that matter, and you are giving yourself a language in which to think about their relationships.

"An important step in solving a problem is to choose the notation. It should be done carefully. The time we spend now on choosing the notation may be well repaid by the time we save later by avoiding hesitation and confusion."

Good notation has several properties:

1. **Unambiguous.** The same symbol never means two different things in the same problem.
2. **Easy to remember.** Initials help: $n$ for the number of elements, $S$ for the set, $r$ for the rate. But initials are not always possible — if $r$ is already taken for "rate," you cannot also use it for "radius" in the same problem.
3. **Structure mirrors the problem's structure.** "The order and connection of signs should suggest the order and connection of things." Related quantities get related names. If $a, b, c$ are three edges playing symmetric roles, use consecutive letters to signal that symmetry. If instead the three lengths play different roles (length, width, height), the notation $l, w, h$ might be better. Choose based on what matters.
4. **Pregnant.** A notation is "pregnant" when it expresses more than the bare minimum. The modern notation $\triangle ABC \sim \triangle EFG$ not only says the triangles are similar — the order of vertices tells you which corresponds to which: $A \leftrightarrow E$, $B \leftrightarrow F$, $C \leftrightarrow G$. From this alone you can derive $\angle A = \angle E$ and $AB : BC = EF : FG$ *without looking at the figure*. Older notation expressed less and permitted fewer consequences.

### Second meanings and standing notation

Symbols acquire connotations from repeated use, just as words do. The letter $e$ means the base of natural logarithms; $\pi$ means the ratio of circumference to diameter; $i$ means $\sqrt{-1}$. Using these symbols for other purposes in the same problem invites confusion. Conversely, a "standing notation" — like the convention $A, B, C$ for vertices, $a, b, c$ for opposite sides, $\alpha, \beta, \gamma$ for angles — gains power from familiarity. You remember formulas in standing notation. Formulas remembered are formulas available.

### Notation for the running example

For our subset-counting problem, reasonable notation is:

- $S = \{a_1, a_2, \ldots, a_n\}$ for the set
- $\mathcal{P}(S)$ for the collection of all subsets
- $|\mathcal{P}(S)|$ for the count we seek

But there is a second representation that the restatement suggested: represent each subset as a binary string of length $n$, where position $i$ is $1$ if $a_i$ is included and $0$ if not. Under this representation:

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

This table is a figure of sorts — not a geometric diagram, but a structured picture of the data. It makes visible what the abstract statement hides: the subsets of a $3$-element set are in exact correspondence with the $8 = 2^3$ binary strings of length $3$.

### Figures beyond geometry

Polya is emphatic that figures are not only for geometry: "Figures are not only the object of geometric problems but also an important help for all sorts of problems in which there is nothing geometric at the outset." Any representation that lets you see the structure — a table, a tree, a graph, a grid, a diagram of states and transitions — counts as a figure. The purpose is the same: to offload part of the problem from your working memory onto paper, where you can examine it at leisure.

"To find a lucid geometric representation for your nongeometrical problem could be an important step toward the solution." Graphs and diagrams are used in all sciences — physics, chemistry, economics, psychology. In discrete mathematics, the practice is everywhere: Hasse diagrams for partial orders, state diagrams for automata, decision trees for algorithms.

A few practical notes on figures, adapted from Polya's own advice:

1. **The figure should not suggest unwarranted special cases.** If you draw a table for $n = 3$, remember that you are looking at a special case. Do not assume properties that hold only for small $n$.
2. **Figures are aids to reasoning, not substitutes for it.** The table above suggests a bijection between subsets and binary strings, but it does not prove one. That comes later.
3. **Use the figure to check your understanding.** Can you point to the unknown in your figure? Can you point to each datum? If not, the figure is incomplete.
4. **Vary the figure.** An inaccurate or overly special figure can occasionally suggest a false conclusion. Drawing a second figure from a different viewpoint protects against this.
5. **Choose the most convenient construction order.** It does not matter in which order you assemble the elements of a figure, as long as the required relations hold. Choose whatever order is easiest. If constructing $A$ from $B$ is hard but constructing $B$ from $A$ is easy, start with $A$.

## Separating the parts of the condition

When the condition of a problem has several parts, separate them. Consider each part by itself. Then consider them together again.

This is the move Polya calls *decomposing.* It sounds trivial, but it is often the step that makes a problem tractable. If the condition is "find a word that (I) means a part of a machine and (II) reads the same forwards and backwards," then separating those two parts gives you two independent handles. You can brainstorm words satisfying (I), then filter by (II), or vice versa. This is exactly how Polya solves the crossword clue for "rotor" — by separating the meaning-constraint from the spelling-constraint, treating each as a "locus," and finding their intersection.

In mathematical problems, the condition often has a similar structure. "Find all integers $n$ such that (I) $n$ divides $2^n - 2$ and (II) $n$ is prime." Each clause restricts the unknown in a different way. Separating them lets you explore each restriction independently and then find their intersection.

For our subset problem, the condition is simple enough that decomposition is unnecessary. But as problems grow in complexity — multiple constraints, multiple unknowns — the habit of separating the condition becomes essential.

The method generalizes into a powerful pattern. If you keep only one part of the condition and drop the other, the unknown is no longer fully determined. You get a "locus" — a set of candidates satisfying one constraint. Do the same for the other constraint. Then look for the intersection. Polya demonstrates this with geometric loci, but the pattern applies everywhere: in number theory (congruences modulo different primes), in combinatorics (independent constraints on a structure), in programming (filtering a list by successive predicates). The move is always the same: separate, explore each part, then recombine.

A subtlety: decomposition can go too far. If you break a condition into too many tiny pieces, you lose sight of how they interact. The graduated principle applies here too — decompose as far as you need to, but no further. The goal is clarity, not atomization.

The question to ask yourself is:

*Separate the various parts of the condition. Can you write them down?*

Writing them down is not pedantry. It is a check on your understanding. If you cannot write the condition in parts, you may not have fully grasped it.

In setting up equations, the same principle applies with particular force. "In easy cases, the verbal statement splits almost automatically into successive parts, each of which can be immediately written down in mathematical symbols. In more difficult cases, the condition has parts which cannot be immediately translated." The understanding-phase work of separating the condition is what makes the translation into equations possible.

## Is the condition possible?

There is another question worth asking early, before you invest effort in solving:

*Is it possible to satisfy the condition?*

*Is the condition sufficient to determine the unknown? Or is it insufficient? Or redundant? Or contradictory?*

You do not need a definitive answer. A guess is enough at this stage. The point is to develop a feel for the problem before diving in.

### Is the problem reasonable?

An important feature of any problem is the number of solutions it admits. Most interesting problems have exactly one solution; you are inclined to consider such problems the only "reasonable" ones. Ask yourself: is your problem, in this sense, reasonable? If you can answer this even by a plausible guess, your interest in the problem increases and you can work better.

For problems to prove, the corresponding question is: *Is it likely that the proposition is true? Or is it more likely that it is false?* The way the question is put shows clearly that only a guess, a plausible provisional answer, is expected. But even a guess focuses your attention.

### An impossibility example

Here is a classic Polya example. *Using each of the ten digits $0, 1, 2, \ldots, 9$ exactly once, write numbers whose sum is $100$.* Before trying to solve this, ask: is it even possible? The digits sum to $0 + 1 + \cdots + 9 = 45$. If $t$ is the sum of the digits that appear in the tens place, then the total sum of the numbers is $10t + (45 - t) = 9t + 45$. For this to equal $100$, we need $t = 55/9$, which is not an integer. The condition is contradictory. No solution exists.

This is a miniature proof — but the question that triggered it was not "prove something." It was the understanding-phase question "is this even possible?" Asking it saved all the effort you would have spent trying combinations. (A reader who knows the procedure of "casting out nines" can see the whole argument at a glance: the sum must be divisible by $9$, and $100$ is not.)

The digit-sum example also illustrates another important point: sometimes the understanding-phase question "is the condition possible?" leads directly to a complete solution — specifically, to a proof of impossibility. You do not always need to reach the devising-a-plan phase. Careful understanding can be the whole solution.

### Insufficiency and redundancy

Not every condition is contradictory. Some are insufficient — they do not pin down a unique answer. "Find a positive integer $n$ such that $n$ is even" has infinitely many solutions. The condition is too weak. Others are redundant — they contain more constraints than necessary. Recognizing redundancy early can simplify your work: you may be able to ignore one clause because the others already imply it.

In well-posed textbook problems, the condition is usually sufficient and consistent. But in problems you pose for yourself — which is increasingly what happens as you advance — the condition may be under-determined, over-determined, or subtly contradictory. Getting in the habit of asking "is this even possible?" and "is the unknown uniquely determined?" protects you against wasted effort in all cases.

### The running example

For our subset problem, the question is simpler: is the unknown well-determined? Given $n$, is there exactly one answer? Yes — the number of subsets of a set depends only on the number of elements, not on what the elements are. The problem is well-posed. This is worth confirming, even if briefly, because it tells you that a single formula in $n$ is what you are looking for — not a case analysis depending on the elements.

## Imitation and practice

"Solving problems is a practical skill like, let us say, swimming. We acquire any practical skill by imitation and practice."

You learn to swim by watching swimmers and then swimming. You learn to solve problems by watching how others solve problems — reading worked solutions deliberately, not passively — and then solving problems yourself.

Polya adds a subtler point about this process. When you study how someone else solved a problem, you should not merely follow the steps. You should dramatize the process to yourself: where was the solver stuck? What question did they ask that unstuck them? What was the decisive idea? This is not about admiring the solution — it is about extracting the *moves* so you can use them yourself.

The questions of the understanding phase are the first moves to practice. They are not a checklist to be completed once and discarded. They are habits of mind — "mental operations typically useful for the solution of problems." When you sit down with a new problem, the first few minutes should be spent making the problem yours: naming the parts, restating in your own words, choosing notation, drawing a picture if one helps, and checking that the condition makes sense. This is not wasted time. It is the foundation on which everything else is built.

Practice these questions on easy problems until they become automatic, and they will serve you on hard ones. If you can ask "What is the unknown?" without thinking about it — if the question arises by reflex whenever you face a new problem — then you have internalized the understanding phase.

The questions we have been discussing proceed from plain common sense. They suggest a conduct which comes naturally to any person who is seriously concerned with a problem. But the person who behaves the right way usually does not bother to express the behavior in clear words. What Polya's list does is express it so — general enough to apply everywhere, specific enough to actually use. "If the reader is sufficiently acquainted with the list and can see, behind the suggestion, the action suggested, he may realize that the list enumerates, indirectly, mental operations typically useful for the solution of problems."

The danger is pedantry. Do not apply these questions mechanically, by rote, in every situation regardless of whether they fit. Use your judgment. The questions are servants, not masters. "Always use your own brains first."

## Questions to keep

- *What is the unknown? What are the data? What is the condition?*
- *Can I restate the problem in my own words?* Could I go back to definitions?
- *Is the condition satisfiable?* Is the unknown determined — too many solutions, too few, or exactly one?
- *Did I understand the problem as a whole before going into detail?*

None of these questions are clever. All of them are useful. Their power is in their generality: they apply to every problem, and they cost nothing but a few minutes of careful thought.
