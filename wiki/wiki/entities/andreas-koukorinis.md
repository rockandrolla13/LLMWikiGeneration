---
title: "Andreas Koukorinis"
page_id: entities/andreas-koukorinis
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-28T12:45:00Z
updated: 2026-04-28T12:45:00Z
sources: [sources/koukorinis-2026-draci]
related: [concepts/conformal-prediction, concepts/doubly-robust-estimation, concepts/adaptive-conformal-inference]
tags: [researcher, ucl, conformal-prediction, causal-inference]
---

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
