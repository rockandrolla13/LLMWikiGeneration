---
title: Mega-Alpha Combination
page_id: concepts/mega-alpha-combination
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [alpha-combination, factor-models, statistical-arbitrage, quantitative-trading]
sources: [sources/kakushadze-2015-101-formulaic-alphas]
related: [concepts/alpha-correlation-turnover, concepts/factor-models, concepts/statistical-arbitrage, concepts/alpha-signal]
mind_map_priority: medium
---

# Mega-Alpha Combination

**Mega-Alpha Combination** is the practice of combining hundreds of thousands to millions of faint, ephemeral, low-correlation alphas into a single unified traded portfolio, which yields diversification (hedging against any subset failing) and automatic internal crossing of trades that saves on transaction costs; a central challenge is the badly singular alpha sample covariance matrix ('too many variables, too few observations').

## Overview

Individual alphas are typically weak and short-lived, so [[entities/zura-kakushadze|Zura Kakushadze]] frames the practical goal as merging many of them into a single "mega-alpha." The low average pairwise correlation of the 101 formulaic alphas (15.9%) is precisely what makes such combination attractive: diversification hedges against any subset of signals decaying, and netting offsetting trades internally reduces transaction costs. The main obstacle is statistical — estimating the alpha covariance matrix when the number of alphas vastly exceeds the number of observations makes the sample covariance matrix badly singular. This motivates specialized risk-modeling techniques for combining large alpha collections.

## Sources

- [[sources/kakushadze-2015-101-formulaic-alphas]] — motivates combining low-correlation alphas into a diversified mega-alpha and notes the singular-covariance challenge.

## Related Concepts

- [[concepts/alpha-correlation-turnover]]
- [[concepts/factor-models]]
- [[concepts/statistical-arbitrage]]
- [[concepts/alpha-signal]]
