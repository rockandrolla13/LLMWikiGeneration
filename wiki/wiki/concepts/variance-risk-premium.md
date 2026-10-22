---
abstraction_level: intermediate
concept_type: metric
content_hash: sha256:d282fe24c1f541d2b7ffb7d1a61e44056c7015a50e487a093d54eae86fa01dce
created: '2026-10-05T15:52:32Z'
page_id: concepts/variance-risk-premium
page_type: concept
related:
- concepts/model-free-implied-variance
- concepts/credit-default-swap-spread
revision_id: 2
schema_version: 2
sources:
- sources/wang-2013-cds-spreads-variance-risk-premia
- sources/bendor-2021-systematic-investing-in-credit
tags:
- options
- volatility
- risk-premia
title: Variance Risk Premium
updated: '2026-10-22T15:27:29Z'
updated_by: op_955147eb8c65
uuid: 68d2288a-0e6d-590d-8290-211efa0dfd26
---

<!-- AUTHORED REGION START -->
# Variance Risk Premium

## Definition

The gap between risk-neutral expected variance, read from option prices, and physical expected variance, a forecast of realised variance. For a single stock, Wang, Zhou and Zhou (2013) argue the idiosyncratic parts of the two expectations cancel, so the firm-level premium isolates the firm's exposure to systematic variance risk. They find it explains CDS spread levels beyond leverage, volatility and the market-level premium.

## Sources

- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)
- [[sources/wang-2013-cds-spreads-variance-risk-premia|Credit Default Swap Spreads and Variance Risk Premia]]

## Related Concepts

- [[concepts/model-free-implied-variance|Model-Free Implied Variance]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
<!-- AUTHORED REGION END -->