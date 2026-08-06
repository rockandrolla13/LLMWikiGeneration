---
title: CDO Tranches
page_id: concepts/cdo-tranches
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
- concepts/bespoke-cdo
mind_map_priority: medium
schema_version: 2
uuid: f59ff478-1bef-5b35-8e41-fddf81004e75
content_hash: sha256:fe614fd8f1d59c23fdd894870641430d6ceafb9312c3240d20340372727870dd
---

<!-- AUTHORED REGION START -->
# CDO Tranches

Slices of a portfolio's loss distribution, each defined by an attachment and a detachment point. A tranche absorbs losses only once cumulative portfolio losses exceed its attachment point, and is wiped out once they reach its detachment point.

## Capital Structure and Standard Strikes

For the standard CDX IG index the market quotes tranches at detachment points of **3%, 7%, 10%, 15% and 30%**, across 5Y, 7Y and 10Y maturities ([[sources/lehman-2007-qcr-quarterly|Baheti & Morgan, Lehman Brothers 2007]]). The 0–3% slice is the **equity tranche**; slices above it are mezzanine and senior.

## Base Tranches

Pricing is organised around **base tranches** — tranches running from 0% up to a detachment point K. Any mezzanine tranche is expressed as the difference of two base tranches, which is what makes the [[concepts/base-correlation|base correlation]] framework work.

The calibration walks up the capital structure:

1. Start with the equity tranche (0–3% for CDX IG).
2. Find the correlation that matches its market price.
3. Move up (3–7%, 7–10%, …), each mezzanine tranche being a combination of two base tranches.
4. Repeat for each maturity.

## Why Correlation Is Tranche-Specific

A single correlation input does not reprice the whole capital structure. Correlation has to depend on where the tranche sits — the phenomenon the base correlation surface ρ(K,T) is built to absorb. Equity and senior tranches have opposite exposures to correlation, which is why the market quotes a surface rather than a number.

Tranches on portfolios that are not the standard indices are covered under [[concepts/bespoke-cdo|Bespoke CDO]].

## See Also

[[concepts/base-correlation|Base Correlation]] · [[concepts/bespoke-cdo|Bespoke CDO]] · [[entities/lehman-brothers|Lehman Brothers]]

**Not yet written:** `concepts/correlation-skew`, `concepts/gaussian-copula`, `concepts/expected-tranche-loss`

<!-- AUTHORED REGION END -->
