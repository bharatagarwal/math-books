# Plausible Reasoning

Mathematics presented with rigor is a systematic deductive science. But mathematics in the making is an experimental inductive science. The gap between the two is where all discovery happens. You guess before you prove. You accumulate evidence before you have certainty. You reason plausibly before you reason strictly. If you refuse to guess, you will never discover anything. If you mistake your guess for a proof, you will discover things that are not true. The discipline is to do both: guess freely, then prove rigorously, and never confuse the two.

## Heuristic reasoning

Heuristic reasoning is reasoning not regarded as final and strict but as provisional and plausible only, whose purpose is to discover the solution of the present problem. You are often obliged to use it. You will attain complete certainty when you have the complete solution, but before that you must often be satisfied with a more or less plausible guess. You need the provisional before you attain the final. You need heuristic reasoning when you construct a strict proof as you need scaffolding when you erect a building.

This is not a new idea. The study of heuristic---the methods and rules of discovery and invention---has a long intellectual lineage. Pappus, around 300 AD, described an "Art of Solving Problems" in his *Collectiones* and gave the first clear account of working backwards from what is sought to what is known. Descartes planned a universal method for solving problems; he left his *Rules for the Direction of the Mind* unfinished, but what survives contains more about discovery than his better-known *Discours de la Méthode*. He wrote: "As a young man, when I heard about ingenious inventions, I tried to invent them by myself, even without reading the author. In doing so, I perceived, by degrees, that I was making use of certain rules." Leibniz planned an "Art of Invention" he never completed, but fragments show he understood the stakes: "Nothing is more important than to see the sources of invention which are, in my opinion, more interesting than the inventions themselves." Bolzano devoted nearly 300 pages of his *Wissenschaftslehre* to heuristic, writing with characteristic modesty: "I do not think at all that I am able to present here any procedure of investigation that was not perceived long ago by all men of talent... But I shall take pains to state in clear words the rules and ways of investigation which are followed by all able men, who in most cases are not even conscious of following them."

> **Aside: Bolzano (1781--1848).** Logician and mathematician. His heuristic, buried in the third volume of a comprehensive logic treatise, runs to nearly 300 pages. He attempted what Descartes and Leibniz planned but never finished: to state the rules of discovery in clear words. Polya regarded him as one of the few who took the project seriously.

After these early attempts, the subject went dormant. Ernst Mach, the physicist and philosopher, revived interest in the psychology of discovery. Jacques Hadamard studied the mental operations of mathematicians. William James and Wolfgang Kohler contributed from psychology. Polya drew on all of them. Heuristic reasoning is not an invention of any single thinker; it is a practice as old as problem-solving itself, periodically rediscovered and restated.

> **Aside: Descartes (1596--1650).** Great mathematician and philosopher. His *Rules for the Direction of the Mind*, found unfinished in his manuscripts and printed after his death, contains more interesting material on problem-solving than the better-known *Discours de la Méthode*. The "Rules" were written first; the "Discours" is a distillation and simplification. The origin of the work, as Descartes described it: "As a young man, when I heard about ingenious inventions, I tried to invent them by myself, even without reading the author. In doing so, I perceived, by degrees, that I was making use of certain rules." This is the heuristic impulse in its purest form: the attempt to make explicit the tacit rules that skilled problem-solvers follow without knowing it.

Heuristic reasoning is good in itself. What is bad is to mix up heuristic reasoning with rigorous proof. What is worse is to sell heuristic reasoning for rigorous proof.

Consider the difference in practice. When you are devising a plan, anything is right that leads to the right idea. You follow analogy, you try special cases, you guess. But when you start carrying out the plan, you accept only conclusive, strict arguments. The more painstakingly you check your steps when carrying out the plan, the more freely you may use heuristic reasoning when devising it.

This is a bargain you make with yourself. The freedom of the guess and the discipline of the proof are not enemies. They depend on each other.

A heuristic argument presented with taste and frankness may be useful; it may prepare for the rigorous argument of which it usually contains certain germs. But a heuristic argument is likely to be harmful if it is presented ambiguously, with visible hesitation between shame and pretension. The teaching of many subjects could be improved if the nature of heuristic reasoning were better understood---its advantages and its limitations openly recognized---and if textbooks would present heuristic arguments openly, clearly labeled as what they are.

## Induction before proof

Induction here means the empirical kind: observing particular cases and guessing a general law. It is not mathematical induction (the proof technique), though the two often work together. You discover a pattern by induction, then you prove it by mathematical induction.

Here is the classic example. You compute a few sums of consecutive cubes:

$$
\begin{aligned}
1 &= 1 = 1^2 \\
1 + 8 &= 9 = 3^2 \\
1 + 8 + 27 &= 36 = 6^2 \\
1 + 8 + 27 + 64 &= 100 = 10^2 \\
1 + 8 + 27 + 64 + 125 &= 225 = 15^2.
\end{aligned}
$$

It is hard to believe that all these sums are perfect squares by mere chance. You look at the bases of the squares: $1, 3, 6, 10, 15$. The differences between successive terms are $2, 3, 4, 5$. The pattern is now unmistakable:

$$1^3 + 2^3 + 3^3 + \cdots + n^3 = (1 + 2 + 3 + \cdots + n)^2.$$

This was found by induction. The manner in which it was found tells you something about induction itself: it tries to find regularity and coherence behind observations. Its instruments are generalization, specialization, and analogy. A tentative generalization starts from an effort to understand the observed facts, is based on analogy, and is tested by further special cases.

Notice what happened between the first conjecture and the second. "The sums seem to be squares" is vague. "The sum of the first $n$ cubes equals the square of the $n$-th triangular number" is precise. The precise statement is stronger---it implies the vague one immediately. Yet the precise statement is easier to prove, because it gives you something definite to grab hold of. This is the inventor's paradox applied to conjectures: a more ambitious, more precise conjecture is often easier to prove or disprove than a vague one. The vague conjecture ("these are squares") does not suggest a clear path to proof. The precise one ("these are squares of triangular numbers") practically hands you the induction step.

The same pattern appears in discrete math constantly. Suppose you are counting the subsets of an $n$-element set. You enumerate:

| $n$ | Number of subsets |
|-----|-------------------|
| 0   | 1                 |
| 1   | 2                 |
| 2   | 4                 |
| 3   | 8                 |
| 4   | 16                |

You conjecture that the number of subsets is $2^n$. This is induction. The proof (by bijection with binary strings, or by mathematical induction on $n$) comes later. But the conjecture came first, and the conjecture came from looking at cases.

The point is not that you should trust small-case evidence blindly. The point is that you should collect it deliberately. Enumerate. Tabulate. Look for the pattern. Then prove it or disprove it.

In mathematics as in the physical sciences, you may use observation and induction to discover general laws. But there is a difference. In the physical sciences, there is no higher authority than observation and induction. In mathematics there is such an authority: rigorous proof.

This creates a two-phase rhythm. In the first phase, you work experimentally: compute, tabulate, guess. In the second phase, you work rigorously: prove or disprove. The transition between phases is itself a skill. After working experimentally for a while, it may be good to change your point of view. You have discovered an interesting result, but the reasoning that led to it was merely plausible, experimental, provisional, heuristic. Now try to establish it definitively by a rigorous proof.

Many mathematical results were found by induction first and proved later. The sum-of-cubes formula is one example. The distribution of primes is another: the prime number theorem was conjectured from numerical tables by Gauss when he was fifteen, decades before anyone could prove it. The experimental phase is not a lesser phase. It is the phase in which the interesting results are found. As Polya put it: "Mathematics presented with rigor is a systematic deductive science but mathematics in the making is an experimental inductive science." The two descriptions are not contradictory. They describe the same subject at different stages of its development. The finished product is deductive. The process of creating it is inductive.

The danger is to confuse the stages. To present the finished product as if it were discovered in the order in which it is proved is to conceal the real process. To present the experimental phase as if it constituted proof is to lower your standards. Both are dishonest in different ways.

## Analogy as evidence

Analogy is a sort of similarity. Similar objects agree with each other in some respect; analogous objects agree in certain relations of their respective parts.

The power of analogy for discovery is enormous. You know that the number of binary strings of length $n$ is $2^n$. You suspect that there is a bijection between subsets of an $n$-element set and binary strings of length $n$ (the $i$-th bit indicates whether element $i$ is in the subset). If such a bijection exists, the two counts must agree. They do. The analogy between subsets and binary strings is not a vague resemblance; it is an isomorphism---a one-to-one correspondence preserving the relevant structure. It pushes the conjecture toward certainty. And the bijection itself, once made explicit, becomes the proof.

This is the strongest kind of analogy: a precise structural correspondence. But weaker analogies also have evidential force. If you have proved a result about trees (connected acyclic graphs) and you wonder whether something similar holds for forests (acyclic graphs that need not be connected), you are reasoning by analogy. If you know that every tree on $n$ vertices has exactly $n - 1$ edges and you wonder whether there is a similarly tight relationship for connected planar graphs, you are reasoning by analogy. The analogy does not prove anything. But it tells you where to look.

An analogical conclusion from many parallel cases is stronger than one from fewer. Yet quality matters more than quantity. Clear-cut analogies weigh more heavily than vague similarities. Systematically arranged instances count for more than random collections of cases. Polya distinguishes three levels of precision in analogy:

1. Two systems of objects are governed by the same laws in certain relations---a structural parallel.
2. There is a one-to-one correspondence preserving those relations---an isomorphism.
3. There is a many-to-one correspondence preserving those relations---a homomorphism.

The subset/binary-string example is at level 2. Most analogies that arise in discovery are at level 1, where the parallel is real but the correspondence is not yet nailed down. Your job is to sharpen the analogy from level 1 toward level 2, because that sharpening is the proof.

Here is a concrete illustration. You know that the number of ways to choose $k$ items from $n$ is $\binom{n}{k}$. You know that the number of subsets of an $n$-element set is $2^n$. Is there a connection? You notice that every subset corresponds to a sequence of $n$ binary choices (include or exclude each element), and that a subset of size $k$ corresponds to a binary string with exactly $k$ ones. Therefore:

$$\sum_{k=0}^{n} \binom{n}{k} = 2^n.$$

This is the binomial theorem at $x = 1$. The analogy between "choosing subsets" and "choosing binary strings" is what drove the discovery. The bijection is what made it rigorous.

Inference by analogy appears to be the most common kind of conclusion, and it is possibly the most essential kind. It yields more or less plausible conjectures which may or may not be confirmed by experience and stricter reasoning.

"It would be foolish to regard the plausibility of such conjectures as certainty, but it would be just as foolish, or even more foolish, to disregard such plausible conjectures."

## Examine your guess

You have a guess. Perhaps it came from tabulating cases, perhaps from analogy, perhaps from a vague feeling that something ought to be true. What do you do with it?

Your guess may be right, but it is foolish to accept a vivid guess as a proven truth---as primitive people often do. Your guess may be wrong. But it is also foolish to disregard a vivid guess altogether---as pedantic people sometimes do. Guesses of a certain kind deserve to be examined and taken seriously: those which occur after you have attentively considered and really understood a problem in which you are genuinely interested. Such guesses usually contain at least a fragment of the truth although, of course, they very seldom show the whole truth. Yet there is a chance to extract the whole truth if you examine such a guess appropriately.

Many a guess has turned out to be wrong but nevertheless useful in leading to a better one.

"No idea is really bad, unless we are uncritical. What is really bad is to have no idea at all."

Polya tells the story of Mr. John Jones, who suspected that Director Brown was responsible for his failure to get a raise. The suspicion was not unreasonable---there were some signs pointing to Director Brown. The real mistake was that, after conceiving the suspicion, Mr. Jones became blind to all signs pointing in the opposite direction. He worried himself into firmly believing it and behaved so stupidly that he almost succeeded in making a real enemy of the director. The trouble with Mr. Jones is that he behaves like most of us: he never questions his opinions, major or minor, as long as he has them. At best, he could examine only a few of his convictions---and he never does. Don't do as Mr. John Jones does. Don't let your guess grow without examination till it becomes ineradicable. At any rate, in theoretical matters, the best of ideas is hurt by uncritical acceptance and thrives on critical examination.

The practical discipline is this:

1. **Face it.** Do not let the guess float unexamined. State it explicitly, in precise terms. A vague feeling that "these sums seem to be squares" becomes the conjecture $1^3 + 2^3 + \cdots + n^3 = (1 + 2 + \cdots + n)^2$. The act of stating it forces you to commit, and a committed conjecture is one you can test.

2. **Derive consequences.** If the conjecture is true, what else must be true? The conjecture $|\text{subsets of } \{1, \ldots, n\}| = 2^n$ implies that $|\text{subsets of } \{1, \ldots, n+1\}| = 2 \cdot |\text{subsets of } \{1, \ldots, n\}|$. Check whether that recurrence holds. Each confirmed consequence makes the conjecture more credible.

3. **Switch from problem-to-find to problem-to-prove.** Originally you had a problem to find: what is the pattern? After stating your guess, the situation changes. You now have a problem to prove: is this conjecture true? The shift in framing is important. A problem-to-find is open-ended. A problem-to-prove has a definite target.

4. **Try to break it.** Look for counterexamples. Try the simplest cases first, then extreme cases. A single counterexample kills the conjecture. But even a failed attempt to break it teaches you something about why it might be true.

5. **Refine.** If the guess survives testing but is too vague to prove, sharpen it. If it breaks, ask what fragment of it survived. The broken guess may point to the right guess.

This cycle---state, test, break, refine---is not a detour from mathematics. It is how mathematics is made.

Consider a concrete case from combinatorics. You are asked: of all graphs on $n$ vertices with exactly $m$ edges, which has the most triangles? You might guess: the one where the edges are concentrated as densely as possible---a complete graph on some subset plus remaining edges. If you take this guess seriously, state it precisely. What does "concentrated as densely as possible" mean? The act of forcing yourself to be precise may lead you to the Kruskal-Katona theorem, or it may lead you to a counterexample. Either way, the guess has moved you forward.

Or consider a simpler case. Of all quadrilaterals with a given perimeter, which has the greatest area? You might guess: the square. If you take this guess seriously, you should realize what it means. State it: "Of all quadrilaterals with given perimeter the square has the greatest area." Now the situation changes. Originally you had a problem to find. After formulating the guess, you have a problem to prove.

If the full problem is too hard, try a part: "Of all rectangles with given perimeter the square has the greatest area." Restate it algebraically. A rectangle with sides $a$ and $b$ has area $ab$. The square with the same perimeter has side $\frac{a+b}{2}$ and area $\left(\frac{a+b}{2}\right)^2$. You need to show $\left(\frac{a+b}{2}\right)^2 \geq ab$, which is equivalent to $(a - b)^2 \geq 0$. True, with equality only when $a = b$. You have not solved the full problem, but you have made progress just by facing your guess squarely.

## Why plausible is not certain

Plausible reasoning has a definite logical structure. It is not the same as demonstrative reasoning, and the difference matters.

Consider a demonstrative syllogism and a heuristic syllogism side by side:

$$
\begin{array}{ccc}
\textit{Demonstrative} & \qquad & \textit{Heuristic} \\
\text{If } A \text{ then } B & & \text{If } A \text{ then } B \\
B \text{ false} & & B \text{ true} \\
\hline
A \text{ false} & & A \text{ more credible}
\end{array}
$$

The demonstrative pattern is watertight: if $A$ implies $B$ and $B$ is false, then $A$ is false. Period. This is modus tollens.

The heuristic pattern is not watertight. If $A$ implies $B$ and $B$ turns out to be true, that does not prove $A$. It only makes $A$ more credible. The conclusion of the heuristic syllogism is "comparable to a force, has direction and magnitude." The direction is determined by the premises: $A$ becomes more credible, certainly not less. But the magnitude---how much more credible $A$ becomes---is not determined by the premises alone. It depends on context, on what else you know, on how surprising $B$ was.

This is the deepest difference between demonstrative and plausible reasoning. In a demonstrative syllogism, the premises constitute a full basis for the conclusion. If both premises stand, the conclusion stands. New information that leaves the premises intact cannot shake the conclusion.

In a heuristic syllogism, the premises constitute only part of the basis---the visible part. There is also an invisible part: your background knowledge, your inarticulate feelings, your unstated reasons. It can happen that you receive new information that leaves both premises completely intact but influences your trust in $A$ in the direction opposite to the conclusion. Tomorrow you may find grounds, not interfering at all with these premises, that make $A$ appear less plausible, or even definitively refute it. The conclusion may be overturned by commotions in the invisible parts of its foundation, even though the premises---the visible part---stand firm.

This is exactly the structure of scientific evidence, of debugging, of conjecture in mathematics. You hypothesize that a function has a bug ($A$). If it does, a particular test case should fail ($B$). The test case fails. You have not proved the bug exists in that function, but the hypothesis is now more credible.

Columbus's men saw birds and floating seaweed and concluded they were probably approaching land. They were right to conclude this, even though they were wrong several times before they were finally right. The signs did not constitute proof. But it would have been foolish to ignore them.

For any reasonable person, the premises of the heuristic syllogism imply that $A$ becomes more credible (certainly not less credible). Yet two reasonable people can honestly disagree about how much more credible $A$ becomes, since their temperaments, their backgrounds, and their unstated reasons may be different. This is fundamentally unlike demonstrative reasoning, where the premises leave no room for disagreement about the conclusion.

The crucial point: the conclusion of a heuristic syllogism is not certain. It can be overturned by new evidence. Your guess may be wrong. But "no idea is really bad, unless we are uncritical. What is really bad is to have no idea at all."

## Extreme cases test the rule

When you are collecting evidence for or against a conjecture, not all evidence is equal. Extreme cases---unusual, boundary, degenerate cases---provide stronger inductive evidence than ordinary ones. Why?

Because extreme cases are the most likely to be counterexamples. If a general statement is supposed to apply to all mammals, it must apply even to such an unusual mammal as the whale. If it holds even there, the evidence is strong precisely because the prospect of refutation was strong. "Prospective exceptions test the rule."

In the subset-counting example: the extreme case $n = 0$ (the empty set has exactly one subset, namely itself) is the one most likely to trip up a careless formula. That $2^0 = 1$ matches this boundary case is worth more than the confirmation at $n = 4$.

In number theory: you conjecture that every prime $p$ satisfies $2^p - 2 \equiv 0 \pmod{p}$. You check the ordinary primes $2, 3, 5, 7, 11, 13$. All work. But the real test is to ask the converse: is every $n$ with $2^n - 2 \equiv 0 \pmod{n}$ necessarily prime? The answer is no: $n = 341 = 11 \times 31$ is a pseudoprime, a composite number that passes this particular test. The extreme case---a composite that mimics primality---is where the conjecture would break if it were going to break.

When you test a conjecture, do not only check the cases that confirm it. Actively seek the cases most likely to destroy it. If the conjecture survives the hardest tests, the evidence is worth far more than a hundred easy confirmations.

The same principle applies to checking a formula. If your formula for the number of edges in a complete graph is $\binom{n}{2}$, the extreme case $n = 1$ (zero edges) and the trivial case $n = 2$ (one edge) are worth checking first. These are the cases where off-by-one errors, wrong base cases, and sign mistakes are most visible. If the formula survives the boundary, it has earned some trust.

More generally: the habit of testing extreme cases is a form of plausible reasoning applied to your own work. You are asking: "If my formula is wrong, where is it most likely to fail?" And you go there first.

## Euler showing his work

Among the great mathematicians, Euler was the one who most freely showed how he found his results. He did not merely state and prove; he explained the guesses, the analogies, the inductive evidence that led him to the theorem. This is why Euler is so instructive, and why Polya regarded him as the greatest influence on his own thinking about discovery.

Euler would compute dozens of special cases. He would tabulate. He would notice patterns, conjecture formulas, test them against further cases, and only then attempt proofs. Sometimes the proof eluded him for years. Sometimes it eluded him permanently. But the conjecture, supported by overwhelming inductive evidence, would stand and eventually be proved by others.

Consider the Basel problem. Euler wanted the exact value of $\sum_{k=1}^{\infty} 1/k^2$. He computed partial sums numerically:

$$
\begin{aligned}
\sum_{k=1}^{10} \frac{1}{k^2} &= 1.5497677\ldots \\
\sum_{k=1}^{100} \frac{1}{k^2} &= 1.6349839\ldots \\
\sum_{k=1}^{1000} \frac{1}{k^2} &= 1.6439345\ldots
\end{aligned}
$$

He computed many decimal places and recognized the limit as $\pi^2 / 6 = 1.6449340\ldots$. He published the conjecture in 1735, supported by this numerical evidence and a brilliant but nonrigorous argument: he factored $\sin(x)/x$ as an infinite product over its roots, expanded both sides as power series, and compared coefficients. The argument was inspired---and logically incomplete. He gave a rigorous proof later, in 1741. The conjecture came first. The evidence was plausible reasoning of exactly the kind described in this chapter. The proof came years later.

Euler also showed something else: he was willing to be wrong in public. He published conjectures that turned out to be false. He published incomplete proofs. He was not embarrassed by this because he understood that discovery requires risk. A conjecture is a bet, and some bets lose. The alternative---never conjecturing, never guessing, waiting for certainty before speaking---produces nothing.

Euler also published his failures and partial results. When he could not prove a conjecture, he said so and published the evidence. When a proof turned out to have gaps, he went back and tried again. This willingness to work in public, showing the scaffolding alongside the building, is what makes his collected works an unparalleled education in mathematical discovery.

Polya wrote: "He explained how he found his results... of the great mathematicians, the one who influenced me most." What Polya learned from Euler was not a technique but a stance: compute, tabulate, conjecture, test, prove. In that order. And if the proof does not come, publish the conjecture anyway, with the evidence. Somebody else may find the proof. The conjecture itself is a contribution.

## Lakatos and proofs/refutations

Imre Lakatos, a Hungarian philosopher of mathematics, took Polya's ideas about discovery and pushed them further. In *Proofs and Refutations* (1976), Lakatos told the history of Euler's polyhedron formula $V - E + F = 2$ as a dialogue. The point of the dialogue was that the proof and the theorem evolved together. Counterexamples did not kill the theorem; they refined it.

What Lakatos showed, in meticulous detail, is that the process has a specific structure. When a counterexample appears, there are distinct responses:

- **Monster-barring:** You declare the counterexample is not a "real" polyhedron. The definition is adjusted to exclude it. (A picture frame is not a polyhedron; it has a hole.)
- **Exception-barring:** You add a condition to the theorem. (The formula holds for *convex* polyhedra.)
- **Monster-adjusting:** You reinterpret the counterexample so that it actually does satisfy the formula, by recounting vertices, edges, or faces.
- **Lemma-incorporation:** You trace the failure to a specific step in the proof, then modify the proof and the theorem together so the step goes through.

The crucial insight is that the definitions evolve alongside the proofs. "Polyhedron" does not have a fixed meaning that precedes the investigation. The meaning of "polyhedron" is partly determined by which theorem you want to prove about polyhedra. The proof shapes the definition as much as the definition shapes the proof.

This matters because it demolishes the textbook myth that mathematics proceeds by stating a definition, then a theorem, then a proof, cleanly, in one pass. Definitions are not handed down from above. They are negotiated in the course of trying to prove things. The definition of "continuous function," the definition of "limit," the definition of "polyhedron"---all were shaped by the theorems people were trying to prove about them. The real process is:

1. You notice a pattern (induction).
2. You conjecture a statement.
3. You attempt a proof.
4. You find a counterexample or a gap.
5. You refine the conjecture, the proof, or the definitions.
6. You try again.

This cycle is plausible reasoning in action. Steps 1 and 2 are not rigorous. Step 3 attempts rigor. Steps 4 and 5 are where the real learning happens. The back-and-forth between conjecture and refutation is what produces understanding.

Lakatos's work grew directly from Polya's. Polya suggested the topic. Lakatos translated *How to Solve It* into Hungarian. Both were part of a Hungarian mathematical tradition---running from Polya through Renyi to Lakatos---that took the process of discovery as seriously as its products.

> **Aside: Lakatos (1922--1974).** Hungarian philosopher of mathematics and science. Student of Polya at Stanford. His doctoral thesis, supervised by Polya, became *Proofs and Refutations*. He later moved to the London School of Economics and applied the same evolutionary view to the philosophy of science. The core idea---that concepts are refined through the process of proving theorems about them, not fixed in advance---connects directly to Polya's insistence that you must guess before you prove.

The connection is not accidental. Polya described the psychology of discovery. Lakatos described the sociology and history of it. Both insisted on the same point: plausible reasoning is not a failure mode of mathematics. It is how mathematics is made.

## The heuristic syllogism in practice

The heuristic syllogism is not an abstract curiosity. You use it constantly, whether you name it or not.

Every time you check a special case of a conjecture, you are running a heuristic syllogism. Every time you verify that a formula gives the right answer for $n = 1$, you are reasoning: "If the formula is correct, it should give the right answer for $n = 1$. It does. Therefore, the formula is more credible." Every time an analogy between two structures clicks into place, you are reasoning: "If these structures are truly analogous, then the theorem that holds for one should hold for the other. It does. Therefore, the analogy is more credible."

The reasoning does not prove anything. But it guides the work. It tells you which paths are worth pursuing and which are dead ends. It is the compass, not the destination.

Here are the specific forms it takes in mathematical work.

**Verification of consequences.** You conjecture that the number of subsets of $\{1, 2, \ldots, n\}$ is $2^n$. If this is true, then the number of subsets of $\{1, 2, 3, 4, 5\}$ should be $32$. You enumerate and find $32$. The conjecture is now more credible. You check $n = 6$: you get $64 = 2^6$. More credible still. You check whether the formula satisfies the recurrence $f(n) = 2 f(n-1)$ (each element is either in or out of a subset, doubling the count). It does. The conjecture is now very credible. You have not proved it, but you have a strong inductive basis.

**Analogy as heuristic evidence.** You know that the number of binary strings of length $n$ is $2^n$. You suspect a bijection between subsets and binary strings. If such a bijection exists, the two counts must agree. They do. This analogical evidence pushes the conjecture toward certainty---and the bijection itself, once made explicit, becomes the proof.

**The pattern that breaks.** You conjecture that every prime $p$ satisfies $2^p - 2 \equiv 0 \pmod{p}$. You check: $p = 2, 3, 5, 7, 11, 13$. All work. But then you ask: is the converse true? Is every $n$ with $2^n - 2 \equiv 0 \pmod{n}$ necessarily prime? You check $n = 341 = 11 \times 31$ and find that $2^{341} - 2 \equiv 0 \pmod{341}$. The converse is false. This is a counterexample---a refutation in Lakatos's sense. It does not destroy the original theorem (Fermat's little theorem), but it destroys a plausible extension of it.

**Signs of progress.** When you are deep in a problem and a heuristic conclusion arrives---a new datum brought into play, a clause of the condition appropriately used, an analogy that clicks---it functions as a sign of progress, like the birds and floating seaweed that Columbus's men saw before sighting land. The reasoning has the same structure: if you are approaching the solution, you would expect to see such signs. You see them. Therefore, it becomes more credible that you are approaching the solution.

Why are heuristic conclusions signs of progress? Because they indicate that a typical operation has succeeded. There are certain mental operations typically useful in solving problems: connecting a new datum to the unknown, satisfying another clause of the condition, finding an analogy with a solved problem. When such an operation succeeds, you have reason to believe the work is moving. When operations succeed repeatedly, the signs multiply---as they did for Columbus's men on October 11, 1492, the day before they sighted land.

Schoenfeld formalized this observation into a theory of metacognition: the solver who monitors such signs, deciding consciously whether to persist, switch, or rest, solves problems more reliably than the solver who plunges ahead without reflection.

In each case, the reasoning has the same structure: if the conjecture is true, then a certain consequence should hold. The consequence holds (or fails). The conjecture becomes more (or less) credible. Nothing is proved. But the ground is prepared for proof.

The signs of progress are heuristic. Should you trust them? Should you follow them? Follow, but keep your eyes open. Trust, but look. And never renounce your judgment. If you take a heuristic conclusion as certain, you may be fooled and disappointed. But if you neglect heuristic conclusions altogether, you will make no progress at all.

The expert has no more ideas than the inexperienced, perhaps. But the expert appreciates more what he has and uses it better. The expert reads the signs---notices when a datum has been brought into play, when a clause of the condition has been satisfied, when an analogy has emerged---where the novice sees nothing. The main advantage of the exceptionally talented may consist in a sort of extraordinary mental sensibility: they feel subtle signs of progress where the less talented perceive no difference.

## Why conjectures need proofs---and what proofs need

Mathematicians have sometimes believed true results for centuries without complete proof. The Fundamental Theorem of Algebra---that every polynomial of degree $n$ has exactly $n$ roots---was believed for about 250 years with little more basis than: a first-degree equation has one root, a second-degree equation has two roots, and no equation of degree $n$ has more than $n$ different roots. This plausible evidence was enough to sustain conviction across generations. The complete proof, when Gauss finally gave it, was notoriously difficult.

The lesson is not that proof is unnecessary. The lesson is that plausible reasoning and rigorous proof serve different functions, and both are essential. Plausible reasoning finds the result. Proof secures it. Without plausible reasoning, you have nothing to prove. Without proof, you have nothing you can build on.

There is a traditional story about Newton: as a young student, he began reading Euclid's Elements, saw that the theorems were true, and omitted the proofs. He wondered why anybody should take pains to prove things so evident. Many years later he changed his opinion and praised Euclid. The story may be authentic or not, but the question remains: why proofs? Because proofs hold together the logical system. Connected facts are more interesting and are better retained than isolated facts. And proofs---especially the simple, visual ones---often fix a whole cluster of related propositions in your mind more efficiently than any other device. Even when the aim is not logical rigor but merely coherence of understanding, proofs are useful.

Analogy, in particular, is a powerful source of conjectures. A result about finite sets may suggest an analogous result about multisets. A theorem about permutations may suggest a parallel for derangements. The analogy does not constitute a proof, but it generates the conjecture and helps you remember it.

The relationship between plausible reasoning and proof is not adversarial. Incomplete proofs---arguments that capture the germ of the idea without filling in every detail---are a legitimate and important tool, provided they are clearly labeled as such. The germ of the proof is often a piece of plausible reasoning that can later be made rigorous. The greatest expositors have the gift of presenting just the germ, the main idea in its simplest form, indicating the nature of the remaining details without burying the reader in them.

Polya wrote a sequel to *How to Solve It* called *Mathematics and Plausible Reasoning*, in which he investigated the connection between plausible reasoning and probability. He regarded the heuristic syllogism as the simplest pattern in a larger family that includes scientific induction, statistical evidence, circumstantial evidence, and the signs of progress that guide the working mathematician. The investigation of probability as allied to plausible reasoning---how to make precise the notion that $A$ becomes "more credible"---is the natural next step beyond what this chapter can cover.

The signs that convince the inventor that his idea is good, the indications that guide everyday affairs, the circumstantial evidence of the lawyer, the inductive evidence of the scientist, statistical evidence invoked in many and diverse subjects---all these kinds of evidence agree in two essential points. First, they do not have the certainty of a strict demonstration. Second, they are useful in acquiring essentially new knowledge, and even indispensable to any knowledge concerned with the physical world. The heuristic syllogism is the simplest and most widespread pattern of this kind of reasoning. The present chapter is the gateway to that larger investigation.

## Questions to keep

- *What would have to be true if this conjecture is right?* Derive consequences and check them.
- *Can you find a counterexample?* Try the simplest cases first, then extreme cases.
- *Can you state the guess more precisely?* A precise conjecture is vulnerable — and that vulnerability is what makes it productive.
- *Are you confusing plausible with certain?* The heuristic syllogism points a direction; it does not fix a destination.
