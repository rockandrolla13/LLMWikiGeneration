---
title: Lee-Carter Model
page_id: concepts/lee-carter-model
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- mortality-modelling
- actuarial-science
- demography
- forecasting
sources:
- sources/tsai-2020-hierarchical-mortality
- sources/huynh-2021-mogp-longevity
related:
- concepts/hierarchical-credibility-model
- concepts/multi-population-mortality
- concepts/longevity-risk
- entities/cary-tsai
mind_map_priority: high
schema_version: 2
uuid: 9a0dc1c6-0bc0-54a8-b0d0-58444adb7e6c
content_hash: sha256:959ccc9d819551e2486059ff386575fbebf49d126e4a745d40006763477a62f3
---

<!-- AUTHORED REGION START -->
# Lee-Carter Model

The Lee-Carter model is the foundational stochastic mortality model, decomposing log mortality rates into age and period effects.

## Specification

$$\ln(m_{x,t}) = a_x + b_x \kappa_t + \epsilon_{x,t}$$

Where:
- $m_{x,t}$ = Central death rate at age $x$ in year $t$
- $a_x$ = Average log mortality at age $x$
- $b_x$ = Age-specific sensitivity to mortality improvement
- $\kappa_t$ = Time-varying mortality index
- $\epsilon_{x,t}$ = Error term

## Estimation

Typically via Singular Value Decomposition (SVD):
1. Compute $a_x$ as row means of $\ln(m_{x,t})$
2. Apply SVD to centered matrix
3. First singular vector gives $b_x$, first singular value × time component gives $\kappa_t$
4. Renormalize: $\sum_x b_x = 1$ and $\sum_t \kappa_t = 0$

## Forecasting

Model $\kappa_t$ as a random walk with drift:
$$\kappa_t = \kappa_{t-1} + \delta + \epsilon_t$$

This captures continued mortality improvement.

## Extensions

| Extension | Description |
|-----------|-------------|
| Renshaw-Haberman | Adds cohort effect ($\gamma_{t-x}$) |
| CBD | Age-period-cohort for older ages |
| Li-Lee | Multi-population extension |
| Cairns-Blake-Dowd | Logit mortality, stochastic volatility |

## Limitations

- Single time series ($\kappa_t$) drives all ages
- No cohort effects in basic model
- May not capture structural changes
- Uncertainty in parameters often underestimated

## See Also

- [[concepts/hierarchical-credibility-model|Hierarchical Credibility Model]]
- [[concepts/multi-population-mortality|Multi-Population Mortality]]
- [[concepts/longevity-risk|Longevity Risk]]
- [[sources/tsai-2020-hierarchical-mortality|Hierarchical Credibility Theory for Multi-Country Mortality (2020)]]

<!-- AUTHORED REGION END -->
