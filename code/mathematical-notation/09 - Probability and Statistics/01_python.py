# uv run --with sympy python
# Probability notation → SymPy code.
# X ~ N(mu, sigma^2) → Normal('X', mu, sigma)
# E(X) → E(X), Var(X) → variance(X), etc.
from sympy.stats import Normal, E, variance, density
from sympy.stats import P as Prob
from sympy import symbols, sqrt, simplify, oo, pprint

mu, sigma = symbols('mu sigma', positive=True)

# Declare X ~ N(mu, sigma^2)
X = Normal('X', mu, sigma)

# E(X) = mu
ex = E(X)
print(f"E(X)   = {ex}")

# Var(X) = sigma^2
vx = simplify(variance(X))
print(f"Var(X) = {vx}")

# Standard deviation: sqrt(Var(X)) = sigma
print(f"SD(X)  = {sqrt(vx)}")

print()

# Concrete example: X ~ N(100, 15^2)  (IQ scores)
Y = Normal('Y', 100, 15)
print(f"E(Y)   = {E(Y)}")
print(f"Var(Y) = {variance(Y)}")

# P(Y > 130)  — two std devs above the mean
p_above_130 = Prob(Y > 130)
print(f"P(Y > 130) = {simplify(p_above_130)}")
print(f"          ≈ {float(p_above_130):.6f}")
# E(X)   = mu
# Var(X) = sigma**2
# SD(X)  = sigma
#
# E(Y)   = 100
# Var(Y) = 225
# P(Y > 130) = 1/2 - erf(sqrt(2))/2
#           ≈ 0.022750
