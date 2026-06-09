---
title: On-Line Compression Models (OCM)
page_id: concepts/on-line-compression-models
page_type: concept
revision_id: 1
created: 2026-05-24T16:00:00Z
updated: 2026-05-24T16:00:00Z
tags: [conformal-prediction, on-line-learning, sufficient-statistics, kolmogorov, vovk]
sources: [sources/vovk-2005-algorithmic-learning, sources/shafer-2007-cp-tutorial]
related: [concepts/conformal-prediction, concepts/exchangeability, concepts/state-space-models]
mind_map_priority: medium
---

# On-Line Compression Models (OCM)

**On-Line Compression Models** generalise the [[concepts/exchangeability|exchangeability]] assumption underlying [[concepts/conformal-prediction|conformal prediction]] to any data-generating structure expressible via *sufficient statistics that summarise the past*. Introduced by Vovk in Chs. 8-9 of [[sources/vovk-2005-algorithmic-learning|*Algorithmic Learning in a Random World*]], they sit within Kolmogorov's broader programme of statistical modelling via repetitive structures.

## The Construction

An OCM is defined by:

- **A summary space.** Where the compressed past lives.
- **A summarising function** that updates the summary given a new observation.
- **A one-step backward kernel.** The distribution of the next-to-last observation given the new summary.

The conformal recipe lifts to any OCM: define a nonconformity measure on the summary space, compute p-values via the backward kernel, build valid prediction sets.

## Special Cases

- **Exchangeability model.** Summary = the bag (multiset) of all observations; backward kernel is uniform on permutations.
- **Gaussian linear model.** Summary = sufficient statistics for a Gaussian regression; backward kernel is the joint Gaussian conditional. Conformal prediction recovers exactly the classical t-interval *with stronger on-line validity*.
- **Markov model.** Summary = the most recent observation; backward kernel is the transition kernel.
- **Hypergraphical / junction-tree models.** Graphical-model versions for structured data.

## Why It Matters

OCMs are the right level of generality for "CP works because of some statistical structure, not because of i.i.d. data". They let you apply conformal-style reasoning to time series with known dependence structure, to graphical models, and to dependent panels — *without* the exchangeability assumption that standard CP requires.

In practice, modern CP-for-time-series methods ([[concepts/enbpi|EnbPI]], [[concepts/adaptive-conformal-inference|ACI]], [[concepts/weighted-conformal-prediction|WCP]]) often achieve the same end via different routes (bootstrap, online α-update, reweighting). OCMs remain the cleanest theoretical scaffold and are the framework of choice in [[sources/fontana-2023-cp-unified-review|Fontana et al.'s 2023 review]].

## Sources

- [[sources/vovk-2005-algorithmic-learning]] — Chs. 8 and 9.
- [[sources/shafer-2007-cp-tutorial]] — accessible introduction with worked Gaussian-linear example.

## Related Concepts

- [[concepts/conformal-prediction]]
- [[concepts/exchangeability]]
- [[concepts/state-space-models]]
- [[concepts/mondrian-conformal-prediction]]
