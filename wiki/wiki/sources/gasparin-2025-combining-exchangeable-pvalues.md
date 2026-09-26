---
title: Combining exchangeable p-values
page_id: sources/gasparin-2025-combining-exchangeable-pvalues
page_type: source
source_path: markdown_output/gasparin-2025-combining-exchangeable-pvalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Matteo Gasparin
- Ruodu Wang
- Aaditya Ramdas
year: 2025
venue: Proceedings of the National Academy of Sciences (2025)
tags:
- p-value-merging
- exchangeability
- sample-splitting
- randomized-tests
sources: []
related:
- concepts/p-value-merging
- concepts/exchangeability
- concepts/e-value
- entities/ruodu-wang
- entities/aaditya-ramdas
mind_map_priority: medium
schema_version: 2
uuid: 473a92b4-9dd5-5be0-ba5f-5576ba2c9c8a
content_hash: sha256:4ed2bf85cf7c37fe6ae85a78df847d0fd6ee7025e1e67af805da04aea25cc113
---

<!-- AUTHORED REGION START -->
# Combining Exchangeable P-values

**Authors:** Matteo Gasparin, [[entities/ruodu-wang|Ruodu Wang]], [[entities/aaditya-ramdas|Aaditya Ramdas]]

**Year:** 2025 · **Venue:** PNAS

## Summary

Repeated sample splitting produces p-values that are **exchangeable** but not independent. Exchangeability is stronger than arbitrary dependence and weaker than independence, and this paper shows it is enough to improve on the standard merging rules — without touching the famous constants.

## The unifying view

Every existing arbitrary-dependence rule is: calibrate each p-value into an e-value, average the e-values, apply Markov. Swapping Markov's inequality for a stronger one under [[concepts/exchangeability|exchangeability]], or for a randomized version, delivers the improvements automatically.

## The rules

For the classical rules, the improvement takes a uniform shape: replace the statistic by the **running minimum over prefixes** of the p-value sequence.

| Rule | Arbitrary dependence | Exchangeable |
|---|---|---|
| Arithmetic mean | $2A(\mathbf{p})$ | $2\min_{m\le K} A(\mathbf{p}_m)$ |
| Geometric mean | $e\,G(\mathbf{p})$ | $e\min_{m\le K} G(\mathbf{p}_m)$ |
| Harmonic mean | $(T_K+1)H(\mathbf{p})$ | $(T_K+1)\min_{m\le K} H(\mathbf{p}_m)$ |

with $T_K=\log K+\log\log K+1$ for $K\ge2$. A randomized column exists too, dividing by a uniform draw.

The multiplier 2 is **not** reduced — that is known to be impossible — so the gain comes entirely from the prefix minimum. A structural result explains why order matters: any *symmetric* exchangeable rule is automatically valid under arbitrary dependence, so improvement requires processing the p-values in a fixed order, asymmetrically.

The rules work on a stream and you may stop whenever you like. In one worked example with $K=3$ at $\alpha=0.05$, power rises from 0.5101 to 0.6207.

## Why It Matters

Sample splitting is standard practice and its outputs are exchangeable by construction. This says you have been leaving power on the table by treating them as arbitrarily dependent, and the fix is a one-line change to the statistic.

## See Also

[[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/exchangeability|Exchangeability]] · [[concepts/e-value|E-value]]

Builds on the duality of [[sources/vovk-2021-admissible-merging-pvalues|Vovk, Wang & Wang (2022)]].
<!-- AUTHORED REGION END -->
