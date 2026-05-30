# uv run --with sympy python
#
# Exact combinatorial probabilities behind the Law of Large Numbers (DM 7.3).
#
# The book derives P(A_k) = C(n, k) / 2^n for the event A_k = "exactly k heads"
# in n independent fair coin tosses, and Theorem 7.1 bounds the probability that
# the head count is < m - t or > m + t (for n = 2m) by at most m / t^2.
#
# Everything here is EXACT rational arithmetic (sympy), so we can confirm the
# book's identities to the last digit rather than approximately:
#   * P(A_k) = C(2m, k) / 2^(2m), and the P(A_k) sum to 1 (probability axiom b).
#   * The exact tail probability is genuinely <= m / t^2 (Theorem 7.1).

import sympy as sp


def head_count_prob(n, k):
    """Exact P(exactly k heads in n fair tosses) = C(n,k)/2^n.

    This is the book's formula for P(A_k).
    """
    return sp.Rational(sp.binomial(n, k), 2**n)


def tail_prob(m, t):
    """Exact P(#heads < m - t  OR  #heads > m + t) for n = 2m fair tosses."""
    n = 2 * m
    total = sp.Integer(0)
    for k in range(0, n + 1):
        if k < m - t or k > m + t:
            total += sp.binomial(n, k)
    return sp.Rational(total, 2**n)


# --- P(A_k) sums to 1 (axiom (b): the P(s_i) sum to 1) -----------------------
for n in [2, 20, 100]:
    s = sum(head_count_prob(n, k) for k in range(n + 1))
    print(f"sum_k P(A_k) for n={n:>3}:  {s}   (== 1: {s == 1})")

# --- Theorem 7.1: exact tail probability <= m / t^2 --------------------------
print()
print("Theorem 7.1: P(#heads outside [m-t, m+t]) <= m / t^2")
print(f"{'m':>5} {'t':>5} {'exact tail prob':>22} {'~decimal':>12} "
      f"{'bound m/t^2':>14} {'<= bound':>9}")
for m, t in [(50, 20), (100, 30), (200, 50), (500, 80)]:
    exact = tail_prob(m, t)
    bound = sp.Rational(m, t**2)
    holds = exact <= bound
    print(f"{m:>5} {t:>5} {str(exact):>22} {float(exact):>12.6f} "
          f"{float(bound):>14.6f} {str(holds):>9}")

# --- The book's two worked numbers, reproduced exactly -----------------------
# Single fair coin tossed twice: P(HH) = C(2,2)/2^2 = 1/4.
print()
print(f"P(exactly 2 heads in 2 tosses) = {head_count_prob(2, 2)}  "
      f"(book: each of HH,HT,TH,TT has prob 1/4)")
# Corollary scale: at m = 1,000,000, t = 10*sqrt(m) = 10000,
# the bound is m/t^2 = 1/100.
m, t = 1_000_000, 10_000
bound = sp.Rational(m, t**2)
print(f"Corollary 7.1 bound at m={m:,}, t=10*sqrt(m)={t:,}:  "
      f"m/t^2 = {bound}  => P(inside band) >= {1 - bound}")
