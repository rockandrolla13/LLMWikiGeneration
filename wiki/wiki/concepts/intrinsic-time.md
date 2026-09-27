---
content_hash: sha256:f082c7c95ce3d70c48f2e39d8c20577763dca79342822b28fafd0e1e6f3b1596
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/intrinsic-time
page_type: concept
related:
- concepts/sampling-clocks
- concepts/directional-change
- concepts/event-clock
- concepts/trade-clock
- concepts/volume-clock
- concepts/stylized-facts
revision_id: 1
schema_version: 2
sources:
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
- sources/busetto-2023-continuous-time-modeling-financial-returns-based
- sources/chen-2019-studying-regime-change-directional-change
- sources/constantinou-2010-periodicities-fx-markets-intrinsic-time
- sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time
- sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery
- sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time
- sources/glattfelder-2024-theory-intrinsic-time-primer
- sources/gypteau-2015-generating-directional-change-based-trading-strategies
- sources/palsma-2019-optimising-directional-changes-trading-strategies-different
- sources/rayment-2023-high-frequency-trading-deep-reinforcement-learning
- sources/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed
- sources/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency
- sources/salman-2022-trading-strategies-optimization-genetic-algorithm-under
- sources/salman-2023-optimization-trading-strategies-genetic-algorithm-under
- sources/salman-2025-genetic-algorithm-optimization-multi-threshold-trading
- sources/sjogren-2021-general-compound-hawkes-processes-mid-price
- sources/spears-2020-investment-sizing-deep-learning-prediction-uncertainties
- sources/tao-2018-directional-change-information-extraction-financial-market
- sources/tsang-2024-nowcasting-directional-change-high-frequency-fx
- sources/wu-2023-intelligent-trading-strategy-based-improved-directional
- sources/ye-2017-developing-sustainable-trading-strategies-directional-changes
- sources/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time
tags:
- intrinsic-time
- event-based-sampling
- price-moves
- sampling
- foreign-exchange
title: Intrinsic Time
updated: '2026-09-27T01:47:00Z'
uuid: 2209d597-635c-58ca-9386-bc908474a317
---

<!-- AUTHORED REGION START -->
# Intrinsic Time

Intrinsic time is a clock driven by price. It advances only when the price has moved by a set amount, and stands still otherwise. A quiet hour may produce no observations and a volatile minute may produce several.

## How it is used

- **To sample prices.** A new observation is recorded each time the price moves by a chosen threshold from a reference point.
- **To define a prediction target.** The target is the direction of the next price move of a given size, not the return over a fixed interval.
- **To study scaling.** Counting how many events occur at different thresholds reveals regularities in how price moves of different sizes relate to each other.

## Relation to directional change

[[concepts/directional-change|Directional change]] is the most developed form of intrinsic time. It splits each price trend into a reversal of the threshold size and the move that follows it.

## Relation to other clocks

The [[concepts/event-clock|event]], [[concepts/trade-clock|trade]] and [[concepts/volume-clock|volume]] clocks count activity. Intrinsic time counts outcomes. Two periods with the same trading volume can differ widely in intrinsic time if one of them moved the price and the other did not.

## Caveats

The threshold is a free choice, and a strategy tuned to one threshold may not hold at another. Because the clock is defined by the price path, an observation is only known to have occurred after the price has already moved by the threshold. Any test has to respect that delay, or it will use information that was not available at the time.

## Sources in This Wiki

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
- [[sources/busetto-2023-continuous-time-modeling-financial-returns-based|Continuous-time modeling of financial returns based on Limit Order Book data]] (Riccardo Busetto, Simone Formentin, 2023). Proposes a new order-book imbalance regressor, Base Imbalance, and fits a continuous-time dynamical model on irregularly-spaced, price-change-triggered observations to predict short-term equity returns.
- [[sources/chen-2019-studying-regime-change-directional-change|Studying Regime Change using Directional Change]] (Jun Chen, 2019). PhD thesis using Directional Change (event-based price sampling at peaks and troughs) with a hidden Markov model and naive Bayes to detect, classify, track and trade regime change.
- [[sources/constantinou-2010-periodicities-fx-markets-intrinsic-time|Periodicities of FX Markets in Intrinsic Time]] (Wing Lon Ng, Iacopo Giampaoli, Nick Constantinou, 2010). Applies Lomb-Scargle spectral analysis to FX tick data sampled in event-based 'intrinsic time' to find periodicities in directional-change event series.
- [[sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time|Efficient Sampling for Realized Variance Estimation in Time-Changed Diffusion Models]] (Timo Dimitriadis, Roxana Halbleib, Jeannine Polivka and others, 2025). Derives finite-sample efficiency theory for realized variance under intrinsic-time sampling schemes and shows empirically that hitting-time and a new realized business-time scheme beat calendar-time sampling.
- [[sources/glattfelder-2010-patterns-high-frequency-fx-data-discovery|Patterns in high-frequency FX data: Discovery of 12 empirical scaling laws]] (J.B. Glattfelder, A. Dupuis, R.B. Olsen, 2010). Reports twelve new empirical scaling laws linking price-move size, tick counts, and waiting times in five years of tick data across 13 FX pairs, using an event-based directional-change framework.
- [[sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time|Bridging the Gap: Decoding the Intrinsic Nature of Time in Market Data]] (James B. Glattfelder, Anton Golub, 2022). Derives an analytic bridge between physical-time and intrinsic (directional-change) time statistics, decomposing squared returns into a directional-change-count term and an overshoot-variability term, tested on Brownian motion and two currency series.
- [[sources/glattfelder-2024-theory-intrinsic-time-primer|The Theory of Intrinsic Time: A Primer]] (James B. Glattfelder, Richard B. Olsen, 2024). A conceptual primer explaining intrinsic time, an event-based directional-change measure of market time, and the scaling laws and liquidity/volatility decomposition it reveals in financial data.
- [[sources/gypteau-2015-generating-directional-change-based-trading-strategies|Generating Directional Change Based Trading Strategies with Genetic Programming]] (Jeremie Gypteau, Fernando E. B. Otero, Michael Kampouridis, 2015). Genetic programming combines multiple Directional Change price thresholds into trading strategies, tested on daily closing prices from two stocks and two indices.
- [[sources/palsma-2019-optimising-directional-changes-trading-strategies-different|Optimising Directional Changes trading strategies with different algorithms]] (Jurgen Palsma, Adesola Adegboye, 2019). Compares particle swarm optimisation and a shuffled frog leaping algorithm against a genetic algorithm for tuning multi-threshold directional-change FX trading strategies.
- [[sources/rayment-2023-high-frequency-trading-deep-reinforcement-learning|High Frequency Trading with Deep Reinforcement Learning Agents Under a Directional Changes Sampling Framework]] (George Rayment, Michael Kampouridis, 2023). Trains PPO deep reinforcement learning trading agents on FX tick data sampled with directional changes, and shows they beat buy-and-hold, moving-average, RSI and rule-based benchmarks on return and risk-adjusted return.
- [[sources/rosenbaum-2010-asymptotic-results-statistical-procedures-time-changed|Asymptotic results and statistical procedures for time-changed Lévy processes sampled at hitting times]] (Mathieu Rosenbaum, Peter Tankov, 2010). Proves that a Lévy process, rescaled and observed at first hitting times of a shrinking symmetric barrier, converges to a stable process, yielding consistent estimators of the time change and the Blumenthal-Getoor jump index.
- [[sources/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency|Extending Deep Reinforcement Learning Frameworks in Cryptocurrency Market Making]] (Jonathan Sadighian, 2020). Extends a deep reinforcement learning market-making framework by testing seven reward functions and introducing a price-based event environment, comparing it against a time-based one on Bitcoin data.
- [[sources/salman-2022-trading-strategies-optimization-genetic-algorithm-under|Trading Strategies Optimization by Genetic Algorithm under the Directional Changes Paradigm]] (Ozgur Salman, Michael Kampouridis, Delaram Jarchi, 2022). Builds four new indicator-based directional-changes trading strategies, combines them with three existing ones via a genetic algorithm, and tests all on 44 NYSE stocks against a buy-and-sell benchmark.
- [[sources/salman-2023-optimization-trading-strategies-genetic-algorithm-under|Optimization of Trading Strategies Using a Genetic Algorithm under the Directional Changes Paradigm with Multiple Thresholds]] (Ozgur Salman, Themistoklis Melissourgos, Michael Kampouridis, 2023). Runs ten Directional Change thresholds in parallel for three new trading strategies and uses a genetic algorithm to weight and combine their signals, beating single-threshold strategies and RSI, MACD and buy-and-hold benchmarks on 18 NYSE stocks.
- [[sources/salman-2025-genetic-algorithm-optimization-multi-threshold-trading|A genetic algorithm for the optimization of multi-threshold trading strategies in the directional changes paradigm]] (Ozgur Salman, Themistoklis Melissourgos, Michael Kampouridis, 2025). A genetic algorithm weights eight directional-changes strategies across ten thresholds and beats individual DC strategies, technical indicators, buy-and-hold and market indices on 200 NYSE stocks.
- [[sources/sjogren-2021-general-compound-hawkes-processes-mid-price|General Compound Hawkes Processes for Mid-Price Prediction]] (Myles Sjogren, Timothy DeLise, 2021). Fits four General Compound Hawkes Process variants to sugar futures and stock order-book data and tests two prediction methods for mid-price direction and volatility.
- [[sources/spears-2020-investment-sizing-deep-learning-prediction-uncertainties|Investment sizing with deep learning prediction uncertainties for high-frequency Eurodollar futures trading]] (Trent Spears, Stefan Zohren, Stephen Roberts, 2020). Uses deep-learning aleatoric and epistemic prediction uncertainty to scale position sizes trading a multivariate Eurodollar-futures interest-rate curve, improving out-of-sample Sharpe ratio versus not sizing by uncertainty.
- [[sources/tao-2018-directional-change-information-extraction-financial-market|Using Directional Change for Information Extraction in Financial Market Data]] (Ran Tao, 2018). Introduces directional-change (DC) event-based sampling of price series and defines DC indicators and metrics to profile and compare financial markets as a complement to time series analysis.
- [[sources/tsang-2024-nowcasting-directional-change-high-frequency-fx|Nowcasting directional change in high frequency FX markets]] (Edward P. K. Tsang, Shuai Ma, V. L. Raju Chinthalapati, 2024). Proposes a simple, historical-distribution-based rule to nowcast directional changes in FX tick data before they are formally confirmed, and tests it on three currency pairs.
- [[sources/wu-2023-intelligent-trading-strategy-based-improved-directional|Intelligent trading strategy based on improved directional change and regime change detection]] (Bing Wu, Xiangzu Han, 2023). Adds a decay-coefficient threshold and Bayesian-optimized hyperparameters to the Directional Change framework, filters trades with a hidden Markov regime detector, and shows the combination raises forex trading returns and cuts drawdowns.
- [[sources/ye-2017-developing-sustainable-trading-strategies-directional-changes|Developing Sustainable Trading Strategies Using Directional Changes with High Frequency Data]] (Ailun Ye, V L Raju Chinthalapati, Antoaneta Serguieva and others, 2017). Proposes and backtests four directional-change-based FX trading strategies, alone and combined with the DMI technical indicator, on EUR/USD and GBP/USD tick data across ten thresholds.
- [[sources/zhao-2026-novel-trading-algorithms-augmented-intrinsic-time|Novel Trading Algorithms augmented by Intrinsic Time and Machine Learning]] (Qi Zhao, 2026). PhD thesis using the Directional Change intrinsic-time framework to build FX trading strategies, then layering machine-learning overshoot prediction and a ResNet-policy RL agent on top.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/directional-change|Directional Change]]
- [[concepts/event-clock|Event Clock]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/stylized-facts|stylized facts]]
<!-- AUTHORED REGION END -->