# uv run --with numpy python "code/pim/09 - Groups/09_fundamental_triangle.py"
"""Compute the fundamental triangle of a [p, q] hyperbolic tessellation.

Section 16.7 derives (Lemma 16.26) the vertices A, B, D of the
fundamental triangle, with hyperbolic angles pi/p, pi/q, pi/2. A is
the origin, D is on the x-axis, and B sits on the line y = tan(pi/p) x.
The hyperbolic edge B-D is an arc of a circle (center G on the x-axis)
orthogonal to the unit disk. We run Kun's formulas, then CHECK the
construction: the circle through B,D is orthogonal to the unit circle,
and the three interior angles come out to pi/p, pi/q, pi/2.
"""
import math
import numpy as np


def fundamental_triangle(p, q):
    assert (p - 2) * (q - 2) > 4, "[p,q] must be hyperbolic"
    tan_p = math.tan(math.pi / p)
    Z = math.tan(math.pi / p + math.pi / q) * tan_p
    b_x = math.sqrt(1 / (1 + 2 * Z - tan_p ** 2))
    b_y = b_x * tan_p
    g_x = b_x * (Z + 1)
    r = math.sqrt(b_y ** 2 + (b_x - g_x) ** 2)
    d_x = g_x - r
    A = np.array([0.0, 0.0])
    B = np.array([b_x, b_y])
    D = np.array([d_x, 0.0])
    G = np.array([g_x, 0.0])
    return A, B, D, G, r


def angle_at(vertex, p1, p2):
    """Euclidean angle at `vertex` between rays to p1 and p2."""
    u = (p1 - vertex) / np.linalg.norm(p1 - vertex)
    v = (p2 - vertex) / np.linalg.norm(p2 - vertex)
    return math.acos(np.clip(u @ v, -1, 1))


def tangent_dir(center, point):
    """Unit tangent to a circle (perp to the radius) at `point`."""
    radial = point - center
    t = np.array([-radial[1], radial[0]])
    return t / np.linalg.norm(t)


for p, q in [(7, 3), (6, 4), (5, 5), (8, 3)]:
    A, B, D, G, r = fundamental_triangle(p, q)

    # Edge B-D is an arc orthogonal to the unit circle:
    # orthogonality <=> g_x^2 = 1 + r^2 (Pythagoras on the two radii).
    assert np.isclose(G[0] ** 2, 1 + r * r), "not orthogonal to disk"

    # Angle at A = pi/p (between x-axis edge A-D and edge A-B).
    ang_A = angle_at(A, D, B)
    # Angle at D = pi/2: between x-axis and the tangent to arc B-D at D.
    ang_D = angle_at(D, A, D + tangent_dir(G, D))
    # Angle at B = pi/q: between edge B-A and the tangent to arc at B.
    ang_B = angle_at(B, A, B + tangent_dir(G, B))

    assert np.isclose(ang_A, math.pi / p, atol=1e-9)
    assert np.isclose(ang_D, math.pi / 2, atol=1e-9)
    assert np.isclose(ang_B, math.pi / q, atol=1e-9)
    print(f"[{p},{q}]: angles = pi/{p}, pi/2, pi/{q}  "
          f"(B=({B[0]:.3f},{B[1]:.3f}), D=({D[0]:.3f},0)). OK")

print("Lemma 16.26 verified: the fundamental triangle has the angles")
print("pi/p, pi/q, pi/2 demanded by Definition 16.25.")
