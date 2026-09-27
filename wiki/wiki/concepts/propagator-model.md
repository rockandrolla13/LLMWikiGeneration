---
content_hash: sha256:4cfd079eb548dd5a7cdd31eb269b663ddce33ef54b59c5f70a158ebc877d762f
created: 2026-08-13 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/propagator-model
page_type: concept
related:
- concepts/square-root-law
- concepts/metaorder
- concepts/price-impact
- concepts/order-flow
- concepts/limit-order-book
revision_id: 1
schema_version: 2
sources:
- sources/maitrier-2026-square-root-impact-framework
- sources/maitrier-2025-artificial-market-generator
- sources/mans-2025-en-lokalt-konkav-och-transient-prispaverkningsmodell
tags:
- propagator-model
- price-impact
- metaorder
- long-memory
- diffusivity
- econophysics
title: Propagator Model
updated: '2026-09-27T01:47:00Z'
uuid: a913ad39-bce7-59d2-bebd-ee237ce64dc6
---

<!-- AUTHORED REGION START -->
# Propagator Model

A model of price formation in which the price is a sum of the decaying influences of every past trade. Each order leaves an impression on the price that fades according to a kernel — the *propagator* — and the observed price is the superposition.

Its purpose is to resolve a specific tension: order flow has **long memory**, so if each trade had permanent impact prices would trend far more than they do. Decaying impact and persistent flow offset each other, and the balance is what produces diffusive prices.

## The Generalized Version

[[sources/maitrier-2026-square-root-impact-framework|Maitrier & Bouchaud (2025)]] extend the classical construction to carry three features of [[concepts/metaorder|metaorder]] impact simultaneously:

1. Impact grows as the **square root of the number of child orders executed**.
2. **Peak impact** at end of execution depends only on the square root of total volume traded.
3. Impact then **decays as a slow power law** of time.

The impact of a child order of volume $q$ executed at $t'$ on the price at $t > t'$, for a metaorder started at $t = 0$, is specified with constants $\theta$, $n_0$, $\tau_0$ and participation rate $\phi$, with $\theta(q) \propto \sqrt{q}$ taken from the double square-root law.

The decay exponent that emerges is $\beta = 1/2$ — **different from both the classical propagator model and the LLOB (latent liquidity) model**. That difference is the reason a generalized propagator is needed rather than the standard one.

Two exponents are made size-dependent, linear in $\log q$: $\mu_q = \mu_1 + \lambda \log q$ (large child orders are less persistent) and $\beta_q = \beta_1 - \lambda' \log q$ (their impact decays more slowly).

## What Restores Diffusion

The classical propagator gets diffusion from the long memory of order signs *within* the flow. With transient square-root impact, that is not enough — the power-law tail of metaorder durations alone yields **sub-diffusion**.

Diffusion is recovered when the signs of *distinct* metaorders are long-range correlated, contributing price variance scaling as $T^{2-\gamma_\times-2\beta}$ and giving diffusion at $\gamma_\times \simeq 1 - 2\beta$. The authors conjecture that intra- and cross-metaorder child-order correlations decay in roughly the same way, which would explain why proxy metaorder reconstruction from public data works at all.

This prediction is empirically falsifiable with datasets carrying trader identifiers.

## Implementation

The framework is analytically awkward but numerically straightforward. [[sources/maitrier-2025-artificial-market-generator|The companion paper]] simulates it directly, confirms the analytical approximations hold quantitatively, and publishes the simulator. Its ablation design switches metaorder correlation, volume dependence and volume fluctuation on and off separately, which is how the necessity of cross-metaorder correlation is demonstrated rather than asserted.

The model is **mesoscopic**: it represents market orders and their impact, not the order book. Limit orders and cancellations are absent, which bounds what it can be used for.

## Related

- [[concepts/square-root-law]], [[concepts/metaorder]], [[concepts/price-impact]]
- [[concepts/order-flow]] — the long memory the propagator exists to reconcile with diffusion
- [[concepts/limit-order-book]] — the layer below what this model represents
<!-- AUTHORED REGION END -->