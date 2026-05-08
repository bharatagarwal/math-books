# CLAUDE.md

Guidance for Claude Code working in this repository.

## Learning Approach

Software engineer learning mathematics through programming. Instead of manual computation, use formal verification and symbolic tools to understand concepts deeply.

**Methodology — personal "web book":** All PDF processing here is for personal study only. The goal is to feed source materials to an LLM to draft a custom textbook tailored to the user's background and learning preferences, which the user will then iteratively refine over time. No publication is intended; this is solely a learning methodology. When generating or rewriting content from source PDFs, optimize for *the user's understanding*, not external readability.

## Curriculum

Canonical plan: **`docs/learning-plan.md`** (stages, calibration gates, resources, productization paths).

High-level arc: discrete math foundations → formal verification → distributed systems (TLA+).

Source materials in this repo:
- `mcs/` — MIT 6.042J Mathematics for Computer Science (primary text). **Prefer the per-chapter PDFs in `mcs/01 - Proofs/`, `mcs/02 - Structures/`, `mcs/03 - Counting/`, `mcs/04 - Probability/`** over the full `mcs-2018-06-06.pdf` — never OCR the whole book; process chapters as needed.
- `aops-*/` — Art of Problem Solving books (03 counting & 05 number theory are load-bearing for this curriculum)
- `a-programmers-introduction-to-mathematics.pdf` — Jeremy Kun (programming-first math)
- `deep-learning.pdf` — Goodfellow et al. (deferred until after DM foundation)
- `math-2020-06-outline.pdf` — Bradfield course outline (the original inspiration)

## Verification Toolchain

| Tool | Role | Status |
|------|------|--------|
| **Lean4** (4.30+) | Theorem proving (proofs, induction, logic) | Installed via elan; `lean`/`lake` on PATH |
| **Dafny** (4.11+) | Program verification with pre/post + invariants | Installed via Homebrew; `dafny` on PATH |
| **deal** | Python Design by Contract decorators | Run via `uv run --with deal` |
| **crosshair-tool** | SMT-based symbolic execution (pairs with deal) | Run via `uv run --with crosshair-tool` |
| **z3-solver** | SMT for constraints / puzzles | Run via `uv run --with z3-solver` |
| **hypothesis** | Property-based testing | Run via `uv run --with hypothesis` |
| **XState** | State machine modeling | Pull in via npm when reaching MCS Ch 6 |

Python tools run through `uv` — no virtualenv, no `requirements.txt`. Lean4 and Dafny are installed system-wide.

## Math Notation → Code

When notation feels opaque, translate it to executable code. Each library handles a different family of notation:

| Notation | Library | Run with |
|----------|---------|----------|
| `∂f/∂x`, `∫ f dx`, `Σ`, symbolic algebra | **sympy** — `diff`, `integrate`, `Sum`, `solve` | `uv run --with sympy` |
| `∇f`, Hessian, numeric autodiff | **jax** — `grad(f)`, `hessian(f)`, `jacobian(f)` | `uv run --with jax` |
| `Σᵢ aᵢ bᵢ`, tensor index gymnastics | **numpy einsum** — `np.einsum("ij,jk->ik", A, B)` | `uv run --with numpy` |
| `∀x ∃y …` (predicate logic) | **z3** — `ForAll([x], Exists([y], ...))` | `uv run --with z3-solver` |
| Python expressions → rendered LaTeX | **handcalcs** — Jupyter-only; renders as you type | `uv run --with handcalcs jupyter lab` |

Quick examples:

```bash
# Derivative of x^3 + 2x
uv run --with sympy python -c "
import sympy as sp; x = sp.Symbol('x')
print(sp.diff(x**3 + 2*x, x))"   # 3*x**2 + 2

# Gradient of f(x,y) = x^3 + 2xy + y^2 at (1,2)
uv run --with jax python -c "
import jax.numpy as jnp; from jax import grad
f = lambda v: v[0]**3 + 2*v[0]*v[1] + v[1]**2
print(grad(f)(jnp.array([1.0, 2.0])))"   # [7. 6.]

# Inner product via Einstein summation
uv run --with numpy python -c "
import numpy as np
print(np.einsum('i,i->', [1,2,3], [4,5,6]))"   # 32
```

## Repo Layout

- `docs/learning-plan.md` — Canonical curriculum (stage-based with calibration gates)
- `scripts/` — Tooling. Each script declares deps via PEP 723 inline metadata.
- `scripts/.env` — Holds `MISTRAL_API_KEY` (gitignored)
- `scripts/pdf_to_markdown.py` — Mistral OCR pipeline with high-res image extraction
- `markdown/` — OCR'd output, mirrors source PDF paths; images in sibling `<basename>_images/` dirs
- `mcs/`, `aops-*/`, `*.pdf` — Source materials (read-only)

## Commands

```bash
# OCR pipeline (idempotent; skips already-processed PDFs via manifest)
uv run scripts/pdf_to_markdown.py <pdf>
uv run scripts/pdf_to_markdown.py "mcs/01 - Proofs/"     # accepts directories (recursive)
uv run scripts/pdf_to_markdown.py --all                  # whole library (~$7-8)
uv run scripts/pdf_to_markdown.py --force <pdf>          # re-process

# Verification tools — uv installs each on demand, no global state
uv run --with crosshair-tool crosshair check <module.py>
uv run --with deal python -m deal lint <module.py>
uv run --with deal python -m deal test <module.py>
uv run --with z3-solver python <z3_script.py>
uv run --with hypothesis pytest <test_file.py>

# Symbolic / numerical math (pull in only what's needed per script)
uv run --with sympy python <script.py>
uv run --with jax python <script.py>
uv run --with numpy python <script.py>
uv run --with networkx python <script.py>

# Lean4 — quick check of a single file, or build a project
lean <file>.lean         # type-check / verify a standalone proof file
lake new <proj>          # create project
lake build               # build/check proofs in a project

# Dafny — verify a file
dafny verify <file>.dfy
```

## System Dependencies

Required by `scripts/pdf_to_markdown.py`:
- `pdftoppm` (from Poppler) — page rendering at high DPI
- `magick` (from ImageMagick) — bbox cropping
- Install: `brew install poppler imagemagick`

## Typical Session

1. Pick current stage from `docs/learning-plan.md`
2. Read source: PDF or OCR'd markdown in `markdown/`
3. Practice in stage-appropriate tool (Lean4 for proofs, Z3 for constraints, Python + deal/crosshair for verified code)
4. Verify before advancing — pass the stage's calibration gate
5. Stuck >20 min? Drop difficulty (Flow), or check prerequisites (Goldratt's constraint)

## Gotchas

- **mistralai 2.x import:** `from mistralai.client.sdk import Mistral`. Top-level `from mistralai import Mistral` does NOT work in 2.x (namespace package, no top-level `__init__.py`).
- **Mistral OCR image quality:** The API returns ~100-200px thumbnails. For real resolution, request bboxes only (`include_image_base64=False`), render pages locally with `pdftoppm` at 300 DPI, crop with `magick`. See `scripts/pdf_to_markdown.py`.
- **LaTeX is automatic in OCR:** Mistral OCR already returns equations as inline `$...$` and block `$$...$$` LaTeX in the markdown — no parameter needed. The output preserves `\frac`, `\mathbb`, `\sum`, `\cdots`, etc.
- **OCR is just-in-time, one chapter at a time:** Never OCR the full MCS textbook, never OCR a whole chapter folder, never `--all`. Process exactly the chapter the user is about to study. OCRing ahead of the learning pace builds inventory in front of the real constraint (reading/practice speed) — Goldratt violation. If you find yourself wanting to bulk-OCR, stop and pick the single next chapter instead.
- **OCR idempotency:** Each `.md` has a sibling `.manifest.json` capturing source size + model. Re-runs skip unchanged PDFs; `--force` overrides.
- **No `pip install`:** Always `uv run --with <pkg>` for one-offs, PEP 723 inline metadata for scripts. No `requirements.txt` or `.venv` in this repo.
- **elan PATH for zsh:** elan installs into `~/.profile`, which zsh doesn't source. `~/.zshrc` is patched to source `~/.elan/env`. New shells get `lean`/`lake`/`elan` automatically; existing shells need `source ~/.elan/env` once.
