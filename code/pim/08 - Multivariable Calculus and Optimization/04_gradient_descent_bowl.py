# uv run --with numpy python "code/pim/08 - Multivariable Calculus and Optimization/04_gradient_descent_bowl.py"
#
# Gradient descent (Section 14.7) on a 2D bowl.  Kun's loop:
#   start at random x0; while ||grad f(x)|| > eps: x <- x - eta * grad f(x)
# We minimize the tilted bowl  f(x, y) = 2(x-3)^2 + (y+1)^2 + x*y,
# whose unique minimum we can also solve for exactly to check against.
import numpy as np


def f(p):
    x, y = p
    return 2 * (x - 3) ** 2 + (y + 1) ** 2 + x * y


def grad_f(p):
    x, y = p
    return np.array([4 * (x - 3) + y, 2 * (y + 1) + x])


# Exact minimizer: solve grad f = 0  =>  [[4,1],[1,2]] p = [12, -2].
A = np.array([[4.0, 1.0], [1.0, 2.0]])
b = np.array([12.0, -2.0])
exact = np.linalg.solve(A, b)

rng = np.random.default_rng(0)
x = rng.uniform(-5, 5, size=2)
eta, eps = 0.05, 1e-8
start = x.copy()
steps = 0
while np.linalg.norm(grad_f(x)) > eps and steps < 100_000:
    x = x - eta * grad_f(x)
    steps += 1

print(f"start    = {np.round(start, 4)},  f = {f(start):.4f}")
print(f"descent  = {np.round(x, 6)},  f = {f(x):.6f}  ({steps} steps)")
print(f"exact    = {np.round(exact, 6)},  f = {f(exact):.6f}")

# Each step strictly decreased f, and we landed on the true minimum.
assert np.allclose(x, exact, atol=1e-4)
assert f(x) <= f(start)
print("Gradient descent converged to the exact minimum.")
