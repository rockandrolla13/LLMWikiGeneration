---
title: 'Introducing LEVER: A Framework for Scoring LEVeraging Event Risk'
page_id: sources/trinh-2006-lever-framework
page_type: source
revision_id: 1
created: 2026-05-05 23:15:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- creditETF
- LBO-risk
- event-risk
- credit-strategy
- quantitative-credit
authors:
- entities/minh-trinh
- entities/bodha-bhattacharya
institutions:
- entities/lehman-brothers
related:
- concepts/lever-score
- concepts/lbo-risk
- concepts/event-risk
schema_version: 2
uuid: 95eb4f9a-467a-5531-9d66-a994d0dd1eef
content_hash: sha256:e2a23bd4b7ad385957786bdf562c68268791f3fee8422c6c89c60711cd9f2087
---

<!-- AUTHORED REGION START -->
# Introducing LEVER: A Framework for Scoring LEVeraging Event Risk

**Authors:** [[entities/minh-trinh|Minh Trinh]], [[entities/bodha-bhattacharya|Bodha Bhattacharya]]
**Institution:** [[entities/lehman-brothers|Lehman Brothers]]
**Date:** January 9, 2006
**Type:** Quantitative Credit Research

## Summary

Introduces LEVER, a quantitative framework for measuring relative risk of leveraged buyouts (LBOs) and leveraged recapitalizations in US credit markets. The framework produces two risk measures: the Firm LEVER-Score (company-specific) and the Macro LEVER-Score (market-wide). Demonstrates strong predictive power over 1995-2005 testing period.

## Motivation

LBOs and leveraged recapitalizations emerged as significant credit risks in 2005:
- **Knight Ridder:** -1950bp excess return (worst IG performer 2005)
- **Albertsons:** -1275bp excess return (#5)
- **Kerr-McGee:** -1223bp excess return (#6, forced recap by Carl Icahn)

Debt investors lack access to standard screening processes used by financial sponsors, creating an informational gap.

## The LEVER Framework

### Firm LEVER-Score

Scores range 0-10; companies above 7.5 are particularly at risk.

**Three Component Scores:**

**1. Valuation Score:**
- **Book-to-market ratio** (↑) - proxy for disposal/replacement value
- **EV/EBITDA multiple** (↓) - low multiple suggests undervaluation vs. peers

**2. Operations Score:**
- **Free cash flow yield** (↑) - high FCF + low market value = attractive
- **Capex growth** (↓) - rising capex indicates competing cash commitments

**3. Execution Score:**
- **Firm size** (↓) - smaller firms require less debt to fund
- **Free cash flow variability** (↓) - stable cash flows enable debt servicing

**Score Construction:**
- Uses cross-sectional ranking of normalized values
- Sector-adjusted for valuation metrics (book-to-market, EV/EBITDA, capex growth)
- Universe-wide for other metrics

### Macro LEVER-Score

Captures overall market environment for LBO transactions.

**Key Correlations with LBO Activity:**

| Variable | Correlation |
|----------|-------------|
| Private equity capital raised (prior year) | +65% |
| Credit spread changes | +51% |
| GDP growth | +31% |
| S&P 500 cash-flow yield | +22% |
| S&P 500 returns | -12% |
| S&P 500 leverage | -23% |
| 10-year yield change | -29% |
| 2y-10y slope change | -52% |
| S&P 500 dividend yield | -75% |

## Sector Considerations

**Excluded from Analysis:**
- Financial sector (already highly leveraged)
- Technology firms pre-2001 (growth phase, low book-to-market)

**Post-2001 Technology:**
- Transitioned from "growth" to "value" status
- Book-to-market ratios normalized
- Became more attractive LBO candidates

## Historical Performance

Strong predictive power demonstrated in backtests covering 1995-2005.

## Applications

- Portfolio screening for LBO/recap risk
- Risk-adjusted positioning around high LEVER-Score names
- Market timing based on Macro LEVER-Score

## Related Concepts

- [[concepts/lever-score]]
- [[concepts/lbo-risk]]
- [[concepts/event-risk]]
- [[concepts/leveraged-recapitalization]]

<!-- AUTHORED REGION END -->
