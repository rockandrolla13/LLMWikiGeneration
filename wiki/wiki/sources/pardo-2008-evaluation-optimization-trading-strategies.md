---
authors:
- Robert Pardo
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/pardo-2008-evaluation-optimization-trading-strategies
page_type: source
publication_date: '2008'
publication_venue: John Wiley & Sons (Wiley Trading Series), 2nd edition
related:
- concepts/historical-simulation-backtesting
- concepts/optimization-search-methods
- concepts/strategy-robustness
- concepts/trading-strategy-optimization
- concepts/trading-strategy-overfitting
- concepts/walk-forward-analysis
- entities/john-wiley-sons
- entities/robert-pardo
revision_hash: sha256:7b6b59788f1b1e816aa231c79066d79b55880cbcf4e75d04bc2e68f5141c58f3
revision_id: 1
source_hash: sha256:e2deed2d2c8c38f32a996a4855d8c040bb0f2e2657d3016e44a4e3582c699b03
source_path: raw/creditmacro/Evaluation and Optimization of Trading Strategies (Robert
  Pardo) (z-library.sk, 1lib.sk, z-lib.sk).md
source_type: book
sources: []
tags:
- algorithmic-trading
- backtesting
- walk-forward-analysis
- optimization
- overfitting
- trading-systems
title: The Evaluation and Optimization of Trading Strategies
updated: '2026-06-09T12:00:00Z'
updated_by: op_dac7763811d3
---

# The Evaluation and Optimization of Trading Strategies

**Authors:** Robert Pardo · **Year:** 2008 · **Venue:** John Wiley & Sons (Wiley Trading Series), 2nd edition · **Type:** book

## Summary

Robert Pardo's practitioner methodology for building, testing, optimizing, and validating systematic trading strategies before risking capital. The central thesis is that a properly developed strategy is verifiable, quantifiable, objective, consistent, and extensible, and that historical simulation plus disciplined optimization produces a realistic performance profile. The signature contribution is walk-forward analysis: repeatedly optimizing on an in-sample window and testing on the subsequent out-of-sample window, then rolling forward - presented as the cure for overfitting. Much of the book makes simulation realistic (slippage, commissions, contract construction) and catalogs overfitting causes (overparameterization, overscanning, insufficient degrees of freedom, small samples).

## Key Claims

1. Walk-forward analysis is the primary defense against overfitting and the most reliable estimator of real-time robustness, risk, and return.
2. A strategy must be specified in definitive, testable rules and validated through a repeatable 8-step development process.
3. Realistic historical simulation requires explicit modeling of slippage, commissions, limit moves, and correct futures-contract construction.
4. Overfitting arises chiefly from overparameterization, overscanning, too few degrees of freedom, and small trade samples.
5. Adequate test-window size and a sufficient number of trades are statistical prerequisites for trustworthy results.
6. Strategy performance must be judged using risk-adjusted metrics (maximum drawdown, reward-to-risk, model efficiency), not raw net profit.

## Questions Raised

- How should walk-forward window sizes be chosen for a given market and trading frequency?
- What constitutes a statistically significant and robustly shaped optimization profile rather than a fragile peak?
- How do shifting market regimes and finite strategy life cycles limit forward validity?

## Concepts

- [[concepts/walk-forward-analysis|Walk-Forward Analysis]]
- [[concepts/trading-strategy-overfitting|Overfitting of Trading Strategies]]
- [[concepts/trading-strategy-optimization|Strategy Optimization]]
- [[concepts/historical-simulation-backtesting|Historical Simulation (Backtesting)]]
- [[concepts/strategy-robustness|Robustness and Walk-Forward Efficiency]]
- [[concepts/optimization-search-methods|Search and Optimization Methods]]

## Entities

- [[entities/robert-pardo|Robert Pardo]]
- [[entities/john-wiley-sons|John Wiley & Sons]]

## Source

- **Path:** `raw/creditmacro/Evaluation and Optimization of Trading Strategies (Robert Pardo) (z-library.sk, 1lib.sk, z-lib.sk).md`
- **Type:** book
- **Hash:** `sha256:e2deed2d2c8c38f32...`