---
title: Tukey g-and-h Transformation
page_id: concepts/tukey-gh-transformation
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- statistics
- distributions
- heavy-tails
- skewness
- risk-modelling
sources:
- sources/technical-2025-bond-similarity
- sources/peters-2026-quantile-diffusions
related:
- concepts/factor-models
- concepts/liquidity-risk
- analyses/conformal-tukey-gh-intervals
- concepts/quantile-regression
- entities/gareth-peters
mind_map_priority: low
schema_version: 2
uuid: 02e5abfb-cc11-5e2e-866b-3ea0f030ae72
content_hash: sha256:b37279aa106ff1dabb46809158efcce663944fd0765be106ed768635e1b781b7
---

<!-- AUTHORED REGION START -->
# Tukey g-and-h Transformation

The Tukey g-and-h transformation generates flexible distributions by transforming standard normal variables, allowing independent control of skewness and kurtosis.

## Definition

Given $Z \sim N(0,1)$, the g-and-h random variable is:

$$Y = \frac{e^{gZ} - 1}{g} \cdot e^{hZ^2/2}$$

Where:
- $g$ controls **skewness** (asymmetry)
- $h$ controls **kurtosis** (tail heaviness)

## Special Cases

| Parameters | Distribution |
|------------|--------------|
| $g = 0, h = 0$ | Normal |
| $g \neq 0, h = 0$ | Shifted log-normal |
| $g = 0, h > 0$ | Symmetric heavy-tailed |
| $g \neq 0, h > 0$ | Skewed heavy-tailed |

## Properties

**Moments** (when they exist):
- Mean, variance, skewness, kurtosis all have closed forms
- Moments exist only for $h < 1/k$ (kth moment)
- Heavy tails can have infinite higher moments

**Flexibility**:
- Can match any valid skewness-kurtosis combination
- Parsimonious (only 2 shape parameters)
- Easy simulation via transformation

## Applications in Finance

| Application | Use of g-h |
|-------------|-----------|
| VaR/CVaR | Model heavy-tailed losses |
| Credit losses | Skewed loss distributions |
| Operational risk | Extreme event modelling |
| Bond returns | Non-normal return distributions |

## Estimation

- **Method of moments**: Match sample moments
- **Quantile matching**: Fit to empirical quantiles
- **MLE**: Requires numerical optimization (no closed-form density)

## Generalization

The g-and-h is part of a family:
- **g-distribution**: $h = 0$, skewness only
- **h-distribution**: $g = 0$, kurtosis only
- **g-and-k**: Alternative parameterization

## Continuous-Time Extension

[[sources/peters-2026-quantile-diffusions|Peters, Macrina & Brannelly (2026)]] develop **Tukey g-h quantile diffusions**—continuous-time stochastic processes whose marginals follow the g-h distribution:

**Random-level construction**: For driving diffusion Y with quantile level $U_t = F_Y(t, Y_t)$:
$$Z_t = Q_{\phi_{gh}}(U_t; A, B, g, h)$$

**Function-valued construction**: Parameters evolve stochastically:
$$d\xi_t = b(t, \xi_t)dt + \Sigma(t, \xi_t)dB_t, \quad Z_t(u) = Q_{\phi_{gh}}(u; \xi_t)$$

This enables dynamic skewness and kurtosis in continuous time with applications to insurance reserve risk and VaR/TVaR computation.

## See Also

- [[analyses/conformal-tukey-gh-intervals|Conformal Prediction with Tukey g-h]]
- [[sources/peters-2026-quantile-diffusions|Quantile Processes for Dynamic Risk Modelling (2026)]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[sources/technical-2025-bond-similarity|Bond Similarity Framework (2025)]]

<!-- AUTHORED REGION END -->
