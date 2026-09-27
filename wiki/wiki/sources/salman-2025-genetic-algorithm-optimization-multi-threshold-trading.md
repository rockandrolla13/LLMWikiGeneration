---
authors:
- Ozgur Salman
- Themistoklis Melissourgos
- Michael Kampouridis
content_hash: sha256:dda9cb71fec49974a0ef4473c98147ca15ec34be903f085036cce7f3b9316ff5
created: 2026-09-27 01:47:00+00:00
page_id: sources/salman-2025-genetic-algorithm-optimization-multi-threshold-trading
page_type: source
publication_venue: Artificial Intelligence Review
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/alpha-signal
- concepts/directional-change
- entities/ozgur-salman
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:4ca15b5332ba5a88d0209941276453fc305d06c8c8f8b5cb7584af9ff5a868b0
source_path: markdown_output/salman-2025-genetic-algorithm-optimization-multi-threshold-trading.md
source_type: paper
tags:
- directional-changes
- genetic-algorithm
- technical-analysis
- equity-trading-strategy
- intrinsic-time
- backtesting
- nyse-stocks
- clock-intrinsic
- asset-equity
- harvest-relevant
title: A genetic algorithm for the optimization of multi-threshold trading strategies
  in the directional changes paradigm
updated: '2026-09-27T01:47:00Z'
uuid: 9a6e6a29-898d-5b6b-b508-71ebb1c23e07
year: 2025
---

<!-- AUTHORED REGION START -->
# A genetic algorithm for the optimization of multi-threshold trading strategies in the directional changes paradigm

## Summary

Technical trading strategies are usually built on fixed time intervals (daily, hourly, weekly), which can miss price information that occurs between those snapshots. The paper instead uses the directional-changes (DC) paradigm, an event-based sampling scheme that records a data point only when price moves by a chosen percentage threshold, and asks whether combining several DC-based trading strategies evaluated at several different thresholds, letting a genetic algorithm learn how to weight and combine their conflicting Buy/Sell/Hold recommendations, can out-trade both simpler DC strategies and conventional technical-analysis benchmarks.

Eight DC-based trading strategies are defined: two derived from previously documented DC scaling laws relating average overshoot size and duration to the threshold, and six built on DC-derived indicators (an overshoot/DC duration ratio, an overshoot/DC event-count ratio, overshoot-value and total-moves-value indicators benchmarked against training-set best values, and two pattern strategies that look for three consecutive overshoot events within one trend type). Each strategy is paired with ten thresholds (five for the two pattern strategies), forming 70 strategy-threshold sub-strategies; the proposed genetic algorithm, MSTGAM (Multi-Strategy/Threshold-Genetic-Algorithm-Model), represents each sub-strategy as one gene whose weight determines its contribution to the chromosome's aggregated trading decision, and evolves the weights using tournament selection, two-point crossover, one-point mutation and elitism to maximise the Sharpe ratio. The method is tested on daily closing prices of 200 randomly selected NYSE stocks over ten years, with eight years used for training and validation and the final two years held out for testing.

Against DC-based benchmarks (single-threshold multi-strategy models, single-strategy multi-threshold models, individual sub-strategies, and a naive DC-confirmation-point strategy) and non-DC benchmarks (seven technical indicators, buy-and-hold, and seven NYSE market indices), MSTGAM achieves the highest average Sharpe ratio (5.59) and rate of return (22%) of any strategy tested, while keeping standard deviation and Value-at-Risk lower than most benchmarks; Friedman tests with false-discovery-rate correction show it statistically outperforms every other tested algorithm on Sharpe ratio and rate of return at the 5% significance level.

What is new relative to the authors' two earlier papers is optimizing over both multiple strategies and multiple thresholds simultaneously in one chromosome, rather than fixing the threshold (as in the first paper) or fixing the strategy count (as in the second), which the authors argue lets the genetic algorithm draw on a wider, more complementary pool of signals.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Data are sampled using the directional-changes (DC) paradigm: an event fires only when price moves by at least a preset percentage threshold theta away from the last extreme price, defining alternating uptrend/downtrend regimes and directional-change/overshoot intervals rather than fixed calendar bars. Ten thresholds (from about 0.098% to 2.55%) are profiled in parallel across eight strategies and combined by the genetic algorithm. The underlying price series is daily NYSE closing prices, so DC events are detected on top of end-of-day data rather than intraday ticks, and each strategy's holding period runs from a signal's confirmation point in one trend until the corresponding confirmation point in the opposite trend.

## Data

- **Asset class:** Equities
- **Instruments:** 200 randomly selected stocks listed on the New York Stock Exchange
- **Venue:** New York Stock Exchange
- **Period:** November 27, 2009 to November 27, 2019 (first eight years for training/validation; final two years, November 27, 2017 to November 27, 2019, held out for testing)
- **Granularity:** Daily closing prices, obtained via the yfinance Python module

## Features and Measures

- **Directional change (DC) event.** A confirmed price move of at least a chosen threshold percentage away from the last extreme (peak or trough), which flips the market between an uptrend and a downtrend regime.
- **Overshoot (OS) event.** The interval between two directional-change confirmation points, during which price continues moving in the confirmed trend beyond the threshold that triggered it.
- **Ratio of duration (RD).** The total time spent in overshoot events divided by the total time spent in directional-change events, used as a trading trigger in Strategy 5.
- **Ratio of number of events (RN).** The number of overshoot events divided by the number of directional-change events, used as a probability-like trigger in Strategy 6.
- **Overshoot Value at Current Point (OSVCUR).** A running measure of how far the current price has moved beyond the extremum that started the current overshoot, compared against a best quartile value observed in training, used to trigger Strategy 3.
- **Total Moves Value at Current Point (TMVCUR).** A running measure of the total price movement from a trend's starting extreme point to the current price, compared against a best training-set value, used to trigger Strategy 4.
- **MSTGAM weighting chromosome.** A genetic-algorithm chromosome of 70 weights, one per combination of trading strategy and DC threshold, whose weighted vote across sub-strategies determines the chromosome's Buy/Sell/Hold action at each time step.

## Method

Eight trading strategies are defined over the DC paradigm: two follow previously documented DC scaling laws relating average overshoot size and duration to the threshold, and six use DC-derived indicators (duration ratios, event-count ratios, overshoot/total-move magnitudes measured against training-set best values, and two pattern strategies that look for three consecutive overshoot events in one trend type). Each strategy is combined with ten thresholds (or five, for the two pattern strategies), producing 70 strategy-threshold sub-strategies, each represented as one gene/weight in a chromosome; the sub-strategies' weighted Buy/Sell/Hold votes are aggregated, with a rule that ignores Hold recommendations once at least two sub-strategies vote to trade, to decide the chromosome's action at each point in time.

A genetic algorithm (MSTGAM) evolves populations of these chromosomes using tournament selection, two-point crossover with probability p and one-point mutation with probability 1-p, plus elitism that carries the best chromosome to the next generation; fitness is the Sharpe ratio computed on the training set. Population size, number of generations and crossover probability are tuned by grid search on a validation split (50 runs per configuration, best chromosome kept, configurations compared via the Friedman test), yielding a population size of 150, 50 generations, tournament size 2, crossover probability 0.95 and mutation probability 0.05; these are then fixed and the GA is re-run 50 times on the combined training-plus-validation data across all 200 stocks, keeping the highest-Sharpe chromosome for test-set evaluation. Trading rules disallow opening a new position while one is open, disallow short selling, and apply a transaction cost of 0.25% per trade.

Performance is judged on the held-out two-year test period by Sharpe ratio, rate of return, standard deviation, Value-at-Risk (95% confidence) and turnover rate, averaged across the 200 stocks, against two families of benchmarks: DC-based benchmarks (single-threshold multi-strategy models, single-strategy multi-threshold models, individual sub-strategies, and a naive DC-confirmation-point strategy) and non-DC benchmarks (seven technical indicators, buy-and-hold, and seven NYSE market indices); differences across all algorithms are tested with the non-parametric Friedman test followed by two-stage false-discovery-rate-corrected pairwise comparisons against the top-ranked algorithm.

## Results

- The combined multi-strategy, multi-threshold model (MSTGAM) achieves the highest average Sharpe ratio across 200 stocks, 5.59, about 3.26 times the best single-threshold multi-strategy benchmark and 1.79 times the best single-strategy multi-threshold benchmark.
- MSTGAM's average rate of return is 22%, adding an additional 3% over the next best-performing DC-based benchmark.
- Against non-DC benchmarks, MSTGAM's Sharpe ratio of 5.59 is far above the next highest, buy-and-hold at 1.62, and it delivers an additional return of over 8% in the rate-of-return metric compared with the technical-analysis and buy-and-hold benchmarks.
- MSTGAM's risk metrics remain moderate despite its highest trade count (70.19 trades on average) and highest turnover rate (4.40): standard deviation of 0.04 and Value-at-Risk of 0.05, both lower than most benchmarks.
- Friedman tests with false-discovery-rate correction show MSTGAM statistically outperforms every other tested algorithm on Sharpe ratio and rate of return at the 5% significance level, though it ranks only third on standard deviation and fourth on Value-at-Risk, behind the two single-strategy multi-threshold models.
- Against seven NYSE market indices, MSTGAM has the highest Sharpe ratio (5.59 versus a next-best 4.20 for the S&P 500) and the lowest standard deviation (0.036) and Value-at-Risk (0.05).
- Training the genetic algorithm takes about 55-60 minutes, but applying the trained best chromosome to the test set takes only about 15 seconds.

## Limitations

- The test period (2017-2019) was deliberately chosen to avoid COVID-19 market conditions, so the authors themselves note performance may not generalize to the extreme volatility and structural shifts seen afterward.
- The fitness function (Sharpe ratio) targets return volatility rather than tail-risk measures such as maximum drawdown or conditional Value-at-Risk, which the authors flag as a direction for future work.
- Headline results come from a single selected run (the highest-training-Sharpe chromosome out of 50 runs) rather than an average across all runs, which the authors themselves note needs further evaluation.
- Reader note: short selling is not permitted and all positions are long-only, so the strategies cannot directly monetize downtrends and results may not transfer to markets or rules that permit shorting.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/directional-change|Directional Change]]
- [[entities/ozgur-salman|Ozgur Salman]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Ozgur Salman, Themistoklis Melissourgos, Michael Kampouridis (2025). A genetic algorithm for the optimization of multi-threshold trading strategies in the directional changes paradigm. Artificial Intelligence Review.

DOI: 10.1007/s10462-025-11419-z

Text ingested: `markdown_output/salman-2025-genetic-algorithm-optimization-multi-threshold-trading.md`, converted from `raw/ofi-event-clock/salman-2025-genetic-algorithm-optimization-multi-threshold-trading.pdf`.

Coverage of this summary: Read the full markdown text in full, including the abstract, introduction, DC background, literature review, methodology (strategies, thresholds, genetic algorithm), experimental setup, all results tables and discussion, the computational-time note, and the conclusion.

Known problems with the input: Markdown contains PDF-conversion artifacts (equations and diagrams replaced by 'picture omitted' placeholders, table cells merged with embedded line breaks), but the surrounding prose and table values are legible and complete; The paper's running header prints a 2026 journal volume year (Artificial Intelligence Review (2026) 59:2) while the article's own published-online date and copyright line read 2025; the year field uses 2025 to match the stated publication/copyright date.
<!-- AUTHORED REGION END -->