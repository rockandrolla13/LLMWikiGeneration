---
title: Bühlmann-Straub Model
page_id: concepts/buhlmann-straub-model
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- actuarial-science
- credibility-theory
- insurance-pricing
- statistics
sources:
- sources/namora-2021-hierarchical
related:
- concepts/credibility-theory
- concepts/hierarchical-credibility-model
mind_map_priority: medium
schema_version: 2
uuid: a4c716f1-9eaf-52be-b914-56768bf62f1c
content_hash: sha256:02c89f65ef9255005bc4c7f8461f9893feef29fe8108ea997a5159fe0a2c7d0a
---

<!-- AUTHORED REGION START -->
# Bühlmann-Straub Model

The Bühlmann-Straub model extends classical Bühlmann credibility to handle unequal exposures or weights across observations.

## Model Setup

For risk $i$ with observations $(X_{i1}, w_{i1}), \ldots, (X_{in_i}, w_{in_i})$ where $w_{ij}$ is the exposure/weight:

**Assumptions:**
1. $E[X_{ij}|\theta_i] = \mu(\theta_i)$ (conditional mean depends on risk parameter)
2. $\text{Var}(X_{ij}|\theta_i) = \sigma^2(\theta_i)/w_{ij}$ (variance inversely proportional to weight)
3. Observations conditionally independent given $\theta_i$

## Credibility Formula

$$\hat{\mu}_i = Z_i \cdot \bar{X}_i^w + (1 - Z_i) \cdot \hat{\mu}$$

Where:
- $\bar{X}_i^w = \sum_j w_{ij} X_{ij} / \sum_j w_{ij}$ (weighted average)
- $Z_i = w_{i\cdot} / (w_{i\cdot} + k)$ (credibility factor)
- $w_{i\cdot} = \sum_j w_{ij}$ (total weight)
- $k = E[\sigma^2(\theta)] / \text{Var}(\mu(\theta))$ (Bühlmann k)

## Parameter Estimation

**Within-variance** ($\sigma^2$):
$$\hat{\sigma}^2 = \frac{1}{n - I} \sum_i \sum_j w_{ij}(X_{ij} - \bar{X}_i^w)^2$$

**Between-variance** ($\tau^2$):
$$\hat{\tau}^2 = \frac{1}{I-1} \sum_i w_{i\cdot}(\bar{X}_i^w - \bar{X}^w)^2 - \frac{n-I}{n-w_0}\hat{\sigma}^2$$

Where $w_0$ is a correction term for unequal weights.

## Applications

- **Insurance ratemaking**: Policies with different exposures
- **Mortality rates**: Populations of different sizes
- **Quality control**: Products with varying sample sizes
- **Premium calculation**: Risk classes with unequal experience

## See Also

- [[concepts/credibility-theory|Credibility Theory]]
- [[concepts/hierarchical-credibility-model|Hierarchical Credibility Model]]
- [[sources/namora-2021-hierarchical|Hierarchical Credibility Model (2021)]]

<!-- AUTHORED REGION END -->
