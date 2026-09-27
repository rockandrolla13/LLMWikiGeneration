---
content_hash: sha256:3845866ee332878abeb50591a6d8c4e1cfbd23a6aca5ad40ab66246730f6a567
created: 2026-09-27 01:47:00+00:00
mind_map_priority: high
page_id: concepts/vpin
page_type: concept
related:
- concepts/volume-clock
- concepts/bulk-volume-classification
- concepts/informed-trading
- concepts/order-imbalance
- concepts/adverse-selection
- concepts/trade-classification
- concepts/sampling-clocks
revision_id: 1
schema_version: 2
sources:
- sources/andersen-2013-assessing-measures-order-flow-toxicity-early
- sources/andersen-2013-reflecting-vpin-dispute
- sources/balagan-2026-learning-polymarket-taker-trade-direction-chain
- sources/bambade-2019-assessment-prediction-quality-vpin
- sources/bambade-2019-new-way-compute-probability-informed-trading
- sources/bethel-2011-federal-market-information-technology-post-flash
- sources/bongaerts-2025-cross-sectional-identification-private-information
- sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability
- sources/fang-2019-design-high-frequency-trading-algorithm-based
- sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility
- sources/he-2016-volume-synchronised-probability-informed-trading-chinese
- sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
- sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
- sources/karyampas-2011-probability-informed-trading-volatility-etf
- sources/lee-2017-informed-trading-futures-markets-during-financial
- sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych
- sources/qin-2026-polymarket-v1-database
- sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e
- sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification
- sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability
- sources/turkoglu-2015-natural-time-crash-risk
- sources/wu-2013-big-data-approach-analyzing-market-volatility
- sources/wu-2013-testing-vpin-big-data-response-reflecting
- sources/zhai-2026-public-trader-identity-adverse-selection-return
tags:
- vpin
- flow-toxicity
- informed-trading
- volume-clock
- order-imbalance
title: VPIN
updated: '2026-09-27T01:47:00Z'
uuid: 36c60eed-24af-5f92-948c-d8e2b4eec705
---

<!-- AUTHORED REGION START -->
# VPIN

VPIN stands for the volume-synchronized probability of informed trading. It is a measure of order flow toxicity: how likely it is that liquidity providers are trading against better-informed counterparties.

## How it is built

1. Trading is cut into buckets of equal volume, on a [[concepts/volume-clock|volume clock]].
2. The volume in each bucket is split into buys and sells, usually by [[concepts/bulk-volume-classification|bulk volume classification]].
3. The absolute difference between buy and sell volume is taken for each bucket.
4. That difference is averaged over a rolling window of buckets and scaled by the bucket size.

A high value means trading has been one-sided.

## Why it matters here

VPIN is the most widely studied imbalance measure built on an activity clock. It is the clearest worked example of measuring [[concepts/order-imbalance|order imbalance]] in volume time.

## The dispute

The sources in this wiki disagree about whether it works. Its proponents report that it rises ahead of episodes of market stress. Its critics report that its predictive power comes mainly from its link to trading volume and volatility, and that it depends heavily on how trades are classified. A reader should treat the measure as contested and read both sides.

## Caveats

The result depends on the bucket size, the length of the rolling window, and the classification method. None of these has an agreed value. The measure is unsigned, so it shows that flow was one-sided without showing which side.

## Sources in This Wiki

- [[sources/andersen-2013-assessing-measures-order-flow-toxicity-early|Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market Turbulence]] (Torben G. Andersen, Oleg Bondarenko, 2014). Tests whether the VPIN order-flow-toxicity metric predicts volatility, using CME best-bid-offer data for E-mini S&P 500 futures to build a near-exact trade-classification benchmark.
- [[sources/andersen-2013-reflecting-vpin-dispute|Reflecting on the VPIN Dispute]] (Torben G. Andersen, Oleg Bondarenko, 2013). A rejoinder arguing that VPIN's apparent power to forecast volatility is a mechanical artifact of its correlation with trading volume and volatility, not genuine order-flow-toxicity information.
- [[sources/balagan-2026-learning-polymarket-taker-trade-direction-chain|Learning Polymarket Taker Trade Direction from the On-Chain Tape]] (Sukhman Balagan, 2026). Trains gradient-boosted trees and a 1D CNN on causal tape features to classify Polymarket taker trade direction, beating a corrected tick rule and better recovering OFI and VPIN downstream.
- [[sources/bambade-2019-assessment-prediction-quality-vpin|An Assessment of the Prediction Quality of VPIN]] (Antoine Bambade, Kesheng Wu, 2019). Builds a precision/recall framework to test whether VPIN predicts flash crashes in five liquid futures, benchmarks it against a naive classifier, and checks sensitivity to the data set's starting point.
- [[sources/bambade-2019-new-way-compute-probability-informed-trading|A New Way to Compute the Probability of Informed Trading]] (Antoine Bambade, 2019). Re-derives the Probability of Informed Trading (PIN) exactly in its original time-clock framework, shows why VPIN's volume-clock approximation is theoretically flawed, and proposes a new exact PIN estimator.
- [[sources/bethel-2011-federal-market-information-technology-post-flash|Federal Market Information Technology in the Post Flash Crash Era: Roles for Supercomputing]] (E. Wes Bethel, David Leinweber, Oliver Rubel and others, 2011). Reports early experiments applying HPC data management (HDF5, bitmap indexing) and parallel computation to VPIN and market-fragmentation (HHI) indicators as an early-warning system for events like the 2010 Flash Crash.
- [[sources/bongaerts-2025-cross-sectional-identification-private-information|Cross-sectional identification of private information]] (Dion Bongaerts, Dominik Rösch, Mathijs van Dijk, 2026). Derives a closed-form private information measure -- price impact times order imbalance -- from a multi-security strategic trading model and validates it using NYSE data.
- [[sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability|Microstructural changes before Macroeconomic Announcements: Predictability of Economic Surprises in the U.S. market]] (Rita Dias Barreto Calçada, 2015). Tests whether pre-announcement order and depth imbalances (VPIN, DI) in S&P 500 and 10-year Treasury futures predict the sign of U.S. macroeconomic surprises.
- [[sources/fang-2019-design-high-frequency-trading-algorithm-based|Design of High-Frequency Trading Algorithm Based on Machine Learning]] (Boyue Fang, Yutong Feng, 2019). Combines VPIN informed-trading signals, GARCH volatility forecasts, and an SVM filter into a high-frequency market-making strategy, backtested on CSI300 index futures.
- [[sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility|Informed trading, investor beliefs consensus and volatility: Evidence from the Limit Order Book dynamics during COVID-19 and short-selling ban]] (Sandra Ferreruela, Daniel Martín, 2025). Compares VPIN (executed order-flow toxicity) against the slope of the limit order book (belief consensus) as predictors of short-horizon volatility for 32 IBEX-35 stocks in 2019-2020.
- [[sources/he-2016-volume-synchronised-probability-informed-trading-chinese|Volume-Synchronised Probability of Informed Trading on Chinese Index Futures: A Comparative Approach]] (Zhongzhi (Lawrence) He, Jinzhi Jiang, Martin Kusy and others, 2016). Compares three trade-classification-based VPIN metrics (tick rule, Lee-Ready, bulk volume) on Chinese index futures data to see which best warns of two 2013 volatility events.
- [[sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin|Volume-Synchronized Probability of Informed Trading (VPIN), Market Volatility, and High-Frequency Liquidity]] (Jinzhi Jiang, 2015). Compares three ways of computing VPIN on two volatile episodes in Chinese stock index futures and tests a two-way feedback loop between VPIN and high-frequency liquidity.
- [[sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact|Flow Toxicity of High Frequency Trading and Its Impact on Price Volatility: Evidence from the KOSPI 200 Futures Market]] (Jangkoo Kang, Kyung Yoon Kwon, Wooyeon Kim, 2019). Shows that a bulk-volume-classified VPIN measure predicts short-term volatility in KOSPI 200 futures, and that high-frequency traders cut flow toxicity in normal times but add to it in stressful times.
- [[sources/karyampas-2011-probability-informed-trading-volatility-etf|Probability of Informed Trading and Volatility for an ETF]] (Dimitrios Karyampas, Paola Paiardini, 2011). Estimates VPIN, a volume-bucketed measure of informed trading, for the SPY ETF and links it to jump-robust realized volatility through a HAR-RV model.
- [[sources/lee-2017-informed-trading-futures-markets-during-financial|Informed Trading of Futures Markets During the Financial Crisis: Evidence from the VPIN]] (Yen-Hsien Lee, Wen-Chien Liu, Chia-Lin Hsieh, 2017). Tests whether VPIN-measured informed trading affects Taiwan futures returns during the 2008-2009 crisis, separately for domestic and foreign institutional investors and interacted with day-of-week effects.
- [[sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych|Ekonometryczna analiza prawdopodobieństwa zawarcia transakcji wynikających z napływu informacji – wpływ założeń co do rozkładu stóp zwrotu na zmienność miary VPIN]] (Marcin Niedużak, Mateusz Pipień, 2014). Tests how three assumed return distributions in the Bulk Volume Classification algorithm change estimated VPIN for a Warsaw-listed stock (KGHM).
- [[sources/qin-2026-polymarket-v1-database|Polymarket-v1 Database]] (Boka Qin, Rui Yang, 2026). Introduces a -billion-trade, ground-truth-direction archive of Polymarket's v1 exchange and uses it to show standard trade-classification rules fail systematically and that true order-flow toxicity predicts forecast accuracy.
- [[sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e|Análise dos Algoritmos Tick Rule e Bulk Volume Classification no Mercado Acionário Brasileiro]] (Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral, 2023). Compares Tick Rule and Bulk Volume Classification for labeling B3 stock-trade sides and shows, via VPIN, that Tick Rule tracks true order-flow imbalance far better in the Brazilian market.
- [[sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification|Analysis of the Tick Rule and Bulk Volume Classification Algorithms in the Brazilian Stock Market]] (Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral, 2023). Compares the Tick Rule against Bulk Volume Classification for labeling buyer- versus seller-initiated trades on the Brazilian B3 exchange and finds Tick Rule clearly more accurate and a better basis for a VPIN order-flow-toxicity proxy.
- [[sources/song-2014-parameter-analysis-vpin-volume-synchronized-probability|Parameter Analysis of the VPIN (Volume synchronized Probability of Informed Trading) Metric]] (Jung Heon Song, Kesheng Wu, Horst D. Simon, 2014). Uses the NOMAD optimizer and UQTK sensitivity analysis to search VPIN's free-parameter space and cut its false positive rate across a large futures panel.
- [[sources/turkoglu-2015-natural-time-crash-risk|Natural Time and Crash Risk]] (Ata Türkoğlu, 2015). A PhD thesis that recovers near-normal high-frequency stock returns via order-book-based subordination in transaction time, then reuses the same order-book variables to predict flash crashes and G10 currency crashes.
- [[sources/wu-2013-big-data-approach-analyzing-market-volatility|A Big Data Approach to Analyzing Market Volatility]] (Kesheng Wu, E. Wes Bethel, Ming Gu and others, 2013). Applies HPC data-management techniques to compute VPIN and a fast Maximum Intermediate Return measure across 16,000 parameter combinations on 3 billion futures trades, confirming VPIN predicts liquidity-driven volatility.
- [[sources/wu-2013-testing-vpin-big-data-response-reflecting|Testing VPIN on Big Data -- Response to "Reflecting on the VPIN Dispute"]] (Kesheng Wu, E. Wes Bethel, Ming Gu and others, 2013). A rebuttal note defending VPIN's false-positive-rate methodology and event count against Andersen and Bondarenko's critique, using tests on 94 futures contracts.
- [[sources/zhai-2026-public-trader-identity-adverse-selection-return|Public Trader Identity: Adverse Selection and Return Predictability]] (Daojing Zhai, 2026). Uses Hyperliquid's public wallet addresses to show that trader-level adverse selection persists across time and that adding known-toxic wallets' activity to an anonymous order-book benchmark raises short-horizon return forecasts.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/sampling-clocks|Sampling Clocks]]
<!-- AUTHORED REGION END -->