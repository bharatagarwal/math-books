# Make the Problem Yours

"It is foolish to answer a question that you do not understand." Polya says this plainly, and it needs no softening. The foolishness he describes is not rare. It is the most common mistake. You see a problem, you feel a twinge of recognition, and you start computing. Twenty minutes later you have an answer to a question nobody asked.

The first thing you do when you sit down with a problem is make it yours. Not skim it. Not nod at it. Interrogate it. Name its parts. Reach the point where you could set the problem aside for an hour and reconstruct it from memory — not the exact words, but the structure. If you cannot do that, you have not understood it, and everything that follows will be built on sand.

## Start from the statement

Read the problem. Then read it again.

On the first pass, get the shape. What kind of thing is being asked? A number? A set? A proof? A procedure? Do not worry about details yet. Visualize the problem as a whole, as clearly and as vividly as you can.

On the second pass, read for parts. What exactly is given? What exactly is sought? Where does the difficulty lie: in the amount of data, in an unfamiliar term, in a condition that is hard to picture?

Polya calls these two passes "Getting Acquainted" and "Working for Better Understanding." In the first, you see the forest. In the second, you examine the trees — but only as far as you need to. The principle is graduated decomposition: whole first, then parts, and not further than the problem requires.

A common and costly habit is to skip the first pass. You see a familiar-looking term and start fiddling with it before you grasp what the problem is actually asking. Resist this. The whole first, then the parts.

## Unknown, data, condition

Every problem to find has three principal parts:

- **The unknown:** what you are looking for.
- **The data:** what you are given.
- **The condition:** how the unknown is linked to the data.

Ask yourself these three questions, in this order:

*What is the unknown?*

*What are the data?*

*What is the condition?*

These questions sound mechanical. They are mechanical — and that is the point. They work on every problem, from a puzzle to a research question, because they are maximally general. Their generality is what makes them useful: they force you to name things you might otherwise leave vague.

**The running example.** Suppose the problem is: *How many subsets does a set with $n$ elements have?*

What is the unknown? A number: the count of subsets of an $n$-element set.

What are the data? A single positive integer $n$, the size of the set.

What is the condition? Each subset is a selection of zero or more elements from the set, and two subsets are different if they differ in at least one element.

Notice what the exercise already does. It forces you to think about what "subset" means. You need the definition. You need to know that the empty set counts (it selects zero elements) and that the full set counts (it selects all of them). If you did not pause to state the condition, you might forget one of these edge cases and be off by one or two in your count.

The three questions cost you sixty seconds. They save you from the most common failure mode in problem-solving: working hard on a problem you have not actually understood.

## Problems to find vs problems to prove

Not all problems are the same kind. Polya distinguishes two families, and the distinction matters because the questions you ask yourself are different for each.

A **problem to find** asks you to determine some object (a number, a set, a function, a configuration) satisfying a stated condition. The principal parts are the unknown, the data, and the condition.

A **problem to prove** asks you to establish the truth or falsity of a clearly stated assertion. The principal parts are the **hypothesis** (what you assume) and the **conclusion** (what you must show follows).

These are not just labels. They change how you work. For a problem to find, the driving question is *what is the unknown?* For a problem to prove, the driving question splits into two: *what is the hypothesis?* and *what is the conclusion?*

Our subset-counting example is a problem to find: we want a number. But once we guess that the answer is $2^n$, the problem shifts. Now we have a problem to prove: *The number of subsets of an $n$-element set is $2^n$.* The hypothesis is that we have a set with $n$ elements; the conclusion is that the count of its subsets equals $2^n$.

This shift from finding to proving happens constantly. You compute, you guess, you conjecture — and then you must prove. The understanding phase applies to both kinds.

### The parallel structure

For a problem to find:

*What is the unknown? What are the data? What is the condition?*

For a problem to prove:

*What is the hypothesis? What is the conclusion?*

The two sets of questions are structurally the same. "Look at the unknown" corresponds to "look at the conclusion." "Keep only part of the condition" corresponds to "keep only part of the hypothesis." The vocabulary changes; the move does not.

If you cannot state the hypothesis and conclusion distinctly, you do not yet understand the theorem you are trying to prove. And if you cannot see the parallel between find-questions and prove-questions, practice both until the parallel is second nature.

### Recognizing which kind you face

When you sit down with a problem, one of the first things to settle is which kind it is. This is usually obvious, but not always. A problem phrased as "show that..." is a problem to prove. A problem phrased as "find all..." is a problem to find. But "determine whether..." could be either: you may need to find a counterexample (problem to find) or construct a proof (problem to prove), and you will not know which until you have done some work.

The subset problem starts as a problem to find. The moment you write down a conjecture, it becomes a problem to prove. Knowing which phase you are in tells you which questions to ask.

## Questions to keep

- *What is the unknown? What are the data? What is the condition?*
- *Is this a problem to find or a problem to prove?*
- *Can I state the problem from memory, in my own words, without looking at the original?*
- *Did I understand the problem as a whole before going into detail?*
