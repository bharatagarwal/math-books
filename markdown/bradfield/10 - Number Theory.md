# Number Theory

*Bradfield session 10 · Thursday 16 July · pre-work: LL chapter 8*

Number theory is, as Lovász (our **LL** text, the *Discrete Mathematics* book in
this reader) opens LL ch 8 by saying, "a truly venerable field" — 2500 years old,
and *still* full of simple questions nobody can answer. G. H. Hardy prized it
precisely because it seemed useless; it then turned out to be the bedrock of
modern cryptography. That is not a coincidence this chapter glosses over — it is
the spine of it. LL ch 8 deliberately builds the number theory the *next* session
needs for public-key crypto, and we follow that exact arc: divisibility, primes
and unique factorization, the infinitude of primes, the Euclidean algorithm and
Bézout, congruences, and Fermat's Little Theorem. The chapter on cryptography is
the payoff; everything here is a prerequisite assembled in order.

Number theory is also where the programmer's advantage is sharpest: every object
is an integer, so when a theorem feels abstract we can **build the integers and
look** — print the factorizations, trace the algorithm, tabulate the residues —
*before* we trust the closed form. Discovery first, theorem second, exhaustive
check third, exactly as in the Counting chapter.

## Divisibility, and division with remainder

LL §8.1 starts from the ground: $a \mid b$ ("$a$ divides $b$") means there is an
integer $m$ with $b = am$. When $a \nmid b$ (and $a > 0$) we can still **divide
with remainder** — the single most useful fact in the chapter — getting a unique
quotient $q$ and remainder $r$ with
$$b = aq + r, \qquad 0 \le r < a.$$
Everything downstream is built on this: the Euclidean algorithm is just repeated
division with remainder, and a congruence $a \equiv b \pmod n$ is the statement
that $a$ and $b$ leave the *same* remainder mod $n$. The basic divisibility laws
LL asks you to prove in exercise 8.3 — transitivity ($a\mid b$, $b\mid c
\Rightarrow a\mid c$) and linearity ($a\mid b$, $a\mid c \Rightarrow a \mid b\pm
c$) — are exactly the closure properties that make the later algorithms correct.

## Primes and the Fundamental Theorem

LL §8.2 defines a **prime** $p>1$ as one with no divisors other than $1$ and $p$
(equivalently, one that cannot be written as a product of two smaller positive
integers), and $1$ is neither prime nor composite. The Greeks already knew the two
deep facts: every integer factors into primes, and that factorization is
**unique** — LL's *Fundamental Theorem of Arithmetic* (Theorem 8.1).

Lovász's own advice is to try small numbers first, so before the theorem we
*discover* primes the way Eratosthenes did — cross out every multiple of each
survivor, and whatever is never crossed out is prime — and then build the
factorization of each small integer and *look* that it is forced and unique. The
demo runs the sieve, factors $2$ through $30$ and reconstructs each $n$ from its
prime powers, then uses the factorizations for LL's gcd recipe below:

```python
<!-- include: code/bradfield/10-number-theory/05_factor_explore.py -->
```

It prints the sieve's primes up to $50$, then lines like `12 = 2^2 * 3^1` and
`30 = 2^1 * 3^1 * 5^1` — each integer rebuilt exactly from one factorization,
which *is* Theorem 8.1 made concrete. (LL proves uniqueness by his elegant
"minimal criminal" descent: a smallest integer with two distinct factorizations
would force an even smaller one, a contradiction.) The same script also confirms
the **prime-power gcd recipe** of LL §8.6 — take the common primes at the *smaller*
exponent: from $300 = 2^2\cdot 3\cdot 5^2$ and $18 = 2\cdot 3^2$ it gets
$\gcd(300,18)=2\cdot 3 = 6$, the matching `lcm` $=900$ at the *larger* exponent,
and the identity $\gcd\cdot\operatorname{lcm} = ab$ (LL exercise 8.23). The book
prints $18 = 2\cdot 3^3$ in this example, a source typo; $2\cdot 3^2 = 18$, which
the code uses.

Unique factorization is not just bookkeeping — LL §8.3 turns it straight into a
proof that $\sqrt 2$ is irrational (Theorem 8.2): if $2b^2 = a^2$, the prime $2$
appears an *even* number of times on the right but an *odd* number on the left, and
unique factorization forbids that. The same engine — counting one prime's exponent
— powers much of the chapter.

## How many primes? Euclid's infinitude

LL §8.4 gives Euclid's theorem (Theorem 8.3): **there are infinitely many
primes.** The argument is a gem of indirect proof — for any $n$, consider $n! + 1$.
Any prime divisor $p$ of it must exceed $n$, because if $p \le n$ then $p \mid n!$
and $p \mid (n!+1)$, so $p \mid 1$ — impossible. Hence primes never run out. (LL
turns the same trick around in Theorem 8.4 to manufacture arbitrarily long runs of
*composite* numbers: $n!+2, \dots, n!+n$ are all composite, since $i \mid n!+i$.)
The reason crypto cares: it needs large primes to *exist* in abundance, and the
Prime Number Theorem (LL Theorem 8.5, $\pi(n)\sim n/\ln n$) says they do — about
one in every $2.3k$ of the $k$-digit numbers is prime.

## The Euclidean algorithm

The prime-power recipe for $\gcd$ is correct but useless at scale: factoring large
integers is hard (that hardness is what crypto is built on). LL §8.6 gives the way
out — **Euclid's algorithm**, "an important ingredient of almost all other
algorithms involving computation with integers." It needs no factorization, only
the observation (LL exercise 8.19) that
$$\gcd(a, b) = \gcd(b,\ a \bmod b),$$
applied until the remainder hits $0$. Rather than take the shrinkage on faith,
let's *trace* it and watch the pair collapse, reproducing LL's own worked chains:

```python
<!-- include: code/bradfield/10-number-theory/06_euclid_trace.py -->
```

The trace prints exactly the book's reductions —
`gcd(300,18) = gcd(18,12) = gcd(12,6) = 6` and the long Fibonacci chain
`gcd(89,55) = gcd(55,34) = ... = gcd(2,1) = 1` — so you can see each step replace
the larger number by a remainder. It then checks **Lemma 8.2** (the product of the
current pair at least *halves* every genuine reduction; on the $89,55$ chain the
products fall $4895 \to 1870 \to 714 \to \dots$), and from that lemma
**Theorem 8.7**: the number of steps never exceeds $\log_2 a + \log_2 b =
\log_2(ab)$. Sweeping every pair below $400$ (excluding only the degenerate
$a=b=1$, where the bound is $0$), the bound is never violated. Finally it shows
LL exercise 8.25's worst case directly: consecutive Fibonacci numbers force one
extra step each time, so $\gcd(F_{13}, F_{14}) = \gcd(233, 377)$ takes $12$ steps
— the algorithm is *longest* exactly on Fibonacci inputs.

Python's own `math.gcd` is the trusted oracle; this hand-written Euclid matches it
and ties $\gcd$ to $\operatorname{lcm}$ across a wide range:

```python
<!-- include: code/bradfield/10-number-theory/01_gcd.py -->
```

## Bézout's identity and modular inverses

LL §8.6 ends with the observation that makes Euclid pay off twice: *every* number
produced during the algorithm is an integer combination $am + bn$ of the inputs,
so in particular the gcd is. That is **Bézout's identity** (LL Theorem 8.8):
$$\gcd(a,b) = a x + b y \quad\text{for some integers } x, y,$$
and the **extended Euclidean algorithm** produces the witnesses $x, y$ by
back-substituting through the trace. This is not a curiosity — it is the key that
unlocks *division* in modular arithmetic. The **modular inverse** $a^{-1} \bmod n$
(the number you multiply by to "divide by $a$") **exists exactly when
$\gcd(a,n)=1$**, and Bézout hands it over: from $ax + ny = 1$ we read off
$ax \equiv 1 \pmod n$, so $x \bmod n$ is the inverse. Without this there is no RSA
decryption. The demo verifies $am+bn=g$ for every pair below $100$ and that the
Bézout inverse is correct for every coprime $(a,n)$:

```python
<!-- include: code/bradfield/10-number-theory/02_bezout.py -->
```

## Congruences and the two key theorems

A **congruence** $a \equiv b \pmod n$ means $n \mid (a-b)$ — equivalently, $a$ and
$b$ have the same remainder mod $n$ (LL's "clock arithmetic"). Addition and
multiplication respect congruence, which is what makes it computationally friendly:
you can reduce mod $n$ at *every* step and never let numbers explode. LL §8.7 leans
on this hard. To test $n \mid 2^{n-1}-1$ for a 100-digit $n$ you cannot form
$2^{n-1}$ (its digit count alone is astronomical); instead you compute it by
**square-and-multiply**, reducing mod $n$ after each squaring, in $O(\log e)$
multiplications and never exceeding $n^2$. The `power_mod` here is exactly LL's
"read the exponent in binary, square and occasionally multiply" recipe, and it
matches Python's built-in `pow(b, e, m)`.

The reason congruences matter for crypto is **Fermat's Little Theorem** (LL §8.5,
Theorem 8.6): for a prime $p$ and any integer $a$, $p \mid a^p - a$; equivalently,
when $p \nmid a$,
$$a^{p-1} \equiv 1 \pmod p.$$
LL proves it by induction on $a$ using the binomial expansion and Lemma 8.1 ($p
\mid \binom{p}{k}$ for $0<k<p$, straight from the Counting chapter). Before
trusting it, let's tabulate $a^{p-1} \bmod p$ and *see* the wall of $1$s appear for
primes and break for composites:

```python
<!-- include: code/bradfield/10-number-theory/07_fermat_table.py -->
```

Restricting to the $a$ coprime to $n$ (the only ones Fermat speaks about), the
table prints an all-$1$s row for *every* prime
(`n= 7 [PRIME, all 1s] a=[1, 2, 3, 4, 5, 6] -> [1, 1, 1, 1, 1, 1]`) and a row
that *breaks* for every composite — even $n=9$, whose row is
`[1, 4, 7, 7, 4, 1]`, has a $4$ and a $7$ giving it away. So on small numbers the
all-$1$s test looks like a perfect prime detector. The catch is that "row breaks
$\Rightarrow$ composite" is only the *contrapositive* of Fermat; the forward claim
"all $1$s $\Rightarrow$ prime" is false, and the script demonstrates exactly that,
following LL §8.7: $341 = 11\cdot 31$ is composite yet satisfies
$341 \mid 2^{340}-1$ (a base-$2$ *pseudoprime*, exposed because base $3$ gives
$3^{340}\equiv 56 \not\equiv 1 \pmod{341}$), and
$561 = 3\cdot 11\cdot 17$ is a **Carmichael number** — it passes for *every* base
$a$, so no choice of base rescues a Fermat-only test. (This is precisely why LL
then sketches Miller–Rabin, and why the cryptography session uses a probabilistic
primality test.)

The clean, *quantified* statements — square-and-multiply against `pow`, and Fermat
plus its generalization holding for all valid inputs — are checked exhaustively
here. The generalization is **Euler's Theorem**: if $\gcd(a,n)=1$ then
$a^{\varphi(n)} \equiv 1 \pmod n$, where **Euler's totient** $\varphi(n)$ counts
the integers in $1..n$ coprime to $n$. Euler's theorem (with $n = pq$) is what
guarantees RSA's "encrypt then decrypt" returns the original message:

```python
<!-- include: code/bradfield/10-number-theory/03_modular.py -->
```

## The Chinese Remainder Theorem

One more tool, built directly on Bézout's modular inverses: a system of
congruences with **pairwise coprime** moduli,
$$x \equiv r_1 \pmod{m_1},\quad \dots,\quad x \equiv r_k \pmod{m_k},$$
has a **unique** solution modulo $m_1 m_2 \cdots m_k$. The **Chinese Remainder
Theorem (CRT)** both proves this and constructs the solution. It is more than
elegant: it speeds up RSA decryption by roughly $4\times$ (work mod $p$ and mod $q$
separately, then recombine) and underlies secret-sharing. We solve the classic
system $x\equiv 2\,(3),\ x\equiv 3\,(5),\ x\equiv 2\,(7)$ and confirm by brute
force that $23$ is its *only* solution mod $105$:

```python
<!-- include: code/bradfield/10-number-theory/04_crt.py -->
```

## Where to go deeper

Unique factorization, Euclid/Bézout and modular inverses, congruences,
Fermat–Euler, and CRT are precisely the prerequisites for the next chapter, where
they assemble into RSA: pick two large primes $p, q$ (the infinitude and density of
primes guarantee they exist), let $n=pq$, choose $e$ coprime to $\varphi(n)$,
recover $d = e^{-1} \bmod \varphi(n)$ by Bézout, and Euler's theorem makes
decryption invert encryption. The full treatment is LL ch 8 (the **Discrete
Mathematics** book here) and MCS chapter 9; the 6.042J "Number Theory" videos are a
good supplement, and Koblitz's *A Course in Number Theory and Cryptography* is the
traditional deeper text — and the bridge directly into session 11.
