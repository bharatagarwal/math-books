# uv run --with numpy python
# Matrix operations in NumPy: multiplication, determinant,
# inverse, eigenvalues, trace, rank — each notation symbol
# maps to a NumPy call.
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A =")
print(A)
print()

# Matrix multiplication: AB  (the @ operator)
print(f"AB =\n{A @ B}\n")
# AB =
# [[19 22]
#  [43 50]]

# Transpose: Aᵀ
print(f"Aᵀ =\n{A.T}\n")
# Aᵀ =
# [[1 3]
#  [2 4]]

# Determinant: det(A)
det_A = np.linalg.det(A)
print(f"det(A) = {det_A:.1f}")
# det(A) = -2.0

# Inverse: A⁻¹  (exists because det ≠ 0)
A_inv = np.linalg.inv(A)
print(f"A⁻¹ =\n{A_inv}\n")
# A⁻¹ =
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Verify: A · A⁻¹ = I
print(f"A @ A⁻¹ ≈ I? "
      f"{np.allclose(A @ A_inv, np.eye(2))}\n")
# A @ A⁻¹ ≈ I? True

# Identity matrix: I₃
print(f"I₃ =\n{np.eye(3).astype(int)}\n")
# I₃ =
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

# Trace: tr(A) = sum of diagonal
print(f"tr(A) = {np.trace(A)}")
# tr(A) = 5

# Rank
print(f"rank(A) = {np.linalg.matrix_rank(A)}")
# rank(A) = 2

# Eigenvalues & eigenvectors: Ax = λx
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\nEigenvalues  λ = {eigenvalues}")
# λ ≈ [-0.3723, 5.3723]
print(f"Eigenvectors:\n{eigenvectors}\n")

# Verify Av = λv for first eigenvalue
lam, v = eigenvalues[0], eigenvectors[:, 0]
print(f"Av  = {A @ v}")
print(f"λv  = {lam * v}")
print(f"Av ≈ λv? {np.allclose(A @ v, lam * v)}")
# True

# Singular values: σ
U, sigma, Vt = np.linalg.svd(A)
print(f"\nSingular values σ = "
      f"{np.round(sigma, 4)}")
# σ ≈ [5.465, 0.366]

# Frobenius norm: ‖A‖_F
print(f"‖A‖_F = {np.linalg.norm(A, 'fro'):.4f}")
# ‖A‖_F = 5.4772

# Condition number: κ(A) = σ_max / σ_min
print(f"κ(A)  = {np.linalg.cond(A):.4f}")
# κ(A)  ≈ 14.9330
