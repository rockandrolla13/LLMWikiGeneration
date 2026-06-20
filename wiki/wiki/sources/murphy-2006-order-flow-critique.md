---
title: 'Order Flow, Transaction Clock and Normality: A Critique of Ané and Geman (2006)'
page_id: sources/murphy-2006-order-flow-critique
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25 23:45:00+00:00
updated: '2026-06-20T01:03:51Z'
authors:
- Anthony Murphy
- Marwan Izzeldin
year: 2006
venue: Working Paper
tags:
- subordinated-process
- transaction-clock
- information-flow
- normality
- monte-carlo
- stochastic-time-change
- market-microstructure
related:
- concepts/stylized-facts
- concepts/long-memory
- sources/golub-2014-multiscale-liquidity
- sources/koukorinis-stylized-facts
mind_map_priority: medium
schema_version: 2
uuid: 7061d429-9b41-50b2-b1ab-8a6cde0ab500
content_hash: sha256:839b830fbe701ad95f707fa522a370bb8a3e22d424000be5bcd06086d726ac88
---

<!-- AUTHORED REGION START -->
# Order Flow, Transaction Clock and Normality: A Critique of Ané and Geman

## Summary

Murphy & Izzeldin (2006) critically examine the empirical procedure used by Ané and Geman (2000) to recover the moments of information flow from high-frequency data. Using Monte Carlo experiments, they demonstrate that higher moments of the latent information flow cannot be accurately recovered, and that returns conditioned on the recentered number of trades are not approximately Gaussian as AG claimed.

## Key Contributions

### Main Critique
The paper challenges the widely-cited finding that the "transactions clock" (number of trades) is a better representation of information flow than volume for recovering normality of returns.

### Monte Carlo Evidence
- Third and higher moments of latent information flow cannot be accurately recovered using AG's procedure
- This is not a small sample problem - persists even with 10,000 observations
- Approximate MGF (moment generating function) conditions are not informative about higher moments

### Identification Problems
1. **Scale identification:** Parameters μr and σ²r only identified up to scale since information flow it is unobserved
2. **Zero mean issue:** With high-frequency data where returns are approximately zero on average, odd moment conditions become uninformative
3. **Overparameterization:** Seven parameters cannot be identified from six moment conditions

## Methodology

### AG's Original Approach
- Returns r(t) = x(i(t)) where x(·) is Brownian motion and i(t) is stochastic time change
- Conditional on information flow it, returns are normally distributed
- Uses approximate moment generating function conditions

### Monte Carlo DGPs Tested
1. **Normal Lognormal:** Information flow lognormally distributed (Clark 1973)
2. **Normal Inverse Gaussian:** Inverse Gaussian information flow (Barndorff-Nielsen 1995)
3. **Normal Gamma:** Gamma distributed information flow (Madan & Seneta 1990)

### Bivariate Alternative
Murphy & Izzeldin propose using both returns and market activity (volume or trades) jointly:
- Conditional on it: rt ~ N(μr·it, σ²r·it) and at ~ N(μa·it, σ²a·it)
- More identifying restrictions available
- More precise moment estimation

## Key Findings

### Monte Carlo Results
| Approach | m³_i Recovery | m⁴_i Recovery |
|----------|---------------|---------------|
| AG univariate | Poor | Very poor |
| Bivariate (trades) | Good | Reasonable |
| Bivariate (volume) | Good | Reasonable |

### Empirical Evidence
Using 1997 NASDAQ data for Cisco and Intel:
- Returns conditioned on recentered transactions are NOT approximately Gaussian
- Jarque-Bera test decisively rejects normality
- Similar results for Dell and WorldCom (2000 data)

## Implications

### For Time-Change Models
- Non-parametric recovery of information flow moments is very difficult
- Parametric approaches may be necessary
- Bivariate models offer more identification power

### For Market Microstructure
- Neither volume nor trade count alone captures all features of latent information flow
- Challenge to the "transactions hypothesis" as commonly implemented
- Need for richer models of the price-volume-information relationship

## Connections to Other Work

### Related to Information Clocks
- [[sources/golub-2014-multiscale-liquidity|Golub et al. (2014)]]: Intrinsic time alternative
- [[sources/koukorinis-stylized-facts|Koukorinis et al. (2022)]]: Volume clock analysis

### Subordinated Processes Literature
- Clark (1973): Original subordinated process model
- Tauchen and Pitts (1983): Bivariate models
- Richardson and Smith (1994): GMM estimation

## Practical Implications

1. **Caution with AG procedure:** Higher moment estimates are unreliable
2. **Use bivariate approaches:** Joint modeling of returns and activity improves identification
3. **Transaction clock limitations:** Number of trades alone insufficient for normality recovery
4. **Large samples required:** Even with bivariate approach, precise higher moment estimation needs substantial data

## See Also

- [[concepts/stylized-facts|Stylized Facts]]
- [[concepts/long-memory|Long Memory]]
- [[sources/golub-2014-multiscale-liquidity|Multi-Scale Liquidity]]
- [[sources/koukorinis-stylized-facts|Koukorinis Stylized Facts]]

<!-- AUTHORED REGION END -->
