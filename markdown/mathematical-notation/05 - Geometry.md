# Geometry

Around 300 BCE, Euclid sat down and wrote what may be the most influential textbook in history. His *Elements* started from five postulates and built the entire theory of plane geometry through rigorous proof -- no measurements, no approximations, just definitions and deductions. For two thousand years, "doing mathematics" essentially meant "doing geometry in the style of Euclid."

Then in 1637, Descartes had an insight that changed everything: geometry and algebra are the same thing. A point is a pair of numbers. A line is an equation. A circle is $x^2 + y^2 = r^2$. This marriage -- analytic geometry -- is so natural to us now that we forget how revolutionary it was. Every time you plot a function or compute a distance in code, you're using Descartes' idea.

The notation below is the language that makes geometric reasoning compact. If you've worked with coordinate tuples, distance functions, or vector math in code, most of it will feel familiar -- the symbols just formalize what you already do.

## 1. Fundamentals

The most basic geometric object is a point, denoted with upper case letters: $A$, $B$, $C$. Points in the plane can also be represented as 2-tuples $(x,y)$ or as vectors $\begin{bmatrix} x \\ y \end{bmatrix}$; in that case they may be named with lower case bold letters, $\mathbf{x}$, $\mathbf{y}$, and so on.

The entire Euclidean plane is written $\mathbb{R}^{2}$, or $E^{2}$ ($\mathbb{E}^{2}$) for those who prefer a coordinate-free, synthetic view. More generally, $n$-dimensional Euclidean space is $\mathbb{R}^{n}$, $E^{n}$, or $\mathbb{E}^{n}$.

### Lines, rays, and segments

Two distinct points $A$ and $B$ determine a unique line, ray, or segment:

| Object | Notation | Meaning |
| --- | --- | --- |
| Line | $\overleftrightarrow{AB}$ | extends infinitely in both directions |
| Ray | $\overrightarrow{AB}$ | starts at $A$, passes through $B$, continues |
| Segment | $\overline{AB}$ (or simply $AB$) | the finite piece from $A$ to $B$ |
| Length | $\lvert AB \rvert$ or $\lvert \overline{AB} \rvert$ | the distance between $A$ and $B$ |

The length of a segment in coordinates is the distance formula you already know:

$$
\lvert AB \rvert = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}
$$

### Angles

An angle is the union of two rays emanating from the same point. If the rays are $\overrightarrow{AB}$ and $\overrightarrow{AC}$, the angle is written $\angle BAC$ or, when unambiguous, $\angle A$. Angles in diagrams are sometimes labeled with numbers ($\angle 1$) or Greek letters ($\angle\alpha$). The measure of an angle is $m\angle BAC$, though many authors omit the $m$ and let context distinguish an angle from its measure.

### Triangles and standard labeling

A triangle is denoted $\triangle ABC$. By long convention, the sides are named by lower case letters corresponding to the **opposite** angle:

- $a = \lvert BC \rvert$ (opposite $\angle A$)
- $b = \lvert AC \rvert$ (opposite $\angle B$)
- $c = \lvert AB \rvert$ (opposite $\angle C$)

![Figure 5.1: Standard labeling of a triangle.](05 - Geometry_images/img-0.jpeg)

This labeling makes the **law of cosines** compact:

$$
c^{2} = a^{2} + b^{2} - 2ab\cos C
$$

Here $c$ is the length of segment $AB$ and $\cos C$ is the cosine of the (measure of) $\angle C$.

### Geometric relations

| Symbol | Meaning | Example |
| --- | --- | --- |
| $=$ | equality (exactly the same object) | $A = B$ |
| $\cong$ | congruence (same shape and size) | $\angle A \cong \angle Y$ |
| $\sim$ | similarity (same shape, possibly different size) | $\triangle ABC \sim \triangle DEF$ |
| $\parallel$ | parallel | $\overleftrightarrow{AB} \parallel \overleftrightarrow{XY}$ |
| $\perp$ | perpendicular | $\overleftrightarrow{AB} \perp \overleftrightarrow{CD}$ |

### Geometry in SymPy

Every piece of notation above has a direct counterpart in SymPy's geometry module. Points become `Point` objects, distances are method calls, and relations like $\parallel$ and $\perp$ are boolean checks:

```python
<!-- include: code/mathematical-notation/05 - Geometry/01_python.py -->
```

The mapping is almost one-to-one: $\lvert AB \rvert$ becomes `A.distance(B)`, $\triangle ABC$ becomes `Triangle(A, B, C)`, $\overleftrightarrow{AB} \perp \overleftrightarrow{CD}$ becomes `line_AB.is_perpendicular(line_CD)`. Notation is a compression of operations you can run.

## 2. Coordinates

In analytic geometry, points are specified by a list of numbers. The most common system is **Cartesian coordinates** (rectangular coordinates), named for Descartes. Points are written as $d$-tuples: $(x, y)$ in 2D, $(x, y, z)$ in 3D. In higher dimensions, subscripts are the natural choice: $(x_1, x_2, x_3, x_4)$.

The Cartesian convention is not the only coordinate system. Different geometries suggest different representations:

### Polar coordinates

In the plane, a point can be specified by its distance from a fixed origin and a rotation from the positive $x$-axis. The notation uses $(r, \theta)$ where $r$ is the distance and $\theta$ is the rotation:

$$
x = r \cos \theta \quad \text{and} \quad y = r \sin \theta
$$

### Spherical coordinates

Spherical (or spherical polar) coordinates extend polar coordinates to 3D. Each point is specified by:

- $r$ -- distance from the origin
- $\theta$ -- azimuth (rotation from the $+x$-axis in the $xy$-plane)
- $\phi$ -- inclination (polar angle from the $z$-axis)

The point is written $(r, \theta, \phi)$. (Beware: some authors swap the order of $\theta$ and $\phi$.)

$$
x = r \cos \theta \sin \phi, \quad y = r \sin \theta \sin \phi, \quad z = r \cos \phi
$$

### Cylindrical coordinates

Cylindrical coordinates locate a point in the $xy$-plane by polar coordinates $(r, \theta)$, then add a height $z$. The full specification is $(r, \theta, z)$:

$$
x = r \cos \theta, \quad y = r \sin \theta, \quad z = z
$$

### Coordinate summary

| System | Notation | Parameters | Use case |
| --- | --- | --- | --- |
| Cartesian | $(x, y)$ or $(x, y, z)$ | distances along axes | default; linear problems |
| Polar | $(r, \theta)$ | distance, angle | radial symmetry in 2D |
| Spherical | $(r, \theta, \phi)$ | distance, azimuth, inclination | radial symmetry in 3D |
| Cylindrical | $(r, \theta, z)$ | distance, angle, height | axial symmetry (pipes, columns) |

## 3. Differential geometry

### Curves

A curve is (the image of) a continuous function $\alpha : [a,b] \to \mathbb{R}^{k}$. The parameterization is **unit speed** if $\|\alpha'(s)\| = 1$ for all $s \in [a,b]$.

Associated with curves are the following notations:

| Symbol | Name | Definition (unit speed) |
| --- | --- | --- |
| $\mathbf{T}(s)$ | tangent vector | $\mathbf{T}(s) = \alpha'(s)$ |
| $\mathbf{N}(s)$ | normal vector | $\mathbf{N}(s) = \mathbf{T}'(s) / \|\mathbf{T}'(s)\|$ |
| $\mathbf{B}(s)$ | binormal vector | $\mathbf{B}(s) = \mathbf{T}(s) \times \mathbf{N}(s)$ (in $\mathbb{R}^3$) |
| $\kappa(s)$ | curvature | $\kappa(s) = \|\mathbf{T}'(s)\|$ |
| $\tau(s)$ | torsion | $\tau(s) = -\mathbf{B}'(s) \cdot \mathbf{N}(s)$ |

The triple $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ is the **Frenet-Serret frame** -- an orthonormal basis that "rides along" the curve. Curvature $\kappa$ measures how fast the curve turns; torsion $\tau$ measures how fast it twists out of a plane.

### Surfaces

Various geometric surfaces have their own notation:

| Surface | Notation | Notes |
| --- | --- | --- |
| $k$-sphere | $S^k$ | $S^1$ = circle, $S^2$ = sphere |
| Ball | $B(\mathbf{x}, r) = \{\mathbf{y} : \|\mathbf{y} - \mathbf{x}\| \leq r\}$ | closed ball centered at $\mathbf{x}$ |
| Torus | $T^2$, $S^1 \times S^1$, $\mathbb{R}^2 / \mathbb{Z}^2$ | surface of a doughnut |
| Projective plane | $\mathbb{RP}^2$ | real projective plane |
| Hyperbolic plane | $\mathbb{H}^2$ | constant negative curvature |

### The Euler characteristic and Gauss-Bonnet

The **Euler characteristic** of a surface $M$ is denoted $\chi(M)$. If a connected graph is embedded on $M$ so that every face is homeomorphic to a disc, then:

$$
\chi(M) = \nu - e + f
$$

where $\nu$ is the number of vertices, $e$ the number of edges, and $f$ the number of faces. (For a sphere: $\chi(S^2) = 2$. For a torus: $\chi(T^2) = 0$.)

The **Gaussian curvature** at a point $p$ on a surface is $K(p)$. It is the product of the two principal curvatures: $K = k_1 k_2$.

The **Gauss-Bonnet formula** connects curvature to topology:

$$
\int_{M} K \, dA = 2\pi \chi(M)
$$

This is one of the deepest results in geometry: the total curvature of a surface is determined entirely by its topology, not its specific shape. A sphere can be stretched, dented, or deformed in any way -- as long as you don't tear or glue it, the integral of $K$ over the whole surface is always $4\pi$.
