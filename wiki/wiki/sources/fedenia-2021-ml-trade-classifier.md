---
title: "Machine Learning in the Corporate Bond Market: A New Classifier"
page_id: sources/fedenia-2021-ml-trade-classifier
page_type: source
created: 2026-04-26T02:00:00Z
updated: 2026-04-26T02:00:00Z
tags: [machine-learning, trade-classification, corporate-bonds, random-forest, TRACE, market-microstructure]
authors: [Mark Fedenia, Tavy Ronen, Seunghan Nam]
year: 2021
journal: SSRN Working Paper
institution: [University of Wisconsin-Madison, Rutgers Business School, New York Institute of Technology]
related: [concepts/trade-classification, concepts/random-forest, concepts/trace-data, concepts/market-microstructure-noise]
---

# Machine Learning in the Corporate Bond Market: A New Classifier

## Summary

Develops a Random Forest-based trade classification algorithm for corporate bonds using TRACE signed trade data. The ML classifier outperforms traditional methods (Tick Rule, Lee-Ready) in both bond and equity markets, with improvements of up to 8.3% accuracy over the Tick Rule.

## Key Findings

- **RF Superiority**: Random Forest outperforms traditional classifiers (Tick Rule, Lee-Ready, BVC)
- **Feature Importance**: Trading and information environment critically affect classification accuracy
- **Cross-Market Application**: Model trained on bonds also works well in equity markets
- **Liquidity Effect**: Accuracy tends to be better in more liquid bonds

## Methodology

- Uses TRACE Enhanced Historical Data with buy/sell indicators
- Compares Random Forest, decision trees, and traditional classifiers
- Tests across 17.5 years of corporate bond data
- Examines accuracy around earnings announcements

## Key Results

| Classifier | Accuracy Improvement |
|-----------|---------------------|
| RF vs Tick Rule (bonds) | +8.3% |
| RF vs Tick Rule (equities) | +3.3% |
| RF vs Lee-Ready (equities) | +3.6% |

## Trading Environment Effects

- Higher accuracy in more liquid bonds
- Trade frequency positively related to accuracy
- Smaller trades have higher classification accuracy
- Information events (earnings) slightly degrade accuracy

## Key Concepts

- [[concepts/trade-classification|Trade Classification]]
- [[concepts/random-forest|Random Forest]]
- [[concepts/trace-data|TRACE Data]]
- [[concepts/market-microstructure-noise|Market Microstructure]]

## Implications

1. ML can improve trade signing accuracy with historical signed data
2. Feature selection crucial for classification performance
3. Model generalizes across asset classes
4. Traditional rules (TR, LR) have limitations in modern markets

## Related Sources

- [[sources/dickerson-2024-bond-pitfalls|Dickerson et al. (2024)]] - microstructure issues in bond research
- [[sources/houweling-2017-factor-investing|Houweling & van Zundert (2017)]] - bond factor investing
