---
authors:
- Damian Kisiel
- Denise Gorse
content_hash: sha256:0e69a953d7245c5700798ff8b05e3851166fa14ced0ceb598eae70a18057c6ad
created: 2026-09-27 01:47:00+00:00
page_id: sources/kisiel-2022-axial-lob-high-frequency-trading-axial
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/transformers
- concepts/lstm-networks
- concepts/order-flow-prediction
- concepts/mid-price-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:8d1a5aff12afd515ad14222169a9e4b1f13f2e28659a8ce413e0fca489881bb6
source_path: markdown_output/kisiel-2022-axial-lob-high-frequency-trading-axial.md
source_type: paper
tags:
- limit-order-book
- attention-mechanism
- deep-learning
- high-frequency-trading
- mid-price-prediction
- fi-2010
- clock-event
- asset-equity
- harvest-relevant
title: 'Axial-LOB: High-Frequency Trading with Axial Attention'
updated: '2026-09-27T01:47:00Z'
uuid: 1188e296-d9f9-589e-9e50-0d7a17c3b31c
year: 2022
---

<!-- AUTHORED REGION START -->
# Axial-LOB: High-Frequency Trading with Axial Attention

## Summary

The paper asks whether an attention-only architecture, without any hand-crafted convolutional kernels, can predict the direction of future limit-order-book mid-price moves at least as well as existing CNN- and LSTM-based models, while using fewer parameters and staying robust to how the input features are ordered.

The authors introduce Axial-LOB, built around gated axial attention: the standard 2D attention operation over an order-book image (time by features) is factorized into two much cheaper 1D self-attention passes, one along the feature axis and one along the time axis, with learned gated positional encodings added to each. The model takes as input only raw historical price and volume at the top ten levels on both book sides over the last 40 snapshots, with no hand-crafted technical indicators. It is trained and evaluated on the FI-2010 benchmark dataset, ten days of Nasdaq Nordic limit-order-book data for five stocks, using a three-way up/down/stationary classification of the smoothed future mid-price relative to a fixed threshold, at five prediction horizons.

Axial-LOB achieves the best precision, recall, and F1 score of all tested models at every one of the five prediction horizons, improving over the previous best model, an attention-augmented DeepLOB variant, while having a similar parameter count to the smallest benchmark models and far fewer parameters than the DeepLOB family. Under random permutations of the input feature order, Axial-LOB's F1 score degrades much less than the best CNN-based benchmark's, showing it does not depend on a fixed spatial arrangement of features.

The novelty is applying axial attention, previously used in vision and image-segmentation work, to limit-order-book prediction for the first time, combined with gated positional encodings, giving a fully-attentional model that avoids hand-crafted convolutional structure, reduces the parameter count relative to prior CNN/LSTM/attention hybrids, and is demonstrably robust to the ordering of input features.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed in tick (order-book event) time rather than wall-clock time, so the interval between consecutive snapshots can range from a fraction of a second to several seconds. The model uses the 40 most recent order-book snapshots as input and predicts, at horizon k, the direction of a smoothed future mid-price (the mean of the next k mid-prices) relative to the current mid-price, using k in {10, 20, 30, 50, 100}.

## Data

- **Asset class:** Equities
- **Instruments:** Five stocks from the FI-2010 benchmark dataset, traded on the Nasdaq Nordic stock market
- **Venue:** Nasdaq Nordic
- **Period:** Ten consecutive trading days (FI-2010 dataset), with the first seven days used for training and the last three for testing
- **Granularity:** Millisecond-level intraday limit-order-book updates restricted to normal trading hours (10:30-18:00), first ten price levels and volumes on both bid and ask sides

## Features and Measures

- **axial attention.** An attention mechanism that factorizes standard 2D self-attention into two sequential 1D attention passes, along width then height, recovering a global receptive field at much lower computational cost than full 2D attention.
- **gated positional embeddings.** Learned positional bias terms added to the attention computation, passed through learnable gates that control how much position-dependent information is allowed to influence the attention output, intended to help with noisy financial input.
- **smoothed mid-price direction label.** The target label: the percentage change between the current mid-price and the mean of the next k mid-prices, classified as up, down, or stationary using a fixed threshold.

## Method

Axial-LOB stacks gated axial attention blocks, each applying two multi-head axial attention operations, first along the feature/width axis then the time/height axis, with gated relative positional encodings, interleaved with 1x1 convolutions, batch normalization and ReLU used only for channel-wise pooling rather than spatial feature extraction. The final feature map is adaptively pooled and passed through a fully connected softmax layer to output probabilities over three mid-price-direction classes. The network is trained with mini-batch stochastic gradient descent on cross-entropy loss, momentum, batch size 64, up to 100 epochs, a cosine-annealing learning-rate schedule, and early stopping after 10 epochs without validation improvement; hyperparameters such as attention heads and channel sizes are tuned via 100 iterations of random grid search on a held-out validation split taken from the last 20% of the training days. Performance is compared against six benchmark architectures, a CNN model, two attention-augmented bilinear networks, DeepLOB, DeepLOB-Seq2Seq, and DeepLOB-Attention, using precision, recall and F1 score averaged over five independent training runs, and separately tested for robustness to random permutation of the input feature order.

## Results

- Axial-LOB achieved the highest precision, recall, and F1 score of all compared models at every tested prediction horizon (k = 10, 20, 30, 50, 100), beating its closest competitor with statistical significance under 5%.
- At k = 10, Axial-LOB reached an F1 score of 85.14%, versus 82.37% for the previous best model, DeepLOB-Attention.
- At k = 100, Axial-LOB reached an F1 score of 85.93%, versus 81.49% for DeepLOB-Attention.
- Axial-LOB uses 9,615 parameters, a similar order of magnitude to the smallest benchmarks, B(TABL) with 5,844 and C(TABL) with 11,344, and far fewer than DeepLOB-family models, which range from 142,435 to 177,699 parameters.
- Under random permutation of the input feature order, Axial-LOB's F1 score dropped by only 0.37 to 1.05 percentage points across horizons, versus a 2.48 to 4.81 point drop for DeepLOB-Attention.
- Model performance generally improved as the prediction horizon k increased, except that the shortest horizon (k = 10) performed better than expected, which the authors attribute to near-term price moves being easier to predict.

## Limitations

- The model is only tested on the FI-2010 benchmark, five Nasdaq Nordic stocks over ten trading days; the authors state they plan to test robustness and generalization on a larger dataset in future work.
- No technical indicators or additional order-book features beyond raw price/volume at the top ten levels are used, so the approach is not tested with a richer feature set.
- The model predicts mid-price direction only and does not address execution, transaction costs, market impact, or order sizing, which the authors note are separate considerations for a trading strategy.
- Reader note: the paper reports averages over only five independent training runs, a small number for assessing variability from the stochastic optimizer.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/transformers|transformers]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]

## Citation

Damian Kisiel, Denise Gorse (2022). Axial-LOB: High-Frequency Trading with Axial Attention.

DOI: 10.1109/ssci51031.2022.10022284

Text ingested: `markdown_output/kisiel-2022-axial-lob-high-frequency-trading-axial.md`, converted from `raw/ofi-event-clock/kisiel-2022-axial-lob-high-frequency-trading-axial.pdf`.

Coverage of this summary: Read the full paper start to finish, including the model architecture description (self-attention, axial attention, gated positional embeddings), the FI-2010 dataset and target-labeling description, training and calibration details, the benchmark comparison, both results subsections (performance and permutation robustness), and the conclusion.

Known problems with the input: No explicit publication year is printed in the visible text; year_hint (2022) from the job file was used, per instructions; Two figure captions (Figs. 1 and 2) are garbled OCR renderings of the architecture and order-book diagrams in the markdown; only the surrounding prose was used.
<!-- AUTHORED REGION END -->