---
title: Bespoke CDO
page_id: concepts/bespoke-cdo
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- CDO
- credit-derivatives
- tranche-pricing
- correlation
- creditETF
sources:
- sources/lehman-2007-qcr-quarterly
related:
- concepts/base-correlation
- concepts/cdo-tranches
mind_map_priority: medium
schema_version: 2
uuid: 863a64e7-fdfe-5833-86d4-76807ec65dd5
content_hash: sha256:d53ce692bdba5ab90763bce822ef0f8931a078cbb11125e9c0fcbe9be1bba6ea
---

<!-- AUTHORED REGION START -->
# Bespoke CDO

A CDO written on a custom portfolio rather than on a standard index. Because there are no liquid quotes for the bespoke portfolio itself, its tranches must be priced by borrowing correlation information from the liquid index tranches — which is the whole problem.

## The Mapping Problem

Correlations are calibrated from index tranches. A **mapping rule** decides which index detachment point K_Eq corresponds to the bespoke detachment point K_B. [[sources/lehman-2007-qcr-quarterly|Baheti & Morgan (2007)]] compare four:

| Method | Rule | Note |
|---|---|---|
| No-Mapping (NM) | K_Eq = K_B | Benchmark; overestimates equity |
| At-The-Money (ATM) | K_Eq/EPL_S = K_B/EPL_B | Normalises by expected portfolio loss; can produce arbitrage; poor for senior tranches |
| Probability Matching (PM) | P(L_T^S > K_Eq) = P(L_T^B > K_B) | Matches probability of tranche wipeout; needs smoothing for discrete loss distributions |
| Tranche Loss Proportion (TLP) | ETL(K_Eq,ρ)/EPL_S = ETL(K_B,ρ)/EPL_B | Matches fraction of expected loss in the base tranche |

## What Works

Testing on 31 January 2007 data, mapping iTraxx S6 and CDX HY7 onto CDX IG7, **TLP performed best**, followed by PM. ATM gave poor results, particularly for senior tranches, and NM overestimated equity tranche prices.

## What a Good Mapping Should Do

The properties Baheti & Morgan set out are worth stating separately from the methods, because they are the test any new rule has to pass: intuitive and theoretically justified; sensitive to correlation but not to spread levels; stable under market changes; introducing no arbitrage; easy to implement; and working across a wide range of portfolio risks.

The ATM failure is instructive — normalising by expected loss is intuitive but is not arbitrage-safe, and it needs extrapolation when the bespoke is much riskier or much safer than the index.

## See Also

[[concepts/base-correlation|Base Correlation]] · [[concepts/cdo-tranches|CDO Tranches]] · [[entities/lehman-brothers|Lehman Brothers]]

**Not yet written:** `concepts/correlation-skew`, `concepts/gaussian-copula`

<!-- AUTHORED REGION END -->
