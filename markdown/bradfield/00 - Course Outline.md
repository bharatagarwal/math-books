# Mathematics for Computing — Course Outline

*Bradfield School of Computer Science · June–July 2020 · with Tom Alcorn*

> If people do not believe that mathematics is simple, it is only because they
> do not realize how complicated life is.
> — John von Neumann

Computer science is in some ways an overgrown branch of applied mathematics.
While many software engineers try — and to varying degrees succeed — at ignoring
this, this course embraces it with direct study. Most of the course focuses on
topics in **discrete mathematics**, with occasional detours to other areas that
have proved important in computing, such as **linear algebra**.

This page is the original Bradfield syllabus. The chapters that follow in this
book take each of its twelve sessions and expand them into a self-contained,
worked lesson aimed at a programmer: the core ideas in real notation, with
runnable `sympy` / `z3` / `numpy` / `networkx` demos woven in at each concept so
the math and the code read as one argument, plus solutions to the session's
problem set. Read this outline for the map; read the chapters for the territory.

## Recommended Resources

In this course, classes are highly interactive and problem-solving based. For
this reason it is important to complete all of the pre-work for class.

The course's **main text** is a set of discrete-mathematics lecture notes
(referred to as **LL**) that László Lovász wrote for a course at Yale. Lovász did
a good job of making the content approachable and intuitive, so it is a better
starting point than more formal texts. Those notes are the **Discrete
Mathematics** book in this reader.

> László Lovász (pronounced "lo-varsh") is a Hungarian mathematician known for
> his contributions to combinatorics — the focus of our early classes in
> particular. He is a fellow of the American Mathematical Society, received the
> 1999 Knuth Prize for his contributions to computer science, and the 2021 Abel
> Prize.

The course also makes use of **Mathematics for Computer Science** (**MCS**), the
book-length lecture notes for a course of the same name at MIT (also the
**Mathematics for Computer Science** book in this reader). It is somewhat more
technical but also approachable, with a little patience. The video lectures for
that course (MIT 6.042J) are freely available and referenced below.

For those who would prefer a traditional discrete-mathematics textbook, the
course suggests Rosen's *Discrete Mathematics and its Applications* (7th
edition), referenced below as **Rosen**.

## 1. Counting

We start gently, by ensuring we know how to count things correctly. We will see
that it is worth employing more rigor here than we might otherwise have imagined.

- **Pre-class:** LL chapter 2, [*Let us count!*](#dm/1), and chapter 4,
  [*Counting subsets*](#dm/3), doing as many exercises as you need.
- **Post-class:** from MCS chapter 15, *Cardinality Rules*: problems 15.1–4,
  15.21, 15.34, 15.38; a few subproblems from 15.26. Stretch: 15.9, 15.11.
- **Further:** Rosen chapter 2, *Basic Structures: Sets, Functions, Sequences,
  Sums, and Matrices*; the first six sections of his chapter 6, *Counting*; and
  sections 8.4–8.6 (*Generating Functions*, *Inclusion–Exclusion* and its
  applications). In MCS, chapters 14–16: *Sums and Asymptotics*, *Cardinality
  Rules*, and *Generating Functions*. The 6.042J videos *Counting Rules 1 & 2*.
  Counting benefits from set theory — see the very short *Naïve Set Theory*
  (Halmos).

## 2. Probability

One of the most common applications of "counting things" is to count the possible
states from which a choice is randomly made. This brings us to probability, which
we explore in a little more depth.

- **Pre-class:** LL chapter 7, [*Combinatorial probability*](#dm/6); MCS
  problems 17.2 and 17.3, from chapter 17, *Events and Probability Spaces*.
- **Post-class:** MCS problems 17.3 and 17.4.
- **Further:** Rosen chapter 7, *Discrete Probability*. In MCS, the full
  probability run of chapters 17–21: *Events and Probability Spaces*,
  *Conditional Probability*, *Random Variables*, *Deviation from the Mean*,
  and *Random Walks*. The 6.042J probability videos. For a
  superb interactive exposition, see [Seeing Theory](https://seeing-theory.brown.edu/)
  ("A visual introduction to probability and statistics").

## 3. Bayes' Rule

We continue our coverage of probability, focusing on conditional probability and
Bayes' rule.

- **Pre-class:** check with your instructor; in the absence of guidance, enough
  of MCS chapter 18, *Conditional Probability*, to attempt problems 18.2, 18.7,
  18.26.
- **Post-class:** MCS problem 18.37 (c)(d)(e).
- **Further:** to dive deeper, *Introduction to Probability* by Bertsekas &
  Tsitsiklis.

## 4. Logic

Logic is literally at the core of computing, from transistors up through many
layers of abstraction to our languages and interfaces. This class gives us the
vocabulary and the extra level of understanding that comes from exploring the
mathematical formalisms of logic.

> Using boolean logic to model digital circuits was not at all obvious, and was
> one of the most important breakthroughs in computing. For it we can thank
> Claude Shannon, who — working in the control room of the Differential Analyzer
> at MIT — figured the switching and relay circuits could be rationalized using a
> then-obscure novelty from an undergraduate philosophy class: George Boole's
> algebra. Shannon's *A Symbolic Analysis of Relay Switching Circuits* may be the
> most consequential master's thesis of all time; he went on to invent
> Information Theory.

- **Pre-class:** MCS chapter 3, [*Logical Formulas*](#mcs/3) (this topic is not
  covered in LL).
- **Post-class:** MCS problems 3.1, 3.2, 3.5.
- **Further:** Rosen chapter 1, *The Foundations: Logic and Proofs*; for a
  theoretical but approachable treatment, *Introduction to Logic* by Patrick
  Suppes.

## 5. Proofs

Using our understanding of propositional logic, we can begin to construct formal
proofs. Even when we do not use proofs to *guarantee* program correctness, the
habit imparts rigor to how we reason about software.

- **Pre-class:** MCS chapter 1, [*What is a Proof?*](#mcs/0) (not covered in
  LL).
- **Post-class:** from the same chapter: problem 1.3 (hint: assume
  $\sqrt{x}^{2}=x$); problem 1.8 (hint: cases $r<s$, $r>s$, $r=s$); and show that
  if $a^{3}>a$ then $a^{5}>a$.
- **Further:** 6.042J video *Introduction and Proofs*; the excellent *How to
  Prove It: A Structured Approach* (Velleman); and, for a programmer's take, *The
  Reasoned Schemer*.

> The entire *Little Schemer* series uses a side-by-side question-and-answer
> format that is excellent for self-teaching. In *The Reasoned Schemer* you
> implement the embedded logic-programming language miniKanren — a kind of
> simplified modern Prolog — by answering its questions.

## 6. Induction and Recursive Data Types

In this class we cover the mathematical basis of recursion, used for both proofs
and calculations.

- **Pre-class:** LL chapter 3, [*Induction*](#dm/2).
- **Post-class:** from MCS chapter 5, [*Induction*](#mcs/7): problems 5.1, 5.4,
  5.7, 5.8, 5.13. Stretch: 5.21.
- **Further:** Rosen chapter 5, *Induction and Recursion*. In MCS, chapter 5,
  [*Induction*](#mcs/7), chapter 7, [*Recursive Data Types*](#mcs/9), and
  chapter 22, *Recurrences*. The 6.042J videos *Induction*, *Divide and Conquer
  Recurrences*, and *Linear Recurrences*. For a programmer's perspective, *The
  Little Prover*.

## 7. Linear Algebra

In a single class we attempt to get to the root of a vast field: linear algebra,
the basis of computer graphics and machine learning, among other applications.

- **Pre-class:** watch 3Blue1Brown's [*Essence of Linear Algebra*](https://www.3blue1brown.com/topics/linear-algebra)
  videos 1–7.
- **Further:** Gilbert Strang's MIT OpenCourseWare lectures (18.06) and his
  *Introduction to Linear Algebra*; the BetterExplained post *An Intuitive Guide
  to Linear Algebra*; the interactive online book [*immersive linear
  algebra*](https://immersivemath.com/ila/); and, for programmers, *Coding the
  Matrix* (Klein) and its exercises.

> The *Essence of Linear Algebra* series is by Grant Sanderson, whose channel
> 3Blue1Brown builds strong geometric intuition for ideas usually presented
> symbolically. The *Essence of Calculus* series is similarly excellent.

## 8. Linear Algebra 2

We continue our study of linear algebra, with a focus on applications.

- **Pre-class:** depends on how much the prior class covered — check with your
  instructor.

## 9. Graph Theory

We cover the mathematical foundation of the trees and graphs you know from
algorithms and data structures. Beyond the traversal algorithms of day-to-day
work, graph theory takes a more analytical approach, identifying interesting
properties and substructures of graphs.

- **Pre-class:** LL chapter 9, [*Graphs*](#dm/8), and chapter 12, [*Matchings
  in graphs*](#dm/11).
- **Further:** Rosen chapter 10, *Graphs*. In MCS, chapters 10–13: *Directed
  Graphs & Partial Orders*, *Communication Networks*, *Simple Graphs*, and
  *Planar Graphs*. The 6.042J videos *Graph Theory 1, 2, 3*.

## 10. Number Theory

We dip our toes into number theory — a branch of pure mathematics that has found
remarkable applications in computing. Our objective is to build the foundation we
need to understand public-key cryptography.

- **Pre-class:** LL chapter 8, [*Integers, divisors, and primes*](#dm/7).
- **Further:** Rosen chapter 4, *Number Theory and Cryptography*; MCS chapter 9,
  *Number Theory*; the 6.042J videos *Number Theory 1 & 2*. For a traditional
  treatment, *A Course in Number Theory and Cryptography* (Koblitz).

## 11. Cryptography

Now that we have a basic understanding of number theory, we explore one of its
most famous applications: public-key cryptography.

- **Pre-class:** LL chapter 15, [*A glimpse of cryptography*](#dm/14), and
  chapter 16, [*One-time pads*](#dm/15), aiming to understand the RSA scheme —
  the *Public key cryptography* section of chapter 16 — and its dependencies.
- **Further:** Brit Cruise's Khan Academy course *Journey into Cryptography*; the
  [Cryptopals Crypto Challenges](https://cryptopals.com/) (with Maciej
  Cegłowski's ringing endorsement); and, traditionally, *A Course in Number
  Theory and Cryptography*.

## 12. Revision and Problem-Solving Practice

Our final lesson is an opportunity to revise content covered throughout the
course and reinforce our understanding with further problem solving.

There is much more to learn in mathematics, and many angles from which to revisit
the topics you have seen. Two broadly valuable books for recent students of the
course: *Discrete Mathematics using a Computer*, where you learn (or re-learn)
discrete math by writing short Haskell programs; and the single 1000-plus-page
*Princeton Companion to Applied Mathematics* — the one book you might hope to have
on a desert island (there is also an original *Princeton Companion to
Mathematics*, covering pure mathematics).
