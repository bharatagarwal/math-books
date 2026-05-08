## 5 Induction

Induction is a powerful method for showing a property is true for all nonnegative integers. Induction plays a central role in discrete mathematics and computer science. In fact, its use is a defining characteristic of discrete—as opposed to continuous—mathematics. This chapter introduces two versions of induction, Ordinary and Strong, and explains why they work and how to use them in proofs. It also introduces the Invariant Principle, which is a version of induction specially adapted for reasoning about step-by-step processes.

## 5.1 Ordinary Induction

To understand how induction works, suppose there is a professor who brings a bottomless bag of assorted miniature candy bars to her large class. She offers to share the candy in the following way. First, she lines the students up in order. Next she states two rules:

1. The student at the beginning of the line gets a candy bar.
2. If a student gets a candy bar, then the following student in line also gets a candy bar.

Let's number the students by their order in line, starting the count with 0, as usual in computer science. Now we can understand the second rule as a short description of a whole sequence of statements:

- If student 0 gets a candy bar, then student 1 also gets one.
- If student 1 gets a candy bar, then student 2 also gets one.
- If student 2 gets a candy bar, then student 3 also gets one.

Of course, this sequence has a more concise mathematical description:

If student $n$ gets a candy bar, then student $n + 1$ gets a candy bar, for all nonnegative integers $n$.

So suppose you are student 17. By these rules, are you entitled to a miniature candy bar? Well, student 0 gets a candy bar by the first rule. Therefore, by the second rule, student 1 also gets one, which means student 2 gets one, which means student 3 gets one as well, and so on. By 17 applications of the professor's second rule, you get your candy bar! Of course the rules really guarantee a candy bar to every student, no matter how far back in line they may be.

### 5.1.1 A Rule for Ordinary Induction

The reasoning that led us to conclude that every student gets a candy bar is essentially all there is to induction.

**The Induction Principle**.

Let $P$ be a predicate on nonnegative integers. If

- $P(0)$ is true, and
- $P(n)$ IMPLIES $P(n + 1)$ for all nonnegative integers, $n$,

then

- $P(m)$ is true for all nonnegative integers, $m$.

Since we're going to consider several useful variants of induction in later sections, we'll refer to the induction method described above as ordinary induction when we need to distinguish it. Formulated as a proof rule as in Section 1.4.1, this would be

### Rule. Induction Rule

$$
\frac{P(0),\quad \forall n \in \mathbb{N}.\ P(n)\ \text{IMPLIES}\ P(n + 1)}{\forall m \in \mathbb{N}.\ P(m)}
$$

This Induction Rule works for the same intuitive reason that all the students get candy bars, and we hope the explanation using candy bars makes it clear why the soundness of ordinary induction can be taken for granted. In fact, the rule is so obvious that it's hard to see what more basic principle could be used to justify it (see Section 5.3). What's not so obvious is how much mileage we get by using it.

### 5.1.2 A Familiar Example

Below is the formula (5.1) for the sum of the nonnegative integers up to $n$. The formula holds for all nonnegative integers, so it is the kind of statement to which induction applies directly. We’ve already proved this formula using the Well Ordering Principle (Theorem 2.2.1), but now we’ll prove it *by induction*, that is, using the Induction Principle.

**Theorem 5.1.1**.

For all $n\in\mathbb{N}$,

$1+2+3+\cdots+n=\frac{n(n+1)}{2}$ (5.1)

To prove the theorem by induction, define predicate $P(n)$ to be the equation (5.1). Now the theorem can be restated as the claim that $P(n)$ is true for all $n\in\mathbb{N}$. This is great, because the Induction Principle lets us reach precisely that conclusion, provided we establish two simpler facts:

- $P(0)$ is true.
- For all $n\in\mathbb{N}$, $P(n)$ implies $P(n+1)$.

So now our job is reduced to proving these two statements.

The first statement follows because of the convention that a sum of zero terms is equal to $0$. So $P(0)$ is the true assertion that a sum of zero terms is equal to $0(0+1)/2=0$.

The second statement is more complicated. But remember the basic plan from Section 1.5 for proving the validity of any implication: *assume* the statement on the left and then *prove* the statement on the right. In this case, we assume $P(n)$—namely, equation (5.1)—in order to prove $P(n+1)$, which is the equation

$1+2+3+\cdots+n+(n+1)=\frac{(n+1)(n+2)}{2}.$ (5.2)

These two equations are quite similar; in fact, adding $(n+1)$ to both sides of equation (5.1) and simplifying the right side gives the equation (5.2):

$1+2+3+\cdots+n+(n+1)$ $=\frac{n(n+1)}{2}+(n+1)$
$=\frac{(n+2)(n+1)}{2}$

Thus, if $P(n)$ is true, then so is $P(n+1)$. This argument is valid for every nonnegative integer $n$, so this establishes the second fact required by the induction proof. Therefore, the Induction Principle says that the predicate $P(m)$ is true for all nonnegative integers, $m$. The theorem is proved.

####

### 5.1.3 A Template for Induction Proofs

The proof of equation (5.1) was relatively simple, but even the most complicated induction proof follows exactly the same template. There are five components:

1. State that the proof uses induction. This immediately conveys the overall structure of the proof, which helps your reader follow your argument.
2. Define an appropriate predicate  $P(n)$ . The predicate  $P(n)$  is called the induction hypothesis. The eventual conclusion of the induction argument will be that  $P(n)$  is true for all nonnegative  $n$ . A clearly stated induction hypothesis is often the most important part of an induction proof, and its omission is the largest source of confused proofs by students.

In the simplest cases, the induction hypothesis can be lifted straight from the proposition you are trying to prove, as we did with equation (5.1). Sometimes the induction hypothesis will involve several variables, in which case you should indicate which variable serves as  $n$ .

3. Prove that  $P(0)$  is true. This is usually easy, as in the example above. This part of the proof is called the base case or basis step.
4. Prove that  $P(n)$  implies  $P(n + 1)$  for every nonnegative integer  $n$ . This is called the inductive step. The basic plan is always the same: assume that  $P(n)$  is true and then use this assumption to prove that  $P(n + 1)$  is true. These two statements should be fairly similar, but bridging the gap may require some ingenuity. Whatever argument you give must be valid for every nonnegative integer  $n$ , since the goal is to prove that all the following implications are true:

$$
P (0) \rightarrow P (1), P (1) \rightarrow P (2), P (2) \rightarrow P (3), \dots .
$$

5. Invoke induction. Given these facts, the induction principle allows you to conclude that  $P(n)$  is true for all nonnegative  $n$ . This is the logical capstone to the whole argument, but it is so standard that it's usual not to mention it explicitly.

Always be sure to explicitly label the base case and the inductive step. Doing so will make your proofs clearer and will decrease the chance that you forget a key step—like checking the base case.
5.1. Ordinary Induction


### 5.1.4 A Clean Writeup

The proof of Theorem 5.1.1 given above is perfectly valid; however, it contains a lot of extraneous explanation that you won't usually see in induction proofs. The writeup below is closer to what you might see in print and should be prepared to produce yourself.

**Revised proof of Theorem 5.1.1.** We use induction. The induction hypothesis, $P(n)$, will be equation (5.1).

**Base case**: $P(0)$ is true, because both sides of equation (5.1) equal zero when $n = 0$.

**Inductive step**: Assume that $P(n)$ is true, that is equation (5.1) holds for some nonnegative integer $n$. Then adding $n + 1$ to both sides of the equation implies that

$$
\begin{array}{l}
1 + 2 + 3 + \rightarrow 4 n + (n + 1) = \frac{n(n + 1)}{2} + (n + 1) \\
= \frac{(n + 1)(n + 2)}{2} \quad \text{(by simple algebra)}
\end{array}
$$

which proves $P(n + 1)$.

So it follows by induction that $P(n)$ is true for all nonnegative $n$.

It probably bothers you that induction led to a proof of this summation formula but did not provide an intuitive way to understand it nor did it explain where the formula came from in the first place. This is both a weakness and a strength. It is a weakness when a proof does not provide insight. But it is a strength that a proof can provide a reader with a reliable guarantee of correctness without requiring insight.

### 5.1.5 A More Challenging Example

During the development of MIT's famous Stata Center, as costs rose further and further beyond budget, some radical fundraising ideas were proposed. One rumored plan was to install a big square courtyard divided into unit squares. The big square would be $2^n$ units on a side for some undetermined nonnegative integer $n$, and one of the unit squares in the center (in the special case $n = 0$, the whole courtyard consists of a single central square; otherwise, there are four central squares) occupied by a statue of a wealthy potential donor—whom the fund raisers privately referred to as "Bill." The $n = 3$ case is shown in Figure 5.1.

A complication was that the building's unconventional architect, Frank Gehry, was alleged to require that only special L-shaped tiles (shown in Figure 5.2) be


![img-0.jpeg](08 - Induction_images/img-0.jpeg)
Figure 5.1 A  $2^{n} \times 2^{n}$  courtyard for  $n = 3$ .

![img-1.jpeg](08 - Induction_images/img-1.jpeg)
Figure 5.2 The special L-shaped tile.

used for the courtyard. For  $n = 2$ , a courtyard meeting these constraints is shown in Figure 5.3. But what about for larger values of  $n$ ? Is there a way to tile a  $2^{n} \times 2^{n}$  courtyard with L-shaped tiles around a statue in the center? Let's try to prove that this is so.

**Theorem 5.1.2. For all  $n \geq 0$  there exists a tiling of a  $2^n \times 2^n$  courtyard with Bill in a central square**

Proof. (doomed attempt) The proof is by induction. Let  $P(n)$  be the proposition that there exists a tiling of a  $2^n \times 2^n$  courtyard with Bill in the center.

Base case:  $P(0)$  is true because Bill fills the whole courtyard.

Inductive step: Assume that there is a tiling of a  $2^{n} \times 2^{n}$  courtyard with Bill in the center for some  $n \geq 0$ . We must prove that there is a way to tile a  $2^{n+1} \times 2^{n+1}$  courtyard with Bill in the center ...

Now we're in trouble! The ability to tile a smaller courtyard with Bill in the

center isn't much help in tiling a larger courtyard with Bill in the center. We haven't figured out how to bridge the gap between  $P(n)$  and  $P(n + 1)$ .

So if we're going to prove Theorem 5.1.2 by induction, we're going to need some other induction hypothesis than simply the statement about  $n$  that we're trying to prove.

When this happens, your first fallback should be to look for a stronger induction hypothesis; that is, one which implies your previous hypothesis. For example, we could make  $P(n)$  the proposition that for every location of Bill in a  $2^{n} \times 2^{n}$  courtyard, there exists a tiling of the remainder.

This advice may sound bizarre: "If you can't prove something, try to prove something grander!" But for induction arguments, this makes sense. In the inductive step, where you have to prove  $P(n)$  IMPLIES  $P(n + 1)$ , you're in better shape because you can assume  $P(n)$ , which is now a more powerful statement. Let's see how this plays out in the case of courtyard tiling.

Proof (successful attempt). The proof is by induction. Let  $P(n)$  be the proposition that for every location of Bill in a  $2^n \times 2^n$  courtyard, there exists a tiling of the remainder.

Base case:  $P(0)$  is true because Bill fills the whole courtyard.

Inductive step: Assume that  $P(n)$  is true for some  $n \geq 0$ ; that is, for every location of Bill in a  $2^n \times 2^n$  courtyard, there exists a tiling of the remainder. Divide the  $2^{n+1} \times 2^{n+1}$  courtyard into four quadrants, each  $2^n \times 2^n$ . One quadrant contains Bill (B in the diagram below). Place a temporary Bill (X in the diagram) in each of the three central squares lying outside this quadrant as shown in Figure 5.4.

![img-3.jpeg](08 - Induction_images/img-3.jpeg)
Figure 5.4 Using a stronger inductive hypothesis to prove Theorem 5.1.2.

Now we can tile each of the four quadrants by the induction assumption. Replacing the three temporary Bills with a single L-shaped tile completes the job. This proves that  $P(n)$  implies  $P(n + 1)$  for all  $n \geq 0$ . Thus  $P(m)$  is true for all  $m \in \mathbb{N}$ , and the theorem follows as a special case where we put Bill in a central square**

This proof has two nice properties. First, not only does the argument guarantee that a tiling exists, but also it gives an algorithm for finding such a tiling. Second, we have a stronger result: if Bill wanted a statue on the edge of the courtyard, away from the pigeons, we could accommodate him!

Strengthening the induction hypothesis is often a good move when an induction proof won't go through. But keep in mind that the stronger assertion must actually be true; otherwise, there isn't much hope of constructing a valid proof. Sometimes finding just the right induction hypothesis requires trial, error, and insight. For example, mathematicians spent almost twenty years trying to prove or disprove the conjecture that every planar graph is 5-choosable. Then, in 1994, Carsten Thomassen gave an induction proof simple enough to explain on a napkin. The key turned out to be finding an extremely clever induction hypothesis; with that in hand, completing the argument was easy!
5.1. Ordinary Induction 123

5.1.6 A Faulty Induction Proof

If we have done a good job in writing this text, right about now you should be thinking, “Hey, this induction stuff isn’t so hard after all—just show $P(0)$ is true and that $P(n)$ implies $P(n + 1)$ for any number $n$.” And, you would be right, although sometimes when you start doing induction proofs on your own, you can run into trouble. For example, we will now use induction to “prove” that all horses are the same color—just when you thought it was safe to skip class and work on your robot program instead. Sorry!

False Theorem. All horses are the same color.

Notice that no $n$ is mentioned in this assertion, so we’re going to have to re-formulate it in a way that makes an $n$ explicit. In particular, we’ll (falsely) prove that

False Theorem 5.1.3. In every set of $n \geq 1$ horses, all the horses are the same color.

This is a statement about all integers $n \geq 1$ rather $\geq 0$, so it’s natural to use a slight variation on induction: prove $P(1)$ in the base case and then prove that $P(n)$ implies $P(n + 1)$ for all $n \geq 1$ in the inductive step. This is a perfectly valid variant of induction and is not the problem with the proof below.

Bogus proof. The proof is by induction on $n$. The induction hypothesis, $P(n)$, will be

In every set of $n$ horses, all are the same color. (5.3)

Base case: $(n = 1)$. $P(1)$ is true, because in a size-1 set of horses, there’s only one horse, and this horse is definitely the same color as itself.

Inductive step: Assume that $P(n)$ is true for some $n \geq 1$. That is, assume that in every set of $n$ horses, all are the same color. Now suppose we have a set of $n + 1$ horses:

$$
h_1, h_2, \dots, h_n, h_{n+1}.
$$

We need to prove these $n + 1$ horses are all the same color.

By our assumption, the first $n$ horses are the same color:

$$
\underbrace{h_1, h_2, \dots, h_n}_{\text{same color}}, h_{n+1}
$$

Also by our assumption, the last $n$ horses are the same color:

$$
h_1, \underbrace{h_2, \dots, h_n, h_{n+1}}_{\text{same color}}
$$

So $h_1$ is the same color as the remaining horses besides $h_{n+1}$ —that is, $h_2, \ldots, h_n$. Likewise, $h_{n+1}$ is the same color as the remaining horses besides $h_1$ —that is, $h_2, \ldots, h_n$, again. Since $h_1$ and $h_{n+1}$ are the same color as $h_2, \ldots, h_n$, all $n+1$ horses must be the same color, and so $P(n+1)$ is true. Thus, $P(n)$ implies $P(n+1)$.

By the principle of induction, $P(n)$ is true for all $n \geq 1$.

We’ve proved something false! Does this mean that math broken and we should all take up poetry instead? Of course not! It just means that this proof has a mistake.

The mistake in this argument is in the sentence that begins “So $h_1$ is the same color as the remaining horses besides $h_{n+1}$ —that is $h_2, \ldots, h_n, \ldots$.” The ellipsis notation (“...”) in the expression “$h_1, h_2, \ldots, h_n, h_{n+1}$” creates the impression that there are some remaining horses—namely $h_2, \ldots, h_n$ —besides $h_1$ and $h_{n+1}$. However, this is not true when $n = 1$. In that case, $h_1, h_2, \ldots, h_n, h_{n+1}$ is just $h_1, h_2$ and there are no “remaining” horses for $h_1$ to share a color with. And of course, in this case $h_1$ and $h_2$ really don’t need to be the same color.

This mistake knocks a critical link out of our induction argument. We proved $P(1)$ and we correctly proved $P(2) \longrightarrow P(3)$, $P(3) \longrightarrow P(4)$, etc. But we failed to prove $P(1) \longrightarrow P(2)$, and so everything falls apart: we cannot conclude that $P(2)$, $P(3)$, etc., are true. And naturally, these propositions are all false; there are sets of $n$ horses of different colors for all $n \geq 2$.

Students sometimes explain that the mistake in the proof is because $P(n)$ is false for $n \geq 2$, and the proof assumes something false, $P(n)$, in order to prove $P(n + 1)$. You should think about how to help such a student understand why this explanation would get no credit on a Math for Computer Science exam.

## 5.2 Strong Induction

A useful variant of induction is called strong induction. Strong induction and ordinary induction are used for exactly the same thing: proving that a predicate is true for all nonnegative integers. Strong induction is useful when a simple proof that the predicate holds for $n + 1$ does not follow just from the fact that it holds at $n$, but from the fact that it holds for other values $\leq n$.
5.2. Strong Induction


### 5.2.1 A Rule for Strong Induction

### Principle of Strong Induction.

Let $P$ be a predicate on nonnegative integers. If

- $P(0)$ is true, and
- for all $n \in \mathbb{N}$, $P(0), P(1), \ldots, P(n)$ together imply $P(n + 1)$,

then $P(m)$ is true for all $m \in \mathbb{N}$.

The only change from the ordinary induction principle is that strong induction allows you make more assumptions in the inductive step of your proof! In an ordinary induction argument, you assume that $P(n)$ is true and try to prove that $P(n + 1)$ is also true. In a strong induction argument, you may assume that $P(0), P(1), \ldots,$ and $P(n)$ are all true when you go to prove $P(n + 1)$. So you can assume a stronger set of hypotheses which can make your job easier.

Formulated as a proof rule, strong induction is

**Rule. Strong Induction Rule**

$$
\frac{P(0), \quad \forall n \in \mathbb{N}. \left(P(0) \text{ AND } P(1) \text{ AND } \ldots \text{ AND } P(n)\right) \text{ IMPLIES } P(n + 1)}{\forall m \in \mathbb{N}. P(m)}
$$

Stated more succinctly, the rule is

**Rule.**

$$
\frac{P(0), \quad [\forall k \leq n \in \mathbb{N}. P(k)] \text{ IMPLIES } P(n + 1)}{\forall m \in \mathbb{N}. P(m)}
$$

The template for strong induction proofs is identical to the template given in Section 5.1.3 for ordinary induction except for two things:

- you should state that your proof is by strong induction, and
- you can assume that $P(0), P(1), \ldots, P(n)$ are all true instead of only $P(n)$ during the inductive step.

### 5.2.2 Products of Primes

As a first example, we'll use strong induction to re-prove Theorem 2.3.1 which we previously proved using Well Ordering.

Theorem. Every integer greater than 1 is a product of primes.

Proof. We will prove the Theorem by strong induction, letting the induction hypothesis, $P(n)$, be

$n$ is a product of primes.

So the Theorem will follow if we prove that $P(n)$ holds for all $n \geq 2$.

Base Case: $(n = 2)$: $P(2)$ is true because 2 is prime, so it is a length one product of primes by convention.

Inductive step: Suppose that $n \geq 2$ and that every number from 2 to $n$ is a product of primes. We must show that $P(n + 1)$ holds, namely, that $n + 1$ is also a product of primes. We argue by cases:

If $n + 1$ is itself prime, then it is a length one product of primes by convention, and so $P(n + 1)$ holds in this case.

Otherwise, $n + 1$ is not prime, which by definition means $n + 1 = k \cdot m$ for some integers $k, m$ between 2 and $n$. Now by the strong induction hypothesis, we know that both $k$ and $m$ are products of primes. By multiplying these products, it follows immediately that $k \cdot m = n + 1$ is also a product of primes. Therefore, $P(n + 1)$ holds in this case as well.

So $P(n + 1)$ holds in any case, which completes the proof by strong induction that $P(n)$ holds for all $n \geq 2$.

### 5.2.3 Making Change

The country Inductia, whose unit of currency is the Strong, has coins worth $3\mathrm{Sg}$ (3 Strongs) and $5\mathrm{Sg}$. Although the Inductians have some trouble making small change like $4\mathrm{Sg}$ or $7\mathrm{Sg}$, it turns out that they can collect coins to make change for any number that is at least 8 Strongs.

Strong induction makes this easy to prove for $n + 1 \geq 11$, because then $(n + 1) - 3 \geq 8$, so by strong induction the Inductians can make change for exactly $(n + 1) - 3$ Strongs, and then they can add a $3\mathrm{Sg}$ coin to get $(n + 1)\mathrm{Sg}$. So the only thing to do is check that they can make change for all the amounts from 8 to $10\mathrm{Sg}$, which is not too hard to do.

Here's a detailed writeup using the official format:

Proof. We prove by strong induction that the Inductians can make change for any amount of at least $8\mathrm{Sg}$. The induction hypothesis, $P(n)$ will be:

There is a collection of coins whose value is $n + 8$ Strongs.
5.2. Strong Induction

![img-4.jpeg](08 - Induction_images/img-4.jpeg)
Figure 5.5 One way to make  $26\mathrm{Sg}$  using Strongian currency

We now proceed with the induction proof:

Base case:  $P(0)$  is true because a 3Sg coin together with a 5Sg coin makes 8Sg.

Inductive step: We assume  $P(k)$  holds for all  $k \leq n$ , and prove that  $P(n + 1)$  holds. We argue by cases:

Case  $(n + 1 = 1)$ : We have to make  $(n + 1) + 8 = 9\mathrm{Sg}$ . We can do this using three 3Sg coins.

Case  $(n + 1 = 2)$ : We have to make  $(n + 1) + 8 = 10\mathrm{Sg}$ . Use two  $5\mathrm{Sg}$  coins.

Case  $(n + 1 \geq 3)$ : Then  $0 \leq n - 2 \leq n$ , so by the strong induction hypothesis, the Inductians can make change for  $(n - 2) + 8\mathrm{Sg}$ . Now by adding a  $3\mathrm{Sg}$  coin, they can make change for  $(n + 1) + 8\mathrm{Sg}$ , so  $P(n + 1)$  holds in this case.

Since  $n \geq 0$ , we know that  $n + 1 \geq 1$  and thus that the three cases cover every possibility. Since  $P(n + 1)$  is true in every case, we can conclude by strong induction that for all  $n \geq 0$ , the Inductians can make change for  $n + 8$  Strong. That is, they can make change for any number of eight or more Strong.

### 5.2.4 The Stacking Game

Here is another exciting game that's surely about to sweep the nation!

You begin with a stack of  $n$  boxes. Then you make a sequence of moves. In each move, you divide one stack of boxes into two nonempty stacks. The game ends when you have  $n$  stacks, each containing a single box. You earn points for each move; in particular, if you divide one stack of height  $a + b$  into two stacks with heights  $a$  and  $b$ , then you score  $ab$  points for that move. Your overall score is the sum of the points that you earn for each move. What strategy should you use to maximize your total score?

![img-5.jpeg](08 - Induction_images/img-5.jpeg)
Figure 5.6 An example of the stacking game with  $n = 10$  boxes. On each line, the underlined stack is divided in the next step.

As an example, suppose that we begin with a stack of  $n = 10$  boxes. Then the game might proceed as shown in Figure 5.6. Can you find a better strategy?

## Analyzing the Game

Let's use strong induction to analyze the unstacking game. We'll prove that your score is determined entirely by the number of boxes—your strategy is irrelevant!

**Theorem 5.2.1. Every way of unstacking  $n$  blocks gives a score of  $n(n - 1) / 2$  points**

There are a couple technical points to notice in the proof:

- The template for a strong induction proof mirrors the one for ordinary induction.
- As with ordinary induction, we have some freedom to adjust indices. In this case, we prove  $P(1)$  in the base case and prove that  $P(1), \ldots, P(n)$  imply  $P(n + 1)$  for all  $n \geq 1$  in the inductive step.

Proof. The proof is by strong induction. Let  $P(n)$  be the proposition that every way of unstacking  $n$  blocks gives a score of  $n(n - 1) / 2$ .

Base case: If  $n = 1$ , then there is only one block. No moves are possible, and so the total score for the game is  $1(1 - 1) / 2 = 0$ . Therefore,  $P(1)$  is true.
5.3. Strong Induction vs. Induction vs. Well Ordering

Inductive step: Now we must show that $P(1), \ldots, P(n)$ imply $P(n + 1)$ for all $n \geq 1$. So assume that $P(1), \ldots, P(n)$ are all true and that we have a stack of $n + 1$ blocks. The first move must split this stack into substacks with positive sizes $a$ and $b$ where $a + b = n + 1$ and $0 < a, b \leq n$. Now the total score for the game is the sum of points for this first move plus points obtained by unstacking the two resulting substacks:

$$
\begin{array}{l}
\text{total score} = (\text{score for 1st move}) \\
\quad + (\text{score for unstacking } a \text{ blocks}) \\
\quad + (\text{score for unstacking } b \text{ blocks}) \\
= ab + \frac{a(a - 1)}{2} + \frac{b(b - 1)}{2} \quad \text{by } P(a) \text{ and } P(b) \\
= \frac{(a + b)^2 - (a + b)}{2} = \frac{(a + b)((a + b) - 1)}{2} \\
= \frac{(n + 1)n}{2}
\end{array}
$$

This shows that $P(1), P(2), \ldots, P(n)$ imply $P(n + 1)$.

Therefore, the claim is true by strong induction.

## 5.3 Strong Induction vs. Induction vs. Well Ordering

Strong induction looks genuinely "stronger" than ordinary induction —after all, you can assume a lot more when proving the induction step. Since ordinary induction is a special case of strong induction, you might wonder why anyone would bother with the ordinary induction.

But strong induction really isn't any stronger, because a simple text manipulation program can automatically reformat any proof using strong induction into a proof using ordinary induction—just by decorating the induction hypothesis with a universal quantifier in a standard way. Still, it's worth distinguishing these two kinds of induction, since which you use will signal whether the inductive step for $n + 1$ follows directly from the case for $n$ or requires cases smaller than $n$, and that is generally good for your reader to know.

The template for the two kinds of induction rules looks nothing like the one for the Well Ordering Principle, but this chapter included a couple of examples where induction was used to prove something already proved using well ordering. In fact, this can always be done. As the examples may suggest, any well ordering proof can automatically be reformatted into an induction proof. So theoretically, no one

need bother with the Well Ordering Principle either.

But it's equally easy to go the other way, and automatically reformat any strong induction proof into a Well Ordering proof. The three proof methods—well ordering, induction, and strong induction—are simply different formats for presenting the same mathematical reasoning!

So why three methods? Well, sometimes induction proofs are clearer because they don't require proof by contradiction. Also, induction proofs often provide recursive procedures that reduce large inputs to smaller ones. On the other hand, well ordering can come out slightly shorter and sometimes seem more natural and less worrisome to beginners.

So which method should you use? There is no simple recipe. Sometimes the only way to decide is to write up a proof using more than one method and compare how they come out. But whichever method you choose, be sure to state the method up front to help a reader follow your proof.
