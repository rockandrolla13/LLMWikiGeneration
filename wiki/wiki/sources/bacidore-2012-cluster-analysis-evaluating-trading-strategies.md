---
authors:
- Jeff Bacidore
- Kathryn Berkow
- Ben Polidore
- Nigam Saraiya
content_hash: sha256:ff51bb59b9cd8ba4105bd02e446f98d56e98b37ae5599505b8ad96049747e80d
created: 2026-09-27 01:47:00+00:00
page_id: sources/bacidore-2012-cluster-analysis-evaluating-trading-strategies
page_type: source
publication_venue: The Journal of Trading (Summer 2012 issue)
related:
- concepts/trader-clustering
- concepts/optimal-execution
- concepts/feature-engineering
revision_id: 1
schema_version: 2
source_hash: sha256:527b8491ebcf3ed2d743b66ef0ca4b25d623d81c87a453b08a6e7a57dfbd734b
source_path: markdown_output/bacidore-2012-cluster-analysis-evaluating-trading-strategies.md
source_type: paper
tags:
- k-means
- transaction-cost-analysis
- algorithmic-trading
- trader-clustering
- post-trade-analysis
- vwap
- implementation-shortfall
- execution-strategy
- clock-calendar
- asset-equity
- added-by-hand
title: Cluster Analysis for Evaluating Trading Strategies
updated: '2026-09-27T01:47:00Z'
uuid: 41745adc-b183-5f36-85c0-fe2dd6440bd2
year: 2012
---

<!-- AUTHORED REGION START -->
# Cluster Analysis for Evaluating Trading Strategies

## Summary

Trading cost analysis (TCA) usually groups trades by the algorithm used, but high-touch traders often switch between algorithms as tactics within a single order, so grouping by algorithm or by average aggressiveness can hide the trader's real underlying strategy. The authors propose identifying these strategies empirically from post-trade fill data instead of relying on any strategy tag entered before or during the trade.

For each order they build a progress chart: the trading day is split into fixed 15-minute bins, and for each bin they compute the cumulative percentage of the order filled by the end of that bin. K-means clustering is then applied to these progress-chart vectors (using only the earlier bins, since the final bin is always 100% complete) to group orders into a small number of distinct execution styles, each represented by a cluster center that looks like an 'average' progress chart for that style.

Applied to a sample of orders sent to VWAP and implementation-shortfall (IS) algorithms, k-means recovered the four known order types (full- and half-day VWAP, full- and half-day IS) with high classification accuracy, and in an example with a hypothetical client it separated a trader's activity into three distinct strategies, including a minority strategy that made up only a small share of total value traded.

What is new is that the strategy grouping is derived purely from the shape of post-trade fill trajectories, with no need to tag strategies in advance or change trading workflows. Once orders are grouped this way, the authors argue TCA can be done per strategy, and the shape of each cluster's progress chart can suggest which benchmark (open, close, VWAP, arrival) a trader was implicitly targeting for that strategy.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Each order is represented as a progress chart: the trading day (9:30 AM to 4:00 PM) is divided into fixed 15-minute bins (26 per day), and the cumulative percentage of the order filled is computed at the end of each bin. K-means is applied to the vector of bin-level fill percentages (the paper notes only the first two of three illustrative bins carry information, since the last bin is always 100% complete) to assign each order to one of k execution-style clusters. There is no forecasting horizon; the method clusters already-completed orders by the shape of their intraday fill trajectory rather than predicting a future value.

## Data

- **Asset class:** Equities
- **Instruments:** Not stated beyond 'single stock' orders; the sample is described only as not-held market orders sent to a VWAP algorithm or to ITG Active Algorithm, a single-stock implementation shortfall (IS) algorithm.
- **Venue:** not stated
- **Period:** January 1, 2011, and September 31, 2011 (as printed)
- **Granularity:** 26 fixed 15-minute bins per trading day; orders limited to more than 500 shares so they were worked over time rather than executed in one slice.

## Features and Measures

- **fill progress chart.** For a given order, the sequence of cumulative percentage-filled values measured at the end of each fixed 15-minute bin across the trading day, used as the feature vector that characterizes how the order was worked.
- **k-means cluster center (strategy prototype).** The average progress chart of all orders assigned to a given cluster, used to characterize and label the 'average' execution style of that strategy.

## Method

The core method is k-means clustering applied to the bin-level progress-chart vectors described above. The algorithm starts from k initial cluster centers (user-specified or random), then iteratively assigns each order to the nearest center by a distance metric and recomputes centers, stopping once assignments and centers stop changing materially. The resulting cluster centers characterize each strategy's average shape, and the per-order assignments let analysts split trades by strategy for downstream transaction cost analysis (TCA).

Performance is judged by classification accuracy against known ground truth: because the sample orders were actually sent to specific algorithm/horizon combinations (half- and full-day VWAP, half- and full-day IS), the authors check what fraction of orders k-means assigns to the cluster matching their true algorithm and horizon. They also illustrate the method qualitatively on a hypothetical client's orders and on trader-level usage patterns, arguing that cluster assignments can suggest which benchmark (open, close, VWAP, arrival) a given strategy implicitly targets and can be cut by trader, fund, order size, market capitalization, time period, or market conditions.

## Results

- With no prior strategy labels, k-means recovered four distinct trading strategies matching half-day VWAP, full-day VWAP, full-day IS, and half-day IS orders.
- K-means classified over 98% of orders into the correct strategy overall.
- VWAP orders were correctly identified more than 99.5% of the time.
- IS orders were correctly identified more than 98% of the time.
- In a hypothetical client example, k-means separated trading into three distinct fill trajectories: trading into the close, front-loaded trading, and participation-based trading through the day.
- In that same example, only 5% of value was executed via the minority strategy (Strategy C), a pattern the authors say a traditional aggregate analysis could overlook.
- In a trader-level breakdown, one trader (Trader 1) was the dominant user of Strategy C, but Strategy C made up only 25% of that trader's overall trading.
- Different clusters/strategies performed best against different benchmarks (e.g., one strategy scored well versus the close, another versus arrival/open, another versus VWAP), consistent with traders implicitly targeting different benchmarks for different strategies.

## Limitations

- Sample restricted to orders of more than 500 shares sent to only two algorithm types (VWAP and a single implementation-shortfall algorithm, ITG Active Algorithm) at one broker (ITG).
- Sample period covers only about nine months (January-September 2011).
- Reader note: the client-level and trader-level illustrations (Exhibits 6-8) are presented as a 'hypothetical client' example rather than a validated out-of-sample result.
- Reader note: no statistical significance testing or robustness checks beyond the reported classification accuracy percentages are described.
- Reader note: the figures/exhibits referenced throughout (progress charts, cluster diagrams) are not reproduced in the converted text, so some illustrative detail could not be independently checked.

## Related

- [[concepts/trader-clustering|trader clustering]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/feature-engineering|feature engineering]]

## Citation

Jeff Bacidore, Kathryn Berkow, Ben Polidore, Nigam Saraiya (2012). Cluster Analysis for Evaluating Trading Strategies. The Journal of Trading (Summer 2012 issue).

Text ingested: `markdown_output/bacidore-2012-cluster-analysis-evaluating-trading-strategies.md`, converted from `raw/ofi-event-clock/bacidore-2012-cluster-analysis-evaluating-trading-strategies.pdf`.

Coverage of this summary: Read the entire markdown file: introduction/motivation, methodology, the worked k-means example, the VWAP/IS classification-accuracy application, the hypothetical-client and trader-usage examples, and the conclusion.

Known problems with the input: Author names are printed with irregular mid-word capitalization from the markdown/OCR conversion ('Kathryn BerKow', 'nigam Saraiya'); normalized here to standard capitalization (Kathryn Berkow, Nigam Saraiya) as this looks like a formatting artifact rather than the true printed spelling; The article states it originally appeared in the Summer 2012 issue of The Journal of Trading, but the converted file carries 'Fall 2018' running headers and a 2018 copyright notice, indicating this copy is a later reprint; year is taken as 2012 per the stated original publication date; Exhibits/figures referenced throughout (progress charts, cluster diagrams, trader-usage breakdowns) are not reproduced in the converted markdown, so figure-only detail could not be verified against source images.
<!-- AUTHORED REGION END -->