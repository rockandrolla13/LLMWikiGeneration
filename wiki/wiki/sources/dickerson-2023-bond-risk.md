---
title: Priced risk in corporate bonds
page_id: sources/dickerson-2023-bond-risk
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Alexander Dickerson
- Philippe Mueller
- Cesare Robotti
year: 2023
venue: Journal of Financial Economics
doi: 10.1016/j.jfineco.2023.103707
tags:
- corporate-bonds
- asset-pricing
- capm
- factor-models
- liquidity-risk
related:
- sources/martin-2024-credit-curve
- concepts/bond-capm
- concepts/factor-models
- concepts/liquidity-risk
- entities/cesare-robotti
mind_map_priority: high
schema_version: 2
uuid: 6741638a-f02a-56cd-9a87-a99b582df6a6
content_hash: sha256:ff9b70a40ae64f168a5dda9048e67c6513c3d901b0c2d0183f9a3583f3c896da
---

<!-- AUTHORED REGION START -->
# Priced Risk in Corporate Bonds

**Authors:** Alexander Dickerson, Philippe Mueller, [[entities/cesare-robotti|Cesare Robotti]]

**Year:** 2023

**Venue:** Journal of Financial Economics

**Institutions:** UNSW Business School, Warwick Business School

## Summary

This paper challenges the empirical support for multifactor models in corporate bond pricing, showing that the bond CAPM is not dominated by more complex factor models. Only traded liquidity shows marginal incremental explanatory power.

## Key Findings

### 1. Bond CAPM Sufficiency
- Common factor pricing in corporate bonds is difficult to establish
- Previously proposed bond risk factors lack incremental power over the market factor
- Only traded liquidity (LRF) shows some marginal explanatory power

### 2. Data Issues with Prior Research
- BBW (Bai, Bali, Wen 2019) factors have lead/lag construction errors
- DRF, CRF, LRF factors not properly constructed
- Truncating market factor tails artificially favors alternative factors

### 3. Nontraded Factors Fail
Examined factors show no pricing power:
- Systematic volatility (VIX exposure)
- Macroeconomic uncertainty
- Long-run consumption risk
- Illiquidity factors

## Methodology

### Statistical Tools
- Mean-variance frontier distance analysis
- Maximum Sharpe ratio analysis
- Misspecification-robust time-series tests
- GLS cross-sectional regressions (following Lewellen et al. 2010)

### Data
- Enhanced TRACE database (July 2002 - December 2016)
- Mergent FISD for bond characteristics
- 31,348 bonds from 3,792 firms
- 861,524 bond-month observations

## Key Claims

1. Bond CAPM (single market factor) is not dominated by multifactor models
2. Previously documented factor premia are artifacts of data errors
3. GLS weighting substantially weakens apparent multifactor pricing
4. Model misspecification adjustments are critical for valid inference

## Implications

- Caution needed when evaluating corporate bond factor models
- Replication and data verification essential
- Simpler models may be sufficient for corporate bond pricing

## See Also

- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[sources/martin-2024-credit-curve|Martin 2024 (Credit Curve)]]

<!-- AUTHORED REGION END -->
