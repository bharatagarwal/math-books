# uv run --with numpy python
"""Matrix form of the recurrence, and Cassini's identity as a determinant.

The recurrence F_{n+1}=F_n+F_{n-1} is exactly one matrix step:

    [F_{n+1}]   [1 1] [F_n  ]              [1 1]^n   [F_{n+1}  F_n    ]
    [F_n    ] = [1 0] [F_{n-1}]   so       [1 0]   = [F_n      F_{n-1}].

So M^n recovers the whole sequence by repeated doubling (memo-free fast
power), and det(M)=-1 gives det(M^n)=(-1)^n, which IS Cassini's identity
(6.5 d): F_{n+1}F_{n-1} - F_n^2 = (-1)^n. We use Python ints (object
dtype) so the entries stay exact, then check against the book's sequence.
"""
import numpy as np

M = np.array([[1, 1], [1, 0]], dtype=object)  # object -> exact big ints


def mat_pow(A, k):
    """Fast exponentiation by squaring; A^0 = I."""
    R = np.array([[1, 0], [0, 1]], dtype=object)
    while k:
        if k & 1:
            R = R @ A
        A = A @ A
        k >>= 1
    return R


# M^n = [[F_{n+1}, F_n], [F_n, F_{n-1}]]
expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
            55, 89, 144, 233, 377, 610, 987, 1597]
got = []
for n in range(len(expected)):
    Mn = mat_pow(M, n)
    got.append(int(Mn[0, 1]))  # F_n is the off-diagonal entry of M^n
print("F_0..F_17 via M^n   :", got)
assert got == expected, "matrix power did not reproduce the book's sequence"

# Cassini via determinant: det(M^n) = det(M)^n = (-1)^n.
print("\nCassini  F_{n-1}F_{n+1} - F_n^2  vs  (-1)^n:")
for n in range(1, 11):
    Mn = mat_pow(M, n)
    Fn1, Fn, Fnm1 = int(Mn[0, 0]), int(Mn[0, 1]), int(Mn[1, 1])
    cassini = Fnm1 * Fn1 - Fn * Fn
    det = round((-1) ** n)
    lhs = f"  n={n:2d}:  {Fnm1}*{Fn1} - {Fn}^2 = {cassini:>2d}"
    print(f"{lhs}   (-1)^{n} = {det:>2d}")
    assert cassini == det == (-1) ** n

# A big term to show exactness survives: F_100.
F100 = int(mat_pow(M, 100)[0, 1])
print("\nF_100 =", F100)
assert F100 == 354224848179261915075
print("OK: matrix recurrence reproduces the sequence; det = Cassini")
