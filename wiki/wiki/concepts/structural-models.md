---
content_hash: sha256:cdec3b804fddf4d5d711725003acb128e6e580934ece3862054a4505f4b889fe
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/structural-models
page_type: concept
related:
- concepts/merton-model
- concepts/credit-spread-puzzle
- concepts/bond-liquidity
revision_id: 2
schema_version: 2
sources:
- sources/huang-2025-global-credit-spread-puzzle
- sources/bai-2016-anchoring-cds-spreads-firm-fundamentals
- sources/bharath-2008-forecasting-default-merton-distance-to-default
- sources/carr-2011-american-puts-credit-protection
- sources/cremers-2008-individual-stock-option-prices-credit-spreads
- sources/finger-2002-creditgrades-technical-document
- sources/wang-2013-cds-spreads-variance-risk-premia
- sources/yu-2006-how-profitable-capital-structure-arbitrage
tags:
- structural-models
- credit-risk
- merton-model
- bond-pricing
- credit-spreads
title: Structural Models
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: e4ccdaf7-b7e1-5a38-a2c7-36ef8cf53846
---

<!-- AUTHORED REGION START -->
# Structural Models

Credit models that derive default from a firm-value process: default happens when firm value falls to a debt-related threshold. Equity is a call option on firm value and risky debt a short put. The family starts with Merton (1974) — see [[concepts/merton-model|Merton Structural Model]].

## The Variants Used Here

[[sources/huang-2025-global-credit-spread-puzzle|Huang, Nozawa & Shi (2025)]] test three, and the differences between them are the point:

- **Black-Cox (1976)** — baseline, with a flat default boundary.
- **Collin-Dufresne–Goldstein (2001)** — stationary leverage, so the firm targets a leverage ratio rather than drifting.
- **He-Milbradt (2014)** — adds endogenous liquidity in the secondary debt market, with search and bargaining frictions.

They also use three alternative estimates of the default boundary (d^FS, d^BGY, d^HNS), which matters because the boundary is not directly observable and the spread implied is sensitive to it.

## The Calibration Failure

Once calibrated to historical default data and equity risk premia, the standard models "generate similar credit spreads and tend to substantially underpredict investment-grade corporate-Treasury spreads" ([[sources/huang-2025-global-credit-spread-puzzle|Huang et al. 2025]]). This is the [[concepts/credit-spread-puzzle|credit spread puzzle]], and it holds across seven of eight developed economies studied — Japan is the exception.

Adding liquidity closes much of the gap. Cross-sectional R² rises from 19–35% under Black-Cox to 34–79% under He-Milbradt. The implication is that a pure firm-value model is not enough: the frictions of the market the debt trades in are part of the price. See [[concepts/bond-liquidity|Bond Liquidity]].

## Open Questions

- If liquidity has to be bolted on to make structural models fit, is the firm-value channel still doing the work?
- Why does Japan not show the puzzle, when the same models are applied?

## See Also

[[concepts/merton-model|Merton Structural Model]] · [[concepts/credit-spread-puzzle|Credit Spread Puzzle]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[concepts/reduced-form-credit-models|Reduced-Form Credit Models]] · [[concepts/corporate-bonds|Corporate Bonds]]

**Not yet written:** `concepts/default-boundary`, `concepts/black-cox-model`

## Sources

- [[sources/yu-2006-how-profitable-capital-structure-arbitrage|How Profitable Is Capital Structure Arbitrage?]]
- [[sources/wang-2013-cds-spreads-variance-risk-premia|Credit Default Swap Spreads and Variance Risk Premia]]
- [[sources/finger-2002-creditgrades-technical-document|CreditGrades Technical Document]]
- [[sources/cremers-2008-individual-stock-option-prices-credit-spreads|Individual Stock-Option Prices and Credit Spreads]]
- [[sources/carr-2011-american-puts-credit-protection|A Simple Robust Link Between American Puts and Credit Protection]]
- [[sources/bharath-2008-forecasting-default-merton-distance-to-default|Forecasting Default with the Merton Distance to Default Model]]
- [[sources/bai-2016-anchoring-cds-spreads-firm-fundamentals|Anchoring Credit Default Swap Spreads to Firm Fundamentals]]
<!-- AUTHORED REGION END -->