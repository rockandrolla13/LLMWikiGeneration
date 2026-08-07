---
title: Momentum in Corporate Bond Returns
page_id: sources/jostova-2013-momentum
page_type: source
source_type: working-paper
revision_id: 1
source_path: markdown_output/jostova-2013-momentum.md
created: 2026-08-07 00:00:00+00:00
updated: '2026-08-07T11:27:07Z'
authors:
- Gergana Jostova
- Stanislava Nikolova
- Alexander Philipov
- Christof W. Stahel
year: 2010
venue: FDIC Center for Financial Research Working Paper 2010-04
tags:
- momentum
- corporate-bonds
- high-yield
- credit
- anomalies
sources: []
related:
- concepts/corporate-bonds
- concepts/bond-liquidity
mind_map_priority: high
schema_version: 2
uuid: d827c1b9-ff67-591b-83a1-25f5fc2fc55a
content_hash: sha256:2068adba05e1d2704b9356c8018193077182ca8d9bf7e6ccc577584c28033842
---

<!-- AUTHORED REGION START -->
# Momentum in Corporate Bond Returns

**Authors:** Gergana Jostova, Stanislava Nikolova, Alexander Philipov, Christof W. Stahel

**Version here:** FDIC Center for Financial Research Working Paper 2010-04, May 2010

> **Version note.** Pages in this wiki cite this work as "Jostova et al. (2013)", the
> *Review of Financial Studies* article. The document held here is the **2010 working
> paper**, which is what was obtainable. The argument is the same, but figures, sample
> cut-offs and robustness tables may differ from the published version. Treat any number
> below as the 2010 working-paper value, and re-check against the published article before
> relying on it. Listed in `wiki/BACKLOG.md` for replacement.

## Summary

Finds significant price momentum in US corporate bonds, using 3.2 million observations on 77,150 bonds drawn from two transaction and three dealer-quote databases, 1973–2008.

## Findings

- Momentum profits are significant in the **second half of the sample, 1991–2008**, at **64 basis points per month**.
- Profits come **only from non-investment-grade bonds**, where they reach **190 basis points per month**.
- As in equities, profits disappear once the worst-rated bonds are removed — about **8%** of observations.
- **Unlike equities, bond momentum comes primarily from winners.** TRACE data complicate this: losers trade more actively than winners, so trade-based datasets give losers a larger share of measured profitability than quote-based ones.

## Why the Explanations Fail

The paper closes off the two obvious dismissals.

**Illiquidity** is unlikely, because momentum is equally profitable in quote-based and trade-based data — if illiquidity drove it, the two should diverge.

**Opacity** is unlikely, because profits *increased* after TRACE reporting was introduced. More transparency did not compete the effect away.

## Caveats

The effect is concentrated in high yield and vanishes without the worst-rated names, so it lives precisely where trading costs are highest. The paper does not settle whether it survives realistic execution — see [[concepts/bond-liquidity|bond liquidity]].

## Open Questions

- Does the 1991–2008 result hold post-crisis, and after the 2013 publication date?
- If profits sit in the worst-rated 8%, is this momentum or a distress premium?

## See Also

[[concepts/corporate-bonds|Corporate Bonds]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] · [[sources/haesen-2017-momentum-spillover|Haesen et al. (2017)]] · [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]

**Not yet written:** `concepts/momentum`, `concepts/high-yield`
<!-- AUTHORED REGION END -->

