---
authors:
- Florian Ziel
- Kevin Berk
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/ziel-2019-multivariate-forecasting-evaluation
page_type: source
publication_date: '2019'
publication_venue: arXiv preprint (arXiv:1910.07325)
related:
- concepts/copula-sklar-theorem
- concepts/dawid-sebastiani-score
- concepts/diebold-mariano-test
- concepts/energy-score
- concepts/marginal-copula-score
- concepts/strictly-proper-scoring-rules
- concepts/variogram-score
- entities/florian-ziel
- entities/francis-diebold
- entities/kevin-berk
- entities/pierre-pinson
- entities/tilmann-gneiting
revision_hash: sha256:62711bdb05301492d29a95caa32cc207d73cd32878f1ae29cfd7abad3d1e8ec3
revision_id: 1
source_hash: sha256:ee5e8436d8ce9438e6d97de2b02c10967017b309f7270de815622b0cd8d70afc
source_path: raw/creditmacro/1910.07325v1.md
source_type: paper
sources: []
tags:
- scoring-rules
- multivariate-forecasting
- energy-score
- copula
- diebold-mariano-test
- ensemble-forecasting
title: 'Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper Scoring
  Rules'
updated: '2026-06-09T12:00:00Z'
updated_by: op_b7a89e800e62
---

# Multivariate Forecasting Evaluation: On Sensitive and Strictly Proper Scoring Rules

**Authors:** Florian Ziel, Kevin Berk · **Year:** 2019 · **Venue:** arXiv preprint (arXiv:1910.07325) · **Type:** paper

## Summary

Ziel and Berk study scoring rules for evaluating multivariate probabilistic forecasts, focusing on whether common rules can detect errors in the forecasted dependency structure. They review established multivariate rules (energy score, variogram score, Dawid-Sebastiani score) and propose a new family of marginal-copula scores that multiplicatively combine a marginal score (e.g. CRPS) with a copula score applied to copula observations via the probability integral transform; by Sklar's theorem the result is strictly proper for continuous marginals. Across simulation studies the energy score is the only measure that consistently separates the true model from alternatives with strong Diebold-Mariano power, and the copula energy score is the most sensitive to misspecified dependency. The authors stress that the Diebold-Mariano test, not relative change in score, is the appropriate discrimination tool, and that ensemble size and forecast horizon strongly affect power.

## Key Claims

1. The energy score is, across all simulation studies, the only evaluation measure that clearly separates the true model from alternatives with strong DM-test power, including dependency differences.
2. This contradicts Pinson and Tastu (2013), who used relative change in score rather than the Diebold-Mariano test.
3. The proposed marginal-copula score is strictly proper for continuous marginals by Sklar's theorem when both components are strictly proper.
4. The copula energy score is the single most sensitive score for detecting misspecified dependency structures.
5. The variogram and Dawid-Sebastiani scores are only proper, not strictly proper, so they can favor incorrect models and must not be used alone.
6. Relative change in score is not a reliable measure of discrimination ability; the Diebold-Mariano test should be used instead.
7. Ensemble sample size and forecast horizon strongly affect discrimination power; reported ensemble sizes in the literature are often far too small.

## Questions Raised

- Can a strict lower bound for the copula energy score be proven?
- Are there better linking functions than the multiplicative structure for combining marginal and copula scores?
- Could Wasserstein- or Hellinger-distance-based scoring rules yield useful proper scores for forecast evaluation?

## Concepts

- [[concepts/energy-score|Energy Score]]
- [[concepts/strictly-proper-scoring-rules|Strictly Proper Scoring Rules]]
- [[concepts/marginal-copula-score|Marginal-Copula Score]]
- [[concepts/copula-sklar-theorem|Copula and Sklar's Theorem]]
- [[concepts/variogram-score|Variogram Score]]
- [[concepts/diebold-mariano-test|Diebold-Mariano Test]]
- [[concepts/dawid-sebastiani-score|Dawid-Sebastiani Score]]

## Entities

- [[entities/florian-ziel|Florian Ziel]]
- [[entities/kevin-berk|Kevin Berk]]
- [[entities/tilmann-gneiting|Tilmann Gneiting]]
- [[entities/pierre-pinson|Pierre Pinson]]
- [[entities/francis-diebold|Francis X. Diebold]]

## Source

- **Path:** `raw/creditmacro/1910.07325v1.md`
- **Type:** paper
- **Hash:** `sha256:ee5e8436d8ce9438e...`