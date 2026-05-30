# uv run python code/bradfield/06-induction/05_structural_trees.py
# Intuition + verification for STRUCTURAL induction on a recursive data
# type. A full binary tree is defined recursively:
#   Tree = Leaf | Node(Tree, Tree)
# Conjecture: in any such tree, #leaves = #internal-nodes + 1.
# We first DISCOVER the pattern by building random trees and printing
# the two counts side by side, then state the structural-induction proof
# (base: a Leaf has 1 leaf, 0 internal; step: a Node combines two
# subtrees, adding one internal node and merging their leaf counts).
import random

Leaf = "leaf"  # base constructor


def node(left, right):
    return ("node", left, right)  # constructor rule


def random_tree(depth, rng):
    """Build a random full binary tree of bounded depth."""
    if depth == 0 or rng.random() < 0.3:
        return Leaf
    return node(random_tree(depth - 1, rng),
                random_tree(depth - 1, rng))


def count_leaves(t):
    if t == Leaf:
        return 1
    return count_leaves(t[1]) + count_leaves(t[2])


def count_internal(t):
    if t == Leaf:
        return 0
    return 1 + count_internal(t[1]) + count_internal(t[2])


def main():
    rng = random.Random(42)
    print(f"{'leaves':>7} {'internal':>9}  leaves == internal + 1 ?")
    for _ in range(8):
        t = random_tree(4, rng)
        L, I = count_leaves(t), count_internal(t)
        print(f"{L:>7} {I:>9}  {L == I + 1}")
    # Now make it a real check across many random shapes.
    for _ in range(5000):
        t = random_tree(6, rng)
        assert count_leaves(t) == count_internal(t) + 1
    print("structural invariant holds for 5000 random trees")


if __name__ == "__main__":
    main()
