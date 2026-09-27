---
authors:
- Timothée Fabre
- Damien Challet
content_hash: sha256:b5333d0b15f326f21a9a6b9bce81fbeee0be778329bc16dbe0e1268dd5a7069d
created: 2026-09-27 01:47:00+00:00
page_id: sources/fabre-2025-learning-spoofability-limit-order-books-interpretable
page_type: source
related:
- concepts/event-clock
- concepts/limit-order-book
- concepts/hawkes-processes
- concepts/order-flow
- concepts/order-flow-imbalance
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/high-frequency-trading
revision_id: 1
schema_version: 2
source_hash: sha256:7ef062acaa7f3877a1c98ef8c97a68253935b68c264121ab6d3026c0bf3bbda8
source_path: markdown_output/fabre-2025-learning-spoofability-limit-order-books-interpretable.md
source_type: paper
tags:
- spoofing
- limit-order-book
- hawkes-processes
- cryptocurrency
- market-manipulation
- order-flow-imbalance
- clock-event
- asset-crypto
- harvest-relevant
title: Learning the Spoofability of Limit Order Books With Interpretable Probabilistic
  Neural Networks
updated: '2026-09-27T01:47:00Z'
uuid: be93599c-34b1-5815-b7f3-f831621336c0
year: 2025
---

<!-- AUTHORED REGION START -->
# Learning the Spoofability of Limit Order Books With Interpretable Probabilistic Neural Networks

## Summary

The paper asks whether real-time spoofing (posting a large, non-genuine order on one side of the book to move the price before cancelling it) can be detected using a data-driven model of how newly inserted limit orders affect the future price-move distribution, in particular accounting for how far from the best price an order is placed rather than treating only top-of-book imbalance as informative. The approach constructs order flow variables inspired by the self-exciting (Hawkes) part of order book intensity, separately for limit and marketable orders, each summed over several time scales and (for limit orders) several distance-from-mid scales; these features and the bid-ask spread are fed into a small feed-forward neural network trained to output the parameters of a (skewed) Gaussian distribution for the mid-price move over a fixed short horizon.

Using this fitted conditional distribution, the authors study how the predicted mean, standard deviation and a risk-adjusted (Sharpe-like) measure of the price move respond to a hypothetical new order's size and distance from the best price, and use the same distribution to write a spoofer's expected trading cost as a function of order size and placement distance for a small genuine order and a large manipulative one. Comparing the expected cost of spoofing against not spoofing yields a live detection rule. The main finding is that price impact from a newly placed order decays with distance from the best price but remains statistically significant well beyond the top of book, so detectors that only look at top-of-book imbalance miss most of the spoofing activity the model finds; applying the rule to real BTC-USD order flow, a substantial share of large orders were found capable of profitably spoofing the market, and orders flagged as suspicious differ systematically from normal orders in size, placement distance and subsequent price response. What is new is the explicit dependence of the order flow features on placement distance (rather than only top-of-book imbalance), the use of a probabilistic (distributional) rather than point-prediction network, and a cost-function-based detection rule fast enough to run live.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are keyed to the insertion of each limit order in Level-3 (market-by-event) data; order flow features are exponentially-weighted (Hawkes-style) sums of past limit- and marketable-order arrivals computed at that event, spanning several time scales and, for limit orders, several distance-from-mid scales. The prediction target is the mid-price move over a fixed trading horizon of 1 second following the order's insertion.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC-USD and ETH-USD spot pairs
- **Venue:** Coinbase (centralised cryptocurrency exchange)
- **Period:** Neural network training/validation data from 2022-12-01 to 2022-12-03 (2,000,000 orders); the live spoofing-detection application covers 2024-12-04 to 2024-12-07 (88,327,661 orders).
- **Granularity:** Level-3 market-by-event data: every limit order insertion with its timestamp, size and price; orders posted more than about 20% of the mid price away, or smaller than 50 USD, are filtered out before feature construction.

## Features and Measures

- **Hawkes-inspired limit order flow variable.** An exponentially time-weighted sum of past limit-order arrivals, with the weight of each past order also depending on its size and its distance of placement from the mid price, computed separately per time scale, per distance scale, and per side of the book.
- **Hawkes-inspired marketable order flow variable.** An exponentially time-weighted sum of past marketable (trade-triggering) order arrivals, with weight depending on elapsed time and order size but not distance, computed per time scale and per side.
- **limit order flow imbalance.** A weighted combination of the limit order flow variables across time and distance scales that summarises net buy versus sell pressure coming from newly posted limit orders.
- **market order flow imbalance.** The analogous weighted combination built from the marketable order flow variables, summarising net buy versus sell pressure from executed trades.
- **bid-ask spread feature.** The current bid-ask spread, included directly as a model input and also used on its own to check that the model reproduces the known positive spread-volatility relationship.
- **risk-adjusted price-move statistic.** The model's predicted mean price move divided by its predicted standard deviation, used as a Sharpe-like summary of the expected impact of an order once its size and distance are accounted for.

## Method

The order flow features (24 limit-order features plus 6 marketable-order features plus the spread, totalling 31 variables in the single-asset case, 62 in the two-asset case) are pre-processed with a per-feature Box-Cox transform, chosen by maximising the transformed feature's Gaussian log-likelihood on the training set, followed by z-score standardisation using training-set statistics. These inputs feed a feed-forward neural network with one hidden layer of 64 ReLU units, whose output is mapped to the parameters of either a univariate skewed Gaussian (mean, standard deviation, skew) or, in the two-asset case, a bivariate Gaussian describing the joint mid-price moves. The network is trained by maximum likelihood (negative log-likelihood loss) with the Adam optimiser, using a training set of 1,000,000 orders and a chronologically later validation set of 1,000,000 orders drawn from a pool of 2,000,000 orders, for up to 1,000 epochs with early stopping after 100 epochs without validation improvement.

The fitted network is then used two ways: first, to compute partial-dependence plots of the predicted price-move mean, standard deviation and risk-adjusted statistic against the bid-ask spread, the order flow imbalance features, and the size and distance of a hypothetical new limit order (assessed with a Student's t-statistic over repeated draws); second, to build a spoofing agent's expected trading cost as a function of the size and distance of a small genuine order and a large manipulative order, under assumptions that orders are either fully filled or not filled at all, that execution follows a first-passage-time rule tied to the fair price crossing the order's limit price, and that any unwanted inventory from a filled manipulative order is liquidated with a marketable order at the trading horizon. An order is flagged as suspicious in the resulting live detection rule whenever this expected gain from spoofing, versus not spoofing, is positive.

## Results

- The predicted standard deviation of the price move increases roughly linearly with the bid-ask spread across bins spanning 0.1 bp to 10 bps, reproducing the known empirical spread-volatility relationship.
- A larger limit order flow imbalance is associated with a bigger expected price move in the same direction, while a larger market order flow imbalance is associated with a smaller expected price move, consistent with a liquidity-pressure interpretation.
- Price impact grows with an inserted order's size and shrinks with its posting distance from the best price, but remains statistically significant for orders placed several basis points away, not only at the top of the book.
- Orders of size at least 50,000 USD placed within a few basis points of the best price were found to generate the largest impact on the predicted risk-adjusted price move.
- In the cross-asset test, orders posted in the BTC-USD book had a much more statistically significant effect on the ETH-USD Sharpe-like measure than the reverse, suggesting BTC-based spoofing of ETH is easier than the converse.
- Applying the detection rule to 88,327,661 orders posted between 4 and 7 December 2024, of which 8,601,227 were large (size at least 4,500 USD), about 31% of large orders were flagged as capable of profitably spoofing the market, versus about 7% of all orders.
- Suspicious orders were rarely placed at the very top of the book (0% of large suspicious orders and 0.13% of all suspicious orders), compared with 4.20% of large normal orders and 10.14% of all normal orders quoted at the top of book.
- Suspicious orders were on average larger, placed further from the best price, and followed by larger price moves than normal orders (e.g. large suspicious orders averaged 15,980 USD in size versus 2,042 USD for all normal orders), and several examples showed layering behaviour.

## Limitations

- The bona fide order size behind a suspected spoof, and trader identity, cannot be directly observed, so the rule can only flag suspicious activity rather than prove manipulation with certainty.
- The cross-asset and cross-venue extensions of the spoofing cost framework are derived analytically but not applied to detection, because the authors say reliable cross-asset detection needs anonymised trader identifiers that were not available.
- The spoofing cost model assumes orders are either completely filled or not filled at all; the authors note this is restrictive for the large manipulative order and say partial fills are left for future extension.
- Reader note: the empirical detection results are limited to two cryptocurrency pairs on a single exchange (Coinbase); the paper does not test the method on regulated equity or bond markets.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/hawkes-processes|hawkes processes]]
- [[concepts/order-flow|order flow]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]

## Citation

Timothée Fabre, Damien Challet (2025). Learning the Spoofability of Limit Order Books With Interpretable Probabilistic Neural Networks.

DOI: 10.2139/ssrn.5230047

Text ingested: `markdown_output/fabre-2025-learning-spoofability-limit-order-books-interpretable.md`, converted from `raw/ofi-event-clock/fabre-2025-learning-spoofability-limit-order-books-interpretable.pdf`.

Coverage of this summary: Read the full paper: abstract, introduction and literature review, the order flow feature construction, the probabilistic neural network specification, training and normalisation, the partial-dependence/microstructure analysis, the spoofing cost-function framework, the single- and cross-asset price-response results, the suspicious-order identification results and Table 1 descriptive statistics, and the conclusion. The appendix's closed-form cost formulas were noted but not transcribed.

Known problems with the input: Most of the paper's equations are rendered as omitted images in the converted markdown, so exact functional forms of the Hawkes kernels, the loss function, and the cost-function formulas are described here from surrounding prose rather than the equations themselves; Several large numbers in the source markdown have their thousands-separating commas split by italics markup (e.g. '4 _,_ 500'); these are reported here in their evident unbroken form (e.g. 4,500), consistent with how the extraction instructions treat the converter's similar splitting of decimal points.
<!-- AUTHORED REGION END -->