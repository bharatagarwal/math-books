# Linear Algebra

*Bradfield session 7 · Monday 6 July · pre-work: 3Blue1Brown
"Essence of Linear Algebra", videos 1–7 · further: Strang,
*Introduction to Linear Algebra**

This is the one session whose suggested reading is not a book but a
series of animations: Grant Sanderson's **3Blue1Brown "Essence of
Linear Algebra"** (we abbreviate it **3b1b** below, citing chapters as
*3b1b ch N*). That choice sets the whole tone. Most linear-algebra
courses open with a wall of matrix arithmetic — row reduction, cofactor
expansions — and the *meaning* arrives, if ever, much later. Sanderson
inverts that order on purpose: every symbol is anchored to a moving
picture first, and the arithmetic is derived from the picture. His
recurring plea is *"don't just memorize the operations — understand
what they're doing to space."*

So this chapter follows his sequence exactly: **vectors as arrows →
span and basis → a matrix as where the basis vectors land → matrix
multiplication as composition → the same ideas in 3D → the determinant
as an area/volume factor → inverses, rank, column space, null space.**
And because we are software engineers, we do one thing the videos can
only gesture at: after each picture we *build the objects and look*, in
NumPy, so the geometric claim becomes something the machine confirms.

## Vectors are arrows you can add and scale

3b1b ch 1 reconciles three views of a vector: the physicist's arrow (a
direction and a magnitude), the CS view (an ordered list of numbers),
and the mathematician's view (anything you can add and scale).
Sanderson's stance is that the arrow rooted at the origin is the picture
to keep in your head, and the list of coordinates is just its address.

Two operations are fundamental, and *everything* in the subject is built
from them. **Addition** is "tip to tail": slide $\vec{w}$ so its tail
sits on the tip of $\vec{v}$, and the sum is the arrow from the start to
the final tip — which, in coordinates, is just adding componentwise.
**Scaling** by a number (a *scalar*) stretches the arrow, squishes it,
or — for a negative scalar — flips it around. The whole of $\mathbb{R}^2$
is then reachable as
$$\begin{bmatrix} x \\ y \end{bmatrix}
   = x\begin{bmatrix} 1 \\ 0 \end{bmatrix}
   + y\begin{bmatrix} 0 \\ 1 \end{bmatrix}
   = x\,\hat{\imath} + y\,\hat{\jmath},$$
the two special vectors $\hat{\imath}=(1,0)$ and $\hat{\jmath}=(0,1)$
being the **standard basis**. A coordinate pair is really a recipe: "go
$x$ of the way along $\hat{\imath}$, then $y$ along $\hat{\jmath}$."

The verification is small but worth making concrete — addition really is
componentwise, and any vector really does decompose along the basis:

```python
<!-- include: code/bradfield/07-linear-algebra/01_vectors.py -->
```

## Span: which points can you reach?

3b1b ch 2 asks the question that turns two arrows into a *set*: given
$\vec{v}$ and $\vec{w}$, which points can you reach by **linear
combinations** $a\vec{v} + b\vec{w}$ as $a$ and $b$ range over all
numbers? That reachable set is the **span**. Sanderson's punchline is
visual: if the two arrows point in genuinely different directions, their
combinations sweep out the *entire plane*; but if $\vec{w}$ happens to
lie along $\vec{v}$ (a scaled copy of it), the combinations never leave
that single line. The second arrow added *no new direction*.

That distinction is exactly **linear dependence**: a set is dependent
when one vector is already in the span of the others (it is redundant),
and **independent** when every vector pulls in a fresh direction. A
**basis** is then a set of independent vectors that spans the whole
space — the minimum recipe-ingredients you need.

Rather than assert this, the cleaner move is to *discover* it: sweep $a$
and $b$ over a grid and literally count how many distinct points each
pair of vectors can reach. Independent vectors reach a full 2D cloud of
points; a dependent pair collapses onto a line.

```python
<!-- include: code/bradfield/07-linear-algebra/02_span.py -->
```

The demo prints that the independent pair reaches a full grid of $81$
points while the dependent pair lands every one of its $25$ combinations
on the line $y=x$ — the span has dropped from a plane to a line. That
collapse from 2D to 1D is the same phenomenon we will meet again as a
*zero determinant*.

## A matrix is where the basis vectors land

This is the conceptual hinge of the whole series (3b1b ch 3), and the
sentence to memorize is Sanderson's: **the columns of a matrix are where
the basis vectors land.** A *linear transformation* is a way of moving
every point in the plane such that grid lines stay parallel and evenly
spaced and the origin stays fixed. The remarkable fact is that such a
transformation is *completely determined* by what it does to just
$\hat{\imath}$ and $\hat{\jmath}$, because every other vector is
$x\,\hat{\imath} + y\,\hat{\jmath}$ and linearity means it must follow:
$$L(x\,\hat{\imath} + y\,\hat{\jmath})
  = x\,L(\hat{\imath}) + y\,L(\hat{\jmath}).$$

So we record only the two landing spots, as the columns of a $2\times2$
matrix. Reading the matrix
$\bigl[\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\bigr]$, the
first column $(a,c)$ is the new home of $\hat{\imath}$ and the second
$(b,d)$ is the new home of $\hat{\jmath}$. Matrix–vector multiplication
is then nothing more than "scale the columns by the coordinates and add":
$$\begin{bmatrix} a & b \\ c & d \end{bmatrix}
  \begin{bmatrix} x \\ y \end{bmatrix}
  = x\begin{bmatrix} a \\ c \end{bmatrix}
  + y\begin{bmatrix} b \\ d \end{bmatrix}.$$

```python
<!-- include: code/bradfield/07-linear-algebra/03_matrices_as_maps.py -->
```

The demo checks both halves of the idea: applying the rotation matrix to
$\hat{\imath}$ recovers its first column, and applying it to a general
vector gives the same answer as scaling-and-adding the columns by hand
($R\vec{v}=(-1,3)$ either way). A 90-degree rotation sends $\hat{\imath}$
to $(0,1)$ and $\hat{\jmath}$ to $(-1,0)$; a shear pins $\hat{\imath}$
and slides $\hat{\jmath}$ to $(1,1)$. Once you read columns as
*landings*, you can often picture a matrix's effect without computing
anything.

## Watching the grid move, and multiplication as composition

The best way to feel a transformation is the 3b1b move of watching a
whole grid of points slide to their new homes at once. We can do that in
text: take a small integer grid and print where each point goes under a
shear, and then under a rotation applied on top of it.

3b1b ch 4 then delivers the payoff: **matrix multiplication is the
composition of transformations.** If you first apply the transform $S$
and then the transform $R$, the single matrix that does both at once is
the product $R\,S$ — and the order reads *right to left*, like function
composition $R(S(\vec{v}))$, because the right-hand matrix touches the
vector first. This is *why* matrix multiplication is defined by that
otherwise-mysterious row-times-column rule: it is forced on us by "track
where the basis vectors end up after doing $S$, then $R$."

```python
<!-- include: code/bradfield/07-linear-algebra/04_grid_transform.py -->
```

The demo prints the new address of each grid point after shearing and
then rotating, then verifies that the composed matrix $R\,S$ applied in
one step lands every point in the same place as doing $S$ then $R$ in two
steps. It also confirms Sanderson's warning that composition is **not
commutative**: $R\,S \neq S\,R$ in general — rotating a sheared square is
not the same as shearing a rotated one, and the matrices disagree.

## The same ideas in three dimensions

3b1b ch 5 reassures us that nothing conceptual changes in 3D. A
transformation is still "where do the basis vectors land," only now there
are three of them — $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$ — so the
matrix is $3\times3$ and has three columns, one landing spot each. Grid
lines (now grid *planes*) stay parallel and evenly spaced, the origin
stays put, and multiplication is still composition. The dimension is a
detail; the story is identical. We will lean on this when the determinant
generalizes from area to volume.

## The determinant: how much does area change?

3b1b ch 6 attaches a single number to a transformation that captures its
most important geometric effect: **the determinant is the factor by which
the transformation scales area** (volume in 3D). Track the unit square
spanned by $\hat{\imath}$ and $\hat{\jmath}$, area $1$. After the
transform it becomes a parallelogram; the determinant is that
parallelogram's area. Scale $x$ by $3$ and $y$ by $2$ and the unit square
becomes a $3\times2$ box — determinant $6$. A pure shear slides the top
sideways but keeps base and height, so area is unchanged — determinant
$1$.

Two refinements make the determinant carry even more meaning. First,
**sign encodes orientation**: a negative determinant means the
transformation *flipped* space over (what was a counter-clockwise
$\hat{\imath}\!\to\!\hat{\jmath}$ turn becomes clockwise). Second, and
most important for what follows, **$\det = 0$ means space got squished**
into a line (in 3D, a plane or line) — the area is crushed to zero
because the columns became linearly dependent. That is the algebraic
shadow of the span collapse we watched earlier. For a $2\times2$ matrix
the formula is $\det = ad - bc$.

```python
<!-- include: code/bradfield/07-linear-algebra/05_determinant.py -->
```

The demo confirms each reading: the scaling matrix has determinant $6$
(its area factor), the shear has determinant $1$ (area preserved), a
reflection has determinant $-1$ (orientation flipped), and the dependent
matrix $\bigl[\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr]$ has
determinant $0$ — it squishes the plane onto a line. (The $ad-bc$ formula
is also checked against NumPy inside the file.)

## Inverses, rank, column space, and null space

3b1b ch 7 ties everything together through the most practical question in
the subject: **solving $A\vec{x} = \vec{v}$.** Geometrically this asks
*"which vector $\vec{x}$ lands on $\vec{v}$ after we apply $A$?"* When
$\det A \neq 0$, $A$ does not squish space, so the motion can be run
backwards: there is an **inverse** $A^{-1}$ that undoes $A$
($A^{-1}A = I$), and the unique answer is $\vec{x} = A^{-1}\vec{v}$. When
$\det A = 0$, $A$ has already collapsed space onto something
lower-dimensional, information is lost, and no inverse exists — there is
either no solution or infinitely many.

Sanderson introduces the vocabulary for *how badly* a matrix squishes.
The **rank** is the number of dimensions in the output — the dimension of
the **column space** (the span of the columns, i.e. all the places
vectors can land). A full-rank $2\times2$ matrix has rank $2$: its output
fills the whole plane. A squishing matrix has rank $1$: its output is a
line. And the **null space** (or *kernel*) is the set of vectors sent all
the way to the origin — for a full-rank matrix that is just $\vec{0}$, but
for a squishing matrix it is a whole line of vectors that collapse to
zero.

```python
<!-- include: code/bradfield/07-linear-algebra/06_inverse_rank.py -->
```

The demo solves $A\vec{x}=\vec{v}$ for an invertible $A$ — getting
$\vec{x}=(1.4,1.2)$ — and checks the solution really lands on
$\vec{v}=(4,5)$ and that $A^{-1}A = I$. It then takes the squishing
matrix $\bigl[\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr]$ —
determinant $0$, rank $1$, output a line — and exhibits an explicit
null-space vector $(2,-1)$ that the matrix sends to the origin. Det,
rank, and null space are three views of the same fact: *did the
transformation lose a dimension?*

## Working the problem set

The Bradfield set for this session is small but it rewards translating
each problem back into a picture before reaching for arithmetic:

- **Given a matrix, predict its effect before multiplying.** Read the
  columns as basis landings. Is it a rotation, a shear, a reflection, a
  projection? Then check by applying it to $\hat{\imath}$ and
  $\hat{\jmath}$ in NumPy.
- **Decide invertibility by eye.** Compute (or estimate) the determinant.
  Zero determinant ⇒ the columns are dependent ⇒ no inverse. Confirm with
  `np.linalg.det` and `np.linalg.matrix_rank`.
- **For a singular matrix, find the null space by hand,** then verify
  `A @ v` is the zero vector. This is the most common place intuition and
  arithmetic are made to agree.
- **Compose two transforms both ways** and confirm $AB \neq BA$, then
  explain the difference geometrically.

The reusable habit, straight from 3b1b: when a linear-algebra statement
feels opaque, ask *"what is this doing to space?"* and then build the
arrows or the grid and look.

## Where to go deeper

The natural next step is **Strang's *Introduction to Linear Algebra***
(our "further" resource for this session), which supplies the
computational backbone the videos deliberately skip — row reduction and
$LU$ factorization, the four fundamental subspaces, and least squares.
Strang's "column picture" of $A\vec{x}=\vec{b}$ ("$\vec{b}$ is a
combination of the columns of $A$") is exactly the span/column-space idea
of this chapter in matrix-algebra clothing, so the two sources reinforce
rather than repeat each other. After that, **eigenvalues and
eigenvectors** (3b1b ch 14) are the natural sequel: the special
directions a transformation only stretches, never rotates — which is
where the next session ("Linear Algebra 2") picks up.
