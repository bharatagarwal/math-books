# Letters

Before the sixteenth century, mathematics was written in words. To say "the square of the unknown plus three equals twelve," you wrote exactly that — a full sentence. Then François Viète did something radical: he used vowels ($A$, $E$, $I$) for unknowns and consonants ($B$, $G$, $D$) for known quantities. For the first time, an equation could be *seen* rather than merely read. A generation later, Descartes refined the convention — letters from the beginning of the alphabet ($a, b, c$) for known constants, letters from the end ($x, y, z$) for unknowns — and that split has held for four centuries.

This chapter is about the raw material of notation: the letters themselves. Which alphabets, which styles, and which decorations mathematicians reach for, and why.

## The Latin alphabet

In mathematics we use letters to name mathematical objects. These objects are often numbers, but they may also be functions, vectors, matrices, sets, and so forth.

The familiar Latin alphabet is the most used (and for many students, the most comfortable) set of letters, appearing in upper and lower case versions. In most mathematics books, these letters are typeset in an italic font, like this: $x + y - 3$. Notice that the numeral 3 is not set in italics. However, when written by hand, most people do not attempt to distinguish between roman x and italic $x$. Some books use roman letters for well-known mathematical constants such as $\mathrm{e} \approx 2.718$ and $\mathrm{i} = \sqrt{-1}$.

Named functions (such as those from trigonometry) are written as short words: $\cos(x)$, $\log(z+2)$, $\det(A)$. Notice that these are written in roman.

Upper and lower case letters are considered different. Thus $X + x$ is not equivalent to $2x$.

### Type styles

One may also see different type styles applied to letters, such as bold $\mathbf{x}$ and script $\mathcal{X}$. Bold letters are often used to denote vectors. Bold letters can be difficult to draw on the board in class; instead, various accents and decorations can be used. For example, instead of writing $\mathbf{x}$, one may write $\vec{x}$ to denote that $x$ is a vector. A wavy underline also indicates bold: $\underline{x}$. However, writing a plain $x$ to stand for a vector is not unusual.

Another way in which bold letters are written by hand (and also in print) is to double some portion of the shape of the letter. For example, in lieu of **Z**, one writes $\mathbb{Z}$. This style is called *blackboard bold* and is typically reserved for specific sets of numbers such as the real numbers $\mathbb{R}$ or the complex numbers $\mathbb{C}$.

The use of different styles of letters is especially useful to distinguish different sorts of mathematical objects. For example, in linear algebra it is helpful to use italic lower case letters to denote numbers (scalars), bold lower case letters to denote vectors, and upper case letters to denote matrices:

| Object | Convention | Example |
| --- | --- | --- |
| Scalar (number) | italic lower | $a$, $x$, $\lambda$ |
| Vector | bold lower | $\mathbf{v}$, $\mathbf{x}$ |
| Matrix | upper | $A$, $M$ |
| Set | upper (blackboard bold for standard sets) | $S$, $\mathbb{R}$, $\mathbb{Z}$ |
| Function | lower (roman for named functions) | $f$, $g$, $\sin$, $\det$ |

### Descartes' convention in code

Descartes' split — $a, b, c$ for knowns, $x, y, z$ for unknowns — maps directly to how symbolic math libraries work. In SymPy, you declare unknowns as `Symbol` objects; everything else is a concrete value:

```python
<!-- include: code/mathematical-notation/01 - Letters/01_python.py -->
```

The convention matters: when you read $ax^2 + bx + c = 0$, you immediately know $a$, $b$, $c$ are given and $x$ is what you're solving for. Four hundred years of muscle memory.

## The Greek alphabet

Somehow the 52 upper and lower case Latin letters, in various font styles (italic, bold, script) are just not sufficient, and for this reason letters from other alphabets are brought into service. The most common choice after the Latin alphabet is the Greek alphabet.

Why Greek? Historical accident. Early modern European mathematicians read Euclid and Archimedes in Greek, and the letters felt naturally "mathematical." Euler cemented the convention in the eighteenth century by assigning Greek letters to constants and functions that have kept those names ever since: $\pi$ for the circle ratio, $e$ for the natural base, $\Sigma$ for summation, $\Delta$ for difference.

| Name | Lower | Upper | Common use |
| --- | --- | --- | --- |
| Alpha | $\alpha$ | $A$ | angles, significance level |
| Beta | $\beta$ | $B$ | angles, type II error |
| Gamma | $\gamma$ | $\Gamma$ | Euler–Mascheroni constant, gamma function |
| Delta | $\delta$ | $\Delta$ | small change, difference |
| Epsilon | $\epsilon$ or $\varepsilon$ | $E$ | small positive quantity |
| Zeta | $\zeta$ | $Z$ | Riemann zeta function |
| Eta | $\eta$ | $H$ | learning rate |
| Theta | $\theta$ or $\vartheta$ | $\Theta$ | angles, big-Theta |
| Iota | $\iota$ | $I$ | (rare) |
| Kappa | $\kappa$ | $K$ | curvature |
| Lambda | $\lambda$ | $\Lambda$ | eigenvalues, rate parameter |
| Mu | $\mu$ | $M$ | mean |
| Nu | $\nu$ | $N$ | (rare; looks like $v$) |
| Xi | $\xi$ | $\Xi$ | random variable |
| Omicron | $o$ | $O$ | big-O notation |
| Pi | $\pi$ | $\Pi$ | circle constant, product |
| Rho | $\rho$ | $R$ | correlation, density |
| Sigma | $\sigma$ | $\Sigma$ | std deviation, summation |
| Tau | $\tau$ | $T$ | time constant |
| Upsilon | $\upsilon$ | $\Upsilon$ | (rare) |
| Phi | $\phi$ or $\varphi$ | $\Phi$ | golden ratio, normal CDF |
| Chi | $\chi$ | $X$ | chi-squared test |
| Psi | $\psi$ | $\Psi$ | wave function |
| Omega | $\omega$ | $\Omega$ | angular frequency, sample space |

Some Greek letters look exactly the same as their Latin counterparts (e.g., upper case mu and em) and therefore cannot be used to stand for different things.

Letters from other alphabets (such as German $\mathfrak{G}$ or Hebrew $\aleph$) are used in mathematics, but these are not often seen in science and engineering settings.

SymPy knows all of these — you can work with Greek letters symbolically, and they print as their names:

```python
<!-- include: code/mathematical-notation/01 - Letters/02_python.py -->
```

## Decorations

The repertoire provided by the dozens of letters available from the Latin and Greek alphabets (in their various cases and type styles) is often expanded by various decorations attached to these letters. As we noted earlier, one often places a small arrow above a letter to denote a vector: $\vec{v}$.

### Subscripts and superscripts

The most common decorations attached to letters are subscripts. For example, if one is referring to several points in the plane, it is natural to designate these points by coordinates with numerical subscripts:

$$
(x_{1}, y_{1}),\; (x_{2}, y_{2}),\; \ldots,\; (x_{9}, y_{9})
$$

This is the mathematical version of array indexing. Where a programmer writes `x[1]`, a mathematician writes $x_1$. The convention is universal: subscripts index into families of related objects.

Superscripts are usually reserved for exponentiation; that is, $x^{2}$ means $x$-squared. But sometimes superscripts are also used to denote members of a series; see, for example, the discussion of tensors in the Linear Algebra chapter.

### Primes and other marks

The prime mark ($\prime$) attached to letters can be used to denote a different object. For example, $x$ and $x'$ might be two different numbers. One may place multiple prime marks on a letter to create several different names: $a$, $a'$, $a''$, $a'''$. This can easily become unreadable after three marks. In that case, some people write small (lower case) roman numerals to show the number of primes: $a^{(\mathrm{iv})}$ in place of $a''''$. In calculus, the prime mark is reserved for differentiation.

Other decorations are attached to letters to create additional names:

| Decoration | Notation | Common meaning |
| --- | --- | --- |
| Hat | $\hat{x}$ | estimator, unit vector |
| Bar | $\bar{x}$ | mean, conjugate |
| Dot | $\dot{x}$ | time derivative |
| Double dot | $\ddot{x}$ | second time derivative |
| Tilde | $\tilde{x}$ | approximation, equivalence class |
| Arrow | $\vec{x}$ | vector |

The hat and dot conventions come from physics. Newton wrote $\dot{x}$ for velocity and $\ddot{x}$ for acceleration — his "fluxion" notation — while Leibniz wrote $dx/dt$ and $d^2x/dt^2$. Both notations survive to this day, used in different contexts. The hat $\hat{x}$ comes from statistics, where it denotes an estimator of the true value $x$.

## Traditional uses

In principle, any letter can be used to stand for any mathematical object. However, in certain disciplines there are strong traditions to reserve certain letters for specific purposes. For example, in much of science and engineering the Greek letter $\pi$ stands for the familiar ratio of a circle's circumference to its diameter, approximately 3.14159. However, in other branches of mathematics, the symbol $\pi$ can have other meanings. In general, of course, it is best to use symbols in a discipline's conventional manner.

Here are some of the strongest conventions:

| Letter | Conventional meaning |
| --- | --- |
| $e$ | base of natural logarithms ($\approx 2.718$) |
| $i$, $j$ | $\sqrt{-1}$ (math); loop indices (CS); current (EE uses $j$) |
| $n$, $m$ | integers (especially sizes) |
| $x$, $y$, $z$ | unknowns / coordinates |
| $f$, $g$, $h$ | functions |
| $\epsilon$, $\delta$ | small positive quantities (analysis) |
| $\pi$ | circle constant ($\approx 3.14159$) |
| $\sigma$ | standard deviation |
| $\lambda$ | eigenvalue; rate parameter |

These conventions are not rules — they are expectations. Violating them is legal but confusing, like naming a variable `false` and setting it to `True`.
