---
authors:
- Guillaume Maitrier
- Grégoire Loeper
- Jean-Philippe Bouchaud
content_hash: sha256:7b8597153df40bdb3102474b0b3494b249d2243985a79f63542050872156825b
created: 2026-08-13 00:00:00+00:00
page_id: sources/maitrier-2025-artificial-market-generator
page_type: source
related:
- concepts/square-root-law
- concepts/metaorder
- concepts/propagator-model
- concepts/price-impact
- entities/jean-philippe-bouchaud
- entities/guillaume-maitrier
- sources/maitrier-2026-square-root-impact-framework
revision_id: 1
schema_version: 2
source_hash: sha256:3c3e6fe0b2178a6ac74368b2328e0dd79826ecc0cc6689fc660a71e7471c4b0e
source_path: markdown_output/2509.05065.md
tags:
- square-root-law
- metaorder
- propagator-model
- simulation
- market-simulator
- price-impact
- econophysics
- proxy-metaorders
title: 'The Subtle Interplay between Square-root Impact, Order Imbalance & Volatility
  II: An Artificial Market Generator'
updated: '2026-08-13T00:00:00Z'
uuid: 486a5b9b-2fe1-56f7-9402-3a821ae64114
year: 2025
---

<!-- AUTHORED REGION START -->
# The Subtle Interplay between Square-root Impact, Order Imbalance & Volatility II: An Artificial Market Generator

## Summary

The simulation half of [[sources/maitrier-2026-square-root-impact-framework|the unifying framework]]. Its first job is defensive: the theory paper made analytical approximations its authors called strong and uncontrolled, and this paper simulates the model without them to check they hold. They do. Its second job is constructive — the simulator is released as a tool for generating synthetic order flow and prices at the mesoscopic scale.

The most consequential result is a side effect. Inside the synthetic market, where the true mapping from child orders to [[concepts/metaorder|metaorders]] is known exactly, **proxy metaorders reconstructed from anonymous trades alone reproduce the square-root law** — including its prefactor. That validates measuring metaorder impact from public tape data, long thought impossible.

## What Is Simulated

Metaorders are generated at Poisson rate $\nu$, each with a child volume $q$ drawn from a truncated lognormal $\mathcal{LN}(m, \sigma_\ell)$, a size $s$ from the $q$-dependent power law $\Psi_q$, a sign (optionally correlated across metaorders), and a unique start time that doubles as its identifier. Child orders arrive at participation rate $\phi$ and each carries impact under the generalized propagator, with $\beta_q = \beta_1 - \lambda' \log q$ so that large child orders decay more slowly.

Parameters are set close to the theory paper: $m \in \{3, 6\}$, $\sigma_\ell = 1$, $\lambda\sigma_\ell^2 = 1/8$, $\lambda' = 2\lambda$, $\mu_m = 1.5$, $\beta_m = 0.25$, constrained so $0 < \beta_q < 1$. A representative run is 10,000 metaorders over an eight-hour day.

The output is what the authors call an ideal dataset — comparable to the Tokyo Stock Exchange data that carries real trader identifiers — recording each child order with its metaorder ID, execution time and impact. That is precisely the data real markets do not publish.

## The Ablation Design

Five configurations isolate what each ingredient contributes, named by a triplet: **C** (correlation between metaorders), **VD** (volume dependence of $\mu_q$, $\beta_q$), **VF** (volume fluctuations), with N for negation.

```
NC-NVD-NVF  →  NC-NVD-VF  →  NC-VD-VF  →  C-NVD-VF  →  C-VD-VF
```

`C-VD-VF` is the fully realistic case. This is the clean part of the design: rather than asserting that cross-metaorder correlation restores diffusion, the simulation switches it off and shows what breaks.

## Results

Simulation reproduces, from parameters fitted on real data, all the empirical phenomena of the theory paper: the $q$-dependence of trade sign autocorrelation, the scaling of generalized order flow imbalance, diffusive prices, aggregated impact and anomalous rescaling, and — the theory's most distinctive prediction — the covariance and correlation structure between generalized order flow and returns. The approximations behind the analytical results are therefore quantitatively justified, not merely convenient.

## The Proxy Metaorder Result

Real metaorder impact studies need trader identifiers. Almost no one has them. Ref. [2] proposed reconstructing *proxy* metaorders from anonymous trades, and observed the surprising fact that randomly shuffling trading IDs in the TSE data and rebuilding synthetic metaorders still preserves the square-root law.

Here the algorithm is run inside the simulator, where ground truth is available. Two conditions turn out to be essential: the construction must **preserve the exact trade history** and **sample trades without replacement**.

The agreement between the true impact law (known exact child-to-metaorder matching) and the proxy-reconstructed one is close to perfect when $Q/V_D$ is not too small. It degrades toward linear at small $Q$, which is expected — short proxy metaorders are more likely to miss the true start, and the start is where impact is most concave. Crucially the prefactor $Y$ in $I(Q) = Y\sigma\sqrt{Q/V_D}$ is confirmed, which matters for cost estimation and is rarely checked.

## Availability

The code is published at `https://github.com/glatouille/ArtificialMarketSimulator.git`.

## What It Is Not

The authors are explicit about the boundaries.

- The model is **mesoscopic**. It does not represent the order book — only market orders exist; limit orders and cancellations are named as future work. Anything requiring book state is out of scope.
- Only long-term diffusive behaviour is calibrated; the short-term structure of the signature plot is not yet reproduced.
- Trader categories are homogeneous. Market makers, HFTs and slow institutions are not distinguished, though the authors expect they submit systematically different metaorders.
- The impact of proxy metaorders is confirmed numerically but **not computed analytically**, so the crossover between the square-root regime and the small-volume linear regime is not characterised.
- Some phenomenology remains unexplained by the underlying Latent Liquidity picture.

## Why This Belongs Next to the OFI Literature

The rest of the order flow imbalance work in this wiki — [[sources/cont-2023-cross-impact-ofi]], [[sources/sitaru-2023-decomposed-ofi]] — measures linear relations between book-level flow and returns on real data. This pair of papers works at the metaorder scale and argues those linear relations are the aggregate shadow of square-root impact from overlapping parent orders. The simulator is the bridge: it produces the metaorder-labelled data needed to test that claim, which no exchange feed supplies.

## Related

- [[sources/maitrier-2026-square-root-impact-framework]] — the theory this validates
- [[concepts/square-root-law]], [[concepts/metaorder]], [[concepts/propagator-model]]
- [[entities/guillaume-maitrier]], [[entities/jean-philippe-bouchaud]], Grégoire Loeper

## Citation

Maitrier, G., Loeper, G., & Bouchaud, J.-P. (2025). The Subtle Interplay between Square-root Impact, Order Imbalance & Volatility II: An Artificial Market Generator. arXiv:2509.05065, 8 September 2025.
<!-- AUTHORED REGION END -->