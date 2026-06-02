# Chapter 5 Variable Names, Overloading, and Your Brain

> Math is the art of giving the same name to different things.
>
> – Henri Poincaré

Programmers often complain about how mathematicians use single-letter variable names, how they overload and abuse notation, and how the words they use to describe things are essentially nonsense words made up for the sole purpose of having a new word. This causes bizarre sentences like “Map each co-monad to the Hom-set of quandle endomorphisms of $X$.” I just made that up, by the way, though each word means something individually. One question programmers rarely ask is why mathematicians do this. Is it to feign complexity? Historical precedence? A hint of malice?

Of course there are bad writers out there, along with people who like to sound smart. There is certainly a somewhat unhealthy pattern of mathematicians who think a dose of emotional and intellectual pain is the best way to learn. But that’s true of every field. I want to take a quick moment to explain the mathematician’s perspective. As you’ve probably guessed by now, a central issue is culture. I won’t try to convince you that this is the only explanation, but rather show you a different reasonable angle on the debate.

In producing mathematics, the mathematician has two goals: discover insight about a mathematical thing, and then communicate that truth to others in an intuitive and elegant way. While the second goal implies that mathematicians do care about style, what makes a proof or mathematical theory elegant is first and foremost the degree to which it facilitates understanding.

On the other hand, good software is measured (after it’s deemed to work) by maintainability, extensibility, modularization, testability, robustness, and a whole host of other metrics which are primarily business metrics. You care about modularization because you want to be able to delegate work to many different programmers without stepping on each other’s toes. You want extensibility because customers never know what features they actually want until you finish designing the features they later decide are no good. You want to ensure that your software is idiot-proof because your company just hired three idiots. These metrics are good targets because they save time and money.

Mathematicians don’t experience these scaling problems to the same degree of tedium because mathematics isn’t a business. Mathematics isn’t idiot-proof because the success of a mathematical theory doesn’t depend on whether the next idiot that comes along understands it.[^1] In fact, mathematical sophistication in the business world is extraordinary. And while having tests (providing worked-out examples) is a sign of a good mathematical writer, there’s no manager staking their job or a salary bonus on the robustness of a bit of notation. If someone gets confused reading your paper, it doesn’t siphon money out the window the same way it does at Twitter during an outage. There’s just not the same sense of urgency in mathematics.

I should make a side note that saying “mathematics isn’t a business” is overly naive. Mathematicians need to make money just like everyone else, and this manifests itself in some strange practices in academic journals, conferences, and the multitude of committees that decide who is worth hiring and giving tenure. Mathematicians, like folks in industry, bend over backwards to game (or accommodate) the system. But all of that is academia. What I’m talking about is established mathematics which has been around for decades, or even centuries, which has been purified of political excrement. This applies to basically every topic in this book.

That’s not to say that mathematics isn’t designed to scale. To the contrary, the invention of algebraic notation was one of humanity’s first massively scalable technologies. On the other end of the spectrum, category theory—which you can think of as a newer foundation for math roughly based on a new notation that goes beyond what sets and functions can offer—provides the foundation for much of modern pure mathematics. It’s considered by many as a major advancement.

Rather than being designed to scale to millions of average users, mathematics aims to scale far up the ladder of abstraction. Algebra—literally, the marks on paper—boosted humanity from barely being able to do arithmetic through to today’s machine learning algorithms and cryptographic protocols. Sets, which were only invented in the late 1800’s, hoisted mathematical abstraction even further. Category theory is a relative rocket fuel boosting one through the stratosphere of abstraction (for better or worse).

The result of this, as the argument goes, is that mathematicians have optimized their discourse for more relevant metrics: maximizing efficiency and minimizing cognitive load *after deep study*.

Let me map out a few areas where this shows up:

- Variable names
- Operator overloading
- Sloppy notation

**Variable names.** Variable names are designed to transmit a lot of information: types, behavior, origin, and more. Programmers do this as well, but the conventions differ. Every mathematician knows that $n$ is a natural number, and that $f$ is a function. Or at least, they know that when they see these letters out of context, they should at least behave like a natural number and a function, respectively. Seeing $n(f)$ out of context would momentarily startle me, though I can imagine situations making it appropriate.[^2] Similarly, if $f$ is a function and you can use $f$ to construct another function in a “canonical” (forced, unique) way, then a mathematician might typically adorn $f$ with a star like $f^{*}$. Two related objects often inhabit the same letter with a tick, like $x$ and $x^{\prime}$. Even if you forget what they represent, you know they’re related.

Every field of mathematics has its own little conventions that help save time. This is especially true since mathematics is often done in real time (talking with colleagues in front of a blackboard, or speaking to a crowd). The time it takes to write $f^{*}$ while saying *out loud* “the canonical induced homomorphism,”[^3] is much faster than writing down `InducedHomomorphismF` in ten places. And then when you need an $h^{*}$ to compose $f^{*}h^{*}$, half of the characters help you distinguish it from $h^{*}f^{*}$. Whereas determining the order of

```
InducedHomomorphismF.compose(InducedHomomorphismH)
```

is harder with more characters, and Gauss forbid you have to write down an identity about the composition of three of these things! A single statement would fill up an entire blackboard, and you’d never get to the point of your discussion.

More deeply, there is often nothing more a name can do to elucidate the nature of a mathematical object. Does saying $f^{*}$ really tell you less about what an object is than something like `InducedF`? It’s related to $f$, its definition is somehow “induced,” and what? The further up the ladder of abstraction you go, the more contrived these naming conventions would get. Rather than say, for example, `FirstCohomologyGroupOfInvertibleSubsheavesOfX`, you say $H^{1}(X,O^{*})$ because you would rather claw your eyes out than read the first thing, which could easily be *just one part* of a larger expression, with maybe ten more similar copies of the notation. For example, here is an actual snippet from a chapter of a graduate algebra textbook cheekily titled, “Algebra: Chapter 0.”

$$\nu_{L}:\mathsf{L}_{0}\mathcal{F}(M)=H^{0}(\mathsf{C}(\mathcal{F})(P^{\bullet}))\to\mathcal{F}(M)$$

It is a bit ridiculous that $L$ and $\mathsf{L}$ refer to different mathematical things, despite being the same letter. Here $L$ is an object and $\mathsf{L}$ (short for “left”) describes a kind of function. But this is a trade-off. You can use long words that make it difficult to put everything you want to say in front of your face at the same time—thus making it harder to reason. Or, you can use fonts and foreign alphabets to differentiate concepts. Sans-serif is for one purpose, the curly-scripty font is for another.

Why not invent a better name? They do! Just later. In fact, because the expression $H^{1}(X,O^{*})$ is so important in the study of algebraic geometry, it was renamed to $\operatorname{Pic}(X)$ named after Picard who studied them. But it might take decades to get to the point where you realize this object is worth giving a name, and in the mean time you just can’t use 80-character names and expect to get things done.

One reason mathematicians can get away with single-character variable names is that they spend so much time studying them. When a mathematician comes up with a new definition, it’s usually the result of weeks of labor, if not months or years! These objects aren’t just variables in some program whose output or process is the real prize. The variables represent the cool things! It’s as if you returned to rewrite and recheck and retest the same twenty-line program every day for a month. You’d have such an intimate understanding of every line that you could recite it while drunk or asleep. Now imagine that the intimate understanding of every line of that program was the basis of every program you wrote for the next year, and you see how ingrained this stuff is in the mind of a mathematician.

Mathematicians don’t just write a proof and file it away under “great tool; didn’t read.” They constantly revisit the source. It’s effective to gild meaning and subtext into the bones of single letters, because after years you don’t have to think about it any more. It eliminates the need to keep track of types. Clearly $f$ is a function, $z$ is probably a complex variable, and everyone knows that $\aleph_{0}$ is the countably infinite cardinal. If you use $b$ and $\beta$ in the same place, I will know that they are probably related, or at least play analogous roles in two different contexts, and that will jump-start my understanding in a way that descriptive variable names do not.

**Operator overloading.** Much of what I said above for variable names holds for operator overloading too. One key feature that stands out for operator overloading is that it highlights the intended nature of an operation.

We’ll get to this more in Chapter 9, but mathematicians use just a handful of boolean logic operations for almost everything. There are the standard inequalities and equalities. Then there are operators that look like $\cong$ or $\simeq$ that represent equality “up to some differences that we don’t care about.” In Java terms, mathematicians regularly roll their own `.equals()` methods, with proofs that their notions behave. Specifically, they prove it satisfies the properties required of an *equivalence relation*, which is the mathematical version of saying “equals agrees with hashing and `toString`.”

And so typically mathematicians will drop whatever the original operator symbol was and replace it with the equal sign. The core properties of $=$ are respected even if not identity. We’ll see this in detail in Chapters 9 and 16, but the same idea goes behind the reuse of standard arithmetic operations like addition and multiplication. It suggests what behavior to expect from the operation. For example, it is considered bad form to use the $+$ operator for an operation that doesn’t satisfy $a+b=b+a$ for every choice of $a$ and $b$—the commutative property—because this is true of addition. Many multiplications are not commutative, such as matrix multiplication, and so a generic multiplication uses $\times$ or juxtaposition to signal this.

With this in mind it’s the mathematician’s turn to criticize programmers. For example, reading programming style guides has always amused me. It makes sense for a company to impose a style guide on their employees (especially when your IDE is powerful enough to auto-format your programs) because you want your codebase to be uniform. In the same way, a mathematician would never change notational convention in the same paper, except to introduce a new notation. But to have a programming language designer declare style edicts for the entire world, like the following from the Python Style Guide, is just ridiculous:

```
Imports should usually be on separate lines, e.g.:

Yes: import os
     import sys

No:  import sys, os
```

Okay, so you have an arbitrary idea of what a pretty program looks like, but wouldn’t you rather spend that time and energy on actually understanding and writing a good program? Besides, if there were truly a good reason for the first option, why wouldn’t the language designer just disallow the second option in the syntax? Of course, programmers get away with it because they use automated tools to apply style guides automatically. It’s much harder to do that in math, where the worst offenses are not resolvable (or discoverable!) from syntax alone. Still, I don’t doubt there could be some progress made in automating some aspects of a mathematical style guide.

In an ideal world, a compiler would see how I use the “stdout” variable and be able to infer the semantics from a shared understanding about the behavior of standard output in basically every program ever. This would eliminate the need to declare module imports or even define stdout! That’s basically how math solves the problem of overloaded operators. There is a clarifying and rigorous definition somewhere, but if you’ve forgotten it you can still understand the basic intent and infer appropriate meaning.

**Sloppy notation.** This is probably the area where mathematicians get the most flak, and where they could easily improve their communication with those aiming to learn.

Take summation notation, the $\sum$ symbol. Officially this symbol has three parts: an index variable, a minimum and maximum value for the index, and an expression being summed. So $\sum_{i=0}^{9}2i+1$ sums the first ten positive odd integers. This is the kind of syntactical rigidity that makes one itch to write a parser.

However, this notation is so convenient that it’s been overloaded to include many other syntax forms. A simple one is to replace the increment-by-one range of integers with a “all elements in this set” notation. For example, if $B$ is a set, you can write $\sum_{b\in B}b^{2}$ to sum the squares of all elements of $B$.

But wait, there’s more! It often happens that $B$ has an implicit, or previously defined order of the elements $B=\{b_{1},\ldots,b_{n}\}$, in which case one takes the liberty of writing $\sum_{i}b_{i}^{2}$ (“the sum over relevant $i$”) with no mention of the set in the (local) syntax at all! As we saw in Chapter 2 with polynomials, one can additionally add conditions below the index to filter only desired values, or even have the *constraint* implicitly define the variable range! So you can say the following to sum all odd $b_{i}\in B$

$$\sum_{b_{i}\text{ odd}}b_{i}^{2}+3$$

The reason this makes any sense is because, as is often the case, the math notation often comes from speech. You’re literally speaking, “over all $b_{i}$ that are odd, sum the terms $b_{i}^{2}+3$.” Equations are written to mimic conversation, not the other way around. You see it when you’re in the company of mathematicians explaining things. They’ll write their formulas down as they talk, and half the time they’ll write them backwards! For a sum, they might write the body of the summation first, then add the sum sign and the index. Because out loud they’ll be emphasizing the novel parts of the equation, filling the surrounding parts for completeness.

Finally, the things being summed need not be numbers, so long as addition is defined for those objects and it satisfies the properties addition should satisfy. In Chapter 10 we’ll see a new kind of summation for vectors, and it will be clear why it’s okay for us to reuse $\sum$ in that context. The summing operation needs to have properties that result in the final sum not depending on the order the operations are applied.

Another prominent example of summation notation being adapted for an expert audience is the so-called Einstein notation. This notation is popular in physics. In Einstein notation the $\sum$ symbol is itself implied from context! For example, rather than write

$$y=\sum_{k=1}^{n}a_{k}x^{k},$$

the sum and the bounds on the indices are implied from the presence of the indices, as in

$$y=a_{k}x^{k}.$$

To my personal sensibilities this is extreme. But I can’t fault proponents of the abuse when they find it genuinely useful.

What makes all of this okay is when the missing parts are fixed throughout the discussion or clear from context. What counts as context is (tautologically) context dependent. More often than not, mathematicians will preface their abuse to prepare you for the new mental hoop. The benefit of these notational adulterations is to make the mathematics less verbose, and to sharpen the focus on the most important part: the core idea being presented. These “abuses” reduce the number of things you see, and as a consequence reduce the number of distractions from the thing you want to understand.

[^1]: I mean this in a practical sense, not a social sense. If your math is so hard to understand that nobody but you learns it, it will be lost to history. But from a practical standpoint, calculus doesn’t stop being a good foundation for a video game engine just because the programmer doesn’t understand the math.

[^2]: For example, $n$ could represent some integer-valued property of a function, like the so-called *winding number*.

[^3]: For example. You don’t need to know what a homomorphism is.
