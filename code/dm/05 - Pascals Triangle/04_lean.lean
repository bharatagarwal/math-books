-- lean 04_lean.lean
-- Hockey-stick identity (7) from the chapter, proved by induction on k,
-- exactly the way the book does it:
--   C(n,0) + C(n+1,1) + ... + C(n+k,k) = C(n+k+1, k).
--
-- Self-contained (no Mathlib): we define the binomial coefficient `c`
-- directly by the Pascal recurrence (5)
--   c n 0           = 1
--   c 0 (k+1)       = 0
--   c (n+1) (k+1)   = c n k + c n (k+1)
-- and the running diagonal sum `hsum n k = sum_{i=0}^{k} C(n+i, i)`.

namespace Pascal

/-- Binomial coefficient defined purely by the Pascal recurrence (5). -/
def c : Nat → Nat → Nat
  | _,     0     => 1
  | 0,     _+1   => 0
  | n+1, k+1 => c n k + c n (k+1)

/-- The fundamental property (5): C(n+1,k+1) = C(n,k) + C(n,k+1). -/
theorem pascal (n k : Nat) : c (n+1) (k+1) = c n k + c n (k+1) := rfl

/-- Each row starts with 1: C(n,0) = 1 (exercise 5.2, the left 1's). -/
theorem start_one (n : Nat) : c n 0 = 1 := by
  cases n <;> rfl

/-- Diagonal sum  hsum n k = C(n,0) + C(n+1,1) + ... + C(n+k,k). -/
def hsum (n : Nat) : Nat → Nat
  | 0     => c n 0
  | k+1 => hsum n k + c (n + (k+1)) (k+1)

/-- Hockey-stick identity (7), by induction on k -- the book's proof.
    Base k = 0 is `1 = 1`; the step uses property (5). -/
theorem hockey_stick (n k : Nat) : hsum n k = c (n + k + 1) k := by
  induction k with
  | zero =>
      -- hsum n 0 = c n 0 = 1 = c (n+1) 0
      show c n 0 = c (n + 0 + 1) 0
      rw [start_one, start_one]
  | succ k ih =>
      -- hsum n (k+1) = hsum n k + C(n+k+1, k+1)
      --             = C(n+k+1, k) + C(n+k+1, k+1)   (induction hypothesis)
      --             = C(n+k+2, k+1)                 (Pascal recurrence)
      show hsum n k + c (n + (k + 1)) (k + 1) = c (n + (k + 1) + 1) (k + 1)
      rw [ih]
      -- Normalize the index n + (k+1) to the canonical n + k + 1 so the
      -- two C(n+k+1, .) terms line up, then apply the Pascal recurrence.
      have idx : n + (k + 1) = n + k + 1 := by omega
      rw [idx, pascal (n + k + 1) k]

-- Reproduce the book's worked example: starting from the last entry of
-- row 2 and summing down-left gives 1, 4, 10, 20  (these are C(3,0)=1 of
-- the diagonal n=2):  hsum 2 0..3  =  1, 4, 10, 20.
example : hsum 2 0 = 1  := by decide
example : hsum 2 1 = 4  := by decide
example : hsum 2 2 = 10 := by decide
example : hsum 2 3 = 20 := by decide

-- And these equal the closed form C(n+k+1, k):
example : c 3 0 = 1  := by decide
example : c 4 1 = 4  := by decide
example : c 5 2 = 10 := by decide
example : c 6 3 = 20 := by decide

#eval (List.range 4).map (hsum 2)        -- [1, 4, 10, 20]

end Pascal
