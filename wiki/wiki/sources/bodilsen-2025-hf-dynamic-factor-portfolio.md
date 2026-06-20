---
title: Large-Dimensional Portfolio Selection with a High-Frequency-Based Dynamic Factor
  Model
page_id: sources/bodilsen-2025-hf-dynamic-factor-portfolio
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Simon T. Bodilsen
year: 2025
venue: Journal of Financial Econometrics
volume_issue_pages: 23(2), nbae018
doi: 10.1093/jjfinec/nbae018
tags:
- realized-covariance
- high-frequency-data
- factor-models
- hierarchical-clustering
- portfolio-selection
related:
- concepts/realized-covariance
- concepts/multivariate-realized-kernel
- concepts/hierarchical-clustering
- concepts/har-model
- concepts/minimum-variance-portfolio
- concepts/approximate-factor-models
- concepts/factor-models
- entities/simon-t-bodilsen
- entities/jianqing-fan
- entities/ole-barndorff-nielsen
- entities/neil-shephard
mind_map_priority: high
schema_version: 2
uuid: f12d42ec-c3e4-5e2a-9f5c-e65fee2b746c
content_hash: sha256:9264563e60df2c704b4a3519d0ddd7f3f21950991da5b997b6c2617953039631
---

<!-- AUTHORED REGION START -->
# Large-Dimensional Portfolio Selection with a High-Frequency-Based Dynamic Factor Model

**Authors:** [[entities/simon-t-bodilsen|Simon T. Bodilsen]]

**Venue:** *Journal of Financial Econometrics*, 23(2), nbae018 (2025)

**DOI:** [10.1093/jjfinec/nbae018](https://doi.org/10.1093/jjfinec/nbae018)

## Summary

Proposes a high-frequency-based dynamic factor model for forecasting large [[concepts/realized-covariance|realized covariance]] matrices of S&P 500 constituents, with observable ETF factors and a data-driven block-structured idiosyncratic covariance inferred via [[concepts/hierarchical-clustering|hierarchical clustering]]. The model is OLS-estimable, scales linearly, and outperforms standard multivariate volatility benchmarks in out-of-sample [[concepts/minimum-variance-portfolio|minimum-variance portfolio]] selection.

## Key Claims

1. Hierarchical clustering on idiosyncratic correlations recovers block structure more effectively than sector groupings
2. The model produces lower ex-post portfolio standard deviation and lower turnover than HEAVY, HAR-DRD, and DCC-style benchmarks at daily and weekly horizons
3. Components of the realized covariance can be estimated via the [[concepts/multivariate-realized-kernel|multivariate realized kernel]] and modeled with separable AR processes

## Concepts

- [[concepts/realized-covariance|Realized Covariance]] — central
- [[concepts/multivariate-realized-kernel|Multivariate Realized Kernel]] — central
- [[concepts/hierarchical-clustering|Hierarchical Clustering]] — central
- [[concepts/har-model|Heterogeneous Autoregressive Model]] — central
- [[concepts/minimum-variance-portfolio|Minimum Variance Portfolio]] — supporting
- [[concepts/approximate-factor-models|Approximate Factor Models]] — supporting
- [[concepts/factor-models|Factor Models]] — supporting

## Related Sources

(Leave empty for now — links will be added by future ingestions)

<!-- AUTHORED REGION END -->
