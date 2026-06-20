---
title: Machine Learning-based Relative Valuation of Municipal Bonds
page_id: sources/saha-2024-muni-bond-ml
page_type: source
created: 2026-04-26 02:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- machine-learning
- municipal-bonds
- CatBoost
- similarity-learning
- relative-valuation
authors:
- Preetha Saha
- Dhruv Desai
- Jingrao Lyu
- Rishab Chauhan
- Jerinsh Jeyapaulraj
- Peter Chu
- Philip Sommer
- Dhagash Mehta
year: 2024
journal: arXiv
institution: BlackRock
related:
- concepts/similarity-learning
- concepts/catboost
- concepts/municipal-bonds
- concepts/relative-valuation
schema_version: 2
uuid: 83af4255-4e21-5527-a25c-06b24d1f6a80
content_hash: sha256:bfd15457bab533f7d7bb2b6ae9bc0582cb82194013fe97e2e6e441616f2ace68
---

<!-- AUTHORED REGION START -->
# Machine Learning-based Relative Valuation of Municipal Bonds

## Summary

Proposes a supervised similarity framework using CatBoost for relative valuation in the municipal bond market. Addresses the challenge of valuing illiquid bonds (less than 10% trade >25 days/year) by learning distance metrics to identify similar bonds based on risk profiles.

## Key Findings

- **CatBoost Superiority**: Outperforms rule-based, heuristic, and Random Forest approaches
- **Proximity Learning**: Novel method to calculate proximity for boosting trees
- **Multi-Output Regression**: Learns on multiple targets simultaneously
- **Practical Deployment**: Back-testing methodology validates real-world applicability

## Market Challenges

- $4 trillion market with 50,000+ issuers
- Less than 2% of securities trade daily
- 50% of bonds trade ≤5 days per year
- Highly fragmented across states, sectors, maturities

## Methodology

- CatBoost algorithm with categorical feature handling
- Tree-based proximity/similarity learning
- Multi-output regression for multiple targets
- Novel tree importance weighting for gradient boosting

## Key Innovation: Proximity Calculation

For gradient boosted trees, uses exponentially decreasing tree importance:
- Earlier trees have larger impact on error correction
- Similarity weighted by residual error reduction
- Extends Random Forest proximity concept to boosting

## Applications

- Relative value analysis for illiquid bonds
- Price discovery using similar bond cohorts
- Portfolio construction for institutional investors
- Risk profile comparison

## Key Concepts

- [[concepts/similarity-learning|Similarity Learning]]
- [[concepts/catboost|CatBoost Algorithm]]
- [[concepts/municipal-bonds|Municipal Bonds]]
- [[concepts/relative-valuation|Relative Valuation]]

## Implications

1. ML enables pricing in illiquid markets
2. Supervised similarity outperforms unsupervised clustering
3. Categorical features well-handled by CatBoost
4. Industrial-strength solution from major asset manager

## Related Sources

- [[sources/feng-2025-predicting-bond-returns|Feng et al. (2025)]] - ML for corporate bonds
- [[sources/fedenia-2021-ml-trade-classifier|Fedenia et al. (2021)]] - ML in bond markets

<!-- AUTHORED REGION END -->
