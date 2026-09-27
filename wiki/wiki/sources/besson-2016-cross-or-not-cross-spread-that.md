---
authors:
- Paul Besson
- Stéphanie Pelin
- Matthieu Lasnier
content_hash: sha256:55b7af91fa90ff243d3aa5e912e643afa803597679a3c88b66f1c7eccac8b8aa
created: 2026-09-27 01:47:00+00:00
page_id: sources/besson-2016-cross-or-not-cross-spread-that
page_type: source
publication_venue: The Journal of Trading (Fall 2016)
related:
- concepts/trade-clock
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/limit-order-book
- concepts/optimal-execution
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:bf5deb25962775b922ca38cc9ad442ee8f6f4d07f15183b9df95837315e3de9d
source_path: markdown_output/besson-2016-cross-or-not-cross-spread-that.md
source_type: paper
tags:
- order-book-imbalance
- limit-order-book
- execution-algorithms
- passive-vs-aggressive
- equities
- market-microstructure
- trading-costs
- clock-trade
- asset-equity
- harvest-core
title: 'To Cross or Not to Cross the Spread: That Is the Question'
updated: '2026-09-27T01:47:00Z'
uuid: 5dcbd255-e555-5afe-968a-3e1f8720ee02
year: 2016
---

<!-- AUTHORED REGION START -->
# To Cross or Not to Cross the Spread: That Is the Question

## Summary

The paper asks whether the state of the order book just before a trade can forecast which side (bid or ask) the next aggressive trade will hit, and how large that trade will be. Using tick data on DJ STOXX 600 European equities, the authors define order book imbalance as the percentage difference between best-bid and best-ask size and relate it to the side and size of the next trade.

They show that order book imbalance is close to linearly related to the probability of the next trade's side, that the effect survives from large caps to small caps, and that it remains useful even when the next trade is delayed by more than half a second. They then translate the expected number of trades until a passive order is filled into an expected waiting time and, combined with stock volatility, into a market-risk estimate for posting passively rather than crossing the spread.

The main finding is a simple passive posting Sharpe ratio, the ratio of the bid-ask spread (price improvement) to the estimated risk of waiting, that tells a trader or algorithm when to post passively versus cross the spread. In a simulated percentage-of-volume execution algorithm, using this order-book-imbalance rule to decide when to send aggressive catch-up orders raised the passive fill rate and turned a positive slippage into a negative one relative to VWAP.

What is new is turning a well-known empirical regularity, that order book imbalance predicts trade side, into an explicit, tradable risk-reward rule for the cross-or-wait decision, rather than just documenting the predictive relationship.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are the state of the order book (best bid/ask price and size) sampled once per next aggressive trade; to avoid double counting, all trades on the same side within 100 microseconds of each other are aggregated into a single trade so each observation corresponds to a distinct prior order-book state. There is no fixed forecast horizon in calendar time; the object predicted is the side/size of whichever aggressive trade occurs next, and the paper separately reports how prediction accuracy varies with the wall-clock delay (dt) until that next trade.

## Data

- **Asset class:** Equities
- **Instruments:** DJ STOXX 600 constituents (large, mid, and small caps); named single-stock examples are Unilever (ULVR LN), ThyssenKrupp (TKA GY), and Euronext; the percentage-of-volume simulation uses Stoxx Europe 50 constituents.
- **Venue:** Primary exchange markets (the authors state the results also hold on multilateral trading facilities).
- **Period:** February 2016 for the main imbalance/trade analysis; June 2016 for the dt-based exhibit; April 2016 for the TKA GY volatility example; one month for the percentage-of-volume simulation.
- **Granularity:** Tick-by-tick trade and first-limit order book data (best bid/ask price and size).

## Features and Measures

- **Order book imbalance.** The percentage difference between the quantity on the best bid and the quantity on the best ask, ranging from -100% to +100%; used to predict the side and size of the next aggressive trade.
- **Passive posting Sharpe ratio.** The ratio of price improvement (the bid-ask spread captured by a filled passive order) to the estimated market risk of waiting for that fill, used as a rule for deciding whether to post passively or cross the spread.
- **Average waiting time (AVGWT).** An estimate of the time until a passive order is executed, computed as the expected number of trades before execution divided by the average daily number of trades, scaled to seconds.
- **Passive fill rate.** The percentage of an execution algorithm's target quantity that was filled through passive (non-aggressive) orders rather than by crossing the spread.

## Method

The analysis is empirical and descriptive rather than a fitted statistical model: the authors bin historical order book states by order book imbalance (and separately by relative bid/ask size) and compute empirical trade-side and fill-size probabilities within each bin. Two assumptions (best case: order posted at the top of the queue; worst case: order posted at the bottom, requiring full-limit consumption) bound the expected number of trades until a passive fill, which is converted to a risk estimate using each stock's volatility per second. Performance of the resulting trading rule is judged by simulating percentage-of-volume execution algorithms (fully aggressive, standard passive, and imbalance-aware advanced passive) on a one-month, tick-by-tick sample and comparing slippage against VWAP and the achieved participation rate versus a target participation rate.

## Results

- When the order book imbalance is strongly negative, the probability that the next trade is at the bid reaches 86%; when strongly positive, the probability of the next trade being at the ask reaches 87%.
- Once the order book imbalance exceeds 60% in absolute terms (which happens in 40% of cases), trade-side predictability exceeds 76%.
- When the smaller first limit is hit, on average 78% of its size is consumed by the next trade, versus only 53% when the larger limit is hit.
- Aggregating same-side trades within 100 microseconds merges 68% of trades (70% of volume) on DJ STOXX LARGE 200 names into single next-trade observations.
- In a one-month simulation of percentage-of-volume algorithms on Stoxx Europe 50 (1,000 client orders, 1,000,248 individual trades), the fully aggressive strategy had 60% spread slippage and a 0% passive fill rate.
- The standard passive strategy achieved 33% spread slippage at a 50% passive fill rate; the imbalance-aware advanced passive strategy achieved -6% spread slippage at an 81% passive fill rate.
- The advanced strategy's participation rate stayed close to its 20% target on average (19.2%) with a 16.6% worst-case (10% quantile) outcome, versus 19.9% average and 19.5% worst-case for the fully aggressive strategy.

## Limitations

- The estimates are conditioned on the last observed order book state before a trade, which the authors note is a specific, non-random sample of all order book states and so is not theoretically fully transposable to arbitrary order book states.
- The article does not discuss the practical latency between observing the order book and acting on it, which affects how usable the signal is in practice.
- Reader note: the empirical relationships are shown as bivariate charts (imbalance versus probability, imbalance versus waiting time) rather than a single estimated model with reported confidence intervals or out-of-sample validation.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Paul Besson, Stéphanie Pelin, Matthieu Lasnier (2016). To Cross or Not to Cross the Spread: That Is the Question. The Journal of Trading (Fall 2016).

DOI: 10.3905/jot.2016.11.4.077

Text ingested: `markdown_output/besson-2016-cross-or-not-cross-spread-that.md`, converted from `raw/ofi-event-clock/besson-2016-cross-or-not-cross-spread-that.pdf`.

Coverage of this summary: Read the full article, front to back, including the appendix on trade-matching methodology and the endnote.
<!-- AUTHORED REGION END -->