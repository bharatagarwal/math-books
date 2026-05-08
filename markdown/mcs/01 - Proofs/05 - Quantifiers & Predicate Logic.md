## 3.6 Predicate Formulas

### 3.6.1 Quantifiers

The “for all” notation, $\forall$, has already made an early appearance in Section 1.1. For example, the predicate

$$
“x^2 \geq 0”
$$


is always true when $x$ is a real number. That is,

$$
\forall x \in \mathbb{R}. x^2 \geq 0
$$

is a true statement. On the other hand, the predicate

$$
“5x^2 - 7 = 0”
$$

is only sometimes true; specifically, when $x = \pm \sqrt{7/5}$. There is a “there exists” notation, $\exists$, to indicate that a predicate is true for at least one, but not necessarily all objects. So

$$
\exists x \in \mathbb{R}. 5x^2 - 7 = 0
$$

is true, while

$$
\forall x \in \mathbb{R}. 5x^2 - 7 = 0
$$

is not true.

There are several ways to express the notions of “always true” and “sometimes true” in English. The table below gives some general formats on the left and specific examples using those formats on the right. You can expect to see such phrases hundreds of times in mathematical writing!

## Always True

For all $x \in D$, $P(x)$ is true.

For all $x \in \mathbb{R}$, $x^2 \geq 0$.

$P(x)$ is true for every $x$ in the set, $D$.

$x^2 \geq 0$ for every $x \in \mathbb{R}$.

## Sometimes True

There is an $x \in D$ such that $P(x)$ is true.

There is an $x \in \mathbb{R}$ such that $5x^2 - 7 = 0$.

$P(x)$ is true for some $x$ in the set, $D$.

$5x^2 - 7 = 0$ for some $x \in \mathbb{R}$.

$P(x)$ is true for at least one $x \in D$.

$5x^2 - 7 = 0$ for at least one $x \in \mathbb{R}$.

All these sentences “quantify” how often the predicate is true. Specifically, an assertion that a predicate is always true is called a universal quantification, and an assertion that a predicate is sometimes true is an existential quantification. Sometimes the English sentences are unclear with respect to quantification:

If you can solve any problem we come up with,

then you get an $A$ for the course. (3.16)

The phrase “you can solve any problem we can come up with” could reasonably be interpreted as either a universal or existential quantification:

you can solve every problem we come up with, (3.17)


or maybe

$$
\text{you can solve at least one problem we come up with.} \tag{3.18}
$$

To be precise, let Probs be the set of problems we come up with, $\text{Solves}(x)$ be the predicate "You can solve problem $x$," and $G$ be the proposition, "You get an $A$ for the course." Then the two different interpretations of (3.16) can be written as follows:

$$
(\forall x \in \text{Probs. Solves}(x)) \text{ IMPLIES } G, \quad \text{for (3.17)},
$$

$$
(\exists x \in \text{Probs. Solves}(x)) \text{ IMPLIES } G. \quad \text{for (3.18)}.
$$

### 3.6.2 Mixing Quantifiers

Many mathematical statements involve several quantifiers. For example, we already described

Goldbach's Conjecture 1.1.8: Every even integer greater than 2 is the sum of two primes.

Let's write this out in more detail to be precise about the quantification:

For every even integer $n$ greater than 2, there exist primes $p$ and $q$ such that $n = p + q$.

Let Evens be the set of even integers greater than 2, and let Primes be the set of primes. Then we can write Goldbach's Conjecture in logic notation as follows:

$$
\underbrace{\forall n \in \text{Evens}}_{\text{for every even integer } n > 2} \underbrace{\exists p \in \text{Primes} \exists q \in \text{Primes}}_{ \text{there exist primes } p \text{ and } q \text{ such that}} n = p + q.
$$

### 3.6.3 Order of Quantifiers

Swapping the order of different kinds of quantifiers (existential or universal) usually changes the meaning of a proposition. For example, let's return to one of our initial, confusing statements:

"Every American has a dream."

This sentence is ambiguous because the order of quantifiers is unclear. Let $A$ be the set of Americans, let $D$ be the set of dreams, and define the predicate $H(a, d)$ to be "American $a$ has dream $d$." Now the sentence could mean there is a single dream that every American shares—such as the dream of owning their own home:

$$
\exists d \in D \ \forall a \in A. \ H(a, d)
$$


3.6. Predicate Formulas


Or it could mean that every American has a personal dream:

$$
\forall a \in A \exists d \in D. H(a, d)
$$

For example, some Americans may dream of a peaceful retirement, while others dream of continuing practicing their profession as long as they live, and still others may dream of being so rich they needn't think about work at all.

Swapping quantifiers in Goldbach's Conjecture creates a patently false statement that every even number $\geq 2$ is the sum of the same two primes:

$$
\underbrace{\exists p \in \text{Primes} \ \exists q \in \text{Primes.}}_{\text{there exist primes} \ p \text{ and } q \text{ such that}} \underbrace{\forall n \in \text{Evens} \ n = p + q}_{\text{for every even integer } n > 2}.
$$

### 3.6.4 Variables Over One Domain

When all the variables in a formula are understood to take values from the same nonempty set, $D$, it's conventional to omit mention of $D$. For example, instead of $\forall x \in D \ \exists y \in D. Q(x, y)$ we'd write $\forall x \exists y. Q(x, y)$. The unnamed nonempty set that $x$ and $y$ range over is called the domain of discourse, or just plain domain, of the formula.

It's easy to arrange for all the variables to range over one domain. For example, Goldbach's Conjecture could be expressed with all variables ranging over the domain $\mathbb{N}$ as

$$
\forall n. n \in \text{Evens IMPLIES} \ (\exists p \ \exists q. p \in \text{Primes} \ \text{AND} \ q \in \text{Primes} \ \text{AND} \ n = p + q).
$$

### 3.6.5 Negating Quantifiers

There is a simple relationship between the two kinds of quantifiers. The following two sentences mean the same thing:

Not everyone likes ice cream.

There is someone who does not like ice cream.

The equivalence of these sentences is a instance of a general equivalence that holds between predicate formulas:

$$
\operatorname{NOT}(\forall x. P(x)) \quad \text{is equivalent to} \quad \exists x. \operatorname{NOT}(P(x)). \tag{3.19}
$$

Similarly, these sentences mean the same thing:

There is no one who likes being mocked.

Everyone dislikes being mocked.


The corresponding predicate formula equivalence is

$$
\operatorname {N O T} \left(\exists x. P (x)\right) \quad \text {is equivalent to} \quad \forall x. \operatorname {N O T} (P (x)). \tag {3.20}
$$

The general principle is that moving a NOT across a quantifier changes the kind of quantifier. Note that (3.20) follows from negating both sides of (3.19).

### 3.6.6 Validity for Predicate Formulas

The idea of validity extends to predicate formulas, but to be valid, a formula now must evaluate to true no matter what the domain of discourse may be, no matter what values its variables may take over the domain, and no matter what interpretations its predicate variables may be given. For example, the equivalence (3.19) that gives the rule for negating a universal quantifier means that the following formula is valid:

$$
\operatorname {N O T} (\forall x. P (x)) \text {I F F} \exists x. \operatorname {N O T} (P (x)). \tag {3.21}
$$

Another useful example of a valid assertion is

$$
\exists x \forall y. P (x, y) \text {I M P L I E S} \forall y \exists x. P (x, y). \tag {3.22}
$$

Here's an explanation why this is valid:

Let  $D$  be the domain for the variables and  $P_0$  be some binary predicate² on  $D$ . We need to show that if

$$
\exists x \in D. \forall y \in D. P _ {0} (x, y) \tag {3.23}
$$

holds under this interpretation, then so does

$$
\forall y \in D \exists x \in D. P _ {0} (x, y). \tag {3.24}
$$

So suppose (3.23) is true. Then by definition of  $\exists$ , this means that some element  $d_0 \in D$  has the property that

$$
\forall y \in D. P _ {0} (d _ {0}, y).
$$

By definition of  $\forall$ , this means that

$$
P _ {0} (d _ {0}, d)
$$

is true for all  $d \in D$ . So given any  $d \in D$ , there is an element in  $D$ , namely,  $d_0$ , such that  $P_0(d_0, d)$  is true. But that's exactly what (3.24) means, so we've proved that (3.24) holds under this interpretation, as required.

²That is, a predicate that depends on two variables.


## 3.7 References

We hope this is helpful as an explanation, but we don't really want to call it a "proof." The problem is that with something as basic as (3.22), it's hard to see what more elementary axioms are ok to use in proving it. What the explanation above did was translate the logical formula (3.22) into English and then appeal to the meaning, in English, of "for all" and "there exists" as justification.

In contrast to (3.22), the formula

$$
\forall y \exists x. P (x, y) \text{ IMPLIES } \exists x \forall y. P (x, y). \tag{3.25}
$$

is not valid. We can prove this just by describing an interpretation where the hypothesis, $\forall y\exists x. P(x,y)$, is true but the conclusion, $\exists x\forall y. P(x,y)$, is not true. For example, let the domain be the integers and $P(x,y)$ mean $x > y$. Then the hypothesis would be true because, given a value, $n$, for $y$ we could choose the value of $x$ to be $n + 1$, for example. But under this interpretation the conclusion asserts that there is an integer that is bigger than all integers, which is certainly false. An interpretation like this that falsifies an assertion is called a counter model to that assertion.
