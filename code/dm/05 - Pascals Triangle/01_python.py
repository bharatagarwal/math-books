# uv run --with numpy python
"""Build Pascal's Triangle purely by the recurrence (5):

    C(n, k) = C(n-1, k-1) + C(n-1, k),    with the boundary 1's.

No factorials, no math.comb -- only additions, exactly the way the book
says the triangle "generates itself very fast, building it up row by row."
We then read off the book's row-sum (=2^n) and alternating-sum (=0) facts
straight from the rows we built.
"""
import numpy as np

N = 8  # build rows 0..8 (enough to also see the sum-of-squares target C(2n,n))


def pascal_rows(N):
    rows = [[1]]
    for n in range(1, N + 1):
        prev = rows[-1]
        # interior entry j is prev[j-1] + prev[j]; ends are the boundary 1's
        row = [1] + [prev[j - 1] + prev[j] for j in range(1, n)] + [1]
        rows.append(row)
    return rows


rows = pascal_rows(N)

print("Pascal's Triangle, rows 0..%d (built only by the recurrence):" % N)
for n, row in enumerate(rows):
    print(f"  n={n}: {row}")

# The chapter's numeric triangle: verify the recurrence built reproduces
# the textbook entries, e.g. interior 6 = 3 + 3 in row 4.
assert rows[4] == [1, 4, 6, 4, 1], "row 4 must match the book's 1 4 6 4 1"
assert rows[4][2] == rows[3][1] + rows[3][2] == 6  # 6 = 3 + 3

print("\nRow sum = 2^n (exercise 5.3) and alternating sum = 0 for"
      " n>=1 (Sec 5.1):")
for n, row in enumerate(rows):
    r = np.array(row, dtype=object)
    total = int(r.sum())
    signs = np.array([(-1) ** k for k in range(len(row))], dtype=object)
    alt = int((r * signs).sum())
    assert total == 2 ** n, f"row {n} sum {total} != 2^{n}"
    # The alternating sum is 0 for every n >= 1; the
    # empty/degenerate row 0 is just 1.
    assert alt == (1 if n == 0 else 0), \
        f"row {n} alternating sum {alt} unexpected"
    print(f"  n={n}: sum={total}=2^{n}   alternating sum={alt}")

print("\nAll recurrence-built rows satisfy sum=2^n, and"
      " alternating sum=0 for n>=1.")
