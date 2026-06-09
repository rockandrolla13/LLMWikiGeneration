---
title: Yaniv Romano
page_id: entities/yaniv-romano
page_type: entity
entity_type: person
revision_id: 2
created: 2026-04-26T12:00:00Z
updated: 2026-05-24T19:00:00Z
tags: [researcher, conformal-prediction, uncertainty-quantification, statistics, machine-learning]
sources: [sources/zaffran-2023-conformal-missing, sources/romano-2019-cqr, sources/romano-2020-aps]
related: [concepts/conformal-prediction, concepts/conformalized-quantile-regression, concepts/coverage-guarantee, entities/margaux-zaffran, entities/emmanuel-candes]
mind_map_priority: high
---

# Yaniv Romano

**Yaniv Romano** is a leading researcher in [[concepts/conformal-prediction|conformal prediction]] and [[concepts/uncertainty-quantification|uncertainty quantification]], known for developing Conformalized Quantile Regression (CQR) and extending conformal methods to complex real-world settings.

## Affiliation

- Assistant Professor, Departments of Electrical Engineering and Computer Science
- Technion - Israel Institute of Technology, Haifa, Israel

## Research Focus

Romano's research focuses on distribution-free uncertainty quantification methods that provide reliable prediction intervals without strong distributional assumptions. His work bridges statistics and machine learning, developing practical methods with theoretical guarantees.

## Key Contributions

### Conformalized Quantile Regression (CQR)

Romano et al. (2019) introduced CQR, which combines quantile regression with conformal prediction to produce adaptive prediction intervals that achieve marginal coverage while adapting to local data characteristics.

### Conformal Prediction with Missing Values

[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] at NeurIPS 2023, co-authored with Romano, addresses conformal prediction when covariates have missing values:
- Proved marginal validity holds for impute-then-predict
- Introduced mask-conditional validity (MCV) concept
- Developed CP-MDA framework for pattern-specific calibration

### Equalized Coverage

Romano, Barber, Sabatti & Candès (2020) developed methods for achieving equalized coverage across protected groups, ensuring fairness in uncertainty quantification.

## Academic Background

- PhD from Stanford University
- Postdoctoral work with [[entities/emmanuel-candes|Emmanuel Candès]]

## Collaborators

- [[entities/emmanuel-candes|Emmanuel Candès]] (Stanford)
- [[entities/margaux-zaffran|Margaux Zaffran]] (EDF/INRIA)
- [[entities/aaditya-ramdas|Aaditya Ramdas]] (CMU)
- Stephen Bates (Berkeley)

## Publications in This Wiki

- [[sources/zaffran-2023-conformal-missing|Conformal Prediction with Missing Values (NeurIPS 2023)]]

## See Also

- [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
