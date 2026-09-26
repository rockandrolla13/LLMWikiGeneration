---
title: Vladimir Vovk
page_id: entities/vladimir-vovk
page_type: entity
entity_type: person
revision_id: 2
created: 2026-04-10 18:00:00+00:00
updated: '2026-09-16T00:00:00Z'
tags:
- researcher
- conformal-prediction
- machine-learning
- statistics
- game-theoretic-probability
- foundational
sources:
- sources/vovk-2005-algorithmic-learning
- sources/shafer-2007-cp-tutorial
- sources/vovk-2012-cross-conformal
related:
- concepts/conformal-prediction
- concepts/exchangeability
- concepts/cross-conformal-prediction
- concepts/venn-predictors
- concepts/on-line-compression-models
- concepts/mondrian-conformal-prediction
- entities/alexander-gammerman
- entities/glenn-shafer
mind_map_priority: high
schema_version: 2
uuid: 4ca0b88b-dc14-557f-b5c6-fabc8226c83d
content_hash: sha256:48e3973f447c970b36445bedddf1d2e075f5ce5abe907966110fb0a1290b9cd2
---

<!-- AUTHORED REGION START -->
# Vladimir Vovk

**Vladimir Vovk** is a Professor at Royal Holloway, University of London, and one of the founders of [[concepts/conformal-prediction|conformal prediction]].

## Affiliation

- Royal Holloway, University of London
- Computer Learning Research Centre

## Key Contributions

### Conformal Prediction Framework
Together with Alex Gammerman and Glenn Shafer, Vovk developed the theoretical foundations of conformal prediction in the late 1990s and early 2000s.

### "Algorithmic Learning in a Random World" (2005)
The foundational textbook on conformal prediction, co-authored with Alex Gammerman and Glenn Shafer. This work established:

- The mathematical framework for conformal prediction
- Validity guarantees under [[concepts/exchangeability|exchangeability]]
- Various conformity measures and their properties
- Connections to online learning and game-theoretic probability

### Game-Theoretic Probability
Vovk has also contributed to game-theoretic foundations of probability and statistics.

## Impact

Vovk's work on conformal prediction has enabled:
- Distribution-free uncertainty quantification
- Finite-sample valid prediction intervals
- Model-agnostic approaches to prediction sets

His framework is now widely used in machine learning for applications requiring reliable uncertainty estimates.

## Publications in This Wiki

- [[sources/vovk-2005-algorithmic-learning]] — foundational CP textbook with [[entities/alexander-gammerman|Gammerman]] and [[entities/glenn-shafer|Shafer]].
- [[sources/shafer-2007-cp-tutorial]] — canonical 58-page CP tutorial with [[entities/glenn-shafer|Shafer]].
- [[sources/vovk-2012-cross-conformal]] — primary source for [[concepts/cross-conformal-prediction|cross-conformal prediction]].

### E-values

With [[entities/ruodu-wang|Ruodu Wang]], Vovk founded the [[concepts/e-value|e-value]] literature — the second framework in this wiki built on betting rather than tail probabilities.

- [[sources/vovk-2020-evalues-calibration-combination|E-values: calibration, combination, and applications]] (2021) — the founding paper.
- [[sources/vovk-2019-confidence-discoveries-evalues|Confidence and discoveries with e-values]] (2023) — e-processes and discovery matrices.
- [[sources/vovk-2021-admissible-merging-pvalues|Admissible ways of merging p-values under arbitrary dependence]] (2022), with Bin Wang.
- [[sources/vovk-2024-merging-sequential-evalues|Merging sequential e-values via martingales]] (2024) — betting is the only admissible sequential merge.
- [[sources/vovk-2024-true-false-discoveries-evalues|True and false discoveries with independent and sequential e-values]] (2024).
- [[sources/vovk-2024-nonparametric-e-tests-symmetry|Nonparametric e-tests of symmetry]] (2024).
- [[sources/vovk-2026-conformal-e-confounding|Conformal e-prediction in the presence of confounding]] (2026) — joins the e-value work to his own conformal framework.
- [[sources/vovk-2026-ci-causal-sequential|Confidence intervals for causal effects in sequential decision making]] (2026).

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/exchangeability|Exchangeability]]
- [[concepts/venn-predictors|Venn Predictors]]
- [[concepts/on-line-compression-models|On-Line Compression Models]]
- [[entities/alexander-gammerman]], [[entities/glenn-shafer]] — co-inventors.

<!-- AUTHORED REGION END -->
