---
created: 2026-04-26 10:00:00+00:00
mind_map_priority: medium
page_id: concepts/nadaraya-watson-estimator
page_type: concept
related:
- concepts/conformal-prediction
- concepts/kernel-methods
- concepts/kowcpi
- concepts/local-regression
revision_id: 2
sources:
- sources/lee-2024-kowcpi
tags:
- nonparametric-statistics
- kernel-methods
- regression
- time-series
- quantile-regression
title: Nadaraya-Watson Estimator
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 66ac0093-27f5-5c1e-9f75-df6e00748cd1
content_hash: sha256:b47cce8ff4b95e8301f7b85d117664bda4c6bcc76d379a2df05da4fb4f06e91c
---

<!-- AUTHORED REGION START -->
# Nadaraya-Watson Estimator

The **Nadaraya-Watson (NW) estimator** is a classical nonparametric method for estimating conditional expectations or distributions using kernel weighting. The **Reweighted Nadaraya-Watson (RNW)** variant introduces adjustment weights for improved bias properties, making it particularly useful for quantile regression in time-series [[concepts/conformal-prediction|conformal prediction]].

## Classic Nadaraya-Watson Estimator

Given observations $(\tilde{X}_i, \tilde{Y}_i)$, $i = 1, \ldots, n$, the NW estimator of $\mathbb{E}[\tilde{Y}|\tilde{X}=x]$ is:

$$\hat{m}(x) = \frac{\sum_{i=1}^n K_h(x - \tilde{X}_i) \tilde{Y}_i}{\sum_{i=1}^n K_h(x - \tilde{X}_i)}$$

where $K_h(u) = h^{-p}K(h^{-1}u)$ is a scaled kernel function with bandwidth $h$.

## Reweighted Nadaraya-Watson (RNW) Estimator

The RNW estimator (Hall et al., 1999) extends the classic NW by introducing **adjustment weights** $p_i(\tilde{X})$ to improve bias properties while maintaining the distribution function property.

### Adjustment Weights
The adjustment weights are obtained by maximizing the empirical log-likelihood:
$$\max_{p_1, \ldots, p_n} \sum_{i=1}^n \log p_i(\tilde{X})$$

subject to:
- $p_i(\tilde{X}) \geq 0$ for all $i$
- $\sum_{i=1}^n p_i(\tilde{X}) = 1$
- $\sum_{i=1}^n p_i(\tilde{X})(\tilde{X}_i - \tilde{X}) = 0$

### Final Weights
The final RNW weights combine adjustment weights with kernel weights:
$$\hat{W}_i(\tilde{X}) = \frac{p_i(\tilde{X}) K_h(\tilde{X} - \tilde{X}_i)}{\sum_{j=1}^n p_j(\tilde{X}) K_h(\tilde{X} - \tilde{X}_j)}$$

### RNW CDF Estimator
The RNW estimate of the conditional CDF $\mathbb{P}(\tilde{Y} \leq b | \tilde{X})$ is:
$$\hat{F}(b|\tilde{X}) = \sum_{i=1}^n \hat{W}_i(\tilde{X}) \mathbf{1}_{\{\tilde{Y}_i \leq b\}}$$

## Computational Efficiency

The adjustment weights can be computed via a simple one-dimensional convex minimization:

$$p_i(\tilde{X}) = \frac{1}{n} \cdot \frac{1}{1 + \lambda^\top(\tilde{X}_i - \tilde{X})}$$

where $\lambda \in \mathbb{R}^p$ minimizes:
$$L(\lambda; \tilde{X}) = \frac{1}{n} \sum_{i=1}^n \log(1 + \lambda^\top(\tilde{X}_i - \tilde{X}))$$

## Properties

### Advantages over Classic NW
1. **Better bias**: Combines favorable bias properties of local linear estimator
2. **Distribution function**: Remains a proper CDF (unlike local linear)
3. **Consistency**: Consistent under strongly mixing conditions

### Theoretical Guarantees
Under strong mixing assumptions with $\alpha(\tau) = O(\tau^{-(2+\delta)})$ for some $\delta > 0$:
$$\hat{F}(y|x) - F(y|x) = O_p\left(h^2 + \sqrt{\frac{1}{nh^p}}\right)$$

## Applications in Conformal Prediction

The RNW estimator is central to the [[concepts/kowcpi|KOWCPI]] method:
1. Quantile regression on non-conformity scores
2. Learning data-adaptive weights for time-series data
3. Achieving asymptotic conditional [[concepts/coverage-guarantee|coverage]]

## Bandwidth Selection

### Optimal Bandwidth
The theoretically optimal bandwidth minimizing asymptotic MSE:
$$h^* \sim n^{-1/(w+4)}$$
where $w$ is the dimension of $\tilde{X}$.

### Practical Selection
- Cross-validation (computationally expensive)
- Nonparametric AIC (Cai & Tiwari, 2000): More efficient for dependent data

## Kernel Requirements

For valid theoretical guarantees, the kernel $K: \mathbb{R}^p \to \mathbb{R}$ should satisfy:
1. Nonnegative, bounded, continuous
2. Compactly supported
3. Symmetric: $\int u K(u) du = 0$
4. $\int uu^\top K(u) du = \mu_2 I$ for some $\mu_2 > 0$

Common choices: Epanechnikov kernel $K(u) = k(\|u\|)$ with $k(t) = \frac{3}{4}(1-t^2)_+$.

## Historical Context

- **Nadaraya (1964)** and **Watson (1964)**: Original NW estimator
- **Hall et al. (1999)**: Reweighted NW extension
- **Cai (2002)**: Theory for quantile regression with RNW
- **Salha (2006)**: Consistency under strong mixing

## See Also

- [[concepts/kowcpi|KOWCPI]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/kernel-methods|Kernel Methods]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/local-regression|local-regression]]
<!-- AUTHORED REGION END -->
