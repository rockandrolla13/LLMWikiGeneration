---
title: Measuring Credit-Spread Risk on a Single Issuer Basis
page_id: sources/pullirsch-2006-credit-spread-risk
page_type: source
revision_id: 1
created: 2026-05-05 23:15:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- creditETF
- credit-spread-risk
- zero-coupon-curves
- VaR
- bond-pricing
authors:
- entities/rainer-pullirsch
related:
- concepts/credit-spread-curve
- concepts/residual-variance
- concepts/zero-coupon-curve
schema_version: 2
uuid: 2cc09829-56b5-5949-b760-45edefd00704
content_hash: sha256:53776aabd5310b36e0e7be014f7b91669129914252f79337d28f72edccff6710
---

<!-- AUTHORED REGION START -->
# Measuring Credit-Spread Risk on a Single Issuer Basis

**Author:** [[entities/rainer-pullirsch|Rainer Pullirsch]], Bank Austria Creditanstalt
**Published:** Wirtschaft und Management, November 2006
**Focus:** Credit spread curve estimation and risk measurement

## Abstract

Presents a model for measuring credit-spread risk at the single issuer level. Details a method for calculating zero-coupon credit-spread curves from bond quotations with emphasis on numerical stability. Introduces residual variances to capture individual bond behavior and describes a three-level mapping procedure for illiquid issuers.

## Key Contributions

### Zero-Coupon Credit-Spread Curve Estimation

**Algorithm:**
1. Start with riskless zero-coupon term structure (derived from swap rates)
2. Add credit spread s(t) to discount cash flows
3. Minimize pricing error function across all issuer bonds
4. Use m = Q grid points for Q bonds

**Grid Point Selection:**
- Five different schemes for equidistant grid points
- Considers minimum and maximum time to maturity
- Uses cubic-spline interpolation between points

**Risk Factors:**
- Values at t ∈ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 25]
- Limited by actual maximum maturity of underlying bonds

### Numerical Stability

**Two Approaches:**
1. **Condition number method:** K < K_max for matrix A in linear system
2. **Coupon variation method (implemented):** Estimates sensitivity of spread curve to coupon changes

**Stability Control:**
- Maximum sensitivity Δ calculated for each grid scheme
- Reduce grid points (m → m-1) until stability criterion met
- Allows maximum 5% deviation between model and quoted prices

**Effect of Grid Reduction:**
- Smoother credit-spread curves with fewer grid points
- Trade-off between numerical stability and pricing accuracy

### Residual Variance

**Purpose:** Account for individual bond behavior beyond issuer-level curve

**Sources of Variation:**
- Currency differences in trading
- Liquidity differences
- Bond-specific factors

**Calculation Method:**
- Start with fewer grid points than bonds (m < n)
- Compute parallel shifts needed to exactly price each bond
- Calculate weighted returns and time-weighted variance (λ = 0.97)

### Three-Level Mapping Procedure

For issuers with limited liquid bonds:
1. **Issuer credit-spread curves** - direct estimation where possible
2. **Synthetic curves** - grouped by sector, rating, and region
3. **Bond and company-specific residuals** - capture idiosyncratic behavior

## Technical Details

**Riskless Rate Choice:**
- Uses swap rates rather than government bonds
- More liquid, reflects current term structure
- Slightly higher level due to counterparty/LIBOR risk

**Input Data Quality:**
- Minimum one quotation in time window
- Bond quotations loaded at 4 p.m. CET (±1.5 hours)
- Bid-ask spread filter: β = 4
- Deviation filter: μ = 2

## Applications

- Value-at-Risk calculation for credit portfolios
- Pricing credit derivatives (CDS)
- Single-issuer risk measurement

## Related Concepts

- [[concepts/credit-spread-curve]]
- [[concepts/residual-variance]]
- [[concepts/zero-coupon-curve]]
- [[concepts/value-at-risk]]

<!-- AUTHORED REGION END -->
