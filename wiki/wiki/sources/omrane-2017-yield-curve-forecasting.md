---
title: "Forecasting the Yield Curve of Bonds: A Government Dynamic Factor Approach"
page_id: sources/omrane-2017-yield-curve-forecasting
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [yield-curve, kalman-filter, nelson-siegel, dynamic-factor-model, bond-pricing, forecasting]
authors: [Walid Ben Omrane, Chao He, Zhongzhi Lawrence He, Samir Trabelsi]
year: 2017
related: [concepts/kalman-filter, concepts/nelson-siegel-model, concepts/yield-curve, concepts/state-space-models, concepts/dynamic-factor-model]
---

## Summary

This paper develops a unified dynamic factor approach based on the Diebold-Li (2006) and Nelson-Siegel (1987) three-factor model to forecast yield curve movements. The key innovation is treating the decay parameter lambda as a free parameter estimated from data, rather than fixing it as in prior literature.

## Key Contributions

1. **Free Decay Parameter**: Estimates lambda dynamically instead of fixing it, capturing richer yield curve dynamics
2. **State-Space Implementation**: Uses Kalman filter for efficient parameter and factor extraction
3. **Superior Forecasting**: Outperforms existing models, especially at medium and long horizons
4. **Comprehensive Comparison**: Benchmarks against Fama-Bliss, Cochrane-Piazzesi, random walk, AR(1), VAR(1)

## Methodology

### Nelson-Siegel Model

Yield at maturity tau:
y(tau) = beta_1 + beta_2 * [(1-exp(-lambda*tau))/(lambda*tau)] + beta_3 * [(1-exp(-lambda*tau))/(lambda*tau) - exp(-lambda*tau)]

Where:
- beta_1: Level factor (long-term yields)
- beta_2: Slope factor (spread between long and short)
- beta_3: Curvature factor (medium-term hump)
- lambda: Decay rate (shape of factor loadings)

### State-Space Formulation

**State Equation** (factor dynamics):
[beta_1,t; beta_2,t; beta_3,t] = A + B * [beta_1,t-1; beta_2,t-1; beta_3,t-1] + epsilon_t

**Measurement Equation**:
Y_t = Lambda(lambda) * [beta_1,t; beta_2,t; beta_3,t] + u_t

Lambda(lambda) contains the Nelson-Siegel factor loadings.

### Kalman Filter Estimation

- Extracts latent factors (level, slope, curvature)
- Estimates factor dynamics parameters
- Jointly estimates decay parameter lambda
- Maximum likelihood for all parameters

## Data

- US Treasury yield curve
- Multiple maturities (3-month to 10-year)
- Monthly observations

## Results

### In-Sample Fit
- Dynamic approach produces best fit to historical data
- Kalman filter highly efficient

### Out-of-Sample Forecasting

| Horizon | Dynamic Factor | Diebold-Li | Random Walk |
|---------|---------------|------------|-------------|
| 1 month | Moderate | Good | Best |
| 6 months | Good | Moderate | Poor |
| 12 months | Best | Poor | Poor |

**Key Finding**: Dynamic model dominates at medium (6-month) and long (12-month) horizons but trails at short horizons due to efficiency-robustness tradeoff.

## Cautions

- Kalman filter trades off robustness for efficiency
- Short-maturity, short-horizon forecasts less reliable
- Economic shocks can cause sudden breaks that Kalman filter adapts to slowly

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] for state estimation
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]] for yield curves
- [[concepts/yield-curve|Yield Curve]] dynamics
- [[concepts/dynamic-factor-model|Dynamic Factor Model]] framework

## Citations

Ben Omrane, W., He, C., He, Z. L., & Trabelsi, S. (2017). Forecasting the yield curve of bonds: A government dynamic factor approach. Managerial Finance, 43(7), 774-793.
