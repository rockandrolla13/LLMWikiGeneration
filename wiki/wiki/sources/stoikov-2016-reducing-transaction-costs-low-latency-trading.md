---
authors:
- Sasha Stoikov
- Rolf Waeber
content_hash: sha256:6041bf72f8e7b1b9f288d6705010d658389b5090c298f520d3bb3e7b60b1a41c
created: 2026-09-27 01:47:00+00:00
page_id: sources/stoikov-2016-reducing-transaction-costs-low-latency-trading
page_type: source
publication_venue: SSRN working paper (ssrn.com/abstract=2661618)
related:
- concepts/event-clock
- concepts/optimal-execution
- concepts/market-microstructure
- concepts/order-imbalance
- concepts/bid-ask-spread
- concepts/high-frequency-trading
- entities/sasha-stoikov
revision_id: 1
schema_version: 2
source_hash: sha256:8088ce58e51b6252063c203e07a32661ad0a1e24999bef46448a3597ad416b68
source_path: markdown_output/stoikov-2016-reducing-transaction-costs-low-latency-trading.md
source_type: paper
tags:
- order-book-imbalance
- optimal-execution
- latency
- market-microstructure
- treasury-bonds
- twap-benchmark
- optimal-stopping
- transaction-costs
- clock-event
- asset-bonds-rates
- harvest-relevant
title: Reducing transaction costs with low-latency trading algorithms
updated: '2026-09-27T01:47:00Z'
uuid: 9cb4681b-8a48-5b0c-ac8d-089d6026f8f5
year: 2015
---

<!-- AUTHORED REGION START -->
# Reducing transaction costs with low-latency trading algorithms

## Summary

The paper asks how much reducing execution latency can lower trading costs when liquidating a single lot using a short-term order-book signal. It formulates the problem as an optimal-stopping problem over a short horizon T, using the top-of-book bid/ask size imbalance as the state variable, with a fixed round-trip latency L built directly into the payoff: an order decided upon at time tau is only executed at the market price prevailing at time tau+L.

The imbalance process is assumed Markov and the bid-price process is assumed periodic (price increments independent of the price level), which lets the authors discretize the imbalance into deciles and reduce the state space to a finite Markov chain. The optimal liquidation policy is then obtained from a Bellman recursion and divides the (time, imbalance) state space into a trade region and a no-trade region, similar to the exercise boundary of an American option; a time step of 100 milliseconds is used to estimate the imbalance transition matrix.

The policy is backtested out-of-sample on Level-I quotes and trades for on-the-run 5-year U.S. Treasury bonds traded on the eSpeed platform, using a time-weighted-average-price (TWAP) algorithm as the benchmark. The imbalance-based algorithm consistently beats TWAP, and the savings grow with the trading horizon T and shrink as the assumed latency L increases, consistent with a formal result that the value function is non-increasing in latency.

The main contribution is a tractable dynamic-programming framework that directly prices, in fraction-of-spread and dollar terms, the cost of latency for a signal-based execution strategy; the authors state this is, to their knowledge, the first paper to backtest an optimal liquidation strategy using Level-I market data.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The state variable is the top-of-book size imbalance I_t = B_t/(A_t+B_t), driven by order book updates and discretized into 10 deciles; the empirical Markov transition matrix for the imbalance is estimated using a fixed time step of 100 milliseconds. The prediction/decision horizon is a short liquidation window T (values from 10 seconds to 5 minutes are tested), with a fixed round-trip latency L (values from 1 to 5000 milliseconds are tested) inserted between the moment a trade decision is made and the moment it is executed at the market.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** On-the-run 5-year U.S. Treasury bonds; the bid-ask spread is almost always exactly one tick, with tick size 1/128th of a dollar.
- **Venue:** eSpeed electronic trading platform
- **Period:** First 10 trading days of July 2010
- **Granularity:** Level-I quotes and trades recorded from 10:30am to 3pm each trading day, at millisecond timestamp precision

## Features and Measures

- **Top-of-book size imbalance (I_t).** The ratio of best-bid size to the sum of best-bid and best-ask sizes, used as a short-horizon Markov signal for the direction of the next price move.
- **Latency-adjusted payoff function (g^L).** The expected payoff, expressed as a fraction of the bid-ask spread, from delaying a trade by a given latency L given the current imbalance level, used to evaluate the immediate-exercise option in the optimal-stopping problem.
- **Trade / no-trade region.** A partition of the (time, imbalance) state space, obtained from the Bellman recursion, indicating whether the optimal policy is to execute immediately or wait for a more favorable imbalance level.

## Method

The authors set up an optimal-stopping problem over [0,T] in which the payoff from liquidating one lot depends on the current bid price and imbalance decile, which are assumed jointly Markov, with the bid-price process assumed periodic so that transition probabilities do not depend on the price level itself. They discretize the imbalance into M=10 deciles and solve the resulting Bellman equation using the empirical decile transition matrix together with an estimated payoff function for each candidate latency L and time step, yielding a trade region and a no-trade region over (time, imbalance) pairs. Performance is judged by out-of-sample backtesting: each trading day is split into intervals of length T, a simulated market sell order is submitted at the first time the imbalance enters the estimated trade region, executed at the prevailing bid price L milliseconds later, and the realized average execution price of this imbalance-based algorithm is compared against a TWAP benchmark that trades at the same fixed frequency without using the imbalance signal.

## Results

- Empirically, most sell (buy) trades arrive when the top-of-book imbalance is low (high), and almost no volume trades when the imbalance is close to 0.5.
- Trading once per minute with about 1 millisecond of latency, the imbalance-based algorithm saved close to a third of the bid-ask spread compared with a TWAP benchmark on the Treasury bond dataset tested.
- Across the tested combinations of trading horizon (10 seconds, 1 minute, 5 minutes) and latency (1, 100, 1000, 5000 milliseconds), estimated savings ranged from 0.20 to 0.35 of the tick-size spread, rising with the trading horizon T and falling as latency L increases.
- At a one-minute trading frequency, the estimated savings rise from 0.17 of the tick size at 1000 ms latency to 0.32 at 1 ms latency; using 270 minutes per trading day and a $78 tick notional for 5-year Treasuries, this corresponds to roughly $3,580.20 versus $6,739.20 saved per day.
- A formal proposition shows the value function is non-increasing in latency L, confirming that a strategy with shorter latency can never perform worse than an otherwise identical strategy with longer latency.
- The authors state this is, to their knowledge, the first paper to backtest an optimal-liquidation strategy using Level-I quotes data.

## Limitations

- The model assumes the bid-ask spread never exceeds one tick and filters out periods when it does, so results may not generalize directly to assets with wider typical spreads.
- The backtest uses only 10 trading days of July 2010 data for a single instrument (on-the-run 5-year Treasuries) on a single venue (eSpeed).
- The strategy is restricted to pure market orders for tractable backtesting; the authors note that adding limit orders could improve performance but would complicate backtesting.
- Latency L is treated as a fixed, known constant, whereas the authors note real-world latency can vary and may be related to market volatility.
- Reader note: to control for price impact, all strategies are constrained to trade exactly one lot per fixed interval, which may understate cost differences at larger trade sizes.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[entities/sasha-stoikov|Sasha Stoikov]]

## Citation

Sasha Stoikov, Rolf Waeber (2015). Reducing transaction costs with low-latency trading algorithms. SSRN working paper (ssrn.com/abstract=2661618).

DOI: 10.1080/14697688.2016.1151926

Text ingested: `markdown_output/stoikov-2016-reducing-transaction-costs-low-latency-trading.md`, converted from `raw/ofi-event-clock/stoikov-2016-reducing-transaction-costs-low-latency-trading.pdf`.

Coverage of this summary: Read the whole paper (abstract, introduction, optimal stopping formulation, discrete Markov-chain model, U.S. Treasury empirical case study including backtest and latency results, conclusions, and reference list).
<!-- AUTHORED REGION END -->