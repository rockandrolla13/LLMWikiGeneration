---
created: 2026-04-28 12:45:00+00:00
page_id: concepts/double-machine-learning
page_type: concept
related:
- concepts/back-door-front-door-adjustment
- concepts/conformal-prediction
- concepts/doubly-robust-estimation
- concepts/empirical-evaluation-causal-inference
revision_id: 3
sources:
- sources/koukorinis-2026-draci
tags:
- causal-inference
- machine-learning
- methodology
title: Double Machine Learning
updated: '2026-06-09T12:00:00Z'
---

# Double Machine Learning (DML)

## Definition

Double Machine Learning (DML) is a framework introduced by Chernozhukov et al. (2018) for causal inference that enables the use of machine learning methods for nuisance parameter estimation while maintaining valid statistical inference for target parameters.

## Core Ideas

### 1. Neyman Orthogonality

The moment condition for the target parameter is orthogonal (insensitive) to first-order perturbations in nuisance parameters. This means small errors in nuisance estimation have second-order effects on the target.

### 2. Cross-Fitting

Sample splitting where:
- Nuisance models trained on one fold
- Target estimation on held-out fold
- Results averaged across folds

This prevents overfitting bias that would arise from using the same data for both nuisance estimation and target inference.

### 3. Product-Bias Rate

For [[concepts/doubly-robust-estimation|doubly robust]] estimators, the bias is:

$$O(\|\hat{e} - e\|_2 \cdot \|\hat\mu - \mu\|_2)$$

If each nuisance converges at rate T^{-1/4}, the product converges at T^{-1/2}—fast enough for √T-consistent inference.

## Under Temporal Dependence

Standard cross-fitting assumes independence between folds, which fails for time series. [[sources/koukorinis-2026-draci|DR-ACI]] extends DML to β-mixing data via:

**Temporal block cross-fitting with guard bands:**
- Partition time series into contiguous blocks
- When calibrating on block k, exclude g adjacent observations (guard band)
- Train on remaining blocks

The coupling remainder under β-mixing is O(β(g)^{δ/(2+δ)}), where:
- g = guard band size
- δ = moment exponent
- β(g) = mixing coefficient at lag g

## Key Result

Under geometric β-mixing and standard nuisance convergence (ζ_e + ζ_μ > 1/2), the asymptotic rate matches the exchangeable (i.i.d.) case.

## Applications

- Treatment effect estimation with ML nuisance models
- Policy evaluation
- Heterogeneous treatment effects
- [[sources/koukorinis-2026-draci|Conformal inference for causal effects]]

## References

- Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., & Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. *The Econometrics Journal*.

## See Also

- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper]]
- [[concepts/beta-mixing|β-Mixing]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/back-door-front-door-adjustment|back-door-front-door-adjustment]]
- [[concepts/doubly-robust-estimation|doubly-robust-estimation]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/doubly-robust-estimation|doubly-robust-estimation]]
- [[concepts/empirical-evaluation-causal-inference|empirical-evaluation-causal-inference]]