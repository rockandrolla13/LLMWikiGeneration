---
title: Split Conformal Prediction
page_id: concepts/split-conformal-prediction
page_type: concept
revision_id: 1
created: 2026-04-10 18:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- conformal-prediction
- uncertainty-quantification
- computational-efficiency
sources:
- sources/zaffran-phd
- sources/zaffran-2022-aci
- sources/johnstone-2025-multioutput
related:
- concepts/conformal-prediction
- concepts/calibration
- concepts/prediction-intervals
- concepts/coverage-guarantee
mind_map_priority: high
schema_version: 2
uuid: 68e688f7-5f79-5070-a7d9-2ea8e8ac9f08
content_hash: sha256:9d0ff973c829efda88af6989904f43c4bb54417087aadcef29f4c66364078d16
---

<!-- AUTHORED REGION START -->
# Split Conformal Prediction

**Split Conformal Prediction (SCP)** is a computationally efficient variant of [[concepts/conformal-prediction|conformal prediction]] that achieves finite-sample validity guarantees by splitting the training data into a proper training set and a calibration set.

## Algorithm

1. **Split**: Divide training data into two disjoint sets:
   - Proper training set (Tr): Used to fit the predictive model
   - Calibration set (Cal): Used to compute conformity scores

2. **Train**: Fit a regression model μ̂ on the proper training set

3. **Calibrate**: Compute conformity scores on the calibration set:
   - Typically: sᵢ = |μ̂(xᵢ) - yᵢ| (absolute residuals)

4. **Quantile**: Compute the corrected (1-α)-th quantile of the calibration scores

5. **Predict**: For new point xₙ₊₁, output interval:
   - Ĉₐ(xₙ₊₁) = [μ̂(xₙ₊₁) ± Q̂₁₋ₐ(Scal)]

## Advantages

- **Computational efficiency**: Model is trained only once (vs. O(n) times for full CP)
- **Model-agnostic**: Works with any underlying predictor
- **Simple implementation**: Easy to add to existing ML pipelines
- **Finite-sample validity**: Guarantees hold exactly, not asymptotically

## Limitations

- **Data inefficiency**: Part of the data is used only for calibration
- **Requires [[concepts/exchangeability|exchangeability]]**: Not directly applicable to time series
- **Marginal coverage**: Guarantees are marginal, not conditional on X

## Extensions

- **Conformalized Quantile Regression (CQR)**: Uses quantile regression for heteroskedastic data
- **[[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]]**: Extends SCP to handle distribution shift
- **Weighted conformal prediction**: Handles covariate shift

## Key References

- Lei et al. (2018): Formalized split conformal for regression
- Papadopoulos et al. (2002): Original "inductive" conformal prediction
- Romano et al. (2019): Conformalized quantile regression

## See Also

- [[concepts/conformal-prediction|Conformal Prediction]]
- [[concepts/coverage-guarantee|Coverage Guarantee]]
- [[concepts/calibration|Calibration]]

<!-- AUTHORED REGION END -->
