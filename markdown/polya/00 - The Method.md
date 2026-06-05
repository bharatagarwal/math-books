# The Method

## What this edition is

A great discovery solves a great problem, but there is a grain of discovery in the solution of any problem. Your problem may be modest; but if it challenges your curiosity and brings into play your inventive faculties, and if you solve it by your own means, you may experience the tension and enjoy the triumph of discovery.

That is Polya, writing in 1944. Behind that sentence lies a question that haunted him as a student: "Yes, the solution seems to work, it appears to be correct; but how is it possible to invent such a solution? And how could I invent or discover such things by myself?" That question drove the book. Not how to teach mathematics, but how discovery works, and whether its methods can be made explicit.

The result was *How to Solve It*, which Schoenfeld later described as marking "a line of demarcation between two eras, problem solving before and after Polya." Four publishers rejected the English version before Princeton brought it out in 1945. It has since sold over a million copies in seventeen languages.

Polya saw mathematics as having two faces. "It is the rigorous science of Euclid but it is also something else. Mathematics presented in the Euclidean way appears as a systematic, deductive science; but mathematics in the making appears as an experimental, inductive science." The finished proof is one face. The groping, guessing, testing process that produced it is the other. Most books show you the first face. This one is about the second.

The study of that second face has a name: *heuristic*. Polya notes that it "is not in fashion nowadays but has a long past and, perhaps, some future." Heuristic is the study of methods and rules of discovery. It is not a theory that guarantees solutions. It is a collection of questions, mental operations, and habits of attention that make discovery more likely. The questions are general enough to apply across subject matter. Their power is in that generality; their difficulty is that generality makes them feel obvious until you watch yourself fail to use them.

The subject has "manifold connections," as Polya put it --- mathematicians, logicians, psychologists, and philosophers may each claim parts of it. Polya's claim to it was simple: he had experience solving problems and teaching others to solve them, and he had thought hard about what the successful solvers actually did. The book is empirical in that sense. It reports on observed patterns of successful problem-solving, stated as general questions you can reuse.

Polya himself pointed toward this second face in a later work, *Mathematics and Plausible Reasoning*, which "continues the line of thinking begun in *How to Solve It*." There he showed Euler at work --- not presenting finished proofs, but explaining how he found his results, guessing from numerical evidence, testing by analogy, strengthening conjectures incrementally. Of the great mathematicians, Polya said, Euler was the one who influenced him most, precisely because Euler showed his work.

The book you are reading is Polya's *How to Solve It*, re-voiced for a software engineer learning mathematics. The voice is more direct. The examples come from discrete mathematics and programming rather than solid geometry. The alphabetical dictionary has been reorganized into thematic chapters. But the concepts --- heuristic, plausible reasoning, the inventor's paradox, problems to find versus problems to prove --- are his. Where his sentences still land, they appear verbatim.

The original was structured as a classroom guide (Part I), a short dialogue (Part II), and an alphabetical dictionary of heuristic (Part III). The dictionary was the heart of the book --- sixty-seven articles ranging from systematic discussions of general themes to cross-references, historical notes, quotations, and jokes. But the alphabetical arrangement makes it hard to see the conceptual territory. You look up "Analogy" and find a brilliant discussion, but you have no sense of where analogy fits in the arc of problem-solving.

This edition replaces all three parts with ten thematic chapters. The dictionary entries are not deleted; they are redistributed into the chapters where their ideas belong. Analogy lives in Discovery, alongside related problems and the bright idea. The inventor's paradox lives in Variation, alongside dropping constraints and changing the unknown. Looking back lives in Proof and Review, alongside checking, alternative proofs, and mathematical induction. The ideas are Polya's; the organization is new.

You can read the chapters in order or jump to whichever one names the kind of stuck you are.

> *Aside: George Polya.* Born György Pólya in Budapest in 1887, Polya came to mathematics late --- his undergraduate studies began in law, moved through languages and philosophy, and arrived at mathematics on the advice of a philosophy professor. "I wasn't good enough for physics, and was too good for philosophy --- mathematics is in between." He studied under Fejér in Budapest and spent years in Göttingen among Klein, Hilbert, Weyl, and Courant before settling in Zürich, where he wrote *How to Solve It* in German. A pacifist who refused military service in World War I, he could not return to Hungary for fifty-four years. He moved to Stanford in 1943, taught until 1978, and died in 1985 at ninety-seven. His mathematical contributions range across probability (coining "Central Limit Theorem," proving the recurrence of random walks in dimensions $\leq 2$), combinatorics (Polya's Enumeration Theorem), and analysis. But he is most remembered for this book and its successors, *Mathematics and Plausible Reasoning* and *Mathematical Discovery*, which pursue the question of how mathematical ideas are actually found.


## The four phases

Trying to find the solution, you may repeatedly change your point of view, your way of looking at the problem. You have to shift your position again and again. Your conception of the problem is likely to be rather incomplete when you start; your outlook is different when you have made some progress; it is different again when you have almost obtained the solution.

Polya distinguishes four phases of work:

1. **Understanding the problem.** See clearly what is required. What is the unknown? What are the data? What is the condition? Can you state the problem in your own words? Can you draw a figure, introduce notation, separate the parts of the condition?

2. **Devising a plan.** Find the connection between the data and the unknown. This is the hardest phase and the most interesting one. Have you seen a related problem? Can you use its method? Should you introduce an auxiliary element? If the direct attack fails, can you change the problem --- generalize, specialize, drop a constraint, work backwards?

3. **Carrying out the plan.** Execute each step and check it. Can you see clearly that the step is correct? Can you prove it is correct? The plan gives a general outline; carrying it out means convincing yourself that every detail fits, "patiently, till everything is perfectly clear, and no obscure corner remains in which an error could be hidden."

4. **Looking back.** Examine the completed solution. Can you check the result? Can you derive it differently? Can you use the result, or the method, for some other problem? This is not a formality. It is where a solved problem becomes a piece of lasting knowledge.

These are not stages you pass through once. You cycle. You think you understand the problem, begin devising a plan, realize you misunderstood a constraint, return to phase one. You carry out a plan, hit an error, retreat to phase two. The phases are a protocol for orientation: at any moment, you can ask *which phase am I in?* and that question alone often unsticks you.

### Understanding: more than reading

It is foolish to answer a question that you do not understand. It is sad to work for an end that you do not desire. These foolish and sad things happen constantly --- in mathematics, in programming, in life.

Understanding the problem is not the same as reading it. You have read the problem when you can repeat the statement. You have understood it when you can identify the unknown, the data, and the condition; when you can state the problem in your own words; when you have considered whether the condition is sufficient, insufficient, redundant, or contradictory; when you have drawn a figure or introduced notation that makes the structure visible.

Polya is insistent on notation. Choosing good names for the objects in your problem is not a clerical step. It forces you to consider what the objects are. If naming them is hard, you probably do not yet understand what you are working with. *Introduce suitable notation* is a suggestion that looks minor and does real work.

Similarly: *Is it possible to satisfy the condition?* This question is worth asking early, even if you cannot answer it definitively. Sometimes a quick check reveals that the problem as stated is impossible, or that you have misread a constraint. Better to discover this before investing in a plan.

A related question: *Is the condition sufficient to determine the unknown? Or is it insufficient? Or redundant? Or contradictory?* These sound pedantic until you encounter a problem where the answer is "insufficient" --- the problem as stated has multiple solutions, and you need to find all of them, or recognize that additional constraints are needed. Or "contradictory" --- the conditions cannot be simultaneously satisfied, and the problem is to prove impossibility rather than find a solution. Sorting this out is part of understanding, not part of solving.

Polya is clear that the problem itself must be well-chosen: "not too difficult and not too easy, natural and interesting." If you are choosing your own problems (and as a self-directed learner, you often are), this matters. A problem that is too easy teaches nothing; a problem that is too hard produces only frustration. The right problem is one that challenges your curiosity, brings your inventive faculties into play, and is solvable with effort. Finding such problems is itself a skill.

Polya's original preface captures why this matters: "Having tasted the pleasure in mathematics he will not forget it easily and then there is a good chance that mathematics will become something for him: a hobby, or a tool of his profession, or his profession, or a great ambition." The taste comes from solving problems that are genuinely challenging but within reach. The method in this book is what extends your reach.

### Why phase two is the hard one

The way from understanding the problem to conceiving a plan may be long and tortuous. Polya is direct about what it takes: "It takes so much to succeed; formerly acquired knowledge, good mental habits, concentration upon the purpose, and one more thing: good luck."

The idea of a plan may emerge gradually, through patient variation and re-examination. Or it may arrive suddenly, "in a flash, as a bright idea," after apparently unsuccessful trials and a period of hesitation. Both paths are normal. What matters is what you bring to them.

Good ideas are based on past experience and formerly acquired knowledge. But mere remembering is not enough. Polya uses a construction analogy: "Materials alone are not enough for constructing a house but we cannot construct a house without collecting the necessary materials." The materials for solving a mathematical problem are relevant items of formerly acquired knowledge --- solved problems, proved theorems, known techniques. You need to have them, and you need to recall the right ones at the right time.

This is why the question *Do you know a related problem?* is so central. The difficulty is that there are usually too many problems that are somewhat related to yours. How do you choose the one that is actually useful? A sharper question helps: *Look at the unknown --- can you think of a familiar problem having the same or a similar unknown?* This narrows the search from "vaguely related" to "structurally similar."

If that fails, you vary the problem. Could you restate it? Could you solve a more general problem, or a more special one? Could you drop part of the condition and see how the unknown varies? Could you change the unknown, or the data, or both? Could you work backwards from the desired result? Each of these is a specific operation, not a vague wish. They are the subject of the chapters on Discovery, Variation, and Auxiliary Problems.

And through all of this, a safety question: *Did you use all the data? Did you use the whole condition?* If you have not, something essential is being ignored. Trying to apply various known problems or theorems, considering various modifications, experimenting with various auxiliary problems, you may stray so far from your original problem that you are in danger of losing it altogether. This safety question brings you back.

### Carrying out: patience and honesty

To devise a plan is hard. To carry it out is comparatively easy --- what you need is mainly patience. But "easy" does not mean "trivial." The plan gives a general outline; you have to fill in every detail and check that each step is correct.

There are two ways to check a step. You can concentrate on it until you see it clearly and distinctly, with no remaining doubt --- this is intuitive conviction. Or you can derive it formally from known results. Polya distinguishes these as "seeing" and "proving": *Can you see clearly that the step is correct? But can you also prove that it is correct?*

The main danger during execution is losing the plan. If you received the idea from outside (a hint, a textbook, a friend), it may slip away as you work through details. If you conceived it yourself, even with some help, and felt the satisfaction of the bright idea, you are less likely to lose it. This is one reason why doing the planning work yourself matters --- not as a moral imperative, but as a practical one. Your own idea sticks better.

### Failure modes

Each phase has its characteristic failure:

- Skip understanding, and you solve the wrong problem. "It is foolish to answer a question that you do not understand." It is equally foolish to start coding before understanding the specification, or to manipulate symbols before grasping what a theorem says.
- Skip planning, and you thrash. You try computations without seeing the main connection. "It is generally useless to carry out details without having seen the main connection, or having made a sort of plan."
- Skip checking during execution, and errors hide in the details. The plan gives a general outline; you have to convince yourself that the details fit, "patiently, till everything is perfectly clear, and no obscure corner remains in which an error could be hidden."
- Skip looking back, and you lose the chance to consolidate. The method you just used could have solved three other problems, but you closed the book and moved on.

The worst of these is the first. Polya never wavers on this point. And the most commonly skipped, in his observation, is the last. "Even fairly good students, when they have obtained the solution of the problem and written down neatly the argument, shut their books and look for something else."

### Looking back: the most neglected phase

"Even fairly good students, when they have obtained the solution of the problem and written down neatly the argument, shut their books and look for something else. Doing so, they miss an important and instructive phase of the work."

Polya's claim about looking back is stronger than "check your answer." It is this: "No problem whatever is completely exhausted. There remains always something to do; with sufficient study and penetration, we could improve any solution, and, in any case, we can always improve our understanding of the solution."

What does looking back actually involve? Polya's own demonstrations are detailed. When he solves a problem, he does not merely verify the answer. He checks whether the formula uses all the data. He tests symmetry: if the problem treats certain variables interchangeably, does the answer? He checks limiting cases: what happens when a variable goes to zero, or to one, or to infinity? He looks for analogy: is the result analogous to the known result in a simpler setting? He tests proportional scaling: if all inputs double, does the output change as expected? He asks whether the result can be given a concrete interpretation.

These are not idle exercises. Each one is a different lens on the solution, and each has a chance of revealing an error or a deeper structure. Polya's point is that the solution, once obtained, is raw material for further work.

Looking back serves three purposes:

1. **Verification.** Can you check the result? Can you check the argument? Errors are always possible, especially if the argument is long. If there is some rapid, intuitive procedure to test the result, use it.

2. **Alternative derivation.** "As we prefer perception through two different senses, so we prefer conviction by two different proofs." Can you derive the result differently? Can you see it at a glance?

3. **Transfer.** Can you use the result, or the method, for some other problem? This is where a single solved problem becomes a tool for future problems. The connections you find here are what build mathematical knowledge, not just mathematical answers.

The looking-back phase is where you discover what you actually learned. Skip it and you solved a problem. Do it well and you acquired a method.

Polya observes that students who have made an honest effort and succeeded "are eager to see what else they could accomplish with that effort, and how they could do equally well another time." Looking back feeds on the satisfaction of having solved the problem. Use that momentum.


## The questions are the method

The heart of Polya's system is not a theory. It is a list of questions.

*What is the unknown? What are the data? What is the condition?* These are for understanding. *Do you know a related problem? Look at the unknown --- can you think of a familiar problem with a similar unknown?* These are for devising a plan. *Can you see clearly that the step is correct?* This is for carrying out. *Can you check the result? Can you derive it differently? Can you use the result, or the method, for some other problem?* These are for looking back.

### What the questions really are

Polya makes a subtle observation about the nature of these questions. They are not just prompts. They "indirectly enumerate mental operations typically useful for the solution of problems." When you ask *What is the unknown?*, you are not requesting a label. You are performing a cognitive operation: directing your attention to the goal, separating it from the noise, making it precise. When you ask *Do you know a related problem?*, you are performing a memory search with a specific structure. The questions are compressed descriptions of mental moves.

This is why they work across subject matter. The mental operation of focusing on the unknown is the same whether the unknown is a number, a set, a proof, or a bug. The mental operation of searching for a related solved problem is the same whether you are doing combinatorics or debugging a distributed system.

Consider the question *Could you restate the problem?* On the surface, it asks you to rephrase. But the mental operation it triggers is deeper: you are searching for an equivalent formulation that might be easier to work with, or that reveals a structure the original statement hid. Restating "how many subsets does an $n$-element set have?" as "how many binary strings of length $n$ are there?" is a restatement that immediately solves the problem. The question did not tell you *how* to restate; it told you to perform the operation of looking for a restatement. The skill is in learning which restatements are productive, and that comes from practice.

Or consider *Did you use all the data?* This is not a bookkeeping question. It triggers a scan of your current approach to check whether you are ignoring something the problem gave you. If you are, either your approach is incomplete or the problem has redundant data worth noticing. Either way, the scan itself is the valuable operation.

### Generality and its restriction

The questions are general. They apply to algebraic problems and combinatorial problems, to proofs and to computations, to puzzles and to research. Their power comes from this generality: they are not subject-matter knowledge, they are the scaffolding you erect around any problem regardless of subject.

But there is a restriction, and it matters. Certain questions on the list apply only to *problems to find*, not to *problems to prove*. The question *What is the unknown?* belongs to problems to find --- where the unknown is a thing (a number, a set, a function, an object satisfying given conditions). For problems to prove --- where the task is to establish or refute a statement --- the questions shift: *What is the hypothesis? What is the conclusion? Can you think of a related theorem?*

If you are trying to prove an inequality and you keep asking "What are the data?", you are using the wrong template. Check which kind of problem you have before reaching for the questions. The distinction is developed fully in the chapter on Understanding.

### The weakness of generality

Generality is also the questions' weakness, at first. "Look at the unknown and try to think of a familiar problem having the same or a similar unknown" sounds obvious. Of course you would do that. The trouble is that you often don't. Under pressure, with a blank page, you skip the obvious and reach for something clever, or you stare at the problem without decomposing it, or you start computing before you have a plan.

The questions are plain common sense stated in general terms. They suggest conduct which comes naturally to anyone who is seriously concerned with a problem and has some common sense. But the person who behaves the right way usually does not bother to express that behavior in clear words --- and possibly cannot. The list tries to express it so.

### How the questions become yours

How do the questions become yours? By repetition. You ask them of yourself, problem after problem. At first they feel mechanical. Then, occasionally, one of them provokes the right idea. That success teaches you when and how to deploy it. After enough such successes, the question fires automatically. You do not consult a list; you *are* the list.

There is a specific mechanism for how this happens, and Polya is concrete about it. You learn the questions the way you learn any practical skill: by watching them used, then using them yourself.

Polya compares this to swimming. You acquire any practical skill by imitation and practice. Trying to swim, you imitate what other people do with their hands and feet to keep their heads above water, and finally you learn to swim by practicing swimming. Trying to solve problems, you observe and imitate what other people do when solving problems, and finally you learn to do problems by doing them.

The imitation phase has a specific form. When someone solves a problem in front of you, they should "dramatize their ideas a little" --- externalize the self-questioning so you can see the mental operations happening. They should visibly ask themselves *What is the unknown?* and *Do I know a related problem?* and *Did I use all the data?* When you watch this, you are not learning the solution to that particular problem. You are learning the pattern of attention that produced it. Later, when you solve problems alone, you reproduce that pattern.

The internalization happens through a specific cycle. If the same question is repeatedly helpful, you will notice it. You will be induced to ask it yourself in a similar situation. Asking it repeatedly, you may succeed once in eliciting the right idea. By that success, you discover the right way of using the question, and then you have really assimilated it. The question stops being something you read on a list and becomes something you do.

This book is the imitation phase. It dramatizes the self-questioning on problems you care about. The practice phase is yours.

"Mathematics is not a spectator sport," as Polya put it. "To understand mathematics means to be able to do mathematics." And what does it mean to do mathematics? "In the first place, it means to be able to solve mathematical problems."

The questions, used repeatedly and honestly, are the bridge between watching someone else solve problems and solving them yourself. They are not a substitute for mathematical knowledge --- you cannot ask *Do you know a related problem?* if you know no problems. They are the scaffolding that lets you deploy whatever knowledge you have. As your knowledge grows, the same questions reach further.


## The recurring example

Throughout this edition, one problem recurs across multiple chapters to show the same four phases and the same questions working on a single thread. The problem is this:

> How many subsets does an $n$-element set have?

This problem was chosen because it is small enough to hold in your head and rich enough to demonstrate real moves. Here is a preview of the four phases applied to it, so you can see the method working before the chapters develop each phase in detail.

### Understanding

What is the unknown? A count --- the number of subsets. What are the data? A set with $n$ elements. What is the condition? You want *all* subsets, including the empty set $\emptyset$ and the full set itself.

Can you state it in your own words? You are counting the distinct subsets of $\{a_1, a_2, \ldots, a_n\}$.

Is the condition sufficient to determine the unknown? Yes --- if you know $n$, the number of subsets is determined (it does not depend on what the elements are, only on how many there are). Is the condition possible to satisfy? Trivially yes for any non-negative integer $n$.

Can you try small cases to make sure you understand? If $n = 0$, the set is $\emptyset$ and it has one subset: $\emptyset$ itself. If $n = 1$, the set $\{a\}$ has two subsets: $\emptyset$ and $\{a\}$. If $n = 2$, the set $\{a, b\}$ has four: $\emptyset, \{a\}, \{b\}, \{a,b\}$. If $n = 3$, the set $\{a, b, c\}$ has eight: $\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}$.

The pattern $1, 2, 4, 8$ suggests $2^n$. You have a conjecture. Now you need a plan.

### Devising a plan

*Do you know a related problem?* If you know binary representations, you might notice that each subset corresponds to a binary string of length $n$: a $1$ in position $i$ means element $i$ is included, a $0$ means it is not. The subsets of $\{a, b, c\}$ correspond to $000, 001, 010, 011, 100, 101, 110, 111$. There are $2^n$ binary strings of length $n$, so there are $2^n$ subsets.

*Can you think of another approach?* You might think inductively. Every subset of $\{a_1, \ldots, a_n\}$ either contains $a_n$ or does not. The subsets that do not contain $a_n$ are exactly the subsets of $\{a_1, \ldots, a_{n-1}\}$. The subsets that do contain $a_n$ are obtained by taking each subset of $\{a_1, \ldots, a_{n-1}\}$ and adding $a_n$ to it. This is a bijection: the count doubles with each new element.

Two plans, two points of contact with past knowledge. Notice how both plans emerged from specific questions. The binary-string plan came from *Do you know a related problem?* (the answer: counting binary strings). The inductive plan came from a variation: *Can you solve a simpler version first?* (the answer: reduce $n$ by one). Neither plan arrived by staring at the problem. Each was provoked by a question.

### Carrying out the plan

**The binary-string argument.** Define a map $f$ from subsets of $\{a_1, \ldots, a_n\}$ to binary strings of length $n$: for each subset $S$, let the $i$-th bit of $f(S)$ be $1$ if $a_i \in S$ and $0$ if $a_i \notin S$. This map is a bijection --- distinct subsets produce distinct strings (injective), and every string corresponds to some subset (surjective). The number of binary strings of length $n$ is $2^n$. Done.

*Can you see clearly that each step is correct?* The injectivity and surjectivity are each one-line arguments. Check them.

**The inductive argument.** Let $f(n)$ be the number of subsets of an $n$-element set. You have $f(0) = 1$ (the empty set has one subset). The doubling argument gives $f(n) = 2 \cdot f(n-1)$. Solving the recurrence by repeated substitution:

$$f(n) = 2 \cdot f(n-1) = 2 \cdot 2 \cdot f(n-2) = \cdots = 2^n \cdot f(0) = 2^n$$

*Can you prove that the step is correct?* The key claim is that the "contains $a_n$" / "does not contain $a_n$" partition is exhaustive and the two halves have equal size. Both follow directly from the definition.

### Looking back

Now the solution is complete. This is where most people stop. Don't.

**Check boundary cases.** For $n = 0$: the empty set has one subset (itself), and $2^0 = 1$. For $n = 1$: $\{a\}$ has two subsets, and $2^1 = 2$. These are not just "sanity checks" --- they are tests of whether your formula handles degenerate inputs. A formula that fails at the boundary is wrong or incomplete.

**Check growth behavior.** Each new element doubles the count. Does that make sense? Yes: each new element creates a choice (include it or not) that is independent of all previous choices. The exponential growth is the product of $n$ independent binary choices. If your formula gave something like $n^2$ or $n!$, that would conflict with this independence structure.

**Compare two independent proofs.** You have the binary-string bijection and the inductive recurrence. They use different ideas (representation vs. recursion) and arrive at the same answer. As Polya says, "as we prefer perception through two different senses, so we prefer conviction by two different proofs."

**Check by symmetry.** The formula $2^n$ does not depend on which elements are in the set, only on how many. Is that right? Yes --- relabeling the elements permutes the subsets but does not change the count. If your formula had depended on the specific elements, something would be wrong. (Compare Polya's check on the parallelepiped diagonal: the formula $\sqrt{a^2 + b^2 + c^2}$ is symmetric in $a, b, c$ because the three dimensions play the same role. The same principle works here: the $n$ elements play interchangeable roles, so the count should depend only on $n$.)

**Ask: can you use the method elsewhere?** The binary-string bijection is a general technique. It establishes a correspondence between subsets of an $n$-element set and elements of $\{0,1\}^n$. This same idea appears when:

- Counting lattice paths on a grid (each step is a binary choice: right or up).
- Enumerating bit-masks in programming (a common pattern in combinatorial algorithms).
- Analyzing power sets in set theory (the power set $\mathcal{P}(S)$ is literally $\{0,1\}^S$).
- Computing probabilities over independent binary events (each event either occurs or does not).

The inductive doubling argument generalizes to any situation where adding one element multiplies the count by a fixed factor. If adding an element multiplied the count by $k$ instead of $2$, you would get $k^n$. This is the bridge to more general counting problems.

**Ask: can you reuse the result?** From $2^n$ subsets you can immediately derive that the number of subsets of size $k$ sums correctly: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$. This is a non-trivial identity that falls out as a corollary. You solved one problem and got a second result for free.

This is what looking back looks like when done properly. Not a perfunctory check, but a systematic exploration: boundary cases, growth behavior, symmetry, alternative proofs, reuse of the method, and corollaries of the result. Polya's point is that "no problem whatever is completely exhausted." You can always go further.

Notice what the looking-back phase accomplished here. You started with one problem (count the subsets) and ended with: a verified formula, two independent proofs, a general bijection technique (binary strings), a general recursion technique (inductive doubling), a non-trivial corollary (the binomial-coefficient identity), boundary-case confidence, and a structural explanation for why the answer is exponential. One problem, worked thoroughly, produced seven usable pieces of knowledge. This is what Polya means by "no problem whatever is completely exhausted."

When this problem appears in later chapters, it will be in service of a specific heuristic: the binary-string representation illustrates *auxiliary elements* and *change of representation*; the inductive argument illustrates *specialization* (try small cases) and *generalization* (from specific $n$ to arbitrary $n$); looking back illustrates *using the result elsewhere* and *consolidation*.


## How to read this edition

The chapters are thematic, not alphabetical. Here is the map:

| Chapter | Territory |
|---|---|
| **0. The Method** | The four phases, the questions, how to read the book |
| **1. Understanding** | Phase one: making the problem graspable before solving it |
| **2. Discovery** | Phase two: how ideas are found --- memory, analogy, the unknown |
| **3. Variation** | What to do when the direct attack stalls: change the problem |
| **4. Auxiliary Problems** | The indirect route: solve another problem, introduce another object |
| **5. Signs of Progress** | How to tell if your work is moving, stalling, or drifting |
| **6. Plausible Reasoning** | Guessing is not proof, but it is how discovery starts |
| **7. Proof and Review** | Carrying out, proving, checking, and looking back |
| **8. Style, Judgment, and Practice** | Self-training for the developing solver |
| **9. Problems** | Practice problems organized by heuristic move |

The original book's Conway foreword offers a useful test for whether you are reading actively enough: "If you can't solve a problem, then there is an easier problem you can't solve: find it." That advice --- find the easier problem you also can't solve --- is itself an application of the method (it is the question *Can you think of a more accessible related problem?* turned into a diagnostic). Keep it in mind throughout.

You can read straight through. Or you can start from wherever you are stuck:

- *I don't know where to begin.* Read **Understanding**.
- *I understand the problem but have no ideas.* Read **Discovery** and **Variation**.
- *I have too many ideas and none of them work.* Read **Signs of Progress**.
- *I have a guess but can't prove it.* Read **Plausible Reasoning** and **Proof and Review**.
- *I solved it but I'm not sure I learned anything.* Read **Proof and Review**, especially the section on looking back.
- *I want to get better at this over time.* Read **Style, Judgment, and Practice**.

Each chapter ends with a compact list of **Questions to keep** --- the two to four questions from that chapter most worth internalizing. These are the residue of the chapter: if you forget everything else, keep the questions. They are the main cognitive-load reducers: a handful of questions that compress an entire chapter of method into portable self-interrogation.

Every chapter makes clear which phase of the solver's protocol it strengthens. The four phases are not one chapter's concern; they are the spine of the entire book.

One more thing. Polya distinguishes two kinds of problems:

- **Problems to find.** The unknown is a thing --- a number, a set, a function, an object satisfying given conditions. "Find all $x$ such that..." The questions *What is the unknown? What are the data? What is the condition?* belong here.

- **Problems to prove.** The unknown is the truth or falsity of a statement. "Prove that for all $n$..." The questions shift: *What is the hypothesis? What is the conclusion? Can you think of a related theorem?*

This distinction matters because the wrong questions waste your time. If you are trying to prove an inequality and you keep asking "What are the data?", you are using the wrong template. The chapters ahead will make the distinction concrete, but it is worth naming now: check which kind of problem you have before reaching for the questions.

A practical note on the structure: each major heuristic entry in the chapters ahead follows a common shape. First, *the idea* --- Polya's concept, re-voiced. Then *concrete moves* --- three to six specific sub-strategies (because a general heuristic like "solve a related problem" is actually a family of moves: set $n = 1, 2, 3$; drop a constraint; lower the dimension; specialize the type). Then *when to reach for it* --- one or two lines. Then *questions to keep* --- the two to four self-questions worth internalizing from that entry. This shape is meant to make the heuristics usable, not just readable.

A practical note on the problems in this book. The original included problems from solid geometry and continuous mathematics. This edition replaces most of them with problems from discrete mathematics, combinatorics, and occasionally programming --- domains closer to the reader's daily work. But the heuristic moves are the same. A change of representation is a change of representation whether the objects are triangles or binary strings. Working backwards is working backwards whether you are constructing a geometric figure or deriving a recurrence. The method is independent of the subject matter. That is its point.


## Questions to keep

These are the questions from this chapter worth carrying forward. They are not about any particular problem. They are about orientation --- the meta-level of problem-solving where you monitor your own process. If the method in this book has a single sentence summary, it is: ask yourself the right question at the right time. The questions below are the ones that apply always, regardless of subject or phase.

- **Which phase am I in?** Understanding, planning, executing, or looking back? If you cannot say, you are probably drifting.
- **What is the unknown?** The single most important question in the entire book. Ask it first, every time.
- **Have I understood the problem, or have I only read it?** Can you state it in your own words? Can you identify the unknown, the data, and the condition (or the hypothesis and the conclusion)?
- **Am I solving the problem I was given, or a different one?** It is easy to drift into a related but different problem without noticing. Check.
- **Did I use all the data? Did I use the whole condition?** If not, something essential is being ignored --- or the problem has redundancy worth noticing.
- **Can I use the result, or the method, for some other problem?** The question that turns a solved problem into a tool.
- **Is this a problem to find or a problem to prove?** The answer determines which questions apply. Get this wrong and you waste time with the wrong template.

These seven questions are the method in miniature. Everything else in this book is elaboration, illustration, and practice. If you carry nothing else away, carry these.

The chapters ahead will make each question concrete with worked examples, specific sub-strategies, and the full texture of Polya's thinking about discovery, variation, plausible reasoning, and proof. But the questions themselves are ready to use now, on the next problem you encounter. Try them. They feel mechanical at first. That is normal. Keep going. The mechanism Polya describes --- repeated use, occasional success, gradual internalization --- is real, and it starts with the first honest attempt.
