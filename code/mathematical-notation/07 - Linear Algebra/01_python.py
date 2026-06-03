# uv run --with numpy python
# Vectors in NumPy: every notation symbol has a direct
# NumPy equivalent.
import numpy as np

# A vector x ∈ R³ — NumPy arrays ARE vectors
x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, 5.0, 6.0])

# Sum: x + y
print(f"x + y = {x + y}")
# x + y = [5. 7. 9.]

# Scalar multiple: 3x
print(f"3x    = {3 * x}")
# 3x    = [3. 6. 9.]

# Magnitude (Euclidean norm): ‖x‖
print(f"‖x‖   = {np.linalg.norm(x):.4f}")
# ‖x‖   = 3.7417

# p-norms: ‖x‖₁, ‖x‖₂, ‖x‖∞
print(f"‖x‖₁  = {np.linalg.norm(x, 1)}")
# ‖x‖₁  = 6.0
print(f"‖x‖₂  = {np.linalg.norm(x, 2):.4f}")
# ‖x‖₂  = 3.7417
print(f"‖x‖∞  = {np.linalg.norm(x, np.inf)}")
# ‖x‖∞  = 3.0

# Dot product: x · y  (three equivalent ways)
print(f"x · y  = {np.dot(x, y)}")
# x · y  = 32.0
print(f"x @ y  = {x @ y}")
# x @ y  = 32.0
print(f"⟨x,y⟩  = {np.inner(x, y)}")
# ⟨x,y⟩  = 32.0

# Angle between x and y: cos θ = (x·y)/(‖x‖‖y‖)
cos_theta = (x @ y) / (
    np.linalg.norm(x) * np.linalg.norm(y)
)
theta_deg = np.degrees(np.arccos(cos_theta))
print(f"angle  = {theta_deg:.2f}°")
# angle  = 12.93°

# Orthogonality check: x ⊥ y iff x·y = 0
a = np.array([1.0, 0.0])
b = np.array([0.0, 1.0])
print(f"a ⊥ b? {np.isclose(a @ b, 0)}")
# a ⊥ b? True

# Unit vector (hat): û = u / ‖u‖
u_hat = x / np.linalg.norm(x)
print(f"x̂      = {np.round(u_hat, 4)}")
# x̂      = [0.2673 0.5345 0.8018]
print(f"‖x̂‖    = {np.linalg.norm(u_hat):.1f}")
# ‖x̂‖    = 1.0

# Cross product (R³ only): v × w
v = np.array([1.0, 0.0, 0.0])
w = np.array([0.0, 1.0, 0.0])
print(f"v × w  = {np.cross(v, w)}")
# v × w  = [0. 0. 1.]
