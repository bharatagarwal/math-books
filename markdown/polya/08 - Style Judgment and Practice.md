# Style, Judgment, and Practice

You have read about the four phases, about discovery and variation and proof. You have a list of questions. Now what?

Now you train. The questions are useless if they stay on a page. They become powerful only when they become reflexes -- when you ask them of yourself, at the right moment, without thinking about asking them. This chapter is about how that training works: what heuristic actually is, how style sharpens thought, and how judgment develops through practice.

## What heuristic is

Polya defines his program precisely:

> Modern heuristic endeavors to understand the process of solving problems, especially the mental operations typically useful in this process. It has various sources of information none of which should be neglected. A serious study of heuristic should take into account both the logical and the psychological background, it should not neglect what such older writers as Pappus, Descartes, Leibnitz, and Bolzano have to say about the subject, but it should least neglect unbiased experience.

This is not a loose aspiration. It is a research program with a specific aim: study the procedures that are *typically* useful in solving problems, stated with enough generality to apply independent of subject matter. Not infallible rules. Not a method guaranteed to work. Procedures that tend to help -- drawn from the accumulated experience of centuries, from Pappus's method of analysis to Descartes's rules for the direction of the mind to Leibnitz's attempts at a universal art of invention.

The questions in this book are the output of that program. Each one hints at a mental operation that skilled solvers perform, often without noticing. "What is the unknown?" prompts you to focus attention. "Have you seen it before?" prompts you to search memory for related problems. "Can you use the result?" prompts you to consolidate what you have gained.

The questions are general -- they apply to counting problems, graph theory, recurrences, formal proofs, and practical engineering problems alike. They are natural -- they are what any intelligent person does when genuinely engaged with a problem. They are common sense stated in general terms. And they are not magic. There is no philosopher's stone here. There are useful habits of thought that you can train.

## Pedantry and mastery

Pedantry and mastery are opposite attitudes toward rules.

To apply a rule rigidly, unquestioningly, in cases where it fits and in cases where it does not fit, is pedantry. Some pedants never understood the rule they apply so conscientiously. Others understood it once, chose a good one, and then stopped thinking.

To apply a rule with natural ease, noticing the cases where it fits, and without ever letting the words of the rule obscure the purpose of the action or the opportunities of the situation -- that is mastery.

The questions in this book are rules of a sort. "What is the unknown?" is a rule: always ask it. But if you ask it mechanically, at the wrong moment, ignoring what the problem is actually telling you, you are being a pedant. The question should arise because you are genuinely confused about what you are looking for, not because it is next on a checklist.

Here is the only rule about rules worth memorizing: **Always use your own brains first.**

You are doing a hard problem. The step you try next should be prompted by an attentive, open-minded look at the problem before you -- not by some rigid habit. Be prepared for various questions and suggestions and use your judgment. If you must rely on a rule, let it be that one.

Consider the difference concretely. You are trying to count the number of spanning trees of the complete graph $K_n$. A pedant works through the list: "What is the unknown? What are the data? Have I seen it before?" -- checking each box, moving on. A master asks "What is the unknown?" and actually pauses: it is a count, a single number, depending on $n$. That pause -- that genuine engagement with the answer -- changes everything. It suggests looking at small cases ($n = 1, 2, 3, 4$), which suggests a pattern, which suggests a conjecture, which leads to Cayley's formula $n^{n-2}$. The pedant asked the same question. The master listened to the answer.

## Rules of discovery

"The first rule of discovery is to have brains and good luck. The second rule of discovery is to sit tight and wait till you get a bright idea."

Polya states this bluntly to kill a fantasy. There are no infallible rules of discovery. "Infallible rules of discovery leading to the solution of all possible mathematical problems would be more desirable than the philosophers' stone, vainly sought by the alchemists. Such rules would work magic; but there is no such thing as magic." The alchemists searched in vain; so will anyone who expects a mechanical procedure that always works.

What exists instead is the program of modern heuristic: study procedures that are *typically* useful, collect them, state them with generality, and practice them. Not always effective. Not guaranteed. Typically useful. The questions in this book are such procedures. They are practiced by every sane person sufficiently interested in a problem. They are natural, obvious, just plain common sense -- stated in general terms.

This is the crucial distinction. You are not learning a method that will solve problems for you. You are learning to notice and name the moves you already make when you are thinking well, so that you can make them more reliably when you are stuck.

## Rules of style

"The first rule of style is to have something to say. The second rule of style is to control yourself when, by chance, you have two things to say; say first one, then the other, not both at the same time."

This applies to proofs, to code, and to mathematical writing of every kind. A proof that tries to establish two things simultaneously is hard to follow. A function that does two things at once is hard to debug. Say one thing. Then say the next thing.

Style in problem-solving is not decoration. It is the discipline of clear thinking made visible. When you write a proof and it feels tangled, the tangle is usually in the thought, not in the words. Restate the problem. Separate the parts. Say first one, then the other.

### Notation

Good notation is unambiguous, suggestive, and easy to remember. "The order and connection of signs should suggest the order and connection of things." When you are counting subsets of an $n$-element set by binary strings, the notation $b_1 b_2 \cdots b_n$ where each $b_i \in \{0, 1\}$ is better than $x_1 x_2 \cdots x_n$ -- because $b$ suggests "bit" or "binary," and that suggestion keeps you oriented. A small advantage, but small advantages compound.

Bad notation costs time. It creates hesitation and confusion that you pay for later. "An important step in solving a problem is to choose the notation. It should be done carefully. The time we spend now on choosing the notation may be well repaid by the time we save later."

### Precision of language

The word "solution" is a trap. It can mean the object satisfying the condition (the roots $1$ and $2$ of $x^2 - 3x + 2 = 0$), the process of obtaining it ("a difficult solution"), or the written result of that process ("a beautiful solution"). If you use the word in all three senses in the same paragraph, the paragraph cannot be clear. Polya notes this as a general problem with the terminology of problem-solving: the activity is familiar to everyone but the terms to describe it are ambiguous, "used in different meanings by different authors."

The discipline is: when you catch yourself using a word in two senses, stop and separate them. This is not pedantry about language -- it is the same move as "say first one, then the other" applied to meaning instead of structure.

### Style of proof

Not every proof needs to be complete in the logician's sense. Polya distinguishes carefully between complete proofs -- leaving no gaps, no loopholes -- and incomplete proofs that capture the germ of an argument.

"Some authors, but not many, have the gift of presenting just the germ of the proof, the main idea in its simplest form, and indicating the nature of the remaining details. Such a proof, although incomplete, may be much more instructive than a proof presented with complete details."

This matters for self-training because most of your first attempts at a proof will be incomplete. The germ appears before the details. When you find the germ, write it down. Distinguish it clearly from a finished proof -- "to confuse one with the other is bad, to sell one for the other is worse" -- but do not discard it. An incomplete proof that exposes the main idea is more valuable than a complete proof you cannot follow.

The cookbook alternative is worse. "Teaching the mechanical performance of routine mathematical operations and nothing else is well under the level of the cookbook because kitchen recipes do leave something to the imagination and judgment of the cook but mathematical recipes do not." A cookbook proof -- all formulas, no ideas -- is correct but uninstructive. An incomplete proof with a visible main idea teaches you something you can use on the next problem.

The intelligent reader of a proof demands two things: to see that each step is correct, and to see the *purpose* of each step. A derivation may be impeccable and still uninstructive if you cannot understand "how it was humanly possible to find such an argument." When you read a proof and cannot see the why of a step, that is the moment to ask: *Did we use all the data?* Often, the purpose of a step is to bring in a datum that has not yet been used. That single question can make an opaque proof transparent.

## Routine problems

A routine problem is one you can solve by substituting into a known formula or by following step-by-step, without any trace of originality, some well-worn example. Solve $x^2 - 3x + 2 = 0$ after six similar quadratics have been solved in front of you -- that is routine. Apply the inclusion-exclusion formula to count derangements of $\{1, 2, 3, 4\}$ after seeing the same formula applied to three other counting problems -- that is routine.

Routine problems are necessary. You need fluency with the basic moves before you can combine them in new ways. A pianist practices scales. A programmer writes straightforward functions before designing systems.

But if you do nothing but routine problems, you never develop judgment. You never face the moment where no formula applies, where you must invent the next step. "To make the students do no other kind is inexcusable."

Since you are training yourself, the balance is yours to set. When you are learning a new technique -- induction, generating functions, the pigeonhole principle -- start with routine problems to build fluency. Then move to problems where the technique is needed but not obvious. Then move to problems where you do not know in advance which technique applies. That third kind is where real skill develops.

## How progress works

Understanding what progress *is* helps you recognize it -- and helps you understand why the questions work.

Polya analyzes progress as having two inseparable aspects: **mobilization** and **organization**.

**Mobilization** is extracting relevant knowledge from memory. Many of the list's questions aim directly at this: *Have you seen it before? Do you know a related problem? Do you know a theorem that could be useful? Look at the unknown! And try to think of a familiar problem having the same or a similar unknown.* Each question creates a new point of contact with your previously acquired knowledge, a new chance that something useful will surface.

**Organization** is combining the mobilized materials into a structure adapted to the problem. The questions for this phase are different: *Here is a problem related to yours and solved before. Could you use it? Could you use its result? Could you use its method? Should you introduce some auxiliary element in order to make its use possible?*

Other questions aim at **variation** -- changing your mode of conception when the current one is stuck: *Could you restate the problem? Could you restate it still differently?* And still others aim at **foresight** -- anticipating the shape of the solution: *Is it possible to satisfy the condition? Is the condition sufficient to determine the unknown?*

The **bright idea** -- the sudden advance, the moment when the path to the solution becomes visible -- is "an abrupt and momentous change of our outlook, a sudden reorganization of our mode of conceiving the problem, a just emerging confident prevision of the steps we have to take." All the questions in the list are concerned with provoking this moment. Understanding the problem, you prepare for it. Devising a plan, you try to provoke it. Having provoked it, you carry it through. Looking back, you try to exploit it better.

This is why the questions work: they are not arbitrary prompts. Each one targets a specific aspect of the mental process -- mobilization, organization, variation, or foresight -- that contributes to progress.

## Practical problems and drawing the line

Unknowns, data, and conditions are more complex and less sharply defined in practical problems than in mathematical ones. A mathematical problem comes with a clean statement. A practical problem -- designing a system, debugging a production issue, planning a migration -- comes with vague constraints, inexhaustible data, and conditions that shade into one another.

The same questions apply, but in modified form. Not "Did you use all the data?" but "Did you use all the data which *could contribute appreciably* to the solution?" Not "Did you use the whole condition?" but "Did you use all the conditions which *could influence appreciably* the solution?"

You take stock of the available information. You collect more if necessary. But eventually you must stop collecting. You must draw the line somewhere, knowing that a margin of uncertainty remains. "If you will sail without danger, you must never put to sea." This is judgment -- knowing when you have enough to act, even though you do not have everything.

## The developing solver

How does the method become second nature? By imitation and practice.

"Solving problems is a practical skill like, let us say, swimming. We acquire any practical skill by imitation and practice. Trying to swim, you imitate what other people do with their hands and feet to keep their heads above water, and, finally, you learn to swim by practicing swimming. Trying to solve problems, you have to observe and to imitate what other people do when solving problems and, finally, you learn to do problems by doing them."

Reading about heuristic is not enough. You must do problems. And after doing them, you must look back.

### Looking back is the most important part

For the developing solver, looking back at the completed solution matters more than any other phase. Polya is explicit:

> Surveying the course of his work and the final shape of the solution, he may find an unending variety of things to observe. He may meditate upon the difficulty of the problem and about the decisive idea; he may try to see what hampered him and what helped him finally. He may look out for simple intuitive ideas: *Can you see it at a glance?* He may compare and develop various methods: *Can you derive the result differently?* He may try to clarify his present problem by comparing it to problems formerly solved; he may try to invent new problems which he can solve on the basis of his just completed work: *Can you use the result, or the method, for some other problem?*

This is where judgment develops. Not by reading about judgment, but by meditating on what worked, what failed, and why.

### Discovering the proper use of the questions

You cannot learn the proper use of a question from explanation alone. The intelligent problem-solver "may understand quite well the explanations and examples illustrating a certain question, he may suspect the proper use of the question; but he cannot attain real understanding unless he comes across the procedure that the question tries to provoke in his own work and, by having experienced its usefulness, discovers the proper use of the question for himself."

This is the core mechanism. You read the question. You apply it clumsily. One day it actually works -- it unsticks you, it produces the key idea. That experience teaches you what no explanation can: when and how this question helps. From then on, the question is yours.

### Discovering your taste

"He should solve problems, choose the problems which are in his line, meditate upon their solution, and invent new problems. By these means, and by all other means, he should endeavor to make his first important discovery: he should discover his likes and his dislikes, his taste, his own line."

This applies to you even if your goal is not to become a mathematician. Discover your taste. Find the problems that genuinely interest you. Interest is fuel; without it, the method stalls.

The future mathematician, Polya says, should "look out for the right model to imitate. He should observe a stimulating teacher. He should compete with a capable friend. Then, what may be the most important, he should read not only current textbooks but good authors till he finds one whose ways he is naturally inclined to imitate." The same applies to you: find authors and solvers whose style you want to absorb. Read not just for results but for *method*.

### The insect, the mouse, and the man

When progress stalls, you must vary your trials -- but with intelligence.

> An insect tries to escape through the windowpane, tries the same hopeless thing again and again, and does not try the next window which is open. A mouse may act more intelligently; caught in the trap, he tries to squeeze through between two bars, then between the next two bars, then between other bars; he varies his trials, he explores various possibilities. A man is able, or should be able, to vary his trials still more intelligently.

"Try, try again" is good advice. But the insect, the mouse, and the man all follow it. The difference is that one *varies the problem* more intelligently than the others.

When you are stuck, the danger is that you get tired of the problem. Your attention falters, your interest fades. "In order to keep the attention alive, the object on which it is directed must unceasingly change." Setting yourself a new question about the problem -- varying it -- reconquers your interest by showing a new aspect. This is not a trick; it is the psychology of sustained work.

## Proverbs worth keeping

Polya collected proverbs that describe the typical procedures of problem-solving. They are not a scientific system -- "many a proverb can be matched with another proverb giving exactly opposite advice, and there is a great latitude of interpretation." But the best of them are vivid, memorable, and true.

**On understanding the problem:**

*Who understands ill, answers ill.* -- If you rush past the problem statement, everything downstream is wrong.

*Think on the end before you begin.* -- Know what you are looking for. This is just "What is the unknown?" in folk dress.

*A fool looks to the beginning, a wise man regards the end.* -- Do not fixate on the data before you understand what you need.

*A wise man begins in the end, a fool ends in the beginning.* -- Work from the goal backward to the given. This is Pappus's method in a sentence.

**On finding the idea:**

*Diligence is the mother of good luck.* -- Bright ideas come to those who have worked hard enough to deserve them.

*If at first you don't succeed, try, try again.* -- But not the same thing. Try different means. Vary the problem.

*Try all the keys in the bunch.* -- Systematic variation beats random repetition.

*A wise man will make tools of what comes to hand.* -- Use what you have. A small observation, a partial result, an analogy -- these are your materials.

*Look around when you have got your first mushroom or made your first discovery; they grow in clusters.* -- One insight often neighbors another. When something works, look nearby.

*Arrows are made of all sorts of wood.* -- Do not be too particular about where your ideas come from.

**On carrying out the plan:**

*Look before you leap.* -- Do not start executing until the plan is ripe.

*Step after step the ladder is ascended.* -- Check each step before moving to the next.

*What a fool does at last, a wise man does at first.* -- The order of execution is often the reverse of the order of discovery.

**On looking back:**

*Second thoughts are best.* -- Always review. The first solution is rarely the best.

*It is safe riding at two anchors.* -- Two independent confirmations are better than one.

**On morale:**

*Where there is a will there is a way.* -- You must actually want to solve the problem.

*A wise man changes his mind, a fool never does.* -- Be willing to abandon a failing approach.

*We soon believe what we desire.* -- The most common fallacy. Watch for it.

### Synthetic proverbs

Polya also invented his own, distilling more systematic points into the same memorable form:

*The end suggests the means.* -- If you know what you want, work backward from it.

*Your five best friends are What, Why, Where, When, and How. You ask What, you ask Why, you ask Where, When, and How -- and ask nobody else when you need advice.*

*Do not believe anything but doubt only what is worth doubting.* -- Credulity and indiscriminate skepticism are both wastes of time.

These synthetic proverbs describe "somewhat more sophisticated attitudes" than the folk originals. They capture the same heuristic procedures in sharper form. They are worth memorizing alongside the folk originals -- they fill in the gaps where common wisdom runs out and more systematic thought begins.

## Sayings of the traditional mathematics professor

The traditional mathematics professor of popular legend "usually appears in public with a lost umbrella in each hand." A few of his sayings have survived:

"In order to solve this differential equation you look at it till a solution occurs to you."

"This principle is so perfectly general that no particular application of it is possible."

"Geometry is the art of correct reasoning on incorrect figures."

"My method to overcome a difficulty is to go round it."

"What is the difference between method and device? A method is a device which you use twice."

These are jokes, but they are not empty. "Correct reasoning on incorrect figures" is a real description of how diagrams work -- they need not be accurate to be useful. "A method is a device which you use twice" is a genuine insight about when an ad hoc trick becomes a reusable technique.

"After all, you can learn something from this traditional mathematics professor."

## Training the self-dialogue

The dialogues in this book -- between solver and problem, between the phases of work -- are not classroom scripts. They are models for the conversation you have with yourself.

Polya says: "To describe thinking as 'mental discourse,' as a sort of conversation of the thinker with himself, is not inappropriate." The questions in the list are prompts for this conversation. When you are stuck, the conversation has gone silent. The questions restart it.

### The structure of the dialogue

The dialogue in this book follows a four-phase structure. In each phase, the same three questions recur: *Where should I start? What can I do? What can I gain by doing so?*

In the understanding phase, you start from the statement, you visualize the problem as a whole, you gain familiarity. In the planning phase, you start from the principal parts clearly arranged, you consider the problem from various sides and seek contacts with formerly acquired knowledge, you gain a helpful idea. In execution, you start from the plan you are confident in, you carry through each step and convince yourself of its correctness, you gain a presentation beyond doubt. In review, you start from the completed solution, you scrutinize method and result, you gain reusable knowledge.

This is the structure you internalize. When solving your own problems, the same three questions -- where am I starting from, what can I do, what will I gain -- keep the self-dialogue organized.

### After solving: reconstruct the dialogue

Where were you stuck? What question, asked at the right moment, would have unstuck you? Write it down. Not the answer -- the question. Over time, you build a personal repertoire of questions that are effective for you.

### When stuck: make the silence explicit

Say to yourself: "I am stuck. What do I know? What do I want? What is the gap between them?" This sounds trivial. It is not. Most wasted time comes from staring at a problem in a fog, without articulating what the difficulty actually is.

### Dramatize the process to yourself

When you solve a problem, replay the key moments. Where did the idea come from? What triggered it? Was it a small case? An analogy? A change of notation? Polya advises: "when the teacher solves a problem before the class, he should dramatize his ideas a little and he should put to himself the same questions which he uses when helping the students." You are both the teacher and the student. Dramatize for yourself. The replay is how the dialogue becomes natural.

### Practice the phases explicitly

On a difficult problem, note what phase you are in. "I am still understanding the problem." "I am looking for a plan." "I have a plan and I am carrying it out." "I am checking." This prevents the common error of trying to carry out a plan you do not yet have, or checking a result you have not yet obtained.

### Keep a problem diary

Not elaborate -- a line or two per problem. What was the key idea? Which heuristic move produced it? What would you do differently? This is "looking back" made concrete, and it is where judgment develops.

## Desire and concentration

The intelligent problem-solver "tries first of all to understand the problem as fully and as clearly as he can. Yet understanding alone is not enough; he must concentrate upon the problem, he must desire earnestly to obtain its solution. If he cannot summon up real desire for solving the problem he would do better to leave it alone. The open secret of real success is to throw your whole personality into your problem."

This is not motivational fluff. It is a description of how the method works. The questions are inert without desire. The desire is what drives the self-dialogue. Without it, you are going through motions. With it, the questions become sharp instruments.

The connection between desire and subconscious work is direct. "Only such problems come back improved whose solution we passionately desire, or for which we have worked with great tension; conscious effort and tension seem to be necessary to set the subconscious work going."

## Subconscious work and when to stop

"Take counsel of your pillow" is old advice, and it works.

You work hard on a problem. You get stuck. You go to sleep, or walk away, or work on something else. The next morning, a bright idea appears. This is subconscious work -- the mind continuing to process the problem below the surface of awareness.

It is real, but it has conditions. You cannot solve problems by sleeping. You solve them by working hard, then sleeping, then working again.

The practical rule: do not set a problem aside without some achievement, however small. Settle at least some little point. Clarify at least some aspect. Then stop. When you return, you will often find that the problem has shifted in your mind, that connections have formed that were not there before.

"Past ages regarded a sudden good idea as an inspiration, a gift of the gods. You must deserve such a gift by work, or at least by a fervent wish."

The balance is: conscious work creates the tension, rest allows the reorganization. Neither alone suffices. Work without rest leads to exhaustion; rest without prior work leads to nothing at all.

## Questions to keep

These are the questions from this chapter that are worth internalizing:

- Am I applying a rule because it fits, or because it is next on my list? (Pedantry vs. mastery.)
- Am I listening to the answers, or just asking the questions?
- Have I stated one thing clearly before moving to the next? (Rules of style.)
- Can I see the purpose of each step in this proof, or only that it is correct? (The intelligent reader's test.)
- Is this problem routine or non-routine for me? Am I practicing the right kind?
- What aspect of progress am I working on -- mobilization, organization, variation, or foresight?
- Where did the key idea come from in the last problem I solved? (Looking back, building judgment.)
- Am I stuck? Can I say precisely *what* I am stuck on?
- Can I set myself a new question about this problem to reconquer my interest?
- Have I worked hard enough on this to deserve a night's sleep on it?
- Do I actually want to solve this problem? If not, why am I working on it?
