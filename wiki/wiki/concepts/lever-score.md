---
title: LEVER Score
page_id: concepts/lever-score
page_type: concept
revision_id: 1
created: 2026-05-05 23:20:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- creditETF
- event-risk
- LBO
- quantitative-credit
sources:
- sources/trinh-2006-lever-framework
- sources/lehman-2007-qcr-quarterly
related:
- concepts/lbo-risk
- concepts/event-risk
- concepts/leveraged-recapitalization
schema_version: 2
uuid: 73c55cda-925d-5a33-880f-fcb3f2ebdf57
content_hash: sha256:53cdf3e256b58331be39163a6732e62aeb0504d15f16adbfb91fb93518bed071
---

<!-- AUTHORED REGION START -->
# LEVER Score

**LEVER** (LEVeraging Event Risk) is a quantitative framework developed by [[entities/lehman-brothers|Lehman Brothers]] in 2006 for measuring the relative risk of leveraged buyouts (LBOs) and leveraged recapitalizations in credit markets.

## Components

### Firm LEVER-Score

A company-specific score ranging from 0-10, where scores above 7.5 indicate particularly high LBO/recap risk.

**Three Sub-Scores:**

| Score | Variables | Direction |
|-------|-----------|-----------|
| **Valuation** | Book-to-market | ↑ |
| | EV/EBITDA | ↓ |
| **Operations** | Free cash flow yield | ↑ |
| | Capex growth | ↓ |
| **Execution** | Firm size | ↓ |
| | FCF variability | ↓ |

The score uses cross-sectional ranking of normalized values, with some variables adjusted relative to sector peers.

### Macro LEVER-Score

Measures overall market environment favorability for LBO transactions.

**Key Positive Correlations:**
- Private equity capital raised (prior year): +65%
- Credit spread changes: +51%
- GDP growth: +31%

**Key Negative Correlations:**
- S&P 500 dividend yield: -75%
- Yield curve slope changes: -52%

## Usage

1. **Screening:** Identify names with elevated LBO/recap risk
2. **Portfolio Positioning:** Risk-adjust exposures to high-score names
3. **Alpha Generation:** LEVER-based trades show low correlation with traditional credit strategies
4. **Market Timing:** Macro LEVER-Score indicates favorable/unfavorable environment

## Sector Exclusions

- **Financials:** Already highly leveraged
- **Pre-2001 Technology:** Growth phase made them unattractive LBO targets

## Historical Performance

Demonstrated strong predictive power in backtests covering 1995-2005. Notable 2005 examples where high LEVER-Score preceded large losses:
- Knight Ridder: -1950bp excess return
- Albertsons: -1275bp
- Kerr-McGee: -1223bp

## See Also

- [[concepts/lbo-risk]]
- [[concepts/event-risk]]
- [[sources/trinh-2006-lever-framework]]

<!-- AUTHORED REGION END -->
