# uv run --with numpy python code/bradfield/02-probability/04_variance_independence.py
# Independence, variance, and when variances add.
from itertools import product
from fractions import Fraction
import numpy as np

omega = list(product(range(1, 7), repeat=2))      # two fair dice
P = Fraction(1, 36)

def E(f):
    return sum(Fraction(f(o)) * P for o in omega)

X = lambda o: o[0]          # first die
Y = lambda o: o[1]          # second die

# Independence check: P(X=a and Y=b) == P(X=a) * P(Y=b) for all a, b.
def joint(a, b):
    return Fraction(sum(1 for o in omega if o[0] == a and o[1] == b), 36)
def marg_x(a):
    return Fraction(sum(1 for o in omega if o[0] == a), 36)
assert all(joint(a, b) == marg_x(a) * marg_x(b)
           for a in range(1, 7) for b in range(1, 7))

# Var(X) = E[X^2] - E[X]^2. For one die this is 35/12.
varX = E(lambda o: X(o) ** 2) - E(X) ** 2
assert varX == Fraction(35, 12)

# Because X and Y are independent, Var(X+Y) = Var(X) + Var(Y).
varXY = E(lambda o: (X(o) + Y(o)) ** 2) - E(lambda o: X(o) + Y(o)) ** 2
assert varXY == varX + varX == Fraction(35, 6)

# Sanity-check the variance numerically too.
rng = np.random.default_rng(3)
s = rng.integers(1, 7, size=(2, 500_000)).sum(axis=0)
assert abs(s.var() - float(varXY)) < 0.05

print("Var(one die) =", varX, " Var(sum of two) =", varXY,
      "(independent, so they add)")
