# Linear Algebra

> There is hardly any theory which is more elementary [than linear algebra], in spite of the fact that generations of professors and textbook writers have obscured its simplicity by preposterous calculations with matrices.
>
> – Jean Dieudonné

### From Sets to Functions

For a long time mathematicians focused on studying interesting sets, like numbers and solutions to various equations. In Chapter 6 we saw graphs, which are interesting kinds of sets. In Chapter 8 we saw sets of numbers (sequences) and sets of pairs of numbers (functions $\mathbb{R}\to\mathbb{R}$). One could spend a lifetime studying interesting graphs or interesting sets of numbers. However, more recent trends in mathematics have shifted the main focus from studying sets with interesting structure to studying *functions* with interesting structure.

To ease into it, let's first consider the familiar concept of a compiler. A compiler is a function mapping the set of programs in a source language to the set of programs in a target language, often assembly. A compiler preserves the semantic behavior of a valid input program in the target language when you run it. In that sense, it preserves the structure of the input by representing that structure appropriately in the codomain.

Moreover, a computer program written in a compiled language like C is truly only defined by the behavior of the compiler. This is never more visible than when dealing with language forms that have "undefined behavior." Different compilers run on the same source produce programs that behave differently. Languages like C, in which behavior can vary depending on the arbitrary contents of uninitialized memory, widen such pitfalls. This isn't how we *want* to work with programs. We want to consider programs in their most natural environment, the semantics defined by a language's documentation.

In mathematics, when complexity and notational grime builds up we use essentially the same tool: abstraction. We add a layer of indirection that allows us to write arguments that say, "these two things are the same" in the context that matters for the task at hand, and we exhibit bijections and equivalence relations to formalize the connection (cf. Chapter 9). This allows us to identify and isolate structure in new settings, and mentally disregard impertinent information.

### What This Chapter Covers

The vector space, which encompasses mathematical objects with a linear structure, is a foundational example. It's the basic object of study in linear algebra. The main tool that we use to relate two vector spaces is the linear map. As we will see, linear maps have a useful computational representation called matrices (singular, matrix). Matrices are "compiled" representations of a linear map in a particular environment (looking ahead, the particular choice of a basis for the vector space). The magic appears when we deeply understand how the operations on matrices translate back and forth to operations on linear maps, and how it all relates to geometry.

Linear algebra is obscenely practical. The application we'll see in this chapter, singular value decomposition (SVD), is a staple of data science and machine learning. But linear algebra seems to seep into all applied mathematics, most simply because linear approximations are easy to compute. When faced with a challenging phenomenon, the first step is to try a linear model and see how well it does. Many more complex techniques also end up "linearizing" a non-linear thing behind the scenes so as to apply linear algebraic tools.

We devote a fair chunk of this chapter's application to studying a specific linear model for movie ratings and text documents, using SVD to cluster the latter. An additional goal of this chapter is to prepare us for multivariable calculus and optimization. These subjects use vectors, vector spaces, and linear maps as primitive types.

## Linear Maps and Vector Spaces

### The Intuition Behind Linearity

The definition of a linear map requires a bit of groundwork to nail down precisely, but the crucial underlying intuition is simple. A function $f:A\rightarrow B$ is called linear if the following identity is always true, no matter what $x,y\in A$ are:

$$f(x+y)=f(x)+f(y)$$

Simple, yet something is missing. Take a moment to identify what that is.

The problem is that we don't know what "$+$" means in this context. Because I used the $+$ symbol you may have guessed that $A$ and $B$ are sets of numbers, but this need not be the case. Instead, we'll isolate the important properties of addition, and the result will be called a vector space. Any set can be a vector space, and we call the elements of a vector space vectors. One defines a $+$ operation and establishes that the isolated addition properties hold.

### The Vector Space Axioms

Now we can define a vector space. The gist is that vectors can be any type, scalars must be nicely-behaved numbers, and almost every arithmetic identity you expect to be true is true, so long as you formally prove the axioms according to this definition. The only missing thing is that vector spaces don't have multiplication or division of vectors by other vectors. Moreover, the concepts defined here, particularly the zero vector and additive inverses, can be proven to be unique from the definition. You will do this in the exercises, and it justifies the use of the notation post hoc.

**Definition 10.1.** A set $V$ is called a vector space over $\mathbb{R}$ if it has two operations $+$ and $\cdot$ with the following properties:

1. $+:V\times V\to V$ is a function on pairs of vectors and $\cdot:\mathbb{R}\times V\to V$ is a function mapping a real number and a vector to a vector. Often the values in $\mathbb{R}$ are called scalars, and using the operation $\cdot$ is called scaling. Rather than denoting the operation by the prefix notation $+(x,y)$ and $\cdot(a,v)$, we'll use the infix notation $x+y$ and $a\cdot v$.
2. Every $v\in V$ has an additive inverse, i.e., a vector $w$ for which $v+w=0$. This special vector is denoted $-v$, and is used in conjunction with $+$ to perform subtraction: $u-v=u+(-v)$.
3. There is a distinguished, unique vector denoted $0$ in $V$.
4. $+$ obeys the following identities for every $u,v,w\in V$:
   1. $v+w=w+v$
   2. $(u+v)+w=u+(v+w)$
   3. $0+u=u+0=u$
   4. $u+(-u)=(-u)+u=0$
5. $\cdot$ obeys the following identities for every $v\in V$ and every $a,b\in\mathbb{R}$:
   1. $0\cdot v=\mathbf{0}$. Here $\mathbf{0}$ denotes the zero vector to help with disambiguation.
   2. $1\cdot v=v$
   3. $a\cdot(b\cdot v)=(ab)\cdot v$
6. $+$ and $\cdot$ distribute with each other, i.e., $a\cdot(v+w)=a\cdot v+a\cdot w$, and $(a+b)\cdot v=a\cdot v+b\cdot v$.

As a logical consequence of these properties, all usual algebraic operations involving $+$ and $\cdot$ that you'd expect are valid are indeed valid. These properties are the minimum set of requirements to force the needed arithmetic to work.

Another word commonly used here is that $V$ is closed under this operation: applying $+$ to vectors in $V$ stays in $V$. We ensure this by stating the codomain of $+$ is $V$, but it is a more stringent requirement if the vector space is built from a subset of some well-known set. We call it "scaling" to picture this operation as "stretching" or "shrinking" the vector by a factor given by the scalar quantity. One can also "scale" negatively, which is a reflection. Some authors write all vectors bold, but I will only do it when disambiguation is needed. More often than not the choice of letters suffices, $u,v,w,x,y,z$ for vectors and $a,b,c$ or Greek letters for scalars.

This is a monumental definition, and it's not even the most general definition (see the Chapter Notes for more). But it's entirely contained in the implementation of the operations $+$ and $\cdot$. The miniature proofs that $+,\cdot$ have the needed properties constitute a proof that the chosen implementation is a vector space. This proof is rarely a challenge. In the examples that follow, I'll skip detailed proofs, but if you want more practice, fill in the details.

### Examples of Vector Spaces

The simplest natural vector space is $\mathbb{R}$, with $\mathbb{R}$ also being the scalars. In this case vectors are just numbers, $+$ is addition of real numbers, and $\cdot$ is multiplication of real numbers. The number zero is both the scalar identity and the zero vector. Nothing about this should be surprising.

A more interesting example is one we're familiar with from Chapter 2, polynomials. Call $V$ the set of all polynomials of a single variable. If $t$ is our variable then $1+t\in V$ as well as $7$ (a degree-zero polynomial) and $\pi t+700t^{99}$. The operation $+$ is defined by adding coefficients term-wise, and $c\cdot p(t)$ by scaling each coefficient of $p$ by $c$. The zero polynomial is the zero vector. As an aside, the secret sharing application from Chapter 2 can also be understood and proved by appealing to polynomials as a vector space; the evaluation-at-a-point function $\operatorname{eval}_{a}(p)$ defined by $p\mapsto p(a)$ is a linear map. See the exercises for an exploration of this.

Even more general is the vector space of *all* functions $f:X\to\mathbb{R}$ for any set $X$. As an exercise to the reader: go through the conditions from Definition 10.1 and figure out what $+$ and $\cdot$ could mean. There should only be one natural option. As a specific example, the space of all *differentiable* functions $f:\mathbb{R}\to\mathbb{R}$ is a vector space, and the derivative operation $f\mapsto f^{\prime}$ is a linear map from that space to the space of all functions.

The final example is $\mathbb{R}^{n}=\mathbb{R}\times\mathbb{R}\times\cdots\times\mathbb{R}$, the set of all tuples of length $n$ of real numbers. The elements of $\mathbb{R}^{n}$ are *vectors* in the sense the reader is probably used to. A vector is just a tuple of numbers. The operation $+$ on tuples is entry-wise addition. This means

$$(a_{1},a_{2},\ldots,a_{n})+(b_{1},b_{2},\ldots,b_{n})=(a_{1}+b_{1},\ldots,a_{n}+b_{n}).$$

Similarly, $c\cdot(a_{1},\ldots,a_{n})=(ca_{1},\ldots,ca_{n})$, where on the right hand side the multiplication happening in each coordinate is the usual product of real numbers. The zero vector is $(0,0,\ldots,0)$, and the inverse of $(a_{1},\ldots,a_{n})$ is $-1\cdot(a_{1},\ldots,a_{n})=(-a_{1},\ldots,-a_{n})$. All of the vector space axioms hold because they apply independently to each entry, and each entry is just arithmetic in $\mathbb{R}$.

### Geometric Interpretation of Vectors

With a few examples handy, let's turn to the geometric side of Definition 10.1. A vector space is designed to be the simplest way to define what addition means in a context that is useful for geometry (defining an "algebra" for geometric objects). Let's expand this. The first thing a geometry needs is a space of points. In a vector space, the points are the vectors themselves. In Figure 10.1, we draw some vectors in $\mathbb{R}^{2}$ for the ease of visualization. For a reason we'll explain shortly, we also draw these points as arrows from the zero vector (the zero vector is called the "origin," in graphical parlance).

![Figure 10.1: Examples of vectors drawn as arrows from the origin in $\mathbb{R}^2$.](06 - Linear Algebra_images/img-0.jpeg)

The "position" of a point specified by such an arrow is at the non-origin end of the drawn line segment. This choice of drawing from the origin also implies that every vector has a direction. We can add two vectors by adding their coordinates. Geometrically this involves moving the tail of one arrow to the head of the other and drawing an arrow from the origin to the end of the resulting path. In Figure 10.2, we can add the two solid vectors to get the dashed vector. The transparent dotted vector shows this geometric motion of "moving the tail to the head."

Second, a geometry needs lines. In a vector space, a line is the set of all ways to scale a single nonzero vector. In symbols, a line through the origin and $v$ is the set $L_{v} = \{c\cdot v : c\in \mathbb{R}\}$. For example, drawn in Figure 10.3 you can scale $v = (1,2)$ by a factor of 2 to get $(2,4)$, shrink it down to $(0.5,1)$, or scale it negatively to $(-2,-4)$. The set of all possible ways to do this gives you all the points on the line through $(1,2)$.

You can further get a line not passing through the origin by taking some other vector $w$ and adding it to every point on the line, i.e. $\{w + c \cdot v : c \in \mathbb{R}\}$. This is the line through the point $w$ parallel to $L_v$, shown in Figure 10.4.

<!-- carousel -->
![Figure 10.2: An example of vector addition. The dark dashed vector is the sum of the two solid vectors, and the light dotted vector shows the geometric "tail to head" addition process.](06 - Linear Algebra_images/img-1.jpeg)
![Figure 10.3: A line as all possible scalings of a single nonzero vector $v=(1,2)$.](06 - Linear Algebra_images/img-2.jpeg)
![Figure 10.4: A line described as all possible scalings of a vector $v$, then shifted away from the origin by a second vector $w$.](06 - Linear Algebra_images/img-3.jpeg)
<!-- endcarousel -->

All this said, a plain vector space isn't quite enough to get all of geometry. For example, we can't compute distances or angles without more structure in the vector space. We will enhance the geometric picture by the end of the chapter, but for now we see there are connections between vectors and geometry. We'll keep this geometric foundation in mind while dealing with linear maps more abstractly (which, to be frank, is the hard part of linear algebra). Our task for now is to study where Definition 10.1 takes us.

## Linear Maps, Formally This Time

A linear map describes a function between two vector spaces that preserves the linear structure of the input. The formal definition is just an iota more complicated than our version from the beginning of the chapter.

**Definition 10.2.** Let $X, Y$ be vector spaces with $+_{X}, \cdot_{X}$ being the operations in $X$ and $+_{Y}, \cdot_{Y}$ in $Y$. A function $f: X \to Y$ is called a linear map if the following two identities hold for every $v, w \in X$ and every scalar $c \in \mathbb{R}$:

1. $f(v +_{X}w) = f(v) +_{Y}f(w)$
2. $f(c\cdot_X v) = c\cdot_Y f(v)$

In other words, if $u$ has a linear relationship with $v$—say, $u = a \cdot_X v +_X w$—then $f(u)$ has the same linear relationship with $f(v)$—in this case, $f(u) = a \cdot_Y f(v) +_Y f(w)$.

This notation $+_{X}, \cdot_{X}$ burns my eyes, so we'll drop it and understand that when I say $f(v + w) = f(v) + f(w)$, I mean that the $+$ on the left hand side is happening in $X$ and the $+$ on the right hand side is happening in $Y$. Likewise for scaling, $f(cv) = cf(v)$. Any other interpretation would be a fatal type error. Moreover, as we go on I'll begin to drop the $\cdot$ in favor of "juxtaposition", so that if $a$ is a scalar and $v$ is a vector, it's understood that $av = a \cdot v$. I will use the dot only when disambiguation is needed.

### Examples and Property Testing

Here's a simple example of a linear map. Let $X$ be the vector space of polynomials, and $Y=\mathbb{R}$. Define the *evaluation at 7* function, which I'll denote by $\operatorname{eval}_{7}:X\to\mathbb{R}$, as $\operatorname{eval}_{7}(p)=p(7)$. Let's check the two conditions hold. If $p,q$ are two polynomials, then

$$\operatorname{eval}_{7}(p)+\operatorname{eval}_{7}(q)=p(7)+q(7)=(p+q)(7).$$

In just a little bit more detail at the expense of a big ugly formula, if $p=a_{0}+a_{1}x+\cdots+a_{k}x^{k}$ and $q=b_{0}+b_{1}x+\cdots+b_{m}x^{m}$, then $p+q$ is the polynomial formed by adding the coefficients together. If we suppose that $m\geq k$, then

$$(p+q)(7)=(a_{0}+b_{0})+(a_{1}+b_{1})7+\cdots+(a_{k}+b_{k})7^{k}+b_{k+1}7^{k+1}+\cdots+b_{m}7^{m}.$$

And we can distribute and rearrange all these terms to get exactly $p(7)+q(7)$. Likewise, $\operatorname{eval}_{7}(c\cdot p)=c\cdot p(7)$. Since the number $7$ was arbitrary, the same logic shows that $\operatorname{eval}_{a}$ for any scalar $a\in\mathbb{R}$ is a linear map.

A second example is the map $f:\mathbb{R}^{3}\to\mathbb{R}^{2}$ defined by $(a,b,c)\mapsto(-2a+3b,c)$. Verify as an exercise that this is a linear map.

Linearity is a claim about *all* inputs, so it is a perfect target for a property test: pick thousands of random vectors and scalars and assert both identities hold every time. The demo below does exactly that for Kun's two examples, and—as a control—shows that the innocent-looking $g(x)=x+1$ is *not* linear, because it fails the consequence we prove next (it doesn't fix the zero vector).

```python
<!-- include: code/pim/06 - Linear Algebra/01_linear_map_check.py -->
```

```
eval_7 is linear: 10000 random (p, q, c) all passed
(a,b,c) -> (-2a+3b, c) is linear: 10000 passed
x -> x+1 fails linearity (g(0) = 1, not 0)
```

### Linear Maps Preserve the Zero Vector

For the rest of the chapter, linear maps are the only kind of function we care about for vector spaces. The reason, which we'll spend the rest of the chapter trying to understand, is that linear maps are the maps which preserve the structure of a vector space. Indeed, we *defined* them to preserve the two operations that define a vector space! But as we'll see this covers all the bases. For example, linear maps preserve the zero vector.

**Proposition 10.3.** If $X,Y$ are vector spaces and $f:X\to Y$ is a linear map, then $f(0)=0$.

As I did with $+$ and $\cdot$, I'm using the same symbol $0$ for the additive identity in both vector spaces. In light of this fact it's not so surprising: if there's a unique zero vector in every vector space, and every linear map preserves the zero, then using the same symbol for both zero vectors is not so strange, even if the types of the two zero vectors may be very different.

The proof of this fact "falls out" from the definition. To distinguish $0$ the vector from $0$ the scalar, I'll make the vector bold, like $\mathbf{0}$.

**Proof.** Let's use the fact that $\cdot$ is preserved by a linear map. First, $f(\mathbf{0})$ is the same as $f(0\cdot\mathbf{0})$. Since $f$ is linear, this is the same as $0\cdot f(\mathbf{0})$. But $0\cdot v=\mathbf{0}$ no matter what $v$ is. Putting these together,

$$f(\mathbf{0})=f(0\cdot\mathbf{0})=0\cdot f(\mathbf{0})=\mathbf{0}.$$

∎

Just as trivially, a second proof:

$$f(\mathbf{0})=f(\mathbf{0}+\mathbf{0})=f(\mathbf{0})+f(\mathbf{0}).$$

Subtracting $f(\mathbf{0})$ from both sides gives $\mathbf{0}=f(\mathbf{0})$. Now it's your turn: prove the facts in Exercises 10.1–10.4 which establish basic properties of linear maps.

## The Basis and Linear Combinations

Though we defined a vector space as a set with two operations, you can't do much with that mental model. We need more concrete computational tools to work with a vector space. The first tool is called a *basis*. In short, a basis for a vector space $V$ is a minimal set of vectors $B$ from which you can get all vectors in $V$ by adding and scaling vectors in $B$. The important examples in this book—and crucially, the proofs in this chapter—will focus on the case where $B$ is finite.

The simplest example of a basis is for $V=\mathbb{R}^{2}$. Let $e_{1}=(1,0)$ and $e_{2}=(0,1)$. Then any vector $(a,b)$ can be written as $a\cdot(1,0)+b\cdot(0,1)$. More generally, $\mathbb{R}^{n}$ has a basis of the $n$ vectors which have a 1 in a single coordinate and zeroes elsewhere. E.g., $e_{2}=(0,1,0,\ldots,0)$. This is often called the *standard basis* of $\mathbb{R}^{n}$ and denoted with $e$'s as $\{e_{1},\ldots,e_{n}\}$.

### Non-uniqueness of Bases and Coordinate Systems

Two things to note about the $\mathbb{R}^{2}$ example. First, this is far from the only basis. Almost any two vectors you can think of form a basis. Say, $\{(3,4),(-1,-5)\}$. One way to show this is a basis is to write a known basis like $(1,0)$ and $(0,1)$ in terms of these two vectors:

$$(1,0)=\frac{5}{11}(3,4)+\frac{4}{11}(-1,-5).$$

From the above, one can write $(0,1)$ as $\frac{1}{4}((3,4)-3\cdot(1,0))$. Once $(1,0)$ and $(0,1)$ are expressed in terms of your basis, you can get any vector by using $(c,d)=c(1,0)+d(0,1)$. Convince yourself of this by expressing $(2,-1)$ in terms of our example basis. By the way, I calculated the fractions $5/11$ and $4/11$ by writing down the equation

$$a(3,4)+b(-1,-5)=(1,0),$$

which is really a set of two equations, one for each coordinate:

$$3a-b=1$$
$$4a-5b=0$$

Solving for $a$ and $b$ gives $a=5/11$ and $b=4/11$. The fact that this works for most pairs of vectors you can think of is no coincidence, but we'll return to that later in the chapter. The point for now is that there are many possible bases ("BAY-sees," the plural of basis) of a vector space, and each basis allows you to write any vector in the vector space by summing and scaling the vectors in the basis.

![Figure 10.5: Assembling a point $(1,2)$ as the linear combination $v=e_1+2e_2$ of the standard basis vectors representing the $x$ and $y$ coordinates.](06 - Linear Algebra_images/img-4.jpeg)

The second note is that a basis can be thought of as an alternative coordinate system for a vector space. In $\mathbb{R}^2$ we usually think of coordinates for points by specifying their $x$- and $y$-coordinates (i.e., using the standard basis, $e_1, e_2$). However, once we're fluid with linear algebra we realize that saying "the $x$- and $y$-coordinate" is an arbitrary choice, and one could just as easily have chosen $v_1 = (2, -1)$, $v_2 = (-1, -1)$ as a basis and expressed the same points by their $v_1$-coordinate and $v_2$-coordinate, the coefficients needed to write a point using sums-and-scales of $v_1, v_2$. In this case, the vector in the diagram in Figure 10.6 is represented as $\left(-\frac{1}{3}, -\frac{5}{3}\right)$.

This process of expressing a vector's coordinates with respect to a different basis is analogous to the process of writing integers in a different number base, such as binary or hexadecimal. You choose a base that's useful to you. And just like with numbers, if you find a basis with useful properties, you study it in depth and learn its computational secrets.

![Figure 10.6: Assembling the same point as a linear combination $v=-\frac{1}{3}v_1-\frac{5}{3}v_2$ of two new basis vectors $v_1=(2,-1)$, $v_2=(-1,-1)$.](06 - Linear Algebra_images/img-5.jpeg)

### Linear Combinations and Span

The brief and formal way to say a vector $v$ "can be written using sums and scales of other vectors" is the following definition.

**Definition 10.4.** Let $v_{1}, v_{2}, \ldots, v_{n}$ be a set of vectors in a vector space $V$, and let $x$ be a vector in $V$. We say $x$ is a linear combination of $v_{1}, \ldots, v_{n}$ if there are scalars $a_{1}, \ldots, a_{n} \in \mathbb{R}$ with

$$x = a_{1} v_{1} + \cdots + a_{n} v_{n} = \sum_{i=1}^{n} a_{i} v_{i}.$$

In particular, any way one could "add and scale" vectors reduces to this form, provided one is willing to distribute scalar multiplication over addition, expand, and group all the terms. This is the standardized way to express the existential claim that $x$ can be "built" up from the $v_{i}$.

A bit of common terminology is the span of a set $B$ of vectors, which is the set of all linear combinations of those vectors. That is,

$$\operatorname{span}(v_{1}, \ldots, v_{k}) = \left\{a_{1} v_{1} + \cdots + a_{k} v_{k}: a_{i} \in \mathbb{R} \right\}.$$

When we said informally that a basis is a set of vectors from which you can "get all vectors in $V$," we could have said the set spans $V$. That would have been incomplete, and now we're ready for the formal definition.

**Definition 10.5.** Let $V$ be a vector space. A set $\{v_{1},\ldots ,v_{n}\} \subset V$ is called a basis of $V$ if its span is $V$ and if it is minimal in the property of spanning $V$. That is, if you remove any vector from a basis $\{v_{1},\dots,v_{n}\}$, the resulting set does not span $V$.

This definition makes it clear why we don't say things like $\{(1,0),(2,0),(3,0),(0,1)\}$ is a basis for $\mathbb{R}^2$. Because while it does span $\mathbb{R}^2$, it includes superfluous information. It doesn't make sense as a coordinate system either, because points don't have unique representations.

We will have a lot more to say about bases. Many insights and applications of linear algebra revolve around computing a clever basis. But first we need a few more tools. One of the most important definitions in elementary linear algebra is related to the existence and uniqueness of linear combinations.

### Linear Independence

**Definition 10.6.** Let $V$ be a vector space, and $v_{1},\ldots,v_{n}\in V$ be nonzero vectors. The set $\{v_{1},\ldots,v_{n}\}$ is said to be linearly independent if no $v_{i}$ is in the span of the other vectors $\{v_{j}:j\neq i\}$. Informally we will also say the list $v_{1},\ldots,v_{n}$ is linearly independent, though the ordering of the vectors has no consequence.

Another, equivalent definition of linear independence, and one that's easier to work with in proofs, is that the only way to write the zero vector as a linear combination of $v_{1},\ldots,v_{n}$ is if all the coefficients $a_{i}$ are zero. In other words, there is no nontrivial way to write zero as a linear combination.

$$0=a_{1}v_{1}+\cdots+a_{n}v_{n}\Rightarrow a_{i}=0\text{ for all }i$$

Another equivalent (but seemingly more restrictive) way to express linear independence is to say that $B$ is linearly independent if every vector in $\operatorname{span}(B)$ has a unique expression as a linear combination of vectors in $B$. Indeed, if some vector $x$ could be written as both $\sum_{i=1}^{n}a_{i}v_{i}$ and $\sum_{i=1}^{n}b_{i}v_{i}$, then the difference $\sum_{i=1}^{n}(a_{i}-b_{i})v_{i}$ would be a nontrivial way to write the zero vector! It's nontrivial because some $a_{i}$ and $b_{i}$ have to be different, by our assumption that $x$ has two different representations.

For example, in $\mathbb{R}^{2}$ the set $\{(1,0),(0,1)\}$ is linearly independent, as is the set $\{(3,4),(-1,-5)\}$. However, $\{(1,0),(3,4),(-1,-5)\}$ is linearly dependent (i.e., not linearly independent) because, as we saw, $(1,0)$ is a linear combination of the other two vectors.

Linear independence provides a different perspective on the concept of a basis, which will lead us to Theorem 10.8 and allow us to have a coherent definition of a vector space's dimension.

### Maximally Independent Sets Are Bases

**Theorem 10.7.** Let $V$ be a vector space. Let $B=\{v_{1},\ldots,v_{n}\}$ be a set of linearly independent vectors in $V$, and suppose it's maximal in the sense that if you add any new vector to $B$, then the resulting set is linearly dependent. Then $B$ is a basis for $V$.

**Proof.** Suppose $B=\{v_{1},\ldots,v_{n}\}$ is maximally linearly independent. Our task is to prove that $B$ is a basis of $V$. By definition, this means we need to show both that $\operatorname{span}(B)=V$ and that one cannot remove any vectors from $B$ and still span $V$.

For the first, let $x\in V$ be a vector not in $B$, and our task is to write $x$ as a linear combination of the vectors in $B$. First, we form the set $C=B\cup\{x\}$ by adding $x$ to $B$. Since $B$ is maximally independent, $C$ is a linearly dependent set. That means there are some $a_{i}\in\mathbb{R}$ that allow us to write

$$\mathbf{0}=a_{0}x+a_{1}v_{1}+\cdots+a_{n}v_{n},$$

and not all the $a_{i}$ are zero. Note $a_{0}$ is the coefficient of $x$, the newly added vector. Moreover, $a_{0}\neq 0$ since, if it were, that would provide a nontrivial linear combination equal to 0 using only the vectors in $B$, which contradicts the assumption that $B$ is linearly independent.

We can then safely rearrange to solve for $x$:

$$x=-\frac{1}{a_{0}}(a_{1}v_{1}+\cdots+a_{n}v_{n}).$$

This proves that $x\in\operatorname{span}(B)$. Because $x$ was chosen arbitrarily from $V$, this proves that $V\subset\operatorname{span}(B)$. Since $\operatorname{span}(B)\subset V$ by definition of a vector space, we've shown $\operatorname{span}(B)=V$ (cf. Definition 4.2 for a reminder on using subsets to prove set equality).

Second, we need to show that $B$ is minimal with respect to spanning $V$. Indeed, you cannot write $v_{1}$ as a linear combination of $v_{2},\ldots,v_{n}$, because $v_{1},\ldots,v_{n}$ form a linearly independent set! Hence, removing $v_{1}$ from $B$ would make the resulting set not span $V$ (since $v_{1}\not\in\operatorname{span}\{v_{2},\ldots,v_{n}\}$). The same goes for removing any $v_{i}$.

∎

The above proof makes it clear that for any $x\not\in B$, the statements "$x\in\operatorname{span}(B)$" and "$B\cup\{x\}$ is a linearly dependent set" are logically equivalent. This theorem also provides a simple algorithm to construct a basis (though it's not quite concrete enough to implement). Start with $B=\{\}$. While there exists some vector not in $\operatorname{span}(B)$, find such a vector and add it to $B$. When this loop terminates, $B$ is a basis.

With linear independence, spanning, and bases in hand, we can define dimension and finally the matrix.

## Dimension

At first the concept of a basis seems tame. But it unlocks a world of use. The first thing it allows us to do is measure the size of a vector space. We can do this because of the following fact:

**Theorem 10.8 (The Steinitz exchange lemma).** Let $V$ be a vector space. Then every basis of $V$ has the same size.

**Proof.** This proof hinges on the claim that if $U=\{u_{1},\ldots,u_{n}\}$ is a list of $n$ linearly independent vectors in $V$ (perhaps not maximal), and $W=\{w_{1},\ldots,w_{m}\}$ is a list of $m$ vectors which span $V$ (perhaps not minimally), then $n\leq m$. The theorem follows because if $U$ and $W$ are both bases, then they are both independent and spanning, meaning both $n\leq m$ and $m\leq n$, so $n=m$. To prove the claim, we use an iterative algorithm that transforms $W$ into $U$ as much as possible. This will work by replacing each item from $W$ by one from $U$ until we run out of vectors from $U$. Using the terminology from the "Sets, Functions, and Their -Jections" section, we're building an injection $U\to W$ one element at a time, and the existence of an injection $U\to W$ implies $|U|\leq|W|$.

Start by taking $u_{1}$, removing it from $U$, and adding it to $W$. By the fact that $W$ spans $V$, we can write $u_{1}$ as a linear combination of the $w_{i}$ in which some coefficient, say $a_{1}$ for $w_{1}$, is nonzero.[^wlog]

$$u_{1} = a_{1} w_{1} + a_{2} w_{2} + \cdots + a_{m} w_{m}$$

This means we can rearrange the above to solve for $w_{1}$ in terms of $u_{1}, w_{2}, w_{3}, \ldots, w_{m}$, and hence we can remove $w_{1}$ from $W \cup \{u_{1}\}$ without changing the fact that what remains spans $V$. Call this resulting set $W_{1} = \{u_{1}, w_{2}, w_{3}, \ldots, w_{m}\}$, and call $U_{1} = U - \{u_{1}\}$. Repeat this process with $u_{2}$, forming $W_{2}, U_{2}$, and keep doing it until you get to $U_{n} = \{\}$ and $W_{n}$. In each step we can always remove a new $w_{i}$—that is, we can find a $w_{i}$ with a nonzero coefficient—because all of the $u$'s that we're adding are linearly independent, while $W_{i}$ is still spanning. So the algorithm will reach the $n$-th step, at which point either all of $W$ is replaced by all of $U$ (i.e. $n = m$), or there are some $w_{i}$ left over ($n < m$).

∎

[^wlog]: This is another example of the mathematical sleight of hand called "without loss of generality." What we really mean is: take whichever $w_{i}$ has a nonzero coefficient, and use that going forward. However, since we're planning to do this step iteratively, if we wanted to be precise we'd have to keep track of which indices were selected, and writing that down is painful (with a sub-index like $w_{i_1}, w_{i_2}, \ldots$). Instead we say, "let's just relabel the vectors post-hoc so that $w_{1}$ is one of the vectors with a nonzero coefficient." You often need a mental spot-check to convince yourself this doesn't break the argument; in this case, the order of the $w_{i}$ is irrelevant. If we had to program this, we might be forced to keep track, perhaps for efficiency gains (relabeling would require a full loop through the $w_{i}$). But in mathematical discourse we can flexibly and usefully change the data to avoid crusty notation and get to the heart of the proof.

**Definition 10.9.** The *dimension* of a vector space $V$ is the size of a basis. Denote the dimension of $V$ by $\dim(V)$.

Theorem 10.8 provides well-definition for the notion of the dimension of a vector space. Dimension does not depend on which basis you choose. This reinforces our intuitive understanding of what dimension should be for $\mathbb{R}^n$, i.e., how many coordinates are needed to uniquely specify a point. $\mathbb{R}$ is one-dimensional, the plane $\mathbb{R}^2$ is two-dimensional, physical space at a fixed instant in time is 3-dimensional, etc. The dimension of the space doesn't (and shouldn't) depend on the perspective, and for linear algebra the perspective is the choice of a basis.

### Subspaces

We end this section with the notion of a subspace.

**Definition 10.10.** Let $V$ be a vector space, and let $W \subset V$ be a subset. We call $W$ a *subspace* if the same operations from $V$ also make $W$ a vector space.

In particular, to be a subspace all operations involving only vectors in $W$ must evaluate to vectors in $W$, and $W$ must have the same zero vector as $V$.

The simplest nontrivial example of a subspace is in $V = \mathbb{R}^2$. A one-dimensional subspace here is a line through $(0,0)$, equivalently the span of a single nonzero vector $v \in V$. Likewise, the span of two linearly independent vectors $v, w \in \mathbb{R}^3$ forms a two-dimensional subspace. Geometrically the subspace is the plane containing $(0,0,0)$ and $v$ and $w$. In general, any set of $k\leq n$ linearly independent vectors in $\mathbb{R}^{n}$ spans a $k$-dimensional subspace of $\mathbb{R}^{n}$, which corresponds to a $k$-dimensional plane. Such things are impossible to visualize, but we understand them simply as a set, the span of the chosen vectors.

As these two examples suggest, subspaces can be formed easily by taking a basis $B$ of $V$, and picking any subset $A$ of $B$ to form a basis of $W=\operatorname{span}(A)\subset V$. The converse also works: if you start with a set of vectors $A=\{v_{1},\ldots,v_{k}\}$ spanning a $k$-dimensional subspace of an $n$-dimensional vector space $V$, you can iteratively add vectors not in the span of $A$ until the resulting set spans all of $V$. This process, though not well-defined algorithmically, is existentially possible, and it's called *extending* $A$ to a basis of $V$. In Chapter 12 we'll see a concrete algorithm for it called the *Gram-Schmidt process*, which produces additional useful properties of the resulting basis.

## Matrices

Now we can finally get to the heart of linear algebra.

Linear maps seem relatively complicated at first glance, but they have a rigid structure uniquely determined once you fix a basis in the domain and codomain. Let's draw this out and discover what that structure is. In this section English letters $v$, $w$, $x$, and $y$ will always be vectors, while Greek letters $\alpha$, $\beta$, and $\gamma$ will be scalars.

### Deriving the Matrix from a Linear Map

Start with a linear map $f:\,V\to W$, maybe given by some formula. We want to compute $f$ on an input $x$. You choose a basis $\{v_{1},\ldots,v_{n}\}$ and a basis $\{w_{1},\ldots,w_{m}\}$ for $V$ and $W$, respectively. Now fix $x\in V$ to be arbitrary. Since the $v_{i}$ form a basis, there is some way to write $x$ as a linear combination of the $v_{i}$, say

$$x=\alpha_{1}v_{1}+\alpha_{2}v_{2}+\cdots+\alpha_{n}v_{n}.$$

Crucially, $f$ is a linear map, so we can break $f(x)$ up across the input.

$$f(x)=\alpha_{1}f(v_{1})+\cdots+\alpha_{n}f(v_{n}).$$

If we know what $f$ does to the basis vectors, the above formula tells us how $f$ behaves on $x$. In other words, a linear map is completely determined by how it acts on a basis. This is such an important revelation that I want to shout it from the mountaintops! Chisel it on the forearm of the Statue of Liberty! Put a fuchsia HTML marquee on the front page of Google!

**Theorem 10.11.** A linear map is completely determined by its behavior on a basis![^mnemonic]

[^mnemonic]: I just want to point out how, even though I'm casually defining this basis here, you will remember that the lower-case $v$'s are the basis of $V$ while the $w$'s are the basis of $W$. This is the kind of notational mnemonic mentioned earlier that mathematicians use everywhere.

This implies the data representation of any linear map $f:V\to W$ can be reduced to a fixed number $\dim(V)$ of vectors in $W$: the output of $f$ for each input basis vector.

Now let's say we know that $f(v_{1})=y_{1},f(v_{2})=y_{2}$, etc., the vectors $y_{i}$ now being in $W$. We can do the same decomposition of each $y_{i}$ in terms of the chosen basis for $W$.

$$
\begin{aligned}
f(v_{1}) &=y_{1}=\beta[1,1]w_{1}+\cdots+\beta[1,m]w_{m}\\
f(v_{2}) &=y_{2}=\beta[2,1]w_{1}+\cdots+\beta[2,m]w_{m}\\
&\ \vdots\\
f(v_{n}) &=y_{n}=\beta[n,1]w_{1}+\cdots+\beta[n,m]w_{m}
\end{aligned}
$$

I'm using familiar array-index notation to hint at where we're going. The structure of the matrix will fall out of our analysis. The point of the notation is that the first index, the $i$ in $\beta[i,j]$, tells you which basis vector $v_{i}$ of $V$ you're mapping through $f$ to get $y_{i}$, and the second index $j$ identifies the coefficient of the basis of $W$ in the output (that of $w_{j}$).

To write $f(x)$ in terms of the basis for $W$, we substitute the expansion of each $f(v_{i})$ into the formula $f(x)=\sum_{i}\alpha_{i}f(v_{i})$.

$$
\begin{aligned}
f(x) &=\alpha_{1}(\beta[1,1]w_{1}+\cdots+\beta[1,m]w_{m})\\
&+\alpha_{2}(\beta[2,1]w_{1}+\cdots+\beta[2,m]w_{m})\\
&+\cdots\\
&+\alpha_{n}(\beta[n,1]w_{1}+\cdots+\beta[n,m]w_{m})
\end{aligned}
$$

If you expand and regroup the terms so that the $w_{j}$'s are on the outside (so you can read off their coefficients), you get

$$
\begin{aligned}
f(x) &=(\alpha_{1}\beta[1,1]+\alpha_{2}\beta[2,1]+\cdots+\alpha_{n}\beta[n,1])w_{1}\\
&+(\alpha_{1}\beta[1,2]+\alpha_{2}\beta[2,2]+\cdots+\alpha_{n}\beta[n,2])w_{2}\\
&+\cdots\\
&+(\alpha_{1}\beta[1,m]+\alpha_{2}\beta[2,m]+\cdots+\alpha_{n}\beta[n,m])w_{m}
\end{aligned}
$$

Using summation notation, the coefficient of $w_{j}$ is $\sum_{i=1}^{n}\alpha_{i}\beta[i,j]$.

This is a mouthful of notation, but it's completely generic. The $\alpha_{i}$'s let you specify an arbitrary input vector $x\in V$, and the $n$-by-$m$ array $\beta[i,j]$ contains all the data we need to specify the linear map $f$. We've reduced this initially enigmatic operation $f$ to a simple table of numbers. Provided we've fixed a basis, that is.

We've only cracked the tip of the iceberg. The problem with the notational mess above is it adds too much cognitive load. It's hard to keep track of so many indices! You could make it more succinct by writing it in summation notation, but we can do better. What we really need is a well-chosen abstraction.

The abstraction we're about to see (the matrix) has two virtues. First, it eases the cognitive burden of doing a calculation by representing the operations visually. Second, it provides a rung on the ladder of abstraction which you can climb up when you want to consider the relationship between matrices, linear maps, and the basis you've chosen more abstractly. It does this by defining a new algebra for manipulating linear maps.

Both the visual representation and the algebra merge seamlessly with the functional description of linear maps. As we'll see, composition of functions corresponds to matrix multiplication. Natural operations on linear maps correspond to operations on the corresponding matrices, and conversely operations on matrices correspond to new, useful operations on functions. We will explore this in even more detail in Chapter 12.

### The Matrix as a Table of Numbers

So here's the abstraction that works for any linear map $f:V\to W$. Again, we fix a basis $\{v_{i}\}$ for $V$ and $\{w_{j}\}$ for $W$. Write the numbers from $\beta$ describing the linear map $f:V\to W$ in a table according to the following rule. The columns of the table correspond to the basis of $V$, and the rows correspond to basis vectors of $W$. We call this construction $M(f)$, and the mapping $f\mapsto M(f)$ will be a bijection from the set of linear maps (all using the same fixed basis) to the set of matrices. The entries of column $i$ are defined as the expansion of $f(v_{i})$ in terms of the $w_{j}$. That is, take the basis vector $v_{i}$ for that column, and expand $f(v_{i})$ in terms of the $w_{j}$, getting $f(v_{i})=\beta[i,1]w_{1}+\cdots+\beta[i,m]w_{m}$. The numbers $\beta[i,j]$ (where $j$ ranges from $1$ to $m$) form the $i$-th column of $M(f)$.

$$
M(f)=\begin{pmatrix}
\beta[1,1] & \beta[2,1] & \cdots & \beta[n,1]\\
\beta[1,2] & \beta[2,2] & \cdots & \beta[n,2]\\
\vdots & \vdots & \ddots & \vdots\\
\beta[1,m] & \beta[2,m] & \cdots & \beta[n,m]
\end{pmatrix}
$$

You will have noticed that we've flipped the indices $\beta[i,j]$ from their normal orientation so that $i$ is the column instead of the row. This is an occupational hazard, but we trust a programmer can handle index wizardry. One clever way to express the construction of $M(f)$ with fewer indices is to say that the $i$-th column is just $f(v_{i})$, "spread out" over the column by its expansion in terms of $\{w_{j}\}$:

$$
M(f)=\begin{pmatrix}
\mid & & \mid\\
f(v_{1}) & \cdots & f(v_{n})\\
\mid & & \mid
\end{pmatrix}
$$

### Matrix-Vector Multiplication

The computational process of mapping an input vector $x$ to $f(x)$ is called a matrix-vector product, and it works as follows. First, write $x$ in terms of the basis for $V$ as before, $x = \alpha_{1}v_{1} + \cdots + \alpha_{n}v_{n}$, this time writing the coefficients in a column:

$$
x = \begin{pmatrix} \alpha_{1} \\ \alpha_{2} \\ \vdots \\ \alpha_{n} \end{pmatrix}
$$

Sometimes people call this a "column vector" to distinguish it from the obvious analogue of writing the entries in a row. Let's just call it a vector. Now to compute $f(x)$ using $M = M(f)$, you write $M$ and $x$ side by side (as if the operation were multiplication of integers). The output is a vector $f(x) = z \in W$, which, if written in the same column style as $x$, would have $m$ entries. We'll denote these entries by the Greek gamma $(\gamma_1, \ldots, \gamma_m) = z$.

$$
Mx = \begin{pmatrix} \beta[1,1] & \cdots & \beta[n,1] \\ \beta[1,2] & \cdots & \beta[n,2] \\ \vdots & \ddots & \vdots \\ \beta[1,m] & \cdots & \beta[n,m] \end{pmatrix} \begin{pmatrix} \alpha_{1} \\ \alpha_{2} \\ \vdots \\ \alpha_{n} \end{pmatrix} = \begin{pmatrix} \gamma_{1} \\ \gamma_{2} \\ \vdots \\ \gamma_{m} \end{pmatrix} = z
$$

The computation to get from the left-hand side of this equation to the right is the same as how we grouped terms to get the coefficient of $w_{i}$ earlier. Take the row of $M$ corresponding to $w_{i}$, compute an entrywise product with $x$, and sum the result.[^innerproduct]

$$\gamma_{i} = \beta[1,i]\alpha_{1} + \beta[2,i]\alpha_{2} + \cdots + \beta[n,i]\alpha_{n}$$

[^innerproduct]: As we'll see later in this chapter, this "entrywise product with sum" is called the inner product.

Visually it has always helped me to imagine picking up the first row and rotating it 90 degrees clockwise; that motion lines up the $\beta$ entry with the $\alpha$ entry that it should be multiplied by. Then the sum gives you the first entry $\gamma_{1}$, and you continue down the rows of $M$. Here's an example with a $2 \times 3$ matrix.

$$
\begin{pmatrix} 9 & 2 & 1 \\ 7 & -2 & 0 \end{pmatrix} \begin{pmatrix} 3 \\ -1 \\ 4 \end{pmatrix} = \begin{pmatrix} a \\ b \end{pmatrix}
$$

The first step pairs up the first row of $M$ with $x$:

$$a = 9 \cdot 3 + 2 \cdot (-1) + 1 \cdot 4 = 29.$$

The second does the same with the second row:

$$b = 7 \cdot 3 + (-2) \cdot (-1) + 0 \cdot 4 = 23.$$

It's easy to get lost in the notation and miss the bigger picture, so let's make Theorem 10.11 concrete. The columns of $M(f)$ literally *are* the images $f(e_i)$ of the basis vectors, and the matrix-vector product just rebuilds $f(x)=\sum_i \alpha_i f(e_i)$ as a weighted sum of those columns. The demo verifies Kun's $29, 23$ by hand, then checks that each column equals $A e_i$, and finally confirms Theorem 10.14 below—composition is matrix multiplication—on a thousand random inputs.

```python
<!-- include: code/pim/06 - Linear Algebra/02_matrix_as_map.py -->
```

```
A x = [29 23] (matches Kun's 29, 23)
column i of A equals A @ e_i: [9 7] [ 2 -2] [1 0]
rebuilt from columns: [29 23]
M(g o f) = M(g) M(f): 1000 random vectors agree
```

### Matrix Addition, Scaling, and the Bijection to Linear Maps

We've defined a mechanical algebraic process for computing the output $f(x) \in W$ from the input $x \in V$, provided we have chosen a basis for $V$ and $W$ and provided we can express vectors in terms of a given basis. This is a new type of "multiplication" operator that has very nice properties. For example:

**Definition 10.12.** Let $A, B$ be two $n \times m$ matrices and let $c \in \mathbb{R}$ be a scalar.

1. Define by $cA$ the matrix whose $i,j$ entry is $c \cdot A[i,j]$.
2. Define by $A + B$ the matrix whose $i, j$ entry is $A[i, j] + B[i, j]$.

**Theorem 10.13.** Let $V, W$ be vector spaces and $f, g: V \to W$ two linear maps. The mapping $f \mapsto M(f)$ is linear. That is, if $f + g$ is the function $x \mapsto f(x) + g(x)$, then $M(f + g) = M(f) + M(g)$, and likewise $M(cf) = cM(f)$ for every scalar $c$.

**Proof.** The proof is left as an exercise to the reader.[^trivialproof] ∎

[^trivialproof]: This generally means the proof is not complicated, but it may contain a mess of notation required to write it out properly and doesn't make for good reading. In any event, the statement of the theorem is the enlightening part, while the proof is purely mechanical.

Beyond being linear, the mapping $f \mapsto M(f)$ is a bijection (again, for a fixed choice of bases). Injectivity: every $f$ maps to a different $M(f)$, since $f$ is completely determined by how it acts on the basis, and two matrices $M(f)$ and $M(g)$ with the same entries act the same on a basis. If that's not convincing enough, consider $M(f-g)=M(f)+(-1)M(g)$. If that's the matrix of all zeroes, then, because linear maps preserve zero, $f-g$ must be the zero map. Surjectivity: if you specify a matrix $A$, the $f$ mapping to $A$ is the one with $f(v_{i})$ equal to the linear combination defined by the $i$-th column of $A$.

This bijection allows us to say that linear maps and matrices are "the same thing" without angry mathematicians throwing chalkboard erasers at us. The matrix representation of a linear map is unique, so we can freely switch back and forth between a linear map and its matrix, provided the bases do not change.

### Matrix Multiplication and Function Composition

Matrix-vector multiplication continues to surprise: given two matrices $A$ and $B$ whose dimensions line up appropriately, one can define the *product* of the two matrices by applying the matrix-vector product of $A$ to each column of $B$ separately.

$$
B=\begin{pmatrix}\mid & & \mid\\ \mathbf{b}_{1} & \cdots & \mathbf{b}_{m}\\ \mid & & \mid\end{pmatrix}\qquad AB=\begin{pmatrix}\mid & & \mid\\ A\mathbf{b}_{1} & \cdots & A\mathbf{b}_{m}\\ \mid & & \mid\end{pmatrix}
$$

Then we have the following astounding theorem.

**Theorem 10.14.** Let $U,V,W$ be three vector spaces. Let $f:U\to V$ and $g:V\to W$ be linear maps. Then

$$M(g\circ f)=M(g)M(f),$$

where $g\circ f$ denotes the function composition $x\mapsto g(f(x))$, and $M(g)M(f)$ denotes matrix multiplication.

So the matrix representation of a linear map allows us to compute the composition of functions. If you reflect on this fact (before attempting a rigorous and index-intensive proof), it could not be any other way: the matrix-vector product using $M(g)$ details how to take a basis vector $v_{i}\in V$ and express $g(v_{i})$ in terms of the basis of $W$, while the columns of $M(f)$ express how to do the same with $f$ from $U$ to $V$.

### The Algebra of Linear Maps

This whole process we've undertaken, going from an abstractly defined theory of vector spaces and linear maps to the concrete world of matrices, is analogous to the process of building a computational model for a real-world phenomenon. It's like we're taking light, something which we observe obeys certain behaviors such as reflecting on various surfaces, and casting it to a type where we can quantitatively answer how much it reflects. We can say, without observation, what its different components are in our model, and how two types of light we've never observed interacting would interact. All of these things are possible because of the computational model.

In some more concrete and advanced terminology, we've defined an algebra for linear maps. We showed how to add and "multiply" (compose) linear maps, and these operations hold true to standard algebraic identities (distributive and associative properties). We then did the same for matrices—after fixing a basis—where adding and multiplying are matrix addition and multiplication. The map $f\mapsto M(f)$ provides a way to say these two perspectives behave identically. A linear map $f$ and $M(f)$ are the "same" object, represented two different ways.

The task of finding a route from a conceptually intuitive land (linear maps) to a computationally friendly world (matrices) is a chief goal of much of mathematics. This is the same goal of calculus—its namesake is "calculate"—to convert computations on curves with an infinite nature to a domain where one can do mechanical calculations. And we aren't yet done doing this with linear algebra! Because while we have said how to compute once you have chosen a basis, we haven't discussed the means of actually finding such bases. Many applications of linear algebra are based on computing a useful basis, and that will be the subject of both this chapter's application and the next. As such, we must dive deeper.

## Conjugations and Computations

One assumption I've been leaning on so far is that, given a basis $\{v_{1},\ldots,v_{n}\}$ for $V$ and a vector $x\in V$, one can find the unique expression of $x$ in terms of the basis. In fact, the way we defined a basis ensures existence, but the only example I gave so far to compute this decomposition was, for $V=\mathbb{R}^{2}$, to set up a system of two linear equations with two variables, and solve them.

$$3a-b=1$$
$$4a-5b=0$$

Here $v_{1}=(3,4)$ and $v_{2}=(-1,-5)$ were the two vectors acting as our basis, and we wanted to express the vector $x=(1,0)$ in terms of them. The variables $a,b$ are the unknown coefficients of $v_{1},v_{2}$ we solved for.

One important thing to point out: even though we want to write $x=(1,0)$ in terms of $v_{1},v_{2}$, we actually had a representation of $x$ in terms of a basis already! To even write $x$ down in this coordinate-form, we implicitly used the standard basis for $\mathbb{R}^{2}$, $e_{1}=(1,0),e_{2}=(0,1)$. In the example above $x=1e_{1}+0e_{2}$. In order to express $x$ in terms of a given basis, you have to have already expressed it in terms of some (maybe easy) basis.

### The General Change of Basis Equation

This strategy generalizes. Let's say we have an $n$-dimensional vector space $V$ with two bases:

$$
\begin{aligned}
E &=\{e_{1},e_{2},\ldots,e_{n}\}\\
B &=\{v_{1},v_{2},\ldots,v_{n}\}
\end{aligned}
$$

Say $E$ is the "easy" basis, often the standard basis in $\mathbb{R}^{n}$, and $B$ is the target basis we wish to express some vector $x=\alpha_{1}e_{1}+\cdots+\alpha_{n}e_{n}$ in. Write down a system of $n$ equations with $n$ unknowns, as follows. First express each of the vectors in $B$ in terms of $E$. I'm going to use the notation (e.g.) $v_{2,4}$ to denote the 4th coefficient of $v_{2}$ as it's written in the basis $E$. Finally, write down an equation for each $e_{i}$, which asserts that the coefficient $\alpha_{i}$ of $x$ in $E$ is the same as the sum of the $e_{i}$ coefficients of the (hypothetical) representation of $x$ in $B$. Note that all symbols here represent numbers in $\mathbb{R}$.

$$
\begin{aligned}
\beta_{1}v_{1,1}+\cdots+\beta_{n}v_{n,1} &=\alpha_{1}\\
\beta_{1}v_{1,2}+\cdots+\beta_{n}v_{n,2} &=\alpha_{2}\\
&\ \vdots\\
\beta_{1}v_{1,n}+\cdots+\beta_{n}v_{n,n} &=\alpha_{n}
\end{aligned}
$$

This was a mouthful, but refer back to the two-dimensional example above and identify how that generalizes to this system of equations. Next, we can rewrite the system of equations as a single matrix equation.

$$
\begin{pmatrix}v_{1,1} & \cdots & v_{n,1}\\ v_{1,2} & \cdots & v_{n,2}\\ \vdots & \ddots & \vdots\\ v_{1,n} & \cdots & v_{n,n}\end{pmatrix}\begin{pmatrix}\beta_{1}\\ \beta_{2}\\ \vdots\\ \beta_{n}\end{pmatrix}=\begin{pmatrix}\alpha_{1}\\ \alpha_{2}\\ \vdots\\ \alpha_{n}\end{pmatrix}
$$

This makes it clear that expressing a vector in terms of a basis can be phrased as computing the unknown input of a linear map, $y=(\beta_{1},\ldots,\beta_{n})$, given a specified output $x=(\alpha_{1},\ldots,\alpha_{n})$. It's worthwhile to break this down a bit further.

The matrix $A=(v_{i,j})$ defined above converts a vector from the domain basis to the codomain basis. The domain basis—which indexes the columns of $A$—is the target basis. It's the one we want to express $x$ in terms of. The codomain basis—indexing the rows—is the "easy" basis $E$, the basis used to write $x=(\alpha_{1},\ldots,\alpha_{n})$. Finally, $y$ is the vector of coefficients $(\beta_{1},\ldots,\beta_{n})$ that expresses $x$ in terms of $v_{1},\ldots,v_{n}$, which is what we want.

This entire matrix-vector equation $Ay=x$ expresses the conversion of a vector in the hard basis to a vector in the easy basis. This is mildly strange, since if we think of $A$ as the matrix of a linear map, that linear map is $x\mapsto x$, a no-op! Much like a change of a number basis from binary to decimal or hexadecimal, the semantic meaning of the input is unchanged by the operation, just its data representation and interpretation. Linear maps are semantic, matrices are data interpretations. Nevertheless, these so-called change of basis matrices are crucial to every computational endeavor. In particular, to express $x$ in the basis $(v_{1},\ldots,v_{n})$, we form the change of basis matrix $P$ whose columns are the $v_{i}$, and write $y=P^{-1}x$.

As an aside, it should be intuitively clear that $P$ has an inverse as a function: every vector has exactly one representation in terms of a basis. Even if we didn't know how the conversion works computationally, changing a basis must be a bijection. More usefully, and now that we have a matrix multiplication operation, the inverse of a matrix $A$ is defined in terms of an identity. The identity matrix, denoted $I_{n}$ or $1_{n}$, is the square $n\times n$ matrix defined by having $1$'s on the diagonal and zeros elsewhere.

$$
I_{n}=\begin{pmatrix}1 & 0 & 0 & \cdots & 0\\ 0 & 1 & 0 & \cdots & 0\\ 0 & 0 & 1 & \cdots & 0\\ \vdots & \vdots & \vdots & \ddots & \vdots\\ 0 & 0 & 0 & \cdots & 1\end{pmatrix}
$$

The matrix multiplication operation ensures that $I_{n}A=AI_{n}=A$ for any matrix $A$. Then the inverse $A^{-1}$, if it exists, is defined as the matrix $B$ for which $AB=BA=I_{n}$. As an exercise, prove that if a linear map is a bijection, then its inverse is also a linear map, and the linear-map-to-matrix correspondence preserves inverses.

### Conjugation and Matrix Similarity

More generally, a pattern used everywhere in mathematics is to change basis for a limited-scope operation. In other words, given a change of basis matrix $P$ which changes from basis $B$ to basis $E$, and some linear map $A$ expressed in terms of $E$, you can apply $A$ to a vector $w$ expressed in $B$-coordinates as

$$P^{-1}APw.$$

This expression works in sequence right to left: express $w$ in basis $E$, apply $A$, and convert the result back to $B$. The matrix $P^{-1}AP$ is exactly the linear map for $A$ expressed in terms of the $B$ basis.

Generally, forming the matrix $P^{-1}AP$ is called conjugation of $A$ by $P$. If two matrices can be equated by conjugation, they are often called similar. I personally hate the term "similar" because we're really saying they're identical. If you look at a laptop on your desk and then pick it up and hold it sideways above your head, it's not "similar" to the laptop on your desk, it's the same thing from two different perspectives! That's exactly what happens when you conjugate a matrix. Taking a cue from Chapter 9, matrix similarity is an equivalence relation, and the equivalence classes correspond to linear maps.

Here is the whole story in code. We form $P$ from Kun's basis $\{(3,4),(-1,-5)\}$, recover the coordinates $(5/11, 4/11)$ of $(1,0)$ via $P^{-1}x$, and then conjugate a shear matrix $A$ to get $B=P^{-1}AP$. The check confirms that applying $A$ in standard coordinates and applying $B$ in $v$-coordinates produce the same vector—and that the basis-independent "fingerprints" trace and determinant survive the change of perspective.

```python
<!-- include: code/pim/06 - Linear Algebra/03_change_of_basis.py -->
```

```
(1,0) in basis {v1,v2} = [0.45454545 0.36363636]  (Kun: 5/11, 4/11)
P^-1 A P reproduces A in the new basis: 1000 vectors agree
trace(A)=trace(B)=2.000  det(A)=det(B)=1.000
Same map, two perspectives -- not 'similar', identical.
```

### Gaussian Elimination and Choosing a Good Basis

To compute $P^{-1}x$ is a different pickle. From the perspective of a system of $n$ equations, the standard principle of solving the matrix-vector equation $Ab=x$ by isolating a single variable, substituting, and solving works, but it's extremely tedious. To help with the tedium, mathematicians came up with an algorithm called Gaussian elimination that uses the tabular format of the matrix equation to help organize. Gaussian elimination is important, but it's both inefficient and it computes a lot of extra information.

Gaussian elimination is a general-purpose algorithm that works no matter what your basis is. A shrewder approach, which many applications of linear algebra utilize, is to think hard about the best basis for your intended application, and convert to that basis once at the beginning of a computation. See the exercises for further references and pointers to industry-standard techniques for changing bases, and Chapter 12 for an extended parable on the value of a good basis.

## One Vector Space to Rule Them All

Now we turn to a classification theorem, that $\mathbb{R}^{n}$ is the "only" vector space of finite dimension. We make this formal by showing that all $n$-dimensional vector spaces are isomorphic to each other. We'll define "isomorphic" shortly.

Why do I limit us to finite ($n$) dimensions? Because infinite dimensional vector spaces are more complicated. We have seen an example of such an exotic vector space: polynomials. The set $\{1,t,t^{2},t^{3},\dots\}$ forms a basis. There are other bases, to be sure (see the exercises), but general questions about infinite dimensional vector spaces are much harder to answer without more advanced techniques.

Let's restrict our attention back to finite-dimension. We'll argue why $\mathbb{R}^{n}$ is the only vector space by an illuminating example. Define by $P_{m}$ the vector space of polynomials of degree at most $m$. Note that the obvious basis is $\{1,t,\dots,t^{m}\}$, making $\dim P_{m}=m+1$. Recall from Chapter 2 the "data definition" of a polynomial as a list of coefficients. This perspective naturally inclines us to think that it's "the same" as a usual list of numbers, that is, a vector in $\mathbb{R}^{m+1}$. We make this formal by constructing an isomorphism between $P_{m}$ and $\mathbb{R}^{m+1}$.

**Definition 10.15.** Let $V$ and $W$ be vector spaces. A linear map $f:V\to W$ is called an isomorphism if it is a bijection. If an isomorphism exists $V\to W$, then we say $V$ and $W$ are isomorphic, often denoted by $V\cong W$.

An isomorphism $f$ preserves all structure in mapping elements from $V$ to $W$. As far as linear-algebraic structure is concerned, $V$ and $W$ are identical, and the vectors of $W$ can be thought of as a "relabeling" of the vectors of $V$.

### Polynomials Are Isomorphic to Tuples

**Proposition 10.16.** Let $P_{m}$ be the vector space of polynomials in one variable with degree at most $m$. Then $\mathbb{R}^{m+1}\cong P_{m}$.

**Proof.** Let $\{1,t,t^{2},\dots,t^{m}\}$ be the usual basis for $P_{m}$, and fix the standard basis of $\mathbb{R}^{m+1}$, i.e., $\{e_{1},\dots,e_{m+1}\}$. Define $f:P_{m}\to\mathbb{R}^{m+1}$ as

$$f(a_{0}+a_{1}t+\dots+a_{m}t^{m})=(a_{0},a_{1},\dots,a_{m}).$$

First, $f$ is a linear map: when you add polynomials you add their same-degree coefficients together, and scaling simply scales each coefficient. Second, $f$ is a bijection: if two polynomials are different, then they have at least one differing coefficient (injection); if $(b_{0},b_{1},\dots,b_{m})$ is a vector in $\mathbb{R}^{m+1}$, then it is the image of $p(t)=\sum_{k=0}^{m}b_{k}t^{k}$ under $f$. ∎

This theorem isn't meant to conclude that polynomials are the same as lists in every respect. Quite the opposite, a polynomial comes with all kinds of extra interesting structure (as we saw in Chapter 2). Rather, to phrase polynomials as a vector space is to ignore that additional structure. It says: if all you consider about polynomials is their linearity, then they have the same linear structure as lists of numbers. At times it can be extremely helpful to "ignore" certain unneeded aspects of a problem. As you'll see in an exercise, the polynomial interpolation problem from Chapter 2 relies only on the linear structure of polynomials. Noticing this can inspire other (perhaps more efficient) techniques for doing secret sharing.

### The Classification Theorem

This exploration suggests that *all* data representations of finite-dimensional vector spaces can be thought of as lists of numbers. Those numbers are the coefficients of the basis vectors.

**Theorem 10.17.** Every $n$-dimensional vector space is isomorphic to $\mathbb{R}^{n}$.

**Proof.** Let $\{v_{1},\ldots,v_{n}\}$ be a basis for an $n$-dimensional vector space $V$, and let $\{e_{1},\ldots,e_{n}\}$ be the standard basis for $\mathbb{R}^{n}$. Define $f:V\to\mathbb{R}^{n}$ as follows. Let $x\in V$ be the input, write $x=\alpha_{1}v_{1}+\cdots+\alpha_{n}v_{n}$, and let $f(x)=(\alpha_{1},\ldots,\alpha_{n})$. An analogous argument as in Proposition 10.16 shows $f$ is a linear bijection. ∎

## Geometry of Vector Spaces

In studying matrices, we saw the elegant relationship linear algebra provides between the functional and algebraic perspectives on a linear map. Geometry is the final ingredient. To that end, we need to be able to compute distances and angles. Because all finite-dimensional vector spaces are isomorphic to $\mathbb{R}^{n}$, it makes sense to define angles and distances for vectors in $\mathbb{R}^{n}$ with its standard basis. Subsequently, angles in a vector space $V$ can be defined using an isomorphism between $V$ and $\mathbb{R}^{n}$.

This plan has a wrinkle. We're about to define the inner product, which computes angles in $\mathbb{R}^{n}$. However, the quantitative values of the inner product might not be preserved by an isomorphism! As it turns out, you can always find a special isomorphism that preserves the formula, allowing the inner product formula to work in generality. We'll see this happen in Chapter 12 in more detail.

**Definition 10.18.** Let $v,w$ be vectors in $\mathbb{R}^{n}$, and let $\{e_{1},\ldots,e_{n}\}$ be the standard basis for $\mathbb{R}^{n}$, so that $v=\sum_{i=1}^{n}\alpha_{i}e_{i}$ and $w=\sum_{i=1}^{n}\beta_{i}e_{i}$. The *standard inner product* (or *dot product*) of $v$ and $w$, denoted $\langle v,w\rangle$, is a scalar given by the formula

$$\langle v,w\rangle=\alpha_{1}\beta_{1}+\cdots+\alpha_{n}\beta_{n}=\sum_{i=1}^{n}\alpha_{i}\beta_{i}.$$

### Norms, Angles, and the Law of Cosines

This formula is special because it has a geometric interpretation. Indeed, it can even be defined geometrically without any appeal to the basis, which we'll do now. Note that to understand this proof requires some "elementary" geometry which we haven't covered in this book, namely the idea of a cosine and the law of cosines. If you're unfamiliar with these topics, look them up online.

![Figure 10.7: A triangle with sides $v$, $w$, and $v-w$, whose side lengths satisfy the law of cosines.](06 - Linear Algebra_images/img-6.jpeg)

First, a special case of the inner product: the norm of a vector $v$, denoted $\|v\|$, is defined as $\|v\| = \sqrt{\langle v, v \rangle}$. This quantity is the geometric length or magnitude of $v$. Its formula, $\|v\| = \sqrt{\alpha_1^2 + \cdots + \alpha_n^2}$, is the generalization of the Pythagorean theorem to $n$ dimensions.

We'll also need two facts in the proof, whose proofs follow from the formula for the inner product and simple arithmetic. We will see in Chapter 12 how these properties become a definition.

**Proposition 10.19.** The inner product is symmetric, i.e., $\langle v, w \rangle = \langle w, v \rangle$, and linear in each input. In particular for the first input: $\langle x + y, z \rangle = \langle x, z \rangle + \langle y, z \rangle$ and $\langle cx, z \rangle = c\langle x, z \rangle$. The same holds for the second input by symmetry of the two inputs.

**Theorem 10.20.** The inner product $\langle v, w \rangle$ is equal to $\|v\| \|w\| \cos(\theta)$, where $0 \leq \theta \leq \pi$ is the angle between the two vectors.[^anglesubspace]

[^anglesubspace]: This angle is computed in a 2-dimensional subspace containing $v, w$, viewed as a flat plane. If $v, w$ are linearly independent, this can be the plane spanned by them.

**Proof.** If either $v$ or $w$ is zero, then both sides of the equation are zero and the theorem is trivial, so we may assume both are nonzero. Label a triangle with sides $v, w$ and the third side $v - w$ as in Figure 10.7. The length of each side is $\|v\|, \|w\|$, and $\|v - w\|$, respectively. Assume for the moment that $\theta$ is not 0 or 180 degrees, so that this triangle has nonzero area.

The law of cosines states that

$$\|v - w\|^{2} = \|v\|^{2} + \|w\|^{2} - 2\|v\|\|w\|\cos(\theta).$$

The left hand side is the inner product of $v-w$ with itself, i.e. $\|v-w\|^{2}=\langle v-w,v-w\rangle$. We'll expand $\langle v-w,v-w\rangle$ using symmetry and linearity.

$$
\begin{aligned}
\langle v-w,v-w\rangle &=\langle v,v-w\rangle-\langle w,v-w\rangle\\
&=\langle v,v\rangle-\langle v,w\rangle-\langle w,v\rangle+\langle w,w\rangle\\
&=\|v\|^{2}-2\langle v,w\rangle+\|w\|^{2}
\end{aligned}
$$

Combining our two offset equations, subtract $\|v\|^{2}+\|w\|^{2}$ from each side and get

$$-2\|v\|\|w\|\cos(\theta)=-2\langle v,w\rangle,$$

which, after dividing by $-2$, proves the theorem if $\theta\not\in\{0,180\}$.

Now if $\theta=0$ or $180$ degrees, the vectors are parallel and $\cos(\theta)=\pm 1$. That means we can write $w=cv$ for some scalar $c$. In particular, $c<0$ when $\theta=180$ and $c>0$ for $\theta=0$, and $\|w\|=c\|v\|$ when $c>0$ and $\|w\|=-c\|v\|$ when $c<0$. So the inner product is

$$\langle v,cv\rangle=c\langle v,v\rangle=c\|v\|^{2}=(c\|v\|)\|v\|=\pm\|w\|\|v\|,$$

where the sign matches up with $\cos(\theta)\in\{\pm 1\}$. ∎

### Perpendicularity and Linear Independence

The inner product is important because it allows us to describe perpendicularity of vectors in terms of algebra.

**Theorem 10.21.** Two nonzero vectors $v,w\in\mathbb{R}^{n}$ are perpendicular if and only if $\langle v,w\rangle=0$.

When I say, "$P$ is true if and only if $Q$ is true," I am claiming that the two properties are logically equivalent. In other words, you cannot have one without the other, nor can you exclude one without excluding the other. Proving such an equivalence requires two sub-proofs, that $P$ implies $Q$ and that $Q$ implies $P$. Because logical implication is often denoted using arrows—"$P$ implies $Q$" being written $P\to Q$, and "$Q$ implies $P$" being written $P\leftarrow Q$—these sub-proofs are informally called "directions." So one will prove an if-and-only-if by saying, "For the forward direction, assume $P$ … and hence $Q$," and "For the reverse/other direction, assume $Q$ … and hence $P$." Authors will also often mix in proof by contradiction to complete the sub-proofs. The combined if-and-only-if is often denoted with double-arrows: $P\leftrightarrow Q$, and when pressed for brevity, mathematicians abbreviate "if and only if" with "iff" using two f's. So "iff" is the mathematical cousin of a classic Unix command: 2–3 letters and a long man page to explain it.

Let's prove the if and only if for perpendicular vectors now.

**Proof.** For the forward direction, assume $v$ and $w$ are perpendicular. By definition the angle $\theta$ between them is $90$ or $270$ degrees, and $\cos(\theta)=0$. Hence $\langle v,w\rangle=\|v\|\|w\|\cos(\theta)=0$. For the reverse direction, if $\langle v,w\rangle=0$ then so is $\|v\|\|w\|\cos(\theta)$, meaning one of $\|v\|,\|w\|$, or $\cos(\theta)$ must be zero. Perpendicularity is not defined if one of the two vectors is zero, so both vectors must be nonzero and have a nonzero norm. This leaves $\cos(\theta)=0$. The vectors are perpendicular. ∎

These three geometric facts are exactly the kind of thing a property test nails down. The demo confirms Theorem 10.20 holds on ten thousand random pairs, manufactures perpendicular vectors to confirm Theorem 10.21, and verifies the Pythagorean split $\|\operatorname{proj}\|^2+\|\text{residual}\|^2=\|w\|^2$ that the SVD derivation will lean on heavily.

```python
<!-- include: code/pim/06 - Linear Algebra/04_inner_product_geometry.py -->
```

```
Theorem 10.20: <v,w> = ||v|| ||w|| cos(theta), 10000 OK
Theorem 10.21: <v, w-proj_v(w)> = 0, 10000 OK
Figure 10.8: ||proj||^2 + ||residual||^2 = ||w||^2, 10000 OK
```

As a side note, we'll need the following fact.

**Proposition 10.22.** Two nonzero perpendicular vectors are linearly independent.

**Proof.** Suppose for contradiction that $\langle x,y\rangle=0$ but $ax+by=0$ for some scalars $a,b$. Suppose without loss of generality that $b\neq 0$ (i.e., $ax+by=0$ is a nontrivial linear dependence). In this case, $a$ is also nonzero, since $a=0$ implies $by=0$, which implies $y=0$, and $y$ was assumed to be nonzero. Then

$$0=\langle x,y\rangle=\langle x,-(a/b)x\rangle=-(a/b)\|x\|^{2},$$

meaning that $\|x\|=0$, which implies $x$ is the zero vector, a contradiction. ∎

A similar proof shows that if $x$ is a vector perpendicular to the plane spanned by two vectors $y,z$, then the set $\{x,y,z\}$ is a linearly independent set. In general, given a set of linearly independent vectors, adding a vector that's perpendicular to their span increases the dimension of the spanned subspace by one.

### Projections and Distance to a Subspace

Next we define the projection of one vector onto another.

**Definition 10.23.** Let $v,w$ be vectors in $\mathbb{R}^{n}$, with $v$ nonzero. The *projection* of $w$ onto $v$, denoted $\operatorname{proj}_{v}(w)$, is defined as $\operatorname{proj}_{v}(w)=cv$ where $c\in\mathbb{R}$ is a scalar defined as $c=\frac{\langle v,w\rangle}{\|v\|^{2}}$.

Let me depict this formula geometrically. Say that $v$, the vector being projected onto, is special in that it has magnitude $1$. Such a special vector is called a *unit vector*. In this case the formula defined above for the projection is just $\langle v,w\rangle v$. Now (trivially) write

$$w=\operatorname{proj}_{v}(w)+[w-\operatorname{proj}_{v}(w)].$$

The terms above are labeled on the diagram in Figure 10.8, with $v$ and $w$ solid dark vectors, and the terms of the projection formula as dotted lighter vectors perpendicular to each other. To convince you that the inner product computes the pictured projection, I need to prove to you that the two terms $\operatorname{proj}_v(w)$ and $w - \operatorname{proj}_v(w)$ are geometrically perpendicular. Indeed, I need to show you that

$$\langle w - \operatorname{proj}_{v}(w), \operatorname{proj}_{v}(w) \rangle = 0.$$

![Figure 10.8: The orthogonal projection of $w$ onto $v$. The residual $w-\operatorname{proj}_v(w)$ is perpendicular to the projection.](06 - Linear Algebra_images/img-7.jpeg)

Indeed, since $\operatorname{proj}_v(w) = \langle v,w\rangle v$, let's call $p = \langle v,w\rangle$ and expand:

$$
\begin{aligned}
\langle w - \operatorname{proj}_{v}(w), \operatorname{proj}_{v}(w) \rangle &= \langle w - pv, pv \rangle\\
&= \langle w, pv \rangle - \langle pv, pv \rangle\\
&= p\langle w, v \rangle - p^{2}\|v\|^{2}\\
&= p^{2} - p^{2} = 0
\end{aligned}
$$

The last step used the assumption that $\|v\| = 1$, and again that $p = \langle w, v \rangle = \langle v, w \rangle$. You can prove the same fact with the version of the projection formula that does not require unit vectors, if you keep track of the extra norms. The essence of the proof is the same. The extra term in the formula for $\operatorname{proj}_v(w)$ dividing by $\|v\|^2$ is just to make $v$ a unit vector in the two places $v$ is used, once in the inner product and once to make the $v$ being projected onto a unit vector. Ideally you never project onto something which is not a unit vector, but if you must you can normalize it as part of the formula.

Figure 10.8 is accurate in suggesting the two vectors are actually perpendicular. By virtue of being perpendicular to the projection, the norm of the vector $w - \operatorname{proj}_v(w)$ can be thought of as measuring the distance of $w$ from $\operatorname{proj}_v(w)$. Or, more geometrically, the distance of the point represented by $w$ from the line spanned by $v$. This is useful for obvious reasons in the kind of geometry used in computer graphics. But it's also useful for us because the data we compute from the projection allows us to measure a "best fit." Finding the line of best fit for a collection of points is the base case of the SVD algorithm, the application for this chapter.

More generally, given a subspace $V \subset \mathbb{R}^n$ spanned by $\{v_1, \ldots, v_k\}$, the distance from $w$ to the subspace can be thought of as the minimal distance from $w$ to any vector in $\operatorname{span}\{v_{1},\ldots,v_{k}\}$. If the basis vectors $v_{i}$ are pairwise perpendicular, then you can also define the projection of a vector $w$ onto a subspace as the sum of projections onto each vector in the subspace basis:

$$\operatorname{proj}_{V}(w)=\sum_{i=1}^{k}\operatorname{proj}_{v_{i}}(w).$$

Then the distance from $w$ to the subspace $V$ is $\|w-\operatorname{proj}_{V}(w)\|$, as expected.

## Application: Singular Value Decomposition

A brief summary of this chapter would rephrase the relationship between a matrix and a linear map. A matrix is a useful representation of a linear map that is fixed after choosing a basis, and the algebraic properties of a matrix correspond to the functional properties of the map. That, and certain operations on vectors have nice geometric interpretations.

We save the juiciest properties for Chapter 12, where we will discuss eigenvalues and eigenvectors. Nevertheless, we have access to fantastic applications. The technique for this chapter, the singular value decomposition (SVD), is a ubiquitous data science tool. It was also a crucial part of the winning entry for the million dollar Netflix Prize. The Netflix Challenge, held from 2006–2009, was a competition to design a better movie recommendation algorithm. The winning entry, awarded to Robert Bell, Yehuda Koren, and Chris Volinsky, improved on the accuracy of Netflix's algorithm by ten percent. The singular value decomposition was used to represent the data (movie ratings) as vectors in a vector space, and the "decomposition" part of SVD chooses a clever basis that models the data. After finding this useful representation, the Netflix Prize winners used the vector representation as input to a learning algorithm.

Though true movie ratings require dealing with issues we will ignore (like missing data), we'll couch the derivation of the SVD in a discussion of movie ratings. The geometric punchline is: treat the movie ratings as points in a vector space, and find a low-dimensional subspace which all the points are close to. This low-dimensional subspace "approximates" the data by projecting onto the subspace. Using the subspace as a model makes subsequent operations like clustering and prediction faster and more stable in the presence of noise.

### A Linear Model for Rating Movies

Let's start with the idea of a movie rating database to understand the modeling assumptions of the SVD. We have a list of people, say Aisha, Bob, and Chandrika, who rate each movie with an integer 1–5. These intrepid movie lovers have watched and critiqued every single movie in the database. We write their ratings in a matrix $A$ as in Figure 10.9.

<!-- carousel -->
![Figure 10.9: An example movie rating matrix for three people. Columns are people, rows are movies.](06 - Linear Algebra_images/img-8.jpeg)
![Figure 10.10: The rating map $A$ sends each "person" basis vector to that person's column of ratings.](06 - Linear Algebra_images/img-9.jpeg)
<!-- endcarousel -->

Each person's ratings is a priori a complicated function, not entirely determined by the movies alone. Aisha likes Thor but not Skyfall, but the reason is not in the data. By writing the ratings in a matrix we are implicitly adding a "linear model" to the ratings. That is, we're saying the input is $\mathbb{R}^3$ and the basis vectors are people:

$$\{x_{\text{Aisha}}, x_{\text{Bob}}, x_{\text{Chandrika}}\}$$

The codomain is $\mathbb{R}^8$ (if there are only 8 movies, as in this toy example), and the basis vectors are $y_{\mathrm{Up}}, y_{\mathrm{Skyfall}}$, etc. By representing the ratings this way, we're imposing the hypothesis that the process of rating movies is linear in nature. That is, the map $A$ computes the decision making process from people to ratings. The coefficients of $A(x_{\mathrm{Aisha}})$ written in terms of the basis of movies form the first column of the matrix in Figure 10.9. In this way, each vector in the domain can be seen as either a person, or purely as the movie ratings provided by that person. Conversely, each vector on the codomain is purely defined in terms of how it is assembled from the ratings of the basis movies. The movie rating function $A$ is also assumed to be one combined function, as opposed to different for each person.

These assumptions should give us pause. Beyond the sociological assumptions made here, the linear model also grants us strange new mathematical abilities. We started with a dataset of ratings, which is included in the linear-algebraic world as $A(x_{\text{Aisha}}),A(x_{\text{Bob}})$, and $A(x_{\text{Chandrika}})$. But since we represent movies and people as vectors, we may form linear combinations. We may construct the movie $0.5y_{\text{Up}}+0.5y_{\text{Snatch}}$, which we might think of as the abstract equivalent of a movie that is "half-way" between Up and Snatch. We may also ask for a "person" whose movie-rating preferences are half-way in between Aisha and Bob, and ask how this person would rate Amelie. Indeed, the fact that $A$ is a linear map provides an immediate answer to this question: average the ratings of Aisha and Bob. The behavior of $A$ on any vector is determined by its behavior on the basis.

We can also create nonsense when we subtract vectors, or scale them beyond reasonable interpretations. What would the movie $75y_{\text{Grease}}-8y_{\text{Thor}}$ look like? You may conjure a cohesive explanation, but you'd be straining logic to fit the image of gibberish. Very off brand.

Of course, the goal of a rating system is to predict the ratings of people on movies they have not seen, based on how two people's ratings align. So a valid answer is, "we don't care about weird linear combinations." That said, more likely than not our chosen linear algebraic hammer relies on strange linear combinations. It's worthwhile to illustrate the necessary assumptions entailed by imposing linear algebra on a real world problem, and the curious luggage this stranger brings along.

The central point is that we can represent a movie (or a person) formally as a linear combination in some abstract vector space. But we don't represent a movie in the sense of its content, only those features of the movie that influence its rating. We don't know what those features are, but we can presumably access them indirectly through the data of how people rate movies. We don't have a legitimate mathematical way to understand that process, so the linear model is a proxy. What's amazing is how powerful a dumb linear proxy can be, given enough data.

It's totally unclear what this means in terms of real life, except that you can hope (or hypothesize, or verify) that if the process of rating movies is "linear" in nature then this formal representation will accurately reflect the real world. It's like how physicists all secretly know that mathematics doesn't literally dictate the laws of nature, because humans made up math in their heads and if you poke nature too hard the math breaks down. But math as a language is so convenient to describe hypotheses (and so accurate in most cases!), that we can't help but use it to design airplanes. We haven't yet found a better tool than math.

Likewise, movie ratings aren't literally a linear map, but if we pretend they are we can make algorithms that accurately predict how people rate movies. So if you know that Skyfall gets ratings 1, 2, and 1 from Aisha, Bob, and Chandrika, respectively, then a new person would rate Skyfall based on a linear combination of how well they align with these three people on other ratings. In other words, up to a linear combination, in this example Aisha, Bob, and Chandrika epitomize the process of rating movies.

The idea in SVD is to use a better choice of people than Aisha, Bob, and Chandrika, and a better choice of movies, by isolating the independent aspects of the process into separate vectors in the basis. Concretely this means the following:

1. Choose a basis $p_{1},\ldots,p_{n}$ of the space of people. Every person in the database can be written as a linear combination of the $p_{i}$, and all the $p_{i}$ are perpendicular and unit vectors. This is true of our starting basis, but (3) will clarify why this new basis is special.
2. Do the same for movies, to get $q_{1},\ldots,q_{m}$.
3. Do (1) and (2) in such a way that the resulting representation of $A$ only has entries on the diagonal. I.e., $A(p_{1})=c_{1}q_{1}$ for some constant $c_{1}$, likewise for $p_{2}$, $p_{3}$, etc.

One might think of the $p_{i}$ as "idealized critics" and the $q_{j}$ as "idealized movies." If the world were unreasonably logical, then $q_{1}$ might correspond to the "ideal action movie" and $p_{1}$ to the "idealized action movie lover." The fact that $A$ only has entries on the diagonal means that $p_{1}$ gives a nonzero rating to $q_{1}$ and only $q_{1}$. A movie is represented by how it decomposes (linearly) into "idealized" movies. To make up some arbitrary numbers, maybe Skyfall is $2/3$ action movie, $1/5$ dystopian sci-fi, and $-6/7$ comedic romance. A person would similarly be represented by how they decompose (via linear combination) into an action movie lover, rom-com lover, etc.

To be completely clear, the singular value decomposition does not find the ideal action movie. The "ideality" of the singular value decomposition is with respect to the inherent linear structure of the rating data. In particular, the "idealized genres" are related to how closely the data sits in relation to certain lines and planes. This is the crux of why the SVD algorithm works, so we'll explain it shortly. But nobody has a strong idea of how the movie itself relates to the geometric structure of this abstraction. It almost certainly depends on completely superficial aspects of the movie, such as how much it was advertised or whether it's a sequel. Nevertheless, much of the usefulness of the SVD abstraction relies on not being domain-specific. The more a model encodes about movie-specific features, the less it applies to data of other kinds. One sign of a deep mathematical insight is domain-agnosticism.

The takeaway is that this mental model of an idealized genre movie and an idealized genre-lover grounds our understanding of the SVD. We want to find bases with special structure related to the data. We know the analogy is wrong, but it's a helpful analogy nonetheless.

Earlier I said that the SVD is about finding a low-dimensional subspace that approximates the data well. It won't be clear until we dive into the algorithm, but this is achieved by taking our special basis of idealized people, $p_{1},\ldots,p_{n}$ (likewise for movies), and ordering them by how well they capture the data. There is a single best line, spanned by one of these $p_{i}$, that the points are collectively closest to. Once you've found that, there is a second best vector which, when combined with the first, forms the best-fitting plane (two-dimensional subspace), and so on.

The approximation aspect of the SVD is to stop at some step $k$, so that you have a $k$-dimensional subspace that fits the data well. The matrix $P$ whose rows are the chosen $p_{1},\ldots,p_{k}$ is the linear map that projects the input vector $x$ to the closest point in the subspace spanned by $p_{1},\ldots,p_{k}$. This is simply because the matrix-vector multiplication $Px$ involves an inner product $\langle p_{i},x\rangle$—the projection formula onto a unit vector $p_{i}$—between each row of $P$ and $x$.

Hopefully $k$ is much less than $m$ or $n$, but still captures the "essence" of the data. Indeed, it turns out that if you define the special basis vectors in this way—spanning the best-fitting subspaces in increasing order of dimension—you get everything you want. You can also build these best-fitting subspaces recursively. The best-fitting 2-dimensional subspace is formed by taking the best line and finding the next best vector you could add. Likewise, the best 3-dimensional subspace is that best plane coupled with the next best vector. We're glomming on vectors greedily.

It should be shocking that this works. Why should the best 5-dimensional subspace be at all related to the best 3-dimensional subspace? For most problems, in math and in life, the greedy algorithm is far from optimal. When it happens, once in a blue moon, that the greedy algorithm is the best solution to a natural problem—and not obviously so—it's our intellectual duty to stop what we're doing, sit up straight, and really understand and appreciate it.

### Minimizing and Maximizing

First we'll define what it means to be the "best-fitting" subspace to some data. Below, by the "distance from a vector $x$ to a subspace $W$," I mean the minimal distance between $x$ and any vector in $W$.

**Definition 10.24.** Let $X=\{w_{1},\ldots,w_{m}\}$ be a set of $m$ vectors in $\mathbb{R}^{n}$. The best approximating $k$-dimensional linear subspace for $X$ is the $k$-dimensional linear subspace $W\subset\mathbb{R}^{n}$ which minimizes the sum of the squared distances from the vectors in $X$ to $W$.

Next we study this definition to come up with a suitable quantity to optimize. Say I have a set of $m$ vectors $w_{1},\ldots,w_{m}$ in $\mathbb{R}^{n}$, and I want to find the best approximating 1-dimensional subspace. Given a candidate line spanned by a unit vector $v$, measure the quality of that line by adding the sum-of-squares distances from $w_{i}$ to $v$. Using the projection function defined earlier,

$$\operatorname{quality}(v)=\sum_{i=1}^{m}\|w_{i}-\operatorname{proj}_{v}(w_{i})\|^{2}.$$

This formula, in a typical math writing fashion, exists only to help us understand what we're optimizing: squared distances of points from a line. To make it tractable, we convert it back to the inner product. I'll describe this process in fine detail, with sidebars to explain some notational choices.

We want to find the unit vector $v$ that minimizes the quality function. We'd write the goal of minimizing this expression as

$$\arg\min_{v}\sum_{i=1}^{m}\|w_{i}-\operatorname{proj}_{v}(w_{i})\|^{2}.$$

A sidebar on notation: when I write $\min_{v}\text{EXPR}$ I am defining an anonymous function whose input is $v$ and whose output is EXPR (depending on $v$), and the total expression (with the min) evaluates to the minimal output value considered over all possible inputs $v$. The domain of $v$ is usually defined in the prose, but if it's helpful and fits, the conditions on $v$ can be expressed in the subscript, such as

$$\min_{\substack{v\in\mathbb{R}^{n}\\\|v\|=1}}\text{EXPR},$$

which is the minimum value of EXPR considered over all possible unit vectors in $\mathbb{R}^{n}$. Just to drive the point home, this is equivalent to the pseudo-Python snippet:

```python
min(EXPR for v in domain if norm(v) == 1)
```

The analogous expression which evaluates to the input vector $v$ (instead of the value of the expression being optimized) is called "arg min." The arg prefix generally means, get the "argument," or input, to the optimized expression. Note that there can be multiple minimizers of an expression, so we are implicitly saying we don't care which minimizer is chosen. It's a highly context-dependent bit of notation. If I replaced min with arg min in the offset equation above, it would correspond to the following Python snippet.

```python
min(v for v in domain if norm(v) == 1, key=lambda v: EXPR)
```

I introduced the argmin because we actually want to find the minimizing vector. It's false to claim $\min_{x\geq 0}(x^{2}+1)=\min_{x\geq 0}x^{2}$, even though the argmins are unique and equal. So our line-of-best-fit problem is most rigorously written as:

$$\arg\min_{\substack{v\in\mathbb{R}^{n}\\\|v\|=1}}\sum_{i=1}^{m}\|w_{i}-\operatorname{proj}_{v}(w_{i})\|^{2}.$$

Now we continue to convert it to the inner product. Since $\operatorname{proj}_{v}(w_{i})$ and $w_{i}-\operatorname{proj}_{v}(w_i)$ are perpendicular, we can apply the Pythagorean theorem, in this case that $\|\operatorname{proj}_{v}(w_{i})\|^{2}+\|w_{i}-\operatorname{proj}_{v}(w_{i})\|^{2}=\|w_{i}\|^{2}$, rearranging to replace each term in the sum:

$$\arg\min_{v}\sum_{i=1}^{m}\left(\|w_{i}\|^{2}-\|\operatorname{proj}_{v}(w_{i})\|^{2}\right).$$

Next, notice that the $\|w_{i}\|^{2}$ don't depend on the input $v$, meaning we can't optimize them and can remove them from the expression without changing the argument of the minimum (it does change the value of the min). The minimization problem is now

$$\arg\min_{v}\left(-\sum_{i=1}^{m}\|\operatorname{proj}_{v}(w_{i})\|^{2}\right).$$

And because minimizing something is the same as maximizing its opposite, we can swap the optimization. Let's also use the inner product formula for the projection instead of the squared-norm. We've reduced the best fitting line optimization to finding a unit vector $v$ which maximizes

$$\arg\max_{v}\sum_{i=1}^{m}\langle w_{i},v\rangle^{2}.$$

If we place the vectors $w_{i}$ as the rows of a matrix $A$, the matrix-vector multiplication formula gives us (almost) exactly these inner products! That is, $Av$ as a vector has the values $\langle w_{i},v\rangle$ as its entries, and taking a squared norm $\|Av\|^{2}$ gives the quantity we're trying to optimize. So our problem can be written as

$$\arg\max_{v}\|Av\|^{2}.$$

Maximizing the square of a non-negative value is the same as maximizing the non-squared thing, so we can equivalently write $\arg\max_{v}\|Av\|$.

To summarize, we started with a dataset of $m$ vectors $w_{i}$ which we interpreted as points in $\mathbb{R}^{n}$. These are the rows of the movie rating matrix, the vector of ratings per movie. We saw that the best approximating line for the vectors $\{w_{i}\}$ is spanned by the unit vector $v\in\mathbb{R}^{n}$ which maximizes $\|Av\|$, where $A$ is a matrix whose rows are the $w_{i}$. This $v$ will end up being one of our "idealized people," the so-called first singular vector of $A$.

There are many algorithms that solve this optimization problem. We'll use a particularly simple one, and defer implementing it until after we see how this problem can be used as a subroutine to compute the full singular value decomposition.

### Singular Values and Vectors

Here is the main theorem that makes the SVD work:

**Theorem 10.25 (The SVD Theorem).** Computing the best $k$-dimensional subspace fitting a dataset reduces to $k$ applications of the one-dimensional optimization problem.

This is so astounding and useful that the solutions to each one-dimensional problem are given names: the singular vectors. I will define them recursively. Let $A$ be an $m\times n$ matrix ($m$ rows for the movies, and $n$ columns for the people) whose rows are the data points $w_{i}$. Let $v_{1}$ be the solution to the one-dimensional problem

$$v_{1}=\arg\max_{\substack{v\in\mathbb{R}^{n}\\\|v\|=1}}\|Av\|.$$

Call $v_{1}$ the first singular vector of $A$. Call the value of the optimization problem, i.e. $\|Av_{1}\|$, the first singular value and denote it by $\sigma_{1}(A)$, or just $\sigma_{1}$ if $A$ is understood from context.

Informally, $\sigma_{1}(A)$ is larger if we capture the data better by $v_{1}$. So as the points in $A$ move toward the line spanned by $v_{1}$, $\sigma_{1}(A)$ increases. If all the data points lie on the line spanned by $v_{1}$, then $\sigma_{1}(A)^{2}$ is exactly the sum of squared-norms of the rows of $A$. Indeed, if $x\in\operatorname{span}(v_{1})$ and $v_{1}$ is a unit vector, then $v_{1}=\pm x/\|x\|$ and $\operatorname{proj}_{v_{1}}(x)=\langle x,v_{1}\rangle v_{1}=x$.

Now we can move up in dimension. To find the best $2$-dimensional subspace, you first take the best line $v_{1}$, and you look for the next best line, considering only those vectors perpendicular to $v_{1}$. That optimization problem is written as (assuming henceforth that the domain is $\mathbb{R}^{n}$)

$$v_{2}=\arg\max_{\substack{\|v\|=1\\\langle v,v_{1}\rangle=0}}\|Av\|.$$

The solution $v_{2}$ is called the second singular vector, along with the second singular value $\sigma_{2}(A)=\|Av_{2}\|$.

Often writers will use the binary operator $\perp$ to denote perpendicularity of vectors instead of the inner product. So $v\perp v_{1}$ is the assertion that $v$ and $v_{1}$ are perpendicular. The $\perp$ symbol has many silly names ("up tack" on Wikipedia). In my experience most people call it the "perp" symbol, since in mathematical typesetting it's denoted by `\perp`.

Continuing with the recursion, the $k$-th singular vector $v_{k}$ is defined as the solution to the optimization problem $\|Av\|$ for unit vectors $v$ perpendicular to every vector in $\operatorname{span}\{v_{1},\ldots,v_{k-1}\}$. The corresponding singular value is $\sigma_{k}(A)=\|Av_{k}\|$. You can keep going until either you reach $k=n$ and you have a full basis, or else some $\sigma_{k}(A)=0$, in which case all the vectors in your data set lie in the span of $\{v_{1},\ldots,v_{k-1}\}$.

As a side note, by the way we defined the singular values and vectors,

$$\sigma_{1}(A)\geq\sigma_{2}(A)\geq\cdots\geq\sigma_{n}(A)\geq 0.$$

This should be obvious, and if it's not take a moment to do a spot check and see why.

Now we can prove the SVD Theorem.

**Proof.** Recall we're trying to prove that the first $k$ singular vectors span the $k$-dimensional subspace of best fit for the vectors that are the rows of $A$. That is, they span a linear subspace $Y$ which maximizes the sum-of-squares of the projections of the data onto $Y$. For $k=1$ this is trivial, because we defined $v_{1}$ to be the solution to that optimization problem. The case of $k=2$ contains all the important features of the general inductive step. Let $Y$ be any best-approximating $2$-dimensional linear subspace for the rows of $A$. We'll show that the subspace spanned by the two singular vectors $v_{1},v_{2}$ is at least as good (and hence equally good as $Y$).

Let $y_{1}, y_{2}$ be a basis of unit vectors of $Y$, and require $y_{1} \perp y_{2}$. Note $\|Ay_{1}\|^{2} + \|Ay_{2}\|^{2}$ is the quantity we need to maximize, and any unit-vector-basis of $Y$ maximizes this quantity by assumption. Moreover, we're going to pick $y_{2}$ so that it's perpendicular to the first singular vector $v_{1}$. Justify this by considering two cases: either by happenstance $v_{1}$ is already perpendicular to every vector in $Y$, in which case any choice for $y_{1}, y_{2}$ will do, or else $v_{1}$ isn't perpendicular to $Y$ and you can choose $y_{1}$ to be the unit vector spanning $\operatorname{proj}_Y(v_1)$, with $y_{2}$ being any unit vector in $Y$ perpendicular to $y_{1}$. The resulting $y_{2}$ is perpendicular to $v_{1}$. (If it's hard to visualize that this can be done, draw a picture in 3 dimensions.)

By definition $v_{1}$ maximizes $\|Av\|$, implying $\|Av_{1}\|^{2} \geq \|Ay_{1}\|^{2}$. Moreover, since we chose $y_{2}$ to be perpendicular to $v_{1}$ (and hence a possible candidate for the second singular vector), the second singular value $v_{2}$ satisfies $\|Av_{2}\|^{2} \geq \|Ay_{2}\|^{2}$. Hence the objective by $\{v_{1}, v_{2}\}$ is at least as good as $Y$:

$$\|Av_{1}\|^{2} + \|Av_{2}\|^{2} \geq \|Ay_{1}\|^{2} + \|Ay_{2}\|^{2}.$$

The right hand side of this inequality is maximal by assumption, so they must actually be equal and both be maximizers.

For the general case of $k$, the inductive hypothesis tells us that the first $k$ terms of the objective for $k + 1$ singular vectors is maximized, and we just have to pick any vector $y_{k+1}$ that is perpendicular to all $v_1, v_2, \ldots, v_k$, and the rest of the proof is just like the 2-dimensional case. We encourage the skeptical reader to fill in the details. ∎

The singular vectors $v_{i}$ are elements of the domain. In the context of the movie rating example, the domain was people, and so the singular vectors in that case are "idealized people." As we said earlier, we also want the same thing for the codomain, the "idealized movies," in such a way that $A$ is diagonal when represented with respect to these two bases.

Say the singular vectors are $v_{1}, \ldots, v_{n}$, and the singular values are $\sigma_{1}, \ldots, \sigma_{n}$. That gives us two pieces of the puzzle: the diagonal representation $\Sigma$ (the Greek capital letter sigma, since its entries are the lower case sigma singular values $\sigma_{i}$) defined as follows:

$$
\Sigma = \begin{pmatrix}
\sigma_{1} & 0 & \cdots & 0 & 0\\
0 & \sigma_{2} & \cdots & 0 & 0\\
\vdots & \vdots & \ddots & \vdots & \vdots\\
0 & 0 & \cdots & \sigma_{n-1} & 0\\
0 & 0 & \cdots & 0 & \sigma_{n}\\
0 & 0 & \cdots & 0 & 0\\
\vdots & \vdots & \ddots & \vdots & \vdots\\
0 & 0 & \cdots & 0 & 0
\end{pmatrix}
$$

And the domain basis: a matrix $V$ whose columns are the $v_i$, or equivalently $V^T$ whose rows are the $v_i$.[^transpose] If we want to write $A$ in this diagonal way, we just have to fill in a change of basis matrix $U$ for the codomain.

$$A = U\Sigma V^T$$

[^transpose]: Here the superscript $T$ denotes the transpose of $V$; that is, $V^T$ has as its $i, j$ entry the $j, i$ entry of $V$. It swaps rows and columns, but we'll have much more to say in Chapter 12. For now, it's enough to note (and easy to verify) that if $V$ has perpendicular unit vectors as columns, then $V^T = V^{-1}$, so we can use $V^T$ as a change of basis from the standard basis to the basis defined by $V$.

Indeed, there's one obvious guess (which we'll later scale to unit vectors): define $u_i = A v_i$. Let's verify the $u_i$ form a basis. Note they form a basis of the image of $A$ (the set $\{A v : v \in \mathbb{R}^n\}$), since it can happen that $m > n$. To get a full basis, just extend the partial basis of $u_i$'s in any legal way to get a full basis. To show the $u_i$ form a basis, take any vector $w$ in the image of $A$, write it as $w = A x$, and write $x$ as a linear combination of the $v_i$:

$$
\begin{aligned}
w &= A(c_1 v_1 + \cdots + c_n v_n)\\
&= c_1 A v_1 + \cdots + c_n A v_n\\
&= c_1 u_1 + \cdots + c_n u_n
\end{aligned}
$$

It can be proved that the $u_i$ are perpendicular, but the only proof I have seen is somewhat technical and for brevity's sake I will skip it. But taking this on faith, the $u_i$ form a basis and one can express $A = U\Sigma V^T$, as desired. The fact that $A = U\Sigma V^T$ is why SVD is called a "decomposition." The $U, \Sigma, V$ are the components that $A$ is broken into, and each are particularly simple.

This decomposition is also what makes the SVD a tool for approximation. If we keep only the top $k$ singular triples $(\sigma_i, u_i, v_i)$ and rebuild $A_k = \sum_{i=1}^{k} \sigma_i u_i v_i^T$, we get the best possible rank-$k$ approximation of $A$. The demo below builds a noisy near-rank-2 matrix, reconstructs it at every rank, and watches the error fall monotonically—then confirms the Eckart–Young theorem, that the best rank-$k$ error is exactly the norm of the discarded singular values. This is image compression and dimensionality reduction in one identity.

```python
<!-- include: code/pim/06 - Linear Algebra/06_low_rank_approx.py -->
```

```
singular values: [59.341  9.471  1.045  0.597  0.408  0.364]
k = 6  rebuilds A exactly

 rank k | reconstruction error ||A - A_k||
    1   |    9.56281
    2   |    1.32212
    3   |    0.80990
    4   |    0.54725
    5   |    0.36438
    6   |    0.00000

best rank-2 error = ||discarded sigmas|| = 1.32212
(Eckart-Young: truncating the SVD IS the best approximation)
```

### The One-dimensional Problem

Now that we've seen that the SVD can be computed by greedily solving a one-dimensional optimization problem, we can turn our attention to solving it. We'll use what's called the power method for computing the top eigenvector. The next chapter will be all about eigenvectors, but we don't need to know anything about eigenvectors to see this algorithm. In lieu of knowledge about eigenvectors, the algorithm will just appear to use a clever trick.

The idea is to take $A$, the original input data matrix, and instead work with $A^T A$. Why is this helpful? Using our decomposition from the previous section, we can write $A = U\Sigma V^T$, where $U, V$ are change of basis matrices (whose columns are perpendicular unit vectors!) and $V$ actually contains as its columns the vectors we want to compute. So we can do a little bit of matrix algebra to get

$$A^T A = \left(U\Sigma V^T\right)^T \left(U\Sigma V^T\right) = V\Sigma^T U^T U\Sigma V^T = V\Sigma^2 V^T.$$

We're using $\Sigma^2$ to denote $\Sigma^T\Sigma$, which is a square matrix whose diagonals are the squares of the singular values $\sigma_i(A)^2$. Also note that because the columns of $U$ are perpendicular unit vectors, the product $U^{T}U$ is a matrix with $1$'s on the diagonal and zeros elsewhere; i.e., the identity matrix.

Using $A^{T}A$ isolates the $V$ part of the decomposition. Now for the algorithm:

**Theorem 10.26 (The Power Method).** Let $x$ be a unit vector that has a nonzero component of $v_{1}$ (a random unit vector has this property with high probability). Let $B=A^{T}A=V\Sigma^{2}V^{T}$. Define $x_{k}=B^{k}x$, the result of $k$ applications of $B$ to $x$. Then as long as $\sigma_{1}(A)>\sigma_{2}(A)$, the limit $\lim_{k\to\infty}\frac{x_{k}}{\|x_{k}\|}=v_{1}$.

**Proof.** I will use $\sigma_{i}$ as a shorthand for $\sigma_{i}(A)$. First expand $x$ in terms of the singular vectors $x=\sum_{i=1}^{n}c_{i}v_{i}$. Applying $B$ gives $Bx=\sum_{i=1}^{n}c_{i}\sigma_{i}^{2}v_{i}$. Applying it repeatedly gives

$$x_{k}=B^{k}x=\sum_{i=1}^{n}c_{i}\sigma_{i}^{2k}v_{i}.$$

Notice that, since $\sigma_{1}$ is larger than $\sigma_{2}$ (and hence all other singular values), the coefficient for $\sigma_{1}$ grows faster than the others. Normalizing $x_{k}$ causes the coefficient of $\sigma_{1}$ to tend to $1$ while the other coefficients tend to $0$. ∎

The intuition to glean from this proof is that $B=A^{T}A$, when applied to a vector, "pulls" that vector a little bit toward the top singular vector. If you normalize after each step, then the magnitude of the vector doesn't change, but the direction does.

The relevant quantity tracking the coefficient growth is the ratio between the two biggest singular values, $\left(\sigma_{1}/\sigma_{2}\right)^{2k}$. Even if $\sigma_{1}$ is only marginally bigger, say $\sigma_{1}=(1+\varepsilon)\sigma_{2}$, the resulting growth rate is exponential in the number of iterations. The bigger the gap, the swifter the convergence. Most importantly, this lets us compute! Solving the $1$-dimensional optimization problem is now as simple as computing a matrix-vector product and normalizing at each step.

### Code It Up

Here's the Python code that solves the one-dimensional problem, using the numpy library for matrix algebra. Note that numpy uses the `dot` method for all types of matrix-matrix and matrix-vector and inner product operations. Also note the `.T` property returns the transpose of a matrix or vector. The full file defines a function that produces a random unit vector and then the core subroutine `svd_1d`, which implements the power method exactly as the theorem describes—repeatedly apply $B$, normalize, and stop once the iterate's angle barely changes. We run it on Kun's movie-rating matrix and cross-check the recovered singular vector and value against numpy's battle-tested SVD.

```python
<!-- include: code/pim/06 - Linear Algebra/05_power_method.py -->
```

```
power method converged in 6 iterations
first singular vector v1 = [0.5418 0.6707 0.5065]
agreement with numpy's v1 (|cos|): 1.0
sigma_1 = ||A v1|| = 15.096269 (numpy: 15.096269 )
```

Since, as we saw in Chapter 8, the sequence will never *quite* achieve its limit, we stop after $x_{k}$ changes its angle (as computed using the inner product) by less than some threshold.

Now we can use the one-dimensional subroutine to compute the entire SVD. The helper we need is how to exclude vectors in the span of the singular vectors you've already computed. Unfortunately, to solve this opens up questions about a new topic, namely the rank of a matrix, which I've found hard to fit into this already very long chapter. As much as it hurts me to do so, we will save it for an exercise, and present the formula here.

The idea is this: to exclude vectors in the span of the first singular vector $v_{1}$ with corresponding $u_{1}$, subtract from the original input matrix $A$ the rank-$1$ matrix $B_{1}$ defined by $b_{i,j}=u_{1,i}v_{1,j}$ (the product of the $i$-th and $j$-th entries of $u_{1},v_{1}$, respectively). The name for this matrix is the "outer product" of $u_{1}$ and $v_{1}$, and it's closely related to a concept called the *tensor product*. Likewise, you can define $B_{i}$ for each of the singular vectors $v_{i}$. To exclude all the vectors in the span of $\{v_{1},\ldots,v_{k}\}$, you replace $A$ with $A-\sum_{i=1}^{k}B_{i}$.

The full `svd` function does this iteratively: it loops over the singular triples found so far, subtracts off each outer product $\sigma_i \, u_i v_i^T$, and feeds the leftover signal back into `svd_1d` to extract the next triple. The demo runs Kun's greedy `svd` on the movie matrix, confirms the singular values match numpy exactly, and rebuilds $A = U\Sigma V^T$ from the from-scratch pieces.

```python
<!-- include: code/pim/06 - Linear Algebra/07_svd_from_scratch.py -->
```

```
singular values from scratch: [15.0963  4.3006  3.407 ]
match numpy singular values: [15.0963  4.3006  3.407 ]
U Sigma V^T rebuilds the rating matrix exactly
```

Let's run this on some data. Specifically, we'll analyze a corpus of news stories and use SVD to find a small set of "category" vectors for the stories. These can be used, for example, to suggest category labels for a new story not present in our data set. We'll sweep a lot of the data-munging details under the rug (see the Github repository for full details), but here's a summary:

1. Scrape a set of 1000 CNN stories, and a text file `one-grams.txt` containing a list of the most common hundred-thousand English words. These files are in the data directory of the Github repository.
2. Using the natural language processing library nltk, convert each CNN story into a list of (possibly repeated) words, excluding all stop words and words that aren't in `one-grams.txt`. The output is the file `all-stories.json`.
3. Convert the set of all stories into a document-term matrix $A$, with $m$ rows (one for each word) and $n$ columns (one for each document), where the $a_{i,j}$ entry is the count of occurrences of word $i$ in document $j$.

Then we run SVD on $A$ to get a low-dimensional subspace of the vector space of words, in our case a 10-dimensional subspace. If the above recipe is factored out into functions, then the entire routine is:

```python
data = load(filename)
matrix, (index_to_word, index_to_document) = (
    make_document_term_matrix(data))
matrix = normalize(matrix)
sigma, U, V = svd(matrix, k=10)
```

Here `U` is the basis for the subspace of documents, `V` for the words. However, these basis vectors are very difficult to understand! If we go back to our interpretation of such a word vector as an "idealized" word, then it's a "word" that best describes some large set of documents in our linear model. It's represented as a linear combination of a hundred thousand words!

To clarify, we can project the existing words onto the subspace, and then we can cluster those vectors into groups and look at the groups. Here we use a black-box clustering algorithm called `kmeans2`, provided by the scipy library.

```python
projectedDocuments = np.dot(matrix.T, U)
projectedWords = np.dot(matrix, V.T)

documentCenters, documentClustering = kmeans2(projectedDocuments)
wordCenters, wordClustering = kmeans2(projectedWords)
```

Once we've clustered, we can look at the output clusters and see what words are grouped together. As it turns out, such clusters often form topics. For example, after one run the clusters have size:

```python
>>> Counter(wordClustering)
Counter({1: 9689, 2: 1051, 8: 680, 5: 557, 3: 321,
         7: 225, 4: 174, 6: 124, 9: 123})
```

The first cluster, as it turns out, contains all the words that don't fit neatly in other clusters—such as "skunk," "pope," and "vegan"—which explains why it's so big. The other clusters have more reasonable interpretations. For example, after one run the second largest cluster contained primarily words related to crime:

```python
>>> print(wordClusters[1])
['accuse', 'act', 'affiliate', 'allegation', 'allege', 'altercation',
 ... 'dead', 'deadly', 'death', 'defense', 'department', 'describe',
 ... 'investigator', 'involve', 'judge', 'jury', 'justice', 'kid',
 'killing', ...]
```

This is just as we'd expect, because crime is one of the largest news beats. Other clusters include business, politics, and entertainment. We encourage the reader to run the code themselves and inspect the output.

A natural question to ask is why not just cluster to begin with? Efficiency! In this model, each word is a vector of length 1000 (one entry for each story), and each document has length 100,000! Clustering on such large vectors is slow. But after we compute the SVD and project, we get clusters of length $k=10$. We trade off accuracy for efficiency, and the SVD guarantees us that it's extracting the most important (linear) features of the data. Because of this, SVD is often called a "dimensionality reduction" algorithm: it reduces the dimension of the data from their natural dimension to a small dimension, without losing too much information.

But there's more to the story. Recall our modeling assumption, that word meanings "have the structure of" a low-dimensional vector space, but the values we see are perturbed by some noise. A crime story might use the word "baseball" for idiosyncratic reasons, but most crime stories do not. The low-dimensional subspace captures the "essence" of the data, ignoring noise, and the projection of the input word vectors onto the SVD subspace provides a "smoothed" representation of the data. This new representation has some strikingly useful properties, which are a direct consequence of the linear model doing its job well in representing the most influential aspects of the English language.

Before I explain what that means, I need a caveat. What I'm about to describe doesn't strictly work for the code presented in this chapter. Since I wrote this code with the goal to group news articles by topic, I counted frequency of terms occurring in documents (and the dataset I used is quite small!). If you want to reproduce the behavior below, you need a larger dataset and a different preprocessing technique, which is basically to count how often word pairs co-occur in a document. Check out Chris Moody's lda2vec, which does this.

Now the fun stuff. The vector representation of words produced by the SVD has a semantic linear structure. For example, if you take the vector for the word "king," subtract the vector for "man" and add the vector for "woman," the result approximates the vector for "queen." Indeed, the SVD representation has reproduced the gender aspect of language. This occurs for all kinds of other properties of words that fit into typical word-association style tests like "Paris is to France as Berlin is to…"

We can make the "king − man + woman ≈ queen" phenomenon concrete with a miniature example. We secretly place six words at latent positions along two axes (royalty and femaleness), generate noisy co-occurrence counts that are a linear image of those positions, then run the SVD and keep the top two components. The recovered embedding has exactly the additive structure Kun describes—the analogy arithmetic lands on the right word.

```python
<!-- include: code/pim/06 - Linear Algebra/08_word_vectors.py -->
```

```
king - man + woman  ->  queen  (cos 1.000)
prince - man + woman -> princess
Semantic meaning is roughly additive -- the SVD found it.
```

This is surprising, and it tells us that some aspect of this SVD representation of words is much better than the original input of raw word counts. It's surprising because we think of language as a highly quirky, strange, perhaps nonlinear thing. But when it comes to the relationships between words, or the semantic meaning of document topics, these linear methods work well. One might argue that the core insight behind this is that for language, context is linear in nature. And then it's immediately clear why this works: if you see a document with "child" and "she" in it, and those words occur close together, you intuitively know that you're more likely to be talking about a daughter than a son. Replace the "she" with a "he" and you expect to see the word son instead. The SVD captures this.

This fascinates me philosophically. Because while I certainly unconsciously understood that semantic meaning is roughly additive, I never consciously knew it until I saw these linear models and asked why they work. Math imitates life, but it can also teach us about life as it drives us to explore, refine, and build. In fact, I was confused for a long time because the original "additive word vector" ideas came from neural network research, which typically involves models that are highly nonlinear. It wasn't until I talked with some experts in natural language processing that the additive roots of the model became apparent.

## Cultural Review

1. The heart of linear algebra is a very concrete connection between linear maps and matrices. The former is intuitive, useful for thinking about linear algebra geometrically. The latter is computationally tractable, allowing us to discover and apply useful algorithms. Operations on linear maps, such as function composition, correspond pleasingly to operations on matrices, such as matrix multiplication.
2. Coordinate systems are arbitrary, and linear algebra gives you the power to change coordinate systems—change the basis of the vector space—at will. A useful basis is a treasure.
3. The matrix representation hides the difficult notation of working with linear maps, reducing the cognitive burden of the mathematician.
4. The linear model is a powerful abstraction for working with real-world data, and understanding linear algebra allows us to pinpoint the assumptions of this model, and in particular where those assumptions might break down or limit the applicability of the model.

## Exercises

### Vector Spaces and Linear Maps

1. Prove that $0$ (the zero vector) is unique; that is, if there are two vectors $v$, $w$ both having the properties of the zero vector, then they are equal.
2. Prove that the composition of two linear maps is linear. I.e., the map $x\mapsto g(f(x))$ is linear if $g$ and $f$ are linear.
3. Prove that if a linear map $f$ is a bijection, then the inverse $f^{-1}$ is also a linear map.
4. Let $V,W$ be two vector spaces. Show that the direct product $V\times W$ is also a vector space by defining the two operations $+$ and $\cdot$. How does the dimension of $V\times W$ compare to the dimensions of $V$ and $W$?
5. Prove that the image of a linear map $f:V\to W$ is a subspace of the codomain, $W$. Prove that the subset $\{v\in V:f(v)=0\}$ is a subspace of $V$.
### Matrices and Geometric Transformations

6. In $\mathbb{R}^{2}$ we have colorful names for special classes of linear maps that correspond to geometric transformations. Look up definitions and pictures to understand matrices that perform rotation, shearing, and reflection through a line.
7. Research definitions and write down examples for the following concepts:
   1. The column space and row space of a matrix.
   2. The rank of a matrix.
   3. The rank-nullity theorem.
   4. The outer product of two vectors.
   5. The direct sum of two subspaces of a vector space.
8. Prove that the standard inner product on $\mathbb{R}^{n}$ (Definition 10.18) is linear in the first input. I.e., if you fix $y\in\mathbb{R}^{n}$, then $\langle x,y\rangle:\mathbb{R}^{n}\to\mathbb{R}$ is a linear map. Argue by symmetry that the same is true of the second coordinate.
9. Prove that for two matrices $A,B$, we have $(AB)^{T}=B^{T}A^{T}$.
### Bases, Interpolation, and Polynomials

10. Given two (possibly negative) integers $a,b\in\mathbb{Z}$, the Fibonacci-type sequence is a sequence $f_{a,b}(n)$ defined by
    $$f_{a,b}(0)=a,\quad f_{a,b}(1)=b,\quad f_{a,b}(n)=f_{a,b}(n-1)+f_{a,b}(n-2)\ \text{for }n>1.$$
    Prove that the set of all Fibonacci-type sequences form a vector space (under what operations?). Find a basis, and thus compute its dimension.
11. In Chapter 2 we defined and derived an algorithm for polynomial interpolation. Reminder: given a set of $n+1$ points $(x_{0},y_{0}),\ldots,(x_{n},y_{n})$, with no two $x_{i}$ the same, there is a unique degree-at-most-$n$ polynomial passing through those points. Rephrase this problem as solving a matrix-vector multiplication problem $Ay=x$ for $y$. Hint: $A$ should be an $(n+1)\times(n+1)$ matrix.
12. Again in Chapter 2, return to exercise 2.9 on Newton interpolation. Find a source that explains how Lagrange and Newton interpolation correspond to solving matrix inversion problems using different bases for a vector space of polynomials.
13. The Bernstein basis is a basis of the vector space of polynomials of degree at most $n$. In an exercise from Chapter 2, you explored this basis in terms of Bézier curves. Like Taylor polynomials, Bernstein polynomials can be used to approximate functions $\mathbb{R}\to\mathbb{R}$ to arbitrary accuracy. Look up the definition of the Bernstein basis, and read a theorem that proves they can be used to approximate functions arbitrarily well.
### Computational Linear Algebra

14. Look up the process of Gaussian Elimination, and specifically pay attention to the so-called elementary row operations. Each of these operations corresponds to a change of basis, and is hence a matrix. Write down what these matrices are for $\mathbb{R}^{3}$, and realize that every change of basis matrix is a product of some number of these elementary matrices.
15. The LU decomposition is a technique related to Gaussian Elimination which is much faster when doing batch processing. For example, suppose you want to compute the basis representation for a change of basis matrix $A$ and vectors $y_{1},\ldots,y_{m}$. One can compute the LU decomposition of $A$ once (computationally intensive) and use the output to solve $Ax=y_{i}$ many times quickly. Look up the LU decomposition, what it computes, read a proof that it works, and then implement it in code.
16. A linear program is an optimization problem specified by minimizing a linear function of many variables, subject to linear inequality constraints. Linear programs are a workhorse of the supply chain industry. Research the formal specification of a linear program, and find some natural problems that can be cast as a linear program. If you struggle to find one, look up the Stigler Diet.
17. Continuing the previous exercise, the classical algorithm for solving linear programs is called the simplex method. It was invented in the 1940's by George Dantzig. At its core, the algorithm builds up a vector space basis corresponding to the variables in the solution that have nonzero values. Then it iteratively uses the objective (and Gaussian-elimination-style elementary row operations) to guide how to improve the solution. Research this algorithm and implement it in its basic form.
### Inner Products, Matroids, and SVD

18. Look up the definition of an inner product space (a vector space equipped with an inner product), and the definition of an isometry between two inner product spaces. Find, or discover yourself, the aforementioned proof that all $n$-dimensional inner product spaces are isometric.
19. Linear independence has applications and generalizations all over mathematics. One fruitful area is the concept of a matroid. Matroids have a special place in computer science, because they are the setting in which one studies greedy algorithms in general. That is, every problem that can be solved optimally with a greedy algorithm corresponds to some matroid, and every matroid can be optimized using the greedy algorithm. Look up an exposition on matroids and understand this correspondence. Apply this to the problem of finding a minimum spanning tree in a weighted graph. See Chapter 6, Exercise 6.12 for an introduction to weighted graphs.
20. The $k$-means clustering algorithm is an algorithm for splitting a set of $n$ vectors $\{x_{1},\ldots,x_{n}\}\subset\mathbb{R}^{d}$ into $k<n$ sets. The algorithm works as follows: choose $k$ random input vectors that are considered as "centers" of their clusters. Then repeat the following: label each vector $x_{i}$ with its closest center ("assign" the vector to that cluster). Then compute a new center for each cluster as the center of all the vectors in the cluster (add up all the vectors and divide by the number of vectors added). Repeat this until there is a round in which the centers don't change, or you exceed a predetermined number of rounds. Look up this algorithm and read about what goal it's trying to achieve, and how it can fail.
21. The singular value decomposition code in this chapter has at least one undesirable property: numerical instability. In general, numerical instability is when an algorithm is highly sensitive to small perturbations in the input. The SVD of a matrix which is not full rank (cf. Exercise 10.7) contains values that are zero. The algorithm in this chapter does not output these properly, and instead produces non-deterministic mumbo-jumbo. Audit the algorithm to verify this undesirable behavior occurs, and research a fix.
22. Research the details of the winning submission for the Netflix Prize competition. Identify what other ways a linear model is incorporated into the solution.

## Chapter Notes

### Vector Spaces, Rigorously

The rigorous definition of a vector space first requires a rigorous definition of the scalar type, which goes by the name of field.

**Definition 10.27.** A field is a set $K$ with addition $+:K\times K\rightarrow K$ and multiplication $\cdot:K\times K\rightarrow K$ (or just juxtaposition) operations having the following properties.

- Both operations are commutative and associative.
- Addition and multiplication have identity elements which are distinct. Call them zero and one, respectively.
- Addition and multiplication both have inverses, and every element is invertible, with the exception that zero has no multiplicative inverse.
- Multiplication distributes over addition, i.e. $x\cdot(y+z)=(x\cdot y)+(x\cdot z)$ for all $x,y,z\in K$.

The field is the triple $(K,+,\cdot)$, or just $K$ if the operations are clear from context.

By convention, multiplication has higher operator precedence than addition, regardless of the definition of the operations. The letter $K$ stands for Körper, the German term for this mathematical object (which literally translates to "body"). Obviously, $\mathbb{R}$ is a field, but there are many others. For example, the set of fractions of integers (rational numbers) forms a field denoted $\mathbb{Q}$ with the normal addition and multiplication. Another example is the binary field $\{0,1\}$ with the logical AND and OR operations.

Now a vector space can be defined so that its scalars come from some field $K$ in the same way we used scalars from $\mathbb{R}$. We say that $V$ is a vector space over $K$ to mean that the scalars come from $K$. As long as the operations in $K$ have the properties outlined above, you can do all the same linear algebra we've done in this chapter. To be particularly clear, a linear combination of vectors in $V$ requires coefficients coming from $K$, and so they're called $K$-linear combinations. Also note that $K$-linear combinations must be finite sums.

Linear algebra can have more nuance for some special fields, but to understand when and how they are different you need to study a bit of field theory. If you're interested, look up the notion of field characteristic and in particular what happens when fields have characteristic $2$.

To leave you with one example of an interesting vector space over a field that's not $\mathbb{R}$, consider $V=\mathbb{R}$ as a vector space over $K=\mathbb{Q}$. This might not seem interesting at first until you ask what a basis might be. Take the set $C=\{1,2,3,4,5\}$, for example. Is it possible to write $\pi$ (an element of $V$) as a $\mathbb{Q}$-linear combination of the vectors in $C$? You could only do so if $\pi$ itself was rational, which it's not. So how, then, might one find a basis so that $\pi$ (and every other irrational number) can be written as a finite $\mathbb{Q}$-linear combination of the elements in the basis? A curious thought indeed.

### Bias in Word Embeddings

The process of turning English language words into vectors in such a way that arithmetic on vectors corresponds to semantic transformations of words ("king" − "man" + "woman" = "queen") is called semantic word embedding. This approach has roots in linguistics and information retrieval, and was popularized in computer science in the early 2000's by Yoshua Bengio and others. In 2013, Google released an open source tool called "word2vec" that constructs embeddings using neural networks, and there are many other tools (such as GloVe) that have become popular since then.

Semantic word embeddings are an interesting case study into the shortcomings of linear models. In a 2016 paper, "Man is to Computer Programmer as Woman is to Homemaker?" a team of researchers at Microsoft Research studied how human bias expressed itself through word embeddings. Here a corpus of documents is used to train a linear model, in which pairs of words like "woman" and "receptionist" show up more often than, say, "woman" and "architect." These associations (intended or not) will manifest themselves in the resulting embedding. As a consequence, any system based on these word embeddings is likely to associate women with receptionists more than architects. This outcome is not surprising, considering the adage, "a word is characterized by the company it keeps."

Whether one is willing to accept this outcome depends on the goal of the application, but awareness is crucial. Mathematical assumptions baked into algorithms and models—even simple ones like linearity—can dupe the unwitting. Take care when applying them to situations that involve people's lives or livelihoods.
