# Multivariable Calculus and Optimization

> The world is continuous, but the mind is discrete.
>
> —David Mumford

Much of practical applied mathematics revolves around optimization. Financial math optimizes cost and revenue, supply chains optimize routing and allocation of resources, and machine learning optimizes generalization error from training examples. These complex problems can be modeled using multi-input, multi-output functions composed of simple, differentiable pieces. Constructing good models is hard. But once a model is agreed upon, we optimize it with calculus.

Calculus generalizes nicely from one dimension (Chapter 8) to many dimensions. In particular, the idea that a function can be linearly approximated at a point generalizes to the so-called total derivative. Because we have multiple input variables, the total derivative is a multivariable linear function, i.e., a linear map. With some work—and dipping back into the single-variable setting momentarily—we'll show that its computation reduces to the easy problem of computing single-variable derivatives. And finally, we'll take advantage of the geometry we established with the inner product to interpret the total derivative geometrically, which will result in a natural optimization technique called gradient descent.

As the application for this chapter, we'll write a neural network from scratch. We'll define the so-called computation graph of a function, and optimize its parameters using the chain rule and gradient descent. We'll apply this to the classic problem of classifying handwritten digits. Along the way, we'll get a whirlwind introduction to the theory and practice of machine learning.

## Generalizing the Derivative

Let's start with our fond memories of single-variable calculus. Recall Definition 8.6 of the derivative of a single-variable function.

**Definition 14.1.** Let $f:\mathbb{R}\rightarrow\mathbb{R}$ be a function. Let $c\in\mathbb{R}$. The derivative of $f$ at $c$, if it exists, is the limit

$$f'(c) = \lim_{x \rightarrow c} \frac{f(x) - f(c)}{x - c}$$

On the real line, we defined the symbolic abstraction $x \to c$ to mean "any sequence $x_{n}$ that converges to $c$," where we declared the derivative only exists if the limit doesn't depend on the choice of sequence. When we work in $\mathbb{R}^n$ (which, among many other properties, has a nice measure of distance for vectors $d(x,y) = \| x - y\|$) the notion of a convergent sequence generalizes seamlessly. A sequence of vectors $x_{1},x_{2},\dots \in \mathbb{R}^{n}$ converges to $c \in \mathbb{R}^n$ if the sequence $d_{n} = \| x_{n} - c\|$ of real numbers converges to zero.

Despite sequence convergence generalizing, the obvious first attempt to adapt the derivative violates well-definition. We might try the same formula as Definition 14.1, interpreting $x$ and $c$ as vectors, and using the norm in the denominator. Unfortunately, the "value" of this derivative depends on the sequence chosen.

An easy example demonstrates. The function $f(x_{1},x_{2}) = -x_{2}^{2}$, and the two sequences $x_{n} = (1 + \frac{1}{n},1)$ and $x_{n}' = (1,1 + \frac{1}{n})$. Both sequences converge to $(1,1)$, but because $f$ depends on the second coordinate quadratically, (and doesn't depend on the first coordinate at all!) the direction along which $x_{n}'$ approaches is steeper than that of $x_{n}$. Using the former for "the derivative" would result in something like $\lim_{n\to \infty}\frac{-1 + 1}{(1 / n)} = 0$, while the latter would be $\lim_{n\to \infty}\frac{-1 - (2 / n) - (1 / n^2) + 1}{(1 / n)} = -2$. This is illustrated in Figure 14.1.

![Figure 14.1: The steepness of a surface depends on the direction you look. Two sequences approach $(1,1)$: along the dashed path $(1+1/n,\,1)$ the surface is flat (slope $0$), while along the solid path $(1,\,1+1/n)$ it falls steeply (slope $-2$).](08 - Multivariable Calculus and Optimization_images/img-0.jpeg)

This is exactly the sort of claim worth confirming numerically before trusting it. The naive vector "derivative" returns two different limits along Kun's two sequences—so it cannot be the derivative.

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/01_directional_derivative_sequences.py -->
```

We are right to be suspicious. With multiple variables, the underlying idea of "steepness" now inherently depends on direction. This is something one intuitively understands from the natural world; a hiker traverses switchbacks to avoid walking straight up a hill, and a skier skis in an S shape to slow down their descent. In fact, for $f(x_{1},x_{2})=-x_{2}^{2}$, and standing at the point $(1,1)$, every direction provides a slightly different slope.

This suggests one intuitive way to generalize the one-dimensional definition of the derivative: parameterize by the direction of approach.

**Definition 14.2.** The directional derivative of a function $f:\mathbb{R}^{n}\to\mathbb{R}$ at a point $c\in\mathbb{R}^{n}$ in the direction of a unit vector $v\in\mathbb{R}^{n}$ is the limit

$$\operatorname{Dir}(f,c,v)=\lim_{t\to 0}\frac{f(c+tv)-f(c)}{t}$$

If this limit exists, we say $f$ is differentiable at $c$ in the direction of $v$.

So instead of allowing a sequence to approach the point of interest from any direction, we restrict it to the line through the direction $v$ we're interested in. Here we're using $t\to 0$ to denote any sequence $t_{n}\in\mathbb{R},t_{n}\neq 0$ which converges to zero.

In Chapter 8 we started with the derivative and developed an optimal linear approximation that was easy to compute. That was extremely useful. Now we ask, how can we compute a similar linear approximation of a multivariable function? The directional derivative alone falls short. The corkscrew surface shown in Figure 14.2 illustrates the problem.

On this surface at $(0,0)$, the directional derivative exists in every direction, but jumps sharply as the direction rotates past the negative $x_{1}$ axis. In the technical parlance we left to Exercises 8.1 and 14.1 to define, the directional derivative isn't continuous with respect to direction. Informally, if I stand at the origin and look directly in the direction of the jump (a ray down the negative $x_{1}$-axis), then as my gaze perturbs left and right by any infinitesimally small amount, my view of the steepness of the surface jumps drastically from very steeply negative to very steeply positive. This destroys the possibility that a derivative based on the directional derivative can serve as a global approximation to $f$ near $(0,0)$. It will err egregiously in the vicinity of the jump.

![Figure 14.2: A corkscrew function, demonstrating that directional derivatives need not be continuous as the direction changes.](08 - Multivariable Calculus and Optimization_images/img-1.jpeg)

As we'll see soon, a stronger derivative definition avoids these issues. It will provide a linear map representing the whole function, and applying linear algebra produces the directional derivative in any direction. Being linear algebra, we may choose a beneficial basis, though I haven't yet made it clear what the vector space in question is. That will come as we refine what the right definition of "the" derivative should be.

## Linear Approximations

For dimension 1, the derivative of $f$ had the distinction of providing the most accurate line approximating $f$ at a point. The line through $(c,f(c))$ with slope $f'(c)$ is closer to the graph of $f$ near $c$ than any other line. We proved this in detail in Theorem 8.11.

This approximator is more than just a line. It's a linear map, and now that we have the language of linear algebra we can discuss it. Define by $L_{f,c}$ the linear map $L_{f,c}(z) = f'(c)z$. As input, this linear map takes a (one-dimensional) vector $z$ representing a deviation from $c$. The output is the derivative's approximation of how much $f$ will change as a result. The matrix for $L_{f,c}$ is the single-entry matrix $[f'(c)]$. Moreover, $L_{f,c}(z)$ is exactly the first-degree Taylor polynomial for the version of $f$ that gets translated so that $(c, f(c))$ is at the origin. Figure 14.3 shows the difference.

If you don't like shifting $f$ to the origin, we can define the affine linear map (affine just means a translation of a linear map away from the origin), which we'll call a linear approximation to $f$.

**Definition 14.3.** Let $f: \mathbb{R} \to \mathbb{R}$ be a single-variable differentiable function. Then the linear approximation to $f$ at a point $c \in \mathbb{R}$ is the affine linear map

$$L_{c}(x) = f'(c)(x - c) + f(c).$$

That is, $L_{c}(x)$ is the degree-1 Taylor approximation of $f$ at $c$.

<!-- carousel -->
![Figure 14.3 (left): A linear approximation to $f$ without shifting—the tangent line through $(c, f(c))$.](08 - Multivariable Calculus and Optimization_images/img-2.jpeg)
![Figure 14.3 (right): The same approximation shifted so that $(c, f(c))$ is at the origin, exposing it as the pure linear map $L_{f,c}(z) = f'(c)z$.](08 - Multivariable Calculus and Optimization_images/img-3.jpeg)
<!-- endcarousel -->

The linear approximator has the following property, which is a restatement of the limit definition of the derivative.

**Proposition 14.4.** For any differentiable $f: \mathbb{R} \to \mathbb{R}$ and its linear approximation $L_{c}(x)$,

$$\lim_{x \rightarrow c} \frac{f(x) - L_{c}(x)}{x - c} = 0$$

**Proof.** Split the limit into two pieces:

$$\lim_{x \rightarrow c} \frac{f(x) - f(c)}{x - c} - \lim_{x \rightarrow c} \frac{f'(c)(x - c)}{x - c} = f'(c) - f'(c) = 0$$

$\blacksquare$

I spell this out in such detail because the existence of a linear approximator (an affine linear function satisfying 14.4) becomes a definition for functions $\mathbb{R}^n\to \mathbb{R}$.

**Definition 14.5.** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a function. We say $f$ has a total derivative at a point $c \in \mathbb{R}^n$ if a linear map $A: \mathbb{R}^n \to \mathbb{R}$ exists such that the affine linear function defined by $L_c(x) = A(x - c) + f(c)$ (which depends on $A$) satisfies

$$\lim_{x \rightarrow c} \frac{f(x) - L_{c}(x)}{\| x - c \|} = 0$$

If such an $A$ exists, we call $L_{c}$ a linear approximation of $f$ at $c$, and $A$ a total derivative of $f$ at $c$.

In this definition, we again allow $x \to c$ to mean "any sequence $x_{n} \neq c$ converging to $c$." Because that's exactly the point! If no proposed linear map works due to a devious choice of approaching sequence, then the function doesn't have the property we want. There is no consistent way to have a linear approximation to $f$ (ignoring how good or bad such an approximation might be). This rules out the confounding corkscrew example. The jump in the directional derivative violates Definition 14.5.

If the definition is satisfied, then near $c$ the function $f$ can be approximated by a linear map $A$. The term $A(x - c)$ makes the linear map apply to deviations from $c$. Equivalently, the shift by $-c$ translates $f$ to the origin to apply $A$, and the addition of $f(c)$ translates back to $(c, f(c))$. $L$ and $A$ are related by the conjugation of these two translations.

![Figure 14.4: The linear subspace defined by the total derivative of $f$ sits tangent to the surface of $f$ at the point the total derivative is evaluated at. Shown here: the tangent plane to $f(x,y) = -x^{2} - y^{2}$ at $(x,y) = (1,1)$.](08 - Multivariable Calculus and Optimization_images/img-4.jpeg)

Geometrically in two dimensions, the linear approximation defines a plane touching the graph of the surface $z = f(x,y)$ at the point $(c,f(c))$. If the limit above holds, then no matter the direction of approach, the steepness of $f$ matches the slope of the plane in that direction. If $f$ has discontinuous jumps, then the linear approximator can only line up with $f$ on one side of the jump. Figure 14.4 shows an example of the tangent plane to $f(x,y) = -x^{2} - y^{2}$ at $(x,y) = (1,1)$.

The computational centerpiece of Definition 14.5 is the linear map $A$. It helps conceptually to isolate $A$ and ignore the shifting by $c$ and $f(c)$ in a principled manner. Let's do this now. We want to make the linear map $A$ the focus of our analysis, and here's how we'll do that. For every point $c \in \mathbb{R}^n$, we "attach" a copy of the vector space denoted $T_f(c) = \mathbb{R}^n$ to $(c, f(c))$, and we call it the tangent space of $f$ at $c$. The tangent space is the set of inputs to $A$. Because we view $T_f(c)$ as "attached" to $f$ at $(c, f(c))$, as in Figure 14.4, we declare the tangent space's origin to be $(c, f(c))$. From that perspective, the linear approximation of $f$ at $c$ is just a linear map $T_f(c) \to \mathbb{R}$, without the shifting by $c$ and $f(c)$.

It's worthwhile to do some concrete examples. First in one dimension, then in three. For single-variable functions $f:\mathbb{R}\to\mathbb{R}$, at every point $c$ the tangent space is a one-dimensional vector space. The vectors in the vector space represent left/right deviations of the input of $f$ from $c$, and the linear map $A$ describes the approximate change in $f$ due to this deviation. As an example, let $f(x)=2+\sqrt{x+2}$ and consider the point $(c,f(c))=(2,4)$. The derivative of $f$ is $1/(2\sqrt{x+2})$, which evaluates to $1/4$ at $c=2$. Thus, the tangent space $T_{f}(2)$ is a copy of $\mathbb{R}$, and the total derivative at $c=2$ is $A(x)=\frac{1}{4}x$. The affine linear map is $L(x)=\frac{1}{4}(x-2)+4$.

In three dimensions, let $f(x,y,z)=x^{2}+(y-1)^{3}+(z-2)^{4}$ and let $c=(3,2,1)$. The tangent space $T_{f}(c)=\mathbb{R}^{3}$, and so the total derivative $A:\mathbb{R}^{3}\to\mathbb{R}$ has three-dimensional inputs. We won't learn how to compute this map from the definition of $f$ until the "Computing the Total Derivative" section, so for now we give the answer magically; it's the following $1\times 3$ matrix:

$$A=\begin{pmatrix}6&3&-4\end{pmatrix}.$$

And as a result

$$\begin{aligned}L(x,y,z)&=A(x-3,y-2,z-1)+f(3,2,1)\\&=6(x-3)+3(y-2)-4(z-1)+11.\end{aligned}$$

Many elementary calculus books have students compute this ("the equation of the plane tangent to the surface of $f$") as something of an afterthought, ignoring that it is the conceptual centerpiece of the derivative. Next we turn to some questions of consistency of the definition of the total derivative.

**Proposition 14.6.** The total derivative is unique.

**Proof.** Suppose there are two functions $L_{A}$ with matrix $A$ and $L_{B}$ with matrix $B$ that are both total derivatives of $f$ at $c$. We will show that $A=B$, and hence that $L_{A}=L_{B}$.

First, notice the difference of the two defining limits of the total derivative is related to the difference between $B$ and $A$. Below, $L_{B,c}(x)=B(x-c)+f(c)$ and likewise for $L_{A}$.

$$\begin{aligned}&\lim_{x\to c}\frac{f(x)-L_{B,c}(x)}{\|x-c\|}-\lim_{x\to c}\frac{f(x)-L_{A,c}(x)}{\|x-c\|}\\&=\lim_{x\to c}\frac{f(x)-[B(x-c)+f(c)]-f(x)+[A(x-c)+f(c)]}{\|x-c\|}\\&=\lim_{x\to c}\frac{(A-B)(x-c)}{\|x-c\|}\end{aligned}$$

Since both $L_{A}$ and $L_{B}$ are total derivatives, both of their defining limits exist and are zero. This reduces the above to

$$0=\lim_{x\to c}\frac{(A-B)(x-c)}{\|x-c\|}$$

Assume to the contrary that $B\neq A$. Then there must be some unit vector $v\in\mathbb{R}^{n}$ for which $(A-B)v\neq 0$. Define the sequence $x_{k}\to c$ by $x_{k}=c+(1/k)v$. Then, noting the change in limit index from $x$ to $k$,

$$\lim_{x\to c}\frac{(A-B)(x-c)}{\|x-c\|}=\lim_{k\to\infty}\frac{(1/k)(A-B)v}{\|(1/k)v\|}=(A-B)v\neq 0.$$

This is a contradiction, and hence $A=B$, completing the proof. $\blacksquare$

This validates us calling the total derivative the total derivative. There is no other linear map that can satisfy the defining property. As such, we can define a more convenient notation for the total derivative.

**Definition 14.7.** Define the notation $Df(c)$ to mean the total derivative matrix $A$ of $f$ at the point $c$.

A quick note on notation, $D$ is a mapping from functions to functions, but the way it's written it looks like $c$ is an argument to a function called "Df". To be formal one might attempt to curry arguments. $D(f)(c)$ is a concrete matrix of real numbers, and $D(f)$ is a function that takes as input a point $c$ and produces a matrix as output. Mathematicians often drop the parentheses to reduce clutter, and even the evaluation at $c$ if this is clear from context. One might also subscript the $c$ as in $Df_{c}$, or use a pipe that usually means "evaluated at," as in $Df|_{x=c}$. We will stick to $Df(c)$, as it achieves a happy middle: just think of the total derivative of $f$ as being named $Df$.

Now we'd like to compute total derivatives. To make this process cleaner, we first deviate to generalize the derivative to functions $\mathbb{R}^{n}\to\mathbb{R}^{m}$.

## Vector-valued Functions and the Chain Rule

Comfort with linear algebra makes converting relevant definitions of single-output functions to multiple-output functions trivial. A function $f:\mathbb{R}^{n}\to\mathbb{R}^{m}$ consumes a vector $x=(x_{1},\ldots,x_{n})$ as before, and produces as output a vector

$$f(x)=(f_{1}(x),f_{2}(x),\ldots,f_{m}(x)).$$

Each $f_{i}:\mathbb{R}^{n}\to \mathbb{R}$ stands on its own as a function. Moreover, if one defines $\pi_j:\mathbb{R}^m\to \mathbb{R}$ to be the function that extracts the $j$-th coordinate of its input, then $f_{i} = \pi_{i}\circ f$.[^1][^2]

The definition of the derivative is nearly identical with multiple outputs, but now all codomains are $\mathbb{R}^m$ and the limit numerator has a vector norm. The diff between Definitions 14.5 and 14.8 is literally four characters (two $m$'s in $\mathbb{R}^m$ and two $\|$'s).

**Definition 14.8.** Let $f: \mathbb{R}^n \to \mathbb{R}^m$ be a function. We say $f$ has a *total derivative* at a point $c \in \mathbb{R}^n$ if a linear map $A: \mathbb{R}^n \to \mathbb{R}^m$ exists such that the affine linear function defined by $L_c(x) = A(x - c) + f(c)$ (which depends on $A$) satisfies

$$\lim_{x \rightarrow c} \frac{\| f(x) - L_{c}(x) \|}{\| x - c \|} = 0$$

We again denote the linear map $A$ as $Df(c)$.

Proposition 14.6 on uniqueness can be rewritten almost verbatim for Definition 14.8. In most of the rest of this chapter, we'll restrict to the special case $m = 1$. However, the chain rule—a singularly powerful and beautiful tool that will guide our proofs and application—shines most brightly in arbitrary dimensions. It says that the derivative of a composition of two functions is the composition (product) of their total derivative matrices.

Note that this should not be surprising! The best linear approximation of a composition should naturally be the compositions of the best linear approximations of the composed functions. This formalizes it, and allows us to compute it using matrices.

**Definition 14.9.** Let $f: \mathbb{R}^n \to \mathbb{R}^m$ and $g: \mathbb{R}^m \to \mathbb{R}^k$ be two functions with total derivatives, and let $Df(c)$ be the total derivative matrix of $f$ at $c \in \mathbb{R}^n$ and $Dg(f(c))$ the matrix for $g$ at $f(c) \in \mathbb{R}^m$. Suppose that $Df$ and $Dg$ are represented in the same basis for $\mathbb{R}^m$. Then the total derivative of $g \circ f$ at $c \in \mathbb{R}^n$ is the matrix product $Dg(f(c))Df(c)$.

Restated with fewer parentheses, if $F$ is the total derivative matrix of $f$ at $c$, and $G$ is the total derivative of $g$ at $f(c)$, then the total derivative of $g \circ f$ at $c$ is $GF$.

This tidy theorem will be the foundation of our neural network application. It is not far off to say that all you need to train a neural network is "the chain rule with caching." However, we'll delegate the proof—it's admittedly technical and dull—to the chapter notes.

The chain rule is an extremely useful tool, and despite being abstract, it lands us within arms reach of our ultimate goal—easy derivative computations. In the next section, we'll see how finding these complicated matrices reduces to computing a handful of directional derivatives.

[^1]: The little circle $\circ$ denotes function composition.
[^2]: Mathematicians tend to call the function "extract the $i$-th coordinate" a projection onto the $i$-th coordinate. Because indeed, it's exactly the linear-algebraic projection onto the $i$-th basis vector. This is also why you'll see $\pi$ used as a function, since $\pi$ is the Greek "p," and "p" stands for projection.

## Computing the Total Derivative

Back to single-output functions, recall the total derivative at a point $c$ is a linear map $A: \mathbb{R}^n \to \mathbb{R}$, where the domain represents deviations from $c$. If we want to compute a matrix representation, a natural goal is to find a basis for which $A$ is easy to compute. We'll do this, and arrive at a matrix representation for $A$ (depending on $c$), by computing a small number of directional derivatives. First we'll show that the total derivative is closely related to directional derivatives.

**Theorem 14.10.** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a function with a total derivative at a point $c \in \mathbb{R}^n$. Let $\{v_1, \ldots, v_n\}$ be an orthonormal basis for $\mathbb{R}^n$, and recall that $\operatorname{Dir}(f, c, v)$ is the directional derivative of $f$ at $c$ in the direction of $v$. The matrix representation of the total derivative of $f$ with respect to the basis $\{v_1, \ldots, v_n\}$ is the $1 \times n$ matrix

$$\left(\operatorname{Dir}(f, c, v_{1}) \quad \operatorname{Dir}(f, c, v_{2}) \quad \dots \quad \operatorname{Dir}(f, c, v_{n})\right)$$

**Proof.** The proof is a clever use of the chain rule. We prove it first for $v_{1}$ and the first component, but the same proof will hold if $v_{1}$ is replaced with any $v_{i}$.[^3] Define by $g: \mathbb{R} \to \mathbb{R}^{n}$ the map $t \mapsto c + tv_{1}$. Then define $h(t) = f(g(t))$.

$$h: \mathbb{R} \xrightarrow{t \mapsto c + t v_{1}} \mathbb{R}^{n} \xrightarrow{f} \mathbb{R}$$

By the definition of the directional derivative, $h'(0) = Dh(0) = \mathrm{Dir}(f, c, v_1)$.[^4] Apply the chain rule to $h$, and get $Dh(0) = Df(c)Dg(0)$. Note $Df(c)$ is a $1 \times n$ matrix. Call $z_1, \ldots, z_n$ the unknown entries of $Df(c)$, written with respect to the basis $\{v_1, \ldots, v_n\}$. Also note that $Dg(0)$ can be written as an $n \times 1$ matrix with respect to the same basis (for the codomain of $g$):

$$Dg(0) = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$

The form of $Dg(0)$ is trivial: $t \mapsto tv_1$ has no coefficient of any other $v_i$ but $v_1$. Combining these, $Dh(0) = Df(c) \cdot Dg(0)$ is the $1 \times 1$ matrix $[z_1]$, proving $z_1 = \mathrm{Dir}(f, c, v_1)$. Doing this for each $v_i$ instead of $v_1$ establishes the theorem. $\square$

This proof easily adapts to functions $\mathbb{R}^n\to \mathbb{R}^m$, which we leave as an exercise.

[^3]: Note that if $f$ were not defined on all of $\mathbb{R}^n$—such as if it has a discontinuity or hole in its domain—this proof could be adapted by only defining $g$ on some small epsilon ball around $c$.
[^4]: I'm implicitly identifying $h'(0)$ with the $1 \times 1$ matrix $Dh(0)$.

Theorem 14.10 provides two pieces of insight. The first is that the directional derivative wasn't so far off from the "right" definition. For "nicely behaved" functions, the total derivative and the directional derivatives agree. There's even a theorem that relates the two: if the directional derivative is continuous with respect to the choice of direction, then the directional derivative matrix from Theorem 14.10 is the total derivative. That theorem implies that our initial corkscrew counterexample (with a jump as the direction rotates) is the only serious obstacle to exclusively using directional derivatives for computation. This theorem is important enough that it deserves offsetting, despite our negligence in providing a proof, as one can say something slightly stronger.

**Theorem 14.11.** Let $f:\mathbb{R}^{n}\to\mathbb{R}$ be a function and $c\in\mathbb{R}^{n}$ a point, and $\{v_{1},\ldots,v_{n}\}$ an orthonormal basis. Suppose that for every basis vector $v_{i}$ the directional derivative $\mathrm{Dir}(f,c,v_{i})$ is locally continuous in $c$, then $f$ has a total derivative given by the matrix in Theorem 14.10.

See the exercises for a deeper dive.

The second insight is that we can compute *any* directional derivative easily by first computing a small number of directional derivatives—one for each basis vector—and then simply projecting onto the direction of our choice. This projection is precisely the inner product with the vector of directional derivatives, or, for multiple output variables, the corresponding matrix multiplication. Projection works because it coincides with the way to express a vector in terms of an orthonormal basis (Proposition 12.15).

Speaking in terms of general bases is fine, and on occasion you'll find derivatives are easier to compute with a clever change of coordinates. However, it's usually easiest to use the same, simple basis: each basis vector is the standard basis vector for $\mathbb{R}^{n}$, and is denoted $dx_{i}$. This vector represents a change in a single input variable while leaving all others constant. If you have names for your variables, like $f(x,y,z)=x^{2}y+\cos(z)$, then you would use $dx$, $dy$, and $dz$. When we do examples, we'll stick to using $x_{i}$ and $dx_{i}$.

The standard basis is so useful because it allows one to define an easy computational rule of thumb. For a directional derivative for basis vector $dx_{2}$, you may consider all variables except $x_{2}$ to be constants, and then apply the same rules for single-variable derivatives to the function considered just as a function of $x_{2}$. If it helps, you can imagine a "curried" function $f(x_{1},x_{2},x_{3})=f(x_{1},x_{3})(x_{2})$, the former part of which closes over the fixed choices of values for $x_{1},x_{3}$. The values of $x_{1},x_{3}$ are fixed, but unknown at the time of derivative computation, and what's left is a single-variable function of $x_{2}$. As an example with $f(x_{1},x_{2},x_{3})=x_{1}^{2}x_{2}+\cos(x_{3})$, we have $\mathrm{Dir}(f,c,dx_{1})=2c_{1}c_{2}$. You will prove the mathematical validity of this rule in the exercises, but I suspect most readers have seen it and used it before.

The directional derivative along a standard basis vector—i.e., with respect to a single variable—has a special name: the *partial derivative* with respect to that variable. This is denoted using the $\partial$ sign (which I have always spoken "partial," or just "d") as $\partial f/\partial x_{2}$, which is read, "the partial derivative of $f$ with respect to $x_{2}$." In the same way that single variable derivatives $f'$ are typically written in the same variables as $f$ (i.e., using $x$ instead of $c$), the example above can be written as $\partial f/\partial x_{1}=2x_{1}x_{2}$. One refers to the *operation* of taking a partial derivative with respect to $x$ by the function named $\frac{\partial}{\partial x}$, with the juxtaposition of the $f$ in the numerator taking place of the standard parenthetical function application. Mathematicians have built up a hodgepodge of notations throughout history for this. In part, it's because parentheses are slow to write on a chalkboard—though they are easy for computers to parse, every new Lisp (or Scheme, or Racket) programmer discovers they're hard for humans to read unless formatted just so. In part, it's because mathematicians don't always want to think of derivatives as functions. Sometimes they want to highlight a different aspect, such as the vector structure. A mess of Lisp-y parentheses would not fit nicely in an inner product or summation. Syntactic sugar is a strong incentive.

When your chosen basis is the standard basis for each variable, the resulting total derivative matrix $Df$ is called the *gradient* of $f$, denoted $\nabla f$. The symbol $\nabla$ is often spoken "grad," and officially called a "nabla." We'll discuss the gradient in more detail below, because the gradient has a useful geometric property.

An example gradient for the function $f(x_{1},x_{2},x_{3})=x_{1}^{2}x_{2}+\cos(x_{3})$ is as follows. Below I will write the matrix generically in the sense that it works for any choice of $c=(x_{1},x_{2},x_{3})$, in the same way that when writing a single-variable derivative one uses the same variable before and after taking the derivative.

$$\nabla f=\begin{pmatrix}2x_{1}x_{2}&x_{1}^{2}&-\sin(x_{3})\end{pmatrix}$$

With this, we can compute the directional derivative in the direction of a vector $v=(1,-1,2)$ by applying the linear map $\nabla f$.

$$\begin{aligned}\operatorname{Dir}(f,x,v)&=\nabla f(v/\|v\|)=\langle\nabla f,v/\|v\|\rangle\\&=\begin{pmatrix}2x_{1}x_{2}&x_{1}^{2}&-\sin(x_{3})\end{pmatrix}\cdot\frac{1}{\sqrt{6}}\begin{pmatrix}1\\-1\\2\end{pmatrix}\\&=\frac{1}{\sqrt{6}}(2x_{1}x_{2}-x_{1}^{2}-2\sin(x_{3}))\end{aligned}$$

As $(x_{1},x_{2},x_{3})$ varies, this expression tracks the derivative of $f$ in the direction of $(1,-1,2)$ evaluated at $(x_{1},x_{2},x_{3})$. One can also slice it the other way, fixing a position to arrive at an expression that tracks the derivative of $f$ at a specific position as the direction varies. Doing this for $f$ above at $x=(1,2,\pi/2)$, leaving the unit vector $v=(v_{1},v_{2},v_{3})$ unspecified, we get

$$\nabla f(1, 2, \pi/2) \cdot v = \left(4 \quad 1 \quad -1\right) \cdot \begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix} = 4v_1 + v_2 - v_3$$

Any way you slice it, the value we want is just one inner product away! Symbolic differentiation makes this whole computation—the gradient and the inner product Kun does by hand—checkable in a few lines. We confirm both the generic gradient and the $(4, 1, -1)$ slice at $(1, 2, \pi/2)$.

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/02_gradient_symbolic.py -->
```

Many authors don't write the gradient as a vector in this way. Instead, they denote the basis vectors as $dx_i$, and the gradient is written as a single linear combination of these basis vectors. For the example $f$ we've been using, it would be

$$\nabla f = 2x_1x_2\,dx_1 + x_1^2\,dx_2 - \sin(x_3)\,dx_3$$

This notation has the advantage that you can use it while still hating linear algebra: this is just the inner product written out before choosing values for $v_1, v_2, v_3$, i.e., the coefficients of $dx_1, dx_2, dx_3$ in the vector $v$ to evaluate. It also helps you keep in mind that $dx_i$ are meant to represent deviations of $x_i$ from the point being evaluated. Sometimes they're written as a "delta," $\Delta x_i$ or $\delta x_i$, since delta is commonly used to represent a change.[^5] On the other hand, since it uses the symbols $dx_i$, it's easy to confuse the meaning with $d/dx_i$. We learned to love linear algebra. We'll stick to the vector notation.

[^5]: I find it curious how "delta" is used as a synonym for "difference" or "change" by executives in discussions that otherwise lack precision. Perhaps they studied math and incorporated that into their natural speech, or perhaps their faux-technical jargon impresses and confounds their enemies. I have certainly seen instances of both.

## The Geometry of the Gradient

Next we study the geometry of the gradient. Henceforth, when we say "differentiable function" we mean a function with a total derivative, we'll assume all functions are differentiable, and we'll seamlessly swap between total derivatives, directional derivatives, linear maps, and matrices.

Take the gradient $\nabla f$ of a differentiable function $f: \mathbb{R}^n \to \mathbb{R}$, and evaluate it at a concrete point $x \in \mathbb{R}^n$, as we did at the end of the "Computing the Total Derivative" section. The result is an $n \times 1$ matrix whose entries are all concrete numbers, but since we're working with 1-dimensional outputs, the total derivative is also a vector. This vector represents the linear map $\mathbb{R}^n \to \mathbb{R}$ whose input is a "direction to look in" and whose output is how steep the derivative is in that direction. Since $\nabla f$ is derived from $f$, it's natural to ask how the geometry of $\nabla f$ relates to the shape of $f$.

The answer reveals itself easily with a strong grasp of the projection function from linear algebra. Recall the function $\mathrm{proj}_v(w)$, which projects a vector $w$ onto a unit vector $v$. We studied this in Chapters 10 and 12, and there we noted some interesting facts. Let's recall them here. Let $v$ be a unit vector and $w$ an arbitrary vector of the same dimension.

1. The standard inner product $\langle w,v\rangle$ is the signed length of $\operatorname{proj}_{v}(w)$. The sign is positive if the result of the projection points in the same direction as $v$ and negative if it points opposite to $v$.
2. If you project $w$ onto $v$, and $v$ is not on the same line as $w$, then $\|\operatorname{proj}_{v}(w)\|<\|w\|$.
3. An alternate formula for $\langle v,w\rangle$ is $\|v\|\|w\|\cos(\theta)$, where $\theta$ is the angle between $v$ and $w$. In the case that $\|v\|=1$, the formula is $\|w\|\cos(\theta)$.

All of these point to the same general insight, which is a theorem with a famous name.

**Theorem 14.12 (The Cauchy-Schwarz Inequality).** Let $v,w\in\mathbb{R}^{n}$ be vectors, and $\langle v,w\rangle$ the standard inner product. Then $|\langle v,w\rangle|\leq\|v\|\|w\|$, with equality holding if and only if $v$ and $w$ are linearly dependent.

The Cauchy-Schwarz inequality has many proofs. I'll just share one that uses the cosine formula above to emphasize the geometry. You'll do a different proof in the exercises.

**Proof.** From $\langle v,w\rangle=\|v\|\|w\|\cos(\theta)$, and since $-1\leq\cos(\theta)\leq 1$, it follows that $|\langle v,w\rangle|\leq\|v\|\|w\|$.

Because $\cos(\theta)$ repeats after $\theta=2\pi$, we can restrict our attention to $0\leq\theta<2\pi$. For this range, $\cos(\theta)=1$ if and only if $\theta=0$, and $\cos(\theta)=-1$ if and only if $\theta=\pi$. For all other values, $-1<\cos(\theta)<1$. This proves the "if and only if" part of the theorem, because when $\cos(\theta)=\pm 1$, the two vectors lie on the same line, and hence are linearly dependent. $\blacksquare$

The details of this proof show more than the statement. Since the directional derivative is a projection of the gradient $\nabla f$ onto a unit vector $v$—i.e., $\langle\nabla f(x),v\rangle$—if you want to maximize the directional derivative, $v$ should point in the same direction as $\nabla f(x)$. Said a different way, the gradient $\nabla f(x)$ points in the steepest possible direction.

**Theorem 14.13.** For every differentiable function $f:\mathbb{R}^{n}\to\mathbb{R}$ and every point $x\in\mathbb{R}^{n}$, the gradient $\nabla f(x)$ points in the direction of steepest ascent of $f$ at $x$.

One is tempted to think this theorem is amazing (it is), but in light of our linear algebraic preparation it is a trivial consequence of how linear projection works. We can confirm it the brute-force way: sweep every unit direction $v$ around a point, compute the directional derivative $\langle\nabla f, v\rangle$, and watch the maximum land exactly on the normalized gradient—with the maximal slope equal to $\|\nabla f\|$, which is Cauchy-Schwarz attaining equality.

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/03_steepest_ascent.py -->
```

We can exploit this further. A level curve of $f$ at $c$ is the set of constant-height inputs $\{(x,f(x)):f(x)=f(c)\}$, like the topographic altitude lines on a map. For a differentiable function, the gradient at $c$ is perpendicular to the vector pointing along the level curve at $c$. If $v$ is a direction on the level curve, then the value of $f$ doesn't change in that direction, so $0=\operatorname{Dir}(f,c,v)=\langle\nabla f,v\rangle$. Such inner products occur when two vectors are perpendicular. This allows us to easily compute level curves.

Since many things in life and science can be modeled using functions $\mathbb{R}^{n}\to\mathbb{R}$, a common desire is to find an input $x\in\mathbb{R}^{n}$ which maximizes or minimizes such a function. For the sake of discussion, let's suppose we're looking for a minimum. Even when a mathematical model $f$ exists for a phenomenon, minimizing it might be algebraically intractable for a variety of reasons. For example, it might involve functions that are difficult to separate, such as trigonometric functions and threshold functions. Alternatively, it might simply be so large as to avoid any human analysis whatsoever, as is often the case with a neural network that has millions of parameters related to labeled data. The rest of this chapter is devoted to understanding how to tackle such situations, and the core idea is to "follow" the direction indicated by the gradient.

## Optimizing Multivariable Functions

Now we'll use the geometry of the gradient to derive a popular technique for optimizing functions $\mathbb{R}^{n}\to\mathbb{R}$. First, we review the situation for single-variable functions. In Chapter 9 we outlined the steps to solve a one-dimensional minimization problem, which I'll repeat here:

- Define your function $f:\mathbb{R}\to\mathbb{R}$ whose input $x$ you control, and whose output you'd like to minimize. Select a range of interest $a\leq x\leq b$.
- Compute the values $a\leq x\leq b$ for which $f'(x)=0$ or $f'(x)$ is undefined. These are called critical points.
- The optimal input $x$ is the minimum value of $f(x)$ where $x$ is among the critical points, or $x=a$ or $x=b$.

For multivariable inputs, you might reasonably expect an analogous technique to work: look at all the points $x$ for which $\nabla f(x)$ is the zero vector, and check them all for optimality. Unfortunately the story is more complicated. There are still critical points—those values $x$ for which $\nabla f(x)$ is the zero vector or undefined—but it's not as simple to enumerate them all and check which is the largest.

Take, for example, the function $f(x,y)=x^{2}+y^{2}+2xy$. Its gradient is $(2x+2y,2y+2x)$. Equating this to the zero vector results in an infinite family of solutions given by $x+y=0$. In other words, while one-dimensional functions can be reduced to a discrete (or continuous but trivial) set of points to check, the solution to $\nabla f=0$ can be a complicated surface. Even if you restrict just to polynomial equations life is still hard. There is an entire field of math, called algebraic geometry, dedicated to understanding the geometry of so-called varieties. A variety is the formal term for the space of solutions to a set of polynomial equations. The study of varieties is interesting and nuanced, beyond what can fit in this humble volume. Suffice it to say that understanding the shape of varieties from their defining formulas is not trivial, so we generally shouldn't expect to enumerate the zeros of the gradient.

If the equations are simple enough, one can apply a classical technique called Lagrange multipliers to compute optima. This was a central workhorse of a lot of pre-computer-era optimization. In general, Lagrange multipliers fail to help in almost every modern application, so we relegate it to the exercises. We'll instead focus on a more general algorithmic technique that works best when the function you're optimizing is intractable for pen-and-paper analysis. The technique is called gradient descent, and in modern times it has grown into a huge field of study.

Gradient descent (or gradient ascent, if you're maximizing) works as follows. Given $f$, start at a random point $x_{0}$. Iteratively evaluate the gradient $\nabla f(x_{i})$, which points in the direction of steepest ascent of $f$, and set $x_{i+1}=x_{i}-\varepsilon\nabla f(x_{i})$, where $\varepsilon$ is some small scalar. The subtraction is the focus: you "take a small step" in the opposite direction of the gradient to get closer to a minimum of $f$. So long as the gradient is a reasonable enough approximator of $f$ at each $x_{i}$, each $f(x_{i+1})$ is smaller than the $f(x_{i})$ before it. Repeat this over and over again, and you should find a minimum of some sort.

Gradient descent intuitively makes sense, but there are a few confounding details that trick this algorithm into stopping before it reaches a minimum. The devil lies in the details of the stopping condition: if we're at a minimum, the gradient should definitely be the zero vector (there's no direction of ascent at all, so there's no "steepest" direction), but does it work the other way as well?

Definitely not. However, to get a useful feel for why, we have to correct an injustice from Chapter 8: we never discussed the geometry of the second derivative.

### Curvature for Single Variable Functions

The derivative of a single variable function represents the slope of that function at a given point. Higher derivatives ($f'',f^{(3)},f^{(4)}$, etc.) correspond to certain sorts of curvature.

The second derivative is the example in most school curricula. Let $f:\mathbb{R}\to\mathbb{R}$ be a twice-differentiable function, and $f''$ its second derivative. Then the sign of $f''(x)$ at a point $x$ is called the concavity of $f$. Positive concavity implies the function is "curved upward" while negative concavity implies "curved downward." When $f''(x)=0$, the case is a bit more complicated, but it often corresponds to the case where $f$ is changing from having upward curvature to downward curvature, or vice versa.

Moreover, the magnitude of $f''(x)$ describes the "severity" of the curvature. $f(x)=x^{2}$ and $f(x)=5x^{2}$ have different second derivatives at $x=0$, and the latter is much more "sharply" curved upward.

There are definitions of curvature that are much more precise and expressive than the second derivative. In fact, the second derivative is quite bad at it. It only captures "second-order" curvature of a function. So it sees no curvature in $f(x)=x^{4}$ at $x=0$, despite that this function is very obviously concave up. The reason is that close to zero $x^{4}$ is also very close to zero, and so it makes the function quite flat in that region. Higher derivatives make up for the second derivative's failure, but looking at a finite number of derivatives will never provide the whole story. In particular, Theorems 14.14 and 14.18 are only sufficiency tests for a max/min. They cannot guarantee the detection of optima.

<!-- carousel -->
![Figure 14.5: Examples of functions with different concavity—concave up (positive second derivative) versus concave down (negative).](08 - Multivariable Calculus and Optimization_images/img-5.jpeg)
![Figure 14.6: An example of a function with a local max at $x = 1$, namely $f(x)=\frac{1}{2}(x-1)^{2}(x-4)(x+2)$.](08 - Multivariable Calculus and Optimization_images/img-6.jpeg)
<!-- endcarousel -->

We start with the presence of a local maximum or minimum in a single variable function. To be rigorous I need to clarify what is meant by a local max or min. When I say any property for $f$ holds locally at a point $c$, I mean that there is an interval $(a,b)$ containing $c$, such that the property is true when $f$ is restricted to $(a,b)$. $(a,b)$ may be very small if need be. In other words, if you "zoom in" to $f$ at $c$, then the property is true as far as you can see.

To specifically say a point $c,f(c)$ is a local minimum of $f$ means there is an interval $(a,b)$ around $c$ for which $f(c)\leq f(x)$ for all $x\in(a,b)$. In the example function in Figure 14.6, $f(x)=\frac{1}{2}(x-1)^{2}(x-4)(x+2)$, a sufficiently small interval around $x=1$ proves that $f$ has a local max at $(1,0)$, and likewise a local minimum close to $(3,-10)$.

Now we can prove the theorem that concavity is sufficient to detect a local min/max.

**Theorem 14.14.** Let $f:\mathbb{R}\to\mathbb{R}$ be a three-times-differentiable function and $c\in\mathbb{R}$ be a value for which $f'(c)=0$. If $f''(c)<0$, then $f$ has a local maximum at $c$. If $f''(c)>0$, then $f$ has a local minimum at $c$.

**Proof.** The Taylor series is our hammer. Since $f'(c)=0$, near $c$ we can expand $f(x)$ using a Taylor series that primarily depends on $f''(c)$.

$$f(x)=f(c)+\frac{f''(c)}{2}(x-c)^{2}+r(x)$$

Here $r(x)$ is the remainder term of the Taylor Theorem (Theorem 8.14). It's a degree-3 polynomial in $x-c$ whose coefficient depends on an evaluation of $f^{(3)}(z)$ at some unknown point $z\in(c,x)$. The most important detail of this is that it's a degree-3 polynomial, but in complete detail, it's

$$r(x)=\frac{f^{(3)}(z)}{6}(x-c)^{3}\qquad\text{for some unknown }z\text{ between }c\text{ and }x.$$

We need to argue that because $x-c$ is very small when $x$ is close to $c$, the value of $(x-c)^{3}$ is dwarfed by the value of $(x-c)^{2}$, so that the min/max behavior of $f$ is determined solely by the $(x-c)^{2}$ term.

Indeed, if you could informally argue that—say, by erasing $r(x)$ with reckless abandon—then $f(x)$ would be a simple, shifted parabola. The sign of $f''(c)$ would dictate whether the curve is concave up or concave down, and the peak would obviously be a min or a max (respectively). To make it more rigorous, we restrict ourselves to a small interval.

Let's suppose that $f''(c)>0$, so that we need to show $f(c)$ is a local min. In this case we want an interval $(a,b)$ on which $f(c)\leq f(x)$ for all $x$. Rearranging the formula above,

$$f(c)=f(x)-\frac{f''(c)}{2}(x-c)^{2}-r(x).$$

If the term $[-\frac{f''(c)}{2}(x-c)^{2}-r(x)]$ is not positive on $(a,b)$, then $f(c)\leq f(x)$. So the theorem will be proved if we can find an interval on which that term is at most zero. Rearranging, we need the following inequality to hold:

$$(x-c)^{2}\geq-\frac{2f^{(3)}(z)}{6f''(c)}(x-c)^{3}$$

Since the value of $r(x)$ depends on $z$ (which can be different for different values of $x$), we can't proceed unless we eliminate the dependence on $z$. We'll do that by estimating, i.e., replacing $f^{(3)}(z)$ with the max of $f^{(3)}$ over an interval. So start with some fixed interval around $c$, say $(c-0.01,c+0.01)$, and let $M>0$ be the maximum value of $|f^{(3)}(z)/(3f''(c))|$ on that interval. I.e., $M$ is the largest magnitude of the coefficient of $(x-c)^{3}$ in the above inequality that can occur close to $c$. Then we need to find an interval, perhaps smaller than $(c-0.01,c+0.01)$, for which the following (simplified) inequality is true for all $x$ in that interval.

$$(x-c)^{2}\geq M(x-c)^{3}$$

But this is easy! So long as $x\neq c$ we can simplify to see we just need a small enough interval that ensures $(x-c)\leq 1/M$. This will be true of either $(c-1/M,c+1/M)$ or $(c-0.01,c+0.01)$, whichever is smaller. $\blacksquare$

That was a lot of work to achieve a proof. Recalling our discussion of waves in Chapter 12, the reader might begin to understand why a working physicist would rather erase terms with reckless abandon than wade through the strange existential $z$'s that plague Taylor series. However, as was the case with matrix algebra providing an elegant (though intentionally leaky) abstraction for linear maps, mathematical analyses like these have their own abstractions to aid computation while maintaining rigor. In this case, most programmers are aware of it: big-O notation. We'll display its use in Chapter 15.

When $f''(x)=0$, we can't conclude anything. $f$ might have a max/min, or it might have neither. One example of having neither is $f(x)=x^{3}$ at $x=0$. The function switches concavity from concave down to concave up, but $f$ has no local max or min.

The idea of "local" behavior is a powerful one across mathematics. It is almost always easier to talk about local properties of an object rather than the global structure. A lot of time is spent investigating how a collection of unrelated bits of local information affect a global property. For single variable functions, one incarnation of this is that the local mins and maxes of $f$—along with a slight amount of extra information—determine the global min/max of $f$.

One can also think of a directional derivative as a sort of "local" property. It's the derivative when one "only looks" in a certain window, while the total derivative is global. If you can show that each directional derivative is continuous—or even just that the partial derivatives are continuous—then you automatically get the global (total) derivative. You have built global structure out of local pieces. Of course, the total derivative at a point is also a local construct from a different perspective. The total derivative describes the approximate structure of $f$ at a point, and with enough information about the total derivative at every point of $f$ (and a few bits of extra information), you can completely reconstruct $f$. So there are multiple scales of locality that allow one to discuss local and global properties, and how they relate to each other.

### The Hessian

For multivariable functions, locality replaces an interval with an "open ball," i.e., a set $B_r(c) = \{x : \|x - c\| < r\}$, which consists of all the points within a given radius of the point in question. The radius takes the place of the length of the interval to say "how local" you're looking.

While there are still local maxes and mins of the obvious sort, there are many ways a local min/max can fail to exist. An important way is called a saddle point. The shape of these is quite literal: the surface looks like the saddle of a horse, or the shape of a potato chip, in which the curvature goes up along one direction and down along another. A prototypical example of a curve with a saddle point is $f(x,y) = x^2 - y^2$, pictured in Figure 14.7.

With many variables comes many different directions along which curvature can differ. You might imagine a function with 5 variables, each axis giving two choices of up-curvature or down-curvature, for a total of $2^5 = 32$ different kinds of saddles (including the normal max/min). The way to get a handle on these forms is to look at the matrix of all ways to take second derivatives. First we define notation for second derivatives.

**Definition 14.15.** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a function which has first partial derivatives for every variable (recall, denoted $\partial f / \partial x_i$). The second-order partial derivative with respect to $x_i$ and $x_j$ is the partial derivative of the partial derivative, if it exists. A compact notation for this is

$$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial}{\partial x_i} \left( \frac{\partial f}{\partial x_j} \right)$$

If $i \neq j$, the derivative is called a mixed partial. If $i = j$ we write $\partial^2 f / \partial x_i^2$.

![Figure 14.7: An example of a function with a saddle point, $f(x,y) = x^2 - y^2$.](08 - Multivariable Calculus and Optimization_images/img-7.jpeg)

Personally I hate this notation, particularly how arbitrarily it's defined so that the "numerator" of the variable names are smushed together. My inner programmer cries out in anguish, because it's breaking algebra and functional notation at the same time by pretending they're the same. Are we taking the squared derivative with respect to a squared variable? Multiplying the top and bottom of a function name separately? Your syntactic sugar is rotting my brain! Alas, the notation is widespread, and the only alternative I know of, $f_{x_i x_j}(x) = \frac{\partial^2 f}{\partial x_j \partial x_i}$, is not all that much better.

One might expect the mixed partials with respect to $x_{i}, x_{j}$ and $x_{j}, x_{i}$ to be different due to the order of the computation. Under sufficiently strong conditions, they turn out to be the same.

**Theorem 14.16 (Schwarz's theorem).** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a function. Suppose that all of $f$'s partial derivatives exist and each partial derivative itself has a total derivative. Then for every $i, j$, it holds that $\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$.

We quote this theorem without proof, but notice that, in addition to reducing our computation duties by a half, it gives a hindsight rationalization for the fraction notation. If the order of partial derivatives doesn't matter, then we need not bother with the functional notation that emphasizes order precedence.

Next we define the Hessian, which is the matrix of mixed partial derivatives of a function.

**Definition 14.17.** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a function for which all second-order partial derivatives exist. Define the Hessian of $f$, denoted $H(f)$ (or often, when $f$ is fixed, just $H$), as an $n \times n$ matrix whose $i, j$ entry is $\partial^2 f / \partial x_i \partial x_j$.

$$H=\begin{pmatrix}\frac{\partial^{2}f}{\partial x_{1}^{2}}&\frac{\partial^{2}f}{\partial x_{1}\partial x_{2}}&\cdots&\frac{\partial^{2}f}{\partial x_{1}\partial x_{n}}\\[4pt]\frac{\partial^{2}f}{\partial x_{2}\partial x_{1}}&\frac{\partial^{2}f}{\partial x_{2}^{2}}&\cdots&\frac{\partial^{2}f}{\partial x_{2}\partial x_{n}}\\[4pt]\vdots&\vdots&\ddots&\vdots\\[4pt]\frac{\partial^{2}f}{\partial x_{n}\partial x_{1}}&\frac{\partial^{2}f}{\partial x_{n}\partial x_{2}}&\cdots&\frac{\partial^{2}f}{\partial x_{n}^{2}}\end{pmatrix}$$

Just like the gradient, $H(f)$ is really a function whose input is a point $x$ in the domain of $f$, and the output is the matrix $H(f)(x)$. The notation gets even hairier since $H(f)(x)$ is itself a linear map $\mathbb{R}^{n}\to\mathbb{R}^{n}$. In an exercise you'll interpret this linear map to make more sense of it.

Because of Schwarz's theorem, any point $x$ we use to make $H(f)$ concrete produces a real symmetric matrix. As we know from Chapter 12, symmetric matrices have an orthonormal basis of real eigenvectors with real eigenvalues, and so we can ask what these eigenvalues tell us about the structure of $f$ local to $x$. The theorem is a nice generalization of the min/max structure for single variable functions.

**Theorem 14.18.** Let $f:\mathbb{R}^{n}\to\mathbb{R}$ be a function which is twice differentiable, let $x\in\mathbb{R}^{n}$ be a point, and let $H$ be the Hessian of $f$ at $x$. If all the eigenvalues of $H$ are positive, then $f$ has a local min at $x$. If all the eigenvalues are negative, then $f$ has a local max at $x$. If $H$ has both positive and negative eigenvalues (and no zero eigenvalues), then $f$ has a saddle point at $x$.

We'll skip the proof for brevity, but our understanding of eigenvalues and eigenvectors provides a tidy interpretation. The eigenvectors of nonzero eigenvalues correspond to the directions (when looking from $x$) in which the curvature of $f$ is purely upward or downward, and maximally so. In a sense that can be made rigorous, because $H$ has an orthonormal basis of eigenvectors, these curvatures "don't interfere" with each other. If the surface were an ellipsoidal bowl, the eigenvectors would be the "axes" of the bowl. For a saddle point, the eigenvectors are the directions of the saddle that are parallel and perpendicular to the imagined horse's body. This is shown in Figure 14.8.

The eigenvalue test is short enough to run on the spot. Building the Hessian symbolically and reading off the signs of its eigenvalues recovers all three cases—the bowl ($x^2+y^2$, both eigenvalues positive), the dome (both negative), and Kun's saddle ($x^2-y^2$, mixed signs).

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/05_hessian_classify.py -->
```

![Figure 14.8: A function with a saddle point. The eigenvectors of the Hessian at the saddle point are shown as arrows, and represent the maximally positive and negative curvatures at the saddle point.](08 - Multivariable Calculus and Optimization_images/img-8.jpeg)

Of course, all of this breaks down if the sort of curvature we're looking at can't be captured by second derivatives. There might be an eigenvalue of zero, in which case you can't tell if the curvature is positive, negative, or even completely flat.

But this raises a natural question: if the gradient gives you first derivative information, and the Hessian gives you second derivative information, can we get third derivative information and higher? Yes! And can we use these to form a sort of "Taylor series" for multivariable functions? More yes! One difficulty with this topic is the mess of notation. A fourth-derivative-Hessian analogue is a four-dimensional array of numbers. With more dimensions comes more difficulty of notation (or the need for a better abstraction). Nevertheless, we can at least provide the analogue of the Taylor series for the first two terms:

**Theorem 14.19.** Let $f: \mathbb{R}^n \to \mathbb{R}$ be a twice differentiable function. Let $x \in \mathbb{R}^n$ be a point and $v \in \mathbb{R}^n$ be a small nonzero vector (a deviation direction from $x$). Let $\nabla f$ be the gradient of $f$ at $x$, and $H$ the Hessian at $x$. Then we have the following approximation:

$$f(x + v) \approx f(x) + \langle \nabla f, v \rangle + \langle Hv, v \rangle$$

See the exercises for a deeper investigation when $n = 2$.

## Gradient Descent: an Optimization Hammer

As we mentioned, the Hessian provides a sufficient condition to determine if a point is a local min: the gradient is zero and all the eigenvalues of the Hessian are positive. There are two caveats to this. First, the Hessian is expensive to compute. Its size is the square of the size of the gradient. Second, a provable optimum is something of a luxury. Most optimization problems benefit well enough from progressively improving an approximate optimum. Gradient descent does precisely this, and allows you to easily trade off solution quality for runtime.

Informally, gradient descent is the process: "go slowly in the opposite direction of the gradient until the gradient is zero." More formally, choose a stopping threshold $\varepsilon > 0$ and a learning rate $\eta > 0$, and loop as follows.

1. Start at some position $x = x_0$ (often a randomly chosen starting point).
2. While $\|\nabla f(x)\|>\varepsilon$:
    1. Update $x=x-\eta\nabla f(x)$.
3. Output $x$.

This is small enough to write and watch converge. On a tilted 2D bowl whose minimum we can also solve for exactly, the loop steps strictly downhill and lands on the true minimizer.

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/04_gradient_descent_bowl.py -->
```

This algorithm can be fast or slow depending on the choice of the starting point and the smoothness of $f$. If $x$ lands in a bowl, it will quickly find the bottom. If $x$ starts on a plateau of $f$, it will never improve. For this reason, one might run multiple copies of this loop, and output the most optimal run. If the inputs are chosen randomly, there's a good chance one avoids the avoidable plateaus.

The bottleneck of gradient descent is computing the gradient. When $f$ is complicated, such as in a neural network, efficient use of the chain rule is the primary tool for making gradient computations manageable. The rest of this chapter is dedicated to doing exactly that.

One might wonder, if the Hessian gives more information about the curvature of $f$, why not use the Hessian in determining the next step to take? You can! But unfortunately, since the Hessian is often an order of magnitude more difficult to compute than the gradient—and the gradient *already* requires mountains of engineering to get right—it's simply not feasible to do so. And, as you'll get to explore in the exercises, there are alternative techniques that allow one to "accelerate" gradient descent in a principled fashion without the Hessian.

## Gradients of Computation Graphs

The primary practical use of the chain rule is to allow us to compute complicated derivatives mechanically. In particular, one decomposes a function into a large composition of simple pieces, where the derivative of each piece is known, and applies the chain rule to build up the full derivative from the pieces.

Recall, for two differentiable functions $g:\mathbb{R}^{m}\to\mathbb{R}^{k}$ and $f:\mathbb{R}^{n}\to\mathbb{R}^{m}$, the derivative of the composition is the product of their total derivative matrices. In the case that $k=1$ (we can think of isolating one of the coordinates of $g$ to inspect), the chain rule becomes the following product, where we hide the evaluation point for brevity.

$$D(g\circ f)=(\nabla g)Df=\begin{pmatrix}\frac{\partial g}{\partial f_{1}}&\frac{\partial g}{\partial f_{2}}&\cdots&\frac{\partial g}{\partial f_{m}}\end{pmatrix}\begin{pmatrix}\frac{\partial f_{1}}{\partial x_{1}}&\frac{\partial f_{1}}{\partial x_{2}}&\cdots&\frac{\partial f_{1}}{\partial x_{n}}\\[2pt]\frac{\partial f_{2}}{\partial x_{1}}&\frac{\partial f_{2}}{\partial x_{2}}&\cdots&\frac{\partial f_{2}}{\partial x_{n}}\\[2pt]\vdots&\vdots&\ddots&\vdots\\[2pt]\frac{\partial f_{m}}{\partial x_{1}}&\frac{\partial f_{m}}{\partial x_{2}}&\cdots&\frac{\partial f_{m}}{\partial x_{n}}\end{pmatrix}$$

Supposing we only want to inspect the dependence of $g$ on $x_{1}$, we can restrict our attention to the first column of $Df$, and the result is the inner product. Note the fraction notation suggests that the $f_{i}$ in the last sum "cancel," which is not true but some find it helpful.

$$\frac{\partial g}{\partial x_{1}} = \begin{pmatrix} \frac{\partial g}{\partial f_{1}} & \frac{\partial g}{\partial f_{2}} & \dots & \frac{\partial g}{\partial f_{m}} \end{pmatrix} \begin{pmatrix} \frac{\partial f_{1}}{\partial x_{1}} \\ \frac{\partial f_{2}}{\partial x_{1}} \\ \vdots \\ \frac{\partial f_{m}}{\partial x_{1}} \end{pmatrix} = \sum_{i=1}^{m} \frac{\partial g}{\partial f_{i}} \frac{\partial f_{i}}{\partial x_{1}}$$

This situation often happens. A function depends on some input parameter transitively through many layers of function composition. To compute the derivative with respect to that parameter requires a long "chain" of partial derivatives, summed across the different paths to get from the input to the output. Chains that may look like:

$$\frac{\partial f}{\partial x} = \frac{\partial f}{\partial g} \frac{\partial g}{\partial h} \frac{\partial h}{\partial i} \frac{\partial i}{\partial j} \frac{\partial j}{\partial x}.$$

Notice that the terms in this chain can be grouped and re-grouped arbitrarily. For example, if you've already computed $\frac{\partial g}{\partial j}$, then to get $\frac{\partial f}{\partial x}$ you need only compute the missing terms

$$\frac{\partial f}{\partial x} = \frac{\partial f}{\partial g} \frac{\partial g}{\partial j} \frac{\partial j}{\partial x}.$$

This allows one to use caching to avoid recomputing derivatives over and over again. That's especially useful when there are many dependency branches. In fact, as we'll realize concretely when we build a neural network, the concept of derivatives with branching dependencies is core to training neural networks. To prepare for that, we'll describe the abstract idea of a computation graph and reiterate how the chain rule is computed recursively through such a network.

**Definition 14.20.** Let $G: \mathbb{R}^n \to \mathbb{R}$ be a function. A *computation graph* for $G$ is a directed, acyclic graph[^6] $(V, E)$ with the following properties.

1. There is a set of $n$ vertices identified as *input vertices*.
2. Each non-input vertex $v \in V$ has an associated integer $k_v \in \mathbb{N}$ (the number of inputs) and a function $f_v: \mathbb{R}^{k_v} \to \mathbb{R}$, along with an ordering of the edges $(w, v)$ with target $v$.
3. Each non-input vertex $v$ has exactly $k_v$ directed edges with target $v$.
4. There is exactly one vertex $v \in V$ with no outgoing edges designated as the *output vertex*.

[^6]: Recall, a directed edge $e = (v,w)$ is said to have *source* $v$ and *target* $w$, and represents a dependency of $w$ on $v$. A graph is acyclic if it contains no cycles, i.e., no circular dependencies.

![Figure 14.9: A computation graph. Each node $N$ is an input or some mathematical operation on the outputs of dependent nodes feeding into $N$.](08 - Multivariable Calculus and Optimization_images/img-9.jpeg)

If there's an edge $(v, w)$, we say that $v$ is an argument to $w$ and that $w$ depends on $v$.

A computation graph represents the computation of $G$ by first picking operations at each vertex, then specifying the dependencies of those operations, and adding vertices for the input. "Evaluating" a computation graph at a particular input is the obvious computational process of setting "values" for the input vertices, and following the operations of the graph to produce an output. Such a graph is a circuit in which each "gate" corresponds to the function of your choice.

For us, the operations $f_{v}$ at each vertex will always be differentiable (with one caveat), and hence $G$ will be differentiable, though the definition of a computation graph doesn't require differentiability.

Now we'll reiterate the chain rule for an arbitrary computation graph. Say we have a programmatic representation of a computation graph for $G$, and somewhere deep in the graph is a vertex with operation $f(a_{1},\ldots ,a_{n})$. We want to compute a partial derivative of $G$ with respect to an input variable that may be even deeper than $f$. Using the chain rule, we'll describe the algorithm for computing the derivative generically at any vertex and then apply induction/recursion. More specifically, at vertex $f$ we'll compute $\partial G / \partial f$ and multiply it by $\partial f / \partial a_{i}$ to get $\partial G / \partial a_{i}$.

So given a vertex with operation $f(a_{1},\ldots ,a_{n})$, argument vertices $a_1,\dots ,a_n$, and whose output is depended on by vertices $h_1,\ldots ,h_k$. We're interested in computing $\partial G / \partial a_{i}$ for some fixed $i$. This is illustrated in Figure 14.10.

![Figure 14.10: A generic node of a computation graph. Node $f$ has many inputs, its output feeds into many nodes, and each of its inputs and outputs may also have many inputs and outputs.](08 - Multivariable Calculus and Optimization_images/img-10.jpeg)

We know $\partial f / \partial a_1$ by assumption, having designed the graph so the gradient $\nabla f_v$ of each vertex $v$ is easy to compute. By induction, for each output vertex $h_j$ we can compute $\partial G / \partial h_j$. Then apply the chain rule:

$$\partial G / \partial f = \sum_{i=1}^{k} \frac{\partial G}{\partial h_{i}} \cdot \frac{\partial h_{i}}{\partial f}.$$

Once we have that, each $\partial G / \partial a_{i} = (\partial G / \partial f)\cdot (\partial f / \partial a_{i})$, as desired. Note that if $G$ depends on $a_{i}$ via another path through the computation graph, then $\partial G / \partial a_{i}$ sums over all such paths.

Because we use the vertices that depend on $f$ as the inductive step, the base case is the output vertex, and there $\partial G / \partial G = 1$. Likewise, the top of the recursive stack are the input vertices, and at the end we'll have $\partial G / \partial x_{i}$ for all inputs $x_{i}$.

This recursion is *reverse-mode automatic differentiation*, and it's worth seeing in miniature before scaling it to a neural network. Below is a tiny scalar "tape": each node caches its output on a forward pass, then the backward pass seeds $\partial G/\partial G = 1$ at the output and accumulates $\partial G/\partial f = \sum_h (\partial G/\partial h)(\partial h/\partial f)$ from outputs back to inputs—exactly the formula above. We then check the whole-graph gradient against sympy's exact symbolic derivative.

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/06_reverse_autodiff.py -->
```

As one can easily see, a network with heavily interdependent vertices requires one to cache the intermediate values to avoid recomputing derivatives everywhere. That's exactly the strategy we'll take with our neural network.

## Application: Automatic Differentiation and a Simple Neural Network

Neural networks are extremely popular right now. In the decade between 2010 and 2020, neural networks—specifically "deep" neural networks—have transformed subfields of computer science like computer vision and natural language processing. Neural networks and techniques using them can, with rather high fidelity, identify objects and scenes, translate simple language, and play abstract games of logic like Go. This was enabled, in large part, by the increased availability of cheap compute resources and graphical processing units (GPUs).

Perhaps surprisingly, the mathematical techniques that are used to train these networks are largely the same as they were decades ago. They are all variations on gradient descent, and the specific instance of gradient descent applied to training neural networks is called backpropagation.

In this section, we'll implement a neural network from scratch and train it to classify handwritten digits with relatively decent accuracy. Along the way, we'll get a taste for the theory and practice of machine learning.

### Learning from Data

Machine learning is the process of using data to design a program that performs some task. A prototypical example is classifying handwritten digits: you want a function which, given as input the pixels of an image of a handwritten digit, produces as output the digit in the picture. To solve such a problem, ignoring issues of engineering maintenance over time, you need a broad recipe of three steps:

1. Collect a large sample of handwritten digits, and clean them up (as all programmers know, we must sanitize our inputs!).
2. Get humans to provide labels for which pictures correspond to which digits.
3. Run a machine learning training algorithm on the labeled data, and get as output a classifier that can be used to label new, unseen data.

![Figure 14.11: An example decision tree classifying an image by looking at specific pixels.](08 - Multivariable Calculus and Optimization_images/img-11.jpeg)

One usually defines an allowed universe of possible classifiers—say, the class of decision trees that make decisions based on individual pixels—and the training algorithm uses the data to select a decision tree. An example decision tree might ask yes/no questions like, "does pixel (12, 25) have intensity higher than 128?" The answer determines the next question to ask, and eventually the final classification.

A slow, brutish training algorithm might be: generate all possible decision trees in increasing order of size, and select the first one that's consistent with the data.

To get a more pungent whiff, let's jump right into the handwritten digit dataset we'll use in the remainder of this chapter. The dataset is a famous one that goes by the irrelevant acronym MNIST (Modified National Institute of Standards and Technology referring to the institution that created the original dataset). The database consists of 70,000 data points, each of which is a 28-by-28 pixel black and white image of a handwritten digit. The digits have been preprocessed in various ways, including resizing, centering, and anti-aliasing. The raw dataset was originally created around 1995, and since 1998 the machine learning researchers Yan LeCun, Corinna Cortes, and Christopher Burges have provided the cleaned copy on LeCun's website.[^7] We also include a copy in the code samples for this book, since their version of the dataset has a non-standard encoding scheme.

MNIST is the Petersen graph of machine learning: every technique should first be tested on it as a sanity check. Figure 14.12 shows an example of a training point with label 7, pretty-printed from its raw format as a flat list of 784 ints.

![Figure 14.12: A training point for a digit 7 (aligned to make it easier to see).](08 - Multivariable Calculus and Optimization_images/img-12.jpeg)

The data is split into a training set and a test set, the former having 60,000 examples and the latter 10,000, which are stored in separate files. The separation exists to give a simulation of how well a classifier trained on the training data would perform on "new" data. As such, to get a good quality estimate, it's crucial that the training algorithm uses no information in the test set. We load the data using a helper function, which scales the pixel values from $[0, 255]$ to $[0, 1]$. For our application, we'll simplify the problem a bit to distinguishing between two digits: is it a 1 or a 7? The digit 1 corresponds to a label of 0, and a digit 7 corresponds to a label of 1.

```python
def load_1s_and_7s(filename):
    print('Loading data {}...'.format(filename))
    examples = []
    with open(filename, 'r') as infile:
        for line in infile:
            if line[0] in ['1', '7']:
                tokens = [int(x) for x in line.split(',')]
                label = tokens[0]
                example = [x / 255 for x in tokens[1:]]  # scale to [0,1]
                if label == 1:
                    examples.append([example, 0])
                elif label == 7:
                    examples.append([example, 1])
    print('Data loaded.')
    return examples
```

Before we go on, I must emphasize that the first two steps in the "machine learning recipe," collecting and cleaning data, are much harder than they appear. A misstep in any part of these processes can cause wild swings in the quality of the output classifier, and getting it right requires clear and strict procedures. See the Chapter Notes for more on this.

[^7]: The full program is available in the repository linked at pimbook.org.

### Learning Models and Hypotheses

In mathematical terms, the process of training a machine learning algorithm starts with defining the domain over your data. Very often the domain is $\mathbb{R}^{n}$ or $\{0,1\}^{n}$, so that an input datum is transformed from its natural format, such as an analog image, into a vector of numbers, such as the 4096 pixels in a discrete 64-by-64 digital image. Labels, though they can often have multiple values, will for our purposes be restricted to two options: $\{0,1\}$. For the handwritten digits example, think of this as the classifier for "is the digit a 7 or not?"

With these definitions, a dataset is a set of input-output pairs called labeled examples, $S=\{(x,l):x\in\mathbb{R}^{n},l\in\{0,1\}\}$, where $x$ is the example and $l$ is the label. If $f:\mathbb{R}^{n}\rightarrow\{0,1\}$ is the "true" function that labels examples correctly, then $f(x)=l$ for every $(x,l)\in S$.

Next, one defines a so-called hypothesis class. This is the universe of all possible output classifiers that a learning algorithm may consider. A useful hypothesis class has natural parameters that vary the behavior of a hypothesis. The learning algorithm learns by selecting parameters based on examples given to it. One of the most common examples, and a building block of neural networks, is the inner product.

**Definition 14.21.** Fix a dimension $n\in\mathbb{N}$. A linear threshold function is a function $L_{w,b}:\mathbb{R}^{n}\rightarrow\{0,1\}$, parameterized by a vector $w=(w_{1},\ldots,w_{n})\in\mathbb{R}^{n}$ called the weights and a scalar $b\in\mathbb{R}$ called a bias, which is defined as

$$L_{w,b}(x)=\begin{cases}1&\text{if }\langle w,x\rangle+b\geq 0\\0&\text{otherwise.}\end{cases}$$

Linear threshold functions have $n+1$ parameters: the $n$ weights $w$ and the bias $b$. The linear threshold function lives up to its name, thanks to the geometry of the inner product. In particular, $w\neq 0$ defines an $(n-1)$-dimensional vector space $w^{\perp}=\{v:\langle w,v\rangle=0\}$, which splits $\mathbb{R}^{n}$ into two halves. If $b=0$, then $w^{\perp}$ passes through the origin, and the inner product $\langle w,x\rangle$ is positive or negative depending on whether $x$ is on the same side of $w^{\perp}$ as $w$ or the opposite side (respectively). If $b\neq 0$, then the set $\{x:\langle w,v\rangle+b=0\}$ is $w^{\perp}$ shifted away from the origin by a distance of $b$ in the direction of $-w$.[^8]

[^8]: For this reason, a linear threshold function is sometimes called a "halfspace." I can't help but think of a halfspace as a fantasy convention for halflings and half-bloods.

One must also decide how to measure the quality of a proposed classifier. Measures vary depending on the learning model, but in practice it usually boils down to: does the classifier accurately classify the slice of data that has been cordoned off solely for the purpose of evaluation? This special slice of data is the test set. In the exercises, we'll explore a handful of theoretical learning models that give provable guarantees.[^9] Though these models are theoretical—for example, they assume the true labels have a particular structure—they serve as the foundation for all principled machine learning models.[^10] In these models, if a classifier is accurate on a test set, it will provably generalize to accurately classify new data.

A simple example learning model and problem, which is a building block for many other learning problems, is the following. Given labeled data points chosen randomly from a distribution over $\mathbb{R}^{n}$ that can be classified perfectly by a linear threshold function, design an algorithm that finds a "good" threshold function, i.e., one that will generalize well to new examples drawn from the same distribution. We'll explore this more in the exercises.

Summarizing, given a hypothesis class $H$ and a dataset $S$, a learning algorithm takes as input $S$ and produces as output a hypothesis $h\in H$. We want training algorithms to be efficient and classification to be "correct," where correct means that $h$ should accurately classify the test data.

[^9]: Such as neural networks and the support vector machine.
[^10]: We're ignoring some concerns related to overfitting, which is an important topic, but beyond the scope of this book.

### Neural Networks as Computation Graphs

In the "Gradients of Computation Graphs" section we explored how a differentiable function can be represented as a computation graph of simple operations, each of whose derivative is known. We saw how to compute the gradient of a complicated multivariable function by breaking it into pieces and using recursion and caching.

A neural network is exactly this: a massive function composed of simple, differentiable parts, whose output is a real number approximating the desired label of a training example. In Python, our network is an object wrapping the computation graph data structure. The trained network will evaluate an input and produce a binary label saying whether the input is a 1 (a label of zero) or a 7 (a label of one).

```python
network = NeuralNetwork(computation_graph, ...)
network.train(dataset)
network.evaluate(new_example)
```

The most important component operation that is used to build up a neural network is the linear halfspace $L_{w,b}$ from Definition 14.21. We'll call a vertex of the computation graph corresponding to a linear halfspace a linear node, and each linear node will have its own independently tunable set of parameters, $w$ and $b$.

In principle, there must be more to a neural network than linear nodes. As we know well from linear algebra, a composition of linear functions is still linear. The geometry of the space of handwritten digits is probably complicated enough to warrant more help. We should include operations in our computation graph that transform the input in nonlinear ways.

![Figure 14.13: A sigmoid function used to introduce nonlinearity into a computation graph.](08 - Multivariable Calculus and Optimization_images/img-13.jpeg)

A historically prevalent operation is the sigmoid function, that is, the single-variable function defined by $\sigma(x) = e^x / (1 + e^x)$, with the graph depicted in Figure 14.13. The sigmoid is nonlinear, differentiable, and its output is confined to $[0, 1]$. You may hear this operation compared to the "impulse" of a neuron in a brain, which is why the sigmoid is often called an activation function. Though neural networks are called "neural," the name is merely an inspiration. Simply put, sigmoids and other activation functions introduce nonlinearity in a useful way.

Typically, one applies the single-input activation function to the output of every linear node. The combined pair of a linear node and its activation function are called a neuron. Activation functions usually do not have tunable parameters.

Another important activation function, which is particularly popular in deep learning, is the rectified linear unit.

**Definition 14.22.** The ReLU function is the function

$$\operatorname{ReLU}(x) = \begin{cases} x & \text{if } x \geq 0 \\ 0 & \text{otherwise} \end{cases}$$

Equivalently, it can be defined as $\operatorname{ReLU}(x) = \max(0, x)$.

A ReLU needs no plot, as it's simply the function: truncate negative values to zero. The ReLU is particularly interesting because it is not differentiable! However, it only fails to have a derivative at $x = 0$, and in practice one can simply ignore the problem. The ReLU implements the thresholding of the linear halfspace, but with the twist that "activated" neurons can express how activated they are. Another advantage, which is particularly nice for hardware optimization, is that evaluating a ReLU and its derivative requires only branching comparisons and constants. No exponential math is required.

![Figure 14.14: A simple neural network architecture for MNIST.](08 - Multivariable Calculus and Optimization_images/img-14.jpeg)

The network we'll build is architected (quite arbitrarily) as depicted in Figure 14.14. The leftmost layer consists of the 784 input nodes, which are inputs to each node of the first layer of 10 linear nodes, each of which has a ReLU activation function. The outputs of the first-layer ReLUs feed as input to a second layer of 10 linear nodes, again with ReLUs, and the output of those goes into a final single linear node with a sigmoid activation.

```python
def build_network():
    input_nodes = InputNode.make_input_nodes(28 * 28)

    first_layer = [LinearNode(input_nodes) for i in range(10)]
    first_layer_relu = [ReluNode(L) for L in first_layer]

    second_layer = [LinearNode(first_layer_relu) for i in range(10)]
    second_layer_relu = [ReluNode(L) for L in second_layer]

    linear_output = LinearNode(second_layer_relu)
    output = SigmoidNode(linear_output)
    error_node = L2ErrorNode(output)
    network = NeuralNetwork(output, input_nodes, error_node=error_node)

    return network
```

The final output of the network is a real number in $[0,1]$. Labels are binary $\{0,1\}$, and so we interpret the output as a probability of the label being $1$. Then we can say that the label predicted by a network is $1$ if the output is at least $1/2$, and $0$ otherwise.

You might be wondering how someone comes up with the architecture of a neural network. The answer is that there are some decent heuristics, but in the end it's an engineering problem with no clear answers. Our network is quite small, only about 7,500 tunable parameters in all (because it's written in pure Python, training a large network would be prohibitively slow). In real production systems, networks have upwards of millions of parameters, and the process of determining an architecture is more alchemy than science.

There is a now-famous 2017 talk by Ali Rahimi in which he criticized what he argued was a loss of rigor in the field. He quoted, for example, how a change to the default rounding mechanism in a popular deep learning library (from "truncate" to "round") caused many researchers' models to break completely, and nobody knew why. The networks still trained, but suddenly failed to learn anything. Rahimi argues that brittle optimization techniques (gradient descent) applied to massively complex and opaque networks create a house of cards, and that theory and rigor can alleviate these problems. I tend to agree. But brittle or not, gradient descent on neural networks has proved to be remarkably useful, making some learning problems tractable despite the failure of decades of research into other techniques. So let's continue.

Once we've specified a neural network as a computation graph and obtained a dataset $S$ of labeled examples $(x,l)$, we need to choose a function to optimize. This is often called a *loss function*. For a single labeled example $(x,l)$, it's not so hard to come up with a reasonable loss function. Let $f_{w}$ be the function computed by the neural network and $w$ the combined vector of all of its parameters. Then define $E(w)=\left(f_{w}(x)-l\right)^{2}$ as the "error" of a single example. This is just the squared distance of the output of $f_{w}$ on an example from that example's label. Note we're not doing any rounding here, so that $f_{w}(x)\in[0,1]$.

If we wanted to convert this to a loss function for an entire training dataset, we could, as $E_{\text{total}}(w)=\frac{1}{|S|}\sum_{(x,l)\in S}\left(f_{w}(x)-l\right)^{2}$. Then the natural method is to use gradient descent to minimize $E_{\text{total}}$. However, this loss function requires us to loop over the entire training dataset for each step of gradient descent. That is prohibitively slow. Instead, one typically applies what's called *stochastic* gradient descent. In stochastic gradient descent, one chooses an example $(x,l)$ at random, and applies a gradient descent step update to $E(w)=\left(f_{w}(x)-l\right)^{2}$. Each subsequent gradient step update uses a different, randomly chosen example. The fact that this usually produces a good result is not obvious.

There are many different loss functions, and the loss function we chose above is called the $L_{2}$-loss. The name $L_{2}$ comes from mathematics, and the number $2$ describes the $2$'s that occur in the formula for the norm: $\|x\|_{2}=\left(\sum_{i}x_{i}^{2}\right)^{1/2}$. Changing the $2$ to, say, a $3$ results in an $L_{3}$ norm, and for a general $p$ these are called $L_{p}$ norms. You will explore different loss functions in the exercises.

This is the right moment to make the whole apparatus concrete and small. The following self-contained network is built in exactly the spirit Kun describes—linear nodes feeding sigmoid activations, an $L_2$ loss, and stochastic gradient descent via hand-rolled backpropagation—but with one hidden layer of sigmoids trained on XOR. XOR is the canonical example of a function *no* single linear threshold can separate (Definition 14.21), so it is the smallest task that genuinely needs the nonlinear hidden layer. After training, the net classifies all four cases correctly.

```python
<!-- include: code/pim/08 - Multivariable Calculus and Optimization/07_tiny_neural_net.py -->
```

As we outlined in the "Gradients of Computation Graphs" section, each vertex of our computation graph needs to know about various derivatives related to the operation computed at that node, and that these values need to be cached to compute a gradient efficiently. Now we'll see one way to manifest that in code. Let's start by defining a generic base node class, representing a generic operation in a computation graph. We'll call the operation computed at that node $f$, which has arguments $z_{1},\ldots,z_{m}$, and possibly tunable parameters $w_{1},\ldots,w_{k}$.

$$f=f(w_{1},\ldots,w_{k},z_{1},\ldots,z_{m})$$

Call the function computed by the entire graph $E$. The inputs to $E$ are both the normal inputs and all of the tunable parameters at every node. For the sake of having good names, we'll define the *global* derivative of some quantity $x$ to mean $\partial E/\partial x$, while the *local* derivative is $\partial f/\partial x$ (it's local to the node we're currently operating with). These are not standard terms.

Now we define a cache to attach to each node, whose lifetime will be a single step of the gradient descent algorithm.

```python
class CachedNodeData(object):
    def __init__(self):
        self.output = None
        self.global_gradient = None
        self.local_gradient = None
        self.local_parameter_gradient = None
        self.global_parameter_gradient = None
```

The attributes are as follows, with each expression evaluated at the current input $x$ and the current choice of tunable parameters.

1. `output`: a single float, the output of this node.
2. `global_gradient`: a single float, the value of $\partial E/\partial f$.
3. `local_gradient`: a list of floats, the values $(\partial f/\partial z_{1},\ldots,\partial f/\partial z_{m})$; i.e., the components of $\nabla f$ that correspond to the non-tunable arguments of $f$.
4. `local_parameter_gradient`: the same thing as `local_gradient`, but for the components of $\nabla f$ corresponding to the tunable parameters of $f$.
5. `global_parameter_gradient`: the same thing as `local_parameter_gradient`, but for the components of $\nabla E$ corresponding to the tunable parameters of $f$.

Now we define a base class `Node` for the vertices of the computation graph. Its children are `InputNode`, `ConstantNode`, `LinearNode`, `ReluNode`, `SigmoidNode`, and `L2ErrorNode`. Here's an example of how the subclasses of `Node` are used to build a computation graph:

```python
input_nodes = [InputNode(i) for i in range(10)]
linear_node_1 = LinearNode(input_nodes)
linear_node_2 = LinearNode(input_nodes)
linear_node_3 = LinearNode(input_nodes)
sigmoid_node_1 = SigmoidNode(linear_node_1)
sigmoid_node_2 = SigmoidNode(linear_node_2)
sigmoid_node_3 = SigmoidNode(linear_node_3)
linear_output = LinearNode(
    [sigmoid_node_1, sigmoid_node_2, sigmoid_node_3])
output = SigmoidNode(linear_output)
error_node = L2ErrorNode(output)

network = NeuralNetwork(
    output, input_nodes, error_node=error_node, step_size=0.5)
network.train(dataset)
network.evaluate(new_data_point)
```

And now we define `Node` and its subclasses.

```python
class Node(object):
    def __init__(self, *arguments):
        # if has_parameters is True, the child class must set
        # self.parameters (this is not good software engineering)
        self.has_parameters = False
        self.parameters = []
        self.arguments = arguments
        self.successors = []
        self.cache = CachedNodeData()

        # link argument successors to self
        for argument in self.arguments:
            argument.successors.append(self)

        # Argument nodes z_i will query this node f(z_1, ..., z_k)
        # for df/dz_i, so track the index for each argument node.
        self.argument_to_index = {
            node: index for (index, node) in enumerate(arguments)}
```

The list of arguments is ordered, so that all inputs and gradients correspond index-wise. We'll define the core methods in `Node` that perform gradient descent training momentarily, but first we have to define what functions the subclasses need to implement. They are:

1. `compute_output`: take as input a list of floats representing the concrete values of the global input to the computation graph (called `inputs`), and produce as output the output of this node, by recursively calling `output` on the argument nodes and performing an operation to produce an output.
2. `compute_local_gradient`: Take nothing as input and produce as output the list of partial derivatives $\partial f/\partial z_{i}$.
3. `compute_local_parameter_gradient`: Take nothing as input and produce as output the partial derivatives $\partial f/\partial w_{i}$.
4. `compute_global_parameter_gradient`: Take nothing as input and produce as output the partial derivatives $\partial E/\partial w_{i}$.

The example of the linear node illustrates each of these pieces. Let

$$f(w,b,x)=\langle w,x\rangle+b=b+\sum_{i=1}^{n}w_{i}x_{i}$$

We model the bias term $b$ by adding an extra input as a `ConstantNode`. We also have a simple `InputNode` for the input to the whole graph.

```python
class ConstantNode(Node):
    def compute_output(self, inputs):
        return 1


class InputNode(Node):
    def __init__(self, input_index):
        super().__init__()
        self.input_index = input_index

    def compute_output(self, inputs):
        return inputs[self.input_index]

    @staticmethod
    def make_input_nodes(count):
        '''A helper so the user doesn't have to keep track of
        the input indexes.'''
        return [InputNode(i) for i in range(count)]
```

Now we can define `LinearNode`. First, we initialize the weights and add a constant node for the bias. In this way, the bias is treated the same as any other input, which makes the formulas convenient.

```python
class LinearNode(Node):
    def __init__(self, arguments):
        # first arg is the bias
        super().__init__(ConstantNode(), *arguments)
        self.initialize_weights()
        self.has_parameters = True
        self.parameters = self.weights  # name alias

    def initialize_weights(self):
        arglen = len(self.arguments)
        # initial weights random, per a heuristic distribution
        weight_bound = 1.0 / math.sqrt(arglen)
        self.weights = [
            random.uniform(-weight_bound, weight_bound)
            for _ in range(arglen)]
```

A common heuristic to initialize a linear node's weights is to set the weights to be random numbers in $[-1/\sqrt{d},1/\sqrt{d}]$, where $d$ is the number of weights. This aligns with gradient descent: start at a random initial configuration and try to optimize.

The rest of the class consists of the required implementations of the `Node` interface. The gradients are particularly simple formulas. For $f(x,w)=\sum_{i=0}^{n}w_{i}x_{i}$, we have

$$\frac{\partial f}{\partial x_{i}}=w_{i},\qquad\frac{\partial f}{\partial w_{i}}=x_{i},\qquad\frac{\partial E}{\partial w_{i}}=\frac{\partial E}{\partial f}\frac{\partial f}{\partial w_{i}}$$

This turns into code as follows:

```python
class LinearNode(Node):
    # [...]

    def compute_output(self, inputs):
        return sum(
            w * x.evaluate(inputs)
            for (w, x) in zip(self.weights, self.arguments)
        )

    def compute_local_gradient(self):
        return self.weights

    def compute_local_parameter_gradient(self):
        return [arg.output for arg in self.arguments]

    def compute_global_parameter_gradient(self):
        return [
            self.global_gradient *
            self.local_parameter_gradient_for_argument(argument)
            for argument in self.arguments
        ]

    def local_parameter_gradient_for_argument(self, argument):
        '''Derivative of this node w.r.t. the weight associated
        with a particular argument.'''
        argument_index = self.argument_to_index[argument]
        return self.local_parameter_gradient[argument_index]
```

The other nodes are defined similarly, with the parameter functions returning empty lists as the `LinearNode` is the only node with tunable parameters. For each of the four `compute_` methods defined on each child class, we define corresponding methods on the parent class that check the cache and call the subclass methods on cache miss. They all look more or less like this:

```python
class Node:
    # [...]

    @property
    def local_gradient(self):
        if self.cache.local_gradient is None:
            self.cache.local_gradient = self.compute_local_gradient()
        return self.cache.local_gradient
```

The methods in the child classes use these properties when referring to their arguments, so the values will be lazily evaluated and then cached as needed. Finally, the computation of the global gradient for a node doesn't depend on the formula for that node, so it can be defined in the parent class.

```python
class Node:
    # [...]

    def compute_global_gradient(self):
        return sum(
            successor.global_gradient *
            successor.local_gradient_for_argument(self)
            for successor in self.successors)

    def local_gradient_for_argument(self, argument):
        argument_index = self.argument_to_index[argument]
        return self.local_gradient[argument_index]
```

At this point we've enabled the computation of all the gradients we need to do a step of gradient descent.

```python
class Node:
    # [...]

    def do_gradient_descent_step(self, step_size):
        '''The core gradient step: compute the gradient for each of
        this node's tunable parameters, step away from the gradient.'''
        if self.has_parameters:
            grad = self.global_parameter_gradient
            for i, gradient_entry in enumerate(grad):
                self.parameters[i] -= step_size * gradient_entry
```

Recall, each subclass defines its vector of parameters, and the `global_parameter_gradient` has to line up index by index. Also recall that we're subtracting because we want to minimize the error function $E$, and $\nabla E$ points in the direction of steepest increase of $E$.

The very last node of the computation graph, which computes the error for a training example, has some extra methods that depend on a training example's label. For the $L_{2}$ error, the entire class is:

```python
class L2ErrorNode(Node):
    def compute_error(self, inputs, label):
        argument_value = self.arguments[0].evaluate(inputs)
        self.label = label  # cache the label
        return (argument_value - label) ** 2

    def compute_local_gradient(self):
        last_input = self.arguments[0].output
        return [2 * (last_input - self.label)]

    def compute_global_gradient(self):
        return 1
```

Now we define a wrapper class `NeuralNetwork` that keeps track of the input and terminal nodes of the computation graph, resets caches, and controls the training of the network. We start with a self-explanatory constructor, and a helper function for applying some function to each node of the computation graph exactly once.

```python
class NeuralNetwork(object):
    def __init__(self, terminal_node, input_nodes,
                 error_node=None, step_size=None):
        self.terminal_node = terminal_node
        self.input_nodes = input_nodes
        self.error_node = error_node or L2ErrorNode(self.terminal_node)
        self.step_size = step_size or 1e-2

    def for_each(self, func):
        '''Walk the graph and apply func to each node.'''
        nodes_to_process = set([self.error_node])
        processed = set()

        while nodes_to_process:
            node = nodes_to_process.pop()
            func(node)
            processed.add(node)
            nodes_to_process |= set(node.arguments) - processed
```

The `for_each` function performs a classic graph traversal.[^11] We can use it to reset the caches at every node. We can also trivially define the `evaluate` function and `compute_error` functions as wrappers.

```python
class NeuralNetwork(object):
    # [...]

    def reset(self):
        def reset_one(node):
            node.cache = CachedNodeData()
        self.for_each(reset_one)

    def evaluate(self, inputs):
        self.reset()
        return self.terminal_node.evaluate(inputs)

    def compute_error(self, inputs, label):
        '''Compute the error for a given labeled example.'''
        self.reset()
        return self.error_node.compute_error(inputs, label)
```

[^11]: Whether it's depth-first or breadth-first depends on the semantics of `pop` and `add`, but we only care that each node is visited exactly once.

Finally, the training loop. It's as simple as randomly choosing an example, computing the output error for that example, and then calling `do_gradient_descent_step` on each node.

```python
class NeuralNetwork(object):
    # [...]

    def backpropagation_step(self, inputs, label, step_size=None):
        self.compute_error(inputs, label)
        self.for_each(
            lambda node: node.do_gradient_descent_step(step_size))

    def train(self, dataset, max_steps=10000):
        '''dataset is a list of pairs ([float], int): the first entry
        is the input point and the second is the label.'''
        for i in range(max_steps):
            inputs, label = random.choice(dataset)
            self.backpropagation_step(inputs, label, self.step_size)
```

Now let's apply this to the MNIST dataset. First we build our network, with two fully connected layers of `LinearNode`s and `ReluNode`s, with a final `LinearNode` with a `SigmoidNode` output.

```python
def build_network():
    input_nodes = InputNode.make_input_nodes(28 * 28)
    first_layer = [LinearNode(input_nodes) for i in range(10)]
    first_layer_relu = [ReluNode(L) for L in first_layer]
    second_layer = [LinearNode(first_layer_relu) for i in range(10)]
    second_layer_relu = [ReluNode(L) for L in second_layer]

    linear_output = LinearNode(second_layer_relu)
    output = SigmoidNode(linear_output)
    error_node = L2ErrorNode(output)
    return NeuralNetwork(
        output, input_nodes, error_node=error_node, step_size=0.05)
```

Then we split the training set into batches, separating from each batch a so-called validation set, which we use to measure the quality of the training as it progresses. At the end, we evaluate the error on the test set.

```python
train = load_1s_and_7s('mnist/mnist_train.csv')
test = load_1s_and_7s('mnist/mnist_test.csv')
network = build_network()
n, epoch_size = len(train), int(len(train) / 10)

for i in range(5):
    shuffle(train)
    validation = train[:epoch_size]
    train_piece = train[epoch_size:2 * epoch_size]
    print("Starting epoch of {} examples with {} validation".format(
        len(train_piece), len(validation)))

    network.train(train_piece, max_steps=len(train_piece))
    print("Finished epoch. Validation error={:.3f}".format(
        network.error_on_dataset(validation)))

print("Test error={:.3f}".format(network.error_on_dataset(test)))
```

During training we see:

```text
Starting epoch of 1300 examples with 1300 validation
Finished epoch. Validation error=0.015
Starting epoch of 1300 examples with 1300 validation
Finished epoch. Validation error=0.007
Starting epoch of 1300 examples with 1300 validation
Finished epoch. Validation error=0.007
Starting epoch of 1300 examples with 1300 validation
Finished epoch. Validation error=0.006
Starting epoch of 1300 examples with 1300 validation
Finished epoch. Validation error=0.010
Test error=0.011
```

Which is about $1.1\%$ error. Figure 14.15 shows some examples of classifications of digits after training. To make it easier to display in the book, I've rounded any nonzero values to $0$ and $1$, though in the full code we provide a helper function `show_random_examples` that shows the raw pixel values. As you can see, the first two are correct, and the third is incorrect (though the correct classification of that digit is hardly obvious).

![Figure 14.15: Example predictions of our neural network. The first two are classified correctly; the third is wrong, though the right label is hardly obvious to a human either.](08 - Multivariable Calculus and Optimization_images/img-15.jpeg)

Looking closely at the validation error as training progresses, the validation error progressively decreases, but at the end increases from $0.6\%$ to $1\%$. One possible explanation for this is the phenomenon of overfitting. We'll explore it more in the exercises, but a cursory explanation is that as a sufficiently expressive machine learning model continues to be trained, it can learn to encode specific features of the dataset. That is, the longer one trains on the same data, the more the trained model resembles a lookup table. This hurts generalization accuracy.

So there we have it! A functioning neural network, built as a computational graph of arbitrary operations, with automatic gradient computations.

## Cultural Review

- At its core, the derivative is the linear approximation of a function at a point. This view applies to both single- and multivariable settings.
- Local properties—those properties which hold only in a narrow slice around a point of interest—tend to be easier to reason about and compute, and they often inform one about the global properties of an object.

## Exercises

**14.1.** A function $f: \mathbb{R}^n \to \mathbb{R}$ is called continuous at a point $c \in \mathbb{R}^n$ if for every $\varepsilon > 0$ there exists a $\delta > 0$ such that whenever $\| x - c \| < \delta$ it holds that $|f(x) - f(c)| < \varepsilon$. Using this definition, show that $f(x, y, z) = x^2 + y^2 + z^2$ is continuous at $(0, 0, 0)$, but that $g(x, y, z) = \frac{xyz}{x^3 + y^3 + z^3}$ (defining $g(0, 0, 0) = 0$) is not continuous at $(0, 0, 0)$. Hint: look at different directions one could approach $(0, 0, 0)$.

**14.2.** Prove the first part of the Cauchy-Schwarz inequality for real vectors, that $|\langle v, w \rangle| \leq (\sum_{i} v_{i})(\sum_{i} w_{i})$, using elementary algebra.

**14.3.** Prove the analogue of Theorem 14.10 for functions $\mathbb{R}^n\to \mathbb{R}^m$. In that case, if $f = (f_{1},\ldots ,f_{m})$, the total derivative matrix should be:

$$\begin{pmatrix}\text{Dir}(f_{1},c,v_{1})&\text{Dir}(f_{1},c,v_{2})&\cdots&\text{Dir}(f_{1},c,v_{n})\\\text{Dir}(f_{2},c,v_{1})&\text{Dir}(f_{2},c,v_{2})&\cdots&\text{Dir}(f_{2},c,v_{n})\\\vdots&\vdots&\ddots&\vdots\\\text{Dir}(f_{m},c,v_{1})&\text{Dir}(f_{m},c,v_{2})&\cdots&\text{Dir}(f_{m},c,v_{n})\end{pmatrix}$$

Hint: the same proof works, but the construction of the single-variable function to apply the chain rule to is slightly different.

**14.4.** Look up a proof of the fact that a function $f:\mathbb{R}^{n}\to\mathbb{R}$ is differentiable (has a total derivative) if all of its partial derivatives exist and are continuous (Theorem 14.11). This theorem relies on a chain of results: the definition of continuity, Rolle's Theorem for single-variable functions, and the Mean Value Theorem for single variable functions. The Mean Value Theorem is one of the most powerful technical tools in the fields of mathematics that deal with continuous functions.

**14.5.** In the chapter I provided a corkscrew surface for which, if the direction of the directional derivative changed slightly, the value of the directional derivative changed drastically (i.e., it was not continuous in the choice of direction). On the other hand, Theorem 14.11 fixes the basis vector and requires the directional derivative to be continuous with respect to $c$, the position. Reconcile these two perspectives. Squint at the corkscrew surface and see why continuity with respect to $c$ covers the same edge case as rotating the direction.

**14.6.** Find and study a proof of Schwarz's theorem, that mixed partial derivatives of sufficiently nice functions don't depend on the order you take them in.

**14.7.** Prove that the rule for computing partial derivatives by assuming other variables are constant is valid.

**14.8.** Make sense of the Hessian as a linear map.

**14.9.** The gradient of a function $\mathbb{R}^{n}\to\mathbb{R}$ is a vector which points in the direction of steepest ascent of the function, which we investigated via projections. What can be said about the direction of steepest ascent of a multi-output function $\mathbb{R}^{n}\to\mathbb{R}^{m}$ by inspecting its total derivative matrix?

**14.10.** Find and understand a statement of Taylor's theorem for two-variable functions (with an arbitrary number of approximation terms).

**14.11.** Perhaps the most famous theoretical machine learning model is called the *Probably Approximately Correct* model (abbreviated PAC). This model formalizes much of modern machine learning. Given a finite set $X$ (the universe of possible inputs), the PAC model involves a probability distribution $D$ over $X$ used both for generating data and evaluating the quality of a hypothesis. A machine learning algorithm gets as input the ability to sample as much data as it wants from $D$, and its output hypothesis $h$ must have high accuracy on $D$ (hence the name "approximately" in PAC). Since the sampled data is random, the learning algorithm may fail to produce an accurate classifier with small probability. However—and this is the most stringent qualification—in order for a learning algorithm to be considered successful in the PAC model, it must provably succeed *for any* distribution on the data. If the distribution is uniformly random or focused on just a small set of screwy points, a valid "PAC learner" must be able to adapt. Look up the formal definition of the PAC model, find a simple example of a problem that can be PAC-learned, and read a proof that a successful algorithm does the trick.

**14.12.** Another important learning model involves an algorithm that, rather than passively analyzing data that's given to it (as in the PAC model of the previous exercise), is allowed to formulate queries of a certain type, an "oracle" (a human) answers those queries, and then eventually the algorithm produces a hypothesis. Such a model is often called an "active learning" model. Perhaps the most famous example is *exact learning with membership and equivalence queries*. Look up a formal definition of this model, and learn about its main results and variations.

**14.13.** Write a program that uses gradient descent to learn linear threshold functions. In particular: write a function that samples data uniformly from the set $[0,1]^{5}\subset\mathbb{R}^{5}$, and labels them (unbeknownst to the learning algorithm) according to their value under a fixed linear threshold function $L_{w,b}$. Design a learning algorithm to learn $w$ and $b$ from the data. That is, determine what the appropriate loss function should be, determine a formula for the gradient, and enshrine it in code. How much data is needed to successfully and consistently learn? How does this change as the exponent $5$ grows?

**14.14.** In this chapter, our gradient descent used a fixed $\varepsilon$ as the step size. However, it can often make sense to adjust the rate of descent as the optimization progresses. At the beginning of the descent, larger steps can provide quicker gains toward an optimum. Later, smaller steps help refine a close-to-optimal solution. A popular technique due to Yurii Nesterov involves keeping track of a so-called *momentum* term, and adding both the normal gradient descent step plus the momentum term. Research Nesterov's method (Under what conditions does it work? Do these reasonably apply to neural networks?) and adapt the program in this chapter to use it. Measure the improvement in training time.

**14.15.** Another popular technique for training neural networks is the so-called *minibatch*, where instead of a stochastic update for each example, one groups the examples into batches and computes the average loss for the batch. Research why minibatch is considered a good idea, and augment the program in this chapter to incorporate it. Does it improve the error rate of the learned hypothesis?

**14.16.** There are many different loss functions for a neural network. Look up a list of the most widely used loss functions, and research their properties.

**14.17.** One particularly relevant loss function is called softmax, because it applies to a vector-valued input. Softmax is typically used to represent the loss of a categorical (1 out of $N$ options) labeling, and it's particularly useful to adapt MNIST from a binary two-digit discriminator to a full ten-digit classifier. Augment the code in this chapter to incorporate softmax, and use this to implement a classifier for the full MNIST dataset.

**14.18.** Overfitting is the phenomenon of a machine learning algorithm "hard-coding" the labels of specific training examples in a way that does not generalize. Imagine a robot that memorizes a lookup table for conversation replies, but then fails to respond to every unexpected query. It could hardly be called learning! Overfitting seeps into neural networks in pernicious ways, such as not properly separating training, validation, and test data. Overusing validation data can also cause some degree of overfitting of tuned parameters. The most common type of overfitting occurs simply when training goes on too long on the same set of examples. Explore the degree to which overfitting occurs in the neural network in this chapter for MNIST by running the training loop for a long time. Try decreasing the size of the training set, and observe the overfitting get worse.

**14.19.** Space and orientation is particularly useful to computer vision applications. One industry-standard "feature" used in deep neural networks for computer vision is a primitive called convolution. Research this new operation, and implement a $4\times 4$ convolution node in the neural network from this chapter. Design an architecture that incorporates convolution, and train MNIST on it. Does the quality improve?

## Chapter Notes

### The Chain Rule: a Reprise and a Proof

Recall for single-variable functions $f,g:\mathbb{R}\to\mathbb{R}$, the chain rule says that the derivative of $f(g(x))$ involves evaluating $f'$ at $g$, and multiplying the result by $g'$. I.e., $\frac{d}{dx}(f(g(x)))=f'(g(x))g'(x)$.

The analogous formula for multivariable functions involves a matrix multiplication:

$$D(g\circ f)(c)=Dg(f(c))Df(c).$$

Let's first think about why this should be harder in principle than the single variable case. Call $x=(x_{1},\ldots,x_{n})$ the variables input to $f=(f_{1},\ldots,f_{m})$, a function $\mathbb{R}^{n}\to\mathbb{R}^{m}$. The derivative of $g\circ f$ measures how much $g$ depends on changes to each $x_{i}$. But while $f$ depends on an input $x_{i}$ in a straightforward way, $g$ depends on $x_{i}$ transitively through the possibly many outputs of $f$. Computing $\partial g/\partial x_{i}$ should require one to combine the knowledge of $\partial f_{j}/\partial x_{i}$ for each $j$, and that combination might be strange. The function $g\circ f$ has a dependency graph like in Figure 14.16, where the arrows $a\to b$ indicate that $b$ depends on $a$. A similar dependence describes dependence among the partial derivatives.

![Figure 14.16: The dependence of $g \circ f$ on each $x_{i}$ contains paths through each of the $f_{j}$.](08 - Multivariable Calculus and Optimization_images/img-16.jpeg)

Luckily the relationship is quite elegant: for one dependent variable you multiply along each branch and sum the results. Doing this for every input variable produces exactly the matrix multiplication that makes up the chain rule. We'll prove a slightly simpler version of the chain rule where $g$ has only one output, which has all the necessary features of the more general proof where $g = (g_{1},\ldots ,g_{k})$ is vector-valued.

**Theorem 14.23.** Let $g: \mathbb{R}^m \to \mathbb{R}$ and $h: \mathbb{R}^n \to \mathbb{R}^m$ be differentiable functions. Write $h = (h_1, \ldots, h_m)$, with $h_i = h_i(x)$ for $x = (x_1, \ldots, x_n)$, and $g(y)$ with $y = (y_1, \ldots, y_m)$. Then $g(h(x)) = g(h_1(x), \ldots, h_m(x))$ is differentiable, and the gradient at $c \in \mathbb{R}^n$ is

$$\frac{\partial (g \circ h)}{\partial x_{1}}(c) = \sum_{i=1}^{m} \frac{\partial g}{\partial h_{i}}(h(c)) \cdot \frac{\partial h_{i}}{\partial x_{1}}(c)$$

The other components of the gradient are defined by replacing $x_{1}$ with $x_{j}$.

**Proof.** For clarity, in this proof the boldface $\mathbf{v}$ will denote a vector of numbers or functions (a function with multiple outputs). Denote by $\mathbf{h}(\mathbf{x}) = (h_1(\mathbf{x}),\dots ,h_m(\mathbf{x}))$, so that we can conveniently abbreviate $g(h_{1}(\mathbf{x}),\ldots ,h_{m}(\mathbf{x}))$ as $g(\mathbf{h}(\mathbf{x}))$. Let $H$ be the matrix representation of the total derivative of $\mathbf{h}$,

$$H = \begin{pmatrix} - & H_{1} & - \\ - & H_{2} & - \\ & \vdots & \\ - & H_{m} & - \end{pmatrix}$$

Let $G$ be the matrix representation of the total derivative of $g$ (i.e., $\nabla g$). The claimed total derivative matrix for $g(\mathbf{h}(\mathbf{x}))$ is the matrix multiplication $GH$. This results in the formula claimed by the theorem. We need to show that $GH$ satisfies the linear approximation condition for $g(\mathbf{h}(\mathbf{x}))$, i.e., that

$$\lim_{\mathbf{x}\to\mathbf{c}}\frac{g(\mathbf{h}(\mathbf{x}))-g(\mathbf{h}(\mathbf{c}))-GH(\mathbf{x}-\mathbf{c})}{\|\mathbf{x}-\mathbf{c}\|}=0$$

We start with a convenient change of variables. Define $\mathbf{t}=\mathbf{x}-\mathbf{c}$, and then we can see that the limit above can equivalently be written in terms of a vector $\mathbf{t}$ as $\mathbf{t}\to\mathbf{0}$.

$$\lim_{\mathbf{t}\to\mathbf{0}}\frac{g(\mathbf{h}(\mathbf{c}+\mathbf{t}))-g(\mathbf{h}(\mathbf{c}))-GH(\mathbf{t})}{\|\mathbf{t}\|}$$

Now we define two functions that track the error of the linear approximators. More specifically, the first function represents the error of $H$ as a linear approximator of $\mathbf{h}$ at $\mathbf{c}$, and the second is the error of $G$ as a linear approximator of $g$ at $\mathbf{h}(\mathbf{c})$.

$$\begin{aligned}\mathbf{err}_{H}(\mathbf{t})&=\mathbf{h}(\mathbf{c}+\mathbf{t})-\mathbf{h}(\mathbf{c})-H(\mathbf{t})\\\mathrm{err}_{G}(\mathbf{s})&=g(\mathbf{h}(\mathbf{c})+\mathbf{s})-g(\mathbf{h}(\mathbf{c}))-G(\mathbf{s})\end{aligned}$$

Note that in $\mathrm{err}_{G}$, the vector $\mathbf{s}$ is in the domain of $g$, while in $\mathbf{err}_{H}$ the vector $\mathbf{t}$ is in the domain of the $h_{i}$. We can use these formulas to simplify the limit above. Substitute for $\mathbf{h}(\mathbf{c}+\mathbf{t})$ a rearrangement of the definition of $\mathbf{err}_{H}$, getting

$$\lim_{\mathbf{t}\to\mathbf{0}}\frac{g\big(\mathbf{h}(\mathbf{c})+H(\mathbf{t})+\mathbf{err}_{H}(\mathbf{t})\big)-g(\mathbf{h}(\mathbf{c}))-GH(\mathbf{t})}{\|\mathbf{t}\|}$$

Define $\mathbf{s}=H(\mathbf{t})+\mathbf{err}_{H}(\mathbf{t})$, so that we can substitute $g(\mathbf{h}(\mathbf{c})+\mathbf{s})$ using a rewriting of the definition of $\mathrm{err}_{G}$.

$$\lim_{\mathbf{t}\to\mathbf{0}}\frac{g(\mathbf{h}(\mathbf{c}))+G(\mathbf{s})+\mathrm{err}_{G}(\mathbf{s})-g(\mathbf{h}(\mathbf{c}))-GH(\mathbf{t})}{\|\mathbf{t}\|}$$

Expand $\mathbf{s}$, apply linearity of $G$, and cancel opposite terms, to reduce the limit to

$$\lim_{\mathbf{t}\to\mathbf{0}}\frac{G(\mathbf{err}_{H}(\mathbf{t}))+\mathrm{err}_{G}(\mathbf{s})}{\|\mathbf{t}\|}.$$

To show this limit is zero, we split it into two pieces. The first is

$$\lim_{\mathbf{t}\to\mathbf{0}}\frac{G(\mathbf{err}_{H}(\mathbf{t}))}{\|\mathbf{t}\|}.$$

Note that because $G$ is a gradient, $G(\mathbf{err}_{H}(\mathbf{t}))$ is an inner product—the projection of $\mathbf{err}_{H}(\mathbf{t})$ onto a fixed vector, $\nabla g(\mathbf{c})$. The Cauchy-Schwarz inequality informs us that the norm of $G(\mathbf{err}_{H}(\mathbf{t}))$ is bounded from above by $C\|\mathbf{err}_{H}(\mathbf{t})\|$, where $C=\|\nabla g(\mathbf{c})\|$ is constant. So the limit above is

$$C\lim_{\mathbf{t}\to\mathbf{0}}\frac{\|\mathbf{err}_{H}(\mathbf{t})\|}{\|\mathbf{t}\|}=0.$$

This goes to zero because (by the definition of $\mathbf{err}_{H}$) it's the defining property of the total derivative of $H$. It remains to show the second part is zero:

$$\lim_{\mathbf{t}\to\mathbf{0}}\frac{\mathrm{err}_{G}(\mathbf{s})}{\|\mathbf{t}\|}$$

We would like to bound this limit from above by a different limit we can more easily prove goes to zero. Indeed, if there were a constant $B$ for which

$$\frac{\mathrm{err}_{G}(\mathbf{s})}{\|\mathbf{t}\|}\leq\frac{\mathrm{err}_{G}(\mathbf{s})}{B\|\mathbf{s}\|}$$

Then we'd be done: $\mathbf{s}\to\mathbf{0}$ if and only if $\mathbf{t}\to\mathbf{0}$, due to how $\mathbf{s}$ is defined in terms of $\mathbf{t}$, and $\mathrm{err}_{G}(\mathbf{s})/\|\mathbf{s}\|\to 0$ again by the definition of the total derivative of $g$. Expanding $\mathbf{s}=H(\mathbf{t})+\mathbf{err}_{H}(\mathbf{t})$ and again expanding $\mathbf{err}_{H}(\mathbf{t})$, the needed $B$ occurs when

$$\frac{1}{B}\geq\left\|\frac{\mathbf{h}(\mathbf{c}+\mathbf{t})-\mathbf{h}(\mathbf{c})}{\|\mathbf{t}\|}\right\|$$

The quantity on the right hand side is familiar: it's the inside of the limit for the directional derivative of $\mathbf{h}$ (rather, a vector of directional derivatives). As $\|\mathbf{t}\|\to 0$ it gets close to the directional derivatives, so for a sufficiently small $\mathbf{t}$, the quantity is no larger than twice the largest possible directional derivative, i.e., $2\|(\nabla h_{1}(\mathbf{c}),\ldots,\nabla h_{m}(\mathbf{c}))\|$. Choose $B$ so that $1/B$ is larger than this quantity, and the proof is complete. $\blacksquare$

This was the most difficult proof in this book. And it's easy to get lost in it. We started from a relatable premise: find a formula for the chain rule for multivariable functions. To prove our formula worked, we reduced progressively trickier and more specialized arguments, boiling down to an arbitrary-seeming upper bound of a haphazard limit of an error term of a linear approximation.

To be sure, the steps in this proof were not obvious. One has to take a bit of a leap of faith to guess that $GH$ was the right formula (though it is the simplest and most elegant option), and then jump from an obtuse limit to the realization that, if one writes everything in terms of error terms, the hard parts ($g$ composed with $\mathbf{h}$) will cancel out. Suffice it to say that this proof was distilled from hard work and many examples, and it leaves a taste of mystery in the mouth. Until, that is, one dives deeper into the general subfield of mathematics known as "analysis," where arguments like this one are practiced until they become relatively routine. One gains the nose for what sorts of quantities should yield their secrets to a well-chosen upper bound. Contrast this to subjects like linear algebra and abstract algebra (Chapter 16), in which pieces largely tend to fit together in a structured manner that—in my opinion—tends to appeal to programmers in a way that analysis doesn't. Another demonstration of subcultures in mathematics.

### The Perils of Clean Data

We were fortunate enough to have LeCun and his colleagues vet MNIST for us. These prepared datasets are like goods in supermarkets. A shopper doesn't see, appreciate, or viscerally comprehend the amount of work and resources required to rear the cow and grow the almonds, nor even the general form of the pipeline. A common refrain among data scientists and machine learning practitioners is that machine learning is 10% machine learning, and 90% data pipelines.

For example, deciding on the meaning of a label is no simple task. It seems easy for problems like handwritten digits, because it's mostly unambiguous what the true label for a digit is. But for many interesting use cases—detecting fraud/spam, predicting what video a user will enjoy, or determining whether a loan applicant should receive a loan—determining what constitutes a positive or negative label requires serious thought, or worse, the hindsight of a disaster caused by getting it wrong. Harder still are the system-level implications of how a classifier will be used. If a video website deploys a system that naively optimizes for a shallow metric like total time watched, creators will upload superficially longer videos. This wastes everyone's time and hurts the reputation of the site.

Another concern is bias in the training data. Not just statistical bias, which can be a result of errors in data collection on the part of the process designer, but human bias beyond one's control. When you collect data on human preferences, it's easy for population majorities to overwhelm less prevalent signals. This happens roughly because machine learning algorithms tend to look for the statistically dominant trends first, and only capture disagreeing trends if the model is complex enough to have both coexist. Think of Chapter 12 in which we studied a physical model by throwing out small order terms. In this context, if those terms corresponded to a coherent group of users, those users would be ignored or actively harmed by the mathematical model.

Even worse, active discrimination can be encoded into training labels. If one trains an algorithm to predict job fitness on a dataset of hiring information, incorporating the reviews of human interviewers can muddy the dataset. You have to be aware that humans, and especially humans in a position of power, can exhibit bias for any number of superficial characteristics that are unrelated to job fitness, most notably that an applicant looks and behaves like the people currently employed. An algorithm trained on this data will learn to mimic the human preferences, which may be unrelated to one's goal.

While mathematics and engineering do weigh in on these problems, it's extremely important to realize that the transition to numbers and equations doesn't magically avoid problems like bias and bad process. If anything it obfuscates them from those who aren't fluent in the language. All the user sees is the biscuit that the algorithm decided was appropriate for them to eat. When math is applied to the real world, it serves as a model with assumptions as a foundation. If the assumptions disagree with reality, the levee will break. Riots can literally ensue. We acutely understand this in software: most systems rely on a mess of consistency constraints, some validated explicitly and others not, and when you put garbage data into a software system, you'll get garbage results. So it is for machine learning, which is why it's sometimes called the "high interest credit card of technical debt." These sorts of problems, though interesting and important, are beyond the scope of this book. Instead we'll focus on the "easy" part, actually training an algorithm and producing a classifier.

### Scaling Neural Networks

Our neural network and computation graph are almost laughably small. And, having written our network in pure Python, training proceeds at a snail's pace. It should be obvious that our toy implementation falls far short of industry-strength deep learning libraries, even though the underlying concepts of computation graphs are the same. I'd like to lay out a few specific reasons.

Our network for learning (a subset of) MNIST has roughly $7,500$ tunable parameters. Large-scale neural networks can have millions or even billions of tunable parameters. Many additional mathematical and engineering tricks are required to achieve such scale.

One aspect of this is hardware. Top-tier neural networks take advantage of the structure of certain nodes (for example, many nodes are linear) and the typical architecture of a network (nodes grouped in layers) to convert evaluation and gradient computations to matrix multiplications. Once this is done, graphics cards (GPUs) can drastically accelerate the training process. Even more, companies like Google develop custom ASICs (application-specific integrated circuits) that are particularly fast at doing the operations neural networks need for training. One such chip is called a Tensor Processing Unit (TPU). The proliferation of graphics cards and custom hardware has resulted in the ability to train more ambitious models for applications like language translation and playing board games like Go.

However, fancy hardware won't fix issues like overfitting, where a model with billions of parameters essentially becomes a lookup table for the training data and doesn't generalize to new data. To avoid this, experts employ a handful of engineering and architectural tricks. For example, between each layer of linear nodes, one can employ a technique called dropout, in which the outputs of random nodes are set to zero. This prevents nodes in subsequent layers from depending on specific arguments in a fragile way. In other words, it promotes redundancy. Such techniques fall under the umbrella of regularization methods.

Other techniques are specific to certain application domains. For example, the concept of convolution is used widely in networks that process image data. While convolution has a mathematically precise definition, we'll suffice to describe it as applying a "filter" to every $4\times 4$ pixel window of an image. Such techniques allow individual neurons to encode edge detectors. When combined in layers—filters of filters, and so on—the results are nodes that act as quite sophisticated texture and shape detectors.

The individual computational nodes also get much consideration. Historically, the original nonlinear activation node for a linear node was the sigmoid function. However, because the function plateaus for large positive and negative values, training a network that solely uses sigmoid activations can result in prohibitively slow learning. The ReLU function avoids this, but brings its own problems. In particular, when linear weights are randomly initialized as we did, ReLU nodes have an equal chance of being zero or nonzero. When a ReLU activation is zero, that neuron (and all the input work to get to that neuron) is essentially dead. Even if the neuron should contribute to the output of an example, the gradient is zero and so gradient descent can't update it. Other activation functions have been defined and studied to try to get the best of both worlds.
