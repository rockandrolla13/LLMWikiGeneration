---
authors:
- Andres Jaime
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/ms-2018-11-05-trading-risk-premia-emfx-virp
page_type: source
publication_date: '2018'
publication_venue: Morgan Stanley Research
related:
- concepts/carry-rolldown
- concepts/risk-premia
- concepts/style-premia
- concepts/volatility-risk-premia
- entities/andres-jaime
- entities/morgan-stanley
revision_hash: sha256:e55ab3fd1b12e97e39dc784a4edb22ab9994f19864591f5bbcb3007d6fc680c6
revision_id: 1
source_hash: sha256:75670fe1da1ddfbf3972134b6db6ff7b8d3d66f64e9aa8e2e316ac129c876501
source_path: raw/creditmacro/Morgan Stanley - EM Quant Strategy — Trading Risk Premia
  in EMFX (Part 2) A mixed strategy using Volatility Risk Premia (VIRP) - 2018-11-05.md
source_type: article
sources: []
tags: []
title: 'Trading Risk Premia in EMFX (Part 2): A mixed strategy using Volatility Risk
  Premia (VIRP)'
updated: '2026-06-20T01:03:51Z'
updated_by: op_b42b5e980551
schema_version: 2
uuid: 229f64bc-f492-5883-9f51-168c58f75d4f
content_hash: sha256:5854db8b08a85685195ae26fcc5a7555a5a69f31af21ca8e1652485ca976c250
---

<!-- AUTHORED REGION START -->
# Trading Risk Premia in EMFX (Part 2): A mixed strategy using Volatility Risk Premia (VIRP)

**Authors:** Andres Jaime · **Year:** 2018 · **Venue:** Morgan Stanley Research · **Type:** report

## Summary

The second installment of an EM Quant Strategy series introduces a mixed VIRP strategy that combines an idiosyncratic risk-premia two-factor model (IRP) with a volatility risk-premia model (VRP) for trading EM currencies. Backtests show the combined VIRP strategy beats EM Carry and GBI-EM LC benchmarks in both absolute and vol-adjusted returns, achieving a Sharpe ratio of 0.99 versus 0.71 for VRP and 0.68 for IRP. The IRP and VRP signals are complementary: IRP detects extremes and reversals while VRP captures trend continuation. The strategy performs particularly well in high-beta currencies (MXN, ZAR, TRY, RUB, BRL) and serves as a tool to detect EM trends in both bull and bear markets.

## Key Claims

1. The mixed VIRP strategy outperforms both the standalone IRP and VRP models because IRP and VRP signals are complementary across reversals and trends.
2. VIRP achieves a Sharpe ratio of 0.99 (net of transaction costs), beating EM Carry and GBI-EM LC benchmarks in vol-adjusted terms.
3. Volatility risk premium, defined as realized minus implied vol, has predictive power for the cross-section of currency returns, consistent with Della Corte, Ramadorai and Sarno (2013).

## Concepts

- [[concepts/volatility-risk-premia|Volatility Risk Premia (VIRP)]]
- [[concepts/risk-premia|Risk Premia]]
- [[concepts/carry-rolldown|Carry and Rolldown]]
- [[concepts/style-premia|Style Premia]]

## Entities

- [[entities/andres-jaime|Andres Jaime]]
- [[entities/morgan-stanley|Morgan Stanley]]

## Source

- **Path:** `raw/creditmacro/Morgan Stanley - EM Quant Strategy — Trading Risk Premia in EMFX (Part 2) A mixed strategy using Volatility Risk Premia (VIRP) - 2018-11-05.md`
- **Type:** article
- **Hash:** `sha256:75670fe1da1ddfbf3...`
<!-- AUTHORED REGION END -->
