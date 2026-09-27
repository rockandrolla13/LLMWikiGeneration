---
authors:
- Yufei Wu
- Mahmoud Mahfouz
- Daniele Magazzeni
- Manuela Veloso
content_hash: sha256:50daebc4001f2f55c1f3dea347a6169c435e9b0b94593b8872461ca47a2db11c
created: 2026-09-27 01:47:00+00:00
page_id: sources/wu-2022-towards-robust-representations-limit-orders-books
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/deep-learning-for-finance
- concepts/lstm-networks
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/feature-engineering
revision_id: 1
schema_version: 2
source_hash: sha256:2e3c65c767f29351999da36b6f8441f606deff73135c4108b57d27cd5dd4e450
source_path: markdown_output/wu-2022-towards-robust-representations-limit-orders-books.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- data-representation
- adversarial-robustness
- price-forecasting
- market-microstructure
- clock-event
- asset-equity
- harvest-relevant
title: Towards Robust Representations of Limit Orders Books for Deep Learning Models
updated: '2026-09-27T01:47:00Z'
uuid: 4bf1ca98-18b2-5e44-a016-4574a1e749f0
year: 2022
---

<!-- AUTHORED REGION START -->
# Towards Robust Representations of Limit Orders Books for Deep Learning Models

## Summary

The paper asks whether the limit order book (LOB) representation commonly fed into deep learning forecasting models is actually compatible with the assumptions those models make, and whether a different representation could be both more accurate and more robust. It contrasts the widely used compressed representation, which stores each price level as a (price, volume) pair ranked by depth, with a vector representation that instead stores volumes on a fixed price grid, and proposes two new schemes built on that grid: a moving-window representation and an accumulated market-depth representation, both centred on the mid-price.

To probe robustness, the authors design an adversarial perturbation in which minimum-size limit orders are added at previously empty price ticks beyond the best bid or ask, chosen so the mid-price itself never moves. In a worked example with a tick size of 0.01 and a minimum order size of 1, adding 4 orders like this can move the L1-norm distance of the compressed 20-dimensional representation by close to 400, while the equivalent vector representation moves by only 4 - showing that the compressed scheme amplifies small, valid market actions into large representation changes and can shift information out of the model's field of view entirely.

Using the FI-2010 limit order book benchmark (5 stocks from the Helsinki Stock Exchange, Level-II data over 10 trading days) and five forecasting models (linear, MLP, LSTM, DeepLOB and a temporal convolutional network), the moving-window and market-depth representations both outperformed the compressed representation without perturbation, and unlike the compressed representation, they showed almost no accuracy loss when the test data was perturbed. Under a perturbation applied to both sides of the book, DeepLOB - the strongest model on unperturbed data - suffered the largest degradation of any model tested.

The paper's contribution is bringing adversarial robustness testing to LOB input representations for the first time, arguing that a representation's compatibility with a model's architectural assumptions (for example, the spatial homogeneity CNNs assume) matters as much as its raw information content, and offering two concrete representations that satisfy this compatibility while also improving forecasting accuracy.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are LOB snapshots recorded after order-book events (placements, cancellations, executions) rather than fixed time intervals, using the 10 most recent snapshots as history for each input sample. The prediction target is the smoothed mid-price movement l_t, computed from the ratio between the current mid-price and the average of the next k mid-prices (the prediction horizon k), discretised into up/stationary/down classes using a threshold; the paper's own figure illustrates this construction for horizons of 10 and 100 events.

## Data

- **Asset class:** Equities
- **Instruments:** 5 stocks from the Helsinki Stock Exchange (the FI-2010 benchmark dataset)
- **Venue:** Helsinki Stock Exchange
- **Period:** 10 trading days total (from the FI-2010 dataset); the paper does not state how those days were split between training and testing
- **Granularity:** Level-II order book data, top 10 price levels per side, updated per event (order placement, execution, cancellation); each input sample uses the 10 most recent snapshots, giving an input dimension of 10 x 40 for the compressed representation and 10 x 41 for the moving-window and market-depth representations

## Features and Measures

- **Vector representation.** Encodes a limit order book snapshot as a fixed-length vector over price ticks near the mid-price, with a zero entry for every tick that has no orders, so distances between adjacent entries always equal the tick size.
- **Compressed representation.** Encodes a snapshot as a sequence of (price, volume) pairs, one per occupied price level on each side, ranked by depth from the best price; this is the representation most commonly used in the LOB deep-learning literature and in the FI-2010 benchmark.
- **Moving-window representation.** A 2D matrix of ask/bid volumes over a fixed-width band of price ticks centred on the current mid-price, tracked across the most recent LOB snapshots, so each matrix cell keeps the same price meaning through time.
- **Market-depth representation.** An accumulated (cumulative-volume) version of the moving-window representation, where each entry holds the total volume up to that price level on its side, reflecting the book's capacity to absorb order flow without a large price move.

## Method

Five forecasting models are compared: a multi-class logistic regression, a multi-layer perceptron with two hidden layers of 100 and 50 ReLU neurons, a single-layer LSTM with 20 units, DeepLOB (a CNN + inception module + LSTM architecture built specifically for the compressed representation), and a temporal convolutional network (TCN) with 3 causal convolutional layers of 32 channels each, used with the paper's own moving-window and market-depth representations since DeepLOB is not compatible with them. Models are trained once on the unperturbed FI-2010 training data and then evaluated on four test variants: no perturbation, and perturbation applied to the ask side only, the bid side only, or both sides. Performance is scored with (unbalanced) accuracy and an unweighted, per-class-averaged F-score, each averaged over 5 runs with different random seeds and reported with standard deviations.

## Results

- Across representations, model performance ranked consistently as deep models (DeepLOB, TCN) > LSTM > MLP > linear.
- Using the compressed representation with no perturbation, accuracy/F-score were 52.98%/38.50% for the linear model, 60.14%/53.96% for MLP, 70.74%/68.45% for LSTM, and 77.30%/77.23% for DeepLOB.
- Replacing the compressed representation with the paper's proposed representations raised unperturbed forecasting performance: about 7% for the linear model (moving-window vs. compressed), about 11% for MLP (market-depth vs. compressed), and about 7% for LSTM (market-depth vs. compressed).
- The market-depth representation gave the best performance of all schemes tested; LSTM combined with market-depth came close to matching the far more complex DeepLOB model's unperturbed performance.
- Under perturbation applied to both sides of the book, accuracy fell by about 11% for MLP, about 12% for LSTM, and over 25% for DeepLOB using the compressed representation, while the moving-window and market-depth representations showed no comparable performance decay under any perturbation condition tested.
- The text reports DeepLOB's accuracy and F-score under the 'both-sides' perturbation as 47.5% and 22.2% respectively - worse than the simplest logistic-regression model - though this differs from the 51.35%/39.59% shown in the paper's own results table for the same condition.
- Under perturbation, DeepLOB's confusion matrix showed it misclassifying almost all samples into the 'stationary' class.

## Limitations

- Authors state future work should extend robustness testing to more market-related tasks, including reinforcement learning settings, beyond the price-forecasting task studied here.
- Reader note: robustness is evaluated only against one hand-designed, mid-price-preserving perturbation scheme on a single benchmark dataset (FI-2010, 5 equities), so it is unclear whether the conclusions extend to other kinds of market disturbance or other markets.
- Reader note: DeepLOB could only be tested with the compressed representation because it was built specifically for that input, so the cross-representation comparison for that model is incomplete.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]

## Citation

Yufei Wu, Mahmoud Mahfouz, Daniele Magazzeni, Manuela Veloso (2022). Towards Robust Representations of Limit Orders Books for Deep Learning Models.

DOI: 10.2139/ssrn.4295991

Text ingested: `markdown_output/wu-2022-towards-robust-representations-limit-orders-books.md`, converted from `raw/ofi-event-clock/wu-2022-towards-robust-representations-limit-orders-books.pdf`.

Coverage of this summary: Read the full paper markdown end to end: introduction, related work, both current representation schemes, the adversarial perturbation analysis, the desiderata section, the two proposed representations, experimental setup, and results/conclusion.

Known problems with the input: No publication year is printed anywhere in the paper text; the job file's year_hint (2022) was used instead; No journal or conference name is printed in the paper text (only J.P. Morgan AI Research author affiliations), so venue is left blank; The paper's own prose states DeepLOB's 'both-sides' perturbation performance as 47.5% accuracy / 22.2% F-score, which conflicts with the 51.35%/39.59% given in Table 1 for the same cell; both numbers are reported as printed rather than reconciled.
<!-- AUTHORED REGION END -->