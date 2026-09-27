---
authors:
- Chris D'Souza
- Charles Gaa
- Jing Yang
content_hash: sha256:ada8fb24b974c202801a0280dfab929ba1a371f0f8d736b126d418a405d4f14a
created: 2026-09-27 01:47:00+00:00
page_id: sources/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered
page_type: source
publication_venue: Bank of Canada Working Paper 2003-28
related:
- concepts/bond-liquidity
- concepts/bid-ask-spread
- concepts/order-flow
- concepts/price-impact
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/liquidity-risk
- concepts/informed-trading
revision_id: 1
schema_version: 2
source_hash: sha256:5554e51187acf03e9ffafe9d52bab93a49a7f7410da4aee83e7bbd00c6af4cf5
source_path: markdown_output/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered.md
source_type: paper
tags:
- bond-liquidity
- interdealer-market
- bid-ask-spread
- price-impact
- government-bonds
- market-microstructure
- order-flow
- canada
- clock-calendar
- asset-bonds-rates
- harvest-relevant
title: An Empirical Analysis of Liquidity and Order Flow in the Brokered Interdealer
  Market for Government of Canada Bonds
updated: '2026-09-27T01:47:00Z'
uuid: 7c025984-c44f-5a22-ab91-e437c11e3069
year: 2003
---

<!-- AUTHORED REGION START -->
# An Empirical Analysis of Liquidity and Order Flow in the Brokered Interdealer Market for Government of Canada Bonds

## Summary

The paper asks which of several commonly used liquidity indicators are actually appropriate for a wholesale, dealer-to-dealer bond market, using the first detailed intraday data set available for the Canadian government bond market. The authors build six activity and liquidity measures -- trading volume, trade frequency, the bid-ask spread, quote size, trade size, and two Kyle-style price-impact coefficients -- plus two new measures based on how often dealers use the market's order-expansion ('workup') protocol, whereby a trade's size can be renegotiated upward once it has been initiated.

The measures are constructed from CanPX, a consolidated feed of quotes and trades from Canada's interdealer brokers, covering the 2-, 5-, 10- and 30-year Government of Canada benchmark bonds over 250 trading days from 25 February 2002 to 27 February 2003, aggregated into 5-minute intervals.

Trading activity is positively correlated with price volatility for both trading volume and trade frequency, which limits their use as clean liquidity proxies, while the bid-ask spread and the two price-impact coefficients move together consistently with each other and with volatility, which the authors take as evidence that these are the most appropriate indicators in this market. Signed order flow (the net of buyer- and seller-initiated trades) is found to explain contemporaneous 5-minute price changes, with the net number of trades outperforming net trading volume as an explanatory variable. Compared with Fleming's results for the U.S. Treasury market, the authors describe the Canadian 2-year benchmark bond as trading in about half the size, at roughly twice the bid-ask spread, with more than double the price impact, alongside much heavier use of the workup protocol.

What is new is the first systematic, intraday description of the Canadian government bond interdealer market, together with two liquidity measures built around the workup protocol; the authors report that use of the workup is not consistently linked to trading activity, liquidity, or volatility, so it cannot simply be explained as a reaction to illiquid or volatile conditions.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Continuous quote and trade records are aggregated into 144 discrete 5-minute intervals per trading day, running from 0600h to 1800h; each interval records the most recently updated bid/offer and the cumulative trading and quotation activity over the preceding five minutes for that security. Price-impact coefficients are estimated by regressing the 5-minute log price change on net buyer-minus-seller trading activity (measured either in volume or in number of trades) over that same interval; the other liquidity indicators are daily or weekly aggregates of the underlying quote and trade records, typically computed over the 0730h-1700h trading window.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** Government of Canada benchmark bonds in the 2-, 5-, 10- and 30-year maturity sectors, plus the previous ('old') benchmark in each sector
- **Venue:** Canadian brokered interdealer market for Government of Canada bonds, aggregated via CanPX from the four Canadian interdealer brokers (IDBs); the authors note Canadian IDBs accounted for about 46 per cent of secondary Government of Canada bond trading volume in 2002, with about 86 per cent of that interdealer volume passing through IDB screens
- **Period:** 25 February 2002 to 27 February 2003 (250 trading days)
- **Granularity:** quote and trade snapshots aggregated into 144 five-minute intervals per day (0600h to 1800h); most reported daily liquidity indicators are computed over the narrower 0730h-1700h trading window

## Features and Measures

- **Trading volume.** The total value of securities traded per unit of time, used as a rough activity-based proxy for liquidity.
- **Trade frequency.** The number of trades observed per unit of time; treated as a purer activity measure than trading volume because it excludes the effect of trade-size changes.
- **Bid-ask spread.** The difference between the best bid and offer prices posted by dealers, taken as a direct estimate of one-way transaction cost.
- **Quote size.** The amount dealers are willing to trade at the best bid and offer prices, used as a proxy for pre-trade market depth.
- **Trade size.** The realized size of completed trades, including any size negotiated upward through the workup, used as an ex post depth measure.
- **Price-impact (Kyle-style) coefficients.** Regression coefficients from regressing 5-minute log price changes on net trading activity, measured either as net buyer-minus-seller trading volume or as the net number of buyer- minus seller-initiated trades.
- **Order-expansion ('workup') measures.** Two new measures proposed by the authors: the proportion of trades, and the proportion of trading volume, in which the final trade size exceeds the amount initially quoted.

## Method

For each of the four benchmark maturities, the authors compute daily and weekly summary statistics (mean, median, standard deviation, quartiles) for each liquidity indicator, and correlate the indicators against each other, against daily price volatility (the standard deviation of 5-minute log returns), and across the four bond maturities. Price-impact coefficients are estimated by regressing 5-minute log price changes on net trading activity over the same interval, separately for each week and then again pooling the whole sample; the workup-based measures are computed as the share of trades or trading volume in which the final trade size exceeds the amount originally quoted. The authors compare their Canadian results, in particular for the 2-year benchmark, against a published set of equivalent indicators for the on-the-run U.S. Treasury market.

## Results

- In price-impact regressions relating 5-minute log price changes to net buyer-minus-seller trading activity, the version using the net number of trades explains more variation than the version using net trading volume; pooling the whole sample for the 2-year benchmark bond, the adjusted R-squared is 0.0874 with net number of trades against 0.0219 with net trading volume.
- Trading volume and trade frequency are both positively correlated with price volatility across the benchmark bonds, which the authors say limits how cleanly these activity measures can be read as liquidity indicators.
- The bid-ask spread and the two price-impact coefficients are the measures that consistently move together, both with each other and with volatility, across the benchmark bonds, which the authors take as the strongest evidence for their appropriateness as liquidity indicators in this market.
- Canadian dealers make much heavier use of the order-expansion ('workup') protocol than U.S. dealers: for the comparable on-the-run 5-year note, the reported U.S. figures are 25.9 per cent of trades and 45.6 per cent of trading volume undergoing size expansion, versus 41 per cent and 72 per cent for the Canadian market.
- Relative to the U.S. Treasury market, the authors report roughly 20:1 and 11:1 differentials in trading volume and trade frequency, respectively, favouring the United States for the 2-year benchmark bond.
- Adjusted for the size of securities outstanding, Inoue's survey turnover ratios put the U.S. and Canadian markets close together, at 22 times and 21.9 times respectively, in third and fourth place among the ten countries surveyed.
- Use of the order-expansion protocol is not consistently correlated with trading activity, other liquidity measures, or price volatility across the benchmark bonds, and, unlike patterns reported for the U.S. Treasury market, is not more prevalent among less-liquid, non-benchmark securities.

## Limitations

- The authors describe this as a preliminary study covering a single, roughly one-year sample period.
- The authors state that CanPX does not include the Canadian IDB 'roll' market, where dealers trade one security for another on a spread basis, leaving out a potentially significant amount of interdealer activity.
- The authors state that price-impact coefficients are estimated over longer weekly or full-sample windows and so cannot be used directly to characterize intraday conditions the way the other five indicators can.
- The authors state that quote size understates true market depth because it excludes size that dealers are willing to trade beyond the posted quote through the workup protocol.
- Reader note: the study covers only benchmark and near-benchmark Government of Canada bonds in four maturity sectors, over about one year, so results may not generalize to non-benchmark securities or other periods.

## Related

- [[concepts/bond-liquidity|bond liquidity]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-flow|order flow]]
- [[concepts/price-impact|price impact]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/informed-trading|informed trading]]

## Citation

Chris D'Souza, Charles Gaa, Jing Yang (2003). An Empirical Analysis of Liquidity and Order Flow in the Brokered Interdealer Market for Government of Canada Bonds. Bank of Canada Working Paper 2003-28.

DOI: 10.34989/swp-2003-28

Text ingested: `markdown_output/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered.md`, converted from `raw/ofi-event-clock/dsouza-2003-empirical-analysis-liquidity-order-flow-brokered.pdf`.

Coverage of this summary: Read the full working paper front to back, including the abstract, all numbered sections (1 to 6), the bibliography, every reported table (1-26), and both appendices.
<!-- AUTHORED REGION END -->