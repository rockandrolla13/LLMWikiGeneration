---
title: The only admissible way of merging arbitrary e-values
page_id: sources/wang-2025-admissible-merging-evalues
page_type: source
source_path: markdown_output/wang-2025-admissible-merging-evalues.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Ruodu Wang
year: 2025
venue: Biometrika (2025)
tags:
- e-value
- merging
- admissibility
- arbitrary-dependence
- optimal-transport
sources: []
related:
- concepts/e-value
- concepts/p-value-merging
- entities/ruodu-wang
mind_map_priority: high
schema_version: 2
uuid: d54c4cd1-7868-5533-92f3-84dc5e21bc68
content_hash: sha256:2e8c222d53a7dd35d1b5def90bc13b4e4178039a947fa32d097d1b57c20680bc
---

<!-- AUTHORED REGION START -->
# The Only Admissible Way of Merging Arbitrary E-values

**Author:** [[entities/ruodu-wang|Ruodu Wang]]

**Year:** 2025 · **Venue:** Biometrika

## Summary

Closes the question left open by [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]]. That paper showed the arithmetic mean is the only admissible *symmetric* way of merging e-values under arbitrary dependence. This one drops symmetry: the only admissible way, full stop, is a **weighted** average of the inputs and the constant 1.

## The result

For weights $\boldsymbol\lambda$ in the $(K+1)$-simplex, define
\[
M_{\boldsymbol\lambda}(\mathbf{e})=\boldsymbol\lambda\cdot(\mathbf{e},1),
\]
the $\boldsymbol\lambda$-weighted average of the $K$ e-values together with the constant 1.

**Theorem 1.** Every e-merging function is dominated by some $M_{\boldsymbol\lambda}$; and a merging function is admissible if and only if it *is* some $M_{\boldsymbol\lambda}$.

The supporting machinery is worth noting because it is unusual for this literature: an optimal transport duality (the worst case over dependence structures with fixed marginals equals an infimum over separable dominating functions) plus a minimax interchange via Sion's theorem. A single-input lemma, settling the case $K=1$, is described as not previously in the literature.

## Why It Matters

The practical consequence is licence to stop looking. If your e-values are arbitrarily dependent, weighted averaging is not merely convenient, it is the only thing that can be admissible, so no cleverer combination rule is waiting to be found. The paper puts it as freeing us "of any doubts about whether there are better choices in particular contexts".

That is specific to arbitrary dependence. The paper lists four subclasses where $M_{\boldsymbol\lambda}$ remains admissible but is no longer the only admissible choice: fixed marginals, bounded second moments, identical e-variables, and exchangeable e-variables. Under independence or sequentiality, many other admissible methods exist — that is the regime of the product and the martingale constructions.

An explicit open problem is stated: whether a particular randomized-Markov merging function is admissible is unresolved.

## A note on how the result is stated elsewhere

Three statements in this cluster look alike and are not interchangeable:

- the arithmetic mean **essentially dominates** any symmetric e-merging function (Vovk & Wang, 2021, Proposition 3.1);
- arithmetic averaging is **essentially the only symmetric** merging method (the same result, restated);
- a weighted arithmetic average is **the only admissible** way of merging, without symmetry (this paper).

The first is essential domination; the third is admissibility without symmetry.

## See Also

[[concepts/e-value|E-value]] · [[concepts/p-value-merging|Merging P-values and E-values]]

Generalises [[sources/vovk-2020-evalues-calibration-combination|Vovk & Wang (2021)]]. Cites [[sources/wang-2021-fdr-control-evalues|e-BH]] as an application of weighted averaging, and [[sources/vovk-2019-confidence-discoveries-evalues|Vovk & Wang (2023)]] for discovery matrices. The independent and sequential regimes it excludes are the subject of [[sources/vovk-2024-merging-sequential-evalues|Merging sequential e-values via martingales]].
<!-- AUTHORED REGION END -->
