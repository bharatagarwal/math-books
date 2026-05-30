// dafny verify code/bradfield/06-induction/03_gauss_sum.dfy
// The little-Gauss sum 1 + 2 + ... + n = n(n+1)/2, but as a verified
// LOOP. The loop invariant is the inductive hypothesis made machine-
// checkable: Dafny proves it holds initially, is preserved by each
// iteration, and -- together with the loop guard -- yields the
// postcondition. That is exactly base case + inductive step.
method GaussSum(n: nat) returns (s: nat)
  ensures s == n * (n + 1) / 2
{
  s := 0;
  var i := 1;
  while i <= n
    invariant 1 <= i <= n + 1
    // s already holds 1 + 2 + ... + (i-1) = (i-1)*i/2
    invariant s == (i - 1) * i / 2
    decreases n - i + 1
  {
    s := s + i;
    i := i + 1;
  }
}

// A second proof: the closed form as a recursive function with a
// matching inductive lemma. Structural/ordinary induction in Dafny is
// just a recursive proof, and Dafny checks the step for us.
function SumTo(n: nat): nat
{
  if n == 0 then 0 else SumTo(n - 1) + n
}

lemma GaussClosedForm(n: nat)
  ensures SumTo(n) == n * (n + 1) / 2
{
  // base case n == 0 is automatic; the inductive step recurses.
  if n == 0 {
  } else {
    GaussClosedForm(n - 1); // inductive hypothesis for n-1
  }
}
