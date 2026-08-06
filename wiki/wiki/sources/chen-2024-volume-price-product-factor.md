---
title: "The Inclusion of the Volume-Price-Product Factor for the Trend Forecasting of Futures Time Series Data"
page_id: sources/chen-2024-volume-price-product-factor
page_type: source
source_type: journal-article
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
authors: [Yipiao Chen, Xiaogang Yuan]
year: 2024
venue: IEEE Access
doi: 10.1109/ACCESS.2024.3358406
tags: [quant-finance, futures, trend-following, moving-average, volume-price, technical-analysis, statistical-learning-theory, deep-learning, trading-strategy]
related: [concepts/volume-price-product-factor, concepts/moving-average-crossover-trading, concepts/vapnik-chervonenkis-dimension, concepts/return-vs-accuracy-tradeoff, concepts/structural-risk, concepts/lstm-networks, entities/yipiao-chen, entities/xiaogang-yuan, entities/wenhui-li, entities/yubo-wang, entities/warren-buffett]
mind_map_priority: high
---

# The Inclusion of the Volume-Price-Product Factor for the Trend Forecasting of Futures Time Series Data

**Authors:** [[entities/yipiao-chen|Yipiao Chen]], [[entities/xiaogang-yuan|Xiaogang Yuan]]

**Venue:** IEEE Access, 2024

## Summary

The paper proposes the Volume-Price-Product Moving Average (VPPMA), a trend-forecasting model for futures that injects a [[concepts/volume-price-product-factor|volume-price-product (VPP) factor]] S_i = V_i * C_i (trading volume times closing price) directly in place of the closing price inside the standard simple moving average. Trading signals are generated from golden-cross/death-cross comparisons among four VPPMA lines plus two SMA lines via [[concepts/moving-average-crossover-trading|moving-average crossover trading]], and the authors argue via [[concepts/vapnik-chervonenkis-dimension|VC-dimension]] / statistical-learning theory that the moving-average model behaves as a binary classifier with near-zero empirical error and strong generalization. Backtested on six Chinese commodity futures, VPPMA delivers higher annualized returns and R-squared than both an [[concepts/lstm-networks|LSTM]] deep-learning benchmark and a plain SMA, with top-ranked annualized returns exceeding 66%. A central methodological theme is the [[concepts/return-vs-accuracy-tradeoff|divergence between predictive accuracy and profitability]], grounded in [[concepts/structural-risk|structural risk minimization]].

## Key Claims

1. The volume-price-product factor S_i = V_i * C_i, substituted for the closing price inside the SMA formula, defines the [[concepts/volume-price-product-factor|VPPMA]] and makes the moving average more sensitive to genuine market trends than either price-only SMA or Li's volume-weighted PVMA.
2. Because a moving average can classify any closing price as above or below the line, the hypothesis space has infinite [[concepts/vapnik-chervonenkis-dimension|VC dimension]] and zero empirical (classification) loss; selecting a combination of moving-average periods that minimizes the overall loss function is equivalent to maximizing annualized return.
3. High prediction accuracy or low MSE does not imply profitability: the [[concepts/lstm-networks|LSTM]] model shows a low MSE but R-squared of only ~0.2 and one-step predictive lag, whereas VPPMA achieves R-squared above 0.7 on most top-ranked varieties (see [[concepts/return-vs-accuracy-tradeoff|return-vs-accuracy divergence]]).
4. Across six Chinese futures (fuel, methanol, PTA, cotton, palm oil, rebar), VPPMA consistently beats SMA on annualized return from top to bottom rankings, with the weakest top-ranked variety (rebar) still at 66.94%, far above Warren Buffett's reported ~20% annualized return.
5. Adding more moving averages does not monotonically improve performance; a combination of six VPPMAs outperformed seven, because pairwise comparisons collapse to the single pair with the minimum loss function value.

## Concepts

- [[concepts/volume-price-product-factor|Volume-Price-Product Factor (VPPMA)]] — the core signal, replacing closing price with volume-times-price inside a moving average.
- [[concepts/moving-average-crossover-trading|Moving-Average Crossover Trading]] — the golden-cross/death-cross rule set generating trade signals across six lines.
- [[concepts/vapnik-chervonenkis-dimension|Vapnik-Chervonenkis Dimension]] — invoked to argue the moving-average classifier has infinite VC dimension yet zero empirical error.
- [[concepts/return-vs-accuracy-tradeoff|Return-vs-Accuracy Divergence]] — the argument that MSE/accuracy do not translate to profitability.
- [[concepts/structural-risk|Structural Risk Minimization]] — used to justify the low-complexity moving-average line's minimal structural risk.
- [[concepts/lstm-networks|LSTM Networks]] — the deep-learning benchmark shown to lag and underperform on R-squared.

## Related Sources

(Leave empty for now — links added by future ingestions)
