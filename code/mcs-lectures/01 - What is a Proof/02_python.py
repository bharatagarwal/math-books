# uv run --with sympy python
a, b, c, d = 95800, 217519, 414560, 422481
print(f"a⁴ + b⁴ + c⁴ = {a**4 + b**4 + c**4}")
print(f"d⁴         = {d**4}")
print(f"Equal: {a**4 + b**4 + c**4 == d**4}")
# Output: Equal: True
