---
authors:
- André Meyer
- Ingo Fiedler
content_hash: sha256:66ed2e8809cbda8f83df03665d0306f93179e86538064c11b336ba5d65fd7a47
created: 2026-09-27 01:47:00+00:00
page_id: sources/meyer-2019-discovering-market-prices-which-price-formation
page_type: source
publication_venue: BRL Working Paper Series, No. 2 (Blockchain Research Lab)
related:
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/high-frequency-trading
- concepts/order-imbalance
- concepts/market-making
revision_id: 1
schema_version: 2
source_hash: sha256:5f7765b737d290b09ebc47ace54cc22b924dd49ab3829c7de01ebfa528357b1d
source_path: markdown_output/meyer-2019-discovering-market-prices-which-price-formation.md
source_type: paper
tags:
- price-discovery
- crypto-currency
- limit-order-book
- mid-price
- forecast-accuracy
- high-frequency-trading
- clock-calendar
- asset-crypto
- harvest-core
title: 'Discovering market prices: Which price formation model best predicts the next
  trade?'
updated: '2026-09-27T01:47:00Z'
uuid: 5de88823-6651-5da6-b49b-86e92ab9bdf1
year: 2019
---

<!-- AUTHORED REGION START -->
# Discovering market prices: Which price formation model best predicts the next trade?

## Summary

The paper questions the common practice of treating the price of the last trade (the ticker) as the representative market price, since it looks only at a past event and ignores current order book information such as volume and depth. The authors ask whether alternative price formation models built from level-II order book and trade data can better predict the price of the next trade than the ticker or the widely used mid-price.

Five price formation models are defined and tested: the mid-price, a volume-limited clearing price (vlcp) that averages volume-weighted bid and ask prices up to a fixed volume limit, a price-limited clearing price (plcp) that weights order book prices by their distance from a reference price out to a percentage-depth limit, an adjusted reference price (arp) that corrects the vlcp reference price by a capped, volume-based imbalance factor, and a trade history model (th) that weights past trades by age and volume decay. Each model is computed continuously from live order book and trade data on the crypto exchanges Bitstamp and Coinbase Pro for BTC/USD, ETH/USD and LTC/USD over December 2018, and compared against the next minute's volume-weighted average trade price using five accuracy measures: mean error, mean absolute error, root-mean-square error, mean absolute percentage error, and mean directional accuracy.

Only two of the five models, the mid-price and the vlcp, consistently outperformed the ticker as a predictor of the next minute's price; the vlcp gave the best accuracy in nearly every currency-pair/exchange combination, and its mean directional accuracy reached almost 80% for BTC/USD on Coinbase Pro. The more complex plcp, arp and trade-history models generally did worse than the ticker, and increasing the percentage-depth parameter used in plcp made its forecasts worse rather than better.

What is new is the volume-limited clearing price itself as a reference price, and a systematic head-to-head comparison of several current-information-based price formation models (rather than the historical ticker) for short-horizon prediction, using continuous crypto market data chosen for its ability to trade around the clock without exchange-imposed halts or auctions.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Each price formation model is computed continuously from live level-II order book and trade feeds, but is evaluated on a fixed one-minute calendar clock: the target is the volume-weighted average price (ap) of all trades within a given minute, and each model's value from the end of the previous minute (t-1) is used to forecast that minute's ap (t), i.e. a one-minute-ahead forecast horizon.

## Data

- **Asset class:** Crypto
- **Instruments:** BTC/USD, ETH/USD, LTC/USD
- **Venue:** Bitstamp and Coinbase Pro
- **Period:** 01.12.2018 00:00 to 31.12.2018 23:59
- **Granularity:** level II (full order book depth) and trade data, aggregated into 44,640 minute-level observations per currency pair per exchange

## Features and Measures

- **mid-price (mp).** The midpoint between the best (top-of-book) bid and best ask price.
- **weighted mid-price (wmp).** A mid-price adjusted by the order book imbalance between the volumes of the best bid and best ask.
- **volume-limited clearing price (vlcp).** The average of the volume-weighted average bid price and volume-weighted average ask price, each computed over order book depth up to a fixed volume limit; it equals the mid-price when the top-of-book volume already exceeds that limit.
- **price-limited clearing price (plcp).** A price that weights order book quotes by their distance from a reference price (the vlcp) out to a price limit set by a percentage-depth parameter, so quotes closer to the reference price count more.
- **adjusted reference price (arp).** The vlcp reference price adjusted up or down by a capped correction factor derived from the volume imbalance of orders within a price limit set by a volume-based parameter.
- **trade history model (th).** A representative price built from past trades, each weighted by a function that decays with the trade's age and scales with its volume, up to a fixed age limit beyond which trades are excluded.

## Method

Each of the five price formation models (mid-price, vlcp, plcp, arp, trade history) is calculated continuously from live level-II order book and trade data recorded via exchange APIs for three currency pairs on two exchanges, using external parameters fixed in advance (percentage depth pd = 1, 2 or 3; distance exponent, base parameter, quantity exponent and age exponent all set to 0.75; maximum adjustment 0.003; volume limit 0.5; age limit 180 seconds). Raw order book and trade data were discarded after each model's value was computed and stored, and any gaps caused by exchange connectivity problems or lack of trading were left as missing rather than interpolated. Forecast quality is judged against the ticker price and the actual next-minute volume-weighted average price using five measures: the mean error, mean absolute error, root-mean-square error, mean absolute percentage error, and mean directional accuracy (which counts how often a model gets the sign of the next minute's price move right). Results are reported separately by currency pair and exchange, and the distribution of forecast errors (skewness, kurtosis, range) is also examined for signs of systematic bias or outliers.

## Results

- Only the mid-price and the vlcp consistently outperformed the ticker as predictors of the next minute's volume-weighted average price; the null hypothesis that no model beats the ticker was rejected.
- The vlcp gave the lowest (best) mean absolute error, root-mean-square error and mean absolute percentage error in almost every currency-pair/exchange combination, except BTC/USD on Coinbase Pro where the mid-price was best.
- The vlcp's mean directional accuracy reached almost 80% for BTC/USD on Coinbase Pro, the highest directional accuracy reported in the study.
- The plcp and arp models generally performed worse than the ticker on MAE, RMSE and MAPE, and plcp's accuracy worsened as its percentage-depth parameter increased from 1 to 3.
- The trade history model had the worst mean directional accuracy in nearly every currency pair and exchange, and for BTC/USD on Coinbase Pro also had the worst MAE, RMSE and MAPE of all models tested.
- All price formation models produced leptokurtic (fat-tailed) forecast-error distributions, and none had a forecast-error skewness of exactly zero.
- Forecast errors were consistently smaller on Coinbase Pro, the higher-volume exchange, than on Bitstamp for all three currency pairs, and higher-volume currency pairs also showed lower percentage errors.

## Limitations

- The recorded data had gaps ranging from 7 to 7,653 missing minute observations depending on the currency pair and exchange, due to interface/connectivity problems or a lack of trading, which the authors did not interpolate.
- Only minute-level aggregation was tested; whether the ranking of models holds at shorter or longer intervals is untested.
- Only three crypto currency pairs on two exchanges were studied, so results may not generalize to other exchanges, other crypto currencies, or non-crypto asset classes.
- Model parameters such as percentage depth were tested at only three values (1, 2, 3), so the authors could not determine optimal parameter settings.
- The authors did not test some existing price formation models, such as the micro-price, alongside their five models.
- Reader note: the December 2018 sample period is described by the authors as a phase of sideways movement and relative price stability, so results may not generalize to more volatile or trending market regimes.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/market-making|market making]]

## Citation

André Meyer, Ingo Fiedler (2019). Discovering market prices: Which price formation model best predicts the next trade?. BRL Working Paper Series, No. 2 (Blockchain Research Lab).

DOI: 10.2139/ssrn.3414972

Text ingested: `markdown_output/meyer-2019-discovering-market-prices-which-price-formation.md`, converted from `raw/ofi-event-clock/meyer-2019-discovering-market-prices-which-price-formation.pdf`.

Coverage of this summary: Read the full markdown text end to end: abstract, introduction, all five price formation model definitions, methodology and dataset description, all results tables and their surrounding discussion, the discussion section, limitations, and conclusion.

Known problems with the input: Section 5 (Discussion) contains the sentence 'The models plcp and mid-price in fact delivered superior forecast quality,' which contradicts the paper's abstract, Section 4.2 results and conclusion, all of which state that only the mid-price and the vlcp (not the plcp) outperformed the ticker; this looks like a rendering/OCR substitution of vlcp for plcp in the converted markdown, and this file follows the repeated statement (mid-price and vlcp) rather than this one instance; Most of the paper's model and error-measure equations are rendered as omitted images in the converted markdown, so model definitions here are reconstructed from the surrounding prose rather than the formulas themselves.
<!-- AUTHORED REGION END -->