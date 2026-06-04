# Functions

The concept of "function" took centuries to settle. Euler (1748) thought of a function as any algebraic expression — $y = x^2 + 3x$ qualified, but an arbitrary temperature curve did not. Dirichlet (1837) shattered that limitation: a function is simply a rule that assigns to each input exactly one output. No formula required. That definition — which sounds exactly like a programming function with a single return value — is the one mathematics uses today.

If you can write `def f(x: float) -> float`, you already understand $f \colon \mathbb{R} \to \mathbb{R}$. The notation below makes that intuition precise, and extends it to composition, inversion, and the vast library of named functions that recur across mathematics.

## Fundamentals

### Function notation

The notation $f\colon A \to B$ means that $f$ is a function that takes inputs from the set $A$ (the **domain**) and returns values in the set $B$ (the **codomain**). For a software engineer, this is a type signature:

| Math notation | Python type hint | Meaning |
| --- | --- | --- |
| $f \colon \mathbb{R} \to \mathbb{R}$ | `def f(x: float) -> float` | takes a real, returns a real |
| $f \colon \mathbb{Z} \to \mathbb{Z}$ | `def f(n: int) -> int` | takes an integer, returns an integer |
| $f \colon A \times B \to C$ | `def f(a: A, b: B) -> C` | takes a pair, returns a value |

It is not necessary that every value of $B$ be realized as an output. For example, we may write $\cos\colon\mathbb{R}\to\mathbb{R}$ because the cosine function takes any real number as input and returns real numbers. Of course, the outputs of the cosine function lie in the interval $[-1,1]$.

### Evaluation and mapping notation

The notation $f(x)$ indicates the value returned by the function $f$ when evaluated at $x$. That is, $f$ is the function while $f(x)$ is the value (typically a number) returned by the function.

An alternative notation for function evaluation uses the "evaluation bar":

$$
\text{(some expression involving }x)\Big|_{x=a}
$$

This means: substitute the value $a$ for the variable $x$. This notation is especially common with Leibniz-notation derivatives (see the Calculus chapter).

The notation $y=f(x)$ is sometimes abbreviated to $x\mapsto y$, pronounced "$x$ maps to $y$." This is Python's `lambda`: the expression $x \mapsto x^2 + 1$ is exactly `lambda x: x**2 + 1`. One may also write $x\xmapsto{f}y$ to make the function explicit.

### Operators and dot notation

A function whose inputs and outputs are themselves functions is often called an *operator* or a *transform*. Operators are typographically distinguished from functions of numbers; for example, one may capitalize the operator's name. The application of an operator to a function might omit the parentheses: $Lf$ denotes the evaluation of the operator $L$ on the function $f$.

The notation $f(\cdot)$ uses a dot to emphasize that $f$ expects an argument. This is handy for non-letter symbols — when discussing the absolute value function, one may write $|\cdot|$ rather than putting in a dummy variable.

Functions may take more than one argument, e.g., $f(x,y)$ is a function of two arguments. In this case the dot notation expresses which argument varies and which is held constant. For example, $f(\cdot,b)$ is a function of one variable: the first argument varies over its domain while the second is fixed at $b$. This is the mathematical version of Python's `functools.partial`.

### Image and preimage

For a function $f: X \to Y$, the **image** of $f$ is denoted $\operatorname{Im}(f)$:

$$
\operatorname{Im}(f) = \{y \in Y \mid \exists x \in X,\; f(x) = y\}.
$$

More generally, if $A \subseteq X$, then $f(A)$ stands for the set $\{f(a) \mid a \in A\}$. Thus $f(X) = \operatorname{Im}(f)$.

### Piecewise definition

Functions are often specified by a single algebraic formula, but this is not necessary. A function may be defined piecewise:

$$
f(x) = \begin{cases}
e^{-1/x^2} & \text{for } x > 0 \\
0 & \text{otherwise.}
\end{cases}
$$

### Composition and inversion

If $f \colon A \to B$ and $g \colon B \to C$ then $g \circ f$ is a new function, the **composition** of $g$ and $f$, with $(g \circ f) \colon A \to C$ defined by

$$
(g \circ f)(x) = g[f(x)].
$$

Note the right-to-left order: $g \circ f$ means "first apply $f$, then apply $g$." This matches nesting in code: `g(f(x))`.

The notation $f^{-1}(y)$ stands for the value $x$ such that $f(x) = y$; we call $f^{-1}$ the **inverse** of $f$.

If there is more than one value $x$ with $f(x) = y$, then $f^{-1}$ is not a function. Some people use $f^{-1}(y)$ to stand for the set of all $x$ values that map to $y$. In other cases one coerces $f^{-1}$ to be a function by restricting the domain. For example, the arc sine function is $\sin^{-1}$. There are infinitely many values $x$ such that $\sin x = \frac{1}{2}$, but we restrict $x$ to $(-\frac{\pi}{2}, \frac{\pi}{2}]$, making arc sine a proper function. Note that $f^{-1}(y)$ is undefined if there is no value $x$ such that $f(x) = y$.

The notation $f^{-1}$ may be applied to a set. If $B \subseteq Y$, then

$$
f^{-1}(B) = \{x \in X \mid f(x) \in B\}.
$$

### The $f^2$ ambiguity

The notation $f^2(x)$ sometimes means $[f(x)]^2$; this is especially common with trigonometric functions, e.g., $\sin^2\theta$. But in other contexts $f^2(x)$ means $(f \circ f)(x) = f[f(x)]$. The latter is consistent with $f^{-1}$; the former is not. Watch for context.

Here is how all of this looks in Python and SymPy — type signatures as domain/codomain, composition as nesting, and the inverse as a `solve` call:

```python
<!-- include: code/mathematical-notation/06 - Functions/01_python.py -->
```


## Standard functions

### Functions of real numbers

There is a vast array of functions defined on the real numbers. The table below maps the most common ones from notation to code, then each is explained in detail.

| Math notation | Python (`math`) | SymPy | Notes |
| --- | --- | --- | --- |
| $\|x\|$ | `abs(x)` | `Abs(x)` | absolute value |
| $\sqrt{x}$, $\sqrt[n]{x}$ | `math.sqrt(x)` | `sqrt(x)`, `root(x,n)` | nonneg root |
| $\operatorname{sgn} x$ | `(x>0)-(x<0)` | `sign(x)` | sign function |
| $e^x$, $\exp x$ | `math.exp(x)` | `exp(x)` | exponential |
| $\ln x$ | `math.log(x)` | `log(x)` | natural log |
| $\log_{10} x$ | `math.log10(x)` | `log(x,10)` | common log |
| $\lg x$ | `math.log2(x)` | `log(x,2)` | binary log |
| $\sin x$, $\cos x$, $\tan x$ | `math.sin(x)`, ... | `sin(x)`, ... | trig (radians) |
| $\arcsin x$ / $\sin^{-1} x$ | `math.asin(x)` | `asin(x)` | inverse trig |
| $\sinh x$, $\cosh x$ | `math.sinh(x)`, ... | `sinh(x)`, ... | hyperbolic |
| $\lfloor x \rfloor$ | `math.floor(x)` | `floor(x)` | floor |
| $\lceil x \rceil$ | `math.ceil(x)` | `ceiling(x)` | ceiling |
| $n!$ | `math.factorial(n)` | `factorial(n)` | factorial |
| $\Gamma(x)$ | `math.gamma(x)` | `gamma(x)` | gamma function |

Here they are in action:

```python
<!-- include: code/mathematical-notation/06 - Functions/02_python.py -->
```

Now the details on each:

- **Absolute value.** For a real or complex number $x$, $|x|$ is the absolute value of $x$. (See also pages 14 and 17.)

- **Square (and other) roots.** For nonnegative real numbers $x$, the notation $\sqrt{x}$ is unambiguously the nonnegative square root of $x$. Likewise, for $x\geq 0$ and $n>0$, $\sqrt[n]{x}$ is the nonnegative $n^{\text{th}}$-root of $x$. ($n$ need not be an integer.)

  These may be written in exponential form: $\sqrt{x}=x^{1/2}$ and $\sqrt[n]{x}=x^{1/n}$.

  When $x$ is a negative real number the situation becomes more complex (pun intended). In this case $\sqrt{x}=i\sqrt{|x|}$. If $n$ is an odd integer, $\sqrt[n]{x}$ is the unique (necessarily negative) real number $y$ so that $y^{n}=x$. All other cases are ambiguous and handled by special convention.

- **Signum (sign).** The notation $\operatorname{sgn}x$ is the sign of $x$:

  $$\operatorname{sgn}x=\begin{cases}1&\text{if }x>0,\\ 0&\text{if }x=0\text{, and}\\ -1&\text{if }x<0.\end{cases}$$

  Some people write the full word "sign" in place of $\operatorname{sgn}$.

- **Exponential function.** $\exp x$ stands for $e^{x}$. Sometimes people enclose the argument in curly braces like $\exp\{x\}$, but this is not necessary. If the argument is a complicated expression, parentheses are clearer: $\exp\left(x^{2}+y^{2}\right)$.

- **Logarithms.** The notation $\log x$ is ambiguous. In science and engineering it typically means the base-10 logarithm. In mathematics, it typically means the natural logarithm ($\log_e$). In computer science, it often means $\log_2$.

  The notation $\ln x$ stands for $\log_{e}x$ and $\lg x$ stands for $\log_{2}x$.

  The function $\log^{*}x$ occurs in computer science. It is the number of times one must apply $\log$ to reach a result less than 1 — the *log star* function.

- **Trigonometric functions.** The standard trigonometric functions are $\sin$, $\cos$, $\tan$, $\sec$, $\csc$, and $\cot$. Arguments are usually expressed in radians in mathematics; degrees may appear in science and engineering. Greek letters, especially $\theta$, are customary but not required as arguments.

  The notation $\sin^2 x$ means $(\sin x)^2$; however $\sin^{-1} x$ does not mean $1 / \sin x$. Rather, $\sin^{-1} x$ is the inverse sine (or arc sine) function, also written $\arcsin x$. Likewise: $\arccos$, $\arctan$, and so forth.

- **Hyperbolic trigonometric functions.** The standard trigonometric functions have hyperbolic "cousins," denoted by appending the letter "h":

  $$\sinh x = \frac{e^x - e^{-x}}{2} \quad \text{and} \quad \cosh x = \frac{e^x + e^{-x}}{2}.$$

  Also: $\tanh x = \sinh x / \cosh x$, $\operatorname{sech} x = 1 / \cosh x$, $\operatorname{csch} x = 1 / \sinh x$, and $\coth x = \cosh x / \sinh x$.

  As with ordinary trig functions, $\sinh^2 x$ means $(\sinh x)^2$ but $\sinh^{-1} x$ is the inverse function.

- **Sine cardinal.** The function $\operatorname{sinc} x$ is called the sine cardinal:

  $$\operatorname{sinc} x = \frac{\sin x}{x} \quad \text{or} \quad \operatorname{sinc} x = \frac{\sin \pi x}{\pi x}$$

  for $x \neq 0$, with $\operatorname{sinc} 0 = 1$.

- **Floor, ceiling.** The notation $\lfloor x \rfloor$ is the **floor** of $x$ — rounding down to the nearest integer. In older books: $[x]$. The notation $\lceil x \rceil$ is the **ceiling** of $x$ — rounding up. In older books: $\{x\}$.

  $$\lceil e \rceil = \lceil 3 \rceil = \lfloor 3 \rfloor = \lfloor \pi \rfloor = 3.$$

- **Error function.** $\operatorname{erf} x$ occurs in probability theory:

  $$\operatorname{erf} x = \frac{2}{\sqrt{\pi}} \int_{0}^{x} \exp\left(- t^{2}\right) dt.$$

- **Gamma function.** $\Gamma(x)$ is defined by

  $$\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t}\, dt.$$

  It is closely related to the factorial function: $n! = \Gamma(n+1)$ for nonnegative integers $n$. And it generalizes factorials to all complex numbers (except non-positive integers).

- **Beta function.** $B(a, b)$ is defined by

  $$B(a, b) = \int_{0}^{1} t^{a-1} (1 - t)^{b-1}\, dt$$

  and equals $\Gamma(a)\Gamma(b) / \Gamma(a + b)$. It is closely related to binomial coefficients.

- **Bessel functions.** The following notations are used for Bessel functions:

  | Notation | Name |
  | --- | --- |
  | $J_{n}$ | Bessel function of the first kind, order $n$ |
  | $Y_{n}$ | Bessel function of the second kind, order $n$ |
  | $I_{n}$ | modified Bessel function of the first kind, order $n$ |
  | $K_{n}$ | modified Bessel function of the second kind, order $n$ |

  Closely related are the Hankel functions of the first and second kinds:

  $$H _ {n} ^ {(1)} (x) = J _ {n} (x) + i Y _ {n} (x) \quad \text{and} \quad H _ {n} ^ {(2)} (x) = J _ {n} (x) - i Y _ {n} (x).$$

- **Hypergeometric functions.** The hypergeometric function ${}_{2}F_{1}$ takes three "parameters" ($a$, $b$, $c$) and one argument ($x$):

  $${}_{2}F_{1}(a, b; c; x) = \sum_{k=0}^{\infty} \frac{a^{(k)} b^{(k)}}{c^{(k)}} \cdot \frac{x^{k}}{k!}.$$

  For an explanation of the rising factorial notation $a^{(k)}$, see the entry on factorial functions below.

  This is also written more elaborately as:

  $${}_{2}F_{1}\left(\begin{array}{c} a, b \\ c \end{array}\right| x$$

  which more clearly illustrates the placement of $a$ and $b$ in the numerator and $c$ in the denominator.

  More generally, if $p$ and $q$ are nonnegative integers, the function ${}_pF_q$ has $p$ upper indices ($a_1$ through $a_p$) and $q$ lower indices ($b_1$ through $b_q$):

  $${}_{p}F_{q}(a_1, a_2, \ldots, a_p; b_1, b_2, \ldots, b_q; x) = \sum_{k=0}^{\infty} \frac{a_1^{(k)} a_2^{(k)} \cdots a_p^{(k)}}{b_1^{(k)} b_2^{(k)} \cdots b_q^{(k)}} \cdot \frac{x^{k}}{k!}.$$

- **Riemann zeta function.** The function $\zeta(z)$ is the Riemann zeta function. For an integer $n \geq 2$:

  $$\zeta(n) = \sum_{k=1}^{\infty} \frac{1}{k^{n}}$$

  and is defined for arbitrary complex $z$ by analytic continuation.

- **Dirac delta "function."** This entry comes with a caveat: the Dirac $\delta$ is not actually a function (it is a distribution). Nevertheless, the word "function" is traditionally used. Dirac's $\delta$ can be imagined as taking the value zero everywhere except at the origin, where it is "infinite," yet its integral is 1. Given a function $f: \mathbb{R} \to \mathbb{R}$:

  $$\int_{-\infty}^{\infty} f(x)\, \delta(x)\, dx = f(0).$$

  The Dirac $\delta$ may be thought of as the derivative of the Heaviside function $H$ defined by

  $$H(x) = \begin{cases} 1 & \text{for } x \geq 0 \\ 0 & \text{for } x < 0. \end{cases}$$

  Notice that $H(x) = \int_{-\infty}^{x} \delta(t)\, dt$, and in that sense the derivative of $H$ is $\delta$.

  For a spike at a value other than 0 (say at $c$), use $\delta(x - c)$, sometimes denoted $\delta_c(x)$.

### Functions of integers

The following functions are defined only for integer values.

- **Factorial and related functions.** For a nonnegative integer $n$, the notation $n!$ is pronounced "$n$-factorial" and is defined by $0! = 1$ and for $n > 0$:

  $$n! = n(n - 1)(n - 2) \cdots 2 \cdot 1.$$

  It is closely related to the gamma function: $n! = \Gamma(n + 1)$.

  The use of the exclamation point for factorial is universally accepted, but it was not always the case; see Figure 6.1. For more historical tidbits on notation see Cajori's *A History of Mathematical Notations* and Jeff Miller's [Earliest Uses of Various Mathematical Symbols](http://jeff560.tripod.com/mathsym.html).

  $$f(x) = f(a) + \frac{(x - a)}{\lfloor 1 \rfloor} f^{\prime}(a) + \frac{(x - a)^{2}}{\lfloor 2 \rfloor} f^{\prime\prime}(a) + \frac{(x - a)^{3}}{\lfloor 3 \rfloor} f^{\prime\prime\prime}(a) + \dots$$

  ![Figure 6.1: The formula for the Taylor series of a function as it appears in \[4\]. Note the notation for n!.](06 - Functions_images/img-0.jpeg)

  The notation $n!!$ is the **double factorial**; the factors descend by two. For example, $7!! = 7 \times 5 \times 3 \times 1$.

  For a real number $x$ and a nonnegative integer $k$, the notations $x^{(k)}$ and $x_{(k)}$ are the **rising** and **falling** factorial functions:

  $$x^{(k)} = x(x + 1) \cdots (x + k - 1) = \prod_{j=0}^{k-1} (x + j)$$

  $$x_{(k)} = x(x - 1) \cdots (x - k + 1) = \prod_{j=0}^{k-1} (x - j).$$

  Note that $x^{(0)} = x_{(0)} = 1$.

  Alternative (and especially clear) notations for rising/falling factorials:

  $$x^{\overline{k}} = x^{(k)} \qquad \text{and} \qquad x^{\underline{k}} = x_{(k)}.$$

  The notations $P(n,k)$, $P_{n,k}$, $P_{k,n}$, and ${}_nP_k$ are also used for the falling factorial $n_{(k)}$, mostly in older works. Here $P$ stands for "permutation" and $P(n,k)$ means "the number of permutations of $n$ things taken $k$ at a time." We discourage the use of $P$ for this purpose.

  Finally, the notation $(x)_k$ (the **Pochhammer symbol**) is also used for the rising factorial function — an unfortunate ambiguity.

- **Binomial coefficient.** The binomial coefficient $\binom{n}{k}$ is defined for nonnegative integers $n$ and $k$ to be the number of $k$-element subsets of an $n$-element set. For $0 \leq k \leq n$:

  $$\binom{n}{k} = \frac{n!}{k!(n - k)!}$$

  and for $k > n$ we have $\binom{n}{k} = 0$.

  The letter $C$ is also used: $C(n, k)$, $C_{n,k}$, $C_{k,n}$, ${}_nC_k$. In this context $C$ stands for "combinations." We strongly encourage the exclusive use of $\binom{n}{k}$.

  There are additional notations closely related to binomial coefficients:

- **Multinomial coefficient.** For nonnegative integers $n, k_1, k_2, \ldots, k_t$ with $k_1 + k_2 + \cdots + k_t = n$:

  $$\binom{n}{k_1 \; k_2 \; \cdots \; k_t} = \frac{n!}{k_1! k_2! \cdots k_t!}.$$

- **Multichoose.** The notation $\left(\!\binom{n}{k}\!\right)$ stands for the number of $k$-element multisets from an $n$-element set:

  $$\left(\!\binom{n}{k}\!\right) = \binom{n + k - 1}{k}.$$

- **$q$-binomial coefficient.** For nonnegative integers $n, k$ and a variable $q$, the notation $\binom{n}{k}_q$ is the $q$-binomial coefficient:

  $$\binom{n}{k}_q = \begin{cases}
  \dfrac{(1 - q^n)(1 - q^{n-1}) \cdots (1 - q^{n-k+1})}{(1 - q)(1 - q^2) \cdots (1 - q^k)} & \text{if } k \leq n \\ 0 & \text{otherwise.}
  \end{cases}$$

- **Stirling numbers.** Stirling numbers come in two varieties:

  - **First kind:** denoted $s(n, k)$. It is the coefficient of $x^k$ in the polynomial $(x)_n = x(x-1)\cdots(x-n+1)$. The unsigned version $c(n,k) = |s(n,k)|$ counts permutations in $S_n$ with exactly $k$ cycles. Also denoted $\left[\begin{smallmatrix}n\\k\end{smallmatrix}\right]$.
  - **Second kind:** denoted $S(n, k)$. They count the number of partitions of an $n$-element set into exactly $k$ nonempty parts. Also denoted $\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}$.

- **Divisibility.** For integers $a$ and $b \neq 0$, the expression $b \mid a$ means $a$ is divisible by $b$ — there is an integer $q$ such that $a = bq$. Read "$b$ divides $a$."

- **Mod.** For integers $a, b$ with $b > 0$, the expression $a \bmod b$ is the remainder when $a$ is divided by $b$. Specifically, $a = qb + r$ with $0 \leq r < b$, and $a \bmod b = r$.

  For example: $13 \bmod 10 = 3$ and $-10 \bmod 9 = 8$ (because $-10 = -2 \times 9 + 8$). In Python: `13 % 10` and `-10 % 9`.

  There is also a **congruence relation** using mod. For a positive integer $n$ and any integers $a, b$:

  $$a \equiv b \pmod{n} \quad \text{or more simply} \quad a \equiv b \quad (n)$$

  means $a - b$ is divisible by $n$ (i.e., $n \mid a - b$). When the modulus is understood, the $(\bmod\; n)$ may be omitted.

- **GCD and LCM.** For integers $n$ and $m$, $\gcd(n, m)$ is the greatest common divisor. In number theory, this is abbreviated to $(n, m)$. Python: `math.gcd(n, m)`.

  The notation $\operatorname{lcm}(n, m)$ is the least common multiple. Python: `math.lcm(n, m)`.

- **Euler's totient.** For a positive integer $n$, $\varphi(n)$ is the number of integers in $\{1, 2, \ldots, n\}$ that are relatively prime to $n$. The symbol $\varphi$ is a stylized Greek phi; some use $\phi$.

- **Legendre/Jacobi symbol.** If $p$ is an odd prime and $a$ is an integer, the **Legendre symbol** $\left(\frac{a}{p}\right)$ is:

  $$\left(\frac{a}{p}\right) = \begin{cases} 0 & \text{if } a \equiv 0 \pmod{p}, \\ 1 & \text{if } a \text{ is a quadratic residue mod } p \text{ and } a \not\equiv 0, \\ -1 & \text{otherwise}. \end{cases}$$

  Some authors write it horizontally: $(a \mid p)$.

  If the lower entry in $\left(\frac{a}{n}\right)$ is not prime, the notation is the **Jacobi symbol**. If $n = p_1^{e_1}p_2^{e_2}\cdots p_t^{e_t}$, then

  $$\left(\frac{a}{n}\right) = \left(\frac{a}{p_1}\right)^{e_1} \left(\frac{a}{p_2}\right)^{e_2} \cdots \left(\frac{a}{p_t}\right)^{e_t}.$$

### Other standard functions

- **Identity function.** For a set $A$, the notation $\mathrm{Id}_A$ is the identity function on $A$: $\mathrm{Id}_A(a) = a$ for all $a \in A$. In Python: `lambda x: x`.

- **Characteristic function.** Given a set $A$ (often a subset of the reals), $\chi_A$ denotes the characteristic function of $A$:

  $$\chi_{A}(x) = \begin{cases} 1 & \text{if } x \in A \\ 0 & \text{otherwise.} \end{cases}$$

  Some people write $\mathbf{1}_A$ for this. In programming terms, this is `1 if x in A else 0`.

## Classes of functions

The notation $C^k$ denotes those functions whose $k^{\mathrm{th}}$ derivative is defined and continuous. Thus $C^0$ is the class of continuous functions, $C^1$ the class of differentiable functions with continuous derivatives, and so on:

$$C^{0} \supset C^{1} \supset C^{2} \supset \cdots$$

For functions defined on an interval $[a, b]$, we write $C^k([a, b])$. The notation $C^k(\mathbb{R})$ is equivalent to $C^k$.

The class $C^\infty$ contains functions for which derivatives of all orders exist (and are therefore continuous). Polynomials and $e^x$ live here.

The notation $L^p$, where $p$ is a positive real number, denotes the class of functions for which

$$\int_{-\infty}^{\infty} |f(x)|^{p}\, dx < \infty.$$

This may be restricted to an interval: $L^p([a, b])$ stands for those functions with $\int_{a}^{b} |f(x)|^{p}\, dx < \infty$.

Closely related is $\ell^p$, the class of sequences $a_0, a_1, a_2, \ldots$ for which

$$\sum_{k=0}^{\infty} |a_k|^p < \infty.$$

## Polynomials, power series, and rational functions

### Polynomials

A polynomial is a function of the form

$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0.$$

Some authors prefer that the subscripts run counter to the exponents:

$$p(x) = a_0 x^n + a_1 x^{n-1} + \cdots + a_{n-1} x + a_n.$$

The **degree** of a polynomial is denoted $\deg p(x)$; it is the largest exponent on $x$ with a nonzero coefficient. If $p(x) = 0$ (the zero polynomial), $\deg p$ is either undefined or $-\infty$.

The set of all polynomials in $x$ with real coefficients is denoted $\mathbb{R}[x]$. More generally, if $R$ is any ring, then $R[x]$ is the set of all polynomials in $x$ with coefficients in $R$. Polynomials in multiple variables: $R[x,y]$.

Just as we have divisibility $|$ and mod for integers, the same notions apply to polynomials:

- $p(x) \mid q(x)$ means there is a polynomial $a(x)$ with $a(x)p(x) = q(x)$.
- $p(x) \equiv q(x) \pmod{a(x)}$ means $a(x) \mid p(x) - q(x)$.
- $R[x]/(a(x))$ is the set of polynomials taken modulo $a(x)$. For example, $\mathbb{Z}[x]/(x^2 + 1)$ is, effectively, the Gaussian integers.

Certain families of polynomials have their own notation:

| Notation | Family |
| --- | --- |
| $T_n(x)$, $U_n(x)$ | Chebyshev polynomials (first and second kind) |
| $H_n(x)$ | Hermite polynomials |
| $L_n(x)$ | Laguerre polynomials |
| $P_n(x)$ | Legendre polynomials |

### Power series

A power series is a function of the form

$$f(x) = a_{0} + a_{1}x + a_{2}x^{2} + \cdots = \sum_{k=0}^{\infty} a_k x^k.$$

The set of all power series with coefficients from a ring $R$ is denoted $R[[x]]$. These are called *formal power series* when convergence is not at issue.

### Rational functions

A rational function is the ratio of two polynomials:

$$f(x) = \frac{a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{1}x + a_{0}}{b_{m}x^{m} + b_{m-1}x^{m-1} + \cdots + b_{1}x + b_{0}}.$$

The set of all rational functions with real coefficients is denoted $\mathbb{R}(x)$. In general, if $F$ is any field, $F(x)$ is the set of rational functions in $x$ with coefficients from $F$.

Note the bracket convention: $R[x]$ for polynomials (square brackets), $R[[x]]$ for power series (double square), $F(x)$ for rational functions (parentheses).

## Miscellany

Here are a few additional notations concerning functions.

- **Arg min and arg max.** Given a function $f$, we write $\arg\max f(x)$ to stand for the value of $x$ that makes $f(x)$ as large as possible. Similarly, $\arg\min f(x)$ is the value of $x$ that minimizes $f$. These appear constantly in machine learning: $\arg\min_\theta \mathcal{L}(\theta)$ — find the parameters $\theta$ that minimize loss.

- **Functions as superscripts.** On rare occasions, $x^{f}$ means $f(x)$.

- **Arrows for one-to-one and onto.** Sometimes the arrow in $f\colon A \to B$ is modified:

  $$f \colon A \xrightarrow{1:1} B \quad \text{or} \quad f \colon A \xrightarrow{\text{onto}} B$$

  Or with decorated arrows:

  $$f \colon A \hookrightarrow B \quad \text{(one-to-one / injection)} \qquad f \colon A \twoheadrightarrow B \quad \text{(onto / surjection)}$$

  A function that is both injective and surjective is a **bijection** — a perfect one-to-one correspondence between $A$ and $B$. Bijections have proper inverses.

- **Commutative diagrams.** Sometimes a figure illustrates multiple functions between sets with an announcement that "this diagram commutes." For example:

  ![Figure 6.2: A commutative diagram. Any path from one set to another, following the arrows and composing functions, gives the same result.](06 - Functions_images/img-0.jpeg)

  The capital letters are sets, the labeled arrows are functions. The arrow from $A$ to $B$ labeled $\alpha$ means $\alpha : A \to B$. The assertion that the diagram commutes means any path between two sets, formed by composing functions, gives the same result. For example:

  $$A \xrightarrow{\alpha} B \xrightarrow{\beta} C \xrightarrow{h} F \quad \text{and} \quad A \xrightarrow{f} D \xrightarrow{\gamma} E \xrightarrow{\delta} F$$

  The commutative property means $h \circ \beta \circ \alpha = \delta \circ \gamma \circ f$:

  $$\forall a \in A,\; (h \circ \beta \circ \alpha)(a) = (\delta \circ \gamma \circ f)(a).$$

- **Exact sequences.** Suppose $A_0, A_1, \ldots, A_n$ are algebraic structures (groups, modules, vector spaces) with homomorphisms $f_1, \ldots, f_n$:

  $$A_{0} \xrightarrow{f_{1}} A_{1} \xrightarrow{f_{2}} A_{2} \xrightarrow{f_{3}} \cdots \xrightarrow{f_{n}} A_{n}.$$

  To say this sequence is **exact** means $\operatorname{Im} f_i = \ker f_{i+1}$ for all $1 \leq i < n$. (The kernel: $\ker f = \{x : f(x) = 0\}$; see the Linear Algebra chapter.)

  Two important special cases:

  - $0 \longrightarrow A \xrightarrow{f} B$ being exact implies $\ker f = \{0\}$, so $f$ is **one-to-one** (injective).
  - $A \xrightarrow{f} B \longrightarrow 0$ being exact implies $\operatorname{Im} f = B$, so $f$ is **onto** (surjective).
