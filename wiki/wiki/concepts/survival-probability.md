---
title: "Survival Probability"
page_id: concepts/survival-probability
page_type: concept
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
tags: [credit-risk, default-modelling, fixed-income, probability]
sources: [sources/martin-2024-credit-curve]
related: [concepts/credit-spread-curve, concepts/z-spread, concepts/longevity-risk]
mind_map_priority: medium
---

# Survival Probability

Survival probability is the likelihood that a bond issuer (or any obligor) will not default by a given time horizon.

## Definition

$Q(t)$ = Probability that the issuer survives (does not default) until time $t$

Key properties:
- $Q(0) = 1$ (starts alive)
- $Q(t)$ is monotonically decreasing
- $\lim_{t \to \infty} Q(t) = 0$ (eventually all issuers default or mature)

## Relationship to Credit Spreads

Under risk-neutral pricing with constant hazard rate $\lambda$ and recovery rate $R$:

$$Q(t) = e^{-\lambda t}$$

Credit spread approximation:
$$s \approx \lambda (1 - R) = -\frac{\ln Q(t)}{t}(1 - R)$$

## Calibration Methods

1. **From CDS spreads**: Market-implied default probabilities
2. **From bond spreads**: Back out implied survival curve
3. **From ratings**: Historical default rates by rating category
4. **Structural models**: Merton-style models using equity volatility

## Applications

- **Bond valuation**: Price risky cash flows as expected values
- **CVA calculation**: Credit valuation adjustment for derivatives
- **Portfolio credit risk**: Loss distribution estimation
- **Limit setting**: Credit exposure management

## Term Structure

The survival probability curve $Q(t)$ defines the term structure of credit risk:
- Flat: constant hazard rate
- Upward-curving: declining hazard rate (survival effect)
- Downward-curving: increasing hazard rate (deterioration)

## See Also

- [[concepts/credit-spread-curve|Credit Spread Curve]]
- [[concepts/z-spread|Z-Spread]]
- [[concepts/longevity-risk|Longevity Risk]]
- [[sources/martin-2024-credit-curve|The Credit Curve Spread I (Martin, 2024)]]
