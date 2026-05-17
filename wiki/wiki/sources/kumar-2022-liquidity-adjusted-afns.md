---
title: "Term Structure Estimation with Liquidity-Adjusted Affine Nelson Siegel Model"
page_id: sources/kumar-2022-liquidity-adjusted-afns
page_type: source
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [term-structure, nelson-siegel, unscented-kalman-filter, liquidity-risk, indian-bonds, emerging-markets, affine-term-structure]
authors: [Sudarshan Kumar, Vineet Virmani]
year: 2022
related: [concepts/kalman-filter, concepts/nelson-siegel-model, concepts/unscented-kalman-filter, concepts/liquidity-risk, concepts/affine-term-structure-models]
---

## Summary

This paper implements the Arbitrage-Free Nelson-Siegel (AFNS) model for Indian Government bonds while explicitly incorporating liquidity effects. Using the Unscented Kalman Filter in a nonlinear state-space setting, the authors demonstrate that accounting for both security-specific and systematic funding liquidity significantly improves term structure estimation.

## Key Contributions

1. **Liquidity-Augmented AFNS**: First application of liquidity-adjusted AFNS to emerging markets
2. **Two-Dimensional Liquidity**: Incorporates both idiosyncratic (security-specific) and systematic (funding) liquidity
3. **Heteroscedasticity Correction**: Accounts for liquidity-induced error variance differences
4. **UKF Implementation**: Nonlinear state-space approach for accurate estimation

## Theoretical Framework

### Standard AFNS Model

The Dynamic Nelson-Siegel yield equation:
y(tau) = L_t + S_t * [(1-exp(-lambda*tau))/(lambda*tau)] + C_t * [(1-exp(-lambda*tau))/(lambda*tau) - exp(-lambda*tau)]

Where L, S, C follow VAR(1) dynamics and satisfy no-arbitrage restrictions.

### Liquidity Extensions

**Security-Specific Liquidity**:
- Trading volume (TurnoverRatio)
- Bond age
- Duration

**Systematic Funding Liquidity**:
- Modeled as latent factor (Fontaine & Garcia 2011)
- Captures market-wide liquidity conditions
- Correlated with India VIX

### Extended Pricing Equation

Bond price includes liquidity adjustment:
P_i = f(L,S,C,tau) * exp(phi * Liquidity_i) + epsilon_i

Where error variance is inversely related to liquidity.

## Methodology

### Unscented Kalman Filter

Used because:
- Bond prices are nonlinear functions of factors
- Standard EKF may introduce bias
- UKF provides better accuracy without Jacobian computation

### Sigma Point Generation

- 2n+1 sigma points for n-dimensional state
- Weights determined by tuning parameters (alpha, beta, kappa)
- Propagated through nonlinear bond pricing function

## Data

- Indian Government Securities (G-Secs)
- Period: 2008-2018
- Weekly observations (typically Wednesdays for liquidity)
- Multiple maturities across yield curve

## Key Findings

1. **Model Fit**: Liquidity-adjusted AFNS significantly improves in-sample fit
2. **Likelihood Ratio Test**: Rejects standard AFNS in favor of extended model
3. **Funding Liquidity Factor**:
   - Correlates with banking system liquidity
   - Correlates with India VIX
   - Captures Taper Tantrum (2013) and demonetization (2016)

## Practical Implications

- Central banks: Better yield curve estimation for policy analysis
- Portfolio managers: Account for liquidity premium in bond pricing
- Risk managers: Understand liquidity risk in emerging market bonds

## Related Concepts

- [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] for nonlinear estimation
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]] for yield curves
- [[concepts/liquidity-risk|Liquidity Risk]] in bond markets
- [[concepts/affine-term-structure-models|Affine Term Structure Models]]

## Citations

Kumar, S., & Virmani, V. (2022). Term structure estimation with liquidity-adjusted Affine Nelson Siegel model: A nonlinear state space approach applied to the Indian bond market. Applied Economics, 54(6), 648-669.
