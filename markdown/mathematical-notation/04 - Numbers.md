<!-- page 1 -->

Chapter 4 Numbers

### 4.1 Real numbers

#### Writing numbers.

The set of all real numbers is denoted $\mathbb{R}$. Real numbers are typically written in decimal notation starting with a sign (optional if positive, mandatory if negative), a finite list of digits, a decimal point, and then either finitely many or infinitely many more digits.

An infinite repeating block of decimals is often denoted with an overline:

$45.07123123123123\ldots=45.07\overline{123}$

When a decimal number is between 0 and 1, it is preferable to include a leading zero digit. Thus 0.123 is preferred to .123 as the leading zero alerts the reader to the otherwise easily missed decimal point.

For numbers with more than three digits to the left of the decimal point, commas are used to improve readability: 1,332,443. However, for numbers between 1000 and 9999 the comma is often omitted. In some cases, a small space is used instead of a comma: 1 332 443.

The use of a period as the decimal point is not universal. In many countries a comma is used instead (e.g., $\pi\approx 3$,14159) and the period is used to separate groups of three digits (e.g., 1.332.443).

The per cent symbol means “divided by 100”. The following numbers are exactly the same; they are simply written differently:

$\frac{1}{4}\qquad 0.25\qquad 25\%$

Scientific notation is often used to express real numbers, especially if they are very large or very small. For example:

$1.23\times 10^{7}=12,300,000\quad\text{and}\quad 4.56\times 10^{-4}=0.000456$

The number before the power of 10 is usually at least 1 and less than 10. Computer programs may output numbers in scientific notation with an E (or e) to mark the power of ten, like this:

$1.23\times 10^{7}\quad 1.23E07$
$4.56\times 10^{-4}\quad 4.56E-04$

Engineering notation is a variant form of scientific notation in which the exponent on 10 must be a multiple of three, like this:

---

<!-- page 2 -->

\S 4.1\bullet
Real numbers

Scientific notation:  $6.022 \times 10^{23}$

Engineering notation:  $602.2 \times 10^{21}$

For engineering notation, the factor in front of the multiple of 10 should be at least 1 and less than 1000.

Sometimes it is useful to express numbers in bases other than ten. There are a few ways in which this is indicated:

- The base of the number is written as a word subscript like this:  $14_{\mathrm{FIVE}}$  or  $0.202020_{\mathrm{THREE}}$ .
- The base of the number is written as a numerical subscript, like this:  $1011_{2}$ .
- In computer science, base-16 (hexadecimal) integers are written with a  $\mathbf{0X}$  or  $\mathbf{0x}$  prefix. For example:  $\mathbf{0X1A2B93}$  or  $\mathbf{0x1a2b93}$ . In this notation, the letters A through F stand for digits whose values are 10 through 15, respectively.
- In computer science, base-8 (octal) integers are written by simply beginning the number with a zero. For example 0177.

Some real numbers are expressed using continued fractions. For example:

![img-0.jpeg](04 - Numbers_images/img-0.jpeg)

This may be written compactly like this:

$$
1 + \frac {1}{2 +} \frac {1}{3 +} \frac {1}{4 +} \dots .
$$

In these examples, the numerators are all 1s, but this is not necessary. However, in that case, continued fractions may also be expressed this way: [1; 2, 3, 4, ...].

Further number notation. The absolute value of a real number  $x$  is denoted  $|x|$ .

The plus-minus notation  $\pm$  is used to indicate two different values. Thus,  $\pm 2$  stands for 2 and  $-2$ . It is a useful shorthand to encapsulate two different values in a single expression. For example, the solutions to the equation  $x^{2} - 2x - 2 = 0$  are  $1 \pm \sqrt{3}$ ; this means that both  $1 + \sqrt{3}$  and  $1 - \sqrt{3}$  are solutions.

Using the symbol  $\pm$  twice in a single expression can be ambiguous. Consider  $\pm 1 \pm \sqrt{5}$ . This might either mean the two values  $1 + \sqrt{5}$  and  $-1 - \sqrt{5}$ , or it might also include the additional values  $1 - \sqrt{5}$  and  $-1 + \sqrt{5}$ . The meaning needs to be derived from context.

---

<!-- page 3 -->

Numbers

The minus-plus symbol $\mp$ means the same thing as $\pm$. It is typically used in conjunction with $\pm$ and has the opposite sign. Thus $\pm 3 \mp \sqrt{7}$ means the two values $3 - \sqrt{7}$ and $-3 + \sqrt{7}$.

The equal sign = has two meanings. One asserts that two values are equal as in $3 + 4 = 7$. The other meaning occurs when defining values as in "Let $x = 1 + \sqrt{5}$." Some people use the notation := when defining a value. The symbols $\triangleq$ and $\triangleq$ are also used as defining equal signs.

A triple line equal sign $\equiv$ is used to mean identically equal to. For example, an equation may be written as $x^{2} - 2 = 0$ which is true for some values of $x$. However, when we write $\sin^2 x + \cos^2 x \equiv 1$, we assert the equation is true for all values of $x$.

## 2. Subsets of the reals

The integers are the real numbers that can be expressed without any digits after the decimal point (in which case writing the decimal point is optional). The set of integers is denoted $\mathbb{Z}$:

$$
\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}
$$

There is no standard definition for the term natural number. We prefer the definition that a natural number is a nonnegative integer. Thus $\mathbb{N} = \{0,1,2,3,\ldots\}$. However, some mathematicians prefer not to include 0 in this set.$^1$

The rational numbers are those real numbers that can be expressed as the ratio of integers $a / b$ where $b$ is nonzero. The set of rational numbers is denoted $\mathbb{Q}$. This may be written

$$
\mathbb{Q} = \{x \in \mathbb{R} : x = a / b \text{ where } a, b \in \mathbb{Z} \text{ and } b \neq 0\}.
$$

These sets of numbers are nested as follows:

$$
\mathbb{R} \supset \mathbb{Q} \supset \mathbb{Z} \supset \mathbb{N}.
$$

Appending a star superscript to these may have various meanings:

- $\mathbb{R}^*$, $\mathbb{C}^*$, and so on denote the nonzero elements of the set. [Note: $\mathbb{C}$ stands for the set of complex numbers; see §4.4.]
- $\mathbb{R}^*$, $\mathbb{C}^*$, and so on denote the invertible elements of the set. In the case of the fields, $\mathbb{R}$, $\mathbb{C}$, $\mathbb{Q}$, this is the same as the nonzero elements. In the case of the integers, $\mathbb{Z}^*$ would mean $\{-1, 1\}$. For this meaning, we prefer a $\times$ superscript: $\mathbb{Z}^\times$.
- $\mathbb{C}^*$ is sometimes used to denote $\mathbb{C} \cup \{\infty\}$ (though we recommend $\hat{\mathbb{C}}$ or $\overline{\mathbb{C}}$ for this). Similarly, $\mathbb{R}^*$ is sometimes used to denote $\mathbb{R} \cup \{-\infty, +\infty\}$ (but we prefer $\overline{\mathbb{R}}$).

$^1$The 1993 ANSI/IEEE standard [8] excludes 0 from $\mathbb{N}$ whereas the ISO standard [9] includes 0. The ISO recommends $\mathbb{N}^*$ for the set of positive integers.

---

<!-- page 4 -->

\S 4.3
\bullet
"Famous" real numbers

- $\mathbb{Z}^*$ is used by [13] to denote the nonnegative integers, $\{0, 1, 2, \ldots\}$ (but we prefer $\mathbb{N}$).
- Finally, ${}^{*}\mathbb{R}$ denotes the nonstandard reals (see page 19).

Appending a + superscript or subscript to $\mathbb{R}$ generally denotes the positive reals: $\mathbb{R}^+$ or $\mathbb{R}_+$. However, it is sometimes convenient to include 0; in that way, $\mathbb{R}_+^n$ would denote the nonnegative orthant. Whether or not to include 0 in this set is a matter of convenience to the matter being discussed. If in doubt, ask. Likewise $\mathbb{Q}^+$ and $\mathbb{Z}^+$ denote the positive rationals and integers respectively.

Intervals of real numbers are denoted with open/close parentheses and brackets. A parenthesis indicates that the endpoint is not included whereas a bracket indicates that the endpoint is included. Some examples:

$$
[1, 2] = \{x \in \mathbb{R} : 1 \leq x \leq 2\}
$$

$$
[1, 2) = \{x \in \mathbb{R} : 1 \leq x &lt; 2\}
$$

$$
(1, 2] = \{x \in \mathbb{R} : 1 &lt; x \leq 2\}
$$

$$
(1, 2) = \{x \in \mathbb{R} : 1 &lt; x &lt; 2\}.
$$

Some people use brackets facing the wrong direction to indicate the non-inclusion of an interval's endpoint. For example $[a, b[$ means the same thing as $[a, b)$, namely the set $\{x : a \leq x &lt; b\}$. Likewise, $]a, b]$ is the interval $(a, b]$ and $]a, b[$ is the open interval $(a, b)$.

The symbols $-\infty$ and $\infty$ may be used for the left and right ends of an interval:

$$
[1, \infty) = \{x \in \mathbb{R} : x \geq 1\} \quad \text{and} \quad (-\infty, 2) = \{x \in \mathbb{R} : x &lt; 2\}.
$$

Although one could write $(-\infty, \infty)$, this would indicate all real numbers and it's clearer simply to write $\mathbb{R}$.

# 3. "Famous" real numbers

Some real numbers have their own special notation. Here are a few that you may encounter.

- $e$, the base of the natural logarithms. Its approximate value is 2.71828.
- $\pi$, the ratio of a circle's circumference to its diameter. Its approximate value is 3.14159.
- $\gamma$, the Euler-Mascheroni constant:

$$
\gamma = \lim_{n \to \infty} \left[ \sum_{k=1}^{n} \frac{1}{k} - \ln n \right].
$$

Its approximate value is 0.5772.

- $\phi$, the golden ratio: $\phi = (1 + \sqrt{5})/2$. Its approximate value is 1.618.

Note that various scientific disciplines reserve certain letters for physical constants (such as $c$ for the speed of light).

---

<!-- page 5 -->

4 Complex numbers

The complex numbers are created by appending a new object, $i$, to the real numbers and following the natural consequence of algebraic steps. Here, $i$ stands for a number with the property $i^{2}=-1$. The result is a collection of numbers of the form $a+bi$ where $a,b\in\mathbb{R}$. The set of complex numbers is denoted $\mathbb{C}$. Some people prefer to write the imaginary unit before its coefficient, like this: $a+ib$.

[Special note: Electrical engineers use $i$ to represent current, and so they use the letter $j$ to represent $\sqrt{-1}$. For them, complex numbers are written as $a+bj$.]

Just as real numbers are visualized as a (number) line, the complex numbers are visualized as a (complex) plane in which the number $a+bi$ corresponds to the point with coordinates $(a,b)$.

The *absolute value* of $z=a+bi$ is denoted $|z|=|a+bi|$ and equals $\sqrt{a^{2}+b^{2}}$. It is the distance from the point $(a,b)$ to the origin. This is also called the complex number’s *magnitude*.

The *(complex) conjugate* of the complex number $z=a+bi$ is denoted with an overline: $\overline{z}=\overline{a+bi}=a-bi$. The conjugate of $z$ is also denoted $z^{*}$.

A fancy R and a fancy I are used to denote the real and imaginary parts of a complex number. If $z=a+bi$, then

$\Re z=a\qquad\text{and}\qquad\Im z=b.$

The abbreviations Re and Im are also used:

$\text{Re}\,z=a\qquad\text{and}\qquad\text{Im}\,z=b.$

Points in the plane may also be expressed in polar coordinates $(r,\theta)$ where $r$ is the radius/distance of the point from the origin and $\theta$ is the counterclockwise angle of the point from positive $x$-axis. If a point has rectangular coordinates $(a,b)$ and polar coordinates $(r,\theta)$, then these quantities are related by the equations

$a=r\cos\theta\qquad\text{and}\qquad b=r\sin\theta.$

This idea extends to complex numbers in that every complex number may be expressed as $re^{i\theta}$ where $r,\theta\in\mathbb{R}$ because

$re^{i\theta}=r\,[\cos\theta+i\sin\theta]=(r\cos\theta)+(r\sin\theta)i=a+bi.$

Thus $r=|a+bi|$. The angle $\theta$ is called the *argument* or the *phase angle* of $a+bi$; this is denoted $\arg(a+bi)$. Typically one defines $\arg z$ to lie in the interval $[0,2\pi)$ or in the interval $(-\pi,\pi]$. See Figure 1 on the following page.

The value $e^{i\theta}$ is sometimes written $\cos\theta$. The notation $\cos$ is an abbreviation for $\cos$ plus $i\sin$:

$\cos\theta=\cos\theta+i\sin\theta.$

---

<!-- page 6 -->

\S 4.6
• Other number systems

![img-1.jpeg](04 - Numbers_images/img-1.jpeg)
FIGURE 4.1. Rectangular and polar representation of a complex number  $a + bi = re^{i\theta}$ .

# 5. Basic operations

For two numbers  $a$  and  $b$  their sum is written  $a + b$  and their difference is  $a - b$ .

Multiplication is expressed in several different ways. If the numbers are expressed as letters, then  $ab$  is the most commonly used notation. For the product of a specific number and a letter, the number is usually written first, e.g.,  $3x$ . The product of two specific numbers is written with either  $\cdot$  or  $\times$  to show the operation:  $5 \cdot 7$  or  $8 \times 11$ . Because the  $\cdot$  and  $\times$  symbols are not standard keyboard characters, some people (and most computer languages) use an asterisk to stand for multiplication:  $3 * 5$ .

Division is expressed in one of the following ways:  $a \div b$ ,  $a / b$ , or  $\frac{a}{b}$ . One should choose a notation that maximizes readability.

Exponentiation is expressed using superscripts:  $a^b$ . However, a wedge  $\wedge$  or double asterisks  $**$  are sometimes used.

See the discussion of  $\sum$  and  $\prod$  notation on page 8.

# 6. Other number systems

There are other number systems used by mathematicians that are useful in engineering and science applications. We list here some of the more common ones.

- Modular numbers. For an integer  $n \geq 2$ , we write  $\mathbb{Z}_n$  to stand for the set  $\{0,1,\ldots,n-1\}$  with operations mod  $n$ . The notations  $\mathbb{Z}/n\mathbb{Z}$  and  $\mathbb{Z}/(n)$  are also used.
- Finite fields. A finite field $^2$  with  $n$  elements may be written either  $\mathrm{GF}(n)$  or  $\mathbb{F}_n$ . It is known that the size of a finite field must be a power of a prime, so it is likely that this notation will be seen like this:  $\mathrm{GF}(p^a)$  or  $\mathbb{F}_{p^a}$ .

---

<!-- page 7 -->

Numbers

- Gaussian integers. The Gaussian integers are numbers of the form  $a + bi$  where  $a$  and  $b$  are integers. The set of Gaussian integers is denoted  $\mathbb{Z}[i]$ .
- Quaternions. Hamilton's quaternions are numbers of the form  $a + bi + cj + dk$  where  $a, b, c, d \in \mathbb{R}$  and  $i, j, k$  have the following properties:

$i^2 = -1$ $ij = k$ $ik = -j$

$j^2 = -1$ $ji = -k$ $jk = i$

$k^2 = -1$ $ki = j$ $kj = -i.$

The set of all quaternions is denoted  $\mathbb{H}$ . Note that multiplication in  $\mathbb{H}$  is not commutative.

- Extensions. Above we presented the notation  $\mathbb{Z}[i]$  for the Gaussian integers. This notation means we take the integers  $\mathbb{Z}$  together with the imaginary number  $i$  and build all possible numbers using the operations addition, subtraction, and multiplication.

This notation generalizes to any ring $^3$  and any auxiliary element  $\alpha$  we wish to append to the ring. The notation  $R[\alpha]$  denotes the set of all objects we can form by repeatedly using addition, subtraction, and multiplication with the elements of  $R$  and  $\alpha$ . For example,  $\mathbb{Z}[\sqrt{-2}]$ . See also the notation  $R[x]$  in §6.4 on polynomials.

For a field  $F$ , the notation  $F(\alpha)$  is the extension of  $F$  created by including the element  $\alpha$  with repeated use of all four basic operations. Thus  $\mathbb{Q}(\pi)$  includes numbers such as  $\frac{2 + 5\pi}{1/2 - \pi^2}$ .

See page 35 for the notation  $R[[x]]$ , the set of formal power series with coefficients from  $R$  in the variable  $x$ .

# 7. To infinity and beyond

It is often useful to append the concept of infinity to the real or complex number systems.

In the realm of real numbers,  $\overline{\mathbb{R}}$  denotes the set of extended real numbers which includes the additional values  $+\infty$  and  $-\infty$ .

For complex numbers,  $\hat{\mathbb{C}}$  [or  $\overline{\mathbb{C}}$ ] denotes the extended complex numbers (also called the Riemann sphere) which includes the single additional value  $\infty$ . This system is sometimes expressed simply as  $\mathbb{C} \cup \{\infty\}$ . Some authors write  $\mathbb{C}^*$ , but this is also (and preferably) used to denote the set  $\mathbb{C} - \{0\}$ .

An exotic extensions of the real numbers is  ${}^*\mathbb{R}$ , the nonstandard reals which includes infinitesimals and hyperintegers.

---

<!-- page 8 -->

\S 4.7
\bullet
To infinity and beyond

As discussed on page 7, given a set $A$, the notation $|A|$ gives the cardinality (size) of the set $A$. This is an integer for finite sets. There is, however, special notation for infinite sets.

The symbol $\aleph_{0}$ denotes the cardinality of the integers: $\aleph_{0}=|\mathbb{Z}|$. It is the smallest transfinite cardinal number. The symbol $\aleph$ is the Hebrew letter aleph and the notation $\aleph_{0}$ is usually spoken “aleph null” or “aleph naught”. Sets with cardinality $\aleph_{0}$ are called countable.

The cardinality of the real numbers, $|\mathbb{R}|$, is denoted $c$. The quantity $c$ is also called the cardinality of the continuum.