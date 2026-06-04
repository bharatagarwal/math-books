# Linear Algebra

In 1858, Arthur Cayley published "A Memoir on the Theory of Matrices" — the first paper to treat rectangular arrays of numbers as algebraic objects in their own right, with their own rules for addition, multiplication, and inversion. The ideas were older (Gauss had been solving systems of linear equations since the 1800s, and Sylvester had coined the word "matrix" in 1850), but Cayley gave the algebra its modern form.

The payoff was enormous. Systems of linear equations, which had required pages of symbol-juggling, collapsed into a single equation $A\mathbf{x} = \mathbf{b}$. Geometric transformations — rotations, reflections, projections — became matrix multiplications. And in the twentieth century, linear algebra became the workhorse of computation: computer graphics (every pixel you see is matrix-multiplied into place), machine learning (a neural network is a chain of matrix multiplications and nonlinearities), Google's PageRank (the dominant eigenvector of the web's link matrix), and quantum mechanics (observables are Hermitian operators on a Hilbert space).

For a software engineer, the notation below maps almost one-to-one onto NumPy. A vector $\mathbf{x}$ is `np.array(...)`. The dot product $\mathbf{x} \cdot \mathbf{y}$ is `x @ y`. The transpose $A^T$ is `A.T`. The eigenvalues $\lambda_1, \ldots, \lambda_n$ come from `np.linalg.eig`. The notation is the API specification; NumPy is the implementation.

## Vectors

A (real) vector is an $n$-long column$^{1}$ of real numbers:

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}.
$$

In textbooks, vectors are often denoted with bold letters $\mathbf{v}$, but some people write vectors as ordinary letters with an arrow on top $\vec{v}$. However, when writing vectors by hand (on paper or on a black board), it's easier to draw a single-tined arrow (called a harpoon): $\vec{v}$. Another convention for handwritten vectors is $\underline{\nu}$ as the wavy underline is a typographer's convention for boldface. Finally, many mathematicians use plain letters $\nu$ (no boldface or arrows) to stand for vectors.

The set of all vectors of length $n$ is denoted $\mathbb{R}^n$. (Complex vectors are $n$-long columns of complex numbers, and the set of all such vectors is denoted $\mathbb{C}^n$.)

### Notation conventions at a glance

| Symbol | Meaning | NumPy |
| --- | --- | --- |
| $\mathbf{x}$, $\vec{x}$ | a vector | `np.array([...])` |
| $\mathbb{R}^n$ | set of all $n$-vectors | shape `(n,)` |
| $\mathbf{e}_j$ | $j$-th standard basis vector | `np.eye(n)[j]` |
| $\hat{\mathbf{u}}$ | unit vector | `u / np.linalg.norm(u)` |
| $\mathbf{0}$ | zero vector | `np.zeros(n)` |
| $\|\mathbf{x}\|$ | Euclidean norm | `np.linalg.norm(x)` |
| $\|\mathbf{x}\|_p$ | $p$-norm | `np.linalg.norm(x, p)` |
| $\mathbf{x} \cdot \mathbf{y}$ | dot product | `x @ y` or `np.dot(x, y)` |
| $\mathbf{x} \perp \mathbf{y}$ | orthogonal | `np.isclose(x @ y, 0)` |
| $\mathbf{v} \times \mathbf{w}$ | cross product ($\mathbb{R}^3$) | `np.cross(v, w)` |

### Basis vectors

Vectors corresponding to physical quantities (such as forces or displacements) are typically three dimensional, i.e., are elements of $\mathbb{R}^3$. Such vectors are often expressed using $\mathbf{i}, \mathbf{j}, \mathbf{k}$-coordinates. These basis vectors are defined as

$$
\mathbf{i} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{j} = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \quad \text{and} \quad \mathbf{k} = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}.
$$

In $\mathbb{R}^n$ the standard basis vectors are usually denoted $\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n$ where $\mathbf{e}_j$ is a vector entirely populated by zeros except for a 1 in position $j$. (The dimension of the vector, $n$, is inferred from context.)

Whether one writes $\mathbf{i}, \mathbf{j}, \mathbf{k}$ or $\mathbf{e}_1, \mathbf{e}_2, \ldots$, all of these vectors have length one (see entry under Magnitude below) and are called unit vectors. Some people indicate that a vector has length one with a hat decoration: $\hat{\mathbf{u}}$.

The vector of all zeros is variously denoted $\mathbf{0}, \vec{0}$, or sometimes simply as 0 (in which case it is difficult to distinguish from the real number zero). A vector of all ones can be written $\mathbf{1}, \vec{1}, \mathbf{e}$, or $\vec{e}$. We prefer the notation $\mathbf{1}$.

$^{1}$Some people write vectors as row vectors. This is convenient because the notation is more compact. It is also traditional in some application areas.

### Standard vector operations

- **Sum.** The sum of vectors $\mathbf{x}$ and $\mathbf{y}$ is simply $\mathbf{x} + \mathbf{y}$.
- **Scalar multiple.** The scalar multiplication is usually written with the scalar $s$ on the left and the vector $\mathbf{x}$ on the right: $s\mathbf{x}$.
- **Magnitude.** The magnitude (length, norm) of a vector is denoted $\| \mathbf{x} \|$ and we have

$$
\| \mathbf{x} \| = \sqrt {x _ {1} ^ {2} + x _ {2} ^ {2} + \cdots + x _ {n} ^ {2}}.
$$

Some people use single bars $|\mathbf{x}|$ to denote the magnitude of a vector.

- **$p$-norm.** For a positive real number $p$, the $p$-norm of $\mathbf{x}$ is

$$
\| \mathbf{x} \| _ {p} = \left[ | x _ {1} | ^ {p} + | x _ {2} | ^ {p} + \cdots + | x _ {n} | ^ {p} \right] ^ {1 / p}.
$$

Note that $\| \mathbf{x}\| _2 = \| \mathbf{x}\|$.

The infinity norm is $\| \mathbf{x}\|_{\infty} = \max \left(|x_1|, |x_2|, \dots, |x_n|\right)$.

### Dot product and inner products

- **Dot (inner) product.** The dot product of two vectors $\mathbf{x}$ and $\mathbf{y}$ is

$$
\mathbf {x} \cdot \mathbf {y} = x _ {1} y _ {1} + x _ {2} y _ {2} + \cdots + x _ {n} y _ {n}.
$$

The dot product of $\mathbf{x}$ and $\mathbf{y}$ is also written $\langle \mathbf{x},\mathbf{y}\rangle$. These delimiters are called angle brackets and are not less-than and greater-than symbols. The dot product may also be written as $\mathbf{x}'\mathbf{y}$ or $\mathbf{x}^T\mathbf{y}$ (see the discussion of Transpose below).

If the angle between vectors $\mathbf{x}$ and $\mathbf{y}$ is $\theta$, then we have the formula

$$
\mathbf {x} \cdot \mathbf {y} = \| \mathbf {x} \| \times \| \mathbf {y} \| \times \cos \theta .
$$

If $\mathbf{x}$ and $\mathbf{y}$ are complex $n$-vectors, then often

$$
\langle \mathbf {x}, \mathbf {y} \rangle = \sum_ {k = 1} ^ {n} x _ {k} \overline {{y _ {k}}}
$$

but some authors define this as $\sum_{k=1}^{n} \overline{x_k} y_k$. (Here $\overline{x}$ denotes complex conjugate; see page 17.)

Physicists denote inner products like this: $\langle \mathbf{x} \mid \mathbf{y} \rangle$. This is known as bra-ket (or bracket) notation. They also write $\langle x \mid$ and $|y\rangle$ for row and column vectors which they call bra-vectors and ket-vectors.

Inner products arise in contexts beyond $\mathbb{R}^n$ or $\mathbb{C}^n$. For example, if $f, g: \mathbb{R} \to \mathbb{R}$, then we may put

$$
\langle f, g \rangle = \int_ {- \infty} ^ {\infty} f (t) g (t) d t
$$

or there may be a weighting in the formula as in this example:

$$
\langle f, g \rangle = \int_ {- \infty} ^ {\infty} e ^ {- t ^ {2} / 2} f (t) g (t) d t.
$$

### Orthogonality

Two vectors are orthogonal provided their dot product is zero, in which case we write $\mathbf{x} \perp \mathbf{y}$.

The $\perp$ symbol is also used to define subspaces of $\mathbb{R}^n$. If $\mathcal{V}$ is a subspace of $\mathbb{R}^n$, then $\mathcal{V}^{\perp}$ is the set of vectors that are orthogonal to all vectors in $\mathcal{V}$:

$$
\mathcal{V}^{\perp} = \{\mathbf{x} \in \mathbb{R}^n: \forall \mathbf{v} \in \mathcal{V}, \mathbf{x} \perp \mathbf{v}\}.
$$

The subspace $\mathcal{V}^{\perp}$ is called the orthogonal complement of $\mathcal{V}$.

### Cross product and scalar triple product

- **Cross product.** The cross product is defined only for vectors in $\mathbb{R}^3$. If $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}$ and $\mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix}$ then

$$
\mathbf{v} \times \mathbf{w} = \begin{bmatrix} v_2 w_3 - v_3 w_2 \\ v_3 w_1 - v_1 w_3 \\ v_1 w_2 - v_2 w_1 \end{bmatrix}.
$$

- **Scalar triple product.** Given three vectors $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{R}^3$, their scalar triple product is

$$
[\mathbf{a}, \mathbf{b}, \mathbf{c}] = \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c} = \det \begin{bmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{bmatrix}.
$$

### Vectors in NumPy

Every operation above has a direct NumPy equivalent. NumPy arrays *are* vectors — there's no wrapper class, no abstraction layer. The `@` operator is the dot product, `np.linalg.norm` computes any $p$-norm, and `np.cross` handles the cross product:

```python
<!-- include: code/mathematical-notation/07 - Linear Algebra/01_python.py -->
```

## Matrices

A matrix is a rectangular array of numbers. A matrix with $m$ rows and $n$ columns is called an $m \times n$-matrix; the number of rows is always given first and then the number of columns. The set of all real $m \times n$-matrices is denoted $\mathbb{R}^{m \times n}$ and for complex matrices we write $\mathbb{C}^{m \times n}$. An alternative notation is $M_n(\mathbb{R})$ for real $n \times n$-matrices and $M_{a,b}(\mathbb{R})$ for real $a \times b$-matrices. Likewise for complex matrices, we write $M_n(\mathbb{C})$ and $M_{a,b}(\mathbb{C})$.

It is often useful to consider vectors as $n \times 1$-matrices.

If $A$ is a matrix, the $i,j$-entry of $A$ is the entry in the $i^{\text{th}}$ row and $j^{\text{th}}$ column and is variously denoted $A_{i,j}$ or $a_{i,j}$ or $[A]_{i,j}$. It is common to omit the comma separating the subscripts.

### Notation-to-NumPy cheat sheet

| Notation | Meaning | NumPy |
| --- | --- | --- |
| $A_{i,j}$ | entry at row $i$, col $j$ | `A[i, j]` (0-indexed) |
| $A + B$ | matrix sum | `A + B` |
| $rA$ | scalar multiplication | `r * A` |
| $AB$ | matrix product | `A @ B` |
| $I_n$ | identity matrix | `np.eye(n)` |
| $A^{-1}$ | inverse | `np.linalg.inv(A)` |
| $A^T$ | transpose | `A.T` |
| $\det A$ | determinant | `np.linalg.det(A)` |
| $\operatorname{tr} A$ | trace | `np.trace(A)` |
| $\operatorname{rank}(A)$ | rank | `np.linalg.matrix_rank(A)` |
| $\lambda_i$ | eigenvalues | `np.linalg.eig(A)[0]` |
| $\sigma_i$ | singular values | `np.linalg.svd(A)[1]` |
| $\kappa(A)$ | condition number | `np.linalg.cond(A)` |
| $\|A\|_F$ | Frobenius norm | `np.linalg.norm(A, 'fro')` |

### Arithmetic

There are many notations associated with matrices.

- **Addition/subtraction.** Matrices of the same shape may be added. The $i, j$-entry of $A + B$ is $a_{i,j} + b_{i,j}$. Likewise $A - B$ is the matrix whose $i, j$-entry is $a_{i,j} - b_{i,j}$.
- **Scalar multiplication.** If $A$ is a matrix and $r$ is a scalar, then $rA$ is a matrix, of the same size as $A$, whose $i, j$-entry is $ra_{i,j}$.
- **Matrix multiplication.** If $A$ is an $m \times n$-matrix and $B$ is an $n \times p$-matrix, then they may be multiplied and the $i, j$-entry of $AB$ is

$$
[AB]_{i,j} = \sum_{k=1}^{n} a_{i,k} b_{k,j}.
$$

In Python, the `@` operator performs this sum-of-products for you: `A @ B`. The key constraint is that the inner dimensions must match — $A$ is $m \times n$ and $B$ is $n \times p$ — which is why you get a shape error when they don't.

### Special matrices

- **Identity matrix and Kronecker's delta.** The identity matrix is an $n \times n$-matrix whose off-diagonal entries are all 0 and whose main diagonal entries are all 1. An identity matrix is denoted $I$; the notation $I_n$ is used to denote an $n \times n$-identity matrix.

The notation $\delta(i, j)$, called Kronecker's delta, is used to represent the $i, j$-entry of an identity matrix. It is defined by

$$
\delta(i, j) = \begin{cases} 1 & \text{if } i = j \text{ and} \\ 0 & \text{if } i \neq j. \end{cases}
$$

Kronecker's delta is sometimes written with its arguments as subscripts: $\delta_{i,j}$ or $\delta_{ij}$.

- **Inverse.** If $A$ is a square matrix and there is another square matrix $B$ such that $AB = I$, then $B$ is called the inverse of $A$ and is denoted $A^{-1}$.

- **Pseudoinverse.** The Moore-Penrose pseudoinverse of a matrix $A$ is denoted $A^+$. Some people write $A^\dagger$, but this notation is also used for the conjugate transpose of $A$ (see Transpose below). In NumPy: `np.linalg.pinv(A)`. The pseudoinverse generalizes the inverse to non-square and singular matrices — it's what `np.linalg.lstsq` uses under the hood.

- **Hadamard product.** Given two matrices $A$ and $B$ of the same shape, their Hadamard product is denoted $A \circ B$. It is a new matrix with the same shape as $A$ and $B$ whose $i, j$-entry is $a_{i,j}b_{i,j}$. In NumPy this is just `A * B` — elementwise multiplication is the default, not matrix multiplication. (This trips up beginners: `*` is Hadamard, `@` is matrix product.)

- **Matrix of all 1s.** A matrix of all 1s is often denoted $J$. We write $J_{m,n}$ to stand for an $m \times n$-matrix of all 1s. In NumPy: `np.ones((m, n))`.

### Transpose

If $A$ is an $m \times n$-matrix, its transpose is an $n \times m$-matrix denoted $A^t$ (or $A^T$); it is defined by

$$
\left[ A^t \right]_{i,j} = a_{j,i}.
$$

A matrix $A$ that satisfies $A = A^t$ is called symmetric.

For a (complex) $m \times n$-matrix $A$, its conjugate transpose is an $n \times m$-matrix $A^*$; it is defined by

$$
\left[ A^* \right]_{i,j} = \overline{a_{j,i}}.
$$

Some authors prefer an $H$ superscript to denote conjugate transpose: $A^H$. In addition, some people write $A^\dagger$, but this may be confused with the notation for the Moore-Penrose pseudoinverse (described earlier).

In MATLAB, the transpose of a matrix is denoted with a prime symbol: `A'`. If `A` is complex, this returns the conjugate transpose. In NumPy, `A.T` gives the (non-conjugated) transpose and `A.conj().T` gives the conjugate transpose.

The matrix $A^*$ (or $A^H$) is known as the adjoint of $A$.

A matrix that satisfies $A = A^*$ (equivalently $A = A^H$) is called Hermitian or self-adjoint.

Note: The adjoint of $A$ should not be confused with the adjugate of $A$, denoted $\mathrm{adj}(A)$, which is the transpose of the matrix of cofactors of $A$.

### Trace, rank, and null space

- **Trace.** The trace of a matrix is the sum of its diagonal elements. If $A$ is an $m \times n$-matrix then

$$
\operatorname{tr} A = \sum_{i=1}^{\min\{m,n\}} a_{i,i}.
$$

- **Rank/nullity.** The rank of a matrix $A$ is the dimension of its column (or row) space and is denoted $\operatorname{rank}(A)$, though other notations may be used.

The null space of $A$, the set of vectors $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$, may be denoted $\mathrm{null}(A)$. It is also denoted $\ker(A)$ because the null space is also known as the kernel of $A$.

### Determinant and permanent

- **Determinant.** The determinant of a matrix is denoted $\det A$. Sometimes the determinant of a matrix is indicated by vertical bars in place of square brackets:

$$
\left| \begin{array}{ccc} 1 & 2 & 3 \\ 4 & 7 & 0 \\ 2 & 1 & 9 \end{array} \right| = \det \left[ \begin{array}{ccc} 1 & 2 & 3 \\ 4 & 7 & 0 \\ 2 & 1 & 9 \end{array} \right].
$$

Some people place the vertical bars around the name of the matrix to denote determinant: $|A|$.

The determinant of an $n \times n$-matrix $A$ can be expressed by the following formula:

$$
\det A = \sum_{\pi \in S_n} (\operatorname{sgn} \pi) a_{1,\pi(1)} a_{2,\pi(2)} \cdots a_{n,\pi(n)}. \tag{1}
$$

This formula affords us the opportunity to discuss additional notation:

- $S_n$ stands for the set of all permutations on the set $\{1,2,\ldots,n\}$. Thus the sum has $n!$ terms; one for each permutation of $[n]$. It is called the symmetric group. Some people use a German $S$ for this set: $\mathfrak{S}_n$.
- $\pi$ in this formula is not the real number 3.14159... but rather is a dummy variable standing for a permutation.
- $\operatorname{sgn} \pi$ is the sign of the permutation $\pi$; it equals 1 if $\pi$ is an even permutation and $-1$ if $\pi$ is an odd permutation.

- **Permanent.** By omitting the $\operatorname{sgn} \pi$ factor in the formula in equation (1), we arrive at the permanent of the matrix $A$:

$$
\operatorname{perm} A = \sum_{\pi \in S_n} a_{1,\pi(1)} a_{2,\pi(2)} \cdots a_{n,\pi(n)}.
$$

### Matrix operations in NumPy

Matrix multiplication, determinant, inverse, eigenvalues, singular values — each notation symbol maps directly to a NumPy call. The `@` operator is matrix multiplication, `np.linalg` holds the decompositions:

```python
<!-- include: code/mathematical-notation/07 - Linear Algebra/02_python.py -->
```

### Matrix powers and exponential

- **Matrix powers.** Let $A$ be a square matrix. For an integer $n$,

$$
A ^ {n} = \begin{cases} \underbrace{A \cdot A \cdots A}_{n \text{ times}} & \text{for } n > 0, \\ I & \text{for } n = 0, \text{ and} \\ \left(A^{-1}\right)^{|n|} & \text{for } n < 0, \text{ provided } A \text{ is invertible}. \end{cases}
$$

In NumPy: `np.linalg.matrix_power(A, n)`.

Given a square matrix $A$, the square root of $A$ should be a matrix $B$ so that $B^2 = A$. In case $A$ is real symmetric or Hermitian, and positive semi-definite, then $\sqrt{A} = A^{1/2}$ has a generally agreed upon interpretation: Diagonalize $A = S^*\Lambda S$ where $S^*S = I$ and put $\sqrt{A} = S^*\sqrt{\Lambda}S$ where $\sqrt{\Lambda}$ is the diagonal matrix of the (nonnegative) square roots of the eigenvalues.

- **Matrix exponential.** Let $A$ be a square matrix. The expression $\exp A$ (or $e^A$) is the matrix exponential function. It means

$$
\exp A = \sum_ {k = 0} ^ {\infty} \frac {1}{k !} A ^ {k}.
$$

In SciPy: `scipy.linalg.expm(A)`. (Note: `np.exp(A)` computes the elementwise exponential, not the matrix exponential — a common gotcha.)

### Tensor/Kronecker product and direct sum

- **Tensor/Kronecker product.** Let $A$ be an $m \times n$-matrix and $B$ be a $p \times q$-matrix. Their tensor (or Kronecker) product is an $mp \times nq$-matrix given by the following formula:

$$
A \otimes B = \left[ \begin{array}{cccc} a _ {1, 1} B & a _ {1, 2} B & \dots & a _ {1, n} B \\ a _ {2, 1} B & a _ {2, 2} B & \dots & a _ {2, n} B \\ \vdots & \vdots & \ddots & \vdots \\ a _ {m, 1} B & a _ {m, 2} B & \dots & a _ {m, n} B \end{array} \right].
$$

In NumPy: `np.kron(A, B)`.

- **Kronecker sum.** For square matrices $A$ and $B$ (where $A$ is $a \times a$ and $B$ is $b \times b$) their Kronecker sum is denoted $A \oplus B$ and is defined by

$$
A \oplus B = A \otimes I _ {b} + I _ {a} \otimes B
$$

where $I_{a}$ and $I_{b}$ are identity matrices whose sizes are given by their subscripts. Be warned! The notation $A \oplus B$ has another meaning that we consider next.

- **Direct sum.** For any two matrices $A$ and $B$, their direct sum is denoted $A \oplus B$. This is the block diagonal matrix with the structure

$$
\left[ \begin{array}{cc} A & 0 \\ 0 & B \end{array} \right]
$$

where the 0's represent blocks of zeros of the appropriate size. In SciPy: `scipy.linalg.block_diag(A, B)`.

Note that $\oplus$ is also used for the Kronecker sum (see the previous entry).

### Inequalities

If $A$ and $B$ are the same shape, then $A \geq B$ means that each term in $A$ is greater than or equal to the corresponding term in $B$, i.e., $a_{i,j} \geq b_{i,j}$. Likewise $A > B$, $A < B$, and $A \leq B$ have similar meanings. However, $A \neq B$ simply means that the two matrices are not identical.

The notation $A \geq 0$ means that every entry in $A$ is nonnegative, and likewise for $A > 0$, $A \leq 0$, and $A < 0$.

If $A$ and $B$ are square, real symmetric or complex Hermitian matrices, $A \succeq B$ means that $A - B$ is positive semidefinite and $A \succ B$ means that $A - B$ is positive definite. The notations $A \preceq B$ and $A \prec B$ mean $B \succeq A$ and $B \succ A$, respectively. Writing $A \succ 0$ [resp. $A \succeq 0$] means that $A$ is positive definite [resp. positive semidefinite]. Of course, $A \prec 0$ [$A \preceq 0$] means that $A$ is negative definite [negative semidefinite].

The Loewner ordering ($\succeq$, $\preceq$) shows up constantly in optimization and machine learning — covariance matrices are positive semidefinite, and semidefinite programming constrains matrices to satisfy $A \succeq 0$.

### Eigenvalues and singular values

- **Eigenvalues.** It is strongly traditional (but not mandatory) to use the letter $\lambda$ for an eigenvalue of a matrix and subscripted $\lambda$'s (i.e., $\lambda_1, \ldots, \lambda_n$) to denote the full spectrum.

The eigenvalue equation $A\mathbf{v} = \lambda\mathbf{v}$ says: $A$ acts on the eigenvector $\mathbf{v}$ by simply scaling it. The matrix doesn't rotate or shear $\mathbf{v}$ — it just stretches (or shrinks) it by a factor of $\lambda$. This is why eigenvalues reveal the "essential behavior" of a matrix.

If the eigenvalues are all real (as is the case for Hermitian matrices), then one often subscripts the eigenvalues in order, i.e., $\lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n$ or the reverse. In either case, we use the notation $\lambda_{\min}$ and $\lambda_{\max}$ for the smallest and largest eigenvalues, respectively.

- **Singular values.** It is traditional to use the letters $\sigma$ or $s$ to stand for a singular value of a matrix $A$. The full list of singular values are usually subscripted in numerical order: $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n$ or the reverse. We write $\sigma_{\max}$ and $\sigma_{\min}$ for the largest and smallest singular values, respectively.

The SVD ($A = U\Sigma V^T$) generalizes eigendecomposition to non-square matrices and is the backbone of dimensionality reduction (PCA), recommender systems, and numerical stability analysis.

### Matrix norms

We use a triple vertical line to denote matrix norms: $\|A\|$. Note that viewing $\mathbb{C}^{n\times n}$ as a vector space allows us to consider vector norms, but matrix norms require the submultiplicative property: $\|AB\| \leq \|A\| \cdot \|B\|$; the triple delimiter distinguishes true matrix norms from vector norms on $\mathbb{C}^{n\times n}$ viewed merely as an $n^2$-dimensional subspace. However, some authors use the double bars $\|A\|$ for matrix norms.

Here are some specific norms defined on matrices:

| Norm | Notation | Formula | NumPy |
| --- | --- | --- | --- |
| Spectral | $\|A\|_2$ | $\sigma_{\max}(A)$ | `np.linalg.norm(A, 2)` |
| Column sum | $\|A\|_1$ | $\max_j \sum_i \|a_{i,j}\|$ | `np.linalg.norm(A, 1)` |
| Row sum | $\|A\|_\infty$ | $\max_i \sum_j \|a_{i,j}\|$ | `np.linalg.norm(A, np.inf)` |
| Frobenius | $\|A\|_F$ | $\left(\sum_{i,j} \|a_{i,j}\|^2\right)^{1/2}$ | `np.linalg.norm(A, 'fro')` |

- **Spectral norm.** Denoted $\|A\|_2$, the spectral norm is defined by

$$
\|A\|_2 = \sqrt{\lambda_{\max}(A^*A)} = \sigma_{\max}(A).
$$

Sometimes the subscript 2 is omitted.

- **Maximum absolute column sum norm.** This is denoted $\|A\|_1$ and is defined to be

$$
\|A\|_1 = \max_j \sum_i |a_{i,j}|.
$$

- **Maximum absolute row sum norm.** This is denoted $\|A\|_\infty$ and is defined to be

$$
\|A\|_\infty = \max_i \sum_j |a_{i,j}|.
$$

- **Operator norm.** Every vector norm on $\mathbb{C}^n$ induces a matrix norm on $\mathbb{C}^{n \times n}$. In particular, for the $p$-norms we have this:

$$
\|A\|_p = \max_{\mathbf{x}: \|\mathbf{x}\|_p = 1} \|A\mathbf{x}\|_p.
$$

- **Frobenius norm.** The Frobenius norm of $A$ is denoted $\|A\|_F$. It equals

$$
\|A\|_F = \left( \sum_{i,j} |a_{i,j}|^2 \right)^{\frac{1}{2}}.
$$

It is not a matrix norm (it fails submultiplicativity in general).

### Spectral radius and condition number

- **Spectral radius.** The spectral radius of a square matrix $A$ is denoted $\rho(A)$. It is defined by

$$
\rho(A) = \max \{ |\lambda| : \lambda \text{ is an eigenvalue of } A \}.
$$

- **Condition number.** The condition number of a matrix $A$ is denoted $\kappa(A)$. It equals $\sigma_{\max} / \sigma_{\min}$. A large $\kappa(A)$ means the matrix is "nearly singular" — small perturbations in input cause large perturbations in output. This is why numerical linear algebra cares about conditioning: if $\kappa(A) \approx 10^{16}$, you've lost all your floating-point digits.

### Matrix groups

Certain collections of matrices form a group under matrix multiplication. Here are notations associated with some of these groups.

- **General linear group.** $\mathrm{GL}_n(\mathbb{R})$ is the group of real $n \times n$-matrices that are invertible. The $\mathbb{R}$ can be replaced by $\mathbb{C}$ or other rings/fields.

- **Special linear group.** $\mathrm{SL}_n(\mathbb{R})$ is the group of real $n \times n$-matrices with determinant equal to 1. The $\mathbb{R}$ can be replaced by $\mathbb{C}$ or other rings/fields.

- **Orthogonal group.** $\mathrm{O}(n)$ is the group of real $n \times n$-matrices that are orthogonal, i.e., $U^t U = I$. This may also be written $\mathrm{O}(n, \mathbb{R})$.

The notation $\mathrm{O}(n, \mathbb{C})$ is the set of all complex $n \times n$-matrices $U$ such that $U^*U = I$.

- **Special orthogonal group.** $\mathrm{SO}(n)$ is the subgroup of $\mathrm{O}(n)$ with the added condition that $\det U = 1$. Likewise for $\mathrm{SO}(n, \mathbb{C})$.

These groups are not just abstract algebra — $\mathrm{SO}(3)$ is the group of 3D rotations, fundamental to computer graphics, robotics, and physics. Every time you rotate a 3D model on screen, you're multiplying by an element of $\mathrm{SO}(3)$.

## Tensors

In its simplest form, a tensor is a multidimensional array of numbers. As such, an entry of, say, an order-3 tensor $T$ is $T_{i,j,k}$ or $T_{ijk}$. (Some authors use the word rank instead of order.) Thus scalars are order-0 tensors, vectors are order-1, and matrices are order-2. Higher order tensors are typically written with capital letters in either italics $T$ or boldface $\mathbf{T}$.

If you've used NumPy arrays with more than 2 dimensions — `np.zeros((3, 4, 5))` — you've already worked with tensors. The mathematical formalism below just adds index conventions and a contraction rule.

More abstractly, a tensor is an element of the (repeated) tensor product of a vector space $\mathcal{V}$ with itself and/or its dual space $\mathcal{V}^*$. That is, a type-$(n,m)$ tensor $T$ is an element of

$$
\underbrace{\mathcal{V} \otimes \mathcal{V} \otimes \cdots \otimes \mathcal{V}}_{n \text{ times}} \otimes \underbrace{\mathcal{V}^* \otimes \mathcal{V}^* \otimes \cdots \otimes \mathcal{V}^*}_{m \text{ times}}.
$$

The order of an $(n,m)$-tensor is $n + m$.

An entry in an $(n,m)$-tensor is indicated with $n$ upper indices (written as superscripts) and $m$ lower indices (written as subscripts):

$$
T_{j_1, j_2, \dots, j_m}^{i_1, i_2, \dots, i_n}.
$$

In particular, Kronecker's delta in tensor notation is often seen with one upper and one lower index:

$$
\delta_j^i = \begin{cases} 1 & \text{if } i = j \text{ and } \\ 0 & \text{otherwise.} \end{cases}
$$

### Einstein notation

Einstein notation is often used with tensors. Typically, the repeated index is a lower index in one tensor and an upper index in the other:

$$
T_k^{ij} v^k := \sum_k T_k^{ij} v^k.
$$

The rule is simple: a repeated index (one up, one down) implies summation — you don't write the $\Sigma$. This is exactly what NumPy's `np.einsum` implements: `np.einsum('ijk,k->ij', T, v)` contracts the $k$ index automatically. Einstein notation and `einsum` are the same idea — one for paper, one for code.
