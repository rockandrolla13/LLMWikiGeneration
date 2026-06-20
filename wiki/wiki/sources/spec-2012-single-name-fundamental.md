---
title: 'Specification Draft: Single Name Fundamental Analysis'
page_id: sources/spec-2012-single-name-fundamental
page_type: source
revision_id: 1
created: 2026-05-05 23:15:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- creditETF
- credit-analysis
- fundamental-analysis
- relative-value
related:
- concepts/credit-spread-curve
- concepts/spread-per-turn-of-leverage
- concepts/relative-value-analysis
schema_version: 2
uuid: 656ecc97-3960-50c1-a02c-4d6875d65569
content_hash: sha256:3adbce09924010ebf777f3e490c4db18d06c54eea6b315068cdad204b00b2f69
---

<!-- AUTHORED REGION START -->
# Specification Draft: Single Name Fundamental Analysis

**Type:** Internal specification document
**Date:** August 2012 (v. 080212)
**Focus:** European corporate single-name credit analysis

## Summary

An internal framework document outlining a comprehensive, semi-automated approach for fundamental credit analysis of European single-name corporates. The specification covers data gathering, ratio calculation, and relative value assessment using both static and dynamic methods.

## Key Components

### Data Collection (Building the Factset)

**Step 1A - Accounting/Fundamental Data:**
- Primary sources: Bloomberg, Capital IQ, CS Holt
- Required history: 3 years minimum (7-10 years for EBITDA, net debt, free cash flow)
- Quarterly data needed for LTM calculations

**Step 1B - Forward-Looking Estimates:**
- Equity analyst estimates from Bloomberg
- Credit analyst forecasts from research reports (more labor-intensive)
- Annual forecasts adequate for most purposes

**Step 1C - Sector/Macroeconomic Data:**
- Country growth rates, industry forecasts
- Used to sense-check individual company estimates

### Key Ratios Calculated

**Capitalisation & Solvency:**
- Net debt/EBITDA, Total debt/EBITDA
- EBIT/Interest expense, EBITDA/Interest expense
- Funds from operations/debt ratios

**Liquidity:**
- Current ratio, Quick ratio
- Cash conversion cycle metrics

**Profitability:**
- ROA, ROE, ROIC
- Margin metrics (gross, EBITDA, EBIT, net income)

**Valuation Multiples:**
- EV/EBITDA, EV/Revenue, EV/EBIT
- P/E, P/B

### Static Relative Value Analysis

**[[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage (SPL)]]:**
```
SPL = 5Y CDS Spread / (Net Debt/EBITDA)
```
- Compares company SPL to sector average
- Identifies rich/cheap names within sector
- Uses both LTM and NTM (forward) leverage

**Spread vs. Interest Coverage:**
- Similar framework using ICR as denominator
- Expected negative correlation with spreads

**Spread vs. Rating:**
- Maps agency ratings to numerical buckets
- Identifies mispricing vs. rating-implied spread

### Dynamic Relative Value Analysis

**Cyclicality vs. Liquidity Screen:**
- Identifies EBITDA decline required to force refinancing
- Inputs: cash, LTM EBITDA, interest expense, capex
- Useful for shorter/more volatile business cycle themes

**Ratings Drift Screen:**
- Regression-based model predicting ratings from fundamentals
- Identifies upgrade/downgrade candidates
- Trade templates around rating watch status

## Applications

- Cross-sectional sector analysis
- Intra-sector relative value identification
- Stress testing and scenario analysis
- Ratings migration prediction

## Related Concepts

- [[concepts/credit-spread-curve]]
- [[concepts/spread-per-turn-of-leverage]]
- [[concepts/relative-value-analysis]]
- [[concepts/leverage-ratios]]

<!-- AUTHORED REGION END -->
