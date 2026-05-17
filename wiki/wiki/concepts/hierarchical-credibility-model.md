---
title: "Hierarchical Credibility Model"
page_id: concepts/hierarchical-credibility-model
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [credibility-theory, actuarial-science, mortality-modelling, bayesian-methods]
sources: [sources/tsai-2020-hierarchical-mortality, sources/namora-2021-hierarchical]
related: [concepts/credibility-theory, concepts/buhlmann-straub-model, concepts/lee-carter-model, concepts/multi-population-mortality, entities/cary-tsai]
mind_map_priority: high
---

# Hierarchical Credibility Model

Hierarchical credibility models extend classical credibility theory to multi-level data structures, optimally blending individual observations with group-level information.

## Basic Framework

For a hierarchical structure (e.g., countries within regions):

$$\hat{\theta}_{ij} = Z_{ij} \cdot \bar{X}_{ij} + (1 - Z_{ij}) \cdot \hat{\theta}_j$$

Where:
- $\hat{\theta}_{ij}$ = Credibility estimate for unit $i$ in group $j$
- $Z_{ij}$ = Credibility factor (0 to 1)
- $\bar{X}_{ij}$ = Individual experience
- $\hat{\theta}_j$ = Group-level estimate (which itself is a blend)

## Credibility Factor

$$Z_{ij} = \frac{n_{ij}}{n_{ij} + k_{ij}}$$

Where:
- $n_{ij}$ = Volume/exposure measure
- $k_{ij}$ = Bühlmann k (ratio of within to between variance)

## Application to Mortality

Tsai & Wu (2020) apply this to multi-country mortality:

1. **Individual level**: Country-specific mortality rates
2. **Group level**: Regional average (e.g., European countries)
3. **Global level**: Overall mortality pattern

The model optimally weights country data against regional patterns, particularly valuable for small populations.

## Advantages Over Lee-Carter

| Aspect | Lee-Carter | Hierarchical Credibility |
|--------|------------|--------------------------|
| Data borrowing | None (single population) | Systematic across hierarchy |
| Small populations | High variance | Stabilized by group info |
| Forecast intervals | Often too narrow | More realistic |
| Computational | SVD-based | Iterative credibility |

## See Also

- [[concepts/credibility-theory|Credibility Theory]]
- [[concepts/buhlmann-straub-model|Bühlmann-Straub Model]]
- [[concepts/lee-carter-model|Lee-Carter Model]]
- [[sources/tsai-2020-hierarchical-mortality|Hierarchical Credibility Theory for Multi-Country Mortality (2020)]]
