---
authors:
- Daojing Zhai
content_hash: sha256:bd90a90ac3ddcbcb22169a3828b4bbb6b42686fc720d1c44a248781a87fce73e
created: 2026-09-27 01:47:00+00:00
page_id: sources/zhai-2026-public-trader-identity-adverse-selection-return
page_type: source
related:
- concepts/sampling-clocks
- concepts/adverse-selection
- concepts/informed-trading
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/order-flow-imbalance
- concepts/order-flow-prediction
- concepts/price-impact
- concepts/high-frequency-trading
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:ad5d0e20e68fae51e22e8f383ffe11a18bfb52328b740aaef9388a463c25de63
source_path: markdown_output/zhai-2026-public-trader-identity-adverse-selection-return.md
source_type: paper
tags:
- decentralized-exchange
- crypto-perpetuals
- wallet-identity
- adverse-selection
- return-prediction
- order-book-reconstruction
- hyperliquid
- high-frequency-trading
- clock-compares
- asset-crypto
- harvest-core
title: 'Public Trader Identity: Adverse Selection and Return Predictability'
updated: '2026-09-27T01:47:00Z'
uuid: 0dc5c5ff-7671-50f1-b57a-1681ecc54648
year: 2026
---

<!-- AUTHORED REGION START -->
# Public Trader Identity: Adverse Selection and Return Predictability

## Summary

The paper asks whether trader anonymity, which classical adverse-selection theory treats as the condition that lets informed traders profit, still holds on a decentralized exchange where every order, cancellation and fill carries a permanent, public wallet address. It studies Hyperliquid, the largest decentralized perpetual-futures exchange, reconstructing the full order book from a non-validating node's record of 17.1 billion messages and 14.3 million aggressive orders from 147,113 wallets over July 2026, covering $84.3 billion in taker notional.

The approach scores each wallet by the notional-weighted ten-second markout of its aggressive trades over a frozen ten-day window, then tests whether that ranking persists into a later ten-day window and whether adding the previously scored wallets' activity to a standard anonymous forecasting benchmark (built from prices, quotes and order flow) improves short-horizon return forecasts on a 100-millisecond grid, using both ridge regression and gradient-boosted trees.

The ranking is persistent: the Spearman rank correlation of wallet markouts is 0.52 across adjacent ten-day windows, concentrated in a narrow top tail. Adding the top-decile wallets' identity features raises one-second out-of-sample R-squared from 10.88% to 12.31% under ridge (a 13.2% gain), a result that survives 200 activity-matched placebo cohorts, rolling and peer-adjusted scores, feature-timing embargoes, a nonlinear tree model, and an independent December 2025 replication sample. Evaluated only at moments when a trade actually occurs, the gain is larger still (2.47 versus 1.43 percentage points of R-squared).

What is new is the direct measurement of an out-of-sample forecasting increment from public wallet identity itself, something anonymous order-book data cannot supply; the paper also partially separates this from a simple readout of imminent order flow by showing the gain survives after revealing the arriving order's realized direction and after restricting to fills followed by no further trading from another parent order.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Underlying prices and markouts are indexed by Hyperliquid's irregular consensus-block clock, where blocks commit on average every 67.6 milliseconds; the main forecasting exercise instead samples states on a regular 100-millisecond calendar grid over horizons from 200 milliseconds to 30 seconds, with every feature using only information committed strictly before the sample time. A separate test compares this full-grid evaluation with evaluation restricted to the subset of grid points that coincide with an actual maker fill (a trade-clock subsample), finding a larger identity-driven R-squared gain at those trade arrivals (2.47 percentage points) than across the full grid (1.43 percentage points), with the increment partly, but not fully, explained by the arriving order's realized direction.

## Data

- **Asset class:** Crypto
- **Instruments:** Perpetual futures contracts on Hyperliquid across its ten most active markets by message count (BTC, ETH, SOL, HYPE, ZEC, LIT, WLD, XRP, NEAR, PUMP); the main persistence and forecasting analyses use BTC, ETH and SOL.
- **Venue:** Hyperliquid decentralized exchange
- **Period:** July 1-27, 2026 (primary sample); December 1-31, 2025 (independent public replication sample)
- **Granularity:** Level-4, order-by-order book reconstruction from consensus-ordered blocks; forecasting is evaluated on a 100-millisecond grid at horizons from 200 milliseconds to 30 seconds

## Features and Measures

- **Wallet toxicity score.** Notional-weighted mean ten-second markout of a wallet's aggressive orders over a frozen ten-day window, used to rank wallets from least to most costly to trade against.
- **Peer-adjusted wallet score.** A wallet's markout net of the notional-weighted mean markout of other wallets trading the same coin in the same minute, used to strip out market-wide price moves common to everyone trading at that time.
- **Identity quote and flow block.** Eleven predictors that mirror the anonymous benchmark's depth-imbalance and order-flow-imbalance measures but restrict them to the top-decile toxic wallets, plus the toxic decile's net buyer count, share of best-quote depth, and contribution to quote imbalance.
- **Anonymous benchmark block.** A ten-variable set built only from prices, quotes and aggregate order flow (near-touch and best-quote imbalance, one- and thirty-second order-flow imbalance, signed prints and taker notional, past return, realized volatility and spread), used as the no-identity forecasting comparison.

## Method

Wallets are scored on ten days of data (July 1-10) and the ranking is frozen before any later evaluation. Persistence is tested with the Spearman rank correlation between scoring-window and validation-window (July 11-20) markouts, and with a ventile sort that controls for market, time, order size, volatility and spread. Return prediction is framed as forecasting the forward midpoint return at horizons from 200 milliseconds to 30 seconds on a 100-millisecond grid, comparing a ridge regression and a gradient-boosted tree model fit on the anonymous benchmark alone against the same model with the toxic-wallet identity block added; models are fit on July 11-20 and evaluated once, out of sample, on July 21-27, with out-of-sample R-squared reported against a zero forecast and t-statistics from seven paired daily mean-squared-error differences.

To separate the identity ranking from wallet size and trading activity, the study draws 200 cohorts of non-toxic wallets matched cell by cell on scoring-window notional and order count, rebuilds the same eleven identity features for each, and compares the real toxic cohort's R-squared increment against this placebo distribution. To rule out mechanical grid misalignment, every feature in both blocks is delayed by 200 and 300 milliseconds while the target stays fixed. To probe whether the larger gain at actual trade arrivals is just a readout of the imminent order's direction, the realized side of the arriving order is revealed to both models and interacted with every predictor, and the sample is separately restricted to fills followed by no trade from a different parent order within the forecast horizon.

## Results

- Wallet toxicity ranks are persistent: the Spearman rank correlation of wallet markouts between adjacent ten-day windows is 0.52, and the peer-adjusted version of the score has a correlation of 0.62.
- Persistence is concentrated in a narrow tail: after controlling for market, time, order size, volatility and spread, validation-window markouts stay flat through the fifteenth ventile and rise to 3.11 basis points in the top ventile.
- Adding the top-decile identity block to the anonymous benchmark raises one-second out-of-sample R-squared from 10.88% to 12.31% under ridge regression, a 13.2% relative gain (t = 9.2), and from 19.48% to 20.65% under gradient-boosted trees, a 6.0% gain (t = 5.0).
- At the one-second horizon the toxic-wallet increment is 1.6 times the largest of 200 activity-matched placebo cohorts, and it exceeds every one of the 200 draws through ten seconds.
- Measured only at moments when a maker fill actually occurs, the one-second identity gain is 2.47 percentage points of R-squared, versus 1.43 percentage points measured across the whole 100-millisecond grid.
- Revealing the realized direction of the arriving order removes 39% of the pre-arrival identity increment, and the remainder still holds among fills followed by no trade from another parent order.
- The same design applied without retuning to an independent December 2025 sample reproduces both the persistence (rank correlation 0.47) and the one-second forecasting gain (+14.6% under ridge, t = 3.9).

## Limitations

- The 'identity' is a pseudonymous wallet address rather than a legal person: one entity may control several wallets and one wallet may aggregate several principals.
- Translating the forecasting increment into implementable trading profits would require a full execution and market-making model with latency, queue priority, fill probabilities, fees and inventory, which the paper does not build.
- The collection recorded infrastructure outages (a collector lag and a node failure spanning July 27-28) that truncate the primary sample and required gated, gap-filled reconstruction around damaged archive files.
- Reader note: the study covers a single decentralized exchange and a single asset class (crypto perpetual futures) over roughly one month of primary data, so persistence and forecasting results may not generalize to other venues, asset classes, or longer horizons.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/price-impact|price impact]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/vpin|VPIN]]

## Citation

Daojing Zhai (2026). Public Trader Identity: Adverse Selection and Return Predictability.

DOI: 10.48550/arxiv.2608.04373

Text ingested: `markdown_output/zhai-2026-public-trader-identity-adverse-selection-return.md`, converted from `raw/ofi-event-clock/zhai-2026-public-trader-identity-adverse-selection-return.pdf`.

Coverage of this summary: Read the full markdown text, including all main sections (introduction, institutional setting and data, wallet toxicity, high-frequency return prediction) and all appendices (data collection/reconstruction/audit, additional robustness results, December 2025 replication, and the payoff-unit conversion appendix).

Known problems with the input: Markdown contains PDF-conversion artifacts (picture placeholders in place of equations/figures, minus signs and decimals occasionally split by OCR, e.g. '_−_' and 'X _._ Y'), but the surrounding prose and tables are legible and complete.
<!-- AUTHORED REGION END -->