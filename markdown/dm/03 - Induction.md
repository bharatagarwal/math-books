## Induction

## The sum of odd numbers

It is time to learn one of the most important tools in discrete mathematics. We start with a question: We add up the first $n$ odd numbers. What do we get?

Perhaps the best way to try to find the answer is to experiment. If we try small values of $n$, this is what we find:

$1$ $=$ $1$
$1+3$ $=$ $4$
$1+3+5$ $=$ $9$
$1+3+5+7$ $=$ $16$
$1+3+5+7+9$ $=$ $25$
$1+3+5+7+9+11$ $=$ $36$
$1+3+5+7+9+11+13$ $=$ $49$
$1+3+5+7+9+11+13+15$ $=$ $64$
$1+3+5+7+9+11+13+15+17$ $=$ $81$
$1+3+5+7+9+11+13+15+17+19$ $=$ $100$

It is easy to observe that we get squares; in fact, it seems from this examples that the sum of the first $n$ odd numbers is $n^{2}$. This we have observed for the first 10 values of $n$; can we be sure that it is valid for all? Well, I’d say we can be reasonably sure, but not with mathematical certainty. How can we prove the assertion?

Consider the sum for a general $n$. The $n$-th odd number is $2n-1$ (check!), so we want to prove that

$1+3+\ldots+(2n-3)+(2n-1)=n^{2}.$ (2)

If we separate the last term in this sum, we are left with the sum of the first $(n-1)$ odd numbers:

$1+3+\ldots+(2n-3)+(2n-1)=\Big(1+3+\ldots+(2n-3)\Big)+(2n-1)$

Now here the sum in the large parenthesis is $(n-1)^{2}$, so the total is

$(n-1)^{2}+(2n-1)=(n^{2}-2n+1)+(2n-1)=n^{2},$ (3)

just as we wanted to prove.

We can have this exact argument machine-checked. The following is eq. (2) as a formal Lean 4 proof: `oddSum` is defined recursively (the $(k{+}1)$-th odd number is $2k+1$), and `oddSum_eq_sq` proves $\text{oddSum}(n)=n^2$ by `induction n`. The `zero` case is `rfl`, and the `succ` case peels off the last odd number and rewrites with the induction hypothesis `ih` -- exactly the "separate the last term" move we just made -- before discharging the algebra. Lean accepts it only if every step is sound.

```lean
<!-- include: code/dm/03 - Induction/03_lean.lean -->
```

Running it exits $0$ (proof accepted) and the `#eval` prints `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, reproducing the table above from the verified definition.

Wait a minute! Aren’t we using in the proof the statement that we are proving? Surely this is unfair! One could prove everything if this were allowed.

But in fact we are not quite using the same. What we were using, is the assertion about the sum of the first $n-1$ odd numbers; and we argued (in (3)) that this proves the assertion about the sum of the first $n$ odd numbers. In other words, what we have shown is that if the assertion is true for a certain value of $n$, it is also true for the next.

This is enough to conclude that the assertion is true for every $n$. We have seen that it is true for $n=1$; hence by the above, it is also true for $n=2$ (we have seen this anyway by

direct computation, but this shows that this was not even necessary: it followed from the case $n=1$).

In a similar way, the truth of the assertion for $n=2$ implies that it is also true for $n=3$, which in turn implies that it is true for $n=4$, etc. If we repeat this sufficiently many times, we get the truth for any value of $n$.

This proof technique is called induction (or sometimes mathematical induction, to distinguish it from a notion in philosophy). It can be summarized as follows.

Suppose that we want to prove a property of positive integers. Also suppose that we can prove two facts:

(a) $1$ has the property, and

(b) whenever $n-1$ has the property, then also $n$ has the property ($n\geq 1$).

The principle of induction says that if (a) and (b) are true, then every natural number has the property.

Often the best way to try to carry out an induction proof is the following. We try to prove the statement (for a general value of $n$), and we are allowed to use that the statement is true if $n$ is replaced by $n-1$. (This is called the induction hypothesis.) If it helps, one may also use the validity of the statement for $n-2$, $n-3$, etc., in general for every $k$ such that $k<n$.

Sometimes we say that if $0$ has the property, and every integer $n$ inherits the property from $n-1$, then every integer has the property. (Just like if the founding father of a family has a certain piece of property, and every new generation inherits this property from the previous generation, then the family will always have this property.)

What induction buys us over the 10-row table is a closed form valid for *every* $n$, and we can get a symbolic engine to certify that closed form directly. `sympy.summation` evaluates each sum as a function of $n$: it returns $n^2$ for $1+3+\dots+(2n-1)$, and -- looking ahead to the next sections -- it also confirms the region count equals both $1+\frac{n(n+1)}{2}$ and the $1+n+\binom{n}{2}$ form, and checks the subset split $2^{n-1}+2^{n-1}=2^n$. It also reproduces the book's exact numbers, $1,4,\dots,100$ and $1,2,4,7,11$.

```python
<!-- include: code/dm/03 - Induction/01_python.py -->
```

Running it prints `sum_(k=1..n) (2k-1) = n**2`, `region table n=0..4 = [1, 2, 4, 7, 11]`, and `ALL SYMBOLIC IDENTITIES PROVED`, confirming all three closed forms and reproducing the chapter's tables.

> **3.1** Prove, using induction but also without it, that $n(n+1)$ is an even number for every non-negative integer $n$.

> **3.2** Prove by induction that the sum of the first $n$ positive integers is $n(n+1)/2$.

> **3.3** Observe that the number $n(n+1)/2$ is the number of handshakes among $n+1$ people. Suppose that everyone counts only handshakes with people older than him/her (pretty snobbish, isn’t it?). Who will count the largest number of handshakes? How many people count 6 handshakes?
>
> Give a proof of the result of exercise 3.1, based on your answer to these questions.

> **3.4** Give a proof of exercise 3.1, based on figure 3.

> **3.5** Prove the following identity:
>
> $1\cdot 2+2\cdot 3+3\cdot 4+\ldots+(n-1)\cdot n=\frac{(n-1)\cdot n\cdot(n+1)}{3}.$

Exercise 3.1 relates to a well-known (though apocryphal) anecdote from the history of mathematics. Carl Friedrich Gauss (1777-1855), one of the greatest mathematicians of all times, was in elementary school when his teacher gave the class the task to add up the integers from $1$ to $1000$ (he was hoping that he would get an hour or so to relax while his students were working). To his great surprise, Gauss came up with the correct answer almost immediately. His solution was extremely simple: combine the first term with the last, you get $1+1000=1001$; combine the second term with the last but one,

<!-- carousel -->
![Figure 3: The sum of the first $n$ integers. A triangular array of dots asks $1+2+3+4+5=?$](03 - Induction_images/img-0.jpeg)

![Figure 3 (continued): Two copies of the triangle fill an $n \times (n+1)$ rectangle, so $2(1+2+3+4+5) = 5 \cdot 6 = 30$, giving $1+2+\dots+n = n(n+1)/2$](03 - Induction_images/img-1.jpeg)
<!-- endcarousel -->

you get  $2 + 999 = 1001$ ; going on in a similar way, combining the first remaining term with the last one (and then discarding them) you get 1001. The last pair added this way is  $500 + 501 = 1001$ . So we obtained 500 times 1001, which makes 500500. We can check this answer against the formula given in exercise 3.1:  $1000 \cdot 1001 / 2 = 500500$ .

> **3.6** Use the method of the little Gauss to give a third proof of the formula in exercise 3.1
> **3.7** How would the little Gauss prove the formula for the sum of the first  $n$  odd numbers (2)?
> **3.8** Prove that the sum of the first  $n$  squares  $(1 + 4 + 9 + \ldots + n^2)$  is  $n(n + 1)(2n + 1) / 6$ .
> **3.9** Prove that the sum of the first  $n$  powers of 2 (starting with  $1 = 2^0$ ) is  $2^n - 1$ .

## Subset counting revisited

In chapter 2 we often relied on the convenience of saying "etc.": we described some argument that had to be repeated  $n$  times to give the result we wanted to get, but after giving the argument once or twice, we said "etc." instead of further repetition. There is nothing wrong with this, if the argument is sufficiently simple so that we can intuitively see where the repetition leads. But it would be nice to have some tool at hand which could be used instead of "etc." in cases when the outcome of the repetition is not so transparent.

The precise way of doing this is using induction, as we are going to illustrate by revisiting some of our results. First, let us give a proof of the formula for the number of subsets of an  $n$ -element set, given in Theorem 2.1 (recall that the answer is  $2^n$ ).

As the principle of induction tells us, we have to check that the assertion is true for  $n = 0$ . This is trivial, and we already did it. Next, we assume that  $n > 0$ , and that the assertion is true for sets with  $n - 1$  elements. Consider a set  $S$  with  $n$  elements, and fix any element  $a \in S$ . We want to count the subsets of  $S$ . Let us divide them into two classes: those containing  $a$  and those not containing  $a$ . We count them separately.

First, we deal with those subsets which don't contain  $a$ . If we delete  $a$  from  $S$ , we are left with a set  $S'$  with  $n - 1$  elements, and the subsets we are interested in are exactly the subsets of  $S'$ . By the induction hypothesis, the number of such subsets is  $2^{n - 1}$ .

Second, we consider subsets containing  $a$ . The key observation is that every such subset consists of  $a$  and a subset of  $S'$ . Conversely, if we take any subset of  $S'$ , we can add  $a$  to it

to get a subset of $S$ containing $a$. Hence the number of subsets of $S$ containing $a$ is the same as the number of subsets of $S^{\prime}$, which, as we already know, is $2^{n-1}$. (With the jargon we introduced before, the last piece of the argument establishes as one-to-one correspondence between those subsets of $S$ containing $a$ and those not containing $a$.)

To conclude: the total number of subsets of $S$ is $2^{n-1}+2^{n-1}=2\cdot 2^{n-1}=2^{n}$. This proves Theorem 2.1 (again).

We can attack the *other* half of an induction proof -- the inductive step itself -- by brute force. Where `sympy` proved the formulas, `hypothesis` generates hundreds of random $n$ and checks the moving parts: the inductive step $S(n)=S(n-1)+(2n-1)$ for the odd-number sum, the brute-force odd-number sum against $n^2$, the region recurrence against $1+\frac{n(n+1)}{2}$, and -- matching the argument just given -- counts every bitmask subset of an $n$-set to confirm $2^n$ and the containing/not-containing split. A wrong formula would surface as a concrete counterexample.

```python
<!-- include: code/dm/03 - Induction/02_python.py -->
```

Running it prints `5 passed`, confirming the identities and the inductive step hold across the full randomized range (the book tables $1,\dots,100$ and $1,2,4,7,11$ are checked exactly).

> **3.10** Use induction to prove Theorem 2.2 (the number of strings of length $n$ composed of $k$ given elements is $k^{n}$) and Theorem 2 (the number of permutations of a set with $n$ elements is $n!$).

> **3.11** Use induction on $n$ to prove the “handshake theorem” (the number of handshakes between $n$ people is $n(n-1)/2$).

> **3.12** Read carefully the following induction proof:
>
> Assertion: $n(n+1)$ is an odd number for every $n$.
>
> Proof: Suppose that this is true for $n-1$ in place of $n$; we prove it for $n$, using the induction hypothesis. We have
>
> $n(n+1)=(n-1)n+2n.$
>
> Now here $(n-1)n$ is odd by the induction hypothesis, and $2n$ is even. Hence $n(n+1)$ is the sum of an odd number and an even number, which is odd.
>
> The assertion that we proved is obviously wrong for $n=10$: $10\cdot 11=110$ is even. What is wrong with the proof?

> **3.13** Read carefully the following induction proof:
>
> Assertion: If we have $n$ lines in the plane, no two of which are parallel, then they all go through one point.
>
> Proof: The assertion is true for one line (and also for 2, since we have assumed that no two lines are parallel). Suppose that it is true for any set of $n-1$ lines. We are going to prove that it is also true for $n$ lines, using this induction hypothesis.
>
> So consider a set of $S=\{a,b,c,d,\ldots\}$ of $n$ lines in the plane, no two of which are parallel. Delete the line $c$, then we are left with a set $S^{\prime}$ of $n-1$ lines, and obviously no two of these are parallel. So we can apply the induction hypothesis and conclude that there is a point $P$ such that all the lines in $S^{\prime}$ go through $P$. In particular, $a$ and $b$ go through $P$, and so $P$ must be the point of intersection of $a$ and $b$.
>
> Now put $c$ back and delete $d$, to get a set $S^{\prime\prime}$ of $n-1$ lines. Just as above, we can use the induction hypothesis to conclude that these lines go through the same point $P^{\prime}$; but just like above, $P^{\prime}$ must be the point of intersection of $a$ and $b$. Thus $P^{\prime}=P$. But then we see that $c$ goes through $P$. The other lines also go through $P$ (by the choice of $P$), and so all the $n$ lines go through $P$.
>
> But the assertion we proved is clearly wrong; where is the error?

## Counting regions

Let us draw $n$ lines in the plane. These lines divide the plane into some number of regions. How many regions do we get?

<!-- carousel -->
![Figure 4 (a, b): a) two parallel lines cut the plane into 3 regions; b) two crossing lines cut it into 4 regions](03 - Induction_images/img-2.jpeg)

![Figure 4 (c): three lines through one common point give 6 regions](03 - Induction_images/img-3.jpeg)

![Figure 4 (d): three lines in general position (no common point) give 7 regions](03 - Induction_images/img-4.jpeg)
<!-- endcarousel -->

![Figure 5: Lines in general position. With $1, 2, 3, 4$ lines we get $2, 4, 7, 11$ regions](03 - Induction_images/img-5.jpeg)

A first thing to notice is that this question does not have a single answer. For example, if we draw two lines, we get 3 regions if the two are parallel, and 4 regions if they are not.

OK, let us assume that no two of the lines are parallel; then 2 lines always give us 4 regions. But if we go on to three lines, we get 6 regions if the lines go through one point, and 7 regions, if they do not (Figure 4).

OK, let us also exclude this, and assume that no 3 lines go through the same point. One might expect that the next unpleasant example comes with 4 lines, but if you experiment with drawing 4 lines in the plane, with no two parallel and no three going through the same point, then you invariably get 11 regions (Figure 5). In fact, we'll have a similar experience for any number of lines.

A set of lines in the plane such that no two are parallel and no three go through the same point is said to be in general position. If we choose the lines "randomly" then accidents like two being parallel or three going through the same point will be very unlikely, so our assumption that the lines are in general position is quite natural.

Even if we accept that the number of regions is always the same for a given number of lines, the question still remains: what is this number? Let us collect our data in a little table (including also the observation that 0 lines divide the plane into 1 region, and 1 line divides the plane into 2):

|  0 | 1 | 2 | 3 | 4  |
| --- | --- | --- | --- | --- |
|  1 | 2 | 4 | 7 | 11  |

Staring at this table for a while, we observe that each number in the second row is the sum of the number above it and the number before it. This suggests a rule: the  $n$ -th entry is  $n$  plus the previous entry. In other words: If we have a set of  $n - 1$  lines in the plane

in general position, and add a new line (preserving general position), then the number of regions increases by $n$.

Let us prove this assertion. How does the new line increase the number of regions? By cutting some of them into two. The number of additional regions is just the same as the number of regions intersected.

So, how many regions does the new line intersect? At a first glance, this is not easy to answer, since the new line can intersect very different sets of regions, depending on where we place it. But imagine to walk along the new line, starting from very far. We get to a new region every time we cross a line. So the number of regions the new line intersects is one larger than the number of crossing points on the new line with other lines.

Now the new line crosses every other line (since no two lines are parallel), and it crosses them in different points (since no three lines go through the same point). Hence during our walk, we see $n-1$ crossing points. So we see $n$ different regions. This proves that our observation about the table is true for every $n$.

We are not done yet; what does this give for the number of regions? We start with $1$ region for $0$ lines, and then add to it $1,2,3,\ldots,n$. This way we get

$1+(1+2+3+\ldots+n)=1+\frac{n(n+1)}{2}.$

Thus we have proved:

**Theorem 3.1.**

A set of $n$ lines in general position in the plane divides the plane into $1+n(n+1)/2$ regions.

- 3.14 Describe a proof of Theorem 3.1 using induction on the number of lines.

Let us give another proof of Theorem 3.1; this time, we will not use induction, but rather try to relate the number of regions to other combinatorial problems. One gets a hint from writing the number in the form $1+n+\binom{n}{2}$.

Assume that the lines are drawn on a vertical blackboard (Figure 6), which is large enough so that all the intersection points appear on it. We also assume that no line is horizontal (else, we tilt the picture a little), and that in fact every line intersects the bottom edge of the blackboard (the blackboard is very long).

Now consider the lowest point in each region. Each region has only one lowest point, since the bordering lines are not horizontal. This lowest point is then an intersection point of two of our lines, or the intersection point of line with the lower edge of the blackboard, or the lower left corner of the blackboard. Furthermore, each of these points is the lowest point of one and only one region. For example, if we consider any intersection point of two lines, then we see that four regions meet at this point, and the point is the lowest point of exactly one of them.

Thus the number of lowest points is the same as the number of intersection points of the lines, plus the number of intersection points between lines and the lower edge of the blackboard, plus one. Since any two lines intersect, and these intersection points are all different (this is where we use that the lines are in general position), the number of such lowest points is $\binom{n}{2}+n+1$.

Theorem 3.1 also has an imperative twin. A loop invariant is the program-level counterpart of an induction hypothesis: the verifier checks it holds before the loop, is preserved by each iteration (the $n-1 \to n$ step), and is strong enough at exit to give the postcondition. `SumOfOdds` carries the invariant $s = k^2$ to prove its result is $n^2$ (the odd-sum identity from Section 3.1), and `CountRegions` carries $r = 1+\frac{k(k+1)}{2}$ to prove Theorem 3.1 -- both proved for *all* $n$ by the SMT backend, with no test run.

```dafny
<!-- include: code/dm/03 - Induction/04_dafny.dfy -->
```

Running it prints `Dafny program verifier finished with 3 verified, 0 errors`, confirming both the $n^2$ odd-sum postcondition and the $1+\frac{n(n+1)}{2}$ region count hold for every $n$.
