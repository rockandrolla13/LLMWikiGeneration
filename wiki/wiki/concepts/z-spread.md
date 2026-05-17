---
title: "Z-Spread"
page_id: concepts/z-spread
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [fixed-income, credit-risk, bond-pricing, spreads]
sources: [sources/martin-2024-credit-curve]
related: [concepts/credit-spread-curve, concepts/survival-probability, concepts/nelson-siegel-model]
mind_map_priority: medium
---

# Z-Spread (Zero-Volatility Spread)

The Z-spread is the constant spread that, when added to each point on the risk-free spot rate curve, makes the present value of a bond's cash flows equal to its market price.

## Definition

For a bond with cash flows $C_i$ at times $t_i$ and market price $P$:

$$P = \sum_i C_i \cdot e^{-(r(t_i) + z) \cdot t_i}$$

where $r(t)$ is the risk-free spot rate and $z$ is the Z-spread.

## Interpretation

The Z-spread captures:
- **Credit risk premium**: Compensation for default risk
- **Liquidity premium**: Compensation for trading costs
- **Other factors**: Embedded options, tax effects, supply/demand

## Advantages

1. **Curve-aware**: Uses the full term structure, not just a single benchmark
2. **Comparable**: Allows comparison across bonds with different maturities
3. **Additive**: Can decompose into component spreads

## Limitations

- Assumes constant spread across all maturities (may not hold)
- Ignores optionality in callable/putable bonds (use OAS instead)
- Sensitive to the choice of risk-free curve

## Related Measures

| Measure | Description |
|---------|-------------|
| **I-spread** | Spread over swap curve at matching maturity |
| **G-spread** | Spread over government bond at matching maturity |
| **OAS** | Option-adjusted spread, removes optionality |
| **ASW** | Asset swap spread, derivative-based measure |

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/survival-probability|Survival Probability]]
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (Martin, 2024)]]
