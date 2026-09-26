---
title: 'E-values: calibration, combination, and applications'
page_id: sources/vovk-2020-evalues-calibration-combination
page_type: source
source_path: markdown_output/vovk-2020-evalues-calibration-combination.md
source_type: journal-article
revision_id: 1
created: 2026-09-16 00:00:00+00:00
updated: '2026-09-16T00:00:00Z'
authors:
- Vladimir Vovk
- Ruodu Wang
year: 2020
venue: Annals of Statistics 49(3), 1736-1754 (2021)
tags:
- e-value
- calibration
- merging
- multiple-testing
- arbitrary-dependence
sources: []
related:
- concepts/e-value
- concepts/e-process
- concepts/p-value-merging
- concepts/multiple-testing
- entities/vladimir-vovk
- entities/ruodu-wang
mind_map_priority: high
schema_version: 2
uuid: 7abc81b7-0c35-5b84-b34c-32e0ba0b10ad
content_hash: sha256:9920ad9a0dc4b6c33af0409e8f79e53b446b796f85cb0973e7d4c1fed4b053c3
---

<!-- AUTHORED REGION START -->
# E-values: Calibration, Combination, and Applications

**Authors:** [[entities/vladimir-vovk|Vladimir Vovk]], [[entities/ruodu-wang|Ruodu Wang]]

**Year:** preprint 2020 · **Venue:** Annals of Statistics 49(3), 1736–1754 (2021)

## Summary

The foundational paper of this cluster. It defines the e-value, shows how to convert between p-values and e-values, and settles how e-values should be combined. The headline practical fact: **e-values can always be averaged**, with no assumption whatsoever about dependence and no correction constant. Nothing comparable is true for p-values.

## Definitions

An **e-variable** is an extended random variable $E:\Omega\to[0,\infty]$ with $\mathbb{E}[E]\le 1$; an **e-value** is a value it takes. The value $\infty$ is allowed and licenses rejection outright. A **p-variable** satisfies $\mathbb{P}(P\le\alpha)\le\alpha$.

The interpretation is a bet against the null at fair odds. An e-value of 20 means a stake of 1 turned into 20 in a game that is fair under the null, which is evidence against it.

## Calibration

A decreasing $f:[0,1]\to[0,\infty]$ is a **calibrator**, turning p-values into e-values, if and only if $\int_0^1 f\le 1$; it is admissible if and only if $f$ is upper semicontinuous, $f(0)=\infty$ and $\int_0^1 f=1$. Two named examples: the family $f_\kappa(p)=\kappa p^{\kappa-1}$ for $\kappa\in(0,1)$, and
\[
F(p)=\frac{1-p+p\log p}{p(-\log p)^2},
\]
attributed to Ramdas, which behaves like $p^{-1}(-\log p)^{-2}$ for small $p$.

Going the other way is essentially unique: $f(t)=\min(1,1/t)$ is the **only** admissible e-to-p calibrator. Round trips are lossy, which is the price of moving between the two currencies; [[sources/vovk-2019-confidence-discoveries-evalues|Vovk & Wang (2023)]] quantifies the loss.

## Merging

Under **arbitrary dependence**, the arithmetic mean essentially dominates every symmetric e-merging function (Proposition 3.1), and Theorem 3.2 sharpens this: any symmetric e-merging function is dominated by $\lambda+(1-\lambda)M_K$, and such a function is admissible exactly when it takes that form with $\lambda=F(\mathbf{0})$.

Under **independence or sequentiality** — where $\mathbb{E}[E_k\mid E_1,\dots,E_{k-1}]\le 1$ — the product $E_1\cdots E_K$ becomes available, along with U-statistics of order $n$ and their convex mixtures. The product weakly dominates every independent-merging function.

Two algorithms give family-wise valid adjusted e-values: Algorithm 1 in $O(K^2)$ for arbitrary dependence via the arithmetic mean, and Algorithm 2 in $O(K)$ for the sequential case via the product.

## Numbers

The paper adopts Jeffreys's scale for reading an e-value: below 1 supports the null; 1 to $\sqrt{10}\approx3.16$ is "not worth more than a bare mention"; up to 10 substantial; up to $10^{3/2}\approx31.6$ strong; up to 100 very strong; above 100 decisive.

In a normal-mean experiment with 10,000 observations and a true shift of $-0.1$, the product e-value starts below Fisher's method but overtakes it after roughly 2,000 observations. In a multiple-testing example with 20 hypotheses of which 10 are false, the Simes and Bonferroni closures reach about $2\times10^3$ while averaging-based methods reach about $10^2$; with 200 hypotheses and 100 false, the figures are about $2\times10^2$ and $10^1$.

## Why It Matters

Two properties make e-values worth the trouble. Averaging is always valid, so combining evidence across arbitrarily dependent tests needs no dependence model. And because the definition is an expectation rather than a tail probability, e-values compose multiplicatively over time, which is what makes sequential testing and [[concepts/anytime-valid-inference|optional stopping]] work.

## See Also

[[concepts/e-value|E-value]] · [[concepts/e-process|E-process]] · [[concepts/p-value-merging|Merging P-values and E-values]] · [[concepts/multiple-testing|Multiple Testing]]

[[sources/wang-2025-admissible-merging-evalues|Wang (2025)]] removes the symmetry assumption from Theorem 3.2. [[sources/wang-2021-fdr-control-evalues|Wang & Ramdas (2022)]] builds FDR control on this framework. [[sources/vovk-2019-confidence-discoveries-evalues|Vovk & Wang (2023)]] uses the arithmetic-mean result for discovery matrices.
<!-- AUTHORED REGION END -->
