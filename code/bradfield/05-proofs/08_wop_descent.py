# uv run --with sympy python code/bradfield/05-proofs/08_wop_descent.py
import sympy as sp

# INTUITION DEMO (MCS ch 2): the Well Ordering Principle proof of sqrt(2)
# irrational works by DESCENT. If some positive integer m has m*sqrt(2)
# an integer, then m' = m*(sqrt(2) - 1) is a SMALLER positive integer
# with the same property -- impossible if m was the least. We watch the
# descent strictly shrink, which is why no such m can exist.

r2 = sp.sqrt(2)

# Pretend (falsely) sqrt(2) = a/b; then m = b makes m*sqrt(2)= a an int.
# Use the best rational approximations to sqrt(2) to play the role of m,
# and show m' = m*(sqrt(2)-1) is always smaller and positive.
print(" m (claimed)   m' = m*(sqrt2 - 1)   smaller & positive?")
m = sp.Integer(1000)
for _ in range(6):
    m_prime = m * (r2 - 1)
    val = float(m_prime)
    ok = 0 < val < float(m)
    print(f"   {str(m):>6}        {val:12.4f}              {ok}")
    assert 0 < val < float(m)        # strictly descends, stays positive
    m = sp.Integer(int(val))         # next claimed integer, strictly less
    if m <= 0:
        break

print("\nthe sequence strictly decreases yet stays positive --")
print("an infinite descent in the positive integers is impossible,")
print("so no least m exists, so sqrt(2) is not a ratio of integers")

# The factor sqrt(2) - 1 is what guarantees the shrink: 0 < it < 1.
assert 0 < float(r2 - 1) < 1
print(f"\nkey: 0 < sqrt(2) - 1 = {float(r2 - 1):.4f} < 1  drives the descent")
