def implies(p, q):
    """P ⇒ Q is False only when P is True and Q is False."""
    return not p or q

def iff(p, q):
    """P ⇔ Q is True when P and Q have the same truth value."""
    return p == q

print("P\tQ\tP⇒Q\tP⇔Q")
for p in [True, False]:
    for q in [True, False]:
        print(f"{p}\t{q}\t{implies(p, q)}\t{iff(p, q)}")
