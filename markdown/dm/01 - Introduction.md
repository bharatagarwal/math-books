## 1 Introduction

For most students, the first and often only area of mathematics in college is calculus. And it is true that calculus is the single most important field of mathematics, whose emergence in the 17th century signalled the birth of modern mathematics and was the key to the successful applications of mathematics in the sciences.

But calculus (or analysis) is also very technical. It takes a lot of work even to introduce its fundamental notions like continuity or derivatives (after all, it took 2 centuries just to define these notions properly). To get a feeling for the power of its methods, say by describing one of its important applications in detail, takes years of study.

If you want to become a mathematician, computer scientist, or engineer, this investment is necessary. But if your goal is to develop a feeling for what mathematics is all about, where is it that mathematical methods can be helpful, and what kind of questions do mathematicians work on, you may want to look for the answer in some other fields of mathematics.

There are many success stories of applied mathematics outside calculus. A recent hot topic is mathematical cryptography, which is based on number theory (the study of positive integers $1,2,3,\ldots$), and is widely applied, among others, in computer security and electronic banking. Other important areas in applied mathematics include linear programming, coding theory, theory of computing. The mathematics in these applications is collectively called *discrete mathematics*. (“Discrete” here is used as the opposite of “continuous”; it is also often used in the more restrictive sense of “finite”.)

The aim of this book is not to cover “discrete mathematics” in depth (it should be clear from the description above that such a task would be ill-defined and impossible anyway). Rather, we discuss a number of selected results and methods, mostly from the areas of combinatorics, graph theory, and combinatorial geometry, with a little elementary number theory.

At the same time, it is important to realize that mathematics cannot be done without *proofs*. Merely stating the facts, without saying something about why these facts are valid, would be terribly far from the spirit of mathematics and would make it impossible to give any idea about how it works. Thus, wherever possible, we’ll give the proofs of the theorems we state. Sometimes this is not possible; quite simple, elementary facts can be extremely difficult to prove, and some such proofs may take advanced courses to go through. In these cases, we’ll state at least that the proof is highly technical and goes beyond the scope of this book.

In this reader we take that insistence on proof one step further: every claim is backed by real, runnable tooling rather than taken on faith, complementing pen-and-paper proofs with machine verification and picking the tool that fits each kind of statement. Throughout the book you will meet the same small toolchain, all invoked the same way — `uv run --with <pkg> python <file>` for Python (no `pip`, no virtualenv), or `lean <file>` / `dafny verify <file>` for proof assistants:

- **sympy** — symbolic algebra. Proves identities and closed forms for *all* values of a variable at once (e.g. $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$), the natural fit for the algebraic facts in combinatorics.
- **z3** — an SMT solver. Decides logical/arithmetic constraints and quantified statements ($\forall$, $\exists$), ideal for the existence and counting puzzles to come.
- **networkx** — graph algorithms and data structures, for the graph-theory chapters that form the spine of this book.
- **hypothesis** — property-based testing. Throws hundreds of random inputs at a claimed property to hunt for counterexamples before we try to prove there are none.
- **Lean4 / Dafny** — full proof assistants. When we want a statement checked *to the foundations* (Lean) or an algorithm checked against pre/post-conditions and loop invariants (Dafny).

The smallest possible instance of this methodology lives right here in the introduction. The book frames number theory as the study of the positive integers $1,2,3,\ldots$; the first closed form one ever meets about those integers is $1+2+\cdots+n = \frac{n(n+1)}{2}$. Rather than plugging in numbers, we can let a computer algebra system verify it symbolically: `sympy.Sum` evaluates the sum over a *symbolic* upper bound $n$, and we confirm that the result minus $\frac{n(n+1)}{2}$ simplifies to $0$ — a proof for every $n$ at once. We also spot-check $n=100$, reproducing the classic Gauss total $5050$.

```python
<!-- include: code/dm/01 - Introduction/01_python.py -->
```

Running it prints `sympy evaluates  1 + 2 + ... + n  = n**2/2 + n/2`, then `closed_form - n(n+1)/2 simplifies to: 0` and `spot check n=100:  1 + 2 + ... + 100 = 5050`, confirming the closed form holds symbolically for all $n$ and matches the hand computation at $n=100$.

Another important ingredient of mathematics is *problem solving*. You won’t be able to learn any mathematics without dirtying your hands and trying out the ideas you learn about in the solution of problems. To some, this may sound frightening, but in fact most people pursue this type of activity almost every day: everybody who plays a game of chess, or solves a puzzle, is solving discrete mathematical problems. The reader is strongly advised to answer the questions posed in the text and to go through the problems at the end of each chapter of this book. Treat it as puzzle solving, and if you find some idea that you come up with in the solution to play some role later, be satisfied that you are beginning to get the essence of how mathematics develops.

We hope that we can illustrate that mathematics is a building, where results are built on earlier results, often going back to the great Greek mathematicians; that mathematics is alive, with more new ideas and more pressing unsolved problems than ever; and that mathematics is an art, where the beauty of ideas and methods is as important as their difficulty or applicability.
