theorem even_square_is_even (n : Nat) (h : Even n) : Even (n * n) := by
  rcases h with ⟨k, hk⟩           -- "n is even" means n = 2k for some k
  rw [hk]                          -- substitute n = 2k
  use 2 * k * k                    -- n² = 2(2k²), so witness is 2k²
  ring                             -- algebra: (2k)² = 2(2k²)
