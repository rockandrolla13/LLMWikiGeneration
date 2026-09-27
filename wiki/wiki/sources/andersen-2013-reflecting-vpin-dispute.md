---
authors:
- Torben G. Andersen
- Oleg Bondarenko
content_hash: sha256:a051d2e719b993ccf467602944790e51dda53925a062911bb8a067bcbd13c6a2
created: 2026-09-27 01:47:00+00:00
page_id: sources/andersen-2013-reflecting-vpin-dispute
page_type: source
publication_venue: CREATES Research Paper Series, Aarhus University (Research Paper
  2013-42)
related:
- concepts/sampling-clocks
- concepts/informed-trading
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/trade-classification
- concepts/high-frequency-trading
- concepts/high-frequency-data
- concepts/market-microstructure
- concepts/vpin
- concepts/bulk-volume-classification
revision_id: 1
schema_version: 2
source_hash: sha256:816391d942abdf85e02caf05d5ebf904c4f3a4603acc0895cdb4757142fdffd4
source_path: markdown_output/andersen-2013-reflecting-vpin-dispute.md
source_type: paper
tags:
- vpin
- flash-crash
- order-flow-toxicity
- trade-classification
- volatility-forecasting
- futures
- econometric-critique
- clock-compares
- asset-futures
- harvest-relevant
title: Reflecting on the VPIN Dispute
updated: '2026-09-27T01:47:00Z'
uuid: fe53038b-426e-5286-8fc1-78ba0bc9eb46
year: 2013
---

<!-- AUTHORED REGION START -->
# Reflecting on the VPIN Dispute

## Summary

This note is Andersen and Bondarenko's response to a rejoinder from Easley, Lopez de Prado and O'Hara (ELO) defending the VPIN metric. The core question is whether VPIN, by construction, is simply proxying for recent trading volume and return volatility rather than capturing genuine order-flow toxicity, and whether it in fact reached a historically extreme level before the May 6, 2010 flash crash as originally claimed.

The authors' approach is econometric: they argue that because volume and volatility are strongly persistent and correlated with each other, almost any activity-related variable will appear to forecast future volatility unless one controls for current volume and volatility levels. They revisit the empirical CDF of VPIN around the flash crash, proposing that the CDF of the daily maximum VPIN value is a more meaningful yardstick for extreme readings than the raw CDF of all intraday VPIN values, and they compare VPIN's apparent forecasting power for volatility to a simple benchmark that uses current realized volatility itself as the predictor. They also review independent evidence on trade-classification accuracy, comparing the standard tick rule to the bulk volume classification scheme that VPIN relies on.

Their central finding is that VPIN did not reach a genuinely unprecedented level before the crash once measured against the daily-maximum benchmark, and that a naive realized-volatility-based predictor produces far fewer false positives than VPIN's reported false positive rate when signaling elevated future volatility. They also report that transaction-based trade classification (the tick rule) is substantially more accurate than the bulk-volume classification used to build VPIN, and that after controlling for realized volatility, VPIN's incremental forecasting power for future volatility disappears.

What is new here relative to the authors' earlier published critique is a direct, detailed rebuttal of ELO's specific counter-arguments: a re-derivation of the daily-maximum-VPIN CDF around the crash timeline, a false-positive-rate comparison against realized volatility as an explicit benchmark, and a review of independent studies showing none of them tests VPIN against any such benchmark or control variable.

## Clock and Sampling

**Compares clocks: the same quantity is measured on two or more clocks.**

See [[concepts/sampling-clocks|Sampling Clocks]].

The note discusses two VPIN implementations built on different sampling clocks: a tick-rule-classified VPIN (TR-VPIN), typically computed on fixed time bars, and a bulk-volume-classified VPIN (BV-VPIN), computed on either time bars or volume/bucket bars; it argues the choice between calendar-time bars and volume/bucket (business time) bars, and between trade-classification schemes, changes whether VPIN ends up forecasting short-term volatility for genuine order-flow reasons or by mechanically resembling realized volatility. The underlying bar/bucket construction itself is not re-derived in this note but is drawn from the authors' companion working paper.

## Data

- **Asset class:** Futures
- **Instruments:** E-mini S&P 500 futures
- **Venue:** not stated
- **Period:** not stated precisely in this note beyond the May 6, 2010 flash-crash day itself; the authors' companion study is described elsewhere as covering more than five years of data
- **Granularity:** tick-level/intraday trade data aggregated into VPIN bars (e.g. a 60-second bar delta is shown in Figure 1); a daily realized-volatility benchmark is also computed

## Features and Measures

- **TR-VPIN.** VPIN computed using the standard tick rule to classify individual transactions as buys or sells.
- **BV-VPIN.** VPIN computed using bulk volume classification, which splits each bar's volume into buy/sell portions via a distributional transform of price changes rather than classifying individual trades.
- **Daily CDF of maximum VPIN.** The empirical cumulative distribution function of each trading day's single highest intraday VPIN reading, used as an alternative to the raw intraday VPIN CDF for judging whether a given VPIN level is historically extreme.
- **Normalized VIX benchmark.** The VIX index divided by its own trailing 21-day moving average, used as a comparison series for how quickly a toxicity/turbulence indicator should rise ahead of a liquidity event.

## Method

The authors combine a re-examination of published VPIN time series around the May 6, 2010 flash crash with an explicit benchmarking exercise. They compute the CDF of the daily maximum VPIN value and track when TR-VPIN and BV-VPIN cross various CDF thresholds on the crash day, comparing this to how many preceding days also crossed the same threshold. Separately, they replicate a false-positive-rate exercise similar to one used to support VPIN, but substitute current realized volatility (the square root of daily realized variance) as the predictor of subsequent above-average volatility, at several percentile thresholds, and compare the resulting false-positive rates to the VPIN-based rate reported elsewhere. They also summarize third-party trade-classification accuracy studies (comparing the tick rule and bulk volume classification) and discuss why, in their account, BV-VPIN's forecasting power for volatility is explained by its mechanical resemblance to realized volatility rather than by genuine order-imbalance content.

## Results

- At 13:30 on the day of the flash crash, TR-VPIN (BV-VPIN) had reached only a 98.5% (94.7%) daily CDF level, a level exceeded on 26 (49) preceding days, i.e. 4.3% (8.1%) of the pre-crash sample, which the authors argue is not the unprecedented historical high originally claimed for VPIN.
- Using current realized volatility itself as the predictor of above-average subsequent volatility produced a false positive rate of 0.0% at both the 95th and 99th percentile thresholds, versus a previously reported 7% false positive rate for VPIN at its 99% CDF threshold.
- A cited independent study (Chakrabarty, Pascual and Shkilko) found the best bulk-volume classification scheme misclassifies 20.3% of trades versus only 9.2% for the standard tick rule, and that the tick rule correctly identifies 91% to 93% of toxic events versus 64% to 70% for bulk-volume-based VPIN.
- In the authors' own companion study on S&P 500 futures, the tick rule misclassified only 2.3% of trades at the volume-bucket level, versus 8.3% for the one-minute time-bar bulk-volume scheme favored in the original VPIN papers.
- After controlling for realized volatility and a volume trend, the authors report that BV-VPIN's incremental predictive power for future volatility is fully subsumed by realized volatility, leaving no independent forecasting content.
- The authors report that switching from time bars to volume/bucket bars, or from bulk-volume to tick-rule classification, reverses several of the original VPIN findings, which they attribute to VPIN's mechanical dependence on volume and volatility rather than to genuine order-flow information.

## Limitations

- This is a reply/dispute note rather than a self-contained new empirical study; much of the primary supporting evidence is drawn from the authors' companion working paper (AB 2013), which is summarized but not fully reproduced here.
- Reader note: as an adversarial rejoinder to a specific counter-response, the framing and selection of evidence are argumentative by genre; the opposing (ELO) side's rebuttal arguments are represented only as characterized by these authors.
- The realized-volatility false-positive benchmark uses a daily horizon chosen, in the authors' words, to neutralize intraday patterns, and is described as a non-optimized, single choice of lag window rather than a tuned comparison.

## Related

- [[concepts/sampling-clocks|Sampling Clocks]]
- [[concepts/informed-trading|informed trading]]
- [[concepts/order-flow-imbalance|order flow imbalance]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/high-frequency-data|high frequency data]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/vpin|VPIN]]
- [[concepts/bulk-volume-classification|Bulk Volume Classification]]

## Citation

Torben G. Andersen, Oleg Bondarenko (2013). Reflecting on the VPIN Dispute. CREATES Research Paper Series, Aarhus University (Research Paper 2013-42).

DOI: 10.1016/j.finmar.2013.08.002

Text ingested: `markdown_output/andersen-2013-reflecting-vpin-dispute.md`, converted from `raw/ofi-event-clock/andersen-2013-reflecting-vpin-dispute.pdf`.

Coverage of this summary: Read the entire markdown text of the note, including the introduction, all four numbered sections, the false-positive-rate table, footnotes, the postscript, and the reference list.

Known problems with the input: One figure (Figure 1, showing TR-VPIN, BV-VPIN and normalized VIX over the flash-crash day) is rendered only as an omitted picture with partially OCR'd axis text, so its content is described here only qualitatively; This document is a CREATES working-paper/rejoinder version (Research Paper 2013-42); it does not itself print a journal name, so venue is given as the working-paper series rather than any later journal publication; The instrument venue (exchange) for the E-mini S&P 500 futures data is not printed in this document, though it is a well-known CME product; it is left as 'not stated' per the source-only rule.
<!-- AUTHORED REGION END -->