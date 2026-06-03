<!-- page 1 -->

Chapter 3 Logic

### 1. Boolean operations and proof symbols

The mathematical words and, or, not, implies, and so on are often abbreviated with special symbols.

- And. $p\land q$ is the customary notation for the sentence “$p$ and $q$.” Sometimes an ampersand & is used.
- Or. $p\lor q$ is the customary notation for the sentence “$p$ or $q$.” Sometimes a vertical stroke | is used.
- Not. The sentence “not $p$” is denoted $\sim p$ or $\neg p$.

Note that many math relation symbols may be “slashed” to mean that the relation does not hold. For example $\neq$ (not equal), $\notin$ (not an element of), $\not\subseteq$ (not a subset of), and so on.
- Exclusive or. $p\not\supseteq q$ means “$p$ or $q$, but not ($p$ and $q$).” Sometimes a circled plus sign $\oplus$ is used. The word xor is often used as an abbreviation for exclusive or and sometimes is used as a notation for this operation: $p$ xor $q$.
- Nand. $p\not\supset q$ means $\neg(p\lor q)$. The term nand is a contraction of not and.
- Implies. The notation $a\Rightarrow b$ means “If $a$ then $b$” or “$a$ implies $b$.”
- Implied by. The notation $a\Leftarrow b$ means “$a$ is implied by $b$” or “If $b$ then $a$.”
- If and only if. The notation $a\iff b$ means “$a$ if and only if $b$.” In other words “If $a$ then $b$” and “If $b$ then $a$” are both true statements. The words if and only if are often abbreviated iff.
- Therefore. A small triangle of three dots $\therefore$ is an abbreviation for the word therefore.
- Because. An inverted triangle of three dots $\because$ is an abbreviation for the word because.
- Contradiction. The notation $\Rightarrow\Leftarrow$ indicates a contradiction has been reached in a proof. It is an abbreviation for: “We have reached a contradiction. Therefore the supposition is false.”
- End of proof. A square $\sqsupset$ (or a filled square $\blacksquare$) is often used to show the end of a mathematical proof. The letters QED are also used; they

---

<!-- page 2 -->

§3.2 • Quantifiers

stand for *Quod Erat Demonstrandum* [thus it has been demonstrated]. In class, I use this symbol: $\odot$.

## 2. Quantifiers

The mathematical symbols $\forall$ and $\exists$ are abbreviations that loosely translate to *always* and *sometimes*.

The symbol $\forall$ is called the *universal quantifier* and means *for all*. For example,

$\forall x\in\mathbb{R},\ x^{2}\geq 0.$

This translates to: Every real number $x$ has the property that $x^{2}$ is nonnegative. Or, more colloquially, the square of a real number must be zero or larger.

The symbol $\exists$ is called the *existential quantifier* and means *there exists*. For example,

$\exists x\in\mathbb{R},\ x^{2}=2.$

This sentence asserts that there is a real number whose square equals $2$. (And, of course, $\sqrt{2}$ is such a number.)

To make this notation a bit more pronounceable, some people insert the words “such that” (typically abbreviated s.t. or notated $\ni$) into quantifier notation:

$\exists x\in\mathbb{R}\ \text{s.t.}\ x^{2}=2$

reads “there is a real number $x$ such that $x^{2}=2$.”

When an $\exists$ is followed by an exclamation point it means there is a *unique* object that satisfies the property. For example, $\exists!x\in\mathbb{R},\ x^{2}=0$. This means there is a real number whose square is zero, and there is only one such number.

Quantifiers may be combined to form more complex statements. For example, the property that addition is commutative can be written like this:

$\forall x\in\mathbb{R},\ \forall y\in\mathbb{R},\ x+y=y+x.$

However, when quantifiers alternate the meaning becomes more difficult to parse. For example,

$\forall x\in\mathbb{R},\exists y\in\mathbb{R},\ x+y=0$

asserts that whenever we pick a number $x$, we can find a number $y$ so that $x+y=0$. Of course, we should pick $y=-x$. But

$\exists y\in\mathbb{R},\forall x\in\mathbb{R},\ x+y=0$

makes the false assertion that there’s a “magic” number $y$ with the property that no matter what number $x$ you add to it, the result must be zero.