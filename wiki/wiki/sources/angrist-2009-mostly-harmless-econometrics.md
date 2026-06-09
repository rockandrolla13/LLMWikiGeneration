---
authors:
- Joshua D. Angrist
- Jörn-Steffen Pischke
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/angrist-2009-mostly-harmless-econometrics
page_type: source
publication_date: '2009'
publication_venue: Princeton University Press
related:
- concepts/conditional-independence-assumption
- concepts/difference-in-differences
- concepts/instrumental-variables
- concepts/local-average-treatment-effect
- concepts/potential-outcomes
- concepts/quantile-treatment-effects
- concepts/regression-discontinuity
- entities/david-card
- entities/jorn-steffen-pischke
- entities/joshua-angrist
- entities/princeton-university-press
- entities/victor-chernozhukov
revision_hash: sha256:c1b2abf18500505e33331bb8db2f026d805a5b30b37881163acef7ccee4dab92
revision_id: 1
source_hash: sha256:797016915fe2d18fcb1ff31a1b86cadb7fd25d22a5bfe8f3e193e2cd8976e095
source_path: raw/creditmacro/Mostly Harmless Econometrics An Empiricists Companion
  (Joshua D. Angrist, Jorn-Steffen Pischke) (z-library.sk, 1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- econometrics
- causal-inference
- instrumental-variables
- panel-data
- program-evaluation
- quantile-regression
title: 'Mostly Harmless Econometrics: An Empiricist''s Companion'
updated: '2026-06-09T12:00:00Z'
updated_by: op_fa4f0577e2a2
---

# Mostly Harmless Econometrics: An Empiricist's Companion

**Authors:** Joshua D. Angrist, Jörn-Steffen Pischke · **Year:** 2009 · **Venue:** Princeton University Press · **Type:** book

## Summary

A graduate-level applied econometrics text organized around credible causal inference rather than abstract estimation theory. Angrist and Pischke argue empirical work should begin with a well-posed causal question framed as a comparison of potential outcomes; the central challenge is the selection problem, which randomization solves by construction. Every observational method is an attempt to approximate that ideal under explicit identifying assumptions. The 'Core' develops four workhorse strategies (regression under conditional independence, instrumental variables / 2SLS and LATE, fixed effects and differences-in-differences, regression discontinuity). The lasting influence is methodological: it codified the design-based 'credibility revolution' approach.

## Key Claims

1. Empirical questions should be posed as causal comparisons of potential outcomes; the fundamental obstacle is the selection problem, solved by randomization.
2. Regression estimates causal effects only under the conditional independence assumption; controlling for outcomes of treatment ('bad controls') reintroduces bias.
3. Instrumental variables / 2SLS identify causal effects under endogeneity; with heterogeneous effects, IV identifies LATE (the effect on compliers), not the population ATE.
4. Fixed effects and differences-in-differences identify causal effects by differencing out time-invariant confounders under a parallel-trends assumption.
5. Regression discontinuity identifies local causal effects at a treatment-assignment cutoff; fuzzy RD is a form of instrumental variables.
6. Standard errors require care: clustering and serial correlation can severely understate uncertainty, and robust standard errors are biased in small samples.

## Questions Raised

- When is the conditional independence assumption defensible in observational data?
- How should one interpret and generalize LATE when compliers differ from the population of interest?
- How can the common-trends assumption underlying differences-in-differences be assessed or relaxed?

## Concepts

- [[concepts/potential-outcomes|Potential Outcomes]]
- [[concepts/instrumental-variables|Instrumental Variables]]
- [[concepts/local-average-treatment-effect|Local Average Treatment Effect (LATE)]]
- [[concepts/conditional-independence-assumption|Conditional Independence Assumption]]
- [[concepts/difference-in-differences|Differences-in-Differences]]
- [[concepts/regression-discontinuity|Regression Discontinuity Design]]
- [[concepts/quantile-treatment-effects|Quantile Treatment Effects]]

## Entities

- [[entities/joshua-angrist|Joshua D. Angrist]]
- [[entities/jorn-steffen-pischke|Jörn-Steffen Pischke]]
- [[entities/victor-chernozhukov|Victor Chernozhukov]]
- [[entities/david-card|David Card]]
- [[entities/princeton-university-press|Princeton University Press]]

## Source

- **Path:** `raw/creditmacro/Mostly Harmless Econometrics An Empiricists Companion (Joshua D. Angrist, Jorn-Steffen Pischke) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:797016915fe2d18fc...`