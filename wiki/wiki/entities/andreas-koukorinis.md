---
created: 2026-04-28 12:45:00+00:00
entity_type: person
page_id: entities/andreas-koukorinis
page_type: entity
related:
- concepts/conformal-prediction
- concepts/doubly-robust-estimation
- concepts/adaptive-conformal-inference
revision_id: 2
sources:
- sources/ahmad-2014-alaph-liquid-macro-credit-fund
- sources/koukorinis-2024-xantium-business-plan
- sources/koukorinis-2026-draci
tags:
- researcher
- ucl
- conformal-prediction
- causal-inference
title: Andreas Koukorinis
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 422778c1-c12e-52da-afe0-e06f489a87b5
content_hash: sha256:b8810eb4a4890c13e99bd05978cc3c0a455130f4fcc9f7a6df6df91482b47b6d
---

<!-- AUTHORED REGION START -->
# Andreas Koukorinis

**Affiliation:** Department of Computer Science, University College London

**Email:** a.koukorinis@cs.ucl.ac.uk

## Overview

Researcher at UCL working on uncertainty quantification for causal inference, with focus on combining [[concepts/conformal-prediction|conformal prediction]] methods with [[concepts/doubly-robust-estimation|doubly robust estimation]] for time series data.

## Research Interests

- Conformal prediction under temporal dependence
- Causal inference and treatment effect estimation
- Market microstructure and financial applications
- Distribution-free inference

## Key Contributions

### DR-ACI Method ([[sources/koukorinis-2026-draci|2026]])

Developed **Doubly Robust Adaptive Conformal Inference (DR-ACI)**, which:
- Constructs prediction intervals for treatment effects under β-mixing dependence
- Introduces temporal block cross-fitting with guard bands
- Proves coverage guarantees with explicit mixing, nuisance-bias, and adaptation terms
- Applied to Nasdaq's Dynamic M-ELO market microstructure study

The variance-standardized version (VS-DR-ACI) achieves 63% narrower intervals than alternatives while maintaining valid coverage under combined dependence and drift.

## Related Concepts

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]]
- [[concepts/beta-mixing|β-Mixing]]

## See Also

- [[sources/koukorinis-2026-draci|DR-ACI Paper (2026)]]

## Added by credit-macro ingest (2026-06-09)

Also appears in: [[sources/ahmad-2014-alaph-liquid-macro-credit-fund]], [[sources/koukorinis-2024-xantium-business-plan]]
<!-- AUTHORED REGION END -->
