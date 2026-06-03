# Calculus with One Variable

> The derivative can be thought of as infinitesimal, symbolic, logical, geometric, a rate, an approximation, microscopic.
>
> This is a list of different ways of thinking about or conceiving of the derivative, rather than a list of different logical definitions. Unless great efforts are made to maintain the tone and flavor of the original human insights, the differences start to evaporate as soon as the mental concepts are translated into precise, formal and explicit definitions.
>
> I can remember absorbing each of these concepts as something new and interesting, and spending a good deal of mental time and effort digesting and practicing with each, reconciling it with the others. I also remember coming back to revisit these different concepts later with added meaning and understanding.
>
> – William Thurston

Calculus is a difficult subject to introduce. It has a hundred different motivating angles, a thousand books you could read, and millions of applications. You can start with basic physics, where position is a function, and derivatives are velocity and acceleration, and work your way to Newtonian mechanics.

You could aim for systems of differential equations and numerical simulations, tread the probability path and dabble in measure theory, or take a purely mathematical approach. Your ultimate goal might be machine learning, weather modeling, the frontiers of theoretical physics, economics, or operations research and optimization. These all rely on the fundamental idea of calculus: progressively better approximations ultimately produce the truth.

Luckily, as a programmer you're familiar with the existence of these fantastic applications. You may have seen and played with programmed physics models before, or programmed a sprite jumping on a screen. You're probably aware at least in a vague sense that many widely-used algorithms involve calculus. This makes the job of learning calculus much easier, because I don't have to convince you it's worth learning.

Much of the mastery of calculus (and any subject!) comes with practice. Even so, in this chapter and Chapter 14 we can survey many of the important features of a complete calculus course and do a bit of machine learning at the end. This chapter will be about calculus for functions with one input, while Chapter 14 will cover functions with many inputs.

If you've seen a lot of calculus before, you can probably tell that I don't regard it as reverently as most other authors. While I can appreciate its place in history and its applications to physics and everything else, my esteem for calculus is essentially limited to "It's a great tool for computation."

I avoid nonsense rhetoric about calculus like a plague ("With calculus you can hold infinity in the palm of your hand!"). I'd much rather use it to do something useful and draw divine inspiration from other areas of math. But that's a personal preference.

Besides calculus, in this chapter we'll dive into more detail about the process of *designing* a good mathematical definition. In doing this we'll introduce the idea of a *quantifier*, which is the basis for compound (recursive) conditions and claims.

We'll also come to understand the idea of *well-definition* in mathematics, which is how a mathematician proves (or asserts) that the definition of a concept doesn't depend on certain irrelevant details in its construction. Finally, we'll level up our proof skills by using multiple definitions in conjunction to prove theorems. The application for this chapter is an analysis of the classic Newton's method for finding roots of functions.

## Lines and Curves

### Slope of a Line

Let's start with something we know well. If you give me a line in the plane, with tick marks forming integer coordinates like in Figure 8.1, then I can tell you how "steep" the line is. That is, I can assign a number to the line, and larger numbers correspond to steeper lines while smaller numbers correspond to more gradual lines.

Also recall that the picture with coordinate axes is just one representation of the line. Another might be as a set of points $\{(x,y)\in\mathbb{R}^{2}:2y-x=2\}$. How we choose to draw the line isn't as important as the set-with-equation definition, but a good drawing swiftly reveals qualitative facts about the line (such as whether its "steepness" goes up or down).

Assigning a steepness number is easy, something most students do when they're 11 or 12 years old. Just pick two different points on the line, *any two*, call them $(x_{1},y_{1}),(x_{2},y_{2})$, and then call the *slope* of the line

$$\text{slope}(L)=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}.$$

The difference in the $y$'s corresponds to a vertical change, while the difference in $x$'s corresponds to a horizontal change. The slope is an invariant of the line because it does not depend on the choice of points. This can be proved rigorously by appealing to similar triangles. Lines and other simple functions often represent the 1-dimensional position of an object over time, while the steepness—the ratio of the change in position to the change in time—is the velocity of that object.

Before graduating from lines, let me point out that not all lines are functions from the $x$ coordinate to the $y$ coordinate. If you pick a line which is a function $y=f(x)$, then

![Figure 8.1: A line in the plane.](05 - Calculus with One Variable_images/img-0.jpeg)

the formula for the slope can be written as

$$\operatorname{slope}(f) = \frac{f(x_{2}) - f(x_{1})}{x_{2} - x_{1}}.$$

In this way, the concept of slope requires an orientation of the line and the coordinate system it is represented in. The input coordinate is defined as "horizontal" while the output coordinate is "vertical." This is the mathematician's choice, though calling $x$ the "horizontal" coordinate is standard.

### From Lines to Curves

Now let's try to translate the concepts to the curved function $f(x)$ in Figure 8.2. It has a complicated formula we won't write down. The curve is steeper at some places (e.g., $A$) and less steep at others ($B$).

Despite the self-evident fact that the line is steep at $A$ and gradual at $B$, if we were pressed to say numerically and consistently how the two steepnesses compare, we'd be at a loss. The picture gives only qualitative information. We must leave the picture behind to get useful quantitative data.

To motivate an exact answer, let's approximate steepness using tools we know. Focus on the point labeled $A$, and call it $A = (x, f(x))$. After a moment of thought, the idea naturally occurs to draw a line between $(x, f(x))$, and a nearby point $(x', f(x'))$, and have our approximation be the slope of that line, as in Figure 8.3.

$$\text{steepness}_A \approx \frac{f(x') - f(x)}{x' - x}$$

As a reminder, we adorn a variable with the tick ' (called a "prime") to denote a slight difference. So $x$ and $x'$ play similar roles, but $x'$ is slightly different from $x$ in some way.

<!-- carousel -->
![Figure 8.2: For a general curve, steepness depends on where you measure.](05 - Calculus with One Variable_images/img-1.jpeg)
![Figure 8.3: We can use the slope of a line as a proxy for the corresponding "steepness" measurement on a curve.](05 - Calculus with One Variable_images/img-2.jpeg)
![Figure 8.4: Two different lines show how the approximation can be better or worse, depending on where it is.](05 - Calculus with One Variable_images/img-3.jpeg)
<!-- endcarousel -->

We also use the $\approx$ symbol as a stand-in for the phrase "is approximately." I also went back to using the word "steepness" instead of slope because we're using the slope of a line to reason about this new kind of steepness.

My choice of $x'$ isn't that close to $x$, but I chose it to illustrate a point. While imperfect, the approximation is good enough to distinguish it from a similarly bad approximation of the steepness of $f$ at $B$, as shown by Figure 8.4.

Concrete numbers for the slopes of these two lines suggest that $f$ is twice as steep at $A$ as at $B$. Our brains itch to be more precise. Otherwise, how could we be certain we aren't fooling ourselves with inadequate picture-drawing skills? To that effort, let's improve our estimate.

### Iterating Toward the True Steepness

Once blessed with the idea of approximating the steepness of $f$ at $A$ by drawing a line from $(x, f(x))$ to some other $(x', f(x'))$, we neurotically yearn to move $x'$ closer to $x$. We could move $x'$ halfway closer to $x$, call this new point $x_1$, and update our slope approximation, as in Figure 8.5.

$$\text{steepness}_A \approx \frac{f(x_{1}) - f(x)}{x_{1} - x}$$

Our yearnings are destined for iteration. Do it again, and again, getting $\frac{f(x_2) - f(x)}{x_2 - x}$ and $\frac{f(x_3) - f(x)}{x_3 - x}$, and so on. With each step the line approximation gets better and better, closer and closer to our brain's intuitive picture of the steepness at $A$.

![Figure 8.5: Moving $x'$ halfway closer to $x$ improves the approximation.](05 - Calculus with One Variable_images/img-4.jpeg)

How do we reason about the "end" of this process? We get a number at every step. If we were to run this loop forever, would these approximate numbers approach some concrete number? If so, we could reasonably call that number the "true" steepness of $f$ at $A$.

That is exactly what limits do. A limit is computational machinery that allows one to say "this sequence of increasingly good approximations would, if followed forever, end up at a specific value." The limit of this particular line-approximation-scheme is called the derivative. We'll return to derivatives in a bit. Note in particular that whether this "limiting process" works shouldn't depend on how we move $x'$ closer to $x$. A good definition should work so long as $x'$ approaches $x$ somehow.

## Limits

### Why Definitions Are Hard

In the last section we saw a strong motivation for inventing limits, and an intuitive understanding for what a limit should look like. It's the "end result" of iteratively improving an approximation forever. You have some quantity $a_{n}$ indexed by a positive integer $n$, and as $n$ grows, $a_{n}$ eventually gets closer and closer to some target. For example, if $a_{n} = 1 - 1/n$, the numbers in the sequence $0, \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \ldots$ seem to approach 1.

But we need a definition. A definition is like the implementation of a program spec. From a specification standpoint, you care mostly about how one intends to use an interface. When actually writing the program you have to worry about people misusing your code, intentionally or not.

You have to anticipate and defend against the edge case inputs which are syntactically allowed but semantically unnatural. Anyone who has spent time designing a software library has spent hours upon hours thinking about:

- How to organize code to handle all inputs generically and elegantly.
- How to reduce cognitive load by maintaining conceptual consistency.
- How to avoid writing a mess of extra code just to handle edge cases.

Ideally a library author wants to meet all of these criteria at once! We have the same problem in mathematics.

Most concepts in math—in this case limits—usually make intuitive sense in the overwhelming majority of cases you encounter in real life. However, 99% of the work in making the math rigorous is converting the concept into concrete definitions that can handle pathological counterexamples.

By pathological, I mean examples that are mathematically valid, but which nobody would ever encounter in the wild. The best pathological examples are edge cases on steroids, and some mathematicians gain fame for constructing particularly vexing pathological examples. They're the penetration testers of mathematics. You have heard of a particularly famous one called the Cantor Set.

Indeed, much like a program, once a mathematical definition is written down it must be judged on its own merits. It must behave properly under any "input." Best practices also suggest definitions reduce cognitive load and avoid too many special cases. Achieving the right balance is a serious challenge.

An unfortunate consequence of all this is that math books start with the final definition—the end result of this arduous design process—followed by many pages of theorems and proofs explaining why it doesn't succumb to edge cases. Calculus is no different, and in fact most of how Isaac Newton and Gottfried Leibniz originally did calculus was in an informal, intuitive setting, without much rigor at all.

It was a less famous mathematician, Karl Weierstrass, who is considered to have finally "set calculus straight" (though it was really a team effort over decades). Modern calculus textbooks are a strange mix. They want to capture the informality of Leibniz, feel obliged to Weierstrass's rigor, but can't commit to either approach fully. Going full Leibniz would be error-prone.

On the other hand, the cult of Weierstrass requires detailed proof-reading skills. Alas, mathematicians are usually the only ones who enjoy the elaborate tour of blunders and false starts that historically sculpted a modern definition. One could hardly cajole the average student to care, or even the brightest student, until after those blunders come to bear on their own work.

### A Pathological Example

To my delight, you're still reading. My goal for the rest of the chapter is to whet your appetite for definition crafting. Let's continue with the "steepness of a function" as our prototypical example of a limit. Here's one of those pathological examples that makes limits hard. I'm going to define a non-curve and not-even-connected function $f:\mathbb{R}\to\mathbb{R}$ as follows: if $x$ is $1/k$ for some integer $k$, then $f(x)=2x$, otherwise $f(x)=x$. Figure 8.6 sketches $f$.

Now we can ask: what's the steepness of $f$ at $x=0$? We pick some starting $x_{1}$, compute the slope, pick an $x_{2}$, compute the slope, and keep going until we see convergence. But I dastardly chose $f$ in such a way that the limit changes depending on how you pick the sequence $x_{1},x_{2},\dots$.

In fact, if you pick $x_{k}=1/k$, every slope in the sequence is $2$, implying the limit is $2$. There isn't even an approximation because the values in the sequence are constant. But if you choose $x_{k}=\frac{1}{k+0.5}$, the slopes are always $1$. So should

![Figure 8.6: This pathological function admits two different possibilities for the derivative depending on the sequence of approach.](05 - Calculus with One Variable_images/img-5.jpeg)

the limit be 1 or 2? Neither?

This will be the last pathological example I inflict upon you, but it emphasizes an important point. However we choose to define derivatives, it should not depend on the arbitrary choice of which points you use to do the approximation. It should be a definition like "no matter how your $x$ values approach the target, the slope limit is the same."

The generic mathematical term for this is that the derivative should be well-defined. Two of the definitions we scrutinize in this chapter—the limit of a function (Definition 8.4) and the derivative (Definition 8.6)—will encounter the issues above. The quality of Definition 8.1, which defines the limit of a sequence of numbers, and its subsequent analysis provide a foundation that ensures well-definition.

### The Limit of a Sequence

With that thought, let's start with the limit of a sequence of numbers, which will be used to define limits for functions. Since sequences of numbers can have repetition, we won't use set notation (though some authors do).

Instead we'll use a comma notation $x_{1}, x_{2}, \ldots$ which the strongly-typed programmer can think of as the output of an iterator which never terminates, or a tuple/array of infinite length $(x_{1}, x_{2}, \ldots)$. The $\varepsilon$ character is a lower-case Greek epsilon, contextually used across mathematics as a small positive real number.

**Definition 8.1.** Let $x_{1}, x_{2}, \ldots$ be a sequence of real numbers, one $x_{n}$ for each $n \in \mathbb{N}$, and let $L \in \mathbb{R}$ be fixed. We say that $x_{n}$ converges to $L$ if for every threshold $\varepsilon > 0$, there is a corresponding $k \in \mathbb{N}$ so that all the $x_{n}$ after $x_{k}$ are within distance $\varepsilon$ of $L$. We also equivalently say the limit of $x_{n}$ is $L$.

This is the first time we've encountered a definition that relies heavily on alternating quantifiers (for every..., there is...), so let's discuss it in detail. A statement like "for every FOO there is a BAR," means there's a computational relationship.

If you give me a FOO as input, I can produce a BAR with the desired property as output. In fact there may be many such BARs. Interpreting this for Definition 8.1, the input is a real number threshold $\varepsilon>0$, and the output is an integer $k$ with a special property. So the relationship is:

```java
int sequence_index_from_threshold(float epsilon) {
    // compute k depending on epsilon
    return k;
}
```

The special property of $k$ is that all the sequence elements after $k$ are close to $L$. They're at least as close as specified by $\varepsilon$.

### Proving a Sequence Converges

As a simple non-pathological example, let's take the sequence $x_{n}=1-\frac{1}{n}$. This is the sequence $0,\frac{1}{2},\frac{2}{3},\frac{3}{4},\frac{4}{5},\dots$. Our intuition tells us that the limit should be $L=1$, so let's prove it strictly by the letter of the definition.

First let's see a concrete example of the threshold-to-sequence-index functional relationship. If you require $\varepsilon=1/4$, I need to find an index after which all $x_{n}$ are within $1/4$ of $1$. I.e., all these $x_{n}$'s should satisfy $1-1/4<x_{n}<1+1/4$.

Another way to write this is with the absolute value: $|x_{n}-1|<1/4$. Since we already see that $3/4$, also known as $1-1/4$, is one of the sequence elements, it should be easy to guess that everything starting at $k=5$ will be close enough to $1$. Indeed, we can do the algebra.

$$|x_{n}-1|=\left|\left(1-\frac{1}{n}\right)-1\right|=\left|-\frac{1}{n}\right|=\frac{1}{n},$$

and $1/n<1/4$ when $n>4$.

Now let $\varepsilon>0$ be unknown, but fixed. We can do the same algebra as above. How large of an index $k$ do we need to ensure $|x_{n}-1|<\varepsilon$ for all $n>k$? In other words, can I write $\varepsilon$ in terms of $n$ so that all of the above equations and inequalities are still true when I replace $1/4$ with $\varepsilon$?

Above we showed that $|x_{n}-1|=1/n$, so to ensure that $1/n<\varepsilon$ we can rearrange to get $n>1/\varepsilon$. Picking any index $k$ bigger than that will work. Since $\varepsilon$ is fixed, pick $k=\lceil 1/\varepsilon\rceil$ (the "ceiling" of $1/\varepsilon$). Let me restate all of this as a theorem with a proof as you might see in a book.

###### Theorem 8.2.

The limit of the sequence $x_{n}=1-\frac{1}{n}$ is $1$.

###### Proof.

Let $\varepsilon>0$ be fixed. Pick any integer $k>1/\varepsilon$. We will show that $|x_{n}-1|<\varepsilon$ for all $n\geq k$. Indeed,

$$|x_{n}-1|=\left|\left(1-\frac{1}{n}\right)-1\right|=\left|-\frac{1}{n}\right|=\frac{1}{n},$$

and because $n\geq k>1/\varepsilon$, we have $1/n\leq 1/k<\varepsilon$. $\blacksquare$

You can think of this $\varepsilon$-to-$k$ process as a game. A skeptical contender doesn't believe $x_{n}$ converges to $L$, and challenges you to find the tail of the sequence that stays within $\varepsilon=1/2$ of $L$. You provide such a $k$, but the contender isn't happy and re-ups the challenge using $\varepsilon=1/100$.

You comply with a bigger $k$. The contender retorts with $\varepsilon=(1/2)^{99}$. Unfazed, you still produce a working $k$. If there's any way for the contender to stump you in this game, then $x_{n}$ doesn't converge to $L$. But if you can always produce a good $k$ no matter what, the sequence converges to $L$.

We can play the contender's game in code. For each threshold the contender throws, we hand back the proof's index $k=\lceil 1/\varepsilon\rceil$ and then *verify* that every one of the next several thousand terms really does stay within $\varepsilon$ of $1$. The skeptic never wins.

```python
<!-- include: code/pim/05 - Calculus with One Variable/01_limit_sequence_game.py -->
```

### Quantifier Notation

As a notational side note, the phrase "for every $x$ there is a $y$" can be long and annoying to write all the time. It also makes it difficult to study the *syntactic* structure of statements like this, since dependence among variables may be unclear.

Mathematicians designed an unambiguous notation for this situation called *quantifiers*. We briefly introduced quantifiers in Chapter 4, and promised we wouldn't use them in this book. However, standard textbook definitions often use the symbols heavily, so this digression helps put what you might see elsewhere in context.

The first quantifier is the symbol $\forall$, which means "for all" (the upside-down A stands for All). The second is $\exists$, which stands for "there exists" (the backwards E in "Exists"). Quantifiers may appear in any order. If I claim

$$\exists x\in\mathbb{R},\forall y\in\mathbb{R},x+y=3,$$

I'm saying I can come up with a real number $x$, such that no matter which $y$ you produce, it's true that $x+y=3$. Obviously no such $x$ exists, so the statement is false. Note the meaning changes if the order of the quantifiers is reversed: for every $y$, there is indeed an $x$ for which $x+y=3$, it's $x=3-y$.

If I were to state the definition of the limit in its briefest form, I might say:

$$x_{n}\text{ converges to }L\text{ if: }\forall\varepsilon>0,\exists k>0,\forall n>k,|x_{n}-L|<\varepsilon.$$

We've just packed the math like sardines in a tin box. That being said (and now we're really digressing), some situations benefit from writing logical statements in this form. Particularly in the realm of formal logic, it turns out that as you add more "alternating" quantifiers ($\forall x\exists y\forall z$), you get progressively more expressive power.

In theoretical computer science this is formalized by the so-called *polynomial hierarchy*, which conjecturally asserts that the computational cost of deciding the truth of generic logical statements increases dramatically with the number of alternating quantifiers.

That's why one might believe factoring integers ($\exists a,\exists b,ab=n$) is easier than deciding if one can force a win in a two player game like chess (there exists a move for me, such that for every move for my opponent, there exists a move for me, such that (…), such that I have a winning move).

### Convergence and Divergence

Back to limits. The definition of a limit allows a sequence to have no limit, like the sequence $0,1,0,1,0,\dots$, which isn't pathological at all. For this sequence you can't even satisfy the limit definition with $\varepsilon=1/3$ (no matter what you think the limit $L$ might be!).

![Figure 8.7: Starting in the top left corner, we want to deduce the top right corner. We do this by taking the longer route down and around.](05 - Calculus with One Variable_images/img-6.jpeg)

This fits with our intuition that an alternating $(0,1,0,1,\ldots)$ sequence doesn't "get closer and closer" to anything. So now we can add to our definition.

**Definition 8.3.** Let $x_{n}$ be a sequence of real numbers. If there is an $L$ satisfying the definition of the limit for $x_{n}$, we say that $x_{n}$ converges. Otherwise, we say it does not converge.

Sometimes we abbreviate the claim that $x_{n}$ converges to $L$ by the notation $\lim_{n\to \infty}x_n = L$, and sometimes even more compactly as $x_{n}\rightarrow L$. In this setting, the symbol $\infty$ doesn't have any concrete mathematical meaning by itself, it's just notation to remind us that we're talking about $n$'s that get arbitrarily large.

### The Limit of a Function

Now we're ready to define the limit of a function.

**Definition 8.4.** Let $f: \mathbb{R} \to \mathbb{R}$ be a function. Let $c$ and $L$ be real numbers. We say that $\lim_{x \to c} f(x) = L$ if for every sequence $x_n$ that converges to $c$ (and for which $x_n \neq c$ for all $n$), the sequence $f(x_n)$ converges to $L$.

The notation $f(x_{n})$ is shorthand for a sequence $y_{n} = f(x_{n})$. In this context we're implicitly "mapping" $f$ across the sequence $x_{n}$ as one would say in functional programming, or alternatively we're "vectorizing" $f$. The notation $x \to c$ is used to signify that $x_{n}$ is a sequence converging to $c$, and the value of $x$ is used in the expression inside the limit.

Let's do another simple example: compute $\lim_{x\to 2}x^2 -1$. We prove it directly. Given any sequence $x_{n}$ for which $x_{n}\rightarrow 2$ and $x_{k}\neq 2$, we must prove that $f(x_{n})\to L$ for a specific $L$. Most often $L = f(c)$, which in this example is $f(2) = 3$.

###### Proposition 8.5.

$$\lim_{x \to 2} x^{2} - 1 = 3.$$

###### Proof.

Let $\varepsilon > 0$ be the threshold required by the definition of $f(x_{n}) \to 3$. We'll use the proof of the fact that $x_{n} \to 2$ as a subroutine for some special $\varepsilon'$ that we choose, and use the index we get as output to prove that $f(x_{n}) \to 3$.

Figure 8.7 contains a diagram to illustrate the gymnastics. The top row is the theorem we want to prove, with the input on the left and the desired output on the right. Likewise, the bottom row is the black box subroutine for $x_{n}\to 2$. Given the initial $\varepsilon>0$ that we don't get to pick, we choose a threshold $\varepsilon^{\prime}$ to use for $x_{n}\to 2$. Picking a useful $\varepsilon^{\prime}$ is the tricky part of these kinds of proofs.

To that effort, at the end of the day we need to show that

$$|f(x_{n})-3|=|x_{n}^{2}-4|=|(x_{n}+2)(x_{n}-2)|<\varepsilon.$$

We get to control how close $x_{n}$ is to 2 and how fast it gets there—this will be the subroutine proving that $x_{n}\to 2$ and the choice of $\varepsilon^{\prime}$. Through that control we can make the term $|x_{n}-2|$ small. As long as we can make $|x_{n}-2|$ smaller faster than the other term $(x_{n}+2)$ grows (which may be a consequence of us trying to make $|x_{n}-2|$ small), we'll be able to make the product $|(x_{n}+2)(x_{n}-2)|$ as small as we need.

To achieve this, we need to reason about how much $x_{n}+2$ can grow as $x_{n}\to 2$. Since we know $x_{n}$ will eventually be close to 2, we can analyze that growth in the range $1<x_{n}<3$, i.e., when $\varepsilon^{\prime}<1$. In this range, $|x_{n}+2|<5$. This bounds the growth as described, and simplifies the expression.

$$|(x_{n}+2)(x_{n}-2)|<5|x_{n}-2|.$$

We are nearly victorious. Now we want to choose $\varepsilon^{\prime}$ smaller than 1, such that $5|x_{n}-2|<\varepsilon$. Since $\varepsilon^{\prime}$ also controls the size of $x_{n}-2$ (it's the threshold for the subroutine for $x_{n}\to 2$) we arrive at $5|x_{n}-2|<5\varepsilon^{\prime}$.

Finally, we can solve: $5\varepsilon^{\prime}<\varepsilon$ when $\varepsilon^{\prime}<\varepsilon/5$. Combining the pieces together, we can start the proof from the beginning, explicitly invoking the subroutine this time.

Let $\varepsilon>0$ be arbitrary. Choose $\varepsilon^{\prime}<\min(1,\varepsilon/5)$, and choose $k$ such that $|x_{n}-2|<\varepsilon^{\prime}$ for all $n>k$. In this range,

$$|f(x_{n})-3|=|x_{n}^{2}-4|=|(x_{n}+2)(x_{n}-2)|<5|x_{n}-2|<5\varepsilon^{\prime}<\varepsilon,$$

which proves that $f(x_{n})\to 3$. $\blacksquare$

### Analysis and Approximation Style

All of this was a formal way of saying that to compute $\lim_{x\to 2}x^{2}-1$, you may "plug in" $2$ to the expression $x^{2}-1$. Indeed, in almost all cases where the expression inside the limit is defined (and continuous) at the limiting input (in this case $x=2$), you can do that.

But there are non-pathological functions with useful limits (not just the derivative) for which you can't simply "plug the value in." See the exercises for a famous example. To reiterate from earlier, all of this hefty calculus machinery was invented to deal with those difficult functions.

This proof embraces a style of mathematics called analysis. The term "analysis" can refer to specific subfields of study, such as real analysis or complex analysis which are the formalizations of calculus for real and complex numbers. More broadly, an area of math called "analysis" stresses proof techniques that deal with bounds and approximations.

The error in these approximations can be controlled to achieve the necessary goals: loosely when attempting to simplify complexity that is irrelevant to the goal, or tightly when that complexity needs to be understood to achieve the goal. As Weierstrass practiced in formalizing calculus, analysis aims to reduce problems to parts that can be independently understood with number sense.

This is why, as we recalled in Chapter 7, Henri Poincaré calls the analytical approach a "prolongation of arithmetic." This also motivates the Taylor series that we'll see later in this chapter. They further prolong our arithmetic abilities to express things that finite sums cannot, giving us further tools to control the quality of an approximation.

As we saw with our pathological "two lines" example from Figure 8.6, not every function has a limit at every point. For the "two lines" $f(x)$, we computed the slope as $\frac{f(x_{n})-f(0)}{x_{n}-0}$ where $x_{n}$ was part of a sequence tending to zero. I.e., we informally computed the limit $\lim_{x\to 0}\frac{f(x)-f(0)}{x-0}$.

But then we found two sequences $a_{n},b_{n}$ that both converge to zero, but their slope-sequences $\frac{f(a_{n})-f(0)}{a_{n}-0}$, $\frac{f(b_{n})-f(0)}{b_{n}-0}$ gave different values. As a consequence, the limit cannot be equal to either value. So we've seen that this definition of the limit passes a litmus test: good functions have limits, and bad functions do not.

### Arithmetic Rules for Limits

Before continuing, here are a few basic propositions for working with limits that will come in handy in the rest of the chapter and in the exercises. Most calculus or real analysis textbooks will contain a detailed proof.

Basically, they say that most arithmetic operations are compatible with limits, provided the limits involved exist. These formalize the general rule that, absent of any strange function behavior, you can "plug in" the sequence limit to get a function limit, i.e., that $f(a)=\lim_{x\to a}f(x)$.

- For all constants $c$, $\lim_{x\to a}cf(x)=c\lim_{x\to a}f(x)$.
- $\lim_{x\to a}(f(x)+g(x))=\lim_{x\to a}f(x)+\lim_{x\to a}g(x)$, provided that each limit on the right hand side exists.
- $\lim_{x\to a}f(x)g(x)=(\lim_{x\to a}f(x))\cdot(\lim_{x\to a}g(x))$, provided that each limit on the right hand side exists.
- $\lim_{x\to a}g(f(x))=g(f(a))$, provided that $\lim_{x\to a}f(x)=L$ exists and $g$ is continuous at $L$.

## The Derivative

### Definition and a First Computation

Now we define the derivative, which formalizes the steepness of a function $f(x)$ at a given input $x=c$.

###### Definition 8.6.

Let $f:\mathbb{R}\to\mathbb{R}$ be a function. Let $c\in\mathbb{R}$. The derivative of $f$ at $c$, if it exists, is the limit

$$\lim_{x\to c}\frac{f(x)-f(c)}{x-c}.$$

This value is denoted $f^{\prime}(c)$. In the limit, sequences $x_{n}\to c$ are taken so that $x_{n}\neq c$ to avoid division by zero.

Let's compute an example, the derivative of $f(x)=x^{2}-6x+1$ at $c=3$. A priori (without looking at a plot of the function) we might have no clue whether the derivative is even positive or negative at $3$. By definition, it's:

$$
\begin{aligned}
f^{\prime}(3) &=\lim_{x\to 3}\frac{f(x)-f(3)}{x-3} \\
&=\lim_{x\to 3}\frac{x^{2}-6x+9}{x-3} \\
&=\lim_{x\to 3}\frac{(x-3)(x-3)}{x-3}
\end{aligned}
$$

We can now simplify $(x-3)/(x-3)=1$. Indeed, recalling the definition of the limit, the expression $\frac{(x-3)(x-3)}{x-3}$ is evaluated at the entries of a sequence $x_{n}$ for which $x_{n}\neq 3$. Hence, we never divide zero by zero and may simplify.

$$
\begin{aligned}
f^{\prime}(3) &=\lim_{x\to 3}\frac{(x-3)(x-3)}{x-3} \\
&=\lim_{x\to 3}x-3 \\
&=0
\end{aligned}
$$

The derivative is the *limit* of the difference quotient, so we can watch that limit happen numerically. Sliding $x'$ halfway closer to $c=3$ over and over — exactly the iterative scheme from Figure 8.5 — the quotient marches straight toward the exact symbolic value $f'(3)=0$ that sympy computes for us.

```python
<!-- include: code/pim/05 - Calculus with One Variable/02_derivative_difference_quotient.py -->
```

### The Derivative as a Function

This was a nice exercise, but it's tedious to compute derivatives over and over again for every input. It would be much more efficient to instead compute a compact representation of the derivative at all possible points. That is, we want a process which, when given a differentiable function $f:\mathbb{R}\to\mathbb{R}$ as input, produces another function $g:\mathbb{R}\to\mathbb{R}$ as output, such that $g(c)=f^{\prime}(c)$ for every $c$.

While computing the limit may be tedious, our representation of $g$ should make subsequent derivative calculations as computationally easy as evaluating $f$.

If you ask a mathematician how to come up with such a $g$, you'd probably receive the reply, "You just do it." This means we can calculate directly from the definition. If, for example, $f(x)=x^{2}$,

$$
\begin{aligned}
f^{\prime}(c) &=\lim_{x\to c}\frac{f(x)-f(c)}{x-c} \\
&=\lim_{x\to c}\frac{x^{2}-c^{2}}{x-c} \\
&=\lim_{x\to c}\frac{(x-c)(x+c)}{x-c} \\
&=\lim_{x\to c}x+c \\
&=2c
\end{aligned}
$$

Forever after, we may plug in the desired value of $c$ to get the derivative at $c$. Most mathematicians don't switch variables, so they'd call the derivative function $f^{\prime}(x)$ instead of $f^{\prime}(c)$. This has the added advantage of displaying patterns in derivative computations.

For example, if you compute the derivative of $x^{4}$, you get $4x^{3}$, and the derivative of $x^{8}$ is $8x^{7}$, suggesting the correct rule that the derivative of $x^{n}$ is $nx^{n-1}$ (for a positive integer $n$). Here, the notation makes this pattern clear in a way that pictures do not. In fact, if you want to prove this, the following theorem makes the limit calculation less painful.

###### Theorem 8.7.

For any real numbers $x,c$ and any positive integer $n$,

$$x^{n}-c^{n}=(x-c)(x^{n-1}+x^{n-2}c+x^{n-3}c^{2}+\cdots+xc^{n-2}+c^{n-1}).$$

I'll call the sum $(x^{n-1}+x^{n-2}c+\cdots+c^{n-1})$ "the ugly sum."

###### Proof.

Start to multiply the right-hand side and notice that each term, except the first and last, pair off and sum to zero. In particular, you get

$$
\begin{aligned}
&x^{n} \\
&+[-c\cdot x^{n-1}+x\cdot x^{n-2}c] \\
&+[-c\cdot x^{n-2}c+x\cdot x^{n-3}c^{2}] \\
&\quad\vdots \\
&+[-c\cdot xc^{n-2}+x\cdot c^{n-1}] \\
&+(-c\cdot c^{n-1})
\end{aligned}
$$

Each of the square-bracketed terms is zero and can be removed. $\blacksquare$

Tenderly applying Theorem 8.7 while computing the derivative of $f(x)=x^{n}$ reveals that in the limit defining $f^{\prime}(x)$ you can cancel two $(x-c)$ terms, as in our previous examples, leaving just the ugly sum. Plugging $x=c$ in to the ugly sum gives $nc^{n-1}$.

###### Theorem 8.8.

For every integer $n\geq 1$, the derivative of $x^{n}$ is $nx^{n-1}$.

The whole power rule is hiding inside that factoring identity, so it is worth seeing both pieces verified at once. The following demo confirms, symbolically and for every $n$ up to $8$, that $(x-c)$ times the ugly sum really is $x^n - c^n$, that the ugly sum collapses to $n\,c^{n-1}$ when $x=c$, and that this matches the actual derivative sympy reports for $x^n$.

```python
<!-- include: code/pim/05 - Calculus with One Variable/03_power_rule_ugly_sum.py -->
```

### Linearity, the Chain Rule, and Notation

At this point in a standard calculus course, a student would spend a few weeks (or months) learning:

1. The derivatives of particular "elementary" functions, such as polynomials, $\sin(x)$, $e^{x}$, and $\log x$.
2. When given two functions $f,g$ whose derivatives you know separately, how to compute the derivative of an elementary combination of $f$ and $g$, such as $f+3g$ and $f(g(x))$.
3. How to use special values of the derivative (such as zero) to find maxima and minima of various functions, such as maximizing profit from selling a widget subject to costs for creating certain variations of that widget.
4. Assorted nonsense like the derivative of the inverse cosine function.

Because this book can only give you a taste of calculus, and because we're rushing to an interesting application, we'll skip most of this in favor of stating the facts that are, in my view, the most important for applications.

Let $F$ be the set of all functions $\mathbb{R}\to\mathbb{R}$ that have derivatives. Let $D$ be the function that takes as input a function $f$ and produces as output its derivative $f^{\prime}$. Note the domain of $D$ is $F$, but its codomain is not $F$ because some differentiable functions are not twice differentiable.

###### Theorem 8.9.

$D$ is a linear function. Meaning $D(f+g)=D(f)+D(g)=f^{\prime}+g^{\prime}$, and $D(cf)=cD(f)=cf^{\prime}$ for any $c\in\mathbb{R}$.

As a function, "$cf$" is the function that takes as input $x$ and produces as output $c\cdot f(x)$. Likewise, $f+g$ takes as input $x$ and produces as output $f(x)+g(x)$.

As a quick aside, I hate writing sentences like "the function that on input $x$ produces as output $c\cdot f(x)$." Instead I like to use the mathematical analogue of "anonymous function" notation, using the $\mapsto$ symbol. So I can instead say "$cf$ is defined by $x\mapsto c\cdot f(x)$," or even "$D$ is the function $f\mapsto f^{\prime}$." When you're reading this out loud, $\mapsto$ is pronounced "maps to."

This derivative-computing function $D$ is also often written as $\frac{d}{dx}$, but this causes inconsistent notation like $\frac{d}{dx}(f)$ versus $\frac{df}{dx}$ and forces one to choose a variable name $x$. In my opinion, this notation exists for bad reasons: backwards compatibility with legacy math, and trying to trick you into thinking that derivatives are fractions so you'll guess the forthcoming chain rule. But it is too widespread to avoid.

Theorem 8.9 immediately lets us compute the derivative of any polynomial, because we can use Theorem 8.8 to compute the derivatives of each term and add them up. E.g., the derivative of $3+2x-5x^{3}$ is $2-15x^{2}$. Quick spot check exercise: using intuition, reason that a constant function like $f(x)=3$ has derivative $f^{\prime}(x)=0$. If your intuition fails you, use the definition of the limit to compute it.

The other crucial fact, which we'll use later, is the chain rule.

###### Theorem 8.10 (The chain rule).

Let $f,g:\mathbb{R}\to\mathbb{R}$ be two functions which have derivatives. Then the derivative of $f(g(x))$ is $f^{\prime}(g(x))g^{\prime}(x)$.

In the chapter exercises you'll look up a proof of this theorem. The chain rule makes it easy to compute derivatives that would require a lot of algebra to compute, such as $\left(x^{2}-10\right)^{50}$. Here $f$ is $z\mapsto z^{50}$ and $g$ is $x\mapsto x^{2}-10$, so the derivative is $50(x^{2}-10)^{49}\cdot(2x)$.

The chain rule also lets us compute derivatives that would otherwise be completely mysterious, such as that of $\sin(e^{x})$. If you're told what the derivatives of $\sin(x)$ and $e^{x}$ are separately, then you can compute the derivative of the composition.

As a notational side note, let me explain the "fractions make you guess the chain rule" remark. Call $h(x)=f(g(x))$. Then if we use the fraction notation $\frac{dh}{dx}$ for the derivative of $h$, the standard way to write the chain rule for this would be $\frac{dh}{dx}=\frac{dh}{dg}\cdot\frac{dg}{dx}$.

The "hint" of the notation is that if you're a reckless miscreant, you might jump to the conclusion that the $dg$'s "cancel" like fractions do. Rest assured that is not how it works, but calculus students the world over are encouraged to do it this way because the resulting rule is correct. We'll return to this in Chapter 14.

Historically, symbols like $dx$ had no concrete mathematical meaning. They were called "infinitesimals" and regarded informally as quantities infinitely smaller than any fixed value. More recently, $dx$ was retroactively assigned a semantic meaning that allows one to work with it as the notation suggests. The formalism is beyond the scope of this book.

## Taylor Series

### Approximation by a Line

If you got ten mathematicians in a room they'd come up with twenty different ways to motivate calculus. In this chapter we used, "generalize the slope of a line to curvy things," but here's another. One prevalent idea is to take a complicated thing and approximate it by simpler things.

Without calculus, the simplest function we fully understand is a straight line. So we might ask, "Given a function $f:\mathbb{R}\to\mathbb{R}$ and a point $x\in\mathbb{R}$ at which $f$ is differentiable, what line best approximates $f$ at $x$?"

If you define "best approximates" in a particular but reasonable way, the answer to this question uniquely defines the derivative. Call $L(x)$ the line approximation of $f$ we get using the derivative of $f$ at $x=c$. That is, $L(x)=f^{\prime}(c)(x-c)+f(c)$. This is just the line passing through $(c,f(c))$ with slope $f^{\prime}(c)$, often called the "tangent line" to $f$ at $c$.

Before we state the "official" definition, let's try crafting an artisanal definition from a naive guess at what "best approximates" should mean. Let's say the line $L(x)$ "best approximates" $f(x)$ at $c$ if, for any other line $K(x)$ that passes through $(c,f(c))$, for every $x$ the line $L(x)$ is closer to $f(x)$ than $K(x)$. Note the two universal quantifiers in the statement. Sadly, this doesn't work.

Take our example from earlier, replotted in Figure 8.8. There, the line between $A$ and $A'$ is not the tangent line at $A$, and it is also far closer to $f$ at $A'$ than the tangent line would be. However, for points close to $A$, the tangent line is a much better approximator. If we're trying to approximate $f$ "at" $A$, we care more about points closer to $A$ than points far from $A$. Here's how we make this clear in the math.

![Figure 8.8: The line between $A$ and $A'$ does not approximate $f$ well close to $A$.](05 - Calculus with One Variable_images/img-7.jpeg)

Take any line $K(x)$ that is supposedly challenging the tangent line for the title of "best approximating line of $f$ at $x = c$." Then I claim I can choose a small enough interval around $c$ (the width of this interval depends on the features of the challenger $K$) so that $L$ beats $K$ on all points in this interval. Here's the formal theorem I'll prove momentarily.

###### Theorem 8.11.

Let $f: \mathbb{R} \to \mathbb{R}$ be a function and $A = (c, f(c))$ be a point on $f$ at which $f$ is differentiable. Let $L(x)$ be the tangent line at $c$, i.e. $L(x) = f'(c)(x - c) + f(c)$. Then for every line $K(x)$ passing through $(c, f(c))$, there is a sufficiently small $\varepsilon > 0$ such that if $|x - c| < \varepsilon$, then $|L(x) - f(x)| \leq |K(x) - f(x)|$.

Notation time: people often write the set of points $\{x\in \mathbb{R}:|x - c| < \varepsilon \}$ using the "open interval" notation $(c - \varepsilon ,c + \varepsilon)$. They also often call this an epsilon-ball around $c$.

Using this, the last sentence of the theorem might read, "For all $x\in (c - \varepsilon ,c + \varepsilon)$, it holds that $|L(x) - f(x)|\leq |K(x) - f(x)|$." This makes the statement clearer. Instead of saying "if this then that," you're saying what you want to say outright, that "FOO is always true in my domain of interest."

###### Proof.

If $K$ is a line passing through $(c, f(c))$, then it can be written in the same way as $L$ but with a different slope. I.e., for some $m \in \mathbb{R}$, $K(x) = m(x - c) + f(c)$.

Expanding $K$ and $L$ according to their formulas, the theorem's conclusion requires us to choose an $\varepsilon > 0$ such that when $|x - c| < \varepsilon$ the following inequality is true.

$$|f^{\prime}(c)(x-c)+f(c)-f(x)|\leq|m(x-c)+f(c)-f(x)|$$

We don't yet know this inequality is true, but we can "work backwards" by doing valid algebraic manipulations until we get to something we know is true. In particular, one might recognize the definition of the derivative hiding in there and divide by $|x-c|$ to get

$$\left|f^{\prime}(c)-\frac{f(x)-f(c)}{x-c}\right|\leq\left|m-\frac{f(x)-f(c)}{x-c}\right|.$$

The fraction $\frac{f(x)-f(c)}{x-c}$, which is on both sides, is most of the definition of the derivative, missing only the limit. And $f^{\prime}(c)$ is the *value* of that limit, whereas $m$ is some other number. This should already make it pretty clear that the inequality above holds, but let's prove it formally by contradiction.

Suppose to the contrary that no matter which $\varepsilon$ I choose, there is some $x$ in $(c-\varepsilon,c+\varepsilon)$ that contradicts the inequality above. I would like to pick a sequence of $x$ values going to $c$ that violates the definition of the derivative. I will do that by picking a sequence of $\varepsilon$'s, using the supposed hypothesis that the inequality above is false for *every* $\varepsilon$, and arriving at the sequence of $x$'s needed for my contradiction. Let

$$(\varepsilon_{1},\varepsilon_{2},\varepsilon_{3},\dots)=(1,1/2,1/3,\dots)$$

and let $x_{1},x_{2},x_{3},\dots$ be the corresponding $x$'s violating the inequality for each $\varepsilon_{i}$. Since each $x_{i}$ is in $(c-\varepsilon_{i},c+\varepsilon_{i})$, it follows that $x_{i}\to c$, but because (by assuming the contradictory hypothesis) the inequalities are false, the sequence $\frac{f(x_{i})-f(c)}{x_{i}-c}$ *does not* converge to $f^{\prime}(c)$.

The contradictory hypothesis says it's closer to $m$ instead. This contradicts the definition of the derivative. $\blacksquare$

We have proved that derivatives provide the best linear approximation to a function at a point for a concrete sense of "best." This raises a natural question. Can we improve this approximation by using more complicated functions than lines? The answer is yes. The tool is called the Taylor polynomial.

### Taylor Polynomials

One nice thing about polynomials is that they have a *grading*. By that I mean, if you increase the degree of your polynomial, you can express a wider variety of functions. In principle, higher degree allows a polynomial to express more complexity, and produces better approximations of $f$.

You can derive exactly how this works by following the steps of Theorem 8.11, and asking for a degree at most $2$ polynomial *whose derivative best approximates $f^{\prime}$ close to $a$*. Suppose our candidate is the following (where below $q^{*}\in\mathbb{R}$ is the unknown parameter we must set to get a degree $2$ polynomial).

$$p(x)=q^{*}(x-a)^{2}+f^{\prime}(a)(x-a)+f(a)$$

We can't avoid using $f^{\prime}(a)$ for the coefficient of the $(x-a)$ term, because $p^{\prime}(a)$ needs to be exactly $f^{\prime}(a)$ and $p^{\prime}(x)$ is

$$p^{\prime}(x)=2q^{*}(x-a)+f^{\prime}(a).$$

Plugging in $x=a$ leaves only $f^{\prime}(a)$. In the same way, in Theorem 8.11 we couldn't avoid using $f(a)$ for the constant term because the line had to pass through $(a,f(a))$. And so if we want to optimize $p^{\prime}(x)$ by choosing $q^{*}$, it's almost *exactly* the same proof as Theorem 8.11, with the difference being an extra factor of $2$.

We'll leave it as an exercise for the reader to redo the steps, but at the end you get $q^{*}=\frac{f^{\prime\prime}(a)}{2}$, where $f^{\prime\prime}$ is the derivative of the derivative of $f$ (the "second" derivative of $f$).

Two quick asides. First, the attempt to use the second derivative only makes sense if $f$ has a first derivative at that point, and as we saw not all functions have derivatives at all points. Second, adding more and more primes to denote repeated applications of the derivative operation is cumbersome. Rather, it's customary to use a parenthetical superscript notation $f^{(n)}(x)$ for the $n$-th derivative of $f$.

You call a function $n$-times differentiable if it has $n$ derivatives at every point. If $f$ has infinitely many derivatives (i.e., it is $n$-times differentiable for every $n\in\mathbb{N}$), $f$ is called *smooth*. The typical example of a smooth function is $\sin(x)$ or $2^{x}$. A default modeling assumption is that life is smooth, and when it's not you pay very close attention.

Our exploration has led us to the Baby Taylor Theorem.

###### Theorem 8.12 (The Baby Taylor Theorem).

Let $f:\mathbb{R}\to\mathbb{R}$ be a twice-differentiable function and let $(a,f(a))$ be a point on $f$. Then there is a unique degree at most 2 polynomial $p(x)$ which simultaneously is the best approximation of $f$ close to $a$, and its derivative $p^{\prime}(x)$ is the best approximation of $f^{\prime}(x)$ close to $a$. This polynomial is:

$$p(x)=f(a)+f^{\prime}(a)(x-a)+\frac{f^{(2)}(a)}{2}(x-a)^{2}$$

A proof by induction, which the reader should finish (we just did the step from $n=1$ to $n=2$ which has all the features of the general induction), extends the Baby Taylor Theorem to the Adolescent Taylor Theorem. Note that by $n!$ we mean the factorial function $n\mapsto n\cdot(n-1)\cdot(n-2)\cdot\dots\cdot 2\cdot 1$ where $n$ is a positive integer. We're not merely excited about $n$, though it is bittersweet to have watched $n$ grow up so fast.

###### Theorem 8.13 (The Adolescent Taylor Theorem).

Let $f:\mathbb{R}\to\mathbb{R}$ be a $k$-times differentiable function and let $(a,f(a))$ be a point on $f$. Then the degree at most $k$ polynomial that best approximates $f$ and all of the $k$ derivatives of $f$ simultaneously close to $a$ is[^1]

$$p(a)+\sum_{n=1}^{k}\frac{f^{(n)}(a)}{n!}(x-a)^{n}$$

This is called the degree $k$ Taylor polynomial of $f$ at $a$.

[^1]: Like the Baby Taylor Theorem, here I mean that $p$ approximates $f$, $p^{\prime}$ approximates $f^{\prime}$, $p^{\prime\prime}$ approximates $f^{\prime\prime}$, etc.

As if possessed by the spirit of Leonhard Euler, we write down examples. Here are the first three terms of the general summation.

$$f(a)+\frac{f^{\prime}(a)}{1!}(x-a)+\frac{f^{(2)}(a)}{2!}(x-a)^{2}+\frac{f^{(3)}(a)}{3!}(x-a)^{3}$$

To have an example that's not already a polynomial, let $f(x)=e^{x}$. Recall or learn now that the derivative of $e^{x}$ is also $e^{x}$. In fact, the number $e$ is uniquely defined by this property. Then the degree 4 Taylor polynomial for $e^{x}$ at $x=0$ is particularly simple because $e^{0}$ is 1 in every term:

$$1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+\frac{x^{4}}{24}.$$

Figure 8.9 contains a picture of $e^{x}$ and its approximation by the degree 4 Taylor polynomial. The approximation is faithful to the original function, but only close to $x=0$. Elsewhere it can be arbitrarily bad.

![Figure 8.9: The degree 4 Taylor polynomial of $f(x) = e^{x}$ at $x = 0$.](05 - Calculus with One Variable_images/img-8.jpeg)

We can build these polynomials and watch the approximation improve. The demo below confirms Kun's printed degree-4 polynomial for $e^x$ exactly, then evaluates the degree-$k$ polynomial at $x=1$ and prints the remainder $|e^x - p_k(x)|$, which shrinks toward zero as $k$ grows — each extra Taylor term buys you more correct digits. It also recovers the textbook alternating series for $\sin x$.

```python
<!-- include: code/pim/05 - Calculus with One Variable/04_taylor_remainder.py -->
```

The Taylor polynomial is one of the most often used applications of mathematics to itself. The reason is because when you're analyzing a mathematical problem, it's easy to define functions with convoluted behavior. One example of this is in machine learning, when you analyze the probability that a classifier is wrong.

You can often write down the probability as a massive product, but can't compute it exactly. Instead, one often uses a small-degree Taylor polynomial to approximate it. With knowledge of whether the Taylor polynomial is an over- or under-approximation of the truth, one can bound the complicated behavior enough to prove, for example, that the classification error decreases with more data.

Theorem 8.13 seems to show us that every function can be approximated arbitrarily well using polynomials. As useful as polynomials are, it turns out this is not entirely true. Let's say we're working with a function where the polynomial approximation does get progressively better at higher degrees. If you're in the proper mindset for calculus, you naturally ask what happens in the limit? If I call $p_{k}$ the degree $k$ Taylor polynomial for $f$ at $a=0$, how can we make sense of the expression

$$\lim_{k\to\infty}p_{k}(x)\ldots?$$

Remember, we only defined what it means for a sequence of numbers to converge, but this is a sequence of functions $\mathbb{R}\to\mathbb{R}$. Convergence of functions requires a definition of what it means for two functions to be "close" together, which has subtleties beyond the scope of this chapter.

But suppose we did that and we can make sense of this expression, we'd hope that this limit was also equal to $f$, at least when $x$ is sufficiently close to 0. This expression, the limit of Taylor polynomials, is called the Taylor series of $f$ at that point.

Mathematics is not so kind to us here. There are certain simple functions for which the Taylor series breaks down in certain regions. In particular, if $f(x) = \log (1 + x)$ and you compute the limit at $a = 0$, the resulting function would only be equal to $f(x)$ between $x = -1$ and $x = 1$. When $x > 1$ the sequence does not converge, even though $\log (1 + x)$ exists for $x > 1$.

In that case, you have to compute a different Taylor series at, say, $a = 2$. The complete function is then joined together piece-wise by enough Taylor series pieces until you get the whole function. The functions which can be reconstructed in this way (and aren't sensitive to which points you choose within a region, again in the interest of well-definition) are called analytic functions.

There are somewhat natural functions that fail to accommodate Taylor series worse than the logarithm. Let $f(x) = 2^{-1 / x^2}$ when $x \neq 0$, and let $f(0) = 0$. Figure 8.10 contains a plot of this function. You will prove in Exercise 8.11 that $f^{(n)}(0) = 0$ for every $n \in \mathbb{N}$.

As a consequence, all of its Taylor polynomials at $x = 0$ are the zero function, and the "limit function" should be the constant zero function. In this case, the Taylor series tells you nothing about the function except its value at $x = 0$. Polynomials aren't able to express what $f$ looks like near zero.

![Figure 8.10: A function $f(x) = 2^{-1 / x^2}$, all of whose derivatives are zero at $x = 0$.](05 - Calculus with One Variable_images/img-9.jpeg)

This highlights the shortcomings of Taylor polynomials. They're not the perfect tool for every job. It also leads us to ask why, for this mildly pathological $f$, the Taylor series fails so spectacularly. Complex analysis provides a satisfactory answer, but the subject is unfortunately beyond the scope of this book.

## Remainders

The Adolescent Taylor Theorem tells us how to compute the best polynomial of a given degree that approximates the behavior of a function. In fact, it approximates the behavior of a function's "slope" (first derivative) and more informally its curvature (higher derivatives), provided you're willing to compute enough terms.

The Adolescent Taylor Theorem, however, doesn't allow us to quantify how good the approximation is. As we just saw, there are pesky functions whose Taylor polynomials at certain rotten points are all zero. They're so flat they tricked the poor polynomial!

As you might have guessed, there is an Adult Taylor Theorem—just called the Taylor Theorem—which gets one much closer to quantifying the error of the Taylor polynomial. Unfortunately, the proof of this theorem requires the Mean Value Theorem, which does not fit in this book, but we can state the Taylor theorem easily enough.

###### Theorem 8.14 (The Taylor Theorem).

Let $d\in\mathbb{N}$ and $f$ be a $(d+1)$-times differentiable function. Let $p_{d}$ be the degree $d$ Taylor polynomial approximating $f$ at $a$, and let $x$ be an input to $f$. Then there exists some $z$ between $a$ and $x$ for which

$$f(x)=p_{d}(x)+\frac{f^{(d+1)}(z)}{(d+1)!}(x-a)^{d+1}$$

In words, the *exact* value of $f(x)$ can be computed from the Taylor polynomial $p_{d}(x)$ plus a remainder term involving a magical $z$ plugged into the $(d+1)$-st derivative instead of $x$.

The dependence of the variables on each other are a bit confusing. Let's make it explicit with some pseudocode. In particular, the needed value of $z$ depends on the specific input $x$.

```python
def exact_value(f, d, a, x):
    '''Return the exact value of f at x.

    Arguments:
    f: the function to evaluate
    d: the degree for the Taylor polynomial
    a: the input we can compute f at
    x: the input we'd like to compute f at
    '''
    p = taylor_polynomial(f, d, a)
    next_derivative = nth_derivative(f, n=d + 1)

    # note z depends on all of these!
    z = find_magical_z_value(f, d, a, x)

    remainder = (x - a)**(d + 1) * next_derivative(z) / factorial(d + 1)
    return p(x) + remainder
```

One important consequence of the remainder formula is that if $f^{(d+1)}$ is never large between $a$ and $x$, then $z$ is irrelevant. For the sake of concreteness, let's say that $f^{(3)}(z)<100$ between $a$ and $x$. Then $|f(x)-p_{2}(x)|$, the error in computing $f(x)$ from its Taylor polynomial at $a$, is bounded.

$$|f(x)-p_{2}(x)|<(100/6)(x-a)^{3}$$

In this case, if $x$ is within $0.1$ of $a$, then the error of the Taylor polynomial is only about $0.017$. Often this coarse $z$-be-damned bound is enough. This is the viewpoint of Newton's method, this chapter's application.

![Figure 8.11: A function whose root does not have a nice formula.](05 - Calculus with One Variable_images/img-10.jpeg)

## Application: Finding Roots

### The Problem and Binary Search

Let's say you have a function $f(x)$ and you want to find its zeros,[^2] that is, an input $r$ producing $f(r) = 0$. Let's also say that you can compute both $f(x)$ and $f'(x)$ at any given input. An example of such a function is $x^5 - x - 1$. Try to algebraically solve for $f(x) = 0$, if you dare. On the other hand, $f'(x) = 5x^4 - 1$ is simple enough to compute.

[^2]: Some authors say "roots" instead of "zeros." We use them interchangeably.

Figure 8.11 contains a plot of $f(x)$. The root is just under 1.2, but coming up with an algebraic formula for the root in terms of the coefficients is impossible in general (this is a deep theorem known as the Abel-Ruffini theorem).

One idea that should feel very natural by this point is to approximate the root of $f$ by starting with some value close to the root (which we can guess), and progressively improving it. In theory, we want to find a sequence $x_{1}, x_{2}, \ldots$, such that $\lim_{n \to \infty} x_{n} = r$, where $f(r) = 0$.

One initial thought is obvious: perform a binary search. That is, pick two guesses $c, d$, where $f(c) < 0 < f(d)$, and then let your improved guess be the midpoint $(c + d) / 2$, updating your upper and lower search bounds in the obvious way depending on whether $f((c + d) / 2) > 0$.

<!-- carousel -->
![Figure 8.12: An example of Newton's method outperforming a binary search. The tangent line at $d$ is better than the slow approach from $c$.](05 - Calculus with One Variable_images/img-11.jpeg)
![Figure 8.13: A generic illustration of Newton's method to get from $x_{n}$ to $x_{n+1}$.](05 - Calculus with One Variable_images/img-12.jpeg)
<!-- endcarousel -->

Binary search does produce a sequence approaching a root of $f$, but it turns out to be much slower than the forthcoming Newton's method. In Newton's method you choose your next guess $x_{n+1}$ depending on the derivative of $f$ at $x_n$. To convince you that this could be faster than binary search, suppose you chose bad bounds for binary search as in Figure 8.12.

The tangent line at the point $(d,f(d))$ intersects the $x$-axis quite close to the root, whereas the midpoint between $c$ and $d$ is rather far away. A binary search would slowly approach the root from the left, whereas the tangent line guides us close to the root in the first step.

### Deriving the Newton Update

If this isn't convincing enough, we can provide something much better: a proof. But first, we have to make the algorithm explicit. Phrased geometrically, start from some intermediary $x$-value guess, calling it $x_{n}$ for the $n$-th step in the algorithm.

Draw the tangent line at $x_{n}$, which is $y=f(x_{n})+f^{\prime}(x_{n})(x-x_{n})$, and let $x_{n+1}$ be the intersection of this line with the $x$-axis. This is illustrated in Figure 8.13. To find the intersection point, set $y=0$ in the equation for the tangent line, and solve for $x$:

$$
\begin{aligned}
0 &=f(x_{n})+f^{\prime}(x_{n})(x-x_{n}) \\
0 &=\frac{f(x_{n})}{f^{\prime}(x_{n})}+(x-x_{n}) \\
x &=x_{n}-\frac{f(x_{n})}{f^{\prime}(x_{n})}
\end{aligned}
$$

So set $x_{n+1}=x_{n}-\frac{f(x_{n})}{f^{\prime}(x_{n})}$, and from a given starting $x_{1}$, use this formula to define a sequence $x_{1},x_{2},\dots$. As a Python generator:

```python
def newton_sequence(f, f_derivative, starting_x):
    x = starting_x
    while True:
        yield x
        x -= f(x) / f_derivative(x)
```

Obviously, if $f^{\prime}(x_{n})=0$ then we're dividing by zero which is highly embarrassing. So let's assume $f^{\prime}(x_{n})\neq 0$, i.e., that the tangent line to $f$ is never horizontal, and we'll make this formal in a moment.

When Taylor's theorem is your hammer, the world is full of nails. It takes no inspiration to come up with this algorithm. As we'll see in the proof below, literally all you do is rearrange the degree 1 Taylor polynomial and squint at the remainder. Still, without going through the proof it's not entirely clear that Newton's method should outperform binary search, other than the fuzzy reasoning that an algorithm that *somehow* uses the derivative should do better than one that does not.

### Quadratic Convergence

Indeed, we'll wield a Taylor polynomial like a paring knife to prove Newton's method works. The theorem says that not only does $x_{n}$ converge to a root $r$ of $f$, but that if $x_{1}$ starts close enough, then in every step the number of correct digits roughly *doubles*. That is, the error in step $n+1$, which is $|x_{n+1}-r|$, is roughly the square of the error in step $n$, i.e. $|x_{n}-r|^{2}$. Binary search, on the other hand, improves by only a constant number of digits in each step.

This theorem we'll treat like a cumulative review of proof reading. That is, we'll be more terse than usual and it's your job to read it slowly, parse the individual bits, and generate tests if you don't understand part of it.

Let $f: \mathbb{R} \to \mathbb{R}$ be a function which is "nice enough" (it has some properties we'll explain after the proof). Let $r \in \mathbb{R}$ be a root of $f$ inside a known interval $c < r < d$, and pick a starting value $x_1$ in that interval. Define $x_2, x_3, \ldots$ using the formula $x_{n+1} = x_n - f(x_n) / f'(x_n)$. Call $e_k = |x_k - r|$ the error of $x_k$.

###### Theorem 8.15 (Convergence of Newton's Method).

For every $k \in \mathbb{N}$, the error $e_{k+1} \leq Ce_k^2$, where $C$ is a constant defined as

$$C = \max_{c \leq z, y \leq d} \frac{|f''(z)|}{2 |f'(y)|}.$$

In other words, the error of Newton's method vanishes quadratically fast in the number of steps of the algorithm.

###### Proof.

Fix step $k$. Compute the degree 1 Taylor polynomial for $f$ at $x_k$. This is exactly the tangent line to $f$ at $x_k$. Use that Taylor polynomial to approximate $f(r)$, the value of $f$ at the unknown root $r$.

$$f(r) = f(x_k) + f'(x_k)(r - x_k) + R$$

Here $R$ is the remainder from Theorem 8.14, and can be written as $R = \frac{1}{2} f''(z)(r - x_k)^2$ for some unknown $z$ between $r$ and $x_k$. Since $r$ is a root, $f(r) = 0$ and applying this we arrive at:

$$0 = f(x_k) + f'(x_k)(r - x_k) + \frac{1}{2} f''(z)(r - x_k)^2.$$

Recall we want to analyze the error of the approximation $e_{k+1} = |x_{k+1} - r|$, so at some point we must use the formula for $x_{k+1}$ in terms of $x_k$. The next three steps are purely algebraic rearrangements to enable this.

$$
\begin{aligned}
- f(x_k) - f'(x_k)(r - x_k) &= \tfrac{1}{2} f''(z)(r - x_k)^2 \\
\frac{f(x_k)}{f'(x_k)} + (r - x_k) &= -\frac{f''(z)}{2 f'(x_k)} (r - x_k)^2 \\
\left[ x_k - \frac{f(x_k)}{f'(x_k)} \right] - r &= \frac{f''(z)}{2 f'(x_k)} (r - x_k)^2
\end{aligned}
$$

The bracketed term is $x_{k+1}$, and so we get

$$e_{k+1} = |x_{k+1} - r| = \left| \frac{f''(z)}{2 f'(x_k)} (e_k)^2 \right|.$$

The fraction $\frac{|f''(z)|}{2 |f'(x_k)|}$ is at most $C$, as defined in the statement of the theorem.[^3] $\blacksquare$

[^3]: A tighter choice of $C$ is possible, where we set $z = y$, but it requires a more detailed proof and uses the Taylor polynomial in the same way as this proof.

Despite all the algebraic brouhaha in the proof above, all we did was take some value $x=x_{k}$ (though calling it $x_{k}$ was only relevant in hindsight), write down the degree 1 Taylor polynomial that approximates $f$ at $x$, and use that approximation to guess at the value of the unknown root $r$. We needed the notation and formalism to ensure that we weren't being tricked by our intuition, and to clearly outline the guarantees, and where those guarantees break down.

### When Newton's Method Fails

Speak of the devil! The proof allows us to identify the requirements of a "nice enough" function:

- $f^{\prime}(x)$ can never be zero between $c$ and $d$, except possibly at the root $r$ itself, in which case you can check to see if $f(x)=0$ at each step to avoid the edge case of hitting $r$ exactly. Otherwise we risk dividing by zero, or worse, getting stuck in a loop (as we'll see in the example below).
- $f$ has to have first and second derivatives everywhere between $c$ and $d$. Otherwise the claims in the proof that use those values are false.
- $f^{\prime}(x)$ should never be very close to zero, and $f^{\prime\prime}(x)$ should never be very far from zero, or else $C$ will be impractically large.

### Newton's Method in Practice

Using our `newton_sequence` generator from before, we can implement Newton's method for $f(x)=x^{5}-x-1$.

```python
THRESHOLD = 1e-12


def newton_sequence(f, f_derivative, starting_x, threshold=THRESHOLD):
    x = starting_x
    function_at_x = f(x)
    while abs(function_at_x) > threshold:
        yield x
        x -= function_at_x / f_derivative(x)
        function_at_x = f(x)


def f(x):
    return x**5 - x - 1


def f_derivative(x):
    return 5 * x**4 - 1


starting_x = 1
for i, x in enumerate(newton_sequence(f, f_derivative, starting_x)):
    print((x, f(x)))
    if i == 100:
        break
```

After only six iterations we have reached the limit of the display precision.

```txt
(1, -1)
(1.25, 0.8017578125)
(1.1784593935169048, 0.09440284131467558)
(1.16753738939611, 0.001934298548380342)
(1.1673040828230083, 8.661229708994966e-07)
(1.1673039782614396, 1.7341683644644945e-13)
```

The headline claim of Theorem 8.15 is that the error roughly *squares* each step, so the count of correct digits doubles. We can watch this directly: compute a high-precision root with sympy, run Newton from $x_1=1$, and print the error $e_n$ alongside the ratio $e_n / e_{n-1}^2$. That ratio stays bounded (it does not blow up), which is exactly quadratic convergence — and the iterates reproduce the book's table line for line.

```python
<!-- include: code/pim/05 - Calculus with One Variable/05_newton_quadratic.py -->
```

### A Bad Starting Point

![Figure 8.14: An example where the starting point of Newton's method fails to converge due to an unexpected loop.](05 - Calculus with One Variable_images/img-13.jpeg)

Let's see the same experiment with the `starting_x` changed to 0 instead of 1. This is an input which, as you can see from Figure 8.14, drives Newton's method in the wrong direction! By the end of a hundred iterations, Newton's method cycles between three points:

```txt
(0.08335709970125815, -1.083353075191566)
(-1.0002575619492795, -1.001030911349579)
(-0.7503218281592572, -0.4874924386834848)
```

This behavior is allowed by Theorem 8.15, because in between the starting point and the true root, the derivative $f'(x)$ is zero, making the error bound $C$ from Theorem 8.15 undefined (and indeed, unboundedly large for $x$ values close to where $f'(x)$ is zero). Newton's method is very powerful, but take care to choose a wise starting point.

The demo below runs both starts side by side: from $x_1=1$ it converges to the root in a handful of steps, while from $x_1=0$ it never lands on a root — its tail revisits only a small set of values, the three-point cycle the book describes.

```python
<!-- include: code/pim/05 - Calculus with One Variable/06_newton_failure_loop.py -->
```

### Beyond Newton: Higher-Degree Generalizations

Newton's method stirs up a mathematical hankering: why stop at the degree 1 Taylor polynomial? Why not degree 2 or higher? All we did to "derive" Newton's method was take a random point, write down the degree 1 Taylor polynomial $p(x)$, and solve $p(x)=0$. By rearranging to isolate the error terms, we got the formula for $x_{k+1}$ for free. For degree 2, why not simply use the degree 2 Taylor polynomial instead?

$$0=f(x_{k})+f^{\prime}(x_{k})(x-x_{k})+\frac{1}{2!}f^{\prime\prime}(x_{k})(x-x_{k})^{2}$$

There are two obstacles: (a) this polynomial might not even hit the $x$ axis; it's trickier to nail down for quadratics than lines, and (b) even if it does, it might be hard to find the intersection, since finding roots is the problem we started with!

Admittedly, finding the root of a degree 2 polynomial isn't so hard (there's a formula with a sing-a-long mnemonic), but if you take this idea up to degree 3, 4, or higher, the formula approach eventually breaks down. For degree 5, the polynomial we want to approximate a root for is the Taylor polynomial, and we don't know how to find its roots.

Nevertheless, there is a technique called Householder's method that generalizes Newton's method to higher degree Taylor polynomials. Higher degrees unlock order-of-magnitude better convergence.

The tradeoff, as expected, is that it takes progressively more work to compute each step in the update (and existence and good behavior of higher derivatives). Moreover, there are additional requirements at each step on the suitability of a starting point to guarantee convergence. You will explore this in an exercise.

## Cultural Review

- Good definitions are designed to match a visual intuition while withstanding (or excluding) pathological counterexamples.
- Much of the murkiness of calculus comes from the fact that it must support a long history of manual calculations and pathological counterexamples. The "normal" case is usually easier to understand.
- A concept is well-defined if it doesn't depend on choices that are supposed to be arbitrary. E.g., the limit of a function as the input approaches a point must not depend on which sequence you choose to approach that point.
- The Taylor polynomial is a mathematical hammer, and math is full of nails.

## Exercises

### Limits and Continuity

**8.1.** Write down examples for the following definitions.

1. A sequence $x_{1},x_{2},\dots$ is said to diverge, written $\lim_{x\to\infty}x_{n}=\pm\infty$, if for every $M>0$, there is a $k\in\mathbb{N}$ so that if $n>k$, then $|x_{n}|>M$. Note that $\infty$ is not being used as a number, but rather notation for the concept, "$x_{n}$ grows in magnitude without bound." This unifies it with the usual limit definition.
2. A function $f$ is said to diverge at $a$, written $\lim_{x\to a}f(x)=\pm\infty$, if whenever $x_{n}\to a$ then $f(x_{n})$ diverges.
3. A function $f:\mathbb{R}\to\mathbb{R}$ is called concave up at $a$ if the second derivative $f^{\prime\prime}(x)$ is positive at $x=a$. Likewise, if $f^{\prime\prime}(a)<0$, $f$ is called concave down at $a$. How does the numerical property of being concave up/down relate to the geometric shape of a curve?
4. A function $f:\mathbb{R}\to\mathbb{R}$ is called continuous at $a$ if for every $\varepsilon>0$, there is a $\delta>0$ such that whenever $|x-a|<\delta$, then $|f(x)-f(a)|<\varepsilon$. A function is called continuous if it is continuous at all inputs. Most functions in this book are continuous. Find an example function defined in this chapter which is not continuous according to this definition.

**8.2.** Prove the following basic facts using the definitions from Exercise 8.1.

1. Prove Theorem 8.9 that the map $f\mapsto f^{\prime}$ is linear.
2. Using the definition of the limit of a function, prove that

$$\lim_{x\to a}[f(x)g(x)]=\left(\lim_{x\to a}f(x)\right)\left(\lim_{x\to a}g(x)\right),$$

provided both of the limits on the right hand side exist.
3. Prove that $a_{n}=\frac{2^{\sqrt{n}}}{n^{10}}$ diverges as $n\to\infty$.
4. Prove that a function $f(x)$ which is differentiable at $a$ is also continuous at $a$.
5. Let $x_{n}$ be a sequence of real numbers.

Suppose that for every $\varepsilon>0$, there is an $N\in\mathbb{N}$ (depending on $\varepsilon$), such that for every $n, m>N$ it holds that $|x_{n}-x_{m}|<\varepsilon$. Such a sequence is called a Cauchy sequence. Look up the statement of the Bolzano-Weierstrass theorem and use it to prove that every Cauchy sequence converges.

**8.3.** Prove that the numeric value for the slope of a line doesn't depend on the choice of points.

**8.4.** Prove that the limit of a sequence, if it exists, is unique. In other words, the limit $L$ does not change depending on the choices of $\varepsilon$ and $k$ used to satisfy the definition. This justifies us calling it "the" limit of a sequence. Hint: Suppose you had an $L$ and an $L^{\prime}$ that both worked, and prove that $L=L^{\prime}$.

### Taylor Series and Approximation

**8.5.** Compute the Taylor series for $f(x)=1/x$ at $x=1$.

**8.6.** Compute the Taylor series for $f(x)=e^{-2x}$, and compare this to the procedure of plugging in $z=-2x$ into the Taylor series for $e^{z}$. Find an explanation of why this works.

**8.7.** Compute the Taylor series for $f(x)=\sqrt{1+x^{2}}$ at $x=0$. We will use this in Chapter 12 to simplify a model for a physical system.

**8.8.** Let $N\in\mathbb{N}$ and $0\leq P\in\mathbb{R}$ be constants. Compute the linear (degree-1) Taylor approximation for $C(r)=\frac{Pr(1+r)^{N}}{(1+r)^{N}-1}$ at $r=0$. This formula computes the monthly interest payment on a loan with compounding monthly interest rate $r$, total number of months $N$, and principal $P$.

In the December 1996 issue of Mathematics Magazine, Peyman Milanfar described a slightly modified version of the linear Taylor approximation, $C^{*}(r)\approx\frac{1}{N}(P+\frac{1}{2}PNr)$, which has been used by Persian merchants for hundreds of years to compute monthly loan payments in their heads. Compare $C^{*}(r)$ with the exact degree-1 Taylor polynomial for $C(r)$. What is the error of the Persian method? Under what conditions on $N$ and $P$ is the Persian method accurate?

**8.9.** There are some functions which are challenging to compute limits for, but they aren't considered "pathological." One particularly famous function is

$$f(x)=x\sin(1/x).$$

Compute the limit for this function as $x\to 0$. The difficulty is that $\sin(1/x)$ is not defined at $x=0$, and algebra doesn't provide a way to simplify $\sin(1/x)$. Instead, you have to use "common sense" reasoning about the sine function. This common-sense reasoning is made rigorous by the so-called Squeeze Theorem. Look it up after trying this problem. A plot of $f$ will help.

**8.10.** Find a differentiable function $f:\mathbb{R}\to\mathbb{R}$ with the property that $\lim_{x\to\infty}f(x)=0$, but $\lim_{x\to\infty}f^{\prime}(x)$ does not exist.

**8.11.** Let $f(x)$ be defined as

$$f(x)=\begin{cases}2^{-1/x^{2}}&\text{if }x\neq 0\\0&\text{if }x=0\end{cases}$$

This function has derivatives of all orders at $x=0$, and despite the fact that $f(x)$ is not flat, all of its derivatives are zero at $x=0$. Prove this or look up a proof, as the computation is quite involved. These functions are sometimes called flat functions, since they're literally so flat that they avoid detection of any curvature by derivatives.

**8.12.** There are two definitions of the number $e$. One is the number used as an exponent base in the exponential function $e^{x}$, for which the derivative of $e^{x}$ is $e^{x}$. The other is $e=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^{n}$. First, prove the somewhat surprising fact that this limit is not equal to 1. Second, understand why these two definitions result in the same quantity.

**8.13.** Find the maximum of $f(x)=x^{1/x}$ for $x\geq 0$. One method: use an approximation given by the early terms of the Taylor series of $e^{x}$. Another: maximize the logarithm of $f$, which has the same maximizing input.

### Derivatives and Root-Finding

**8.14.** Look up a proof of the chain rule on the internet, and try to understand it. Note that there are many proofs, so if you can't understand one try to find another. Come up with a good geometric interpretation.

**8.15.** Write a program that implements the binary search root-finding algorithm and compare its empirical convergence to Newton's method. Find an example input for which (gasp!) they have the same convergence rate, and analyze the statement of Theorem 8.15 to determine why this is possible.

**8.16.** Look up a proof of the Taylor theorem, which may depend on other theorems in single-variable calculus like Rolle's theorem or the Intermediate Value Theorem.

**8.17.** Look up an exposition of the degree-2 Householder method for finding roots of differentiable functions, and implement it in code.

**8.18.** In the chapter I mentioned that parts of calculus and real analysis are formalized in such a way that maintains backwards compatibility with "legacy math." The experienced programmer might protest: why not redesign analysis from scratch to avoid that? This has been done, and the field of nonstandard analysis is one such redesign. Look up an introductory exposition about nonstandard analysis and identify where it becomes backwards incompatible with standard calculus.
