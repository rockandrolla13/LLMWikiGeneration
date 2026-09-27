---
authors:
- Zihao Zhang
- Stefan Zohren
content_hash: sha256:b666e2a7a7bfb7788891cb5922f150b34f99cd7cf0636347fcd4e85b4c0b1020
created: 2026-09-27 01:47:00+00:00
page_id: sources/zhang-2021-multi-horizon-forecasting-limit-order-books
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/order-flow-prediction
- concepts/high-frequency-data
- concepts/order-imbalance
- concepts/feature-engineering
- entities/stefan-zohren
revision_id: 1
schema_version: 2
source_hash: sha256:f8477c9aa8bf4ae1131f0b8c7dbdca985be61f91d635363d1992cadf608e04ff
source_path: markdown_output/zhang-2021-multi-horizon-forecasting-limit-order-books.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- sequence-to-sequence
- attention
- multi-horizon-forecasting
- hardware-acceleration
- equity-microstructure
- clock-event
- asset-equity
- harvest-relevant
title: 'Multi-Horizon Forecasting for Limit Order Books: Novel Deep Learning Approaches
  and Hardware Acceleration using Intelligent Processing Units'
updated: '2026-09-27T01:47:00Z'
uuid: 4d0be026-6ac6-5f35-b9f5-8e5fbec6cfd1
year: 2021
---

<!-- AUTHORED REGION START -->
# Multi-Horizon Forecasting for Limit Order Books: Novel Deep Learning Approaches and Hardware Acceleration using Intelligent Processing Units

## Summary

Most existing deep learning models for limit order book (LOB) data predict price direction at a single future point in time. The authors argue this is limiting for a stochastic, low signal-to-noise process like a LOB, and instead want one model that outputs a full forecasting path across several horizons at once, useful for trading decisions or risk management. Because the models needed for this are recurrent and slow to train, they also ask whether new hardware can speed up training.

They take the existing DeepLOB network (a convolutional block, an Inception module, and an LSTM) as an encoder, and attach one of two decoders borrowed from neural machine translation: a plain sequence-to-sequence (Seq2Seq) decoder that conditions only on the encoder's last hidden state, and an Attention decoder that lets the decoder draw on a weighted combination of all encoder hidden states. Both variants produce a three-class (up/stationary/down) forecast path across multiple horizons from a single trained network, instead of requiring one model per horizon. They evaluate on the public FI-2010 LOB benchmark and on a full year of order book data for five London Stock Exchange (LSE) stocks, and test transfer of the trained models to 20 further LSE stocks not used in training. Separately, they benchmark training time for these and other LOB networks on a single GPU against a Graphcore Intelligent Processing Unit (IPU).

On FI-2010, both DeepLOB-Seq2Seq and DeepLOB-Attention match prior state-of-the-art single-horizon models at short horizons and do better at the longest tested horizon, which the authors attribute to the decoder's autoregressive structure feeding short-term estimates into later predictions. The same pattern appears on the LSE dataset, and the models generalize to the 20 held-out stocks not used to fit them. Attention weights are concentrated on the most recent order book observations, which the authors use to explain why the plainer Seq2Seq decoder is not hurt by long input sequences here. On hardware, training an encoder-decoder model on the IPU takes about 15% of the GPU wall-clock time needed for the same training run, using a single NVIDIA GeForce RTX 2080 as the GPU comparison point.

The main contribution is a network that outputs a multi-step forecast path from a single model rather than one model per horizon, applied here for the first time (to the authors' knowledge) to limit order book data, together with a practical demonstration that a non-GPU accelerator can substantially cut training time for the resulting recurrent architectures.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations and prediction horizons are counted in limit order book update events ('tick time', i.e. consecutive LOB updates), not wall-clock time. Each input uses the most recent 50 LOB updates (both ask and bid sides). On FI-2010 the model predicts a 3-class direction label at horizons k = 10, 20, 30, 50, 100 updates ahead; on the LSE dataset it predicts at k = 20, 50, 100 updates ahead. The label at each horizon is assigned by comparing the percentage change in mid-price over that many updates to an instrument-specific threshold.

## Data

- **Asset class:** Equities
- **Instruments:** FI-2010: five stocks from the Nasdaq Nordic exchange. LSE dataset: Lloyds (LLOY), Barclays (BARC), Tesco (TSCO), BT, and Vodafone (VOD) as the core training/testing stocks, plus 20 additional London Stock Exchange stocks used only to test transfer of the trained models.
- **Venue:** Nasdaq Nordic stock exchange (FI-2010 dataset) and the London Stock Exchange (LSE dataset)
- **Period:** FI-2010 covers 10 consecutive trading days. The LSE dataset covers the full year 2018, split into the first 6 months for training, the next 3 months for validation, and the last 3 months for testing.
- **Granularity:** Limit order book updates with up to 10 price/volume levels on each side (bid and ask); each network input uses the most recent 50 updates. LSE data is restricted to continuous trading hours, 08:30:00 to 16:00:00, excluding auctions.

## Features and Measures

- **encoder context vector (Seq2Seq).** The last hidden state of the recurrent encoder that has read the order book input sequence, used as the single summary vector the decoder conditions on to generate the whole forecast path.
- **attention context vector.** A weighted combination of all encoder hidden states, with weights recomputed at every decoder step, letting the decoder draw on encoder information from any point in the input sequence rather than only its last hidden state.
- **DeepLOB encoder features.** Features extracted from the raw price/volume grid of the order book by a convolutional block, an Inception module, and an LSTM layer, used as the encoder for both new decoder variants.
- **class threshold label (alpha).** A per-instrument threshold on the percentage change of the mid-price over the prediction horizon, used to assign each observation to an up, down, or stationary class while keeping classes roughly balanced.

## Method

The authors use the existing DeepLOB network (convolutional block, Inception module, LSTM) as an encoder that reads the raw order book price/volume grid, then attach either a Seq2Seq decoder (a single LSTM conditioned on the encoder's final hidden state) or an Attention decoder (an LSTM that additionally computes a weighted combination of all encoder hidden states at each output step) to produce a sequence of class probabilities across several future horizons in one forward pass. The whole network is trained end to end with a categorical cross-entropy loss. Each input window covers the 50 most recent order book updates on both sides, giving each sample dimension (50, 40). Labels are three-class (up/stationary/down), assigned from the percentage change in mid-price over the horizon relative to an instrument-specific threshold chosen to keep classes roughly balanced.

Models are evaluated with accuracy, precision, recall and F1, with Kolmogorov-Smirnov tests used to check whether differences between models are statistically significant; F1 is treated as the main metric because the FI-2010 labels are not well balanced. Separately, the authors compare training-time efficiency of DeepLOB, DeepLOB-Seq2Seq, DeepLOB-Attention and three earlier benchmark networks (MLP, CNN-I, LSTM) on a single NVIDIA GeForce RTX 2080 GPU against a Graphcore IPU, training each for 200 epochs and reporting the average training time per epoch.

## Results

- On FI-2010, DeepLOB-Seq2Seq and DeepLOB-Attention perform comparably to prior state-of-the-art single-horizon models at short horizons (k = 10, 20, 30, 50) and outperform them at the longest tested horizon (k = 100), with DeepLOB-Attention the better of the two.
- All model comparisons on the FI-2010 results are reported as statistically different according to Kolmogorov-Smirnov tests.
- On the LSE dataset, DeepLOB-Seq2Seq and DeepLOB-Attention match DeepLOB's performance at short horizons and outperform it at longer horizons (k = 50, 100), attributed to the decoder feeding short-term estimates into later-horizon predictions.
- Applying the models (trained on 5 instruments) directly to 20 other LSE stocks not used in training still gives strong predictive results, with DeepLOB-Attention showing an additional edge over the other two models.
- Attention weights from DeepLOB-Attention are concentrated on the most recent order book observations, with features further in the past contributing little to predictions.
- Training an encoder-decoder model on the IPU takes about 15% of the wall-clock time needed on the comparison GPU.

## Limitations

- The authors describe the FI-2010 dataset itself as limited in scope and size, which is why they also test on the larger LSE dataset.
- The LSE experiments train and calibrate on only 5 instruments (with 20 more used only to test transfer), drawn from a single exchange and a single year (2018).
- Reader note: the GPU comparison point is a single consumer GPU model (NVIDIA GeForce RTX 2080); results may differ with other GPU hardware, and hardware benchmarking is a secondary focus relative to the forecasting results.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/feature-engineering|feature engineering]]
- [[entities/stefan-zohren|Stefan Zohren]]

## Citation

Zihao Zhang, Stefan Zohren (2021). Multi-Horizon Forecasting for Limit Order Books: Novel Deep Learning Approaches and Hardware Acceleration using Intelligent Processing Units.

DOI: 10.48550/arxiv.2105.10430

Text ingested: `markdown_output/zhang-2021-multi-horizon-forecasting-limit-order-books.md`, converted from `raw/ofi-event-clock/zhang-2021-multi-horizon-forecasting-limit-order-books.pdf`.

Coverage of this summary: Read the entire paper markdown (18 pages): abstract, introduction, literature review, IPU description, network architecture (Seq2Seq and Attention), the full experiments section (FI-2010 results, LSE results, transfer learning, IPU vs GPU comparison), conclusion, and skimmed the appendix tables (label thresholds and per-instrument transfer results) without transcribing their individual figures.

Known problems with the input: Several equations are rendered as omitted pictures or with mangled sub/superscripts in the markdown conversion; the surrounding prose was used instead of the formulas themselves; The detailed per-instrument numeric results in Tables 11, 13 and 14 (appendix) were not individually verified or used, since the paper's own prose summary of these results was sufficient for this extraction.
<!-- AUTHORED REGION END -->