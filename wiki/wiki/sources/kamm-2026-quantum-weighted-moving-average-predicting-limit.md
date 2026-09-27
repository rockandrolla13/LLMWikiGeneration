---
authors:
- Matthias Kamm
- Dinh-Long Vu
- Patrick Rebentrost
content_hash: sha256:9ef9738bb24a7e84ff1a78da63aba4e04339ca88dd2d473fb98b1d9f5ab636ca
created: 2026-09-27 01:47:00+00:00
page_id: sources/kamm-2026-quantum-weighted-moving-average-predicting-limit
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/order-flow-prediction
- concepts/deep-learning-for-finance
- concepts/feature-engineering
- concepts/transformers
- concepts/high-frequency-data
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:b0527f42cc00674d4b4e3a9cab941d94175a37af347a32d432c759f34d0649dd
source_path: markdown_output/kamm-2026-quantum-weighted-moving-average-predicting-limit.md
source_type: paper
tags:
- quantum-machine-learning
- limit-order-book
- price-trend-prediction
- fi-2010-dataset
- linear-combination-of-unitaries
- bilinear-normalization
- temporal-attention
- clock-event
- asset-equity
- harvest-relevant
title: Quantum Weighted Moving Average for Predicting Limit Order Book Trends
updated: '2026-09-27T01:47:00Z'
uuid: f6f7c5d2-c613-5f68-b21d-3771b565604a
year: 2026
---

<!-- AUTHORED REGION START -->
# Quantum Weighted Moving Average for Predicting Limit Order Book Trends

## Summary

The paper asks whether quantum computers can usefully forecast multivariate financial time series, specifically price-trend labels derived from limit order book (LOB) data. It introduces the quantum weighted moving average (QWMA), a quantum machine-learning layer built from a linear combination of unitaries (LCU) that embeds each time step of an input sequence as a unitary and combines these embeddings with trainable coefficients, drawing an explicit analogy to the classical moving average used in technical trading.

The method first identifies which components of existing classical benchmark models matter: it reproduces a prior benchmark study's comparison of models on the FI-2010 dataset and isolates the roles of bilinear/temporal/feature input normalization and of a temporal self-attention mechanism (TABL). It then builds QWMA (trainable per-time-step weights), a simplified quantum simple moving average (QSMA, uniform weights implemented with Hadamard gates), and a quantum exponential moving average (QEMA, fixed exponentially decaying weights implemented with single-qubit rotations), all simulated on a noiseless statevector simulator and compared to the classical benchmarks by F1-score across the FI-2010 dataset's five prediction horizons, plus a second dataset of China A-share stocks.

The main finding is that the combined classical-quantum QWMA model reaches performance close to the best classical models while using far fewer trainable parameters, without input normalization it fails outright, and the QEMA variant with fixed exponential weights approaches QWMA's performance whenever the unitary embedding circuit is expressive enough. Ablations show the model's learned coefficients pick out genuinely predictive time steps and features (the first-level bid/ask price). The paper explicitly states it does not demonstrate quantum advantage and instead frames the contribution as a general, hardware-aware way to map multivariate time series into a quantum circuit, plus a discussion of shortcomings in the standard LOB benchmark datasets themselves.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each time step in the FI-2010 dataset is a snapshot of the limit order book taken after a fixed count of order-book events (submissions, cancellations, deletions, and visible or hidden executions); the raw benchmark study's prediction horizons K in {10, 20, 30, 50, 100} events are renamed, following that study's convention, to K/10 in {1, 2, 3, 5, 10} time steps. The model's input is a rolling context window of the past T=10 time steps, and the prediction target is the average percentage change of the mid-price over the next K time steps relative to a fixed significance threshold.

## Data

- **Asset class:** Equities
- **Instruments:** FI-2010 benchmark dataset (Finnish stocks traded on NASDAQ Nordic); a second dataset of China A-share stocks
- **Venue:** NASDAQ Nordic (FI-2010); Chinese A-share exchanges (second dataset, not further specified in the sections read)
- **Period:** FI-2010 is described as recorded over a fixed number of trading days (stated in words in the source, not digits) and curated to approximately 396,000 time steps from about 4,000,000 raw LOB events; no explicit date range for the China A-share dataset was found in the portion of the markdown read
- **Granularity:** LOB snapshots after each fixed block of order-book events, with 144 recorded features per time step in the full FI-2010 set; this paper restricts its classical and quantum models to the 40 price/volume features of the first 10 LOB levels over a context window of T=10 time steps

## Features and Measures

- **Quantum Weighted Moving Average (QWMA) operator.** A linear combination of per-time-step unitary embeddings with trainable, non-negative coefficients that weight the contribution of each time step, implemented as a linear-combination-of-unitaries circuit using ancilla qubits and post-selection.
- **Quantum Simple Moving Average (QSMA).** A QWMA variant with the trainable coefficients replaced by uniform weights (1/T across a context window of length T), which can be prepared by applying a Hadamard gate to each ancilla qubit instead of a trained state-preparation circuit.
- **Quantum Exponential Moving Average (QEMA).** A QWMA variant with fixed, exponentially decaying coefficients governed by a multiplier alpha (set to 0.5 in the experiments) that weight recent time steps more heavily, implementable with a sequence of single-qubit rotations instead of a general state-preparation circuit.
- **Bilinear normalization (BiN).** A trainable input-normalization scheme for two-dimensional (time by feature) sequences that normalizes the input separately along the temporal axis and the feature axis and takes a learned weighted combination of the two normalized versions.
- **Temporal Attention-augmented Bilinear Network (TABL / BiNTABL).** A classical benchmark architecture that combines bilinear feature/temporal transformations with a temporal self-attention mechanism, optionally preceded by bilinear normalization (BiNTABL), used here as the strongest prior classical model on FI-2010.

## Method

Classical inputs (feature vectors per time step) are normalized (temporal, feature, or bilinear normalization, or none), linearly mapped to circuit parameters, and angle-encoded into a per-time-step unitary on nq qubits via a parameterized quantum circuit. These per-time-step unitaries are combined through a linear-combination-of-unitaries (LCU) circuit using an ancilla register: a state-preparation unitary encodes the coefficients as ancilla amplitudes (Hadamard gates for uniform QSMA weights, single-qubit rotations for exponential QEMA weights, or a general trained circuit for full QWMA), the ancilla register is measured and post-selected on the all-zero outcome, the state register is then measured in the Pauli X, Y and Z bases, and a classical multilayer perceptron maps the resulting measurement vector through a softmax to the three-class trend probabilities.

All quantum models are simulated (not run on physical hardware) using the noiseless TorchQuantum statevector simulator built on PyTorch. Classical benchmarks (MLP, TABL, BiNTABL) are trained with the Adam optimizer at learning rate 0.001, batch size 128, and 100 epochs, using a weighted cross-entropy loss to counter class imbalance; the quantum experiments instead use batch size 256, an Adam learning rate of 0.002 with cosine annealing, and 30 training epochs, which the authors report was sufficient for the loss to converge. Model quality is judged with the F1-score across the FI-2010 dataset's five prediction horizons, plus dedicated ablations for temporal importance, feature importance, and an empirical estimate of the LCU circuit's post-selection success probability.

## Results

- The trainable-weight QWMA model performs comparably to the classical MLP and BiNTABL benchmarks for longer prediction horizons (K in {5,10}) and slightly worse for shorter horizons (K in {1,2,3}), while using far fewer trainable parameters: 2.2k for a 6-qubit QWMA versus 11k for BiNTABL and 256k for the MLP.
- QWMA needs input normalization to work at all: without normalization, or with feature-only normalization, it fails to reliably predict price trends on FI-2010, whereas temporal normalization alone performs about as well as the combined bilinear normalization.
- The uniform-weight QSMA model underperforms QWMA, improves clearly with more qubits (nq in {2,4,6}) for a shallow embedding circuit, and gets close to QWMA's performance once a deeper, more expressive embedding circuit is used.
- The exponentially-weighted QEMA model (multiplier alpha=0.5) outperforms QSMA for short horizons (K in {1,2,3}) but underperforms at K=10, and with an expressive embedding circuit its performance approaches that of trainable-weight QWMA.
- A temporal-importance ablation shows QWMA's learned per-time-step weights pick out genuinely predictive time steps: retraining on only the top-weighted steps matches or beats using the full T=10 sequence, while retraining on the low-weighted steps performs clearly worse.
- A feature-importance ablation shows the model assigns the largest weights to the first-level bid and ask price; training on just those two features matches the performance obtained from the full feature set.
- Applied to a second dataset of China A-share stocks, QWMA reaches performance comparable to the classical benchmarks and again shows QEMA generalizing better than trainable-weight QWMA, though the classical models generalize slightly better overall.
- The authors report no theoretical or numerical evidence of a quantum advantage over the classical benchmarks studied.

## Limitations

- Authors state that FI-2010's event-based sampling unevenly represents market activity (busier periods carry more information than quiet ones) and introduces autocorrelation between neighboring samples.
- Authors state that the fixed labeling threshold is chosen to balance classes only at prediction horizon K=5, which they say introduces label noise at the other horizons and may explain a performance dip observed at K=2.
- Authors note that the overlapping windows used to build consecutive labels make samples non-i.i.d., compounding the non-stationarity already present in financial data.
- Authors state that current quantum hardware is far too slow and unreliable for high-frequency trading use, and that even future fault-tolerant hardware would still require costly post-selection and multi-controlled gates for the LCU circuit.
- Reader note: all reported results come from noiseless statevector simulation rather than physical quantum hardware, so hardware noise and post-selection overhead are not reflected in the F1-scores presented.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/transformers|transformers]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Matthias Kamm, Dinh-Long Vu, Patrick Rebentrost (2026). Quantum Weighted Moving Average for Predicting Limit Order Book Trends.

DOI: 10.48550/arxiv.2609.01524

Text ingested: `markdown_output/kamm-2026-quantum-weighted-moving-average-predicting-limit.md`, converted from `raw/ofi-event-clock/kamm-2026-quantum-weighted-moving-average-predicting-limit.pdf`.

Coverage of this summary: Read the full markdown of the preprint from title/abstract through the conclusion, acknowledgements and reference list (Sections 1-9), and continued into the appendices covering the classical bilinear-normalization/TABL background (App. A) and the temporal- and feature-importance ablations (App. B) plus the start of the LCU success-probability discussion (App. C); the detailed China A-share results in App. D were only covered via the one summary sentence given in Section 7, not read in full.

Known problems with the input: All equations and plots are rendered in the markdown as image placeholders ('picture... intentionally omitted') or garbled OCR text (e.g. duplicated legend text in the Figure 6/7 captions), so exact equation forms and plotted values could not be verified beyond the surrounding prose; The FI-2010 trading-day count and stock count are given in the source as words ('ten trading days', 'five Finnish stocks') rather than digits, so those specific counts are described in words here rather than as numbers, per the numbers rule.
<!-- AUTHORED REGION END -->