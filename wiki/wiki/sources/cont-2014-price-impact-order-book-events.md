---
authors:
- Rama Cont
- Arseniy Kukanov
- Sasha Stoikov
content_hash: sha256:69fb9056ea4e98e8eab40e80590b9107e0632142078985ad43ba4475bd5fc05a
created: 2026-09-25 21:37:03+00:00
page_id: sources/cont-2014-price-impact-order-book-events
page_type: source
related:
- concepts/order-flow-imbalance
- concepts/order-imbalance
- concepts/price-impact
- concepts/square-root-law
- concepts/limit-order-book
- concepts/market-microstructure
- entities/rama-cont
- entities/arseniy-kukanov
- entities/sasha-stoikov
- sources/cont-2023-cross-impact-ofi
- sources/xu-2020-mlofi
- sources/sitaru-2023-decomposed-ofi
- sources/su-2021-generalized-ofi
- sources/hu-2025-ofi-csi300-ou
revision_id: 1
schema_version: 2
source_hash: sha256:9a1631620b3f2c647cbcad6ec5e864d1a5883c0b1230d0ffa7dca76163d17e23
source_path: markdown_output/cont-2014-price-impact-order-book-events.md
tags:
- order-flow-imbalance
- price-impact
- limit-order-book
- market-microstructure
- market-depth
- trade-imbalance
- taq-data
- intraday-seasonality
title: The Price Impact of Order Book Events
updated: '2026-09-25T21:37:03Z'
uuid: dbebb3a1-1879-5d7b-8eca-e3d9f1a51510
year: 2014
---

<!-- AUTHORED REGION START -->
# The Price Impact of Order Book Events

## Summary

The paper that defines [[concepts/order-flow-imbalance|order flow imbalance]]. Its claim is that the price impact of every order book event — limit order, market order, cancellation — can be collapsed into one variable, the net change in the bid and ask queues, and that mid-price changes over short intervals are a *linear* function of that variable. On 50 randomly chosen S&P 500 stocks the relation has an average $R^2$ of 65% at a ten-second horizon, needs one parameter, and holds across stocks and time scales. That parameter, the price impact coefficient, is inversely proportional to the depth at the best quotes, which is what makes intraday patterns in impact and volatility explainable from observable quantities rather than from information asymmetry.

Two further results follow from the same model. Trade imbalance, the variable most of the prior literature used, explains only 32% of the same variation and becomes insignificant once OFI is in the regression. And the widely reported concave "square-root" relation between price changes and traded volume is derived as a statistical artefact of aggregation: if prices follow OFI linearly, a noisy square-root dependence on volume appears anyway.

The text ingested here is the arXiv preprint (v3, April 2011); the paper was later published in the *Journal of Financial Econometrics* in 2014, which is the year the rest of this wiki cites.

## The Construction

Only the best bid and ask are used. Each observation $n$ of the book is a quadruple: bid price $P^B_n$, bid size $q^B_n$, ask price $P^A_n$, ask size $q^A_n$. The contribution $e_n$ of the event between observations $n-1$ and $n$ is assigned by four rules on the bid side, with signs reversed on the ask side:

- bid price unchanged, bid size grows: $e_n$ is the size added;
- bid price unchanged, bid size shrinks: $e_n$ is the size removed, whether by a market sell or a cancelled buy;
- bid price rises: $e_n$ is the full size $q^B_n$ of the price-improving order;
- bid price falls: $e_n$ is the full size $q^B_{n-1}$ that was removed.

Written compactly, these rules are

$$e_n = \mathbb{1}_{\{P^B_n \ge P^B_{n-1}\}}\, q^B_n - \mathbb{1}_{\{P^B_n \le P^B_{n-1}\}}\, q^B_{n-1} - \mathbb{1}_{\{P^A_n \le P^A_{n-1}\}}\, q^A_n + \mathbb{1}_{\{P^A_n \ge P^A_{n-1}\}}\, q^A_{n-1}.$$

The variable rises whenever demand increases or supply decreases, and falls in the opposite cases. A consequence the authors flag as interesting: a market sell and a cancelled buy of the same size are treated identically, because both shrink the bid queue by the same amount.

OFI over a grid interval $[t_{k-1}, t_k]$ is the sum of the $e_n$ for every event in that interval:

$$\text{OFI}_k = \sum_{n = N(t_{k-1})+1}^{N(t_k)} e_n,$$

where $N(t)$ counts events up to $t$. Mid-price changes $\Delta P_k$ over the same grid are measured in ticks. Unlike the trade-imbalance measures of earlier work, OFI includes cancellations, which Hopman's earlier supply/demand imbalance did not.

## The Stylised Model and the Depth Relation

Suppose every price level beyond the best has the same depth $D$, and limit orders and cancellations arrive only at the best quotes. Then the effect of events on each side of the book is additive and depends only on the net change in queue size. Averaging bid and ask gives, up to truncation,

$$\Delta P_k \approx \frac{\text{OFI}_k}{2D},$$

with no free parameters. Real books have uneven depth, activity at deeper levels, intraday variation and hidden orders, so the working specification is statistical:

$$\Delta P_k = \beta_i\, \text{OFI}_k + \epsilon_k, \qquad \beta_i = \frac{c}{AD_i^{\lambda}} + \nu_i,$$

where $\beta_i$ is the **price impact coefficient** in half-hour window $i$, $AD_i$ is the average of the bid and ask queue sizes over that window, and the stylised model corresponds to $\lambda = 1$ and $c = 1/2$.

The model is one of *instantaneous* impact. An order that reinforces the concurrent imbalance moves the price; one that goes against it is absorbed by the other orders in the same interval and may have zero realised impact. All event types, trades included, have the same average impact $\beta$.

## Data

One month, April 2010, of NYSE TAQ consolidated quotes and trades for 50 stocks drawn at random from the S&P 500, obtained through WRDS. TAQ is Level 1: it records every change to the best bid and ask but nothing deeper. The authors chose it deliberately over Level 2 data because it is far more accessible and still carries every event at the touch, and they note that quote updates outnumber trades by about 40 to 1.

Quotes from all exchanges are aggregated into an NBBO, with sizes summed across venues at the best price. Trades are signed by a quote test: a trade at or above the NBBO ask within one second of the quote is a buy, at or below the bid a sell. The tick test and the Lee–Ready rule give virtually the same results. The 5% of each stock's quotes with the widest spreads are removed.

The base grid is $\Delta t = 10$ seconds. Each stock yields 273 half-hour subsamples of about 180 observations, and every regression is run per subsample and averaged. Repeating the work at grids from ten quote updates (under half a second) to ten minutes raises the fit as the interval lengthens and changes nothing else.

## Results

**The linear fit.** Across the 50 stocks the average $R^2$ is 65%, and $\beta_i$ passes a 5% z-test with White standard errors in 97% of subsamples while the intercept is mostly insignificant. Residual kurtosis is low, so the misses are not concentrated in large moves. Adding a quadratic term $\text{OFI}_k |\text{OFI}_k|$ raises $R^2$ from 65% to 68% and the term is insignificant in most samples. There is no evidence of nonlinearity at this horizon.

A tautology worry is addressed directly: OFI includes the price-changing events themselves. Removing those events from OFI on a subsample of stocks lowers $R^2$ but leaves it in the 35%–60% range.

**Impact is inverse to depth.** A log-linear regression of $\hat\beta_i$ on $AD_i$ gives $\hat\lambda$ close to 1 across stocks, and $\lambda = 1$ cannot be rejected for 35 of the 50. The constant $c$ does have to be calibrated and is generally below the stylised $1/2$, meaning mid-prices are more resilient than the best-quote depth alone implies. Three stocks fit badly (APOL, AZO, CME); all three have wide spreads and thin best-quote depth, where hidden orders and deeper levels presumably dominate. Newey–West errors are used here because the residuals are autocorrelated.

**Intraday seasonality is explained by depth.** Depth near the open is about half its daily average, so the impact coefficient is about twice its average at the open and roughly five times higher at the open than at the close. Taking the variance of the model gives $\text{var}[\Delta P_k]_i \approx \beta_i^2\, \text{var}[\text{OFI}_k]_i$, and the two sides match on the data. Price volatility peaks at the open; OFI volatility peaks near the close, but that peak is offset by low impact. The authors read this as a reconciliation with the information-asymmetry accounts of Madhavan et al. and Hasbrouck: limit order traders who fear being picked off in the morning post less depth, low depth means high impact, and so the two stories are two sides of one coin.

## Trade Imbalance Versus Order Flow Imbalance

Trade imbalance $TI_k$ is buy volume minus sell volume over the interval. Alone it explains 32% of ten-second mid-price variation against 65% for OFI. In a joint regression the OFI coefficient stays strong while the trade-imbalance t-statistic falls by a factor of four and is significant in only 31% of subsamples. The conclusion is that the effect of trades is already inside OFI, which is the more general measure.

A robustness check in trade time, on transaction prices over $L = 2, 5, 10$ trades for five stocks, gives the same ranking: $R^2$ of 14%, 38% and 51% for OFI against 1%, 8% and 13% for trade imbalance. Here, though, the fits are concave in some samples, with a quadratic term significant in about half of them. The authors attribute this to sampling at trade times, when traders may be choosing moments of low expected impact.

## Volume and the Square Root

Proposition 1 makes the square-root price–volume relation a consequence of the linear model. If events arrive at a steady average rate, contributions $e_i$ are i.i.d. with finite variance $\sigma^2$, and trade sizes are i.i.d. with mean $\mu$ and a fraction $\pi$ of events are trades, then the law of large numbers pins volume to $N(T)\mu\pi$ while the central limit theorem makes OFI of order $\sigma\sqrt{N(T)}$. Together:

$$\text{OFI}(T) \approx \xi\, \sigma \sqrt{\frac{\text{VOL}(T)}{\mu \pi}}, \qquad \xi \sim N(0,1).$$

Substituting into the price model gives $\Delta P_k \approx \theta_k \sqrt{\text{VOL}_k}$, where the slope $\theta_k$ is a fresh normal draw in every interval. So the square root appears even when $\epsilon_k = 0$ and prices are driven entirely by OFI. Its slope is random, which is why the authors call the relation noisy and do not recommend using it. If the assumptions fail — dependent or heavy-tailed $e_i$ — the exponent changes, which they offer as a reading of the range of exponents $0 < H < 1$ reported by Bouchaud, Farmer and Lillo.

Empirically, exponents estimated per subsample are generally below one half and vary widely. Regressing $|\Delta P_k|$ on $|\text{OFI}_k|$, on $\text{VOL}_k^{\hat H_i}$, and on both gives average $R^2$ of 58%, 23% and 61%; only $|\text{OFI}_k|$ stays significant in the joint regression, and the number of trades, significant alone, also drops out. The price–volume relation is indirect: volume is correlated with $|\text{OFI}|$, and $|\text{OFI}|$ is what moves prices.

## Limitations

- Best quotes only. Depth beyond the touch enters as noise, and the three worst-fitting stocks are the ones where that noise is largest. [[sources/xu-2020-mlofi|Xu, Gould & Howison]] later show that deeper levels matter, especially for small-tick stocks, once ridge regression controls the collinearity.
- TAQ timestamps are rounded to the second, and trade signing uses a one-second matching window. The ten-second grid is chosen partly to absorb these errors.
- One month of data. Robustness across time scales and stocks is shown; robustness across years and regimes is not.
- The model is contemporaneous. Nothing here is a forecast, and the $R^2$ figures should not be compared with the forecasting $R^2$ of later OFI papers, which are routinely negative. See [[concepts/price-impact]].
- The square-root argument concerns the price–volume relation at fixed clock intervals, not the impact of a metaorder against its executed size. The two are different objects; see [[concepts/square-root-law]].

## Relation to Later Work

Every later page in this cluster extends one part of this construction. [[sources/xu-2020-mlofi|Xu, Gould & Howison (2020)]] add book depth; [[sources/cont-2023-cross-impact-ofi|Cont, Cucuringu & Zhang (2023)]] compress the multi-level vector to a scalar and add cross-asset terms; [[sources/sitaru-2023-decomposed-ofi|Sitaru, Calinescu & Cucuringu (2023)]] split OFI by event type, which the equal-impact assumption here explicitly averages over; [[sources/su-2021-generalized-ofi|Su et al. (2021)]] drop the implicit one-tick-per-observation assumption; [[sources/hu-2025-ofi-csi300-ou|Hu & Zhang (2025)]] model the response to an OFI shock over time rather than within a fixed interval. The event-contribution rules and the depth scaling are still the base of all of them.

## Citation

Cont, R., Kukanov, A., & Stoikov, S. (2014). The price impact of order book events. *Journal of Financial Econometrics*, 12(1), 47–88. Preprint: arXiv:1011.6402 (v3, April 2011), which is the text ingested here.
<!-- AUTHORED REGION END -->
