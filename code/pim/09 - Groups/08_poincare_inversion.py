# uv run --with numpy python "code/pim/09 - Groups/08_poincare_inversion.py"
"""Circle inversion and the cross ratio in the Poincare disk.

The hyperbolic reflections of Section 16.5 are inversions in circles.
Definition 16.15 fixes the inverse p' of p in a circle (center x,
radius r) by the rule d(p,x) d(p',x) = r^2, computed by the formula
    p' = x + r^2 (p - x) / ||p - x||^2.
Theorem 16.19 is the deep fact that inversion preserves the CROSS
RATIO -- the invariant Kun uses to *define* hyperbolic distance. We
verify both, numerically, on random configurations.
"""
import numpy as np

rng = np.random.default_rng(7)


def invert(p, center, r):
    """Inverse of point p in the circle (center, r). Definition 16.15."""
    d = p - center
    return center + r * r * d / (d @ d)


def cross_ratio(w, x, y, z):
    """[wx; yz] = (||w-y|| ||x-z||) / (||w-z|| ||x-y||)."""
    n = np.linalg.norm
    return (n(w - y) * n(x - z)) / (n(w - z) * n(x - y))


# 1. The defining property d(p,x) d(p',x) = r^2.
for _ in range(5000):
    center = rng.uniform(-3, 3, 2)
    r = rng.uniform(0.5, 3)
    p = center + rng.uniform(-3, 3, 2)
    if np.linalg.norm(p - center) < 1e-6:
        continue
    pp = invert(p, center, r)
    lhs = np.linalg.norm(p - center) * np.linalg.norm(pp - center)
    assert np.isclose(lhs, r * r)
print("Definition 16.15 holds: d(p,x) d(p',x) = r^2 for all tested p.")

# Inversion is an involution: inverting twice returns the point.
center, r = np.array([0.4, -0.2]), 1.3
p = np.array([0.7, 0.5])
assert np.allclose(invert(invert(p, center, r), center, r), p)
print("Inversion is its own inverse (an involution).")

# 2. Theorem 16.19: inversion preserves the cross ratio.
for _ in range(5000):
    center = rng.uniform(-2, 2, 2)
    r = rng.uniform(0.5, 2)
    pts = [center + rng.uniform(-3, 3, 2) for _ in range(4)]
    if any(np.linalg.norm(q - center) < 1e-3 for q in pts):
        continue
    before = cross_ratio(*pts)
    after = cross_ratio(*[invert(q, center, r) for q in pts])
    assert np.isclose(before, after, rtol=1e-6)
print("Theorem 16.19 holds: circle inversion preserves the cross ratio,")
print("which is exactly why it serves as a hyperbolic isometry.")
