# uv run --with networkx python
#
# The Prufer code (Section 10.4, method (d)) on the book's own example.
#
# We implement the book's EXACT construction rule, not a library shortcut:
#   "look for a node of degree 1, different from 0, with the smallest label,
#    write down its edge (son on top, father on bottom), delete it, repeat."
# For the tree of Figure 24 this must reproduce, verbatim, the extended
# Prufer code printed in the book:
#       first row : 1 3 4 5 6 7 8 9 2
#       second row: 6 0 2 6 2 9 9 2 0
# and hence the Prufer code (first n-2 of the second row): 6 0 2 6 2 9 9 2.
#
# We then verify Lemma 10.1 ("the second row determines the first") by
# reconstructing the first row from second row 2 4 0 3 3 1 0 (the book's
# 8-node example, Figure 25) and checking we get 5 2 4 6 7 3 1.
import networkx as nx


def figure_24_tree():
    edges = [(1, 6), (2, 0), (3, 0), (4, 2), (5, 6),
             (6, 2), (7, 9), (8, 9), (9, 2)]
    G = nx.Graph()
    G.add_nodes_from(range(10))
    G.add_edges_from(edges)
    return G


def extended_prufer(G):
    """Book's rule: repeatedly strip the smallest-label leaf != root 0."""
    G = G.copy()
    first, second = [], []
    while G.number_of_edges() > 0:
        v = min(u for u in G.nodes() if G.degree(u) == 1 and u != 0)
        father = next(iter(G.neighbors(v)))
        first.append(v)
        second.append(father)
        G.remove_node(v)
    return first, second


def reconstruct_first_row(second):
    """Lemma 10.1 rule (book): each first-row entry is the smallest integer
    not already in the first row, nor in the second row at/after this column."""
    n = len(second) + 1  # second row has n-1 entries
    first = []
    for k in range(len(second)):
        used = set(first)
        below_after = set(second[k:])
        for cand in range(n):
            if cand not in used and cand not in below_after:
                first.append(cand)
                break
    return first


def main():
    G = figure_24_tree()
    first, second = extended_prufer(G)
    print("Extended Prufer code of Figure 24:")
    print(f"  first row  = {first}")
    print(f"  second row = {second}")
    ok_first = first == [1, 3, 4, 5, 6, 7, 8, 9, 2]
    ok_second = second == [6, 0, 2, 6, 2, 9, 9, 2, 0]
    print(f"  matches book first  row 1 3 4 5 6 7 8 9 2 : {ok_first}")
    print(f"  matches book second row 6 0 2 6 2 9 9 2 0 : {ok_second}")
    prufer = second[:-1]  # drop the trailing 0
    print(f"  Prufer code (length n-2) = {prufer}")
    print(f"  matches book 6 0 2 6 2 9 9 2 : {prufer == [6,0,2,6,2,9,9,2]}")

    print("\nLemma 10.1: second row determines first"
          " (8-node example, Figure 25):")
    second2 = [2, 4, 0, 3, 3, 1, 0]
    fr = reconstruct_first_row(second2)
    print(f"  given second row = {second2}")
    print(f"  reconstructed first row = {fr}")
    print(f"  matches book 5 2 4 6 7 3 1 : {fr == [5,2,4,6,7,3,1]}")


if __name__ == "__main__":
    main()
