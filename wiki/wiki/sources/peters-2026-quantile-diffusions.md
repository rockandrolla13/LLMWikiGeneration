---
title: "Quantile Processes for Dynamic Risk Modelling in Finance and Insurance"
page_id: sources/peters-2026-quantile-diffusions
page_type: source
revision_id: 2
created: 2026-05-15T22:00:00Z
updated: 2026-05-24T20:15:00Z
tags: [quantile-diffusions, tukey-gh, stochastic-processes, risk-modelling, insurance, actuarial-science]
authors: ["Gareth W. Peters", "Andrea Macrina", "Holly Brannelly"]
year: 2026
related: [concepts/tukey-gh-transformation, analyses/conformal-tukey-gh-intervals, concepts/quantile-regression, concepts/extreme-value-theory]
mind_map_priority: high
revision_note: "An updated draft (April 26, 2026; first author rewrite dated 16.03.2026 noted in the document header) is staged at markdown_output/QD1_IME_March2026 (6) (1).md. The original draft (ingested 2026-05-15) and the April-26 revision share the same title, authors (Peters, Macrina, Brannelly), and Tukey g-h framework; the GWP-rewrite annotation suggests substantive revisions to specific sections rather than the full paper. A diff has not yet been performed — re-summarise this page if any new theoretical contribution or empirical result is identified."
---

# Quantile Processes for Dynamic Risk Modelling in Finance and Insurance

Peters, Macrina, and Brannelly (April 2026, two drafts in circulation including a 16.03.2026 first-author rewrite) develop a novel continuous-time framework for **Tukey g-h quantile diffusions**—stochastic processes whose marginal distributions are controlled through quantile transformations.

## Key Contributions

1. **Random-level quantile diffusions**: Scalar processes obtained by transforming a driving diffusion through a composite distribution–quantile map, yielding exact marginal control while inheriting serial dependence from the driver.

2. **Function-valued quantile diffusions**: Processes evolving in the space of quantile functions, where parameters (g, h) themselves follow diffusion dynamics.

3. **Tukey g-h parameterization**: Specialization to Tukey families with direct parameter interpretation:
   - A shifts location
   - B rescales
   - g governs relative skewness
   - h governs tail-thickening

4. **Dynamic distortion pricing**: Framework for distortion-based pricing using g-h induced measure changes for insurance and financial applications.

## The Tukey g-h Quantile Diffusion

**Definition**: For parameters A ∈ ℝ, B > 0, g ∈ ℝ, h ≥ 0, the Tukey g-h quantile function is:

$$Q_{\phi_{gh}}(u; A, B, g, h) = A + B \cdot \frac{e^{g x_u} - 1}{g} \cdot e^{h x_u^2/2}$$

where $x_u = \Phi^{-1}(u)$ is the standard normal quantile.

**Random-level construction**: The Tukey g-h quantile diffusion is:

$$Z_t = Q_{\phi_{gh}}(U_t; A, B, g, h)$$

where $U_t = F_Y(t, Y_t)$ is the random quantile level process from driving diffusion Y.

## Two Constructions

### Construction I: Random-Level Quantile Diffusions

- Scalar-valued process where randomness enters through quantile level
- True-law: $Z_t = Q_\zeta(F_Y(t, Y_t); \xi)$ gives exact target marginal
- False-law: Uses different CDF family for pushforward measure
- Preserves pathwise order at each time
- Copula invariance under monotone transforms

### Construction II: Function-Valued Quantile Diffusions

- Each time point yields an entire quantile curve
- Parameter vector follows diffusion: $d\xi_t = b(t, \xi_t)dt + \Sigma(t, \xi_t)dB_t$
- Quantile function process: $Z_t(u) = Q_\zeta(u; \xi_t)$
- Enables dynamic skewness and kurtosis modulation

## Key Theoretical Results

**Theorem 2.1** (Marginal Law): In true-law construction, for each t > t₀:
- $Z_t \stackrel{d}{=} \zeta_\xi$ (exact target distribution)
- Marginal distribution independent of t

**Proposition 2.4** (Copula Invariance): The copula of $(Z_{t_1}, ..., Z_{t_m})$ coincides with the copula of $(U_{t_1}, ..., U_{t_m})$ and hence with the copula of $(Y_{t_1}, ..., Y_{t_m})$.

**Proposition 2.6** (Itô Dynamics): Under smoothness assumptions, the quantile diffusion satisfies an explicit SDE derived via chain rule.

## Tukey Subfamilies

| Family | Parameters | Effect |
|--------|------------|--------|
| Tukey g | g only (h=0) | Skewness without tail change |
| Tukey h | h only (g=0) | Tail-thickening, symmetric |
| Tukey g-h | Both g, h | Full flexibility |

## Applications

### Insurance Reserve Risk

- Empirical application to aggregate paid-loss data
- Fitted OU driver with Tukey g-h marginal
- One-year-ahead predictive distributions for reserve deterioration
- Stop-loss pricing under quantile-induced measures

### Layer Pricing

- Compared PH, Wang, and Tukey-g distortions
- Tukey-g produces steeper layer premium increases
- Better captures asymmetric tail risk

### Dynamic Risk Measures

- VaR and TVaR as natural outputs
- Capital adequacy under Solvency II
- Catastrophe risk management

## Connection to [[analyses/conformal-tukey-gh-intervals|Conformal Prediction]]

This paper provides the **continuous-time foundation** for combining conformal prediction with Tukey g-h transformations:

1. **Conformity scores**: The inverse g-h transform can normalize residuals to approximately N(0,1), improving conformal prediction efficiency.

2. **Dynamic intervals**: Function-valued quantile diffusions enable time-varying prediction intervals with calibrated coverage.

3. **Tail-aware inference**: g-h parameterization allows direct control over interval asymmetry and width based on estimated tail behavior.

## Empirical Results

**Parameter Recovery** (Table 2): Synthetic experiments show accurate recovery of g, h parameters from simulated quantile diffusions.

**Insurance Data** (Table 6): Real loss data fitted with:
- g = -0.703 (left skew)
- h ≈ 0 (near-Gaussian tails on short series)

## Mathematical Framework

The paper distinguishes three classical notions from the proposed constructions:
1. Classical deterministic quantile curves $q_u(t) = Q_{X_t}(u)$
2. Quantiles of diffusion marginals
3. Fixed-level quantile dynamics

The new constructions are **constructive** rather than derived—starting from a target quantile family and building processes with prescribed marginal behavior.

## See Also

- [[concepts/tukey-gh-transformation|Tukey g-h Transformation]]
- [[analyses/conformal-tukey-gh-intervals|Conformal Prediction with Tukey g-h]]
- [[concepts/quantile-regression|Quantile Regression]]
- [[entities/gareth-peters|Gareth W. Peters]]
