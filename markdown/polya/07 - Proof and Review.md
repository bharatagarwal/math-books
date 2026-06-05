# Proof and Review

You have a plan. You believe it works. Now you must carry it out, and then you must check what you have done. These are the third and fourth phases of the method: carrying out the plan, and looking back. They are different activities but they share a question: *Is this actually right?*

Discovery runs on plausible reasoning. Proof runs on strict reasoning. The shift between them is one of the most important transitions in problem-solving, and learning to make it cleanly is worth deliberate practice. This chapter is about that shift and what comes after.


## Why proofs?

Before getting into the mechanics of proof, it is worth asking directly: why should you learn to prove things at all? The question is not idle. There is a traditional story about Newton: as a young student, he began reading Euclid's Elements, saw that the theorems were true, and omitted the proofs. He wondered why anybody should take pains to prove things so evident. Many years later, he changed his opinion and praised Euclid.

Proofs serve you on three levels.

**As evidence and strict reasoning.** A complete proof leaves no gaps, no loopholes, no uncertainty. You may rarely achieve such rigor outside mathematics, but the *idea* of rigorous proof --- that there exists a standard of certainty beyond mere plausibility --- is one of the most valuable things a mathematical education can give you. If you have never really understood a proof, you lack a true standard with which to compare alleged evidence of all sorts. The proof of the angle-sum theorem via alternate interior angles is enough. If you have gone through that once, honestly, you know what evidence looks like.

**As the cement of a logical system.** Geometry, as Euclid presented it, is not a mere collection of facts but a logical system. Each proposition is linked to the foregoing axioms, definitions, and propositions by a proof. Without understanding proofs, you cannot understand the system --- and without the system, the facts are isolated fragments. Other sciences have tried to imitate this logical architecture. Whether they should or not is debatable, but you cannot join the debate without knowing the original.

**As a memory device.** Connected facts are more interesting and better retained than isolated ones. The figure showing the angle-sum proof links that theorem to the theorem about alternate angles. The two facts, connected, fix each other in memory. Even when your goal is just to remember results, proofs help. Any sort of connection that unites facts simply, naturally, and durably is welcome. A clear proof is often the simplest such connection.

### Incomplete proofs and the cookbook

What about proofs that are not fully rigorous? For a strict logician, an incomplete proof is no proof at all. But in practice, incomplete proofs can be valuable --- provided you know they are incomplete and do not pretend otherwise.

P&oacute;lya distinguished this carefully. If you present a heuristic argument with taste and frankness, stating openly that it is not a proof, it may prepare the ground for the rigorous argument and lend interest and coherence to your understanding. But if you present it ambiguously, with visible hesitation between shame and pretension, it does harm.

The alternative is worse. Without any proofs at all, a subject reduces to what P&oacute;lya called the "cookbook system" --- a collection of recipes with no reasons, no connections, no understanding. A cookbook may serve its purpose, but mathematics presented as a cookbook becomes an incoherent inventory of indigestible information. Procedures taught without proofs are not understood. Rules given without reasons are quickly forgotten.

The right answer is usually somewhere between: give complete proofs where you can, use incomplete proofs as scaffolding where you must, and mark the difference honestly.


## Carrying out the plan

To devise a plan, to conceive the idea of the solution, is not easy. It takes knowledge, good habits, concentration, and one more thing: good luck. To carry out the plan is much easier; what you need is mainly patience.

The plan gives a general outline. You must convince yourself that the details fit into the outline. Examine them one after another, patiently, until everything is perfectly clear and no obscure corner remains in which an error could hide.

The main danger is forgetting the plan. If you received the plan from outside and accepted it passively, you will lose it easily. If you worked for it yourself, struggled with the problem, and felt satisfaction when the idea arrived, you will not lose it. But even then, distractions and fatigue can pull you off course. Keep the outline visible. Write it down if you must.

The relationship between planning and carrying out is the relationship between analysis and synthesis in the old Greek sense. Pappus described it: analysis is devising a plan, synthesis is carrying it through. In analysis you work backward from the goal; in synthesis you work forward from what is known. The order of discovery is the reverse of the order of presentation. "What a fool does at last, a wise man does at first." When you carry out your plan, you proceed in the direction opposite to the one in which you found it.

As you fill in each step, ask yourself two things:

- *Can you see clearly that the step is correct?*
- *Can you prove that the step is correct?*

These are different, and the difference matters.

### Stepping stones

In a long plan, you do not leap from start to finish. You pass through intermediate results --- stepping stones. P&oacute;lya used the image directly: "A stone in the middle of the creek is nearer to me than the other bank which I wish to arrive at and, when the stone is reached, it helps me on toward the other bank."

An intermediate unknown should be both *accessible* (easier to reach from the data than the final unknown) and *useful* (once found, it helps you reach the final unknown). In practice, you must often settle for less. If nothing better presents itself, it is not unreasonable to derive something from the data that has some chance of being useful. Or to try an intermediate unknown that is closely connected with the original, even if it does not seem particularly accessible.

In the subset-counting example, the bijection with binary strings produces the count $2^n$ by passing through three stepping stones: well-defined, injective, surjective. Each is accessible (one short argument) and useful (together they establish the bijection). The chain of stepping stones is the proof.

### The recurring example: counting subsets

Suppose you have found (in an earlier phase) that the number of subsets of an $n$-element set should be $2^n$, and your plan is to prove this by establishing a bijection between subsets and binary strings of length $n$. Each subset corresponds to a string where the $k$-th bit is $1$ if the $k$-th element is included and $0$ otherwise.

Carrying out the plan means checking the details of this bijection:

1. **Well-defined.** Given any subset $S \subseteq \{1, 2, \ldots, n\}$, the binary string is uniquely determined. Do you see this clearly? Yes: for each element, the element is either in $S$ or not.

2. **Injective.** Different subsets produce different strings. If $S \neq T$, some element $k$ is in one but not the other, so bit $k$ differs. Clear.

3. **Surjective.** Every binary string of length $n$ comes from some subset. Given a string, take the set of positions where the bit is $1$. Clear.

4. **Counting.** There are $2^n$ binary strings of length $n$ (two choices per position, $n$ positions). Therefore there are $2^n$ subsets.

Each step is short. Each is checkable. The whole argument takes a minute. But if you had skipped any step, you might have carried a hidden error into later work. "Step after step the ladder is ascended."


## Can you see it? Can you prove it?

The distinction between seeing and proving deserves more attention than it usually gets.

When you see that a step is correct, you grasp it whole. The conviction is immediate. You may not be able to articulate why, but you are sure. This kind of understanding is fast and powerful. It is also fallible. Optical illusions exist in mathematics too: arguments that look right and are wrong.

When you prove that a step is correct, you lay out a chain of reasoning from premises to conclusion. Each link is small enough to verify. The conviction is transferable: someone else can check it. This kind of understanding is slower and more laborious. It is also more reliable.

The ideal is to have both. See it first, then prove it. If you can see it but not prove it, be suspicious of the seeing. If you can prove it but not see it, you have a correct result but an incomplete understanding. Keep working until you can do both.

P&oacute;lya put the relationship this way: we may convince ourselves of the correctness of a step either "intuitively" or "formally." We may concentrate upon the point until we see it so clearly and distinctly that we have no doubt, or we may derive the point according to formal rules. The difference between insight and formal proof is clear enough in many important cases; we may leave further discussion to philosophers.

In practice, you must decide which steps need full proof and which need only a clear look. This is a matter of judgment, and the judgment improves with experience. A useful default: prove the steps that surprise you, and prove the steps where a mistake would be hard to detect later. In a long argument, pick the "touchy" points for rechecking. You do not need to recheck every step with equal care --- but you need to know which steps are touchy.

Consider the bijection proof above. The surjectivity step is so immediate that seeing suffices. But suppose you were proving a bijection between integer partitions and some family of lattice paths. Surjectivity might be the hard part, the place where your construction could silently fail. That is where you need proof, not just sight.


## Problems to prove

P&oacute;lya distinguishes two kinds of problems: problems to find and problems to prove. In a problem to find, you seek an object (a number, a configuration, a function). In a problem to prove, you seek to establish that a clearly stated assertion is true, or to show that it is false.

The principal parts of a problem to prove are the **hypothesis** and the **conclusion**. The questions that guide you are adapted accordingly:

- *What is the hypothesis?*
- *What is the conclusion?*
- *Did you use the whole hypothesis?*
- *Look at the conclusion! And try to think of a familiar theorem having the same or a similar conclusion.*

This last question is the "problems to prove" analogue of "Look at the unknown! And try to think of a familiar problem having the same or a similar unknown." The strategy is the same: you focus on the target and search your memory for something with a matching target.

"Problems to find" are more common in elementary mathematics. "Problems to prove" become dominant as you advance. The two are not separate worlds. A problem to find often requires a proof that the answer is correct, and a problem to prove often requires you to find a key construction or auxiliary object. The subset-counting example is both. You first *find* that the answer should be $2^n$ (by testing small cases: $n = 0, 1, 2, 3$ give $1, 2, 4, 8$). Then you *prove* it (by the bijection argument, or by induction).

When you are stuck on a problem to prove, the same repertoire of variation that works on problems to find is available:

- *Keep the conclusion and change the hypothesis.* Can you think of a stronger hypothesis from which the conclusion would follow more easily?
- *Keep the hypothesis and change the conclusion.* Can you derive *something* useful from the hypothesis, even if it is not the full conclusion?
- *Drop part of the hypothesis.* Is the conclusion still valid?

These are not random changes. Each one is a systematic way to vary the problem in search of a foothold.

### Did you use all the data?

This question deserves more than a passing mention. P&oacute;lya treated it as a diagnostic tool, not just a checklist item.

Suppose you are working on a problem whose hypothesis has three parts, all essential to the truth of the theorem. If you discard any part, the theorem ceases to be true. Therefore, if your proof neglects to use any part of the hypothesis, the proof must be wrong. Ask yourself: does the proof use the first part? Where? The second part? Where? The third? Answering these questions, you check the proof from a direction that catches errors the forward flow of argument can miss.

The same question works in constructing a proof. If some datum does not appear in your argument, either the datum is redundant (rare in well-stated problems) or you have not yet found the decisive connection. The missing datum points to the gap. It tells you where to look next.

Consider a chess problem where you must mate in two moves: if there is a white knight on the board that your proposed solution never moves or threatens through, your solution is probably wrong. A well-constructed problem has no superfluous pieces. *Did you use all the data?* is the question that catches this.


## Mathematical induction

Induction is the most common proof technique for statements that depend on an integer $n$. Its structure is simple:

1. **Base case.** Verify the statement for the smallest value of $n$ (often $n = 0$ or $n = 1$).
2. **Inductive step.** Assume the statement holds for some $n = k$. Show that it then holds for $n = k + 1$.

If both steps succeed, the statement holds for all $n$ from the base case onward. The base case starts the chain; the inductive step ensures it never breaks.

### The idea

Why does this work? Because the inductive step is a bridge. It connects each case to the next. If the base case is solid ground, the inductive step lets you walk from $n = 0$ to $n = 1$, from $n = 1$ to $n = 2$, and so on without limit. You never have to check infinitely many cases. You check one, and you check the bridge.

It is rather unfortunate that the name "mathematical induction" is so close to the word "induction" in its ordinary sense. Ordinary induction is the process of discovering general laws by observation --- checking cases, spotting patterns, guessing the rule. Mathematical induction is a technique of proof, not of discovery. The two are connected in practice (you often discover the statement by ordinary induction and then prove it by mathematical induction), but they are logically quite different.

### Concrete moves

1. **State the claim precisely.** Induction requires an explicit formula or property depending on $n$. Vague claims cannot be checked at the inductive step. This is closely related to the inventor's paradox: the more precise statement is often easier to prove.
2. **Check the base case.** Do not skip it. It is not a formality. The inductive step alone proves nothing; it says "if true for $k$, then true for $k + 1$," and if the base case fails, the whole chain is suspended in air.
3. **Write the inductive hypothesis.** State clearly what you are assuming: "Suppose the claim holds for $n = k$."
4. **Prove the inductive step.** Show the claim for $n = k + 1$, using the assumption for $n = k$. The art is in connecting $k + 1$ back to $k$.
5. **Check that you actually used the inductive hypothesis.** If you proved the step for $k + 1$ without ever invoking the assumption for $k$, either you have found a direct proof (and induction was unnecessary) or you have made an error.

### The sum of cubes

P&oacute;lya's own example is worth keeping. We observe:

$$
\begin{aligned}
1 &= 1^2 \\
1 + 8 &= 9 = 3^2 \\
1 + 8 + 27 &= 36 = 6^2 \\
1 + 8 + 27 + 64 &= 100 = 10^2 \\
1 + 8 + 27 + 64 + 125 &= 225 = 15^2.
\end{aligned}
$$

The bases of the squares are $1, 3, 6, 10, 15$. These are the triangular numbers: $1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5$. Ordinary induction (pattern-spotting) discovered two things: first, that the sum of cubes is always a perfect square; second, more precisely, that

$$1^3 + 2^3 + 3^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2.$$

Now we use mathematical induction to prove it.

**Base case.** $n = 1$: $1^3 = 1 = (1 \cdot 2 / 2)^2 = 1$. True.

**Inductive step.** Assume the formula holds for $n = k$. Then for $n = k + 1$:

$$1^3 + \cdots + k^3 + (k+1)^3 = \left(\frac{k(k+1)}{2}\right)^2 + (k+1)^3$$

$$= (k+1)^2 \left(\frac{k^2}{4} + (k+1)\right) = (k+1)^2 \cdot \frac{k^2 + 4k + 4}{4} = (k+1)^2 \cdot \frac{(k+2)^2}{4}$$

$$= \left(\frac{(k+1)(k+2)}{2}\right)^2.$$

This is the formula with $n = k + 1$. The chain holds.

Notice the **inventor's paradox** at work. The vaguer statement "the sum of cubes is always a perfect square" is harder to prove by induction than the sharper statement with the explicit formula. The more precise claim gives you something concrete to work with at the inductive step. The stronger theorem is easier to prove.

P&oacute;lya made this point carefully: passing from the first, less precise assertion to the second, more precise one was an important preparation for the final proof. The first assertion is less "explicit," less "tangible," less accessible to testing and checking. The step from vague to precise --- from "it seems to be a square" to "the square root is the $n$-th triangular number" --- is itself an act of discovery, and it is what makes the proof possible.

The inventor's paradox deserves more than passing mention. P&oacute;lya stated it bluntly: "The more ambitious plan may have more chances of success." This sounds paradoxical, but it is not based on mere pretension. It is based on *vision* --- on seeing something of the structure beyond the immediate question. A more general problem may be easier to solve because generality reveals what is essential and strips away what is accidental. (The octahedron-bisection example from the Generalization entry is a perfect case: the general problem about solids with a center of symmetry is trivially solved, while the specific problem about the octahedron looks hard.) When you are stuck on an induction, the first thing to try is strengthening the hypothesis.

### Counting subsets by induction

The same result $|\mathcal{P}(\{1, \ldots, n\})| = 2^n$ admits an inductive proof.

**Base case.** $n = 0$: the empty set has one subset (itself). $2^0 = 1$. True.

**Inductive step.** Assume a set with $k$ elements has $2^k$ subsets. Consider a set with $k + 1$ elements, say $\{1, \ldots, k, k+1\}$. Every subset either contains $k + 1$ or does not. Subsets not containing $k + 1$ are exactly the subsets of $\{1, \ldots, k\}$: there are $2^k$ by hypothesis. Subsets containing $k + 1$ are in bijection with subsets of $\{1, \ldots, k\}$ (just remove $k + 1$): also $2^k$. Total: $2^k + 2^k = 2^{k+1}$.

Two proofs of the same fact (bijection with binary strings, and induction) are better than one. They illuminate different aspects and provide independent confirmation. "It is safe riding at two anchors."

### When to reach for induction

Reach for it when the claim depends on an integer and the case $n = k + 1$ can be related to the case $n = k$ by adding one element, one term, or one step. If you cannot see how $k + 1$ connects to $k$, induction may not be the right tool --- or you may need a stronger inductive hypothesis (the inventor's paradox again).


## Reductio and indirect proof

Reductio ad absurdum shows the falsity of an assumption by deriving from it a manifest absurdity. Indirect proof establishes the truth of an assertion by showing the falsity of the opposite assumption. They are related but different procedures, and both are effective tools of discovery.

"Reductio ad absurdum" has some resemblance to irony, which is the favorite procedure of the satirist: adopt an opinion, stress it and overstress it, until it leads to a manifest absurdity. "Indirect proof" has some resemblance to a politician's trick of establishing a candidate by demolishing the reputation of his opponent. Not everyone likes these procedures. A few philosophers and many beginners dislike them. But they work.

### The idea

Sometimes you cannot see how to prove a statement directly. Instead, you assume the opposite and show that the opposite leads to a contradiction. Since the opposite cannot be true, the original statement must be.

The key psychological move is to face squarely a hypothetical situation that you suspect is impossible, and to examine it closely enough to find the point that is definitely wrong. You must keep an open mind during this examination. P&oacute;lya emphasized this: the investigation, if it is well conducted, starts the same way whether you hope to find a solution or hope to show that no solution exists. It "shows only in its later course which hope is justified." You do not prejudge. You set up the equations, you draw the consequences, and you see where they lead. This open-mindedness is essential. If you have already decided the answer, you are not investigating --- you are performing.

### Infinitely many primes

The primes are $2, 3, 5, 7, 11, 13, \ldots$ Is the list infinite?

Suppose not. Suppose there is a last prime $P$, so the complete list is $2, 3, 5, \ldots, P$. Form the number:

$$Q = (2 \cdot 3 \cdot 5 \cdots P) + 1.$$

$Q$ is greater than $P$, so by assumption $Q$ is not prime. Then $Q$ must be divisible by some prime in our list. But dividing $Q$ by any of $2, 3, 5, \ldots, P$ leaves remainder $1$. Contradiction. There is no last prime.

This is Euclid's proof. It has stood for over two thousand years.

But notice: the reductio can be rearranged into a direct, constructive argument. Given any finite set of primes $2, 3, 5, \ldots, P$, the number $Q = (2 \cdot 3 \cdot 5 \cdots P) + 1$ is divisible by some prime not in that set (namely, any prime factor of $Q$). So no finite set of primes is complete. The content is the same; the presentation is positive rather than negative. Nothing is indirect in it, no impossible situation needs to be considered.

This illustrates a general pattern. Once you have found an argument by reductio, look back and ask: *Can you derive the result differently?* Often the reductio was scaffolding for a direct argument that you can now see.

### Digit sums

Write numbers using each of the ten digits $0, 1, 2, \ldots, 9$ exactly once, so that their sum is exactly $100$. Can it be done?

Suppose it can. Each number has one or two digits. The ten digits sum to $0 + 1 + \cdots + 9 = 45$. Let $t$ be the sum of the digits that appear in the tens place. Then the total is $10t + (45 - t) = 9t + 45$. For this to equal $100$, we need $t = 55/9$. But $t$ must be an integer. Contradiction. The puzzle has no solution.

The reductio led to a positive insight: the sum of any such arrangement is always $9t + 45$, which is always divisible by $9$. Once you see this, you can restate the argument without any false assumption: "Every such arrangement sums to a multiple of $9$. Since $100$ is not a multiple of $9$, no arrangement works." The discovery happened by reductio; the clean statement is direct.

P&oacute;lya gave careful attention to *why* you should rearrange. It is not mere aesthetics. Listening to a reductio, you are obliged to focus your attention all the time upon a false assumption which you should forget, not upon the true theorem which you should retain. If you do not wish to store falsehoods in your memory, you should seek the positive content --- carve out the part of the argument that is independent of the initial false assumption and that contains genuine information. In the digit-sum example, the positive content is the divisibility-by-nine law. In the primes example, it is the construction of a new prime from any finite list.

The direct proof retains truth. The reductio stores falsehoods that you must eventually discard. Both are legitimate tools, but the direct proof, when you can find it, is the one you want to keep.

### Concrete moves

1. **Assume the opposite** of what you want to prove.
2. **Derive consequences** from that assumption, using all the tools available.
3. **Seek a contradiction**: two statements that cannot both be true.
4. **Conclude** that the assumption was false.
5. **Look back**: can you rearrange the argument into a direct proof? Often you can. When you can, the direct proof is usually clearer.

### When to reach for it

When direct proof stalls. When you have no idea how to construct the object you need, but you can see that its nonexistence would be absurd. When the structure of the problem invites you to "face squarely the hypothetical situation" and examine it for contradictions. And always, when you succeed, ask whether the scaffolding can be removed.

### A note on taste

P&oacute;lya acknowledged the objection to indirect proof honestly. A long reductio can become unbearable --- the words "hypothetically," "supposedly," "allegedly" must recur incessantly, and the inner discord between examining an impossible situation and wanting to reject it grows painful. The verbal expression becomes tedious.

Yet it would be foolish to repudiate reductio as a tool of discovery. Experience shows that usually there is little difficulty in converting an indirect proof into a direct proof. Use the reductio to find the argument. Then rearrange the argument for clarity.


## Check the result

Even fairly good problem-solvers, when they have obtained the solution and written down neatly the argument, shut their books and look for something else. Doing so, they miss an important and instructive phase of the work.

By looking back at the completed solution, by reconsidering and reexamining the result and the path that led to it, you consolidate your knowledge and develop your ability to solve problems.

No problem whatever is completely exhausted. There remains always something to do; with sufficient study and penetration, you could improve any solution, and in any case you can always improve your understanding of the solution.

The first question is: *Can you check the result?*

### Why checks work

Each check below gives you what P&oacute;lya called "experimental evidence" --- confidence that comes from a *different source* than the derivation itself. You were convinced before that the formula is correct because you derived it carefully. After checking, you are more convinced, and your gain in confidence comes from a different source. It is due to a sort of independent verification, like perceiving an object through two different senses. This is what makes checks valuable even when you trust your proof.

### Concrete checks

1. **Test special cases.** Substitute simple values. For the subset formula $2^n$: does $n = 0$ give $1$? Does $n = 1$ give $2$? Does $n = 3$ give $8$?

2. **Test boundary cases.** What happens at the extremes? Does the formula degenerate gracefully? The number of edges in $K_n$ is $\binom{n}{2}$. For $n = 0$: $\binom{0}{2} = 0$ edges. For $n = 1$: $\binom{1}{2} = 0$ edges. For $n = 2$: $\binom{2}{2} = 1$ edge. Each makes sense.

3. **Check symmetry.** If the problem is symmetric in its data, the answer should be too. The binomial coefficient $\binom{n}{k}$ counts $k$-element subsets of an $n$-element set. Choosing which $k$ elements to include is the same as choosing which $n - k$ elements to exclude. So $\binom{n}{k}$ must equal $\binom{n}{n-k}$. If your formula for $\binom{n}{k}$ did not have this symmetry, something would be wrong. The same principle applies to any formula whose inputs play interchangeable roles: if the problem does not distinguish between them, the answer must not distinguish between them either.

4. **Check dimensions or types.** If the problem asks for a count, the answer should be a non-negative integer. If the problem asks for a probability, the answer should lie between $0$ and $1$. P&oacute;lya devoted an entire entry to "test by dimension," showing how dimensional analysis alone can determine the form of a physical formula. His pendulum example is striking: if the period $T$ depends only on the length $l$ and gravitational acceleration $g$, then purely from the requirement that dimensions match, $T = c\sqrt{l/g}$ for some constant $c$. The dimensions force the exponents. In discrete math the analogue is type-checking: a count must be a non-negative integer, a probability must lie in $[0, 1]$, a graph on $n$ vertices has at most $\binom{n}{2}$ edges.

5. **Verify that you used all the data.** If some datum does not appear in the answer, either the datum was redundant (possible in practical problems, rare in well-stated problems) or you dropped it. "Did you use all the data? Did you use the whole condition?" This question does double duty: it checks the result and it checks the argument.

6. **Check monotonicity.** Does the answer increase when you expect it to increase? For $2^n$ subsets of an $n$-element set: adding one element should roughly double the count, and indeed $2^{n+1} = 2 \cdot 2^n$. For $\binom{n}{k}$ with $k$ fixed and $n$ increasing: more elements means more subsets of size $k$, and indeed $\binom{n+1}{k} > \binom{n}{k}$.

7. **Brute-force a small case.** For $n = 3$, list all subsets of $\{1, 2, 3\}$ by hand: $\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \{1,2,3\}$. Eight subsets. $2^3 = 8$. Good.

These checks are fast. None of them is a proof. But a result that passes all of them is almost certainly correct, and a result that fails any of them is certainly wrong. After some experience with such checks, you begin to perceive the underlying general ideas: use of all relevant data, variation of the data, symmetry, analogy, dimensional consistency. If you get into the habit of directing your attention to such points, your ability to solve problems will definitely profit.


## Derive it differently

"In order to convince ourselves of the presence or of the quality of an object, we like to see and to touch it. And as we prefer perception through two different senses, so we prefer conviction by two different proofs."

*Can you derive the result differently?*

For the subset count, we have three proofs:

- **Bijection with binary strings.** Each subset maps to a unique string of $n$ bits; there are $2^n$ such strings.
- **Induction.** Each new element doubles the number of subsets.
- **Multiplication principle.** For each of $n$ elements, you make an independent binary choice (in or out). $2 \times 2 \times \cdots \times 2 = 2^n$.

Three arguments, each self-contained, each illuminating a different facet of the same truth. The bijection argument shows *why* the answer is a power of two (binary encoding). The induction argument shows *how* the count grows (doubling). The multiplication principle shows *where* the count comes from (independent choices).

If all three agree, the result is virtually certain. But more importantly, you now understand it from three directions, and that understanding transfers to other problems. The next time you see independent binary choices, you will think $2^n$. The next time you see a structure that doubles with each new element, you will think induction.

We prefer a short and intuitive argument to a long and heavy one: *Can you see it at a glance?* The multiplication principle gives the most compact proof. To "see it at a glance" means to compress the argument to its essence --- to find the single picture or sentence that makes the result obvious. This is not a luxury. A proof you can see at a glance is a proof you can reconstruct from memory, a proof you own rather than merely recall. The question "Can you see it at a glance?" is a test of understanding, not just efficiency.

The question "Can you derive the result differently?" is not idle curiosity. It is training. Each new proof you find for a known result strengthens a different connection in your knowledge and prepares you for a different class of future problems.


## Use the result elsewhere

*Can you use the result, or the method, for some other problem?*

This is where understanding consolidates into knowledge. The solution you do not examine is the solution you cannot reuse.

P&oacute;lya wrote about the future mathematician: "For him, the most important part of the work is to look back at the completed solution. Surveying the course of his work and the final shape of the solution, he may find an unending variety of things to observe. He may meditate upon the difficulty of the problem and about the decisive idea; he may try to see what hampered him and what helped him finally." This is not a description of an advanced activity reserved for professionals. It is a description of how understanding works. If you have made an honest effort at a problem and solved it, you are naturally eager to see what else you could accomplish with that effort, and how you could do equally well another time. That eagerness is the engine of looking back.

The binary-string representation of subsets is not a one-problem trick. It is a general technique. Here are a few immediate consequences:

1. **Subsets of a given size.** The number of $k$-element subsets of an $n$-element set equals the number of binary strings of length $n$ with exactly $k$ ones. This is $\binom{n}{k}$.

2. **The binomial theorem in combinatorics.** Summing over $k$: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$. This is the same result, seen from another angle. The identity follows immediately from the two counting methods: count all subsets by size, or count them all at once.

3. **Inclusion-exclusion.** Subsets that avoid a particular element $j$ correspond to strings with bit $j$ set to $0$. There are $2^{n-1}$ such subsets. Subsets containing $j$ also number $2^{n-1}$. The representation makes these counts obvious.

4. **Characteristic functions.** In more advanced work, the binary string associated with a subset $S$ is precisely the characteristic function $\chi_S : \{1, \ldots, n\} \to \{0, 1\}$. This bijection between subsets and functions to $\{0, 1\}$ generalizes: functions to a $k$-element set correspond to $k$-colorings, and there are $k^n$ of them. The subset result is the special case $k = 2$.

The method of the proof (establishing a bijection to a simpler set) is even more reusable than the result. Bijective proofs are a standard technique in combinatorics. Every time you want to count a complicated set, ask: is there a simpler set in bijection with it?

Looking back at the method, you extract a transferable skill. Looking back at the result, you see connections to other problems. Both strengthen your ability to solve future problems. Problems are not isolated. The connections between them are where mathematical understanding lives. You have a natural opportunity to investigate those connections when looking back at the solution.

"Look around when you have got your first mushroom or made your first discovery; they grow in clusters."


## Questions to keep

- *Can you see clearly that the step is correct? Can you also prove it?* (Polya's two levels of conviction — use both.)
- *Can you check the result?* Special cases, boundary cases, a different derivation.
- *Can you use the result, or the method, for some other problem?*
- *Did you use all the data? Did you use the whole condition?*

The fourth phase, looking back, is not a luxury. It is where understanding consolidates into knowledge, where you discover your own method, where the future mathematician in you takes shape. Check it, rederive it, connect it. Then move on.
