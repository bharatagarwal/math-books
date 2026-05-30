# Counting

*Bradfield session 1 · Monday 15 June · pre-work: LL chapters 2 & 4 ·
post-work: MCS chapter 15*

The course starts gently, by making sure we can count things *correctly* — and
Lovász (our **LL** text, the *Discrete Mathematics* book in this reader) starts
even more gently than that: with a birthday party. That choice is deliberate, and
worth imitating. Counting is the one part of mathematics where the objects are
concrete enough that, when in doubt, **you can build them and look.** That is
exactly the programmer's advantage, and the spine of this chapter: we will
*discover* each rule by enumerating small cases, *then* state it as a theorem,
*then* verify the closed form against a brute-force count. Intuition first,
formula second, machine-checked proof third.

Why does an engineer need this? Because the moment you ask "how many states can
this protocol be in," "how many distinct cache keys are there," or "how many keys
must an attacker try," you are counting a set you've described *indirectly* — you
know the rule that generates its elements and you want $|S|$ without listing them.
Get the reasoning subtly wrong (off by a factor of $k!$ is the classic) and every
downstream estimate is wrong with it.

## Lovász's party: three principles hiding in a conversation

In LL §2.1, Alice's guests stumble onto the whole toolkit just by talking. It is
worth following their dialogue, because each turn is one of the three counting
principles.

**The handshakes — the division principle.** Seven people shake hands; each
shakes six, so Carl says $7 \cdot 6 = 42$. Diane objects: two people give *one*
handshake, not two. Eve resolves it — every handshake was counted *twice* (once
from each end), so the answer is $42 / 2 = 21$. That "count a convenient
over-count, then divide by the symmetry" move is the **division principle**, and
it is the single most common counting idea in the chapter.

**The seating — the product rule.** With Alice's chair fixed, the chair to her
right can hold any of $6$ guests; *whoever* sits there, the next chair has $5$
choices, then $4$, and so on: $6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720$
seatings. A sequence of independent choices *multiplies*. This is the **product
rule**.

**The lottery and bridge — combinations as "product over symmetry."** To cover
every 5-from-90 lottery ticket, George reasons $90 \cdot 89 \cdot 88 \cdot 87
\cdot 86$ — but Alice catches the bug: that counts *ordered* picks, and a ticket
doesn't care about order. Each ticket of $5$ numbers was counted $5! = 120$ times,
so the real count is $\frac{90 \cdot 89 \cdot 88 \cdot 87 \cdot 86}{5!} =
43{,}949{,}268$. The same reasoning gives the number of bridge hands,
$\frac{52 \cdot 51 \cdots 40}{13!} = 635{,}013{,}559{,}600$. Counting handshakes
and counting lottery tickets are *the same problem* — division by the order you
don't care about.

These are too large to list, but the closed forms are exactly checkable. The
verification confirms both of the book's figures with arbitrary-precision
integers:

```python
<!-- include: code/bradfield/01-counting/01_rules.py -->
```

The party's *small* counts we don't even need a formula for — we can build the
objects and count them. Enumerating every seating (with Alice fixed), every
2-subset (the handshakes), and every way to split six players into pairs across
indistinguishable chess boards reproduces $720$, $21$, and Bob's $15$ matchings
directly:

```python
<!-- include: code/bradfield/01-counting/02_perms_combs.py -->
```

## How many subsets? Discover the doubling, then prove it twice

LL §2.3 asks the first genuinely general question: how many subsets does an
$n$-element set have? Lovász's method — and ours — is to *try small numbers
first.* The empty set has $1$ subset; $\{a\}$ has $2$; $\{a,b\}$ has $4$;
$\{a,b,c\}$ has $8$. Rather than assume the pattern, let's **build the powersets
and watch the count**, then see the mechanism: adding one new element takes every
old subset and offers it twice — "without the new element" and "with it" — so the
count *doubles* at each step.

```python
<!-- include: code/bradfield/01-counting/06_discover_doubling.py -->
```

That doubling is the first proof: $n$ independent in/out decisions, $2^n$
outcomes (LL's decision-tree argument, his Figure 1). **Theorem (LL 2.1):** *a set
with $n$ elements has $2^n$ subsets.*

Lovász then gives a *second* proof, and explains why a second proof is worth
having: "every proof reveals much more than the bare fact." His second argument
is a **bijection** — encode each subset of $\{a,b,c\}$ as a $3$-bit string (1 =
in, 0 = out). The subsets then *are* the numbers $0$ through $2^n - 1$. Seeing the
correspondence laid out is the real "aha," and it introduces the bijection rule we
will lean on constantly: *if you can match two sets one-to-one, they have the same
size.*

```python
<!-- include: code/bradfield/01-counting/07_subset_binary_bijection.py -->
```

## Sequences: the product rule in general

LL §2.4 generalizes the binary encoding: how many strings of length $n$ are there
over an alphabet of $k$ symbols? Each position is an independent choice of one of
$k$, so by the product rule it is $k^n$ (LL Theorem 2.2). And the choices need not
all be the *same* size — a database record with fields of sizes $k_1, k_2, \dots,
k_n$ admits $k_1 k_2 \cdots k_n$ records (LL Theorem 2.3). The bijection demo
above is exactly the $k=2$ case: bit-strings of length $n$, hence $2^n$ subsets.

## Permutations and combinations: order, and dividing it out

The seating problem, generalized (LL §2.5), is the number of **permutations** of
$n$ objects: $n!$. Recording only the first $k$ places of a race (LL §4.1) gives
the **falling factorial**, the number of *ordered* $k$-subsets:
$$P(n,k) = n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!}.$$

Now apply the division principle. An *unordered* $k$-subset can be ordered in $k!$
ways, so we have over-counted by exactly $k!$ (LL §4.2). Dividing gives the
**binomial coefficient** — "$n$ choose $k$":
$$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!}{k!\,(n-k)!}.$$

This is the lottery/bridge reasoning made general, and the most common source of
off-by-a-factorial bugs: *does order matter?* If yes, stop at $P(n,k)$; if no,
divide by $k!$. The `02` demo above already checks both the falling-factorial and
the identity $P(n,k) = \binom{n}{k}\,k!$ by enumeration.

## Pascal's triangle and the binomial theorem

Arrange the $\binom{n}{k}$ in a triangle and patterns leap out *before* you prove
anything. Let's print it and let the eye find them, then attach a counting story
to each:

```python
<!-- include: code/bradfield/01-counting/08_pascal_explore.py -->
```

Three of those patterns are the identities worth knowing by reflex:

- **Symmetry** $\binom{n}{k} = \binom{n}{n-k}$ — choosing what to *include* is the
  same as choosing what to *leave out* (LL exercise 4.9).
- **Pascal's rule** $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ — fix one
  element; your subset either contains it or doesn't. This recurrence *builds* the
  triangle (LL exercise 4.8).
- **Row sums** $\sum_k \binom{n}{k} = 2^n$ — every subset, sorted by size; the
  subset count yet again (LL exercise 4.10).

The reason these are called *binomial* coefficients is LL §4.3's **Binomial
Theorem**: expanding $(x+y)^n = (x+y)(x+y)\cdots(x+y)$, a term $x^k y^{n-k}$ arises
once for each way to pick the $x$ from $k$ of the $n$ factors — and there are
$\binom{n}{k}$ such ways. Hence
$$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k}\,x^k y^{n-k}.$$
Setting $x=y=1$ recovers $2^n$; setting $x=1, y=-1$ gives $0$ (equally many
even- and odd-sized subsets). We verify the expansion and these specializations
symbolically:

```python
<!-- include: code/bradfield/01-counting/03_binomial.py -->
```

## Multinomials and stars-and-bars

LL §4.4–4.6 push the division principle two steps further, and these are the
shapes that show up most in practice:

- **Distributing distinguishable presents / anagrams (the multinomial).** The
  number of ways to split $n$ distinct items into groups of prescribed sizes
  $n_1, \dots, n_k$ — equivalently, the distinct rearrangements of a word with
  those letter-multiplicities — is $\dfrac{n!}{n_1!\,n_2!\cdots n_k!}$. It is the
  division principle again: $n!$ orderings, divided by the $n_i!$ orderings
  *within* each indistinguishable group.
- **Distributing identical pennies (stars and bars).** The number of ways to write
  $n$ as an *ordered* sum of $k$ non-negative integers — equivalently, to drop $n$
  identical balls into $k$ distinct boxes — is $\binom{n+k-1}{k-1}$ (LL Theorem
  4.5). This is the shape of "split $n$ units of budget across $k$ buckets," and it
  is genuinely surprising that binomial coefficients answer it.

## Inclusion–exclusion: counting "at least one"

The sum rule needs *disjoint* cases. When cases overlap, correct for the
double-counting (LL exercise 2.19 proves the two-set version $|A \cup B| = |A| +
|B| - |A \cap B|$). For three sets the corrections alternate — add singles,
subtract pairs, add the triple — and the pattern continues. This is how you count
sets defined by "satisfies at least one property," and, by complement, "satisfies
none" — the shape of "how many inputs miss every cache," "how many integers are
divisible by none of these primes." We check it against a literal count over a
universe of a thousand integers:

```python
<!-- include: code/bradfield/01-counting/04_inclusion_exclusion.py -->
```

## The pigeonhole principle

The simplest counting argument, and the one that feels like magic: **if $n+1$
pigeons occupy $n$ holes, some hole holds at least two** — you cannot inject a
bigger set into a smaller one. All the art is in *choosing the holes*. From any
six numbers in $\{1,\dots,10\}$, two must sum to $11$: the five pairs
$\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$ are the holes, and six picks can't avoid
filling one twice. We verify it the way an engineer should — over *every*
six-element subset — and confirm it is tight (five numbers can dodge it):

```python
<!-- include: code/bradfield/01-counting/05_pigeonhole.py -->
```

## Working the problem set (MCS Chapter 15)

The post-class problems live in MCS chapter 15, which packages the same ideas as a
small set of named rules — worth keeping as a checklist:

- **Bijection rule.** $|A| = |B|$ when a bijection exists — count the hard set via
  an easy one (subsets $\leftrightarrow$ bit-strings was our first use).
- **Sum / product rules.** Disjoint cases add; independent choices multiply.
- **Generalized product & "subset" rules.** Functions $k\!\to\!n$: $n^k$;
  injections: $P(n,k)$; subsets of an $n$-set: $2^n$.
- **Division rule.** If a map is exactly $k$-to-$1$, the image has $|A|/k$
  elements — the handshake/lottery move, and the source of $\binom{n}{k}$ and the
  multinomial.
- **Bookkeeper rule (multinomial)** and **stars-and-bars**, as above.

Almost every counting problem in practice is one of these wearing a costume, plus
the constant discipline of *checking the small case by enumeration.* The deeper
treatment, with full exercises, is LL chapters 2 & 4 (the **Discrete
Mathematics** book here) and MCS chapters 14–16; for the set-theory underpinnings
the syllabus recommends Halmos's very short *Naïve Set Theory*. The next session
turns counting into **probability** — counting with a denominator.
