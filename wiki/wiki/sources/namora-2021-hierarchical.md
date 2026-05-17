---
title: "Hierarchical Credibility Model"
page_id: sources/namora-2021-hierarchical
page_type: source
source_type: conference-paper
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [F. Namora, S. Nurrohmah, I. Fithriani]
year: 2021
venue: AIP Conference Proceedings
doi: 10.1063/5.0059047
tags: [credibility-theory, insurance, premium-calculation, hierarchical-models, buhlmann-straub]
related: [sources/tsai-2020-hierarchical-mortality, concepts/credibility-theory, concepts/buhlmann-straub-model]
mind_map_priority: medium
---

# Hierarchical Credibility Model

**Authors:** F. Namora, S. Nurrohmah, I. Fithriani

**Year:** 2021

**Venue:** AIP Conference Proceedings (6th International Symposium on Current Progress in Mathematics and Sciences)

**Institution:** Department of Mathematics, Universitas Indonesia

## Summary

This paper develops a [[concepts/hierarchical-credibility-model|hierarchical credibility model]] that accommodates more than one risk factor, providing a better description of complex insurance data structures compared to simpler models.

## Key Contributions

### 1. Hierarchical Extension of Bühlmann-Straub
- Extends the [[concepts/buhlmann-straub-model|Bühlmann-Straub model]] to handle multiple levels of risk factors
- Uses orthogonal projection in Hilbert spaces for estimation
- Handles structural parameters with zero variance at upper levels

### 2. Estimation Methods
Two methods for estimating structural parameters:
- **Ohlsson method**
- **Bühlmann-Gisler method**

### 3. Premium Calculation
- Hypothetical mean used as benchmark for premium calculation
- Estimation via linear combination of past observations
- More realistic than single-level Bühlmann-Straub model

## Mathematical Framework

The credibility estimator takes the form of a weighted mean:
- Weights based on precision (inverse of mean square error)
- Combines past observations with prior knowledge
- Uses general intuitive principle for weight derivation

## Key Claims

1. Hierarchical credibility better describes complex insurance data than flat models
2. The method handles cases where upper-level variance estimates are zero
3. Comparison with Bühlmann-Straub shows hierarchical approach is more realistic

## Applications

- Insurance premium determination
- Multi-level risk classification
- Property and casualty insurance

## See Also

- [[concepts/credibility-theory|Credibility Theory]]
- [[concepts/buhlmann-straub-model|Bühlmann-Straub Model]]
- [[sources/tsai-2020-hierarchical-mortality|Tsai & Wu 2020 (Hierarchical Mortality)]]
