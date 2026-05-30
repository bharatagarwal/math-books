<!-- page 1 -->

![img-0.jpeg](04 - Counting subsets_images/img-0.jpeg)
Figure 6:

# 4 Counting subsets

# 4.1 The number of ordered subsets

At a competition of 100 athletes, only the order of the first 10 is recorded. How many different outcomes does the competition have?

This question can be answered along the lines of the arguments we have seen. The first place can be won by any of the athletes; no matter who wins, there are 99 possible second place winners, so the first two prizes can go  $100 \cdot 99$  ways. Given the first two, there are 98 athletes who can be third, etc. So the answer is  $100 \cdot 99 \cdot \ldots \cdot 91$ .

4.1 Illustrate this argument by a tree.

4.2 Suppose that we record the order of all 100 athletes.

(a) How many different outcomes can we have then?
(b) How many of these give the same for the first 10 places?
(c) Show that the result above for the number of possible outcomes for the first 10 places can be also obtained using (a) and (b).

There is nothing special about the numbers 100 and 10 in the problem above; we could carry out the same for  $n$  athletes with the first  $k$  places recorded.

To give a more mathematical form to the result, we can replace the athletes by any set of size  $n$ . The list of the first  $k$  places is given by a sequence of  $k$  elements of  $n$ , which all have to be different. We may also view this as selecting a subset of the athletes with  $k$  elements, and then ordering them. Thus we have the following theorem.

Theorem 4.1 The number of ordered  $k$ -subsets of an  $n$ -set is  $n(n - 1)\ldots (n - k + 1)$ .

---

<!-- page 2 -->

(Note that if we start with $n$ and count down $k$ numbers, the last one will be $n-k+1$.)

4.3 If you generalize the solution of exercise 4.1, you get the answer in the form

$\frac{n!}{(n-k)!}$

Check that this is the same number as given in theorem 4.1.

4.4 Explain the similarity and the difference between the counting questions answered by theorem 4.1 and theorem 2.2.

### 4.2 The number of subsets of a given size

From here, we can easily derive one of the most important counting results.

###### Theorem 4.2

The number of $k$-subsets of an $n$-set is

$\frac{n(n-1)\ldots(n-k+1)}{k!}=\frac{n!}{k!(n-k)!}$

Recall that if we count ordered subsets, we get $n(n-1)\ldots(n-k+1)=n!/(n-k)!$, by Theorem 4.1. Of course, if we want to know the number of unordered subsets, then we have overcounted; every subset was counted exactly $k!$ times (with every possible ordering of its elements). So we have to divide this number by $k!$ to get the number of subsets with $k$ elements (without ordering).

The number of $k$-subsets of an $n$-set is such an important quantity that one has a separate notation for it: ${n\choose k}$ (read: ‘$n$ choose $k$’). Thus

${n\choose k}=\frac{n!}{k!(n-k)!}.$

Thus the number of different lottery tickets in ${90\choose 5}$, the number of handshakes is ${7\choose 2}$ etc.

4.5 Which problems discussed during the party were special cases of theorem 4.2?

4.6 Tabulate the values of ${n\choose k}$ for $n,k\leq 5$.

In the following exercises, try to prove the identities by using the formula in theorem 4.2, and also without computation, by explaining both sides of the equation as the result of a counting problem.

4.7 Prove that ${n\choose 2}+{n+1\choose 2}=n^{2}$.

4.8 (a) Prove that ${90\choose 5}={89\choose 5}+{89\choose 4}$.

(b) Formulate and prove a general identity based on this.

4.9 Prove that ${n\choose k}={n\choose n-k}$.

##

---

<!-- page 3 -->

4.10 Prove that

$1+\binom{n}{1}+\binom{n}{2}+\ldots+\binom{n}{n-1}+\binom{n}{n}=2^{n}.$

4.11 Prove that for $0<c\leq b\leq a$,

$\binom{a}{b}\binom{b}{c}=\binom{a}{a-c}\binom{a-c}{b-c}$

### 4.3 The Binomial Theorem

The numbers $\binom{n}{k}$ also have a name, binomial coefficients, which comes from a very important formula in algebra involving them. We are now going to discuss this theorem.

The issue is to compute powers of the simple algebraic expression $(x+y)$. We start with small examples:

$(x+y)^{2}=x^{2}+2xy+y^{2},$
$(x+y)^{3}=(x+y)\cdot(x+y)^{2}=(x+y)\cdot(x^{2}+2xy+y^{2})=x^{3}+3x^{2}y+3xy^{2}+y^{3},$

and, going on like this,

$(x+y)^{4}=(x+y)\cdot(x+y)^{3}=x^{4}+4x^{3}y+6x^{2}y^{2}+4xy^{3}+y^{4}.$

You may have noticed that the coefficients you get are the numbers that we have seen, e.g. in exercise 4.2, as numbers $\binom{n}{k}$. Let us make this observation precise. We illustrate the argument for the next value of $n$, namely $n=5$, but it works in general.

Think of expanding

$(x+y)^{5}=(x+y)(x+y)(x+y)(x+y)(x+y)$

so that we get rid of all parentheses. We get each term in the expansion by selecting one of the two terms in each factor, and multiplying them. If we choose $x$, say, 2 times then we choose $y$ 3 times, and we get $x^{2}y^{3}$. How many times do we get this same term? Clearly as many times as the number of ways to select the two factors that supply $x$ (the remaining factors supply $y$). Thus we have to choose two factors out of 5, which can be done in $\binom{5}{2}$ ways.

Hence the expansion of $(x+y)^{5}$ looks like this:

$(x+y)^{5}=\binom{5}{0}y^{5}+\binom{5}{1}xy^{4}+\binom{5}{2}x^{2}y^{3}+\binom{5}{3}x^{3}y^{2}+\binom{5}{4}x^{4}y+\binom{5}{5}x^{5}.$

We can apply this argument in general to obtain

###### Theorem 4.3 (The Binomial Theorem)

The coefficient of $x^{k}y^{n-k}$ in the expansion of $(x+y)^{n}$ is $\binom{n}{k}$. In other words, we have the identity:

$(x+y)^{n}=y^{n}+\binom{n}{1}x^{n-1}y+\binom{n}{2}x^{n-2}y^{2}+\ldots+\binom{n}{n-1}x^{n-1}y+\binom{n}{n}x^{n}.$

---

<!-- page 4 -->

This important theorem is called the Binomial Theorem; the name comes from the Greek word binome for an expression consisting of two terms, in this case, $x+y$. The appearance of the numbers $\binom{n}{k}$ in this theorem is the source of their name: binomial coefficients.

The Binomial Theorem can be applied in many ways to get identities concerning binomial coefficients. For example, let us substitute $x=y=1$, then we get

$2^{n}=\binom{n}{0}+\binom{n}{1}+\binom{n}{2}+\ldots+\binom{n}{n-1}+\binom{n}{n}.$ (4)

Later on we are going to see trickier applications of this idea. For the time being, another twist on it is contained in the next exercise.

> 4.12 Give a proof of the Binomial Theorem by induction, based on exercise 4.2.
>
> 4.13 (a) Prove the identity
>
> $\binom{n}{0}-\binom{n}{1}+\binom{n}{2}-\binom{n}{3}\ldots=0$
>
> (The sum ends with $\binom{n}{n}=1$, with the last depending on the parity of $n$.)
>
> (b) This identity is obvious if $n$ is odd. Why?
>
> 4.14 Prove identity 4, using a combinatorial interpretation of the two sides (recall exercise 4.2).

### 4.4 Distributing presents

Suppose we have $n$ different presents, which we want to distribute to $k$ children. For some reason, we are told how many presents should each child get; so Adam should get $n_{\text{Adam}}$ presents, Barbara, $n_{\text{Barbara}}$ presents etc. In a mathematically convenient (though not very friendly) way, we call the children $1,2,\ldots,k$; thus we are given the numbers (non-negative integers) $n_{1},n_{2},\ldots,n_{k}$. We assume that $n_{1}+n_{2}+\ldots+n_{k}=n$, else there is no way to distribute the presents.

The question is, of course, how many ways can these presents be distributed?

We can organize the distribution of presents as follows. We lay out the presents in a single row of length $n$. The first child comes and picks up the first $n_{1}$ presents, starting from the left. Then the second comes, and picks up the next $n_{2}$; then the third picks up the next $n_{3}$ presents etc. Child No. k gets the last $n_{k}$ presents.

It is clear that we can determine who gets what by choosing the order in which the presents are laid out. There are $n!$ ways to order the presents. But, of course, the number $n!$ overcounts the number of ways to distribute the presents, since many of these orderings lead to the same results (that is, every child gets the same set of presents). The question is, how many?

So let us start with a given distribution of presents, and let’s ask the children to lay out the presents for us, nicely in a row, starting with the first child, then continuing with the second, third, etc. This way we get back one possible ordering that leads to the current distribution. The first child can lay out his presents in $n_{1}!$ possible orders; no matter which order he chooses, the second child can lay out her presents in $n_{2}!$ possible ways, etc. So the

---

<!-- page 5 -->

![img-1.jpeg](04 - Counting subsets_images/img-1.jpeg)
Figure 7: Placing 8 non-attacking rooks on a chessboard

number of ways the presents can be laid out (given the distribution of the presents to the children) is a product of factorials:

$$
n _ {1}! \cdot n _ {2}! \cdot \dots \cdot n _ {k}!.
$$

Thus the number of ways of distributing the presents is

$$
\frac {n !}{n _ {1} ! n _ {2} ! \ldots n _ {k} !}.
$$

4.15 We can describe the procedure of distributing the presents as follows. First, we select  $n_1$  presents and give them to the first child. This can be done in  $\binom{n}{n_1}$  ways. Then we select  $n_2$  presents from the remaining  $n - n_1$  and give them to the second child, etc.

Complete this argument and show that it leads to the same result as the previous one.

4.16 The following special cases should be familiar from previous problems and theorems. Explain why.

(a)  $n = k, n_1 = n_2 = \ldots = n_k$ ;
(b)  $n_1 = n_2 = \ldots = n_{k - 1} = 1, n_k = n - k + 1;$
(c)  $k = 2$
(d)  $k = 3, n = 6, n_{1} = n_{2} = n_{3} = 2$ .

4.17 (a) How many ways can you place  $n$  rooks on a chessboard so that no two attack each other (Figure 7)? We assume that the rooks are identical, so e.g. interchanging two rooks does not count as a separate placement.

(b) How many ways can you do this if you have 4 black and 4 white rooks?
(c) How many ways can you do this if all the 8 rooks are different?

---

<!-- page 6 -->

4.5 Anagrams

Have you played with anagrams? One selects a word (say, COMBINATORICS) and tries to compose from its letters meaningful, often funny words or expressions.

How many anagrams can you build from a given word? If you try to answer this question by playing around with the letters, you will realize that the question is badly posed; it is difficult to draw the line between meaningful and non-meaningful anagrams. For example, it could easily happen that A CROC BIT SIMON. And it may be true that Napoleon always wanted a TOMB IN CORSICA. It is questionable, but certainly grammatically correct, to assert that COB IS ROMANTIC. Some universities may have a course on MAC IN ROBOTICS.

But one would have to write a book to introduce an exciting character, ROBIN COSMICAT, who enforces a COSMIC RIOT BAN, while appealing TO COSMIC BRAIN.

And it would be terribly difficult to explain an anagram like MTBIRASCIONOC.

To avoid this controversy, let’s accept everything, i.e., we don’t require the anagram to be meaningful (or even pronouncible). Of course, the production of anagrams becomes then uninteresting; but at least we can tell how many of them are there!

> 4.18 How many anagrams can you make from the word COMBINATORICS?
>
> 4.19 Which word gives rise to more anagrams: COMBINATORICS or COMBINATORICA? (The latter is the Latin name of the subject.)
>
> 4.20 Which word with 13 letters gives rise to the most anagrams? Which word gives rise to the least?

So let’s see the general answer to the question of counting anagrams. If you have solved the problems above, it should be clear that the number of anagrams $n$-letter word depends on how many times letters of the word are repeated. So suppose that the word contains letter No. 1 $n_{1}$ times, letter No. 2 $n_{2}$ times, etc., letter No. k $n_{k}$ times. Clearly, $n_{1}+n_{2}+\ldots+n_{k}=n$.

Now to form an anagram, we have to select $n_{1}$ positions for letter No. 1, $n_{2}$ positions for letter No. 2, etc., $n_{k}$ positions fro letter No. 3. Having formulated it this way, we can see that this is nothing but the question of distributing $n$ presents to $k$ children, when it is prescribed how many presents each child gets. Thus we know from the previous section that the answer is

$\frac{n}{n_{1}!n_{2}!\ldots n_{k}!}.$

> 4.21 It is clear that STATUS and LETTER have the same number of anagrams (in fact, $6!/(2!2!)=180$). We say that these words are “essentially the same” (at least as far as counting anagrams goes): they have two letters repeated twice and two letters occurring only once.
>
> (a) How many 6-letter words are there? (As before, the words don’t have to be meaningful. The alphabet has 26 letters.)
>
> (b) How many words with 6 letters are “essentially the same” as the word LETTER?
>
> (c) How many “essentially different” 6-letter words are there?

---

<!-- page 7 -->

![img-2.jpeg](04 - Counting subsets_images/img-2.jpeg)
Figure 8: How to distribute  $n$  pennies to  $k$  children?

(d) Try to find a general answer to question (c) (that is, how many "essentially different" words are there on  $n$  letters?). If you can't find it, read the following section and return to this exercise after it.

# 4.6 Distributing money

Instead of distributing presents, let's distribute money. Let us formulate the question in general: we have  $n$  pennies that we want to distribute among  $k$  kids. Each child must get at least one penny (and, of course, an integer number of pennies). How many ways can we distribute the money?

Before answering this question, we must clarify the difference between distributing money and distributing presents. If you are distributing presents, you have to decide not only how many presents each child gets, but also which are these presents. If you are distributing money, only the quantity matters. In other words, the presents are distinguishable while the pennies are not. (A question like in section 4.4, where we specify in advance how many presents does a given child get, would be trivial for money: there is only one way to distribute  $n$  pennies so that the first child gets  $n_1$ , the second child gets  $n_2$ , etc.)

Even though the problem is quite different from the distribution of presents, we can solve it by imagining a similar distribution method. We line up the pennies (it does not matter in which order, they are all alike), and then let child No. 1 begin to pick them up from left to right. After a while we stop him and let the second child pick up pennies, etc. (Figure 8) The distribution of the money is determined by specifying where to start with a new child.

Now there are  $n - 1$  points (between consecutive pennies) where we can let a new child in, and we have to select  $k - 1$  of them (since the first child always starts at the beginning, we have no choice there). Thus we have to select a  $(k - 1)$ -element subset from an  $(n - 1)$ -element set. The number of possibilities to do so is  $\binom{n-1}{k-1}$ .

To sum up, we get

Theorem 4.4 The number of ways to distribute  $n$  identical pennies to  $k$  children, so that each child gets at least one, is  $\binom{n-1}{k-1}$ .

It is quite surprising that the binomial coefficients give the answer here, in a quite non-trivial and unexpected way.

Let's also discuss the natural (though unfair) modification of this question, where we also allow distributions in which some children get no money at all; we consider even giving all the money to one child. With the following trick, we can reduce the problem of counting such distributions to the problem we just solved: we borrow 1 penny from each child, and the distribute the whole amount (i.e.,  $n + k$  pennies) to the children so that each child gets

---

<!-- page 8 -->

at least one penny. This way every child gets back the money we borrowed from him or her, and the lucky ones get some more. The “more” is exactly $n$ pennies distributed to $k$ children. We already know that the number of ways to distribute $n+k$ pennies to $k$ children so that each child gets at least one penny is $\binom{n+k-1}{k-1}$. So we have

###### Theorem 4.5

The number of ways to distribute $n$ identical pennies to $k$ children is $\binom{n+k-1}{k-1}$.

- 4.22 In how many ways can you distribute $n$ pennies to $k$ children, if each child is supposed to get at least 2?
- 4.23 We distribute $n$ pennies to $k$ boys and $\ell$ girls, so that (to be really unfair) we require that each of the girls gets at least one penny. In how many ways can we do this?
- 4.24 $k$ earls play cards. Originally, they all have $p$ pennies. At the end of the game, they count how much money they have. They do not borrow from each other, so that they cannot loose more than their $p$ pennies. How many possible results are there?