---
authors:
- Torben G. Andersen
- Oleg Bondarenko
content_hash: sha256:97d8275fbe51348408d149074d744fcfdd1e34150c8c73883339b078f08e0e5c
created: 2026-09-27 01:47:00+00:00
page_id: sources/andersen-2013-assessing-measures-order-flow-toxicity-early
page_type: source
related:
- concepts/sampling-clocks
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/trade-classification
- concepts/informed-trading
- concepts/adverse-selection
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/vpin
- concepts/bulk-volume-classification
- concepts/volume-clock
revision_id: 1
schema_version: 2
source_hash: sha256:e8b085c82180309f56e2290c55683d64501cd410453521f068c5532e5784b1ad
source_path: markdown_output/andersen-2013-assessing-measures-order-flow-toxicity-early.md
source_type: paper
tags:
- vpin
- trade-classification
- order-flow-toxicity
- e-mini-sp500
- flash-crash
- volatility-forecasting
- volume-bucketing
- clock-compares
- asset-futures
- harvest-core
title: Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market
  Turbulence
updated: '2026-09-27T01:47:00Z'
uuid: 44494bc0-b6f9-5287-9f28-fb985e2bf451
year: 2014
---

<!-- AUTHORED REGION START -->
# Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market Turbulence

## Summary

The paper asks whether VPIN, a metric introduced by Easley, Lopez de Prado and O'Hara that tracks a rolling average of order-flow imbalance over volume buckets, genuinely measures toxic (informed) order flow and can warn of episodes like the May 2010 flash crash, or whether its apparent forecasting power is instead an artifact of how trades get classified into buys and sells.

Using five years of tick-by-tick best-bid-offer records for the CME E-mini S&P 500 futures contract, the authors build a near-perfect benchmark for the true buy or sell side of each trade by comparing transaction prices to the prevailing quotes. They compare this benchmark against the tick rule and against Easley-Lopez de Prado-O'Hara's Bulk Volume Classification (BVC) scheme, always at matched levels of order-flow aggregation (individual transactions, several time-bar lengths, and two volume-bar sizes). They also redesign the volume-bucket size to track a trailing one-month average of trading volume, removing distortion caused by the strong upward trend in E-mini volume over the sample.

Classification accuracy is always better for less-aggregated data, and the plain tick rule applied trade-by-trade is markedly more accurate than any BVC variant at the same aggregation level, reversing an earlier claim that BVC dominates. VPIN computed from the accurate benchmark, or from the tick rule, is negatively related to future volatility, while VPIN computed from BVC on time or volume bars is positively related to volatility, but only because the BVC scheme's classification errors are themselves correlated with trading volume and volatility. Once lagged realized volatility is added to the forecasting regression, BVC-VPIN's coefficient becomes insignificant; the causal relationship runs from past volatility to VPIN, not the reverse.

Unlike earlier VPIN studies, this analysis has an observable, near-exact ground truth for trade direction. That lets the authors show directly that prior accuracy comparisons mixed bar-level BVC accuracy with transaction-level tick-rule accuracy and were therefore invalid, and that VPIN's apparent forecasting power for volatility, including around the flash crash, is fully explained by conventional volume and volatility measures rather than by order-flow toxicity.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper builds VPIN as a trailing moving average, over the most recent 50 volume buckets, of the absolute proportional buy/sell imbalance in each bucket; buckets are sized to 1/50 of the trailing one-month average daily volume, restarted at the start of each trading day. It systematically compares this against alternative aggregation units for classifying trade direction: individual transactions, fixed calendar-time bars (1, 10, 60, and 300 seconds), and fixed-size volume bars (2% and 10% of a bucket). The prediction horizon studied is 5-minute-ahead and 1-day-ahead average absolute one-minute returns.

## Data

- **Asset class:** Futures
- **Instruments:** E-mini S&P 500 futures contract (front-month, rolled 8 days before expiry)
- **Venue:** CME Group / Chicago Mercantile Exchange, traded on the CME Globex electronic platform
- **Period:** February 10, 2006 to March 22, 2011
- **Granularity:** Tick-by-tick best-bid-offer (BBO) records timestamped to the second, with a sequence indicator giving sub-second event ordering; aggregated into volume buckets sized to roughly 1/50 of a trailing month's average daily volume.

## Features and Measures

- **VPIN.** A trailing moving average, over 50 volume buckets, of the absolute proportional order imbalance, used as a real-time gauge of order flow toxicity.
- **Signed order imbalance (OI).** The proportional difference between active buy and sell volume within a volume bucket or bar, the building block used to construct VPIN.
- **Bulk Volume Classification (BVC).** A trade-classification rule that assigns the proportion of buy volume in a bar as a function of the bar's price change scaled by the standard deviation of price changes, rather than classifying individual trades.
- **Tick rule.** Classifies a bar or trade as a buy or sell based on the sign of the price change relative to the previous trade or bar.
- **Order book matching (actual classification).** Classifies each trade as a buy or sell by comparing the trade price to the prevailing best bid and ask from the BBO record, providing a near-exact ground truth for trade direction.
- **Misclassification measure (MC/MB).** Quantifies the discrepancy between a candidate scheme's inferred buy volume and the actual buy volume, computed either at the individual-contract level (MC) or the volume-bucket level (MB).

## Method

The authors build an accurate benchmark trade-classification series (ACT) from CME BBO quote-and-trade sequencing, then construct many variants of VPIN by crossing four trade-classification rules (actual, tick rule, BVC with unconditional volatility, BVC with conditional volatility) with three data-aggregation choices (individual transactions, time bars at four frequencies, volume bars at two sizes). They regularize the metric by detrending the volume-bucket size against a trailing one-month average daily volume and by restarting the bucket count each trading day, to remove distortions from the long-run rise in E-mini trading volume.

Performance is judged in two ways. First, misclassification rates for each scheme are computed against the accurate benchmark, both at the individual-contract level and at the volume-bucket level, to test whether more aggregated schemes are genuinely more accurate. Second, OLS predictive regressions of future 5-minute and 1-day average absolute returns on each VPIN variant, with and without controls for trading volume, the VIX, and realized volatility (RV), are estimated with HAC standard errors, including a two-stage regression that decomposes VPIN into a component predicted by lagged RV and a residual component to test for reverse causality.

## Results

- The tick rule applied to individual transactions misclassifies 11.6% of trades, far better than any Bulk Volume Classification (BVC) variant, reversing an earlier claim that BVC is more accurate than the tick rule.
- Order flow aggregation mechanically improves classification accuracy for every scheme (error diversification), so classification rules must be compared at matched aggregation levels rather than across levels.
- The time-bar BVC scheme closest to the original ELO implementation (60-second bars) misclassifies 23.2% of transactions, roughly double the 11.6% rate of the transaction-level tick rule.
- VPIN computed from the actual or tick-rule order imbalance is negatively correlated with future return volatility, whereas VPIN computed from BVC on time or volume bars is strongly positively correlated with volatility.
- Once lagged realized volatility is included as a predictor, the BVC-VPIN measure's coefficient becomes statistically insignificant, showing it has no incremental power to forecast future volatility beyond standard volume and volatility measures.
- The positive relationship between BVC-VPIN and future volatility largely reflects reverse causality: past realized volatility predicts future VPIN rather than VPIN predicting volatility.
- On May 6, 2010 (the flash crash), VPIN built from the actual order imbalance stayed flat or fell rather than rising in advance of the event, while the BVC-based VPIN spiked only after the crash began, coinciding with a sharp deterioration in BVC's classification accuracy.
- Under the paper's volume-detrended bucketing method, the sample maximum of the BVC-VPIN metric occurs on February 27, 2007, not on the day of the flash crash in 2010.

## Limitations

- The analysis is confined to a single futures contract (the E-mini S&P 500) traded on one venue (CME Globex).
- The authors identify but do not fully explain the mechanism behind the negative correlation between actual VPIN and future volatility (linked qualitatively to falling average trade size and faster buy/sell alternation), leaving it for future research.
- Reader note: findings on classification accuracy and VPIN behavior are established for one liquid index-futures contract and may not generalize to equities or less liquid instruments.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]
- [[concepts/volume-clock|Volume Clock]]

## Citation

Torben G. Andersen, Oleg Bondarenko (2014). Assessing Measures of Order Flow Toxicity and Early Warning Signals for Market Turbulence.

DOI: 10.2139/ssrn.2292602

Text ingested: `markdown_output/andersen-2013-assessing-measures-order-flow-toxicity-early.md`, converted from `raw/ofi-event-clock/andersen-2013-assessing-measures-order-flow-toxicity-early.pdf`.

Coverage of this summary: Read the full text: abstract, introduction, data section, VPIN construction and notation, bucket regularization, misclassification measures and empirical results, predictive regressions, the flash-crash event study, the discussion of why actual VPIN and volatility are negatively correlated, and the conclusion; the web appendix's step-by-step VPIN pseudocode (which restates the main-text algorithm) was skimmed rather than read in full.

Known problems with the input: The paper carries two dates ('This version: June 2014', 'First version: March 2013'); the year field uses the later 'this version' date (2014); Many equations and figures are rendered as omitted images/tables in the markdown conversion (e.g. the VPIN formula, the BVC rule, the misclassification-measure formulas), so some formal definitions are described qualitatively rather than reproduced exactly; Several data tables (e.g. Table 1, Table 3) are OCR-garbled or collapsed in the markdown conversion; numbers from those tables were used only when independently confirmed in the surrounding prose.
<!-- AUTHORED REGION END -->