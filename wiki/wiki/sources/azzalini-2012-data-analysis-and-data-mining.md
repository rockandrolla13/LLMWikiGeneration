---
authors:
- Adelchi Azzalini
- Bruno Scarpa
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/azzalini-2012-data-analysis-and-data-mining
page_type: source
publication_date: '2012'
publication_venue: Oxford University Press
related:
- concepts/bias-variance-tradeoff
- concepts/cluster-analysis-and-association-rules
- concepts/curse-of-dimensionality
- concepts/decision-trees
- concepts/discriminant-analysis
- concepts/local-regression
- concepts/splines-and-additive-models
- entities/adelchi-azzalini
- entities/bruno-scarpa
- entities/oxford-university-press
revision_hash: sha256:9bfc6094295fac5efc84844b8376bd0e5bd7afc74d1deee84bee7de7f94b60b0
revision_id: 1
source_hash: sha256:2d781fb8503063db895fdc4636595960fc59772341f41aee5df3d2cf69642381
source_path: raw/creditmacro/Data Analysis and Data Mining An Introduction (Azzalini
  A., Scarpa B.) (z-library.sk, 1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- data-mining
- statistical-learning
- nonparametric-regression
- classification
- clustering
- model-selection
title: 'Data Analysis and Data Mining: An Introduction'
updated: '2026-06-09T12:00:00Z'
updated_by: op_517152a99a7e
---

# Data Analysis and Data Mining: An Introduction

**Authors:** Adelchi Azzalini, Bruno Scarpa · **Year:** 2012 · **Venue:** Oxford University Press · **Type:** book

## Summary

A graduate introductory textbook positioning data mining at the intersection of statistics, computer science, and machine learning. The central thesis is that the classical statistical paradigm (model chosen on theoretical grounds before data, with proper sampling) does not fit modern large, opportunistically collected datasets, demanding a different methodology while keeping analysis human-directed (in R). It reviews classical foundations then develops the optimism/bias-variance trade-off and model selection, a toolkit of flexible nonparametric methods (local regression, splines, GAM, projection pursuit, trees, neural networks), classification, and unsupervised methods (clustering, association rules), motivated by real CRM-oriented case studies.

## Key Claims

1. Modern large-scale data is collected without the sampling procedures classical statistics assumes, so the inferential paradigm must adapt.
2. Size (number of units) mainly raises computational cost while dimensionality raises both computation and conceptual complexity.
3. High dimensionality induces the curse of dimensionality, degrading simple tools and local/nonparametric estimation.
4. Without preexisting theory, the model must be chosen by data exploration and checked with diagnostics and model-selection criteria.
5. Flexible function estimation provides a unified nonparametric approach to predicting quantitative variables.
6. Data analysis should remain human-directed within a flexible computational environment, not delegated to an automatic program.

## Questions Raised

- How should model complexity be selected to balance bias and variance when no theory specifies the true function?
- How can classical inferential guarantees be reinterpreted when data lack a designed sampling scheme?
- How do supervised methods perform on rare-event problems such as fraud detection?

## Concepts

- [[concepts/bias-variance-tradeoff|Bias-Variance Trade-off and Model Selection]]
- [[concepts/curse-of-dimensionality|Curse of Dimensionality]]
- [[concepts/local-regression|Nonparametric Local Regression]]
- [[concepts/splines-and-additive-models|Splines and Generalized Additive Models]]
- [[concepts/decision-trees|Decision Trees]]
- [[concepts/discriminant-analysis|Discriminant Analysis and Classification]]
- [[concepts/cluster-analysis-and-association-rules|Cluster Analysis and Association Rules]]

## Entities

- [[entities/adelchi-azzalini|Adelchi Azzalini]]
- [[entities/bruno-scarpa|Bruno Scarpa]]
- [[entities/oxford-university-press|Oxford University Press]]

## Source

- **Path:** `raw/creditmacro/Data Analysis and Data Mining An Introduction (Azzalini A., Scarpa B.) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:2d781fb8503063db8...`