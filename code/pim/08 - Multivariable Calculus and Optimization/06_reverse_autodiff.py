# uv run --with numpy --with sympy python "code/pim/08 - Multivariable Calculus and Optimization/06_reverse_autodiff.py"
#
# Section 14.8: reverse-mode autodiff on a computation graph.  A tiny
# scalar tape (like Kun's Node class, but condensed) where each node
# caches its output (forward pass) and accumulates dG/dnode (backward
# pass) via the chain rule  dG/df = sum_h (dG/dh)(dh/df).  We then check
# the whole-graph gradient against sympy's exact symbolic gradient.
import math
import numpy as np
import sympy as sp


class Node:
    def __init__(self, value=0.0, parents=()):
        self.value = value
        self.parents = parents      # list of (parent_node, local_deriv)
        self.grad = 0.0             # accumulated dG/dself


def const(v):
    return Node(v)


def add(a, b):
    return Node(a.value + b.value, [(a, 1.0), (b, 1.0)])


def mul(a, b):
    return Node(a.value * b.value, [(a, b.value), (b, a.value)])


def sin(a):
    return Node(math.sin(a.value), [(a, math.cos(a.value))])


def expnode(a):
    e = math.exp(a.value)
    return Node(e, [(a, e)])


def backward(out):
    out.grad = 1.0              # dG/dG = 1 (base case)
    topo, seen = [], set()

    def build(n):
        if id(n) in seen:
            return
        seen.add(id(n))
        for p, _ in n.parents:
            build(p)
        topo.append(n)

    build(out)
    for n in reversed(topo):       # outputs before inputs
        for p, local in n.parents:
            p.grad += n.grad * local   # chain rule, summed over paths


# Graph for  G(x, y) = sin(x*y) + exp(x + y)   at (x, y) = (1.3, -0.7).
xv, yv = 1.3, -0.7
x, y = Node(xv), Node(yv)
G = add(sin(mul(x, y)), expnode(add(x, y)))
backward(G)
auto = np.array([x.grad, y.grad])

# Exact symbolic gradient for comparison.
sx, sy = sp.symbols("x y")
Gs = sp.sin(sx * sy) + sp.exp(sx + sy)
exact = np.array([float(sp.diff(Gs, v).subs({sx: xv, sy: yv}))
                  for v in (sx, sy)])

print("G value     :", round(G.value, 6))
print("autodiff dG :", np.round(auto, 6))
print("exact    dG :", np.round(exact, 6))
assert np.allclose(auto, exact, atol=1e-9)
print("Reverse-mode autodiff matches the analytic gradient.")
