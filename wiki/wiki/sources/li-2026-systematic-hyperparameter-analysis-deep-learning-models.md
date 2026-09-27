---
authors:
- Hongyi Li
content_hash: sha256:71027091e6a8cae52cc1b429ed2d8564e8084c8b31b67640f33ae2eaefcc7e41
created: 2026-09-27 01:47:00+00:00
page_id: sources/li-2026-systematic-hyperparameter-analysis-deep-learning-models
page_type: source
publication_venue: 'Proceedings of ICFTBA 2026 Symposium: Strategic Management & Business
  Analytics: Data-Driven Performance Models'
related:
- concepts/event-clock
- concepts/deep-learning-for-finance
- concepts/limit-order-book
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/transformers
- concepts/order-flow-prediction
revision_id: 1
schema_version: 2
source_hash: sha256:b13034103abfc9fa24668dde7365e02a39a798ab35dd5f9fd825c45742c925be
source_path: markdown_output/li-2026-systematic-hyperparameter-analysis-deep-learning-models.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- hyperparameter-tuning
- bilinear-networks
- fi-2010
- ablation-study
- mid-price-prediction
- clock-event
- asset-equity
- harvest-relevant
title: A Systematic Hyperparameter Analysis of Deep Learning Models for Limit Order
  Book Mid-price Prediction
updated: '2026-09-27T01:47:00Z'
uuid: 9f59076a-196d-5bdb-86f1-e76af8bd1eaa
year: 2026
---

<!-- AUTHORED REGION START -->
# A Systematic Hyperparameter Analysis of Deep Learning Models for Limit Order Book Mid-price Prediction

## Summary

The paper asks which of the many deep-learning architectures proposed for short-term limit-order-book (LOB) mid-price prediction actually performs best under one common experimental setup, and then which hyperparameters most affect that best model's performance, since prior work mostly tunes hyperparameters manually without systematic sensitivity checks.

Using the FI-2010 benchmark (five stocks on Nasdaq Nordic, split chronologically into training and test days, with a three-class down/stationary/up mid-price label), the paper first compares eleven representative architectures spanning feed-forward, recurrent (LSTM), convolutional (CNN, CNN+LSTM, DeepLOB, DeepLOB-Attention), bilinear (TABL, BiNTABL, plus the DAIN normalization baseline) and Transformer-based (TransLOB, LiT) families, evaluated by accuracy, precision, recall and macro-F1. Having identified the strongest architecture, the paper then holds everything else fixed and varies, one at a time, the number of bilinear layers, the learning rate, the internal dimensions of the bilinear projection matrices W1 and W2, the training batch size, the length of the historical input window, and the forecast horizon, to see how each choice moves the model's F1 score.

BiNTABL is the best of the eleven architectures on every metric reported. In the ablations on BiNTABL, removing its bilinear layer entirely causes by far the largest performance drop of anything tested, and learning rate and forecast horizon also produce large swings in F1, while batch size, the width of the bilinear projection matrices, and the number of stacked bilinear layers beyond the first have comparatively small effects. A shorter history window and a longer forecast horizon than the paper's own baseline setting both improved F1 in the configurations tested.

The contribution is not a new architecture but the first systematic, controlled-variable sweep of these hyperparameters for a bilinear LOB model, ranking the bilinear layer's presence, the learning rate, and the forecast horizon as the three settings that matter most, offered as practical guidance for configuring future LOB prediction models.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Following the FI-2010 benchmark's own design, each input example is a sliding window of order-book snapshots (100 snapshots in the baseline setting, tested down to 10 and up to 200), and the prediction target is the mid-price direction some number of order-book events ahead (the baseline forecasts 5 events ahead; the ablation also tests horizons of 3 and 10 events), rather than a fixed wall-clock interval.

## Data

- **Asset class:** Equities
- **Instruments:** five stocks traded on Nasdaq Nordic (Finland), via the FI-2010 benchmark dataset
- **Venue:** Nasdaq Nordic (Finland)
- **Period:** 10 consecutive trading days in June 2010, split chronologically into the first 7 days for training and the last 3 days for testing
- **Granularity:** Per-order-book-event snapshots; FI-2010 provides 40 raw bid/ask price-and-volume features across price levels 1 to 10 on both sides, plus 104 handcrafted microstructure features, for 149 features in total, with labels for 5 prediction horizons (1, 2, 3, 5 and 10 events ahead)

## Features and Measures

- **Bilinear projection layer (W1, W2).** A layer that maps an input matrix of time steps by features through two separate learnable weight matrices, one transforming along the feature dimension and one along the temporal dimension, to model interactions between the two before a nonlinearity is applied.
- **BiN (bilinear) normalization.** A normalization step applied before the bilinear layers that adjusts the input jointly across both the temporal and feature dimensions, intended to make training more robust to distributional shifts in the input than batch or instance normalization.

## Method

Two experiments are run on FI-2010. In the first, eleven architectures (MLP, LSTM, CNN, CNN+LSTM, DeepLOB, DeepLOB-Attention, DAIN, TABL, BiNTABL, TransLOB and LiT) are all given the same 100-tick, 40-feature input window and trained with the same cross-entropy loss, stochastic gradient descent optimizer and a learning rate of 0.01, to predict the 3-class mid-price movement 5 ticks ahead; each is scored on the held-out test days by F1, precision, accuracy and recall, and the best of the eleven is carried into the second experiment. In the second experiment, that architecture (BiNTABL) is fixed as a baseline configuration and, following a controlled-variable design, six hyperparameter groups are each varied one at a time while the rest of the configuration is held fixed: the number of bilinear layers, the learning rate, the internal dimensions of the W1 and W2 projection matrices, the batch size, the history window length, and the forecast horizon. Every configuration is trained for 30 epochs, and the resulting F1 (plus, for a couple of settings, training time) is compared back to the baseline.

## Results

- BiNTABL is the best of the eleven models on every metric reported, with an F1 of 86.61%, precision of 87.63%, accuracy of 87.07% and recall of 85.80%, well ahead of the next-best model, DeepLOB-Attention (F1 72.47%).
- Removing the bilinear layer from BiNTABL causes an immediate F1 drop of 38.4 percentage points, pushing the model close to random-guess performance on the 3-class task.
- Going from one to two bilinear layers improves F1 by 0.0029, and a third layer adds only a further 0.0006, so most of the benefit comes from having a bilinear layer at all rather than stacking more of them.
- Lowering the learning rate by one order of magnitude from the 0.01 baseline lowers F1 by about 10 percentage points, and lowering it by a further order of magnitude (to a training F1 of 0.3441) stops the model from converging.
- Changing the width of the W1 projection matrix changes F1 by only 0.0013 across the settings tested, while the best W2 configuration (100 to 30 to 5 to 1) improves F1 by 0.0036 over the baseline.
- A batch size of 32 improves F1 by 0.25 percentage points over the baseline batch size of 64, but takes 2336 seconds to train versus 1317 seconds for the baseline, an increase of roughly 77.3% in training time; a batch size of 128 instead lowers F1 by 0.23 percentage points.
- Shortening the history window from 100 to 10 snapshots improves F1 by 0.74 percentage points, while extending it to 200 snapshots lowers F1 by 0.54 percentage points, so the shorter 10-snapshot window performs best among those tested.
- Extending the forecast horizon from 5 to 10 events raises F1 by 4.7 percentage points, while shortening it from 5 to 3 events lowers F1 by 6.6 percentage points, making forecast horizon one of the most influential hyperparameters tested.

## Limitations

- All experiments use only the FI-2010 benchmark (five Nasdaq Nordic stocks, one ten-day period from 2010), so the hyperparameter rankings may not transfer to other markets or volatility regimes.
- Each hyperparameter is varied one at a time from a single fixed baseline configuration rather than jointly, so interactions between hyperparameters (for example learning rate with batch size) are not explored.
- The paper itself proposes extending the analysis to higher-volatility markets such as crypto and to newer architectures, implying the current guidance is specific to this benchmark and model family.
- Reader note: all ablation models are trained for a fixed 30 epochs, so settings that converge more slowly (such as a lower learning rate) may be penalized by the epoch budget rather than by their eventual performance.
- Reader note: the paper's own description of the BiNTABL baseline configuration in section 4.3 is internally garbled (it lists 'a learning rate of 0.0, 64 as batch size'), so the exact intended baseline learning rate is inferred from the 0.01 value used consistently elsewhere rather than read directly from that sentence.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/transformers|transformers]]
- [[concepts/order-flow-prediction|order flow prediction]]

## Citation

Hongyi Li (2026). A Systematic Hyperparameter Analysis of Deep Learning Models for Limit Order Book Mid-price Prediction. Proceedings of ICFTBA 2026 Symposium: Strategic Management & Business Analytics: Data-Driven Performance Models.

DOI: 10.54254/2754-1169/2026.ld36740

Text ingested: `markdown_output/li-2026-systematic-hyperparameter-analysis-deep-learning-models.md`, converted from `raw/ofi-event-clock/li-2026-systematic-hyperparameter-analysis-deep-learning-models.pdf`.

Coverage of this summary: Read the full converted markdown text: abstract, introduction, related work, the model-family overview (feed-forward, recurrent, convolutional, bilinear, Transformer), both experiments (the eleven-model comparison and the BiNTABL ablations, including all six ablation subsections), the conclusion, and the reference list.

Known problems with the input: Figures 1-8, which carry the main ablation results, are rendered only as picture captions in the converted markdown (with no chart data), so ablation findings here rely entirely on the paper's own prose description of each figure; The baseline description in section 4.3 contains a garbled fragment ('a learning rate of 0.0, 64 as batch size'); the intended learning rate (0.01) and batch size (64) are inferred from other unambiguous mentions in the text rather than from that sentence itself.
<!-- AUTHORED REGION END -->