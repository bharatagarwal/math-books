# Vary the Problem

When the direct attack stalls, change the problem. Not randomly—deliberately. You keep some parts fixed and alter others. You weaken a condition, specialize a variable, push a parameter to an extreme. The altered problem is not your problem, but solving it may teach you how to solve yours.

This is not a fallback tactic. Variation is the central engine of problem-solving. Trying to solve a problem, you consider different aspects of it in turn, you roll it over and over in your mind. Success depends on choosing the right aspect, on attacking the fortress from its accessible side. To find out which side is accessible, you try various sides—you vary the problem.

Repeated effort helps only when the repetitions differ. If the direct path is blocked, the useful move is not to try harder at the same point but to change the point of attack. "Try, try again" is good advice only when each trial teaches you something and changes the next one.


## Why variation works

Variation keeps your mind engaged. You remember things by association—what you have in mind now recalls what was connected with it before. Varying the problem brings in new points, new contacts, new possibilities of reaching relevant knowledge.

There is a second reason: attention cannot survive stagnation. You cannot solve a worthwhile problem without intense concentration, but you tire quickly when concentrating on the same unchanging point. If your work progresses, there is something new to examine and your interest stays alive. But if you fail to make progress, your attention falters, your thoughts wander, and there is danger of losing the problem altogether. To escape this danger, set yourself a new question about the problem.

When you feel stuck, the worst thing you can do is keep staring at the same formulation. Change something. Even if the new problem does not solve the old one, the act of varying restores your engagement. The new question may reconquer your interest by showing some new aspect of the problem. And from that renewed engagement, the decisive idea may come.


## Change the problem deliberately

Your problem has three principal parts: the unknown, the data, and the condition. When you construct a new problem from the old one, you can:

1. **Keep the unknown and change the rest** (the data and the condition).
2. **Keep the data and change the rest** (the unknown and the condition).
3. **Change both the unknown and the data.**

The first two are safer—you stay closer to the original. The third is more radical, for when the gentler variations have failed. These cases overlap: sometimes you keep both the unknown and the data, and the decisive variation is merely restating the *form* of the condition.


## Drop part of the condition

The single most useful variation: keep the unknown, keep the data, but weaken the condition. Drop a clause. Remove a constraint. See what happens.

When you weaken the condition, you restrict the unknown less. More objects satisfy it. Ask yourself: *How far is the unknown now determined? How can it vary?*

**Example.** You want to count the subsets of an $n$-element set $S$ that have exactly $k$ elements. The condition has two parts: (I) the subset is drawn from $S$, and (II) it has exactly $k$ elements. Drop part (II). Now you count *all* subsets—each element is in or out, giving $2^n$. You understand the full space. Your original question asks how many of those $2^n$ subsets satisfy the additional constraint of having size $k$.

Drop part (I) instead—specialize it. Fix $n = 3$, $k = 2$, and list: $\{a,b\}$, $\{a,c\}$, $\{b,c\}$. Three. Fix $n = 4$, $k = 2$: six. The numbers $1, 3, 6, 10, \ldots$ appear—triangular numbers. You are building toward $\binom{n}{k}$.

The pattern: separate the condition into parts. Keep one, drop the other. Explore the space satisfying the weaker condition. Then check which of those objects also satisfy the dropped part. The two partial conditions function like two loci whose intersection is the answer.

**When to reach for it.** Whenever the full condition feels too tight to work with. Whenever you cannot see the unknown at all under all the constraints. Loosen the grip; see what moves.


## Keep the unknown and change the rest

Once you know the type of the unknown, ask: *Have I solved any problem before that had the same kind of unknown?* Not the same problem—the same *kind* of unknown. If you are counting paths, recall other counting problems. If you need a bijection, recall other bijection arguments. This narrows the search from everything you know to problems with the same shape of answer.

If nothing comes to mind, invent something. Ask: *Could I think of other data appropriate to determine the unknown?* Keep the unknown fixed and imagine different data that would make the problem easier or more familiar.

**Example.** You want to count the subsets of $\{1, 2, \ldots, n\}$ whose elements sum to a given value $s$. That is hard. But the unknown is "a count of subsets." You have solved simpler problems with the same unknown: counting all subsets, counting subsets of a given size. Each is a formerly solved problem with the same kind of unknown. Can you use any of them as a stepping stone?


## Keep the data and derive something useful

Forget the original unknown for a moment and look at what you have. The data. What can you derive from them?

Sometimes a useful intermediate quantity jumps out—a *stepping stone*. It is more accessible than the original unknown and, if you are lucky, useful for finding it afterward. A stepping stone in the middle of a creek is closer to you than the far bank, and once you reach it, it helps you across.

**Example.** Given the recurrence $a_0 = 1$, $a_1 = 1$, $a_n = a_{n-1} + a_{n-2}$, you want a closed form for $a_n$. Before attacking that, derive something from the data: compute the first several terms ($1, 1, 2, 3, 5, 8, 13, 21, \ldots$), compute their ratios ($1, 2, 1.5, 1.667, 1.6, \ldots$). The ratios converge. To what? This new, more accessible question yields $\phi = \frac{1+\sqrt{5}}{2}$. From the growth rate you guess $a_n \approx C\phi^n$, and from there the exact formula follows. You derived a stepping stone before you found the final unknown.


## Extreme cases

Push a parameter to its boundary. Set $n = 0$. Set $n = 1$. Let a variable go to infinity. Let a constraint become vacuous or maximally tight.

Extreme cases serve two purposes. They *test*: if you have a formula, checking it at the extremes is a fast sanity check. They also *suggest*: the behavior at the boundary often reveals the structure of the general case.

**Example.** You conjecture $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. Check the extremes. If $k = 0$: one way to choose nothing, and $\binom{n}{0} = 1$. If $k = n$: one way to choose everything, and $\binom{n}{n} = 1$. If $k = 1$: $n$ choices, and $\binom{n}{1} = n$. These checkpoints do not prove the formula, but any formula that fails one is certainly wrong. And the boundary values constrain the shape of any correct formula—you can use them to *guess* the formula, not just to check it.

As Polya notes, extreme cases are particularly instructive—they are apt to be overlooked by inventors of generalizations, so if a conjecture survives them, the inductive evidence is strong. When an extreme case *does* fail, a single counterexample refutes the conjecture entirely, saving you the effort of attempting a proof.


## When variation fails, then succeeds

Not every variation works. You take away from the original problem the time you devote to the auxiliary one. But a failed variation often contains the seed of a successful one.

**Example.** You need a bijection between binary strings of length $n$ with exactly $k$ ones and $k$-element subsets of $\{1, 2, \ldots, n\}$. First variation: drop the size constraint and build a bijection from *all* binary strings to *all* subsets. That works easily (each string maps to the set of positions where it has a $1$), but it does not directly handle the size constraint. This variation has failed.

But look at what you learned. The bijection preserves size: a string with exactly $k$ ones maps to a subset of size $k$. So the restriction to size-$k$ strings and size-$k$ subsets is itself a bijection. The first variation gave you the machinery; the second, restricting the first, finishes the job. "We may arrive at a more successful trial by modifying an unsuccessful one."

When a variation gives you some useful structure but not the full solution, do not discard it. Ask: can I modify this variation? Restrict it, extend it, combine it with something else?


## Variation and completeness: did you use all the data?

When you derive a formula, check whether every datum appears in the result. If one is missing, something is wrong—or incomplete.

**Example.** Counting lattice paths from $(0,0)$ to $(m,n)$ using steps right and up, the answer is $\binom{m+n}{m}$. Both $m$ and $n$ appear. But if you had mistakenly written $2^{m+n}$, the formula uses $m + n$ but not $m$ and $n$ separately. The question "did you use all the data?" catches the error: the problem distinguishes $m$ from $n$, so any correct formula must depend on them separately.

When you notice a missing datum, you have identified which variation to try next. If your formula omits $n$, vary $n$ and see what changes. The question does not just detect errors—it generates the next productive variation.


### Concrete moves

When the direct attack stalls, here is what to try, roughly from least disruptive to most:

1. **Drop a constraint.** Keep the unknown, weaken the condition. See how the unknown varies under the weaker condition.
2. **Specialize.** Set a parameter to $0$, $1$, $2$, $3$. Look for a pattern. Try an extreme or degenerate case.
3. **Generalize.** Replace a specific object with a family. Replace numbers with letters. (The inventor's paradox.)
4. **Change the unknown.** Keep the data, seek a different quantity—a stepping stone.
5. **Restate the condition.** Go back to definitions. Sometimes the decisive variation is not changing what the problem asks but how it asks it.
6. **Interchange unknown and data.** Take the answer as given and ask what data would produce it. Work backwards.

Not every variation succeeds. But the risk of varying is usually smaller than the risk of staring at the original problem without progress.


## Questions to keep

- *Can I satisfy part of the condition? What happens when I drop the rest?*
- *What happens at the extremes—when a parameter is $0$, $1$, or $\infty$?*
- *Did I use all the data? Is there a datum that does not appear in my result?*
- *Did my last variation fail? What did it teach me? Can I modify it into a better one?*
