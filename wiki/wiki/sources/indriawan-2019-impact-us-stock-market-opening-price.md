---
authors:
- Ivan Indriawan
- Feng Jiao
- Yiuman Tse
content_hash: sha256:526c9c71e20f413952b13bf5482bd94a4388d7791e27ae53ee38d0f7ff65cf41
created: 2026-09-27 01:47:00+00:00
page_id: sources/indriawan-2019-impact-us-stock-market-opening-price
page_type: source
related:
- concepts/informed-trading
- concepts/order-flow
- concepts/market-microstructure
- concepts/high-frequency-data
revision_id: 1
schema_version: 2
source_hash: sha256:5bdd395bf9fe3e13cd577d78864f54843a91cba8134b3acd8d4355ed145d42b5
source_path: markdown_output/indriawan-2019-impact-us-stock-market-opening-price.md
source_type: paper
tags:
- price-discovery
- government-bond-futures
- information-share
- order-flow
- event-study
- cross-market-linkages
- state-space-model
- clock-calendar
- asset-bonds-rates
- harvest-relevant
title: The Impact of the US Stock Market Opens on Price Discovery of Government Bond
  Futures
updated: '2026-09-27T01:47:00Z'
uuid: 38723921-ecbb-5782-bb19-db9a33f8d448
year: 2019
---

<!-- AUTHORED REGION START -->
# The Impact of the US Stock Market Opens on Price Discovery of Government Bond Futures

## Summary

The paper asks whether US Treasury futures, and international government bond futures more broadly, become more informationally efficient once the US stock market begins regular trading, and whether any such gain traces to trade-related or trade-unrelated information.

It measures price discovery in sequential (non-overlapping) markets using an information-share concept adapted from Hasbrouck, estimated from a daily state-space model (Kalman filter) that splits the observed futures price into a permanent, information-driven efficient price and a transitory pricing-error component driven by signed order flow. It compares 10-, 20-, and 30-minute windows before and after 9:30am Eastern, and repeats the same design on US-only public holidays as a placebo.

Information share increases for all three futures right after the US stock market opens; the increase for the US Treasury and German Bund futures traces mainly to trade-related information, while the UK Gilt's increase is mostly trade-unrelated. The effect disappears on US holidays, when the stock market is closed but the futures still trade.

What is new is extending price-discovery analysis to markets that trade sequentially rather than in parallel, which lets the authors isolate the specific incremental effect of the US stock market opening on both domestic and foreign bond futures, and using a placebo-holiday design to support a causal reading of the result.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The main analysis studies fixed calendar-time windows around 9:30am Eastern (10, 20, and 30 minutes before versus after the US stock market open); the underlying state-space model is estimated from transaction-level data with signed order flow entering both the permanent and transitory price components, but the reported price-discovery statistics are computed once per day for these fixed clock-time windows.

## Data

- **Asset class:** Bonds and rates
- **Instruments:** 10-year UK Gilt futures (FLG), 10-year German Bund futures (FGBL), and US 10-year Treasury Note futures (TY), each rolled to the nearby (most liquid) contract
- **Venue:** FLG on Intercontinental Exchange (ICE); FGBL on Eurex Exchange (EUX); TY on Chicago Board of Trade (CBOT); transaction data sourced from Thomson Reuters Tick History
- **Period:** January 1, 2010 to June 30, 2017
- **Granularity:** transaction-level trade and quote data timestamped to the millisecond

## Features and Measures

- **Information share (IS).** The share of the total variance of the efficient (permanent) price over a period that is attributable to a given sub-period or market, adapted here to sequential rather than parallel markets.
- **Signed order-flow surprise.** The residual of an autoregressive model of signed order flow, used as the trade-related shock driving the permanent (efficient) price component.
- **State-space permanent/transitory price decomposition.** A Kalman-filter model that splits the observed futures price into a random-walk efficient price driven by order-flow surprises and non-trade news, and an AR(1) transitory pricing-error component driven by signed order flow.

## Method

Each future's price is modeled daily with a Kalman-filter state-space specification in which the efficient price follows a random walk driven by the surprise component of signed order flow ($\hat O_t$) plus non-trade news, with a price-impact parameter $\lambda$, while a transitory component follows an AR(1) process in the pricing error driven by order flow with parameters $\phi$ and $\theta$. The model is fit separately for each trading day by maximum likelihood via the Kalman filter, with the order-flow autoregression lag chosen by the Akaike Information Criterion. Information share is computed from the variance of daily efficient-price innovations before versus after the event time and averaged over the full 2010-2017 sample; variance decomposition further splits both the permanent and transitory components into trade-related and trade-unrelated (noise) shares. A placebo test repeats the whole exercise on days that are public holidays only in the United States, comparing to the UK and Germany where markets stay open that day.

## Results

- At the 10-minute window, information share for the US Treasury Note futures rose from 43.9% before the US market open to 56.1% after (a 12.2 percentage-point increase); the German Bund rose from 46.3% to 53.7% (7.4 points) and the UK Gilt from 45.4% to 54.6% (9.1 points).
- The increase in information share held at wider windows, though it shrank with window size: at 30 minutes the increase was 4.3 points for the Treasury (47.8% to 52.2%), 3.3 points for the Bund (48.3% to 51.7%), and 4.4 points for the Gilt (47.8% to 52.2%).
- For the permanent (efficient) price, the trade-related share of variance rose modestly after the open for the Treasury (47.2% to 48.0%, +0.7 points) and the Bund (32.7% to 33.3%, +0.6 points), but fell slightly for the Gilt (10.9% to 10.6%), indicating its information gain is not trade-driven.
- For the transitory (pricing-error) component, the trade-related share fell for the Treasury after the open (41.4% to 40.7%) and showed no significant change for the Bund or Gilt.
- On US-only public holidays, information share showed no significant increase around 9:30am, e.g. the Bund's share moved from 52.4% to 47.6% with an insignificant t-statistic of -0.84, unlike the significant increases found on ordinary trading days.
- Trading volume around 9:30am collapsed on US holidays relative to normal days, falling by about 93% for the Treasury, 54% for the Gilt, and 61% for the Bund.

## Limitations

- The authors' own robustness check (the holiday placebo) already shows the effect depends on the US stock market actually being open, but the text read does not otherwise list explicit stated limitations.
- Reader note: the sample covers only three futures contracts (10-year US, UK, and German government bonds), so results may not generalize to other maturities or bond markets.
- Reader note: the event window is limited to the period around the 9:30am US equity open; other intraday informational events (e.g. macro releases, the market close) are not analyzed here.

## Related

- [[concepts/informed-trading|informed trading]]
- [[concepts/order-flow|order flow]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]

## Citation

Ivan Indriawan, Feng Jiao, Yiuman Tse (2019). The Impact of the US Stock Market Opens on Price Discovery of Government Bond Futures.

DOI: 10.1002/fut.22015

Text ingested: `markdown_output/indriawan-2019-impact-us-stock-market-opening-price.md`, converted from `raw/ofi-event-clock/indriawan-2019-impact-us-stock-market-opening-price.pdf`.

Coverage of this summary: Read the full markdown file: abstract, introduction, methodology (state-space model), data section, all reported empirical results sections (price discovery, variance decomposition, holiday placebo), and the conclusion and appendix.

Known problems with the input: No publication year is printed in the visible text (only the January 2010-June 2017 sample period and in-text citation years up to 2018); used the job file's year_hint (2019); No venue/journal name is printed; the presence of 'INSERT TABLE X HERE' placeholders throughout indicates this is a working-paper draft rather than a finished, typeset publication, so venue is left not stated.
<!-- AUTHORED REGION END -->