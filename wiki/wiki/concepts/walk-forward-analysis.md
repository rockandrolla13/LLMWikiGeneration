---
abstraction_level: intermediate
concept_type: technique
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/walk-forward-analysis
page_type: concept
related:
- concepts/algorithmic-trading
- concepts/data-leakage
- concepts/look-ahead-bias
revision_hash: sha256:587ab49d4998f0790a556df15895649087d894c9c512edde2d99441aa2490581
revision_id: 1
sources:
- sources/pardo-2008-evaluation-optimization-trading-strategies
tags: []
title: Walk-Forward Analysis
updated: '2026-06-20T01:03:51Z'
updated_by: creditmacro-batch
schema_version: 2
uuid: eccc5c1f-2c8d-5a89-ab8e-299d522b96b3
content_hash: sha256:646d63e4f484a116a8250f47f3659dddf6f5b7623c44f455ed1c737ebe507afb
---

<!-- AUTHORED REGION START -->
# Walk-Forward Analysis

## Definition

A validation procedure repeatedly optimizing a strategy on an in-sample window and evaluating the selected parameters on the immediately following out-of-sample window, rolled through history; Pardo's central tool against overfitting.

## Sources

- [[sources/pardo-2008-evaluation-optimization-trading-strategies|The Evaluation and Optimization of Trading Strategies]]

## Related Concepts

- [[concepts/algorithmic-trading|algorithmic-trading]]
- [[concepts/data-leakage|data-leakage]]
- [[concepts/look-ahead-bias|look-ahead-bias]]
<!-- AUTHORED REGION END -->
