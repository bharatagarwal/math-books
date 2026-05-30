# uv run python code/bradfield/06-induction/02_gnomon_squares.py
# Intuition demo: WHY does adding the next odd number grow the square?
# Build the n x n grid out of nested L-shaped "gnomons". The k-th
# gnomon (the border added to reach a k x k square) has exactly
# 2k - 1 cells -- the k-th odd number. This is the inductive step you
# can *see*: going from (n-1)^2 to n^2 costs exactly 2n - 1 new cells.


def gnomon_layer(grid, k):
    """Number of NEW cells added going from a (k-1)^2 to a k^2 square."""
    added = 0
    for r in range(k):
        for c in range(k):
            if (r == k - 1 or c == k - 1) and grid[r][c] == 0:
                grid[r][c] = k  # label the cell with the layer it joined
                added += 1
    return added


def render(grid, n):
    rows = []
    for r in range(n):
        rows.append(" ".join(str(grid[r][c]) for c in range(n)))
    return "\n".join(rows)


def main():
    n = 5
    grid = [[0] * n for _ in range(n)]
    for k in range(1, n + 1):
        added = gnomon_layer(grid, k)
        print(f"layer k={k}: added {added} cells (odd number 2k-1="
              f"{2 * k - 1}), total = {k * k}")
        assert added == 2 * k - 1
    print()
    print("grid labelled by the layer each cell joined:")
    print(render(grid, n))


if __name__ == "__main__":
    main()
