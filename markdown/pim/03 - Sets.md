# Chapter 4 Sets

> God created infinity, and man, unable to understand infinity, created finite sets.
>
> – Gian-Carlo Rota

In this chapter we'll lay foundation for the rest of the book. Most of the chapter is devoted to the mathematical language of sets and functions between sets. Sets and functions serve not only as the basis of most mathematics related to computer science, but also as a common language shared between all mathematicians. Sets are the modeling language of math. The first, and usually simplest, way to convert a real world problem into math involves writing down the core aspects of that problem in terms of sets and functions. Unfortunately set theory has a lot of new terminology. The parts that are new to you are best understood by writing down lots of examples.

After converting an idea into the language of sets, you may use the many existing tools and techniques for working with sets. As such, the work one invests into understanding these techniques pays off across all of math. It's largely the same for software: learning how to decompose a complex problem into simple, testable, maintainable functions pays off no matter the programming language or problem you're trying to solve. The same goes for the process of modeling business rules in software in a way that is flexible as the business changes. Sets are a fundamental skill.

At the end of the chapter we'll see the full modeling process for an application called *stable marriages*, which is part of an interdisciplinary field of mathematics and economics called *market design*. In economics, there are occasionally markets in which money can't be used as a medium of exchange. In these instances, one has to find some other mechanism to allow the market to function efficiently. The example we'll see is the medical residency matching market, but similar ideas apply to markets like organ donation and housing allocation. As we'll see, the process of modeling these systems so they can be analyzed with mathematics requires nothing more than fluency with sets and functions. The result is a Nobel-prize winning algorithm used by thousands of medical students every year.

## 4.1 Sets, Functions, and Their -Jections

A set is a collection of unique objects. You've certainly seen sets before in software. In Python they are simply called "sets." In Java they go by HashSet, and in C++ by unordered_set. Functionally they are all equivalent: a collection of objects without repetition. While set implementations often have a menagerie of details—such as immutability of items, collision avoidance techniques, complexity of storing/lookup—mathematical sets "just work." In other words, we don't care how items enter and leave sets, and mutability is not a concern because we aren't hashing anything to look it up. Efficiency is irrelevant.

To start, we need to know how to describe sets. The simplest way is with words. For example, I can describe the set of integers divisible by seven, or the set of primes, or the set of all syntactically correct Java programs. Often the goal of analyzing a mathematical object is to come up with a concrete description of a set, but implicit definitions are a great starting point.

Set-builder notation provides a more syntactic way to describe sets. For example, the set of all positive integers divisible by seven can be written:

$$S = \{x : x \in \mathbb{N}, x \text{ is divisible by } 7\}$$

The notation reads like the sentence in words, where the colon stands for "such that." I.e., "The set of values $x$ such that $x$ is in $\mathbb{N}$ and $x$ is divisible by $7$." Sometimes a vertical bar $|$ is used in place of the colon. The symbols separate the constructive expression from the membership conditions (it's not an output-input pipe as in shell scripting). The $\in$ symbol denotes membership in a set, and the objects in a set are called *elements*.

Fans of functional programming are cheering as they read, because set-builder notation exists in many programming languages as *comprehension* syntax. In a language with infinite list comprehensions, say Haskell, the above would be implemented as follows:

```haskell
[x | x <- [1..], mod x 7 == 0]
```

Lists made with list comprehensions need not have unique elements, while mathematical sets must. And set-builder notation is also more expressive. Put whatever conditions you like after the colon, even if you don't know how to compute them! The left hand side of the colon may also be an expression, as in

$$\{(x, 2x + 1) : 0 \leq x < 10\}$$

Now we turn to some definitions you may already be familiar with. If not, remember it's your job to write down examples. In either case, mathematical texts typically define something once and only once. I will occasionally repeat definitions that are used across chapters, but generally authors will not. You're expected to have understood a definition to an appropriate degree of comfort before continuing.

**Definition 4.1.** The *cardinality* or *size* of a set $A$, denoted $|A|$, is the number of elements in $A$ when that number is finite, and otherwise we say $A$ has *infinite cardinality*. A set with no elements is called the *empty set*, and it has cardinality zero.

**Definition 4.2.** A set $B$ is a *subset* of another set $A$ if every element $b \in B$ is also an element of $A$. This relationship is denoted $B \subset A$. Two sets are said to be *equal* if they contain the same elements. Equivalently, two sets $A, B$ are equal if both $A \subset B$ and $B \subset A$. Set equality is denoted by $A = B$.

Proving one set is a subset of another is usually easy, but not always. The standard technique is to fix $b$ to be an arbitrary element of $B$, and use whatever characteristic defines $B$ to show that $b \in A$ as well. Here's a brief example: the set of integers divisible by $57$ is a subset of the set of integers divisible by $3$, because any number $b$ divisible by $57$ has the form $b = 57 \cdot k = 3 \cdot (19 \cdot k)$, which means it's also divisible by $3$. No alarms and no surprises.

If I have a binary boolean-valued operator like $\in$, then putting a slash through it like $\notin$ denotes the negation of that claim or query. Other slashed operators include $\neq, \not\subset, \not\sim$.

**Definition 4.3.** Given two sets $A$ and $B$, the *complement* of $B$ in $A$ is the set $\{a \in A : a \notin B\}$. The complement is denoted either by $A \setminus B$ or $A - B$, and sometimes $B^{\mathsf{C}}$ when $B \subset A$ and $A$ is clear from context.

You can already see I'm starting to be creatively flexible with set-builder notation. Here $a \in A$ might be interpreted as a boolean-valued expression, suggesting the set has only boolean-valued members. However, reading it as a sentence makes sense of it instead as an assertion: "The set of $a$ in $A$ such that $a$ is not in $B$." Writing it more verbosely, $\{a : a \in A \text{ and } a \notin B\}$ is extra work without significant gain for the reader. If you prefer the verbose version, it's likely because you've spent so long phrasing your thoughts to be machine readable. Appeal to your inner voice here, not your inner type-checker.

**Definition 4.4.** Given sets $A, B$, their *union*, denoted $A \cup B$, is the set $\{x : x \in A \text{ or } x \in B\}$ (inclusive or). The *intersection*, denoted $A \cap B$, is the set $\{x : x \in A \text{ and } x \in B\}$.

It is not trivial to prove formally that every set has a well-defined size. This fact is intertwined with the formal axiomatic framework set theory is based on, called the Zermelo-Fraenkel set theory, often abbreviated as ZF or ZFC. Axiomatic set theory is beyond the scope of this book, but it is one of those topics that every mathematician has seen at least once.

Mathematicians are divided on whether $A \subset B$ allows $A$ to be equal to $B$. Some authors insist, drawing from the $\leq$ and $<$ notation for numbers, that only $A \subseteq B$ allows for $A = B$, and they call $\subset$ the "strict subset" operator. I have never heard a convincing argument that the matter warrants debate, and so I opt for the briefest: $\subset$ allows equality. This book never requires a strict subset operator, but if it did I would use $\subsetneq$.

Hence the name of my blog, Math $\cap$ Programming.

If you want some practice working with basic set definitions, prove that for any two sets $A, B$, the following containments hold: $A \cap B \subset A$ and $A \subset A \cup B$.

**Definition 4.5.** The *product* of two sets $A, B$, denoted $A \times B$, is the set of all ordered pairs of elements in $A$ and elements in $B$. In set-builder notation it is:

$$A \times B = \{(a, b) : a \in A \text{ and } b \in B\}$$

The parentheses denote a tuple, i.e., an ordered list allowing repetition.

The product is the usual way we turn the real line $\mathbb{R}$ into the real plane $\mathbb{R}^2$. That is, $\mathbb{R}^2$ is *defined* to be $\mathbb{R} \times \mathbb{R}$, and $\mathbb{R}^3 = \mathbb{R} \times \mathbb{R} \times \mathbb{R}$. Unpacking this, there is a little confusion over where the parentheses go. That is, should it be $(\mathbb{R} \times \mathbb{R}) \times \mathbb{R}$, or $\mathbb{R} \times (\mathbb{R} \times \mathbb{R})$? These give rise to two different sets. The first is

$$(\mathbb{R} \times \mathbb{R}) \times \mathbb{R} = \{((a, b), c) : a \in \mathbb{R}, b \in \mathbb{R}, c \in \mathbb{R}\}$$

and the second is

$$\mathbb{R} \times (\mathbb{R} \times \mathbb{R}) = \{(a, (b, c)) : a \in \mathbb{R}, b \in \mathbb{R}, c \in \mathbb{R}\}$$

We want these sets to be considered the same. Indeed, the difference between the two is the kind of distinction that programmers are very familiar with, because compilers will refuse to proceed unless the parentheses align. But mathematicians, for reasons we'll see shortly, brush aside the difference and just say they're the "same" set, and they're both equivalent to

$$(\mathbb{R} \times \mathbb{R}) \times \mathbb{R} = \mathbb{R} \times (\mathbb{R} \times \mathbb{R}) = \{(a, b, c) : a \in \mathbb{R}, b \in \mathbb{R}, c \in \mathbb{R}\}$$

We will return later in this chapter, and again in Chapters 9 and 16 when complexity will beg for a rigorous and useful abstraction called the *quotient*, to understand why it's okay to call these two sets "the same." For now, simply define an $n$-fold product to collapse pairs into tuples of length $n$:

$$\mathbb{R}^n = \underbrace{\mathbb{R} \times \cdots \times \mathbb{R}}_{n \text{ times}} = \{(a_1, \ldots, a_n) : a_i \in \mathbb{R} \text{ for every } i\}$$

This notation can be used for any set. Next we define functions as special subsets of a product.

**Definition 4.6.** Let $A, B$ be sets, and let $F$ be a subset of $A \times B$. We say that $F$ is a *function* if it satisfies the following property: for each $a \in A$, there is a unique pair $(a, b) \in F$ (an input must have exactly one output). The set $A$ is called the *domain* of $F$ and $B$ is called the *codomain* of $F$. To denote this, we use the arrow notation $F : A \to B$.

You should be writing down examples, but this one needs some help. We think of functions computationally as mappings from inputs to outputs. So much so that the nouns function and map are synonyms. But this definition of a function is a set. I'm going to convince you that the distinction is merely a matter of notation. It exists to fill the role of a "bare metal" implementation of a function in the modeling language of sets.

For the example, say $F$ is the set of pairs of positive integers and their squares.

$$F = \{(1, 1), (2, 4), (3, 9), (4, 16), \dots\} = \{(x, x^2) : x \in \mathbb{N}\}.$$

It's a subset of $\mathbb{N} \times \mathbb{N}$. Now we can add a bit of notation: instead of saying that $(3, 9) \in F$ we use the mapping notation $F(3) = 9$. With this, we could describe $F$ the way we wanted to all along, as $F(x) = x^2$. The conditions in Definition 4.6 ensure that every input $x$ has some output $F(x)$, and that each input $x$ has only one output $F(x)$. Providing a concrete algorithm to compute the output from the input makes these conditions trivial, as is the case with squared integers, but an algorithm is not needed to define a function.

Reiterating a note from Chapter 2, the codomain $B$ is not strictly encoded in the data of a function $F : A \to B$. The codomain is the set of allowed outputs.

So why go through all the trouble of defining functions in terms of sets? Part of the answer is historical. The concept of sets as a modeling tool has probably existed for as long as mathematics, but it was primarily used in its language form ("I declare, considereth only those heavenly numbers whose factorisation into prymes containeth nary a repeated factor!"). The notation $y = f(x)$ was invented in the 1700's by Leonhard Euler, and in those times most functions were only defined in terms of formulas that were easy to write down. It was not until the late 19th century that mathematicians formally studied sets, and proposed them as a logical foundation for all of mathematics. To do so requires restating all existing concepts in terms of sets. Definition 4.6 does this for functions. Similar definitions exist defining integers and ordered tuples in terms of sets. How tedious.

In this light, our initial definition of a set was completely imprecise. There is a more precise definition, but it is the sort that only a logician would love, called Zermelo-Fraenkel set theory. In brief, its base concepts are the empty set, set membership, a notion of infinity, and a restricted choice of ways to build sets from other sets. Using this one can define numbers, functions—even all of calculus—from "first principles." To instill this idea in future mathematicians, many introductory proof textbooks define everything in terms of sets, and do formal proofs to a degree of precision most mathematicians avoid in their day to day work.

In theory, mathematicians like the idea that everything can be reduced to sets. Actually doing it in practice will drive you mad. It's like writing all your programs in pure binary. Few do it, but we all take comfort in the idea that we could peel back the layers to reveal the raw assembly instructions. In reality, abstractions keep us productive. Likewise, defining the entirety of mathematics in sets is like "bare metal" programming, but without any of the speed benefits of the finished program. Someone ironed out set theory once, and we have a record of their work. Now we can get back to doing mathematics.

The special notation for functions highlights our conceptual emphasis. We think of functions differently than regular sets, with a semantic input-output dependence that set notation doesn't natively convey.

Now we turn to a few useful definitions about subsets of inputs and outputs of a function. A seasoned programmer is less likely to be familiar with the remainder of the definitions in this chapter, but we will rely on them throughout the book.

**Definition 4.7.** Given a function $f : A \to B$, we define the *image* of $f$ (or the image of $A$ under $f$) as the set

$$f(A) = \{f(a) : a \in A\}$$

This is denoted $f(A)$ to signal that we're putting everything in $A$ through $f$, though it is also denoted $\operatorname{im}(f)$ or just $\operatorname{im} f$. If $C \subset A$ is a subset, we can similarly define the image of $C$, denoted $f(C)$, as $f(C) = \{f(c) : c \in C\}$. The image of $A$ is equivalent to the range of a function with domain $A$, but we use a different word so we can speak of the image of a particular subset as well.

As a shorthand for "there exists," mathematicians often use the symbol $\exists$. So an equivalent definition of $\operatorname{im} f$ is

$$\operatorname{im} f = \{b \in B : \exists\, a \in A \text{ with } f(a) = b\}.$$

We won't rely heavily on the $\exists$ notation, but it is quite common. Now we define the preimage, the set of inputs mapping to a specified set of outputs.

**Definition 4.8.** Let $A, B$ be sets and $f : A \to B$ a function. Let $b \in B$. The *preimage* of $b$ under $f$, denoted $f^{-1}(b)$, is the set $\{a \in A : f(a) = b\}$. Likewise, if $C \subset B$ is a subset, then $f^{-1}(C)$ is defined to be $\{a \in A : f(a) \in C\}$.

For $F(x) = x^2$ as a mapping $\mathbb{R} \to \mathbb{R}$, the preimage of $4$ is $F^{-1}(4) = \{-2, 2\}$. The superscript $-1$ is intended to invoke the concept of an inverse function. The preimage generalizes an inverse to operate on any element or subset of the codomain. The preimage always exists, though it may be the empty set.

The next three definitions are quite special.

**Definition 4.9.** A function $f : A \to B$ is called an *injection* (adjectivally, is *injective*) if whenever $a, a' \in A$ are different elements of $A$, then $f(a), f(a')$ are different elements of $B$.

An injection "injects" a copy of $A$ inside $B$ by way of $f$, so that no two elements of $A$ get mapped to the same thing in $B$. For example, $F(x) = x^2$ is an injection from $\mathbb{N} \to \mathbb{N}$, but if we defined it for all integers $\mathbb{Z} \to \mathbb{Z}$ it would not be injective because, by way of counterexample, $(-4)^2 = 4^2 = 16$. Figure 4.1 is the picture you should have in your head whenever you think of an injection. To put injectivity another way, $f : A \to B$ is an injection exactly when the preimage of every element $b \in B$ has size $0$ or $1$.

The three "-jection" properties are easiest to feel by classifying functions as sets of pairs. The demo below builds a genuine bijection on small finite sets, then constructs its inverse $g$ and checks the two inverse laws of Definition 4.11; it also confirms that integer squaring is not injective (the preimage of $4$ is exactly $\{-2, 2\}$) and so cannot be inverted.

```python
<!-- include: code/pim/03 - Sets/02_inverse.py -->
```

<!-- carousel -->
![Figure 4.1: An example of an injection, where different inputs are mapped to different outputs. The dots are elements of the set, and the arrows show the mapping. This example is also a non-surjection.](03 - Sets_images/img-0.jpeg)
![Figure 4.2: An example of a surjection, where every element of the codomain is hit by some element of the domain mapped through $f$. The dots are elements of the set, and the arrows show the mapping. This example is also a non-injection.](03 - Sets_images/img-1.jpeg)
![Figure 4.3: An example of a bijection, which is both an injection and a surjection.](03 - Sets_images/img-2.jpeg)
<!-- endcarousel -->

**Definition 4.10.** A function $f : A \to B$ is called a *surjection* (adjectivally, is *surjective*) if for every $b \in B$, there is some $a \in A$ with $f(a) = b$. In other words, $f$ is surjective if $\operatorname{im} f = B$.

Surjections "hit everything" in $B$ by things mapped from $A$. So our squaring function on integers $F(x) = x^2$ is not a surjection, because $2$ has no integer square root. However, if we redefined it for positive *real* numbers it would be: every positive real number has a positive square root. To phrase it in terms of preimages, a surjection $f : A \to B$ has the property that every $b \in B$ has a nonempty preimage $f^{-1}(b)$.

Another bit of notation, just like $\exists$ meaning "there exists," the symbol $\forall$ is a shorthand for "for all." I remember it by the backwards E standing for Exists, while the upside-down A stands for All. So the surjective property can be written hyper-compactly as

$$\forall\, b \in B,\ \exists\, a \in A \text{ such that } f(a) = b.$$

The symbols $\forall, \exists$ are called *quantifiers* and an expression in which every variable is bound by a quantifier is called "fully quantified."

I will shy away from such dense notation in this book, though it will come in handy when we study Calculus in Chapter 8. While this example is not particularly difficult to parse, unrestrained use of $\forall, \exists$ can quickly spin out of control. Just as programmers shouldn't cram a lot of complex logic into a single line of code, bad mathematical writers cram many quantifiers into a single line of math when it's not necessary. That being said, familiarity with the symbols is broadly assumed.

Finally, $f : A \to B$ is called a *bijection* if it is both a surjection and an injection. Adjectivally $f$ is called *bijective*. A bijection is also called a one-to-one correspondence. Bijections are nice because they can be used to say that two sets have the same cardinality (size), and it makes sense for infinite sets. If there is a bijection $A \to B$ then $|A| = |B|$. Likewise, if there is an injection $A \to B$ then $|A| \leq |B|$, and the opposite works for surjections. See the exercises for more on this. Figure 4.3 shows the typical picture for a bijection.

Being a bijection $f : A \to B$ means every $b \in B$ has a preimage of size exactly $1$. In this case, the idea of an "inverse" to $f$ makes sense: to invert $f$, map $b \in B$ to the unique element $a$ with $f(a) = b$. One denotes this function $f^{-1} : B \to A$. A more precise definition goes as follows.

**Definition 4.11.** An *inverse* of a function $f : A \to B$ is a function $g : B \to A$ satisfying both $g(f(a)) = a$ for every $a \in A$ and $f(g(b)) = b$ for every $b \in B$. If such a $g$ exists, we say $f$ is *invertible*.

All bijections are invertible, and vice versa invertible functions must be bijections. Computing the inverse function given only a description of a function can be notoriously difficult. Indeed, most of cryptography rests on the assumption that some functions are computationally infeasible to invert. On the other hand, in linear algebra it is feasible, though often expensive, to compute the inverse of a matrix. As such, it is worthwhile to study the notion of an inverse in generality. This can grease the wheels of a complicated proof in an advanced setting, but more importantly it separates the mere set-theoretic aspects of a function from application-specific properties.

Here are two such propositions we'll use much later in our study of linear algebra concerning the existence and structure of inverses. If you feel emotionally drained by all the definitions in this chapter so far, feel free to skip these and come back when we refer to them in Chapter 12.

**Proposition 4.12.** *Inverses are unique.*

*Proof.* Let $f : A \to B$ be a bijection and suppose that both $g_1 : B \to A$ and $g_2 : B \to A$ are inverses. We will show $g_1(b) = g_2(b)$ for every $b \in B$. Fix any $b \in B$. Let $a$ be an element of $A$ such that $f(a) = b$. Then $g_1(b) = g_1(f(a)) = a$ and the same reasoning proves $g_2(b) = a$. So $g_1$ and $g_2$ are the same function. $\blacksquare$

The next proposition says that a "left-sided" inverse—satisfying just one of the two requirements to be an inverse—that happens to be a bijection is automatically a two-sided inverse.

**Proposition 4.13.** Let $A, B$ be sets and $f : A \to B$ a bijection. Suppose $g : B \to A$ is a function satisfying $g(f(a)) = a$ for every $a \in A$. Then $g$ is the inverse for $f$, i.e., $f(g(b)) = b$ for every $b \in B$.

*Proof.* It's crucial here that $f$ is surjective (otherwise the theorem is not true!). Given $b \in B$, we need to show that $f(g(b)) = b$. Start by choosing an $a \in A$ for which $f(a) = b$. Then $g(b) = g(f(a)) = a$. Apply $f$ to both sides to get $f(g(b)) = f(a) = b$, as desired. $\blacksquare$

Before we move on let me explain an earlier comment. I said we call $(\mathbb{R} \times \mathbb{R}) \times \mathbb{R} = \mathbb{R} \times (\mathbb{R} \times \mathbb{R})$ by "brushing aside" the differences between the two. There is a rigorous way to do this, but I'll only explain half of the rigor right now. The essential reason is because there is a bijection $(\mathbb{R} \times \mathbb{R}) \times \mathbb{R} \to \mathbb{R} \times (\mathbb{R} \times \mathbb{R})$ that maps $((a, b), c)$ to $(a, (b, c))$. Often when mathematicians want to "call" two things the same, they'll come up with such a bijection, and say the two things on either side of such a bijection should be considered the same. It's like an implicit typecast, always reversible in this case. The formal idea is called a "quotient," which we'll see in Chapter 9.

## 4.2 Clever Bijections and Counting

Now that we have the basic language of sets to model our problems, on to some problems. Say you want to count the size of a set. Since sets can be defined implicitly, it may not be obvious how. A useful tool used all over math is the trick of coming up with a clever bijection. This can transform a seemingly difficult counting problem into an elegantly trivial one.

Our first problem concerns a tournament of tennis players. The tournament is single-elimination, meaning when two players finish a match the winner stays in the tournament and the loser is out. As the tournament host, you want to know how many games will be played in total. That is, given a set of games (each game is a set of two players) generated by this elimination process, we want to count its size.

Say you start with a thousand players. Let's entertain a naive computation. In the first round of the tournament, each player is paired up with another and 500 games are played. In the second round there are 500 remaining players, and they again pair off to play 250 games. In the third, 125 games. In the fourth round you hit an edge case, because there are an odd number of players and one must sit out. Fine, you keep going, diligently tracking the players who sit out, and eventually you get to a number. You should try this yourself, and verify that the answer is 999 games. Isn't that a weird coincidence? We got 1 less than the total number of players. Does this pattern hold for other tournament sizes?

The answer is yes. To prove it, we apply the technique of finding a clever bijection. It will make you feel like our computation was a complete waste of time, but if you did the exercise you'll appreciate the elegance of this method that much more.

The primary observation is that every loser loses exactly one game. So if we want to count the number of games, we can instead count the number of losers. But there is only one player who is not a loser: the winner. Hence 999 games.

Let's rephrase that elegant argument in the language of sets. Let $X$ be the set of games and $Y$ the set of players. Define a function $f : X \to Y$ by calling $f(x)$ the loser of game $x$. This function is not a surjection. Rather, the image $f(X)$ is the subset $L \subset Y$ of losers. However, $f$ is an injection (different games have different losers), and $f$ defines a bijection between $X$ and $L$. This means that $X$ and $L$ have the same size, and the fact that there is only one winner of the entire tournament means that $|L| = |Y| - 1$. So if there are $n$ players then there will always be $n - 1$ games.

The naive simulation and the bijection ought to agree, so let's make them. The demo below runs the messy round-by-round elimination (odd players sitting out and all) to count games, but then directly verifies the bijection's claim: the loser-map is injective and the champion is the one player who is never a loser. It reproduces Kun's $999$ for a thousand players and confirms $n - 1$ for every size and random draw.

```python
<!-- include: code/pim/03 - Sets/03_tournament.py -->
```

To make sure you understand this argument, extend it to the case of a double-elimination tournament. In double-elimination, you are ousted from the tournament once you've lost two games, and a player who loses one game might still ultimately win the tournament. In this case you won't have an injection, but a so-called "double-cover" of the set of players. What I mean by double-cover is that every $y \in Y$ has a preimage $f^{-1}(y) = \{x \in X : f(x) = y\}$ of size (almost) exactly $2$. "Almost," because the winner may have lost zero games or one game. This also means you can't count the number of games exactly, but will be forced to provide bounds.

This general strategy for counting has applications any time you need to count or estimate the size of a set. Imagine you want to estimate the number of homeless people in a city, a problem the US Census Bureau faces regularly. You might implicitly count them by observing the residual effects of their actions. This is precisely looking for functions between sets that are close to bijections, or double- or triple-covers of the set you want to count.

Here is another magnificent example of finding a clever bijection. Given a set $X$ let's define the quantity $\binom{X}{2}$, read "$X$ choose two," to be the set of all unordered pairs of distinct elements of $X$. I.e.,

$$\binom{X}{2} = \{\{x, y\} : x, y \in X \text{ and } x \neq y\}.$$

If $X$ is a finite set of size $n = |X|$, we denote the size of $\binom{X}{2}$ by $\binom{n}{2}$, which doesn't depend on the particular elements in $X$, just its size. In words, $\binom{n}{2}$ is the number of ways to choose two objects from a set of $n$ objects. The problem is, can we come up with an arithmetic formula for $\binom{n}{2}$ in terms of $n$? We'll show by way of a bijection that it's equal to the quantity

$$1 + 2 + \cdots + n - 1.$$

In fact, the bijection is easiest to understand by the picture in Figure 4.4. Here's how we read this picture. We're setting $n = 7$ and calling the lightly shaded balls $Y$, and calling the $n$ squares in the last row $X$. The picture shows how to define a bijection $g : Y \to \binom{X}{2}$: given any ball $y \in Y$, you draw two diagonals as in the picture and you get $g(y)$ as the pair of squares at the end of both diagonals. The picture should convince you that two different choices of balls give you different diagonals, i.e., $g$ is an injection.

![Figure 4.4: A picture proof that $\left|\binom{X}{2}\right| = 1 + 2 + \cdots + n - 1$ when $|X| = n$. Each pair of squares in the bottom row corresponds to a unique ball in the triangular arrangement above it.](03 - Sets_images/img-3.jpeg)

Likewise, given a pair of squares $x_1 \neq x_2 \in X$, the inner diagonals meet at a ball $y$ that maps under $g$ back to $\{x_1, x_2\}$. So $g$ is a surjection, and together with being an injection this makes $g$ a bijection.

Now we count: how many balls and squares are there? The last row has $n - 1 = 6$ balls, and each row has one fewer ball than the row underneath it, so $|Y| = 1 + 2 + \cdots + n - 1$. Moreover, $X$ has $n$ squares in it, so $\left|\binom{X}{2}\right| = \binom{n}{2}$. The bijection tells us that these two values must be equal.

We can put the bijection's two sides on the table side by side. The demo below enumerates the actual set $\binom{X}{2}$ of unordered pairs and compares its size to the triangular count $1 + 2 + \cdots + (n-1)$ (the balls in Figure 4.4) for many $n$ at once. The two columns match exactly, and both equal the textbook $\frac{n(n-1)}{2}$.

```python
<!-- include: code/pim/03 - Sets/04_choose_two.py -->
```

You may wonder: how can we use a picture as the central part of our proof? Didn't we only prove that this bijection works for $n = 7$? Technically you're right: no mathematician would consider a picture as a rigorous proof in and of itself. However, when the goal is to communicate the central nugget of wisdom in a proof, a small example with all the essential features of a general proof is often good enough. Consider one alternative. You could represent the balls as points inside $\mathbb{R}^2$. You'd need a generic way to construct coordinates for them, and a generic way to describe the diagonals. That's a huge pain in the ass for something so simple! Every mathematician would agree it could be done but it would be a colossal waste of time to actually do it.

This is a common feature of more advanced mathematics. Mathematicians are constantly reading papers, and there is rarely enough time to verify all the details of every argument. If you're not an official reviewer of the paper before it's been published, it is usually enough to be convinced that something should be true, especially if the details are messy but clear, while focusing on the high level picture. An example with all the essential features of a general solution is an effective substitute. And this doubles for readers of mathematics too: finding a simple example with the essential features of a general solution, and testing claims on the example, is one of the best ways to read a proof!

## 4.3 Proof by Induction and Contradiction

Next we're going to see two rigorous methods of proof that are used in all areas of math. The first is induction, but you're likely familiar with it by a different name: recursion.

We understand recursion: a function is defined in such a way that it invokes itself for some smaller set of parameters, with a "base case" to process the smallest allowed parameters. The classic example is the Fibonacci sequence $\text{fib}(n)$, defined recursively as

$$\text{fib}(n) = \text{fib}(n - 1) + \text{fib}(n - 2),$$

with $\text{fib}(0) = \text{fib}(1) = 1$. Most programmers have implemented some version of this function early on in their career, since it is a common instrument to teach recursion.

Likewise, induction is a proof technique that allows you to prove a statement by invoking the same statement for smaller parameters, with a similar base case. One difficulty is identifying when and where induction is likely to be used. It's usually when someone is trying to prove a statement which holds for all natural numbers (or all positive integers above some number). So a statement might look like, "For all integers $n \geq 6$, the statement $P(n)$ is true." A proof by induction operates in two steps:

1. First show the *base case*, in this case that $P(6)$ is true.
2. Second, do the *inductive step*, where one uses the assumption that $P(n)$ is true to prove that $P(n + 1)$ is true. Equivalently, one can use $P(n - 1)$ to prove $P(n)$.

Just like with recursion, you get a chain of proofs: $P(6)$ implies $P(7)$ implies … implies $P(n)$ for any $n$ you like. One bit of terminology: one often invokes the *inductive hypothesis*, which is the assumption that $P(n)$ is true. It's helpful when $P(n)$ is cumbersome to restate.

Let's use induction for a second proof that $\binom{n}{2} = 1 + 2 + \cdots + n - 1$.

*Proof.* Call the statement to be proved $P(n)$. We prove this by induction for $n \geq 2$. For the base case $n = 2$, we need to prove

$$P(2) : \binom{2}{2} = 1.$$

We argue $\binom{2}{2}$ is trivially $1$. There is only one way to choose two items from a set of two items. Now assume the inductive hypothesis $P(n)$ holds:

$$P(n) : \binom{n}{2} = 1 + 2 + \cdots + n - 1.$$

We must now prove that $P(n + 1)$ follows, i.e.:

$$P(n + 1) : \binom{n + 1}{2} = 1 + 2 + \cdots + n.$$

Take the set $X = \{1, 2, \ldots, n + 1\}$ of size $n + 1$, and consider the set $\binom{X}{2}$ of ways to pick two elements from $X$. Note that we are using numbers as elements of $X$ instead of "arbitrary objects." We might have instead called them "ball 1, ball 2, ball 3" and discussed how many ways to select two balls from a bin. For simplicity we'll use the numbers themselves. Now $\binom{X}{2}$ is a set of size $\binom{n + 1}{2}$ and we want to express the size in terms of our (inductively assumed) formula for $\binom{n}{2}$. Pick any element of $X$, say $n + 1$, and define $Y$ to be the set that remains after removing that element from $X$.

$$Y = X - \{n + 1\} = \{1, 2, \ldots, n\}.$$

Now let's split the elements of $\binom{X}{2}$ into two parts: the part where both chosen elements are in $Y$, and the part where one of the two chosen elements is $n + 1$. Since there are no other options and no overlap between the two options, we can add the sizes of both parts to count the size of $\binom{X}{2}$.

The first part, where both chosen elements are in $Y$, has size $\left|\binom{Y}{2}\right| = \binom{n}{2}$, which by the inductive hypothesis is $1 + 2 + \cdots + n - 1$. The second part, where one of the chosen elements is guaranteed to be $n + 1$, has size $n$ by the following reasoning: if you had to choose $n + 1$ as one of the two elements, then there are only $n$ remaining choices for the second element.

Adding up the sizes of the two parts gives exactly

$$1 + 2 + \cdots + (n - 1) + n,$$

which is what we set out to prove. $\blacksquare$

The split that drives the inductive step — pairs entirely inside $Y$ versus pairs that include the new element $n + 1$ — can be made completely concrete. The demo below takes $X = \{1, \dots, n+1\}$, partitions $\binom{X}{2}$ into exactly those two parts, and checks the bookkeeping: the parts are disjoint, they cover everything, the "$Y$-only" part has size $\binom{n}{2}$, and the "$n+1$" part has size $n$.

```python
<!-- include: code/pim/03 - Sets/06_induction_step.py -->
```

Is the proof still a bit murky? Go back and set $n = 4$, $X = \{1, 2, 3, 4, 5\}$, and then write down the elements of $\binom{X}{2}$. Follow the steps through the inductive step of the proof on this example, and your understanding of the general case will feel like an epiphany.

Interestingly, proof by induction has a bad reputation in mathematics. The reason is that proofs by induction often convey little insight to the reader. As the mathematician Gian-Carlo Rota once said, "If we have no idea why a statement is true, we can still prove it by induction." Be that as it may, induction is a central tool for proving theorems.

The second proof technique is called "proof by contradiction." There's a simple puzzle I often use to illustrate the technique.

You're at a party. You're chatting with your friend, and out of curiosity you ask how many friends he has at the party. He counts them up, there are five, and you realize that you also have five friends at the party. What a coincidence! Putting on your mathematician hat, you poll everyone at the party and you're shocked to find that a few other people also have five friends at the party. The puzzle is: is this true of every party? Maybe not five exactly, but will there always be at least two people with the same number of friends who are at the party?

Before I give the solution by contradiction, let's iron out what I mean by "friendship." I insist that friendship is symmetric: you can't be friends with someone who is not friends with you. And moreover you can't be friends with yourself.

You'll appreciate the answer to this problem best if you spend some time trying to solve it first.

Back already? The answer is yes, there will always be a pair of people with the same number of friends. The technique we use to prove it is called proof by contradiction. It works by assuming the opposite of what you want to prove is true, and using that assumption to deduce nonsense.

*Proof.* Suppose for the sake of contradiction that there is some party where everybody has a different number of friends at the party. Say the party has $n > 1$ people, then everyone must have between zero and $n - 1$ friends. Since there are $n$ people and $n$ different numbers between zero and $n - 1$, we can map each person to the number of friends they have, and this map will be a bijection. Now here comes the contradiction: someone must have zero friends at the party, and someone must have $n - 1$ friends, i.e., someone must be friends with everyone. But the person who is friends with everyone must be friends with the person that has no friends! The only way to resolve this contradiction is if the original assumption is actually false. That is, there must be two people with the same number of friends. $\blacksquare$

This is the "pigeonhole" argument in disguise: $n$ people, but only $n - 1$ achievable friend-counts once you notice $0$ and $n-1$ can't coexist. The demo below makes that empirical: it generates thousands of random friendship graphs and checks that in every single one, two people share a degree (number of friends) — the conclusion of the proof, observed rather than assumed.

```python
<!-- include: code/pim/03 - Sets/07_party.py -->
```

This is how every proof by contradiction goes, but they're usually a bit more concise. They always start with, "Suppose to the contrary" to signal the method. And there is no warning when the contradiction will come. A proof writer usually just states the contradiction and follows it with "which is a contradiction," ending the proof.

The point of a proof by contradiction is to get an object with a property that you can work with. If you're trying to prove that no object with some special property exists, a proof by contradiction gives you an instance of such an object, and you can use its special property to go forward in the proof. In this case the object was a special friendship count among partygoers, and in the next section we'll apply the same logic to "marriages."

For those readers who are interested in a bit more details about what makes a mathematical proof, or how to approach proving things, in this second edition I added two appendices that may help. Appendix B contains a bit more details about the formalities underlying proofs, along with a section at the end called "How does one actually prove things?" Appendix C contains a list of books under "Fundamentals and Foundations" that cover the basics of set theory, proofs, and problem solving strategies. Readers of the first edition have told me that following along with these books has helped immensely.

## 4.4 Application: Stable Marriages

Now we're ready to apply the tools in this chapter to implement a Nobel Prize-winning algorithm for the stable marriage problem. The problem is set up as follows. Say you have $n$ men and $n$ women. Your end goal is to choose who should marry whom. Same-sex marriages are excluded, not for political or religious reasons but because it's a more difficult problem. So if we call $M$ the men and $W$ the women, our output will be a bijection $M \to W$ describing the marriages (or equivalently $W \to M$). I will freely switch between "bijection" and "marriage" in this section.

Of course, we don't just want any bijection. This is where the "stable" part comes in. We want to choose the marriage so that everyone is happy in some sense. Let's make this precise. Say that each man has a ranking of the women, mathematically a bijection $W \to \{1, 2, \ldots, n\}$, with $1$ being the most preferred and $n$ being the least. In other words, if we call the bijection $p$ then $p(w) < p(x)$ means that this particular man prefers woman $w$ over woman $x$. Likewise, each woman has a ranking of the men $M \to \{1, 2, \ldots, n\}$. Now we obviously can't ensure that every woman gets her top choice and vice versa; the men could all prefer the same woman. So we need a subtler notion of happiness: that no (man, woman) pair mutually prefer each other over their assigned partners.

Marriages are a colorful, if somewhat silly, setting for this problem. Realistically, this algorithm applies to different sorts of 'marriage', such as the assignment of a student to an apprenticeship. A widely known example is medical residency, in which medical students work in a hospital before becoming a doctor. This is the perfect example of a market in which money should not play a part. As a society we want all our hospitals filled with talented apprentices. We don't want the students with the richest parents or best connections to get the most prestigious positions in the best cities, while poorer areas suffer. We want to spread the talent around. So we need a market with a protocol that respects student and hospital preferences in a way that no (student, hospital) pair is incentivized to make their own arrangements. This version of the problem is a natural extension of the marriage version. So we'll explore marriages in depth here, and dive into medical residency matching in the exercises.

Define a ranking function as a bijection between $\{1, 2, \ldots, n\}$ and either $M$ or $W$.

Before I state what "not cheating" means mathematically for the marriage problem, I encourage you to write down a small example of sets $M, W$ of size $n = 4$, rankings $\text{pref}_w(m)$ for each $w \in W$ and $\text{pref}_m(w)$ for each $m \in M$, and a candidate marriage $f : M \to W$. I'll call the marriage from the women's perspective $f^{-1} : W \to M$.

What I mean by "no mutually desired cheating" is the following.

**Definition 4.14.** A bijection $f : M \to W$ is called *stable* if there is no pair $m \in M$ and $w \in W$ such that the following two conditions hold:

1. $f(m) \neq w$, i.e., the two are not matched by $f$.
2. The pair $m$ and $w$ mutually prefer each other over their assigned matches. I.e., both $\text{pref}_m(w) < \text{pref}_m(f(m))$ and $\text{pref}_w(m) < \text{pref}_w(f^{-1}(w))$.

In other words, the bijection is called stable if there is no pair of people with mutual incentive to cheat on their assigned spouses. This is not to say cheating can't happen, but if it does one of the two involved will be "lowering their standards."

The algorithmic question is, given lists of preferences as input, can we find a stable marriage? Can we even guarantee a stable marriage will exist for any set of preferences? The answer to both questions is yes, and it uses an algorithm called deferred acceptance.

Here is an informal description of the algorithm. It goes in rounds. In each round, each man "proposes" to the highest-preferred woman that has not yet rejected him. On the other side, each woman holds a reference to a man at all times. If a woman gets new proposals in a round, she immediately rejects every proposer except her most preferred, but does not accept that proposal. She "defers" the acceptance of the proposal until the very end.

The rejected men are sad, but in the next round they recover and propose to their next most preferred woman, and again the women reject all but one. The men keep proposing until every man is tentatively held by some woman, or until all women have rejected them. That is not a happy place to imagine. But actually, the theorem that we'll prove says that this process always ends with each woman holding onto a man, and no men are left out; the set of women's held picks forms a stable bijection.

Before we prove that the algorithm works, let's state it more formally in Python code. A complete working program is available on this book's Github repository. In the interest of generality, I've defined classes `Suitor` and `Suited` to differentiate: Suitors propose to Suiteds.

```python
class Suitor:
    def __init__(self, id, preference_list):
        self.preference_list = preference_list
        self.index_to_propose_to = 0
        self.id = id

    def preference(self):
        return self.preference_list[self.index_to_propose_to]

    def post_rejection(self):
        self.index_to_propose_to += 1
```

The `Suitor` class is simple. Instances are uniquely identified by an `id`, which I'm defining to be the index in a global list of Suitors. A Suitor has a `preference_list`, which is a list of Suited ids sorted from most preferred to least preferred. The `index_to_propose_to` variable simultaneously counts the number of rejections and which index in the `preference_list` to use for the next proposal.

A bit more complicated is the `Suited` class:

```python
class Suited:
    def __init__(self, id, preference_list):
        self.preference_list = preference_list
        self.held = None
        self.current_suitors = set()
        self.id = id

    def reject(self):
        """Return the subset of Suitors in self.current_suitors to
        reject, leaving only the held Suitor in self.current_suitors.
        """
        if len(self.current_suitors) == 0:
            return set()

        self.held = min(
            self.current_suitors,
            key=lambda suitor: self.preference_list.index(suitor.id))
        rejected = self.current_suitors - set([self.held])
        self.current_suitors = set([self.held])

        return rejected

    def add_suitor(self, suitor):
        self.current_suitors.add(suitor)
```

Here `current_suitors` are the new proposals in a given round, and `held` is the Suited's held pick. In the method `reject`, a Suited looks at all her current suitors, chooses the best in her `preference_list`, and returns all others as rejected Suitors.

Finally, we have the main routine for the deferred acceptance algorithm.

```python
def stable_marriage(suitors, suiteds):
    """ Construct a stable marriage between Suitors and Suiteds. """
    unassigned = set(suitors)

    while len(unassigned) > 0:
        for suitor in unassigned:
            next_to_propose_to = suiteds[suitor.preference()]
            next_to_propose_to.add_suitor(suitor)
        unassigned = set()

        for suited in suiteds:
            unassigned |= suited.reject()  # python set union operator

        for suitor in unassigned:
            suitor.post_rejection()  # have some ice cream

    return dict([(suited.held, suited) for suited in suiteds])
```

The dictionary at the end is the type we use to represent a bijection. Now let's prove this algorithm always produces a stable marriage.

We will argue that the algorithm terminates by *monotonicity*. Here's what I mean by that: say you have a sequence of integers $a_1, a_2, \dots$ which is *monotonically increasing*, meaning that $a_1 < a_2 < \cdots$. Say moreover that you know none of the $a_i$ are larger than $50$ ($a_i$ is *bounded* from above) but each $a_{i+1} \geq a_i + C$ for some constant $C > 0$. Then it's trivial to see that either the sequence stops before it hits $50$, or eventually it hits $50$.

To show an algorithm terminates, you can cleverly choose an integer $a_t$ for each iteration $t$ of the core loop, and show that $a_t$ is monotonically increasing (or decreasing) and bounded. Then show that if the algorithm hits the bound then it's forced to finish, and otherwise it finishes on its own.

**Theorem 4.15.** The deferred acceptance algorithm always terminates, and the bijection produced at the end is stable.

*Proof.* For the deferred acceptance algorithm we have a nice monotonic sequence. For round $t$ set $a_t$ to be the sum of all the Suitors' `index_to_propose_to` variables. Recall that this variable also represents the number of rejections of each Suitor. Since there are exactly $n$ preferences in the list and exactly $n$ Suitors, we get the bound $a_t \leq n^2$ (each Suitor could be at the very end of their list; come up with an example to show this can happen!).

Moreover, in each round one of two things happens. Either no Suitor is rejected by a Suited and by definition the algorithm finishes, or someone is rejected and their `index_to_propose_to` variable increases by $1$, so $a_{t+1} \geq a_t + 1$. Now in the case where all the Suitors are at the end of their lists, that means that every Suited was proposed to by every Suitor. In other words, each of the Suiteds gets their top pick: they only reject when they see a better option, and they got to consider all proposals! Clearly the algorithm will stop in this case.

Now that we've shown the algorithm will stop, we need to show the bijection $f$ produced as output is stable. The definition of stability says there is no Suitor $m$ and Suited $w$ with mutual incentive to cheat, so for contradiction's sake we'll suppose that the $f$ output by the algorithm does have such a pair, i.e., for some $m, w$, $\operatorname{pref}_m(w) < \operatorname{pref}_m(f(m))$ and $\operatorname{pref}_w(m) < \operatorname{pref}_w(f^{-1}(w))$.

What had to happen to $w$ during the algorithm? Well, $m$ ended up with $f(m)$ instead of $w$, and if $\operatorname{pref}_m(f(m)) > \operatorname{pref}_m(w)$, then $m$ must have proposed to $w$ at some earlier round. Likewise, the `held` pick of $w$ only increases in quality when $w$ rejects a Suitor, but $w$ ended up with some Suitor $f^{-1}(w)$ while $\operatorname{pref}_w(m) < \operatorname{pref}_w(f^{-1}(w))$. So at some point in between being proposed to by $m$ and choosing to hold on to $f^{-1}(w)$, $w$ had to go the wrong way in her preference list, contradicting the definition of the algorithm. $\blacksquare$

The proof claims two things we can check head-on: the output is stable, and it terminates fast. The demo below runs Kun's exact `Suitor`/`Suited` classes on his exact example, then verifies stability by searching for a blocking pair directly from Definition 4.14. It goes one step further and brute-forces *all* stable matchings to confirm a deeper fact the proof hints at: deferred acceptance is *suitor-optimal* — every proposer ends up with the best partner he could have in any stable matching at all.

```python
<!-- include: code/pim/03 - Sets/05_stable_marriage.py -->
```

We close with an example run:

```python
>>> suitors = [
        Suitor(0, [3, 5, 4, 2, 1, 0]),
        Suitor(1, [2, 3, 1, 0, 4, 5]),
        Suitor(2, [5, 2, 1, 0, 3, 4]),
        Suitor(3, [0, 1, 2, 3, 4, 5]),
        Suitor(4, [4, 5, 1, 2, 0, 3]),
        Suitor(5, [0, 1, 2, 3, 4, 5]),
    ]
>>> suiteds = [
        Suited(0, [3, 5, 4, 2, 1, 0]),
        Suited(1, [2, 3, 1, 0, 4, 5]),
        Suited(2, [5, 2, 1, 0, 3, 4]),
        Suited(3, [0, 1, 2, 3, 4, 5]),
        Suited(4, [4, 5, 1, 2, 0, 3]),
        Suited(5, [0, 1, 2, 3, 4, 5]),
    ]
>>> stable_marriage(suitors, suiteds)
{
    Suitor(0): Suited(3),
    Suitor(1): Suited(2),
    Suitor(2): Suited(5),
    Suitor(3): Suited(0),
    Suitor(4): Suited(4),
    Suitor(5): Suited(1),
}
```

## 4.5 Cultural Review

1. Sets and functions between sets are a modeling language for mathematics.
2. Bijections show up everywhere, and they're a central tool for understanding the same object from two different perspectives.
3. Mathematicians usually accept silent type conversions between sets when it makes sense to do so, i.e., when there is a very clear and natural bijection between the two sets.
4. Induction is a similar idea to recursion in programming, but applied to proofs.
5. A picture or example that captures the spirit of a fully general proof is often good enough.

## 4.6 Exercises

**4.1.** Write down examples for the following definitions. A set $A$ (finite or infinite) is called *countable* if it is empty, or if there is a surjection $\mathbb{N} \to A$. The *power set* of a set $A$, denoted $2^A$, is the set of all subsets of $A$. For two sets $A, B$, we denote by $B^A$ the set of all functions from $A$ to $B$. This makes sense with the previous notation $2^A$ if we think of "2" as the set of two elements $2 = \{0, 1\}$, and think of a function $f : A \to \{0, 1\}$ as describing a subset $C \subset A$ by sending elements of $C$ to $1$ and elements of $A - C$ to $0$. In other words, the subset defined by $f$ is $C = f^{-1}(1)$.

This exercise gives us the cleanest verification in the chapter. The identity $|2^A| = 2^{|A|}$ is really the statement that subsets of $A$ correspond exactly to functions $A \to \{0, 1\}$. The demo below builds the power set explicitly from binary masks (one mask per subset), checks $|2^S| = 2^{|S|}$ for $|S| = 0, \dots, 7$, and spells out the subset-vs-indicator bijection from the exercise, recovering each subset as $f^{-1}(1)$.

```python
<!-- include: code/pim/03 - Sets/01_power_set.py -->
```

**4.2.** Recall that for $A \subset X$, $A^{\mathsf{C}}$ sometimes denotes the complement of $A$ in $X$. Prove De Morgan's law for sets, which for $A, B \subset X$ states that $(A \cap B)^{\mathsf{C}} = A^{\mathsf{C}} \cup B^{\mathsf{C}}$, and $(A \cup B)^{\mathsf{C}} = A^{\mathsf{C}} \cap B^{\mathsf{C}}$. Draw the connection between this and the corresponding laws for negations of boolean formulas (e.g., `not (a and b) == (not a) or (not b)`).

The set identity and the boolean identity are the same statement seen through the subset-vs-indicator bijection of Exercise 4.1. The demo below verifies both De Morgan laws by brute force over all subsets $A, B$ of a small universe, and then verifies the boolean version exhaustively over all truth assignments.

```python
<!-- include: code/pim/03 - Sets/08_de_morgan.py -->
```

**4.3.** Look up a formula online for the quantity $\binom{n}{k}$, the number of ways to choose $k$ elements from a set of size $n$, in terms of factorials $m! = 1 \cdot 2 \cdot 3 \cdot \dots \cdot m$. Find a proof that explains why this formula is true.

**4.4.** Look up a statement of the pigeonhole principle, and research how it is used in proofs.

**4.5.** Prove that $\mathbb{N} \times \mathbb{N}$ is countable, i.e., there is a surjection $\mathbb{N} \to \mathbb{N} \times \mathbb{N}$.

**4.6.** For each $n \in \mathbb{N}$, let $A_n$ be a countably infinite set, such that all the $A_n$ have empty intersection. Prove that the union of all the $A_n$ is countable. Hint: use the previous problem.

**4.7.** Is there a bijection between $2^{\mathbb{N}}$ and the interval $[0, 1]$ of real numbers $x$ with $0 \leq x \leq 1$? Is there a bijection between $(0, 1] = \{x \in \mathbb{R} : 0 < x \leq 1\}$ and $[1, \infty) = \{x \in \mathbb{R} : x \geq 1\}$?

**4.8.** I would be remiss to omit Georg Cantor from a chapter on set theory. Cantor's Theorem states that the set of real numbers $\mathbb{R}$ is not countable. The proof uses a famous technique called "diagonalization." There are many expositions of this proof on the internet ranging in difficulty. Find one that you can understand and read it. The magic of this theorem is that it means there is more than one kind of infinity, and some infinities are bigger than others.

**4.9.** The principle of inclusion-exclusion is a technique used to aid in counting the size of a set. Look for a description of this principle (it is a family of theorems) and find ways it is used to help count.

**4.10.** There is a large body of mathematics related to configurations of sets with highly symmetric properties. Let $n, k, t$ be integers. A *Steiner system* is a family $F$ of size-$k$ subsets of an $n$-element set $S$, say $\{1, \ldots, n\}$, such that every size-$t$ subset of $S$ is in exactly one member of $F$. For example, for $(n, k, t) = (7, 3, 2)$, the corresponding Steiner system is a choice of triples in $\{1, 2, 3, 4, 5, 6, 7\}$, such that every pair of numbers is in exactly one of the chosen triples. Find an explicit description of a $(7, 3, 2)$-system.

The $(7, 3, 2)$-system is the celebrated *Fano plane*. As a worked highlight, the demo below tests one explicit candidate (seven triples on $\{1, \dots, 7\}$) and verifies the defining property directly: every one of the $\binom{7}{2} = 21$ pairs lies in exactly one triple.

```python
<!-- include: code/pim/03 - Sets/09_fano.py -->
```

**4.11.** Continuing the previous exercise, a Steiner system may not exist for every choice of $n > k > t$. Prove that if an $(n, k, t)$-system exists, then so must an $(n - 1, k - 1, t - 1)$-system. Determine under what conditions on $n$ may a Steiner $(n, 3, 2)$-system exist.

**4.12.** Continuing the previous exercise, the non-existence of Steiner systems for some choices of $n$ suggests a modified problem of finding a minimal size family $F$ of size-$k$ subsets such that every $t$-size subset is in at least one set in $F$. For $(n, k, t)$ arbitrary, find a lower bound on the size of $F$. Try to come up with an algorithm that gets close to this lower bound for small values of $k, t$.

**4.13.** A generalization of Steiner systems are called *block designs*. A block design $F$ is again a family of size-$k$ subsets of $X = \{1, \ldots, n\}$ covering all size-$t$ subsets, but also with parameters controlling: the number of sets in $F$ that contain each $x \in X$, and the number of sets covering each size-$t$ subset (i.e., it can be more than one). Block designs are used in the theory of experimental design in statistics when, for example, one wants to test multiple drugs on patients, but the outcome could be confounded by which subset of drugs each patient takes, as well as which order they are taken in, among other factors. Research how block designs are used to mitigate these problems.

**4.14.** A *Sperner family* is a family $F$ of subsets of $\{1, \ldots, n\}$ for which no member of $F$ is a subset of any other member of $F$. Sperner's theorem gives an upper bound on the maximum size of a Sperner family. Find a proof of this theorem. There are multiple proofs, though one of them has at its core an inequality called the Lubell–Yamamoto–Meshalkin inequality, which is proved using a double-counting argument (and Exercise 4.3).

**4.15.** The formal mathematical foundations for set theory are called the Zermelo-Fraenkel axioms (also called ZF-set theory, or ZFC). Research these axioms and determine how numbers and pairs are represented in this "bare metal" mathematics. Look up Russell's paradox, and understand why ZF-set theory avoids it.

**4.16.** A *fuzzy set* $S \subset X$ is a function $m_S : X \to [0, 1]$ that measures the (possibly partial) membership of an $x \in X$ in the set $S$. One can think of $m_S(x)$ as representing the "confidence," or "probability" that an $x$ is in $S$. Show that every set can be represented as a fuzzy set. Research fuzzy sets, and determine a sensible definition for the cardinality of a fuzzy set.

**4.17.** Write a program that extends the deferred acceptance algorithm to the setting of "marriages with capacity." That is, imagine now that instead of men and women we have medical students and hospitals. Each hospital may admit multiple students as residents, but each student attends a single hospital. Find the most natural definition for what a stable marriage is in this context, and modify the algorithm in this chapter to find stable marriages in this setting. Then implement it in code. See the chapter notes for historical notes on this algorithm.

**4.18.** Come up with a version of stable marriages that includes the possibility of same-sex marriage. This variant is sometimes called the *stable roommate problem*. In this setting, there is simply a pool of people that must be paired off, and everybody ranks everyone else. Perform the full modeling process: write down the definitions, design an algorithm, prove it works, and implement it in code.

**4.19.** Is the stable marriage algorithm biased? Come up with a concrete measure of how "good" a bijection is for the men or the women collectively, and determine if the stable marriage algorithm is biased toward men or women for that measure.

## 4.7 Chapter Notes

### Residency Matching

Medical residency matching was the setting for one of the major accomplishments of Alvin Roth, currently an economics professor at Stanford. He applied this and related algorithms to kidney exchange markets and schooling markets. Along with Lloyd Shapley, one of the original designers of the deferred acceptance algorithm, their work designing and implementing these systems in practice won the 2012 Nobel Prize in economics. Measured by a different standard, their work on kidney markets has saved thousands of lives, put students in better schools, and reduced stress among young doctors.

Roth gives a fascinating talk about the evolution of the medical residency market before he stepped in, detailing how students and hospitals engaged in a maniacal day-long sprint of telephone calls, and all the ways unethical actors would try to game the protocol in their favor.

### Marriage

Please don't treat marriage as an allocation problem in real life. I hope it's clear that the process of doing mathematics—and the modeling involved in converting real world problems to sets—involves deliberately distilling a problem down to a tractable core. This often involves ignoring features that are quite crucial to the real world. A quote often attributed to Albert Einstein speaks truth here, that "a problem should be made as simple as possible, but no simpler." Indeed, the unstated hope is that by analyzing the simplified, distilled problem, one can gain insights that are applicable to the more complex, realistic problem. Don't remove the core of the problem when phrasing it in mathematics, but remove as much as you need to make progress. Then gradually restore complexity until you have solved the original problem, or fail to make more progress. Marriage is used as a communication device for this particular simplification. It's not the problem being solved.

The idea that one can reduce complex human relationships to a simple allocation problem is laughable, and borderline offensive. In the stable marriage problem the actors are static, unchanging symbols that happen to have preferences. In reality, the most important aspect of human relationships is that people can grow and improve through communication, introspection, and hard work.
