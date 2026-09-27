---
authors:
- Zhiming Hu
content_hash: sha256:343c8c042629d357f8d66927a3a39eda9d8c4b441e153e92f50c5ea9d83e55bd
created: 2026-09-27 01:47:00+00:00
page_id: sources/hu-2025-volatility-aware-temporal-transformer-intraday-risk
page_type: source
publication_venue: Frontiers in Business and Finance
related:
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/transformers
- concepts/lstm-networks
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/realized-variance
- concepts/deep-learning-for-finance
- concepts/queue-imbalance
revision_id: 1
schema_version: 2
source_hash: sha256:6e0d8a262b87cd402f56f35b49bc78bdc62698a5f01f01982856b77341f67765
source_path: markdown_output/hu-2025-volatility-aware-temporal-transformer-intraday-risk.md
source_type: paper
tags:
- transformers
- limit-order-book
- realized-volatility
- market-microstructure
- attention-mechanism
- garch
- order-flow-imbalance
- deep-learning
- clock-calendar
- asset-equity
- harvest-relevant
title: A Volatility-Aware Temporal Transformer for Intraday Risk Forecasting with
  Market Microstructure Signals
updated: '2026-09-27T01:47:00Z'
uuid: 64d804fb-d434-51de-9eae-9ab990d4ca8d
year: 2025
---

<!-- AUTHORED REGION START -->
# A Volatility-Aware Temporal Transformer for Intraday Risk Forecasting with Market Microstructure Signals

## Summary

The paper asks how to forecast intraday realized volatility from limit order book data when classical GARCH-family models are too rigid and plain deep-learning sequence models lack any notion of volatility regime. It argues that a standard Transformer treats calm and turbulent periods identically, which either overfits to microstructure noise or fails to adapt its effective look-back window when the market shifts state.

The proposed model, the Volatility-Aware Temporal Transformer (VATT), augments a standard Transformer encoder with a Volatility Gating Module: a small convolutional sub-network that reads recent squared returns and produces a scalar gate $\gamma$ between 0 and 1, which rescales how much the self-attention output contributes relative to the residual path. A second addition, a volatility-biased attention mechanism, adds a learned bias term $B_{vol}$ (derived from local return standard deviation) to the attention scores before the softmax, shrinking the model's effective attention span when local volatility is high. Inputs are Level-2 order-book features, including order flow imbalance and a bid/ask depth-weighted spread, on top of price history, and the model is trained with a quasi-likelihood loss rather than mean squared error.

On five NASDAQ equities in 2022, VATT beat GARCH(1,1), an LSTM, a temporal convolutional network, and a vanilla Transformer on mean absolute error, root mean squared error, and quasi-likelihood loss for 10-minute-ahead realized volatility. An ablation attributes most of the gain to the gating module rather than the attention bias term, and the authors report the extra compute cost over a vanilla Transformer is small.

What is new relative to prior LOB-based deep learning volatility work is making the attention mechanism itself regime-aware, rather than adding volatility as just another input feature, and pairing that with a loss function chosen specifically to penalize underestimating risk.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Level-2 limit order book data is sampled at fixed 1-minute intervals; the prediction target is realized volatility over the following 10-minute window, computed as the sum of squared 10-second returns within that window. A learnable time-of-day embedding is added on top of standard positional encoding so the model can distinguish, for example, 09:30 from midday.

## Data

- **Asset class:** Equities
- **Instruments:** Five NASDAQ-traded large-cap stocks: AAPL, MSFT, AMZN, GOOGL, INTC
- **Venue:** LOBSTER dataset (NASDAQ)
- **Period:** January 2022 to December 2022, split into training (January-August), validation (September-October) and testing (November-December)
- **Granularity:** Level-2 limit order book (top-of-book depth), resampled to 1-minute intervals; the paper describes the source as tick-level data

## Features and Measures

- **Order Flow Imbalance (OFI).** A microstructure measure computed at a given book level that approximates the net flow of aggressive buy versus sell orders.
- **Depth-weighted spread.** A spread measure that weights the bid-ask gap by the volume available at each book level, used alongside price history as a model input.
- **Depth Balance.** The ratio of liquidity resting on the bid side versus the ask side of the book, used because a one-sided drying-up of liquidity tends to precede volatility.
- **Volatility Gating Module (VGM).** A convolutional sub-network attached to each Transformer encoder layer that reads recent squared returns and outputs a gate $\gamma \in [0,1]$ scaling the self-attention output, so the model falls back on the residual (near-random-walk) path when recent activity looks noisy.
- **Volatility-biased attention.** A modification of scaled dot-product attention that adds a learned bias term $B_{vol}$, derived from local return standard deviation, to the attention scores before the softmax, penalizing attention to distant time steps when local volatility is high.

## Method

VATT embeds robust-scaled (interquartile-range normalized) log-return and order-book features through a stack of 4 Transformer encoder layers, each with 8 attention heads and a hidden dimension of 128, using GELU activations and a dropout rate of 0.1. Each encoder layer contains the Volatility Gating Module and the volatility-biased attention term described above. Training uses the quasi-likelihood (QLIKE) loss instead of mean squared error, because QLIKE penalizes underpredicting variance more heavily than overpredicting it, which the authors argue better matches risk-management priorities.

VATT is compared against GARCH(1,1), a 2-layer LSTM with 128 hidden units, a Temporal Convolutional Network, and a vanilla Transformer without the gating or bias components, all trained on the same features and evaluated on the same held-out test period. Performance is judged with Mean Absolute Error, Root Mean Squared Error, and QLIKE loss on the 10-minute-ahead realized-volatility target. An ablation study separately removes the gating module and removes the bias term (while keeping the gate) to isolate each component's contribution, and training time and inference latency are compared across models.

## Results

- Averaged across the five stocks, VATT reached MAE 3.01 (x10^-4), RMSE 4.65 (x10^-4) and QLIKE 2.12, versus GARCH(1,1) at MAE 4.12, RMSE 6.33, QLIKE 2.85.
- VATT also beat the deep-learning baselines: LSTM (MAE 3.56, RMSE 5.42, QLIKE 2.51), TCN (MAE 3.48, RMSE 5.28, QLIKE 2.45) and the vanilla Transformer (MAE 3.45, RMSE 5.15, QLIKE 2.48).
- Removing the Volatility Gating Module raised RMSE from 4.65 to 5.10 on AAPL and from 4.72 to 5.18 on MSFT, close to vanilla-Transformer error levels.
- Removing the volatility-biased attention term alone (keeping the gating module) gave RMSE 4.88 on AAPL and 4.95 on MSFT, a smaller degradation than removing the gate.
- VATT trained in 9.1 hours versus 12.5 hours for the LSTM and 8.2 hours for the vanilla Transformer, with inference latency of 4.1 ms versus 4.2 ms (LSTM) and 3.8 ms (vanilla Transformer).
- Visualized attention weights spanned roughly the past 60 minutes during calm periods but collapsed to about the most recent 2-3 minutes immediately after a volatility spike such as a large order imbalance.

## Limitations

- The authors note the model depends on high-quality Level-2 order book data, which may be unavailable or degraded in fragmented cryptocurrency markets or dark pools.
- The authors note the computational cost, while acceptable for minute-level trading, may still be prohibitive for microsecond-level applications requiring FPGA-based logic.
- Reader note: tested on only five large-cap NASDAQ equities over a single calendar year (2022), so generalization to other asset classes, market regimes, or fixed income is untested.
- Reader note: the paper's own reference list cites works on unrelated topics (tax-risk AI, architectural design generation, 3D scene segmentation), which raises doubts about editorial rigor at this venue and warrants caution before relying on the reported numbers.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/transformers|transformers]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/queue-imbalance|Queue Imbalance]]

## Citation

Zhiming Hu (2025). A Volatility-Aware Temporal Transformer for Intraday Risk Forecasting with Market Microstructure Signals. Frontiers in Business and Finance.

DOI: 10.71465/fbf552

Text ingested: `markdown_output/hu-2025-volatility-aware-temporal-transformer-intraday-risk.md`, converted from `raw/ofi-event-clock/hu-2025-volatility-aware-temporal-transformer-intraday-risk.pdf`.

Coverage of this summary: Read the entire markdown file: abstract, introduction, related work, methodology including both code snippets, the experimental setup, all three results tables and surrounding discussion, conclusion, and reference list.
<!-- AUTHORED REGION END -->