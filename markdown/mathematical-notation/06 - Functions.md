# Functions

## 1. Fundamentals

Basic notation. Many of the functions encountered in science and engineering take real numbers as input and return real numbers as output. The notation $f\colon\mathbb{R}\to\mathbb{R}$ means that $f$ is a function, that any real number may be the input to $f$, and that the output of $f$ lies in the set of real numbers.

More generally, if $A$ and $B$ are any sets, the notation $f\colon A\to B$ means that $f$ is a function that takes as input values from the set $A$ and returns values in the set $B$.

It is not necessary that every value of $B$ be realized as an output. For example, we may write $\cos\colon\mathbb{R}\to\mathbb{R}$ because the cosine function takes any real number as input and returns real numbers. Of course, the outputs of the cosine function lie in the interval $[-1,1]$.

The notation $f(x)$ indicates the value returned by the function $f$ when evaluated at the value $x$. That is, $f$ is the function while $f(x)$ is the value (typically a number) returned by the function.

An alternative notation for function evaluation is sometimes used, especially when the function is specified by a formula. The general form is this:

$\text{(some expression involving a variable }x)\Big{|}_{x=a}$

This means to evaluate the expression by substituting the value $a$ for the variable $x$. This type of notation is often used with Leibniz notation derivatives (see page 50).

The notation $y=f(x)$ is sometimes abbreviated to $x\mapsto y$; this is pronounced “$x$ maps to $y$.” Note that the function $f$ is absent from the expression $x\mapsto y$ so it is important to use this notation only when the function under consideration is unambiguously known. Alternatively, one may write $x\xmapsto{f}y$ to mean $f(x)=y$.

A function whose inputs and outputs are themselves functions is often called an *operator* or a *transform*. It is useful to typographically distinguish operators from functions of numbers; for example, one may capitalize the operator’s name. The application of an operator to a function might omit the parentheses: $Lf$ denotes the evaluation of the operator $L$ on the function $f$.


The notation $f(\cdot)$ is sometimes used to emphasize that $f$ is a function with the dot showing that an argument is expected. This notation is handy when referring to a function specified by non-letter symbols. For example, when discussing the absolute value function, one may write $|\cdot|$; this may be preferable to putting in a dummy variable between the bars or leaving a blank space.

Functions may take more than one argument, e.g., $f(x,y)$ is a function of two arguments. In this case the dot notation is handy in expressing which argument to the function is constant and which is variable. For example, $f(\cdot,b)$ expresses a function of one variable: the first argument of $f$ varies over its domain while the second argument is held constant at the value $b$.

For a function $f: X \to Y$, the image of $f$ is denoted $\operatorname{Im}(f)$:

$$
\operatorname{Im}(f) = \{y \in Y \mid \exists x \in X, f(x) = y\}.
$$

More generally, if $A \subseteq X$, then $f(A)$ stands for the set $\{f(a) \mid a \in A\}$. Thus $f(X) = \operatorname{Im}(f)$.

Functions are often specified by a single algebraic formula, but this is not necessary. A function may be defined piecewise like this:

$$
f(x) = \begin{cases}
e^{-1/x^2} &amp; \text{for } x &gt; 0 \\
0 &amp; \text{otherwise.}
\end{cases}
$$

**Composition and inversion.** If $f \colon A \to B$ and $g \colon B \to C$ then $g \circ f$ is a new function, the composition of $g$ and $f$, with $(g \circ f) \colon A \to C$ defined by

$$
(g \circ f)(x) = g[f(x)].
$$

The notation $f^{-1}(y)$ stands for the value $x$ such that $f(x) = y$; we call $f^{-1}$ the inverse of $f$.

If there is more than one value $x$ with $f(x) = y$, then $f^{-1}$ is not a function. Some people use the notation $f^{-1}(y)$ to stand for the set of all $x$ values that map to $y$. However, in some instances one coerces $f^{-1}$ to be a function by restricting the choice of $x$. For example, the arc sine function is $\sin^{-1}$. There are infinitely many values $x$ such that $\sin x = \frac{1}{2}$, but we restrict the choice of $x$ (in the case of arc sine) to be in the interval $(-\frac{\pi}{2}, \frac{\pi}{2}]$. In this case, arc sine becomes a proper function. Note that $f^{-1}(y)$ is undefined if there is no value $x$ such that $f(x) = y$.

The notation $f^{-1}$ may be applied to a set of values. For example, suppose $X$ and $Y$ are sets and $f: X \to Y$. If $B \subseteq Y$, then

$$
f^{-1}(B) = \{x \in X \mid f(x) \in B\}.
$$

The notation $f^2(x)$ sometimes means $[f(x)]^2$; this notation is used especially with trigonometric functions, e.g., $\sin^2\theta$. Thus we have an inconsistency because $f^{-1}(x)$ does not mean $1/f(x)$. (See the discussion of trigonometric functions later in this chapter.) However, in some contexts $f^2(x)$ means $(f \circ f)(x) = f[f(x)]$ in which case this notation is consistent with the meaning of $f^{-1}$.


## 2. Standard functions

### Functions of real numbers

There is a vast array of functions defined on the real numbers. Here we present a modest assortment that have their own special notation.

- Absolute value. For a real or complex number $x$, $|x|$ is the absolute value of $x$. (See also pages 14 and 17.)
- Square (and other) roots. For nonnegative real numbers $x$, the notation $\sqrt{x}$ is unambiguously the nonnegative square root of $x$. Likewise, for $x\geq 0$ and $n>0$, $\sqrt[n]{x}$ is the nonnegative $n^{\text{th}}$-root of $x$. (Note: $n$ need not be an integer.)

These may be written in exponential form: $\sqrt{x}=x^{1/2}$ and $\sqrt[n]{x}=x^{1/n}$.

When $x$ is a negative real number the situation becomes more complex (pun intended). In this case $\sqrt{x}=i\sqrt{|x|}$. If $n$ is an odd integer, $\sqrt[n]{x}$ is the unique (necessarily negative) real number $y$ so that $y^{n}=x$.

All other cases are ambiguous and handled by special convention.
- Signum (sign). The notation $\operatorname{sgn}x$ is the sign of $x$; that is,

\[ \operatorname{sgn}x=\begin{cases}1&\text{if }x>0,\\
0&\text{if }x=0\text{, and}\\
-1&\text{if }x<0.\end{cases} \]

It is called the *signum* function. Some people write the full word sign in place of $\operatorname{sgn}$.
- Exponential function. $\exp x$ stands for $e^{x}$. Sometimes people enclose the argument in curly braces like this: $\exp\{x\}$, but this is not necessary. If the argument is an algebraic expression, parentheses are a good alternative: $\exp\left(x^{2}+y^{2}\right)$.
- Logarithms. The notation $\log x$ is somewhat ambiguous. In science and engineering it typically means the base-10 logarithm. In mathematics, it typically means the base-$e$ (natural) logarithm.

The notation $\ln x$ stands for $\log_{e}x$ and $\lg x$ stands for $\log_{2}x$.

The function $\log^{*}x$ occurs in computer science. It stands for the number of times one must apply the $\log$ function to a number to reach a result that is less than 1. It is called the *log star* function.
- Trigonometric functions. The standard trigonometric functions are $\sin$, $\cos$, $\tan$, $\sec$, $\csc$, and $\cot$.

In mathematics, the arguments to trigonometric functions are usually expressed in radians; in science and engineering they might be expressed in degrees.

Greek letters, especially $\theta$, often appear as the argument to trigonometric functions, but this is a custom, not a requirement.


The notation $\sin^2 x$ means $(\sin x)^2$; however, the notation $\sin^{-1} x$ does not mean $1 / \sin x$. Rather, $\sin^{-1} x$ is the inverse sine (or arc sine) function. This may also be written $\arcsin x$ (although the $\sin^{-1} x$ notation is more common). Likewise we have $\arccos$, $\arctan$, and so forth.

- Hyperbolic trigonometric functions. The standard functions of trigonometry (sine, cosine, tangent, and so on) have hyperbolic "cousins". These are denoted by appending the letter 'h' after their names. For example:

$$
\sinh x = \frac{e^x - e^{-x}}{2} \quad \text{and} \quad \cosh x = \frac{e^x + e^{-x}}{2}.
$$

Also: $\tanh x = \sinh x / \cosh x$, $\operatorname{sech} x = 1 / \cosh x$, $\operatorname{csch} x = 1 / \sinh x$, and $\coth x = \cosh x / \sinh x$.

As with the ordinary trigonometric functions $\sinh^2 x$ means $(\sinh x)^2$ but $\sinh^{-1} x$ is the inverse function of $\sinh$.

- Sine cardinal. The function $\operatorname{sinc} x$ is called the sine cardinal. It is variously defined as

$$
\operatorname{sinc} x = \frac{\sin x}{x} \quad \text{or} \quad \operatorname{sinc} x = \frac{\sin \pi x}{\pi x}
$$

for $x \neq 0$ and $\operatorname{sinc} 0 = 1$.

- Floor, ceiling. The notation $\lfloor x \rfloor$ stands for the floor of $x$. This is the result of rounding $x$ down to the nearest integer. In older books this is written $[x]$.

The notation $\lceil x \rceil$ is the ceiling of $x$; it is the result of rounding $x$ up to the nearest integer. In older books this is written $\{x\}$.

Thus,

$$
\lceil e \rceil = \lceil 3 \rceil = \lfloor 3 \rfloor = \lfloor \pi \rfloor = 3.
$$

- Error function. $\operatorname{erf} x$ is a function that occurs in probability theory. It is defined by

$$
\operatorname{erf} x = \frac{2}{\sqrt{\pi}} \int_{0}^{x} \exp \left(- t^{2}\right) dt.
$$

- Gamma function. $\Gamma(x)$ is defined by

$$
\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t} dt.
$$

It is closely related to the factorial function.

- Beta function. $B(a, b)$ is defined by

$$
B(a, b) = \int_{0}^{1} t^{a-1} (1 - t)^{b-1} dt
$$

and is equal to $\Gamma(a)\Gamma(b) / \Gamma(a + b)$. It is closely related to binomial coefficients.


- Bessel functions. The following notations are used for Bessel functions:

- $J_{n}$: Bessel function of the first kind, order $n$.
- $Y_{n}$: Bessel function of the second kind, order $n$.
- $I_{n}$: modified Bessel function of the first kind, order $n$.
- $K_{n}$: modified Bessel function of the second kind, order $n$.

Closely related to these are the Hankel functions of the first and second kinds which are, respectively:

$$
H _ {n} ^ {(1)} (x) = J _ {n} (x) + i Y _ {n} (x) \quad \text{and} \quad H _ {n} ^ {(2)} (x) = J _ {n} (x) - i Y _ {n} (x).
$$

- Hypergeometric functions. The hypergeometric function ${}_{2}F_{1}$ takes three "parameters" $(a, b, \text{and } c)$ and one argument $(x)$:

$$
{ } _ { 2 } F _ { 1 } ( a , b ; c ; x ) = \sum _ { k = 0 } ^ { \infty } \frac { a ^ { ( k ) } b ^ { ( k ) } } { c ^ { ( k ) } } \cdot \frac { x ^ { k } } { k ! } .
$$

For an explanation of the rising factorial notation $a^{(k)}$ see the entry on factorial functions on the next page.

The notation ${}_{2}F_{1}(a,b;c;x)$ is also more elaborately written like this:

$$
{ } _ { 2 } F _ { 1 } \left( \begin{array} { c } a , b \\ c \end{array} \right| x
$$

This notation more clearly illustrates the placement of $a$ and $b$ in the numerator and $c$ in the denominator. The LaTeX code (which relies on the amsmath package) to produce this formula is:

$\{_{-}2\} F_{-}1 \backslash left(\backslash genfrac{.} \{|\} \{\emptyset pt\} \{\} \{a,b\} \{c\} x \backslash right)$

More generally, if $p$ and $q$ are nonnegative integers, the function ${}_pF_q$ has $p$ upper indices ($a_1$ through $a_p$) and $q$ lower indices ($b_1$ through $b_q$) and is notated like this:

$$
{ } _ { p } F _ { q } ( a _ { 1 } , a _ { 2 } , \ldots , a _ { p } ; b _ { 1 } , b _ { 2 } , \ldots , b _ { q } ; x ) = { } _ { p } F _ { q } \left( \left. \begin{array} { c } ( a _ { 1 } , a _ { 2 } , \ldots , a _ { p } ) \\ ( b _ { 1 } , b _ { 2 } , \ldots , b _ { q } ) \end{array} \right| x \right)
$$

and is given by the formula

$$
\sum_ {k = 0} ^ {\infty} \frac {a _ {1} ^ {(k)} a _ {2} ^ {(k)} \cdots a _ {p} ^ {(k)}}{b _ {1} ^ {(k)} b _ {2} ^ {(k)} \cdots b _ {q} ^ {(k)}} \cdot \frac {x ^ {k}}{k !}.
$$

- Riemann zeta function. The function $\zeta(z)$ is known as the Riemann zeta function. For an integer $n \geq 2$ we have

$$
\zeta (n) = \sum_ {k = 0} ^ {\infty} \frac {1}{k ^ {n}}
$$

and is defined for arbitrary complex $z$ by analytic extension.


- Dirac delta "function". The final entry for this section is given with some trepidation because it is not a function; however, since the word function is traditionally (albeit erroneously) used with its name, we recall here the Dirac  $\delta$ -function. Dirac's  $\delta$  can be imagined as a function that takes the value zero for all nonzero arguments, but  $\delta(0)$  is infinite. Nevertheless, the integral of  $\delta$  (the area under its "curve") is 1. The  $\delta$  function often appears inside an integral; given a function  $f: \mathbb{R} \to \mathbb{R}$  we have

$$
\int_ {- \infty} ^ {\infty} f (x) \delta (x) d x = f (0).
$$

The Dirac  $\delta$  may be thought of as the derivative of the Heaviside function  $H$  defined by

$$
H (x) = \left\{ \begin{array}{l l} 1 &amp; \text { for } x \geq 0 \\ 0 &amp; \text { for } x &lt; 0. \end{array} \right.
$$

Notice that

$$
H (x) = \int_ {- \infty} ^ {x} \delta (t) d t
$$

and in that sense the derivative of  $H$  is  $\delta$ .

In case one wants a spike at a value other than 0 (say at  $c$ ) one can use  $\delta(x - c)$  which is sometimes denoted  $\delta_c(x)$ .

Functions of integers. The following are some functions that are defined only for integer values.

- Factorial and related functions. For a nonnegative integer  $n$ , the notation  $n!$  is pronounced  $n$ -factorial and is defined by  $0! = 1$  and for  $n &gt; 0$

$$
n! = n (n - 1) (n - 2) \dots 2 \cdot 1.
$$

It is closely related to the gamma function:  $n! = \Gamma (n + 1)$

The use of the exclamation point for the factorial function is universally accepted, but it is interesting to note that this was not always the case; see Figure 6.1. For more historical tidbits on notation see [1] (and also [10]).

$$
f (x) = f (a) + \frac {(x - a)}{\lfloor 1 \rfloor} f ^ {\prime} (a) + \frac {(x - a) ^ {2}}{\lfloor 2 \rfloor} f ^ {\prime \prime} (a) + \frac {(x - a) ^ {3}}{\lfloor 3 \rfloor} f ^ {\prime \prime \prime} (a) + \dots
$$

FIGURE 6.1. The formula for the Taylor series of a function as it appears in [4]. Note the notation for  $n!$ .

The notation  $n!!$  is the double factorial; here the factors descend by two. For example,  $7!! = 7 \times 5 \times 3 \times 1$ .

For a real number $x$ and a nonnegative integer $k$, the notations $x^{(k)}$ and $x_{(k)}$ are known respectively as the rising and falling factorial functions and are given by the formulas:

$$
x^{(k)} = x(x + 1) \cdots (x + k - 1) = \prod_{j=0}^{k-1} (x + j) \quad \text{and}
$$

$$
x_{(k)} = x(x - 1) \cdots (x - k + 1) = \prod_{j=0}^{k-1} (x - j).
$$

Note that $x^{(0)} = x_{(0)} = 1$.

Alternative (and especially clear) notations for rising/falling factorials are these:

$$
x^{\overline{k}} = x^{(k)} \qquad \text{and} \qquad x^k = x_{(k)}.
$$

In addition, the notations $P(n,k)$, $P_{n,k}$, $P_{k,n}$, and ${}_nP_k$ are also used for falling factorial $n_{(k)}$, but these are mostly seen in older works. Here the letter $P$ stands for permutation and $P(n,k)$ is understood to mean “the number of permutations of $n$ things taken $k$ at a time.” We discourage the use of $P$ for this purpose.

Finally, and unfortunately, the notation $(x)_k$ (known as the Pochhammer symbol) is also used for the rising factorial function.

- **Binomial coefficient.** The binomial coefficient $\binom{n}{k}$ is defined for nonnegative integers $n$ and $k$ to be the number of $k$-element subsets of an $n$-element set. For $0 \leq k \leq n$ we have

$$
\binom{n}{k} = \frac{n!}{k! (n - k)!}
$$

and for $k &gt; n$ we have $\binom{n}{k} = 0$.

The letter $C$ is also used for the binomial coefficient in these various forms: $C(n, k)$, $C_{n,k}$, $C_{k,n}$, and ${}_nC_k$. In this context $C$ stands for combinations and $C(n, k)$ stands for “the number of combinations of $n$ things taken $k$ at a time.” We grudgingly acknowledge the utility of $C(n, k)$ (especially for communicating mathematics in an email) but strongly encourage the exclusive use of $\binom{n}{k}$.

There are some additional notations closely related to binomial coefficients.

- **Multinomial coefficient.** For nonnegative integers $n, k_1, k_2, \ldots, k_t$ with $k_1 + k_2 + \cdots + k_t = n$ we have

$$
\binom{n}{k_1 \ k_2 \ \cdots \ k_t} = \frac{n!}{k_1! k_2! \cdots k_t!}.
$$

- **Multichoose.** The notation $\left(\binom{n}{k}\right)$ stands for the number of $k$-element multisets that can be formed with elements drawn from


an $n$-element set. The multichoose notation is related to the ordinary binomial coefficient by the following formula:

$$
\binom{n}{k} = \binom{n + k - 1}{k}.
$$

- $q$-binomial coefficient. For nonnegative integers $n, k$ and a variable $q$ the notation $\binom{n}{k}_q$ is the $q$-binomial coefficient defined by

$$
\binom{n}{k}_q = \begin{cases}
\frac{(1 - q^n)(1 - q^{n-1}) - (1 - q^{n-k+1})}{(1 - q)(1 - q^2) - (1 - q^k)} &amp; \text{if } k \leq n \text{ and } \\ 0 &amp; \text{otherwise.}
\end{cases}
$$

- Stirling numbers. Stirling numbers come in two varieties. For nonnegative integers $n, k$ we have:

- Stirling numbers of the first kind are denoted $s(n, k)$. It is the coefficient of $x^k$ in the polynomial $(x)_n = x(x - 1) \cdots (x - n + 1)$. We use $c(n, k)$ to denote the unsigned Stirling numbers of the first kind. It equals $|s(n, k)|$ and is the number of permutations in $S_n$ (the set of all permutations of $\{1, 2, \ldots, n\}$—see page 43) that have exactly $k$ cycles. It is also denoted $\binom{n}{k}$.
- Stirling numbers of the second kind are denoted $S(n, k)$. They represent the number of partitions of an $n$-element set into exactly $k$ parts. An alternative notation is $\binom{n}{k}$.

- Divisibility. For integers $a$ and $b \neq 0$, the expression $b|a$ means $a$ is divisible by $b$, i.e., there is an integer $q$ such that $a = bq$. The statement $b|a$ is read “$b$ divides $a$.”

- Mod. For integers $a, b$ with $b &gt; 0$ the expression $a \bmod b$ is the remainder when $a$ is divided by $b$. Specifically, dividing $a$ by $b$ yields integers $q$ (quotient) and $r$ (remainder) such that

$$
a = qb + r \quad \text{and} \quad 0 \leq r &lt; b.
$$

The value of $a \bmod b$ is the remainder $r$. For example $13 \bmod 10 = 3$ and $-10 \bmod 9 = 8$ (because $-10 = -2 \times 9 + 8$).

In addition to the function mod, there is also a relation on integers called congruence that employs the term mod. For a positive integer $n$ and any integers $a$ and $b$ we write

$$
a \equiv b \pmod{n} \quad \text{or more simply} \quad a \equiv b \quad (n)
$$

to mean $a - b$ is divisible by $n$ (i.e., $n|a - b$). When the modulus, $n$, is understood the (mod $n$) or ($n$) portion may be omitted.

- GCD and LCM. For integers $n$ and $m$, the notation $\gcd(n, m)$ is the greatest common divisor of $n$ and $m$. In number theory, this is abbreviated to $(n, m)$.

The notation $\operatorname{lcm}(n, m)$ is the least (positive) common multiple of $n$ and $m$.


- Euler's totient. For a positive integer $n$, $\varphi(n)$ is the number of integers in $[n] = \{1, 2, \ldots, n\}$ that are relatively prime to $n$. This function is known as Euler's totient and the symbol $\varphi$ is a stylized Greek phi, $\phi$. Some people use the ordinary $\phi$ for this function.
- Legendre/Jacobi symbol. If $p$ is an odd prime and $a$ is an integer, the notation $\left(\frac{a}{p}\right)$ is known as the Legendre symbol defined by

$$
\left(\frac {a}{p}\right) = \left\{ \begin{array}{l l} 0 &amp; \text{if } a \equiv 0 \pmod{p}, \\ 1 &amp; \text{if } a \text{ is a quadratic residue mod } p \text{ and } a \not\equiv 0, \text{ and} \\ - 1 &amp; \text{otherwise}. \end{array} \right.
$$

Some authors write the Legendre symbol horizontally: $(a|p)$.

If the lower entry in $\left(\frac{a}{n}\right)$ is not prime, then this notation is known as the Jacobi symbol. If the prime factorization of $n$ is $p_1^{e_1}p_2^{e_2}\dots p_t^{e_t}$, then

$$
\left(\frac {a}{n}\right) = \left(\frac {a}{p _ {1}}\right) ^ {e _ {1}} \left(\frac {a}{p _ {2}}\right) ^ {e _ {2}} \dots \left(\frac {a}{p _ {t}}\right) ^ {e _ {t}}.
$$

### Other standard functions

- Identity function. For a set $A$, the notation $\mathrm{Id}_A$ is the identity function on $A$, i.e., $\mathrm{Id}_A: A \to A$ by $\mathrm{Id}_A(a) = a$ for all $a \in A$.
- Characteristic function. Given a set $A$, often a subset of the real numbers, $\chi_A$ denotes the characteristic function of $A$ given by

$$
\chi_ {A} (x) = \left\{ \begin{array}{l l} 1 &amp; \text{if } x \in A, \text{ and} \\ 0 &amp; \text{otherwise}. \end{array} \right.
$$

Some people write $\mathbf{1}_A$ for the characteristic function of $A$.

## 3. Classes of functions

The notation $C^k$ denotes those functions for whose $k^{\mathrm{th}}$ derivative is defined and continuous. Thus $C^0$ stands for the class of continuous functions, $C^1$ stands for the class of differentiable functions whose derivatives are continuous. Naturally,

$$
C ^ {0} \supset C ^ {1} \supset C ^ {2} \supset \dots .
$$

For functions defined only on an interval $[a, b]$, we may write $C^k([a, b])$. The notation $C^k(\mathbb{R})$ is equivalent to $C^k$.

The class $C^\infty$ contains those functions for which derivatives of all orders exist (and are therefore continuous).

The notation $L^p$, where $p$ is a positive real number, denotes the class of functions for which

$$
\int_ {- \infty} ^ {\infty} | f (x) | ^ {p} d x &lt;   \infty .
$$


This notation may be restricted to an interval: $L^p([a, b])$ stands for those functions for which

$$
\int_{a}^{b} |f(x)|^{p} dx &lt; \infty.
$$

Closely related to this is the notation $\ell^p$. This stands for the class of sequences $a_0, a_1, a_2, \ldots$ for which

$$
\sum_{k=0}^{\infty} |a_k|^p &lt; \infty.
$$

## 4. Polynomials, power series, and rational functions

**Polynomials.** A polynomial is a function of the form

$$
p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0.
$$

Some authors prefer that the subscripts on the coefficients run counter to the exponents, like this:

$$
p(x) = a_0 x^n + a_1 x^{n-1} + \cdots + a_{n-1} x + a_n.
$$

The degree of a polynomial is denoted $\deg p(x)$; it is the largest exponent on $x$ associated with a nonzero coefficient. If $p(x) = 0$ (the zero polynomial), then $\deg p$ is either undefined or $-\infty$.

The set of all polynomials in the variable $x$ with real coefficients is denoted $\mathbb{R}[x]$. More generally, if $R$ is any ring$^2$, then $R[x]$ is the set of all polynomials in the variable $x$ with coefficients in $R$.

Polynomials may have more than one variable, e.g., $x^3 y^2 - 3xy + 2x - 3$. The notation $R[x,y]$ stands for the set of all polynomials with coefficients from $R$ in the variables $x$ and $y$.

Just as we have the notions of divisibility $|$ and mod for integers, the same notions apply to polynomials:

- $p(x)|q(x)$ means there is a polynomial $a(x)$ so that $a(x)p(x) = q(x)$.
- $p(x) \equiv q(x) \pmod{a(x)}$ means that $a(x)|p(x) - q(x)$.
- $R[x]/(a(x))$ is the set of polynomials (with coefficients from $R$) taken modulo $a(x)$. For example, $Z[x]/(x^2 + 1)$ is, effectively, the Gaussian integers.

Certain families of polynomials have their own notation. These include the following:

- **Chebyshev polynomials.** The degree-$n$ Chebyshev polynomial of the first kind is denoted $T_n(x)$ and the degree-$n$ polynomial of the second kind is denoted $U_n(x)$.

$^2$See footnote on page 19.


- Hermite polynomials. The degree-$n$ Hermite polynomial is denoted $H_{n}(x)$. There are two variations on how these are defined (for the probability community and the physics community).
- Laguerre Polynomials. The degree-$n$ Laguerre polynomial is denoted $L_{n}(x)$.
- Legendre polynomials. The degree-$n$ Legendre polynomial is denoted $P_{n}(x)$.

Power series. A power series is a function of the form

$$
f(x) = a_{0} + a_{1}x + a_{2}x^{2} + \cdots.
$$

The set of all power series, with coefficients drawn from a ring $R$, is denoted $R[[x]]$. These are sometimes called formal power series when convergence is not at issue.

Rational functions. A rational function is the ratio of two polynomials:

$$
f(x) = \frac{a_{n}x^{n} + a_{n-1}x^{n-1} + \cdots + a_{1}x + a_{0}}{b_{m}x^{m} + b_{m-1}x^{m-1} + \cdots + b_{1}x + b_{0}}.
$$

The set of all rational functions with real coefficients is denoted $\mathbb{R}(x)$. In general, if $F$ is any field$^3$, $F(x)$ is the set of rational functions in the variable $x$ with coefficients drawn from $F$.

## 5. Miscellany

Here are a few additional notations concerning functions one might encounter.

- Arg min and arg max. Given a function $f$, we write $\arg \max f(x)$ to stand for the value of $x$ that makes $f(x)$ as large as possible. Similarly, $\arg \min f(x)$ is the value of $x$ that minimizes $f$.
- Functions as superscripts. On rare occasions one may see the application of a function to its argument—usually written $f(x)$—expressed by writing the function as an exponent. That is, $x^{f}$ means $f(x)$.
- Arrows to denote one-to-one and onto. Sometimes the arrow in $f\colon A \to B$ is modified to give special meaning. This can be done by writing words above the arrow, such as

$$
f \colon A \xrightarrow{1:1} B \quad \text{or} \quad f \colon A \xrightarrow{\text{onto}} B
$$

to indicate that $f$ is one-to-one or onto, respectively. However, some people "decorate" the arrow to give the same meanings:

$$
f \colon A \hookrightarrow B \quad \text{or} \quad f \colon A \twoheadrightarrow B
$$

where the hooked arrow means "one-to-one" and the double-headed arrow means "onto".

$^3$See footnote on page 18.


Incidentally, a one-to-one function is called an injection and an onto function is called a surjection. While these terms have waning popularity, the term bijection—a function that is both an injection and a surjection—is commonly used.

- Commutative diagrams. Sometimes one may encounter a figure illustrating multiple functions between various sets with an announcement that "this diagram commutes." For example, the following is such a commutative diagram:

![img-0.jpeg](06 - Functions_images/img-0.jpeg)

In this diagram, the capital letters stand for sets and the labeled arrows stand for functions. The arrow from  $A$  to  $B$  labeled  $\alpha$  means that  $\alpha$  is a function from  $A$  to  $B$ , i.e.,  $\alpha : A \to B$ . Likewise  $h : C \to F$ , and so on. The assertion that this diagram commutes means that any path from one set to another, formed by composing functions, gives the same result. In this diagram there are several paths from  $A$  to  $F$  including

$$
A \xrightarrow {\alpha} B \xrightarrow {\beta} C \xrightarrow {h} F \quad \text {a n d} \quad A \xrightarrow {f} D \xrightarrow {\gamma} E \xrightarrow {\delta} F.
$$

The commutative property in this case means that the compositions  $h \circ \beta \circ \alpha$  and  $\delta \circ \gamma \circ f$  are equal, i.e.,

$$
\forall a \in A, (h \circ \beta \circ \alpha) (a) = (\delta \circ \gamma \circ f) (a).
$$

- Exact sequences. Another function diagram notation is concept of an exact sequence of functions. Suppose  $A_0, A_1, \ldots, A_n$  are algebraic structures (e.g., groups, modules, vector spaces) and we have functions  $f_1, \ldots, f_n$  arranged like this:

$$
A _ {0} \xrightarrow {f _ {1}} A _ {1} \xrightarrow {f _ {2}} A _ {2} \xrightarrow {f _ {3}} \dots \xrightarrow {f _ {n}} A _ {n}.
$$

That is  $f_{i}: A_{i-1} \to A_{i}$ . In this algebraic context, it is understood that the functions are homomorphisms.

To say that this sequence is exact means  $\operatorname{Im} f_i = \ker f_{i+1}$  for all  $1 \leq i &lt; n$ . (The kernel of  $f$  is the set  $\ker f = \{x : f(x) = 0\}$ . See page 43.) In other words, for all  $i = 1, 2, \ldots, n-1$  and for all  $a \in A_{i-1}$ , we have  $f_{i+1}[f_i(a)] = 0$  (or the identity element of  $A_{i+1}$ ).

This notion of an exact sequence has two interesting special cases. Suppose we have that

$$
0 \longrightarrow A \xrightarrow {f} B
$$

4Strictly speaking, the leftmost set in this sequence should be written
\{0\}


is exact. The image of the unnamed first function must be the 0-element of $A$ and so the exactness property requires that $\ker f = \{0\}$ which, in turn, implies that $f$ is one-to-one.

On the other hand, suppose

$$
A \xrightarrow {f} B \xrightarrow {} 0
$$

is an exact sequence. This means that the entire space $B$ is mapped to 0 by the unnamed function on the right, and so $\operatorname{Im} f = B$; that is, $f$ must be onto.
