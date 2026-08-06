---
title: FX carry trade
page_id: concepts/carry-trade
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [foreign-exchange, carry-trade, currency-strategy, risk-premia, uncovered-interest-parity]
sources: [sources/serban-2010-mean-reversion-momentum-fx]
related: [concepts/uncovered-interest-parity, concepts/futures-carry, concepts/currency-exchange-rates, concepts/risk-premia]
mind_map_priority: medium
---

# FX carry trade

**FX carry trade** is borrowing in a low-interest currency and lending in a high-interest currency to harvest the interest differential, exploiting UIP failure; used here as a traditional FX benchmark that the combination strategy outperforms on a Sharpe-ratio basis.

## Overview

The carry trade is profitable precisely because [[concepts/uncovered-interest-parity|uncovered interest parity]] fails — high-interest currencies do not depreciate enough to offset the interest differential, so the carry harvests a currency [[concepts/risk-premia|risk premium]]. Serban (2010) uses it as the most common incumbent FX strategy against which to benchmark the combination strategy, citing Burnside et al. (2008) figures of roughly 4.8% average annual return and a Sharpe ratio of about 1.06 (falling only modestly to 4.44% and 0.87 after transaction costs). The paper's mean-reversion/momentum combination strategy delivers substantially higher Sharpe ratios, showing that a returns-based signal can dominate the traditional carry.

## Sources

- [[sources/serban-2010-mean-reversion-momentum-fx]] — uses the carry trade as a traditional FX benchmark that the combination strategy outperforms.

## Related Concepts

- [[concepts/uncovered-interest-parity]]
- [[concepts/futures-carry]]
- [[concepts/currency-exchange-rates]]
- [[concepts/risk-premia]]
