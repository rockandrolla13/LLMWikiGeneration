---
authors:
- Adesola Adegboye
- Michael Kampouridis
- Fernando Otero
content_hash: sha256:7380c483d3b0872a9cc10180638d4b83887d95c226fe26008d0a50e025e75bb7
created: 2026-09-27 01:47:00+00:00
page_id: sources/adegboye-2022-algorithmic-trading-directional-changes
page_type: source
publication_venue: Artificial Intelligence Review
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/feature-engineering
- concepts/alpha-signal
- concepts/directional-change
- entities/adesola-adegboye
- entities/michael-kampouridis
revision_id: 1
schema_version: 2
source_hash: sha256:8736c3f2759d0717bc8e78220681ff101f0f91260c1635779e29c0a5c2e2be99
source_path: markdown_output/adegboye-2022-algorithmic-trading-directional-changes.md
source_type: paper
tags:
- directional-changes
- genetic-algorithm
- genetic-programming
- forex
- intrinsic-time
- algorithmic-trading
- trend-reversal
- clock-intrinsic
- asset-fx
- harvest-relevant
title: Algorithmic trading with directional changes
updated: '2026-09-27T01:47:00Z'
uuid: d09b40a8-e9e8-5105-9dba-1bb5a20e0eb5
year: 2023
---

<!-- AUTHORED REGION START -->
# Algorithmic trading with directional changes

## Summary

The paper asks whether combining several directional-change (DC) thresholds, instead of relying on one, can improve algorithmic FX trading. Directional changes summarise a price series in intrinsic, price-move, time: once price moves by a preset threshold from the last extreme, a DC event is confirmed, followed by an overshoot (OS) event until the trend reverses; the threshold size controls how many events are detected.

The proposed multi-threshold DC (MTDC) strategy runs five single-threshold DC (STDC) pipelines in parallel, each of which classifies whether a DC trend also contains an OS event, via an Auto-WEKA-selected classifier, and, if so, estimates the OS event's length with a symbolic-regression genetic program, so as to predict the trend's reversal point. A genetic algorithm then learns a weight for each threshold; the weighted majority vote sets the trading action, buy, sell or hold, and the weighted average of the recommended reversal times sets when to act, with the GA's fitness measured by the resulting strategy's Sharpe ratio.

Tested on 200 monthly datasets built from 10-minute FX data for 20 currency pairs, MTDC produced a higher average return, Sharpe ratio and lower maximum drawdown than each of five individual single-threshold DC strategies, with the differences statistically significant by a Friedman/Hommel test on return, Sharpe ratio and drawdown, though not on return volatility. MTDC also beat buy-and-hold and three technical-analysis indicators, RSI, EMA and MACD, on average return. The paper's contribution is the GA-based weighting scheme itself, since prior single-threshold DC work by the same research group already established the underlying classification-plus-regression reversal forecast.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Raw data are 10-minute-interval physical-time FX snapshots; a directional-change event is confirmed once price has moved by a preset percentage threshold theta from the last confirmed extreme, splitting the series into alternating up and down DC and overshoot segments sampled in intrinsic, price-move time rather than fixed clock time. The prediction target is the trend's reversal point: a classifier first labels whether the current DC trend also has an overshoot event, then a symbolic-regression genetic program estimates the overshoot event's length from the DC event's length, giving a predicted reversal point at the DC-confirmation time plus the estimated overshoot length. The multi-threshold version runs this pipeline for five thresholds drawn from a pool of 100 and uses a genetic algorithm to weight and combine their buy, sell or hold votes and reversal-time forecasts into one trading decision.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** 20 FX currency pairs: AUD/JPY, AUD/NZD, AUD/USD, CAD/JPY, EUR/AUD, EUR/GBP, EUR/CAD, EUR/CSK, EUR/NOK, GBP/AUD, NZD/USD, USD/CAD, USD/NOK, USD/JPY, USD/SGD, USD/ZAR (16 pairs) plus EUR/USD, EUR/JPY, GBP/CHF, GBP/USD (4 pairs)
- **Venue:** OANDA (data purchased from OANDA; not publicly available)
- **Period:** 16 pairs: March 2016 to February 2017; 4 pairs: June 2013 to May 2014
- **Granularity:** 10-minute-interval snapshots of physical-time price data, each resampled into DC and overshoot event series per threshold, with 5 thresholds per dataset drawn from a pool of 100

## Features and Measures

- **DC event.** A confirmed price move of at least threshold theta from the last extreme, marking the start of a new up- or down-trend; it can only be confirmed in hindsight, at the DC confirmation point.
- **OS event (overshoot).** The continuation of price movement in the same direction after a DC event is confirmed, ending when a DC event in the opposite direction is confirmed.
- **DC-event attributes for classification.** DC event price, DC event time, speed, previous DC event price, a previous-OS indicator and a flash-event indicator, used as inputs to an Auto-WEKA classifier that predicts whether a DC trend also contains an OS event.
- **multi-threshold GA weight.** A real-valued weight per DC threshold, evolved by a genetic algorithm to combine each threshold's buy, sell or hold recommendation and predicted reversal point into one trading decision, with fitness measured by the resulting strategy's Sharpe ratio.

## Method

The single-threshold pipeline has three steps: an Auto-WEKA-selected classifier predicts whether a DC trend contains only a DC event or a DC-plus-OS pair; for trends with an OS event, a tree-based symbolic-regression genetic program, tuned with the I/F-Race package, evolves an equation mapping DC event length to OS event length, chosen from a pool of 100 candidate thresholds by lowest root-mean-squared regression error; a trading rule then opens or closes a position with the entire capital at the predicted reversal point when the resulting return, net of a 0.025% transaction cost, would be positive. The multi-threshold strategy runs five single-threshold pipelines in parallel and uses a genetic algorithm, population 500, generation size 50, tournament size 7, crossover probability 0.90, mutation probability 0.10, elitism 0.1, to evolve per-threshold weights; trading decisions follow the weighted-majority action and the weighted-average predicted reversal time. Strategies are compared on a 70:30 train/test split within each monthly dataset, against five single-threshold variants, three technical-analysis indicators (RSI, EMA, MACD) and buy-and-hold, using a non-parametric Friedman test with Hommel post hoc correction.

## Results

- Average monthly return across the 20 currency pairs was 1.1577% for the multi-threshold strategy, over 100% better than the best single-threshold strategy's 0.53% average return, and the multi-threshold strategy had the best return for every individual currency pair.
- A Friedman test with Hommel post hoc correction found the multi-threshold strategy statistically outranked all five single-threshold strategies on return at the 5% significance level.
- The multi-threshold strategy's average Sharpe ratio was 0.78, over 200% better than the best single-threshold strategy's Sharpe ratio, and it outperformed the single-threshold strategies in all 20 currency pairs on this measure.
- The multi-threshold strategy recorded the lowest overall average maximum drawdown (0.02), about 10 times lower on average than the single-threshold strategies, confirmed as statistically significant by the Friedman test.
- The multi-threshold strategy did not statistically outperform the single-threshold strategies on standard deviation of returns, though it ranked first with the lowest average standard deviation (0.1638).
- Against financial benchmarks, the multi-threshold strategy's average return of 1.1577% beat buy-and-hold (-0.128%), RSI (-0.0378%), EMA (0.1117%) and MACD (-0.1879%); its return variance was 0.76 versus 6.91 for buy-and-hold, 0.09 for RSI, 0.14 for EMA and 0.16 for MACD.
- A Friedman test ranked the multi-threshold strategy first, average rank 1.35, against the four financial benchmarks at the 5% significance level; average computation time was about 330 minutes for its classification step and about 7 minutes for GA optimisation, versus about 65 minutes for a single threshold's classification step.

## Limitations

- Tested only on FX data at a 10-minute interval; authors state it is unconfirmed whether performance generalizes to commodities, bonds, indices, stocks or cryptocurrency, or to higher-frequency (1-minute or tick) data.
- Number of thresholds is fixed at five, based on prior tuning experiments, rather than dynamically selected per dataset.
- The multi-threshold strategy's computation time is substantially higher than the single-threshold strategies' (about 330 minutes for classification versus about 65 minutes), which the authors argue is acceptable only because training runs offline before live trading.
- The multi-threshold strategy did not statistically outperform single-threshold strategies on the standard-deviation risk measure.
- Reader note: data was purchased from OANDA and is not publicly available, so results cannot be independently replicated on the same dataset.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/directional-change|Directional Change]]
- [[entities/adesola-adegboye|Adesola Adegboye]]
- [[entities/michael-kampouridis|Michael Kampouridis]]

## Citation

Adesola Adegboye, Michael Kampouridis, Fernando Otero (2023). Algorithmic trading with directional changes. Artificial Intelligence Review.

DOI: 10.1007/s10462-022-10307-0

Text ingested: `markdown_output/adegboye-2022-algorithmic-trading-directional-changes.md`, converted from `raw/ofi-event-clock/adegboye-2022-algorithmic-trading-directional-changes.pdf`.

Coverage of this summary: Read the entire paper: abstract, introduction, DC and OS background, STDC and MTDC methodology and pseudocode, GA description, experimental setup and parameter tables, all results sections including every results table, conclusion, and reference list.

Known problems with the input: The paper's header shows both a journal-issue year of 2023 ("Artificial Intelligence Review (2023) 56:5619-5644") and an online-publication date of 7 November 2022; year is recorded as 2023, the printed journal-issue year, which differs from the job file's year_hint of 2022; PDF-to-markdown conversion rendered pseudocode and several results tables with garbled cell alignment; only the prose descriptions and the numeric results legible in the tables were used.
<!-- AUTHORED REGION END -->