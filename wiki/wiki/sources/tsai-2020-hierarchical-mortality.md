---
title: "Incorporating hierarchical credibility theory into modelling of multi-country mortality rates"
page_id: sources/tsai-2020-hierarchical-mortality
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Cary Chi-Liang Tsai, Adelaide Di Wu]
year: 2020
venue: Insurance Mathematics and Economics
doi: 10.1016/j.insmatheco.2020.01.001
tags: [mortality-modelling, credibility-theory, lee-carter, multi-population, longevity-risk]
related: [sources/namora-2021-hierarchical, sources/huynh-2021-mogp-longevity, concepts/lee-carter-model, concepts/hierarchical-credibility-model, concepts/longevity-risk, entities/cary-tsai]
mind_map_priority: high
---

# Incorporating Hierarchical Credibility Theory into Modelling of Multi-Country Mortality Rates

**Authors:** [[entities/cary-tsai|Cary Chi-Liang Tsai]], Adelaide Di Wu

**Year:** 2020

**Venue:** Insurance: Mathematics and Economics

**Institution:** Simon Fraser University

## Summary

This paper applies [[concepts/hierarchical-credibility-model|hierarchical credibility theory]] from property/casualty insurance to model multi-country mortality rates, achieving more accurate forecasts than traditional [[concepts/lee-carter-model|Lee-Carter]] approaches.

## Motivation

- Mortality rates across countries are correlated due to shared exposures (healthcare, environment)
- Traditional single-population models ignore cross-population dependencies
- Longevity risk management requires accurate multi-population forecasting
- Existing multi-population extensions of Lee-Carter have limitations

## Key Contributions

### 1. Hierarchical Structure for Mortality Data
Five-level hierarchy:
1. **Level 0:** Year (yearly mortality decrements)
2. **Level 1:** Age (consecutive ages xL to xU)
3. **Level 2:** Gender (male/female)
4. **Level 3:** Country (US, UK, Japan)
5. **Level 4:** Multi-country aggregate

### 2. Model Specification
- Models yearly decrement: Y_{c,g,x,t} = ln(m_{c,g,x,t}) - ln(m_{c,g,x,t-1})
- Removes downward trend for stationarity
- Risk parameters at each level are i.i.d. conditional on upper level

### 3. Empirical Performance
Compared against:
- Classical Lee-Carter model
- Joint-k Lee-Carter model
- Co-integrated Lee-Carter model
- Augmented common factor Lee-Carter model

**Result:** Hierarchical credibility approach produces more accurate forecasts (lower AMAPE)

### 4. Stochastic Extension
- Provides predictive intervals for projected mortality rates
- Enables stochastic simulations for applications
- Useful for pricing mortality-linked securities

## Data

- Human Mortality Database (HMD)
- US, UK, Japan (both genders)
- Multiple fitting year spans and forecasting periods

## Impact

- Bridges property/casualty credibility methods with life/longevity modelling
- Provides practical tool for multi-population mortality forecasting
- Applicable to pricing q-forwards, longevity bonds, survivor swaps

## See Also

- [[concepts/hierarchical-credibility-model|Hierarchical Credibility Model]]
- [[concepts/lee-carter-model|Lee-Carter Model]]
- [[concepts/longevity-risk|Longevity Risk]]
- [[sources/huynh-2021-mogp-longevity|Huynh & Ludkovski 2021 (MOGP Longevity)]]
