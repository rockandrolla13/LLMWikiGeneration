---
authors:
- Yutong Lu
- Gesine Reinert
- Mihai Cucuringu
content_hash: sha256:3632ca102ac366623b4f872a54358fa2bce6335193f514519412c0a6820ec560
created: 2026-09-27 01:47:00+00:00
page_id: sources/lu-2023-trade-co-occurrence-trade-flow-decomposition
page_type: source
related:
- concepts/trade-clock
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/price-impact
- concepts/flow-decomposition
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/trade-classification
- concepts/informed-trading
- entities/mihai-cucuringu
revision_id: 1
schema_version: 2
source_hash: sha256:a9fc2beb06c80e5f1d12b181e7266a9ce1a8c036b124308a1fc03f88c84ea89d
source_path: markdown_output/lu-2023-trade-co-occurrence-trade-flow-decomposition.md
source_type: paper
tags:
- order-imbalance
- trade-classification
- equity-microstructure
- high-frequency-trading
- price-impact
- portfolio-sorting
- return-prediction
- co-occurrence-analysis
- clock-trade
- asset-equity
- harvest-relevant
title: Trade Co-occurrence, Trade Flow Decomposition, and Conditional Order Imbalance
  in Equity Markets
updated: '2026-09-27T01:47:00Z'
uuid: d34fb23a-60dc-5b3e-bd91-d1cd7b3ffe1c
year: 2024
---

<!-- AUTHORED REGION START -->
# Trade Co-occurrence, Trade Flow Decomposition, and Conditional Order Imbalance in Equity Markets

## Summary

The paper asks whether the timing of a trade relative to other trades carries information about price formation, beyond the usual buy/sell classification of order imbalance. The authors define trade co-occurrence: two trades co-occur if they arrive within a small time window (a neighbourhood of size delta) of each other, and they pick delta by comparing the empirical share of isolated trades to what a null model of independent Poisson arrivals would predict, settling on a value of 1 millisecond. Using this window, every trade in a stock is placed into one of five bins depending on whether it co-occurs with no other trade (isolated), only with trades of the same stock, only with trades of other stocks in a chosen market index, or both. Daily order imbalance is then computed separately within each bin, producing what the authors call conditional order imbalances (COIs).

Working with 457 constituents of the S&P 500 traded on NASDAQ, using LOBSTER limit order book data from 2017-01-03 to 2020-12-31, the authors show that although the null model predicts about 81.28% of trades should be isolated at a 1 millisecond window, only 28.55% actually are, which the authors take as evidence that trade arrivals are not independent. All types of COI are positively related to same-day returns, with the isolated-trade COI alone reaching an adjusted R-squared of 5.91% versus 5.66% for standard undecomposed order imbalance, and combining several COI types raises explanatory power further. For predicting the next day's return, only the isolated and non-self-isolated COIs carry a positive sign, while the other three types are negatively related to future returns.

The authors turn these signals into daily long-short portfolios formed by sorting stocks on lagged COI values. Single-sorting on the isolated-trade COI is profitable, and double-sorting on pairs of COI types raises returns further, with the isolated/non-cross-isolated combination reaching the highest reported annualized return of 34.87% and the highest reported Sharpe ratio of 1.79. The authors describe the resulting COI features as distinguishable from one another, citing pairwise correlations below 0.6.

What is new is the idea of trade co-occurrence itself: classifying trades by their time-proximity to other trades in the market, rather than by trade size, direction, or investor type, as a way to decompose order flow and recover a return-forecasting signal that plain order imbalance no longer shows in this sample.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Every executed trade in a stock is labelled by whether another trade (of the same stock, of other stocks in a chosen market index, or both) falls within a symmetric window of size delta around it, with delta chosen empirically and fixed at 1 millisecond for the main analysis. The resulting per-type order imbalances are aggregated once per trading day, and the prediction target is either the same trading day's open-to-close return (contemporaneous regressions) or the next trading day's market-excess return (predictive regressions and portfolio sorts).

## Data

- **Asset class:** Equities
- **Instruments:** 457 constituents of the S&P 500 index (common stock), plus the SPY ETF used as a market benchmark
- **Venue:** NASDAQ (order book data obtained from the LOBSTER database)
- **Period:** 2017-01-03 to 2020-12-31
- **Granularity:** trade-level order book records with nanosecond timestamps, aggregated to daily order imbalances and daily open-to-close returns

## Features and Measures

- **Trade co-occurrence.** Two trades are said to co-occur if the time between their arrivals is smaller than a chosen neighbourhood size delta, set at 1 millisecond in the main analysis.
- **Trade flow decomposition.** Every trade in a stock is assigned to one of five categories -- isolated, non-isolated, non-self-isolated, non-cross-isolated, or non-both-isolated -- according to whether the trades in its delta-neighbourhood belong to the same stock, to other stocks in a chosen market index, to both, or to neither.
- **Conditional order imbalance (COI).** For each trade category, the normalized difference between the number of buyer-initiated and seller-initiated trades of that category on a given stock-day, computed the same way as standard order imbalance but restricted to that category's trades.
- **Market set / market index.** A chosen universe of stocks (the S&P 500 constituents used in the main study, with S&P 100 and Dow 30 tested for robustness) whose trades are considered when deciding whether a given stock's trades co-occur with trades of other stocks.

## Method

To measure contemporaneous price impact, the authors run a panel regression of daily stock returns on the various COIs plus control variables (realized volatility, dollar volume, and the market, size, value, profitability, investment and momentum factors), first entering each COI type individually and then jointly, and compare regressions by their adjusted R-squared and by two-tailed t-tests on the COI coefficients. To measure forecasting power they repeat the same regression design with the return shifted one day ahead. Economic value is assessed by forming daily quintile portfolios sorted on lagged COI values (single-sorts and double-sorts on pairs of COI types), holding long-short positions from market open to close, and comparing annualized returns and Sharpe ratios against benchmark portfolios (undecomposed order imbalance, prior-day return momentum, an equally-weighted portfolio, and the SPY ETF); abnormal returns are estimated by regressing long-short portfolio returns on the same risk factors with Newey-West standard errors. Robustness checks repeat the analysis for eight choices of delta, for two alternative market-index universes (S&P 100 and Dow 30), for three intraday sub-periods, for a volume-based version of order imbalance, and under several assumed transaction-cost levels.

## Results

- The empirical share of isolated trades (28.55%) is far below what a null model of independent Poisson trade arrivals at the same 1 millisecond window predicts (81.28%), which the authors read as evidence that trades genuinely co-occur.
- All conditional order imbalance types are positively and significantly related to same-day stock returns; the isolated-trade COI alone reaches an adjusted R-squared of 5.91%, versus 5.66% for the standard, undecomposed order imbalance.
- Combining multiple COI types in one regression raises explanatory power further, and once the decomposed COIs are included, the coefficient on the undecomposed order imbalance is no longer significant.
- For next-day returns, only isolated and non-self-isolated COIs carry a positive relationship; the other three decomposed types are negatively related to future returns, unlike the near-zero coefficient found for undecomposed order imbalance.
- Daily long-short portfolios sorted on the isolated-trade COI are profitable, and double-sorting on pairs of COI types improves results further, with the isolated / non-cross-isolated combination reaching the highest reported annualized return of 34.87% and the highest reported Sharpe ratio of 1.79.
- The decomposed order imbalances are described as behaving differently from each other, with all pairwise correlations among COI types below 0.6.
- Findings are reported as holding under several robustness checks: alternative neighbourhood sizes, alternative market-index universes, intraday sub-periods, a volume-based order imbalance measure, and assumed transaction costs of 1 to 5 basis points.

## Limitations

- The authors state that without client order identifiers they cannot verify which trader types generate each of the five trade categories.
- The authors state that the classification of a trade depends on the chosen market-index universe, and that results weaken when a much smaller index (Dow 30) is used.
- The authors state that the neighbourhood size delta is fixed across all stocks and set by a simple heuristic rather than optimized per task.
- Reader note: the study covers a single equity universe (S&P 500 names) and a four-year US sample; no out-of-sample period or other asset class is tested.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/flow-decomposition|flow decomposition]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/informed-trading|informed trading]]
- [[entities/mihai-cucuringu|Mihai Cucuringu]]

## Citation

Yutong Lu, Gesine Reinert, Mihai Cucuringu (2024). Trade Co-occurrence, Trade Flow Decomposition, and Conditional Order Imbalance in Equity Markets.

DOI: 10.2139/ssrn.4363082

Text ingested: `markdown_output/lu-2023-trade-co-occurrence-trade-flow-decomposition.md`, converted from `raw/ofi-event-clock/lu-2023-trade-co-occurrence-trade-flow-decomposition.pdf`.

Coverage of this summary: Read the full introduction, literature review, methodology (Sections 3-4), all empirical results sections (5-8), and the conclusion; skimmed the reference list and did not read the lettered appendices (A-I) in detail.

Known problems with the input: Running header prints the date 'March 15, 2024', which is used here as the paper's year; this is a revision/typesetting date and may not match the year_hint of 2023 in the job file, which could reflect an earlier preprint version.
<!-- AUTHORED REGION END -->