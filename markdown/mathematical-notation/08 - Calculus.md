# Calculus

In the 1660s, Isaac Newton and Gottfried Wilhelm Leibniz independently invented calculus — and then spent the rest of their lives fighting over who deserved the credit. The priority dispute was bitter, personal, and conducted through proxies in the Royal Society. But mathematically, the most lasting consequence wasn't about who was first. It was about *notation*.

Newton wrote derivatives as dots over letters: $\dot{x}$, $\ddot{x}$. His notation was compact but limited — it tied differentiation to time and scaled poorly beyond two derivatives. Leibniz wrote $\frac{dx}{dt}$, $\frac{d^2x}{dt^2}$, treating derivatives as ratios of infinitesimal quantities. His notation was heavier on the page but far more flexible: it made the chain rule look like fraction cancellation ($\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$), and it generalized naturally to partial derivatives, higher dimensions, and integrals.

The remarkable outcome: *both notations survived*. Physicists still write $\dot{x}$ and $\ddot{x}$ for velocity and acceleration. Everyone else uses Leibniz's $dx/dt$. And Lagrange added a third — the prime notation $f'(x)$ — that splits the difference. You'll encounter all three, sometimes in the same textbook.

This chapter catalogs the notation for limits, derivatives, integrals, and transforms — the four pillars of calculus — with the programming bridges that make each symbol executable.

## 1. Limits

The principal notation for limits is

$$
\lim_{x \to a} f(x)
$$

which stands for the limit of $f(x)$ as $x$ approaches $a$.

One sided limits have the notation

$$
\lim_{x \to a^-} f(x) = \lim_{x \uparrow a} f(x)
$$

for the limit of $f(x)$ as $x$ approaches $a$ from the left and

$$
\lim_{x \to a^+} f(x) = \lim_{x \downarrow a} f(x)
$$

for the limit of $f(x)$ as $x$ approaches $a$ from the right. We also have limits in which the variable increases or decreases without bound:

$$
\lim_{x \to \infty} f(x) \quad \text{and} \quad \lim_{x \to -\infty} f(x).
$$

For a sequence $a_1, a_2, a_3, \ldots$ we also use the notation

$$
\lim_{n \to \infty} a_n
$$

to express the limiting value of the sequence. In addition we have

$$
\limsup_{n \to \infty} a_n = \lim_{n \to \infty} \left[ \sup \{a_k : k \geq n \} \right] \quad \text{and}
$$

$$
\liminf_{n \to \infty} a_n = \lim_{n \to \infty} \left[ \inf \{a_k : k \geq n \} \right].
$$

We may also write $\varlimsup$ for $\limsup$ and $\varliminf$ for $\liminf$.

## 2. Derivatives (single variable)

Given a function $f$, we have three standard notations for the derivative — each born from the priority dispute:

| Notation | Name | Origin | Best for |
| --- | --- | --- | --- |
| $f'(x)$ | Lagrange (prime) | Joseph-Louis Lagrange, 1797 | Quick shorthand, abstract arguments |
| $\frac{df}{dx}$ | Leibniz | Gottfried Leibniz, 1684 | Chain rule, substitution, integrals |
| $\dot{x}$ | Newton (fluxion) | Isaac Newton, 1690s | Time derivatives in physics |
| $Df$ | Operator | Augustin-Louis Cauchy / Oliver Heaviside | Differential equations, functional analysis |

### Lagrange (prime) notation

The derivative is $f'$, the second derivative is $f''$, the third is $f'''$. Sometimes lower case roman numerals replace multiple prime marks, e.g. $f^{(\mathrm{iv})}$. For a positive integer $n$, the $n^{\mathrm{th}}$ derivative may be written $f^{(n)}$.

The value at a specific point is simply $f'(a)$.

### Leibniz notation

Higher order derivatives in Leibniz's notation use exponents on the $d$:

$$
\frac{df}{dx}, \quad \frac{d^{2}f}{dx^{2}}, \quad \frac{d^{3}f}{dx^{3}}, \quad \dots
$$

The $n^{\mathrm{th}}$ derivative is written $\frac{d^n f}{dx^n}$. Some authors use a roman $\mathrm{d}$ instead of italic $d$: $\frac{\mathrm{d}f}{\mathrm{d}x}$.

The value at a specific point requires the evaluation bar:

$$
\left. \frac{df}{dx} \right|_{x = a}
$$

The genius of this notation is how it makes the chain rule look like fraction cancellation. If $y = f(u)$ and $u = g(x)$, then:

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

This isn't *really* fraction cancellation (these aren't fractions), but the notation makes the rule impossible to forget.

### Newton (dot) notation

Suppose $y$ is a function of $t$ (which often represents time). Then $\dot{y}$ denotes the derivative $dy/dt$. Likewise $\ddot{y}$ is the second derivative $d^2 y/dt^2$. You'll see this almost exclusively in physics and engineering — Newton's original context.

### Operator notation

The notation $\frac{d}{dx}$ means "the derivative of." It is also denoted with a simple capital $D$:

$$
\frac{d}{dx} \left[ x^{2} - 3x + 2 \right] = D \left[ x^{2} - 3x + 2 \right] = 2x - 3.
$$

Higher order derivatives are denoted as $\frac{d^n}{dx^n}$ or $D^n$.

### Notation-to-code mapping

Every notation variant maps to the same SymPy function — `diff`. The integral sign $\int$ maps to `integrate`. These two functions are the executable versions of Leibniz's notation:

| Math notation | SymPy code | Result |
| --- | --- | --- |
| $\frac{d}{dx} x^3$ | `diff(x**3, x)` | $3x^2$ |
| $\frac{d^2}{dx^2} x^3$ | `diff(x**3, x, 2)` | $6x$ |
| $\int \sin x\, dx$ | `integrate(sin(x), x)` | $-\cos x$ |
| $\int_0^\infty e^{-x}\, dx$ | `integrate(exp(-x), (x, 0, oo))` | $1$ |
| $\frac{\partial f}{\partial x}$ | `diff(f, x)` | partial derivative |

```python
<!-- include: code/mathematical-notation/08 - Calculus/01_python.py -->
```

### Vector-valued functions

The notations for the derivative of a vector-valued function of a single variable are the same as for that of a single-valued function. Let $f\colon \mathbb{R}\to \mathbb{R}^n$. Then the derivative of $f$ is denoted either $f'$ or $df/dt$ (or $df/dx$). Higher order derivatives are, likewise, $f''$ and $d^2 f/dt^2$, and so forth.

## 3. Derivatives (multiple variables, scalar-valued)

When a function depends on two or more variables, the ordinary $d$ becomes the "curly $d$" — the partial derivative symbol $\partial$, introduced by Adrien-Marie Legendre in 1786.

### Partial derivatives

Suppose $f\colon \mathbb{R}^n\to \mathbb{R}$. Then the partial derivative of $f$ with respect to its $j^{\mathrm{th}}$ argument is

$$
\frac{\partial f}{\partial x_{j}}.
$$

When $f$ is a function of (say) just two variables $x$ and $y$, then the partial derivatives can also be written as $f_{x} = \partial f / \partial x$ and $f_{y} = \partial f / \partial y$. Another notation is $\partial_x f$.

All four notations for the same thing:

$$
D_{x} f = \partial_{x} f = f_{x} = \frac{\partial f}{\partial x}.
$$

More generally, if $\mathbf{v}$ is a unit vector then $D_{\mathbf{v}}$ is the derivative of $f$ in the $\mathbf{v}$ direction; this is known as a directional derivative.

### Higher order partial derivatives

Higher order partial derivatives are denoted like this:

$$
\frac{\partial^{2} f}{\partial x_{i} \partial x_{j}}
$$

which means to first take the partial derivative of $f$ with respect to $x_{j}$ and then the partial derivative of that result with respect to $x_{i}$. In symbols:

$$
\frac{\partial^{2} f}{\partial x_{i} \partial x_{j}} = \frac{\partial}{\partial x_{i}} \left(\frac{\partial f}{\partial x_{j}}\right).
$$

For most functions likely to be encountered in science and engineering the order of differentiation does not matter (Clairaut's theorem: if the mixed partials are continuous, $f_{xy} = f_{yx}$).

For a function of (say) two variables $x$ and $y$, the higher order partials can be written like this: $f_{xx}, f_{xy}, f_{yx}, f_{yy}$.

### Gradient

The gradient of a function $f: \mathbb{R}^n \to \mathbb{R}$ is the vector of partial derivatives:

$$
\nabla f = \left[ \begin{array}{c} \frac{\partial f}{\partial x_{1}} \\ \frac{\partial f}{\partial x_{2}} \\ \vdots \\ \frac{\partial f}{\partial x_{n}} \end{array} \right].
$$

It is denoted either $\operatorname{grad} f$ or $\nabla f$. The gradient points in the direction of steepest ascent — this is why gradient *descent* moves in the direction $-\nabla f$.

For a function $f$ of three variables, the gradient can be expressed in $\mathbf{i}, \mathbf{j}, \mathbf{k}$-notation like this:

$$
\operatorname{grad} f = \nabla f = f_{x} \mathbf{i} + f_{y} \mathbf{j} + f_{z} \mathbf{k}.
$$

### Gradient and Hessian in JAX

JAX's `grad` function computes $\nabla f$ by automatic differentiation — it traces the computation graph and applies the chain rule mechanically. No symbolic algebra, just numerical derivatives at machine precision. `jax.hessian` computes the full matrix of second partials:

```python
<!-- include: code/mathematical-notation/08 - Calculus/02_python.py -->
```

The SymPy demo above computed $\frac{\partial f}{\partial x} = 2xy$ as a symbolic expression. JAX computes the same derivative *numerically* at a specific point: at $(1, 2)$, $2 \cdot 1 \cdot 2 = 4$... wait, that's $\frac{\partial}{\partial x}[x^2 y + y^3]$. The JAX demo uses a different function ($x^3 + 2xy + y^2$), giving $\nabla f = [3x^2 + 2y,\; 2x + 2y] = [7, 6]$ at $(1, 2)$. Two tools, same notation, complementary strengths: SymPy gives you the formula, JAX gives you the number.

### Laplacian

The Laplacian operator is denoted with a capital $\Delta$ (or $\nabla^2$). For $f: \mathbb{R}^n \to \mathbb{R}$ we have

$$
\Delta f = \nabla^2 f = \sum_{i = 1}^{n} \frac{\partial^{2} f}{\partial x_{i}^{2}}
$$

or more simply for a function of three variables,

$$
\Delta f = \frac{\partial^{2} f}{\partial x^{2}} + \frac{\partial^{2} f}{\partial y^{2}} + \frac{\partial^{2} f}{\partial z^{2}}.
$$

The Laplacian measures how much a function at a point differs from its average in a neighborhood — it's the continuous analog of "the value at this node minus the average of its neighbors" in a graph.

### Hessian

For a function $f: \mathbb{R}^n \to \mathbb{R}$, we can form an $n \times n$-matrix of its partial second derivatives. This matrix is the Hessian matrix of $f$:

$$
H f = \left[ \begin{array}{cccc} \frac{\partial^{2} f}{\partial x_{1}^2} & \frac{\partial^{2} f}{\partial x_{1} \partial x_{2}} & \dots & \frac{\partial^{2} f}{\partial x_{1} \partial x_{n}} \\ \frac{\partial^{2} f}{\partial x_{2} \partial x_{1}} & \frac{\partial^{2} f}{\partial x_{2}^2} & \dots & \frac{\partial^{2} f}{\partial x_{2} \partial x_{n}} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial^{2} f}{\partial x_{n} \partial x_{1}} & \frac{\partial^{2} f}{\partial x_{n} \partial x_{2}} & \dots & \frac{\partial^{2} f}{\partial x_{n}^2} \end{array} \right].
$$

The Hessian tells you about curvature. If the Hessian is positive definite at a critical point ($\nabla f = 0$), you're at a local minimum — this is the second-derivative test generalized to $n$ dimensions. In machine learning, the Hessian of the loss function characterizes the local geometry of the optimization landscape.

## 4. Derivatives (multiple variables, vector-valued)

In this section we consider derivatives of functions $\mathbf{f}:\mathbb{R}^m\to \mathbb{R}^n$. We denote vector-valued functions with bold letters (though this is not mandatory).

Such functions map a vector $\mathbf{x} \in \mathbb{R}^m$ to a vector $\mathbf{y} \in \mathbb{R}^n$. This can be simply written $\mathbf{y} = \mathbf{f}(\mathbf{x})$ or separated into components:

$$
\mathbf{f}(\mathbf{x}) = \left[ \begin{array}{c} f_{1}(\mathbf{x}) \\ f_{2}(\mathbf{x}) \\ \vdots \\ f_{n}(\mathbf{x}) \end{array} \right]
$$

where $f_{j}(\mathbf{x})$ denotes the $j^{\mathrm{th}}$ component of the vector $\mathbf{f}(\mathbf{x})$.

### Partial derivatives

Partial derivatives of $\mathbf{f}$ typically specify both the component function and the variable with respect to which the function is being differentiated:

$$
\frac{\partial f_{i}}{\partial x_{j}}.
$$

Some people express this partial derivative as $f_{i,j}$.

One can take the partial derivative of all components of $\mathbf{f}$ with respect to a single variable:

$$
\frac{\partial \mathbf{f}}{\partial x_{j}} = \left[ \begin{array}{c} \frac{\partial f_{1}}{\partial x_{j}} \\ \frac{\partial f_{2}}{\partial x_{j}} \\ \vdots \\ \frac{\partial f_{n}}{\partial x_{j}} \end{array} \right]
$$

This vector of partial derivatives can be written $f_{,j}$. One needs to be careful with this notation as the comma may be difficult to notice.

### Jacobian

The matrix of all partial derivatives is called the Jacobian matrix of $f$ and is simply denoted $D\mathbf{f}$:

$$
D\mathbf{f} = \left[ \begin{array}{cccc} \frac{\partial f_{1}}{\partial x_{1}} & \frac{\partial f_{1}}{\partial x_{2}} & \dots & \frac{\partial f_{1}}{\partial x_{m}} \\ \frac{\partial f_{2}}{\partial x_{1}} & \frac{\partial f_{2}}{\partial x_{2}} & \dots & \frac{\partial f_{2}}{\partial x_{m}} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial f_{n}}{\partial x_{1}} & \frac{\partial f_{n}}{\partial x_{2}} & \dots & \frac{\partial f_{n}}{\partial x_{m}} \end{array} \right] = \left[ \begin{array}{cccc} f_{1,1} & f_{1,2} & \dots & f_{1,m} \\ f_{2,1} & f_{2,2} & \dots & f_{2,m} \\ \vdots & \vdots & \ddots & \vdots \\ f_{n,1} & f_{n,2} & \dots & f_{n,m} \end{array} \right].
$$

The Jacobian is the multivariate generalization of the derivative. Where the derivative of $f: \mathbb{R} \to \mathbb{R}$ is a number (the slope), the Jacobian of $\mathbf{f}: \mathbb{R}^m \to \mathbb{R}^n$ is an $n \times m$ matrix — the best linear approximation to $\mathbf{f}$ near a point. In JAX, `jax.jacobian(f)` computes this entire matrix.

If $\mathbf{f}:\mathbb{R}^n\to \mathbb{R}^n$, then $D\mathbf{f}$ is a square matrix; its determinant is, unfortunately, also called the Jacobian of $\mathbf{f}$.

One can think of $\mathbf{f}:\mathbb{R}^n\to \mathbb{R}^n$ as a change of coordinate systems. If the original coordinates are, say, $(x,y,z)$, then $\mathbf{f}(x,y,z) = (u,v,w)$ are the coordinates of the point in the alternative system. Then the (determinant of the) Jacobian of $\mathbf{f}$ is also denoted:

$$
\left| \frac{\partial(u, v, w)}{\partial(x, y, z)} \right| = \det \left[ \begin{array}{ccc} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} & \frac{\partial u}{\partial z} \\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} & \frac{\partial v}{\partial z} \\ \frac{\partial w}{\partial x} & \frac{\partial w}{\partial y} & \frac{\partial w}{\partial z} \end{array} \right].
$$

### Curl

For a function $\mathbf{f}:\mathbb{R}^3\to \mathbb{R}^3$ the *curl* of $\mathbf{f}$ is

$$
\operatorname{curl} \mathbf{f} = \nabla \times \mathbf{f} = \left[ \begin{array}{l} f_{3,2} - f_{2,3} \\ f_{1,3} - f_{3,1} \\ f_{2,1} - f_{1,2} \end{array} \right]
$$

where $f_{1,2}$ means the partial derivative of $f_{1}$ in its second argument, i.e., $\partial f_1 / \partial x_2$.

The notation $\nabla \times \mathbf{f}$ is inspired by the cross product in which the first "vector" is a list of operators:

$$
\nabla \times \mathbf{f} = \left[ \begin{array}{c} \frac{\partial}{\partial x_{1}} \\ \frac{\partial}{\partial x_{2}} \\ \frac{\partial}{\partial x_{3}} \end{array} \right] \times \left[ \begin{array}{c} f_{1} \\ f_{2} \\ f_{3} \end{array} \right].
$$

### Divergence

For a function $\mathbf{f}:\mathbb{R}^3\to \mathbb{R}^3$, the *divergence* of $\mathbf{f}$ is

$$
\operatorname{div} \mathbf{f} = \nabla \cdot \mathbf{f} = \frac{\partial f_{1}}{\partial x_{1}} + \frac{\partial f_{2}}{\partial x_{2}} + \frac{\partial f_{3}}{\partial x_{3}}.
$$

Like the notation for curl, this notation is inspired by the dot product in which the first "vector" is a list of operators:

$$
\nabla \cdot \mathbf{f} = \left[ \begin{array}{c} \frac{\partial}{\partial x_{1}} \\ \frac{\partial}{\partial x_{2}} \\ \frac{\partial}{\partial x_{3}} \end{array} \right] \cdot \left[ \begin{array}{c} f_{1} \\ f_{2} \\ f_{3} \end{array} \right].
$$

More generally, for $\mathbf{f}:\mathbb{R}^n\to \mathbb{R}^n$,

$$
\operatorname{div} \mathbf{f} = \nabla \cdot \mathbf{f} = \sum_{j = 1}^{n} \frac{\partial f_{j}}{\partial x_{j}}.
$$

### The $\nabla$ operator unifies gradient, divergence, and Laplacian

Note that for the scalar valued function $f: \mathbb{R}^n \to \mathbb{R}$, the gradient of $f$, denoted $\nabla f$, is the vector of $f$'s partial derivatives, and so $\nabla f: \mathbb{R}^n \to \mathbb{R}^n$. If we take the divergence of $\nabla f$ we have

$$
\nabla \cdot (\nabla f) = \sum_{j = 1}^{n} \frac{\partial^{2} f}{\partial x_{j}^{2}}
$$

which is the Laplacian of $f$. Thus $\nabla \cdot (\nabla f) = \nabla^2 f = \Delta f$. Three different notations, one operation — the pattern of this chapter in miniature.

| Operation | Notation | Input | Output | $\nabla$ form |
| --- | --- | --- | --- | --- |
| Gradient | $\nabla f$ | scalar field | vector field | $\nabla$ applied to scalar |
| Divergence | $\nabla \cdot \mathbf{f}$ | vector field | scalar field | $\nabla$ dot vector |
| Curl | $\nabla \times \mathbf{f}$ | vector field ($\mathbb{R}^3$) | vector field | $\nabla$ cross vector |
| Laplacian | $\nabla^2 f$ | scalar field | scalar field | $\nabla \cdot \nabla f$ |

## 5. Integration

The integral sign $\int$ was introduced by Leibniz in 1675 — it's a stylized elongated S, for *summa* (sum). And that's exactly what integration is: a limit of sums.

### Indefinite and definite integrals

Let $f: \mathbb{R} \to \mathbb{R}$. The notation $\int f(x) \, dx$ is the indefinite integral of $f$; it is a function $F$ whose derivative is $f$. The function $F$ is called an antiderivative or a primitive of $f$. The notation

$$
\int_{a}^{b} f(x) \, dx
$$

is the definite integral of $f$ and its value can be expressed

$$
F(x) \Big|_{a}^{b} = F(b) - F(a)
$$

where $F$ is an antiderivative of $f$. Some authors use a roman $\mathrm{d}$ in the integral, like this: $\int f(x) \, \mathrm{d}x$.

The left and right end points of the interval over which a function is integrated may be $-\infty$ and $\infty$, respectively.

### Multiple integrals

Multiple integrals take the following form:

$$
\iint f(x, y) \, dx \, dy.
$$

This means we integrate $f(x, y)$ first with respect to $x$ (holding $y$ constant), and then integrate the resulting expression with respect to $y$. It is equivalent to

$$
\int \left[ \int f(x, y) \, dx \right] \, dy.
$$

This is not equivalent to $\iint f(x,y) \, dy \, dx$, although the end result is often the same (Fubini's theorem gives conditions under which you can swap the order).

### Domain subscripts

Subscripts on integrals indicate the domain of integration. The typical notation is

$$
\int_{A} f \, ds
$$

where $A$ is a set. Some examples:

$$
\int_{[0,1]} x^{2} \, dx \text{ means } \int_{0}^{1} x^{2} \, dx
$$

$$
\int_{\mathbb{R}} \exp \left\{- x^{2} \right\} \, dx \text{ means } \int_{-\infty}^{\infty} e^{-x^{2}} \, dx
$$

$$
\int_{[0,1]^{2}} (x - y)^{2} \, dx \, dy \text{ means } \int_{0}^{1} \int_{0}^{1} (x - y)^{2} \, dx \, dy
$$

### Line and contour integrals

When the subscript on the integral is a curve

$$
\int_{\gamma} f \, ds
$$

denotes the line integral of $f$ along the curve $\gamma$.

If the curve is closed (i.e., it begins and ends at the same point) then we write

$$
\oint_{\gamma}f\,ds
$$

for the line integral. (The subscript indicating the name of the curve may be omitted if it is clear from context.) In this case, the line integral may also be called a contour integral. When the contour is the boundary of a domain $D$, the following notation may be used:

$$
\int_{\partial D}f\,ds\quad\text{or}\quad\oint_{\partial D}f\,ds
$$

where $\partial D$ indicates the boundary of $D$.

## 6. Convolution and transforms

### Convolution

If $f$ and $g$ are functions from $\mathbb{R}$ to $\mathbb{R}$, we define their convolution $f*g$ as a new function with

$$
(f*g)(x)=\int_{-\infty}^{\infty}f(t)g(x-t)\,dt.
$$

The convolution integral need not be computed over the entire real line. Sometimes, it is computed just on an interval especially if the functions $f$ and $g$ are periodic. The interval over which we integrate can be arbitrary:

$$
(f*g)(x)=\int_{a}^{b}f(t)g(x-t)\,dt.
$$

Common intervals include $[0,1]$, $[-\pi,\pi]$, and $[0,2\pi]$.

In some cases, we normalize the integral by dividing by the length of the interval:

$$
(f*g)(x)=\frac{1}{b-a}\int_{a}^{b}f(t)g(x-t)\,dt.
$$

The notion of convolution (and the use of the symbol $*$) extends to other realms. For example, given sequences $a=(a_{0},a_{1},a_{2},\ldots)$ and $b=(b_{0},b_{1},b_{2},\ldots)$, their convolution is a new sequence $c=a*b$ with

$$
c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}.
$$

Similarly, in number theory, the convolution of two functions $f,g:\mathbb{Z}^{+}\to\mathbb{R}$ is $f*g$ with

$$
(f*g)(n)=\sum_{d|n}f(d)g(n/d).
$$

If you've used a convolutional neural network, the operation is the same idea: slide one function across another, multiplying and summing at each position. The $*$ in `nn.Conv2d` is literally this $*$.

### Laplace transform

Let $f: \mathbb{R}_+ \to \mathbb{R}$. The Laplace transform of $f$ is denoted $\mathcal{L}f$. It is a new function defined on the nonnegative real numbers by

$$
(\mathcal{L}f)(s) = \int_{0}^{\infty} f(t)e^{-st} dt.
$$

The inverse Laplace transform is denoted $\mathcal{L}^{-1}$.

### Fourier transform

Let $f: \mathbb{R} \to \mathbb{R}$ (or, more generally, $f: \mathbb{R} \to \mathbb{C}$). The Fourier transform of $f$ is denoted $\mathcal{F}f$. This is a new function $F: \mathbb{R} \to \mathbb{C}$. Definitions for this vary depending on the author, but the one we prefer is this:

$$
(\mathcal{F}f)(\omega) = F(\omega) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) \exp\{-i\omega x\} dx.
$$

Variations on this definition have different coefficients outside the integral and/or omit the minus sign in the exponential term.

The inverse Fourier transform is denoted $\mathcal{F}^{-1}$.

### Discrete Fourier transform and Fourier series

The Fourier transform applies to a function defined on $\mathbb{R}$ while the discrete Fourier transform applies to a finite sequence of numbers $a = (a_0, a_1, \ldots, a_{n-1})$. It is also denoted $\mathcal{F}(a)$ and is a new sequence $A = (A_0, A_1, \ldots, A_{n-1})$ with

$$
A_k = \sum_{j=0}^{n-1} a_j e^{-jki\pi/n}.
$$

Some authors scale this by a factor of $1/\sqrt{n}$ (which we think is preferable). Discrete Fourier transforms can be efficiently computed using the fast Fourier transform algorithm, commonly abbreviated FFT. In NumPy: `np.fft.fft(a)`.

The discrete Fourier transform is closely related to the discrete cosine transform which is commonly abbreviated DCT.

Closely related to the Fourier transform is the Fourier series of a (periodic) function. Let $f: [-\pi, \pi] \to \mathbb{R}$. We seek to represent $f$ as a sum of sine and cosine terms like this:

$$
f(t) = a_0 + \sum_{k=1}^{\infty} \left(a_k \cos kt + b_k \sin kt\right).
$$

This can be written in exponential form:

$$
f(t) = \sum_{k=-\infty}^{\infty} \hat{f}(k)e^{ikt}
$$

and the numbers $\hat{f}(k)$ are the Fourier coefficients. As with the Fourier transform, variations in the definition exist to account for intervals other than $[-\pi, \pi]$ and with different scaling factors.

### Transforms notation summary

| Transform | Notation | Domain | Definition |
| --- | --- | --- | --- |
| Laplace | $\mathcal{L}f$ | $\mathbb{R}_+ \to \mathbb{R}$ | $\int_0^\infty f(t) e^{-st}\, dt$ |
| Fourier | $\mathcal{F}f$ or $\hat{f}$ | $\mathbb{R} \to \mathbb{C}$ | $\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) e^{-i\omega x}\, dx$ |
| Discrete Fourier | $\mathcal{F}(a)$ | finite sequence | $\sum_{j=0}^{n-1} a_j e^{-jki\pi/n}$ |
| Inverse | $\mathcal{L}^{-1}$, $\mathcal{F}^{-1}$ | — | reverses the transform |
