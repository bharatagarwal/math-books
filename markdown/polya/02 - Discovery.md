# Discovery

You understand the problem. You have the unknown, the data, the condition clearly in mind. Now what?

Now you need an idea. A plan. Some bridge between what you know and what you seek. This chapter is about how ideas are found: how you search your memory, how you spot connections, how you coax the right thought into appearing. The process is not magic, but it is not mechanical either. It depends on past experience, on good habits of attention, and on a certain willingness to look at the problem from more than one side.

The main achievement in solving a problem is to conceive the idea of a plan. Everything before it is preparation; everything after it is execution. The idea may emerge gradually, or it may arrive suddenly, as a "bright idea." The habits in this chapter prepare the ground for such ideas.

## Look at the unknown

The oldest and most reliable piece of advice is simple: look at the unknown. What are you trying to find? What kind of thing is it?

Focus on the unknown and let everything else recede for a moment. You are looking for a number, or a formula, or a combinatorial object, or a proof. Strip the problem down to its schematic form:

"Given $\ldots$ find a count."

"Given $\ldots$ find a function."

"Given $\ldots$ find a proof of an identity."

"Given $\ldots$ construct a graph with property $P$."

Now ask yourself: what is the simplest problem you know that has the same kind of unknown? If you are looking for the number of elements in some set, the simplest problems you know are direct enumeration, multiplication principle, bijection with something already counted. If you are looking for a proof that two quantities are equal, the simplest tools are algebraic manipulation and induction.

This creates an economy of search. Instead of rummaging through every problem you have ever solved, you consider only problems with the same kind of unknown --- and among those, the most elementary ones first. The problem appears to you schematically, and that schema narrows the field.

Polya develops this idea through four archetypes. You are looking for some unknown, and the schematic form tells you what kind of attack is plausible:

- If the unknown is a count, it should be obtained by enumeration, a counting principle, or a bijection with something already counted.
- If the unknown is a formula or closed form, it should be obtained by recognizing a pattern in small cases and then proving it.
- If the unknown is an object satisfying constraints, it should be obtained by building up from simpler cases or by working backwards from the constraints.
- If the unknown is a proof, it should be obtained by connecting the hypothesis to the conclusion through known theorems.

In each case, looking at the unknown gives you a direction. You know what kind of formerly solved problem to search for, and you can begin the search immediately.

**Concrete moves:**

1. State the unknown out loud: "I need a count," "I need a bijection," "I need to show divisibility."
2. Recall the simplest problem you know with that kind of unknown. Write it down if it helps.
3. Ask: could the method that solved that simple problem apply here, perhaps with modification?
4. If the unknown is composite (say, a pair of values, or a function and its domain), consider whether solving for one part first might open the way.

**When to reach for it:** Always. This is the default starting move whenever you sit down to devise a plan.

## Have you seen it before?

You may have solved the same problem before, or heard of it, or encountered one very like it. This is the most direct route to a plan: if you recognise the problem, you already know the answer --- or at least the shape of the answer.

But "have you seen it before?" is useful even when the answer is no. The question starts a search. It sends you rummaging through what you know. It sets up the conditions for recognition. Even if no feature of the problem is familiar, the act of asking puts your memory to work.

Polya calls this process *mobilization*: extracting from your dormant knowledge the items that are relevant to the problem at hand. Good ideas are based on past experience and formerly acquired knowledge. Mere remembering is not enough for a good idea, but you cannot have any good idea without recollecting some pertinent facts. Materials alone are not enough for constructing a house, but you cannot construct a house without collecting the necessary materials.

But mobilization is only half the story. The other half is *organization*: combining what you have recalled into a whole that is adapted to the problem at hand. You do not just dump remembered facts on the table; you arrange them, connect them, fit them to your present purpose. Mobilization and organization are not separate stages --- they are two aspects of the same process. Working at the problem with concentration, you recall only facts that are more or less connected with your purpose, and you have nothing to connect and organize but materials you have mobilized.

The practical distinction matters: sometimes you stall because you have not recalled enough (mobilization is incomplete), and sometimes you stall because you have recalled plenty but have not seen how the pieces fit (organization is incomplete). The question "have you seen it before?" primarily drives mobilization. The questions that follow --- about related problems, analogy, generalization --- primarily drive organization.

So you ask: *Have you seen it before? Or have you seen the same problem in a slightly different form?* And if any feature of the present problem strikes you as familiar, you press further: what is it? Where did you see it? What happened there?

If nothing comes to mind through remembering, the next step is to *invent* a related problem, not merely recall one. "I hope you have tried already the question: Do you know a related problem?" Polya writes. "You should now *invent* a related problem, not merely *remember* one."

**Concrete moves:**

1. Scan the problem for any familiar feature: the unknown, a datum, a structural pattern, a technique that seems relevant.
2. If you recognize something, trace the memory: where did you see it? What was the method? What was the result?
3. If nothing is familiar, shift from remembering to inventing: what related problem *could* exist? What would a simpler version of this problem look like?
4. Ask: is my difficulty a mobilization problem (I have not recalled enough) or an organization problem (I have the pieces but cannot see how they fit)?

**When to reach for it:** Immediately after looking at the unknown. This is the second move in the default sequence.

## Related problems and theorems

The difficulty is that there are usually too many problems that are somewhat related to yours. They share a datum, or a condition, or a method. How do you choose the one that is actually useful?

Here is a suggestion that puts your finger on an essential common point: *try to think of a familiar problem having the same or a similar unknown*.

Suppose you are trying to count the number of subsets of an $n$-element set. The unknown is a count. You have seen counts before. Which counting problems do you know well? Perhaps you recall that the number of binary strings of length $n$ is $2^n$. That is a problem with the same kind of unknown --- a count --- and it was solved by a clean argument (each position has two choices, multiply). Could you use it?

In fact, you can. There is a bijection between subsets of $\{1, 2, \ldots, n\}$ and binary strings of length $n$: the $k$-th bit is $1$ if element $k$ is in the subset, $0$ if it is not. So the number of subsets is $2^n$.

The key step was connecting the new problem to a solved one through the unknown. You did not search randomly among all problems you have ever seen. You searched among problems with the same unknown --- a count --- and found one whose method could be transferred.

*Here is a problem related to yours and solved before. Could you use it?* This is the moment when the plan begins to crystallise. You know the solution of the related problem, but you do not yet know how to use it. So you ask: *Could you use its result? Could you use its method? Should you introduce some auxiliary element in order to make its use possible?*

Sometimes you use the result directly. Sometimes you imitate the method, applying it step by step to the new setting. Sometimes you need both. And sometimes you need to introduce an auxiliary element --- a new representation, a relabelling, a bridge concept --- to make the connection possible. The consideration of a formerly solved related problem often leads you to introduce just such an element. You are trying to determine the number of spanning trees of a complete graph. You recall that for the complete graph $K_n$, Cayley's formula gives $n^{n-2}$. The proof you remember uses labelled trees encoded as sequences (Prufer sequences). *Should you introduce some auxiliary element in order to make its use possible?* The auxiliary element is the encoding itself --- a bijection between labelled trees and sequences of labels.

**Concrete moves:**

1. Recall a solved problem with the same or a similar unknown.
2. Ask: can I use its result? Its method? Both?
3. If the connection is not immediate, ask: what auxiliary element --- a new variable, a new representation, a relabelling --- would bridge the gap?
4. If no problem with the same unknown comes to mind, widen the search: a problem with a similar unknown, or one that shares a key piece of data or condition.

## Analogy

Analogy is a sort of similarity. Similar objects agree with each other in some respect; analogous objects agree in certain *relations* of their respective parts.

Analogy pervades all our thinking and all our discovery. It operates on many levels, from the vague ("this problem feels like that one") to the mathematically precise. All sorts of analogy may play a role in finding the solution, and you should not neglect any sort.

**The simpler analogous problem.** The most productive use of analogy in problem-solving is the *simpler analogous problem*. You have a problem about a complicated structure; consider the analogous problem about a simpler one. You have a problem about graphs; consider the analogous problem about trees. You have a problem about $n$ objects; consider the case $n = 1$ or $n = 2$. The simpler analogous problem serves as a *model*. Having solved it, you know the method, and you try to transfer that method to the original.

Consider the problem of counting the number of edges in the complete graph $K_n$. You might not see the formula immediately for general $n$. But the analogous problem for small cases is immediate: $K_2$ has $1$ edge, $K_3$ has $3$, $K_4$ has $6$. The pattern $1, 3, 6, 10, \ldots$ is the sequence of triangular numbers $\binom{n}{2}$. The analogy between the small cases and the general case guides you to the formula, and the formula suggests the proof: each edge is determined by choosing $2$ vertices from $n$.

**Method, result, or both.** Sometimes you can use the *method* of the simpler analogous problem, imitating it point by point. Sometimes you can use the *result*, applying it as a lemma. Sometimes, if you are fortunate, you can use both. Even when the method of the simpler problem cannot be immediately transferred, it may be worth reconsidering the solution, varying it, modifying it, until you find a form that *can* be extended to the original problem.

**A worked example: trees and forests.** Suppose you want to count the number of labelled forests on $n$ vertices (a forest is a graph with no cycles). You might not see how to approach this directly. But there is a simpler analogous problem: count the number of labelled *trees* on $n$ vertices. That problem is solved --- Cayley's formula gives $n^{n-2}$. Having solved the simpler analogous problem, you have a model. Can you transfer the method? The Prufer-sequence proof of Cayley's formula encodes each tree as a sequence. Can you encode forests similarly? In fact, you can: a standard trick adds a vertex $0$ connected to each component's root, turning a forest on $\{1, \ldots, n\}$ into a tree on $\{0, 1, \ldots, n\}$. The number of labelled forests is $(n+1)^{n-1}$. You used both the result and the method of the simpler analogous problem.

**Strength of analogical evidence.** An analogical conclusion from many parallel cases is stronger than one from fewer cases. But quality is more important than quantity. Clear-cut analogies weigh more heavily than vague similarities; systematically arranged instances count for more than random collections of cases.

**Precise levels of analogy.** At the most informal level, two problems "feel alike." At a more precise level, there is a one-to-one correspondence between the objects of two systems that preserves certain relations --- this is *isomorphism*. At a still more general level, the correspondence may be many-to-one and still preserve structure --- this is *homomorphism*. All of these are forms of analogy, and all may guide discovery. Recognizing that two structures are isomorphic is recognizing the strongest possible analogy; recognizing a homomorphism is recognizing a weaker but still useful one. The feeling that "this problem is like that one" is the vaguest form, and even it can be productive.

> *Simplex sigillum veri* --- simplicity is the seal of truth.

**Concrete moves:**

1. Ask: is there a simpler analogous problem? Lower the dimension, reduce the number of variables, specialise the structure.
2. Solve the simpler problem. Study its method.
3. Ask: can I transfer this method to the original problem? What breaks? What needs to be added?
4. If the method transfers cleanly, check whether the result also generalises (it often does).
5. If the analogy is vague, try to make it precise: is there a bijection, a homomorphism, a structural correspondence?

**When to reach for it:** When the problem involves a complicated structure (many variables, a general class of objects) and you suspect that the essential difficulty already appears in a simpler case.

## Generalization

Generalization is passing from one object to a set containing it, or from a restricted set to a more comprehensive one.

In problem-solving, generalization serves two purposes. The first is to reveal the *structure* behind a particular fact.

**The sum-of-cubes discovery.** Polya's most complete example of discovery through generalization, specialization, and induction working together begins with a single numerical observation:

$$1 + 8 + 27 + 64 = 100$$

which can be written as $1^3 + 2^3 + 3^3 + 4^3 = 10^2$. Does it often happen that a sum of successive cubes is a square? You generalize: consider $1^3 + 2^3 + 3^3 + \cdots + n^3$. You specialise by computing small cases:

$$
\begin{aligned}
1 &= 1^2 \\
1 + 8 &= 9 = 3^2 \\
1 + 8 + 27 &= 36 = 6^2 \\
1 + 8 + 27 + 64 &= 100 = 10^2 \\
1 + 8 + 27 + 64 + 125 &= 225 = 15^2.
\end{aligned}
$$

The sums are squares whose bases are $1, 3, 6, 10, 15$. What about these bases? The differences between successive terms are $2, 3, 4, 5$ --- conspicuously regular. You see a deeper pattern:

$$
\begin{aligned}
1 &= 1 \\
3 &= 1 + 2 \\
6 &= 1 + 2 + 3 \\
10 &= 1 + 2 + 3 + 4 \\
15 &= 1 + 2 + 3 + 4 + 5.
\end{aligned}
$$

The bases are triangular numbers. If this regularity is general, the theorem takes a precise form:

$$1^3 + 2^3 + 3^3 + \cdots + n^3 = (1 + 2 + 3 + \cdots + n)^2 = \left(\frac{n(n+1)}{2}\right)^2.$$

You arrived at this conjecture by generalizing a single observation, specializing to compute more cases, noticing an analogy among the cases, and generalizing again to state the pattern precisely. This is Polya's premier example of how induction (in the broad sense: observing particular instances and seeking a general law) and the heuristic moves of this chapter work together. The proof --- by mathematical induction in the narrow sense --- is a separate matter, treated in the chapter on Proof and Review.

**The inventor's paradox.** The second purpose of generalization is more paradoxical: it can make a problem *easier*. The more ambitious plan may have more chances of success --- "provided it is not based on mere pretension but on some vision of the things beyond those immediately present."

Consider a problem about a specific graph: show that every connected graph on $n$ vertices has at least $n - 1$ edges. You might try to prove this directly for connected graphs, but the argument is cleaner if you generalize: prove that a connected graph on $n$ vertices with exactly $n - 1$ edges is a tree (has no cycles), and that removing any edge disconnects it. The general statement about trees gives you more structure to work with than the bare inequality about connected graphs.

This is the **inventor's paradox**. Passing from the sum-of-cubes observation to the precise general formula was harder, but the precise formula was easier to prove by induction than the vague statement "sums of cubes tend to be squares." The more general, more precise statement had more handles.

A common and useful form of generalization is to replace numbers by letters. "Find the number of subsets of a $5$-element set" becomes "find the number of subsets of an $n$-element set." The problem in letters is more general, but it is also more *testable*: you can check the formula for $n = 0, 1, 2, 3$ before committing to it, and the pattern may suggest the proof.

**Concrete moves:**

1. Replace specific numbers by variables. Solve the general problem.
2. Ask: is there a more general class of objects for which the same argument works?
3. If the general problem is hard, solve it for small cases first (this is specialization --- the two moves work together).
4. Check whether the general result, once found, has a simpler proof than the special case that started you off.

**When to reach for it:** When a specific problem seems to depend on features that feel incidental, or when a slightly broader formulation would let you use a stronger tool.

## Specialization

Specialization is the reverse of generalization: passing from a set to a smaller set, or to a single object. You specialise when you check small cases, when you test extreme values, when you try a concrete example before attacking the general statement.

Specialization is the experimentalist's move. You do not yet know whether the general statement is true, so you test it. You do not yet see how to solve the general problem, so you solve a special case and look for a pattern.

To count the subsets of an $n$-element set, you might start with small cases:

| $n$ | subsets | count |
|-----|---------|-------|
| $0$ | $\{\emptyset\}$ | $1$ |
| $1$ | $\emptyset, \{1\}$ | $2$ |
| $2$ | $\emptyset, \{1\}, \{2\}, \{1,2\}$ | $4$ |
| $3$ | (all eight) | $8$ |

The pattern $1, 2, 4, 8$ suggests $2^n$, which you then prove by the binary-string bijection or by induction.

Extreme cases are particularly instructive. If a general statement is supposed to hold for all values of a parameter, test it at the boundary: $n = 0$, $n = 1$, or the limiting case where some quantity vanishes. Extreme cases are apt to be overlooked by the inventors of conjectures, so they are good places to look for counterexamples. Conversely, if a conjecture survives an extreme case, the inductive evidence is strong, precisely because the prospect of refutation was high.

**Concrete moves:**

1. Set $n = 0, 1, 2, 3$ (or whatever the natural small values are). Compute by hand.
2. Examine extreme or degenerate cases: what happens when a parameter vanishes, or grows very large?
3. Look for a pattern in the small cases. State it as a conjecture.
4. Use the pattern to guide the proof of the general case.

**When to reach for it:** When the general problem is opaque and you need data to form a conjecture, or when you have a conjecture and want to test it before investing in a proof.

## How to vary a problem

The moves described so far --- looking at the unknown, recalling related problems, analogy, generalization, specialization --- are all forms of *variation*. You change the problem deliberately, hoping the changed version is more tractable or more illuminating.

Polya gives a formal classification of the ways you can vary a "problem to find." You have an unknown, data, and a condition. You can:

1. **Keep the unknown and change the rest** (the data and the condition). This is what "look at the unknown" does: you keep the unknown fixed and search for problems with the same unknown but different data. You may also weaken the condition, dropping part of it to see how far the unknown is then determined.

2. **Keep the data and change the rest** (the unknown and the condition). Ask: *Could you derive something useful from the data?* You introduce a new, more accessible unknown --- a stepping stone. A stone in the middle of the creek is nearer to you than the far bank, and when the stone is reached, it helps you across.

3. **Change both the unknown and the data.** This is the most drastic variation. You may be compelled to it if less radical changes have failed. One interesting special case: *interchange the unknown with one of the data*.

This taxonomy is not just a catalogue. It is the structural backbone of how discovery works. Every time you are stuck, you are choosing (consciously or not) among these three moves. Making the choice explicit helps you avoid repeating the same failed variation.

**Why variation works.** There is a psychological reason, not just a logical one. You remember things by mental association --- what you have in mind now tends to recall what was connected to it before. Varying the problem brings in new points, creating new contacts with your stored knowledge, new possibilities of recalling something relevant.

There is also the problem of attention. You cannot concentrate on the same unchanging object indefinitely without your attention flagging. If your work progresses, there is always something new to examine and your interest stays alive. But if you fail to make progress, your attention falters, your interest fades, and you are in danger of losing the problem altogether. A new question about the problem --- a deliberate variation --- reconquers your interest by showing a new aspect. As Polya puts it: "attention needs change to stay alive."

**Concrete moves:**

1. Identify which type of variation you have been trying. If you have only varied the unknown, try varying the data instead.
2. Drop part of the condition and ask: how far is the unknown then determined? How can it vary?
3. Introduce a new, more accessible unknown as a stepping stone.
4. If stuck for a long time, change both the unknown and the data --- the most drastic variation, but sometimes the only one that works.
5. When one variation fails, modify it rather than abandon it entirely. There may be a good idea in an unsuccessful trial.

**When to reach for it:** Whenever the direct attack has stalled and you need a new angle.

## The bright idea

The coming of a bright idea is an experience familiar to everybody but difficult to describe. Aristotle defined "sagacity" as "a hitting by guess upon the essential connection in an inappreciable time." The essential connection --- that is the key phrase. You suddenly see how the unknown is linked to the data, how the pieces fit, why the conjecture must be true.

**The moon and the sun.** Polya preserves a vivid illustration from Aristotle. You observe that the bright side of the moon always faces the sun. Night after night, the relationship holds: when the moon is a crescent, the bright side points toward the sun; when the moon is full, the sun is opposite. And then, in a flash, you understand *why*: the moon shines by reflected light. The bright side faces the sun because the sun is the source of the light. The observation was gradual; the understanding was sudden. That sudden understanding --- seeing the essential connection between the bright side and the sun's position --- is what Aristotle called sagacity.

A bright idea is an abrupt and momentous change in your outlook: a sudden reorganisation of how you conceive the problem, a confident prevision of the steps you must take. It is what Polya calls a "flash" --- and what, in less dramatic form, is simply the moment when the plan falls into place.

**Subconscious work.** You cannot force a bright idea. But you can prepare the ground for one. Every question in this chapter --- look at the unknown, recall related problems, try analogy, generalise, specialise --- is a way of preparing. You are turning the problem over, viewing it from different angles, testing connections. Each attempt that fails still teaches you something about the problem's shape.

And sometimes, after all this preparation, you need to stop. You work hard on a problem, get nowhere, and set it aside. The next morning, or after a few days, you return to it and the solution comes easily. Polya takes this phenomenon seriously: "The fact is that a problem, after prolonged absence, may return into consciousness essentially clarified, much nearer to its solution than it was when it dropped out of consciousness." Who clarified it? You did, working at it subconsciously.

There is a limit beyond which you should not force conscious reflection. "Take counsel of your pillow" is old advice. But the subconscious does not work for free. Only problems that you passionately desire to solve, problems for which you have worked with great tension, come back improved. Conscious effort and tension seem necessary to set the subconscious work going. "At any rate, it would be too easy if it were not so; we could solve difficult problems just by sleeping and waiting for a bright idea."

Past ages regarded a sudden good idea as an inspiration, a gift of the gods. You must deserve such a gift by work, or at least by a fervent wish.

**The rules of discovery.** Polya states them with characteristic dryness: "The first rule of discovery is to have brains and good luck. The second rule of discovery is to sit tight and wait till you get a bright idea." Infallible rules of discovery leading to the solution of all possible problems would be more desirable than the philosopher's stone, and just as imaginary. What heuristic can offer is not certainty but a set of moves that are *typically useful* --- moves that, applied with judgment, increase the odds.

> Descartes traced the origin of his own method to a similar observation: "As a young man, when I heard about ingenious inventions, I tried to invent them by myself, even without reading the author. In doing so, I perceived, by degrees, that I was making use of certain rules."

Descartes left unfinished his *Rules for the Direction of the Mind*. The fragments, found in his manuscripts and printed after his death, contain more --- and more interesting --- materials concerning the solution of problems than his better-known *Discours de la Methode*.

> Bolzano, the logician and mathematician, wrote about this process with characteristic modesty: "I do not think at all that I am able to present here any procedure of investigation that was not perceived long ago by all men of talent; and I do not promise at all that you can find here anything quite new of this kind. But I shall take pains to state in clear words the rules and ways of investigation which are followed by all able men, who in most cases are not even conscious of following them."

The moves described in this chapter are not new. Every good problem-solver uses them, consciously or not. The value of stating them explicitly is that you can reach for them deliberately when you are stuck, instead of waiting passively for inspiration.

## Putting the moves together

In practice, the heuristics of discovery do not operate one at a time. You look at the unknown and recall a related problem; that related problem suggests an analogy; the analogy leads you to specialise; the special case reveals a pattern; the pattern suggests a generalisation; and the generalisation turns out to be the plan.

Let us trace this through the recurring example. You want to prove that the number of subsets of $\{1, 2, \ldots, n\}$ is $2^n$.

1. **Look at the unknown.** The unknown is a count. You are looking for the total number of subsets.

2. **Have you seen it before?** You recall that powers of $2$ come up when you count binary strings. A binary string of length $n$ is a sequence of $0$s and $1$s; there are $2^n$ of them, since each of $n$ positions has $2$ choices.

3. **Related problem.** *Here is a problem related to yours and solved before. Could you use it?* The binary-string count is solved. Could you use its result?

4. **Auxiliary element.** You need a bridge: a bijection between subsets and binary strings. Associate to each subset $S \subseteq \{1, \ldots, n\}$ the string $b_1 b_2 \cdots b_n$ where $b_k = 1$ if $k \in S$ and $b_k = 0$ if $k \notin S$. This is a one-to-one correspondence.

5. **The plan.** Subsets biject with binary strings; binary strings number $2^n$; therefore subsets number $2^n$.

6. **Check by specialization.** For $n = 0$: one subset (the empty set), $2^0 = 1$. For $n = 1$: two subsets, $2^1 = 2$. For $n = 3$: eight subsets, $2^3 = 8$. The formula checks out.

The discovery happened because you connected *look at the unknown* (a count) with *a related problem* (binary strings) through *an auxiliary element* (the bijection). Each move was simple. The combination produced the plan.

Now consider a different problem where the moves combine in a less obvious order. You want to find a closed form for the number of regions created by $n$ lines in general position in the plane. You try specialization first: $n = 0$ gives $1$ region, $n = 1$ gives $2$, $n = 2$ gives $4$, $n = 3$ gives $7$. You try to generalize from the pattern $1, 2, 4, 7$, but it is not a familiar sequence. You look at the *differences*: $1, 2, 3$. Each new line adds as many regions as the number of pieces it is cut into by the previous lines --- which is one more than the number of lines it crosses. So the $k$-th line adds $k$ regions. The total is:

$$1 + 1 + 2 + 3 + \cdots + n = 1 + \frac{n(n+1)}{2} = \binom{n}{0} + \binom{n}{1} + \binom{n}{2}.$$

Here you used specialization (small cases), then looked at the unknown differently (differences instead of totals), then recognized a related problem (summing an arithmetic progression), and finally expressed the result using generalization (the binomial-coefficient form that hints at higher-dimensional analogues). The moves came in a different order than in the subset example, guided by what each move revealed.

## Questions to keep

- *What kind of object am I looking for?* (Look at the unknown — this narrows the search.)
- *Have I seen it before?* Do I know a problem with the same kind of unknown, and could I use its method?
- *Could I specialise or generalise?* Small cases, extreme cases, a more general statement that might be easier to prove?
- *Did I use all the data? Did I use the whole condition?*
