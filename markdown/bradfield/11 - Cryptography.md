# Cryptography

Cryptography is where number theory stops being recreational and starts guarding
your bank account. This chapter follows Lovász & Vesztergombi (*Discrete
Mathematics*, "LL") chapters 15 and 16: we begin with the classical
key-distribution problem, distil it into the one-time pad (where "perfect
secrecy" gets a precise meaning), and then escape its impracticality with
public-key cryptography — Diffie-Hellman key exchange and the RSA scheme of LL
section 16.4. RSA leans throughout on the modular arithmetic of LL chapter 8
(Fermat's and Euler's theorems, modular inverses), so we pull those facts in
exactly where the construction needs them.

As in the earlier chapters we treat each claim the same way: tell the story the
way LL tells it, *discover* the mechanism by building the objects and looking,
then *verify* the result in code.

## The key-distribution problem (LL ch 15)

Classical cryptography assumes Alice and Bob already share a secret key. LL ch 15
opens with the **codebook cipher**: both parties hold an identical codebook
mapping each letter to a five-digit string (at most $10^5 = 100000$ code words,
plenty for 26 letters). The flaw is statistical — letter frequencies survive the
substitution, so "e", the commonest English letter, shows up as the commonest
code word, and the cipher unravels letter by letter.

LL's fix is to use a *different* codebook for each letter: the first book for the
first letter, the second for the second, and so on. If the books are random and
each is used once, the cipher becomes provably unbreakable — but now the key (the
stack of codebooks) is as long as all the messages combined, and Alice and Bob
must somehow share it in advance.

That is the **key-distribution problem**, which LL ch 15 names as the central
difficulty of classical cryptography: before they can communicate secretly,
Alice and Bob must already have agreed on a secret, and they cannot use the
insecure channel to do it. (LL's analogy: a new lock ships with its keys — how
does the manufacturer stop anyone copying your key in transit?) The rest of the
two chapters is about escaping this bind.

## One-time pads: perfect secrecy (LL ch 16)

The **one-time pad** (LL section 16.1) is the random-codebook idea distilled to
bits. Encode the message as a bit string $m$ of length $n$. The key $k$ is a
uniformly random bit string of the same length. Encryption is bitwise XOR,
$c = m \oplus k$; decryption is XOR again, because
$c \oplus k = m \oplus k \oplus k = m$.

Why is this *perfectly* secure? LL's argument: fix any ciphertext $c$. For every
candidate message $m'$ there is exactly one key $k' = m' \oplus c$ that would
have produced it. Since the keys are uniform, every message is equally likely
given $c$ — the ciphertext leaks nothing at all. Rather than take that on faith,
we can DISCOVER it by enumerating a tiny message space and grouping every
(message, key) pair by the ciphertext it produces.

```python
<!-- include: code/bradfield/11-cryptography/03_one_time_pad.py -->
```

For each of the eight ciphertexts the demo prints the eight (message, key) pairs
that yield it, and asserts that the messages reached are *all eight, each exactly
once*. So $P(m \mid c)$ is uniform — "for every ciphertext, each message
reachable by exactly one key: P(m | c) is uniform -> perfect secrecy". That is
LL's perfect-secrecy claim made concrete: seeing $c$ tells the eavesdropper
nothing about $m$.

The same demo shows the catch in the name "one-*time* pad". The key must be used
once. Reuse it on two messages $m_1, m_2$ and the key cancels:
$c_1 \oplus c_2 = (m_1 \oplus k) \oplus (m_2 \oplus k) = m_1 \oplus m_2$. The
script confirms `c1 XOR c2 = 101 = m1 XOR m2 = 101`, handing the eavesdropper the
difference of the two plaintexts. So the one-time pad is the gold standard for
secrecy but, as LL notes, it does not solve key distribution — it makes it
*worse*, since the key is now as long as the message. This is the pressure that
forces us toward public-key cryptography.

## Public-key cryptography and trapdoor functions (LL ch 16)

LL section 16.2 introduces the escape, credited to Diffie and Hellman (and, in a
different form, to Rivest, Shamir, and Adleman). Each participant holds **two**
keys: a *public* key, published openly in a directory, and a *private* key, kept
secret. To message Bob, Alice encrypts with Bob's public key; only Bob's private
key can decrypt. There is no shared secret to distribute — the key-distribution
problem dissolves.

For this to work we need a special **one-way function** (LL ch 15 first meets
one-way functions when storing passwords: easy to compute $f(x)$, hard to invert
$f$). Public-key cryptography needs more — a *trapdoor* one-way function: hard to
invert in general, but easy to invert if you know a secret. The public key
*describes the function*; the private key *is the trapdoor*. The most famous such
function rests on the difficulty of factoring large integers, and leads to RSA.

## Diffie-Hellman key exchange (LL ch 16)

Before RSA, the cleanest illustration of the public-channel idea is the
Diffie-Hellman key exchange: two parties agree on a shared secret over a public
channel with no prior secret, relying on modular exponentiation being a one-way
function (easy forward, hard to reverse — the *discrete logarithm* problem).

The protocol: agree publicly on a prime $p$ and a base $g$. Alice picks a secret
$a$ and sends $g^a \bmod p$; Bob picks a secret $b$ and sends $g^b \bmod p$. Each
raises the *other's* value to their own secret: Alice computes $(g^b)^a$, Bob
computes $(g^a)^b$, and both equal $g^{ab} \bmod p$. The eavesdropper sees $g^a$
and $g^b$ but cannot get $g^{ab}$ without solving a discrete log. We trace the
whole exchange and, at this toy scale, even run the only general attack — brute
force over the exponent.

```python
<!-- include: code/bradfield/11-cryptography/02_diffie_hellman.py -->
```

With $g=5, p=23$ and secrets $a=6, b=15$, Alice sends $A=8$, Bob sends $B=19$,
and both land on the shared secret $g^{ab} \bmod 23 = 2$. The brute-force loop
recovers $a=6$ from $A=8$ — feasible here only because $p$ is tiny; for a
several-hundred-digit prime the discrete log is infeasible.

## RSA: a trapdoor one-way function (LL section 16.4)

RSA is the concrete trapdoor one-way function. Its trapdoor is the
**factorization of $n = pq$**. LL section 16.4 builds the scheme directly on
Euler's theorem (LL ch 8):

- Bob picks two primes $p, q$, sets $n = pq$ and $\varphi(n) = (p-1)(q-1)$.
- He picks an **encryption exponent** $e$ coprime to $\varphi(n)$, computes the
  **decryption exponent** $d = e^{-1} \bmod \varphi(n)$, **publishes $(n, e)$**,
  and keeps $d$ (equivalently $p, q$, equivalently $\varphi(n)$) secret.
- Encryption of a message $m$ with $0 \le m < n$ is $c \equiv m^e \pmod n$;
  decryption is $m \equiv c^d \pmod n$. Both are cheap to compute by repeated
  squaring, even for enormous numbers.

Why does $c^d$ give back $m$? This is the crux of LL 16.4. Because
$ed \equiv 1 \pmod{\varphi(n)}$ we can write $ed = 1 + t\,\varphi(n)$, and then
Euler's theorem $m^{\varphi(n)} \equiv 1 \pmod n$ collapses the exponent:

$$c^d \equiv m^{ed} = m^{1 + t\varphi(n)} = m \cdot (m^{\varphi(n)})^{t}
\equiv m \cdot 1^{t} = m \pmod n.$$

It is worth *seeing* this happen rather than only reading the algebra. The next
demo takes LL's own tiny example — $p=5$, $q=11$, so $n=55$, $\varphi(n)=40$,
$e=3$, $d=27$ — and traces the mechanism step by step: it checks Euler's theorem
on this modulus, shows $ed = 81 = 2\varphi(n)+1$ so the exponent on $m$
collapses, and then hand-traces $13^{27} \bmod 55$ by repeated squaring exactly
as LL does on the page.

```python
<!-- include: code/bradfield/11-cryptography/04_euler_decryption.py -->
```

The output mirrors LL's hand computation: $7^{40} \equiv 1 \pmod{55}$, then the
squaring ladder $13^2 \equiv 4$, $13^4 \equiv 16$, $13^8 \equiv 36$,
$13^{16} \equiv 31$, and finally
$13^{27} = 13^{16}\cdot 13^{8}\cdot 13^{2}\cdot 13 \equiv 7 \pmod{55}$ — back to
the original message. Euler's theorem is not invoked as a black box; you watch it
turn $m^{ed}$ into $m$.

## The number theory RSA needs (LL ch 8)

RSA leans on three facts from LL ch 8, each exercised inside the demos above and
the full cipher below.

- **Fermat's little theorem:** for a prime $p$ and $a$ not divisible by $p$,
  $a^{p-1} \equiv 1 \pmod p$.
- **Euler's theorem:** if $\gcd(a, n) = 1$ then
  $a^{\varphi(n)} \equiv 1 \pmod n$, where $\varphi(n)$ counts the integers in
  $\{1, \ldots, n\}$ coprime to $n$. For $n = pq$ a product of two distinct
  primes, $\varphi(n) = (p-1)(q-1)$. This is the theorem that makes decryption
  invert encryption (verified in `04_euler_decryption.py` above).
- **Modular inverse:** when $\gcd(e, \varphi) = 1$, $e$ has a unique inverse
  modulo $\varphi$, computable by the extended Euclidean algorithm. This is how
  Bob gets $d$ from $e$ — and it is exactly where his *secret* knowledge of
  $\varphi(n)$ is used.

## Putting it together: the RSA cipher

The full scheme runs key generation, encryption, and decryption on LL's example,
checks the ciphertext is LL's $c = 13$, verifies $c^d$ recovers $m$ for *every*
message $0 \le m < n$, and then shows the trapdoor in action: knowing the
factorization $n = 5 \cdot 11$ yields $\varphi(n) = 40$ and hence $d = 27$.

```python
<!-- include: code/bradfield/11-cryptography/01_rsa.py -->
```

The eavesdropper, by contrast, sees only $(n, e)$ and $c$. To recover $d$ she
needs $\varphi(n) = (p-1)(q-1)$, which needs the factorization of $n$. LL section
16.4 ends on exactly this point: multiplying $p$ and $q$ is one step, but
factoring the product back is infeasible for several-hundred-digit primes — the
gap *is* the trapdoor. We can watch that asymmetry emerge by timing naive
trial-division factoring as $n$ grows, and confirm that the attacker's only route
to $d$ runs through the factorization.

```python
<!-- include: code/bradfield/11-cryptography/05_factoring_trapdoor.py -->
```

The factor-time column climbs steeply with the size of $n$ while the forward
multiplication stays a single step; and the attack recovers the private exponent
$d$ *only* after factoring $n$. Scale the primes to hundreds of digits and that
factoring step is the wall today's cryptography stands behind.

One bonus from the symmetry of $e$ and $d$: because encryption and decryption are
inverse operations, Bob can also **sign** a message by applying his private
exponent $d$; anyone can verify the signature by applying his public $e$ and
checking the original message comes back. LL closes ch 16 noting this is the
basis of digital signatures.

## Where to go deeper

- **LL chapters 15 and 16** — the source development: classical ciphers, the
  key-distribution problem, one-time pads, public-key cryptography, and the RSA
  scheme of section 16.4.
- **LL chapter 8** — the number theory RSA rests on: Fermat, Euler, $\varphi$,
  the Euclidean algorithm, and modular inverses.
- **MCS "Number Theory" chapter** — the same Euler/Fermat machinery and an RSA
  treatment with CS-flavored framing and Turing's-codebreaking history.

Seeing perfect secrecy in a truth-table, watching Euler's theorem fold
$m^{ed}$ back to $m$, and timing the factoring wall do for cryptography what
enumeration did for counting: they turn a claim you could only nod at into one
you have checked with your own (machine's) hands. The proof still tells you
*why*; the code tells you it is *so*.
