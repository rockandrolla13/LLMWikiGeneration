---
title: "Jump Clustering, Information Flows, and Stock Price Efficiency"
page_id: sources/chen-2024-jump-clustering-information-flows
page_type: source
source_type: paper
revision_id: 1
created: 2026-05-21T12:00:00Z
updated: 2026-05-21T12:00:00Z
authors: [Jian Chen]
year: 2024
venue: Journal of Financial Econometrics
volume_issue_pages: "22(5), 1588-1615"
doi: 10.1093/jjfinec/nbae009
tags: [jump-clustering, hawkes-processes, stochastic-volatility, particle-filter, market-efficiency]
related: [concepts/hawkes-processes, concepts/jump-clustering, concepts/stochastic-volatility-with-jumps, concepts/particle-filter, concepts/stock-price-efficiency, concepts/ranked-probability-score, concepts/mcmc-bayesian-inference, entities/jian-chen, entities/darrell-duffie, entities/yacine-ait-sahalia]
mind_map_priority: high
---

# Jump Clustering, Information Flows, and Stock Price Efficiency

**Authors:** [[entities/jian-chen|Jian Chen]]

**Venue:** *Journal of Financial Econometrics*, 22(5), 1588-1615 (2024)

**DOI:** [10.1093/jjfinec/nbae009](https://doi.org/10.1093/jjfinec/nbae009)

## Summary

Models stock-return jumps as a bivariate (positive/negative) self/cross-exciting [[concepts/hawkes-processes|Hawkes process]] embedded in a [[concepts/stochastic-volatility-with-jumps|stochastic volatility]] model and proposes a novel [[concepts/jump-clustering|jump-clustering]]-based measure of [[concepts/stock-price-efficiency|stock price (in)efficiency]]. Uses [[concepts/mcmc-bayesian-inference|Bayesian MCMC]] for in-sample estimation and a [[concepts/particle-filter|particle filter]] for out-of-sample probabilistic jump forecasts, yielding a trading strategy with Sharpe ratio of 1.62 after transaction costs.

## Key Claims

1. Self-excitation of return jumps is stronger than cross-excitation; clustering varies across stocks and is associated with small caps, low liquidity, and high volatility
2. A jump-clustering measure outperforms Hou-Moskowitz price delay in capturing post-earnings-announcement drift
3. A signal based on the difference between predicted positive and negative jump probabilities has predictive power for returns

## Concepts

- [[concepts/hawkes-processes|Hawkes Processes]] — central
- [[concepts/jump-clustering|Jump Clustering]] — central
- [[concepts/stochastic-volatility-with-jumps|Stochastic Volatility with Jumps]] — central
- [[concepts/particle-filter|Particle Filter]] — central
- [[concepts/stock-price-efficiency|Stock Price Efficiency]] — central
- [[concepts/ranked-probability-score|Ranked Probability Score]] — supporting
- [[concepts/mcmc-bayesian-inference|MCMC Bayesian Inference]] — supporting

## Related Sources

(Leave empty for now — links will be added by future ingestions)
