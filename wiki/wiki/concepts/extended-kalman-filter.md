---
title: Extended Kalman Filter
page_id: concepts/extended-kalman-filter
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- kalman-filter
- nonlinear-estimation
- state-space-models
sources: []
related:
- concepts/kalman-filter
- concepts/unscented-kalman-filter
- concepts/state-space-models
mind_map_priority: medium
schema_version: 2
uuid: c7ea7e68-7f25-5da9-bd32-c2c7296bcdba
content_hash: sha256:acde448889f64b80c5f1c26866368b03a32210a080b4ac02647c7b62f6c50280
---

<!-- AUTHORED REGION START -->
# Extended Kalman Filter

The oldest way to run a [[concepts/kalman-filter|Kalman filter]] on a nonlinear system: linearize the state transition and measurement functions around the current estimate, then apply the ordinary linear recursions to the linearized matrices.

## How It Works

The EKF takes a first-order Taylor expansion of the nonlinear functions f() and h(). That means computing their Jacobians at each step and substituting those in place of the transition and observation matrices the linear filter expects. Everything downstream — prediction, gain, update — is unchanged.

## Its Three Weaknesses

The [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] page states them plainly:

- **Bias** from truncating the higher-order terms of the expansion.
- **Jacobians** may be difficult or impossible to compute for the model at hand.
- **Poor performance** when the nonlinearity is strong.

Against the UKF the comparison runs: EKF linearizes by first-order Taylor and needs Jacobians, the UKF needs neither; EKF accuracy is second-order for the mean, the UKF is third-order in the Gaussian case; both are O(n³), but the EKF adds the Jacobian cost; the EKF implementation is more complex because it requires derivatives; the EKF is the more sensitive of the two to strong nonlinearity.

## Where the Wiki's Papers Landed

Nonlinearity is the normal case in the applications collected here — bond prices as nonlinear functions of yields, option prices through Black-Scholes, CDS spreads from hazard rates. Both applied papers in the wiki that faced it chose the UKF over the EKF: [[sources/shi-2022-cds-options-comovement|Shi et al. (2022)]] for CDS curve factors and [[sources/kumar-2022-liquidity-adjusted-afns|Kumar & Virmani (2022)]] for liquidity-adjusted AFNS estimation.

The [[concepts/kalman-filter|Kalman Filter]] page lists the EKF alongside the UKF, the particle filter (non-Gaussian, severely nonlinear) and the ensemble Kalman filter (high-dimensional) as the standard extensions.

## Thinness Note

The wiki holds no source that uses the EKF directly. Everything above is what the UKF and Kalman filter pages say about it, which is a comparison rather than a treatment.

## See Also

[[concepts/kalman-filter|Kalman Filter]] · [[concepts/unscented-kalman-filter|Unscented Kalman Filter]] · [[concepts/state-space-models|State-Space Models]] · [[concepts/nelson-siegel-model|Nelson-Siegel Model]]

[[concepts/particle-filter|Particle Filter]]

<!-- AUTHORED REGION END -->
