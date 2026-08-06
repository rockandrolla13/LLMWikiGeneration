---
title: Kernel Methods
page_id: concepts/kernel-methods
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- nonparametric-statistics
- machine-learning
- hypothesis-testing
- rkhs
sources:
- sources/laumann-2021-kernel-tests-nonstationary
- sources/hastie-2009-elements-statistical-learning
- sources/lee-2024-kowcpi
- sources/gibbs-2023-conditional-guarantees
related:
- concepts/nadaraya-watson-estimator
- concepts/local-regression
- concepts/gaussian-processes
- concepts/kowcpi
mind_map_priority: medium
schema_version: 2
uuid: b0507785-bc85-50de-8096-ed499df9abff
content_hash: sha256:f0c279fe4e8b055cbe6d714dc2807d63a28a97465120c899356cc0fd49ff0a33
---

<!-- AUTHORED REGION START -->
# Kernel Methods

A family of techniques built on a kernel function k(x, x') that measures similarity between two points. The kernel appears in the wiki in three distinct roles, and they are worth keeping apart.

## Kernel as a Local Weight

The kernel decides how much each observation contributes to an estimate at a given point, with a bandwidth h setting the neighbourhood size. This is the [[concepts/nadaraya-watson-estimator|Nadaraya-Watson estimator]] of a conditional expectation, and more generally [[concepts/local-regression|nonparametric local regression]], which fits simple models inside kernel-weighted neighbourhoods and trades bias against variance through h.

Bandwidth choice is the whole game: the asymptotically optimal rate is h* ~ n^(−1/(w+4)) for w-dimensional conditioning, with cross-validation or a nonparametric AIC used in practice. The Epanechnikov kernel is the common choice. The theory requires the kernel to be nonnegative, bounded, continuous, compactly supported and symmetric.

[[concepts/kowcpi|KOWCPI]] uses the reweighted variant to learn data-adaptive weights for [[concepts/conformal-prediction|conformal prediction]] on time series ([[sources/lee-2024-kowcpi|Lee et al. 2024]]).

## Kernel as a Covariance Function

In [[concepts/gaussian-processes|Gaussian Processes]] the kernel *is* the model: it specifies the covariance between function values, and its choice fixes the smoothness of the posterior. The wiki's table covers the squared exponential (infinitely smooth), Matérn 3/2 and 5/2 (once and twice differentiable), and periodic kernels.

## Kernel as an Embedding into a Function Space

The kernel maps distributions into a reproducing kernel Hilbert space, where distances between embeddings become test statistics. [[sources/laumann-2021-kernel-tests-nonstationary|Laumann et al. (2021)]] use exactly this: MMD as the RKHS distance between two kernel mean embeddings for two-sample testing, and HSIC for independence testing. Characteristic kernels are what make the tests consistent; the Gaussian RBF with a median-heuristic bandwidth is the default.

Their contribution is dropping the i.i.d. assumption. Under alpha- or beta-mixing, block bootstrap (MMD) and wild bootstrap (HSIC) preserve the temporal structure and restore Type I error control, which classical tests lose under AR(1) dependence, a nonstationary mean, or time-varying variance.

The same RKHS idea underlies support vector machines — [[sources/hastie-2009-elements-statistical-learning|Hastie et al. (2009)]] describe the margin problem as penalised classification in an RKHS, with the kernel trick buying an implicitly infinite-dimensional feature map at the cost of an O(N³) quadratic programme — and appears in [[sources/gibbs-2023-conditional-guarantees|Gibbs et al. (2023)]] as the infinite-dimensional covariate-shift class.

## See Also

[[concepts/nadaraya-watson-estimator|Nadaraya-Watson Estimator]] · [[concepts/local-regression|Nonparametric Local Regression]] · [[concepts/gaussian-processes|Gaussian Processes]] · [[concepts/kowcpi|KOWCPI]] · [[concepts/conformal-prediction|Conformal Prediction]]

**Not yet written:** `concepts/mmd`, `concepts/hsic`, `concepts/reproducing-kernel-hilbert-space`, `concepts/support-vector-machines`, `concepts/nonstationarity`

<!-- AUTHORED REGION END -->
