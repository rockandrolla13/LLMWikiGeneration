---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/observational-sampling-from-rcts
page_type: concept
related:
- concepts/confounding
- concepts/do-operator
- concepts/potential-outcomes
revision_hash: sha256:cd7a00625a58cfba0f6cef1ba641ebddc6b74443e81668dab791d71088bd1f17
revision_id: 1
sources:
- sources/gentzel-2021-osrct-evaluation
tags: []
title: Observational sampling from randomized controlled trials (OSRCT)
updated: '2026-06-09T12:00:00Z'
updated_by: creditmacro-batch
---

# Observational sampling from randomized controlled trials (OSRCT)

## Definition

A procedure that non-randomly sub-samples RCT data using biasing covariates to select a single treatment per unit, accepting a unit only if it actually received the selected treatment, thereby inducing confounding while keeping the original RCT's treatment effect recoverable as ground truth.

## Sources

- [[sources/gentzel-2021-osrct-evaluation|How and Why to Use Experimental Data to Evaluate Methods for Observational Causal Inference]]

## Related Concepts

- [[concepts/confounding|confounding]]
- [[concepts/do-operator|do-operator]]
- [[concepts/potential-outcomes|potential-outcomes]]