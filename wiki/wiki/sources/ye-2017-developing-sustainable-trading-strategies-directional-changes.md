---
authors:
- Ailun Ye
- V L Raju Chinthalapati
- Antoaneta Serguieva
- Edward Tsang
content_hash: sha256:f48554ebfe79fd3c01131142a08e75fad5c4c511d011b42fcfd28b8899bbfca2
created: 2026-09-27 01:47:00+00:00
page_id: sources/ye-2017-developing-sustainable-trading-strategies-directional-changes
page_type: source
related:
- concepts/intrinsic-time
- concepts/high-frequency-trading
- concepts/stylized-facts
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:a60b9df8f06bfdfb563d2165eb1f7ffa82aceafa14e56ae01222ee22803f7c18
source_path: markdown_output/ye-2017-developing-sustainable-trading-strategies-directional-changes.md
source_type: paper
tags:
- directional-change
- fx-trading
- trading-strategy
- trailing-stop
- technical-analysis
- backtesting
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Developing Sustainable Trading Strategies Using Directional Changes with High
  Frequency Data
updated: '2026-09-27T01:47:00Z'
uuid: 31004017-a2ac-554c-9bea-1c8ac973bc38
year: 2017
---

<!-- AUTHORED REGION START -->
# Developing Sustainable Trading Strategies Using Directional Changes with High Frequency Data

## Summary

The paper asks whether trading strategies built on directional change (DC), an intrinsic-time way of summarising price movement that the authors argue is more consistent across time scales than fixed-interval time series, can be made profitable and sustainable, and whether combining DC with a traditional technical-analysis indicator improves results further.

Four strategies are proposed, all entering a position at a DC confirmation point: Strategy 1 exits at a fixed take-profit/stop-loss; Strategy 2 replaces the fixed exit with a trailing stop; Strategy 3 exits using a close-threshold formula based on the event's overshoot value (OSV); and Strategy 4 restricts Strategy 3 to periods where the Directional Movement Index (DMI) shows an established uptrend. Each strategy is tested on EUR/USD and GBP/USD tick data across ten DC thresholds from 0.01% to 0.9%, with one year of in-sample back-testing used to fix parameters and a subsequent six-month out-of-sample demo period used to evaluate them, assuming no commission or slippage.

Strategy 2 (trailing stop) produced the most consistent improvement over Strategy 1, and Strategy 3 (close-threshold exit) achieved a high proportion of profitable thresholds with much lower and more stable drawdown than the other strategies in both currency pairs. Combining DC with the DMI trend filter (Strategy 4) reduced trading frequency substantially but did not improve win rate or profitability over Strategy 3, and the authors attribute this to DMI's inherently lagged trend signal.

The contribution is a set of concrete DC-based entry/exit rules, including a trailing-stop and an overshoot-based close-threshold exit, evaluated with a proper in-sample/out-of-sample split, plus an explicit test of whether adding a classic technical indicator to a DC strategy helps or hurts.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Trades are triggered by directional-change (DC) events: a trader-set threshold theta marks alternating upturn and downturn confirmation points on tick bid/ask data, and every strategy enters a position at a DC confirmation point. Ten thresholds from 0.01% to 0.9% are tested. Exit timing differs by strategy: Strategy 1 uses a fixed take-profit/stop-loss, Strategy 2 a trailing stop, and Strategies 3 and 4 a close-threshold rule computed from the overshoot value (OSV), so the holding horizon is defined by when the close condition is met rather than by a fixed amount of time.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** EUR/USD and GBP/USD
- **Venue:** not stated
- **Period:** 01/01/2015 to 31/12/2015 used for in-sample back-testing; 01/01/2016 to 30/06/2016 used for out-of-sample demo testing
- **Granularity:** Tick-level bid/ask price data

## Features and Measures

- **DC confirmation point / threshold theta.** The point at which price has moved by a trader-set percentage threshold from the previous extreme, confirming a directional change and triggering entry in all four strategies.
- **Overshoot value (OSV).** A normalised measure of how far price has moved beyond the DC confirmation point relative to the threshold, used to compute a dynamic close threshold for exiting Strategies 3 and 4.
- **DMI trend filter.** A technical-analysis filter built from the Directional Movement Index (ADX, +DI, -DI) that only allows Strategy 4 to trade when ADX is above 25 and +DI is above -DI, indicating an established uptrend.

## Method

Strategies are back-tested on the first year of data (01/01/2015 to 31/12/2015) to fix parameter values, then re-run unchanged on the following six months (01/01/2016 to 30/06/2016) as an out-of-sample demo test. No commission or slippage is assumed; orders are filled instantly at the quoted ask (long) or bid (short) price. Each simulated account starts with a balance of 100,000 dollars and trades a fixed size of 100,000 contracts (1 lot) per order. Ten DC thresholds from 0.01% to 0.9% are tested for each strategy and currency pair. Performance is judged using total profit, maximum balance and equity drawdown, profit factor (gross profit over gross loss), total number of trades, and winning rate.

## Results

- Strategy 1 produced positive total profit in 7 of 10 thresholds for EUR/USD but only 3 of 10 for GBP/USD, with EUR/USD returns as high as about 60% at some thresholds and a near-25% loss at the 0.01% threshold.
- Strategy 2 (trailing stop) improved on Strategy 1, averaging a 28.69% return across thresholds in EUR/USD versus 21.68% for Strategy 1, and turning Strategy 1's -99,951 loss at the 0.01% GBP/USD threshold into a 55,470 profit.
- Strategy 3 (close-threshold exit) produced positive returns in 80% of EUR/USD threshold tests, averaging 9.42%, with balance drawdown held under 5% in EUR/USD and under 20% in GBP/USD across all thresholds.
- Strategy 4 (DC plus DMI filter) cut total trades to roughly a quarter of Strategy 3's count and did not improve win rate or profitability over Strategy 3, though it further lowered balance drawdown.
- The highest profit factor recorded across all strategies was 1.91 (Strategy 2, EUR/USD, 0.9% threshold); the highest recorded winning rate was 89.18% (Strategy 1, GBP/USD, 0.05% threshold).

## Limitations

- No commission and no slippage are assumed in the simulation, with orders assumed to fill instantly at the quoted bid/ask, which likely overstates real-world profitability.
- Only two currency pairs (EUR/USD and GBP/USD) and an 18-month sample were tested.
- Reader note: Strategy 4's DMI filter is built from lagged, backward-looking price indicators, which the authors themselves note delays its trend signal relative to when the market has already turned.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/directional-change|Directional Change]]

## Citation

Ailun Ye, V L Raju Chinthalapati, Antoaneta Serguieva, Edward Tsang (2017). Developing Sustainable Trading Strategies Using Directional Changes with High Frequency Data.

DOI: 10.1109/bigdata.2017.8258453

Text ingested: `markdown_output/ye-2017-developing-sustainable-trading-strategies-directional-changes.md`, converted from `raw/ofi-event-clock/ye-2017-developing-sustainable-trading-strategies-directional-changes.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, the directional-change framework section, all four strategy descriptions, the experimental setup, the results and analysis section, and the conclusion.

Known problems with the input: No publication year or venue is printed on the paper itself; year is taken from the job file's year_hint (2017).
<!-- AUTHORED REGION END -->