# uv run --with numpy python \
#   "code/bradfield/07-linear-algebra/02_span.py"
# 3Blue1Brown, Essence of Linear Algebra, ch 2 (Linear
# combinations, span, basis). INTUITION DEMO: don't assert a
# result -- DISCOVER span by sweeping the scalars a, b over a
# grid and watching which points a*v + b*w can reach.
import numpy as np


def reaches(v, w, samples):
    """Set of points a*v + b*w for a,b in `samples`."""
    pts = set()
    for a in samples:
        for b in samples:
            p = a * v + b * w
            pts.add((round(p[0], 6), round(p[1], 6)))
    return pts


samples = np.linspace(-2, 2, 9)

# Case 1: two vectors pointing in different directions.
# Their combinations fill out the whole plane -> span = R^2.
v1, w1 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
plane = reaches(v1, w1, samples)
print("independent v,w: reach", len(plane), "distinct points")
print("  e.g.", sorted(plane)[:3], "... a full 2D grid")

# Case 2: w is just a scaled copy of v (linearly dependent).
# Now every combination lands on a single line -> span is 1D.
v2, w2 = np.array([1.0, 1.0]), np.array([2.0, 2.0])
line = reaches(v2, w2, samples)
on_line = all(abs(px - py) < 1e-9 for px, py in line)
print("dependent v,w:   reach", len(line), "points,",
      "all on the line y = x:", on_line)

# The difference IS the definition of linear (in)dependence:
# w adds a new direction (case 1) or it doesn't (case 2).
assert len(plane) > len(line)
assert on_line
print("span collapses from a plane to a line when w is "
      "redundant")
