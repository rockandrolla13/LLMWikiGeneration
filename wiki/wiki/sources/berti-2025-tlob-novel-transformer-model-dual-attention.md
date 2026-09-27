---
authors:
- Leonardo Berti
- Gjergji Kasneci
content_hash: sha256:5d7cbf4cf81f23b8b6c6c248977676c7f3aecde2ac4c007f93b77e0a08223b94
created: 2026-09-27 01:47:00+00:00
page_id: sources/berti-2025-tlob-novel-transformer-model-dual-attention
page_type: source
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/transformers
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/lstm-networks
- concepts/order-flow-prediction
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:dfa71c491870cfdb751814c6b600a12f994e1b2cc5e27a1c7419c562e5c9304a
source_path: markdown_output/berti-2025-tlob-novel-transformer-model-dual-attention.md
source_type: paper
tags:
- transformer
- limit-order-book
- price-trend-prediction
- dual-attention
- fi-2010
- bitcoin
- market-efficiency
- labeling-bias
- clock-compares
- asset-multi
- harvest-relevant
title: 'TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction
  with Limit Order Book Data'
updated: '2026-09-27T01:47:00Z'
uuid: 70d190e6-b33f-5b4c-b7da-e4adc4e0518d
year: 2025
---

<!-- AUTHORED REGION START -->
# TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data

## Summary

The paper addresses price trend prediction (PTP) from limit order book (LOB) data, arguing that existing deep learning models for this task generalize poorly across market conditions and assets. It proposes two new architectures: MLPLOB, a simple MLP-Mixer-style model with alternating feature-mixing and temporal-mixing layers, and TLOB, a transformer that applies two separate self-attention operations per block — one over the temporal axis (across LOB snapshots) and one over the feature axis (across price/volume features) — followed by an MLPLOB block instead of a standard feed-forward layer, with a bilinear normalization layer at the input to handle non-stationarity.

Both models are evaluated on three datasets: the FI-2010 benchmark of five Finnish NASDAQ Nordic stocks (sampled every 10 events), a NASDAQ dataset of Tesla and Intel built by the authors and sampled every 500 shares traded (volume-based sampling), and a 2023 Binance Bitcoin perpetual dataset sampled at 250ms intervals. They also introduce a new labeling method that decouples the past smoothing window from the future prediction horizon, removing a bias present in prior labeling schemes that tied the two together.

TLOB and MLPLOB beat all listed SOTA baselines (including SVM, Random Forest, XGBoost, LSTM, CNN, CTABL, DAIN, CNNLSTM, DeepLOB, BiN-CTABL, AXIALLOB and DLA) on every dataset and horizon tested. MLPLOB tends to win at short horizons while TLOB, benefiting from long-range attention, wins at longer horizons. The paper also finds that Intel's predictability fell between 2012 and 2015, and that redefining the trend threshold as the average bid-ask spread (rather than a class-balancing value) sharply degrades performance, which the authors read as evidence that classification accuracy does not translate directly into trading profitability.

What is new relative to prior work is the dual-attention (temporal + spatial) transformer design itself, the demonstration that a much simpler MLP-based model can match or beat specialized LOB architectures, the horizon-bias-free labeling scheme, and the explicit link drawn between prediction accuracy, historical market efficiency, and transaction-cost-aware thresholding.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The three datasets use three different sampling schemes: FI-2010 is sampled every 10 LOB events (event-based); the Tesla/Intel dataset built by the authors is sampled every 500 shares traded (volume-based), chosen after explicitly weighing time-based, event-based and volume-based sampling and judging volume-based best able to reflect the varying market impact of individual trades; the Bitcoin dataset is sampled at a fixed 250-millisecond wall-clock interval. Prediction horizons of 10, 20, 50 and 100 observations ahead are used (with an additional 200-step horizon in the spread-threshold experiment), each defined as a count of sampled observations rather than elapsed time.

## Data

- **Asset class:** Several asset classes
- **Instruments:** FI-2010: five Finnish NASDAQ Nordic stocks (Kesko Oyj, Outokumpu Oyj, Sampo, Rautaruukki, Wärtsilä Oyj); NASDAQ dataset: Tesla (TSLA) and Intel (INTC); crypto dataset: Bitcoin perpetual futures (BTCUSDT.P)
- **Venue:** NASDAQ Nordic (FI-2010), NASDAQ (TSLA/INTC), Binance (BTC)
- **Period:** FI-2010: June 1 to June 14, 2010; TSLA/INTC: January 2 to January 30, 2015, with one additional Intel day from June 21, 2012 used for a historical comparison; BTC: January 9 to January 20, 2023
- **Granularity:** FI-2010 sampled every 10 LOB events (about 394,337 samples across 10 levels); TSLA/INTC sampled every 500 shares traded, using 10 LOB levels augmented with message-file order data; BTC sampled at 250-millisecond intervals (about 3,730,870 rows)

## Features and Measures

- **TLOB dual-attention block.** A transformer block containing separate self-attention operations over the temporal axis (across LOB snapshots) and the feature axis (across price/volume features), followed by an MLPLOB feed-forward block, used to jointly capture spatial and temporal LOB dependencies.
- **MLPLOB.** An isotropic MLP-Mixer-style model built from alternating feature-mixing and temporal-mixing fully connected layers with GeLU activations, used both as a standalone baseline and as the feed-forward component inside TLOB.
- **Bilinear normalization layer.** An input normalization layer (adapted from prior work) that adapts to batch-specific statistics rather than fixed z-score statistics, used to handle non-stationarity and magnitude disparity between prices and sizes.
- **Decoupled smoothing-horizon labeling.** A trend-labeling method that sets the past-smoothing window length independently from the future prediction horizon, correcting a bias in prior methods where the two were forced to be equal.

## Method

Both models take as input a sequence of the last T LOB snapshots across 10 price/volume levels per side. MLPLOB projects the input linearly, then alternates feature-mixing MLPs (applied per time step across features) and temporal-mixing MLPs (applied per feature across time), each with GeLU activations and layer normalization, before a final dimensionality-reducing classification head. TLOB stacks multiple dual-attention blocks (temporal self-attention, then feature self-attention, then an MLPLOB block), preceded by bilinear normalization and sinusoidal positional encoding, with the number of layers and other hyperparameters chosen via grid search (reported in a supplementary table).

Models are trained with the Adam optimizer to predict a ternary (up/down/stable) trend label. On FI-2010 the original labels and threshold are kept for comparability with prior benchmarks; on TSLA/INTC and BTC the threshold is set to the mean percentage price change to balance classes, and a separate experiment instead sets it to the average bid-ask spread as a percentage of mid-price. F1-score is used as the primary metric because classes are imbalanced; precision-recall curves are also reported. TLOB and MLPLOB are compared against 3 classical ML baselines (SVM, Random Forest, XGBoost) and 10 deep-learning SOTA LOB models, with the top-2 performers (DeepLOB, BiN-CTABL) carried over to the TSLA-INTC and BTC datasets due to compute constraints. An ablation study removes spatial or temporal attention from TLOB to isolate each mechanism's contribution.

## Results

- On FI-2010, TLOB's F1 reached 92.81 at horizon 100, versus 92.62 for MLPLOB and lower scores for all other SOTA baselines listed in the paper.
- MLPLOB outperformed TLOB on the two shorter FI-2010 horizons (e.g., 91.39 vs 90.03 at horizon 50), consistent with TLOB's transformer design paying off mainly at longer horizons.
- On Tesla, TLOB and MLPLOB's average F1 improvement over the best baseline was 1.3; on Intel it was 7.7.
- On the 2023 Bitcoin dataset, TLOB was the best model on every horizon, with an average F1 improvement of 1.1 over the prior SOTA.
- Comparing Intel on a single day from 2012 versus 2015 (both at horizon 50), TLOB's F1 fell from 66.87 to 60.19, which the authors read as evidence of declining stock-price predictability over time.
- Setting the trend threshold to the average bid-ask spread (Tesla only) produced F1 scores of 41.39 (horizon 50), 36.48 (horizon 100) and 30.82 (horizon 200), substantially lower than under the class-balancing threshold.
- Ablation on FI-2010 at horizon 100: full TLOB scored 92.81 F1, versus 91.40 without spatial attention and 91.42 without temporal attention, with the full dual-attention model ahead at every horizon tested.

## Limitations

- Authors state the proposed methods are not yet mature enough for deployment in live trading.
- The TSLA-INTC dataset cannot be released publicly for copyright reasons, limiting external reproducibility.
- Authors state that defining the trend threshold via average spread degrades classification performance, exposing a gap between academic metrics and practical trading profitability.
- Reader note: the historical-decline comparison for Intel rests on a single day each from 2012 and 2015.
- Reader note: the Bitcoin sample spans only 12 consecutive days.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/transformers|transformers]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Leonardo Berti, Gjergji Kasneci (2025). TLOB: A Novel Transformer Model with Dual Attention for Price Trend Prediction with Limit Order Book Data.

DOI: 10.48550/arxiv.2502.15757

Text ingested: `markdown_output/berti-2025-tlob-novel-transformer-model-dual-attention.md`, converted from `raw/ofi-event-clock/berti-2025-tlob-novel-transformer-model-dual-attention.pdf`.

Coverage of this summary: Read the full paper end-to-end, including introduction, background, related work, task definition, models, all experiment sections, conclusion, limitations, and the appendix hyperparameter table.

Known problems with the input: No explicit publication year is printed on the paper itself; used the year_hint (2025) from the job file; No venue (journal/conference/workshop) is stated in the text read; left venue empty; The main text states the Bitcoin data is sampled every 250 milliseconds, while a footnote in the same section states the BTC dataset is sampled every 100ms; both figures appear in the source and are noted here as an internal inconsistency.
<!-- AUTHORED REGION END -->