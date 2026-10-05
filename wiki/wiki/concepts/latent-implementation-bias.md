---
abstraction_level: intermediate
concept_type: phenomenon
content_hash: sha256:f94c04a1ce525b1bc50c1313ad92e2d266a61490dc6ef1815b7012c794657d1a
created: '2026-10-05T15:52:32Z'
page_id: concepts/latent-implementation-bias
page_type: concept
related:
- concepts/bond-momentum
revision_id: 1
schema_version: 2
sources:
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
tags:
- corporate-bonds
- backtesting
- data-quality
title: Latent Implementation Bias
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: a409e4ff-ccbc-5a47-a965-17212c4fd5a8
---

<!-- AUTHORED REGION START -->
# Latent Implementation Bias

## Definition

Inflation of a corporate-bond strategy's measured premium that arises when the same noisy month-end transaction price is used both to compute the sorting signal and as the return's starting price, and when that price is not one an investor could trade at. Price errors then push bonds into the leg where their return error helps the strategy. Dickerson, Robotti and Rossetti (2026) remove it by gapping the two: compute the signal from an earlier price, or measure the return from the start of the next month.

## Sources

- [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|The Corporate Bond Factor Replication Crisis]]

## Related Concepts

- [[concepts/bond-momentum|Bond Momentum]]
<!-- AUTHORED REGION END -->