# uv run --with networkx python
#
# Section 11.1 / Figure 27: the greedy ("optimistic") method is optimal for the
# cheapest TREE, but FAILS for the cheapest CYCLE (the Travelling Salesman
# tour).
#
# The chapter: "Figure 27 shows an example where the optimistic method (called
# 'greedy') gives a cycle that is quite a bit worse than optimal."
#
# We reproduce that failure on 4 towns with explicit construction costs c(ij).
# Greedy builds a tour by repeatedly taking the cheapest edge that keeps every
# town at degree <= 2 and does not close a short cycle (exactly the rule the
# book describes). We compare it against the exact optimum found by brute force
# over all permutations (feasible only because TSP is hard -- the whole point).
import itertools
import networkx as nx

# Symmetric construction costs between 4 towns.
C = {
    ("1", "2"): 1, ("1", "3"): 2, ("1", "4"): 3,
    ("2", "3"): 3, ("2", "4"): 9, ("3", "4"): 4,
}
TOWNS = ["1", "2", "3", "4"]


def cost(u, v):
    return C[(u, v)] if (u, v) in C else C[(v, u)]


def tour_cost(perm):
    n = len(perm)
    return sum(cost(perm[i], perm[(i + 1) % n]) for i in range(n))


def optimal_tour():
    """Exact TSP by brute force over all cyclic orders (n! permutations)."""
    return min((tour_cost(p), p) for p in itertools.permutations(TOWNS))


def greedy_tour():
    """The book's optimistic rule, building a CYCLE instead of a tree."""
    edges = sorted(C.items(), key=lambda kv: kv[1])  # cheapest first
    deg = {t: 0 for t in TOWNS}
    H = nx.Graph()
    H.add_nodes_from(TOWNS)
    chosen = []
    for (u, v), w in edges:
        if deg[u] < 2 and deg[v] < 2:
            # skip an edge that would close a cycle on fewer than all n towns
            if nx.has_path(H, u, v) and H.number_of_edges() < len(TOWNS) - 1:
                continue
            H.add_edge(u, v)
            deg[u] += 1
            deg[v] += 1
            chosen.append((u, v, w))
            if H.number_of_edges() == len(TOWNS):
                break
    return chosen, sum(w for _, _, w in chosen)


def main():
    opt_cost, opt_order = optimal_tour()
    g_edges, g_cost = greedy_tour()

    print("Costs c(ij):", {f"{u}{v}": w for (u, v), w in C.items()})
    opt_path = "-".join(opt_order) + "-" + opt_order[0]
    print(f"Optimal tour : {opt_path}  cost = {opt_cost}")
    print(f"Greedy edges : {[(u, v, w) for u, v, w in g_edges]}  "
          f"cost = {g_cost}")
    print(f"Greedy is worse: {g_cost} > {opt_cost}  "
          f"(factor {g_cost / opt_cost:.3f})")

    # The greedy CYCLE is strictly worse than optimal -- Figure 27's lesson.
    assert g_cost > opt_cost, "greedy should be strictly worse here"
    # ...yet for the cheapest TREE the very same greedy rule (Kruskal) is exact.
    G = nx.Graph()
    for (u, v), w in C.items():
        G.add_edge(u, v, weight=w)
    mst = nx.minimum_spanning_tree(G)
    print(f"For the cheapest TREE the same greedy rule is exact: "
          f"MST cost = {mst.size(weight='weight'):g}")


if __name__ == "__main__":
    main()
