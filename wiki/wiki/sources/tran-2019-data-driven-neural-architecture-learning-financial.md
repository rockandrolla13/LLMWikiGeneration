---
authors:
- Dat Thanh Tran
- Juho Kanniainen
- Moncef Gabbouj
- Alexandros Iosifidis
content_hash: sha256:1b301910fa807010cdd992e546666b15b3f540802f6f311204e5738f8879f9c8
created: 2026-09-27 01:47:00+00:00
page_id: sources/tran-2019-data-driven-neural-architecture-learning-financial
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/feature-engineering
- entities/dat-thanh-tran
- entities/juho-kanniainen
- entities/moncef-gabbouj
- entities/alexandros-iosifidis
revision_id: 1
schema_version: 2
source_hash: sha256:31a1ba22c427e505f7a7e6fd1b52cc4052d1255ca177619538aebb7394d09658
source_path: markdown_output/tran-2019-data-driven-neural-architecture-learning-financial.md
source_type: paper
tags:
- limit-order-book
- mid-price-prediction
- neural-architecture-search
- class-imbalance
- high-frequency-trading
- deep-learning
- clock-event
- asset-equity
- harvest-relevant
title: Data-driven Neural Architecture Learning for Financial Time-series Forecasting
updated: '2026-09-27T01:47:00Z'
uuid: 1a69ede6-ec0f-5bcf-90aa-3c285fd8069e
year: 2019
---

<!-- AUTHORED REGION START -->
# Data-driven Neural Architecture Learning for Financial Time-series Forecasting

## Summary

Financial time-series forecasting is hard because real data is nonstationary and nonlinear, and hand-designed neural network topologies impose a fixed functional form that may not suit every problem. The paper asks whether a network architecture can instead be learned directly from data for the specific task of predicting limit order book (LOB) mid-price movement, and whether such a method can also cope with the imbalance between 'increasing', 'decreasing' and 'stationary' movement classes that is common in this kind of data.

The approach adapts an existing progressive-learning algorithm, HeMLGOP, which builds a heterogeneous multilayer network out of Generalized Operational Perceptron (GOP) neurons. Each GOP is composed of a nodal, a pooling and an activation operation chosen from a predefined operator set, giving it a richer range of nonlinear transformations than a standard perceptron. Blocks of GOPs are added one at a time; for each new block, a randomized search picks the best operator set and an output layer is solved as a re-weighted least-squares problem, followed by backpropagation fine-tuning. The paper's own modification scales the squared-error contribution of each training sample inversely to how common its movement class is, so the network is not biased toward the majority class.

On the FI-2010 limit order book benchmark, evaluated with a 9-fold anchored, day-based cross-validation split, HeMLGOP obtained the best average F1 score among all compared methods. It beat the next-best vector-input method by close to 8 percentage points of F1, and still beat the best tensor-based methods (which use far more historical order-book information) by close to 3 percentage points, while HeMLGOP itself used only the 10 most recent order events.

What is new relative to prior progressive-learning work is the combination of automatic, data-driven architecture search (via GOPs) with an explicit class-imbalance correction in the training objective, applied to the LOB mid-price prediction problem.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are formed per block of the 10 most recent limit order book events, each summarized as a 144-dimensional feature vector. The prediction target is the direction of mid-price movement (decreasing, stationary, increasing) over a horizon defined in order-event counts; the FI-2010 dataset provides labels for horizons H = 10, 20, 30, 50 and 100 future order events, and this paper reports results for H = 10.

## Data

- **Asset class:** Equities
- **Instruments:** 5 Finnish stocks (the FI-2010 limit order book dataset)
- **Venue:** Nasdaq Nordic
- **Period:** 10 working days
- **Granularity:** order-book event level; 144-dimensional feature vectors computed per block of 10 order events, more than 4 million limit orders in total

## Features and Measures

- **Generalized Operational Perceptron (GOP).** A neuron model that replaces the standard perceptron with a sequence of nodal, pooling and activation operators chosen from a predefined operator set, giving each neuron a wider range of possible nonlinear transformations.
- **HeMLGOP architecture.** A heterogeneous multilayer network built by progressively adding blocks of GOP neurons (allowing different operator sets within the same layer), stopping each layer's growth and the whole network's growth once loss improvement falls below a threshold.
- **class-reweighted output layer.** The output layer's regularized least-squares solution scales each training sample's squared-error term by a weight inversely proportional to how frequent its movement class is, to counter class imbalance in the mid-price movement labels.

## Method

The network is grown one block of GOP neurons at a time. For a new block, a randomized search assigns weights and evaluates each candidate operator set, after which the output layer weights are recomputed by solving a regularized, class-reweighted least-squares problem; the best-performing operator set is kept and the block's weights (together with the output layer) are then fine-tuned with several hundred epochs of backpropagation. A new block is added to the current hidden layer while performance keeps improving beyond a given threshold; once growth in a layer saturates, the layer's contribution to overall performance is checked against the same kind of threshold to decide whether to start a new layer or stop growing and fine-tune the whole network. HeMLGOP is compared against other progressive-learning methods (S-ELM, BLS, PLN) that take the same 10-event vector input, against simpler baselines (Ridge Regression, a single-layer feedforward network, LDA), and against tensor-based methods (MDA, MCSDA, MTR, WMTR, BoF, N-BoF) that use at least 100 past order events. Because the movement classes are imbalanced, average F1 score is used as the primary metric, alongside accuracy, precision and recall, averaged over the dataset's 9-fold anchored (day-based) cross-validation splits.

## Results

- HeMLGOP obtained accuracy 83.06%, precision 48.57%, recall 50.67% and F1 49.43% on FI-2010 at horizon H=10.
- HeMLGOP achieved the highest F1 score among all compared methods, vector-based or tensor-based.
- HeMLGOP's F1 was nearly 8 percentage points higher than the second-best vector-input method, N-BoF (41.63% F1).
- HeMLGOP's F1 was almost 3 percentage points higher than the best tensor-based method, WMTR (47.87% F1), despite tensor methods using at least 100 past order events versus HeMLGOP's 10.
- Other progressive-learning baselines (S-ELM, BLS, PLN) reached higher raw accuracy (around 87-89%) but much lower recall, illustrating that accuracy is a misleading metric on this imbalanced task.

## Limitations

- Evaluated on a single benchmark (FI-2010) covering only 5 Finnish stocks over 10 working days.
- Only prediction horizon H=10 is reported in the experiments, though the dataset provides labels for several horizons.
- Reader note: no comparison against more recent deep sequence models (e.g. CNN- or attention-based LOB predictors), even though such work is cited in the introduction.
- Reader note: mathematical details of the GOP operations and the loss/termination criteria are given only as equations rendered as images in the source, so exact functional forms could not be checked here.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/feature-engineering|feature engineering]]
- [[entities/dat-thanh-tran|Dat Thanh Tran]]
- [[entities/juho-kanniainen|Juho Kanniainen]]
- [[entities/moncef-gabbouj|Moncef Gabbouj]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]

## Citation

Dat Thanh Tran, Juho Kanniainen, Moncef Gabbouj, Alexandros Iosifidis (2019). Data-driven Neural Architecture Learning for Financial Time-series Forecasting.

DOI: 10.48550/arxiv.1903.06751

Text ingested: `markdown_output/tran-2019-data-driven-neural-architecture-learning-financial.md`, converted from `raw/ofi-event-clock/tran-2019-data-driven-neural-architecture-learning-financial.pdf`.

Coverage of this summary: Read the full markdown text end to end, from title and abstract through the method, experiments and conclusion, to the reference list.

Known problems with the input: Paper prints no explicit publication year in the extracted text; year taken from job file metadata; Several equations (GOP operations, termination criteria, output-layer solution) are rendered as omitted images in the converted markdown, so their exact forms are not verifiable from this file.
<!-- AUTHORED REGION END -->