# Is the Condition Possible?

Before you invest effort in solving, ask a blunt question: is there even a solution?

This is not a philosophical worry. It is a practical filter. Problems can be contradictory, under-determined, or over-constrained. Discovering any of these early saves you from the worst kind of wasted effort — the kind where you search harder and harder for something that does not exist.

The question belongs to the understanding phase. You have identified the unknown, the data, the condition. Now you check the condition itself.

*Is it possible to satisfy the condition?*

*Is the condition sufficient to determine the unknown? Or is it insufficient? Or redundant? Or contradictory?*

You do not need a proof at this stage. A guess is enough. The point is to develop a feel for the problem before diving in.

## Is the problem reasonable?

An important feature of any problem is the number of solutions it admits. Most interesting problems have exactly one solution; you are inclined to consider such problems the only "reasonable" ones. Ask yourself: is your problem, in this sense, reasonable?

If the unknown is determined uniquely by the data and condition, you are looking for a single answer — a formula, a number, one object. If the unknown is not determined, you need to know that too: you might be looking for a family of solutions, or for conditions that narrow the family, or you might be facing an ill-posed question.

For problems to prove, the corresponding question is: *Is it likely that the proposition is true? Or is it more likely that it is false?* Even a guess focuses your attention. If you suspect the proposition is false, you look for counterexamples. If you suspect it is true, you look for structure that would support a proof.

## A contradictory condition

Here is a classic example from Polya. *Using each of the ten digits $0, 1, 2, \ldots, 9$ exactly once, write numbers whose sum is $100$.*

Before trying combinations, ask: is this even possible?

The digits sum to $0 + 1 + 2 + \cdots + 9 = 45$. Any arrangement of the digits into multi-digit numbers assigns each digit to either the units place or the tens place (or higher, but the total is $100$, so at most two-digit numbers matter). If $t$ is the sum of the digits occupying tens places, then the total sum of all the numbers is $10t + (45 - t) = 9t + 45$. For this to equal $100$, you need $9t = 55$, so $t = 55/9$. But $t$ must be an integer — it is a sum of digits. The condition is contradictory. No solution exists.

The question that triggered this was not "prove something." It was the understanding-phase question "is this even possible?" Asking it saved all the effort you would have spent trying combinations.

A reader who knows the procedure of casting out nines can see the whole argument at a glance: the digit-sum of any number formed from these digits is $45$, which is divisible by $9$; the digit-sum of $100$ is $1$; so no combination of those digits can sum to $100$.

Notice what happened. The feasibility check did not merely flag a problem — it *was* the complete solution. A proof of impossibility. You do not always need to reach the planning phase. Careful understanding can be the whole solution.

## Insufficiency

Some conditions fail not by contradiction but by weakness. They do not pin down a unique answer.

"Find a positive integer $n$ such that $n$ is even." This has infinitely many solutions. The condition is insufficient — it constrains too little. In a textbook, this usually means you misread the problem, or the problem is poorly stated. But in problems you pose for yourself — which happens more and more as you advance — under-determination is common and worth catching early.

When you notice insufficiency, the productive response is to ask what additional constraint would determine the unknown. That question often reveals what the problem is really about.

## Redundancy

Other conditions contain more constraints than necessary. Recognizing redundancy early can simplify your work: you may be able to ignore one clause because the others already imply it.

If the problem says "find a prime $p$ such that $p$ is odd and $p > 5$," the clause "$p$ is odd" is redundant — every prime greater than $5$ is odd. Dropping it costs nothing and simplifies your search space. More importantly, spotting redundancy tells you something about the structure: the constraints are not independent, and that dependence may be a clue.

In harder problems, redundancy is subtler. A system of equations may have one equation that is a linear combination of the others. A set of geometric conditions may include one that follows from the rest. The habit of asking "did I use the whole condition?" — one of Polya's standard questions — is the flip side: if you solved the problem without using one clause, that clause is either redundant or you made an error.

## Hidden assumptions

Beyond contradiction, insufficiency, and redundancy, there is a fourth possibility: the condition rests on an assumption you did not notice.

The problem says "divide the $n$ objects into $k$ equal groups." This silently assumes $k$ divides $n$. If it does not, the problem has no solution — but the impossibility is hidden behind an unstated assumption rather than visible in the explicit conditions.

Checking feasibility means checking these hidden assumptions too. Ask: what must be true about the data for the condition to even make sense? This is where divisibility conditions, non-negativity requirements, connectivity assumptions, and existence conditions live. They are easy to miss because the problem statement takes them for granted.

## The running example

For our subset-counting problem — *how many subsets does a set with $n$ elements have?* — the feasibility check is quick but worth doing.

Is the unknown well-determined? Given $n$, is there exactly one answer? Yes. The number of subsets of a set depends only on the number of elements, not on what the elements are. (A set $\{a, b, c\}$ has exactly the same number of subsets as $\{1, 2, 3\}$, because you can rename elements without changing the subset structure.) The problem is well-posed, and a single formula in $n$ is what you are looking for — not a case analysis depending on the elements.

Is the condition possible? For any non-negative integer $n$, a set with $n$ elements exists, and it has subsets. No contradiction. No hidden assumptions beyond $n \geq 0$.

Is the condition sufficient? Yes — $n$ alone determines the answer. Nothing is missing.

This took thirty seconds. It confirmed that the problem is reasonable and that a clean formula is the right thing to look for. That confirmation is worth having before you start searching.

## Questions to keep

- *Is it possible to satisfy the condition?* Could the condition be contradictory?
- *Is the unknown determined?* Too many solutions, too few, or exactly one?
- *What must be true about the data for the condition to even make sense?* What is assumed but not stated?
- *Did I use the whole condition?* If not, is the unused part redundant — or did I make an error?
