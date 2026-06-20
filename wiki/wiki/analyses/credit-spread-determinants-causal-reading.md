---
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: high
page_id: analyses/credit-spread-determinants-causal-reading
page_type: analysis
query: What are the main factors that affect credit spread changes in the medium term,
  and what is the do-calculus of it?
related:
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/babecky-2013-leading-indicators-crisis-incidence
- sources/babecky-2014-developed-country-crisis-ewi
- sources/pearl-2018-book-of-why
- sources/hernan-2020-causal-inference-what-if
- concepts/credit-spread-changes
- concepts/credit-spread-puzzle
- concepts/merton-model
- concepts/bond-market-segmentation
- concepts/corporate-bond-liquidity-premium
- concepts/principal-components-analysis
- concepts/baa-corporate-bond-spread
- concepts/credit-to-gdp-gap
- concepts/limits-to-arbitrage
- concepts/causal-inference
- concepts/ladder-of-causation
- concepts/do-operator
- concepts/causal-diagram
- concepts/confounding
- concepts/back-door-front-door-adjustment
- concepts/instrumental-variables
revision_hash: sha256:01d7ce6cb163ab49960481ea34890f4387c8fae37d1e767358b44cf03b12f30b
revision_id: 1
sources:
- sources/collin-dufresne-2001-determinants-credit-spread-changes
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/babecky-2013-leading-indicators-crisis-incidence
- sources/babecky-2014-developed-country-crisis-ewi
- sources/pearl-2018-book-of-why
- sources/hernan-2020-causal-inference-what-if
tags:
- credit-spreads
- causal-inference
- do-calculus
- confounding
- credit-macro
title: 'Credit-Spread Determinants: An Empirical and Do-Calculus Reading'
updated: '2026-06-20T01:03:51Z'
updated_by: op_db16de9c3673
schema_version: 2
uuid: 57d4d4c6-f7f9-51a2-8205-5f820448b3e1
content_hash: sha256:b0013a03e60d23f6b00158c58455b8c9ff72ef20adc354a2b830e677bb17b7bb
---

<!-- AUTHORED REGION START -->
# Credit-Spread Determinants: An Empirical and Do-Calculus Reading

**Query:** What are the main factors that affect credit spread changes in the medium term, and what is the do-calculus of it?

> **Caveat:** Part A is grounded in ingested sources. Part B is a *synthesis* bridging the credit and causal-inference branches; no single source applies do-calculus to credit spreads. The causal diagram is an illustrative hypothesis, not a sourced result.

## A. What moves credit spreads in the medium term

The anchor is [[sources/collin-dufresne-2001-determinants-credit-spread-changes|Collin-Dufresne, Goldstein & Martin (2001)]], who regress monthly [[concepts/credit-spread-changes|credit-spread changes]] on structurally motivated variables. Three tiers emerge:

1. **Theory-motivated ([[concepts/merton-model|Merton-model]]) drivers** — individually significant but jointly weak (adj. R^2 ~ 19-25%): firm leverage / equity return, the risk-free rate level (a rate rise *lowers* spreads), yield-curve slope, volatility (asymmetric: spreads widen sharply on vol increases), jump risk (the implied-vol smirk), and the business climate (S&P 500 return, more significant than firm-specific equity returns).
2. **A dominant unnamed aggregate factor** — a single common factor explains ~71% of residual variation ([[concepts/principal-components-analysis|PCA]] of residuals). Aggregate factors dominate firm-specific ones, pointing to [[concepts/bond-market-segmentation|bond-market segmentation]] and a [[concepts/corporate-bond-liquidity-premium|liquidity-driven supply/demand premium]]. [[sources/kapadia-2012-limited-arbitrage-equity-credit|Kapadia & Pu (2012)]] add that equity-credit markets are imperfectly integrated, with [[concepts/limits-to-arbitrage|limits to arbitrage]] sustaining short-horizon mispricings.
3. **Macro / slower-moving factors** — from [[sources/babecky-2013-leading-indicators-crisis-incidence|Babecky et al. (2013]]/[[sources/babecky-2014-developed-country-crisis-ewi|2014)]]: the [[concepts/baa-corporate-bond-spread|BAA corporate-bond spread]] (global risk aversion) and the [[concepts/credit-to-gdp-gap|credit-to-GDP gap]] (the most robust multi-year early-warning indicator).

**Bottom line:** medium-term spreads are driven less by firm fundamentals than by an aggregate liquidity/risk-aversion factor the structural variables fail to capture - the [[concepts/credit-spread-puzzle|credit-spread puzzle]].

## B. The do-calculus reading (synthesis)

CDM's regression lives on **rung 1 of the [[concepts/ladder-of-causation|ladder of causation]]** - association, P(dSpread | drivers). The causal question is rung 2: P(dSpread | [[concepts/do-operator|do]](leverage), do(rate), ...).

The bridge: **CDM's single latent common factor is, in [[concepts/causal-diagram|causal-diagram]] terms, an unobserved common cause - a [[concepts/confounding|confounder]]** that fans out to equity returns, rates, and spreads. The rung-1 coefficients therefore mix each driver's direct effect with a spurious path through this factor - which is precisely why R^2 is low and the residuals share one big factor.

Identification strategies from the causal branch:
- **[[concepts/back-door-front-door-adjustment|Back-door adjustment]]** requires *measuring* the latent factor (which CDM cannot) - so the effect is unidentified from regression alone.
- The **[[concepts/merton-model|Merton]] structural model** acts as a mechanism (front-door-like) restriction: leverage -> firm value V -> spread.
- **[[concepts/instrumental-variables|Instrumental variables]]** - an instrument shifting leverage but independent of the latent factor would recover the causal effect.

**Conclusion:** the credit-spread puzzle is, in part, a *confounding* problem. Moving from "what correlates with spreads" to "what moves spreads under intervention" requires measuring the latent factor, a structural model, or a valid instrument - not a larger kitchen-sink regression.

## Sources

- [[sources/collin-dufresne-2001-determinants-credit-spread-changes|Collin-Dufresne et al. 2001]]
- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Kapadia & Pu 2012]]
- [[sources/babecky-2013-leading-indicators-crisis-incidence|Babecky et al. 2013]]
- [[sources/babecky-2014-developed-country-crisis-ewi|Babecky et al. 2014]]
- [[sources/pearl-2018-book-of-why|Pearl 2018, The Book of Why]]
- [[sources/hernan-2020-causal-inference-what-if|Hernan & Robins 2020]]
<!-- AUTHORED REGION END -->
