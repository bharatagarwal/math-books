# Spec: Adapting *How to Solve It* in place

Status: **approved design, rewrite not yet started.** The faithful port lives in
`markdown/polya/` (17 pages, ported from `../reading/books/polya/` June 2026);
the original source remains in `../reading`. This spec governs the in-place
rewrite of `markdown/polya/`.

## Purpose

Turn the faithful port into a personal, low-friction edition for one reader: a
software engineer learning mathematics who wants Pólya's problem-solving
method, his psychology of discovery, and his philosophical distinction between
guessing and proving — without the 1945 classroom packaging.

The dominant design goal is readability and transfer. The rewrite should reduce
the cognitive load of reading the whole book while preserving the reusable
questions and habits that make Pólya valuable. Programming, symbolic
calculation, and formal tools may appear, but only as instruments that make an
idea easier to see. They are not the subject of the book.

## Handoff directive

This file is the handoff artifact for a new rewrite session. A new agent should
be able to start from this spec, the faithful port in `markdown/polya/`, and the
house rules in `CLAUDE.md` without needing prior conversation.

The chosen table-of-contents theme is **Conceptual Themes**. Do not revert to an
alphabetical dictionary, a classroom sequence, or a purely workflow/question-led
TOC. The reader should be able to glance at the sidebar and see the conceptual
territory of Pólya's method:

1. The Method
2. Understanding
3. Discovery
4. Variation
5. Auxiliary Problems
6. Signs of Progress
7. Plausible Reasoning
8. Proof and Review
9. Style, Judgment, and Practice
10. Problems

The page names and subheadings below are starting commitments, not decorative
labels. A writer may adjust wording while drafting, but the final structure
should keep this thematic shape.

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
- **Readability outranks instrumentation.** A worked example should first make
  the heuristic move clear to the reader. Add code, symbolic checks, brute-force
  enumeration, Z3, Lean, or other tools only when they reduce confusion,
  strengthen a natural check, or make a hidden structure visible. Do not turn
  the rewrite into a formal-verification book or an AGI/math-tools book.
- **The thematic TOC is part of the rewrite.** The current port's alphabetic
  dictionary and general part titles are hard to scan. The rewrite uses the
  Conceptual Themes table of contents from this spec, with clear page titles and
  subheadings.
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
| Parallelepiped diagonal (§8, §10, §12) | One worked thread reused across the phases: preferably counting subsets by binary strings; handshake/degree-sum is the backup |
| Construction problem (§18) | A small constraint or arrangement problem solved by hand first; Z3 only if it clarifies the same reasoning |
| Problem to prove (§19) | An induction proof (sum of cubes — already in the book's own Induction entry — or a graph invariant); Lean is optional, not the point |
| Rate problem (§20) | A recurrence / growth problem (Fibonacci-flavored, ties to dm ch. 6) |
| Dictionary-entry mini-examples | Discrete-math or programming equivalents per entry; keep domain-neutral classics (bear puzzle, bottles) |

Rules: every replacement must genuinely exercise the same heuristic the
original example existed to teach. Each worked example should include a natural
check at the moment the guess, plan, or proof appears. That check may be mental,
numerical, diagrammatic, small-case enumeration, symbolic calculation,
property-based testing, Z3, Lean, or another tool. Use the lightest check that
helps the reader. Never add a trailing "code section" merely to satisfy the
tooling habit. Programming analogies (debugging ↔ understanding the problem,
etc.) are allowed as brief asides, not as the spine.

The recurring four-phase example should be deliberately low-overhead. Counting
subsets by binary strings is the current preferred thread because it naturally
supports: identifying unknown/data/condition; choosing notation; solving small
cases; finding an auxiliary representation; checking by enumeration; proving by
bijection or induction; and looking back to reuse the method.

## Heuristic entries (the dictionary rebuild)

Each kept entry follows this internal shape:

1. **The idea** — Pólya's concept, re-voiced, with his examples replaced per
   the policy above. Leads the entry; this stays the heart.
2. **Concrete moves** — 3–6 decomposed sub-strategies (the Schoenfeld
   corrective: "solve an easier related problem" is a family — set n=1,2,3;
   drop a constraint; lower the dimension; specialize the type). Compact list.
3. **When to reach for it** — one or two lines.
4. **Questions to keep** — 2–4 reusable self-questions, when the entry is long
   enough to need them. These are the main cognitive-load reducers.

Schoenfeld himself is named once: in the Monitoring & psychology group, a
short section on control/metacognition (monitoring progress, deciding to
persist vs switch — the descriptive-vs-prescriptive finding). Not a drumbeat.

## Target structure (replaces current 17-page layout)

Use these page titles in `reader/app.js` and these filenames in
`markdown/polya/`.

| Page file | Reader title | Job | Suggested subheadings | Built from |
|---|---|---|---|---|
| `00 - The Method.md` | The Method | Introduce the edition, the four phases, and the recurring problem thread. This replaces a separate preface/reading-guide page. | What this edition is; The four phases; The questions are the method; The recurring example; How to read this edition | 01, 02, 03, 04, 05, 06 |
| `01 - Understanding.md` | Understanding | Make the first phase concrete: before solving, make the problem graspable. | Start from the statement; Unknown, data, condition; Problems to find vs problems to prove; Restating and definitions; Notation and figures; Is the condition possible?; Questions to keep | 02, 05, 06, 08, 10, 11, 12, 13 |
| `02 - Discovery.md` | Discovery | Explain how ideas are found: memory, analogy, the unknown, and the first useful plan. | Look at the unknown; Have you seen it before?; Related problems and theorems; Analogy; Generalization; Specialization; The bright idea; Questions to keep | 06, 07, 09, 10, 11, 12, 13 |
| `03 - Variation.md` | Variation | Show how to change the problem when the direct attack stalls. This is a central chapter, not a side tactic. | Change the problem deliberately; Drop part of the condition; Keep the unknown and change the rest; Keep the data and derive something useful; Extreme cases; The inventor's paradox; Questions to keep | 07, 09, 10, 11, 12, 13 |
| `04 - Auxiliary Problems.md` | Auxiliary Problems | Teach the main indirect route: solve another problem, introduce another object, or work backwards. | Why auxiliary problems help; Auxiliary elements; Auxiliary unknowns and lemmas; Equivalent reductions; Working backwards and Pappus; When the detour is worth it; Questions to keep | 06, 07, 09, 10, 11, 12, 13 |
| `05 - Signs of Progress.md` | Signs of Progress | Give the reader a way to monitor whether work is moving, stalling, or drifting. | What progress feels like; Clear signs; Misleading signs; Examine your guess; Persist, switch, or rest; Subconscious work; Questions to keep | 08, 10, 11, 12, 13 |
| `06 - Plausible Reasoning.md` | Plausible Reasoning | Preserve Pólya's philosophical core: guessing is not proof, but it is how discovery starts. | Heuristic reasoning; Induction before proof; Analogy as evidence; Why plausible is not certain; Euler showing his work; Lakatos and proofs/refutations; Questions to keep | 09, 10, 11, 12, 13 plus researched sources |
| `07 - Proof and Review.md` | Proof and Review | Connect carrying out, proving, checking, and looking back. | Carrying out the plan; Can you see it? Can you prove it?; Problems to prove; Mathematical induction; Reductio and indirect proof; Check the result; Derive it differently; Use the result elsewhere; Questions to keep | 02, 06, 07, 10, 11, 12, 13 |
| `08 - Style Judgment and Practice.md` | Style, Judgment, and Practice | Recast the wisdom and pedagogy entries as self-training for a solver. | Pedantry and mastery; Rules of discovery; Rules of style; Routine problems; The developing solver; Proverbs worth keeping; Training the self-dialogue; Questions to keep | 05, 08, 11, 12, 13 |
| `09 - Problems.md` | Problems | Curate practice around the new thematic chapters. Keep problems that exercise a named move; remove pure geometry unless it is unusually clarifying. | How to use these problems; Problems by heuristic move; First hints; Solutions or solution sketches; Where each problem points back | 14, 15, 16 plus selected replacements from Lovász/AoPS |

Notes:
- The four phases remain the spine inside the thematic TOC. Every major page
  should make clear which part of the solver's protocol it strengthens.
- Do not create a standalone `Reading Guide` unless the rewrite unexpectedly
  needs it. Fold the "how to read this edition" material into `00 - The
  Method.md`.
- Do not create a standalone "Solver's Instruments" chapter by default. Fold
  tool notes into the relevant examples: small-case search in Discovery or
  Variation, symbolic scratch work in Plausible Reasoning, formal checking in
  Proof and Review.
- Long pages should end with a compact "questions to keep" recap. The goal is
  not to summarize content for its own sake, but to leave the reader with the
  next question to ask when stuck.
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

1. Preserve the faithful port first. If it is not already committed, stop and
   commit it or ask the user before deleting/replacing pages.
2. Draft against the thematic TOC in this spec. Do not preserve the old
   alphabetical dictionary as a reader-facing structure.
3. For each page: read the source pages listed in "Built from"; extract the
   Pólya ideas; choose or adapt examples that exercise the same heuristic; write
   in second person; end with "Questions to keep" when the page is long enough.
4. Use subset-counting by binary strings as the default recurring example
   across `00 - The Method.md` and the early chapters. Switch to
   handshake/degree-sum only if the prose is clearly better after drafting.
5. Keep code optional. Any woven code actually run before inclusion; any formal
   proof files type-checked. Unchecked code is not allowed.
6. Fold tool notes into relevant pages by default. Do not create extra chapters
   unless the existing thematic TOC demonstrably cannot hold the material.
7. Update `reader/app.js` to the 10-page thematic TOC, delete old pages only
   after the new pages exist, run `make build`, and verify rendered pages
   editorially: screenshots, console/404 sweep, math/figure/code readability.

## Defaults for the rewrite

- TOC: use the **Conceptual Themes** structure exactly unless drafting exposes a
  concrete readability failure.
- Recurring example: subset-counting by binary strings.
- Reading guide: folded into `00 - The Method.md`.
- Solver instruments: folded into examples, not standalone.
- Hints and solutions: fold hints into `09 - Problems.md` unless separate
  sections make the practice page easier to use.
