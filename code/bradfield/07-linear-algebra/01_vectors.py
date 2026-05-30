# uv run --with numpy python \
#   "code/bradfield/07-linear-algebra/01_vectors.py"
# 3Blue1Brown, Essence of Linear Algebra, ch 1 (Vectors).
# A vector is an arrow from the origin; the two fundamental
# operations are addition (tip-to-tail) and scaling.
import numpy as np

v = np.array([1.0, 2.0])
w = np.array([3.0, -1.0])

# Addition is tip-to-tail: walk along v, then along w.
# Componentwise, that is just adding coordinates.
assert np.array_equal(v + w, np.array([4.0, 1.0]))

# Scaling stretches/squishes (and flips, if negative).
assert np.array_equal(2 * v, np.array([2.0, 4.0]))
assert np.array_equal(-1 * v, np.array([-1.0, -2.0]))

# Every vector is a linear combination of the basis
# vectors i-hat = (1,0) and j-hat = (0,1):
#   (x, y) = x * i-hat + y * j-hat.
ihat = np.array([1.0, 0.0])
jhat = np.array([0.0, 1.0])
x, y = v
assert np.array_equal(x * ihat + y * jhat, v)

print("v + w        =", v + w)
print("2 * v        =", 2 * v)
print("x*ihat+y*jhat =", x * ihat + y * jhat, "(== v)")
print("all vector identities hold")
