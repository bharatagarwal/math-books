# A New Interface

> We are no longer constrained by pencil and paper. The symbolic shuffle should no longer be taken for granted as the fundamental mechanism for understanding quantity and change. Math needs a new interface.
>
> –Bret Victor, "Kill Math"

This book has been quite a journey. We laughed. We cried. We computed with matrices like fury.

Math is a human activity. It's messy and beautiful, complicated and elegant, useful and bull-headedly frustrating. But in reading this book, dear reader, my dream is that you have found the attitude, confidence, and enough prerequisite knowledge to continue to engage with mathematics beyond these pages. I hope that you will find the same joy that I have in the combination of math and programming.

You may be wondering what's next. Each topic in this book was only covered lightly. There's a vast world of math out there, in the form of books, blog posts, video lectures, and the questions from your own curiosity. So much to explore! I included an annotated list of resources in Appendix C to whet your appetite.

In these closing words, I'd like to explore a vision for how mathematics and software can grow together. Much of our effort in this book involved understanding notation, and using our imagination to picture arguments written on paper. In contrast, there's a growing movement that challenges mathematics to grow beyond its life on a chalkboard.

One of the most visible proponents of this view is Bret Victor. If you haven't heard of him or seen his fantastic talks, please stop reading now and go watch his talk, "Inventing on Principle."[^1] It's worth every minute. Victor's central thesis is that creators must have an immediate connection to their work. As such, Victor finds it preposterous that programmers often have to write code, compile, run, debug, and repeat every time they make a change. Programmers shouldn't need to simulate a machine inside their head when designing a program—there's a machine sitting right there that can perform the logic perfectly!

[^1]: [https://vimeo.com/36579366](https://vimeo.com/36579366)

Victor reinforces his grand, yet soft-spoken ideas with astounding prototypes. But his ideas are deeper than a flashy user interface. Victor holds a deep reverence for ideas and enabling creativity. He doesn't want to fundamentally change the way people interact with their music library. He wants to fundamentally change the way people create *new* ideas. He wants to enable humans to think thoughts that could not previously have been thought at all. You might wonder what one could possibly mean by "think new thoughts," but fifteen minutes of Victor's talk will show you and make disbelieve how we could have possibly made do without the typical software write-compile-run loop. His demonstrations rival the elegance of the finest mathematical proofs.

Just as Lamport's structured proof hierarchies and automated assistants are his key to navigating complex proofs, and similarly to how Atiyah's most effective tool is a tour of ideas that pique his interest, Victor feels productive when he has an immediate connection with his work. A large part of it is having the thing you're creating react to modifications in real time. Another aspect is simultaneously seeing all facets relevant to your inquiry. Rather than watch a programmed car move over time, show the entire trajectory for a given control sequence, the view updating as the control sequence updates. Victor demonstrates this to impressive effect.[^2]

[^2]: It's amusing to see an audience's wild applause for this, when the same people might easily have groaned as students being asked to sketch (or parse a plot of) the trajectories of a differential equation, despite the two concepts being identical. No doubt it is related to the use of a video game.

It should not surprise you, then, that Victor despises mathematical notation. In his essay "Kill Math," Victor argues that a pencil and paper is the most antiquated and unhelpful medium for using mathematics. Victor opines on what a shame it is that so much knowledge is only accessible to those who have the unnatural ability to manipulate symbols on paper. How many good ideas were never thought because of that high bar?

One obvious reason for the ubiquity of mathematical notation is an accident of history's most efficient information distribution systems, the printing press and later the text-based internet. But given our fantastic new technology—virtual reality, precise sensors, machine learning algorithms, brain-computer interfaces—how is it that mathematics is left in the dust? Victor asks all these questions and more.

I have to tread carefully here, because mathematics is a large part of my identity. When I hear "kill math," my lizard brain shoots sparks of anger. For me, this is a religious issue deeper than my favorite text editor. Even as I try to remain objective and tactful, take what I say with a grain of salt.

Overall, I agree with Victor's underlying sentiment. Lots of people struggle with math, and a better user interface for mathematics would immediately usher in a new age of enlightenment. This isn't an idle speculation. It has happened time and time again throughout history. The Persian mathematician Muhammad ibn Musa al-Khwarizmi invented algebra (though without the symbols for it) which revolutionized mathematics, elevating it above arithmetic and classical geometry, quickly scaling the globe. Make no mistake, the invention of algebra literally enabled average people to do contemporarily advanced mathematics.[^3] I'm surprised Victor does not reference algebra as a perfect example of a tool for thinking new thoughts, even if before arguing its time has passed.

[^3]: See Keith Devlin's essay for more on this: [http://devlinsangle.blogspot.com/2016/04/algebraic-roots-part-1.html](http://devlinsangle.blogspot.com/2016/04/algebraic-roots-part-1.html)

And it only gets better, deeper, and more nuanced. Shortly after the printing press was invented French mathematicians invented modern symbolic notation for algebra, allowing mathematics to scale up in complexity. Symbolic algebra was a new user interface that birthed countless new thoughts. Without this, for example, mathematicians would never have discovered the connections between algebra and geometry that are so prevalent in modern mathematics and which lay the foundation of modern physics. Later came the invention of set theory, and shortly after category theory, which were each new and improved user interfaces that allowed mathematicians to express deeper, more unified, and more nuanced ideas than was previously possible.

Meanwhile, many of Victor's examples of good use of his prototypes are "happy accidents." By randomly fiddling with parameters (and immediately observing the effect), Victor stumbles upon ideas that would never occur without the immediacy. To be sure, serendipity occurs in mathematics as well. Recall Andrew Wiles fumbling in his dark room looking for a light switch. Many creative aspects of mathematics involve luck, good fortune, and "eureka" moments, but there is nowhere near the same immediacy.

Immediacy makes it dreadfully easy to explore examples, which is one of the most important techniques I hope you take away from this book! But what algebraic notation and its successors bring to the table beyond happenstance is to scale in complexity beyond the problem at hand. While algebra limits you in some ways—you can't see the solutions to the equations as you write them—it frees you in other ways. You need not know how to find the roots of a polynomial before you can study them. You need not have a complete description of a group before you start finding useful homomorphisms. As Sir Arthur Eddington said, group theory studies operations that are as unknown as the quantities that they operate on. We didn't need to understand precisely how matrices correspond to linear maps before studying them, as might be required to provide a useful interface meeting Victor's standards. Indeed, it was algebraic grouping and rearranging (with cognitive load reduced by passing it off to paper) that provided the derivation of matrices in the first place.

Then there are the many "interfaces" that we've even seen in this book: geometry and the Cartesian plane, graphs with vertices and edges, pyramids of balls with arrows, drawings of arcs that we assert are hyperbolic curves, etc. Mathematical notation goes beyond "symbol manipulation," because any picture you draw to reason about a mathematical object is literally mathematical notation.

I see a few ways Victor's work falls short of enabling new modes of thought, particularly insofar as it aims to replace mathematical notation. I'll outline the desiderata I think a new interface for mathematics must support if it hopes to replace notation.

1. **Counterfactual reasoning:** The interface must support reasoning about things that cannot logically exist.
2. **Meaning assignment:** The interface must support assigning arbitrary semantic meaning to objects.
3. **Flexible complexity:** The interface should be as accessible to a child learning algebra as to a working mathematician.
4. **Incrementalism:** Adapting the interface to study a topic must not require encoding extensive prior knowledge about that topic.

The last two properties are of particular importance for any interface. Important interfaces throughout history satisfy the last two, including spoken language, writing, most tools for making art and music, spreadsheets, touchscreens and computer mice, keyboards,[^4] and even the classic text editors vim and emacs—anyone can use them in a basic fashion, while experts dazzle us with them.

[^4]: Layouts of buttons and toggles in general, of which QWERTY is one.

Let's briefly explore each desired property.

## Counterfactual Reasoning

Because mathematical reasoning can be counterfactual, any system for doing mathematics must allow for the possibility that the object being reasoned about cannot logically exist. We've seen this time and again in this book when we do proof by contradiction: we assume to the contrary that some object $A$ exists, and we conclude via logic that $1=2$ or some other false statement, and then $A$, which we handled as concretely as we would throw a ball, suddenly never existed to begin with. There is no largest prime, but I can naively assume that there is and explore what happens when I square it. Importantly, the interface need not encode counterfactual reasoning literally. It simply needs to support the task of counterfactual reasoning by a human.

Lumped in with this is *population reasoning*. I need to be able to reason about the entire class of all possible objects satisfying some properties. The set of all algorithms that compute a function (even if no such algorithm exists), or the set of all distance-preserving functions of an arbitrary space. These kinds of deductions are necessary to organize and synthesize ideas from disparate areas of math together (connecting us to "Flexible complexity" below).

A different view is that a useful interface for mathematics must necessarily allow the mathematician to make mistakes. But part of the point of a new interface was to avoid the mistakes and uncertainty that pencil and paper make frequent! It's not entirely clear to me whether counterfactual reasoning *necessarily* enables mistakes. It may benefit from a tradeoff between the two extremes.

## Meaning Assignment

One of the handiest parts of mathematical notation is being able to draw an arbitrary symbol and imbue it with arbitrary semantic meaning. $N$ is a natural number by fiat. I can write $f(ab)=f(a)f(b)$ and overload which multiplication means what. I can define a new type of arrow $\hookrightarrow$ on the fly and say "this means injective map."

This concept is familiar in software, but the defining feature in mathematics is that one need not know how to implement it to assert it and then study it. This ties in with "Incrementalism" below. Anything I can draw, I can give logical meaning.

Ideally the interface also makes the assignment and management of meaning *easy*. That is, if I've built up an exploration of a problem involving pennies on a table, I should easily be able to change those pennies to be coins of arbitrary unknown denomination. And then allow them to be negative-valued coins. And then give them a color as an additional property. And it should be easy to recall what semantics are applied to which objects later. If each change requires me to redo large swaths of work (as many programs built specifically to explore such a problem would), the interface will limit me. With algebraic notation, I could simply add another index, or pull out a colored pencil (or pretend it's a color with shading), and continue as before. In real life I just say the word, even if doing so makes the problem drastically more difficult.

## Flexible Complexity

Music is something that exhibits flexible complexity. A child raps the keys of a piano and makes sounds. So too does Ray Charles, though his technique is multifaceted and deliberate.

Mathematics has similar dynamic range that can accommodate the novice and the expert alike. Anyone can make basic sense of numbers and unknowns. Young children can understand and generate simple proofs. With a decent grasp of algebra, one can compute difficult sums. Experts use algebra to develop theories of physics, write computer programs with provable guarantees, and reallocate their investment portfolios for maximum profit.

On the other hand, most visual interactive explorations of mathematics—as impressive and fun as they are—are single use. Their design focuses on a small universe of applicable ideas, and the interface is more about guiding you toward a particular realization than providing a tool. These are commendable, but when the experience is over one returns to pencil and paper.

The closest example of an interface I've seen that meets the kind of flexible complexity I ask of a replacement for mathematics is Ken Perlin's Chalktalk.[^5] Pegged as a "digital presentation and communication language," the user may draw anything they wish. If the drawing is recognized by the system, it becomes interactive according to some pre-specified rules. For example, draw a circle at the end of a line, and it turns into a pendulum you can draw to swing around. Different pieces are coupled together by drawing arrows; one can plot the displacement of the pendulum by connecting it via an arrow to a plotting widget. Perlin displays similar interactions between matrices, logical circuits, and various sliders and dials.

[^5]: [https://github.com/kenperlin/chalktalk](https://github.com/kenperlin/chalktalk)

Chalktalk falls short in that your ability to use it is limited by what has been explicitly programmed into it as a behavior. If you don't draw the pendulum just right, or you try to connect a pendulum via an arrow to a component that doesn't understand its output, you hit a wall. To explain to the interface what you mean, you write a significant amount of code. This isn't a deal breaker, but rather where I personally found the interface struggling to keep up with my desires and imagination. What's so promising about Chalktalk is that it allows one to offset the mental task of keeping track of interactions that algebraic notation leaves to manual bookkeeping.

## Incrementalism

Incrementalism means that if I want to repurpose a tool for a new task, I don't already need to be an expert in the target task to use the tool on it. If I've learned to use a paintbrush to paint a flower on a canvas, I need no woodworking expertise to paint a fence. Likewise, if I want to use a new interface for math to study an optimization problem, using the interface shouldn't require me to solve the problem in advance. Algebra allows me to pose and reason about an unknown optimum of a function; so must any potential replacement for algebra.

Geometry provides an extended example. One could develop a system in which to study classical geometry, and many such systems exist (Geogebra is a popular one, and quite useful in its own right!). You could enable this system to draw and transform various shapes on demand. You can phrase theorems from Euclidean geometry in it, and explore examples with an immediate observation of the effect of any operation.

Now suppose we want to study parallel lines; it may be as clear as the day from simulations that two parallel lines never intersect, but does this fact follow from the inherent properties of a line? Or is it an artifact of the implementation of the simulation? As we remember, efficient geometry algorithms can suffer from numerical instability or fail to behave properly on certain edge cases. Perhaps parallel lines intersect, but simply very far away and the interface doesn't display it well? Or maybe an interface that does display far away things happens to make non-intersecting lines appear to intersect due to the limitations of our human eyes and the resolution of the screen.

In this system, could one study the possibility of a geometry in which parallel lines always intersect? With the hindsight of Chapter 16 we know such geometries exist (projective geometry has this property), but suppose this was an unknown conjecture. To repurpose our conventional interface for studying geometry would seem to require defining a correct model for the alternative geometry in advance. Worse, it might require us to spend weeks or months fretting over the computational details of that model. We might hard-code an intersection point, effectively asserting that intersections exist. But then we need to specify how two such hard-coded points interact in a compatible fashion, and decide how to render them in a useful way. If it doesn't work as expected, did we mess up the implementation, or is it an interesting feature of the model? All this fuss before we even know whether this model is worth studying!

This is mildly unfair, as the origins of hyperbolic geometry did, in fact, come from concrete models. The point is that the inventors of this model were able to use the sorts of indirect tools that precede computer-friendly representations. They didn't need a whole class of new insights to begin. If the model fails to meet expectations early on, they can throw it out without expending the effort that would have gone into representing it within our hypothetical interface.

## On the Shoulders of Giants

Most of my objections boil down to the need to create abstractions not explicitly programmed into the interface. Mathematics is a language, and it's expressiveness is a core feature. Like language, humans use it primarily to communicate to one another. Like writing, humans use it to record thoughts in times of inspiration, so that memory can be offset to paper and insights can be reproduced faithfully later. Paraphrasing Thurston, mathematics only exists in the social fabric of the people who do it. An interface purporting to replace mathematical notation must build on the shoulders of the existing mathematics community. As Isaac Newton said, "If I have seen further it is by standing on the shoulders of giants."

The value of Victor's vision lies in showing us what we struggle to see in our minds. Now let's imagine an interface that satisfies our desiderata, but also achieves immediacy with one's work. I can do little more than sketch a dream, but here it is.

Let's explore a puzzle played on an infinite chessboard, which I first learned from mathematician Zvezdelina Stankova via the YouTube channel Numberphile.[^6] You start with an integer grid $\mathbb{N} \times \mathbb{N}$, and in each grid cell $(i,j)$ you can have a person or no person. The people are called "clones" because they are allowed to take the following action: if cells $(i+1,j)$ and $(i,j+1)$ are both empty, then the clone in cell $(i,j)$ can split into two clones, which now occupy spaces $(i+1,j)$, $(i,j+1)$, leaving space $(i,j)$ vacant. You start with three clones in "prison" cells $(1,1)$, $(1,2)$, $(2,1)$, and the goal is to determine if there is a finite sequence of moves, after which all clones are outside the prison. For this reason, Stankova calls the puzzle "Escape of the Clones."

[^6]: [http://youtu.be/1FQGSGsXbXE](http://youtu.be/1FQGSGsXbXE)

<!-- carousel -->
![Left: An example move in "Escape of the Clones" whereby the solid-bordered clone transforms into the two dotted-border clones.](09a - A New Interface_images/img-0.jpeg)
![Right: the starting configuration for the puzzle.](09a - A New Interface_images/img-1.jpeg)
<!-- endcarousel -->

Suppose that our dream interface is sufficiently expressive that it can encode the rules of this puzzle, and even simulate attempts to solve it. If the interface is not explicitly programmed to do this, it would already be a heroic accomplishment of *meaning assignment* and *flexible complexity*.

Now after playing with it for a long time, you start to get a feeling that it is impossible to free the clones. We want to use the interface to prove this, and we can't already know the solution to do so. This is *incrementalism*.

If we were to follow in Stankova's footsteps, we'd employ two of the mathematician's favorite tools: proof by contradiction and the concept of an invariant. The invariant would be the sum of some *weights* assigned to the initial clones: the clone in cell $(1,1)$ has weight $1$, and the clone in cells $(1,2),(2,1)$ each get weight $1/2$. To be an invariant, a clone's splitting action needs to preserve weight. A simple way to do this is to simply have the cloning operation split a clone's current weight in half. So a clone in cell $(2,1)$ with weight $1/2$ splits into two clones in cells $(2,2),(3,1)$ each of weight $1/4$. We can encode this in the interface, and the interface can verify for us that the invariant is indeed an invariant. In particular, the weight of a clone depends only on its position, so that the weight of a clone in position $(i,j)$ is $2^{-(i+j-2)}$. The interface would determine this and tell us. This is *immediacy*.

Then we can, with the aid of the interface, compute the weight-sum of any given configuration. The starting region's weight is $2$, and it remains $2$ after any sequence of operations. It dawns on us to try filling the entire visible region outside the prison with clones. We have assumed to the contrary that an escape sequence exists, in which the worst case is that it fills up vast regions of the plane. The interface informs us that our egregiously crowded region has weight $1.998283$. We then ask the interface to fill the *entire complement* of the prison with clones (even though that is illegal; the rules imply you must have a finite sequence of moves!). It informs us that weight is also $2$. We realize that if any cell is cloneless, as must be true after a finite number of moves, we will have violated the invariant. This is *counterfactual reasoning*.

Frankly, an interface that isn't explicitly programmed to explore this specific proof—yet enables an exploration that can reveal it in a more profound way than paper, pencil, and pondering could—sounds so intractable that I am tempted to scrap this entire essay in utter disbelief. How can an interface be so expressive without simply becoming a general-purpose programming language? What would prevent it from displaying the same problems that started this inquiry? What precisely is it about the nature of human conversation that makes it so difficult to explain the tweaks involved in exploring a concept to a machine?

While we may never understand such deep questions, it's clear that abstract logic puzzles and their proofs provide an excellent test bed for proposals. Mathematical puzzles are limited, but rich enough to guide the design of a proposed interface. Games involve simple explanations for humans with complex analyses (flexible complexity), drastically different semantics for abstract objects like chessboards and clones (meaning assignment), there are many games which to this day still have limited understanding by experts (incrementalism), and the insights in many games involve reasoning about hypothetical solutions (counterfactual reasoning).

In his book "The Art of Doing Science and Engineering," the mathematician and computer scientist Richard Hamming put this difficulty into words quite nicely,

> It has rarely proved practical to produce exactly the same product by machines as we produced by hand. Indeed, one of the major items in the conversion from hand to machine production is the imaginative redesign of an equivalent product. Thus in thinking of mechanizing a large organization, it won't work if you try to keep things in detail exactly the same, rather there must be a larger give-and-take if there is to be a significant success. You must get the essentials of the job in mind and then design the mechanization to do that job rather than trying to mechanize the current version—if you want a significant success in the long run.

Hamming's attitude about an "equivalent product" summarizes the frustration of writing software. What customers want differs from what they say they want. Automating manual human processes requires arduously encoding the loose judgments made by humans—often inconsistent and based on folk lore and experience. Software almost always falls short of really solving your problem. Accommodating the shortcomings requires a whole extra layer of process.

We write programs to manage our files, and in doing so we lose much of the spatial reasoning that helps people remember where things are. The equivalent product is that the files are stored and retrievable. On the other hand, for mathematics the equivalent product is human understanding. This should be no surprise by now, provided you've come to understand the point of view espoused throughout this book. In this it deviates from software. We don't want to retrieve the files, we want to understand the meaning behind their contents.

My imagination may thus defeat itself by failing to give any ground. If a new interface is to replace pencil and paper mathematics, must I give up the ease of some routine mathematical tasks? Or remove them from my thinking style entirely? Presuming I can achieve the same sorts of understanding—though I couldn't say how—the method of arrival shouldn't matter. And yet, this attitude ignores my experience entirely. The manner of insight you gain when doing mathematics is deeply intertwined with the method of inquiry. That's precisely why Victor's prototypes allow him to think new thoughts!

Mathematics succeeds only insofar as it advances human understanding. Pencil and paper may be the wrong tool for the next generation of great thinkers. But if we hope to enable future insights, we must understand how and why the existing tools facilitated the great ideas of the past. We must imbue the best features of history into whatever we build. If you, dear programmer, want to build those tools, I hope you will incorporate the lessons and insights of mathematics.

Until then!
