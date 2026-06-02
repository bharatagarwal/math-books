# uv run --with networkx --with scipy python \
#   "code/pim/04 - Graphs/05_euler_formula.py"
"""Theorem 6.5 (Euler's formula): for a connected planar graph,
V - E + F = 2.

networkx can both test planarity and hand back a combinatorial
embedding.  From the embedding we count faces by walking each
directed edge around its face (the "traverse_face" routine), then
check V - E + F = 2 -- the invariant that does not depend on how
the graph is drawn.
"""
import networkx as nx


def count_faces(embedding):
    """Count faces of a planar embedding by tracing face cycles."""
    seen = set()
    faces = 0
    for u, v in embedding.edges():       # each directed half-edge
        if (u, v) in seen:
            continue
        face = embedding.traverse_face(u, v, mark_half_edges=seen)
        faces += 1
        _ = face
    return faces


def euler(G):
    ok, emb = nx.check_planarity(G)
    assert ok, "graph is not planar"
    V = G.number_of_nodes()
    E = G.number_of_edges()
    F = count_faces(emb)
    return V, E, F


graphs = {
    "triangle K3": nx.complete_graph(3),
    "K4 (planar)": nx.complete_graph(4),
    "cube Q3": nx.hypercube_graph(3),
    "Petersen-minus-edge": None,   # filled below; Petersen itself
}
# The Petersen graph is NOT planar, so use a planar cousin instead:
del graphs["Petersen-minus-edge"]
graphs["wheel W6"] = nx.wheel_graph(6)
graphs["icosahedron"] = nx.icosahedral_graph()

for name, G in graphs.items():
    V, E, F = euler(G)
    assert V - E + F == 2, (name, V, E, F)
    print(f"{name:>16}: V={V:2d}, E={E:2d}, F={F:2d}, "
          f"V-E+F = {V - E + F}")

print("\nEvery connected planar graph gives V - E + F = 2.")
