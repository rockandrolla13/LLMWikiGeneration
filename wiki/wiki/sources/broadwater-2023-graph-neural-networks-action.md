---
title: "Graph Neural Networks in Action"
page_id: sources/broadwater-2023-graph-neural-networks-action
page_type: source
revision_id: 1
created: 2026-06-19T00:00:00Z
updated: 2026-06-19T00:00:00Z
updated_by: batch_ingest_technical_books_2_2026_06_19
tags: [graph-neural-networks, gnn, pytorch-geometric, deep-learning, graph-machine-learning, node-embeddings, graph-convolutional-networks, graph-attention-networks, spatiotemporal, drug-discovery, fraud-detection, recommendation-systems, manning, practitioner-book, 2023]
sources: [sources/broadwater-2023-graph-neural-networks-action]
related: []
mind_map_priority: high
authors: ["Keita Broadwater", "Namid Stillman"]
year: 2023
source_type: book
---

# Graph Neural Networks in Action

**Authors:** Keita Broadwater, Namid Stillman  
**Year:** 2023  
**Type:** book  
**Markdown source:** `markdown_output/broadwater-2023-graph-neural-networks-action.md`

## Summary

Graph Neural Networks in Action (Manning, 2025 copyright; ISBN 9781617299056) by Keita Broadwater and Namid Stillman, with foreword by Matthias Fey (creator of PyTorch Geometric), is a practitioner-oriented guide to building GNN applications. The book covers the full GNN project pipeline — from raw data through graph data modeling, embeddings, model training, and scaling — using PyTorch Geometric as the primary implementation framework. It is structured in three parts: First Steps (graph fundamentals and embeddings), Graph Neural Networks (GCN/GraphSAGE, GAT, graph autoencoders), and Advanced Topics (spatiotemporal/dynamic graphs, scaling, and project considerations). Two appendices cover graph theory fundamentals and PyTorch Geometric installation. The book was authored out of a felt need for a single, accessible, non-academic resource that fills gaps left by scattered online tutorials, particularly for practitioners at companies without large ML research teams.

## Key Claims

- GNNs revolutionize graph machine learning by learning representations from raw graph data without handcrafted feature engineering (Matthias Fey foreword)
- The GNN project pipeline mirrors conventional ML pipelines but requires graph-specific tools for data modeling, storage, exploration, and preprocessing
- Real-world adoption of GNNs remains limited to resource-rich organizations due to a knowledge gap the book aims to close
- Node2Vec and GNN-based embeddings are contrasted as two approaches to generating graph node representations
- Graph attention networks (GAT) can address oversmoothing and class imbalance challenges faced by simpler GCN baselines
- Variational graph autoencoders (VGAEs) can be used to generate novel molecular graphs for drug discovery
- Dynamic/spatiotemporal GNNs combine recurrent architectures (GRU, RNNs) with graph attention to model relations through time
- Scaling GNNs requires a multi-faceted approach: hardware choice, data representation, algorithm selection, mini-batching/sampling, distributed processing, remote storage, and graph coarsening

## Main Concepts

- [[concepts/graph-neural-networks-gnns-|Graph Neural Networks (GNNs)]]
- [[concepts/graph-embeddings|Graph embeddings]]
- [[concepts/node2vec|Node2Vec]]
- [[concepts/message-passing|Message passing]]
- [[concepts/graph-convolutional-networks-gcn-|Graph Convolutional Networks (GCN)]]
- [[concepts/graphsage|GraphSAGE]]
- [[concepts/neighborhood-aggregation|Neighborhood aggregation]]
- [[concepts/graph-attention-networks-gat-|Graph Attention Networks (GAT)]]
- [[concepts/oversmoothing|Oversmoothing]]
- [[concepts/graph-autoencoders|Graph autoencoders]]
- [[concepts/variational-graph-autoencoders-vgae-|Variational graph autoencoders (VGAE)]]
- [[concepts/link-prediction|Link prediction]]
- [[concepts/spatiotemporal-gnns|Spatiotemporal GNNs]]
- [[concepts/dynamic-graphs|Dynamic graphs]]
- [[concepts/neural-relational-inference-nri-|Neural Relational Inference (NRI)]]
- [[concepts/gumbel-softmax|Gumbel-Softmax]]
- [[concepts/temporal-adjacency-matrices|Temporal adjacency matrices]]
- [[concepts/mini-batching-and-sampling-for-large-graphs|Mini-batching and sampling for large graphs]]
- [[concepts/distributed-data-parallel-ddp-|Distributed data parallel (DDP)]]
- [[concepts/graph-coarsening|Graph coarsening]]
- [[concepts/transductive-vs-inductive-learning|Transductive vs. inductive learning]]
- [[concepts/spectral-vs-spatial-convolution|Spectral vs. spatial convolution]]
- [[concepts/node-features-and-edge-features|Node features and edge features]]
- [[concepts/graph-data-pipeline-etl-preprocessing-|Graph data pipeline (ETL, preprocessing)]]
- [[concepts/recommendation-engines|Recommendation engines]]
- [[concepts/drug-discovery-molecular-graphs|Drug discovery / molecular graphs]]
- [[concepts/fraud-spam-detection|Fraud/spam detection]]

## Key Entities

- [[entities/keita-broadwater-author-former-cloudera-fast-forward-labs-|Keita Broadwater (author; former Cloudera/Fast Forward Labs)]]
- [[entities/namid-stillman-co-author-|Namid Stillman (co-author)]]
- [[entities/matthias-fey-foreword-author-creator-of-pytorch-geometric-founding-engineer-at-kumo-ai-|Matthias Fey (foreword author; creator of PyTorch Geometric; founding engineer at Kumo.AI)]]
- [[entities/manning-publications-publisher-|Manning Publications (publisher)]]
- [[entities/pytorch-geometric-pyg-primary-implementation-framework-|PyTorch Geometric (PyG) (primary implementation framework)]]
- [[entities/cloudera-employer-where-broadwater-first-encountered-gnns-|Cloudera (employer where Broadwater first encountered GNNs)]]
- [[entities/fast-forward-labs-team-where-book-concept-originated-|Fast Forward Labs (team where book concept originated)]]
- [[entities/linkedin-inspiration-for-network-visualization-in-preface-|LinkedIn (inspiration for network visualization in preface)]]
- [[entities/kumo-ai-matthias-fey-s-company-|Kumo.AI (Matthias Fey's company)]]
- [[entities/amazon-products-dataset-used-in-chapters-3-5-7-|Amazon Products dataset (used in chapters 3, 5, 7)]]
- [[entities/geogrid-dataset-used-in-chapter-7-|GeoGrid dataset (used in chapter 7)]]
- [[entities/frances-lefkowitz-development-editor-|Frances Lefkowitz (development editor)]]
- [[entities/frances-buontempo-technical-development-editor-|Frances Buontempo (technical development editor)]]

## Questions Raised

- Which specific versions of PyTorch Geometric are covered/supported?
- How does the book handle heterogeneous graphs (multiple node/edge types)?
- What is the GeoGrid dataset and what task does it represent?
- Does the book cover graph transformer architectures introduced after 2022?
- How does performance of GAT compare to XGBoost on the fraud detection task (quantitative results)?
- What graph databases are discussed in the data pipeline chapter (ch. 8)?
- Does the book address graph-level (as opposed to node-level) classification tasks?
- What hardware benchmarks or recommendations are given in the scaling chapter?
