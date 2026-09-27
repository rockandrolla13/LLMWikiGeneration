---
content_hash: sha256:9a72440cf3b72b8418ef5a62535e84e3157804f87a446fb4e2866e3a5bb6f5ca
created: 2026-09-27 01:47:00+00:00
mind_map_priority: medium
page_id: concepts/kyles-lambda
page_type: concept
related:
- concepts/price-impact
- concepts/order-flow
- concepts/order-imbalance
- concepts/amihud-illiquidity
- concepts/informed-trading
- concepts/adverse-selection
revision_id: 1
schema_version: 2
sources:
- sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts
- sources/bugaenko-2020-empirical-study-market-impact-conditional-order
- sources/rola-2025-boltzmann-price-toward-understanding-fair-price
tags:
- kyles-lambda
- price-impact
- illiquidity
- order-flow
- market-microstructure
title: Kyle's Lambda
updated: '2026-09-27T01:47:00Z'
uuid: 2e435f56-2d80-54be-b3a7-ed356ed31d0e
---

<!-- AUTHORED REGION START -->
# Kyle's Lambda

Kyle's lambda is the amount by which the price moves per unit of net signed order flow. It comes from a model of trading in which a market maker sets the price after seeing total order flow, without knowing how much of it comes from informed traders.

## How it is measured

In practice it is the slope from a regression of price changes on signed order flow over a set of intervals. A high value means a given amount of net buying moves the price a lot, so the market is illiquid.

## Why it matters here

It is the simplest summary of [[concepts/price-impact|price impact]]. It is also a direct example of how the clock affects a measure: the regression needs intervals, and the estimate can change with how those intervals are defined.

## Relation to other measures

[[concepts/amihud-illiquidity|Amihud illiquidity]] is a related measure that uses unsigned volume and needs no trade classification. Kyle's lambda needs signed flow, so it depends on [[concepts/order-imbalance|order imbalance]] being measured correctly.

## Caveats

The model behind it assumes price impact is linear in order flow. Much of the empirical literature finds impact to be concave for large orders, as described under [[concepts/square-root-law|the square-root law]]. The estimate also varies through the day and with the sampling interval.

## Sources in This Wiki

- [[sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts|Revisiting the ∪-shaped patterns in volatility and price impacts: Novel results using trade-time estimates]] (Yashar H. Barardehi, Dan Bernhardt, 2025). Using trade-time (fixed-dollar-volume) sampling instead of calendar-time intervals, the paper shows volatility and Kyle's lambda fall monotonically over the trading day rather than following the classic U-shape.
- [[sources/bugaenko-2020-empirical-study-market-impact-conditional-order|Empirical Study of Market Impact Conditional on Order-Flow Imbalance]] (Anastasia Bugaenko, 2019). Empirically tests Kyle-style linear and square-root market impact models on NASDAQ LOBSTER data, then fits linear regression and decision tree models to predict impact from order-flow imbalance.
- [[sources/rola-2025-boltzmann-price-toward-understanding-fair-price|Boltzmann Price: Toward Understanding the Fair Price in High-Frequency Markets]] (Przemysław Rola, 2025). Derives a maximum-entropy 'Boltzmann price' from bid/ask volume imbalance and shows it can explain excess kurtosis and market impact better than mid-price benchmarks.

## Related

- [[concepts/price-impact|price impact]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/amihud-illiquidity|amihud illiquidity]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/adverse-selection|adverse selection]]
<!-- AUTHORED REGION END -->