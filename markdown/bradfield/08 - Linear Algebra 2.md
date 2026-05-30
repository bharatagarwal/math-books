# Linear Algebra 2

*Bradfield session 8 · Thursday 9 July · applications (continues session 7)*

The previous session built the mental model that 3Blue1Brown spends its whole
series on: a matrix is a **linear transformation** — it moves the whole grid of
space while keeping lines straight and the origin fixed — multiplication is
**composition** of those moves, and the **determinant** is the factor by which
the map scales area (or volume), with $\det = 0$ meaning the map *squishes* space
into a lower dimension. This session spends that model on what linear algebra is
actually *used* for: solving systems of equations, fitting models to noisy data,
finding the special directions of a transformation, and — the showpiece that ties
linear algebra to next session's graph theory — ranking the web.

The spine of the chapter is one question and one habit. The question is *"given a
transformation, which input produces a desired output?"* The habit, as always in
this reader, is to **build the small object and look** before trusting a formula:
print the column space, watch the projection error shrink, watch power iteration
swing onto an eigenvector. Each application is only a few lines of `numpy` once
you see what it is really computing.

## Solving linear systems: the question behind $A\mathbf{x} = \mathbf{b}$

A system of linear equations is a single matrix equation $A\mathbf{x} =
\mathbf{b}$. Following **3Blue1Brown ch 7**, read it geometrically: $A$ is a
transformation, and we are hunting for the input vector $\mathbf{x}$ that *lands
on* the output $\mathbf{b}$ after the transformation is applied. Whether such an
$\mathbf{x}$ exists, and whether it is unique, is decided entirely by the
determinant/rank story from session 7:

- $A$ **invertible** ($\det \neq 0$, full rank): the map doesn't squish space, so
  it has an inverse $A^{-1}$ — the unique transformation that "plays the tape
  backward," $A^{-1}A = I$. There is exactly **one** solution, $\mathbf{x} =
  A^{-1}\mathbf{b}$ (though in practice we *solve* directly rather than form the
  inverse).
- $A$ **singular** ($\det = 0$): the map squishes space onto a lower-dimensional
  **column space** — a line, or a plane. Now $\mathbf{b}$ might not be reachable
  at all (**no** solution), or it might lie in that squished output and be
  reachable in **infinitely many** ways.

The clean machine test for the two singular cases compares
$\operatorname{rank}(A)$ — the dimension of the column space — with
$\operatorname{rank}([A \mid \mathbf{b}])$. Equal ranks mean $\mathbf{b}$ added no
new direction, so it lies in the column space and the system is *consistent*; a
larger augmented rank means $\mathbf{b}$ pokes out of the column space and the
equations *contradict* each other. (Under the hood, a direct `solve` runs Gaussian
elimination — the systematic row-reduction you may have done by hand.)

```python
<!-- include: code/bradfield/08-linear-algebra-2/01_solving_systems.py -->
```

That demo *confirms* the trichotomy on three matrices. But the words "column
space" and "null space" only click once you **build them and look**. Take the
singular map $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$: its second row is
twice the first, so it collapses the entire plane onto the single line spanned by
$(1, 2)$ — that line *is* its column space, and its rank is $1$. The directions
that get crushed all the way to the origin form the **null space** (a whole line
here, not just the zero vector), and that null space is exactly the "wiggle room"
behind *infinitely many* solutions: add any null-space vector to one solution and
you get another. The next demo feeds a grid of inputs through $A$ to watch every
output land on that one line, finds the null direction, and then shows a target on
the line acquiring a one-parameter family of solutions:

```python
<!-- include: code/bradfield/08-linear-algebra-2/05_colspace_nullspace.py -->
```

So the trichotomy isn't three unrelated cases — it is one picture (3Blue1Brown
ch 7): *does the map squish space, and if so, does $\mathbf{b}$ survive the
squish?*

## Least squares: regression as projection

Real data hands you *more equations than unknowns* — sixty noisy points, two
parameters of a line. Then $A\mathbf{x} = \mathbf{b}$ has **no** exact solution:
$\mathbf{b}$ sits outside the column space of $A$ (the relatively thin set of
outputs the model can actually produce). The right question becomes: which
$\mathbf{x}$ makes $A\mathbf{x}$ as *close* to $\mathbf{b}$ as possible?
Minimizing $\|A\mathbf{x} - \mathbf{b}\|^2$ gives the **least-squares** solution,
and the geometry is the whole point: the best $A\mathbf{x}$ is the **orthogonal
projection** of $\mathbf{b}$ onto the column space — the foot of the perpendicular
— and the leftover error is perpendicular to that space. Writing "the residual is
orthogonal to every column of $A$" as $A^{\mathsf{T}}(\mathbf{b} - A\mathbf{x}) =
\mathbf{0}$ and rearranging gives the **normal equations**
$$A^{\mathsf{T}}A\,\mathbf{x} = A^{\mathsf{T}}\mathbf{b}.$$
This *is* linear regression — the workhorse of statistics and the simplest
machine-learning model. We fit a line to noisy data two ways (the normal
equations and `numpy`'s numerically stable solver), confirm they agree, recover
the true line, and check that the residual really is orthogonal to the column
space:

```python
<!-- include: code/bradfield/08-linear-algebra-2/02_least_squares.py -->
```

"Closest point = drop a perpendicular" is worth *seeing*, not just asserting. The
next demo puts a target $\mathbf{b}$ above a plane (the column space of $A$ in
$\mathbb{R}^3$) and slides $\mathbf{x}$ from a poor guess toward the least-squares
answer, printing the squared error $\|A\mathbf{x} - \mathbf{b}\|^2$ shrinking
monotonically and bottoming out exactly at the projection — where, and only where,
the residual sticks straight out of the plane:

```python
<!-- include: code/bradfield/08-linear-algebra-2/06_projection_error.py -->
```

Seeing the error collapse to its minimum at the foot of the perpendicular is the
intuition; the normal equations are just that picture written in symbols.

## Eigenvalues and eigenvectors: the directions a map only scales

Most directions get knocked off their own line by a transformation — rotated as
well as stretched. A few special directions get **only scaled**: the map leaves
their line exactly where it was, merely stretching or squishing along it. Those
are the **eigenvectors**, and their scale factors are the **eigenvalues**:
$$A\mathbf{v} = \lambda\mathbf{v}.$$
They expose the intrinsic axes of a transformation: the long axis of a cloud of
data (PCA), the steady state of a Markov chain, the modes of a vibrating system,
the growth rate of a recurrence. Two invariants come for free and tie back to
session 7: the **trace** (sum of the diagonal) equals the sum of the eigenvalues,
and the **determinant** equals their product — fitting, since the determinant is
the overall area scale and the eigenvalues are the per-axis scales. A specially
important case is a **symmetric** matrix ($A = A^{\mathsf{T}}$): the **spectral
theorem** guarantees its eigenvalues are *real* and its eigenvectors *orthogonal*,
which is exactly why covariance matrices yield clean, perpendicular principal
components.

```python
<!-- include: code/bradfield/08-linear-algebra-2/03_eigen.py -->
```

`numpy` hands us the eigenvectors in one call, but that hides *how* you would find
the dominant one when the matrix is huge — and the answer is the same engine that
runs PageRank. **Power iteration** starts from an arbitrary direction and applies
$A$ over and over, renormalizing each step. Because the component along the
largest-$|\lambda|$ eigenvector grows fastest, the vector swings toward that
eigendirection. The next demo prints that happening: the angle between the current
vector and the true dominant eigenvector collapsing toward $0$, and the Rayleigh
quotient $\frac{\mathbf{v}^{\mathsf{T}}A\mathbf{v}}{\mathbf{v}^{\mathsf{T}}
\mathbf{v}}$ homing in on the dominant eigenvalue:

```python
<!-- include: code/bradfield/08-linear-algebra-2/07_power_iteration.py -->
```

## PageRank: the dominant eigenvector of a graph

The application that made a company. Model a web surfer who, $85\%$ of the time,
clicks a random outgoing link, and otherwise teleports to a random page. This is a
Markov chain whose transition matrix $G$ (the "Google matrix") is built from the
link graph. A page's importance is its share of the surfer's time in the long run
— the **stationary distribution** $\mathbf{r}$ satisfying
$$G\mathbf{r} = \mathbf{r},$$
which is precisely the eigenvector of $G$ for eigenvalue $1$. You find it by the
**power iteration** we just watched converge: start anywhere and apply $G$
repeatedly until it settles. This is where this session and the next meet —
*importance on a graph is an eigenvector problem.* We build the Google matrix by
hand, check its columns are stochastic, power-iterate to the stationary ranking,
and cross-check against `networkx`'s implementation:

```python
<!-- include: code/bradfield/08-linear-algebra-2/04_pagerank.py -->
```

## Where to go deeper

These four — Gaussian elimination (solving), least squares (projection), the
eigen-decomposition, and the power method — are the algorithms underneath most
numerical and data work, and three of them are *the same idea* wearing different
clothes: find a special vector (a solution, a projection, an eigenvector) by
exploiting structure of the map. The eigen/PageRank thread also previews the next
session: graphs carry matrices (adjacency, Laplacian) whose **spectra** encode
connectivity, clustering, and flow. For the geometric intuition behind every
section here, rewatch **3Blue1Brown** *Essence of Linear Algebra* ch 6 (the
determinant and what $\det = 0$ destroys) and ch 7 (inverse matrices, column
space, rank, and null space). Strang's *Introduction to Linear Algebra* is the
companion text for the least-squares and eigenvalue machinery, and Klein's
*Coding the Matrix* for the programmer's-eye view; this session's pre-work depends
on how far the prior one reached, so check with your instructor.
