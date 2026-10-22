---
authors:
- Arik Ben Dor
- Albert Desclée
- Lev Dynkin
- Jay Hyman
- Simon Polbennikov
chapter: 19
content_hash: sha256:8aa69ecedd3c100d15885244a7eaca4d6165321b6691ce9d58a7ff71023133e8
created: '2026-10-22T15:31:24Z'
mind_map_priority: high
page_id: sources/bendor-2021-onescore-chapter-19
page_type: source
part_of: sources/bendor-2021-systematic-investing-in-credit
pdf_pages: 625-635
publisher: John Wiley & Sons
related:
- sources/bendor-2021-systematic-investing-in-credit
- concepts/quantamental-investing
- concepts/excess-spread-to-peers
- concepts/equity-momentum-in-credit
- concepts/duration-times-spread
- concepts/factor-signals-in-credit
- entities/arik-ben-dor
- entities/albert-desclee
- entities/lev-dynkin
- entities/jay-hyman
- entities/simon-polbennikov
- sources/dickerson-2026-corporate-bond-factor-replication-crisis
revision_id: 1
schema_version: 2
source_hash: sha256:3da27977b1a55ad23821c375533cf247df4c4c48f5b837e031bbc7993871f59d
source_path: markdown_output/bendor-2021-onescore-chapter-19.md
source_type: book
sources: []
tags:
- onescore
- quantamental
- credit-factors
- relative-value
- equity-momentum
- dts
- signal-combination
title: 'OneScore: Combining Quantitative and Fundamental Views in Credit'
updated: '2026-10-22T15:31:24Z'
updated_by: op_6041749c5f06
uuid: 9ff4eebd-0516-51bd-91a0-5091e50af13f
year: 2021
---

<!-- AUTHORED REGION START -->
# OneScore: Combining Quantitative and Fundamental Views in Credit

*Chapter 19 of [[sources/bendor-2021-systematic-investing-in-credit|Systematic Investing in Credit]] (Ben Dor, Desclée, Dynkin, Hyman & Polbennikov, Wiley, 2021), PDF pages 625–635.*

**Converted text:** `markdown_output/bendor-2021-onescore-chapter-19.md`. Its Part 1 is the chapter text. Its Part 2 holds Tables 19.2–19.4, transcribed from page images because the PDF text layer garbles them.

## Summary

OneScore is an issuer-level score that combines two credit signals: relative value, measured by [[concepts/excess-spread-to-peers|excess spread to peers (ESP)]], and [[concepts/equity-momentum-in-credit|equity momentum in credit (EMC)]]. It differs from the bond-level blend of Chapter 18 in two ways. It aggregates the signals to the issuer, because analyst recommendations in investment-grade credit are made on issuers, not bonds. And it ranks within industry sectors, so every sector has top and bottom names and the output lines up with how fundamental research teams are organised.

The point of adding momentum to value is to avoid value traps: issuers that look cheap because their business keeps getting worse. The authors present OneScore as the quantitative half of a [[concepts/quantamental-investing|quantamental]] process. The model screens the whole universe and points analysts at issuers that score well against sector peers. The analysts then add depth the model lacks.

The top-minus-bottom OneScore portfolio outperformed in every sector over the five years to February 2020. The chapter's more general lesson concerns risk matching. Without matching the long and short legs on [[concepts/duration-times-spread|DTS]], value looks pro-cyclical and momentum looks contra-cyclical. Once DTS is matched, both add value in drawdowns and in calm periods, and the combined score is steady across regimes.

## Construction

1. **Inputs.** Bond-level ESP (Chapter 13) and EMC (Chapter 15) scores for the Bloomberg Barclays US Corporate investment-grade index.
2. **Drop short bonds.** Exclude bonds with three years or less to maturity. Their contribution to excess return is small, because excess return scales with spread duration, yet trading them still costs money.
3. **Aggregate to the issuer.** For each issuer, average the ESP scores of its remaining bonds, weighted by market value. Do the same for EMC.
4. **Rank within sector.** Rank (normalise) issuer ESP and issuer EMC separately within each industry sector.
5. **Combine.** Average the two normalised ranks with equal weights.
6. **Re-rank and bucket.** Re-rank the average within each sector, then assign deciles from 1 to 10. A higher OneScore means a more attractive issuer within its sector.

In symbols, for issuer *i* in sector *s*:

$$\mathrm{OneScore}_i = \mathrm{Decile}_s\Big(\mathrm{rank}_s\big[\tfrac12\,\mathrm{rank}_s(\overline{\mathrm{ESP}}_i) + \tfrac12\,\mathrm{rank}_s(\overline{\mathrm{EMC}}_i)\big]\Big)$$

where the bars are market-value-weighted averages over the issuer's bonds with more than three years to maturity. (This notation is ours; the book describes the steps in words.)

**Test portfolios.**
- At the start of each month, form equally weighted top and bottom portfolios across all sectors.
- Each sector contributes at most 10 issuers to each side, and fewer in concentrated sectors such as transportation.
- Within an issuer, bonds are market-value weighted, again excluding bonds of three years or less.
- Returns are excess returns over duration-matched Treasuries. The book says total returns show similar top-over-bottom results.
- No turnover constraints. All results are **before transaction costs**. The authors point to Chapter 18's turnover controls for live use.

**DTS matching.**
- Divide each leg's monthly excess return by its beginning-of-month DTS, then multiply by 12.
- 12 is close to the time-average DTS of the US Corporate IG index from 1993 to 2020.
- Both legs therefore carry the same DTS each month.
- In practice, targeting DTS could mean holding cash in volatile high-spread periods and using leverage in benign ones.

**Worked example.** On 28 February 2020, Kinross Gold (KCN) was among the top OneScore issuers in basic industry, with ESP = 8.1 and EMC = 9.4. Fundamental analysts rated it Overweight, so the two views agreed. The chapter uses this to show the intended workflow: the model score sits next to the analyst's rating and commentary.

## Evidence

**All sectors combined, top minus bottom, periods ending 28 February 2020 (Table 19.2):**
- Average excess return: 3.24%/yr over 1 year, 3.24%/yr over 3 years, 4.00%/yr over 5 years.
- Volatility: 0.49%, 0.52% and 0.83% a year.
- Information ratio: 6.58, 6.23 and 4.84.

**By sector:** the long-short portfolio had positive returns over 1, 3 and 5 years in every sector. The authors highlight basic industry, consumer cyclical and technology as especially strong. Energy is the weakest: its information ratio is below 1 at every horizon (0.08, 0.9 and 0.93). The full table is at the end of this page.

**Drawdowns (Table 19.3), returns in bp per month.** The authors define eight credit drawdown episodes from 1997 to 2020. In every one, the DTS-matched OneScore long-short portfolio earned a positive return. Examples:
- Mar 2007–Nov 2008: the index lost 128bp a month and DTS-matched OneScore earned 43.
- Jan 2020–Mar 2020: the index lost 432bp a month and DTS-matched OneScore earned 89.
- Outside drawdowns (230 months): DTS-matched OneScore earned 31.

Without DTS matching, ESP lost money in three episodes, including −77bp a month in Jan–Mar 2020. EMC never did.

**Correlation with the IG index (Table 19.4, January 1993 to March 2020):**

| Strategy | Drawdowns, outright | Drawdowns, DTS-matched | Other periods, outright | Other periods, DTS-matched |
|---|---|---|---|---|
| ESP | 34% | −6% | 44% | −22% |
| EMC | −64% | −50% | 20% | −11% |
| OneScore | −37% | −48% | 35% | −28% |

Read: matching on DTS removes most of ESP's market exposure. It makes OneScore more defensive in drawdowns, and turns its calm-period correlation from positive (35%) to negative (−28%).

## What the Chapter Shows

- **Combining helps because the parts disagree in crises.** In drawdowns, outright ESP and EMC are negatively correlated (−32%). In calm periods they are positively correlated (43%).
- **Much of the "cyclicality" of value and momentum is a risk bias, not a property of the signal.** Top-ESP names carry more spread risk, so outright ESP is pro-cyclical. In volatile periods, top-EMC names tend to be safer, lower-OAS issuers. That flight to quality makes outright EMC contra-cyclical.
- **Sector-neutral, issuer-level ranking** fits how analysts work. It also separates issuer selection from sector allocation.

## Caveats

- All performance is **before transaction costs**, with **no turnover limits**.
- The sector table covers only the five years to February 2020, a short and mostly benign window. The sector portfolios are concentrated, with at most 10 issuers a side.
- Investment-grade USD only. The test is in-sample research by the signal's own authors, and the chapter reports no out-of-sample hold-out.
- Equal weighting across issuers is a test design. It is not a capacity-weighted portfolio.

## Use for Bond Signals

- **A template for combining signals.** Aggregate to issuer (MV-weighted, maturity > 3y). Rank within sector. Average the ranks. Re-rank. Bucket. This applies to any pair or set of issuer-level signals.
- **Always DTS-match the legs** before judging whether a signal is pro- or contra-cyclical. Unmatched results confuse spread beta with alpha.
- **Momentum as a value-trap filter.** Combine a cheapness signal with a news or flow signal, so cheap-and-deteriorating names don't dominate the long side.
- **Next tests to run:** costs and turnover (Chapter 18's buffers), a post-2020 out-of-sample period, high yield, and the corrected bond-return data of [[sources/dickerson-2026-corporate-bond-factor-replication-crisis|Dickerson, Robotti & Rossetti (2026)]].

## Concepts

- [[concepts/quantamental-investing|Quantamental Investing]]
- [[concepts/excess-spread-to-peers|Excess Spread to Peers (ESP)]]
- [[concepts/equity-momentum-in-credit|Equity Momentum in Credit]]
- [[concepts/duration-times-spread|Duration Times Spread]]
- [[concepts/factor-signals-in-credit|Factor Signals in Credit]]

## Entities

- [[entities/arik-ben-dor|Arik Ben Dor]]
- [[entities/albert-desclee|Albert Desclée]]
- [[entities/lev-dynkin|Lev Dynkin]]
- [[entities/jay-hyman|Jay Hyman]]
- [[entities/simon-polbennikov|Simon Polbennikov]]

## Appendix: Table 19.2 by Sector (top minus bottom, periods ending 28 February 2020)

| Sector | Return 1y / 3y / 5y (%/yr) | Information ratio 1y / 3y / 5y |
|---|---|---|
| Basic Industry | 3.36 / 5.16 / 8.57 | 1.25 / 2.3 / 1.69 |
| Capital Goods | 3.49 / 2.44 / 2.47 | 2.72 / 2 / 1.67 |
| Consumer Cyclical | 4.51 / 4.77 / 4.91 | 3.49 / 4.09 / 3.61 |
| Healthcare & Pharma | 5.05 / 4.95 / 3.82 | 2.34 / 2.59 / 1.95 |
| Noncyclical | 3.7 / 2.28 / 3.00 | 2.75 / 1.62 / 2.09 |
| Energy | 0.27 / 2.24 / 4.73 | 0.08 / 0.9 / 0.93 |
| Utility | 1.94 / 2.76 / 3.6 | 1.15 / 1.69 / 2.09 |
| Technology | 3.47 / 3.09 / 4.22 | 2.26 / 2.14 / 2.33 |
| Communication | 3.28 / 2.56 / 3.03 | 1.93 / 1.67 / 1.7 |
| Banking, Brokerage, Financing | 3.45 / 2.75 / 3.57 | 2.09 / 2.12 / 2.91 |
| Insurance | 3.51 / 3.88 / 4.01 | 2.27 / 3.05 / 2.17 |
| REITS | 3.84 / 2.92 / 3.28 | 4.31 / 3.07 / 2.78 |
| Transportation | 1.53 / 1.65 / 2.03 | 1.38 / 1.46 / 0.92 |
| ALL | 3.24 / 3.24 / 4.00 | 6.58 / 6.23 / 4.84 |
<!-- AUTHORED REGION END -->