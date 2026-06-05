# Work Backwards

Start from the end. Ask: *from what antecedent could this result be derived?* Then ask the same question of that antecedent. Keep going until you reach something you already know. Then reverse the whole chain and execute it forwards.

This is the single most important technique for devising a plan. It applies to problems to find and problems to prove alike. If you have a theorem $A$ to prove, ask: what antecedent theorem would imply $A$? Find some $B$ that would do. Then ask what would imply $B$. Continue until you reach something known. Reverse the chain into a forward proof.

The order of invention is the reverse of the order of execution.


## Pappus and the method of analysis

> Pappus of Alexandria (c. 300 AD) described this method, which he called *analysis*: "We start from what is required, we take it for granted, and we draw consequences from it, and consequences from the consequences, till we reach a point that we can use as starting point in synthesis."

Analysis is devising the plan. Synthesis is carrying it out. You work backwards to discover what to do; you work forwards to do it.

Pappus left behind the clearest ancient description of heuristic method. His account of analysis and synthesis, preserved in Book VII of his *Collectiones*, influenced Descartes, Leibniz, and through them the entire modern tradition of problem-solving. Descartes planned a universal method to solve problems; his unfinished *Rules for the Direction of the Mind* contains more interesting material about problem-solving than his better-known *Discours de la Méthode*. "As a young man," Descartes wrote, "when I heard about ingenious inventions, I tried to invent them by myself, even without reading the author. In doing so, I perceived, by degrees, that I was making use of certain rules." Leibniz planned an "Art of Invention" but never carried it through; he wrote: "Nothing is more important than to see the sources of invention which are, in my opinion, more interesting than the inventions themselves."

The restriction of this method to geometry textbooks alone shows a persistent lack of understanding. The method is universal.


## "Assume what is required as already done"

Pappus's instruction sounds like self-deception. It is not. You are not claiming the problem is solved. You are examining the *hypothetical situation* in which the condition is fully satisfied, to discover what must be true in that situation.

Is this legitimate? A judge does not act incorrectly when, questioning a defendant, he considers the hypothesis that the defendant committed the crime — provided he does not commit himself to this hypothesis before the evidence is in. Both the mathematician and the judge may examine a possibility without prejudice, postponing judgment until the examination yields a definite result.

In a "problem to find," to "assume the problem as solved" means to assume there exists an object $x$ satisfying the condition — having the relations to the data which the condition prescribes. This assumption is provisional and harmless. If no such object exists and the analysis leads anywhere, it will lead to a final problem with no solution, making it clear that the original problem has no solution either.

The provisional assumption is what gives you a foothold. Without it, you cannot start the backward chain. The general recommendation: *examine the hypothetical situation in which the condition of the problem is supposed to be fully satisfied.*


## Why turning around is hard

There is a psychological difficulty in going *away* from the goal, in proceeding without looking continually at the aim.

A fence forms three sides of a rectangle, the fourth side open. A dog is placed at point $D$ on one side, food at point $F$ on the other, close to the fence. To reach the food, the dog must first move *away* from it, go around the end, and approach from the open side.

A chimpanzee or a four-year-old child solves this almost instantly. The dog may lose time barking and scratching before conceiving the bright idea of going around. A hen, placed in the same situation, runs back and forth excitedly on her side and may spend considerable time before reaching the food — if she gets there at all.

The hen's difficulty is the difficulty of turning around. It is the same difficulty you face when working backwards. You must accept that the first steps take you *away* from the answer, toward antecedents and preconditions. The dog who scratched and jumped before turning around solved his problem about as well as most of us solve ours.

You should not blame the hen. But recognizing the repugnance to the reverse order helps you overcome it. When you are stuck and keep trying the same direct approach, you are running back and forth on one side of the fence. Working backwards means turning away from the visible goal and asking a different kind of question. It requires deliberate restraint: stop trying to reach the answer directly and instead ask what would have to be true *just before* the answer.


## Example: the water-pouring puzzle

You have two containers: one holds $9$ quarts, the other $4$ quarts. You need exactly $6$ quarts. No markings on the containers.

Working forwards — filling, pouring, guessing — you may stumble on the answer eventually, like the hen running back and forth. But turn around. "Assume what is required as already done." Visualize the desired final situation: the large container holding exactly $6$ quarts, the small container empty.

*From what antecedent could this result be derived?* Fill the large container to $9$ and pour off exactly $3$. To pour off exactly $3$, the small container must already hold exactly $1$ quart (since $4 - 1 = 3$ leaves room for exactly $3$). That is the key idea.

*From what antecedent could you get $1$ quart in the small container?* Fill the large container to $9$, pour $4$ into the small, empty the small, pour $4$ more. The large container now has $9 - 4 - 4 = 1$. You have reached known ground.

Now reverse. The synthesis retraces the analysis:

1. Fill the large container ($9$ quarts).
2. Pour into the small, filling it ($4$ out). Empty the small.
3. Pour again ($4$ out). The large container now has $1$ quart.
4. Pour that $1$ quart into the small container.
5. Fill the large container again ($9$ quarts).
6. Pour into the small until full: it has $1$, so it takes $3$ more. The large container now has $9 - 3 = 6$.

The analysis consisted in thoughts; the synthesis in acts. The finishing act of the synthesis is the first desire from which the analysis started.


## Working backwards in counting

You want to prove that the number of subsets of an $n$-element set is $2^n$. You know the answer you want. Work backwards: what would establish it?

If you could show a bijection between subsets and binary strings of length $n$, you would be done, because there are $2^n$ such strings. So the problem reduces to: construct a bijection between subsets of $\{1, 2, \ldots, n\}$ and elements of $\{0,1\}^n$. That bijection is immediate — a subset corresponds to its characteristic function. Done.

The plan was found by working backwards from the desired conclusion to a sufficient condition, then verifying that condition directly. This is a short chain: goal $\to$ bijection $\to$ characteristic function. In harder counting problems, you might work backwards through several intermediate representations before reaching one you know how to handle.


## Equivalent reductions

Two problems are **equivalent** if the solution of each involves the solution of the other. If your original problem $A$ and your auxiliary problem $B$ are equivalent, the passage from $A$ to $B$ is a *convertible reduction* (or *bilateral reduction*, or *equivalent reduction*).

Convertible reductions are especially clean. You lose nothing by switching from $A$ to $B$, because whatever you learn about $B$ transfers back completely.

### Chains of equivalent problems

You need to solve problem $A$ but cannot see the solution. You find that $A$ is equivalent to $B$. Considering $B$, you find it equivalent to $C$. You continue — $C$ to $D$, and so on — until you reach a problem $L$ whose solution is known or immediate. Each problem being equivalent to the preceding, $L$ is equivalent to $A$. You infer the solution of $A$ from $L$.

This pattern was noticed by the Greek mathematicians, as we see from Pappus. The key property: *every link is convertible*. If even one step is not an equivalent reduction — if you pass from a condition to a narrower or wider one — the chain breaks. You may lose solutions, admit spurious ones, or lose track of the original problem entirely.

### The quartic chain

Starting from:

$$(\text{A}) \quad x^4 - 13x^2 + 36 = 0$$

Complete the square. Multiply by $4$:

$$(\text{B}) \quad (2x^2)^2 - 2(2x^2) \cdot 13 + 144 = 0$$

Add $25$ to both sides:

$$(\text{C}) \quad (2x^2 - 13)^2 = 25$$

$$(\text{D}) \quad 2x^2 - 13 = \pm 5$$

$$(\text{E}) \quad x^2 = \frac{13 \pm 5}{2}$$

$$(\text{F}) \quad x = \pm 3 \text{ or } \pm 2$$

Each reduction is convertible. The last condition is equivalent to the first, so $3, -3, 2, -2$ are *all* solutions. The chain has six links, each preserving the solution set exactly.

The discipline of checking convertibility at each step is the discipline of keeping track of what you have actually proved.

### Pappus's proviso

Pappus's method works cleanly only when each step is reversible. Modern paraphrases include the phrase "provided that all our derivations are convertible." But this phrase is an interpolation — Pappus's *original text* contains nothing of the sort.

The absence is significant. Without the convertibility proviso, the method can appear to prove things that are not true. You derive $B$ from $A$, then $C$ from $B$, until you reach $L$, which you find to be true. You claim $A$ is true. But if any step was a one-way implication, the truth of $L$ says nothing about $A$. You have shown that $A$ implies $L$, not that $L$ implies $A$.

Check the direction of each implication. Every step backwards must be a step you can later reverse forwards. The entire edifice of analysis-and-synthesis rests on this.


## Questions to keep

- *From what antecedent could this result be derived?* Can I work backwards from the goal to known ground?
- *Is each step in my chain convertible?* If I reverse the analysis into a synthesis, does every link hold in both directions?
- *Am I running back and forth on one side of the fence?* Would turning around — moving temporarily away from the goal — open a path?
- *Have I assumed the problem as solved?* What does the hypothetical solution look like, and what must be true just before it?
