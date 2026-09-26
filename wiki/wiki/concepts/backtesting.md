---
abstraction_level: intermediate
concept_type: technique
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
sources:
- sources/halls-moore-advanced-algorithmic-trading
tags: []
title: Backtesting
updated: '2026-09-16T00:00:00Z'
updated_by: creditmacro-batch
schema_version: 2
uuid: bbc9c9ed-87ac-53de-97f0-8ae0b892d1b6
content_hash: sha256:b3887e2191a47d3354aba844fb8dda1a718abab88f9ebc45c2cdfd1e9d9abcb8
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
