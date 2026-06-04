# Bibliography

The original bibliography from Scheinerman's guide, annotated with context and relevance to this curriculum (discrete math → formal verification → distributed systems, from a software engineering background).

### History of notation

**Florian Cajori. *A History of Mathematical Notations: Two Volumes Bound As One*. Dover, 1993.** Originally published in 1928–29. Almost a century later, this remains the definitive reference on how mathematical notation evolved — from Babylonian numerals to modern operator symbols. Cajori traces each symbol's first appearance, the competition it faced from alternatives, its spread across countries, and its eventual survival or extinction. The Mathematical Association of America lists it as essential for undergraduate libraries. 820 pages, still in print. *Read when curious — enriches context but not load-bearing for learning.*

**Jeff Miller. [Earliest Uses of Various Mathematical Symbols](https://jeff560.tripod.com/mathsym.html).** A remarkable one-person project by a retired Florida high school teacher: a meticulously sourced catalogue of when each mathematical symbol first appeared in print and who introduced it. Also mirrored at the [MacTutor History of Mathematics](https://mathshistory.st-andrews.ac.uk/Miller/mathsym/) archive at St Andrews. The companion page [Earliest Uses of Some Words of Mathematics](https://mathshistory.st-andrews.ac.uk/Miller/mathword/) covers terminology. *Same — interesting for context, not for learning.*

### Standards and symbol catalogues

**IEEE. *American National Standard: Mathematical Signs and Symbols for Use in Physical Sciences and Technology*, 1993.** The ANSI/IEEE standard that codifies which symbols mean what in engineering contexts. Relevant when conventions clash — for instance, whether $\mathbb{N}$ includes zero (this standard says no; ISO says yes). *Not relevant to this curriculum — standards compliance is not a concern here.*

**ISO. *Quantities and Units Part 2: Mathematical Signs and Symbols to be Used in the Natural Sciences and Technology*, 2009.** ISO 80000-2:2009 (superseding ISO 31-11:1992). The international counterpart to the IEEE standard. *Same — off-path.*

**Scott Pakin. [The Comprehensive $\mathrm{LaTeX}$ Symbol List](http://www.ctan.org/tex-archive/info/symbols/comprehensive/).** Over 18,000 symbols from 226 $\mathrm{LaTeX}$ packages, organized by visual similarity. Indispensable for finding the command for a symbol you can draw but can't name. *Useful if you're writing LaTeX. This reader uses KaTeX in markdown, so marginally relevant — but handy when you need a KaTeX command name for an unfamiliar symbol.*

**Eric Weisstein. [Wolfram Mathworld](http://mathworld.wolfram.com/).** The most comprehensive online mathematics encyclopedia. Each entry includes formal definitions, properties, history, and often interactive demonstrations. *Actually useful. When you hit unfamiliar notation in MCS or Lovász, this is the fastest lookup that gives definitions, properties, and examples on one page.*

**Wikipedia. [Table of Mathematical Symbols](http://en.wikipedia.org/wiki/Table_of_mathematical_symbols).** A quick-reference table organizing common symbols by category (arithmetic, set theory, logic, etc.) with $\mathrm{LaTeX}$ codes. *Redundant with this guide — you're already reading the more detailed version.*

### $\mathrm{LaTeX}$ guides

**Michael Downes. *Short Math Guide for $\mathrm{LaTeX}$*.** A concise (17-page) reference for typesetting mathematics in $\mathrm{LaTeX}$, published by the AMS.

**George Grätzer. *Math into $\mathrm{LaTeX}$*. Birkhäuser, 2000.** and ***More Math into $\mathrm{LaTeX}$*. Birkhäuser, 4th ed., 2007.** The standard tutorial and reference for mathematical $\mathrm{LaTeX}$.

**Michel Goossens, Johannes Braams, and David Carlisle. *The $\mathrm{LaTeX}$ Companion*. Addison-Wesley, 2nd ed., 2004.** The authoritative reference for $\mathrm{LaTeX}$ beyond math — page layout, fonts, bibliography management, indexing.

*The LaTeX guides are off-path. This curriculum uses KaTeX-in-markdown, not LaTeX documents. If that changes (e.g., writing up proofs for Lean4 documentation), Downes' 17-page guide is the one to start with.*

### Mathematics references

**Roger A. Horn and Charles R. Johnson. *Matrix Analysis*. Cambridge University Press, 1990.** (2nd ed. 2012.) The definitive graduate textbook on matrix theory — eigenvalues, canonical forms, matrix decompositions, norms, and perturbation theory. Over 1,100 exercises in the second edition. *Way past the current stage. Graduate-level linear algebra is not on the path to discrete math and formal verification. Revisit if the curriculum ever reaches ML/optimization depth.*

**William Anthony Granville. *Elements of the Differential and Integral Calculus*. Ginn and Company, rev. ed., 1911.** Known affectionately as "the Granville," this was *the* calculus textbook for generations of engineers and physicists. Its notation conventions (some now archaic, like $\lfloor n \rfloor$ for $n!$) appear in Figure 6.1 of the Functions chapter. [Freely available on the Internet Archive](https://archive.org/details/elementsofdiffer00granuoft). *Historical curiosity only — referenced for one figure showing archaic notation.*

**Ambler Thompson and Barry N. Taylor. *Guide for the Use of the International System of Units (SI)*. NIST, 2008.** The official U.S. guide to SI units and their notation. *Not relevant — this curriculum doesn't touch physical units.*
