---
title: Large-Dimensional Factor Modeling Based on High-Frequency Observations
page_id: sources/pelger-2019-large-dimensional-hf-factor-model
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-08-06 00:00:00+00:00
updated: '2026-08-06T20:51:36Z'
authors:
- Markus Pelger
year: 2019
venue: Journal of Econometrics
tags:
- high-frequency-data
- factor-models
- pca
- jumps
- systematic-risk
sources: []
related:
- concepts/approximate-factor-models
- concepts/principal-components-analysis
- concepts/high-frequency-data
- concepts/factor-models
- concepts/jump-clustering
- concepts/realized-covariance
mind_map_priority: high
schema_version: 2
uuid: 6e04d13b-d14b-560c-8558-881e92d4177b
content_hash: sha256:623308259565cc0d4490149a98b970d284b218d2a3832c9accf45624e9a8e609
---

<!-- AUTHORED REGION START -->
# Large-Dimensional Factor Modeling Based on High-Frequency Observations

**Author:** Markus Pelger

**Year:** 2019 · **Venue:** Journal of Econometrics 208, 23–42

**Institution:** Department of Management Science & Engineering, Stanford University

## Summary

Inferential theory for [[concepts/approximate-factor-models|approximate factor models]] estimated from intraday returns over a *short* fixed horizon — a week or a month rather than decades. The distinguishing feature is that the method separates factors driving continuous price movements from factors driving jumps.

## What It Does

Loadings and factors come from [[concepts/principal-components-analysis|PCA]] on the quadratic covariation matrix, using rescaled increments. This is essentially the Bai (2003) principal-component estimator, but the paper is explicit that the assumptions and proofs cannot be mapped from the long-horizon discrete-time model except in special cases. The processes are Itô semimartingales with jumps; idiosyncratic errors may be weakly correlated serially and cross-sectionally. Asymptotics are joint in the cross-section and the number of high-frequency observations. Loadings and factors are consistent and asymptotically mixed-normal.

Continuous and jump components are split by the threshold estimator of Lee and Mykland (2008) and Mancini (2009), so the same PCA machinery yields separate continuous and jump factor sets.

Two further tools. A diagnostic for the number of factors based on a **perturbed** eigenvalue ratio — perturbing before taking the ratio avoids the random matrix theory assumptions the paper calls unrealistic here, and detects factors that are weak in finite samples. And a total generalized correlation statistic, with asymptotic distribution, for testing whether statistical factors are close to observable economic ones.

## Findings

5-minute S&P 500 prices, 2003–2012, roughly 250 trading days a year, 77 increments per day, 500–600 firms per year. For 2007–2012 four continuous factors are estimated, well approximated by market, oil, finance and electricity portfolios; from 2003 to 2006 the finance factor disappears. The four account for about 40–47% of total correlation in 2008–2011 but only 20–31% in other years.

Jump structure differs. In most years the estimator indicates one jump factor, essentially an equally weighted market jump factor, whose first generalized correlation with the economic jump factors is 1.00. At threshold `a = 3` under 1% of increments are jumps, explaining 12–21% of quadratic variation.

## Caveats

The author states plainly that the continuous factor results are robust to the jump threshold but the jump factor results are not, and should be read with caution.

## Open Questions

- Is the disappearing finance factor a structural change or an artefact of the pre-crisis sample?
- What drives the time variation in the number of continuous factors?

## See Also

[[concepts/approximate-factor-models|Approximate Factor Models]] · [[concepts/principal-components-analysis|Principal Components Analysis]] · [[concepts/high-frequency-data|High-Frequency Data]] · [[concepts/jump-clustering|Jump Clustering]] · [[sources/pelger-2015-understanding-systematic-risk|Pelger (2015)]] · [[sources/aitsahalia-2017-pca-hf-factor-model|Aït-Sahalia & Xiu (2017)]]

**Not yet written:** `generalized-correlation`, `eigenvalue-ratio-estimator`, `jump-factors`, `ito-semimartingale`, `threshold-jump-estimator`.

<!-- AUTHORED REGION END -->

