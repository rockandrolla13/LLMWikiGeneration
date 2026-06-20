---
title: Predicting Individual Corporate Bond Returns
page_id: sources/feng-2025-predicting-bond-returns
page_type: source
created: 2026-04-26 01:45:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- machine-learning
- corporate-bonds
- return-prediction
- random-forest
- bond-characteristics
authors:
- Guanhao Feng
- Xin He
- Yanchu Wang
- Chunchi Wu
year: 2025
journal: Journal of Banking and Finance
related:
- concepts/machine-learning-bonds
- concepts/bond-return-predictability
- concepts/random-forest
- entities/guanhao-feng
schema_version: 2
uuid: b020934e-f0be-5204-ab7d-ab8d9affa05f
content_hash: sha256:0568ec47d4e07c52c595600402ea9ed8588c461ce60ebc832bf0989d19c93342
---

<!-- AUTHORED REGION START -->
# Predicting Individual Corporate Bond Returns

## Summary

Applies machine learning to predict corporate bond returns using 45 years of data (1976-2020) including both public and private bonds. Achieves out-of-sample R² of 4.48% and annualized Sharpe ratio of 3.27 using Random Forest.

## Key Findings

- **Model Performance**: RF outperforms linear models (Lasso) and combination forecasts
- **Key Aggregate Predictors**: Bond market returns, TERM factor, HML factor, GDP growth
- **Key Bond Characteristics**: Downside risk, short-term reversal, return skewness, credit spreads
- **Time-Varying Predictability**: Stronger during high risk aversion, slow growth, high VIX

## Methodology

- Random Forest and other ML methods (Lasso, boosted trees)
- Long-span dataset: 1976-2020 covering multiple business cycles
- Includes both public and private bonds (significant improvement)
- Out-of-sample testing period: 1996-2020

## Key Results

| Metric | Value |
|--------|-------|
| R²_OOS | 4.48% |
| Sharpe Ratio | 3.27 (annualized) |
| Monthly Alpha | 2.09% |
| Direction-implied Alpha | 1.59% |

## Trading Strategy

- Long-short strategy: 1.95% monthly return
- Robust to transaction costs (30-140% monthly turnover)
- Alpha not captured by Fama-French 3-factor model

## Key Concepts

- [[concepts/machine-learning-bonds|ML for Bond Pricing]]
- [[concepts/bond-return-predictability|Return Predictability]]
- [[concepts/random-forest|Random Forest]]

## Implications

1. Big data (many predictors + long history) crucial for ML models
2. Private bonds add significant predictive power
3. Aggregate and cross-sectional predictors complement each other
4. Time-varying predictability tied to economic conditions

## Related Sources

- [[sources/bali-2022-bond-ml|Bali et al. (2022)]] - related ML approach
- [[sources/kelly-2023-ipca|Kelly et al. (2023)]] - IPCA factors

<!-- AUTHORED REGION END -->
