# CLAUDE.md

Guidance for Claude Code working in this repository.

## Working Agreement (non-negotiable)

These are corrections from past sessions. Do not repeat them.

- **Finish the work. Never hand back partial work with a question to dodge the rest.** Do not stop at "good enough," do not present "~20% polish left" as done, and do not end a turn with a clarifying question whose real purpose is to avoid doing the work. If the path is obvious, do it. Token cost is not a reason to stop. Drive every task to genuinely complete + verified.
- **Verify qualitatively, not just for absence of errors.** "0 KaTeX errors" is not verification. Actually look: are equations sized right and not clipping the column? do figures have proper captions and sensible size? does the page read like a book? Screenshot real pages and assess.
- **Weave programmatic examples INTO the narrative, at the concept.** Each runnable verification (sympy/z3/networkx/Lean4/Dafny demo) goes immediately after the theorem/example/derivation it illuminates — NOT dumped in a single "Programmatic Exploration" section at the end. The point of this reader is that code and math read as one argument; making the reader jump between sections is a failure.
- **Use carousels for groups of related/sequential figure panels** (see Authoring Reader Pages) so the reader isn't forced to scroll through many similar images.
- **The source PDF is ground truth.** When fixing OCR'd math/figures, read the actual source pages and make the content faithful (or mathematically correct where the source itself has a typo); never leave a known-garbled formula "flagged for later."
- **Don't assume the user is avoiding work or being "lazy."** This math project is a deliberate **discovery / curriculum-framing phase** on a **medium-term horizon** — explicitly *not* meant to yield within ~6 months — pursued alongside a day job and separate agentic-coding and CS-fundamentals tracks. The reader, the lecture-dialogues, and the verification tooling are **scaffolding the user is building so they CAN do the real work**, not a substitute for it. Facilitate (pull up sources, build the scaffolding, engage the ideas); never inject judgments about motivation, procrastination, "dodging the reps," or "appreciation without ability." Sequencing and pace are the user's to set.
- **When the user names a source (article, person, book), pull it up before responding** — don't merely offer to. Read it, then engage with the actual text.
- **Background the grunt work; keep the foreground for the conversation.** Anything mechanical that doesn't itself advance the discussion — bulk markdown/normalization passes, OCR, builds, multi-file edits, long verification sweeps — must run in the background (a `/bg` subagent or a background shell job), not in the foreground while the user waits. The user is focused on the bigger picture; do not make them sit and watch grunt work. Launch it, hand control straight back, and report when it lands. Foreground turns are for thinking and discussion, not for me grinding.
- **Respect the user's time — maximize parallelism.** Run independent tasks concurrently using background subagents, parallel tool calls, and background shell jobs. Be judicious about *what* can safely run in parallel (independent file edits, builds + tests, OCR of separate chapters, research queries) vs. what has true sequential dependencies. The goal is wall-clock efficiency: if three things can happen at once, they should.
- **Never hand over without verifying.** Every deliverable must be verified before reporting it as done — run the code, screenshot the page, check the build, confirm the output. "It should work" is not verification. If you can't verify (e.g., no browser available), say so explicitly rather than claiming success.
- **Token spend is not a concern; quality of thought and implementation is.** Do not cut corners, skip verification, or produce shallow work to save tokens. Think deeply, explore the problem space, and produce work that reflects genuine understanding. High quality means both *quality of reasoning* (correct analysis, good judgment calls, engagement with the actual ideas) and *quality of implementation* (clean code, faithful rendering, working artifacts).

## Learning Approach

Software engineer learning mathematics through programming. Instead of manual computation, use formal verification and symbolic tools to understand concepts deeply.

**Methodology — personal "web book":** All PDF processing here is for personal study only. The goal is to feed source materials to an LLM to draft a custom textbook tailored to the user's background and learning preferences, which the user will then iteratively refine over time. No publication is intended; this is solely a learning methodology. When generating or rewriting content from source PDFs, optimize for *the user's understanding*, not external readability.

## Curriculum

Canonical plan: **`docs/learning-plan.md`** (stages, calibration gates, resources, productization paths).

High-level arc: discrete math foundations → formal verification → distributed systems (TLA+).

Source materials in this repo:
- `mcs/` — MIT 6.042J Mathematics for Computer Science (primary text). **Prefer the per-chapter PDFs in `mcs/01 - Proofs/`, `mcs/02 - Structures/`, `mcs/03 - Counting/`, `mcs/04 - Probability/`** over the full `mcs-2018-06-06.pdf` — never OCR the whole book; process chapters as needed.
- `mcs-lectures` (video-derived) — separate track from the textbook: MIT 6.042J Fall 2010 lectures turned into prose via `scripts/srt_to_prose.py`, output in `markdown/mcs-lectures/`.
- `dmbook.pdf` / `dm/` — Lovász & Vesztergombi *Discrete Mathematics* (Yale lecture notes, 1999). Split into per-chapter PDFs under `dm/`, OCR'd to `markdown/dm/`, code in `code/dm/`, registered in the reader as the **Discrete Mathematics** book. Programmatic-exploration demos are woven inline per chapter; figures live in `markdown/dm/<chapter>_images/` with raw-OCR backup in `markdown/dm/.raw/`.
- `aops-*/` — Art of Problem Solving books (03 counting & 05 number theory are load-bearing for this curriculum)
- `a-programmers-introduction-to-mathematics.pdf` / `pim/` — Jeremy Kun (programming-first math); `pim/` holds the per-chapter PDFs to OCR.
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
- `scripts/code_embed.py` — extract fenced code ↔ inline via `<!-- include: -->` directives
- `scripts/srt_to_prose.py` — turn lecture `.vtt`/`.srt` into readable prose (pause-based segmentation)
- `scripts/cleanup_ocr.py` — strip OCR page-header/footer/number artifacts from `.md`
- `markdown/` — OCR'd / authored output, mirrors source paths; images in sibling `<basename>_images/` dirs
- `code/` — code blocks extracted from markdown (`code/<book>/<chapter>/NN_<lang>.<ext>`)
- `reader/` — client-side web reader (`app.js` + KaTeX/marked/highlight.js); `serve.py` serves it locally
- `public/` — build output for Cloudflare (regenerated by `make build`; gitignored — never edit by hand)
- `lecture-videos/` — MIT 6.042J `.vtt`/`.webm` source for the `mcs-lectures` prose track
- `pim/` — Jeremy Kun *Programmer's Intro to Mathematics* chapter PDFs
- `mcs/`, `aops-*/`, `*.pdf` — Source materials (read-only)

## Authoring Reader Pages

New content lives in `markdown/<book>/<chapter>.md` and is read through `reader/`. Follow these so it renders correctly and matches existing pages:

- **Structure:** one `#` H1 title per page, `##` for sections (these populate the reader outline), prose underneath. Optimize for *the user's understanding* (see Learning Approach), not external readability.
- **Math is LaTeX, never Unicode lookalikes.** Wrap every bit of math in `$…$` (inline) or `$$…$$` (display) and write real LaTeX — `\forall`, `\leq`, `\sqrt{x}`, `\frac{a}{b}`, `\mathbb{N}`. Do **not** paste glyphs (`∀`, `≤`, `√`, `ℕ`) as a substitute for math: the reader runs KaTeX *only* inside the math delimiters, so raw glyphs get no real typesetting/spacing and drift from the rest of the book. (Plain Unicode in prose — names, heading arrows — is fine; this is about *math content*.) Supported delimiters: `$…$`, `$$…$$`, `\(…\)`, `\[…\]`.
- **Code goes in `code/`, not inline.** Put runnable snippets in `code/<book>/<chapter>/NN_<lang>.<ext>` and reference them with `<!-- include: code/... -->` (see `code_embed.py`). Start each snippet with its invocation as a comment (`# uv run --with z3-solver python`) so it stays reproducible and verifiable.
- **Figures need real captions.** Write `![Figure N: caption text](<path with spaces>)` — the reader renders non-empty alt text as a styled `<figcaption>`. OCR figures land in a sibling `<chapter>_images/` dir (the pipeline default; the reader resolves the path relative to the book `basePath`). A bare `![](path)` renders as an uncaptioned image, so always recover the caption from the source. Caption math is LaTeX (`$…$`).
- **Weave programmatic demos inline.** Put each demo's `<!-- include: code/… -->` (inside a ```` ```python ```` / ```` ```lean ```` / ```` ```dafny ```` fence) right after the theorem/example it verifies, with a sentence of narrative — not in a trailing section. Keep code lines **≤ 80 chars** so they fit the reader column without horizontal scrolling, and actually run each file before trusting it.
- **Carousels:** to group related/sequential figure panels into one swipeable widget, wrap their image lines in `<!-- carousel -->` … `<!-- endcarousel -->`. The reader turns the enclosed images into a single carousel with prev/next controls (see `buildCarousels` in `app.js`).

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

# Reader (web book) — local preview & Cloudflare deploy
make serve     # uv run reader/serve.py → http://localhost:8765/reader/
make build     # assemble ./public from reader/ + markdown/ + code/
make deploy    # build, then `wrangler deploy` (project: math-reader)

# Code embedding — keep code blocks in real files, inline for reading
uv run scripts/code_embed.py list    <markdown_file>   # preview extractable blocks
uv run scripts/code_embed.py extract <markdown_file>   # blocks → code/, leave include directives
uv run scripts/code_embed.py build   <markdown_file>   # inline includes back into the markdown

# Lecture video subtitles → prose
uv run scripts/srt_to_prose.py <file.vtt> -o out.txt
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

- **Reader renders spaced image paths now:** marked.js silently refuses image destinations containing spaces (`![](04 - Foo_images/x.jpeg)` → literal text). `app.js` `processMarkdown` auto-wraps spaced destinations in `<>` before parsing, so OCR figure paths render (this also repaired long-broken mcs/pim figures). Figures are capped at 460px and centered; `.katex-display` scrolls horizontally so wide equations don't clip.
- **`hypothesis` invocation:** property tests need `uv run --with hypothesis --with pytest pytest` — pytest must be injected into the same uv env. The bare `uv run --with hypothesis pytest` shown elsewhere fails on this machine.
- **mistralai 2.x import:** `from mistralai.client.sdk import Mistral`. Top-level `from mistralai import Mistral` does NOT work in 2.x (namespace package, no top-level `__init__.py`).
- **Mistral OCR image quality:** The API returns ~100-200px thumbnails. For real resolution, request bboxes only (`include_image_base64=False`), render pages locally with `pdftoppm` at 300 DPI, crop with `magick`. See `scripts/pdf_to_markdown.py`.
- **LaTeX is automatic in OCR:** Mistral OCR already returns equations as inline `$...$` and block `$$...$$` LaTeX in the markdown — no parameter needed. The output preserves `\frac`, `\mathbb`, `\sum`, `\cdots`, etc.
- **OCR is just-in-time, one chapter at a time:** Never OCR the full MCS textbook, never OCR a whole chapter folder, never `--all`. Process exactly the chapter the user is about to study. OCRing ahead of the learning pace builds inventory in front of the real constraint (reading/practice speed) — Goldratt violation. If you find yourself wanting to bulk-OCR, stop and pick the single next chapter instead.
- **OCR idempotency:** Each `.md` has a sibling `.manifest.json` capturing source size + model. Re-runs skip unchanged PDFs; `--force` overrides.
- **No `pip install`:** Always `uv run --with <pkg>` for one-offs, PEP 723 inline metadata for scripts. No `requirements.txt` or `.venv` in this repo.
- **elan PATH for zsh:** elan installs into `~/.profile`, which zsh doesn't source. `~/.zshrc` is patched to source `~/.elan/env`. New shells get `lean`/`lake`/`elan` automatically; existing shells need `source ~/.elan/env` once.
- **`public/` is generated:** `make build` regenerates it from `reader/`, `markdown/`, `code/`. Never edit `public/` directly — edit the sources. It's gitignored.
- **Code lives outside markdown:** Fenced code in `markdown/mcs-lectures/` is stored under `code/…` and pulled in via `<!-- include: path -->`. Edit the `code/*.py` file (so it stays runnable/verifiable), not the inlined copy — then `code_embed.py build` to re-inline.
- **Math delimiters are protected from marked.js:** `app.js` masks `$…$`/`$$…$$`/`\(…\)`/`\[…\]` before markdown parsing, then KaTeX renders them. So authored math must use those delimiters — don't HTML-escape or hand-render math, just write LaTeX between them. (This is what the recent "protect math blocks from marked.js escaping" fix set up.)
