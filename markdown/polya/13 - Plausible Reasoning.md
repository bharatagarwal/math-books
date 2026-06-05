# Plausible Reasoning

Mathematics presented with rigor is a systematic deductive science. But mathematics in the making is an experimental inductive science. The gap between the two is where all discovery happens. You guess before you prove. You accumulate evidence before you have certainty. You reason plausibly before you reason strictly. If you refuse to guess, you will never discover anything. If you mistake your guess for a proof, you will discover things that are not true. The discipline is to do both: guess freely, then prove rigorously, and never confuse the two.

## Heuristic reasoning

Heuristic reasoning is reasoning not regarded as final and strict but as provisional and plausible only, whose purpose is to discover the solution of the present problem. You are often obliged to use it. You will attain complete certainty when you have the complete solution, but before that you must often be satisfied with a more or less plausible guess. You need heuristic reasoning when you construct a strict proof as you need scaffolding when you erect a building.

Heuristic reasoning is good in itself. What is bad is to mix up heuristic reasoning with rigorous proof. What is worse is to sell heuristic reasoning for rigorous proof.

Consider the difference in practice. When you are devising a plan, anything is right that leads to the right idea. You follow analogy, you try special cases, you guess. But when you start carrying out the plan, you accept only conclusive, strict arguments. The more painstakingly you check your steps when carrying out the plan, the more freely you may use heuristic reasoning when devising it.

This is a bargain you make with yourself. The freedom of the guess and the discipline of the proof are not enemies. They depend on each other.

## Induction before proof

Induction here means the empirical kind: observing particular cases and guessing a general law. Not mathematical induction (the proof technique), though the two often work together. You discover a pattern by induction, then you prove it by mathematical induction.

Here is the classic example. You compute a few sums of consecutive cubes:

$$1 = 1^2, \quad 1 + 8 = 9 = 3^2, \quad 1 + 8 + 27 = 36 = 6^2.$$

It is hard to believe all these sums are perfect squares by mere chance. You look at the bases: $1, 3, 6$. The differences are $2, 3$. The pattern is unmistakable — these are triangular numbers. You conjecture:

$$1^3 + 2^3 + \cdots + n^3 = (1 + 2 + \cdots + n)^2.$$

Notice what happened. "The sums seem to be squares" is vague. "The sum of the first $n$ cubes equals the square of the $n$-th triangular number" is precise. The precise statement is stronger, yet easier to prove — it gives you something definite to grab hold of. This is the inventor's paradox applied to conjectures: a more ambitious, more precise conjecture is often easier to prove than a vague one.

The same pattern appears in counting. Suppose you enumerate the subsets of an $n$-element set:

| $n$ | Subsets | Count |
|---|---|---|
| 0   | $\{\emptyset\}$ | 1 |
| 1   | $\emptyset, \{a\}$ | 2 |
| 2   | $\emptyset, \{a\}, \{b\}, \{a,b\}$ | 4 |
| 3   | all eight | 8 |

You conjecture that the count is $2^n$. This is induction. The proof — by bijection with binary strings, or by mathematical induction on $n$ — comes later. But the conjecture came first, and the conjecture came from looking at cases.

In mathematics as in the physical sciences, you may use observation and induction to discover general laws. But there is a difference. In the physical sciences, there is no higher authority than observation and induction. In mathematics there is such an authority: rigorous proof.

This creates a two-phase rhythm. In the first phase, you work experimentally: compute, tabulate, guess. In the second phase, you work rigorously: prove or disprove. The transition between phases is itself a skill. As Polya put it: "Mathematics presented with rigor is a systematic deductive science but mathematics in the making is an experimental inductive science." The two descriptions are not contradictory. They describe the same subject at different stages of its development.

The danger is to confuse the stages. To present the finished product as if it were discovered in the order in which it is proved is to conceal the real process. To present the experimental phase as if it constituted proof is to lower your standards. Both are dishonest in different ways.

## Analogy as evidence

Analogy is a sort of similarity. Similar objects agree with each other in some respect; analogous objects agree in certain relations of their respective parts.

You know that the number of binary strings of length $n$ is $2^n$. You suspect a bijection between subsets of an $n$-element set and binary strings of length $n$ — the $i$-th bit indicates whether element $i$ is in the subset. If such a bijection exists, the two counts must agree. They do. The analogy between subsets and binary strings is not vague resemblance; it is an isomorphism. It pushes the conjecture toward certainty. And the bijection itself, once made explicit, becomes the proof.

This is the strongest kind of analogy: a precise structural correspondence. But weaker analogies also have evidential force. If you have proved a result about trees and wonder whether something similar holds for forests, you are reasoning by analogy. The analogy does not prove anything. But it tells you where to look.

An analogical conclusion from many parallel cases is stronger than one from fewer. Yet quality matters more than quantity. Clear-cut analogies weigh more heavily than vague similarities. "It would be foolish to regard the plausibility of such conjectures as certainty, but it would be just as foolish, or even more foolish, to disregard such plausible conjectures."

## Why plausible is not certain

Plausible reasoning has a definite logical structure. It is not the same as demonstrative reasoning, and the difference matters.

Consider the two side by side:

$$
\begin{array}{ccc}
\textit{Demonstrative} & \qquad & \textit{Heuristic} \\
\text{If } A \text{ then } B & & \text{If } A \text{ then } B \\
B \text{ false} & & B \text{ true} \\
\hline
A \text{ false} & & A \text{ more credible}
\end{array}
$$

The demonstrative pattern is watertight: if $A$ implies $B$ and $B$ is false, then $A$ is false. This is modus tollens.

The heuristic pattern is not watertight. If $A$ implies $B$ and $B$ turns out to be true, that does not prove $A$. It only makes $A$ more credible. The direction is determined by the premises: $A$ becomes more credible, certainly not less. But the magnitude — how much more credible — depends on context, on what else you know, on how surprising $B$ was.

This is the deepest difference. In a demonstrative syllogism, the premises constitute a full basis for the conclusion. New information that leaves the premises intact cannot shake the conclusion.

In a heuristic syllogism, the premises constitute only part of the basis — the visible part. There is also an invisible part: your background knowledge, your unstated reasons. It can happen that you receive new information that leaves both premises intact but makes $A$ appear less plausible, or even definitively refutes it. The conclusion may be overturned by commotions in the invisible parts of its foundation, even though the visible premises stand firm.

Two reasonable people can honestly disagree about how much more credible $A$ becomes, since their backgrounds, temperaments, and unstated reasons differ. This is fundamentally unlike demonstrative reasoning, where the premises leave no room for disagreement about the conclusion.

Columbus's men saw birds and floating seaweed and concluded they were probably approaching land. They were right to conclude this, even though they were wrong several times before they were finally right. The signs did not constitute proof. But it would have been foolish to ignore them. The crucial point: the conclusion of a heuristic syllogism is not certain. It can be overturned by new evidence. Your guess may be wrong. But "no idea is really bad, unless we are uncritical. What is really bad is to have no idea at all."

## The heuristic syllogism in practice

You use the heuristic syllogism constantly, whether you name it or not.

**Verification of consequences.** You conjecture that the number of subsets of $\{1, 2, \ldots, n\}$ is $2^n$. If true, the number of subsets of $\{1, 2, 3, 4, 5\}$ should be $32$. You enumerate and find $32$. More credible. You check whether the formula satisfies the recurrence $f(n) = 2f(n-1)$. It does. More credible still. Nothing is proved, but the ground is prepared for proof.

**Analogy as heuristic evidence.** You know the number of binary strings of length $n$ is $2^n$. You suspect a bijection between subsets and binary strings. If such a bijection exists, the counts must agree. They do. This pushes the conjecture toward certainty — and the bijection, once explicit, becomes the proof.

**The pattern that breaks.** You conjecture that every prime $p$ satisfies $2^p - 2 \equiv 0 \pmod{p}$. You check $p = 2, 3, 5, 7, 11, 13$. All work. Then you ask the converse: is every $n$ with $2^n - 2 \equiv 0 \pmod{n}$ necessarily prime? You find $n = 341 = 11 \times 31$ passes the test but is composite. The converse is false. This does not destroy Fermat's little theorem, but it destroys a plausible extension of it.

In each case, the reasoning has the same structure: if the conjecture is true, a certain consequence should hold. The consequence holds (or fails). The conjecture becomes more (or less) credible. Nothing is proved. But the work has direction.

## Why conjectures need proofs

Euler was the great mathematician who most freely showed how he found his results. He computed dozens of special cases. He tabulated. He noticed patterns, conjectured formulas, tested them, and only then attempted proofs. Sometimes the proof eluded him for years. But the conjecture, supported by overwhelming inductive evidence, would stand and eventually be proved by others. Polya wrote: "He explained how he found his results... of the great mathematicians, the one who influenced me most."

What Polya learned from Euler was not a technique but a stance: compute, tabulate, conjecture, test, prove. In that order.

Lakatos pushed this further. In *Proofs and Refutations*, he traced how Euler's polyhedron formula $V - E + F = 2$ evolved through counterexamples and refinements — the proof and the theorem developed together. Counterexamples did not kill the theorem; they sharpened it. Definitions evolved alongside proofs. "Polyhedron" did not have a fixed meaning that preceded the investigation. The meaning was partly determined by which theorem you wanted to prove.

This demolishes the textbook myth that mathematics proceeds by stating a definition, then a theorem, then a proof, in one clean pass. The real process is:

1. You notice a pattern (induction).
2. You conjecture a statement.
3. You attempt a proof.
4. You find a counterexample or a gap.
5. You refine the conjecture, the proof, or the definitions.
6. You try again.

This cycle is plausible reasoning in action. Steps 1 and 2 are not rigorous. Step 3 attempts rigor. Steps 4 and 5 are where the real learning happens. Without plausible reasoning, you have nothing to prove. Without proof, you have nothing you can build on.

The relationship between plausible reasoning and proof is not adversarial. The freedom of the guess and the discipline of the proof depend on each other. "No idea is really bad, unless we are uncritical. What is really bad is to have no idea at all."

## Questions to keep

- *What would have to be true if this conjecture is right?* Derive consequences and check them.
- *Are you confusing plausible with certain?* The heuristic syllogism points a direction; it does not fix a destination.
- *Can you sharpen the analogy?* A vague resemblance suggests where to look. A precise correspondence becomes the proof.
- *Is this evidence or is this proof?* Name which one you are doing. The freedom to guess depends on never selling the guess as the proof.
