---
authors:
- Måns Hjort
content_hash: sha256:a388eb3ba8891b28c50ef7c22065c119752b0b663901c37c547feb112ee03ae8
created: 2026-09-27 01:47:00+00:00
page_id: sources/mans-2025-en-lokalt-konkav-och-transient-prispaverkningsmodell
page_type: source
publication_venue: KTH Royal Institute of Technology, Degree Project in Financial
  Mathematics (second cycle, 30 credits); TRITA - SCI-GRU 2025:077, Stockholm, Sweden
related:
- concepts/price-impact
- concepts/optimal-execution
- concepts/square-root-law
- concepts/metaorder
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/overfitting-backtesting
- concepts/propagator-model
revision_id: 1
schema_version: 2
source_hash: sha256:1061808e1fdd3525551191706cfe57e045b2c18efb1278d21e386dc51791aafb
source_path: markdown_output/mans-2025-en-lokalt-konkav-och-transient-prispaverkningsmodell.md
source_type: paper
tags:
- price-impact
- optimal-execution
- futures
- square-root-law
- twap
- market-microstructure
- concave-impact
- rolling-calibration
- clock-calendar
- asset-futures
- harvest-relevant
title: A Locally Concave Transient Price Impact Model and Optimal Execution
updated: '2026-09-27T01:47:00Z'
uuid: 464a9fdd-9653-5dba-b1c8-e645b20d3f55
year: 2025
---

<!-- AUTHORED REGION START -->
# A Locally Concave Transient Price Impact Model and Optimal Execution

## Summary

The thesis asks two questions about futures execution: how much of intraday price change a locally concave, transient price impact model can explain out of sample, and how much a discrete-time execution schedule built on that model saves relative to a TWAP benchmark. It is written from inside a hedge fund's systematic strategies team, using public one-minute futures data for Corn, E-mini S&P 500, Henry Hub Natural Gas and 10-Year T-Note contracts.

The approach combines an exponential decay term for how quickly impact fades with a concave power-law scaling of the signed trade imbalance in each one-minute bin, normalised by rolling volatility and volume estimates so the model behaves consistently across days and markets. The concavity exponent and impact coefficient are calibrated on six months of in-sample data and validated on three months of out-of-sample data, rolled forward repeatedly, and the coefficient is allowed to update at different intraday frequencies rather than staying fixed for the whole day. The calibrated model is then handed to a discrete-time optimisation solver (GEKKO) that produces an execution schedule under a no-sign-change constraint meant to rule out manipulative round-trip trading, and this schedule is compared against a TWAP schedule that spreads the same order evenly through time.

The main finding is that the model explains a moderate but non-trivial share of intraday price variation out of sample, and that this signal is still enough to meaningfully beat TWAP, especially for larger orders and when the impact coefficient is refreshed intraday rather than held constant for the day. The concavity exponent stays below one for every market studied, which the thesis reads as new evidence, in a futures setting, for the broadly known square-root law of price impact. What is new relative to the cited prior work is less the functional form itself, which borrows from existing propagator models, and more the systematic calibration across four futures markets, the comparison of daily versus intraday recalibration, and the embedding of the calibrated model directly into a constrained execution solver rather than treating impact estimation and execution design separately.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Data are binned into fixed one-minute wall-clock intervals within each trading day (δt = 1 minute). The signed trade imbalance for a bin is the ask-executed volume minus the bid-executed volume in that bin, and impact is updated recursively bin by bin with an exponential decay term plus a new, normalised impact contribution. The impact coefficient can be refreshed on a day, hourly, or half-hourly basis rather than staying fixed all day. The prediction horizon for calibration is any multiple of the one-minute bin (h = m times δt), and the optimal execution schedule is evaluated over a fixed 90-minute window from 19:00 to 20:30 (Central Time) common to all four underlyings.

## Data

- **Asset class:** Futures
- **Instruments:** Four exchange-traded futures contracts: Corn (C), E-mini S&P 500 (ES), Henry Hub Natural Gas (NG), and 10-Year T-Note (TY).
- **Venue:** CME Group (the cited contract-expiration calendars for Corn, Natural Gas and 10-Year T-Note are CME Group sources, and all four underlyings are CME Group futures products).
- **Period:** 2014-04-01 to 2025-02-04
- **Granularity:** One-minute intraday bins with volume-based contract rollover between expirations; calibrated on rolling 6-month in-sample windows and validated on the following 3-month out-of-sample window.

## Features and Measures

- **Signed trade imbalance (q_t).** In each one-minute bin, the total volume executed at the ask price minus the total volume executed at the bid price; the driver variable for the impact model.
- **Locally concave transient impact function.** The per-bin impact contribution is an impact coefficient times the sign of the trade imbalance times the absolute imbalance raised to a concavity power c between 0 and 1, so impact grows sub-linearly with trade size, combined with an exponential decay of prior impact.
- **Volatility/volume normalisation (sigma^SMA, ADV^SMA).** 20-day simple moving averages of one-bin return volatility and of aggregated daily traded volume, used to rescale the trade-imbalance input so the impact model behaves consistently across trading days and across underlyings.
- **Intraday time-varying impact coefficient (lambda_t).** The impact coefficient is allowed to take a different calibrated value for each day, each hour, or each half-hour of the trading session, rather than one fixed value per day, to capture intraday liquidity variation.

## Method

The model recursively updates price impact each one-minute bin as an exponentially decaying term (decay half-life fixed at 60 minutes, based on prior literature rather than calibrated) plus a new impact contribution equal to an impact coefficient times the sign of the trade imbalance times the volatility/volume-normalised absolute imbalance raised to a concavity power c in (0,1). For each candidate value of c, the h-horizon price return is regressed, with no intercept, on the corresponding h-horizon impact change to estimate the impact coefficient by ordinary least squares; the c that maximises in-sample R-squared is selected as the optimal c*, and its associated coefficient estimate is carried forward without look-ahead, since only in-sample fit (not out-of-sample fit) is available at the time real execution decisions would be made.

Performance is judged by in-sample versus out-of-sample R-squared across rolling six-month/three-month windows, by the ratio of out-of-sample to in-sample R-squared as a robustness check for overfitting, and by residual normality and autocorrelation diagnostics. The calibrated impact model is then plugged into a discrete-time optimal execution problem that minimises expected impact cost subject to full execution of a target order, trading confined to a valid time grid, and a constraint forbidding sign changes in the trade schedule (to prevent round-trip price manipulation). This constrained problem is solved with the GEKKO algebraic modelling and optimisation package, using Polars for data handling and chunked processing to manage a multi-year, multi-underlying dataset, and the resulting schedule's cost is compared against a Time-Weighted Average Price (TWAP) benchmark that executes the same order in equal slices across the same valid trading times.

## Results

- Out-of-sample R² reached up to about 45% using 20-day SMA-normalised volatility and volume, with the highest fit for Natural Gas (NG) and E-mini S&P 500 (ES) and the lowest for the 10-Year T-Note (TY).
- Letting the impact coefficient update within the day rather than staying fixed improved fit for most underlyings, e.g. NG out-of-sample R² moved from 38.6% (day updates) to 38.9% (hourly) and 38.8% (half-hourly).
- The calibrated concavity parameter c* stayed below 1 for every underlying and update frequency, ranging from about 0.35 (Corn, half-hourly) to 0.75 (E-mini S&P 500, half-hourly), consistent with a concave, sub-linear impact function and the square-root law.
- Residual autocorrelations up to lag 10 stayed within the 95% confidence bands for every underlying and update interval; the day interval showed autocorrelation near ±0.40, versus about ±0.10 to ±0.13 for the hourly and half-hourly intervals, indicating little serial dependence once intraday updates are used.
- Extending the in-sample window from 1 to 2 months raised average out-of-sample R² from 22.5% to 28.5%, after which gains flattened; the thesis adopted a 6-month in-sample and 3-month out-of-sample rolling split as its working configuration.
- Against a TWAP benchmark, the optimised discrete-time execution schedule cut costs by 20 to 50% for large orders and 7 to 8% for small to medium orders; for Corn at the largest order size, cost fell from 220 to 90 bps (day updates) and from 200 to 34 bps (half-hourly updates), an 87.03% saving.

## Limitations

- The calibration regression assumes zero alpha (no intercept), so any true price drift is absorbed into the estimated impact coefficient, which the authors note can bias the coefficient either up or down.
- The model excludes permanent price impact, bid-ask spreads, commissions and fill risk, so it only explains a bounded share (about 20% to 45%) of intraday price variation.
- All optimal-execution results use a single shared 19:00-20:30 execution window across four different futures, which the authors note does not match each market's own peak-liquidity period.
- Calibration and cost-saving figures come from public order-flow data mixing many participants' trades rather than proprietary parent/child order records, which the authors say likely understates the execution savings achievable in practice.
- Reader note: findings are limited to four liquid CME futures products (Corn, E-mini S&P 500, Natural Gas, 10-Year T-Note) over the 2014-04-01 to 2025-02-04 period; the authors state as a delimitation that results may not generalise to less liquid markets.

## Related

- [[concepts/price-impact|price impact]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/square-root-law|square root law]]
- [[concepts/metaorder|metaorder]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/propagator-model|propagator model]]

## Citation

Måns Hjort (2025). A Locally Concave Transient Price Impact Model and Optimal Execution. KTH Royal Institute of Technology, Degree Project in Financial Mathematics (second cycle, 30 credits); TRITA - SCI-GRU 2025:077, Stockholm, Sweden.

Text ingested: `markdown_output/mans-2025-en-lokalt-konkav-och-transient-prispaverkningsmodell.md`, converted from `raw/ofi-event-clock/mans-2025-en-lokalt-konkav-och-transient-prispaverkningsmodell.pdf`.

Coverage of this summary: Read the abstract, acknowledgments, full introduction, mathematical framework, literature review, price impact model chapter, data/preprocessing chapter, assumptions/delimitations, parameter calibration chapter, optimal execution setup, all of Chapter 9 (Results, sections 9.1-9.7), and all of Chapter 10 (Discussion, Conclusion, Future Work); skimmed the bibliography and the Appendix C square-root-law derivation, and did not read the detailed appendix tables (A.1-A.7) or the theorem appendix (Appendix B) beyond what is summarised in the main chapters.

Known problems with the input: Nearly all mathematical equations and several figures were rendered as '==> picture... intentionally omitted <==' placeholders by the PDF-to-markdown conversion, so exact functional forms and derivations are described qualitatively from surrounding prose rather than reproduced as extracted formulas; Several results tables (e.g. Table 9.5, Table 9.11) were mangled by the markdown table conversion (merged/shifted cells), so figures were cross-checked against the accompanying prose discussion before being used here.
<!-- AUTHORED REGION END -->