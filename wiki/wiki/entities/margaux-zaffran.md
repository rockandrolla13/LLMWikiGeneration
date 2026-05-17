---
title: Margaux Zaffran
page_id: entities/margaux-zaffran
page_type: entity
entity_type: person
revision_id: 2
created: 2026-04-10T18:00:00Z
updated: 2026-04-26T12:00:00Z
tags: [researcher, conformal-prediction, time-series, electricity-forecasting, missing-data]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci, sources/zaffran-2023-conformal-missing]
related: [concepts/adaptive-conformal-inference, concepts/conformal-prediction, concepts/missing-data-imputation, concepts/mask-conditional-validity, entities/julie-josse, entities/aymeric-dieuleveut, entities/yaniv-romano]
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
[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] at NeurIPS 2023 studied conformal prediction when covariates have missing values. Key contributions:

- Proved marginal validity holds for **any** imputation method and **any** missingness mechanism
- Showed missing values induce **heteroskedasticity**: uncertainty depends on which features are observed
- Introduced **Mask-Conditional Validity (MCV)**: coverage guarantee conditional on missing pattern
- Developed **CP-MDA** (Missing Data Augmentation) framework achieving MCV
- Demonstrated asymptotic conditional coverage with universally consistent quantile regression

This work, co-authored with [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]], [[entities/julie-josse|Julie Josse]], and [[entities/yaniv-romano|Yaniv Romano]], has practical implications for medical and critical care applications where missing patterns correlate with patient characteristics.

## PhD Thesis

**"Post-hoc predictive uncertainty quantification: methods with applications to electricity price forecasting"** (2024)

Supervised by:
- [[entities/julie-josse|Julie Josse]] (INRIA)
- [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]] (École Polytechnique)

Committee included: Florence Forbes, Pierre Pinson, Étienne Roquain, [[entities/emmanuel-candes|Emmanuel Candès]], Éric Moulines, [[entities/aaditya-ramdas|Aaditya Ramdas]]

## Publications in This Wiki

- [[sources/zaffran-2023-conformal-missing|Conformal Prediction with Missing Values (NeurIPS 2023)]]
- [[sources/zaffran-2022-aci|Adaptive Conformal Predictions for Time Series (ICML 2022)]]
- [[sources/zaffran-phd|PhD Thesis (2024)]]

## See Also

- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/missing-data-imputation|Missing Data Imputation]]
- [[concepts/mask-conditional-validity|Mask-Conditional Validity]]
