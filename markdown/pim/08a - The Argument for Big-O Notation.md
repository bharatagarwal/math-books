# The Argument for Big-O Notation

> [Big-O notation] significantly simplifies calculations because it allows us to be sloppy—but in a satisfactorily controlled way. […] The extra time needed to introduce $O$ notation is amply repaid by the simplifications that occur later.
>
> – Donald Knuth

Big-O notation is a common plight of programmers seeking a job at a top-tier software company. It can feel extremely unfair to be rejected from a job for not being able to rattle off the big-O runtime of an algorithm, despite being able to implement that algorithm on the spot on a whiteboard. It's a loathsome feeling conspicuously detached from the job.

As we've discussed, the bulk of software is bookkeeping, moving and reshaping data to adhere to APIs of various specifications, and doing this in a way that's easy to extend and maintain. The ever-present specter of software is the fickle user who thinks they know what they want, only to change their mind when you finish implementing it. Big-O analysis doesn't seem to play a part in that struggle.

One should try to see the other side of the coin as well. Often an interviewer doesn't particularly care about the exact big-O runtime of an algorithm. They aren't testing your aptitude to recall arbitrary facts and do algebra. They care that you can reason about the behavior of the thing you just wrote on the whiteboard. As we all know, beyond correctness, an important part of software is anticipating how things will break in subtler ways. What kind of data will make the system hog memory? For what sort of usage will a system thrash? Can you guarantee there are no deadlocks? Most importantly, can you be concrete in your analysis?

Among the simplest things one could possibly ask is what part of the algorithm you just wrote is the bottleneck at scale. To do that, you have to walk a fine line between being precise and vague. Define the quantities of interest—whether they're joins in a database query or sending data across a network—and the simplifying assumptions that make it possible to discuss in principle. You also have to sweep an immense amount of complexity under the rug. Maybe you'll ignore problems that could occur due to multithreading, or the overhead of stack frame management incurred by splitting code into functions in just such a way, or even ignore the *benefits* of helpful compiler optimizations and memory locality, when the application doesn't depend on it.

In dealing with this, we weigh the consequences of a double-edged sword. Be too precise and you drown in a sea of details. It becomes impossible to have a discussion with principled arguments and reasonable conclusions. On the other hand, be too vague and you risk invalid conclusions, leading to wasted work and worse software. Like we did with waves on a string in Chapter 12, even if we know we're ignoring certain details, we want to understand the dominant behavior of the system—the aspects we care about—while ignoring the complexities that prevent us from gaining a deeper understanding.

Few tools in computer science help one balance on the tightrope. We have experimental measurements, tests against historical data, and monitoring on live data. But these are tools designed for incrementalism. For most big decisions, such as designing a new database, data structure, operating system, or a truly novel product—as companies like Google, Amazon, Facebook, and Microsoft have done many times—the investment required for a redesign requires strong and principled justification. No users exist yet, nor does any usage data.

Mathematics provides an abstraction that helps one, as Knuth says, be sloppy in a precisely controlled way. The abstraction is big-O notation, along with its cousins little-o, big-$\Omega$ and little-$\omega$, and big-$\Theta$.[^omega] Together they are called *asymptotic notation*. Big-O notation is a language in which to phrase tradeoffs, compare critical resource usage, and measure things that scale.

[^omega]: $\Omega$ is the Greek capital letter Omega, $\omega$ is lower-case omega, and $\Theta$ is the capital Theta.

The key word in that description is *language*. Big-O is a piece of technical mathematics specifically designed to make conversation between humans about messy math easier. It fits that description more obviously and shamelessly than any other bit of math I know. And it's not just about runtime. You can use big-O and its relatives to describe the usage of any constrained resource, be it runtime, space, queries, collisions, errors, or bits sent to a satellite.

Of course, like any tool big-O is not a panacea. Often one needs to peek behind the curtain and optimize at a granular level. Customer attention is a matter of milliseconds. In time-critical engines like text editors and video games, frame rate and response latency are the bottom line. But big-O has the advantage of being able to fit entirely inside your head, unlike tables of measurements. As a language aid, a first approximation, and a start to a conversation, big-O is hard to beat.

So in this short chapter I'll introduce big-O notation, describe some of its history, show how it simplifies some of the calculations in this book, and then describe some of my favorite places where big-O takes center stage.

### History and Definition

The original use of big-O notation was by Landau and Bachmann in the 1890's for approximating the accuracy of function approximations at a point. The $O$ notation was chosen because $O$ stands for "Order" (more precisely, the German *Ordnung*). Big-O notation is meant to replace an expression with its order of magnitude. It was a particularly popular notation in number theory. It was not until mid-century 1900's that big-O found its way to computer science, in part because computer science had to be invented. Donald Knuth opens a 1976 essay with, "Most of us have gotten accustomed to [big-O notation]," and goes on to formalize it and introduce lower-bound analogues.

For understanding function approximations, big-O is relevant to Taylor series. In the language of big-O, $\sin(x)$ being well approximated by $x$ near $x=0$ is phrased as

$$\sin(x)=x+O(x^{3})$$

To explain what this means, recall that the Taylor series for $\sin(x)$ at $x=0$ is

$$\sin(x)=x-\frac{x^{3}}{3!}+\frac{x^{5}}{5!}-\frac{x^{7}}{7!}+\frac{x^{9}}{9!}-\cdots$$

Big-O says the $x^{3}$ terms and smaller are dominated by the $x$ term. What's unspoken here is what "dominates" means. In the analysis of algorithms, "dominates" usually means an upper bound as the size of the input grows larger. But here nothing is growing! Instead, here the big-O notation implies a limit $x\to 0$. I.e., when $x$ shrinks, $x^{3}$ vanishes much faster than $x$. The formal definition is as a limit.

**Definition 15.1.** Let $a\in\mathbb{R}$ and let $f,g:\mathbb{R}\to\mathbb{R}$ be two functions with $g(x)\neq 0$ on some interval around $a$. We say $f(x)=O(g(x))$ as $x\to a$ if the limit of their ratios does not diverge.

$$\lim_{x\to a}\left|\frac{f(x)}{g(x)}\right|<\infty$$

The limit notation needs a disambiguation. We're not saying that the limit has to exist. We simply need that the limit does not grow without bound. So when we say $f=O(g)$, we mean that $g$ is a sort of upper bound on $f$ under some limit. Usually the limit point $a$ is established once at the beginning of a discussion, or obvious from context (e.g., you're doing a Taylor series at $a$). In the rare cases one needs to disambiguate, one can use $O_{x\to a}(g(x))$.

Unpacking this definition a bit, consider the special case when the limit exists and is finite. Then there is some constant $C$ for which

$$\lim_{x\to a}\left|\frac{f(x)}{g(x)}\right|=C,$$

and so there is some interval around $a$ so that $|f(x)|\leq(C+1)|g(x)|$. Indeed, $|f(x)|\leq D|g(x)|$ for some constant $D$, so long as $x$ is near the point of interest.

This notation satisfies some straightforward properties that allows one to do algebra with big-O quantities. Their proofs are straightforward from Definition 15.1 and standard properties of limits. In each of these, assume that the expressions inside the big-O are nonzero on some interval around $a$.

1. $f=O(f)$ for any $f$.
2. If $f_{1}=O(g_{1})$ and $f_{2}=O(g_{2})$, then $f_{1}f_{2}=O(g_{1}g_{2})$.
3. If $f_{1}=O(g_{1})$ and $f_{2}=O(g_{2})$, then $f_{1}+f_{2}=O(g_{1}+g_{2})$.
4. $f+f=O(f)$, and moreover $Cf=O(f)$ for any constant $C$.

Take care, because when we say $f=O(g)$, the symbol $=$ doesn't mean equals in the usual sense. For example, it's not symmetric or transitive; $x^{3}=O(x)$ and $x^{2}=O(x)$ as $x\to 0$, but $x^{3}\neq x^{2}$. When someone uses big-O notation like $f=O(g)$, it's best to read $=$ as "is," and then the sentence makes sense: "$f$ is (at most) order of $g$." Moreover, when we include $O(g(x))$ in the context of some larger expression, like $\sin(x)=x+O(x^{3})$, what we mean is that $\sin(x)=x+f(x)$ for some $f(x)=O(x^{3})$. Fluent use of big-O involves "native support" for this implicit association in your head, which can take to get used to.

Continuing with the example of $\sin(x)$, say we wanted an estimate of $\sin(x)\sqrt{1+x^{2}}$. Recall from the "Application: Waves" section that the Taylor series for $\sqrt{1+x^{2}}$ is

$$\sqrt{1+x^{2}}=1+\frac{x^{2}}{2}-\frac{x^{4}}{8}+\frac{x^{6}}{16}-\cdots$$

The generic $n$-th term of $\sqrt{1+x^{2}}$ is not that easy to write down, so we won't. But we just want to compute an approximation of the product $\sin(x)\sqrt{1+x^{2}}$ near zero. One thing we could do is compute the Taylor series of the entire thing by hand, computing derivatives for every term. Quite laborious! Another thing we could do is try to reason about the infinite product of their Taylor series. That would still be a lot of work, and without extra prior knowledge, we might question whether it's valid to take a term-by-term product of two infinite series.

Big-O can help. If we decide in advance how many terms we care about, then we can truncate the two series with big-O and we're left with a finite product. Note that if these next computations look strange, it's probably because you're used to seeing big-O as an infinite limit, whereas the big-O used here is a limit as $x\to 0$. In this context, $x^{5}=O(x^{3})$. We'll see the "usual" version of big-O shortly.

$$\begin{aligned}
\sin(x) &=x+O(x^{3}), \\
\sqrt{1+x^{2}} &=1+O(x^{2}), \\
\sin(x)\sqrt{1+x^{2}} &=(x+O(x^{3}))(1+O(x^{2})) \\
&=x+O(x^{3})+x\cdot O(x^{2})+O(x^{3})O(x^{2}) \\
&=x+O(x^{3})+O(x^{3})+O(x^{3}) \\
&=x+O(x^{3})
\end{aligned}$$

In particular, this makes rigorous the idea that "($x+$ something small), multiplied by ($1+$ something small), is still ($x+$ something small)." It's the kind of reasoning that one sees in physics books all the time, but instead of using the mathematically valid big-O, they say "we'll ignore this term" or "assume this term is zero." Being sloppy in this uncontrolled way can result in unforeseeable errors. Missing error terms can get combined in ways that the combination of the error is of the same order of magnitude as the term you care about. With big-O, error terms are still present, but they're present in a way that doesn't complicate calculations too much more. When two terms get combined, you're forced to ask if the combined error is too big. The interface helps prevent careless mistakes. Following one of the major themes of this book, it reduces both the cognitive load of doing algebra, and the cognitive load of keeping track of error terms.

We can extend this notation to infinite limits:

**Definition 15.2.** Let $f,g:\mathbb{R}\to\mathbb{R}$ be two functions with $g(x)\neq 0$ for all sufficiently large $x$. We say $f(x)=O(g(x))$ as $x\to\infty$ if the limit of their ratios does not diverge.

$$\lim_{x\to\infty}\left|\frac{f(x)}{g(x)}\right|<\infty$$

With the infinite limit, we're saying $|f(x)|\leq D|g(x)|$ for all sufficiently large $x$ and some constant $D$. Here and elsewhere in math, "sufficiently large" abbreviates the claim that some $N$ exists, above which ($x>N$) the property is always true.

Definitions 15.1 and 15.2 have the same name because they satisfy the same properties. However, the hypotheses of these properties are different. For example, $x^{2}=O_{x\to 0}(x)$ and $x^{3}=O_{x\to 0}(x)$, implying $x^{2}+x^{3}=O_{x\to 0}(x)$. But for infinite limits, $x^{2}\neq O_{x\to\infty}(x)$ and $x^{3}\neq O_{x\to\infty}(x)$. Instead, $x^{2}=O_{x\to\infty}(x^{3})$, $x^{3}=O_{x\to\infty}(x^{3})$, and so $x^{2}+x^{3}=O_{x\to\infty}(x^{3})$.

### Little-o, Omega, and Theta

There is one other important asymptotic notation known as little-o notation. If big-O is phrased as "less than or equal to," then little-o is "much less than." Formally, instead of the defining limit being finite, for little-o the defining limit is zero.

**Definition 15.3.** Let $f,g:\mathbb{R}\to\mathbb{R}$ be two functions with $g(x)\neq 0$ for all $x$ sufficiently close to $a\in\mathbb{R}$. We say $f(x)=o(g(x))$ as $x\to a$ if the limit of their ratios is zero.

$$\lim_{x\to a}\left|\frac{f(x)}{g(x)}\right|=0$$

We allow $a=\infty$, in which case the nonzero condition is again "sufficiently large" instead of "sufficiently close to $a$."

In other words, the function $f(x)$ vanishes compared to $g(x)$. So while $2x^{3}=O(x^{3})$ as $x\to\infty$, it's not $o(x^{3})$. Little-o requires something smaller, for example $x^{2}=o(x^{3})$. Shaving off any sufficiently large-growing function can also be the difference between big-O and little-o. In particular, as $x\to\infty$ it's true that $x=o(x\log x)$ and even $x=o(x\log(\log(\log(x))))$.

The rest of the asymptotic notation family is defined by relation to big-O and little-o.

**Definition 15.4.** Let $f,g$ be functions as before, with both nonzero on some interval around $a$.

- Define $f=\Omega(g)$ if $g=O(f)$. This is a big-O "lower bound."
- Define $f=\omega(g)$ if $g=o(f)$. This is a little-o "lower bound."
- Define $f=\Theta(g)$ if $f=O(g)$ and $g=O(f)$. This is an asymptotic "equality."

Little-o in particular has some nice uses simplifying calculus. In particular, we can define the derivative entirely in terms of $O$ notation. Donald Knuth is a champion of this approach.

**Definition 15.5.** Let $f(x)$ be a function. We say that $f'(x)$ is the derivative of $f$ if (for a parameter $\varepsilon\to 0$)

$$f(x+\varepsilon)=f(x)+f'(x)\varepsilon+o(\varepsilon)$$

As an exercise, prove that this is a restatement of the usual definition of the derivative as a limit.

Part of what makes this version of the derivative definition so elegant is that it puts the core idea of derivatives—that we care about a linear approximator—front and center. The function $f$ is literally approximated by a linear map $\varepsilon\mapsto f'(x)\varepsilon$ in the formula. All of the cruft about limits is now hidden by the $O$ notation. As an example of its usage, the derivative of $x^{2}$ is computed to be $2x$:

$$(x+\varepsilon)^{2}=x^{2}+2x\varepsilon+\varepsilon^{2}=x^{2}+(2x)\varepsilon+o(\varepsilon).$$

Recall the chain rule, Theorem 8.10, which you proved in an exercise and we generalized in Chapter 14. We can prove this theorem using easy calculations.

**Theorem 15.6.** *The derivative of $f(g(x))$ is $f'(g(x))g'(x)$.*

*Proof.* Using the definition of differentiability for $g$,

$$f(g(x+\varepsilon))=f(g(x)+g'(x)\varepsilon+o(\varepsilon))$$

Define $\eta=g'(x)\varepsilon+o(\varepsilon)$. Note that as $\varepsilon\to 0$ we also have $\eta\to 0$. So we can apply the definition of the derivative to $f$.

$$\begin{aligned}
f(g(x+\varepsilon)) &=f(g(x)+\eta) \\
&=f(g(x))+f'(g(x))\eta+o(\eta) \qquad\text{(now expand $\eta$)} \\
&=f(g(x))+f'(g(x))g'(x)\varepsilon+[f'(g(x))o(\varepsilon)+o(g'(x)\varepsilon+o(\varepsilon))]
\end{aligned}$$

Note that $f'(g(x))$ and $g'(x)$ are constants relative to the little-o, so the bracketed terms simplify to $o(\varepsilon)$. What's left is the coefficient of $\varepsilon$, which is $f'(g(x))g'(x)$. $\blacksquare$

Half of the work in this book is finding computationally friendly representations of interesting conceptual ideas. In this case big-O allowed us to turn *proofs* into easy computation!

### Algorithm Analysis

Infinite limit big-O notation is a hallmark of algorithm runtime and space analysis. One cares about the runtime of an algorithm as the input size scales. The prototypical example is sorting. If an input list has $n$ fixed-length integers, then BubbleSort has $O(n^{2})$ worst-case runtime, while MergeSort has $O(n\log n)$ worst-case runtime. For this essay we ignore the worst-case/best-case/average-case distinction.

To say anything meaningful about which algorithm is better, we want big-O for two reasons. First, just as the interface for a software system shouldn't depend on the implementation, our analysis of the quality of an algorithm shouldn't depend on the fine-grained details of the implementation. If one decides to structure the algorithm as three functions instead of four, the raw runtime will change; extra steps are taken to push stack frames and handle return values! Of course, many engineers spend a lot of important and valuable time studying the fine-grained runtime of time-critical algorithms. There are experts in loop-unrolling, after all. But big-O isn't meant for those situations; rather, it's meant for the life of the system that comes before fine-tuning. Big-O is a first responder to the scene. By the time you're fine-tuning, big-O's job is done.

Second, and closely related, the analysis of the quality of the algorithm shouldn't depend on features of the system the code is being run on that are beyond the programmer's control. If you're sensitive to whether your C compiler is run with aggressive or *extremely* aggressive optimization flags, then big-O will not help. But most systems don't ever reach that level of care in their entire lifetime. Big-O allows you to ignore it.

And so we package those details up into a "constant factor" of overhead, which we accept as the penalty for having principle to guide our decisions. As such, given two algorithms with different big-O runtime, the order of magnitude change inside the big-O is our main focus. When we ask, "can this algorithm be solved any faster?" we don't mean can the constant be improved. Rather, we mean can it be solved an *order of magnitude* faster, ignoring constants and runtime for small inputs.

I often hear the complaint, "But what if the constant factor is a billion! Then it's completely useless to use big-O!" Computer scientists are well aware of the possibility that the hidden constant might be absurd. A witty meme, whose origin I can't recall and failed to hunt down, involves the Black Knight of Monty Python and the Holy Grail. This character famously loses his limbs in a sword fight, but refuses to surrender, exclaiming, "It's just a flesh wound!" On this image, the meme superimposes the quote, "It's just a constant factor!" Joking aside, more often than not the constant factors are mere flesh wounds. Constants dominating runtime—i.e., when big-O misleads—is the exception to the rule, and usually a sign of recent, or purely theoretical research. A famous example is the linear-time algorithm for polygon triangulation. This algorithm has a large constant factor, and is so tricky to implement that it has been called "hopeless" by Steve Skiena, the author of "The Algorithm Design Manual."

We've established that big-O can be used to measure things beyond algorithm runtime and space usage, like the quality of an approximation. Indeed, big-O can be used to discuss the usage of *any* constrained resource. For Taylor series the resource is "deviation from the truth," but in computer science there are a whole host of other things that big-O is used to analyze.

- **Communication:** In a distributed system, a common bottleneck is the amount of data that needs to be communicated across servers in order to finish a computation.
- **Randomness:** In cryptography, one can measure the security of a protocol in terms of encryption key size, which is usually proportional to the number of bits of a random seed. High quality random number generators can be slow, and time-sensitive cryptographic applications need to make a tradeoff between security and time.
- **Collisions:** Load balancers have to assign jobs to servers with an extremely high rate of jobs assigned per second. In particular, they almost never have enough time to ask a server how many jobs it's processing. Instead, load balancing algorithms use randomness and reason about the expected worst-case load of a server. One can think of collisions of job assignments as a constrained resource a load balancer wants to minimize for the most impacted server.
- **Errors:** In systems where data integrity is important, expensive, and bits are often lost or flipped (such as data being transmitted through space, or on a scratched up disc), one often employs redundancy schemes called *error-correcting codes* that allow one to recover from these errors. Such schemes require one to store additional bits, and so there's a tradeoff between how many additional bits one needs to store and the error tolerance of the scheme.
- **Labeled examples:** Most machine learning systems require labeled training data to produce a classifier. Since compute power is generally cheaper than getting humans to label examples, one major bottleneck on the efficiency of a learning system is access to clean data. Many learning systems are studied under the lens of so-called *query complexity*, which measures access to data. A popular topic these days is also interactive learning, in which a learning system has a "human in the loop" that helps the machine with difficult examples. A human doing work is clearly a bottleneck to an automated system.
- **Regret:** Some machine learning systems involve an explore/exploit tradeoff, where the learning algorithm receives a reward for each action it takes, and would like to find the best actions while still getting a good reward as it searches.[^bandit] The quantity one wants to optimize for is *regret*, the difference between the reward you got and the reward you would have got had you behaved optimally in hindsight.

[^bandit]: If you're interested in this, a keyword to search for is "bandit learning."

Each of these topics has a rich history of design and analysis, and for each the principles of the discussion revolve around asymptotic analysis. An interactive learning system that takes $n$ pieces of input data but requires $\Omega(n)$ queries to a human to learn can already be determined unscalable, but one that only needs $O(\log(n))$ might work. A load balancer that spreads $m$ jobs over $n$ servers and causes the worst server to have $\Theta(m/n+\sqrt{m})$ jobs is almost certain to crash servers during peak hours compared to one that guarantees $O(m/n+\log n)$.

Big-O is a cognitive tool that allows a human to organize and make sense of a mess of details in a rigorous fashion. It's a tool for high level thinking. Software is full of constrained resources, tradeoffs, and the desire for principled decision making. Fluency in asymptotic language will help you navigate these decisions efficiently and formulate hypotheses that can then be backed up by data.
