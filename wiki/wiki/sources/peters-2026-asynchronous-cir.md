---
title: "Asynchronous Regime-Switching Multivariate CIR Spot-Rate Models via Onsager–Machlup Topological HMM Inference"
page_id: sources/peters-2026-asynchronous-cir
page_type: source
revision_id: 1
created: 2026-05-15T22:00:00Z
updated: 2026-05-15T22:00:00Z
tags: [cir-models, regime-switching, hmm, interest-rates, copulas, onsager-machlup]
authors: ["Gareth W. Peters", "Minxing Xu", "Zimo Zhu", "Peilun He"]
year: 2026
related: [concepts/state-space-models, concepts/copulas, entities/gareth-peters]
mind_map_priority: medium
---

# Asynchronous Regime-Switching Multivariate CIR Spot-Rate Models

Peters, Xu, Zhu, and He (April 2026) develop a multivariate spot-rate modelling framework where each rate follows CIR-type dynamics while regimes switch **asynchronously** across assets, with inference via Onsager-Machlup topological HMM.

## Key Contributions

1. **Asynchronous regime switching**: Each rate/factor has its own latent regime process, allowing different yield curve segments to respond to different drivers at different time scales.

2. **Onsager-Machlup (OM) emissions**: Replaces traditional HMM emission densities with path-likelihood surrogates derived from OM functionals.

3. **Scalable inference**: Coordinate-wise OM scoring with factorized transitions reduces complexity from O(∏Kⱼ) to O(d·K²·T).

4. **Copula dependence**: Exact CIR marginals coupled via Gaussian or Student-t copulas for tail dependence.

## Motivation

Empirically, yield curve segments respond differently:
- **Short maturities**: React sharply to monetary policy and liquidity
- **Long maturities**: Reflect slow-moving macro and risk-premium regimes

A single synchronous regime is too rigid—asynchronous switching captures this heterogeneity.

## Model Specifications

### Model A: Coordinate-wise CIR

Each component j conditional on regime $S_t^{(j)} = i_j$:

$$dX_t^{(j)} = \kappa_{i_j,j}(\theta_{i_j,j} - X_t^{(j)})dt + \sigma_{i_j,j}\sqrt{X_t^{(j)}}dB_t^{(j)}$$

With instantaneous correlation matrix $\rho_{\mathbf{S}_t}$ (potentially regime-dependent).

### Model B: Factor CIR

Low-dimensional CIR factors drive multiple rates:
$$X_t^{(j)} = \alpha^{(j)}_{\mathbf{S}_t} + \sum_{k=1}^r \beta^{(jk)}_{\mathbf{S}_t} Y_t^{(k)}$$

### Model C: Wishart Square-Root

Matrix-valued $V_t \in S_d^+$ with scalar rates $X_t^{(j)} = \langle A_j, V_t \rangle$.

## Asynchronous Regime Processes

For each asset j, define continuous-time Markov chain:
$$S^{(j)}_t \in \{1, ..., K_j\}$$

with generator $Q^{(j)}$ and transition matrix $A^{(j)}(\Delta) = \exp(Q^{(j)}\Delta)$.

**Key property**: If chains are independent, the joint configuration $\mathbf{S}_t = (S_t^{(1)}, ..., S_t^{(d)})$ factors:

$$\mathbb{P}(\mathbf{S}_{k+1} = \mathbf{j} | \mathbf{S}_k = \mathbf{i}) = \prod_{l=1}^d A^{(l)}_{i_l, j_l}$$

## Onsager-Machlup Functionals

The OM functional for multivariate diffusion path φ under configuration **i**:

$$\mathcal{I}_{\mathbf{i}}[\phi] = \frac{1}{2}\int_0^T \left[(\dot{\phi}_t - \mu_{\mathbf{i}}(\phi_t))^\top \Gamma_{\mathbf{i}}(\phi_t)^{-1}(\dot{\phi}_t - \mu_{\mathbf{i}}(\phi_t)) - \text{div}(\mu_{\mathbf{i}})\right]dt$$

Used as THMM emission cost: $\tilde{b}_{\mathbf{i}}(k) \propto \exp\{-I_{\mathbf{i}}(k)\}$.

### Coordinate-wise Approximation

For scalability:
$$I_{\mathbf{i}}^{\text{cw}}(k) = \sum_{j=1}^d I_{i_j}^{(j)}(k)$$

This decomposes across j, enabling d independent Viterbi problems.

### Robust Student-t OM

For outlier penalization:
$$I_{\mathbf{i}}^{t_\nu}(k) = \frac{d + \nu}{2}\log\left(1 + \frac{q_{\mathbf{i}}(k)}{\nu - 2}\right)$$

Heavy-tailed robustness for stress-period dynamics.

## Copula Coupling

After discretization, impose dependence via copulas:
$$\mathbf{U}_{k+1} = (U_{k+1}^{(1)}, ..., U_{k+1}^{(d)}) \sim C_{\mathbf{i}_k}$$

where $U_{k+1}^{(j)} = F_{i_j}^{\text{CIR}}(X_{k+1}^{(j)} | X_k^{(j)})$.

**Gaussian copula**: $C_{\mathbf{i}} = \text{GaussCop}(\rho_{\mathbf{i}})$

**Student-t copula**: $C_{\mathbf{i}} = \text{tCop}(\rho_{\mathbf{i}}, \nu_{\mathbf{i}})$—provides tail dependence for stress co-movements.

## Inference Algorithms

### Forward-Backward with OM Emissions

$$\alpha_{k+1}(\mathbf{j}) = \tilde{b}_{\mathbf{j}}(k+1) \sum_{\mathbf{i} \in \mathcal{K}} \alpha_k(\mathbf{i}) \prod_{l=1}^d A^{(l)}_{i_l, j_l}$$

### Viterbi Decoding

$$V_k(\mathbf{i}) = \max_{\mathbf{j}} \left[V_{k-1}(\mathbf{j}) + \log A(\mathbf{j}, \mathbf{i}) - I_{\mathbf{i}}(k)\right]$$

With coordinate-wise emissions, decomposes to O(dK²T).

## Swaption Calibration Example

**Panel of instruments**: ATM swaptions on grid (Te, Ts) ∈ {1Y, 5Y, 10Y} × {2Y, 5Y, 10Y}.

**Joint objective**:
$$\max_\Theta \left[\mathcal{L}_{\text{THMM}}(\Theta) - \lambda \sum_m w_m (\sigma_m^{\text{model}} - \sigma_m^{\text{mkt}})^2\right]$$

Alternating:
1. THMM/OM-driven EM for regime and CIR parameters
2. Derivative calibration for copula and mapping weights

## Connection to Tukey g-h Work

This paper and [[sources/peters-2026-quantile-diffusions|Peters (2026) Quantile Diffusions]] share:

1. **Author**: Gareth W. Peters
2. **OM functionals**: Both use Onsager-Machlup for path likelihoods
3. **Tail modeling**: Student-t robustification here, g-h tail control there
4. **Continuous-time focus**: Both develop rigorous continuous-time frameworks

## See Also

- [[sources/peters-2026-quantile-diffusions|Quantile Processes for Dynamic Risk Modelling]]
- [[concepts/state-space-models|State Space Models]]
- [[concepts/copulas|Copulas]]
- [[entities/gareth-peters|Gareth W. Peters]]
