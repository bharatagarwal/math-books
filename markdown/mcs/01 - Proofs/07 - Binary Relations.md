## 4.3 Functions

### 4.3.1 Domains and Images

A function assigns an element of one set, called the domain, to an element of another set, called the codomain. The notation

$$
f: A \to B
$$

indicates that  $f$  is a function with domain,  $A$ , and codomain,  $B$ . The familiar notation  $f(a) = b$  indicates that  $f$  assigns the element  $b \in B$  to  $a$ . Here  $b$  would be called the value of  $f$  at argument  $a$ .

Functions are often defined by formulas, as in:

$$
f _ {1} (x) ::= \frac {1}{x ^ {2}}
$$

where  $x$  is a real-valued variable, or

$$
f _ {2} (y, z) ::= y 1 0 y z
$$

where  $y$  and  $z$  range over binary strings, or

$$
f _ {3} (x, n) ::= \text {the length} n \text {sequence} \underbrace {(x , \dots , x)} _ {n x ^ {\prime} s}
$$

where  $n$  ranges over the nonnegative integers.

A function with a finite domain could be specified by a table that shows the value of the function at each element of the domain. For example, a function  $f_{4}(P, Q)$  where  $P$  and  $Q$  are propositional variables is specified by:

|  P Q | f4(P, Q)  |
| --- | --- |
|  T T | T  |
|  T F | F  |
|  F T | T  |
|  F F | T  |

Notice that  $f_{4}$  could also have been described by a formula:

$$
f _ {4} (P, Q) ::= [ P \text {I M P L I E S} Q ].
$$

A function might also be defined by a procedure for computing its value at any element of its domain, or by some other kind of specification. For example, define


$f_{5}(y)$ to be the length of a left to right search of the bits in the binary string $y$ until a 1 appears, so

$$
f_{5}(0010) = 3,
$$

$$
f_{5}(100) = 1,
$$

$$
f_{5}(0000) \quad \text{is} \quad \text{undefined}.
$$

Notice that $f_{5}$ does not assign a value to any string of just 0's. This illustrates an important fact about functions: they need not assign a value to every element in the domain. In fact this came up in our first example $f_{1}(x) = 1 / x^{2}$, which does not assign a value to 0. So in general, functions may be partial functions, meaning that there may be domain elements for which the function is not defined. If a function is defined on every element of its domain, it is called a total function.

It's often useful to find the set of values a function takes when applied to the elements in a set of arguments. So if $f: A \to B$, and $S$ is a subset of $A$, we define $f(S)$ to be the set of all the values that $f$ takes when it is applied to elements of $S$. That is,

$$
f(S) ::= \{b \in B \mid f(s) = b \text{ for some } s \in S\}.
$$

For example, if we let $[r,s]$ denote set of numbers in the interval from $r$ to $s$ on the real line, then $f_{1}([1,2]) = [1/4, 1]$.

For another example, let's take the "search for a 1" function, $f_{5}$. If we let $X$ be the set of binary words which start with an even number of 0's followed by a 1, then $f_{5}(X)$ would be the odd nonnegative integers.

Applying $f$ to a set, $S$, of arguments is referred to as "applying $f$ pointwise to $S$", and the set $f(S)$ is referred to as the image of $S$ under $f$. The set of values that arise from applying $f$ to all possible arguments is called the range of $f$. That is,

$$
\operatorname{range}(f) ::= f(\operatorname{domain}(f)).
$$

Some authors refer to the codomain as the range of a function, but they shouldn't. The distinction between the range and codomain will be important later in Sections 4.5 when we relate sizes of sets to properties of functions between them.

### 4.3.2 Function Composition

Doing things step by step is a universal idea. Taking a walk is a literal example, but so is cooking from a recipe, executing a computer program, evaluating a formula, and recovering from substance abuse.

4There is a picky distinction between the function $f$ which applies to elements of $A$ and the function which applies $f$ pointwise to subsets of $A$, because the domain of $f$ is $A$, while the domain of pointwise-$f$ is $\operatorname{pow}(A)$. It is usually clear from context whether $f$ or pointwise-$f$ is meant, so there is no harm in overloading the symbol $f$ in this way.


## 4.4 Binary Relations


Abstractly, taking a step amounts to applying a function, and going step by step corresponds to applying functions one after the other. This is captured by the operation of composing functions. Composing the functions $f$ and $g$ means that first $f$ is applied to some argument, $x$, to produce $f(x)$, and then $g$ is applied to that result to produce $g(f(x))$.

**Definition 4.3.1.** For functions $f: A \to B$ and $g: B \to C$, the composition, $g \circ f$, of $g$ with $f$ is defined to be the function from $A$ to $C$ defined by the rule:

$$
(g \circ f) (x) ::= g (f (x)),
$$

for all $x\in A$.

Function composition is familiar as a basic concept from elementary calculus, and it plays an equally basic role in discrete mathematics.


Binary relations define relations between two objects. For example, "less-than" on the real numbers relates every real number, $a$, to a real number, $b$, precisely when $a < b$. Similarly, the subset relation relates a set, $A$, to another set, $B$, precisely when $A \subseteq B$. A function $f: A \to B$ is a special case of binary relation in which an element $a \in A$ is related to an element $b \in B$ precisely when $b = f(a)$.

In this section we'll define some basic vocabulary and properties of binary relations.

**Definition 4.4.1.** A binary relation, $R$, consists of a set, $A$, called the domain of $R$, a set, $B$, called the codomain of $R$, and a subset of $A \times B$ called the graph of $R$.

A relation whose domain is $A$ and codomain is $B$ is said to be "between $A$ and $B$", or "from $A$ to $B$." As with functions, we write $R: A \to B$ to indicate that $R$ is a relation from $A$ to $B$. When the domain and codomain are the same set, $A$, we simply say the relation is "on $A$." It's common to use "$a R b$" to mean that the pair $(a, b)$ is in the graph of $R$.

Notice that Definition 4.4.1 is exactly the same as the definition in Section 4.3 of a function, except that it doesn't require the functional condition that, for each

5Writing the relation or operator symbol between its arguments is called *infix notation*. Infix expressions like "$m < n$" or "$m + n$" are the usual notation used for things like the less-then relation or the addition operation rather than prefix notation like "$< (m,n)$" or "$+(m,n)$."


domain element, $a$, there is at most one pair in the graph whose first coordinate is $a$. As we said, a function is a special case of a binary relation.

The "in-charge of" relation, $Chrg$, for MIT in Spring '10 subjects and instructors is a handy example of a binary relation. Its domain, $Fac$, is the names of all the MIT faculty and instructional staff, and its codomain is the set, $SubNums$, of subject numbers in the Fall '09–Spring '10 MIT subject listing. The graph of $Chrg$ contains precisely the pairs of the form

$$
(\langle \text{instructor-name} \rangle, \langle \text{subject-num} \rangle)
$$

such that the faculty member named $\langle \text{instructor-name} \rangle$ is in charge of the subject with number $\langle \text{subject-num} \rangle$ that was offered in Spring '10. So graph(Chrg) contains pairs like

(T. Eng, 6.UAT)
(G. Freeman, 6.011)
(G. Freeman, 6.UAT)
(G. Freeman, 6.881)
(G. Freeman, 6.882)
(J. Guttag, 6.00)
(A. R. Meyer, 6.042) (4.4)
(A. R. Meyer, 18.062)
(A. R. Meyer, 6.844)
(T. Leighton, 6.042)
(T. Leighton, 18.062)

Some subjects in the codomain, SubNums, do not appear among this list of pairs—that is, they are not in range(Chrg). These are the Fall term-only subjects. Similarly, there are instructors in the domain, Fac, who do not appear in the list because they are not in charge of any Spring term subjects.

### 4.4.1 Relation Diagrams

Some standard properties of a relation can be visualized in terms of a diagram. The diagram for a binary relation, $R$, has points corresponding to the elements of the domain appearing in one column (a very long column if domain($R$) is infinite). All the elements of the codomain appear in another column which we'll usually picture as being to the right of the domain column. There is an arrow going from a point, $a$, in the lefthand, domain column to a point, $b$, in the righthand, codomain column, precisely when the corresponding elements are related by $R$. For example, here are diagrams for two functions:


# 4.4. Binary Relations

![img-0.jpeg](07 - Binary Relations_images/img-0.jpeg)

![img-1.jpeg](07 - Binary Relations_images/img-1.jpeg)

Being a function is certainly an important property of a binary relation. What it means is that every point in the domain column has at most one arrow coming out of it. So we can describe being a function as the “ $\leq 1$  arrow out” property. There are four more standard properties of relations that come up all the time. Here are all five properties defined in terms of arrows:

Definition 4.4.2. A binary relation,  $R$ , is:

- a function when it has the  $[\leq 1$  arrow out] property.
- surjective when it has the  $[\geq 1$  arrows in] property. That is, every point in the righthand, codomain column has at least one arrow pointing to it.
- total when it has the  $[\geq 1$  arrows out] property.
- injective when it has the  $[\leq 1$  arrow in] property.
- bijective when it has both the  $[= 1$  arrow out] and the  $[= 1$  arrow in] property.

From here on, we'll stop mentioning the arrows in these properties and for example, just write  $[\leq 1$  in] instead of  $[\leq 1$  arrows in].

So in the diagrams above, the relation on the left has the  $[= 1$  out] and  $[\geq 1$  in] properties, which means it is a total, surjective function. But it does not have the  $[\leq 1$  in] property because element 3 has two arrows going into it; it is not injective.

The relation on the right has the  $[= 1$  out] and  $[\leq 1$  in] properties, which means it is a total, injective function. But it does not have the  $[\geq 1$  in] property because element 4 has no arrow going into it; it is not surjective.

The arrows in a diagram for  $R$  correspond, of course, exactly to the pairs in the graph of  $R$ . Notice that the arrows alone are not enough to determine, for example, if  $R$  has the  $[\geq 1$  out], total, property. If all we knew were the arrows, we wouldn't know about any points in the domain column that had no arrows out. In other words,  $\operatorname{graph}(R)$  alone does not determine whether  $R$  is total: we also need to know what  $\operatorname{domain}(R)$  is.


Example 4.4.3. The function defined by the formula $1 / x^2$ has the $[\geq 1$ out] property if its domain is $\mathbb{R}^+$, but not if its domain is some set of real numbers including 0. It has the $[\equiv 1$ in] and $[\equiv 1$ out] property if its domain and codomain are both $\mathbb{R}^+$, but it has neither the $[\leq 1$ in] nor the $[\geq 1$ out] property if its domain and codomain are both $\mathbb{R}$.

### 4.4.2 Relational Images

The idea of the image of a set under a function extends directly to relations.

**Definition 4.4.4.** The image of a set, $Y$, under a relation, $R$, written $R(Y)$, is the set of elements of the codomain, $B$, of $R$ that are related to some element in $Y$. In terms of the relation diagram, $R(Y)$ is the set of points with an arrow coming in that starts from some point in $Y$.

For example, the set of subject numbers that Meyer is in charge of in Spring '10 is exactly $Chrg$(A. Meyer). To figure out what this is, we look for all the arrows in the $Chrg$ diagram that start at "A. Meyer," and see which subject-numbers are at the other end of these arrows. Looking at the list (4.4) of pairs in graph($Chrg$), we see that these subject-numbers are $\{6.042, 18.062, 6.844\}$. Similarly, to find the subject numbers that either Freeman or Eng are in charge of, we can collect all the arrows that start at either "G. Freeman," or "T. Eng" and, again, see which subject-numbers are at the other end of these arrows. This is $Chrg(\{\mathrm{G.~{}Freeman,T.~{}Eng}\})$. Looking again at the list (4.4), we see that

$$
Chrg(\{\mathrm{G.~{}Freeman,T.~{}Eng}\}) = \{6.011, 6.881, 6.882, 6.UAT\}
$$

Finally, Fac is the set of all in-charge instructors, so $Chrg(\mathrm{Fac})$ is the set of all the subjects listed for Spring '10.

## Inverse Relations and Images

**Definition 4.4.5.** The inverse, $R^{-1}$ of a relation $R: A \to B$ is the relation from $B$ to $A$ defined by the rule

$$
b R^{-1} a \quad \text{IFF} \quad a R b.
$$

In other words, $R^{-1}$ is the relation you get by reversing the direction of the arrows in the diagram of $R$.

**Definition 4.4.6.** The image of a set under the relation, $R^{-1}$, is called the inverse image of the set. That is, the inverse image of a set, $X$, under the relation, $R$, is defined to be $R^{-1}(X)$.


4.5. Finite Cardinality

Continuing with the in-charge example above, the set of instructors in charge of 6.UAT in Spring '10 is exactly the inverse image of {6.UAT} under the Chrg relation. From the list (4.4), we see that Eng and Freeman are both in charge of 6.UAT, that is,

$$
\{\mathrm {T . E n g , D . F r e e m a n} \} \subseteq C h r g ^ {- 1} (\{6. U A T \}).
$$

We can't assert equality here because there may be additional pairs further down the list showing that additional instructors are co-incharge of 6.UAT.

Now let Intro be the set of introductory course 6 subject numbers. These are the subject numbers that start with "6.0." So the set of names of the instructors who were in-charge of introductory course 6 subjects in Spring '10, is  $Chrg^{-1}$  (Intro). From the part of the  $Chrg$  list shown in (4.4), we see that Meyer, Leighton, Freeman, and Guttag were among the instructors in charge of introductory subjects in Spring '10. That is,

$$
\{\text {M e y e r}, \text {L e i g h t o n}, \text {F r e e m a n}, \text {G u t t a g} \} \subseteq C h r g ^ {- 1} (\text {I n t r o}).
$$

Finally,  $Chrg^{-1}(\mathrm{SubNums})$ , is the set of all instructors who were in charge of a subject listed for Spring '10.

## 4.5 Finite Cardinality

A finite set is one that has only a finite number of elements. This number of elements is the "size" or cardinality of the set:

**Definition 4.5.1.** If  $A$  is a finite set, the cardinality of  $A$ , written  $|A|$ , is the number of elements in  $A$ .

A finite set may have no elements (the empty set), or one element, or two elements,..., so the cardinality of finite sets is always a nonnegative integer.

Now suppose  $R: A \to B$  is a function. This means that every element of  $A$  contributes at most one arrow to the diagram for  $R$ , so the number of arrows is at most the number of elements in  $A$ . That is, if  $R$  is a function, then

$$
| A | \geq \# \text {a r r o w s}.
$$

If  $R$  is also surjective, then every element of  $B$  has an arrow into it, so there must be at least as many arrows in the diagram as the size of  $B$ . That is,

$$
\# \text {a r r o w s} \geq | B |.
$$


Combining these inequalities implies that if $R$ is a surjective function, then $|A| \geq |B|$.

In short, if we write $A$ surj $B$ to mean that there is a surjective function from $A$ to $B$, then we've just proved a lemma: if $A$ surj $B$ for finite sets $A, B$, then $|A| \geq |B|$. The following definition and lemma lists this statement and three similar rules relating domain and codomain size to relational properties.

**Definition 4.5.2.** Let $A, B$ be (not necessarily finite) sets. Then

1. $A$ surj $B$ iff there is a surjective function from $A$ to $B$.
2. $A$ inj $B$ iff there is an injective total relation from $A$ to $B$.
3. $A$ bij $B$ iff there is a bijection from $A$ to $B$.

**Lemma 4.5.3.** For finite sets $A, B$:

1. If $A$ surj $B$, then $|A| \geq |B|$.
2. If $A$ inj $B$, then $|A| \leq |B|$.
3. If $A$ bij $B$, then $|A| = |B|$.

**Proof.** We've already given an "arrow" proof of implication 1. Implication 2. follows immediately from the fact that if $R$ has the $[\leq 1$ out], function property, and the $[\geq 1$ in], surjective property, then $R^{-1}$ is total and injective, so $A$ surj $B$ iff $B$ inj $A$. Finally, since a bijection is both a surjective function and a total injective relation, implication 3. is an immediate consequence of the first two.

Lemma 4.5.3.1. has a converse: if the size of a finite set, $A$, is greater than or equal to the size of another finite set, $B$, then it's always possible to define a surjective function from $A$ to $B$. In fact, the surjection can be a total function. To see how this works, suppose for example that

$$
\begin{array}{l}
A = \{a_0, a_1, a_2, a_3, a_4, a_5\} \\
B = \{b_0, b_1, b_2, b_3\}.
\end{array}
$$

Then define a total function $f: A \to B$ by the rules

$$
f(a_0) ::= b_0, \quad f(a_1) ::= b_1, \quad f(a_2) ::= b_2, \quad f(a_3) = f(a_4) = f(a_5) ::= b_3.
$$

More concisely,

$$
f(a_i) ::= b_{\min(i, 3)},
$$


4.5. Finite Cardinality

for $0 \leq i \leq 5$. Since $5 \geq 3$, this $f$ is a surjection.

So we have figured out that if $A$ and $B$ are finite sets, then $|A| \geq |B|$ if and only if $A$ surj $B$. All told, this argument wraps up the proof of a theorem that summarizes the whole finite cardinality story:

Theorem 4.5.4. [Mapping Rules] For finite sets, $A, B$,

$$
| A | \geq | B | \quad \text{iff} \quad A \text{ surj } B, \tag{4.5}
$$

$$
| A | \leq | B | \quad \text{iff} \quad A \text{ inj } B, \tag{4.6}
$$

$$
| A | = | B | \quad \text{iff} \quad A \text{ bij } B, \tag{4.7}
$$

### 4.5.1 How Many Subsets of a Finite Set?

As an application of the bijection mapping rule (4.7), we can give an easy proof of:

Theorem 4.5.5. There are $2^n$ subsets of an $n$-element set. That is,

$$
| A | = n \quad \text{implies} \quad |\operatorname{pow}(A)| = 2^n.
$$

For example, the three-element set $\{a_1, a_2, a_3\}$ has eight different subsets:

$$
\begin{array}{c c c c c}
\emptyset & \{a_1\} & \{a_2\} & \{a_1, a_2\} \\
\{a_3\} & \{a_1, a_3\} & \{a_2, a_3\} & \{a_1, a_2, a_3\}
\end{array}
$$

Theorem 4.5.5 follows from the fact that there is a simple bijection from subsets of $A$ to $\{0,1\}^n$, the $n$-bit sequences. Namely, let $a_1, a_2, \ldots, a_n$ be the elements of $A$. The bijection maps each subset of $S \subseteq A$ to the bit sequence $(b_1, \ldots, b_n)$ defined by the rule that

$$
b_i = 1 \quad \text{iff} \quad a_i \in S.
$$

For example, if $n = 10$, then the subset $\{a_2, a_3, a_5, a_7, a_{10}\}$ maps to a 10-bit sequence as follows:

$$
\begin{array}{c}
\text{subset:} \quad \{ \quad a_2, \quad a_3, \quad \quad a_5, \quad \quad a_7, \quad \quad \quad a_{10} \} \\
\text{sequence:} \quad ( \quad 0, \quad 1, \quad 1, \quad 0, \quad 1, \quad 0, \quad 1, \quad 0, \quad 0, \quad 1 \)
\end{array}
$$

Now by bijection case of the Mapping Rules 4.5.4.(4.7),

$$
|\operatorname{pow}(A)| = |\{0, 1\}^n|.
$$

But every computer scientist knows$^6$ that there are $2^n$ $n$-bit sequences! So we've proved Theorem 4.5.5!

$^6$In case you're someone who doesn't know how many $n$-bit sequences there are, you'll find the $2^n$ explained in Section 14.2.2.
