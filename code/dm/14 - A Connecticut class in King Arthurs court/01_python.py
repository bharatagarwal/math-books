# uv run --with networkx python
#
# The MARRIAGE problem (the chapter's first tale).
#
# 150 knights and 150 ladies. Some pairs refuse to marry. King Arthur wants a
# PERFECT MATCHING in the bipartite "willing-to-marry" graph; Merlin proves none
# exists by parading "a certain 56 ladies" whose only acceptable husbands number
# just 55 knights -- by the pigeon-hole principle you cannot give 56 ladies
# distinct husbands out of 55 men. This is the easily CHECKABLE certificate of
# NON-existence (a Hall / Frobenius violating set X with |N(X)| < |X|).
#
# We build a concrete willing-to-marry graph that embeds exactly such a 56->55
# bottleneck, run Hopcroft-Karp maximum bipartite matching to confirm there is
# NO perfect matching, then independently exhibit and verify the 56-vs-55
# certificate -- reproducing the book's exact numbers.

import networkx as nx

n = 150
ladies = [("L", i) for i in range(n)]
knights = [("K", j) for j in range(n)]

G = nx.Graph()
G.add_nodes_from(ladies, bipartite=0)
G.add_nodes_from(knights, bipartite=1)

# Engineer the bottleneck exactly as Merlin describes it:
#   - 56 specific ladies (the "deficient set" X) are only willing to marry
#     among a pool of just 55 knights.  => |N(X)| = 55 < 56 = |X|.
deficient_ladies = ladies[:56]          # the 56 ladies Merlin lines up
allowed_knights = knights[:55]          # the only 55 men any of them accept
for lady in deficient_ladies:
    for kn in allowed_knights:
        G.add_edge(lady, kn)

# Everyone else marries freely (dense edges) so the ONLY obstruction is the
# 56->55 bottleneck, not some incidental shortage elsewhere.
for lady in ladies[56:]:
    for kn in knights:                  # the remaining 94 ladies accept anyone
        G.add_edge(lady, kn)

# Maximum bipartite matching: if it covered all 300 people it would be perfect.
M = nx.bipartite.hopcroft_karp_matching(G, top_nodes=ladies)
matched_pairs = len(M) // 2
print("maximum matching size:", matched_pairs,
      "pairs (need 150 for a wedding-all plan)")
assert matched_pairs < n, "there must be NO perfect matching"
print("=> NO perfect matching exists: at least one lady is left "
      "without a husband.")

# Now the certificate Merlin shows the King -- and verify it ourselves.
X = set(deficient_ladies)
neighbors = set()
for lady in X:
    neighbors.update(G.neighbors(lady))
print(f"Merlin's set X: |X| = {len(X)} ladies")
print(f"their combined suitors N(X): |N(X)| = {len(neighbors)} knights")
assert len(X) == 56 and len(neighbors) == 55
assert len(neighbors) < len(X), "Hall's condition is violated: |N(X)| < |X|"
print("Pigeon-hole: 56 ladies cannot get 56 distinct husbands from 55 knights.")
print("This violating set is the EASILY-CHECKED proof that no perfect matching")
print("exists -- so non-matching is itself an NP-property "
      "(Frobenius' theorem).")
