---
authors:
- Yufei Wu
- Mahmoud Mahfouz
- Daniele Magazzeni
- Manuela Veloso
content_hash: sha256:15020aae6ff23bc9872e176415e39c9bee85379ecc17eb1ddc53de946845d5d2
created: 2026-09-27 01:47:00+00:00
page_id: sources/wu-2021-how-robust-limit-order-book-representations
page_type: source
publication_venue: Proceedings of the 38th International Conference on Machine Learning,
  PMLR 139, 2021
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/feature-engineering
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:2ecef98b362a96ddfa200d092c1b8ca6f9a5b885549dcb085a8c0fb08892c9a4
source_path: markdown_output/wu-2021-how-robust-limit-order-book-representations.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- data-perturbation
- price-forecasting
- market-microstructure
- robustness
- representation-learning
- clock-event
- asset-equity
- harvest-relevant
title: How Robust are Limit Order Book Representations under Data Perturbation?
updated: '2026-09-27T01:47:00Z'
uuid: 813ef3d9-b461-50e2-994e-256600466ea1
year: 2021
---

<!-- AUTHORED REGION START -->
# How Robust are Limit Order Book Representations under Data Perturbation?

## Summary

The paper asks whether the usual way of feeding limit order book (LOB) data into machine learning models is actually a stable representation, or whether it is fragile to small, realistic changes in the underlying order book. It focuses on price forecasting from LOB snapshots, since almost all recent deep-learning studies feed models the same price-level vector format without questioning it.

The authors introduce a perturbation method: they add minimum-size orders at previously empty price levels beyond the best bid and ask, chosen so the mid-price itself never moves. This shifts which orders occupy each price level in the representation even though the total added volume is tiny. They train logistic regression, a multi-layer perceptron, an LSTM, and the DeepLOB convolutional-LSTM model on the FI-2010 benchmark dataset to predict short-horizon mid-price direction, then test each model on unperturbed data and on data perturbed on the ask side, the bid side, or both.

All four models lose accuracy once the perturbation is applied, and the loss is worse for the more complex models. DeepLOB, the strongest model on unperturbed data, degrades the most and ends up performing worse than logistic regression once both sides are perturbed. The authors also show that a tiny order-volume change produces a large jump in the raw input vector, meaning the representation does not vary smoothly with small real-world changes.

The contribution is diagnostic rather than a new model: the paper frames itself as a first attempt to directly test the robustness of the price-level LOB representation, and it closes by proposing four desiderata -- smoothness, efficiency, stochasticity and validity -- that future LOB representations and the models built on them should satisfy.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Each input observation stacks a history of T=10 raw limit order book snapshots (10 price levels per side), each snapshot corresponding to an order book update (placement, cancellation or execution). The model predicts a three-class label for the smoothed mid-price move over a prediction horizon of k=50 future snapshots, using a threshold of 0.002 to separate the up/stationary/down classes.

## Data

- **Asset class:** Equities
- **Instruments:** 5 stocks from the Helsinki Stock Exchange (the FI-2010 benchmark dataset)
- **Venue:** Helsinki Stock Exchange
- **Period:** 10 trading days, normal trading hours with no auctions
- **Granularity:** Limit order book snapshots with 10 price levels on the bid and ask sides, updated on order placement, execution and cancellation events

## Features and Measures

- **Level-based LOB vector.** A snapshot of the order book represented as a fixed-length vector of ask/bid prices and volumes at each of 10 price levels, stacked over a history window to form the model input.
- **Data perturbation (minimum-size fill).** Adding orders of the smallest allowed size at empty price levels beyond the best bid/ask, chosen so neither the mid-price nor the prediction label changes, used to test representation robustness.
- **Micro-movement prediction label.** A three-class label (up/stationary/down) built from the smoothed mid-price a fixed number of snapshots ahead, using a fixed threshold to separate the classes.

## Method

The paper benchmarks four supervised models -- logistic regression, a multi-layer perceptron, an LSTM, and the DeepLOB convolutional-LSTM architecture -- all trained on the same FI-2010 training set to predict a three-class mid-price movement label over a fixed prediction horizon. Each trained model is then evaluated on four test conditions: the original unperturbed test data, data perturbed only on the ask side, data perturbed only on the bid side, and data perturbed on both sides. Performance is judged with accuracy, precision, recall and F-score (all in percent), with precision/recall/F-score averaged unweighted across classes to correct for class imbalance in the test set, and confusion matrices are used to show how misclassifications shift under perturbation.

## Results

- All four models (logistic regression, MLP, LSTM, DeepLOB) lost predictive accuracy once minimum-size orders were added at empty price levels, even though the perturbation never changed the mid-price or the true label.
- DeepLOB, the strongest model with no perturbation (77.2% accuracy), suffered the largest decline, falling to 47.5% accuracy and a 22.2% F-score once both sides of the book were perturbed, underperforming logistic regression on F-score.
- One-sided (ask-only or bid-only) perturbation cut accuracy by about 6% for the MLP, about 7% for the LSTM, and 9%-14% for DeepLOB; two-sided perturbation cut accuracy by about 11% for the MLP, 12% for the LSTM, and 30% for DeepLOB.
- A tiny, mid-price-neutral perturbation of only 10 units of total order volume moved the raw 40-dimensional input vector by a Euclidean distance of 344.623, showing the representation is not locally smooth.
- Under heavy (both-sided) perturbation, DeepLOB's confusion matrix showed it classifying almost all samples as 'stationary', a near-complete breakdown compared with its behaviour on unperturbed data.
- Logistic regression showed the smallest degradation, mainly because it already classified most samples as 'stationary' regardless of perturbation, so it had little accuracy left to lose.

## Limitations

- The perturbation study is demonstrated on a single benchmark (FI-2010), covering 5 stocks over 10 trading days on one exchange.
- The paper tests only one representation family (price-level vectors) and one perturbation design (minimum-size fills at empty levels); it does not implement or test the alternative representations it recommends.
- Reader note: with only 5 stocks and 10 trading days, the perturbation experiment is a controlled proof-of-concept rather than a broad robustness study across market regimes.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Yufei Wu, Mahmoud Mahfouz, Daniele Magazzeni, Manuela Veloso (2021). How Robust are Limit Order Book Representations under Data Perturbation?. Proceedings of the 38th International Conference on Machine Learning, PMLR 139, 2021.

DOI: 10.48550/arxiv.2110.04752

Text ingested: `markdown_output/wu-2021-how-robust-limit-order-book-representations.md`, converted from `raw/ofi-event-clock/wu-2021-how-robust-limit-order-book-representations.pdf`.

Coverage of this summary: Read the entire markdown file, a short conference paper (abstract through references, all sections and Table 1).
<!-- AUTHORED REGION END -->