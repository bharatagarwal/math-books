# Chapter 16 Groups

> We need a super-mathematics in which the operations are as unknown as the quantities they operate on, and a super-mathematician who does not know what he is doing when he performs these operations. Such a super-mathematics is the Theory of Groups.
>
> – Sir Arthur Eddington

In Chapter 10 we briefly discussed the shift in mathematics from thinking about objects to thinking about transformations between objects. This shift was radical for mathematics and much of physics. It has been less dramatic for programmers, because many ideas that brewed in mathematics for centuries have commonplace analogues in programming. That, and that software matured as a discipline largely after these mathematical revolutions took hold.

Embodying part of this novelty are ideas like programs that transform other programs. You write programs. Compilers are programs that turn your programs into other programs. A program analyzes the quality of a compiler. Programs test the correctness of the compiler analyzer. Software automates the running of the tests of the correctness of the compiler analyzer. And, of course, you use a program to help refactor the programs that automate the running of the tests of the correctness of the compiler analyzer. It's programs all the way down.

What's less obvious to a programmer is that studying the class of transformations of an object provides insight into that object. By analogy, if you study the way a refactoring tool changes the behavior of a program, that can help you understand how the program works. Even more, it can help you understand how to write clearer and more refactorable programs. Building up a theory based on transformations is like a slick development framework, which you later learn applies to programs you never anticipated writing. Group theory is a fantastic example of this.

Group theory is the mathematical study of symmetry. As we'll see in this chapter, symmetry has algebraic structure. We can work with symmetry in much the same way we do algebra with numbers or matrices. This is why group theory is part of a general area of mathematics called abstract algebra.

The original insight of group theory, bringing us full circle to Chapter 2, is that the roots of a single-variable polynomial have symmetric structure. Such structure can be formulated as a group, and used to analyze the properties of a polynomial. Or, as the case may have it, to make general statements about all polynomials. Indeed, as we mentioned in Chapter 8, it can be hard to analytically find the roots of a polynomial of large degree. By "analytically" I mean in the sense of the quadratic formula: a single algebraic expression using elementary operations, involving the coefficients of the polynomial, which one could use to find all the roots. The difficulty of this motivated us to derive and implement Newton's method for numerically finding approximate roots.

We have group theory in part to thank for not wasting our time on the analytical approach. Using group theory one can prove that it's not merely *difficult* to find an algebraic formula for the roots of a generic degree-$5$ polynomial. It's impossible. We foreshadowed this in Chapter 2 when we discussed existence and uniqueness. This theorem—known as the Abel-Ruffini theorem—is a crown jewel of mathematics. And though this book is too short to do the theorem justice, the modern proof relies heavily on the shift in thought from objects to transformations.

A second perspective on groups is understood easily, almost trivially, from programming. One beautiful aspect of group theory is how it allows one to cleanly compartmentalize the difference between a mathematical object and its representation. The definition of a group serves as an interface or a template class—in the sense of object-oriented programming—and concrete groups are semantically equivalent implementations of this interface in different contexts. True surprises occur when a family of objects that has been studied for a long time is discovered to implement the group interface. Such is the case with elliptic curves of cryptography fame. Any time a field of mathematics has the word "algebraic" prepended to it—such as algebraic geometry or algebraic topology—you automatically know the subject is about finding algebraic structures like groups hidden among seemingly non-algebraic company. When such miracles occur, you can leverage the power of algebra to compute in the cleaner, abstract setting of the algebraic structure.

Michael Atiyah, a famous geometer, once quipped,

> Algebra is the offer made by the devil to the mathematician. The devil says: "I will give you this powerful machine, it will answer any question you like. All you need to do is give me your soul: give up geometry and you will have this marvellous machine."

Hermann Weyl echoed a similar idea seventy years earlier: "In these days the angel of topology and the devil of abstract algebra fight for the soul of each individual mathematical domain." While these seem like superstitious warnings to the unsuspecting apprentice of mathematics, the utility of algebra for computation is undeniable. If there's anything to read from these quotes, it's that geometric arguments are considered fashionable, pure, and beautiful by a certain group of influential mathematicians. Subcultures abound.

But you, dear programmer, would never patronize computation as mere contentedness. We know deep in our hearts that computation is beautiful. It deserves to be cherished as an equal to geometry, analysis, logic, and the rest. Algebra deserves our special attention in that, to the extent it destroys geometry, it enables computation.

![Figure 16.1: A square with each of its corners labeled.](09 - Groups_images/img-0.jpeg)

The most common example of a group—and its raison d'être—is the set of symmetries of some object. That is to say, a group is nothing if it does not "act" on some set by transforming it in a composable, reversible way. You use groups to elucidate the symmetry in objects of interest. In this final chapter we'll see how the concept manifests itself in Euclidean and hyperbolic geometry, and in the exercises we'll explore groups as they show up in number theory, cryptography, polynomials, graphs, and others.

We'll finish off the chapter, and the book, with a dive into hyperbolic geometry. We'll see how geometry can be studied via the groups that transform geometric space. Finally, we'll apply what we learned to draw hyperbolic tessellations, of the same sort that M.C. Escher studied to create his art.

## 16.1 The Geometric Perspective

The simplest approach to understanding groups as objects describing symmetry is with geometry. Picture a square in the plane. We're going to transform this square. To keep track of what we're doing, we label each corner with a letter, as in Figure 16.1.

Now imagine cutting this square out of the plane, doing some kind of rigid physical manipulation, and placing it back into the same hole so that it fills up all the same space. For example, you could rotate the square counterclockwise by a quarter turn, or reflect it across the $AC$ diagonal, or both. These are rigid motions of the square. As functions, they are bijections from the square to itself. Moreover, they preserve the distances between all pairs of points. In symbols, let's give coordinates $(x,y)$ to the square. Say the square is the product of two intervals

$$
Q = [0, 1] \times [0, 1] = \{(x, y) \in \mathbb{R}^{2} : 0 \leq x, y \leq 1\},
$$

and call $f(x,y)$ one of the rigid motions described above. Then $f:Q\to Q$ has the property that for every pair of points $(x_{1},y_{1}),(x_{2},y_{2})$, the distance between $(x_{1},y_{1})$ and $(x_{2},y_{2})$ is equal to the distance between $f(x_{1},y_{1})$ and $f(x_{2},y_{2})$.

**Definition 16.1.** Given a set $X$, a *metric* is a non-negative function $d: X \times X \to \mathbb{R}$ with the following three properties:

- $d(x, y) = 0$ if and only if $x = y$.
- $d(x, y) = d(y, x)$ for all $x, y \in X$.
- The "triangle inequality": $d(x, y) \leq d(x, z) + d(z, y)$ for all $x, y, z \in X$.

These properties make an arbitrary function sensible enough that one could reasonably call it a "distance" function. Of particular interest is the triangle inequality, which says that taking a direct path from $x$ to $y$ is never worse than taking an indirect path through $z$.

In Chapters 10 and 12 we discussed how the Euclidean inner product gives rise to a distance metric

$$
d(x, y) = \|x - y\| = \sqrt{\langle x - y, x - y \rangle}.
$$

This metric is the same metric for Euclidean geometry. However, not all metrics arise from an inner product. Our study of hyperbolic geometry will produce a highly nonlinear metric, so it's worth teasing apart the two concepts.

**Definition 16.2.** Let $X$ be a set with a distance function $d: X \times X \to \mathbb{R}$. An *isometry* or *rigid motion* of $X$ is a bijection $f: X \to X$ such that $d(x, y) = d(f(x), f(y))$ for every $x, y \in X$.

Back to our example of the square. Since we labeled the corners, we can track how an isometry affects the corners. And in a sense that will become clear shortly, we *only* care about how it affects the corners. If we denote a counterclockwise quarter-turn by $\rho$ (the Greek lower-case rho) and a flip across the $AC$ diagonal[^flip] by $\sigma$ (the Greek lower-case sigma), we can write down a sequence of these operations like

$$
\rho \rho \sigma \rho,
$$

where we apply the operations in order from right to left. That is, the above operation is "rotate a quarter turn, then flip, then rotate twice more." Figure 16.2 shows how the symmetries transform the square.

[^flip]: This flip is specific to the *initial* position of $A$ and $C$. As $A$ and $C$ move around, the flip operation is still top-left-corner to bottom-right-corner. Of course, you want the definition of an operation to be independent of what operations are applied before or after it, so this configuration-independent definition is best.

We often emphasize that we're talking about isometries that preserve the square—map points in the square to other points in the square—by calling these isometries *symmetries* of the square. Such a provocative name encourages the natural question: what are all of the different symmetries of the square? There are infinitely many ways to compose symmetries on paper, but two symmetries created via different methods can result in the same operation.

<!-- carousel -->
![Figure 16.2: Example symmetries of the square.](09 - Groups_images/img-1.jpeg)
![Figure 16.2 (continued): Composing a rotation with a reflection.](09 - Groups_images/img-2.jpeg)
![Figure 16.2 (continued): The result of the composite symmetry.](09 - Groups_images/img-3.jpeg)
<!-- endcarousel -->

To study this, we identify some core properties of symmetries.

- The operation where we "do nothing" (the identity function $f(x, y) = (x, y)$) is a symmetry.
- Every symmetry has an opposite symmetry. This follows from isometries being bijections.
- We can compose any two symmetries to get another symmetry.

Two different ways to compose symmetries can result in the same symmetry. Flipping across the same diagonal twice is the same thing as doing nothing, and rotating four times in the same direction is also the same thing as doing nothing. Note we only consider the relative change of the square compared to how it started. To apply the next rigid motion in a sequence, you need not know how it was previously transformed.

A symmetry of the square is completely determined by how it acts on the corners. We sketch a proof. By our requirement that distances are preserved, the corners must also go to corners. Specifically, opposite diagonal corners have a maximal distance between any two points in the square. Their distance can't be achieved except by opposite-corner points. Once the corners are chosen every other point in the square is required to be a certain distance from each corner. And there is a short but not completely trivial proof that three or more circles (whose centers don't form a line) that have a simultaneous intersection point must have exactly one such point. Figure 16.3 shows an example.

As an exercise, flesh out this proof sketch in more detail. However, be warned that not all possible labelings of the corners arise from symmetries of the square. Opposite corners of the square cannot be mapped by an isometry to neighboring corners.

![Figure 16.3: The position of a point is uniquely determined by its distance from the three corners.](09 - Groups_images/img-4.jpeg)

With a handful of symmetries, such as our $\rho$ and $\sigma$ from earlier, we can write down compositions of those symmetries, and make equations of symmetries. The following three are some particularly simple ones:

$$
\rho^{4} = 1
$$

$$
\sigma^{2} = 1
$$

$$
\rho \sigma \rho = \sigma
$$

Where $1$ is a placeholder for the identity symmetry. The suggestive algebraic notation hints at our goal: $1$ is the multiplicative identity satisfying, e.g., $\rho \cdot 1 = \rho$. We even write $\rho^{-1}$ as the quarter-turn in the reverse direction.

These three identities allow us to reduce complicated expressions, such as $\sigma \rho^{9}\sigma \rho^{-3}\sigma$, to a more tractable form. The geometric picture of applying symmetries give way to mechanized computation. The notation bears the burden of the mental picture. Note that below we mostly use $\rho \sigma \rho = \sigma$ to reduce the large powers of $\rho$.

$$
\begin{aligned}
\sigma\rho^{9}\sigma\rho^{-3}\sigma
&= \sigma(\rho^{9}\sigma\rho^{9})\rho^{-12}\sigma \\
&= \sigma(\rho^{8}\sigma\rho^{8})\rho^{-12}\sigma \\
&\;\;\vdots \\
&= \sigma(\rho\sigma\rho)\rho^{-12}\sigma \\
&= \sigma^{2}\rho^{-12}\sigma \\
&= \sigma^{2}(\rho^{4})^{-3}\sigma = 1\cdot(1)^{-3}\cdot\sigma = \sigma.
\end{aligned}
$$

This kind of bookkeeping is exactly what a computer should do for us. Representing each symmetry as a permutation of the corners $A,B,C,D$, we can build the entire group from $\rho$ and $\sigma$, confirm it has eight elements, and let Python carry out the very reduction above—turning the geometric picture into a mechanical check.

```python
<!-- include: code/pim/09 - Groups/02_dihedral_square.py -->
```

As you might have guessed, the properties we've identified are what define a group, and the algebra above is characteristic of doing algebra with a group structure. Before we see the formal definition, here's a more complicated example of a group: the symmetries of the Rubik's cube.

In the same way that we can enumerate all possible symmetries of the square, one could enumerate all possible symmetries of the Rubik's cube. One can rotate any one of the six faces of the cube, but the relationships between operations are not at all obvious. The colored stickers take place of $A,B,C,D$ labels to distinguish two configurations, but it's not clear which (if any) stickers are superfluous. Nevertheless, the same properties hold: there is a do-nothing operation, every operation is reversible, and any two operations can be composed and the result is still a viable operation. As we've suggested, if you want to understand the Rubik's cube, you should study its group of symmetries.

## 16.2 The Interface Perspective

The three properties of symmetries sculpt the formal definition of a group as an interface.

**Definition 16.3.** A group $(G,\cdot)$ is a set paired with a binary operation $\cdot:G\times G\to G$, so that the following properties hold:

1. $G$ contains an identity element denoted $e$ for which $e\cdot x=x$ and $x\cdot e=x$ for all $x\in G$. (A priori there may be more than one identity element.)
2. For every $x\in G$ there is some element $y\in G$ called an "inverse" for which $x\cdot y=e$ and $y\cdot x=e$. (A priori there may be more than one such inverse.)
3. The group operation is associative. That is, $x\cdot(y\cdot z)=(x\cdot y)\cdot z$.

People often say that a set $G$ is a group "under" an operation instead of "paired with." There are a few issues we need to tackle regarding this definition and the notation associated with it, but first let's see some trivial examples.

The singleton set $\{e\}$ with the binary operation $\cdot$ defined by asserting $e\cdot e=e$ is a group. And there was much rejoicing. The set of integers $\mathbb{Z}$ forms a group under the operation of addition. It is common knowledge that zero fits the definition of the identity element, that the sum of two integers is an integer, that addition on integers is associative, and that every integer $x$ has an additive inverse $-x$.

Likewise, all of the number systems in this book except $\mathbb{N}$ are groups under addition: rational numbers, real numbers, complex numbers, etc. If we want to work with multiplication, it is not hard to see that $\mathbb{R}-\{0\}$ is a group, since every nonzero real number has a multiplicative inverse, and $1$ is the multiplicative identity. Vector spaces are groups under vector addition; indeed, the group axioms are a subset of the vector space axioms.

An important example comes from our discussion in Chapter 9, the set of integers modulo $n$, denoted $\mathbb{Z}/n\mathbb{Z}$, under the operation of addition modulo $n$. For example, $\mathbb{Z}/4\mathbb{Z}=\{0,1,2,3\}$.

Definition 16.3 reads like an interface, so let's implement it. The most honest way to *believe* that $\mathbb{Z}/n\mathbb{Z}$ is a group is to check each axiom exhaustively—the unit test Kun says you should write the instant you read a definition. The function below takes any finite set, an operation, and a claimed identity, and verifies closure, identity, inverses, and associativity. We run it on $\mathbb{Z}/n\mathbb{Z}$ for several $n$, and watch it correctly *reject* $\mathbb{Z}/6\mathbb{Z}$ under multiplication (where $0,2,3,4$ have no inverse) while accepting the unit group $\{1,5\}$.

```python
<!-- include: code/pim/09 - Groups/01_group_axioms.py -->
```

A few basic propositions clear up the ambiguities in Definition 16.3. For instance, the uniqueness of the identity element follows from the other axioms of a group. Here's a proof: if there were two identity elements $e,e^{\prime}$, then by the following logic they must be equal:

$$e=e\cdot e^{\prime}=e^{\prime}$$

The first equality holds because $e^{\prime}$ is an identity element, and the second because $e$ is. A similar proof shows that the inverse of an element is unique. These facts justify the following notation: we call *the* identity element $1$, and use subscripts $1_{G},1_{H}$ to distinguish between identity elements in different groups $G,H$. We also replace the explicit $\cdot$ operation with an invisible operation (juxtaposition). So that $xyz$ replaces $x\cdot y\cdot z$. Moreover, we emulate repeated applications of the operation by saying $x^{n}$ to mean $x\cdot x\cdot\cdots\cdot x$ multiplying $n$ copies of $x$.

One more caveat to support "legacy" math. If we're talking about the integers $\mathbb{Z}$ under addition, the juxtaposition operation (which implies multiplication) feels unsanitary. It simply won't do. In this case, and whenever we have a group of numbers with a $+$ symbol as the operation, we'll use $+$. And instead of $x^{n}$ we'll use $nx$ to mean $x+x+\cdots+x$ adding $n$ copies. Here $n$ is not considered an element of $\mathbb{Z}$ as a group, but just the number of additions. Likewise, $-x$ is the inverse of $x$, while in a multiplicative group the inverse is $x^{-1}$. This is purely syntactic sugar.

Now we demonstrate how two drastically different sets can have the same underlying group structure, which will inform our dive into structure-preserving mappings between groups. The first group we understand well: $\mathbb{R}$ under addition. For the second, consider the set of $2\times 2$ matrices of the following form, under the operation of matrix multiplication.

$$ G=\left\{\begin{pmatrix}1&a\\ 0&1\end{pmatrix}:a\in\mathbb{R}\right\} $$

The identity matrix is the identity element. Notice $G$ has some familiar structure:

$$ \begin{pmatrix}1&a\\ 0&1\end{pmatrix}\begin{pmatrix}1&b\\ 0&1\end{pmatrix}=\begin{pmatrix}1&a+b\\ 0&1\end{pmatrix}. $$

Indeed, matrix multiplication in $G$ corresponds to addition of the top-right entry of the matrix. This suggests the natural bijection $f:\mathbb{R}\to G$ defined by

$$ x\mapsto\begin{pmatrix}1&x\\ 0&1\end{pmatrix}. $$

Addition of the inputs corresponds exactly to multiplication of the corresponding matrices! The fact that these *particular* groups have the same underlying structure isn't all that shocking. What's deep is that we have two different concrete representations for the same abstract algebraic structure. Not only are the elements in bijective correspondence, but the *operations* are as well! Even better, this family of matrices has a geometric interpretation as a shear transformation along the horizontal axis. This bijection shows that the compositional structure of shearing (in a fixed direction) is identical to the additive structure of the magnitude of the distortion. With that comes all the benefits of understanding real numbers.

We can watch this correspondence hold up under random inputs: the map $f$ turns addition of reals into multiplication of shear matrices, and we recover the real number by reading the matrix's top-right entry, so $f$ is a bijection. That makes $(\mathbb{R},+)$ and the shear group genuinely isomorphic.

```python
<!-- include: code/pim/09 - Groups/03_shear_iso.py -->
```

Any mathematical setting that expresses the abstract group $\mathbb{R}$ can be identified by finding this sort of group-correspondence with $(\mathbb{R},+)$. A mathematician sees this wonderful example and dreams: can we classify all the different kinds of group structures? Could we get a new perspective on the symmetry group of the square by turning it into a suitable group of matrices?

Before we get ahead of ourselves, let's make these structure-preserving maps precise.

## 16.3 Homomorphisms: Structure Preserving Functions

To study the structure of groups, we study the structure of compatible functions between groups. By "compatible," I mean the group structure is somewhat preserved.

**Definition 16.4.** Let $G,H$ be groups under multiplication. A function $f:G\to H$ is called a *homomorphism* if for every $x,y\in G$, $f(xy)=f(x)f(y)$. The multiplication on the left is in $G$ and the multiplication on the right is in $H$.

Homomorphisms between groups don't necessarily preserve everything about a group. In particular, they need not be bijections. But they do preserve the defining features of the group structure. To build up intuition we can do some simple proofs.

**Proposition 16.5.** *Group homomorphisms preserve the identity.*

*Proof.* Let $G$ be a group with identity $1_{G}$, and $H$ a group with identity $1_{H}$. Let $f:G\to H$ be a homomorphism. Since $f$ preserves the group operation,

$$f(1_{G})=f(1_{G}1_{G})=f(1_{G})f(1_{G})$$

Since $H$ is a group, all its elements have inverses, including $f(1_{G})$. So multiply both ends by $f(1_{G})^{-1}$ to get

$$
\begin{aligned}
f(1_{G})f(1_{G})^{-1} &= f(1_{G})f(1_{G})f(1_{G})^{-1} \\
1_{H} &= f(1_{G})1_{H}=f(1_{G})
\end{aligned}
$$

$\blacksquare$

**Proposition 16.6.** *Group homomorphisms preserve inverses.*

*Proof.* If $x\in G$ and $f:G\to H$ is a homomorphism, then

$$1_{H}=f(1_{G})=f(xx^{-1})=f(x)f(x^{-1})$$

And likewise for $f(x^{-1}x)$. Taking the left- and rightmost ends, we've shown that $f(x^{-1})f(x)=f(x)f(x^{-1})=1_{H}$. In particular, the inverse of $f(x)$ is $f(x^{-1})$. Another way to say this is that $f(x)^{-1}=f(x^{-1})$.

$\blacksquare$

The extent to which a homomorphism degrades the structure of the input group is tracked by what elements are mapped to the identity.

**Definition 16.7.** Let $G,H$ be groups, and $f:G\to H$ a homomorphism. Then the kernel of $f$, denoted $\ker f$, is the set

$$\ker f=\{x:f(x)=1_{H}\}$$

An example: $G=\mathbb{Z}$ under addition and $H=\mathbb{Z}/10\mathbb{Z}$ under addition modulo $10$. Let $f:G\to H$ mapping $n\mapsto 2n\bmod 10$ (Exercise: prove this is a homomorphism). The kernel of $f$ is $\{0,\pm 5,\pm 10,\pm 15,\dots\}$. Despite losing the multiples of $5$, the image $f(G)$ still has a group structure inside $H$. Note $f(G)=\{0,2,4,6,8\}$, and the group operation in $H$—applied only to elements of $f(G)$—maintains the property of being in $f(G)$. In other words, part of the structure of $G$ is embedded inside $H$ using the operation of $H$, but not all of it.

This running example is concrete enough to run. We verify the homomorphism law $f(a+b)=f(a)+f(b)$, read off the kernel as exactly the multiples of $5$, and confirm the image $\{0,2,4,6,8\}$ is closed under addition mod $10$. We also check the punchline that the quotient $\mathbb{Z}/\ker f$ is isomorphic to $\mathbb{Z}/5\mathbb{Z}$, since each equivalence class $[n]$ is just $n \bmod 5$.

```python
<!-- include: code/pim/09 - Groups/04_homomorphism_kernel.py -->
```

A group that sits inside another group (and shares the containing group's operation) is called a subgroup.

**Definition 16.8.** Let $H\subset G$ be two sets and let $G$ be a group under the operation $\cdot$. Then $H$ is called a subgroup of $G$ if:

- $1\in H$.
- For all $x,y\in H$, it's true that $x\cdot y\in H$.
- If $x\in H$, then so is $x^{-1}$.

Another term for the above conditions is that $H$ is "closed" under $\cdot$ and the inverse-taking operation $(-)^{-1}$.

Our observation about the image of a homomorphism being a group is no coincidence. A homomorphism provides two useful subgroups: its image and its kernel.

**Theorem 16.9.** *Let $G,H$ be groups and $f:G\to H$ be a group homomorphism. Then $\ker f$ is a subgroup of $G$ and $\operatorname{im}f$ is a subgroup of $H$, where $\operatorname{im}f$ denotes the image of $f$.*

*Proof.* First we prove that $\ker f$ is a subgroup of $G$. We'll prove this directly, by assuming $x,y$ are arbitrary elements of $\ker f$, and showing that $xy\in\ker f$ and $x^{-1}\in\ker f$. These are the second two conditions required of a subgroup by Definition 16.8, and the first condition, $1_{G}\in\ker f$, is implied by Proposition 16.5.

If $x,y\in\ker f$, then $f(xy)=f(x)f(y)=1\cdot 1=1$, so $xy\in\ker f$. Likewise, since group homomorphisms preserve inverses, $f(x^{-1})=f(x)^{-1}=1^{-1}=1$.

Next we'll prove $\operatorname{im}f$ is a subgroup of $H$. Let $x,y\in\operatorname{im}f$. By the definition of the image, there are two elements $a,b\in G$ for which $f(a)=x,f(b)=y$. Then $f(ab)=f(a)f(b)=xy$, which by definition means that $xy$ is in the image of $f$. Likewise, $f(a^{-1})=f(a)^{-1}=x^{-1}$, so $x^{-1}$ is in the image of $f$. Again, Proposition 16.5 implies $1_{H}\in\operatorname{im}f$.

$\blacksquare$

As we discussed in Chapter 9, any set-function $f:G\to H$ defines a natural equivalence relation on the domain. When $f$ is a homomorphism, the corresponding set-quotient maintains the group structure of $G$. Appropriately, it's called the *quotient group*.

Let $f:G\to H$ be a group homomorphism. Define an equivalence relation whereby two elements $a,b\in G$ are equivalent if and only if $ab^{-1}\in\ker f$. Or, in terms of additive groups, $a-b\in\ker f$. Note that this aligns with the equivalence relation defined in Chapter 9 using $f(a)=f(b)$, since then $f(ab^{-1})=f(a)f(b)^{-1}=1_{H}$, from which it follows that $ab^{-1}\in\ker f$ if and only if $f(a)=f(b)$. The quotient group is denoted $G/\ker f$, and if $\ker f$ is a known subgroup, the notation for that subgroup is often used instead.

Take $\mathbb{Z}$ with addition, and the map $f:\mathbb{Z}\to\mathbb{Z}/10\mathbb{Z}$ defined by $x\mapsto 2x$ modulo $10$. The kernel of this map is the subgroup $\{0,\pm 5,\pm 10,\pm 15,\dots\}$. The quotient $\mathbb{Z}/\ker f$ is the set of equivalence classes $\{[0],[1],[2],[3],[4]\}$. The numbers $3$, $8$, and $-22$ are all in the equivalence class $[3]$, because, for example, $3-(-22)=25\in\ker f$. The group operation on $\mathbb{Z}$ passes to the equivalence classes, so that $[a]+[b]=[a+b]=[a+b\bmod 5]$. The quotient group is suspiciously similar to $\mathbb{Z}/5\mathbb{Z}$. Indeed, they are isomorphic (cf. the upcoming Definition 16.11).

**Lemma 16.10.** *For any homomorphism $f$, the quotient set $G/\ker f$ forms a group under the operation $[a][b]=[ab]$.*

*Proof.* You will prove this in the exercises. $\blacksquare$

Finally, if $\ker f=\{1\}$, then $f$ is necessarily an injection. Such homomorphisms completely preserve the structure of the input group, embedded via the image of $f$ inside the codomain. In the added case that $f$ is a surjection, then $f$ completely preserves the structure of the group.

**Definition 16.11.** Let $G$ and $H$ be groups. A homomorphism $f:G\to H$ is called an isomorphism if it is a bijection. If there is an isomorphism between $G$ and $H$, we call them isomorphic.

If $G$ and $H$ are isomorphic, they have identical group structure, and $H$ is simply a relabeling of the elements of $G$. The boolean comparison (or assertion) that two groups $G,H$ are isomorphic is denoted $G\cong H$. And in words, we say that two groups are the same "up to isomorphism," meaning only their representations are different. For our "suspicious" example above, $\mathbb{Z}/\ker f\cong\mathbb{Z}/5\mathbb{Z}$.

A simple theorem relates the groups defined by a homomorphism.

**Theorem 16.12 (The first isomorphism theorem).** *Let $G,H$ be groups, $f:G\to H$ a homomorphism. Then $\operatorname{im}f\cong G/\ker f$.*

## 16.4 Building Blocks of Groups

If you're tasked with understanding a mysterious group $G$, perhaps encountered in a wildly non-algebraic locale such as the symmetries of geometric solids, the general strategy is to find homomorphisms between $G$ and other groups you understand well. A homomorphism $f:G\to H$ gives you two groups related to $G$: $\ker f$ and $G/\ker f$. Meanwhile, a homomorphism $g:H\to G$ gives the subgroup $\operatorname{im}g$. Each is a local piece of information about $G$ that you can use to reconstruct a global picture of $G$. I like to think of it like shining a light on an object, so that we can observe the shadow projected on a wall. To support this, every enterprising algebraist has a repertoire of concrete groups to use as building blocks.

The most common, as we've seen multiple times in this chapter, are the integers under addition, their subgroups, and their quotients, under addition and addition modulo $n$. These arise as the kernels and quotients of the maps $\mathbb{Z}\to\mathbb{Z}$ defined by $x\mapsto nx$. The kernels have the form $n\mathbb{Z}=\{nx:x\in\mathbb{Z}\}$ for some fixed $n$, and also the trivial subgroups $\{0\},\mathbb{Z}$. The quotients are denoted $\mathbb{Z}/n\mathbb{Z}$.

The groups $\mathbb{Z}$ and $\mathbb{Z}/n\mathbb{Z}$ both have the property that $1$, when repeatedly added to itself, produces the entire group. Because of this, $1$ is called a generator of the group. In general, an element $x\in G$ is called a generator if the subgroup $\{1,x,x^{2},x^{3},\dots\}$ is equal to $G$. Groups with such an element are called cyclic groups, and all cyclic groups are isomorphic to $\mathbb{Z}$ or $\mathbb{Z}/n\mathbb{Z}$ under addition. In general, a set $S\subset G$ is said to generate $G$ if every $x\in G$ is a product of elements in $S$. A generating set of a group is like a vector space basis, but a group $G$ may have generating sets of different sizes. Hence, any concept of "group dimension" must be more nuanced.[^dim]

[^dim]: Even worse, the minimal generating set is not always unique, and for some groups there's no finite generating set at all.

<!-- carousel -->
![Figure 16.4: Because 5 is odd, the lines of symmetry of the regular pentagon each pass through a side and a vertex.](09 - Groups_images/img-5.jpeg)
![Figure 16.4 (continued): Because 6 is even, the hexagon's lines of symmetry pass through either two opposite vertices or two opposite edge midpoints.](09 - Groups_images/img-6.jpeg)
<!-- endcarousel -->

One of the simplest ways to build a larger group from smaller pieces is the direct product. This construction simply forms the product of two groups as sets, and defines the group operation component-wise. E.g., $\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ is the set of pairs $\{(n,b) \mid n \in \mathbb{Z}, b \in \{0,1\}\}$, where $(n,b) + (n',b') = (n + n',b + b')$. If a group decomposes as a direct product of subgroups, the symmetry structure can be seen to have independent components.

The set $\mathbb{Z}/n\mathbb{Z}$ forms a group under multiplication if we remove the numbers $k$ such that $\gcd(n, k) \neq 1$. This guarantees that inverses exist. In the special case that $n$ is prime, we need only remove zero. This group is denoted $(\mathbb{Z}/n\mathbb{Z})^{\times}$, and it's substantially more interesting than integers under addition. Up to isomorphism it is always possible to write $(\mathbb{Z}/n\mathbb{Z})^{\times}$ as a direct product of cyclic groups. However, there is no known generic method for finding generators of the cyclic pieces. This computational difficulty is exploited by RSA public-key cryptography, which we will explore in an exercise.

Next we have the symmetry groups of regular convex polygons in the plane, such as the square we started this chapter with. The group corresponding to the polygon with $n \geq 3$ sides is called the dihedral group and is denoted $D_{2n}$. It has $2n$ elements, corresponding to the $n$ rotations by an angle of $2\pi/n$ and the $n$ reflections across lines passing through the vertices and sides. These lines of symmetry depend on the parity of $n$, as is made clear by the lines of symmetry in the pentagon and the hexagon in Figure 16.4. Confusingly, the dihedral group for a polygon with $n$ sides is sometimes denoted $D_{n}$ instead of $D_{2n}$, which makes $D_{8}$ terribly ambiguous. We'll use $D_{2n}$.

Dihedral groups are not cyclic. Each $D_{2n}$ is generated by $\rho$ and $\sigma$, where $\rho$ is a rotation by $2\pi/n$ and $\sigma$ is a reflection across some axis of symmetry. Because two elements generate the entire group, you might guess $D_{2n}$ to be isomorphic to a product of two cyclic groups, $\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/n\mathbb{Z}$, with $\sigma$ generating the former and $\rho$ the latter. You might guess, and you'd be wrong. These are subgroups, but dihedral groups have extra structure because the interaction between $\rho$ and $\sigma$ is not independent. If it were, $\sigma\rho\sigma$ would equal $\sigma^{2}\rho=\rho$, but in fact $\sigma\rho\sigma=\rho^{-1}$. The extra structure is more precisely described by a *semi-direct product*, which you will see in the exercises.

Next we have matrix groups. Given any reasonably well-behaved number system that has addition and multiplication, say $\mathbb{R}$ for example, we can form a group of square matrices under matrix multiplication, which is often called the *general linear group*. Define by $GL_{n}(\mathbb{R})$ the set of invertible $n\times n$ matrices with real entries. As we saw in Section 16.2, asserting some specific structure on the groups often leads to an interesting subgroup. One famous subgroup of the general linear group is called the *orthogonal group*, denoted $O_{n}(\mathbb{R})$, consisting of matrices whose columns form orthonormal bases.

$$O_{n}(\mathbb{R})=\{A\in GL_{n}(\mathbb{R})\mid A^{T}A=I_{n}\}.$$

This group is closely related to the symmetry group of Euclidean space we'll study in Section 16.5. Another interesting facet of groups of matrices is that they have enough structure that one can do calculus on them. In the formal jargon, the general linear group is a smooth manifold. This is far beyond the scope of this book, but at least explains why the general linear group gets such a special name.

The last example is called the *symmetric group*. Really, it should be called the *permutation group*, since it is the set of all bijections of a fixed set to itself. Let $A$ be a set, and define the *symmetric group* $S(A)$ to be the set of all bijections $A\to A$. It is easy to see that if $A,B$ are both finite sets of size $n$, then $S(A)\cong S(B)$. In that case, denote $S(A)$ by $S_{n}$. In the exercises you will study the structure of finite permutation groups, and a useful data representation for computation.

The symmetric group is small enough to lay out entirely. For $S_{3}$ we can print its full $6\times 6$ Cayley table, then exhaustively enumerate every subgroup. Doing so verifies Lagrange's theorem (Exercise 16.7): the order of every subgroup divides the order of the group. Here $|S_3|=6$, and the subgroups have orders $1,2,3,6$, each of which divides $6$.

```python
<!-- include: code/pim/09 - Groups/05_lagrange_s3.py -->
```

As it turns out, every group is a subgroup of a symmetry group. The proof is simple: every group $G$ has a group homomorphism $f:G\to S(G)$, where $a\in G$ defines the bijection $x\mapsto ax$ (the inverse is $x\mapsto a^{-1}x$). Since $\operatorname{im}f$ is a subgroup of $S(G)$ and $\ker f\cong\{1\}$, we have that $G\cong\operatorname{im}f$. One takeaway is that if you want to write programs that do computations on finite groups, it's enough to write programs that work with finite permutation groups. Indeed, most useful group-theoretic algorithms are algorithms on finite permutation groups. Entire books have been written about this.

This embedding—Cayley's theorem—is itself a short program. For $G=\mathbb{Z}/5\mathbb{Z}$ we turn each element $a$ into the permutation $x\mapsto a+x$, check that the map is a homomorphism with trivial kernel (hence injective), and confirm its image is a subgroup of $S_5$.

```python
<!-- include: code/pim/09 - Groups/06_cayley_theorem.py -->
```

## 16.5 Geometry as the Study of Groups

For the rest of the chapter, we're going to study geometry from the perspective of groups. In fact, the modern mathematical attitude toward geometry is that it *is* the study of groups. This view was espoused by Felix Klein in the late 1800's. Around this time, special cases of projective geometry and hyperbolic geometry had been discovered, but it was largely unclear how different geometries were related.

In general, to define a geometry you need to define a few things:

- A set $X$ of points (the space), and a set of lines.
- A prescription of incidence, i.e., what points lie on what lines.
- A quantity of interest that you want to study. For example, you may want to measure length. In that case, you need a metric $d:X\times X\to\mathbb{R}$.

With these in hand, the symmetry group of the space is the set of bijections $X\to X$ that preserve the quantity of interest. In Euclidean geometry, points and lines are the usual points and lines in $\mathbb{R}^{n}$, and distance is the quantity of interest. Such "quantities of interest" are called invariants. A different type of geometry might only wish to preserve area of figures, or preserve the property of similarity (invariance under scaling).

Klein's view was that a geometry should be studied via its group of symmetries. The classical concepts like angles, areas, and lengths are seen as measures that may or may not be invariant under the application of a symmetry. Thus, geometry has two approaches: given a group of symmetries, study the interesting quantities invariant to those transformations; and given a quantity you think is important, find the group of symmetries that preserves that quantity. Every geometry has a group. Every group corresponds to some geometry.

Klein called his view the Erlangen Program. One striking result was that all geometries are a special case of projective geometry—a geometry that allows projections to a possibly infinite horizon. In particular, even though different geometries might have different axioms (regarding, say, configurations of parallel lines), every geometry can be modeled inside of a projective geometry. For example, hyperbolic geometry is projective geometry restricted to a particular surface inside a larger projective space. Moreover, the group corresponding to this model of hyperbolic geometry is a subgroup of the symmetry group of the projective geometry. We get containments of the spaces as sets, and of the groups as subgroups.

$$\text{Hyperbolic geometry} \subset \text{Projective geometry}$$
$$\text{Hyperbolic group} \subset \text{Projective group}$$

We won't study this particular relationship in this book, but it shows how Klein's desire fits into the larger mathematical goal: to connect and unify disparate geometries into a single theory. I encourage the reader interested in cryptography to learn about projective geometry, in part because it's the correct setting for studying elliptic curves. It's also a great way to exercise your linear algebra muscles, as projective geometry is simply a quotient of the vector space $\mathbb{R}^n$ by a suitable equivalence relation.[^proj]

[^proj]: A while back I wrote a blog series on this topic, in which I build up elliptic curve cryptography from scratch. The second post in the series defines projective geometry as a quotient. You can find it here: <https://jeremykun.com/2014/02/08/introducing-elliptic-curves/>.

We now turn to Euclidean geometry, and study it through the lens of groups.

### Euclidean Geometry

Euclidean geometry is the study of isometries of $\mathbb{R}^n$ with the usual distance metric $d(x,y) = \|x - y\|$. Recalling Definition 16.2, $f: \mathbb{R}^n \to \mathbb{R}^n$ is an isometry if $d(x,y) = d(f(x),f(y))$ for all $x,y \in \mathbb{R}^n$. Because isometries preserve distance, and angle measure is determined by the lengths of the sides of triangles, isometries also preserve angle measure.

With a few moments of thought, it's easy to come up with examples of Euclidean isometries for the plane:

1. Translations by a fixed vector, i.e., $x \mapsto x + v$.
2. Reflections through a subspace $W$ of dimension $n - 1$. I.e., given $x$, first compute $w = \operatorname{proj}_W(x)$, then output $x - 2(x - w)$.
3. Rotations around points (in 2 dimensions) or lines (in 3 dimensions).[^rot4]

[^rot4]: It is quite hard to picture rotations in 4 dimensions. As we'll see, we won't need to because reflections capture everything.

Remember that rotations, projections, and reflections are examples of linear maps. Ignoring translations for a moment, it's natural to wonder which linear maps double as isometries.

**Theorem 16.13.** *The isometries of $\mathbb{R}^n$ that fix the origin are exactly the linear maps whose columns form an orthonormal basis.*

*Proof.* In Chapter 12, we observed that matrices with orthonormal columns preserve the inner product. Let $A$ be such a matrix. In $\mathbb{R}^n$, squared distance is $d(x,y)^2 = \langle x - y, x - y \rangle$. As a consequence,

$$
\begin{aligned}
d(Ax, Ay)^{2} &= \langle Ax - Ay, Ax - Ay \rangle \\
&= \langle A(x - y), A(x - y) \rangle \\
&= \langle x - y, x - y \rangle \\
&= d(x, y)^{2}.
\end{aligned}
$$

Since distances are non-negative, the square roots are also equal.

To show that any isometry fixing the origin is a linear map with orthonormal columns, we first show it is linear. We will use slick geometric arguments, but one can prove it just as well with formulas involving inner products (which the reader is encouraged to try).

Let $f$ be an isometry that fixes the origin; we need to show $f(x + y) = f(x) + f(y)$ and $f(ax) = af(x)$ for any vectors $x, y$ and any scalar $a$.

First, $f(ax) = af(x)$. To prove this we first prove that any Euclidean isometry maps lines to lines. We will use the fact that in Euclidean geometry a straight line is the shortest path between any two points. In particular, if $x$ lies on the shortest path from $0$ to $ax$, then $f(x)$ lies on the shortest path from $0$ to $f(ax)$: letting $c = d(0, x)$, then $x$ minimizes the following:

$$
\min_{\substack{y\in \mathbb{R}^{n}\\ d(0,y) = c}}d(0,y) + d(y,ax)
$$

Any property defined entirely in terms of distances must be preserved by $f$, because $f$ preserves distances. A similar statement applies when $|a| < 1$, in which case $ax$ lies on the shortest path from $0$ to $f(ax)$.

Using the fact that isometries map lines to lines, we continue. Since $d(0, ax) = |a|\|x\| = d(0, f(ax))$, the only way $f(ax)$ can be on the same line through the origin as $f(x)$ is if $f(ax) = \pm af(x)$. We claim it must be $f(ax) = af(x)$. Suppose for contradiction that $f(ax) = -af(x)$, then there are two cases. In the first case, $|a| \geq 1$. Then,

$$
\begin{aligned}
|a|\|x\| &= d(0, f(ax)) = d(0, f(x)) + d(f(x), f(ax)) \\
&= \|x\| + \|-af(x) - f(x)\| \\
&= \|x\| + |-a - 1|\|f(x)\| \\
&= (1 + |-a - 1|)\|x\|
\end{aligned}
$$

This implies $|a| - 1 = |a + 1|$, which is only true for $a = -1$. This provides a contradiction for all $a \neq -1$. But if $a = -1$, then $f(-x) = f(x)$, which contradicts $f$ being injective. We conclude that $f(ax) = af(x)$. The second case, $|a| < 1$ is similar, and starting from $\|x\| = d(0, f(ax)) + d(f(ax), f(x))$ one arrives again at $|a + 1| = |a| - 1$.

To show $f(x + y) = f(x) + f(y)$, we additionally claim that $f$ preserves parallelism of lines (even those that do not pass through the origin). Indeed, given two lines $L_{1}, L_{2}$, define the distance between the lines as $d(L_{1}, L_{2}) = \min_{x \in L_{1}, y \in L_{2}} d(x, y)$. When $L_{1}, L_{2}$ are parallel, this distance is a positive constant, and otherwise it is zero. Since the property is defined entirely in terms of distance, an isometry must preserve it.

Now consider the parallelogram, with opposite sides being parallel line segments, and having one vertex at the origin.

![Figure: A parallelogram whose vertex sits at the origin. Vector addition is exactly the parallelogram law, so isometries—which preserve length, angle, and parallelism—must respect it.](09 - Groups_images/img-7.jpeg)

By our arguments above (isometries preserve length, angle measure, and parallelism of lines), isometries map parallelograms to parallelograms. But a parallelogram is precisely how we define addition of two vectors! The sum of the vectors representing the sides is the diagonal vector drawn from the origin to the opposite vertex.

Now that we've established isometries that fix the origin are linear maps, we already know from linear algebra that a linear map preserves distance if and only if it preserves the inner product ($d(x,y)=\|x-y\|$ is defined in terms of the inner product), which happens if and only if its columns are orthonormal. (Cf. Chapter 12, Exercise 12.3)

$\blacksquare$

This proof puts into practice Klein's idea to study invariants preserved by isometries. The invariants that can be derived from distance preservation are highly structured, allowing one to explicitly limit an isometry's shenanigans. As an added benefit, thinking in terms of invariants removes the need to rephrase geometric concepts in symbolic language. If you found the epsilon-delta proofs of calculus tedious, you might just be a geometer.

The group of $n\times n$ matrices with orthogonal unit vector columns is called the *orthogonal group* $O(n)$. Recall it has the following characterization.

$$O(n)=\{A:A^{T}A=I_{n}\}.$$

We've already shown that this set forms a group under matrix multiplication. Still, it's worthwhile to check again in purely linear algebraic terms. Each matrix represents a change of basis, and composing two basis-changes is again a change of basis. The identity is a no-op basis change, and every basis change has an inverse. Finally, orthogonality is preserved: if $A^{T}A=I_{n},B^{T}B=I_{n}$, then $(AB)^{T}(AB)=B^{T}(A^{T}A)B=B^{T}B=I_{n}$. Likewise for $A^{-1}$.

We can watch Theorem 16.13 and the group structure of $O(2)$ play out numerically. A rotation and a reflection both satisfy $A^{T}A=I$ and preserve every distance, the group is closed under products and inverses, and a generic shear—invertible but not orthogonal—fails to preserve distance, so it is not an isometry.

```python
<!-- include: code/pim/09 - Groups/07_orthogonal_group.py -->
```

Because these isometries are linear maps, we can also infer that the complete behavior of the isometry is determined by its behavior on $n$ linearly independent points. This is another example of local information being used to infer global structure.

Now the classification theorem: every isometry is a composition of an orthogonal map with a single translation.

**Theorem 16.14.** *The group of Euclidean isometries is isomorphic to the group*

$$E(n)=\{Ax+v\mid A\in O(n),v\in\mathbb{R}^{n}\}$$

*Proof.* First, we prove that $E(n)$ is a group. The identity is in $E(n)$ if we set $v=0,A=I_{n}$. Given $f(x)=Ax+v$, the inverse is $f^{-1}(x)=A^{-1}(x-v)$. Given $f(x)=Ax+v,g(x)=Bx+w$, the composition is $B(Ax+v)+w=BAx+Bv+w$. Since $O(n)$ is a group, $BA\in O(n)$, and the translation vector is $Bv+w$.

Next, fix an isometry $f$ that does not necessarily preserve the origin. Let $v=f(0)$, and define $f^{\prime}(x)=f(x)-v$, effectively translating $v$ to the origin. $f^{\prime}(0)=f(0)-v=0$ so $f^{\prime}\in O(n)$ and can be written as a matrix $A$ by Theorem 16.13. Rewrite $f$ as $f(x)=Ax+v$, which has the form required to be a member of $E(n)$. This maps an isometry $f$ to a member of $E(n)$. This mapping is a homomorphism by repeating the argument from the last paragraph: if $f=x\mapsto Ax+v$ with $v=f(0)$ and $g=y\mapsto By+w$ with $w=g(0)$, then $gf=x\mapsto BAx+Bv+w$, where $Bv+w$ is precisely $g(f(0))$. This mapping is also a bijection: if $f$ and $g$ differ, $f(0)=g(0)=v$, then $f(x)-v$ and $g(x)-v$ must differ on some basis vector, and hence have different matrix representations. Coupling this with the one-sided inverse ($Ax+v$ is an isometry for any choice of $A$, $v$), we get our bijection.

$\blacksquare$

### Hyperbolic Geometry

In antiquity, the Greek mathematician Euclid laid out a grand vision of geometry in which every theorem can be proved from a core set of axioms. The axioms, one of which was "any two points can be connected by a straight line," cannot be proved and must be taken as a truism.

Euclid's 5 axioms, published in his magnum opus, *The Elements*, were:

1. Any two points can be connected by a straight line segment.
2. Any straight line segment can be extended indefinitely to a straight line.
3. For any straight line segment, there is a circle with that line as its radius and one endpoint as its center.
4. All right angles are congruent.
5. Given any straight line and a point not on that line, there is a unique straight line that passes through the point and never intersects the first line.

The fifth axiom, commonly called "the parallel postulate," nagged mathematicians for centuries. It always seemed possible that it could be converted from an axiom to a theorem by deducing it from the other four axioms.

These efforts were sadly in vain. As is often the case, the more failed attempts at proving a claim, the more it seems the claim might be false. Indeed, the parallel postulate can be broken in a few ways. There are geometries that satisfy the first four axioms, but no parallel lines exist (all possible lines intersect the first). There are also geometries in which multiple parallel lines exist. Projective geometry is an instance of the first breakage, and hyperbolic geometry the second.

Let's now define a model of the hyperbolic plane and classify its symmetries. I say "a" because there are many models of the hyperbolic plane. The connections between them are interesting and useful, but for this chapter we'll work entirely in the model called the Poincaré disk. The Chapter Notes and Exercises contain more historical details.

The universe of points for the Poincaré disk is the interior of the unit disk, $\mathbb{D}^{2}=\{(x,y)\in\mathbb{R}^{2}\mid x^{2}+y^{2}<1\}$. One is supposed to colorfully imagine the boundary of the unit disk as a "line at infinity," a sort of horizon that lines can approach without ever reaching. To us—we omniscient beings viewing this universe from the outside—a point moving at unit speed along such a line simply appears to slow down. As we'll make clear with a distance formula, points close to the boundary grow exponentially farther away from each other compared to points near the origin.

In the Poincaré disk, there are two kinds of lines. The first is one which includes the origin, and these lines are simply diameters of the unit circle (not including the endpoints). Otherwise, a line is a segment of a circle perpendicular to the unit circle. More formally, define the angle made by two distinct, intersecting circles to be the angles made by the tangent lines to those circles at their intersection points. Because the line through the circles' centers is a line of symmetry, the angle will be the same regardless of which intersection point is chosen. A circle is perpendicular (or orthogonal) to another circle if they form right angles at their intersection points. The types of lines are displayed in Figure 16.5.

Now we can immediately see why the parallel postulate fails: parallel lines are just circles that don't intersect! Given one such circle $C$ and a point not on that circle, we can find many circles passing through the point that don't intersect $C$. This is pictured in Figure 16.6, where $C$ is the dotted line.

There is a bit of work to do to establish the axioms of geometry for this model. We need to be able to draw a line between any two points, and to draw a circle with a segment as its radius. A priori, it's not clear what a circle would look like in this model, since some lines are defined as parts of Euclidean circles. We will have to define such a "Poincaré circle." We also need to define the angle between two hyperbolic lines, and verify that right angles are all congruent. For each of these it helps to have our first hyperbolic symmetry in hand: inversion in a Euclidean circle.

**Definition 16.15.** Let $C$ be a Euclidean circle with center $x$ and radius $r$. Let $p$ be a point different from $x$. Define the inverse of $p$ with respect to $C$ as the point $p^{\prime}$ along the ray from $x$ through $p$ that satisfies:

$$d(p,x)\,d(p^{\prime},x)=r^{2}.$$

The verb for computing the inverse with respect to $C$ is "inverting in $C$." For the classical geometric construction of the inverse of $p$ in $C$: suppose $p$ is in the interior of $C$. Draw a ray from $x$ through $p$, as in Figure 16.7. Then draw a perpendicular segment from $p$ to $C$ to get a point $q$. Then the inverse $p^{\prime}$ is the intersection of the tangent to $C$ at $q$ with the ray $x\rightarrow p$.

<!-- carousel -->
![Figure 16.5: Lines in the Poincaré disk. The solid black line is the boundary of the disk. The dashed diameters are one type of line. The arcs of the dashed circles are another. The circles must intersect the boundary of the disk at perpendicular angles.](09 - Groups_images/img-8.jpeg)
![Figure 16.6: Given the dotted Poincaré line and the indicated point, all three dashed lines pass through the point without ever intersecting the dotted line. The parallel postulate fails.](09 - Groups_images/img-9.jpeg)
![Figure 16.7: The construction of the inverse of a point in a circle.](09 - Groups_images/img-10.jpeg)
<!-- endcarousel -->

If $p$ is outside the circle, one can perform these steps backward: compute a tangent to $C$ through $p$ to get $q$, then $p'$ is the intersection of the altitude of the triangle $\Delta xqp$ with the ray $x \to p$. If $p$ lies on the circle, then $p$ is its own inverse.

To see why this has the property required by Definition 16.15, look again at Figure 16.7. Triangles $\Delta xp'q$ and $\Delta xqp$ are similar (a general truth about altitudes of right triangles), meaning $d(x,p')/r = r/d(x,p)$.

Another way to construct the inverse is to "just do it." You want a point along the ray from the center $x$ through $p$ compatible with its defining property. Simply compute

$$p^{\prime} = x + r^{2}(p - x)/\|p - x\|^{2}.$$

Working out the details,

$$
\begin{aligned}
d(p, x)\,d(p^{\prime}, x) &= \|p - x\|\,\|p^{\prime} - x\| \\
&= \|p - x\|\left\|\frac{r^{2}(p - x)}{\|p - x\|^{2}}\right\| \\
&= \|p - x\|^{2}\,r^{2}/\|p - x\|^{2} = r^{2}.
\end{aligned}
$$

This formula is the workhorse of the rest of the chapter, so it's worth confirming directly. Below we implement Definition 16.15's formula and check, on thousands of random configurations, that $d(p,x)\,d(p',x)=r^2$ exactly, and that inverting a point twice returns it (inversion is an involution). Later we'll reuse this same function to verify the cross ratio is invariant.

```python
<!-- include: code/pim/09 - Groups/08_poincare_inversion.py -->
```

We will also need the following.

**Proposition 16.16.** *Let $C$ and $D$ be circles. If $C$ and $D$ are orthogonal, then inversions in $C$ map $D$ to itself, and inversions in $D$ map $C$ to itself. Moreover, if $x, y$ are two points that are inverses with respect to $C$, and $D$ passes through both of them, then $C$ and $D$ are orthogonal.*

*Proof.* The proof is left as an exercise in geometry. As George Pólya said, geometry is the science of correct reasoning on incorrect figures. Take this to heart and make lots of bad drawings.

$\blacksquare$

![Figure 16.8: The construction of a Poincaré circle with center $p$ and radius $pq$.](09 - Groups_images/img-11.jpeg)

Next, we define a Poincaré line as the arc of a circle orthogonal to the boundary of the unit disk. We ignore some special cases made precise in code in Section 16.7. Given two points $p, q \in \mathbb{D}^2$, pick one that's not the center of $\mathbb{D}^2$ and invert it in the unit circle to get a third point $s$ outside the unit disk. By Proposition 16.16, the unique circle through these three points is orthogonal to the unit circle, as desired. The arc of that segment that is between $p$ and $q$ and lies inside the unit circle is defined to be the line segment between $p$ and $q$, as well as the shortest path between them. To extend this segment to a line, include the entire arc within the interior of $\mathbb{D}^2$.

Second, we define a Poincaré circle. We take a cue from Euclidean geometry, where a circle has the property that it is perpendicular to every line through its center, and use this property to guide the construction. Again we use the inversion: fix a line segment between $p$ and $q$, and say we want to draw the circle with center $p$. Pick any two hyperbolic lines $L_{1}, L_{2}$ that pass through $p$ but not $q$. Invert $q$ in both of these lines to get $q', q''$. Then the Euclidean circle passing through $q, q', q''$ is the hyperbolic circle centered at $p$ with radius $pq$. See Figure 16.8 for a diagram. Curiously, a hyperbolic circle in the Poincaré disk is a Euclidean circle, but its center is not the same point as the Euclidean center.

Finally, define the angle between hyperbolic lines as the usual Euclidean angle between their tangents at their point of intersection. Since hyperbolic lines are orthogonal to the unit circle, their centers necessarily lie outside of the Poincaré disk. Hence, if two lines intersect they intersect at a single point. Since the angles are defined in terms of Euclidean angles, all right angles are congruent.

Together, these facts establish the axioms of a geometry for the Poincaré disk.

## 16.6 The Symmetry Group of the Poincaré Disk

Taking a cue from Klein, let's study the symmetries of the Poincaré disk. We already have one symmetry: reflection across a hyperbolic line, which is inversion with respect to the circle defining that line. In the case of a hyperbolic line which is a diameter of $\mathbb{D}^{2}$, reflection is the same as Euclidean reflection in that line. By Proposition 16.16, these operations preserve the boundary of the Poincaré disk $\mathbb{D}^{2}$, and it's not hard to prove that the interior of $\mathbb{D}^{2}$ is also mapped to itself.

We want to study the invariant quantities with respect to hyperbolic reflection. One such quantity is angle measure, but a more interesting one is called the cross ratio. We'll use the cross ratio to define distance, so that reflections across hyperbolic lines will be isometries by definition. First we define the cross ratio in general, and in Definition 16.20 we'll make it specific to hyperbolic lines.

**Definition 16.17.** Let $w,x,y,z$ be four distinct points (in a specific order). The cross ratio of $w,x,y,z$, denoted $[wx;yz]$ is defined as

$$\frac{\|w-y\|}{\|w-z\|}\bigg/\frac{\|x-y\|}{\|x-z\|}=\frac{\|w-y\|\,\|x-z\|}{\|w-z\|\,\|x-y\|}.$$

The cross ratio holds the distinguished position of being the invariant quantity of projective geometry. Since all geometries are special cases of projective geometry, an appropriately contextualized version of the cross ratio should be invariant for hyperbolic geometry as well.

To show this, first we need a lemma.

**Lemma 16.18.** *Two hyperbolic reflections agreeing on two distinct pairs of inversion are equal. That is, the circle defining an inversion operation is uniquely determined by how that operation behaves on two points with distinct images.*

*Proof.* When reflecting across a diameter of $\mathbb{D}^{2}$, the lemma is true because reflection in a Euclidean line is uniquely determined by its behavior on two points (prove this as an exercise). The paragraphs to follow will heavily use Definition 16.15.

Let $x,y$ be points and $x^{\prime},y^{\prime}$ be their inversions, with respect to an unknown circle $C$ with center $z$ and radius $r$. The simple case is when $x,y,z$ are not on a common line. Then $z$ is the intersection of the line through $x,x^{\prime}$ and the line through $y,y^{\prime}$, and $r=\sqrt{\|z-x\|\,\|z-x^{\prime}\|}$ (Definition 16.15). This is depicted in Figure 16.9.

If $x,y,z$ lie on a common line, then we may assume without loss of generality that $x,y,z$ lie on the horizontal axis—otherwise we may make this true via a rotation about the origin of $\mathbb{D}^{2}$, and the uniqueness will still be determined. With this, we may set $x=(a,0),x^{\prime}=(a^{\prime},0),y=(b,0),y^{\prime}=(b^{\prime},0)$, and we need to find $z=(c,0)$ and $r>0$ such that $(a^{\prime}-c)(a-c)=r^{2}$ and $(b^{\prime}-c)(b-c)=r^{2}$ (i.e. Definition 16.15), where $c,r$ are variables. Subtracting the two equations gives $aa' - bb' + c(b + b' - a - a') = 0$, which can be solved for $c$ as long as $a \neq b$ and $a' \neq b'$. Note that if $b - a = a' - b'$, then the two points must be interchanged by the inversion, and hence they are not two distinct pairs of inversions.

$\square$

![Figure 16.9: The image of two points uniquely determines the circle of inversion (the easy case).](09 - Groups_images/img-12.jpeg)

Lemma 16.18 fails in the case that the two points are exchanged by the inversion. It simplifies the pair of equations used in the proof to $(a - c)(b - c) = r^2$. If you arbitrarily choose a position for $c$ to the right of both $a$ and $b$ or to the left of both $a$ and $b$, then you can always find a radius $r = \sqrt{(a - c)(b - c)}$ that works. Hence, an extra condition is required for uniqueness, and the condition relevant to the upcoming Lemma 16.21 is that the inverting circle is orthogonal to the unit disk.

Next, we show that the cross ratio is preserved by hyperbolic reflections. The proof is trivial for reflection in a diameter of the Poincaré disk, so we focus on the case of inversion in a circle.

**Theorem 16.19.** *Let $f(x)$ be inversion in a circle with center $c$ and radius $r$. Let $w, x, y, z \in \mathbb{R}^2$ be any four distinct points. Then $[wx; yz] = [f(w)f(x); f(y)f(z)]$.*

*Proof.* For ease of notation, let $w' = f(w)$ (similarly for $x, y, z$), and let $(ab)$ denote $\|a - b\|$, the length of the line segment between two vectors $a$ and $b$. We'll use $\cdot$ for multiplication to disambiguate. Then we must prove

$$\frac{(wy)\cdot(xz)}{(wz)\cdot(xy)} = \frac{(w^{\prime}y^{\prime})\cdot(x^{\prime}z^{\prime})}{(w^{\prime}z^{\prime})\cdot(x^{\prime}y^{\prime})}$$

It suffices to show that for any two of these points, say $w, y$, that $\frac{(wy)}{(w'y')} = \frac{(cw)}{(cy')}$. If we can show this, then (note the second equality is where we apply the claim, and the rest is grouping):

![Figure 16.10: The central claim is that $\frac{(wy)}{(w'y')} = \frac{(cw)}{(cy')}$.](09 - Groups_images/img-13.jpeg)

$$
\begin{aligned}
\frac{(wy)\cdot(xz)}{(wz)\cdot(xy)} \bigg/ \frac{(w^{\prime}y^{\prime})\cdot(x^{\prime}z^{\prime})}{(w^{\prime}z^{\prime})\cdot(x^{\prime}y^{\prime})}
&= \frac{(wy)\cdot(xz)\cdot(w^{\prime}z^{\prime})\cdot(x^{\prime}y^{\prime})}{(w^{\prime}y^{\prime})\cdot(x^{\prime}z^{\prime})\cdot(wz)\cdot(xy)} \\
&= \frac{(cw)\cdot(cx)\cdot(cw^{\prime})\cdot(cx^{\prime})}{(cy^{\prime})\cdot(cz^{\prime})\cdot(cz)\cdot(cy)} \\
&= \frac{(cw)\cdot(cw^{\prime})\cdot(cx)\cdot(cx^{\prime})}{(cy)\cdot(cy^{\prime})\cdot(cz)\cdot(cz^{\prime})} \\
&= \frac{r^{4}}{r^{4}} = 1,
\end{aligned}
$$

which proves the theorem.

To prove that $\frac{(wy)}{(w'y')} = \frac{(cw)}{(cy')}$, we split into two cases depending on whether $c, w, y$ are collinear. If they are not, then this follows from the similarity of the triangles $\Delta cwy \sim \Delta cy'w'$: they share the angle with $c$ and the defining property of circle inversion implies $\frac{(cw)}{(cy')} = \frac{(cy)}{(cw')}$. If they are collinear, consider the diagram in Figure 16.10. If $w, y$ are on different sides of $c$, then

$$
\frac{(wy)}{(cw)} = \frac{(cw) + (cy)}{(cw)} = 1 + \frac{(cy)}{(cw)} = 1 + \frac{r^{2}/(cy^{\prime})}{r^{2}/(cw^{\prime})} = 1 + \frac{(cw^{\prime})}{(cy^{\prime})} = \frac{(cy^{\prime}) + (cw^{\prime})}{(cy^{\prime})} = \frac{(w^{\prime}y^{\prime})}{(cy^{\prime})}
$$

Equating the left-most and right-most expressions, we rearrange to get $\frac{(wy)}{(w'y')} = \frac{(cw)}{(cy')}$, which was our goal. If $w$ and $y$ are on the same side of $c$, then replacing the sum $(wy) = (cy) + (cw)$ with $(wy) = (cy) - (cw)$, or $(cw) - (cy)$, as the case may be, yields the same result.

$\square$

Theorem 16.19 is precisely the invariance the demo above confirmed numerically: in `08_poincare_inversion.py` we sample four random points, invert all four in a random circle, and watch the cross ratio come out identical before and after. This is *why* inversion deserves to be called a hyperbolic isometry.

Though we leave out a coherent explanation of why this ultimately works as a distance function, the following construction provides the "correct" metric on the Poincaré disk.

**Definition 16.20.** Let $p, q \in \mathbb{D}^2$ be two distinct points. Form the hyperbolic line through those points, and let $x, y$ be the intersection of the hyperbolic line with the boundary of $\mathbb{D}^2$, so that $x$ is closest to $p$ and $y$ to $q$. Define the distance between $p$ and $q$ to be:

$$d(p, q) = \frac{1}{2}\left|\log[xy; qp]\right| = \frac{1}{2}\left|\log\frac{(x - q)(y - p)}{(x - p)(y - q)}\right|$$

where logs are taken with base $e$.

Admittedly vaguely, the choice of these two special points used to compute the cross ratio results in a "canonical" choice that allows different distances to be compared with respect to the same reference scale. As $p$ and $q$ near the boundary of the circle, the denominators involved in the cross ratio tend to zero and the cross ratio increases. See the exercises for more.

The hyperbolic distance function satisfies the properties of a metric from Definition 16.1 (proof omitted). If a metric is defined on a geometric space that has unique shortest line segments between points, then we get an additional property: $d(x,y)=d(x,z)+d(z,y)$ if and only if $z$ lies on the shortest path between $x$ and $y$. We will use this in the proof of Lemma 16.21.

Due to Theorem 16.19, we automatically know that hyperbolic distance is an invariant of a hyperbolic reflection. Moreover, a rotation $t_{\theta}$ of $\mathbb{D}^{2}$ by $\theta$ radians around the origin is also an isometry of the Poincaré disk: such rotations preserve the unit circle and are Euclidean isometries. These two facts together allow us to analyze the structure of all hyperbolic isometries.

First we prove an important lemma.

**Lemma 16.21.** *The set of points equidistant from two distinct points $x,y$ is a hyperbolic line, and a hyperbolic reflection in this line exchanges $x$ and $y$.*

*Proof.* First, we establish that for any two points $x,y$, there is a unique hyperbolic reflection $f:\mathbb{D}^{2}\to\mathbb{D}^{2}$ that exchanges $x$ and $y$. Then we prove that a point is fixed by $f$ if and only if it is equidistant to $x$ and $y$. Since we know that a point is fixed by a circle inversion if and only if it lies on that circle, this completes the proof.

The existence of $f$: if $x$ and $y$ both have the same Euclidean distance from the origin, then one can use the diameter of $\mathbb{D}^{2}$ that bisects the angle between $x$, $y$, and the center of $\mathbb{D}^{2}$. Otherwise, as per the postscript of Lemma 16.18 we follow the steps of Lemma 16.18 with the added condition that the inverting circle is orthogonal to the unit circle.

Rotate the center of the (unknown) circle of inversion so it, $x$, and $y$ all lie on the same horizontal line, which we may suppose without loss of generality is the horizontal axis. Let $x=(a,0),y=(b,0)$, and the center be $(c,0)$. The condition that $x,y$ are exchanged is $(a-c)(b-c)=r^{2}$. Via the Pythagorean theorem, being orthogonal to $\mathbb{D}^{2}$ adds the constraint $1+r^{2}=\|d-(c,0)\|^{2}$, where $d=(d_{1},d_{2})$ is a fixed vector. Combining these two equations and rearranging we get

$$ab-\|d\|^{2}+1+(-a-b+2d_{1})c=0$$

This has a unique solution for $c$ if and only if $d_1 \neq (a + b)/2$, i.e., if $d$ does not lie on the (Euclidean) perpendicular bisector of the line segment between $x, y$. This exceptional case is exactly when we use a reflection in a diameter of $\mathbb{D}^2$, i.e., the first case above.

![Figure 16.11: The line between $x$ and $f(z)$ is mapped to the line between $y$ and $z$ by reflection, and the intersection of these points is $w$.](09 - Groups_images/img-14.jpeg)

Next, we show a point $z$ is fixed by $f$ if and only if $z$ is equidistant to $x, y$. For the forward implication, suppose $f$ exchanges $x$ and $y$, and let $z = f(z)$. Then $d(x, z) = d(f(x), f(z)) = d(y, f(z)) = d(y, z)$. For the converse, let $z$ be a point with $d(x, z) = d(y, z)$, and suppose to the contrary that $z \neq f(z)$. Let $L$ be the hyperbolic line defined by $f$; by swapping $z$ and $f(z)$ we may assume $z$ is on the same side of $L$ as $x$. In this case note that $z, f(z)$ are exchanged by $f$, since $f$ is a reflection. This implies that any point $w$ fixed by $f$ is also equidistant to $z$ and $f(z)$. We have the picture in Figure 16.11.

Now $d(x,z) = d(y,z)$ by hypothesis, and chaining this with $d(y,z) = d(f(y),f(z)) = d(x,f(z))$ (since $f$ preserves distance and $f(y) = x$) we get $d(x,z) = d(x,f(z))$. Now consider the hyperbolic line segment between $x, f(z)$, which intersects $L$ (the hyperbolic line defining $f$) at a point $w$. This $w$ is on the shortest path between $x$ and $f(z)$, meaning $d(x,f(z)) = d(x,w) + d(w,f(z))$, and note that $w$ is fixed by $f$. Finally,

$$
\begin{aligned}
d(x, z) &= d(x, f(z)) \\
&= d(x, w) + d(w, f(z)) \\
&= d(x, w) + d(w, z)
\end{aligned}
$$

This implies $w$ is on the shortest path between $x$ and $z$. This contradicts the equality part of the triangle inequality: $x$ and $z$ are on the same side of $L$ while $w$ is on $L$.

$\square$

And now the finale: all isometries of the Poincaré disk are a composition of reflections. This proof relies on a fact whose proof I have omitted for brevity: isometries of the hyperbolic plane map lines to lines, just like in the Euclidean setting.

**Theorem 16.22.** *Every isometry of $\mathbb{D}^2$ is a product of at most 3 hyperbolic reflections.*

*Proof.* First, we claim that any isometry is determined by its effect on three non-collinear points $x,y,z$ (not on any Poincaré line). Suppose to the contrary there were two isometries $f,g$ with $f(x)=g(x),f(y)=g(y),f(z)=g(z)$, but for which some $p\not\in\{x,y,z\}$ satisfies $f(p)\neq g(p)$. Since $f$ and $g$ are isometries, each of the points $\{f(x),f(y),f(z)\}$ is equidistant to $f(p),g(p)$. By Lemma 16.21, $\{f(x),f(y),f(z)\}$ must lie on a hyperbolic line. But this contradicts the fact that isometries map lines to lines, since $\{x,y,z\}$ are not collinear.

To show three reflections are enough to express any isometry $f:\mathbb{D}^{2}\to\mathbb{D}^{2}$, choose any $x,y,z$ not on a line. In the special case that $x=f(x)$ and $y=f(y)$, then reflection in the hyperbolic line through $x,y$ must map $z$ to $f(z)$. Indeed, $z$ has the same distance to $x=f(x)$ and $y=f(y)$ as $f(z)$, so Lemma 16.21 applies. In this case $f$ is just a reflection.

In the slightly less special case that only one of the three points equals its image under $f$, say $x=f(x)$, then map $y$ to $f(y)$ via reflection in the unique hyperbolic line consisting of equidistant points to $y$ and $f(y)$ provided by Lemma 16.21. Again, since $y$ and $f(y)$ are equidistant from $x=f(x)$, the line being reflected must pass through $x$, meaning $x$ is fixed by this reflection. With one reflection we've reduced to the case $x=f(x),y=f(y)$; the first case adds one more reflection to get $f$.

Finally, in the least special case that all three points are different from their images, we can apply any reflection mapping $x\mapsto f(x)$, reducing to the second case. This results in a simple algorithm:

1. If $x\neq f(x)$, map $x$ to $f(x)$ via a reflection. Call this reflection $g_{1}$, or if $x=f(x)$ call $g_{1}$ the identity map.
2. If $g_{1}(y)\neq f(y)$, then map $g_{1}(y)$ to $f(y)$ using a second reflection. This is guaranteed to leave $g_{1}(x)$ fixed. Call that reflection $g_{2}$ (or the identity if $g_{1}(y)=f(y)$).
3. Do the same for $g_{2}(g_{1}(z))$ and $f(z)$, provided they are not equal, and call the resulting reflection $g_{3}$. This reflection fixes both $g_{2}(g_{1}(x))=g_{1}(x)$ and $g_{2}(g_{1}(y))$.

Compose the three reflections to get $f=g_{3}g_{2}g_{1}$.

$\blacksquare$

## 16.7 Application: Drawing Hyperbolic Tessellations

A tessellation is a tiling of space by a repeating pattern. Tessellations are ubiquitous in art, pervasive across cultures and throughout history. Islamic mosque decorations and Russian church tiles, Incan and Tahitian textiles, Native American baskets and Chinese porcelain. It seems that every major civilization incorporated tessellations in their art. Even today, we tessellate our footballs with black-and-white pentagons and our tweed coats with herringbone. Look around you—tessellations!

Tessellations and groups are natural bedfellows. A fixed isometry of the ambient space containing a starting pattern will move the pattern to one of its repetitions, and the (usually infinitely large) set of all such transformations forms a group. This group uniquely describes the geometry of the tessellation.

<!-- carousel -->
![Figure: Indian metalwork at the Great Exhibition in 1851. From Owen Jones's The Grammar of the Ornament (1856).](09 - Groups_images/img-15.jpeg)
![Figure: Fired Clay, Kerma, 1700–1550 BC. Harvard University–Boston Museum of Fine Arts.](09 - Groups_images/img-16.jpeg)
![Figure: Ceiling of an Egyptian tomb. From The Grammar of the Ornament.](09 - Groups_images/img-17.jpeg)
![Figure: Wall panelling, the Alhambra, Spain. From The Grammar of the Ornament.](09 - Groups_images/img-18.jpeg)
![Figure 16.16: Cloth, Hawaii. From The Grammar of the Ornament. A pattern which has two linearly independent directions of translational symmetry.](09 - Groups_images/img-19.jpeg)
<!-- endcarousel -->

The Euclidean plane provides a notable example before we return to hyperbolic geometry. Let's consider the set of all patterns that have discrete repetition in two linearly independent directions (as opposed to a pattern that only repeats when shifted, say, right), such as in Figure 16.16. The groups that describe such patterns—which include the tessellations used in many historical decorations—have a complete known classification. They are called wallpaper groups, and there are exactly 17 of them, up to isomorphism. Wikipedia contains a complete classification of the wallpaper groups, and examples of each occurring in actual decorations from cultures all around the world. One example is in Figure 16.17, the group called "p4." It's characterized by its core pattern providing two quarter-turn centers of rotation (the corner diamond and the center square), one 180-degree center of rotation (the thin diamonds bisecting each side), translation along two independent dimensions, and no other isometries.

Simpler than classifying all wallpaper patterns, we can ask what are the possible tessellations of the Euclidean plane by a convex polygon? For example, regular squares (each interior angle having the same measure, and each side being the same length) tile a plane via a group of translations isomorphic to $\mathbb{Z} \times \mathbb{Z}$, a fact familiar to anyone who has seen a chess or checkers board. And while regular pentagons don't tile the plane, irregular pentagons do, as depicted in Figure 16.18.

To reiterate, a tessellation transforms a single base shape via a fixed group of isometries. The shapes we're narrowing down to study are convex, possibly irregular polygons. Out of curiosity, if you try to tessellate the plane using an 8-sided convex polygon, you will struggle. Your struggle is true: it's impossible. The proof we'll see is quite interesting—it uses graph theory, aided by asymptotic notation, to double-count angles in a hypothetical tessellation. A veritable capstone for the techniques in this book!

<!-- carousel -->
![Figure 16.17: A figure which, when used to tile the plane, has p4 as its symmetry group. Figure by Martin von Gagern.](09 - Groups_images/img-20.jpeg)
![Figure 16.18: Irregular pentagonal tilings of the Euclidean plane. Figure by David Eppstein.](09 - Groups_images/img-21.jpeg)
<!-- endcarousel -->

**Theorem 16.23.** *There is no tessellation of the Euclidean plane by a single $n$-sided convex polygon for any $n > 6$.*

*Proof.* Suppose for contradiction that there is an $n$-sided convex polygon $P$, scaled to area 1, that tessellates the plane, and fix the set $T$ of all polygons in such a tessellation. Our proof will have two steps: first, we will fix a bounded piece of the tessellation of area $A$. Then we'll count the number of angles of polygons contained in that piece in two different ways, and arrive at an inequality of $A$ in terms of $A$. This inequality will be a contradiction for a sufficiently large $A$.

Fix a circle $C$ of area $A$, and let $S \subset T$ be the polygons in $T$ that contain at least one point within $C$. This finite set of polygons forms a graph $G = (V, E)$, where $V$ is the set of vertices of polygons in $S$, and $E$ is the (possibly subdivided[^subdiv]) set of polygon edges. Moreover, this graph is planar since the tessellation $S$ provides a literal drawing in the plane. Call $F$ the set of faces of $G$ (i.e., the polygons plus the outside face, as we did in Chapter 6). We summarize in Figure 16.19.

[^subdiv]: A vertex of one polygon may lie in the interior of an edge of an adjacent polygon, subdividing that edge into two.

First, split each of $V, E, F$ into "interior" and "exterior" subsets. The exterior subsets correspond to those vertices, edges, and faces that are adjacent to the outside of the graph. I.e., these came from the polygons that are only partially in the circle $C$. The interior vertices, edges, and faces are those that come from polygons entirely inside $C$. Subscript $V, E, F$ with "int" for interior and "ext" for exterior, like $V_{\mathrm{ext}}$.

![Figure 16.19: The setup for a hypothetical tiling of the Euclidean plane by a convex 7-gon. The bold circle has area $A$, and we include any polygon having at least one point inside the disk with boundary $C$.](09 - Groups_images/img-22.jpeg)

We will use the Euler characteristic formula from our chapter on graphs, Theorem 6.5, which says that for a planar graph $|V| - |E| + |F| = 2$. We first claim two facts which imply the formula $|V| = (n/2 - 1)A + O(A^{1/2})$, which is attained by substituting these two facts into Euler's formula and combining.

1. $|F| = |F_{\mathrm{int}}| + |F_{\mathrm{ext}}| = A + O(A^{1/2})$
2. $|E| = |E_{\mathrm{int}}| + |E_{\mathrm{ext}}| = nA/2 + O(A^{1/2})$

You will prove these facts in the exercises, but they can be thought of intuitively: the interior faces $F_{\mathrm{int}}$ (each of area 1) fill up a total area roughly equal to the area of the circle $C$, and the exterior faces are a thin band surrounding $C$, providing area proportional to the circumference of $C$ times some constant width. The big-O hides both the deviation of the area covered by $F_{\mathrm{int}}$ from being exactly $A$, and the entire area of $F_{\mathrm{ext}}$; both are $O(A^{1/2})$.

Now we will count the number of interior angles of polygons in $S$ in two different ways. What I mean by "interior angle" is an angle at a vertex inside a face. The first way is obvious, $n(|F| - 1) = n|S| \leq n|F|$, because each polygon has $n$ interior angles by definition (ignoring the exterior face). Second, we count by vertex, splitting into interior and exterior cases. Call $a_{v}$ the number of interior angles meeting at a vertex $v\in V$.

$$\#\text{ interior angles}=\sum_{v\in V_{\text{int}}}a_{v}+\sum_{v\in V_{\text{ext}}}a_{v}.$$

For $V_{\text{int}}$, there must be at least three interior angles at each vertex (one of these angles may be part of an edge of some polygon, thus having measure $\pi$). This bounds the first sum from below by $3|V_{\text{int}}|$. The second sum is $O(A^{1/2})$ because every exterior vertex touches an exterior edge, and fact (2) above shows the number of exterior edges is $O(A^{1/2})$. This gives $\#\text{ interior angles} \geq 3|V_{\text{int}}|+O(A^{1/2})$. Since $|V_{\text{int}}|=|V|-|V_{\text{ext}}|$, we have $|V_{\text{int}}|=(n/2-1)A+O(A^{1/2})$ as well.

Combining these formulas and bounds gives

$$n|F|\geq(\#\text{ interior angles})\geq 3|V_{\text{int}}|+O(A^{1/2})$$

Expanding $|F|$ and $|V_{\text{int}}|$,

$$
\begin{aligned}
nA+nO(A^{1/2}) &\geq 3(n/2-1)A+O(A^{1/2}) \\
nA &\geq 3(n/2-1)A+O(A^{1/2})
\end{aligned}
$$

because as $A\to\infty,\;nO(A^{1/2})=O(A^{1/2})$.

The right hand side is approximately $\frac{3}{2}nA$, and the left hand side is $nA$, hinting at the contradiction. More precisely, this inequality fails as $A\to\infty$ if and only if $1>\frac{n}{3(n/2-1)}$, which happens if and only if $n>6$.

$\blacksquare$

While this may disappoint hopeful weavers of the next great tapestry, one can tessellate the hyperbolic plane with a 7-gon. Not only that, but there are infinitely many ways to do it! Figure 16.20 shows two ways produced by the program in this section.

<!-- carousel -->
![Figure 16.20: Left: a tiling of the hyperbolic plane by 7-gons with 3 meeting per vertex.](09 - Groups_images/img-23.jpeg)
![Figure 16.20: Right: a tiling of the hyperbolic plane by 7-gons with 4 meeting per vertex.](09 - Groups_images/img-24.jpeg)
<!-- endcarousel -->

In the figure, a regular 7-gon tessellates the Poincaré disk, with 3 polygons meeting at each vertex. The two parameters implied by $(7,3)$ provide an infinite family of tessellations by regular, convex $p$-gons. Given a convex, regular, hyperbolic $p$-gon, let $[p,q]$ denote the configuration of a tessellation by that polygon in which $q$ copies of the polygon meet at each vertex. The example above has configuration $[7,3]$. This configuration is sometimes called the Schläfli symbol.

**Theorem 16.24.** *Let $p, q$ be integers. A regular, convex, hyperbolic $p$-gon tessellates the plane with $q$ copies of the polygon meeting at each vertex if and only if $(p - 2)(q - 2) > 4$.*

The artist M.C. Escher used a $[6, 4]$ tessellation to construct his *Circle Limit IV*, displayed in Figure 16.21 with additional lines showing the hyperbolic lines used in its design. The remainder of this chapter is devoted to drawing the outlines of hyperbolic tessellations. In an exercise you'll extend the program to input a pattern (like the angel/devil motif in Figure 16.21) and output an Escher-style drawing.

The core of these kinds of hyperbolic tessellations is the fundamental region, which is the smallest subset of the tessellation which, when all symmetries in the tessellation group are applied, tile the plane. In the case of Escher's angels, the fundamental region is the region shown in Figure 16.22. Since we're just drawing the outline of a tessellation, we only need a single triangle.

**Definition 16.25.** The fundamental triangle for a $[p,q]$ tessellation of the hyperbolic plane is a hyperbolic triangle with angle measures $\frac{\pi}{p},\frac{\pi}{q},\frac{\pi}{2}$.

If such a triangle has its $\pi/p$ vertex centered at the origin, then Figure 16.23 shows why it produces a hyperbolic $p$-gon that tessellates the plane. In Figure 16.23, the fundamental triangle is the thick solid shape, and it's been repeatedly reflected along the edges incident to the origin. Recall from Theorem 16.22 that all isometries are products of reflections, and here we're expressing rotations of $2\pi/p$ by two reflections. The result is that the triangle and its mirror are rotated to produce a hyperbolic $p$-gon centered at the origin. Likewise, the vertex with an angle of $\pi/q$ allows one to rotate around an exterior vertex by an angle of $2\pi/q$, forming a piece of each of the $q$ distinct polygons at each vertex.

<!-- carousel -->
![Figure 16.21: Left: Circle Limit IV, M.C. Escher, 1960.](09 - Groups_images/img-25.jpeg)
![Figure 16.21: Right: annotated showing the center 6-gon that is tessellated.](09 - Groups_images/img-26.jpeg)
![Figure 16.22: The fundamental region of Circle Limit IV. The region tiles the plane by rotations and reflections.](09 - Groups_images/img-27.jpeg)
![Figure 16.23: The fundamental triangle (thick, solid), reflected across its top edge (faint, thick, dotted), rotated around the center vertex to form the center polygon (thin dashed), and rotated around the $\pi/q$ vertex to form pieces of tessellated polygons (thick dotted).](09 - Groups_images/img-28.jpeg)
<!-- endcarousel -->

Thus, if we can draw a fundamental triangle and reflect a set of points across a hyperbolic line, we'll be able to draw regular convex tessellations.

### Computing Orthogonal Circles and Reflections

Recall that a hyperbolic line between two points in the Poincaré disk is represented by the circle passing through those two points orthogonal to the unit circle (or a diameter). Moreover, reflection in that line is inversion in the circle (or reflection across the diameter).

To compute these quantities, we start by defining geometric classes for a (Euclidean) point, circle, and line. These classes are largely not interesting. Their method signatures are outlined in Figure 16.24. In these classes all equality comparisons are "closeness" comparisons, up to some arbitrary but fixed tolerance $\varepsilon\approx 10^{-8}$. The reflection across a Euclidean line is also relevant because some hyperbolic lines—those that are diameters of the Poincaré disk—are also Euclidean lines. The `Circle` class has an extra key method computing the inversion of a point via the formula from Section 16.5.

```python
def invert_point(self, point):
    """Compute the inverse of a point with respect to self."""
    x, y = point
    center, radius = (self.center, self.radius)
    square_norm = (x - center.x) ** 2 + (y - center.y) ** 2
    x_inverted = center.x + radius ** 2 * (x - center.x) / square_norm
    y_inverted = center.y + radius ** 2 * (y - center.y) / square_norm
    return Point(x_inverted, y_inverted)
```

With these basic objects and operations, we can compute the hyperbolic line passing through two points. The inputs are two points which the hyperbolic line must pass through, along with a circle it must be orthogonal to. The orthogonal circle argument happens to be the boundary of $\mathbb{D}^{2}$, but the implementation does not depend on this.

There is one simple case to start: when both points are already on the orthogonal circle. In this case, the hyperbolic line is the Euclidean circle whose center is the intersection of the two tangent lines at the points, depicted in Figure 16.25. This results in the following edge case in code.

```python
def intersection_of_common_tangents(circle, point1, point2):
    line1 = circle.tangent_at(point1)
    line2 = circle.tangent_at(point2)
    return line1.intersect_with(line2)


def circle_through_points_perpendicular_to_circle(point1, point2, circle):
    """Return a Circle that passes through the two given points and
    intersects the given circle at a perpendicular angle.
    """
    if circle.contains(point1) and circle.contains(point2):
        circle_center = intersection_of_common_tangents(
            circle, point1, point2)
        radius = distance(circle_center, point1)
        return Circle(circle_center, radius)
```

If at least one point is not on the circle, then the output is computed as follows. Invert the non-circle point in the circle (Proposition 16.16 guarantees orthogonality), and the result is a set of three points, which uniquely determine the equation of a circle.

<!-- carousel -->
![Figure 16.24: The function signatures of the geometry helper classes.](09 - Groups_images/img-29.jpeg)
<!-- endcarousel -->

The equation for the center of the circle passing through three given points can be computed by setting up three equations and solving. The equations being solved are built by substituting our known points into the equation of a circle. Here the unknowns are $c_{x}$, $c_{y}$, and $r$.

$$
\begin{aligned}
(x_{1}-c_{x})^{2}+(y_{1}-c_{y})^{2}&=r^{2}\\
(x_{2}-c_{x})^{2}+(y_{2}-c_{y})^{2}&=r^{2}\\
(x_{3}-c_{x})^{2}+(y_{3}-c_{y})^{2}&=r^{2}
\end{aligned}
$$

A succinct way to express the solution to these equations is in terms of the ratios of determinants of a cleverly chosen matrix. We haven't talked about the determinant in this book, but in addition to being a deeply meaningful quantity in its own right, it shows up frequently in computational geometry. More about the determinant in the Chapter Notes. In this case, the solution is summarized by ratios of determinants of sub-matrices of the following matrix:

$$ \begin{pmatrix}x^{2}+y^{2}&x&y&1\\ x_{1}^{2}+y_{1}^{2}&x_{1}&y_{1}&1\\ x_{2}^{2}+y_{2}^{2}&x_{2}&y_{2}&1\\ x_{3}^{2}+y_{3}^{2}&x_{3}&y_{3}&1\end{pmatrix} $$

Computing a determinant reduces to repeatedly removing a (row, column) pair and computing the determinant of the smaller matrix, called a minor. Once the recursion reduces to determinants of 3-dimensional matrices, we can easily hard-code a formula. You'll read about the correctness of this function in an Exercise.

```python
def circle_through_points_perpendicular_to_circle(point1, point2, circle):
    # [...edge case...]
    point3 = (circle.invert_point(point2)
              if circle.contains(point1)
              else circle.invert_point(point1))

    def row(point):
        (x, y) = point
        return [x ** 2 + y ** 2, x, y, 1]

    M = [row(point1), row(point2), row(point3)]

    # detminor stands for "determinant of (matrix) minor"
    detminor_1_1 = det3(remove_column(M, 0))
    detminor_1_2 = det3(remove_column(M, 1))
    detminor_1_3 = det3(remove_column(M, 2))
    detminor_1_4 = det3(remove_column(M, 3))

    circle_center_x = 0.5 * detminor_1_2 / detminor_1_1
    circle_center_y = -0.5 * detminor_1_3 / detminor_1_1
    circle_radius = math.sqrt(
        circle_center_x ** 2 + circle_center_y ** 2
        + detminor_1_4 / detminor_1_1)
    return Circle(
        Point(circle_center_x, circle_center_y), circle_radius)
```

This allows us to define relevant abstractions for a hyperbolic line and the hyperbolic plane. An instance of the Poincaré disk is a circle, with methods to compute a line through two given points. A hyperbolic line is a circle, which happens to be orthogonal to the unit circle forming the boundary of the Poincaré disk.

```python
class PoincareDiskModel(Circle):
    def line_through(self, p1, p2):
        """Return a PoincareDiskLine through the two given points."""
        if orientation(p1, p2, self.center) == 'collinear':
            return Line.through(p1, p2)
        else:
            circle = circle_through_points_perpendicular_to_circle(
                p1, p2, self)
            return PoincareDiskLine(circle.center, circle.radius)


class PoincareDiskLine(Circle):
    def reflect(self, point):
        """Reflect a point across this line."""
        return self.invert_point(point)
```

To determine if three points are collinear, we again employ the determinant. More generally, if you provide three points $A=(a_{x},a_{y}),B=(b_{x},b_{y}),C=(c_{x},c_{y})$ in sequence, one can determine via the sign of a determinant whether visiting the points in order results in a clockwise turn, a counterclockwise turn, or a straight line. The relevant matrix is

$$ \begin{pmatrix}1&a_{x}&a_{y}\\ 1&b_{x}&b_{y}\\ 1&c_{x}&c_{y}\end{pmatrix} $$

The determinant, which can be thought of as computing a signed area of a particular triangle built from the rows of the matrix, will produce zero if the points all lie on a common line. For a $3\times 3$ matrix the determinant formula is simple enough to inline.

```python
def orientation(a, b, c):
    """Compute the orientation of three points visited in sequence."""
    a_x, a_y = a
    b_x, b_y = b
    c_x, c_y = c
    value = (b_x - a_x) * (c_y - a_y) - (c_x - a_x) * (b_y - a_y)

    if value > EPSILON:
        return 'counterclockwise'
    elif value < -EPSILON:
        return 'clockwise'
    else:
        return 'collinear'
```

### Computing a Fundamental Triangle

Next we compute the vertices of a fundamental triangle. Recall a fundamental triangle has vertices $A,B,D$ with interior angles $\pi/p$, $\pi/q$, and $\pi/2$, respectively. Also recall that the angle measure between two hyperbolic lines is defined to be the angle between their tangent lines at the point of intersection. To simplify the description of our fundamental triangle, we require that $A$ is the origin and $D$ lies on the horizontal axis. Thus, computing our desired triangle can be summarized by identifying the coordinates of $B$ and $D$ in Figure 16.26.

The requirement of the three angle measures, paired with the side $AD$ lying on the horizontal axis, uniquely determines the positions of $B$ and $D$. Let's derive this now.

**Lemma 16.26.** *Define the constant $Z=\tan\left(\frac{\pi}{p}+\frac{\pi}{q}\right)\tan\left(\frac{\pi}{p}\right)$. The coordinates of the point $B=(b_{x},b_{y})$ are given by*

$$
\begin{aligned}
b_{x} &=\sqrt{\frac{1}{1+2Z-\left(\tan(\pi/p)\right)^{2}}}\\
b_{y} &=b_{x}\tan(\pi/p),
\end{aligned}
$$

*and the $x$-coordinate of $D=(d_{x},0)$ is given by*

$$
\begin{aligned}
r^{2} &=b_{y}^{2}+(b_{x}-g_{x})^{2}\\
d_{x} &=g_{x}-r,
\end{aligned}
$$

*where $G=(g_{x},0)=(b_{x}(Z+1),0)$ is the $x$-coordinate of the center of the circle defining the hyperbolic line passing through $B$ and $D$.*

*Proof.* The point $B=(b_{x},b_{y})$ is defined to be on the line which makes an angle of $\pi/p$ with the horizontal, i.e., $y=\tan(\pi/p)x$. Since $A$ is the origin, hyperbolic lines through $A$ are the same as Euclidean lines. This gives the formula for $b_{y}$. $B$ also lies on a circle orthogonal to the unit circle that passes through $D$. Call this unknown circle $C$, and suppose it has center $G=(g_{x},0)$. Note that the $y$-coordinate of $G$ must be zero in order for $C$ to make a right angle with $D=(d_{x},0)$. Refer to Figure 16.26.

We're asking for an angle of $\pi/q$ between the line $y=\tan(\pi/p)x$ and the tangent to this unknown circle $C$ at $B$. Stare at the diagram in Figure 16.27 to convince yourself that the desired tangent line must have an angle of $\frac{\pi}{p}+\frac{\pi}{q}$ with the horizontal, implying the slope of this tangent line is $\tan(\frac{\pi}{p}+\frac{\pi}{q})$.

The equation of the unknown circle (in terms of our unknown quantities) is $(x-g_{x})^{2}+y^{2}=r^{2}$, where $r^{2}=\left(b_{x}-g_{x}\right)^{2}+b_{y}^{2}$. When $y>0$, the derivative of the circle is given by $C^{\prime}(b_{x},b_{y})=-(b_{x}-g_{x})/b_{y}$, and setting $C^{\prime}=\tan(\frac{\pi}{p}+\frac{\pi}{q})$, we solve for $g_{x}$ in terms of $b_{x}$ as

$$b_{x}(Z+1)=g_{x},\qquad\text{where }Z=\tan\left(\frac{\pi}{p}+\frac{\pi}{q}\right)\tan\left(\frac{\pi}{p}\right)$$

<!-- carousel -->
![Figure 16.26: The unknown points computed in Lemma 16.26 are $B, D$, and $G$, which is the center of the orthogonal circle $C$ passing through $B, D$, that makes the desired angle of $\pi/q$ with the top edge of the fundamental triangle.](09 - Groups_images/img-30.jpeg)
![Figure 16.27: By symmetry, the angle of the tangent line to $C$ at $B$ with the horizontal is $\pi/p + \pi/q$.](09 - Groups_images/img-31.jpeg)
<!-- endcarousel -->

If we can get another independent equation relating $b_{x}$ and $g_{x}$, we can eliminate one variable and solve the entire system. The fact we have yet to use is that $C$ and the unit circle are orthogonal. This gives a relationship between their radii, which form the legs of a right triangle: $1^{2}+r^{2}=g_{x}^{2}$, where $r^{2}=(b_{x}-g_{x})^{2}+\tan(\pi/p)^{2}b_{x}^{2}$. Solving this equation for $b_{x}$ gives the formula stated in the theorem, and substitution provides the rest.

$\blacksquare$

This results in the following code, whose documentation is far more tedious than its implementation:

```python
def compute_fundamental_triangle(tessellation_configuration):
    p = tessellation_configuration.num_polygon_sides
    q = tessellation_configuration.num_polygons_per_vertex
    tan_p = math.tan(math.pi / p)
    Z = math.tan(math.pi / p + math.pi / q) * tan_p

    b_x = math.sqrt(1 / (1 + 2 * Z - tan_p ** 2))
    b_y = b_x * tan_p
    g_x = b_x * (Z + 1)
    d_x = g_x - math.sqrt(b_y ** 2 + (b_x - g_x) ** 2)

    A = Point(0, 0)
    B = Point(b_x, b_y)
    D = Point(d_x, 0)
    return [A, B, D]
```

Before we trust these formulas to drive the whole drawing, we should *check* them. The demo below runs Kun's `compute_fundamental_triangle` for several hyperbolic configurations and verifies the geometry that Lemma 16.26 promises: the circle through $B$ and $D$ really is orthogonal to the unit disk (so $g_x^2 = 1 + r^2$), and the three interior angles—measured between the appropriate tangent lines—come out to exactly $\pi/p$, $\pi/q$, and $\pi/2$.

```python
<!-- include: code/pim/09 - Groups/09_fundamental_triangle.py -->
```

### Tessellating the Fundamental Triangle

Finally, we have all the pieces we need to draw a tessellation. The majority of the code is helpers. We output the drawing as an SVG file, and so in addition to using a library to draw SVGs, we need to keep track of the differences in coordinate systems. Beyond that, the core routine is quite simple.

First we define a configuration class for a tessellation (used above to draw the fundamental triangle). Followed by a class representing a tessellation. In the latter, the `compute_center_polygon` method computes the center polygon by computing the fundamental triangle, and then iteratively reflecting it across the appropriate edges.

Finally, the `tessellate` method builds the tessellation using a breadth-first traversal of the underlying graph. We use the standard Python `deque` class that can behave as both a stack and a queue to achieve the traversal. Start with a queue containing only the center polygon, and an empty list of "visited" polygons. As long as the queue is nonempty, pop off a polygon, add it to the visited set, reflect it across all possible edges, and add to the queue any unvisited polygons produced this way. Also skip any polygons that are smaller than some limit (i.e., skip them if they're too small to see when rendered on the screen).

The remainder of the code[^remainder] involves rendering the edges of the polygons as SVG arcs. We also created a simple data structure that allows one to compare polygons for equality in a principled way (since the process of reflecting them changes the order of their vertices).

[^remainder]: The full program, including SVG rendering, is available in the book's source repository.

```python
class TessellationConfiguration(
        namedtuple('TessellationConfiguration',
                   ['num_polygon_sides',
                    'num_polygons_per_vertex'])):
    def __init__(self, num_polygon_sides, num_polygons_per_vertex):
        if not self.is_hyperbolic():
            raise Exception(
                "Configuration {}, {} is not hyperbolic.".format(
                    self.num_polygon_sides,
                    self.num_polygons_per_vertex))

    def is_hyperbolic(self):
        return (self.num_polygon_sides - 2) * (
            self.num_polygons_per_vertex - 2) > 4
```

```python
class HyperbolicTessellation(object):
    def __init__(self, configuration):
        self.configuration = configuration
        self.disk_model = PoincareDiskModel(Point(0, 0), radius=1)

        # compute the vertices of the center polygon via reflection
        self.center_polygon = self.compute_center_polygon()
        self.tessellated_polygons = self.tessellate()
```

```python
def compute_center_polygon(self):
    center, top_vertex, x_axis_vertex = compute_fundamental_triangle(
        self.configuration)
    p = self.configuration.num_polygon_sides

    # The center polygon's first vertex is the top vertex (the one
    # that makes an angle of pi / q), because the x_axis_vertex is
    # the center of an edge.
    polygon = [top_vertex]

    p1, p2 = top_vertex, x_axis_vertex
    for i in range(p - 1):
        p2 = self.disk_model.line_through(center, p1).reflect(p2)
        p1 = self.disk_model.line_through(center, p2).reflect(p1)
        polygon.append(p1)

    return polygon
```

```python
def tessellate(self, max_polygon_count=500):
    """Return the set of polygons that make up a tessellation of
    the center polygon. Keep reflecting polygons until drawing a
    total of max_polygon_count."""
    queue = deque()
    queue.append(self.center_polygon)
    tessellated_polygons = []
    processed = PolygonSet()
    while queue:
        polygon = queue.popleft()
        if processed.contains_polygon(polygon):
            continue
        edges = [(polygon[i], polygon[(i + 1) % len(polygon)])
                 for i in range(len(polygon))]
        for u, v in edges:
            line = self.disk_model.line_through(u, v)
            reflected_polygon = [line.reflect(p) for p in polygon]
            queue.append(reflected_polygon)
        tessellated_polygons.append(polygon)
        processed.add_polygon(polygon)
        if len(processed) > max_polygon_count:
            break
    return tessellated_polygons
```

We close with some outputs for different configurations, shown in Figure 16.32.

<!-- carousel -->
![Figure 16.32: A [3, 7] tessellation. Example output from the tessellation program.](09 - Groups_images/img-32.jpeg)
![Figure 16.32: A [5, 5] tessellation.](09 - Groups_images/img-33.jpeg)
![Figure 16.32: A [6, 6] tessellation.](09 - Groups_images/img-34.jpeg)
![Figure 16.32: A [7, 7] tessellation.](09 - Groups_images/img-35.jpeg)
<!-- endcarousel -->

## 16.8 Cultural Review

1. Groups are the primary tool mathematics has for studying symmetry, and symmetry shows up all over mathematics and science.
2. Any class of structured objects can be studied in terms of structure-preserving mappings between those objects.
3. Geometry is the study of groups of symmetry, and the invariants preserved by those symmetries.

## 16.9 Exercises

**16.1.** Recall the symmetric group $S_{n}$ is the set of all bijections of a set of $n$ elements. Call the set being permuted $\{1,2,3,\ldots,n\}$, and consider the following helpful notation for a permutation: define a cycle notation whereby the tuple $(1\ 3\ 4\ 2)$ represents the permutation $\sigma$ mapping $1\mapsto 3$, $3\mapsto 4$, $4\mapsto 2$, and $2\mapsto 1$. All other values are fixed by $\sigma$. Define a product of cycles, such as (going right to left) $(2\ 4)(1\ 2)=(1\ 4\ 2)$ as the composition of the corresponding maps. A cycle of length $2$ is called a transposition. Prove that every permutation can be written as a product of disjoint cycles. Prove that the $n$-cycle $(1\ 2\ 3\ \cdots\ n)$ and a single transposition $(1\ 2)$ are a generating set for $S_{n}$.

**16.2.** Using the previous exercise, define a permutation $x\in S_{n}$ to be *even* if it is a product of an even number of transpositions. Otherwise call it *odd*. Show that this definition is well defined: every permutation is either even or odd, but not both. Show a product of two even permutations is even, a product of two odd permutations is even, and a product of an even and an odd permutation is odd.

**16.3.** Let $G$ be a group and $H$ a subgroup. A *coset* of $H$ by a fixed element $x\in G$ is the set $\{xh\mid h\in H\}$. This set is denoted $xH$. Prove the following:

1. $aH=bH$ if and only if $b^{-1}a\in H$.
2. Let $f:G\to H$ be a group homomorphism. Recall the equivalence relation $\sim_{f}$ defined in Chapter 9 by $a\sim_{f}b$ iff $f(a)=f(b)$. Show the equivalence classes are the cosets of $\ker f$.
3. Let $G$ be a group. Given a subgroup $H\subset G$, show that the set of all cosets of $H$ partition $G$ into disjoint subsets. Conclude that "being in the same coset of $H$" is an equivalence relation on $G$, and define $G/H$ to be the quotient of $G$ by this equivalence relation.
4. Prove that the group operation $[x]\cdot[y]=[xy]$ is well-defined in the quotient group $G/H$ if and only if $H$ has the property that for every $b\in H$ and every $a\in G$, the element $aba^{-1}\in H$. Prove that the kernel of a homomorphism has this property. Such subgroups are called *normal* subgroups.
5. Prove that every normal subgroup $H$ of a group $G$ is the kernel of some homomorphism from $G$ to some group. Thus, our definition of a quotient using a kernel is identical to this definition.

**16.4.** Prove that the property of being isomorphic is an equivalence relation on groups. In particular, show that the inverse of an isomorphism is a homomorphism.

**16.5.** Find a generator of the multiplicative integer group $\left(\mathbb{Z}/82\mathbb{Z}\right)^{\times}$.

**16.6.** Prove that $x\in\mathbb{Z}/n\mathbb{Z}$ has a multiplicative inverse if and only if $\gcd(x,n)=1$.

**16.7.** Let $G$ be a finite group and $H$ a subgroup. Prove $|H|$ evenly divides $|G|$. Use this to prove that for any $a\in G$, $a^{|G|}$ is the identity.

**16.8.** Define by $\varphi(n)$ the size of the set $\{k\in\mathbb{N}:k<n,\gcd(n,k)=1\}$. This function is called the *Euler totient function*. Prove that for any integer $a$, $a^{\varphi(n)}\equiv 1\bmod n$. Hint: use the previous exercise.

**16.9.** Prove Theorem 16.12, assembling the pieces laid out in the chapter.

**16.10.** Let $n\in\mathbb{N}$, and let $G=\left(\mathbb{Z}/n\mathbb{Z}\right)^{\times}$ be the multiplicative group of integers (those integers between $1$ and $n$ that have a greatest common divisor of $1$ with $n$). When $n$ is a product of two large primes, this group is called the RSA group. Research the RSA public-key cryptography protocol, and write a program that implements it for two hundred-digit primes. Hint: you will need to find a fast way to generate hundred-digit primes.

**16.11.** Research and implement the ElGamal digital signature scheme using $\left(\mathbb{Z}/n\mathbb{Z}\right)^{\times}$.

**16.12.** Look up the definition of a semi-direct product of groups, and use this to understand the characterization of the dihedral group $D_{2n}$ as a semi-direct product of $\mathbb{Z}/2\mathbb{Z}$ with $\mathbb{Z}/n\mathbb{Z}$, where the former acts on the latter by "conjugation."

**16.13.** If you're comfortable with complex numbers, find a source online that discusses the symmetry groups of the roots of polynomials with coefficients in $\mathbb{Q}$. At the risk of referring to an interactive essay that has disappeared from the internet after this book is published, see Fred Akalin's essay, "Why is the Quintic Unsolvable?"

**16.14.** Recall an undirected graph $G=(V,E)$ is a set of vertices $V$ and a set of edges $E\subset\binom{V}{2}$ that link pairs of vertices. A symmetry of $G$ is a bijection $f:V\rightarrow V$ such that $(v,w)$ is an edge if and only if $(f(v),f(w))$ is an edge. In words, a symmetry permutes the vertices of $G$ in such a way that preserves adjacency and non-adjacency. Compute the symmetry group of the Petersen graph. Hint: the size of this group is $120$, so brute-force will be difficult.

**16.15.** Two graphs are called isomorphic if there is a bijection between their vertex sets having the same property as a symmetry: all adjacencies and non-adjacencies are preserved. The problem of efficiently computing whether two graphs are isomorphic is one of the most famous open problems in computer science, called the graph isomorphism problem. Prove that the graph isomorphism problem reduces to the problem of computing a generating set of the symmetry group of a single graph.

**16.16.** Prove that any Euclidean isometry in $E(n)$ can be written as the product of at most $n+1$ reflections.

**16.17.** Read about determinants and understand why the formula we presented in Section 16.7 for the circle passing through three given points is correct.

**16.18.** Research the cross ratio in the context of projective geometry. How is it defined there? What are the projective transformations, and why do they preserve the cross ratio?

**16.19.** Prove the two facts from Theorem 16.23:

1. $|F|=|F_{\text{int}}|+|F_{\text{ext}}|=A+O(A^{1/2})$
2. $|E|=|E_{\text{int}}|+|E_{\text{ext}}|=nA/2+O(A^{1/2})$

For the first, consider a well-chosen larger circle containing $C$, and look at the difference of areas. For the second, borrow ideas from Chapter 4 and count the number of edges in terms of the number of faces, then substitute the first formula.

**16.20.** Prove Proposition 16.16.

**16.21.** We neglected to give a good intuition for why the hyperbolic distance function is intuitively a good choice. The reason is that the morally acceptable way to think about this function involves integral calculus, which we avoided in this book. To do this formally, one defines a metric tensor or line element that describes the length of a curve via an integral. Research these topics to understand how the hyperbolic metric is defined. Be warned that many sources jump straight into advanced terminology and concepts. You're looking for an "introduction to tensor calculus" or an "introduction to Riemannian geometry." Because of the close relation to physics and general relativity, there are also many sources explaining these concepts for physicists. Apply the usual caveats that come with physicists explaining mathematics.

**16.22.** Extend the hyperbolic tessellation program in this chapter to one which, when given an input motif (an image that replaces the fundamental triangle) draws a hyperbolic polygon using that image and then tessellates the Poincaré disk.

**16.23.** A different model of hyperbolic geometry is the upper half-plane model. This model has as points the complex numbers $\{a+bi:b>0\}$, and as lines the half circles orthogonal to the horizontal axis $b=0$, along with vertical rays. The line $b=0$ forms the "boundary" analogous to the unit circle bounding the Poincaré disk. The isometries of this model are the so-called Möbius transformations. For these exercises it may help to read the section in the chapter notes about the complex matrix representation of hyperbolic isometries. Prove the following.

1. The set of Möbius transformations, those mappings of the complex line defined by $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc\neq 0$, form a group under function composition. This group is called the Möbius group.
2. Find a formula for inversion in a circle (reflection in an upper-half-plane-model line) as a Möbius transformation.
3. The Möbius group is isomorphic to the group of matrices $PGL_{2}(\mathbb{R})=GL_{2}(\mathbb{R})/\sim$, where $\sim$ is the equivalence relation defined by $A\sim\lambda A$ for every nonzero $\lambda\in\mathbb{R}$. Why is this quotient necessary?
4. All Möbius transformations preserve the cross ratio.
5. Find a bijection between the upper half plane and the Poincaré disk that preserves hyperbolic lines.

**16.24.** Yet another model of hyperbolic geometry is the Minkowski hyperboloid model. This model has as points the vectors $\{(x,y,z):x>0\text{ and }x^{2}-y^{2}-z^{2}=1\}$. These points lie on a hyperboloid. Find the resource that explains the following for this model:

1. Defines hyperbolic lines.
2. Defines hyperbolic distance.
3. How hyperbolic lines in the Minkowski model correspond to lines in the Poincaré disk model.
4. Using the above, write a program that draws a hyperbolic tessellation in the Minkowski model, and then projects it to the Poincaré disk. What are the advantages and disadvantages to doing it this way, instead of directly in the Poincaré model?

**16.25.** In this exercise we'll explore the symmetry group of the hyperbolic tessellation of a regular convex $p$-gon with configuration $[p,q]$. Fix the fundamental triangle of the configuration, and consider the reflections $\alpha,\beta,\gamma$ across each edge. What are the algebraic relations between these symmetries? Can you identify the resulting (infinite) group of symmetries with a subgroup of a familiar group?

## 16.10 Chapter Notes

### History of the Hyperbolic Plane

Like many topics in mathematics, the discovery of the hyperbolic plane was far more roundabout than its final form. The first hyperbolic geometry was discovered on the surface of revolution of the so-called tractrix, which is itself derived indirectly from the catenary curve—the name for the not-quite-parabolic shape formed by an ideal rope hanging from its ends under its own weight.

John Stillwell's *Geometry of Surfaces* has a complete derivation of the hyperbolic plane in terms of the tractrix (Chapter 4). It also contains sections devoted to each model of the hyperbolic plane, including a few that are deemed relatively useless from a computational perspective.

### More About the Determinant

The determinant of a linear map is defined as the product of its eigenvalues (including multiplicity for repeated eigenvalues). If any of those eigenvalues are zero, the linear map is not invertible, and as a consequence a common substitute for "invertible matrix" is "matrix with nonzero determinant."

However, the determinant has another definition—one that is somewhat mysterious and irrelevant for our purposes—in terms of symmetry groups. Specifically, let $S_{n}$ be the permutation group on the set of rows of a matrix $A$. See Exercise 16.1 and its sequel for more details on what permutation groups look like. For $\sigma\in S_{n}$ define $\left(-1\right)^{\sigma}$ to be the parity of $\sigma$ (1 if $\sigma$ is an even permutation and $-1$ if it is odd).

Then the determinant of a matrix is defined as:

$$\det A=\sum_{\sigma\in S_{n}}\left[(-1)^{\sigma}\prod_{i=1}^{n}a_{i,\sigma(i)}\right]$$

That is, for each permutation you take the products of the entries of $A$ whose rows and columns are input-output pairs of $\sigma$, scale by the parity of $\sigma$, and sum.

A more useful definition of the determinant explains why it shows up in so many geometric formulas: it computes the signed volume of a particular solid based on the rows of $A$. This solid is called a *parallelepiped*, the $n$-dimensional analogue of a parallelogram. For example, for the (signed) area of a triangle $T$ with vertices $(a_{x},a_{y}),(b_{x},b_{y}),(c_{x},c_{y})$, we used

$$ \det\begin{pmatrix}1&a_{x}&a_{y}\\ 1&b_{x}&b_{y}\\ 1&c_{x}&c_{y}\end{pmatrix} $$

This embeds the triangle in the plane defined as $\{x\in\mathbb{R}^{3}:x_{1}=1\}$, and computes the signed volume of the triangular prism of height $1$ whose apex is the origin and whose base is $T$. We set the prism's height to $1$ so that the volume of the prism equals the area of $T$. If the points lie in a line, the volume is zero, and otherwise the sign is determined by whether the vertices of $T$ are visited in clockwise or counterclockwise order. Note that swapping two rows of a matrix multiplies the determinant by $-1$.

### The Hyperbolic Isometry Group as a Group of Matrices

Multiple times throughout this book, we've avoided using complex numbers, resulting in some slightly nonstandard work. This was essentially a cop out. Be that as it may, the group structure of hyperbolic isometries is best studied with complex numbers.

The briefest review: the set $\mathbb{C}=\{a+ib:a,b\in\mathbb{R}\}$ is called the set of *complex numbers*, where $i$ is the "complex unit," i.e., it's a unit vector defined to be linearly independent from $1$. There is a bijection $\mathbb{C}\to\mathbb{R}^{2}$ via $a+ib\mapsto(a,b)$, so that complex numbers can be viewed as a plane. Using this view, denote by $\arg(a+bi)$ the angle between $(a,b)$ and $(1,0)$ (chosen to be in the interval $[0,2\pi)$), denote by $|a+bi|$ the length of $(a,b)$, and define multiplication of $a+ib=(a,b)$ by $i$ as the rotation of $(a,b)$ by $90$ degrees counterclockwise. Extrapolate from this that $i^{2}=-1$, and assert that the usual arithmetic rule that $(a+ib)(c+id)=ac-bd+i(ad+bc)$.

As an elegantly stated consequence, if $z,w\in\mathbb{C}$ then their multiplication is uniquely determined by the two properties $\arg(zw)=\arg(z)+\arg(w)$ and $|zw|=|z||w|$. Multiplying two complex numbers adds their angles and multiplies their lengths. Inverses are also defined: $1/z$ is the unique complex number whose angle is $2\pi-\arg(z)$ and whose length is $1/|z|$, provided $z\neq 0$. If we define the *complex conjugate* $\overline{a+bi}=a-bi$, then $1/z=\overline{z}/|z|^{2}$. This formula looks familiar; it's because $z\mapsto 1/\overline{z}$ is a geometric inversion in the unit circle.

There is a slick encoding of Poincaré disk isometries as a group of matrices. First identify $(x,y)\in\mathbb{D}^{2}$ with the complex number $z=x+iy$. Then consider the two maps defined for any two constants $a,b\in\mathbb{C}$:

$$
\begin{aligned}
f^{+}_{a,b}(z) &=\frac{az+b}{\overline{b}z+\overline{a}}\\
f^{-}_{a,b}(z) &=\frac{a\overline{z}+b}{\overline{b}\,\overline{z}+\overline{a}}
\end{aligned}
$$

Also force $a,b$ to satisfy $|a|^{2}-|b|^{2}=1$. These are the isometries of the Poincaré disk.

**Theorem 16.27.** *The isometries of $\mathbb{D}^{2}$ are of the form $f^{+}_{a,b}$ or $f^{-}_{a,b}$.*

*Proof.* The proof is left in the exercises for those who feel comfortable with complex numbers. $\blacksquare$

The functions $f^{+}_{a,b}$ are "orientation preserving" isometries of $\mathbb{D}^{2}$, meaning they are a product of an even number of reflections. Each one can be identified with a matrix

$$ f^{+}_{a,b}\mapsto\begin{pmatrix}a&b\\ \overline{b}&\overline{a}\end{pmatrix} $$

And if you multiply the matrices, you get the composition of the two maps.

Likewise, the functions $f^{-}_{a,b}$ form orientation reversing isometries (the product of an odd number of reflections). It is tedious, but elementary, to show that a product of the form $f^{-}_{c,d}\circ f^{-}_{a,b}$ has the form $f^{+}_{\overline{a}c+db,\,\overline{b}c+ad}$, which is exactly what you get when you multiply their corresponding matrices. Two orientation reversing isometries compose to get an orientation preserving isometry (if not, it would be hard to speak of "orientation" in good faith). One must be a little careful here, because the matrix representations of orientation reversing and orientation preserving isometries are not trivially compatible. The same matrix $A$ is interpreted in two ways depending on whether you conjugate the input. This is one of the deficiencies of the Poincaré disk model, which is not present in some other models of hyperbolic geometry (see Exercise 16.23).

Finally, a complete description of the group. Let $G=\left\{\begin{pmatrix}a&b\\\overline{b}&\overline{a}\end{pmatrix}:a,b\in\mathbb{C}\right\}$ be the set of orientation preserving isometries under matrix multiplication. Augment this group by adding a single $f^{-}_{a,b}$, say $f^{-}_{1,0}(z)=\overline{z}$ (a reflection across the horizontal axis), to get the set $G\cup f^{-}_{1,0}G$. This is the isometry group of the Poincaré disk. Another way to describe it is that $G$, the orientation preserving isometries, is the quotient of the full isometry group by the subgroup consisting of the identity and a single reflection.
