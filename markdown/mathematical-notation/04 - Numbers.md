# Numbers

Every extension of the number system was forced by an equation that couldn't be solved. The naturals ($\mathbb{N}$) handle "how many?" but $x + 3 = 1$ has no natural solution, so we invent the negative integers and get $\mathbb{Z}$. Then $2x = 3$ demands fractions: $\mathbb{Q}$. But $x^2 = 2$ has no rational solution (Hippasus proved this around 500 BCE, and legend says the Pythagoreans drowned him for it), so we fill in the gaps and get $\mathbb{R}$. Finally, $x^2 = -1$ has no real solution, so we append $i = \sqrt{-1}$ and arrive at $\mathbb{C}$.

Each extension is strictly larger, and each preserves all the arithmetic that came before:

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

This chapter covers the notation for these number systems — how to write them, name their parts, and operate on them. If you've used Python's `int`, `float`, `complex`, and `fractions.Fraction`, you've already worked with the first four levels of this tower.

## 1. Real numbers

### Writing numbers

The set of all real numbers is denoted $\mathbb{R}$. Real numbers are typically written in decimal notation starting with a sign (optional if positive, mandatory if negative), a finite list of digits, a decimal point, and then either finitely many or infinitely many more digits.

An infinite repeating block of decimals is often denoted with an overline:

$$
45.07123123123123\ldots=45.07\overline{123}
$$

When a decimal number is between 0 and 1, it is preferable to include a leading zero digit. Thus 0.123 is preferred to .123 as the leading zero alerts the reader to the otherwise easily missed decimal point.

For numbers with more than three digits to the left of the decimal point, commas are used to improve readability: 1,332,443. However, for numbers between 1000 and 9999 the comma is often omitted. In some cases, a small space is used instead of a comma: 1 332 443.

The use of a period as the decimal point is not universal. In many countries a comma is used instead (e.g., $\pi\approx 3{,}14159$) and the period is used to separate groups of three digits (e.g., 1.332.443).

### Percentages and scientific notation

The per cent symbol means "divided by 100". The following numbers are exactly the same; they are simply written differently:

$$
\frac{1}{4}\qquad 0.25\qquad 25\%
$$

Scientific notation is often used to express real numbers, especially if they are very large or very small. For example:

$$
1.23\times 10^{7}=12{,}300{,}000\quad\text{and}\quad 4.56\times 10^{-4}=0.000456
$$

The number before the power of 10 is usually at least 1 and less than 10. Computer programs may output numbers in scientific notation with an E (or e) to mark the power of ten:

| Mathematical notation | Programming notation |
| --- | --- |
| $1.23\times 10^{7}$ | `1.23E07` or `1.23e7` |
| $4.56\times 10^{-4}$ | `4.56E-04` or `4.56e-4` |

In Python, `1.23e7` is a valid `float` literal — the `e` means "$\times 10$ to the power of."

Engineering notation is a variant form of scientific notation in which the exponent on 10 must be a multiple of three (matching SI prefixes like kilo, mega, giga):

| Form | Example |
| --- | --- |
| Scientific notation | $6.022 \times 10^{23}$ |
| Engineering notation | $602.2 \times 10^{21}$ |

For engineering notation, the factor in front of the power of 10 should be at least 1 and less than 1000.

### Number bases

Sometimes it is useful to express numbers in bases other than ten. There are a few ways in which this is indicated:

- The base of the number is written as a word subscript like this: $14_{\mathrm{FIVE}}$ or $0.202020_{\mathrm{THREE}}$.
- The base of the number is written as a numerical subscript, like this: $1011_{2}$.
- In computer science, base-16 (hexadecimal) integers are written with a $\mathbf{0x}$ prefix. For example: $\mathbf{0x1A2B93}$. The letters A through F stand for digits 10 through 15.
- In computer science, base-8 (octal) integers are written with a leading zero (C convention) or $\mathbf{0o}$ prefix (Python convention). For example: `0o177` in Python.

Python supports all of these:

| Base | Math notation | Python literal | Python converter |
| --- | --- | --- | --- |
| Binary (2) | $1011_2$ | `0b1011` | `bin(11)` |
| Octal (8) | $0177_8$ | `0o177` | `oct(127)` |
| Hex (16) | $\mathbf{0x1A}$ | `0x1A` | `hex(26)` |

### Continued fractions

Some real numbers are expressed using continued fractions. For example:

![img-0.jpeg](04 - Numbers_images/img-0.jpeg)

This may be written compactly like this:

$$
1 + \frac {1}{2 +} \frac {1}{3 +} \frac {1}{4 +} \dots
$$

In these examples, the numerators are all 1s, but this is not necessary. However, in that case, continued fractions may also be expressed this way: $[1; 2, 3, 4, \ldots]$.

### Further number notation

The absolute value of a real number $x$ is denoted $|x|$. In Python: `abs(x)`.

The plus-minus notation $\pm$ is used to indicate two different values. Thus, $\pm 2$ stands for 2 and $-2$. It is a useful shorthand to encapsulate two different values in a single expression. For example, the solutions to the equation $x^{2} - 2x - 2 = 0$ are $1 \pm \sqrt{3}$; this means that both $1 + \sqrt{3}$ and $1 - \sqrt{3}$ are solutions.

Using the symbol $\pm$ twice in a single expression can be ambiguous. Consider $\pm 1 \pm \sqrt{5}$. This might either mean the two values $1 + \sqrt{5}$ and $-1 - \sqrt{5}$, or it might also include the additional values $1 - \sqrt{5}$ and $-1 + \sqrt{5}$. The meaning needs to be derived from context.

The minus-plus symbol $\mp$ means the same thing as $\pm$. It is typically used in conjunction with $\pm$ and has the opposite sign. Thus $\pm 3 \mp \sqrt{7}$ means the two values $3 - \sqrt{7}$ and $-3 + \sqrt{7}$.

### Equality notation

The equal sign $=$ has two meanings. One asserts that two values are equal as in $3 + 4 = 7$. The other meaning occurs when defining values as in "Let $x = 1 + \sqrt{5}$." Some people use the notation $:=$ when defining a value. The symbols $\triangleq$ and $\stackrel{\text{def}}{=}$ are also used as defining equal signs.

A triple line equal sign $\equiv$ is used to mean *identically equal to*. For example, an equation may be written as $x^{2} - 2 = 0$ which is true for some values of $x$. However, when we write $\sin^2 x + \cos^2 x \equiv 1$, we assert the equation is true for all values of $x$.

| Symbol | Meaning | Programming analogue |
| --- | --- | --- |
| $=$ | equality or assignment | `==` (test) or `=` (assign) |
| $:=$ | definition | `=` (first assignment) |
| $\equiv$ | identically equal (for all values) | identity / invariant |
| $\approx$ | approximately equal | `math.isclose(a, b)` |
| $\neq$ | not equal | `!=` |

## 2. Subsets of the reals

The integers are the real numbers that can be expressed without any digits after the decimal point. The set of integers is denoted $\mathbb{Z}$ (from German *Zahlen*, "numbers"):

$$
\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}
$$

There is no standard definition for the term *natural number*. We prefer the definition that a natural number is a nonnegative integer. Thus $\mathbb{N} = \{0,1,2,3,\ldots\}$. However, some mathematicians prefer not to include 0 in this set.$^1$

The rational numbers are those real numbers that can be expressed as the ratio of integers $a / b$ where $b$ is nonzero. The set of rational numbers is denoted $\mathbb{Q}$ (from German *Quotient*). This may be written:

$$
\mathbb{Q} = \{x \in \mathbb{R} : x = a / b \text{ where } a, b \in \mathbb{Z} \text{ and } b \neq 0\}
$$

### The number-set tower

These sets of numbers are nested:

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

Each number type in Python maps to one of these sets:

| Math set | Name | Python type | Key property |
| --- | --- | --- | --- |
| $\mathbb{N}$ | Naturals | `int` ($\geq 0$) | Counting |
| $\mathbb{Z}$ | Integers | `int` | $+$, $-$, $\times$ closed |
| $\mathbb{Q}$ | Rationals | `fractions.Fraction` | Division closed (except $\div 0$) |
| $\mathbb{R}$ | Reals | `float` (approximate) | Limits, continuity |
| $\mathbb{C}$ | Complex | `complex` | Every polynomial has a root |

Python's `int` has arbitrary precision (no overflow), which is better than $\mathbb{Z}$ — mathematically $\mathbb{Z}$ is infinite and so is Python's `int`. But `float` is only an approximation of $\mathbb{R}$: it has finite precision (64-bit IEEE 754), so $0.1 + 0.2 \neq 0.3$ in floating point.

We can explore this tower and complex arithmetic directly:

```python
<!-- include: code/mathematical-notation/04 - Numbers/01_python.py -->
```

### Superscript conventions

Appending a star superscript to these may have various meanings:

- $\mathbb{R}^*$, $\mathbb{C}^*$, and so on denote the nonzero elements of the set. [Note: $\mathbb{C}$ stands for the set of complex numbers; see below.]
- $\mathbb{R}^*$, $\mathbb{C}^*$, and so on denote the invertible elements of the set. In the case of the fields $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$, this is the same as the nonzero elements. In the case of the integers, $\mathbb{Z}^*$ would mean $\{-1, 1\}$. For this meaning, we prefer a $\times$ superscript: $\mathbb{Z}^\times$.
- $\mathbb{C}^*$ is sometimes used to denote $\mathbb{C} \cup \{\infty\}$ (though we recommend $\hat{\mathbb{C}}$ or $\overline{\mathbb{C}}$ for this). Similarly, $\mathbb{R}^*$ is sometimes used to denote $\mathbb{R} \cup \{-\infty, +\infty\}$ (but we prefer $\overline{\mathbb{R}}$).
- $\mathbb{Z}^*$ is used by some authors to denote the nonnegative integers, $\{0, 1, 2, \ldots\}$ (but we prefer $\mathbb{N}$).
- Finally, ${}^{*}\mathbb{R}$ denotes the nonstandard reals (see section 7).

$^1$The 1993 ANSI/IEEE standard excludes 0 from $\mathbb{N}$ whereas the ISO standard includes 0. The ISO recommends $\mathbb{N}^*$ for the set of positive integers.

Appending a $+$ superscript or subscript to $\mathbb{R}$ generally denotes the positive reals: $\mathbb{R}^+$ or $\mathbb{R}_+$. However, it is sometimes convenient to include 0; in that way, $\mathbb{R}_+^n$ would denote the nonnegative orthant. Whether or not to include 0 is a matter of convenience. Likewise $\mathbb{Q}^+$ and $\mathbb{Z}^+$ denote the positive rationals and integers respectively.

### Intervals

Intervals of real numbers are denoted with parentheses and brackets. A parenthesis indicates the endpoint is *not* included; a bracket indicates it *is* included:

| Notation | Set | Type |
| --- | --- | --- |
| $[a, b]$ | $\{x \in \mathbb{R} : a \leq x \leq b\}$ | Closed |
| $(a, b)$ | $\{x \in \mathbb{R} : a < x < b\}$ | Open |
| $[a, b)$ | $\{x \in \mathbb{R} : a \leq x < b\}$ | Half-open |
| $(a, b]$ | $\{x \in \mathbb{R} : a < x \leq b\}$ | Half-open |

Some people use brackets facing the wrong direction to indicate non-inclusion: $[a, b[$ means $[a, b)$, $]a, b]$ means $(a, b]$, and $]a, b[$ means $(a, b)$. This is the French/ISO convention.

The symbols $-\infty$ and $\infty$ may be used for the ends of an interval:

$$
[1, \infty) = \{x \in \mathbb{R} : x \geq 1\} \quad \text{and} \quad (-\infty, 2) = \{x \in \mathbb{R} : x < 2\}
$$

Although one could write $(-\infty, \infty)$, this indicates all real numbers and it's clearer simply to write $\mathbb{R}$.

Python's `range(a, b)` is the discrete analogue of $[a, b)$ — half-open on the right.

## 3. "Famous" real numbers

Some real numbers have their own special notation. Here are the ones you will encounter most often:

| Constant | Symbol | Approximate value | Definition |
| --- | --- | --- | --- |
| Euler's number | $e$ | 2.71828 | $\lim_{n\to\infty}(1 + 1/n)^n$ |
| Pi | $\pi$ | 3.14159 | circumference / diameter |
| Euler-Mascheroni | $\gamma$ | 0.57722 | $\lim_{n\to\infty}\bigl[\sum_{k=1}^n \frac{1}{k} - \ln n\bigr]$ |
| Golden ratio | $\phi$ | 1.61803 | $(1 + \sqrt{5})/2$ |

Note that various scientific disciplines reserve certain letters for physical constants (such as $c$ for the speed of light).

The golden ratio satisfies the elegant equation $\phi^2 = \phi + 1$, meaning it is a root of $x^2 - x - 1 = 0$. It appears in the Fibonacci sequence: the ratio $F_{n+1}/F_n$ converges to $\phi$.

Euler's identity connects all four constants (plus 0 and 1) in one equation:

$$
e^{i\pi} + 1 = 0
$$

## 4. Complex numbers

The complex numbers are created by appending a new object, $i$, to the real numbers and following the natural consequence of algebraic steps. Here, $i$ stands for a number with the property $i^{2}=-1$. The result is a collection of numbers of the form $a+bi$ where $a,b\in\mathbb{R}$. The set of complex numbers is denoted $\mathbb{C}$.

Some people prefer to write the imaginary unit before its coefficient, like this: $a+ib$.

**Special note:** Electrical engineers use $i$ to represent current, and so they use the letter $j$ to represent $\sqrt{-1}$. For them, complex numbers are written as $a+bj$. Python follows the engineering convention: `2+3j`.

### The complex plane

Just as real numbers are visualized as a (number) line, the complex numbers are visualized as a (complex) plane in which the number $a+bi$ corresponds to the point with coordinates $(a,b)$.

### Absolute value, conjugate, and parts

The *absolute value* (or *magnitude*) of $z=a+bi$ is denoted $|z|=|a+bi|$ and equals $\sqrt{a^{2}+b^{2}}$. It is the distance from the point $(a,b)$ to the origin.

The *(complex) conjugate* of $z=a+bi$ is denoted with an overline: $\overline{z}=\overline{a+bi}=a-bi$. The conjugate of $z$ is also denoted $z^{*}$.

A fancy R and a fancy I are used to denote the real and imaginary parts:

$$
\Re z=a\qquad\text{and}\qquad\Im z=b
$$

The abbreviations $\text{Re}$ and $\text{Im}$ are also used. In Python: `z.real` and `z.imag`.

| Math | Python | Example for $z = 2+3i$ |
| --- | --- | --- |
| $\|z\|$ | `abs(z)` | `3.6056` |
| $\overline{z}$ | `z.conjugate()` | `(2-3j)` |
| $\Re z$ | `z.real` | `2.0` |
| $\Im z$ | `z.imag` | `3.0` |

### Polar form

Points in the plane may also be expressed in polar coordinates $(r,\theta)$ where $r$ is the distance from the origin and $\theta$ is the counterclockwise angle from the positive $x$-axis. If a point has rectangular coordinates $(a,b)$ and polar coordinates $(r,\theta)$, then:

$$
a=r\cos\theta\qquad\text{and}\qquad b=r\sin\theta
$$

This extends to complex numbers: every complex number may be expressed as $re^{i\theta}$ because

$$
re^{i\theta}=r\,[\cos\theta+i\sin\theta]=(r\cos\theta)+(r\sin\theta)i=a+bi
$$

Thus $r=|a+bi|$. The angle $\theta$ is called the *argument* or the *phase angle* of $a+bi$; this is denoted $\arg(a+bi)$. Typically one defines $\arg z$ to lie in the interval $[0,2\pi)$ or in the interval $(-\pi,\pi]$. See Figure 1 below.

The value $e^{i\theta}$ is sometimes written $\operatorname{cis}\theta$. The notation $\operatorname{cis}$ is an abbreviation for $\cos$ plus $i\sin$:

$$
\operatorname{cis}\theta=\cos\theta+i\sin\theta
$$

In Python: `cmath.polar(z)` returns $(r, \theta)$ and `cmath.rect(r, theta)` converts back.

![Figure 1: Rectangular and polar representation of a complex number $a + bi = re^{i\theta}$.](04 - Numbers_images/img-1.jpeg)

## 5. Basic operations

For two numbers $a$ and $b$ their sum is written $a + b$ and their difference is $a - b$.

Multiplication is expressed in several different ways:

| Context | Notation | Example |
| --- | --- | --- |
| Two letters | Juxtaposition | $ab$, $3x$ |
| Two specific numbers | Centered dot or cross | $5 \cdot 7$, $8 \times 11$ |
| Programming | Asterisk | `3 * 5` |

Division is expressed as $a \div b$, $a / b$, or $\frac{a}{b}$. One should choose a notation that maximizes readability.

Exponentiation is expressed using superscripts: $a^b$. In programming, a caret `^` or double asterisks `**` are used (Python uses `**`; note that `^` in Python is bitwise XOR, not exponentiation).

### Floor division and modular arithmetic

Two operations that matter enormously in discrete math and computer science:

**Floor division.** $\lfloor a / b \rfloor$ gives the largest integer $\leq a/b$. In Python: `a // b`.

**Modular arithmetic.** $a \bmod n$ gives the remainder when $a$ is divided by $n$. In Python: `a % n`. The notation $a \equiv b \pmod{n}$ means $n$ divides $a - b$ (i.e., $a$ and $b$ have the same remainder mod $n$).

| Math | Python | Example |
| --- | --- | --- |
| $\lfloor 7/2 \rfloor$ | `7 // 2` | $3$ |
| $\lceil 7/2 \rceil$ | `math.ceil(7/2)` | $4$ |
| $17 \bmod 5$ | `17 % 5` | $2$ |
| $a \equiv b \pmod{n}$ | `a % n == b % n` | $17 \equiv 2 \pmod{5}$ |

See the discussion of $\sum$ and $\prod$ notation on page 8.

## 6. Other number systems

There are other number systems used by mathematicians that are useful in engineering and science applications. We list here some of the more common ones.

### Modular integers

For an integer $n \geq 2$, we write $\mathbb{Z}_n$ to stand for the set $\{0,1,\ldots,n-1\}$ with operations mod $n$. The notations $\mathbb{Z}/n\mathbb{Z}$ and $\mathbb{Z}/(n)$ are also used.

This is the clock arithmetic you already know: hours are $\mathbb{Z}_{12}$ (or $\mathbb{Z}_{24}$), and Python's `%` operator is how you compute in it.

### Finite fields

A finite field$^2$ with $n$ elements may be written either $\mathrm{GF}(n)$ or $\mathbb{F}_n$. The size of a finite field must be a power of a prime, so the notation typically appears as $\mathrm{GF}(p^a)$ or $\mathbb{F}_{p^a}$.

Finite fields are central to cryptography and error-correcting codes. AES operates over $\mathrm{GF}(2^8)$; Reed-Solomon codes use larger fields.

### Gaussian integers

The Gaussian integers are numbers of the form $a + bi$ where $a$ and $b$ are integers. The set of Gaussian integers is denoted $\mathbb{Z}[i]$.

### Quaternions

Hamilton's quaternions are numbers of the form $a + bi + cj + dk$ where $a, b, c, d \in \mathbb{R}$ and $i, j, k$ have the following properties:

$$
i^2 = j^2 = k^2 = -1
$$

$$
ij = k, \quad jk = i, \quad ki = j
$$

$$
ji = -k, \quad kj = -i, \quad ik = -j
$$

The set of all quaternions is denoted $\mathbb{H}$ (for Hamilton). Note that multiplication in $\mathbb{H}$ is not commutative: $ij = k$ but $ji = -k$.

Quaternions are used in 3D graphics and robotics for representing rotations — they avoid gimbal lock and interpolate more smoothly than Euler angles.

### Extensions

The notation $\mathbb{Z}[i]$ for Gaussian integers means: take the integers $\mathbb{Z}$ together with $i$ and build all possible numbers using addition, subtraction, and multiplication.

This generalizes to any ring and any auxiliary element $\alpha$. The notation $R[\alpha]$ denotes the set of all objects formed by repeatedly using $+$, $-$, $\times$ with elements of $R$ and $\alpha$. For example, $\mathbb{Z}[\sqrt{-2}]$.

For a field $F$, the notation $F(\alpha)$ is the extension created by including $\alpha$ with all four basic operations. Thus $\mathbb{Q}(\pi)$ includes numbers such as $\frac{2 + 5\pi}{1/2 - \pi^2}$.

## 7. To infinity and beyond

It is often useful to append the concept of infinity to the real or complex number systems.

In the realm of real numbers, $\overline{\mathbb{R}}$ denotes the set of extended real numbers which includes the additional values $+\infty$ and $-\infty$.

For complex numbers, $\hat{\mathbb{C}}$ (or $\overline{\mathbb{C}}$) denotes the extended complex numbers (also called the Riemann sphere) which includes the single additional value $\infty$. This system is sometimes expressed simply as $\mathbb{C} \cup \{\infty\}$.

An exotic extension of the real numbers is ${}^*\mathbb{R}$, the nonstandard reals which includes infinitesimals and hyperintegers.

### Transfinite cardinals

As discussed on page 7, given a set $A$, the notation $|A|$ gives the cardinality (size) of the set $A$. This is an integer for finite sets. There is, however, special notation for infinite sets.

The symbol $\aleph_{0}$ denotes the cardinality of the integers: $\aleph_{0}=|\mathbb{Z}|$. It is the smallest transfinite cardinal number. The symbol $\aleph$ is the Hebrew letter aleph and the notation $\aleph_{0}$ is usually spoken "aleph null" or "aleph naught." Sets with cardinality $\aleph_{0}$ are called *countable*.

The cardinality of the real numbers, $|\mathbb{R}|$, is denoted $\mathfrak{c}$. The quantity $\mathfrak{c}$ is also called the *cardinality of the continuum*. Cantor proved $\mathfrak{c} > \aleph_0$ — there are "more" reals than integers, even though both are infinite.

Python has `float('inf')` and `float('-inf')` for the extended reals, and `math.inf` as a named constant. NumPy adds `np.inf`. These follow IEEE 754 rules: `inf + 1 == inf`, `inf - inf` is `nan`.

## 8. Number notation in SymPy

SymPy knows all the standard number sets and can do exact arithmetic with intervals, floor/ceiling, modular arithmetic, and the famous constants. This demo shows the notation-to-code mapping:

```python
<!-- include: code/mathematical-notation/04 - Numbers/02_python.py -->
```
