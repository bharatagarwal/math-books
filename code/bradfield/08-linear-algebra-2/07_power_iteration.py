# uv run --with numpy python \
#   code/bradfield/08-linear-algebra-2/07_power_iteration.py
#
# INTUITION DEMO: how power iteration FINDS the dominant
# eigenvector. Start from an arbitrary direction and apply A
# over and over, renormalizing each step. The component along
# the biggest-|lambda| eigenvector grows fastest, so the vector
# swings toward that eigendirection -- we print the angle to it
# collapsing toward 0, and the Rayleigh quotient homing in on
# the dominant eigenvalue. This is the engine under PageRank.
import numpy as np

A = np.array([[2.0, 1.0], [1.0, 2.0]])
vals, vecs = np.linalg.eig(A)
top = int(np.argmax(np.abs(vals)))
lam, target = vals[top], vecs[:, top]
print(f"dominant eigenvalue = {lam:.1f}, "
      f"eigenvector = {np.round(target, 3)}\n")


def angle_to(v, t):
    c = abs(v @ t) / (np.linalg.norm(v) * np.linalg.norm(t))
    return np.degrees(np.arccos(min(1.0, c)))


v = np.array([1.0, 0.0])  # start nowhere near the eigenvector
print(" step  vector              angle->v   Rayleigh")
prev_angle = None
for step in range(7):
    rayleigh = (v @ (A @ v)) / (v @ v)
    ang = angle_to(v, target)
    if prev_angle is not None:
        assert ang <= prev_angle + 1e-9  # angle never grows
    prev_angle = ang
    print(f"  {step:2d}  {np.round(v, 4)!s:>18}  {ang:7.3f}  "
          f"{rayleigh:8.4f}")
    w = A @ v
    v = w / np.linalg.norm(w)

# A few more silent steps to drive it home to full convergence.
for _ in range(30):
    w = A @ v
    v = w / np.linalg.norm(w)

assert angle_to(v, target) < 1e-6   # aligned with eigenvector
assert abs((v @ (A @ v)) / (v @ v) - lam) < 1e-6  # found lambda
print("\nconverged: aligned with the dominant eigenvector,")
print("Rayleigh quotient -> the dominant eigenvalue")
