---
title: "Temporal Cross-Fitting"
page_id: concepts/temporal-cross-fitting
page_type: concept
revision_id: 1
created: 2026-04-28T14:00:00Z
updated: 2026-04-28T14:00:00Z
tags: [time-series, cross-validation, machine-learning, causal-inference]
sources: [sources/koukorinis-2026-draci]
related: [concepts/doubly-robust-estimation, concepts/beta-mixing, concepts/causal-inference, concepts/conformal-prediction, concepts/adaptive-conformal-inference]
mind_map_priority: medium
---

# Temporal Cross-Fitting

**Temporal cross-fitting** (also called **temporal block cross-fitting**) is a technique for fitting nuisance models on time series data while preserving approximate independence between training and calibration sets. It extends standard cross-fitting from IID settings to temporally dependent data.

## The Problem

Standard **cross-fitting** (used in [[concepts/doubly-robust-estimation|Double Machine Learning]]) relies on independence between folds:
- Train nuisance models on fold $k$
- Calibrate/evaluate on fold $j \neq k$
- Independence ensures training errors don't affect calibration

Under temporal dependence, this breaks down:
- Random splitting creates look-ahead bias
- Adjacent observations remain correlated even when in different folds
- Standard cross-validation leaks future information

## Temporal Block Cross-Fitting

**Solution:** Partition the time series into **contiguous blocks** rather than random folds.

### Algorithm

1. **Block partition**: Divide $\{1, \ldots, T\}$ into $K$ contiguous blocks $\mathcal{B}_1, \ldots, \mathcal{B}_K$ of size $b = T/K$

2. **For each block $k$:**
   - Train nuisance models on $\mathcal{B}_{-k}$ (all blocks except $k$)
   - Evaluate/calibrate on $\mathcal{B}_k$

3. **Aggregate** results across all blocks

### Limitations

Even with temporal blocking:
- Observations at block boundaries are still correlated with training data
- [[concepts/beta-mixing|Beta-mixing]] dependence decays but doesn't vanish

## Guard Bands

[[sources/koukorinis-2026-draci|Koukorinis (2026)]] introduces **guard bands** to ensure approximate independence.

### Construction

When calibrating on block $k$:
1. Define guard band $\mathcal{G}_k$ = $g$ observations before and $g$ observations after $\mathcal{B}_k$
2. Train on $\mathcal{B}_{-k}^g = \{1, \ldots, T\} \setminus (\mathcal{B}_k \cup \mathcal{G}_k)$
3. The nearest training observation is at least $g$ steps from any calibration point

### Coupling Error

Under [[concepts/beta-mixing|beta-mixing]] with coefficient $\beta(k)$:

$$\text{Coupling error} = O\left(\beta(g)^{\delta/(2+\delta)}\right)$$

where $\delta > 0$ is the moment exponent from the moment bound assumption.

### Optimal Guard Band Size

The block size $b$ and guard band size $g$ trade off:
- **Larger $g$**: Better decorrelation (smaller $\beta(g)$)
- **Smaller $g$**: More training data (better nuisance estimation)

Optimal choice: $b \asymp g \asymp T^{1/(r+1)}$ where $r$ is the mixing rate.

In practice, setting $g = b$ (guard band equals block size) provides a simple default.

## Key Result: Product-Bias Preservation

The DML product-bias rate extends to beta-mixing data with guard bands:

$$|\mathbb{E}[\psi^{\mathrm{DR}} - \tau(X) \mid X]| \leq C \cdot \|\hat{e} - e\|_{2,k} \cdot \|\hat\mu - \mu\|_{2,k} + C' \cdot \beta(g)^{\delta/(2+\delta)}$$

This is **Lemma 2** in [[sources/koukorinis-2026-draci|DR-ACI]], the main technical contribution.

## Comparison with Standard Approaches

| Method | Data Type | Key Assumption | Issue with Dependence |
|--------|-----------|----------------|----------------------|
| Random K-fold | IID | Independence | Look-ahead bias |
| Leave-one-out | IID | Independence | Maximum leakage |
| Temporal blocks | Time series | Stationarity | Boundary correlation |
| Blocks + guards | Time series | Beta-mixing | Discards data |

## Applications

1. **Causal inference**: [[concepts/doubly-robust-estimation|Doubly robust estimation]] under dependence
2. **Conformal prediction**: [[concepts/conformal-prediction|CP]] calibration for time series
3. **Model selection**: Hyperparameter tuning without look-ahead bias
4. **Ensemble methods**: Training base learners on temporal folds

## Illustration

```
Time: ──────────────────────────────────────────────────►
      [████Block1████][====Guard====][████Block2████][====Guard====][████Block3████]

When calibrating Block2:
- Train on: Block1 + Block3 (NOT on Guard bands)
- Calibrate: Block2
- Temporal separation: ≥ g steps
```

## See Also

- [[concepts/doubly-robust-estimation|Doubly Robust Estimation]]
- [[concepts/beta-mixing|Beta-Mixing]]
- [[concepts/causal-inference|Causal Inference]]
- [[concepts/conformal-prediction|Conformal Prediction]]
- [[sources/koukorinis-2026-draci|DR-ACI Paper]]
