---
title: Conditional Validity
page_id: concepts/conditional-validity
page_type: concept
revision_id: 1
created: 2026-04-26 12:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- coverage-guarantee
- fairness
sources:
- sources/chernozhukov-2021-distributional-cp
- sources/yang-2026-multi-distribution-robust-cp
related:
- concepts/conformal-prediction
- concepts/coverage-guarantee
- concepts/distributional-conformal-prediction
- concepts/exchangeability
mind_map_priority: medium
schema_version: 2
uuid: cc31d8eb-be0e-5496-99b2-c8ff391c5906
content_hash: sha256:f718744f7a1781202bf07da968281553830d61973b70e595c7d1cd6b61900cf0
---

<!-- AUTHORED REGION START -->
# Conditional Validity

**Conditional validity** refers to the property of prediction sets having correct coverage probability conditional on the observed features (or other conditioning variables), rather than just on average across all possible feature values.

## Formal Definition

A prediction set Ĉ(X_{n+1}) is **conditionally valid** at level 1-α if:

> P(Y_{n+1} ∈ Ĉ(X_{n+1}) | X_{n+1} = x) = 1 - α for all x

This is a much stronger requirement than **unconditional (marginal) validity**:

> P(Y_{n+1} ∈ Ĉ(X_{n+1})) ≥ 1 - α

## Types of Conditional Validity

### Object Conditional
Coverage conditional on the test features X_{n+1}:
> P(Y_{n+1} ∈ Ĉ | X_{n+1})

This is what [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]] aims to achieve.

### Training Conditional
Coverage conditional on the training data:
> P(Y_{n+1} ∈ Ĉ | {(X_i, Y_i)}_{i=1}^n)

Split conformal prediction automatically achieves this.

### Label Conditional
Coverage conditional on the true label value:
> P(Y_{n+1} ∈ Ĉ | Y_{n+1} = y)

Important in classification for controlling false positive/negative rates.

### Group Conditional
Coverage conditional on group membership:
> P(Y_{n+1} ∈ Ĉ | G_{n+1} = g) for all groups g

Related to [[concepts/multi-distribution-robust-cp|multi-distribution robustness]] and fairness.

## Impossibility Result

A fundamental impossibility result (Vovk 2012; Lei & Wasserman 2014; Foygel Barber et al. 2021) states:

> Any prediction set satisfying P(Y ∈ Ĉ(X) | X = x) ≥ 1-α for **all** distributions has infinite Lebesgue measure with non-trivial probability.

Therefore, exact conditional validity is **not achievable** in a distribution-free manner. Methods like DCP achieve **approximate** conditional validity under modeling assumptions.

## Why Conditional Validity Matters

### Fairness
A prediction interval with only marginal validity might:
- Have 95% coverage overall
- Have 50% coverage for high-risk patients
- Have 100% coverage for low-risk patients

Conditional validity ensures equitable coverage across all subgroups.

### Heteroskedasticity
In regression with varying noise levels:
- Marginal validity: Same interval width everywhere
- Conditional validity: Wider intervals where variance is high

### Decision Making
When making decisions for specific individuals (not populations), we care about coverage **for that individual's characteristics**.

## Approaches to Conditional Validity

1. **[[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]**: Uses probability integral transform
2. **[[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]]**: Uses quantile estimates
3. **Locally-weighted conformal prediction**: Reweights calibration points
4. **Conditional density estimation**: Builds prediction sets from density estimates

## Trade-offs

| Validity Type | Distribution-Free? | Efficiency | Fairness |
|--------------|-------------------|------------|----------|
| Unconditional | Yes | Can be good | No guarantee |
| Conditional | No (approximate) | Optimal | Guaranteed |
| Group-conditional | Yes | Moderate | Yes |

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/distributional-conformal-prediction|Distributional Conformal Prediction]]
- [[sources/chernozhukov-2021-distributional-cp|Chernozhukov et al. (2021)]]

<!-- AUTHORED REGION END -->
