---
title: "Momentum Spillover from Stocks to Corporate Bonds"
page_id: sources/haesen-2017-momentum-spillover
page_type: source
created: 2026-04-26T02:00:00Z
updated: 2026-04-26T02:00:00Z
tags: [momentum, corporate-bonds, spillover-effect, residual-momentum, default-risk, time-varying-risk]
authors: [Daniel Haesen, Patrick Houweling, Jeroen van Zundert]
year: 2017
journal: Journal of Banking and Finance
institution: Robeco
related: [concepts/bond-momentum, concepts/spillover-effect, concepts/residual-momentum, entities/patrick-houweling, entities/jeroen-van-zundert]
---

# Momentum Spillover from Stocks to Corporate Bonds

## Summary

Investigates and improves momentum spillover from stocks to corporate bonds - the phenomenon that past equity winners become future bond winners. Finds that ranking companies on residual (firm-specific) equity returns rather than total returns halves volatility, doubles Sharpe ratio, and substantially reduces drawdowns.

## Key Findings

- **Spillover Exists in HY**: First to document momentum spillover effect in high-yield bonds
- **Default Risk Exposure**: Winner-minus-loser portfolio has strong structural default risk exposure
- **Time-Varying Risk**: Default risk exposure depends on equity market return during formation period
- **Residual Momentum Superior**: Using idiosyncratic equity returns dramatically improves performance

## Performance Comparison

| Metric | Total Momentum | Residual Momentum |
|--------|---------------|-------------------|
| Volatility | 8.85% | 4.80% |
| Sharpe Ratio | 0.35 | 0.77 |
| Worst Drawdown | -80% | -25% |

## Key Mechanisms

1. **Structural Risk**: Winners have lower default risk than losers at portfolio formation
2. **Time-Varying Risk**: Negative equity markets → smaller default risk exposure → hurt in credit bull markets
3. **2009 Example**: -80% drawdown when equity bear followed by credit bull
4. **Risk Factors Explain 44%**: Structural and time-varying exposures explain variation in profitability

## Methodology

- Barclays US Corporate IG and HY indexes (Jan 1994 - Dec 2013)
- Excess returns over duration-matched Treasuries
- Residual returns from Fama-French equity factor model
- Various hedging methods compared

## Key Concepts

- [[concepts/bond-momentum|Bond Momentum]]
- [[concepts/spillover-effect|Spillover Effect]]
- [[concepts/residual-momentum|Residual Momentum]]
- [[concepts/time-varying-risk|Time-Varying Risk]]

## Implications

1. Equity information relevant for bond returns
2. Simple total return momentum has significant risk exposures
3. Firm-specific (residual) signals more robust
4. Ex-post hedging less effective than residual approach

## Related Sources

- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] - factor investing framework
- [[sources/jostova-2013-momentum|Jostova et al. (2013)]] - momentum in high-yield bonds
