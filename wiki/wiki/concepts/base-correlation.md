---
title: Base Correlation
page_id: concepts/base-correlation
page_type: concept
revision_id: 1
created: 2026-05-05T23:20:00Z
updated: 2026-05-05T23:20:00Z
tags: [creditETF, CDO, correlation, credit-derivatives, tranche-pricing]
sources: [sources/lehman-2007-qcr-quarterly]
related: [concepts/cdo-tranches, concepts/bespoke-cdo, concepts/correlation-skew]
---

# Base Correlation

**Base correlation** is a market standard framework for pricing CDO tranches using the one-factor Gaussian copula model. It addresses the phenomenon of correlation skew by allowing correlation to depend on the tranche's position in the capital structure.

## Definition

The base correlation surface ρ(K,T) gives the single correlation that should be used for all credits in the one-factor Gaussian copula model to compute the expected loss of a **base tranche** with detachment point K at time T.

A base tranche is a tranche from 0% to K% attachment.

## Calibration

For standard indices (e.g., CDX IG), base correlation is calibrated via bootstrapping:

1. Start with equity tranche (0-3% for CDX IG)
2. Find correlation that matches market price
3. Move up capital structure (3-7%, 7-10%, etc.)
4. Each mezzanine tranche is combination of two base tranches
5. Repeat for each maturity (5Y, 7Y, 10Y)

**Standard CDX IG strikes:** 3%, 7%, 10%, 15%, 30%

## Mapping Methods for Bespoke Tranches

Bespoke portfolios require mapping rules to apply index-calibrated correlations.

### No-Mapping (NM)
```
K_Eq = K_B
```
Uses index BC surface directly. Benchmark method.

### At-The-Money (ATM)
```
K_Eq/EPL_S = K_B/EPL_B
```
Normalizes by expected portfolio loss. Can produce arbitrage.

### Probability Matching (PM)
```
P(L_T^S > K_Eq) = P(L_T^B > K_B)
```
Matches probability of tranche wipeout.

### Tranche Loss Proportion (TLP)
```
ETL(K_Eq,ρ)/EPL_S = ETL(K_B,ρ)/EPL_B
```
Matches fraction of expected loss in base tranche. **Best performing method empirically.**

## Empirical Results

Testing mapping of iTraxx S6 and CDX HY7 to CDX IG7 (January 2007):

| Method | Performance |
|--------|-------------|
| TLP | Best overall |
| PM | Second best |
| NM | Overestimates equity |
| ATM | Poor for senior tranches |

## Ideal Mapping Properties

- Intuitive and theoretically justified
- Sensitive only to correlation, not spread levels
- Stable with respect to market changes
- No arbitrage introduction
- Easy to implement
- Works for wide range of portfolio risks

## See Also

- [[concepts/cdo-tranches]]
- [[concepts/correlation-skew]]
- [[concepts/bespoke-cdo]]
- [[sources/lehman-2007-qcr-quarterly]]
