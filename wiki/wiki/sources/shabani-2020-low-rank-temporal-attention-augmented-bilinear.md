---
authors:
- Mostafa Shabani
- Alexandros
content_hash: sha256:979ba0a1c3bfce9ec74df49199a568e460ce400611408028615be82a305c157e
created: 2026-09-27 01:47:00+00:00
page_id: sources/shabani-2020-low-rank-temporal-attention-augmented-bilinear
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/mid-price-prediction
- entities/mostafa-shabani
revision_id: 1
schema_version: 2
source_hash: sha256:351586ce178c513b24499b138cc9700f7dfac2508a97386ee5d7ec763cbb93f6
source_path: markdown_output/shabani-2020-low-rank-temporal-attention-augmented-bilinear.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- low-rank-approximation
- tabl
- fi-2010
- mid-price-prediction
- clock-event
- asset-equity
- harvest-relevant
title: Low-Rank Temporal Attention-Augmented Bilinear Network for financial time-series
  forecasting
updated: '2026-09-27T01:47:00Z'
uuid: 32037237-56c1-5c48-bfb6-3ca51a083b6e
year: 2020
---

<!-- AUTHORED REGION START -->
# Low-Rank Temporal Attention-Augmented Bilinear Network for financial time-series forecasting

## Summary

Building on the previously proposed TABL (Temporal Attention-Augmented Bilinear) network for limit order book time-series forecasting, the paper asks whether a low-rank tensor approximation of the TABL layer's weight matrices can reduce the number of trainable parameters and inference cost, as needed for ultra-high-frequency use, without losing prediction accuracy.

The proposed LR-TABL layer factorizes each of the TABL layer's weight matrices (the input data-transformation matrix, the temporal-aggregation matrix, and the attention matrix) as a product of two smaller matrices of a chosen rank K, trained end-to-end rather than approximated after the fact, while keeping the same input-transform, attention, and aggregation structure and bias term as the original TABL layer. It is evaluated on the publicly available FI-2010 limit order book benchmark (10 depth levels for 5 Finnish NASDAQ Nordic stocks over 10 days, with the standard 7-day train / 3-day test split and z-score normalized inputs), predicting the direction of the mid-price (up, stationary, down) at a prediction horizon of 10, using three network depths that mirror the original TABL paper's architectures and a weighted cross-entropy loss to handle class imbalance.

Across all three network structures, increasing the low-rank dimension K raises LR-TABL's accuracy and F1-score toward the full-rank TABL network's performance while still using substantially fewer parameters. For example the deepest structure reaches an F1 of 0.720 at K = 14 with 5824 parameters, versus the full-rank network's F1 of 0.776 with 11344 parameters, and the shallowest structure reaches F1 = 0.563 at K = 3 with 204 parameters versus the full-rank network's F1 of 0.5603 with 234 parameters.

What is new is restricting the TABL layer's three weight matrices to be jointly low-rank and training that low-rank factorization end-to-end, rather than approximating a pretrained full-rank layer afterward, reducing both the parameter count and the time complexity of the attention-augmented bilinear layer while targeting the same limit-order-book forecasting task.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The model consumes the 10 most recent limit order book update instances (10 price/volume levels per side, giving a 40-dimensional feature per instance) as its input tensor, and predicts the categorical direction of the mid-price at a prediction horizon of 10 instances ahead, following the FI-2010 benchmark's event-indexed sampling rather than a fixed calendar-time interval.

## Data

- **Asset class:** Equities
- **Instruments:** 5 stocks traded on NASDAQ Nordic, via the FI-2010 limit order book benchmark dataset
- **Venue:** NASDAQ Nordic
- **Period:** 10 consecutive trading days, following the FI-2010 benchmark protocol of the first 7 days for training and the remaining 3 days for evaluation
- **Granularity:** Ultra high-frequency limit order book updates with 10 price/volume levels per side (a 40-dimensional feature per instance), using the 10 most recent instances as the input window

## Features and Measures

- **Low-rank bilinear/attention layer (LR-TABL).** A neural network layer that factorizes the input-transform, temporal-aggregation, and attention weight matrices of the TABL layer into products of two low-rank matrices of dimension K, cutting parameter count and inference cost while the low-rank factors are learned end-to-end.

## Method

The paper takes the previously proposed TABL layer, which applies a bilinear input transform, a learned softmax attention mask over the time axis, a soft blend of attended and un-attended representations via a learnable scalar gate, and a final nonlinear temporal aggregation, and replaces each of its large weight matrices with a product of two matrices of rank K, so parameter count and multiply-add cost scale with K instead of with the full input and time dimensions. Three network depths (LR-TABL A, B, and C, of one, two, and three layers respectively) mirroring the original TABL paper's architectures are trained end-to-end with a weighted categorical cross-entropy loss, to handle the imbalanced up/stationary/down classes, on the FI-2010 benchmark, using the same experimental protocol (train/test split, 40x10 input tensor, prediction horizon of 10) as the original TABL evaluation. Performance is judged by accuracy, precision, recall, and macro F1-score on the held-out test days, compared against the original full-rank TABL network at matched architecture depth, and efficiency is judged by the number of trainable parameters as a function of the low-rank dimension K.

## Results

- For the deepest architecture (structure C), LR-TABL's F1-score rises from 0.458 at K = 1 (1658 parameters) to 0.720 at K = 14 (5824 parameters), compared with the full-rank TABL C's F1 of 0.776 using 11344 parameters.
- For the shallowest architecture (structure A), LR-TABL reaches F1 = 0.563 at K = 3 using 204 parameters, versus TABL A's F1 of 0.5603 using 234 parameters.
- For the medium architecture (structure B), LR-TABL's best reported F1 is 0.685 at K = 19 (4144 parameters), close to TABL B's F1 of 0.692 at 5844 parameters.
- Across all three structures, LR-TABL's F1-score approaches that of the corresponding full-rank TABL network while using markedly fewer trainable parameters.
- All experiments use the FI-2010 benchmark of 5 NASDAQ Nordic stocks over 10 trading days, with a mid-price prediction horizon of 10.

## Limitations

- Evaluation is restricted to a single public benchmark dataset (FI-2010, 5 stocks, 10 days), so generalization to other markets or longer samples is not shown.
- The paper compares only against the original TABL network, not against the other efficient limit-order-book forecasting architectures it cites in its own related-work discussion.
- Reader note: F1-scores for LR-TABL do not increase monotonically with K in the reported tables (for example structure C's F1 dips at several intermediate K values), which the paper does not discuss.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/mid-price-prediction|Mid-Price Prediction]]
- [[entities/mostafa-shabani|Mostafa Shabani]]

## Citation

Mostafa Shabani, Alexandros (2020). Low-Rank Temporal Attention-Augmented Bilinear Network for financial time-series forecasting.

DOI: 10.1109/ssci47803.2020.9308440

Text ingested: `markdown_output/shabani-2020-low-rank-temporal-attention-augmented-bilinear.md`, converted from `raw/ofi-event-clock/shabani-2020-low-rank-temporal-attention-augmented-bilinear.pdf`.

Coverage of this summary: Read the whole paper: abstract, introduction, related work, the TABL layer description, the proposed low-rank LR-TABL layer with its parameter and time-complexity tables, the FI-2010 experimental setup, the per-architecture performance tables (structures A, B, C), and the conclusion.

Known problems with the input: The performance tables (Tables III, IV, V) are rendered with heavy conversion noise (repeated strikethrough artifacts) in this markdown; numeric values were reconstructed from row order and cross-checked against the bolded best-performing rows, but exact cell alignment could not be fully verified for every row; The second author's name is cut off in the converted text: only the given name 'Alexandros' appears, with no surname printed, so the author list here reproduces exactly what is legible rather than inferring a surname from the reference list.
<!-- AUTHORED REGION END -->