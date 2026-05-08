## 1 What is a Proof?

## 1.1 Propositions

**Definition.** A *proposition* is a statement (communication) that is either true or false.

For example, both of the following statements are propositions. The first is true, and the second is false.

**Proposition 1.1.1.** $2 + 3 = 5$.

**Proposition 1.1.2.** $1 + 1 = 3$.

Being true or false doesn't sound like much of a limitation, but it does exclude statements such as "Wherefore art thou Romeo?" and "Give me an $A$!" It also excludes statements whose truth varies with circumstance such as, "It's five o'clock," or "the stock market will rise tomorrow."

Unfortunately it is not always easy to decide if a proposition is true or false:

**Proposition 1.1.3.** For every nonnegative integer, $n$, the value of $n^2 + n + 41$ is prime.

(A prime is an integer greater than 1 that is not divisible by any other integer greater than 1. For example, 2, 3, 5, 7, 11, are the first five primes.) Let's try some numerical experimentation to check this proposition. Let

$$
p(n) ::= n^2 + n + 41. \tag{1.1}
$$

We begin with $p(0) = 41$, which is prime; then

$$
p(1) = 43, p(2) = 47, p(3) = 53, \dots, p(20) = 461
$$

are each prime. Hmmm, starts to look like a plausible claim. In fact we can keep checking through $n = 39$ and confirm that $p(39) = 1601$ is prime.

But $p(40) = 40^2 + 40 + 41 = 41 \cdot 41$, which is not prime. So it's not true that the expression is prime for all nonnegative integers. In fact, it's not hard to show that no polynomial with integer coefficients can map all nonnegative numbers into. 1The symbol ::= means "equal by definition." It's always ok simply to write "=" instead of ::=, but reminding the reader that an equality holds by definition can be helpful.

prime numbers, unless it's a constant (see Problem 1.17). But the real point of this example is to show that in general, you can't check a claim about an infinite set by checking a finite set of its elements, no matter how large the finite set.

By the way, propositions like this about all numbers or all items of some kind are so common that there is a special notation for them. With this notation, Proposition 1.1.3 would be

$$
\forall n \in \mathbb {N}. p (n) \text { is prime.} \tag {1.2}
$$

Here the symbol  $\forall$  is read "for all." The symbol  $\mathbb{N}$  stands for the set of nonnegative integers: 0, 1, 2, 3, ... (ask your instructor for the complete list). The symbol " $\in$ " is read as "is a member of," or "belongs to," or simply as "is in." The period after the  $\mathbb{N}$  is just a separator between phrases.

Here are two even more extreme examples:

**Proposition 1.1.4.** [Euler's Conjecture] The equation

$$
a ^ {4} + b ^ {4} + c ^ {4} = d ^ {4}
$$

has no solution when  $a, b, c, d$  are positive integers.

Euler (pronounced "oiler") conjectured this in 1769. But the proposition was proved false 218 years later by Noam Elkies at a liberal arts school up Mass Ave. The solution he found was  $a = 95800$ ,  $b = 217519$ ,  $c = 414560$ ,  $d = 422481$ .

In logical notation, Euler's Conjecture could be written,

$$
\forall a \in \mathbb {Z} ^ {+} \forall b \in \mathbb {Z} ^ {+} \forall c \in \mathbb {Z} ^ {+} \forall d \in \mathbb {Z} ^ {+}. a ^ {4} + b ^ {4} + c ^ {4} \neq d ^ {4}.
$$

Here,  $\mathbb{Z}^+$  is a symbol for the positive integers. Strings of  $\forall$ 's like this are usually abbreviated for easier reading:

$$
\forall a, b, c, d \in \mathbb {Z} ^ {+}. a ^ {4} + b ^ {4} + c ^ {4} \neq d ^ {4}.
$$

**Proposition 1.1.5.**  $313(x^{3} + y^{3}) = z^{3}$  has no solution when  $x, y, z \in \mathbb{Z}^{+}$ .

This proposition is also false, but the smallest counterexample has more than 1000 digits!

It's worth mentioning a couple of further famous propositions whose proofs were sought for centuries before finally being discovered:

**Proposition 1.1.6 (Four Color Theorem).** Every map can be colored with 4 colors so that adjacent regions have different colors.

2Two regions are adjacent only when they share a boundary segment of positive length. They are not considered to be adjacent if their boundaries meet only at a few points.

Several incorrect proofs of this theorem have been published, including one that stood for 10 years in the late 19th century before its mistake was found. A laborious proof was finally found in 1976 by mathematicians Appel and Haken, who used a complex computer program to categorize the four-colorable maps. The program left a few thousand maps uncategorized, which were checked by hand by Haken and his assistants-among them his 15-year-old daughter.

There was reason to doubt whether this was a legitimate proof: the proof was too big to be checked without a computer. No one could guarantee that the computer calculated correctly, nor was anyone enthusiastic about exerting the effort to recheck the four-colorings of thousands of maps that were done by hand. Two decades later a mostly intelligible proof of the Four Color Theorem was found, though a computer is still needed to check four-colorability of several hundred special maps. (See Robin Wilson's "Four Colors Suffice" for the full story.)

**Proposition 1.1.7 (Fermat's Last Theorem).** There are no positive integers $x$, $y$, and $z$ such that

$$
x^n + y^n = z^n
$$

for some integer $n > 2$.

In a book he was reading around 1630, Fermat claimed to have a proof for this proposition, but not enough space in the margin to write it down. Over the years, the Theorem was proved to hold for all $n$ up to 4,000,000, but we've seen that this shouldn't necessarily inspire confidence that it holds for all $n$. There is, after all, a clear resemblance between Fermat's Last Theorem and Euler's false Conjecture. Finally, in 1994, British mathematician Andrew Wiles gave a proof, after seven years of working in secrecy and isolation in his attic. His proof did not fit in any margin. (Wiles' original proof was wrong, but he and collaborators arrived at a correct proof a year later—see Simon Singh's "Fermat's Enigma".)

Finally, let's mention another simply stated proposition whose truth remains unknown.

**Proposition 1.1.8 (Goldbach's Conjecture).** Every even integer greater than 2 is the sum of two primes.

Goldbach's Conjecture dates back to 1742. It is known to hold for all numbers up to $10^{18}$, but to this day, no one knows whether it's true or false.


For a computer scientist, some of the most important things to prove are the correctness of programs and systems-whether a program or system does what it's supposed to. Programs are notoriously buggy, and there's a growing community of researchers and practitioners trying to find ways to prove program correctness. These efforts have been successful enough in the case of CPU chips that they are now routinely used by leading chip manufacturers to prove chip correctness and avoid mistakes like the notorious Intel division bug in the 1990's.

Developing mathematical methods to verify programs and systems remains an active research area. We'll illustrate some of these methods in Chapter 5.

## 1.2 Predicates

A predicate can be understood as a proposition whose truth depends on the value of one or more variables. So " $n$  is a perfect square" describes a predicate, since you can't say if it's true or false until you know what the value of the variable  $n$  happens to be. Once you know, for example, that  $n$  equals 4, the predicate becomes the true proposition "4 is a perfect square". Remember, nothing says that the proposition has to be true: if the value of  $n$  were 5, you would get the false proposition "5 is a perfect square."

Like other propositions, predicates are often named with a letter. Furthermore, a function-like notation is used to denote a predicate supplied with specific variable values. For example, we might use the name " $P$ " for predicate above:

$$
P (n) ::= "n \text{ is a perfect square"}
$$

and repeat the remarks above by asserting that  $P(4)$  is true, and  $P(5)$  is false.

This notation for predicates is confusingly similar to ordinary function notation. If  $P$  is a predicate, then  $P(n)$  is either true or false, depending on the value of  $n$ . On the other hand, if  $p$  is an ordinary function, like  $n^2 + 1$ , then  $p(n)$  is a numerical quantity. Don't confuse these two!

## 1.3 The Axiomatic Method

The standard procedure for establishing truth in mathematics was invented by Euclid, a mathematician working in Alexandria, Egypt around 300 BC. His idea was to begin with five assumptions about geometry, which seemed undeniable based on direct experience. (For example, "There is a straight line segment between every

pair of points".) Propositions like these that are simply accepted as true are called *axioms*.

Starting from these axioms, Euclid established the truth of many additional propositions by providing "proofs." A *proof* is a sequence of logical deductions from axioms and previously proved statements that concludes with the proposition in question. You probably wrote many proofs in high school geometry class, and you'll see a lot more in this text.

There are several common terms for a proposition that has been proved. The different terms hint at the role of the proposition within a larger body of work.

- Important true propositions are called *theorems*.
- A *lemma* is a preliminary proposition useful for proving later propositions.
- A *corollary* is a proposition that follows in just a few logical steps from a theorem.

These definitions are not precise. In fact, sometimes a good lemma turns out to be far more important than the theorem it was originally used to prove.

Euclid's axiom-and-proof approach, now called the *axiomatic method*, remains the foundation for mathematics today. In fact, just a handful of axioms, called the Zermelo-Fraenkel with Choice axioms (ZFC), together with a few logical deduction rules, appear to be sufficient to derive essentially all of mathematics. We'll examine these in Chapter 7.

## 1.4 Our Axioms

The ZFC axioms are important in studying and justifying the foundations of mathematics, but for practical purposes, they are much too primitive. Proving theorems in ZFC is a little like writing programs in byte code instead of a full-fledged programming language-by one reckoning, a formal proof in ZFC that $2+2=4$ requires more than 20,000 steps! So instead of starting with ZFC, we're going to take a *huge* set of axioms as our foundation: we'll accept all familiar facts from high school math.

This will give us a quick launch, but you may find this imprecise specification of the axioms troubling at times. For example, in the midst of a proof, you may start to wonder, "Must I prove this little fact or can I take it as an axiom?" There really is no absolute answer, since what's reasonable to assume and what requires proof depends on the circumstances and the audience. A good general guideline is simply to be up front about what you're assuming.

### 1.4.1 Logical Deductions

Logical deductions, or *inference rules*, are used to prove new propositions using previously proved ones.

A fundamental inference rule is *modus ponens*. This rule says that a proof of $P$ together with a proof that $P$ IMPLIES $Q$ is a proof of $Q$.

Inference rules are sometimes written in a funny notation. For example, *modus ponens* is written:

**Rule.**

$$
\frac{P, \quad P \text{ IMPLIES } Q}{Q}
$$

When the statements above the line, called the *antecedents*, are proved, then we can consider the statement below the line, called the *conclusion* or *consequent*, to also be proved.

A key requirement of an inference rule is that it must be *sound*: an assignment of truth values to the letters, $P, Q, \ldots$, that makes all the antecedents true must also make the consequent true. So if we start off with true axioms and apply sound inference rules, everything we prove will also be true.

There are many other natural, sound inference rules, for example:

**Rule.**

$$
\frac{P \text{ IMPLIES } Q, \quad Q \text{ IMPLIES } R}{P \text{ IMPLIES } R}
$$

**Rule.**

$$
\frac{\text{NOT}(P) \text{ IMPLIES NOT}(Q)}{Q \text{ IMPLIES } P}
$$

On the other hand,

**Non-Rule.**

$$
\frac{\text{NOT}(P) \text{ IMPLIES NOT}(Q)}{P \text{ IMPLIES } Q}
$$

is not sound: if $P$ is assigned $\mathbf{T}$ and $Q$ is assigned $\mathbf{F}$, then the antecedent is true and the consequent is not.

As with axioms, we will not be too formal about the set of legal inference rules. Each step in a proof should be clear and "logical"; in particular, you should state what previously proved facts are used to derive each new conclusion.
### 1.4.2 Patterns of Proof

In principle, a proof can be *any* sequence of logical deductions from axioms and previously proved statements that concludes with the proposition in question. This freedom in constructing a proof can seem overwhelming at first. How do you even *start* a proof?

Here's the good news: many proofs follow one of a handful of standard templates. Each proof has it own details, of course, but these templates at least provide you with an outline to fill in. We'll go through several of these standard patterns, pointing out the basic idea and common pitfalls and giving some examples. Many of these templates fit together; one may give you a top-level outline while others help you at the next level of detail. And we'll show you other, more sophisticated proof techniques later on.

The recipes below are very specific at times, telling you exactly which words to write down on your piece of paper. You're certainly free to say things your own way instead; we're just giving you something you *could* say so that you're never at a complete loss.

## 1.5 Proving an Implication

Propositions of the form "If $P$, then $Q$" are called *implications*. This implication is often rephrased as "$P$ implies $Q$."

Here are some examples:

- (Quadratic Formula) If $ax^2 + bx + c = 0$ and $a \neq 0$, then

$$
x = \left(- b \pm \sqrt {b ^ {2} - 4 a c}\right) / 2 a.
$$

- (Goldbach's Conjecture 1.1.8 rephrased) If $n$ is an even integer greater than 2, then $n$ is a sum of two primes.

- If $0 \leq x \leq 2$, then $-x^{3} + 4x + 1 > 0$.

There are a couple of standard methods for proving an implication.

### 1.5.1 Method #1

In order to prove that $P$ implies $Q$:

1. Write, "Assume $P$."

2. Show that $Q$ logically follows.

## Example

**Theorem 1.5.1.** If $0 \leq x \leq 2$, then $-x^3 + 4x + 1 > 0$.

Before we write a proof of this theorem, we have to do some scratchwork to figure out why it is true.

The inequality certainly holds for $x = 0$; then the left side is equal to 1 and $1 > 0$. As $x$ grows, the $4x$ term (which is positive) initially seems to have greater magnitude than $-x^3$ (which is negative). For example, when $x = 1$, we have $4x = 4$, but $-x^3 = -1$ only. In fact, it looks like $-x^3$ doesn't begin to dominate until $x > 2$. So it seems the $-x^3 + 4x$ part should be nonnegative for all $x$ between 0 and 2, which would imply that $-x^3 + 4x + 1$ is positive.

So far, so good. But we still have to replace all those "seems like" phrases with solid, logical arguments. We can get a better handle on the critical $-x^3 + 4x$ part by factoring it, which is not too hard:

$$
- x ^ {3} + 4 x = x (2 - x) (2 + x)
$$

Aha! For $x$ between 0 and 2, all of the terms on the right side are nonnegative. And a product of nonnegative terms is also nonnegative. Let's organize this blizzard of observations into a clean proof.

**Proof.** Assume $0 \leq x \leq 2$. Then $x, 2 - x$, and $2 + x$ are all nonnegative. Therefore, the product of these terms is also nonnegative. Adding 1 to this product gives a positive number, so:

$$
x (2 - x) (2 + x) + 1 > 0
$$

Multiplying out on the left side proves that

$$
- x ^ {3} + 4 x + 1 > 0
$$

as claimed.

There are a couple points here that apply to all proofs:

- You'll often need to do some scratchwork while you're trying to figure out the logical steps of a proof. Your scratchwork can be as disorganized as you like-full of dead-ends, strange diagrams, obscene words, whatever. But keep your scratchwork separate from your final proof, which should be clear and concise.
- Proofs typically begin with the word "Proof" and end with some sort of delimiter like □ or "QED." The only purpose for these conventions is to clarify where proofs begin and end.
### 1.5.2 Method #2 - Prove the Contrapositive

An implication ("$P$ IMPLIES $Q$") is logically equivalent to its contrapositive

$$
\mathrm{NOT}(Q) \text{ IMPLIES } \mathrm{NOT}(P).
$$

Proving one is as good as proving the other, and proving the contrapositive is sometimes easier than proving the original statement. If so, then you can proceed as follows:

1. Write, "We prove the contrapositive:" and then state the contrapositive.
2. Proceed as in Method #1.

## Example

**Theorem 1.5.2.** If $r$ is irrational, then $\sqrt{r}$ is also irrational.

A number is rational when it equals a quotient of integers - that is, if it equals $m/n$ for some integers $m$ and $n$. If it's not rational, then it's called irrational. So we must show that if $r$ is not a ratio of integers, then $\sqrt{r}$ is also not a ratio of integers. That's pretty convoluted! We can eliminate both not's and simplify the proof by using the contrapositive instead.

**Proof.** We prove the contrapositive: if $\sqrt{r}$ is rational, then $r$ is rational.

Assume that $\sqrt{r}$ is rational. Then there exist integers $m$ and $n$ such that:

$$
\sqrt{r} = \frac{m}{n}
$$

Squaring both sides gives:

$$
r = \frac{m^2}{n^2}
$$

Since $m^2$ and $n^2$ are integers, $r$ is also rational.

## 1.6 Proving an "If and Only If"

Many mathematical theorems assert that two statements are logically equivalent; that is, one holds if and only if the other does. Here is an example that has been known for several thousand years:

Two triangles have the same side lengths if and only if two side lengths and the angle between those sides are the same.

The phrase "if and only if" comes up so often that it is often abbreviated "iff."

### 1.6.1 Method #1: Prove Each Statement Implies the Other

The statement "$P$ IFF $Q$" is equivalent to the two statements "$P$ IMPLIES $Q$" and "$Q$ IMPLIES $P$." So you can prove an "iff" by proving two implications:

1. Write, "We prove $P$ implies $Q$ and vice-versa."
2. Write, "First, we show $P$ implies $Q$." Do this by one of the methods in Section 1.5.
3. Write, "Now, we show $Q$ implies $P$." Again, do this by one of the methods in Section 1.5.

### 1.6.2 Method #2: Construct a Chain of Iffs

In order to prove that $P$ is true iff $Q$ is true:

1. Write, "We construct a chain of if-and-only-if implications."
2. Prove $P$ is equivalent to a second statement which is equivalent to a third statement and so forth until you reach $Q$.

This method sometimes requires more ingenuity than the first, but the result can be a short, elegant proof.

## Example

The standard deviation of a sequence of values $x_{1}, x_{2}, \ldots, x_{n}$ is defined to be:

$$
\sqrt{\frac{(x_{1} - \mu)^{2} + (x_{2} - \mu)^{2} + \cdots + (x_{n} - \mu)^{2}}{n}} \tag{1.3}
$$

where $\mu$ is the average or mean of the values:

$$
\mu ::= \frac{x_{1} + x_{2} + \cdots + x_{n}}{n}
$$

**Theorem 1.6.1.** The standard deviation of a sequence of values $x_{1}, \ldots, x_{n}$ is zero iff all the values are equal to the mean.

For example, the standard deviation of test scores is zero if and only if everyone scored exactly the class average.

**Proof.** We construct a chain of "iff" implications, starting with the statement that the standard deviation (1.3) is zero:

$$
\sqrt{\frac{(x_{1} - \mu)^{2} + (x_{2} - \mu)^{2} + \cdots + (x_{n} - \mu)^{2}}{n}} = 0. \tag{1.4}
$$

## 1.7 Proof by Cases

Now since zero is the only number whose square root is zero, equation (1.4) holds iff

$$
(x_1 - \mu)^2 + (x_2 - \mu)^2 + \cdots + (x_n - \mu)^2 = 0. \tag{1.5}
$$

Squares of real numbers are always nonnegative, so every term on the left hand side of equation (1.5) is nonnegative. This means that (1.5) holds iff

Every term on the left hand side of (1.5) is zero. \tag{1.6}

But a term $(x_i - \mu)^2$ is zero iff $x_i = \mu$, so (1.6) is true iff

Every $x_i$ equals the mean.
