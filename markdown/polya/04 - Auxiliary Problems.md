# Auxiliary Problems

You have understood the problem. You have tried the direct attack: look at the unknown, recall a related problem, vary the conditions. Nothing has worked. The problem sits there, unmoved.

Now what?

You solve a different problem. Not because you have given up, but because the obstacle in front of you cannot be overcome directly. An insect tries to escape through the windowpane, tries the same again and again, and does not try the next window which is open. Human superiority over the insect consists precisely in this: the ability to go around. To devise a suitable auxiliary problem when the original one appears insoluble --- to raise a clear-cut new problem subservient to another problem, to conceive distinctly as an end what is means to another end --- is a refined achievement of the intelligence. It is an important task to learn how to handle auxiliary problems intelligently.

This chapter is about the indirect route. Auxiliary problems, auxiliary elements, auxiliary unknowns, equivalent reductions, and working backwards. These are not fallback tactics. They are often the main line of attack. In many problems --- perhaps most problems worth solving --- the indirect route *is* the route. The direct attack clears the easy problems; the ones that remain are precisely those that require a detour.


## Why auxiliary problems help

An auxiliary problem is a problem you consider not for its own sake but because you hope its consideration will help you solve another problem --- your original problem. The original problem is the end; the auxiliary problem is a means.

Why does this work? Because problems are connected. A problem that shares your unknown, or your data, or part of your condition, may have a solution you can transfer. But the transfer can take different forms, and the distinction matters.

### Result, method, or both

When you profit from an auxiliary problem, you may use its **result**, its **method**, or **both**. These are genuinely different situations.

*Using the result.* You solve the auxiliary problem, get an answer, and plug that answer into the original problem. The quartic equation $x^4 - 13x^2 + 36 = 0$ reduces to a quadratic $y^2 - 13y + 36 = 0$ via $y = x^2$. You solve the quadratic, get $y = 4$ or $y = 9$, and feed those values back to find $x$. You used the result of the auxiliary problem. You did not care how the quadratic was solved --- any method would do.

*Using the method.* You solve a simpler analogous problem and imitate its approach on the original. You count the subsets of a $3$-element set to understand the pattern, then apply the same binary-string encoding to the $n$-element case. What you carried over was the method --- the encoding idea --- not any particular numerical answer.

*Using both.* Sometimes you are lucky enough to use both the result and the method of the auxiliary problem. You count $2$-element subsets by a method that generalizes, and the base-case answer also feeds into an inductive argument. When both transfer, the auxiliary problem has paid double.

Knowing which kind of profit you seek sharpens your choice. If you need only a result, any route to that result works --- you do not care how the auxiliary problem was solved, only what answer it gave. If you need a method, the auxiliary problem should be structurally similar to the original, not just numerically related --- because what you intend to transfer is the approach, the pattern of reasoning, not a particular number.

Sometimes, examining the solution of the auxiliary problem, you find that you cannot immediately use it for the original. Then it may be worth reconsidering the solution, varying and modifying it, trying various forms until you find one that extends to the original problem. The first form of the solution is not always the most useful form.

### Inventing versus remembering

There is an important difference between *remembering* a related problem you have solved before and *inventing* a new auxiliary problem from scratch. The question "Do you know a related problem?" asks you to search memory. But "Could you imagine a more accessible related problem?" asks you to create something new. You should try remembering first --- it is cheaper. But when memory fails, you must invent, and invention requires a different kind of effort: you must vary the problem deliberately until something more tractable appears.

### Concrete moves

1. **Solve a simpler version.** Drop a constraint, shrink the domain, reduce the number of variables. If you cannot count the subsets of an $n$-element set that satisfy a complex property, count the subsets of a $3$-element set first.

2. **Solve an analogous problem.** If your problem is about graphs, is there a simpler problem about sequences that has the same structure? If your problem is three-dimensional, what happens in two dimensions?

3. **Solve a more general problem.** This sounds backwards, but a more general problem may be easier because it reveals the essential structure. This is the inventor's paradox, and it is real.

4. **Solve a stepping-stone problem.** You cannot reach the far bank in one leap. A stone in the middle of the creek is nearer to you than the other bank --- and when the stone is reached, it helps you on toward the other bank. Find an intermediate result that is both accessible from your data and useful toward your unknown. Not merely accessible, and not merely related to the goal, but both at once.

5. **Change the unknown.** If you cannot find $x$ directly, find some $y$ that is related to $x$ and easier to obtain from the data. Then use $y$ to get $x$.

### The risk

Every auxiliary problem costs time and effort. If it fails, that investment is lost. You should exercise judgment in choosing one. A good auxiliary problem may appear more accessible than the original; or it may appear instructive; or it may have some sort of aesthetic appeal. Sometimes the only advantage of the auxiliary problem is that it is new and offers unexplored possibilities --- you choose it because you are tired of the original problem, all approaches to which seem exhausted.

But you should have *some* reason for your choice. Do not wander into auxiliary problems wantonly. There is no infallible method of discovering suitable auxiliary problems, just as there is no infallible method of discovering the solution itself. But there are questions and suggestions which are frequently helpful --- *look at the unknown*, *vary the problem*, *could you imagine a more accessible related problem?* --- and these questions often lead to useful auxiliary problems naturally.


## Auxiliary elements

As your work progresses, you add new elements to those originally considered. An element that you introduce in the hope that it will further the solution is called an *auxiliary element*.

In a graph problem, you might introduce a new vertex, a new edge, or a partition. In a counting problem, you might introduce a new variable or a new representation --- a generating function, a bijection, or a binary encoding. In an equation, you might introduce a substitution. In a combinatorial argument, you might introduce an ordering or a coloring. The principle is the same: you enrich the problem's structure to create a foothold that was not there before. There is much more in your conception of the problem at the end of the work than was in it at the start; auxiliary elements are how the conception grows.

### Four reasons to introduce them

There are several reasons to introduce auxiliary elements, and it helps to be conscious of which reason is driving you.

**To use a known result.** You have recalled a theorem or a previously solved problem that seems relevant. But it does not quite apply --- your problem is missing a piece that the theorem needs. You introduce that piece as an auxiliary element to bridge the gap. In a graph problem, you might need a particular partition to apply a known coloring theorem, so you construct that partition.

**To unpack a definition.** You have a term in your problem whose definition involves objects not yet present in your working representation. Going back to the definition and introducing those objects can unlock the problem. Stating a definition without drawing something from it is mere lip-service. If the problem mentions "connected graph" but you have not introduced any paths, you have not yet used the definition of connectedness.

**To make the problem fuller.** You may feel that adding a certain element makes the problem more suggestive, more familiar, even though you cannot yet say how. It is "a bright idea" to conceive the problem with such-and-such elements added, though you can barely articulate why. That instinct is worth following --- but you should have *some* reason. Do not introduce auxiliary elements wantonly.

**To create symmetry or simplicity.** Sometimes the problem as stated is lopsided. You introduce an element to restore a symmetry that the statement obscured, or to bring in a particularly simple and familiar structure. In a counting problem, you might introduce a complementary set; in a graph problem, an auxiliary vertex that regularizes the structure.

### The rabbit-from-a-hat problem

> "The intelligent student and the intelligent reader are not satisfied by verifying that the steps of a reasoning are correct but also want to know the motive and the purpose of the various steps."

If a tricky auxiliary element appears abruptly, without any motivation, and solves the problem surprisingly, you feel cheated. Mathematics is interesting insofar as it occupies your reasoning and inventive powers. But there is nothing to learn about reasoning and invention if the motive and purpose of the most conspicuous step remain incomprehensible. The introduction of an auxiliary element should be *motivated* --- by a known result you want to apply, by a definition you want to unpack, or by an analogy you want to pursue. When you read a proof where an auxiliary element appears from nowhere and works by magic, ask yourself: what would have led me to introduce it? If you cannot answer that, the proof has taught you a fact but not a method.

### Example: counting subsets by substitution

You want to count the number of subsets of $\{1, 2, \ldots, n\}$ whose elements sum to an even number. Call this $E(n)$.

Direct attack: enumerate and classify. This works for small $n$ but gives no formula. You are stuck.

Introduce an auxiliary representation. Encode each subset as a binary string $b_1 b_2 \cdots b_n$ where $b_i = 1$ means element $i$ is included. The sum of the subset is $\sum_{i=1}^{n} i \cdot b_i$. You want this sum to be even.

Now introduce an auxiliary unknown. Let $O(n)$ be the number of subsets whose elements sum to an odd number. You know $E(n) + O(n) = 2^n$ (every subset sums to something). If you can find the relationship between $E(n)$ and $O(n)$, you are done.

Consider what happens when you toggle the bit $b_1$ (include or exclude element $1$). This changes the sum by $1$, flipping its parity. So toggling $b_1$ is a bijection between even-sum subsets and odd-sum subsets. Therefore $E(n) = O(n) = 2^{n-1}$.

The auxiliary unknown $O(n)$ and the auxiliary element (the toggle bijection) did the work. Neither was in the original problem statement. You introduced them because they made a known technique --- bijection --- applicable. The motivation is clear: you wanted to use a bijection, so you needed two sets to biject between. That led you to introduce $O(n)$.

A quick sanity check: for $n = 3$, the subsets are $\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}$ with sums $0, 1, 2, 3, 3, 4, 5, 6$. Even sums: $0, 2, 4, 6$ --- that is $4 = 2^2$. Correct.


## Auxiliary unknowns and lemmas

An **auxiliary unknown** is a new unknown that you introduce to serve as a stepping stone. You do not care about its value for its own sake; you care because finding it brings you closer to the original unknown. The new unknown should be both *accessible* (easier to obtain from the data than the original unknown) and *useful* (capable of rendering definite service in the search for the original unknown). In practice, you must often settle for less --- an unknown that seems accessible even if you cannot yet see how it will help, or one that would clearly help if only you could find it.

Consider the equation:

$$x^4 - 13x^2 + 36 = 0.$$

If you observe that $x^4 = (x^2)^2$, you may introduce $y = x^2$. The equation becomes $y^2 - 13y + 36 = 0$, which is a quadratic you can solve. The auxiliary unknown $y$ made a hard problem routine.

A **lemma** is an auxiliary theorem --- a theorem you prove not for its own sake but because it helps you prove the theorem you actually care about. The word is Greek; a more literal translation would be "what is assumed." You suspect that if theorem $B$ were true, you could use it to prove theorem $A$. So you assume $B$ provisionally, work out whether it helps, and then go back and prove $B$.

Lemmas are everywhere in mathematics. The habit of carving out a useful sub-result, proving it cleanly, and then deploying it, is one of the most important skills a solver can develop. A good lemma, like a good stepping stone, is both within reach and load-bearing.

Note the pattern: auxiliary unknowns serve "problems to find" the way lemmas serve "problems to prove." In both cases, you introduce a subsidiary goal that you care about only because it advances the original goal. And in both cases, the subsidiary goal should be *motivated* --- you should be able to say why you expect it to help, even if only tentatively.

The choice of auxiliary unknown matters. If you introduce $y$ and it turns out to have no clear relation to $x$, you have created a stepping stone that does not bridge the creek. The ideal auxiliary unknown is one that is both closer to the data (easier to compute) and visibly connected to the original unknown (useful once found). In the quartic example, $y = x^2$ satisfies both criteria: it simplifies the equation (accessible) and it immediately yields $x$ once known (useful).


## Equivalent reductions

Two problems are **equivalent** if the solution of each involves the solution of the other. If your original problem $A$ and your auxiliary problem $B$ are equivalent, the passage from $A$ to $B$ is called a *convertible reduction* (or *bilateral reduction*, or *equivalent reduction*).

Convertible reductions are especially clean. You lose nothing by switching from $A$ to $B$, because whatever you learn about $B$ transfers back to $A$ completely.

### Chains of equivalent problems

Chains of equivalent auxiliary problems are frequent in mathematical reasoning and deserve a general description. You are required to solve problem $A$; you cannot see the solution, but you find that $A$ is equivalent to another problem $B$. Considering $B$ you may run into a third problem $C$ equivalent to $B$. Proceeding in the same way, you reduce $C$ to $D$, and so on, until you come upon a last problem $L$ whose solution is known or immediate. Each problem being equivalent to the preceding, the last problem $L$ must be equivalent to your original problem $A$. Thus you infer the solution of $A$ from the problem $L$ which you attained as the last link in a chain.

This pattern was noticed by the Greek mathematicians, as we may see from an important passage of Pappus. The key property of the chain is that *every link is convertible*. If even one step in the chain is not an equivalent reduction --- if you pass from a proposed condition to a narrower one, or to a wider one --- the chain breaks. You may lose solutions, or admit spurious ones, or lose track of the original problem entirely.

### The quartic chain

The quartic equation illustrates a chain of equivalent conditions in full. Starting from:

$$(\text{A}) \quad x^4 - 13x^2 + 36 = 0$$

one way to solve it is to complete the square. Multiply through by $4$:

$$(\text{B}) \quad (2x^2)^2 - 2(2x^2) \cdot 13 + 144 = 0$$

Add $25$ to both sides to complete the square:

$$(\text{C}) \quad (2x^2)^2 - 2(2x^2) \cdot 13 + 169 = 25$$

$$(\text{D}) \quad (2x^2 - 13)^2 = 25$$

$$(\text{E}) \quad 2x^2 - 13 = \pm 5$$

$$(\text{F}) \quad x^2 = \frac{13 \pm 5}{2}$$

$$(\text{G}) \quad x = \pm\sqrt{\frac{13 \pm 5}{2}}$$

$$(\text{H}) \quad x = 3, \text{ or } {-3}, \text{ or } 2, \text{ or } {-2}$$

Each reduction is convertible. The last condition $(\text{H})$ is equivalent to the first $(\text{A})$, so $3, -3, 2, -2$ are *all* possible solutions of the original equation. The chain has eight links, each preserving the solution set exactly.

The point deserves the greatest care. If in a series of successive reductions you pass to a narrower condition and then to a wider one, you may lose track of the original problem completely. Check carefully the nature of each newly introduced condition: *Is it equivalent to the original condition?*

### Unilateral reductions

Not all reductions are convertible. If you have two problems $A$ and $B$, both unsolved, and solving $A$ would give you $B$ but not vice versa, then $A$ is the *more ambitious* problem and $B$ the *less ambitious*. Reducing to a less ambitious problem --- passing from the hard problem to an easier one --- is the natural move. It can work: the less ambitious problem may serve as a stepping stone, and its solution, combined with some supplementary remark, may yield the original. But you are not guaranteed a way back. The risk is that you solve the easier problem and then discover it was not enough.

Reducing to a *more* ambitious problem sounds perverse but can also succeed. A more ambitious problem may be more accessible because it is more general, with more structure to exploit. This is the inventor's paradox again. But the risk here is different: the more ambitious problem, being stronger, may be genuinely harder, and you have wandered further from your goal.

Both kinds of unilateral reduction are more risky than a bilateral one. When you make a non-convertible step, note it explicitly and check later whether you can get back.

### When to reach for equivalent reductions

Equivalent reductions are especially valuable when you face a problem whose condition is stated in an unfamiliar or complicated form. The strategy is: transform the condition, step by equivalent step, until it reaches a form you recognize. Each step must be convertible so that the final, recognizable form is genuinely equivalent to the original. The completed chain is then both a solution and a proof of completeness --- you have found *all* solutions, not just some.

This is why the quartic chain above is instructive beyond its algebraic content. The discipline of checking convertibility at each step is the discipline of keeping track of what you have actually proved. Skip that check, and you may end with a narrower condition (missing solutions) or a wider one (admitting spurious ones) without realizing it.


## Working backwards and Pappus

Working backwards is the most important single technique for devising a plan. Its core idea is simple: start from the desired end and ask, *from what antecedent could this result be derived?* Then ask the same question of that antecedent. Keep going until you reach something you already know how to do. Then reverse the whole chain and execute it forwards.

The pattern applies to "problems to prove" as well as "problems to find." If you have a theorem $A$ to prove, you ask: from what antecedent theorem could $A$ be derived? You find some $B$ that would imply $A$. Then you ask what would imply $B$, and so on, until you reach something known. Then you reverse the chain into a forward proof: from the known thing, prove $B$; from $B$, prove $A$.

### Pappus's description

> Pappus of Alexandria (c. 300 AD) described this method, which he called *analysis*: "We start from what is required, we take it for granted, and we draw consequences from it, and consequences from the consequences, till we reach a point that we can use as starting point in synthesis."

Analysis is devising the plan. Synthesis is carrying it out. The order of invention is the reverse of the order of execution. This is not just a technique for mathematics --- it applies whenever you can work backwards from a goal to known ground.

### Why turning around is hard

There is a certain psychological difficulty in working backwards --- in going *away* from the goal, in proceeding without looking continually at the aim. A famous experiment in animal psychology illustrates this vividly.

A fence forms three sides of a rectangle, leaving the fourth side open. A dog is placed at a point $D$ on one side of the fence, and food is placed at a point $F$ on the other side, close to the fence. The dog's problem is to reach the food. To do so, it must first move *away* from the food, go around the end of the fence, and approach from the open side.

A chimpanzee or a four-year-old child solves this almost instantly. The dog may lose some time barking and scratching at the fence before conceiving the "bright idea" of going around. But a hen, placed in the same situation, runs back and forth excitedly on her side of the fence and may spend considerable time before reaching the food --- if she gets there at all.

The hen's difficulty is the difficulty of turning around, of moving away from the visible goal. It is the same difficulty you face when working backwards. You must accept that the first steps of the plan take you *away* from the answer, toward antecedents and preconditions. The dog who scratched and jumped before turning around solved his problem about as well as most of us solve ours. The dog who, after brief inspection, turned and dashed off gives --- rightly or wrongly --- the impression of superior insight.

You should not blame the hen. Going around an obstacle is what you do in solving any kind of problem, and the psychological repugnance to the reverse order is real. But recognizing it helps you overcome it.

The analogy between the hen's predicament and yours is not superficial. When you are stuck on a problem and keep trying the same direct approach, you are running back and forth on one side of the fence. The food is visible --- you can *see* the answer you want, or at least you can see the form it should take --- but the direct path is blocked. Working backwards means turning away from the visible goal and asking a different kind of question. It requires a moment of deliberate restraint: stop trying to reach the answer directly, and instead ask what would have to be true *just before* the answer.

### A non-mathematical illustration

A primitive man wishes to cross a creek; but he cannot do so in the usual way because the water has risen overnight. The crossing is his problem. Working backwards: from what antecedent could he reach the other bank? If there were something to walk across on. From what antecedent could there be something to walk across on? If a tree lay across the creek. From what antecedent could a tree fall across the creek? If he could make a tree fall.

This train of ideas is analysis in Pappus's sense. If the primitive man finishes his analysis, he may become the inventor of the bridge and the axe. The synthesis --- the actual execution --- reverses the order: first fell the tree, then walk across. The finishing act of the synthesis is the first desire from which the analysis started.

### Example: the water-pouring puzzle

You have two containers: one holds $9$ quarts, the other $4$ quarts. You need exactly $6$ quarts. No markings on the containers.

Imagine the two empty cylindrical containers side by side. If there were a scale of equally spaced horizontal lines on each, the problem would be trivial. But there is no such scale, and so you are far from the solution.

Working forwards --- filling, pouring, guessing --- you may stumble on the answer eventually, like the hen running back and forth on her side of the fence. You fill the large container, pour some into the small one, empty, pour again. You are trying this and that, and when you do not succeed, you start again. Most people who attempt this puzzle work this way and may succeed, after many trials, accidentally.

But turn around. Start from the goal. "Assume what is required as already done," says Pappus. Visualize the desired final situation: the large container holding exactly $6$ quarts, the small container empty.

*From what antecedent could this result be derived?* You could fill the large container to its full $9$ quarts and pour off exactly $3$. To pour off exactly $3$, the small container must already hold exactly $1$ quart (since it holds $4$, and $4 - 1 = 3$ leaves room for exactly $3$). That is the key idea. Few people find it without hesitation; recognizing its significance, you can foresee an outline of the full solution.

*From what antecedent could you get $1$ quart in the small container?* If the large container had $1$ quart, you could pour it into the small one. *From what antecedent could the large container have $1$ quart?* Fill it to $9$, pour $4$ into the small container, empty the small container, pour $4$ more. Now the large container has $9 - 4 - 4 = 1$ quart. You have reached known ground --- "something already known," in Pappus's words.

Now reverse the process. The synthesis retraces the steps of the analysis:

1. Fill the large container ($9$ quarts).
2. Pour into the small container, filling it ($4$ quarts out). Empty the small container.
3. Pour again into the small container ($4$ quarts out). The large container now has $1$ quart.
4. Pour that $1$ quart into the small container.
5. Fill the large container again ($9$ quarts).
6. Pour into the small container until full: it already has $1$ quart, so it takes $3$ more. The large container now has $9 - 3 = 6$ quarts.

The same objects fill the analysis and the synthesis. The analysis consists in thoughts, the synthesis in acts. Walking across the creek (or measuring six quarts) is the first desire from which the analysis starts and the last act with which the synthesis ends. The order is reversed throughout.

### Working backwards in counting

You want to prove that the number of subsets of an $n$-element set is $2^n$. You know the answer you want. Work backwards: what would establish it?

If you could show a bijection between subsets and binary strings of length $n$, you would be done, because there are $2^n$ such strings. So the auxiliary problem becomes: construct a bijection between subsets of $\{1, 2, \ldots, n\}$ and elements of $\{0,1\}^n$. That bijection is immediate: a subset corresponds to its characteristic function. Done.

The plan was found by working backwards from the desired conclusion to a sufficient condition (the bijection), and then verifying that sufficient condition directly. Notice that this is a short chain: goal $\to$ bijection $\to$ characteristic function. But the same pattern applies to longer chains. In a harder counting problem, you might work backwards through several intermediate representations before reaching one you know how to handle.

### "Assume what is required as already done"

Pappus's curious instruction --- "assume what is required to be done as already done, what is sought as already found" --- sounds like self-deception. But it is not. You are not claiming the problem is solved. You are examining the *hypothetical situation* in which the condition of the problem is fully satisfied, in order to discover what must be true in that situation.

Is this legitimate? Consider: a judge does not act incorrectly when, questioning a defendant, he considers the hypothesis that the defendant committed the crime --- provided he does not commit himself to this hypothesis before the evidence is in. Both the mathematician and the judge may examine a possibility without prejudice, postponing their judgment until the examination yields some definite result.

In a "problem to find," to "assume the problem as solved" means to assume that there exists an object $x$ satisfying the condition --- having those relations to the data which the condition prescribes. This assumption is provisional and harmless. If there is no such object and the analysis leads anywhere, it is bound to lead to a final problem with no solution, and so it will become manifest that the original problem has no solution either. The assumption is also *natural*. The primitive man imagines himself walking on a fallen tree and crossing the creek long before he can actually do so; he sees his problem "as solved."

This provisional assumption is what lets you start the backward chain. Without it, you have no foothold. The general recommendation is: *examine the hypothetical situation in which the condition of the problem is supposed to be fully satisfied*. This applies not only to geometric constructions (where it originated) but to any "problem to find."

### Pappus's proviso and convertibility

Pappus's method works cleanly only when each step is reversible. If you derive consequence $B$ from your goal $A$, and then $C$ from $B$, you need each derivation to be convertible in order to reverse the chain into a valid proof.

Modern paraphrases of Pappus include the critical phrase "provided that all our derivations are convertible." But this phrase is an interpolation --- Pappus's *original text* contains nothing of the sort. This omission was observed and criticized in modern times. The absence is significant: without the convertibility proviso, the method can appear to prove things that are not true. You derive $B$ from $A$, then $C$ from $B$, and so on until you reach $L$, which you find to be true. You claim $A$ is true. But if any step in the chain from $A$ to $L$ was not convertible --- if it was a one-way implication --- then the truth of $L$ says nothing about $A$. You have shown that $A$ implies $L$, not that $L$ implies $A$.

This is the same warning as with equivalent reductions: check the direction of each implication. Every step backwards must be a step you can later reverse forwards. The entire edifice of analysis-and-synthesis rests on this.

> Pappus of Alexandria left behind the clearest ancient description of heuristic method. His account of analysis and synthesis, preserved in Book VII of his *Collectiones*, influenced Descartes, Leibniz, and through them the entire modern tradition of problem-solving. Descartes planned to give a universal method to solve problems; his unfinished *Rules for the Direction of the Mind* contains more interesting material about problem-solving than his better-known *Discours de la Méthode*. "As a young man," Descartes wrote, "when I heard about ingenious inventions, I tried to invent them by myself, even without reading the author. In doing so, I perceived, by degrees, that I was making use of certain rules." Leibniz planned an "Art of Invention" but never carried it through; he wrote: "Nothing is more important than to see the sources of invention which are, in my opinion, more interesting than the inventions themselves." The method Pappus described is not specifically geometric; it applies whenever you can work backwards from a goal to known ground. Almost every elementary textbook of geometry contains a few remarks about analysis and synthesis. There is little doubt that this nearly ineradicable tradition goes back to Pappus, although hardly any current textbook whose writer shows direct acquaintance with Pappus. The restriction of the method to geometry textbooks alone shows a persistent lack of understanding; the method is universal.



## When the detour is worth it

Every auxiliary problem is a detour. You leave the main road to explore a side path, hoping it reconnects. When is this justified?

**When the direct attack has genuinely stalled.** If you have tried looking at the unknown, recalling related problems, and varying the conditions, and nothing has worked, then you need a new problem to work on. An auxiliary problem gives you that. The key word is *genuinely*. Do not reach for an auxiliary problem as a first move; it is a move for after the direct approaches have been tried and have failed. But once they have failed, do not keep beating against the same windowpane.

**When the auxiliary problem is visibly more accessible.** If you can see that the auxiliary problem is simpler --- fewer variables, weaker conditions, a pattern you recognize --- the detour is likely short.

**When the auxiliary problem is more instructive.** Even if it does not solve your original problem directly, it may teach you a method or reveal a structure that you can use later. Solving the analogous problem in two dimensions before tackling three is a classic example. Here you are seeking the *method*, not the result.

**When you are tired of the original problem.** This is a real reason. Determination fluctuates with hope and hopelessness. It is easy to keep going when you think the solution is just around the corner; it is hard to persevere when you see no way out. Sometimes the only advantage of the auxiliary problem is that it is new. A new problem reconquers interest, and with interest comes progress. "If you cannot solve the proposed problem, try to solve first some related problem" --- this is advice about morale as much as method. You do not despise little successes; on the contrary, you seek them. Freshness restores attention; a small advance restores hope; and hope sustains determination.

**When the auxiliary problem is more general.** The inventor's paradox: a more general problem sometimes has more structure to exploit, more symmetry to leverage, more room to maneuver. If you cannot prove that a specific graph invariant holds for bipartite graphs, try proving it for all graphs. The stronger statement may be easier because it does not require you to use the bipartite condition, which was a distraction.

**When the auxiliary problem teaches you something regardless.** Even if the detour does not solve your original problem, it may teach you something worth knowing. You attempted an auxiliary problem, it did not lead back to the original, but in working on it you learned a technique, noticed a pattern, or discovered a connection that will serve you on some future problem. Not all detours are wasted even when they fail to reconnect. The question is whether you learned a method, not just whether you got a result.

**When it is not worth it.** When you have no reason to believe the detour leads back. When you are exploring for the sake of exploring, without even a vague plan to reconnect. When the auxiliary problem is harder than the original. When you have already tried three auxiliary problems and none have panned out --- at that point, you may need to reconsider whether you understood the original problem correctly, rather than casting about for yet another detour. Exercise judgment. You should have *some* reason for your choice.

> Bolzano wrote of heuristic: "I do not think at all that I am able to present here any procedure of investigation that was not perceived long ago by all men of talent; and I do not promise at all that you can find here anything quite new of this kind. But I shall take pains to state in clear words the rules and ways of investigation which are followed by all able men, who in most cases are not even conscious of following them." This humility is appropriate. The moves described in this chapter are not secrets. They are what good problem-solvers do, often without knowing they are doing it. The value of naming them is that you can reach for them deliberately when you are stuck.


## Summary: the indirect route

The moves in this chapter share a common structure. You cannot solve the problem directly, so you solve a different problem --- one that is related to the original but more accessible, more instructive, or at least fresh. The auxiliary problem may be simpler (drop a constraint), analogous (change the domain), more general (the inventor's paradox), or a stepping stone (an intermediate result). You may introduce auxiliary elements to enrich the problem, auxiliary unknowns to create stepping stones, or lemmas to prove sub-results. You may chain equivalent reductions to transform the problem step by step into a recognizable form. You may work backwards from the goal to discover what must precede it.

All of these are forms of going around. The insect beats against the glass; the solver finds the open window. The difference is not intelligence in some abstract sense but the willingness to turn away from the direct path and seek a better one. And behind all these moves is a single habit of mind: when the direct path is blocked, ask a different question.

The moves are not secrets. They are what good problem-solvers do, often without knowing they are doing it. The value of naming them is that you can reach for them deliberately when you are stuck, rather than waiting for inspiration to arrive on its own.


## Questions to keep

- *Could I solve a simpler related problem first?* What would I simplify — the data, the condition, the domain?
- *What kind of profit do I expect from the detour?* The result, the method, or both?
- *Can I work backwards?* From what antecedent could the desired result be derived?
- *Is my reduction equivalent?* If I switch to this new problem, can I get back to the original?
