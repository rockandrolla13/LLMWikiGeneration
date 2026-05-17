---
title: Code Reading in Practice
page_id: sources/hermans-2024-code-reading-in-practice
page_type: source
source_type: book
revision_id: 1
created: '2026-05-17T16:44:06Z'
updated: '2026-05-17T16:44:06Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
authors:
- Felienne Hermans
year: 2024
publisher: O'Reilly Media
edition: Early Release
is_early_release: true
page_count_estimate: 250
tags:
- ai-engineering
- code-comprehension
related:
- concepts/chunking
- concepts/code-reading
- concepts/code-smells
- concepts/entry-point-analysis
- concepts/eye-tracking-in-code-reading
- concepts/linguistic-anti-patterns
- concepts/mental-model-of-code
- concepts/name-molds
- concepts/program-slicing
- concepts/ubiquitous-language
- concepts/working-memory-in-programming
- entities/dror-feitelson
- entities/eric-evans
- entities/felienne-hermans
- entities/hedy-language
- entities/martin-fowler
- entities/oreilly-media
- entities/teresa-busjahn
- entities/venera-arnaoudova
mind_map_priority: medium
revision_hash: sha256:7909e78158a23726
---

# Code Reading in Practice
*Hands-On Techniques to Understand, Refactor and Improve How You Work With Code*

**Authors:** [[entities/felienne-hermans|Felienne Hermans]]

**Year:** 2024

**Publisher:** O'Reilly Media

**Edition:** Early Release

## Summary

Code Reading in Practice is a hands-on field guide arguing that reading code is a distinct, teachable skill that has been neglected relative to writing code. Hermans organises the practice into five dimensions — structure, domain, [[code-smells|code quality]], context, and collaboration — and supplies concrete exercises (folded-code surveys, dependency tables, name-mold inventories) for each. The book grounds its techniques in cognitive science: programmers fail to understand code not because they lack intelligence but because [[working-memory-in-programming|working memory]] holds only 2–6 items, so unfamiliar code must be processed through deliberate [[chunking|chunking]] and explicit [[mental-model-of-code|mental-model construction]] rather than top-to-bottom scrolling.

The early-release chapters work through structural reading (identifying object, functional, and singular components; building dependency tables; locating [[entry-point-analysis|entry points]] and following [[program-slicing|program slices]]) and domain reading (extracting nouns and verbs from identifier names to surface the [[ubiquitous-language|Ubiquitous Language]] of a codebase). Each technique pairs IDE tooling (find-usages, code folding, breakpoints) with manual table-filling exercises, and ends with refactoring prompts driven by [[code-smells|structural and linguistic code smells]] — the latter drawn from Arnaoudova's [[linguistic-anti-patterns|linguistic anti-pattern]] catalogue.

The book sits between popular-science texts like The Programmer's Brain (Hermans's earlier Manning book) and academic programming-comprehension research. It pulls from [[eye-tracking-in-code-reading|eye-tracking studies]] (Busjahn et al.), naming experiments (Feitelson), and Fowler's refactoring taxonomy, but stays exercise-driven rather than survey-driven. The Hedy compiler serves as the running example, giving readers a single codebase to anchor the structural and domain analyses against.

## Key Contributions

- A five-dimension framework — structure, domain, concepts, context, collaboration — for decomposing the otherwise-vague task of 'reading code'.
- Concrete table-based exercises (component-by-component dependency grids, parameter-overlap matrices, name-mold inventories) that externalise mental models so working memory is not overloaded.
- An integration of cognitive-science findings (working-memory limits, chunking, eye-tracking results) directly into IDE-based reading workflows.
- A practical pairing of structural code smells (Fowler) with linguistic code smells (Arnaoudova), turning reading sessions into refactoring conversations.
- The argument that following the call stack is a learned expert behaviour, not an intuition — and a method for novices to practise it via entry-point-driven slice reading.

## Key Topics Covered

structural code reading, dependency analysis, entry points and program slicing, working memory and chunking, mental models, domain-driven naming, ubiquitous language, linguistic anti-patterns, name molds, structural code smells, refactoring from reading, IDE-supported comprehension

## Questions Raised

- How do these reading techniques transfer to multi-language codebases where static analysis tools (find-usages, slicers) fail at language boundaries?
- Can the dependency-table and name-mold exercises be partially automated without losing the cognitive benefit of manual table-filling?
- How should code-reading skill be assessed or taught in computer-science curricula, and what is the evidence base for these specific exercises?
- How do LLM-based code assistants change which reading skills remain essential versus which they automate away?

## Intended Audience

Working software engineers onboarding to unfamiliar codebases, technical leads coaching juniors on code comprehension, and CS educators teaching reading as a first-class skill alongside writing.

## Key Concepts in This Source

- [[concepts/code-reading|Code Reading]]
- [[concepts/working-memory-in-programming|Working Memory in Programming]]
- [[concepts/chunking|Chunking]]
- [[concepts/mental-model-of-code|Mental Model of Code]]
- [[concepts/code-smells|Code Smells]]
- [[concepts/linguistic-anti-patterns|Linguistic Anti-Patterns]]
- [[concepts/program-slicing|Program Slicing]]
- [[concepts/ubiquitous-language|Ubiquitous Language]]
- [[concepts/name-molds|Name Molds]]
- [[concepts/entry-point-analysis|Entry Point Analysis]]
- [[concepts/eye-tracking-in-code-reading|Eye Tracking in Code Reading]]

## Entities

- [[entities/felienne-hermans|Felienne Hermans]]
- [[entities/martin-fowler|Martin Fowler]]
- [[entities/venera-arnaoudova|Venera Arnaoudova]]
- [[entities/teresa-busjahn|Teresa Busjahn]]
- [[entities/eric-evans|Eric Evans]]
- [[entities/dror-feitelson|Dror Feitelson]]
- [[entities/hedy-language|Hedy]]
- [[entities/oreilly-media|O'Reilly Media]]
