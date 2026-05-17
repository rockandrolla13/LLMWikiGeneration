---
title: "Gegenbauer Processes"
page_id: concepts/gegenbauer-processes
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [time-series, long-memory, spectral-analysis, econometrics]
sources: [sources/technical-2025-bond-similarity]
related: [concepts/nelson-siegel-model, concepts/state-space-models]
mind_map_priority: low
---

# Gegenbauer Processes

Gegenbauer processes (also called Gegenbauer long-memory or GARMA processes) generalize ARFIMA models by allowing long-memory behavior at non-zero frequencies.

## Motivation

Standard ARFIMA captures long memory at frequency zero (persistent trends). Many economic series exhibit:
- Cyclical persistence (business cycles)
- Seasonal long memory
- Spectral peaks away from origin

## Definition

The Gegenbauer polynomial is:

$$G_n(d, u) = \sum_{k=0}^{n} \binom{d}{k}\binom{d}{n-k}(-1)^k u^{n-2k}$$

A Gegenbauer process $X_t$ satisfies:

$$(1 - 2u B + B^2)^d X_t = \epsilon_t$$

Where:
- $B$ is the backshift operator
- $u = \cos(\lambda)$, with $\lambda$ the Gegenbauer frequency
- $d$ is the memory parameter
- $\epsilon_t$ is white noise

## Spectral Density

The spectral density has a pole at frequency $\lambda$:

$$f(\omega) \propto |1 - 2\cos(\lambda)e^{-i\omega} + e^{-2i\omega}|^{-2d}$$

This creates persistent cyclical behavior.

## Special Cases

| Parameters | Model |
|------------|-------|
| $\lambda = 0$ ($u = 1$) | ARFIMA(0,d,0) |
| $\lambda = \pi$ ($u = -1$) | Anti-persistent |
| $d = 0$ | White noise |
| $0 < \lambda < \pi$ | Cyclical long memory |

## Applications

- **Business cycle analysis**: Persistent cycles in GDP
- **Financial volatility**: Long-memory in squared returns
- **Bond yields**: Cyclical patterns in term structure
- **Seasonal adjustment**: Long-memory seasonality

## See Also

- [[concepts/nelson-siegel-model|Nelson-Siegel Model]]
- [[concepts/state-space-models|State-Space Models]]
- [[sources/technical-2025-bond-similarity|Bond Similarity Framework (2025)]]
