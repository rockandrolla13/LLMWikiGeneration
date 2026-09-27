---
authors:
- Trent Spears
- Stefan Zohren
- Stephen Roberts
content_hash: sha256:cebe33ea88fee78ba66ef5f91e37fcf6a232bc683c7c5b6de9366717e36def9b
created: 2026-09-27 01:47:00+00:00
page_id: sources/spears-2020-investment-sizing-deep-learning-prediction-uncertainties
page_type: source
related:
- concepts/intrinsic-time
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/volatility-targeting
- entities/stefan-zohren
revision_id: 1
schema_version: 2
source_hash: sha256:1f303301194779cc6495b7e9ca33da4f4a33b70aceb7ecd5feaa333647f10513
source_path: markdown_output/spears-2020-investment-sizing-deep-learning-prediction-uncertainties.md
source_type: paper
tags:
- deep-learning
- uncertainty-estimation
- position-sizing
- eurodollar-futures
- interest-rate-curve
- high-frequency-trading
- dropout
- clock-intrinsic
- asset-bonds-rates
- harvest-relevant
title: Investment sizing with deep learning prediction uncertainties for high-frequency
  Eurodollar futures trading
updated: '2026-09-27T01:47:00Z'
uuid: 984f1c91-df61-516f-a177-e4df5f71615f
year: 2020
---

<!-- AUTHORED REGION START -->
# Investment sizing with deep learning prediction uncertainties for high-frequency Eurodollar futures trading

## Summary

The paper studies whether uncertainty estimates from a deep learning price-prediction model can be used to size trading positions in a principled, data-driven way, rather than trading a fixed unit size, when forecasting short-horizon moves in a segment of the Eurodollar futures interest-rate curve.

Level 1 order-book data for Eurodollar futures contracts EDc7 through EDc15 are used to build a rolling window of 100 recent microprice curve observations, down-sampled whenever any contract's microprice moves by at least a stated cutoff. Two architectures, a multi-layer perceptron (MLP) and a CNN-LSTM with an inception module, predict the next curve observation as a multivariate Gaussian mean and covariance, giving aleatoric uncertainty via a heteroscedastic loss, and dropout sampling at test time approximates epistemic uncertainty. An optimal position-size formula, derived by maximizing an assumed Sharpe ratio objective, converts the predicted mean and total uncertainty for each contract into a continuous investment size.

Trading strategies that size positions using the combined aleatoric-plus-epistemic uncertainty estimate achieved the highest cumulative five-month out-of-sample Sharpe ratio in most of the tested model and covariance combinations, outperforming a strategy with no uncertainty-based sizing and a strategy that instead scales by realised window volatility. The CNN-LSTM Inc model also had lower validation loss than the MLP, and the benefit of uncertainty-based sizing persisted, though it narrowed, as transaction costs increased.

What is new is applying learned aleatoric and dropout-based epistemic uncertainty jointly to continuous position sizing in a multivariate, correlated interest-rate curve setting, rather than to a single asset or a discrete buy, sell, or hold decision, and deriving a closed-form Sharpe-optimal sizing rule under a simplifying independent, equal-frequency-of-opportunity assumption.

## Clock and Sampling

**Intrinsic time: one observation per price move of a set size.**

See [[concepts/intrinsic-time|Intrinsic Time]].

Curve observations are recorded only when at least one contract's microprice has moved by more than a fixed cutoff since the last recorded observation, an intrinsic, threshold-triggered sampling rule, rather than at fixed calendar intervals; each observation is paired with a rolling window of the previous 100 such observations, and the prediction target and horizon are the next intrinsic-clock event, a next-event prediction rather than a fixed time-ahead prediction.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** Eurodollar futures continuous contracts EDc7 to EDc15 (a segment of the interest rate curve)
- **Venue:** CME Group
- **Period:** Each US trading day of 2018.
- **Granularity:** Level 1 (best bid/ask/volume) order book quotes with some trade execution data, down-sampled to an intrinsic microprice-move threshold; rolling windows of 100 observations.

## Features and Measures

- **Microprice.** A volume-weighted combination of best bid and ask prices and volumes used as the underlying price series for each futures contract, chosen over the simple midpoint to reflect order-book imbalance.
- **Aleatoric uncertainty (heteroscedastic variance-covariance).** A learned, input-dependent variance-covariance matrix output by the network alongside its mean price-change prediction, estimated via a Cholesky-parameterized negative log-likelihood loss without explicit variance labels.
- **Epistemic uncertainty (dropout sampling).** An approximation to model uncertainty obtained by generating many stochastic forward passes with dropout enabled at test time and computing the spread across those samples.
- **Sharpe-optimal investment size.** A closed-form position-sizing rule, derived by maximizing an assumed Sharpe ratio objective, that scales trade size according to each contract's predicted mean return relative to its predicted total uncertainty.

## Method

Two competing network architectures, a two-hidden-layer MLP and a CNN-LSTM with an inception module adapted from prior deep limit-order-book work, take the rolling window of curve observations as input and output both a predicted next curve observation and a variance-covariance matrix, diagonal or full, parameterizing a multivariate Gaussian. Models are trained in Keras with the Adam optimizer, in batches, with early stopping on validation loss, and evaluated month by month: training on earlier months, validating on the next month, and testing the month after that.

Epistemic uncertainty is estimated by running each trained model many times with dropout active at test time and averaging the resulting predictions and their spread; a Bayesian linear (ordinary least squares) model with matrix-normal and inverse-Wishart priors is used as a simpler baseline for both point prediction and uncertainty.

Trading performance is judged mainly by out-of-sample Sharpe ratio, monthly and cumulated over five months, for a family of position-sizing strategies: a fixed-size long/short baseline, sizing by realised window volatility, sizing by aleatoric uncertainty alone, and sizing by aleatoric plus epistemic uncertainty; results are also reported after subtracting a stated transaction cost per unit volume traded, at increasing multiples of that cost.

## Results

- CNN-LSTM Inc had lower validation loss than the MLP on average by a factor of 2.0, and beat the MLP on mean-squared error in 3 of 5 test months with one-tailed t-test p-values of at most 0.0001.
- On average across all months, CNN-LSTM Inc's mean-squared error was 2.5% smaller than the MLP's.
- The cumulative five-month Sharpe ratio was highest for the aleatoric-plus-epistemic sizing strategy in three of the four model and covariance combinations, with aleatoric-only sizing second in each of those cases.
- Relative outperformance of aleatoric-plus-epistemic sizing versus the no-uncertainty baseline strategy ranged from 2.9% to 12.7%, and it beat the realised-volatility-sizing strategy by at least 11.3%.
- The median daily bid-ask spread was 0.5 basis points for each contract throughout 2018, versus a much smaller assumed transaction cost of 0.005bps per unit volume, 5% of the trading threshold.
- For the diagonal-covariance MLP, Sharpe ratios of the two uncertainty-based sizing strategies varied by less than 1.8% across three tested non-zero dropout rates, while the no-uncertainty baseline strategy's Sharpe ratio was much more sensitive to the dropout rate.

## Limitations

- The dataset covers only one calendar year and a subset of the 44 available Eurodollar futures contracts (EDc7 through EDc15).
- Transaction costs analyzed are stated to be well below the median bid-ask spread, so the strategy's real-world profitability net of the full spread is not established.
- The Sharpe-optimal sizing formula is derived under simplifying assumptions of independent returns and an equal number of trading opportunities per contract, which may not hold in practice.
- Reader note: hyperparameters such as dropout rate and weight regularization were tuned by grid search on the same validation data used for model and strategy selection, which can inflate reported out-of-sample performance.

## Related

- [[concepts/intrinsic-time|Intrinsic Time]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/volatility-targeting|volatility targeting]]
- [[entities/stefan-zohren|Stefan Zohren]]

## Citation

Trent Spears, Stefan Zohren, Stephen Roberts (2020). Investment sizing with deep learning prediction uncertainties for high-frequency Eurodollar futures trading.

DOI: 10.2139/ssrn.3664497

Text ingested: `markdown_output/spears-2020-investment-sizing-deep-learning-prediction-uncertainties.md`, converted from `raw/ofi-event-clock/spears-2020-investment-sizing-deep-learning-prediction-uncertainties.pdf`.

Coverage of this summary: Read the full markdown paper, including summary, introduction, data commentary and preprocessing, model specification (aleatoric and epistemic uncertainty), trading strategy derivation, results, conclusion, and appendix (sizing derivation, data and modelling notes, Bayesian baseline).

Known problems with the input: Several equations (microprice definition, loss functions, the Sharpe-optimal sizing derivation, and the Bayesian baseline formulas) are rendered as 'picture... omitted' placeholders in the converted markdown and were not transcribed.
<!-- AUTHORED REGION END -->