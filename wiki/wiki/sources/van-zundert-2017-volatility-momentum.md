---
title: Volatility-Adjusted Momentum
page_id: sources/van-zundert-2017-volatility-momentum
page_type: source
source_type: thesis-chapter
revision_id: 1
source_path: markdown_output/van-zundert-2017-volatility-momentum.md
created: 2026-08-07 00:00:00+00:00
updated: '2026-08-07T11:27:07Z'
authors:
- Jeroen van Zundert
year: 2018
venue: Chapter 4 of "Empirical Studies on the Cross-Section of Corporate Bond and
  Stock Markets", CentER Dissertation Series, Tilburg University
tags:
- momentum
- volatility-scaling
- corporate-bonds
- equities
- portfolio-construction
sources: []
related:
- concepts/corporate-bonds
- sources/van-zundert-2018-thesis
- sources/jostova-2013-momentum
mind_map_priority: medium
schema_version: 2
uuid: 71b5763a-b473-5ecb-a97f-af8af1081b08
content_hash: sha256:22a8eaedcfcbba5ee2e7df26f9e8425b20d4e0f1fb701a88638bf94d53487cf0
---

<!-- AUTHORED REGION START -->
# Volatility-Adjusted Momentum

**Author:** Jeroen van Zundert

**Version here:** Chapter 4 of his 2018 Tilburg dissertation. See [[sources/van-zundert-2018-thesis|the full thesis]].

> **Version note.** Pages here cite this as "van Zundert (2017)". The document held is the
> thesis chapter, which is the version that was obtainable. The argument matches the
> citation — volatility-adjusted momentum — but it is a chapter, not a standalone 2017
> article, so the year and venue on citing pages may not match a published version if one
> exists.

## The Argument

Standard momentum sorts assets into unlevered quantile portfolios on past returns. That has been the default since Jegadeesh & Titman (1993) and has been applied across asset classes, including high-yield corporate bonds by [[sources/jostova-2013-momentum|Jostova et al.]].

Van Zundert's point is that standard portfolio theory says you should **scale by ex-ante expected volatility** — both the past returns you sort on, and the position sizes you take. Not doing so is a choice, and an unexamined one.

## Findings

On US stocks, **1927 to 2015**: annualised alpha rises from **17% for standard momentum to 39% for volatility-adjusted momentum**. The result holds when the universe is restricted to large caps, so it is not a small-cap artefact.

The chapter attributes the gain to two sources and includes an out-of-sample check on **corporate bonds**, which is why it is cited here rather than in an equities context.

## Why It Matters

The claimed improvement is large — alpha more than doubles from a change in construction, not in signal. If that holds, a great many published momentum results are measuring a portfolio-construction choice as much as a premium.

That size is also the reason for caution. A doubling from rescaling invites the question of how much survives leverage constraints, turnover and shorting costs, none of which a scaled unlevered sort accounts for by itself.

## Open Questions

- How much of the 17%-to-39% gap survives realistic implementation, especially in bonds where costs are higher?
- Does the bond out-of-sample check reach the same magnitude, or only the same sign?

## See Also

[[sources/van-zundert-2018-thesis|van Zundert (2018), full thesis]] · [[sources/jostova-2013-momentum|Jostova et al., Momentum in Corporate Bond Returns]] · [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] · [[concepts/corporate-bonds|Corporate Bonds]]

**Not yet written:** `concepts/momentum`, `concepts/volatility-scaling`
<!-- AUTHORED REGION END -->

