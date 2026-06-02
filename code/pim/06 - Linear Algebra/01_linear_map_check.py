# uv run --with numpy python \
#   "code/pim/06 - Linear Algebra/01_linear_map_check.py"
#
# Chapter 10, Section 10.2: a linear map preserves + and scaling.
# We test two of Kun's own examples:
#   - eval_7(p) = p(7) on the vector space of polynomials, and
#   - f(a,b,c) = (-2a + 3b, c) from R^3 to R^2.
# A function is linear iff f(v+w)=f(v)+f(w) and f(c.v)=c.f(v)
# for ALL inputs, so we hammer it with random inputs.

import random


def eval_7(coeffs):
    """Evaluate a polynomial (low-degree-first coeffs) at x = 7."""
    return sum(a * 7 ** i for i, a in enumerate(coeffs))


def poly_add(p, q):
    """Add two coefficient lists, padding the shorter one."""
    n = max(len(p), len(q))
    p = p + [0] * (n - len(p))
    q = q + [0] * (n - len(q))
    return [a + b for a, b in zip(p, q)]


def poly_scale(c, p):
    return [c * a for a in p]


def f_R3_to_R2(v):
    a, b, c = v
    return (-2 * a + 3 * b, c)


def check_eval_7():
    for _ in range(10_000):
        p = [random.randint(-9, 9) for _ in range(random.randint(0, 5))]
        q = [random.randint(-9, 9) for _ in range(random.randint(0, 5))]
        c = random.randint(-9, 9)
        # f(p + q) == f(p) + f(q)
        assert eval_7(poly_add(p, q)) == eval_7(p) + eval_7(q)
        # f(c . p) == c . f(p)
        assert eval_7(poly_scale(c, p)) == c * eval_7(p)


def check_R3_R2():
    for _ in range(10_000):
        v = [random.randint(-9, 9) for _ in range(3)]
        w = [random.randint(-9, 9) for _ in range(3)]
        c = random.randint(-9, 9)
        vw = [a + b for a, b in zip(v, w)]
        fv, fw, fvw = f_R3_to_R2(v), f_R3_to_R2(w), f_R3_to_R2(vw)
        assert fvw == (fv[0] + fw[0], fv[1] + fw[1])
        cv = [c * a for a in v]
        assert f_R3_to_R2(cv) == (c * fv[0], c * fv[1])


def check_nonlinear_counterexample():
    """g(x) = x + 1 is NOT linear: it fails to preserve zero."""
    g = lambda x: x + 1
    # Proposition 10.3 says a linear map sends 0 to 0. g(0) = 1.
    assert g(0) != 0
    # and it breaks additivity outright:
    assert g(2 + 3) != g(2) + g(3)


if __name__ == "__main__":
    check_eval_7()
    print("eval_7 is linear: 10000 random (p, q, c) all passed")
    check_R3_R2()
    print("(a,b,c) -> (-2a+3b, c) is linear: 10000 passed")
    check_nonlinear_counterexample()
    print("x -> x+1 fails linearity (g(0) = 1, not 0)")
