// dafny verify 04_dafny.dfy
// The chapter's eq.(2) as a VERIFIED imperative program: sum the first n odd
// numbers in a loop and prove the result is n*n. A loop invariant is the
// programming counterpart of an induction hypothesis -- Dafny's verifier checks
// it is established before the loop, preserved by every iteration (the n-1 -> n
// step), and strong enough at exit to give the postcondition. No test runs;
// the SMT backend proves it for ALL n.

method SumOfOdds(n: nat) returns (s: nat)
  ensures s == n * n            // 1 + 3 + ... + (2n-1) = n^2
{
  s := 0;
  var k := 0;
  while k < n
    invariant 0 <= k <= n
    // <-- the "induction hypothesis": after k terms, sum is k^2
    invariant s == k * k
  {
    s := s + (2 * k + 1);       // add the (k+1)-th odd number, 2k+1
    k := k + 1;
  }
  // On exit k == n, so the invariant gives s == n*n, discharging `ensures`.
}

// Theorem 3.1 as a verified loop: n lines in general position cut the plane
// into 1 + (1+2+...+n) regions. The k-th new line adds k regions; the
// invariant says after placing k lines we have the closed-form count.
method CountRegions(n: nat) returns (r: nat)
  ensures r == 1 + n * (n + 1) / 2
{
  r := 1;                       // 0 lines -> 1 region (the start point)
  var k := 0;
  while k < n
    invariant 0 <= k <= n
    invariant r == 1 + k * (k + 1) / 2
  {
    k := k + 1;
    r := r + k;                 // k-th line crosses k-1 others -> +k
  }
}
