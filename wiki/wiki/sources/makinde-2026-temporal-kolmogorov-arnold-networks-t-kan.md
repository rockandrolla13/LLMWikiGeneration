---
authors:
- Ahmad Makinde
content_hash: sha256:b0ba8e9c68a1652efd0ca0a528f6473f4533c80aa87cb9dda8d26843fd19ce3c
created: 2026-09-27 01:47:00+00:00
page_id: sources/makinde-2026-temporal-kolmogorov-arnold-networks-t-kan
page_type: source
publication_venue: Bristol Institute for Learning and Teaching (BILT) Student Research
  Journal, Issue 7, Article 0502
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:e198ff21d3215224b20afba0752c4b7de620496c48bb0aced092a73c1459b82f
source_path: markdown_output/makinde-2026-temporal-kolmogorov-arnold-networks-t-kan.md
source_type: paper
tags:
- limit-order-book
- kolmogorov-arnold-networks
- alpha-decay
- deep-learning
- high-frequency-trading
- interpretability
- lstm
- fpga
- clock-event
- asset-equity
- harvest-relevant
title: 'Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order
  Book Forecasting: Efficiency, Interpretability, and Alpha-Decay'
updated: '2026-09-27T01:47:00Z'
uuid: e24370ac-3311-53db-baab-cf4f340f46f1
year: 2026
---

<!-- AUTHORED REGION START -->
# Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha-Decay

## Summary

The paper asks whether replacing the fixed linear weights inside an LSTM's gates with learnable univariate B-spline functions, inspired by Kolmogorov-Arnold Networks (KAN), can reduce the 'alpha decay' problem in high-frequency limit order book forecasting, where models like DeepLOB lose predictive power as the prediction horizon grows. It proposes a hybrid architecture the author calls T-KAN, in which KAN-style spline layers redefine the LSTM's gating logic, and compares it against a DeepLOB (CNN-LSTM) baseline on the FI-2010 limit order book benchmark.

Both models take a sliding window of ten past normalized order-book states as input and are trained to classify the direction of the mid-price over look-ahead horizons of 10, 50 or 100 ticks, using a strict chronological (non-overlapping) train/test split and macro-averaged F1 to avoid the leakage and class-imbalance issues the author says inflate other studies' reported accuracy. Class imbalance in the FI-2010 labels is handled with inverse-frequency loss weighting, and the spline coefficients are additionally regularized with an L1 sparsity penalty.

At the longest horizon (k=100 ticks), T-KAN reached a macro F1-score of 0.3995 against 0.3354 for the DeepLOB baseline, a 19.1% relative improvement, and also had higher precision (0.5343). In a mid-price backtest with a 1.0 bps transaction cost, DeepLOB's directional edge could not cover trading costs and ended with a -82.76% terminal return, while T-KAN produced a 132.48% terminal return despite using more parameters (104,451 versus 58,211).

The novelty claimed is twofold: the learned spline activations converge to an interpretable S-shaped 'dead-zone' function that visibly filters near-zero microstructure noise before amplifying strong signals, and because KAN layers rely on localized spline evaluations rather than dense matrix multiplication, the author argues the architecture is a natural fit for low-latency FPGA implementation via high-level synthesis, though this hardware step is left as future work.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Both models consume a rolling window of T=10 past 144-dimensional, z-score-normalized limit order book states (the FI-2010 feature set) and predict the direction of the mid-price (up, down, or stationary) over a look-ahead horizon k of 10, 50 or 100 ticks, with a smoothing rule applied to the mid-price label to filter instantaneous microstructure noise.

## Data

- **Asset class:** Equities
- **Instruments:** not stated (FI-2010 benchmark limit order book dataset)
- **Venue:** not stated
- **Period:** not stated
- **Granularity:** 144-dimensional per-observation LOB feature vectors; T=10 lookback window; prediction horizons k=10, 50, 100 ticks ahead

## Features and Measures

- **T-KAN cell.** A recurrent cell that replaces the LSTM's fixed weight matrices in the input, forget and output gates with learnable univariate B-spline functions (mixed with a SiLU base function), so the gating nonlinearity itself is learned rather than fixed.
- **DeepLOB baseline (CNN-LSTM).** A convolutional-recurrent baseline that uses 1x2 kernels to summarise bid-ask spreads and 4x1 kernels to extract depth across price levels, feeding the resulting feature maps into a 64-unit LSTM before classification.
- **Sliding Window Unit.** The supervised-learning framing that turns a stream of normalized order-book snapshots into fixed-length input samples of T=10 past states, giving the model access to short-term order-flow history rather than a single static snapshot.
- **Inverse frequency class weighting.** A loss weighting scheme that assigns each of the three price-direction classes a weight inversely proportional to its frequency in the FI-2010 labels, to stop the model defaulting to the dominant 'stationary' class.
- **B-spline sparsity penalty.** An L1 penalty applied to the learnable B-spline coefficient vectors in the KAN layers, added to the cross-entropy loss to encourage smoother, less overfit activation shapes.

## Method

The study benchmarks two architectures on the FI-2010 limit order book dataset: a DeepLOB-style CNN-LSTM baseline, re-implemented by the authors, and the proposed T-KAN, which pairs a two-layer, 64-hidden-unit LSTM encoder with a Kolmogorov-Arnold-Network-based classification head that projects the final 256-dimensional hidden state through learnable spline activations rather than a standard MLP. Both models are trained to predict the direction of the mid-price label over horizons of k = 10, 50 and 100 ticks.

Class imbalance in the three-way direction label (with class counts 36533, 138391 and 37135) is corrected with inverse-frequency loss weights (1.93, 0.51 and 1.90) inside a weighted cross-entropy objective, and the spline coefficients are further regularized with an L1 sparsity penalty. To avoid the intraday data leakage the authors say affects random or overlapping-sequence validation splits, evaluation uses a strict chronological train/test split and macro-averaged F1, which the authors argue produces lower but more trustworthy absolute scores than prior work.

Beyond classification metrics, the authors run a simple mid-price trading simulation under a 1.0 bps transaction cost to translate predictive accuracy into an economic outcome, and they visually inspect the learned B-spline activation functions of the T-KAN model as a form of interpretability analysis.

## Results

- T-KAN reached a macro F1-score of 0.3995 at the k=100 horizon versus 0.3354 for the DeepLOB baseline, a 19.1% relative improvement.
- T-KAN's precision at k=100 was 0.5343, described as better at flagging trend reversals and reducing false-positive trade signals.
- Under a 1.0 bps transaction cost, DeepLOB's mid-price strategy ended with a -82.76% terminal return, while T-KAN ended with a 132.48% terminal return.
- T-KAN used more parameters than DeepLOB (104,451 versus 58,211, a 79.4% increase), which the authors argue is justified by its much higher backtested profitability.
- The T-KAN model's learned activation converged to an S-shaped B-spline with a 'dead-zone' near zero, which the authors interpret as automatic filtering of bid-ask-bounce noise.
- The authors attribute their lower absolute F1-scores relative to Zhang et al.'s original DeepLOB results to using a strict chronological split (no random/overlapping validation) and macro- rather than micro-averaged F1.

## Limitations

- Evaluated on a single benchmark dataset (FI-2010) rather than live or multi-asset order book data.
- The paper reports inconsistent total parameter counts for the models (532,675 mentioned in the introduction versus 104,451/58,211 given later for T-KAN/DeepLOB), an inconsistency in the source text itself.
- Interpretability and FPGA/HLS suitability are argued qualitatively; no actual hardware implementation or latency measurement is reported.
- Reader note: results rest on one train/test split and one transaction-cost assumption (1.0 bps); no confidence intervals or repeated-run variability are reported.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Ahmad Makinde (2026). Temporal Kolmogorov-Arnold Networks (T-KAN) for High-Frequency Limit Order Book Forecasting: Efficiency, Interpretability, and Alpha-Decay. Bristol Institute for Learning and Teaching (BILT) Student Research Journal, Issue 7, Article 0502.

DOI: 10.71706/f0ee1480-22dc-4fc7-a6d4-4807f32ece2d

Text ingested: `markdown_output/makinde-2026-temporal-kolmogorov-arnold-networks-t-kan.md`, converted from `raw/ofi-event-clock/makinde-2026-temporal-kolmogorov-arnold-networks-t-kan.pdf`.

Coverage of this summary: Read the entire converted markdown, including the coversheet, abstract, literature review, methodology, results, conclusion, and reference list.

Known problems with the input: The paper does not explicitly state the asset class or instruments underlying the FI-2010 benchmark dataset; asset_class is recorded as 'equity' based on contextual cues (auction-phase, continuous-trading language) rather than an explicit statement in this paper's text; The paper gives two different total parameter counts for its models: 532,675 in the introduction versus 104,451 (T-KAN) and 58,211 (DeepLOB) in the results/conclusion; this inconsistency is in the source text, not introduced here; Several figures/diagrams were omitted by the PDF-to-markdown conversion (marked as picture placeholders in the source) and could not be described.
<!-- AUTHORED REGION END -->