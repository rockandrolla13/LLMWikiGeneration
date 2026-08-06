---
title: Structural Models
page_id: concepts/structural-models
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- structural-models
- credit-risk
- merton-model
- bond-pricing
- credit-spreads
sources:
- sources/huang-2025-global-credit-spread-puzzle
related:
- concepts/merton-model
- concepts/credit-spread-puzzle
- concepts/bond-liquidity
mind_map_priority: medium
schema_version: 2
uuid: e4ccdaf7-b7e1-5a38-a2c7-36ef8cf53846
content_hash: sha256:4981a30d23f4ff0795384af39252a1d41b9b9f09af472271dc648930649ce2c0
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

<!-- AUTHORED REGION END -->
