---
title: Leverage Ratios
page_id: concepts/leverage-ratios
page_type: concept
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T19:48:23Z'
tags:
- credit-analysis
- fundamental-analysis
- leverage
- creditETF
sources:
- sources/spec-2012-single-name-fundamental
related:
- concepts/spread-per-turn-of-leverage
- concepts/relative-value-analysis
mind_map_priority: medium
schema_version: 2
uuid: b358f0f2-1c29-549a-97d4-2f4fa5ae556f
content_hash: sha256:80da87dc4a2ad90c6097865b7b7d3576a7b8d351d52b39d72507dd9cb24843c8
---

<!-- AUTHORED REGION START -->
# Leverage Ratios

Accounting ratios that express how much debt a company carries relative to its earnings or its ability to service that debt. In single-name credit work they are the denominator against which spreads get normalised.

## The Ratios Used Here

[[sources/spec-2012-single-name-fundamental|The single-name fundamental analysis specification (2012)]] groups them under capitalisation and solvency:

- **Net debt / EBITDA** and **total debt / EBITDA**
- **EBIT / interest expense** and **EBITDA / interest expense** (interest coverage)
- **Funds from operations / debt**

Alongside these it calculates liquidity ratios (current, quick, cash conversion cycle), profitability measures (ROA, ROE, ROIC, margins) and valuation multiples (EV/EBITDA, EV/revenue, EV/EBIT, P/E, P/B).

## LTM Versus NTM

The same ratio computed on trailing and on forecast earnings answers different questions. **LTM** (last twelve months) uses reported history; **NTM** (next twelve months) uses analyst forecasts and therefore embeds expectations of deleveraging or re-leveraging. Both are used. Building the LTM series requires quarterly data, and the specification asks for three years of history as a minimum, extending to seven to ten years for EBITDA, net debt and free cash flow.

## Why They Are the Denominator

Leverage on its own does not say whether a bond is cheap. [[concepts/spread-per-turn-of-leverage|Spread per turn of leverage]] divides the five-year CDS spread by net debt / EBITDA, so that issuers with different absolute debt loads become comparable. Interest coverage is used the same way, as an alternative denominator, and is expected to correlate negatively with spreads.

The limitation carries over: this assumes the relationship between spread and leverage is linear, and it ignores business risk and asset quality.

## See Also

[[concepts/spread-per-turn-of-leverage|Spread Per Turn of Leverage]] · [[concepts/relative-value-analysis|Relative Value Analysis]] · [[concepts/leveraged-recapitalization|Leveraged Recapitalization]] · [[concepts/lbo-risk|LBO Risk]] · [[concepts/credit-spread-curve|Credit Spread Curve]]

**Not yet written:** `concepts/interest-coverage-ratio`, `concepts/ebitda`

<!-- AUTHORED REGION END -->
