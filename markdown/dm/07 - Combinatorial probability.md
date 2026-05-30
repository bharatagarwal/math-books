## 7 Combinatorial probability

## 7.1 Events and probabilities

Probability theory is one of the most important areas of mathematics from the point of view of applications. In this book, we do not attempt to introduce even the most basic notions of probability theory; our only goal is to illustrate the importance of combinatorial results about the Pascal Triangle by explaining a key result in probability theory, the Law of Large Numbers. To do so, we have to talk a little about what probability is.

If we make an observation about our world, or carry out an experiment, the outcome will always depend on chance (to a varying degree). Think of the weather, the stockmarket, or a medical experiment. Probability theory is a way of modeling this dependence on chance.

We start with making a mental list of all possible outcomes of the experiment (or observation, which we don’t need to distinguish). These possible outcomes form a set $S$. Perhaps the simplest experiment is tossing a coin. This has two outcomes: $H$ (head) and $T$ (tail). So in this case $S=\{H,T\}$. As another example, the outcomes of throwing a dice form the set $S=\{1,2,3,4,5,6\}$. In this book, we assume that the set $S=\{s_{1},s_{2},\ldots,s_{k}\}$ of possible outcomes of our experiment is finite. The set $S$ is often called a sample space.

Every subset of $S$ is called an event (the event that the observed outcome falls in this subset). So if we are throwing a dice, the subset $\{2,4,6\}\subseteq S$ can be thought of as the event that we have thrown an even number.

The intersection of two subsets corresponds to the event that both events occur; for example, the subset $L\cap E=\{4,6\}$ corresponds to the event that we throw a better-than-average number that is also even. Two events $A$ and $B$ (i.e., two subsets of $S$) are called exclusive if they never occur at the same time, i.e., $A\cap B=\emptyset$. For example, the event $O=\{1,3,5\}$ that the outcome of tossing a dice is odd and the event $E$ that it is even are exclusive, since $E\cap O=\emptyset$.

> **7.1** What event does the union of two subsets corresponds to?

So let $S=\{s_{1},s_{2},\ldots,s_{n}\}$ be the set of possible outcomes of an experiment. To get a probability space we assume that each outcome $s_{i}\in S$ has a “probability” $\mathsf{P}(s_{i})$ such that

(a) $\mathsf{P}(s_{i})\geq 0$ for all $s_{i}\in S$,

and

(b) $\mathsf{P}(s_{1})+\mathsf{P}(s_{2})+\ldots+\mathsf{P}(s_{k})=1$.

Then we call $S$, together with these probabilities, a probability space. For example, if we toss a “fair” coin, then $\mathsf{P}(H)=\mathsf{P}(T)=1/2$. If the dice in our example is of good quality, then we will have $\mathsf{P}(i)=1/6$ for every outcome $i$.

A probability space in which every outcome has the same probability is called a uniform probability space. We shall only discuss uniform spaces here, since they are the easiest to imagine and they are the best for the illustration of combinatorial methods. But you should be warned that in more complicated modelling, non-uniform probability spaces are very often needed. For example, if we are observing if a day is rainy or not, we will have a 2-element sample space $S=\{\text{RAINY},\text{NON-RAINY}\}$, but these two will typically not have the same probability.

The probability of an event $A\subseteq S$ is defined as the sum of probabilities of outcomes in $A$, and is denoted by $\mathsf{P}(A)$. If the probability space is uniform, then the probability of $A$ is

$\mathsf{P}(A)=\frac{|A|}{|S|}=\frac{|A|}{k}.$

> **7.2** Prove that the probability of any event is at most 1.

> **7.3** What is the probability of the event $E$ that we throw an even number with the dice? What is the probability of the event $T=\{3,6\}$ that we toss a number that is divisible by 3?

> **7.4** Prove that if $A$ and $B$ are exclusive, then $\mathsf{P}(A)+\mathsf{P}(B)=\mathsf{P}(A\cap B)$.
>
> *(Note: as printed in the source. Since $A$ and $B$ are exclusive, $A\cap B=\emptyset$ and $\mathsf{P}(A\cap B)=0$; the identity the exercise means to state is $\mathsf{P}(A)+\mathsf{P}(B)=\mathsf{P}(A\cup B)$, which is what disjointness gives. This is a typo in the source text.)*

> **7.5** Prove that for any two events $A$ and $B$,
>
> $\mathsf{P}(A\cap B)+\mathsf{P}(A\cup B)=\mathsf{P}(A)+\mathsf{P}(B)$.

These axioms and exercises are really claims about *every* uniform space, so rather than check one by hand we can let a property-based tester hunt for a counterexample. The following models a finite uniform space where $\mathsf{P}(A)=|A|/|S|$ and throws hundreds of random sample spaces and events at axiom (a) $\mathsf{P}(A)\geq 0$, Exercise 7.2 $\mathsf{P}(A)\leq 1$, the complement rule $\mathsf{P}(\bar A)=1-\mathsf{P}(A)$, Exercise 7.4 (exclusive events add), and Exercise 7.5 $\mathsf{P}(A\cap B)+\mathsf{P}(A\cup B)=\mathsf{P}(A)+\mathsf{P}(B)$. A final test pins the dice independence example we meet in the next section: $E=\{2,4,6\}$, $T=\{3,6\}$, $E\cap T=\{6\}$, so $\mathsf{P}(E\cap T)=1/6=\tfrac12\cdot\tfrac13=\mathsf{P}(E)\mathsf{P}(T)$.

```python
<!-- include: code/dm/07 - Combinatorial probability/03_python.py -->
```

Running it prints `5 passed`, meaning Hypothesis found no counterexample to any axiom or identity across all generated spaces, and the worked dice independence example holds exactly.

## 7.2 Independent repetition of an experiment

Let us repeat our experiment $n$ times. We can consider this as a single big experiment, and a possible outcome of this repeated experiment is a sequence of length $n$, consisting of elements of $S$. Thus the sample space corresponding to this repeated experiment is the set $S^{n}$ of such sequences. Thus the number of outcomes of this “big” experiment is $k^{n}$. We consider every sequence equally likely, which means that we consider it a uniform probability space. Thus if $(a_{1},a_{2},\ldots,a_{n})$ is an outcome of the “big” experiment, then we have

$\mathsf{P}(a_{1},a_{2},\ldots,a_{n})=\frac{1}{k^{n}}.$

As an example, consider the experiment of tossing a coin twice. Then $S=\{H,T\}$ (head,tail) for a single coin toss, and so the sample space for the two coin tosses is $\{HH,HT,TH,TT\}$. The probability of each of these outcomes is $1/4$.

This definition intends to model the situation where the outcome of each repeated experiment is independent of the previous outcomes, in the everyday sense that “there cannot possibly be any measurable influence of one experiment on the other”. We cannot go here into the philosophical questions that this notion raises; all we can do is to give a mathematical definition that we can check on examples that it expresses the informal notion above.

A key notion in probability is that of independence of events. Informally, this means that information about one (whether or not it occurred) does not influence the probability of the other. Formally, two events $A$ and $B$ are independent if $\mathsf{P}(A\cap B)=\mathsf{P}(A)\mathsf{P}(B)$. For example, if $E=\{2,4,6\}$ is the event that the result of throwing a dice is even, and $T=\{3,6\}$ is the event that it is a multiple of 3, then $E$ and the event $T$ are independent: we have $E\cap T=\{6\}$ (the only possibility to throw a number that is even and divisible by 3 is to throw 6), and hence

$\mathsf{P}(E\cap T)=\frac{1}{6}=\frac{1}{2}\cdot\frac{1}{3}=\mathsf{P}(E)\mathsf{P}(T).$

Consider again the experiment of tossing a coin twice. Let $A$ be the event that the first toss is head; let $B$ be the event that the second toss is head. Then we have $\mathsf{P}(A)=\mathsf{P}(HH)+\mathsf{P}(HT)=1/4+1/4=1/2$, similarly $\mathsf{P}(B)=1/2$, and $\mathsf{P}(A\cap B)=\mathsf{P}(HH)=1/4=(1/2)\cdot(1/2)$. Thus $A$ and $B$ are independent events (as they should be).

> **7.6** Which pairs of the events $E,O,T,L$ are independent? Which pairs are exclusive?

> **7.7** Show that $\emptyset$ is independent from every event. Is there any other event with this property?

> **7.8** Consider an experiment with sample space $S$ repeated $n$ times ($n\geq 2$). Let $s\in S$. Let $A$ be the event that the first outcome is $s$, and let $B$ be the event that the last outcome is $s$. Prove that $A$ and $B$ are independent.

## 7.3 The Law of Large Numbers

In this section we study an experiment that consists of $n$ independent coin tosses. For simplicity, assume that $n$ is even, so that $n=2m$ for some integer $m$. Every outcome is a sequence of length $n$, in which each element is either $H$ or $T$. A typical outcome would look like this:

$HHTTTHTHTTHTHHHHTHTT$

(for $n=20$).

The “Law of Large Numbers” says that if we toss a coin many times, the number of ‘heads’ will be about the same as the number of ‘tails’. How can we make this statement precise? Certainly, this will not always be true; one can be extremely lucky or unlucky, and have a winning or losing streak of arbitrary length. Also, we can’t claim that the number of heads is equal to the number of tails; only that they are close. The following theorem is the simplest form of the Law of Large Numbers.

**Theorem 7.1.**

Let $0\leq t\leq m$. Then the probability that out of $2m$ independent coin tosses, the number of heads is less than $m-t$ or larger than $m+t$, is at most $m/t^{2}$.

Let us discuss this a little. If $t<\sqrt{m}$ then the assertion does not say anything, since we know anyhow that the probability of any event is at most $1$, and the upper bound given is larger than $1$. But if we choose, say, $t=10\sqrt{m}$, then we get an interesting special case:

**Corollary 7.1.**

With probability at least $.99$, the number of heads among $2m$ independent coin tosses is between $m-10\sqrt{m}$ and $m+10\sqrt{m}$.

Of course, we need that $m>10\sqrt{m}$, or $m>100$, for this to have any meaning. But after all, we are talking about Large Numbers! If $m$ is very large, then $10\sqrt{m}$ is much smaller than $m$, so we get that the number of heads is very close to $m$. For example, if $m=1,000,000$ then $10\sqrt{m}=m/100$, and so it follows that with probability at least $.99$, the number of heads is within $1$ percent of $m=n/2$.

We can watch this happen. The following Monte-Carlo simulation tosses the coin and prints the relative frequency of heads as the number of tosses $n$ grows; the frequency drifts steadily toward $p=1/2$, exactly as the law predicts. It also checks Corollary 7.1 empirically at $m=1{,}000{,}000$: the band $[m-10\sqrt{m},\,m+10\sqrt{m}]$ has half-width $10\sqrt{m}=10{,}000=m/100$ (the "within 1 percent" remark above), and across thousands of independent experiments the head count lands inside that band at least $99\%$ of the time.

```python
<!-- include: code/dm/07 - Combinatorial probability/01_python.py -->
```

Running it prints `n=10 freq 0.40000`, then `n=10000000 freq 0.49979` with `|freq - 1/2| = 0.000207`, and `fraction of 5000 experiments inside band = 1.0000 (theorem guarantees >= 0.99)`, confirming both the convergence to $1/2$ and Corollary 7.1's $99\%$ guarantee.

We would like to show that the Law of Large Numbers is not a mysterious force, but a simple consequence of the properties of binomial coefficients.

Let $A_{k}$ denote the event that we toss exactly $k$ heads. It is clear that the events $A_{k}$ are mutually exclusive. It is also clear that for every outcome of the experiment, exactly one of the $A_{k}$ occurs.

The number of outcomes for which $A_{k}$ occurs is the number of sequences of length $n$ consisting of $k$ ‘heads’ and $n-k$ ‘tails’. If we specify which of the $n$ positions are ‘heads’, we are done. This can be done in $\binom{n}{k}$ ways, so the set $A_{k}$ has $\binom{n}{k}$ elements. Since the total number of outcomes is $2^{n}$, we get the following.

$\mathsf{P}(A_{k})=\frac{\binom{n}{k}}{2^{n}}.$

What is the probability that the number of heads is far from the expected, which is $m=n/2$? Say, it is less than $m-t$ or larger than $m+t$, where $t$ is any positive integer not larger than $m$? Using exercise 7.1, we see that the probability that this happens is

$\frac{1}{2^{2m}}\left(\binom{2m}{0}+\binom{2m}{1}+\ldots+\binom{2m}{m-t-1}+\binom{2m}{m+t+1}+\ldots+\binom{2m}{2m-1}+\binom{2m}{2m}\right).$

Now we can use Theorem 5.2, with $k=t^{2}/m$, and get that

$\binom{2m}{0}+\binom{2m}{1}+\ldots+\binom{2m}{m-t-1}<\frac{m}{2t^{2}}2^{2m}.$

By the symmetry of the Pascal Triangle, we also have

$\binom{2m}{m+t+1}+\ldots+\binom{2m}{2m-1}+\binom{2m}{2m}<\frac{m}{2t^{2}}2^{2m}.$

Hence we get that the probability that we toss either less than $m-t$ or more than $m+t$ heads is less than $m/t^{2}$. This proves the theorem.

The proof rests on two things we can compute exactly: the probabilities $\mathsf{P}(A_k)=\binom{n}{k}/2^{n}$ and the tail bound $m/t^2$. Using exact rational arithmetic, the following reproduces that formula, verifies that the $\mathsf{P}(A_k)$ sum to $1$ (probability axiom (b)), and checks Theorem 7.1 — that the probability of the head count falling outside $[m-t,\,m+t]$ is at most $m/t^2$ — for several concrete $(m,t)$ pairs. It also reproduces $\mathsf{P}(HH)=1/4$ and the Corollary's bound $m/t^2=1/100$ at $m=1{,}000{,}000,\ t=10\sqrt{m}=10{,}000$.

```python
<!-- include: code/dm/07 - Combinatorial probability/02_python.py -->
```

Running it prints `sum_k P(A_k) for n=100: 1 (== 1: True)`, a table where every tail probability satisfies `<= bound True` (e.g. $m=50,\,t=20$ gives exact tail $\approx 0.000032 \le 0.125$), and `m/t^2 = 1/100 => P(inside band) >= 99/100`, confirming Theorem 7.1 and Corollary 7.1 exactly.
