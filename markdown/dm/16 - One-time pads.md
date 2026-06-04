## One-time pads

There is another simple, frequently used method, which is much more secure: the use of “one-time pads”. This method is very safe; it was used e.g. during World War II for communication between the American President and the British Prime Minister. Its disadvantage is that it requires a very long key, which can only be used once.

A one-time pad is a randomly generated string of 0’s and 1’s. Say, here is one:

11000111000010000110010100100100101100110010101100001110110000010

Both Kings Arthur and Bela has this sequence (it was sent well in advance by a messenger). Now King Arthur wants to send the following message to King Bela:

ATTACK MONDAY

First, he has to convert it to 0’s and 1’s. It is not clear that medieval kings had the knowledge to do so, but the reader should be able to think of various ways: using ASCII codes, or Unicodes of the letters, for example. But we want to keep things simple, so we just number the letters from 1 to 26, and then write down the binary representation of the numbers, putting 0’s in front so that we get a string of length 5 for each letter. Thus we have “00001” for A, “00010” for B, etc. We use “00000” for “Space”. The above message becomes:

00001100101001000001000110101100000011010111101110001000000111001

This might look cryptic enough, but Caligula (or rather one the excellent Greek scientist he keeps in his court) could easily figure out what it stands for. To encode it, Arthur adds the one-time pad to the message bit-by-bit. To the first bit of the message (which is 0) he adds the first bit of the pad (1) and writes down the first bit of the encoded message: $0+1=1$. He computes the second, third, etc. bits similarly: $0+1=1$, $0+0=0$, $0+0=0$, $1+0=1$, $1+1=0$,… (What is this $1+1=0$? Isn’t $1+1=2$? Or, if we want to use the binary number system, $1+1=10$? Well, all that happens is that we ignore the “carry”, and just write down the last bit. We could also say that the computation is done modulo 2). Another way of saying what King Arthur does is the following: if the $k$-th bit of the pad is 1, he flips the $k$-th bit of the text; else, he leaves it as it was.

So Arthur computes the encoded message:

11001011101011000111010010001000101111100101000010000110110111011

He sends this to King Bela, who looking at the one-time pad, can easily flip back the appropriate bits, and recover the original message.

But Caligula (and even his excellent scientists) does not know the one-time pad, so he does not know which bits were flipped, and so he is helpless. The message is safe.

It can be expensive to make sure that Sender and Receiver both have such a common key; but note that the key can be sent at a safer time and by a completely different method than the message; moreover, it may be possible to agree on a key even without actually passing it.

We can reproduce King Arthur's encryption bit-for-bit in a few lines of Python. XORing the book's plaintext `00001100101...` with its pad `11000111000...` should yield exactly the printed ciphertext `11001011101...`, and XORing the pad back must recover the plaintext (perfect secrecy: each bit is flipped iff the pad bit is 1). The same script also dramatizes exercise 16.3 above — encrypting two messages under the *same* pad and XORing the two ciphertexts cancels the pad entirely, leaking $m_1 \oplus m_2$ with no key at all, which is precisely why a one-time pad must be used exactly once.

```python
<!-- include: code/dm/16 - One-time pads/01_python.py -->
```

Running it prints `encrypt reproduces book ciphertext: True`, `decrypt round-trips to plaintext: True`, and `c1 XOR c2 == m1 XOR m2 (pad gone): True`, confirming both the book's arithmetic and the catastrophic leakage from pad reuse.

## How to save the last move in chess?

Modern cryptography started in the late 1970’s with the idea that it is not only lack of information that can protect our message against an unauthorized eavesdropper, but also the computational complexity of processing it. The idea can is illustrated by the following simple example.

Alice and Bob are playing chess over the phone. They want to interrupt the game for the night; how can they do it so that the person to move should not get the improper advantage of being able to think about his move whole night? At a tournament, the last move is not made on the board, only written down, put in an envelope, and deposited with the referee. But now the two players have no referee, no envelope, no contact other than the telephone line. The player making the last move (say, Alice) has to send Bob some message. The next morning (or whenever they continue the game) she has to give some additional information, some “key”, which allows Bob to reconstruct the move. Bob should not be able to reconstruct Alice’s move without the key; Alice should not be able to change her mind overnight and modify her move.

Surely this seems to be impossible! If she gives enough information the first time to uniquely determine her move, Bob will know the move too soon; if the information given the first time allows several moves, then she can think about it overnight, figure out the best among these, and give the remaining information, the “key” accordingly.

If we measure information in the sense of classical information theory, then there is no way out of this dilemma. But complexity comes to our help: it is not enough to communicate information, it must also be processed.

So here is a solution to the problem, using elementary number theory! (Many other schemes can be designed.) Alice and Bob agree to encode every move as a 4-digit number (say, ‘11’ means ‘K’, ‘6’ means ‘f’, and ‘3’ means itself, so ‘1163’ means ‘Kf3’). So far, this is just notation.

Next, Alice extends the four digits describing her move to a prime number $p=1163\ldots$ with 200 digits. She also generates another prime $q$ with 201 digits and computes the product $N=pq$ (this would take rather long on paper, but is trivial using a personal computer). The result is a number with 400 or 401 digits; she sends this number to Bob.

Next morning, she sends both prime factors $p$ and $q$ to Bob. He reconstructs Alice’s move from the first four digits of the smaller prime. To make sure that Alice was not cheating, he should check that $p$ and $q$ are primes and that their product is $N$.

Let us argue that this protocol does the job.

First, Alice cannot change her mind overnight. This is because the number $N$ contains all the information about her move: this is encoded as the first four digits of the smaller prime factor of $N$. So Alice commits herself to the move when sending $N$.

But exactly because the number $N$ contains all the information about Alice’s move, Bob seems to have the advantage, and he indeed would have if he had unlimited time or unbelievably powerful computers. What he has to do is to find the prime factors of the number $N$. But since $N$ has 400 digits (or more), this is a hopelessly difficult task with current technology.

Can Alice cheat by sending a different pair $(p^{\prime},q^{\prime})$ of primes the next morning? No, because Bob can easily compute the product $p^{\prime}q^{\prime}$, and check that this is indeed the number $N$ that was sent the previous night. (Note the role of the uniqueness of prime factorization, Theorem 8.1.)

All the information about Alice’s move is encoded in the first 4 digits of the smaller prime factor $p$. We could say that the rest of $p$ and the other prime factor $q$ serve as a “deposit box”: they hide this information from Bob, and can be opened only if the appropriate key (the factorization of $N$) is available. The crucial ingredient of this scheme is complexity: the computational difficulty to find the factorization of an integer.

With the spread of electronic communication in business, many solutions of traditional correspondence and trade must be replaced by electronic versions. We have seen an electronic “deposit box” above. Other schemes (similar or more involved) can be found for electronic passwords, authorization, authentication, signatures, watermarking, etc. These schemes are extremely important in computer security, cryptography, automatic teller machines, and many other fields. The protocols are often based on simple number theory; in the next section we discuss (a very simplified version of) one of them.

## How to verify a password—without learning it?

In a bank, a cash machine works by name and password. This system is safe as long as the password is kept in secret. But there is one week point in security: the computer of the bank must store the password, and the administrator of this computer may learn it and later misuse it.

Complexity theory provides a scheme where the bank can verify that the customer does indeed know the password—without storing the password itself! At the first glance this looks impossible—just as the problem with filing the last chess move was. And the solution (at least the one we discuss here) uses the same kind of construction as our telephone chess example.

Suppose that the password is a 100-digit prime number $p$ (this is, of course, too long for everyday use, but it illustrates the idea best). When the customer chooses the password, he chooses another prime $q$ with 101 digits, forms the product $N=pq$ of the two primes, and tells the bank the number $N$. When the teller is used, the customer tells his name and the password $p$. The computer of the bank checks whether or not $p$ is a divisor of $N$; if so, it accepts $p$ as a proper password. The division of a 200 digit number by a 100 digit number is a trivial task for a computer.

Let us assume that the system administrator learns the number $N$ stored along with the files of our customer. To use this in order to impersonate the customer, he has to find a 100-digit number that is a divisor of $N$; but this is essentially the same problem as finding the prime factorization of $N$, and this is hopelessly difficult. So—even though all the necessary information is contained in the number $N$—the computational complexity of the factoring problem protects the password of the customer!

## How to find these primes?

In our two simple examples of “modern cryptography”, as well as in almost all the others, one needs large prime numbers. We know that there are arbitrarily large primes (Theorem 8.3), but are there any with 200 digits, starting with 1163 (or any other 4 given digits)? Maple found (in a few seconds on a laptop!) the smallest such prime number:

```
1163000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000371
```

The smallest 200 digit integer starting with 1163 is $1163\cdot 10^{196}$. This is of course not a prime, but above we found a prime very close by. There must be zillions of such primes! In fact, a computation very similar to what we did in section 8.4 shows that the number of primes Alice can choose from is about $1.95\cdot 10^{193}$.

This is a lot of possibilities, but how to find one? It would not be good to use the prime above (the smallest eligible): Bob could guess this and thereby find out Alice’s move. What Alice can do is to fill in the missing 196 digits randomly, and then test whether the number she obtains is a prime. If not, she can throw it away and try again. As we computed in section 8.4, one in every 460 200-digit numbers is a prime, so on the average in about 460 trials she gets a prime. This looks like a lot of trials, but of course she uses a computer; here is one we computed for you with this method (in a few seconds again):

1163146712876555763279909704559660690828365476006668873814489354662
4743604198911046804111038868958805745715572480009569639174033385458
418593535488622323782317577559864739652701127177097278389465414589

So we see that in the “envelope” scheme above, both computational facts mentioned in section 8.7 play a crucial role: it is easy to test whether a number is a prime (and thereby it is easy to compute the encryption), but it is difficult to find the prime factors of a composite number (and so it is difficult to break the cryptosystem).

Let us make the whole envelope scheme concrete with `sympy`, using the book's exact numbers. The move Kf3 becomes the code $1163$, extended to a 200-digit *prime* whose first four digits are $1163$, then hidden inside $N = pq$. We can check the book's own claims: the smallest 200-digit prime starting $1163$ really is $1163\cdot 10^{196} + 371$, and the random 200-digit prime printed above really is prime (`isprime` returns `True`). Binding is shown by `verify_and_read` (Bob checks both factors are prime and multiply to $N$) and by confirming that a *different* prime does not divide $N$ — unique factorization (Theorem 8.1) pins $N$ to exactly $\{p,q\}$.

```python
<!-- include: code/dm/16 - One-time pads/02_python.py -->
```

Running it prints `book's random p: 200 digits, 1163.., prime: True True True`, `N has 400 digits`, and `Bob recovers move code: 1163 == 1163 -> True`, confirming the commitment is both hiding and binding using the book's exact primes.

> **16.1** For the following message, the Kings used substitution code. Caligula intercepted the message and quite easily broke it. Can you do it too?
>
> U GXUAY LS ZXMEKW AMG TGGTIY HMD TAMGXSD LSSY, FEG GXSA LUGX HEKK HMDIS. FSKT

> **16.2** At one time, Arthur made the mistake of using the one-time pad shifted: the first bit of the plain text he encoded using the second bit of the pad, the second bit of the plain text he encoded using the third bit of the pad etc. He noticed his error after he sent the message off. Being afraid that Bela will not understand his message, he encoded it again (now correctly) using the same one-time pad, and sent it to Bela by another courier, explaining what happened.
>
> Caligula intercepted both messages, and was able to recover the plain text. How?

> **16.3** The Kings were running low on one-time pads, and so Bela had to use the same pad to encode his reply as they used for Arthur’s message. Caligula intercepted both messages, and was able to reconstruct the plain texts. Can you explain how?

> **16.4** Motivated by the one-time pad method, Alice suggests the following protocol for saving the last move in their chess game: in the evening, she encrypts her move (perhaps with other text added, to make it reasonably long) using a randomly generated 0-1 sequence as the key (just like in the one-time pad method). The next morning she sends the key to Bob, so that he can decrypt the message. Should Bob accept this suggestion?

> **16.5** Alice modifies her suggestion as follows: instead of the random 0-1 sequence, she offers to use a random, but meaningful text as the key. For whom would this be advantageous?

## Public key cryptography

Cryptographic systems used in real life are more complex than those described in the previous section—but they are based on similar principles. In this section we sketch the math behind the most commonly used system, the RSA code (named after its inventors, Rivest, Shamir and Adleman).

the protocol. Let Alice generate two 100-digit prime numbers, $p$ and $q$ and computes their product $m=pq$. Then she generates two 200-digit numbers $d$ and $e$ such that $(p-1)(q-1)$ is a divisor of $ed-1$. (We’ll come back to the question how this is done.)

The numbers $m$ and $e$ she publishes on her web site, or in the phone book, but the prime factors $p$ and $q$ and the number $d$ remain her closely guarded secrets. The number $d$ is called her private key, and the number $e$, her public key (the number $p$ and $q$ she may even forget—they will not be needed to operate the system, just to set it up.

Suppose first that Bob wants to send a message to Alice. He writes the message as a number $x$ (we have seen before how to do so). This number $x$ must be a non-negative integer less than $m$ (if the message is longer, he can just break it up into smaller chunks).

The next step is the trickiest: Bob computes the remainder of $x^{e}$ modulo $m$. Since both $x$ and $e$ are huge integers (200 digits), the number $x^{e}$ has more than $10^{200}$ digits - we could not even write it down, let alone compute it! Luckily, we don’t have to compute this number, only its remainder when dividing with $m$. This is still a large number - but at least it can be written down in 2-3 lines. We’ll return to computing it in the exercises.

So let $r$ be this remainder; this is sent to Alice. When she receives it, she can decrypt it using her private key $d$ by doing essentially the same procedure as Bob did: she computes the remainder of $r^{d}$ modulo $m$. And—a black magic of number theory, until you see the explanations—this remainder is just the plain text $x$.

What if Alice wants to send a message to Bob? He also needs to go through the trouble of generating his private and public keys. He has to pick two primes $p^{\prime}$ and $q^{\prime}$, compute their product $m^{\prime}$, select two positive integers $d^{\prime}$ and $e^{\prime}$ so that $(p^{\prime}-1)(q^{\prime}-1)$ is a divisor of $e^{\prime}d^{\prime}-1$, and finally publish $m^{\prime}$ and $e^{\prime}$. Then Alice can send him a secure message.

The black math magic behind the protocol. The key fact from mathematics we use is Fermat’s Theorem 8.6. Recall that $x$ is the plain text (written as an integer) and the encrypted message $r$ is the remainder of $x^{e}$ modulo $m$. So we can write

$r=x^{e}-km$

with an appropriate integer $k$ (the value of $k$ is irrelevant for us). To decrypt, Alice raises this to the $d$-th power, to get

$r^{d}=(x^{e}-km)^{d}=x^{ed}+k^{\prime}m,$

where $k^{\prime}$ is again some integer. To be more precise, she computes the remainder of this modulo $m$, which is the same as the remainder of $x^{ed}$ modulo $m$. We want to show that this is just $x$. Since $0\leq x<m$, it suffices to argue that $x^{ed}-x$ is divisible by $m$. Since $m=pq$ is the product of two distinct primes, it suffices to prove that $x^{ed}-x$ is divisible by each of $p$ and $q$.

Let us consider divisibility by $p$, for example. The main property of $e$ and $d$ is that $ed-1$ is divisible by $(p-1)(q-1)$, and hence also by $p$. This means that we can write $ed=(p-1)l+1$, where $l$ is a positive integer. we have

$x^{ed}-x=x(x^{(p-1)l}-1).$

Here $x^{(p-1)l}-1$ is divisible by $x^{p-1}-1$ (see exercise 8.1), and so $x(x^{(p-1)l}-1)$ is divisible by $x^{p}-x$, which in turn is divisible by $p$ by Fermat’s “Little” Theorem.

A correctness *theorem* is precisely a "for all inputs" claim, so the natural way to stress-test this argument is property-based testing. The following `hypothesis` demo encodes the proof's three steps and checks them on hundreds of random inputs: Fermat's theorem holds mod $p$ and mod $q$; the composed map $x \mapsto x^{ed}$ is the identity mod $m$ (because $(p-1)(q-1) \mid ed-1$); and the full RSA round trip recovers every plaintext $0 \le x < m$.

```python
<!-- include: code/dm/16 - One-time pads/04_python.py -->
```

Running it prints `3 passed`, confirming Fermat's theorem, the $x^{ed}\equiv x$ identity, and the RSA round trip all hold across hundreds of randomized cases — the executable counterpart of this correctness proof.

How to do all this computation? We already discussed how to find primes, and Alice can follow the the method described in section 8.7.

The next issue is the computation of the two keys $e$ and $d$. One of them, say $e$, Alice can choose at random, from the range $1..(p-1)(q-1)-1$. She has to check that it is relatively prime to $(p-1)(q-1)$; this can be done efficiently with the help of the Euclidean Algorithm discussed in section 8.6. If the number she chose is not relatively prime to $(p-1)(q-1)$, she just throws it out, and tries another one. This is similar to the method we used for finding a prime, and it is not hard to see that she’ll find a good number on more trials than she can find a prime.

But if the euclidean algorithm finally succeeds, then, as in section 8.6, it also gives two integers $m$ and $n$ so that

$em+(p-1)(q-1)n=1.$

So $em-1$ is divisible by $(p-1)(q-1)$. Let $d$ denote the remainder of $m$ modulo $(p-1)(q-1)$, then $ed-1$ is also divisible by $(p-1)(q-1)$, and so we have found a suitable key $d$.

Finally, we have to address the question: how to compute the remainder of $x^{e}$ modulo $m$, when just to write down $x^{e}$ would fill the universe? The answer is easy: after each operation, we can replace the number we get by its remainder modulo $m$. This way we never get numbers with more than 400 digits, which is manageable.

But there is another problem: $x^{e}$ denotes $x$ multiplied by itself $e\approx 10^{200}$ times; even if we carry out 1 billion multiplications every second, we will not finish before the end of the universe!

The first hint that something can be done comes if we think of the special case when $e=2^{k}$ is a power of 2. In this case, we don’t have to multiply with $x$ $2^{k}-1$ times; instead, we can repeatedly square $x$ just $k$ times: we get $x^{2}$, $(x^{2})^{2}=x^{4}$, $(x^{4})^{2}=x^{8}$ etc.

If $e$ is not a power of 2, but say the sum of two powers of 2: $e=2^{k}+2^{l}$, then we can separately compute $x^{2^{k}}$ and $x^{2^{l}}$ by this repeated squaring, and then multiply these 2 numbers (not forgetting that after each squaring and multiplication, we replace the number by its remainder modulo $m$). This works similarly if $m$ is the sum of a small number of powers of 2.

But every number is the sum of a small number of powers of 2: just think of its representation in binary. The binary representation $101100101_{2}$ actually means that the number is $2^{8}+2^{6}+2^{5}+2^{2}+2^{0}$. A 200 digit number is the sum of at most 665 powers of 2. We can easily compute (with a computer, of course) $x^{2^{k}}$ for every $k\leq 664$ by repeated squaring, and then the product of these numbers.

> **16.6** Let $e=e_{0}e_{1}\ldots e_{k}$ be the expression of $e$ in binary ($e_{i}=0$ or $1$, $e_{0}$ is always 1). Let $x_{0}=x$, and for $j=1,\ldots,k$, let
>
> $$x_{j}=\left\{\begin{array}{ll}x_{j-1}^{2},&\text{ if }e_{j}=0,\\ x_{j-1}^{2}x,&\text{ if }e_{j}=1.\end{array}\right.$$
>
> Show that $x_{k}=x^{e}$.

### Signatures, etc.

There are many other nice things this system can do. For example, suppose that Alice gets a message from Bob as described above. How can she know that it indeed came from Bob? Just because it is signed “Bob”, it could have come from anybody. But Bob can do the following. First, he encrypts the message with his private key, then adds “Bob”, and encrypts it again with Alice’s public key. When Alice receives it, she can decrypt it with her private key. She’ll see a still encrypted message, signed “Bob”. She can cut away the signature, look up Bob’s public key in the phonebook, and use it to decrypt the message.

One can use similar tricks to implement many other electronic gadgets, using RSA.

We can now run the entire protocol of this section end to end with `sympy`: $m = pq$, a public exponent $e$ coprime to $(p-1)(q-1)$, and the private key $d = e^{-1} \bmod (p-1)(q-1)$ obtained from the Euclidean algorithm (`mod_inverse`). Encrypting the chess move $x = 1163$ as $r = x^e \bmod m$ and decrypting $r^d \bmod m$ returns $1163$ exactly. The script also shows this section's "fills the universe" point — $x^e$ has 16 digits here but $r \bmod m$ stays tiny via fast modular exponentiation — and implements the signature trick just described (sign with the private key, verify with the public key).

```python
<!-- include: code/dm/16 - One-time pads/03_python.py -->
```

Running it prints `check  e*d mod (p-1)(q-1) = 1`, `x = 1163 -> ciphertext r = 506213033549 -> decrypt = 1163  ok? True`, and `signature verifies to original msg: True`, confirming the round trip and the signature scheme.

### Security.

The security of the RSA protocol is a difficult issue, and since its inception in 1977, thousands of researchers have investigated it. The fact that no attack has been generally successful is a good sign; but unfortunately no exact proof of it security has been found (and it appears that current mathematics lacks the tools to provide such a proof in the foreseeable future.

We can give, however, at least some arguments that support its security. Suppose that you intercept the message of Bob, and want to decipher it. You know the remainder $r$ (this is the intercepted message). You also know Alice’s public key $e$, and the number $m$. One could think of two lines of attack: either you can figure out her private key $d$ and then decrypt the message just as she does, or you could somehow more directly find the integer $x$, knowing the remainder of $x^{e}$ modulo $m$.

Unfortunately there is no theorem stating that either of this is impossible in less than astronomical time. But one can justify the security of the system with the following fact: if one can break the RSA system, then one can use the same algorithm to find the prime factors of $m$ (see exercise 16.7). Since the factorization problem has been studied by so many and no efficient method has been found, this makes the security of RSA quite probable.

> **16.7** Suppose that Bob develops an algorithm that can break RSA in the first, more direct way described above: knowing Alice’s public key $m$ and $e$, he can find her private key $d$.
>
> (a) Show that he can use this to find the number $(p-1)(q-1)$;
>
> (b) from this, he can find the prime factorization $m=pq$.

### The real word.

How practical could such a complicated system be? It seems that only a few mathematicians could ever use it. But in fact you have probably used it yourself hundreds of times! RSA is used in SSL (Secure Socket Layer), which in turn is used in https (secure http). Any time you visit a “secure site” of the internet, your computer generates a public and private key for you, and uses them to make sure that your credit card number and other personal data remain secret. It does not have to involve you in this at all—all you notice is that the connection is a bit slower.

In practice, the two 100 digit primes are not considered sufficiently secure. Commercial applications use more than twice this length, military applications, more than 4 times.

While the hairy computations of raising the plain text $x$ to an exponent which itself has hundreds of digits are surprisingly efficient, it would still be too slow to encrypt and decrypt each message this way. A way out is to send, as a first message, the key to a simpler system (think of a one-time pad, although one uses a more efficient system in practice, like DES, the Digital Encryption Standard). This key is then used for a few minutes to encode the messages going back and force, then thrown away. The idea is that in a short session, the number of encoded messages is not enough for an eavesdropper to break the system.
