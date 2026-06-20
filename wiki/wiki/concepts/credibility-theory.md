---
title: Credibility Theory
page_id: concepts/credibility-theory
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- actuarial-science
- statistics
- bayesian-methods
- insurance
sources:
- sources/namora-2021-hierarchical
- sources/tsai-2020-hierarchical-mortality
related:
- concepts/buhlmann-straub-model
- concepts/hierarchical-credibility-model
- concepts/lee-carter-model
mind_map_priority: medium
schema_version: 2
uuid: 516ff2f7-e31c-5e3e-932a-6aa354d261b2
content_hash: sha256:14de452e76818a5a8bff7e142e024e030b969cff3c4da6cc002782b15fd28e19
---

<!-- AUTHORED REGION START -->
# Credibility Theory

Credibility theory provides a framework for combining individual experience with collective information to make optimal predictions, originally developed for insurance ratemaking.

## Core Idea

"How much should we trust individual experience vs. class averages?"

$$\text{Credibility Estimate} = Z \cdot \text{Individual Experience} + (1-Z) \cdot \text{Class Average}$$

Where $Z$ is the **credibility factor** (0 to 1).

## Historical Development

| Model | Year | Key Contribution |
|-------|------|-----------------|
| Limited Fluctuation | 1918 | Ad-hoc credibility rules |
| Bühlmann | 1967 | Least squares optimal credibility |
| Bühlmann-Straub | 1970 | Unequal exposure/weights |
| Hachemeister | 1975 | Regression credibility |
| Hierarchical | 1970s+ | Multi-level structures |

## Bühlmann Credibility

For experience $X_1, \ldots, X_n$ from a risk with true mean $\theta$:

$$\hat{\theta} = Z \cdot \bar{X} + (1-Z) \cdot \mu$$

Where:
$$Z = \frac{n}{n + k}, \quad k = \frac{E[\text{Var}(X|\theta)]}{\text{Var}(E[X|\theta])}$$

The parameter $k$ balances within-risk vs. between-risk variance.

## Bayesian Interpretation

Credibility estimates are:
- Best linear approximations to Bayesian posterior means
- Exact Bayesian posteriors for normal-normal models
- Robust to distributional assumptions

## Applications

- **Insurance pricing**: Premium calculation for groups
- **Mortality modelling**: Small population mortality rates
- **Quality control**: Process monitoring
- **Finance**: Portfolio estimation

## See Also

- [[concepts/buhlmann-straub-model|Bühlmann-Straub Model]]
- [[concepts/hierarchical-credibility-model|Hierarchical Credibility Model]]
- [[sources/namora-2021-hierarchical|Hierarchical Credibility Model (2021)]]

<!-- AUTHORED REGION END -->
