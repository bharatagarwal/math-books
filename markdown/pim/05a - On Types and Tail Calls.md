# On Types and Tail Calls

> By relieving the brain of all unnecessary work, a good notation sets it free to concentrate on more advanced problems, and in effect increases the mental power of the race.
>
> – Alfred Whitehead

There are two topics I want to discuss in this chapter that don't fit elsewhere in the progression of the book. First, on how the organizational structure of a proof can guide the reader's attention. Second, on equivalence relations and quotients, the standard abstraction for building and representing complicated mathematical spaces. Both are new ways to reduce reader's cognitive burden by hiding technicalities. The latter will also prepare us for the use of equivalence relations through the rest of the book.

## Tail Call Optimization for Proofs

In Chapter 8 we worked entirely with functions whose type signature was $\mathbb{R}\to\mathbb{R}$. Although we only intuitively understood the formal notion of 'continuity'—the fact that the graphs of these functions formed contiguous curves when plotted—we concentrated intently on the interplay between the algebra (computing limits, derivatives, and using Taylor series) and geometry (the intrinsic qualitative shapes of curves). There is much more to be said for single-variable calculus. One of the most common uses of calculus is to tune parameters of some process. For example, a car manufacturer tunes how many of each car model to manufacture based on their costs and sales figures. Another example is an algorithm that fails with some measurable probability—or whose output quality degrades—depending on a tunable parameter.

The recipe for doing this is taught in most undergraduate calculus courses. It reduces the optimal parameter choice from a continuum of options to a discrete set to check by hand. Define $f:\mathbb{R}\to\mathbb{R}$ whose input is the parameter of interest, and whose output you'd like to minimize (maximizing is analogous).

- Select a range of interest$^1$ $a\leq x\leq b$.
- Compute the values $a\leq x\leq b$ for which $f^{\prime}(x)=0$ or $f^{\prime}(x)$ is undefined. These are called critical points.
- The optimal parameter $x$ is the minimum value of $f(x)$ where $x$ is among the critical points, or $x=a$ or $x=b$.

The analysis of an algorithm using the above recipe is so routine that authors seldom remark on it. In research papers they often skip the entire argument assuming the reader will recognize it. Life is similar for the ubiquitous Taylor polynomial. Such brevity can seem like malicious obfuscation, but it makes sense as a cognitive "tail call optimization" for proofs.$^2$

The core of the proof is the primary focus. It requires all your working memory. Optimizing a parameter using standard tools is easy once you've done it enough times. Leaving it to the end compartmentalizes the two jobs. Big picture comprehension first, and rote computation last. Indeed, the ability to maximize an elementary function rarely depends on memory of how you created that function, so why not shed a few mental stack frames while you do the real work?

## Guiding Attention with Theorem Structure

This is also a justification for why one might write the statement of a theorem like we did in the last chapter.

###### Theorem (Convergence of Netwon's Method).

For every $k\in\mathbb{N}$, the error $e_{k+1}\leq Ce_{k}^{2}$, where $C$ is a constant defined as

$$C=\max_{c\leq z,y\leq d}\frac{|f^{\prime\prime}(z)|}{2|f^{\prime}(y)|}$$

The value of $C$, while it needs to be defined somewhere, is not crucially important to the first-glance understanding of the statement of the theorem. The big picture is that the error vanishes quadratically as opposed to linearly. The coefficient itself can be defined afterwards to emphasize the separation of concerns between the quadratic error rate and the exact data guiding the error. In Chapter 5, we emphasized how overloading notation with context can help reduce cognitive overload. Here the organizational structure of the formula contributes. It guides the reader's focus by placing the interesting part first.

## Equivalence Relations and Quotients

Now let's move on to discuss two technical tools for making complicated types (realized as sets): equivalence relations and quotients.

Since quotients are often formed from set products, let's briefly review. The direct product of sets, $A\times B$, is the most common mathematical way to make a compound data type. It's the set $\{(a,b):a\in A,b\in B\}$. To reiterate from Chapter 4, if we repeat this operation, we tend to ignore the nested grouping of tuples, so that $A\times B\times C$ is viewed as a tuple of length $3$. Likewise, given a set $A$, we denote by $A^{n}$ the tuples of length $n$ for some fixed $n\in\mathbb{N}$. Quotients provide a way to make our "ignoring" rigorous.

Quotients are usually defined in terms of an *equivalence relation*, which generalizes the concept of equality. Given a set $A$, an equivalence relation on $A$ is a function $f:A\times A\to\{0,1\}$ (where $\{0,1\}$ are thought of as booleans) with the following three properties:

1. Reflexivity: $f(a,a)=1$ for all $a\in A$.
2. Symmetry: $f(a,b)=f(b,a)$ for all $(a,b)\in A\times A$.
3. Transitivity: for all $a,b,c\in A$, if $f(a,b)=1$ and $f(b,c)=1$, then $f(a,c)=1$.

In your mind you can replace $f(a,b)=1$ with "$a$ and $b$ are equivalent." A more common notation for this is a squiggle $\sim$, so that $a\sim b$ if and only if $f(a,b)=1$, with $a\not\sim b$ if $f(a,b)=0$. The squiggle reminds one of the equal sign without asserting that it's an equivalence relation before it's proved to be.

To define an equivalence relation is to say, "Here are the terms by which I want to think of different things as the same." We are essentially overloading equality with a specific implementation. As long as the equivalence relation satisfies these three properties, you rest assured it has the most important properties of the equality operator.

### Equivalence Classes and Partitions

Let's do a simple example with $\mathbb{R}$. Let $a\sim b$ if $a-b\in\mathbb{Z}$, and $a\not\sim b$ otherwise. Check that this indeed satisfies the three properties of an equivalence relation. This equivalence relation declares that $-1/2,1/2,3/2,5/2$ are all equivalent, as are $-2,-1,0,1,2$. But $1/2$ is not equivalent to $1$. We call the set of all things equivalent to one object an *equivalence class*. So in this case $\mathbb{Z}$ is an equivalence class, as is the set of half-fractions $\{\ldots,-3/2,-1/2,1/2,3/2,\ldots\}$. An exercise to the reader: show that given a set $X$ and an equivalence relation $\sim$, the equivalence classes partition $X$ into disjoint subsets—i.e., every $x\in X$ is in exactly one equivalence class. No two classes may overlap. For this reason, an equivalence relation is also called a *partition*.

## Quotients: Enforcing Equivalence as Equality

An equivalence relation allows us to do math in a world (on a set) in which an equivalence relation is enforced as equality. This world is the quotient.

###### Definition 9.1.

Let $X$ be a set and $\sim$ an equivalence relation on $X$. The *quotient* of $X$ by $\sim$, denoted $X/\sim$ is the set of equivalence classes of $\sim$ in $X$.

Back to our example with $\mathbb{R}$, the quotient $\mathbb{R}/\sim$ has a simpler representation. Since equivalence classes partition $\mathbb{R}$, and every real number shows up in some equivalence class, we can identify each equivalence class in $\mathbb{R}/\sim$ with our favorite "representative" from that class.

Concretely, let's choose the representative from each class in $\mathbb{R}/\sim$ that's between 0 and 1. For the equivalence class $\{\ldots,-2/3,1/3,4/3,7/3,\ldots\}$, we choose $1/3$ as the representative. One abbreviates the equivalence class represented by a particular element (say, $1/3$) using the notation $[1/3]$, so that $[1/3]=[-2/3]=[7/3]$ are all the same equivalence class. Noting that $[0]=[1]$, we can summarize:

$$
\mathbb{R}/\sim = \{[x] : 0 \leq x < 1\}.
$$

Curious plants spring from fertile soil. In this world $[1+1]=[0]$, and a sequence which diverges in $\mathbb{R}$ converges here: $x_{n}=\left[\frac{2n+1}{2}+\frac{1}{n}\right]$.

## The Circle as a Quotient of the Reals

$\mathbb{R}/\sim$ inherits operations from $\mathbb{R}$, as if $\mathbb{R}/\sim$ were a wrapper class encapsulating $\mathbb{R}$. Define $[x]+[y]$ to be $[x+y]$ for any representatives $x,y$. We must prove this definition is well-defined, i.e., that any chosen representatives result in the same operation. We need to show that if $x\sim x'$ and $y\sim y'$, then $x+y\sim x'+y'$. Indeed, $(x+y)-(x'+y')$ is an integer because $(x-x')$ and $(y-y')$ both are. Note you cannot say the same of multiplication (find a counterexample!).

We can also think of $\mathbb{R}/\sim$ geometrically. Imagine standing at 0 on $\mathbb{R}$ and walking in the positive direction, say, following a sequence $x_{n}=0.001n$. On $\mathbb{R}$ you increase unboundedly. When we pass to the quotient, you cycle every thousand steps. This is an animated way to see that $\mathbb{R}/\sim$ is geometrically a circle. In fact, we can design a nice bijection that makes this formal. Call $C=\{(\cos(\theta),\sin(\theta)):0\leq\theta<2\pi\}$. Define $f:\mathbb{R}/\sim\to C$ by $f([t])=(\cos(2\pi t),\sin(2\pi t))$. Prove that $f$ is well-defined (doesn't depend on the choice of which member of $[t]$ you choose), and a bijection.

This example generalizes nicely. Given a surjective function $f:X\to Y$, define $\sim_f$ so that $a\sim_f b$ if and only if $f(a)=f(b)$. Show that this is always an equivalence relation, and notice that you get a new function $f:X/\sim_f\to Y$ defined by $f([x])=f(x)$ that is guaranteed to be a bijection when $f$ is a surjection (and an injection otherwise). Describing an equivalence relation in terms of a function has an advantage: the structure of the function $f$ can be used to "move" properties between one space and the other. In the case of $\mathbb{R}/\sim$ and the circle $C$, since $f$ is differentiable,$^4$ functions defined on the circle can be converted to functions on $\mathbb{R}/\sim$ with most properties intact. This is how we can ultimately say that $\mathbb{R}/\sim$ has the "same geometry" as $C$, though to do this in general—connect two generic spaces in which one can make geometric statements—requires extensive groundwork beyond the scope of this book. You'll know you're treading in these waters if you hear the term "manifold" or "topology."

Nevertheless, equivalence relations will be meaningful even in less technical settings, such as vector spaces (Chapter 10) and groups (Chapter 16). There the structure of the function defining the relevant equivalence relations are *algebraic* in nature. This is all to explain the primary tool mathematicians use to assert that they want to consider two different things to be the same in a principled manner. You override equality, show it meets standards of decency, and then introduce it to your friends.

## Associativity of Products and Modular Arithmetic

We can now make the "ignoring" of nested pairs in the set product rigorous. Define the sets

1. $L=(A\times B)\times C=\left\{\left((a,b),c\right):a\in A,b\in B,c\in C\right\}$ (left grouping)
2. $R=A\times(B\times C)=\left\{\left(a,(b,c)\right):a\in A,b\in B,c\in C\right\}$ (right grouping)
3. $Z=\left\{\left(a,b,c\right):a\in A,b\in B,c\in C\right\}$ (no grouping)

Now define an equivalence relation on $L\cup R$ so that $(a,(b,c))\sim\left((a^{\prime},b^{\prime}),c^{\prime}\right)$ if and only if $a=a^{\prime},b=b^{\prime},c=c^{\prime}$. The resulting quotient $(L\cup R)/\sim$ is in bijective correspondence with $Z$.

### Modular Arithmetic as a Quotient

Another useful example is when working with modular arithmetic. Working in $\mathbb{Z}$, define $a\sim_{n}b$ if, to use programming syntax, `a % n == b % n`. Equivalently, $a\sim_{n}b$ if and only if $a-b$ is a multiple of $n$. The quotient space for this equivalence relation is called $\mathbb{Z}/n\mathbb{Z}$ (where $n\mathbb{Z}$ is a shorthand for multiples of $n$; we'll revisit this in Chapter 16). The equivalence relation $\equiv$ for modular arithmetic is usually denoted with an operator paired with "mod $n$," as in $a\equiv b\mod n$.

Arithmetic modulo $n$ shares most properties with normal arithmetic on integers, which makes it extremely convenient. For example, a complex expression like $8^{3000}$ is extremely simple mod $9$. From $8\equiv-1\mod 9$, you get $8^{3000}\equiv(-1)^{3000}\equiv\left((-1)^{2}\right)^{1500}\equiv 1\mod 9$. This tells you that $8^{3000}$ is one plus a multiple of $9$. Similar tricks with conveniently chosen moduli can extract useful information about $8^{3000}$ without computing it exactly, such as the last few digits of the number in base 10. Another useful tool when studying equations of integer variables is to recognize that if an equation has a solution, then the same solution must exist if the equation is considered mod $n$ for any $n$.

Equivalence relations and quotients reduce the burden of ignoring irrelevant differences on a domain of study. You establish once that there's an equivalence relation, and you prove the important operations are well-defined on equivalence classes. Then you can safely suppress the type difference between $[x]$ and $x$ forever. In fact, after defining a quotient and proving its well-definition, mathematicians immediately drop the brackets. You can also freely choose the most advantageous equivalence class representative for your task, possibly easing computation. It's similar to the programmer's adage: work hard now to allow yourself to be lazy later. Mathematicians are well practiced in that philosophy.

---

$^1$ If you don't want to restrict to a range, you have to worry about the limiting behavior of $f$ as the input tends to $\pm\infty$. When $f$ blows up to $\infty$ or $-\infty$, these are sort of "trivial" optima, as well as being unattainable by a fixed input. But if, for example, you can compute that both infinite limits are $-\infty$, then that leaves open the possibility of a finite global maximum.

$^2$ For unfamiliar readers, tail call optimization is a feature of certain programming languages whereby a function whose last operation is a recursive call can actually shed its stack frame. It doesn't need it because there is no work left after the recursive call but to return. In this way, functions written in tail-call style will never cause a stack overflow.

$^4$ We'll see more about what it means for a function with multiple inputs and outputs to have a derivative in Chapter 14, but in this case it just means each component of the output is differentiable as a single-variable function of the input.
