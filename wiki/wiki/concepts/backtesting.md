---
abstraction_level: intermediate
concept_type: technique
content_hash: sha256:b3887e2191a47d3354aba844fb8dda1a718abab88f9ebc45c2cdfd1e9d9abcb8
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: concepts/backtesting
page_type: concept
related:
- concepts/algorithmic-trading
- concepts/arima-garch-models
- concepts/historical-simulation-backtesting
- concepts/information-ratio
- concepts/look-ahead-bias
- concepts/look-ahead-bias-data-mining
- concepts/overfitting-in-alpha-research
revision_id: 1
schema_version: 2
sources:
- sources/halls-moore-advanced-algorithmic-trading
- sources/adegboye-2017-regression-genetic-programming-estimating-trend-end
- sources/adegboye-2021-improving-trend-reversal-estimation-forex-markets
- sources/adegboye-2021-machine-learning-classification-regression-models-predicting
- sources/adegboye-2022-algorithmic-trading-directional-changes
- sources/alkhamees-2017-directional-change-based-trading-strategy-dynamic
- sources/alkhamees-2019-developing-event-identification-methods-structured-unstructured
- sources/aloud-2016-profitability-directional-change-based-trading-strategies
- sources/bakhach-2016-forecasting-directional-changes-fx-markets
- sources/bakhach-2018-developing-trading-strategies-under-directional-changes
- sources/batrinca-2016-analysis-key-drivers-trading-performance
- sources/bilokon-2023-transformers-versus-lstms-electronic-trading
- sources/brutti-2026-noise-robust-orthogonal-clustering-applications-equity-markets
- sources/chen-2019-studying-regime-change-directional-change
- sources/das-2026-predicting-stock-price-movements-high-frequency
- sources/fang-2019-design-high-frequency-trading-algorithm-based
- sources/fayyaz-2026-frequency-controlled-comparison-tick-minute-based
- sources/george-2025-deep-reinforcement-learning-trading-strategy-development
- sources/gypteau-2015-generating-directional-change-based-trading-strategies
- sources/jaddu-2023-combining-deep-learning-order-books-reinforcement
- sources/long-2025-depth-investigation-genetic-programming-under-physical
- sources/long-2026-multi-objective-genetic-programming-based-algorithmic
- sources/michael-2022-option-volume-imbalance-predictor-equity-market
- sources/nortier-2016-second-order-proximal-methods-applied-elastic
- sources/palsma-2019-optimising-directional-changes-trading-strategies-different
- sources/prata-2024-lob-based-deep-learning-models-stock
- sources/rubisov-2015-statistical-arbitrage-limit-order-book-imbalance
- sources/salman-2022-trading-strategies-optimization-genetic-algorithm-under
- sources/salman-2023-optimization-trading-strategies-genetic-algorithm-under
- sources/salman-2025-genetic-algorithm-optimization-multi-threshold-trading
- sources/scalia-1998-information-transmission-causality-italian-treasury-bond-market
- sources/wu-2023-intelligent-trading-strategy-based-improved-directional
- sources/yamagishi-2026-run-one-rule-five-clocks-only
- sources/yang-2021-forecasting-high-frequency-financial-time-series
- sources/ye-2017-developing-sustainable-trading-strategies-directional-changes
- sources/young-2026-openmarket-synchronized-polymarket-binance-dataset-high
- sources/zaman-2026-volatility-aware-extreme-event-detection-high
- sources/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time
- sources/zheng-2022-order-flow-technical-analysis-neural-network
tags: []
title: Backtesting
updated: '2026-09-27T01:47:00Z'
updated_by: creditmacro-batch
uuid: bbc9c9ed-87ac-53de-97f0-8ae0b892d1b6
---

<!-- AUTHORED REGION START -->
# Backtesting

## Definition

Simulating a trading strategy over historical data to estimate performance, here using the event-driven QSTrader engine with transaction costs and tearsheet metrics.

## Backtesting a Risk Forecast, Continuously

A separate problem from strategy backtesting: checking whether a *risk forecast* was honest. The classical approach fixes a sample size and applies a binomial test, which is what Basel's three-zone VaR framework does. That breaks down for [[concepts/expected-shortfall|Expected Shortfall]], which is not elicitable, and it does not permit continuous monitoring — checking every day and stopping at the first rejection inflates the error rate.

[[sources/wang-2022-e-backtesting|E-backtesting]] solves both by turning each forecast into a bet ([[concepts/testing-by-betting|testing by betting]]) and accumulating the wealth into an [[concepts/e-process|e-process]]. The result is valid at any stopping time, needs no parametric assumption or fixed sample size, and only punishes under-forecasting. [[sources/fan-2024-testing-mean-variance-eprocesses|Fan, Jiao & Wang (2024)]] do the same for a conditional mean and variance, which is the closer fit for monitoring a volatility model.

## Sources

- [[sources/halls-moore-advanced-algorithmic-trading|Advanced Algorithmic Trading]]
- [[sources/wang-2022-e-backtesting|E-backtesting (2022)]]
- [[sources/fan-2024-testing-mean-variance-eprocesses|Testing the mean and variance by e-processes (2024)]]

## Related Concepts

- [[concepts/algorithmic-trading|algorithmic-trading]]
- [[concepts/arima-garch-models|arima-garch-models]]
- [[concepts/historical-simulation-backtesting|historical-simulation-backtesting]]
- [[concepts/information-ratio|information-ratio]]
- [[concepts/look-ahead-bias|look-ahead-bias]]
- [[concepts/look-ahead-bias-data-mining|look-ahead-bias-data-mining]]
- [[concepts/overfitting-in-alpha-research|overfitting-in-alpha-research]]
<!-- AUTHORED REGION END -->