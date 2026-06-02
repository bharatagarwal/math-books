# uv run --with numpy python "code/pim/08 - Multivariable Calculus and Optimization/03_steepest_ascent.py"
#
# Theorem 14.13: the gradient points in the direction of steepest ascent.
# We check it the brute-force way: the directional derivative Dir(f,c,v)
# = <grad f(c), v> is maximized over all unit vectors v exactly when v
# is the normalized gradient.  We sweep every direction and confirm.
import numpy as np


def f(p):
    x, y = p
    return np.sin(x) + 0.5 * y ** 2 + x * y


def grad_f(p):
    x, y = p
    return np.array([np.cos(x) + y, y + x])


c = np.array([0.7, -0.4])
g = grad_f(c)
g_hat = g / np.linalg.norm(g)

# Sweep 100k unit directions; track the steepest one found.
thetas = np.linspace(0, 2 * np.pi, 100_000, endpoint=False)
best_theta, best_slope = None, -np.inf
for t in thetas:
    v = np.array([np.cos(t), np.sin(t)])
    slope = g @ v          # directional derivative = <grad, v>
    if slope > best_slope:
        best_slope, best_theta = slope, t

v_best = np.array([np.cos(best_theta), np.sin(best_theta)])

# The steepest direction found should equal the normalized gradient,
# and its slope should equal ||grad f|| (Cauchy-Schwarz with equality).
print("normalized gradient :", np.round(g_hat, 4))
print("steepest direction  :", np.round(v_best, 4))
print("max slope found     :", round(best_slope, 6))
print("||grad f||          :", round(np.linalg.norm(g), 6))

assert np.allclose(v_best, g_hat, atol=1e-3)
assert abs(best_slope - np.linalg.norm(g)) < 1e-3
print("Steepest ascent IS the gradient direction (Theorem 14.13).")
