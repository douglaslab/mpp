---
layout: post
category: publication
published: true
title: "Layering Assume-Guarantee Contracts for Hierarchical System Design"
date: 2018-09-14 12:00:00
pmid: 
authors: "Filippidis I, Murray RM"
firstauthor: "Filippidis I"
journalname: "Proc. IEEE"
journalvolume: 106
journalissue: 9
journalpages: 1616–1654
---

Specifications for complex engineering systems are typically decomposed into specifications for individual subsystems in a manner that ensures they are implementable and simpler to develop further. We describe a method to algorithmically construct component specifications that implement a given specification when assembled. By eliminating variables that are irrelevant to realizability of each component, we simplify the specifications and reduce the amount of information necessary for operation. We parametrize the information flow between components by introducing parameters that select whether each variable is visible to a component. The decomposition algorithm identifies which variables can be hidden while preserving realizability and ensuring correct composition, and these are eliminated from component specifications by quantification and conversion of binary decision diagrams to formulas. The resulting specifications describe component viewpoints with full information with respect to the remaining variables, which is essential for tractable algorithmic synthesis of implementations. The specifications are written in TLA+, with liveness properties restricted to an implication of conjoined recurrence properties, known as GR(1). We define an operator for forming open systems from closed systems, based on a variant of the “while-plus” operator. This operator simplifies the writing of specifications that are realizable without being vacuous. To convert the generated specifications from binary decision diagrams to readable formulas over integer variables, we symbolically solve a minimal covering problem. We show with examples how the method can be applied to obtain contracts that formalize the hierarchical structure of system design.

URL: [http://dx.doi.org/10.1109/JPROC.2018.2834926](http://dx.doi.org/10.1109/JPROC.2018.2834926)
