---
authors:
- Peter Carr
- Liuren Wu
content_hash: sha256:83e25b37c3caabf9e323e080586d68d6788b39a77dadac9a0c497be68194ce30
created: '2026-10-05T15:52:32Z'
page_id: sources/carr-2011-american-puts-credit-protection
page_type: source
publication_date: '2011'
publication_venue: Review of Financial Studies 24(2)
related:
- concepts/capital-structure-arbitrage
- concepts/credit-default-swaps
- concepts/credit-default-swap-spread
- concepts/option-implied-credit-information
- concepts/merton-model
- concepts/structural-models
- concepts/reduced-form-credit-models
- concepts/jump-diffusion-option-pricing
- concepts/implied-volatility-skew
- concepts/no-arbitrage-restrictions
- concepts/error-correction-model
- concepts/unit-recovery-claim
- sources/kapadia-2012-limited-arbitrage-equity-credit
- sources/avino-2024-hedging-credit-equity-options
- sources/shi-2022-cds-options-comovement
- sources/amadori-2014-relative-informational-efficiency
- sources/dafonseca-2020-cds-equity-volatility-comovement
- analyses/capital-structure-arbitrage-literature-review
- entities/peter-carr
- entities/liuren-wu
revision_id: 1
schema_version: 2
source_hash: sha256:d56b21cf6fe9d251270ac3bd5688c82570155fb57ec154cfab68b7fc5e334a05
source_path: markdown_output/carr-2011-american-puts-credit-protection.md
source_type: paper
sources: []
tags:
- capital-structure-arbitrage
- cds
- deep-out-of-the-money-puts
- american-options
- default-corridor
- unit-recovery-claim
- equity-credit-linkage
- information-flow
title: A Simple Robust Link Between American Puts and Credit Protection
updated: '2026-10-05T15:52:32Z'
updated_by: op_225eb9cd3c09
uuid: f14560c8-e453-522a-8ab5-b8605f7c1476
version_read: 'Author copy of the published RFS article (manifest version: ''author
  copy''); text matches the journal typeset pages 474-500.'
year: 2011
---

<!-- AUTHORED REGION START -->
# A Simple Robust Link Between American Puts and Credit Protection

**Authors:** Peter Carr, Liuren Wu · **Year:** 2011 · **Venue:** Review of Financial Studies 24(2)
**Version read:** Author copy of the published RFS article (manifest version: 'author copy'); text matches the journal typeset pages 474-500.

## Summary

The paper links deep out-of-the-money American puts on a stock to credit protection on the same firm. The key assumption is a 'default corridor'. Before default the stock stays above a barrier B. At default it jumps below a lower barrier A, and stays there. So the stock never sits between A and B.

If such a corridor exists, a put struck inside it is never exercised before default and is exercised right at default. A spread of two same-expiry American puts struck inside the corridor, scaled by the strike gap, therefore pays one dollar at default if default happens before expiry, and nothing otherwise. The authors call this target claim a unit recovery claim (URC). The replication does not depend on how the stock, interest rates or default intensity move. If the stock goes to zero at default, one put divided by its strike is enough.

Empirically, they estimate the URC value two ways for 121 US firms over 186 weeks (2005-2008): from a single low-strike, low-delta long-dated put, and from the five-year CDS spread under flat-hazard and 40% recovery assumptions. The two estimates have similar size and move together. Once measurement error in both is allowed for, the slope between them is not distinguishable from one. Puts were on average cheaper than CDS before mid-2007, a gap that faded once the crisis began.

Gaps between the two estimates are partly tied to put delta, volatility, leverage and a Merton default probability. More importantly, the gaps predict future moves in both markets toward each other: the put-implied value falls back and the CDS-implied value rises. The authors read this as two-way information flow. A final section shows the corridor can come from a reduced-form 'defaultable displaced diffusion' stock model or from a structural model with an American-style bankruptcy put.

## Data

- Firms: 121 US companies with both qualifying puts and five-year CDS quotes (after filters, from 452 candidate firms, 152 with a CDS ticker).
- Period: weekly Wednesday reference dates, Feb 2005 to Aug 2008 (186 usable weeks); daily data in a 60-trading-day window around each reference date (30 days before for control regressions, 30 after for forecasting).
- Options: OptionMetrics American puts; filters: bid > 0, open interest > 0, maturity > 360 days, strike $5 or less, |delta| at most 15%; highest open interest chosen. Final 5,276 contracts (strikes mostly $2.5 and $5; maturities 360-955 days, mean 568).
- CDS: five-year spreads from Bloomberg; URC from CDS must be at least 3%, URC from put below one.
- Rates: USD LIBOR and swap rates from Bloomberg, stripped to a continuously compounded zero curve.
- Controls: put implied vol, one-year 50-delta put implied vol, 30- and 360-day realized variance, book debt/book equity, book debt/market cap, a Merton default probability, open interest.

## Method

Theory: with constant rate r and default intensity \lambda, the URC value is
$$U(t,T)=E^Q_t[e^{-r\tau}1(\tau<T)]=\lambda\frac{1-e^{-(r+\lambda)(T-t)}}{r+\lambda}.$$
Inside the corridor, the URC is replicated by a scaled put spread
$$U^p(t,T)=\frac{P_t(K_2,T)-P_t(K_1,T)}{K_2-K_1},\quad A\le K_1<K_2\le B,$$
which reduces to U^p = P_t(K,T)/K when A = 0. From CDS, with fixed bond recovery R^b, flat hazard and k = \lambda(1-R^b),
$$U^c(t,T)=\xi k_t\frac{1-e^{-(r(t,T)+\xi k_t)(T-t)}}{r(t,T)+\xi k_t},\quad \xi=1/(1-R^b),$$
with R^b = 40%.

Empirics: (1) OLS and Deming / total least squares regressions of U^p on U^c and back, with equal error variances; (2) pooled regressions of the gap (level and log) on one characteristic at a time plus date dummies; (3) an error-correction style test: for each contract, regress the gap D_t = U^p_t - U^c_t on a control over the past 30 days, take the residual, and use it to predict 7-day and 30-day changes in U^p and U^c separately (\Delta U^j_{t+\Delta t} = \alpha^j + \beta^j \tilde D_t + e). A negative \beta^p and positive \beta^c mean both markets move toward each other.

Theory extensions: a defaultable displaced diffusion (DDD) model combining Merton (1976) jump-to-default with Rubinstein (1983) displaced diffusion, which produces a volatility smile and a corridor; and a structural model where equity is a cancelable American call on firm value and debt equals par minus an American bankruptcy put.

## Key Findings

1. The put-implied and CDS-implied URC values have similar size (means of 0.111 and 0.127) and a cross-correlation of about 70%.
2. OLS slopes between the two estimates are below one (0.727 and 0.681), consistent with measurement error in both; total least squares slopes (1.047 and 0.955) are not significantly different from one.
3. Puts were on average cheaper than CDS: the gap U^p - U^c averaged -1.56% (median -2%, std 7.66%), and this bias largely disappeared after mid-2007.
4. A Merton-model default probability correlates more with the put-implied URC than the CDS-implied one (89.8% vs 61.9%), and the gap rises with it, hinting puts carry extra credit information.
5. The demeaned cross-market gap predicts the next 7 days' changes in both markets: slope -0.122 for the put-implied value and +0.138 for the CDS-implied value, i.e. convergence from both sides.
6. At 30 days the CDS-side predictability gets stronger (slope 0.274 with demeaned gap) while the put-side weakens, across all control variables.
7. The sample is 5,276 put-CDS pairs on 121 firms over 186 weekly dates, with 1,622 puts struck at $2.5 and 3,635 at $5.

## Limitations

The empirical test sets the lower barrier to zero and uses one put, so any positive equity recovery biases the put-implied URC down. A strike may sit above the corridor, letting diffusion and delta leak in. The CDS side assumes a fixed 40% recovery and a flat curve, and uses five-year CDS against puts of 360-955 days, so maturity mismatch matters. CDS also pays on credit events (e.g. distressed exchanges) that may not push the stock through the corridor. Bailout expectations for 'too big to fail' firms break the link. Option tick size and the non-zero bid filter overstate small default probabilities, hence the 3% floor. The paper says how to trade deviations is left for future work.

## Questions Raised

- Does the put-minus-CDS URC gap still predict CDS and bond spread changes after the 2009 CDS standardisation and in the post-2010 sample?
- How should the put strike be chosen to sit inside the corridor in practice, and can the corridor be detected from linearity of put prices in strike?
- Does the URC gap predict corporate bond excess returns, not just CDS changes?
- How much of the pre-crisis 'cheap puts' bias is a risk premium versus market segmentation?

## Relevance to Bond Signals

The put-implied URC is a model-light, equity-option-based default price that can be set against CDS or bond-implied default values; the paper shows the gap mean-reverts and leads CDS moves by up to 30 days. A firm-level 'DOOM put minus CDS' gap is a candidate lead signal for credit spread changes on names with listed long-dated low-strike puts.

See [[analyses/capital-structure-arbitrage-literature-review|Capital Structure Arbitrage: Literature Review for Bond Signals]].

## Concepts

- [[concepts/capital-structure-arbitrage|Capital Structure Arbitrage]]
- [[concepts/credit-default-swaps|Credit Default Swaps]]
- [[concepts/credit-default-swap-spread|Credit Default Swap Spread]]
- [[concepts/option-implied-credit-information|Option-Implied Information in Credit Markets]]
- [[concepts/merton-model|Merton Structural Model]]
- [[concepts/structural-models|Structural Models]]
- [[concepts/reduced-form-credit-models|Reduced-Form Credit Models]]
- [[concepts/jump-diffusion-option-pricing|Jump-Diffusion Option Pricing]]
- [[concepts/implied-volatility-skew|Implied Volatility Skew]]
- [[concepts/no-arbitrage-restrictions|No-Arbitrage Restrictions]]
- [[concepts/error-correction-model|Error Correction Model]]
- [[concepts/unit-recovery-claim|Unit Recovery Claim]]

## Entities

- [[entities/peter-carr|Peter Carr]]
- [[entities/liuren-wu|Liuren Wu]]

## Related Sources

- [[sources/kapadia-2012-limited-arbitrage-equity-credit|Limited arbitrage between equity and credit markets]]
- [[sources/avino-2024-hedging-credit-equity-options|Contingent Claims and Hedging of Credit Risk with Equity Options]]
- [[sources/shi-2022-cds-options-comovement|Market Co-movement Between Credit Default Swap Curves and Option Volatility Surfaces]]
- [[sources/amadori-2014-relative-informational-efficiency|The Relative Informational Efficiency of Stocks, Options and Credit Default Swaps During the Financial Crisis]]
- [[sources/dafonseca-2020-cds-equity-volatility-comovement|The Co-Movement of Credit Default Swap Spreads, Equity Returns and Volatility: Evidence from Asia-Pacific Markets]]
<!-- AUTHORED REGION END -->