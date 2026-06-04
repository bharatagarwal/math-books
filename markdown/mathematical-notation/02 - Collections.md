# Collections

Georg Cantor invented set theory in the 1870s and almost immediately it became the foundation of all mathematics. The idea was deceptively simple: a *set* is a collection of distinct objects, considered as an object in its own right. That one move — treating a collection as a thing — let mathematicians build numbers, functions, spaces, and eventually all of modern mathematics from a single primitive concept.

Cantor also showed that some infinities are bigger than others (the reals outnumber the integers), a result so shocking that his contemporaries called it a "disease" from which mathematics would eventually recover. It never did. Set notation is now the universal language.

If you've used Python's `set` type, you already know the basics. The notation is almost identical.

## Sets

A set is an unordered collection of things in which repetition is forbidden. The simplest way to specify a set is to list its objects between curly braces: $\{1, 2, 7\}$. This is a set containing exactly three objects: the numbers $1$, $2$, and $7$. Order and repetition do not matter, so $\{2, 1, 7\}$ and $\{7, 1, 1, 2\}$ are the same set with precisely the same three elements.

### Membership

Membership in a set is indicated with the special symbol $\in$, which is often pronounced "is an element of." Thus $x \in A$ asserts that the object $x$ is an element of the set $A$. For example: $2 \in \{1, 2, 7\}$. The symbol $\notin$ means "not an element of," as in $3 \notin \{1, 2, 7\}$.

The set containing no elements is called the *empty set* or *null set*. It is denoted by the symbol $\varnothing$, or by an empty pair of braces $\{\}$.

### Set-builder notation

Large sets may be specified by listing a few elements and then suggesting the pattern continues using ellipses: $\{1, 2, 3, \ldots, 100\}$ is the set of integers from 1 to 100, and $\{2, 4, 6, 8, \ldots\}$ is the set of positive even numbers.

However, a less ambiguous way to describe a set is to use *set-builder notation*:

$$
\{x \in \mathbb{Z} : 1 \leq x \leq 100\}
$$

The letter $x$ is a dummy variable. Next we read "$\in \mathbb{Z}$" which means the elements come from the integers. After the colon is a condition. Sometimes a vertical bar $|$ replaces the colon: $\{u \in \mathbb{Z} \mid u \geq 100\}$.

More elaborate expressions may appear to the left of the colon. For example, $\{(x, y) : x + y = 5\}$ is a set of ordered pairs.

If you've written a Python set comprehension, you've written set-builder notation:

| Math | Python |
| --- | --- |
| $\{x \in \mathbb{Z} : 1 \leq x \leq 100\}$ | `{x for x in range(1, 101)}` |
| $\{a \in \mathbb{Z} : 5 \mid a\}$ | `{a for a in range(...) if a % 5 == 0}` |
| $\{x^2 : x \in \{1, \ldots, 10\}\}$ | `{x**2 for x in range(1, 11)}` |

### Operations on sets

There are a variety of relations and operations involving sets. Python's `set` type implements all of them:

```python
<!-- include: code/mathematical-notation/02 - Collections/01_python.py -->
```

Here is the full catalogue of standard set operations:

- **Set equality.** $A = B$ means $A$ and $B$ have exactly the same elements.

- **Subset.** $A \subseteq B$ means every element of $A$ is also in $B$. Some older books write $A \subset B$. It would be preferable to reserve $\subset$ for "subset but not equal" (analogous to $<$ vs. $\leq$), but usage is not universal. Note that $A \subseteq B$ does not mean the same thing as $A \in B$.

- **Superset.** $A \supseteq B$ means $B \subseteq A$.

- **Union.** $A \cup B$ is the set of elements in $A$ or $B$ or both.

$$
\{1, 2, 3\} \cup \{2, 4, 6\} = \{1, 2, 3, 4, 6\}
$$

- **Intersection.** $A \cap B$ is the set of elements in both $A$ and $B$.

$$
\{1, 2, 3\} \cap \{2, 4, 6\} = \{2\}
$$

- **Difference.** $A - B$ (or $A \setminus B$) is the set of elements in $A$ that are not in $B$.

$$
\{1, 2, 3\} - \{2, 4, 6\} = \{1, 3\}
$$

- **Complement.** $\overline{A}$ is the set of all elements (in some universe) not in $A$. Context determines the universe.

- **Symmetric difference.** $A \triangle B$ is the set of elements in $A$ or $B$ but not both. Equivalently, $A \triangle B = (A \cup B) - (A \cap B) = (A - B) \cup (B - A)$. In Python, this is `A ^ B` — the XOR of sets.

$$
\{1, 2, 3\} \triangle \{2, 4, 6\} = \{1, 3, 4, 6\}
$$

- **Cardinality.** $|A|$ denotes the number of elements in $A$. For $A = \{1, 2, 4\}$, $|A| = 3$.

- **Cartesian product.** $A \times B = \{(a, b) : a \in A,\; b \in B\}$. The notation $A^2$ means $A \times A$; more generally, $A^n$ is the set of all $n$-long lists of elements of $A$.

$$
\{1, 2, 3\} \times \{3, 4\} = \{(1,3), (1,4), (2,3), (2,4), (3,3), (3,4)\}
$$

### Power set

If $A$ is a set, its *power set* $\mathcal{P}(A)$ (also written $2^A$) is the set of all subsets of $A$:

$$
\mathcal{P}(\{1, 2, 3\}) = \bigl\{\{1,2,3\},\; \{1,2\},\; \{1,3\},\; \{2,3\},\; \{1\},\; \{2\},\; \{3\},\; \varnothing\bigr\}
$$

The notation $2^A$ makes sense because $|\mathcal{P}(A)| = 2^{|A|}$: each element is either in or out of a subset, giving $2^n$ choices for an $n$-element set.

We can verify this computationally — and see the set-builder / comprehension parallel in action:

```python
<!-- include: code/mathematical-notation/02 - Collections/02_python.py -->
```

### Set exponentiation

If $A$ and $B$ are sets, then $B^A$ stands for the set of all functions from $A$ to $B$:

$$
B^A = \{f \mid f \colon A \to B\}
$$

If $|A| = a$ and $|B| = b$, then $|B^A| = b^a$. This is why the power set is written $2^A$: a subset of $A$ is the same as a function $A \to \{0, 1\}$ (each element is in or out).

### Supremum and infimum

If $A$ is a set of real numbers, then $\max A$ is the largest element and $\min A$ is the smallest. The wedge and vee symbols are also used:

$$
x \vee y = \max\{x, y\} \qquad \text{and} \qquad x \wedge y = \min\{x, y\}
$$

Not all sets contain a maximum or minimum element. A related pair of notions are the *supremum* ($\sup A$, the least upper bound) and *infimum* ($\inf A$, the greatest lower bound).

## Lists

A *list* (or *tuple*) is an ordered collection in which repetition is permitted. Lists are enclosed in round parentheses: $(1, 2, 2, 3)$. Unlike sets, order matters and elements may be repeated, so $(1, 2, 2, 3)$, $(1, 2, 3)$, and $(2, 1, 2, 3)$ are all different lists.

A list of $n$ elements is called an *$n$-tuple*. When a list is named by a letter (e.g., $a$), the elements are typically named $a_1, a_2$, etc.

## Big sums, products, and so on

The symbols $\sum$ and $\prod$ are used for the sum and product of a collection of numbers. They are the mathematical equivalent of `reduce`: take a binary operation and fold it over a sequence.

$$
\sum_{j=1}^{5} x^j = x^1 + x^2 + x^3 + x^4 + x^5
$$

$$
\prod_{j=0}^{5} (2j+1) = 1 \times 3 \times 5 \times 7 \times 9 \times 11
$$

If the upper index is $\infty$, the sum goes on without end:

$$
\sum_{n=0}^{\infty} \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = 2
$$

The index can also range over a set. If $A = \{1, 5, 6, 22\}$:

$$
\sum_{t \in A} t^2 = 1^2 + 5^2 + 6^2 + 22^2
$$

Or a condition: the product over all primes (Euler's product, 1737):

$$
\prod_{p \text{ prime}} \left(1 - \frac{1}{p}\right) = \left(1 - \frac{1}{2}\right) \times \left(1 - \frac{1}{3}\right) \times \left(1 - \frac{1}{5}\right) \times \cdots
$$

SymPy handles all of these — finite products, infinite sums, and symbolic evaluation:

```python
<!-- include: code/mathematical-notation/02 - Collections/03_python.py -->
```

### Einstein summation

In some contexts, the $\sum$ symbol is omitted entirely. In *Einstein notation*, any repeated index is implicitly summed. The expression $a_{i,j} b_j$ means $\sum_j a_{i,j} b_j$. If $A$ is a square matrix, then $a_{i,i}$ is the trace. For matrices $A$ and $B$, $a_{i,j} b_{j,k}$ is the $i,k$-entry of $AB$.

Einstein reportedly joked that this was "the only useful thing" he contributed to mathematics. NumPy's `einsum` function implements it directly: `np.einsum('ij,j->i', A, b)` is matrix-vector multiplication.

### Analogues

The $\sum$ and $\prod$ pattern generalizes. If $A_1, A_2, \ldots$ are sets:

$$
\bigcup_{i=1}^{\infty} A_i = A_1 \cup A_2 \cup A_3 \cup \cdots
$$

$$
\bigcap_{i=1}^{\infty} A_i = A_1 \cap A_2 \cap A_3 \cap \cdots
$$

If $p_1, \ldots, p_n$ are Boolean values:

$$
\bigwedge_{i=1}^{n} p_i = p_1 \wedge p_2 \wedge \cdots \wedge p_n
$$

In general, most binary operations can be "biggified" with a dummy index — the mathematical version of `functools.reduce`.
