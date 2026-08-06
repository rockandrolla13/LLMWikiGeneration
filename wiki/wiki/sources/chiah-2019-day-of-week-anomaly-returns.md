---
title: 'Day-of-the-week effect in anomaly returns: International evidence'
page_id: sources/chiah-2019-day-of-week-anomaly-returns
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Mardy Chiah
- Angel Zhong
year: 2019
venue: Economics Letters 182, 90-92
tags:
- seasonality
- anomalies
- investor-sentiment
- quality-minus-junk
- international-evidence
sources: []
related:
- concepts/fama-french-factors
- concepts/risk-vs-mispricing
- concepts/factor-investing
mind_map_priority: medium
schema_version: 2
uuid: f4770e30-9294-5731-8757-e1c17028b0b8
content_hash: sha256:b71a31f1a58a1090d1d175d632ced292ac5497a51a8da7aed348fa90ee34b9d7
---

<!-- AUTHORED REGION START -->
# Day-of-the-Week Effect in Anomaly Returns

**Authors:** Mardy Chiah, Angel Zhong

**Year:** 2019 · **Venue:** Economics Letters 182, 90–92

**Institutions:** Swinburne University of Technology; RMIT University

## Summary

An out-of-sample test of Birru's (2018) US finding that anomalies with a speculative leg pay differently by weekday. Using quality-minus-junk (QMJ) as a proxy for the speculative/non-speculative split, the authors show the pattern holds internationally: QMJ pays a positive premium on Monday and a negative one on Friday. Momentum (UMD), which has no clean speculative leg, shows no such pattern.

## Sample

24 developed equity markets aggregated into four regions (Europe, North America, Global ex US, Pacific), July 1993 to December 2017. Daily QMJ returns come from AQR's data library; daily UMD and global risk factors from Ken French's website. The start date is set by QMJ data coverage.

## Findings

Globally (ex US), QMJ earns 0.0537% on Monday (t = 4.98) and −0.0103% on Friday (t = −1.16), decreasing monotonically through the week, for a Monday-minus-Friday spread of 0.064% significant at the 1% level. North America is strongest: 0.0932% Monday (t = 6.05) against −0.0579% Friday (t = −4.79), a spread of 0.1511% (t = 7.72). Across the four regions the Monday QMJ premium is **2.89 times its daily average**.

Pacific is the exception to the monotonic decline: Tuesday's premium (0.0430%) slightly exceeds Monday's (0.0408%), which the authors attribute to the time-zone effect documented by Aggarwal and Rivoli (1989).

The momentum control works as intended. UMD shows no consistent weekday ordering; the Monday-minus-Friday spread is significant only in Europe (0.0631%, t = 2.19), and even there Friday is not the weakest day.

Robustness: risk adjustment with the global Fama–French five-factor model preserves the monotonic decline, and the result holds in two subperiods (1993–2005, 2006–2017) and at country level.

## Why It Matters / Caveats

This is evidence for a mispricing rather than risk reading of QMJ: a premium that moves with the calendar and with investor mood is hard to call compensation for risk. The authors state the caveats themselves — mood is inferred, not measured, and seasonality in institutional trading or strategic news timing are not ruled out. Effect sizes are hundredths of a percent per day with no transaction costs applied, so this is a statement about return patterns, not a tradable strategy. Developed markets only.

## Open Questions

- Does the weekday effect in QMJ show up in trading volume or order flow, which would separate the mood story from an institutional-trading story?
- Would a direct sentiment measure, rather than the weekday proxy, produce the same monotonic ordering?

## See Also

[[concepts/fama-french-factors|Fama-French Factors]] · [[concepts/risk-vs-mispricing|Risk vs Mispricing]] · [[concepts/factor-investing|Factor Investing]]

The null result for UMD here contrasts with the momentum papers in this collection: [[sources/daniel-2016-momentum-crashes|Daniel & Moskowitz (2016)]] and [[sources/blitz-2011-residual-momentum|Blitz, Huij & Martens (2011)]] both find momentum's returns strongly state-dependent, just not along the weekday dimension.

**Not yet written:** `concepts/quality-minus-junk`, `concepts/investor-sentiment`, `concepts/calendar-effects`, `entities/angel-zhong`

<!-- AUTHORED REGION END -->
