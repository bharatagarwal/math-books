# Logic

*Bradfield session 4 · Thursday 25 June · pre-work: MCS chapter 3 ·
problems 3.1, 3.2, 3.5*

Counting asked *how many*; logic asks *what follows from what*. This is the
chapter where mathematics stops being about objects and starts being about
**arguments** — the rules that let you move from premises you accept to
conclusions you must accept. For a programmer it is the most familiar
mathematics in the whole course: a propositional formula *is* a Boolean
expression, a truth table *is* an exhaustive test, "are these two formulas
equivalent?" *is* the refactoring question every compiler optimizer asks, and
"is this formula satisfiable?" *is* the question a SAT solver answers. **MCS ch
3** is our source, and it leans into exactly that framing — Java conditionals,
digital circuits, system specifications, and the SAT problem. We will keep the
programmer's habit from the counting chapter: when in doubt, **build the truth
table and look**, then state the law, then machine-check it.

## Propositions and the connectives

A **proposition** is a statement that is either true or false (MCS 3.1). We
build complex propositions from simple ones with **logical connectives**, and
MCS pins each one down not with English but with a **truth table** — the
exhaustive listing of the output for every combination of input truth values.
The propositional variables $P, Q$ range over just $\mathbf{T}$ and $\mathbf{F}$
(Boolean variables, after Boole). The connectives we will use constantly are
$\lnot$ (NOT), $\land$ (AND), $\lor$ (OR), $\oplus$ (XOR), $\rightarrow$
(IMPLIES), and $\leftrightarrow$ (IFF). Defining them in code *is* defining them:
a connective is exactly its truth table.

```python
<!-- include: code/bradfield/04-logic/01_truth_tables.py -->
```

Two subtleties MCS flags right away. OR is **inclusive** — "$P$ OR $Q$" is true
even when *both* hold (if you want "one or the other but not both," that is XOR).
And the truth table is *all there is*: there is no hidden notion of relevance or
causation, only the four rows.

## How many connectives are there? Exactly sixteen

Before memorizing names, it is worth discovering the whole landscape — MCS 3.1
mentions there are **sixteen binary connectives**, and the reason is a tiny
counting argument from the last chapter. A binary connective takes the four
input rows TT, TF, FT, FF and assigns each an output bit. So a connective *is*
its four-bit output column, and there are $2^4 = 16$ possible columns. Rather
than take that on faith, let us enumerate all sixteen and watch the familiar
ones — AND, OR, XOR, IMPLIES, IFF, NAND, NOR, plus the constant TRUE and FALSE —
fall out of the list, leaving seven that are perfectly real but have no everyday
name.

```python
<!-- include: code/bradfield/04-logic/04_count_connectives.py -->
```

The demo confirms $2^4 = 16$ columns and tags the nine that have names. That
$2^4$ is the *generalized product rule* from the counting chapter wearing a logic
costume: four independent binary choices, one per input row.

## The subtlety of IMPLIES

MCS dwells on $P \rightarrow Q$ because its truth table is the one that surprises
people: it is true whenever $P$ is **false**, regardless of $Q$. The book's
slogan is worth memorizing:

> An implication is true exactly when the if-part is false or the then-part is
> true.

That is precisely the claim that $P \rightarrow Q$ is equivalent to $\overline{P}
\lor Q$ — a fact we will lean on when we strip a formula down to AND/OR/NOT. The
classic MCS examples make the convention vivid:

- *"If pigs fly, then you can understand the Chebyshev bound."* **True** — pigs
  don't fly, so we are on a false-hypothesis row and the implication holds no
  matter what the conclusion is.
- *"If Goldbach's Conjecture is true, then $x^2 \geq 0$ for every real $x$."*
  **True** — and we can say so *without knowing whether Goldbach holds*, because
  the conclusion is true, putting us on a true-conclusion row.
- *"If the moon shines white, then the moon is made of white cheddar."*
  **False** — the one falsifying pattern: true hypothesis, false conclusion.

MCS also motivates the false-hypothesis convention with engineering: a system
spec is a conjunction $[C_1 \rightarrow A_1] \land \cdots \land [C_n \rightarrow
A_n]$ of "in condition $i$, take action $i$" rules. When condition $C_i$ doesn't
hold, we still want that rule to count as *satisfied* — which is exactly what
"false hypothesis $\Rightarrow$ true implication" delivers. The first demo's
IMPLIES column already shows the rule mechanically; the duality demo below will
treat $P \rightarrow Q \equiv \overline{P} \lor Q$ as a validity to check.

## Equivalence: simplifying a real conditional

MCS 3.2 grounds equivalence in code refactoring. Consider a C/C++/Java guard:

```
if (x > 0 || (x <= 0 && y > 100))
```

Let $A$ be "$x > 0$" and $B$ be "$y > 100$." Since "$x \leq 0$" is just
$\overline{A}$, the condition is

$$A \lor (\overline{A} \land B).$$

MCS fills in the truth table one sub-column at a time — first $\overline{A}$,
then $\overline{A} \land B$, then the outer OR — and discovers the final column
is **identical** to the column for the much simpler $A \lor B$. Two formulas whose
truth values agree on every row are **equivalent**, so the guard can be replaced
by `if (x > 0 || y > 100)` with no change in behavior. This is not a toy:
simplifying logical expressions makes programs faster to read and run, and in
hardware it means *fewer gates* — smaller, cheaper, lower-power chips (MCS 3.2,
Problems 3.5–3.6). Let us rebuild MCS's column-by-column table and check the two
result columns match in every row.

```python
<!-- include: code/bradfield/04-logic/05_simplify_circuit.py -->
```

The demo reproduces the four rows of MCS's table and asserts the two result
columns are identical — equivalence is exactly "same output bit on every row."

## Implication, contrapositive, converse

MCS 3.3 sorts out three statements that English speakers routinely confuse. With
$P =$ "I am hungry," $Q =$ "I am grumpy":

- $P \rightarrow Q$ — *"If I am hungry, then I am grumpy."*
- **Contrapositive** $\overline{Q} \rightarrow \overline{P}$ — *"If I am not
  grumpy, then I am not hungry."* A truth table shows this is **equivalent** to
  the original; they say the same thing.
- **Converse** $Q \rightarrow P$ — *"If I am grumpy, then I am hungry."* This is
  **not** equivalent (it differs on the rows where exactly one of $P,Q$ holds).

And an implication *together with* its converse is equivalent to the biconditional:
$(P \rightarrow Q) \land (Q \rightarrow P) \equiv (P \leftrightarrow Q)$. These
are exactly the relationships Problem 3.2 drills, and they are checkable as
equivalences — which the next section turns into a single mechanical question.

## Validity and satisfiability — and their duality

Two notions that look alike but are duals of each other (MCS 3.3.2):

- A formula is **valid** if it is true under *every* assignment — a tautology.
  The smallest example is $P \lor \overline{P}$. Validity captures the formulas
  that are *logically forced*, like the transitivity of implication
  $$[(P \rightarrow Q) \land (Q \rightarrow R)] \rightarrow (P \rightarrow R).$$
- A formula is **satisfiable** if it is true under *at least one* assignment.
  Satisfiability is the system-designer's question: does *any* configuration meet
  all the specs at once?

MCS frames two bridges that make these one idea. **Equivalence is a special case
of validity**: $F$ and $G$ are equivalent exactly when $F \leftrightarrow G$ is
valid (so the circuit simplification above is the *validity* of $(A \lor
(\overline{A}\land B)) \leftrightarrow (A \lor B)$). And the central duality:

$$P \text{ is valid} \iff \overline{P} \text{ is unsatisfiable.}$$

This is the most useful fact in the chapter, because it means **one machine** —
something that hunts for a satisfying assignment — answers both questions. Before
calling that machine, let us watch the duality directly over full truth tables:
count how many of the $2^n$ assignments satisfy a formula, and confirm that
"valid" means "all $2^n$," that "$\overline{P}$ unsatisfiable" means the same
thing, and that a contradiction has zero models.

```python
<!-- include: code/bradfield/04-logic/07_validity_duality.py -->
```

The demo tabulates the transitivity chain (8/8 — valid), excluded middle (2/2 —
valid), a contradiction (0/2 — unsatisfiable), and the MCS 3.5 example (3/8 —
satisfiable but *not* valid), asserting `valid(P) == unsat(NOT P)` each time.

Truth tables make all of this concrete, but they don't scale: an $n$-variable
formula has $2^n$ rows, so checking validity by table is hopeless past ~30
variables (MCS 3.4.2 makes this point — a billion rows already). That is what a
SAT/SMT solver is for. **Z3** decides validity through the duality — assert
$\overline{P}$ and check for `unsat` — and decides satisfiability by asserting
$P$ and checking for `sat`. Here it confirms the same results plus De Morgan and
the circuit simplification:

```python
<!-- include: code/bradfield/04-logic/02_z3_validity.py -->
```

## The algebra of propositions and normal forms

MCS 3.4 gives a second route to equivalence that doesn't enumerate rows: an
**algebra** of equivalence axioms — commutativity, associativity, identity, the
distributive laws, double negation, and crucially **De Morgan's laws**
$$\overline{A \land B} \equiv \overline{A} \lor \overline{B}, \qquad
  \overline{A \lor B} \equiv \overline{A} \land \overline{B},$$
which push negations inward. These axioms are *complete*: two formulas are
equivalent iff you can derive one from the other (MCS Theorem 3.4.5). The bridge
between the table view and the algebra view is **normal form**. MCS 3.4 shows
every formula is equivalent to both:

- a **disjunctive normal form (DNF)** — an OR of AND-terms, one AND-term for each
  row where the formula is **true** (each variable plain if it is T in that row,
  negated if F);
- a **conjunctive normal form (CNF)** — an AND of OR-terms, one OR-term for each
  row where the formula is **false**.

You can read both straight off the truth table, mechanically. Take MCS's running
example $A \land (B \lor C)$: it is true on three rows and false on five, so its
DNF has three AND-terms and its CNF has five OR-terms. Let us build them from the
table the way MCS does, then verify each normal form reproduces the original
truth column on all eight rows.

```python
<!-- include: code/bradfield/04-logic/06_normal_forms.py -->
```

The demo prints the DNF $(A\land B\land C)\lor(A\land B\land\overline{C})\lor
(A\land\overline{B}\land C)$ — exactly MCS equation (3.6) — and the five-clause
CNF, then asserts both re-evaluate to the original column everywhere. DNF answers
"*when* is this true" at a glance; CNF is the shape SAT solvers consume, and the
**SAT problem** — is a given CNF satisfiable? — is the one MCS 3.5 hangs the
whole $\mathbf{P}$ vs. $\mathbf{NP}$ question on. The Z3 demo above already solves
the MCS 3.5 CNF instance directly.

## Predicate logic and quantifiers

Propositional logic bottoms out at atomic propositions. **Predicate logic** (MCS
3.6) adds **predicates** — propositions parameterized by a variable, like $P(x) =$
"$x$ is prime" — and **quantifiers** that say how often a predicate holds over a
domain: $\forall x$ ("for all") and $\exists x$ ("there exists"). With these we
can finally state things like Goldbach's Conjecture precisely:
$$\forall n \in \text{Evens}.\ \exists p, q \in \text{Primes}.\ n = p + q.$$

MCS emphasizes two traps. First, **order of quantifiers matters**. $\forall x\,
\exists y.\ P(x,y)$ is genuinely weaker than $\exists y\, \forall x.\ P(x,y)$:
the first lets the witness $y$ depend on $x$, the second demands *one* $y$ that
works for all $x$. MCS's example is *"Every American has a dream"* — does each
person have their own dream ($\forall a\, \exists d$), or is there one shared
dream ($\exists d\, \forall a$)? Swapping Goldbach's quantifiers likewise turns a
famous conjecture into the obviously-false claim that two fixed primes sum to
*every* even number. Second, **negation flips quantifiers** (De Morgan for
quantifiers, MCS 3.6.5):
$$\overline{\forall x.\ P(x)} \equiv \exists x.\ \overline{P(x)}, \qquad
  \overline{\exists x.\ P(x)} \equiv \forall x.\ \overline{P(x)}.$$
"Not everyone likes ice cream" *is* "someone doesn't."

Z3 handles quantifiers directly. We check that $\forall x\,\exists y.\ x < y$ is
valid over the integers while its swap $\exists y\,\forall x.\ x \leq y$ is
unsatisfiable (no greatest integer), confirm the negation-flip equivalence over
an uninterpreted predicate, and then make the order distinction concrete on a
tiny finite domain: a world where every American dreams but no dream is shared
satisfies the $\forall\exists$ reading yet falsifies the $\exists\forall$ one.

```python
<!-- include: code/bradfield/04-logic/03_predicate_logic.py -->
```

The integer cases use the unbounded domain where "greatest integer" is plainly
false; the finite-domain case exhibits an actual model separating the two
quantifier orders — the cleanest possible proof that they are not equivalent.

## Working the problem set (MCS 3.1, 3.2, 3.5)

The post-class problems drill exactly these ideas:

- **3.1** translates English sentences into propositional formulas — the art of
  naming atomic propositions and wiring them with connectives, then checking the
  translation against intended truth values.
- **3.2** is about IMPLIES and its relatives — converse, contrapositive, inverse
  — and which of them are equivalent. The contrapositive section above is the
  core; each claim is an equivalence the Z3 demo's method settles.
- **3.5** connects formulas to **digital circuits** — AND/OR/NOT gates — and asks
  you to simplify, which is the practical payoff of the algebra of propositions:
  fewer connectives means fewer gates. The circuit-simplification and normal-form
  demos are the worked machinery.

The deeper treatment is MCS ch 3 in full — the equivalence axioms, the
completeness theorem, and the SAT / $\mathbf{P}$ vs. $\mathbf{NP}$ discussion. The
next session moves from *static* logic to **proof techniques** that put this
machinery to work: with validity and equivalence defined, we can finally ask
*how* one proves an implication — directly, by contrapositive, or by
contradiction.
