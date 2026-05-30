## 14 A Connecticut class in King Arthur's court

<!-- carousel -->
![Figure 47: Two non-3-colorable graphs (first graph)](14 - A Connecticut class in King Arthurs court_images/img-0.jpeg)
![Figure 47: Two non-3-colorable graphs (second graph)](14 - A Connecticut class in King Arthurs court_images/img-1.jpeg)
<!-- endcarousel -->

In the court of King Arthur there dwelt 150 knights and 150 ladies-in-waiting. The king decided to marry them off, but the trouble was that some pairs hated each other so much that they would not even get married, let alone speak! King Arthur tried several times to pair them off but each time he ran into conflicts. So he summoned Merlin the Wizard and ordered him to find a pairing in which every pair was willing to marry. Now Merlin had supernatural powers and he saw immediately that none of the 150! possible pairings was feasible, and this he told the king. But Merlin was not only a great wizard, but a suspicious character as well, and King Arthur did not quite trust him. "Find a pairing or I shall sentence you to be imprisoned in a cave forever!" said Arthur.

Fortunately for Merlin, he could use his supernatural powers to browse forthcoming scientific literature, and he found several papers in the early 20th century that gave the reason why such a pairing could not exist. He went back to the King when all the knights and ladies were present, and asked a certain 56 ladies to stand on one side of the king and 95 knights on the other side, and asked: "Is any one of you ladies, willing to marry any of these knights?", and when all said "No!", Merlin said: "O King, how can you command me to find a husband for each of these 56 ladies among the remaining 55 knights?" So the king, whose courtly education did include the pigeon-hole principle, saw that in this case Merlin had spoken the truth and he graciously dismissed him.

We can reconstruct Merlin's certificate directly with **networkx**. Building a willing-to-marry bigraph engineered with exactly that $56 \to 55$ bottleneck, we run Hopcroft–Karp maximum matching to confirm there is no perfect matching, then exhibit and verify Merlin's violating set $X$ with $|X| = 56$ and $|N(X)| = 55$ — reproducing the book's exact numbers:

```python
<!-- include: code/dm/14 - A Connecticut class in King Arthurs court/01_python.py -->
```

Running it prints `maximum matching size: 149 pairs` and `|X| = 56 ladies`, `|N(X)| = 55 knights`, confirming that the violating set is the easily-checked proof that no perfect matching exists — so *non-existence* of a matching is itself an NP-property (Frobenius' theorem).

Some time elapsed and the king noticed that at the dinners served for the 150 knights at the famous round table, neighbors often quarrelled and even fought. Arthur found this bad for the digestion and so once again he summoned Merlin and ordered him to find a way to seat the 150 knights around the table so that each of them should sit between two friends. Again, using his supernatural powers Merlin saw immediately that none of the 150! seatings would do, and this he reported to the king. Again, the king bade him find one or explain why it was impossible. "Oh I wish there were some simple reason I could give to you! With some luck there could be a knight having only one friend, and so you too could see immediately that what you demand from me is impossible. But alas!, there is no such simple reason here, and I cannot explain to you mortals why no such seating exists, unless you are ready to spend the rest of your life listening to my arguments!" The king was naturally unwilling to do that and so Merlin has lived imprisoned in a cave ever since.

A round seating with only friendly neighbours is exactly a **Hamilton cycle** in the friendship graph, and we can hand that to an SMT solver. We encode "assign each knight a distinct seat so non-friends are never cyclically adjacent" and let **z3** (a) *find* a valid seating for a friendly court — the easy-to-check certificate Merlin hopes for — and (b) prove `UNSAT` for a court containing Sir Kay, a knight with only one friend. The degree-$1$ knight is the chapter's "simple reason" for impossibility: he needs two friendly table-neighbours but has only one.

```python
<!-- include: code/dm/14 - A Connecticut class in King Arthurs court/02_python.py -->
```

Running it prints a concrete `Arthur -> Lancelot -> Gawain -> Percival -> Galahad -> Bors -> Arthur` ring for the friendly court and `z3 proves UNSAT` for the lonely-knight court, confirming that a found seating is an easily-verified certificate while general non-existence (no lonely-knight shortcut) is what kept Merlin imprisoned.

<!-- carousel -->
![Figure 48: Graph $G$ — a bigraph with a perfect matching (shown by the heavy lines)](14 - A Connecticut class in King Arthurs court_images/img-2.jpeg)
![Figure 48: Graph $H$ — a bigraph with no perfect matching (the four black points share only three neighbours)](14 - A Connecticut class in King Arthurs court_images/img-3.jpeg)
<!-- endcarousel -->

(A severe loss for applied mathematics!)

The moral of this tale is that there are properties of graphs which, when they hold, are easily proven to hold. If a graph has a perfect matching, or a Hamilton cycle, this can be "proved" easily by exhibiting one. If a bipartite graph does not have a perfect matching, then this can be "proved" by exhibiting a subset  $X$  of one color class which has fewer than  $|X|$  neighbors in the other. The reader (and King Arthur!) are directed to Figure 48 in which graph  $G$  has a perfect matching (indicated by the heavy lines), but graph  $H$  does not. To see the latter, consider the four black points and their neighbors.

That instruction *is* Hall's condition: four black nodes sharing fewer than four neighbours. Let's confirm it by reproducing both bigraphs in **networkx**, checking that $G$ is perfectly matchable, that $H$ is not, and extracting the four-black-points deficient set as the certificate of non-existence:

```python
<!-- include: code/dm/14 - A Connecticut class in King Arthurs court/03_python.py -->
```

Running it prints a perfect matching for $G$ and, for $H$, `four black points X` with `N(X)` of size $3 < 4$ — exactly the "$4$ black points share only $3$ neighbours" obstruction the figure illustrates.

Most graph-theoretic properties which interest us have this logical structure. Such a property is called (in the jargon of computer science) an NP-property (if you really want to know, NP is an abbreviation of Nondeterministic Polynomial Time, but it would be difficult to explain where this highly technical phrase comes from). The two problems that Merlin had to face — the existence of a perfect matching and the existence of a Hamilton cycle — are clearly NP-properties. But NP-properties also appear quite frequently in other parts of mathematics. A very important NP-property of natural numbers is their compositeness: if a natural number is composite then this can be exhibited easily by showing a decomposition  $n = ab$  ( $a, b > 1$ ).

The remarks we have made so far explain how Merlin can remain free if he is lucky and the task assigned to him by King Arthur has a solution. For instance, suppose he could find a good way to seat the knights for dinner. He could then convince King Arthur that his seating plan was "good" by asking if there was anybody sitting beside an enemy of his. This shows that the property of the corresponding "friendship graph" that it contains a Hamilton cycle is an NP-property. But how could he survive Arthur's wrath in the case of the marriage problem and not in the case of the seating problem when these problems do not have solutions? What distinguishes the non-existence of a Hamilton cycle in a graph from the non-existence of a perfect matching in a bigraph? From our tale, we hope the answer is clear: the non-existence of a perfect matching in a bigraph is also an NP-property (this is a main implication of Frobenius' Theorem), while the non-existence of a Hamilton cycle in a graph is not! (To be precise, no proof of this latter fact is known, but there is strong evidence in favor of it.)

So for certain NP-properties the negation of the property is again an NP-property.

A theorem asserting the equivalence of an NP-property with the negation of another NP-property is called a good characterization. There are famous good characterizations throughout graph theory and elsewhere.

We can stress-test this dichotomy with a **hypothesis** property test. For a bipartite graph, exactly one of two easily-checked certificates always exists: the matching, or a Hall-violating set. Throwing $200$ random bipartite graphs at it, we assert that the smaller side is fully matchable *if and only if* there is no Hall-violating set, then independently verify whichever certificate networkx produces:

```python
<!-- include: code/dm/14 - A Connecticut class in King Arthurs court/04_python.py -->
```

Running it prints `1 passed`, confirming across all generated graphs that the matching/Hall dichotomy holds and both certificates check out — the precise reason Merlin could always answer the marriage question, unlike the Hamilton-cycle seating question.

Many NP-properties are even better. Facing the problem of marrying off his knights and ladies, Arthur himself (say, after attending this class) could decide himself whether or not it was solvable: he could run the algorithm described in section 12.4. A lot of work, but probably doable with the help of quite ordinary people, without using the supernatural talents of Merlin. Properties which can be decided efficiently are called properties in the class P (here P stand for Polynomial Time, an exact but quite technical definition of the phrase “efficiently”). Many other simple properties of graphs discussed in this book also belong to the class: connectivity, or the existence of a cycle.
