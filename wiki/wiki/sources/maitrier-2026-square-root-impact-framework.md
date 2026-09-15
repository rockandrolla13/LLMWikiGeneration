---
authors:
- Guillaume Maitrier
- Jean-Philippe Bouchaud
content_hash: sha256:9138e29cec9eb1122594303e3d84645740c0edb5a9002e8fc24d0116c8a0ad7c
created: 2026-08-13 00:00:00+00:00
page_id: sources/maitrier-2026-square-root-impact-framework
page_type: source
related:
- concepts/square-root-law
- concepts/metaorder
- concepts/propagator-model
- concepts/price-impact
- concepts/order-flow-imbalance
- concepts/order-flow
- entities/jean-philippe-bouchaud
- entities/guillaume-maitrier
- sources/maitrier-2025-artificial-market-generator
revision_id: 1
schema_version: 2
source_hash: sha256:c9e08fbb0f43940409c7226db03cd1a3201747bfea0682e875ecba3a5eaae026
source_path: markdown_output/2506.07711.md
tags:
- square-root-law
- price-impact
- metaorder
- propagator-model
- market-microstructure
- volatility
- econophysics
- order-flow-imbalance
- diffusivity-puzzle
title: 'The Subtle Interplay between Square-root Impact, Order Imbalance & Volatility:
  A Unifying Framework'
updated: '2026-08-13T00:00:00Z'
uuid: faa98c0e-6602-55e6-9a8c-78ee95cf4911
year: 2025
---

<!-- AUTHORED REGION START -->
# The Subtle Interplay between Square-root Impact, Order Imbalance & Volatility: A Unifying Framework

## Summary

Three well-established facts about markets appear to contradict each other. Impact of a large parent order grows as the **square root** of its volume and then decays. Order signs have **long memory**. Prices are **diffusive**, with volatility proportional to the square-root law's amplitude. This paper builds a framework in which all three hold simultaneously, and finds that the ingredient making it work is correlation *between* [[concepts/metaorder|metaorders]] — not just within them.

The conclusion is a claim about where volatility comes from: it is generated mechanically by trading, not by revelation of fundamental value.

## The Puzzle

The square-root law states that the average impact of a metaorder of volume $Q$ is

$$I(Q) = Y \sigma \sqrt{Q / V_D}$$

with $Y$ an $O(1)$ constant. This is not the trivial random-walk statement it resembles: $I(Q)$ is an *average* price change rather than a standard deviation, it depends on $Q$ alone and not on execution time $T$, and impact *decays* after execution ends. All three features are at odds with the Kyle model, which predicts linear and permanent impact from information revelation.

The paper takes the square-root law as given empirical input — explicitly declining to derive it — and attacks two downstream questions: can volatility be explained entirely by the impact of possibly uninformed metaorders, and can square-root impact for individual metaorders coexist with a locally *linear* relation between aggregate returns and [[concepts/order-flow-imbalance|order flow imbalance]]?

## The Framework

Metaorders arrive at rate $\nu$ with random sign $\varepsilon$, duration $s$ drawn from a power law $\Psi(s) \propto s^{-1-\mu}$, and child orders of volume $q$ executing at rate $\phi$. This inherits the Lillo–Mike–Farmer mechanism, under which the power-law size distribution generates the long memory of order signs with $\gamma = \mu - 1$.

Two extensions do the real work:

**Metaorder signs are correlated across metaorders**, $\mathbb{E}[\varepsilon(t)\varepsilon(t+\tau)] \sim \tau^{-\gamma_\times}$.

**The exponents depend on child order size.** Empirically, large child orders are less persistent and their impact decays more slowly, so $\mu_q$ and $\beta_q$ are made linear in $\log q$.

To bridge sign imbalance and volume imbalance, they define a **generalized imbalance** interpolating between them:

$$I^a_T = \sum_{t \in [0,T]} \varepsilon_t (q_t)^a$$

with $a = 0$ weighting every child order equally and larger $a$ overweighting big ones.

## Three Results

**1. Diffusion needs cross-metaorder correlation.** When impact is transient, the heavy tail of metaorder durations *alone* produces sub-diffusion, not diffusion — impact decay wins and prices mean-revert. Diffusion is restored by long-range correlation between the signs of distinct metaorders, giving a price-variance contribution scaling as $T^{2-\gamma_\times-2\beta}$ and hence diffusion when $\gamma_\times \simeq 1 - 2\beta$. This is the paper's central mechanism and it is falsifiable.

**2. Volume heterogeneity produces $a$-dependent scaling.** The moments of $I^a_T$ show an $a$-dependent crossover, confirmed in data. For sign imbalance ($a=0$) the rescaled distribution collapses onto a master curve with $\chi = 0.72$ on EUROSTOXX, near the theoretical $1/\mu$ with $\mu = 3/2$; volume imbalance shows fat tails a Gaussian of the same variance does not.

**3. The reconciliation, with two sharp predictions.** The scaling exponent of $\mathbb{E}[\Delta_T \cdot I^a_T]$ against $T$ is predicted to be **non-monotonic in $a$**, and the correlation coefficient $R_a(T)$ is predicted to be **hump-shaped in $a$** — there is an optimal weighting of large trades. Both are observed. The hump-shape match uses parameters fixed from earlier fits, not refitted.

The decay exponent that emerges is $\beta = 1/2$, differing from both the classic propagator model and the LLOB model, which is why a *generalized* propagator is needed.

## Data

Four assets chosen to span tick sizes and asset classes, with trade-by-trade prices and signed volumes: two LSE stocks — LLOY (small tick, spread-to-tick $\approx 3$) and TSCO (medium tick, $\approx 1.5$) — over 2012–2015; and two futures — SPMINI ($\approx 1.1$, 2022) and EUROSTOXX (large tick, $\approx 1.02$, 2016–2018). Stocks and futures are found to differ markedly on these metrics, which the authors suggest could itself characterise price formation across market types.

## Why It Matters Beyond Microstructure

The paper derives what an additional exogenous "fundamental" volatility component would do to the covariances and correlations, and finds those scalings are **not** supported by the observed $a$-dependence. That is the argument against the efficient-market reading: if a large share of volatility came from fundamental value changes, the correlation structure between returns and generalized imbalance should look different than it does.

The model also predicts impact amplitude proportional to volatility as a consequence rather than an assumption.

An honest reopening: the authors note that if correlations *between* metaorders are essential, the order-splitting-versus-herding debate — widely considered settled in favour of splitting — is less clear-cut than assumed. The correlation could come from shared signals, from market makers unwinding inventory, or from traders anticipating each other.

## Limitations

- The square-root law is taken as input, not derived. The authors state plainly it still awaits a fully convincing explanation.
- Analytical treatment requires approximations the authors describe as "somewhat strong and uncontrolled"; these are checked by simulation in [[sources/maitrier-2025-artificial-market-generator|the companion paper]].
- Results are computed in trade time; translating to real time is non-trivial because activity rate is intermittent and has a U-shaped intraday pattern. Activity fluctuations and intraday seasonality are neglected throughout.
- Four assets.
- A note added after submission flags Muhle-Karbe et al., *A unified theory of order flow, market impact, and volatility* (January 2026), whose relation to this work is unexamined.

## Related

- [[sources/maitrier-2025-artificial-market-generator]] — the simulation companion that validates these approximations
- [[sources/cont-2023-cross-impact-ofi]] — the linear-OFI tradition this paper reconciles the square-root law against
- [[concepts/square-root-law]], [[concepts/metaorder]], [[concepts/propagator-model]], [[concepts/price-impact]]
- [[entities/guillaume-maitrier]], [[entities/jean-philippe-bouchaud]]

## Citation

Maitrier, G., & Bouchaud, J.-P. (2025). The Subtle Interplay between Square-root Impact, Order Imbalance & Volatility: A Unifying Framework. arXiv:2506.07711; *Quantitative Finance*. Submitted June 2025; the arXiv version consulted here is dated March 2026.
<!-- AUTHORED REGION END -->