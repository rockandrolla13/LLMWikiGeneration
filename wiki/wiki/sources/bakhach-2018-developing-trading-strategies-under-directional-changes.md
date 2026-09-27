---
authors:
- Amer Bakhach
content_hash: sha256:08e653682daa21553bea32c44d17e7f2664bd3856518e8819d87b09dd479ebc3
created: 2026-09-27 01:47:00+00:00
page_id: sources/bakhach-2018-developing-trading-strategies-under-directional-changes
page_type: source
publication_venue: University of Essex
related:
- concepts/intrinsic-time
- concepts/backtesting
- concepts/bid-ask-spread
- concepts/feature-engineering
- concepts/overfitting-backtesting
- concepts/stylized-facts
- concepts/alpha-signal
- concepts/directional-change
revision_id: 1
schema_version: 2
source_hash: sha256:39471703ce830b5c2a50c3ab1cc14c6aca996276a72542745b94b4a729913698
source_path: markdown_output/bakhach-2018-developing-trading-strategies-under-directional-changes.md
source_type: paper
tags:
- fx
- directional-changes
- contrarian-trading
- trading-strategy
- forecasting
- backtesting
- rolling-window
- event-based-sampling
- clock-intrinsic
- asset-fx
- harvest-relevant
title: 'Developing Trading Strategies under the Directional Changes Framework: With
  Application in the FX Market'
updated: '2026-09-27T01:47:00Z'
uuid: d686ccc3-02b6-59db-879e-002b84d07ed3
year: 2018
---

<!-- AUTHORED REGION START -->
# Developing Trading Strategies under the Directional Changes Framework: With Application in the FX Market

## Summary

The thesis asks whether the Directional Changes (DC) framework, an event-based way of summarizing a price series into alternating up- and down-trends separated by a fixed percentage threshold, can be turned into a genuinely profitable FX trading strategy. Prior work had argued that an idealized DC strategy with perfect foresight could be extremely profitable, but that this promise remained unexploited in practice.

The thesis develops two DC-based strategies and backtests both on eight currency pairs sampled minute-by-minute, using a monthly rolling-window methodology. The first, TSFDC, rests on a forecasting problem formulated specifically for the DC framework: tracking two simultaneous DC thresholds (a small STheta and a larger BTheta) and predicting a boolean variable, built from the thesis's new 'Big-Theta' concept, that indicates whether the current small DC trend will extend far enough to also trigger a DC event at the larger threshold. The prediction uses a novel indicator, an overshoot-value ratio computed with reference to both thresholds, fed into a J48 decision tree; the trading rule buys or sells on this forecast or on the subsequent confirmed DC event. The second strategy, the Backlash Agent (BA), makes no forecast: it opens a countertrend position once a normalized overshoot value crosses a threshold, and its dynamic version (DBA) re-estimates that threshold every rolling window by grid-searching past training-period returns.

Backtested with real bid and ask prices (but no transaction costs) over a seven-month out-of-sample period, both strategies were mostly profitable and both produced Sharpe ratios statistically different from a buy-and-hold benchmark. Averaged across the eight currency pairs, TSFDC produced higher returns while DBA had shallower drawdowns and a comparable or better average Sharpe ratio, so the thesis concludes that neither dominates the other; the choice depends on the trader's risk tolerance. Both strategies were also compared against previously published DC-based trading strategies and outperformed them on the reported profitability and risk-adjusted metrics.

What is new is the formalization of 'will this DC trend keep extending to a larger threshold' as a forecasting problem native to the DC framework (rather than ordinary next-value or fixed-interval prediction), the accompanying overshoot-value indicator, and a controlled head-to-head comparison of a forecasting-based versus a non-forecasting DC trading strategy under one identical backtest methodology.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

The Directional Changes (DC) framework replaces fixed-interval sampling with event-based, price-move-defined time: the market is modeled as alternating uptrends and downtrends, and a new trend is confirmed only once price has moved by a fixed percentage threshold theta from the most recent extreme point (the 'DC confirmation point'). Both trading strategies act at these DC confirmation points or during the following overshoot rather than at fixed calendar times. TSFDC's forecasting target is defined over two simultaneous thresholds: at the confirmation point of a DC event under the smaller threshold STheta, the model predicts whether that same trend will later also confirm a DC event under a larger threshold BTheta before it reverses; the Backlash Agent instead reacts once a normalized overshoot measure crosses a fixed cutoff.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** Eight FX currency pairs: EUR/CHF, GBP/CHF, EUR/USD, GBP/AUD, GBP/JPY, NZD/JPY, AUD/JPY, EUR/NZD
- **Venue:** Over-the-counter FX market; minute-by-minute bid, ask and mid-price data obtained from the data provider kibot.com
- **Period:** 1/1/2013 to 31/7/2015 (31 months) used to build/train the DC summaries and forecasting model; out-of-sample trading backtest from 1/1/2015 to 31/7/2015 (7 months) via seven rolling windows of 24 months' training plus 1 month applied; a separate 12-month period, 1/8/2014 to 31/7/2015, is used in one Backlash Agent parameter-sensitivity experiment
- **Granularity:** Minute-by-minute mid-prices for constructing DC summaries and the forecasting dataset; instantaneous actual bid and ask prices used for every simulated trade

## Features and Measures

- **Directional Change (DC) event and threshold theta.** A price move of at least a percentage threshold theta from the most recent extreme point, used to split a price series into alternating DC events (the fixed-size confirming move) and overshoot (OS) events (the remaining, unbounded part of the trend).
- **Big-Theta / BBTheta.** A boolean variable attached to each DC event observed under a smaller threshold STheta, equal to True if the same trend's total price change also reaches a larger threshold BTheta before it reverses; this is the variable the thesis's forecasting model is built to predict.
- **OSVBTheta_STheta indicator.** A DC-based independent variable computed from the price at the extreme point of a STheta-threshold DC event together with the price needed to confirm the most recent BTheta-threshold event; it is the single input fed to a J48 decision tree that forecasts BBTheta.
- **Overshoot Value (OSV).** A normalized measure of how far the current price has moved past the DC confirmation point of the active trend, expressed relative to the DC threshold theta, used by the Backlash Agent to decide when to open a countertrend position.
- **down_ind / up_ind trading thresholds.** Overshoot-value cutoffs used by the Backlash Agent's buy and sell rules; in the dynamic version (DBA) these are re-estimated every rolling window by testing 100 candidate values against the preceding training-period returns and keeping the best-performing one.

## Method

TSFDC's forecasting stage trains a J48 (C4.5) decision tree, using OSVBTheta_STheta as the sole independent variable, to classify BBTheta as True or False, fitted separately for uptrends and downtrends of each currency pair on a training window and evaluated out of sample; its accuracy is benchmarked against an ARIMA model fitted to the same True/False sequence. The trading stage (TSFDC-down and TSFDC-up, run and evaluated independently) opens a contrarian position when the forecast, or a subsequently confirmed BTheta-threshold event, signals that a trend will or will not extend, and closes at the next opposite-direction DC confirmation; all simulated trades use real bid or ask prices with no transaction-cost deduction.

The Backlash Agent has a static form (SBA), in which the user fixes an overshoot-value threshold (down_ind or up_ind) for opening a countertrend position and exits at the next DC confirmation in the other direction, and a dynamic form (DBA), in which that threshold is instead chosen automatically each period by testing 100 candidate values (stepped by 0.01) against the preceding 24-month training window and selecting whichever produced the highest training-period return.

Both strategies are evaluated with an identical monthly rolling-window backtest (24 months training, 1 month out-of-sample, seven such windows spanning 1/1/2015 to 31/7/2015) across the same eight currency pairs, using rate of return, profit factor, maximum drawdown, win ratio, Sharpe ratio, Sortino ratio, and Jensen's Alpha/Beta against a buy-and-hold benchmark. Wilcoxon rank-sum tests are used to check whether differences in Sharpe ratio or win ratio, versus the benchmark or between strategy variants, are statistically significant.

## Results

- The forecasting model (OSVBTheta_STheta indicator plus a J48 decision tree) reached out-of-sample accuracy between 0.62 and 0.82 across the eight currency pairs and outperformed ARIMA in every tested case.
- TSFDC, trading on this forecasting model, produced total seven-month out-of-sample returns as high as 41.87% (TSFDC-down) and 41.22% (TSFDC-up) on EUR/NZD, with maximum drawdowns as deep as -21.1% on some pairs.
- DBA, which uses no forecasting model, produced total seven-month returns as high as 28.41% (DBA-down) and 32.81% (DBA-up) on EUR/NZD, with maximum drawdowns no worse than about -3.1% to -3.2% on that pair.
- Averaged over the eight currency pairs, TSFDC earned higher rates of return (13.22% and 11.77% for the down/up versions) than DBA (9.58% and 11.25%), but DBA had shallower average drawdowns (-7.1% and -7.4%) than TSFDC (-9.7% and -9.9%), and DBA's average Sharpe ratios (1.97 and 1.55) were similar to or better than TSFDC's (1.20 and 1.93).
- Wilcoxon rank-sum tests found both TSFDC's and DBA's Sharpe ratios statistically different from the buy-and-hold benchmark's Sharpe ratio at the 5% level, in both cases favoring the DC-based strategy.
- DBA-down's Sharpe ratio on individual pairs (3.46 on NZD/JPY, 3.18 on EUR/NZD) exceeded the 3.06 annual Sharpe ratio reported in prior work for the 'Alpha Engine' DC-based strategy, and DBA's EUR/NZD return of more than 28% in seven months exceeded Alpha Engine's reported 21.34% return over eight years.
- A previously published GP-tree DC-based strategy (Gypteau et al.) returned less than 10% over 500 trading days on stock and index data, and a previously published strategy called DCT1 returned 6.2% over one year on EUR/USD, both well below the returns reported here for TSFDC and DBA.
- Neither TSFDC nor DBA approaches the theoretical maximum annual return of 1600% estimated elsewhere in the literature for a DC-based strategy with perfect foresight.

## Limitations

- Transaction costs and slippage are excluded from every backtest; only the bid-ask spread is deducted, which matches the practice of the other DC-based strategies compared against but likely overstates realizable profit.
- The DC thresholds used in each experiment (theta, STheta, BTheta) are chosen arbitrarily rather than optimized or validated out of sample.
- Money management is a simple all-in approach that commits the entire trading capital to every signal; the author states this is naive and flags it for future work.
- Performance varies substantially across the eight currency pairs tested, and the out-of-sample trading window covers a single seven-month period (January-July 2015).
- Reader note: with one out-of-sample evaluation window per currency pair, and thresholds and rolling-window lengths set by hand rather than tuned, the reported returns carry meaningful risk of being specific to this sample rather than robust across market regimes.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/backtesting|backtesting]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/directional-change|Directional Change]]

## Citation

Amer Bakhach (2018). Developing Trading Strategies under the Directional Changes Framework: With Application in the FX Market. University of Essex.

Text ingested: `markdown_output/bakhach-2018-developing-trading-strategies-under-directional-changes.md`, converted from `raw/ofi-event-clock/bakhach-2018-developing-trading-strategies-under-directional-changes.pdf`.

Coverage of this summary: Read the abstract, glossary, introduction (Chapter 1), the Directional Changes framework chapter (Chapter 4), the forecasting-problem formulation and results chapter (Chapter 5), both trading-strategy chapters with their full experiments and results (Chapter 6, TSFDC; Chapter 7, Backlash Agent/DBA), the TSFDC-vs-DBA comparison (Chapter 8), and the conclusions/contributions/future-work chapter (Chapter 9). The FX-market background (Chapter 2), the general trading-strategy literature review (Chapter 3), and the appendices (R code, Big-Theta proof, extra result tables) were not read in detail, consistent with the guidance for long documents.

Known problems with the input: Equations throughout the document are replaced by the converter with placeholder text ('picture... intentionally omitted'), so exact formulas (e.g. for OSV, RR, MDD, Sharpe ratio) could not be verified beyond the surrounding prose; Several converted tables have jumbled cell/column alignment (e.g. the interest-rate and MAR/risk-free-rate tables in Chapters 6 and 7), and one average-MDD figure in the Chapter 8 comparison table is printed without its minus sign ('9.9' where the other three cells are negative); figures used here were cross-checked against the surrounding text discussion where possible.
<!-- AUTHORED REGION END -->