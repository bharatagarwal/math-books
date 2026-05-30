# uv run python code/bradfield/10-number-theory/06_euclid_trace.py
# INTUITION (LL ch 8, sec 8.6): TRACE Euclid's algorithm step by step and
# watch the remainders shrink.  Reproduces the book's own example chains and
# checks Lemma 8.2 (the pair's product at least halves each reduction) and
# Theorem 8.7 (steps <= log2(a) + log2(b)).
import math


def trace(a, b):
    # Always reduce the LARGER by the smaller: (a,b) with a>=b becomes
    # (b, a mod b).  LL writes gcd(a,b) = gcd(b, a mod b).  Recording the
    # pair larger-first means every recorded step is a real reduction.
    if a < b:
        a, b = b, a
    steps = []
    while b:
        steps.append((a, b))
        a, b = b, a % b
    return a, steps


def show(a, b):
    g, steps = trace(a, b)
    chain = " = ".join(f"gcd({x},{y})" for x, y in steps) + f" = {g}"
    print(f"  {chain}")
    return g, steps


print("Euclid traced, watching the pair shrink to the gcd:")
# LL's own examples (sec 8.6).
g1, s1 = show(300, 18)        # gcd(300,18) = gcd(18,12) = gcd(12,6) = 6
g2, s2 = show(101, 100)       # consecutive integers -> one real step
g3, s3 = show(89, 55)         # consecutive Fibonacci -> the long chain
assert g1 == 6 and g2 == 1 and g3 == 1

# Lemma 8.2: each genuine reduction at least halves the product of the pair.
# Each recorded pair is (larger, smaller); the next pair is (smaller, a mod b),
# and a mod b < b, so the product strictly more than halves.
print()
print("Lemma 8.2 -- product of the pair at least halves each step (89,55):")
prods = [a * b for (a, b) in s3]
for i, ((a, b), prod) in enumerate(zip(s3, prods)):
    if i == 0:
        print(f"  pair ({a:2d},{b:2d})  product {prod}")
    else:
        prev = prods[i - 1]
        print(f"  pair ({a:2d},{b:2d})  product {prod}"
              f"  (was {prev}, dropped {prev / prod:.2f}x)")
        assert prod <= prev / 2 + 1e-9      # product dropped by a factor >= 2

# Theorem 8.7: steps <= log2(a) + log2(b) = log2(a*b).  This follows from
# Lemma 8.2 once there is at least one reduction; the only escape is a=b=1
# (product 1, bound 0) where the loop still runs once trivially.
print()
print("Theorem 8.7 -- steps <= log2(a) + log2(b), checked widely:")
worst = 0.0
for a in range(1, 400):
    for b in range(1, 400):
        if a == 1 and b == 1:
            continue                         # degenerate: bound is 0
        _, steps = trace(a, b)
        bound = math.log2(a) + math.log2(b)  # = log2(a*b)
        assert len(steps) <= bound + 1e-9
        worst = max(worst, len(steps) / bound)
print(f"  bound never violated; tightest ratio seen = {worst:.3f}")

# The Fibonacci pairs are the worst case (LL exercise 8.25): consecutive
# Fibonacci numbers force one extra step each time -- the algorithm is
# longest exactly here.
fib = [1, 1]
while len(fib) < 16:
    fib.append(fib[-1] + fib[-2])
print()
print("Fibonacci pairs are the worst case (steps grow by one each time):")
for k in range(2, 13):
    _, steps = trace(fib[k + 1], fib[k])
    print(f"  gcd(F{k+2}={fib[k+1]:3d}, F{k+1}={fib[k]:3d}) "
          f"takes {len(steps)} steps")
