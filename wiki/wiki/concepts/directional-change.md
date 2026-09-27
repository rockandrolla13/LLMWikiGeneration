---
content_hash: sha256:42eb890a6c46aa4ea02b657a2a08ec94147c168d6a137db96c109a83dc29d48e
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/directional-change
page_type: concept
related:
- concepts/intrinsic-time
- concepts/sampling-clocks
- concepts/event-clock
- concepts/stylized-facts
- concepts/backtesting
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
sources:
- sources/abdulkarim-2019-topics-market-microstructure
- sources/adegboye-2017-regression-genetic-programming-estimating-trend-end
- sources/adegboye-2021-improving-trend-reversal-estimation-forex-markets
- sources/adegboye-2021-machine-learning-classification-regression-models-predicting
- sources/adegboye-2022-algorithmic-trading-directional-changes
- sources/alkhamees-2017-directional-change-based-trading-strategy-dynamic
- sources/alkhamees-2019-developing-event-identification-methods-structured-unstructured
- sources/aloud-2016-profitability-directional-change-based-trading-strategies
- sources/aloud-2016-time-series-analysis-indicators-under-directional
- sources/bakhach-2016-forecasting-directional-changes-fx-markets
- sources/bakhach-2018-developing-trading-strategies-under-directional-changes
- sources/chen-2019-studying-regime-change-directional-change
- sources/constantinou-2010-periodicities-fx-markets-intrinsic-time
- sources/george-2025-deep-reinforcement-learning-trading-strategy-development
- sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery
- sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time
- sources/glattfelder-2024-theory-intrinsic-time-primer
- sources/gypteau-2015-generating-directional-change-based-trading-strategies
- sources/long-2025-depth-investigation-genetic-programming-under-physical
- sources/long-2026-multi-objective-genetic-programming-based-algorithmic
- sources/palsma-2019-optimising-directional-changes-trading-strategies-different
- sources/rayment-2023-high-frequency-trading-deep-reinforcement-learning
- sources/salman-2022-trading-strategies-optimization-genetic-algorithm-under
- sources/salman-2023-optimization-trading-strategies-genetic-algorithm-under
- sources/salman-2025-genetic-algorithm-optimization-multi-threshold-trading
- sources/tao-2018-directional-change-information-extraction-financial-market
- sources/tsang-2024-nowcasting-directional-change-high-frequency-fx
- sources/wu-2023-intelligent-trading-strategy-based-improved-directional
- sources/ye-2017-developing-sustainable-trading-strategies-directional-changes
- sources/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time
tags:
- directional-change
- intrinsic-time
- overshoot
- event-based-sampling
- foreign-exchange
title: Directional Change
updated: '2026-09-27T01:47:00Z'
uuid: 161a9d0f-1ca0-52ec-be16-8fe5f4d93f3f
---

<!-- AUTHORED REGION START -->
# Directional Change

Directional change is a way of summarising a price series as a sequence of trend reversals. A threshold is chosen, as a percentage of price. A directional change event is confirmed when the price has moved against the current trend by at least that threshold, measured from the last extreme. The trend then flips.

## The two parts of a trend

Each trend is split in two.

- **The directional change event.** The move from the last extreme to the point where the reversal is confirmed.
- **The overshoot event.** The rest of the move, from the confirmation point to the next extreme.

The overshoot is the part that can be traded, because it begins only once the reversal is known. Much of the literature is about estimating how long or how large the overshoot will be.

## How it is used

- **As a sampling scheme.** It is the main form of [[concepts/intrinsic-time|intrinsic time]].
- **As a source of indicators.** Counts of events, overshoot sizes and the total distance travelled by the price are used to profile a market.
- **As the basis of trading rules.** Strategies open a position at a confirmation point and close it at an estimate of the trend's end. Several thresholds are often combined.

## Caveats

The confirmation point is known only after the price has moved by the threshold, so the extreme itself is never tradeable in real time. Thresholds, and the rules that combine them, are usually tuned on past data, which makes [[concepts/overfitting-backtesting|backtest overfitting]] a standing risk. Most of the evidence is from foreign exchange.

## Sources in This Wiki

- [[sources/abdulkarim-2019-topics-market-microstructure|Topics in Market Microstructure]] (, 2019). A PhD thesis with three studies: an agent-based FTT market simulation, and two LSE order-book studies of an NVWAP trend indicator and order-cancellation effects on price and spread.
- [[sources/adegboye-2017-regression-genetic-programming-estimating-trend-end|Regression genetic programming for estimating trend end in foreign exchange market]] (Adesola Adegboye, Michael Kampouridis, Colin G. Johnson, 2018). Uses genetic programming to learn linear and non-linear equations mapping directional-change event length to overshoot length, then plugs the equations into a directional-change Forex trading strategy.
- [[sources/adegboye-2021-improving-trend-reversal-estimation-forex-markets|Improving Trend Reversal Estimation in Forex Markets Under a Directional Changes Paradigm with Classification Algorithms]] (Adesola Adegboye, Michael Kampouridis, Fernando Otero, 2021). Adds a classifier predicting whether a directional-change event has a following overshoot event, improving overshoot-length estimation and trading returns across 20 forex pairs.
- [[sources/adegboye-2021-machine-learning-classification-regression-models-predicting|Machine Learning Classification and Regression Models for Predicting Directional Changes Trend Reversal in FX Markets]] (Adesola Adegboye, Michael Kampouridis, 2020). Proposes a directional-changes framework that classifies whether a trend reversal will have an overshoot, then uses genetic-programming regression to predict its length, backing a new FX trading strategy.
- [[sources/adegboye-2022-algorithmic-trading-directional-changes|Algorithmic trading with directional changes]] (Adesola Adegboye, Michael Kampouridis, Fernando Otero, 2023). Proposes a genetic-algorithm-weighted combination of five directional-change thresholds for FX trading, showing it statistically outperforms single-threshold directional-change strategies and technical/buy-and-hold benchmarks on 20 currency pairs.
- [[sources/alkhamees-2017-directional-change-based-trading-strategy-dynamic|A Directional Change Based Trading Strategy with Dynamic Thresholds]] (Nora Alkhamees, Maria Fasli, 2017). Proposes a Directional-Change trading strategy with a daily, data-driven threshold instead of a fixed one, and shows it outperforms fixed thresholds and other strategies on FTSE 100 minute data.
- [[sources/alkhamees-2019-developing-event-identification-methods-structured-unstructured|Developing event identification methods for structured and unstructured data streams]] (Nora Alkhamees, 2019). A PhD thesis that replaces the fixed threshold in Directional Change price-event detection and the fixed support value in Twitter topic detection with values recomputed daily, then tests whether the two streams' detected events correlate.
- [[sources/aloud-2016-profitability-directional-change-based-trading-strategies|Profitability of Directional Change Based Trading Strategies: The Case of Saudi Stock Market]] (Monira Essa Aloud, 2016). Tests three directional-change event trading strategies (ZI-DCT0, DCT1, DCT2) on five Saudi stock indices in an agent-based simulation, finding the self-adaptive learning strategy DCT2 earns the highest average return.
- [[sources/aloud-2016-time-series-analysis-indicators-under-directional|Time Series Analysis Indicators under Directional Changes: The Case of Saudi Stock Market]] (Monira Essa Aloud, 2016). Defines time series indicators (NDC, NOS, OSM, TT, PCC) under the directional-change/intrinsic-time framework and profiles them on five Saudi stock indices at 3% and 9% thresholds.
- [[sources/bakhach-2016-forecasting-directional-changes-fx-markets|Forecasting Directional Changes in the FX Markets]] (Amer Bakhach, Edward P. K. Tsang, Hamid Jalalian, 2016). Introduces a single explanatory variable to forecast, under the Directional Change framework, whether an FX trend will extend to a larger price-move threshold before reversing.
- [[sources/bakhach-2018-developing-trading-strategies-under-directional-changes|Developing Trading Strategies under the Directional Changes Framework: With Application in the FX Market]] (Amer Bakhach, 2018). Develops and backtests two contrarian FX trading strategies built on the Directional Changes framework: one using a novel DC-based forecasting indicator, one using automatically tuned overshoot thresholds.
- [[sources/chen-2019-studying-regime-change-directional-change|Studying Regime Change using Directional Change]] (Jun Chen, 2019). PhD thesis using Directional Change (event-based price sampling at peaks and troughs) with a hidden Markov model and naive Bayes to detect, classify, track and trade regime change.
- [[sources/constantinou-2010-periodicities-fx-markets-intrinsic-time|Periodicities of FX Markets in Intrinsic Time]] (Wing Lon Ng, Iacopo Giampaoli, Nick Constantinou, 2010). Applies Lomb-Scargle spectral analysis to FX tick data sampled in event-based 'intrinsic time' to find periodicities in directional-change event series.
- [[sources/george-2025-deep-reinforcement-learning-trading-strategy-development|Deep Reinforcement Learning for Trading Strategy Development on High-Frequency Currency Data Using Directional Changes Sampling]] (George Rayment, 2025). A PhD thesis training deep reinforcement learning trading agents on directional-change-sampled high-frequency FX data, progressing from a filtered agent (FDRL) to positionally-aware (PADRL) to spread-aware (SADRL) frameworks.
- [[sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery|Patterns in high-frequency FX data: Discovery of 12 empirical scaling laws]] (J.B. Glattfelder, A. Dupuis, R.B. Olsen, 2010). Reports twelve new empirical scaling laws linking price-move size, tick counts, and waiting times in five years of tick data across 13 FX pairs, using an event-based directional-change framework.
- [[sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time|Bridging the Gap: Decoding the Intrinsic Nature of Time in Market Data]] (James B. Glattfelder, Anton Golub, 2022). Derives an analytic bridge between physical-time and intrinsic (directional-change) time statistics, decomposing squared returns into a directional-change-count term and an overshoot-variability term, tested on Brownian motion and two currency series.
- [[sources/glattfelder-2024-theory-intrinsic-time-primer|The Theory of Intrinsic Time: A Primer]] (James B. Glattfelder, Richard B. Olsen, 2024). A conceptual primer explaining intrinsic time, an event-based directional-change measure of market time, and the scaling laws and liquidity/volatility decomposition it reveals in financial data.
- [[sources/gypteau-2015-generating-directional-change-based-trading-strategies|Generating Directional Change Based Trading Strategies with Genetic Programming]] (Jeremie Gypteau, Fernando E. B. Otero, Michael Kampouridis, 2015). Genetic programming combines multiple Directional Change price thresholds into trading strategies, tested on daily closing prices from two stocks and two indices.
- [[sources/long-2025-depth-investigation-genetic-programming-under-physical|An In-Depth Investigation of Genetic Programming Under Physical Time and Directional Change Frameworks for Algorithmic Trading]] (Xinpeng Long, Michael Kampouridis, Panagiotis Kanellopoulos, 2025). Introduces two genetic programming trading algorithms, GP-DC and GP-DC-PT, that use directional-change event indicators alongside or instead of physical-time technical indicators, testing them on 220 international stock datasets.
- [[sources/long-2026-multi-objective-genetic-programming-based-algorithmic|Multi-objective genetic programming-based algorithmic trading, using directional changes and a modified sharpe ratio score for identifying optimal trading strategies]] (Xinpeng Long, Michael Kampouridis, Tasos Papastylianou, 2026). Combines directional-change price events, genetic programming, and NSGA-II multi-objective optimisation to evolve trading rules balancing return and risk, then picks one via a modified Sharpe ratio.
- [[sources/palsma-2019-optimising-directional-changes-trading-strategies-different|Optimising Directional Changes trading strategies with different algorithms]] (Jurgen Palsma, Adesola Adegboye, 2019). Compares particle swarm optimisation and a shuffled frog leaping algorithm against a genetic algorithm for tuning multi-threshold directional-change FX trading strategies.
- [[sources/rayment-2023-high-frequency-trading-deep-reinforcement-learning|High Frequency Trading with Deep Reinforcement Learning Agents Under a Directional Changes Sampling Framework]] (George Rayment, Michael Kampouridis, 2023). Trains PPO deep reinforcement learning trading agents on FX tick data sampled with directional changes, and shows they beat buy-and-hold, moving-average, RSI and rule-based benchmarks on return and risk-adjusted return.
- [[sources/salman-2022-trading-strategies-optimization-genetic-algorithm-under|Trading Strategies Optimization by Genetic Algorithm under the Directional Changes Paradigm]] (Ozgur Salman, Michael Kampouridis, Delaram Jarchi, 2022). Builds four new indicator-based directional-changes trading strategies, combines them with three existing ones via a genetic algorithm, and tests all on 44 NYSE stocks against a buy-and-sell benchmark.
- [[sources/salman-2023-optimization-trading-strategies-genetic-algorithm-under|Optimization of Trading Strategies Using a Genetic Algorithm under the Directional Changes Paradigm with Multiple Thresholds]] (Ozgur Salman, Themistoklis Melissourgos, Michael Kampouridis, 2023). Runs ten Directional Change thresholds in parallel for three new trading strategies and uses a genetic algorithm to weight and combine their signals, beating single-threshold strategies and RSI, MACD and buy-and-hold benchmarks on 18 NYSE stocks.
- [[sources/salman-2025-genetic-algorithm-optimization-multi-threshold-trading|A genetic algorithm for the optimization of multi-threshold trading strategies in the directional changes paradigm]] (Ozgur Salman, Themistoklis Melissourgos, Michael Kampouridis, 2025). A genetic algorithm weights eight directional-changes strategies across ten thresholds and beats individual DC strategies, technical indicators, buy-and-hold and market indices on 200 NYSE stocks.
- [[sources/tao-2018-directional-change-information-extraction-financial-market|Using Directional Change for Information Extraction in Financial Market Data]] (Ran Tao, 2018). Introduces directional-change (DC) event-based sampling of price series and defines DC indicators and metrics to profile and compare financial markets as a complement to time series analysis.
- [[sources/tsang-2024-nowcasting-directional-change-high-frequency-fx|Nowcasting directional change in high frequency FX markets]] (Edward P. K. Tsang, Shuai Ma, V. L. Raju Chinthalapati, 2024). Proposes a simple, historical-distribution-based rule to nowcast directional changes in FX tick data before they are formally confirmed, and tests it on three currency pairs.
- [[sources/wu-2023-intelligent-trading-strategy-based-improved-directional|Intelligent trading strategy based on improved directional change and regime change detection]] (Bing Wu, Xiangzu Han, 2023). Adds a decay-coefficient threshold and Bayesian-optimized hyperparameters to the Directional Change framework, filters trades with a hidden Markov regime detector, and shows the combination raises forex trading returns and cuts drawdowns.
- [[sources/ye-2017-developing-sustainable-trading-strategies-directional-changes|Developing Sustainable Trading Strategies Using Directional Changes with High Frequency Data]] (Ailun Ye, V L Raju Chinthalapati, Antoaneta Serguieva and others, 2017). Proposes and backtests four directional-change-based FX trading strategies, alone and combined with the DMI technical indicator, on EUR/USD and GBP/USD tick data across ten thresholds.
- [[sources/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time|Novel Trading Algorithms augmented by Intrinsic Time and Machine Learning]] (Qi Zhao, 2026). PhD thesis using the Directional Change intrinsic-time framework to build FX trading strategies, then layering machine-learning overshoot prediction and a ResNet-policy RL agent on top.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/event-clock|Event Clock]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
<!-- AUTHORED REGION END -->