<!-- page 1 -->

Chapter 5 Geometry

### 1. Fundamentals

The most basic geometric object is a point and points are often denoted with upper case letters, $A$, $B$, $C$, etc. However, points in the plane can be represented as 2-tuples $(x,y)$ or as vectors $[\,{}^{s}_{y}\,$]; as such, they may be named like vectors with lower case bold letters, $\mathbf{x}$, $\mathbf{y}$, and so on. The entire Euclidean plane may be written as $\mathbb{R}^{2}$, but for those who prefer to think of the plane in a coordinate-free, synthetic way, we may write $E^{2}$ or $\mathbb{E}^{2}$. More generally, $n$-dimensional Euclidean space is $\mathbb{R}^{n}$, $E^{n}$, or $\mathbb{E}^{n}$.

Two distinct points $A$ and $B$ determine a unique line which is typically denoted $\overleftrightarrow{AB}$. The ray emanating from $A$ and including $B$ is denoted $\overrightarrow{AB}$. The line segment joining $A$ and $B$ is denoted $\overrightarrow{AB}$, however, for simplicity’s sake, some people write $AB$ for the line segment. Line segments have length which can be denoted in various ways including the same notation as for the segment itself ($AB$ or $\overrightarrow{AB}$) or with absolute value bars, $|AB|$ or $|\overrightarrow{AB}|$.

An angle is the union of two rays emanating from the same point. If the rays are $\overrightarrow{AB}$ and $\overrightarrow{AC}$, the angle can be denoted $\angle BAC$ or, if there is only one angle with vertex $A$ under consideration, $\angle A$. Sometimes angles in diagrams are marked with numbers or Greek letters, so one may see $\angle 1$ or $\angle\alpha$. The measure of an angle is written $m\angle BAC$, but some people omit the $m$ and use the same notation for an angle and its measure.

A triangle is the union of three line segments determined by three points and is denoted $\triangle ABC$.

In a triangle, the angles are named by their vertex points ($\angle A$, $\angle B$, $\angle C$) and the lengths of the sides are named by lower case letters corresponding to the opposite angle. That is, $a$ is the length of the segment opposite $\angle A$ (the length of the segment $\overrightarrow{BC}$). See Figure 5.1. A classic example of this is the law of cosines:

$c^{2}=a^{2}+b^{2}-2ab\cos C.$

Here $c$ is the length of the segment $AB$ and $\cos C$ is the cosine of the (measure of) $\angle C$.

There are some standard relation symbols for geometric objects. The most basic is equality, denoted with an equals sign $=$, which means the two things are exactly the same. More generally, two geometric figures are congruent if there

---

<!-- page 2 -->

\S 5.2
- Coordinates

![img-0.jpeg](05 - Geometry_images/img-0.jpeg)
FIGURE 5.1. Standard labeling of a triangle.

is an isometry of space that equates one with the other. Congruence of figures is denoted with the symbol  $\cong$ , e.g.,  $\angle A \cong \angle Y$ . More general still is similarity of figures which is denoted  $\sim$ , e.g.,  $\triangle ABC \sim \triangle DEF$ .

Lines, rays, and segments may be parallel; this is denoted  $\overleftrightarrow{AB} \parallel \overleftrightarrow{XY}$ . They may also be perpendicular:  $\overleftrightarrow{AB} \perp \overleftrightarrow{CD}$ .

# 2. Coordinates

In analytic geometry, points are specified by a list of numbers. The most common system for doing this is known as Cartesian coordinates (also called rectangular coordinates). Points are specified by  $d$ -tuples (i.e., lists of  $d$  numbers) either written horizontally  $(x,y)$  or vertically  $[x^y]$ . It is traditional to use the letters  $x$  and  $y$  for Cartesian coordinates in two dimensions and  $x, y,$  and  $z$  in three dimensions. In higher dimensions, it is easiest to use subscripts, e.g.,  $(x_1, x_2, x_3, x_4)$ .

The Cartesian convention is not the only system of coordinates. Here are a few others for 2- and 3-dimensional space and their associated notation.

- Polar coordinates. In the plane, points may be specified by a distance from a fixed origin and a rotation from a ray emanating from that origin (typically the positive  $x$ -axis). It is traditional to use the letters  $(r,\theta)$  where  $r$  is the distance and  $\theta$  is the rotation. The relation to Cartesian coordinates is

$$
x = r \cos \theta \quad \text {and} \quad y = r \sin \theta .
$$

- Spherical coordinates. Spherical coordinates, also known as spherical polar coordinates, are a natural extension of polar coordinates to three-dimensional space. Each point is specified by a distance  $r$  from the origin, a first rotation clockwise  $\theta$  from the  $+x$ -axis in the  $xy$ -plane, and a second rotation  $\phi$  out of the  $xy$ -plane.

The point is written  $(r,\theta ,\phi)$  and  $\theta$  is called the azimuth and  $\phi$  is called the inclination or polar angle. However, some authors use a different order for the two angles in the triple.

The conversion from spherical to Cartesian coordinates is given by these formulas:

$$
x = r \cos \theta \sin \phi , \quad y = r \sin \theta \sin \phi , \quad \text {and} \quad z = r \cos \phi .
$$

---

<!-- page 3 -->

Geometry

- Cylindrical coordinates. This is another extension of polar coordinates. Points in space are first located in the $x,y$-plane by polar coordinates $(r,\theta)$ and then a height above that plane by $z$. Thus the full specification is the triple $(r,\theta,z)$.

The conversion to Cartesian coordinates is

$x=r\cos\theta,\quad y=r\sin\theta,\quad\text{and}\quad z=z.$

## 3 Differential geometry

Curves. A curve is (the image of) a continuous function $\alpha:[a,b]\to\mathbb{R}^{k}$. This parameterization is unit speed if $\|\alpha^{\prime}(s)\|=1$ for all $s\in[a,b]$.

Associated with curves are the following notations:

- $\mathbf{T}(s)$ is the tangent vector at $\alpha(s)$. For a unit speed curve, we have $\mathbf{T}(s)=\alpha^{\prime}(s)$.
- $\mathbf{N}(s)$ is the normal vector at $\alpha(s)$. For a unit speed curve, we have $\mathbf{N}(s)=T^{\prime}(s)/\|T^{\prime}(s)\|$.
- $\mathbf{B}(s)$ is the binormal vector at $\alpha(s)$. For a curve in $\mathbb{R}^{3}$, we have $\mathbf{B}(s)=\mathbf{T}(s)\times\mathbf{N}(s)$.
- $\kappa(s)$ is the curvature of the curve at $\alpha(s)$. For a unit speed curve, $\kappa(s)=\|T^{\prime}(s)\|$.
- $\tau(s)$ is the torsion of the space curve at $\alpha(s)$. It is given by the formula $\tau(s)=-\mathbf{B}^{\prime}(s)\cdot\mathbf{N}(s)$.

Surfaces. Various geometric surfaces have special notation used to describe them.

- Spheres. The sphere is $S^{2}$. In general $S^{k}$ is a $k$-dimensional sphere, so $S^{1}$ is a circle.

A sphere is the boundary of a ball. The notation $B(\mathbf{x},r)$ is often used for the ball centered at $\mathbf{x}$ with radius $r$, i.e., $B(\mathbf{x},r)=\{\mathbf{y}:\|\mathbf{y}-\mathbf{x}\|\leq r\}$.
- Torus. The following notations are used to denote a torus (the surface of a doughnut): $T^{2}$, $S^{1}\times S^{1}$, and $\mathbb{R}^{2}/\mathbb{Z}^{2}$.
- Projective plane. The (real) projective plane is denote $\mathbb{RP}^{2}$.
- Hyperbolic plane. The hyperbolic plane is denoted $\mathbb{H}^{2}$.

The Euler characteristic of a surface $M$ is denoted $\chi(M)$. If a connected graph is embedded on the surface of $M$ so that every face is homeomorphic to the interior of a disc, then $\chi(M)=\nu-e+f$ where $\nu$ is the number of vertices, $e$ is the number of edges, and $f$ is the number of faces.

The Gaussian curvature at a point $p$ on a surface is denoted $K(p)$. The Gaussian curvature of a compact, boundaryless surface $M$ is related to the Euler characteristic by the Gauss-Bonnet formula

$\int_{M}K\,dA=2\pi\chi(M)$

---

<!-- page 4 -->

\S 5.3
\bullet
Differential geometry

where  $dA$  is an element of surface area.

Gaussian curvature is related to the principal curvatures of the surface, which are denoted  $k_{1}$  and  $k_{2}$ , by the equation  $K = k_{1}k_{2}$ .