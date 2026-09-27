---
content_hash: sha256:a6dac18c82c5f205fda8ac36a583510227876e69a1be4b88dc1ead1c83584b84
created: 2026-09-27 01:47:00+00:00
mind_map_priority: medium
page_id: concepts/bulk-volume-classification
page_type: concept
related:
- concepts/trade-classification
- concepts/vpin
- concepts/volume-clock
- concepts/order-imbalance
- concepts/informed-trading
revision_id: 1
schema_version: 2
sources:
- sources/andersen-2013-assessing-measures-order-flow-toxicity-early
- sources/andersen-2013-reflecting-vpin-dispute
- sources/bambade-2019-assessment-prediction-quality-vpin
- sources/he-2016-volume-synchronised-probability-informed-trading-chinese
- sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
- sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
- sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych
- sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e
- sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification
- sources/wu-2013-big-data-approach-analyzing-market-volatility
tags:
- trade-classification
- bulk-volume-classification
- vpin
- order-imbalance
- volume-clock
title: Bulk Volume Classification
updated: '2026-09-27T01:47:00Z'
uuid: 1038e45a-18f7-53f0-9d34-4d1557d0d3a3
---

<!-- AUTHORED REGION START -->
# Bulk Volume Classification

Bulk volume classification estimates how much of the volume in a bar was buying and how much was selling. It does this from the bar's price change alone, without classifying any single trade.

## How it works

The price change over the bar is divided by a measure of recent price variability. A probability distribution is applied to that standardised change, giving a fraction between zero and one. That fraction of the bar's volume is counted as buys and the rest as sells. A bar that closed well above where it opened is counted as mostly buying.

## Why it exists

Classifying each trade needs the quotes in force at the moment of the trade, and needs the two records to be lined up exactly. Bulk classification needs only bar prices and bar volumes. It is therefore usable where trade-level data is missing or poorly time-stamped.

## Relation to other methods

It is an alternative to the trade-by-trade rules covered under [[concepts/trade-classification|trade classification]], such as the tick rule. It is the usual input to [[concepts/vpin|VPIN]].

## Caveats

Because the buy fraction is a function of the price change, any imbalance measured this way is tied to the price move by construction. A link between that imbalance and later volatility may then say more about price moves than about order flow. Several sources in this wiki find it less accurate than classifying each trade.

## Sources in This Wiki

- [[sources/andersen-2013-assessing-measures-order-flow-toxicity-early|Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market Turbulence]] (Torben G. Andersen, Oleg Bondarenko, 2014). Tests whether the VPIN order-flow-toxicity metric predicts volatility, using CME best-bid-offer data for E-mini S&P 500 futures to build a near-exact trade-classification benchmark.
- [[sources/andersen-2013-reflecting-vpin-dispute|Reflecting on the VPIN Dispute]] (Torben G. Andersen, Oleg Bondarenko, 2013). A rejoinder arguing that VPIN's apparent power to forecast volatility is a mechanical artifact of its correlation with trading volume and volatility, not genuine order-flow-toxicity information.
- [[sources/bambade-2019-assessment-prediction-quality-vpin|An Assessment of the Prediction Quality of VPIN]] (Antoine Bambade, Kesheng Wu, 2019). Builds a precision/recall framework to test whether VPIN predicts flash crashes in five liquid futures, benchmarks it against a naive classifier, and checks sensitivity to the data set's starting point.
- [[sources/he-2016-volume-synchronised-probability-informed-trading-chinese|Volume-Synchronised Probability of Informed Trading on Chinese Index Futures: A Comparative Approach]] (Zhongzhi (Lawrence) He, Jinzhi Jiang, Martin Kusy and others, 2016). Compares three trade-classification-based VPIN metrics (tick rule, Lee-Ready, bulk volume) on Chinese index futures data to see which best warns of two 2013 volatility events.
- [[sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin|Volume-Synchronized Probability of Informed Trading (VPIN), Market Volatility, and High-Frequency Liquidity]] (Jinzhi Jiang, 2015). Compares three ways of computing VPIN on two volatile episodes in Chinese stock index futures and tests a two-way feedback loop between VPIN and high-frequency liquidity.
- [[sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact|Flow Toxicity of High Frequency Trading and Its Impact on Price Volatility: Evidence from the KOSPI 200 Futures Market]] (Jangkoo Kang, Kyung Yoon Kwon, Wooyeon Kim, 2019). Shows that a bulk-volume-classified VPIN measure predicts short-term volatility in KOSPI 200 futures, and that high-frequency traders cut flow toxicity in normal times but add to it in stressful times.
- [[sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych|Ekonometryczna analiza prawdopodobieństwa zawarcia transakcji wynikających z napływu informacji – wpływ założeń co do rozkładu stóp zwrotu na zmienność miary VPIN]] (Marcin Niedużak, Mateusz Pipień, 2014). Tests how three assumed return distributions in the Bulk Volume Classification algorithm change estimated VPIN for a Warsaw-listed stock (KGHM).
- [[sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e|Análise dos Algoritmos Tick Rule e Bulk Volume Classification no Mercado Acionário Brasileiro]] (Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral, 2023). Compares Tick Rule and Bulk Volume Classification for labeling B3 stock-trade sides and shows, via VPIN, that Tick Rule tracks true order-flow imbalance far better in the Brazilian market.
- [[sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification|Analysis of the Tick Rule and Bulk Volume Classification Algorithms in the Brazilian Stock Market]] (Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral, 2023). Compares the Tick Rule against Bulk Volume Classification for labeling buyer- versus seller-initiated trades on the Brazilian B3 exchange and finds Tick Rule clearly more accurate and a better basis for a VPIN order-flow-toxicity proxy.
- [[sources/wu-2013-big-data-approach-analyzing-market-volatility|A Big Data Approach to Analyzing Market Volatility]] (Kesheng Wu, E. Wes Bethel, Ming Gu and others, 2013). Applies HPC data-management techniques to compute VPIN and a fast Maximum Intermediate Return measure across 16,000 parameter combinations on 3 billion futures trades, confirming VPIN predicts liquidity-driven volatility.

## Related

- [[concepts/trade-classification|trade classification]]
- [[concepts/vpin|VPIN]]
- [[concepts/volume-clock|Volume Clock]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/informed-trading|informed trading]]
<!-- AUTHORED REGION END -->