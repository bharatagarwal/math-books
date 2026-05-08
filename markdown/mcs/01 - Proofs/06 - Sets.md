## 4 Mathematical Data Types

We have assumed that you've already been introduced to the concepts of sets, sequences, and functions, and we've used them informally several times in previous sections. In this chapter, we'll now take a more careful look at these mathematical data types. We'll quickly review the basic definitions, add a few more such as "images" and "inverse images" that may not be familiar, and end the chapter with some methods for comparing the sizes of sets.

## 4.1 Sets

Informally, a set is a bunch of objects, which are called the elements of the set. The elements of a set can be just about anything: numbers, points in space, or even other sets. The conventional way to write down a set is to list the elements inside curly-braces. For example, here are some sets:

$$
A = \{\text{Alex}, \text{Tippy}, \text{Shells}, \text{Shadow}\}
$$

$$
\text{dead pets}
$$

$$
B = \{\text{red}, \text{blue}, \text{yellow}\}
$$

$$
\text{primary colors}
$$

$$
C = \{\{a, b\}, \{a, c\}, \{b, c\}\}
$$

$$
\text{a set of sets}
$$

This works fine for small finite sets. Other sets might be defined by indicating how to generate a list of them:

$$
D ::= \{1, 2, 4, 8, 16, \dots\}
$$

$$
\text{the powers of } 2
$$

The order of elements is not significant, so $\{x,y\}$ and $\{y,x\}$ are the same set written two different ways. Also, any object is, or is not, an element of a given set—there is no notion of an element appearing more than once in a set.¹ So, writing $\{x,x\}$ is just indicating the same thing twice: that $x$ is in the set. In particular, $\{x,x\} = \{x\}$.

The expression $e \in S$ asserts that $e$ is an element of set $S$. For example, $32 \in D$ and blue $\in B$, but Tailspin $\notin A$—yet.

Sets are simple, flexible, and everywhere. You'll find some set mentioned in nearly every section of this text.

¹It's not hard to develop a notion of *multisets* in which elements can occur more than once, but multisets are not ordinary sets and are not covered in this text.


### 4.1.1 Some Popular Sets

Mathematicians have devised special symbols to represent some common sets.

|  symbol | set | elements  |
| --- | --- | --- |
|  ∅ | the empty set | none  |
|  N | nonnegative integers | {0,1,2,3,...}  |
|  Z | integers | {...,-3,-2,-1,0,1,2,3,...}  |
|  Q | rational numbers | $\frac{1}{2}$, $-\frac{5}{3}$, 16, etc.  |
|  R | real numbers | $\pi$, $e$, $-9$, $\sqrt{2}$, etc.  |
|  C | complex numbers | $i$, $\frac{19}{2}$, $\sqrt{2}-2i$, etc.  |

A superscript “+” restricts a set to its positive elements; for example, $\mathbb{R}^+$ denotes the set of positive real numbers. Similarly, $\mathbb{Z}^-$ denotes the set of negative integers.

### 4.1.2 Comparing and Combining Sets

The expression $S \subseteq T$ indicates that set $S$ is a subset of set $T$, which means that every element of $S$ is also an element of $T$. For example, $\mathbb{N} \subseteq \mathbb{Z}$ because every nonnegative integer is an integer; $\mathbb{Q} \subseteq \mathbb{R}$ because every rational number is a real number, but $\mathbb{C} \not\subseteq \mathbb{R}$ because not every complex number is a real number.

As a memory trick, think of the “$\subseteq$” symbol as like the “$\leq$” sign with the smaller set or number on the left hand side. Notice that just as $n \leq n$ for any number $n$, also $S \subseteq S$ for any set $S$.

There is also a relation, $\subset$, on sets like the "less than" relation $<$ on numbers. $S \subset T$ means that $S$ is a subset of $T$, but the two are not equal. So just as $n \not\prec n$ for every number $n$, also $A \not\subset A$, for every set $A$. " $S \subset T$ " is read as " $S$ is a strict subset of $T$ ".

There are several basic ways to combine sets. For example, suppose

$$
X ::= \{1, 2, 3\},
$$

$$
Y ::= \{2, 3, 4\}.
$$

## Definition 4.1.1.

- The union of sets $A$ and $B$, denoted $A \cup B$, includes exactly the elements appearing in $A$ or $B$ or both. That is,

$$
x \in A \cup B \quad \text{IFF} \quad x \in A \text{ OR } x \in B.
$$

So $X \cup Y = \{1,2,3,4\}$.


- The intersection of $A$ and $B$, denoted $A \cap B$, consists of all elements that appear in both $A$ and $B$. That is,

$$
x \in A \cap B \quad \text{IEF} \quad x \in A \text{ AND } x \in B.
$$

So, $X \cap Y = \{2, 3\}$.

- The set difference of $A$ and $B$, denoted $A - B$, consists of all elements that are in $A$, but not in $B$. That is,

$$
x \in A - B \quad \text{IEF} \quad x \in A \text{ AND } x \notin B.
$$

So, $X - Y = \{1\}$ and $Y - X = \{4\}$.

Often all the sets being considered are subsets of a known domain of discourse, $D$. Then for any subset, $A$, of $D$, we define $\overline{A}$ to be the set of all elements of $D$ not in $A$. That is,

$$
\overline{A} ::= D - A.
$$

The set $\overline{A}$ is called the complement of $A$. So

$$
\overline{A} = \emptyset \quad \text{IEF} \quad A = D.
$$

For example, if the domain we're working with is the integers, the complement of the nonnegative integers is the set of negative integers:

$$
\overline{N} = \mathbb{Z}^{-}.
$$

We can use complement to rephrase subset in terms of equality

$$
A \subseteq B \text{ is equivalent to } A \cap \overline{B} = \emptyset.
$$

### 4.1.3 Power Set

The set of all the subsets of a set, $A$, is called the power set, $\operatorname{pow}(A)$, of $A$. So

$$
B \in \operatorname{pow}(A) \quad \text{IEF} \quad B \subseteq A.
$$

For example, the elements of $\operatorname{pow}(\{1,2\})$ are $\emptyset, \{1\}, \{2\}$ and $\{1,2\}$.

More generally, if $A$ has $n$ elements, then there are $2^n$ sets in $\operatorname{pow}(A)$—see Theorem 4.5.5. For this reason, some authors use the notation $2^A$ instead of $\operatorname{pow}(A)$.


### 4.1.4 Set Builder Notation

An important use of predicates is in set builder notation. We'll often want to talk about sets that cannot be described very well by listing the elements explicitly or by taking unions, intersections, etc., of easily described sets. Set builder notation often comes to the rescue. The idea is to define a set using a predicate; in particular, the set consists of all values that make the predicate true. Here are some examples of set builder notation:

$$
A ::= \{n \in \mathbb{N} \mid n \text{ is a prime and } n = 4k + 1 \text{ for some integer } k\}
$$

$$
B ::= \{x \in \mathbb{R} \mid x^3 - 3x + 1 > 0\}
$$

$$
C ::= \{a + bi \in \mathbb{C} \mid a^2 + 2b^2 \leq 1\}
$$

The set $A$ consists of all nonnegative integers $n$ for which the predicate

“$n$ is a prime and $n = 4k + 1$ for some integer $k$”

is true. Thus, the smallest elements of $A$ are:

$$
5, 13, 17, 29, 37, 41, 53, 61, 73, \dots.
$$

Trying to indicate the set $A$ by listing these first few elements wouldn't work very well; even after ten terms, the pattern is not obvious! Similarly, the set $B$ consists of all real numbers $x$ for which the predicate

$$
x^3 - 3x + 1 > 0
$$

is true. In this case, an explicit description of the set $B$ in terms of intervals would require solving a cubic equation. Finally, set $C$ consists of all complex numbers $a + bi$ such that:

$$
a^2 + 2b^2 \leq 1
$$

This is an oval-shaped region around the origin in the complex plane.

### 4.1.5 Proving Set Equalities

Two sets are defined to be equal if they have exactly the same elements. That is, $X = Y$ means that $z \in X$ if and only if $z \in Y$, for all elements, $z$. So, set equalities can be formulated and proved as “iff” theorems. For example:

2This is actually the first of the ZFC axioms for set theory mentioned at the end of Section 1.3 and discussed further in Section 7.3.2.


**Theorem 4.1.2.** [Distributive Law for Sets] Let $A$, $B$, and $C$ be sets. Then:

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \tag{4.1}
$$

**Proof.** The equality (4.1) is equivalent to the assertion that

$$
z \in A \cap (B \cup C) \quad \text{iff} \quad z \in (A \cap B) \cup (A \cap C) \tag{4.2}
$$

for all $z$. Now we'll prove (4.2) by a chain of iff's.

Now we have

$$
z \in A \cap (B \cup C)
$$

$$
\text{iff} \quad (z \in A) \text{ AND } (z \in B \cup C) \tag{def of \cap}
$$

$$
\text{iff} \quad (z \in A) \text{ AND } (z \in B \text{ OR } z \in C) \tag{def of \cup}
$$

$$
\text{iff} \quad (z \in A \text{ AND } z \in B) \text{ OR } (z \in A \text{ AND } z \in C) \quad (\text{AND distributivity Thm 3.4.1})
$$

$$
\text{iff} \quad (z \in A \cap B) \text{ OR } (z \in A \cap C) \tag{def of \cap}
$$

$$
\text{iff} \quad z \in (A \cap B) \cup (A \cap C) \tag{def of \cup}
$$

■

Although the basic set operations and propositional connectives are similar, it's important not to confuse one with the other. For example, $\cup$ resembles OR, and in fact was defined directly in terms of OR:

$$
x \in A \cup B \text{ is equivalent to } (x \in A \text{ OR } x \in B).
$$

Similarly, $\cap$ resembles AND, and complement resembles NOT.

But if $A$ and $B$ are sets, writing $A$ AND $B$ is a type-error, since AND is an operation on truth-values, not sets. Similarly, if $P$ and $Q$ are propositional variables, writing $P \cup Q$ is another type-error.

The proof of Theorem 4.1.2 illustrates a general method for proving a set equality involving the basic set operations by checking that a corresponding propositional formula is valid. As a further example, from De Morgan's Law (3.11) for propositions

$$
\mathrm{NOT}(P \text{ AND } Q) \text{ is equivalent to } \overline{P} \text{ OR } \overline{Q}
$$

we can derive (Problem 4.5) a corresponding De Morgan's Law for set equality:

$$
\overline{A \cap B} = \overline{A} \cup \overline{B}. \tag{4.3}
$$

Despite this correspondence between two kinds of operations, it's important not to confuse propositional operations with set operations. For example, if $X$ and $Y$


are sets, then it is wrong to write “ $X$  AND  $Y$ ” instead of “ $X \cap Y$ .” Applying AND to sets will cause your compiler—or your grader—to throw a type error, because an operation that is only supposed to be applied to truth values has been applied to sets. Likewise, if  $P$  and  $Q$  are propositions, then it is a type error to write “ $P \cup Q$ ” instead of “ $P$  OR  $Q$ .”

## 4.2 Sequences

Sets provide one way to group a collection of objects. Another way is in a sequence, which is a list of objects called terms or components. Short sequences are commonly described by listing the elements between parentheses; for example,  $(a,b,c)$  is a sequence with three terms.

While both sets and sequences perform a gathering role, there are several differences.

- The elements of a set are required to be distinct, but terms in a sequence can be the same. Thus,  $(a,b,a)$  is a valid sequence of length three, but  $\{a,b,a\}$  is a set with two elements, not three.
- The terms in a sequence have a specified order, but the elements of a set do not. For example,  $(a,b,c)$  and  $(a,c,b)$  are different sequences, but  $\{a,b,c\}$  and  $\{a,c,b\}$  are the same set.
- Texts differ on notation for the empty sequence; we use  $\lambda$  for the empty sequence.

The product operation is one link between sets and sequences. A Cartesian product of sets,  $S_{1} \times S_{2} \times \dots \times S_{n}$ , is a new set consisting of all sequences where the first component is drawn from  $S_{1}$ , the second from  $S_{2}$ , and so forth. Length two sequences are called pairs. For example,  $\mathbb{N} \times \{a, b\}$  is the set of all pairs whose first element is a nonnegative integer and whose second element is an  $a$  or a  $b$ :

$$
\mathbb {N} \times \{a, b \} = \{(0, a), (0, b), (1, a), (1, b), (2, a), (2, b), \dots \}
$$

A product of  $n$  copies of a set  $S$  is denoted  $S^n$ . For example,  $\{0,1\}^3$  is the set of all 3-bit sequences:

$$
\{0, 1 \} ^ {3} = \{(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1) \}
$$

3Some texts call them ordered pairs.
