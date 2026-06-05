# Look for a Related Problem

You understand the problem. You know the unknown, the data, the condition. Now you need a plan. Where do you look?

The answer is deceptively simple: look at the unknown. What kind of thing are you trying to find? A count, a formula, a proof, an object satisfying constraints? Strip the problem to its schematic form—"given $\ldots$, find a count"—and let that schema direct your search.

This creates an economy of search. Instead of rummaging through every problem you have ever solved, you search only among problems with the same kind of unknown. The schema narrows the field. If you are looking for a count, you recall counting problems. If you are looking for a proof of an identity, you recall proof techniques for identities. The problem appears schematically, and that schematic form tells you where to look.

## The search starts with the unknown

State the unknown out loud. "I need a count." "I need a bijection." "I need to show divisibility." Now ask: what is the simplest problem I know with that kind of unknown?

If you are looking for a count, the simplest tools are direct enumeration, the multiplication principle, and bijection with something already counted. If you are looking for a proof that two quantities are equal, the simplest tools are algebraic manipulation and induction. You do not need to consider every technique in mathematics. The unknown tells you which shelf to search.

This is not a detour. It is the default starting move whenever you sit down to devise a plan. Look at the unknown first, always.

## Have you seen it before?

You may have solved the same problem before, or one very like it. This is the most direct route to a plan: if you recognise the problem, you already know the shape of the answer.

But "have you seen it before?" is useful even when the answer is no. The question starts a search. It sends you rummaging through what you know. Even if nothing is familiar, the act of asking puts your memory to work.

Polya calls this process *mobilization*: extracting from your dormant knowledge the items that are relevant. Good ideas are based on past experience and formerly acquired knowledge. Mere remembering is not enough for a good idea, but you cannot have any good idea without recollecting some pertinent facts. "Materials alone are not enough for constructing a house, but you cannot construct a house without collecting the necessary materials."

The other half is *organization*: combining what you have recalled into a whole adapted to the problem at hand. You do not just dump remembered facts on the table; you arrange them, connect them, fit them to your present purpose. Mobilization and organization are not separate stages—they are two aspects of the same process.

The practical distinction matters. Sometimes you stall because you have not recalled enough (mobilization is incomplete). Sometimes you stall because you have the pieces but cannot see how they fit (organization is incomplete). Diagnosing which kind of stall you are in tells you what to do next.

## Related problems and theorems

The difficulty is that there are usually too many problems somewhat related to yours. They share a datum, or a condition, or a method. How do you choose the one that is actually useful?

Here is Polya's suggestion, which puts your finger on an essential common point: *try to think of a familiar problem having the same or a similar unknown*.

Suppose you are trying to count the subsets of an $n$-element set. The unknown is a count. You have seen counts before. Which counting problems do you know well? Perhaps you recall that the number of binary strings of length $n$ is $2^n$—each position has two choices, multiply. That is a problem with the same kind of unknown, solved by a clean argument. Could you use it?

You can. There is a bijection between subsets of $\{1, 2, \ldots, n\}$ and binary strings of length $n$: the $k$-th bit is $1$ if element $k$ is in the subset, $0$ if not. So the number of subsets is $2^n$.

The key step was connecting the new problem to a solved one through the unknown. You did not search randomly. You searched among problems with the same unknown—a count—and found one whose method could be transferred.

*Here is a problem related to yours and solved before. Could you use it?* This is the moment the plan begins to crystallise. You know the solution of the related problem but not yet how to use it. So you press further: *Could you use its result? Could you use its method? Should you introduce some auxiliary element in order to make its use possible?*

Sometimes you use the result directly. Sometimes you imitate the method, applying it step by step to the new setting. Sometimes you need to introduce an auxiliary element—a new representation, a relabelling, a bridge concept—to make the connection. The binary-string bijection is exactly such a bridge: an auxiliary representation that lets you transfer a known count to a new setting.

If no problem with the same unknown comes to mind, widen the search: a problem with a similar unknown, or one that shares a key piece of data or condition. But start narrow. The economy of search depends on it.

## Analogy as a way of finding related problems

Analogy is a sort of similarity. Similar objects agree with each other in some respect; analogous objects agree in certain *relations* of their respective parts.

Why does analogy belong in a chapter about related problems? Because analogy is the main mechanism by which you *find* them. When you say "this problem feels like that one," you are recognising an analogy. When you make the analogy precise—a bijection, a shared structure, a parallel argument—you have found a related problem you can use.

**The simpler analogous problem.** The most productive use of analogy is the *simpler analogous problem*. You have a problem about a complicated structure; consider the analogous problem about a simpler one. You have a problem about $n$ objects; consider $n = 1$ or $n = 2$. The simpler problem serves as a *model*. Having solved it, you know the method, and you try to transfer that method to the original.

Consider counting the edges of the complete graph $K_n$. The general formula is not obvious. But the analogous problem for small cases is immediate: $K_2$ has $1$ edge, $K_3$ has $3$, $K_4$ has $6$. The pattern $1, 3, 6, 10, \ldots$ is $\binom{n}{2}$. The analogy between small cases and the general case guides you to the formula, and the formula suggests the proof: each edge is a choice of $2$ vertices from $n$.

**Method, result, or both.** Sometimes you can transfer the *method* of the simpler problem, imitating it point by point. Sometimes you can transfer the *result*, applying it as a lemma. Sometimes you can use both. Even when the method does not transfer immediately, it may be worth modifying it until you find a form that extends to the original.

**When analogies are strong.** An analogical conclusion from many parallel cases is stronger than one from fewer. But quality matters more than quantity. Clear-cut analogies weigh more heavily than vague similarities; systematically arranged instances count for more than random collections of cases.

At the most informal level, two problems "feel alike." At a more precise level, there is a one-to-one correspondence between objects of two systems that preserves certain relations—this is *isomorphism*, the strongest possible analogy. At a still more general level, the correspondence may be many-to-one and still preserve structure—this is *homomorphism*, weaker but still useful. The feeling that two problems are alike is the vaguest form, and even it can be productive. But making the analogy precise is what turns a hunch into a plan.

> *Simplex sigillum veri*—simplicity is the seal of truth.

**When analogies are weak.** A vague analogy that resists being made precise is a warning sign, not an invitation to push harder. If you cannot identify what structural feature the two problems share, the analogy may be misleading you. Set it aside and search for a different related problem. Not every resemblance is useful.

## The search in action

Trace the search through the recurring example. You want to prove that the number of subsets of $\{1, 2, \ldots, n\}$ is $2^n$.

1. **Look at the unknown.** It is a count.
2. **Have you seen it before?** You recall that binary strings of length $n$ number $2^n$.
3. **Related problem.** There it is: a solved problem with the same unknown. Could you use it?
4. **Auxiliary element.** You need a bridge—a bijection between subsets and binary strings. Associate to each subset $S$ the string $b_1 b_2 \cdots b_n$ where $b_k = 1$ if $k \in S$, $0$ otherwise. One-to-one correspondence.
5. **The plan.** Subsets biject with binary strings; binary strings number $2^n$; therefore subsets number $2^n$.

The discovery happened because you connected *look at the unknown* (a count) with *a related problem* (binary strings) through *an auxiliary element* (the bijection). Each move was simple. The combination produced the plan.

## Questions to keep

- *What kind of object am I looking for?* State the unknown's type. This narrows the search.
- *Do I know a solved problem with the same kind of unknown?* Could I use its result? Its method?
- *Is there a simpler analogous problem whose method might transfer?*
- *Is my stall a mobilization problem (not enough recalled) or an organization problem (pieces recalled but not connected)?*
