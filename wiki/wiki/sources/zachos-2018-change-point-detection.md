---
title: 'Bayesian On-line Change-point Detection: Spatio-temporal point processes'
page_id: sources/zachos-2018-change-point-detection
page_type: source
source_type: dissertation
revision_id: 1
created: 2026-04-25 22:00:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Ioannis Zachos
year: 2018
venue: University of Warwick BSc Thesis
tags:
- change-point-detection
- bayesian-inference
- point-processes
- spatio-temporal
- machine-learning
related:
- concepts/change-point-detection
- concepts/bayesian-inference
- concepts/point-processes
- concepts/poisson-process
mind_map_priority: medium
schema_version: 2
uuid: ac98b369-0cb5-54ec-82e6-f6378d6d1097
content_hash: sha256:7c2833bdf8c46e3999afcbe4ef88acf2816ab79d530b5e928b540ff36bb20765
---

<!-- AUTHORED REGION START -->
# Bayesian On-line Change-point Detection

**Author:** Ioannis Zachos

**Year:** 2018

**Venue:** BSc Data Science Thesis, University of Warwick

**Supervisor:** Dr. Theodoros Damoulas

## Summary

This thesis develops an approach for on-line (real-time) Bayesian change-point detection (CPD) in spatio-temporal settings. The goal is to detect changes in mean, variance, and covariance of time series while providing step-ahead predictions and partitioning the series into disjoint segments.

## Key Contributions

### 1. BOCDMS Algorithm
- Bayesian On-line Change-point Detection and Model Selection
- Linear computational and storage complexity in observations
- Real-time processing capabilities
- Simultaneously performs detection and model selection

### 2. Conjugate Point Process Models
- Poisson-Gamma (PG) model for count data
- Multinomial-Dirichlet (MD) model for categorical data
- Sensitivity analysis for both models
- Performance comparison on synthetic data

### 3. Real-world Applications
- Chicago crime data
- UK property transactions
- Cryptocurrency transactions

## Methodology

### Framework
- Data modeled as samples from a data-generating process
- Probability distribution used as model
- Most likely model chosen at each time step
- Bayesian inference for parameter updates

### Key Components
- Prior beliefs specification
- Useful recursions for efficient computation
- Prediction and segmentation procedures
- Hyper-parameter tuning methods

## Experimental Results

### Synthetic Data
- Four synthetic datasets tested
- Model sensitivity and performance assessed
- Comparison between PG and MD models

### Real-world Performance
- Crime data: temporal change detection in Chicago
- Property: UK transaction pattern changes
- Crypto: Bitcoin/Ethereum transaction anomalies

## Key Claims

1. Linear complexity makes real-time detection feasible
2. Conjugate models enable efficient Bayesian updates
3. Model selection can be integrated with change detection
4. Approach generalizes across different data types

## See Also

- [[concepts/change-point-detection|Change-point Detection]]
- [[concepts/bayesian-inference|Bayesian Inference]]
- [[concepts/point-processes|Point Processes]]

<!-- AUTHORED REGION END -->
