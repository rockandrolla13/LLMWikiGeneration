---
title: "Market Co-movement Between Credit Default Swap Curves and Option Volatility Surfaces"
page_id: sources/shi-2022-cds-options-comovement
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [credit-default-swaps, implied-volatility, options, unscented-kalman-filter, nelson-siegel, market-comovement]
authors: [Yukun Shi, Charalampos Stasinakis, Yaofei Xu, Cheng Yan]
year: 2022
related: [concepts/kalman-filter, concepts/nelson-siegel-model, concepts/credit-default-swaps, concepts/implied-volatility-surface, concepts/unscented-kalman-filter]
---

## Summary

This paper analyzes the co-movement between the Credit Default Index (CDX) curve and the S&P 500 index's option volatility surface. Using the Unscented Kalman Filter (UKF) with Nelson-Siegel parameterization, the authors identify level, slope, and curvature factors in both markets and examine their interconnections.

## Key Contributions

1. **Nelson-Siegel for Hazard Rates**: Links no-arbitrage model on hazard rates (Carr & Wu 2010) to N-S model, validating N-S application to CDS curves
2. **Joint Parametric Modeling**: Uses N-S for CDS and DLF (Deterministic Linear Function) for volatility surface
3. **Factor Co-movement Analysis**: Examines relationship between level, slope, curvature of both surfaces
4. **Stock Return Bridge**: Shows S&P 500 return mediates relationship between CDS and volatility markets

## Methodology

### Nelson-Siegel for CDS Curve

Hazard rate curve modeled as:
h(tau) = beta_1 + beta_2 * exp(-lambda*tau) + beta_3 * (lambda*tau) * exp(-lambda*tau)

Where:
- beta_1: Level (long-term default intensity)
- beta_2: Slope (term structure steepness)
- beta_3: Curvature (hump shape)

### Unscented Kalman Filter

Uses UKF instead of standard Kalman filter because:
- CDS spread is nonlinear function of factors
- Better handling of non-Gaussian distributions
- Sigma point approximation for state propagation

### Factor Dynamics

Factors follow VAR(1) process:
X_t = Phi * X_{t-1} + epsilon_t

Measurement equation links observed spreads to latent factors.

## Data

- **CDS**: Investment-grade CDX index (ratings > BBB)
- **Options**: S&P 500 index options from OptionMetrics
- **Period**: January 2002 to December 2019 (939 weekly observations)
- **Volatility Surface**: 5 moneyness levels x 6 maturities

## Key Findings

1. **Direct Channel**: CDS level correlates with vol level (consistent with Carr & Wu URC theory)

2. **Indirect Channel via Stock Return**:
   - CDS slope correlates with vol slope through stock return
   - CDS level affects vol smile skewness

3. **Financial Crisis Impact**: Co-movement strengthens after 2008-09 global financial crisis

4. **After Controlling for Stock Return**: Relationship between markets becomes insignificant

## Theoretical Foundation

Based on Carr & Wu (2010, 2011):
- Default arrival rate impacts option discount rate
- Deep OTM puts capture default probability
- Unit Recovery Claim (URC) bridges CDS and options

## Related Concepts

- [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] for nonlinear estimation
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]] for curve fitting
- [[concepts/credit-default-swaps|Credit Default Swaps]] market
- [[concepts/implied-volatility-surface|Implied Volatility Surface]] dynamics

## Citations

Shi, Y., Stasinakis, C., Xu, Y., & Yan, C. (2022). Market co-movement between credit default swap curves and option volatility surfaces. International Review of Financial Analysis, 82, 102192.
