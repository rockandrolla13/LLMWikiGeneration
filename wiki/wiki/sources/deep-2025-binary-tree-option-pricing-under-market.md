---
authors:
- Akash Deep
- Chris Monico
- W. Brent Lindquist
- Svetlozar T. Rachev
- Frank J. Fabozzi
content_hash: sha256:b3b4572a1fc7de5264ff7640143bac33a1e4d6b5b8d7d8fde116a6a5c68b03ec
created: 2026-09-27 01:47:00+00:00
page_id: sources/deep-2025-binary-tree-option-pricing-under-market
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/order-flow
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/feature-engineering
- concepts/bid-ask-spread
- concepts/informed-trading
revision_id: 1
schema_version: 2
source_hash: sha256:81f52789e2d31f6a8f06c0d7eb1209b430a5cfa6883743970bbb7bbf7c206c56
source_path: markdown_output/deep-2025-binary-tree-option-pricing-under-market.md
source_type: paper
tags:
- option-pricing
- random-forest
- market-microstructure
- binomial-tree
- order-flow-imbalance
- no-arbitrage
- clock-calendar
- asset-equity
- harvest-relevant
title: 'Binary Tree Option Pricing Under Market Microstructure Effects: A Random Forest
  Approach'
updated: '2026-09-27T01:47:00Z'
uuid: 66ec3114-95c6-56a4-8702-0fc49fb3b1ae
year: 2025
---

<!-- AUTHORED REGION START -->
# Binary Tree Option Pricing Under Market Microstructure Effects: A Random Forest Approach

## Summary

The paper asks whether market microstructure effects such as bid-ask spreads, discrete price changes and serial correlation in returns can be built directly into a discrete-time option-pricing tree, instead of being assumed away as in the Black-Scholes framework.

The approach extends the classical Cox-Ross-Rubinstein binomial tree so that every node carries a market 'state' (recent returns, spread measures, volume and order-flow measures, time-of-day) in addition to price. A Random Forest classifier is trained on historical SPY minute data to output the physical (real-world) probability of an up-move for a given state, and separate state-dependent up/down price factors are fitted to match each state's estimated return mean and variance. Because these Random Forest probabilities are not automatically arbitrage-free, the paper applies a Minimal Martingale Measure adjustment -- the risk-neutral probability closest (by Kullback-Leibler divergence) to the physical one that still satisfies the no-arbitrage, discounted-martingale condition -- and prices options on the resulting tree by standard backward induction.

The Random Forest classifies the direction of the next minute's return with high accuracy, with order flow imbalance as the single most important input feature. Physical and risk-neutral probabilities differ substantially across the calibrated market states, which the authors interpret as evidence of a state-dependent risk premium, and the resulting no-arbitrage option price differs meaningfully from a Black-Scholes benchmark.

The paper is explicit that this is a proof-of-concept rather than a deployable pricing engine: correcting a time-scaling error in the initial implementation was necessary to obtain a realistic price, and the tree's non-recombining, exponentially growing node count currently limits the method to short-dated options with coarse time steps.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The underlying data are 1-minute OHLCV bars of SPY (46,655 observations, January-June 2025); the Random Forest predicts the direction of the next minute's return from lagged returns, spread, volume and order-flow-imbalance features. This per-minute prediction is then mapped onto a much coarser option-pricing tree, where each of the tree's 10 steps represents about 3 days for a 30-day option, after applying a square-root-of-time scaling correction to the minute-level factors.

## Data

- **Asset class:** Equities
- **Instruments:** SPDR S&P 500 ETF (SPY)
- **Venue:** not stated
- **Period:** January 2, 2025 to June 25, 2025
- **Granularity:** 1-minute bars (open, high, low, close, volume, tick count)

## Features and Measures

- **Order flow imbalance (OFI) proxy.** A signed-volume measure accumulated over a 5-minute window, used to capture the direction and intensity of order flow; it is the single most important Random Forest feature.
- **Spread proxy.** A liquidity/transaction-cost measure computed from the high-low range divided by the close price for the minute, together with its lag and change.
- **State-dependent transition probability.** The Random Forest's predicted probability that the next price move is up, computed as a function of the current feature vector (returns, spread, volume, order flow, time-of-day) rather than a single fixed value.
- **Minimal Martingale Measure (MMM) adjustment.** A transformation of the Random Forest's physical up-move probability into a risk-neutral probability by minimizing the Kullback-Leibler divergence from the physical measure subject to the no-arbitrage (discounted martingale) condition.
- **State-dependent up/down factors u(s), d(s).** Per-state price movement factors solved so the discrete tree matches the estimated conditional mean and variance of returns for that market state, rather than using one constant volatility for the whole tree.

## Method

The paper first reviews the standard Cox-Ross-Rubinstein binomial tree, then extends it so each node carries a market state built from lagged returns, spread, volume/order-flow measures and time features in addition to price. A Random Forest classifier is trained on this feature set from historical SPY minute bars to output a physical probability of an up-move for each state, while up and down factors are separately fitted per state by matching the conditional first and second moments implied by that state. Because the resulting physical probabilities need not satisfy the no-arbitrage martingale condition, the paper applies a constrained Minimal Martingale Measure optimization to obtain risk-neutral probabilities for each of a fixed number of pre-calibrated market states. The calibrated tree is then used to price a European call by standard backward induction. Model quality is judged by AUC, accuracy, precision, recall and F1 on held-out and cross-validated data, and pricing quality is judged by comparing the resulting option price to a Black-Scholes benchmark.

## Results

- The Random Forest predicted the direction of the next minute's SPY return with an AUC of 0.8825 and a balanced accuracy of 0.7968, far above a random classifier.
- Order flow imbalance was the most important feature (43.2% importance); lagged returns collectively contributed 31.5% importance, and volume-related features together contributed 14.1%.
- Cross-validation gave a mean AUC of 0.8747 with a standard deviation of 0.0100 (range 0.8678 to 0.8792), and feature-importance rankings stayed correlated above 0.95 across sub-periods.
- Across 20 calibrated market states, physical and risk-neutral (MMM) up-move probabilities differed by an average of 0.217 (absolute difference), with a correlation of 0.634 between the two sets of probabilities.
- State-dependent implied volatility ranged from 16.2% to 70.7% annualized across the 20 states, indicating volatility clustering tied to microstructure conditions rather than just price level.
- A 30-day, at-the-money SPY call priced on the 10-step microstructure-enhanced tree came out at $15.41, 13.79% below the $17.87 Black-Scholes benchmark price, after correcting an initial time-scaling error that had produced an unrealistic price of $0.38.
- Building the 10-step tree (2,047 nodes) took 87.31 seconds, while pricing an option on the already-built tree took 0.004 seconds, showing tree construction rather than pricing is the computational bottleneck.

## Limitations

- The tree is non-recombining, so the number of nodes grows exponentially with the number of time steps; the authors state this limits practical use to short-dated options with coarse (multi-day) time steps.
- Tree nodes are mapped to only 20 pre-calibrated market states based on the Random Forest's probability alone rather than the full feature vector, which the authors say loses microstructure detail.
- The empirical analysis covers a single six-month sample (SPY, January-June 2025) under relatively stable market conditions; behaviour during market stress or regime change was not tested.
- Reader note: results rely on a single underlying (SPY) and a single option (a 30-day at-the-money call), so the size and even the sign of the Black-Scholes gap may not generalize to other strikes, maturities or assets.

## Related

- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-flow|order flow]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/informed-trading|informed trading]]

## Citation

Akash Deep, Chris Monico, W. Brent Lindquist, Svetlozar T. Rachev, Frank J. Fabozzi (2025). Binary Tree Option Pricing Under Market Microstructure Effects: A Random Forest Approach.

DOI: 10.48550/arxiv.2507.16701

Text ingested: `markdown_output/deep-2025-binary-tree-option-pricing-under-market.md`, converted from `raw/ofi-event-clock/deep-2025-binary-tree-option-pricing-under-market.pdf`.

Coverage of this summary: Read the entire markdown file, a working paper of moderate length (abstract through references, all sections and tables).

Known problems with the input: Venue/journal not stated in the paper; it presents as a working paper with only department affiliations, keywords and JEL codes.
<!-- AUTHORED REGION END -->