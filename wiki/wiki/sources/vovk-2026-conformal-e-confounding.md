---
title: Conformal e-prediction in the presence of confounding
page_id: sources/vovk-2026-conformal-e-confounding
page_type: source
source_path: markdown_output/vovk-2026-conformal-e-confounding.md
source_type: paper
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2026
venue: Working paper, arXiv:2603.11134 (13 March 2026)
tags:
- e-value
- conformal-prediction
- causal-inference
- confounding
- back-door
sources: []
related:
- concepts/e-value
- concepts/conformal-prediction
- concepts/causal-inference
- concepts/exchangeability
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: medium
schema_version: 2
uuid: de9de08a-5210-5902-bf69-94ce6dced771
content_hash: sha256:aabb99101d5932b5e836352339784862bf36fa569de547a47fba7fd9e4b14e45
---

<!-- AUTHORED REGION START -->
# Conformal E-prediction in the Presence of Confounding

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2026 · **Venue:** Working paper, arXiv:2603.11134

## Summary

What happens to $Y$ if we set $X:=x$, when a confounder $Z$ is observed and the data are purely observational? This note answers it with finite-sample validity, using [[concepts/e-value|e-values]] rather than p-values, and connects the answer directly to [[concepts/conformal-prediction|conformal prediction]].

## Construction

Let $p_y$ be the probability that $Y=y$ in the mutilated model — the causal graph with the arrow $Z\to X$ removed and $X$ set to $x$. A regularised plug-in estimate $F_y$ is formed from $N$ observations, with "+1" added to numerator and denominator. Lemma 1 bounds the expectation of $p_y/F_y$ by $|Z|$, the number of values the confounder takes. Corollary 2 converts that into an e-variable, and the prediction region is
\[
\Gamma^{\alpha}=\{\,y : \text{the e-value for } y < \alpha\,\},
\]
where $\alpha$ is typically a large number such as 10 or 100. Validity holds in the strong integral form, with Markov's inequality then giving an error probability of at most $1/\alpha$.

The exact form of the e-variable and of the region is equation (3) and Corollary 2 of the paper; the converter dropped both as images, so they are not restated here.

## Results

Validity is proved in two settings: the IID case (Lemma 1), and a "Y-oblivious" sequential case where the next treatment $X_{n+1}$ may depend on all past treatments and confounders but not on past outcomes (Lemma 3). Remark 1 extends the result to any back-door adjustment set.

## Relation to conformal prediction

This is Vovk's own framework, not a loose analogy. Appendix A shows the causal e-predictor is a combination of $|Z|$ conformal e-predictors, built from simple conformal e-prediction and its object-conditional variant. Validity needs only that the outcomes are IID conditional on the treatment. The price of the causal setting is explicit: Appendix A.3 shows the causal bound is weaker than plain conformal e-prediction by a factor of $|Z|$.

The paper positions itself closer to "randomness prediction" than to conformal prediction proper.

## Open Problems Stated

- The strong interpretation, where the past includes outcomes. The suggested route is conformal test martingales.
- Regression-valued outcomes.
- The admissible constants in the main bound.

## See Also

[[concepts/e-value|E-value]] · [[concepts/conformal-prediction|Conformal Prediction]] · [[concepts/causal-inference|Causal Inference]] · [[concepts/exchangeability|Exchangeability]]

[[sources/vovk-2026-ci-causal-sequential|Vovk & Wang (2026)]] is the direct successor: it handles the strong interpretation this note cannot, at the cost of much more conservative regions.

**Not yet written:** `concepts/back-door-criterion`, `concepts/conformal-test-martingale`.
<!-- AUTHORED REGION END -->
