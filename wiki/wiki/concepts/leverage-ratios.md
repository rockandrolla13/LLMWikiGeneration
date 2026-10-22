---
content_hash: sha256:e3e9712bb94007f076d0650d569520afc06ab05f131bb399fd20c4da5ec25787
created: 2026-08-06 00:00:00+00:00
mind_map_priority: medium
page_id: concepts/leverage-ratios
page_type: concept
related:
- concepts/spread-per-turn-of-leverage
- concepts/relative-value-analysis
revision_id: 3
schema_version: 2
sources:
- sources/spec-2012-single-name-fundamental
- sources/bai-2016-anchoring-cds-spreads-firm-fundamentals
- sources/wang-2013-cds-spreads-variance-risk-premia
- sources/bendor-2021-systematic-investing-in-credit
tags:
- credit-analysis
- fundamental-analysis
- leverage
- creditETF
title: Leverage Ratios
updated: '2026-10-22T15:27:29Z'
updated_by: op_955147eb8c65
uuid: b358f0f2-1c29-549a-97d4-2f4fa5ae556f
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

## Sources

- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)
- [[sources/wang-2013-cds-spreads-variance-risk-premia|Credit Default Swap Spreads and Variance Risk Premia]]
- [[sources/bai-2016-anchoring-cds-spreads-firm-fundamentals|Anchoring Credit Default Swap Spreads to Firm Fundamentals]]
<!-- AUTHORED REGION END -->