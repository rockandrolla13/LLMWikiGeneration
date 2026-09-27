---
authors:
- Rafaël Brutti
- Maciej Marowka
- Mihai Cucuringu
content_hash: sha256:918d4ad952a8ca021637c0b0daf6eb6c1efb868895dab299d41a973a37df2d15
created: 2026-09-27 01:47:00+00:00
page_id: sources/brutti-2026-noise-robust-orthogonal-clustering-applications-equity-markets
page_type: source
publication_venue: Quantitative Finance, Vol. 26, No. 6, pp. 903-930
related:
- concepts/hierarchical-clustering
- concepts/alpha-signal
- concepts/backtesting
- concepts/overfitting-backtesting
- concepts/feature-engineering
- entities/mihai-cucuringu
revision_id: 1
schema_version: 2
source_hash: sha256:df6138a5c5a9aeaaaad8f69bfd9cd2acf542a08967baf7f70e2c35c4053adbec
source_path: markdown_output/brutti-2026-noise-robust-orthogonal-clustering-applications-equity-markets.md
source_type: paper
tags:
- clustering
- equities
- gics
- statistical-arbitrage
- portfolio-construction
- ensemble-methods
- noise-filtering
- pca
- clock-calendar
- asset-equity
- added-by-hand
title: Noise-robust orthogonal clustering and applications to equity markets
updated: '2026-09-27T01:47:00Z'
uuid: 7f1a2366-b42a-55f3-be07-1170135c0411
year: 2026
---

<!-- AUTHORED REGION START -->
# Noise-robust orthogonal clustering and applications to equity markets

## Summary

The paper asks whether purely data-driven clustering of stock returns can find groupings that are both statistically meaningful and genuinely different from the standard sector classification (GICS), rather than just re-deriving sector structure under another name. It works with daily returns of S&P 500 constituents from 2010 to 2024, re-estimating clusters every quarter from a rolling window of historical daily returns.

The method first standardises returns cross-sectionally and over time, then projects them onto the leading eigenvectors of the correlation matrix for noise reduction (PCA cleaning). To force deviation from GICS, it further projects the data onto the subspace orthogonal to the GICS sector indicators before clustering, and shows this orthogonal-projection objective is mathematically equivalent to a trade-off between minimising reconstruction error and maximising distance from the GICS partition. Because base algorithms such as k-means are unstable across runs and under noise, the paper runs the base clustering many times and aggregates the results into a co-association matrix (the fraction of runs in which each pair of stocks lands in the same cluster), then clusters that matrix to obtain one stable consensus partition.

The main finding is that this ensemble, GICS-orthogonalised clustering ("Deviation-Aware" clustering) is markedly more stable under repeated runs and under several injected noise models (Gaussian, sign-flip, cross-sectional permutation, block-shock) than plain k-means, while still being statistically distinct from GICS by several external similarity metrics (ARI, NMI, cosine similarity) and still internally cohesive (higher-than-random intra-cluster covariance). Embedded in a simple cluster-based quantile mean-reversion trading strategy, this Deviation-Aware clustering earns a higher Sharpe ratio and cumulative P&L than the same strategy run on GICS sectors or on plain K-Means clusters, and randomised placebo versions of every clustering strategy earn close to zero Sharpe, indicating the gains come from real structure rather than the mechanics of the trading rule.

What is new relative to prior clustering-in-finance work is the explicit orthogonal-projection step against a benchmark partition (inspired by non-redundant/orthogonal clustering ideas from the data-mining literature) combined with an ensemble/co-association procedure for stability, and a direct economic test of whether the resulting deviation from GICS is itself a source of tradable, low-correlation alpha rather than noise.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Clusters are re-estimated at fixed calendar points (the start of every quarter) using a rolling 500-day (roughly two trading years) window of daily close-to-close returns for the current S&P 500 constituents. There is no intraday or trade-level sampling; the unit of observation is the daily return series per stock. In the trading application, cluster-based long/short positions are formed from a trailing 10-day cumulative-return ranking within each cluster, cluster selection is based on a trailing 3-month backtest, and the resulting weights are held for the following 3 trading months before the next quarterly re-clustering.

## Data

- **Asset class:** Equities
- **Instruments:** S&P 500 index constituents; all 880 firms that were index members at any point from 2010 to 2024
- **Venue:** Daily U.S. equity prices from CRSP via Wharton Research Data Services (WRDS), University of Pennsylvania; not a trading venue itself
- **Period:** 2010 to end of 2024
- **Granularity:** Daily close-to-close returns, adjusted for dividends and stock splits; clustering re-estimated quarterly from a rolling 500-day window

## Features and Measures

- **GICS orthogonal projection.** A projection operator built from GICS sector indicator vectors that removes the component of stock returns explained by sector membership, leaving a residual used to search for structure not captured by GICS.
- **Co-association (ensemble) matrix.** A matrix built by running a base clustering algorithm many times and recording, for each pair of stocks, the fraction of runs in which they were placed in the same cluster; clustering this matrix yields a single stable consensus partition.
- **Adjusted Rand Index (ARI).** A chance-corrected measure of pairwise agreement between two partitions of the same stocks, used to compare a clustering both to GICS and to itself across repeated runs or noise perturbations.
- **Normalised Mutual Information (NMI).** An information-theoretic measure of how much knowing one clustering assignment reduces uncertainty about another, used as a second external similarity metric against GICS.
- **Cosine similarity of cluster projection matrices (CoSim).** A similarity score between two clusterings computed from the trace overlap of their normalised cluster-indicator projection matrices.
- **Intra-cluster mean covariance.** The size-weighted average covariance between stocks placed in the same cluster, used as an internal validation measure of cluster cohesion.
- **Silhouette score and Calinski-Harabasz index.** Two internal clustering-quality measures: the Silhouette score compares each stock's average distance to its own cluster versus the nearest other cluster, and the Calinski-Harabasz index compares between-cluster to within-cluster dispersion.
- **Cluster-selection mean-reversion signal.** Within each cluster, stocks in the top 20% of trailing 10-day cumulative return are shorted and the bottom 20% are bought; clusters are then ranked by their own trailing 3-month Sharpe ratio and only the top three clusters' positions are kept for the next quarter.

## Method

The pipeline standardises the return matrix cross-sectionally and then over time, computes the empirical correlation matrix and its leading eigenvectors, and projects the standardised returns onto that subspace for PCA-based noise cleaning, then rescales again. To make the clustering deviate from GICS, the data are additionally projected onto the subspace orthogonal to the GICS sector indicators before applying a base clustering algorithm (mainly k-means, but also agglomerative clustering, spectral clustering, Gaussian mixture models, HDBSCAN, and the Giada-Marsili method, plus a bootstrapped hierarchical-clustering alternative to PCA for noise cleaning). The number of clusters K is fixed at 11 to match the number of GICS sectors, since alternative heuristics (cumulative variance, Marchenko-Pastur spectral thresholds, the elbow method) disagree strongly on the 'right' K. Stability is obtained through an ensemble/consensus procedure that reclusters the co-association matrix from many repeated base-clustering runs.

Performance is judged along two axes. Statistically, the paper compares each clustering to GICS and to itself across repeated runs and under four injected noise models (Gaussian, sign-flip, cross-sectional permutation, block-shock) using external metrics (ARI, NMI, CoSim) and internal metrics (intra-cluster covariance, Silhouette, Calinski-Harabasz). Economically, the clusters are fed into a quantile long/short mean-reversion strategy, backtested and compared by cumulative P&L, annualised Sharpe ratio, and turnover against a market benchmark, a no-clustering quantile strategy, and GICS- and K-Means-based versions of the same strategy, together with randomised placebo versions of each clustering strategy and a beta-adjusted residual-P&L analysis against those benchmarks.

## Results

- The Deviation-Aware (orthogonal, ensemble) clustering strategy reaches a Sharpe ratio of 0.788 and cumulative P&L of 161.10, above GICS (0.578, 118.33) and K-Means (0.663, 135.56), and above the no-clustering Quantile MR baseline (0.534, 108.74), though below the equally-weighted Market benchmark (0.918, 187.61).
- Placebo versions of every clustering strategy, built by randomising long/short assignment within clusters, have Sharpe ratios near zero (Placebo GICS 0.040, Placebo K-Means 0.021, Placebo Deviation 0.017), indicating the real strategies' performance reflects genuine cluster information rather than the mechanics of the 20/20 rebalancing rule.
- Clustering-based strategies trade far less than the naive cross-sectional Quantile MR baseline: turnover is about 24.4% for GICS and Deviation and 24.2% for K-Means, versus 87.9% for the no-clustering baseline.
- Ensemble (consensus) clustering with M=1000 runs concentrates pairwise stability scores (ARI/NMI/CoSim) between about 0.8 and 1.0, whereas plain K-Means shows much wider run-to-run dispersion on the same metrics.
- Heuristics for choosing the number of clusters disagree sharply: the 90% cumulative-variance threshold requires 145 principal components, the Marchenko-Pastur spike heuristic suggests 13 clusters, and non-parametric methods return cluster counts ranging from 11-15 up to 89-94 and 101-111 depending on the algorithm.
- The orthogonal projection materially reduces similarity to GICS on external metrics relative to standard K-Means, while retaining statistically significant intra-cluster covariance above a 3-sigma band of random clusterings.
- Under pure sampling noise (T=N=500, no true correlation), the expected median maximum pairwise correlation among stocks is approximately 0.197, illustrating how much spurious correlation can arise from noise alone.
- GICS's overlap with standard K-Means clustering shows a slight downward trend over the sample, and case studies (e.g. Tesla) show the two clustering schemes assign the same stock to markedly different economic groupings.

## Limitations

- The trading backtest excludes transaction costs and execution frictions, so reported P&L and Sharpe ratios are not directly deployable performance figures.
- The number of clusters K=11 is fixed to match GICS's 11 sectors for comparability rather than chosen by a principled criterion; the authors state this is 'not necessarily the optimal value'.
- Quarterly rebalancing is described by the authors as high-frequency from a diagnostic standpoint but coarser than would typically be used in a live strategy.
- Missing return observations are imputed with zeros, a simplification the authors acknowledge is not optimal though they argue it is low-impact given its low frequency.
- Reader note: the empirical analysis is limited to large-cap U.S. equities (S&P 500 constituents) over one 2010-2024 sample; generalisation to other markets, cap sizes, or periods is untested.

## Related

- [[concepts/hierarchical-clustering|hierarchical clustering]]
- [[concepts/alpha-signal|alpha signal]]
- [[concepts/backtesting|backtesting]]
- [[concepts/overfitting-backtesting|overfitting backtesting]]
- [[concepts/feature-engineering|feature engineering]]
- [[entities/mihai-cucuringu|Mihai Cucuringu]]

## Citation

Rafaël Brutti, Maciej Marowka, Mihai Cucuringu (2026). Noise-robust orthogonal clustering and applications to equity markets. Quantitative Finance, Vol. 26, No. 6, pp. 903-930.

DOI: 10.1080/14697688.2026.2671183

Text ingested: `markdown_output/brutti-2026-noise-robust-orthogonal-clustering-applications-equity-markets.md`, converted from `raw/ofi-event-clock/brutti-2026-noise-robust-orthogonal-clustering-applications-equity-markets.pdf`.

Coverage of this summary: Read the full paper end to end: abstract, introduction and related work, the data section, the methodology (standardisation, PCA cleaning, GICS orthogonal projection, ensemble clustering), the clustering evaluation metrics section, all experiments (choice of K, consensus clustering, cluster validation, economic benefits/trading strategy, correlation and residual P&L analysis), the conclusion, and the appendices (notation, BAHC, K-means proofs, Marchenko-Pastur theorem, performance-metric definitions, and the Tesla case-study appendix).

Known problems with the input: Most equations in the PDF-to-markdown conversion are replaced with '==> picture... omitted <==' placeholders, so exact formula forms could not be verified from the text and are described only in prose; Some passages show OCR/layout artifacts (reordered sentences, stray symbols, mangled subscripts/superscripts) around the proof-of-equivalence and clustering-evaluation-metrics sections; content there was used cautiously and only where the surrounding prose was unambiguous.
<!-- AUTHORED REGION END -->