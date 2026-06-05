# Style and Practice

You have the four phases. You have the questions. Now what?

Now you train. The questions are useless on a page. They become powerful only when they become reflexes, when you ask them at the right moment without thinking about asking them. This chapter is about how that training works: how style sharpens thought, and how judgment develops through practice.

## Pedantry and mastery

Pedantry and mastery are opposite attitudes toward rules.

To apply a rule rigidly, unquestioningly, in cases where it fits and in cases where it does not fit, is pedantry. Some pedants never understood the rule they apply so conscientiously. Others understood it once, chose a good one, and then stopped thinking.

To apply a rule with natural ease, noticing the cases where it fits, and without ever letting the words of the rule obscure the purpose of the action or the opportunities of the situation — that is mastery.

The questions in this book are rules of a sort. "What is the unknown?" is a rule: always ask it. But if you ask it mechanically, at the wrong moment, ignoring what the problem is actually telling you, you are being a pedant. The question should arise because you are genuinely confused about what you are looking for, not because it is next on a checklist.

Here is the only rule about rules worth memorizing: **Always use your own brains first.**

Consider the difference concretely. You are counting the subsets of $\{1, 2, \ldots, n\}$ that contain exactly $k$ elements. A pedant works through the list ("What is the unknown? What are the data? Have I seen it before?"), checking each box, moving on. A master asks "What is the unknown?" and actually pauses: it is a count, a single number, depending on $n$ and $k$. That pause changes everything. It suggests looking at small cases ($n = 3, k = 2$: the subsets $\{1,2\}, \{1,3\}, \{2,3\}$, so $3$). The small cases suggest a pattern. The pedant asked the same question. The master listened to the answer.

## Rules of style

"The first rule of style is to have something to say. The second rule of style is to control yourself when, by chance, you have two things to say; say first one, then the other, not both at the same time."

This applies to proofs, to code, and to mathematical writing of every kind. A proof that tries to establish two things simultaneously is hard to follow. A function that does two things at once is hard to debug. Say one thing. Then say the next thing.

Style in problem-solving is not decoration. It is the discipline of clear thinking made visible. When you write a proof and it feels tangled, the tangle is usually in the thought, not in the words. Restate the problem. Separate the parts. Say first one, then the other.

### Notation

Good notation is unambiguous, suggestive, and easy to remember. "The order and connection of signs should suggest the order and connection of things." When you are counting subsets of an $n$-element set by binary strings, the notation $b_1 b_2 \cdots b_n$ where each $b_i \in \{0, 1\}$ is better than $x_1 x_2 \cdots x_n$, because $b$ suggests "bit" or "binary," and that suggestion keeps you oriented. A small advantage, but small advantages compound.

Bad notation costs time. It creates hesitation and confusion that you pay for later. "An important step in solving a problem is to choose the notation. It should be done carefully. The time we spend now on choosing the notation may be well repaid by the time we save later."

### Precision of language

The word "solution" is a trap. It can mean the object satisfying the condition (the roots $1$ and $2$ of $x^2 - 3x + 2 = 0$), the process of obtaining it ("a difficult solution"), or the written result of that process ("a beautiful solution"). If you use the word in all three senses in the same paragraph, the paragraph cannot be clear.

The discipline is: when you catch yourself using a word in two senses, stop and separate them. This is not pedantry about language; it is "say first one, then the other" applied to meaning instead of structure.

### Style of proof

Not every proof needs to be complete in the logician's sense. Polya distinguishes between complete proofs (leaving no gaps, no loopholes) and incomplete proofs that capture the germ of an argument.

"Some authors, but not many, have the gift of presenting just the germ of the proof, the main idea in its simplest form, and indicating the nature of the remaining details. Such a proof, although incomplete, may be much more instructive than a proof presented with complete details."

An incomplete proof that exposes the main idea is more valuable than a complete proof you cannot follow. But distinguish it clearly from a finished proof: "to confuse one with the other is bad, to sell one for the other is worse."

The intelligent reader of a proof demands two things: to see that each step is correct, and to see the *purpose* of each step. When you read a proof and cannot see the why of a step, ask: *Did we use all the data?* Often, the purpose of a step is to bring in a datum that has not yet been used. That single question can make an opaque proof transparent.

## Routine and non-routine

A routine problem is one you can solve by substituting into a known formula or by following a well-worn example, without any trace of originality. Count the binary strings of length $4$ with exactly two $1$s after you have seen three similar binomial-coefficient problems worked out: that is routine. Apply the formula $\binom{4}{2} = 6$ and move on.

Routine problems are necessary. You need fluency with the basic moves before you can combine them in new ways. A pianist practices scales. A programmer writes straightforward functions before designing systems.

But if you do nothing but routine problems, you never develop judgment. You never face the moment where no formula applies, where you must invent the next step. "Teaching the mechanical performance of routine mathematical operations and nothing else is well under the level of the cookbook because kitchen recipes do leave something to the imagination and judgment of the cook but mathematical recipes do not."

Since you are training yourself, the balance is yours to set. When you are learning a new technique (induction, generating functions, the pigeonhole principle), start with routine problems to build fluency. Then move to problems where the technique is needed but not obvious. Then move to problems where you do not know in advance which technique applies. That third kind is where real skill develops.

## The developing solver

How does the method become second nature? By imitation and practice.

"Solving problems is a practical skill like, let us say, swimming. We acquire any practical skill by imitation and practice. Trying to swim, you imitate what other people do with their hands and feet to keep their heads above water, and, finally, you learn to swim by practicing swimming. Trying to solve problems, you have to observe and to imitate what other people do when solving problems and, finally, you learn to do problems by doing them."

Reading about heuristic is not enough. You must do problems. And after doing them, you must look back.

### Discovering the proper use of the questions

You cannot learn the proper use of a question from explanation alone. You "may understand quite well the explanations and examples illustrating a certain question, he may suspect the proper use of the question; but he cannot attain real understanding unless he comes across the procedure that the question tries to provoke in his own work and, by having experienced its usefulness, discovers the proper use of the question for himself."

You read the question. You apply it clumsily. One day it actually works — it unsticks you, it produces the key idea. That experience teaches you what no explanation can: when and how this question helps. From then on, the question is yours.

### Discovering your taste

"He should solve problems, choose the problems which are in his line, meditate upon their solution, and invent new problems. By these means, and by all other means, he should endeavor to make his first important discovery: he should discover his likes and his dislikes, his taste, his own line."

Find the problems that genuinely interest you. Interest is fuel; without it, the method stalls. Read not just for results but for *method*. Find authors and solvers whose style you want to absorb.

## Training the self-dialogue

The questions in the list are prompts for a conversation you have with yourself. Polya says: "To describe thinking as 'mental discourse,' as a sort of conversation of the thinker with himself, is not inappropriate." When you are stuck, the conversation has gone silent. The questions restart it.

### The recurring three questions

In each phase, the same three questions recur: *Where should I start? What can I do? What can I gain by doing so?*

In understanding, you start from the statement and gain familiarity. In planning, you start from the principal parts clearly arranged and gain a helpful idea. In execution, you start from the plan and gain a presentation beyond doubt. In review, you start from the completed solution and gain reusable knowledge.

These three questions keep the self-dialogue organized when your thinking drifts.

### After solving: reconstruct

Where were you stuck? What question, asked at the right moment, would have unstuck you? Write it down. Not the answer — the question. Over time, you build a personal repertoire of questions that are effective for you.

### When stuck: make the silence explicit

Say to yourself: "I am stuck. What do I know? What do I want? What is the gap between them?" This sounds trivial. It is not. Most wasted time comes from staring at a problem in a fog, without articulating what the difficulty actually is.

Once the gap is explicit, choose the next question deliberately: restate the problem, try a small case, vary a condition, or stop and leave notes for later.

## Questions to keep

- Am I applying a rule because it fits this problem, or because it is next on my list? (The test for pedantry.)
- Have I stated one thing clearly before moving to the next?
- Is this problem routine or non-routine for me right now, and am I practicing the right kind?
- Where did the key idea come from in the last problem I solved?
