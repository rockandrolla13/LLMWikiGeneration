---
authors:
- Muyao Zhong
- Yushi Lin
- Peng Yang
content_hash: sha256:07f96e8e2d2ec29142d58a47743688a96ee44004bf163d895ae7b26e7bf60c66
created: 2026-09-27 01:47:00+00:00
page_id: sources/muyao-2025-representation-learning-limit-order-book-comprehensive
page_type: source
related:
- concepts/limit-order-book
- concepts/transformers
- concepts/lstm-networks
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:a08e004d6c93cffcb76e949389087c0c0e4448bc96e6486d97fd161f473798cd
source_path: markdown_output/muyao-2025-representation-learning-limit-order-book-comprehensive.md
source_type: paper
tags:
- limit-order-book
- representation-learning
- benchmark
- china-a-share
- deep-learning
- transformers
- price-trend-prediction
- transfer-learning
- clock-calendar
- asset-equity
- harvest-relevant
title: 'Representation Learning of Limit Order Book: A Comprehensive Study and Benchmarking'
updated: '2026-09-27T01:47:00Z'
uuid: 843ad6b7-2ba0-5458-9ec7-b4ae3d1954dc
year: 2025
---

<!-- AUTHORED REGION START -->
# Representation Learning of Limit Order Book: A Comprehensive Study and Benchmarking

## Summary

The paper asks whether a single, general-purpose representation of the limit order book (LOB) learned through reconstruction can serve multiple downstream tasks as well as, or better than, models built end-to-end for each task separately. To test this, the authors introduce LOBench, a benchmark built from real China A-share market data with unified preprocessing, normalization and evaluation, and benchmark nine neural architectures spanning foundational models (CNN, LSTM, Transformer), general-purpose time-series models (iTransformer, TimesNet, TimeMixer), and LOB-specific models (DeepLOB, TransLOB, SimLOB).

The framework standardizes stock selection, temporal alignment (dropping the noisy pre-open and pre-close auction phases), a global (cross-feature) z-score normalization that avoids breaking the LOB's required price ordering, and sliding-window segmentation. Reconstruction is trained with a composite loss combining weighted mean-squared error with a structural penalty for price-ordering violations, and the resulting encoders are reused, frozen, as feature extractors for two downstream tasks: price-trend classification and masked-snapshot imputation.

Across five stocks, most models reconstruct the LOB with low error, and models built on Transformer-style architectures generally do best, while DeepLOB, CNN and LSTM show clearer weaknesses. Freezing a pretrained reconstruction encoder and only training a lightweight decoder matches end-to-end training on prediction and imputation, and transfers substantially better to unseen stocks than any end-to-end model.

The contribution is the first standardized, reproducible benchmark and comparative study of LOB representation learning as a decoupled paradigm, rather than task-specific end-to-end modeling, along with a structure-aware reconstruction loss and empirical evidence for the sufficiency and transfer benefit of learned LOB representations.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Raw exchange order-flow updates for five China A-share stocks are resampled into LOB snapshots every 3 seconds (10 price levels per side), using forward-fill when no trade occurs in an interval; only the continuous auction period (09:30-11:30 and 13:00-14:57) is kept. Sequences are cut into sliding windows of 100 consecutive snapshots (about five minutes of trading), and the label for the last snapshot in a window is the direction of the average mid-price over the following 5 snapshots relative to a 0.001 threshold.

## Data

- **Asset class:** Equities
- **Instruments:** Five Shenzhen Stock Exchange A-share stocks: Ping An Bank (sz000001), China Vanke (sz000002), Wuliangye (sz000858), Gree Electric Appliances (sz002415), Guangzhou Xiangxue Pharmaceutical (sz300147)
- **Venue:** Shenzhen Stock Exchange (SZSE)
- **Period:** Full-year 2019 trading records
- **Granularity:** Limit order book snapshots at 10 price levels per side, resampled to 3-second intervals, restricted to the continuous auction session

## Features and Measures

- **LOBench benchmark.** A standardized benchmark of curated China A-share LOB data with unified preprocessing (selection, temporal alignment, normalization, segmentation, labeling) and consistent evaluation metrics across reconstruction, prediction and imputation tasks.
- **Global (joint) z-score normalization.** Normalizing all prices together and all volumes together within a snapshot, rather than each of the 40 features separately, to avoid breaking the LOB's price-ordering constraints that feature-wise normalization can violate.
- **Composite reconstruction loss (L_All).** A training objective combining a weighted mean-squared error over prices and volumes with a structural regularization term that penalizes reconstructed bid/ask prices that violate the required price ordering.
- **Frozen-encoder transfer setup.** Using an encoder trained only on reconstruction as a fixed feature extractor, then training a small downstream decoder (or fine-tuning it on a new stock with limited data) to test transferability and reduce the need for end-to-end retraining.

## Method

Nine models spanning three families (foundational CNN/LSTM/Transformer, general-purpose time-series architectures iTransformer/TimesNet/TimeMixer, and LOB-specific DeepLOB/TransLOB/SimLOB) are trained under identical settings (256-dimensional latent representation, Adam optimizer, 100 training epochs) to encode LOB windows into a common representation space and reconstruct them with a uniform decoder, using the composite L_All loss. Reconstruction quality is compared using MSE, weighted MSE and MAE, decomposed into price and volume components, and training time is tracked on shared hardware (two NVIDIA A6000 GPUs).

The same pretrained encoders are then paired with simple fully-connected decoders for two downstream tasks: price-trend classification (up, down or flat, evaluated by cross-entropy) and masked-snapshot imputation (evaluated by mean-squared error on the masked region), both trained end-to-end and with the encoder frozen. A further experiment trains a model on one stock (sz000001) and evaluates it directly on four other stocks, then compares this to fine-tuning only the decoder of a frozen encoder on a limited amount of target-stock data (100 batches, about 20% of full training data).

## Results

- Reconstruction validation MSE and weighted MSE are on the order of 1e-3 for most models, indicating that a compact learned representation retains most of the original LOB structure.
- Transformer-family architectures (Transformer, TimesNet) generally reconstruct better than CNN or LSTM baselines; TimesNet performs best overall but has the longest training time.
- DeepLOB and CNN reconstructions show visible price-curve shifts, and DeepLOB and LSTM are consistently the weakest performers on the downstream prediction and imputation tasks.
- A frozen pretrained encoder paired with a small decoder matches end-to-end training performance on downstream tasks, needing only more training epochs for the decoder.
- The fine-tuned frozen-encoder model (SimLOB-freeze) transfers to unseen stocks better than any end-to-end model, reaching mean precision 0.7332 and mean recall 0.7260, versus 0.6289-0.7078 mean precision for models trained end-to-end only on sz000001.
- Model complexity (parameter count) does not track reconstruction quality: Transformer and TransLOB have among the most parameters but do not achieve the best reconstruction results.

## Limitations

- The benchmark currently covers only five stocks from one market (China A-share, SZSE) in one calendar year (2019), which the authors say they plan to expand.
- Raw order-flow data cannot be released due to sensitivity and proprietary restrictions, so only desensitized LOB snapshot sequences are shared, limiting exact reproducibility of the underlying data.
- Reader note: downstream prediction evaluation uses a downsampled, class-balanced version of the trend-labeling task, which may not reflect performance under the market's natural, imbalanced trend distribution.
- Reader note: only a single time-ordered 80/20 train/test split per stock is used, rather than multiple periods, so robustness to regime change over time is not directly tested.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/transformers|transformers]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Muyao Zhong, Yushi Lin, Peng Yang (2025). Representation Learning of Limit Order Book: A Comprehensive Study and Benchmarking.

DOI: 10.48550/arxiv.2505.02139

Text ingested: `markdown_output/muyao-2025-representation-learning-limit-order-book-comprehensive.md`, converted from `raw/ofi-event-clock/muyao-2025-representation-learning-limit-order-book-comprehensive.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction, related work, the LOBench framework and all preprocessing subsections (dataset, temporal alignment, normalization, segmentation, labeling, dataloader), the baseline model and downstream-task/metrics sections, all three experiment groups (reconstruction, downstream tasks, transferability) and the conclusion. Skimmed the reference list only for citation context.

Known problems with the input: year from file metadata.
<!-- AUTHORED REGION END -->