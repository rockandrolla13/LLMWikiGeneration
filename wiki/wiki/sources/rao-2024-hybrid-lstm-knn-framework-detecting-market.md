---
authors:
- GuoLi Rao
- Tianyu Lu
- Lei Yan
- Yibang Liu
content_hash: sha256:82efc3ad29cbc8cc4a2cac586efd37e2fe48fd690cc14919af3546fe10e1b563
created: 2026-09-27 01:47:00+00:00
page_id: sources/rao-2024-hybrid-lstm-knn-framework-detecting-market
page_type: source
publication_venue: Journal of Knowledge Learning and Science Technology
related:
- concepts/trade-clock
- concepts/lstm-networks
- concepts/deep-learning-for-finance
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/bid-ask-spread
- concepts/jump-clustering
- concepts/order-imbalance
revision_id: 1
schema_version: 2
source_hash: sha256:7250551ff22e06bb49efdc85d2a9907bdb0e0413660c86d5a9fb3b404a7d085f
source_path: markdown_output/rao-2024-hybrid-lstm-knn-framework-detecting-market.md
source_type: paper
tags:
- credit-default-swaps
- jump-detection
- lstm
- knn
- market-microstructure
- hybrid-model
- clock-trade
- asset-bonds-rates
- harvest-relevant
title: 'A Hybrid LSTM-KNN Framework for Detecting Market Microstructure Anomalies:
  Evidence from High-Frequency Jump Behaviors in Credit Default Swap Markets'
updated: '2026-09-27T01:47:00Z'
uuid: f2425cb8-0067-50ee-86f8-89e0f4d1041a
year: 2024
---

<!-- AUTHORED REGION START -->
# A Hybrid LSTM-KNN Framework for Detecting Market Microstructure Anomalies: Evidence from High-Frequency Jump Behaviors in Credit Default Swap Markets

## Summary

The paper's stated question is whether combining LSTM's temporal feature learning with KNN's pattern-based classification can detect price jumps in high-frequency credit default swap (CDS) markets more accurately than either classical statistical jump tests or a single machine-learning model on its own.

The proposed framework has three stages: a preprocessing module that cleans missing tick values; a stacked LSTM (three layers of 128, 256 and 64 units) that learns a 32-dimensional temporal feature representation over a 50-time-step window; and a KNN classifier, tuned over k = 3 to 15 with k = 7 selected as optimal, that labels jump events from those learned features. The framework is evaluated on tick-by-tick CDS data from five major indices (CDX NA IG, CDX NA HY, iTraxx Europe, iTraxx Asia, CDX EM) covering January 2020 to December 2023, and compared against a standalone LSTM, a standalone KNN, an unnamed statistical baseline, and a random forest.

The paper's headline claim, repeated in the abstract and conclusion, is that the hybrid model reaches a test-set jump-detection accuracy around 92.8%, ahead of the other baselines, with an average processing latency of about 48 milliseconds; a feature-importance analysis attributes a large share of detection accuracy to bid-ask spreads and order-book imbalances. However, a separate passage in the methodology section states a materially different accuracy figure (93.5%) for what is described as the same integrated model, an inconsistency noted below.

The stated contribution is a hybrid deep-learning/classical-ML pipeline specifically applied to CDS market jump detection, an asset class and anomaly-detection task the authors argue has been underexplored relative to equities.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

The model consumes tick-by-tick CDS price and quote data (bid-ask spreads, trading volume, order-book depth), using a rolling training window of 50,000 ticks and an LSTM input window of 50 time steps, with the KNN stage then classifying jump versus non-jump states from the learned features. The paper does not clearly state a fixed forward prediction horizon beyond this tick-window-based sampling.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** Five major credit default swap indices: CDX NA IG, CDX NA HY, iTraxx Europe, iTraxx Asia, CDX EM
- **Venue:** not stated
- **Period:** January 2020 to December 2023
- **Granularity:** Tick-by-tick data; over 2.5 million data points in total, with daily tick counts per index ranging from roughly 2,715 to 3,275

## Features and Measures

- **Bid-ask spread.** Identified in the paper's feature-importance analysis as the largest single predictor of detected jumps, attributed 45% of detection accuracy.
- **Order-book imbalance.** Identified as the second most important predictor of detected jumps, attributed 32% of detection accuracy.
- **LSTM-learned temporal feature vector.** A 32-dimensional representation produced by the stacked LSTM layers from the raw tick window, passed forward as the input to the KNN classification stage.

## Method

The framework has three stages: a data-preprocessing module that cleans missing values (0.32% of raw data, reduced to 0.00% after processing) using microstructure-based interpolation; a three-layer LSTM (128, 256 and 64 units across the layers, tanh activations, dropout of 0.2 to 0.3) that learns a 32-dimensional feature representation over a 50-time-step input window; and a KNN classifier swept over k = 3, 5, 7, 11 and 15, with k = 7 selected as optimal. Training uses a rolling 50,000-tick window, a batch size of 64, a learning rate of 0.001, a 20% validation split and a 30% test split, run for 8.5 hours on a 16GB GPU with 64 CPU cores. Performance is judged by accuracy, precision, recall, F1-score and processing latency, benchmarked against a standalone LSTM, a standalone KNN, an unnamed statistical method, and a random forest.

## Results

- The paper's headline figure, given in both the abstract and conclusion, is 92.8% jump-detection accuracy for the hybrid model on the test set, described as a 15.2% improvement over traditional statistical methods and an 8.5% improvement over standalone deep learning.
- A separate paragraph in the methodology section instead states the integrated model reaches 93.5% accuracy, a 15% improvement over standalone LSTM or KNN -- a figure that does not match the 92.8% reported elsewhere in the same paper.
- A benchmark table lists test-set accuracy as 0.928 for the hybrid model versus 0.876 for a standalone LSTM, 0.843 for a standalone KNN, 0.856 for a random forest, and 0.812 for the unnamed statistical baseline.
- Average processing latency for the hybrid model is reported as 48.2 milliseconds, versus 45.5ms (LSTM only), 28.3ms (KNN only), and 15.7ms (statistical method).
- Feature-importance analysis attributes 45% of detection accuracy to bid-ask spreads and 32% to order-book imbalances, alongside a 0.83 correlation between detected jumps and market liquidity during high-volatility periods.
- A separate sweep of the KNN classifier alone over k = 3, 5, 7, 11, 15 peaked at k = 7 with 0.924 accuracy.
- The dataset spans five CDS indices with jump-event counts ranging from 977 to 1,342 per index.

## Limitations

- Authors state the model depends on consistently available high-quality, high-frequency data, which may not exist across all market segments.
- Authors state the computational requirements for real-time processing may be a barrier for smaller market participants.
- Authors state the framework's effectiveness in extreme market conditions is only partially validated, given few such events occurred in the sample period, and the current implementation is specific to CDS markets.
- Reader note: the paper gives two different, mutually inconsistent overall accuracy figures for what is presented as the same hybrid model's test performance -- 92.8% (abstract, conclusion, and the main benchmark table) versus 93.5% (a methodology-section paragraph and a separate integration table) -- so its headline performance claim should be treated with caution.
- Reader note: the acknowledgments and several reference-list entries cite the authors' own work on apparently unrelated topics (monoclonal antibody production, IoT network traffic anomaly detection, drug discovery, Kubernetes cluster optimisation), and the journal's own masthead is internally inconsistent (a decreasing page range of 361-170, and an Accepted date of 10-12-2024 followed by a Published date of 25-12-2025, a year after the stated 2024 issue), which together raise doubts about the outlet's editorial rigor and the reliability of the reported numbers.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/jump-clustering|jump clustering]]
- [[concepts/order-imbalance|order imbalance]]

## Citation

GuoLi Rao, Tianyu Lu, Lei Yan, Yibang Liu (2024). A Hybrid LSTM-KNN Framework for Detecting Market Microstructure Anomalies: Evidence from High-Frequency Jump Behaviors in Credit Default Swap Markets. Journal of Knowledge Learning and Science Technology.

DOI: 10.60087/jklst.v3.n4.p361

Text ingested: `markdown_output/rao-2024-hybrid-lstm-knn-framework-detecting-market.md`, converted from `raw/ofi-event-clock/rao-2024-hybrid-lstm-knn-framework-detecting-market.pdf`.

Coverage of this summary: Read the whole paper: abstract, introduction, literature review, methodology, empirical results, conclusion, acknowledgments and references.

Known problems with the input: The paper reports two different, contradictory overall test-accuracy figures for the same hybrid model: 92.8% (abstract, conclusion, main benchmark table) versus 93.5% (a methodology-section paragraph and a separate integration-metrics table); both are reproduced above as printed, but they cannot both be correct; Much of the prose, especially the introduction and literature-review sections, reads as garbled, machine-generated text with non-standard grammar (for example, describing the research as helping 'the participants in the business to manage the risks better'); this is reproduced faithfully as the paper's own wording, not corrected; The journal's own masthead metadata is internally inconsistent: the listed page range is 361-170 (a decreasing range), and the paper is marked Accepted 10-12-2024 but Published 25-12-2025, a year after acceptance and after the stated 2024 issue year; The acknowledgments and several reference-list entries cite work on subjects unrelated to this paper (monoclonal antibody production, IoT network traffic anomaly detection, drug discovery, Kubernetes cluster optimisation), consistent with citation padding rather than genuine related work; Given the above, this paper's numeric results should be treated as unverified; they are reported here only because the exact digit strings appear in the converted text, not because the paper's methodology or editorial process is trustworthy.
<!-- AUTHORED REGION END -->