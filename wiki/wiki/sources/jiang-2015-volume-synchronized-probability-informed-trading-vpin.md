---
authors:
- Jinzhi Jiang
content_hash: sha256:96ddbce30e5bdbb69aaf792fb94461398e8decaeb2cbe3d823c27ca2bb2df175
created: 2026-09-27 01:47:00+00:00
page_id: sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
page_type: source
publication_venue: Goodman School of Business, Brock University (MSc in Management
  thesis)
related:
- concepts/volume-clock
- concepts/adverse-selection
- concepts/bid-ask-spread
- concepts/high-frequency-trading
- concepts/informed-trading
- concepts/liquidity-risk
- concepts/market-microstructure
- concepts/order-imbalance
- concepts/trade-classification
- concepts/vpin
- concepts/bulk-volume-classification
revision_id: 1
schema_version: 2
source_hash: sha256:29ccbb4bbdf0e5dc6601c66eda44ca14361740fcaf5247438887ea7499d8d445
source_path: markdown_output/jiang-2015-volume-synchronized-probability-informed-trading-vpin.md
source_type: paper
tags:
- vpin
- informed-trading
- market-liquidity
- order-flow-toxicity
- trade-classification
- high-frequency-trading
- var-model
- china-futures
- clock-volume
- asset-futures
- harvest-core
title: Volume-Synchronized Probability of Informed Trading (VPIN), Market Volatility,
  and High-Frequency Liquidity
updated: '2026-09-27T01:47:00Z'
uuid: 340a92be-dcc3-5e5e-88bb-c3602fc3adba
year: 2015
---

<!-- AUTHORED REGION START -->
# Volume-Synchronized Probability of Informed Trading (VPIN), Market Volatility, and High-Frequency Liquidity

## Summary

This MSc thesis asks which of three trade-classification algorithms gives VPIN (Volume-Synchronized Probability of Informed Trading) the most reliable early-warning signal ahead of extreme volatility, and whether VPIN and market liquidity feed back on each other in a high-frequency setting. It compares Bulk Volume Classification (BV-VPIN), Tick Rule (TR-VPIN) and Lee-Ready (LR-VPIN) around two Chinese Stock Index Futures episodes: the August 2013 'Fat Finger Event' and the June 2013 'Money Shortage Event'.

VPIN is built by splitting trading into fixed-size volume buckets, classifying each bucket's volume as buy- or sell-initiated under each of the three algorithms, and averaging the absolute order imbalance over a rolling window of buckets. The thesis checks BV-VPIN's stability across eight combinations of time-bar length, bucket size and sample length, tests the VPIN-volatility link with Pearson correlation, conditional-probability tables and four regression models, and tests the VPIN-liquidity link with two Vector Auto-Regression (VAR) models over four high-frequency liquidity benchmarks, followed by Granger causality tests and impulse-response analysis.

BV-VPIN gave the earliest and most stable warning ahead of both events, crossing a CDF value of 0.8 about 15 minutes before the Fat Finger Event's 5.62% price spike and staying elevated through the plunge, while TR-VPIN and LR-VPIN were unstable or lagged the event. VPIN's prior level correlates positively with subsequent volatility, and the VAR/Granger-causality results show a two-way feedback: prior liquidity changes Granger-cause VPIN changes, and prior VPIN changes Granger-cause further liquidity changes, consistent with market makers widening spreads and withdrawing when order flow looks toxic, which then pushes VPIN higher still.

The thesis presents this as the first out-of-sample test of VPIN outside the U.S. and Spanish markets on which it had previously been evaluated, and as the first formal empirical test (via VAR, Granger causality and impulse response) of the theorized feedback loop between order-flow toxicity and liquidity, rather than only a one-directional VPIN-to-volatility link.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

VPIN is computed on a volume clock: trading is split into fixed-size volume buckets (bucket size = average daily volume divided by 50), and each bucket's volume is classified as buy- or sell-initiated by one of three algorithms (Bulk Volume Classification, Tick Rule, Lee-Ready). VPIN is the average absolute order imbalance over a rolling window of buckets, the 'sample length' (e.g. 50 buckets for a daily VPIN, 250 buckets for a five-day VPIN). Robustness checks vary the underlying time-bar length (1 or 5 minutes) used to build the bars that are then grouped into buckets. The 'forecast' is intraday: whether the VPIN CDF crosses a high threshold minutes before a price crash, not a fixed-horizon return prediction.

## Data

- **Asset class:** Futures
- **Instruments:** China Shanghai Shenzhen 300 Stock Index Futures (front-month contracts)
- **Venue:** China Financial Futures Exchange; data collected from the China Shanghai Stock Exchange
- **Period:** January 2012 to December 2013 (2-year sample)
- **Granularity:** 500 microsecond tick data, aggregated into 1-minute (and, in robustness checks, 5-minute) time bars, then grouped into volume buckets sized at average daily volume divided by 50 (about 9248 shares).

## Features and Measures

- **BV-VPIN (Bulk Volume VPIN).** VPIN computed with Bulk Volume Classification, which assigns each time bar's volume fractionally to buys and sells using the normal-CDF of the standardized price change over the bar, rather than signing individual trades.
- **TR-VPIN (Tick Rule VPIN).** VPIN computed with the tick rule, which classifies a trade as buyer- or seller-initiated by whether its price is above or below the immediately preceding trade price.
- **LR-VPIN (Lee-Ready VPIN).** VPIN computed with the Lee-Ready algorithm, a level-2 rule that classifies a trade relative to the midpoint of the prevailing bid and ask quotes rather than only the prior trade price.
- **Order imbalance (OI).** The absolute difference between classified buy volume and sell volume within a time bar, used as the building block that VPIN averages over a rolling window of volume buckets.
- **High-frequency liquidity benchmarks.** Four measures of intraday illiquidity used alongside VPIN: the effective spread, the realized spread, the quoted spread, and price impact.

## Method

VPIN is built on the PIN (probability of informed trading) framework, replacing PIN's daily maximum-likelihood estimate with a rolling measure computed on volume buckets. All three trade-classification algorithms (BV, TR, LR) feed the same four-step VPIN calculation: form time bars, assign volume buckets, classify buy/sell volume and compute order imbalance, then average the imbalance over a rolling sample length. BV-VPIN's stability is checked across eight combinations of time-bar length, bucket count and sample length.

To test the VPIN-volatility hypothesis, the thesis computes Pearson correlations between lagged VPIN and two volatility proxies (market risk and absolute return), builds conditional-probability tables of returns given VPIN percentile bins and vice versa, and estimates four OLS regressions of volatility on lagged VPIN, controlling for lagged trade intensity and lagged volatility.

To test the VPIN-liquidity hypothesis, the thesis first runs an Augmented Dickey-Fuller unit-root test to confirm stationarity, then estimates two Vector Auto-Regression models (one with VPIN and each of the four liquidity benchmarks, one adding market volatility as a third variable) with a lag length of 2 chosen by AIC/SC. Granger causality tests on the VAR coefficients establish the direction of predictability, and impulse-response functions trace out how a shock to liquidity propagates to VPIN and back.

## Results

- BV-VPIN's CDF crossed 0.8 about 15 minutes before the Fat Finger Event's 5.62% price spike and stayed high through the afternoon plunge; TR-VPIN and LR-VPIN gave unstable or late signals for the same event.
- In the Money Shortage Event, BV-VPIN rose above 0.9 before the market's 7.1% plunge (from 2296 to 2133) and stayed high, while TR-VPIN and LR-VPIN did not show a stable early rise.
- BV-VPIN's behaviour was stable across eight combinations of time-bar length, bucket size and sample length, with mean VPIN values in the same range as prior studies (e.g. a mean of 0.2961 for the Chinese 1-50-50 series versus 0.2251 in the U.S. and 0.2268 in the Spanish market).
- Prior VPIN correlates positively with current market risk (correlation 0.1174) and current absolute return (correlation 0.0872), both significant at the 1% level.
- Conditional-probability analysis: when VPIN is below the 50th percentile, about 85% of subsequent absolute returns stay below 0.5%; when absolute returns exceed the 1.50% mark, about 90% of the preceding VPIN values are above the 60th percentile.
- Four regression models confirm that prior VPIN positively and significantly (1% level) predicts current market risk and absolute return, robust to controlling for lagged trade intensity and lagged volatility.
- VAR and Granger causality tests show a two-way feedback: prior liquidity changes Granger-cause VPIN changes (coefficients around 0.011 to 0.036) and prior VPIN changes Granger-cause liquidity changes (coefficients around 0.025 to 0.044), both significant at the 1% level.
- Impulse-response analysis: a liquidity shock raises VPIN, peaking around period four at an impulse-response value of 0.03, while a VPIN shock raises illiquidity, peaking near period two at an impulse-response value of 0.01, consistent with a feedback loop between order-flow toxicity and market-maker withdrawal.

## Limitations

- Reader note: the analysis covers only two volatile episodes on one market (Chinese Stock Index Futures), so the ranking of VPIN algorithms and the size of the estimated feedback effect may not generalize to other markets or event types.
- Reader note: BV-VPIN and TR-VPIN use only trade-price data; the thesis notes there is no venue-provided signed-trade benchmark (like the US's IMET) for the Chinese market, so the true buy/sell split cannot be directly verified against the classification algorithms.
- The thesis itself frames its Chinese-market results as one side of an ongoing, unresolved dispute (citing Andersen and Bondarenko's contrary findings on VPIN's predictive power), rather than as a definitive resolution of whether VPIN forecasts volatility.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]

## Citation

Jinzhi Jiang (2015). Volume-Synchronized Probability of Informed Trading (VPIN), Market Volatility, and High-Frequency Liquidity. Goodman School of Business, Brock University (MSc in Management thesis).

Text ingested: `markdown_output/jiang-2015-volume-synchronized-probability-informed-trading-vpin.md`, converted from `raw/ofi-event-clock/jiang-2015-volume-synchronized-probability-informed-trading-vpin.pdf`.

Coverage of this summary: Read the abstract, introduction, the testable-hypotheses section, the full methodology section (VPIN construction and the volatility and liquidity models), the sample-data and descriptive-statistics section, the entire empirical-results section, and the conclusion; the literature review was read at section-heading and topic-sentence level rather than in full.

Known problems with the input: year from file metadata (no publication/submission year is printed in the converted text; year taken from job file year_hint); no journal/venue name beyond the university is printed for this thesis; several equations (VPIN formula, order-imbalance formula, VAR model equations) are rendered as omitted picture placeholders in the converted markdown, so their exact algebraic form could not be verified from this file.
<!-- AUTHORED REGION END -->