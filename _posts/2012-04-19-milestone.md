---
layout: post
title: Milestone Report
author: Ryan Pearl and Michael Sullivan
---


# Major Changes
We have made no major changes to our goals or implementations.


# What We Have Accomplished
We reviewed the literature on different types of range analysis and
decided to implement an analysis based on "Eliminating Range Checks
using Static Single Assignment Form".
One tricky part of this analysis is propagating range information
learned from conditional branches; this requires tracking ranges for
each variable differently at different points in the code, which loses
some of the normal benefits of SSA representations.
This method uses a version of
SSA form augmented with special &beta; nodes that act as a copy but
associate range information with the result. These &beta; nodes are
inserted after conditional branches to split the variables compared in
the branch and thus propagate the range information learned inside the
branches.

We have implemented passes to augment the middle intermediate
representation (MIR) with &beta; nodes and also to remove &beta;
nodes from the MIR. This passes should be fairly inexpensive, meaning
that we should be able to add &beta; nodes, run our optimizations,
and remove &beta; nodes at any stage of the optimization pipeline
without requiring changes to other passes.

We have also implemented an initial version of a worklist based SSA
algorithm. The code works, but can not track ranges bounded by other
variables (which is a feature that we may add eventually) and does not yet
support all arithmetic operations.

# Meeting Our Milestone

We think we mostly hit our milestone. We don't have all of the
arithmetic operations implemented, and we had hoped to but that is
just legwork that should fit easily into our existing framework.
The reason we are a little behind is because figuring out what
algorithms we wanted to implement and what direction to take took
longer than expected. We spent a lot of time trying to figure out ways
we could avoid having to augment the SSA form before we realized that
it wouldn't be that hard and would greatly simplify matters.

# Surprises

We haven't run into any major surprises. We were a little surprised by
how much work has been done on range analysis that is not applicable
to what we want to do.


# Logistics
## Schedule
- *Week 5*:
Implement optimizations, finish analysis.

The current plan is for Ryan to work on wrapping up the analysis while
Michael starts implementing optimizations (probably starting with
eliminating overflow guards). When the analysis is wrapped up, Ryan
will join in writing optimizations.

- *Week 6*:
Evaluation and wrap-up.

We will do benchmarks using common Javascript benchmark suites and
tune our optimizations accordingly.

## Resources Needed
Nothing.

