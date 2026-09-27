---
authors:
- Ozgur Salman
- Themistoklis Melissourgos
- Michael Kampouridis
content_hash: sha256:fc4b123ed99a932c64b121a8661f923bdd4ba04bef7e3d64f95cb5b000f994cc
created: 2026-09-27 01:47:00+00:00
page_id: sources/salman-2023-optimization-trading-strategies-genetic-algorithm-under
page_type: source
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/directional-change
- entities/ozgur-salman
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:d741f0921446944dca00f87a25c682e459df637f199db978ed768022b0e045d7
source_path: markdown_output/salman-2023-optimization-trading-strategies-genetic-algorithm-under.md
source_type: paper
tags:
- directional-change
- genetic-algorithm
- trading-strategy
- multi-threshold
- sharpe-ratio
- equity
- technical-analysis
- clock-intrinsic
- asset-equity
- harvest-relevant
title: Optimization of Trading Strategies Using a Genetic Algorithm under the Directional
  Changes Paradigm with Multiple Thresholds
updated: '2026-09-27T01:47:00Z'
uuid: 70f0c7c8-c40f-5c64-a515-db912cb7aed3
year: 2023
---

<!-- AUTHORED REGION START -->
# Optimization of Trading Strategies Using a Genetic Algorithm under the Directional Changes Paradigm with Multiple Thresholds

## Summary

The paper asks whether a Directional Change (DC) trading strategy can be improved by using many price-change thresholds at once instead of a single, manually chosen one. DC records a price event only once price has moved by a threshold from the last extreme point, alternating between directional-change and overshoot phases, and prior DC-based strategies had generally relied on a single threshold value.

The authors define three new DC-based trading strategies: one based on the empirical scaling law that an overshoot event tends to last about twice as long as its preceding directional-change event; one based on a current-overshoot-magnitude indicator compared against a best value chosen from its own distribution; and one based on seeing three consecutive overshoot events in the same trend. Each strategy is run separately under ten fixed thresholds (five, for the third strategy), so every threshold produces its own buy, hold or sell recommendation at every point in time. A genetic algorithm then learns and evolves a weight for each threshold, using the Sharpe ratio as its fitness function, so that the strategy's final recommendation follows whichever action has the largest combined weight across thresholds.

On 18 NYSE-listed stocks, the genetic-algorithm-optimized combination of thresholds achieved higher Sharpe ratios and rates of return than any individual single-threshold version of the same strategy, and than relative-strength-index, moving-average-convergence-divergence and buy-and-hold benchmarks, with the improvement in risk-adjusted return confirmed as statistically significant by nonparametric tests in most comparisons. The main exception is risk: the combined strategies were not the lowest-risk option, and the authors note the strong bull-market test period may partly explain the size of the gains.

What is new is treating multiple DC thresholds as simultaneous, weighted inputs to a single trading decision, with the weights learned by a genetic algorithm, rather than fixing or individually optimizing one threshold at a time as in earlier DC trading-strategy work.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Observations are event-based under the Directional Change (DC) paradigm: a DC event is confirmed whenever price moves against the current trend by more than a threshold $\theta$ from the last extreme point, followed by an overshoot (OS) event that continues until the next DC event is confirmed. Ten thresholds are tracked in parallel (0.098%, 0.22%, 0.48%, 0.72%, 0.98%, 1.22%, 1.55%, 1.70%, 2%, 2.55%, with only the first five used for one of the three strategies), each generating its own buy/hold/sell recommendation at every data point, and a genetic algorithm learns a weight per threshold so the final decision follows the recommendation with the largest total weight. There is no fixed forecast horizon; positions are opened and closed according to each strategy's own DC/overshoot timing rules, and performance is judged on the resulting test-period return and risk.

## Data

- **Asset class:** Equities
- **Instruments:** 18 NYSE-listed stocks: ALL, ASGN, CI, COP, CTXS, EME, EVR, GILD, GPK, ISRG, MKL, MOH, PEG, PXD, QCOM, UBSI, VFC, XEL
- **Venue:** New York Stock Exchange, price data sourced from Yahoo Finance
- **Period:** November 27, 2009 to November 27, 2019
- **Granularity:** Daily adjusted closing prices, split 60% for training, 20% for validation and 20% for testing

## Features and Measures

- **Number of DC events (NDC).** The count of confirmed directional-change events over the profiled period.
- **Number of overshoot events (NOS).** The count of overshoot events over the profiled period.
- **Theoretical confirmation point (DCC*).** The earliest point at which the price change since the last extreme point reaches the threshold, used to time trade signals more precisely than the discrete confirmation point.
- **Overshoot Value at Current Point (OSVCUR).** An indicator measuring the magnitude of the ongoing overshoot move relative to the current price, evaluated at every data point rather than only at trend extremes.

## Method

Three DC-based strategies are defined: the first buys or sells after waiting twice the duration of the most recent directional-change event, based on an empirical scaling law relating overshoot and directional-change durations; the second compares the current overshoot-value indicator against a best-performing value selected from the quartiles of its own distribution, chosen by in-sample Sharpe ratio; the third acts after observing three consecutive overshoot events in the same trend. Each strategy is evaluated separately under ten fixed thresholds (five for the third strategy), and a genetic algorithm then assigns and evolves a weight per threshold using one-point crossover, one-point mutation and elitism, with the Sharpe ratio as the fitness function; genetic-algorithm hyperparameters (population size, number of generations, crossover probability) are tuned by grid search on a held-out subset of the training data. Test-set performance is measured by Sharpe ratio, rate of return and the standard deviation of returns (risk), and the genetic-algorithm-optimized strategies are compared against every individual single-threshold version of the same strategy, and against relative strength index, moving average convergence divergence, and buy-and-hold benchmarks, with differences assessed using the nonparametric Friedman test and Conover post-hoc comparisons.

## Results

- The genetic-algorithm-optimized strategies achieved Sharpe ratios of 4.14, 2.50 and 5.63 for the three strategies, versus best single-threshold Sharpe ratios of only 0.59, 1.63 and 2.83 respectively.
- Average rate of return for the genetic-algorithm-optimized strategies was 24.5%, 18.2% and 16.1% for the three strategies, compared with 11.17% for RSI, 1.3% for MACD and 14.9% for buy-and-hold.
- Risk (standard deviation of returns) for the genetic-algorithm-optimized strategies ranged from about 2% to 8%, similar to the individual single-threshold strategies.
- Friedman tests with Conover post-hoc comparisons ranked the genetic-algorithm-optimized strategy first for Sharpe ratio and rate of return across all three strategies, with statistically significant differences against most individual thresholds.
- The genetic-algorithm-optimized strategies were not the lowest-risk option: they ranked 2nd, 2nd and 5th among competing strategies on risk, with no statistical significance found there.
- The best-performing genetic-algorithm-optimized strategy achieved nearly 3.5 times the Sharpe ratio of RSI and about 25 times that of MACD.
- The genetic-algorithm-optimized strategies statistically outperformed RSI and MACD, though in some comparisons the difference was only significant at the 10% level.

## Limitations

- A transaction cost of 0.25% per trade is applied, but no other frictions such as slippage or market impact are modeled.
- The test period coincided with a strong bull market, which the authors note may partly explain the size of the Sharpe ratio and rate-of-return improvements.
- Reader note: only 18 NYSE stocks and a single roughly ten-year sample window (chosen partly to exclude the COVID-19 period) are tested, limiting how far the results generalize across markets and regimes.
- Short selling is not permitted and only one position can be open at a time, simplifying the trading rules relative to a live strategy.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/directional-change|Directional Change]]
- [[entities/ozgur-salman|Ozgur Salman]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Ozgur Salman, Themistoklis Melissourgos, Michael Kampouridis (2023). Optimization of Trading Strategies Using a Genetic Algorithm under the Directional Changes Paradigm with Multiple Thresholds.

DOI: 10.1109/cec53210.2023.10254029

Text ingested: `markdown_output/salman-2023-optimization-trading-strategies-genetic-algorithm-under.md`, converted from `raw/ofi-event-clock/salman-2023-optimization-trading-strategies-genetic-algorithm-under.pdf`.

Coverage of this summary: Read the full paper end to end, including the introduction, DC background, related work, methodology for all three strategies and the genetic algorithm, experimental setup, all eleven results tables, and the conclusion.

Known problems with the input: No conference or journal name is printed in the markdown; only an IEEE copyright/ISBN-style line (979-8-3503-1458-8/23) appears, so the specific venue is recorded as not stated even though the numbering suggests an IEEE 2023 proceeding.
<!-- AUTHORED REGION END -->