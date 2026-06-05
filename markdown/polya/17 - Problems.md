# Problems

This last part offers you additional opportunity for practice. The problems require no more preliminary knowledge than the earlier chapters supply. Yet they are not routine; some demand originality and ingenuity.

## How to use these problems

Pick a problem. Work it seriously before looking at the hint. If you are stuck after a genuine effort, read the hint — it names the move, usually as a question. If the hint is not enough, read the solution sketch, but stop as soon as you see the key idea, close the page, and finish it yourself.

If you solve a problem by your own means, you can still learn something by comparing your method with the one printed here. The reader who has earnestly tried to solve a problem has the best chance to profit from the hint and the solution. If, after a serious effort, you are inclined to give up, the hint may supply the missing idea. If even the hint does not help, look at the solution, isolate the key idea, put the book aside, and try to work out the solution from that idea alone.

Every problem below exercises at least one named heuristic move. The tag after each problem tells you which move is central. This is not a spoiler — knowing that a problem is about specialization does not tell you *how* to specialize. But after you solve it (or fail), the tag helps you file the experience: next time you are stuck, you have one more memory of what that move looks like in action.

Work with pencil and paper first. Code is a verification tool, not a discovery tool. If you want to check a conjecture by brute force, do it after you have the conjecture, not before.

## Problems by heuristic move

### Understanding the problem

**Problem 1.** A bear, starting from the point $P$, walked one mile due south. Then he changed direction and walked one mile due east. Then he turned again to the left and walked one mile due north, and arrived exactly at the point $P$ he started from. What was the color of the bear?

*Move: examine whether the condition is satisfiable; question your assumptions about the setup.*

**Problem 2.** Bob wants a piece of land, exactly level, with four boundary lines. Two run exactly north-south, two exactly east-west, and each measures exactly 100 feet. Can Bob buy such a piece of land in the U.S.?

*Move: do you know a related problem? Connect this to Problem 1's reasoning about the sphere. A square on a flat map is not a square on a sphere.*

**Problem 3.** Bob has 10 pockets and 44 silver dollars. He wants to distribute his dollars into his pockets so that each pocket contains a different number of dollars. Can he do so?

*Move: restate the problem; find the hidden constraint.*

**Problem 4.** To number the pages of a bulky volume, the printer used 2989 digits. How many pages has the volume?

*Move: separate the condition into parts; solve a related, simpler problem first.*

### Specialization and small cases

**Problem 5.** Observe that

$$\frac{1}{2!} + \frac{2}{3!} + \frac{3}{4!} + \cdots + \frac{n}{(n+1)!}$$

equals $1/2$ for $n = 1$, equals $5/6$ for $n = 2$, equals $23/24$ for $n = 3$. Guess the general formula, verify it for $n = 4$, and prove it.

*Move: compute small cases; recognize a pattern; use mathematical induction.*

**Problem 6.** Consider the table:

$$
\begin{aligned}
1 &= 1 \\
3 + 5 &= 8 \\
7 + 9 + 11 &= 27 \\
13 + 15 + 17 + 19 &= 64 \\
21 + 23 + 25 + 27 + 29 &= 125
\end{aligned}
$$

Guess the general law suggested by these examples. Express it in suitable notation and prove it.

*Move: observe; name what you see; prove by induction or direct calculation.*

**Problem 7.** How many subsets does a set of $n$ elements have? Compute the answer for $n = 0, 1, 2, 3, 4$. Conjecture a formula. Prove it two ways: by induction, and by constructing a bijection between subsets and binary strings of length $n$.

*Move: specialization; look for a pattern; find an auxiliary representation.*

### Decomposing and separating the condition

**Problem 8.** Among Grandfather's papers a bill was found:

> 72 turkeys \$\_67.9\_

The first and last digits of the total price have faded and are illegible. What are the two faded digits, and what was the price of one turkey?

*Move: separate the condition into independent divisibility constraints.*

**Problem 9.** Three numbers are in arithmetic progression, three other numbers in geometric progression. Adding the corresponding terms of these two progressions gives

$$85, \quad 76, \quad \text{and} \quad 84$$

and the sum of the three terms of the arithmetic progression is $126$. Find the terms of both progressions.

*Move: introduce good notation; separate the various parts of the condition; write them down as equations.*

**Problem 10.** Bob, Peter, and Paul travel together. Peter and Paul are good hikers, each walking $p$ miles per hour. Bob has a bad foot and drives a small car that holds two people (not three) at $c$ miles per hour. They adopt a leapfrog scheme: Bob and Paul start in the car while Peter walks. After a while Bob drops Paul (who walks on), drives back to pick up Peter, and they ride until they overtake Paul. Then they switch. The cycle repeats.

(a) How much progress does the company make per hour?

(b) What fraction of the travel time does the car carry just one person?

(c) Check the extreme cases $p = 0$ and $p = c$.

*Move: separate the condition into phases; name durations; write equations; check extreme cases.*

### Working backwards and auxiliary problems

**Problem 11.** Determine $m$ so that the equation in $x$

$$x^4 - (3m + 2)x^2 + m^2 = 0$$

has four real roots in arithmetic progression.

*Move: exploit the structure of the unknown; use the symmetry of even powers; work backwards from the form the roots must take.*

**Problem 12.** Find $x, y, u, v$ satisfying

$$
\begin{aligned}
 x + 7y + 3v + 5u &= \phantom{-}16 \\
8x + 4y + 6v + 2u &= -16 \\
2x + 6y + 4v + 8u &= \phantom{-}16 \\
5x + 3y + 7v + \phantom{0}u &= -16
\end{aligned}
$$

This may look long and boring: look for a short cut.

*Move: look for structure before computing; find relations between equations that suggest advantageous combinations.*

### The inventor's paradox and generalization

**Problem 13.** In how many ways can you change one dollar? (A "way of changing" is determined by how many coins of each kind — cents, nickels, dimes, quarters, half dollars — are used.)

*Move: the direct problem is isolated and hard. Generalize: define $E_n$ as the number of ways to pay $n$ cents. Build a family of simpler analogous problems ($A_n$ using only cents, $B_n$ using cents and nickels, ...). The general problem is easier than the special one — the inventor's paradox.*

**Problem 14.** A point and a convex polygon with a center of symmetry are given in the plane. Draw a straight line through the given point that divides the polygon into two parts of equal area.

*Move: the specific shape distracts. Generalize: any figure with a center of symmetry is bisected by any line through that center. The general statement is obvious; the special case looked hard. This is the inventor's paradox again — "the more ambitious plan may have more chances of success."*

### Separating the condition: algebraic decomposition

**Problem 15.** The sides of a right triangle are positive integers that sum to 60, and the altitude to the hypotenuse is 12. Find the sides.

*Move: separate the condition into parts. The perimeter gives $a + b + c = 60$. The right angle gives $a^2 + b^2 = c^2$. The altitude gives $ab = 12c$ (from the area). Use the identity $(a + b)^2 = a^2 + b^2 + 2ab$ to connect the parts — the algebraic identity trick collapses three equations into one.*

### Counting and combinatorial reasoning

**Problem 16.** The side of a regular hexagon is $n$ (a positive integer). By drawing all parallels to its sides at unit spacing, the hexagon is divided into $T$ equilateral triangles of side $1$. Let $V$ be the number of vertices and $L$ the number of unit boundary lines in this subdivision. When $n = 1$: $T = 6$, $V = 7$, $L = 12$. Find $T$, $V$, and $L$ in terms of $n$.

*Move: draw a figure; compute small cases; guess; prove. Check via Euler's relation $T + V = L + 1$.*

**Problem 17.** A group of $n$ people are at a party. Each pair either knows each other or does not. Show that there must exist two people at the party who have the same number of acquaintances (among the group).

*Move: count carefully; use the pigeonhole principle; notice that the extremes (knowing nobody vs knowing everybody) cannot both occur.*

**Problem 18.** You have a $2 \times n$ grid. In how many ways can you tile it with $1 \times 2$ dominoes? Compute for $n = 1, 2, 3, 4, 5$. Conjecture a formula. Prove it.

*Move: specialization; recognize a recurrence; the answer is a familiar sequence in disguise.*

## First hints

**1.** *What is the unknown?* The color of a bear — but how could you find a bear's color from mathematical data? *What is given?* A geometric situation that seems self-contradictory: how could the bear return to $P$?

**2.** *Do you know a related problem?* Think about Problem 1. On a sphere, parallel lines of latitude are not straight — the east-west boundary lines of Bob's land lie on circles whose radius shrinks away from the equator. Where must the center of such a plot lie for all four sides to be truly 100 feet?

**3.** If Bob had very many dollars, he would obviously have no difficulty. *Could you restate the problem?* What is the *minimum* number of dollars needed to fill $10$ pockets with distinct amounts?

**4.** *Here is a problem related to yours.* If a book has exactly $9$ pages, the printer uses $9$ digits. If it has exactly $99$ pages? How many digits through $999$ pages?

**5.** Do you recognize the denominators $2, 6, 24$? *Do you know an analogous problem?* Think of telescoping.

**6.** Observe the right-hand sides. Observe the initial and final terms on each left-hand side. What is the $k$th odd number?

**7.** When you add one new element to a set, each old subset spawns exactly one new subset (by including the new element). *Can you use this?*

**8.** *Could you restate the problem?* What can the two faded digits be if the total price in cents is divisible by $72$? Since $72 = 8 \times 9$, separate the divisibility condition into two parts.

**9.** Let the arithmetic progression be $a - d$, $a$, $a + d$ and the geometric progression be $bg^{-1}$, $b$, $bg$. Write down the four equations. Which unknown can you find first?

**10.** Between start and meeting point, each friend travels the same total distance. Write $\text{distance} = \text{velocity} \times \text{time}$ for each phase. There are three phases: Bob rides with Paul, Bob rides alone (returning), Bob rides with Peter.

**11.** The equation contains only even powers of $x$. Therefore, if $a$ is a root, so is $-a$. What form must four roots in arithmetic progression take if they come in opposite pairs?

**12.** The first equation is related to the last as the second is to the third: same coefficients in reverse order, opposite right-hand sides. Add the first to the last, the second to the third. The resulting system is much simpler.

**13.** *Could you imagine a more accessible analogous problem?* In how many ways can you pay $n$ cents using only cents? ($A_n = 1$.) Using cents and nickels? Build up coin by coin. As Polya put it: "the reader should create a little theory."

**14.** *Could you imagine a more general problem?* Do not think about the specific polygon. What property of any figure with a center of symmetry determines where bisecting lines must pass?

**15.** *Separate the various parts of the condition.* Write three equations, one for each part (perimeter, right angle, altitude). Observe that $(a + b)^2 = a^2 + b^2 + 2ab$. Can you combine the three parts using this identity?

**16.** *Draw a figure.* Compute $T$, $V$, $L$ for $n = 1, 2, 3$. Look at how each quantity grows. The perimeter contributes $6n$ vertices and $6n$ edges at each step.

**17.** Each person's acquaintance count is a number between $0$ and $n - 1$. That gives $n$ possible values for $n$ people — not enough for the pigeonhole principle *yet*. Look at $0$ and $n - 1$ together.

**18.** Call $f(n)$ the number of tilings. A vertical domino at the right end leaves a $2 \times (n-1)$ grid. Two horizontal dominoes at the right end leave a $2 \times (n-2)$ grid. No other placement is possible.

## Solutions or solution sketches

### Solution 1

The situation seems impossible on a flat plane. On a sphere it works: if $P$ is the North Pole, walking south, then east, then north returns you to $P$. The bear is white — a polar bear.

There is a subtlety. The bear could also start near the South Pole, at a latitude where the parallel circle has circumference exactly $1/k$ miles for some positive integer $k$, so that walking one mile east traverses the circle exactly $k$ times. But bears do not live near the South Pole. The answer is white.

*Looking back:* the problem looked like it lacked information (what does geometry have to do with a bear's color?). The real move was questioning the hidden assumption that the walk takes place on a flat plane. Whenever a condition seems self-contradictory, examine the assumptions behind the model.

### Solution 2

Represent the globe as in Solution 1. The land Bob wants is bounded by two meridians and two parallel circles. On a sphere, the arc of a parallel circle intercepted between two fixed meridians gets shorter as you move away from the equator. For all four sides to be 100 feet, the center of the plot must sit on the equator. Bob cannot get it in the U.S.

*Looking back:* the key was connecting this problem to Problem 1's insight — reasoning about the sphere. Polya paired these problems deliberately: "Do you know a related problem?" pointed back to the bear.

### Solution 3

The smallest possible amounts in $10$ pockets, each different, are $0, 1, 2, \ldots, 9$. The minimum total is

$$0 + 1 + 2 + \cdots + 9 = 45.$$

Bob has only $44$ dollars. He cannot do it.

### Solution 4

Pages $1$–$9$ use $9$ digits. Pages $10$–$99$ use $2 \times 90 = 180$ digits. Pages $100$–$999$ use $3 \times 900 = 2700$ digits. Total through page $999$: $9 + 180 + 2700 = 2889$ digits. The remaining $2989 - 2889 = 100$ digits number $100/4 = 25$ four-digit pages. The volume has $999 + 25 = 1024$ pages.

*Looking back:* the key move was solving related, simpler problems first (how many digits for $9$ pages? for $99$? for $999$?) to build up to the answer. This problem teaches that a preliminary estimate of the unknown may be useful — or even necessary, as in the present case. Without estimating that the volume has roughly 1000 pages, you would not know whether to count three-digit or four-digit page numbers.

### Solution 5

The values $1/2 = 1 - 1/2!$, $\;5/6 = 1 - 1/3!$, $\;23/24 = 1 - 1/4!$ suggest

$$\frac{1}{2!} + \frac{2}{3!} + \cdots + \frac{n}{(n+1)!} = 1 - \frac{1}{(n+1)!}.$$

**Proof by induction.** The base case $n = 1$ checks: $1/2 = 1 - 1/2$. For the inductive step, assume the formula holds for $n$. Adding $\frac{n+1}{(n+2)!}$ to both sides:

$$1 - \frac{1}{(n+1)!} + \frac{n+1}{(n+2)!} = 1 - \frac{n+2}{(n+2)!} + \frac{n+1}{(n+2)!} = 1 - \frac{1}{(n+2)!}.$$

This is precisely the formula for $n + 1$. $\square$

*Looking back:* the denominators were factorials. Recognizing them turned the problem from mysterious to routine. The pattern $1 - 1/(n+1)!$ is a telescoping sum in disguise: $\frac{k}{(k+1)!} = \frac{1}{k!} - \frac{1}{(k+1)!}$.

### Solution 6

The right-hand sides are $1^3, 2^3, 3^3, 4^3, 5^3$. The $n$th line sums $n$ consecutive odd numbers. The last odd number on line $n$ is the $m$th odd number where $m = 1 + 2 + \cdots + n = n(n+1)/2$, so it equals $n^2 + n - 1$. The first term on line $n$ is $n^2 - n + 1$.

The claim is:

$$(n^2 - n + 1) + (n^2 - n + 3) + \cdots + (n^2 + n - 1) = n^3.$$

The left side is the sum of $n$ terms of an arithmetic progression with first term $n^2 - n + 1$, last term $n^2 + n - 1$, so the sum is $\frac{(n^2 - n + 1) + (n^2 + n - 1)}{2} \cdot n = n^2 \cdot n = n^3$. $\square$

### Solution 7

For $n = 0, 1, 2, 3, 4$ the counts are $1, 2, 4, 8, 16$. Conjecture: $2^n$.

**Proof by induction.** Base case: the empty set has $1 = 2^0$ subsets (itself). Adding element $a_{n+1}$ to a set of $n$ elements: every old subset survives, and every old subset spawns a new one containing $a_{n+1}$. So the count doubles: $2^n \to 2^{n+1}$. $\square$

**Proof by bijection.** Map each subset $S \subseteq \{a_1, \ldots, a_n\}$ to a binary string $b_1 b_2 \cdots b_n$ where $b_i = 1$ if $a_i \in S$ and $b_i = 0$ otherwise. This is a bijection between subsets and binary strings of length $n$. There are $2^n$ such strings. $\square$

*Looking back:* the binary-string representation is an auxiliary element that makes the count obvious. It reappears whenever you count by finding a bijection to something you already understand.

### Solution 8

The total price in cents is a five-digit number of the form $\_6792$ or similar. Since $72 = 8 \times 9$, we separate:

**Divisibility by 8.** Since $1000$ is divisible by $8$, we need $79\_$ divisible by $8$. Testing: $792 = 99 \times 8$. The last digit is $2$.

**Divisibility by 9.** The digit sum of $\_6792$ must be divisible by $9$. We have $6 + 7 + 9 + 2 = 24$, so the first digit must make the total a multiple of $9$: the first digit is $3$ (giving digit sum $27$).

The total price is $\$367.92$. The price of one turkey: $367.92 / 72 = \$5.11$.

*Looking back:* the key move was decomposing the divisibility condition. Testing $72$ directly would be painful; splitting it into coprime factors $8$ and $9$ turned each part into a quick check. Whenever a divisibility condition involves a composite number, ask: can I factor it into simpler pieces?

### Solution 9

Let the arithmetic progression be $a - d, a, a + d$ and the geometric progression be $bg^{-1}, b, bg$. The conditions give:

$$
\begin{aligned}
(a - d) + bg^{-1} &= 85 \\
a + b &= 76 \\
(a + d) + bg &= 84 \\
3a &= 126.
\end{aligned}
$$

From the fourth equation: $a = 42$. From the second: $b = 34$. Adding the first and third equations eliminates $d$:

$$2a + b(g^{-1} + g) = 169.$$

Substituting known values gives a quadratic in $g$: $g = 2, d = -26$ or $g = 1/2, d = 25$.

**Solution A** ($g = 2$, $d = -26$): the AP is $68, 42, 16$ and the GP is $17, 34, 68$.

**Solution B** ($g = 1/2$, $d = 25$): the AP is $17, 42, 67$ and the GP is $68, 34, 17$.

### Solution 10

Between start and meeting point, each friend travels the same total distance. Let $t_1, t_2, t_3$ be the durations of the three phases (Bob with Paul, Bob alone returning, Bob with Peter). Write distance equations:

Bob's total: $ct_1 - ct_2 + ct_3$. Paul's total: $ct_1 + pt_2 + pt_3$. Peter's total: $pt_1 + pt_2 + ct_3$.

Setting Paul = Peter: $ct_1 + pt_2 + pt_3 = pt_1 + pt_2 + ct_3$, giving $(c - p)t_1 = (c - p)t_3$, so $t_1 = t_3$ (since $c > p$). Peter walks exactly as long as Paul rides.

Setting Bob = Paul and using $t_1 = t_3$: we get $t_1/t_2 = (c + p)/(c - p)$.

**(a)** Progress per hour:

$$\frac{c(t_1 - t_2 + t_3)}{t_1 + t_2 + t_3} = \frac{c(c + 3p)}{3c + p}.$$

**(b)** Fraction of time the car carries one person: $t_2/(t_1 + t_2 + t_3) = (c - p)/(3c + p)$.

**(c)** If $p = 0$: progress is $c/3$ (the car shuttles back and forth, effectively dividing its speed by $3$), and the car is solo $1/3$ of the time. If $p = c$: progress is $c$ and the car is never solo. Both make immediate sense.

*Looking back:* the key move was separating into phases and writing each person's distance. The extreme-case check caught would-be errors cheaply. Always check: does the formula behave right when a variable hits its boundary?

### Solution 11

Since the equation has only even powers, roots come in pairs $\pm a$. Four roots in arithmetic progression with this symmetry must be $-3a, -a, a, 3a$. So the polynomial factors as $(x^2 - a^2)(x^2 - 9a^2)$. Expanding and comparing coefficients:

$$10a^2 = 3m + 2, \qquad 9a^4 = m^2.$$

Eliminating $a$: $19m^2 - 108m - 36 = 0$. Hence $m = 6$ or $m = -6/19$.

*Looking back:* the decisive step was working backwards — asking what form the roots must take before trying to solve the equation. The symmetry of even powers forced roots into opposite pairs, which determined the arithmetic progression up to a single parameter. Working backwards from the answer's structure often cuts through what looks like a wall of algebra.

### Solution 12

The first and fourth equations have the same coefficients in reverse order but opposite right-hand sides. Same for the second and third. Add the first to the fourth, the second to the third:

$$6(x + u) + 10(y + v) = 0, \qquad 10(x + u) + 10(y + v) = 0.$$

This immediately gives $x + u = 0$ and $y + v = 0$. Substituting back into the first two original equations:

$$-4x + 4y = 16, \qquad 6x - 2y = -16.$$

Solving: $x = -2, y = 2, u = 2, v = -2$.

*Looking back:* brute-force elimination would have worked but taken much longer. The shortcut came from looking at the structure — the symmetry between equations — before computing. This is the difference between pedantry and mastery: the pedant reaches for Gaussian elimination; the solver looks first.

### Solution 13

Define:

- $A_n$: ways to pay $n$ cents using only cents.
- $B_n$: ways using cents and nickels.
- $C_n$: ways using cents, nickels, and dimes.
- $D_n$: ways using cents, nickels, dimes, and quarters.
- $E_n$: ways using all five coins.

The key insight is a recurrence. Every way to pay $n$ cents either uses no half-dollar (counted by $D_n$) or uses at least one (after removing it, you pay $n - 50$ cents, counted by $E_{n-50}$):

$$E_n = D_n + E_{n-50}.$$

Similarly: $D_n = C_n + D_{n-25}$, $\;C_n = B_n + C_{n-10}$, $\;B_n = A_n + B_{n-5}$.

Since $A_n = 1$ for all $n \geq 0$, you can build up the table:

| $n$ | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $A_n$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| $B_n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| $C_n$ | 1 | 2 | 4 | 6 | 9 | 12 | 16 | 20 | 25 | 30 | 36 |
| $D_n$ | 1 | 2 | 4 | 6 | 9 | 13 | 18 | 24 | 31 | 39 | 49 |
| $E_n$ | 1 | 2 | 4 | 6 | 9 | 13 | 18 | 24 | 31 | 39 | 50 |

Continuing to $n = 100$: $E_{100} = 292$. You can change a dollar in $292$ different ways.

*Looking back:* the original question — "how many ways to change a dollar?" — was isolated and hard. The move was the inventor's paradox: solve the *more general* problem (arbitrary $n$, arbitrary coin sets) and it becomes easier, because you can build recursively from simpler cases. The general problem has structure that the special case hides.

### Solution 14

The required line passes through the center of symmetry. Any line through the center of a figure with a center of symmetry divides it into two congruent (hence equal-area) halves. The problem asked about one specific polygon, but the answer works for *any* figure with a center of symmetry.

*Looking back:* the specific shape (a convex polygon) was a distraction. Generalizing from "this polygon" to "any centrally symmetric figure" made the answer obvious. This is the inventor's paradox in its purest form: the more general statement is easier to see than the special case. When a problem about a specific object seems hard, ask whether a more general statement might be trivially true.

### Solution 15

Let $a$, $b$, and $c$ denote the sides, the last being the hypotenuse. The three parts of the condition give:

$$
\begin{aligned}
a + b + c &= 60, \\
a^2 + b^2 &= c^2, \\
ab &= 12c.
\end{aligned}
$$

The third equation comes from the area: the area is $\frac{1}{2}ab$ (from the legs) and also $\frac{1}{2} \cdot c \cdot 12$ (from the hypotenuse and altitude), so $ab = 12c$.

Now observe that $(a + b)^2 = a^2 + b^2 + 2ab$. Substituting: $(60 - c)^2 = c^2 + 24c$. This simplifies to $3600 - 120c = 24c$, giving $c = 25$. Then $a + b = 35$ and $ab = 300$, so $a$ and $b$ are the roots of $t^2 - 35t + 300 = 0$: the sides are $15, 20, 25$.

*Looking back:* three separate conditions became one equation in one unknown through the algebraic identity $(a+b)^2 = a^2 + b^2 + 2ab$. The identity connected all three parts. When you have several equations involving sums and products of the same variables, look for identities that link them — especially symmetric ones.

### Solution 16

The perimeter has $6n$ unit segments and $6n$ vertices. When $n$ grows by $1$, $V$ increases by $6n$, so:

$$V = 1 + 6(1 + 2 + \cdots + n) = 3n^2 + 3n + 1.$$

Divide the hexagon into $6$ large equilateral triangles by its three main diagonals. Each large triangle of side $n$ contains $1 + 3 + 5 + \cdots + (2n - 1) = n^2$ unit triangles. So:

$$T = 6n^2.$$

Each triangle has $3$ sides. The $T$ triangles have $3T$ side-slots total. Interior edges are shared by two triangles (counted twice); perimeter edges are counted once. So $3T = 2(L - 6n) + 6n = 2L - 6n$, giving:

$$L = \frac{3T + 6n}{2} = 9n^2 + 3n.$$

**Check via Euler's formula:** $T + V - L = 6n^2 + 3n^2 + 3n + 1 - 9n^2 - 3n = 1$. Confirmed: $T + V = L + 1$. $\square$

### Solution 17

Each person has between $0$ and $n - 1$ acquaintances. That is $n$ possible values for $n$ people — not enough for the pigeonhole principle *yet*. But notice: if someone knows everybody ($n - 1$ acquaintances), then nobody knows nobody (the value $0$ is impossible). If someone knows nobody, then the value $n - 1$ is impossible. Either way, only $n - 1$ distinct values are actually available for $n$ people. By the pigeonhole principle, two people share the same count. $\square$

*Looking back:* the key was not just counting slots and items (the mechanical pigeonhole step) but noticing that the extreme values $0$ and $n - 1$ cannot coexist. That observation reduced the number of slots by one. The pigeonhole principle rarely works on its first application; you almost always need a preliminary insight to shrink the number of slots.

### Solution 18

Let $f(n)$ be the number of tilings of a $2 \times n$ grid. Clearly $f(1) = 1$ (one vertical domino) and $f(2) = 2$ (two verticals, or two horizontals). For $n \geq 3$: the rightmost column is either covered by a vertical domino (leaving $f(n-1)$ tilings) or by two horizontal dominoes spanning the last two columns (leaving $f(n-2)$ tilings). So:

$$f(n) = f(n-1) + f(n-2).$$

This is the Fibonacci recurrence. With $f(1) = 1, f(2) = 2$: $f(3) = 3, f(4) = 5, f(5) = 8$. The number of tilings of a $2 \times n$ grid is $F_{n+1}$, the $(n+1)$st Fibonacci number.

*Looking back:* the recurrence appeared because we asked "what happens at the boundary?" — a form of working backwards from the last piece placed. Recognizing the Fibonacci sequence was a bonus; the real work was seeing that only two cases arise at the right edge.

## Where each problem points back

If you failed a problem, revisit its chapter. If you solved it but your method differs from the one here, the difference itself is worth studying — it may reveal a move you used unconsciously, or one you missed.

| Problem | Primary move | Chapter |
|---|---|---|
| 1 | Examine the condition; question hidden assumptions | 1 — Make the Problem Yours |
| 2 | Do you know a related problem? Reasoning about the sphere | 1, 4 — Make the Problem Yours, Look for a Related Problem |
| 3 | Restate the problem; find the extremal constraint | 2 — Restate and Represent |
| 4 | Solve related simpler problems; preliminary estimate | 4 — Look for a Related Problem |
| 5 | Specialize; guess from small cases; induction | 5 — Try Small Cases, 13 — Proof and Review |
| 6 | Observe; name the pattern; prove directly | 5 — Try Small Cases, 13 — Proof and Review |
| 7 | Auxiliary representation (bijection); two proof methods | 8 — Auxiliary Problems, 13 — Proof and Review |
| 8 | Separate the condition; divisibility decomposition | 3 — Is the Condition Possible?, 7 — Vary the Problem |
| 9 | Introduce notation; decompose conditions into equations | 2 — Restate and Represent |
| 10 | Decompose into phases; check extreme cases | 7 — Vary the Problem, 11 — Signs of Progress |
| 11 | Exploit symmetry; work backwards from the answer's form | 8 — Auxiliary Problems |
| 12 | Look for structure before computing; combine equations | 4 — Look for a Related Problem, 16 — Style, Judgment, and Practice |
| 13 | The inventor's paradox; generalize to make it easier | 6 — Generalize |
| 14 | The inventor's paradox; generalize the figure | 6 — Generalize |
| 15 | Separate the condition; algebraic identity trick | 7 — Vary the Problem, 4 — Look for a Related Problem |
| 16 | Draw a figure; compute cases; verify with Euler's formula | 5 — Try Small Cases, 13 — Proof and Review |
| 17 | Pigeonhole; notice which extremes coexist | 12 — Plausible Reasoning, 13 — Proof and Review |
| 18 | Recurrence from boundary analysis; recognize a known sequence | 5 — Try Small Cases, 8 — Auxiliary Problems |

## Questions to keep

- *Which named move did I actually use?* If you cannot name the heuristic, you have not yet filed the experience.
- *Did I check extreme or boundary cases?* It costs almost nothing and catches errors early.
- *Could I have generalized?* Problems 13 and 14 were easier in their general form. When a specific instance resists attack, ask whether a broader statement might be more tractable.
- *What would I do differently next time?* The point of practice is not to collect solved problems but to sharpen the self-dialogue.
