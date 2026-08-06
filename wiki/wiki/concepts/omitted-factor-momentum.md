---
title: Omitted-factor momentum
page_id: concepts/omitted-factor-momentum
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [factor-momentum, momentum, asset-pricing, factor-models, empirical-finance]
sources: [sources/ehsani-2022-factor-momentum-and-the-momentum-factor]
related: [concepts/residual-momentum, concepts/factor-models, concepts/cross-sectional-momentum]
mind_map_priority: medium
---

# Omitted-factor momentum

**Omitted-factor momentum** is spurious momentum appearing in estimated residuals when an investor's asset-pricing model omits autocorrelated factors, even when true firm-specific returns are IID. If omitted factors are more autocorrelated than included ones, residuals display more momentum than raw returns, so residual-momentum profitability is an omitted-variables artifact rather than evidence of firm-specific continuation.

## Overview

The paper formalizes why [[concepts/residual-momentum|residual momentum]] can exceed raw-return momentum. When an estimated model excludes autocorrelated factors, those factors leak into the residuals, injecting the very momentum the residualization was meant to remove. Simulations with IID firm-specific returns reproduce the empirical pattern that CAPM residual momentum is strongest and profitability declines as more factors are added to the model. This makes residual momentum a diagnostic of model incompleteness rather than proof of stock-specific return continuation.

## Sources

- [[sources/ehsani-2022-factor-momentum-and-the-momentum-factor]] — derives the omitted-factor mechanism analytically and confirms it in simulation and actual data.

## Related Concepts

- [[concepts/residual-momentum]]
- [[concepts/factor-models]]
- [[concepts/cross-sectional-momentum]]
