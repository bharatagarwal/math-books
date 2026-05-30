# uv run --with networkx python
#
# Tribes and tortoises (Section 12.2) + the Marriage Theorem (12.2).
# Six tribes must each pick a DIFFERENT tortoise species that lives on their
# territory -- i.e. we want a perfect matching in the bipartite graph of
# Figure 32. The book argues a matching must exist because of "Hall's
# condition": any k tribes have, on their combined territory, at least k
# species (else k species would have to cover > 100*k sq mi of a 100*k region).
#
# We (1) check Hall's condition directly over ALL 2^6 subsets of tribes,
# and (2) confirm a perfect matching (a valid totem assignment) actually
# exists via Hopcroft-Karp. The two facts agree, illustrating the theorem's
# "if and only if".

from itertools import combinations
import networkx as nx

# Tribe A has 2 tortoises to choose from, tribe D has 4 (the book's words).
# A concrete acquaintance pattern consistent with the chapter's Figure 32:
territory = {
    "A": {1, 2},            # tribe A: 2 species  (book: "only two")
    "B": {2, 3},
    "C": {3, 4},
    "D": {1, 4, 5, 6},      # tribe D: 4 species  (book: "four")
    "E": {5, 6},
    "F": {1, 6},
}
tribes = list(territory)
species = sorted({s for ss in territory.values() for s in ss})
print("tribe -> available species:", {t: sorted(territory[t]) for t in tribes})

G = nx.Graph()
G.add_nodes_from(tribes, bipartite=0)
G.add_nodes_from([("sp", s) for s in species], bipartite=1)
for t in tribes:
    for s in territory[t]:
        G.add_edge(t, ("sp", s))

# (1) Hall's condition: for every subset S of tribes, |neighbours(S)| >= |S|.
def neighbours(S):
    nb = set()
    for t in S:
        nb |= territory[t]
    return nb

hall_holds = True
tightest = None
for k in range(1, len(tribes) + 1):
    for S in combinations(tribes, k):
        nb = neighbours(S)
        if len(nb) < len(S):
            hall_holds = False
        if tightest is None or len(nb) - len(S) < tightest[2]:
            tightest = (S, sorted(nb), len(nb) - len(S))
print("Hall's condition holds for all 2^6 subsets:", hall_holds)
print("tightest subset (smallest slack):", tightest[0],
      "-> species", tightest[1], "slack", tightest[2])
assert hall_holds

# (2) A perfect matching = a valid assignment of distinct totems.
matching = nx.bipartite.maximum_matching(G, top_nodes=tribes)
totems = {t: matching[t][1] for t in tribes}
print("totem assignment:", totems)
assert len(set(totems.values())) == len(tribes)        # all distinct
for t, s in totems.items():
    assert s in territory[t]                            # lives on territory
print("Marriage Theorem confirmed: Hall's condition holds, and a perfect")
print("matching (distinct totems for all 6 tribes) exists.")
