---
authors:
- Nikolas Michael
- Mihai Cucuringu
- Sam Howison
content_hash: sha256:69bdff9c26a9d8093a16d1dc42ae00c342dccb11bee670b1ad67eba84b3aed29
created: 2026-09-27 01:47:00+00:00
page_id: sources/michael-2022-option-volume-imbalance-predictor-equity-market
page_type: source
related:
- concepts/informed-trading
- concepts/order-imbalance
- concepts/cross-impact
- concepts/alpha-signal
- concepts/market-making
- concepts/flow-decomposition
- concepts/backtesting
- concepts/market-microstructure
- entities/mihai-cucuringu
revision_id: 1
schema_version: 2
source_hash: sha256:19f9607eb6a73cf645d90a04932759beee48053f6e84bedb89cfaf41162505d0
source_path: markdown_output/michael-2022-option-volume-imbalance-predictor-equity-market.md
source_type: paper
tags:
- options
- informed-trading
- market-microstructure
- cross-impact
- equity-returns
- sharpe-ratio
- market-makers
- signal-research
- clock-calendar
- asset-equity
- harvest-relevant
title: Option Volume Imbalance as a predictor for equity market returns
updated: '2026-09-27T01:47:00Z'
uuid: 01517f90-a8ff-5800-87c2-f7427031c2dc
year: 2022
---

<!-- AUTHORED REGION START -->
# Option Volume Imbalance as a predictor for equity market returns

## Summary

The paper asks whether the imbalance between option volumes tied to bullish and bearish views can predict the next-day direction of the underlying stock or ETF price. The authors build the Option Volume Imbalance (OVI), a normalized measure comparing volumes from call-buy/put-sell trades against call-sell/put-buy trades, computed separately for five market participant classes (Firms, Brokers, Market Makers, Customers, Professional Customers) using ten-minute intraday volume data from the Nasdaq NOM and PHLX option exchanges between 02 Jan 2015 and 31 Dec 2019.

The sign of each day's OVI is used to open a hypothetical long or short position in the underlying, and predictive power is judged through cumulative profit-and-loss and annualized Sharpe Ratio rather than R-squared, because the relationship between OVI and returns need not be linear. A new estimation method, P&L regression, is introduced to combine several OVI variants into a single signal by directly maximizing a smoothed profit objective with an L1 penalty, instead of ordinary least squares.

Market Maker OVI turns out to be the strongest and most consistent predictor of overnight returns, with Sharpe Ratios reaching about 4.5; Customer and Broker OVI are also informative, while Firm and Professional Customer OVI carry little signal. Predictability concentrates in high-implied-volatility contracts and in put rather than call options, persists for at least two days without reverting (pointing to informed trading rather than short-lived price pressure), and extends across assets through a statistically significant cross-impact network.

The novelty lies in decomposing option flow by trader class rather than treating it in aggregate, in using a P&L-based nonlinear objective instead of linear regression to combine signals, and in mapping cross-sectional predictability between different underlyings as a directed network.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Option exchanges report cumulative daily volume for each contract in 10-minute snapshots from market open to close, giving 39 intraday points per day; the paper aggregates these into one daily volume figure per asset, market-participant class and transaction type, and predicts the next trading day's return (mainly overnight close-to-open, but also open-to-close and close-to-close).

## Data

- **Asset class:** Equities
- **Instruments:** US-listed common stocks (mostly) plus a selection of 11 ETFs, matched to their traded option contracts
- **Venue:** Options: Nasdaq Option Market (NOM/NOTO) and Nasdaq PHLX (PHOTO); underlying equity/ETF prices from NYSE via the CRSP database
- **Period:** 02 Jan 2015 to 31 Dec 2019
- **Granularity:** Daily signal built from exchange-reported 10-minute cumulative intraday option volume snapshots (39 per trading day), decomposed by market participant class and by call/put and buy/sell type

## Features and Measures

- **Option Volume Imbalance (OVI).** Normalized difference between option volumes (or trade counts) that signal an upward view (call buys plus put sells) and a downward view (call sells plus put buys), for a given asset, market participant class and day, scaled to lie between -1 and 1.
- **Trade-based and nominal-volume-based OVI.** Variants of OVI built from the number of trades rather than contract volume, or from volume weighted by the average option price, meant to reduce the influence of cheap, high-volume contracts or emphasize higher-cost trades.
- **P&L regression.** A nonlinear estimation method that combines several OVI variants into one signal by directly maximizing a smoothed proxy for cumulative trading profit and loss, with an L1 penalty to shrink uninformative variants, fit with the Adam optimizer in rolling windows.
- **Bet-size weighting schemes.** Rules (uniform, signal-magnitude, option volume, nominal volume, volume relative to open interest, and volume times implied volatility) for sizing the hypothetical position taken in each asset.
- **Cross-impact network.** A directed graph built by testing, for each pair of assets, whether one asset's Market Maker OVI significantly predicts another asset's return, used to assess predictability that crosses between underlyings.

## Method

The core empirical test uses the sign of a chosen OVI series as a directional trading signal; a hypothetical position is taken for or against the underlying, and predictability is judged from the resulting excess-return-adjusted profit and loss and its annualized Sharpe Ratio, tested for significance with the Bailey and Lopez de Prado deflated Sharpe Ratio test and compared across strategies with a Ledoit-Wolf Sharpe Ratio difference test. Assets are split into quantile groups by signal strength each day to see whether stronger signals perform better.

To combine multiple OVI variants (different market participant classes, exchanges, or buy/sell types) into a single signal, the authors replace ordinary least squares with a purpose-built P&L regression: coefficients are chosen to directly maximize a smoothed version of cumulative profit and loss, subject to an L1 penalty, refit on a rolling window of 500 trading days and evaluated out-of-sample over the following 100 days. Sub-sample analysis by option Greeks (Delta, Gamma, Theta, Rho, Vega), moneyness, maturity and implied volatility is used to locate where predictive power concentrates, and a directed network built from pairwise Sharpe Ratio significance tests (Bonferroni-corrected) is used to assess cross-impact between different underlyings.

## Results

- Market Maker option volume imbalance is the strongest overnight-return predictor, with annualized Sharpe Ratios up to about 4.5 and tail-portfolio profit per dollar of up to 4 basis points a day.
- Customer and Broker imbalance also predict returns significantly; Firm and Professional Customer imbalance show little to no predictive power.
- Predictability is strongest for overnight returns, weaker for close-to-close returns, and weakest for open-to-close returns.
- Predictive power concentrates in high-implied-volatility contracts and in put rather than call options, and is roughly flat with respect to option maturity.
- Market Maker signal returns persist for at least two days without reverting, consistent with informed trading rather than transient price pressure.
- A cross-impact network built from pairwise Sharpe Ratio tests contains far more significant cross-asset links than self-predictive links, rejecting the hypothesis of no cross-impact.
- Results replicate qualitatively on the Nasdaq NOM exchange data (NOTO), though weaker than the Nasdaq PHLX data (PHOTO), with Market Maker Sharpe Ratios of about 2.5 to 3.
- Combining multiple OVI variants with the P&L regression modestly raises out-of-sample profitability versus using a single market participant class's signal.

## Limitations

- No transaction costs are included in the profit-and-loss calculation, so realized returns from actually trading the signal would be lower.
- The sample covers only 2015-2019 on U.S. NYSE-listed equities and 11 ETFs; it is unclear whether findings generalize to other markets or periods.
- Each option transaction is double-counted across the two counterparties' market participant classes, a design choice the authors acknowledge can complicate interpreting which class 'wins'.
- Reader note: the multiple-testing correction used for the cross-impact network is conservative, but the underlying pairwise tests still number in the hundreds of thousands, leaving some risk of residual false positives.

## Related

- [[concepts/informed-trading|informed trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/cross-impact|cross impact]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/market-making|market making]]
- [[concepts/flow-decomposition|flow decomposition]]
- [[concepts/backtesting|backtesting]]
- [[concepts/market-microstructure|market microstructure]]
- [[entities/mihai-cucuringu|Mihai Cucuringu]]

## Citation

Nikolas Michael, Mihai Cucuringu, Sam Howison (2022). Option Volume Imbalance as a predictor for equity market returns.

DOI: 10.48550/arxiv.2201.09319

Text ingested: `markdown_output/michael-2022-option-volume-imbalance-predictor-equity-market.md`, converted from `raw/ofi-event-clock/michael-2022-option-volume-imbalance-predictor-equity-market.pdf`.

Coverage of this summary: Read the abstract, introduction, related literature review, the OVI definition, the full data-set description, the evaluation-methods and P&L regression sections, the main empirical results (Section 5), the options-features analysis (Section 6), all of Section 7 (holding-period persistence, buy/sell decomposition, NOTO comparison) and the cross-impact network analysis (Section 7.4), and the conclusion; did not read Appendices A-E (definitions and supplementary tables).
<!-- AUTHORED REGION END -->