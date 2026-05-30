<!-- page 1 -->

9 Graphs

### 9.1 Even and odd degrees

We start with the following exercise (admittedly of no practical significance).

*Prove that at a party with 51 people, there is always a person who knows an even number of others.* (We assume that acquaintance is mutual. There may be people who don’t know each other. There may even be people who don’t know anybody else — of course, such people know an even number of others, so the assertion is true if there is such a person.)

If you don’t have any idea how to begin a solution, you should try to experiment. But how to experiment with such a problem? Should we find 51 names for the participants, then create, for each person, a list of those people he knows? This would be very tedious, and we would be lost among the data. It would be good to experiment with smaller numbers. But which number can we take instead of 51? It is easy to see that 50, for example, would not do: if, say, we have 50 people all know each other, then everybody knows 49 others, so there is no person with an even number of acquaintances. For the same reason, we could not replace 51 by 48, or 30, or any even number. Let’s hope that this is all; let’s try to prove that

*at a party with an odd number of people, there is always a person who knows an even number of others.*

Now we can at least experiment with smaller numbers. Let us have, say, 5 people: Alice, Bob, Carl, Diane and Eve. When they first met, Alice new everybody else, Bob and Carl new each other, and Carl also new Eve. So the numbers of acquaintances are : Alice 4, Bob 2, Carl 3, Diane 1 and Eve 2. So we have not only one but three people with an even number of acquaintances.

It is still rather tedious to consider examples by listing people and listing pairs knowing each other, and it is quite easy to make mistakes. We can, however, find a graphic illustration that helps a lot. We represent each person by a point in the plane (well, by a small circle, to make the picture nicer), and we connect two of these points by a segment if the people know each other. This simple drawing contains all the information we need (Figure 14).

A picture of this kind is called a *graph*. More exactly, a graph consists of a set of *nodes* (or *points*, or *vertices*, all these names are in use), and some pairs of these (not necessarily all pairs) are connected by *edges* (or *lines*). It does not matter whether these edges are straight of curvy; all that is important is which pair of nodes they connect. The set of nodes of a graph $G$ is usually denoted by $V$; the set of edges, by $E$. Thus we write $G=(V,E)$ to indicate that the graph $G$ has node set $V$ and edge set $E$.

The only thing that matters about an edge is the pair of nodes it connects; hence the edges can be considered as 2-element subsets of $V$. This means that the edge connecting nodes $u$ and $v$ is just the set $\{u,v\}$. We’ll further simplify notation and denote this edge by $uv$.

Coming back to our problem, we see that we can represent the party by a graph very conveniently. Our concern is the number of people known by a given person. We can read this off the graph by counting the number of edges leaving a given node. This number is called the *degree* (or *valency*) of the node. The degree of node $v$ is denoted by $d(v)$. So $A$

---

<!-- page 2 -->

![img-0.jpeg](09 - Graphs_images/img-0.jpeg)
Figure 14: The graph depicting aquaitence between our friends

![img-1.jpeg](09 - Graphs_images/img-1.jpeg)
Figure 15: Some graphs with an odd number of nodes, with nodes of even degree marked

has degree 4,  $B$  has degree 2, etc. If Frank now arrives, and he does not know anybody, then we add a new node that is not connected to any other node. So this new node has degree 0.

In the language of graph theory, we want to prove:

if a graph has an odd number of nodes than it has a node with even degree.

Since it is easy to experiment with graphs, we can draw a lot of graphs with an odd number of nodes, and count the number of nodes with even degree (Fig. 15). We find that they contain 1, 5, 3, 3, 7 such nodes. So we observe that not only is there always such a node, but the number of such nodes is odd.

Now this is a case when it is easier to prove more: if we formulate the following stronger statement:

if a graph has an odd number of nodes then the number of nodes with even degree is odd, then we made an important step towards the solution! (Why is this statement stronger? Because 0 is not an odd number.) Let's try to find an even stronger statement by looking also at graphs with an even number of nodes. Experimenting on several small graphs again (Fig 16), we find that the number of nodes with even degree is 2, 0, 4, 2, 0. So we conjecture that the following is true:

if a graph has an even number of nodes then the number of nodes with even degree is even.

---

<!-- page 3 -->

![img-2.jpeg](09 - Graphs_images/img-2.jpeg)
Figure 16: Some graphs with an even number of nodes, with nodes of even degree marked

![img-3.jpeg](09 - Graphs_images/img-3.jpeg)
Figure 17: Building up a graph one edge at a time

This is nicely parallel to the statement about graphs with an odd number of nodes, but it would be better to have a single common statement for the odd and even case. We get such a version if we look at the number of nodes with odd, rather than even, degree. This number is obtained by subtracting the number of nodes with even degree from the total number of nodes, and hence both statements will be implied by the following:

# Theorem 9.1 In every graph, the number of nodes with odd degree is even.

We still have to prove this theorem. It seems that having made the statement stronger and more general in several steps, we made our task harder and harder. But in fact we got closer to the solution.

One way of proving the theorem is to build up the graph one edge at a time, and observe how the parities of the degrees change. An example is shown in Figure 17. We start with a graph with no edge, in which every degree is 0, and so the number of nodes with odd degree is 0, which is an even number.

Now if we connect two nodes by a new edge, we change the parity of the degrees at these nodes. In particular,

- if both endpoints of the new edge had even degree, we increase the number of nodes with odd degree by 2;
- if both endpoints of the new edge had odd degree, we decrease the number of nodes with odd degree by 2;

---

<!-- page 4 -->

— if one endpoint of the new edge had even degree and the other had odd degree, then we don’t change the number of nodes with odd degree.

Thus if the number of nodes with odd degree was even before adding the new edge, it remained even after this step. This proves the theorem. (Note that this is a proof by induction on the number of edges.)

Graphs are very handy in representing a large variety of situations, not only parties. It is quite natural to consider the graph whose nodes are towns and whose edges are highways (or railroads, or telephone lines) between these towns. We can use a graph to describe an electrical network, say the printed circuit on a card in your computer.

In fact, graphs can be used any situation where a “relation” between certain objects is defined. Graphs are used to describe bonds between atoms in a molecule; connections between cells in the brain; descendence between species, etc. Sometimes the nodes represent more abstract things: for example, they may represent stages of a large construction project, and an edge between two stages means that one arises from the other in a single phase of work. Or the nodes can represent all possible positions in a game (say, chess, although you don’t really want to draw this graph), where we connect two nodes by an edge if one can be obtained from the other in a single move.

> 9.1 Find all graphs with 2,3 and 4 nodes.
>
> 9.2 (a) Is there a graph on 6 nodes with degrees 2,3,3,3,3,3?
>
> (b) Is there a graph on 6 nodes with degrees 0,1,2,3,4,5?
>
> (c) How many graphs are there on 4 nodes with degrees 1,1,2,2?
>
> (d) How many graphs are there on 10 nodes with degrees 1,1,1,1,1,1,1,1,1,1,1?
>
> 9.3 At the end of the party, everybody knows everybody else. Draw the graph representing this situation. How many edges does it have?
>
> 9.4 Draw the graphs representing the bonds between atoms in (a) a water molecule; (b) a methane molecule; (c) two water molecules.
>
> 9.5 (a) Draw a graph with nodes representing the numbers 1,2,…,10, in which two nodes are connected by an edge if and only if one is a divisor of the other.
>
> (b) Draw a graph with nodes representing the numbers 1,2,…,10, in which two nodes are connected by an edge if and only if they have no common divisor larger than 1.
>
> (c) Find the number of edges and the degrees in these graphs, and check that theorem 9.1 holds.
>
> 9.6 What is the largest number of edges a graph with 10 nodes can have?
>
> 9.7 How many graphs are there on 20 nodes? (To make this question precise, we have to make sure we know what it means that two graphs are the same. For the purposes of this exercise, we consider the nodes given, and labeled say, as Alice, Bob, …The graph consisting of a single edge connecting Alice and Bob is different from the graph consisting of a single edge connecting Eve and Frank.)
>
> 9.8 Formulate the following assertion as a theorem about graphs, and prove it: At every party one can find two people who know the same number of other people (like Bob and Eve in our first example).

---

<!-- page 5 -->

![img-4.jpeg](09 - Graphs_images/img-4.jpeg)
Figure 18: Two paths and two cycles

It will be instructive to give another proof of the theorem formulated in the last section. This will hinge on the answer to the following question: How many edges does a graph have? This can be answered easily, if we think back to the problem of counting handshakes: for each node, we count the edges that leave that node (this is the degree of the node). If we sum these numbers, we count every edge twice. So dividing the sum by two, we get the number of edges. Let us formulate this observation as a theorem:

Theorem 9.2 The sum of degrees of all nodes in a graph is twice the number of edges.

In particular, we see that the sum of degrees in any graph is an even number. If we omit the even terms from this sum, we still get an even number. So the sum of odd degrees is even. But this is only possible if the number of odd degrees is even (since the sum of an odd number of odd numbers is odd). Thus we have obtained a new proof of Theorem 9.1.

# 9.2 Paths, cycles, and connectivity

Let us get acquainted with some special kinds of graphs. The simplest graphs are the empty graphs, having any number of nodes but no edges.

We get another very simple kind of graphs if we take  $n$  nodes and connect any two of them by an edge. Such a graph is called a complete graph (or a clique). A complete graph with  $n$  nodes has  $\binom{n}{2}$  edges (recall exercise 9.1).

Let us draw  $n$  nodes in a row and connect the consecutive ones by an edge. This way we obtain a graph with  $n - 1$  edges, which is called a path. The first and last nodes in the row are called the endpoints of the path. If we also connect the last node to the first, we obtain a cycle (or circuit). Of course, we can draw the same graph in many other ways, placing the nodes elsewhere, and we may get edges that intersect (Figure 18).

A graph  $H$  is called a subgraph of a graph  $G$  if it can be obtained from  $G$  by deleting some of its edges and nodes (of course, if we delete a node we automatically delete all the edges that connect it to other nodes).

9.9 Find all complete graphs, paths and cycles among the graphs in the previous figures.
9.10 How many subgraphs does an empty graph on  $n$  nodes have? How many subgraphs does a triangle have?

---

<!-- page 6 -->

![img-5.jpeg](09 - Graphs_images/img-5.jpeg)
Figure 19: A path in a graph connecting two nodes

A key notion in graph theory is that of a connected graph. It is heuristically clear what this should mean, but it is also easy to formulate the property as follows: a graph  $G$  is connected if every two nodes of the graph can be connected by a path in  $G$ . To be more precise: a graph  $G$  is connected if for every two nodes  $u$  and  $v$ , there exists a path with endpoints  $u$  and  $v$  that is a subgraph of  $G$  (Figure 19).

It will be useful to include a little discussion of this notion. Suppose that nodes  $a$  and  $b$  can be connected by a path  $P$  in our graph. Also suppose that nodes  $b$  and  $c$  can be connected by a path  $Q$ . Can  $a$  and  $c$  be connected by a path? The answer seems to be obviously "yes", since we can just go from  $a$  to  $b$  and then from  $b$  to  $c$ . But there is a difficulty: concatenating (joining together) the two paths may not yield a path from  $a$  to  $c$ , since  $P$  and  $Q$  may intersect each other (Figure 20). But we can construct a path from  $a$  to  $c$  easily: Let us follow the path  $P$  to its first common node  $d$  with  $Q$ ; then let us follow  $Q$  to  $c$ . Then the nodes we traversed are all distinct. Indeed, the nodes on the first part of our walk are distinct because they are nodes of the path  $P$ ; similarly, the nodes on the second part are distinct because they are nodes of the path  $Q$ ; finally, any node of the first part must be distinct from any node of the second part (except, of course, the node  $d$ ), because  $d$  is the first common node of the two paths and so the nodes of  $P$  that we passed through before  $d$  are not nodes of  $Q$  at all. Hence the nodes and edges we have traversed form a path from  $a$  to  $c$  as claimed. $^3$

9.11 Is the proof as given above valid if (a) the node  $a$  lies on the path  $Q$ ; (b) the paths  $P$  and  $Q$  have no node in common except  $b$ .
9.12 (a) We delete an edge  $e$  from a connected graph  $G$ . Show by an example that the

---

<!-- page 7 -->

![img-6.jpeg](09 - Graphs_images/img-6.jpeg)

![img-7.jpeg](09 - Graphs_images/img-7.jpeg)

![img-8.jpeg](09 - Graphs_images/img-8.jpeg)
Figure 20: How to select a path from  $a$  to  $c$ , given a path from  $a$  to  $b$  and a path from  $b$  to  $c$ ?

---

<!-- page 8 -->

remaining graph may not be connected.

(b) Prove that if we assume that the deleted edge $e$ belongs to a cycle that is a subgraph of $G$, then the remaining graph is connected.

9.13 Let $G$ be a graph and let $u$ and $v$ be two nodes of $G$. A walk in $G$ from $u$ to $v$ is a sequence of nodes $(w_{0},w_{1},\ldots,w_{k})$ such that $w_{0}=u$, $w_{k}=v$, and consecutive nodes are connected by an edge, i.e., $w_{i}w_{i+1}\in E$ for $i=0,1,\ldots,k-1$.

(a) Prove that if there is a walk in $G$ from $u$ to $v$, then $G$ contains a path connecting $u$ to $v$.

(b) Use part (a) to give another proof of the fact that if $G$ contains a path connecting $a$ and $b$, and also a path connecting $b$ to $c$, then it contains a path connecting $a$ to $c$.

9.14 Let $G$ be a graph, and let $H_{1}=(V_{1},E_{1})$ and $H_{2}=(V_{2},E_{2})$ be two subgraphs of $G$ that are connected. Assume that $H_{1}$ and $H_{2}$ have at least one node in common. Form their union, i.e., the subgraph $H=(V^{\prime},E^{\prime})$, where $V^{\prime}=V_{1}\cup V_{2}$ and $E^{\prime}=E_{1}\cup E_{2}$. Prove that $H$ is connected.

Let $G$ be a graph that is not necessarily connected. $G$ will have connected subgraphs; for example, the subgraph consisting of a single node (and no edge) is connected. A connected component $H$ is a maximal subgraph that is connected; in other words, $H$ is a connected component if it is connected but every other subgraph of $G$ that contains $H$ is disconnected. It is clear that every node of $G$ belongs to some connected component. It follows by exercise 9.2 that different connected components of $G$ have no node in common (else, their union would be a connected subgraph containing both of them). In other words, every node of $G$ is contained in a unique connected component.

9.15 Determine the connected components of the graphs constructed in exercise 9.1.

9.16 Prove that no edge of $G$ can connect nodes in different connected components.

9.17 Prove that a node $v$ is a node of the connected component of $G$ containing node $u$ if and only if $g$ contains a path connecting $u$ to $v$.

9.18 Prove that a graph with $n$ nodes and more than $\binom{n-1}{2}$ edges is always connected.

##