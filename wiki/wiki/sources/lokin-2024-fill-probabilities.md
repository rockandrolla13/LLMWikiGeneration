---
title: Fill Probabilities in a Limit Order Book with State-Dependent Stochastic Order
  Flows
page_id: sources/lokin-2024-fill-probabilities
page_type: source
created: 2026-04-26 03:00:00+00:00
updated: '2026-06-20T01:03:51Z'
tags:
- limit-order-book
- fill-probability
- execution-probability
- queueing-theory
- laplace-transforms
- fx-spot
authors:
- Felix Lokin
- Fenghui Yu
year: 2024
related:
- concepts/limit-order-book
- concepts/fill-probability
- concepts/optimal-execution
- concepts/market-microstructure
schema_version: 2
uuid: 226c43a3-f529-5bdc-b60f-64f276746486
content_hash: sha256:b86a2bb7edb0ae6f4f37a07464140ce2ea5f053d668287bcfe6796bc922c99ac
---

<!-- AUTHORED REGION START -->
# Fill Probabilities in a Limit Order Book with State-Dependent Stochastic Order Flows

## Summary

This paper develops semi-analytical expressions for computing **fill probabilities** of limit orders at various price levels in a [[concepts/limit-order-book]]. The framework uses state-dependent stochastic order flows and models the order book dynamics as a series of queueing systems.

## Key Contributions

1. **Generic state-dependent model**: Order arrival and cancellation rates depend on stylized factors
2. **Semi-analytical formulas**: Using Laplace transforms and continued fractions for probability computation
3. **Multi-level fill probabilities**: Not just best quotes, but deeper levels in the book
4. **Empirical validation**: Extensive experiments with FX spot market data

## Model Framework

The limit order book is modeled as a continuous-time process:
$$Q(t) = (Q_1(t), Q_2(t), \ldots, Q_N(t))$$

where $|Q_i(t)|$ is the number of outstanding orders at price level $i$.

### State-Dependent Rates

- Limit order arrival rate: $\lambda_{Q_i}(X_i)$
- Market order arrival rate: $\mu_{Q_i}(X_i)$
- Cancellation rate: $\phi_{Q_i}(X_i)$

where $X_i$ is a vector of stylized factors (spread, order depth, imbalance, etc.)

## Probabilities Computed

The paper derives formulas for:
1. **Mid-price change probability**: Likelihood of price moving up vs. down
2. **Best quote fill probability**: Execution at bid/ask before opposite quote moves
3. **Deeper level fill probability**: Execution at levels beyond best quotes

## Methodological Approach

- Model order book dynamics as **birth-death processes**
- Use **Laplace transforms** for first-passage time analysis
- Employ **continued fractions** for numerical computation
- Connect to survival analysis concepts

## Example Models Covered

1. **Model I** (Cont et al. 2010): Rates as deterministic functions of price distance
2. **Model II** (Toke & Yoshida 2017): Parametric models with spread and queue size

## Numerical Experiments

Using FX spot market data:
- Model captures dynamics reasonably well
- Formulas show good accuracy in estimating fill probabilities
- Practical for algorithmic trading applications

## Related Concepts

- [[concepts/optimal-execution]] - Fill probabilities are crucial input
- [[concepts/market-microstructure]] - Underlying theory
- [[concepts/limit-order-book]] - Market structure

## Citation

Lokin, F., & Yu, F. (2024). Fill Probabilities in a Limit Order Book with State-Dependent Stochastic Order Flows.

<!-- AUTHORED REGION END -->
