---
title: "On Forecasting the Term Structure of Credit Spreads"
page_id: sources/krishnan-2007-credit-spread-forecast
page_type: source
created: 2026-04-26T02:00:00Z
updated: 2026-04-26T02:00:00Z
tags: [credit-spreads, term-structure, forecasting, yield-curve, macroeconomic-factors]
authors: [C.N.V. Krishnan, Peter H. Ritchken, James B. Thomson]
year: 2007
journal: Federal Reserve Bank of Cleveland Working Paper
institution: [Case Western Reserve University, Federal Reserve Bank of Cleveland]
related: [concepts/credit-spread-curve, concepts/term-structure, concepts/yield-curve-forecasting, concepts/diebold-li-model]
---

# On Forecasting the Term Structure of Credit Spreads

## Summary

Investigates firm-by-firm credit spread forecasting using the shape of credit-spread curves and riskless yield curves. Finds that current credit-spread and riskless-yield curves contain essentially all information necessary for predicting future credit spreads - additional macro and firm-specific variables provide no incremental benefit.

## Key Findings

- **Shape Matters**: Credit-spread curve shape (level, slope, curvature) improves on spot/forward models
- **Riskless Curve Informative**: Riskless yield curve factors significantly improve credit spread forecasts
- **Sufficiency Result**: Credit-spread + riskless curves impound all relevant market/firm information
- **Macro Variables Not Helpful**: Additional macro, market, or firm variables don't improve forecasts

## Methodology

- Modified Diebold-Li 3-factor model for credit-spread curves
- Panel and firm-by-firm regressions
- Both in-sample and out-of-sample testing
- 6-month ahead forecasts for 5-year credit spreads

## Key Results

| Model | Out-of-Sample Performance |
|-------|--------------------------|
| Spot (random walk) | Baseline |
| Credit-spread factors | Substantial improvement |
| + Riskless factors | Further improvement |
| + Macro/firm variables | No additional improvement |

- Average absolute prediction error: 31 basis points (6-month ahead, 5-year spreads)
- Credit-spread factors model beats spot for >80% of firms

## Factor Structure

### Credit Spread Factors
- Level, slope, and curvature of firm credit-spread curve
- 2-year and 5-year spreads change same direction only ~60% of time

### Riskless Yield Factors
- Level, slope, and curvature of Treasury curve
- Well-known correlation between credit spreads and interest rates

## Key Concepts

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/term-structure|Term Structure]]
- [[concepts/diebold-li-model|Diebold-Li Model]]
- [[concepts/yield-curve-forecasting|Yield Curve Forecasting]]

## Implications

1. Shape of credit-spread curve is not sufficient statistic
2. Riskless yield curve contains incremental information
3. Macro forecasts don't improve predictions
4. Supports affine-like models where yields summarize information

## Related Sources

- [[sources/huang-2025-global-credit-spread-puzzle|Huang et al. (2025)]] - credit spread puzzle
- [[sources/feng-2025-predicting-bond-returns|Feng et al. (2025)]] - ML bond prediction
