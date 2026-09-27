---
authors:
- Justin A. Sirignano
content_hash: sha256:8acb145d195a7f2fc3037c6d1d56f87042f2f9af251e23e926b88768f68ad4f8
created: 2026-09-27 01:47:00+00:00
page_id: sources/sirignano-2018-deep-learning-limit-order-books
page_type: source
related:
- concepts/sampling-clocks
- concepts/limit-order-book
- concepts/order-imbalance
- concepts/deep-learning-for-finance
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/order-flow-prediction
- concepts/liquidity-risk
revision_id: 1
schema_version: 2
source_hash: sha256:c64668ad65bc819c603a4d9325988088ca9f3f6e2be235d084541d1f40220daa
source_path: markdown_output/sirignano-2018-deep-learning-limit-order-books.md
source_type: paper
tags:
- limit-order-book
- deep-learning
- neural-networks
- market-microstructure
- risk-management
- order-book-imbalance
- high-frequency-data
- equities
- clock-compares
- asset-equity
- harvest-relevant
title: Deep Learning for Limit Order Books
updated: '2026-09-27T01:47:00Z'
uuid: 27c9b795-023c-565d-8cd0-3db66dad22b0
year: 2016
---

<!-- AUTHORED REGION START -->
# Deep Learning for Limit Order Books

## Summary

The paper asks how well the future joint distribution of the best bid and best ask prices can be predicted from the current state of a stock's limit order book, rather than just predicting the direction of the next move. It argues that modelling the full distribution, not only its mean, matters for risk applications such as value-at-risk and market-making risk, because the joint behaviour of the bid and ask (not just the mid-price) determines exposure. The author first shows, through per-stock logistic regressions, that the probability a price crosses a given book level depends mostly on the order size sitting at that exact level rather than on sizes elsewhere in the book, a property called local spatial structure. A new architecture, called the spatial neural network, is designed to exploit this: instead of treating every possible outcome as an unrelated class, it models each outcome using only the inputs local to it, which lets it generalise smoothly over nearby price levels, cover the whole real line rather than a truncated grid, and train faster than a standard feed-forward network. The model is compared against a naive empirical baseline, a logistic regression with nonlinear order-book-imbalance features, and a standard deep neural network. What is new is both the architecture itself and a formal well-posedness argument for when such a spatial model avoids leaking probability mass to infinity, together with a large-scale empirical demonstration on hundreds of individually-trained stock models. The main finding is that both neural network types clearly beat the simpler baselines, and the spatial neural network in turn beats the standard neural network, especially in the tails of the distribution and when a price actually moves, which the paper argues is the setting most relevant to trading and risk management.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

Two prediction setups are compared. Case 1 uses a fixed calendar interval: the state of the book at time t is used to predict the best bid/ask prices exactly 1 second later, regardless of whether a change occurs. Case 2 uses an event/next-move clock: predictions are made for the joint best bid/ask prices at the next time either price changes, so the horizon between observations is random and can range from a fraction of a second to many seconds. Case 2 conditions on a price change occurring, while Case 1 usually does not see one, since the best ask changes only 5-15% of the time inside a 1-second window for typical stocks.

## Data

- **Asset class:** Equities
- **Instruments:** 489 U.S. stocks, primarily drawn from the S&P 500 and NASDAQ-100
- **Venue:** NASDAQ stock exchange (Level III order book feed)
- **Period:** January 1, 2014 to August 31, 2015; training/validation drawn from January 1, 2014 to May 31, 2015, test set is June 1, 2015 to August 31, 2015
- **Granularity:** Event-by-event limit order book state (submissions, cancellations, and transactions) with nanosecond timestamps; the first 100 nonzero price levels (50 bid, 50 ask) are recorded for each stock, giving roughly 50 terabytes of raw data

## Features and Measures

- **size at level k.** The number of shares available to buy or sell in the limit order book at a price k levels away from the best ask (or best bid), used as the raw input describing book depth.
- **order book imbalance.** A nonlinear function of the bid and ask sizes at a given level, computed as the bid size minus the ask size divided by their sum, used as an extra nonlinear input to the logistic regression baseline.
- **coefficient ratio.** A per-stock diagnostic built from fitted logistic-regression coefficients that compares how strongly the price move depends on the size at one specific level versus the sizes at nearby levels, used to test for local dependence.

## Method

The paper frames predicting the future best ask and best bid prices as predicting how many price levels each moves, i.e. modelling a joint distribution on a two-dimensional integer grid. A standard feed-forward neural network (4 layers, tanh units, 250 neurons per hidden layer) is compared against the new spatial neural network (also 4 layers and tanh units, but only 50 neurons per hidden layer), a logistic regression that includes order-book-imbalance features, and a naive empirical baseline equal to the training set's unconditional distribution. The spatial neural network's key design choice is to model the conditional probability of each candidate outcome using a function of only the current price and the inputs local to that outcome, rather than a single function that must be evaluated at every possible outcome; a dimension-splitting trick is applied to all models so the joint ask/bid distribution can be built from lower-dimensional pieces. Models are trained per stock, separately for each of the 489 stocks, using dropout, inter-layer batch normalization, the RMSProp optimizer, an adaptive learning rate, an l2 penalty, and early stopping on a validation set, for 75 epochs. Training and testing were run on a cluster of 50 GPUs with data pre-processing parallelized across 150 vCPUs, because the roughly 50-terabyte raw dataset made training computationally demanding. Performance is judged mainly by out-of-sample cross-entropy error (equivalent to negative log-likelihood) on the held-out test period, with accuracy and top-k accuracy (whether the true outcome is among the model's k most likely predictions) reported as a more interpretable secondary metric, including separately in the upper tail of the best-ask distribution.

## Results

- Both neural network types produced lower out-of-sample error than logistic regression and the naive empirical baseline for almost all 489 stocks tested, in both the fixed 1-second case and the next-price-move case.
- The spatial neural network had lower joint-distribution error than the standard neural network on 458 of 489 stocks in the fixed 1-second case and on 473 of 489 stocks in the next-price-move case.
- Averaged across all 489 stocks, the spatial neural network cut the joint-distribution error by about 0.6% relative to the standard neural network at the 1-second horizon, rising to about 3.5% at the next price move.
- The neural networks had roughly 10% lower joint-distribution error than logistic regression at the 1-second horizon and about 20% lower error at the next price move.
- In the upper tail of the best-ask distribution (conditional on the ask increasing), top-1 accuracy reached about 70.98% for the spatial neural network versus 69.90% for the standard neural network, 66.42% for logistic regression, and 62.04% for the naive model.
- The spatial neural network's advantage over the standard network in the tail grew for stocks whose best-ask price changes have a larger standard deviation, matching the earlier statistical evidence for local dependence.
- On Amazon, the spatial neural network reached the standard neural network's lowest error in about 90 seconds of training, versus about 1700 seconds for the standard network.

## Limitations

- For a typical stock the best ask price changes only 5-15% of the time within a 1-second window, so most Case 1 samples give the tested models little to distinguish, which the authors say is why the spatial network's overall Case 1 gain is modest even though it is large conditional on a move.
- To keep the comparison feasible, the modelled price-move range is truncated to a finite grid for the baseline and standard-network models, so results describe performance on that truncated range rather than the untruncated real line the spatial network can in principle cover.
- Every model is trained separately per stock with a fresh random initialization, so the paper does not test whether a single model can generalize across stocks.
- Reader note: all data comes from a single exchange feed (NASDAQ) over one 20-month window (January 1, 2014 to August 31, 2015), so it is unclear whether the results transfer to other venues, time periods, or market regimes.
- Reader note: the evaluation is purely statistical (cross-entropy error and accuracy); no trading strategy, transaction costs, or execution outcomes are backtested.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow-prediction|order flow prediction]]
- [[concepts/liquidity-risk|liquidity risk]]

## Citation

Justin A. Sirignano (2016). Deep Learning for Limit Order Books.

DOI: 10.1080/14697688.2018.1546053

Text ingested: `markdown_output/sirignano-2018-deep-learning-limit-order-books.md`, converted from `raw/ofi-event-clock/sirignano-2018-deep-learning-limit-order-books.pdf`.

Coverage of this summary: Read the abstract, introduction, related-literature and neural-network-advantages subsections, the full data description (Section 2) including the spread/joint-distribution motivation, the local-spatial-structure evidence (Section 3), the neural network architecture derivation (Section 4, including the spatial neural network and the well-posedness theorem statement), the training and computational setup (Section 5), the complete out-of-sample results (Section 6: Case 1, Case 2, tail performance, and error-versus-computational-cost), and the conclusion (Section 7); skimmed but did not fully verify the technical well-posedness proofs in Appendices B and C, and did not read Appendix D.

Known problems with the input: The paper's own printed date is May 16, 2016, which differs from the job file's year_hint of 2018; the printed date was used for the year field since the document states it explicitly; Several equations in the converted markdown are rendered as picture placeholders rather than text, so exact equation forms are described only loosely from surrounding prose and were not independently verified.
<!-- AUTHORED REGION END -->