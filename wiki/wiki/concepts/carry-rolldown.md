---
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/carry-rolldown
page_type: concept
related:
- concepts/bond-momentum
- concepts/credit-risk-premium
- concepts/credit-spread-curve
- concepts/cross-asset-rotation
- concepts/equity-forward-pricing
- concepts/ewmac-carry-trading-rules
- concepts/factor-investing
- concepts/forward-rate
- concepts/futures-carry
- concepts/government-bond-spreads
- concepts/macro-cycle-cross-asset-allocation
- concepts/nelson-siegel-model
- concepts/risk-premia
- concepts/style-premia
- concepts/term-structure-risk-premium
- concepts/trend-following
- concepts/volatility-risk-premia
- concepts/z-spread
revision_id: 3
sources:
- sources/ilmanen-2011-expected-returns
- sources/martin-2024-credit-curve
- sources/ms-2009-11-12-us-rate-strategist
- sources/ms-2015-03-06-bond-market-indicators
- sources/ms-2016-04-13-euro-sovereign-bond-market-indicators
- sources/ms-2016-09-27-momentum-for-diversification
- sources/ms-2017-06-15-bmi2-xbmi-models
- sources/ms-2018-02-27-who-buys-treasuries
- sources/ms-2018-03-16-toward-more-tightening
- sources/ms-2018-06-05-emfx-risk-premia-two-factor
- sources/ms-2018-11-05-trading-risk-premia-emfx-virp
- sources/ms-2019-01-26-duration-and-curves
- sources/ms-2019-01-28-european-credit-reluctant-rally
- sources/ms-2019-02-03-self-catalysing-dollar-weakness
- sources/ms-2019-02-09-dont-miss-the-bull-market
- sources/ms-2019-02-11-emfx-quants-lab-steady-path
- sources/ms-2019-02-13-eurex-futures-rolls
- sources/ms-2019-04-05-crossing-the-rubicon-government-bonds
- sources/ms-2019-04-05-long-dated-equity-vol
- sources/ms-2019-04-12-meet-in-the-middle
- sources/ms-2019-05-17-tariffs-government-bonds
- sources/ms-2019-06-03-emfx-quants-lab-carry-performs
- sources/ms-2019-06-28-fx-volatility-playbook
tags:
- fixed-income
- portfolio-management
- return-decomposition
- trading-strategies
title: Carry and Rolldown
updated: '2026-06-09T12:00:00Z'
---

# Carry and Rolldown

Carry and rolldown are components of expected bond returns that arise from the passage of time, assuming no change in market conditions.

## Definitions

### Carry
The income return from holding a bond, typically:
- **Coupon income** minus **financing cost**
- For a funded position: yield minus repo rate
- Represents compensation for holding duration/credit risk

### Rolldown
The capital gain (or loss) from a bond "rolling down" the yield curve as it ages:
- If the curve is upward sloping, shorter maturity → lower yield → higher price
- A 5-year bond today becomes a 4-year bond tomorrow

## Mathematical Framework

Total expected return (assuming unchanged curves):

$$\text{Expected Return} = \text{Carry} + \text{Rolldown}$$

**Carry**:
$$\text{Carry} = \text{Yield} - \text{Funding Rate}$$

**Rolldown** (approximation):
$$\text{Rolldown} \approx -\text{Duration} \times \Delta y_{\text{curve shape}}$$

## Applications

1. **Relative value**: Compare carry-adjusted valuations across bonds
2. **Curve positioning**: Identify "sweet spots" with high rolldown
3. **Performance attribution**: Decompose realized returns
4. **Strategy design**: Carry strategies systematically harvest these returns

## Considerations

- Carry/rolldown are **not risk-free**—curves can shift
- High carry often signals high risk (credit, liquidity)
- Rolldown assumes parallel curve dynamics (rarely exact)

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/z-spread|Z-Spread]]
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (Martin, 2024)]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ilmanen-2011-expected-returns]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2009-11-12-us-rate-strategist]], [[sources/ms-2015-03-06-bond-market-indicators]], [[sources/ms-2016-04-13-euro-sovereign-bond-market-indicators]], [[sources/ms-2016-09-27-momentum-for-diversification]], [[sources/ms-2017-06-15-bmi2-xbmi-models]], [[sources/ms-2018-02-27-who-buys-treasuries]], [[sources/ms-2018-03-16-toward-more-tightening]], [[sources/ms-2018-06-05-emfx-risk-premia-two-factor]], [[sources/ms-2018-11-05-trading-risk-premia-emfx-virp]], [[sources/ms-2019-01-26-duration-and-curves]], [[sources/ms-2019-01-28-european-credit-reluctant-rally]], [[sources/ms-2019-02-03-self-catalysing-dollar-weakness]], [[sources/ms-2019-02-09-dont-miss-the-bull-market]], [[sources/ms-2019-02-11-emfx-quants-lab-steady-path]], [[sources/ms-2019-02-13-eurex-futures-rolls]], [[sources/ms-2019-04-05-crossing-the-rubicon-government-bonds]], [[sources/ms-2019-04-05-long-dated-equity-vol]], [[sources/ms-2019-04-12-meet-in-the-middle]], [[sources/ms-2019-05-17-tariffs-government-bonds]], [[sources/ms-2019-06-03-emfx-quants-lab-carry-performs]], [[sources/ms-2019-06-28-fx-volatility-playbook]]