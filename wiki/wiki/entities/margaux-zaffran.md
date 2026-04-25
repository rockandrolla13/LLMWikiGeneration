---
title: Margaux Zaffran
page_id: entities/margaux-zaffran
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-10T18:00:00Z
updated: 2026-04-10T18:00:00Z
tags: [researcher, conformal-prediction, time-series, electricity-forecasting]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci]
related: [concepts/adaptive-conformal-inference, concepts/conformal-prediction, entities/julie-josse, entities/aymeric-dieuleveut]
mind_map_priority: high
---

# Margaux Zaffran

**Margaux Zaffran** is a researcher specializing in [[concepts/uncertainty-quantification|uncertainty quantification]] and [[concepts/conformal-prediction|conformal prediction]], with applications to electricity price forecasting.

## Affiliation

- PhD from Institut Polytechnique de Paris / École Polytechnique (defended June 2024)
- INRIA Sophia-Antipolis/Montpellier
- EDF R&D (Électricité de France)

## Research Focus

Zaffran's work focuses on developing predictive intervals for machine learning models without distributional assumptions, motivated by the need for reliable electricity price forecasting in volatile energy markets.

## Key Contributions

### Adaptive Conformal Inference for Time Series
[[sources/zaffran-2022-aci|Zaffran et al. (2022)]] analyzed and extended [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference (ACI)]] for time series with general dependency. Key contributions:

- Theoretical analysis of ACI's learning rate parameter γ
- Introduction of **AgACI**: parameter-free method using online expert aggregation
- Extensive benchmarking against EnbPI and online SCP
- Application to French electricity price forecasting

### Conformal Prediction with Missing Data
Zaffran's PhD thesis proved that [[concepts/split-conformal-prediction|split conformal prediction]] maintains validity guarantees even when applied to imputed data with missing values—regardless of the imputation method used.

## PhD Thesis

**"Post-hoc predictive uncertainty quantification: methods with applications to electricity price forecasting"** (2024)

Supervised by:
- [[entities/julie-josse|Julie Josse]] (INRIA)
- [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]] (École Polytechnique)

Committee included: Florence Forbes, Pierre Pinson, Étienne Roquain, [[entities/emmanuel-candes|Emmanuel Candès]], Éric Moulines, [[entities/aaditya-ramdas|Aaditya Ramdas]]

## Publications in This Wiki

- [[sources/zaffran-2022-aci|Adaptive Conformal Predictions for Time Series (2022)]]
- [[sources/zaffran-phd|PhD Thesis (2024)]]

## See Also

- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/conformal-prediction|Conformal Prediction]]
