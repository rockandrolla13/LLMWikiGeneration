---
authors:
- Alexey Feigin
content_hash: sha256:1b64baa524e3358fc0b2786d7ecb406f8f1bdbc8a346caf7dd46d02a0b8197bf
created: 2026-09-27 01:47:00+00:00
page_id: sources/feigin-2015-assessing-informed-trading-measures-against-material
page_type: source
publication_venue: PhD Thesis, University of Technology, Sydney, Accounting Discipline
  Group
related:
- concepts/informed-trading
- concepts/limit-order-book
- concepts/trade-classification
- concepts/adverse-selection
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:54517b2b62dacab2c69be05b5f2a1a60e085aafbc38e3aefc99d6dfbf8e54def
source_path: markdown_output/feigin-2015-assessing-informed-trading-measures-against-material.md
source_type: paper
tags:
- informed-trading
- pin-model
- limit-order-book-slope
- mining-stocks
- asx
- material-news
- measure-validation
- insider-trading
- clock-calendar
- asset-equity
- harvest-relevant
title: Assessing informed trading measures against material mining progress reports
updated: '2026-09-27T01:47:00Z'
uuid: 3e8a7b3c-dbd0-5975-8e37-87ff859e289b
year: 2015
---

<!-- AUTHORED REGION START -->
# Assessing informed trading measures against material mining progress reports

## Summary

The thesis asks whether existing econometric measures of informed trading, PIN and limit order book slope, genuinely detect informed trading, given that the underlying phenomenon is unobservable and cannot be directly validated. Rather than relying only on correlations with other economic variables as prior literature does, the author builds a testable framework from three minimal assumptions about informed-trader behaviour: news acquisition never reverses, traders respond to bigger incentives with more activity, and informed traders never come to dominate the whole market. From these assumptions, periods before highly material announcements should show relatively high informed trading, and periods before non-material announcements should show relatively low informed trading.

The method builds an experimental sample (periods before the most extreme two-day price reactions to progress-report announcements), a control sample (periods before flat-reaction announcements), and a random sample of ordinary stock-periods, using Australian mining stocks and Mining Development Stage Entities (MDSEs) listed on the ASX between January 1995 and June 2011, chosen because material news is comparatively rare and high-stakes there. A candidate informed-trading measure is computed for every sample period, fed into a Logit classifier trained to separate the experimental from the control sample, then applied to the random sample to obtain an unconditional detection rate. Two effectiveness scores are then computed for the classifier: a predictive-power score based on true/false positive and negative rates, and an information-theoretic uncertainty coefficient that measures how much the classifier's detection actually reduces uncertainty about the true (unobservable) level of informed trading.

Applied to PIN (in both its 1996 and 2002 forms, using 60 trading days of pre-event buyer/seller-initiated trade counts), the measure is found not to work as theorised: its Logit coefficient is negative in almost every fitted model, meaning higher raw PIN values are associated with the low-informed-trading (control) sample rather than the high-informed-trading sample, and several models even fail a basic consistency check tying the classifier's detection rate on random data to its rates on the experimental and control samples. The author traces this to buyer-initiated trading rising sharply before both good-news and bad-news announcements, contrary to PIN's assumption that trade initiation should move in one direction only ahead of bad news. Limit order book slope (using pre-event windows of intraday snapshots) performs somewhat better: several of its Logit models are statistically significant and pass the consistency check, giving weak but genuine predictive power, but the measure's information is completely dominated by conditions at the best bid and ask, and it cannot tell whether detected informed trading is on the buy or the sell side.

What is new is the general assessment method itself, an assumption-based framework for stress-testing any informed-trading measure by whether it also fires under conditions where informed trading is deliberately expected to be absent, together with the specific finding that PIN, despite widespread prior use, is not consistent with these assumptions in a low-liquidity mining setting, while order book slope offers only weak, direction-blind signal.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

PIN is estimated from daily counts of buyer- and seller-initiated trades over a fixed 60-trading-day window before each sample event; limit order book slope is instead sampled from intraday order-book snapshots taken at six fixed clock times per trading day (10:30, 11:30, 12:30, 13:30, 14:30 and 15:30) and averaged into a daily value over a fixed 25-trading-day pre-event window. The forecasting horizon in both cases is not a price move at a fixed lag, but classification of a stock-period as belonging to a high- or low-informed-trading sample, where high/low status is defined ex post from the size of a two-trading-day price reaction (days 0 to 2) around a mining progress-report announcement.

## Data

- **Asset class:** Equities
- **Instruments:** ASX-listed mining companies, mostly Mining Development Stage Entities (MDSEs), identified by GICS sub-code 15104000 (metals and mining) from July 2001, and by ASX gold/other-metals industry groups before that
- **Venue:** Australian Securities Exchange (ASX); data sourced from SIRCA Core Research Data and Thomson Reuters
- **Period:** January 1995 to June 2011
- **Granularity:** daily buyer/seller-initiated trade counts for PIN (60-trading-day pre-event windows); intraday limit order book snapshots at six fixed times per day for order book slope (25-trading-day pre-event windows); event samples built from 5000 most extreme two-day price reactions each for the UP and DOWN samples, with matching FLAT and RANDOM samples

## Features and Measures

- **PIN1996 / PIN2002.** The probability of informed trading, estimated from a sequential trade model fit by maximum likelihood to daily counts of buyer- and seller-initiated trades; PIN2002 extends PIN1996 by allowing separate buyer and seller arrival rates for uninformed trading.
- **Limit order book slope (SLOPE, SLOPE1, SCALED_SLOPE).** A measure of the elasticity of cumulative order-book depth with respect to price on the bid and ask sides; lower elasticity (volume building up slowly away from the midpoint) is taken as a sign of higher information asymmetry, following Glosten's model of cautious limit order submission.
- **Predictive power.** An effectiveness score built by the author for this thesis, equal to the sum of a classifier's true-positive and true-negative detection rates, used to judge how well a fitted measure distinguishes high from low informed trading.
- **Uncertainty coefficient.** An information-theoretic effectiveness score built from the expected Kullback-Leibler divergence between the classifier's detection outcome and the underlying informed-trading state, normalised by entropy, giving a 0-to-1 measure of how much a classifier's output actually informs about the true state.

## Method

Stock-periods are sorted into an experimental sample (highest-magnitude two-day price reactions around progress-report announcements, split into UP and DOWN sub-samples by direction), a control sample (flattest reactions, the FLAT sample), and a random sample of ordinary mining stock-periods. Each candidate measure (PIN or order book slope, in several variants) is computed over its own pre-event window for every period in every sample, then fit via a Logit model to discriminate the experimental sample from the control sample for each relevant directional pairing (UP-FLAT, DOWN-FLAT, and UP-DOWN or DOWN-UP where the measure is meant to be directional). Each fitted Logit model is then applied to the random sample to obtain an unconditional detection rate, from which a prior probability of informed trading is backed out via Bayes' theorem. The thesis checks whether the classifier's true- and false-positive rates are internally consistent with this unconditional rate (a violation is treated as falsifying the measure against the assumptions), then reports predictive power and the uncertainty coefficient for every non-falsified model, alongside a discussion of Type I and Type II error rates.

## Results

- PIN's Logit coefficient is negative in almost every fitted model (the opposite sign to what PIN theory implies), and several PIN models fail the basic consistency check tying the random-sample detection rate to the experimental- and control-sample detection rates, so they are treated as falsified with respect to the assumptions.
- For a representative PIN1996 model (UP-FLAT pairing), the false-positive rate is 0.655 and the true-positive rate is 0.710 against an unconditional detection rate of 0.679, showing that a detection barely moves the prior probability of informed trading (0.426) at all.
- The best-performing PIN variant, PIN_SELL1996 fit to the DOWN-FLAT sample pairing, still only reaches an absolute prior gain of 5.8% on the positive side and 10% on the negative side, with an uncertainty-coefficient information gain of 0.029.
- Buyer-initiated trading frequency is found to rise in the run-up to both UP (good-news) and DOWN (bad-news) sample events, which the author argues directly contradicts the PIN assumption that only one side's trade initiation should rise ahead of bad news.
- Limit order book slope models are statistically significant in most fitted specifications and are not falsified for the UP-FLAT and DOWN-FLAT pairings, but every slope model fit to the UP-DOWN pairing does violate the consistency check, meaning slope cannot tell buyer-driven from seller-driven informed trading.
- Working order book slope models show predictive power of 1.179 to 1.305 (against a maximum possible score of 2 for a perfect measure), with implied prior probabilities of informed trading between 0.248 and 0.553, and the strongest uncertainty-coefficient information gain is 0.061, for SLOPE and SCALED_SLOPE fit to the DOWN-FLAT pairing.
- The elasticity signal in limit order book slope is found to be dominated by conditions at the single best bid and best ask tick, rather than by deeper levels of the book.

## Limitations

- The whole framework rests on three assumptions about informed-trader behaviour that the author states explicitly cannot themselves be directly tested; a researcher who rejects those assumptions would not accept the thesis's conclusions.
- The assumptions only say when informed trading is more or less likely, not how much of it exists, so it remains possible that genuine informed trading is present but too rare or well concealed for any measure to detect it in this design.
- The sample is restricted to the Australian mining industry, dominated by small, thinly-traded MDSEs, and the author explicitly leaves generalisation to other industries or markets to future research.
- The sample period spans the global financial crisis (affecting the DOWN sample) and an Australian mining boom (affecting the UP sample), which could in principle bias materiality-based sample construction even though the author argues a general informed-trading measure should not be confused by either.
- Reader note: PIN and order book slope are tested with fixed pre-event windows (60 and 25 trading days respectively) chosen from visual inspection of trading-pattern charts rather than from an independent, out-of-sample selection procedure.

## Related

- [[concepts/informed-trading|informed trading]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/trade-classification|trade classification]]
- [[concepts/adverse-selection|adverse selection]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Alexey Feigin (2015). Assessing informed trading measures against material mining progress reports. PhD Thesis, University of Technology, Sydney, Accounting Discipline Group.

Text ingested: `markdown_output/feigin-2015-assessing-informed-trading-measures-against-material.md`, converted from `raw/ofi-event-clock/feigin-2015-assessing-informed-trading-measures-against-material.pdf`.

Coverage of this summary: Read the abstract, introduction, background, the full research method and effectiveness-metric derivation (Section 3), the full application/sample-formation section (Section 4), the descriptions of PIN and limit order book slope (Section 5), the full results and discussion section (Section 6), limitations (Section 7) and conclusion (Section 8). Did not read the reproduced figures/tables section, the detailed per-model appendices (B-G), or the non-thesis regulatory reference material reproduced in Appendix I onward.

Known problems with the input: Most inline mathematical formulas (PIN likelihood equations, order book slope elasticity formulas, the uncertainty-coefficient derivation) are rendered as omitted pictures or garbled OCR fragments in the converted markdown, so exact equation forms could not be verified beyond the plain-language description already in the text; The markdown file bundles a large, unrelated regulatory reference document (the JORC Code for mineral resource reporting, and several ASX rule appendices) as later appendices; these were not treated as part of the thesis's own research content and were not read or extracted from.
<!-- AUTHORED REGION END -->