---
title: Julie Josse
page_id: entities/julie-josse
page_type: entity
entity_type: person
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- researcher
- missing-data
- statistics
- machine-learning
- conformal-prediction
sources:
- sources/zaffran-2023-conformal-missing
- sources/zaffran-2022-aci
related:
- concepts/conformal-prediction
- concepts/missing-data-imputation
- entities/margaux-zaffran
- entities/aymeric-dieuleveut
mind_map_priority: medium
schema_version: 2
uuid: 388d4ea4-91a6-5175-9a88-f04970e52996
content_hash: sha256:49bd0d6e250c6098827ee1c238473e0af7e3c7cb78bce200cbbba06bcdb6aa54
---

<!-- AUTHORED REGION START -->
# Julie Josse

**Julie Josse** is a leading researcher in missing data methods, multivariate analysis, and machine learning, with significant contributions to understanding how imputation affects downstream learning tasks.

## Affiliation

- Research Director, INRIA
- PreMeDICaL project team, INRIA Sophia-Antipolis, Montpellier, France

## Research Focus

Josse's research focuses on:
- Missing data mechanisms and imputation methods
- Multivariate analysis and dimensionality reduction
- Statistical learning with incomplete data
- Conformal prediction under data incompleteness

## Key Contributions

### Missing Data in Machine Learning

Josse's work has established theoretical foundations for understanding how imputation methods interact with prediction algorithms:
- Proved Bayes consistency of impute-then-predict strategies
- Analyzed the distribution of imputed data
- Developed practical recommendations for handling missing values

### Conformal Prediction with Missing Values

As co-author on [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]], contributed to showing that:
- Missing values induce heteroskedasticity in predictions
- Standard conformal methods fail mask-conditional validity
- CP-MDA framework achieves equitable coverage across patterns

### Adaptive Conformal Inference

Co-authored [[sources/zaffran-2022-aci|Zaffran et al. (2022)]] on adaptive conformal inference for time series.

## PhD Supervision

Primary supervisor of [[entities/margaux-zaffran|Margaux Zaffran]]'s PhD thesis on uncertainty quantification for electricity price forecasting (defended 2024).

## Software

- Developer of missMDA R package for PCA/MCA with missing values
- Contributor to sklearn-compatible missing data tools

## Collaborators

- [[entities/margaux-zaffran|Margaux Zaffran]]
- [[entities/aymeric-dieuleveut|Aymeric Dieuleveut]] (École Polytechnique)
- [[entities/yaniv-romano|Yaniv Romano]] (Technion)
- Gaël Varoquaux (INRIA)
- Erwan Scornet (École Polytechnique)

## Publications in This Wiki

- [[sources/zaffran-2023-conformal-missing|Conformal Prediction with Missing Values (NeurIPS 2023)]]
- [[sources/zaffran-2022-aci|Adaptive Conformal Predictions for Time Series (ICML 2022)]]

## See Also

- [[concepts/missing-data-imputation|Missing Data Imputation]]
- [[concepts/conformal-prediction|Conformal Prediction]]

<!-- AUTHORED REGION END -->
