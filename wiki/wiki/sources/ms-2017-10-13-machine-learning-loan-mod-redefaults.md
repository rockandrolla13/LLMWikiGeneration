---
authors:
- Jeen Ng
- James Egan
- Vishwanath Tirupattur
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/ms-2017-10-13-machine-learning-loan-mod-redefaults
page_type: source
publication_date: '2017'
publication_venue: Morgan Stanley Research
related:
- concepts/default-rates
- concepts/distressed-exchange
- concepts/machine-learning-credit-modeling
- entities/james-egan
- entities/jeen-ng
- entities/morgan-stanley
- entities/vishwanath-tirupattur
revision_hash: sha256:73408de9f6f849cf1bc928f3a24ff84aba8d1f327f17ebc23ae6699a87b39df4
revision_id: 1
source_hash: sha256:0fa192572cacfd55909946838e8e2f5b3ed76452137ec48c05d987968b433712
source_path: raw/creditmacro/Morgan Stanley - MODs Machine Learning on Drivers - 2017-10-13.md
source_type: article
sources: []
tags: []
title: 'MODs: Machine Learning on Drivers'
updated: '2026-06-09T12:00:00Z'
updated_by: op_43b3448a64f7
---

# MODs: Machine Learning on Drivers

**Authors:** Jeen Ng, James Egan, Vishwanath Tirupattur · **Year:** 2017 · **Venue:** Morgan Stanley Research · **Type:** report

## Summary

A Resi Credit Insights / QuantWise note applying machine learning to identify the features driving re-defaults of modified loans in legacy non-agency RMBS pools, where modifications grew from 6% of balances in January 2009 to 54% by 2017. The authors find that features measured at the time of modification (notably the percentage change in payment) are more predictive than origination-time features such as original FICO and LTV. Feature importance has shifted over time, with delinquency duration prior to modification and rate incentive becoming more informative. More complex models such as neural networks, gradient boosting and random forests outperform regularized logistic regression and LDA, and ensembling further improves predictive power and stability.

## Key Claims

1. Modified loans grew from 6% of legacy non-agency UPB in January 2009 to 54% by 2017, making post-modification performance a primary driver of relative value.
2. Features measured at modification, especially the payment-change percentage, are more predictive of re-default than origination-time features like FICO or LTV.
3. Ensembles of complex learners (neural networks, gradient boosting, random forest) outperform regularized logistic regression and linear discriminant analysis in predicting re-defaults.

## Concepts

- [[concepts/default-rates|Default Rates]]
- [[concepts/machine-learning-credit-modeling|Machine Learning for Credit Modeling]]
- [[concepts/distressed-exchange|Distressed Exchange]]

## Entities

- [[entities/morgan-stanley|Morgan Stanley]]
- [[entities/jeen-ng|Jeen Ng]]
- [[entities/james-egan|James Egan]]
- [[entities/vishwanath-tirupattur|Vishwanath Tirupattur]]

## Source

- **Path:** `raw/creditmacro/Morgan Stanley - MODs Machine Learning on Drivers - 2017-10-13.md`
- **Type:** article
- **Hash:** `sha256:0fa192572cacfd559...`