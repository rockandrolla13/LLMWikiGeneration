---
authors:
- Mamoune Khadira
content_hash: sha256:8f7c8a0397363288c80e38b9271c060755d3cf5974ae3acf9a35408ebfd12a71
created: 2026-09-27 01:47:00+00:00
page_id: sources/khadira-2026-path-signatures-universal-feature-extractors-limit
page_type: source
publication_venue: Working Paper — SSRN / arXiv Preprint
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/transformers
- concepts/high-frequency-trading
- concepts/order-flow-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:b27f686e4a05ad25e0bd24961a05e6695265b3c587255c98bfd93d33c82f029a
source_path: markdown_output/khadira-2026-path-signatures-universal-feature-extractors-limit.md
source_type: paper
tags:
- path-signature
- limit-order-book
- rough-path-theory
- feature-extraction
- mid-price-prediction
- high-frequency-trading
- interpretability
- gpu-acceleration
- clock-event
- asset-equity
- harvest-relevant
title: Path Signatures as Universal Feature Extractors for Limit Order Book Mid-Price
  Prediction
updated: '2026-09-27T01:47:00Z'
uuid: c7f84d52-fb8c-566b-9628-78731a5d3568
year: 2026
---

<!-- AUTHORED REGION START -->
# Path Signatures as Universal Feature Extractors for Limit Order Book Mid-Price Prediction

## Summary

The paper asks whether a mathematically lossless encoding of the limit order book's path, the path signature, can outperform manual feature engineering (order book imbalance, spread, VPIN, microprice) and deep-learning models (DeepLOB, LSTM, Transformer) at predicting the next mid-price direction, without hand-designed features. The path signature, based on iterated integrals and rough path theory, summarises how a multidimensional path evolved over a window rather than just its current state.

The approach builds a 4-dimensional path from best bid price, best ask price, best bid volume and best ask volume over a rolling window, computes the signature truncated at order 4, yielding 341 features, applies a lead-lag path augmentation, and feeds the result into a linear model and a LightGBM model. It is evaluated on the FI-2010 benchmark limit order book dataset and on proprietary US equity tick data from 2020 to 2024 for ten large-cap names, using a purged walk-forward validation scheme with an embargo between train and test.

The signature-based features improve the Information Coefficient over hand-crafted features and outperform DeepLOB, LSTM and Transformer baselines while using far fewer parameters and running faster. The paper also applies SHAP analysis to identify which signature terms matter most, arguing that the top terms, cross-covariations between price and volume paths and Lévy areas between bid and ask price paths, map onto established microstructure ideas such as order-flow direction and inventory pressure, so the signature is presented as an interpretable, structured decomposition rather than an opaque feature set.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

For the US equity experiments, a 4-dimensional path of best bid price, best ask price, best bid volume and best ask volume is built from a rolling 500ms window of raw tick data, typically 40-80 ticks per window for liquid US equities, with windows updated every 100ms and the prediction target being mid-price direction 100-500ms ahead. For the FI-2010 benchmark, the same signature features are computed from 10-level limit order book snapshots and the target is mid-price direction k=10 or k=50 LOB events ahead, using a fixed first-7-day train, last-3-day test split. The window boundaries are fixed-time, but the signature transform applied inside each window is itself invariant to how irregularly the underlying ticks are spaced in time.

## Data

- **Asset class:** Equities
- **Instruments:** FI-2010 benchmark: NASDAQ-listed stocks with a 10-level limit order book (the abstract states 10 stocks, the results section and Table 1 caption state five stocks); US equity tick data: SPY, AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, JPM, GS
- **Venue:** NASDAQ (FI-2010); not stated for the proprietary US equity tick data
- **Period:** FI-2010: 10 trading days; US equity tick data: 2020-2024
- **Granularity:** Tick-level order book updates aggregated into rolling 500ms path windows updated every 100ms (US equity), or 10-level LOB snapshots indexed by LOB event count (FI-2010)

## Features and Measures

- **path signature (order k).** The collection of iterated integrals, tensor products of increments, of the 4-dimensional LOB path up to order k: order 1 gives level means, order 2 gives pairwise covariations and Lévy areas, order 3 gives triple interactions, order 4 gives four-body interaction terms.
- **truncated signature feature set (order 4, 341 features).** The signature truncated at order 4 over the 4-dimensional path, yielding 1+4+16+64+256=341 features, used directly as inputs to a linear or LightGBM model.
- **lead-lag augmentation.** A path transform, following Chevyrev and Kormilitzin (2016), that embeds the raw path into a doubled dimension by including both current and previous tick values before computing the signature, enriching second-order terms with quadratic-variation information.
- **Lévy area between bid and ask price paths.** A second-order signature term interpreted as the signed area between the bid and ask price paths, read by the authors as a momentum-asymmetry, informed-order-flow proxy in a Kyle (1985) framework.

## Method

Signature features, orders 1-4, 341 dimensions, are computed per window via the GPU-accelerated Signatory library and fed into a linear model and a LightGBM model, compared against seven hand-crafted features (OBI, spread, VPIN, microprice among them), DeepLOB, an LSTM and a Transformer baseline. On FI-2010, performance is measured by directional accuracy and Information Coefficient, the Pearson correlation between predicted and realized direction, at k=10 and k=50 LOB-event horizons using a fixed 7-day train, 3-day test split. On US equity tick data from 2020-2024, the same signature and baseline features are evaluated at 100ms, 200ms and 500ms horizons under a purged walk-forward cross-validation scheme with a 3-month embargo between train and test; annualized Sharpe ratios are estimated from the Information Coefficient via the paper's own approximation formula rather than a direct backtest. Feature importance is assessed via SHAP applied to the LightGBM model on the US equity data, and computational cost is benchmarked on an A100 GPU and a Xeon Gold 6326 CPU over 10,000 windows of 50 ticks.

## Results

- On the FI-2010 benchmark at k=10 LOB events, the signature-plus-LightGBM model reached 74.6% directional accuracy and an Information Coefficient of 0.082, versus 65.4% accuracy and 0.052 for the seven hand-crafted features and 71.2% accuracy and 0.067 for DeepLOB.
- Adding the 7 hand-crafted features to the 341 signature features gave only a marginal further gain, to 75.1% accuracy and an Information Coefficient of 0.084 at k=10, read by the authors as evidence the signature already subsumes standard features.
- On 2020-2024 US equity tick data, the order-4 signature reached an Information Coefficient of 0.081 at a 100ms horizon versus 0.048 for hand-crafted features and 0.062 for DeepLOB, with an estimated annual Sharpe ratio of 3.07, rising to 3.14 combined with standard features.
- A truncation-depth check found signature orders 1-4 explain 94.2% of predictable variance on held-out data, with order 5 adding under 1.1% more at a cost of 1,024 extra features.
- The lead-lag path augmentation improved the Information Coefficient by 8-12% in the reported experiments at no extra computational cost.
- GPU-accelerated signature extraction via the Signatory library took 0.12ms per 500ms window on a single A100 GPU stream, 0.048ms batched, and 0.82ms on a Xeon CPU, versus 2.1ms for DeepLOB and 1.8ms for LSTM inference.
- During the February-March 2020 volatility regime, the optimal truncation depth increased from order 4 to order 5 for two of the ten US equity test assets.

## Limitations

- Authors state the primary limitation is data stationarity: window length, normalization period and truncation depth are regime-sensitive and require recalibration; for example, optimal truncation rose from order 4 to order 5 for some assets during the February-March 2020 volatility regime.
- Reader note: the abstract states the FI-2010 evaluation covers 10 stocks, but the results section and Table 1's caption say five NASDAQ-listed stocks; the paper does not resolve this discrepancy.
- Reader note: the proprietary US equity tick data (2020-2024) is not shared and its exact venue or tick source is not described, so results cannot be independently reproduced.
- Reader note: the reproducibility code link given is a bracketed placeholder, github.com/[anonymous]/lobsignature-features, not a resolvable repository, so the implementation could not be verified from the paper alone.
- Interpretability analysis via SHAP is applied only to the LightGBM model on US equity data, not to the FI-2010 results or the linear signature model.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/transformers|transformers]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-flow-prediction|order flow prediction]]

## Citation

Mamoune Khadira (2026). Path Signatures as Universal Feature Extractors for Limit Order Book Mid-Price Prediction. Working Paper — SSRN / arXiv Preprint.

DOI: 10.5281/zenodo.19732419

Text ingested: `markdown_output/khadira-2026-path-signatures-universal-feature-extractors-limit.md`, converted from `raw/ofi-event-clock/khadira-2026-path-signatures-universal-feature-extractors-limit.pdf`.

Coverage of this summary: Read the entire working paper: abstract, mathematical framework, LOB path construction, FI-2010 and US-equity empirical results tables, SHAP interpretability analysis, computational-performance benchmarks, discussion and limitations, and references.

Known problems with the input: Abstract states the FI-2010 evaluation covers 10 stocks; Table 1's caption and surrounding text say five NASDAQ-listed stocks, an internal inconsistency the paper does not resolve; The reproducibility code link is a bracketed placeholder, github.com/[anonymous]/lobsignature-features, not a resolvable repository; No author institution or university is given, only 'Quantitative Research Division' with no organization name, so author_affiliations is effectively unstated beyond that label; This is a working paper (SSRN/arXiv preprint format) rather than a peer-reviewed publication; the reported Sharpe ratios are derived via the paper's own approximation formula from Information Coefficient rather than a direct backtest.
<!-- AUTHORED REGION END -->