---
authors:
- Roel C.A. Oomen
content_hash: sha256:df03d63711cd35c8dc9921fca0f69e7d17a1cc1a608b06cd69d5ec519cb1f604
created: 2026-09-27 01:47:00+00:00
page_id: sources/oomen-2004-properties-realized-variance-pure-jump-process
page_type: source
publication_venue: Warwick Business School Working Papers Series (WP04-14)
related:
- concepts/sampling-clocks
- concepts/realized-variance
- concepts/market-microstructure-noise
- concepts/market-microstructure
- concepts/high-frequency-data
- concepts/autocorrelation-time-series
- concepts/stochastic-time-change
revision_id: 1
schema_version: 2
source_hash: sha256:3aa334f08d93277b2827f46dab9fdd13f724a572c99cd68a9d34d0032eee7dfb
source_path: markdown_output/oomen-2004-properties-realized-variance-pure-jump-process.md
source_type: paper
tags:
- realized-variance
- market-microstructure-noise
- business-time-sampling
- calendar-time-sampling
- optimal-sampling-frequency
- pure-jump-process
- working-paper
- clock-compares
- asset-equity
- harvest-relevant
title: 'Properties of Realized Variance for a Pure Jump Process: Calendar Time Sampling
  versus Business Time Sampling'
updated: '2026-09-27T01:47:00Z'
uuid: 34696afd-9528-5b58-8310-f935db979827
year: 2004
---

<!-- AUTHORED REGION START -->
# Properties of Realized Variance for a Pure Jump Process: Calendar Time Sampling versus Business Time Sampling

## Summary

The paper asks how market-microstructure noise affects the statistical properties (bias and mean squared error, MSE) of realized variance, and whether sampling prices at fixed calendar-time intervals is the best choice compared with alternative sampling schemes.

Prices are modelled as a compound Poisson (pure jump) process with an MA(q) dependence structure on price increments to capture microstructure noise, and an unspecified, separately estimated trade-intensity process. The paper derives the joint characteristic function of returns under this model and uses it to obtain closed-form bias and MSE expressions for realized variance under general time sampling (GTS) and its two special cases, calendar time sampling (CTS, fixed clock intervals) and business time sampling (BTS, fixed numbers of transactions). The empirical section fits restricted CPP-MA(1) and CPP-MA(2) versions of the model day by day to IBM transaction data, estimating the trade-intensity process non-parametrically, to obtain the daily optimal sampling frequency and the resulting efficiency loss from using CTS instead of BTS.

In the absence of microstructure noise, BTS is shown analytically to always be at least as efficient (lower MSE) as any other sampling scheme, including CTS; with noise present, BTS has larger bias than CTS at intermediate sampling frequencies, but simulation and the IBM data show BTS still achieves lower MSE around the optimal sampling frequency. Using IBM transaction data from January 2000 to August 2003, BTS achieved lower MSE than CTS on every single day in the sample, with the average CTS efficiency loss around 3% but exceeding 30%-40% on days with unusually irregular trading activity. The estimated optimal sampling frequency fell from about 5 minutes in 2000 to about 2.5 minutes in 2003, driven mainly by changes in the noise ratio rather than in the number of transactions.

The contribution is the explicit distinction between sampling scheme (not just frequency) as a source of realized-variance inefficiency, a tractable pure-jump framework in which this can be derived in closed form, and a practical method for estimating a time-varying, day-by-day optimal sampling frequency that is shown by simulation to be robust to parameter measurement error.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The paper defines three sampling schemes for a fixed period: general time sampling (GTS, arbitrary sampling points), calendar time sampling (CTS, equally spaced in wall-clock time, e.g. every 5 minutes), and business time sampling (BTS, equally spaced in cumulative trade count, e.g. every 100 transactions), and analytically and empirically compares realized variance's bias and MSE across them at a given sampling frequency. The object being judged is the accuracy of the realized-variance estimator itself relative to the (unobserved) integrated variance implied by the trade-intensity process, not a forward return prediction.

## Data

- **Asset class:** Equities
- **Instruments:** IBM common stock
- **Venue:** TAQ consolidated data, all reporting exchanges
- **Period:** January 2000 to August 2003 (917 trading days)
- **Granularity:** Transaction (trade) level data restricted to the 9.45-16.00 trading window; a price-reversal filter removes 1358 outlier transactions; the final data set contains 5,522,929 transactions.

## Features and Measures

- **Realized variance.** The sum of squared intraperiod returns over a sampling interval, used as a model-free estimator of price variance.
- **CTS / BTS / GTS sampling schemes.** Ways of choosing return-sampling points: equally spaced calendar-time intervals (CTS), equally spaced counts of transactions (BTS), or arbitrary points satisfying minimal ordering conditions (GTS, of which CTS and BTS are special cases).
- **Optimal sampling frequency.** The sampling frequency that minimises the closed-form MSE expression for realized variance, estimated day by day from the fitted model parameters and intensity process.
- **CTS loss.** The percentage increase in MSE of realized variance from using calendar time sampling instead of business time sampling, evaluated at the optimal sampling frequency.

## Method

The logarithmic price is modelled as a heterogeneous compound Poisson process (CPP) with MA(q)-dependent price increments (the 'restricted CPP-MA(q)' model) and an unspecified trade-intensity process; the paper derives the model's joint characteristic function conditional on intensity and uses it to obtain closed-form return moments and bias/MSE expressions for realized variance under GTS, CTS and BTS. Optimal sampling frequency is found by numerically minimising the MSE expression over the number of sampling points N. Empirically, daily return variance and first- and second-order return autocovariances identify the noise variance, price-innovation variance and MA parameter of the restricted CPP-MA(1)/CPP-MA(2) models from IBM TAQ transaction data; the trade-intensity process is estimated non-parametrically with a quartic kernel and a mirror-image edge correction, with bootstrapped confidence bounds. A simulation exercise checks whether measurement error in the estimated parameters biases the estimated optimal sampling frequency, and a day-by-day linear regression relates the estimated optimal frequency to the noise ratio and transaction count.

## Results

- In the absence of microstructure noise, BTS is proven to achieve the lowest MSE of realized variance among all conceivable sampling schemes, with the efficiency gain over CTS increasing in the variability of trade intensity and in price-innovation variance.
- With first-order microstructure noise, the bias of realized variance under BTS is larger than under any other scheme at intermediate sampling frequencies, but simulation shows BTS still has lower MSE than CTS around the optimal frequency.
- Using IBM transaction data from January 2000 to August 2003, BTS achieved a lower MSE than CTS on every single day in the sample.
- The average CTS efficiency loss relative to BTS was a modest 3% but reached as high as 30%-40% on days with unusually irregular trading activity.
- The estimated optimal sampling frequency fell from about 5 minutes in 2000 to about 2.5 minutes in 2003, with considerable day-to-day variation.
- A regression of the log optimal sampling frequency on trade intensity and the noise ratio found that transaction count alone explained less than 25% of the variation, the noise ratio alone explained just under 70%, and the two together explained about 99.998% (R-squared).
- Simulation showed that measurement error in the estimated model parameters did not bias the estimated optimal sampling frequency, unlike results reported for a related framework in Bandi and Russell (2003).

## Limitations

- The model assumes Gaussian returns in business time and Gaussian price/noise innovations; the author notes transaction-level returns are more accurately multinomial due to price discreteness, though he argues the misspecification washes out under temporal aggregation.
- The 'feasible' BTS scheme used empirically substitutes an estimate of trade intensity for the (unobservable) true intensity process, so BTS as implemented is itself subject to estimation error.
- The empirical analysis is confined to a single stock (IBM) over 2000-2003; results for other names or later market-structure regimes are not reported.
- Reader note: the headline efficiency comparisons (e.g. the 3% average CTS loss) are evaluated at the BTS-optimal sampling frequency rather than a separately-optimised CTS frequency, though the paper notes the two optima lie close together in most cases.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/realized-variance|realized variance]]
- [[concepts/market-microstructure-noise|market microstructure noise]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/autocorrelation-time-series|autocorrelation time series]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]

## Citation

Roel C.A. Oomen (2004). Properties of Realized Variance for a Pure Jump Process: Calendar Time Sampling versus Business Time Sampling. Warwick Business School Working Papers Series (WP04-14).

Text ingested: `markdown_output/oomen-2004-properties-realized-variance-pure-jump-process.md`, converted from `raw/ofi-event-clock/oomen-2004-properties-realized-variance-pure-jump-process.pdf`.

Coverage of this summary: Read the entire markdown file (working paper, under the threshold): abstract, introduction, the model section, both sampling-scheme theory sections (absence and presence of noise), the full empirical section on IBM TAQ data, and the conclusion; did not attempt to verify the picture-omitted equations against the original PDF.

Known problems with the input: Most equations, the formal statements inside propositions/theorems, and figures are rendered as '==> picture... intentionally omitted <==' by the PDF-to-markdown conversion, so exact closed-form bias/MSE expressions could not be transcribed and are described only in words; Table 1 and Table 2 in the markdown show visibly mis-parsed rows/columns compared to the surrounding prose description; numbers quoted here were cross-checked against the prose rather than the raw table cells where the two might disagree.
<!-- AUTHORED REGION END -->