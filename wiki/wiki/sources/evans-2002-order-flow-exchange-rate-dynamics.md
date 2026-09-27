---
authors:
- Martin D. D. Evans
- Richard K. Lyons
content_hash: sha256:4eef7e4d08149d52ef1fe1399125b4d5ca98664a801f7cd02e8157aea15e8e4b
created: 2026-09-27 01:47:00+00:00
page_id: sources/evans-2002-order-flow-exchange-rate-dynamics
page_type: source
publication_venue: NBER Working Paper Series (Working Paper 7317)
related:
- concepts/order-flow
- concepts/market-microstructure
- concepts/price-impact
- concepts/informed-trading
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:9bf4d761ddbe4daca48c4d5a86ad277ee854d1d382898515f857c9cd82dcbd67
source_path: markdown_output/evans-2002-order-flow-exchange-rate-dynamics.md
source_type: paper
tags:
- order-flow
- exchange-rates
- market-microstructure
- price-impact
- dealer-market
- daily-frequency
- out-of-sample-forecasting
- clock-calendar
- asset-fx
- harvest-relevant
title: Order Flow and Exchange Rate Dynamics
updated: '2026-09-27T01:47:00Z'
uuid: 9e82ba41-d59a-5ecd-aac1-36fb76e0be14
year: 1999
---

<!-- AUTHORED REGION START -->
# Order Flow and Exchange Rate Dynamics

## Summary

Exchange-rate economics has struggled since Meese and Rogoff (1983) to explain nominal rates with macroeconomic fundamentals, and macro models are typically beaten out-of-sample by a random walk. The paper asks whether a microstructure variable -- order flow, the net of buyer- and seller-initiated trades -- can do better, since order flow is the proximate driver of price in microstructure models but has no role in macro models that treat information as common knowledge.

The authors build a three-round dealership (Portfolio Shifts) model in which non-public customer portfolio shifts are revealed to the market only through the interdealer order flow dealers observe, and specialize it into a daily estimating equation with the change in the interest differential and daily order flow as regressors. They estimate this on four months of tick-by-tick interdealer transaction data for DM/$ and Yen/$ from the Reuters D2000-1 system (May-August 1996).

The main finding is that daily order flow accounts for most of the daily variation in both exchange rates, with in-sample R2 far above what macro models achieve, and that the order-flow coefficient is robust to nonlinearity, activity-level, and day-of-week checks. Causality tests (lagged order flow, lagged price changes, and a bias-decomposition analysis) support order flow driving price rather than the reverse. Out of sample, the model beats a random-walk benchmark on short-horizon forecasts.

What is new is the demonstration that a microstructure variable, aggregated to a daily frequency rather than the usual transaction frequency, can bridge the 'missing middle' between tick-by-tick microstructure models and monthly macro models, offering both strong in-sample fit and improved out-of-sample forecasts at horizons where macro models have historically failed.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

All variables are aggregated to a fixed 24-hour trading day (4pm GMT to 4pm GMT, with weekends folded into the following Monday). Order flow for a day is the difference between the number of buyer-initiated and seller-initiated interdealer trades that day (a trade count, not dollar volume); the dependent variable is the daily log change in the spot rate from one day's 4pm price to the next; the interest-differential regressor is the daily change in the overnight interest-rate spread. Out-of-sample forecasts use recursively estimated models to predict 1-day, 1-week, and 2-week-ahead spot-rate changes using realized future order flow and interest-differential values.

## Data

- **Asset class:** Foreign exchange
- **Instruments:** DM/$ and Yen/$ spot exchange rates
- **Venue:** Reuters Dealing 2000-1 (D2000-1) interdealer electronic trading system
- **Period:** May 1, 1996 to August 31, 1996 (89 trading days)
- **Granularity:** Tick-by-tick, time-stamped interdealer transactions (bought/sold indicator, no trade size) aggregated to daily order flow and daily spot-rate changes

## Features and Measures

- **Order flow.** The net of buyer-initiated minus seller-initiated trades in a currency, cumulated over a day; a positive value means net dollar purchases.
- **Portfolio Shifts model.** A three-round dealership model in which non-public customer portfolio shifts in round one are revealed to the market only through observed interdealer order flow in round two, and dealers then adjust the round-three price so the public re-absorbs the shift.
- **Interest differential.** The change in the overnight nominal interest-rate gap between the dollar and the non-dollar currency (DM or Yen), used as the model's macroeconomic determinant.

## Method

The paper develops a three-round dealership (Portfolio Shifts) model in which unobserved customer portfolio shifts in round one are revealed to dealers only through the interdealer order flow they observe at the end of round two; this order flow is a sufficient statistic for the aggregate portfolio shift, so round-three prices adjust to induce the public to re-absorb it. The model is specialized to an estimating equation with the daily change in the log spot rate as the dependent variable and the daily change in the interest differential and daily order flow as regressors, estimated by OLS with heteroskedasticity-corrected standard errors where needed.

Robustness is checked with squared and kinked (asymmetric) order-flow terms, sub-samples by transaction-activity quartile and by day of week, and specifications in levels rather than changes. Causality is examined by testing lagged order flow and lagged price changes in the regression (Anticipation and Feedback hypotheses), and by a bias-analysis decomposition of measured order flow into a portfolio-shift component and a feedback-trading component under alternative assumed ratios of common-knowledge news to order-flow news. Out-of-sample forecast accuracy is judged by root mean squared error (RMSE) of recursive model forecasts against a random-walk benchmark at 1-day, 1-week, and 2-week horizons.

## Results

- The in-sample regression of daily exchange-rate changes on the interest differential and order flow yields R2 statistics of 64 percent for the DM/$ equation and 45 percent for the Yen/$ equation, far higher than typical macro-model fits.
- The order-flow coefficient is 2.1 in the DM equation, with t-statistics above 5 in both equations; the interest-differential coefficient is correctly signed but significant only in the Yen equation.
- For the DM/$ market as a whole, $1 billion of net dollar purchases is estimated to raise the DM price of a dollar by about 0.8 pfennig (rounded to about 1 pfennig in the abstract).
- Regressing exchange-rate changes on the interest differential alone (dropping order flow) produces an R2 below 1 percent in both equations, showing the explanatory power comes almost entirely from order flow.
- Out-of-sample, the Portfolio Shifts model's root mean squared forecast error is 30 to 40 percent lower than a random walk at 1-day, 1-week, and 2-week horizons, though the outperformance is not statistically significant at the 1-week and 2-week horizons given the short 89-day sample.
- Neither lagged order flow nor lagged price changes are significant once added to the regression, arguing against both a delayed-anticipation and a positive-feedback-trading explanation for the order-flow/price relation.
- A bias analysis shows that treating the order-flow coefficient as spurious (driven by positive feedback trading) would require common-knowledge news to be one to two orders of magnitude larger than order-flow news, which the authors judge implausible.

## Limitations

- Sample spans only four months (May-August 1996) with 89 trading days, giving the out-of-sample tests low statistical power at the 1-week and 2-week horizons.
- Order flow is measured only for interdealer trades on one system (Reuters D2000-1); customer-dealer and brokered interdealer trades are not observed, so the order-flow measure is described by the authors as incomplete.
- Individual trade sizes are not observable in the data, so order flow is measured as a net trade count (in thousands) rather than net dollar volume.
- The model and estimates cover two currency pairs (DM/$ and Yen/$) only.
- Reader note: the paper itself flags as an open question whether order flow's relation to price would change if the market were more transparent (order flow fully observable to dealers in real time).

## Related

- [[concepts/order-flow|order flow]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/price-impact|price impact]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Martin D. D. Evans, Richard K. Lyons (1999). Order Flow and Exchange Rate Dynamics. NBER Working Paper Series (Working Paper 7317).

DOI: 10.1086/324391

Text ingested: `markdown_output/evans-2002-order-flow-exchange-rate-dynamics.md`, converted from `raw/ofi-event-clock/evans-2002-order-flow-exchange-rate-dynamics.pdf`.

Coverage of this summary: Read the entire converted markdown from the abstract through the reference list, including the model derivation (Sections 2-3), data description (Section 4), all empirical-results subsections (Section 5.1-5.4), the discussion (Section 6), the conclusion (Section 7), and skimmed the appendix model-solution proofs.

Known problems with the input: This document is the August 1999 NBER working paper (No. 7317); the job's slug and year hint (2002) appear to refer to a later published version, which is not the text analyzed here. The year field uses 1999 as printed in this document; Most equations, Figure 1, and the regression tables (Tables 1-4) are rendered as omitted pictures or reflowed/garbled table markup in the markdown conversion; numeric results are drawn from the surrounding prose wherever the table cells themselves are ambiguous.
<!-- AUTHORED REGION END -->