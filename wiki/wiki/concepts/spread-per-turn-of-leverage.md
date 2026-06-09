---
created: 2026-05-05 23:20:00+00:00
page_id: concepts/spread-per-turn-of-leverage
page_type: concept
related:
- concepts/credit-spread-curve
- concepts/hyperscaler-data-center-bond-relative-value
- concepts/leverage-ratios
- concepts/relative-value-analysis
revision_id: 2
sources:
- sources/spec-2012-single-name-fundamental
tags:
- creditETF
- relative-value
- credit-analysis
- leverage
title: Spread Per Turn of Leverage
updated: '2026-06-09T12:00:00Z'
---

# Spread Per Turn of Leverage

**Spread Per Turn of Leverage (SPL)** is a relative value metric that normalizes credit spreads by the issuer's leverage, enabling comparison across companies with different debt levels.

## Definition

```
SPL = CDS Spread / (Net Debt / EBITDA)
```

Where:
- CDS Spread: Typically 5-year CDS level
- Net Debt/EBITDA: Leverage ratio (can use LTM or NTM forecast)

## Interpretation

SPL measures how much spread the market is charging **per unit of leverage**. It allows identification of:

- **Cheap names:** Low SPL relative to sector (paying less per turn)
- **Rich names:** High SPL relative to sector (paying more per turn)

## Relative Value Analysis

### Within-Sector Comparison

Compare company SPL to sector average (excluding the company):

```
"Predicted" Spread = (Sector Average SPL) × (Company Leverage)
Actual - Predicted = Relative Value Signal
```

### Example

| Company | Spread | Leverage | SPL | Sector Avg SPL | Predicted | Rich/Cheap |
|---------|--------|----------|-----|----------------|-----------|------------|
| A | 240 | 1.50x | 160 | 173 | 260 | Cheap (-20) |
| B | 350 | 2.25x | 156 | 174 | 393 | Cheap (-43) |
| C | 330 | 1.65x | 200 | 163 | 270 | Rich (+60) |

**Interpretation:** Company C is expensive (paying more spread per turn than peers), while B is cheap (paying less per turn despite higher absolute leverage).

## Variants

### LTM vs. NTM

- **LTM (Last Twelve Months):** Uses historical leverage
- **NTM (Next Twelve Months):** Uses analyst forecast leverage

NTM variant captures market expectations about deleveraging/releveraging.

### Alternative Denominators

Similar analysis frameworks use:
- Interest coverage ratio (EBIT/Interest Expense)
- Total debt/EBITDA
- Free cash flow/debt

## Applications

1. **Sector Screening:** Rank names by SPL within sector
2. **Trade Idea Generation:** Long cheap, short rich
3. **Fundamental Validation:** Cross-check fundamental views vs. market pricing
4. **Stress Testing:** Assess spread impact of leverage changes

## Limitations

- Assumes linear relationship between spread and leverage
- Sector composition affects benchmark
- Doesn't capture other credit factors (business risk, asset quality)
- Point-in-time snapshot

## See Also

- [[concepts/relative-value-analysis]]
- [[concepts/leverage-ratios]]
- [[sources/spec-2012-single-name-fundamental]]

## Related (credit-macro ingest, 2026-06-09)

- [[concepts/hyperscaler-data-center-bond-relative-value|hyperscaler-data-center-bond-relative-value]]