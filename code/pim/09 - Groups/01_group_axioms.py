# uv run python "code/pim/09 - Groups/01_group_axioms.py"
"""Verify Definition 16.3 (the group axioms) for Z/nZ under +.

Kun frames a group as an *interface*: a set with a binary operation
satisfying identity, inverses, and associativity. Here we implement
that interface for Z/nZ and exhaustively check every axiom -- the
"unit test" Kun says you must write the instant you read a definition.
"""


def check_group(elements, op, identity):
    """Return True iff (elements, op) satisfies the group axioms,
    with `identity` as the claimed identity element."""
    s = set(elements)

    # Closure: a . b stays inside the set (required for op: G x G -> G).
    for a in s:
        for b in s:
            if op(a, b) not in s:
                return False

    # Identity: e . x == x and x . e == x for all x.
    for x in s:
        if op(identity, x) != x or op(x, identity) != x:
            return False

    # Inverses: every x has some y with x . y == e and y . x == e.
    for x in s:
        if not any(op(x, y) == identity and op(y, x) == identity
                   for y in s):
            return False

    # Associativity: x . (y . z) == (x . y) . z.
    for x in s:
        for y in s:
            for z in s:
                if op(x, op(y, z)) != op(op(x, y), z):
                    return False

    return True


def zmod_add(n):
    return lambda a, b: (a + b) % n


for n in (1, 2, 3, 4, 5, 6, 7, 8):
    elems = list(range(n))
    assert check_group(elems, zmod_add(n), 0), f"Z/{n}Z failed"
    print(f"Z/{n}Z under + is a group (identity 0).")

# A non-example: Z/6Z under multiplication is NOT a group --
# 0, 2, 3, 4 have no multiplicative inverse mod 6.
mult6 = lambda a, b: (a * b) % 6
assert not check_group(range(6), mult6, 1), "Z/6Z* should fail"
print("Z/6Z under * is NOT a group (some elements lack inverses).")

# Removing the non-units leaves (Z/6Z)^x = {1, 5}, which IS a group.
assert check_group([1, 5], mult6, 1), "(Z/6Z)^x failed"
print("(Z/6Z)^x = {1, 5} under * is a group (identity 1).")
