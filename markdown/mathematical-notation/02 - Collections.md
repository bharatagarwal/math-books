# Collections

## 1. Sets

A set is an unordered collection of things in which repetition is forbidden. The simplest way to specify a set is to list its objects between curly braces: $\{1,2,7\}$. This is a set containing exactly three objects: the numbers $1$, $2$, and $7$. Order and repetition do not matter, so $\{2,1,7\}$ and $\{7,1,1,2\}$ are the same set with precisely the same three elements.

Membership in a set is indicated with the special symbol $\in$ which is often pronounce “is an element of”. The symbol looks like the Greek epsilon ($\epsilon$) but is, in fact, different (though some people use it for set membership nonetheless). Thus $x \in A$ asserts that the object $x$ is an element of the set $A$. For example: $2 \in \{1, 2, 7\}$. The symbol $\notin$ means not an element of as in $3 \notin \{1, 2, 7\}$. When the symbol $\in$ is written backwards$^1$ ($\ni$) it means, includes the element, like this: $A \ni x$. This means exactly the same thing as $x \in A$. For example, $\{1, 2, 7\} \ni 7$.

The set containing no elements is called the empty set or null set. It is denoted by the symbol $\emptyset$ or $\varnothing$, or by an empty pair of braces $\{\}$. Of these, $\varnothing$ is the clearest.

Large sets may be specified by listing a few elements and then suggesting the pattern continues using ellipses (...). This is handy for both finite and infinite sets provided the pattern established is crystal clear. For example: $\{1,2,3,\ldots,100\}$ is clearly the set of integers from 1 to 100 inclusive and $\{2,4,6,8,\ldots\}$ is the set of positive even numbers.

However, a less ambiguous (if more elaborate) way to describe a set is to use set builder notation. The notation looks like this:

$$
\{x \in \mathbb{Z} : 1 \leq x \leq 100\}.
$$

The letter $x$ is a dummy variable; its purpose is to stand for a generic name for the elements of this set. Next we read “$\in \mathbb{Z}$” which means the elements of this set come from the set of integers$^2$. After this preamble, which is punctuated by a colon, is a condition that tells us which integers are in this set. In this case, they are the integers that are at least 1 and at most 100. Incidentally, the set of integers from 1 to $n$ inclusive is sometimes written $[n]$.

$^1$The symbol $\ni$ (or $\ni$) is sometimes used as an abbreviation for the words such that. If one wishes to abbreviate this expression, it is much clearer to simply write “s.t.”

$^2$The symbol $\mathbb{Z}$ stands for the set of all integers; see §4.2 on page 15.


Sometimes the colon is replaced by a vertical bar $|$ as in $\{u \in \mathbb{Z} \mid u \geq 100\}$. This, of course, is the set $\{100, 101, 102, \ldots\}$.

The condition after the colon or vertical bar may be expressed in words. For example:

$$
\{a \in \mathbb{Z} : a \text{ is divisible by } 5\}
$$

is the set $\{\ldots, -15, -10, -5, 0, 5, 10, 15, \ldots\}$.

If the context is clear, this notation may be abbreviated to omit the set to the left of the colon; for example, $\{n : n &gt; 5\}$. The problem, of course, is that it is unclear if this means all real numbers that are greater than 5, or just the integers 6 and up.

More elaborate expressions may appear to the left of the colon. For example, $\{(x,y) : x + y = 5\}$ stands for a set of ordered pairs that includes the element (2, 3) but not the element (4, 4).

There are a variety of relations and operations involving sets; here are the ones most frequently encountered.

- Set equality. If $A$ and $B$ are sets, then $A = B$ means that $A$ and $B$ have exactly the same elements.
- Subset. If $A$ and $B$ are sets, $A \subseteq B$ means that every element of $A$ is also an element of $B$. Some older books (and professors) might simply write $A \subset B$. It would be preferable to reserve $\subset$ to mean "subset but not equal" so that $\subset / \subseteq$ are analogous to $&lt; / \leq$, but this usage is not universally accepted.

Note that $A \subseteq B$ does not mean the same thing as $A \in B$.

- Superset. $A \supseteq B$ means $B \subseteq A$. That is, the elements of $A$ include all the elements of $B$ (and possibly more). Some people write $\supset$ for $\supseteq$.
- Union. If $A$ and $B$ are sets, then $A \cup B$ (the union of $A$ and $B$) is the set whose elements that are in $A$ or $B$ or both. For example,

$$
\{1, 2, 3\} \cup \{2, 4, 6\} = \{1, 2, 3, 4, 6\}.
$$

A variety of special notation is used to indicate the disjoint union of sets. Some of the symbols used are $+, \oplus, \uplus, \cup, \sqcup$, and $\sqcup$. In all cases the notation takes on a double meaning. First, it asserts the sets in question are pairwise disjoint (no element is common to any two); second, it expresses the union of those sets. For example, if you read

$$
A_1 \cup A_2 \cup \cdots \cup A_n = B
$$

then you know (a) that $A_i \cap A_j = \emptyset$ for all $i \neq j$ and (b) the union of the sets $A_1, A_2, \ldots, A_n$ is $B$.

- Intersection. If $A$ and $B$ are sets, then $A \cap B$ (the intersection of $A$ and $B$) is the set whose elements that are in both $A$ and $B$. For example,

$$
\{1, 2, 3\} \cap \{2, 4, 6\} = \{2\}.
$$


- Difference. If $A$ and $B$ are sets, then $A - B$ is the set of all elements of $A$ that are not elements of $B$. For example,

$$
\{1, 2, 3 \} - \{2, 4, 6 \} = \{1, 3 \}.
$$

Some people write set difference like this $A \setminus B$ to distinguish set difference from ordinary subtraction.

- Complement. If $A$ is a set, then $\overline{A}$ stands for the set of all elements that are not in $A$. One needs to be careful about context with this notation; that is, there needs to be a clearly articulated "universe" of elements. For example, if the context is the integers and $X$ is the set of odd integers, then $\overline{X}$ is the set of even integers. Generally, it is better to use set difference, like this: $\mathbb{Z} - X$.

- Symmetric difference. If $A$ and $B$ are sets, then $A \triangle B$ is the set of all elements that are in $A$ or $B$ but not both.

$$
\{1, 2, 3 \} \triangle \{2, 4, 6 \} = \{1, 3, 4, 6 \}.
$$

Observe that $A \triangle B = (A \cup B) - (A \cap B) = (A - B) \cup (B - A)$.

- Cardinality. If $A$ is a set, then $|A|$ denotes the number of elements in $A$. This is also sometimes written $\#A$. For example, if $A = \{1,2,4\}$, then $|A| = 3$.

- Cartesian product. Given sets $A$ and $B$, their Cartesian product is the set

$$
A \times B = \{(a, b): a \in A, b \in B \}.
$$

For example,

$$
\{1, 2, 3 \} \times \{3, 4 \} = \{(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4) \}.
$$

The notation $A^2$ stands for $A \times A$; that is, the set of all ordered pairs $(x,y)$ with $x,y \in A$.

More generally, $A^n$ (where $n$ is a positive integer) is the set of all $n$-long lists of elements of $A$. See the Lists section on the next page.

- Power set. If $A$ is a set, then the power set of $A$ is the set of all subsets of $A$. This is typically denoted $2^A$ or $\mathcal{P}(A)$. For example, if $A = \{1, 2, 3\}$ then

$$
\mathcal{P}(A) = 2^A = \left\{ \{1, 2, 3 \}, \{1, 2 \}, \{1, 3 \}, \{2, 3 \}, \{1 \}, \{2 \}, \{3 \}, \emptyset \right\}.
$$

- Set exponentiation. If $A$ and $B$ are sets, then $B^A$ stands for the set of all functions from $A$ to $B$; that is,

$$
B^A = \{f \mid f: A \to B \}.
$$

See page 25 for an explanation of the notation $f \colon A \to B$.

The rationale for this notation is as follows. If $A$ and $B$ are finite sets with $|A| = a$ and $|B| = b$, then there are $b^a$ functions from $A$ to $B$. In symbols: $|B^A| = |B|^{|A|}$.


- Maximum and minimum. If $A$ is a set of real numbers, then $\max A$ stands for the largest element in $A$ and $\min A$ stands for the smallest element in $A$. The wedge and vee symbols are also used in this context:

$x\vee y=\max\{x,y\}\qquad\text{and}\qquad x\wedge y=\min\{x,y\}.$

Not all sets of numbers necessarily contain a maximum or minimum element. A related pair of notions are the *supremum* and *infimum* denoted $\sup A$ and $\inf A$. The supremum is also called the *least upper bound* and the infimum is called the *greatest lower bound*; these are sometimes abbreviated lub and glb.

## 2. Lists

In mathematics, a list is an ordered collection of objects in which repetition is permitted. A list is usually enclosed in round parentheses (although sometimes square brackets are used). For example, $(1,2,2,3)$ is a list. The lists $(1,2,2,3)$, $(1,2,3)$, and $(2,1,2,3)$ are all different as order matters and elements may be repeated.

A list of $n$ elements is sometimes called an *$n$-tuple*.

When a list is named by a letter (e.g., $a$), the elements of that list are typically named $a_{1}$, $a_{2}$, etc.

## 3. Big sums, products, and so on

The symbols $\sum$ and $\prod$ are used to represent the sum and product of a collection of numbers. A typical use of the sum notation has the following form:

$\sum_{j=\text{start}}^{\text{stop}}\text{expression involving }j.$

The letter $j$ is a dummy variable. For example,

$\sum_{j=1}^{5}x^{j}=x^{1}+x^{2}+x^{3}+x^{4}+x^{5}.$

If the upper index in the sum is $\infty$, this means that the sum goes on without end:

$\sum_{n=0}^{\infty}\frac{1}{2^{n}}=1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\cdots.$

The $\prod$ notation is exactly analogous to the $\sum$ notation, but signifies multiplication. For example,

$\prod_{j=0}^{5}(2j+1)=1\times 3\times 5\times 7\times 9\times 11.$


In these examples the sum/product index (dummy variable) traverses a contiguous stretch of integers. However, sometimes we may wish to sum over other kinds of indices.

For example, if $A$ is the set $\{1,5,6,22\}$ then

$\sum_{t\in A}t^{2}=1^{2}+5^{2}+6^{2}+22^{2}.$

Alternatively, a brief description of the desired indices may be written below the sum or product symbol. For example:

$\prod_{p\text{ prime}}\left(1-\frac{1}{p}\right)=\left(1-\frac{1}{2}\right)\times\left(1-\frac{1}{3}\right)\times\left(1-\frac{1}{5}\right)\times\left(1-\frac{1}{7}\right)\times\left(1-\frac{1}{11}\right)\times\cdots.$

Sometimes a summation expression is presented without any indication as to which variable is the dummy variable and without specifying upper/lower limits for that index. In such situations, it is often the case that a repeated variable is the summation index. For example, if you see

$\sum\binom{n}{k}x^{k}$

then it is likely that $k$ is the summation index. One then has to infer the proper range for $k$. In this case, since $\binom{n}{k}$ is defined only for $k\geq 0$ and is zero for $k>n$, it’s a safe bet that $k$ ranges from $0$ to $n$. In general, if no upper or lower bounds are given for the a index, then the sum is over all allowable values for that index. For example, if $A$ is an $n\times m$-matrix and $B$ is an $m\times p$-matrix, then

$\sum a_{i,j}b_{j,k}$

likely means that the sum is for $j=1,2,3,\ldots,m$.

In some contexts, it is convenient write sums without the $\sum$ symbol altogether by using Einstein notation. In this notation, the $\sum$ symbol is omitted. Any time an index (typically a subscript) is repeated, one sums over the range of that index. For example, the term $a_{i,j}b_{j}$ means

$\sum_{j}a_{i,j}b_{j}$

where the range of $j$ is (we hope) clear from context.

Following this convention, if $A$ is a square matrix, then $a_{i,i}$ would be the trace of $A$. For appropriately shaped matrices $A$ and $B$, $a_{i,j}b_{j,k}$ would denote the $i,k$-entry of $AB$.

Analogues of the $\sum$ and $\prod$ notation are used for other operations. For example if $A_{1}$, $A_{2}$, $A_{3}$,$\ldots$ are sets, their union may be written like this:

$\bigcup_{i=1}^{\infty}A_{i}$

which means, of course, $A_{1}\cup A_{2}\cup A_{3}\cup\cdots$. Likewise $\bigcap_{i=1}^{\infty}A_{i}$ is their intersection.


In general, most operation symbols may be written large with a dummy variable index. For example, if $p_1, p_2, \ldots, p_n$ are Boolean (true/false) values (see Chapter 3), then

$$
\bigwedge_{i=1}^{n} p_i
$$

means $p_1 \wedge p_2 \wedge \cdots \wedge p_n$.
