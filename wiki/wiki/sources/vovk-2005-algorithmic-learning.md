---
title: Algorithmic Learning in a Random World
page_id: sources/vovk-2005-algorithmic-learning
page_type: source
source_type: book
revision_id: 1
created: 2026-05-24 16:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Vladimir Vovk
- Alexander Gammerman
- Glenn Shafer
year: 2005
venue: Springer (1st ed. 2005; substantially revised 2nd ed. 2022)
tags:
- conformal-prediction
- foundational
- textbook
- exchangeability
- on-line-learning
- venn-predictors
- on-line-compression-models
related:
- concepts/conformal-prediction
- concepts/split-conformal-prediction
- concepts/nonconformity-score
- concepts/exchangeability
- concepts/marginal-coverage
- concepts/conditional-coverage
- concepts/full-conformal-prediction
- concepts/mondrian-conformal-prediction
- concepts/venn-predictors
- concepts/on-line-compression-models
- concepts/cross-conformal-prediction
- entities/vladimir-vovk
- entities/alexander-gammerman
- entities/glenn-shafer
- sources/shafer-2007-cp-tutorial
- sources/vovk-2012-cross-conformal
- sources/fontana-2023-cp-unified-review
- sources/angelopoulos-2022-gentle-intro
mind_map_priority: high
schema_version: 2
uuid: df137b6f-155d-5d53-ae28-932aa7300f4d
content_hash: sha256:06b1e66293b0fe2171baa8b36a4657f8deaa7eea2dabefee3fd79ac2ebd4e875
---

<!-- AUTHORED REGION START -->
# Algorithmic Learning in a Random World

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/alexander-gammerman|Alexander Gammerman]], [[entities/glenn-shafer|Glenn Shafer]]

**Year:** 2005 (1st ed.); 2022 (substantially revised 2nd ed.)

**Venue:** Springer

## Summary

The foundational monograph on [[concepts/conformal-prediction|conformal prediction]] by its inventors. The book develops a theory of *hedged* prediction algorithms that learn and predict simultaneously in an on-line, transductive framework. Each prediction is accompanied by a valid measure of accuracy and reliability under the [[concepts/exchangeability|randomness (i.i.d./exchangeability)]] assumption.

The central machinery is the conformal predictor: take any user-chosen [[concepts/nonconformity-score|nonconformity measure]] `A(B, z)` together with p-values computed within an exchangeable bag, and you get nested prediction sets that are provably valid. Long-run error frequency stays at or below the chosen significance level ε regardless of the underlying distribution or the choice of nonconformity measure.

Beyond the basic batch and transductive constructions the book develops:

- **Inductive Conformal Predictors (ICP, Ch. 4).** The split-conformal variant that decouples training from prediction for computational efficiency. The version everyone uses in practice.
- **[[concepts/mondrian-conformal-prediction|Mondrian conformal predictors]].** Category- and label-conditional validity via a user-chosen taxonomy partition.
- **Ridge Regression Confidence Machine (RRCM) and kernelised variants.** Closed-form full CP for regression by exploiting linear dependence on `y`.
- **[[concepts/venn-predictors|Venn predictors]] (Chs. 6, 9).** Multiprobability predictors producing calibrated probability forecasts under exchangeability, sidestepping Ch. 5's impossibility results which show no probabilistic predictor can be well-calibrated under unconstrained randomness.
- **[[concepts/on-line-compression-models|On-Line Compression Models (OCM)]] (Chs. 8-9).** A generalisation beyond exchangeability subsuming the Gaussian and Markov models within Kolmogorov's programme of statistical modelling via sufficient statistics / repetitive structures.
- **Exchangeability supermartingales (Ch. 7).** Sequential tests of the exchangeability assumption itself via power supermartingales and the simple-mixture / tracking-the-best constructions.

Chapter 10 situates the framework against inductive learning (PAC, statistical learning theory), Bayesian inference, and classical transductive prediction (Fisher-Student tolerance regions).

## Key Contributions

1. The conformal prediction framework: distribution-free prediction sets with finite-sample [[concepts/marginal-coverage|marginal validity]] under exchangeability.
2. Any nonconformity measure yields a valid conformal predictor. Choice only affects efficiency.
3. The on-line / transductive protocol as the natural setting for hedged prediction, with single-parameter (ε) guarantees rather than PAC (ε, δ) bounds.
4. Inductive Conformal Predictors (ICP), the split-conformal scheme that became dominant in practice.
5. [[concepts/mondrian-conformal-prediction|Mondrian conformal predictors]] for category- and label-conditional validity.
6. The Ridge Regression Confidence Machine (RRCM) and a general scheme for nonconformity from SVMs, nearest neighbours, decision trees, boosting, neural networks, and logistic regression.
7. [[concepts/venn-predictors|Venn predictors]] for calibrated probability forecasting under exchangeability.
8. Impossibility theorems (Theorems 5.2, 6.5) showing well-calibrated probabilistic prediction is unattainable under unconstrained randomness.
9. Generalisation beyond i.i.d. via [[concepts/on-line-compression-models|On-Line Compression Models]] — exchangeability, Gaussian, Markov, and hypergraphical models as instances of Kolmogorov's repetitive-structure programme.
10. Confidence (1 − second-largest p-value) and credibility (largest p-value) as a two-number summary of a conformal prediction.

## Why This Source Matters

This is the source. Every CP paper either cites it or cites someone who does. If you want the formal language (bags, n-events, on-line compression, randomness vs exchangeability) you read this book. For ML practitioners the [[sources/angelopoulos-2022-gentle-intro|Angelopoulos-Bates 2022]] tutorial covers the algorithmic recipes more accessibly; for theoreticians extending the framework, Vovk-Gammerman-Shafer remains the reference.

A second edition (Springer, 2022) updates the development with material from the post-2005 wave (covariate shift, online ACI-style work, conformal predictive distributions).

## Relation to Other Wiki Sources

- [[sources/shafer-2007-cp-tutorial]] — short tutorial companion to this book.
- [[sources/vovk-2012-cross-conformal]] — Vovk's later paper introducing cross-conformal prediction.
- [[sources/fontana-2023-cp-unified-review]] — theory-focused review of post-2005 developments.
- [[sources/angelopoulos-2022-gentle-intro]] — practitioner-facing tutorial for the modern ML audience.

## See Also

- [[concepts/conformal-prediction]]
- [[concepts/venn-predictors]]
- [[concepts/on-line-compression-models]]
- [[entities/vladimir-vovk]], [[entities/alexander-gammerman]], [[entities/glenn-shafer]]

<!-- AUTHORED REGION END -->
