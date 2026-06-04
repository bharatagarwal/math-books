## Integers, divisors, and primes

In this chapter we discuss properties of integers. This area of mathematics is called *number theory*, and it is a truly venerable field: its roots go back about 2500 years, to the very beginning of Greek mathematics. One might think that after 2500 years of research, one would know essentially everything about the subject. But we shall see that this is not the case: there are very simple, natural questions which we cannot answer; and there are other simple, natural questions to which an answer has only been found in the last years!

## Divisibility of integers

We start with some very basic notions concerning integers. Let $a$ and $b$ be two integers. We say that $a$ *divides* $b$, or $a$ *is a divisor of* $b$, or $b$ *is a multiple of* $a$ (these phrases mean the same thing), if there exists an integer $m$ such that $b=am$. In notation: $a|b$. If $a$ is not a divisor of $b$, then we write $a\not|b$. If $a\neq 0$, then this means that the ratio $b/a$ is an integer.

If $a\not|b$, and $a>0$, then we can still divide $b$ by $a$ with remainder. The remainder $r$ of the division $b:a$ is an integer that satisfies $0\leq r<a$. If the quotient of the division with remainder is $q$, then we have

$b=aq+r.$

This is a very useful way of thinking about a division with remainder.

You have probably seen these notions before; the following exercises should help you check if you remember enough.

- 8.1 Check (using the definition) that $1|a$, $-1|a$, $a|a$ and $-a|a$ for every integer $a$.
- 8.2 What does it mean for $a$, in more everyday terms, if (a) $2|a$; (b) $2\not|a$; (c) $0|a$.
- 8.3 (a) Prove that

(a) if $a|b$ and $b|c$ then $a|c$;

(b) if $a|b$ and $a|c$ then $a|b+c$ and $a|b-c$;

(c) if $a,b>0$ and $a|b$ then $a\leq b$;

(d) if $a|b$ and $b|a$ then either $a=b$ or $a=-b$.
- 8.4 Let $r$ be the remainder of the division $b:a$. Assume that $c|a$ and $c|b$. Prove that $c|r$.
- 8.5 Assume that $a|b$, and $a,b>0$. Let $r$ be the remainder of the division $c:a$, and let $s$ be the remainder of the division $c:b$. What is the remainder of the division $s:a$?
- 8.6 (a) Prove that for every integer $a$, $a-1|a^{2}-1$.

(b) More generally, for every integer $a$ and positive integer $m$,

$a-1|a^{n}-1.$

## Primes and their history

An integer $p>1$ is called a prime if it is not divisible by any integer other than $1,-1,p$ and $-p$. Another way of saying this is that an integer $p>1$ is a prime if it cannot be written as the product of two smaller positive integers. An integer $n>1$ that is not a prime is called composite (the number $1$ is considered neither prime, nor composite). Thus $2,3,5,7,11$ are primes, but $4=2\cdot 2$, $6=2\cdot 3$, $8=2\cdot 4$, $9=3\cdot 3$, $10=2\cdot 5$ are not primes. Table 1 contains the first $500$ primes.

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571

Table 1: The first 500 primes

Primes have fascinated people ever since ancient times. Their sequence seems very irregular, yet on closer inspection it seems to carry a lot of hidden structure. The ancient Greeks already knew that there are infinitely many such numbers. (Not only did they know this; they proved it!)

It was not easy to prove any further facts about primes. Their sequence has holes and

![Figure 11: A bar chart of primes up to 1000](08 - Integers divisors and primes_images/img-0.jpeg)

dense spots (see also figure 11). How large are these holes? For example, is there a prime number with any given number of digits? The answer to this question will be important for us when we discuss cryptography. The answer to this question is in the affirmative, but this fact was not proved until the mid-19th century, and many similar questions are open even today.

A new wave of developments in the theory of prime numbers came with the spread of computers. How do you decide about a positive integer  $n$  whether it is a prime? Surely this is a finite problem (you can try out all smaller positive integers to see if any of them is a proper divisor), but such simple methods become impractical as soon as the number of digits is more than 20 or so.

It is only in the last 20 years since much more efficient algorithms (computer programs) exist to test if a given integer is a prime. We will get a glimpse of these methods later. Using these methods, one can now rather easily determine about a number with 1000 digits whether it is a prime or not.

If an integer larger than 1 is not a prime itself, then it can be written as a product of primes: we can write it as a product of two smaller positive integers; if one of these is not a prime, we write it as the product of two smaller integers etc; sooner or later we must end up with only primes. The ancient Greeks also knew (and proved!) a subtler fact about this representation: that it is unique. What this means is that there is no other way of writing  $n$  as a product of primes (except, of course, we can multiply the same primes in a different order). To prove this takes some sophistication, and to recognize the necessity of such a result was quite an accomplishment; but this is all more than 2000 years old!

It is really surprising that, even today, no efficient way is known to find such a decomposition. Of course, powerful supercomputers and massively parallel systems can be used to find decompositions by brute force for fairly large numbers; the current record is around a 140 digits, and the difficulty grows very fast (exponentially) with number of digits. To

find the prime decomposition of a number with 400 digits, by any of the known methods, is way beyond the possibilities of computers in the foreseeable future.

## Factorization into primes

We have seen that every integer larger than 1 that is not a prime itself can be written as a product of primes. We can even say that every positive integer can be written as a product of primes: primes can be considered as “products with one factor”, and the integer 1 can be thought of as the “empty product”. With this in mind, we can state and prove the following theorem, announced above, sometimes called the “Fundamental Theorem of Number Theory”.

**Theorem 8.1.**

Every positive integer can be written as the product of primes, and this factorization is unique up to the order of the prime factors.

We prove this theorem by a version of induction, which is sometimes called the “minimal criminal” argument. The proof is indirect: we suppose that the assertion is false, and using this assumption, we derive a logical contradiction.

So assume that there exists an integer with two different factorizations; call such an integer a “criminal”. There may be many criminals, but we consider the smallest one. Being a criminal, this has at least two different factorizations:

$n=p_{1}\cdot p_{2}\cdot\ldots\cdot p_{m}=q_{1}\cdot q_{2}\cdot\ldots\cdot q_{k}\,.$

We may assume that $p_{1}$ is the smallest prime occurring in these factorizations. (Indeed, if necessary, we can interchange the left hand side and the right hand side so that the smallest prime in any of the two factorizations occurs on the left hand side; and then change the order of the factors on the left hand side so that the smallest factor comes first. In the usual slang of mathematics, we say that we may assume that $p_{1}$ is the smallest prime without loss of generality.)

The number $p_{1}$ cannot occur among the factors $q_{i}$, otherwise we can divide both sides by $p_{1}$ and get a smaller criminal.

Divide each $q_{i}$ by $p_{1}$ with residue: $q_{i}=p_{1}a_{i}+r_{i}$, where $0\leq r_{i}<p_{1}$. We know that $r_{i}\neq 0$, since a prime cannot be a divisor of another prime.

Let $n^{\prime}=r_{1}\cdot\ldots\cdot r_{k}$. We show that $n^{\prime}$ is a smaller criminal. Trivially $n^{\prime}=r_{1}r_{2}\ldots r_{k}<q_{1}q_{2}\ldots q_{k}=n$. We show that $n^{\prime}$ too has two different factorizations into primes. One of these can be obtained from the definition $n^{\prime}=r_{1}r_{2}\ldots r_{k}$. Here the factors may not be primes, but we can break them down into products of primes, so that we end up with a decomposition of $n^{\prime}$.

To get another decomposition, we observe that $p_{1}|n^{\prime}$. Indeed, we can write the definition of $n^{\prime}$ in the form

$n^{\prime}=(q_{1}-a_{1}p_{1})(q_{2}-a_{2}p_{1})\ldots(q_{k}-a_{k}p_{1}),$

and if we expand, then every term will be divisible by $p_{1}$. Now we divide $n^{\prime}$ by $p_{1}$ and then continue to factor $n^{\prime}/p_{1}$, to get a factorization of $n^{\prime}$.

But are these two factorizations different? Yes! The prime $p_{1}$ occurs in the second, but it cannot occur in the first, where every prime factor is smaller than $p_{1}$.

Thus we have found a smaller criminal. Since $n$ was supposed to be the smallest among all criminals, this is a contradiction. The only way to resolve this contradiction is to conclude that there are no criminals; our “indirect assumption” was false, and no integer can have two different prime factorizations.

As an application of Theorem 8.1, we prove a fact that was known to the Pythagoreans (students of Pythagoras) in the 6th century B.C.

**Theorem 8.2.**

The number $\sqrt{2}$ is irrational.

(A real number is irrational if it cannot be written as the ratio of two integers. For the Pythagoreans, the question arose from geometry: they wanted to know whether the diagonal of a square is “commeasurable” with its side, i.e., is there any segment which would be contained in both an integer number of times. The above theorem answered this question in the negative, causing a substantial turmoil in their ranks.)

We give an indirect proof again: we suppose that $\sqrt{2}$ is rational, and derive a contradiction. What the indirect assumption means is that $\sqrt{2}$ can be written as the quotient of two positive integers: $\sqrt{2}=\frac{a}{b}$. Squaring both sides and rearranging, we get $2b^{2}=a^{2}$.

Now consider the prime factorization of both sides, and in particular, the prime number $2$ on both sides. Suppose that $2$ occurs $m$ times in the prime factorization of $a$ and $n$ times in the prime factorization of $b$. Then it occurs $2m$ times in the prime factorization of $a^{2}$. On the other hand, it occurs $2n$ times in the prime factorization of $b^{2}$, and thus it occurs $2n+1$ times in the prime factorization of $2b^{2}$. Since $a^{2}=2b^{2}$ and the prime factorization is unique, we must have $2m=2n+1$. But this is impossible since $2m$ is even but $2n+1$ is odd. This contradiction proves that $\sqrt{2}$ must be irrational.

> **8.7** Are there any even primes?

> **8.8** (a) Prove that if $p$ is a prime, $a$ and $b$ are integers, and $p|ab$, then either $p|a$ or $p|b$ (or both).
>
> (b) Suppose that $a$ and $b$ are integers and $a|b$. Also suppose that $p$ is a prime and $p|b$ but $p\not|a$. Prove that $p$ is a divisor of the ratio $b/a$.

> **8.9** Prove that the prime factorization of a number $n$ contains at most $\log_{2}n$ factors.

> **8.10** Let $p$ be a prime and $1\leq a\leq p-1$. Consider the numbers $a,2a,3a,\ldots,(p-1)a$. Divide each of them by $p$, to get residues $r_{1},r_{2},\ldots,r_{p-1}$. Prove that every integer from $1$ to $p-1$ occurs exactly once among these residues.
>
> [Hint: First prove that no residue can occur twice.]

> **8.11** Prove that if $p$ is a prime, then $\sqrt{p}$ is irrational. More generally, prove that if $n$ is an integer that is not a square, then $\sqrt{n}$ is irrational.

> **8.12** Try to formulate and prove an even more general theorem about the irrationality of the numbers $\sqrt[8]{n}$.

## On the set of primes

The following theorem was also known to Euclid.

**Theorem 8.3.**

There are infinitely many primes.

What we need to do is to show that for every positive integer $n$, there is a prime number larger than $n$. To this end, consider the number $n!+1$, and any prime divisor $p$ of it. We show that $p>n$. Again, we use an indirect proof, supposing that $p\leq n$ and deriving a contradiction. If $p\leq n$ then $p|n!$, since it is one of the integers whose product is $n!$. We also know that $p|n!+1$, and so $p$ is a divisor of the difference $(n!+1)-n!=1$. But this is impossible, and thus $p$ must be larger than $n$.

If we look at various charts or tables of primes, our main impression is that there is a lot of irregularity in them. For example, figure 11 represents each prime up to 200 by a bar. We see large “gaps” and then we also see primes that are very close. We can prove that these gaps get larger and larger as we consider larger and larger numbers; somewhere out there is a string of 100 consecutive composite numbers, somewhere (much farther away) there is a string of a 1000, etc. To state this in a mathematical form:

**Theorem 8.4.**

For every positive integer $k$, there exist $k$ consecutive composite integers.

We can prove this theorem by an argument quite similar to the proof of theorem 8.3. Let $n=k+1$ and consider the numbers

$n!+2,\;n!+3,\;\ldots,\;n!+n.$

Can any of these be a prime? The answer is no: the first number is even, since $n!$ and 2 are both even. The second number is divisible by 3, since $n!$ and 3 are both divisible by 3 (assuming that $n>2$). In general $n!+i$ is divisible by $i$, for every $i=2,3,\ldots,n$. Hence these numbers cannot be primes, and so we have found $n-1=k$ consecutive composite numbers.

What about the opposite question, finding primes very close to each other? Since all primes except 2 are odd, the difference of two primes must be at least two, except for 2 and 3. Two primes whose difference is 2 are called *twin primes*. Thus $(3,5)$, $(5,7)$, $(11,13)$, $(17,19)$ are twin primes. Looking at the table of the first 500 primes, we find many twin primes; extensive computation shows that there are twin primes with hundreds of digits. However, it is not known whether there are infinitely many twin primes! (Almost certainly there are, but no proof of this fact has been found, in spite of the efforts of many mathematicians for over 2000 years!)

Another way of turning Theorem 8.4 around: how large can be these gaps? Could it happen that there is no prime at all with, say, 100 digits? This is again a very difficult question, but here we do know the answer. (No, this does not happen.)

One of the most important questions about primes is: how many primes are there up to a given number $n$? We denote the number of primes up to $n$ by $\pi(n)$. Figure 12 illustrates the graph of this function in the range of 1 to 100, and Figure 13, in the range of 1 to 2000. We can see that the function grows reasonably smoothly, and that its slope decreases slowly. An exact formula for $\pi(n)$ is certainly impossible to obtain. Around the turn of the century, a powerful result called the Prime Number Theorem was proved by two French mathematicians, Hadamard and de la Vallée-Poussin. From this result it follows that

<!-- carousel -->
![Figure 12: The graph of $\pi(n)$ from 1 to 100](08 - Integers divisors and primes_images/img-1.jpeg)
![Figure 13: The graph of $\pi(n)$ from 1 to 2000](08 - Integers divisors and primes_images/img-2.jpeg)
<!-- endcarousel -->

we can find prime numbers with a prescribed number of digits, and up to a third of the digits also prescribed. For example, there exist prime numbers with 30 digits starting with 1234567890.

**Theorem 8.5 (The Prime Number Theorem).**

Let $\pi(n)$ denote the number of primes among $1,2,\ldots,n$. Then

$\pi(n)\sim\frac{n}{\ln n}$

(Here $\ln n$ means the “natural logarithm”, i.e., logarithm to the base $e=2.718281\ldots$. Also recall that the notation means that

$\frac{\pi(n)}{\frac{n}{\ln n}}$

will be arbitrarily close to 1 if $n$ is sufficiently large.)

The proof of the prime number theorem is very difficult; the fact that the number of primes up to $n$ is about $n/\ln n$ was observed empirically in the $18^{\text{th}}$ century, but it took more than 100 years until Hadamard and de la Vallée-Poussin proved it in 1896.

As an illustration of the use of this theorem, let us find the answer to a question that we have posed in the introduction: how many primes with (say) 200 digits are there? We get the answer by subtracting the number of primes up to $10^{199}$ from the number of primes up to $10^{200}$. By the Prime Number Theorem, this number is about

$\frac{10^{200}}{200\ln 10}-\frac{10^{199}}{199\ln 10}\approx 1.95\cdot 10^{197}.$

This is a lot of primes! Comparing this with the total number of positive integers with 200 digits, which we know is $10^{200}-10^{199}=9\cdot 10^{199}$, we get

$\frac{9\cdot 10^{199}}{1.95\cdot 10^{197}}\approx 460.$

Thus among the integers with 200 digits, one in every 460 is a prime.

We can verify this whole thread of the chapter at once with **sympy** — the unique factorization of Theorem 8.1, the "common primes, smaller exponent" gcd recipe, the $\sqrt 2$ irrationality argument of Theorem 8.2 (the exponent of $2$ in $2b^2$ is always odd, so it can never equal a perfect square), and this Prime Number Theorem density estimate. `factorint` recovers $300=2^2\cdot 3\cdot 5^2$ and $18=2\cdot 3^2$ and rebuilds $\gcd(300,18)=2\cdot 3=6$, then the script evaluates the same "one in every $460$" density we just derived (and the "one in about $2.3k$" rule for $k$-digit numbers).

```python
<!-- include: code/dm/08 - Integers divisors and primes/01_python.py -->
```

Running it prints `300 = 2^2 * 3^1 * 5^2`, `gcd(300,18) via shared prime powers = 6`, and `density 1 in 461  (book: ~460)`, confirming the factorizations, the prime-power gcd recipe, and the $200$-digit prime density all match the chapter. (The book's $18=2\cdot 3^3$ in the gcd example is a source typo; $2\cdot 3^2=18$, which the code computes correctly.)

(Warning: This argument is not precise; the main source of concern is that in the prime number theorem, we only stated the $\pi(n)$ is close to $n/\ln n$ if $n$ is sufficiently large. One can say more about how large $n$ has to be to have, say, an error less than 1 percent, but this leads to even more difficult questions, which are even today not completely resolved.)

There are many other simple observations one can make by looking at tables of primes, but they tend to be very difficult and most of them are not resolved even today, in some cases after 2,500 years of attempts. We have already mentioned the problem whether there are infinitely many twin primes.

Another famous unsolved problem is *Goldbach’s conjecture*. This states that every even integer larger than 2 can be written as the sum of two primes. (Goldbach also formulated a conjecture about odd numbers: every odd integer larger than 5 can be written as the sum of three primes. This conjecture was essentially proved, using very deep methods, by Vinogradov in the 1930’s. We said “essentially” since the proof only works for numbers that are very large, and the possibility of a finite number of exceptions remains open.)

Suppose that we have an integer  $n$  and want to know how soon after  $n$  can we be sure to find a prime. For example, how small, or large, is the first prime with at least 100 digits? Our proof of the infinity of primes gives that for every  $n$ , there is a prime between  $n$  and  $n! + 1$ . This is a very weak statement; it says for example that there is a prime between 10 and  $10! + 1 = 3628801$ , while of course the next prime is 11. Chebyshev proved in the last century that there is always a prime between  $n$  and  $2n$ . It is now proved that there is always a prime between two consecutive cubes (say, between  $27 = 3^3$  and  $64 = 4^3$ ). But it is another old and famous unsolved problem whether there is always a prime between two consecutive squares. (Try this out: you'll in fact find many primes. For example, between  $100 = 10^2$  and  $121 = 11^2$  we find 101, 103, 107, 109, 113. Between  $100^2 = 10,000$  and  $101^2 = 10201$  we find 10007, 10009, 10037, 10039, 10061, 10067, 10069, 10079, 10091, 10093, 10099, 10103, 10111, 10133, 10139, 10141, 10151, 10159, 10163, 10169, 10177, 10181, 10193.)

![P. L. Chebyshev](08 - Integers divisors and primes_images/img-3.jpeg)

> **8.13** Show that among k-digit numbers, one in about every  $2.3k$  is a prime.

## Fermat's "Little" Theorem

Primes are important because we can compose every integer from them; but it turns out that they also have many other, often surprising properties. One of these was discovered by the French mathematician Pierre de Fermat (1601-1655), now called the "Little" Theorem of Fermat.

**Theorem 8.6.** If  $p$  is a prime and  $a$  is an integer, then  $p|a^p - a$ .

To prove this theorem, we need a lemma, which states another divisibility property of primes (but is easier to prove):

**Lemma 8.1.** If  $p$  is a prime and  $1 < k < p$ , then  $p| \binom{p}{k}$ .

Proof. We know by theorem 4.2 that

$$
\binom{p}{k} = \frac{p(p-1)\cdot\ldots\cdot(p-k+1)}{k(k-1)\cdot\ldots\cdot 1}.
$$

Here  $p$  divides the numerator, but not the denominator, since all factors in the denominator are smaller than  $p$ , and we know by exercise 8.3(a) that if a prime  $p$  does not divide any of these factors, then it does not divide the product. Hence it follows (see exercise 8.3(b)) that  $p$  is a divisor of  $\binom{p}{k}$ .

![P. de Fermat](08 - Integers divisors and primes_images/img-4.jpeg)

Now we can prove Fermat's Theorem by induction on  $a$ . The assertion is trivially true if  $a = 0$ . Let  $a > 0$ , and write  $a = b + 1$ . Then

$$
\begin{aligned}
a^{p} - a
  &= (b+1)^{p} - (b+1)
   = b^{p} + \binom{p}{1} b^{p-1} + \ldots + \binom{p}{p-1} b + 1 - b - 1\\
  &= \left(b^{p} - b\right) + \binom{p}{1} b^{p-1} + \ldots + \binom{p}{p-1} b.
\end{aligned}
$$

Here the expression  $b^{p} - b$  in parenthesis is divisible by  $p$  by the induction hypothesis, while the other terms are divisible by  $p$  by lemma 8.1. It follows that  $a^{p} - a$  is also divisible by  $p$ , which completes the induction.

Let us make a remark about the history of mathematics here. Fermat is most famous for his "Last" theorem, which is the following assertion:

If  $n > 2$ , then the sum of the  $n$ -th powers of two positive integers is never the  $n$ -th power of a positive integer.

(The assumption that  $n > 2$  is essential: there are many examples of two squares whose sum is a third square: for example,  $3^2 + 4^2 = 5^2$ , or  $5^2 + 12^2 = 13^2$ .)

Fermat claimed in a note that he proved this, but never wrote down the proof. This statement remained perhaps the most famous unsolved problem in mathematics until 1995, when Andrew

Wiles (in one part with the help of Robert Taylor) finally proved it.

![A.J. Wiles](08 - Integers divisors and primes_images/img-6.jpeg)

> **8.14** Show by examples that neither the assertion in lemma 8.1 nor Fermat's Little Theorem remain valid if we drop the assumption that  $p$  is a prime.
> **8.15** Consider a regular  $p$ -gon, and all  $k$ -subsets of the set of its vertices, where  $1 \leq k \leq p-1$ . Put all these  $k$ -subsets into a number of boxes: we put two  $k$ -subsets into the same box if they can be rotated into each other. For example, all  $k$ -subsets consisting of  $k$  consecutive vertices will belong to one and the same box.
>
> (a) Prove that if  $p$  is a prime, then each box will contain exactly  $p$  of these sets.
> (b) Show by an example that (a) does not remain true if we drop the assumption that  $p$  is a prime.
> (c) Use (a) to give a new proof of Lemma 8.1.

> **8.16** Imagine numbers written in base  $a$ , with at most  $p$  digits. Put two numbers in the same box if they arise by cyclic shift from each other. How many will be in each class? Give a new proof of Fermat's theorem this way.

> **8.17** Give a third proof of Fermat's "Little Theorem" based on exercise 8.3.

[Hint: consider the product $a(2a)(3a)\ldots ((p - 1)a)$.]

## The Euclidean Algorithm

So far, we have discussed several notions and results concerning integers. Now we turn our attention to the question of how to do computations in connection with these results. How to decide whether or not a given number is a prime? How to find the prime factorization of a number?

We can do basic arithmetic: addition, subtraction, multiplication, division with remainder efficiently, and will not discuss this here.

The key to a more advanced algorithmic number theory is an algorithm that computes the greatest common divisor of two positive integers $a$ and $b$. This is defined as the largest positive integer that is a divisor of both of them. (Since $1$ is always a common divisor, and no common divisor is larger than either integer, this definition makes sense.) We say that two integers are relatively prime if their greatest common divisor is $1$. The greatest common divisor of $a$ and $b$ is denoted by $\gcd(a,b)$. Thus

$\gcd(1,6)=1,\qquad\gcd(2,6)=2,\qquad\gcd(3,6)=3,\qquad\gcd(4,6)=2,$
$\gcd(5,6)=1,\qquad\gcd(6,6)=6.$

Two numbers whose greatest common divisor is $1$ are called relatively prime. It will be convenient to also define $\gcd(a,0)=a$ for every $a\geq 0$.

A somewhat similar notion is the least common multiple of two integers, which is the least positive integer that is a multiple of both integers, and denote by $\operatorname{lcm}(a,b)$. For example,

$\operatorname{lcm}(1,6)=6,\qquad\operatorname{lcm}(2,6)=6,\qquad\operatorname{lcm}(3,6)=6,\qquad\operatorname{lcm}(4,6)=12,$
$\operatorname{lcm}(5,6)=30,\qquad\operatorname{lcm}(6,6)=6$

The greatest common divisor of two positive integers can be found quite simply by using their prime factorizations: look at the common prime factors, raise them to the smaller of the two exponents, and take the product of these prime powers. For example, $300=2^{2}\cdot 3\cdot 5^{2}$ and $18=2\cdot 3^{3}$, and hence $\gcd(300,18)=2\cdot 3=6$.

The trouble with this method is that it is very difficult to find the prime factorization of large integers. The algorithm to be discussed in this section will compute the greatest common divisor of two integers in a much faster way, without finding their prime factorization. This algorithm is an important ingredient of almost all other algorithms involving computation with integers. (And, as we see it from its name, it goes back to the great Greek mathematicians!)

> **8.18** Show that if $a$ and $b$ are positive integers with $a|b$, then $\gcd(a,b)=a$.

> **8.19** (a) $\gcd(a,b)=\gcd(a,b-a)$.
>
> (b) Let $r$ be the remainder if we divide $b$ by $a$. Then $\gcd(a,b)=\gcd(a,r)$.

> **8.20** (a) If $a$ is even and $b$ is odd, then $\gcd(a,b)=\gcd(a/2,b)$.
>
> (b) If both $a$ and $b$ are even, then $\gcd(a,b)=2\gcd(a/2,b/2)$.

> **8.21** How can you express the least common multiple of two integers, if you know the prime factorization of each?

> **8.22** Suppose that you are given two integers, and you know the prime factorization of one of them. Describe a way of computing the greatest common divisor of these numbers.

> **8.23** Prove that for any two integers $a$ and $b$,
>
> $\gcd(a,b)\operatorname{lcm}(a,b)=ab.$

Now we turn to Euclid’s Algorithm. Let $a$ and $b$ be two positive integers, and suppose that $a<b$. The algorithm is based on two simple facts, already familiar as exercises 8.6 and 8.6.

Suppose that we are given two positive integers $a$ and $b$, and we want to find their g.c.d. Here is what we do:

1. If $a>b$ then we interchange $a$ and $b$.

2. If $a>0$, divide $b$ by $a$, to get a remainder $r$. Replace $b$ by $r$ and return to $1$.

3. Else (if $a=0$), return $b$ as the g.c.d. and halt.

When you carry out the algorithm, especially by hand, there is no reason to interchange $a$ and $b$ if $a<b$: we can simply divide the larger number by the smaller (with remainder), and replace the larger number by the remainder if the remainder is not $0$. Let us do some examples.

$\gcd(300,18)$ $=$ $\gcd(12,18)=\gcd(12,6)=6.$
$\gcd(101,100)$ $=$ $\gcd(1,100)=1.$
$\gcd(89,55)$ $=$ $\gcd(34,55)=\gcd(34,21)=\gcd(13,21)=\gcd(13,8)=\gcd(5,8)$
$=$ $\gcd(5,3)=\gcd(2,3)=\gcd(2,1)=1.$

You can check in each case (using a prime factorization of the numbers) that the result is indeed the g.c.d.

If we describe an algorithm, the first thing to worry about is whether it terminates at all. So why is the euclidean algorithm finite? This is easy: the numbers never increase, and one of them decreases any time step 2 is executed, so it cannot last infinitely long.

Then of course we have to make sure that our algorithm yields what we need. This is clear: step 1 (interchanging the numbers) trivially does not change the g.c.d., step 3 (replacing the larger number by the remainder of a division) does not change the g.c.d. by exercise 8.6(b). And when we halt at step 2, the number returned is indeed the g.c.d. of the two current numbers by exercise 8.6.

A third, and more subtle, question you should ask when designing an algorithm: how long does it take? How many steps will it make before it terminates? We can get a bound from the argument that proves finite termination: since one or the other number decreases any time the 1-2 loop is executed, it will certainly halt in less than $a+b$ iterations. This is really not a great time bound: if we apply the euclidean algorithm to two numbers with 100 digits, then it says that it will not last longer than $2\cdot 10^{100}$ steps, which is astronomical and therefore useless. But this is only a most pessimistic bound; the examples seem to show that the algorithm terminates much faster than this.

But the examples also suggest that question is quite delicate. We see that the euclidean algorithm may be quite different in length, depending on the numbers in question. Some of the possible observations made from this examples are contained in the following exercises.

> **8.24** Show that the euclidean algorithm can terminate in two steps for arbitrarily large positive integers, even if their g.c.d. is 1.

> **8.25** Describe the euclidean algorithm applied to two consecutive Fibonacci numbers. Use your description to show that the euclidean algorithm can last arbitrarily many steps.

So what can we say about how long does the euclidean algorithm last? The key to the answer is the following lemma:

**Lemma 8.2.**

During the execution of the euclidean algorithm, the product of the two current numbers drops by a factor of two in each iteration.

To see that this is so, consider the step when the pair $(a,b)$ $(a<b)$ is replaced by the pair $(r,a)$, where $r$ is the remainder of $b$ when divided by $a$. Then we have $r<a$ and hence $b\geq a+r>2r$. Thus $ar<\frac{1}{2}ab$ as claimed.

Suppose that we apply the euclidean algorithm to two numbers $a$ and $b$ and we make $k$ steps. It follows by Lemma 8.2 that after the $k$ steps, the product of the two current numbers will be at most $ab/2^{k}$. Since this is at least 1, we get that

$ab\geq 2^{k},$

and hence

$k\leq\log_{2}(ab)=\log_{2}a+\log_{2}b.$

Thus we have proved the following.

**Theorem 8.7.**

The number of steps of the euclidean algorithm, applied to two positive integers $a$ and $b$, is at most $\log_{2}a+\log_{2}b$.

We have replaced the sum of the numbers by the sum of the logarithms of the numbers in the bound on the number of steps, which is a really substantial improvement. For example, the number of iterations in computing the g.c.d. of two 300-digit integers is less than $2\log_{2}10^{300}=600\log_{2}10<2000$. Quite a bit less than our first estimate of $10^{100}$. Note that $\log_{2}a$ is less than the number of bits of $a$ (when written in base 2), so we can say that the euclidean algorithm does not take more iterations than the number of bits needed to write down the numbers in base 2.

The theorem above gives only an upper bound on the number of steps the euclidean algorithm takes; we can be much more lucky: for example, when we apply the euclidean algorithm to two consecutive integers, it takes only one step. But sometimes, one cannot do much better. If you did exercise 8.6, you saw that when applied to two consecutive Fibonacci numbers $F_{k}$ and $F_{k+1}$, the euclidean algorithm takes $k-1$ steps. On the other hand, the lemma above gives the bound

$\log_{2}F_{k}+\log_{2}F_{k+1}\approx\log_{2}\left(\frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^{k}\right)+\log_{2}\left(\frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^{k+1}\right)$
$=-\log_{2}5+(2k+1)\log_{2}\left(\frac{1+\sqrt{5}}{2}\right)\approx 1.388k-1.628,$

so we have overestimated the number of steps only by a factor of about 1.388.

Fibonacci numbers are not only good to give examples of large numbers for which we can see how the euclidean algorithm works; they are also useful in obtaining an even better bound on the number of steps. We state the result as an exercise. Its contents is that, in a sense, the euclidean algorithm is longest on two consecutive Fibonacci numbers.

> **8.26** Suppose that $a<b$ and the euclidean algorithm applied to $a$ and $b$ takes $k$ steps. Prove that $a\geq F_{k}$ and $b\geq F_{k+1}$.

> **8.27** Consider the following version of the euclidean algorithm to compute $\gcd(a,b)$: (1) swap the numbers if necessary to have $a\leq b$; (2) if $a=0$, then return $b$; (3) if $a\neq 0$, then replace $b$ by $b-a$ and go to (1).
>
> (a) Carry out this algorithm to compute $\gcd(19,2)$.
>
> (b) Show that the modified euclidean algorithm always terminates with the right answer.
>
> (c) How long does this algorithm take, in the worst case, when applied to two 100-digit integers?

> **8.28** Consider the following version of the euclidean algorithm to compute $\gcd(a,b)$. Start with computing the largest power of 2 dividing both $a$ and $b$. If this is $2^{r}$, then divide $a$ and $b$ by $2^{r}$. After this “preprocessing”, do the following:
>
> (1) Swap the numbers if necessary to have $a\leq b$.
>
> (2) If $a\neq 0$, then check the parities of $a$ and $b$; if $a$ is even, and $b$ is odd, then replace $a$ by $a/2$; if both $a$ and $b$ are odd, then replace $b$ by $b-a$; in each case, go to (1).
>
> (3) if $a=0$, then return $2^{r}b$ as the g.c.d.
>
> Now come the exercises:
>
> (a) Carry out this algorithm to compute $\gcd(19,2)$.
>
> (b) It seems that in step (2), we ignored the case when both $a$ and $b$ are even. Show that this never occurs.
>
> (c) Show that the modified euclidean algorithm always terminates with the right answer.
>
> (d) Show that this algorithm, when applied to two 100-digit integers, does not take more than 1500 iterations.

The Euclidean Algorithm gives much more than just the g.c.d. of the two numbers. The main observation is that if we carry out the Euclidean Algorithm to compute the greatest common divisor of two positive integers $a$ and $b$, all the numbers we produce along the computation can be written as the sum of an integer multiple of $a$ and an integer multiple of $b$. Indeed, suppose that this holds for two numbers consecutive numbers we computed, so that one is $a^{\prime}=am+bn$, and the other is $b^{\prime}=ak+bl$, where $m,n,k,l$ are integers (not necessarily positive). Then in the next steps we compute (say) the remainder of $b^{\prime}$ modulo $a^{\prime}$, which is

$a^{\prime}-qb^{\prime}=(am+bn)-q(ak+bl)=a(m-qk)+b(n-ql),$

which is of the right form again.

In particular, we get the following:

**Theorem 8.8.**

Let $d$ be the greatest common divisor of the integers $a$ and $b$. Then $d$ can be written in the form

$d=am+bn$

where $m$ and $n$ are integers.

By maintaining the representation of integers in the form $an+bm$ during the computation, we see that the expression for $d$ in the theorem not only exists, but it is easily computable.

The book states Euclid's algorithm and Theorems 8.7 and 8.8 but verifies them only on examples; **Hypothesis** lets us check them as "for all inputs" guarantees. A hand-written `euclid_gcd` and `ext_gcd` are checked against `math.gcd` over hundreds of random pairs up to $10^{12}$: the algorithm always agrees with the trusted gcd, the extended version always returns integers with $am+bn=d$ exactly, and the step count never exceeds the $\log_2 a+\log_2 b$ bound of Theorem 8.7. A trace test reproduces the book's reductions $\gcd(300,18)=\gcd(12,18)=\gcd(12,6)=6$ and the long Fibonacci chain $\gcd(89,55)=\gcd(34,55)=\gcd(34,21)=\cdots=1$.

```python
<!-- include: code/dm/08 - Integers divisors and primes/02_python.py -->
```

Running it prints `4 passed` and (from the main block) `ext_gcd(300,18): d=6, m=-1, n=17  ->  300*-1+18*17 = 6`, confirming the algorithm matches `math.gcd` on every generated input and that Bézout's identity $300\cdot(-1)+18\cdot 17=6$ holds.

## Testing for primality

Returning to a question proposed in the introduction of this chapter: how do you decide about a positive integer $n$ whether it is a prime? You can try to see if $n$ can be divided, without remainder, by any of the smaller integers (other than 1). This is, however, a very clumsy and inefficient procedure! To determine this way whether a number with 20 digits is a prime would take astronomical time.

You can do a little better by noticing that it is enough to try to divide $n$ by the positive integers less than $\sqrt{n}$ (since if $n$ can be written as the product of two integers larger than 1, then one of these integers will necessarily be less than $\sqrt{n}$). But this method is still hopelessly slow if the number of digits goes above 20.

A much more promising approach is offered by Fermat’s “Little” Theorem. Its simplest nontrivial case says that if $p$ is a prime, then $p|2^{p}-2$. If we assume that $p$ is odd (which only excludes the case $p=2$), then we also know that $p|2^{p-1}-1$.

What happens if we check the divisibility relation $n|2^{n-1}-1$ for composite numbers? It obviously fails if $n$ is even (no even number is a divisor of an odd number), so let’s restrict our attention to odd numbers. Here are some results:

$9\not|2^{8}-1=255,\qquad 15\not|2^{14}-1=16,383,\qquad 21\not|2^{20}-1=1,048,575,$
$25\not|2^{24}-1=16,777,215.$

This suggests that perhaps we could test whether or not the number $n$ is a prime by checking whether or not the relation $n|2^{n-1}-1$ holds. This is a nice idea, but it has several major shortcomings.

First, it is easy to write up the formula $2^{n-1}-1$, but it is quite a different matter to compute it! It seems that to get $2^{n-1}$, we have to multiply $n-2$ times by 2. For a 100 digit number, this is about $10^{100}$ steps, which we will never be able to carry out.

But, we can be tricky when we compute $2^{n-1}$. Let us illustrate this on the example of $2^{24}$: we could start with $2^{3}=8$, square it to get $2^{6}=64$, square it again to get $2^{12}=4096$, and square it once more to get $2^{24}=16,777,216$. Instead of 23 multiplications, we only needed 5.

It seems that this trick only worked because 24 was divisible by such a large power of 2, and we could compute $2^{24}$ by repeated squaring, starting from a small number. So let us show how to do a similar trick if the exponent is a less friendly integer. Let us compute, say, $2^{29}$:

$2^{2}=4,2^{3}=8,2^{6}=64,2^{7}=128,2^{14}=16,384,2^{28}=268,435,456,2^{29}=536,870,912.$

It is perhaps best to read this sequence backwards: if we have to compute an odd power of 2, we obtain it by multiplying the previous power by 2; if we have to compute an even power, we obtain it by squaring the appropriate smaller power.

> **8.29** Show that if $n$ has $k$ bits in base 2, then $2^{n}$ can be computed using less than $2k$ multiplications.

Thus we have shown how to overcome the first difficulty; but the computations we did above reveal the second: the numbers grow too large! Let’s say that $n$ has 100 digits; then $2^{n-1}$ is not only astronomical: the number of its digits is astronomical. We could never write it down, let alone check whether it is divisible by $n$.

The way out is to divide by $n$ as soon as we get any number that is larger than $n$, and just work with the remainder of the division. For example, if we want to check whether $25|2^{24}-1$, then we have to compute $2^{24}$. As above, we start with computing $2^{3}=8$, then square it to get $2^{6}=64$. We immediately replace it by the remainder of the division $64:25$, which is 14. Then we compute $2^{12}$ by squaring $2^{6}$, but instead we square 14 to get 196, which we replace by the remainder of the division $196:25$, which is 21. Finally, we obtain $2^{24}$ by squaring $2^{12}$, but instead we square 21 to get 441, and then divide this by 25 to get the remainder 16. Since $16-1=15$ is not divisible by 25, it follows that 25 is not a prime.

This does not sound like an impressive conclusion, considering the triviality of the result, but this was only an illustration. If $n$ has $k$ bits in base 2, then as we have seen, it takes only $2k$ multiplications to compute $2^{n}$, and all we have to do is one division (with remainder) in each step to keep the numbers small. We never have to deal with numbers larger than $n^{2}$. If $n$ has 100 digits, then $n^{2}$ has 199 or 200 — not much fun to multiply by hand, but quite easily manageable by computers.

But here comes the third shortcoming of the primality test based on Fermat’s Theorem. Suppose that we carry out the test for a number $n$. If it fails (that is, $n$ is not a divisor of $2^{n-1}-1$), then of course we know that $n$ is not a prime. But suppose we find that $n|2^{n-1}-1$. Can we conclude that $n$ is a prime? Fermat’s Theorem certainly does not justify this conclusion. Are there composite numbers $n$ for which $n|2^{n-1}-1$? Unfortunately, the answer is yes. The smallest such number is $341=11\cdot 31$.

Here is an argument showing that 341 is a pseudoprime, without using a computer. We start with noticing that 11 divides $2^{5}+1=33$, and that 31 divides $2^{5}-1=31$. Therefore $341=11\cdot 31$ divides $(2^{5}+1)(2^{5}-1)=2^{10}-1$. To finish, we invoke the result of exercise 8.1: it implies that $2^{10}-1$ is a divisor of $(2^{10})^{34}-1=2^{340}-1$.

Such numbers are sometimes called pseudoprimes (fake primes). While such numbers are quite rare (there are only 22 of them between 1 and 10,000), they do show that our primality test can give a “false positive”, and thus (in a strict mathematical sense) it is not a primality test at all.

Nevertheless, efficient primality testing is based on Fermat’s Theorem. Below we sketch how it is done; the mathematical details are not as difficult as in the case of, say, the Prime Number Theorem, but they do go beyond the scope of this book.

One idea that comes to rescue is that we haven’t used the full force of Fermat’s Theorem: we can also check that $n|3^{n}-3$, $n|5^{n}-5$, etc. These can be carried out using the same tricks as described above. And in fact already the first of these rules out the “fake prime” 341. Unfortunately, some pseudoprimes are worse than others; for example, the number

$561=3\cdot 11\cdot 17$ has the property that

$561|a^{561}-a$

for every integer $a$. These pseudoprimes are called Carmichael numbers, and it was believed that their existence kills every primality test based on Fermat’s theorem.

We can confirm this entire arc with **sympy** — Fermat's Little Theorem itself (Theorem 8.6, $p\mid a^p-a$ for every prime $p$ and integer $a$) and then exactly the failures just discussed. The script reproduces the divisor table above ($2^8-1=255$, $2^{14}-1=16{,}383$, $2^{20}-1=1{,}048{,}575$, $2^{24}-1=16{,}777{,}215$, none divisible by the corresponding odd composite), confirms that $341=11\cdot 31$ is the smallest base-$2$ Fermat pseudoprime (it divides $2^{340}-1$ yet is composite, while base $3$ exposes it), and verifies that $561=3\cdot 11\cdot 17$ is a Carmichael number with $561\mid a^{561}-a$ for *every* $a$ (Exercise 8.30).

```python
<!-- include: code/dm/08 - Integers divisors and primes/03_python.py -->
```

Running it prints `341 prime? False  but 341 | 2^340 - 1 ? True`, `561 | a^561 - a for ALL a in 0..560 : True`, and `base-2 Fermat pseudoprimes < 10000: 22 of them  (book says 22)`, confirming the pseudoprime $341$, the Carmichael number $561$, and the book's count of exactly $22$ pseudoprimes below $10{,}000$.

But in the late 70’s, M. Rabin and G. Miller found a very simple way to strengthen Fermat Theorem just a little bit, and thereby overcome the difficulty caused by Carmichael numbers. We illustrate the method on the example of 561. We use some high school math, namely the identity $x^{2}-1=(x-1)(x+1)$, to factor the number $a^{561}-a$:

$$
\begin{aligned}
a^{561}-a
  &= a(a^{560}-1) = a(a^{280}-1)(a^{280}+1) && (15)\\
  &= a(a^{140}-1)(a^{140}+1)(a^{280}+1) && (16)\\
  &= a(a^{70}-1)(a^{70}+1)(a^{140}+1)(a^{280}+1) && (17)\\
  &= a(a^{35}-1)(a^{35}+1)(a^{70}+1)(a^{140}+1)(a^{280}+1) && (18)
\end{aligned}
$$

Now suppose that 561 were a prime. Then by Fermat’s Theorem, it must divide $a^{561}-a$, whatever $a$ is (this in fact happens). Now if a prime divides a product, it divides one of the factors (exercise 8.3), and hence at least one of the relations

$561|a\qquad 561|a^{35}-1\qquad 561|a^{35}+1\qquad 561|a^{70}+1\qquad 561|a^{140}+1\qquad 561|a^{280}+1$

must hold. But already for $a=2$, none of these relations hold.

We can discharge this argument as a constraint with **z3**. The script first checks the factorization identity above and the Carmichael premise $561\mid 2^{561}-2$, then asks Z3 whether $561$ divides *any* of the six factors — i.e. whether some integer quotient $q_i$ makes $\text{factor}_i=561\,q_i$. Z3 returning `unsat` is a machine proof that no factor works, so $561$ cannot be prime.

```python
<!-- include: code/dm/08 - Integers divisors and primes/04_python.py -->
```

Running it prints `561 | 2^561 - 2 : True` and `Z3: does 561 divide at least one factor (a=2)? unsat`, with the six remainders `2, 262, 264, 167, 68, 2` all nonzero — confirming that $561$ divides none of the factors and is therefore exposed as composite, exactly as the Miller–Rabin argument claims.

The Miller-Rabin test is an elaboration of this idea. Given an odd integer $n>1$ that we want to test for primality. We choose an integer $a$ from the range $0\leq a\leq n-1$ at random, and consider $a^{n}-a$. We factor it as $a(a^{n-1}-1)$, and then go on to factor it, using the identity $x^{2}-1=(x-1)(x+1)$, as long as we can. Then we test that one of the factors must be divisible by $n$.

If the test fails, we can be sure that $n$ is not a prime. But what happens if it succeeds? Unfortunately, this can still happen even if $n$ is composite; but the crucial point is that this test gives a false positive with probability less than $1/2$ (remember we chose a random $a$).

Reaching a wrong conclusion half of the time does not sound good enough; but we can repeat the experiment several times. If we repeat it 10 times (with a new, randomly chosen $a$), the probability of a false positive is less than $2^{-10}<1/1000$ (since to conclude that $n$ is prime, all 10 runs must give a false positive, independently of each other). If we repeat the experiment 100 times, the probability of a false positive drops below $2^{-100}<10^{-30}$, which is astronomically small.

Thus this test, when repeated sufficiently often, tests primality with error probability that is much less than the probability of, say, hardware failure, and therefore it is quite adequate for practical purposes. It is widely used in programs like Maple or Mathematica and in cryptographic systems.

Suppose that we test a number $n$ for primality and find that it is composite. Then we would like to find its prime factorization. It is easy to see that instead of this, we could ask for less: for a decomposition of $n$ into the product of two smaller positive integers: $n=ab$.

If we have a method to find such a decomposition efficiently, then we can go on and test $a$ and $b$ for primality. If they are primes, we have found the prime factorization of $n$; if (say) $a$ is not a prime, we can use our method to find a decomposition of $a$ into the product of two smaller integers etc. Since $n$ has at most $\log_{2}n$ prime factors (exercise 8.3), we have to repeat this at most $\log_{2}n$ times (which is less than the number of its bits).

But, unfortunately (or fortunately? see the next chapter on cryptography) no efficient method is known to write a composite number as a product of two smaller integers. It would be very important to find an efficient factorization method, or to give a mathematical proof that no such method exists; but we don’t know what the answer is.

> **8.30** Show that $561|a^{561}-a$, for every integer $a$. [Hint: since $561=3\cdot 11\cdot 17$, it suffices to prove that $3|a^{561}-a$, $11|a^{561}-1$ and $17|a^{561}-a$. Prove these relations separately, using the method of the proof of the fact that $341|2^{340}-1$.]
