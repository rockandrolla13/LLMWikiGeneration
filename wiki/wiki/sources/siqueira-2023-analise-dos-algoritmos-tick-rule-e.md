---
authors:
- Leonardo Souza Siqueira
- Laíse Ferraz Correia
- Hudson Fernandes Amaral
content_hash: sha256:7b9e443b6cc860d360199c68df63d674b489f5c734d52c4be2d2c5ae2d5c41b0
created: 2026-09-27 01:47:00+00:00
page_id: sources/siqueira-2023-analise-dos-algoritmos-tick-rule-e
page_type: source
related:
- concepts/sampling-clocks
- concepts/trade-classification
- concepts/informed-trading
- concepts/market-microstructure
- concepts/adverse-selection
- concepts/high-frequency-data
- concepts/order-flow
- concepts/bulk-volume-classification
- concepts/vpin
revision_id: 1
schema_version: 2
source_hash: sha256:a4c7f049462c74852142fe7dd6764b7026125728f1e03830af51f2558abfcef0
source_path: markdown_output/siqueira-2023-analise-dos-algoritmos-tick-rule-e.md
source_type: paper
tags:
- trade-classification
- vpin
- brazil
- equities
- market-microstructure
- informed-trading
- order-flow
- emerging-markets
- clock-compares
- asset-equity
- harvest-relevant
title: Análise dos Algoritmos Tick Rule e Bulk Volume Classification no Mercado Acionário
  Brasileiro
updated: '2026-09-27T01:47:00Z'
uuid: 6d82c64b-1ceb-5b29-8204-cb3f5e14d80c
year: 2023
---

<!-- AUTHORED REGION START -->
# Análise dos Algoritmos Tick Rule e Bulk Volume Classification no Mercado Acionário Brasileiro

## Summary

The paper compares two classic algorithms for inferring which side (buyer or seller) initiated a stock trade: the tick rule (TR), which uses only the sequence of trade prices transaction by transaction, and bulk volume classification (BVC), which groups trades into fixed time or volume buckets and splits each bucket's volume between buy and sell using a normal-distribution approximation of the bucket's price change. Both are tested on Brazilian equities traded on B3, with stocks split into small, medium and large volume classes using a Fisher-Jenks clustering rule; 2018 data is used to find each class's best-performing BVC bucket setting, and 2019 data is used to check whether that setting still works out of sample.

Both algorithms' output is checked directly against real recorded buy/sell trade-initiator data from B3's own market-data feed, and both are also fed into the Volume-Synchronized Probability of Informed Trading (VPIN) measure, computed over a fixed number of equal volume buckets per day, to see how closely each algorithm's estimated order-flow imbalance matches the VPIN computed from the real trade sides.

TR beat BVC by a wide margin in every volume class, and the VPIN built from BVC-estimated volumes correlated far more weakly with the VPIN built from real trade sides than the TR-based VPIN did, turning negative for some small-volume stocks. BVC's best bucket parameter was also far less stable between 2018 and 2019 for small-volume stocks than for medium or large ones. A closer look at TR's own errors traces most of them to same-broker order pairs executed with essentially no time gap between them, consistent with order-splitting or rapid same-side sequences, while BVC's weaker performance is traced to its normal-distribution assumption assigning large buy/sell imbalances even for small price changes, and to its use of only the bucket's last price, which discards information about trades inside the bucket.

What is new is testing both algorithms, and the VPIN toxicity measure built on top of them, on Brazilian order-driven equity trading rather than the mostly US and European markets studied previously; the paper finds the opposite ranking of TR versus BVC from BVC's original US-futures study, and attributes this reversal to Brazil's comparatively lower trading volumes and higher return volatility as an emerging market.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The tick rule works on the raw, one-transaction-at-a-time trade tape: each trade is classified as buy or sell by comparing its price to the immediately preceding trade's price, tick by tick. Bulk volume classification instead aggregates trades into buckets before classifying: the paper tests both fixed time buckets (1, 2, 3 and 5 minutes) and fixed volume buckets (from 1,000 up to 500,000 shares), assigning a probabilistic buy/sell split to each bucket from its standardized price change. The best BVC bucket choice is calibrated per volume class on 2018 data and re-tested on 2019 data; VPIN itself is computed over a fixed number of equal volume buckets per trading day, treating each bucket as one unit of information time regardless of how long it took to fill.

## Data

- **Asset class:** Equities
- **Instruments:** 181 individual Brazilian stocks traded on B3 that had at least one trade on every day of the sample period, split into small/medium/large volume classes using a Fisher-Jenks clustering rule
- **Venue:** B3 (Brazilian stock exchange)
- **Period:** 2 January 2018 to 28 June 2019 (2018 data used to calibrate BVC parameters; the window from 2 January to 28 June 2019 used for out-of-sample testing and the VPIN comparison)
- **Granularity:** Tick-by-tick order/trade-level data from B3's market-data feed, about 150 million rows in total averaging about 2,6 million traded shares per day, compared against BVC computed on time buckets (1-5 minutes) or volume buckets (1,000-500,000 shares)

## Features and Measures

- **Tick Rule (TR).** Classifies each trade as a buy if its price is higher than the previous trade's price, a sell if lower, and repeats the previous trade's classification when the price is unchanged.
- **Bulk Volume Classification (BVC).** Aggregates trades into fixed time or volume buckets and splits each bucket's volume between buy and sell using the cumulative standard normal distribution applied to the bucket's standardized price change, assigning an even split when price does not change.
- **VPIN.** Volume-Synchronized Probability of Informed Trading: the average absolute imbalance between estimated buy and sell volume across a fixed number of equal volume buckets in a trading day, used as a proxy for order-flow toxicity.
- **Fisher-Jenks volume classes.** A clustering rule used to split stocks into small, medium and large groups by average 2018 traded volume, chosen to minimize variance within a class and maximize variance between classes.

## Method

For each volume class, the paper searches over a grid of BVC time-bucket and volume-bucket settings using 2018 trades, keeping the setting that maximizes agreement between BVC-estimated and real buy/sell volumes for each stock, then re-applies that same setting to 2019 data to test whether the calibration holds up. Tick rule classification requires no calibration and is applied directly to the tick-by-tick 2019 trade tape. Both methods' estimated buy/sell volumes are compared against B3's recorded true trade-initiator side to compute per-stock accuracy rates, and are separately fed into the VPIN formula (computed over a fixed number of equal volume buckets per day) so that TR-based and BVC-based VPIN series can be correlated against the VPIN computed from real trade sides.

A separate diagnostic analysis studies where each algorithm goes wrong: for TR, the frequency of buy/sell classifications is tabulated against the size of the preceding price change, and sequences of consecutive misclassifications are broken down by whether the current and prior orders shared the same buying or selling broker and by the time gap between them; for BVC, the estimated buy percentage is plotted against price change and compared to the real buy percentage at each price-change level, including the special case of a zero price change within a bucket.

## Results

- Tick Rule classification accuracy averaged 80,82% overall on the B3 sample, well above BVC's overall average accuracy of 56,85%.
- TR's accuracy ranged from a low of 62,99% (small-volume stocks) up to over 90% for the higher-volume classes, while BVC's accuracy ranged from a low of 33,08% up to a maximum of 70,90% among the highest-volume stocks.
- When there was no price change between consecutive trades, the current trade repeated the previous trade's classified side in 95,31% of cases, matching the tick rule's core assumption for this sample.
- Even for larger price changes (above 0,20 monetary units), the fraction of trades correctly signed by price direction stayed around 88%, showing the tick rule's underlying logic held up across the sample.
- BVC's best-fit bucket parameter from 2018 remained the top parameter in 2019 for 78% of large-volume stocks and 74% of medium-volume stocks, but for only 35% of small-volume stocks, indicating much weaker parameter stability for thinly traded names.
- VPIN built from TR-estimated volumes correlated with the VPIN built from real trade data at an average close to 80% across all volume classes, while VPIN built from BVC-estimated volumes correlated with the real-data VPIN at an average of at most 50% (for medium-volume stocks), turning negative in some small-volume-stock cases.
- When price did not change within a bucket, BVC assigned close to a 50/50 buy/sell split (51,88% buy on average), which matched real data reasonably well for the roughly 22% of intervals that had no price change.
- The study drew on 181 B3 stocks trading every day of the sample, about 150 million trade rows averaging about 2,6 million shares traded per day, with VPIN computed using n equal to 50 volume buckets per day.

## Limitations

- The sample is restricted to B3-listed Brazilian equities that traded every day of the period; the authors attribute BVC's weaker performance specifically to Brazil's lower trading volumes and higher return volatility relative to the US/European markets where BVC was originally developed.
- BVC's best bucket parameter was shown to be unstable across years specifically for small-volume stocks, so conclusions about BVC's overall usefulness may not generalize evenly across liquidity tiers.
- The 2018-2019 sample window is comparatively short and does not span multiple market regimes or a crisis period.
- Reader note: both algorithms' accuracy is measured against B3's own recorded trade-initiator side as ground truth; any labeling error in that underlying feed would affect TR and BVC accuracy jointly, and the paper has no way to check this from outside the exchange's data.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]
- [[concepts/vpin|VPIN]]

## Citation

Leonardo Souza Siqueira, Laíse Ferraz Correia, Hudson Fernandes Amaral (2023). Análise dos Algoritmos Tick Rule e Bulk Volume Classification no Mercado Acionário Brasileiro.

DOI: 10.15728/bbr.2023.20.1.6.pt

Text ingested: `markdown_output/siqueira-2023-analise-dos-algoritmos-tick-rule-e.md`, converted from `raw/ofi-event-clock/siqueira-2023-analise-dos-algoritmos-tick-rule-e.pdf`.

Coverage of this summary: Read the full article from abstract through references; the source is written in Portuguese and is summarized here in English.

Known problems with the input: Source document is written in Portuguese; the fields above are a translation and compilation into English rather than a quotation of the original text; The journal/venue name is not printed anywhere in the visible text; the DOI (bbr, volume 20, issue 1, year 2023) suggests Brazilian Business Review, but this could not be confirmed from the document itself, so venue is left blank and the year is taken from the DOI year rather than a printed masthead (submission, acceptance and online-publication dates in the header show 2021 and 2022, so there is some ambiguity about which year best labels this version); Most equation images (BVC formula, VPIN formula, tick-rule frequency equations) are omitted by the markdown converter, so their exact mathematical form could not be verified beyond what the surrounding prose describes; Several results tables (e.g. Tables 3, 5, 6, 7) are collapsed into single newline-separated cells by the conversion; numbers were matched to row/column labels using the surrounding prose and may not be perfectly reliable.
<!-- AUTHORED REGION END -->