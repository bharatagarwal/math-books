# Discrete Math Learning Plan

Stage-based plan for building formal verification skills. No time constraints - advance when you pass the gate, not when the calendar says.

## Principles

- **Constraint (Goldratt):** Identify what's actually blocking you, fix that first
- **Flow (Csikszentmihalyi):** Stay in challenge zone - stuck >20min means drop difficulty
- **Fundamentals (Lombardi):** No skipping. Each stage gates the next.
- **Calibration:** Test before advancing. If you can't pass, you're not ready.

## Skill Transfer Path

```
Discrete Math (MCS)
    │
    ├── Logic (Ch 3) ──────────────────┐
    │                                   │
    ├── Proofs (Ch 1) ─────────────────┼──▶ Lean4 / Dafny
    │                                   │         │
    ├── Induction (Ch 5) ──────────────┤         │
    │                                   │         ▼
    ├── State Machines (Ch 6) ─────────┼──▶ TLA+ / Alloy
    │                                   │         │
    └── Graph Theory (Ch 10-12) ───────┘         │
                                                  ▼
                                          Distributed Systems
                                          Verification
```

---

## Stage 0: Setup

**Goal:** Environment ready, tools working

| Task | Done when |
|------|-----------|
| Lean4 installed, Natural Number Game loads | Complete one level |
| Dafny installed | Verify a simple method compiles |
| Python env with deal, crosshair, z3, sympy | `crosshair check` runs on a sample file |

---

## Stage 1: Logic

**Goal:** Fluent in propositional and predicate logic

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 3 | Natural Number Game: Tutorial + Addition World | Translate 5 English statements to logic and back, no errors |
| | Z3: encode and solve logic puzzles | Solve a logic puzzle from scratch in Z3 |

**Calibration gate:** 5 random MCS Ch 3 problems. ≥4 correct → advance.

---

## Stage 2: Proofs

**Goal:** Can construct direct proofs, proof by contradiction, proof by cases

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 1-2 | Natural Number Game: Multiplication, Power worlds | Complete all levels without hints |
| | Lean4: prove 5 theorems from MCS | Proofs compile, you can explain each step |

**Calibration gate:** Given a theorem you haven't seen, write a valid proof (paper or Lean4) in <15 min.

---

## Stage 3: Induction

**Goal:** Strong induction is automatic, can identify inductive structure

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 5 | Natural Number Game: Induction World | All levels complete |
| AoPS 05 (Number Theory, induction sections) | Dafny: write 3 verified loops with invariants | Invariants hold, Dafny verifies |

**Calibration gate:** Prove sum of first n squares formula. Prove a property about a recursive function. Both cold, no reference.

---

## Stage 4: Counting

**Goal:** Can count without overcounting, undercounting, or handwaving

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 14-15 | Python: verify counting formulas with brute force | Formula matches brute force for n=1..10 |
| AoPS 03 (Counting) | Z3: generate edge cases for counting claims | Z3 confirms or finds counterexample |

**Calibration gate:** 10 AoPS counting problems, mixed difficulty. ≥8 correct with valid reasoning.

---

## Stage 4.5: Algorithms (Understanding-First)

**Goal:** Understand *why* algorithms work, not just memorize patterns

This stage builds algorithm foundations through understanding. Interview drilling comes later.

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 10-12 | Graph theory foundations | Can prove properties of trees, paths |
| Skiena Ch 1-2 | Problem-solving methodology | Explain his framework in your own words |
| Skiena Ch 3 (Data Structures) | Implement each with contracts in Python | Crosshair finds no violations |
| Skiena Ch 4-5 (Sorting, Search) | Implement + prove loop invariants in Dafny | Dafny verifies |
| Skiena Ch 6-7 (Graphs) | BFS, DFS, shortest path with NetworkX + contracts | Trace execution by hand, verify with code |
| Skiena "War Stories" | Read, attempt before reading solution | Can articulate *why* each approach works/fails |
| K&T (optional) | Formalize proofs in Lean4 | Pick 2-3 algorithms, prove correctness |

**Calibration gate:** 
- Given a novel problem (not from Skiena), identify which algorithm family applies and *why*
- Implement solution with contracts; Crosshair finds no edge case violations

**Your advantage:** Most people memorize patterns. You verify them. When you later do interview prep, you'll recognize *why* patterns work instead of pattern-matching blindly.

---

## Stage 5: Probability

**Goal:** Can compute probabilities, expectations; intuition matches math

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 17-19 | Python: simulate vs. calculate, compare | Simulation converges to your formula |
| AoPS 03 (Probability) | Predict outcomes before running simulation | Predictions within 5% of simulation |

**Calibration gate:** MCS probability problem set. ≥80% correct. No calculator surprises.

---

## Stage 6: State Machines & Invariants

**Goal:** Can model systems as state machines, prove invariants hold

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 6 | XState: model Die Hard water jug problem | Find winning sequence |
| | Dafny: prove invariant on a state machine | Dafny verifies |
| | Model a real protocol (mutex, leader election) | Identify invariants, verify or find bug |

**Calibration gate:** Given a new state machine spec, identify the invariant and sketch a proof.

---

## Stage 7: Number Theory

**Goal:** Modular arithmetic, GCD, primes are automatic; can prove properties

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| MCS Ch 9 | Lean4: prove GCD properties | Proofs compile |
| AoPS 05 | Python: implement extended Euclidean algorithm with contracts | Crosshair finds no violations |
| | Implement RSA from scratch | Encrypt/decrypt works, you can explain why |

**Calibration gate:** Prove Fermat's Little Theorem (Lean4 or paper). Explain RSA security to a non-expert.

---

## Stage 8: Integration & TLA+ Bridge

**Goal:** Ready for distributed systems verification

| Task | Exit Criteria |
|------|---------------|
| Model a distributed protocol in XState | Leader election or consensus |
| Identify safety vs. liveness properties | Can distinguish and articulate |
| TLA+ tutorial (Lamport video course, first 3) | Write a simple spec, model checker runs |

**Calibration gate:** Translate an XState model to TLA+. Verify an invariant with TLC model checker.

---

## Daily Rhythm

```
Fundamentals (30 min):
  - 1 drill in current stage tool (Lean4/Dafny/Z3)
  
Main session (60-90 min):
  - Read/work problems in current stage
  - Verify with tools, not answer key
  
When stuck >20 min:
  - Drop to simpler problem (stay in flow)
  - Or identify: is this a prerequisite gap? (Goldratt)
  
Before advancing:
  - Pass calibration gate
  - If fail: stay in stage, drill weak areas
```

---

## After Stage 8

You have:
- Proof fluency (Lean4)
- Invariant thinking (Dafny)  
- State machine modeling (XState → TLA+)
- Solid DM foundation
- Entry point to formal verification career track

**Next steps:**
- Hillel Wayne's "Practical TLA+"
- Pick productization lane (smart contracts, enterprise consulting, or content)

---

## Productization Paths

| Path | What you'd do | Revenue model |
|------|---------------|---------------|
| **Smart Contract Auditing** | Verify DeFi protocols won't lose funds | $50-500k per audit |
| **Formal Methods Consulting** | Verify critical systems (finance, aerospace, medical) | $200-400/hr retainers |
| **Training/Courses** | Teach engineers formal verification | Course sales, corporate training |
| **Tooling SaaS** | Make verification accessible for specific domain | Subscription |
| **Content → Authority** | YouTube/writing → book → consulting | Ad rev → book advance → $500/hr |

---

## Key Resources

### Discrete Math & Proofs
- MCS (mcs-2018-06-06.pdf) - Primary text
- AoPS 03 (Counting & Probability) - Essential
- AoPS 05 (Intro Number Theory) - Essential
- A Programmer's Introduction to Mathematics - Supplementary

### Algorithms (Understanding Phase)
- **Skiena - Algorithm Design Manual** - Primary. Problem-solving methodology, "war stories," when to use what
- **Kleinberg & Tardos - Algorithm Design** - Optional depth. Rigorous proofs, good for formalizing in Lean4
- MCS Ch 10-12 - Graph theory foundations

### Algorithms (Interview Prep Phase)
- **Beyond Cracking the Coding Interview (BCTCI)** - Pattern recognition framework, "Triggers & Boosters" methodology. Use when preparing for interviews.
- **NeetCode 150** - Timed drilling, coverage checklist. Use in final interview sprint.

### Tools
- Natural Number Game (adam.math.hhu.de) - Gamified Lean4 proofs
- Lean4 - Theorem proving
- Dafny - Program verification with invariants
- Deal + Crosshair - Python Design by Contract + symbolic execution
- Z3 - SMT solver for constraint problems
- XState - State machine modeling

### Later
- TLA+ - Distributed systems specification
- Practical TLA+ (Hillel Wayne) - Applied TLA+

---

## Interview Prep Sprint (When Needed)

When interviews are 4-6 weeks out, add this focused sprint:

| Source | Practice | Exit Criteria |
|--------|----------|---------------|
| BCTCI "Triggers" chapter | Learn pattern recognition framework | Can identify problem type in <2 min |
| NeetCode 150 - Easy | 30 problems, timed | Solve in <15 min each |
| NeetCode 150 - Medium | 50 problems, timed | Solve in <25 min each |
| Mock interviews | Pramp, interviewing.io, or friends | 3+ mocks with feedback |

**Calibration gate:** 3 random medium LeetCode, 45 min total, ≥2 optimal solutions.

Your foundation means you'll understand *why* patterns work, not just memorize them.
