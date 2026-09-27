---
authors:
- Makoto Takahashi
content_hash: sha256:50da4a08d574dd2485250094ee9ea232ce8f12fd5e1842742dd32ea6088dcac3
created: 2026-09-27 01:47:00+00:00
page_id: sources/takahashi-2025-returns-order-flow-imbalances-intraday-dynamics
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/order-flow
- concepts/bid-ask-spread
revision_id: 1
schema_version: 2
source_hash: sha256:af5b644e428d3050be629747ef43216cf023ed2189d7fdbe45e71b439ae88b77
source_path: markdown_output/takahashi-2025-returns-order-flow-imbalances-intraday-dynamics.md
source_type: paper
tags:
- order-flow-imbalance
- price-impact
- market-microstructure
- structural-var
- intraday-patterns
- macro-news-announcements
- futures
- clock-calendar
- asset-futures
- harvest-relevant
title: 'Returns and Order Flow Imbalances: Intraday Dynamics and Macroeconomic News
  Effects'
updated: '2026-09-27T01:47:00Z'
uuid: f925e573-82b8-5dc0-a4b1-37c77f1391c0
year: 2025
---

<!-- AUTHORED REGION START -->
# Returns and Order Flow Imbalances: Intraday Dynamics and Macroeconomic News Effects

## Summary

The paper studies the two-way interaction between returns and order flow imbalance (OFI) in the S&P 500 E-mini futures market, aiming to jointly capture the endogeneity between prices and order flow and the strong intraday variation documented separately in prior literature. It builds on Deuskar and Johnson (2011) and on Fleming, Mizrach and Nguyen (2018), extending their simultaneous-equations approach to a full structural VAR re-estimated many times across the trading day.

Using one-second best-bid-offer data on the S&P 500 E-mini from 2008 to 2013, the author constructs order flow imbalance following Cont, Kukanov and Stoikov (2014) and estimates a bivariate structural VAR of returns and OFI, identified through heteroskedasticity (the ITH method of Rigobon, 2003): the residual variance-covariance matrix is allowed to differ across three nested five-minute sub-windows within each 15-minute estimation block, over-identifying the system and allowing generalized-method-of-moments estimation of the contemporaneous price-impact and flow-impact coefficients, plus impulse response functions.

Macroeconomic news announcements sharply reshape the return-flow relationship: price impact rises and flow impact falls around news releases, while return-innovation volatility spikes and flow-innovation volatility falls, consistent with a temporary withdrawal of liquidity. Pooling across all estimated 15-minute intervals, both price impact and flow impact are significant much of the time and are larger, respectively smaller, than the levels reported by Deuskar and Johnson (2011) using coarser one-minute data. Impulse responses show that almost all of the return-flow interaction dissipates within about one second, and both structural parameters and innovation volatilities vary strongly across the trading day in ways tied to depth, order activity, and spreads.

The main contribution is combining, in one framework, the identification-through-heteroskedasticity treatment of simultaneity with a systematic account of intraday variation and of macro-announcement effects, at a much finer (one-second) sampling frequency than prior studies of this kind.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Mid-quote returns and order flow imbalance are aggregated into fixed one-second wall-clock intervals from best-bid-offer data. The structural VAR is then re-estimated separately for each 15-minute window of the trading day (with three nested five-minute sub-windows used for the innovation-volatility parameters), so the prediction horizon of interest is the same one-second interval for contemporaneous impacts, extended to up to ten one-second lags for impulse responses.

## Data

- **Asset class:** Futures
- **Instruments:** S&P 500 E-mini futures (CME Group), most-active contract selected each trading day
- **Venue:** CME Group (best-bid-offer data)
- **Period:** 1,490 trading days from January 2, 2008 to December 31, 2013
- **Granularity:** One-second best-bid-offer data during 8:30-15:00 Chicago time, with the model re-estimated separately for each 15-minute (and nested 5-minute) interval of the day.

## Features and Measures

- **order flow imbalance (OFI).** A one-second aggregate of best-bid and best-ask price and size changes, following Cont, Kukanov and Stoikov (2014), measuring net buying versus selling pressure implied by limit-order-book updates at the best quotes.
- **depth.** The average of bid and ask sizes around price changes within a one-second interval, used as an inverse liquidity proxy whose reciprocal enters regressions of the structural parameters.
- **price impact ($b_r$) and flow impact ($b_f$).** Structural-VAR coefficients where $b_r$ is the contemporaneous effect of order flow on returns (illiquidity), and $b_f$ is the reverse contemporaneous feedback of returns on order flow, reflecting endogeneity from price-contingent trading.

## Method

Returns and order flow imbalance are modeled jointly as a bivariate structural VAR (SVAR) at one-second frequency, extending the simultaneous-equations approach of Deuskar and Johnson (2011). Because the contemporaneous price-impact and flow-impact coefficients are not separately identified from the reduced-form residual covariance alone, identification is achieved through heteroskedasticity (the ITH method of Rigobon, 2003): the residual variance-covariance matrix is allowed to differ across three nested five-minute states within each 15-minute estimation window, giving an over-identified system solved by generalized method of moments. The SVAR is estimated separately for each 15-minute interval of each trading day, with lag order chosen by the Akaike information criterion, yielding a cross-section of structural-parameter and innovation-volatility estimates that are then related to market-activity variables (depth, number of events, average event size, spread) and to macroeconomic-announcement dummies via panel regressions with standard errors clustered by date.

## Results

- Price impact $b_r$ averages 0.834 and is statistically significant in 64% of the 37,029 usable 15-minute intervals, well above the 0.474 conditional impact reported by Deuskar and Johnson (2011) using one-minute data.
- Flow impact $b_f$ averages 0.301 and is significant in 71% of intervals, below the 0.55 reported by Deuskar and Johnson (2011), consistent with weaker endogeneity as the sampling interval shortens toward the event level.
- Around 9:00 macroeconomic announcements, price impact rises and flow impact falls, while return-innovation volatility spikes and flow-innovation volatility declines, indicating a temporary withdrawal of liquidity.
- Impulse responses show almost all of the return-flow interaction dissipates within about one second; the first-lag return-to-return response is negative in over 95% of intervals, indicating short-term return reversal.
- A one-unit order-flow shock, corresponding to roughly 1,000 contracts at the best bid or ask, raises prices by about 1.42 basis points in the long run, translating to a scaled price impact of about 0.48 basis points once flow volatility is accounted for.
- Reciprocal depth (illiquidity) raises price impact and return volatility while lowering flow impact and flow volatility; together with event count, event size, spread and time dummies it explains 54%, 27%, 68%, and 51% of the variation in the two structural parameters and two innovation volatilities respectively.
- Price impact peaks in the early afternoon near 13:00 and falls sharply into the close, while flow impact is lowest around midday near 12:45 and rises sharply in the final minutes before the 15:00 close.

## Limitations

- The bivariate SVAR covers a single instrument (the S&P 500 E-mini) and the best-quote level only, without decomposing order flow by order type when that breakdown is unavailable.
- Identification relies on the assumption that the structural coefficients are constant within each 15-minute window while only innovation volatilities vary across the three five-minute sub-states.
- Reader note: the 2008-2013 sample covers a specific period of market structure and volatility regime; results may not generalize to different microstructure or regulatory environments.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/bid-ask-spread|bid ask spread]]

## Citation

Makoto Takahashi (2025). Returns and Order Flow Imbalances: Intraday Dynamics and Macroeconomic News Effects.

DOI: 10.48550/arxiv.2508.06788

Text ingested: `markdown_output/takahashi-2025-returns-order-flow-imbalances-intraday-dynamics.md`, converted from `raw/ofi-event-clock/takahashi-2025-returns-order-flow-imbalances-intraday-dynamics.pdf`.

Coverage of this summary: Read the full markdown file: abstract, literature review, data and variable construction, intraday summary statistics, the SVAR/ITH methodology, and all empirical results sections including macro-news effects, structural parameters, impulse responses, and intraday variation, plus the reference list.

Known problems with the input: year from file metadata (no publication year printed in the paper text; year_hint 2025 from the job file was used).
<!-- AUTHORED REGION END -->