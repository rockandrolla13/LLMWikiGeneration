---
title: Optimal Option Market Making and Volatility Arbitrage
page_id: sources/lucic-2024-option-market-making-vol-arbitrage
page_type: source
source_path: markdown_output/4729290.md
source_type: working-paper
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Vladimir Lucic
- Alex S. L. Tse
year: 2024
venue: Working paper (25 November 2024)
tags:
- market-making
- options
- volatility-arbitrage
- stochastic-control
- algorithmic-trading
sources: []
related:
- concepts/market-making
- concepts/avellaneda-stoikov-model
- concepts/stochastic-optimal-control
- concepts/implied-volatility-surface
- concepts/inventory-risk
- concepts/implied-volatility-skew
- concepts/limit-order-book
mind_map_priority: high
schema_version: 2
uuid: 808d56d5-c7a9-5032-9d08-2b8ab790d2c3
content_hash: sha256:85f4d574831e379c38089082144547bb22f294ac7dcd5481eb6e132ad5f60e06
---

<!-- AUTHORED REGION START -->
# Optimal Option Market Making and Volatility Arbitrage

**Authors:** Vladimir Lucic (Imperial College London; Marex), Alex S. L. Tse (University College London)

**Year:** 2024 · **Venue:** Working paper, dated 25 November 2024

## Summary

Most algorithmic market-making theory is built for delta-one instruments. This
paper extends the [[concepts/avellaneda-stoikov-model|Avellaneda-Stoikov]]
framework to options, and does so in a way that lets the market maker's own view
on volatility drive the quotes.

The setup: order arrivals are Cox processes with exponential intensity
lambda(delta) = lambda_0 e^{-kappa·delta}, so tighter quotes fill more often.
The market maker delta-hedges using the Black-Scholes delta computed from the
**implied** volatility, and marks positions to a given implied volatility
surface that is assumed static over the market-making horizon. Their subjective
volatility process is separate and may differ from that surface — which is
exactly where the edge comes from.

## Findings

Under a second-order approximation of the HJB equation, the optimal bid and ask
are available in closed form, and decompose into three economically readable
pieces:

1. the expected, penalty-discounted volatility arbitrage profit implied by the
   actual-versus-implied volatility differential — the gamma-theta carry, which
   scales with option gamma;
2. a term governed by the demand and supply elasticity `kappa`, i.e. how
   order flow responds to spread;
3. an [[concepts/inventory-risk|inventory]] adjustment tied to the penalty on
   running and residual positions.

Because gamma PnL is first-order here, the model differs from the stochastic
volatility treatments it cites, where market maker and market implicitly agree on
spot volatility and only vega PnL survives.

The approximation holds up. Compared against a finite-difference solution of the
original PDE, quotes differ by under 0.015% annualised implied volatility, and
the gap only becomes visible when the horizon runs past a full business day.

Extensions preserve tractability: hard position limits, general European
payoffs, simultaneous quoting of multiple options, and factor-based risk control
over custom buckets. The numerical section quotes a 44-instrument surface under
vega-bucket monitoring against zero-intelligence constant-spread quoting.

From the risk-reversal example: shocks to the implied volatility **skew** move
quotes far more than parallel shifts of the surface, since a delta-hedged long
risk reversal is effectively short skew and the two legs offset under a parallel
move.

## Caveats

The static implied volatility surface is the load-bearing assumption. It is
defensible for a horizon of hours, and the authors flag it as the main limitation
— particularly if one wants to extend to exotics. They also note the theoretical
admissibility of the strategies has not been examined rigorously.

## Open Questions

- What replaces the static-surface assumption without losing closed form?
- The order flow model is exponential-intensity by assumption; empirical work
  cited in the paper favours Hawkes-type arrival dynamics.

## See Also

[[concepts/market-making|Market Making]] ·
[[concepts/implied-volatility-surface|Implied Volatility Surface]] ·
[[concepts/implied-volatility-skew|Implied Volatility Skew]] ·
[[concepts/market-microstructure|Market Microstructure]] ·
[[concepts/hawkes-processes|Hawkes Processes]]

**Not yet written:** `gamma-theta-carry`, `vega-bucket-risk`,
`hamilton-jacobi-bellman-equation`, `delta-hedging`, `risk-reversal`.
<!-- AUTHORED REGION END -->

