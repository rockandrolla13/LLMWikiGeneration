---
created: 2026-04-26 12:00:00+00:00
mind_map_priority: medium
page_id: concepts/missing-data-imputation
page_type: concept
related:
- concepts/conformal-prediction
- concepts/heteroskedasticity
- concepts/ip-weighting-marginal-structural-models
- concepts/mask-conditional-validity
- entities/julie-josse
revision_id: 2
sources:
- sources/zaffran-2023-conformal-missing
tags:
- missing-data
- imputation
- statistics
- machine-learning
- conformal-prediction
title: Missing Data Imputation
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: 44153a21-3356-588c-b0fc-9133aff48796
content_hash: sha256:3e2abdb1bc17daa6e0cfcef391e5c342c22c7552b5967b4c5b784c8bd7797ed6
---

<!-- AUTHORED REGION START -->
# Missing Data Imputation

**Missing data imputation** refers to methods for filling in missing values in datasets, enabling analysis with standard algorithms that require complete data.

## Missingness Mechanisms (Rubin, 1976)

Understanding why data is missing is crucial for choosing appropriate methods.

### Missing Completely At Random (MCAR)

P(M = m | X) = P(M = m)

The probability of missing depends on neither observed nor unobserved values. Example: random sensor failures.

### Missing At Random (MAR)

P(M = m | X) = P(M = m | X_obs(m))

The probability of missing depends only on observed values. Example: patients with certain conditions more likely to have additional tests.

### Missing Not At Random (MNAR)

Otherwise. Missing depends on the unobserved values themselves. Example: high-income individuals less likely to report income.

## Imputation Methods

### Simple Methods

- **Mean/Median imputation**: Replace missing values with column average
- **Mode imputation**: For categorical variables
- **Constant imputation**: Replace with fixed value (e.g., 0)

### Model-Based Methods

- **Regression imputation**: Predict missing values from observed features
- **k-NN imputation**: Use values from similar complete observations
- **MICE** (Multiple Imputation by Chained Equations): Iterative regression

### Advanced Methods

- **Matrix factorization**: Low-rank approximations
- **Deep learning**: Autoencoders, GANs for imputation
- **Optimal transport**: Transport-based imputation

## Impute-Then-Predict Strategies

A common workflow:
1. Impute missing values in training data
2. Train model on imputed data
3. Impute test data and predict

### Theoretical Results

[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] and Le Morvan et al. (2021) established:

- **Bayes consistency**: For almost all imputation functions, a universally consistent learner on imputed data achieves Bayes-optimal predictions
- **No distributional assumptions required**: Results hold for any missingness mechanism

## Interaction with Conformal Prediction

### Marginal Validity Preserved

[[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] proved that conformal prediction on imputed data maintains marginal coverage:

P(Y ∈ Ĉ_α(X, M)) ≥ 1 - α

This holds for:
- **Any** symmetric imputation method
- **Any** missingness mechanism (MCAR, MAR, MNAR)

### Symmetric Imputation (Assumption A2)

An imputation function Φ is symmetric if the imputation algorithm treats data points symmetrically:

I((X^(σ(k)), M^(σ(k)))_{k=1}^{n+1}) = I((X^(k), M^(k))_{k=1}^{n+1})

for any permutation σ. This is satisfied by all standard imputation methods.

### Key Insight: Exchangeability Preservation

**Lemma**: If data is exchangeable and imputation is symmetric, then imputed data is also exchangeable.

This enables applying standard conformal prediction theory.

## Induced Heteroskedasticity

**Critical finding**: Even with homoskedastic noise, missing values create **heteroskedastic** predictions.

For a Gaussian linear model Y = β^T X + ε:

Oracle interval length: L*_α(m) ∝ √(β_mis(m)^T Σ_{mis|obs} β_mis(m) + σ²_ε)

- Uncertainty increases when **predictive variables** are missing
- Different missing patterns require different interval widths
- Standard methods fail to adapt to this heteroskedasticity

## Practical Implications

1. **Concatenate mask to features**: Allows models to adapt to missing patterns
2. **Use quantile regression**: Handles heteroskedasticity better than mean regression
3. **Consider mask-conditional validity**: See [[concepts/mask-conditional-validity|MCV]]

## Software

- **scikit-learn**: SimpleImputer, IterativeImputer
- **missMDA** (R): PCA/MCA with missing values
- **fancyimpute** (Python): Various advanced methods
- **mice** (R): Multiple imputation

## Key References

- Rubin (1976) - Missing data mechanisms taxonomy
- Le Morvan et al. (2021) - Consistency of impute-then-predict
- [[sources/zaffran-2023-conformal-missing|Zaffran et al. (2023)]] - Conformal prediction with missing values

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/mask-conditional-validity|Mask-Conditional Validity]]
- [[concepts/heteroskedasticity|Heteroskedasticity]]
- [[entities/julie-josse|Julie Josse]] - Leading researcher in missing data

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/ip-weighting-marginal-structural-models|ip-weighting-marginal-structural-models]]
<!-- AUTHORED REGION END -->
