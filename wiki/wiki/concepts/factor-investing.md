---
created: 2026-04-26 02:25:00+00:00
page_id: concepts/factor-investing
page_type: concept
related:
- concepts/alpha-signal
- concepts/behavioral-finance
- concepts/bond-momentum
- concepts/carry-rolldown
- concepts/credit-spread-curve
- concepts/cross-asset-rotation
- concepts/cross-sectional-momentum
- concepts/etf-flow-tactical-asset-allocation
- concepts/factor-models
- concepts/factor-signals-in-credit
- concepts/global-tactical-asset-allocation
- concepts/illiquidity-premium
- concepts/law-of-active-management
- concepts/low-expected-returns
- concepts/macro-cycle-cross-asset-allocation
- concepts/momentum-trend-following
- concepts/non-fundamental-demand-shocks
- concepts/quant-factor-driven-markets
- concepts/risk-premia
- concepts/robust-portfolio-optimisation
- concepts/statistical-arbitrage
- concepts/style-premia
- concepts/systematic-credit-relative-value
- concepts/systematic-diversification
- concepts/taarss
- concepts/trend-following
- concepts/value-premium
- sources/houweling-2017-factor-investing
revision_id: 4
sources:
- sources/cotturo-2026-multifactor-timing-deep-learning
- sources/dickerson-2024-bond-pitfalls
- sources/houweling-2017-factor-investing
- sources/ilmanen-2022-investing-amid-low-expected-returns
- sources/ms-2016-09-27-momentum-for-diversification
- sources/ms-2019-03-10-cross-asset-playbook-overpricing-goldilocks
- sources/ms-2019-04-14-low-beta-defensiveness-scorecard
- sources/ms-2019-06-03-emfx-quants-lab-carry-performs
tags:
- factor-investing
- corporate-bonds
- quantitative-investing
- size
- value
- momentum
- low-risk
title: Factor Investing in Corporate Bonds
updated: '2026-06-20T01:03:51Z'
schema_version: 2
uuid: d37b4007-5179-5d0b-ba63-0f1957858fcd
content_hash: sha256:4933941937852f4a985c66469032237282bb550385063320758e8419825f4b3f
---

<!-- AUTHORED REGION START -->
# Factor Investing in Corporate Bonds

## Definition

Factor investing applies systematic, rules-based strategies to corporate bond markets, targeting persistent risk premia associated with specific characteristics. Unlike equities, bond factor investing must account for credit risk, interest rate sensitivity, and lower liquidity.

## Key Factors

### Size (Small Issuer)
- Small issuers earn premium over large issuers
- Measured by amount outstanding or issuer size
- 12-month holding periods typical

### Low-Risk
- Low-beta bonds outperform on risk-adjusted basis
- Measured by credit rating, duration, or beta
- Related to betting-against-beta phenomenon

### Value
- Cheap bonds (high spread relative to fundamentals) outperform
- Measured by spread vs. model-implied spread
- Credit spread deviation from curve

### Momentum
- Past winners continue outperforming
- Strong in high-yield, weak in investment-grade
- [[concepts/bond-momentum|Bond Momentum]]

## Empirical Evidence

| Factor | Monthly Alpha | Significance |
|--------|---------------|--------------|
| Size | 0.10-0.15% | Moderate |
| Low-Risk | 0.15-0.25% | Strong |
| Value | 0.20-0.30% | Strong |
| Momentum | 0.15-0.20% | High-Yield only |

## Implementation Considerations

### Transaction Costs
- Corporate bonds have higher transaction costs than equities
- 12-month holding periods reduce turnover
- Bid-ask spreads vary significantly by credit quality

### Data Quality
- [[concepts/trace-data|TRACE Data]] enables US research
- [[concepts/market-microstructure-noise|Market Microstructure Noise]] affects signals
- Look-ahead bias from bond filtering

### Multi-Factor Portfolios
- Factors have low correlations with each other
- Combined portfolios show improved Sharpe ratios
- Robeco research shows 0.5+ Sharpe achievable

## Related Concepts

- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/market-microstructure-noise|Market Microstructure Noise]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]

## Sources

- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]]
- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]]
- [[sources/cotturo-2026-multifactor-timing-deep-learning|Cotturo, Liu & Proner (2026)]] — multifactor timing with multitask deep learning across size/value/momentum/profitability/investment factors

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ilmanen-2022-investing-amid-low-expected-returns]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2016-09-27-momentum-for-diversification]], [[sources/ms-2019-03-10-cross-asset-playbook-overpricing-goldilocks]], [[sources/ms-2019-04-14-low-beta-defensiveness-scorecard]], [[sources/ms-2019-06-03-emfx-quants-lab-carry-performs]]
<!-- AUTHORED REGION END -->
