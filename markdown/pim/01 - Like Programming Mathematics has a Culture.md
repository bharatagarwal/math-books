# Like Programming, Mathematics has a Culture

> Mathematics knows no races or geographic boundaries; for mathematics, the cultural world is one country.
>
> –David Hilbert

## Learning to Code, One Disaster at a Time

Do you remember when you started to really learn programming? I do. I spent two years in high school programming games in Java. Those two years easily contain the worst and most embarrassing code I have ever written. My code absolutely reeked. Hundred-line functions and thousand-line classes, magic numbers, unreachable blocks of code, ridiculous comments, a complete disregard for sensible object orientation, and type-coercion that would make your skin crawl.

The code worked, but it was filled with bugs and mishandled edge-cases. I broke every rule, but for all my shortcomings I considered myself a hot-shot (at least, among my classmates!). I didn’t know how to design programs, or what made a program “good,” other than that it ran and I could impress my friends with a zombie shooting game.

Even after I started studying software in college, it was another year before I knew what a stack frame or a register was, another year before I was halfway competent with a terminal, another year before I appreciated functional programming, and to this day I still have an irrational fear of systems programming and networking. I built up a base of knowledge over time, with fits and starts at every step.

In a college class on C++ I was programming a Checkers game, and my task was to generate a list of legal jump-moves from a given board state. I used a depth-first search and a few recursive function calls. Once I had something I was pleased with, I compiled it and ran it on my first non-trivial example.

Despite following test-driven development, I saw those dreaded words: `Segmentation fault`. Dozens of test cases and more than twenty hours of confusion later, I found the error: my recursive call passed a reference when it should have been passing a pointer. This wasn’t a bug in syntax or semantics—I understood pointers and references well enough—but a design error.

As most programmers can relate, the most aggravating part was that changing four characters (swapping a few ampersands with asterisks) fixed it. Twenty hours of work for four characters! Once I begrudgingly verified it worked, I promptly took the rest of the day off to play Starcraft.

## The Secret Club

Such drama is the seasoning that makes a strong programmer. One must study the topics incrementally, learn from a menagerie of mistakes, and spend hours in a befuddled stupor before becoming “experienced.” This gives rise to all sorts of programmer culture, Unix jokes, urban legends, horror stories, and reverence for the masters of C that make the programming community so lovely.

It’s like a secret club where you know all the handshakes, but should you forget one, a crafty use of grep and sed will suffice. The struggle makes you appreciate the power of debugging tools, slick frameworks, historically enshrined hacks, and new language features that stop you from shooting your own foot.

When programmers turn to mathematics, they seem to forget these trials. The same people who invested years grokking the tools of their trade treat new mathematical tools and paradigms with surprising impatience. I can see a few reasons why.

For one, we were forced to take math classes for many year in school. That forced investment shouldn’t have been pointless. But the culture of mathematics and the culture of mathematics education—elementary through lower-level college courses—are completely different.

### The Disenchantment Pipeline

Even college math majors have to reconcile this. I’ve had many conversations with such students, including friends, colleagues, and even family, who by their third year decided they didn’t really enjoy math. The story often goes like this: a student who was good at math in high school reaches the point of a math major at which they must read and write proofs in earnest.

It requires an ambiguous, open-ended exploration that they don’t enjoy. Despite being a stark departure from the rigid structure of high school math, incoming students are not warned in advance. After coming to terms with their unfortunate situation, they decide that their best option is to persist until they graduate, at which point they return to the comfortable setting of pre-collegiate math, this time in the teacher’s chair.

I don’t mean to insult teaching as a profession—I love teaching and understand why one would choose to do it full time. There are many excellent teachers who excel at both the math and the trickier task of engaging aloof teenagers to think critically about it.

But this pattern of disenchantment among math teachers is prevalent, and it widens the conceptual gap between secondary and “college level” mathematics. Programmers often have similar feelings. The subject they once were good at is suddenly impenetrable. It’s a negative feedback loop in the education system. Math takes the blame.

### The Illusion of Familiarity

Another reason programmers feel impatient is because they do so many things that relate to mathematics in deep ways. They use graph theory for data structures and search. They study enough calculus to make video games. They hear about the Curry-Howard correspondence between proofs and programs. They hear that Haskell is based on a complicated math thing called category theory. They even use mathematical results in an interesting way.

I worked at a “blockchain” company that implemented a Bitcoin wallet, which is based on elliptic curve cryptography. The wallet worked, but the implementer didn’t understand why. They simply adapted pseudocode found on the internet. At the risk of a dubious analogy, it’s akin to a “script kiddie” who uses hacking tools as black boxes, but has little idea how they work. Mathematicians are on the other end of the spectrum. Why things work takes priority over practical implementation.

## Barriers to Entry

There’s nothing inherently wrong with using mathematics as a black box, especially the sort of applied mathematics that comes with provable guarantees. But many programmers *want* to dive deeper. This isn’t surprising, given how much time engineers spend studying source code and the internals of brittle, technical systems.

Systems that programmers rely on, such as dependency management, load balancers, search engines, alerting systems, and machine learning, all have rich mathematical foundations. We’re naturally curious.

A second obstacle is that math writers are too terse. The purest fields of mathematics take a sort of pretentious pride in how abstract and compact their work is. I can think of a handful of famous books, for which my friends spent weeks or months on a single chapter! This acts as a barrier to entry, especially since minute details matter for applications.

Yet another hindrance is that mathematics has no centralized documentation. Instead it has a collection of books, papers, journals, and conferences, each with subtle differences, citing each other in a haphazard manner. Dealing with this is not easy.

One often needs to translate between two different notations or jargons. Students of mathematics solve these problems with knowledgeable teachers. Working mathematicians “just do it.” They reconcile the differences themselves with coffee and contemplation.

## Notation as Technology

What programmers consider “sloppy” notation is one symptom of the problem, but there there are other expectations on the reader that, for better or worse, decelerate the pace of reading. Unfortunately I have no solution here. Part of the power and expressiveness of mathematics is the ability for its practitioners to overload, redefine, and omit in a suggestive manner.

Mathematicians also have thousands of years of “legacy” math that require backward compatibility. Enforcing a single specification for all of mathematics—a suggestion I frequently hear from software engineers—would be horrendously counter-productive.

Ideas we take for granted today, such as algebraic notation, drawing functions in the Euclidean plane, and summation notation, were at one point actively developed technologies. Each of these notations had a revolutionary effect on science, and also, to quote Bret Victor, on our capacity to “think new thoughts.” One can draw a line from the proliferation of algebraic notation to the invention of the computer.

Borrowing software terminology, algebraic notation is among the most influential and scalable technologies humanity has ever invented. And as we’ll see in Chapter 10 and Chapter 16, we can find algebraic structure hiding in exciting places. Algebraic notation helps us understand this structure not only because we can compute, but also because we can visually see the symmetries in the formulas. This makes it easier for us to identify, analyze, and encapsulate structure when it occurs.

## A Well-Designed Legacy System

Finally, the best mathematicians study concepts that connect decades of material, while simultaneously inventing new concepts which have no existing words to describe them. Without flexible expression, such work would be impossible. It reduces cognitive load, a theme that will follow us throughout the book. Unfortunately, it only does so for the readers who have already absorbed the basic concepts of discussion.

By contrast, good software practice assumes a lower bar. Code is encouraged to be simple enough for new grads to understand, and heavily commented otherwise. Surprising behavior is considered harmful. As such, the uninitiated programmer often has a much larger cognitive load when reading math than when reading a program.

There are good reasons why mathematics is the way it is, though the reasons may not always be clear. I like to summarize the contrast by claiming that mathematical notation is closer to spoken language than to code. There is a historical and cultural context missing from many criticisms of math. It’s a legacy system, yes, but a well-designed one. We should understand it, learn from its advantages, and discard the obsolete parts. Those obsolete parts are present, but rarer than they seem.

## Two Cultures, Two Sets of Questions

To fairly evaluate mathematics, we must first learn some mathematics. Only then can we compare and contrast programming and mathematics in terms of their driving questions, their values, their methods, their measures of success, and their cultural expectations.

Programming, at its core, focuses on how to instruct a computer to perform some task. But the broader driving questions include how to design a flexible system, how to efficiently store and retrieve data, how to design systems that can handle various modes of failure, how to scale, and how to tame growth and complexity.

Contrast this with mathematics which, at its core, focuses on how to describe a mathematical object and how to prove theorems about its behavior. The broader driving questions include how to design a unified framework for related patterns, how to find computationally useful representations of an object, how to find interesting patterns to study, and most importantly, how to think more clearly about mathematical subjects.

A large chunk of this book expands on this summary through interludes between each chapter and digressions after introducing technical concepts. The rest covers the fundamental objects and methods of a typical mathematical education. So let’s begin our journey into the mathematical mists with an open mind.

Read on, and welcome to the club.
