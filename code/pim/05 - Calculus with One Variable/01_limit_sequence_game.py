# uv run python \
#   "code/pim/05 - Calculus with One Variable/01_limit_sequence_game.py"
# The epsilon-to-k game for x_n = 1 - 1/n -> 1 (Definition 8.1).
# A skeptic names a threshold eps; we must hand back an index k so
# that EVERY term after x_k stays within eps of the limit L = 1.
# The proof's recipe is k = ceil(1/eps); we check it really works.
import math


def x(n):
    return 1 - 1 / n


L = 1


def k_for(eps):
    """Index produced by the proof: any k > 1/eps suffices."""
    return math.ceil(1 / eps) + 1


for eps in [1 / 2, 1 / 4, 1 / 100, (1 / 2) ** 10]:
    k = k_for(eps)
    # Check the next 5000 terms after x_k are all within eps of L.
    worst = max(abs(x(n) - L) for n in range(k, k + 5000))
    assert worst < eps, (eps, k, worst)
    print(f"eps={eps:<12.8f} -> k={k:<6} max|x_n-1|={worst:.3e} < eps")

print("Every challenge answered: x_n converges to 1.")
