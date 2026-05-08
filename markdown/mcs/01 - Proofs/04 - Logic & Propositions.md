## 3.1 Propositions from Propositions

In English, we can modify, combine, and relate propositions with words such as "not," "and," "or," "implies," and "if-then." For example, we can combine three propositions into one like this:

If all humans are mortal and all Greeks are human, then all Greeks are mortal.

For the next while, we won't be much concerned with the internals of propositions—whether they involve mathematics or Greek mortality—but rather with how propositions are combined and related. So, we'll frequently use variables such as  $P$  and  $Q$  in place of specific propositions such as "All humans are mortal" and  $2 + 3 = 5$ . The understanding is that these propositional variables, like propositions, can take on only the values  $\mathbf{T}$  (true) and  $\mathbf{F}$  (false). Propositional variables are also called Boolean variables after their inventor, the nineteenth century mathematician George—you guessed it—Boole.

### 3.1.1 NOT, AND, and OR

Mathematicians use the words NOT, AND, and OR for operations that change or combine propositions. The precise mathematical meaning of these special words can be specified by truth tables. For example, if  $P$  is a proposition, then so is "NOT(P)," and the truth value of the proposition "NOT(P)" is determined by the truth value of  $P$  according to the following truth table:

|  P | NOT(P)  |
| --- | --- |
|  T | F  |
|  F | T  |

The first row of the table indicates that when proposition  $P$  is true, the proposition "NOT(P)" is false. The second line indicates that when  $P$  is false, "NOT(P)" is true. This is probably what you would expect.

In general, a truth table indicates the true/false value of a proposition for each possible set of truth values for the variables. For example, the truth table for the proposition “ $P$  AND  $Q$ ” has four lines, since there are four settings of truth values for the two variables:

|  P | Q | P AND Q  |
| --- | --- | --- |
|  T | T | T  |
|  T | F | F  |
|  F | T | F  |
|  F | F | F  |


According to this table, the proposition “ $P$  AND  $Q$ ” is true only when  $P$  and  $Q$  are both true. This is probably the way you ordinarily think about the word “and.”

There is a subtlety in the truth table for “ $P$  OR  $Q$ ”:

|  P | Q | P OR Q  |
| --- | --- | --- |
|  T | T | T  |
|  T | F | T  |
|  F | T | T  |
|  F | F | F  |

The first row of this table says that “ $P$  OR  $Q$ ” is true even if both  $P$  and  $Q$  are true. This isn’t always the intended meaning of “or” in everyday speech, but this is the standard definition in mathematical writing. So if a mathematician says, “You may have cake, or you may have ice cream,” he means that you could have both.

If you want to exclude the possibility of having both cake and ice cream, you should combine them with the exclusive-or operation, XOR:

|  P | Q | P XOR Q  |
| --- | --- | --- |
|  T | T | F  |
|  T | F | T  |
|  F | T | T  |
|  F | F | F  |

### 3.1.2 IMPLIES

The combining operation with the least intuitive technical meaning is "implies." Here is its truth table, with the lines labeled so we can refer to them later.

|  P | Q | P IMPLIES Q  |   |
| --- | --- | --- | --- |
|  T | T | T | (tt)  |
|  T | F | F | (tf)  |
|  F | T | T | (ft)  |
|  F | F | T | (ff)  |

The truth table for implications can be summarized in words as follows:

An implication is true exactly when the if-part is false or the then-part is true.

This sentence is worth remembering; a large fraction of all mathematical statements are of the if-then form!

Let's experiment with this definition. For example, is the following proposition true or false?


> “If Goldbach’s Conjecture is true, then $x^{2}\geq 0$ for every real number $x$.”

Now, we already mentioned that no one knows whether Goldbach’s Conjecture, Proposition 1.1.8, is true or false. But that doesn’t prevent you from answering the question! This proposition has the form $P\ \texttt{implies}\ Q$ where the hypothesis, $P$, is “Goldbach’s Conjecture is true” and the conclusion, $Q$, is “$x^{2}\geq 0$ for every real number $x$.” Since the conclusion is definitely true, we’re on either line (tt) or line (ft) of the truth table. Either way, the proposition as a whole is true!

One of our original examples demonstrates an even stranger side of implications.

> “If pigs fly, then you can understand the Chebyshev bound.”

Don’t take this as an insult; we just need to figure out whether this proposition is true or false. Curiously, the answer has nothing to do with whether or not you can understand the Chebyshev bound. Pigs do not fly, so we’re on either line (ft) or line (ff) of the truth table. In both cases, the proposition is true!

In contrast, here’s an example of a false implication:

> “If the moon shines white, then the moon is made of white cheddar.”

Yes, the moon shines white. But, no, the moon is not made of white cheddar cheese. So we’re on line (tf) of the truth table, and the proposition is false.

##### False Hypotheses

It often bothers people when they first learn that implications which have false hypotheses are considered to be true. But implications with false hypotheses hardly ever come up in ordinary settings, so there’s not much reason to be bothered by whatever truth assignment logicians and mathematicians choose to give them.

There are, of course, good reasons for the mathematical convention that implications are true when their hypotheses are false. An illustrative example is a system specification (see Problem 3.12) which consisted of a series of, say, a dozen rules,

> if $C_{i}$: the system sensors are in condition $i$, then $A_{i}$: the system takes action $i$,

or more concisely,

$C_{i}\ \texttt{implies}\ A_{i}$

for $1\leq i\leq 12$. Then the fact that the system obeys the specification would be expressed by saying that the and

$[C_{1}\ \texttt{implies}\ A_{1}]\ \texttt{and}\ [C_{2}\ \texttt{implies}\ A_{2}]\ \texttt{and}\cdots\ \texttt{and}\ [C_{12}\ \texttt{implies}\ A_{12}]$ (3.1)

of these rules was always true.


# 3.2. Propositional Logic in Computer Programs

For example, suppose only conditions  $C_2$  and  $C_5$  are true, and the system indeed takes the specified actions  $A_2$  and  $A_5$ . This means that in this case the system is behaving according to specification, and accordingly we want the formula (3.1) to come out true. Now the implications  $C_2$  IMPLIES  $A_2$  and  $C_5$  IMPLIES  $A_5$  are both true because both their hypotheses and their conclusions are true. But in order for (3.1) to be true, we need all the other implications with the false hypotheses  $C_i$  for  $i \neq 2, 5$  to be true. This is exactly what the rule for implications with false hypotheses accomplishes.

### 3.1.3 If and Only If

Mathematicians commonly join propositions in one additional way that doesn't arise in ordinary speech. The proposition "  $P$  if and only if  $Q$  " asserts that  $P$  and  $Q$  have the same truth value. Either both are true or both are false.

|  P | Q | P IFF Q  |
| --- | --- | --- |
|  T | T | T  |
|  T | F | F  |
|  F | T | F  |
|  F | F | T  |

For example, the following if-and-only-if statement is true for every real number  $x$ :

$$
x ^ {2} - 4 \geq 0 \text {I F F} | x | \geq 2.
$$

For some values of  $x$ , both inequalities are true. For other values of  $x$ , neither inequality is true. In every case, however, the IFF proposition as a whole is true.


Propositions and logical connectives arise all the time in computer programs. For example, consider the following snippet, which could be either C, C++, or Java:

```txt
if (x > 0 || (x <= 0 && y > 100))
```

(further instructions)

Java uses the symbol  $|\cdot|$  for "OR," and the symbol  $\&\&$  for "AND." The further instructions are carried out only if the proposition following the word if is true. On closer inspection, this big expression is built from two simpler propositions.


Let $A$ be the proposition that $x > 0$, and let $B$ be the proposition that $y > 100$. Then we can rewrite the condition as

$$
A \text{ OR } (\mathrm{NOT}(A) \text{ AND } B). \tag{3.2}
$$

### 3.2.1 Truth Table Calculation

A truth table calculation reveals that the more complicated expression 3.2 always has the same truth value as

$$
A \text{ OR } B. \tag{3.3}
$$

We begin with a table with just the truth values of $A$ and $B$:

|  A | B | A | OR | (NOT(A) | AND | B) | A | OR | B  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  T | T |  |  |  |  |  |  |  |   |
|  T | F |  |  |  |  |  |  |  |   |
|  F | T |  |  |  |  |  |  |  |   |
|  F | F |  |  |  |  |  |  |  |   |

These values are enough to fill in two more columns:

|  A | B | A | OR | (NOT(A) | AND | B) | A | OR | B  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  T | T |  |  | F |  |  |  | T |   |
|  T | F |  |  | F |  |  |  | T |   |
|  F | T |  |  | T |  |  |  | T |   |
|  F | F |  |  | T |  |  |  | F |   |

Now we have the values needed to fill in the AND column:

|  A | B | A | OR | (NOT(A) | AND | B) | A | OR | B  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  T | T |  |  | F | F |  |  | T |   |
|  T | F |  |  | F | F |  |  | T |   |
|  F | T |  |  | T | T |  |  | T |   |
|  F | F |  |  | T | F |  |  | F |   |

and this provides the values needed to fill in the remaining column for the first OR:

|  A | B | A | OR | (NOT(A) | AND | B) | A | OR | B  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  T | T |  | T | F | F |  |  | T |   |
|  T | F |  | T | F | F |  |  | T |   |
|  F | T |  | T | T | T |  |  | T |   |
|  F | F |  | F | T | F |  |  | F |   |

Expressions whose truth values always match are called equivalent. Since the two emphasized columns of truth values of the two expressions are the same, they are


3.2. Propositional Logic in Computer Programs

equivalent. So we can simplify the code snippet without changing the program's behavior by replacing the complicated expression with an equivalent simpler one:

```txt
if (x > 0 || y > 100)
```

(further instructions)

The equivalence of (3.2) and (3.3) can also be confirmed reasoning by cases:

$A$  is  $\mathbf{T}$ . An expression of the form ( $\mathbf{T}$  or anything) is equivalent to  $\mathbf{T}$ . Since  $A$  is  $\mathbf{T}$  both (3.2) and (3.3) in this case are of this form, so they have the same truth value, namely,  $\mathbf{T}$ .

$A$  is  $\mathbf{F}$ . An expression of the form ( $\mathbf{F}$  or anything) will have same truth value as anything. Since  $A$  is  $\mathbf{F}$ , (3.3) has the same truth value as  $B$ .

An expression of the form ( $\mathbf{T}$  and anything) is equivalent to anything, as is any expression of the form  $\mathbf{F}$  or anything. So in this case  $A$  or  $(\mathrm{NOT}(A)$  and  $B)$  is equivalent to  $(\mathrm{NOT}(A)$  and  $B)$ , which in turn is equivalent to  $B$ .

Therefore both (3.2) and (3.3) will have the same truth value in this case, namely, the value of  $B$ .

Simplifying logical expressions has real practical importance in computer science. Expression simplification in programs like the one above can make a program easier to read and understand. Simplified programs may also run faster, since they require fewer operations. In hardware, simplifying expressions can decrease the number of logic gates on a chip because digital circuits can be described by logical formulas (see Problems 3.5 and 3.6). Minimizing the logical formulas corresponds to reducing the number of gates in the circuit. The payoff of gate minimization is potentially enormous: a chip with fewer gates is smaller, consumes less power, has a lower defect rate, and is cheaper to manufacture.

### 3.2.2 Cryptic Notation

Java uses symbols like “&&” and “||” in place of AND and OR. Circuit designers use “-” and “+,” and actually refer to AND as a product and OR as a sum. Mathematicians use still other symbols, given in the table below.


|  English | Symbolic Notation  |
| --- | --- |
|  NOT(P) | ¬P (alternatively, P)  |
|  P AND Q | P ∧ Q  |
|  P OR Q | P ∨ Q  |
|  P IMPLIES Q | P → Q  |
|  if P then Q | P → Q  |
|  P IFF Q | P ←→ Q  |
|  P XOR Q | P ⊕ Q  |

For example, using this notation, "If  $P$  AND  $\mathrm{NOT}(Q)$ , then  $R$ " would be written:

$$
(P \wedge \overline {{Q}}) \longrightarrow R.
$$

The mathematical notation is concise but cryptic. Words such as "AND" and "OR" are easier to remember and won't get confused with operations on numbers. We will often use  $\overline{P}$  as an abbreviation for  $\mathrm{NOT}(P)$ , but aside from that, we mostly stick to the words—except when formulas would otherwise run off the page.

## 3.3 Equivalence and Validity

### 3.3.1 Implications and Contrapositives

Do these two sentences say the same thing?

If I am hungry, then I am grumpy.

If I am not grumpy, then I am not hungry.

We can settle the issue by recasting both sentences in terms of propositional logic. Let  $P$  be the proposition "I am hungry" and  $Q$  be "I am grumpy." The first sentence says "P IMPLIES  $Q$ " and the second says "NOT(Q) IMPLIES NOT(P)." Once more, we can compare these two statements in a truth table:

|  P | Q | (P IMPLIES Q) | (NOT(Q) | IMPLIES | NOT(P))  |
| --- | --- | --- | --- | --- | --- |
|  T | T | T | F | T | F  |
|  T | F | F | T | F | F  |
|  F | T | T | F | T | T  |
|  F | F | T | T | T | T  |

Sure enough, the highlighted columns showing the truth values of these two statements are the same. A statement of the form "NOT(Q) IMPLIES NOT(P)" is called


the contrapositive of the implication “ $P$  IMPLIES  $Q$ ”. The truth table shows that an implication and its contrapositive are equivalent—they are just different ways of saying the same thing.

In contrast, the converse of “ $P$  IMPLIES  $Q$ ” is the statement “ $Q$  IMPLIES  $P$ ”. The converse to our example is:

If I am grumpy, then I am hungry.

This sounds like a rather different contention, and a truth table confirms this suspicion:

|  P | Q | P IMPLIES Q | Q IMPLIES P  |
| --- | --- | --- | --- |
|  T | T | T | T  |
|  T | F | F | T  |
|  F | T | T | F  |
|  F | F | T | T  |

Now the highlighted columns differ in the second and third row, confirming that an implication is generally not equivalent to its converse.

One final relationship: an implication and its converse together are equivalent to an iff statement, specifically, to these two statements together. For example,

If I am grumpy then I am hungry, and if I am hungry then I am grumpy.

are equivalent to the single statement:

I am grumpy iff I am hungry.

Once again, we can verify this with a truth table.

|  P | Q | (P IMPLIES Q) | AND | (Q IMPLIES P) | P IFF Q  |
| --- | --- | --- | --- | --- | --- |
|  T | T | T | T | T | T  |
|  T | F | F | F | T | F  |
|  F | T | T | F | F | F  |
|  F | F | T | T | T | T  |

The fourth column giving the truth values of

$(P \text{ IMPLIES } Q) \text{ AND } (Q \text{ IMPLIES } P)$

is the same as the sixth column giving the truth values of  $P$  IFF  $Q$ , which confirms that the AND of the implications is equivalent to the IFF statement.


### 3.3.2 Validity and Satisfiability

A valid formula is one which is always true, no matter what truth values its variables may have. The simplest example is

$$
P \text{ or } \mathrm{not}(P).
$$

You can think about valid formulas as capturing fundamental logical truths. For example, a property of implication that we take for granted is that if one statement implies a second one, and the second one implies a third, then the first implies the third. The following valid formula confirms the truth of this property of implication.

$$
[(P \text{ implies } Q) \text{ and } (Q \text{ implies } R)] \text{ implies } (P \text{ implies } R).
$$

Equivalence of formulas is really a special case of validity. Namely, statements $F$ and $G$ are equivalent precisely when the statement $(F \text{ iff } G)$ is valid. For example, the equivalence of the expressions (3.3) and (3.2) means that

$$
(A \text{ or } B) \text{ iff } (A \text{ or } (\mathrm{not}(A) \text{ and } B))
$$

is valid. Of course, validity can also be viewed as an aspect of equivalence. Namely, a formula is valid iff it is equivalent to $\mathbf{T}$.

A satisfiable formula is one which can sometimes be true—that is, there is some assignment of truth values to its variables that makes it true. One way satisfiability comes up is when there are a collection of system specifications. The job of the system designer is to come up with a system that follows all the specs. This means that the AND of all the specs must be satisfiable or the designer’s job will be impossible (see Problem 3.12).

There is also a close relationship between validity and satisfiability: a statement $P$ is satisfiable iff its negation $\mathrm{not}(P)$ is not valid.

## 3.4 The Algebra of Propositions

### 3.4.1 Propositions in Normal Form

Every propositional formula is equivalent to a “sum-of-products” or disjunctive form. More precisely, a disjunctive form is simply an OR of AND-terms, where each AND-term is an AND of variables or negations of variables, for example,

$$
(A \text{ and } B) \text{ or } (A \text{ and } C). \tag{3.4}
$$


You can read a disjunctive form for any propositional formula directly from its truth table. For example, the formula

$$
A \text{ AND } (B \text{ OR } C) \tag{3.5}
$$

has truth table:

|  A | B | C | A | AND | (B OR C)  |
| --- | --- | --- | --- | --- | --- |
|  T | T | T |  | T |   |
|  T | T | F |  | T |   |
|  T | F | T |  | T |   |
|  T | F | F |  | F |   |
|  F | T | T |  | F |   |
|  F | T | F |  | F |   |
|  F | F | T |  | F |   |
|  F | F | F |  | F |   |

The formula (3.5) is true in the first row when $A$, $B$, and $C$ are all true, that is, where $A$ AND $B$ AND $C$ is true. It is also true in the second row where $A$ AND $B$ AND $\overline{C}$ is true, and in the third row when $A$ AND $\overline{B}$ AND $C$ is true, and that's all. So (3.5) is true exactly when

$$
(A \text{ AND } B \text{ AND } C) \text{ OR } (A \text{ AND } B \text{ AND } \overline{C}) \text{ OR } (A \text{ AND } \overline{B} \text{ AND } C) \tag{3.6}
$$

is true.

**Theorem 3.4.1. [Distributive Law of AND over OR]**

$A$ AND $(B \text{ OR } C)$ is equivalent to $(A \text{ AND } B) \text{ OR } (A \text{ AND } C)$.

Theorem 3.4.1 is called a distributive law because of its resemblance to the distributivity of products over sums in arithmetic.

Similarly, we have (Problem 3.10):

**Theorem 3.4.2. [Distributive Law of OR over AND]**

$A \text{ OR } (B \text{ AND } C) \text{ is equivalent to } (A \text{ OR } B) \text{ AND } (A \text{ OR } C).$

Note the contrast between Theorem 3.4.2 and arithmetic, where sums do not distribute over products.

The expression (3.6) is a disjunctive form where each AND-term is an AND of every one of the variables or their negations in turn. An expression of this form is called a disjunctive normal form (DNF). A DNF formula can often be simplified into a smaller disjunctive form. For example, the DNF (3.6) further simplifies to the equivalent disjunctive form (3.4) above.


Applying the same reasoning to the $\mathbf{F}$ entries of a truth table yields a conjunctive form for any formula—an AND of OR-terms in which the OR-terms are OR's only of variables or their negations. For example, formula (3.5) is false in the fourth row of its truth table (3.4.1) where $A$ is $\mathbf{T}$, $B$ is $\mathbf{F}$ and $C$ is $\mathbf{F}$. But this is exactly the one row where $(\overline{A} \text{ OR } B \text{ OR } C)$ is $\mathbf{F}$! Likewise, the (3.5) is false in the fifth row which is exactly where $(A \text{ OR } \overline{B} \text{ OR } \overline{C})$ is $\mathbf{F}$. This means that (3.5) will be $\mathbf{F}$ whenever the AND of these two OR-terms is false. Continuing in this way with the OR-terms corresponding to the remaining three rows where (3.5) is false, we get a conjunctive normal form (CNF) that is equivalent to (3.5), namely,

$$
\begin{array}{l}
(\overline{A} \text{ OR } B \text{ OR } C) \text{ AND } (A \text{ OR } \overline{B} \text{ OR } \overline{C}) \text{ AND } (A \text{ OR } \overline{B} \text{ OR } C) \text{ AND} \\
(A \text{ OR } B \text{ OR } \overline{C}) \text{ AND } (A \text{ OR } B \text{ OR } C)
\end{array}
$$

The methods above can be applied to any truth table, which implies

Theorem 3.4.3. Every propositional formula is equivalent to both a disjunctive normal form and a conjunctive normal form.

### 3.4.2 Proving Equivalences

A check of equivalence or validity by truth table runs out of steam pretty quickly: a proposition with $n$ variables has a truth table with $2^n$ lines, so the effort required to check a proposition grows exponentially with the number of variables. For a proposition with just 30 variables, that's already over a billion lines to check!

An alternative approach that sometimes helps is to use algebra to prove equivalence. A lot of different operators may appear in a propositional formula, so a useful first step is to get rid of all but three: AND, OR, and NOT. This is easy because each of the operators is equivalent to a simple formula using only these three. For example, $A$ IMPLIES $B$ is equivalent to NOT($A$) OR $B$. Formulas using only AND, OR, and NOT for the remaining operators are left to Problem 3.13.

We list below a bunch of equivalence axioms with the symbol “ $\longleftrightarrow$ ” between equivalent formulas. These axioms are important because they are all that’s needed to prove every possible equivalence. We’ll start with some equivalences for AND’s that look like the familiar ones for multiplication of numbers:

$$
A \text{ AND } B \longleftrightarrow B \text{ AND } A \quad (\text{commutativity of AND}) \tag{3.7}
$$

$$
(A \text{ AND } B) \text{ AND } C \longleftrightarrow A \text{ AND } (B \text{ AND } C) \quad (\text{associativity of AND}) \tag{3.8}
$$

$$
\mathbf{T} \text{ AND } A \longleftrightarrow A \quad (\text{identity for AND})
$$

$$
\mathbf{F} \text{ AND } A \longleftrightarrow \mathbf{F} \quad (\text{zero for AND})
$$


Three axioms that don't directly correspond to number properties are

$$
A \text{ AND } A \longleftrightarrow A \quad \text{(idempotence for AND)}
$$

$$
A \text{ AND } \overline{A} \longleftrightarrow \mathbf{F} \quad \text{(contradiction for AND)} \tag{3.9}
$$

$$
\operatorname{NOT}(\overline{A}) \longleftrightarrow A \quad \text{(double negation)} \tag{3.10}
$$

It is associativity (3.8) that justifies writing $A$ AND $B$ AND $C$ without specifying whether it is parenthesized as $A$ AND $(B \text{ AND } C)$ or $(A \text{ AND } B) \text{ AND } C$. Both ways of inserting parentheses yield equivalent formulas.

There are a corresponding set of equivalences for OR which we won't bother to list, except for the OR rule corresponding to contradiction for AND (3.9):

$$
A \text{ OR } \overline{A} \longleftrightarrow \mathbf{T} \quad \text{(validity for OR)}
$$

Finally, there are DeMorgan's Laws which explain how to distribute NOT's over AND's and OR's:

$$
\operatorname{NOT}(A \text{ AND } B) \longleftrightarrow \overline{A} \text{ OR } \overline{B} \quad \text{(DeMorgan for AND)} \tag{3.11}
$$

$$
\operatorname{NOT}(A \text{ OR } B) \longleftrightarrow \overline{A} \text{ AND } \overline{B} \quad \text{(DeMorgan for OR)} \tag{3.12}
$$

All of these axioms can be verified easily with truth tables.

These axioms are all that's needed to convert any formula to a disjunctive normal form. We can illustrate how they work by applying them to turn the negation of formula (3.5),

$$
\operatorname{NOT}\left(\left(A \text{ AND } B\right) \text{ OR } \left(A \text{ AND } C\right)\right). \tag{3.13}
$$

into disjunctive normal form.

We start by applying DeMorgan's Law for OR (3.12) to (3.13) in order to move the NOT deeper into the formula. This gives

$$
\operatorname{NOT}(A \text{ AND } B) \text{ AND } \operatorname{NOT}(A \text{ AND } C).
$$

Now applying Demorgan's Law for AND (3.11) to the two innermost AND-terms, gives

$$
(\overline{A} \text{ OR } \overline{B}) \text{ AND } (\overline{A} \text{ OR } \overline{C}). \tag{3.14}
$$

At this point NOT only applies to variables, and we won't need Demorgan's Laws any further.

Now we will repeatedly apply The Distributivity of AND over OR (Theorem 3.4.1) to turn (3.14) into a disjunctive form. To start, we'll distribute $(\overline{A} \text{ OR } \overline{B})$ over AND to get

$$
\left(\left(\overline{A} \text{ OR } \overline{B}\right) \text{ AND } \overline{A}\right) \text{ OR } \left(\left(\overline{A} \text{ OR } \overline{B}\right) \text{ AND } \overline{C}\right).
$$


Using distributivity over both AND's we get

$$
\left(\left(\bar {A} \text{ AND } \bar {A}\right) \text{ OR } \left(\bar {B} \text{ AND } \bar {A}\right)\right) \text{ OR } \left(\left(\bar {A} \text{ AND } \bar {C}\right) \text{ OR } \left(\bar {B} \text{ AND } \bar {C}\right)\right).
$$

By the way, we've implicitly used commutativity (3.7) here to justify distributing over an AND from the right. Now applying idempotence to remove the duplicate occurrence of $\overline{A}$ we get

$$
(\bar {A} \text{ OR } (\bar {B} \text{ AND } \bar {A})) \text{ OR } ((\bar {A} \text{ AND } \bar {C}) \text{ OR } (\bar {B} \text{ AND } \bar {C})).
$$

Associativity now allows dropping the parentheses around the terms being OR'd to yield the following disjunctive form for (3.13):

$$
\bar {A} \text{ OR } (\bar {B} \text{ AND } \bar {A}) \text{ OR } (\bar {A} \text{ AND } \bar {C}) \text{ OR } (\bar {B} \text{ AND } \bar {C}). \tag {3.15}
$$

The last step is to turn each of these AND-terms into a disjunctive normal form with all three variables $A$, $B$, and $C$. We'll illustrate how to do this for the second AND-term $(\overline{B} \text{ AND } \overline{A})$. This term needs to mention $C$ to be in normal form. To introduce $C$, we use validity for OR and identity for AND to conclude that

$$
(\bar {B} \text{ AND } \bar {A}) \longleftrightarrow (\bar {B} \text{ AND } \bar {A}) \text{ AND } (C \text{ OR } \bar {C}).
$$

Now distributing $(\overline{B} \text{ AND } \overline{A})$ over the OR yields the disjunctive normal form

$$
(\bar {B} \text{ AND } \bar {A} \text{ AND } C) \text{ OR } (\bar {B} \text{ AND } \bar {A} \text{ AND } \bar {C}).
$$

Doing the same thing to the other AND-terms in (3.15) finally gives a disjunctive normal form for (3.5):

$$
\begin{array}{l}
(\bar {A} \text{ AND } B \text{ AND } C) \text{ OR } (\bar {A} \text{ AND } B \text{ AND } \bar {C}) \text{ OR} \\
(\bar {A} \text{ AND } \bar {B} \text{ AND } C) \text{ OR } (\bar {A} \text{ AND } \bar {B} \text{ AND } \bar {C}) \text{ OR} \\
(\bar {B} \text{ AND } \bar {A} \text{ AND } C) \text{ OR } (\bar {B} \text{ AND } \bar {A} \text{ AND } \bar {C}) \text{ OR} \\
(\bar {A} \text{ AND } \bar {C} \text{ AND } B) \text{ OR } (\bar {A} \text{ AND } \bar {C} \text{ AND } \bar {B}) \text{ OR} \\
(\bar {B} \text{ AND } \bar {C} \text{ AND } A) \text{ OR } (\bar {B} \text{ AND } \bar {C} \text{ AND } \bar {A}).
\end{array}
$$

Using commutativity to sort the term and OR-idempotence to remove duplicates, finally yields a unique sorted DNF:

$$
\begin{array}{l}
(A \text{ AND } \bar {B} \text{ AND } \bar {C}) \text{ OR} \\
(\bar {A} \text{ AND } B \text{ AND } C) \text{ OR} \\
(\bar {A} \text{ AND } B \text{ AND } \bar {C}) \text{ OR} \\
(\bar {A} \text{ AND } \bar {B} \text{ AND } C) \text{ OR} \\
(\bar {A} \text{ AND } \bar {B} \text{ AND } \bar {C}).
\end{array}
$$

This example illustrates a strategy for applying these equivalences to convert any formula into disjunctive normal form, and conversion to conjunctive normal form works similarly, which explains:


## 3.5 The SAT Problem


**Theorem 3.4.4.** Any propositional formula can be transformed into disjunctive normal form or a conjunctive normal form using the equivalences listed above.

What has this got to do with equivalence? That's easy: to prove that two formulas are equivalent, convert them both to disjunctive normal form over the set of variables that appear in the terms. Then use commutativity to sort the variables and AND-terms so they all appear in some standard order. We claim the formulas are equivalent iff they have the same sorted disjunctive normal form. This is obvious if they do have the same disjunctive normal form. But conversely, the way we read off a disjunctive normal form from a truth table shows that two different sorted DNF's over the same set of variables correspond to different truth tables and hence to inequivalent formulas. This proves

**Theorem 3.4.5 (Completeness of the propositional equivalence axioms).** Two propositional formula are equivalent iff they can be proved equivalent using the equivalence axioms listed above.

The benefit of the axioms is that they leave room for ingeniously applying them to prove equivalences with less effort than the truth table method. Theorem 3.4.5 then adds the reassurance that the axioms are guaranteed to prove every equivalence, which is a great punchline for this section. But we don't want to mislead you: it's important to realize that using the strategy we gave for applying the axioms involves essentially the same effort it would take to construct truth tables, and there is no guarantee that applying the axioms will generally be any easier than using truth tables.


Determining whether or not a more complicated proposition is satisfiable is not so easy. How about this one?

$$
(P \text{ or } Q \text{ or } R) \text{ and } (\overline{P} \text{ or } \overline{Q}) \text{ and } (\overline{P} \text{ or } \overline{R}) \text{ and } (\overline{R} \text{ or } \overline{Q})
$$

The general problem of deciding whether a proposition is satisfiable is called SAT. One approach to SAT is to construct a truth table and check whether or not a T ever appears, but as with testing validity, this approach quickly bogs down for formulas with many variables because truth tables grow exponentially with the number of variables.

Is there a more efficient solution to SAT? In particular, is there some brilliant procedure that determines SAT in a number of steps that grows *polynomially*—like


$n^2$ or $n^{14}$—instead of exponentially—$2^n$—whether any given proposition of size $n$ is satisfiable or not? No one knows. And an awful lot hangs on the answer.

The general definition of an “efficient” procedure is one that runs in polynomial time, that is, that runs in a number of basic steps bounded by a polynomial in $s$, where $s$ is the size of an input. It turns out that an efficient solution to SAT would immediately imply efficient solutions to many other important problems involving scheduling, routing, resource allocation, and circuit verification across multiple disciplines including programming, algebra, finance, and political theory. This would be wonderful, but there would also be worldwide chaos. Decrypting coded messages would also become an easy task, so online financial transactions would be insecure and secret communications could be read by everyone. Why this would happen is explained in Section 8.12.

Of course, the situation is the same for validity checking, since you can check for validity by checking for satisfiability of a negated formula. This also explains why the simplification of formulas mentioned in Section 3.2 would be hard—validity testing is a special case of determining if a formula simplifies to $\mathbf{T}$.

Recently there has been exciting progress on SAT-solvers for practical applications like digital circuit verification. These programs find satisfying assignments with amazing efficiency even for formulas with millions of variables. Unfortunately, it’s hard to predict which kind of formulas are amenable to SAT-solver methods, and for formulas that are unsatisfiable, SAT-solvers generally get nowhere.

So no one has a good idea how to solve SAT in polynomial time, or how to prove that it can’t be done—researchers are completely stuck. The problem of determining whether or not SAT has a polynomial time solution is known as the “$\mathbf{P}$ vs. $\mathbf{NP}$” problem. It is the outstanding unanswered question in theoretical computer science. It is also one of the seven Millenium Problems: the Clay Institute will award you \$1,000,000 if you solve the $\mathbf{P}$ vs. $\mathbf{NP}$ problem.

$^1\mathbf{P}$ stands for problems whose instances can be solved in time that grows polynomially with the size of the instance. $\mathbf{NP}$ stands for nondeterministic polynomial time, but we’ll leave an explanation of what that is to texts on the theory of computational complexity.
