---
authors:
- Yichi Zhang
- Mihai Cucuringu
- Alexander Y. Shestopaloff
- Stefan Zohren
content_hash: sha256:a9f825c251b62a2784a7f20748a79248df5d8a84a937f61e23cf22052b7ee39d
created: 2026-09-27 01:47:00+00:00
page_id: sources/zhang-2026-clusterlob-enhancing-trading-strategies-clustering-orders-published
page_type: source
publication_venue: Quantitative Finance, Vol. 26, No. 8, pp. 1285-1309
related:
- concepts/limit-order-book
- concepts/order-flow-imbalance
- concepts/trader-clustering
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/flow-decomposition
- entities/mihai-cucuringu
- entities/stefan-zohren
revision_id: 1
schema_version: 2
source_hash: sha256:11bceb8d473bf470bcdb950424ceb45d6a713e2daf660d76eda78ba671ca8e41
source_path: markdown_output/zhang-2026-clusterlob-enhancing-trading-strategies-clustering-orders-published.md
source_type: paper
tags:
- limit-order-book
- clustering
- order-flow-imbalance
- market-by-order-data
- high-frequency-trading
- market-microstructure
- clock-calendar
- asset-equity
- harvest-relevant
title: 'ClusterLOB: enhancing trading strategies by clustering orders in limit order
  books'
updated: '2026-09-27T01:47:00Z'
uuid: bccfbdf8-4489-571c-a20f-410206df392e
year: 2026
---

<!-- AUTHORED REGION START -->
# ClusterLOB: enhancing trading strategies by clustering orders in limit order books

## Summary

The paper asks whether individual orders in a limit order book can be grouped into behaviorally meaningful participant types using only public market-by-order (MBO) data, and whether signals built from those groups predict returns better than signals built from the whole order flow. It targets three archetypes motivated by prior agent-based and broker-order-flow work: directional traders whose orders move price immediately, opportunistic traders who anticipate short-term moves, and market-making traders who supply liquidity with little directional impact.

Each new order is described by six time-dependent features (available same-side volume, time since the last mid-price change, time since the price level was first and most recently touched, and cumulative same-side and opposite-side book volume ahead of the order), all forward-rolling normalized over the preceding 100 orders to avoid look-ahead bias and to make features comparable across stocks. K-means++ with a shared reference-stock initialization groups orders into three clusters per stock, on one year (2021) of NASDAQ MBO data for 15 stocks split into small-, medium- and large-tick groups, using the first half of the year to train and the second half to test. Clusters are labeled directional, opportunistic or market-making by which one correlates most with contemporaneous, next-bucket, or end-of-day-bucket returns within 30-minute buckets, and the best-Sharpe cluster/order-flow-imbalance (OFI) combination from the training period is then evaluated out of sample against an unclustered benchmark.

Cluster identity and feature importance are stable from training to test (illustrated in detail for Comcast, CMCSA), and the best clustered strategy beats the unclustered benchmark in every tick-size group and for both return horizons tested, with the opportunistic cluster generally producing the strongest signal for near-term returns and the directional cluster doing best for medium-tick stocks. Decomposing the imbalance signal by add, cancel and trade event types did not further improve forward-looking performance.

What is new is a clustering pipeline that works directly on public MBO data without any proprietary broker or exchange labels, a consistent cross-stock cluster-labeling scheme based on correlation with three different return horizons, and evidence that conditioning an order-flow-imbalance signal on the inferred trader cluster materially improves its predictive and risk-adjusted trading performance relative to using the whole, unclustered order flow.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Individual orders are featurized and clustered at the order-message (MBO) level using a 100-order forward-rolling normalization window, but the order-flow-imbalance signals and the three return measures (contemporaneous, next-bucket, end-of-day-bucket) are computed on fixed 30-minute wall-clock buckets across the 09:30-16:00 trading day. The prediction horizon is therefore one bucket ahead for the next-bucket return, or from the current bucket to the trading day's last bucket for the end-of-day-bucket return.

## Data

- **Asset class:** Equities
- **Instruments:** 15 NASDAQ-listed stocks split into three tick-size groups: small-tick (CHTR, GOOG, GS, IBM, MCD, NVDA), medium-tick (AAPL, ABBV, PM), large-tick (CMCSA, CSCO, INTC, MSFT, KO, VZ)
- **Venue:** NASDAQ (order book reconstructed via LOBSTER from ITCH data)
- **Period:** Full year 2021; training set January 1 - June 30, 2021, test set July 1 - December 31, 2021
- **Granularity:** Market-by-order (MBO) event-level messages during 09:30-16:00 trading hours, with signals and returns aggregated into 30-minute buckets

## Features and Measures

- **six time-dependent order features (V, T^m, T^1, T', SBS, OBS).** Per-order features capturing the available same-side book volume at the order's price, the time since the mid-price last changed, the time since that price level was first and most recently touched, and the cumulative same-side and opposite-side book volume ahead of the new order, each forward-rolling normalized over the preceding 100 orders.
- **Size-based and Count-based order flow imbalance (OFI).** Best-level imbalance measures comparing, over an interval, the change in order size or order count added, cancelled and traded at the best bid versus the best ask, following the definition used by Cont, Kukanov and Stoikov.
- **Decomposed OFI by event type.** OFI computed separately for add (submission), cancel (deletion) and trade (execution) events, to test whether the mix of event types changes the signal's predictive power.
- **K-means++ order clustering with base initialization.** Clustering of normalized per-order features into three groups per stock using K-means++, with cluster centroids first fit on a reference stock and then used to initialize clustering on every other stock so cluster labels are comparable across stocks.

## Method

For each stock and tick-size group, the six per-order features are computed and forward-rolling normalized on every trading day, then clustered into three groups (K=3) with K-means++, using a base-initialization scheme (a randomly chosen reference stock's fitted centroids seed the clustering of every other stock) so cluster labels are consistent across stocks. Size-based and Count-based OFI are computed per cluster within 30-minute buckets for the training period, and each cluster is labeled directional, opportunistic or market-making according to which of three return measures (contemporaneous CONR, next-bucket FRNB, end-of-bucket-to-day-end FREB) its OFI correlates with most strongly; a mode-estimation step reconciles labels that vary slightly across stocks.

For each return target, the cluster/OFI combination with the highest annualized Sharpe ratio in the training data is selected as the best strategy, then applied unchanged to the test period and compared against a benchmark that uses the full, unclustered order flow. All strategies are rescaled to a common annualized volatility target of 0.15 before comparison. Performance is judged on annualized expected excess return, hit rate, volatility, downside deviation, maximum drawdown, Sharpe ratio, Sortino ratio, Calmar ratio, average profit over average loss, and PnL per trade, computed separately for all events and for add/cancel/trade event-type decompositions of OFI, and separately for the small-, medium- and large-tick stock groups.

## Results

- For CMCSA, the ANOVA F-test ranks OBS, T^m and SBS as by far the most discriminative features for the clustering, with V and T^1 the weakest, in both training and test.
- CMCSA cluster shares were fairly stable out of sample: the directional cluster grew from 45.2% of events in training to 51.9% in test, opportunistic fell from 39.4% to 34.6%, and market-making fell from 15.4% to 13.5%.
- Executions were concentrated away from the market-making cluster: only 0.004% of that cluster's events in training (0.013% in test) were trades, while the overall execution share rose from 3.44% to 4.57%.
- In the small-tick test set, the opportunistic cluster's Count-based OFI signal for next-bucket returns (FRNB) achieved a Sharpe ratio of 1.34 and a PnL per trade of 0.66, versus 0.6 and -0.78 Sharpe for the unclustered Size- and Count-based benchmarks respectively.
- For the same small-tick opportunistic signal applied to end-of-day-bucket returns (FREB), Sharpe fell to 0.23, while both unclustered benchmarks stayed sharply negative (Sharpe below -2.35).
- Across tick-size groups, the best clustered strategy beat the no-cluster benchmark for FRNB everywhere: Sharpe ratios of 1.34 (small-tick, opportunistic), 1.248 (medium-tick, directional) and 1.548 (large-tick, opportunistic).
- The same ordering held for FREB but with weaker Sharpes (0.23 small-tick, 0.531 medium-tick, 0.438 large-tick), consistent with OFI signals being more informative at short horizons than at longer ones.
- Decomposing OFI by add, cancel and trade event types did not improve forward-looking predictive performance.

## Limitations

- The three cluster labels (directional, opportunistic, market-making) are an ex-post interpretation based on correlation with returns, not verified against ground-truth trader identities.
- Results are for 15 NASDAQ equities across three tick-size groups; the paper does not test other venues or asset classes.
- The best OFI/cluster combination is chosen in-sample by highest Sharpe ratio and then evaluated out of sample only once, so the reported test performance may still reflect some in-sample selection.
- Reader note: the article does not describe transaction costs, market impact, or execution slippage for the backtested trading strategies.
- Cluster identity was not perfectly consistent across stocks and required a mode-estimation relabeling step, which the authors note as a residual source of variability.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/trader-clustering|trader clustering]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/flow-decomposition|flow decomposition]]
- [[entities/mihai-cucuringu|Mihai Cucuringu]]
- [[entities/stefan-zohren|Stefan Zohren]]

## Citation

Yichi Zhang, Mihai Cucuringu, Alexander Y. Shestopaloff, Stefan Zohren (2026). ClusterLOB: enhancing trading strategies by clustering orders in limit order books. Quantitative Finance, Vol. 26, No. 8, pp. 1285-1309.

DOI: 10.1080/14697688.2026.2665153

Text ingested: `markdown_output/zhang-2026-clusterlob-enhancing-trading-strategies-clustering-orders-published.md`, converted from `raw/ofi-event-clock/zhang-2026-clusterlob-enhancing-trading-strategies-clustering-orders-published.pdf`.

Coverage of this summary: Read the full published article: abstract, background and OFI/decomposed-OFI definitions, data and methodology (LOBSTER preprocessing, six features, K-means++ clustering with base initialization, ClusterLOB algorithm, performance metrics), the CMCSA case-study results, the cross-stock tick-size-group FRNB/FREB tables, the conclusion, and the event-type-decomposition appendix tables and figures.

Known problems with the input: Several results tables (Tables 2-6 and Appendix Tables A1-A6) render with duplicated or misaligned columns after PDF-to-markdown conversion; the numbers used above were taken from the surrounding prose, which restates the same figures in full sentences, rather than read directly off those garbled table cells.
<!-- AUTHORED REGION END -->