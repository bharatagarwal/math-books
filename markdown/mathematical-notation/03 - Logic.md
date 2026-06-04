# Logic

George Boole had an audacious idea in 1854: thought itself could be reduced to algebra. His *Laws of Thought* showed that the words "and," "or," "not" obeyed precise algebraic rules, just like addition and multiplication. A century later, Claude Shannon realized that Boole's algebra was exactly what electrical switches computed — and the digital age was born.

If you've written an `if` statement, you've done Boolean algebra. The notation below formalizes what you already know, and extends it with quantifiers ($\forall$, $\exists$) that let you make claims about entire collections at once.

## 1. Boolean operations and proof symbols

The mathematical words *and*, *or*, *not*, *implies*, and so on are abbreviated with special symbols. If you know Python's `and`, `or`, `not`, you already know the semantics — the notation just makes it more compact.

### Connectives

- **And.** $p \land q$ means "$p$ and $q$." True only when both are true. In Python: `p and q`.

- **Or.** $p \lor q$ means "$p$ or $q$." True when at least one is true (inclusive or). In Python: `p or q`.

- **Not.** $\neg p$ (or $\sim p$) means "not $p$." In Python: `not p`.

- **Exclusive or.** $p \oplus q$ means "$p$ or $q$, but not both." In Python: `p ^ q`. This is the XOR you know from bitwise operations.

- **Implies.** $a \Rightarrow b$ means "if $a$ then $b$." The only way this is false is when $a$ is true but $b$ is false. Equivalently, $a \Rightarrow b \;\equiv\; \neg a \lor b$.

  This is the one that trips people up: "false implies anything" is true. A promise you never have to keep isn't a broken promise.

- **If and only if.** $a \iff b$ means "$a$ implies $b$" and "$b$ implies $a$." Often abbreviated *iff*.

- **Implied by.** $a \Leftarrow b$ means "$a$ is implied by $b$" (equivalently, $b \Rightarrow a$).

We can generate the full truth table for implication — the result matches the equivalence $p \Rightarrow q \;\equiv\; \neg p \lor q$:

```python
<!-- include: code/mathematical-notation/03 - Logic/01_python.py -->
```

Note: many math relation symbols can be "slashed" to negate them: $\neq$ (not equal), $\notin$ (not an element of), $\not\subseteq$ (not a subset of), and so on.

### Proof markers

A few symbols appear specifically in the context of writing proofs:

- **Therefore.** $\therefore$ abbreviates the word "therefore."
- **Because.** $\because$ abbreviates the word "because."
- **Contradiction.** $\Rightarrow\!\Leftarrow$ indicates a contradiction has been reached.
- **End of proof.** $\square$ (or $\blacksquare$) marks the end of a proof. The letters QED are also used, from the Latin *Quod Erat Demonstrandum* ("thus it has been demonstrated").

## 2. Quantifiers

The symbols $\forall$ and $\exists$ are the most powerful notation in logic. They let you make claims about every element or some element of a set — the mathematical equivalent of `all()` and `any()` in Python.

### Universal quantifier

The symbol $\forall$ means *for all*:

$$
\forall x \in \mathbb{R},\; x^2 \geq 0
$$

This says: every real number $x$ has the property that $x^2$ is nonnegative.

### Existential quantifier

The symbol $\exists$ means *there exists*:

$$
\exists x \in \mathbb{R},\; x^2 = 2
$$

This asserts that there is a real number whose square equals 2. (And $\sqrt{2}$ is such a number.)

When $\exists$ is followed by an exclamation point, it means *uniquely exists*: $\exists!\, x \in \mathbb{R},\; x^2 = 0$ asserts there is exactly one real number whose square is zero.

### Quantifier order matters

Quantifiers may be combined. When they alternate, the order changes the meaning dramatically:

$$
\forall x \in \mathbb{R},\; \exists y \in \mathbb{R},\; x + y = 0
$$

This is true: for every $x$, we can pick $y = -x$. But swap the quantifiers:

$$
\exists y \in \mathbb{R},\; \forall x \in \mathbb{R},\; x + y = 0
$$

This claims there is a single "magic" number $y$ that, when added to *any* $x$, gives zero. That's false — no such $y$ exists.

The difference is exactly the difference between "every thread has its own lock" ($\forall$ thread $\exists$ lock) and "there is one global lock for all threads" ($\exists$ lock $\forall$ thread). Same words, very different architecture.

### Quantifiers in Z3

Z3 can verify or refute quantified claims directly. We can ask: "Is there a counterexample to $\forall x,\; x^2 \geq 0$?" If Z3 says `unsat`, no counterexample exists and the universal claim holds. We can also verify the existential claim, and confirm the false "magic $y$" claim fails:

```python
<!-- include: code/mathematical-notation/03 - Logic/02_python.py -->
```

The key technique: to check $\forall x,\; P(x)$, ask Z3 to find an $x$ where $\neg P(x)$. If it can't (`unsat`), the universal holds. This is proof by contradiction — automated.
