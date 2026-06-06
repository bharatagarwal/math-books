# Tooling Mix: the Python stack behind the demos

Every chapter in this library leans on the same small set of Python tools. They run the inline demos, check the proofs, and translate notation into something executable. Each of them is documented well, but the good pages are scattered — an official tutorial here, a decade-old blog post there that still explains the idea better than anything written since. This mix collects the readings that are actually worth your time, in an order that builds.

The theme running through all of it: these tools are not conveniences bolted onto the mathematics. They are the method. When $\Sigma$ becomes a loop, when $\forall$ becomes a solver query, when a contract becomes a test oracle, the notation stops being something you decode and becomes something you operate.

## The substrate: uv

Everything in this repo runs through uv — no virtualenvs, no requirements files, just `uv run --with sympy python` for one-offs and a `# /// script` block for anything that lives in a file.

- [Running scripts](https://docs.astral.sh/uv/guides/scripts/) is the page that documents exactly this workflow: `uv run`, inline PEP 723 metadata, and `--with` for ad-hoc dependencies. Read it once and the repo's command lines stop looking magical.
- Simon Willison's [Building Python tools with a one-shot prompt](https://simonwillison.net/2024/Dec/19/one-shot-python-tools/) supplies the mental model — why a script that declares its own dependencies is a different kind of artifact from a project, and what that unlocks.
- [First steps](https://docs.astral.sh/uv/getting-started/first-steps/) is worth ten minutes for orientation, since uv's command surface covers scripts, tools, and projects, and it helps to know which of those you are standing in.

## Symbols that compute: sympy

SymPy is how $\frac{\partial f}{\partial x}$ and $\int f\,dx$ get checked in this library rather than trusted.

- The [introductory tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/intro.html) opens with the right framing — exact computation rather than approximate, $\sqrt{8}$ becoming $2\sqrt{2}$ — and chains into symbols, simplification, calculus, and solvers at a comfortable pace.
- [Gotchas and Pitfalls](https://docs.sympy.org/latest/tutorials/intro-tutorial/gotchas.html) is the more important read, because every early SymPy frustration comes from the same few conceptual gaps: a `Symbol` is not a Python variable, `==` is not `Eq`, and `1/2` evaluates before SymPy ever sees it.

## Index notation made honest: einsum

The repo's CLAUDE.md translates $\Sigma_i a_i b_i$ to `np.einsum('i,i->', a, b)`, and that single idea — subscript strings as executable index notation — deserves more than a reference lookup.

- Alex Riley's [basic introduction to einsum](https://ajcr.net/Basic-guide-to-einsum/) remains the gentlest way in, building the reading rules one operation at a time.
- Tim Rocktäschel's [Einsum is All You Need](https://rockt.ai/2018/04/30/einsum) is the famous one: dot products, outer products, matrix multiplication, and transposes all collapse into one uniform notation, which is precisely the experience of reading Einstein summation fluently.
- Eli Bendersky's [Understanding NumPy's einsum](https://eli.thegreenplace.net/2025/understanding-numpys-einsum/) is a careful, recent derivation of what einsum actually computes, and the [official reference](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html) is where the subscript-string grammar is spelled out exactly.

## Gradients without tears: jax

Where SymPy differentiates symbolically, JAX differentiates numerically — `grad(f)` is the $\nabla f$ of the repo's quick examples.

- The [automatic differentiation tutorial](https://docs.jax.dev/en/latest/automatic-differentiation.html) covers `jax.grad` and the composition of transformations, and is the right first page.
- [The Autodiff Cookbook](https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html) goes deeper — `jacfwd`, `jacrev`, Hessians as forward-over-reverse — and explains the machinery well enough that forward and reverse mode stop being incantations.

## Logic you can query: z3

Z3 is where $\forall x\, \exists y$ stops being philosophy. The repo uses it for predicate logic, constraints, and puzzles, and it later becomes the engine underneath CrossHair.

- The [Z3Py guide](https://ericpony.github.io/z3py-tutorial/guide-examples.htm) is the standard hands-on walkthrough: build a solver, add constraints, check, read off the model, then graduate to quantifiers.
- [Programming Z3](https://theory.stanford.edu/~nikolaj/programmingz3.html), by Z3's own authors, is the long-form treatment that connects the API to the decision procedures underneath it. Read it slowly and in pieces.
- For the conceptual question — *how does an SMT solver actually work?* — the [Beginner's Tutorial on SMT](https://hanielbarbosa.com/papers/fm2024.pdf) from FM 2024 is the best single answer, written by the people who build Z3 and cvc5.
- Philip Zucker's [Programming and Interactive Proving With Z3Py](https://www.philipzucker.com/programming-and-interactive-proving-with-z3py/) is for later, once the basics have settled and you want to see Z3 bent toward real proving.

## The verification triad: hypothesis, deal, crosshair

These three are designed here to be read as one system. Hypothesis generates inputs, deal states what must hold, and CrossHair tries to prove — symbolically, with Z3 underneath — that nothing can violate the contract.

- Start with Hillel Wayne's [Property Tests + Contracts = Integration Tests](https://www.hillelwayne.com/pbt-contracts/). It is the conceptual keystone for the whole triad: once your functions carry contracts, "no input violates any contract" becomes a property you can test for free, and your contracts become oracles.
- For Hypothesis itself, the [tutorial introduction](https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html) explains `@given`, strategies, and shrinking; the [quickstart](https://hypothesis.readthedocs.io/en/latest/quickstart.html) exists if you would rather run something within five minutes. Wayne's [Property Testing with Complex Inputs](https://www.hillelwayne.com/post/property-testing-complex-inputs/) addresses the two genuinely hard parts — finding good properties and generating structured inputs — and is the natural second read.
- Deal's [intro](https://deal.readthedocs.io/basic/intro.html) positions contracts as "typing on steroids" and walks the pre/post/invariant decorators.
- CrossHair's [introduction](https://crosshair.readthedocs.io/en/latest/introduction.html) covers the workflow, and [How Does It Work?](https://crosshair.readthedocs.io/en/latest/how_does_it_work.html) explains the trick — your function is called with symbolic values backed by Z3, so the solver explores paths your example-based tests never would.

## Graphs: networkx

NetworkX carries the graph-theory demos in the discrete mathematics chapters.

- The [official tutorial](https://networkx.org/documentation/stable/tutorial.html) covers creating graphs and applying algorithms, and is short.
- The reference [introduction](https://networkx.org/documentation/stable/reference/introduction.html) is the better conceptual read: nodes can be any hashable object, and once that design choice makes sense, the whole API follows from it.

## A suggested order

If you want a sequence rather than a shelf: read the uv pages first, since everything else runs through it. Then take sympy and einsum together — they are two answers to the same question of turning notation into computation. The z3 readings come next and do double duty, because the SMT concepts return when you reach CrossHair. Then the verification triad, anchored by the Hillel Wayne piece. JAX and NetworkX can wait until the chapters that need them — calculus and graphs respectively — which is, after all, the same just-in-time principle the Foundations Mix is built on.
