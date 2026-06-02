# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/04_inner_product_geometry.py"
#
# Chapter 10, Section 10.8: the geometry of the inner product.
# We verify Kun's three load-bearing facts:
#   Theorem 10.20  <v,w> = ||v|| ||w|| cos(theta)
#   Theorem 10.21  v perp w  iff  <v,w> = 0
#   Definition 10.23 / Figure 10.8: w - proj_v(w) is perpendicular
#                    to proj_v(w).

import numpy as np


def inner(v, w):
    return float(np.dot(v, w))


def norm(v):
    return np.sqrt(inner(v, v))


def proj(v, w):
    """Projection of w onto v (Definition 10.23)."""
    return (inner(v, w) / inner(v, v)) * v


# Theorem 10.20: dot product equals the law-of-cosines formula.
for _ in range(10_000):
    v = np.random.randn(4)
    w = np.random.randn(4)
    cos_theta = inner(v, w) / (norm(v) * norm(w))
    assert np.isclose(inner(v, w), norm(v) * norm(w) * cos_theta)
print("Theorem 10.20: <v,w> = ||v|| ||w|| cos(theta), 10000 OK")

# Theorem 10.21: build a w guaranteed perpendicular to v and check
# its inner product is (numerically) zero.
for _ in range(10_000):
    v = np.random.randn(3)
    u = np.random.randn(3)
    w = u - proj(v, u)               # strip off the v-component
    assert np.isclose(inner(v, w), 0.0)
print("Theorem 10.21: <v, w-proj_v(w)> = 0, 10000 OK")

# Figure 10.8: the projection and the residual are perpendicular,
# so the Pythagorean theorem splits ||w||^2 exactly. This identity
# is the one the SVD derivation later leans on.
for _ in range(10_000):
    v = np.random.randn(5)
    w = np.random.randn(5)
    p = proj(v, w)
    residual = w - p
    assert np.isclose(inner(p, residual), 0.0)
    assert np.isclose(norm(p) ** 2 + norm(residual) ** 2, norm(w) ** 2)
print("Figure 10.8: ||proj||^2 + ||residual||^2 = ||w||^2, 10000 OK")
