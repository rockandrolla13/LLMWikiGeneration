---
authors:
- Antonio Briola
- Jeremy Turiel
- Tomaso Aste
content_hash: sha256:6c7a63003e1b0bead8ffa1cc0358b55d186da2fed2a3edbeda5834d6ab32634f
created: 2026-09-27 01:47:00+00:00
page_id: sources/briola-2020-deep-learning-modeling-limit-order-book
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/high-frequency-trading
- entities/antonio-briola
- entities/jeremy-turiel
- entities/tomaso-aste
revision_id: 1
schema_version: 2
source_hash: sha256:fe420844f9dc0c41ffd62c55e04bbce676a05e2cc7c4e188fa46a14c057f80c0
source_path: markdown_output/briola-2020-deep-learning-modeling-limit-order-book.md
source_type: paper
tags:
- deep-learning
- limit-order-book
- lstm
- cnn-lstm
- model-comparison
- price-prediction
- lobster-data
- clock-event
- asset-equity
- harvest-relevant
title: 'Deep Learning Modelling of the Limit Order Book: A Comparative Perspective'
updated: '2026-09-27T01:47:00Z'
uuid: ff0b8bc5-87da-55a4-9311-789078cc3835
year: 2020
---

<!-- AUTHORED REGION START -->
# Deep Learning Modelling of the Limit Order Book: A Comparative Perspective

## Summary

The paper asks whether the temporal and spatial structure that recurrent, attention, and convolutional deep learning architectures explicitly impose on limit order book (LOB) data is actually necessary to forecast short-term price direction, or whether a generic Multilayer Perceptron (MLP) that models no explicit dynamic can do just as well. It reviews and re-implements a set of models from the LOB deep-learning literature (Logistic Regression, MLP, Shallow LSTM, LSTM with Self-Attention, CNN-LSTM) plus two naive baselines, trains them on identical data, features and tasks, and statistically compares their out-of-sample performance.

All models are trained on LOBSTER order-book snapshots for a single NASDAQ-listed large-tick stock (Intel, INTC), using the ten most recent order-book states (ten price/volume levels per side) as input, and are asked to classify the sign of the forward mid-price log-return into three quantile-based classes at three prediction horizons. Performance is measured with balanced accuracy, weighted precision/recall/F-measure, per-class precision/recall/F-measure, Matthews Correlation Coefficient and Cohen's Kappa, and models are grouped into statistically equivalent clusters using a Bayesian correlated t-test rather than a classical frequentist significance test.

The main finding is that the MLP performs comparably to, or slightly better than, the CNN-LSTM (the architecture the authors treat as the pre-existing state of the art) across all three horizons and most metrics, even though the MLP does not explicitly encode any temporal or spatial relationship between order-book snapshots. A Self-Attention LSTM is competitive with both at the shortest horizon but degrades sharply at longer horizons, while a plain Logistic Regression baseline is stable across horizons but systematically fails to detect the upper return quantile.

What is new is the joint, apples-to-apples statistical comparison of this family of models on one dataset and task, and the interpretive claim that follows from it: temporal and spatial structure (as encoded by LSTM and CNN layers) are good approximations of the LOB's underlying dynamics for return prediction, but the MLP's equivalent performance shows they are not obviously the necessary or unique dimensions governing that dynamic.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are per-order-book-update snapshots taken from LOBSTER order-book files at a fixed depth of ten price levels per side (a 40-dimensional state vector), so the underlying sampling clock is event time rather than a fixed wall-clock interval. The prediction target is the sign of the mid-price log-return, mapped into three quantile classes, over three horizons; each horizon is defined not as a fixed number of ticks ahead but as the point at which a fixed count (10, 50 or 100) of non-zero log-returns has accumulated, so as to skip over periods of flat, noisy order flow.

## Data

- **Asset class:** Equities
- **Instruments:** Intel Corporation (INTC) common stock, described by the authors as a representative large-tick stock
- **Venue:** NASDAQ
- **Period:** training set: 4 February 2019 to 31 May 2019 (82 files); test set: 3 June 2019 to 28 June 2019 (20 files)
- **Granularity:** event-by-event limit order book snapshots (LOBSTER orderbook files), 10 price levels per side, tick size $0.01

## Features and Measures

- **LOB state vector.** A 40-dimensional vector per snapshot listing the price and available volume at the ten nearest bid levels and ten nearest ask levels of the order book.
- **Quantile return-class labels.** The forward mid-price log-return at a given horizon is mapped into one of three classes using the 0, 0.25, 0.75 and 1.0 quantile cut points computed on the training set.

## Method

Seven models are trained on identical inputs (ten most recent 40-dimensional LOB states, flattened for the non-sequential models): a Random baseline, a Naive majority-class baseline, multinomial Logistic Regression, an MLP, a Shallow LSTM, a Self-Attention LSTM, and a CNN-LSTM. All deep models are trained with the Adam optimizer, categorical cross-entropy loss, batches of 1024 samples, and 30 epochs, with each epoch drawing a fixed number of randomly chosen batches to approximate one month of training data.

Out-of-sample performance is evaluated fold by fold using balanced accuracy, weighted precision/recall/F-measure, per-class precision/recall/F-measure, Matthews Correlation Coefficient and Cohen's Kappa. Rather than a classical null-hypothesis significance test, models are compared with a Bayesian correlated t-test, with a region of practical equivalence of 3 percent, and grouped into clusters of statistically indistinguishable performance separately for each horizon.

## Results

- Across all three prediction horizons, the Multilayer Perceptron matches or slightly outperforms the CNN-LSTM, the architecture the authors treat as state of the art, despite not modelling any explicit temporal or spatial structure.
- Balanced accuracy for the MLP rises with horizon length, from 0.56 at the shortest horizon to 0.59 and then 0.61 at the two longer horizons, whereas CNN-LSTM balanced accuracy drifts down from 0.57 to 0.56 and 0.55 over the same horizons.
- The Self-Attention LSTM is statistically indistinguishable from the CNN-LSTM and MLP at the shortest horizon but degrades sharply at the two longer horizons.
- The plain Logistic Regression baseline is stable across horizons and even matches the CNN-LSTM at the longest horizon, though it is consistently unable to identify the upper return quantile well.
- The Shallow LSTM performs close to Logistic Regression at the two shorter horizons, but its performance collapses at the longest horizon, especially for the upper return quantile.
- All trained models clearly beat the Random and Naive baselines, whose Matthews Correlation Coefficient and Cohen's Kappa are both 0 by construction.
- Models were trained for 30 epochs with batches of 1024 samples of ten consecutive LOB snapshots, using the Adam optimizer with a learning rate of 0.001.

## Limitations

- The study is conducted on a single stock (INTC), described by the authors as a large-tick stock, which they note is known to be more predictable for machine-learning models than small-tick stocks; results may not transfer to small-tick names.
- The MLP is given the same historical window as the sequential models but does not itself encode sequential order, so its strong performance does not rule out that some sequential information is still being exploited implicitly by the other models.
- The authors state that the McNemar test was deliberately not used to compare models, relying only on the Bayesian correlated t-test.
- Reader note: the task predicts price-change-based horizons defined by counting non-zero returns rather than fixed real-time horizons, which the authors themselves flag as a simplification for future work.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[entities/antonio-briola|Antonio Briola]]
- [[entities/jeremy-turiel|Jeremy Turiel]]
- [[entities/tomaso-aste|Tomaso Aste]]

## Citation

Antonio Briola, Jeremy Turiel, Tomaso Aste (2020). Deep Learning Modelling of the Limit Order Book: A Comparative Perspective.

DOI: 10.2139/ssrn.3714230

Text ingested: `markdown_output/briola-2020-deep-learning-modeling-limit-order-book.md`, converted from `raw/ofi-event-clock/briola-2020-deep-learning-modeling-limit-order-book.pdf`.

Coverage of this summary: Read the whole markdown file end to end, including the introduction, related work, dataset description, all model descriptions, the training and test pipeline, the results tables, the discussion, and the conclusion.

Known problems with the input: Several equations (log-return definitions, quantile mapping, model architecture diagrams) were rendered by the PDF-to-markdown converter as omitted picture placeholders, so exact formula forms could not be independently verified beyond the surrounding prose and tables.
<!-- AUTHORED REGION END -->