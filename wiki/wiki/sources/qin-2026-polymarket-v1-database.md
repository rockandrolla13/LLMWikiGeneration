---
authors:
- Boka Qin
- Rui Yang
content_hash: sha256:a95fe2f85aa35ec47ba2de9a81c8fc9092290b11015804dd3098aca6e3a64b5f
created: 2026-09-27 01:47:00+00:00
page_id: sources/qin-2026-polymarket-v1-database
page_type: source
related:
- concepts/trade-clock
- concepts/trade-classification
- concepts/order-flow-imbalance
- concepts/informed-trading
- concepts/market-microstructure
- concepts/price-impact
- concepts/bid-ask-spread
- concepts/high-frequency-data
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:4f3101543bd24b41d121538184d23ce2cb2b498232ee8735afbf218f0392faeb
source_path: markdown_output/qin-2026-polymarket-v1-database.md
source_type: paper
tags:
- prediction-markets
- polymarket
- trade-classification
- vpin
- order-flow
- blockchain-data
- forecast-calibration
- clock-trade
- asset-options
- harvest-relevant
title: Polymarket-v1 Database
updated: '2026-09-27T01:47:00Z'
uuid: 7ebb342f-7f1a-59b3-8ecb-22d61ad0c360
year: 2026
---

<!-- AUTHORED REGION START -->
# Polymarket-v1 Database

## Summary

The paper asks whether standard trade-direction classifiers such as the tick rule and bulk volume classification are reliable in prediction markets, and whether the resulting measurement error in liquidity and informed-trading metrics distorts conclusions about market quality and forecasting performance -- questions existing prediction-market archives could not answer directly because they infer trade direction rather than observe it.

The authors build and release the Polymarket-v1 Database, a complete on-chain trade tape of Polymarket's first-generation CTF Exchange on Polygon spanning 2022-11-21 to 2026-04-28, in which every trade carries a ground-truth buyer/seller direction read from blockchain settlement rather than inferred from prices. They benchmark the tick rule and bulk volume classification against this ground truth, propagate the resulting classification error into VPIN and order-flow-imbalance estimates and a Hasbrouck-style structural VAR/VECM price-impact decomposition, exploit a staggered difference-in-differences design around a 2026 fee reform, and regress per-market Brier scores on both ground-truth and classification-based microstructure metrics.

Standard classifiers achieve close to random aggregate accuracy, which conceals a systematic price-level gradient -- over-predicting buys at low prices and under-predicting them at high prices -- driven by positive trade-direction autocorrelation and concentrated market-making. This error propagates into inferred VPIN and order-flow imbalance and attenuates the estimated relationship between microstructure quality and forecast accuracy: ground-truth True VPIN positively predicts Brier score (worse calibration under toxic flow) while ground-truth Gibbs spread negatively predicts it, a pattern the authors attribute to informed specialists concentrating in wide-spread, niche markets.

What is new is the ground-truth, on-chain trade-direction field itself, unavailable in prior Polymarket datasets that rely on heuristic classification, together with a full-lifecycle trade tape that lets the authors show classification error is not just statistically detectable but economically consequential for transaction-cost analysis and probability-forecast calibration research.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Every observation is one on-chain OrderFilled execution (a maker-taker match), not a fixed time bucket; the trade tape is then aggregated into market-month panels for cross-sectional and difference-in-differences regressions and into 0.01-wide price bins for the classifier-accuracy tables. The 'prediction' target studied is not a return over a fixed horizon but a market's eventual binary resolution outcome, used to compute per-market Brier scores and to test whether large or run-persistent classified trades anticipate that outcome.

## Data

- **Asset class:** Options
- **Instruments:** Binary YES/NO outcome tokens across roughly 1.3 million Polymarket condition-level markets, organized in a four-level Series -> Event -> Market -> Token hierarchy; trades settle in USDC on Polygon.
- **Venue:** Polymarket's first-generation CTF Exchange (on-chain settlement layer on the Polygon blockchain).
- **Period:** 2022-11-21 to 2026-04-28 (41 months, the complete v1 contract lifecycle).
- **Granularity:** Individual on-chain trade records (1.2016 billion total) across 42 monthly parquet partitions.

## Features and Measures

- **Ground-truth trade direction (D).** A per-trade buy/sell label read directly from the blockchain settlement layer and normalized so that D=+1 always corresponds to an increase in the event's implied probability, resolving the fact that buying a NO token is equivalent to selling the YES token.
- **Tick rule and bulk volume classification (BVC).** Standard heuristics that infer trade direction from price changes (or the probability of a price change) between consecutive trades, benchmarked here against the ground-truth direction field.
- **True VPIN vs BVC-VPIN.** Volume-synchronized probability of informed trading computed once from ground-truth trade direction and once from classifier-inferred direction, to isolate how classification error distorts a standard order-flow-toxicity measure.
- **Order Flow Imbalance (OFI).** A signed measure of net buy versus sell pressure over a window, computed from ground-truth direction and compared against a version built from classified direction to quantify directional bias.
- **Gibbs effective spread and Roll spread.** Two effective bid-ask spread estimators: a Bayesian (Gibbs-sampling) estimator that uses ground-truth trade direction, and the classical Roll estimator inferred purely from price-change autocovariance.
- **Hasbrouck permanent/transitory price impact and VECM information shares.** A structural VAR decomposition of how much of a trade's price impact is permanent (informational) versus transitory (liquidity-related), plus a VECM-based split of price discovery between a binary market's YES and NO legs.

## Method

The authors validate the tick rule and bulk volume classification against ground-truth direction across roughly 202 million Standard Binary trades (neg_risk=false markets with both legs trading and at least 30 trades), tabulating accuracy by 0.01-wide price bins and separately estimating trade-direction autocorrelation by price bin to explain the failure mechanism.

They compute exact, classification-free OFI and VPIN from ground-truth direction, and estimate a Hasbrouck-style structural VAR (identified via a Cholesky restriction that blocks contemporaneous feedback from price changes into the trade decision) and a VECM price-discovery decomposition across thousands of Standard Binary markets, plus a staggered difference-in-differences design with market and month fixed effects exploiting a 2026 fee reform activated on different dates across market categories.

Forecasting performance is judged with per-market Brier scores regressed cross-sectionally on ground-truth microstructure quality (Gibbs spread, True VPIN) versus classification-based proxies (Roll spread, BVC VPIN), controlling for mean price level, trade activity and category fixed effects, across a balanced panel of 1,019 resolved Standard Binary markets.

## Results

- The tick rule and bulk volume classification achieved near-random overall accuracy of 49.83% and 50.51% across 202 million Standard Binary trades.
- Classifier accuracy formed a systematic price-level gradient, exceeding 50% for trades priced in the low range and falling below 50% for trades priced in the high range, driven by positive trade-direction autocorrelation and concentrated market-making.
- Classification error propagated into downstream metrics: the median OFI bias reached a magnitude of 1.3636 for bulk volume classification versus 0.1815 for the tick rule, relative to true OFI.
- In a staggered difference-in-differences around the 2026 fee reform, True VPIN rose by 0.015941 in the main sample and wash-trading share fell by 0.00036, consistent with noise-trader flight and reduced manipulative trading.
- True VPIN positively predicted per-market Brier score (coefficient 0.1979 in the ground-truth model) while Gibbs spread negatively predicted it (coefficient of magnitude 4.1280), and both relationships attenuated when classification-based proxies (BVC VPIN, Roll spread) were substituted.
- The top 1% of maker addresses controlled 84.1% of maker-side volume (Gini 0.9698), indicating a highly concentrated market-making ecosystem.
- Large first-mover trades (at or above $100, above the within-market 90th percentile) achieved a 52.3% hit rate at anticipating the eventual resolution outcome versus a 50.2% baseline.

## Limitations

- Only on-chain settlement data is used; no off-chain order-book snapshots are included, so pre-execution quote dynamics are not observed.
- The archive is restricted to Polymarket's v1 contract; the authors state external validity to the v2 architecture is uncertain.
- The authors acknowledge that difference-in-differences estimates for True VPIN and Amihud illiquidity are limited by pre-activation trend violations, so those two metrics should be read as descriptive rather than strictly causal.
- The wash-trading proxy, based on detecting closed maker-taker cycles in the transaction graph, has not been independently validated against confirmed wash-trading cases.
- Reader note: several very large reported t-statistics in the difference-in-differences tables (over 100) are flagged by the authors themselves as implausible, likely reflecting under-estimated clustered standard errors rather than genuinely high precision.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/price-impact|price impact]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/vpin|VPIN]]

## Citation

Boka Qin, Rui Yang (2026). Polymarket-v1 Database.

DOI: 10.2139/ssrn.6870538

Text ingested: `markdown_output/qin-2026-polymarket-v1-database.md`, converted from `raw/ofi-event-clock/qin-2026-polymarket-v1-database.pdf`.

Coverage of this summary: Read the entire paper start to end: abstract, introduction, institutional background, the dataset description (Section 3), cross-sectional stylized facts (Section 4), the longitudinal market-quality and fee-reform difference-in-differences analysis (Section 5), the informed-trading and classification-bias measurement (Section 6), volume decomposition and wash-trading (Section 7), the microstructure-and-calibration regressions (Section 8), discussion/limitations (Section 9), conclusion, category-mapping table and reference list.

Known problems with the input: Several formula definitions (the direction-normalization equation, the OFI formula, the Gibbs-sampling regression, and the SVAR specification) are rendered as omitted images in the converted markdown, so their exact functional form could not be verified beyond what the surrounding text states.
<!-- AUTHORED REGION END -->