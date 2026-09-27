---
authors:
- A. Christian Silva
- Victor M. Yakovenko
content_hash: sha256:438873ca9fbd4800f1b3d40b0b754aa0d414dc74cb4309d17c18b88fef6f2f87
created: 2026-09-27 01:47:00+00:00
page_id: sources/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate
page_type: source
related:
- concepts/trade-clock
- concepts/stylized-facts
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/stochastic-time-change
revision_id: 1
schema_version: 2
source_hash: sha256:3e5546d152bfcc0c7e50964bd5ceaca692b80587ba1eada0ff4ce9a82548e85d
source_path: markdown_output/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate.md
source_type: paper
tags:
- subordination
- stochastic-volatility
- trade-clock
- tick-data
- high-frequency-data
- stylized-facts
- heston-model
- clock-trade
- asset-equity
- harvest-relevant
title: 'Stochastic volatility of financial markets as the fluctuating rate of trading:
  an empirical study'
updated: '2026-09-27T01:47:00Z'
uuid: 5f4dc3b1-9d6a-585c-9746-99f2c35bbb0c
year: 2006
---

<!-- AUTHORED REGION START -->
# Stochastic volatility of financial markets as the fluctuating rate of trading: an empirical study

## Summary

The paper asks whether the well-known non-Gaussian, exponential-tailed shape of stock return distributions over fixed calendar time can be explained by 'subordination': treating returns as approximately Gaussian when measured per completed trade, with the apparent fat tails over calendar time coming instead from randomness in how many trades occur per unit of time. This reframes stochastic volatility as a reflection of a fluctuating rate of trading rather than an independent hidden process.

Using tick-by-tick TAQ transaction data for Intel stock (INTC) over 1999, the authors test three linked predictions: that the distribution of log-returns after a fixed number of trades N is approximately Gaussian; that a specific Fourier/Laplace-transform relation linking the return distribution to the distribution of trade counts holds empirically; and that the empirical distribution of the number of trades in a fixed time interval is exponential-tailed rather than Poisson. They then recombine these empirical pieces to reconstruct the return distribution over fixed time and compare it to the data and to a closed-form Heston stochastic-volatility fit.

The return distribution conditioned on the number of trades is close to Gaussian in its central part, with the expected deviations in the tails; the Fourier/Laplace relation holds approximately, deviating mainly for large argument values; and the empirical distribution of trade counts over a fixed time interval has an exponential tail for large counts and is suppressed near zero, unlike a Poisson process. Combining an exponential trade-count distribution with a Gaussian per-trade return distribution reproduces the Gaussian center and exponential tails seen in the calendar-time return distribution, matching a Heston-model fit to the data.

The paper's contribution is largely confirmatory and diagnostic rather than a new model: it treats the number of trades, rather than volume, as the empirically observable clock underlying stochastic volatility, and it separately tests each analytical step of the subordination argument against high-frequency data instead of only checking the final return distribution's shape.

## Clock and Sampling

**Trade clock: one observation per trade or tick.**

See [[concepts/trade-clock|Trade Clock]].

The paper studies stock log-returns both as a function of the number of completed trades N elapsed (the trade clock) and as a function of fixed calendar time lag delta-t, using tick-by-tick data; it treats the cumulative number of trades over a time interval as the variable whose randomness ('subordination') converts a Gaussian per-trade return distribution into the non-Gaussian, exponential-tailed distribution observed at fixed calendar time lags.

## Data

- **Asset class:** Equities
- **Instruments:** Intel stock (INTC)
- **Venue:** NYSE (TAQ database)
- **Period:** 1 January - 31 December 1999 (intraday data); similar results also reported for 1997
- **Granularity:** tick-by-tick (every transaction); INTC averaged about 2.5 x 10^4 transactions per day in 1999

## Features and Measures

- **Subordination representation.** Writing the return distribution over a fixed time interval as an average of a per-trade Gaussian return distribution over the (random) distribution of how many trades occur in that interval, so the fixed-time return distribution's shape is inherited from the randomness in trade counts.
- **Trade-count distribution K_delta-t(N).** The empirical probability distribution of the number of trades N occurring within a fixed time interval delta-t, used as the key ingredient that is transformed into the shape of the return distribution.
- **Fourier/Laplace consistency check.** A test of the subordination relation using the Fourier transform of the empirical return distribution against the Laplace transform of the empirical trade-count distribution, evaluated directly from the data without assuming a functional form for either distribution.

## Method

The analysis is purely empirical, based on TAQ tick data for INTC in 1999. The authors first verify that the variance of log-returns after N trades grows linearly in N (extracting a coefficient xi), and that the variance and average trade count over a time lag delta-t both grow linearly in delta-t (extracting coefficients eta and theta), then check the approximate consistency relation between these coefficients. They compare the empirical distribution of returns after N trades, and its cumulative and Q-Q plots, to a Gaussian.

They then construct the empirical characteristic function of returns and the empirical Laplace transform of the trade-count distribution directly from the data (as normalized sums over observed values) and plot one against the other to test the subordination relation without assuming any parametric form. Finally, the empirical trade-count distribution over several time lags is examined in log-linear form to characterize its tail behavior, and the resulting reconstructed return distribution is compared to a closed-form fit from the Heston stochastic-volatility model.

## Results

- Linear fits give xi = 2.4 x 10^-8 per trade, eta = 3.8 x 10^3 trades per hour, and theta = 9.5 x 10^-5 per hour, with the relation theta = xi*eta approximately satisfied.
- The distribution of log-returns after N trades is close to Gaussian in the central part for the N values examined, with deviations in the tails as expected.
- The Fourier-transform/Laplace-transform consistency plot lies close to the diagonal for most of its range, deviating mainly in the region corresponding to large return values, indicating the subordination relation holds only approximately.
- The empirical distribution of the number of trades in a fixed interval has an exponential tail for large N and is strongly suppressed for small N, unlike a Poisson distribution.
- Reconstructing the fixed-time return distribution from an exponential trade-count distribution and a Gaussian per-trade distribution reproduces a Gaussian center with exponential tails, matching both the empirical data and a Heston-model fit with 1/gamma = 50 minutes.
- Similar patterns were found in the same stock's 1997 data, though results are reported in detail only for 1999.

## Limitations

- Both the Gaussian per-trade assumption and the subordination relation only hold approximately, with visible deviations for large returns.
- The distribution of returns after N trades only becomes smooth enough to study after roughly a thousand trades, so short trade counts and long (near-daily) time lags could not both be examined.
- The Gaussian hypothesis at the daily horizon could not be verified because too few daily data points are available from a single year of one stock.
- Reader note: the empirical results are drawn from a single stock (Intel) on a single exchange (NYSE) in 1999, with 1997 mentioned only briefly as a robustness check.

## Related

- [[concepts/trade-clock|Trade Clock]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/stochastic-time-change|Stochastic Time Change]]

## Citation

A. Christian Silva, Victor M. Yakovenko (2006). Stochastic volatility of financial markets as the fluctuating rate of trading: an empirical study.

DOI: 10.1016/j.physa.2007.03.051

Text ingested: `markdown_output/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate.md`, converted from `raw/ofi-event-clock/silva-2007-stochastic-volatility-financial-markets-fluctuating-rate.pdf`.

Coverage of this summary: Read the whole converted markdown, including the introduction, the empirical results described around each figure and table, and the reference list.

Known problems with the input: No journal or conference venue is printed in the text; only a dated arXiv-style identifier (physics/0608299, v.2, December 10, 2006) appears, so venue is left blank; The year field uses the version date explicitly printed on the paper (2006) rather than the job's year_hint (2007), since a year is stated in the text.
<!-- AUTHORED REGION END -->