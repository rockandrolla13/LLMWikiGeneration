---
title: Multi-Population Mortality Modelling
page_id: concepts/multi-population-mortality
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- mortality-modelling
- actuarial-science
- demography
- longevity
sources:
- sources/huynh-2021-mogp-longevity
- sources/tsai-2020-hierarchical-mortality
related:
- concepts/lee-carter-model
- concepts/gaussian-processes
- concepts/hierarchical-credibility-model
- concepts/longevity-risk
- entities/mike-ludkovski
mind_map_priority: high
schema_version: 2
uuid: 3e3f4443-1a06-5037-990d-d218151c50e9
content_hash: sha256:34fc580cc84c62108ed5c1c9db73e5f1b871e39a2f8db55972e7900489663a06
---

<!-- AUTHORED REGION START -->
# Multi-Population Mortality Modelling

Multi-population mortality modelling jointly forecasts mortality for several related populations, exploiting cross-country or cross-group correlations.

## Motivation

- **Small populations**: Insufficient data for reliable single-population models
- **Coherence**: Forecasts should not diverge unrealistically
- **Hedging**: Basis risk between hedge instrument and liability population
- **Efficiency**: Borrow strength across similar populations

## Key Approaches

### Augmented Common Factor Models
Extend Lee-Carter with common and population-specific factors:
$$\ln(m_{x,t}^{(i)}) = a_x^{(i)} + B_x \mathbf{K}_t + b_x^{(i)} \kappa_t^{(i)} + \epsilon_{x,t}^{(i)}$$

### Li-Lee Model
Two-tier structure:
1. Common trend for all populations
2. Population-specific deviations (mean-reverting)

### Hierarchical Credibility
- Blend population data with regional/global patterns
- Optimal weighting based on data volume and variance structure

### Gaussian Processes (MOGP)
- Non-parametric flexible modelling
- Captures complex correlation structures
- Scales to 10+ populations efficiently

## Coherence Constraints

Forecasts should satisfy:
- **Divergence control**: Spreads don't explode
- **Ordering preservation**: If A > B historically, maintain relationship
- **Biological reasonableness**: No impossible mortality patterns

## Challenges

| Challenge | Impact |
|-----------|--------|
| Computational scaling | O(n³) for naive GP approaches |
| Structural breaks | COVID-19 disrupted patterns |
| Data quality | Different definitions across countries |
| Correlation estimation | Limited historical overlap |

## See Also

- [[concepts/lee-carter-model|Lee-Carter Model]]
- [[concepts/gaussian-processes|Gaussian Processes]]
- [[concepts/hierarchical-credibility-model|Hierarchical Credibility Model]]
- [[sources/huynh-2021-mogp-longevity|Multi-output Gaussian Processes for Multi-population Longevity Modelling (2021)]]

<!-- AUTHORED REGION END -->
