---
authors:
- Marcin Niedużak
- Mateusz Pipień
content_hash: sha256:ba8475480bcd26e4d7122745c7e78c99ebd2dbe4c228918e6895f20bc12c31c4
created: 2026-09-27 01:47:00+00:00
page_id: sources/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych
page_type: source
publication_venue: Przegląd Statystyczny, R. LXI, Zeszyt 2, 2014
related:
- concepts/volume-clock
- concepts/informed-trading
- concepts/trade-classification
- concepts/market-microstructure
- concepts/order-flow-imbalance
- concepts/liquidity-risk
- concepts/vpin
- concepts/bulk-volume-classification
revision_id: 1
schema_version: 2
source_hash: sha256:acc31ace5f2047243f7521312848ece65b1ebb85385c2b0d6f870a3df1770e00
source_path: markdown_output/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych.md
source_type: paper
tags:
- informed-trading
- vpin
- market-microstructure
- volume-bars
- trade-classification
- warsaw-stock-exchange
- return-distribution
- clock-volume
- asset-equity
- harvest-relevant
title: Ekonometryczna analiza prawdopodobieństwa zawarcia transakcji wynikających
  z napływu informacji – wpływ założeń co do rozkładu stóp zwrotu na zmienność miary
  VPIN
updated: '2026-09-27T01:47:00Z'
uuid: 57887400-5f61-59c0-b03f-81ee9929301e
year: 2014
---

<!-- AUTHORED REGION START -->
# Ekonometryczna analiza prawdopodobieństwa zawarcia transakcji wynikających z napływu informacji – wpływ założeń co do rozkładu stóp zwrotu na zmienność miary VPIN

## Summary

The paper studies informed trading on the Warsaw Stock Exchange using the VPIN (volume-synchronized probability of informed trading) measure, which is built on the EKOP/PIN model of Easley, Kiefer, O'Hara and Paperman and estimated via the Bulk Volume Classification (BVC) trade-classification algorithm.

BVC classifies each equal-sized volume bucket's shares into buy- and sell-initiated portions using the standardized price change within the bucket, mapped through the cumulative distribution function of an assumed return distribution; the original BVC proposal assumed a normal distribution. The authors instead compare three assumptions for that distribution: normal, Student-t with a fixed, arbitrarily low degrees of freedom, and Student-t with degrees of freedom estimated period-by-period from the sample's own kurtosis.

Using intraday data on KGHM Polska Miedź, a single, highly liquid Warsaw-listed stock, over about five months, the authors compute VPIN under each distributional assumption and compare the resulting descriptive statistics and time paths.

The main finding is that VPIN under the normal assumption and under the estimated-degrees-of-freedom Student-t assumption are close to each other, while forcing a low, fixed degrees of freedom pulls VPIN's average down and makes it noticeably more volatile and wide-ranging; the authors frame this as evidence that the return-distribution assumption inside BVC is not innocuous for the resulting informed-trading measure.

## Clock and Sampling

**Volume clock: one observation per unit of volume traded.**

See [[concepts/volume-clock|Volume Clock]].

Raw trade-level quotes are first aggregated within each session (9:00 to 17:35) into five-minute sub-periods, using the average trade price and summed volume in each sub-period; these sub-period series are then regrouped into equal-size volume buckets of exactly 10 000 shares, and the Bulk Volume Classification algorithm splits each bucket's volume into buy- and sell-initiated portions from the standardized price change within the bucket, before VPIN is computed as a rolling measure of the absolute buy/sell imbalance across a fixed number of consecutive volume buckets.

## Data

- **Asset class:** Equities
- **Instruments:** KGHM Polska Miedź S.A. (single Warsaw-listed stock).
- **Venue:** Warsaw Stock Exchange (Giełda Papierów Wartościowych w Warszawie).
- **Period:** 2 January 2013 to 31 May 2013 (101 trading days).
- **Granularity:** Raw intraday trade data aggregated into 5-minute sub-periods (103 per session), then regrouped into volume buckets of 10 000 shares each.

## Features and Measures

- **EKOP / PIN model parameters.** The structural parameters of the Easley-Kiefer-O'Hara-Paperman model of order arrivals (the arrival rate of uninformed traders, the arrival rate of informed traders, the probability of a new-information event, and the probability that new information is bad news), from which the probability of informed trading is derived.
- **Bulk Volume Classification (BVC).** A probabilistic trade-classification algorithm that splits the volume in each equal-size volume bucket into buy- and sell-initiated portions using the bucket's standardized price change passed through the cumulative distribution function of an assumed return distribution, avoiding the need for tick-by-tick trade-direction data.
- **VPIN (volume-synchronized probability of informed trading).** A rolling measure of order-flow imbalance computed from BVC-classified buy and sell volumes across a fixed number of consecutive equal-size volume buckets, used as a proxy for the intensity of informed trading.

## Method

The authors estimate VPIN separately under three assumptions for the return distribution used inside the Bulk Volume Classification step: a normal distribution, a Student-t distribution with a fixed degrees-of-freedom parameter of 0,25 (following Easley, López de Prado and O'Hara), and a Student-t distribution whose degrees of freedom are instead estimated for each five-minute sub-period from the sample kurtosis of returns, with kurtosis near 3 mapped to 100 degrees of freedom and any estimated value below 4 floored at 4 degrees of freedom. For each of the three distributional assumptions, the resulting buy/sell volume split is used to compute VPIN over consecutive volume buckets, and the authors compare descriptive statistics (mean, median, minimum, maximum, standard deviation, coefficient of variation, excess kurtosis) and the time series of VPIN across the three assumptions.

## Results

- The full sample covers 101 trading days from 2 January 2013 to 31 May 2013, with 171 187 raw trade observations on KGHM Polska Miedź.
- Mean VPIN under the normal-distribution assumption was 0,682691 (median 0,680310, minimum 0,137730, maximum 1, standard deviation 0,159832).
- Mean VPIN under the Student-t distribution with degrees of freedom estimated from sample kurtosis was 0,671002, close to the normal-distribution result (median 0,666233, standard deviation 0,162676).
- Mean VPIN under a fixed Student-t distribution with 0,25 degrees of freedom was materially lower and more dispersed, at 0,496400 (median 0,464566, standard deviation 0,196307), with a coefficient of variation of 39,54610 versus 23,41213 for the normal case.
- Under the normal and estimated-degrees-of-freedom Student-t assumptions, VPIN mostly ranged between 0,5 and 0,9 and between 0,5 and 0,8 respectively, while under the fixed 0,25-degrees-of-freedom Student-t it ranged more widely, between 0,1 and 1,0.
- A sharp rebound of about 35% relative to neighbouring values occurred at VPIN observation 389, corresponding to 12 April 2013, coinciding with a strong price drop and the start of a stabilization in the stock's price.

## Limitations

- The study covers a single stock, KGHM Polska Miedź, chosen for its high investor interest and liquidity, over roughly five months.
- The authors state that justifying the choice of degrees-of-freedom assumptions for the Student-t case was left outside the scope of this paper and flagged for future research.
- Reader note: the converted markdown has heavy corruption of Polish diacritics, and the exact formula used to estimate degrees of freedom from sample kurtosis could not be reliably reconstructed from the garbled text.

## Related

- [[concepts/volume-clock|Volume Clock]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/liquidity-risk|liquidity risk]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]

## Citation

Marcin Niedużak, Mateusz Pipień (2014). Ekonometryczna analiza prawdopodobieństwa zawarcia transakcji wynikających z napływu informacji – wpływ założeń co do rozkładu stóp zwrotu na zmienność miary VPIN. Przegląd Statystyczny, R. LXI, Zeszyt 2, 2014.

DOI: 10.59139/ps.2014.02.3

Text ingested: `markdown_output/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych.md`, converted from `raw/ofi-event-clock/nieduzak-2014-ekonometryczna-analiza-prawdopodobienstwa-zawarcia-transakcji-wynikajacych.pdf`.

Coverage of this summary: Read the entire markdown file: introduction, informed-trading/EKOP background, the Bulk Volume Classification section, the VPIN section, the empirical results section including both descriptive-statistics tables, the summary, and both the Polish and English abstracts.

Known problems with the input: Polish diacritics are rendered as replacement characters (mojibake) throughout the converted markdown, corrupting many words and at least one formula; the degrees-of-freedom estimation formula could not be reliably reconstructed and is described only qualitatively; Title and author names are reproduced using the accented-Polish spelling given in the job file's title_hint, since the converted markdown itself shows the title and body text with corrupted diacritics.
<!-- AUTHORED REGION END -->