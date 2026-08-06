---
title: Uncovered interest parity
page_id: concepts/uncovered-interest-parity
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [foreign-exchange, uncovered-interest-parity, currency-strategy, no-arbitrage]
sources: [sources/serban-2010-mean-reversion-momentum-fx]
related: [concepts/currency-exchange-rates, concepts/forward-rate, concepts/no-arbitrage-restrictions, concepts/carry-rolldown]
mind_map_priority: medium
---

# Uncovered interest parity

**Uncovered interest parity** is the no-arbitrage condition that a currency trading at a forward premium should depreciate so that expected returns on domestic and uncovered foreign positions equalize; its empirical failure (the "forward puzzle") leaves tradable deviations that this paper treats as the FX analog of a stock return.

## Overview

UIP states that the change in the exchange rate should incorporate any interest-rate differential between two currencies, so that an investor borrowing at the home rate and lending abroad expects a zero return once currency moves are accounted for. Serban (2010) works directly with the deviations from UIP, defined as y = s(t+1) − f(t) (the realized next-period spot minus the current forward), computed for the Canadian Dollar, German Mark/Euro, UK Pound and Japanese Yen against the US Dollar. These deviations behave like a risky asset's returns — displaying momentum in the short run and mean reversion in the long run — which lets an equity-market trading strategy be ported to FX. UIP contrasts with Covered Interest Parity, which uses the forward rate to lock in conversion and holds under absence of riskless arbitrage.

## Sources

- [[sources/serban-2010-mean-reversion-momentum-fx]] — treats UIP deviations as a return series and builds the combination trading strategy on them.

## Related Concepts

- [[concepts/currency-exchange-rates]]
- [[concepts/forward-rate]]
- [[concepts/no-arbitrage-restrictions]]
- [[concepts/carry-rolldown]]
