---
authors:
- Jan Babecky
- Tomas Havranek
- Jakub Mateju
- Marek Rusnak
- Katerina Smidkova
- Borek Vasicek
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/babecky-2013-leading-indicators-crisis-incidence
page_type: source
publication_date: '2013'
publication_venue: Journal of International Money and Finance
related:
- concepts/baa-corporate-bond-spread
- concepts/bayesian-model-averaging
- concepts/crisis-incidence-real-costs
- concepts/early-warning-indicators
- concepts/great-moderation
- concepts/panel-vector-autoregression
- concepts/system-gmm-dynamic-panel
- entities/borek-vasicek
- entities/jakub-mateju
- entities/jan-babecky
- entities/katerina-smidkova
- entities/marek-rusnak
- entities/tomas-havranek
revision_hash: sha256:12562dd7155a45fba51c9976322aeb366e243e6bdef5d557fb33c2ca5befe00a
revision_id: 1
source_hash: sha256:3bd6a2fbcaff1beece0bec44d5b301e1f34b4596316c6b3fd2766d6bc798b26f
source_path: raw/creditmacro/1-s2.0-S0261560613000028-main.md
source_type: paper
sources: []
tags:
- early-warning-systems
- financial-crises
- bayesian-model-averaging
- panel-var
- macroprudential
- credit-growth
title: 'Leading indicators of crisis incidence: Evidence from developed countries'
updated: '2026-06-09T12:00:00Z'
updated_by: op_0ea28cacd6be
---

# Leading indicators of crisis incidence: Evidence from developed countries

**Authors:** Jan Babecky, Tomas Havranek, Jakub Mateju, Marek Rusnak, Katerina Smidkova, Borek Vasicek · **Year:** 2013 · **Venue:** Journal of International Money and Finance · **Type:** paper

## Summary

Babecky et al. (2013) build a continuous early warning model for 36 EU and OECD countries over 1970-2010 at quarterly frequency, asking which macro-financial indicators best explain the real costs of crises. The dependent variable is an index of real costs (GDP growth, unemployment, fiscal deficit) restricted to the two years after a banking, currency, or debt crisis. Methodologically the paper selects each indicator's prediction horizon via bivariate panel VAR and then applies Bayesian Model Averaging over the 2^30 model space. Twelve of 30 indicators have posterior inclusion probability above 0.5; growth in domestic private credit at a four-year horizon is the single strongest truly-early warning signal, with government debt, current account deficit, FDI inflows, house and share prices, the BAA corporate bond spread and the yield curve warning roughly 5-6 quarters ahead.

## Key Claims

1. About one third of candidate early warning indicators (12 of 30, PIP > 0.5) are useful for explaining crisis incidence in EU/OECD countries over 1970-2010.
2. Growth in domestic credit to the private sector is the key truly-early warning indicator, signalling at a four-year horizon.
3. Higher government debt-to-GDP, current account deficits, and FDI inflows are robustly associated with larger post-crisis real costs.
4. Asset price crashes (house and share prices) amplify post-crisis downturns when distress reaches the banking system.
5. The BAA corporate bond spread, a proxy for global risk aversion, is positively associated with crisis severity.
6. A world private-credit crunch acts as a short-horizon trigger that magnifies post-crisis downturns.

## Questions Raised

- How would real-time usefulness differ given the crisis database benefits from hindsight?
- Could excluded indicators (regulatory capital, household credit) add predictive power?
- Does selecting lags via bivariate PVAR rather than jointly within BMA bias the selected horizons?

## Concepts

- [[concepts/early-warning-indicators|Early Warning Indicators]]
- [[concepts/bayesian-model-averaging|Bayesian Model Averaging]]
- [[concepts/panel-vector-autoregression|Panel Vector Autoregression]]
- [[concepts/crisis-incidence-real-costs|Crisis Incidence and Real Costs]]
- [[concepts/baa-corporate-bond-spread|BAA Corporate Bond Spread]]
- [[concepts/system-gmm-dynamic-panel|System GMM Dynamic Panel Estimation]]
- [[concepts/great-moderation|Great Moderation]]

## Entities

- [[entities/jan-babecky|Jan Babecky]]
- [[entities/tomas-havranek|Tomas Havranek]]
- [[entities/jakub-mateju|Jakub Mateju]]
- [[entities/marek-rusnak|Marek Rusnak]]
- [[entities/katerina-smidkova|Katerina Smidkova]]
- [[entities/borek-vasicek|Borek Vasicek]]

## Source

- **Path:** `raw/creditmacro/1-s2.0-S0261560613000028-main.md`
- **Type:** paper
- **Hash:** `sha256:3bd6a2fbcaff1beec...`