---
authors:
- Jangkoo Kang
- Kyung Yoon Kwon
- Wooyeon Kim
content_hash: sha256:9a8fd75868da2aa1c0876a2fba506aae27c4e41a0c2ff7f523d209375d741787
created: 2026-09-27 01:47:00+00:00
page_id: sources/kang-2019-flow-toxicity-highfrequency-trading-its-impact
page_type: source
publication_venue: Journal of Futures Markets
related:
- concepts/volume-clock
- concepts/high-frequency-trading
- concepts/adverse-selection
- concepts/informed-trading
- concepts/trade-classification
- concepts/bid-ask-spread
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/order-flow
- concepts/vpin
- concepts/bulk-volume-classification
revision_id: 1
schema_version: 2
source_hash: sha256:3d10e8803b75988bf77854331c49814a03f624d1d14a99ed75cbede608e650fb
source_path: markdown_output/kang-2019-flow-toxicity-highfrequency-trading-its-impact.md
source_type: paper
tags:
- high-frequency-trading
- flow-toxicity
- vpin
- adverse-selection
- trade-classification
- futures
- price-volatility
- clock-volume
- asset-futures
- harvest-core
title: 'Flow Toxicity of High Frequency Trading and Its Impact on Price Volatility:
  Evidence from the KOSPI 200 Futures Market'
updated: '2026-09-27T01:47:00Z'
uuid: 4afe7c17-333f-5eab-a6fe-4f871c54e12f
year: 2019
---

<!-- AUTHORED REGION START -->
# Flow Toxicity of High Frequency Trading and Its Impact on Price Volatility: Evidence from the KOSPI 200 Futures Market

## Summary

The paper asks whether the Volume-Synchronized Probability of Informed Trading (VPIN) genuinely measures order flow toxicity in a futures market, and how high frequency traders (HFTs) affect that toxicity and short-term price volatility in normal versus stressful periods. It also asks which trade-classification method, bulk volume classification (BVC) or the true trade initiator, better captures informed trading.

Using millisecond transaction records for KOSPI 200 index futures that include encrypted account identities, the authors classify accounts into HFTs and non-HFTs from their trading behavior, build a VPIN metric on volume buckets classified by BVC (BV-VPIN), and separately build a version using the true trade initiator (TR-VPIN). They regress future price volatility (the bucket high-low range) on lagged VPIN and controls, and regress changes in VPIN and in volatility on HFT participation ratios, with dummy interactions for toxic, intensely traded, and highly volatile buckets, plus a VAR model tying volatility, VPIN, and HFT activity together.

BV-VPIN strongly and robustly predicts next-bucket price volatility, and it rose to unusually high levels ahead of several historical market-stress episodes in the KOSPI 200 market. HFTs are negatively associated with both flow toxicity and volatility in normal conditions, consistent with them supplying liquidity and aiding price discovery, but the relationship flips to positive during intensely traded or highly volatile buckets, consistent with HFTs picking off slower traders once conditions turn stressful. TR-VPIN, built on the true initiator, behaves oppositely to BV-VPIN and fails to signal the stress episodes.

What is new is the direct within-market comparison of BVC-based and true-initiator-based VPIN using account-level data that lets the authors verify the true initiator, plus the finding that the initiator identified by BVC trades at more favorable prices than the true initiator, which the authors take as evidence that aggressiveness is no longer a reliable signal of informed trading.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Observations are volume buckets, each holding a fixed number of contracts equal to one-fiftieth of the average daily trading volume over the sample period (near 5,000 contracts, taking about seven minutes to fill on average). Buy and sell volume within each bucket is split by bulk volume classification (BVC) applied to volume bars of 1,000 contracts. VPIN is a moving average of the absolute trade imbalance over the trailing 50 buckets (one trading day), updated after every new bucket. The main prediction horizon is one bucket ahead: lagged VPIN at bucket t-1 is used to predict the high-low price range at bucket t.

## Data

- **Asset class:** Futures
- **Instruments:** KOSPI 200 index futures, front-month contracts only
- **Venue:** Korea Exchange (KRX)
- **Period:** January 2010 to June 2014 (1,115 trading days), per the data description in Section 3.1; Section 2 separately describes the sample period as spanning January 2011 to June 2014
- **Granularity:** millisecond-timestamped, transaction-by-transaction trade records, aggregated into volume buckets of roughly 5,000 contracts (about seven minutes) each

## Features and Measures

- **BV-VPIN.** Volume-synchronized probability of informed trading, computed as the moving average over 50 volume buckets of the absolute trade imbalance, where buy/sell volume within each bucket is split by bulk volume classification.
- **TR-VPIN.** The same VPIN construction as BV-VPIN, but buy/sell volume is assigned using the true trade initiator identified from order acceptance numbers instead of bulk volume classification.
- **HFT participation ratio.** The share of trading volume in a bucket initiated by, traded against, or otherwise involving accounts classified as high-frequency traders (HFT, HFT_M for HFT-initiated, HFT_L for HFT as counterparty).
- **PRCHL.** High-minus-low price within a volume bucket, used as the short-term price volatility measure, adjusted for overnight price changes using the Corwin-Schultz correction.
- **HL Spread.** The Corwin-Schultz high-low spread estimator, applied to intraday volume buckets instead of daily intervals, used as an illiquidity proxy.
- **Time Duration.** The clock time elapsed to fill a volume bucket, used as an inverse proxy for trading intensity.

## Method

The core empirical tool is OLS regression of the volume-bucket high-low price range on lagged log(VPIN) and control variables (lagged realized volatility, trading intensity, illiquidity), with dummy variables and interaction terms marking toxic, intensely traded, or highly volatile buckets. A parallel set of OLS regressions relates the first difference of log(VPIN) and the level of price volatility to lagged HFT participation ratios and the same stress dummies, to see whether HFTs' association with toxicity and volatility depends on market conditions. A Vector Autoregression (VAR) of price volatility, log(VPIN), and HFT participation ratio is estimated to capture the intertemporal feedback between the three variables jointly. Performance and validity are judged by statistical significance (t-values) of regression coefficients, by whether BV-VPIN anticipates known historical stress episodes in event studies, and, in the trade-classification comparison, by correlating trade imbalance with the Corwin-Schultz High-Low spread and by comparing volume-weighted average execution prices of the BVC-identified versus true trade initiator.

## Results

- ln(VPIN) at bucket t-1 predicts the high-low price range at bucket t with t-value 24.74, and the predictive power survives controls for lagged realized volatility, trading intensity, and illiquidity.
- The HFT participation ratio has a significantly negative coefficient (t-value -3.37) on the change in BV-VPIN in normal times, but this reverses to positive during intensely traded and highly volatile buckets.
- The HFT participation ratio has a significantly negative coefficient (t-value -18.20) on price volatility (PRCHL) in normal times, while its interaction with the toxic and volatile dummies is significantly positive, meaning HFTs raise volatility in stressful buckets.
- BV-VPIN has a sample mean of 0.18 and standard deviation of 0.04, versus a reported mean of 0.23 and standard deviation of 0.06 for VPIN in the E-mini S&P 500 futures market; BV-VPIN reached a maximum of 0.41 during the August 2011 U.S. credit-rating downgrade episode.
- TR-VPIN, built from the true trade initiator, is negatively related to price volatility and the High-Low spread, the opposite sign from BV-VPIN, and fails to signal the historical stress episodes that BV-VPIN signals.
- Trade imbalance classified by BVC has a coefficient of 13.45 (t-value) on the Corwin-Schultz High-Low spread, while trade imbalance from the true initiator has a coefficient of -51.56, i.e., opposite signs.
- The BV-initiator buys at a 0.0102% cheaper price and sells at a 0.0102% more expensive price than the true trade initiator (t-values -31.74 and 32.49), which the authors read as evidence that BVC better identifies informed trading.
- Foreign and domestic HFTs affect flow toxicity and volatility differently in normal times (domestic HFTs reduce toxicity, foreign HFTs do not), but both groups add to toxicity and volatility once conditions turn intensely traded or highly volatile.

## Limitations

- Reader note: the analysis covers a single market and a single asset class (KOSPI 200 index futures) over one sample period; generalizability to other markets is untested.
- HFT identification relies on a data-driven cutoff (the top 20 most active intraday intermediaries per day); the authors state results are insensitive to admissible changes in this cutoff but do not report the sensitivity tests.
- VPIN construction and all regressions exclude opening/closing auctions and overnight sessions, restricting analysis to continuous trading hours only.
- Reader note: the paper gives two different sample start dates for the same data (January 2010 in the data description versus January 2011 in the market environment section), an internal inconsistency in the source text.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/order-flow|order flow]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]

## Citation

Jangkoo Kang, Kyung Yoon Kwon, Wooyeon Kim (2019). Flow Toxicity of High Frequency Trading and Its Impact on Price Volatility: Evidence from the KOSPI 200 Futures Market. Journal of Futures Markets.

DOI: 10.1002/fut.22062

Text ingested: `markdown_output/kang-2019-flow-toxicity-highfrequency-trading-its-impact.md`, converted from `raw/ofi-event-clock/kang-2019-flow-toxicity-highfrequency-trading-its-impact.pdf`.

Coverage of this summary: Read the entire markdown file: abstract, introduction, market environment, data description and HFT identification, VPIN construction, all results sections (predictability of BV-VPIN, HFT and flow toxicity, HFT and volatility, VAR results, foreign versus domestic HFTs, trade classification and TR-VPIN), conclusion, references, and the appendix.

Known problems with the input: Regression equations, VAR specifications, and several tables/figures are OCR-omitted (marked as omitted pictures), so exact coefficient magnitudes beyond the t-values quoted in the running text are not available; The paper states two different sample start dates for the same dataset: January 2010 (Section 3.1, used for the reported 1,115 trading days) and January 2011 (Section 2); the data-description value was used for the period field; No publication year is printed on this manuscript (it is described only as 'Accepted/In press' at the Journal of Futures Markets); year 2019 was taken from the job file's year_hint.
<!-- AUTHORED REGION END -->