---
authors:
- Abdul Rahman
- Neelesh Upadhye
content_hash: sha256:1b1aec96d6f8f0292a556051dd6185d6e7a3bbd577bd96e690a4b5ba1d970e6e
created: 2026-09-27 01:47:00+00:00
page_id: sources/rahman-2024-hybrid-vector-auto-regression-neural-network
page_type: source
related:
- concepts/trade-clock
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/order-flow-prediction
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:be3a5d4fb53890cd2253a5a414509be7863bb139b70341729120ba7af79975e9
source_path: markdown_output/rahman-2024-hybrid-vector-auto-regression-neural-network.md
source_type: paper
tags:
- order-flow-imbalance
- high-frequency-trading
- vector-autoregression
- neural-network
- crypto
- hybrid-model
- clock-trade
- asset-crypto
- harvest-relevant
title: Hybrid Vector Auto Regression and Neural Network Model for Order Flow Imbalance
  Prediction in High-Frequency Trading
updated: '2026-09-27T01:47:00Z'
uuid: aa99ed6e-b90e-549e-bd18-a305ccf26d8b
year: 2024
---

<!-- AUTHORED REGION START -->
# Hybrid Vector Auto Regression and Neural Network Model for Order Flow Imbalance Prediction in High-Frequency Trading

## Summary

The paper asks whether combining a linear Vector Auto Regression (VAR) model with a feedforward neural network (FNN) can forecast Order Flow Imbalance (OFI) - the net difference between buy- and sell-classified trades over a trailing window - more accurately than either model alone, and whether the resulting forecasts can be turned into a useful directional trading signal. OFI is defined as bounded between -1 and 1, and a threshold is applied to the predicted OFI to classify each moment as BUY, SELL, or HOLD.

The VAR component is first trained to forecast future buy and sell order counts, from which an initial OFI forecast is derived; the residual difference between actual and VAR-forecast order counts is then passed to a feedforward neural network with two hidden layers (32 and 16 neurons, ReLU activations, Adam optimizer, learning rate 0.001, batch size 8, 50 training epochs with early stopping) to learn the remaining non-linear pattern, and the two forecasts are summed to give the final OFI prediction.

Tested on 10,000 seconds of continuous Binance buy/sell order data split into a BTCUSD set, an ETCUSDT set, and a synthetic dataset (about 3,000 data points each), the hybrid model consistently produced lower mean-squared and mean-absolute error and higher R-squared than either the VAR-only or FNN-only model, and it also gave the most accurate BUY/SELL/HOLD trading-intensity signal - for example 98.18% accuracy on BTCUSD, versus 97.43% for FNN-only and just 46.61% for VAR-only.

The paper's contribution is applying this VAR-plus-residual-neural-network hybrid specifically to OFI forecasting in high-frequency trading, adding an explicit trading-intensity signal derived from the OFI forecast, and validating the approach on both real cryptocurrency order data and a synthetic dataset built to share the real data's characteristics.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

OFI is defined over a trailing window of length h ending at time T as a function of the difference between the number of buy-classified and sell-classified trades in that window; each trade is labelled BUY or SELL by tracing which side's order was the passive (resting) one. The model forecasts future buy and sell order counts (via VAR) and the residual non-linear pattern (via the FNN) to produce the next OFI value and a derived BUY/SELL/HOLD signal; the paper does not state a fixed value for the window length h used in the reported experiments.

## Data

- **Asset class:** Crypto
- **Instruments:** BTCUSD and ETCUSDT trading pairs on Binance (the paper also refers to the second pair as ETHUSDT in places), plus a synthetically generated dataset built to resemble the real data
- **Venue:** Binance
- **Period:** not stated as calendar dates; the dataset covers 10,000 seconds of continuous buy/sell order data for a single cryptocurrency
- **Granularity:** Tick-level buy/sell order counts; validation subsets of about 3,000 data points each for BTCUSD, ETCUSDT/ETHUSDT, and the synthetic dataset

## Features and Measures

- **Order Flow Imbalance (OFI).** A measure of net trading pressure over a trailing window, computed as a function of the change in the number of buy-classified minus sell-classified trades, bounded between -1 and 1.
- **Trading intensity signal.** A BUY/SELL/HOLD label produced by comparing the (forecast) OFI value against a fixed positive threshold, so that only sufficiently one-sided predicted order flow triggers a directional signal.
- **VAR residuals as FNN input.** The gap between each period's actual buy/sell order counts and the VAR model's linear forecast of them, used as the training target and input for the neural network component of the hybrid model.

## Method

A VAR model of lag order p is fit to the buy and sell order count series to capture their linear autocorrelation and cross-dependence, producing an initial OFI forecast; residuals (actual minus VAR-forecast order counts) are then computed and used to train a feedforward neural network with hidden layers of 32 and 16 ReLU neurons, an Adam optimizer with learning rate 0.001, batch size 8, and up to 50 training epochs with early stopping, whose output is added to the VAR forecast to produce the final OFI prediction. A sensitivity analysis, run manually and via Latin Hypercube Sampling and grid search, evaluated 120 parameter combinations across VAR lag orders (1, 2, 5, 10), several FNN layer sizes, three activation functions, and two optimizers, selecting lag order 2 with a 32-16-2 ReLU/Adam network as best. Performance is judged with Mean Squared Error, Mean Absolute Error, R-squared, and the accuracy/precision of the derived trading-intensity classification, comparing the hybrid model against standalone VAR-only and FNN-only baselines on training data and on three validation datasets (BTCUSD, ETCUSDT, and synthetic).

## Results

- On the primary training dataset, the hybrid model reached MSE 0.00127 and MAE 0.00541 with R-squared 0.9946, versus MSE 0.00133, MAE 0.02240 and R-squared 0.9843 for the FNN-only model.
- On BTCUSD validation data, the hybrid model reached 98.18% trading-intensity accuracy and 96.32% precision, versus 97.43%/95.82% for FNN-only and 46.61%/46.11% for VAR-only.
- On ETCUSDT validation data, the hybrid model reached 96.41% accuracy versus 95.29% for FNN-only and 67.06% for VAR-only.
- On the synthetic dataset, the hybrid model reached an R-squared of 0.999 and 99.77% trading-intensity accuracy, versus an R-squared of 0.435 and 95.40% accuracy for FNN-only.
- VAR-only trading-intensity accuracy stayed close to chance across all three validation datasets (46.61% to 67.06%), showing the linear model alone is not enough for directional signal classification.

## Limitations

- Authors state performance is heavily dependent on the quality and granularity of the high-frequency data and is sensitive to noise in buy/sell order data.
- Authors state the study only used cryptocurrency data (BTCUSD and ETCUSDT/ETHUSDT), so generalisation to other asset classes such as equities or forex has not been validated.
- Authors state the hybrid approach adds computational complexity relative to standalone models, which may limit scalability for real-time/live trading.
- Authors state fixed hyperparameters and network architecture were used in this study and may need further tuning for other datasets or trading contexts.
- Reader note: the paper interchangeably refers to the second cryptocurrency pair as both ETCUSDT and ETHUSDT, and the validation sets are small (about 3,000 points each).

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Abdul Rahman, Neelesh Upadhye (2024). Hybrid Vector Auto Regression and Neural Network Model for Order Flow Imbalance Prediction in High-Frequency Trading.

DOI: 10.48550/arxiv.2411.08382

Text ingested: `markdown_output/rahman-2024-hybrid-vector-auto-regression-neural-network.md`, converted from `raw/ofi-event-clock/rahman-2024-hybrid-vector-auto-regression-neural-network.pdf`.

Coverage of this summary: Read the full paper markdown end to end: introduction, literature review, OFI and VAR/FNN methodology sections, algorithms, experiments and results (including all tables), conclusion, limitations, future work, and the appendices on time-complexity analysis.

Known problems with the input: The paper's abstract and body do not state a venue, journal, or preprint identifier; only the date 'November 14, 2024' is printed, so venue is left blank; The paper names the second real dataset inconsistently as 'ETCUSDT' (Section 4.1, tables) and 'ETHUSDT' (Section 4.5, figures); both spellings are reported as printed.
<!-- AUTHORED REGION END -->