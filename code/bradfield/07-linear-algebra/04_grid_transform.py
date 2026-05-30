# uv run --with numpy python \
#   "code/bradfield/07-linear-algebra/04_grid_transform.py"
# 3Blue1Brown, Essence of Linear Algebra, ch 3 & 4.
# INTUITION DEMO: literally watch a grid of points move under
# a transform, then watch matrix multiplication ACT as the
# composition of two transforms.
import numpy as np

# A small integer grid of sample points.
grid = np.array([[x, y]
                 for x in range(-1, 2)
                 for y in range(-1, 2)], dtype=float).T  # 2xN

shear = np.array([[1.0, 1.0],
                  [0.0, 1.0]])
rot = np.array([[0.0, -1.0],
                [1.0,  0.0]])  # 90 deg CCW

print("point      -> shear        -> then rotate")
for col in grid.T[:5]:
    after_shear = shear @ col
    after_both = rot @ after_shear
    print(f"({col[0]:+.0f},{col[1]:+.0f})    "
          f"({after_shear[0]:+.0f},{after_shear[1]:+.0f})"
          f"        ({after_both[0]:+.0f},{after_both[1]:+.0f})")

# Matrix multiplication IS composition: first apply the right
# matrix, then the left. (rot @ shear) does both at once.
composed = rot @ shear
two_step = rot @ (shear @ grid)
one_step = composed @ grid
assert np.allclose(one_step, two_step)
print("composed matrix rot @ shear =")
print(composed)

# Composition is NOT commutative: order of transforms matters.
assert not np.allclose(rot @ shear, shear @ rot)
print("rot@shear != shear@rot  -> order of transforms matters")
