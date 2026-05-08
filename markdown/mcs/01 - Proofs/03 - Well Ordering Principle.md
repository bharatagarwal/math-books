## 2 The Well Ordering Principle

Every nonempty set of nonnegative integers has a smallest element.

This statement is known as The Well Ordering Principle. Do you believe it? Seems sort of obvious, right? But notice how tight it is: it requires a nonempty set—it's false for the empty set which has no smallest element because it has no elements at all. And it requires a set of nonnegative integers—it's false for the set of negative integers and also false for some sets of nonnegative rationals—for example, the set of positive rationals. So, the Well Ordering Principle captures something special about the nonnegative integers.

While the Well Ordering Principle may seem obvious, it's hard to see offhand why it is useful. But in fact, it provides one of the most important proof rules in discrete mathematics. In this chapter, we'll illustrate the power of this proof method with a few simple examples.

## 2.1 Well Ordering Proofs

We actually have already taken the Well Ordering Principle for granted in proving that $\sqrt{2}$ is irrational. That proof assumed that for any positive integers $m$ and $n$, the fraction $m/n$ can be written in lowest terms, that is, in the form $m'/n'$ where $m'$ and $n'$ are positive integers with no common prime factors. How do we know this is always possible?

Suppose to the contrary that there are positive integers $m$ and $n$ such that the fraction $m/n$ cannot be written in lowest terms. Now let $C$ be the set of positive integers that are numerators of such fractions. Then $m \in C$, so $C$ is nonempty. Therefore, by Well Ordering, there must be a smallest integer, $m_0 \in C$. So by definition of $C$, there is an integer $n_0 > 0$ such that

the fraction $\frac{m_0}{n_0}$ cannot be written in lowest terms.

This means that $m_0$ and $n_0$ must have a common prime factor, $p > 1$. But

$$
\frac{m_0/p}{n_0/p} = \frac{m_0}{n_0}.
$$


so any way of expressing the left hand fraction in lowest terms would also work for $m_0 / n_0$, which implies

the fraction $\frac{m_0 / p}{n_0 / p}$ cannot be in written in lowest terms either.

So by definition of $C$, the numerator, $m_0 / p$, is in $C$. But $m_0 / p < m_0$, which contradicts the fact that $m_0$ is the smallest element of $C$.

Since the assumption that $C$ is nonempty leads to a contradiction, it follows that $C$ must be empty. That is, that there are no numerators of fractions that can't be written in lowest terms, and hence there are no such fractions at all.

We've been using the Well Ordering Principle on the sly from early on!

## 2.2 Template for Well Ordering Proofs

More generally, there is a standard way to use Well Ordering to prove that some property, $P(n)$ holds for every nonnegative integer, $n$. Here is a standard way to organize such a well ordering proof:

To prove that “$P(n)$ is true for all $n \in \mathbb{N}$” using the Well Ordering Principle:

- Define the set, $C$, of counterexamples to $P$ being true. Specifically, define

$$
C ::= \{n \in \mathbb{N} \mid \operatorname{NOT}(P(n)) \text{ is true}\}.
$$

(The notation $\{n \mid Q(n)\}$ means “the set of all elements $n$ for which $Q(n)$ is true.” See Section 4.1.4.)

- Assume for proof by contradiction that $C$ is nonempty.
- By the Well Ordering Principle, there will be a smallest element, $n$, in $C$.
- Reach a contradiction somehow—often by showing that $P(n)$ is actually true or by showing that there is another member of $C$ that is smaller than $n$. This is the open-ended part of the proof task.
- Conclude that $C$ must be empty, that is, no counterexamples exist.

### 2.2.1 Summing the Integers

Let's use this template to prove


## Theorem 2.2.1.

$$
1 + 2 + 3 + \cdots + n = n(n + 1)/2 \tag{2.1}
$$

for all nonnegative integers, $n$.

First, we'd better address a couple of ambiguous special cases before they trip us up:

- If $n = 1$, then there is only one term in the summation, and so $1 + 2 + 3 + \cdots + n$ is just the term 1. Don't be misled by the appearance of 2 and 3 or by the suggestion that 1 and $n$ are distinct terms!
- If $n = 0$, then there are no terms at all in the summation. By convention, the sum in this case is 0.

So, while the three dots notation, which is called an ellipsis, is convenient, you have to watch out for these special cases where the notation is misleading. In fact, whenever you see an ellipsis, you should be on the lookout to be sure you understand the pattern, watching out for the beginning and the end.

We could have eliminated the need for guessing by rewriting the left side of (2.1) with summation notation:

$$
\sum_{i=1}^{n} i \quad \text{or} \quad \sum_{1 \leq i \leq n} i.
$$

Both of these expressions denote the sum of all values taken by the expression to the right of the sigma as the variable, $i$, ranges from 1 to $n$. Both expressions make it clear what (2.1) means when $n = 1$. The second expression makes it clear that when $n = 0$, there are no terms in the sum, though you still have to know the convention that a sum of no numbers equals 0 (the product of no numbers is 1, by the way).

OK, back to the proof:

Proof. By contradiction. Assume that Theorem 2.2.1 is false. Then, some nonnegative integers serve as counterexamples to it. Let's collect them in a set:

$$
C ::= \{n \in \mathbb{N} \mid 1 + 2 + 3 + \cdots + n \neq \frac{n(n + 1)}{2} \}.
$$

Assuming there are counterexamples, $C$ is a nonempty set of nonnegative integers. So, by the Well Ordering Principle, $C$ has a minimum element, which we'll call $c$. That is, among the nonnegative integers, $c$ is the smallest counterexample to equation (2.1).


Since $c$ is the smallest counterexample, we know that (2.1) is false for $n = c$ but true for all nonnegative integers $n < c$. But (2.1) is true for $n = 0$, so $c > 0$. This means $c - 1$ is a nonnegative integer, and since it is less than $c$, equation (2.1) is true for $c - 1$. That is,

$$
1 + 2 + 3 + \cdots + (c - 1) = \frac{(c - 1)c}{2}.
$$

But then, adding $c$ to both sides, we get

$$
1 + 2 + 3 + \cdots + (c - 1) + c = \frac{(c - 1)c}{2} + c = \frac{c^2 - c + 2c}{2} = \frac{c(c + 1)}{2},
$$

which means that (2.1) does hold for $c$, after all! This is a contradiction, and we are done.

## 2.3 Factoring into Primes

We've previously taken for granted the Prime Factorization Theorem, also known as the Unique Factorization Theorem and the Fundamental Theorem of Arithmetic, which states that every integer greater than one has a unique¹ expression as a product of prime numbers. This is another of those familiar mathematical facts which are taken for granted but are not really obvious on closer inspection. We'll prove the uniqueness of prime factorization in a later chapter, but well ordering gives an easy proof that every integer greater than one can be expressed as some product of primes.

**Theorem 2.3.1.** Every positive integer greater than one can be factored as a product of primes.

**Proof.** The proof is by well ordering.

Let $C$ be the set of all integers greater than one that cannot be factored as a product of primes. We assume $C$ is not empty and derive a contradiction.

If $C$ is not empty, there is a least element, $n \in C$, by well ordering. The $n$ can't be prime, because a prime by itself is considered a (length one) product of primes and no such products are in $C$.

So $n$ must be a product of two integers $a$ and $b$ where $1 < a, b < n$. Since $a$ and $b$ are smaller than the smallest element in $C$, we know that $a, b \notin C$. In other words, $a$ can be written as a product of primes $p_1p_2\cdots p_k$ and $b$ as a product of

¹…unique up to the order in which the prime factors appear


## 2.4 Well Ordered Sets


primes $q_1 \cdots q_l$. Therefore, $n = p_1 \cdots p_k q_1 \cdots q_l$ can be written as a product of primes, contradicting the claim that $n \in C$. Our assumption that $C$ is not empty must therefore be false.
