---
title: On the existence of powerful p-values and e-values for composite hypotheses
page_id: sources/zhang-2024-powerful-p-e-composite
page_type: source
source_path: markdown_output/zhang-2024-powerful-p-e-composite.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Zhenyuan Zhang
- Aaditya Ramdas
- Ruodu Wang
year: 2024
venue: Annals of Statistics (2024)
tags:
- e-value
- composite-hypothesis
- existence
- convex-order
- test-martingale
sources: []
related:
- concepts/e-value
- concepts/p-value-merging
- concepts/multiple-testing
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: 78362cad-6713-5c7c-808c-89423d654de6
content_hash: sha256:0f18db5ce6ccf971ee1dbd84972111801738bc37de9fa1234d1e92bd59dafb7d
---

<!-- AUTHORED REGION START -->
# On the Existence of Powerful P-values and E-values for Composite Hypotheses

**Authors:** Zhenyuan Zhang, [[entities/aaditya-ramdas|Aaditya Ramdas]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2024 · **Venue:** Annals of Statistics

## Summary

A prior question to all the construction papers: when a null and an alternative are both composite, does a useful test statistic exist at all? The answer is geometric, and it is the same geometry for p-values and e-values.

## Results

For a finite null $\{P_1,\dots,P_L\}$ and a simple alternative $Q$:

- an **exact, non-trivial** p-value or e-value exists if and only if $Q\notin\mathrm{Span}(P_1,\dots,P_L)$;
- dropping exactness, a non-trivial one exists if and only if $Q\notin\mathrm{Conv}(P_1,\dots,P_L)$.

With a composite alternative that is also a polytope, the conditions become $\mathrm{Span}\,\mathcal{P}\cap\mathrm{Conv}\,\mathcal{Q}=\emptyset$ and $\mathrm{Conv}\,\mathcal{P}\cap\mathrm{Conv}\,\mathcal{Q}=\emptyset$ respectively. In the general case, with a common reference measure, the condition is that zero does not lie in the closure of $\mathrm{Span}\,\mathcal{P}+\mathrm{Conv}\,\mathcal{Q}$ in total variation.

So the question "can this hypothesis be tested with positive power?" reduces to whether the alternative can be written as a mixture, or a signed combination, of the nulls.

**Construction.** An iterative algorithm builds the optimal exact e-variable by repeatedly splitting a measure at its barycentre along a separating hyperplane, converging to the e-variable of largest e-power. It is feasible only in low dimensions.

**A structural surprise.** Sometimes no such p-value or e-value exists in the richest filtration but one does in a **coarsened** filtration — throwing information away can make a hypothesis testable. The paper gives the first general characterisation of when that happens, and a corollary on when test martingales or supermartingales with power one exist.

## Why It Matters

Before building an e-process for a composite null, this tells you whether the effort is possible in principle. The convex-geometry criterion is checkable, and the filtration result is a genuine design lever rather than a curiosity.

## See Also

[[concepts/e-value|E-value]] · [[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/multiple-testing|Multiple Testing]]
<!-- AUTHORED REGION END -->
