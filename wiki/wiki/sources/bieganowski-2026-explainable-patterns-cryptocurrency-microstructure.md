---
authors:
- Bartosz Bieganowski
- Robert Slepaczuk
content_hash: sha256:5fadedcd433a455e8e2198da7161aaa1d0d86a790cad91286c560438da5a717b
created: 2026-09-27 01:47:00+00:00
page_id: sources/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/adverse-selection
- concepts/bid-ask-spread
- concepts/market-making
- concepts/market-microstructure
- concepts/micro-price
revision_id: 1
schema_version: 2
source_hash: sha256:3376fc1b00cec1fafbb566d5b11554b057af5293463d31bbd3056adea34bd88c
source_path: markdown_output/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure.md
source_type: paper
tags:
- cryptocurrency
- limit-order-book
- shap
- catboost
- order-flow-imbalance
- flash-crash
- market-making
- adverse-selection
- clock-calendar
- asset-crypto
- harvest-relevant
title: Explainable Patterns in Cryptocurrency Microstructure
updated: '2026-09-27T01:47:00Z'
uuid: efdc061b-d322-507a-9b39-ec8d374cf400
year: 2026
---

<!-- AUTHORED REGION START -->
# Explainable Patterns in Cryptocurrency Microstructure

## Summary

The paper asks whether short-horizon return predictability in cryptocurrency limit order books is universal: does the same compact set of order-book and trade features carry similar importance and similar functional shape across coins of very different market capitalization? It studies Binance Futures perpetual order books and trades at 1-second frequency from January 1, 2022 to October 12, 2025 for five assets spanning roughly two orders of magnitude in market cap (BTC, LTC, ETC, ENJ, ROSE).

The approach trains a CatBoost gradient-boosted tree model per asset on engineered top-of-book and trade-flow features (spreads, relative prices, order-flow imbalance, and buy/sell VWAP-to-mid deviations) to predict a very short-horizon (3-second) log mid-price return, using a direction-aware GMADL training/model-selection objective alongside a standard squared-error baseline, and rolling time-series cross-validation with a purge gap between train and test windows, plus Optuna-based hyperparameter search. SHAP (TreeSHAP) values on held-out data give feature importance rankings and dependence shapes, which the authors interpret against Kyle- and Glosten-Milgrom-style microstructure theory.

Across the five assets, the same handful of features (order-flow imbalance, spread, VWAP-to-mid deviations) dominate SHAP importance, and the shapes of their dependence curves are similar: order-flow imbalance has a broadly monotone, concave-at-the-extremes effect, wider spreads dampen predictive effect, and VWAP-to-mid deviations show a short-lived, reversion-like asymmetry. A conservative top-of-book taker backtest and a maker (passive, spread-capture) backtest translate the signals into trading strategies; taker strategies are statistically significant against buy-and-hold for ETC, ENJ and ROSE at the 5% level, while none of the maker strategies are.

The main novel contribution is a robustness test around the October 10, 2025 flash crash (triggered by a surprise US tariff announcement on China): the taker strategy profited by shorting into the crash using the order-flow-imbalance signal, while the maker strategy suffered large losses from being adversely selected on its bid-side quotes, which the authors present as a live illustration of classic adverse-selection theory and a caution about systemic risk from widespread use of similar algorithmic signals.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order book and trade data are synchronized and sampled at a fixed 1-second frequency. The prediction target is the log return of the mid price over a fixed 3-second horizon from each snapshot, but position management in the backtests is event-driven, so realized holding times can be shorter than the 3-second horizon.

## Data

- **Asset class:** Crypto
- **Instruments:** Five Binance Futures perpetual contracts - BTC, LTC, ETC, ENJ, and ROSE - which as of January 1, 2022 occupied market-capitalization ranks 1, 20, 40, 60, and 100 respectively; a supplementary comparison also uses the W/USDT spot instrument against its finer-tick W/USDT perpetual future
- **Venue:** Binance Futures
- **Period:** January 1, 2022 to October 12, 2025
- **Granularity:** Order book and trade data synchronized at 1-second frequency; the return-prediction target is a 3-second-ahead log mid-price return

## Features and Measures

- **top-of-book metrics.** Mid price, bid-ask spread, and level-1 (best bid/ask) volumes, meant to capture immediate liquidity and trading cost.
- **order flow / trade imbalance.** Net traded volume and related signed order-flow measures capturing the pressure exerted by aggressive buyers versus sellers.
- **VWAP-to-mid deviation.** The distance of the volume-weighted average trade price (computed separately for buy and sell trades) from the mid price, used as a proxy for recent one-sided trading pressure or informed trading.
- **GMADL objective.** The Generalized Mean Absolute Directional Loss, a direction-aware loss/scoring function that rewards correctly signed, magnitude-scaled return predictions more than plain squared error.

## Method

For each asset separately, a CatBoost gradient-boosted decision tree model is trained to predict the 3-second-ahead log mid-price return from the engineered feature set, using rolling time-series cross-validation with a temporal purge gap between training and validation windows and inner (training-only) folds for Optuna-based Bayesian hyperparameter search; models are trained under squared-error loss and selected using in-sample GMADL performance, with an R-squared-optimized variant kept as a robustness check.

Feature attribution uses SHAP (TreeSHAP) on held-out samples to obtain global importance rankings and local dependence-plot-like curves, compared across assets via rank correlation of mean-absolute SHAP values. Economic significance is assessed with two backtests using the same signals: a conservative taker (market order) backtest that marks inventory to the unfavorable side of the book, and a maker (passive limit order, queue-priority-simulated) backtest, plus a blended combination of the two; strategies are compared against buy-and-hold using annualized return, annualized standard deviation, information-ratio variants, max drawdown, max loss duration, and a t-test of mean return versus buy-and-hold.

## Results

- Across BTC, LTC, ETC, ENJ, and ROSE, the same features (order flow imbalance, spread, VWAP-to-mid deviations) dominate mean absolute SHAP importance, and feature-importance rankings are highly correlated across assets.
- SHAP dependence shapes are consistent across assets: order-flow imbalance shows a largely monotone effect with concavity at extremes, wider spreads associate with weaker predictive effect, and VWAP-to-mid deviations show short-horizon, reversion-like asymmetries.
- For the W/USDT spot instrument versus its finer-tick perpetual future, the futures mid-price's position within the spot bid-ask spread correlates with spot order-book imbalance at 0.94, supporting imbalance as a proxy for the latent efficient price.
- In the taker backtest, mean returns are statistically significant against buy-and-hold at the 5% level for ETC, ENJ, and ROSE, but not for BTC or LTC; in the maker backtest, no asset shows a significant mean return versus buy-and-hold.
- The October 10, 2025 flash crash, triggered by a surprise U.S. tariff announcement, produced over $19 billion in liquidated leveraged positions within 24 hours and an 18% drop in Bitcoin from its all-time high.
- During that crash, the taker strategy shorted into the decline and held the position for about 20 seconds (versus a typical one-to-two-second holding time), capturing a large profit and validating order-flow imbalance as a directional signal even in extreme conditions.
- During the same crash, the maker strategy was repeatedly filled on its bid-side quotes without offsetting ask-side fills, accumulating a losing long position and suffering a sharp equity decline around 23:20.
- A blended strategy allocating 50% of capital to the taker leg and 50% to the maker leg had lower volatility but a weaker aggregate return than the pure taker strategy, because of the maker leg's poor performance.

## Limitations

- The analysis is limited to a single short prediction horizon (3 seconds) and a single model family (CatBoost).
- The authors note potential venue- or regime-specific effects, and that causal identification of order-flow effects remains an open avenue for future work, for example via instrumental strategies or market-design changes.
- The authors state that latency is not explicitly modeled in the taker backtest, so results should be interpreted as an upper bound achievable only in the fastest execution regime.
- Reader note: the flash-crash robustness check covers a single stress event (October 10, 2025), so its generality to other extreme-event types is untested within the paper.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-making|market making]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/micro-price|Micro-Price]]

## Citation

Bartosz Bieganowski, Robert Slepaczuk (2026). Explainable Patterns in Cryptocurrency Microstructure.

DOI: 10.2139/ssrn.6159346

Text ingested: `markdown_output/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure.md`, converted from `raw/ofi-event-clock/bieganowski-2026-explainable-patterns-cryptocurrency-microstructure.pdf`.

Coverage of this summary: Read the full paper markdown: abstract, introduction, literature review, data section, methodology and performance-metrics section, models section (CatBoost, hyperparameter optimization, SHAP interpretation), the SHAP explanations section including the tick-size subsection, both backtesting sections and the combined-strategy discussion, the October 10 2025 flash-crash case study, conclusion, and reference list; the results tables (rounded backtest statistics and t-test table) were read but not independently recomputed.

Known problems with the input: The markdown OCR renders a diacritic mark unreliably in the second author's surname (printed as 'Slepaczuk' with a floating accent mark); it is transcribed here without the mark since the correct placement could not be confirmed from the markdown alone; Several figures (SHAP summary plots, dependence plots, equity curves) are described only by their captions in the markdown conversion, with the plotted content itself omitted, so their visual patterns are reported only as characterized in the paper's own text.
<!-- AUTHORED REGION END -->