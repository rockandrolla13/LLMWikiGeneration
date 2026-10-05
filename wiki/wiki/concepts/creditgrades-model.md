---
abstraction_level: intermediate
concept_type: model
content_hash: sha256:1a2479e99f72a4eb71972a60a7ae0474176a0acb055cb9c57c5a997b44fb37db
created: '2026-10-05T15:52:11Z'
page_id: concepts/creditgrades-model
page_type: concept
related:
- concepts/structural-models
- concepts/merton-model
- concepts/capital-structure-arbitrage
- concepts/credit-default-swap-spread
revision_id: 1
schema_version: 2
sources:
- sources/finger-2002-creditgrades-technical-document
- sources/yu-2006-how-profitable-capital-structure-arbitrage
tags:
- credit-risk
- structural-models
- cds
title: CreditGrades Model
updated: '2026-10-05T15:52:11Z'
updated_by: op_afa4380123f6
uuid: c3764d58-d007-5022-b69a-c4e0037951fc
---

<!-- AUTHORED REGION START -->
# CreditGrades Model

## Definition

An industry structural credit model published in 2002 by RiskMetrics Group with Deutsche Bank, Goldman Sachs and JPMorgan. It builds on first-passage default in the Black and Cox tradition, with a default barrier whose level is uncertain (lognormal recovery). It maps share price, a long-window historical equity volatility and debt per share into a closed-form survival probability and CDS spread. The barrier uncertainty lifts short-dated spreads above what a plain Merton model gives, and the model became the usual engine for capital structure arbitrage trades.

## Sources

- [[sources/finger-2002-creditgrades-technical-document|CreditGrades Technical Document]]
- [[sources/yu-2006-how-profitable-capital-structure-arbitrage|How Profitable Is Capital Structure Arbitrage?]]

## Related Concepts

- [[concepts/structural-models|Structural Models]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
<!-- AUTHORED REGION END -->