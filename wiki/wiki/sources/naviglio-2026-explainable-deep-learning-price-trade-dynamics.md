---
authors:
- Manuel Naviglio
- Fabrizio Lillo
content_hash: sha256:a0c1d77855a425671268efa6a4fc171550653c73287292973cf162ea913055b2
created: 2026-09-27 01:47:00+00:00
page_id: sources/naviglio-2026-explainable-deep-learning-price-trade-dynamics
page_type: source
related:
- concepts/trade-clock
- concepts/price-impact
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- entities/fabrizio-lillo
revision_id: 1
schema_version: 2
source_hash: sha256:a19c86bcf11de6fe9d09eab25313bb4fe150140a9e4fef2ce7182b17314fc129
source_path: markdown_output/naviglio-2026-explainable-deep-learning-price-trade-dynamics.md
source_type: paper
tags:
- explainable-ai
- shap-values
- price-impact
- order-flow
- limit-order-book
- neural-networks
- tick-size-regimes
- clock-trade
- asset-equity
- harvest-core
title: 'Explainable Deep Learning for Price–Trade Dynamics: From Black-Box Forecasts
  to Effective Parametric Models'
updated: '2026-09-27T01:47:00Z'
uuid: 82683fee-5289-596f-85b7-f2281c6ddd91
year: 2026
---

<!-- AUTHORED REGION START -->
# Explainable Deep Learning for Price–Trade Dynamics: From Black-Box Forecasts to Effective Parametric Models

## Summary

The paper asks whether the extra forecasting power of deep neural networks over linear models of price and trade dynamics reflects genuine, economically interpretable structure, or is just a black-box artifact. It compares a linear vector-autoregression (VAR) benchmark with a deep feed-forward network, both predicting next-trade log returns and signed volumes from lagged returns and lagged signed volumes, for five large-tick and five small-tick NASDAQ stocks.

The approach treats the trained network not just as a forecaster but as a device for structural discovery: Shapley (SHAP) values decompose its predictions into the contribution of each lagged input, and these contributions are further aggregated into conditional response surfaces that can be checked against equivalent averages computed directly from the data. The authors also recover an instantaneous (same-trade) order-flow effect on returns from the residuals left over after the lagged models are fitted.

The main finding is that the network's advantage over the VAR is concentrated in specific, stable nonlinear mechanisms: lagged signed volume produces a sign-preserving, saturating contribution to both future returns and future signed volume (nonlinear price impact and order-flow persistence), while lagged returns act mainly as a state variable that reinforces this order-flow signal when the previous trade barely moved the price and attenuates or reverses it when the previous return was large. These patterns are confirmed both in the model's Shapley decomposition and in plain conditional averages of the data, and they differ somewhat between large-tick and small-tick stocks.

What is new is that these extracted mechanisms are then written down as an explicit, low-dimensional parametric model (a one-lag version, plus a multi-lag extension with a shared nonlinear shape and geometric lag decay). This reduced model beats the linear VAR and matches, and in many cases exceeds, the full neural network's out-of-sample performance, despite using far fewer parameters and only the most recent lag(s). The paper frames this as a general route from opaque deep-learning forecasts to parsimonious, calibratable, economically meaningful models of price and trade dynamics.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

Observations are indexed in trade time t, one step per executed trade (specifically, per execution of a visible limit order; hidden-order executions are excluded and orders at the same timestamp and sign are aggregated). The price used is the mid-price of the book immediately before each such execution. Models predict the next trade-time observation, i.e. a one-trade-ahead horizon: the next log return r_t = log(p_{t+1}/p_t) and the next signed volume v_t, from p lagged trade-time returns and signed volumes (p = 20 in the main specification).

## Data

- **Asset class:** Equities
- **Instruments:** Ten NASDAQ-listed stocks, split into five large-tick names (BAC, INTC, CSCO, CMCSA, PFE) and five small-tick names (AMZN, AAPL, GILD, TSLA, NVDA)
- **Venue:** NASDAQ (LOBSTER limit order book data)
- **Period:** June 2024
- **Granularity:** Trade-time (event-by-event) observations built from LOBSTER message and order-book files, restricted to executions of visible limit orders; the first and last 30 minutes of trading each day are removed, observations outside the [0.005, 0.995] quantile range are removed, and the neural-network inputs are normalized; the first 50% of the sample is used for training and the remaining 50% for out-of-sample testing

## Features and Measures

- **signed volume (order flow).** The volume of a trade signed positive for buyer-initiated and negative for seller-initiated trades; used both as a predicted variable and as a lagged regressor in the return and volume equations.
- **trade-time log return.** The log change in the mid-price between consecutive trade-time observations, defined as the log of the ratio of the next mid-price to the current one, used as the return variable being modeled and predicted.
- **Shapley (SHAP) lag decomposition.** An additive decomposition of the neural network's prediction into the contribution of each lagged return and lagged signed-volume input, computed with the DeepExplainer approximation, used to isolate which lags and which variables drive the forecast.
- **SHAP-inspired nonlinear parametric model.** A reduced-form model built directly from the shapes revealed by the Shapley decomposition: a saturating, sign-preserving function of lagged signed volume plus a correction term, driven by the magnitude of the lagged return and the sign of the lagged order flow, that reinforces or reverses that signal.

## Method

The baseline linear model is a vector autoregression (VAR) on log returns and signed volumes, with lag order p. The nonlinear benchmark is a deep feed-forward neural network with three hidden dense layers (64, 64, and 32 neurons) with hyperbolic-tangent activations and a linear output layer, jointly predicting the next return and next signed volume from the same p lagged returns and signed volumes; it is trained by minimizing mean squared error with the Adam optimizer. A lag-sensitivity study is used to fix p = 20 for the main analysis, since both models' out-of-sample performance saturates at short lags. Because both models use only lagged information, any instantaneous (same-trade) dependence between return and order-flow innovations is left in the residuals; the paper recovers this contemporaneous effect separately with a nonparametric binned estimator of a residual price-impact function, under a triangular ordering assumption in which the order-flow innovation is treated as contemporaneously prior to the price revision.

To interpret the trained network, Shapley (SHAP) values are computed via the DeepExplainer approximation, decomposing each prediction into the contribution of each lagged return and lagged signed-volume input. These per-feature contributions are aggregated into binned conditional response surfaces as a function of the most recent lagged return or lagged signed volume, split by the sign or regime of the other variable, and compared against equivalent surfaces computed directly from the empirical data and from the linear VAR. Guided by the shapes of these surfaces, a parsimonious nonlinear parametric model is specified (a saturating sign-preserving term in lagged signed volume plus a return-state correction) and calibrated separately for the return and volume equations by nonlinear least squares on the same training split; a multi-lag extension shares the same nonlinear shape across lags with a geometric (exponentially decaying) lag intensity. All models (VAR, DNN, one-lag reduced parametric, and multi-lag parametric) are judged by out-of-sample R-squared for returns and for signed volumes, computed separately for each stock and averaged within the large-tick and small-tick buckets.

## Results

- At lag p = 20, the deep neural network improves out-of-sample R-squared over the VAR for returns in almost all stocks, e.g. for BAC the return R-squared rises from 0.0494 (VAR) to 0.0591 (DNN).
- For signed volumes the DNN improves over the VAR for every small-tick stock, but for large-tick stocks the two models are closer and the VAR remains competitive in some cases.
- Large-tick stocks show more predictable returns than signed volumes, while small-tick stocks show more predictable signed volumes than returns, under both the VAR and the DNN.
- Shapley values show that contributions are concentrated overwhelmingly at the first lag across both the return and volume equations and both tick-size regimes, with explanatory power decaying rapidly at longer lags.
- Lagged signed volume produces sign-preserving, saturating contributions to both predicted return and predicted volume, while lagged returns act as a state variable: the model reinforces the sign of lagged order flow when the previous return is near zero and attenuates or reverses it when the previous return is large.
- The one-lag SHAP-inspired parametric model raises the out-of-sample return R-squared for BAC from 0.0494 (VAR) to 0.0934, for CSCO from 0.0764 to 0.1156, and for PFE from 0.0356 to 0.0845, in each case exceeding the DNN's corresponding 0.0591, 0.0982, and 0.0367.
- The multi-lag parametric extension (exponential lag decay, p = 20) improves further on signed-volume forecasting, for example raising AMZN's volume R-squared from 0.0892 (one-lag reduced model) to 0.1047, above the DNN's 0.0705.

## Limitations

- The analysis covers a single month (June 2024) and ten U.S. equities; the authors state that testing on longer periods, more assets, and different market regimes is needed to assess how stable the extracted nonlinear mechanisms are.
- The baseline parametric model imposes a symmetric functional form for the return-state correction; the authors note this symmetry is only approximate for large-tick stocks and leave an asymmetric correction for future work.
- The neural-network benchmark is a single feed-forward architecture (three hidden layers, tanh activations) chosen for transparency; the authors note that convolutional or recurrent architectures could in principle be used but were not tested here.
- The contemporaneous (structural) impact function is identified only under a triangular ordering assumption, that the order-flow innovation is contemporaneously prior to the price revision, which is not tested against alternative orderings.
- Reader note: the Shapley (SHAP) attributions are approximate, model-based explanations rather than causal effects, a distinction the authors themselves flag.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/price-impact|price impact]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[entities/fabrizio-lillo|Fabrizio Lillo]]

## Citation

Manuel Naviglio, Fabrizio Lillo (2026). Explainable Deep Learning for Price–Trade Dynamics: From Black-Box Forecasts to Effective Parametric Models.

DOI: 10.2139/ssrn.7436140

Text ingested: `markdown_output/naviglio-2026-explainable-deep-learning-price-trade-dynamics.md`, converted from `raw/ofi-event-clock/naviglio-2026-explainable-deep-learning-price-trade-dynamics.pdf`.

Coverage of this summary: Read the abstract, introduction, all of Section 2 (price-trade model framework, linear VAR and neural-network specifications, residual contemporaneous dependence), Section 3 (data), Section 4 (forecasting performance results), Section 5 (Shapley/SHAP explainability, aggregated conditional response surfaces, structural shock decomposition), Section 6 (SHAP-inspired parametric model construction, calibration, and multi-lag extension), and Section 7 (conclusions). Did not read the mathematical appendices (A-G), which contain supporting derivations and additional per-stock figures.

Known problems with the input: Many display equations and some figures are rendered in the converted markdown only as "picture intentionally omitted" placeholders; their content is inferred only from surrounding text and figure captions, not read directly; No journal, conference, or working-paper series is printed on the paper itself, so venue is left empty; the document shows only a submission/dated cover (September 9, 2026) and institutional affiliation.
<!-- AUTHORED REGION END -->