---
title: Longevity Risk
page_id: concepts/longevity-risk
page_type: concept
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- actuarial-science
- risk-management
- pensions
- insurance
sources:
- sources/tsai-2020-hierarchical-mortality
- sources/huynh-2021-mogp-longevity
related:
- concepts/lee-carter-model
- concepts/multi-population-mortality
- concepts/survival-probability
- concepts/hierarchical-credibility-model
mind_map_priority: high
schema_version: 2
uuid: 7a0121c0-43e3-5057-a8da-34a22bb7bd6a
content_hash: sha256:0f535cd417256a6b9d2ffadb4f17fbd4bef501f2ac3642b58a52d896a1c5d1c1
---

<!-- AUTHORED REGION START -->
# Longevity Risk

Longevity risk is the risk that people live longer than expected, creating financial strain on pension plans, annuity providers, and social security systems.

## Types of Longevity Risk

### Idiosyncratic (Individual) Risk
- Individual variation around expected lifetime
- Diversifiable in large pools
- Handled by law of large numbers

### Systematic (Aggregate) Risk
- Unexpected improvement in mortality for entire population
- NOT diversifiable
- The primary concern for financial institutions

## Financial Impact

For a pension plan or annuity provider:
- 1 year increase in life expectancy ≈ 3-5% increase in liabilities
- Systematic improvements compound over time
- Back-book liabilities particularly exposed

## Measurement

**Longevity Value at Risk**: Amount by which liabilities could exceed expected due to mortality improvements at a given confidence level.

**Key metrics**:
- Life expectancy at age 65
- Survival curves
- Period vs cohort mortality rates

## Management Strategies

| Strategy | Description |
|----------|-------------|
| Longevity swaps | Transfer systematic risk to capital markets |
| Buy-ins/buy-outs | Transfer to insurance company |
| Reinsurance | Share risk with reinsurers |
| Natural hedging | Offset with life insurance book |
| Deferred annuities | Reduce exposure period |

## Modelling Approaches

- Stochastic mortality models ([[concepts/lee-carter-model|Lee-Carter]], CBD)
- Multi-population models for hedging basis risk
- Hierarchical credibility for data-sparse populations
- Gaussian process approaches for flexibility

## See Also

- [[concepts/lee-carter-model|Lee-Carter Model]]
- [[concepts/multi-population-mortality|Multi-Population Mortality]]
- [[concepts/survival-probability|Survival Probability]]
- [[sources/tsai-2020-hierarchical-mortality|Hierarchical Credibility Theory for Multi-Country Mortality (2020)]]

<!-- AUTHORED REGION END -->
