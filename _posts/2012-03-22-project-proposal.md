---
layout: post
title: Project Proposal
author: Ryan Pearl and Michael Sullivan
---


# Introduction
We propose implementing and evaluating range analysis for [IonMonkey](https://hg.mozilla.org/projects/ionmonkey/),
an optimizing JIT compiler for Javascript. Range analysis is
particularly useful in this context: in addition to taking advantage
of the analysis results to eliminate redundant comparisons and
bounds-checks, Javascript's dynamic semantics requires that all
numeric computations are floating point arithmetic.  This is slow, so
numbers that can be stored as integers are, and arithmetic operations
are guarded against overflow into their floating point
representation. With range analysis, we can prove these guards
unnecessary and emit higher-quality code.

# Project Tracking
IonMonkey is an open-source project built by the Mozilla Corporation. The range
analysis [tracking bug](https://bugzilla.mozilla.org/show_bug.cgi?id=699883)
will be used to track implementation progress.

# Project Goals
Our goal is to provide an implementation of range analysis and use the
results to implement two of the potential optimizations we discussed
(eliminating bounds checks, redundant comparisons, and overflow
guards). If progress appears to be too slow, we still hope to complete
range analysis integrate it into the compiler, and maybe implement one
of the optimizations. If our project proceeds faster than expected, we
can implement more optimizations that take advantage of this analysis
or begin to implement other related analysis phases for IonMonkey.

# Logistics
## Schedule
 -  *Weeks 1 - 2*: Research.
We will go over the various algorithms available for range analysis
and weigh their advantages. In particular, we must take care to
consider the time complexity of our selected algorithm since JIT
compilation must run more quickly than ahead-of-time compilation. At
this point we will be able to see if we can gain any advantage by
using the runtime knowledge available to a JIT compiler.

 -  *Week 2*: Source-diving.
IonMonkey is a large code-base and must interact with Firefox's
Javascript runtime and interpreter. While these components are
well-isolated, some source-diving will be necessary to understand the
context of the JIT.

 -  *Weeks 2 - 4*: Implement analysis.
Implementing a range analysis phase on the IonMonkey IL and running it
on a body of Javascript code to get an idea of what optimizations are
likely to be most effectively exposed by the information we are
gathering.

 -  *Weeks 4 - 5*: Implement optimizations.
Implementing some optimizations that take advantage of range information (such
as eliminating bounds checks, redundant comparisons, and overflow guards)
and testing against the large Javascript test-suite and fuzzer.

 -  *Weeks 5 - 6*: Evaluation and wrap-up.
There are several large Javascript benchmarking suites available to
measure the impact of our optimization on the x86, x86_64, and ARM
architectures. Since one of the other groups is apparently working on
building a new Javascript benchmark suite, we could maybe also try
their benchmark suite.

## Milestones
By April 19th, roughly the halfway-point of the project, we hope to be
code complete on the analysis phase of the optimization. At this
point, we will begin working on using these analysis results to
optimize code.

## Literature Search
We have looked at a few papers on range analysis, such as "The Design
and Implementation of a Non-Iterative Range Analysis Algorithm on a
Production Compiler", by Teixeira and Pereira, which is a practical
implementation of "A class of polynomially solvable range
constraints for interval analysis without widenings." by Su and Wagner. The
algorithm due to Su and Wagner is non-iterative, and works by solving a
constraint graph. Other range analyses, generally formulated as a more
traditional iterative dataflow problem, are also available.

## Resources Needed
The software we need is just the IonMonkey code base and a handful of
freely available benchmark suites. We both have good, modern computers
to run tests on.

## Getting Started
So far, we have done some looking over papers and considerations of
what algorithms to use. Both of us have worked on the Javascript team
at Mozilla, and one of us has worked on IonMonkey, so we should have a
leg up in diving into the engine source. We don't have anything preventing us
from starting immediately.
