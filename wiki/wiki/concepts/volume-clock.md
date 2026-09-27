---
content_hash: sha256:3bb78aec6c81a4d30144bc2fc6cfee18115b6246a870fc49655ec4843138d58d
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/volume-clock
page_type: concept
related:
- concepts/sampling-clocks
- concepts/trade-clock
- concepts/event-clock
- concepts/vpin
- concepts/bulk-volume-classification
- concepts/stochastic-time-change
- concepts/informed-trading
revision_id: 1
schema_version: 2
sources:
- sources/andersen-2013-assessing-measures-order-flow-toxicity-early
- sources/bambade-2019-assessment-prediction-quality-vpin
- sources/bambade-2019-new-way-compute-probability-informed-trading
- sources/bechler-2017-order-flows-limit-order-book-resiliency
- sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability
- sources/chang-2021-epps-effect-under-alternative-sampling-schemes
- sources/fang-2019-design-high-frequency-trading-algorithm-based
- sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility
- sources/gillemot-2006-there-s-more-volatility-than-volume
- sources/he-2016-volume-synchronised-probability-informed-trading-chinese
- sources/hellermann-2026-event-based-limit-order-book-representations
- sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
- sources/jonuzaj-2024-information-content-book-trade-order-flow
- sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
- sources/karyampas-2011-probability-informed-trading-volatility-etf
- sources/lee-2017-informed-trading-futures-markets-during-financial
- sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych
- sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability
- sources/wu-2013-big-data-approach-analyzing-market-volatility
- sources/yamagishi-2026-run-one-rule-five-clocks-only
- sources/yamagishi-2026-volume-bar-foreign-exchange-identically-tick
tags:
- volume-time
- volume-bars
- sampling
- high-frequency-trading
- market-microstructure
title: Volume Clock
updated: '2026-09-27T01:47:00Z'
uuid: 0695eae8-4c79-5dbe-b8ad-6c59eb130c63
---

<!-- AUTHORED REGION START -->
# Volume Clock

A volume clock advances each time a fixed amount of trading volume has changed hands. Each observation, often called a volume bar or volume bucket, holds roughly the same traded quantity and a varying span of time. Dollar bars are the same idea with traded value in place of traded quantity.

## How it is used

- **To build bars.** Prices and features are recorded at the close of each volume bucket.
- **To measure imbalance.** Buy and sell volume are compared within each bucket. This is the basis of [[concepts/vpin|VPIN]].
- **To normalise across assets and across the day.** A bucket of fixed volume arrives quickly at the open and close and slowly at midday, so the usual intraday pattern in activity is absorbed by the clock.

## Relation to other clocks

Compared with the [[concepts/trade-clock|trade clock]], the volume clock weights each trade by its size. Compared with the wall clock, it puts more observations where more trading happens. It is one of the [[concepts/sampling-clocks|sampling clocks]] most often tested against calendar time.

## Caveats

The bucket size is a free choice and results can depend on it. A trade larger than the bucket has to be split across buckets or assigned to one, and the rule chosen affects the imbalance measured. In markets where volume is reported late or in capped sizes, the clock inherits those reporting rules.

## Sources in This Wiki

- [[sources/andersen-2013-assessing-measures-order-flow-toxicity-early|Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market Turbulence]] (Torben G. Andersen, Oleg Bondarenko, 2014). Tests whether the VPIN order-flow-toxicity metric predicts volatility, using CME best-bid-offer data for E-mini S&P 500 futures to build a near-exact trade-classification benchmark.
- [[sources/bambade-2019-assessment-prediction-quality-vpin|An Assessment of the Prediction Quality of VPIN]] (Antoine Bambade, Kesheng Wu, 2019). Builds a precision/recall framework to test whether VPIN predicts flash crashes in five liquid futures, benchmarks it against a naive classifier, and checks sensitivity to the data set's starting point.
- [[sources/bambade-2019-new-way-compute-probability-informed-trading|A New Way to Compute the Probability of Informed Trading]] (Antoine Bambade, 2019). Re-derives the Probability of Informed Trading (PIN) exactly in its original time-clock framework, shows why VPIN's volume-clock approximation is theoretically flawed, and proposes a new exact PIN estimator.
- [[sources/bechler-2017-order-flows-limit-order-book-resiliency|Order Flows and Limit Order Book Resiliency on the Meso-Scale]] (Kyle Bechler, Mike Ludkovski, 2017). Uses volume-bucketed Nasdaq order book data to show combining market and limit order flow linearizes price impact and reveals scarce-liquidity regimes on the minute-scale.
- [[sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability|Microstructural changes before Macroeconomic Announcements: Predictability of Economic Surprises in the U.S. market]] (Rita Dias Barreto Calçada, 2015). Tests whether pre-announcement order and depth imbalances (VPIN, DI) in S&P 500 and 10-year Treasury futures predict the sign of U.S. macroeconomic surprises.
- [[sources/chang-2021-epps-effect-under-alternative-sampling-schemes|The Epps effect under alternative sampling schemes]] (Patrick Chang, Etienne Pienaar, Tim Gebbie, 2021). Compares the Epps correlation-decay effect under calendar, event (trade) and volume time using a Hawkes-process simulation and JSE equity data, finding it emerges linearly under volume time.
- [[sources/fang-2019-design-high-frequency-trading-algorithm-based|Design of High-Frequency Trading Algorithm Based on Machine Learning]] (Boyue Fang, Yutong Feng, 2019). Combines VPIN informed-trading signals, GARCH volatility forecasts, and an SVM filter into a high-frequency market-making strategy, backtested on CSI300 index futures.
- [[sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility|Informed trading, investor beliefs consensus and volatility: Evidence from the Limit Order Book dynamics during COVID-19 and short-selling ban]] (Sandra Ferreruela, Daniel Martín, 2025). Compares VPIN (executed order-flow toxicity) against the slope of the limit order book (belief consensus) as predictors of short-horizon volatility for 32 IBEX-35 stocks in 2019-2020.
- [[sources/gillemot-2006-there-s-more-volatility-than-volume|There’s more to volatility than volume]] (László Gillemot, J. Doyne Farmer, Fabrizio Lillo, 2006). Empirical study showing that neither trade count nor volume, but the order and size of individual price changes, drives clustered volatility and heavy tails in NYSE and LSE stock returns.
- [[sources/he-2016-volume-synchronised-probability-informed-trading-chinese|Volume-Synchronised Probability of Informed Trading on Chinese Index Futures: A Comparative Approach]] (Zhongzhi (Lawrence) He, Jinzhi Jiang, Martin Kusy and others, 2016). Compares three trade-classification-based VPIN metrics (tick rule, Lee-Ready, bulk volume) on Chinese index futures data to see which best warns of two 2013 volatility events.
- [[sources/hellermann-2026-event-based-limit-order-book-representations|Event-Based Limit Order Book Representations for Probabilistic VWAP Forecasting in Intraday Electricity Markets]] (Justin Hellermann, Stefan Lessmann, 2026). Compares time, tick, volume, and traded-value order-book bar construction for probabilistic VWAP forecasting in UK intraday electricity trading.
- [[sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin|Volume-Synchronized Probability of Informed Trading (VPIN), Market Volatility, and High-Frequency Liquidity]] (Jinzhi Jiang, 2015). Compares three ways of computing VPIN on two volatile episodes in Chinese stock index futures and tests a two-way feedback loop between VPIN and high-frequency liquidity.
- [[sources/jonuzaj-2024-information-content-book-trade-order-flow|Information Content of Book and Trade Order Flow at Different Trading Volume Time Scales]] (Mariol Jonuzaj, Alessio Sancetta, Yuri Taranenko, 2024). Trains machine-learning classifiers on volume-time-aggregated NASDAQ book and trade order flow across many stocks, finding trade order flow predicts mid-price direction more persistently than book order flow.
- [[sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact|Flow Toxicity of High Frequency Trading and Its Impact on Price Volatility: Evidence from the KOSPI 200 Futures Market]] (Jangkoo Kang, Kyung Yoon Kwon, Wooyeon Kim, 2019). Shows that a bulk-volume-classified VPIN measure predicts short-term volatility in KOSPI 200 futures, and that high-frequency traders cut flow toxicity in normal times but add to it in stressful times.
- [[sources/karyampas-2011-probability-informed-trading-volatility-etf|Probability of Informed Trading and Volatility for an ETF]] (Dimitrios Karyampas, Paola Paiardini, 2011). Estimates VPIN, a volume-bucketed measure of informed trading, for the SPY ETF and links it to jump-robust realized volatility through a HAR-RV model.
- [[sources/lee-2017-informed-trading-futures-markets-during-financial|Informed Trading of Futures Markets During the Financial Crisis: Evidence from the VPIN]] (Yen-Hsien Lee, Wen-Chien Liu, Chia-Lin Hsieh, 2017). Tests whether VPIN-measured informed trading affects Taiwan futures returns during the 2008-2009 crisis, separately for domestic and foreign institutional investors and interacted with day-of-week effects.
- [[sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych|Ekonometryczna analiza prawdopodobieństwa zawarcia transakcji wynikających z napływu informacji – wpływ założeń co do rozkładu stóp zwrotu na zmienność miary VPIN]] (Marcin Niedużak, Mateusz Pipień, 2014). Tests how three assumed return distributions in the Bulk Volume Classification algorithm change estimated VPIN for a Warsaw-listed stock (KGHM).
- [[sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability|Parameter Analysis of the VPIN (Volume synchronized Probability of Informed Trading) Metric]] (Jung Heon Song, Kesheng Wu, Horst D. Simon, 2014). Uses the NOMAD optimizer and UQTK sensitivity analysis to search VPIN's free-parameter space and cut its false positive rate across a large futures panel.
- [[sources/wu-2013-big-data-approach-analyzing-market-volatility|A Big Data Approach to Analyzing Market Volatility]] (Kesheng Wu, E. Wes Bethel, Ming Gu and others, 2013). Applies HPC data-management techniques to compute VPIN and a fast Maximum Intermediate Return measure across 16,000 parameter combinations on 3 billion futures trades, confirming VPIN predicts liquidity-driven volatility.
- [[sources/yamagishi-2026-run-one-rule-five-clocks-only|Run One Rule on Five Clocks and Only the Direction and the Cost Agree [F055]: The direction stays below a cost of  to  pips on all five and the cost differs by only  times, yet the count differs by  times and the duration of a bar by  times]] (Yuuki Yamagishi, 2026). Runs one fixed entry/exit trading rule across five bar-sampling clocks (minute, hour, tick, volume, range) on FX and gold data, and reports which measured quantities agree or disagree across clock choice.
- [[sources/yamagishi-2026-volume-bar-foreign-exchange-identically-tick|為替の「出来⾼⾜」は、ティック⾜と恒等的に同じものである [F053]]] (⼭岸 勇輝（Yuuki YAMAGISHI）, 2026). Shows that FX 'volume bars' are definitionally identical to tick bars (agreement ), while range bars built on price-path length are a genuinely different, though still not net-move-invariant, clock.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/event-clock|Event Clock]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/informed-trading|informed trading]]
<!-- AUTHORED REGION END -->