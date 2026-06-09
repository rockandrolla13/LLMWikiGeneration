---
created: '2026-05-17T16:44:06Z'
mind_map_priority: medium
page_id: concepts/data-leakage
page_type: concept
related:
- concepts/bias-variance-tradeoff
- concepts/look-ahead-bias
- concepts/look-ahead-bias-data-mining
- concepts/overfitting-in-alpha-research
- concepts/trading-strategy-overfitting
- concepts/walk-forward-analysis
revision_hash: sha256:ffed8585f7b91f99
revision_id: 2
sources:
- sources/huyen-2022-designing-ml-systems
tags:
- ai-engineering
- look-ahead-bias
title: Data Leakage
updated: '2026-06-09T12:00:00Z'
updated_by: wiki-batch-ai-engineering-2026-05-17
---

# Data Leakage

## Definition

The unintended exposure of information from outside the training distribution (e.g., target leakage, leakage through preprocessing, time leakage) that inflates offline metrics but causes failures in production.

## Sources

- [[sources/huyen-2022-designing-ml-systems|Designing Machine Learning Systems]]

## Related Concepts

- [[concepts/look-ahead-bias]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/bias-variance-tradeoff|bias-variance-tradeoff]]
- [[concepts/look-ahead-bias-data-mining|look-ahead-bias-data-mining]]
- [[concepts/overfitting-in-alpha-research|overfitting-in-alpha-research]]
- [[concepts/trading-strategy-overfitting|trading-strategy-overfitting]]
- [[concepts/walk-forward-analysis|walk-forward-analysis]]