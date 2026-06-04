# The fork: formal verification career vs AGI engineering

The two curriculum docs point at different destinations. `docs/learning-plan.md`
(older) is a stage-gated path toward formal verification → distributed systems
(TLA+), ending in formal-methods consulting / auditing. `wsjf.md` (recent) is a
WSJF-ranked backlog toward AGI/ML systems math. They share a methodology
(throughput thinking, verify-with-code, fundamentals for the trunk) but not a
syllabus: overlap is ~30% (graphs, probability, state machines); the divergent
buys are proof fluency (Lean) vs linear algebra + calculus intuition.

**Decision: deferred.** Focus on shared foundations; revisit when the deep buys
would start (Lean gate-grinding vs PyTorch/infra projects).

## How the paths differ structurally

| | Formal verification | AGI engineering |
| :-- | :-- | :-- |
| Daily work | Specs, invariants, protocol models, proofs, audits | Implement papers, training/eval infra, debug training dynamics |
| Role of math | Math **is the deliverable** | Math is load-bearing intuition; you read it and translate to code |
| Fluency type | **Generative** — construct proofs cold | **Receptive** — read and implement |
| Non-math stack | Lean/Dafny/TLA+/Z3 + one domain (EVM, RTL, protocols) | PyTorch, CUDA, distributed training, evals — large, churning |
| Market | Thin: hardware FV teams (biggest employer), AWS/MS, seL4/aerospace, crypto audits (cooled since 2022), consulting | Enormous, crowded; the market pulls |
| Skill half-life | Very long (TLA+ stable for a decade; Lean growing) | Short (~18-month churn) |

The generative-vs-receptive row is the structural difference. Producing proofs
is the slower, deeper skill even when the material feels familiar.

## Which is more work (priced against my assets)

Transferable asset: backend / distributed-systems engineering.

- **FV:** distributed-systems knowledge helps the fun part (TLA+ modeling) but
  not the long pole — proof fluency plus the last mile of a thin market
  (portfolio audits, reputation, few seats). Getting *paid* is a separate
  project from getting *good*. Learning plan's own gates imply 2–3+ years
  part-time before productization even starts.
- **AGI:** training/agent infra *is* distributed systems — skills convert at a
  high rate; the new math (wsjf Tiers 1–2) needs only structural intuition,
  which the programmatic methodology acquires fast; day-job synergy compounds.

Verdict: **FV is probably more total work to a paycheck despite the
friendlier-feeling math** — proof fluency is the slow skill, the thin market
makes skilled→paid expensive, and my assets discount the easy parts of FV but
the hard parts of AGI engineering.

## The familiarity signal, decomposed

Discrete math feels like home (induction = recursion, propositions = types,
invariants = loop reasoning). Two components:

1. **Legitimate:** lower Job Size for a programmer is a real WSJF input.
2. **Distortion:** familiarity shrinks the perceived denominator only for the
   branch I already like, and says nothing about the Value column. Familiar
   *flavor* ≠ possessed *skill* — I don't have proof fluency yet; it just looks
   like my neighborhood. In Flow terms, "feels familiar" can mean "below the
   challenge zone."

Corrected rubric: hold Job Size honest, decide on Value (cost of delay, what
compounds with my work, which thesis I believe).

## AI-era thesis of each

- **FV:** as AI generates more code, verification of generated artifacts
  becomes the scarce good; specification is the durable human skill; Lean+LLM
  (AlphaProof, proof copilots) is a hot intersection. Counterpoint: AI automates
  proof labor too — what survives is spec-writing and modeling judgment.
- **AGI:** be where capability is built; fastest compounding, biggest market.
  Counterpoint: most crowded trade in tech; the stack churns underneath.
- They **converge at the frontier**: neurosymbolic systems (wsjf already lists
  this), verified agent infrastructure, safeguarded AI, automated reasoning +
  GenAI. The fork is real at the base, less than total at the top.

## Practical upshot (Goldratt)

The current constraint is the same either way: foundations. At this stage the
curricula overlap more than the destinations do. Hold both cheap scouting
positions — MCS proofs via the reader, wsjf Tier 1 linear algebra (Job Size 2) —
and let contact with each tell which generates pull. The fork only gets
expensive at the deep buys; that's the decision point.
