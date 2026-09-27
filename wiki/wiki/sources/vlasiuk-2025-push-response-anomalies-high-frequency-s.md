---
authors:
- Dmitrii Vlasiuk
- Mikhail Smirnov
content_hash: sha256:12d4fb9ac21196cb8f0d7975b6fdcadbf1cd8ff9713dfecc11f7cdcc0b1dab23
created: 2026-09-27 01:47:00+00:00
page_id: sources/vlasiuk-2025-push-response-anomalies-high-frequency-s
page_type: source
related:
- concepts/event-clock
- concepts/price-impact
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/autocorrelation-time-series
- concepts/long-memory
- concepts/bid-ask-spread
- concepts/market-microstructure-noise
revision_id: 1
schema_version: 2
source_hash: sha256:38491ae2df9cb303e9beeb47cfe4196cdf2277b9ef2b3c39042134186da5de02
source_path: markdown_output/vlasiuk-2025-push-response-anomalies-high-frequency-s.md
source_type: paper
tags:
- price-impact
- market-efficiency
- autocorrelation
- tick-data
- spy-etf
- market-microstructure
- event-time
- clock-event
- asset-equity
- harvest-relevant
title: Push-response anomalies in high-frequency S&P 500 price series
updated: '2026-09-27T01:47:00Z'
uuid: b6ee67e5-fe3c-5c89-8ebe-543cfc429e83
year: 2025
---

<!-- AUTHORED REGION START -->
# Push-response anomalies in high-frequency S&P 500 price series

## Summary

The paper asks whether consecutive intraday price changes in SPY, the most liquid U.S. equity ETF, are conditionally nonrandom once responses are examined lag by lag and conditioned on the size of a prior price move, rather than tested only through an unconditional autocorrelation.

Using NBBO event-time quote data for about 1,500 regular trading days, the authors form, for each integer lag L, ordered pairs of a backward price change (the 'push', over the L events before an anchor) and a forward price change (the 'response', over the L events after that anchor), standardize both by their lag-specific volatility, and estimate the expected standardized response on a common grid of standardized push magnitudes. They further decompose the resulting lag-by-magnitude surface into a symmetric (magnitude-driven) part and an antisymmetric (sign-driven) part, and summarize each lag by an overall response-magnitude statistic and a dominance statistic that indicates whether sign or magnitude dominates.

At short lags the expected response is close to zero across most push magnitudes, consistent with high short-term efficiency, but beyond that range a persistent ridge of nonzero conditional response emerges, most pronounced for pushes beyond about one standard deviation, then leveling off at a plateau rather than growing without bound. Large negative pushes are followed by systematically stronger positive responses than equally large positive pushes are followed by negative ones, which the authors interpret as asymmetric liquidity replenishment after sell-side shocks. On several-thousand-event lags the classic reversal ('market mill') pattern from earlier physics-style literature is reproduced in this dataset.

What is new is embedding this push-response idea in a dense, lag-resolved three-dimensional surface across many lags at once (rather than a single lag or a few scales), decomposing that surface into symmetric and antisymmetric parts with an explicit dominance measure, and estimating it at large scale on NBBO event time with a common standardized grid so that structure is directly comparable across lags.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed in NBBO quote-update event time rather than clock time. For each integer lag L, a backward price 'push' over the L events before an anchor event and a forward 'response' over the L events after that same anchor are computed, using two families of lags spanning roughly one to a few thousand events (short family) and thousands to hundreds of thousands of events (long family). A triplet of anchors is used only when all three fall within the same regular trading session, so push-response pairs never cross the market open or close.

## Data

- **Asset class:** Equities
- **Instruments:** SPDR S&P 500 ETF Trust (SPY)
- **Venue:** Consolidated NBBO quotes across seven U.S. equity exchanges (NYSE, Nasdaq, NYSE Arca, Cboe BZX, Cboe BYX, Cboe EDGX, Cboe EDGA), sourced from TAQ
- **Period:** January 2018 to December 2023 (about 1,512 regular trading days)
- **Granularity:** Event-time NBBO quote updates (about 2.6 billion valid events after cleaning), Regular Trading Hours (09:30-16:00 ET) only

## Features and Measures

- **Push.** The raw mid-price change over the L events immediately before an anchor event, for a chosen lag L.
- **Response.** The raw mid-price change over the L events immediately after the same anchor event, at the same lag L as the push.
- **Standardized push and response.** The push and response divided by their lag-specific standard deviation, estimated per lag from all admissible anchors, so conditional shapes can be compared across lags without confounding by scale.
- **Local and lag-level dominance index.** A statistic bounded between -1 and 1, built from the symmetric and antisymmetric parts of the conditional response surface at paired positive and negative push bins, that is positive when the sign-dependent component dominates and negative when the magnitude-dependent component dominates.

## Method

The mid-price is the average of the best bid and best ask from R-condition-flagged NBBO quotes; mid-price returns are winsorized at the extreme 0.001% tails, and residual same-day price jumps larger than $1.50 are treated as data errors and removed. For each lag L, pushes and responses are standardized using lag-specific means and standard deviations estimated from all admissible anchors, then binned on a common standardized-push grid with a step of 0.025 (extended to four standard deviations) subject to a minimum-support rule per bin, so sparse bins are left blank rather than filled by extrapolation. For each lag the conditional response surface is split into a symmetric (magnitude-driven) and an antisymmetric (sign-driven) component, and each lag is summarized by an overall response-magnitude statistic and a dominance statistic; uncertainty on the lag-level dominance statistic comes from bootstrap resampling of symmetric bin pairs, with bands from the empirical 2.5% and 97.5% quantiles.

## Results

- At short lags (roughly 1-5,000 ticks), expected standardized responses cluster near zero across most push magnitudes, consistent with high short-term efficiency.
- Beyond the short-lag range, a ridge of nonzero conditional response emerges once standardized pushes exceed roughly one standard deviation, strengthening as the lag grows into the middle of the long-lag grid before flattening into a plateau.
- On lags of roughly 5,000 to 150,000 events the cross-sections reproduce the classical 'market mill' asymmetry: positive pushes map to negative expected responses and negative pushes to positive responses, strongest in the wings.
- Large negative pushes are followed by stronger positive conditional responses than equally large positive pushes are followed by negative ones, consistent with asymmetric liquidity replenishment after sell-side shocks.
- The aggregate dominance statistic is strongly positive at the shortest lags, turns negative near the short-to-long lag transition, returns to weakly positive values across a broad middle range, and drifts slightly negative again at the longest lags.
- The data-cleaning procedure (winsorizing extreme returns and removing large same-day price jumps of more than $1.50) preserved over 99.5% of the original observations.

## Limitations

- The analysis covers a single, highly liquid instrument (SPY); the authors note that instruments with wider spreads or thinner depth may show different or stronger structure.
- No explicit transaction-cost overlay is applied to the trading implications discussed; the authors describe this as a needed extension.
- The sample spans January 2018 to December 2023 and Regular Trading Hours only, so overnight and premarket dynamics are excluded.
- Reader note: the paper reports descriptive conditional-response structure and dominance statistics, not a backtested trading strategy with realized profit and loss.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/long-memory|long memory]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure-noise|market microstructure noise]]

## Citation

Dmitrii Vlasiuk, Mikhail Smirnov (2025). Push-response anomalies in high-frequency S&P 500 price series.

DOI: 10.2139/ssrn.5724104

Text ingested: `markdown_output/vlasiuk-2025-push-response-anomalies-high-frequency-s.md`, converted from `raw/ofi-event-clock/vlasiuk-2025-push-response-anomalies-high-frequency-s.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, data and preprocessing, methodology, all results, discussion and trading implications, and concluding remarks.

Known problems with the input: Several equations and figures are rendered as images and omitted by the markdown converter ('picture intentionally omitted'); the surrounding prose description of each formula was used instead, and no numeric content beyond what appears in the text was inferred.
<!-- AUTHORED REGION END -->