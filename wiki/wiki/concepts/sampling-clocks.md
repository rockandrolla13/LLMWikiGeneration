---
content_hash: sha256:6246592983e569d9448fe4a96fd4f2baaa26042009fe83512c62fab09cb7b877
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/sampling-clocks
page_type: concept
related:
- concepts/event-clock
- concepts/trade-clock
- concepts/volume-clock
- concepts/intrinsic-time
- concepts/directional-change
- concepts/stochastic-time-change
- concepts/epps-effect
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/realized-variance
revision_id: 1
schema_version: 2
sources:
- sources/abdulkarim-2019-topics-market-microstructure
- sources/anantha-2024-forecasting-high-frequency-order-flow-imbalance
- sources/andersen-2013-assessing-measures-order-flow-toxicity-early
- sources/andersen-2013-reflecting-vpin-dispute
- sources/angstmann-2026-non-unique-time-market-incompleteness
- sources/bambade-2019-new-way-compute-probability-informed-trading
- sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts
- sources/berardi-2005-time-foreign-exchange-markets
- sources/berti-2025-tlob-novel-transformer-model-dual-attention
- sources/bethel-2011-federal-market-information-technology-post-flash
- sources/chang-2021-epps-effect-under-alternative-sampling-schemes
- sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time
- sources/eisler-2007-limit-order-book-different-time-scales
- sources/fang-2019-design-high-frequency-trading-algorithm-based
- sources/fayyaz-2026-frequency-controlled-comparison-tick-minute-based
- sources/gebbie-2026-gabor-epps-uncertainty-principle-traders
- sources/george-2025-deep-reinforcement-learning-trading-strategy-development
- sources/gillemot-2006-there-s-more-volatility-than-volume
- sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time
- sources/gu-2007-empirical-distributions-chinese-stock-returns-different
- sources/hellermann-2026-event-based-limit-order-book-representations
- sources/khubiev-2025-deep-learning-models-meet-financial-data
- sources/lehalle-2019-incorporating-signals-into-optimal-trading
- sources/long-2025-depth-investigation-genetic-programming-under-physical
- sources/masi-2026-analysis-synthetic-generation-financial-time-series
- sources/oomen-2004-properties-realized-variance-pure-jump-process
- sources/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency
- sources/silva-2005-applications-physics-finance-economics-returns-trading
- sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e
- sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification
- sources/sirignano-2018-deep-learning-limit-order-books
- sources/thorburn-2015-forecasting-limit-order-book-price-changes
- sources/yamagishi-2026-run-one-rule-five-clocks-only
- sources/yamagishi-2026-volume-bar-foreign-exchange-identically-tick
- sources/zhai-2026-public-trader-identity-adverse-selection-return
tags:
- sampling
- event-time
- market-microstructure
- high-frequency-data
- feature-engineering
title: Sampling Clocks
updated: '2026-09-27T01:47:00Z'
uuid: 5cb22f08-f5a0-5344-891d-0894457afa6a
---

<!-- AUTHORED REGION START -->
# Sampling Clocks

A sampling clock is the rule that decides when a market is observed. The default is the wall clock: one observation every fixed number of seconds or minutes. The alternatives let the market's own activity set the pace, so that busy periods are sampled often and quiet periods rarely.

## Why the clock matters for features

A feature is always measured over some window, and the clock decides what a window contains. On a wall clock, a window holds a fixed span of time and a varying amount of activity. On an activity clock, it holds a fixed amount of activity and a varying span of time. The same imbalance measure can therefore behave differently on two clocks, and a result found on one does not carry over to another without being tested.

## The main families

- [[concepts/event-clock|Event clock]]: one observation per order book update.
- [[concepts/trade-clock|Trade clock]]: one observation per trade, or per fixed number of trades.
- [[concepts/volume-clock|Volume clock]]: one observation per fixed amount of volume traded.
- [[concepts/intrinsic-time|Intrinsic time]]: one observation per price move of a set size, of which [[concepts/directional-change|directional change]] is the best-known form.
- [[concepts/stochastic-time-change|Stochastic time change]]: the clock treated as a random process inside a model, not only as a way of cutting the data.

## What this page collects

The sources listed here are the ones that test two or more clocks against each other. Papers that use a single clock are listed on that clock's own page.

## Caveats

Changing the clock changes the prediction target as well as the inputs. A forecast of the next price move and a forecast of the return over the next minute are different problems, and their accuracy figures cannot be compared directly. Activity clocks also make the observation times depend on the data, which matters for any statistic that assumes the sampling times were fixed in advance.

## Sources in This Wiki

- [[sources/abdulkarim-2019-topics-market-microstructure|Topics in Market Microstructure]] (, 2019). A PhD thesis with three studies: an agent-based FTT market simulation, and two LSE order-book studies of an NVWAP trend indicator and order-cancellation effects on price and spread.
- [[sources/anantha-2024-forecasting-high-frequency-order-flow-imbalance|Forecasting high frequency order flow imbalance using Hawkes processes]] (Aditya Nittur Anantha, Shashi Jain, 2024). Uses Hawkes processes to build and forecast a tick-level Order Flow Imbalance indicator, then ranks competing forecasting models with a superior-predictive-ability test.
- [[sources/andersen-2013-assessing-measures-order-flow-toxicity-early|Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market Turbulence]] (Torben G. Andersen, Oleg Bondarenko, 2014). Tests whether the VPIN order-flow-toxicity metric predicts volatility, using CME best-bid-offer data for E-mini S&P 500 futures to build a near-exact trade-classification benchmark.
- [[sources/andersen-2013-reflecting-vpin-dispute|Reflecting on the VPIN Dispute]] (Torben G. Andersen, Oleg Bondarenko, 2013). A rejoinder arguing that VPIN's apparent power to forecast volatility is a mechanical artifact of its correlation with trading volume and volatility, not genuine order-flow-toxicity information.
- [[sources/angstmann-2026-non-unique-time-market-incompleteness|Non-unique time and market incompleteness]] (Chris Angstmann, Tim Gebbie, 2026). Argues that financial markets' event-driven, asynchronous nature means the map from discrete event time to a continuous calendar-time price process is not unique, implying deeper market incompleteness.
- [[sources/bambade-2019-new-way-compute-probability-informed-trading|A New Way to Compute the Probability of Informed Trading]] (Antoine Bambade, 2019). Re-derives the Probability of Informed Trading (PIN) exactly in its original time-clock framework, shows why VPIN's volume-clock approximation is theoretically flawed, and proposes a new exact PIN estimator.
- [[sources/barardehi-2025-revisiting-shaped-patterns-volatility-price-impacts|Revisiting the ∪-shaped patterns in volatility and price impacts: Novel results using trade-time estimates]] (Yashar H. Barardehi, Dan Bernhardt, 2025). Using trade-time (fixed-dollar-volume) sampling instead of calendar-time intervals, the paper shows volatility and Kyle's lambda fall monotonically over the trading day rather than following the classic U-shape.
- [[sources/berardi-2005-time-foreign-exchange-markets|Time and foreign exchange markets]] (Luca Berardi, Maurizio Serva, 2005). Tests whether FX price dynamics fit calendar-time or business-time (quote-count) models using one year of DEM/USD tick quotes.
- [[sources/berti-2025-tlob-novel-transformer-model-dual-attention|TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data]] (Leonardo Berti, Gjergji Kasneci, 2025). Proposes TLOB, a dual-attention transformer, and MLPLOB, an MLP baseline, for LOB-based price trend prediction, beating prior SOTA on FI-2010, Tesla/Intel and Bitcoin data.
- [[sources/bethel-2011-federal-market-information-technology-post-flash|Federal Market Information Technology in the Post Flash Crash Era: Roles for Supercomputing]] (E. Wes Bethel, David Leinweber, Oliver Rubel and others, 2011). Reports early experiments applying HPC data management (HDF5, bitmap indexing) and parallel computation to VPIN and market-fragmentation (HHI) indicators as an early-warning system for events like the 2010 Flash Crash.
- [[sources/chang-2021-epps-effect-under-alternative-sampling-schemes|The Epps effect under alternative sampling schemes]] (Patrick Chang, Etienne Pienaar, Tim Gebbie, 2021). Compares the Epps correlation-decay effect under calendar, event (trade) and volume time using a Hawkes-process simulation and JSE equity data, finding it emerges linearly under volume time.
- [[sources/dimitriadis-2022-efficient-sampling-realized-variance-estimation-time|Efficient Sampling for Realized Variance Estimation in Time-Changed Diffusion Models]] (Timo Dimitriadis, Roxana Halbleib, Jeannine Polivka and others, 2025). Derives finite-sample efficiency theory for realized variance under intrinsic-time sampling schemes and shows empirically that hitting-time and a new realized business-time scheme beat calendar-time sampling.
- [[sources/eisler-2007-limit-order-book-different-time-scales|The limit order book on different time scales]] (Zoltán Eisler, János Kertész, Fabrizio Lillo, 2007). A qualitative comparison of the London Stock Exchange limit order book for GlaxoSmithKline across monthly, daily and tick-by-tick time scales.
- [[sources/fang-2019-design-high-frequency-trading-algorithm-based|Design of High-Frequency Trading Algorithm Based on Machine Learning]] (Boyue Fang, Yutong Feng, 2019). Combines VPIN informed-trading signals, GARCH volatility forecasts, and an SVM filter into a high-frequency market-making strategy, backtested on CSI300 index futures.
- [[sources/fayyaz-2026-frequency-controlled-comparison-tick-minute-based|A Frequency-Controlled Comparison of Tick- and Minute-Based Information Bars for Cryptocurrency Markets]] (Muhammad Toheed Fayyaz, Abdul Jabbar, Faheem Ahmad Qureshi and others, 2026). Compares tick-level and minute-level construction of six information bar types on six years of BTCUSDT futures data to test when tick data actually improves bar quality.
- [[sources/gebbie-2026-gabor-epps-uncertainty-principle-traders|A Gabor–Epps uncertainty principle for traders]] (Tim Gebbie, 2026). Uses the Gabor time-frequency uncertainty bound and the clock-dependent Epps effect to derive six rules of thumb for how long a trader must observe cross-asset order flow before treating correlation as tradable.
- [[sources/george-2025-deep-reinforcement-learning-trading-strategy-development|Deep Reinforcement Learning for Trading Strategy Development on High-Frequency Currency Data Using Directional Changes Sampling]] (George Rayment, 2025). A PhD thesis training deep reinforcement learning trading agents on directional-change-sampled high-frequency FX data, progressing from a filtered agent (FDRL) to positionally-aware (PADRL) to spread-aware (SADRL) frameworks.
- [[sources/gillemot-2006-there-s-more-volatility-than-volume|There’s more to volatility than volume]] (László Gillemot, J. Doyne Farmer, Fabrizio Lillo, 2006). Empirical study showing that neither trade count nor volume, but the order and size of individual price changes, drives clustered volatility and heavy tails in NYSE and LSE stock returns.
- [[sources/glattfelder-2022-bridging-gap-decoding-intrinsic-nature-time|Bridging the Gap: Decoding the Intrinsic Nature of Time in Market Data]] (James B. Glattfelder, Anton Golub, 2022). Derives an analytic bridge between physical-time and intrinsic (directional-change) time statistics, decomposing squared returns into a directional-change-count term and an overshoot-variability term, tested on Brownian motion and two currency series.
- [[sources/gu-2007-empirical-distributions-chinese-stock-returns-different|Empirical distributions of Chinese stock returns at different microscopic timescales]] (Gao-Feng Gu, Wei Chen, Wei-Xing Zhou, 2018). Studies the distribution of intraday returns for 23 Chinese stocks at several trade-count and minute-based sampling scales, finding an inverse cubic tail law at the single-trade scale that thins out as the scale grows.
- [[sources/hellermann-2026-event-based-limit-order-book-representations|Event-Based Limit Order Book Representations for Probabilistic VWAP Forecasting in Intraday Electricity Markets]] (Justin Hellermann, Stefan Lessmann, 2026). Compares time, tick, volume, and traded-value order-book bar construction for probabilistic VWAP forecasting in UK intraday electricity trading.
- [[sources/khubiev-2025-deep-learning-models-meet-financial-data|Deep Learning Models Meet Financial Data Modalities]] (Kasymkhan Khubiyev, Mikhail Semenov, 2025). Proposes image-based embeddings of limit order book snapshots (stacked vs. merged) and CNN/CNN-LSTM models to forecast cryptocurrency perpetual futures mid-price and drive a market-making strategy.
- [[sources/lehalle-2019-incorporating-signals-into-optimal-trading|Incorporating Signals into Optimal Trading]] (Charles-Albert Lehalle, Eyal Neuman, 2018). Adds a Markovian signal to optimal-execution models with transient and instantaneous impact, and shows NASDAQ OMX order-book imbalance is a mean-reverting predictor traders use.
- [[sources/long-2025-depth-investigation-genetic-programming-under-physical|An In-Depth Investigation of Genetic Programming Under Physical Time and Directional Change Frameworks for Algorithmic Trading]] (Xinpeng Long, Michael Kampouridis, Panagiotis Kanellopoulos, 2025). Introduces two genetic programming trading algorithms, GP-DC and GP-DC-PT, that use directional-change event indicators alongside or instead of physical-time technical indicators, testing them on 220 international stock datasets.
- [[sources/masi-2026-analysis-synthetic-generation-financial-time-series|Analysis and Synthetic Generation of Financial Time-Series]] (Giuseppe Masi, 2026). A PhD thesis developing formal shock detection, a benchmark of deep-learning limit-order-book trend predictors, GAN and diffusion generators for correlated and causally structured synthetic markets, and power-law-robust causal discovery.
- [[sources/oomen-2004-properties-realized-variance-pure-jump-process|Properties of Realized Variance for a Pure Jump Process: Calendar Time Sampling versus Business Time Sampling]] (Roel C.A. Oomen, 2004). Derives closed-form bias and MSE of realized variance for a compound-Poisson price process under calendar-time vs business-time sampling, and finds business-time sampling reduces MSE using IBM transaction data.
- [[sources/sadighian-2020-extending-deep-reinforcement-learning-frameworks-cryptocurrency|Extending Deep Reinforcement Learning Frameworks in Cryptocurrency Market Making]] (Jonathan Sadighian, 2020). Extends a deep reinforcement learning market-making framework by testing seven reward functions and introducing a price-based event environment, comparing it against a time-based one on Bitcoin data.
- [[sources/silva-2005-applications-physics-finance-economics-returns-trading|Applications of Physics to Finance and Economics: Returns, Trading Activity and Income]] (A. Christian Silva, 2005). A physics-style empirical study of stock log-returns across time scales, using a Heston-model closed form and a trade-count subordination clock, plus a study of the evolving distribution of US personal income.
- [[sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e|Análise dos Algoritmos Tick Rule e Bulk Volume Classification no Mercado Acionário Brasileiro]] (Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral, 2023). Compares Tick Rule and Bulk Volume Classification for labeling B3 stock-trade sides and shows, via VPIN, that Tick Rule tracks true order-flow imbalance far better in the Brazilian market.
- [[sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification|Analysis of the Tick Rule and Bulk Volume Classification Algorithms in the Brazilian Stock Market]] (Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral, 2023). Compares the Tick Rule against Bulk Volume Classification for labeling buyer- versus seller-initiated trades on the Brazilian B3 exchange and finds Tick Rule clearly more accurate and a better basis for a VPIN order-flow-toxicity proxy.
- [[sources/sirignano-2018-deep-learning-limit-order-books|Deep Learning for Limit Order Books]] (Justin A. Sirignano, 2016). Builds a new neural network architecture, the spatial neural network, that models the joint future distribution of best bid and best ask prices from the current limit order book state.
- [[sources/thorburn-2015-forecasting-limit-order-book-price-changes|Forecasting limit order book price changes using change point detection]] (Sebastian Thorburn, 2015). A CUSUM change-point detector applied to a limit order imbalance measure is used to sample the order book irregularly and forecast short-term mid-price changes, benchmarked against fixed 5-minute sampling.
- [[sources/yamagishi-2026-run-one-rule-five-clocks-only|Run One Rule on Five Clocks and Only the Direction and the Cost Agree [F055]: The direction stays below a cost of  to  pips on all five and the cost differs by only  times, yet the count differs by  times and the duration of a bar by  times]] (Yuuki Yamagishi, 2026). Runs one fixed entry/exit trading rule across five bar-sampling clocks (minute, hour, tick, volume, range) on FX and gold data, and reports which measured quantities agree or disagree across clock choice.
- [[sources/yamagishi-2026-volume-bar-foreign-exchange-identically-tick|為替の「出来⾼⾜」は、ティック⾜と恒等的に同じものである [F053]]] (⼭岸 勇輝（Yuuki YAMAGISHI）, 2026). Shows that FX 'volume bars' are definitionally identical to tick bars (agreement ), while range bars built on price-path length are a genuinely different, though still not net-move-invariant, clock.
- [[sources/zhai-2026-public-trader-identity-adverse-selection-return|Public Trader Identity: Adverse Selection and Return Predictability]] (Daojing Zhai, 2026). Uses Hyperliquid's public wallet addresses to show that trader-level adverse selection persists across time and that adding known-toxic wallets' activity to an anonymous order-book benchmark raises short-horizon return forecasts.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/trade-clock|Trade Clock]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/directional-change|Directional Change]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]
- [[concepts/epps-effect|Epps Effect]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/realized-variance|realized variance]]
<!-- AUTHORED REGION END -->