---
title: Momentum-neutral factors
page_id: concepts/momentum-neutral-factors
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [factor-momentum, momentum, asset-pricing, quant-equity, empirical-finance]
sources: [sources/ehsani-2022-factor-momentum-and-the-momentum-factor]
related: [concepts/factor-models, concepts/cross-sectional-momentum, concepts/residual-momentum, concepts/fama-french-factors]
mind_map_priority: medium
---

# Momentum-neutral factors

**Momentum-neutral factors** are factors whose weights are twisted as little as possible to be orthogonal to stocks' past returns (weights equal residuals from a cross-sectional regression of original factor weights on prior returns), removing any incidental bet on individual-stock momentum. They correlate ~0.99 with original factors yet exhibit MORE momentum, and factor momentum in momentum-neutral factors subsumes standard factor momentum, showing incidental momentum explains none of factor-momentum profits.

## Overview

To rule out the objection that factor momentum is merely an accidental byproduct of factors happening to load on past winners and losers, Ehsani and Linnainmaa reconstruct each factor with weights orthogonalized against stocks' prior returns. These momentum-neutral factors remain almost perfectly correlated with the originals but, if anything, exhibit stronger momentum. Because factor momentum built from momentum-neutral factors subsumes the standard version, the authors conclude that factor momentum is a genuine property of factor returns, not a reflection of the individual-stock momentum embedded in factor weights.

## Sources

- [[sources/ehsani-2022-factor-momentum-and-the-momentum-factor]] — constructs momentum-neutral factors and shows their momentum subsumes standard factor momentum.

## Related Concepts

- [[concepts/factor-models]]
- [[concepts/cross-sectional-momentum]]
- [[concepts/residual-momentum]]
- [[concepts/fama-french-factors]]
