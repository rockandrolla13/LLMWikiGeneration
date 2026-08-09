---
title: 'Predicting Corporate Bond Returns: Merton Meets Machine Learning'
page_id: sources/bali-2022-bond-ml
page_type: source
source_type: working-paper
revision_id: 1
source_path: markdown_output/bali-2022-bond-ml.md
created: 2026-08-07 00:00:00+00:00
updated: '2026-08-07T11:38:46Z'
authors:
- Turan G. Bali
- Amit Goyal
- Dashan Huang
- Fuwei Jiang
- Quan Wen
year: 2022
venue: Swiss Finance Institute Research Paper Series 20-110 (this version May 2022)
tags:
- machine-learning
- corporate-bonds
- return-predictability
- merton-model
- structural-models
sources: []
related:
- concepts/merton-model
- concepts/structural-models
- concepts/corporate-bonds
- concepts/random-forest
mind_map_priority: high
schema_version: 2
uuid: 6077fb73-773b-5d93-845f-a0a14918cd33
content_hash: sha256:19b624af9f59e7b130561f0494f2b6eab3dff38f2acc5d7872e92b34f53fe97c
---

<!-- AUTHORED REGION START -->
# Predicting Corporate Bond Returns: Merton Meets Machine Learning

**Authors:** Turan G. Bali (Georgetown), Amit Goyal (Lausanne and Swiss Finance Institute), Dashan Huang (Singapore Management), Fuwei Jiang (CUFE), Quan Wen (Georgetown)

**Version here:** Swiss Finance Institute Research Paper 20-110, this version May 2022

## Summary

Applies machine learning to corporate bond return prediction using both stock and bond characteristics, and asks whether imposing economic structure helps or hurts.

## The Claim That Distinguishes It

Two findings, and the second is the one that matters.

**Machine learning substantially improves out-of-sample performance** of stock and bond characteristics in predicting future bond returns. That much is now a familiar result.

**Imposing the Merton model's structure improves it further**, compared with the reduced-form approach that leaves the model unrestricted. So the gain does not come from letting a flexible learner find whatever it likes — it comes from constraining it with the theoretical link between equity and credit.

The paper's own summary of the point: expected bond and stock returns depend on each other, and making that dependence explicit — through both machine learning and the Merton model — beats ignoring it.

## Why It Sits Here

This is the equity-to-credit channel again, arrived at from the modelling side rather than the trading side. See [[concepts/merton-model|Merton Model]] and [[concepts/structural-models|Structural Models]].

It cuts against a common reading of the ML asset-pricing literature — that flexibility substitutes for theory. Here theory earns its place by improving the flexible model, not by competing with it.

## Caveats

It is a working paper, not a published article. The keywords list a hedge ratio, so the equity-credit link is operationalised as a specific hedging relationship rather than as a general prior; how sensitive results are to that choice is worth checking in the text.

## Open Questions

- How much of the improvement survives corporate bond transaction costs? See [[concepts/bond-liquidity|Bond Liquidity]].
- Does the structural gain hold in high yield, where Merton's assumptions strain most?

## See Also

[[concepts/merton-model|Merton Model]] · [[concepts/structural-models|Structural Models]] · [[concepts/random-forest|Random Forest]] · [[concepts/bond-liquidity|Bond Liquidity]] · [[sources/feng-2025-predicting-bond-returns|Feng et al. (2025)]] · [[sources/cao-2023-implied-vol-bond-returns|Cao et al. (2023)]]

**Not yet written:** `concepts/return-predictability`, `concepts/hedge-ratio`
<!-- AUTHORED REGION END -->

