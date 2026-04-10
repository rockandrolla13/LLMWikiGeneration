---
title: "Self-Attention"
page_id: concepts/self-attention
page_type: concept
tags: [attention, neural-networks]
---

# Self-Attention

## Definition

Self-attention computes relationships between all positions in a sequence.

## Formula

`Attention(Q,K,V) = softmax(QK^T / sqrt(d)) * V`

## Sources

- [[attention-paper|Attention Is All You Need]]
- [[Ashish Vaswani]]

## Related

- [[transformers]]
- [[multi-head-attention]]
