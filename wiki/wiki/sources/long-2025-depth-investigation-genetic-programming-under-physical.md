---
authors:
- Xinpeng Long
- Michael Kampouridis
- Panagiotis Kanellopoulos
content_hash: sha256:f68003a53e001df3c123e29b96096b11162751f68caee5bdef87639eff7366c9
created: 2026-09-27 01:47:00+00:00
page_id: sources/long-2025-depth-investigation-genetic-programming-under-physical
page_type: source
publication_venue: IEEE Access
related:
- concepts/sampling-clocks
- concepts/backtesting
- concepts/feature-engineering
- concepts/alpha-signal
- concepts/directional-change
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:99b623d5030eea414a3cf15979cdda256dfec195e48f2fbe8e47733c9f625b1d
source_path: markdown_output/long-2025-depth-investigation-genetic-programming-under-physical.md
source_type: paper
tags:
- genetic-programming
- directional-changes
- algorithmic-trading
- technical-analysis
- equity-markets
- backtesting
- clock-compares
- asset-equity
- harvest-relevant
title: An In-Depth Investigation of Genetic Programming Under Physical Time and Directional
  Change Frameworks for Algorithmic Trading
updated: '2026-09-27T01:47:00Z'
uuid: 1eef2264-01e6-586e-b423-d9ecd28054b5
year: 2025
---

<!-- AUTHORED REGION START -->
# An In-Depth Investigation of Genetic Programming Under Physical Time and Directional Change Frameworks for Algorithmic Trading

## Summary

The paper asks whether representing price movement as directional-change (DC) events, either alone or alongside conventional fixed-interval physical-time (PT) technical indicators, improves genetic-programming (GP) trading strategies compared with using physical-time indicators only.

The authors build three GP variants that evolve if-then-else logical trading trees: GP-DC uses only 28 DC-based indicators, GP-PT uses only 28 physical-time technical indicators as a benchmark, and GP-DC-PT combines both sets of 28 indicators in one terminal set. A GP individual's rule buys a stock if it predicts the price will rise by a tuned percentage within a tuned number of days, and otherwise holds; fitness is the Sharpe ratio of resulting trades net of a per-trade transaction cost. The strategies are evaluated on 220 datasets (10 stocks from each of 10 international market indices, over both a 5-year and a 10-year period), each split into training, validation and test sets, with trading-rule and DC-threshold parameters tuned per dataset.

Both DC-based algorithms significantly outperform the physical-time-only GP-PT on total return, and have lower risk, across the full set of 220 datasets. Looking at time horizons separately, GP-DC leads on total return and rate of return over 5 years, while GP-DC-PT delivers the lowest risk and the best Sharpe ratio in both the 5-year and 10-year periods. GP-DC-PT also significantly beats three popular technical indicators (MACD, OBV, MTM) and the buy-and-hold benchmark on return, risk and Sharpe ratio.

What is new relative to the authors' own earlier work is combining DC-based indicators with standard technical-analysis indicators inside a single GP terminal set, rather than using DC indicators alone; the study also scales the earlier evaluation from 33 stocks in 3 markets up to 220 datasets across 10 markets and two time horizons, and adds total return as an evaluation metric alongside rate of return, risk and the Sharpe ratio.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Prices start as fixed daily closing values, which are then transformed into directional-change (DC) events: a new event is only marked once cumulative price movement since the last event crosses a trader-set percentage threshold theta, giving an event-driven series alongside the original daily bars. DC-based indicators are computed over the DC event sequence while physical-time technical indicators are computed over the daily bars, and both feed the same genetic-programming trading rule. The prediction horizon is set by the trading rule itself: a strategy predicts whether the price will rise by r% within the next n days, with r tuned per dataset from {1%, 5%, 10%, 20%} and n from {1, 5, 15} days, and the position is closed either on hitting the target or after n days.

## Data

- **Asset class:** Equities
- **Instruments:** 10 stocks from each of 10 international market indices (FTSE100, DAX, Dow Jones, Nasdaq, NYSE, Russell 2000, S&P500, Nifty Fifty, Taiwan Stock Exchange, Nikkei 225) plus the index series themselves; 220 datasets in total across two time periods
- **Venue:** Yahoo! Finance
- **Period:** Two periods per dataset: 5 years (24/11/2015 to 24/11/2020) and 10 years (25/11/2010 to 24/11/2020)
- **Granularity:** Daily closing prices

## Features and Measures

- **DC indicators (28).** Twenty-eight measures computed over directional-change event sequences, such as the count of DC events over 10/20/30/40/50-day windows, overshoot value, and total price move, used as GP terminal-set variables.
- **Physical-time technical indicators (28).** Twenty-eight standard technical-analysis indicators, including moving average, CCI, RSI, William's %R, ATR, EMA, OBV and PSAR, computed with TA-Lib over fixed daily windows and used as GP terminal-set variables.
- **Directional-change threshold theta.** A percentage threshold that determines when a price move is large enough to register a new DC event; tuned per dataset from a grid of candidate values.

## Method

Each of three GP variants (GP-DC, GP-PT, GP-DC-PT) evolves if-then-else logical trees built from AND/OR/less-than/greater-than operators over terminal indicators, using tournament selection, elitism, subtree crossover and point mutation. A tree's Boolean output triggers a buy (otherwise hold) action, and an open position is closed either when price rises by the tuned target percentage or after the tuned number of days. Fitness is the Sharpe ratio of the resulting per-trade returns, net of a 0.025% transaction cost per trade. Each of the 220 datasets is split 60/20/20 into training, validation and test sets; GP parameters are grid-searched and the trading-rule parameters are tuned per dataset on the training and validation data before evaluation on the held-out test set. Performance is judged on total return, rate of return per trade, risk (the standard deviation of per-trade returns) and the Sharpe ratio, compared against a physical-time-only GP, three technical indicators, and buy-and-hold, using the non-parametric Kolmogorov-Smirnov test with Bonferroni correction to assess statistical significance.

## Results

- Across all 220 datasets, GP-DC achieved the highest average (14.90%) and median (10.19%) total return of the three GP variants, while GP-DC-PT had the lowest risk overall.
- Both GP-DC and GP-DC-PT significantly outperformed GP-PT on total return (Kolmogorov-Smirnov p-value 0.0125 for GP-DC vs GP-PT, below the Bonferroni-adjusted 0.025 threshold).
- In the 5-year period GP-DC led on total return (average 13.89%, median 9.63%) and rate of return, while GP-DC-PT had the lowest average risk (0.06).
- In the 10-year period GP-PT had the highest average total return (21.38%), a result the authors attribute to outliers such as a 571.21% maximum return in a strongly bullish stock.
- GP-DC-PT achieved the highest portfolio Sharpe ratio in both the 5-year and 10-year periods, an improvement over GP-DC of about 33% at 5 years and 66% at 10 years.
- Using the best tree from 50 training runs per dataset, GP-DC-PT's median total return (11.63%) was about three times GP-DC's, though GP-PT still had the lowest median risk among best trees (0.04 versus GP-DC-PT's 0.05).
- GP-DC-PT significantly outperformed the MACD, OBV and MTM technical indicators on total return, risk and Sharpe ratio (all Kolmogorov-Smirnov p-values below the Bonferroni-adjusted 0.0167 threshold).
- GP-DC-PT significantly outperformed buy-and-hold on total return (p-value 0.0169); buy-and-hold's average return was inflated by extreme outliers, including a 1753.05% maximum return, and after trimming outliers to within two standard deviations its average total return (12.13%, standard deviation 0.46) was still below GP-DC-PT's (16.97%, standard deviation 0.33).

## Limitations

- Backtested results do not guarantee live-trading performance, where latency, slippage and market impact could affect profitability.
- Portfolio evaluation used equal weighting across datasets rather than an optimized allocation; the authors leave portfolio-weight optimization to future work.
- Reader note: the trading-rule and DC-threshold parameters were tuned per individual dataset rather than fixed globally, which may overstate performance relative to a single deployable rule set.
- Reader note: all data are daily-bar equities from Yahoo! Finance; no fixed-income, futures or intraday data are tested.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/backtesting|backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/directional-change|Directional Change]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Xinpeng Long, Michael Kampouridis, Panagiotis Kanellopoulos (2025). An In-Depth Investigation of Genetic Programming Under Physical Time and Directional Change Frameworks for Algorithmic Trading. IEEE Access.

DOI: 10.1109/access.2025.3599677

Text ingested: `markdown_output/long-2025-depth-investigation-genetic-programming-under-physical.md`, converted from `raw/ofi-event-clock/long-2025-depth-investigation-genetic-programming-under-physical.pdf`.

Coverage of this summary: Read the full paper text, from abstract through methodology, experimental setup, and all results subsections to the concluding remarks.

Known problems with the input: The PDF-to-markdown conversion garbles some inline decimals and figure/table content (e.g. figure-caption thresholds rendered as '0 _._ 22'); only prose and table values that could be read unambiguously were used.
<!-- AUTHORED REGION END -->