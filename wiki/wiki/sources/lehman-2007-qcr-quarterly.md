---
title: 'QCR Quarterly Vol. 2007-Q1: Base Correlation Mapping & Trading Event Risk'
page_id: sources/lehman-2007-qcr-quarterly
page_type: source
revision_id: 1
created: 2026-05-05 23:15:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- creditETF
- base-correlation
- CDO
- event-risk
- LEVER
- quantitative-credit
institutions:
- entities/lehman-brothers
related:
- concepts/base-correlation
- concepts/lever-score
- concepts/cdo-tranches
- sources/trinh-2006-lever-framework
schema_version: 2
uuid: bb8ebec5-5d07-522c-867a-71bedf558484
content_hash: sha256:559adafc304c336a717b3170996bdcc428cbc14b417c79d58045b5026230383f
---

<!-- AUTHORED REGION START -->
# QCR Quarterly Vol. 2007-Q1

**Institution:** [[entities/lehman-brothers|Lehman Brothers]]
**Date:** March 7, 2007
**Type:** Quantitative Credit Research Quarterly

## Contents

This quarterly compilation contains four research articles on credit derivatives and quantitative credit strategies.

---

## Article 1: Base Correlation Mapping

**Authors:** Prasun Baheti, Sam Morgan

### Summary

Addresses pricing of bespoke CDO tranches using base correlation framework. Describes methods for mapping correlations calibrated from liquid index tranches to bespoke portfolios.

### Base Correlation Framework

**Definition:** The BC surface ρ(K,T) gives the single correlation used in one-factor Gaussian copula model to compute expected loss of base tranche with detachment K at time T.

**Calibration Process:**
1. Bootstrap from liquid index tranches (CDX IG: 3%, 7%, 10%, 15%, 30%)
2. Match market prices sequentially up capital structure
3. Interpolate for non-standard strikes/maturities

### Mapping Methods Compared

**1. No-Mapping (NM):**
- K_Eq = K_B (trivial)
- Uses index BC surface directly
- Benchmark for other methods

**2. At-The-Money (ATM):**
- K_Eq/EPL_S = K_B/EPL_B
- Normalizes by expected portfolio loss
- Can produce arbitrage; requires extrapolation for risky/safe bespokes

**3. Probability Matching (PM):**
- Match P(L_T^S > K_Eq) = P(L_T^B > K_B)
- Invariant: probability of tranche wipeout
- Requires smoothing for discrete loss distributions

**4. Tranche Loss Proportion (TLP):**
- ETL(K_Eq, ρ)/EPL_S = ETL(K_B, ρ)/EPL_B
- Invariant: fraction of expected loss in base tranche
- **Best performing method in tests**

### Empirical Results (Jan 31, 2007)

Mapping iTraxx S6 and CDX HY7 to CDX IG7:
- **TLP performs best**, followed by PM
- ATM gives poor results, especially for senior tranches
- NM overestimates equity tranche prices

---

## Article 2: Idiosyncratic Portfolio Risk in Non-Normal Markets

### Summary

Models portfolio idiosyncratic component using t-distribution rather than normal. Introduces entropy-based risk-adjusted diversification measure.

**Key Finding:** Tail index (degrees of freedom) depends on:
1. Risk-adjusted average of single-security tail index
2. Level of portfolio diversification

---

## Article 3: Trading Event Risk in Credit Markets using LEVER

### Summary

Follow-up to [[sources/trinh-2006-lever-framework|LEVER introduction paper]]. Analyzes LEVER as investment framework for alpha extraction.

**Key Findings:**
- LEVER-based trades perform well historically
- Low correlation with market and traditional credit strategies
- Useful for both benchmark-relative and absolute-return mandates

---

## Article 4: Introducing Lehman Brothers' CMetrics Framework

### Summary

New financial framework for improving quality of financial analysis and valuations. Helps analysts interpret financial statements to identify strengths/weaknesses and make informed judgments.

---

## Related Concepts

- [[concepts/base-correlation]]
- [[concepts/cdo-tranches]]
- [[concepts/lever-score]]
- [[concepts/bespoke-cdo]]

<!-- AUTHORED REGION END -->
