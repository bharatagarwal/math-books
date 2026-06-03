# Calculus

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

## 2. Derivatives (single independent variable, scalar- or vector-valued)

Given a function $f$, we have two standard notations for the derivative of $f$: Newton's notation $f'$ and Leibniz's notation $\frac{df}{dx}$. Some authors use a roman (as opposed to italic) $d$ in this notation, like this: $\frac{dy}{dx}$.

Higher order derivatives in Newton's notation are expressed by using additional prime marks. The second derivative is $f''$, the third is $f'''$, and so forth. Sometimes lower case roman numerals replace multiple prime marks, e.g. $f^{(\mathrm{iv})}$. For a positive integer $n$, the $n^{\mathrm{th}}$ derivative may be written $f^{(n)}$.


Higher order derivatives in Leibeniz's notation are expressed using exponents like this:

$$
\frac {d f}{d x}, \frac {d ^ {2} f}{d x ^ {2}}, \frac {d ^ {3} f}{d x ^ {3}}, \dots
$$

The $n^{\mathrm{th}}$ derivative is written $\frac{d^n f}{dx^n}$.

The value of a derivative at a specific value (say, at $x = a$) is written as $f'(a)$ in Newton's notation. The Leibniz notation is more cumbersome:

$$
\left. \frac {d f}{d x} \right| _ {x = a}
$$

The values of the second derivative are written $f''(a)$ and $\left.\frac{d^2f}{dx^2}\right|_{x = a}$ in the two notation styles, and so forth for higher order derivatives.

Another style of notation for derivative involves placing dots over the function. Suppose $y$ is a function of $t$ (which often represents time). Then $\dot{y}$ denotes the derivative $dy/dt$. Likewise $\ddot{y}$ is the second derivative $d^2 y/dt^2$.

The notation $\frac{d}{dx}$ means "the derivative of". It is also denoted with a simple capital $D$:

$$
\frac {d}{d x} \left[ x ^ {2} - 3 x + 2 \right] = D \left[ x ^ {2} - 3 x + 2 \right] = 2 x - 3.
$$

Higher order derivatives are denoted as $\frac{d^n}{dx^n}$ or $D^n$.

The notations for the derivative of a vector-valued function of a single variable are the same as for that of a single-valued function. Let $f\colon \mathbb{R}\to \mathbb{R}^n$. Then the derivative of $f$ is denoted either $f'$ or $df/dt$ (or $df/dx$). Higher order derivatives are, likewise, $f''$ and $d^2 f/dt^2$, and so forth.

## 3. Derivatives (multiple independent variables, scalar-valued)

**Partial derivatives.** When a function depends on two or more variables, the notion of partial derivative comes into play. Suppose $f\colon \mathbb{R}^n\to \mathbb{R}$. Then the partial derivative of $f$ with respect to its $j^{\mathrm{th}}$ argument is

$$
\frac {\partial f}{\partial x _ {j}}.
$$

When $f$ is a function of (say) just two variables $x$ and $y$, then the partial derivatives can also be written as $f_{x} = \partial f / \partial x$ and $f_{y} = \partial f / \partial y$. Another notation is $\partial_x f$.

The notation $D_{x}$ means to take the derivative in the $x$-direction. Thus

$$
D _ {x} f = \partial_ {x} f = f _ {x} = \frac {\partial f}{\partial x}.
$$

More generally, if $\mathbf{v}$ is a unit vector then $D_{\mathbf{v}}$ is the derivative of $f$ in the $\mathbf{v}$ direction; this is known as a directional derivative.

Higher order partial derivatives are denoted like this:

$$
\frac {\partial^ {2} f}{\partial x _ {i} \partial x _ {j}}
$$


which means to first take the partial derivative of $f$ with respect to $x_{j}$ and then the partial derivative of that result with respect to $x_{i}$. In symbols:

$$
\frac {\partial^ {2} f}{\partial x _ {i} \partial x _ {j}} = \frac {\partial}{\partial x _ {i}} \left(\frac {\partial f}{\partial x _ {j}}\right).
$$

For most functions likely to be encountered in science and engineering the order of differentiation does not matter.

For a function of (say) two variables $x$ and $y$, the higher order partials can be written like this: $f_{xx}, f_{xy}, f_{yx}, f_{yy}$.

**Gradient.** The gradient of a function $f: \mathbb{R}^n \to \mathbb{R}$ is the vector of partial derivatives:

$$
\left[ \begin{array}{c} \frac {\partial f}{\partial x _ {1}} \\ \frac {\partial f}{\partial x _ {2}} \\ \vdots \\ \frac {\partial f}{\partial x _ {n}} \end{array} \right].
$$

It is denoted either $\operatorname{grad} f$ or $\nabla f$.

For a function $f$ of three variables, the gradient can be expressed in $\mathbf{i}, \mathbf{j}, \mathbf{k}$-notation like this:

$$
\operatorname {g r a d} f = \nabla f = f _ {x} \mathbf {i} + f _ {y} \mathbf {j} + f _ {z} \mathbf {k}.
$$

**Laplacian.** The Laplacian operator is denoted with a capital $\Delta$. For $f: \mathbb{R}^n \to \mathbb{R}$ we have

$$
\Delta f = \sum_ {i = 1} ^ {n} \frac {\partial^ {2} f}{\partial x _ {i} ^ {2}}
$$

or more simply for a function of three variables,

$$
\Delta f = \frac {\partial^ {2} f}{\partial x ^ {2}} + \frac {\partial^ {2} f}{\partial y ^ {2}} + \frac {\partial^ {2} f}{\partial z ^ {2}}.
$$

**Hessian.** For a function $f: \mathbb{R}^n \to \mathbb{R}$, we can form an $n \times n$-matrix of its partial second derivatives. This matrix is the Hessian matrix of $f$:

$$
H f = \left[ \begin{array}{c c c c} \frac {\partial^ {2} f}{\partial x _ {1} \partial x _ {1}} &amp; \frac {\partial^ {2} f}{\partial x _ {2} \partial x _ {2}} &amp; \dots &amp; \frac {\partial^ {2} f}{\partial x _ {1} \partial x _ {n}} \\ \frac {\partial^ {2} f}{\partial x _ {2} \partial x _ {1}} &amp; \frac {\partial^ {2} f}{\partial x _ {2} \partial x _ {2}} &amp; \dots &amp; \frac {\partial^ {2} f}{\partial x _ {2} \partial x _ {n}} \\ \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\ \frac {\partial^ {2} f}{\partial x _ {n} \partial x _ {1}} &amp; \frac {\partial^ {2} f}{\partial x _ {n} \partial x _ {2}} &amp; \dots &amp; \frac {\partial^ {2} f}{\partial x _ {n} \partial x _ {n}} \end{array} \right].
$$


## 4. Derivatives (multiple independent variables, vector-valued)

In this section we consider derivatives of functions  $\mathbf{f}:\mathbb{R}^m\to \mathbb{R}^n$ . We denote vector-valued functions with bold letters (though this is not mandatory).

Such functions map a vector  $\mathbf{x} \in \mathbb{R}^m$  to a vector  $\mathbf{y} \in \mathbb{R}^n$ . This can be simply written  $\mathbf{y} = \mathbf{f}(\mathbf{x})$  or separated into components like this

$$
y _ {1} = f _ {1} (\mathbf {x})
$$

$$
y _ {2} = f _ {2} (\mathbf {x})
$$

$$
\vdots
$$

$$
y _ {n} = f _ {n} (\mathbf {x})
$$

or like this

$$
\mathbf {f} (\mathbf {x}) = \left[ \begin{array}{c} f _ {1} (\mathbf {x}) \\ f _ {2} (\mathbf {x}) \\ \vdots \\ f _ {n} (\mathbf {x}) \end{array} \right]
$$

where, of course,  $f_{j}(\mathbf{x})$  denotes the  $j^{\mathrm{th}}$  component of the vector  $\mathbf{f}(\mathbf{x})$ .

**Partial derivatives.** Partial derivatives of  $\mathbf{f}$  typically specify both the component function and the variable with respect to which the function is being differentiated:

$$
\frac {\partial f _ {i}}{\partial x _ {j}}.
$$

Some people express this partial derivative as  $f_{i,j}$ .

One can take the partial derivative of all components of  $\mathbf{f}$  with respect to a single variable:

$$
\frac {\partial \mathbf {f}}{\partial x _ {j}} = \left[ \begin{array}{c} \frac {\partial f _ {1}}{\partial x _ {j}} \\ \frac {\partial f _ {2}}{\partial x _ {j}} \\ \vdots \\ \frac {\partial f _ {n}}{\partial x _ {j}} \end{array} \right]
$$

This vector of partial derivatives can be written  $f_{,j}$ . One needs to be careful with this notation as the comma may be difficult to notice.

**Jacobian.** The matrix of all partial derivatives is called the Jacobian matrix of  $f$  and is simply denoted  $D\mathbf{f}$ :

$$
D \mathbf {f} = \left[ \begin{array}{c c c c} \frac {\partial f _ {1}}{\partial x _ {1}} &amp; \frac {\partial f _ {1}}{\partial x _ {2}} &amp; \dots &amp; \frac {\partial f _ {1}}{\partial x _ {m}} \\ \frac {\partial f _ {2}}{\partial x _ {1}} &amp; \frac {\partial f _ {2}}{\partial x _ {2}} &amp; \dots &amp; \frac {\partial f _ {2}}{\partial x _ {m}} \\ \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\ \frac {\partial f _ {n}}{\partial x _ {1}} &amp; \frac {\partial f _ {n}}{\partial x _ {2}} &amp; \dots &amp; \frac {\partial f _ {n}}{\partial x _ {m}} \end{array} \right] = \left[ \begin{array}{c c c c} f _ {1, 1} &amp; f _ {1, 2} &amp; \dots &amp; f _ {1, m} \\ f _ {2, 1} &amp; f _ {2, 2} &amp; \dots &amp; f _ {2, m} \\ \vdots &amp; \vdots &amp; \ddots &amp; \vdots \\ f _ {n, 1} &amp; f _ {n, 2} &amp; \dots &amp; f _ {n, m} \end{array} \right].
$$


If $\mathbf{f}:\mathbb{R}^n\to \mathbb{R}^n$, then $D\mathbf{f}$ is a square matrix; its determinant is, unfortunately, also called the Jacobian of $\mathbf{f}$.

One can think of $\mathbf{f}:\mathbb{R}^n\to \mathbb{R}^n$ as a change of coordinate systems. If the original coordinates are, say, $(x,y,z)$, then $\mathbf{f}(x,y,z) = (u,v,w)$ are the coordinates of the point in the alternative system. In this way, $u$, $v$, and $w$ are themselves functions of $x,y$, and $z$. Then the (determinant of the) Jacobian of $\mathbf{f}$ is also denoted:

$$
\left| \frac {\partial (u , v , w)}{\partial (x , y , z)} \right| = \det  \left[ \begin{array}{c c c} \frac {\partial u}{\partial x} &amp; \frac {\partial u}{\partial y} &amp; \frac {\partial u}{\partial z} \\ \frac {\partial v}{\partial x} &amp; \frac {\partial v}{\partial y} &amp; \frac {\partial v}{\partial z} \\ \frac {\partial w}{\partial x} &amp; \frac {\partial w}{\partial y} &amp; \frac {\partial w}{\partial z} \end{array} \right].
$$

**Curl.** For a function $\mathbf{f}:\mathbb{R}^3\to \mathbb{R}^3$ the *curl* of $\mathbf{f}$ is

$$
\operatorname {c u r l} \mathbf {f} = \nabla \times \mathbf {f} = \left[ \begin{array}{l} f _ {3, 2} - f _ {2, 3} \\ f _ {1, 3} - f _ {3, 1} \\ f _ {2, 1} - f _ {1, 2} \end{array} \right]
$$

where $f_{1,2}$ means the partial derivative of $f_{1}$ in its second argument, i.e., $\partial f_1 / \partial x_2$.

The notation $\nabla \times \mathbf{f}$ is inspired by the cross product in which the first “vector” is a list of operators:

$$
\nabla \times \mathbf {f} = \left[ \begin{array}{c} \frac {\partial}{\partial x _ {1}} \\ \frac {\partial}{\partial x _ {2}} \\ \frac {\partial}{\partial x _ {3}} \end{array} \right] \times \left[ \begin{array}{c} f _ {1} \\ f _ {2} \\ f _ {3} \end{array} \right].
$$

**Divergence.** For a function $\mathbf{f}:\mathbb{R}^3\to \mathbb{R}^3$, the *divergence* of $\mathbf{f}$ is

$$
\operatorname {d i v} \mathbf {f} = \nabla \cdot \mathbf {f} = \frac {\partial f _ {1}}{\partial x _ {1}} + \frac {\partial f _ {2}}{\partial x _ {2}} + \frac {\partial f _ {3}}{\partial x _ {3}}.
$$

Like the notation for curl, this notation is inspired by the dot product in which the first “vector” is a list of operators:

$$
\nabla \cdot \mathbf {f} = \left[ \begin{array}{c} \frac {\partial}{\partial x _ {1}} \\ \frac {\partial}{\partial x _ {2}} \\ \frac {\partial}{\partial x _ {3}} \end{array} \right] \cdot \left[ \begin{array}{c} f _ {1} \\ f _ {2} \\ f _ {3} \end{array} \right].
$$

More generally, for $\mathbf{f}:\mathbb{R}^n\to \mathbb{R}^n$,

$$
\operatorname {d i v} \mathbf {f} = \nabla \cdot \mathbf {f} = \sum_ {j = 1} ^ {n} \frac {\partial f _ {j}}{\partial x _ {j}}.
$$

Note that for the scalar valued function $f: \mathbb{R}^n \to \mathbb{R}$, the gradient of $f$, denoted $\nabla f$, is the vector of $f$'s partial derivatives, and so $\nabla f: \mathbb{R}^n \to \mathbb{R}^n$. If we take the divergence of $\nabla f$ we have

$$
\nabla \cdot (\nabla f) = \sum_ {j = 0} ^ {n} \frac {\partial^ {2} f _ {j}}{\partial x _ {j} ^ {2}}
$$

which is the Laplacian of $f$. Thus $\nabla \cdot (\nabla f) = \nabla^2 f$.


## 5. Integration

Let $f: \mathbb{R} \to \mathbb{R}$. The notation $\int f(x) \, dx$ is the indefinite integral of $f$; it is a function $F$ whose derivative is $f$. The function $F$ is called an antiderivative or a primitive of $f$. The notation

$$
\int_{a}^{b} f(x) \, dx
$$

is the definite integral of $f$ and its value can be expressed

$$
F(x) \Big|_{a}^{b} = F(b) - F(a)
$$

where $F$ is an antiderivative of $f$. Some authors use a roman (as opposed to italic) $d$ in the integral, like this: $\int f(x) \, dx$.

The left and right end points of the interval over which a function is integrated may be $-\infty$ and $\infty$, respectively.

Multiple integrals take the following form:

$$
\iint f(x, y) \, dx \, dy.
$$

This means we integrate $f(x, y)$ first with respect to $x$ (holding $y$ constant), and then integrate the resulting expression with respect to $y$. It is equivalent to

$$
\int \left[ \int f(x, y) \, dx \right] \, dy.
$$

This is not equivalent to $\iint f(x,y) \, dy \, dx$, although the end result is often the same.

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

When the subscript on the integral is a curve

$$
\int_{\gamma} f \, ds
$$

denotes the line integral of $f$ along the curve $\gamma$.


If the curve is closed (i.e., it begins and ends at the same point) then we write

$\oint_{\gamma}f\,ds$

for the line integral. (The subscript indicating the name of the curve may be omitted if it is clear from context.) In this case, the line integral may also be called a contour integral. When the contour is the boundary of a domain $D$, the following notation may be used:

$\int_{\partial D}f\,ds\quad\text{or}\quad\oint_{\partial D}f\,ds$

where $\partial D$ indicates the boundary of $D$.

## 6. Convolution and transforms

If $f$ and $g$ are functions from $\mathbb{R}$ to $\mathbb{R}$, we define their convolution $f*g$ as a new function with

$(f*g)(x)=\int_{-\infty}^{\infty}f(t)g(x-t)\,dt.$

The convolution integral need not be computed over the entire real line. Sometimes, it is computed just on an interval especially if the functions $f$ and $g$ are periodic. The interval over which we integrate can be arbitrary:

$(f*g)(x)=\int_{a}^{b}f(t)g(x-t)\,dt.$

Common intervals include $[0,1]$, $[-\pi,\pi]$, and $[0,2\pi]$.

In some cases, we normalize the integral by dividing by the length of the interval:

$(f*g)(x)=\frac{1}{b-a}\int_{a}^{b}f(t)g(x-t)\,dt.$

The notion of convolution (and the use of the symbol $*$) extends to other realms. For example, given sequences $a=(a_{0},a_{1},a_{2},\ldots)$ and $b=(b_{0},b_{1},b_{2},\ldots)$, their convolution is a new sequence $c=a*b$ with

$c_{n}=\sum_{k=0}^{n}a_{k}b_{n-k}.$

Similarly, in number theory, the convolution of two functions $f,g:\mathbb{Z}^{+}\to\mathbb{R}$ is $f*g$ with

$(f*g)(n)=\sum_{d|n}f(d)g(n/d).$


Let $f: \mathbb{R}_+ \to \mathbb{R}$. The Laplace transform of $f$ is denoted $\mathcal{L}f$. It is a new function defined on the nonnegative real numbers by

$$
(\mathcal{L}f)(s) = \int_{0}^{\infty} f(t)e^{-st} dt.
$$

The inverse Laplace transform is denoted $\mathcal{L}^{-1}$.

Let $f: \mathbb{R} \to \mathbb{R}$ (or, more generally, $f: \mathbb{R} \to \mathbb{C}$). The Fourier transform of $f$ is denoted $\mathcal{F}f$. This is a new function $F: \mathbb{R} \to \mathbb{C}$. Definitions for this vary depending on the author, but the one we prefer is this:

$$
(\mathcal{F}f)(\omega) = F(\omega) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(x) \exp\{-i\omega x\} dx.
$$

Variations on this definition have different coefficients outside the integral and/or omit the minus sign in the exponential term.

The inverse Fourier transform is denoted $\mathcal{F}^{-1}$.

The Fourier transform applies to a function defined on $\mathbb{R}$ while the discrete Fourier transform applies to a finite sequence of numbers $a = (a_0, a_1, \ldots, a_{n-1})$. It is also denoted $\mathcal{F}(a)$ and is a new sequence $A = (A_0, A_1, \ldots, A_{n-1})$ with

$$
A_k = \sum_{j=0}^{n-1} a_j e^{-jki\pi/n}.
$$

Some authors scale this by a factor of $1/\sqrt{n}$ (which we think is preferable). Discrete Fourier transforms can be efficiently computed using the fast Fourier transform algorithm, commonly abbreviated FFT.

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
