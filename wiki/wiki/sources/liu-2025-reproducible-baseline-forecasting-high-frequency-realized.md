---
authors:
- LIU, Zhangqi
content_hash: sha256:32334d7fc861f82a9b87858ad89727cb58e6b3be64322abc6d09c3f4e365e085
created: 2026-09-27 01:47:00+00:00
page_id: sources/liu-2025-reproducible-baseline-forecasting-high-frequency-realized
page_type: source
publication_venue: Journal of Economic Theory and Business Management (Vol. 2, No.
  6, 2025)
related:
- concepts/order-flow-imbalance
- concepts/realized-variance
- concepts/limit-order-book
- concepts/bid-ask-spread
- concepts/feature-engineering
- concepts/overfitting-backtesting
revision_id: 1
schema_version: 2
source_hash: sha256:20057080b88b1fef3a426a4a2bd2b9fdf06129850f7b81e717e253345b14cc90
source_path: markdown_output/liu-2025-reproducible-baseline-forecasting-high-frequency-realized.md
source_type: paper
tags:
- realized-volatility
- gradient-boosting
- order-flow-imbalance
- explainable-ml
- leakage-safe-validation
- monotone-constraints
- clock-calendar
- asset-equity
- harvest-relevant
title: A Reproducible Baseline for Forecasting High-Frequency Realized Volatility
  with Order-Flow Features
updated: '2026-09-27T01:47:00Z'
uuid: d7e07cbc-9055-54f0-9acf-006db80308b2
year: 2025
---

<!-- AUTHORED REGION START -->
# A Reproducible Baseline for Forecasting High-Frequency Realized Volatility with Order-Flow Features

## Summary

The paper sets out to build a baseline for forecasting short-horizon realized volatility that is competitive with flexible machine-learning models while staying interpretable and reproducible enough for regulated use, arguing that existing econometric baselines under-use order-book information and that many learning-based approaches suffer from leakage, weak cross-asset generalization, or unstable explanations.

Its approach organizes limit order book and trade information into five feature families (liquidity/spreads, order-book shape, order flow and trades, short-memory price patterns, and market-state proxies), then fits a gradient-boosted tree model with monotone constraints that force selected features (such as relative spread, microprice premium, and order-flow imbalance) to have a fixed-sign effect on predicted volatility. Evaluation combines rolling-window and purged k-fold cross-validation with an embargo around the forecast horizon, plus a groupwise test that holds whole assets out of training, and compares against HAR-RV, EWMA, ridge regression, and unconstrained gradient boosting using RMSPE and the Diebold-Mariano test.

The monotone-constrained model has the lowest error of the compared models overall and within every reported market condition (opening, midday, closing, high- and low-volatility), and also has the most stable SHAP-based feature-importance rankings across time and across assets, though the gain over unconstrained boosting is smaller in level than the gain over the econometric baselines.

What is new is treating explanation stability as something to be measured (via rank correlation of SHAP importances across rolling windows and asset groups) rather than assumed, and pairing that with a monotone-constrained model and a leakage-aware, cross-asset validation protocol, plus a released reproducibility package.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Quotes and trades are aligned to a uniform clock-time grid at one-minute and five-minute resolutions, with realized volatility computed over a forecast horizon H from returns sampled on that grid; a parallel event-time (message-count) grid is also built as a robustness check when message intensity is very uneven, but the main reported results use the fixed clock-time bars.

## Data

- **Asset class:** Equities
- **Instruments:** not stated (described only as 'multiple liquid equities'; no tickers are given)
- **Venue:** not stated
- **Period:** not stated precisely (described as 'several weeks of continuous trading')
- **Granularity:** millisecond-level quotes and trades aggregated into one-minute and five-minute clock-time bars, with an event-time grid as a sensitivity check

## Features and Measures

- **Microprice.** A volume-weighted blend of the best bid and ask prices, weighted by the size available at each side, used as a proxy for where the price is being pushed.
- **Order-flow imbalance (OFI).** A signed measure aggregating changes in bid and ask queue sizes at the inside of the book over a short window, capturing the net buying or selling pressure on the best quotes.
- **Order-book imbalance / depth.** The relative size of total bid versus ask depth across levels, summarizing the shape and lopsidedness of the book.
- **Effective spread.** The difference between the trade price and the prevailing midprice at the time of the trade, signed by the direction of the trade, used as a realized transaction-cost measure.
- **Multi-scale realized measures.** Short-memory price-pattern features computed at several look-back scales to capture local dispersion and tail behavior in recent returns.

## Method

The target is realized volatility of log midprice returns over a horizon H, computed from a lookback window W of order book and trade history and transformed with a variance-stabilizing (log or square-root) mapping before modeling. A gradient-boosted tree model is trained on the resulting feature set with sample weights that acknowledge heterogeneity in trading activity, and with monotone constraints restricting split directions so that features screened as having a stable, theory-consistent sign (via a monotonicity score and a monotone-violation rate on held-out data) must have a non-decreasing or non-increasing effect on the prediction. Validation combines rolling-window evaluation with purged k-fold cross-validation and an embargo of bars around each forecast horizon to block near-horizon leakage, plus a groupwise split that holds out entire assets to test out-of-domain generalization; hyperparameter search is nested inside the same protocol. The model is compared against a heterogeneous autoregressive (HAR-RV) model, an exponentially weighted moving-average model, a ridge regression on the same features, and an unconstrained gradient-boosting model, using RMSPE, sMAPE, and the Diebold-Mariano test with Newey-West variance. Explanation quality is assessed by computing SHAP feature importances per rolling window and asset group and measuring their Spearman rank correlation across windows and groups.

## Results

- Across the full evaluation, the monotone-constrained gradient-boosting model had the lowest cross-asset RMSPE (0.192), ahead of unconstrained gradient boosting (0.207), ridge regression (0.224), EWMA (0.238), and the HAR-RV benchmark (0.251).
- The same constrained model also had the highest explanation-stability score (0.89, versus 0.74 for unconstrained boosting, 0.87 for ridge, 0.84 for EWMA, and 0.81 for HAR-RV), meaning its SHAP feature-importance rankings held up better across rolling time windows and asset groups.
- Broken out by market condition, the constrained model had the lowest RMSPE in every regime reported: opening session 0.204, midday 0.173, closing session 0.192, high-volatility periods 0.225, and low-volatility periods 0.159, all below the corresponding HAR-RV, EWMA, ridge, and unconstrained-boosting figures.
- The constrained model took the longest to train among the five compared (9.2 minutes versus 8.5 for unconstrained boosting, and well under two minutes for the econometric and ridge baselines).
- Ablations showed that removing the order-flow-imbalance feature hurt accuracy more than removing any other single feature family, and that removing the monotone constraints left point accuracy little changed but visibly reduced the stability of SHAP-based feature rankings across rolling windows.
- The largest forecast errors clustered around brief liquidity droughts (simultaneous depletion of book depth on both sides plus a burst of cancellations) and around opening-auction or late-session jumps, where the model under-predicted the following volatility.

## Limitations

- The authors state that sensitivity to shifts in the underlying trading mechanism (regime shifts) may remain despite the leakage-safe validation design.
- The authors note that excluding news and cross-venue signals may limit the model's coverage of the true information set driving volatility.
- The authors flag that sub-minute forecast horizons would likely need further engineering (streaming feature computation, approximate SHAP), which this study does not implement.
- Reader note: the paper never names the exchange, tickers, or exact sample dates of its 'public limit order book dataset,' which limits independent verification of the results.
- Reader note: two of the paper's main results tables were corrupted by PDF-to-markdown conversion (numbers split across cells), so this summary relies only on the tables that converted cleanly; see input_problems.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]

## Citation

LIU, Zhangqi (2025). A Reproducible Baseline for Forecasting High-Frequency Realized Volatility with Order-Flow Features. Journal of Economic Theory and Business Management (Vol. 2, No. 6, 2025).

DOI: 10.70393/6a6574626d.333538

Text ingested: `markdown_output/liu-2025-reproducible-baseline-forecasting-high-frequency-realized.md`, converted from `raw/ofi-event-clock/liu-2025-reproducible-baseline-forecasting-high-frequency-realized.pdf`.

Coverage of this summary: Read the full markdown file: abstract, introduction, related work, the entire methodology section, and the entire experiments section including all tables, the error-diary discussion, and the conclusion.

Known problems with the input: Two results tables (Table.1 'RMSPE, sMAPE, and DM tests' and Table.2 'statistical significance matrix') are badly corrupted by PDF-to-markdown conversion: individual numbers are split across separate table cells (e.g. '0.24' and '7' in different cells) and rows/columns from different tables appear interleaved, so exact digit strings for those two tables could not be reliably reconstructed; only Table.3 and Table.4, which converted cleanly, were used for numbers_used; The paper does not name the exchange, tickers, or precise sample date range for its 'public limit order book dataset'; data fields are marked not stated accordingly; Reader note: several reference-list entries (e.g. on semiconductor manufacturing defect prediction, EV fleet rebalancing, tall-building wind engineering) are unrelated to this paper's subject, which raises doubts about the reliability of the citation list and possibly of the venue's editorial process.
<!-- AUTHORED REGION END -->