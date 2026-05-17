---
title: "The Behavior of Dealers and Clients on the European Corporate Bond Market: The Case of Multi-Dealer-to-Client Platforms"
page_id: sources/fermanian-2017-md2c-corporate-bonds
page_type: source
source_type: journal-article
revision_id: 1
created: 2026-04-25T22:00:00Z
updated: 2026-04-25T22:00:00Z
authors: [Jean-David Fermanian, Olivier Gueant, Jiang Pu]
year: 2017
venue: Market Microstructure and Liquidity
tags: [corporate-bonds, market-making, request-for-quotes, rfq, dealer-client, electronic-trading, competition]
related: [concepts/market-making, concepts/request-for-quotes, concepts/market-microstructure, entities/olivier-gueant]
mind_map_priority: high
---

# The Behavior of Dealers and Clients on the European Corporate Bond Market

**Authors:** Jean-David Fermanian, Olivier Gueant, Jiang Pu

**Year:** 2017

**Venue:** Market Microstructure and Liquidity, Vol. 2, Nos. 3&4

**Institutions:** ENSAE-CREST, LPMA Universite Paris-Diderot, Institut Europlace de Finance

## Summary

This paper models the request-for-quotes (RFQ) process on multi-dealer-to-client (MD2C) electronic trading platforms for European corporate bonds. Using a large proprietary database from Bloomberg Fixed Income Trading, the authors develop a model to understand dealer competition and client behavior, implicitly estimating the distributions of dealer quotes and client reservation prices.

## Key Contributions

### 1. RFQ Process Model
- Parsimonious model for MD2C platform dynamics
- Dealers' quotes follow skew exponential power (SEP) distribution
- Clients' reservation values modeled as Gaussian
- Maximum likelihood estimation framework

### 2. Competition Analysis
- Dealer behavior depends on number of competitors requested
- Clients can request up to 6 dealers on Bloomberg FIT
- Trade-off between quote aggressiveness and hit ratio
- Cover price analysis for competitive benchmarking

### 3. Market Structure Insights
- Corporate bond market transitioning from voice to electronic
- MD2C platforms dominate electronic trading
- Basel III affects dealer inventory holding
- Market remains quote-driven rather than order-driven

## Methodology

### Data Structure
- Proprietary database from BNP Paribas (reference dealer)
- ~209,000 buy RFQs and ~272,000 sell RFQs
- Years 2014-2015
- Information includes: outcome, cover price, dealer quote, number of competitors

### Model Components
- **Dealer quotes (Wk,i):** Prices answered by competing dealers
- **Client reservation value (Vi):** Latent price threshold for trading
- **Answer indicators (Ak,i):** Whether dealer k answers RFQ i
- Reduced quotes normalized by CBBT bid-to-mid spread

### Distribution Assumptions
- Skew Exponential Power (SEP) distribution for dealer quotes
  - Fat-tailed, asymmetric, spiky around composite price
- Gaussian distribution for client reservation values
- Binomial model for dealer response probability

## Key Findings

1. Dealer behavior systematically depends on competition level
2. Client reservation values follow predictable patterns
3. Not all requested dealers answer (response probability < 1)
4. CBBT prices serve as effective reference points
5. Model enables better hit ratio analysis and quote optimization

## Applications

- Assess competitor behavior for market making
- Estimate probability of trade at given price
- Optimize dealer quoting strategies
- Understand client reservation values
- Input functions for dynamic market making models

## Market Context

- Corporate bonds: illiquid, heterogeneous (multiple bonds per issuer)
- SIFMA estimates: 6x more listed corporate bonds than stocks
- Only 1% of TRACE-eligible bonds traded daily in 2012
- MD2C platforms (Bloomberg FIT, Tradeweb, MarketAxess) dominate

## See Also

- [[concepts/market-making|Market Making]]
- [[concepts/request-for-quotes|Request for Quotes]]
- [[concepts/market-microstructure|Market Microstructure]]
- [[entities/olivier-gueant|Olivier Gueant]]
