---
authors:
- Xinpeng Long
- Michael Kampouridis
- Tasos Papastylianou
content_hash: sha256:cb8e4a6c781b245b9a2b61ce268ac0de880aea478f14c4b510fb351ab02d9e6f
created: 2026-09-27 01:47:00+00:00
page_id: sources/long-2026-multi-objective-genetic-programming-based-algorithmic
page_type: source
publication_venue: Artificial Intelligence Review
related:
- concepts/alpha-signal
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/feature-engineering
- concepts/deep-learning-for-finance
- concepts/transformers
- concepts/directional-change
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:5bf7dc6708da2523fb94120e835751806e83d98073127e76ff64c1dfee323ecb
source_path: markdown_output/long-2026-multi-objective-genetic-programming-based-algorithmic.md
source_type: paper
tags:
- algorithmic-trading
- genetic-programming
- directional-changes
- multi-objective-optimisation
- nsga-ii
- equity-trading-strategies
- sharpe-ratio
- clock-calendar
- asset-equity
- harvest-relevant
title: Multi-objective genetic programming-based algorithmic trading, using directional
  changes and a modified sharpe ratio score for identifying optimal trading strategies
updated: '2026-09-27T01:47:00Z'
uuid: 1e116d1b-86d8-55b1-b7ac-c83910f3694f
year: 2026
---

<!-- AUTHORED REGION START -->
# Multi-objective genetic programming-based algorithmic trading, using directional changes and a modified sharpe ratio score for identifying optimal trading strategies

## Summary

Trading strategies built purely to maximise a single number, such as return alone or an aggregate metric like the Sharpe ratio, oversimplify the real trade-off traders face between return and risk. This paper asks whether treating return and risk as genuinely separate, competing objectives inside a genetic-programming trading-rule search produces better strategies than one that collapses everything into a single aggregate score.

The authors propose 'MOO3', which uses genetic programming (GP) to evolve buy/hold trading rules represented as syntax trees, built from indicators computed under two frameworks: directional-change (DC) event-based indicators and conventional fixed-time technical-analysis indicators. Instead of optimising one fitness score, GP individuals are evaluated with the NSGA-II multi-objective algorithm across three objectives at once (total return, expected rate of return, and risk), producing a Pareto front of trade-off solutions rather than a single answer. To turn that front into one deployable strategy, they define a new aggregate metric, a 'modified Sharpe Ratio' with adjustable weights, so a trader can pick the point on the front matching their own preference among the three objectives; they test seven preset weight combinations. This multi-objective approach is compared against a single-objective GP baseline that uses the same aggregate metric directly as its fitness function, against three classic technical-analysis benchmark strategies, against a Transformer-based deep learning model, and against buy-and-hold, over 110 stock and index datasets from 10 international markets.

Across almost all seven trader-preference weightings, the multi-objective GP achieves higher mean and median total return and expected rate of return, and a higher portfolio-level Sharpe ratio, than the single-objective GP using the identical aggregate metric, even in the weightings where the single-objective approach is optimising that exact metric directly. Statistical tests confirm the multi-objective versions rank ahead of single-objective ones for total return, expected rate of return, and risk, and this advantage holds consistently across all markets tested. The multi-objective approach also outperforms the three technical-analysis benchmarks, the Transformer-based benchmark, and buy-and-hold on total return and risk-adjusted return, though the Transformer model achieves the single highest maximum return and comparably low risk to the risk-focused multi-objective variant.

What is new is applying multi-objective optimisation, rather than single-objective GP or an aggregate score, specifically within the directional-change event framework; adding a third objective (total return) to an earlier two-objective version of this idea; and the modified Sharpe Ratio itself as a tunable, trader-preference-driven way to pick one strategy off a Pareto front.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The underlying data for every dataset is a daily closing-price series (a calendar clock). Trading decisions are evaluated once per trading day using a GP-tree buy/hold rule built from two indicator families computed over that same daily series: physical-time technical-analysis indicators computed over fixed rolling day-windows, and directional-change (DC) indicators, which resegment the daily price series into event-based upturn and downtrend segments whenever price moves beyond a user-set relative threshold from the last extreme. A position, once opened, is closed either after a fixed number of calendar days has passed or once price has risen by a preset percentage, whichever happens first; strategy performance (total return, expected rate of return, risk) is then measured on a held-out out-of-sample period rather than as a single fixed-horizon point forecast.

## Data

- **Asset class:** Equities
- **Instruments:** 100 individual stocks (10 arbitrarily chosen per market) plus the representative stock market index for each market, across 10 international markets: Dow Jones Industrial Average, NASDAQ, NYSE, Russell 2000, and S&P 500 in the United States; Nifty Fifty in India; the Taiwan Stock Exchange Corporation index; the DAX in Germany; the Nikkei 225 in Japan; and the FTSE 100 in the United Kingdom; 110 datasets in total.
- **Venue:** Data sourced from Yahoo! Finance; underlying markets are US, Indian, Taiwanese, German, Japanese and UK exchanges (see instruments).
- **Period:** A 10-year period from 25th November 2010 to 24th November 2020, resulting in approximately 2,500 data points per dataset. The first 60% of each dataset is used for training, the next 20% for validation, and the final 20% for testing.
- **Granularity:** Daily closing prices.

## Features and Measures

- **Total price movement (TMV).** The directional-change price movement between the extreme point at the start and end of a trend, normalised by the DC threshold.
- **Overshoot Value (OSV).** The percentage difference between the current price and the last directional-change confirmation price, divided by the DC threshold.
- **Time-adjusted return (RDC).** A DC-based return measure calculated as TMV times the DC threshold, divided by the time interval between extreme points.
- **Time on trend (TDC).** The amount of time spent on a directional-change trend segment, also averaged over several lookback periods.
- **Number of DC events (NDC).** The count of directional-change events observed over a selected lookback period.
- **Cumulative DC movement (CDC).** The sum of the absolute value of TMV over a selected lookback period.
- **Asymmetry of trend time (AT).** The difference between the time price spends in DC uptrends versus downtrends over a selected lookback period.
- **Physical-time technical indicators.** A set of standard fixed-time technical-analysis indicators (moving average, commodity channel index, relative strength index, Williams %R, average true range, exponential moving average, on-balance volume, parabolic stop-and-reverse), computed over rolling windows of several lengths, used alongside the DC indicators as inputs to the trading-rule search.

## Method

MOO3 represents each trading rule as a genetic-programming (GP) syntax tree with a fixed 'If-Then-Else' root that outputs a buy or hold decision from a boolean condition built out of logic and comparison operators, DC-based indicators, physical-time technical-analysis indicators, and random constants; the terminal set draws from 28 DC indicators and 28 physical-time technical indicators, each normalised to lie between zero and one. A position is closed automatically once either a fixed number of calendar days (n) has passed since purchase, or the price has risen by a percentage (r), whichever comes first; short selling is not allowed, and each completed trade incurs a 0.025% transaction cost. Rather than optimising a single fitness score, GP individuals are evolved with the NSGA-II multi-objective algorithm across three objectives at once: total return, expected rate of return, and risk, producing a Pareto front instead of one solution. Standard GP parameters (population size, tree depth, crossover probability, tournament size, generations) are tuned once via grid search on a validation subset of 10 datasets and then reused across all datasets; the selected values are a maximum tree depth of 6, a population of 500, a crossover probability of 0.95, a tournament size of 2, and 50 generations. The dataset-specific parameters (the sell-rule day count n, the sell-rule return threshold r, and the DC threshold) are tuned separately per dataset and per trader-preference scenario via a grid search of 3 x 4 x 5 = 60 configurations, each run 5 times.

After training, the single Pareto-optimal solution to deploy is chosen with a new aggregate metric, the modified Sharpe Ratio (mSR), which combines normalised total return, expected rate of return, and risk with adjustable weights that a trader sets to express a preference; the paper tests seven preset weight combinations. MOO3 is compared against a single-objective GP (SOO) using the mSR directly as its fitness function, three technical-analysis zero/threshold-crossing benchmark strategies (MACD, on-balance-volume, momentum), a Transformer-based deep learning model using the same trading-decision logic, and a passive buy-and-hold strategy. Each GP-based algorithm is run 50 times per dataset and scenario, and test-set performance is averaged over these runs. Differences between algorithms are assessed with Kolmogorov-Smirnov tests (with Holm-Bonferroni correction) and with the non-parametric Friedman test plus Hommel post-hoc correction.

## Results

- Across almost all seven trader-preference weightings, the multi-objective GP (MOO3) shows higher mean and median total return and expected rate of return than the single-objective GP (SOO) using the identical modified-Sharpe-Ratio fitness function, and MOO3 gets a higher portfolio Sharpe ratio in most weight setups.
- Kolmogorov-Smirnov tests find statistically significant differences between MOO3 and SOO in 9 of 21 metric-by-weighting comparisons at the 5% level, mostly favouring MOO3 on total return and expected rate of return.
- Friedman tests across all weight setups and all 110 datasets rank MOO3 variants ahead of every SOO variant for total return and expected rate of return, and the risk-focused MOO3 variant ranks best for risk.
- The advantage of MOO3 over SOO holds consistently across all international markets tested, with the algorithm focused on a given objective always ranking best on that same objective within each market.
- MOO3 significantly outperforms three technical-analysis benchmark strategies (MACD, on-balance-volume, momentum) on total return, expected rate of return, and risk-adjusted (Sharpe) return.
- Against a Transformer-based benchmark, the return-focused and balanced MOO3 variants achieve higher average and median total return; the Transformer achieves the single highest maximum total return but with much higher variability and the worst Sharpe ratio (0.50), while a risk-focused MOO3 variant achieves comparably low average risk.
- MOO3 significantly outperforms a passive buy-and-hold strategy on total return according to Friedman tests, even though buy-and-hold's average return is inflated by a small number of large outlier trades.

## Limitations

- The single portfolio-level Sharpe ratio figure assumes an equally weighted portfolio of the 110 stocks; the paper does not attempt portfolio-weight optimisation.
- Parameter tuning is computationally heavy (33,000 tuning experiments per algorithm), which the authors flag as a scalability concern and propose addressing with parallelisation for periodic retraining.
- The trading-rule design assumes full-capital, single-asset market orders with no slippage, latency, or partial fills, so real trading frictions are not modelled.
- Reader note: the benchmark Transformer and technical-analysis strategies are relatively simple compared to the current state of the art in each of those families, so the comparison mainly demonstrates the value of the multi-objective GP framework rather than establishing an absolute best-in-class forecasting model.

## Related

- [[concepts/alpha-signal|alpha signal]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/transformers|transformers]]
- [[concepts/directional-change|Directional Change]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Xinpeng Long, Michael Kampouridis, Tasos Papastylianou (2026). Multi-objective genetic programming-based algorithmic trading, using directional changes and a modified sharpe ratio score for identifying optimal trading strategies. Artificial Intelligence Review.

DOI: 10.1007/s10462-025-11390-9

Text ingested: `markdown_output/long-2026-multi-objective-genetic-programming-based-algorithmic.md`, converted from `raw/ofi-event-clock/long-2026-multi-objective-genetic-programming-based-algorithmic.pdf`.

Coverage of this summary: Read the full paper (45 pages): abstract, introduction, background on directional changes/GP/NSGA-II, literature review, methodology (GP representation, model evaluation, selection and genetic operators, modified Sharpe Ratio), experimental setup (data, benchmarks, trader-preference scenarios, parameter tuning), the full results and analysis section (Pareto front illustration, convergence analysis, MOO-vs-SOO comparison, market-condition comparison, TA-indicator comparison, Transformer comparison, buy-and-hold comparison, algorithmic complexity, real-world scalability), and the conclusion.

Known problems with the input: Several equations are rendered as omitted pictures in the markdown conversion; the surrounding prose was used instead of the formulas themselves; The large result tables (Tables 6 through 16) have cell-alignment artifacts from the markdown conversion of multi-row table cells, so individual per-market or per-scenario cell values were not re-derived from the raw table text; findings rely on the paper's own prose summaries of these tables.
<!-- AUTHORED REGION END -->