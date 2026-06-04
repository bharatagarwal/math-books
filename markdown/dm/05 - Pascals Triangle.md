## Pascal's Triangle

To study various properties of binomial coefficients, the following picture is very useful. We arrange all binomial coefficients into a triangular scheme: in the "zeroeth" row we put  $\binom{0}{0}$ , in the first row, we put  $\binom{1}{0}$  and  $\binom{1}{1}$ , in the second row,  $\binom{2}{0}$ ,  $\binom{2}{1}$  and  $\binom{2}{2}$  etc. In general, the  $n$ -th row contains the numbers  $\binom{n}{0}, \binom{n}{1}, \ldots, \binom{n}{n}$ . We shift these rows so that their midpoints match; this way we get a pyramid-like scheme, called the Pascal Triangle (named after the French mathematician and philosopher Blaise Pascal, 1623-1662). The Figure below shows only a finite piece of the Pascal Triangle.

We can replace each binomial coefficient by its numerical value, to get another version of Pascal's Triangle.

<!-- carousel -->
![The Pascal Triangle: each entry is the binomial coefficient $\binom{n}{k}$, with row $n$ holding $\binom{n}{0},\binom{n}{1},\ldots,\binom{n}{n}$.](05 - Pascals Triangle_images/img-0.jpeg)
![The same triangle with each binomial coefficient replaced by its numerical value.](05 - Pascals Triangle_images/img-1.jpeg)
<!-- endcarousel -->

> **5.1** Prove that the Pascal Triangle is symmetric with respect to the vertical line through its apex.
> **5.2** Prove that each row in the Pascal Triangle starts and ends with 1.

## Identities in the Pascal Triangle

Looking at the Pascal Triangle, it is not hard to notice its most important property: every number in it (other than the 1's on the boundary) is the sum of the two numbers immediately above it. This in fact is a property of the binomial coefficients you have already met: it translates into the relation

$$
\binom {n} {k} = \binom {n - 1} {k - 1} + \binom {n - 1} {k} \tag {5}
$$

(cf. exercise 4.2).

This property of the Pascal Triangle enables us to generate the triangle very fast, building it up row by row, using (5). It also gives us a tool to prove many properties of the binomial coefficients, as we shall see.

We can do exactly this with a few lines of **numpy** — pure additions, no factorials — and then read the row sum $=2^n$ (exercise 5.3) and the alternating sum $=0$ (which we are about to prove) straight off the rows the recurrence builds. It reproduces the book's numeric triangle, e.g. the interior $6=3+3$ in row $4$ ($1\;4\;6\;4\;1$):

```python
<!-- include: code/dm/05 - Pascals Triangle/01_python.py -->
```

Running it prints rows through $n=8$ (`n=4: [1, 4, 6, 4, 1]`, `n=8: [1, 8, 28, 56, 70, 56, 28, 8, 1]`) and the table `n=8: sum=256=2^8   alternating sum=0`, confirming that the recurrence-built rows obey $\sum_k\binom{n}{k}=2^n$ and $\sum_k(-1)^k\binom{n}{k}=0$ for $n\geq 1$.

As a first application, let us give a new solution of exercise 4.3. There the task was to prove the identity

$\binom{n}{0}-\binom{n}{1}+\binom{n}{2}-\binom{n}{3}\ldots+(-1)^{n}\binom{n}{n}=0,$

using the binomial theorem. Now we give a proof based on (5): we can replace $\binom{n}{0}$ by $\binom{n-1}{0}$ (both are just 1), $\binom{n}{1}$ by $\binom{n-1}{0}+\binom{n-1}{1}$, $\binom{n}{2}$ by $\binom{n-1}{1}+\binom{n-1}{2}$, etc. Thus we get the sum

$\binom{n-1}{0}-\left[\binom{n-1}{0}+\binom{n-1}{1}\right]+\left[\binom{n-1}{1}+\binom{n-1}{2}\right]-\left[\binom{n-1}{2}+\binom{n-1}{3}\right]+\ldots$

which is clearly 0, since the second term in each bracket cancels with the first term of the next.

This method gives more than just a new proof of an identity we already know. What do we get if we start the same way, adding and subtracting binomial coefficients alternatingly, but stop earlier? In formula, we take

$\binom{n}{0}-\binom{n}{1}+\binom{n}{2}-\binom{n}{3}\ldots+(-1)^{k}\binom{n}{k}.$

If we do the same trick as above, we get

$\binom{n-1}{0}-\left[\binom{n-1}{0}+\binom{n-1}{1}\right]+\left[\binom{n-1}{1}+\binom{n-1}{2}\right]-\ldots(-1)^{k}\left[\binom{n-1}{k-1}+\binom{n-1}{k}\right].$

Here again every term cancels except the last one; so the result is $(-1)^{k}\binom{n-1}{k}$.

There are many other surprising relations satisfied by the numbers in the Pascal Triangle. For example, let’s ask: what is the sum of squares of elements in each row?

Let’s experiment, by computing the sum of squares of elements in the first few rows:

$1^{2}$ $=$ $1,$
$1^{2}+1^{2}$ $=$ $2,$
$1^{2}+2^{2}+1^{2}$ $=$ $6,$
$1^{2}+3^{2}+3^{2}+1^{2}$ $=$ $20,$
$1^{2}+4^{2}+6^{2}+4^{2}+1^{2}$ $=$ $70.$

We may recognize these numbers as the numbers in the middle column of the Pascal triangle. Of course, only every second row contains an entry in the middle column, so the last value above, the sum of squares in row No. 4, is the middle element in row No. 8. So the examples above suggest the following identity:

$\binom{n}{0}^{2}+\binom{n}{1}^{2}+\binom{n}{2}^{2}+\ldots+\binom{n}{n-1}^{2}+\binom{n}{n}^{2}=\binom{2n}{n}.$ (6)

Of course, the few experiments above do not prove that this identity always holds, so we need a proof.

We will give an interpretation of both sides of the identity as the result of a counting problem; it will turn out that they count the same things, so they are equal. It is obvious what the right hand side counts: the number of subsets of size $n$ of a set of size $2n$. It will be convenient to choose, as our $2n$-element set, the set $S=\{1,2,\ldots,2n\}$.

The combinatorial interpretation of the left hand side is not so easy. Consider a typical term, say $\binom{n}{k}^{2}$. We claim that this is the number of those $n$-element subsets of $\{1,2,\ldots,2n\}$ that contain exactly $k$ elements from $\{1,2,\ldots,n\}$ (the first half of our set $S$). In fact, how do we choose such an $n$-element subset of $S$? We choose $k$ elements from $\{1,2,\ldots,n\}$ and then $n-k$ elements from $\{n+1,n+2,\ldots,2n\}$. The first can be done in $\binom{n}{k}$ ways; no matter which $k$-element subset of $\{1,2,\ldots,n\}$ we selected, we have $\binom{n}{n-k}$ ways of choosing the other part. Thus the number of ways to choose an $n$-element subset of $S$ having $k$ elements from $\{1,2,\ldots,n\}$ is

$\binom{n}{k}\cdot\binom{n}{n-k}=\binom{n}{k}^{2}$

(by the symmetry of the Pascal Triangle).

Now to get the total number of $n$-element subsets of $S$, we have to sum these numbers for all values of $k=0,1,\ldots,n$. This proves identity (6).

Where the few experiments above only checked finitely many rows, we can have **sympy** close the sum for a *symbolic* $n$: it evaluates $\sum_{k=0}^{n}\binom{n}{k}^2$ to the closed form $\Gamma(2n+1)/\Gamma(n+1)^2=\binom{2n}{n}$ — that is identity $(6)$ — and regenerates the experimental table $1,2,6,20,70$ as the middle entries $\binom{0}{0},\binom{2}{1},\binom{4}{2},\binom{6}{3},\binom{8}{4}$. For good measure it also evaluates $\sum_k\binom{n}{k}=2^n$ and checks the "stop earlier" result $\sum_{i=0}^{k}(-1)^i\binom{n}{i}=(-1)^k\binom{n-1}{k}$:

```python
<!-- include: code/dm/05 - Pascals Triangle/02_python.py -->
```

Running it prints `sum_{k=0}^{n} C(n,k)^2  -> sympy closes it as: gamma(2*n + 1)/gamma(n + 1)**2` and `sympy from the closed form:    [1, 2, 6, 20, 70]`, confirming identity $(6)$ symbolically and matching the chapter's $1,2,6,20,70$.

> **5.3** Give a proof of the formula in exercise 4.2
>
> $1+\binom{n}{1}+\binom{n}{2}+\ldots+\binom{n}{n-1}+\binom{n}{n}=2^{n}$
>
> along the same lines. (One could expect that, similarly as for the “alternating” sum, we could get a nice formula for the sum obtained by stopping earlier, like $\binom{n}{0}+\binom{n}{1}+\ldots+\binom{n}{k}$. But this is not the case: no simpler expression is known for this sum in general.)

> **5.4** By the Binomial Theorem, the right hand side in identity (6) is the coefficient of $x^{n}y^{n}$ in the expansion of $(x+y)^{2n}$. Write $(x+y)^{2n}$ in the form $(x+y)^{n}(x+y)^{n}$, expand both factors $(x+y)^{n}$ using the binomial theorem, and then try to figure out the coefficient of $x^{n}y^{n}$ in the product. Show that this gives another proof of identity (6).

> **5.5** Prove the following identity:
>
> $\binom{n}{0}\binom{m}{k}+\binom{n}{1}\binom{m}{k-1}+\binom{n}{2}\binom{m}{k-2}+\ldots+\binom{n}{k-1}\binom{m}{1}+\binom{n}{k}\binom{m}{0}=\binom{n+m}{k}$.
>
> You can use a combinatorial interpretation of both sides, similarly as in the proof of (6) above, or the Binomial Theorem as in the previous exercise.

Here is another relation between the numbers in the Pascal Triangle. Let us start with the last element in any row, and sum the elements moving down diagonally to the left. For example, starting with the last element in the second row, we get

$1$ $=$ $1,$
$1+3$ $=$ $4,$
$1+3+6$ $=$ $10,$
$1+3+6+10$ $=$ $20.$

These numbers are just the numbers in the next skew line of the table! If we want to put this in a formula, we get

$\binom{n}{0}+\binom{n+1}{1}+\binom{n+2}{2}+\ldots+\binom{n+k}{k}=\binom{n+k+1}{k}.$ (7)

To *prove* this identity, we use induction on $k$. If $k=0$, the identity just says $1=1$, so it is trivially true. (We can check it also for $k=1$, even though this is not necessary. Anyway, it says $1+n=n+1$.)

So suppose that the identity (7) is true for a given value of $k$, and we want to prove that it also holds for $k+1$ in place of $k$. In other words, we want to prove that

$\binom{n}{0}+\binom{n+1}{1}+\binom{n+2}{2}+\ldots+\binom{n+k}{k}+\binom{n+k+1}{k+1}=\binom{n+k+2}{k+1}.$

Here the sum of the first $k$ terms on the left hand side is $\binom{n+k+1}{k}$ by the induction hypothesis, and so the left hand side is equal to

$\binom{n+k+1}{k}+\binom{n+k+1}{k+1}.$

But this is indeed equal to $\binom{n+k+2}{k+1}$ by the fundamental property of the Pascal Triangle. This completes the proof by induction.

Here is a machine-checked version of exactly that induction. This **Lean 4** file defines $\binom{n}{k}$ *directly* by the Pascal recurrence and reproduces the proof step for step: base case $1=1$, step case using property $(5)$. Lean's kernel checks every line, and `#eval` reproduces the book's worked example — starting from the last entry of row $2$ and summing down-left gives $1,4,10,20$:

```lean
<!-- include: code/dm/05 - Pascals Triangle/04_lean.lean -->
```

The file type-checks with no errors (exit $0$) and its `#eval` prints `[1, 4, 10, 20]`, so the hockey-stick identity is now a formally verified theorem matching the chapter's diagonal example.

Having proved the major identities — the recurrence $(5)$, the row and alternating sums, the sum of squares $(6)$, and the diagonal sum $(7)$ — we can subject the whole collection to a different kind of evidence. **hypothesis** throws hundreds of random $(n,k)$ at each identity, exercising integer arithmetic directly (via `math.comb`, independent of the numpy construction above), trying to falsify them:

```python
<!-- include: code/dm/05 - Pascals Triangle/03_python.py -->
```

Running it prints `6 passed`, confirming all six identities survive randomized testing over $n,k$ up to a few hundred.

> **5.6** Suppose that you want to choose a $(k+1)$-element subset of the $(n+k+1)$-element set $\{1,2,\ldots,n+k+1\}$. You decide to do this by choosing first the largest element, then the rest. Show that counting the number of ways to choose the subset this way, you get a combinatorial proof of identity (7).

## A bird’s eye view at the Pascal Triangle

Let’s imagine that we are looking at the Pascal Triangle from a distance. Or, to put it differently, we are not interested in the exact numerical value of the entries, but rather in their order of magnitude, rise and fall, and other global properties. The first such property of the Pascal Triangle is its symmetry (with respect to the vertical line through its apex), which we already know.

Another property one observes is that along any row, the entries increase until the middle, and then decrease. If $n$ is even, there is a unique middle element in the $n$-th row, and this is the largest; if $n$ is odd, then there are two equal middle elements, which are largest.

So let us prove that the entries increase until the middle (then they begin to decrease by the symmetry of the table). We want to compare two consecutive entries:

$\binom{n}{k}\ ?\ \binom{n}{k+1}.$

If we use formula 4.2, we can write this as

$\frac{n(n-1)\ldots(n-k+1)}{k(k-1)\ldots 1}\ ?\ \frac{n(n-1)\ldots(n-k)}{(k+1)k\ldots 1}.$

There are a lot of common factors on both sides with which we can simplify. We get the really simple comparison

$1\ ?\ \frac{n-k}{k+1}.$

Rearranging, we get

$k\ ?\ \frac{n-1}{2}.$

So if $k<(n-1)/2$, then $\binom{n}{k}<\binom{n}{k+1}$; if $k=(n-1)/2$, then $\binom{n}{k}=\binom{n}{k+1}$ (this is the case of the two entries in the middle if $n$ is odd); and if $k>(n-1)/2$, then $\binom{n}{k}>\binom{n}{k+1}$.

It will be useful later that this computation also describes by how much consecutive elements increase or decrease. If we start from the left, the second entry $(n)$ is larger by a factor of $n$ than the first; the third $(n(n-1)/2)$ is larger by a factor of $(n-1)/2$ than the second. In general,

$\frac{\binom{n}{k+1}}{\binom{n}{k}}=\frac{n-k}{k+1}.$ (8)

> **5.7** For which values of $n$ and $k$ is $\binom{n}{k+1}$ twice the previous entry in the Pascal Triangle?

> **5.8** Instead of the ratio, look at the difference of two consecutive entries in the Pascal triangle:
>
> $\binom{n}{k+1}-\binom{n}{k}.$

For which value of $k$ is this difference largest?

We know that each row of the Pascal Triangle is symmetric. We also know that the entries start with $1$, raise to the middle, and then they fall back to $1$. Can we say more about their shape?

Figure 9 shows the graph of the numbers $\binom{n}{k}$ ($k=0,1,\ldots,n$) for the values $n=10$ and $n=100$. We can make several further observations.

— First, the largest number gets very large.

— Second, not only do these numbers increase to the middle and then they decrease, but that the middle ones are substantially larger than those at the beginning and end. For $n=100$, the figure only shows the range $\binom{100}{20},\binom{100}{21},\ldots,\binom{100}{80}$; the numbers outside this range are so small compared to the largest that they are negligible.

<!-- carousel -->
![Figure 9 (left): Graph of the  $n$ -th row of the Pascal Triangle, for  $n = 10$ .](05 - Pascals Triangle_images/img-2.jpeg)
![Figure 9 (right): Graph of the  $n$ -th row of the Pascal Triangle, for  $n = 100$  (only the range  $\binom{100}{20},\ldots,\binom{100}{80}$  is shown).](05 - Pascals Triangle_images/img-3.jpeg)
<!-- endcarousel -->

— Third, we can observe that the shape of the graph is quite similar for different values of  $n$ .

Let's look more carefully at these observations. For the discussions that follow, we shall assume that  $n$  is even (for odd values of  $n$ , the results would be quite similar, just one would have to word them differently). If  $n$  is even, then we know that the largest entry in the  $n$ -th row is the middle number  $\binom{n}{n/2}$ , and all other entries are smaller.

How large is the largest number in the  $n$ -th row of the Pascal Triangle? We know immediately an upper bound on this number:

$$
\binom{n}{n/2} < 2^{n},
$$

since  $2^n$  is the sum of all entries in the row. It only takes a little more sophistication to get a lower bound:

$$
\binom{n}{n/2} > \frac{2^{n}}{n + 1},
$$

since  $2^n / (n + 1)$  is the average of the numbers in the row, and the largest number is certainly at least as large as the average.

These bounds already give a pretty good idea about the size of  $\binom{n}{n/2}$ . Take, say,  $n = 500$ . Then we get

$$
\frac{2^{500}}{501} < \binom{500}{250} < 2^{500}.
$$

If we want to know, say, the number of digits of  $\binom{500}{250}$ , we just have to take the logarithm (in base 10) of it. From the bounds above, we get

$$
500 \lg 2 - \lg 501 < \lg \binom{500}{250} < 500 \lg 2.
$$

Since $\lg 501<3$, this inequality gives the number of digits with a very small error: if we guess that it is $(500\lg 2)-1$, rounded up (which is 150) then we are off by at most 2 (actually, 150 is the true value).

Using the Stirling Formula, one can get a much better approximation of this largest entry.

$\binom{n}{n/2}\sim\frac{2^{n}}{\sqrt{\pi n/2}}.$ (9)

> **5.9** (a) Give a combinatorial argument to show that $2^{n}>\binom{n}{4}$.
>
> (b) Use this inequality to show that $2^{n}>n^{3}$ if $n$ is large enough.

> **5.10** Show how to use the Stirling Formula to derive (9).

So we know that the largest entry in the $n$-th row of the Pascal triangle is in the middle, and we know approximately how large this element is. We also know that going either left or right, the elements begin to drop. How fast do they drop? We show that if we move away from the middle of the row, quite soon the numbers drop to less than a half of the maximum. (We pick this $1/2$ only for illustration; we shall see that one can estimate similarly how far away from the middle we have to move before the entries drop to a third, or to one percent, of the middle entry.) This quantifies our observation that the large binomial coefficients are concentrated in the middle of the row.

It is important to point out that in the arguments below, using calculus would give stronger results; we only give here as much as we can without appealing to calculus.

Again, we consider the case when $n$ is even; then we can write $n=2m$, where $m$ is a positive integer. The middle entry is $\binom{2m}{m}$. Consider the binomial coefficient that is $t$ steps before the middle: this is $\binom{2m}{m-t}$. We want to compare it with the largest coefficient. We shall choose the value of $t$ later; this way our calculations will be valid for any value of $t$ such that $0\leq t\leq m$, and so they will be applicable in different situations.

We already know that $\binom{2m}{m}>\binom{2m}{m-t}$; we also know by (8) that going left from $\binom{2m}{m}$, the entries drop by factors $\frac{m}{m+1}$, then by $\frac{m-1}{m+2}$, then by $\frac{m-2}{m+3}$, etc. The last drop is by a factor of $\frac{m-t+1}{m+t}$.

Multiplying these factors together, we get

$\binom{2m}{m-t}\left/\binom{2m}{m}\right.=\frac{m(m-1)\ldots(m-t+1)}{(m+1)(m+2)\ldots(m+t)}.$

So we have a formula for this ratio, but how do we know for which value does it become less than $1/3$? We could write up the inequality

$\frac{m(m-1)\ldots(m-t+1)}{(m+1)(m+2)\ldots(m+t)}<\frac{1}{2},$

and solve it for $t$ (as we did when we proved that the entries are increasing to the middle), but this would lead to inequalities that are too complicated to solve.

So we have to do some arithmetic trickery here. We start with looking at the reciprocal ratio:

$\binom{2m}{m}\bigg/\binom{2m}{m-t}=\frac{(m+1)(m+2)\ldots(m+t)}{m(m-1)\ldots(m-t+1)}.$ (10)

and write it in the following form:

$\frac{(m+t)(m+t-1)\ldots(m+1)}{m(m-1)\ldots(m-t+1)}=\frac{m+t}{m}\cdot\frac{m+t-1}{m-1}\cdot\ldots\cdot\frac{m+1}{m-t+1}$
$=\left(1+\frac{t}{m}\right)\cdot\left(1+\frac{t}{m-1}\right)\cdot\ldots\cdot\left(1+\frac{t}{m-t+1}\right).$

If we replace the numbers $m,m-1,\ldots,m-t+1$ in the denominator by $m$, we decrease the value of each factor and thereby the value of the whole product:

$\left(1+\frac{t}{m}\right)\cdot\left(1+\frac{t}{m-1}\right)\cdot\ldots\cdot\left(1+\frac{t}{m-t+1}\right)\geq\left(1+\frac{t}{m}\right)^{t}.$ (11)

It is still not easy to see how large this expression is; the base is close to $1$, but the exponent may be large. We can get a simpler expression if we use the Binomial Theorem and then retain just the first two terms:

$\left(1+\frac{t}{m}\right)^{t}=1+\binom{t}{1}\frac{t}{m}+\binom{t}{2}\left(\frac{t}{m}\right)^{2}+\ldots>1+\binom{t}{1}\frac{t}{m}=1+\frac{t^{2}}{m}.$

To sum up, we conclude that

**Theorem 5.1.**

For all integers $0\leq t\leq m$,

$\binom{2m}{m}\bigg/\binom{2m}{m-t}>1+\frac{t^{2}}{m}.$

Let us choose $t$ to be the least integer that is not smaller than $\sqrt{m}$ (in notation: $\lceil\sqrt{m}\rceil$). Then $t^{2}\geq m$, and we get the following:

$\binom{2m}{m-\lceil\sqrt{m}\rceil}<\frac{1}{2}\binom{2m}{m}.$

> **5.11** Find a number $c$ such that if $t>c\sqrt{m}$, then
>
> $\binom{2m}{m-t}<\frac{1}{100}\binom{2m}{m}.$

Consider, for example, the $500^{\text{th}}$ row. Since $\sqrt{500}=22.36\ldots$, it follows that the entry $\binom{500}{227}$ is less than half of the largest entry $\binom{500}{250}$. This argument only gives an upper bound on how far we have to go; it does not say that the entries closer to the middle are all larger than a third of the middle entry; in fact, the entry $\binom{500}{236}$ is already smaller than a $\frac{1}{2}\binom{500}{250}$, but the entry $\binom{500}{237}$ is larger.

Next we prove that even if we sum all entries outside a narrow range in the middle, we get a small fraction of the sum of all entries. (This fact will be very important when we will apply these results in probability theory.)

We need an inequality that is a generalization of the inequality in Theorem 5.1. We state is as a ”lemma”; this means an auxiliary result that may not be so interesting in itself, but will be important in proving some other theorem.

**Lemma 5.1.**

For all integers $0\leq t,s\leq m$ such that $t+s\leq m$,

$\binom{2m}{m-s}\bigg/\binom{2m}{m-t-s}>\frac{t^{2}}{m}.$

For $s=0$, this lemma says the same as Theorem 5.1. We leave the proof of it as an exercise.

> **5.12** (a) Prove Lemma 5.1, by following the proof of Theorem 5.1.
>
> (b) Show that Lemma 5.1 follows from Theorem 5.1, if one observes that as $s$ increases, the binomial coefficient $\binom{2m}{m-t-s}$ decreases faster than the binomial coefficient $\binom{2m}{m-s}$.
>
> (c) Show that by doing the calculations more carefully, the lower bound of $t^{2}/m$ in Lemma 5.1 can be improved to $1+t(2t+s)/m$.

Now we state the theorem about the sum of the “small” binomial coefficients.

**Theorem 5.2.**

Let $0\leq k\leq m$ and let $t=\lceil\sqrt{km}\rceil$. Then

$\binom{2m}{0}+\binom{2m}{1}+\ldots+\binom{2m}{m-t-1}<\frac{1}{2k}2^{2m}.$ (12)

To digest the meaning of this, choose $k=100$. The quantity $2^{2m}$ on the right hand side is the sum of all binomial coefficient in row No. $2m$ of the Pascal Triangle; so the theorem says that if we take the sum of the first $m-t$ (where $t=\lceil 10\sqrt{m}\rceil$) then we get less than half percent of the total sum. By the symmetry of the Pascal Triangle, the sum of the last $m-t$ entries in this row will be the same, so the $2t+1$ remaining terms in the middle make up $99$ percent of the sum.

To prove this theorem, let us compare the sum on the left hand side of (12) with the sum

$\binom{2m}{t}+\binom{2m}{t+1}+\ldots+\binom{2m}{m-1}.$ (13)

Let us note right away that the sum in (13) is clearly less than $2^{2m}/2$, since even if we add the mirror image of this part of the row of the Pascal Triangle, we get less than $2^{2m}$. Now for the comparison, we have

$\binom{2m}{m-t-1}\leq\frac{1}{k}\binom{2m}{m-1}$

by Lemma 5.1 (check the computation!), and

$\binom{2m}{m-t-2}<\frac{1}{k}\binom{2m}{m-2},$

and similarly, each term on the left hand side of (12) is less than a hundredth of the corresponding term in (13). Hence we get that

$$
\binom{2m}{0} + \binom{2m}{1} + \ldots + \binom{2m}{m-2t} < \frac{1}{k} \left( \binom{2m}{t} + \binom{2m}{t+1} + \ldots + \binom{2m}{m-t} \right) < \frac{1}{2k} 2^{2m}.
$$

This proves the theorem.
