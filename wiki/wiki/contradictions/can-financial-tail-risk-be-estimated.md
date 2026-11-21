---
content_hash: sha256:d3c1a0cd2ad5ff005c1f02856d13491612f7d6104a98878871a0e389fa6f7e3b
created: '2026-11-21T02:33:11Z'
page_id: contradictions/can-financial-tail-risk-be-estimated
page_type: contradiction
related:
- concepts/extreme-value-theory
- concepts/value-at-risk
- entities/howard-marks
revision_id: 1
schema_version: 2
sources:
- sources/marks-2006-risk
- sources/marks-2007-no-different-this-time-the-lessons-of-07
- sources/marks-2008-whodunit
- sources/pasche-2025-extreme-conformal
status: unresolved
tags:
- risk
- extreme-value-theory
- value-at-risk
- howard-marks
title: Can Models Estimate Financial Tail Risk?
updated: '2026-11-21T02:33:11Z'
updated_by: op_5b3739af413f
uuid: 878e5d02-d4b2-5a9f-a08b-6731db8f2782
---

<!-- AUTHORED REGION START -->
# Can Models Estimate Financial Tail Risk?

**Status:** unresolved

## Claim A: tail statistics can be estimated and extrapolated

The wiki's [[concepts/extreme-value-theory|Extreme Value Theory]] page says EVT "provides statistical tools for accurate estimation and inference in the tails of distributions, enabling extrapolation beyond the observed data range". It names financial crashes among the rare events EVT is the foundation for analysing. The page draws on [[sources/pasche-2025-extreme-conformal|Extreme Conformal Prediction: Reliable Intervals for High-Impact Events]] (2025). [[concepts/value-at-risk|Value-at-Risk]] is the related quantile measure of a loss threshold at a set probability.

## Claim B: models are of very limited use at the extremes

In [[sources/marks-2006-risk|Risk]] (January 2006), Howard Marks says models can tell us what happens most of the time, under "normal circumstances". He then argues that "models and modelers are of very limited utility in measuring investment risk at the extremes, where it really matters". His reasons are non-recurring situations, unknown rules and a largely unlimited range of outcomes.

In [[sources/marks-2007-no-different-this-time-the-lessons-of-07|No Different This Time – The Lessons of ‘07]] (December 2007), he reports that UBS's trading losses exceeded its prior-day VaR on 16 days in the third quarter of 2007. There had been no such day since UBS began to use VaR in 1998. He offers three possible reasons: VaR is not a good measure, the model's period was atypical or too short, or the world changed. He sums up the lesson in bold type: "Markets change, invalidating models." In [[sources/marks-2008-whodunit|Whodunit]] (February 2008) he adds that quants and their models primarily extrapolate the patterns of past markets.

## Where exactly they conflict

Both claims are about whether past data can measure the size and likelihood of extreme financial losses. Claim A says statistical theory makes tail estimation and extrapolation possible. Claim B says that in investing, the extreme cases are where models fail.

## Points that bear on a resolution

These are editorial observations. Neither source offers them as a resolution.

- The EVT page states its main theorem for i.i.d. random variables. Its Limitations list covers threshold choice, asymptotics and small samples, but it does not mention a change in the process generating the data. Marks's argument rests on exactly that: the world changes and invalidates the model.
- The UBS episode concerns one bank's VaR model. Marks does not say which estimation method it used, so it does not show that EVT-based tail estimates would also have failed.
- The two can coexist: a tail estimate can be accurate for a stable process and still fail when behaviour, leverage or market structure shifts.

## What would settle it

An out-of-sample test of EVT-based tail estimates on financial losses across a regime change, such as 2007-2008, compared with the losses that occurred. The wiki has no such source yet.
<!-- AUTHORED REGION END -->