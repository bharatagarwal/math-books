## Graph coloring

![Figure 40: Two-coloring the regions formed by a set of circles](13 - Graph coloring_images/img-0.jpeg)

## Coloring regions: an easy case

We draw some circles on the plane (say,  $n$  in number). These divide the plane into a number of regions. Figure 40 shows such a set of circles, and also an "alternating" coloring of the regions with two colors; it gives a nice pattern. Now our question is: can we always color these regions this way? We'll show that the answer is yes; to state this more exactly:

**Theorem 13.1.** The regions formed by  $n$  circles in the plane can be colored with red and blue so that any two regions that share a common boundary arc should be colored differently.

(If two regions have only one or two boundary points in common, then they may get the same color.)

Let us first see why a direct approach does not work. We could start with coloring the outer region, say blue; then we have to color its neighbors red. Could it happen that two neighbors are at the same time neighbors of each other? Perhaps drawing some pictures and then arguing carefully about them, you can design a proof that this cannot happen. But then we have to color the neighbors of the neighbors blue again, and we would have to prove that no two of these are neighbors of each other. This could get quite complicated! And then we would have to repeat this for the neighbors of the neighbors of the neighbors...

We should find a better way to prove this and, fortunately, there is a better way! We prove the assertion by induction on  $n$ , the number of circles. If  $n = 1$ , then we only get two regions, and we can color one of them red, the other one blue. So let  $n > 1$ . Select any of the circles, say  $C$ , and forget about it for the time being. The regions formed by the remaining  $n - 1$  circles can be colored with red and blue so that regions that share a common boundary arc get different colors (this is just the induction hypothesis).

Now we take back the remaining circle, and change the coloring as follows: outside  $C$ , we leave the coloring as it was; inside  $C$ , we interchange red and blue (Figure 41).

It is easy to see that the coloring we obtained satisfies what we wanted. In fact, look at any small piece of arc of any of the circles. If this arc is outside  $C$ , then the two regions on its two sides were different and their colors did not change. If the arc is inside  $C$ , then again, the two regions on its both sides were differently colored, and even though their colors were switched, they are still different. Finally, the arc could be on  $C$  itself. Then

<!-- carousel -->
![Figure 41 (left): Adding a new circle and recoloring — the new circle $C$ is drawn dashed before being added](13 - Graph coloring_images/img-1.jpeg)

![Figure 41 (right): After adding the circle $C$ and interchanging red and blue inside it](13 - Graph coloring_images/img-2.jpeg)
<!-- endcarousel -->

![Figure 42: The proof of Euler's Theorem](13 - Graph coloring_images/img-3.jpeg)

the two regions on both sides of the arc were one and the same before putting  $C$  back, and so they had the same color. Now, one of them is inside  $C$  and this switched its color; the other is outside, and this did not. So after the recoloring, their colors will be different.

Thus we proved that the regions formed by  $n$  circles can be colored with two colors, provided the regions formed by  $n - 1$  circles can be colored with 2 colors. By the Principle of Induction, this proves the theorem.

In graph language, Theorem 13.1 is the statement that a region map is *bipartite* and therefore $2$-colorable. We can make that idea executable. A proper coloring gives adjacent vertices different colors; the chromatic number $\chi(G)$ is the fewest colors any proper coloring needs. The circle region maps above are bipartite (they contain no odd cycle), so an even cycle like $C_6$ stands in for them and colors with $2$; an odd cycle $C_5$ is not bipartite and forces $3$. Let us watch that $2$-vs-$3$ split appear with `networkx`, running `greedy_color` under four strategies and checking `is_bipartite`:

```python
<!-- include: code/dm/13 - Graph coloring/01_python.py -->
```

Running it prints that $C_6$ is bipartite and the deterministic strategies use $2$ colors (the randomized `random_sequential` ordering can overshoot to $3$, since greedy coloring only upper-bounds $\chi$), while $C_5$ is not bipartite and every strategy uses $3$, confirming that $2$-colorability is exactly the bipartite (no-odd-cycle) condition behind Theorem 13.1.

Greedy coloring only upper-bounds $\chi(G)$, though. To pin the chromatic number down *exactly* we can ask `z3` whether a proper $k$-coloring exists for growing $k$: the smallest satisfiable $k$ is $\chi(G)$, and showing the $(k-1)$-coloring is UNSAT is a machine-checked proof of the lower bound. We compute $\chi(C_6)=2$ (the bipartite region map), $\chi(C_5)=3$ (odd cycle), and $\chi(K_4)=4$ (every "country" borders every other, foreshadowing the four-color discussion below):

```python
<!-- include: code/dm/13 - Graph coloring/02_python.py -->
```

Running it prints `chi = 2 (2 SAT, 1 UNSAT)`, `chi = 3 (3 SAT, 2 UNSAT)`, and `chi = 4 (4 SAT, 3 UNSAT)`, so each chromatic number is certified both ways: a coloring exists at $k$ and none exists at $k-1$.

> **13.1** Assume that the color of the outer region is blue. Then we can describe what the color of a particular region  $R$  is, without having to color the whole picture, as follows:

- if  $R$  lies inside an even number of circles, it will be colored blue;
- if  $R$  lies inside an odd number of circles, it will be colored red.

Prove this assertion.

We can stress-test this even/odd rule directly. Using `hypothesis` to throw $120$ random circle arrangements ($1$ to $4$ circles) at it: for each arrangement we recover the real arc-adjacency graph by sampling, then assert the parity coloring is proper on every adjacency, that the outer region (inside nothing) is blue, and that the map is bipartite. A concrete two-overlapping-circles case checks the four regions color blue/red/red/blue:

```python
<!-- include: code/dm/13 - Graph coloring/04_python.py -->
```

Running it prints `2 passed`, confirming the even/odd parity rule of Exercise 13.1 is a proper $2$-coloring on every generated arrangement — the executable witness of Theorem 13.1.

> **13.2** (a) Prove that the regions, into which  $n$  straight lines divide the plane, are colorable with 2 colors.
>
> (b) How could you describe what the color of a given region is?

For part (b), there is a clean local rule: each line $ax+by=c$ splits the plane into a $+$ side and a $-$ side, and a region's color is the *parity of how many lines it is on the $+$ side of*. Crossing exactly one line flips one sign, hence flips the parity, so neighbors always differ. Let us confirm this is a genuine proper $2$-coloring with `numpy` and `networkx`: we build three random arrangements ($3$, $4$, $5$ lines, giving $1+n+\binom{n}{2}=7,11,16$ regions), recover the true adjacency graph by sampling, and check the parity coloring is proper and the map bipartite:

```python
<!-- include: code/dm/13 - Graph coloring/03_python.py -->
```

Running it prints `parity coloring proper on all edges: True` and `region adjacency graph bipartite: True` for all three arrangements, confirming Exercise 13.2's local rule is a genuine proper $2$-coloring.

![Figure 43: 4-coloring the countries](13 - Graph coloring_images/img-4.jpeg)

<!-- carousel -->
![Figure 44 (left): Proof of the 5-color theorem — the graph around the vertices $u$, $v$, $w$ before contraction](13 - Graph coloring_images/img-5.jpeg)

![Figure 44 (right): The same graph after contracting the two non-adjacent neighbors $u$ and $w$ of $v$ into a single vertex $uw$](13 - Graph coloring_images/img-6.jpeg)
<!-- endcarousel -->

![Figure 45: 4-coloring the countries and 3-coloring the edges](13 - Graph coloring_images/img-7.jpeg)

![Figure 46: A graph and its dual](13 - Graph coloring_images/img-8.jpeg)
