# Graphs

> One will not get anywhere in graph theory by sitting in an armchair and trying to understand graphs better. Neither is it particularly necessary to read much of the literature before tackling a problem: it is of course helpful to be aware of some of the most important techniques, but the interesting problems tend to be open precisely because the established techniques cannot easily be applied.
>
> -Tim Gowers

So far we've learned about a few major mathematical tools:

- Using sets for modeling.
- Proof by contradiction, induction, and "trivial" proofs.
- Bijections for counting.

In this chapter we won't learn any new tools. Instead we'll apply the tools above to study graphs. Most programmers have heard about graphs before, perhaps in the context of breadth-first and depth-first search or data structures like heaps. Instead of discussing the standard applications of graphs to computer science, we'll focus on a less familiar topic that still finds use in computer science: graph coloring.

In addition to having interesting applications, graph coloring has important theorems one can prove using only the tools we've learned so far. The main theorem we'll prove in this chapter is that every planar graph is 5-colorable (I will explain these terms soon). So think of this chapter as a sort of checkpoint exam. If you're struggling to understand the definitions, theorems, and proofs here—and you've set your pace appropriately—then you should go back and review the previous chapters.

## The Definition of a Graph

The definition of a graph is best done by picture, as in Figure 6.1. Take some "things" and describe which things are "connected." The result is a graph. As a simple example, the "things" might be airports, and two airports are "connected" if there is a flight between the two. Or the things are people and friends have connections. We draw the things and connections using dots and lines to erase the application from our minds. All we care about is the structure of the connections.

![Figure 6.1: An example of a graph.](04 - Graphs_images/img-0.jpeg)

![Figure 6.2: A graph with labeled vertices and edges.](04 - Graphs_images/img-1.jpeg)

### Vertices, Edges, and the Formal Definition

Let's lay out the definitions, using sets as the modeling language. The "things" are called *vertices* (or often *nodes*) and the "connections" are called *edges* (or *links*). For shorthand in the definition, I'll reuse a definition from Chapter 4 for the set of all ways to choose two things from a set.

$$\binom{V}{2} = \{\{v_{1}, v_{2}\} : v_{1} \in V, v_{2} \in V, v_{1} \neq v_{2}\}.$$

This is like $V \times V$, but the order of the pair does not matter.

**Definition 6.1.** A *graph* $G$ consists of a set $V$ of *vertices*, and a set $E \subset \binom{V}{2}$ of *edges*. The entire package is denoted $G = (V, E)$.

Alternatively, one can think of $E$ as just any set, and require a function $f : E \to \binom{V}{2}$ to describe which edges connect which pairs of vertices. This view is used when one wants to define a graph in a context where the vertices are complicated. We will briefly see one from compiler design later in this chapter. Despite the definition of an edge $e \in E$ as a set of size two like $\{u, v\}$, mathematicians will sloppily write it as an ordered pair $e = (u, v)$.

### Adjacency, Degree, and Neighborhoods

Here's some notation and terminology used for graphs. We always call $n = |V|$ the number of vertices and $m = |E|$ the number of edges, and for us these values will always be finite. When two vertices $u, v \in V$ are connected by an edge $e = (u, v)$ we call the two vertices *adjacent*, and we say that $e$ is *incident* to $u$ and $v$. We call $v$ a *neighbor* of $u$ and we define the *neighborhood* of a vertex $N(u)$ to be the set of all neighbors; i.e.,

$$N(u) = \{v \in V : (u, v) \in E\}.$$

The size of a neighborhood (and the number of incident edges) is called the *degree* of a vertex, and the function taking a vertex $v$ to its degree is called $\deg : V \to \mathbb{Z}$. To practice the new terms, see Figure 6.2, labeling the graph from Figure 6.1. Vertices have label '$v$' and edges have label '$e$'. Vertices $v_{1}, v_{3}$ are adjacent, $e_{2}$ is incident to $v_{1}$, $\deg(v_{2}) = 3$, and all of the neighbors of $v_{2}$ are also neighbors of $v_{3}$.

### Paths, Subgraphs, and Connectivity

Another concept we'll need in this chapter is the concept of a connected graph. First, a *path* in a graph is a sequence of alternating vertices and edges $(v_{1}, e_{1}, v_{2}, e_{2}, \ldots, v_{t})$ so that each $e_{i} = (v_{i}, v_{i+1})$ connects the two vertices next to it in the list. Visually, a path is just a way to traverse through the vertices of $G$ by following edges from vertex to vertex.

In Figure 6.2, there are many different paths from $v_{4}$ to $v_{6}$, four of which do not repeat any vertices. Many authors enforce that paths do not repeat vertices by definition, and give the name "trail" or "walk" to a path which does repeat vertices. For us, the difference won't matter. A *cycle* is a path that starts and ends at the same vertex.

A *subgraph* $(H, F)$ of a graph $(G, E)$ is a choice of a subset of the vertices and edges of $G$ which also forms a valid graph. I.e., $H \subset G$ and $F \subset E$. Crucially, this requires that any edge $e = (u, v)$ in $F$ has both $u$ and $v$ in $H$.

An *induced subgraph* has the additional property that if two vertices are adjacent in $G$, they must also be adjacent in $H$. In that way, the structure of an induced subgraph $H$ is completely determined by the subset of vertices, which is why the term "induce" is appropriate.

A graph is called *connected* if there is a path from each vertex to each other vertex, and otherwise it is called *disconnected*. Equivalently (you will prove this in an exercise), $G = (V, E)$ is connected if it is impossible to split $V$ into two nonempty subsets $X, Y$ with no edges between $X$ and $Y$.

A disconnected graph is a union of connected *components*, where the component of $v$ is the largest connected subgraph containing $v$. A single vertex which forms a connected component is called an *isolated vertex*.

## Graph Coloring

The main object of study in this chapter is called a *coloring* of a graph $G = (V, E)$, which is an assignment of "colors" (really, numbers from $\{1, 2, \ldots, k\}$) to the vertices of $G$ satisfying some property. We realize this officially as a function.

**Definition 6.2.** A $k$-*coloring* of a graph $G = (V, E)$ is a function $\varphi : V \to \{1, 2, \ldots, k\}$. We call an edge $e = (u, v)$ *properly colored* by a $k$-coloring $\varphi$ if $\varphi(u) \neq \varphi(v)$, and otherwise we call that edge *improperly colored*. We call $\varphi$ *proper* if it properly colors every edge. If a graph $G$ has a proper $k$-coloring, we call it $k$-*colorable*.

### The Petersen Graph and Chromatic Number

By now you should know to write down examples for small $n$ and $k$ before moving on. Because this is a crucial definition, here is a more complicated example. The Petersen graph is shown in Figure 6.3. The Petersen graph has a distinguished status in graph theory as a sort of smallest serious unit test. Conjectures that are false tend to fail on the Petersen graph.[^3] The Petersen graph is 3-colorable (find a 3-coloring!) but not 2-colorable.

[^3]: Why? Part of it is that the Petersen graph is highly symmetric. We'll revisit this in the exercises for Chapter 16.

![Figure 6.3: The Petersen graph.](04 - Graphs_images/img-2.jpeg)

**Definition 6.3.** The *chromatic number* of a graph $G$, denoted $\chi(G)$, is the minimum integer $k$ for which $G$ is $k$-colorable.

Recall from Chapter 4 that mathematicians often define functions without knowing how to compute them. The chromatic number is an excellent example. We define the concept to clarify what it is we want to study, and the modeling language of sets allows us to start to reason about it.

We can, however, *compute* $\chi(G)$ for a small graph by brute force—try every assignment of $k$ colors for $k = 1, 2, 3, \ldots$ and stop at the first $k$ that admits a proper coloring. The following demo does exactly that and confirms Kun's claim: the Petersen graph is 3-colorable but not 2-colorable, so $\chi(\text{Petersen}) = 3$.

```python
<!-- include: code/pim/04 - Graphs/03_petersen_chromatic.py -->
```

If you believe that the Petersen graph is not 2-colorable—or you do the exercise that proves this—then we know the Petersen graph has chromatic number 3. Here is a simple fact about the chromatic number.

### Greedy Coloring and the Degree Bound

**Proposition 6.4.** If $G = (V, E)$ is a graph and $d$ is the largest degree of a vertex $v \in V$, then $\chi(G) \leq d + 1$.

*Proof.* We define a greedy algorithm for coloring a graph. Pick an arbitrary ordering $v_{1}, \ldots, v_{n}$ of the vertices of $G$, and then for each $v_{i}$ pick the first color $j$ which is unused by any of the neighbors of $v_{i}$.

In the worst case, a vertex $v$ of degree $d$ will have all of its neighbors using different colors, and so it will use color $d + 1$. Otherwise $v$ could reuse one of the first $d$ colors not used by any neighbor. So the worst-case number of colors is at most the largest degree in the graph plus one, as claimed. $\square$

The proof *is* the algorithm. Here is the greedy coloring written out literally—each vertex takes the smallest color none of its already-colored neighbors use—together with a check that it never exceeds $d + 1$ colors, and a demonstration that the bound can be hopelessly loose.

```python
<!-- include: code/pim/04 - Graphs/02_greedy_bound.py -->
```

![Figure 6.4: A star graph.](04 - Graphs_images/img-3.jpeg)

![Figure 6.5: A coloring of the Petersen graph.](04 - Graphs_images/img-4.jpeg)

A simple graph meets this bound and has $\chi(G) = \max_{v \in V} \deg(v) + 1$. See if you can find it. On the other hand, this bound can be quite loose. Here "loose" means that there are graphs which meet the conditions of the proposition, but the true $\chi(G)$ is much smaller than the proposition enforces.

Consider the "star" graph which has $n$ vertices and only one vertex of degree $n - 1$, pictured in Figure 6.4. Clearly the star graph is 2-colorable, but the max degree is $n - 1$. The guarantee of the proposition is effectively useless.

### The Partition Perspective

One other perspective on graph coloring I want to describe is the partition perspective. Specifically, if $G = (V, E)$ is a graph and $\varphi$ is a proper $k$-coloring, then we can look at $\varphi^{-1}(j)$, the set of all vertices that have color $j$.

Since $\varphi$ is proper, there are no edges among these vertices. Moreover, since $\varphi$ is a function, the set $\{\varphi^{-1}(j) : j = 1, \ldots, k\}$ partitions[^4] $V$ into "color classes," and all the edges of $G$ go between the color classes. Figure 6.5 shows a picture for the Petersen graph.

[^4]: A *partition* of $X$ is a set of non-overlapping (disjoint) subsets $A_{i} \subset X$, the union of all of them being $\cup_{i} A_{i} = X$.

This perspective can be used to design coloring algorithms. Start with an improper or unfinished coloring, and fiddle with it to correct the improprieties. We will do this in the main application of this chapter, coloring planar graphs. But right now we're going to take a quick detour to see why graph coloring is useful.

## Register Allocation and Hardness

The wishy-washy way to motivate graph coloring is to claim that many problems can be expressed as an "anti-coordination problem," where you win when no agent in the system behaves the same as any of their neighbors. A totally made up example is radio frequencies.

Radio towers pick frequencies to broadcast, but if nearby towers are broadcasting on the same frequency, they will interfere. So the vertices of the graph are towers, nearby towers are connected by an edge, and the colors are frequencies.

A more interesting and satisfying application is *register allocation*. That is, suppose you're writing a compiler for a programming language. Logically the programmer has no bound on the number of variables used in a program, but on the physical machine there is a constant number of CPU registers in which to store those variables.

The register allocation algorithm must decide (at compile time) which registers will store which logical variables as the computation progresses, and which logical variables must be stored in memory. The less often you need to shuffle data back and forth between memory and CPU registers, the faster the program will run.

The connection to graph coloring is beginning to reveal itself: the vertices are the logical variables and the colors are physical registers, but I haven't yet said how to connect two vertices by an edge. Intuitively, it depends on whether the logical variables "overlap" in the scope of their use. The structure of scope overlap is destined to be studied with graph theory.

### Liveness Analysis and Interference Graphs

To simplify things, we'll do what a compiler designer might reasonably do, and compile a program down to *almost* assembly code, where the only difference is that we allow infinitely many "virtual" registers, which we'll just call variables. So for a particular program $P$, there is an $n_{P} \in \mathbb{N}$ that is the number of distinct variable names used in the program. Each of these integers is a vertex in $G$.

As an illustrative example, say that the almost-compiled program looks like this, where the dollar sign denotes a variable name:

```
whileBlock:
$41 = $41 - 1
$40 = $40 + $42
$42 = $41 - $42
BranchIfZero $41 endBlock whileBlock

endBlock:
$43 = $41 + $40
```

In this example variables 41 and 42 cannot share a physical register. They have different values and are used in the same line to compute a difference. Call a variable *live* at a statement in the code if its value is used after the end of that statement.

Thinking of it in reverse: a variable is *dead* in all of the lines of code between when it was last read and when it is next written to. Whenever a variable is dead we know it's safe to reuse its physical register (storing the value of the dead variable in memory).

Now we can define the edges. Two variables `$i` and `$j` "interfere," and hence we add the edge $(i, j)$ to $G$, if they are ever live at the same time in the program. With a bit of work (uncoincidentally using graphs to do a flow analysis), one can efficiently compute the places in the code where each variable is live and construct this graph $G$.

Then if we can compute the chromatic number of $G$ and find an actual $\chi(G)$-coloring, we can assign physical registers to the variables according to the coloring. Without some deeper semantic analysis, this provides the most efficient possible use of our physical registers.

We can turn this directly into code. The demo below does the backward liveness pass on Kun's exact snippet (a variable is live where its value is still needed), builds the interference graph, and colors it—giving a concrete register assignment. Note that the edge `$41 -- $42` shows up, just as Kun says it must.

```python
<!-- include: code/pim/04 - Graphs/04_register_allocation.py -->
```

### NP-Hardness and Inapproximability

Unfortunately, in general you should not hope to compute the chromatic number of an arbitrary graph. This problem is what's called "NP-hard," which roughly means there is no known provably correct (in the worst case) and provably efficient algorithm for computing it.

Moreover, if there were, the same algorithm could be adapted to solve a whole class of problems that are also believed to be intrinsically hard to solve. The notion of efficiency here is—as usual for algorithm analysis—in terms of the runtime compared to the size of the input as the input grows. This is called "asymptotic analysis" or "big-O." See Chapter 15 for a longer discussion.

Moreover, it is even NP-hard to get any reasonable approximation of the chromatic number of a general graph. To be more specific, we can't hope to find an efficient and provably correct algorithm for the following problem. Fix any $c$ such that $0 < c < 1$. Given any graph $G$ as input, if $G$ has $n$ vertices, output a number $Z$ with the property that $\frac{Z}{\chi(G)} < n^{c}$.

As mentioned, this is an asymptotic statement, meaning an algorithm that only works for all graphs with fewer than a thousand nodes is not a solution. A lookup table, though it would be massive, would solve this problem efficiently. No, a true solution must work and must work efficiently for any arbitrarily large graph in principle, though working on small graphs may be sufficient in practice.

But to put the numbers in perspective with an example, this theorem says that for graphs with $n = 10^{4}$ vertices and with $c = 1/2$, algorithms will struggle to output a number guaranteed to be between $\chi(G)$ and $100 \cdot \chi(G)$.

But I digress. The takeaway is that coloring is a hard problem. This is a sad result for people who really want to color their graphs, but there are other ways to attack the problem. You can assume that your graph has some nice structure.

This is what we'll do in the next section, and there it turns out that the chromatic number will always be at most 4. Alternatively, you could assume that you know your graph's chromatic number, and try to color it without introducing too many improperly colored edges. We'll see this approach in the "Approximate Coloring" section.

## Planarity and the Euler Characteristic

The condition we'll impose on a graph to make coloring easier is called *planarity*. A graph $G = (V, E)$ is called *planar* if one can draw it on a plane in such a way that no edges cross. Figure 6.6 contains an example.

Here's a little exercise: come up with an example of a graph which is not planar. Don't be surprised if you're struggling to prove that a given graph is not planar. You personally failing to draw a specific graph without edges crossing is not a proof that it is impossible to do so. There is a nice rule that characterizes planar graphs, but it is not trivial. See the chapter exercises for more.

![Figure 6.6: An example of a planar graph which can be drawn with no edges crossing.](04 - Graphs_images/img-5.jpeg)

Now that you've tried the exercise: Figure 6.7 depicts two important graphs that are not planar. The left one is called the *complete graph* on 5 vertices, denoted $K_{5}$. The word "complete" here just means that all possible edges between vertices are present.

The second graph is called the *complete bipartite graph* $K_{3,3}$. "Bipartite" means "two parts," and the completeness refers to all possible edges going between the two parts. The subscript of $K_{a,b}$ for $a, b \in \mathbb{N}$ means there are $a$ vertices in one part and $b$ in the other.

### Embeddings and the Rigorous View

We defined planar graphs informally in terms of drawings in the plane, which doesn't use sets, functions, or anything you've come to expect. Indeed, the hand-wavy definition is the one that belongs in your head, but the official definition of a planar graph is one which has an *embedding* into $\mathbb{R}^{2}$. The problem is that defining an embedding requires opening a big can of worms, because it applies to spaces more general than a graph. We'll give you a taste in the chapter notes.

### Faces and the Euler Formula

One feature about planar graphs is that when you draw a planar graph in such a way that no edges cross, you get a division of $\mathbb{R}^{2}$ into distinct regions called "faces." Figure 6.8 shows a graph with four faces, noting that by convention I'm calling the "outside" of the drawing also a face. If we call $f$ the number of faces, and remember $n$ is the number of vertices and $m$ is the number of edges, then we can notice a nice little pattern: $n - m + f = 2$.

<!-- carousel -->
![Figure 6.7a: The complete graph $K_{5}$, which is not planar.](04 - Graphs_images/img-6.jpeg)
![Figure 6.7b: The complete bipartite graph $K_{3,3}$, which is not planar.](04 - Graphs_images/img-7.jpeg)
<!-- endcarousel -->

![Figure 6.8: Faces of a planar graph: $F_{1}, F_{2}, F_{3}$ are bounded regions and $F_{4}$ is the outer face.](04 - Graphs_images/img-8.jpeg)

The amazing fact is that this equation does not depend on how you draw the graph! So long as your drawing has no crossing edges, the value $n - m + f$ will always be 2. We can prove it quite simply with induction.

**Theorem 6.5.** For any connected planar graph $G = (V, E)$ with at least one vertex, and any drawing of $G$ in the plane $\mathbb{R}^{2}$ defining a set $F$ of faces, the quantity $|V| - |E| + |F| = 2$.

*Proof.* We proceed by induction on the total number of vertices and edges. The base case is a single isolated vertex, for which $|V| = 1$, $|E| = 0$, and $|F| = 1$, so the theorem works out.

Now suppose we have a graph $G$ for which the theorem holds, i.e. $|V| - |E| + |F| = 2$, and we will make it larger and show that the theorem still holds. In particular, we will do induction on the quantity $|V| + |E|$. There are two cases: either we add a new edge connecting two existing vertices, or we add a new edge connected to a new vertex (which now has degree 1). Adding a vertex by itself is not allowed because the graph must stay connected at all times.

In the first case, $|V|$ is unchanged, $|E|$ increases by 1, and $|F|$ also increases by one because the new edge cuts an existing face into two pieces. So

$$|V| - (|E| + 1) + (|F| + 1) = |V| - |E| + |F| = 2.$$

Notice how it does not matter how we drew the edge, so long as it doesn't cross any other edges to create more than one additional face. The second case is similar, except adding an edge connected to a new vertex does not create any new faces. Convince yourself that any vertex involved in a path that encloses a face has to have degree at least two. So again we get that for the new graph $|V| + 1 - (|E| + 1) + |F| = 2$. This finishes the inductive step.

Finally, it should be clear that every connected graph (regardless of whether or not it's planar) can be built up by a sequence of adding edges by these two cases. This completes the proof. $\square$

The cleanest way to *believe* this is to count faces on a real embedding. networkx will both test planarity and hand back a combinatorial embedding; from the embedding we can trace each face and tally $V$, $E$, $F$. Across very different planar graphs the alternating sum lands on 2 every time.

```python
<!-- include: code/pim/04 - Graphs/05_euler_formula.py -->
```

This is a surprising fact. We have some measurement derived from a drawing of a graph that doesn't depend on the choices made to draw it! This is called an *invariant*, and we'll discuss invariants more in Chapter 10 when we study linear algebra, and Chapter 16 when we study geometry. For now it will remain a deep mathematical curiosity. Lastly, note that the connectivity requirement is crucial for the theorem to hold, since a graph with $n$ vertices and no edges has $|V| - |E| + |F| = n + 1$.

## Application: the Five Color Theorem

Here is an amazing theorem about planar graphs.

**Theorem 6.6.** (The four color theorem) Every planar graph can be colored with 4 colors.

This was proved by Kenneth Appel and Wolfgang Haken in 1976 after being open for over a hundred years. You may have heard of it because of its notoriety: it was the first major theorem to be proved with substantial aid from a computer. Unfortunately the proof is very long and difficult (on the order of 400 pages of text!). Luckily for us there is a much easier theorem to prove.

**Theorem 6.7.** (The five color theorem) Every planar graph can be colored with 5 colors.

If you're like me and frequently make off-by-one errors, then the five color theorem is just as good as the four color theorem. In order to prove it we need three short lemmas.

### The Handshake Lemma

**Lemma 6.8.** If $G$ is a graph with $m$ edges, then $2m = \sum_{v \in V} \deg(v)$.

*Proof.* The important observation is that the degree of a vertex is just the number of edges incident to it, and every edge is incident to exactly two vertices.

This is where the proof would usually end. As a variation on a theme, you can (and should) think of this as constructing a clever bijection like we did in Chapter 4, but it's difficult to clearly define a domain and codomain.

Let me try: the domain consists of "edge stubs" sticking out from each vertex, and the codomain is the set of edges $E$. We're mapping each edge stub to the edge that contains that stub. This map is a surjection and a double cover of $E$, and the size of the domain is exactly $\sum_{v \in V} \deg(v)$. $\square$

This "handshake lemma" is the easiest one to confirm on real graphs: sum the degrees, and you always get twice the edge count.

```python
<!-- include: code/pim/04 - Graphs/01_handshake.py -->
```

### Bounding Faces by Edges

**Lemma 6.9.** If a planar graph $G$ has $m \geq 2$ edges and $f$ faces, then $2m \geq 3f$, i.e., $f \leq (2/3)m$.

*Proof.* Pick your favorite embedding (drawing) of $G$ in the plane. We'll use a similar counting argument as in Lemma 6.8: for any planar drawing, every face is enclosed by at least three edges, and every edge touches at most two faces.[^8] In other words, each face is "counted" by each edge it touches, and each face has at least three edges counting it. Hence $3f$ counts each edge at most twice, while $2m$ counts each face at least three times. $\square$

[^8]: An edge incident to a vertex of degree 1 will touch the "outside" face twice, but this only counts as one face.

The requirement that $m \geq 2$ is necessary, since if there is only one edge (or zero), then the outside face is the only face. It only gets "counted" twice (or zero times) by the edges it touches. Once we get to two edges, the outside face is counted twice ($2m = 4$).

As you add more edges, either you add dangling edges (or subdivide existing edges) which increases $2m$ but not $3f$, or you add edges that create new faces. In the case of a single edge creating a single new face, the lower bound $3f$ increases by exactly $3$, but the upper bound $2m$ only increases by $2$.

Despite having just read a proof, this may be surprising: can't we keep adding face-creating edges to make the lower bound of $3f$ exceed the upper bound of $2m$? It's instructive to take a moment and play with examples. You'll eventually get to a situation in which all interior faces are triangles, and the inequality is either an equality or very close.

Then the creation of new faces requires a sufficient number of non-face-creating edges to be made first, which loosens the inequality. The proof above explains how this loosening and tightening of the inequality corresponds to the geometry of a graph drawn in the plane. It translates the geometry to algebra. When the algebra seems to misbehave, we can call back to the geometry to understand.

You should do what I did for Lemma 6.8 and think about how to express this as an injection from one set to another. The last lemma is the key to the five color theorem.

### Every Planar Graph Has a Low-Degree Vertex

**Lemma 6.10.** Every planar graph has a vertex of degree 5 or less.

*Proof.* Suppose to the contrary that every vertex of $G = (V, E)$ has degree 6 or more. Substituting the inequality from Lemma 6.9 into the Euler characteristic equation gives

$$2 = |V| - |E| + |F| \leq |V| - |E| + (2/3)|E|.$$

Rearranging terms to solve for $|E|$ gives $|E| \leq 3|V| - 6$. Now we want to use Lemma 6.8, so we multiply by two to get $2|E| \leq 6|V| - 12$. Since $2|E|$ is the sum of the degrees, and each vertex has degree at least six, $2|E|$ is at least as large as $6|V|$. Putting these together gives

$$6|V| \leq 2|E| \leq 6|V| - 12,$$

which is a contradiction. $\square$

As a quick side note that we'll need in the next theorem, along the way to proving Lemma 6.10 we get a bonus fact: the complete graph $K_{5}$ is not planar. This is because we proved that all planar graphs satisfy $|E| \leq 3|V| - 6$, and for $K_{5}$, $|E| = 10 > 15 - 6 = 9$.

This argument doesn't work for showing $K_{3,3}$ is not planar, but if you're willing to do a bit extra work (and take advantage of the fact that $K_{3,3}$ has no cycles of length 3), then you can improve the bound from Lemma 6.10 to work. In particular, because $K_{5}$ is not planar, no planar graph can contain $K_{5}$ as a subgraph.

The inequality $|E| \leq 3|V| - 6$ is the engine behind both Lemma 6.10 and the "$K_{5}$ is not planar" bonus fact. The demo below checks that planar graphs obey it (and so always have a vertex of degree $\leq 5$), while $K_{5}$ violates it outright.

```python
<!-- include: code/pim/04 - Graphs/06_planarity_bound.py -->
```

### Proof of the Five Color Theorem

Now we can prove the five color theorem.

*Proof.* By induction on $|V|$. For the base case, every graph which has 5 or fewer vertices is 5-colorable by using a different color for each vertex.

Now let $|V| \geq 6$. By Lemma 6.10, $G$ has a vertex $v$ of degree at most 5. If we remove $v$ from $G$ then the inductive hypothesis guarantees us a 5-coloring. We want to extend or modify this coloring and in doing so properly color $v$. This will finish the proof. When $v$ has degree at most 4, choose one of the unused colors among $v$'s neighbors. Otherwise $v$ has degree exactly 5, and we have to be more clever, because the neighbors may need all 5 colors a priori.

Call $v$'s five neighbors $w_{1}, w_{2}, w_{3}, w_{4}, w_{5}$. Because $K_{5}$ is not planar and $G$ is, these five neighbors can't form $K_{5}$. In particular there must be some $i, j$ for which $w_{i}$ and $w_{j}$ are not adjacent.

We can form a new graph $G'$ ("G prime"[^9]) by deleting $v$ and *merging* $w_{i}$ and $w_{j}$, i.e., delete $v, w_{i}, w_{j}$ and add a new vertex $x$ which is adjacent to all the remaining vertices in $N(w_{i}) \cup N(w_{j})$. I claim that if $G'$ is planar then we're done: $G'$ has $|V| - 1$ vertices and so it has a 5-coloring by the inductive hypothesis, and we can use that 5-coloring to color most of $G$ (everything except $w_{i}, w_{j},$ and $v$).

Then use the color assigned to $x$ for both $w_{i}$ and $w_{j}$; they had no edge between them in $G$, so this coloring is proper. These choices ensure the neighbors of $v$ use only 4 of the 5 colors, so finally pick the unused color for $v$. This produces a proper coloring of $G$.

[^9]: The tick is called the "prime" symbol, and it is used to denote that two things are closely related, usually that the prime'd thing is a minor variation on the un-primed thing. So using $G'$ here is a reminder to the reader that $G'$ was constructed from $G$.

So why is $G'$ planar? To argue this, we can show that for any planar drawing of $G$, removing $v$ leaves $w_{i}$ and $w_{j}$ in the same face. This is equivalent to being able to trace a curve in the plane from $w_{i}$ to $w_{j}$ without hitting any other edges, since we could then "drag" $w_{i}$ along that curve to $w_{j}$ and "lengthen" the edges incident to $w_{i}$ as we go.

When the two vertices merge, and "become" $x$, we get a planar drawing of $G'$. The picture in my head is like the strands of a spider web, shown in Figure 6.9.

![Figure 6.9: The "strands of a spider web" image guide the proof that $G'$ is planar.](04 - Graphs_images/img-9.jpeg)

The key is that $G$ is planar and that $v$ has all of the $w$'s as neighbors. If we want to merge $w_{i}$ to $w_{j}$, we can use the curve already traced by the edges from $w_{i}$ to $v$ and from $v$ to $w_{j}$. By planarity this is guaranteed not to cross any of the other edges of $G$, and hence of $G'$.

To say it a different way, if we took the drawing above and continued drawing $G'$, and the result required an edge to cross one of the edges above, then it would have crossed through one of the edges going from $v$ to $w_{i}$ or $v$ to $w_{j}$!

This proves $G'$ is planar, which completes the proof. $\square$

### Implementing the Algorithm in Code

That proof neatly translates into a recursive algorithm for 5-coloring a planar graph. We'll finish this section with Python code implementing it. Kun's book uses a library called igraph to avoid writing custom graph data structures. As a very quick introduction, one can create graphs in igraph as follows.

```python
import igraph
G = igraph.Graph(n=10)
G.add_edges([(0, 1), (1, 2), (4, 5)])
G.vs  # a list-like sequence of vertices
G.es  # a list-like sequence of edges
```

For example, given a graph and a list of nodes in the graph, one might use the following function to find two nodes which are not adjacent.

```python
from itertools import combinations

def find_two_nonadjacent(graph, nodes):
    for x, y in combinations(nodes, 2):
        if not graph.are_connected(x, y):
            return x, y
```

Also, the vertices of an igraph graph can have arbitrary "attributes" that are assigned like dictionary indexing. We use this to assign colors to the vertices, using `[ ]`. For example, this is the base case of our induction: trivially color each vertex of a $\leq 5$ vertex graph with all different colors.

```python
colors = list(range(5))

def planar_five_color(graph):
    n = len(graph.vs)
    if n <= 5:
        graph.vs['color'] = colors[:n]
        return graph
    ...
```

The igraph library overloads the assignment operator to allow for entry-wise assignments by assigning one list to another. So in the statement `graph.vs['color'] = colors[:n]`, the nodes of $G$ are being assigned the first $n$ colors in the list of colors.

The rest of the `planar_five_color` function involves finding the vertices of the needed degree, forming the graph $G'$ to recursively color, and keeping track of which vertices were modified to make $G'$ so you can use its coloring to color $G$.

Here is the part where we find vertices of the right degree and do bookkeeping:

```python
deg_at_most5_nodes = graph.vs.select(_degree_le=5)
deg_at_most4_nodes = deg_at_most5_nodes.select(_degree_le=4)
deg5_nodes = deg_at_most5_nodes.select(_degree_eq=5)

g_prime = graph.copy()
g_prime.vs['old_index'] = list(range(n))
```

The `select` functions are igraph-specific: they allow one to filter a vertex list by various built-in predicates, such as whether the degree of the vertex is equal to 5. The `old_index` attribute keeps track of which vertex in $G'$ corresponded to which vertex in $G$, since when you modify the vertex set of an igraph the locations of the vertices within the data structure change (which changes the index in the list of all vertices).

Next we construct $G'$. This is where the two cases in the proof show up.

```python
if len(deg_at_most4_nodes) > 0:
    v = deg_at_most4_nodes[0]
    g_prime.delete_vertices(v.index)
else:
    v = deg5_nodes[0]
    neighbor_indices = [
        x['old_index'] for x in g_prime.vs[v.index].neighbors()
    ]
    g_prime.delete_vertices(v.index)
    neighbors_in_g_prime = g_prime.vs.select(
        old_index_in=neighbor_indices)
    w1, w2 = find_two_nonadjacent(g_prime, neighbors_in_g_prime)
    merge_two(g_prime, w1, w2)
```

We implemented a function called `merge_two` that merges two vertices, but the implementation is technical and not interesting. The official igraph function we used is called `contract_vertices`. The remainder of the algorithm executes the recursive call, and then copies the coloring back to $G$, computing the first unused color with which to color the originally deleted vertex $v$.

```python
colored_g_prime = planar_five_color(g_prime)
for w in colored_g_prime.vs:
    # subset selection handles the merged w1, w2 with one assignment
    graph.vs[w['old_index']]['color'] = w['color']
neighbor_colors = set(w['color'] for w in v.neighbors())
v['color'] = [j for j in colors if j not in neighbor_colors][0]
return graph
```

The entire program is in the Github repository for this book.[^10] The second case of the algorithm is not trivial to test. One needs to come up with a graph which is planar, and hence has some vertex of degree 5, but has no vertices of degree 4 or less. Indeed, there is a planar graph in which every vertex has degree 5. Figure 6.10 shows one that I included as a unit test in the repository.

[^10]: See [pimbook.org](https://pimbook.org).

![Figure 6.10: A planar graph which is 5-regular.](04 - Graphs_images/img-10.jpeg)

So that this version of the book stays runnable without an igraph install, here is the same algorithm re-expressed in networkx. The structure mirrors the proof line for line: base case, find a vertex of degree $\leq 5$, easy branch for degree $\leq 4$, and the merge-two-non-adjacent-neighbors branch for degree exactly 5. We test it on the icosahedron of Figure 6.10—a planar graph where *every* vertex has degree 5, so the hard branch is forced to fire.

```python
<!-- include: code/pim/04 - Graphs/07_planar_five_color.py -->
```

## Approximate Coloring

Earlier I remarked that coloring is probably too hard for algorithms to solve in the worst case. To get around the problem we added the planarity constraint. Though a practical coloring algorithm would likely use an industry standard optimization engine to approximately color graphs, let's try something different to see the theory around graph coloring. Suppose we're promised a graph can be colored with 3 colors, and let's try to color it with some larger number of colors.

The first algorithm of this kind colors a 3-colorable graph with $4\sqrt{n}$ colors, where $n = |V|$. To make the numbers concrete, for a 3-colorable graph with 1000 vertices, this algorithm will use no more than 127 colors. Sounds pretty rotten, but the algorithm is quite simple.

As long as there is an uncolored vertex $v$ with degree at least $\sqrt{n}$, pick three new colors. Use one for $v$, and the other two to color $N(v)$. Then remove all these vertices from the graph and repeat. If there are no vertices of degree $\sqrt{n}$, then use the greedy algorithm to color the remaining graph.

**Theorem 6.11.** This algorithm colors any 3-colorable graph using at most $4\lceil\sqrt{n}\rceil$ colors.

*Proof.* Let $G$ be a 3-colorable graph. For the first case, where there is a vertex $v$ of degree $\geq \sqrt{n}$, we have to prove that the neighborhood $N(v)$ can be colored with two colors. But this follows from the assumption that $G$ is 3-colorable: in any 3-coloring of $G$, $v$ uses a color that none of its neighbors may use. Only two colors remain.

If there are no vertices of degree $\geq \sqrt{n}$, then the maximum degree of a vertex is at most $\lceil\sqrt{n}\rceil - 1$, and we proved in Proposition 6.4 that the greedy algorithm will use no more than $\lceil\sqrt{n}\rceil$ colors on this graph.

Now we have to count how many colors get used total. The first case can only happen $\sqrt{n}$ times, because each time we color $v$ and its neighbors, we remove those $\sqrt{n} + 1 \geq \sqrt{n}$ vertices from $G$ ($\sqrt{n} \cdot \sqrt{n} = n$). Since we add 3 new colors in each step, this part uses at most $3\sqrt{n}$ colors. The greedy algorithm uses at most $\lceil\sqrt{n}\rceil$ colors, so in total we get at most $4\lceil\sqrt{n}\rceil$, as desired. $\square$

The whole algorithm, including the two-coloring subroutine for $N(v)$, fits in one file. We build a genuinely 3-colorable graph (a random tripartite graph), run the algorithm, and check both that the coloring is proper and that it respects the $4\lceil\sqrt{n}\rceil$ guarantee.

```python
<!-- include: code/pim/04 - Graphs/08_approx_coloring.py -->
```

### Open Problems and Better Bounds

One might naturally ask whether we can improve $\sqrt{n}$ to something like $\log(n)$, or even some very large constant. This is actually an open question. Recent breakthroughs using a technique called *semidefinite programming* got the number of colors down to roughly $n^{0.2}$. For reference, a thousand-node 3-colorable graph would have $n^{0.2} \approx 4$. That's quite an improvement over 127 colors given by the $4\sqrt{n}$ bound.

I should make a clarification here: the open problem is on the existence of an algorithm which is guaranteed to achieve some number of colors (depending on the size of the graph) *no matter what the graph is*. As a programmer you are probably somewhat familiar with this idea that one often measures an algorithm by its worst-case guarantees, but the point is important enough to emphasize.

So when I say a problem is "possible" or "impossible" to solve, I mean that there exists (or does not exist, respectively) an efficient algorithm that achieves the desired worst-case guarantee on all inputs. In particular, there is no evidence for either claim that it is possible or impossible to color a 3-colorable graph with $\log(n)$ colors (or anything close to that order of magnitude, like $(\log(n))^{10}$). A ripe problem indeed.

## Cultural Review

1. Invariants are measurements intrinsic to a concept, which don't depend on the choices made for some particular representation of that concept.
2. Sometimes if you want to come up with the right rigorous definition for an intuitive concept (like a planar graph), you need to develop a much more general framework for that concept. But in the mean time, you can still do mathematics with the informal notion.
3. Every conjecture about graphs must be tested on the Petersen graph.

## Exercises

**6.1.** Write down examples for the following definitions. A graph is a *tree* if it contains no cycles. Two graphs $G, H$ are *isomorphic* if they differ only by relabeling their vertices. That is, if $G = (V, E)$ and $H = (V', E')$, then $G$ and $H$ are isomorphic if there is a bijection $f : V \to V'$ with the property that $(i, j) \in E$ if and only if $(f(i), f(j)) \in E'$.

Given a subset of vertices $S \subset V$ of a graph $G = (V, E)$, the *induced subgraph on $S$* is the subgraph consisting of all edges with both endpoints in $S$. Given a vertex $v$ of degree 2, one can *contract* it by removing it and "connecting its two edges," i.e., the two edges $(v, w), (v, u)$ become $(w, u)$.

Likewise, one can contract an edge by merging its endpoint vertices, or *subdivide* an edge by adding a vertex of degree two in the middle of an edge. If $H$ can be obtained from $G$ after some sequence of contractions and subdivisions, it is called a *minor* of $G$.

**6.2.** Look up the statement of Wagner's theorem, which characterizes planar graphs in terms of contractions and the two graphs $K_{3,3}$ and $K_{5}$. Find a proof you can understand.

**6.3.** In the "Definition of a Graph" section we claimed that the following two definitions of a connected graph are equivalent: (1) there is a path between every pair of vertices, (2) it is impossible to split $V$ into two nonempty subsets $X, Y$ such that no edge $e = (a, b)$ has $a \in X$ and $b \in Y$. Prove this.

**6.4.** Here's a simple way to make examples of planar graphs: draw some non-overlapping circles of various sizes on a piece of paper, call the circles vertices, and put an edge between any two circles that touch each other. Clearly the result is going to be a planar graph, but an interesting question is whether every planar graph can be made with this method. Amazingly the answer is yes!

This is called Koebe's theorem. It is a relatively difficult theorem to prove for the intended reader of this book, but as a consequence it implies Fáry's theorem. Fáry's theorem states that every planar graph can be drawn so that the edges are all straight lines. Look up a proof of Fáry's theorem that uses Koebe's theorem as a starting point, and rewrite it in your own words.

### Coloring and Polynomials

**6.5.** Given a graph $G$, the *chromatic polynomial* of $G$, denoted $P_{G}(x)$, is the unique polynomial which, when evaluated at an integer $k \geq 0$, computes the number of proper colorings of $G$ with $k$ colors. Compute the chromatic polynomial for a path on $n$ vertices, a cycle on $n$ vertices, and the complete graph on $n$ vertices. Look up the chromatic polynomial for the Petersen graph.

**6.6.** Look up a recursive definition of the chromatic polynomial of a graph in terms of edge contractions, and write a program that computes the chromatic polynomial (for small graphs). Think about a heuristic that can be used to speed up the algorithm by cleverly choosing an edge to contract.

**6.7.** In the chapter I remarked that the Euler characteristic is a special quantity because it is an invariant. Look up a source that explains why the Euler characteristic is special.

**6.8.** Find a simple property that distinguishes 2-colorable graphs from graphs that are not 2-colorable. Write a program which, when given a graph as input, determines if it is 2-colorable and outputs a coloring if it is.

**6.9.** Implement the algorithm presented in the chapter to $(4\sqrt{n})$-color a 3-colorable graph. Use the 2-coloring algorithm from the previous problem as a subroutine.

### Directed Graphs, DAGs, and Flows

**6.10.** A *directed graph* is a graph in which edges are oriented (i.e., they're ordered pairs instead of unordered pairs). The endpoints of an edge $e = (u, v)$ are distinguished as the *source* $u$ and the *target* $v$.

A directed graph gives rise to natural *directed paths*, which are like normal paths, but you can only follow edges from source to target. A graph is called *strongly connected* if every pair of vertices is connected by a directed path. Write a program that determines if a given directed graph is strongly connected.

**6.11.** A *directed acyclic graph* (DAG) is a directed graph which has no directed cycles (paths that start and end at the same vertex). DAGs are commonly used to represent dependencies in software systems. Often, one needs to *resolve* dependencies by evaluating them in order so that no vertex is evaluated before all of its dependencies have been evaluated.

One often solves this problem by sorting the vertices using what's called a "topological" sort, which guarantees every vertex occurs before any downstream dependency. Write a program that produces a topological sort of a given DAG.

**6.12.** A *weighted* graph is a graph $G$ for which each edge is assigned a number $w_{e} \in \mathbb{R}$. Weights on edges often represent *capacities*, such as the capacity of traffic flow in a road network. Look up a description of the maximum flow problem in directed, weighted graphs, and the Ford-Fulkerson algorithm which solves it. Specifically, observe how the maximum flow problem is modeled using a graph. Find real-world problems that are solved via a max flow problem.

**6.13.** A *hypergraph* generalizes the size of an edge to contain more than two vertices. Hypergraphs are also called *set systems* or *families of sets*. Edges of a hypergraph are called *hyperedges*, and a $k$-*uniform* hypergraph is one in which all of its hyperedges have size $k$.

Look up a proof of the Erdős-Ko-Rado theorem: let $G$ be a $k$-uniform hypergraph with $n \geq 2k$ vertices, in which every pair of hyperedges shares a vertex in common. Then $G$ has at most $\binom{n-1}{k-1}$ hyperedges in total. Find a construction that achieves this bound exactly when $n > 2k$.

## Chapter Notes

**Some Topology and the Rigorous Definition of an Embedding**

The reason a planar graph is so hard to define rigorously is because the right definition of what it means to "draw" one thing inside another is deep and deserves to be defined in general. And such a definition requires some amount of *topology*, the subfield of mathematics that deals with the intrinsic shape of space without necessarily having the ability to measure distances or angles.

### A Calculus-Based Definition of Embedding

If you really pressed me to define a planar graph without appealing to topology I could do it with a tiny bit of calculus. Here it goes.

**Definition 6.12.** An *embedding* of a graph $G = (V, E)$ in the plane is a set of continuous functions $f_{e} : [0, 1] \to \mathbb{R}^{2}$ for each edge $e \in E$ mapping the unit interval to the plane with the following properties:

- Every $f_{e}$ is injective.
- There are no two $f_{e_{1}}, f_{e_{2}}$ and values $0 < t_{1}, t_{2} < 1$ for which $f_{e_{1}}(t_{1}) = f_{e_{2}}(t_{2})$, i.e., the images of $f_{e_{1}}$ and $f_{e_{2}}$ do not intersect except possibly at their endpoints.
- Whenever there are two edges $(u, v)$ and $(u, w)$, the corresponding functions must intersect at one endpoint, and these intersections must be consistent across all the vertices. I.e., every $u \in V$ corresponds to a point $x_{u} \in \mathbb{R}^{2}$ such that for every edge $(u, v)$ incident to $u$, either $f_{(u,v)}(0) = x_{u}$ or $f_{(u,v)}(1) = x_{u}$.

Disgusting! Why did you make me do that?

The problem is that the definition is full of a bunch of "except" and special cases (like that the endpoint could either be zero or one). This makes for ugly mathematics, and the mathematical perspective is to spend a little bit more time understanding exactly what we want from this definition. We are humans, after all, who are inventing this mathematics so that we can explain our ideas easily to others and appreciate the beautiful proofs and algorithms. Keeping track of edge cases is dreary.

### Toward Abstract Spaces and Topology

We really want to define an embedding as a single function $f$ whose codomain is $\mathbb{R}^{2}$. And because we said we don't want any of the edges to cross each other in the plane, we probably want $f$ to be injective. Finally, because the drawing has to be a sensible drawing, we need $f$ to be continuous.

Recall from calculus that a continuous function intuitively maps points that are "close together" in the domain to points that remain close together in the codomain. Without continuity, a "drawing" could break edges into disjoint pieces and there would be chaos.

The real question is: what is the domain of this function? It can't be $G$ as a set because we don't have a notion of "closeness" for pairs of vertices, and we really want to think of an edge as a line-like thing.

The trick is to start imagining abstract spaces that are not sitting in any ambient geometric space. This is where the formalisms of topology shine, but unfortunately a satisfying overview of the basic definitions of topology is beyond the scope of this book. It suffices for our purposes to understand two concepts:

One can take the *disjoint union* of two abstract spaces and get another abstract space in which the points comprising the two pieces are different. In other words, we can take lots of different copies of the same space (in our case $[0, 1]$), their disjoint union is like a bunch of lines, but we aren't presuming any way to compare the different pieces. Each piece retains its internal geometry in the composite.

The second idea is that one can *identify* two points in an abstract space. Intuitively, one can "glue together" two points and maintain the rest of the space unhindered. For us, if a copy of $[0, 1]$ represents an edge, then we'll want two edges incident to the same vertex to have one of their two endpoints identified. This foreshadows a topic in a later chapter called the *equivalence relation*, which formalizes how to identify points in a consistent way.

Putting these two ideas together, the abstract space $X_{G}$ corresponding to a graph $G$ is the disjoint union of copies of $[0, 1]$ for each edge, with endpoints identified when two edges intersect at a vertex. Then we can define a function $f : X_{G} \to \mathbb{R}^{2}$, require it to be injective, and call it continuous if points that are close in $X_{G}$, using the natural distance for points in the interval $[0, 1]$, get sent to points that are close in $f(X_{G})$.

How do I measure distance between two points $a, b \in X_{G}$ that might be on different edges? Well $a, b$ are either vertices or on some copy of $[0, 1]$, so I can find a path in the graph $G$ that gets from one edge to another (if not, then the distance can be called infinite). Then I could measure the length of each full edge on this path, and add up the partial edges required to get from $a$ or $b$ to the desired endpoint of the edge they're in.

This is a very fancy way to say that I can impose the same geometry that was on $[0, 1]$ onto the different pieces of $X_{G}$ and patch them together. But once you get comfortable with that idea, you have a natural way to define an embedding of any abstract space into any other abstract space: a continuous injective function!

If this interests you and you'd like to see it made more formal, pick up a book on topology. Appendix C contains some references. Unfortunately I haven't yet found a topology book that I genuinely like. Most books tend to be terse and contain few pictures (which is the opposite of how topology is done!). Topology aims to generalize much of calculus, so waiting until after Chapter 14 might be prudent.
