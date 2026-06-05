# Spec: Adapting *How to Solve It* in place

Status: **approved design, rewrite not yet started.** The faithful port lives in
`markdown/polya/` (17 pages, ported from `../reading/books/polya/` June 2026);
the original source remains in `../reading`. This spec governs the in-place
rewrite of `markdown/polya/`.

## Purpose

Turn the faithful port into a personal edition that serves one reader: a
software engineer learning mathematics through programming and formal
verification, who wants (a) the problem-solving methodology and (b) the
philosophical underpinnings — and does not want the 1945 classroom packaging.

## Problems with the original (the user's words)

1. Written in a slightly cardboardy, dated manner.
2. Framed around a student–teacher relationship that doesn't apply; only the
   approaches and methodology matter.
3. Examples are geometry (and similar) the reader doesn't care to get into now.

## Non-negotiable constraints

- **No AI-collaboration framing anywhere in the text.** The human–AI working
  context shapes *how the book is written for this reader*, never what the
  book says. The rewrite must function as a standalone, timeless artifact.
  Nothing that will date quickly.
- **The teacher–student frame is removed by completion, not deletion.**
  Pólya states the teacher's questions exist to be internalized as
  self-questioning. The rewrite addresses the solver directly; every
  teacher-question becomes a question the solver asks themselves. Pedagogy
  sections (how to question, imitation and practice) are recast as: how the
  questions get internalized, how solvers train themselves.
- **Pólya's ideas stay Pólya's.** This is a re-voicing and re-exampling, not a
  new book. Keep his named concepts (heuristic, plausible reasoning, the
  inventor's paradox, problems to find vs problems to prove…), his honesty
  about failure and morale, his aphoristic warmth. Modern, direct prose; no
  corporate self-help register.
- **Schoenfeld is additive, not the narrative.** See "Heuristic entries" below.
- **House authoring rules apply** (CLAUDE.md → Authoring Reader Pages): one H1
  per page, LaTeX-only math, code in `code/polya/<chapter>/` woven inline via
  `<!-- include: -->` immediately after the concept it illuminates, ≤80-char
  code lines, real figure captions, carousels for related panels.

## Voice

- Second person, direct, plain. Short sentences where Pólya wound long ones.
- Keep his best lines verbatim where they still land ("It is foolish to answer
  a question that you do not understand", the proverbs entry's material).
- Questions remain the load-bearing device — but as self-interrogation:
  "What is the unknown?" is something you ask *yourself* at the whiteboard.
- No emoji, no hype, no "in today's fast-paced world."

## Example replacement policy

Geometry worked examples go; replacements come from the reader's curriculum so
this book becomes the meta-layer of the library (cross-link other reader books
where natural):

| Original | Replacement domain |
|---|---|
| Parallelepiped diagonal (§8, §10, §12) | One worked thread reused across the phases: a counting or graph problem solved end-to-end (candidate: handshake/degree-sum, or counting subsets via bijection) |
| Construction problem (§18) | A constraint-satisfaction problem (natural z3 demo) |
| Problem to prove (§19) | An induction proof (sum of cubes — already in the book's own Induction entry — or a graph invariant), carried to Lean |
| Rate problem (§20) | A recurrence / growth problem (Fibonacci-flavored, ties to dm ch. 6) |
| Dictionary-entry mini-examples | Discrete-math or programming equivalents per entry; keep domain-neutral classics (bear puzzle, bottles) |

Rules: every replacement must genuinely exercise the same heuristic the
original example existed to teach. Each worked example gets its verification
woven in at the moment of the guess or the proof (sympy/hypothesis for the
plausible side, z3/Lean for the demonstrative side) — never a trailing code
section. Programming analogies (debugging ↔ understanding the problem, etc.)
are allowed as brief asides, not as the spine.

## Heuristic entries (the dictionary rebuild)

Each kept entry follows this internal shape:

1. **The idea** — Pólya's concept, re-voiced, with his examples replaced per
   the policy above. Leads the entry; this stays the heart.
2. **Concrete moves** — 3–6 decomposed sub-strategies (the Schoenfeld
   corrective: "solve an easier related problem" is a family — set n=1,2,3;
   drop a constraint; lower the dimension; specialize the type). Compact list.
3. **When to reach for it** — one or two lines.

Schoenfeld himself is named once: in the Monitoring & psychology group, a
short section on control/metacognition (monitoring progress, deciding to
persist vs switch — the descriptive-vs-prescriptive finding). Not a drumbeat.

## Target structure (replaces current 14-page layout)

| Page | Content | Built from (current pages) |
|---|---|---|
| 00 Preface | What this edition is, how it differs from the 1945 text, how to read it | new; absorbs Foreword/Introduction's useful matter |
| 01 The Four Phases | The method as a solver's protocol; one problem thread worked through all four phases with woven verification | 02, 03 (§1–14, classroom material recast as self-practice) |
| 02 Inside a Solution | The self-dialogue demonstrated: a solver thinking aloud through one problem from the new example set (modernized Part II) | 05 |
| 03 Understanding Moves | Dictionary group: what is the unknown / data / condition; restating; notation; figures; separating the condition; did you use all the data… | entries from 06–10 |
| 04 Plan-Finding Moves | analogy; specialization & generalization; decomposing & recombining; working backwards; auxiliary elements & problems; variation; inventor's paradox; related problems… | entries from 06–10 |
| 05 Monitoring & the Psychology of Solving | signs of progress; examine your guess; determination/hope/success; subconscious work; bright idea; + the control section (Schoenfeld named here) | entries from 06–10 |
| 06 Style & Wisdom | pedantry & mastery; rules of discovery/style/teaching→self-teaching; routine problems; the future mathematician → the developing solver; proverbs; terms old & new | entries from 06–10 |
| 07 Guessing and Proving | Closing chapter part 1, purely philosophical: demonstrative vs plausible reasoning; finished math as scrubbed guessing; Euler showing his work (π²/6 as narrative); Lakatos & proofs-refutations co-evolution; Hungarian heuristic line; the four phases as guess-then-prove made procedural | new |
| 08 The Solver's Instruments | Part 2, grounding part 1 for the programmer: economics of guessing (instruments change cost, cost changes temperament); symbolic REPL as lab bench (sums-of-cubes session); counterexample hunting as mechanized refutation (Euler's sum-of-powers conjecture as cautionary tale); OEIS as "have you seen it before?"; visual instruments as continuous specialization; proof assistant as demonstrative court — incl. the honest gap (no tool guesses the proof idea); ends pointing back at 07 | new |
| 09 Problems | Curated Part IV: keep domain-neutral classics, drop pure geometry, splice equivalents from Lovász/AoPS where they exercise a dictionary move | 11, 12, 13 (hints folded into problems or kept as a section) |
| 10 Reading Guide | Rewritten last, against the new structure | 00 |

Notes:
- Biographical entries (Bolzano, Descartes, Leibnitz, Pappus) compress into
  sidebars/asides inside the relevant thematic entry (Pappus → working
  backwards; Descartes → setting up equations/universal method).
- Entries that are pure cross-reference stubs in the original merge into
  their parents.
- `reader/app.js` book registration updated to the new page list in the same
  change; old pages deleted (git preserves the faithful port — commit it
  before the rewrite begins).

## Closing chapter sources (already researched)

- Pólya, *Mathematics and Plausible Reasoning* Vol. I preface (the
  demonstrative/plausible passage; "investigating induction inductively").
- Pólya on Euler: "He explained how he found his results… of the great
  mathematicians, the one who influenced me most."
- Lakatos, *Proofs and Refutations* (Euler characteristic story; Pólya
  suggested the topic; Lakatos translated HTSI into Hungarian).
- Schoenfeld, "Pólya, problem solving, and education" / *Mathematical Problem
  Solving* (descriptive-vs-prescriptive; control; belief systems).
- Hungarian heuristic tradition (Pólya–Lakatos–Rényi; ties to
  `docs/notes/` Hungarian-school note).

## Process (when the go-ahead comes)

1. Commit the faithful port first (baseline in git history).
2. Background workflow, one author agent per target page consuming this spec +
   the relevant faithful-port pages; adversarial review per page against this
   spec (voice, constraints, example policy, entry shape) + house authoring
   rules; fix loop.
3. All woven code actually run before inclusion; Lean/Dafny files type-checked.
4. Update `reader/app.js`, `make build`, rendered-page verification
   (screenshots assessed editorially, console/404 sweep).
5. Reading Guide rewritten last, after the rest has settled.

## Open items

- Which single problem threads the Four Phases chapter (handshake vs subset
  counting) — author's call at write time, optimizing for how naturally all
  four phases and the verification weave land on it.
- Whether Hints survive as a separate section or fold per-problem — author's
  call.
