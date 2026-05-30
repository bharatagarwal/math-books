# Graph Theory

*Bradfield session 9 · Monday 13 July · pre-work: LL chapters 9 & 12*

Graphs are the data structure a programmer already knows — nodes and edges,
networks and dependencies, the thing your shortest-path and topological-sort
algorithms run on. Graph *theory* steps back from traversal to ask *structural*
questions, and Lovász (our **LL** text, the *Discrete Mathematics* book in this
reader) opens exactly the way he opened counting: with a party. That is
deliberate, and worth imitating. Like counting, graph theory is a place where
the objects are concrete enough that, when in doubt, **you can build them and
look** — and where the proofs come from *experimenting on small cases, guessing
the pattern, then strengthening the claim until it proves itself.* We follow LL
chapters 9 and 12 in that order: the handshake parity lemma, the degree-sum
identity, paths and trees, Euler's bridges, and finally matchings as the
chapter's climax. Each idea is stated, then either *discovered* by building the
objects or *verified* against an algorithm in `networkx`.

## Lovász's party: discovering the handshake lemma

LL §9.1 starts with a puzzle "of no practical significance": *at a party of 51
people, someone must know an even number of the others.* Why 51? Because the
claim is **false** for even crowds — 50 people who all know each other each know
$49$ others, an odd number, every one of them. So the real statement is *odd*
party size forces an even-acquaintance person. As LL says, experiment on small
cases. Five guests — Alice, Bob, Carl, Diane, Eve — where Alice knows everyone,
Bob and Carl know each other, and Carl also knows Eve, give acquaintance counts
$4, 2, 3, 1, 2$: three people with an even count.

To stop drowning in name-lists, draw it. A **graph** $G = (V, E)$ is a set of
**nodes** (vertices) $V$ and a set of **edges** $E$, each edge a $2$-element
subset $\{u, v\}$ of $V$, written $uv$. The **degree** $d(v)$ of a node is how
many edges touch it. The party is now a graph and "number of acquaintances" is
just degree. We can build LL's Figure 14 exactly and read the degrees off:

```python
<!-- include: code/bradfield/09-graph-theory/01_handshake.py -->
```

That demo encodes a $5$-cycle-with-a-chord rather than the literal party, but it
makes the two facts we are about to prove concrete: it prints
`sum of degrees = 12 = 2|E| = 12` and reports the odd-degree vertices as `[0, 2]`
— **an even number of them**, exactly as the lemma will force. It also checks the
**complete graph** $K_n$ (every pair joined), which has $\binom{n}{2}$ edges and
every degree $n-1$.

Now LL does the move that makes the chapter: rather than prove the weak claim, he
*strengthens* it. Draw many graphs and count even-degree nodes; for odd $n$ the
counts come out $1, 5, 3, 3, 7$ — always **odd**. For even $n$ they come out
$2, 0, 4, 2, 0$ — always **even**. One statement covers both cases if we count
*odd*-degree nodes instead:

**Theorem 9.1 (LL).** *In every graph, the number of nodes with odd degree is
even.*

LL's proof is an induction on edges (his Figure 17): **build the graph one edge
at a time.** Start with no edges — zero odd-degree nodes, which is even. Adding
an edge flips the parity at its two endpoints, so the odd-degree count changes by
$+2$ (both ends were even), $-2$ (both odd), or $0$ (one of each) — never by an
odd amount. So the count, even at the start, stays even forever. This is the kind
of argument best *watched*, so our first intuition demo grows the party graph
edge by edge and prints the running odd-degree count, asserting it never goes
odd — then replays the same mechanism over $2000$ random growth orders:

```python
<!-- include: code/bradfield/09-graph-theory/05_parity_grows.py -->
```

Running it prints the trace `+AB: #odd 0 -> 2`, `+AC: #odd 2 -> 2`,
`+AD: #odd 2 -> 4`, … ending at `final degrees: {'A': 4, 'B': 2, 'C': 3, 'D': 1,
'E': 2}` (two odd-degree nodes, Carl and Diane), and then
`invariant '#odd-degree nodes is even' held after every edge, over 2000 random
growth sequences`. The parity invariant of Theorem 9.1 is the recurring tool of
the whole subject: *parity invariants prove things impossible* (no Euler walk
across Königsberg, no perfect matching when Hall's condition fails).

LL then gives a *second*, slicker proof via a counting identity — the same
handshake-counting move from chapter 1, where each handshake is double-counted:

**Theorem 9.2 (LL).** *The sum of all degrees equals twice the number of edges:*
$$\sum_{v \in V} d(v) = 2\,|E|,$$
*because each edge adds exactly $1$ to each of its two endpoints, hence $2$ to
the total.* In particular the degree sum is even; dropping the even terms leaves
the sum of the *odd* degrees still even, which forces an even *count* of them
(the sum of an odd number of odd numbers is odd) — a one-line re-proof of
Theorem 9.1. The `01` demo above checks $\sum_v d(v) = 2|E|$ directly.

## Special graphs: paths, cycles, and connectivity

LL §9.2 names the building blocks. The **empty graph** has no edges. The
**complete graph** $K_n$ joins every pair: $\binom{n}{2}$ edges. A **path** $P_n$
puts $n$ nodes in a row joined consecutively — $n-1$ edges and two degree-$1$
**endpoints**; closing the last node back to the first makes a **cycle** $C_n$ —
$n$ edges, every degree $2$. A graph is **connected** when every two nodes are
joined by a path; the maximal connected pieces are its **connected components**,
and (LL exercise 9.16) no edge ever crosses between two components. These are
clean definitions to make executable — build each special graph, check its edge
count against the formula, verify connectivity *by the book's definition*, and
split a disconnected graph into its components.

The next demo retargets last chapter's tree object to do exactly this kind of
structural bookkeeping; we examine it under trees, where the path-uniqueness
property lives.

## Trees: the minimally connected graphs

LL chapter 10 isolates the most important family. A **tree** is a graph that is
**connected and contains no cycle.** The two conditions pull opposite ways:
connectedness forbids *too few* edges, acyclicity forbids *too many*. LL's
Theorem 10.1 makes that precise — a tree is *minimally connected* (delete any
edge and it falls into two pieces) and *maximally acyclic* (add any edge and a
cycle appears). LL Theorem 10.3 also says every tree **grows** one leaf at a
time, which immediately yields the count that makes trees so usable:

**Theorem 10.4 (LL).** *Every tree on $n$ nodes has exactly $n - 1$ edges* —
because growth starts with one more node than edge ($1$ vs $0$) and each step
adds one of each, preserving the gap. And (Theorem 10.2) every tree with $\ge 2$
nodes has at least **two leaves** (degree-$1$ nodes). The reader builds these
constantly: file systems, parse trees, spanning trees. We verify the equivalent
characterizations on a concrete $5$-node tree:

```python
<!-- include: code/bradfield/09-graph-theory/02_trees.py -->
```

Running it prints `tree on 5 nodes has 4 = n-1 edges, unique paths, and is
edge-critical`. The demo checks all of LL's tree facts on one object:
`is_tree`/`is_connected` plus $|E| = n - 1$ (Theorem 10.4); that there is
**exactly one** simple path between every pair of nodes (LL exercise 10.3, the
defining property of trees); and edge-criticality both ways — adding an edge
makes a cycle (no longer a tree), removing one disconnects it (Theorem 10.1).
A *spanning tree* is then just the $n-1$-edge backbone that keeps a network
connected with nothing to spare, which is why minimum-spanning-tree algorithms
are the cheapest-network workhorse.

## Euler's bridges, and the odd-cycle test for bipartiteness

Graph theory was *born* in 1736 when Euler settled the **Bridges of
Königsberg**: is there a walk crossing every bridge exactly once? His answer is a
pure parity-of-degree condition, and it is the handshake lemma doing real work.
An **Euler circuit** (return to start, every edge once) exists iff the graph is
connected and **every vertex has even degree** — each visit to a node uses two
incident edges, so an odd degree would strand you. An **Euler path** with
different endpoints exists iff **exactly two** vertices have odd degree (the start
and the end). Königsberg's four landmasses all had odd degree, so no walk exists
— a parity invariant proving impossibility, exactly the tool from Theorem 9.1.

A second structural test sets up the whole next section. A graph is **bipartite**
— its nodes split into two classes $A$ and $B$ with every edge going *between*
them — iff it has **no odd cycle.** (Walk around any cycle alternating sides
$A, B, A, B, \dots$; you can only return to your starting side after an *even*
number of steps.) Bipartite graphs model every "two kinds of things" relation:
workers and jobs, students and dance partners, tribes and totems. We check both
classics — the degree condition for Euler walks, and the odd-cycle obstruction
for bipartiteness:

```python
<!-- include: code/bradfield/09-graph-theory/03_euler_bipartite.py -->
```

Running it prints `C4 is Eulerian (all even degrees); path 0-1-2 has an Euler
path (2 odd vertices)` and `even cycle bipartite: True   odd cycle bipartite:
False`. The $4$-cycle is Eulerian and bipartite; the $5$-cycle — an odd cycle —
is neither $2$-colorable nor bipartite, and the path graph has its two odd-degree
endpoints. The odd cycle is the single obstruction that will reappear in both
matching and coloring.

## Matchings: the chapter's climax (LL chapter 12)

LL chapter 12 opens with the **prom**: $300$ students, every girl knows exactly
$50$ boys and every boy exactly $50$ girls; can they *all* dance at once with
partners they know? Model it as a bipartite graph — boys on the left, girls on
the right, an edge for each acquaintance — and the question becomes: does it have
a **perfect matching**? A **matching** is a set of edges sharing no endpoint (an
assignment); it is **perfect** when every node is covered. LL guesses (correctly)
that the numbers $300$ and $50$ are irrelevant — only *regularity* matters:

**Theorem 12.1 (LL).** *If every node of a bipartite graph has the same degree
$d \ge 1$, it has a perfect matching.*

Before proving anything, watch it happen as $d$ grows. Our intuition demo builds
clean $d$-regular bipartite "proms" and runs a real maximum-matching algorithm,
showing everyone always pairs off — then discovers the *general* condition by
breaking it:

```python
<!-- include: code/bradfield/09-graph-theory/06_prom_hall.py -->
```

The first half prints `d=1: |E|=  8  matched 8/8 pairs`, … `d=5: |E|= 40  matched
8/8 pairs` — every regular bipartite graph dances perfectly (Theorem 12.1). The
second half builds LL's **tribes-and-tortoises** graph (Figure 32): six tribes
must each pick a distinct tortoise totem found on their land — tribe $A$ has $2$
choices, tribe $D$ has $4$. Regularity fails here, so what *does* guarantee a
matching? LL's observation: any $k$ tribes' combined territory holds at least $k$
tortoise species. In graph terms, **every set of $k$ left nodes has at least $k$
neighbors on the right** — and that is exactly the condition that decides it:

**Theorem 12.2 (The Marriage Theorem / Hall, LL).** *A bipartite graph has a
perfect matching iff $|A| = |B|$ and every $k$ nodes on one side are joined to at
least $k$ nodes on the other.*

The demo verifies Hall's condition over all $2^6$ subsets (`Hall's condition over
all 2^6 subsets: True`), finds a valid assignment (`totem assignment: {'A':
't1', ..., 'F': 't6'}`, all six distinct), then **breaks** it (LL exercise
12.2(b)): forcing tribes $A, B, C$ to share only totems $\{t_1, t_2\}$ makes a
set of $3$ left nodes with only $2$ neighbors. Hall fails, and the algorithm
reports `max matching size when Hall fails: 5 (< 6)` — the other tribes still
pair off, but $A, B, C$ cannot all be satisfied, so no *perfect* matching
exists, machine-confirming the "only if" direction. Hall's condition is the parity
invariant's cousin: a *counting* obstruction (too few neighbors) proving a
matching impossible.

The matching/cover duality is just as useful in practice. **König's theorem**
says that in a bipartite graph the **maximum matching equals the minimum vertex
cover** — the largest assignment is bounded by the smallest set of nodes touching
every edge. This is the LP-duality skeleton behind flow and scheduling. We check
it alongside coloring next.

## Coloring: scheduling, register allocation, and the odd cycle again

LL chapter 13 closes with **graph coloring**: assign colors to nodes so adjacent
nodes differ; the **chromatic number** $\chi(G)$ is the fewest colors any proper
coloring needs. This is *register allocation* (variables live at the same time
conflict and need different registers), *scheduling* (overlapping tasks need
different slots), and the four-color map problem. LL's chapter-opening result —
that the regions cut out by $n$ circles are always $2$-colorable — is the
statement that those region maps are *bipartite*, and the odd-cycle obstruction
from the Euler section returns precisely:

- an **even cycle** is bipartite and needs $2$ colors;
- an **odd cycle** is not bipartite and needs $3$;
- the **complete graph** $K_n$ needs all $n$ (everyone borders everyone).

So $2$-colorability **is** bipartiteness is no-odd-cycle — three names for one
thing. The final demo verifies the coloring numbers, the matching size, and
König's matching = cover equality together:

```python
<!-- include: code/bradfield/09-graph-theory/04_coloring_matching.py -->
```

Running it prints `coloring: even cycle 2, odd cycle 3, K4 needs 4` and
`max matching in K(2,3) has size 2 = min vertex cover size 2 (Konig)`. The
coloring half checks $\chi(C_4) = 2$, $\chi(C_5) = 3$, $\chi(K_4) = 4$ (with the
proper-coloring property asserted on every edge); the matching half builds
$K_{2,3}$, finds its maximum matching of size $\min(2, 3) = 2$, and confirms
König by deriving the minimum vertex cover and checking the two sizes agree.

## Working the problem set

The pre-work is LL chapters 9 and 12; the supporting characterizations of trees
are LL chapter 10 and the coloring/odd-cycle connection is LL chapter 13. A few
threads to carry into the exercises:

- **Parity invariants prove impossibility.** Theorem 9.1 (odd-degree count is
  even), Euler's degree condition, and "an odd cycle cannot be $2$-colored" are
  all the same move: an invariant that an object would have to violate.
- **Strengthen the claim to prove it.** LL's party argument got *easier* as it
  got more general (51 people → odd $n$ → all graphs). The generalization is
  often the provable statement.
- **Hall's condition** is the necessary-and-sufficient test for a bipartite
  perfect matching; **König** turns max-matching into min-cover; both are checked
  by polynomial algorithms even though brute force ($150!$ pairings) is hopeless.
- **One obstruction, three guises:** no odd cycle $\iff$ bipartite $\iff$
  $2$-colorable.

The deeper treatment, with full exercises, is LL chapters 9–13 (the **Discrete
Mathematics** book here) and MCS chapters 10–13; the 6.042J "Graph Theory"
videos are excellent. Matchings are a flow problem, coloring is NP-hard in
general, and (from the previous chapter) a graph's importance rankings and
clusters are *eigenvector* problems on its matrices. Next we turn to **number
theory**, the foundation for cryptography.
