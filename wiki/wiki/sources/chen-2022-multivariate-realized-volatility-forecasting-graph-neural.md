---
authors:
- Qinkai Chen
- Christian-Yann Robert
content_hash: sha256:d558b4d0426348a8116b0448b0385f4234cdcc379ef034b0fcc11a9228d52db5
created: 2026-09-27 01:47:00+00:00
page_id: sources/chen-2022-multivariate-realized-volatility-forecasting-graph-neural
page_type: source
related:
- concepts/graph-neural-networks
- concepts/realized-variance
- concepts/realized-covariance
- concepts/limit-order-book
- concepts/high-frequency-data
- concepts/deep-learning-for-finance
- concepts/feature-engineering
revision_id: 1
schema_version: 2
source_hash: sha256:c92dc470d72ab773114178c4e70f61cf00daa400e69ba93af86ab9dcffb31404
source_path: markdown_output/chen-2022-multivariate-realized-volatility-forecasting-graph-neural.md
source_type: paper
tags:
- realized-volatility-forecasting
- graph-neural-networks
- limit-order-book
- multivariate-forecasting
- equities
- deep-learning
- clock-calendar
- asset-equity
- harvest-relevant
title: Multivariate Realized Volatility Forecasting with Graph Neural Network
updated: '2026-09-27T01:47:00Z'
uuid: f3193420-a40b-5f41-acca-a08f7cb76f20
year: 2022
---

<!-- AUTHORED REGION START -->
# Multivariate Realized Volatility Forecasting with Graph Neural Network

## Summary

Prior work on forecasting realized volatility from limit order book (LOB) data is mostly univariate, fitting one model per stock and ignoring the fact that returns across stocks are correlated. The paper asks whether a multivariate approach that jointly models many related stocks, using a graph neural network, improves short-horizon realized-volatility forecasts.

The proposed model, Graph Transformer Network for Volatility Forecasting (GTN-VF), first encodes each stock's LOB and trade data at a given time into a node feature vector, combining numerical indicators with a learned embedding of the stock ticker. A stack of Graph Transformer layers then updates each node's representation using attention over its own features and the features of connected neighbor nodes, where edges come from four relation types: similarity between a stock's own feature values at different times, feature-correlation similarity between different stocks, shared GICS sector membership, and supplier-customer supply-chain links. A fully connected layer converts the final node embedding into a realized-volatility forecast, trained to minimize Root Mean Square Percentage Error (RMSPE).

Using NYSE TAQ quote and trade data for about 500 S&P 500 stocks sampled every second, and testing three forecast horizons, the full GTN-VF (all four relation types combined) beats a naive persistence guess, HAR-RV, LightGBM, an MLP, TabNet, and a vanilla relation-free version of the same network, on every horizon and on both validation and test data.

The main contribution is architectural: a graph-based model flexible enough to combine an unlimited number of relational data sources, including non-covariance-based sources such as sector and supply-chain data, together with LOB features, in a single multivariate volatility forecast, which the authors say had not previously been proposed for this task.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Best bid/ask quotes and trades are snapshotted every second; each stock-day is divided into 6 fixed buckets centered on 10:00, 11:00, 12:00, 13:00, 14:00 and 15:00 EST. Within each bucket, features are built from a backward window before the center time, and the target realized volatility is computed from returns over a forward window after it, with the backward and forward windows both tested at 600, 1200 and 1800 seconds.

## Data

- **Asset class:** Equities
- **Instruments:** About 500 S&P 500 constituent stocks (494 stocks in the reported train/validation/test splits)
- **Venue:** US stock exchanges, via NYSE daily TAQ data
- **Period:** Train: Jan-17 to Dec-19; validation: Jan-20 to Dec-20; test: Jan-21 to Oct-21 (as reported for a 600-second horizon)
- **Granularity:** 1-second snapshots of best bid/ask quotes and aggregated trades, rolled up into 600/1200/1800-second buckets

## Features and Measures

- **GTN-VF node feature.** A per-stock, per-timestamp feature vector combining numerical LOB/trade-based indicators (73 in total, covering quantities such as quote WAP, spreads, size imbalance and realized volatility over the backward window) with a learned embedding of the stock ticker.
- **Temporal relationship graph.** Connects a stock's own node at one timestamp to its most similar other timestamps, where similarity is measured by low RMSPE between average quote WAP in the first and last 100 seconds of each bucket.
- **Cross-sectional feature-correlation graph.** Connects each stock to the other stocks whose LOB-based features are most similar (lowest RMSPE) over the sample.
- **Sector relationship graph.** Connects two stocks if they share the same GICS classification, at a chosen granularity (Sector, Industry Group, Industry or Sub-Industry).
- **Supply-chain relationship graph.** Connects two companies that have a supplier-customer relationship in the training period, built from Factset supply-chain data.

## Method

The model, GTN-VF, is a 3-layer Graph Transformer Network with 8 attention heads and 128 channels per layer; categorical features are embedded into a 32-dimension vector. Each layer updates a node's hidden representation with a multi-head, dot-product-attention aggregation of its own and its connected neighbors' hidden states, following a message-passing-style Graph Transformer operator. The final node embedding is passed through a fully connected layer to produce the realized-volatility forecast, trained by minimizing Root Mean Square Percentage Error (RMSPE) rather than plain MSE, so that stocks with different volatility levels are weighted comparably.

Performance is judged on a strict time-ordered train/validation/test split (validation and test periods never precede training), using RMSPE on held-out buckets for three forecast horizons (600, 1200 and 1800 seconds). Benchmarks include a naive persistence guess, HAR-RV, LightGBM, an MLP, TabNet, and a vanilla GTN-VF trained without any relational graph edges, as well as versions of GTN-VF using each individual relation type alone.

## Results

- The full GTN-VF, combining all four relation types, achieves the lowest RMSPE of any model on both validation and test sets and at all three forecast horizons (600, 1200 and 1800 seconds).
- On average GTN-VF improves RMSPE by about 6% versus the naive persistence guess and by about 2% versus the best single baseline, TabNet, on the test set.
- Individually, the temporal feature-correlation relation gives the largest RMSPE gain (about 1.2% at the 600-second horizon), versus about 0.7% for the sector relation, even though sector edges are far more numerous.
- Prediction is harder for less liquid stocks: RMSPE for the most liquid stocks is about 5% better than for the least liquid.
- The paper reports the graph model's RMSPE improvement over Naive Guess as about 8% for more liquid stocks and about 2% for less liquid stocks, in a passage that also states the improvement is larger for less liquid stocks; the two statements are inconsistent in the source text and are reported here verbatim.
- Node connectivity matters: more strongly connected nodes have better (lower) RMSPE, with about a 2% difference in RMSPE between the most and least connected nodes.
- Among GICS sector granularities, Industry-level sector edges gave the best test RMSPE (0.2422) versus 0.2578 for Industry Group and 0.2441 for Sub-Industry; the coarsest Sector-level graph (178.7M edges) could not be trained because its edge count exceeded memory limits.

## Limitations

- Authors state some individual relations, such as the sector graph with 47.86M edges, add mostly noisy connections because every pair of same-sector stocks is linked whether or not they are meaningfully related.
- The coarsest GICS Sector graph could not be trained at all due to memory limits.
- Reader note: evaluated only on around 500 large, mostly liquid US equities using LOB quote/trade data; not tested on bonds, futures or other asset classes, or outside the sample period covered.
- Reader note: forecast horizons are restricted to six fixed intraday snapshot times and three window lengths (600/1200/1800 seconds); other clock definitions are not tested.

## Related

- [[concepts/graph-neural-networks|graph neural networks]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/realized-covariance|realized covariance]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/feature-engineering|feature engineering]]

## Citation

Qinkai Chen, Christian-Yann Robert (2022). Multivariate Realized Volatility Forecasting with Graph Neural Network.

DOI: 10.1145/3533271.3561663

Text ingested: `markdown_output/chen-2022-multivariate-realized-volatility-forecasting-graph-neural.md`, converted from `raw/ofi-event-clock/chen-2022-multivariate-realized-volatility-forecasting-graph-neural.pdf`.

Coverage of this summary: Read the full paper end to end, including the abstract, model formulation, experiments, ablation studies, conclusion and the Appendix A feature list.

Known problems with the input: year from file metadata; Section 5.5.1 contains an internally inconsistent liquidity-improvement claim (states the graph model improves more on less liquid stocks, but the parenthetical gives 8% for more liquid stocks vs 2% for less liquid stocks); reported verbatim from the source rather than resolved.
<!-- AUTHORED REGION END -->