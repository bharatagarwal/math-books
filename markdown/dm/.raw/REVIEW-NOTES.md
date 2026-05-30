# DM extraction — residual OCR flags (human review)

The per-chapter cleanup applied 29 confirmed KaTeX fixes and I hand-fixed 11 more
unambiguous main-text math errors (binomial theorem term order, anagram `n!`,
Fibonacci Binet/golden-ratio derivation, `2^6=64`, ex 2.6 set literal, RSA `x^e`,
`q_i = p_1 a_i`). Raw OCR is preserved in this `.raw/` dir for diffing.

The items below render in KaTeX but are mathematically suspect. They sit in
exercises, the answers section, or advanced asides, and the exact intended form is
ambiguous without re-checking the source page — left as-is rather than guessing:

- **05 Pascal's Triangle** — Stirling estimate of the central binomial coefficient
  (`\binom{n}{n/2} \sim ...`) is garbled mid-expression (`\binom{n}{2}^n` etc.).
  Needs source pp.40–43 to reconstruct the `2^n / \sqrt{...}` form.
- **06 Fibonacci** — an exercise identity appears to drop a `+` between two
  `\log_2(...)` terms.
- **08 Integers/primes** — in the `a^561 - a` factorization chain, two consecutive
  tagged lines (16) and (17) are byte-identical; likely an OCR-duplicated/dropped step.
- **09 Graphs** — `as claimed. $^3$` is a footnote marker OCR'd as a base-less
  superscript; renders, but is semantically a footnote.
- **16 Answers** — several solution lines are merged/missing an `=`
  (e.g. 6.5(b), 6.5(c)), `2·(10^n - 10^{n-1}` is missing a close paren, and the
  8.5 answer `2^4 - 2 - 14` is probably `= 14`. This is the solutions reference.
