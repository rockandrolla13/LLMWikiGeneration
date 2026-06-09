---
authors:
- Vineer Bhansali
created: '2026-06-09T12:00:00Z'
mind_map_category: null
mind_map_priority: medium
page_id: sources/bhansali-2018-right-tail-hedging
page_type: source
publication_date: '2018'
publication_venue: The Journal of Portfolio Management
related:
- concepts/disposition-effect
- concepts/implied-volatility-skew
- concepts/jump-diffusion-option-pricing
- concepts/log-periodic-power-law
- concepts/right-tail-hedging
- concepts/short-volatility-strategies
- entities/didier-sornette
- entities/journal-of-portfolio-management
- entities/longtail-alpha
- entities/robert-merton
- entities/vineer-bhansali
revision_hash: sha256:26c5d217b66fe1f4f0d98913dd7ac3766e937a47aa1e999ce20553ff5f76537d
revision_id: 1
source_hash: sha256:69e9a81b6e615da3b2707c0005d58090a44eaa927a83e0a96c868696222aa270
source_path: raw/creditmacro/document.md
source_type: article
sources: []
tags:
- options
- tail-hedging
- volatility
- derivatives
- behavioral-finance
- jump-diffusion
title: 'Right Tail Hedging: Managing Risk When Markets Melt Up'
updated: '2026-06-09T12:00:00Z'
updated_by: op_2aa0f0b54fec
---

# Right Tail Hedging: Managing Risk When Markets Melt Up

**Authors:** Vineer Bhansali · **Year:** 2018 · **Venue:** The Journal of Portfolio Management · **Type:** article

## Summary

Bhansali argues that upside ('right tail') hedging using call options can be optimal for investors under certain market conditions, challenging the conventional conclusion that buying options is a negative-expected-return strategy. He notes that historical draw-ups in equity markets are at least as numerous and severe as drawdowns, yet downside protection dominates investor attention, producing an elevated implied-volatility skew that makes call options relatively cheap versus puts on a volatility-normalized basis. Using Merton's jump-diffusion framework he shows that pricing up-jumps materially raises call prices and gamma versus Black-Scholes, producing a 'spot up, vol up' effect and a destabilizing hedging feedback loop when up-jumps are mispriced. The paper also invokes Sornette's log-periodic power-law dynamics and the disposition effect (call options as a pre-commitment device).

## Key Claims

1. Historical draw-ups in equity markets are at least as numerous and severe as drawdowns, yet receive far less hedging attention.
2. The implied-volatility skew makes call options relatively cheap versus puts on a volatility-normalized basis, partly driven by collar and short-volatility strategies.
3. Most empirical studies concluding options are negative-expected-return strategies relied on samples lacking major market melt-ups.
4. Under Merton (1976) jump diffusion, pricing a single up-jump raises a one-year out-of-the-money call price by roughly 50%.
5. When volatility is low, the gamma of a jump-priced option greatly exceeds the Black-Scholes gamma, creating a destabilizing hedging feedback loop ('spot up, vol up').
6. Call options serve as a pre-commitment device that overcomes the disposition effect by capping loss at the premium while retaining upside.

## Questions Raised

- Are correlations during large positive equity moves actually lower than during downturns?
- How robust is the worked call example given the author acknowledges it is cherry-picked?
- Can the destabilizing upside hedging feedback loop be empirically distinguished from other drivers of melt-ups?

## Concepts

- [[concepts/right-tail-hedging|Right Tail Hedging]]
- [[concepts/implied-volatility-skew|Implied Volatility Skew]]
- [[concepts/jump-diffusion-option-pricing|Jump-Diffusion Option Pricing]]
- [[concepts/log-periodic-power-law|Log-Periodic Power Law Market Model]]
- [[concepts/disposition-effect|Disposition Effect]]
- [[concepts/short-volatility-strategies|Short Volatility Strategies]]

## Entities

- [[entities/vineer-bhansali|Vineer Bhansali]]
- [[entities/longtail-alpha|LongTail Alpha, LLC]]
- [[entities/journal-of-portfolio-management|The Journal of Portfolio Management]]
- [[entities/robert-merton|Robert C. Merton]]
- [[entities/didier-sornette|Didier Sornette]]

## Source

- **Path:** `raw/creditmacro/document.md`
- **Type:** article
- **Hash:** `sha256:69e9a81b6e615da3b...`