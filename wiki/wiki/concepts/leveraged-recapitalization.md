---
title: Leveraged Recapitalization
page_id: concepts/leveraged-recapitalization
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- event-risk
- LBO
- corporate-credit
- creditETF
sources:
- sources/trinh-2006-lever-framework
related:
- concepts/lbo-risk
- concepts/event-risk
- concepts/lever-score
mind_map_priority: medium
schema_version: 2
uuid: e8811b33-11c1-5036-9ff5-ba3758f8e811
content_hash: sha256:90ab9f1d4f0108eb1724059a6d0591be3f1966b00449586b6736447a1abedc7c
---

<!-- AUTHORED REGION START -->
# Leveraged Recapitalization

A company loads its own balance sheet with debt without being taken private. The credit effect resembles a leveraged buyout — leverage rises sharply, existing bondholders lose ground — but the company remains public.

## Why It Sits Alongside the LBO

The wiki treats recaps and LBOs as one risk category because the outcome for bondholders is much the same. [[concepts/lbo-risk|LBO Risk]] puts it directly: an actual LBO brings full credit deterioration, a recap has "similar impact, company remains public", and even the *threat* of either raises spread volatility without any transaction occurring.

The LEVER framework of [[sources/trinh-2006-lever-framework|Trinh & Bhattacharya (2006)]] was built to score both together — its name is LEVeraging Event Risk, and it covers leveraged buyouts and leveraged recapitalizations in US credit markets.

## The Case in the Record

Kerr-McGee is the wiki's worked recap example: **−1223bp excess return in 2005**, the sixth-worst investment-grade performer that year, following a recapitalization forced by Carl Icahn. It sits with Knight Ridder (−1950bp) and Albertsons (−1275bp) among the 2005 names that motivated the LEVER work.

## Scoring the Risk

Because the driver is the same, the same screen applies. A firm becomes an attractive target when it is cheaply valued (high book-to-market, low EV/EBITDA versus peers), throws off cash (high free cash flow yield, low capex growth), and is easy to finance (smaller size, stable cash flows). The Firm LEVER-Score compresses these into a 0–10 scale, with above 7.5 flagged as particularly at risk. See [[concepts/lever-score|LEVER Score]].

## See Also

[[concepts/lbo-risk|LBO Risk]] · [[concepts/event-risk|Event Risk]] · [[concepts/lever-score|LEVER Score]] · [[concepts/leverage-ratios|Leverage Ratios]] · [[entities/lehman-brothers|Lehman Brothers]] · [[entities/minh-trinh|Minh Trinh]]

**Not yet written:** `concepts/change-of-control-covenant`, `concepts/structural-subordination`

<!-- AUTHORED REGION END -->
