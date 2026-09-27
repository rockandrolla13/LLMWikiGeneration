---
authors:
- Ozgur Salman
- Michael Kampouridis
- Delaram Jarchi
content_hash: sha256:340bdb8f70206fc03c067eb8af416f76f3eef187b35a720cb55af369c5343d7b
created: 2026-09-27 01:47:00+00:00
page_id: sources/salman-2022-trading-strategies-optimization-genetic-algorithm-under
page_type: source
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/alpha-signal
- concepts/feature-engineering
- concepts/directional-change
- entities/ozgur-salman
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:fe3efc40daaf11e5c925ade27b3670a44d9f1a9ace6fdbd56b1677d623fa0f23
source_path: markdown_output/salman-2022-trading-strategies-optimization-genetic-algorithm-under.md
source_type: paper
tags:
- directional-changes
- genetic-algorithm
- event-based-sampling
- equities
- trading-strategies
- backtesting
- clock-intrinsic
- asset-equity
- harvest-relevant
title: Trading Strategies Optimization by Genetic Algorithm under the Directional
  Changes Paradigm
updated: '2026-09-27T01:47:00Z'
uuid: e95dd61d-c6be-5df2-acbd-db509d7cbbf8
year: 2022
---

<!-- AUTHORED REGION START -->
# Trading Strategies Optimization by Genetic Algorithm under the Directional Changes Paradigm

## Summary

The paper's motivation is that sampling prices at fixed calendar intervals ('physical time series') can miss significant, fast moves that occur between sampling points, such as a flash crash. It instead profiles price series with the Directional Changes (DC) framework, which marks a new event only once price has reversed by a chosen threshold against the prevailing trend, splitting the series into directional-change and overshoot segments.

The authors build four new trading rules from existing DC indicators (current or extreme-point overshoot value, current or extreme-point total price movement, and the ratio of overshoot to DC event counts) and combine them with three previously published DC- and scaling-law-based rules. Each of the seven strategies proposes an open, hold or close action at every point; a genetic algorithm then assigns and evolves a weight per strategy so that, at each decision point, the action whose strategies' weights sum highest is taken, using the resulting Sharpe ratio as the fitness function.

Tested on 44 NYSE stocks over a ten-year window at a 2.5% DC threshold, several individual DC strategies already produced strong Sharpe ratios and returns. The GA-weighted combination achieved the single highest average Sharpe ratio and rate of return across 50 runs, statistically beating most (though not all) of the individual strategies, and beat a passive buy-and-sell benchmark by a statistically significant margin in return, although it did not reduce risk (standard deviation) relative to the individual strategies.

What is new is the four DC-indicator-based strategies themselves, and using a genetic algorithm to reconcile the potentially conflicting open/hold/close recommendations of several DC-based strategies into one combined strategy, rather than only optimizing the DC threshold as earlier GA-based DC work had done.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Price series are re-profiled from calendar time into Directional Change (DC) and Overshoot (OS) events using a fixed threshold theta (2.5% in the experiments): a DC event is confirmed once price reverses by theta against the current trend, and the subsequent move up to the next reversal is the overshoot. Each strategy's open, hold or close decisions and its trading horizon are defined relative to these DC confirmation points rather than to fixed calendar time.

## Data

- **Asset class:** Equities
- **Instruments:** 44 U.S. common stocks traded on the New York Stock Exchange (tickers listed in the paper, including AAL, AAPL, AMZN, IBM, JPM, WMT and XOM).
- **Venue:** New York Stock Exchange, with price data obtained via the Yahoo Finance 'yfinance' Python library.
- **Period:** 20.03.2011 to 20.03.2021, split 60% training, 20% validation and 20% test.
- **Granularity:** Daily adjusted closing prices, re-profiled from calendar time into Directional Change and Overshoot events using a 2.5% threshold.

## Features and Measures

- **Number of DC events (NDC).** A count of confirmed directional-change events over a period at a given threshold, used as a rough volatility gauge for that threshold.
- **Number of Overshoot events (NOS).** A count of overshoot events following DC events; a low NOS relative to NDC can flag that one DC event is quickly followed by another.
- **Overshoot Value (OSV / OSVEXT).** The size of the current, or extreme-point, price move measured from the last directional-change confirmation price, scaled by the threshold, used to gauge how far an overshoot has run.
- **Total price Movement Value at extreme points (TMVEXT).** The price change between two consecutive extreme points of the price series, scaled by the threshold, used as a rough measure of the profit available in a completed trend.
- **Theoretical Confirmation Point (PDCC*).** The smallest price move, in the current trend's direction, that would be sufficient to confirm the next directional-change event.

## Method

Three of the seven trading strategies open or close positions based on two previously published DC 'scaling laws' relating the durations and price changes of DC and overshoot events; the other four are new rules built from DC indicators (current or extreme-point overshoot value, current or extreme-point total price movement, and the overshoot-to-DC count ratio), each triggered when the indicator crosses a threshold chosen from its historical distribution by maximizing Sharpe ratio on a validation set. All strategies impose a fixed per-trade transaction cost, allow short positions, and require closing any open position before a new one can be opened.

A genetic algorithm then assigns one weight per strategy (seven genes per individual), with the decision at each point given by the action (open, hold or close) whose strategies' weights sum highest; the population is seeded with individuals representing each pure strategy, evolved with one-point crossover and mutation plus elitism, and its fitness is the resulting portfolio's Sharpe ratio. GA hyper-parameters (population size, generations, crossover probability) were tuned by grid search on a validation set, and the tuned GA, the seven individual strategies, and a passive buy-and-sell benchmark were compared over 50 runs on the 44-stock test set using average Sharpe ratio, rate of return and standard deviation, together with a non-parametric Friedman test with Hommel post-hoc correction across strategies and a Kolmogorov-Smirnov test against the buy-and-sell benchmark.

## Results

- Averaged over 50 runs on the 44 test stocks, the GA-combined strategy reached a Sharpe ratio of 6.47 and a 0.49 rate of return, against a best single-strategy Sharpe ratio of 6.06 and 0.46 rate of return for strategy St7.
- Under the Friedman test with Hommel correction, the GA statistically outperformed strategies St1, St3, St4, St5 and St6 on both Sharpe ratio and rate of return, but did not statistically beat St2 or St7 on either metric.
- The GA ranked first among all strategies on 17 of the 44 stocks for both Sharpe ratio and rate of return, more than any individual strategy (the closest, St7, ranked first on 12).
- On standard deviation (risk), the GA did not lead: strategy St1 had the lowest average standard deviation and statistically outperformed the GA and most other strategies on this metric.
- The GA-combined strategy averaged a 49% rate of return versus 19.4% for a passive buy-and-sell benchmark on the same stocks; a Kolmogorov-Smirnov test rejected the hypothesis that the GA and buy-sell return distributions were the same, with a p-value of 0.02266.
- The best GA configuration found by grid search used a population of 100, 35 generations, and a crossover probability of 0.95 (mutation probability 0.05).

## Limitations

- Results are reported for a single Directional Changes threshold (2.5%); the authors leave testing other thresholds to future work.
- All 44 stocks were tested over a single, largely bullish window (20.03.2011 to 20.03.2021), and the authors note this bull-market backdrop partly explains the strong absolute returns of both the GA strategy and the buy-and-sell benchmark.
- The GA improved Sharpe ratio and rate of return but not risk: it did not reduce standard deviation relative to the individual DC strategies.
- Reader note: the paper reports results only for equities, so nothing here directly establishes whether DC-based strategies or this GA-combination approach transfer to bonds or other asset classes.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/directional-change|Directional Change]]
- [[entities/ozgur-salman|Ozgur Salman]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Ozgur Salman, Michael Kampouridis, Delaram Jarchi (2022). Trading Strategies Optimization by Genetic Algorithm under the Directional Changes Paradigm.

DOI: 10.1109/cec55065.2022.9870270

Text ingested: `markdown_output/salman-2022-trading-strategies-optimization-genetic-algorithm-under.md`, converted from `raw/ofi-event-clock/salman-2022-trading-strategies-optimization-genetic-algorithm-under.pdf`.

Coverage of this summary: Read the entire converted markdown file front to back, including the literature review, the Directional Changes background, all seven strategy definitions, the GA methodology, the experimental setup, all results tables, and the conclusion.

Known problems with the input: No publication venue or in-text year is printed on the paper itself; year taken from job file metadata (2022); Several equation images (indicator formulas for OSV, PDCC*, OSVEXT, TMVEXT) are omitted in this conversion and could only be described in prose from the surrounding text.
<!-- AUTHORED REGION END -->