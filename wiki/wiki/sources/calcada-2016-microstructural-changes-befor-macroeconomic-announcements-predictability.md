---
authors:
- Rita Dias Barreto Calçada
content_hash: sha256:be7b63752c2f726b6218d6ecf447f99960ba208c0a63d131ce95ba57fe51e9d9
created: 2026-09-27 01:47:00+00:00
page_id: sources/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability
page_type: source
publication_venue: NOVA – School of Business and Economics (Work Project, Master in
  Finance Program)
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/trade-classification
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/adverse-selection
- concepts/vpin
- concepts/queue-imbalance
revision_id: 1
schema_version: 2
source_hash: sha256:49693d781400a01f3b099585720fa248cbf86b196696d8df26e366cf5b18abe7
source_path: markdown_output/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability.md
source_type: paper
tags:
- vpin
- macro-announcements
- order-flow-imbalance
- depth-imbalance
- informed-trading
- event-study
- treasury-futures
- sp500-futures
- clock-volume
- asset-multi
- harvest-core
title: 'Microstructural changes before Macroeconomic Announcements: Predictability
  of Economic Surprises in the U.S. market'
updated: '2026-09-27T01:47:00Z'
uuid: f21fed33-5356-505a-a6c7-55ebd74fab9b
year: 2015
---

<!-- AUTHORED REGION START -->
# Microstructural changes before Macroeconomic Announcements: Predictability of Economic Surprises in the U.S. market

## Summary

This Master's thesis Work Project asks whether microstructural order-flow measures observed just before scheduled U.S. macroeconomic data releases can predict whether the release will surprise positively or negatively relative to consensus, extending the informed-trading literature to the specific window around news announcements.

Standardized surprises for 14 announcements (the realized value minus the Bloomberg median forecast, divided by a rolling 20-day standard deviation of past surprises) are first regressed on the price change of S&P 500 futures and 10-year Treasury futures 1, 5, 15 and 60 minutes after release, to identify which announcements move each asset most. The study then computes the Volume-Synchronized Probability of Informed Trading (VPIN) from tick data using volume buckets, classifying trades with either the tick rule or the Bulk Volume Classification, and separately computes a bid-ask depth imbalance (DI) from the first level of the order book; both are tested as predictors of the sign of the pre-identified relevant announcements using OLS and probit regressions on an in-sample and out-of-sample split.

VPIN calculated on the S&P is found to have some predictive power over economic surprises, corroborated by the depth-imbalance measure, whereas Treasury-based VPIN performs worse; days with relevant announcements show a higher average VPIN and more filled volume buckets than other days, and an out-of-sample strategy that only trades when VPIN signals a negative surprise achieves 100% correct sign predictions for the S&P, though on only 4 signals.

The contribution is attempting to predict the surprise itself rather than only the market's reaction to it, using order-flow toxicity measures, and comparing VPIN's usefulness against a bid-ask depth-imbalance measure evaluated in the same pre-announcement window.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

VPIN divides each trading morning into fixed-size volume buckets (B = 40 for the S&P future, B = 15 for the 10-year Treasury future) and computes order imbalance per bucket from buy/sell-classified volume, averaging the last n = 1 bucket to obtain a value just before an announcement. The depth-imbalance metric instead samples best-bid and best-ask depth to the nearest second. The prediction target is the sign of the economic surprise at the announcement; separate price-impact regressions are run over fixed 1, 5, 15 and 60 minute horizons after release.

## Data

- **Asset class:** Several asset classes
- **Instruments:** S&P 500 futures and 10-year U.S. Treasury futures
- **Venue:** not stated (Bloomberg-sourced minute-bar and tick data; specific exchange not named)
- **Period:** Minute-bar sample: S&P 500 futures from 30 September 2007 and 10-year Treasury futures from 10 June 2007, both through end of March 2015. Tick data: 3 April 2015 to 23 November, split into in-sample (through 31 August) and out-of-sample (from 1 September) periods.
- **Granularity:** Minute bars for the initial event-study regressions; tick-level trade and order-book data (price, volume, best bid/ask and depth) to the nearest second for VPIN and DI construction.

## Features and Measures

- **VPIN (Volume-Synchronized Probability of Informed Trading).** An order-flow toxicity measure computed as the rolling average of absolute order imbalance across volume buckets, where each bucket's buy/sell split is estimated from price changes via the tick rule or Bulk Volume Classification.
- **Depth Imbalance (DI).** The log of best-bid depth minus the log of best-ask depth, sampled to the nearest second, used as a limit-order-book based proxy for liquidity pressure.
- **Standardized economic surprise.** The realized value of a macro indicator minus its Bloomberg median forecast, divided by the rolling 20-day sample standard deviation of past surprises for that indicator.
- **Order Imbalance (OI).** Within a volume bucket, the absolute difference between buy-initiated and sell-initiated volume, used as the input to the VPIN calculation.

## Method

The study first runs OLS regressions of price changes 1, 5, 15 and 60 minutes after release on the standardized surprise for each of 14 U.S. macro announcements, separately for the S&P 500 future and the 10-year Treasury future, to find which announcements have the largest and most significant impact (highest R2); those announcements define the 'days with relevant economic releases' used in the rest of the analysis.

VPIN is built by splitting each trading morning into volume buckets (B = 40 for the S&P, B = 15 for the Treasuries), classifying trades as buyer- or seller-initiated with the tick rule or the Bulk Volume Classification, computing the order imbalance per bucket, and averaging the last n = 1 bucket to obtain the VPIN value just before an announcement. Predictive power is tested with an OLS regression of the standardized surprise on the last pre-announcement VPIN value and with a probit regression of a negative-surprise indicator on VPIN, with the same regressions repeated for the depth-imbalance metric; thresholds for a trading rule are set in-sample and then applied out-of-sample, with strategy profitability measured over 5-minute and 1-hour holding periods.

## Results

- VPIN is higher on days with relevant economic releases than on other days for both the S&P (mean 0.2899 versus 0.2650 across all 14 announcements) and the Treasuries (0.1686 versus 0.1288)
- Regressing surprises on the last pre-announcement VPIN value gives beta -2,10 (SE 1,27, pValue 11,05%, R2 10,70%) for the S&P and beta -3,21 (SE 1,67, pValue 6,16%, R2 8,46%) for the Treasuries
- In-sample, an S&P VPIN threshold of 0.12 correctly signs 73.91% of surprises, and a Treasuries threshold of 0.13 signs 65.85% correctly
- Out of sample, the S&P VPIN threshold predicts the surprise direction with 71.43% accuracy over 14 observations, versus 56.52% accuracy over 23 observations for the Treasuries
- Trading only when VPIN signals a negative surprise, the S&P strategy is correct 100% of the time (only 4 signals above threshold), while the Treasuries version is correct 42,86% of the time
- Holding the VPIN-threshold position for 1 hour returns 1,63%(0,2507) for the S&P and 2,03%(0,0401) for the Treasuries, while the 5-minute holding period loses -0,97% (-0,0840) on the S&P and -3,24% (-0,0156) on the Treasuries
- For depth imbalance, the strongest fit is 10 seconds before the announcement for the S&P (R2 7,15%, pValue 17,77%) and 25 seconds before for the Treasuries (R2 7,22%, pValue 6,20%)

## Limitations

- Reader note: this is an unpublished Master's thesis (Work Project), not peer-reviewed.
- Sample sizes for the out-of-sample threshold test are small (14 S&P observations, 23 Treasury observations), and the fully-correct negative-surprise S&P result rests on only 4 signals.
- The bucket-count parameters (B and n) were tuned in-sample by re-running the regression until explanatory power was highest, which risks overfitting the parameters to the same sample used to evaluate them.
- Depth imbalance is measured only at the first level of the order book and only for a short window before the announcement, so deeper-book information is not used.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/vpin|VPIN]]
- [[concepts/queue-imbalance|Queue Imbalance]]

## Citation

Rita Dias Barreto Calçada (2015). Microstructural changes before Macroeconomic Announcements: Predictability of Economic Surprises in the U.S. market. NOVA – School of Business and Economics (Work Project, Master in Finance Program).

Text ingested: `markdown_output/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability.md`, converted from `raw/ofi-event-clock/calcada-2016-microstructural-changes-befor-macroeconomic-announcements-predictability.pdf`.

Coverage of this summary: Read the full thesis text: abstract, introduction/literature review, data section, methodology (VPIN and DI construction), full results and discussion, conclusion, references, and all appendix tables of regression results.

Known problems with the input: Appendix 2 (Treasury announcement regressions) is OCR-corrupted: category labels such as 'Investment', 'Prices' and 'Sales' appear garbled ('InvTYtment', 'PricTY', 'JoblTYs'), which made a few individual coefficient-to-announcement mappings unreliable and those specific numbers were not used; The Figure 1 announcement-time schedule renders in the markdown as a garbled, duplicated table and was not used; Numeric tables in this document mix comma and period decimal separators inconsistently (likely a PDF-to-markdown conversion artifact); each number above is copied exactly as it appears in its own source table.
<!-- AUTHORED REGION END -->