---
authors:
- Tadeu Augusto Ferreira
content_hash: sha256:e04f35912794942413d08485ee893e5811fb4f8ce8fd9ca1376386368a23d8ff
created: 2026-09-27 01:47:00+00:00
page_id: sources/ferreira-2020-machine-learning-algorithmic-trading-leading-reinforced
page_type: source
publication_venue: Graduate Department of Statistical Sciences, University of Toronto
  (PhD thesis)
related:
- concepts/limit-order-book
- concepts/optimal-execution
- concepts/lstm-networks
- concepts/recurrent-neural-networks
- concepts/deep-learning-for-finance
- concepts/high-frequency-trading
- concepts/order-imbalance
- concepts/market-microstructure
revision_id: 1
schema_version: 2
source_hash: sha256:dc37aacfc40eae23a3cf55692746e7a54eb14b80e6beb9ebdffa6ea937424ba6
source_path: markdown_output/ferreira-2020-machine-learning-algorithmic-trading-leading-reinforced.md
source_type: paper
tags:
- reinforcement-learning
- optimal-execution
- deep-kalman-filter
- limit-order-book
- restricted-boltzmann-machine
- phd-thesis
- market-order-prediction
- lstm
- clock-calendar
- asset-equity
- harvest-relevant
title: Machine Learning in Algorithmic Trading leading to Reinforced Deep Kalman Filters
updated: '2026-09-27T01:47:00Z'
uuid: 80c92104-9a41-5306-835a-c80f5fbff952
year: 2020
---

<!-- AUTHORED REGION START -->
# Machine Learning in Algorithmic Trading leading to Reinforced Deep Kalman Filters

## Summary

The thesis first asks whether the direction of the next market order can be predicted from the state of the limit order book, comparing first-order Markov models and hidden Markov models of bid-ask price transitions, then testing restricted Boltzmann machine (RBM) classifiers, including a Gaussian-Bernoulli RBM and a discriminative Gaussian-Bernoulli RBM (DGB-RBM), against a naive bid-ask depth-imbalance benchmark on Netflix, Microsoft, Dell and Hewlett-Packard order-book data.

The second and larger part asks how to optimally liquidate a stock position under price risk and market impact, framed as a reinforcement learning problem. Benchmarks are Q-learning and model-based DynaQ variants using ARIMA or LSTM price forecasters. The thesis's central proposal, the Reinforced Deep Kalman Filter (RDKF), models the market as a partially observable Markov decision process, filtering noisy, incomplete price and reward observations with a deep-Kalman-filter-style network and searching for an execution policy that also conditions on the filter's own uncertainty about the latent state.

The DGB-RBM improved market-order-direction prediction over the naive imbalance benchmark by up to an 18% increment in AUC. In the optimal-execution experiments, the RDKF produced higher average and accumulated trading reward than all reinforcement-learning and TWAP benchmarks on both a simulated mean-reverting price process and real order-book data for Intel, Microsoft, Vodafone and Facebook, despite being trained on only half the data given to the benchmarks, and most of these differences were statistically significant in paired t-tests.

What is new is the RDKF architecture itself: a single model that filters noisy market observations, lets the agent's own actions affect the latent state, and performs policy search directly over the filtered posterior (mean and uncertainty) rather than over raw observations, combined with an ablation study isolating the contribution of the state-uncertainty input and of extra simulated training trajectories.

## Clock and Sampling

**Calendar clock: fixed wall-clock intervals.**

Part I predicts the sign of each incoming market order using the book state at the prior order arrival, so those observations are one per market-order event. Part II resamples order-execution tick data to a fixed one-second calendar-time mid-price series, and the RL/RDKF agent acts once per one-second step across 500-step (500-second) training and test episodes. The RDKF was trained on the first 200,000 seconds of data for FB, MSFT and INTC (150,000 for VOD) out of 400,000 (200,000 for VOD) total selected points, and tested on the remaining, later portion of the series.

## Data

- **Asset class:** Equities
- **Instruments:** Netflix (NFLX), Microsoft (MSFT), Dell (DELL), Hewlett-Packard (HPQ) for the market-order-prediction chapters; Intel (INTC), Microsoft (MSFT), Facebook (FB) and Vodafone (VOD) for the optimal-execution chapter.
- **Venue:** NASDAQ, stated for the NFLX/MSFT/DELL/HPQ data in Chapters 3-4; not stated for the INTC/MSFT/FB/VOD order-book data used in Chapter 6.
- **Period:** NFLX/MSFT single-day intraday data from 2011 (Ch.3); MSFT LOB from January 2010, and DELL and HPQ from April 2013 (Ch.4); INTC, MSFT and FB traded between January 2018 and March 2018, and VOD traded in 2017 (Ch.6).
- **Granularity:** Ch.3-4: order-book depth at the touchline sampled at each market-order arrival (event-by-event). Ch.6: mid-prices resampled to 1-second calendar intervals from limit-order-book tick-by-tick executions, split into 500-observation batches; the total selected series is 400,000 points for INTC/MSFT/FB and 200,000 for VOD, of which the first 200,000 (150,000 for VOD) are used for RDKF training and the remaining 200,000 (50,000 for VOD) for testing.

## Features and Measures

- **Bid-ask depth imbalance.** The bid depth divided by the sum of bid and ask depths at the touchline, used both as an RBM input and as a simple 'naive predictor' benchmark for the direction of the next market order.
- **LOB binary-picture encoding.** Ask and bid depths converted into a fixed-size binary array (activated/deactivated pixels) as an alternative RBM input to the scalar imbalance measure.
- **Relative savings (RS).** A per-batch measure comparing the total trading reward achieved by the RDKF against a benchmark execution policy on the same price path, used to compare profitability of execution strategies.
- **State uncertainty input.** The covariance of the RDKF's approximated posterior over the latent market state at time t, fed into the policy network alongside the posterior mean so the execution decision accounts for the filter's own confidence.

## Method

Part I compares first-order Markov models and hidden Markov models (trained by expectation-maximisation) for bid-ask price dynamics, then develops supervised classifiers built on restricted Boltzmann machines (RBM) to predict the sign of the next market order from the prior limit-order-book state. Binary RBMs (fed either bid-ask depth-imbalance or a binary-picture LOB encoding) are trained by contrastive divergence and Gibbs sampling; a Gaussian-Bernoulli RBM (GB-RBM) and its discriminative, supervised counterpart (DGB-RBM) are trained by stochastic gradient descent. Performance is judged against the naive depth-imbalance classifier using accuracy at different probability thresholds and the area under the ROC curve (AUC).

Part II frames optimal liquidation as a reinforcement learning problem: an agent holding a stock inventory chooses how many shares to sell at each step to trade off price risk, permanent price impact and holding-inventory penalties. Benchmarks are Q-learning and model-based DynaQ variants that use an ARIMA or LSTM price forecaster inside the planning loop. The Reinforced Deep Kalman Filter (RDKF) casts the same problem as a partially observable Markov decision process: an LSTM summarises past actions, observations and rewards into a hidden state, from which a deep-Kalman-filter-style recognition/emission network approximates the posterior distribution of the latent market state, and a deterministic policy network turns the posterior mean and covariance into the next action. The model is trained by maximising a variational lower bound on the observation likelihood jointly with a gradient-based policy search over expected reward, both optimised with ADAM.

Performance is evaluated first on a simulated mean-reverting price process, then on real limit-order-book mid-prices, using mean and accumulated batch reward, relative savings in basis points, and paired t-tests of the difference in total reward between the RDKF and each benchmark (Q-learning, DynaQ-ARIMA, DynaQ-LSTM, a DynaQ using the RDKF's own filter (DynaQ-DKF), an RDKF ablation without the state-uncertainty input (RDKF-NoU), a time-weighted-average-price baseline (TWAP3), and an RDKF trained on additional simulated trajectories (RDKFx)).

## Results

- The discriminative Gaussian-Bernoulli RBM (DGB-RBM) beat the naive bid-ask depth-imbalance classifier by up to an 18% increment in AUC, with the largest gain on the Hewlett-Packard data.
- In Chapter 3, the plain binary RBM also slightly outperformed the naive imbalance classifier in AUC on single-day tests: 0.6805 vs 0.6675 for Netflix and 0.833 vs 0.831 for Microsoft.
- On the simulated mean-reversion liquidation task, RDKF's average reward per test batch (2105.30) exceeded Q-learning (2104.90), DynaQ-ARIMA (2105.08) and DynaQ-LSTM (2104.89), with paired-t-test mean differences of $0.38, $0.21 and $0.40 (all p=0.000).
- On real order-book data for Intel, Microsoft, Vodafone and Facebook, RDKF achieved the highest mean batch reward in nearly every test set while training on only half the data the benchmarks were given.
- Paired t-tests of total reward showed RDKF significantly ahead of Q-learning, DynaQ-ARIMA, DynaQ-LSTM, DynaQ-DKF, the RDKF-NoU ablation and the TWAP3 baseline on all four real stocks.
- Removing the state-uncertainty input from the policy (RDKF-NoU ablation) always underperformed the full RDKF, indicating that input contributes to the result.
- Feeding the policy extra simulated trajectories (RDKFx) gave at best a marginal improvement (Vodafone) or no change (Microsoft), and a slight loss (Intel, Facebook), so the benefit of extra simulated data was inconsistent.

## Limitations

- Chapters 2-4 experiments use single-stock, single- or few-day intraday windows, a small basis for generalising to other regimes.
- The real-data optimal-execution experiments use price and inventory ranges the author calls small, and the author notes Q-learning/DynaQ scale poorly to wider price or inventory ranges.
- RDKFx's benefit from extra simulated trajectories is inconsistent across the four real stocks, and the author flags this as unresolved.
- The author states that time constraints prevented testing the RDKF with fuller LOB inputs (order types, multi-level depths) beyond mid-price and inventory.
- Reader note: the RL benchmarks (Q-learning, DynaQ variants) are given access to the full real-data set for training while RDKF sees only the first half, so although this is framed as showing RDKF's data efficiency, the two are not compared under identical training-data conditions.

## Related

- [[concepts/limit-order-book|limit order book]]
- [[concepts/optimal-execution|optimal execution]]
- [[concepts/lstm-networks|lstm networks]]
- [[concepts/recurrent-neural-networks|recurrent neural networks]]
- [[concepts/deep-learning-for-finance|deep learning for finance]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/order-imbalance|order imbalance]]
- [[concepts/market-microstructure|market microstructure]]

## Citation

Tadeu Augusto Ferreira (2020). Machine Learning in Algorithmic Trading leading to Reinforced Deep Kalman Filters. Graduate Department of Statistical Sciences, University of Toronto (PhD thesis).

Text ingested: `markdown_output/ferreira-2020-machine-learning-algorithmic-trading-leading-reinforced.md`, converted from `raw/ofi-event-clock/ferreira-2020-machine-learning-algorithmic-trading-leading-reinforced.pdf`.

Coverage of this summary: Read the front matter, abstract, table of contents, Chapter 1 (LOB definitions, liquidation problem), Chapter 3 (RBM applied to LOBs, Section 3.4 results), Chapter 4 (GB-RBM/DGB-RBM experiments and conclusions), Chapter 5 (RL introduction, MDP formulation, optimal liquidation setup), Chapter 6 (RDKF motivation, model formulation, synthetic and real-data experiments in full, discussion/conclusions), and Chapter 7 (summary of contributions, future directions); did not read the detailed derivations in Chapter 2 (HMM/MM), Sections 5.3-5.6 algorithmic detail, Chapter 6.3-6.5 optimisation equations, or the appendices.

Known problems with the input: Many equations and figures are rendered as '==> picture... intentionally omitted <==' by the PDF-to-markdown conversion, so exact formal definitions (e.g. the RDKF's loss functions and update equations) could not be transcribed and are described only in words.
<!-- AUTHORED REGION END -->