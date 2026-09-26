---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/null-hypothesis-significance-testing
page_type: concept
related:
- concepts/calibration
revision_id: 1
sources:
- sources/ellenberg-2014-how-not-to-be-wrong
tags: []
title: Null Hypothesis Significance Testing and p-values
updated: '2026-09-16T00:00:00Z'
updated_by: creditmacro-batch
schema_version: 2
uuid: 6e0336bb-ee57-5e3b-ac34-a4087e2505c1
content_hash: sha256:9e96408c2b6471bfb8342f24fab743c2a65d83ea084d7f942bcd33198dcf5cdd
---

<!-- AUTHORED REGION START -->
# Null Hypothesis Significance Testing and p-values

## Definition

Fisher's framework for rejecting a 'no effect' null when data are sufficiently unlikely under it; 'significant' means detectable, not important, and large samples flag any nonzero effect.

## The E-value Alternative

A p-value is defined by a tail probability; an [[concepts/e-value|e-value]] is defined by an expectation, $\mathbb{E}[E]\le 1$ under the null. The change buys three things p-values do not have: merging under arbitrary dependence with no correction, multiplication over time and hence [[concepts/anytime-valid-inference|optional stopping]], and [[concepts/false-discovery-rate|FDR control]] without a dependence assumption.

The two are convertible, at a cost. Calibrators map p-values to e-values, and $e\mapsto\min(1,1/e)$ is the unique admissible map back, so round trips lose information. [[sources/wang-2023-p-star-values|P\*-values]] sit between the two and are the proper home for mid p-values, which are not p-values at all.

## Sources

- [[sources/ellenberg-2014-how-not-to-be-wrong|How Not to Be Wrong: The Power of Mathematical Thinking]]
- [[sources/vovk-2020-evalues-calibration-combination|E-values: calibration, combination, and applications (2021)]]
- [[sources/wang-2023-p-star-values|Testing with p*-values (2024)]]

## Related Concepts

- [[concepts/calibration|calibration]]
- [[concepts/e-value|E-value]]
- [[concepts/p-value-merging|Merging P-values and E-values]]
- [[concepts/multiple-testing|Multiple Testing]]
<!-- AUTHORED REGION END -->
