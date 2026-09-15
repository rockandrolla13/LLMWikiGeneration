---
authors:
- Yuhan Su
- Zeyu Sun
- Jiarong Li
- Xianghui Yuan
content_hash: sha256:1f1f68699c61e03c7389ea4c571fe810dbc4afadf4e881fdcf3f30df5202f70d
created: 2026-08-13 00:00:00+00:00
page_id: sources/su-2021-generalized-ofi
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/price-impact
- concepts/limit-order-book
- concepts/order-imbalance
- sources/cont-2023-cross-impact-ofi
- sources/hu-2025-ofi-csi300-ou
revision_id: 1
schema_version: 2
source_hash: sha256:07cd3d391c2a8007d01d39077b31a1e714191ca5bf2a87b13ec201ab137c72c2
source_path: markdown_output/2112.02947.md
tags:
- order-flow-imbalance
- price-impact
- limit-order-book
- chinese-markets
- csi-500
- market-microstructure
title: The Price Impact of Generalized Order Flow Imbalance
updated: '2026-08-13T00:00:00Z'
uuid: 5068bac4-e668-52e8-a42e-3fbb2142d56a
year: 2021
---

<!-- AUTHORED REGION START -->
# The Price Impact of Generalized Order Flow Imbalance

## Summary

Points out an assumption buried in the standard [[concepts/order-flow-imbalance|OFI]] definition — that the best quote moves by at most one tick between observations — and shows it fails badly on Chinese snapshot data, where the exchange publishes the book only every three seconds. Relaxing it produces **Generalized OFI (GOFI)**, which more than doubles explained variance of mid-price changes on CSI 500 constituents.

## The Problem with Standard OFI

The classical OFI construction counts changes at the *position* of the best quote: the best bid improving, holding, or receding, each contributing a signed quantity. That accounting is exact only if the best price moves by a single tick per observation interval.

Chinese exchanges disseminate limit order book snapshots at a three-second frequency. Over three seconds the best quote can traverse several price levels — a batch of buy orders exhausts the level, the touch moves, another batch arrives, it moves again. Standard OFI records only the endpoints and discards the levels crossed in between.

## The Construction

GOFI keys on the **value** of the best execution price rather than its position, summing order quantities across every level the best quote traverses within the interval. The number of levels crossed is determined per observation, so a multi-tick move contributes all of the depth it passed through rather than a single truncated increment.

Two variants of each indicator, following the stationarisation of Wang et al. (2021):

- **OFI / GOFI** — quantities used directly.
- **log-OFI / log-GOFI** — logarithm of quantities, which damps the heavy variation in level sizes that the fixed-depth assumption of the original model does not accommodate.

## Data and Results

Ten CSI 500 constituent stocks, three-second snapshot data, linear regression of mid-price change on each indicator at three horizons. Average coefficients of determination across the ten stocks (percentage points, in-sample / out-of-sample):

| Horizon | OFI | log-OFI | GOFI | log-GOFI |
|---|---|---|---|---|
| 30 seconds | 38.38 / 32.89 | 45.73 / 40.35 | 75.96 / 76.37 | **83.58 / 83.57** |
| 1 minute | 44.45 / 38.13 | 51.88 / 46.27 | 77.63 / 77.85 | **85.46 / 85.37** |
| 5 minutes | 49.64 / 42.57 | 56.76 / 51.65 | 77.04 / 77.36 | **85.76 / 86.01** |

Three things stand out.

**The generalisation matters far more than the stationarisation.** Going OFI → log-OFI buys roughly 7 points; going OFI → GOFI buys roughly 38. The two are close to additive, and log-GOFI is best everywhere.

**log-GOFI is stable across time scales.** Its out-of-sample $R^2$ moves from 83.57 to 86.01 across a tenfold change in horizon, whereas plain OFI moves from 32.89 to 42.57. The authors present this stability as the main practical claim.

**The gap between in-sample and out-of-sample essentially vanishes for the generalized indicators** — 75.96/76.37 and 83.58/83.57 at 30 seconds — where standard OFI loses 5–7 points out of sample.

## Reading This Carefully

The improvement is large enough to warrant caution about what is being measured. GOFI aggregates resting depth across traversed levels rather than incremental flow at a fixed level, so it is closer to a *state* variable of the book than to a *flow* variable. The paper does not discuss whether this narrows the gap to the mid-price change mechanically. Anyone building on it should check that separately.

Other caveats:

- Ten stocks, selected "for ease of presentation" from the CSI 500; no universe-wide result.
- The sample period is not stated in the paper.
- Section 4 is headed "Conclusion" but is empty in the arXiv version — the paper stops at the tables.
- The out-of-sample protocol (split, window, chronology) is not described.

## Related

- [[sources/cont-2023-cross-impact-ofi]] — a different generalisation of the same object, by depth rather than by tick-crossing
- [[sources/hu-2025-ofi-csi300-ou]] — also Chinese microstructure, also 500 ms/3 s snapshot data rather than event data
- [[sources/xu-2020-mlofi]] — multi-level OFI, cited here as the prior extension
- [[concepts/order-flow-imbalance]], [[concepts/price-impact]]

## Citation

Su, Y., Sun, Z., Li, J., & Yuan, X. (2021). The Price Impact of Generalized Order Flow Imbalance. arXiv:2112.02947. School of Economics and Finance / School of Software Engineering, Xi'an Jiaotong University.
<!-- AUTHORED REGION END -->