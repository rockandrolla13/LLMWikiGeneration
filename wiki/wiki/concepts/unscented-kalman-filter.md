---
title: "Unscented Kalman Filter"
page_id: concepts/unscented-kalman-filter
page_type: concept
created: 2026-04-26T03:00:00Z
updated: 2026-04-26T03:00:00Z
tags: [kalman-filter, nonlinear-estimation, state-space-models, sigma-points]
related: [concepts/kalman-filter, concepts/state-space-models, concepts/nelson-siegel-model]
sources: [sources/shi-2022-cds-options-comovement, sources/kumar-2022-liquidity-adjusted-afns]
---

## Definition

The Unscented Kalman Filter (UKF) is a nonlinear extension of the [[concepts/kalman-filter|Kalman filter]] that uses deterministic sampling (sigma points) to capture the mean and covariance of state distributions propagated through nonlinear transformations. It avoids the linearization required by the Extended Kalman Filter (EKF).

## Motivation

### Standard Kalman Filter Limitation

Standard Kalman filter requires linear state-space models:
```
x_t = A * x_{t-1} + w_t      (linear state transition)
y_t = H * x_t + v_t          (linear observation)
```

### Nonlinear Systems

Many financial models have nonlinear relationships:
- Bond prices as nonlinear functions of yields
- Option prices via Black-Scholes
- CDS spreads from hazard rates

### Extended Kalman Filter (EKF)

EKF linearizes via Taylor expansion:
- Compute Jacobians of f() and h()
- Apply linear Kalman filter with linearized matrices

**Problems**:
- Bias from truncating higher-order terms
- Jacobians may be difficult/impossible to compute
- Poor performance with high nonlinearity

## Unscented Transform

Key innovation: Approximate the probability distribution, not the nonlinear function.

### Sigma Point Selection

For n-dimensional state with mean x_bar and covariance P:

Generate 2n+1 sigma points:
```
X_0 = x_bar
X_i = x_bar + (sqrt((n+lambda)*P))_i,      i = 1,...,n
X_{n+i} = x_bar - (sqrt((n+lambda)*P))_i,  i = 1,...,n
```

Where:
- lambda = alpha^2 * (n + kappa) - n (scaling parameter)
- (sqrt())_i denotes i-th column of matrix square root

### Weights

Mean weights:
```
W_0^m = lambda / (n + lambda)
W_i^m = 1 / (2*(n + lambda)),  i = 1,...,2n
```

Covariance weights:
```
W_0^c = lambda / (n + lambda) + (1 - alpha^2 + beta)
W_i^c = 1 / (2*(n + lambda)),  i = 1,...,2n
```

Parameters:
- alpha: Controls spread of sigma points (typically 0.001-1)
- beta: Incorporates prior knowledge (beta=2 optimal for Gaussian)
- kappa: Secondary scaling (usually 0 or 3-n)

### Transform Through Nonlinearity

```
Y_i = g(X_i)  for each sigma point
```

### Recover Statistics

Mean:
```
y_bar = sum_i W_i^m * Y_i
```

Covariance:
```
P_yy = sum_i W_i^c * (Y_i - y_bar) * (Y_i - y_bar)'
```

## UKF Algorithm

### Prediction Step

1. Generate sigma points from x_{t-1|t-1}, P_{t-1|t-1}
2. Propagate through state transition: X^-_{t,i} = f(X_{t-1,i})
3. Compute predicted mean and covariance:
   - x_{t|t-1} = sum_i W_i^m * X^-_{t,i}
   - P_{t|t-1} = sum_i W_i^c * (X^-_{t,i} - x_{t|t-1})(X^-_{t,i} - x_{t|t-1})' + Q

### Update Step

1. Generate sigma points from x_{t|t-1}, P_{t|t-1}
2. Transform through measurement function: Y_{t,i} = h(X_{t,i})
3. Compute measurement statistics:
   - y_{t|t-1} = sum_i W_i^m * Y_{t,i}
   - P_yy = sum_i W_i^c * (Y_{t,i} - y_{t|t-1})(Y_{t,i} - y_{t|t-1})' + R
   - P_xy = sum_i W_i^c * (X_{t,i} - x_{t|t-1})(Y_{t,i} - y_{t|t-1})'
4. Kalman gain and update:
   - K_t = P_xy * P_yy^{-1}
   - x_{t|t} = x_{t|t-1} + K_t * (y_t - y_{t|t-1})
   - P_{t|t} = P_{t|t-1} - K_t * P_yy * K_t'

## Applications in Finance

### CDS-Options Co-movement

[[sources/shi-2022-cds-options-comovement|Shi et al. (2022)]]:
- CDS spread is nonlinear function of hazard rate factors
- UKF extracts level, slope, curvature from CDS curve
- Enables analysis of CDS-volatility surface relationship

### Term Structure Estimation

[[sources/kumar-2022-liquidity-adjusted-afns|Kumar & Virmani (2022)]]:
- Bond prices nonlinear in yield factors
- AFNS model requires nonlinear measurement equation
- UKF provides accurate estimation for Indian government bonds
- Better handles liquidity-adjusted pricing function

## UKF vs EKF

| Aspect | EKF | UKF |
|--------|-----|-----|
| Linearization | First-order Taylor | None (sigma points) |
| Jacobians | Required | Not needed |
| Accuracy | O(2) for mean | O(3) for Gaussian |
| Complexity | O(n^3) + Jacobian cost | O(n^3) |
| Implementation | More complex (derivatives) | Simpler |
| Robustness | Sensitive to strong nonlinearity | More robust |

## Advantages

1. **Derivative-free**: No Jacobian computation needed
2. **Higher accuracy**: Captures second-order moments correctly
3. **Easier implementation**: Just function evaluations
4. **Robust**: Works well even with strong nonlinearity

## Limitations

1. **Gaussian assumption**: Sigma points designed for Gaussian
2. **Computational cost**: 2n+1 function evaluations per step
3. **Parameter tuning**: alpha, beta, kappa affect performance
4. **No optimality**: Unlike KF, UKF is not optimal estimator

## Related Concepts

- [[concepts/kalman-filter|Kalman Filter]] - linear case
- [[concepts/state-space-models|State Space Models]] - general framework
- [[concepts/nelson-siegel-model|Nelson-Siegel Model]] - common application
- [[concepts/extended-kalman-filter|Extended Kalman Filter]] - alternative approach
