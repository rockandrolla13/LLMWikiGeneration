---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:21d903334f74ce96139dd71969859199f7c61c207c475f3040e722f2bf2caefd
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/overfitting-in-alpha-research
page_type: concept
related:
- concepts/backtesting
- concepts/data-leakage
- concepts/look-ahead-bias
- concepts/autoresearch
- analyses/autoresearch-for-equity-to-credit-modelling
revision_id: 3
schema_version: 2
sources:
- sources/tulchinsky-2020-finding-alphas
- sources/marks-2003-whad-ya-know
- sources/karpathy-2026-autoresearch
tags: []
title: Overfitting in Alpha Research
updated: '2026-11-24T23:30:14Z'
updated_by: op_53f181d9343b
uuid: 7f3b4cf1-237c-5e32-88e8-fd3effa96088
---

<!-- AUTHORED REGION START -->
# Overfitting in Alpha Research

## Definition

The apparent discovery of a price-driving rule that is actually a spurious historical relationship; mitigated through parameter minimization, regularization, cross-validation, out-of-sample comparison, and economic rationale.

## Sources

- [[sources/tulchinsky-2020-finding-alphas|Finding Alphas: A Quantitative Approach to Building Trading Strategies (Second Edition)]]

## Related Concepts

- [[concepts/backtesting|backtesting]]
- [[concepts/data-leakage|data-leakage]]
- [[concepts/look-ahead-bias|look-ahead-bias]]

## In Howard Marks's Memos

- [[sources/marks-2003-whad-ya-know|Whad’Ya Know?]] (2003)
## When an Agent Runs the Search

An autonomous research loop can run about 100 experiments overnight against one validation set, so chance winners become likely. Karpathy's own guard was a transfer test: changes found on a small model were re-checked on a larger one. His agents also produced spurious results when compute was not held fixed. See [[sources/karpathy-2026-autoresearch|Autoresearch (Karpathy, 2026)]] and [[analyses/autoresearch-for-equity-to-credit-modelling|Autoresearch for Equity-to-Credit Modelling]].
<!-- AUTHORED REGION END -->
