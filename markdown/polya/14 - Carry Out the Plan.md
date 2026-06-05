# Carry Out the Plan

Discovery runs on plausible reasoning. Proof runs on strict reasoning. The shift between them is one of the most important transitions in problem-solving. This chapter is about that shift: you have a plan, you believe it works, and now you must carry it out with the discipline that turns a guess into a result.

To devise a plan, to conceive the idea of the solution, is not easy. It takes knowledge, good habits, concentration, and good luck. To carry out the plan is much easier; what you need is mainly patience.


## Why proofs?

Before getting into the mechanics, ask directly: why prove things at all? There is a traditional story about Newton. As a young student, he began reading Euclid's Elements, saw that the theorems were true, and omitted the proofs. He wondered why anybody should take pains to prove things so evident. Many years later, he changed his opinion and praised Euclid.

Proofs serve you on three levels.

**As a standard of certainty.** A complete proof leaves no gaps, no loopholes. You may rarely achieve such rigor outside mathematics, but the *idea* of rigorous proof is one of the most valuable things a mathematical education can give you. If you have never really understood a proof, you lack a true standard with which to compare alleged evidence of all sorts.

**As the cement of a logical system.** Without proofs, facts are isolated fragments. Connected by proofs, they form a system where each proposition is linked to the foregoing axioms and propositions. The connection is what makes the system useful.

**As a memory device.** Connected facts are more interesting and better retained than isolated ones. Even when your goal is just to remember results, proofs help. Any sort of connection that unites facts simply, naturally, and durably is welcome.

What about incomplete proofs? For a strict logician, an incomplete proof is no proof at all. But in practice, incomplete proofs can be valuable --- provided you know they are incomplete and do not pretend otherwise. If you present a heuristic argument with frankness, stating openly that it is not a proof, it may prepare the ground for the rigorous argument. If you present it ambiguously, with visible hesitation between shame and pretension, it does harm.

Without any proofs at all, a subject reduces to what Polya called the "cookbook system" --- a collection of recipes with no reasons, no connections, no understanding. Rules given without reasons are quickly forgotten.


## Carrying out the plan

The plan gives a general outline. You must convince yourself that the details fit into the outline. Examine them one after another, patiently, until everything is perfectly clear and no obscure corner remains in which an error could hide.

The main danger is forgetting the plan. If you received it from outside and accepted it passively, you will lose it easily. If you worked for it yourself, struggled with the problem, and felt satisfaction when the idea arrived, you will not lose it. But even then, distractions and fatigue can pull you off course. Keep the outline visible. Write it down if you must.

As you fill in each step, ask yourself two things:

- *Can you see clearly that the step is correct?*
- *Can you prove that the step is correct?*

These are different, and the difference matters.

### Stepping stones

In a long plan, you do not leap from start to finish. You pass through intermediate results. Polya used the image directly: "A stone in the middle of the creek is nearer to me than the other bank which I wish to arrive at and, when the stone is reached, it helps me on toward the other bank."

An intermediate unknown should be both *accessible* (easier to reach from the data than the final unknown) and *useful* (once found, it helps you reach the final unknown). In practice, you must often settle for less.

In the subset-counting example, the bijection with binary strings produces the count $2^n$ by passing through three stepping stones: well-defined, injective, surjective. Each is accessible (one short argument) and useful (together they establish the bijection). The chain of stepping stones is the proof.


## Can you see it? Can you prove it?

When you *see* that a step is correct, you grasp it whole. The conviction is immediate. This kind of understanding is fast and powerful. It is also fallible. Optical illusions exist in mathematics too: arguments that look right and are wrong.

When you *prove* that a step is correct, you lay out a chain of reasoning from premises to conclusion. Each link is small enough to verify. The conviction is transferable: someone else can check it. This kind of understanding is slower. It is also more reliable.

The ideal is to have both. See it first, then prove it. If you can see it but not prove it, be suspicious of the seeing. If you can prove it but not see it, you have a correct result but an incomplete understanding.

In practice, you must decide which steps need full proof and which need only a clear look. This is judgment, and it improves with experience. A useful default: prove the steps that surprise you, and prove the steps where a mistake would be hard to detect later. Pick the "touchy" points for rechecking.

Consider the bijection proof for counting subsets. Surjectivity is so immediate that seeing suffices. But if you were proving a bijection between integer partitions and some family of lattice paths, surjectivity might be the hard part, the place where your construction could silently fail. That is where you need proof, not just sight.


## Problems to prove

Polya distinguishes two kinds of problems: problems to find and problems to prove. In a problem to find, you seek an object. In a problem to prove, you seek to establish that a clearly stated assertion is true, or to show that it is false.

The principal parts of a problem to prove are the **hypothesis** and the **conclusion**. The guiding questions adapt accordingly:

- *What is the hypothesis?*
- *What is the conclusion?*
- *Did you use the whole hypothesis?*
- *Look at the conclusion! And try to think of a familiar theorem having the same or a similar conclusion.*

That last question is the analogue of "Look at the unknown!" for problems to find. Focus on the target and search your memory for something with a matching target.

The two kinds are not separate worlds. The subset-counting example is both. You first *find* that the answer should be $2^n$ (by testing small cases: $n = 0, 1, 2, 3$ give $1, 2, 4, 8$). Then you *prove* it.

### Did you use all the data?

This question deserves more than a passing mention. Polya treated it as a diagnostic tool. If a problem's hypothesis has three essential parts and your proof neglects to use one, the proof must be wrong. Ask yourself: does the proof use the first part? Where? The second? The third?

The same question works in constructing a proof. If some datum does not appear in your argument, either it is redundant (rare in well-stated problems) or you have not yet found the decisive connection. The missing datum points to the gap.


## Mathematical induction

Induction is the most common proof technique for statements that depend on an integer $n$. Its structure is simple:

1. **Base case.** Verify the statement for the smallest value of $n$.
2. **Inductive step.** Assume the statement holds for $n = k$. Show it then holds for $n = k + 1$.

If both succeed, the statement holds for all $n$ from the base case onward. The base case starts the chain; the inductive step ensures it never breaks.

It is rather unfortunate that the name "mathematical induction" is so close to "induction" in its ordinary sense. Ordinary induction is the process of discovering general laws by observation. Mathematical induction is a technique of proof, not of discovery. You often discover the statement by ordinary induction and prove it by mathematical induction, but they are logically quite different.

### The sum of cubes

Polya's own example is worth keeping. We observe:

$$
\begin{aligned}
1 &= 1^2 \\
1 + 8 &= 9 = 3^2 \\
1 + 8 + 27 &= 36 = 6^2 \\
1 + 8 + 27 + 64 &= 100 = 10^2.
\end{aligned}
$$

The bases of the squares are $1, 3, 6, 10$ --- the triangular numbers. Pattern-spotting discovers the formula:

$$1^3 + 2^3 + \cdots + n^3 = \left(\frac{n(n+1)}{2}\right)^2.$$

**Base case.** $n = 1$: $1^3 = 1 = (1 \cdot 2 / 2)^2$. True.

**Inductive step.** Assume the formula holds for $n = k$. Then:

$$1^3 + \cdots + k^3 + (k+1)^3 = \left(\frac{k(k+1)}{2}\right)^2 + (k+1)^3 = (k+1)^2 \cdot \frac{k^2 + 4k + 4}{4} = \left(\frac{(k+1)(k+2)}{2}\right)^2.$$

Notice the **inventor's paradox** at work. The vaguer statement "the sum of cubes is always a perfect square" is harder to prove by induction than the sharper statement with the explicit formula. The more precise claim gives you something concrete at the inductive step. The stronger theorem is easier to prove.

### Counting subsets by induction

The same result $|\mathcal{P}(\{1, \ldots, n\})| = 2^n$ admits an inductive proof.

**Base case.** $n = 0$: the empty set has one subset (itself). $2^0 = 1$. True.

**Inductive step.** Assume a set with $k$ elements has $2^k$ subsets. Consider $\{1, \ldots, k, k+1\}$. Every subset either contains $k + 1$ or does not. Subsets not containing $k + 1$ are subsets of $\{1, \ldots, k\}$: there are $2^k$ by hypothesis. Subsets containing $k + 1$ are in bijection with subsets of $\{1, \ldots, k\}$: also $2^k$. Total: $2^{k+1}$.

Two proofs of the same fact (bijection with binary strings, and induction) are better than one. They illuminate different aspects and provide independent confirmation. "It is safe riding at two anchors."


## Reductio and indirect proof

Reductio ad absurdum shows the falsity of an assumption by deriving from it a manifest absurdity. Indirect proof establishes the truth of an assertion by showing the falsity of the opposite assumption. They are related but different.

"Reductio ad absurdum" has some resemblance to irony, which is the favorite procedure of the satirist. "Indirect proof" has some resemblance to a politician's trick of establishing a candidate by demolishing the reputation of his opponent. Not everyone likes these procedures. A few philosophers and many beginners dislike them. But they work.

### The idea

Sometimes you cannot see how to prove a statement directly. Instead, you assume the opposite and show that it leads to a contradiction. The key psychological move is to face squarely a hypothetical situation that you suspect is impossible, and to examine it closely enough to find the point that is definitely wrong.

Polya emphasized: the investigation, if it is well conducted, starts the same way whether you hope to find a solution or hope to show that no solution exists. You do not prejudge. You set up the equations, draw the consequences, and see where they lead.

### Infinitely many primes

Suppose the primes are finite, with $P$ the last. Form $Q = (2 \cdot 3 \cdot 5 \cdots P) + 1$. Then $Q$ is greater than $P$ and so not prime. But dividing $Q$ by any prime in the list leaves remainder $1$. Contradiction.

But the reductio can be rearranged. Given any finite set of primes, the number $Q$ is divisible by some prime not in that set. So no finite set of primes is complete. The content is the same; the presentation is direct. Once you have found an argument by reductio, ask: *Can you derive the result differently?* Often the reductio was scaffolding for a direct argument you can now see.

### A note on taste

A long reductio can become unbearable --- the words "hypothetically," "supposedly," "allegedly" must recur, and the inner discord between examining an impossible situation and wanting to reject it grows painful. Yet it would be foolish to repudiate reductio as a tool of discovery. Use it to find the argument. Then rearrange the argument for clarity.

Polya gave the reason plainly: listening to a reductio, you are obliged to focus your attention all the time upon a false assumption which you should forget, not upon the true theorem which you should retain. The direct proof retains truth. The reductio stores falsehoods that you must eventually discard.


## Questions to keep

- *Can you see clearly that the step is correct? Can you also prove it?*
- *Did you use the whole hypothesis? Did you use all the data?*
- *If you found it by reductio, can you rearrange the argument into a direct proof?*
- *Is your inductive hypothesis precise enough --- or does the inventor's paradox apply?*
