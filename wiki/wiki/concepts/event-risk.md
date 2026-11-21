---
content_hash: sha256:33df207d1594cc0155fa6ac80c88057fe63941e532736df38e1bc3718828965d
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/event-risk
page_type: concept
related:
- concepts/lbo-risk
- concepts/lever-score
- concepts/credit-spread-curve
revision_id: 4
schema_version: 2
sources:
- sources/trinh-2006-lever-framework
- sources/bendor-2021-systematic-investing-in-credit
- sources/kricheff-2012-pragmatists-guide-leveraged-finance
- sources/marks-2001-notes-from-new-york
tags:
- creditETF
- event-risk
- LBO
- corporate-credit
- credit-strategy
title: Event Risk
updated: '2026-11-21T02:22:02Z'
updated_by: op_91f1c2c374f4
uuid: 60a1a9e8-f26d-5f85-b135-268ca59b1897
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

## Sources

- [[sources/kricheff-2012-pragmatists-guide-leveraged-finance|A Pragmatist's Guide to Leveraged Finance: Credit Analysis for Bonds and Bank Debt]] (2012)
- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)

## In Howard Marks's Memos

- [[sources/marks-2001-notes-from-new-york|Notes from New York]] (2001)
<!-- AUTHORED REGION END -->