---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/factor-models
page_type: concept
related:
- concepts/bayesian-model-averaging
- concepts/bond-capm
- concepts/composite-cyclical-indicators
- concepts/credit-risk-premium
- concepts/credit-spread-curve
- concepts/expectations-hypothesis-term-structure
- concepts/factor-investing
- concepts/illiquidity-premium
- concepts/information-ratio
- concepts/liquidity-risk
- concepts/machine-learning-credit-modeling
- concepts/market-timing
- concepts/one-factor-term-structure-model
- concepts/panel-data-fixed-random-effects
- concepts/principal-components-analysis
- concepts/risk-premia
- concepts/risk-vs-mispricing
- concepts/style-premia
- concepts/trend-following
revision_id: 4
sources:
- sources/andreou-2020-mixed-frequency-macro-finance
- sources/bodilsen-2025-hf-dynamic-factor-portfolio
- sources/cotturo-2026-multifactor-timing-deep-learning
- sources/dickerson-2023-bond-risk
- sources/ms-2015-03-06-bond-market-indicators
- sources/ms-2017-06-15-bmi2-xbmi-models
- sources/ms-2018-03-16-credit-bmi
- sources/ms-2018-04-16-credit-bmi-update
- sources/ms-2018-06-05-emfx-risk-premia-two-factor
- sources/ms-2019-04-14-low-beta-defensiveness-scorecard
tags:
- asset-pricing
- risk-management
- portfolio-theory
- quantitative-finance
title: Factor Models
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 46bbce7e-7716-5800-ba8f-4317dd2a38c6
content_hash: sha256:886896ad51178288af97d84e9c1b542f6d9c7012e0f8590af7f60b58c9515685
---

<!-- AUTHORED REGION START -->
# Factor Models

Factor models decompose asset returns into systematic components (factors) and idiosyncratic noise, providing a framework for risk attribution and expected return estimation.

## General Form

$$R_i = \alpha_i + \sum_{k=1}^K \beta_{i,k} F_k + \epsilon_i$$

Where:
- $R_i$ = Asset return
- $\alpha_i$ = Unexplained return (alpha)
- $F_k$ = Factor returns
- $\beta_{i,k}$ = Factor loadings (sensitivities)
- $\epsilon_i$ = Idiosyncratic return

## Types of Factor Models

### Statistical Factors
- Extracted via PCA or similar methods
- No economic interpretation required
- Examples: Principal components of yield curve

### Fundamental Factors
- Based on observable characteristics
- Examples: Value, momentum, size, quality

### Macroeconomic Factors
- Economic variables as factors
- Examples: GDP growth, inflation, yield curve changes

## Applications in Fixed Income

| Application | Factors Used |
|-------------|--------------|
| Duration hedging | Key rate durations |
| Credit risk | Rating transitions, sector exposure |
| Relative value | Spread factors, curve factors |
| Risk budgeting | Factor contribution to tracking error |

## Challenges for Bonds

Corporate bond factor models face difficulties:
- Illiquidity creates stale pricing
- Default risk is jump risk, not continuous
- Issue-specific effects dominate
- Limited time series for individual bonds

## See Also

- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/liquidity-risk|Liquidity Risk]]
- [[sources/dickerson-2023-bond-risk|Corporate Bond Risk Factor Pricing (2023)]]

## Additional Sources

- [[sources/andreou-2020-mixed-frequency-macro-finance|Mixed-Frequency Macro-Finance Factor Models (2020)]] — group factor models for macro-finance with mixed-frequency data, comparing aggregation-first vs PCA-first procedures
- [[sources/bodilsen-2025-hf-dynamic-factor-portfolio|HF Dynamic Factor Portfolio (2025)]] — high-frequency-based dynamic factor model with observable ETF factors and hierarchical-clustering-derived block idiosyncratic covariance
- [[sources/cotturo-2026-multifactor-timing-deep-learning|Multifactor Timing with Deep Learning (2026)]] — multitask deep-learning architecture for forecasting multiple style-factor returns jointly

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/bayesian-model-averaging|bayesian-model-averaging]]
- [[concepts/composite-cyclical-indicators|composite-cyclical-indicators]]
- [[concepts/credit-risk-premium|credit-risk-premium]]
- [[concepts/expectations-hypothesis-term-structure|expectations-hypothesis-term-structure]]
- [[concepts/factor-investing|factor-investing]]
- [[concepts/illiquidity-premium|illiquidity-premium]]
- [[concepts/information-ratio|information-ratio]]
- [[concepts/one-factor-term-structure-model|one-factor-term-structure-model]]
- [[concepts/panel-data-fixed-random-effects|panel-data-fixed-random-effects]]
- [[concepts/principal-components-analysis|principal-components-analysis]]
- [[concepts/risk-premia|risk-premia]]
- [[concepts/risk-vs-mispricing|risk-vs-mispricing]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2015-03-06-bond-market-indicators]], [[sources/ms-2017-06-15-bmi2-xbmi-models]], [[sources/ms-2018-03-16-credit-bmi]], [[sources/ms-2018-04-16-credit-bmi-update]], [[sources/ms-2018-06-05-emfx-risk-premia-two-factor]], [[sources/ms-2019-04-14-low-beta-defensiveness-scorecard]]
<!-- AUTHORED REGION END -->
