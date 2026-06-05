# The Method

## What this edition is

"A great discovery solves a great problem, but there is a grain of discovery in the solution of any problem." That is Polya, writing in 1944. Behind that sentence lies the question that drove the book: how does discovery work, and can its methods be made explicit?

Polya saw mathematics as having two faces. "Mathematics presented in the Euclidean way appears as a systematic, deductive science; but mathematics in the making appears as an experimental, inductive science." The finished proof is one face. The groping, guessing, testing process that produced it is the other. Most books show you the first face. This one is about the second.

The study of that second face has a name: *heuristic*. It is the study of methods and rules of discovery—not a theory that guarantees solutions, but a collection of questions, mental operations, and habits of attention that make discovery more likely. The questions are general enough to apply across subject matter. Their power is in that generality; their difficulty is that generality makes them feel obvious until you watch yourself fail to use them.

Polya himself pursued this line further in *Mathematics and Plausible Reasoning*, where he showed Euler at work—not presenting finished proofs, but explaining how he found his results, guessing from numerical evidence, testing by analogy, strengthening conjectures incrementally. Of the great mathematicians, Polya said, Euler was the one who influenced him most, precisely because Euler showed his work.

This edition re-voices *How to Solve It* for a software engineer learning mathematics. The examples come from discrete mathematics rather than solid geometry. The alphabetical dictionary has been reorganized into thematic chapters. But the concepts—heuristic, plausible reasoning, the inventor's paradox, problems to find versus problems to prove—are his. Where his sentences still land, they appear verbatim.

> *George Polya* (1887–1985) came to mathematics late—his undergraduate studies began in law, moved through languages and philosophy, and arrived at mathematics on a professor's advice. "I wasn't good enough for physics, and was too good for philosophy—mathematics is in between." His contributions range across probability, combinatorics, and analysis. He is most remembered for this book and its successors, which pursue the question of how mathematical ideas are actually found.


## The four phases

Polya distinguishes four phases of work:

1. **Understanding the problem.** See clearly what is required. What is the unknown? What are the data? What is the condition? Can you state the problem in your own words? Can you draw a figure, introduce notation, separate the parts of the condition?

2. **Devising a plan.** Find the connection between the data and the unknown. This is the hardest phase and the most interesting one. Have you seen a related problem? Can you use its method? Should you introduce an auxiliary element? If the direct attack fails, can you change the problem—generalize, specialize, drop a constraint, work backwards?

3. **Carrying out the plan.** Execute each step and check it. Can you see clearly that the step is correct? Can you prove it is correct? The plan gives a general outline; carrying it out means convincing yourself that every detail fits.

4. **Looking back.** Examine the completed solution. Can you check the result? Can you derive it differently? Can you use the result, or the method, for some other problem? "No problem whatever is completely exhausted. There remains always something to do; with sufficient study and penetration, we could improve any solution, and, in any case, we can always improve our understanding of the solution."

These are not stages you pass through once. You cycle. You think you understand the problem, begin devising a plan, realize you misunderstood a constraint, return to phase one. At any moment, you can ask *which phase am I in?* and that question alone often unsticks you.

Each phase has a characteristic failure:

- Skip understanding, and you solve the wrong problem. "It is foolish to answer a question that you do not understand."
- Skip planning, and you thrash—you try computations without seeing the main connection.
- Skip checking during execution, and errors hide in the details.
- Skip looking back, and you lose the chance to consolidate.

The worst is the first. The most commonly skipped, in Polya's observation, is the last: "Even fairly good students, when they have obtained the solution of the problem and written down neatly the argument, shut their books and look for something else."


## The questions are the method

The heart of Polya's system is not a theory. It is a list of questions.

*What is the unknown? What are the data? What is the condition?* These are for understanding. *Do you know a related problem?* This is for devising a plan. *Can you see clearly that the step is correct?* This is for carrying out. *Can you check the result? Can you use the method for some other problem?* These are for looking back.

The questions are not just prompts. They "indirectly enumerate mental operations typically useful for the solution of problems." When you ask *What is the unknown?*, you are performing a cognitive operation: directing your attention to the goal, separating it from the noise, making it precise. When you ask *Do you know a related problem?*, you are performing a memory search with a specific structure. The questions are compressed descriptions of mental moves.

This is why they work across subject matter. The mental operation of focusing on the unknown is the same whether the unknown is a number, a set, a proof, or a bug.

Generality is also the questions' weakness, at first. "Look at the unknown and try to think of a familiar problem having the same or a similar unknown" sounds obvious. The trouble is that you often don't. Under pressure, with a blank page, you skip the obvious and reach for something clever, or you stare without decomposing, or you start computing before you have a plan.

You learn the questions the way you learn any practical skill: by imitation and practice. "Trying to swim, you imitate what other people do with their hands and feet to keep their heads above water, and finally you learn to swim by practicing swimming." If the same question is repeatedly helpful, you will notice it. You will ask it in similar situations. Asking it repeatedly, you may succeed once in eliciting the right idea. By that success, you discover the right way of using the question, and then you have really assimilated it.

"Mathematics is not a spectator sport," as Polya put it. "To understand mathematics means to be able to do mathematics." This book is the imitation phase. The practice phase is yours.


## The recurring example

One problem recurs across multiple chapters to show the four phases and the same questions working on a single thread:

> How many subsets does an $n$-element set have?

Small enough to hold in your head. Rich enough to demonstrate real moves. Here is the preview:

**Understanding.** The unknown is a count. The data is a set with $n$ elements. You want all subsets, including $\emptyset$ and the full set. Small cases: $n=0$ gives $1$; $n=1$ gives $2$; $n=2$ gives $4$; $n=3$ gives $8$. The pattern suggests $2^n$.

**Devising a plan.** Each subset corresponds to a binary string of length $n$: a $1$ in position $i$ means element $i$ is included. The subsets of $\{a,b,c\}$ correspond to $000, 001, 010, \ldots, 111$. There are $2^n$ such strings. Alternatively, think inductively: every subset of $\{a_1, \ldots, a_n\}$ either contains $a_n$ or does not, so the count doubles with each new element. Two plans, each provoked by a specific question.

**Carrying out.** The binary-string map is a bijection; check injectivity and surjectivity. The inductive recurrence $f(n) = 2f(n-1)$ with $f(0)=1$ gives $f(n) = 2^n$. Both arguments are short enough that every step can be verified on sight.

**Looking back.** Check boundaries ($2^0 = 1$). Compare two independent proofs. Note that $\sum_{k=0}^{n}\binom{n}{k} = 2^n$ falls out as a corollary. Ask: where else does the binary-string bijection apply? Lattice paths, bit-masks, power sets, independent binary events. One problem, worked thoroughly, produced a reusable technique.

When this problem appears in later chapters, it will be in service of a specific heuristic: the binary-string representation illustrates *auxiliary elements* and *change of representation*; the inductive argument illustrates *specialization* and *generalization*; looking back illustrates *using the result elsewhere*.


## How to read this edition

| Chapter | Territory |
|---|---|
| **0. The Method** | The four phases, the questions, how to read the book |
| **1. Understanding** | Making the problem graspable before solving it |
| **2. Discovery** | How ideas are found—memory, analogy, the unknown |
| **3. Variation** | What to do when the direct attack stalls |
| **4. Auxiliary Problems** | The indirect route: solve another problem, introduce another object |
| **5. Signs of Progress** | How to tell if your work is moving, stalling, or drifting |
| **6. Plausible Reasoning** | Guessing is not proof, but it is how discovery starts |
| **7. Proof and Review** | Carrying out, proving, checking, and looking back |
| **8. Style, Judgment, and Practice** | Self-training for the developing solver |
| **9. Problems** | Practice problems organized by heuristic move |

Read straight through, or start from wherever you are stuck:

- *I don't know where to begin.* Read **Make the Problem Yours** and **Restate and Represent**.
- *I understand the problem but have no ideas.* Read **Look for a Related Problem**, **Try Small Cases**, and **Generalize**.
- *I'm stuck and nothing works.* Read **Vary the Problem** and **Auxiliary Problems**.
- *I have too many ideas and none of them work.* Read **Signs of Progress** and **Guess, Test, Refine**.
- *I have a guess but can't prove it.* Read **Plausible Reasoning** and **Carry Out the Plan**.
- *I solved it but I'm not sure I learned anything.* Read **Looking Back**.
- *I want to get better at this over time.* Read **Style and Practice**.

Each chapter ends with **Questions to keep**—the few questions most worth internalizing. These are the residue: if you forget everything else, keep the questions. Every chapter makes clear which phase of the solver's protocol it strengthens. The four phases are not one chapter's concern; they are the spine of the entire book.

Each major heuristic entry in the chapters ahead follows a common shape: first *the idea* (Polya's concept, re-voiced), then *concrete moves* (three to six specific sub-strategies, because a general heuristic like "solve a related problem" is actually a family of moves), then *when to reach for it*, then *questions to keep*. This shape is meant to make the heuristics usable, not just readable.

One distinction matters from the start. Polya separates two kinds of problems:

- **Problems to find.** The unknown is a thing—a number, a set, a function. "Find all $x$ such that..." The questions *What is the unknown? What are the data?* belong here.
- **Problems to prove.** The unknown is the truth of a statement. "Prove that for all $n$..." The questions shift: *What is the hypothesis? What is the conclusion?*

If you are proving an inequality and keep asking "What are the data?", you are using the wrong template. Check which kind of problem you have before reaching for the questions. The distinction is developed fully in **Make the Problem Yours**.


## Questions to keep

- **Which phase am I in?** Understanding, planning, executing, or looking back? If you cannot say, you are drifting.
- **What is the unknown?** The single most important question in the book. Ask it first, every time.
- **Have I understood the problem, or have I only read it?** Can you state it in your own words? Can you identify the unknown, the data, and the condition?
- **Can I use the result, or the method, for some other problem?** The question that turns a solved problem into a tool.

Everything else in this book is elaboration, illustration, and practice. The questions are ready to use now, on the next problem you encounter.
