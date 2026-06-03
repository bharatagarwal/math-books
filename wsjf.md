# AGI-Proof WSJF Math Curriculum

A prioritized backlog for the math you actually need to build and understand AGI
systems — ranked by **WSJF**[^wsjf] so the highest-leverage, lowest-effort
concepts get learned first, and the brutal-but-niche ones get deferred.

## How the Score Works

`WSJF = Value ÷ Job Size`, and the highest score is executed first.

| Metric | Scale | The question it answers |
| :-- | :-: | :-- |
| **Value** — cost of delay | 1–10 | If I don't know this, how badly does it block building/understanding AGI architectures (RL, World Models, JEPAs, Neurosymbolic AI)? |
| **Job Size** — cognitive load | 1–10 | How long to gain a *programmatic, structural* intuition of the concept (ignoring manual calculation)? |
| **WSJF** | Value ÷ Job Size | The priority score — **highest is executed first**. |

## The Backlog, Ranked

| Rank | Concept | Tier | Value | Job Size | WSJF |
| --: | :-- | :-: | --: | --: | --: |
| 1 | Matrices as spatial transforms & change of basis | T1 | 10 | 2 | **5.00** |
| 2 | Graph theory: DAGs, adjacency matrices & tree search | T1 | 9 | 2 | **4.50** |
| 3 | Markov chains & MDPs | T1 | 10 | 3 | **3.33** |
| 4 | Expected value, marginal & conditional probability | T1 | 9 | 3 | **3.00** |
| 5 | Eigenvectors, eigenvalues & the characteristic equation | T1 | 9 | 3 | **3.00** |
| 6 | Jacobian matrix & vector gradients | T2 | 10 | 5 | **2.00** |
| 7 | Dynamical systems & continuous control theory | T2 | 9 | 5 | **1.80** |
| 8 | Recurrence relations & state machines (DFA/NFA) | T2 | 7 | 4 | **1.75** |
| 9 | Singular Value Decomposition (SVD) | T3 | 7 | 5 | **1.40** |
| 10 | Lagrange multipliers & constrained optimization | T3 | 6 | 5 | **1.20** |
| 11 | Jordan canonical forms & matrix exponentials | T3 | 7 | 6 | **1.17** |
| 12 | Kullback–Leibler (KL) divergence | T3 | 6 | 6 | **1.00** |

---

## Tier 1 — The Trunk

> [!TIP]
> Massive architectural value at low cognitive job size. **Do not JIT[^jit]
> these.** Hardwire them into your L1 cache through visual and programmatic
> learning.

### 1. Matrices as Spatial Transformations & Change of Basis
**WSJF 5.00** · Value 10 · Job Size 2

- **Why it matters:** the foundational intuition for *latent space* (JEPAs) and neural embeddings.
- **Source:** [3Blue1Brown — *Essence of Linear Algebra*][3b1b] (Ch. 1–4, 13); code it in `NumPy`.

### 2. Graph Theory: DAGs, Adjacency Matrices & Tree Search
**WSJF 4.50** · Value 9 · Job Size 2

- **Why it matters:** `DSPy` pipelines, Neurosymbolic logic routing, Monte Carlo Tree Search (System 2 reasoning).
- **Source:** [A Programmer's Introduction to Mathematics][pim] (Jeremy Kun); MIT *Mathematics for Computer Science* (6.042).

### 3. Markov Chains & Markov Decision Processes (MDPs)
**WSJF 3.33** · Value 10 · Job Size 3

- **Why it matters:** the absolute bedrock of all Reinforcement Learning (Q-learning, PPO) and agentic environments.
- **Source:** Bertsekas, *Introduction to Probability*; [Mathematics for Machine Learning][mml] (Deisenroth).

### 4. Expected Value, Marginal & Conditional Probability
**WSJF 3.00** · Value 9 · Job Size 3

- **Why it matters:** how an AGI updates its "belief" about the world from new telemetry (Bayesian updating in World Models).
- **Source:** Bertsekas, *Introduction to Probability*.

### 5. Eigenvectors, Eigenvalues & the Characteristic Equation
**WSJF 3.00** · Value 9 · Job Size 3

- **Why it matters:** dimensionality reduction, axes of invariance in World Models, and the foundation of State Space Models.
- **Source:** [3Blue1Brown][3b1b] (Ch. 14); [Mathematics for Machine Learning][mml].

---

## Tier 2 — The Heavy Compute

> [!NOTE]
> Critical for AGI, but the cognitive job size is heavier. Run the
> **MLFQ[^mlfq]** method: grab the intuition, and if you bog down, demote the
> deep theory to background processing and move on.

### 6. The Jacobian Matrix & Vector Gradients
**WSJF 2.00** · Value 10 · Job Size 5

- **Why it matters:** the mathematics of backpropagation — how an error at the end of a system updates a weight at the beginning.
- **Source:** [Mathematics for Machine Learning][mml] (calculus chapters).

### 7. Dynamical Systems & Continuous Control Theory
**WSJF 1.80** · Value 9 · Job Size 5

- **Why it matters:** the cheat code for the next 5 years of AI — how V-JEPA models physics and how Mamba (SSMs) models continuous sequences.
- **Source:** Steve Brunton (UW) — *Control Bootcamp* / *Dynamical Systems* (YouTube).

### 8. Recurrence Relations & State Machines (DFA/NFA)
**WSJF 1.75** · Value 7 · Job Size 4

- **Why it matters:** Neurosymbolic loops, autonomous agent planning, and RNN/SSM memory mechanisms.
- **Source:** MIT *Mathematics for Computer Science* (6.042).

---

## Tier 3 — The Leaves

> [!CAUTION]
> Either highly specific (low general value) or mathematically brutal (high job
> size). **Do not study these proactively.** Wait until an interrupt — a
> research paper or a `PyTorch` error — forces the issue, then use an LLM as a
> ZPD[^zpd] tutor to translate the math into Python.

### 9. Singular Value Decomposition (SVD)
**WSJF 1.40** · Value 7 · Job Size 5

- **Why it matters:** feature extraction, PCA, and compressing latent spaces.
- **JIT trigger:** reach for [3Blue1Brown][3b1b] or an LLM *only* when you actually need to compress a matrix or model.

### 10. Lagrange Multipliers & Constrained Optimization
**WSJF 1.20** · Value 6 · Job Size 5

- **Why it matters:** used in RL (TRPO / PPO) to keep the policy from updating too drastically.
- **JIT trigger:** prompt an LLM when you are explicitly coding an RL loss function.

### 11. Jordan Canonical Forms & Matrix Exponentials
**WSJF 1.17** · Value 7 · Job Size 6

- **Why it matters:** discretizing continuous-time differential equations — the core math of Mamba/SSMs.
- **JIT trigger:** *strictly* when implementing a State Space Model from scratch.

### 12. The Kullback–Leibler (KL) Divergence
**WSJF 1.00** · Value 6 · Job Size 6

- **Why it matters:** measures the difference between two probability distributions (used heavily in RL and VAEs).
- **JIT trigger:** prompt an LLM —
  > Write a Python script that calculates the KL divergence between these two arrays and explain it to me.

---

## The Operating Protocol

How to run this OS.

### Phase 1 · Boot Sequence (Weeks 1–3)
Clear all other learning and spend 100% of your CPU cycles on **Tier 1**. Don't
read textbooks passively — write Python to *prove* you understand each node.

- [ ] Code a Markov chain / MDP and watch it converge
- [ ] Compute eigenvectors and visualize a change of basis in `NumPy`
- [ ] Build adjacency-matrix graph search and a small tree search
- [ ] Simulate expected value and conditional probability from samples

### Phase 2 · Process Spawning (Weeks 4+)
Start building AGI-aligned projects.

- [ ] Build a basic Monte Carlo Tree Search
- [ ] Build a simple `DSPy` pipeline
- [ ] Code a rudimentary physics predictor

### Phase 3 · Interrupt Handling (Continuous)
When a project hits a math wall (a Tier 3 concept), halt and hand it to a
frontier LLM (Opus 4.8 / GPT-5.4 / o1) with the ZPD[^zpd] prompt:

> [!IMPORTANT]
> Translate the interrupt into code and anchor it to something you already
> know — don't try to absorb the full theory cold.

```text
I am an AI Systems Engineer. I have hit a hardware interrupt on [Concept].
Translate this math into a Python implementation. Map it to my existing
knowledge of [Tier 1 Concept]. Give me a 10-line coding challenge to clear
the interrupt.
```

---

> You have the architecture background, the backend engineering skills, and now
> the cognitive OS. You don't need to go back to school. You just need to
> **compile the Trunk, and JIT the rest.**

[^wsjf]: **Weighted Shortest Job First** — a Scaled Agile prioritization method that ranks work by Cost of Delay ÷ Job Size, so the highest value-per-effort items run first.
[^jit]: **Just-In-Time** — learn a concept only when a project actually forces the need, instead of studying it ahead of time.
[^mlfq]: **Multi-Level Feedback Queue** — an OS scheduler that demotes long-running jobs to lower-priority queues; here, demote deep theory to "background" until a project needs it.
[^zpd]: **Zone of Proximal Development** — Vygotsky's band of skills just beyond your current reach that become learnable with guidance (here, a frontier LLM as tutor).

[3b1b]: https://www.3blue1brown.com/topics/linear-algebra
[mml]: https://mml-book.github.io
[pim]: https://pimbook.org
