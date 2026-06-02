# uv run python \
#   "code/pim/05 - Calculus with One Variable/06_newton_failure_loop.py"
# The flip side of Theorem 8.15: a BAD starting point. With the same
# f(x) = x^5 - x - 1 but starting at x_1 = 0, Newton's method does NOT
# converge -- it eventually cycles. This is "allowed" because between
# the start and the root f'(x) hits zero, blowing up the constant C in
# the error bound. We detect the cycle instead of converging.
def f(x):
    return x**5 - x - 1


def f_derivative(x):
    return 5 * x**4 - 1


def newton(start, steps):
    x = start
    for _ in range(steps):
        yield x
        x = x - f(x) / f_derivative(x)


# Good start: converges fast.
good = list(newton(1.0, 30))
assert abs(f(good[-1])) < 1e-12
print(f"start 1.0 -> root {good[-1]:.12f}, f={f(good[-1]):.1e}")

# Bad start: never settles. Collect the late iterates and show the
# sequence keeps re-visiting nearby values (a cycle), not a root.
tail = [round(v, 6) for v in list(newton(0.0, 200))[-30:]]
distinct = sorted(set(tail))
assert all(abs(f(v)) > 0.1 for v in distinct)   # none are roots
# The tail revisits only a handful of values: it is looping.
assert len(distinct) <= 6
print(f"start 0.0 -> never converges; tail cycles among "
      f"{len(distinct)} values:")
for v in distinct:
    print(f"   x={v:+.6f}  f(x)={f(v):+.6f}")
print("\nNewton is powerful but needs a wise starting point.")
