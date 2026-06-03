# uv run --with jax python
# JAX automatic differentiation: grad computes ∇f.
# Notation → code: ∇f → grad(f), d²f/dx² → grad(grad(f))
import jax
import jax.numpy as jnp

# --- Scalar derivative: d/dx [x³] at x=2 → 12.0 ---
f = lambda x: x**3
dfdx = jax.grad(f)
print(f"d/dx [x³] at x=2: {dfdx(2.0)}")
# 12.0  (= 3·2² = 12)

# Second derivative: d²/dx² [x³] at x=2 → 12.0
d2fdx2 = jax.grad(jax.grad(f))
print(f"d²/dx² [x³] at x=2: {d2fdx2(2.0)}")
# 12.0  (= 6·2 = 12)

# --- Gradient: ∇f for f(x,y) = x³ + 2xy + y² ---
# ∂f/∂x = 3x² + 2y, ∂f/∂y = 2x + 2y
# At (1,2): ∇f = [3+4, 2+4] = [7, 6]
g = lambda v: v[0]**3 + 2*v[0]*v[1] + v[1]**2
grad_g = jax.grad(g)
pt = jnp.array([1.0, 2.0])
print(f"∇f at (1,2): {grad_g(pt)}")
# [7. 6.]

# --- Hessian: matrix of second partials ---
# H = [[6x, 2], [2, 2]]  →  at (1,2): [[6, 2], [2, 2]]
hessian_g = jax.hessian(g)
H = hessian_g(pt)
print(f"Hessian at (1,2):\n{H}")
# [[6. 2.]
#  [2. 2.]]
