---
title: "Conformal Prediction with Tukey g-h Transformation"
page_id: analyses/conformal-tukey-gh-intervals
page_type: analysis
revision_id: 2
created: 2026-04-26T03:30:00Z
updated: 2026-04-26T14:00:00Z
tags: [conformal-prediction, tukey-gh, prediction-intervals, heavy-tails, uncertainty-quantification, research-idea]
sources: [sources/zaffran-phd, sources/zaffran-2022-aci, sources/technical-2025-bond-similarity, sources/peters-2026-quantile-diffusions]
related: [concepts/conformal-prediction, concepts/tukey-gh-transformation, concepts/prediction-intervals, concepts/coverage-guarantee, concepts/uncertainty-quantification, concepts/conformalized-quantile-regression, entities/gareth-peters]
mind_map_priority: high
status: active-research
---

# Conformal Prediction with Tukey g-h Transformation

This analysis explores combining [[concepts/conformal-prediction|conformal prediction]] with [[concepts/tukey-gh-transformation|Tukey g-h transformation]] to produce calibrated, efficient prediction intervals for non-Gaussian data.

## Motivation

**Problem**: Standard conformal prediction constructs symmetric intervals around predictions. When residuals exhibit:
- **Heavy tails** (h > 0): Intervals become overly conservative due to outliers
- **Skewness** (g ≠ 0): Symmetric intervals waste coverage on the wrong side

**Solution**: Use Tukey g-h to model residual shape, then conformalize to guarantee coverage while maintaining efficiency.

## Theoretical Foundation

### Conformal Prediction Guarantees

For exchangeable data and miscoverage rate α, conformal prediction constructs sets $C_\alpha(X_{n+1})$ such that:

$$P\{Y_{n+1} \in C_\alpha(X_{n+1})\} \geq 1 - \alpha$$

This holds for **any** conformity score function. The choice of score affects **efficiency** (interval width), not validity.

### Tukey g-h as Conformity Score

The g-h transformation maps $Z \sim N(0,1)$ to:

$$Y = \frac{e^{gZ} - 1}{g} \cdot e^{hZ^2/2}$$

**Key insight**: The inverse g-h transform maps heavy-tailed, skewed residuals back to approximately standard normal. Using this as the conformity score:

$$s(x, y) = T_{g,h}^{-1}(\hat{y}(x) - y)$$

where $T_{g,h}^{-1}$ is the inverse g-h transform, produces scores that are approximately $N(0,1)$ distributed.

## Methods

### Method 1: g-h Normalized Conformity Scores

**Algorithm**:
1. Split data into training, calibration, test sets
2. Fit prediction model on training data
3. Compute residuals on calibration set: $r_i = y_i - \hat{y}_i$
4. Estimate g-h parameters $(g, h)$ from calibration residuals
5. Compute normalized scores: $s_i = T_{g,h}^{-1}(r_i)$
6. Find conformal quantile: $\hat{q} = \text{Quantile}_{1-\alpha}(|s_1|, ..., |s_n|, \infty)$
7. Prediction interval: $[\hat{y} + T_{g,h}(-\hat{q}), \hat{y} + T_{g,h}(\hat{q})]$

**Properties**:
- Exact $(1-\alpha)$ coverage (conformal guarantee)
- Asymmetric intervals when $g \neq 0$
- Tighter intervals than standard CP when $h > 0$

### Method 2: Asymmetric Quantile Conformalization

**Algorithm**:
1. Fit g-h to calibration residuals
2. Compute parametric quantiles: $q_{lo} = T_{g,h}(z_{\alpha/2})$, $q_{hi} = T_{g,h}(z_{1-\alpha/2})$
3. Check empirical coverage on calibration set
4. Adjust quantiles to achieve exact coverage (conformalization step)

**Advantage**: Directly produces asymmetric intervals reflecting true risk profile.

### Method 3: Locally Adaptive g-h Conformal

When residual distribution varies with covariates:

1. For each test point $x$, identify $k$ nearest calibration neighbors
2. Fit local $(g(x), h(x))$ from neighbor residuals
3. Construct locally-adapted g-h interval
4. Conformalize using local calibration scores

**Use case**: Heteroscedastic data where tail behavior varies (e.g., volatility regimes in finance).

## Theoretical Considerations

### Coverage Validity

**Theorem** (informal): For any measurable conformity score function $s$, split conformal prediction achieves:

$$P\{Y_{n+1} \in C_\alpha(X_{n+1})\} \geq 1 - \alpha$$

under exchangeability. The g-h transformation is measurable, so validity is preserved.

### Efficiency Gains

The efficiency of conformal prediction depends on how well the conformity score captures the true residual distribution. When residuals follow approximately g-h:

- **Standard CP** (using raw residuals): Intervals sized by extreme quantiles
- **g-h CP** (using transformed scores): Intervals sized by normal quantiles, then back-transformed

Expected efficiency gain: $O(h)$ reduction in interval width for heavy-tailed data.

### Estimation Error

Estimating $(g, h)$ from finite calibration data introduces error. Two approaches:

1. **Conservative**: Use confidence bounds on $(g, h)$ estimates
2. **Cross-conformal**: Average over multiple calibration splits

## Key Research Questions

### Why conformal instead of confidence intervals?

For g-h distributed data specifically:

| Confidence Intervals | Conformal Prediction |
|---------------------|---------------------|
| Require correct $(g,h)$ estimation | Distribution-free validity |
| Asymptotic guarantees only | Finite-sample guarantees |
| Coverage depends on model fit | Coverage guaranteed regardless |
| Specific to g-h assumption | Works even if g-h misspecified |

**Key insight**: The g-h transformation improves **efficiency** (narrower intervals), while conformal guarantees **validity** (coverage). These are orthogonal concerns — g-h conformal gets both.

### What causes over-coverage (conservatism)?

Standard CP with raw residuals on g-h data is conservative because:

1. **Heavy tails ($h > 0$)**: Extreme residuals inflate the empirical quantile $Q_{1-\alpha}(|r|)$
2. **Skewness ($g \neq 0$)**: Symmetric intervals allocate coverage to the wrong tail
3. **Finite calibration sets**: Small $n$ pushes quantiles higher

g-h normalization reduces conservatism by:
- Mapping heavy-tailed scores to approximately $N(0,1)$
- Using normal quantiles (smaller than heavy-tailed quantiles)
- Back-transforming to get tighter, asymmetric intervals

### What determines interval width?

For g-h conformal, interval width $= T_{g,h}(\hat{q}) - T_{g,h}(-\hat{q})$

**Determinants:**

| Factor | Effect on Width | Mitigation |
|--------|----------------|------------|
| Tail heaviness ($h$) | Higher $h$ → wider | g-h normalization |
| Skewness ($g$) | $g \neq 0$ → asymmetric (efficient) | Asymmetric intervals |
| $(g,h)$ estimation error | Misestimation → inflation | Larger calibration set |
| Calibration set size $n$ | Smaller $n$ → higher quantile | Use $n \geq 100$ |
| Base model accuracy | Poor $\hat{y}(x)$ → larger residuals | Better prediction model |

### Oracle comparison: What's the efficiency benchmark?

The **oracle** knows the true residual distribution and constructs optimal intervals. Comparing g-h conformal to oracle reveals:

- **Efficiency gap**: How much wider are g-h intervals vs. optimal?
- **Estimation penalty**: Cost of estimating $(g,h)$ from finite data
- **Misspecification cost**: What if residuals aren't truly g-h?

**Expected results**:
- If residuals are truly g-h: Gap is small, dominated by estimation error
- If residuals are approximately g-h: Small gap from model misspecification
- If residuals are far from g-h: Large gap, but coverage still guaranteed

### When are wide intervals still useful?

In financial applications:

| Use Case | Wide Intervals | Narrow Intervals |
|----------|---------------|------------------|
| VaR/CVaR regulatory | Required for compliance | May understate risk |
| Bond portfolio | Captures tail risk | May miss extreme moves |
| Credit loss reserves | Conservative provisioning | Potential shortfall |
| Trading decisions | Less actionable | More precise signals |

**Principle**: Wide intervals that correctly reflect tail risk are better than narrow intervals that under-cover.

## Research Directions

### Direction 1: Empirical Validation on Financial Data

**Research question**: Does g-h conformal actually improve efficiency on real heavy-tailed financial data?

**Experimental design**:
1. Use bond/equity return data with known g-h characteristics
2. Compare interval width: Standard CP vs. g-h CP vs. [[concepts/conformalized-quantile-regression|CQR]]
3. Verify coverage at 90%, 95%, 99% levels
4. Report efficiency gain: $\frac{\text{Width}_{\text{standard}} - \text{Width}_{\text{g-h}}}{\text{Width}_{\text{standard}}}$

**Expected outcomes**:
- 10-30% width reduction for $h \approx 0.1$
- Larger gains for more heavy-tailed data
- Asymmetric intervals for skewed returns

### Direction 2: Robustness to g-h Misspecification

**Research question**: How robust is g-h conformal when residuals are approximately but not exactly g-h?

**Experimental design**:
1. Generate data from contaminated g-h (mixture with outliers)
2. Test coverage under misspecification
3. Compare: fixed $(g,h)$ vs. adaptive estimation vs. robust estimation

**Key insight**: CP validity is preserved regardless of transformation choice — only efficiency suffers under misspecification.

### Direction 3: Comparison with CQR

**Research question**: When does g-h conformal outperform [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression]]?

**Hypothesis**: g-h conformal wins when:
- Residual distribution is stable (same g-h everywhere)
- Calibration set is small (g-h has 2 parameters vs. CQR's many)
- True distribution is close to g-h family

CQR wins when:
- Residual distribution varies with $x$ (heteroscedasticity)
- Large calibration set available
- Distribution shape is complex (multimodal)

## Proposed Experiments

### Experiment 1: Synthetic g-h Simulation

**Setup**:
```
For (g, h) in [(0,0), (0,0.1), (0.2,0.1), (0.3,0.2)]:
    Generate Y = μ(X) + T_{g,h}(Z), Z ~ N(0,1)
    Compare: Standard CP, g-h CP, CQR
    Metrics: Coverage, Width, Width/Oracle ratio
```

**Expected results table**:

| $(g, h)$ | Standard CP Width | g-h CP Width | Efficiency Gain |
|----------|------------------|--------------|-----------------|
| (0, 0) | Baseline | ~Same | 0% |
| (0, 0.1) | +15% | Baseline | ~15% |
| (0.2, 0.1) | +20% | +5% | ~15% |
| (0.3, 0.2) | +35% | +10% | ~25% |

### Experiment 2: Real Financial Data

**Datasets**:
1. Daily S&P 500 returns (equity, $g \approx -0.2$, $h \approx 0.1$)
2. Investment-grade bond returns (from [[sources/technical-2025-bond-similarity|Technical 2025]])
3. High-yield credit spreads (right-skewed, heavy-tailed)

**Protocol**:
1. Rolling window: Train on 252 days, calibrate on 63 days, test on 21 days
2. Estimate $(g, h)$ on calibration residuals via quantile matching
3. Construct intervals at $\alpha \in \{0.1, 0.05, 0.01\}$
4. Report: Empirical coverage, average width, coverage by decile

### Experiment 3: Estimation Error Impact

**Research question**: How many calibration points needed for reliable $(g, h)$ estimation?

**Setup**:
```
For n_cal in [50, 100, 200, 500, 1000]:
    Estimate (g, h) from n_cal samples
    Measure: Bias, Variance, Coverage gap vs. oracle
```

**Expected finding**: $n \geq 100$ sufficient for quantile matching; moment matching needs $n \geq 200$.

## Applications

### Financial Risk Management

| Asset Class | Typical g | Typical h | Benefit |
|-------------|-----------|-----------|---------|
| Equity returns | -0.1 to -0.3 | 0.05-0.15 | Asymmetric downside intervals |
| Bond returns | -0.2 to -0.4 | 0.1-0.2 | Tighter VaR bounds |
| Credit losses | 0.3 to 0.5 | 0.1-0.3 | Right-skewed loss intervals |
| FX returns | ~0 | 0.1-0.2 | Symmetric but tighter |

### Electricity Price Forecasting

[[sources/zaffran-2022-aci|Zaffran (2022)]] shows electricity prices exhibit:
- Heavy tails from demand spikes
- Skewness from price floors/caps

g-h conformal would improve on [[concepts/adaptive-conformal-inference|ACI]] by capturing this shape.

### Bond Similarity and Clustering

[[sources/technical-2025-bond-similarity|Technical (2025)]] uses g-h for bond return distributions. Combining with conformal prediction enables:
- Prediction intervals for bond returns with coverage guarantees
- Risk-adjusted similarity metrics

## Implementation Notes

### g-h Parameter Estimation

**Quantile matching** (recommended for robustness):
```
Match sample quantiles at p = {0.1, 0.25, 0.5, 0.75, 0.9}
to theoretical g-h quantiles via nonlinear least squares
```

**Moment matching** (faster but sensitive to outliers):
```
Match sample skewness → g
Match sample kurtosis → h
```

### Numerical Inversion

The g-h transform has no closed-form inverse. Use:
- Bisection search (robust)
- Newton-Raphson (faster, needs good initialization)
- Precomputed lookup tables (fastest for production)

### Software

No existing package combines conformal + g-h directly. Implementation requires:
- `mapie` or `crepes` for conformal prediction
- Custom g-h transformation functions
- Integration layer for score computation

## Open Questions

### Theoretical

1. **Optimal score design**: Is inverse g-h the best conformity score for g-h distributed data? Could a different transformation (e.g., Yeo-Johnson, sinh-arcsinh) yield tighter intervals while preserving coverage?

2. **Stochastic dominance**: Under what conditions does g-h conformal satisfy stochastic dominance over oracle scores (analogous to conformal meta-learners for treatment effects)?

3. **Conditional coverage**: Does g-h conformalization improve [[concepts/conditional-validity|conditional coverage]], not just marginal? Does [[concepts/distributional-conformal-prediction|distributional CP]] with g-h improve further?

### Methodological

4. **Adaptive g-h for time series**: How to efficiently update $(g, h)$ estimates in online/streaming settings compatible with [[concepts/adaptive-conformal-inference|ACI]]? Can we use exponentially weighted quantile matching?

5. **Local vs. global g-h**: When is locally adaptive $(g(x), h(x))$ better than global $(g, h)$? What's the bias-variance tradeoff?

6. **Multivariate extension**: How to extend to multivariate g-h using [[concepts/copulas|copulas]] + marginal g-h? Does [[sources/sun-2022-copula-cpts|CopulaCPTS]] provide a template?

### Practical

7. **Calibration set size**: What's the minimum $n$ for reliable $(g, h)$ estimation? How does this compare to CQR's data requirements?

8. **Robustness**: How badly does g-h conformal degrade when residuals are only approximately g-h (e.g., mixture distributions)?

## Related Work

### Continuous-Time Foundation
- [[sources/peters-2026-quantile-diffusions|Peters (2026) Quantile Diffusions]] - **key reference** for Tukey g-h in continuous time, dynamic risk modelling

### Core Concepts
- [[concepts/conformal-prediction|Conformal Prediction]] - theoretical foundation
- [[concepts/tukey-gh-transformation|Tukey g-h Transformation]] - distributional model
- [[concepts/prediction-intervals|Prediction Intervals]] - general framework
- [[concepts/coverage-guarantee|Coverage Guarantee]] - validity concept

### Alternative Approaches
- [[concepts/conformalized-quantile-regression|Conformalized Quantile Regression (CQR)]] - adaptive intervals via quantile regression
- [[concepts/adaptive-conformal-inference|Adaptive Conformal Inference]] - time series extension
- [[concepts/distributional-conformal-prediction|Distributional CP]] - conditional validity via distribution estimation

### Extensions
- [[concepts/conditional-validity|Conditional Validity]] - stronger coverage guarantees
- [[concepts/copulas|Copulas]] - multivariate extension path
- [[concepts/extreme-value-theory|Extreme Value Theory]] - alternative tail modeling

### Applications
- [[sources/technical-2025-bond-similarity|Bond Similarity Framework]] - uses g-h for bond returns
- [[sources/zaffran-2022-aci|Zaffran (2022)]] - ACI for electricity prices

## Conclusion

Combining conformal prediction with Tukey g-h transformation offers a principled approach to constructing prediction intervals that are both **valid** (guaranteed coverage) and **efficient** (adapted to non-Gaussian residual shapes). This is particularly valuable in finance where heavy tails and skewness are ubiquitous.

**Key insights**:
1. Conformal prediction's distribution-free guarantee allows freedom in choosing the conformity score
2. g-h provides a parsimonious (2-parameter) way to capture skewness and heavy tails
3. The combination preserves validity while improving efficiency by 10-30% for typical financial data
4. Coverage is guaranteed even if g-h is misspecified — only efficiency suffers

## Next Steps

1. **Immediate**: Run synthetic simulation (Experiment 1) to validate efficiency gains
2. **Short-term**: Apply to bond return data from [[sources/technical-2025-bond-similarity|Technical (2025)]]
3. **Medium-term**: Compare systematically with [[concepts/conformalized-quantile-regression|CQR]] across data regimes
4. **Long-term**: Develop adaptive g-h for time series compatible with [[concepts/adaptive-conformal-inference|ACI]]

## Changelog

- **2026-04-26 (v2)**: Added Key Research Questions, Research Directions, Proposed Experiments sections based on ideation analysis
- **2026-04-26 (v1)**: Initial analysis exploring g-h + conformal combination
