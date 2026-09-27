---
authors:
- Leonardo Souza Siqueira
- Laíse Ferraz Correia
- Hudson Fernandes Amaral
content_hash: sha256:abc95d7d9e66659ca1b5cfab3992444ad24316ac4330e094e0e63712d07dd167
created: 2026-09-27 01:47:00+00:00
page_id: sources/siqueira-2023-analysis-tick-rule-bulk-volume-classification
page_type: source
related:
- concepts/sampling-clocks
- concepts/trade-classification
- concepts/adverse-selection
- concepts/market-microstructure
- concepts/informed-trading
- concepts/high-frequency-data
- concepts/vpin
- concepts/bulk-volume-classification
revision_id: 1
schema_version: 2
source_hash: sha256:a2a272edef44627c81d1c4ac52d2bd9bdf6a243773b93a60a6f21cb39bdf5331
source_path: markdown_output/siqueira-2023-analysis-tick-rule-bulk-volume-classification.md
source_type: paper
tags:
- trade-classification
- vpin
- bulk-volume-classification
- tick-rule
- market-microstructure
- informed-trading
- brazilian-equities
- clock-compares
- asset-equity
- harvest-core
title: Analysis of the Tick Rule and Bulk Volume Classification Algorithms in the
  Brazilian Stock Market
updated: '2026-09-27T01:47:00Z'
uuid: f41c77f4-e1d9-5220-aec5-2ac65b01f50e
year: 2023
---

<!-- AUTHORED REGION START -->
# Analysis of the Tick Rule and Bulk Volume Classification Algorithms in the Brazilian Stock Market

## Summary

The paper asks which of two trade-classification methods, the tick-by-tick Tick Rule (TR) or the interval-based Bulk Volume Classification (BVC), better recovers the true buy or sell side of trades on the Brazilian B3 stock exchange, and which one produces a more reliable Volume-Synchronized Probability of Informed Trading (VPIN) toxicity measure. Determining which side initiated a trade matters for detecting information asymmetry and informed trading, but the true side is rarely available directly, so classification algorithms are used as a substitute.

Stocks traded on B3 every day between 2018 and mid-2019 are split by traded volume into small, medium and large classes using the Fisher-Jenks algorithm. BVC's parameters (the choice of time or volume interval used to group trades) are calibrated on 2018 data separately for each volume class and then re-tested on 2019 data to check stability. TR and BVC classifications are each compared against the actual recorded buy/sell side of every trade, and VPIN is computed three ways: from the actual trade sides, from TR-estimated sides, and from BVC-estimated sides, using 50 equal-volume buckets per trading day.

TR substantially outperformed BVC on classification accuracy and on how closely its VPIN tracked the VPIN computed from actual trade data, across all three volume classes. Digging into why, the paper shows TR's economic logic (price rises indicate buys, price falls indicate sells) holds up well in this market, while BVC's assumption that trade volume splits according to a normal distribution of price changes does not match the data, especially for lower-volume, more volatile assets, and BVC's most-accurate calibration was unstable for those assets from one year to the next.

What is new is applying this TR-versus-BVC comparison, including a direct VPIN accuracy check against real Brazilian trade-side data, to an emerging, order-driven market with lower trading volume and higher volatility than the US, European or Australian markets where these algorithms were originally validated.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Tick Rule classifies each individual trade (tick-by-tick) by comparing its price to the immediately preceding trade's price, repeating the prior side when price is unchanged. Bulk Volume Classification instead groups trades into fixed time intervals, chosen among 1-, 2-, 3- and 5-minute intervals plus several fixed-volume intervals, and splits each interval's total volume into estimated buy and sell portions using the standard normal distribution applied to the standardized price change over the interval. Both sets of estimated buy/sell volumes are then aggregated into VPIN by dividing each trading day into 50 equal-volume buckets and averaging the absolute imbalance between buy and sell volume across those buckets; there is no forward prediction horizon, since accuracy and VPIN values are checked directly against the actual recorded trade side for the same period.

## Data

- **Asset class:** Equities
- **Instruments:** 181 B3-listed stocks that traded every day in the sample period, split into small, medium and large volume classes using the Fisher-Jenks algorithm
- **Venue:** B3 (Brazilian stock exchange, an order-driven market)
- **Period:** 2018 data used to calibrate BVC parameters; January 02, 2018 to June 28, 2019 used to test the parameters and compute VPIN
- **Granularity:** Tick-by-tick trade records, aggregated into 5-minute intervals for BVC and into 50 equal-volume buckets per trading day for VPIN

## Features and Measures

- **Tick Rule (TR).** Classifies each trade as buyer- or seller-initiated by comparing its price to the immediately preceding trade's price, repeating the prior classification when price is unchanged.
- **Bulk Volume Classification (BVC).** Groups trades into fixed time or volume intervals and splits each interval's volume into buy and sell portions using the standard normal distribution applied to the standardized price change between the start and end of the interval.
- **Volume-Synchronized Probability of Informed Trading (VPIN).** Divides a trading day into equal-volume buckets and averages the absolute imbalance between estimated buy and sell volume across the buckets, as a proxy for order-flow toxicity and the probability of informed trading.

## Method

BVC's interval parameter (time-based or volume-based) is calibrated separately for each of the three volume classes using 2018 trade data, selecting for each asset the setting with the highest classification accuracy against actual trade sides, then the same parameters are re-tested on 2019 data to check whether performance holds. TR and BVC classifications are each compared directly against the true recorded buy/sell side of every trade to compute per-asset and per-class accuracy rates. VPIN is then computed three ways, from actual trade sides, from TR-estimated sides, and from BVC-estimated sides, and the resulting VPIN series are compared by correlation, separately for each volume class. Finally, the properties of TR misclassifications are examined by breaking down errors by the size of the price change, whether the current and previous order share the same brokerage on the buy or sell side, and the time elapsed between trades, and the properties of BVC are examined by comparing its assumed normal-distribution buy/sell split against the actual buy/sell split observed at different levels of price change.

## Results

- Tick Rule's overall classification accuracy across all classes was 80.82%, versus 56.85% for Bulk Volume Classification.
- Tick Rule's lowest per-asset accuracy (62.99%) was still higher than Bulk Volume Classification's highest per-asset accuracy (70.90%), which occurred in the highest-volume asset class.
- The best-performing Bulk Volume Classification interval was 5 minutes for all three volume classes.
- Tick-Rule-derived VPIN correlated strongly with VPIN computed from actual trade data, averaging roughly 80% across classes, while Bulk-Volume-Classification-derived VPIN correlated on average only up to about 50% for medium-class assets, with some negative correlations observed for small stocks.
- For price changes above 0.20 currency units, the trade still moved in the direction Tick Rule assumes in about 88% of cases.
- When price was unchanged between trades, repeating the previous trade's side, as Tick Rule does, was correct in 95.31% of cases.
- When Bulk Volume Classification intervals showed no price change, it split about 51.88% of volume to the buy side, close to an even split, and such no-change intervals made up about 22% of all intervals.
- The most-accurate Bulk Volume Classification parameter setting for a given asset was stable between 2018 and 2019 for 78% of high-volume stocks and 74% of medium-volume stocks, but only 35% of low-volume stocks.

## Limitations

- Findings are based only on Brazilian B3 data, a lower-volume, order-driven and more volatile market than the US, European or Australian markets used in prior TR/BVC studies the authors cite for comparison.
- Bulk Volume Classification's best-performing calibration was unstable for low-volume stocks, and the authors advise caution about applying it to that asset class at all.
- Reader note: Bulk Volume Classification's parameter instability persisted even under an alternative volume-based grouping of the smallest stocks, suggesting the low-volume result reflects a property of the method rather than of the specific grouping chosen.
- Only stocks that traded on every day of the sample period were included, a deliberate restriction the authors adopted to avoid long gaps between trades distorting the interval construction.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]

## Citation

Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral (2023). Analysis of the Tick Rule and Bulk Volume Classification Algorithms in the Brazilian Stock Market.

DOI: 10.15728/bbr.2023.20.1.6.en

Text ingested: `markdown_output/siqueira-2023-analysis-tick-rule-bulk-volume-classification.md`, converted from `raw/ofi-event-clock/siqueira-2023-analysis-tick-rule-bulk-volume-classification.pdf`.

Coverage of this summary: Read the full paper end to end, including the introduction, literature review on trade classification and VPIN, methodology, sample construction, all seven results tables and five figures, and the final remarks.

Known problems with the input: No journal or conference name is spelled out in the markdown; only a DOI with prefix 'bbr' and submission/acceptance dates are printed, so venue is recorded as not stated rather than guessed; Several equations (BVC volume-split formula, VPIN formula, TR frequency formulas) are rendered as omitted pictures or garbled OCR text in the markdown and were not used for any numeric claim.
<!-- AUTHORED REGION END -->