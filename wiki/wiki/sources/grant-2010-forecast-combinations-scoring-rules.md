---
title: Finding Profitable Forecast Combinations Using Probability Scoring Rules
page_id: sources/grant-2010-forecast-combinations-scoring-rules
page_type: source
source_path: markdown_output/1-s2.0-S0169207010000051-main.md
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Andrew Grant
- David Johnstone
year: 2010
venue: International Journal of Forecasting
tags:
- scoring-rules
- forecast-combination
- kelly-betting
- probability-forecasting
- expert-selection
sources: []
related:
- concepts/strictly-proper-scoring-rules
- concepts/logarithmic-score
- concepts/forecast-scaling-and-combination
- concepts/fractional-kelly-position-sizing
- concepts/calibration
mind_map_priority: medium
schema_version: 2
uuid: 30ff5fde-1079-5f9b-8a65-33eaa41b87d8
content_hash: sha256:3fed7347f55c5df01e9f7af3a04b6603445b2bf5b2bae6a05cda5a75ff66f257
---

<!-- AUTHORED REGION START -->
# Finding Profitable Forecast Combinations Using Probability Scoring Rules

**Authors:** Andrew Grant, David Johnstone

**Year:** 2010 · **Venue:** International Journal of Forecasting 26 (2010) 498–510

**Institution:** School of Business, University of Sydney

## Summary

An improper scoring rule can still be useful for picking forecasters. That is the
paper's surprise, and it cuts against the usual advice.

The setting is the Monash University probabilistic football tipping competition,
where entrants state a probability that the home team wins each Australian
Football League match. Seven seasons, 1999–2005, 176 games per season, and after
dropping anyone who skipped games, 41–50 forecasters per season. Bets are placed
on paper against real bookmaker odds using fractional
[[concepts/fractional-kelly-position-sizing|Kelly]] sizing.

Forecasters are ranked four ways: the [[concepts/logarithmic-score|log score]],
a raw Brier score, a "categorical" score that truncates each probability to 0 or
1 and counts misclassifications, and a "Kelly score" measuring the paper profit
the forecaster's own probabilities would have earned.

## Findings

Betting on any single forecaster loses money. Returns are negative almost
everywhere; full-Kelly is worst, its best seven-season outcome being a 67%
geometric average loss per season. Scoring rules still beat chance at selecting
an individual — random selection does worse than any rule — but the edge is not
large enough to clear the bookmaker's spread.

Pooling three forecasters changes the picture. Averaging the probabilities of the
top-ranked forecaster under the log, Kelly and categorical scores, and betting at
40% Kelly, yields a geometric average return of 16.6% per season: $1 becomes
$2.93 over seven seasons, net of the betting agency's spread. Bootstrap p-values
for this pool sit around 2%; the incremental contribution of the categorical
pick alone has a p-value near 7%.

Two results sharpen this. Adding the Brier-best forecaster to the {log, Kelly}
pair is actively **counterproductive** — its incremental p-value runs 0.690 to
0.849 — apparently because Brier and log reward the same profile of skill.
And expanding the pool to six forecasters destroys the profit entirely: the
pooled probability drifts toward the bookmaker's spread and rational bets stop
existing.

## Why It Matters

The diversification logic is the transferable part. A pool wants a member who
contributes something idiosyncratic, not more of the same. The categorically
strongest forecaster is bold — frequently on the right side of 0.5 with extreme
probabilities — and therefore punished by the log score in isolation, yet
valuable once averaged with others.

## Open Questions

- The paper offers no theory for why one *randomly* chosen third forecaster also
  improves the two-forecaster pool.
- Whether the categorical rule keeps its usefulness in pools larger than three
  is untested, and the six-forecaster result suggests the window is narrow.

## See Also

[[concepts/strictly-proper-scoring-rules|Strictly Proper Scoring Rules]] ·
[[concepts/forecast-scaling-and-combination|Forecast Scaling and Combination]] ·
[[concepts/calibration|Calibration]]

**Not yet written:** `brier-score`, `categorical-scoring-rule`,
`opinion-pooling`, `prediction-markets`, `kelly-criterion`.
<!-- AUTHORED REGION END -->

