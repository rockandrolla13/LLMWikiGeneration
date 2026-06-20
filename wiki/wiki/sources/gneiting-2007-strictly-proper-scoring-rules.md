---
authors:
- Tilmann Gneiting
- Adrian E. Raftery
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/gneiting-2007-strictly-proper-scoring-rules
page_type: source
publication_date: '2007'
publication_venue: Journal of the American Statistical Association
related:
- concepts/bregman-divergence
- concepts/continuous-ranked-probability-score
- concepts/energy-score
- concepts/interval-score
- concepts/logarithmic-score
- concepts/optimum-score-estimation
- concepts/strictly-proper-scoring-rules
- concepts/tick-loss
- entities/adrian-raftery
- entities/glenn-brier
- entities/leonard-savage
- entities/philip-dawid
- entities/roger-koenker
- entities/tilmann-gneiting
revision_hash: sha256:4caa4fc6494fcadc39471ecb05c92cea19fcf9b923410b3b42cbd86379241f95
revision_id: 1
source_hash: sha256:4fe98e7889286c7a250a670819522776d2651addaa491509d93b4b00376babcc
source_path: raw/creditmacro/Gneiting2007jasa.md
source_type: paper
sources: []
tags:
- scoring-rules
- probabilistic-forecasting
- forecast-evaluation
- calibration
- crps
title: Strictly Proper Scoring Rules, Prediction, and Estimation
updated: '2026-06-20T01:03:51Z'
updated_by: op_c66282c02cb0
schema_version: 2
uuid: 9fb8cb45-0448-50a9-921f-ce1faf488e5b
content_hash: sha256:7d1352695d8acf86cd54b29b5dbda51a27c0d68cfd361a389a63987832f1bd7e
---

<!-- AUTHORED REGION START -->
# Strictly Proper Scoring Rules, Prediction, and Estimation

**Authors:** Tilmann Gneiting, Adrian E. Raftery · **Year:** 2007 · **Venue:** Journal of the American Statistical Association · **Type:** paper

## Summary

Gneiting and Raftery review and develop the theory of proper scoring rules on general probability spaces, providing a unified treatment that connects scoring rules to convex analysis, information measures, entropy functions, and Bregman divergences. A scoring rule S(P,x) rewards a forecaster who quotes predictive distribution P when x materializes; it is proper if the forecaster maximizes expected reward by quoting their true belief, and strictly proper if that maximum is unique. The central characterization theorem shows every regular proper scoring rule arises as a subtangent of a convex expected-score (entropy) function, with the associated divergence being a Bregman divergence in the finite case. The article gives rigorous versions of the Savage and Schervish representations and catalogs density-forecast scores (logarithmic, spherical, pseudospherical, quadratic, CRPS).

## Key Claims

1. A regular scoring rule is (strictly) proper if and only if it derives from a (strictly) convex expected-score function via a subtangent, unifying scoring rules with convex analysis and Bregman divergences.
2. The continuous ranked probability score (CRPS) generalizes absolute error, can be evaluated in closed form for Gaussian predictive distributions, and is strictly proper relative to Borel measures with finite first moment.
3. The CRPS is a special case of the energy score, a strictly proper score for vector-valued forecasts derived from the Euclidean norm raised to power beta in (0,2).
4. Skill scores (e.g. the Brier skill score) are generally improper even when the underlying score is proper.
5. Any nondecreasing function yields a proper quantile score; the special case s(x)=x recovers the tick/check (pinball) loss used in quantile regression.
6. The interval score for central prediction intervals is proper and jointly rewards narrow width and penalizes non-coverage.
7. Optimum score estimation (maximizing mean proper score) generalizes maximum likelihood (logarithmic score) and quantile regression (tick loss).

## Questions Raised

- What is the general form of all proper scoring rules for quantile forecasts?
- Under what conditions is a divergence function a score divergence admitting representation by a proper scoring rule?
- Do asymptotic equivalences linking the logarithmic score to Bayes factors and BIC extend to other proper scores such as the CRPS?

## Concepts

- [[concepts/strictly-proper-scoring-rules|Strictly Proper Scoring Rules]]
- [[concepts/continuous-ranked-probability-score|Continuous Ranked Probability Score (CRPS)]]
- [[concepts/energy-score|Energy Score]]
- [[concepts/logarithmic-score|Logarithmic Score]]
- [[concepts/interval-score|Interval Score]]
- [[concepts/tick-loss|Tick (Pinball) Loss]]
- [[concepts/bregman-divergence|Bregman Divergence]]
- [[concepts/optimum-score-estimation|Optimum Score Estimation]]

## Entities

- [[entities/tilmann-gneiting|Tilmann Gneiting]]
- [[entities/adrian-raftery|Adrian E. Raftery]]
- [[entities/philip-dawid|A. Philip Dawid]]
- [[entities/glenn-brier|Glenn W. Brier]]
- [[entities/roger-koenker|Roger Koenker]]
- [[entities/leonard-savage|Leonard J. Savage]]

## Source

- **Path:** `raw/creditmacro/Gneiting2007jasa.md`
- **Type:** paper
- **Hash:** `sha256:4fe98e7889286c7a2...`
<!-- AUTHORED REGION END -->
