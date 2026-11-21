---
content_hash: sha256:bd1f54e403a4ed52843bdd12d390ebb3f5eaf3f7edd43a74e90971efede4ba6c
created: 2026-04-25 22:00:00+00:00
mind_map_priority: medium
page_id: concepts/liquidity-risk
page_type: concept
related:
- concepts/bond-capm
- concepts/capital-structure-arbitrage
- concepts/corporate-bond-liquidity-premium
- concepts/corporate-bonds
- concepts/credit-default-swap-spread
- concepts/credit-spread-curve
- concepts/default-rates
- concepts/factor-models
- concepts/illiquidity-premium
- concepts/limits-to-arbitrage
- concepts/liquidity-scoring-mechanism
- concepts/market-crash-liquidity-crisis
- concepts/private-credit
- concepts/risk-premia
- concepts/statistical-arbitrage
- concepts/term-structure-risk-premium
revision_id: 10
schema_version: 2
sources:
- sources/coppola-2025-asset-class-liquidity-indicators
- sources/dickerson-2023-bond-risk
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/ms-2016-03-22-xccy-basis-primer
- sources/ms-2019-03-04-a-premium-for-size
- sources/corradi-2015-liquidity-crises-different-time-scales
- sources/coz-2024-when-cross-impact-relevant
- sources/dobrev-2025-order-flow-imbalances-amplification-price-movements
- sources/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered
- sources/ferreruela-2025-informed-trading-investor-beliefs-consensus-volatility
- sources/hiremath-2026-early-detection-latent-microstructure-regimes-limit
- sources/jiang-2015-volume-synchronized-probability-informed-trading-vpin
- sources/lu-2009-essays-behavioral-finance-market-microstructure
- sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych
- sources/sirignano-2018-deep-learning-limit-order-books
- sources/turkoglu-2015-natural-time-crash-risk
- sources/wang-2012-order-imbalance-liquidity-returns-us-treasury-market
- sources/wang-2025-forecasting-liquidity-withdraw-machine-learning-models
- sources/wu-2013-big-data-approach-analyzing-market-volatility
- sources/bendor-2021-systematic-investing-in-credit
- sources/whitman-2009-distress-investing
- sources/marks-1994-risk-in-todays-markets-revisited
- sources/marks-2000-irrational-exuberance
- sources/marks-2000-investment-miscellany
- sources/marks-2004-the-happy-medium
- sources/marks-2006-risk
- sources/marks-2006-pigweed
- sources/marks-2007-now-its-all-bad
- sources/marks-2008-the-tide-goes-out
- sources/marks-2008-plan-b
- sources/marks-2012-assessing-performance-records-a-case-study
- sources/marks-2012-its-all-a-big-mistake
- sources/marks-2014-risk-revisited
- sources/marks-2015-liquidity
- sources/marks-2015-risk-revisited-again
- sources/marks-2015-its-not-easy
- sources/marks-2023-lessons-from-silicon-valley-bank
- sources/marks-2025-a-look-under-the-hood
- sources/marks-2016-on-the-couch
- sources/marks-2020-latest-update
- sources/marks-2026-whats-going-on-in-private-credit
tags:
- fixed-income
- risk-management
- market-microstructure
- trading
title: Liquidity Risk
updated: '2026-11-21T02:50:17Z'
updated_by: op_b76f64d1a29a
uuid: 47e7be12-ab35-5549-b347-0d0a46218226
---

<!-- AUTHORED REGION START -->
# Liquidity Risk

Liquidity risk is the risk that an investor cannot buy or sell an asset quickly enough at a fair price, or that doing so will significantly impact the market price.

## Components

### Market Liquidity Risk
- **Bid-ask spread**: Cost of immediate execution
- **Market depth**: Size that can be traded without price impact
- **Resiliency**: Speed at which prices recover after large trades

### Funding Liquidity Risk
- Ability to meet margin calls or redemptions
- Cost of financing positions
- Rollover risk for short-term funding

## Measurement in Corporate Bonds

| Measure | Description |
|---------|-------------|
| Bid-ask spread | Direct transaction cost |
| Trading volume | Market activity indicator |
| Amihud measure | Price impact per unit volume |
| Roll measure | Implicit spread from price reversals |
| Age | Time since issuance (proxy) |

## Liquidity Premium in Bonds

Investors require compensation for holding illiquid bonds:
- Estimated at 50-100 bps for investment grade
- Higher for high yield (100-300 bps)
- Time-varying: spikes during crises

## Corporate Bond Specifics

Corporate bonds are particularly illiquid because:
- **Many issues**: Thousands of bonds vs. single equity
- **Dealer market**: No central exchange
- **Inventory costs**: Dealers face capital constraints
- **Credit cliff risk**: Downgrades trigger forced selling

## See Also

- [[concepts/bond-capm|Bond CAPM]]
- [[concepts/factor-models|Factor Models]]
- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[sources/dickerson-2023-bond-risk|Corporate Bond Risk Factor Pricing (2023)]]
- [[sources/coppola-2025-asset-class-liquidity-indicators|Coppola, Urga & Varaldo (2025) Asset Class Liquidity Risk Indicators]] — endogenous Markov-switching liquidity regimes across European/US equity and bond markets with funding-vs-market liquidity decomposition

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/kapadia-2012-limited-arbitrage-equity-credit]]

## Added by credit-macro ingest (2026-06-09)

Now also discussed in: [[sources/ms-2016-03-22-xccy-basis-primer]], [[sources/ms-2019-03-04-a-premium-for-size]]

## Sources

- [[sources/whitman-2009-distress-investing|Distress Investing: Principles and Technique]] (2009)
- [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (2021)

## In Howard Marks's Memos

- [[sources/marks-1994-risk-in-todays-markets-revisited|"Risk in Today's Markets" Revisited]] (1994)
- [[sources/marks-2000-irrational-exuberance|Irrational Exuberance]] (2000)
- [[sources/marks-2000-investment-miscellany|Investment Miscellany]] (2000)
- [[sources/marks-2004-the-happy-medium|The Happy Medium]] (2004)
- [[sources/marks-2006-risk|Risk]] (2006)
- [[sources/marks-2006-pigweed|Pigweed]] (2006)
- [[sources/marks-2007-now-its-all-bad|Now It’s All Bad?]] (2007)
- [[sources/marks-2008-the-tide-goes-out|The Tide Goes Out]] (2008)
- [[sources/marks-2008-plan-b|Plan B]] (2008)
- [[sources/marks-2012-assessing-performance-records-a-case-study|Assessing Performance Records – A Case Study]] (2012)
- [[sources/marks-2012-its-all-a-big-mistake|It’s All a Big Mistake]] (2012)
- [[sources/marks-2014-risk-revisited|Risk Revisited]] (2014)
- [[sources/marks-2015-liquidity|Liquidity]] (2015)
- [[sources/marks-2015-risk-revisited-again|Risk Revisited Again]] (2015)
- [[sources/marks-2015-its-not-easy|It's Not Easy]] (2015)
- [[sources/marks-2023-lessons-from-silicon-valley-bank|Lessons from Silicon Valley Bank]] (2023)
- [[sources/marks-2025-a-look-under-the-hood|A Look Under the Hood]] (2025)
- [[sources/marks-2016-on-the-couch|On the Couch]] (2016)
- [[sources/marks-2020-latest-update|Latest Update]] (2020)
- [[sources/marks-2026-whats-going-on-in-private-credit|What’s Going on in Private Credit?]] (2026)
<!-- AUTHORED REGION END -->