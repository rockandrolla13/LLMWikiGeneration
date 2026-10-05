---
abstraction_level: intermediate
concept_type: metric
content_hash: sha256:6e3184627700f0441ae66ba98500af56d5c941a64ff00cf2502f6cbe1e27929f
created: '2026-10-05T15:52:32Z'
page_id: concepts/model-free-implied-variance
page_type: concept
related:
- concepts/variance-risk-premium
revision_id: 1
schema_version: 2
sources:
- sources/wang-2013-cds-spreads-variance-risk-premia
tags:
- options
- volatility
title: Model-Free Implied Variance
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: a63eb3de-fb4d-560b-ac2a-0079cfce79c4
---

<!-- AUTHORED REGION START -->
# Model-Free Implied Variance

## Definition

The risk-neutral expected return variance over a horizon, computed by integrating option prices across all strikes with weights of one over strike squared, without assuming a pricing model. It uses the whole smile rather than a single at-the-money point, and stays valid when the underlying follows a jump-diffusion.

## Sources

- [[sources/wang-2013-cds-spreads-variance-risk-premia|Credit Default Swap Spreads and Variance Risk Premia]]

## Related Concepts

- [[concepts/variance-risk-premium|Variance Risk Premium]]
<!-- AUTHORED REGION END -->