---
title: Sophia Sun
page_id: entities/sophia-sun
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-26 10:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- researcher
- conformal-prediction
- time-series
- copulas
- ucsd
affiliation: University of California, San Diego
email: shs066@ucsd.edu
related:
- entities/rose-yu
- concepts/conformal-prediction
- concepts/copulas
mind_map_priority: medium
schema_version: 2
uuid: 93002282-7696-5cea-9faf-2433633befe5
content_hash: sha256:2ac15d9da3f0f84ccddd0d079717f5ce8b30162a63cc47940d89e880ceca0e45
---

<!-- AUTHORED REGION START -->
# Sophia Sun

**Sophia Sun** is a researcher at the University of California, San Diego, working in [[entities/rose-yu|Rose Yu]]'s Spatiotemporal Learning (STL) Lab. Her research focuses on uncertainty quantification for deep learning models, particularly in time series forecasting.

## Research Contributions

### CopulaCPTS
Sun is the first author of the **CopulaCPTS** paper ([[sources/sun-2022-copula-cpts]]), published at ICLR 2024. Key contributions:

1. **Copula-based conformal prediction**: Novel approach using [[concepts/copulas|copulas]] to model the joint distribution of uncertainty across multiple prediction time steps

2. **Full-horizon validity guarantee**: Proved finite-sample validity for the entire forecast horizon, not just individual steps

3. **Two-step calibration procedure**: Split calibration for marginal CDFs and copula, enabling rigorous theoretical guarantees

4. **Significant efficiency improvements**: 30-50% reduction in confidence region size compared to Bonferroni-based methods

## Key Ideas

From the CopulaCPTS paper:
- "By using copulas to model the uncertainty jointly over future time steps, we can shrink the confidence regions significantly while maintaining validity"
- The empirical copula provides a nonparametric way to capture dependency without introducing bias
- Frechet-Hoeffding bounds show that Bonferroni correction is a lower bound for copula functions, guaranteeing CopulaCPTS is more efficient

## Research Focus

- Distribution-free uncertainty quantification
- Multi-step time series forecasting
- [[concepts/conformal-prediction|Conformal prediction]] methods
- Applications: autonomous vehicle trajectory prediction, COVID-19 forecasting

## Collaborations

- [[entities/rose-yu|Rose Yu]] - PhD advisor and senior author
- UC San Diego STL Lab members

## Code & Resources

CopulaCPTS implementation: https://github.com/Rose-STL-Lab/CopulaCPTS

## Related Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/copulas|Copulas]]
- [[concepts/multi-step-conformal-prediction|Multi-step Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]

<!-- AUTHORED REGION END -->
