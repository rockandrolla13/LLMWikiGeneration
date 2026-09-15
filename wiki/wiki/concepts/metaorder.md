---
content_hash: sha256:12a810dddb0c7f21f9be8a150b91337f1fa0f86aa5455e91c6d031402da4f77a
created: 2026-08-13 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/metaorder
page_type: concept
related:
- concepts/square-root-law
- concepts/propagator-model
- concepts/price-impact
- concepts/order-flow
- concepts/optimal-execution
revision_id: 1
schema_version: 2
sources:
- sources/maitrier-2026-square-root-impact-framework
- sources/maitrier-2025-artificial-market-generator
tags:
- metaorder
- order-splitting
- long-memory
- price-impact
- square-root-law
- market-microstructure
title: Metaorder
updated: '2026-08-13T00:00:00Z'
uuid: 853eabae-05a7-5de0-95d6-820e7849b396
---

<!-- AUTHORED REGION START -->
# Metaorder

A single trading decision — buy 500,000 shares — executed as a long sequence of small **child orders** over minutes or hours. Almost all institutional volume arrives this way. The metaorder, not the individual trade, is the unit at which [[concepts/price-impact|price impact]] has a clean empirical law.

## Why It Is the Right Unit

Individual trades are fragments of intentions. Their signs are strongly autocorrelated precisely *because* they are fragments: a large parent order being worked over an hour emits same-signed children throughout. Lillo, Mike & Farmer showed that a power-law distribution of metaorder sizes, $\Psi(s) \propto s^{-1-\mu}$, generates exactly the observed long memory of order signs, with $\gamma = \mu - 1$ — a relation validated in detail by Sato & Kanazawa on Tokyo Stock Exchange data.

So the long memory of [[concepts/order-flow|order flow]] is not a separate stylized fact requiring its own explanation. It is a consequence of order splitting.

At the metaorder level, impact follows the [[concepts/square-root-law|square-root law]]: peak impact depends on total volume executed and not on how long execution took, then decays.

## The Identification Problem

Metaorders are not observable in public data. An exchange feed shows anonymous trades; it does not say which belong to the same parent. This is the central practical obstacle in impact research — it is why most metaorder studies rely on broker records, the ANcerno database, or exchange datasets that carry trader identifiers such as the Tokyo Stock Exchange's.

**Proxy metaorders** are the workaround: reconstruct plausible parents from the anonymous tape by a mapping rule. This was long thought hopeless. Two results suggest it is not. Randomly shuffling trading IDs in the TSE data and rebuilding synthetic metaorders still preserves the square-root law. And [[sources/maitrier-2025-artificial-market-generator|Maitrier, Loeper & Bouchaud (2025)]] validate the procedure inside a simulated market where the true parent-child mapping is known, recovering both the law and its prefactor — provided the construction preserves exact trade history and samples trades without replacement. Agreement degrades toward linear impact at small $Q/V_D$, because short proxy metaorders tend to miss the true start where impact is most concave.

## Heterogeneity That Matters

[[sources/maitrier-2026-square-root-impact-framework|Maitrier & Bouchaud (2025)]] find the exponents governing metaorder behaviour depend on child order size $q$:

- **Large child orders are less persistent** — the duration tail exponent $\mu_q$ increases with $\log q$.
- **Their impact decays more slowly** — the decay exponent $\beta_q$ decreases with $\log q$.

This is why sign imbalance ($a=0$) and volume imbalance ($a=1$) scale differently with window size, and it generates the non-monotonic and hump-shaped predictions their framework is tested on.

## Correlation Between Metaorders

Metaorders are correlated with each other, not merely internally. This turns out to be necessary to recover diffusive prices when impact is transient — see [[concepts/square-root-law]]. Whether that correlation reflects shared signals, market makers unwinding inventory, or anticipation of other participants is unresolved.

## Related

- [[concepts/square-root-law]], [[concepts/propagator-model]], [[concepts/price-impact]]
- Researchers: [[entities/jean-philippe-bouchaud|Jean-Philippe Bouchaud]] · [[entities/guillaume-maitrier|Guillaume Maitrier]]
- [[concepts/order-flow]] — long memory, of which metaorder splitting is the proposed cause
- [[concepts/optimal-execution]] — the problem of scheduling a metaorder's children
<!-- AUTHORED REGION END -->