# Variation

When the direct attack stalls, change the problem. Not randomly -- deliberately. You keep some parts fixed and alter others. You weaken a condition, specialize a variable, push a parameter to an extreme. The altered problem is not your problem, but solving it may teach you how to solve yours.

This is not a fallback tactic. Variation is the central engine of problem-solving. As Polya puts it: trying to solve a problem, we consider different aspects of it in turn, we roll it over and over in our mind. Success depends on choosing the right aspect, on attacking the fortress from its accessible side. To find out which side is accessible, we try various sides -- we vary the problem.

An insect tries to escape through the windowpane, tries the same hopeless thing again and again, and does not try the next window which is open. A mouse does better: caught in a trap, it tries to squeeze through between two bars, then between the next two bars, then between other bars. It varies its trials. You should vary yours more intelligently still. "Try, try again" is good advice -- but only if each trial is different from the last.

This chapter catalogs the main ways to vary a problem: dropping conditions, specializing, generalizing, changing the unknown, pushing to extremes. It also explains *why* variation works -- not just as a logical strategy but as a way to keep your mind engaged when progress stalls.


## Why variation works

Variation is not just a technique -- it is how your mind stays engaged with a problem. Polya explains the psychology clearly: progress in solving a problem appears as mobilization and organization of formerly acquired knowledge. You have to extract from memory and work into the problem certain elements. Variation helps because of how memory works.

You remember things by a kind of "action by contact" -- mental association. What you have in mind now tends to recall what was connected with it at some previous occasion. Varying the problem, you bring in new points, and so you create new contacts, new possibilities of contacting elements relevant to your problem.

There is a second reason, equally important: attention cannot survive stagnation. You cannot hope to solve any worthwhile problem without intense concentration, but you are easily tired by intense concentration upon the same point. In order to keep attention alive, the object on which it is directed must unceasingly change. If your work progresses, there is something to do, new points to examine, and your interest stays alive. But if you fail to make progress, your attention falters, your interest fades, your thoughts begin to wander, and there is danger of losing the problem altogether. To escape from this danger you have to set yourself a new question about the problem.

The new question unfolds untried possibilities of contact with your previous knowledge. It revives your hope of making useful contacts. It reconquers your interest by varying the problem, by showing some new aspect of it.

This is why Polya opens his advice on variation with consolation: if you cannot solve the proposed problem, do not let this failure afflict you too much but try to find consolation with some easier success. Try to solve first some related problem; then you may find courage to attack your original problem again. Variation is psychological rescue as much as it is logical strategy. Human superiority consists in going around an obstacle that cannot be overcome directly, in devising some suitable auxiliary problem when the original one appears insoluble.

The practical implication: when you feel stuck, the worst thing you can do is keep staring at the same formulation. Change something. Set a parameter to a specific value. Drop a constraint. Restate the condition. Even if the new problem does not solve the old one, the act of varying restores your engagement. The new question may reconquer your interest by showing some new aspect of the problem. And from that renewed engagement, the decisive idea may come.


## Change the problem deliberately

You have a problem. You have looked at the unknown, recalled related problems, tried what came to mind. Nothing worked. Now what?

The remaining questions in the list that starts with "If you cannot solve the proposed problem" have a common aim: the variation of the problem. There are different means to attain this aim -- generalization, specialization, analogy, and others which are various ways of decomposing and recombining. The rest of this chapter is a catalog of these means.

Now you change the problem on purpose. You construct a new problem from the old one -- a problem that is easier, or more familiar, or that illuminates some part of the original that you could not see before. The new problem is an *auxiliary problem*: you consider it not for its own sake but because its solution may help you solve the original.

There is a formal way to think about this. Your problem has three principal parts: the unknown, the data, and the condition. When you construct a new problem, you can:

1. **Keep the unknown and change the rest** (the data and the condition).
2. **Keep the data and change the rest** (the unknown and the condition).
3. **Change both the unknown and the data.**

Each of these is a different style of variation, and each has its uses. The first two are safer -- you stay closer to the original problem. The third is more radical, and you reach for it when the gentler variations have failed.

There is a subtlety worth noting: these cases overlap. It is possible to keep both the unknown and the data, and transform the problem by changing only the *form* of the condition. Two problems can be equivalent -- solving one immediately solves the other -- and yet differ in the way the condition is stated. Sometimes restating the condition, without changing what it demands, is itself the decisive variation. "Construct an equilateral triangle, being given a side" and "Construct an equiangular triangle, being given a side" are visibly equivalent, but the shift in perspective from sides to angles can be momentous in harder problems.


## Drop part of the condition

The single most useful variation: keep the unknown, keep the data, but weaken the condition. Drop a clause. Remove a constraint. See what happens.

When you weaken the condition, you restrict the unknown less. More objects satisfy it. Ask yourself: *How far is the unknown now determined? How can it vary?*

**Example.** You want to count the number of subsets of an $n$-element set $S$ that have exactly $k$ elements. The condition has two parts:

(I) The subset must be drawn from $S$.

(II) The subset must have exactly $k$ elements.

Drop part (II). Now you are counting *all* subsets of $S$, with no size restriction. That is a problem you know how to solve: each element is either in or out, giving $2^n$ subsets. This is useful. You now understand the space of possibilities -- $2^n$ subsets total -- and your original question asks how many of them satisfy the additional constraint of having size exactly $k$.

Drop part (I) instead -- or rather, specialize it. Fix $n = 3$, $k = 2$, and list every subset of size 2: $\{a,b\}$, $\{a,c\}$, $\{b,c\}$. There are 3. Fix $n = 4$, $k = 2$: there are 6. The numbers $1, 3, 6, 10, \ldots$ are appearing. You recognize triangular numbers. You are building toward $\binom{n}{k}$ by working with the weakened problem.

**Example.** In a crossword puzzle with the clue "Forward and backward part of a machine (5 letters)," the condition has two parts:

(I) The word means some part of some machine.

(II) The word has 5 letters and reads the same forward and backward.

Keep only part (I). List words: lever, screw, wheel, shaft, hinge, motor. Now test each against part (II). "Rotor" -- of course.

The pattern: separate the condition into parts. Keep one part, drop the other. Explore the space of objects satisfying the weaker condition. Then check which of those objects also satisfy the dropped part. The two partial conditions function like two loci whose intersection is the answer.

This locus-intersection pattern is remarkably general. In geometry, the "loci" are literal curves or surfaces. In combinatorics, they are sets of objects satisfying partial constraints. In a crossword puzzle, they are lists of words matching partial clues. The underlying logic is always the same: the full condition is too tight to satisfy directly, so you relax it into two weaker conditions, explore each one separately, and look for the overlap. Polya calls this decomposing and recombining, and it is one of the most broadly applicable moves in the entire method.

The trick is choosing which part of the condition to drop first. A good heuristic: drop the part that seems hardest to satisfy, and keep the part whose solutions you can enumerate or describe. This gives you a concrete list of candidates to test against the dropped part.

**When to reach for it.** Whenever the full condition feels too tight to work with. Whenever you cannot see the unknown at all under all the constraints. Loosen the grip; see what moves.


## Keep the unknown and change the rest

Looking at the unknown is one of the oldest pieces of advice in problem-solving. The Latin is *respice finem* -- look at the end. What kind of object are you seeking? A number? A function? A subset? A proof?

Once you know the type of the unknown, ask: *Have I solved any problem before that had the same kind of unknown?* Not the same problem -- the same *kind* of unknown. If you are looking for the number of paths in a grid, you recall other counting problems. If you are looking for a bijection, you recall other bijection arguments. This narrows the search. Instead of scanning everything you know, you scan only problems with the same shape of answer.

There is a certain economy in this approach. First, you save effort in representing the problem: you need not look at the whole problem, just at the unknown. The problem appears schematically as "Given ... find the count." Second, there is an economy of choice. Many problems may be related to yours, but looking at the unknown restricts your search to problems with the same kind of answer. Among those, you consider first the most elementary and familiar.

If nothing comes to mind from memory, invent something. Ask: *Could I think of other data appropriate to determine the unknown?* You keep the unknown fixed and imagine different data that would make the problem easier or more familiar.

**Example.** You want to count the subsets of $\{1, 2, \ldots, n\}$ whose elements sum to a given value $s$. That is hard. But the unknown is "a count of subsets." You have solved a simpler problem with the same unknown: counting *all* subsets. And another: counting subsets of a given size. Each of these is a formerly solved problem with the same kind of unknown. Can you use any of them? Perhaps -- the question is whether there is a stepping stone from the simpler count to the harder one.

The point is not that you always find the connection. The point is that looking at the unknown gives you a short list of problems to consider, instead of the entire universe of mathematics. When no formerly solved problem with the same unknown exists at all, the situation is qualitatively harder -- that is the difference between a hard problem and a truly novel one. Archimedes, finding the surface area of a sphere, had no simpler problem with the same unknown to lean on. That is part of what made it a great achievement.

**Example.** You want to determine whether a given sequence of $n$ integers can be rearranged to form an arithmetic progression. The unknown is a yes-or-no answer. You have seen problems with the same kind of unknown before: "Is this sequence sorted?" "Does this array contain a duplicate?" Those problems are simpler, but they share the unknown type -- a boolean about a sequence property. The method for "does this contain a duplicate?" (sort, then scan for adjacent equals) suggests a method for the current problem: sort the sequence, then check whether consecutive differences are all equal. You found the approach by looking at the unknown.

**When to reach for it.** When you are stuck and want a structured way to search your memory. Ask what kind of object you need, then ask what problems you know that produce that kind of object.


## Keep the data and derive something useful

The other direction: forget the original unknown for a moment and look at what you have. The data. What can you derive from them?

Sometimes you look at the data and a useful intermediate quantity jumps out. This intermediate quantity is a new unknown -- a *stepping stone*. It is more accessible than the original unknown (easier to compute from the data) and, if you are lucky, useful for finding the original unknown afterward.

A stepping stone in the middle of a creek is closer to you than the far bank, and once you reach it, it helps you across.

Two things are desirable in a stepping stone. First, it should be accessible -- more easily obtainable from the data than the original unknown. Second, it should be useful -- when found, capable of rendering some definite service in the search for the original unknown. In practice, you must often settle for less. If nothing better presents itself, it is reasonable to derive something from the data that has some *chance* of being useful. And it is also reasonable to try a new unknown closely connected with the original one, even if it does not seem particularly accessible from the outset.

There is a related sub-strategy: *Could you solve a part of the problem?* If your problem has two unknowns, or two parts, one may be more accessible than the other. Concentrating on the more accessible part first can give you a foothold. In more complex problems, the decisive idea often consists in carving out some accessible but essential part from the whole.

**Example.** You are given a recurrence: $a_0 = 1$, $a_1 = 1$, and $a_n = a_{n-1} + a_{n-2}$ for $n \geq 2$. You want a closed-form expression for $a_n$. Before attacking that, you might derive something useful from the data: compute the first several terms ($1, 1, 2, 3, 5, 8, 13, 21, \ldots$), compute their ratios ($1, 2, 1.5, 1.667, 1.6, 1.625, 1.615, \ldots$). The ratios appear to converge. To what? This is a new, more accessible question. If you can answer it (the golden ratio $\phi = \frac{1+\sqrt{5}}{2}$), you have a stepping stone: the growth rate. From the growth rate you can guess the form of the closed-form solution ($a_n \approx C \phi^n$), and from there the exact formula follows.

You derived something useful from the data before you found the final unknown.

**When to reach for it.** When you have data but no idea how to connect them to the unknown. When the gap between what you know and what you need feels too wide for a single leap. Look for a stone in the middle.


## Extreme cases

Push a parameter to its boundary. Set $n = 0$. Set $n = 1$. Let a variable go to infinity. Let a constraint become vacuous. Let a constraint become maximally tight.

Extreme cases serve two purposes. First, they test: if you have a formula or a conjecture, checking it at the extremes is a fast sanity check. Second, they *suggest*: the behavior at the boundary often reveals the structure of the general case.

**Example.** You conjecture a closed form for the number of ways to choose $k$ items from $n$, namely $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. Before trying to prove it, check the extremes:

- If $k = 0$: there is exactly one way to choose nothing, so the formula should give $1$. Indeed, $\binom{n}{0} = \frac{n!}{0! \cdot n!} = 1$. Checkpoint passed.
- If $k = n$: there is exactly one way to choose everything, so $\binom{n}{n} = 1$. Indeed, $\frac{n!}{n! \cdot 0!} = 1$. Checkpoint passed.
- If $k = 1$: there are $n$ choices, so $\binom{n}{1}$ should be $n$. Indeed, $\frac{n!}{1!(n-1)!} = n$. Checkpoint passed.

These checkpoints do not prove the formula, but any formula that fails one of them is certainly wrong. And they do more than test: they reveal advance properties of the result. The fact that the answer must be $1$ when $k = 0$ or $k = n$, and must be $n$ when $k = 1$, constrains the shape of any correct formula. You can use these properties to *guess* the formula, not just to check it after the fact.

This is the deeper point about variation of data that Polya makes with the frustum example: varying the data contributes first of all to the interest of the problem. Then, it yields definite properties of the final result. The final formula must satisfy these boundary conditions. It is an advantage to foresee properties of the result you are trying to obtain. Such properties may give valuable suggestions and, in any case, when you have found the final formula you will be able to test it.

**Example.** You conjecture that for any sequence of $n + 1$ distinct integers chosen from $\{1, 2, \ldots, 2n\}$, at least one pair has a member dividing the other. Test the extreme cases:

- If $n = 1$: you pick $2$ numbers from $\{1, 2\}$, so you must pick both. Indeed, $1$ divides $2$. Holds.
- If $n = 2$: you pick $3$ numbers from $\{1, 2, 3, 4\}$. Try to avoid divisibility: $\{2, 3, 4\}$ -- but $2$ divides $4$. Try $\{3, 4\}$ -- only $2$ numbers, not enough. You cannot pick $3$ numbers without a divisibility pair.
- The "hardest" case for the conjecture: pick the $n$ largest numbers, $\{n+1, n+2, \ldots, 2n\}$. This gives $n$ numbers with no divisibility pair (each is more than half of any other). But you need $n + 1$, so you must include at least one number $\leq n$, and it will divide some number in the set.

The extreme cases have not proved the conjecture (the proof requires the pigeonhole principle applied to odd parts), but they have built strong evidence, revealed why the threshold is $n + 1$ and not $n$, and shown exactly where the conjecture would break if weakened.

**Example.** You conjecture that every connected graph on $n$ vertices with $n$ edges contains exactly one cycle. Test the extremes:

- The smallest connected graph on $n$ vertices has $n - 1$ edges (a tree) and zero cycles. Adding one edge to a tree creates exactly one cycle. So the conjecture holds at the boundary $n$ edges.
- What about $n = 1$? A single vertex with a self-loop has $1$ vertex, $1$ edge, and $1$ cycle. The conjecture holds.
- What about $n = 2$? Two vertices with two edges between them (a multigraph): $2$ vertices, $2$ edges, $1$ cycle. Holds.

The extreme cases build confidence. And as Polya notes, extreme cases are particularly instructive -- they are apt to be overlooked by the inventors of generalizations, so if the generalization survives them, the inductive evidence is strong. "Prospective exceptions test the rule." When an extreme case *does* fail, a single counterexample is enough to refute the conjecture entirely, saving you the effort of attempting a proof.


## When variation fails, then succeeds

Not every variation works. You may spend time on an auxiliary problem that leads nowhere. This is a real cost: you take away from the original problem the time and effort you devote to the auxiliary one. But Polya insists on an important lesson: a failed variation often contains the seed of a successful one.

**Example.** You need to find a bijection between binary strings of length $n$ with exactly $k$ ones and $k$-element subsets of $\{1, 2, \ldots, n\}$. Your first attempt at variation: drop the constraint that the string has exactly $k$ ones, and try to build a bijection from *all* binary strings to *all* subsets. That works easily (each string maps to the subset of positions where it has a $1$), but it does not help with the size constraint -- the bijection between all strings and all subsets does not restrict cleanly to the size-$k$ case. This variation has failed to solve the problem.

But look at what you learned. The bijection between all strings and all subsets *does* preserve size: a string with exactly $k$ ones maps to a subset of size exactly $k$. So the restriction to size-$k$ strings and size-$k$ subsets is itself a bijection. Your first variation was not useless -- it gave you the machinery. The second variation, restricting the first, finishes the job.

Polya illustrates this pattern with a construction problem where the first attempt (decreasing a parameter) leads to a dead end, but the second attempt (increasing the same parameter) succeeds. The lesson: "we may arrive at a more successful trial by modifying an unsuccessful one." We varied; we first tried one direction, then the other. The failed attempt was not wasted time -- it clarified the landscape and pointed toward the right direction.

**Example.** You want to count the number of labeled trees on $n$ vertices. You try variation by specialization: compute small cases. For $n = 1$: one tree (a single vertex). For $n = 2$: one tree (a single edge). For $n = 3$: three trees (each vertex can be the center). For $n = 4$: sixteen trees. The sequence $1, 1, 3, 16$ does not immediately suggest a pattern.

You try a different variation: generalize by asking for a formula not just for trees but for labeled forests on $n$ vertices with $k$ components. This is a *harder* problem. But this variation fails -- you do not know enough about forests yet to make progress.

Go back to the sequence: $1, 1, 3, 16$. Try $n = 5$: $125$ trees. Now the sequence is $1, 1, 3, 16, 125$. Written differently: $1^0, 1^0, 3^1, 4^2, 5^3$. You conjecture: $n^{n-2}$. This conjecture came from the failed variation (exhaustive computation of small cases) combined with the pattern-recognition that the failed generalization to forests suggested. The formula $n^{n-2}$ is Cayley's formula, and it has a beautiful proof by Prufer sequences -- but the *discovery* of the formula required variation through specialization and failure.

**When to recognize this pattern.** When a variation gives you *some* useful structure but not the full solution, do not discard it. Ask: can I modify this variation? Can I restrict it, extend it, or combine it with something else?


## Variation and completeness: did you use all the data?

Variation connects to another of Polya's fundamental questions: *Did you use all the data?*

When you derive a formula or build an argument, check whether every datum appears in the result. If a datum is missing, something is wrong -- or at least incomplete. This observation can *trigger* further variation.

**Example.** You are counting the number of lattice paths from $(0,0)$ to $(m,n)$ using steps right and up. You derive an expression that depends only on $m + n$: the total number of steps is $m + n$, and you need to choose which $m$ of them are rightward, giving $\binom{m+n}{m}$. Good -- both $m$ and $n$ appear.

But suppose you had made an error and written $2^{m+n}$ instead. This counts all binary strings of length $m + n$, not just those with exactly $m$ ones. The formula uses $m + n$ but not $m$ and $n$ separately. The question "did you use all the data?" catches the error: the problem distinguishes between $m$ and $n$ (the grid is $m$ wide and $n$ tall), so any correct formula must depend on them separately, not just on their sum.

This is a simple but powerful check. Whenever your result fails to mention a datum that the problem gave you, you have either made an error or missed a constraint. Either way, further variation is needed.

The connection to variation is this: when you notice a missing datum, you have identified a specific deficiency in your current approach. That deficiency tells you *which* variation to try next. If your formula does not contain $n$, vary $n$ and see what changes. If your argument never uses the fact that the graph is connected, look for a disconnected counterexample. The "did you use all the data?" question does not just detect errors -- it generates the next productive variation.

This also works in reverse. If a problem gives you data that seem redundant -- if you solve the problem without using some datum -- check whether the problem is overconstrained, or whether you have solved a weaker problem than intended. Either discovery is valuable.


## The inventor's paradox

Sometimes the more ambitious problem is easier to solve.

This sounds wrong. How can a harder problem be easier? Because generalization can *simplify*. When you strip away accidental features and state the problem in its natural generality, the structure becomes visible.

**Example.** You want to prove that the number of subsets of $\{1, 2, \ldots, n\}$ with an even number of elements equals the number with an odd number of elements (for $n \geq 1$). You could try to count each side separately, but both counts involve sums of binomial coefficients and comparing them is awkward.

Instead, generalize. Consider the identity

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$$

which says that the alternating sum of all binomial coefficients vanishes. This is a *stronger* statement -- it implies the even-odd equality, since the positive terms (even $k$) sum to the same value as the negative terms (odd $k$). And the stronger statement is easy to prove: it is just $(1 - 1)^n = 0$ by the binomial theorem. The weaker, vaguer statement about even and odd subsets resisted direct attack; the stronger, more precise statement yielded immediately to a known identity.

**Example.** You observe that

$$1^3 + 2^3 + 3^3 + 4^3 = 100 = 10^2.$$

Is this a coincidence? You check more cases:

$$
\begin{aligned}
1 &= 1^2 \\
1 + 8 &= 9 = 3^2 \\
1 + 8 + 27 &= 36 = 6^2 \\
1 + 8 + 27 + 64 &= 100 = 10^2 \\
1 + 8 + 27 + 64 + 125 &= 225 = 15^2.
\end{aligned}
$$

The bases of the squares are $1, 3, 6, 10, 15$ -- the triangular numbers. You conjecture:

$$1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2.$$

The first conjecture -- "the sum of the first $n$ cubes is a square" -- is weaker and vaguer. The second conjecture -- naming the square explicitly -- is *stronger* and *more precise*. Yet the second is easier to prove (by induction), because it gives you something concrete to verify in the inductive step. The weaker statement is too shapeless to grab onto.

This is the inventor's paradox in action. "The more ambitious plan may have more chances of success" -- provided it is not based on mere pretension but on some vision of the things beyond those immediately present.

One specific form of generalization deserves mention: replacing numbers with letters. If a problem is stated with specific numerical values, substitute variables. This move, simple as it sounds, gains access to new procedures: you can now vary the data continuously, check boundary cases, and use algebraic identities. It transforms a single problem into a family of problems, and the family is often easier to understand than any single member.

**Example.** "How many ways can you distribute 12 identical balls into 4 distinct boxes?" Replace $12$ with $n$ and $4$ with $k$. Now you have the general stars-and-bars problem: distribute $n$ identical objects into $k$ distinct bins. The general answer $\binom{n+k-1}{k-1}$ is easier to discover and prove than the specific numerical answer, because the general formulation exposes the combinatorial structure (choosing $k - 1$ dividers among $n + k - 1$ positions) that the specific numbers obscure.

The paradox arises constantly in combinatorics and algorithm design. You want to prove that a particular sequence satisfies a bound. You cannot do it directly. But if you prove a stronger statement -- a recurrence, a generating function identity, an invariant -- the stronger statement carries enough structure to support an inductive argument. The weaker statement, lacking that structure, resists proof.

**When to reach for it.** When a direct proof of a specific claim keeps failing. When you suspect there is a pattern behind the specific case. When the problem feels "too special" -- when the specifics are getting in the way of the structure. Try stating the problem more generally. If the general statement has a clean proof, you have found the right level of abstraction.


## Specialization as a stepping stone

Specialization -- restricting the problem to a smaller class or a particular case -- is the mirror image of generalization, and it serves a different purpose. Where generalization seeks the natural level of abstraction, specialization seeks a foothold. You solve a special case first, then use the insight to handle the general case.

The pattern often works like this: specialize to an extreme case, solve the special case completely, then find a supplementary remark that reduces the general case to the special one. Polya illustrates this with a physics problem about two ships, but the pattern is purely logical and appears everywhere.

**Example.** You want to show that in any sequence of $n^2 + 1$ distinct real numbers, there is either an increasing subsequence of length $n + 1$ or a decreasing subsequence of length $n + 1$. Start with the special case $n = 1$: any sequence of $2$ distinct numbers has either an increasing or decreasing pair. Trivially true. Try $n = 2$: any sequence of $5$ distinct numbers must contain an increasing or decreasing subsequence of length $3$.

The special case $n = 2$ is small enough to verify by exhaustion (there are only finitely many orderings of $5$ elements), and doing so reveals the pigeonhole structure: assign to each element its longest increasing subsequence length so far. If none reaches $3$, there are at most $2$ possible values, so by pigeonhole two elements share the same value, and those two -- being distinct -- must be in decreasing order. Extend this argument, and you have the proof for general $n$.

The special case was the stepping stone. You solved it, extracted the mechanism (pigeonhole on subsequence lengths), and the mechanism generalized.

**When to reach for it.** When the general problem feels too abstract or has too many moving parts. Set some parameters to specific values, solve the smaller problem, and look for the mechanism that made the solution work.


## Examining your guess through variation

Variation serves not only to find a solution but to examine one. When you have a guess -- a conjectured formula, a suspected answer -- variation helps you test it and sharpen it.

**Example.** You conjecture that among all graphs on $n$ vertices with a fixed number of edges $m$, the one maximizing the number of triangles is as "concentrated" as possible -- a complete graph on some subset of vertices, plus possibly some extra edges. Before trying to prove this, vary the problem to test the guess.

What happens at the extremes? If $m = \binom{n}{2}$ (the maximum), the graph is complete on all $n$ vertices. The conjecture holds trivially. If $m = 0$, there are no triangles at all. If $m = 3$, a triangle is possible -- and a triangle on 3 vertices is indeed the most concentrated arrangement. The guess survives the boundary checks.

Now try a different kind of variation. Instead of testing extreme cases, *weaken* the problem: restrict to a smaller class. Among all *bipartite* graphs on $n$ vertices with $m$ edges, how many triangles are there? Zero, always -- bipartite graphs have no odd cycles. This does not contradict the conjecture but it shows that the structure of the graph class matters. The conjecture is specifically about unrestricted graphs.

Polya's point: after having formulated your guess, the situation changes. Originally you had a "problem to find." Now you have a "problem to prove." And if the full problem-to-prove seems hard, you can apply variation again: *Could you solve a part of the problem?* Prove the conjecture for a restricted class first (say, only for regular graphs, or only for $m = \binom{r}{2}$). Each partial success builds evidence and may reveal the mechanism of the proof.

**When to reach for it.** When you have a conjecture and want to build confidence before investing in a proof. When you want to sharpen a vague guess into a precise statement. When you suspect a conjecture is false and want to find the counterexample efficiently.


## Concrete moves

When the direct attack stalls and you decide to vary the problem, here is a short list of things to try. They are ordered roughly from least disruptive to most.

1. **Drop a constraint.** Keep the unknown, weaken the condition. See how the unknown can vary under the weaker condition. (This is the most common and most useful variation.)

2. **Specialize.** Set a parameter to a small value. Try $n = 1$, $n = 2$, $n = 3$. Look for a pattern. Try an extreme or degenerate case.

3. **Generalize.** Replace a specific object with a family. Replace numbers with letters. Replace a specific structure with a class sharing the relevant property. (The inventor's paradox.)

4. **Change the unknown.** Keep the data, seek a different quantity. Can you derive something useful that is not the final answer but a stepping stone to it?

5. **Restate the condition.** Go back to definitions. Sometimes the decisive variation is not changing what the problem asks but how it asks it.

6. **Use analogy.** Is there a simpler or lower-dimensional version of the problem? A discrete version of a continuous problem, or vice versa? Solve the analogue first, then try to transfer the method.

7. **Interchange unknown and data.** Take the answer as given and ask what data would produce it. Work backwards from the desired result. (This is the method of analysis that Pappus described.)

Not every variation succeeds. You take away from the original problem the time and effort you devote to the auxiliary problem. If the auxiliary problem fails, that time may be lost -- but not always, as the failure-then-recovery pattern shows. Exercise your judgment. But the risk of varying is usually smaller than the risk of staring at the original problem without progress.


## Questions to keep

These are questions to ask yourself when the direct approach has stalled and you need to change the problem:

- *Can I satisfy part of the condition?* Which part is easy to satisfy? What happens when I drop the rest?
- *How far is the unknown then determined? How can it vary?*
- *Could I think of other data appropriate to determine the unknown?*
- *Could I derive something useful from the data?* Is there a stepping stone?
- *What happens at the extremes?* When a parameter is $0$, $1$, or $\infty$?
- *Is the specific case getting in the way?* Would a more general statement be easier to prove?
- *Could I change the unknown, or the data, or both, so that the new unknown and the new data are nearer to each other?*
- *Did I use all the data?* Is there a datum that does not appear in my result?
- *Did my last variation fail?* What did it teach me? Can I modify it into a better one?

These are not steps in an algorithm. They are prompts for your own thinking. When your progress is satisfactory, when new remarks emerge spontaneously, it would be stupid to hamper your spontaneous progress with extraneous questions. But when your progress is blocked, when nothing occurs to you -- then it is time to think of some general idea that could be helpful, some question from this list that might be suitable. Any question is welcome that has some chance of showing a new aspect of the problem; it may reconquer your interest, it may keep you working and thinking.

The insect does not vary. The mouse varies blindly. You can vary with intent -- asking which part of the problem to keep and which to change, and why.
