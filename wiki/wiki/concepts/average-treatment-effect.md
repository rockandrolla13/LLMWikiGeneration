---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/average-treatment-effect
page_type: concept
related:
- concepts/causal-inference
- concepts/doubly-robust-estimation
- concepts/ip-weighting-marginal-structural-models
- concepts/potential-outcomes
revision_hash: sha256:2780ae14b9bc1a6aef9a002baabd7d7f7f392f2e7a73fddd6661277a9cd9b92e
revision_id: 1
sources:
- sources/gentzel-2021-osrct-evaluation
tags: []
title: Average treatment effect (ATE)
updated: '2026-06-20T01:03:51Z'
updated_by: creditmacro-batch
schema_version: 2
uuid: 0de88de2-6263-58ce-ac69-4766f1d66a01
content_hash: sha256:5cb5aca8225d7a197e75e7e50a32963a56ee100a5113bcab4b0f8f0c91fe8eb4
---

<!-- AUTHORED REGION START -->
# Average treatment effect (ATE)

## Definition

The expected difference in outcome between treatment and control, E[Y(1)] - E[Y(0)], which an RCT estimates without bias as E[Y|T=1] - E[Y|T=0]; the primary estimand evaluated in this paper (with risk difference used for binary outcomes).

## Sources

- [[sources/gentzel-2021-osrct-evaluation|How and Why to Use Experimental Data to Evaluate Methods for Observational Causal Inference]]

## Related Concepts

- [[concepts/causal-inference|causal-inference]]
- [[concepts/doubly-robust-estimation|doubly-robust-estimation]]
- [[concepts/ip-weighting-marginal-structural-models|ip-weighting-marginal-structural-models]]
- [[concepts/potential-outcomes|potential-outcomes]]
<!-- AUTHORED REGION END -->
