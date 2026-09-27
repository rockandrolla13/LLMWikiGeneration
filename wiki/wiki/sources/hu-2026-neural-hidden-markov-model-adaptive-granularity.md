---
authors:
- Tianzuo Hu
content_hash: sha256:7acbb98c299ed332bdc11e8c21d53205c13c8650c98dd9576f3964ccc5988d58
created: 2026-09-27 01:47:00+00:00
page_id: sources/hu-2026-neural-hidden-markov-model-adaptive-granularity
page_type: source
related:
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:977505e4d871643f61167248ab3d7ef3522bce81b55112a00bf12e6f41367cb3
source_path: markdown_output/hu-2026-neural-hidden-markov-model-adaptive-granularity.md
source_type: paper
tags:
- neural-hmm
- order-flow
- adaptive-attention
- multi-resolution
- normalizing-flow
- market-regime
- high-frequency-trading
- limit-order-book
- clock-calendar
- asset-multi
- harvest-relevant
title: Neural Hidden Markov Model with Adaptive Granularity Attention for High-Frequency
  Order Flow Modeling
updated: '2026-09-27T01:47:00Z'
uuid: a40d0fd6-09a1-5003-be9b-d648a6ddccd7
year: 2026
---

<!-- AUTHORED REGION START -->
# Neural Hidden Markov Model with Adaptive Granularity Attention for High-Frequency Order Flow Modeling

## Summary

The paper targets high-frequency order flow modeling, arguing that traditional Hidden Markov Models and their fixed-resolution neural extensions cannot adapt to the fact that tick-level detail matters more in volatile periods while minute-level trends matter more in calm periods. It proposes an Adaptive Granularity Attention (AGA) mechanism that computes local volatility and transaction-frequency signals from the input, uses them to gate between a fine-grained encoder (dilated causal convolutions) and a coarse-grained encoder (a learnable wavelet transform feeding an LSTM), and refines the fused representation with multi-head attention over a lookback window.

The AGA output conditions a Neural HMM whose emission model is a per-state conditional normalizing flow (replacing Gaussian emissions) and whose transition model is a bilinear, volatility-temperature-scaled function of the previous state and the AGA features, so that regime switches become more frequent and less deterministic when volatility is high.

The model is evaluated on order book data described as coming from NASDAQ, the London Stock Exchange and Binance, reconstructed at 100-millisecond snapshots, predicting the mid-price movement 500 milliseconds ahead. It is compared against five baselines (HMM-GARCH, LSTM-ATTN, TCN-MultiRes, a vanilla Neural HMM, and a fixed-wavelet HMM) on accuracy, Matthews Correlation Coefficient, regime-detection F1, Sharpe ratio of a simulated trading strategy, and inference latency, and is reported to beat all baselines on every metric and on a cross-asset generalization test.

What the paper presents as new is the combination of (1) an attention-based, measurably-conditioned gate between two fixed-resolution encoders, (2) a Neural HMM with flow-based emissions, and (3) a volatility-adaptive transition temperature, unified in one end-to-end trained architecture for order flow prediction.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Order book snapshots are reconstructed at fixed 100-millisecond wall-clock intervals from raw timestamped order messages, after which features are normalized using rolling 30-minute z-scores. The prediction target is the mid-price movement 500 milliseconds ahead, discretized into up (≥ 0.5 rolling standard deviations), down (≤ −0.5 standard deviations), and neutral classes.

## Data

- **Asset class:** Several asset classes
- **Instruments:** Equities on NASDAQ, ETFs on the London Stock Exchange, and cryptocurrency data from Binance
- **Venue:** NASDAQ, London Stock Exchange, Binance
- **Period:** not stated
- **Granularity:** Order book reconstructed at 100-millisecond snapshots; forward prediction horizon of 500 milliseconds; features normalized over rolling 30-minute windows

## Features and Measures

- **Adaptive Granularity Attention (AGA).** A gating mechanism that computes local volatility and transaction-frequency signals from recent order flow, uses them to interpolate between fine- and coarse-resolution encoder outputs, and refines the fused features with multi-head attention over a lookback window.
- **Dilated causal convolution encoder.** A fine-resolution pathway using causal convolutions with exponentially increasing dilation rates to capture tick-level order flow patterns without excessive parameter growth.
- **Learnable wavelet + LSTM encoder.** A coarse-resolution pathway that decomposes the input using a learnable discrete wavelet transform (implemented as a constrained 1D convolution) and processes the resulting approximation coefficients with an LSTM to capture minute-level liquidity trends.
- **Conditional normalizing flow emission model.** An HMM emission model that replaces a Gaussian density with a per-state sequence of invertible, differentiable transformations conditioned on the AGA features, allowing flexible non-Gaussian observation distributions.
- **Volatility-adaptive transition model.** An HMM state-transition model whose logits combine a bilinear interaction between the previous state and current AGA features with a volatility-scaled temperature parameter that flattens the transition distribution during high-volatility periods.

## Method

The architecture first runs raw order-flow features through the dilated-convolution and wavelet-LSTM encoders in parallel, then fuses them with the AGA gate and multi-head attention. The fused features condition both the emission model (a per-state conditional normalizing flow with coupling layers) and the transition model (a bilinear, temperature-scaled function of the previous state) of a Neural HMM, which is trained end-to-end by maximizing the log-likelihood of observed sequences via the forward algorithm, combined with a classification cross-entropy loss on the mid-price movement label and L2 weight regularization.

The model is trained on 4-week rolling windows with a 1-week validation set for early stopping, using Adam with an initial learning rate of 3×10⁻⁴ and cosine decay, for up to 200 epochs with batch size 256 on NVIDIA V100 GPUs. It is compared against HMM-GARCH, LSTM-ATTN, TCN-MultiRes, a vanilla Neural HMM, and a fixed-wavelet HMM, all given the same input features and prediction target. Evaluation uses classification accuracy, Matthews Correlation Coefficient, a regime-detection F1 score, the Sharpe ratio of a simulated long/short trading strategy, and 99th-percentile inference latency, with statistical significance assessed via Diebold-Mariano tests on rolling 1-hour prediction differences.

## Results

- On NASDAQ data, AGA-Neural HMM reached 68.3% accuracy on the 500ms mid-price movement task, 4.7 percentage points above the best fixed-resolution baseline, TCN-MultiRes (63.6%).
- AGA-Neural HMM's Matthews Correlation Coefficient was 0.581, versus 0.527 for TCN-MultiRes (p < 0.01, Diebold-Mariano test).
- Regime-shift detection F1 was 71.3% for AGA-Neural HMM versus 64.3% for the best baseline (LSTM-ATTN).
- Ablation on the NASDAQ dataset: removing the AGA mechanism cut accuracy by 7.2 points (to 61.1%); removing the dilated-convolution pathway cut it by 4.1 points; removing the wavelet-LSTM branch cut it by 2.8 points; using Gaussian emissions cut it by 2.3 points; fixing the transition model cut it by 1.2 points.
- Cross-asset accuracy was 68.3% (NASDAQ equities), 66.8% (LSE ETFs) and 65.7% (Binance crypto), each above the corresponding best baseline (63.6%, 62.1%, 59.8% respectively).
- A simulated trading strategy using the model's predictions achieved Sharpe ratios of 2.78 (equities) and 2.41 (crypto), with a state-dependent Sharpe of 3.12 in high-volatility regimes versus 1.89 for baseline strategies.
- During high-volatility periods the average gating weight toward fine-grained features was 0.72, versus 0.38 in stable periods, with a Spearman correlation of 0.83 (p < 0.001) between local volatility and the fine-grained feature contribution.

## Limitations

- Authors state the model assumes discrete hidden states and may not capture a continuum of market regimes.
- Authors state the gating mechanism relies only on local volatility and transaction frequency, potentially overlooking other microstructure indicators such as order book imbalance.
- Authors state the normalizing-flow emission model's computational cost may become prohibitive for sub-millisecond prediction intervals.
- Authors state each asset is modeled independently, missing potential cross-asset dependencies.
- Reader note: the document is dated 'Feb 30, 2026', a date that does not exist on any calendar, no author affiliation or venue is given, and several bibliography entries have irregular author-name ordering; these anomalies raise doubts about whether this is a genuine, verifiable research paper, so its reported numbers should be treated with added caution pending confirmation of the source.

## Related

- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]

## Citation

Tianzuo Hu (2026). Neural Hidden Markov Model with Adaptive Granularity Attention for High-Frequency Order Flow Modeling.

DOI: 10.48550/arxiv.2603.20456

Text ingested: `markdown_output/hu-2026-neural-hidden-markov-model-adaptive-granularity.md`, converted from `raw/ofi-event-clock/hu-2026-neural-hidden-markov-model-adaptive-granularity.pdf`.

Coverage of this summary: Read the full document end-to-end, including abstract, all numbered sections (introduction through conclusion) and the reference list.

Known problems with the input: The document's date line reads 'Feb 30, 2026', a calendar date that does not exist; combined with no stated author affiliation or venue and irregular bibliography author-name ordering, this raises real doubt about whether this is a genuine, peer-reviewed or independently verifiable research paper. All extracted content should be treated as unverified pending confirmation of the source; No institution/affiliation is given for the sole author; No venue (journal, conference, or preprint server) is stated anywhere in the text; No explicit date range (start/end dates) is given for the NASDAQ/LSE/Binance datasets used in the experiments; only the data-source citations carry years, not the sample period, so data.period is marked not stated.
<!-- AUTHORED REGION END -->