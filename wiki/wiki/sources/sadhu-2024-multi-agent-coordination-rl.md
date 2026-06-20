---
title: 'Multi-Agent Coordination: A Reinforcement Learning Approach'
page_id: sources/sadhu-2024-multi-agent-coordination-rl
page_type: source
revision_id: 1
created: 2026-06-19 00:00:00+00:00
updated: '2026-06-20T01:03:51Z'
updated_by: batch_ingest_5_2026_06_19
tags:
- multi-agent-reinforcement-learning
- q-learning
- cooperative-robotics
- path-planning
- nash-equilibrium
- correlated-equilibrium
- evolutionary-algorithms
- firefly-algorithm
- imperialist-competitive-algorithm
- game-theory
- jadavpur-university
- khepera-ii
- multi-robot-coordination
- trajectory-optimisation
- ieee-press
- wiley
sources:
- sources/sadhu-2024-multi-agent-coordination-rl
related: []
mind_map_priority: high
authors:
- Arup Kumar Sadhu
- Amit Konar
year: 2024
source_type: book
schema_version: 2
uuid: 34db0f01-a622-5ca2-9223-4de480d358f6
content_hash: sha256:c94864ea88721e8d18b5fc97e1fd4e53dbc9ef1deddf7762f722325f103b3818
---

<!-- AUTHORED REGION START -->
# Multi-Agent Coordination: A Reinforcement Learning Approach

**Authors:** Arup Kumar Sadhu, Amit Konar  
**Year:** 2024  
**Type:** book  
**Markdown source:** `markdown_output/sadhu-2024-multi-agent-coordination-rl.md`

## Summary

Book: "Multi-Agent Coordination: A Reinforcement Learning Approach" by Arup Kumar Sadhu and Amit Konar. Published 2021 by Wiley-IEEE Press (copyrighted 2021 John Wiley & Sons, Inc.; note: the filename says 2024 but the text gives 2021 as the publication year). The book develops multi-robot/multi-agent coordination algorithms grounded in multi-agent Q-learning (MAQL), game theory (Nash and correlated equilibria), and evolutionary/metaheuristic optimization. It addresses cooperative path planning in both simulated and real robotic environments (Khepera II robots), targeting the dual challenges of convergence speed and the curse of dimensionality in joint state-action spaces. A hybrid evolutionary algorithm (ICFA, fusing Imperialist Competitive Algorithm and Firefly Algorithm) is also proposed for trajectory optimisation in a stick-carrying task.

## Key Claims

- MAQL algorithms suffer from poor convergence speed and the curse of dimensionality as the number of agents grows.
- A team-goal exploration property (agents at their individual goal wait for remaining agents) accelerates convergence of TMAQL.
- A joint-action intersection property selects the preferred joint action for the team and speeds up MAQL convergence.
- Consensus Q-Learning (CoQL) resolves the suboptimal equilibrium selection problem by choosing a consensus that simultaneously satisfies pure-strategy Nash Equilibrium (NE) and pure-strategy Correlated Equilibrium (CE) conditions.
- A single shared Q-table approach (Chapter 4) reduces CE computation cost compared to traditional CQL, which requires consulting m separate Q-tables for m robots.
- The proposed ICFA (hybrid Imperialist Competitive Firefly Algorithm) outperforms state-of-the-art metaheuristics in multi-robot stick-carrying tasks in both accuracy and run-time complexity.
- The No Free Lunch Theorem motivates hybridisation of evolutionary algorithms with other optimisation strategies.
- Reinforcement learning eliminates the need for manually labelled training instances, making it suitable for dynamic multi-robot environments.

## Main Concepts

- [[concepts/multi-agent-reinforcement-learning-marl-|Multi-Agent Reinforcement Learning (MARL)]]
- [[concepts/multi-agent-q-learning-maql-|Multi-Agent Q-Learning (MAQL)]]
- [[concepts/nash-equilibrium-ne-pure-and-mixed-strategy|Nash Equilibrium (NE) — pure and mixed strategy]]
- [[concepts/correlated-equilibrium-ce-|Correlated Equilibrium (CE)]]
- [[concepts/consensus-q-learning-coql-|Consensus Q-Learning (CoQL)]]
- [[concepts/team-goal-exploration|Team-goal exploration]]
- [[concepts/joint-action-selection-joint-state-action-space|Joint action selection / joint state-action space]]
- [[concepts/exploration-vs-exploitation-greedy-boltzmann-strategy-|Exploration vs exploitation (greedy, Boltzmann strategy)]]
- [[concepts/cooperative-path-planning|Cooperative path planning]]
- [[concepts/competitive-and-mixed-coordination|Competitive and mixed coordination]]
- [[concepts/evolutionary-algorithms-ea-and-hybridisation|Evolutionary Algorithms (EA) and hybridisation]]
- [[concepts/imperialist-competitive-algorithm-ica-|Imperialist Competitive Algorithm (ICA)]]
- [[concepts/firefly-algorithm-fa-|Firefly Algorithm (FA)]]
- [[concepts/imperialist-competitive-firefly-algorithm-icfa-|Imperialist Competitive Firefly Algorithm (ICFA)]]
- [[concepts/no-free-lunch-theorem-nflt-|No Free Lunch Theorem (NFLT)]]
- [[concepts/dynamic-programming-dp-and-its-correlation-with-rl|Dynamic programming (DP) and its correlation with RL]]
- [[concepts/game-theory-static-and-stochastic-games-general-sum-games-|Game theory (static and stochastic games, general-sum games)]]
- [[concepts/single-agent-q-learning|Single-agent Q-learning]]
- [[concepts/nash-q-learning-nql-|Nash Q-Learning (NQL)]]
- [[concepts/friend-or-foe-q-learning-fql-|Friend-or-Foe Q-Learning (FQL)]]
- [[concepts/correlated-q-learning-cql-|Correlated Q-Learning (CQL)]]
- [[concepts/sparse-cooperative-q-learning|Sparse Cooperative Q-Learning]]
- [[concepts/trajectory-optimisation|Trajectory optimisation]]
- [[concepts/collision-avoidance|Collision avoidance]]
- [[concepts/khepera-ii-mobile-robots-hardware-platform-|Khepera II mobile robots (hardware platform)]]
- [[concepts/pheromone-based-ant-coordination-motivating-analogy-|Pheromone-based ant coordination (motivating analogy)]]
- [[concepts/dijkstra-s-algorithm-a-algorithm-d-algorithm|Dijkstra's algorithm, A* algorithm, D* algorithm]]

## Key Entities

- [[entities/arup-kumar-sadhu-first-author-phd-jadavpur-university-2017-scientist-at-tata-consultancy-services-|Arup Kumar Sadhu (first author; PhD Jadavpur University 2017; scientist at Tata Consultancy Services)]]
- [[entities/amit-konar-second-author-jadavpur-university-|Amit Konar (second author; Jadavpur University)]]
- [[entities/jadavpur-university-kolkata-india-artificial-intelligence-laboratory-and-control-engineering-laboratory-dept-of-electronics-and-telecommunication-engineering|Jadavpur University, Kolkata, India — Artificial Intelligence Laboratory and Control Engineering Laboratory, Dept. of Electronics and Telecommunication Engineering]]
- [[entities/tata-consultancy-services-tcs-research-innovation-labs|Tata Consultancy Services (TCS) — Research & Innovation Labs]]
- [[entities/wiley-ieee-press-john-wiley-sons-inc-publisher-|Wiley-IEEE Press / John Wiley & Sons, Inc. (publisher)]]
- [[entities/ieee-press-editorial-board-ekram-hossain-editor-in-chief-j-n-atli-benediktsson-david-alan-grier-elya-b-joffe-xiaoou-li-peter-lian-andreas-molisch-saeid-nahavandi-jeffrey-reed-diomidis-spinellis-sarah-spurgeon-ahmet-murat-tekalp|IEEE Press — Editorial Board: Ekram Hossain (Editor in Chief), Jón Atli Benediktsson, David Alan Grier, Elya B. Joffe, Xiaoou Li, Peter Lian, Andreas Molisch, Saeid Nahavandi, Jeffrey Reed, Diomidis Spinellis, Sarah Spurgeon, Ahmet Murat Tekalp]]
- [[entities/claus-and-boutilier-independent-learner-joint-action-learner-framework-|Claus and Boutilier (independent learner / joint action learner framework)]]
- [[entities/littman-team-q-learning-minimax-q-learning-friend-or-foe-q-learning-|Littman (Team Q-learning; Minimax Q-learning; Friend-or-Foe Q-Learning)]]
- [[entities/hu-and-wellman-nash-q-learning-for-general-sum-stochastic-games-|Hu and Wellman (Nash Q-learning for general-sum stochastic games)]]
- [[entities/greenwald-and-hall-correlated-q-learning-cql-|Greenwald and Hall (Correlated Q-Learning, CQL)]]
- [[entities/jelle-and-nikos-sparse-cooperative-q-learning-|Jelle and Nikos (Sparse Cooperative Q-Learning)]]
- [[entities/zinkevich-neural-network-approach-for-state-space-generalisation-in-marl-|Zinkevich (neural network approach for state-space generalisation in MARL)]]
- [[entities/reinaldo-et-al-heuristic-acceleration-of-tmaql-|Reinaldo et al. (heuristic acceleration of TMAQL)]]
- [[entities/hu-et-al-equilibrium-transfer-|Hu et al. (equilibrium transfer)]]
- [[entities/zhang-et-al-q-table-dimension-reduction-in-nql-|Zhang et al. (Q-table dimension reduction in NQL)]]
- [[entities/prof-surnajan-das-vice-chancellor-jadavpur-university-|Prof. Surnajan Das (vice-chancellor, Jadavpur University)]]
- [[entities/prof-chiranjib-bhattacharjee-pro-vice-chancellor-ju-|Prof. Chiranjib Bhattacharjee (pro-vice-chancellor, JU)]]
- [[entities/dr-pradip-kumar-ghosh-pro-vice-chancellor-ju-|Dr. Pradip Kumar Ghosh (pro-vice-chancellor, JU)]]
- [[entities/prof-sheli-sinha-chaudhuri-hod-etce-ju-|Prof. Sheli Sinha Chaudhuri (HoD, ETCE, JU)]]
- [[entities/khepera-ii-mobile-robot-hardware-platform-used-in-experiments-|Khepera II mobile robot (hardware platform used in experiments)]]

## Questions Raised

- How does CoQL scale to larger numbers of agents beyond the two-to-four agent regimes tested?
- Does the team-goal exploration property remain efficient when robots have highly asymmetric path lengths?
- How does ICFA compare to modern gradient-based trajectory optimisers or deep RL methods?
- Can the single shared Q-table approach (Chapter 4) be extended to partially observable or decentralised settings?
- What is the empirical ceiling on the number of agents before the feasible joint-state constraint (Chapter 4) becomes intractable?
- Does the consensus condition (CoQL) always exist when more than two equilibrium types are present?
- How sensitive is ICFA performance to the random-walk step-size modulation heuristic?

<!-- AUTHORED REGION END -->
