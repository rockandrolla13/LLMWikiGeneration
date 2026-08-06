---
title: "101 Formulaic Alphas"
page_id: sources/kakushadze-2015-101-formulaic-alphas
page_type: source
source_type: paper
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
authors: [Zura Kakushadze]
year: 2015
venue: "arXiv preprint (arXiv:1601.00991); Wilmott Magazine"
tags: [quantitative-trading, formulaic-alpha, price-volume, mean-reversion, momentum, statistical-arbitrage, worldquant, alpha-combination, factor-models, empirical-finance]
related: [concepts/formulaic-alpha, concepts/price-volume-alpha, concepts/mean-reversion, concepts/momentum-trend-following, concepts/mega-alpha-combination, concepts/industry-neutralization, concepts/alpha-correlation-turnover, entities/zura-kakushadze, entities/igor-tulchinsky, entities/worldquant]
mind_map_priority: high
---

# 101 Formulaic Alphas

**Authors:** [[entities/zura-kakushadze|Zura Kakushadze]]

**Venue:** arXiv preprint (arXiv:1601.00991); Wilmott Magazine, 2015

## Summary

This catalog paper presents explicit formulas — which double as executable computer code — for 101 real-life quantitative trading alphas proprietary to [[entities/worldquant|WorldQuant LLC]], built almost entirely from daily price-volume data (open, close, high, low, volume, vwap, returns). Each signal is a [[concepts/formulaic-alpha|Formulaic Alpha]] assembled from a compact vocabulary of cross-sectional and time-series operators, and most are [[concepts/price-volume-alpha|Price-Volume Alphas]] combining [[concepts/mean-reversion|Mean-Reversion]] and [[concepts/momentum-trend-following|Momentum / Trend Following]] building blocks. The alphas have short holding periods (~0.6–6.4 days) and low average pairwise correlation (15.9%), making them suitable for [[concepts/mega-alpha-combination|Mega-Alpha Combination]]. Empirically the paper shows alpha returns scale with volatility (R ~ sigma^0.76) while turnover has no significant explanatory power for returns or for pairwise correlations, part of its broader study of [[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]]. Several alphas also apply [[concepts/industry-neutralization|Industry Neutralization]] via the indneutralize operator. It is presented as the first public disclosure of such a large set of real, production-grade formulaic alphas, intended to demystify modern quant trading and let readers replicate and test the signals.

## Key Claims

1. Provides explicit formulas (which are also computer code) for 101 real-life quantitative trading alphas, mostly price-volume based with some fundamental and industry-classification inputs, of which 80 were in production at time of writing.
2. Across the 101 alphas the average holding period ranges roughly 0.6–6.4 days and the average (median) pairwise correlation is low at 15.9% (14.3%), enabling combination into a diversified [[concepts/mega-alpha-combination|mega-alpha]].
3. Alpha returns are strongly correlated with volatility, following an empirical scaling R ~ sigma^zeta with zeta approximately 0.76, and show no statistically significant dependence on turnover.
4. Turnover (specifically its log) has poor explanatory power for the pairwise correlation structure of the alphas, directly confirming an earlier, more indirect result of Kakushadze and [[entities/igor-tulchinsky|Tulchinsky]] (2015).
5. Each alpha is expressible from a fixed operator set (rank, correlation, covariance, delta, delay, decay_linear, scale, ts_rank/ts_min/ts_max/ts_argmax, stddev, signedpower, indneutralize) applied to standardized price-volume inputs, making the signals fully reproducible.

## Concepts

- [[concepts/formulaic-alpha|Formulaic Alpha]] — the paper's central object: each of the 101 alphas is given as an explicit formula that is simultaneously computer code.
- [[concepts/price-volume-alpha|Price-Volume Alpha]] — nearly all 101 alphas are built from daily price and volume inputs rather than fundamentals.
- [[concepts/mean-reversion|Mean-Reversion]] — a core signal archetype, e.g. contrarian delay-0 open-versus-prior-close moves (Alpha#42).
- [[concepts/momentum-trend-following|Momentum / Trend Following]] — the complementary archetype, e.g. the intraday delay-1 momentum example Alpha#101.
- [[concepts/mega-alpha-combination|Mega-Alpha Combination]] — the low pairwise correlations motivate combining the alphas into a single diversified portfolio.
- [[concepts/industry-neutralization|Industry Neutralization]] — several alphas demean within industry groups via the indneutralize operator.
- [[concepts/alpha-correlation-turnover|Alpha Correlation and Turnover]] — the paper's empirical analysis of how returns and correlations relate to volatility and turnover.

## Related Sources

(Leave empty for now — links added by future ingestions)
