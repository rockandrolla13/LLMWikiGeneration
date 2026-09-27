---
authors:
- Nikolaos Passalis
- Anastasios Tefas
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:389e47165c38201b98323a8cd431075f7b18ccfe5e01904ede729127bc1c8362
created: 2026-09-27 01:47:00+00:00
page_id: sources/passalis-2020-temporal-logistic-neural-bag-features-financial
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
- concepts/high-frequency-data
- concepts/feature-engineering
- entities/nikolaos-passalis
- entities/anastasios-tefas
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:bc7648620d73c651da769ff23a0f810e58bdd54808a345bc365244d823f1697a
source_path: markdown_output/passalis-2020-temporal-logistic-neural-bag-features-financial.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- bag-of-features
- mid-price-prediction
- time-series-forecasting
- neural-networks
- temporal-modeling
- clock-event
- asset-equity
- harvest-relevant
title: Temporal Logistic Neural Bag-of-Features for Financial Time series Forecasting
  leveraging Limit Order Book Data
updated: '2026-09-27T01:47:00Z'
uuid: 40870147-618c-5390-a882-892af6ff6281
year: 2020
---

<!-- AUTHORED REGION START -->
# Temporal Logistic Neural Bag-of-Features for Financial Time series Forecasting leveraging Limit Order Book Data

## Summary

The paper asks how to combine the Bag-of-Features (BoF) model, which turns a variable-length sequence into a fixed-length histogram over learned codewords, with deep feature extractors for financial time series forecasting, without the training instabilities that arise when BoF layers are stacked on deep networks. It identifies that the normalizations inside the standard BoF pipeline shrink gradients so severely that layers before the BoF layer barely update during early training.

The proposed Temporal Logistic Neural Bag-of-Features (TLo-NBoF) model replaces the classical Gaussian kernel used in BoF's soft-assignment step with a logistic (sigmoid) kernel, adds a trainable adaptive scaling mechanism for the intermediate vectors so gradients flow smoothly, and splits the extracted feature sequence into short-, mid-, and long-term temporal segments so the resulting histogram captures fine-grained temporal dynamics rather than only an overall summary.

On a large-scale high-frequency limit-order-book dataset, the method trains stably without careful initialization or hyper-parameter tuning, and an ablation study shows that deep feature extraction, temporal segmentation, learnable kernel parameters, and adaptive scaling each contribute measurably to predictive performance. The tuned model outperforms prior Bag-of-Features variants and standard CNN, LSTM, and GRU baselines at predicting the direction of the mid-price a fixed number of steps ahead.

What is new is the logistic reformulation of the BoF kernel together with the adaptive scaling mechanism, which the authors present as the first way to combine a temporal BoF layer with deep feature-extraction layers in an end-to-end trainable architecture for time series forecasting.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are indexed by limit-order-book update events rather than fixed time intervals: for each time step, a time series of the last 15 extracted feature vectors is compiled and split into three temporal regions of 5 feature vectors each (short-, mid-, and long-term). The prediction target is the direction (up, stationary, or down) of the average mid price after 10 further time steps, with a stock labeled stationary if the mid-price change is below 0.01%.

## Data

- **Asset class:** Equities
- **Instruments:** 5 Finnish companies traded on the Helsinki Exchange (Nasdaq Nordic), using the FI-2010 limit order book benchmark dataset
- **Venue:** Helsinki Exchange (Nasdaq Nordic)
- **Period:** 1 June 2010 to 14 June 2010 (10 business days)
- **Granularity:** event-by-event limit order book updates; 144-dimensional feature vectors extracted per event using the top 10 ask/bid price levels, yielding 453,975 feature vectors from 4.5 million limit orders

## Features and Measures

- **Temporal Logistic Neural Bag-of-Features (TLo-NBoF).** a Bag-of-Features layer that quantizes deep-extracted feature vectors against a learned codebook using a logistic (sigmoid) kernel instead of a Gaussian kernel, producing separate short-, mid-, and long-term histograms that are concatenated before classification.
- **Adaptive scaling.** trainable scale factors applied to the Bag-of-Features histogram and transformed feature vectors so the network can adjust their norm during training, restoring gradient flow that the model's normalizations would otherwise suppress.
- **Kernel Parameter Learning.** learning the logistic kernel's own parameters (alpha and beta) during training rather than fixing them, to further improve fit without manual tuning.

## Method

The architecture attaches a 1-D convolutional feature extractor (256 filters, kernel size 5) ahead of the TLo-NBoF layer, which holds 256 randomly initialized codewords learned jointly with the network via backpropagation. Each of the three temporal segments produces its own soft-assignment histogram; the concatenated histograms feed two fully connected layers (512 units, then 3 output classes) trained end-to-end with the cross-entropy loss and the Adam optimizer for 20 epochs, with training series sampled inversely to class frequency to offset class imbalance.

Evaluation uses an anchored walk-forward protocol: the model is trained on day 1 and tested on day 2, then trained on days 1-2 and tested on day 3, and so on, repeated 9 times, reporting the mean and standard deviation of macro-precision, macro-recall, macro-F1, and Cohen's kappa. An ablation study isolates the contribution of the deep convolutional extractor, temporal segmentation, kernel parameter learning, and adaptive scaling, and the full model is compared against prior MLP, BoF, N-BoF, T-BoF, and WMTR baselines from the literature, plus CNN, LSTM, and GRU architectures using the same convolutional feature extractor.

## Results

- Adding a deep convolutional feature extractor to the plain scaled logistic BoF model improved Cohen's kappa by about 20% in the ablation study.
- Adding three-level temporal segmentation (short/mid/long-term histograms) improved Cohen's kappa by over 40% relative to a model without it.
- Removing the trainable adaptive scaling factors reduced Cohen's kappa by over 14%, and without them the network's early-layer gradients were near zero for roughly the first 200 training iterations.
- The full ablated model (deep features + temporal modeling + kernel parameter learning + adaptive scaling) reached Cohen's kappa 0.3031 versus 0.1847 for the plain scaled Lo-NBoF baseline.
- On the FI-2010 benchmark, the proposed TLo-NBoF model reached macro-F1 52.98 and Cohen's kappa 0.2900, exceeding the next-best model (a GRU with 256 neurons, macro-F1 50.55, kappa 0.2560) by over 13% on kappa.
- The proposed method outperformed the earlier MLP, BoF, N-BoF, T-BoF and WMTR baselines from prior work as well as CNN, LSTM and GRU architectures built on the same feature extractor.

## Limitations

- Evaluated on a single benchmark (FI-2010): 5 Finnish stocks over 10 business days in June 2010.
- Reader note: performance is only assessed via the anchored 9-fold walk-forward split on this one dataset; generalization to other markets, asset classes, or periods is not tested.
- The stationary-price threshold (0.01% mid-price change) and the 10-step prediction horizon are fixed design choices whose sensitivity is not explored.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/feature-engineering|feature engineering]]
- [[entities/nikolaos-passalis|Nikolaos Passalis]]
- [[entities/anastasios-tefas|Anastasios Tefas]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Nikolaos Passalis, Anastasios Tefas, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2020). Temporal Logistic Neural Bag-of-Features for Financial Time series Forecasting leveraging Limit Order Book Data.

DOI: 10.1016/j.patrec.2020.06.006

Text ingested: `markdown_output/passalis-2020-temporal-logistic-neural-bag-features-financial.md`, converted from `raw/ofi-event-clock/passalis-2020-temporal-logistic-neural-bag-features-financial.pdf`.

Coverage of this summary: Read the whole markdown file, abstract through conclusion and references, including the ablation and FI-2010 comparison tables.

Known problems with the input: year from file metadata; Several equations and figures were rendered as picture-omitted placeholders in the markdown; exact formula details were not independently verified beyond the surrounding prose; Several results tables use OCR-mangled decimal formatting (digits split across bold/italic markers); numeric values reported here were reconstructed by matching the split-decimal pattern to row and column labels.
<!-- AUTHORED REGION END -->