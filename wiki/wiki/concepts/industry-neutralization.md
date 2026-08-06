---
title: Industry Neutralization
page_id: concepts/industry-neutralization
page_type: concept
created: 2026-07-23T12:00:00Z
updated: 2026-07-23T12:00:00Z
tags: [factor-models, factor-investing, quantitative-trading, statistical-arbitrage]
sources: [sources/kakushadze-2015-101-formulaic-alphas]
related: [concepts/factor-models, concepts/factor-investing, concepts/minimum-variance-portfolio]
mind_map_priority: medium
---

# Industry Neutralization

**Industry Neutralization** is cross-sectionally demeaning a quantity within industry groups (sectors, industries, subindustries) defined by a binary industry classification such as GICS, BICS, NAICS or SIC, via the indneutralize operator, to remove group-level exposure from an alpha.

## Overview

In *101 Formulaic Alphas*, industry neutralization is implemented through the `indneutralize` operator, which demeans a signal cross-sectionally within groups defined by a binary industry classification. The relevant groupings — sectors, industries, and subindustries — can come from standard schemes such as GICS, BICS, NAICS, or SIC. Applying it strips out group-level (e.g. sector) exposure so that an alpha bets on within-group dislocations rather than broad industry moves. Several of the 101 alphas invoke this operator as part of their construction.

## Sources

- [[sources/kakushadze-2015-101-formulaic-alphas]] — defines the indneutralize operator and applies it in several of its alphas.

## Related Concepts

- [[concepts/factor-models]]
- [[concepts/factor-investing]]
- [[concepts/minimum-variance-portfolio]]
