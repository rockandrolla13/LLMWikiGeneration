---
authors:
- Adamantios Ntakaris
- Gbenga Ibikunle
content_hash: sha256:63af70dbea846a3f16cc042a30cd59aefb150fb6ac3cb80aec069898df80614d
created: 2026-09-27 01:47:00+00:00
page_id: sources/ntakaris-2024-online-high-frequency-trading-stock-forecasting
page_type: source
publication_venue: Economics of Financial Technology Conference, Edinburgh, UK, 2023
related:
- concepts/event-clock
- concepts/high-frequency-trading
- concepts/limit-order-book
- concepts/feature-engineering
- concepts/high-frequency-data
- entities/adamantios-ntakaris
revision_id: 1
schema_version: 2
source_hash: sha256:de9d7e3e576ea23e1bf148d5778c5405d4872dddc5181fd9ca77d6689a2e4dc7
source_path: markdown_output/ntakaris-2024-online-high-frequency-trading-stock-forecasting.md
source_type: paper
tags:
- high-frequency-trading
- limit-order-book
- mid-price-forecasting
- feature-importance
- k-means-clustering
- radial-basis-function-network
- online-learning
- clock-event
- asset-equity
- harvest-relevant
title: Online High-Frequency Trading Stock Forecasting with Automated Feature Clustering
  and Radial Basis Function Neural Networks
updated: '2026-09-27T01:47:00Z'
uuid: 29be7614-d8a7-530f-bee5-652d65c2e471
year: 2023
---

<!-- AUTHORED REGION START -->
# Online High-Frequency Trading Stock Forecasting with Automated Feature Clustering and Radial Basis Function Neural Networks

## Summary

The paper asks whether the feature-importance step and the cluster-count step of a machine-learning forecasting pipeline can be made fully automatic, instead of chosen by hand, for tick-by-tick prediction of a stock's limit order book mid-price. The authors build a four-stage online pipeline: first, two competing feature-importance mechanisms score the input features on every sliding window of order book events, one based on mean-decrease impurity (MDI) from a random-forest-style splitting criterion and the other built by turning gradient descent into an importance measure; second, the resulting importance-weighted features are expressed as a correlation-based distance matrix; third, k-means clustering is run repeatedly over a range of cluster counts and the count that gives the best silhouette-based quality ratio is kept; fourth, the chosen clusters set the centroids and spreads of a radial basis function neural network (RBFNN) that regresses the mid-price. Two input feature sets are compared, a small 'Simple' set of best bid/ask prices and volumes, and a larger 'Extended' set adding basic, kernel and polynomial transforms of those quantities.

The pipeline is run on nanosecond-resolution Level 1 order book data from 20 large-cap NASDAQ- and NYSE-listed US stocks (each with a market value of $200 billion or more), covering three months of trading. Training and testing follow a cumulative online scheme: every sliding block of order book events is used first to test, then folded into the training set, so the model keeps absorbing the latest data as it goes.

The main finding is that no single configuration wins everywhere: which of the two feature-importance methods and which of the two feature sets gives the lowest error differs stock by stock and month by month, and the choice of best method changes rapidly through the trading day. Measured by a mid-price-normalised error metric, the MDI method on the Simple feature set gave the lowest error in the largest share of stock-month cases among the four combinations tested. The paper's contribution is less a single winning model than a demonstration that automating both the feature-importance step and the cluster-count step removes the need for a manual, static topology choice, which the authors argue is important because HFT decision-making requires speed and the relevant feature space differs across stocks.

What is new relative to prior work cited by the authors is the combination: earlier studies used MDI, gradient descent, k-means or RBFNNs individually or in static offline pairings, but the authors state this is the first attempt to make both the feature-importance ranking and the k-means cluster count fully online and autonomous within the same LOB mid-price forecasting pipeline.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

Observations are order book trading events (tick-by-tick, not calendar time); the online protocol processes overlapping sliding windows of 100 events per block with an overlap of 99 events between consecutive blocks. The prediction target is the current mid-price at each event, so the forecast horizon is effectively the next reported event rather than a fixed time interval. Training and testing follow a cumulative five-fold online scheme, where each block is first used to test the current model and is then absorbed into the training set before the next block arrives.

## Data

- **Asset class:** Equities
- **Instruments:** 20 large-cap NASDAQ- and NYSE-listed US stocks with market value of $200 billion or more: AMZN, BAC, BRK, GOOGL, JNJ, JPM, KO, LLY, META, MRK, MSFT, NVDA, NVO, ORCL, PEP, PG, UNH, VISA, WMT, HD.
- **Venue:** NASDAQ and NYSE, via a Refinitiv tick data feed
- **Period:** 1 September 2022 to 30 November 2022 (three months)
- **Granularity:** Tick-by-tick Level 1 order book data at nanosecond time resolution

## Features and Measures

- **Mean-decrease impurity (MDI) feature importance.** A feature-importance score computed from how much each feature reduces node impurity, averaged over an ensemble of tree splits; the paper adapts it to score which order-book-derived inputs matter most for mid-price forecasting.
- **Gradient descent (GD) feature importance.** The authors turn the ordinary gradient-descent optimisation update into a feature-importance measure by tracking the learned weight vector that best maps the input features to the target price, and use it as a competing benchmark to MDI.
- **Correlation-based distance matrix.** The MDI- and GD-weighted feature matrices are each converted into a correlation matrix and then into a distance matrix, so that more correlated features sit closer together, which the k-means step can then cluster.
- **Silhouette-based clustering quality score.** A search over candidate cluster counts that scores each candidate using the mean and variance of per-point silhouette coefficients, keeping whichever cluster count gives the best ratio of mean to variance.
- **Mid-price.** The average of the best ask and best bid price in the limit order book at a given trading event; this is the quantity the RBFNN regressor is trained to predict.
- **Simple and Extended feature sets.** Two alternative input representations: 'Simple' uses only the best bid/ask prices and their volumes, while 'Extended' adds basic, synthesized, and linear/polynomial/sigmoid/exponential/RBF kernel transforms of those same best-level prices and volumes.

## Method

The pipeline runs the MDI and GD feature-importance mechanisms in parallel on each sliding window of order-book events, then converts each of the two resulting weighted feature matrices into a correlation-based distance matrix. A k-means search then tries a range of cluster counts against this distance matrix, scoring each candidate with a silhouette-based quality ratio and keeping the best one; this yields the centroids and spreads used to set up the hidden-layer neurons of a radial basis function neural network (RBFNN). The RBFNN's output layer is trained in closed form from the RBF activations and the target mid-price. The whole process is repeated online, block by block, separately for each of the 20 stocks and separately for the Simple and Extended feature sets, so the number of clusters and the winning feature-importance method can change from one block to the next.

Performance is judged with mean squared error (MSE) and root mean squared error (RMSE) on held-out test blocks under the cumulative five-fold online scheme, and with a mid-price-normalised RMSE (relative RMSE, RRMSE) used to compare the four combinations of feature-importance method and feature set on equal footing across stocks with very different price levels.

## Results

- The MDI method on the Simple feature set gave the lowest relative RMSE (RRMSE) in 36 out of 60 stock-month cases, more than the other three method/feature-set combinations.
- Which method (MDI or GD) and which feature set (Simple or Extended) performed best varied by stock and by month; no configuration dominated across all 20 stocks.
- The identity of the better feature-importance method changed rapidly online, alternating on average about every 10 trading events, and the MDI-based clustering mostly alternated between two and three clusters.
- Behaviour depended on the feature set used: for example MSFT's forecasts were worse under the Simple set than under the Extended set, and its best-performing method also differed between the two sets.
- GOOGL using the GD method on the Extended feature set produced the lowest RMSE among the scenarios reported.

## Limitations

- The authors describe the approach as a narrow, task-specific pipeline built specifically to forecast the LOB mid-price rather than a general-purpose method.
- The feature sets are limited to quantities easily engineered from the best bid/ask level; more elaborate hand-crafted or automatically discovered features are left to future work.
- No extensive benchmark modelling framework is used to stress-test the RBFNN topology against alternative regressors.
- The k-means step assumes isotropic clusters (constant variance in every cluster), an assumption the authors note may not hold.
- The authors say the dataset length (three months) should be extended in future studies to make the results more robust.
- Reader note: the evaluation covers only 20 large-cap US stocks over three consecutive months, so the reported RRMSE win rates may not generalise to smaller-cap names, other market regimes, or longer horizons.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/feature-engineering|feature engineering]]
- [[concepts/high-frequency-data|high frequency data]]
- [[entities/adamantios-ntakaris|Adamantios Ntakaris]]

## Citation

Adamantios Ntakaris, Gbenga Ibikunle (2023). Online High-Frequency Trading Stock Forecasting with Automated Feature Clustering and Radial Basis Function Neural Networks. Economics of Financial Technology Conference, Edinburgh, UK, 2023.

DOI: 10.48550/arxiv.2412.16160

Text ingested: `markdown_output/ntakaris-2024-online-high-frequency-trading-stock-forecasting.md`, converted from `raw/ofi-event-clock/ntakaris-2024-online-high-frequency-trading-stock-forecasting.pdf`.

Coverage of this summary: Read the whole converted markdown: introduction, related work, the four-block method description (Blocks 1-4), experimental protocol and dataset description, results discussion, limitations and conclusion, plus the appendix score tables (Tables II-VII), noting that equation and algorithm images were rendered as omitted pictures rather than transcribable text.

Known problems with the input: The job file's year_hint was 2024, but no publication year is printed in the paper body; the only calendar year printed is 2023, in a footnote stating the paper was presented at the Economics of Financial Technology Conference, 21-23 June 2023. Used 2023 as year and that conference as venue, since no journal or proceedings name is otherwise printed; Several equations and two algorithm boxes are rendered in the markdown as 'picture... intentionally omitted', so their exact mathematical form could not be transcribed; they are described only in prose above.
<!-- AUTHORED REGION END -->