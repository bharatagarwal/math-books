-- lean 03_lean.lean
-- A real machine-checked induction proof of the chapter's eq.(2):
--   1 + 3 + ... + (2n-1) = n^2.
-- This mirrors the book's argument exactly: base case n = 0, and the inductive
-- step peels off the last odd number (2n-1) and uses the hypothesis for n-1
-- (here: for `n` to get `n+1`), then closes with `ring`.
-- Standalone Lean 4 (no Mathlib), matching this repo's convention.

-- oddSum n = sum of the first n odd numbers, defined recursively.
-- The (k+1)-th odd number is 2*k + 1  (= 2*(k+1) - 1).
def oddSum : Nat → Nat
  | 0     => 0
  | n + 1 => oddSum n + (2 * n + 1)

-- The induction: oddSum n = n^2 for every n.
theorem oddSum_eq_sq (n : Nat) : oddSum n = n * n := by
  induction n with
  | zero =>
      -- Base case: empty sum is 0 = 0*0.
      -- (chapter checks n=1; n=0 is the cleaner base)
      rfl
  | succ k ih =>
      -- Inductive step: assume oddSum k = k*k (the induction hypothesis `ih`),
      -- prove oddSum (k+1) = (k+1)*(k+1).
      simp only [oddSum, ih]   -- reduce goal to  k*k + (2*k+1) = (k+1)*(k+1)
      -- expand the products to a linear goal, then close it (no `ring`).
      simp [Nat.mul_add, Nat.add_mul, Nat.mul_one, Nat.one_mul]
      omega                    -- k*k + (2*k+1) = (k+1)*(k+1)

-- Sanity #eval reproducing the book's table (1,4,9,...,100 for n=1..10).
#eval (List.range 10).map (fun i => oddSum (i + 1))
-- expect: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

-- A compile-time confirmation that the table matches the squares.
example : (List.range 10).map (fun i => oddSum (i + 1))
        = (List.range 10).map (fun i => (i + 1) * (i + 1)) := by decide
