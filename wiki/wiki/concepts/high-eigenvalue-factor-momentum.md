---
title: High-eigenvalue factor momentum
page_id: concepts/high-eigenvalue-factor-momentum
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [factor-momentum, principal-components, asset-pricing, quant-equity, empirical-finance]
sources: [sources/ehsani-2022-factor-momentum-and-the-momentum-factor]
related: [concepts/principal-components-analysis, concepts/factor-timing, concepts/limits-to-arbitrage, concepts/risk-vs-mispricing]
mind_map_priority: medium
---

# High-eigenvalue factor momentum

**High-eigenvalue factor momentum** is the empirical finding that factor momentum concentrates in high-eigenvalue principal-component factors, i.e., those explaining more of the cross-section of returns. Momentum in the first 10 high-eigenvalue PCs subsumes momentum in lower-eigenvalue PCs (fully in the second half of the sample), consistent with the absence of near-arbitrage opportunities since arbitrageurs could otherwise harvest low-eigenvalue predictability without bearing factor risk.

## Overview

Extracting principal components from a set of factors, Ehsani and Linnainmaa find that timing the high-eigenvalue PCs on their prior returns is highly profitable — a strategy trading the first 10 PCs earns a five-factor alpha with t = 6.51 — while low-eigenvalue PCs contribute little, especially later in the sample. This ordering matters economically: predictable returns tied to high-eigenvalue factors cannot be arbitraged away without taking on substantial common-factor risk, whereas predictability in near-idiosyncratic low-eigenvalue factors would represent a near-arbitrage that competitive traders should eliminate. The pattern is what the [[concepts/sentiment-persistence-factor-autocorrelation|sentiment-persistence mechanism]] predicts.

## Sources

- [[sources/ehsani-2022-factor-momentum-and-the-momentum-factor]] — builds PC-factor momentum strategies and shows momentum concentrates in high-eigenvalue components.

## Related Concepts

- [[concepts/principal-components-analysis]]
- [[concepts/factor-timing]]
- [[concepts/limits-to-arbitrage]]
- [[concepts/risk-vs-mispricing]]
