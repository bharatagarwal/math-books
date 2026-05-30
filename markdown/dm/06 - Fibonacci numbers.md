## 6 Fibonacci numbers

## 6.1 Fibonacci’s exercise

In the $13^{\text{th}}$ century, the Italian mathematician Leonardo Fibonacci studied the following (not too realistic) exercise:

A farmer raises rabbits. Each rabbit gives birth to one rabbit when it turns 2 months old, and then to one rabbit each month. Rabbits never die, and we ignore hares. How many rabbits will the farmer have in the $n$-th month, if he starts with one newborn rabbit?

It is easy to figure out the answer for small values of $n$. He has 1 rabbit in the first month and 1 rabbit in the second month, since the rabbit has to be 2 months old before starting to reproduce. He has 2 rabbits during the third months, and 3 rabbits during the fourth, since his first rabbit delivered a new one after the second and one after the third. After 4 months, the second rabbit also delivers a new rabbit, so two new rabbits are added. This means that the farmer will have 5 rabbits during the fifth month.

It is easy to follow the multiplication of rabbits for any number of months, if we notice that the number of new rabbits added after $n$ months is just the same as the number of rabbits who are at least 2 months old, i.e., who were already there after during the $(k-1)$-st month. In other words, if we denote by $F_{n}$ the number of rabbits during the $n$-th month, then we have, for $n=2,3,4,\ldots$,

$F_{n+1}=F_{n}+F_{n-1}.$ (14)

We also know that $F_{1}=1$, $F_{2}=1$, $F_{3}=2$, $F_{4}=3$, $F_{5}=5$. It is convenient to define $F_{0}=0$; then equation (14) will remain valid for $n=1$ as well. Using the equation (14), we can easily determine any number of terms in this sequence of numbers:

$0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597\ldots$

The numbers in this sequence are called Fibonacci numbers.

We see that equation (14), together with the special values $F_{0}=0$ and $F_{1}=1$, uniquely determines the Fibonacci numbers. Thus we can consider (14), together with $F_{0}=0$ and $F_{1}=1$, as the definition of these numbers. This may seem as a somewhat unusual definition: instead of telling what $F_{n}$ is (say, by a formula), we just give a rule that computes each Fibonacci number from the two previous numbers, and specify the first two values. Such a definition is called a recurrence. It is quite similar in spirit to induction (except that it not a proof technique, but a definition method), and is sometimes also called definition by induction.

> **6.1** Why do we have to specify exactly two of the elements to begin with? Why not one or three?

Before trying to say more about these numbers, let us consider another counting problem:

A staircase has $n$ steps. You walk up taking one or two at a time. How many ways can you go up?

For $n=1$, there is only $1$ way. For $n=2$, you have $2$ choices: take one twice or two once. For $n=3$, you have $3$ choices: three single steps, or one single followed by one double, or one double followed by one single.

Now stop and try to guess what the answer is in general! If you guessed that the number of ways to go up on a stair with $n$ steps is $n$, you are wrong. The next case, $n=4$, gives $5$ possibilities ($1+1+1+1$, $2+1+1$, $1+2+1$, $1+1+2$, $2+2$).

So instead of guessing, let’s try the following strategy. We denote by $G_{n}$ the answer, and try to figure out what $G_{n+1}$ is, assuming we know the value of $G_{k}$ for $k\leq n$. If we start with a single step, we have $G_{n}$ ways to go up the remaining $n$ steps. If we start with a double step, we have $G_{n-1}$ ways to go up the remaining $n-1$ steps. Now these are all the possibilities, and so

$G_{n+1}=G_{n}+G_{n-1}.$

This equation is the same as the equation we have used to compute the Fibonacci numbers $F_{n}$. Does this means that $F_{n}=G_{n}$? Of course not, as we see by looking at the beginning values: for example, $F_{3}=2$ but $G_{3}=3$. However, it is easy to observe that all that happens is that the $G_{n}$ are shifted by one:

$G_{n}=F_{n+1}.$

This is valid for $n=1,2$, and then of course it is valid for every $n$ since the sequences $F_{2},F_{3},F_{4}\ldots$ and $G_{1},G_{2},G_{3},\ldots$ are computed by the same rule from their first two elements.

> **6.2** We have $n$ dollars to spend. Every day we either buy a candy for $1$ dollar, or an icecream for $2$ dollars. In how many ways can we spend the money?

## 6.2 Lots of identities

There are many interesting relations valid for the Fibonacci numbers. For example, what is the sum of the first $n$ Fibonacci numbers? We have

$0$ $=$ $0,$
$0+1$ $=$ $1,$
$0+1+1$ $=$ $2,$
$0+1+1+2$ $=$ $4,$
$0+1+1+2+3$ $=$ $7,$
$0+1+1+2+3+5$ $=$ $12,$
$0+1+1+2+3+5+8$ $=$ $20,$
$0+1+1+2+3+5+8+13$ $=$ $33.$

Staring at these numbers for a while, it is not hard to recognize that adding 1 to the right hand sides we get Fibonacci numbers; in fact, we get Fibonacci numbers two steps after the last summand. In formula:

$F_{0}+F_{1}+F_{2}+\ldots+F_{n}=F_{n+2}-1.$

Of course, at this point this is only a conjecture, an unproved mathematical statement we believe to be true. To prove it, we use induction on $n$ (since the Fibonacci numbers are defined by recurrence, induction is the natural and often only proof method at hand).

We have already checked the validity of the statement for $n=0$ and 1. Suppose that we know that the identity holds for the sum of the first $n-1$ Fibonacci numbers. Consider the sum of the first $n$ Fibonacci numbers:

$F_{0}+F_{1}+\ldots+F_{n}=(F_{0}+F_{1}+\ldots+F_{n-1})+F_{n}=(F_{n+1}-1)+F_{n},$

by the induction hypothesis. But now we can use the recurrence equation for the Fibonacci numbers, to get

$(F_{n+1}-1)+F_{n}=F_{n+2}-1.$

This completes the induction proof.

> **6.3** Prove that $F_{3n}$ is even.

> **6.4** Prove that $F_{5n}$ is divisible by 5.

> **6.5** Prove the following identities.
>
> (a) $F_{1}+F_{3}+F_{5}+\ldots+F_{2n-1}=F_{2n}$.
>
> (b) $F_{0}-F_{1}+F_{2}-F_{3}+\ldots-F_{2n-1}+F_{2n}=F_{2n-1}-1$.
>
> (c) $F_{0}^{2}+F_{1}^{2}+F_{2}^{2}+\ldots+F_{n}^{2}=F_{n}\cdot F_{n+1}$.
>
> (d) $F_{n-1}F_{n+1}-F_{n}^{2}=(-1)^{n}$.

> **6.6** Mark the first entry (a 1) of any row of the Pascal triangle. Move one step East and one step Northeast, and mark the entry there. Repeat this until you get out of the triangle. Compute the sum of the entries you marked.
>
> (a) What numbers do you get if you start from different rows? First ”conjecture”, than prove your answer.
>
> (b) Formulate this fact as an identity involving binomial coefficients.

> **6.7** Cut a chessboard into 4 pieces as shown in Figure 10 and assemble a $5\times 13$ rectangle from them. Does this prove that $5\cdot 13=8^{2}$? Where are we cheating? What does this have to do with Fibonacci numbers?

Rather than spot-check one or two of these identities, we can hand them to **hypothesis**, which throws hundreds of random $n$ (up to $400$, using exact big integers) at each claim. Only the recurrence is trusted; the prefix-sum identity $F_0+\dots+F_n=F_{n+2}-1$, Cassini's $F_{n-1}F_{n+1}-F_n^2=(-1)^n$ (6.5 d), the sum of squares $F_0^2+\dots+F_n^2=F_nF_{n+1}$ (6.5 c), and the odd-index sum $F_1+F_3+\dots+F_{2n-1}=F_{2n}$ (6.5 a) are all left as the claims under test:

```python
<!-- include: code/dm/06 - Fibonacci numbers/03_python.py -->
```

Running it prints `5 passed in 0.35s`, confirming all four identities hold across every generated case (alongside the seed check that $F_1..F_5 = 1,1,2,3,5$).

There is also a way to see Cassini's identity (6.5 d) structurally rather than by random testing. The recurrence is a single matrix step,
$$\begin{pmatrix}F_{n+1}\\F_n\end{pmatrix}=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}F_n\\F_{n-1}\end{pmatrix},$$
so by repeated multiplication $\begin{pmatrix}1&1\\1&0\end{pmatrix}^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$. Since $\det\!\begin{pmatrix}1&1\\1&0\end{pmatrix}=-1$, taking determinants of both sides gives $\det(M^n)=(-1)^n$, which *is* Cassini's identity $F_{n-1}F_{n+1}-F_n^2=(-1)^n$. We can let **numpy** raise that matrix to powers (in exact `object`-dtype integers) to recover the sequence and read the determinant off directly:

```python
<!-- include: code/dm/06 - Fibonacci numbers/04_python.py -->
```

Running it prints the sequence `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]`, the Cassini table (e.g. `n= 4:  2*5 - 3^2 =  1   (-1)^4 =  1`), and `F_100 = 354224848179261915075`, confirming the matrix recurrence reproduces the book's numbers and that the determinant yields Cassini exactly.

## 6.3 A formula for the Fibonacci numbers

How large are the Fibonacci numbers? Is there a simple formula that expresses $F_{n}$ as a function of $n$?

An easy way out, at least for the author of a book, is to state the answer right away:

<!-- carousel -->
![Figure 10 (top): The $8\times 8$ square cut into four pieces, with the apparent relation $8\cdot 8 = 5\cdot 13$.](06 - Fibonacci numbers_images/img-0.jpeg)
![Figure 10 (bottom): Proof of $65 = 64$ — the same four pieces reassembled into a $5\times 13$ rectangle.](06 - Fibonacci numbers_images/img-1.jpeg)
<!-- endcarousel -->

**Theorem 6.1.** The Fibonacci numbers are given by the formula

$$
F _ {n} = \frac {1}{\sqrt {5}} \left(\left(\frac {1 + \sqrt {5}}{2}\right) ^ {n} - \left(\frac {1 - \sqrt {5}}{2}\right) ^ {n}\right).
$$

It is straightforward to check that this formula gives the right value for  $n = 0,1$ , and then one can prove its validity for all  $n$  by induction.

> **6.8** Prove Theorem 6.1 by induction on  $n$ .

Do you feel cheated by this? You should; while it is of course logically correct what we did, one would like to see more: how can one arrive at such a formula? What should we try if we face a similar, but different recurrence?

So let us forget Theorem 6.1 for a while and let us try to find a formula for  $F_{n}$  "from scratch".

One thing we can try is to experiment. The Fibonacci numbers grow quite fast; how fast? Let's compute the ratio of consecutive Fibonacci numbers:

$$
\frac {1}{1} = 1, \quad \frac {2}{1} = 2, \quad \frac {3}{2} = 1.5, \quad \frac {5}{3} = 1.666666667, \quad \frac {8}{5} = 1.600000000,
$$

$$
\frac {13}{8} = 1.625000000, \quad \frac {21}{13} = 1.615384615, \quad \frac {34}{21} = 1.619047619, \quad \frac {55}{34} = 1.617647059,
$$

$$
\frac {89}{55} = 1.618181818, \quad \frac {144}{89} = 1.617977528, \quad \frac {233}{144} = 1.618055556, \quad \frac {377}{233} = 1.618025751.
$$

It seems that the ratio of consecutive Fibonacci numbers is very close to 1.618, at least if we ignore the first few values. This suggests that the Fibonacci numbers behave like a geometric progression. So let’s see if there is any geometric progression that satisfies the same recurrence as the Fibonacci numbers. Let $G_{n}=c\cdot q^{n}$ be a geometric progression ($c,q\neq 0$). Then

$G_{n+1}=G_{n}+G_{n-1}$

translates into

$c\cdot q^{n+1}=c\cdot q^{n}+c\cdot q^{n-1},$

which after simplification becomes

$q^{2}=q+1.$

(So the number $c$ disappears: what this means that if we find a sequence of this form that satisfies Fibonacci’s recurrence, then we can change $c$ in it to any other real number, and get another sequence that satisfies the recurrence.)

What we have is a quadratic equation for $q$, which we can solve and get

$q_{1}=\frac{1+\sqrt{5}}{2}\approx 1.618034,\qquad q_{2}=\frac{1-\sqrt{5}}{2}\approx-0.618034.$

So we have found two kinds of geometric progressions that satisfy the same recurrence as the Fibonacci numbers:

$G_{n}=c\left(\frac{1+\sqrt{5}}{2}\right)^{n},\qquad G_{n}^{\prime}=c\left(\frac{1-\sqrt{5}}{2}\right)^{n}$

(where $c$ is an arbitrary constant). Unfortunately, neither $G_{n}$ nor $G_{n}^{\prime}$ gives the Fibonacci sequence: for one, $G_{0}=G_{0}^{\prime}=c$ while $F_{0}=0$. But notice that the sequence $G_{n}-G_{n}^{\prime}$ also satisfies the recurrence:

$G_{n+1}-G_{n+1}^{\prime}=(G_{n}+G_{n-1})-(G_{n}^{\prime}+G_{n-1}^{\prime})=(G_{n}-G_{n}^{\prime})+(G_{n-1}-G_{n-1}^{\prime})$

(using that $G_{n}$ and $G_{n}^{\prime}$ satisfy the recurrence). Now we have matched the first value $F_{0}$, since $G_{0}-G_{0}^{\prime}=0$. What about the next one? We have $G_{1}-G_{1}^{\prime}=c\sqrt{5}$. We can match this with $F_{1}=1$ if we choose $c=1/\sqrt{5}$.

Now we have two sequences: $F_{n}$ and $G_{n}-G_{n}^{\prime}$, that both begin with the same two numbers, and satisfy the same recurrence. Hence they must be the same: $F_{n}=G_{n}-G_{n}^{\prime}$.

Now you can substitute for the values of $G_{n}$ and $G_{n}^{\prime}$, and see that we got the formula in the Theorem!

We can let a computer-algebra system retrace this whole derivation. Instead of checking Binet, we hand SymPy's `rsolve` *only* the bare recurrence $F(n)-F(n-1)-F(n-2)=0$ with $F_0=0,\,F_1=1$ and let it solve for the closed form, then prove symbolically that its answer is identical to Theorem 6.1 and that the roots of $q^2=q+1$ are exactly the golden ratio and its conjugate:

```python
<!-- include: code/dm/06 - Fibonacci numbers/01_python.py -->
```

Running it prints `rsolve - Binet      : 0` and `F_0..F_17 via Binet : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]`, confirming the formula SymPy derives from the bare recurrence is identically Theorem 6.1 and reproduces the chapter's listed sequence.

Let us include a little discussion of the formula we just derived. The first base in the exponential expression is $q_{1}=\frac{1+\sqrt{5}}{2}\approx 1.618034>1$, while the second base $q_{2}$ is between $-1$ and $0$. Hence if $n$ increases, then $G_{n}$ will become very large, while $|G_{n}^{\prime}|<1/2$ and in fact $G_{n}^{\prime}$ becomes very small. This means that

$F_{n}\approx G_{n}=\frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^{n},$

where the term we ignore is less than $1/2$ (and tends to $0$ if $n$ tends to infinity); this means that $F_{n}$ is the integer nearest to $G_{n}$.

The base $(1+\sqrt{5})/2$ is called the golden ratio, and it comes up all over mathematics; for example, it is the ratio between the diagonal and side of a regular pentagon.

We can confirm the experiment that started this section. The following recomputes every ratio $\frac11,\frac21,\frac32,\frac53,\dots$ printed above in exact rational arithmetic, formats each to nine decimals, and checks it against the book's table character-for-character, then watches $\left|\frac{F_{n+1}}{F_n}-\varphi\right|$ shrink toward $0$ where $\varphi=\frac{1+\sqrt5}{2}$:

```python
<!-- include: code/dm/06 - Fibonacci numbers/02_python.py -->
```

Running it reproduces the whole table (e.g. `377/233    1.618025751  yes`) and prints `golden ratio (1+sqrt5)/2 = 1.61803398875` with the error shrinking to `6.69777E-8`, confirming the ratios match the book and converge to the golden ratio.

> **6.9** Define a sequence of integers $H_{n}$ by $H_{0}=1$, $H_{1}=3$, and $H_{n+1}=H_{n}+H_{n-1}$. Show that $H_{n}$ can be expressed in the form $a\cdot q_{1}^{n}+b\cdot q_{2}^{n}$ (where $q_{1}$ and $q_{2}$ are the same numbers as in the proof above), and find the values of $a$ and $b$.

> **6.10** Define a sequence of integers $I_{n}$ by $I_{0}=0$, $I_{1}=1$, and $I_{n+1}=4I_{n}+I_{n-1}$. Find a formula for $I_{n}$.
