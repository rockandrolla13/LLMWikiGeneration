---
authors:
- Mateusz Wilinski
- Anubha Goel
- Alexandros Iosifidis
- Juho Kanniainen
content_hash: sha256:d3fb33251161871703f1a0e3c2dc14e9bdbdfa30eed71ed1550510b7e368691a
created: 2026-09-27 01:47:00+00:00
page_id: sources/wilinski-2026-classifying-clustering-trading-agents
page_type: source
publication_venue: Quantitative Finance
related:
- concepts/event-clock
- concepts/trader-clustering
- concepts/hierarchical-clustering
- concepts/limit-order-book
- concepts/market-making
- concepts/high-frequency-trading
- concepts/market-microstructure
- concepts/feature-engineering
- entities/alexandros-iosifidis
- entities/juho-kanniainen
revision_id: 1
schema_version: 2
source_hash: sha256:fc64c369566508a09a97d0698474025228ed9fd5935fef706c8e6b76d2b98301
source_path: markdown_output/wilinski-2026-classifying-clustering-trading-agents.md
source_type: paper
tags:
- agent-based-modeling
- trader-classification
- clustering
- limit-order-book
- svm
- deep-learning
- synthetic-data
- clock-event
- asset-simulated
- added-by-hand
title: Classifying and clustering trading agents
updated: '2026-09-27T01:47:00Z'
uuid: e32dbee7-823c-53eb-9184-a4422a83a6e2
year: 2026
---

<!-- AUTHORED REGION START -->
# Classifying and clustering trading agents

## Summary

The paper asks how accurately individual trading agents can be sorted into their true behavioral categories from investor-level limit order book data, a question motivated by the lack of ground-truth labels in real markets and the limited interpretability of many machine-learning methods used for this purpose.

To get around the missing ground truth, the authors build a synthetic continuous double-auction limit order book market populated by five main classes of agents (market makers, market takers, chartists, fundamentalists and noise traders), further split into 15 parametrized subclasses. They compute 18 behavioral features per agent -- 9 drawn from prior literature and 9 new ones the authors design, including price-trend and fundamental-event profit measures -- and feed them to both supervised classifiers (SVM and a deep neural network) and unsupervised clustering methods (five candidate algorithms, with hierarchical clustering selected as the most stable).

Supervised classification recovers the true agent classes with high accuracy, especially for market makers and market takers, while fundamentalists remain the hardest class to separate because their behavior also depends on an unobserved fundamental price. Unsupervised clustering is systematically worse than classification on the same data and features, and degrades further as synthetic noise is added or as the number of clusters is forced to match the true number of classes.

The main contribution is using an agent-based synthetic market as a controlled testbed with true labels, which lets the authors directly quantify the gap between supervised and unsupervised investor profiling and identify which hand-crafted features -- especially directional trend and fundamental-event features -- drive successful classification.

## Clock and Sampling

**Event clock: one observation per order book update.**

See [[concepts/event-clock|Event Clock]].

The simulated market is continuous-time and event-driven: agents arrive and act (send, modify or cancel limit/market orders) at exponentially or Gaussian-distributed times rather than on a fixed clock, and the order book state updates after each such event. There is no single forecasting horizon; instead, agent-level features are computed by aggregating each agent's own orders, trades and cancellations over an entire simulation run, with some features computed over short, medium and long look-back and look-forward windows expressed in simulation time units.

## Data

- **Asset class:** Simulated data
- **Instruments:** A single simulated asset traded through a continuous double-auction limit order book, populated by 15 parametrized subclasses of agents across 5 behavioral classes (market makers, market takers, chartists, fundamentalists, noise traders).
- **Venue:** not stated (synthetic agent-based simulation, no real exchange)
- **Period:** not applicable to real markets; the paper uses 40 independent simulation runs of 20 simulated hours each, with 1590 agents per run (1060 of which are noise traders in the no-noise setting).
- **Granularity:** 18 behavioral features computed per agent per simulation run, aggregated from that agent's own orders, trades and cancellations over the whole run.

## Features and Measures

- **Buy ratio.** Share of an agent's total orders that are buy orders.
- **Cancellation ratio.** Share of an agent's orders that are cancelled before being fully executed.
- **Number of trades.** Average number of trades an agent completes per simulation run.
- **Market ratio.** Share of an agent's orders that are market orders rather than limit orders.
- **Mean order creation time.** Average time gap between an agent's successive order submissions.
- **Standard deviation of creation time.** Variability of the time gaps between an agent's successive order submissions.
- **Mean order size.** Average size of an agent's orders.
- **Standard deviation of order size.** Variability of an agent's order sizes.
- **Total traded volume.** Sum of all volume traded by an agent over a simulation run.
- **Short trend.** Average absolute change in mid-price between the time an order was sent and a short look-back window earlier.
- **Short directed trend.** Average short-horizon mid-price change signed by the agent's order direction (buy or sell), capturing whether the agent trades with or against the recent trend.
- **Medium trend.** Same as the short trend feature but measured over a longer, medium look-back horizon.
- **Medium directed trend.** Same as the short directed trend feature but measured over the medium look-back horizon.
- **Long trend.** Same as the short trend feature but measured over the longest look-back horizon used.
- **Long directed trend.** Same as the short directed trend feature but measured over the longest look-back horizon.
- **Fundamental profit.** Average directional return earned on orders placed shortly after a simulated fundamental-price jump, computed only from price and order direction rather than from an actual closed position.
- **Long fundamental profit.** Same as fundamental profit but measured over a longer post-event look-forward window.
- **Weighted fundamental profit.** Same as fundamental profit but averaged with each order weighted by its size.

## Method

Training and test data come from a purpose-built agent-based limit order book simulator rather than real trading records, so that agent-level ground-truth labels are available. Five broad agent classes (market makers, market takers, chartists, fundamentalists and noise traders) are split further into 15 parametrized subclasses, with orders arriving continuously through an event-driven double-auction mechanism using price-time priority. The authors run 40 independent 20-hour simulations and then construct three noise settings by merging the trading records of an increasing number of noise traders into other agents' activity, producing a no-noise case and 50%- and 66.6%-noise cases.

For every agent the authors compute 18 features, split into 9 features drawn from prior literature (order/trade counts, timing and size statistics, cancellation and market-order ratios) and 9 new features designed by the authors (short/medium/long price-trend measures, their directional counterparts, and profit measures computed around the simulated fundamental-price jumps). Agents are classified into their 15 true classes with a support vector machine and a deep neural network, tuned by grid search and by the Ray Tune library respectively, on a 60/10/30 train/validation/test split, with performance reported via confusion matrices, precision, recall and F1-score.

For clustering, the same features are given to five candidate algorithms (k-means, k-medoids, hierarchical clustering, spectral clustering, kernel k-means); a stability-based selection criterion is used to choose hierarchical clustering with Ward's linkage as the method carried forward. The number of clusters is chosen via the silhouette coefficient and the within-cluster sum of squares elbow, and results are also reported when the number of clusters is forced to match the true number of agent classes (15 without noise, 14 with noise), so that clustering accuracy can be compared directly against the supervised classification accuracy on the same held-out test data.

## Results

- With all 18 features and no additional noise, both SVM and DNN reached an overall classification accuracy of 0.99; accuracy fell to 0.91 (SVM) and 0.90 (DNN) once noise was raised to the 66.6% level.
- Using only the 9 baseline features roughly halved performance under heavy noise: overall accuracy fell to 0.58 (SVM) and 0.57 (DNN) in the 66.6%-noise, 9-feature setting, versus 0.85 for both methods with no noise.
- Market makers and market takers were classified almost perfectly in nearly every setting, while fundamentalists were consistently the hardest class to separate, with some fundamentalist subclasses receiving an F1-score of 0.00 when only 9 features were available.
- Hierarchical clustering with Ward's linkage and k=9 clusters on 18 features reached an overall accuracy of 94.39%, but this required merging several distinct agent types into single clusters, such as all fundamentalists (F1=0.4725) and market takers with noise traders (F1=0.9709).
- Forcing the number of clusters to match the true number of agent classes reduced clustering accuracy, e.g. from 94.39% to 75.33% with 18 features and no noise.
- Clustering accuracy fell further under 66.6% noise, reaching 63.21% (k=9, 18 features) and 55.83% (k=14, 9 features).
- The chosen Ward's-linkage clustering solution had a cophenetic correlation of 70% with the original distance matrix, and the silhouette coefficient peaked at k=9 (S=0.134).
- Across every noise level and feature set tested, supervised classification accuracy exceeded unsupervised clustering accuracy on the same underlying data.

## Limitations

- The agents and market are synthetic and simplified relative to real trading strategies, as the authors themselves note.
- Real investors are not cleanly grouped into fixed behavioral classes and may switch strategies over time, unlike the simulated agents.
- The clustering methods used do not scale to the very large numbers of investors seen in real financial data, which the authors flag as a limitation.
- Reader note: results are demonstrated on a single simulated asset and a single agent-based model design, so generalization to real multi-asset markets with real investor-level data is unverified.

## Related

- [[concepts/event-clock|Event Clock]]
- [[concepts/trader-clustering|trader clustering]]
- [[concepts/hierarchical-clustering|hierarchical clustering]]
- [[concepts/limit-order-book|limit order book]]
- [[concepts/market-making|market making]]
- [[concepts/high-frequency-trading|high frequency trading]]
- [[concepts/market-microstructure|market microstructure]]
- [[concepts/feature-engineering|feature engineering]]
- [[entities/alexandros-iosifidis|Alexandros Iosifidis]]
- [[entities/juho-kanniainen|Juho Kanniainen]]

## Citation

Mateusz Wilinski, Anubha Goel, Alexandros Iosifidis, Juho Kanniainen (2026). Classifying and clustering trading agents. Quantitative Finance.

DOI: 10.1080/14697688.2026.2651768

Text ingested: `markdown_output/wilinski-2026-classifying-clustering-trading-agents.md`, converted from `raw/ofi-event-clock/wilinski-2026-classifying-clustering-trading-agents.pdf`.

Coverage of this summary: Read the full markdown file, including the introduction, methods (synthetic environment, features, supervised classification and unsupervised clustering methods), results (classification and clustering), discussion, limitations and future directions, and the reference list.

Known problems with the input: Markdown has PDF-conversion artifacts, including superscripts rendered as bracketed numbers (e.g. '10[3]') and several equations/figures replaced with 'picture... intentionally omitted' placeholders, so some exact functional forms and figure-only results could not be verified from text alone.
<!-- AUTHORED REGION END -->