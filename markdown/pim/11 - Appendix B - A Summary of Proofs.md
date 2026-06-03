# Appendix B. A Summary of Proofs

## B.1 Propositional and first-order logic

Most mathematical proofs share a common structure. Each has a theorem they’d like to prove, starts from some true statement, and applies simple logical deductions to eventually arrive at the desired claim. Mathematical logic is the mathematical study of frameworks for proving theorems in such a way that could be parsed and verified by a computer. Most of the logic we need in this book is covered by propositional logic—the same sorts of rules that govern the evaluation of a conditional test in a programming language—along with quantifiers for reasoning about classes of objects. Together this is called first-order logic.

I won’t provide a comprehensive introduction to first-order logic. There are many good books on this topic, and I encourage you to read one as a companion to this book. Instead, I will approach propositional logic more casually. I will describe the syntax and semantics of first-order logic in plain language, while a more typical reference would appeal heavily to formulas and symbols. I think many programmers would benefit from a syntactic approach, but then there is a process of returning to plain-English proofs, because very few proofs are written in a style that emphasizes the syntax of first-order logic. It simply makes proofs harder to read. As I hope I’ve stressed enough in this book: mathematical proofs are intended to be written in prose optimized for human readers, and to further human understanding in a way that uses syntax and notation as one of many tools. Nevertheless, the formal foundations for the correctness of mathematical proofs has occupied mathematicians for centuries, and it is worthwhile to see how it is done, even if most proofs need nowhere near as much formality.

The core unit of a claim is called a proposition. For example, “7 is even” is a proposition, albeit a false one, and “$2=2$” is a proposition, which is a tautology in the sense that it is manifestly true without proof. In propositional logic every proposition has a truth value, either true or false, but not both. It is not possible to formulate a proposition that cannot be known to be true or false, because propositional logic has no variables. I.e.,

| $P$ | $Q$ | $P \to Q$ | $Q \to P$ | $(P \to Q)$ and $(Q \to P)$ | $P \leftrightarrow Q$ |
| --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | T | F | F | F |
| F | F | T | T | T | T |

Figure B.1: A truth table for "if and only if."

as a human you may not know how to tell if a statement is true or false (such as "there are infinitely many prime integers"), but its truth value doesn't depend on information not specified in the proposition itself. Of course, if you might use the name  $P$  to refer to a generic proposition, but that is a "variable" of our analysis, not part of the logic itself. Confusingly, some call generic propositions "propositional variables." This will be contrasted with first-order logic momentarily, where variables are first-class citizens.

The core operations performed on propositions are logical connectives, like "and," "or," and "if-then." A compound proposition might be "7 is even and 12 is divisible by 4," or "if 7 is odd then  $7 + 1$  is even." Another logical connective is equivalence, often written as "if and only if," which connects two propositions  $P$  and  $Q$  by asserting that the truth of  $P$  is identical to the truth of  $Q$ . That is, if  $P$  is true then  $Q$  must be true, and if  $P$  is false  $Q$  must be false.

"If-then" statements in propositional logic are often written using an arrow, which denotes "logical implication." You might see  $P \to Q$ , which is the same as "if  $P$  then  $Q$ ." Likewise,  $P \leftarrow Q$  would represent "if  $Q$  then  $P$ ." Finally, if and only if is often written as a double-ended arrow,  $P \leftrightarrow Q$ . One initially strange convention is that if  $P$  is false, then any implication of the form  $P \to Q$  is defined as true. In this way,  $P \to Q$  can be defined as shorthand for "not  $P$ , or  $Q$ ." In other words, the only time  $P \to Q$  can be false is if  $P$  is true, but  $Q$  is false.

For any generic compound proposition, one can write down a truth table that describes the full range of possible truth values the syntactic statement can assume. For example, Figure B.1 shows the truth table that proves  $P \leftrightarrow Q$  is an equivalent statement to "  $P \rightarrow Q$  and  $Q \rightarrow P$ ." This holds regardless of the semantic content of  $P$  and  $Q$ .

First order logic adds variables to propositional logic, meaning statements can have unknown truth values. A claim in first-order logic is called a formula. For example if  $x$  is stated to be a variable ranging over the integers, then "  $x$  is even" is a formula, but its truth value is undetermined absent more knowledge about  $x$ . However, if you interpret  $x$  as 8, then "  $x$  is even" is a true formula; "for every  $x$ ,  $x$  is even," is a false formula; and "there is an  $x$  such that  $x$  is even" is a true formula. These are the three ways that a variable can become "bound" in first-order logic. A variable can be assigned a concrete value. A variable can be universally quantified, meaning we claim the formula is true for all possible assignments. Or, finally, a variable can be existentially quantified, meaning we claim the formula is true for at least one possible assignment. If all variables in a formula are bound, then the formula has a truth value. Often the symbol  $\forall$  is used for the universal quantifier,

as in “$\forall x,\,x$ is even or odd.” Likewise, $\exists$ is the existential quantifier, as in “$\exists x,\,x$ is even.” The domain of values variables can assume is specified by the logical framework itself. For example, one may describe a first-order logic for integers whose values are the symbols $\{\ldots,-3,-2,-1,0,1,2,3,\ldots\}$—syntactically to the logic they are mere symbols, arbitrary as any other, but in our hearts they are the esteemed integers—and which has the additional symbols $<,=$. This would allow you to syntactically phrase mathematical statements pertaining to the ordering of integers.

Once you have a set of rules for constructing statements and interpreting their truth values, you need a set of rules for inferring truth values of statements from known truth values of other statements. There is a long list of inference rules, most of which are common sense. For example, there is a rule (often called *modus ponens*) that says that if you know $P$ is true, and if you know $P\to Q$ is true, then you may conclude that $Q$ is true. Similarly, if “$P$ and $Q$” is true, then you can conclude that $P$ is true. One more: from “not not $P$” being true, you may conclude that $P$ is true. For a complete list, refer to a book or website on first-order logic. None of the rules are surprising.

First-order logic gets additional inference rules related to variables and quantifiers. For example, there is a rule that dictates how a variable may be substituted for a specific value. Similarly, quantifiers get inference rules, such as the following: if “$\forall x,P(x)$” is a true formula (here $P$ is any formula depending on $x$), then you may choose any value for $x$, say $c$, and infer that $P(c)$ is true. Likewise, if there is some $c$ for which $P(c)$ is known to be true, then you can infer the formula “$\exists x,P(x)$.”

Putting all of these together we may start to construct proofs. The statement you’d like to prove is a formula, and there are a set of hypothesis formulas that are assumed to be true. Using the hypotheses, along with any tautologies you wish, a proof is simply a list of logical inference rules applied to any previously proven true formulas to arrive at the theorem.

## B.2 Methods of proof

While a formal proof can have any form legal according to first-order logic (or second-order logic, as the case may be), it is helpful to identify and give names to particular patterns of proof to help with human digestion.

- A *direct proof* proves a formula $P\to Q$ by starting from the assumption $P$, and “going forward” until arriving directly at $Q$.
- A *proof by contrapositive* proves $P\to Q$ by directly proving the equivalent statement “not $Q\to$ not $P$.” (Prove via truth table that these two are equivalent.)
- A *proof by contradiction* proves $P\to Q$ by proving “($P$ and not $Q$) implies $R$,” where $R$ is a contradiction In particular, “$P$ and not $Q$” is the only possibility

if $P\to Q$ is false, so this method assumes the theorem is false and arrives at a trivially false statement. As a consequence, the proved statement “($P$ and not $Q$) implies $R$,” is false, and since $R$ is false, “$P$ and not $Q$” must be false. The negation of “$P$ and not $Q$” is “not $P$, or $Q$,” which is equivalent to $P\to Q$.

There is another important technique, called *proof by induction*, that does not fit neatly in every first-order logical framework (though it does in some, see below). In second-order logic, induction is actually an axiomatic inference rule of the form: for all boolean-valued functions $F:\mathbb{N}\to\{\text{True, False}\}$, if ($P(1)$ and for all $k\in\mathbb{N},P(k)\to P(k+1)$), then for all $n\in\mathbb{N},P(n)$. As we have seen many times in the book, to prove by induction you prove the base case ($P(1)$) and the recursive/inductive step (for all $k\in\mathbb{N},P(k)\to P(k+1)$) separately, and you can infer the theorem is true for any natural number.

For a first-order logic where the universe is the universe of sets, the concept of natural numbers is usually baked into other axioms, and so the induction inference rule can be proved as a theorem. In a logic whose universe of elements are integers, it is baked into axioms about well-ordering. In the end, it is usually singled out as a particularly handy proof technique for the times when you have no other ideas on how to prove a theorem.

Most proofs combine these four basic techniques—direct proof, contrapositive, contradiction, and induction—at different layers. For example, one might start a proof by induction, but then prove the sub-claim “for all $k\in\mathbb{N},P(k)\to P(k+1)$” by contradiction.

Different subfields of mathematics have further groups of techniques which often don’t get catchy names. For example, we’ve used one technique in this book that is common to analytical proofs, which goes as follows. To prove $A(x)<B$ for all $x$, first find a simpler quantity $C$ for which you know that $C<B$, and then prove $A(x)\leq C$. In combinatorics one often finds useful formulas for counting things by regrouping and applying natural formulas. For example, in Chapter 4 we had a proof involving grouping games of a tournament by the losers instead of the rounds of winners. There is also the technique of establishing an invariant, used in multiple chapters in this book (Chapters 6, 12, 16 at least). Mathematicians enjoy identifying the patterns of proof techniques, and generalizing them as much as possible. Programmers often similarly yearn to generalize their programs.

## B.3 How does one actually prove things?

Once you have an intuition for how proofs may be made formal, and you have a grasp on the basic tools for proving simple statements, you will find yourself in a position where you want to prove something and you have no idea how.

This is a frightening stage, but there are simple techniques that can help. In fact, there is an entire book by George Pólya called “How to Solve It” devoted to explaining these techniques. I will describe some techniques I use here, which provide merely a subset of

Pólya’s advice. Before we get to that, there are a number of ways that you can stumble upon something you want to prove.

One common way is when working on another problem and you notice a pattern. For example, you may be working on a number theory problem about square numbers and notice that the difference between successive square numbers is always odd. For example, $25-16=9$ and $81-64=17$. You have already noticed a pattern, you know what it is you want to prove, and you can set out trying to prove it.

Another more tenuous situation is when you have some known inputs, and a known state you’d like to get to, but otherwise no clue on how to get there. For example you may have some quantity you believe is bounded from above by $2$, but you don’t know how to prove it. An example I was working on at the time of this writing consisted of a sum like

$f(t)=A\cos(n2\pi t+p)+B\cos(m2\pi t+q)+C\cos(k2\pi t+r).$

In this sum the numbers $A,B,C$ are fixed positive reals and $n\neq m\neq k$ fixed, distinct positive integers, but the numbers $p,q,r\in[0,2\pi]$ are variable. My goal was to find the choice of $p,q,r$ that made the maximum magnitude of the resulting function as small as possible.

In these more ambiguous cases, first and foremost, you should write down what you want to prove as precisely as you can. Identify the known and unknown parts of the problem. For the cosine problem I’ve dressed it up a bit, to give the most general version of the problem I care about, of which the three-term sum above was a motivating example. If you’re reading this after dipping your toes into the early chapters of this book, pardon the notation salad, and just think of the simpler example above.

**Problem B.1.**

Let $A_{1},\ldots,A_{n}$ be fixed positive real numbers, and $m_{1},\ldots,m_{n}$ be distinct fixed positive integers. What values $p_{1},\ldots,p_{n}\in[0,2\pi]$ achieve the following minimum?

$\min_{p_{1},\ldots,p_{n}}\max_{t\in[0,2\pi]}\left|\sum_{i=1}^{n}A_{i}\cos(m_{i}2\pi t+p_{i})\right|$

With a clear problem in hand, the simplest next step is to write down many examples, and draw pictures, and try to gain an understanding of why the problem resists a proof. Often, simple examples show that my belief about the problem was completely wrong, and it’s actually false for trivial reasons. For the cosine problem above, I plotted a number of different values of the various parameters, and tried to understand a rough idea about what shifts would make the peaks line up, and what shifts would make the troughs line up (both bad situations). I determined that in this case this problem did actually have some meat to it, so I proceed.

Now there are a few techniques I can try. The simplest and most reliable technique, in my opinion, is to make the problem progressively simpler and simpler until you can solve it, and then slowly add back in complexity until you can’t solve it anymore. For the cosine problem above, we can start by fixing all the $A_{i}=1$, and the $m_{i}$ to sequential

integers $m_{i}=i$. After thinking about that version of the problem for a while, it’s still too hard, so I simplify it further by fixing $n$ to small values. Since $n=1$ defeats the problem instantly (the maximum is unchanged no matter what you do), the simplest nontrivial choice is $n=2$.

$f(t)=\cos(2\pi t+p)+\cos(4\pi t+q)$

We can spot one further simplification by noticing that the shift of $p$ in one cosine combined with a shift of $q$ in the other is the same as shifting just the second by $q-p$, so we may as well have only one parameter $r=q-p$. The sum is now simply $\cos(2\pi t)+\cos(4\pi t+r)$.

Now what further resists a proof? We could try to simplify further by letting the two periods $2\pi$ and $4\pi$ be the same value (say, both $2\pi$). We can ignore for the moment that this violates one of the constraints of the problem, in order to determine if that constraint is important. Indeed, such a simplification makes the problem too trivial, because an easily chosen shift of $\pi$ cancels both curves out completely to the zero function. The differing periods (and, it appears, the fact that their ratio is rational) are core ingredients in the fact that a nontrivial minimum can be achieved. At this point, one can try to manually optimize the function to find the right value of $r$, using techniques from calculus. In so accomplishing this task, one reflects on the results. Will the techniques applied generalize to the more complex case of 3 or more curves? If not, at what step does it break down? What, precisely, is the core reason that technique fails? Does that say anything about whether related techniques would also fail? Does that provide any insight into what properties are required of a technique if it is to succeed?

There are a number of other questions naturally raised when doing this simplify-solve-generalize loop. What known problems seem related to this one? For example, the problem above looks like a decomposition called the Fourier series, so one could look for information pertaining to how to tell where the maximum of a finite Fourier series lies.

Another question: can we restate the problem differently to suggest different approaches? For one, I notice that I will fail at my minimization goal if I unluckily cause many peaks of different curves to line up, or many troughs. So somehow I want to mis-align all the peaks relative to all the other peaks, and all the troughs relative to the other troughs. But I can easily compute the peaks and troughs of each curve, they form a discrete set, so maybe it is enough to find an alignment that keeps the peaks and troughs as far away from each other as possible. This idea of mis-aligning peaks and troughs is also a sort of heuristic reasoning that may guide me to a more precise proof.

Another question: can I make the problem more general in a way that helps? Knowing a bit about complex analysis and the famous formula $e^{it}=\cos(t)+i\sin(t)$ suggests to write $\cos(k2\pi t+p)=\operatorname{Re}(e^{i(k2\pi t+p)})$ and work there. Indeed, from that perspective the cosine is the projection of a vector onto the $x$-axis, and the function is a sum of continuously rotating vectors. I want to keep the projection of those vectors from sticking out too far in the horizontal direction left or right (but they may stretch as high or as low as they want). It is worth noting that complex numbers have a rich history of making

some complicated calculus problems much simpler, so it’s reasonable to expect they might help in this situation.

Another question: can I find a good approximation to the thing I want to prove? Perhaps instead of finding the exact minimum of the exact function, I can find the exact minimum of an approximation to the function, or an approximate minimum to the exact function, or an approximate minimum to an approximate function. In each of these I could apply various types of approximations, such as Taylor series (Chapter 8), and try to measure the quality of the approximations.

I would be remiss to neglect the programmer’s favorite approach: I could try to do a brute-force search for solutions to a large class of simple examples, and look for patterns in the results. I have applied this to surprising success on multiple occasions, deriving conjectures that turned into pleasantly simple proofs.

There are many other questions I could ask, but in puzzling over each I form a rough plan of attack for the problem. I get leads for topics to read about that may help, I find a new way to picture the problem, and I can apply each to my list of examples to evaluate whether it is worth pursuing. As I learn more mathematics in general, I find more and newer ways to approach problems.

What’s most important about having all of these leads is that one feels like one is making progress. It is completely useless to write down a problem with nowhere to go from there. The process of simplifying and generalizing in different ways, in addition to the loop of conjecture and proof or refutation, preserves momentum, upholds determination, and preserves sanity through trying times.

Beyond searching for leads, there is the practical matter of prioritization. How do you choose which lead to follow, and for how long should you keep at it before switching tacks? How do you keep track of your progress so that you can easily resume where you left off, or revisit an approach later? In my view the answers to this are deeply personal. Everyone has different styles of managing their “To Do” list and project management. But I will share some thoughts.

Many mathematicians I know, including myself, keep notebooks of various sorts for the off-hand thoughts and tinkering that is too embarrassing to show to the world. Some mathematicians take this a bit further. They rely on the idea expounded in this book that, once you have a nugget of insight, you can hide the details to reduce overhead and re-derive them as needed. As such, the way to “keep track” of a lead may be as simple as a line “Try Fourier series.” One might spend a working session working that angle on a blackboard or scratch paper, or do an extensive literature search, and at the end derive one clear limitation or bit of progress, such as “odd/even makes a big difference.” The intermediate scratch work is often discarded, and can be recreated (often clearer and more concisely) later. As my advisor’s advisor would say (told to me by my advisor), “If you can’t recreate it later, then it was probably wrong anyway.” Luckily, the nugget of insight is often much easier to write down or remember.

Many others use the process of typesetting their notes (and cleaning/pruning them) to preserve the important bits. This has often helped me find mistakes in my scratch work early—or at least, earlier than when my colleagues and I have declared victory and

are ready to typeset it in a paper submission. Typesetting forces you to slow down and reexamine your work, similar to how writing something manually with a paper and pen makes it easier to remember and makes you more deliberate about what you write.

Appendix C contains references to more formal treatments of logic, and practical proof reading and writing skills.
