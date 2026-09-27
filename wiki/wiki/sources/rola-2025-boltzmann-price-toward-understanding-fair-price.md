---
authors:
- Przemysław Rola
content_hash: sha256:06f278d403fdbd4e514f49d456acc8fa2f6d1fed2051e6894fdbdc58dff1ff76
created: 2026-09-27 01:47:00+00:00
page_id: sources/rola-2025-boltzmann-price-toward-understanding-fair-price
page_type: source
related:
- concepts/limit-order-book
- concepts/market-microstructure
- concepts/bid-ask-spread
- concepts/order-imbalance
- concepts/price-impact
- concepts/stylized-facts
- concepts/metaorder
- concepts/micro-price
- concepts/kyles-lambda
revision_id: 1
schema_version: 2
source_hash: sha256:93e3f3733f5420098e606ae84b7d842b01f4d4e55a6f9e352169a989006d9ee8
source_path: markdown_output/rola-2025-boltzmann-price-toward-understanding-fair-price.md
source_type: paper
tags:
- market-microstructure
- fair-price
- maximum-entropy
- limit-order-book
- volume-imbalance
- heavy-tails
- market-impact
- micro-price
- clock-calendar
- asset-equity
- harvest-relevant
title: 'Boltzmann Price: Toward Understanding the Fair Price in High-Frequency Markets'
updated: '2026-09-27T01:47:00Z'
uuid: 8289c860-d835-5b8f-bf1a-f89d94c41801
year: 2025
---

<!-- AUTHORED REGION START -->
# Boltzmann Price: Toward Understanding the Fair Price in High-Frequency Markets

## Summary

The paper asks how to pin down an unobservable 'fair' or fundamental reference price inside a limit order book, given that the two usual candidates fall short: the mid-price ignores volume imbalance and moves slowly, while the weighted mid-price reacts to every top-of-book update, is noisy, and has no theoretical justification as a fair-price estimator. Building on the idea that liquidity providers implicitly agree on a hidden fundamental price, the author sets out to derive a reference price from first principles rather than propose another ad hoc formula.

The approach treats the best bid and best ask as a two-state system and applies Jaynes' Maximum Entropy Principle: entropy is maximized subject to a constraint tying the expected state to the observed bid/ask volume imbalance, which yields a Boltzmann (softmax-style) distribution over the two states controlled by a single parameter beta. The expected price under this distribution is defined as the 'Boltzmann price'; a Taylor expansion shows it reduces to, or closely tracks, the mid-price and weighted mid-price under particular parameter and spread regimes, and motivates a simple 'equilibrium price' equal to their average. The same bid/ask state probabilities are then reused to build a discrete-time biased random walk for the fundamental price whose drift and volatility both depend on volume imbalance, and this is taken to a continuous-time stochastic differential equation limit. The model is checked in two ways: Monte Carlo simulations that vary the spread and imbalance distributions and compare resulting price-change kurtosis to the (driftless) Bachelier model, and fits to one month of minute-bar quote data for two US stocks with different spread behaviour.

The main finding is that letting drift and volatility depend on volume imbalance is enough, on its own, to reproduce fatter tails and higher kurtosis than a constant-volatility model, and that a fitted version of the model can match the mean, standard deviation and kurtosis of real minute-bar price changes reasonably well for both a varying-spread and a constant-spread stock. The author also revisits the standard market-impact story that crossing the spread costs about half the spread, and argues, using the Boltzmann price's sensitivity to imbalance, that the true cost of clearing one side of the book is somewhat less than half the spread, and that the weighted mid-price likely overstates it. What is new relative to prior fair-price proposals (mid-price, weighted mid-price, Stoikov's micro-price) is the derivation route itself: instead of proposing a formula and checking its properties afterward, the paper derives a whole one-parameter family of prices from an entropy argument, recovers the existing candidates as special or limiting cases, and reuses the same state probabilities to get both a price-dynamics model and a market-impact story.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

The theoretical price process is built as a discrete-time biased random walk whose up/down move probability each step is set by the current bid/ask volume imbalance, then taken to a continuous-time stochastic differential equation limit as the step size shrinks; no fixed prediction horizon is defined beyond the next model time step. For the historical validation, top-of-book quotes for individual stocks are aggregated into fixed one-minute wall-clock bins (using the last quote in each bin) over trading hours 9:30 to 16:00, with the first and last four minutes of each day excluded to reduce open/close effects.

## Data

- **Asset class:** Equities
- **Instruments:** Two US-listed common stocks used for the main historical fit: General Electric (GE, NYSE, varying spread) and Lucid Group (LCID, NASDAQ, effectively constant spread); the appendix additionally uses Bank of America (BAC) and Chevron (CVX) quote data for a separate micro-price comparison.
- **Venue:** NYSE (GE) and NASDAQ (LCID); quote data sourced from Refinitiv Eikon.
- **Period:** One month of trading in May 2025 (21 trading days, approximately 8,000 minute-level observations per stock); the BAC/CVX micro-price comparison in the appendix uses a separate one-month sample of quotes timestamped to the nearest second.
- **Granularity:** Top-of-book quotes aggregated into 1-minute bins using the last available quote in each bin, trading hours 9:30-16:00, first/last four minutes of each day excluded, and the first bin of each day (9:35) dropped to avoid overnight price changes.

## Features and Measures

- **Bid/ask volume imbalance (q, theta).** The best-bid size as a fraction of the combined best-bid and best-ask size (q), or its centered version theta = q - 1/2, used as the single input driving the model's state probabilities and price dynamics.
- **Boltzmann price.** The expected value of the bid/ask price pair under a two-state Boltzmann (softmax) distribution obtained by maximizing Shannon entropy subject to a volume-imbalance constraint, controlled by an inverse-temperature parameter beta.
- **Equilibrium / quasi-equilibrium price.** A first- and second-order Taylor approximation of the Boltzmann price around a balanced order book, shown to be closely approximated by the simple average of the mid-price and the weighted mid-price.
- **Imbalance-driven price dynamics.** A discrete-time biased random walk, and its continuous-time SDE limit, in which both the drift and the volatility of the fundamental price are functions of the bid/ask volume imbalance and the spread, rather than the fixed constants used in the Bachelier or Geometric Brownian Motion models.

## Method

The top-of-book bid and ask are modeled as a two-state system, and the Maximum Entropy Principle is applied by maximizing Shannon entropy subject to the constraint that the expected state value equals the observed volume imbalance; solving the resulting Lagrange-multiplier problem gives a Boltzmann (softmax) distribution over the two states with a single free parameter beta. The Boltzmann price is defined as the expectation of the bid/ask price pair under this distribution, and a Taylor expansion around a balanced book is used to connect it algebraically to the mid-price and weighted mid-price and to define an 'equilibrium price' as their average. The same state probabilities then define a discrete-time biased random walk for the fundamental price with imbalance-dependent increments, whose continuous-time limit is a stochastic differential equation in which drift and volatility both scale with the current imbalance and, for volatility, with half the spread.

The model is evaluated by Monte Carlo simulation, drawing the spread from a Gamma distribution and the imbalance from Beta distributions of varying shape, and comparing simulated price-change kurtosis, mean and standard deviation (over batches of 1,000 simulation runs) against the driftless Bachelier model; and by fitting the model to one month of minute-bar historical quote data for two stocks, choosing beta and a volatility-scaling constant eta so that sampled price changes match the historical mean, standard deviation and kurtosis. A separate section applies the same imbalance-sensitivity result to a simplified, Almgren-Chriss-style temporary market-impact setting to argue about how much of the half-spread transaction cost is actually attributable to the resulting change in the fundamental price itself.

## Results

- In a simulation with spread drawn from Γ(1,1) and imbalance from a symmetric Beta(4.5,4.5) with β = 1, price changes from the proposed model had a mean kurtosis of 7.29 (min 3.18, max 41.8) across 1000 simulation runs, versus near-zero kurtosis for the driftless Bachelier model.
- With a constant spread and a U-shaped Beta(0.5,0.5) imbalance and β = 5, a representative simulation produced a kurtosis of 4.67 for the proposed dynamics versus about 0.16 for the Bachelier model, while average simulated standard deviations of price changes were close (0.0028 Bachelier vs 0.0029 proposed).
- Across imbalance distributions Beta(0.5,0.5), Beta(2,2) and Beta(8,2) with β at 5 or 7.5, mean simulated kurtosis ranged from 2.5 to 8.75, indicating that both skewed and U-shaped imbalance distributions raise kurtosis.
- On one month of May 2025 minute-bar data for General Electric (21 trading days, about 8,000 observations), a fitted version of the model (β = 1) produced sampled price changes with a kurtosis of 5.17 versus 4.15 for the historical mid-price changes.
- For Lucid Group (constant 0.01 spread), computed kurtosis was 6.99 for mid-price changes, about 7.54 for Boltzmann price changes at β = 0.5, 8.08 at β = 1, and 9.1 for weighted mid-price changes; a fitted simulation at β = 17 gave sampled-data kurtosis of 6.74 (6.84 after rounding to two decimals) against the historical 6.99.
- In a market-impact example, clearing one side of a balanced order book (θ moving to 1/2) moved the Boltzmann price by about 0.462 times half the spread (tanh(0.5) ≈ 0.462) for β = 1, i.e. somewhat less than the full half-spread move implied by using the weighted mid-price.

## Limitations

- The price-dynamics derivation mostly assumes a constant spread; the authors state that modeling the effect of a time-varying spread on price dynamics is left to future research.
- The parameters beta and the volatility-scaling constant eta are fitted case by case by matching mean, standard deviation and kurtosis rather than estimated by a general statistical procedure; the authors state that formal parameter estimation is left for future work.
- Empirical validation covers only two individual US stocks over a single one-month sample (May 2025), one chosen for a varying spread and one for an effectively constant spread.
- The market-impact analysis considers only Level I (top-of-book) liquidity within a simplified linear, Almgren-Chriss-style temporary-impact setting, as the authors note.
- Reader note: because beta and eta are re-tuned separately for each stock rather than fixed in advance or estimated out of sample, the reported kurtosis matches are better read as an in-sample calibration check than as an out-of-sample predictive test.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/bid-ask-spread|bid ask spread]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/price-impact|price impact]]
- [[concepts/stylized-facts|stylized facts]]
- [[concepts/metaorder|metaorder]]
- [[concepts/micro-price|Micro-Price]]
- [[concepts/kyles-lambda|Kyle's Lambda]]

## Citation

Przemysław Rola (2025). Boltzmann Price: Toward Understanding the Fair Price in High-Frequency Markets.

DOI: 10.48550/arxiv.2507.09734

Text ingested: `markdown_output/rola-2025-boltzmann-price-toward-understanding-fair-price.md`, converted from `raw/ofi-event-clock/rola-2025-boltzmann-price-toward-understanding-fair-price.pdf`.

Coverage of this summary: Read the entire paper front to back: abstract, introduction, related work, the maximum-entropy derivation of the Boltzmann price, the price-decomposition/approximation results, the price-process modeling and its stochastic differential equation limit, all simulation subsections (varying spread, constant spread, market impact, symmetric imbalance), the historical-data analysis for GE and LCID, the market-impact section, the conclusion, and the appendix (micro-price derivation, large-tick stock example, spread/imbalance from the market maker's perspective, and additional histograms).

Known problems with the input: Nearly all mathematical equations were rendered as '==> picture... intentionally omitted <==' placeholders by the PDF-to-markdown conversion, so the exact functional forms of the Boltzmann distribution, the price SDE, and the market-impact expressions are described qualitatively from the surrounding prose rather than reproduced as extracted equations; No explicit publication year, journal, or venue is printed anywhere in the converted text (only citation years for other works and a 'May 2025' data sample), so year was taken from the job file's year_hint and venue was left empty.
<!-- AUTHORED REGION END -->