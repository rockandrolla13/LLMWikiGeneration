---
title: Multi-output Gaussian processes for multi-population longevity modelling
page_id: sources/huynh-2021-mogp-longevity
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Nhan Huynh
- Mike Ludkovski
year: 2021
venue: Annals of Actuarial Science
doi: 10.1017/S1748499521000142
tags:
- gaussian-processes
- mortality-modelling
- multi-population
- machine-learning
- kriging
- longevity
related:
- sources/tsai-2020-hierarchical-mortality
- concepts/gaussian-processes
- concepts/multi-population-mortality
- concepts/kriging
- entities/mike-ludkovski
mind_map_priority: high
schema_version: 2
uuid: f361702c-0fb5-50bb-a729-c2b346719463
content_hash: sha256:2b965659ad3e85db6d5980ecd621812c9fcfe87fd51ecb3f2a1dff58f4e97ebf
---

<!-- AUTHORED REGION START -->
# Multi-output Gaussian Processes for Multi-population Longevity Modelling

**Authors:** Nhan Huynh, [[entities/mike-ludkovski|Mike Ludkovski]]

**Year:** 2021

**Venue:** Annals of Actuarial Science

**Institution:** UC Santa Barbara

## Summary

Develops a [[concepts/gaussian-processes|Gaussian process]] framework for jointly modelling mortality across 2-10 populations, treating populations as levels of a factor covariate with cross-population dependence captured through spatial covariance.

## Motivation

### Why Multi-Population Models?
1. **Predictive accuracy:** Aggregate data to better capture trends vs. noise
2. **Model risk reduction:** Increase forecast credibility
3. **Information fusion:** Use recently released "foreign" data to update domestic forecasts
4. **Coherent scenarios:** Avoid unrealistic crossover/divergence in joint forecasts

### Limitations of Existing Approaches
- Lee-Carter extensions have many parameters (2L+2 factors for L populations)
- Computational bottlenecks with many populations
- Limited to 2 populations (baseline + spread)

## Key Contributions

### 1. Multi-Output GP (MOGP) Framework
- Treats populations as categorical input with 0/1 encoding
- Squared-exponential kernel for Age-Year dimensions
- Cross-population covariance captured via product kernel
- Scales to ~10 populations

### 2. Intrinsic Coregionalisation Model (ICM)
For dimension reduction when L ≥ 4:
- Each output is linear combination of Q latent GPs
- Reduces parameters from L(L-1)/2 to Q×L
- Kronecker structure speeds computation 3-4x
- BIC criterion for selecting rank Q

### 3. Coherent Forecasting
- Generates internally consistent joint scenarios
- No post-hoc coherence adjustments needed
- Full uncertainty quantification (posteriors for mortality and improvement factors)

### 4. Non-Rectangular Data Handling
- Handles asynchronously released HMD data
- "Communication matrix" for missing outputs
- Enables contemporary forecasts with partial data

## Data

- Human Mortality Database (HMD)
- 16 European countries
- Ages 50-84, Years 1990-2016
- Both genders

## Results

- MOGP improves predictive accuracy over single-population GPs
- ICM (rank 2) preferred by BIC
- Information fusion beneficial when populations are correlated
- Stan implementation provides Bayesian uncertainty quantification

## See Also

- [[concepts/gaussian-processes|Gaussian Processes]]
- [[concepts/multi-population-mortality|Multi-Population Mortality]]
- [[concepts/kriging|Kriging]]
- [[sources/tsai-2020-hierarchical-mortality|Tsai & Wu 2020 (Hierarchical Mortality)]]

<!-- AUTHORED REGION END -->
