# Eigenvectors and Eigenvalues

> The notion of eigenvalue is one of the most important in linear algebra, if not in algebra, if not in mathematics, if not in the whole of science.
>
> – Paolo Aluffi

### The Definition

If you polled mathematicians on what the "most interesting" topic in linear algebra was, they'd probably agree on eigenvalues. The definition of an eigenvalue is so simple that I can state it now without further ado.

**Definition 12.1.** Let $V$ be a vector space and let $f:V\to V$ be a linear map. A scalar $\lambda$ is called an *eigenvalue* for $f$ if there is a nonzero vector $v\in V$ such that $f(v)=\lambda v$. The associated vector $v$ is called an *eigenvector* of $f$ with the corresponding eigenvalue $\lambda$.

A more concise, less precise rephrasing is to find a "nontrivial" solution to $f(v)=\lambda v$. Note that $\lambda=0$ is a valid choice, so long as $v$ is nonzero. As you would infer from our discussion in Chapter 10, the same definition holds for a matrix $A$, where the condition is equivalently written $Av=\lambda v$.

The question of why eigenvalues are so central to linear algebra and its applications is a deep one, and there is no easy answer. In a vague sense, the eigenvectors and eigenvalues of a linear map encode the most important data about that map in a natural, efficient way. More concretely, in the scope of this chapter eigenvectors provide the "right" basis in which to study a linear map $V\to V$. They transform our perspective so that the important features of a map can be studied in isolation. If you accept that premise, it's no surprise that eigenvalues are useful for computation. But to say anything more concrete than that, to explain the universality of eigenvalues, is difficult.

The application for this chapter is a deep dive into how eigenvectors and eigenvalues explain the dynamics of a particular physical system describing one-dimensional waves. In no uncertain terms, eigenvalues are the scientific theory that reveals the inner nature of the system. As a bonus, the clarification provided by eigenvectors gives naturally efficient algorithms to determine the state of the dynamical system at any future time. In Chapter 14 we'll see how eigenvalues encode information about smooth surfaces in a way that enables optimization. And the singular values we saw in Chapter 10 are closely related to eigenvectors and eigenvalues in a way we didn't have the language to explain in that chapter (see the exercises for more on that).

I could spend all day giving examples of how eigenvectors are used in practice. But to get to the heart of what makes them useful is another task entirely. The word eigenvalue itself doesn't have any intrinsic meaning that might hint at an answer. Eigenvalue comes from the German word *eigen*, simply meaning "own," in the sense of the phrase, "I have my own principles to uphold and refuse to use emacs." In that sense, eigenvalue simply means a value that is intrinsic to the linear map. The importance of the study of eigenvalues and eigenvectors is analogous to the importance of the roots of a polynomial to the study of polynomials. Knowing the roots of a polynomial allows you to write the polynomial in a simpler form, and "read off" information about the polynomial from the simpler representation. So it is with eigenvalues and eigenvectors. The eigenvalues of a linear map are even the roots of a special polynomial (see Exercise 12.11).

### Eigenvalues Are Basis-Invariant

We'll start by proving intrinsic-ness; the eigenvalues of a matrix are independent of the choice of basis. Let $A$ be the matrix representation of a linear map $f:\mathbb{R}^{n}\to\mathbb{R}^{n}$, written with respect to the standard basis. Let $U$ be a change of basis matrix. That is, the columns of $U$ are the new basis vectors, and if we were to write $f$ with respect to the new basis, its matrix would be $B=UAU^{-1}$. Recall, in words, this matrix converts the input to the standard basis via $U^{-1}$ (the inverse of $U$), then applies $A$, then converts the output back to the new basis using $U$. Now we can state the theorem.

**Theorem 12.2.** Let $A$ be a matrix and $U$ be a change of basis matrix, with $B=UAU^{-1}$. Let $v\in\mathbb{R}^{n}$ be an eigenvector for $A$ with eigenvalue $\lambda$. Then $v'=Uv$ is an eigenvector for $B$ that also has eigenvalue $\lambda$.

*Proof.* We need to show that $BUv=\lambda Uv$. To do this, expand $B=UAU^{-1}$ and apply algebra. In what follows, $I_{n}$ is the $n$-by-$n$ identity matrix, i.e., the representation of the function $I(v)=v$ that is the same for every basis.

$$(UAU^{-1})(Uv)=UA(U^{-1}U)v=UAI_{n}v=U(Av)=U(\lambda v)=\lambda Uv.$$

Finally note that since $U$ is an invertible matrix and $v$ is nonzero, $Uv\neq 0$ as well. $\blacksquare$

So while (the coordinates of) eigenvectors are not preserved across different bases, the eigenvalues are. A technical way to say this is that eigenvalues of a linear map $f$ are *invariant* properties of $f$. Invariance means that the property doesn't change under some prespecified family of transformations. In this case, eigenvalues are invariant under the operation of changing a basis. Invariance is a natural property to require for something which purports to reveal the divine secrets of a linear map.

This is also related to our earlier discussion in Chapter 8 of the well-definition of the limit. We're saying that the eigenvalues of a linear map don't depend on the arbitrary choices you make to represent them in the nice computational setting of matrix algebra. However, this time it's a bit different because we didn't intentionally bake basis-invariance into the definition. If you stumbled across a matrix-vector equation like $Av=2v$ in the wild, perhaps while modeling some physical system, it might not occur to you that the number $2$ is a special property of the system. In other words, this invariance feels discovered. On the other hand, the definition of a limit had an explicit invariance baked in.

Invariance is a "smell." Invariant properties point toward the soul of mathematics. We'll have more to say on this when we study hyperbolic geometry in Chapter 16.

We can watch this invariance happen numerically. Conjugating a matrix $A$ by any invertible $U$ leaves its eigenvalues untouched, and carries each eigenvector $v$ of $A$ to the eigenvector $Uv$ of $B$. While we're here, two free facts fall out: the trace is the sum of the eigenvalues and the determinant is their product.

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/02_invariance.py -->
```

### Eigenvectors as Maximally Invariant Directions

An eigenvector $v$ of $A$ has another sort of "invariance" under the operation of left-multiplication by $A$. That is, if you ignore scaling—or rescale $v$ to a unit vector before and after left multiplying by $A$—then $A$ sends $v$ to itself. This is why we say that the eigenvectors span the "best axes" in which to view $A$, because $A$ sends any vector on the axis to another vector within the same line. They exhibit maximal invariance when the linear map is applied to them. And for the limited scope of this chapter, the set of all eigenvalues and eigenvectors of a linear map allows one to represent the entire map in terms of these invariant, independent pieces.

This is the best high-level intuition I can give without getting too deep in the math. Before we do, let's see a compelling example of why eigenvalues are so interesting and complex for specific matrices called *adjacency matrices*. In the next section we won't prove any of the theorems we state.

## Eigenvalues of Graphs

Let $G=(V,E)$ be an undirected graph, the same sort we studied in Chapter 6. There is a natural matrix we can associate with $G$, defined as follows.

**Definition 12.3.** Let $G=(V,E)$ be a graph and $V=\{v_{1},\ldots,v_{n}\}$ (i.e., pick an ordering of the $n$ vertices of $G$). Define the *adjacency matrix of $G$*, denoted $A(G)$, as the $n\times n$ matrix whose $i,j$ entry is $1$ if $(v_{i},v_{j})\in E$ and $0$ otherwise.

In the exercises, you will write down a description of this matrix as a linear map and interpret what it means in graph-theoretic terms. In particular, each of the standard basis vectors $e_{i}=(0,\ldots,0,1,0,\ldots,0)$ can be thought of as identifying the $i$-th vertex $v_{i}$ of $G$. Figure 12.1 is an example graph and its adjacency matrix. We call a graph *bipartite* if its vertices can be partitioned into two parts in such a way that all edges cross from one part to the other. The graph $G$ in Figure 12.1 is bipartite because it can be partitioned into $\{1,3\}$ and $\{2,4,5\}$.

<!-- carousel -->
![Figure 12.1a: The example graph $G$, with edges $1\text{–}2$, $1\text{–}4$, $1\text{–}5$, and $3\text{–}4$.](07 - Eigenvectors and Eigenvalues_images/img-0.jpeg)
![Figure 12.1b: The adjacency matrix $A(G)$. Rows and columns are indexed by the standard basis vectors $e_i$; the $i,j$ entry is $1$ exactly when $v_i$ and $v_j$ are joined by an edge.](07 - Eigenvectors and Eigenvalues_images/img-1.jpeg)
<!-- endcarousel -->

Bipartite graphs are common in applications, because they naturally encode networks in which there are two classes of things, where things within a class don't relate to each other. For example: students and teachers, with edges being class membership; wholesale factories and distributors, with edges being shipments; or files and users, with edges being access logs. Problems that can be intractable on general graphs can be easy to solve on bipartite graphs, which is a compelling reason to study them.

### Detecting Bipartiteness from the Spectrum

Now here is a fantastic theorem that we won't prove. Let $A(G)$ be the adjacency matrix of a (not-necessarily bipartite) graph $G$. Let $\lambda_1$ be the largest eigenvalue, $\lambda_2$ the second largest, etc., so that $\lambda_n$ is the smallest. Note that these eigenvalues may be negative. Also note that adjacency matrices have $n$ eigenvalues, though to see why we'll need the theory built up in this chapter (Propositions 12.11 and 12.14).

**Theorem 12.4.** Let $G$ be a connected graph. Then $G$ is bipartite if and only if $\lambda_1 = -\lambda_n$.

We can put this to an immediate test. Building Kun's Figure 12.1 graph and asking numpy for its eigenvalues, we find a spectrum that is perfectly symmetric about zero—the telltale signature of bipartiteness. A triangle ($K_3$, the smallest odd cycle) breaks the symmetry, as it must.

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/01_graph_eigenvalues.py -->
```

This is just one of the many ways that the eigenvalues of the adjacency matrix of $G$ encode information about $G$. In hindsight, it's obvious that some relationship should exist: there is a systematic way to get from the graph $G$ to the eigenvalues. What's surprising is that they encode such natural and useful information about $G$, which might otherwise require designing an algorithm to discover.

### Finding Planted Cliques via Eigenvectors

Here is another theorem, which I will paraphrase slightly to hide the nitty-gritty details. It says that the eigenvector for the second-largest eigenvalue of the adjacency matrix encodes information about tightly-knit clusters of vertices in a graph. In fact, it encodes this information better than simple statistics in the following concrete setting.

Let $G = (V, E)$ be a graph constructed by the following process: for each pair of vertices $v_i, v_j \in V$, flip a fair coin. If heads, make $(v_i, v_j)$ an edge of $E$. Otherwise, skip that edge. You can prove that this process produces all possible graphs with equal likelihood, so the output is simply called a *random graph*.

One can show (though we will not) that for a random graph, with overwhelming probability the densest cluster of vertices will have almost exactly $2\log(n)$ vertices in it. It's also widely believed that no efficient algorithm can reliably find the densest cluster.

So to make this cluster-finding problem easier, after creating the graph in this random way, pick a random subset of vertices of size $t$, and connect all remaining edges among those vertices. We'll call the chosen subset a *planted clique*. In general, a *clique* is a subset of vertices with a complete set of edges among them. It's a subgraph that forms the complete graph $K_{t}$ for some $t$. You might expect that such a dense cluster of vertices would be detectable, simply by being a statistical anomaly. Maybe you could just count up how many edges are on each vertex, looking at the ones that are unusually large, to find the planted clique. I won't prove so here, but for this method to work, the planted clique must have size at least $t\sim\sqrt{n\log n}$. The following algorithm succeeds for a much smaller $t$:

**Theorem 12.5.** Let $v$ be an eigenvector for $\lambda_{2}$, the second largest eigenvalue of the adjacency matrix of $G$, a random graph on $n$ vertices with a planted clique of size at least $\sqrt{n}$. The following algorithm recovers the vertices of the planted clique with high probability:

1. Recall that the indices of $v$ correspond to vertices of $G$, and select $\sqrt{n}$ such vertices whose corresponding entries in $v$ are the largest in absolute value. Call this set $T$.
2. Output the set of vertices of $G$ that are adjacent to at least $3/4$ of the vertices in $T$.

This is a result that is quite recent by mathematics standards. It was proved in 1998 by Alon et al. No method is known to exist that can reliably find a smaller planted clique, and moreover it can be *proved* that methods that only use statistics about the graph cannot find a smaller clique. All of this is to say, eigenvalues of the adjacency matrix don't just encode information about $G$, in certain settings they do so in an *optimal way*. The specific area of math studying how and when eigenvalues are useful in encapsulating information about graphs is called *spectral graph theory*. The general idea of using eigenvalues and eigenvectors of matrices derived from a graph to find dense clusters is called *spectral clustering*, and there are many variations.

## Limiting the Scope: Symmetric Matrices

By now I hope I have convinced you that eigenvectors and eigenvalues, together often called an *eigensystem*, encode useful information about linear maps, and the underlying data those linear maps represent.

However, we still have little understanding about why eigensystems reveal such valuable information. The briefest possible answer might be formulated as "eigenvectors, scaled by their eigenvalues, provide the most natural coordinate system in which to view linear maps $V\to V$."

A stronger intuition is difficult to explain without a longer expedition into the theory than we have time in these pages. One reason it's hard is that a linear map $f$ on $\mathbb{R}^{n}$ might not have any eigenvalues! For example, the $2$-dimensional linear map that rotates a vector by $\pi/4$ radians clockwise. In fact, the existence of eigenvalues and eigenvectors is similar in nature to the existence of roots of single-variable polynomials. We will reveal the first step toward making this connection concrete in Exercise 12.11. As a consequence, some linear maps only have eigenvalues that are complex numbers, and the corresponding eigenvectors have complex entries. Each complex eigenvalue a linear map has reduces the number of real eigenvalues it can have.

Introducing complex numbers makes other things simpler, while making some things more complicated. But more importantly, if you're not comfortable with the geometry of complex numbers, you will have difficulty interpreting how they relate to a linear map for vectors of real numbers. This book skips complex numbers, so we will not be able to give a complete picture.

A second reason is that multiple linearly independent eigenvectors can exist for the same eigenvalue, and there may or may not be "enough" eigenvectors to provide a complete picture. This topic is nuanced—and not needed for our application—so we omit it except to mention some pointers in the "Computing Eigenvalues" section.

Luckily, there is a nice way to avoid dealing with these problems while still seeing the lion's share of eigenvalue power in practice. That is the following theorem:

**Theorem 12.6.** Let $f:\mathbb{R}^{n}\to\mathbb{R}^{n}$ be a linear map and let $A$ be its associated matrix. If $A$ is *symmetric*, meaning $A[i,j]=A[j,i]$ for every $i,j$, then $A$ has $n$ real eigenvalues (not necessarily distinct) and eigenvectors.

### Symmetry and the Transpose

A useful notation when working with symmetric matrices is that of the *transpose*. Define by $A^{T}$ the matrix whose $i,j$ entry is $A[j,i]$. That is, you take $A$, and flip it along the top-left-to-bottom-right diagonal, and you get $A^{T}$. With this notation, saying $A$ is symmetric is saying that $A=A^{T}$. Here's an example of a symmetric matrix.

$$\begin{pmatrix}1&2&3&4\\2&5&6&7\\3&6&8&9\\4&7&9&-1\end{pmatrix}$$

In Chapter 10 I promised you that every operation on a matrix corresponds to an operation on a linear map. This is also true for the matrix transpose. If $f$ is a linear map and $A$ is a matrix representation, then $A^{T}$ corresponds to some linear map $f^{T}$ that's related to $f$. However, the operation itself is difficult to describe without a lot of extra notation and definitions. We'll revisit those ideas in the Chapter Notes, but here we'll directly prove the important takeaway of that discussion: symmetric matrices play nicely with the inner product.

First, one can verify that the standard inner product definition results in $\langle Ax,y\rangle=\langle x,A^{T}y\rangle$ for all $x,y$. This is often written as $\langle Ax,y\rangle=x^{T}A^{T}y$. One considers vectors "single-column matrices," notes that in this perspective $\langle x,y\rangle=x^{T}y$, and then, using Exercise 12.1 that $(AB)^{T}=B^{T}A^{T}$,

$$\langle Ax,y\rangle=(Ax)^{T}y=x^{T}A^{T}y=\langle x,A^{T}y\rangle.$$

With symmetry, this simplifies to $\langle Ax,y\rangle=\langle x,Ay\rangle$. What's special is that symmetric matrices can be defined by this property.

**Theorem 12.7.** Let $A$ be a real-valued $n\times n$ matrix, and let $\langle-,-\rangle$ denote the standard inner product of real vectors. Then $A$ is symmetric if and only if $\langle Ax,y\rangle=\langle x,Ay\rangle$ for every pair of vectors $x,y\in\mathbb{R}^{n}$.

*Proof.* Symmetry gives the forward direction of the "if and only if," since $\langle x,A^{T}y\rangle=\langle x,Ay\rangle$. For the reverse direction, suppose that $\langle Ax,y\rangle=\langle x,Ay\rangle$ for all $x,y$. Let $a_{1},\ldots,a_{n}$ be the columns of $A$, and apply this fact to the vectors $x=e_{i},y=e_{j}$ (the standard basis vectors with a $1$ in positions $i$ and $j$, respectively). We have

$$\langle Ae_{i},e_{j}\rangle=\langle a_{i},e_{j}\rangle=A[j,i]$$

And we can do the same thing with $A$ on the other side, by assumption:

$$\langle e_{i},Ae_{j}\rangle=\langle e_{i},a_{j}\rangle=A[i,j]$$

Since $\langle Ae_{i},e_{j}\rangle=\langle e_{i},Ae_{j}\rangle$, we get $A[i,j]=A[j,i]$, implying $A$ is symmetric. $\blacksquare$

### Every Symmetric Matrix Has a Real Eigenvalue

We will use symmetry to prove that every symmetric matrix with real-valued entries has a real eigenvalue. This is the central lemma needed to prove Theorem 12.6. Funnily, we've spent so long preaching the virtues of eigenvalues, we haven't even considered the basic question of their existence!

**Lemma 12.8.** Let $A$ be a symmetric real-valued matrix. Then $A$ has a real eigenvalue.

*Proof.* Let $x$ be a unit vector which maximizes the norm $\|Ax\|$, and let $c=\|Ax\|$. Then $Ax=cy$ for some unit vector $y$. If $y$ is in the span of $x$ (which happens most of the time), then we are done, because $Ax=cy=(cd)x$ for some $d\in\mathbb{R}$, which makes $cd$ an eigenvalue. Otherwise, we may assume going forward that $x$ and $y$ are linearly independent. By the maximality of $x$ we know that $\|Ay\|\leq c$.

We will show that $x+y$ is an eigenvector with eigenvalue $c$. After the proof we'll explain as a side note why it makes sense in hindsight to consider $x+y$. Now notice that

$$\langle x,Ay\rangle=\langle Ax,y\rangle=\langle cy,y\rangle=c.$$

The first equality is due to Theorem 12.7, the second is the definition of $y$, and the third is because the inner product is linear in each argument and $y$ is a unit vector (Proposition 10.19).

The crucial observation is that $\langle x,Ay\rangle$ is the (signed) length of the projection of $Ay$ onto the unit vector $x$. Projecting a vector onto a unit vector can only make the first vector shorter. You should have some intuitive sense that this is true after our analysis—particularly the pictures—in Chapter 10. We leave a rigorous proof for the exercises. As a consequence, $c=\langle x,Ay\rangle\leq\|Ay\|$.

Combining this fact with the earlier fact that $\|Ay\|\leq c$ gives us

$$c=\langle x,Ay\rangle\leq\|Ay\|\leq c$$

Since $c$ is on either end of this inequality, all of the quantities must be equal! Indeed, the only way for the projection of $Ay$ onto $x$ to have the same length as $Ay$ is for $Ay$ to be in the span of $x$ already. To summarize, we have proved that $Ax=cy$ and $Ay=cx$.

The final observation is simply that $A(x+y)=Ax+Ay=cy+cx$, and so $c$ is an eigenvalue for $x+y$. $\blacksquare$

To fulfill my promise: $x+y$ is a natural choice of eigenvector because it's on the line "halfway" between $x$ and $y$. Indeed, it's in the span of the vector $(x+y)/2$, which is a more suggestive way to say the "average" of $x$ and $y$. Symmetry was our guide: $A$ sends $x$ to the span of $y$ and vice versa. The seasoned linear algebraist would guess—and prove shortly thereafter—that the symmetry extends to the whole plane spanned by $\{x,y\}$. Since the behavior of any linear map (on this subspace) only depends on its behavior on the basis (of the subspace), we deduce that $A$ behaves as a reflection, flipping the entire plane $\text{span}\{x,y\}$. And every reflection in a plane has a line of symmetry, which in this case is through $x+y$.

The inner product is starting to take center stage. We should study it in more detail.

## Inner Products

In order to express one very useful aspect of eigenvectors, we must revisit the discussion from Chapter 10 about the inner product. In general, a vector space only has a limited amount of geometry you can describe. However, if you specify an inner product, you can describe angles, lengths, and more. The inner product is imposed on a vector space, in the same way that a style guide is imposed on a programmer: to give structure to (or elucidate structure in) the underlying space. The standard inner product on $\mathbb{R}^{n}$ is defined by the formula

$$\langle x,y\rangle=\sum_{i=1}^{n}x_{i}y_{i}.$$

This formula is intimately connected with geometry. It can be used to compute the angle between two nonzero vectors (via $\cos\theta=\langle x,y\rangle/(\|x\|\cdot\|y\|)$), and its value is the signed length of the projection of one argument onto the other (scaled by the length of the other).

### The Power of a Generalized Inner Product

Over the years mathematicians have extracted the generic properties of this formula that conjure up its geometric magic. The result is a distilled definition of an inner product.

**Definition 12.9.** Let $V$ be a vector space with scalars in $\mathbb{R}$. An *inner product* for $V$ is a function $\langle-,-\rangle:V\times V\to\mathbb{R}$ with the following properties:

1. *Symmetric:* For every $v,w\in V$ swapping the order of the inputs doesn't change the inner product, i.e. $\langle v,w\rangle=\langle w,v\rangle$.
2. *Bi-linear:* If you fix any input to a constant $v\in V$ then the restricted function, considered as a map $V\to\mathbb{R}$, is linear. I.e., if we fix the second input $\langle-,w\rangle$, then $\langle cv,w\rangle=c\langle v,w\rangle$ for all $c\in\mathbb{R}$, and $\langle u+v,w\rangle=\langle u,w\rangle+\langle v,w\rangle$. Likewise for fixing the first input.
3. *Nonnegative norms:* For every $v\in V$, the inner product with itself is nonnegative, i.e. $\langle v,v\rangle\geq 0$. This is called the *squared norm* of $v$. Moreover, we require that the only vector with norm zero is the zero vector.

A vector space $V$ and a specific inner product $\langle-,-\rangle$ are together called an *inner product space*.

In Chapter 10 we proved Theorem 10.17 that every finite-dimensional vector space is isomorphic to $\mathbb{R}^{n}$ for some $n$. A similar theorem holds for finite-dimensional inner product spaces. That is, every finite-dimensional inner product space is isomorphic to $\mathbb{R}^{n}$ with the usual sum-of-squares inner product. The notion of isomorphism is more complicated here, because it needs to preserve the inner product. See the exercises for more details. This allows us to justify using the standard inner product and $\mathbb{R}^{n}$ for applications that lack a more principled choice.

More generally, the abstract definition of an inner product becomes more useful and interesting when you're dealing with infinite-dimensional vector spaces. We won't cover this in depth in this book, but a quick aside may pique your interest. The gold standard example of an interesting inner product space is the space of functions of a single real variable $f: \mathbb{R} \to \mathbb{R}$ whose square has a finite integral. Call this space $L^2(\mathbb{R})$, or just $L^2$ for short (the exponent reminds us we're squaring):

$$L^{2}(\mathbb{R}) = \left\{f: \mathbb{R} \to \mathbb{R} \;\middle|\; \int_{-\infty}^{\infty} f(x)^{2}\, dx \text{ is finite} \right\}$$

A typical example of where these functions occur in real life is as sound waves. $L^2$ forms a vector space. Addition is the point-wise addition of functions $(f + g)(x) = f(x) + g(x)$, and with the requisite calculus one can prove that the sum of two square-integrable functions is square-integrable. The case is similar for the other required vector space properties. And finally, the jewel in the crown, the inner product is

$$\langle f, g \rangle = \int_{-\infty}^{\infty} f(x) g(x)\, dx.$$

This inner product space—which actually satisfies some additional properties that make it into a so-called *Hilbert space*—is different from vector spaces we've seen so far. In particular, in $\mathbb{R}^n$ there's a "default" basis in which we express vectors without realizing it: the standard basis. $L^2$ has no obvious basis. From our discussion of Taylor series in Chapter 8, we know that polynomials can approximate functions in the limit. One might hope that polynomials form a basis of this space, perhaps $\{1, x, x^2, \ldots\}$. But actually these functions are not even in $L^2$. Moreover, many functions in $L^2$ aren't differentiable everywhere, so Taylor series can run into trouble.

As it happens, there are many interesting and useful bases for this space. For example, the following basis is called the *Hermite basis*:

$$\{e^{-x^{2}/2}, x\, e^{-x^{2}/2}, x^{2} e^{-x^{2}/2}, \dots\} = \{x^{k} e^{-x^{2}/2} : k = 0, 1, 2, \dots\}$$

But proving this is a basis is not trivial! There are other useful bases as well. The Fourier basis, a staple of the signal-processing world and electrical engineering, is the set of complex exponentials $\{e^{2\pi i k x} : k \in \mathbb{Z}\}$. Since we're not officially covering complex numbers in this book, think of this basis as the set of all sine and cosine functions with all possible periods.

These bases are difficult to discover. But even when we have one, how in the name of Grace Hopper can one even write a function in such a basis? You can't set up a system of equations because there's no decent starting basis! Not to mention it'd be an infinite system of infinitely long equations.

Using the inner product, and some work to modify the basis to make it geometrically amenable, the process of writing a function with respect to one of these (modified) bases reduces to computing an inner product. Once again, we translate an intuitive but hard mathematical concept into a more computationally friendly language. This should impress upon you the importance of the inner product. Not only does it endow a vector space with new, geometric measurements; it also makes computing basis representations possible where it might otherwise not be. A powerful revelation indeed.

In the rest of this chapter, except for the application, the inner product will be considered abstractly, as we study its generic properties and how it relates to eigenvectors. We'll also see how the inner product relates to simplifying the computation of expressing a vector in terms of a basis.

### Properties of an Inner Product

Definition 12.9 implies some easy consequences. Here are two examples.

**Proposition 12.10.** Let $\mathbf{0}$ be the zero vector of $V$, and $0$ the real number zero. Then $\langle v,w\rangle=0$ for every $w\in V$, if and only if $v=\mathbf{0}$.

*Proof.* For the forward direction, if $\langle v,w\rangle=0$ for every $w$, then fix $w=v$. The defining properties of an inner product require $v=\mathbf{0}$. For the reverse direction, fix any $w$ and note that $f(v)=\langle v,w\rangle$ is a linear map. Linear maps preserve the zero vector, so $f(\mathbf{0})=0$. $\blacksquare$

In the exercises you will prove some other basic facts about inner products, but here is one too important to relegate to the end of the chapter.

**Proposition 12.11.** Let $A$ be a real-valued symmetric matrix. Let $v,w$ be eigenvectors of $A$ with corresponding eigenvalues $\lambda\neq\mu$, respectively. Then $\langle v,w\rangle=0$.

*Proof.* By the symmetry of $A$:

$$\langle\lambda v,w\rangle=\langle Av,w\rangle=\langle v,A^{T}w\rangle=\langle v,Aw\rangle=\langle v,\mu w\rangle$$

Since this is an inner product, we can pull out the scalar multiples on the far left and right-hand sides to get $\lambda\langle v,w\rangle=\mu\langle v,w\rangle$. The only way for this equation to be true in spite of $\lambda\neq\mu$ is if $\langle v,w\rangle=0$. $\blacksquare$

As we proved in Chapter 10, the standard inner product on $\mathbb{R}^{n}$ allows one to compute angles, and more specifically to determine when two vectors are perpendicular to each other. In a generic inner product space, perpendicularity is undefined, and so we define it by generalizing what we proved in $\mathbb{R}^{n}$. Perpendicularity and length get new names.

**Definition 12.12.** Two vectors $u,v\in V$ in an inner product space are called *orthogonal* if $\langle u,v\rangle=0$.

Another way to say Proposition 12.11 is that if two eigenvectors are *not* orthogonal, then they must have the same corresponding eigenvalue (this is the contrapositive statement).

**Definition 12.13.** The *norm* of a vector $v\in V$ is the quantity $\|v\|=\sqrt{\langle v,v\rangle}$. Without a square root, it's called the *square norm*. Vectors with norm 1 are called *unit vectors*.

Most of the facts about perpendicularity and projection we proved for $\mathbb{R}^{n}$ actually don't depend on the definition of the standard inner product. They can be re-proved using any inner product, because the key ingredients from those proofs were extracted into the definition of an inner product. Next we'll show that orthogonal vectors can be used to build up a basis.

**Proposition 12.14.** Any set of nonzero vectors $\{v_{1},\ldots,v_{k}\}$ which is pairwise orthogonal (for each $i\neq j$, $\langle v_{i},v_{j}\rangle=0$) is linearly independent.

*Proof.* Let $\{v_{1},\ldots,v_{k}\}$ be as in the statement of the proposition, and suppose $c_{1}v_{1}+\cdots+c_{k}v_{k}=0$. To show linear independence, recall, we need to show that all the $c_{i}=0$. Fix any $i$. To show $c_{i}$ is zero, inspect $\langle c_{1}v_{1}+\cdots+c_{k}v_{k},v_{i}\rangle$, which is zero because the first argument is zero by assumption. By linearity, this splits up as $\sum_{j=1}^{k}c_{j}\langle v_{j},v_{i}\rangle$. By pairwise orthogonality, all the terms in the sum are zero except $c_{i}\langle v_{i},v_{i}\rangle$. Thus, this sum reduces to $c_{i}\langle v_{i},v_{i}\rangle=0$. Then either $v_{i}=0$ (ruled out by assumption) or $c_{i}=0$. The same argument applies to every $c_{i}$. $\blacksquare$

## Orthonormal Bases

Bases consisting of orthogonal unit vectors are glittering treasures for computation. They make it easy to write a vector in terms of that basis. Let $V$ be an inner product space, and suppose that $\{v_{1},\ldots,v_{n}\}$ is a basis for $V$, where every $v_{i}$ is a unit vector and $\langle v_{i},v_{j}\rangle=0$ for every $i\neq j$. Such a basis is called an *orthonormal basis*. The "ortho" is because each pair is orthogonal, and "normal" because each vector is a unit vector (normalized). Having such a basis allows you to compute the basis representation of any vector using inner products.

**Proposition 12.15.** Let $\{v_{1},\ldots,v_{n}\}$ be an orthonormal basis for $V$, and let $x\in V$. Then $x$ can be written as

$$x=\langle x,v_{1}\rangle v_{1}+\cdots+\langle x,v_{n}\rangle v_{n}$$

That is, the coefficient of the basis vector $v_{i}$ is $\langle x,v_{i}\rangle$.

*Proof.* Fix any basis vector $v_{i}$ and let $x=c_{1}v_{1}+\cdots+c_{n}v_{n}$ where $c_{j}$ are the (unknown) coefficients of $x$'s representation with respect to the basis. Then

$$
\begin{aligned}
\langle x,v_{i}\rangle &=\langle c_{1}v_{1}+\cdots+c_{n}v_{n},v_{i}\rangle \\
&=c_{1}\langle v_{1},v_{i}\rangle+\cdots+c_{n}\langle v_{n},v_{i}\rangle \\
&=c_{1}\cdot 0+\cdots+\underbrace{c_{i}\cdot 1}_{i\text{-th term}}+\cdots+c_{n}\cdot 0 \\
&=c_{i}.
\end{aligned}
$$

And so the inner product gives us exactly the coefficient we wanted. $\blacksquare$

This shortcut is dramatic. The naive way to write $x$ in a basis $\{v_i\}$ is to set up the system $Ay=x$, with the $v_i$ as columns of $A$, and solve it with Gaussian elimination—cubic time in $n$. With an *orthonormal* basis, the coefficients are just $n$ inner products: quadratic time, no solve at all. The following demo builds an orthonormal basis with Gram-Schmidt (which we define just below), then confirms the two methods agree to machine precision.

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/05_orthonormal_basis.py -->
```

As we've discussed, the naive approach to computing the basis representation of a vector $x\in\mathbb{R}^{n}$ with respect to a basis $\{v_{i}\}$ would be to set up the system of linear equations $Ay=x$, where the columns of $A$ are the $v_{i}$, and solve for $y$ using a technique like Gaussian elimination. As it turns out, Gaussian elimination takes cubic runtime in the worst case (cubic in $n$, the dimension of the vector space).

However, with an orthonormal basis all you need to do is compute $n$ inner products. The standard inner product only takes $n$ multiplications and $n$ additions, meaning the entire decomposition only takes time $n^{2}$. This is a huge improvement if, suppose, you could compute an orthonormal basis once and use it to compute basis representations many more times, as opposed to doing Gaussian elimination for each vector you wanted to represent in the target basis. It's also worth noting that in practice there's often a natural ordering on a basis, so that the first vectors in the basis contribute "most significantly" to the space, and one can approximate a basis representation using a constant-sized subset of the basis. The singular values played this role in Chapter 10. For our physics application the eigenvalues will determine the ordering.

But beyond that, in a space like $L^{2}$ where there's no natural starting basis, this gives us a feasible way to compute basis representations: just compute the inner product! In $L^{2}$ you simply integrate.

### Orthonormal Change of Basis Matrices

Going back to finite dimensions, the next important property of an orthonormal basis is that the change of basis matrix (the matrix with the basis vectors as columns) is easy to invert.

**Proposition 12.16.** Let $\{v_{1},\ldots,v_{n}\}$ be an orthonormal basis for $V$, with the $v_{i}$ written in terms of some other basis $\{e_{1},\ldots,e_{n}\}$. Let $B$ be the corresponding change of basis matrix, with the $v_{i}$ as columns. Then $B^{T}=B^{-1}$.

*Proof.* We can prove this directly by showing that $B^{T}B$ is the identity matrix, i.e., the matrix $I_{n}$ with 1s on the diagonal and zeros elsewhere. Indeed, the entries of $B^{T}B$ encode all pairwise inner products of the vectors in the basis. The $i,j$ entry of $B^{T}B$ is the inner product $\langle v_{i},v_{j}\rangle$, which is $1$ if and only if $i=j$, and zero otherwise.

One may wonder if it's also necessary to show $BB^{T}=I_{n}$ in order to conclude that $B^{T}$ is a proper inverse of $B$. A direct proof hits an immediate barrier, because the inner products don't line up as they did above. It turns out this barrier is a mirage. By pure set theory, namely Proposition 4.13 from Chapter 4, a one-sided inverse of a bijection is automatically a two-sided inverse. All change of basis matrices are bijections. $\blacksquare$

This has an almost startling consequence:

**Proposition 12.17.** If the columns of $A$ form an orthonormal basis, then so do the rows of $A$.

*Proof.* Let $B=A^{T}$. Then $B$ satisfies $B^{T}B=I_{n}$, which as we saw above encodes all the pairwise inner products of columns of $B$, i.e., rows of $A$. Since orthogonal vectors are linearly independent (Proposition 12.14), the columns of $B$ form a basis. $\blacksquare$

If we wanted to prove this without set theory hijinks, we could have done so by proving $(A^{T})^{-1}=(A^{-1})^{T}$. You will do this in the exercises.

### The Gram-Schmidt Process

Our next task is to compute orthonormal bases. For finite dimensional inner product spaces there's an algorithmic method called the *Gram-Schmidt process*. It falls short of an algorithm by not defining how to do one important step. First, a definition:

**Definition 12.18.** Let $V$ be an inner product space and $W\subset V$ a subspace with an orthonormal basis $B=\{w_{1},\ldots,w_{k}\}$. Let $v$ be a vector, and define the *projection of $v$ onto the subspace $W$*, denoted by $\operatorname{proj}_{W}(v)$, as follows:

$$\operatorname{proj}_{W}(v)=\sum_{w_{i}\in B}\operatorname{proj}_{w_{i}}(v)$$

The projection of $v$ onto a subspace is the natural geometric generalization of projecting onto a vector. Projecting onto a subspace is the same thing as projecting onto each axis of any basis of that subspace and adding up the results. And just like the one-vector version, $v-\operatorname{proj}_{W}(v)$ is the part of $v$ that lies perpendicular to the subspace $W$ in the sense that it's perpendicular to every vector in $W$.

The Gram-Schmidt process operates as follows to build up an orthonormal basis for an $n$-dimensional inner product space (or subspace).

1. Let $S_{0}=\{\}$ be the empty set. $S_{i}$ will contain the partial basis built up so far at step $i$.
2. For $i=1,\ldots,n$:
   1. Let $v$ be any vector not in the span of $S_{i-1}$.
   2. Let $v'=v-\operatorname{proj}_{\operatorname{span}(S_{i-1})}(v)$ (get the perpendicular part), or $v'=v$ if $i=1$.
   3. Let $S_{i}=S_{i-1}\cup\{v'/\|v'\|\}$ (add normalized $v'$ to the partial basis).
3. Output $S_{n}$.

The Gram-Schmidt process doesn't dictate how to find a vector not in the span of a given set, but using that as a subroutine, the rest is well-defined arithmetic. The proof that the result is an orthonormal basis is a simple exercise in induction. The same algorithm allows one to start from a given basis (possibly of a subspace), and transform it into an orthonormal basis with the same span. For this variant, if you have a subspace basis $\{v_{1},\ldots,v_{k}\}$, and you want to know what new vector to choose at step $i$, you can simply choose $v_{i}$.

As a side note, this algorithm is generally not considered "production ready," because it suffers from numerical instability. Most industry-strength linear algebra libraries use one of a few different techniques based on linear algebra primitives (such as Householder reflections and the famed Cholesky decomposition) that have been fine-tuned and optimized for speed and stability. Instead, it serves as a proof of existence.

## Computing Eigenvalues

Our ultimate goal is to come up with an orthonormal basis of eigenvectors. This will combine the computational ease of orthogonality with the deep secrets revealed by eigenvalues. To appreciate Theorem 12.22, we should investigate why finding a basis of eigenvectors might be hard.

For instance, we established existence of at least one eigenvalue-eigenvector pair, but can we say anything about uniqueness? Given a linear map $A$ with eigenvector $v$ and corresponding eigenvalue $\lambda$, it is obvious that every nonzero vector in $\text{span}(v)$ is also an eigenvector for $\lambda$. But is it possible that some independent vector is also an eigenvector for $\lambda$? A simple example says yes: take the map $f:\mathbb{R}^{3}\to\mathbb{R}^{3}$ sending $(a,b,c)\mapsto(a,b,0)$, a projection onto the degree-two subspace spanned by $(1,0,0)$ and $(0,1,0)$. Both $(1,0,0)$ and $(0,1,0)$ are eigenvectors for the eigenvalue $\lambda=1$, and so are all nonzero linear combinations. The story of an eigenvalue stretches beyond finding a single eigenvector. Due to this, we have a name for the subspace of a vector space $V$ spanned by the eigenvectors of a single eigenvalue $\lambda$ of a map $f:V\to V$, the *eigenspace* for $\lambda$ and $f$.

### Kernels, Eigenspaces, and Geometric Multiplicity

Another reason why the analysis of eigenvalues is hard is that zero can be an eigenvalue. The eigenvectors with eigenvalue zero span the preimage of the zero vector.

**Definition 12.19.** Let $f:V\to W$ be a linear map. Define the *kernel* of $f$, denoted $\ker(f)$, to be the set of $v\in V$ with $f(v)=0$.

As a quick exercise, prove that the kernel of a linear map is a subspace of $V$. Rephrasing the above, the eigenvectors of $f$ corresponding to the eigenvalue $\lambda=0$, along with the zero vector, are exactly the kernel of $f$.

If you believe that finding roots of single-variable polynomials is hard, you might also be convinced that finding "roots" of linear maps is hard. In fact, you'll prove in an exercise that computing eigenvalues of linear maps is at least as hard as computing roots of polynomials. And as we'll see below, all eigenvalues can be expressed in terms of kernels. For the next proposition, $I$ denotes the identity map $I(x)=x$, with corresponding matrix $I_{n}$ for $n$-dimensions.

**Proposition 12.20.** Let $f:V\to V$ be a linear map. Then a nonzero $v\in V$ is an eigenvector corresponding to eigenvalue $\lambda$ if and only if $v\in\ker(f-\lambda I)$. By $f-\lambda I$ we mean the map $x\mapsto f(x)-\lambda x$.

*Proof.* Indeed, $f(v)=\lambda v$ if and only if $f(v)-\lambda v=0$. $\blacksquare$

We saw an example of a simple map $(a,b,c)\mapsto(a,b,0)$ that has a two-dimensional eigenspace for the eigenvalue $1$. The matrix for this is

$$A=\begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}$$

And we can inspect the matrix $A-\lambda I_{3}$ to compute the remaining eigenvalues.

$$A-\lambda I_{3}=\begin{pmatrix}1-\lambda&0&0\\0&1-\lambda&0\\0&0&-\lambda\end{pmatrix}$$

A vector $(a,b,c)$ in the kernel of this map (for some unknown $\lambda$) must satisfy $a(1-\lambda)=0$ and $b(1-\lambda)=0$ and $-\lambda c=0$. The third equality implies either $\lambda=0$ or $c=0$. In the former case, $a=b=0$ and we get $(0,0,1)$ as an eigenvector for $\lambda=0$. In the latter case, we're left with the previously mentioned two-dimensional eigenspace for $\lambda=1$.

Here's a more interesting example, the matrix for the map $(a,b,c)\mapsto(a+b+c,b+c,c)$.

$$B=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$$

This matrix clearly has one eigenvector, $(1,0,0)$ for the eigenvalue $\lambda=1$. But what about other potential eigenvectors? Indeed, we're looking for the kernel of $B-I_{3}$, which is

$$B-I_{3}=\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix}$$

Aside from the span of $(1,0,0)$, there are no other vectors in the kernel. And moreover, $B-\lambda I_{3}$ for $\lambda\neq 1$ has only the trivial kernel $\{0\}$ (set up the system of three equations and verify this).

When an eigenvalue has multiple independent eigenvectors, we get a viscerally interpretable kind of "multiplicity," which goes by the name *geometric multiplicity*.

**Definition 12.21.** Let $f:V\to V$ be a linear map. The *geometric multiplicity* of an eigenvalue $\lambda$ for $f$ is the dimension of the eigenspace for that eigenvalue, i.e., the dimension of $\ker(f-\lambda I)$ as a subspace of $V$.

For the matrix $A$ above, the eigenvalue $1$ has geometric multiplicity $2$, but for $B$ the multiplicity is only $1$.

There is a second kind of multiplicity, related to the geometric multiplicity, which allows one to build a complete characterization of a linear map. We will leave this for the Chapter Notes while we plow on to the main theorem and application.

### Power Iteration

Before we get there, it's worth pausing on the single most-used eigenvalue algorithm in the wild: *power iteration*. It is nothing more than the "left-multiplication invariance" of an eigenvector turned into a loop. Start with a generic vector, apply $A$, normalize, and repeat; the dominant eigenvector swallows everything else and you converge to it. The Rayleigh quotient $v^{T}Av$ then reads off the eigenvalue.

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/03_power_iteration.py -->
```

## The Spectral Theorem

If you're studying a linear map $f:V\to V$, and for each eigenvalue you can find an orthogonal set of eigenvectors spanning the eigenspace, then the representation of the matrix for $f$ is extremely simple. In this case, the eigenvectors form an orthonormal basis (recall Propositions 12.11 and 12.14). The matrix for $f$, when written with respect to that basis, has all its nonzero entries on the diagonal.

$$A=\begin{pmatrix}\lambda_{1}&0&\cdots&0\\0&\lambda_{2}&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\lambda_{n}\end{pmatrix}$$

A linear map that can be written this way for some basis is called *diagonalizable*. What's astounding is that every symmetric matrix has an orthonormal basis of eigenvectors. This is the centerpiece theorem of this chapter and the secret ingredient in the physics application to follow.

**Theorem 12.22 (The Spectral Theorem).** A real-valued matrix $A$ is symmetric if and only if it has eigenvectors that form an orthonormal basis.

This theorem requires some nontrivial amount of work, pieces of which we have already proved in this chapter. The easy part is the reverse direction. It uses the fact that $(AB)^{T}=B^{T}A^{T}$, and Proposition 12.16 that for an orthonormal change of basis matrix $U$, $U^{-1}=U^{T}$.

**Proposition 12.23.** A real-valued matrix $A$ with an orthonormal basis of eigenvectors is symmetric.

*Proof.* There is a change of basis matrix $U$, whose columns are the orthonormal basis, for which $A=U^{T}DU$, for $D$ a diagonal matrix. A diagonal matrix is clearly symmetric, so $A^{T}=(U^{T}DU)^{T}=U^{T}D^{T}(U^{T})^{T}=U^{T}DU=A$, implying $A$ is symmetric. $\blacksquare$

Before finishing the harder direction, let's see the whole theorem in one numerical breath. Force a matrix to be symmetric by averaging it with its transpose; then numpy's symmetric solver returns *real* eigenvalues and an *orthonormal* eigenvector matrix $Q$, and the factorization $A=Q\Lambda Q^{T}$ reconstructs $A$ exactly. By contrast, a $\pi/4$ rotation—not symmetric—has only complex eigenvalues, exactly as Kun warned.

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/04_spectral_theorem.py -->
```

### Proof by Induction on Dimension

The strategy for the other half of the proof will be by induction on the dimension of the vector space. That is, given the fact that every $(n-1)\times(n-1)$ symmetric matrix has an orthonormal basis of eigenvectors, we'll show that every $n\times n$ symmetric matrix does as well.

Induction suggests we should find a way to "peel off" one dimension from the matrix $A$ in a way that's independent of the rest of the argument. Given $A$, we'll find an eigenvector $v$ with corresponding eigenvalue $\lambda$, normalize it, and use it as the first vector in the basis. Then we'll decompose $\mathbb{R}^{n}$ into two subspaces, a one-dimensional space spanned by $v$, and an $(n-1)$-dimensional space, which we'll apply induction on. In particular, we will be able to rewrite $A$ in a "block" form like so:

$$A\rightarrow\begin{pmatrix}\lambda&\mathbf{0}\\\mathbf{0}&A'\end{pmatrix}$$

In the above, the boldface $\mathbf{0}$ are to denote that zeroes take up the entire "area" implied by the dimensions. If $A$ is an $n\times n$ matrix, and $\lambda$ is a scalar, then $A'$ is $(n-1)\times(n-1)$ and each boldface zero represents $n-1$ zeroes in the only allowable shape.

Intuitively, what we're doing here is partially rewriting the basis in terms of one known eigenvector. Indeed, we have to describe a full basis to get a block decomposition, but as long as whatever process we use to make the basis maintains the symmetry of $A'$, we win. We'll be able to combine the orthonormal basis of $A'$ with $v$ to get a full orthonormal basis for $A$. The remaining details relate to the algebra of a precise proof, which we'll exhibit now.

*Proof.* (Finishing the proof of the Spectral Theorem)

Suppose $A$ is a symmetric real-valued $n\times n$ matrix on an $n$-dimensional vector space $\mathbb{R}^{n}$. We will show there is an orthonormal basis of eigenvectors of $A$.

We proceed by induction on $n$. For $n=1$ the claim is trivial, because every nonzero vector is an eigenvector and every basis is orthogonal. In particular, the linear map corresponding to $A$ must be $f(x)=bx$ for some constant $b$, and so the unit vector $1$ is an eigenvector with eigenvalue $b$.

Now let $n>1$, suppose as the inductive hypothesis that every $(n-1)\times(n-1)$ symmetric matrix has an orthonormal basis of eigenvectors, and let $A$ be an $n\times n$ symmetric matrix. We begin by finding any eigenvector of $A$, with some associated eigenvalue $\lambda$. We know we can do this by Lemma 12.8. Normalize the eigenvector, call it $v$, and use it as the first vector in a new basis of $\mathbb{R}^{n}$.

Construct the rest of this basis as follows. Let $W$ be the subspace of $\mathbb{R}^{n}$ consisting of all vectors orthogonal to $v$. Use Gram-Schmidt to choose an orthonormal basis $B'=\{w_{2},\ldots,w_{n}\}$ of $W$. Joining together, $B=B'\cup\{v\}$ is an orthonormal basis of all of $\mathbb{R}^{n}$. Note that only $v$ need be an eigenvector; the other vectors in the basis are not necessarily eigenvectors of $A$, but the whole basis is orthonormal.

Because $B$ is orthonormal, the same argument as Proposition 12.23 implies that $A$, when written with respect to the basis $B$, is symmetric. So when we write $A$ with respect to $B$, the matrix decomposes into blocks (we prove this below). In what follows, I am abusing notation by using $B$ for both the basis (a set) and the relevant change of basis matrix (which implies the basis vectors are in a certain order). In particular $A'$ is the restriction of $A$ to vectors in the subspace $W$.

To prove the block form is as we say it is, we just need to reason about the first column of this matrix: if you apply $A$ to $v$ you get $\lambda v$, which includes none of the other basis vectors. So in the new basis representation you get a column with a $\lambda$ and zeros elsewhere. As we argued above, this block decomposition is symmetric, so the first row must also have zeros as indicated.

Finally, we can invoke the inductive hypothesis for the matrix $A'$ (which is symmetric because $B^{T}AB$ is) and the subspace $W$. I.e., $A'$ has an orthonormal basis of eigenvectors, call it $\{u_{2},\ldots,u_{n}\}$. Then the final basis is $\{v,u_{2},\ldots,u_{n}\}$.

There is one more detail. We defined $u_{i}$ as an eigenvector of this sub-matrix $A'$, but can we be sure it's an eigenvector of the original $A$? Indeed it is, because of the way we decomposed $\mathbb{R}^{n}$ into $\text{span}(v)$ and the orthogonal complement $W$. Specifically, to compute $Ax$ for any vector $x$, we write it with respect to the basis, and apply $A$ to each piece. In this case, if $u_{i}$ is an eigenvector for $A'$ with eigenvalue $\lambda$, then $u_{i}=\langle u_{i},v\rangle v+y$ for some $y\in W$. But since $\langle u_{i},v\rangle=0$, we have $y=u_{i}$ and so $Au_{i}=A'u_{i}=\lambda u_{i}$, which proves $u_{i}$ is an eigenvector for $A$. $\blacksquare$

## Application: Waves

As you can probably tell from the book to this point, my favorite applications of math are to computer science. Linear algebra is no different. However, it would be intellectually dishonest to omit the influence of linear algebra in physics. Nowhere else does the beauty and utility of eigenvalues shine so bright.

![Figure 12.2: A system in which five beads are equidistantly spaced on a taut string fixed to a wall at each end.](07 - Eigenvectors and Eigenvalues_images/img-2.jpeg)

As a demonstration, we consider vibrations (waves) on a string. The analysis we'll perform is a perfect post-hoc motivation for eigenvalues. The string system, with appropriate simplifications, results in a differential equation specified by a symmetric linear map. By the Spectral Theorem, that map has an orthonormal basis of eigenvectors. This allows us to decompose the system into independent components, and results in efficient computation and physical insight. We'll be able to easily compute the long-term behavior of the system—indeed, it will have a formula!—and the eigenvectors will correspond to the "fundamental frequencies" of the vibrating string. In addition to the pictures in this section, there is an interactive demo on the book's website.

The discrete analysis we're about to do also generalizes both in dimension (waves on a surface) and to a continuous setting (the wave equation). While we gave a taste of what linear algebra and eigenvectors look like in infinite dimensions, this application will hopefully motivate further study.

### The Setup

Consider the system depicted in Figure 12.2 in which a string is pulled tight through five equally spaced beads. If you pluck the string, it creates a wave that propagates through the string from end to end.

First, we need to write down a formal mathematical model in which we can describe the motion of a bead. We start by defining a function of time that represents an object's position. Ultimately, we'll only care about the vertical motion of the beads, but a priori we'll need two dimensions to describe the forces involved.

Let $x: \mathbb{R} \to \mathbb{R}^2$ be a function describing the position of an object at a given time $t$. In particular, we choose a reference point in the universe to be $(0, 0)$ and a basis $\{e_1, e_2\}$ of $\mathbb{R}^2$ for measurement. Then the components of $x(t) = (x_1(t), x_2(t))$ represent the position of the object, in $e_1, e_2$ units, respectively, relative to $(0, 0)$. The obvious choices of coordinates are the standard basis vectors $(1,0)$ and $(0,1)$ representing horizontal and vertical, as aligned with the picture.

**Model 12.24.** Let $x(t)=(x_{1}(t),x_{2}(t))$ be the position of an object at time $t$. Then its derivative, $x'(t)=(x'_{1}(t),x'_{2}(t))$, describes the object's velocity at time $t$, and the second derivative $x''(t)=(x''_{1}(t),x''_{2}(t))$ describes its acceleration at time $t$.

These should intuitively make sense when thinking of the derivative as a rate of change. Velocity is the rate of change of position, acceleration the rate of change of velocity. As an aside, this kind of vector-valued function that has a 1-dimensional input and a multi-dimensional output is often called a *parametric function*. We'll cover derivatives in more generality in Chapter 14.

We must also describe a mathematical model for a physical force. Note that while we're doing everything here in two dimensions, the same principles apply to three or more dimensions.

**Definition 12.25.** A *force* is a function $F:\mathbb{R}\to\mathbb{R}^{2}$ whose input represents time and whose output is a vector representing the magnitude and direction of the force. Each force is considered as acting on a specific object.

In the formulas below, we're concerned with the force in a particular direction. Indeed, given a force vector $F(t)$ at a specific time $t$, projecting $F(t)$ onto the appropriate unit vector $v$ gives the component of $F$ in the direction of $v$. If we choose the basis to align with the vertical direction, the projection is trivial: just look at the second entry of the force vector. But in general you can use projections to get the component of a force in any direction.

As part of the mathematical model, forces "act" on objects. By that I mean they are applied to objects and influence their motion. If you pluck a string, it moves. The following revolutionary observation allows us to describe exactly how forces that act on an object influence their motion.

**Model 12.26 (Newton's $n$-th law for some $n$).** If $F_{1},\ldots,F_{n}$ are all of the forces acting on an object with mass $m$ whose position is described by $x(t)$, then

$$\sum_{i=1}^{n}F_{i}(t)=mx''(t)$$

In other words, the sum of the forces applied to an object determines the acceleration of that object. More massive objects need larger forces to move them.

### One Bead

Now let's inspect our beaded string in the special case of a single bead in the middle of a string. The bead has been plucked and released, as in Figure 12.3.

![Figure 12.3: A simpler system that has only one bead, displaced from its equilibrium and released.](07 - Eigenvectors and Eigenvalues_images/img-3.jpeg)

Our goal is to model the dynamics of this system as a linear system. At any given time $t$, we should be able to calculate the acceleration $x''(t)$ of the bead as a linear function of its current position. As we'll see, that's enough to compute the position $x(t)$ at any time. When we extend the model to include all five beads, it will depend linearly on the positions of multiple beads.

We'll make a whole host of unrealistic assumptions to aid us. Let's pretend the string has no mass, the bead has no width, there is no friction or air resistance, and let's do away with gravity. More generously, we assume that all of these values are "negligibly small" compared to the forces we care about. These kinds of simplifying assumptions are the physics analogue of what mathematicians do when they encounter a hard problem: keep stripping out the difficult parts until you can solve it. If you simplify the problem in the right way, you'll be analyzing just the aspects of the problem that you really care about. After solving it, having hopefully gained useful intuition in the process, you can replace each removed bit and use your newfound intuition to find a solution of the harder problem. Or, if you cannot, you can see how the simpler solution breaks with the new assumption, and thus understand why the full problem is hard to solve. This process is by no means as easy as it sounds, but it's a powerful guide.

The above assumptions are minor, but there are two crucial assumptions that we have to discuss in more detail. First, we assume the string is not stretched too far. This allows us to use a Taylor series approximation for the sine and tangent of a small angle. Second, assume the string is already stretched tightly when the beads are plucked. This is what allows us to ignore the horizontal motion of the bead. We'll discuss these in more detail when we employ them.

Once we've eliminated gravity and its cohort, there are only two forces acting on the bead: the force of tension in the string on the left and right sides of the bead. When the bead is pulled downward, the string is stretched, and the bonds between the string's atoms create a force that "pulls" the string back to its normal length. Luckily, tension is well understood. The standard model is Hooke's law.

**Model 12.27 (Hooke's law).** The force of tension in an elastic string that has been stretched from its resting length by a distance $d \geq 0$ is $-Td$, where $T \geq 0$ is a constant depending on the material of the string. This model only applies for a sufficiently small $d$ that does not exceed a limit (which again depends on the material in the string).

If the string is tied to a surface and you pull away from the surface, even at an angle, the force is directed back along the string toward the surface. This gives our bead two forces as in Figure 12.4.

![Figure 12.4: The forces pull in opposite directions toward the walls, and together sum to a vertical force $F_1 + F_2$.](07 - Eigenvectors and Eigenvalues_images/img-4.jpeg)

Since we assumed the bead has no width (or, if you will, the forces act on the center of mass of the bead), the tails of these vectors are the same point, and when we sum them we get the net force pulling the bead upward.

In our system the string is taut, and we'll suppose it's stretched to begin with. Call $2l$ the natural length of the string (so that $l$ is the length of one of the two halves), $T$ the tension constant, and $2l_{\mathrm{init}}$ the length the string is initially pulled to when the system is at rest. In that case, the two forces on the bead have magnitude $T(l_{\mathrm{init}} - l)$ and face in opposite directions. The bead does not move.

<!-- carousel -->
![Figure 12.5: At rest, the two horizontal tension forces $F_1$ and $F_2$ are equal and opposite, so they sum to the zero vector.](07 - Eigenvectors and Eigenvalues_images/img-5.jpeg)
![Figure 12.6: The force $F_1$ pulling the bead rightward when the bead is displaced. The right segment has length $d(t)$, the horizontal gap to the wall is $l_{\mathrm{init}}$, and the bead sits at $(x_1(t), x_2(t))$.](07 - Eigenvectors and Eigenvalues_images/img-6.jpeg)
<!-- endcarousel -->

Let's focus on the right hand side of the bead (the left side is symmetric) in Figure 12.6. Choose the resting point of the bead, when the string is completely straight, to be $(0,0)$. Use the standard basis $\{(1,0),(0,1)\}$ and let $x(t) = (x_{1}(t),x_{2}(t))$ be the displacement of the bead at time $t$. Initially at time zero $x_{1}(t) = 0$ and $x_{2}(t) < 0$. Call $d(t)$ the length of the right string segment at time $t$, and $F_{1}(t)$ the force pulling on the bead by the string. The diagram in Figure 12.6 labels these values.

Now we compute. Our choice of basis and the Pythagorean theorem give $d(t) = \sqrt{l_{\mathrm{init}}^2 + x_2(t)^2}$. We construct $F_{1}(t)$ first by finding a unit vector in the correct direction, then scaling it so its length is the magnitude of the force. That magnitude is $T(d(t) - l)$, according to Hooke's law. The force vector starts at $x(t)$ and points toward $(l_{\mathrm{init}}, 0)$, so we can take $(l_{\mathrm{init}}, 0) - x(t) = (l_{\mathrm{init}}, -x_2(t))$ and normalize it by dividing by $d(t)$. So far we have

$$F_{1}(t)=T(d(t)-l)\frac{(l_{\text{init}},-x_{2}(t))}{d(t)}$$

The magnitude of the vector has a nonlinear part $d(t)-l$ involving $d(t)$, so let's simplify that first. Since the string was initially stretched to length $l_{\text{init}}$, we have $d(t)-l=(d(t)-l_{\text{init}})+(l_{\text{init}}-l)$, and so the magnitude of the force is

$$\|F_{1}(t)\|=T(d(t)-l_{\text{init}})+T(l_{\text{init}}-l).$$

The right hand term is the (constant) magnitude of tension when the system is at rest. For the left hand term, we can use a Taylor series approximation. First we do some simplification.

$$
\begin{aligned}
d(t) &=\sqrt{l_{\text{init}}^{2}+x_{2}(t)^{2}} \\
&=l_{\text{init}}\sqrt{1+\left(\frac{x_{2}(t)}{l_{\text{init}}}\right)^{2}}
\end{aligned}
$$

Next we compute the Taylor series for $\sqrt{1+z^{2}}$, substituting $z=x_{2}(t)/l_{\text{init}}$ at the end. Indeed, the Taylor series is

$$\sqrt{1+z^{2}}=1+\frac{z^{2}}{2}-\frac{z^{4}}{8}+\frac{z^{6}}{16}-\cdots$$

Using the first two terms to approximate, we get $d(t)\approx l_{\text{init}}\left(1+\frac{x_{2}(t)^{2}}{2l_{\text{init}}^{2}}\right)$. If we wanted to be more rigorous, we could hide the lower order terms in a big-O notation, but we'll save that for Chapter 15.

Returning to the force of tension, minor algebra gives $T(d(t)-l_{\text{init}})=T\frac{x_{2}(t)^{2}}{2l_{\text{init}}}$. In other words the magnitude of the force of tension in the string is the initial tension, plus a small factor proportional to the square of the deviation.

$$T\frac{x_{2}(t)^{2}}{2l_{\text{init}}}+T(l_{\text{init}}-l)$$

The formula above is why we can assume, as most physics texts do without nearly as much fuss as we have displayed here, that the magnitude of tension in the string is constant. This Taylor series approximation is the first assumption showing up in the math: if the initial deviation $x_{2}(t)$ is small, say much less than 1 unit of measurement, then $x_{2}(t)^{2}$ is even smaller and can be ignored, as can all higher powers of $x_{2}(t)$. Our computation shows that the first power $x_{2}(t)$ does not show up anywhere in the Taylor series, so if we're committed to simplifying everything to be linear, the Taylor series assures us we're not accidentally ignoring terms we want to preserve.

I personally feel it's important to see how the math justifies the assumptions rather than relying entirely on "physical intuition." Once you state which forces you want to consider—and once you've formalized the mathematical rules governing those forces—the mathematics should stand on its own. In particular, many physics books say that the constant tension assumption rests on the fact that the bead is not displaced very far from rest. Strictly speaking, this is not enough information. What also matters is the relationship between the displacement of the bead and the initial stretch that holds the string taut at rest. The former must contribute an order of magnitude smaller force than the latter to be negligible. The Taylor series revealed this nuance, and further allows us to measure how big a displacement is too big to ignore.

We continue with the assumption, then, that the magnitude of the force of tension in the string is constant over the entire evolution of the system. From this point on we'll use $T$ in place of $T(l_{\text{init}}-l)$ to simplify the formulas (it's all just a constant anyway). Recalling that we formed the unit vector by scaling by $d(t)$, the force on the right string is the vector

$$F_{1}(t)=T\frac{(l_{\text{init}},-x_{2}(t))}{d(t)}$$

Note that while we ignored the $x_{2}(t)^{2}$ factor in the magnitude, we haven't yet ignored its contribution to the scaling of the unit vector. That begins now. Since the two forces $F_{1}(t)$ and $F_{2}(t)$ are symmetric, we only need the component of $F_{1}(t)$ in the vertical direction. We project $F_{1}(t)$ onto the vector $(0,1)$, i.e., isolate the second entry of the vector.

$$F_{\text{vert}}(t)=T(0,-x_{2}(t)/d(t))$$

And if we expand $d(t)=\sqrt{l_{\text{init}}^{2}+x_{2}(t)^{2}}$ and use the same Taylor series argument to justify setting $x_{2}(t)^{2}$ to zero, we get $F_{\text{vert}}(t)=(0,-Tx_{2}(t)/l_{\text{init}})$.

Now that all our forces are vertical, we can just work with the 1-dimensional picture and see that the sum of the forces on the bead in the vertical direction is $F(t)=-2Tx_{2}(t)/l_{\text{init}}$. By Newton's law, this dictates the acceleration of the bead, giving

$$mx_{2}''(t)=-2Tx_{2}(t)/l_{\text{init}}.$$

Let's simplify the numbers by setting $m=1$ and $l_{\text{init}}=1$, a trick called "choosing units cleverly." Then the formula is $x_{2}''(t)=-2Tx_{2}(t)$. The finish line is in sight. We need one additional theorem whose proof is left as an investigative exercise. First recall, or learn now, that the derivative of $\sin(x)$ is $\cos(x)$, and the derivative of $\cos(x)$ is $-\sin(x)$, so that the second derivative of $\sin(x)$ is $-\sin(x)$.

**Theorem 12.28.** Let $f:\mathbb{R}\to\mathbb{R}$ be a twice differentiable function which satisfies $f''(x)=-f(x)$, and $f(0)=0,f'(0)=1$. Then $f(x)=\sin(x)$.

An equation like $f''=-f$, involving the derivatives of an unknown function, is called a *differential equation*. There is an analogous theorem for the cosine instead using $f(0)=1,f'(0)=0$. The restrictions on $f(0)$ and $f'(0)$ are called *initial conditions*, and as they change the solution changes. In the case of Theorem 12.28 the solution only changes by constants. In fact, the way these values vary hints at two independent dimensions which provide solutions to $f''=-f$.

Indeed, the set of solutions to $f''=-f$ forms a two-dimensional vector space (a subspace of the space of all twice-differentiable functions $\mathbb{R}\to\mathbb{R}$), and $\sin(x)$ and $\cos(x)$ form a basis. As an aside, if we call this vector space $U$, then the "take a second derivative" function $d:U\to U$ mapping $f\mapsto f''$ is a linear map on $U$, and the sine and cosine functions are eigenvectors with eigenvalue $-1$. This hints at the deep truth that sine and cosine are special, in part explaining why we expect Theorem 12.28 to be true.

Despite how the initial conditions may vary, the solution is a linear combination $c_{1}\sin(x)+c_{2}\cos(x)$. With a bit of algebra, given the initial conditions you can solve for those coefficients. We will do this below.

First, we have to wrangle the extra coefficient of $2T$. We can modify the theorem slightly. Note that for a scalar $a$, the derivative of $\sin(ax)$ is $a\cos(ax)$ (the chain rule, Theorem 8.10), but since we're differentiating twice we have a square in the second derivative $-a^{2}\sin(ax)$. I.e., the solution to $x_{2}''(t)=-2Tx_{2}(t)$ is a sine or cosine with argument $(\sqrt{2T})t$. Let $\omega$ (the Greek letter omega) be $\sqrt{2T}$.

Combining this with the assumption that at time $t=0$ the bead is displaced by some fixed amount and let go (has zero initial velocity), we get

$$
\begin{aligned}
x_{2}(0) &=c_{1}\sin(\omega\cdot 0)+c_{2}\cos(\omega\cdot 0)=c_{1}\cdot 0+c_{2}\cdot 1 \\
0 &=x_{2}'(0)=c_{1}\omega\cos(\omega\cdot 0)-c_{2}\omega\sin(\omega\cdot 0)=c_{1}\omega\cdot 1-c_{2}\omega\cdot 0
\end{aligned}
$$

We can read off the solution as $c_{1}=0,c_{2}=x_{2}(0)$. This means that our lonely bead, plucked and left to wait all this time to learn its destiny, finally has an equation for its motion: $x_{2}(t)=x_{2}(0)\cos(t\sqrt{2T})$. It's a smooth cosine with a constant frequency determined by the tension in the string. This is exactly what we expect from a single bead.

### Multiple Beads

Now we graduate to multiple beads, shown in Figure 12.7.

![Figure 12.7: Five beads starting from arbitrary initial vertical positions $y_1, \ldots, y_5$, fixed to a wall at each end.](07 - Eigenvectors and Eigenvalues_images/img-7.jpeg)

Horizontal forces are a new concern. We want to retain our assumption of constant tension in the string. But because the angles are different on different sides of a bead, the fraction of that constant tension pulling the bead left and right can be different, resulting in horizontal motion. We know that the tension in the string will eventually pull the bead back to the center, but we want to feel secure that these violations of our assumptions are minor enough that we can justify ignoring them. We leave it as an exercise to the reader to adapt the setup for a single bead to this scenario, and to use Taylor series approximations to find the conditions under which horizontal motion can be ignored.

![Figure 12.8: A close up of $b_2$. The vertical gaps to its neighbors are $y_2 - y_1$ and $y_3 - y_2$, and $\theta_1, \theta_2$ are the angles each string segment makes with the horizontal.](07 - Eigenvectors and Eigenvalues_images/img-8.jpeg)

Since we are ignoring horizontal motion, we'll simplify the notation so that the forces, displacements, velocities, and accelerations are 1-dimensional vectors, i.e., scalars representing vectors pointing in the vertical direction. Let $b_{1}, \ldots, b_{5}$ be the beads of mass $m_{i}$, and let $y_{i}$ be the displacement of $b_{i}$, with $y_{i}'$ and $y_{i}''$ the velocity and acceleration, as before. The natural resting point of the beads is zero. If we just think about position—and as we saw this completely determines the forces and the acceleration—then the state of this system is a vector $y = (y_{1}, y_{2}, y_{3}, y_{4}, y_{5}) \in \mathbb{R}^{5}$. The forces we're about to compute will form a linear map $A$ mapping $y \mapsto y''$.

Let's now focus on bead $b_{2}$ as a generic example, shown in Figure 12.8. In the figure, the vertical gap between $b_{1}$ and $b_{2}$ is $y_{2} - y_{1}$, and the angle $\theta_{1}$ is the angle between the string and the horizontal. Likewise for the corresponding data on the right hand side of the bead. The tension is a constant $T$. The projected tension in the vertical direction is $-T\sin(\theta_{1})+T\sin(\theta_{2})$, with the sign flip because the left side pulls the bead down.

Now we'll use two Taylor series approximations:

$$
\begin{aligned}
\sin(\theta) &=\theta-\frac{\theta^{3}}{3!}+\frac{\theta^{5}}{5!}-\cdots \\
\tan(\theta) &=\theta+\frac{\theta^{3}}{3}+\frac{2\theta^{5}}{15}+\cdots
\end{aligned}
$$

Because the first terms are equal, and for $\theta$ small enough to ignore $\theta^{3}$ and higher, we can replace $\sin(\theta)$ with $\tan(\theta)$ wherever it occurs. This is the same reasoning as before, because we want to extract the linear aspects of the model. The force on bead $b_{2}$ is

$$
\begin{aligned}
y_{2}''m_{2} &=F_{2}(t) \\
&=-T\sin(\theta_{1})+T\sin(\theta_{2}) \\
&=-T\tan(\theta_{1})+T\tan(\theta_{2}) \\
&=-T\frac{y_{2}-y_{1}}{l_{\text{init}}}+T\frac{y_{3}-y_{2}}{l_{\text{init}}}
\end{aligned}
$$

And rearranging gives

$$\frac{m_{2}l_{\text{init}}}{T}y_{2}''=y_{1}-2y_{2}+y_{3}$$

Simplify the equation by setting $m_{2}=l_{\text{init}}=T=1$. The forces for the other beads are analogous, with the beads on the end having slightly different formulas as they're attached to the wall on one side. As a whole, the equations are

$$
\begin{aligned}
y_{1}'' &=-2y_{1}+y_{2} \\
y_{2}'' &=y_{1}-2y_{2}+y_{3} \\
y_{3}'' &=y_{2}-2y_{3}+y_{4} \\
y_{4}'' &=y_{3}-2y_{4}+y_{5} \\
y_{5}'' &=y_{4}-2y_{5}
\end{aligned}
$$

Rewrite this as a linear map $y''=Ay$ with

$$A=\begin{pmatrix}-2&1&0&0&0\\1&-2&1&0&0\\0&1&-2&1&0\\0&0&1&-2&1\\0&0&0&1&-2\end{pmatrix}$$

At last, we turn to eigenvalues. This matrix is symmetric and real valued, and so by Theorem 12.22 it has an orthonormal basis of eigenvectors which $A$ is diagonal with respect to. Let's compute them for this matrix using the Python scientific computing library numpy. Along with Fortran eigenvector computations, numpy wraps fast vector operations for Python.

After defining a helper function that shifts a list to the right or left, we define a function that constructs the bead matrix, foreseeing our eventual desire to increase the number of beads. We then invoke a numpy routine to compute the eigenvalues and eigenvectors and sort the eigenvectors in order of decreasing eigenvalue. The whole pipeline reproduces Kun's Figure 12.9 table exactly (to two decimals).

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/06_bead_eigensystem.py -->
```

Plotting with five beads gives the plot in Figure 12.9. In case it's hard to see (there's a clearer, more obvious diagram at the end of the section), let's inspect it in detail. The top eigenvalue, $\lambda=-0.267\ldots$, corresponds to the eigenvector in the chart with circular markers. The eigenvector entry starts at $0.29$, increases gradually to $0.58$, and then back down to $0.29$, a sort of quarter-period of a full sine curve. The second largest eigenvalue, $\lambda=-1$ with triangular markers, has an eigenvector starting at $-0.5$ and increasing up to $0.5$, performing a half-period of sorts. The next eigenvector for $\lambda=-2$ performs a single full period, and so on. (Eigenvectors are only determined up to sign, so a solver may hand you $v$ or $-v$; the *shape* of each mode is what matters, and that is invariant.)

The rounded entries of the eigenvectors of the 5-bead system are tabulated below; each row pairs an eigenvalue $\lambda$ with its eigenvector $(y_1, \ldots, y_5)$.

| Eigenvalue $\lambda$ | $y_1$ | $y_2$ | $y_3$ | $y_4$ | $y_5$ |
| --- | --- | --- | --- | --- | --- |
| $-0.27$ | $0.29$ | $0.50$ | $0.58$ | $0.50$ | $0.29$ |
| $-1.00$ | $-0.50$ | $-0.50$ | $-0.00$ | $0.50$ | $0.50$ |
| $-2.00$ | $0.58$ | $-0.00$ | $-0.58$ | $0.00$ | $0.58$ |
| $-3.00$ | $-0.50$ | $0.50$ | $-0.00$ | $-0.50$ | $0.50$ |
| $-3.73$ | $-0.29$ | $0.50$ | $-0.58$ | $0.50$ | $-0.29$ |

![Figure 12.9: Plots of the five eigenvectors of the 5-bead system. The $x$-axis is the bead index and the $y$-axis is the eigenvector entry; smaller (more negative) $\lambda$ corresponds to a higher-frequency wave.](07 - Eigenvectors and Eigenvalues_images/img-9.jpeg)

Now this is something to behold! The eigenvectors have a structure that mirrors the waves in the vibrating string, and as the corresponding eigenvalue decreases, the "frequency" of the wave plotted by the eigenvector increases. That is, the wave exhibits faster oscillations.

This wave is not a metaphor. If you simulate the beaded string with initial position set to one of these eigenvectors, you'd see a *standing wave* whose shape is exactly the plot of that eigenvector. In fact, I implemented a demo of this in Javascript, which you can explore for yourself at pimbook.org. The demo is a first-principles simulation of the system, so horizontal forces are not ignored, nor are Taylor series approximations used. Because of this, if you set the initial positions of the beads to be quite large, you'll see irregularities caused by horizontal motion. These are highlighted by how the demo draws the force vector acting on each bead at every instant. It's fun to watch, and it provides a hint as to what assumption allows one to ignore horizontal motion. Indeed, if you set the position to the top eigenvector $100v_{1}$ (scaled to account for the units being pixels), you can see the same shape as $v_{1}$ in the plot above. If you scale it even larger, you can see the horizontal forces come into play. For example, try setting the initial positions to $300v_{1} = (87, 150, 174, 150, 87)$.

Let's witness how the formulas work out for the first eigenvector $v_{1}$, when the positions start as that eigenvector $y = v_{1} \approx (0.29, 0.5, 0.58, 0.5, 0.29)$. In that case each bead's trajectory can be computed independently according to $y''=Ay=-0.27y$. So the second bead, say, evolves as $y_2''=-0.27y_2$ with initial position $y_{2}=0.5$. This is identical to the single-bead system we solved earlier, and the result is a simple cosine wave with a fixed period and amplitude. The same holds for each bead. The beads in the middle have longer periods and higher amplitudes, as expected.

We have the tools to understand this eigenvector phenomenon beyond concrete computations. As we saw, the eigenvectors of the bead system form an orthonormal basis. The basis vectors are the independent components of the joint forces acting on all the beads. What's more, the proof of the Spectral Theorem explains why the eigenvectors have a natural ordering. The way we choose an eigenvector at each step is, according to Lemma 12.8, by maximizing $\|Av\|$ over unit vectors $v$. In the proof of the Spectral Theorem we then removed that vector, and its span, from consideration for the next vector. So the largest magnitude eigenvalue (in this case the most negative one) is the first one extracted, and that corresponds to the highest frequency. The next eigenvector chosen corresponds to the second largest magnitude eigenvalue, and so on, each having a smaller frequency than the last.

But wait, there's more! Because it's an orthonormal basis of eigenvectors, we can express any evolution of this system in terms of the eigenvectors, and do it as simply as taking inner products.

Take, for example, the complex evolution that occurs when you pluck the second bead. Say $y(0)=(0,0.5,0,0,0)$. The individual beads don't evolve according to a single cosine wave. They jostle in a more haphazard manner. Nevertheless, we can express their trajectory as a sum of five simple cosine waves, one for each eigenvector. The decomposition uses the simple formula from Proposition 12.15: the coefficient on $v_i$ is the inner product $\langle y, v_i \rangle$.

The following demo carries the whole story to its conclusion. It decomposes the plucked state $y(0)$ into the eigenbasis, evolves each coefficient independently as a cosine $z_i(t) = z_i(0)\cos(\sqrt{-\lambda_i}\, t)$ (the eigenvalues are negative, hence the minus under the root), reassembles $y(t)$ in the bead basis, and cross-checks the closed-form trajectory against a direct numerical integration of the coupled system $y'' = Ay$. They agree to nine decimal places.

```python
<!-- include: code/pim/07 - Eigenvectors and Eigenvalues/07_decouple_evolution.py -->
```

So, up to the overall sign on each eigenvector (the solver's choice), $y(0)=0.25v_{1}-0.25v_{2}+0v_{3}+0.25v_{4}+0.25v_{5}$, and we can compute this sum and pick out any coordinate we want to get the initial position of a particular bead.

Now, in the basis of eigenvectors, we define a new set of variables $z(t)=(z_{1}(t),\ldots,z_{5}(t))$. Let $z_{i}(t)$ be the coefficient of $v_{i}$ for the representation of $y(t)$ in the basis of eigenvectors. In words, before we were tracking the position of the beads as they evolve over time, and now we're tracking the coefficients of the eigenvectors as they evolve over time. This is the whole point of the change of basis. In this new representation the differential equation changes to

$$y''=Ay\Longrightarrow z''=Dz$$

where $D$ is the diagonal matrix of eigenvalues $\lambda_{1},\ldots,\lambda_{n}$ (in any order we please, let's say in decreasing order). Then each coordinate is just like our single-bead case. For example $z_{1}''=\lambda_{1}z_{1}$, along with an initial condition $z_{1}(0)=0.25$ (as per the decomposition of $y(0)$ above).

We can solve each of these differential equations separately, just as we solved the single-bead equation, and then combine them by converting back to the standard basis of bead positions. The result will give us the trajectory of each bead expressed as a sum of simple cosine waves.

The equations, with initial conditions placed adjacent, are (with some rounding to simplify):

$$
\begin{aligned}
z_{1}''&=-0.27z_{1}; &z_{1}(0)&=0.25, &z_{1}'(0)&=0 \\
z_{2}''&=-z_{2}; &z_{2}(0)&=-0.25, &z_{2}'(0)&=0 \\
z_{3}''&=-2z_{3}; &z_{3}(0)&=0, &z_{3}'(0)&=0 \\
z_{4}''&=-3z_{4}; &z_{4}(0)&=0.25, &z_{4}'(0)&=0 \\
z_{5}''&=-3.73z_{5}; &z_{5}(0)&=0.25, &z_{5}'(0)&=0
\end{aligned}
$$

And the solutions are

$$
\begin{aligned}
z_{1}(t) &=0.25\cos(0.52t) \\
z_{2}(t) &=-0.25\cos(t) \\
z_{3}(t) &=0 \\
z_{4}(t) &=0.25\cos(1.73t) \\
z_{5}(t) &=0.25\cos(1.93t)
\end{aligned}
$$

Converting back to the bead-position basis, we get

$$y(t)=0.25\cos(0.52t)v_{1}-0.25\cos(t)v_{2}+0.25\cos(1.73t)v_{4}+0.25\cos(1.93t)v_{5}$$

Which expanded out coordinate-wise (and again rounded) is

$$
\begin{aligned}
y_{1}(t) &=0.07\cos(0.52t)+0.125\cos(t)-0.125\cos(1.73t)-0.07\cos(1.93t) \\
y_{2}(t) &=0.125\cos(0.52t)+0.125\cos(t)+0.125\cos(1.73t)+0.125\cos(1.93t) \\
y_{3}(t) &=0.145\cos(0.52t)-0.145\cos(1.93t) \\
y_{4}(t) &=0.125\cos(0.52t)-0.125\cos(t)-0.125\cos(1.73t)-0.125\cos(1.93t) \\
y_{5}(t) &=0.07\cos(0.52t)-0.125\cos(t)+0.125\cos(1.73t)-0.07\cos(1.93t)
\end{aligned}
$$

Fantastic! We started with a tightly coupled system, in which the position and motion of the different beads seem to depend heavily on each other. They do, it's true, but this eigensystem provides a perspective in which their motions can be computed independently! You don't have to know where bead 3 is to compute the future position of bead 2. That's the promise fulfilled by eigenvectors.

Finally, as you may have guessed from the arbitrary choice of five beads, we can generalize this system to any number of beads. If we take even just a hundred beads, and plot the eigenvectors for the top few eigenvalues as we did above, we see smoother, more obvious waves. Figure 12.10 shows this. With such natural shapes of increasing complexity, it makes sense to give a name to these eigenvectors. They're called the *fundamental modes* of the system, and the frequencies of the "sinusoidal curve" of each eigenvector are called the *resonant frequencies* of the system.

![Figure 12.10: The plot of the top five eigenvectors for a hundred-bead system. The discrete modes now trace out clean sine curves of increasing frequency.](07 - Eigenvectors and Eigenvalues_images/img-10.jpeg)

If one decreases the distance between beads and increases the number of beads in the limit, the result is the *wave equation*. This is a differential equation (in both time and position along the string) that one can use to track the motion of a traveling wave through a string. See the exercises for more on that. But more importantly for us, the vector space for that continuous model has infinite dimension, it still has a basis of eigenvectors, and they correspond to proper sine curves instead of discrete approximations. In this case, since the "zero-width" beads are now at every position of the string, you can think of them as cross sections of molecules that make up the string itself, with atomic forces playing the role of Hooke's law. These eigenvectors then describe the intrinsic properties of the string itself.

So there you have it. Eigenvectors have revealed the secrets of waves on a string.

## Cultural Review

1. Eigenvalues and eigenvectors often provide the best perspective (basis) with which to study a linear map.
2. An orthonormal basis of eigenvectors allows you to decouple aspects of a complex system that are a priori intertwined, and orthonormality makes computing basis decompositions easy.
3. Invariance is a strong "smell," meaning objects which satisfy an invariance property are probably important, even if you don't know why exactly. In this chapter, it was an eigenvalue being invariant to the choice of basis, and eigenvectors of $f$ being invariant (up to scaling) under the operation of applying $f$.
4. When trying to solve a complicated problem, a good approach is to simplify the problem as much as possible without losing the essential character of the problem. One can then solve that simplified problem and gain insight. Then gradually add complexity back to the problem and, using the new insights, attempt to solve the harder problem.

## Exercises

### Matrix and Inner Product Fundamentals

**12.1.** For two matrices $A,B$ of compatible dimensions, prove that $(AB)^{T}=B^{T}A^{T}$.

**12.2.** Let $V$ be an $n$-dimensional inner product space, whose norm $\|x\|^{2}=\langle x,x\rangle$ is given by the inner product. Prove the following.

1. The only vector with norm zero is the zero vector.
2. The distance function $d(x,y)=\|x-y\|$ is nonnegative and symmetric.
3. The distance function satisfies the triangle inequality. That is, $d(x,z)\leq d(x,y)+d(y,z)$ for all $x,y,z\in V$.

**12.3.** Prove that a linear map $f:\mathbb{R}^{n}\to\mathbb{R}^{n}$ preserves the standard inner product—i.e. $\langle x,y\rangle=\langle f(x),f(y)\rangle$ for all $x,y$—if and only if its matrix representation $A$ has orthonormal columns with respect to the standard basis. Hint: use the fact that $\langle x,y\rangle=x^{T}y$.

**12.4.** Let $A$ be a square matrix with an inverse. Using only the fact that $(BC)^{T}=C^{T}B^{T}$ for two square matrices $B,C$, prove that $(A^{T})^{-1}=(A^{-1})^{T}$.

**12.5.** Prove the following basic facts about eigenvalues, eigenvectors, and inner products.

1. Fix a vector $y$ and let $f_{y}(x)=\langle x,y\rangle$. Prove that if $x$ is restricted to be a unit vector, then $f_{y}(x)$ is maximized when $x=y/\|y\|$.
2. Let $V,W$ be two $n$-dimensional inner product spaces with inner products $\langle-,-\rangle_{V}$ and $\langle-,-\rangle_{W}$. Define a bijective linear map $f:V\to W$ that is an isomorphism of vector spaces and also satisfies $\langle x,y\rangle_{V}=\langle f(x),f(y)\rangle_{W}$ for all $x,y\in V$. Such a map is called an *isometry*. Hint: start by using Gram-Schmidt to choose an orthonormal basis of each vector space.
3. Fix the inner product space $\mathbb{R}^{n}$ with the standard inner product. Let $A:\mathbb{R}^{n}\to\mathbb{R}^{n}$ be a change of basis matrix. Find an example of $A$ for which $\langle x,y\rangle\neq\langle Ax,Ay\rangle$. In other words, an arbitrary change of basis does not preserve the formula for the standard inner product. As we saw in the chapter, only an orthonormal change of basis does this. Determine a formula (that depends on the data of $A$) that shows how to convert inner product calculations in one basis to inner product calculations in another.

### Differential Equations, Graphs, and Eigenvalues

**12.6.** Look up a proof of Theorem 12.28, on the uniqueness of the sine function, that uses Taylor series. The analytical tool required to understand the standard proof is the concept of *absolute convergence*. The central difficulty is that if you're defining a function by an infinite series, you have to make sure that series converges with the properties needed to make it a valid Taylor series. Repeat the proof for $\sin(ax)$.

**12.7.** In Definition 12.3 we defined the adjacency matrix $A(G)$ of a graph $G = (V, E)$. This matrix corresponds to some linear map $f: \mathbb{R}^n \to \mathbb{R}^n$, where $n = |V|$. How would you interpret this vector space in terms of $V$? What is a natural description of the basis of $\mathbb{R}^n$ that we're using to represent $A(G)$? What is a natural (English) description of the linear map $f$, if you restrict to input vectors whose entries are either 0 or 1? If this is hard to formulate abstractly, write down an example graph on 5 vertices. What happens to your description of $f$ when you allow for non-binary inputs?

**12.8.** Prove that a connected graph $G$ is bipartite if and only if it contains no cycles of odd length. Write a program to find cycles of odd length, and hence to decide whether a given graph is bipartite.

**12.9.** Implement the algorithm presented in the chapter to generate a random graph on $n$ vertices with edge probability $1/2$, and a planted clique of size $k$. For the rest of this exercise fix $k = \lceil \sqrt{n \log n} \rceil$. Determine the average degree of a vertex that is in the plant, and the average degree of a vertex that is not in the plant, and use that to determine a rule for deciding if a vertex is in the clique. Implement this rule for finding planted cliques of size at least $\sqrt{n \log n}$ with high probability, where $n = 1000$.

**12.10.** As in the previous problem, implement the algorithm in this chapter for finding planted cliques of size $k = \lceil 10\sqrt{n} \rceil$ in random graphs with $n = 1000$. Use a library such as numpy to compute eigenvalues and eigenvectors for you.

**12.11.** The *minimal polynomial* of a linear map $f: V \to V$ is the monic polynomial $p$ of smallest degree such that $p(f) = 0$. Since the space of all linear maps $V \to V$ is a vector space, we can interpret a "power" $f^k$ as the composition of $f$ with itself $k$ times. Likewise, $cf$ is the map $x \mapsto cf(x)$. So $p(f)$ is a linear map $V \to V$, and by $p(f) = 0$ we mean that $p(f)$ is the zero map. Look up a proof that $\lambda$ is a root of $p$ if and only if $\lambda$ is an eigenvalue of $f$.

**12.12.** We proved that symmetric matrices have a full set of eigenvectors and eigenvalues. In this exercise we will see that to understand eigenvalues of non-symmetric matrices, we must necessarily prove the Fundamental Theorem of Algebra, which we remarked in Exercise 2.15 is quite hard. First prove that $r$ is a root of the polynomial $p(x) = x^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0$ if and only if $r$ is an eigenvalue of the matrix

$$
A_{p} = \begin{pmatrix} 0 & 1 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 1 & 0 \\ 0 & 0 & 0 & \dots & 0 & 1 \\ -a_{0} & -a_{1} & -a_{2} & \dots & -a_{n-2} & -a_{n-1} \end{pmatrix}
$$

Notice that this matrix is not symmetric. Because the roots of a polynomial might be complex numbers, this implies the eigenvalues of a matrix (when viewed as a linear map on a vector space of complex numbers) might also be complex. Walk away from this exercise with a new appreciation for the convenience of symmetric matrices, and the inherent difficulty of writing a generic eigenvalue solver.

### Algorithms and Applications

**12.13.** Implement the Gram-Schmidt algorithm using the following method for finding vectors not in the span of a partial basis: choose a vector with random entries between zero and one, repeating until you find one that works. How often does it happen that you have to repeat? Can you give an explanation for this?

**12.14.** Look up the derivation of the wave equation from Hooke's law for a beaded string (or equivalently, beads on springs) as the distance between adjacent beads tends to zero.

**12.15.** Look up a proof that the singular values of a non-square real matrix $A$ are the square roots of the eigenvalues of the matrix $A^{T}A$. Use this to understand why we computed $A^{T}A$ in the SVD algorithm from Chapter 10.

**12.16.** Generate a "random" symmetric $2000\times 2000$ matrix via the following scheme: pick a distribution (say, normal with a given mean and variance), and let the $i,j$ entry with $i\geq j$ be an independent draw from this distribution. Let the remaining $i<j$ entries be the symmetric mirror. Compute the eigenvalues of this matrix (which are all real) and plot them in a histogram. What does the result look like? How does this shape depend on the parameters of the distribution? On the choice of distribution?

**12.17.** At the end of the chapter we converted the eigenvector-coefficient solution to $z''=Dz$ back to the bead basis by hand. Write a program that, given the initial position of the beads, sets up the independent differential equations in the eigenvector basis, solves those equations, and converts them back to the bead position basis.

**12.18.** Using Taylor series, find appropriate conditions under which horizontal motion in the 5-bead system can be ignored.

**12.19.** Generalize our one-dimensional bead system to a two-dimensional lattice. That is, fix $n$ and put a bead at each $(i,j)\in\{1,2,\ldots,n\}^{2}$, with strings connecting adjacent beads, with fixed walls on each boundary side. Pluck the beads perpendicularly to the lattice. Can you design a symmetric linear model for this system? If so, what do the eigenvectors look like? If not, what step of the modeling process breaks? What is the fundamental obstacle?

**12.20.** Consider a one-dimensional "bead system" where instead of the beads physically moving, they are given some initial heat. Adjacent beads transfer heat between them according to a discrete version of the so-called *heat equation*. Find an exposition of the discrete heat equation online that allows you to set up a linear system and solve it for 10 beads. What do the eigenvalues of this system look like?

**12.21.** PageRank is a ranking algorithm that was a major factor in the Google search engine's domination of the early internet search market. The algorithm involves setting up a linear system based on links between webpages, and computing the eigenvector for the largest eigenvalue. Find an exposition of this algorithm and implement it in code. Can you visualize or interpret the eigenvector in a meaningful way?

## Chapter Notes

### Transposes and Linear Maps

If $f:V\to W$ is a linear map, and $A$ is a matrix representation of $f$, how does $A^{T}$, the operation of transposing the matrix, correspond to an operation on $f$? The answer requires some groundwork.

A *linear functional* on a vector space with scalars in $\mathbb{R}$ is a linear map $V\to\mathbb{R}$. That is, it linearly maps vectors to scalars. This is the origin of the name of the subfield of mathematics called "functional analysis," which studies these mappings as a way to study the structure of the (usually infinite dimensional) vector space. We'll stick to finite dimensions. Fix a vector space $V$ over $\mathbb{R}$. The set of all linear functionals on $V$ forms a vector space (using the same point-wise addition and scalar multiplication we saw for $L^{2}$). This vector space is called the *dual vector space* of $V$, and I'll denote it by $V^{*}$.

The standard basis $\{e_{1},\ldots,e_{n}\}$ for $\mathbb{R}^{n}$ corresponds to a standard dual basis for the dual space, which we'll denote $\{e_{1}^{*},\ldots,e_{n}^{*}\}$. Each $e_{i}^{*}$ is the projection onto the $i$-th coordinate (in the standard basis), i.e. $e_{i}^{*}(a_{1},\ldots,a_{n})=a_{i}$. The mapping $e_{i}\mapsto e_{i}^{*}$ is injective, and in fact every linear functional can be expressed as a linear combination of these dual basis vectors $e_{i}^{*}$. Hence, $\mathbb{R}^{n}$ is isomorphic to its dual. In particular, they have the same dimension.

This construction works without need for an inner product, but if you have an inner product, you get an obvious way to take a general basis $\{v_{1},\ldots,v_{n}\}$ of $V$ to a dual basis of $V^{*}$ by mapping $v$ to the function $x\mapsto\langle v,x\rangle$. If the $\{v_{i}\}$ were an orthonormal basis, this would be the same "coordinate picking" function as we did for the standard basis, due to Proposition 12.15.

Moreover, every linear functional on $\mathbb{R}^{n}$ can be expressed as the inner product with a single vector (not necessarily a basis vector). Expressed in terms of matrices, the linear functional can be written as a $(1\times n)$-matrix—since it is a linear map from an $n$-dimensional vector space to a $1$-dimensional space. Say we call it $f_{v}(x)=\langle v,x\rangle$. If you start from the perspective that all vectors are columns, then the matrix representation of $f_{v}$ is $v^{T}$, and the "matrix multiplication" $v^{T}x$ is a scalar (and also another way to write the inner product, as we saw in this chapter).

Now we finally get to the transpose, which just extends this linear functional picture to a finite number of independent functionals, the outputs of which are grouped together in a vector. Let $f:V\to W$ be a linear map with matrix representation $A$, an $(m\times n)$-matrix for $n$-dimensional $V$ and $m$-dimensional $W$. Define the *transpose* of $f$ (sometimes called the *adjoint*) as the linear map $f^{T}:W^{*}\to V^{*}$ which takes as input (a linear functional!) $g\in W^{*}$ and produces as output the linear functional $g\circ f\in V^{*}$, the composition of the two maps by first applying $f$ and then applying $g$. And indeed, the matrix representation of $f^{T}$ with respect to the dual bases for $V^{*},W^{*}$ is $A^{T}$.

Since $W^{*}$ and $W$ are isomorphic, and $V^{*}$ and $V$ are isomorphic, you may wonder if you can apply this to realize the dual $f^{T}$ as a map $W\to V$ as well. Indeed you can, and it can even be defined without referring to dual vector spaces at all. Let $V,W$ be inner product spaces and $f:V\to W$ a linear map. Define the transpose $f^{T}:W\to V$ input-by-input as follows. Let $w\in W$, and define $f^{T}(w)$ to be the unique vector for which $\langle f(v),w\rangle=\langle v,f^{T}(w)\rangle$. One needs to prove this is well-defined, but it is. It comes from our discussion about symmetry in the "Limiting the Scope: Symmetric Matrices" section about how in $\mathbb{R}^{n}$ you get $\langle Ax,y\rangle=x^{T}A^{T}y$.

Note that these two definitions of the transpose can only be said to be the same in the case that the vector space has scalars in $\mathbb{R}$. If you allow for complex number scalars, things get a bit trickier.

### Jordan Canonical Form

In addition to the geometric multiplicity of an eigenvalue, there's another, more subtle kind of multiplicity called *algebraic multiplicity*. The most common definition uses the definition of the determinant of a matrix (as a polynomial), but a nice alternative way to define it is as follows.

**Definition 12.29.** The *algebraic multiplicity* of an eigenvalue $\lambda$ for $f$ is the largest integer $m$ for which $\ker((f-\lambda I)^{m})$ is strictly larger than $\ker((f-\lambda I)^{m-1})$.

From this definition, we can see that the algebraic multiplicities of $\lambda=1$ are different for $A$ and $B$ in the "Computing Eigenvalues" section. Taking successive powers of $B-I_{3}$ gives first $(0,1,0)$ and then $(0,0,1)$ in the kernels, while the algebraic multiplicity for $A$ is just $1$.

Algebraic and geometric multiplicity work together to give a characterization of any linear map, considered over the complex numbers, in terms of so-called *Jordan blocks*. These are square sub-matrices with $\lambda$ on the diagonal and $1$'s on the adjacent diagonal. For example for $n=3$:

$$J_{\lambda,3}=\begin{pmatrix}\lambda&1&0\\0&\lambda&1\\0&0&\lambda\end{pmatrix}$$

The *Jordan canonical form* theorem states that for any linear map $V\to V$ (with complex scalars) there is a basis for $V$, for which the matrix of that linear map consists entirely of Jordan blocks along the diagonal. There may be more than one Jordan block for a given eigenvalue, but the size and number of blocks are determined by the algebraic and geometric multiplicities of that eigenvalue, respectively.

All of this is to note two things: it's possible to compute all of the eigenvalues and eigenvectors for a linear map, and these, along with some auxiliary data (some of which I've left out from this text), do in fact give a complete characterization of the map. However, it's a more nuanced characterization, and one whose benefits are not as easily displayed as when you have an orthonormal basis of eigenvectors. The Jordan canonical form is an important theorem that has generalizations and adaptations in other fields of mathematics.

Finally, as a quick aside, the set of all eigenvalues together with their geometric multiplicities is called the *spectrum* of a linear map.

**Definition 12.30.** Let $f:V\to V$ be a linear map between vector spaces. Define the *spectrum* of $f$ as the set

$$\operatorname{Spec}(f)=\{(\lambda,\dim\ker(f-\lambda I)):f(v)=\lambda v\text{ for some nonzero }v\in V\}.$$

It is interesting to note that most scientific uses of the word "spectrum" refer to this mathematical idea, for example the spectrum of wavelengths of light or the spectrum of an atom.
