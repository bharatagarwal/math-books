# uv run --with sympy python code/bradfield/02-probability/05_binomial_distribution.py
# LL 7.1-7.2: probability is counting with a denominator, and repeated trials
# give the BINOMIAL distribution. We reproduce the book's two headline numbers.
import sympy as sp

# LL 7.1: toss a fair coin 100 times. P(exactly 50 heads) = C(100,50)/2^100.
# The book says "about 0.08" -- and notes how SMALL that is for the single most
# likely count. Exact rational, then a float to compare with the book.
p50 = sp.Rational(sp.binomial(100, 50), 2**100)
assert abs(float(p50) - 0.0796) < 1e-3            # ~8%, matches LL

# LL 7.2: roll a die 10 times. P(exactly 3 sixes). Favorable = choose which 3
# rolls are sixes, times 5^7 for the rest; over 6^10 total.
p3 = sp.Rational(sp.binomial(10, 3) * 5**7, 6**10)
# Same thing in the book's tidy form  C(10,3) (1/6)^3 (5/6)^7:
assert p3 == sp.binomial(10, 3) * sp.Rational(1, 6)**3 * sp.Rational(5, 6)**7

# The general law: in n independent trials each succeeding with prob p,
# P(exactly k successes) = C(n,k) p^k (1-p)^(n-k). The whole distribution must
# sum to 1 -- and it does, because these are the binomial-theorem terms of
# (p + (1-p))^n = 1^n. Check it symbolically for several n.
p = sp.Symbol("p")
for n in range(1, 8):
    total = sum(sp.binomial(n, k) * p**k * (1 - p)**(n - k) for k in range(n + 1))
    assert sp.simplify(total) == 1

print("P(exactly 50 heads in 100 tosses) =", round(float(p50), 4), "(~8%, per LL)")
print("P(exactly 3 sixes in 10 rolls)    =", round(float(p3), 4))
print("binomial probs sum to 1 for n = 1..7 (binomial theorem)")
