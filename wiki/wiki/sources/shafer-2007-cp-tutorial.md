---
title: A Tutorial on Conformal Prediction
page_id: sources/shafer-2007-cp-tutorial
page_type: source
source_type: tutorial
revision_id: 1
created: 2026-05-24 16:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Glenn Shafer
- Vladimir Vovk
year: 2007
venue: arXiv:0706.3188 (also JMLR 9, 371-421, 2008)
tags:
- conformal-prediction
- tutorial
- foundational
- on-line-learning
- gaussian-linear-model
- exchangeability
related:
- concepts/conformal-prediction
- concepts/nonconformity-score
- concepts/exchangeability
- concepts/on-line-compression-models
- concepts/mondrian-conformal-prediction
- concepts/marginal-coverage
- concepts/split-conformal-prediction
- entities/glenn-shafer
- entities/vladimir-vovk
- sources/vovk-2005-algorithmic-learning
- sources/vovk-2012-cross-conformal
- sources/angelopoulos-2022-gentle-intro
- sources/fontana-2023-cp-unified-review
mind_map_priority: high
schema_version: 2
uuid: 356d8903-0ee7-5e9c-88d7-9a3e38ecd282
content_hash: sha256:02f7198eadb15c5829d009bdfb52742851a5d0a7806e6bab2fa127344c4f0ef2
---

<!-- AUTHORED REGION START -->
# A Tutorial on Conformal Prediction

**Authors:** [[entities/glenn-shafer|Glenn Shafer]], [[entities/vladimir-vovk|Vladimir Vovk]]

**Year:** 2007 (arXiv); 2008 (JMLR)

**Venue:** arXiv:0706.3188; *Journal of Machine Learning Research* 9, 371-421

## Summary

The canonical foundational tutorial on [[concepts/conformal-prediction|conformal prediction]] by its co-originators, written as a 58-page companion to the [[sources/vovk-2005-algorithmic-learning|Vovk-Gammerman-Shafer 2005 monograph]]. Unlike [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates (2022)]], which targets ML practitioners with split-conformal recipes, this tutorial is theoretical and foundational. It develops CP from first principles within the on-line setting where labels are predicted successively, each one revealed before the next.

The central novelty emphasised throughout is a new concept of validity. Under [[concepts/exchangeability|exchangeability]], successive errors of a 1−ε conformal predictor are probabilistically independent ε-rare events, so a law of large numbers applies to an accumulating (not independent) dataset. Validity is proved two ways: via the classical argument (independence of exactly ε-rare events) and via a game-theoretic weak law of large numbers using the Backward-Looking Betting Protocol and Cournot's principle.

The tutorial works through concrete numerical examples to make the algorithm tangible:

- Predicting Czuber's 1900 binomial counts. Fisher's t-interval vs the exchangeability-based conformal interval (matching results).
- Iris classification (setosa vs versicolor) with three [[concepts/nonconformity-score|nonconformity measures]]: nearest neighbours, distance to species average, SVM.
- Petal-width regression on sepal length with NN and least-squares nonconformity measures.
- USPS digit classification showing how non-exchangeability between training and test partitions degrades the advertised error rate (5% becomes 8%).

The second half generalises beyond exchangeability to [[concepts/on-line-compression-models|on-line compression models]] (Martin-Löf, Lauritzen, Asarin), defined via summarising functions, updating functions, and one-step backward kernels. Two special cases are developed in depth:

- The exchangeability-within-label ([[concepts/mondrian-conformal-prediction|Mondrian]]) model, which calibrates errors per class.
- The on-line Gaussian linear model, where the natural nonconformity measure recovers exactly the classical t-distribution prediction interval for linear regression but with a stronger on-line validity guarantee.

An appendix proves a new result that has been overlooked since 1935: successive hits of Fisher's classical t-prediction interval are independent.

## Key Contributions

1. The on-line concept of validity: errors are probabilistically independent ε-rare events, so the law of large numbers applies to accumulating data.
2. Formal definition of nonconformity measure `A(B, z)` and the conformal algorithm in two forms (from old examples alone; using features of a new object).
3. The Backward-Looking Betting Protocol — a game-theoretic interpretation of exchangeability via Cournot's principle, with a self-contained proof of the game-theoretic weak law of large numbers.
4. Generalisation from exchangeability to [[concepts/on-line-compression-models|on-line compression models]] via summarising functions, updating functions, and backward kernels.
5. The on-line Gaussian linear model with proof that conformal prediction recovers the classical t-distribution regression interval while strengthening it to on-line validity.
6. The [[concepts/mondrian-conformal-prediction|exchangeability-within-label]] model calibrating error rates per class, demonstrated on USPS digit 5.
7. Optimality theorem: any invariant, valid, nested region predictor is dominated by a conformal predictor built from a derived nonconformity measure.
8. New proof (Appendix A.3) that successive hits of Fisher's classical t-prediction interval are independent.
9. Empirical demonstration that non-exchangeability (USPS train/test split) degrades the advertised 5% error rate to 8%.

## Why This Source Matters

Read this tutorial **before** the [[sources/vovk-2005-algorithmic-learning|2005 book]] if you want a 60-page distillation of the theoretical core. Read it **after** [[sources/angelopoulos-2022-gentle-intro|Angelopoulos & Bates]] if you've grasped the recipes and want the deep formal scaffolding (game-theoretic probability, on-line compression, the proper validity proof). Pair with [[sources/fontana-2023-cp-unified-review|Fontana et al. 2023]] for a current theory-focused map.

## Relation to Other Wiki Sources

- [[sources/vovk-2005-algorithmic-learning]] — the full monograph this tutorial summarises.
- [[sources/vovk-2012-cross-conformal]] — Vovk's later refinement to cross-conformal prediction.
- [[sources/angelopoulos-2022-gentle-intro]] — the modern practitioner counterpart.
- [[sources/fontana-2023-cp-unified-review]] — the post-2005 theory update.

## Questions Raised

- How should one diagnose and quantify the practical impact of non-exchangeability before trusting an advertised 1−ε coverage level?
- When non-exchangeability is detected, which on-line compression model (Mondrian, exchangeability-within-label, Gaussian linear) is the right relaxation for a given application?
- Under what conditions does on-line conformal prediction extend cleanly to dependent / time-series data where neither exchangeability nor a known compression structure holds?

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/on-line-compression-models]]
- [[concepts/mondrian-conformal-prediction]]
- [[entities/glenn-shafer]], [[entities/vladimir-vovk]]

<!-- AUTHORED REGION END -->
