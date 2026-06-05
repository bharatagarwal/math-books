# Official Documentation — Verification & Math Toolchain

Quick-reference links for every tool used in this repo. All links verified live 2026-06-05.

## Formal Verification

| Tool | Role here | Official docs |
|------|-----------|---------------|
| **Lean4** | Theorem proving (proofs, induction, logic) | [lean-lang.org/documentation](https://lean-lang.org/documentation/) · [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/) · [Mathlib4 docs](https://leanprover-community.github.io/mathlib4_docs/) |
| **Dafny** | Program verification (pre/post + invariants) | [Reference manual](https://dafny.org/latest/DafnyRef/DafnyRef) · [dafny.org](https://dafny.org/) |
| **Z3** (`z3-solver`) | SMT for constraints / puzzles | [Z3 guide](https://microsoft.github.io/z3guide/) · [Python API reference](https://z3prover.github.io/api/html/namespacez3py.html) |
| **deal** | Python Design by Contract decorators | [deal.readthedocs.io](https://deal.readthedocs.io/) |
| **CrossHair** (`crosshair-tool`) | SMT-based symbolic execution (pairs with deal) | [crosshair.readthedocs.io](https://crosshair.readthedocs.io/) |
| **Hypothesis** | Property-based testing | [hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/) |
| **XState** | State machine modeling (MCS Ch 6) | [stately.ai/docs](https://stately.ai/docs) |

## Symbolic / Numerical Math

| Tool | Role here | Official docs |
|------|-----------|---------------|
| **SymPy** | Symbolic algebra: `diff`, `integrate`, `Sum`, `solve` | [docs.sympy.org](https://docs.sympy.org/latest/) |
| **JAX** | Numeric autodiff: `grad`, `hessian`, `jacobian` | [docs.jax.dev](https://docs.jax.dev/) |
| **NumPy** | Arrays, `einsum` for index notation | [numpy.org/doc/stable](https://numpy.org/doc/stable/) · [`einsum` reference](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) |
| **NetworkX** | Graph theory demos | [networkx.org/documentation/stable](https://networkx.org/documentation/stable/) |
| **handcalcs** | Python expressions → rendered LaTeX (Jupyter) | [GitHub README](https://github.com/connorferster/handcalcs) (the official doc) |

## Supporting Tooling

| Tool | Role here | Official docs |
|------|-----------|---------------|
| **uv** | Runs all Python tools (`uv run --with <pkg>`), PEP 723 scripts | [docs.astral.sh/uv](https://docs.astral.sh/uv/) |
| **KaTeX** | Math rendering in the reader | [katex.org/docs](https://katex.org/docs/) · [Supported functions](https://katex.org/docs/supported.html) — the page to check when authoring LaTeX for reader pages |
| **TLA+** | Future destination (distributed systems track) | [Lamport's TLA+ home](https://lamport.azurewebsites.net/tla/tla.html) · [Learn TLA+](https://learntla.com/) |
