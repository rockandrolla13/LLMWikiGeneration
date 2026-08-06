---
title: Event Risk
page_id: concepts/event-risk
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T17:35:34Z'
tags:
- creditETF
- event-risk
- LBO
- corporate-credit
- credit-strategy
sources:
- sources/trinh-2006-lever-framework
related:
- concepts/lbo-risk
- concepts/lever-score
- concepts/credit-spread-curve
mind_map_priority: medium
schema_version: 2
uuid: 60a1a9e8-f26d-5f85-b135-268ca59b1897
content_hash: sha256:bf68f693b21b69e73ff363a14b5c561b1f287c2c9a5d8b390e378d42f81d9a5b
---

<!-- AUTHORED REGION START -->
# Event Risk

The risk that a discrete corporate action — not a gradual deterioration in fundamentals — abruptly damages bondholders. The canonical case in this wiki is the leveraged buyout, where a company's balance sheet is loaded with acquisition debt overnight and existing bondholders become structurally subordinated. See [[concepts/lbo-risk|LBO Risk]].

## Why It Is Hard to Price

Event risk is not well captured by spread or rating models built on financial history. [[sources/trinh-2006-lever-framework|Trinh & Bhattacharya (2006)]] make the structural point: debt investors lack access to the screening processes financial sponsors use when selecting targets, so there is an **informational gap** between who can see the event coming and who bears the loss.

The consequences are large and concentrated. Among 2005 US investment-grade names:

| Company | Excess return |
|---|---|
| Knight Ridder | −1950bp (worst IG performer) |
| Albertsons | −1275bp |
| Kerr-McGee | −1223bp (forced recapitalisation) |

## Scoring It

The LEVER framework produces two measures: a **Firm LEVER-Score** on a 0–10 scale, with companies above 7.5 flagged as particularly at risk, and a **Macro LEVER-Score** capturing market-wide conditions. See [[concepts/lever-score|LEVER Score]].

The separation matters. Firm-level vulnerability and market-level willingness to finance leveraged transactions are distinct: a highly scored firm in a closed financing market is a different proposition from the same firm in an open one.

## Open Questions

- Does a framework calibrated on 1995–2005 transfer to a market with a much larger private credit bid?
- How should event risk be handled at portfolio level, where it is idiosyncratic but not diversifiable if the macro driver is common?

## See Also

[[concepts/lbo-risk|LBO Risk]] · [[concepts/lever-score|LEVER Score]] · [[concepts/credit-spread-curve|Credit Spread Curve]] · [[entities/lehman-brothers|Lehman Brothers]]

**Not yet written:** `concepts/leveraged-recapitalization`

<!-- AUTHORED REGION END -->
