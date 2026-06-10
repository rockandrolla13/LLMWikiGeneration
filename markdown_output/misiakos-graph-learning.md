## GRAPH LEARNING FOR FINANCIAL NETWORKS 

By 

## Shui Yu 

## A dissertation submitted to the 

## Graduate School-Newark 

Rutgers, The State University of New Jersey 

In partial fulfillment of the requirements 

For the degree of 

## Doctor of Philosophy 

Graduate Program in Management 

Written under the direction of 

Dr. Xiaodong Lin 

And approved by 

Newark, New Jersey 

May 2024 

© 2024 

Shui Yu 

ALL RIGHTS RESERVED 

## ABSTRACT OF THE DISSERTATION 

Graph Learning for Financial Networks 

## by Shui Yu 

Dissertation Director: Dr. Xiaodong Lin 

The emergence of real-world financial networks, such as the inter-bank market, overthe-counter (OTC) bond market, and cryptocurrency market, has led to an increasing interest in their applications. These applications include risk propagation, crisis prevention, fraud detection, anti-money laundering, and anomaly detection. In this paper, we focus on the challenge of understanding and predicting the trading behaviors for the OTC corporate bond dealer network. Addressing this challenge is crucial, as accurate predictions can play a key role in preventing the spread of risk and minimizing losses if a dealer encounters financial trouble. We introduce a continuous dynamic network link prediction approach that incorporates neighborhood message aggregation. This method enhances our ability to understand and leverage the local structure of the network, resulting in improved prediction accuracy. 

This thesis comprises three chapters. The first chapter explores the topological structure of the dealer network, examining them in both static and dynamic contexts. We demonstrate that dealers’ topological importance within the network varies considerably, with different dealers assuming distinct roles. Additionally, we find that the importance of trading relationships varies, with some being more critical than others. The second chapter investigates the connection between dealers’ topological significance within the network and their behavior in the bond market. We found that dealers with greater topological importance 

ii 

tend to leverage their position for an advantage in the corporate bond market. In the third chapter, we introduced a continuous dynamic network link prediction method that utilizes neighborhood message aggregation to predict links within the dealer network. Traditional approaches often involve aggregating network data over specific time windows to create snapshots. However, this strategy has two main limitations. First, changing the length of the aggregation window can result in varying outcomes. Second, the network’s topology and the market’s trading volume can change abruptly. Therefore, a shift to a continuous dynamic framework is essential to address these challenges. 

In conclusion, our research focuses on analyzing dealer behaviors within the OTC bond market, with the aim of forecasting their future actions in a continuous dynamic setting. This study provides a strategic tool for the corporate bond dealer network to mitigate risk dissemination and reduce potential losses, particularly in scenarios where dealers face financial difficulties. 

iii 

## **ACKNOWLEDGMENTS** 

I would like to extend my sincere thanks to everyone who has assisted and supported me during my PhD studies. 

Foremost, I am deeply grateful to my supervisor, Prof. Xiaodong Lin, for his invaluable guidance, insightful feedback, and unwavering support. His mentorship extended beyond the academic realm, and his wisdom and life advice have been an inspiration to me. His encouragement during challenging times helped me persevere and his advice on navigating difficult situations was incredibly valuable. 

I am also thankful to the members of my thesis committee, Prof. Jian Yang, Prof. Periklis Papakonstantinou, and Prof. Wenge Guo, for their insightful comments and suggestions, which have significantly contributed to the enhancement of this thesis. 

My heartfelt thanks go to my father and my mother, for their unconditional love, patience, and belief in me. Their constant encouragement has been a source of immense strength and inspiration throughout my studies. Their sacrifices and selflessness have not gone unnoticed, and I owe them more than words can express. 

Finally, I must express my gratitude to my wife Yue Leng, who is my biggest cheerleader. Her support has been the backbone of this journey. Her presence was a constant source of comfort and motivation, and I am deeply grateful for everything she has contributed to my life and studies. 

iv 

## **TABLE OF CONTENTS** 

|**Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|ii|
|---|---|
|**Acknowledgments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|iv|
|**List of Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|viii|
|**List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|ix|
|**Chapter 1: Introduction**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|1|
|**Chapter 2: Corporate Bond Dealer Network Topology Analysis**<br>**. . . . . . . . .**|4|
|2.1<br>Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|4|
|2.2<br>Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
|2.3<br>Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
|2.3.1<br>Data overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
|2.3.2<br>Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
|2.4<br>Static Network Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
|2.4.1<br>Explore Static Network Topology Characteristics . . . . . . . . . .|9|
|2.4.1.1<br>Global-structure network topology . . . . . . . . . . . . .|11|
|2.4.1.2<br>Edge Weights and Node Strengths . . . . . . . . . . . . .|22|
|2.5<br>Dynamic Network Analysis . . . . . . . . . . . . . . . . . . . . . . . . . .|26|



v 

||2.5.1<br>Constructing Dynamic Network<br>. . . . . . . . . . . . . . . . . . .|27|
|---|---|---|
||2.5.2<br>Explore Dynamic Network Topology Characteristics<br>. . . . . . . .|30|
||2.5.2.1<br>Evolution of Network Structure . . . . . . . . . . . . . .|30|
|2.6|Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|**Chapter**|**3: Dealer Network Topology Characteristics and Dealer Trading Be-**||
||**havior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|38|
|3.1|Related Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|38|
|3.2|Data Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
||3.2.1<br>Round-trip Transaction Intermediation Chains . . . . . . . . . . . .|40|
||3.2.2<br>Dealer Markup<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|42|
|3.3|Experiments on the Role of Topological Characteristics in Corporate Bond||
||Dealer Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|42|
||3.3.1<br>Dealer Topological Characteristics and Trading Cost<br>. . . . . . . .|42|
||3.3.2<br>Dealer Topological Characteristics and Transaction Partner Prefer-||
||ence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
||3.3.3<br>Dealer Topological Characteristics and Prearranged Transaction<br>. .|54|
||3.3.4<br>Dealer Topological Characteristics and Dealer Losses . . . . . . . .|56|
||3.3.5<br>Dealer Topological Characteristics and Inventory Time . . . . . . .|58|
|3.4|Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|
|**Chapter**|**4: Temporal Graph Neural Network Link Prediction**<br>**. . . . . . . . . .**|62|
|4.1|Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
|4.2|Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
||4.2.1<br>Notations and Problem Formulation . . . . . . . . . . . . . . . . .|64|



vi 

||4.2.2|Deep Learning on Static Graphs . . . . . . . . . . . . . . . . . . .|65|
|---|---|---|---|
||4.2.3|Dynamic Graph Neural Network . . . . . . . . . . . . . . . . . . .|66|
||4.2.4|Link Prediction Methods . . . . . . . . . . . . . . . . . . . . . . .|70|
|||4.2.4.1<br>Network Embedding Based Methods<br>. . . . . . . . . . .|72|
|4.3|Experiment<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||76|
||4.3.1|Static Network Link Prediction . . . . . . . . . . . . . . . . . . . .|77|
||4.3.2|A Dynamic Graph Neural Network Model to Predict Transactions||
|||in Over-the-counter Bond Market<br>. . . . . . . . . . . . . . . . . .|82|
|||4.3.2.1<br>Modules Used to Construct the Model . . . . . . . . . . .|82|
|||4.3.2.2<br>Training<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|88|
|||4.3.2.3<br>Experiments Outcome . . . . . . . . . . . . . . . . . . .|89|
|4.4|Conclusion<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||92|
|**Chapter**|**5: Conclusion**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**||94|
|**References**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|||96|



vii 

## **LIST OF TABLES** 

|2.1|Constructing the network . . . . . . . . . .|. . . . . . . . . . . . . . . . .|8|
|---|---|---|---|
|2.2|Node level statistics, dealer network centrality. . . . . . . . . . . . . . . . .||11|
|2.3|Graph level statistics, dealer network centrality. . . . . . . . . . . . . . . .||12|
|3.1|Dealer markup and round-trip transactions .|. . . . . . . . . . . . . . . . .|43|
|3.2|Trading cost and dealer centrality: grouped analysis . . . . . . . . . . . . .||46|
|3.3|Trading cost and dealer centrality . . . . . .|. . . . . . . . . . . . . . . . .|49|
|3.4|Transaction chains . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .|50|
|3.5|Dealer centrality, transaction chain length, and dealer’s ability to locate|||
||trading counterparty . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . .|52|
|3.6|Prearranged transactions and dealer centrality|. . . . . . . . . . . . . . . .|55|
|3.7|Dealer loss probability and dealer centrality|. . . . . . . . . . . . . . . . .|57|
|3.8|Dealer markups and dealer inventory holding|time . . . . . . . . . . . . . .|59|
|3.9|Dealer centrality and holding periods . . . .|. . . . . . . . . . . . . . . . .|60|
|4.1|Link prediction results in AUC . . . . . . .|. . . . . . . . . . . . . . . . .|78|
|4.2|Percentile of node similarities . . . . . . . .|. . . . . . . . . . . . . . . . .|80|
|4.3|Percentage of successfully predicited edges|. . . . . . . . . . . . . . . . .|81|
|4.4|Comparison of message aggregation methods|. . . . . . . . . . . . . . . .|90|



viii 

## **LIST OF FIGURES** 

|2.1|The dealer network with edge weight color coded from blue (lower weighted||
|---|---|---|
||edges) to red (higher weighted edges). . . . . . . . . . . . . . . . . . . . .|10|
|2.2|Degree distribution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
|2.3|Local clustering coeffcient. . . . . . . . . . . . . . . . . . . . . . . . . . .|14|
|2.4|A comparison of network resilience, dealers exit randomly vs. larger deal-||
||ers exit frst. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|15|
|2.5|A comparison of network resilience, dealers exit randomly to larger dealer||
||exits frst.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|2.6|Exploring the effect of edge (trading relationship) removal<br>. . . . . . . . .|17|
|2.7|Cumulative node strength distribution (left) and cumulative edge weight||
||distribution (right) in the dealer network . . . . . . . . . . . . . . . . . . .|23|
|2.8|Scatter plot of transaction volume edge weight_wV_<br>_ij_ and the number of trans-||
||actions_wN_<br>_ij_ (left), and scatter plot of node strengths_sV_<br>_ij_ ,_sN_<br>_ij_ (right) . . . . .|24|
|2.9|Average (weighted) neighborhood degree,_⟨knn|k⟩_,_⟨kV_<br>_nn|k⟩_,_⟨kN_<br>_nn|k⟩_<br>. . . .|25|
|2.10|Daily and Monthly total bond transaction volume . . . . . . . . . . . . . .|28|
|2.11|Dealer network of a selected bond, aggregated at the daily level . . . . . . .|29|
|2.12|Dealer network of a random bond, aggregated at the weekly level . . . . . .|29|
|2.13|Dealer network of a random bond, aggregated at the monthly level . . . . .|30|
|2.14|Basic distributions of temporal network<br>. . . . . . . . . . . . . . . . . . .|31|
|2.15|Similarity of networks in consecutive time window<br>. . . . . . . . . . . . .|33|



ix 

|2.16|Topological overlap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
|---|---|---|
|4.1|Categories of link prediction methods (Wu, Song, et al. 2022) . . . . . . . .|72|
|4.2|Example of neighborhood information aggregators<br>. . . . . . . . . . . . .|84|
|4.3|Diagram for the scaler-combined aggregator . . . . . . . . . . . . . . . . .|87|
|4.4|Illustration of the algorithm.<br>. . . . . . . . . . . . . . . . . . . . . . . . .|89|
|4.5|Model performance comparison<br>. . . . . . . . . . . . . . . . . . . . . . .|91|



x 

1 

## **CHAPTER 1** 

## **INTRODUCTION** 

A network is essentially a set of points, known as nodes or vertices, interconnected by lines referred to as edges or links. Networks are pervasive in the real world, manifesting across various domains, allowing a wide array of systems to be analyzed through the lens of network theory. Key examples of such networks include informational networks like the Internet, telecommunications networks such as telephone networks, transportation networks encompassing roads, railways, air routes, and pipelines, social networks evident in social media and criminal networks, networks of scientific collaboration such as citation networks, and biological networks including food webs and protein-protein interaction networks. 

In the realm of financial networks, financial institutions function as nodes (e.g., banks, dealers), and their interactions are the edges (e.g., lending, trading). Given the complexity and vastness of the finance industry, various types of financial networks exist, including the inter-bank market, stock correlation networks, cryptocurrency markets and bond markets. The study of financial networks is pivotal for understanding and predicting complex financial phenomena, with risk management being a primary focus. Through the analysis of financial networks, stakeholders can comprehend how risk spreads throughout the system, identifying potential points of vulnerability where systemic risk may concentrate. 

In this thesis, we concentrate on the networks formed by dealers in the over-the-counter (OTC) corporate bond market. Historically, the network analysis of the OTC bond market has been limited due to challenges in accessing comprehensive data, primarily because transaction data lacked information on the identities of the parties involved. However, utilizing enriched corporate bond transaction dataset, which includes identification for both parties in a transaction, enables the construction of an OTC corporate bond dealer network. 

2 

In this network, the dealers represent the nodes, and the transactions between these dealers form the edges. Access to this dataset was challenging, and as a result, we were able to analyze corporate bond transactions only between the years 2010 and 2015. Despite not being the most current data, it offers a valuable opportunity to explore the OTC corporate bond market through network analysis methodologies. 

In Chapter 2, we establish the dealer network and undertake preliminary analyses. We reveal that the network displays a core-periphery structure through the examination of network topology measures and assess its resilience by simulating the removal of nodes and edges. Additionally, we investigate the network structures associated with bonds of varying ratings and explore the dealer network from both a static and dynamic standpoint. Our findings indicate that, within this over-the-counter (OTC) corporate bond network, nodes (dealers) with different topology attributes occupy varied roles in the network and exert differing levels of influence. 

In Chapter 3, we examine whether nodes of varying network topological importance demonstrate distinct trading behaviors in the corporate bond market. With the help of the detailed identity information available in the bond transaction dataset, we are able to track the movement of bonds from dealer to dealer, constructing transaction intermediation chains in the process. These intermediation chains reveal critical trading data, such as the markups applied by different dealers, the duration of bond holdings by various dealers, and the likelihood of a dealer incurring losses on transactions. We then investigate the connection between the dealers’ topological importance and this trading data. Our analysis reveals that dealers with differing levels of network topological importance exhibit varied trading behaviors. 

In Chapter 4, we explore link prediction within a dynamic dealer network setting, focusing on its implications for risk propagation in financial networks. This analysis helps us understand the mechanisms through which crises may spread across the entire system. We begin by reviewing several traditional link prediction methods commonly used in the 

3 

field. Upon applying these methods to the dealer network, we find that most traditional approaches are inadequate as they do not account for critical aspects such as node and edge attributes, which are crucial within the dealer network context. Consequently, we turn to graph neural networks (GNN) for more effective link prediction. As established in Chapter 2, the selection of aggregation windows significantly impacts the construction of temporal dealer networks. Therefore, we employ the latest advancements in continuous-time dynamic graph neural networks for our link prediction tasks. Additionally, we implement an enhanced message aggregation technique to more accurately capture local neighborhood structural information, resulting in improved prediction outcomes. 

4 

## **CHAPTER 2** 

## **CORPORATE BOND DEALER NETWORK TOPOLOGY ANALYSIS** 

## **2.1 Introduction** 

The financial market has been the subject of extensive study over the years, with a wealth of research shedding light on its various dimensions and dynamics. Among the diverse range of studies, research from a financial network perspective stands out for its critical importance. This approach is particularly valuable because it delves into the mechanisms of risk propagation and the strategies for crisis prevention, offering insights into how financial systems can become more resilient. 

In our investigation, we specifically focus on the financial network using corporate bond data for two primary reasons. First, the corporate bond market represents a significant and rapidly expanding segment of the financial landscape. Its growth and complexity make it a compelling subject for study, particularly from a network analysis viewpoint. Second, the availability of an enriched dataset with dealer identity information has opened up the opportunities to examine the corporate bond market through the lens of network theory. This dataset is unique in that it includes identification for both buyers and sellers, a feature that is crucial for constructing dealer networks. This novel dataset enables us to construct and analyze the network of over-the-counter (OTC) corporate bond dealers, a previously challenging endeavor due to data limitations. 

In this chapter, we employ tools and techniques from network theory to analyze and describe the topology of the OTC corporate bond dealer market. By analyzing the structure and dynamics of this network, we aim to uncover patterns and relationships that are crucial for understanding risk distribution, market behavior, and potential vulnerabilities. Through this analysis, we contribute to the broader field of financial network research, offering new 

5 

perspectives on how the corporate bond market functions and interacts within the global financial ecosystem. 

## **2.2 Related Work** 

Like many real world systems, financial market can be seen as being structured like networks. As pointed out by Gale and Kariv 2007, there are basically two types of financial markets: centralized financial markets and decentralized financial markets. In a centralized financial market, commodities are traded on a centralized exchange. Some typical examples of centralized markets are stock exchanges such as the New York Stock Exchange (NYSE) or NASDAQ, or commodity exchanges such as Chicago Board of Trade (CBOT). On the other hand, decentralized markets can be naturally thought of as networks. A good example of decentralized market is inter-bank market. It was popular for early researchers to study contagion in inter-bank market. Allen and Gale 2000 studied how a small liquidity shock in one region can spread by contagion throughout the entire economy. Boss et al. 2004 constructed a financial network based on the dataset of Austrian inter-bank market. They found that the inter-bank network shows a community structure that exactly mirrors the regional and sectoral organization of the actual Austrian banking system. Degryse and Nguyen 2004 suggested that the network structure of a inter-bank market is an important driving factor in the risk and impact of inter-bank contagion, as an event of an initial bank failure may lead to domino effects to the entire inter-bank market. They found that if an inter-bank market has a more concentrated network structure, the risk and impact of contagion will be decreased. They also suggested that cross-border inter-bank assets has lowered the risk and impact of local contagion. Upper and Worms 2004 studied the German interbank market, they tested whether the breakdown of a single bank can lead to contagion to the entire network. They found that while the danger of contagion is normally confined to a limited number of relatively small banks, bank failures that affect a sizable part of the banking system remain a possibility even if regulators explicitly take into account safety 

6 

mechanisms like the institutional guarantees for savings banks and cooperative banks. Li, He, and Zhuang 2010 built network models of an inter-bank market based on inter-bank credit lending relationships. They showed that the inter-bank network has a low clustering coefficient and a relatively short average path length, community structures, and a twopower-law distribution of out-degree and in-degree. Xu, He, and Li 2016 constructed a dynamic network model for inter-bank market, and tested dynamic stability in the network evolution process. Chiu et al. 2020 showed that in an inter-bank market, banks choose to build relationships in order to insure against liquidity shocks and to economize on the cost to trade in the inter-bank market. They suggested that relationships between banks can explain some anomalies in the level of interest rates. 

The over-the-counter (OTC) bond market serves as another notable instance of financial networks, characterized by its decentralized nature. Historically, the challenge of limited data access hindered researchers’ ability to map out networks within the OTC bond market. However, the recent availability of detailed transaction data, including information on the identities of buyers and sellers, has enabled the construction of OTC bond dealer networks. In these networks, dealers are represented as nodes, while the transactions between them form the edges. Li and Schurhoff 2019 constructed a financial network using the over-thecounter municipal bond market data, and explored the network topology. Colliard et al. 2021 studied the effects of dealers’ connectedness in over-the-counter dealer networks and dealers’ aggregate inventories on prices. Hendershott et al. 2020 examined the network of trading relationships between insurers and dealers in the over-the-counter bond market. Di Maggio et al. 2017 studied financial network’s topological change during periods of market turmoil using over-the-counter bond market data. While comprehensive, those works rely on traditional statistical network models. 

7 

## **2.3 Data** 

## 2.3.1 Data overview 

The foundation for our analysis of the over-the-counter (OTC) bond market dealer network is an enhanced version of the Trade Reporting and Compliance Engine (TRACE) dataset. This enriched dataset encompasses the period from 2010 to 2015 and captures details for each executed trade, including the involved dealer(s), complete CUSIP of the traded bond, transaction volume, price, date, time, and reporting side (buy or sell). The enhanced TRACE data offers several distinct advantages. 

A critical feature of this enhanced dataset is access to identifiers for both the selling and buying parties within each transaction. Each dealer is assigned a unique four-letter identifier, while individual customers are denoted by the letter “C”. This distinction allows for the clear identification of dealer-to-dealer and dealer-to-customer transactions. Furthermore, with access to dealer identifiers, the dataset enables us to track whether a specific dealer is selling bonds to a customer or another dealer. 

This valuable data feature facilitates the construction of a dealer network, where nodes represent dealers and edges represent transactions between them. In essence, two dealers (nodes) are considered connected if they have engaged in at least one transaction, documented within the dataset. Under specific circumstances where the strength of the connection between dealers is relevant, the weight of the edge can be determined by either the total transaction volume or the number of transactions transacted between the two dealers. 

## 2.3.2 Data Preprocessing 

The dataset encompassing OTC bond market dealer network transactions from 2010 to 2015 comprises 67,699,071 records. These transactions include interactions between both dealers and customers. Due to the anonymity assigned to all individual customers (denoted by “C”), our analysis focuses solely on the dealer network, necessitating the removal of all 

8 

transactions involving customers. This filtering process results in a data sample containing 37,834,237 transactions. 

An inherent characteristic of the TRACE data collection process is the duplication of transaction records stemming from the reporting obligations of FINRA member brokerdealers. For instance, a single successful transaction involving two dealers acting as buyer and seller, respectively, would be reported by both parties, leading to duplicate entries within the dataset. An initial, yet ineffective, approach to address these duplicates would be to segregate the dataset into two groups based on the reporting side (buyer or seller) with the expectation of identical transaction counts within each group. However, upon closer examination, the data reveals that this is not the case. Certain transactions are reported only by one party (buyer or seller), while the majority are reported by both. 

To ensure the accurate removal of duplicate records, a more precise approach is required. First, the entire dataset is partitioned into two groups based on reporting side (buyer-reported and seller-reported transactions). Subsequently, transactions within these groups are evaluated for duplicates. If two transactions, one from each group, possess identical bond CUSIP, transaction price, volume, and transaction date, but involve entirely opposite dealers on the reporting sides, they are classified as duplicates reported by both parties, and one record is eliminated. Any remaining transactions that lack a corresponding match in the opposite group are presumed to be unique and retained. Following this duplicate removal process, the resulting dataset contains 22,729,930 transaction records. Table 2.1 provides the details. 

||Number of transactions|
|---|---|
|Full dataset|67,699,071|
|Remove customer involved transactions|37,834,237|
|Remove Duplicates|22,729,930|
|Remove bonds with no information in Mergent FISD|22,497,990|



Table 2.1: Constructing the network 

9 

## **2.4 Static Network Analysis** 

In this section, preliminary examinations are conducted on the dealer networks that we have formulated. 

The initial step in analyzing a network is to distill the data into interpretative, meaningful insights. For networks of a smaller magnitude, the act of visualizing the network data can be both revealing and straightforward. However, in the context of extensive networks, a simplistic visual representation may lead to confusion and lack of precision. In the following, we thoroughly investigate the structural patterns of the network. 

## 2.4.1 Explore Static Network Topology Characteristics 

To understand the overarching structure of this extensive network, we begin by examining the graph of the dealer network depicted in Figure 2.1. In this graph, each node symbolizes a dealer, and each connecting line, or edge, represents a trading relationship between them. The thickness of these edges, indicating the volume of transactions, is visually differentiated by a color gradient ranging from blue (for lower transaction volumes) to red (for higher transaction volumes). A notable observation is the absence of small, localized clusters commonly found in various social networks, such as communication or email networks. Instead, a concentration of densely interconnected nodes, linked by red edges, is prominent at the network’s core. This concentration suggests that the bulk of significant transactions are confined within this central group, with such high-value exchanges scarcely occurring outside this central group. 

Our analysis of transaction volumes and frequencies revealed that the top 10 dealers accounted for 52% of the total transaction volume, with the top 20 dealers contributing to 70%. This disparity highlights the presence of a significant number of less active dealers with fewer connections. With 1,700 nodes and a potential for over 1.4 million connections (considering an undirected graph structure), the actual connection count stood at 48,403, 

10 

Figure 2.1: The dealer network with edge weight color coded from blue (lower weighted edges) to red (higher weighted edges). 

This figure illustrates the network structure of dealers in coporate bond OTC market. Each node represents a dealer, and each edge represents an trading relationship between a pair of dealers. This dealer network shows no small local clusters, instead, a group of nodes that are densely connected by red-colored edges can be observed in the center of the network, and red (high weighted) edges can rarely seen outside the group, which means the majority of the high-weighted edges seem to be within the group. 

underscoring the network’s sparse nature overall. The network exhibits a core-periphery structure, with a densely connected core of dealers surrounded by a more loosely connected periphery, as illustrated by the Figure 2.1 and further supported by the network’s overall topology. 

Besides the comprehensive network developed from the entire dataset, three distinct networks are generated based on the types of bonds traded: investment-grade bonds, junk bonds, and those oscillating between investment and non-investment grade statuses. Table 2.2 and Table 2.3 present both the node-level and graph-level indices for these networks. The data indicates that dealers in the investment-grade bond network generally engage with a wider circle of trading partners. Conversely, the junk bond network features dealers with 

11 

||Overall<br>Investment Grade<br>Flip<br>Junk Bond|
|---|---|
|_dg_<br>_ev_<br>_bt_<br>_cl_<br>_kcore_<br>_cc_<br>_dwn_<br>_dwv_<br>_ewn_<br>_ewv_|N(Nodes) = 2178<br>N(Nodes) = 2044<br>N(Nodes) = 1706<br>N(Nodes) = 1883<br>N(Edges) = 99136<br>N(Edges) = 83407<br>N(Edges) = 52033<br>N(Edges) = 56042<br>Mean<br>S.D.<br>Mean<br>S.D.<br>Mean<br>S.D.<br>Mean<br>S.D.<br>45.51<br>97.94<br>40.80<br>89.60<br>30.5<br>66.83<br>29.76<br>68.78<br>0.1124<br>0.1963<br>0.109<br>0.193<br>0.1028<br>0.1815<br>0.0967<br>0.1773<br>2736<br>22341<br>2535<br>20734<br>2126<br>16093<br>2403<br>18780<br>0.0000042<br>0.00000133<br>0.0000041<br>0.00000137<br>0.0000034<br>0.00000106<br>0.0000043<br>0.00000149<br>26.34<br>38.35<br>23.52<br>34.75<br>17.87<br>26.03<br>16.79<br>25.10<br>0.2833<br>0.2400<br>0.2911<br>0.2554<br>0.2770<br>0.2620<br>0.2782<br>0.2576<br>3076682<br>20882598<br>2239492<br>14675261<br>344366<br>2026654<br>815721<br>5552510<br>10329.66<br>64888.96<br>7373.08<br>45394.57<br>1559.06<br>9096.63<br>2531<br>16196.31<br>0.0080<br>0.0566<br>0.0084<br>0.0554<br>0.0119<br>0.0744<br>0.0085<br>0.0641<br>0.0014<br>0.0256<br>0.0023<br>0.0282<br>0.0020<br>0.0293<br>0.0012<br>0.0269|



Table 2.2: Node level statistics, dealer network centrality. 

This table displays the node level indices in the dealer network. Four networks are constructed, one full dealer network, one network constructed with only investment grade bond transactions, one network constructed with only junk bond transactions, one with bonds that filps between junk and investment grade. In this table, _dg_ , _ev_ , _bt_ , _cl_ , _kcore_ and _cc_ rerepresent degree, eigenvector centrality, betweeness, closeness, k-core and Cliquishness. In the lower panel, _dwn_ , _dwv_ , _ewn_ and _ewv_ denote the transaction number weighted degree centraliry, transaction volume weighted degree centraliry, transaction number weighted eigenvector centrality and transaction volume weighted eigenvector centrality. 

a smaller average number of trading connections. This could suggest that junk bond transactions are more commonly conducted within tighter-knit circles of trusted partners. 

## _2.4.1.1 Global-structure network topology_ 

To precisely define and compare the core-periphery architecture of this over-the-counter (OTC) dealer network, an analysis is conducted to highlight the distinctions between our specific dealer network and a hypothetical random network that emulates a stock exchange environment. Imagine a random dealer network with the same quantity of dealers as our OTC network. In contrast to OTC transactions, dealers in this imaginary network execute trades through a centralized exchange anonymously, leaving them unaware of their counterparties’ identities. Within this random network, a dealer’s degree, which indicates the number of counterparties it engages with, is presumed to follow a Poisson distribution char- 

12 

||Overall<br>Investment Grade<br>Flip<br>Junk Bond|
|---|---|
|Density<br>Reciprocity<br>Clustering Coeffcient<br>Centralization(Degree)<br>Centralization(Closeness)<br>Centralization(Eigenvector Centrality)<br>Diameter|N(Nodes) = 2178<br>N(Nodes) = 2044<br>N(Nodes) = 1706<br>N(Nodes) = 1883<br>N(Edges) = 99136<br>N(Edges) = 83407<br>N(Edges) = 52033<br>N(Edges) = 56042<br>0.0209<br>0.0199<br>0.0158<br>0.0178<br>0.7887<br>0.774<br>0.7254<br>0.7258<br>0.7974<br>0.7897<br>0.7183<br>0.7193<br>0.3857<br>0.3715<br>0.3658<br>0.348<br>0.0002<br>0.0002<br>0.0002<br>0.0004<br>0.8891<br>0.8916<br>0.9046<br>0.8975<br>5<br>4<br>5<br>5|



Table 2.3: Graph level statistics, dealer network centrality. 

acterized by a mean rate _λ_ . For the sake of comparison, we posit that _λ_ is equivalent to the average degree observed within our OTC dealer network, exemplifying a decentralized network model. 

The degree distribution comparison, as illustrated in Figure 2.2, reveals differences in network connectedness between the OTC market and the theoretical random network. In the random network, the degrees of most dealers gravitate around _λ_ or fall below it, with a sharp decline in dealer numbers beyond a specific threshold, indicating a scarcity of dealers with significantly high connectivity. Conversely, the OTC dealer network showcases a subset of dealers with exceedingly high levels of interconnectedness, distinguishing them within the entire network. This results in a predominance of less connected, smaller dealers within the majority of the network, all competing against a few highly connected dealers. 

In Figure 2.3, node degree _k_ , is plotted on the horizontal axis against the local clustering coefficient _cc_ , on the vertical axis, both on a logarithmic scale. The plot reveals a negative correlation between _k_ and _cc_ . The local clustering coefficient measures the extent to which a node’s neighbors form a tightly-knit group, approaching a complete graph. This pattern, where nodes with higher degrees exhibit lower clustering coefficients and nodes with lower degrees display higher clustering coefficients, suggests that nodes with fewer connections are embedded within highly interconnected communities. These dense communities are, in turn, interconnected by nodes that have a higher number of connections. 

A key concept in network theory is how resilient a network is to failures. The resilience 

13 

Figure 2.2: Degree distribution. 

This figure provides the comparison of a randomly generated dealer network and OTC markets. In this figure, an inverse distribution function for the degree _k_ of different dealers in the dealer network on a log-log scale. The colored icons represents OTC dealers networks. Cross-shaped icon represent a randomly generated network, in which the degree of nodes follows a Poisson distribution, with _λ_ equals to the average degree of nodes in the OTC market dealer network. 

of the OTC dealer network is examined in Figure 2.4 by simulating the removal of certain dealers along with their connections (trading relationships) from the market, leaving the rest of the dealers unaffected. 

Figure 2.4 illustrates the size of the largest connected component, expressed as a percentage of the remaining network, as a function of the percentage of dealers (nodes) removed from the network. The left plot demonstrates the impact of randomly removing dealers, whereas the right plot shows the effect of strategically removing the most connected dealers first. The figure reveals that the decline in network integrity is much more pronounced when high-degree dealers are removed, as indicated by the steeper curves on the right compared to those on the left. Notably, even after the removal of a few key deal- 

14 

Figure 2.3: Local clustering coefficient. 

This figure explores the local clustering coefficient and hierarchical structure of the market. The horizontal axis shows the dealers degree distribution of the network, while the vertical axis show the clustering coefficient of the dealers. This figure is plot in log-log scale. 

ers, the main component remains relatively large, suggesting that other highly connected dealers still maintain the network’s cohesion. 

In the dealer network, a hierarchical structure is observed where major dealers are followed by smaller ones, who in turn are followed by even less connected dealers. This tiered arrangement contributes to the network’s resilience to faults. Random failures among the numerous less connected dealers have a negligible impact on the overall network’s connectivity. Even the failure of a major dealer doesn’t critically compromise the network’s connectivity, thanks to the presence of other high-degree dealers that keep the various local communities interconnected. However, the simultaneous failure of several key dealers could fragment the network into isolated components. Therefore, while these high-degree dealers act as crucial hubs ensuring the network’s overall connectedness, their potential failure also represents a significant vulnerability, as it could precipitate the network’s disintegration. 

Figure 2.5 introduces a different angle on assessing the connectedness of the network structure, building upon the previous illustration of how the network responds to dealer 

15 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0026-01.png)


**----- Start of picture text -----**<br>
(a) When dealers exits at random (b) when the most connected dealers exit first<br>**----- End of picture text -----**<br>


Figure 2.4: A comparison of network resilience, dealers exit randomly vs. larger dealers exit first. 

The two figures explore the effect on the network topology of of removing transaction relationships between dealers. The network connectedness is plotted as a function of of the number of dealers that are being removed from the network. The horizontal axis represents the number of dealer being removed from the network, the vertical axis represents the size of largest component in the remaining network. In panel (a) on the left, the dealers are removed randomly, regardless of the dealers network characteristics, while in panel (b) on the right, the dealers with higher degrees are removed first. 

exits under two distinct scenarios: random dealer exits versus targeted exits of the most connected dealers. Here, the focus shifts to examining the impact of dealer removals on the average shortest path lengths within the network. The network’s major dealers act as pivotal connectors or “hubs” linking the peripheral dealers. As these hubs are removed, reaching from one node to another often requires longer, more circuitous routes, explaining the sharp increase in path lengths depicted in the right panel of the figure. Conversely, as these key dealers are systematically removed, the network eventually disintegrates into smaller, disconnected subgraphs, leading to a reduction in the average path length. 

On the left panel, where dealers are removed at random, the departure of a dealer on the network’s periphery minimally impacts the overall structure’s cohesion, leaving the 

16 

average shortest path length relatively unchanged. This contrast highlights the critical role of major dealers in maintaining network integrity, underscoring how their removal not only disrupts direct connections but also necessitates more indirect paths to maintain network connectivity. 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0027-02.png)


**----- Start of picture text -----**<br>
(a) When dealers exits at random (b) when the most connected dealers exit first<br>**----- End of picture text -----**<br>


Figure 2.5: A comparison of network resilience, dealers exit randomly to larger dealer exits first. 

The two figures explore the effect on the network topology of of removing transaction relationships between dealers from another perspective. In this plot, _Average path length_ is used to measure the network’s resilience to dealer (nodes) removal. 

We explore the effect of removing nodes (dealers) from the dealer network in the previous section. In the following part, we study the effect of removing edges (trading relationships) on the dealer network, as shown in Figure 2.6. Instead of removing edges randomly, edges are removed based on three edge attributes: edge weight _wij[V]_[, edge neighbor] similarity (overlap) _Oij_ , and edge betweenness _bij_ . Edges are removed in two directions: edges with low values of _wij[V]_[,] _[ O][ij]_[,] _[ b][ij]_[are removed first, or, edge with high values of these] attributes are removed first. We use parameter _f_ to represent the percentage of edges removed. When _f_ = 0, zero edge is removed and the entire network is fully maintained; 

17 

Figure 2.6: Exploring the effect of edge (trading relationship) removal . 

This figure displays the percolation analysis of the dealer network. The red line indicates the removal of low-valued edges first, and the blue line denotes the removal of high-valued edges first. Each row shows different network indices. For the rows from top to bottom: (1)[[˜]] _s_[2] _ns_ 

_s FGC_ , the fraction of nodes in the giant component, (2) average cluster size _S_[[˜]] = _s N_ excluding the giant component, where _ns_ is the number of clusters of size _s_ , (3) the average shortest path length[˜] _l_ , and (4) the average clustering coefficient _C_[˜] , (5) the assortativity _A_ , which measures whether the nodes tend to be connected with nodes with similar degrees, (6) centralization score of the network _C_ , which measures the centralization of the network from the graph level. While the rows are network indices, the columns define how the edges are removed in the percolation procedure. In the columns, (1) the edges are removed according to edge weight. (2) the edges are removed according to neighborhood similarity (overlap), which quantifies the topology overlap of the neighborhood of two vertices by the relative overlap of their common neighbors. (3) the edges are removed according to edge betweenness. 

18 

when _f_ = 100, all the edges are removed and only a set of isolated nodes left in the network. We explore the network’s response to removal of edges, by studying the six network indices as a function of the percentage of networks removed _f_ . The six indices are (1) _FGC_ , _s_[2] _ns_ the fraction of nodes in the giant component, (2) average cluster size _S_[˜] =[�] _s N_[, where] _ns_ is the number of clusters of size _s_ , (3) the average shortest path length[˜] _l_ , (4) the average clustering coefficient _C_[˜] , (5) the assortativity _A_ , which measures whether the nodes tend to be connected with nodes with similar degrees, and (6) centralization score of the network _C_ , which measures the centralization of the network from the graph level. By observing the behavior of the network indices while deleting edges, we can tell what role different edges play in the global network topology. 

The parameter _FGC_ is defined as the fraction of nodes left in the giant component after the deletion of edges, or in other words, _FGC_ represents the fraction of nodes that can all reach each other through the connected paths within the network. According to Figure 2.6, while removing edges from high _Oij_ to low _Oij_ , from high _bij_ to low _bij_ and from low _wij[V]_[to][high] _[w] ij[V]_[leads][to][a][sudden][disintegration][of][the][network][at] _[f][ O][≈]_[0] _[.]_[95][,] _[f][ b][≈]_[0] _[.]_[9] and _f[w] ≈_ 0 _._ 9, respectively. In contrast, while first removing edges with low _Oij_ , low _bij_ and high _wij_ will shrink the network, it will not suddenly break it apart. This strongly suggests that low-weight and high-weight edges, low and high overlap edges, and low and high betweenness edges all have different global structural roles in the dealer network. In particular, it seems that removing high _Oij_ edges has a similar effect with removing low _bij_ edges. 

The second row of the plot shows the behavior of average component size in the net- _s_[2] _ns_ work with the giant component excluded, which is denoted as _S_[˜] =[�] _s N_[.][According] to percolation theory (Shante and Kirkpatrick 1971), if the network falls apart during the transition of control parameter _f_ , the mean cluster size _S_[˜] goes to infinity and the percolation transition takes place while _f_ approaches the critical value _fc_ . An obvious divergence is clearly visible in the plot while removing edge from high _Oij_ values. In a traditional 

19 

social network, for example, a mobile phone communication network, the divergence occurs at _f ≈_ 0 _._ 8 while removing edges from high _Oij_ values, but in this dealer network, the divergence occurred very late at _f ≈_ 0 _._ 95. This could be the result of the core-periphery topology of the network. The core dealers are so densely connected by many high weight edges that the network doesn’t fall apart until the majority of the edges are deleted from the network. The role of weak and strong edges are different at the local level and has important consequences from the network perspective, understanding their different global role is central. According to the plot, the removal of strong edges lead to an obvious phase transition at _fc[w][≈]_[0] _[.]_[95][, but there is no transition when weak edges are removed first.][The] result confirms that the edges with high or low _Oij_ values have different global roles in the dealer network. 

The findings in these two graphs become even more intriguing when compared with the observations from Figure 2.4 regarding dealer removals from the network. To expedite the network’s disintegration, it’s essential to eliminate dealers with a high number of connections first. However, when simulating percolation in the network by removing trading links, the network tends to fragment more quickly if connections carrying lower volumes are removed first. This is due to the fact that connections involving larger dealers, typically those with many connections, are robust; even if a heavily used connection is cut, the affected dealers might still remain linked through mutual acquaintances, keeping them within the network’s largest connected component. Conversely, a less significant connection’s removal, particularly one that might be the sole link for a less connected dealer to the broader network, could isolate this dealer, accelerating the network’s fragmentation. 

While the size of the largest connected component gives us an overview of network connectivity, it doesn’t unveil the network’s structural details; it only informs us about the count of nodes within this main component. To delve into the network’s structure, we examine the average shortest path length,[˜] _l_ , which represents the average number of steps along the shortest paths connecting any two nodes within the largest component. This measure sheds 

20 

light on the network’s efficiency and functionality from a topological standpoint, as a path’s presence is crucial for potential information flow between nodes. Our analysis reveals that eliminating stronger connections generally leads to longer path lengths than does cutting weaker links, emphasizing the intricate balance between the network’s robustness and its vulnerability to the loss of key connections. 

In line with classic network theory, weak links in social networks often act as bridges between different communities. If we were to apply this concept to the dealer network, one might anticipate a rise in the average path length[˜] _l_ following the removal of weak links, given that such removal would hinder connectivity across diverse communities. However, the data show that cutting weak links barely impacts the size of the largest connected component or the average shortest path length. This outcome implies that, contrary to expectations and unlike in traditional social networks, weak links in the dealer network do not function as connectors between distinct communities. In fact, the core-periphery structure of this network suggests an absence of clearly defined communities as traditionally understood, underscoring a fundamental distinction in network topology between dealer networks and conventional social networks. 

We further study the network topology using the average clustering coefficient _C_[˜] . It serves as an indicator of the network’s local cliquishness or the extent to which nodes tend to cluster together. This measure differs from the average shortest path length[˜] _l_ , which is calculated solely for the largest connected component. The average clustering coefficient, however, is assessed across all nodes with a degree _k_ greater than one within the entire network. As depicted in the fourth row of Figure 2.6, the removal of strong links results in a notably lower curve compared to when weak links are eliminated. This pattern emerges because strong connections are predominantly found within the network’s densely interconnected core, where triangular connections (cliques) are common. Eliminating these strong links disrupts these triangles, diminishing the clustering coefficient. Conversely, the removal of weak links impacts the clustering curve only marginally at first, reflecting 

21 

their peripheral placement within the network. These weak links typically serve as local connectors without contributing significantly to triangular formations, hence their removal scarcely affects the overall clustering coefficient. 

Assortativity in a network evaluates the tendency of nodes to connect with other nodes that have a similar number of connections. As indicated in the fifth row of Figure 2.6, the dealer network’s overall assortativity _A_ consistently stays negative, regardless of how edges are removed. This suggests that within the dealer network, dealers with a large number of connections (high-degree dealers) usually connect with dealers having fewer connections (smaller dealers). Despite both trends showing an increase, the assortativity experiences a slight decline before surging sharply when high-weight edges are removed first. This initial decrease in assortativity can be attributed to the removal of connections between large dealers first, which accentuates the network’s tendency for high-degree nodes to link with low-degree ones (disassortativity). Once approximately 40 percent of the highest weight edges are eliminated, the network predominantly contains smaller dealers with similar degrees of connections, leading to an increase in assortativity. 

The second column examines how the network structure evolves when connections are eliminated based on the degree of overlap in their trading partnerships. The first row highlights that when connections with low neighborhood overlap _Oij_ are removed first, the size of the largest connected component _FGC_ declines more rapidly compared to when connections with high _Oij_ are removed first. This suggests that trading relationships among dealers who share common trading partners play a crucial role in maintaining the cohesion of the dealer network. 

The fifth row within this column focuses on changes in assortativity, a measure that reflects the tendency of nodes to connect with others that have a similar degree of connectivity. The results indicate that removing connections starting from those with high _Oij_ to those with low _Oij_ exerts minimal impact on the network’s overall assortativity. In contrast, when connections with low _Oij_ are targeted for removal, there’s a marked increase 

22 

in assortativity, eventually pushing the network towards a state of assortative mixing. This transition implies that, as the network evolves with these specific removals, the remaining structure increasingly consists of dealers that are more likely to connect with others of similar connectivity levels. 

In the final row of this column, the impact of removing connections based on _Oij_ is analyzed in terms of network centralization. The findings reveal that targeting connections with low _Oij_ for removal significantly influences the network’s centralization. Since centralization measures the degree to which a network is organized around specific central nodes, this pattern suggests that the removal process disproportionately affects the connections between central and peripheral dealers, leading to a decrease in the network’s overall centralization. Essentially, this indicates that the structural links between core dealers and their peripheral counterparts are severed, resulting in a less centralized dealer network. 

## _2.4.1.2 Edge Weights and Node Strengths_ 

The relationships between dealers in terms of trading activity are quantified using two metrics: the aggregated number of transactions between two dealers _wij[N]_[and the total volume] of these transactions _w[V]_[Similarly, the strength of a dealer, or node, can be defined in two] _ij_[.] ways: _s[N] i_[=][�] _j∈N_ ( _vi_ ) _[w] ij[N]_[represents the total number of transactions a dealer engages in] with their trading partners, and _s[V] i_[=][ �] _j∈N_ ( _vi_ ) _[w] ij[V]_[, represents the total volume of transac-] tions conducted by the dealer, where _N_ ( _vi_ ) indicates the neighborhood or the set of direct trading partners of dealer _i_ . The distributions of cumulative link weights _P>_ ( _w[N]_ ) and _P>_ ( _w[V]_ ) and cumulative node strengths _P>_ ( _s[N]_ ) and _P>_ ( _s[V]_ ) are illustrated in Figure 2.7. 

The measures of node strength, _s[N] i_[and] _[s][V] i_[,][indicate][the][level][of][a][dealer’s][market][ac-] tivity, whereas the weights _wij[V]_[and] _[w] ij[N]_[describe][the][strength][of][the][trading][relationship] between two specific dealers. The broad distribution of edge weights signifies that while most dealers engage in a relatively small number of transactions or transactions of low volume, a minority of dealers participate in frequent trading or handle transactions of very 

23 

high volumes. On average, a dealer conducts approximately 1,725 transactions per year, with an average total transaction volume of about 551,008 thousand dollars. Each trading relationship between two dealers sees, on average, about 63.6 transactions annually, involving an average transaction volume of 20,293.6 thousand dollars. 

Figure 2.7: Cumulative node strength distribution (left) and cumulative edge weight distribution (right) in the dealer network 

This figure displays the inverse distribution function for the node strengths and edge weights on a log-log scale. Nodes strengths and edge weights are measured in terms of the number of transactions , corresponding to _P>_ ( _s[N]_ ) and _P>_ ( _w[N]_ ) , as well as the total transaction volume, given by _P>_ ( _s[V]_ ) and _P>_ ( _w[V]_ ). 

The two edge weights _wij[N]_[and] _[ w] ij[V]_[are strongly correlated as expected, and the evidence] is displayed in panel (a) of Figure 2.8. In this dealer network, the edge weight of _wij[N]_[and] _wij[V]_[has a Pearson’s linear correlation coefficient of 0.41. Furthermore, while trying to char-] acterize the relationship between the two edge weight using Spearman’s rank correlation coefficient _ρ_ , a correlation coefficient of 0.73 is found. As for the correlation between node strengths _s[N] ij_[and] _[ s][V] ij_[,][the pattern is even stronger.][Pearson’s linear correlation has a value] of _r_ ( _s[N] ij[, s][V] ij_[)][=][0] _[.]_[64][,][and] _[ρ]_[(] _[s][N] ij[, s][V] ij_[)][=][0] _[.]_[88][.][In][both][cases,][the][Spearman’s][correlation] is higher than Pearson’s, which suggests that while the relationships between _wij[N]_[and] _[ w] ij[V]_ 

24 

(also _s[N] ij_[and] _[ s][V] ij_[) have linear components, the correlation seems to be non-linear.] 

Figure 2.8: Scatter plot of transaction volume edge weight _wij[V]_[and the number of transac-] tions _wij[N]_[(left), and scatter plot of node strengths] _[ s][V] ij_[,] _[ s][N] ij_[(right)] 

In this figure, the horizontal axis represents the transaction volume edge weight (node strength), the vertical axis represents the edge weight of number of transactions (node strength). Both the two plots show strong patterns of correlation. 

Newman 2002 introduced the notion of network assortativity to explore how the likelihood of forming connections to a target node might also depend on the degree of that node’s neighbors. His research delineated networks into two distinct types: those exhibiting “assortative mixing” where nodes of higher degrees tend to connect with other nodes of similarly high degrees, and those showing “disassortative mixing”, where nodes of higher degrees predominantly attach to nodes of lower degrees. Through his analysis of various social networks, such as coauthorship networks, actor collaboration networks, and networks of company directors, Newman 2002 observed that social networks typically display assortative mixing. This suggests a tendency for individuals with a larger circle of acquaintances to associate with others who have similarly extensive networks. This ob- 

25 

servation raises the possibility that the degrees of adjacent nodes in a social network are interdependent, prompting an examination of degree-degree correlations within the dealer network. 

These correlations are captured by the joint probability distribution _P_ ( _k, k[′]_ ), which indicates the likelihood of a node with degree _k_ connecting to a node with degree _k[′]_ . A more direct and informative approach, however, involves examining the average degree of a node _j∈N_ ( _vi_ ) _[w] ij[N][k][j] j∈N_ ( _vi_ ) _[w] ij[V][k][j] vi_ ’s nearest neighbors, expressed as _knn,i[N]_[=] and _knn,i[V]_[=] , _s[N] s[V] i i_ where _knn,i[N]_[denotes the number of transactions weighted average neighbor degree and] _[ k] nn,i[V]_ denotes the transaction volume weighted average neighbor degree. Averaging the three indices gives _⟨knn|k⟩_ , _⟨knn[V][|][k][⟩]_[,] _[⟨][k] nn[N][|][k][⟩]_[,][which][measures][the][relationship][with][immediate] neighbors of a given degree, while taking the magnitude of interaction into account. It can be observed that in Figure 2.9, the three indices behave very similarly, all three plots showed a decreasing pattern, indicating that the the dealer network is disassortative mixing, which is very different from most social networks. In most traditional social networks, including biochemical networks, individuals are more likely to be connected with other similar individuals, and this is assortative mixing. 

Figure 2.9: Average (weighted) neighborhood degree, _⟨knn|k⟩_ , _⟨knn[V][|][k][⟩]_[,] _[ ⟨][k] nn[N][|][k][⟩]_ 

The three legends, corresponds to unweighted _⟨knn|k⟩_ , transaction volume weighted _⟨knn[V][|][k][⟩]_[and number of transactions weighted] _[ ⟨][k] nn[N][|][k][⟩]_[.] 

26 

Conversely, in networks characterized by disassortative mixing, individuals with differing characteristics tend to interact more frequently. Newman (2002) highlighted the Internet as an example of a network exhibiting disassortative mixing. This finding might seem surprising at first, but various explanations offer clarity. Newman posited that within the Internet, nodes with a high degree of connections, such as connectivity providers like telecom companies, often link to clients who typically maintain only a single connection. As a result, there’s a tendency for nodes with a high number of connections to be linked to those with few connections. 

This analogy extends to the dealer network as well. In a similar vein to the Internet’s structure, major dealers in the network act as connectivity hubs. They purchase bonds from peripheral dealers and sell them to other peripheral dealers. To facilitate buying and selling from a diverse group of dealers, these central dealers form numerous connections. However, many of these connections are with smaller dealers who themselves are not highly connected within the network. Meanwhile, these smaller, lower-degree nodes may not have many connections, but they are typically connected to neighbors that do, allowing their trading needs to be met by these more central dealers. This setup illustrates how disassortative mixing in the dealer network enables a functional trading ecosystem, where central hubs facilitate the flow of bonds across the network. 

## **2.5 Dynamic Network Analysis** 

Networks evolve and change over time. The principal aim of dynamic network analysis is to pinpoint and articulate these changes. Moreover, by examining the alterations within networks, it becomes possible to forecast their future evolution and the subsequent shifts in the real-world systems they represent. Indeed, the incorporation of temporal aspects distinguishes dynamic network analysis from conventional link analysis, highlighting the importance of time in understanding network behavior and evolution. 

27 

## 2.5.1 Constructing Dynamic Network 

In discussions of temporal networks, the focus often lands on networks constructed from data collected over specified intervals, such as daily, weekly, monthly, or yearly. This approach shares similarities with static network analysis, where data spanning an entire period are aggregated. In our examination of static dealer networks, we aggregate all transactions between two dealers over six years into a single connection, emphasizing the network’s overall structure. However, this method of aggregation overlooks dynamic changes, as it fails to capture the fluctuating activity of connections over time. For instance, two dealers might engage in numerous transactions in one month and none in the following, illustrating that connections can be intermittently active. Just as network topology influences the dynamics of system interactions, the temporal patterns of connection activations also play a crucial role. 

Constructing a temporal network allows for varying levels of aggregation, generally leading to two main methods for depicting changes over time: (1) Keyframes: This method involves representing the network as a series of snapshots, such as daily, monthly, or yearly networks ; (2) Deltas: This approach views the network as a sequence of individual temporal events, such as the addition or removal of nodes and edges. 

The keyframes approach is more commonly used to describe changes in networks (Kim and Anderson 2012, Li, Cornelius, et al. 2017, Folino and Pizzuti 2013). In this study, we will create temporal networks using keyframes by accumulating transaction data over time. To delve into this method and explore aggregation issues, we examine the bond transaction data from 2015, comprising 11,202,999 transaction records across 26,183 bonds over 252 trading days. To begin analyzing the overall transaction patterns statistically, a straightforward method is to assess the total transaction volumes daily or monthly. The resulting analysis reveals distinct patterns: daily aggregates ( Figure 2.10 (a)) show relatively stable volumes with noticeable weekly cyclicity, suggesting variations in total volume on different weekdays. Conversely, monthly aggregates ( Figure 2.10 (b)) display significant fluctua- 

28 

tions, with transaction volumes in spring and fall surpassing those in summer and winter. 

Figure 2.10: Daily and Monthly total bond transaction volume 

From a network perspective, every edge represents a trading relationship between two dealers, therefore, different levels of aggregation create different networks. Imagine two dealers that make high volume transaction with low frequencies, on a monthly level aggregation we would see a less active trading relationship between the two dealers, even if they make extremely large transactions when they trade. 

Another example is illustrated in Figure 2.11, Figure 2.12 and Figure 2.13. These three networks are created by aggregating the transactions of the most traded corporate bond. The first network is aggregated at the daily level and created using data from the first day of the month. The second network is aggregated at the weekly level using data of the first week of the month. And the third network is aggregated at monthly level using data of the entire month. If we look at Figure 2.11, which is the network aggregated at the daily level, we would identify two subgroups of transactions with node _CITI_ and _INGS_ as the central nodes in the groups. On a weekly aggregated analysis, we observe additional connections created between _CITI_ and _MSCO_ via _FATS_ , because after the first day of the week, the two dealers made indirect transactions via a middleman dealer. The newly added connections alter the network structure significantly. From a network flow perspective, the 

29 

two dealers have become crucial as they now connect two groups within the network. When examining the monthly aggregated network, it appears different because we now observe numerous transactions involving this bond, with transactions occurring between almost all 

dealers, except for the peripheral dealers, who are typically smaller. 

Figure 2.11: Dealer network of a selected bond, aggregated at the daily level 

Figure 2.12: Dealer network of a random bond, aggregated at the weekly level 

30 

Figure 2.13: Dealer network of a random bond, aggregated at the monthly level 

## 2.5.2 Explore Dynamic Network Topology Characteristics 

## _2.5.2.1 Evolution of Network Structure_ 

In order to analyze the evolving structure of the dealer network, we build a network _G_ ( _t_ ), which is aggregated with all the edges up to time _t_ . Initially, we observe the expansion of the aggregated network, focusing on the number of nodes and links, as well as the average degree, as the network _G_ ( _t_ ) evolves over time up to a moment _t_ , as depicted in Figure 2.14(a). Early in the aggregation process, there’s a notably quicker rise in the number of nodes _N_ ( _t_ ), with the network incorporating half of its nodes within approximately 11 days. This rapid expansion is succeeded by a deceleration in growth, attributed to the slower inclusion of less active nodes that commence transactions, thus becoming part of the aggregated network. Compared to a randomly generated network (represented by a dotted line), which sees a swift increase in node numbers within the initial days—quickly approaching its maximum capacity—the growth of _N_ ( _t_ ) in the actual network initially lags behind the random model. However, as the aggregation period extends, the randomly generated network approaches a “saturated” state more quickly, whereas the actual dealer 

31 

network continues to expand, reflecting a sustained integration of nodes over time. 

Figure 2.14: Basic distributions of temporal network 

This figure shows the basic distributions of the temporal dealer network. In the figure, the network _G_ ( _t_ ) is aggregated up to a time _t_ . The four panels, total numbers of nodes (a), total numbers of edges (b), average degree (c) and average edge weight (d) in the network were denoted as a function of aggregation time. The solid lines represent the original empirical data, while the dotted lines represent a randomly generated network. The randomly generated network contains same number of nodes and same number of edges with the original data. The timestamp of all transactions are generated with uniform distribution. 

In comparison, the increase in the number of edges _E_ ( _t_ ) unfolds more steadily, as illustrated in Figure 2.14(b). It takes roughly 40 days to accumulate 50% of the edges present in the entire 12-month aggregated network. Moreover, this growth doesn’t plateau; the number of edges continues to rise steadily over longer aggregation periods (Figure 2.14(c)), unlike the pattern observed for node numbers. This ongoing growth is mirrored in the rise of the average degree, suggesting that the network’s complexity continues to escalate even 

32 

after the node count stabilizes within a 12-month period. This indicates that not all possible connections within the network have been established within this timeframe, with the average degree expected to increase with longer observation windows. 

This phenomenon is influenced by multiple factors: Firstly, the distribution of edge weights is broad, indicating numerous edges with infrequent transactions, which may take an extended period to manifest. Secondly, given such lengthy observation periods, the evolving nature of the network becomes apparent, with new trading relationships emerging and existing ones diminishing or dissolving. Thirdly, considering the dataset contains all the transactions in the OTC bond market, a portion of these may not consistently reflect the underlying dealer network’s structure. This could lead to a constant increase in the edge count. 

The growth of average edge weights, as shown in another Figure 2.14(d) , is expected to continue since all new transactions contribute to the cumulative weight of their respective edges. Although this growth rate decelerates towards the latter part of the observation period, it doesn’t flatten out as distinctly as the average node degree growth does. It’s important to note that introducing new links affects the network in several ways: it not only increases the number of connections (degrees) but also impacts the average weights of these connections. Furthermore, these new links can continuously alter the dynamics and add complexity to how the network evolves over time. 

Due to the dynamic nature described earlier, the dealer network continually evolves during the aggregation process. While certain trading relationships within the network demonstrate stability by remaining active over extended durations, others are transient, manifesting or becoming identifiable only within short timeframes. 

A method to quantitatively determine the characteristic time scale at which the network undergoes significant changes involves assessing the similarity between networks aggregated over various time spans. This assessment can be achieved by dividing the observation period into multiple consecutive aggregation windows and comparing the resulting 

33 

Figure 2.15: Similarity of networks in consecutive time window 

This figure shows the average similarity _σ_ of networks aggregated in time windows of different duration _W_ . The similarity _σ_ is calculated as the size of the intersection of networks in consecutive windows of different duration _W_ , divided by the size of their union. The _σ_ increases very fast at the beginning because as the duration _W_ increases, more common edges are involved in consecutive aggregated networks, and _σ_ becomes stable after _∼_ 30 days. However, as the aggregation time windows increase, more weak and random trading relationships are captured, after the _σ_ reaches a peak at around _∼_ 70 days, _σ_ starts to decrease slowly. 

networks to identify consistencies and variances in their structure. The similarity _σ_ of two networks _G_ 1 = ( _V_ 1 _, E_ 1) and _G_ 2 = ( _V_ 2 _, E_ 2) can be calculated as: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0044-04.png)


which is the size of the intersection of the sets _E_ 1 and _E_ 2 divided by the size of their union. As a result, if _σ_ = 1, then the two networks are completely the same; if _σ_ = 0, then no two edges are the same in the two networks. In Figure 2.15, the similarity _σ_ of networks in consecutive time windows of different duration is displayed. When the time windows 

34 

are very short, the networks are very sparse and the number of common edges is low. The similarity increases with increasing time window duration. The similarity gradually becomes stable after roughly 30 days. At around 70 days, the similarity reaches a peak, and then decreases very slowly. This is because the aggregation process starts to capture more and more of the very weak and random transaction relationships. 

As the number of edges in Figure 2.14(b) continues to grow without reaching a saturation point, it’s crucial to delve into the characteristics of links that emerge early in the aggregation process. Onnela et al. 2007 research on a mobile phone network highlighted how edge weights correlate with network topology, indicating that edges with higher weights are typically found within densely connected neighborhoods, while those with lower weights tend to bridge different neighborhoods. This observation aligns with Granovetter 1973’s well-known theory which posits that “weak ties enable reaching populations and audiences that are not accessible via strong ties.” This suggests that during network aggregation, communities characterized by high-weight edges tend to form early on. To further explore this dynamic, we examine the evolution of node-level Jaccard similarity, defined as: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0045-03.png)


, where _nij_ represents the number of common neighbors between two connected nodes _i_ and _j_ , and _ki_ and _kj_ are their respective degrees. The Jaccard similarity coefficient for the two vertices is calculated by dividing the number of common neighbors by the number of vertices that are neighbors of at least one of the two nodes under consideration. Figure 2.16 illustrates the average 12-month Jaccard similarity for newly added edges as a function of aggregation time, with each edge’s Jaccard similarity in the 12-month aggregated network calculated and then averaged across edges added at time _t_ . 

Past studies, such as Onnela et al. 2007’s work on mobile phone networks, have shown that clusters and communities with high-weight edges often emerge early in the aggrega- 

35 

tion process, supporting Granovetter 1973’s hypothesis. If this hypothesis holds true for the OTC dealer network, we might anticipate that edges integrated earlier in the process exhibit higher similarity than those added later, with the overall trend of similarity decreasing over time. This concept suggests that throughout the network aggregation process, the structure is predominantly shaped by strong links within dense clusters that appear early. In contrast, using longer aggregation periods results in the inclusion of many weak links (bridges between clusters), with strong edges typically connecting nodes that share numerous common neighbors, thereby exhibiting higher Jaccard similarity. 

Figure 2.16: Topological overlap 

The average final overlap of added edges as a function of aggregation time. For the overlap, we calculate the final overlap of edges in the 12-month aggregated network, and average over the final overlap values of newly added links at each time point. What we get is the average Jaccard similarity of the newly added edges at the time point. In the figure, the overlap increased quickly in early stage, and then grows steadily until it reaches the peak at _∼_ 120 days. The overlap then decreases and increases again. The increase indicates that most of the newly created edges are between dealers with common neighbors since the average overlap of the added edges are relatively high. A possible explanation for the decrease after the peak could be the result of some random and low-volume transactions. 

36 

The pattern observed in Figure 2.16 deviates slightly from what was anticipated. Initially, the overlap increases sharply as the aggregation time window _t_ is small, peaking at around 120 days. Afterward, the trend starts to decrease before rising again. This variance could be attributed to the core-periphery structure inherent in the dealer network. In contrast to traditional networks where Granovetter’s hypothesis is applicable, and newly added nodes tend to exhibit lower similarity due to forming connections with “stranger” nodes in other communities, the OTC dealer network operates differently. Despite the overlaps between communities, dealers in the OTC network are more inclined to engage with market participants who share common transaction partners, making transactions between completely unfamiliar dealers with no mutual connections rare. This accounts for the initial peak, where new transaction relationships predominantly form among dealers with shared neighbors. However, as previously suggested, over the long term, some transaction relationships might dissolve while new, significant transaction relationships emerge among dealers, influencing the pattern of Jaccard similarity over time. 

## **2.6 Conclusion** 

In this chapter, we examine the structure of the dealer network. Initially, we discover that the over-the-counter (OTC) corporate bond dealer network exhibits a core-periphery structure. Subsequently, we assess the network’s resilience by simulating the removal of nodes (representing dealers) and edges (indicating trading relationships). This analysis demonstrates that dealers within the network possess varying degrees of topological significance, which can be quantified using methodologies and tools from network theory. 

Further, we conduct a dynamic analysis of the network. We observe that different aggregation window lengths can yield divergent outcomes. Typically, to achieve consistent results, researchers prefer using a longer aggregation window for network aggregation. However, our analysis indicates that, although the similarity between networks in consecutive windows rapidly stabilizes (as indicated by a similarity score, _σ_ , around 0.6, as shown 

37 

in Figure 2.15), transaction volumes remain volatile. Furthermore, our analysis shows that trading relationships are highly unstable, with new trading relationships constantly being formed while older ones may cease to exist over time. Additionally, we note that even with the use of a comparatively longer aggregation window, the similarity of the network could experience sudden shifts. 

Building upon these observations, we intend to delve deeper into the relationship between the topological significance of dealers within the network and their market behavior in the following chapters. 

38 

## **CHAPTER 3** 

## **DEALER NETWORK TOPOLOGY CHARACTERISTICS AND DEALER TRADING BEHAVIOR** 

In the previous chapter, we illustrate how dealers with varying topological characteristics within the network exert different levels of influence. This leads us to explore several questions: How do a dealer’s network topological characteristics relate to their trading behaviors in bond markets? Which dealers are more profitable, and which tend to suffer greater losses? Additionally, how do bonds circulate within the dealer network? This chapter aims to address these problems via statistical models. 

Leveraging transaction data that includes detailed information about buyers, sellers, and bond CUSIPs, we can trace the movement of bonds across dealers, defined as transaction chains. By constructing these transaction chains and analyzing transaction prices, volumes, and timestamps, we can assess various metrics such as transaction markups and losses, as well as the duration bonds are held in inventory. 

## **3.1 Related Works** 

Dealer behaviors in the corporate bond market have been extensively studied by various researchers.” Schultz 2001 explored corporate bond transaction cost using institutional corporate bond trade data. They found that (1) trading costs are lower for larger trades; (2) small institutions pay more to trade than large institutions, when all else being equal; (3) small bond dealers charge more than large ones. However, they found no evidence that trading costs more for lower-rated bonds. Arcuri et al. 2020 compared the bonds issued by banks with those issued by firms from other sectors and find that the trading cost, other things being equal, is significantly higher for banks. Guo, Lehalle, and Xu 2022 discovered that the trading costs of corporate bonds decreased on average over the last 20 years. Dick- 

39 

Nielsen et al. 2023 studied the relationship between dealer network position and transaction costs. They documented a centrality discount (negative trading cost) for customer–dealer trades and a centrality premium (positive trading cost) for interdealer trades. They also showed that core dealers have a comparative advantage in carrying inventory. Pinter et al. 2024 studied trading costs in bond markets and showed that larger trades incur lower trading costs in government bond markets, and trading cost became higher for corporate bonds during major macroeconomic surprises and during Covid-19. 

Rapp 2018 provided empirical evidence that dealers’ inventory financing constraints are a crucial determinant of the costs of their liquidity provision incorporate bond markets. They showed that compared to low volatility bonds, the liquidity provision of high volatility bonds is more sensitive to inventory costs, especially during periods of funding stress. Goldstein and Hotchkiss 2020 found that while most dealers trade infrequently, dealers prefer to trade within the same day rather than holding the bond in inventory for longer periods. Meanwhile, dealers balance inventory costs and search costs in a way that reaches an equilibrium , where these costs are optimized to minimize losses and maximize profitability. Goldstein, Hotchkiss, and Nikolova 2021 studied the behavior of dealers trading in newly issued corporate bonds, they found that large institutions are net sellers of bonds in the initial days of trading, while smaller sized retail customers purchase bonds from non-syndicate member dealers at widely varying prices. At the same time, small customers purchasing a bond on the same day from the same dealer frequently pay over 2% higher prices. Griffin et al. 2023 showed that bond transactions exhibit considerable retail pricing variation, even for same-size trades of the same bond on the same day, and even from the same dealer. Meanwhile, Markups vary widely across dealers. 

40 

## **3.2 Data Construction** 

## 3.2.1 Round-trip Transaction Intermediation Chains 

Unlike frequently traded securities, bonds change hands less often. However, when transactions occur, they typically involve a process called round-trip transactions. In a round-trip transaction, bond dealers act as intermediaries, facilitating the bond sale between buyers and sellers through separate but connected trades. Corporate bond round-trip transactions involve a middleman, the bond dealer, who connects buyers and sellers. In a typical scenario, an individual investor (C) first sells the bonds to the dealer (D). The dealer then finds a new individual buyer (C) for those bonds. This initial sale and subsequent purchase form the “round-trip transaction”. 

Dealers have flexibility in how they handle the bonds they buy. Sometimes, they might sell the entire amount to a single buyer in one transaction (non-split round-trip transactions). Other times, they might divide the bonds into smaller lots and sell them to multiple buyers (split round-trip). 

The “round-trip” can also involve other dealers. In a CDC round-trip, the same dealer who buys from the investor also sells to the final buyer. For more complex situations, a chain of inter-dealer trades might occur before the final sale to the investor. Here, a “tail dealer” initially buys from the investor (C), then sells the bond through a series of trades with other dealers ((N)D), before finally selling it to a customer. This is called a C(N)DC round-trip. 

The round-trip transaction matching algorithm for the corporate bond transaction dataset is based on Green et al. 2007b and Li and Schurhoff 2019. Since the dataset has identifiers for every dealer, round-trip transaction match accuracy can be improved. 

While traditional studies are restricted to analyzing the two direct legs of a trade – the Customer-Dealer (CD) leg and the Dealer-Customer (DC) leg – due to the lack of dealer identifiers, our approach leverages dealer identifiers. This allows us to create the entire 

41 

intermediation round-trip transaction chain by tracing every bond from dealer to dealer through the network. This bond transaction“round-trip” concept helps to track bonds as they flow through the dealer network. This comprehensive tracking offers two key advantages: First, the matching algorithm provides improved matching accuracy. By considering the complete intermediation round-trip transaction chain, we can achieve a more accurate matching of buy and sell orders compared to the limited two-leg approach. Second, intermediation round-trip transaction chain’s complexity can be captured. We can not only record the intricate structure of the intermediation chains but also calculate both customer markups (the difference between the purchase price from the customer and the final sale price) and inter-dealer markups (the profit made by dealers during their internal transactions) within these chains. 

The matching process begins with Customer-Dealer transactions in the dataset. For each Customer-Dealer transaction, a matching transaction is identified based on the CUSIP (unique bond identifier), 4-letter ID (unique dealer identifier), transaction timestamp, and transaction volume. If the subsequent matching transaction is a Dealer-Customer transaction, it indicates that the dealer has sold the bond to an individual investor, and the transaction chain ends. However, if it is a Dealer-Dealer transaction, it signifies that the dealer has passed the bond to another dealer. The matching process then continues to search for the next matching transaction until a Dealer-Customer transaction is ultimately found. 

After running the algorithm to search for transaction round-trip chains in the dataset, we found 2.5 million complete transaction chains (chains that start with Customer-Dealer transactions and end with Dealer-Customer transactions). Additionally, we identified approximately 2 million incomplete chains (chains that begin with a Customer-Dealer transaction but do not find a matching Dealer-Customer transaction subsequently). Of the complete chains, the majority, about 1.7 million, involve only one dealer. We also found a total of 0.85 million chains involving two or more dealers. A detailed summary of the number of chains is displayed in Table 3.1. 

42 

## 3.2.2 Dealer Markup 

Our primary metric for measuring investor trading costs is the markup charged by dealers on round-trip transactions. This markup can be analyzed from both gross and net perspectives to provide a comprehensive understanding of the dealer’s profit margin. The gross markup represents the absolute difference between the price paid to the investor for the bond and the price at which it is ultimately sold. According to Li and Schurhoff 2019, we define dealers’ total markup _Mi_ charged on a round-trip chain _i_ as the volume-weighted transaction prices _Pi[DC]_ in a dealer-to-investor transaction, net of the purchase price _Pi[CD]_ which is the price of the investor selling the bond to the dealer, and normalized by the original purchase price. The formulation is defined as: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0053-03.png)


Within the context of C(N)DC round-trip chains, where multiple dealer-to-dealer transactions are involved in the round-trip, we calculate inter-dealer markups by leveraging the transaction prices observed between each participating dealer. 

## **3.3 Experiments on the Role of Topological Characteristics in Corporate Bond Dealer Network** 

## 3.3.1 Dealer Topological Characteristics and Trading Cost 

In this section, we explore the relationship between dealers’ trading cost and dealers topological importance in corporate bond dealer network. The dealers’ topological importance is measured by the calculated dealer centrality in the network, and the trading cost is measured by the dealers total markup on each transaction round-trip as defined in subsection 3.2.2. 

Table 3.1 summarizes the the descriptive statistics of trading costs associated with cor- 

43 

|Counts<br>Avg<br>Var|Percentile|
|---|---|
||5<br>25<br>50<br>75<br>95|
|C(N)DC<br>2,585,430<br>0.63<br>1.21<br>CDC<br>1,729,241<br>0.62<br>1.22<br>CDC-Nonsplit<br>896,840<br>0.42<br>0.98<br>CDC-Split<br>832,401<br>0.83<br>1.39<br>Markup for different chains:<br>CDC<br>1,729,241<br>0.62<br>1.22<br>CDDC<br>359,376<br>1.23<br>1.34<br>CDDDC<br>303,226<br>1.59<br>1.67<br>CDDDDC<br>123,549<br>1.91<br>1.81<br>CDDDDDC<br>53,189<br>1.90<br>0.21<br>CDDDDDDC<br>12,231<br>1.96<br>2.38<br>CDDDDDDDC<br>4,618<br>1.60<br>2.58<br>markup for different volumes:<br>under 25K<br>1,196,473<br>0.91<br>1.15<br>25K to 50K<br>350,134<br>0.75<br>1.02<br>50K to 99K<br>229,567<br>0.52<br>0.85<br>100K to 249K<br>291,777<br>0.32<br>0.70<br>250K to 499K<br>458,814<br>0.28<br>0.67<br>500K to 999K<br>177,072<br>0.19<br>0.66<br>above 1M<br>646,914<br>0.17<br>0.66<br>Incomplete round-trip chains:<br>C(N)D<br>2,091,140<br>0.54<br>0.94|-0.11<br>0.05<br>0.36<br>1.50<br>3.55<br>-0.14<br>0.00<br>0.22<br>0.72<br>3.06<br>0.00<br>0.00<br>0.07<br>0.31<br>2.60<br>-0.37<br>0.11<br>0.35<br>1.25<br>3.40<br>-0.14<br>0.00<br>0.22<br>0.72<br>3.06<br>0.00<br>0.34<br>0.97<br>1.98<br>3.72<br>-0.09<br>0.49<br>1.30<br>2.42<br>4.45<br>0.06<br>0.78<br>1.61<br>2.73<br>4.95<br>-0.02<br>0.77<br>1.62<br>2.78<br>5.13<br>-0.06<br>0.79<br>1.71<br>2.96<br>5.56<br>-0.01<br>0.55<br>1.44<br>2.74<br>5.17<br>-0.01<br>0.12<br>0.56<br>1.31<br>3.16<br>-0.01<br>0.10<br>0.43<br>1.01<br>2.90<br>-0.09<br>0.05<br>0.25<br>0.74<br>2.25<br>-0.19<br>0.00<br>0.13<br>0.50<br>1.50<br>-0.21<br>0.00<br>0.12<br>0.42<br>1.37<br>-0.25<br>0.00<br>0.09<br>0.25<br>1.00<br>-0.25<br>0.00<br>0.13<br>0.25<br>0.80<br>-0.15<br>0.08<br>0.35<br>0.85<br>2.00|



Table 3.1: Dealer markup and round-trip transactions 

The table provides a comprehensive overview of dealer markups on round-trip transactions, categorized by various trade types. Our analysis encompasses trading costs across diverse samples, incorporating factors such as trade size and the intricacy of intermediation chains. The C(N)DC sample represents the most extensive dataset, encompassing all round-trips involving a maximum of seven dealers. In contrast, the CDC sample focuses solely on round-trips that transpire without any inter-dealer activity. The foundation for our analysis is the CDC-Nonsplit sample, which incorporates all round-trips absent of both inter-dealer trading and order splitting. It’s important to note that agency trades, where dealers function as client representatives, are excluded from this analysis. All markup figures are expressed as a percentage of the initial purchase price paid by the head dealer to the customer 

44 

porate bonds. The findings are largely consistent with prior research, indicating that these costs tend to be substantial. For overall costs, according to the table, of all the C(N)DC chains, the average round-trip trading cost sits at 0 _._ 63%. Dealers earn an average markup of 0 _._ 42% on non-split round-trips, which increases to 0 _._ 83% for split round-trips. As for the impact of dealer involvement, investor costs demonstrably rise with an increasing number of dealers involved in a round-trip transaction. However, previous research shows that in municipal bond network, the average markups exhibit a monotonic increase, however at a decreasing rate, as more and more dealers get involved in the transaction round-trip chain. In corporate bond dealer network, the trading cost reached the highest when six dealers are involved in the entire process. The average markup starts at 0 _._ 62% with one dealer and climbs to 1 _._ 96% with six dealers in the transaction chain. Meanwhile, the markups charged by dealers to other dealers during dealer to dealer transactions (DD legs) are significantly lower compared to the markups charged to individual investors. Also, variations in markups can be observed. The substantial standard deviations observed highlight the significant variation in dealer markups across different round-trips, even when controlling for factors like the number of dealers in the entire round-trip chain and trade volume. 

In summary, the table reports the trading costs incurred by investors in the corporate bond market. The cost structure exhibits a clear dependence on the number of dealers in the entire round-trip chain and trade volume, with markups declining for larger trades executed through shorter intermediation chains. 

Table 3.1 highlights the significant variability in dealer markups across distinct roundtrip transactions, even when factors like the number of participating dealers and the transaction size are held constant. In the following part, we delve deeper into this observation by demonstrating a systematic relationship between markups and the network centrality of the dealers facilitating the transaction. 

Firstly, we employ univariate comparisons to establish a preliminary confirmation of this connection. Subsequently, we utilize a multivariate regression framework to verify 

45 

that this relationship persists even after controlling for a comprehensive set of explanatory variables. This approach ensures a more robust analysis by accounting for the potential influence of other relevant factors. 

In Table 3.2, dealers are categorized to different tiers, by their centrality in the dealer’s network. Also, transactions are categorized to different groups, by the transaction volumes. The high-centrality dealers are defined as the dealers with top centrality and 25% total transaction volumes in the market. The mid-centrality dealers are defined as the following dealers whose total transaction volume ranks between 25% and 50% in the market. 

Next, we explore the relationship between markups and transaction volumes. Smaller transactions, with a par size below $100,000, are typically associated with retail investors. Transactions categorized as medium institutional lots fall within the range of $100,000 to $1 million. Finally, blocks of $1 million or more are more likely to originate from taxable institutions, encompassing both mutual funds and other entities subject to taxation. 

Table 3.2, Panel A, presents a compelling finding: high-centrality dealers, despite their superior matching efficiency, consistently charge higher trading costs compared to lowcentrality dealers across all trade sizes. This disparity in markups can be as substantial as 200%. For instance, trades in the $25,000 to $49,000 range incur an average markup of 1 _._ 76% at high-centrality dealers, which is triple the 0 _._ 55% markup observed at lowcentrality dealers. While the difference diminishes for larger transactions, it remains statistically significant. Trades exceeding $1 million exhibit a centrality premium of 6 basis points, which is 54% more than the markups charged by low-centrality dealers. 

Further analysis of the entire markup distribution reveals not only a difference in average markups across dealer tiers but also a distinct composition of trades. Low-centrality dealers frequently facilitate round-trip transactions with markups close to zero, often positive but minimal. In contrast, such trades are a rarity for high-centrality dealers. The overall distribution for high-centrality dealers exhibits a rightward shift, indicating a greater prevalence of trades executed at markups significantly above zero. This observation suggests 

46 

Panel A: Trading Costs for Dealers of Different Types 

||Panel A: Trading Costs for Dealers|Panel A: Trading Costs for Dealers|of Different Types|of Different Types|
|---|---|---|---|---|
||Markup Charged by||the Dealer on Average||
||Low Centrality|Mid-Centrality|High-Centrality|Difference Between|
|Transaction Type|Dealers|Dealers|Dealers|High & Low|
|C(N)DC|0.51|0.46|0.72|0.21***|
|CDC|0.47|0.46|1.00|0.53***|
|CDC-Nonsplit|0.33|0.36|0.83|0.50***|
|CDC-Split|0.78|0.52|1.09|0.31***|
|CDC-Nonsplit, grouped by trade volume|||||
|Under 25K|1.14|1.34|2.11|0.97***|
|25K to 49K|0.55|0.87|1.76|1.21***|
|50K to 99K|0.30|0.44|1.06|0.76***|
|100K to 249K|0.15|0.20|0.38|0.23***|
|250K to 499K|0.08|0.15|0.17|0.09***|
|500K to 999K|0.09|0.16|0.17|0.08***|
|Above 1M|0.11|0.19|0.17|0.06***|



Panel B: Trading Loss for Dealers of Different Types 

Dealer’s Probability of Suffering a Loss 

||Low Centrality|Mid-Centrality|High-Centrality|Difference Between|
|---|---|---|---|---|
|Transaction Type|Dealers|Dealers|Dealers|High & Low|
|C(N)DC|2.70|1.97|2.47|-0.23***|
|CDC|3.27|2.21|2.20|-1.07***|
|CDC-Nonsplit|1.56|0.79|0.78|-0.78***|
|CDC-Split|5.02|3.74|3.72|-1.30***|
|CDC-Nonsplit, grouped by transaction volume:|||||
|Under 25K|0.80|0.29|0.45|-0.35***|
|25K to 49K|0.59|0.41|0.58|-0.01***|
|50K to 99K|0.79|0.43|0.69|-0.10***|
|100K to 249K|1.08|0.61|0.77|-0.31***|
|250K to 499K|1.07|0.50|0.49|-0.58***|
|500K to 999K|1.51|0.59|0.57|-0.94***|
|Above 1M|2.32|1.24|1.05|-1.27***|



Table 3.2: Trading cost and dealer centrality: grouped analysis 

This table explores both markups charged by the dealers on average (Panel A) and dealer’s probability of suffering a loss (Panel B) through the lens of the involved dealer’s centrality. We present average markups charged by different dealers on round-trip transactions. The dealers are categorized to different tiers by their calculated centrality. These tiers are constructed by ranking dealers based on their centrality measure, assigning an equal weight to each trade. High-centrality dealers are defined as the dealers within the top 25% centrality. Mid-centrality dealers are defined as those whose centrality, ranks between the top 25% and 50%. Low-centrality dealers are defined as those whose centrality, ranks below 50%. CDC-Nonsplit stands for the core sample that encompasses all round-trips except for interdealer trading and order splitting transactions. CDC stands for the sample that incorporates all round-trips transactions without any inter-dealer activity. C(N)DC stands for the comprehensive dataset that represents all round-trips involving a maximum of seven dealers. 

47 

that it is prevalent for the high-centrality dealers to charge more markups than other dealers. The higher centrality found in high-centrality dealers groups is not the result of some extreme cases. 

Table 3.2, Panel B, explores the frequency of dealer losses on round-trip transactions, categorized by the dealer’s calculated centrality in the dealer network. The data reveals that overall dealer losses count for less than 3% of all trades. Notably, high-centrality dealers exhibit a lower propensity for incurring losses compared to low-centrality dealers. This finding challenges the simplistic notion that high-centrality dealers compensate for a potentially higher risk of losing money by charging wider bid-ask spreads on average. 

In order to control for the potential influence of other round-trip characteristics that may exhibit systematic variations across different groups of transaction sizes or dealer centralities, we conduct multivariate analysis in a similar fashion to Li and Schurhoff 2019. These analysis investigate the impact of dealer centrality and a comprehensive set of explanatory variables on the trading cost _Mi_ associated with each round-trip transaction _i_ , 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0058-04.png)


In the equation above, _αi_ stands for month fixed effects, and _Ci_ the the first principal component derived from a combination of network centrality proxies, _Xi_ stands for the vector of control variables that include transaction information, bond information, and issuer information. 

Dealer markups may not solely reflect the cost of execution. These markups could potentially encompass compensation for various additional services provided by brokerdealers, such as pricing expertise, underwriting participation, and research analysis. Furthermore, both theoretical predictions and empirical evidence, suggest a link between inventory management practices and bid-ask spreads. 

Our primary variable of interest, the first principle component of a set of centrality 

48 

measures, is calculated on a rolling basis over a 30-day window. The coefficient _δ_ serves to quantify the differential impact of dealer network centrality on trading costs. Specifically, it represents the trading cost difference between the most low-centrality dealers (when the centrality’s value is 0) and the most high-centrality dealers (when the centrality measure is 1). 

Table 3.3 consolidates the analysis results, presenting alternative specifications across different columns. In each column, different centrality measures are used to explore the relationship between dealer centrality and dealer markups. In the odd numbered columns, the dealer centrality measure is calculated as the first principal component derived from a set of equally weighted centrality proxies. Conversely, the even numbered columns utilize centrality proxies weighted by transaction volumes in the calculation. The regression analyses are conducted on three distinct trade samples: CDC-Nonsplit, CDC, and C(N)DC. These categories differentiate based on the level of dealer involvement within the round-trip transactions. The results echo the findings of Table 3.2: holding both transaction size and bond characteristics constant, a strong positive relationship emerges between trading costs and dealer centrality. Dealers occupying highly interconnected positions within the network are able to extract significantly higher markups from customers, ranging from 0 _._ 1% to 0 _._ 7% on average. This translates to markups that can be up to double those charged by low-centrality dealers. The final two columns of Table 3.3 reinforce the observations from Table 3.1: costs demonstrably increase with a growing number of dealers involved in the intermediation chain. However, this cost escalation is mitigated by the presence of a more central head dealer. 

49 

||CDC-Nonsplit<br>Equal Weighted<br>Value weighted<br>(1)<br>(2)|CDC<br>Equal Weighted<br>Value weighted<br>(3)<br>(4)|C(N)DC|
|---|---|---|---|
||||Equal Weighted<br>Value weighted<br>(5)<br>(6)|
|Dealer Centrality<br>Chain length<br>Chain length*Centrality<br>Dealer Inventory<br>log(Par)*Small<br>log(Par)*Medium<br>log(Par)*Large<br>Maturity<br>Seasoning<br>Issue Size<br>Rating<br>Unrated<br>MTN<br>Asset-backed<br>Yankee<br>Rule144<br>Fungible<br>R2|0.044***<br>0.013***<br>-0.019***<br>-0.015***<br>-0.412***<br>-0.426***<br>-0.263***<br>-0.265***<br>-0.195***<br>-0.197***<br>0.199***<br>0.198***<br>0.084***<br>0.085***<br>-0.104***<br>-0.103***<br>0.015***<br>0.015***<br>-0.136***<br>-0.151***<br>0.064***<br>0.063***<br>-0.197***<br>-0.196***<br>-0.030***<br>-0.034***<br>-0.046***<br>-0.044***<br>-0.052***<br>-0.053***<br>0.311<br>0.307|0.057***<br>0.018***<br>-0.046***<br>-0.041***<br>-0.464***<br>-0.483***<br>-0.319***<br>-0.325***<br>-0.244***<br>-0.249***<br>0.277***<br>0.275***<br>0.102***<br>0.101***<br>-0.099***<br>-0.095***<br>0.029***<br>0.030***<br>-0.381***<br>-0.401***<br>0.007***<br>0.004<br>-0.255***<br>-0.257***<br>-0.006***<br>-0.014***<br>-0.081***<br>-0.081***<br>0.041***<br>-0.053***<br>0.307<br>0.302|0.103***<br>0.075***<br>0.325***<br>0.353***<br>-0.026***<br>-0.030***<br>-0.034***<br>-0.027***<br>-0.450***<br>-0.463***<br>-0.271***<br>-0.278***<br>-0.227***<br>-0.232***<br>0.372***<br>0.369***<br>0.109***<br>0.107***<br>-0.127***<br>-0.120***<br>0.032***<br>0.032***<br>-0.411***<br>-0.424***<br>0.001<br>-0.005*<br>-0.338***<br>-0.337***<br>-0.008***<br>-0.017***<br>-0.175***<br>-0.174***<br>-0.071***<br>-0.070***<br>0.329<br>0.331|



Table 3.3: Trading cost and dealer centrality 

The table explores the key factors influencing trading costs in the bond dealer network. The analysis encompasses a comprehensive set of explanatory variables, categorized as follows: Dealer Characteristics include variables that capture the characteristics of the dealers involved in the transaction, such as their network centrality. The table presents estimates using both equal-weighted and value-weighted versions of this centrality measure across separate columns. Trade Characteristics include variables that describe the specific features of the round-trip transaction itself, such as the presence or absence of interdealer activity. Issue Characteristics include variables that capture the characteristics of the specific bond being traded, such as its size or maturity. 

50 

|Dealer Centrality and Dealer’s Position in the Transaction Round-trip Chain|Chain Type<br>N<br>#1<br>#2<br>#3<br>#4<br>#5<br>#6<br>#7|CDC<br>1,729,241<br>0.29<br>.<br>.<br>.<br>.<br>.<br>.|.<br>.<br>.<br>.<br>.<br>.|CDDC<br>359,376<br>0.32<br>0.27<br>.<br>.<br>.<br>.<br>.|(-0.05***)<br>.<br>.<br>.<br>.<br>.|CDDDC<br>303,226<br>0.25<br>0.35<br>0.22<br>.<br>.<br>.<br>.|(0.10***)<br>(-0.03***)<br>.<br>.<br>.<br>.|CDDDDC<br>123,549<br>0.21<br>0.33<br>0.39<br>0.16<br>.<br>.<br>.|(0.12***)<br>(0.18***)<br>(-0.05***)<br>.<br>.<br>.|CDDDDDC<br>53,189<br>0.18<br>0.34<br>0.31<br>0.40<br>0.13<br>.<br>.|(0.16***)<br>(0.13***)<br>(0.22)<br>(-0.05***)<br>.<br>.|CDDDDDDC<br>12,231<br>0.18<br>0.34<br>0.32<br>0.31<br>0.43<br>0.13<br>.|(0.16***)<br>(0.14**)<br>(0.13*)<br>(0.25***)<br>(-0.05***)<br>.|CDDDDDDDC<br>4,618<br>0.16<br>0.38<br>0.30<br>0.33<br>0.31<br>0.42<br>0.12|(0.22***)<br>(0.16***)<br>(0.17***)<br>(0.15***)<br>(0.26***)<br>(-0.04***)|Table 3.4: Transaction chains|This table explores the dealer centrality and dealer’s position in the transaction round-trip chains. Dealer centrality is calculated using|the frst principal component derived from a set of centrality proxies. These proxies are then standardized using the empirical cumulative|distribution function (cdf). The higher the centrality is, the more central the dealer is in the network.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|



51 

## 3.3.2 Dealer Topological Characteristics and Transaction Partner Preference 

In the previous part, we explore the relationship between dealer network topology characteristics and dealer’s markup. In this section, we explore a crucial question: do these differences in the dealer’s topology characteristics have an influence in their ability to find a transaction partner and eventually find a individual investor for the bond? If this is true, the variation in the markups can be explained by this relationship, and a potential trade-off between transaction speed and transaction cost should be observed. 

To explore the connection between dealer topology characteristics and transaction partner preferences, we conducted the following analysis. First, using Probit regression, we investigate the relationship between a dealer’s centrality and their choice of transaction counterparty, whether another dealer or an individual investor. Next, we examine the relationship between a dealer’s centrality and the total length of the transaction chain. Lastly, to validate the findings of the first two steps, we calculate the average dealer centrality for each position in transaction chains of varying lengths and checked if the results were consistent with our initial analysis. 

To initiate our investigation, we will estimate a panel Probit model. This model will analyze the propensity of dealers to execute trades directly with investors as opposed to selling to other dealers, assuming a trade has already taken place. 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0062-05.png)


In the equation above, Φ is the cumulative distribution of the standard normal distribution, _αi_ stands for month fixed effects, and _Ci_ the first principal component derived from a combination of network centrality proxies, _Xi_ stands for the vector of control variables that include transaction information, bond information, and issuer information. 

Table 3.5 presents the findings from the first two steps of our analysis. The first two columns of this table examine whether a dealer chooses to trade with another dealer or an 

52 

||Probability of Selling<br>to a Investor<br>Equal Weighted<br>Value weighted<br>(1)<br>(2)|Number of dealers involved in the transactions|Number of dealers involved in the transactions|
|---|---|---|---|
|||OLS<br>Equal Weighted<br>Value weighted<br>(3)<br>(4)|Poisson|
||||Equal Weighted<br>Value weighted<br>(5)<br>(6)|
|Dealer Centrality<br>Dealer Inventory<br>log(Par)*Small<br>log(Par)*Medium<br>log(Par)*Large<br>Maturity<br>Seasoning<br>Issue Size<br>Rating<br>Unrated<br>MTN<br>Asset-backed<br>Yankee<br>Rule144<br>Fungible|0.103***<br>0.039***<br>0.053***<br>0.032***<br>0.044***<br>0.054***<br>0.054***<br>0.059***<br>0.075***<br>0.084***<br>0.018***<br>0.020***<br>-0.080***<br>-0.078***<br>0.012***<br>0.008***<br>-0.001***<br>-0.001***<br>0.172***<br>0.174***<br>-0.058***<br>-0.054***<br>0.145***<br>0.157***<br>0.021***<br>0.031***<br>0.027***<br>0.285***<br>-0.010***<br>-0.010***|-0.025***<br>-0.004***<br>-0.050***<br>-0.059***<br>-0.467***<br>-0.455***<br>-0.120***<br>-0.115***<br>-0.122***<br>-0.118***<br>-0.037***<br>-0.036***<br>0.053***<br>0.056***<br>-0.06***<br>-0.068***<br>0.009***<br>0.009***<br>-0.392***<br>-0.371***<br>0.033***<br>0.036***<br>-0.448***<br>-0.447***<br>0.019***<br>0.023***<br>-0.311***<br>-0.312***<br>-0.039***<br>-0.039***|-0.009***<br>-0.002***<br>-0.020***<br>-0.023***<br>-0.169***<br>-0.164***<br>-0.043***<br>-0.041***<br>-0.046***<br>-0.045***<br>-0.014***<br>-0.014***<br>0.020***<br>0.021***<br>-0.021***<br>-0.023***<br>0.003***<br>0.003***<br>-0.156***<br>-0.149***<br>0.010***<br>0.011***<br>-0.188***<br>-0.187***<br>0.007***<br>0.008***<br>-0.136***<br>-0.136***<br>-0.014***<br>-0.014***|



Table 3.5: Dealer centrality, transaction chain length, and dealer’s ability to locate trading counterparty 

The table investigates the relationship between dealer network centrality and two key aspects of their trading behavior: Customer vs. Dealer Interactions and Intermediation Chain Length. The first two columns explores the relationship between a dealer’s probability of selling bonds directly to investors and dealer’s network centrality, using Probit regression. Column (3), (4), (5) and (6) explores the relationship between dealer’s centrality and length of the transaction round-trip chains with OLS regression and Poisson regression. 

53 

individual customer. When controlling for all other variables, dealer centrality exhibits a positive coefficient. Remembering that a centrality value of 0 indicates the least central dealer and 1 the most central, this suggests that dealers with higher centrality are more likely to trade directly with individual investors, while those with lower centrality tend to trade other dealers. Based on this result, we hypothesize that high-centrality dealers may shorten the overall length of transaction chains. We will validate this hypothesis in the next step of our analysis. 

In the remaining four columns of Table 3.5, we explore the connection between transaction round-trip chain length and dealer’s centrality, in column (3), (4) and column (5), (6), using the following regression: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0064-03.png)


In columns (3) and(4) of Table 3.5, OLS regressions are used. In columns (5) and (6) Poisson regressions are used to explore the connection between transaction round-trip chain length and dealer’s centrality. 

The results show a negative correlation between the length of intermediation and the centrality of the head dealer across all specifications. This indicates that transaction chains tend to be shorter when the head dealer has higher centrality. This finding aligns with the results from columns (1) and (2), which suggests that dealers with higher centrality are more likely to trade with individual investors, potentially concluding the transaction chain earlier. 

Finally, we present the average dealer centrality for dealers in different positions within transaction chains of varying lengths, as shown in Table 3.4. We observe a pattern of bonds flowing from the periphery dealers towards the network’s central dealers and then returns back to peripheral dealers. Interestingly, dealers positioned in the middle of a chain exhibit a higher degree of centrality compared to both the dealer initially acquiring the bond from a individual investor and the dealer eventually selling it to another individual investor. For 

54 

longer trade types, dealer centrality reaches its peak with the second and second to last dealers in the chain. This observation suggests that high-centrality dealers function as hubs, actively intermediating to facilitate the flow of bonds within the network. 

Combining the findings from the whole table, we can conclude that, when peripheral dealers acquire bonds from individual investors, they tend to sell the bond to central dealers who serve as hubs in the entire bond dealer network. When central dealers fail to find an individual investor to dump the bond, they sell the bond to other dealers who can likely find a buyer. In conclusion, these findings suggest that high-centrality dealers may be more efficient at facilitating transactions within the network, potentially by leveraging their extensive connections or possessing superior knowledge of investor demand. 

## 3.3.3 Dealer Topological Characteristics and Prearranged Transaction 

Dealers in the over-the-counter bond network act as intermediaries by purchasing bonds from one party and selling them to another. In some cases, a dealer buys a bond when an investor wishes to sell and holds the bond in inventory if no immediate buyers are available. In other cases, the dealer functions purely as a matchmaker, buying a bond from an investor and selling it immediately to another. The first type of transaction is known as a principal trade, while the second type is referred to as a prearranged trade. 

In this part, we explore the relationship between dealer centrality and prearrange transactions using a multivariate Probit model. This model includes various dealer, trade, and bond characteristics as explanatory factors to analyze prearrange transactions. 

In columns (1) and (2) of Table 3.6, the response variable is defined as whether this transaction is a pre-arranged transaction with the same timestamp. In columns (3) and (4) of Table 3.6, the response variable is defined as whether this transactions is a pre-arranged transaction within the same day. 

Table 3.6 delves into the relationship between dealer centrality and the propensity to prearrange trades, which translates to potentially slower execution for sellers. The results 

55 

||Prearranged, Same-minute<br>Round-Trip<br>Equal Weighted<br>Value weighted<br>(1)<br>(2)|Prearranged, Same-Day<br>Round-Trip|
|---|---|---|
|||Equal Weighted<br>Value weighted<br>(3)<br>(4)|
|Dealer Centrality<br>Dealer Inventory<br>log(Par)*Small<br>log(Par)*Medium<br>log(Par)*Large<br>Maturity<br>Seasoning<br>Issue Size<br>Rating<br>Unrated<br>MTN<br>Asset-backed<br>Yankee<br>Rule144<br>Fungible|-0.121***<br>-0.065***<br>-0.045***<br>-0.043***<br>0.168***<br>0.190***<br>0.156***<br>0.163***<br>0.107***<br>0.114***<br>-0.123***<br>-0.117***<br>-0.016***<br>-0.019***<br>0.067***<br>0.071***<br>0.005***<br>0.006***<br>-0.200***<br>-0.192***<br>-0.068***<br>-0.065***<br>0.255***<br>0.260***<br>0.327***<br>0.347***<br>0.081***<br>0.082***<br>0.023***<br>0.024***|-0.186***<br>-0.100***<br>-0.036***<br>-0.023***<br>0.149***<br>0.195***<br>0.121***<br>0.136***<br>0.150***<br>0.165***<br>-0.006***<br>0.004***<br>0.020***<br>0.014***<br>-0.813***<br>-0.075***<br>0.016***<br>0.018***<br>-0.382***<br>-0.363***<br>0.004<br>0.008*<br>0.195***<br>0.211***<br>0.211***<br>0.235***<br>-0.016***<br>-0.009**<br>0.002***<br>0.004***|



Table 3.6: Prearranged transactions and dealer centrality 

The table investigates the key factors influencing the occurrence of prearranged trades compared to principal trades. The analysis employs panel regressions, controlling for both state-specific effects and seasonal variations through month fixed effects. The response variable is a binary indicator, taking a value of 1 for prearranged trades and 0 for principal trades. This allows us to identify the variables that are statistically associated with a higher likelihood of a trade being prearranged. The table presents estimates using both equalweighted and value-weighted versions of this centrality measure across separate columns. Trade Characteristics category includes variables that describe the specific features of the round-trip transaction itself. Issue Characteristics includes variables that capture the characteristics of the specific bond being traded. 

56 

consistently reveal that high-centrality dealers are less likely to have pre-arranged transactions compared to low-centrality dealers across all specifications. This observation suggests that high-centrality dealers prioritize providing immediacy to investors. They are more inclined to commit capital by taking bonds into their inventory to facilitate faster execution, analogous to how market orders function in equity markets. Conversely, interacting with a peripheral dealer bears a greater resemblance to submitting a limit order, potentially resulting in execution delays. Furthermore, the table highlights a positive correlation between large dealer inventory holdings and the likelihood of principal trades (where the dealer takes the bond into inventory), as would be expected. The analysis of bond characteristics also yields generally consistent findings. Less risky and larger bonds tend to be less likely involved in a pre-arranged transaction, suggesting that sellers are less sensitive to potential execution delays for these type of bonds. 

## 3.3.4 Dealer Topological Characteristics and Dealer Losses 

Which type of dealer is more prone to losses in the bond market? Intuitively, central dealers might seem less likely to face losses given their dominant positions and their ability to capitalize on transactions with peripheral dealers. However, there is an argument that central dealers incur higher markups to compensate for the risks involved in intermediating bonds, potentially increasing their risk of losses during the intermediation process. This section investigates the probability of dealers experiencing losses in round-trip transactions. 

We investigate this question in Table 3.7 using a multivariate Probit model. This model includes various dealer, trade, and bond characteristics as explanatory factors to analyze the determinants of trading losses. The results show that the centrality coefficient is negative, indicating that dealers with high centrality have a significantly lower probability of incurring losses on round-trip transactions compared to those with low centrality. 

57 

|Determinant|CDC-Nonsplit<br>Equal Weighted<br>Value weighted<br>(1)<br>(2)|CDC<br>Equal Weighted<br>Value weighted<br>(3)<br>(4)|C(N)DC|
|---|---|---|---|
||||Equal Weighted<br>Value weighted<br>(5)<br>(6)|
|Dealer Centrality<br>Chain length<br>Chain length*Centrality<br>Dealer Inventory<br>log(Par)*Small<br>log(Par)*Medium<br>log(Par)*Large<br>Maturity<br>Seasoning<br>Issue Size<br>Rating<br>Unrated<br>MTN<br>Asset-backed<br>Yankee<br>Rule144<br>Fungible|-0.089***<br>-0.059***<br>-0.034***<br>-0.025***<br>0.003<br>0.016<br>0.001<br>-0.001<br>0.035***<br>0.030***<br>0.030***<br>0.026***<br>-0.038***<br>-0.034***<br>0.108***<br>0.099***<br>-0.002***<br>-0.004***<br>0.582***<br>0.594***<br>-0.037<br>-0.037***<br>-0.367***<br>-0.379***<br>-0.053***<br>-0.077***<br>-0.018***<br>-0.019*<br>0.045***<br>0.043***|-0.068***<br>-0.050***<br>-0.047***<br>-0.036***<br>0.045***<br>0.037***<br>0.060***<br>0.056***<br>0.034***<br>0.029***<br>0.071***<br>0.067***<br>-0.084***<br>-0.080***<br>0.226***<br>0.218***<br>-0.005***<br>-0.007***<br>0.652***<br>0.667***<br>0.005<br>0.005<br>-0.435***<br>-0.448***<br>-0.049***<br>-0.059***<br>-0.016***<br>-0.018***<br>0.043***<br>0.041***|-0.014***<br>-0.026***<br>-0.038***<br>-0.017***<br>0.027***<br>0.011***<br>-0.046***<br>-0.038***<br>0.061***<br>0.055***<br>0.060***<br>0.056***<br>0.037***<br>0.032***<br>0.077***<br>0.073***<br>-0.086***<br>-0.083***<br>0.230***<br>0.223***<br>-0.003***<br>-0.005***<br>0.597***<br>0.608***<br>0.011*<br>0.010***<br>-0.413***<br>-0.425***<br>-0.039***<br>-0.049***<br>-0.010***<br>-0.013***<br>0.046***<br>0.045***|



Table 3.7: Dealer loss probability and dealer centrality 

The table investigates the factors influencing the likelihood of dealers incurring losses on round-trip transactions. The results are derived from Probit regression. The analysis incorporates a range of explanatory variables: Dealer Characteristics category includes variables that capture the attributes of the dealers involved, such as their network centrality. The centrality measure employed is the first principal component derived from a combination of network centrality proxies. The table presents estimates using both equal-weighted and value-weighted versions of this centrality measure across separate columns. Trade Characteristics category includes variables that describe the specific features of the round-trip transaction itself. Issue Characteristics includes variables that capture the characteristics of the specific bond being traded. 

58 

## 3.3.5 Dealer Topological Characteristics and Inventory Time 

In this part, we examine the potential relationship between dealer centrality and inventory holding time. Central dealers, who act as hubs within the dealer network, acquire bonds from peripheral dealers and subsequently sell them to other dealers or investors. This raises questions about the intermediation process: Does it require more time for central dealers to find suitable buyers? Do central dealers need more time to intermediate bonds? Table 3.9 explores the link between inventory holding time and various factors, including measures of dealer centrality, trade characteristics, bond characteristics, and dealer attributes. 

The results indicate that central dealers typically have shorter inventory holding times and faster inventory turnover compared to dealers with lower centrality across all types of transaction chains. Given this finding, it naturally leads to the question: What are the inventory holding times for dealers in different positions within various transaction chains? 

Table 3.8 shows the holding periods for dealers in different transaction chains. Focusing on Panel A, a consistent pattern emerges across all chain lengths: the final dealer in the chain (the one that directly sells the bond to the individual investor) consistently earns the highest markup, averaging around 0.7%. This indicates that the final step in the intermediation process is a crucial profit center for dealers. However, Panel B reveals that while the dealer that directly sells the bond to the investor receives the highest markup, they do not hold the bond in inventory for the longest period. 

This finding suggests that the ability of dealers to efficiently find individual investors for the bonds is more crucial in achieving higher markups. Holding the bond in inventory and assuming the associated risk is not the primary factor driving higher dealer markups. 

Table 3.9 explores the relationship between inventory holding time and various variables, including dealer centrality measure, trade characteristics, bond characteristics and dealer characteristics. 

Our findings reveal a connection between liquidity provision and inventory risk-taking for high-centrality dealers. By assuming this risk, high-centrality dealers offer increased 

59 

Panel A: Markup charged by dealers in trading round-trip chains 

|||Dealer position|Dealer position|v.s. Dealer Markup|v.s. Dealer Markup|v.s. Dealer Markup|||
|---|---|---|---|---|---|---|---|---|
||Total|Investor||||||Investor|
|Transaction Chains|Markup|Sell|2|3|4|5|6|Buy|
|CDC|0.61|.|.|.|.|.|.|.|
|CDDC|1.30|0.53|.|.|.|.|.|0.77|
|CDDDC|1.58|0.50|0.38|.|.|.|.|0.70|
|CDDDDC|1.88|0.51|0.40|0.26|.|.|.|0.71|
|CDDDDDC|1.85|0.45|0.34|0.29|0.15|.|.|0.62|
|CDDDDDDC|1.88|0.45|0.11|0.39|0.20|0.08|.|0.65|
|CDDDDDDDC|1.54|0.34|0.10|0.07|0.21|0.12|0.09|0.61|



Panel B: Inventory time by dealers in trading round-trip chains 

|||Number|of Days|in Dealer Inventory|in Dealer Inventory|in Dealer Inventory|||
|---|---|---|---|---|---|---|---|---|
||Total|Investor||||||Investor|
|Transaction Chains|Days|Sell|2|3|4|5|6|Buy|
|CDC|1.05|.|.|.|.|.|.|.|
|CDDC|1.93|1.27|.|.|.|.|.|0.66|
|CDDDC|2.32|0.77|1.08|.|.|.|.|0.47|
|CDDDDC|2.55|0.49|1.03|0.81|.|.|.|0.22|
|CDDDDDC|2.86|0.31|0.78|1.06|0.51|.|.|0.20|
|CDDDDDDC|3.59|0.33|0.42|1.29|0.87|0.51|.|0.17|
|CDDDDDDDC|3.98|0.29|0.40|0.61|1.32|0.67|0.47|0.22|



Table 3.8: Dealer markups and dealer inventory holding time 

Panel A explores the total markup charged by dealers on different positions in the roundtrip transactions, categorized by the level of dealer involvement. The table presents a breakdown of these markups across two dimensions: The rows represent the number of dealers involved in the intermediation process (round-trip chain length); The columns represent each individual dealer participating in the sequence. Markup figures are expressed as a percentage of the initial purchase price paid by the first dealer to the customer. It’s important to note that this analysis is restricted to non-split round-trip transactions, and no further data filtering has been applied. Panel B focuses on the average inventory holding period for dealers throughout the round-trip chain. 

60 

||Non-Split CDC Chains<br>Equal Weighted<br>Value weighted<br>(1)<br>(2)|CDC Chains<br>Equal Weighted<br>Value weighted<br>(3)<br>(4)|C(N)DC Chains|
|---|---|---|---|
||||Equal Weighted<br>Value weighted<br>(5)<br>(6)|
|Dealer Centrality<br>Dealer Inventory<br>log(Par)*Small<br>log(Par)*Medium<br>log(Par)*Large<br>Maturity<br>Seasoning<br>Issue Size<br>Rating<br>Unrated<br>MTN<br>Asset-backed<br>Yankee<br>Rule144<br>Fungible|-0.845***<br>-0.426***<br>0.091***<br>0.085***<br>-1.35***<br>-1.601***<br>-1.02***<br>-1.081***<br>-0.749***<br>-0.807***<br>-0.008<br>-0.056***<br>0.304***<br>0.336***<br>-0.047***<br>-0.076***<br>-0.048***<br>-0.053***<br>1.271***<br>1.175***<br>-0.138***<br>-0.151***<br>-0.137<br>-0.166<br>-1.153***<br>-1.29***<br>0.316***<br>0.301***<br>-0.011<br>-0.032|-0.625***<br>-0.344***<br>0.129***<br>0.100***<br>-0.467***<br>-0.629***<br>-0.427***<br>-0.487***<br>-0.543***<br>-0.601***<br>0.048***<br>0.012**<br>-0.071***<br>-0.050***<br>0.330***<br>0.308***<br>-0.050***<br>-0.056***<br>1.334***<br>1.272***<br>-0.021<br>-0.032*<br>-0.744***<br>-0.799***<br>-0.699***<br>-0.781***<br>0.100***<br>0.075***<br>0.016<br>0.009|-0.309***<br>-0.209***<br>0.070***<br>0.051***<br>-0.989***<br>-1.016***<br>-0.520***<br>-0.533***<br>-0.603***<br>-0.624***<br>-0.002<br>-0.011**<br>0.015***<br>0.033***<br>0.240***<br>0.220***<br>-0.022***<br>-0.026***<br>0.372***<br>0.376***<br>0.105***<br>0.113***<br>-1.285***<br>-1.309***<br>-0.534***<br>-0.569***<br>-0.359***<br>-0.377***<br>-0.007<br>-0.006|



Table 3.9: Dealer centrality and holding periods 

The table delves into the factors influencing the duration of dealer inventory holding periods. The estimates are derived from panel Tobit regressions, a statistical technique suited for analyzing censored data with a lower limit of zero (inventory cannot be negative). The analysis explores a range of explanatory variables: Dealer Characteristics category includes variables that capture the attributes of the dealers involved, such as their network centrality. The centrality measure employed is the first principal component derived from a combination of network centrality proxies. The table presents estimates using both equal-weighted and value-weighted versions of this centrality measure across separate columns. Trade Characteristics category includes variables that describe the specific features of the roundtrip transaction itself. Issue Characteristics category includes variables that capture the characteristics of the specific bond being traded. 

61 

immediacy to investors seeking swift execution. However, the higher markup charged by high-centrality dealers cannot be explained by the assumption of higher inventory holding costs. High-centrality dealers demonstrate a greater propensity to take on inventory risk, yet they also exhibit a faster inventory turnaround compared to low-centrality dealers. This suggests that factors beyond just holding costs may contribute to the centrality premium 

## **3.4 Conclusion** 

In this chapter, we investigate how the topological characteristics of dealers influence their trading behavior in the bond market. This includes aspects such as the trading costs imposed by dealers, the length of time dealers hold inventory, their losses, pre-arranged transactions, and their preferences when selecting transaction partners. Our findings indicate that the topological characteristics of dealers indeed affect their trading behaviors. Dealers with high centrality tend to: (1) impose higher trading costs compared to other dealers; (2) show a preference for conducting transactions with other dealers over individual customers; (3) have a lower likelihood of incurring losses from transactions; and (4) show a greater preference to keep bonds in their inventory than other dealers. 

62 

## **CHAPTER 4** 

## **TEMPORAL GRAPH NEURAL NETWORK LINK PREDICTION** 

In this chapter, our goal is to forecast bond transaction patterns using a temporal graph neural network (GNN) model. We use this model to analyze the network generated from bond transaction data. We aim to predict the probability of future transactions between specific pairs of dealers using link prediction techniques. 

Traditionally, link prediction methods have focused on static networks. Prior approaches typically either (1) combine all interactions between nodes into a single static graph or (2) depict the graph as a series of discrete snapshots taken at regular intervals, with each snapshot containing aggregated data for that period. These methods often result in the loss of valuable temporal information during the aggregation process. 

Recent advancements have been made with continuous-time dynamic GNNs, which incorporate the time dimension and preserve temporal information. However, these models generally represent each node with a single vector and base interaction predictions on the inner product of two such vectors, neglecting the structural intricacies of the nodes’ local neighborhoods. 

To overcome these limitations, we introduce a novel continuous-time dynamic GNN model specifically designed for predicting interactions in temporal graphs. Our model is capable of (1) incorporating timestamp information and (2) capturing the structural patterns of local neighborhoods, addressing the critical gaps in previous modeling approaches. 

## **4.1 Introduction** 

Recent years have seen great advances in the application of link prediction techniques across various financial sectors, such as fraud detection, anti-money laundering, and cryptocurrency transaction forecasting. Yet, problems involving the prediction of future trans- 

63 

actions between dealers have not been extensively explored. The ability to forecast trading behaviors plays a crucial role in signaling potential risks in the bond market, mitigating the spread of risk, and preventing losses associated with high-risk entities. This is because risks associated with transactions can spread through the network of dealers. In instances where a financial institution experiences a liquidity crisis, the ensuing risk can propagate through transactions to other parties, potentially leading to a cascading effect that culminates in a systemic crisis. Thus, it’s vital to develop early warning systems for risk dissemination and to understand the pathways through which risk may spread in future bond transactions. This chapter delves into the challenge of predicting trading behaviors in the over-the-counter bond market. 

GNNs have demonstrated remarkable success in link prediction tasks for static graphs. However, in temporal contexts, initial approaches employ discrete-time GNNs, which conceptualize temporal graphs as series of snapshots. This approach has limitations in capturing the dynamic correlations between consecutive snapshots and often overlooks historical data. Although recent advancements have introduced continuous-time GNN methods, most rely on node-centric approaches, which do not capture edge relationships as effectively as subgraph-centric methods. To address these gaps, we introduce a novel continuous-time GNN model that is aware of local structures, specifically designed for link prediction in temporal settings. 

Our model works with continuous-time temporal graphs, represented by sequences of timestamped events, enabling the prediction of future links as the network evolves. It includes a memory component to record the activity history of each node. Unlike traditional discrete-time methods, which do not leverage temporal information effectively, our model encodes timestamps using Fourier features alongside learnable features, a technique proven to be efficient. Additionally, it constructs features to represent local neighborhood structures, thereby overcoming the limitations of node-based methods that produce identical vector representations for structurally distinct nodes. 

64 

In conclusion, we propose a strategy for predicting transactions in the over-the-counter (OTC) bond market within a temporal framework. By building a temporal network of bond transactions and applying a continuous-time GNN model, we capture the dynamic nature of bond activities. We validate our method through comprehensive experiments on our corporate bond transaction data . 

## **4.2 Related Work** 

In this section, we review previous works on link prediction and graph neural network. 

## 4.2.1 Notations and Problem Formulation 

In a static graph with _N_ nodes, let _vi_ denote a node _i_ and _eij_ denote an edge connecting node _i_ and _j_ . Then the set of nodes can be written as _V_ = _{v_ 1 _, v_ 2 _, ..., v|N |}_ , and the set of edges can be written as _E ⊆ V × V_ . Consequently, the graph can be represented as _G_ = ( _V, E_ ). Furthermore, _sij_ represents the similarity score of node _i_ and node _j_ . Γ _i_ denotes the set of neighboring nodes of node _i_ , _l_ stands for the number of random walk steps, _L_ stands for Laplacian matrix, _S_ stands for similarity matrix, _A_ stands for adjacency matrix and _πij_ is the probability of a walker starting from node _i_ and stopping at node _j_ . In a continuous-time temporal graph, unlike discrete-time temporal graphs which slice the dataset into sequences of snapshots on regular interval basis, continuous-time temporal graphs offer a more fine-grained framework and can be depicted as series of events marked with timestamps. These events include the addition or removal of nodes, the creation or deletion of edges, and updates to node attributes. Our continuous-time temporal graph is modeled as _G_ = _{x_ ( _t_ 1) _, x_ ( _t_ 2) _, ...}_ representing node events / edge events / attributes updates at time _{_ 0 _≤ t_ 1 _≤ t_ 2 _≤ ...}_ . A node event for node _i_ is represented by _vi_ ( _t_ ), where _i_ is the index of the node, and _v_ is the vector representation of the event. If the index _i_ shows up for the first time, this event means a new node _i_ is added to the existing graph. An edge event between node _i_ and _j_ at time _t_ in a temporal graph is denoted as _eij_ ( _t_ ). 

65 

## 4.2.2 Deep Learning on Static Graphs 

Recurrent graph neural networks are among the foundational works in the field of GNN. Due to limitations in computing resources, early studies primarily concentrated on directed acyclic graphs (Micheli et al. 2004; Sperduti and Starita 1997). An early graph neural network model introduced by Scarselli et al. 2008 expanded upon previous recurrent models to accommodate various graph structures, including cyclic, directed, and undirected graphs. Utilizing a mechanism of information diffusion, this model recurrently updates node states through the exchange of information within their neighborhoods until a stable equilibrium is achieved. The hidden state of node _vi_ is recurrently updated by _h[t] i_[=][�] _j∈_ Γ _i[f]_[(] _[v][i][, v][j][, e][ij][, h] v_[(] _[t] j[−]_[1)] ), where _f_ ( _·_ ) is a parametric function, and _h_[0] _j_[is initialized] randomly. In this model, the summation operation is applied uniformly across all nodes, regardless of variations in the number of neighbors and without any known order in the neighborhood. Another variant of recurrent graph neural networks is the Gated Graph Neural Network, which incorporates a gated recurrent unit (GRU) to limit the recurrence to a fixed number of steps. This approach eliminates the need to restrict parameters to achieve convergence. In this model, a node’s hidden state is updated based on its previous hidden states and those of its neighbors, according to _h[t] i_[=] _[ GRU]_[(] _[h][t] i[−]_[1] _,_[�] _j∈_ Γ _i[Wh] j[t][−]_[1] ) 

Convolutional graph neural networks (GNNs) are intimately connected to recurrent graph neural networks, yet they diverge in their approach to managing node states and dependencies. Unlike recurrent GNNs, which iterate node states under contractive conditions, convolutional GNNs tackle the issue of cyclic dependencies through a structured architecture that employs a predefined number of layers, each with its own set of weights. This method of graph convolution stands out for its efficiency and convenience, leading to its widespread adoption and growth in recent times. Convolutional GNNs fall into two primary categories: spectral-based and spatial-based. Spectral-based models utilize the principles of graph signal processing, defining graph convolutions through filters that aim to cleanse graph signals of noise. In contrast, spatial-based models draw inspiration from 

66 

the mechanisms of recurrent GNNs, establishing graph convolutions through the propagation of information across nodes. Due to their enhanced efficiency and adaptability, spatial-based approaches have outpaced spectral-based methods in popularity. 

## 4.2.3 Dynamic Graph Neural Network 

Dynamic Graph Neural Network is a rapidly developing research area. It can be divided into discrete-time and continuous-time dynamic graphs (Kazemi, Goel, Jain, et al. 2020, Rossi et al. 2020, Kazemi 2022, Wu, Cui, Pei, and Zhao 2022). 

A discrete-time dynamic graph is a sequence of snapshots taken from a dynamic graph, and the snapshots are usually sampled at regularly-spaced time intervals. According to actual needs the time granularity (time interval) can be set to hours, days or months, etc. However, DTDG may lose information in the original graph, as the graph events in the time period are aggregated into a static graph. DTDG can be represented as a series of graph snapshots: _G_ = _{G_ ( _t_ 1) _, G_ ( _t_ 2) _, ..., G_ ( _tn_ ) _}_ , where _n_ is the number of snapshots. Employing a discrete representation of the dynamic network enables the application of static network analysis techniques on each snapshot. By consistently applying these static methods to each snapshot, insights into the network’s dynamics can be gathered. To ensure smoother transitions between snapshots, techniques like overlapping snapshots, such as sliding time windows, are often used in dynamic network analysis to minimize abrupt changes from one network snapshot to another. 

A continuous-time dynamic graph can be viewed as a series of timed events encompassing various activities within the graph, such as adding or deleting nodes and edges, as well as transformations of node or edge features. There are primarily two types of representations for continuous-time dynamic graphs: the event-based graph and the contact sequence. The event-based representation captures the time intervals during which an edge in the graph is active, making it a suitable approach for dynamic networks that emphasize the duration of links. And the representation can be written as _G_ = _{x_ ( _t_ 1 _,_ ∆1) _, x_ ( _t_ 2 _,_ ∆2) _, ...}_ , 

67 

where _tk_ is the timestamp for event _k_ and ∆ _k_ is the duration of the event. A good example of an event-based representation in continuous-time dynamic graphs is mobile phone networks, where researchers are interested not only in the timestamp when a call is initiated ( _tk_ ) but also in the duration of the call (∆ _k_ ). Another representation for continuous-time dynamic graphs is the contact sequence representation, which simplifies the event-based model and focuses only on the timestamp when the event is initiated. In a contact sequence, connections are considered instantaneous, meaning that no duration is specified for any link. It can be modeled as a list of events with timestamps, _G_ = _{x_ ( _t_ 1) _, x_ ( _t_ 2) _, ...}_ , where _x_ ( _tk_ ) represents a event happened at time _tk_ . Since an edge in the dealer network represents a transaction that is instantaneous and has no link duration, contact sequence representation is more suitable for the temporal dealer network. 

Typically, discrete-time dynamic models are combined with sequence models (usually RNNs) in the following manner: GNN models capture the node neighborhood connection and create vector representations for the node, then the node representations are fed to RNN models, which capture the graph evolution. Seo et al. 2018 first combined Graph Convolutional Network with RNN to exploit simultaneously spatial and temporal information in graph-structured and time-varying data. Xu, Cheng, et al. 2019 used a spatio-temporal GRU to differentiate the importance of neighbor factor and time period factor. Also, a dual attention mechanism is used in this model. This article argued that the amount of information provided by different time step varies. So a temporal attention module was designed to detect snapshots with the most valuable information, and a spatial attention module was used to detect the important neighbors of a node. Manessi et al. 2020 tried to modify the graph convolution layers in several ways and combined them with LSTM to process the sequence of adjacency matrices. 

Currently, various methods are being used to model continuous dynamic neural networks, with RNN-based approaches and time embedding approaches receiving significant attention recently. RNN-based approaches utilize an RNN-based architecture to contin- 

68 

uously update node embeddings. A key feature of these models is that the embeddings of nodes involved in any event or network change are immediately updated, ensuring that the embeddings are continuously current. Time embedding approaches employ positional embeddings of time to represent time as a vector. This method also ensures that node embeddings are updated promptly following any changes, maintaining the accuracy and relevance of the embeddings over time. 

Several continuous graph neural network models employ time embedding methods to capture temporal dynamics effectively. One notable method is the use of positional encoding to represent the time dimension, similar to the technique introduced in the Transformer architecture by Vaswani et al. 2017. An example of such a method is Time2Vec, introduced by Kazemi, Goel, Eghbali, et al. 2019, which is a type of positional encoding specifically designed to encode temporal patterns. Another innovative approach is the functional time embedding proposed by Xu, Ruan, et al. 2020. This method transforms the challenge of learning temporal patterns into a kernel learning problem, where the model learns a kernel function tailored to temporal data. These time embedding techniques are particularly effective for capturing temporal differences. This capability is highly beneficial for modeling interaction networks, as it allows the networks to accurately capture the timing between events. 

Kumar, Zhang, and Leskovec 2019 studied dynamic evolution of a user/item binary graph, where the only event type is edge addition (users purchase a new item). They employed two recurrent neural networks separately for users and items, and the recurrent neural networks are updated at every interaction. Besides the temporal embedding for each user/item, another embedding is also learned for each node that is fixed over time and represent the node’s static information. The final embedding is the concatenation of these two embeddings. Xu, Ruan, et al. 2020 developed a continuous-time dynamic graph model, named Temporal Graph Attention (TGAT). This model calculated node embedding based on k-hop neighborhood of nodes. Different from the methods mentioned above, this model 

69 

modified Time2Vec to represent delta of time as a vector. Also TGAT is able to inductively infer embedding for both new nodes and existing nodes as the graph evolves. 

Dynamic graph neural networks have been widely applied in real-world problems. For instance, it provides a new approach for researchers to capture both spatial and temporal dependencies in traffic forecasting problems (Yu et al. 2018; Diao et al. 2019; Huang et al. 2022; Wang, Zheng, et al. 2022; Chen, Li, et al. 2023). Using dynamic graph neural network, Zhao et al. 2019 proposed an approach where the graph structure is considered to be fixed but node features (denoting traffic flow) change over time. In this model, a GCN is used to capture the spatial feature and a GRU is used to capture the temporal feature. Graph neural network has also been applied in temporal knowledge graph completion problems. Since knowledge graphs are multi-relational graphs, in order to apply graph neural network models, relational GNNs are needed. In Schlichtkrull et al. 2018, for instance, relationspecific projections were used on node’s neighbors. Other application fields of temporal graph neural networks include recommendation systems (Song, Xiao, et al. 2019; Bai et al. 2020; Feng et al. 2020; Wang, Ding, et al. 2021; Gao et al. 2022; Xia et al. 2022; Liu, Li, et al. 2023), social network analysis (Min et al. 2021; Song, Wang, et al. 2021; Fu et al. 2020; Guo, Yu, et al. 2022; Wei et al. 2023) and so on. 

Link prediction is an important application in graph neural networks. By predicting upcoming activities between node pairs, link prediction has been widely used in applications like social networks, financial networks, knowledge graphs, etc. According to (Kumar, Singh, et al. 2020), before graph neural network, traditional approaches for link prediction can be categorized into three categories: link prediction methods that are based on heuristic node similarity scores (Liben-Nowell and Kleinberg 2003; Kossinets and Watts 2009; Cannistraci et al. 2013; Liu, Zhang, et al. 2011), link prediction methods based on latent embeddings of nodes (Perozzi et al. 2014; Grover and Leskovec 2016; Kazemi and Poole 2018; Ou et al. 2016), and other methods (Anand and Bianconi 2009; Sole and Valverde 2004; Tan et al. 2014; Xu, Pu, and Yang 2016). As a powerful tool to jointly capture 

70 

both structure features and node/edge features, graph neural network has gained enormous popularity over traditional methods in the application of link prediction. In Wu, Cui, Pei, Zhao, and Guo 2022, graph neural network based link prediction approaches can be categorized to two groups, node-based method and sub-graph based method. As summarize in Li, Wang, et al. 2020, a traditional graph neural network model generally consists of three steps: (1) Initialize a vector representation for each node as their initial attributes; (2) Iteratively update node representations by aggregating the neighborhood nodes’ messages; (3) Decode the final representation of the nodes. 

For applications in finance, Weber et al. 2019 experimented anti-money laundering in Bitcoin, using link prediction to detect illicit activities. Hao et al. 2019 studied link prediction using one-year simulated data of interbank cash bond trading. Lin et al. 2020 constructed a network using Ethereum transaction records, and proposed a random-walk based graph representation method to make predictions. Pareja et al. 2020 performed link prediction using RNN and graph convolutional neural networks on multiple networks constructed by different cryptocurrency transaction records. Using graph convolutional neural networks and LSTM, Zhang 2022 explored future lending relationship prediction on a network constructed with e-MID interbank market dataset. Liu, Tu, et al. 2024 performed link prediction on Bitcoin transaction network using discrete-time GNN models. You et al. 2022 performed link prediction on dataset of financial transaction among companies using two different systems of the Bank of Slovenia. 

## 4.2.4 Link Prediction Methods 

Prior to the widespread adoption of graph neural network techniques for graph embedding in addressing graph-related challenges, a variety of link prediction strategies had been established by researchers. Early methods, for instance, involved counting the number of common neighbors between two nodes, with many link prediction techniques relying on quantifying the similarity score between two points within a graph. Alternatively, some ap- 

71 

proaches aimed to predict the likelihood of a link forming between two nodes by analyzing the structural features of the network. 

According to Wu, Song, et al. 2022 and Martinez et al. 2016, link prediction can be divide into five categories, common neighbor based methods, path based methods, probabilistic and statistical models based methods, classifier based methods and network embedding based methods. The categories of link prediction methods are illustrated in Figure 4.1. Common neighbor based methods and path based methods were the most popular link prediction methods in the earlier days due to their simplicity to apply, efficiency to compute and convenience to interpret. However, these traditional link prediction methods fail to capture either node information or graph structure information. Furthermore, traditional link prediction methods rely on adjacency matrix _A ∈ R[N][×][N]_ . With the advent of the era of big data, traditional link prediction methods are facing great challenges when dealing with large scale graphs, since large adjacency matrices could be memory demanding and computationally expensive. Classifier based methods face the problem of class imbalance, since the real world networks are sparse, which means the existing edges are far less than non-existing edges. 

The network embedding methods successfully solve the shortcomings of the conventional methods. In network embedding methods, each node is represented in low-dimension and continuous feature vector, which are mapped using network embedding techniques that preserves both network structural information and node attributes information. Network embedding based methods can be further divided into several groups, for example, matrix factorization methods, random walk methods and network neural network methods. Recently, network embedding methods using network neural network have been proven to be powerful and effective in link prediction, as network neural network methods can capture the structural information and node attribute. In the following, we describe various network embedding methods in details. 

72 

Figure 4.1: Categories of link prediction methods (Wu, Song, et al. 2022) 

## _4.2.4.1 Network Embedding Based Methods_ 

Different from traditional link prediction methods that are based on adjacency matrix, where each entry indicates the presence or absence of a link between two nodes, network embedding can incorporate node features, higher-order proximity relationships, and network dynamics into the low dimensional vector representations to predict possible future links between node pairs. A good network embedding method should be able to effectively encode the structural patterns and essential node features for efficient network analysis and link prediction. Recently, networks embedding based methods have been developing rapidly and various approaches have been proposed. We divide the network embedding methods to four categories, matrix factorization based methods, random walk based methods ,graph neural network based methods, and other methods. 

73 

**Network Embedding with Matrix Factorization** Early network embedding methods were inspired by matrix factorization. The goal of network embedding methods with matrix factorization is to decompose the sparse adjacency matrix into lower dimensional denser matrices by matrix decomposition or singular value decomposition, so that the essential network structure properties and node relationships are preserved. Network embedding with matrix factorization has been widely used in various domains, for example, recommendation systems. Based on the calculated similarity between the embeddings of two nodes, the likelihood of a link existing between the two nodes can be obtained. Nodes with higher embedding similarities are considered more likely to be connected. Compared to traditional adjacency matrix based methods, network embedding methods with matrix factorization present higher efficiency in handling large networks. Also, this method has higher flexibility, since the learned embeddings can be used for various downstream tasks beyond link prediction, for example, node classification and graph classification. 

_LPMF_ was proposed by Menon and Elkan 2011. This model learns latent features from the topological structure of a graph. The latent features can also be combined with optional edge or node features. The similarity matrix is calculated as follows: _S ≈ L_ ( _U_ Λ _U_ ) where _U ∈ R[n][×][k]_ , Λ _∈ R[k][×][k]_ and _L_ ( _·_ ) is the link function. This model produces a latent vector _ui ∈ R[k]_ for every node _i_ . In order to perform link prediction, the node pair similarities can be calculated as _Sij_ ( _U,_ Λ) = _L_ ( _u[T] i_[Λ] _[u][j]_[)][.] 

_GraRep_ was proposed by Cao, Lu, and Xu 2015. Unlike some methods that focus only on local neighborhood connections, this model aims to incorporate global structural information of the entire network. Compared to previous models, GraRep generally shows better performance in various tasks. However, training the model can become computationally expensive for very large or dense networks. 

**Network Embedding with Random Walk** Decomposing the adjacency matrix primarily captures the impact of direct neighbors on a given node, which is a notably constrained approach. To address this limitation, random walk techniques are employed to create a con- 

74 

text for the nodes, effectively compensating for the shortcomings of matrix factorization. Consequently, node sequences are analogized to sentences, allowing for the application of natural language processing techniques to obtain node embeddings. In this scenario, the frequency with which two nodes co-occur in the same random walk directly correlates with the similarity of their embeddings. 

_DeepWalk_ was proposed by Perozzi et al. 2014. This approach is the first of its kind to derive vector representations of nodes through random walks, capturing local information through truncated random walks to establish the nodes’ context. It innovates by interpreting node sequences as sentences, thereby learning latent representations. This method introduces a fresh perspective to network embedding algorithms and frequently serves as a reference model in this domain. By conducting random walks within the network, sequences of nodes are generated, and their vector representations are determined using the skip-gram model, a technique borrowed from natural language processing. 

_Node2Vec_ Grover and Leskovec 2016 introduced Node2vec, a model that captures continuous feature representations for nodes. This method enhances its approach by employing a biased random walk strategy, which melds breadth-first search (BFS) and depth-first search (DFS) techniques for exploring neighborhoods. This strategy builds on DeepWalk, allowing for a more adaptable understanding of the contextual structure. Consequently, nodes that are “close” within the network are likely to be similarly “close” within the latent representation space. 

_Struc2Vec_ Ribeiro et al. 2017 focuses on structural identity, employing a hierarchical metric to assess node similarity across various scales through the construction of a weighted multilayer graph for context generation. This approach characterizes vertex similarity based on spatial structural characteristics. 

The methods mentioned previously only produce embedding vectors for further analysis, necessitating additional steps like similarity calculations for tasks such as link prediction. Various distance measures, including Euclidean distance, standardized Euclidean 

75 

distance, Chebyshev distance, and cosine distance, are applicable for evaluating similarities. In past experiments investigating the impact of different distance metrics on link prediction across various network embedding techniques, no substantial differences in effectiveness were observed among the metrics. Given its prevalence in network embedding research, we also utilize cosine distance to measure the similarity between two nodes in our current study. 

**Network Embedding with Graph Neural Networks** Graph neural networks (GNNs) were developed by integrating ideas from convolutional neural networks (CNNs) and graph embedding to address specific limitations. Firstly, CNNs are primarily designed for data that exists in a regular Euclidean space, such as images and text, which doesn’t encompass the complex, non-Euclidean structure of networks. Secondly, while early graph embedding methods like DeepWalk and Struc2vec marked significant advancements, they are limited by their shallow learning architectures, making it challenging to enhance the quality of network embeddings further. GNNs emerged as a solution to these challenges. They have been widely applied to three primary types of graph analysis tasks: node classification, graph classification, and link prediction. Despite extensive research on node and graph classification, the application of GNNs to link prediction remains relatively underexplored and less understood, with several key methods highlighted in the ensuing discussion. 

_Graph Convolutional Networks(GCN)_ This model (Kipf and Welling 2017) leveraged a streamlined version of convolutional neural networks (CNNs) tailored for semi-supervised learning on graph datasets. It is designed to capture hidden layer representations that encapsulate the local structure of the graph as well as the attributes of its nodes. By harnessing these features, it facilitated the execution of tasks like node classification, graph classification, and link prediction. 

_Graph Attention Network (GAT)_ This model (Velivckovic, Cucurull, et al. 2017) employed a neural network design tailored for graph-structured data, utilizing masked selfattention layers to overcome the limitations associated with earlier approaches reliant on 

76 

graph convolutions or their approximations. Through the use of layered structures where nodes can focus on the features of their neighboring nodes, GATs facilitated the assignment of variable importance to different nodes within a neighborhood. This is achieved without the need for intensive matrix operations, like inversion, or pre-existing knowledge of the graph’s architecture. 

_DGCNN_ This model (Zhang, Cui, et al. 2018) introduced an innovative spatial graph convolution layer capable of feature extraction, making it suitable for link prediction tasks as well. It differentiated itself by learning from the global graph’s topology through the sorting of vertex features instead of their aggregation, a process facilitated by the newly developed SortPooling layer. 

Since their inception, Graph Neural Networks (GNNs) have emerged as instrumental tools for processing graph-structured data and have proven to be highly effective in link prediction tasks. Extensive experiments have demonstrated that GNN-based approaches are capable of generating link representations that are more effective than those produced by prior methodologies. 

## **4.3 Experiment** 

In this section, we first apply various link prediction methods to the dealer network created from our corporate bond dataset. While previous works have tested these methods on many commonly used public datasets, significant differences exist between this coreperipheral structured dealer network and most other public network datasets. Additionally, few research has attempted these link prediction experiments on the corporate bond dealer dataset to date. Our experiments will also assess the suitability of different link prediction methods for the core-peripheral structured network using the corporate bond dataset. 

In the corporate bond transaction dataset we use, each transaction involves two parties, allowing the construction of a network with dealers as nodes and transactions as edges. The experiments follow the methodology described in Xu, Ruan, et al. 2020, focusing on 

77 

predicting future transactions (edges) in both static and dynamic network settings. 

## 4.3.1 Static Network Link Prediction 

First, we test the link prediction methods on static dealer networks. The static networks are constructed using the transaction records of the most traded bond in the OTC market from 2011. The data is divided into a training set and a testing set. The training set consists of the network constructed from bond transactions in the year 2011 of varying lengths. The testing set is constructed using transaction data immediately after 2011. To explore the relationship between the network aggregation time window and prediction accuracy, we construct seven testing sets using time windows of varying lengths: 1 week (aggregated using data from first week of 2012), 2 weeks (aggregated using data from first two weeks of 2012), 1 month (aggregated using data from first month of 2012), 2 months (aggregated using data from first two months of 2012), 3 months (aggregated using data from first three months of 2012), 6 months (aggregated using data from first six months of 2012), 12 months (aggregated using data from entire year of 2012). In each testing set, negative samples (node pairs that are not connected) are undersampled to the testing set to balance the class distributions. Undersampling techniques are applied to the negative class so that the positive class constitutes 25% observations (Rummele et al. 2015, da Silva Soares and Prudˆencio 2012, Davis et al. 2013, Lichtenwalter and Chawla 2012, Lichtenwalter, Lussier, and Chawla 2010). Based on the training set, the probability of a link exists between two arbitrary nodes can be calculated. After computing the probability for all possible node pairs, the pairs within top 20% highest probabilities are kept as prediction results. The results are summarized in Table 4.1. Common neighbor based methods and path based methods calculate the probability for all possible node pairs and the pairs with the highest probabilities are chosen the outcome. As a result, these two methods can only produce positive predictions in the outcome. 

In Table 4.1, the performance of Katz Index (Katz 1953), with an AUC value of 0.5, 

78 

|||||AUC||||
|---|---|---|---|---|---|---|---|
||1 week|2 weeks|1 month|2 months|3months|6 months|12 months|
|Common Neighbors|0.5911|0.6232|0.6459|0.6592|0.6747|0.6841|0.6812|
|Jaccard Index|0.4979|0.4979|0.4978|0.4956|0.4966|0.4934|0.4918|
|Salton Index|0.5000|0.4984|0.4987|0.4963|0.4962|0.4928|0.4913|
|Sorensen Index|0.4979|0.4994|0.4978|0.4956|0.4966|0.4934|0.4918|
|Hub Promoted Index|0.4979|0.4974|0.4969|0.4981|0.4945|0.4940|0.4949|
|Hub Depressed Index|0.4989|0.4984|0.4984|0.4958|0.4956|0.4921|0.4917|
|Local Leicht-Holme Index|0.4979|0.4969|0.4981|0.4967|0.4969|0.4933|0.4899|
|Adamic Adar Index|0.5943|0.6176|0.6447|0.6613|0.6727|0.6830|0.6824|
|Resource Allocation|0.5880|0.5959|0.6265|0.6452|0.6579|0.6747|0.6772|
|Preferential Attachment|0.6100|0.6308|0.6685|0.6783|0.6940|0.7018|0.7085|
|Local Naive Bayes - RA|0.5880|0.5929|0.6219|0.6428|0.6558|0.6752|0.6775|
|Local Naive Bayes - AA|0.5817|0.6085|0.6382|0.6574|0.6726|0.6828|0.6847|
|Local Naive Bayes - CN|0.5974|0.6131|0.6456|0.6623|0.6736|0.6840|0.6852|
|Katz Index|0.5000|0.4994|0.4978|0.4975|0.4974|0.4968|0.4979|
|Local Path Index|0.5000|0.4994|0.4990|0.4985|0.4974|0.4978|0.4965|
|Glocal Leicht-Holme-Newman|0.5000|0.4994|0.4987|0.4989|0.4972|0.4971|0.4966|
|Local Random Walk - 2|0.5031|0.5055|0.5003|0.5022|0.5032|0.4983|0.4969|
|Local Random Walk - 3|0.5031|0.5060|0.5061|0.5047|0.5035|0.4988|0.4997|
|Local Random Walk - 4|0.5031|0.5075|0.5058|0.5032|0.5025|0.4980|0.4964|
|Superposed Random Walk - 3|0.5031|0.5050|0.5024|0.5032|0.5032|0.5002|0.4996|
|Superposed Random Walk - 8|0.5031|0.5060|0.5064|0.5036|0.5029|0.4984|0.4983|
|SimRank|0.4979|0.4979|0.4984|0.4963|0.4967|0.4928|0.4917|
|Matrix Forest Index|0.5000|0.4979|0.4978|0.4985|0.4983|0.4972|0.4970|
|GCN|0.5052|0.5035|0.5817|0.5187|0.5267|0.5388|0.5457|
|GCN - Number of Trades|0.5283|0.5767|0.5870|0.6019|0.6019|0.6078|0.6130|
|GCN - Volume of Trades|0.5251|0.5722|0.5820|0.5996|0.6024|0.6033|0.6082|
|GAT|0.4989|0.4994|0.4975|0.4950|0.4949|0.4949|0.4953|



Table 4.1: Link prediction results in AUC 

This Table reports the link prediction results of core-peripheral structured dealer network using various link prediction methods. The training set contains the edges of the network created using one year’s transaction between dealers. The link predictions are tested on networks constructed using five different testing sets, each created using transactions in the next 1 month, 2 months, 3 months, 6 months and 12 months. 

79 

suggests it is no more effective than random chance at distinguishing between positive and negative link examples. This reflects its limited predictive utility. Conversely, methods like Common Neighbors (Jin et al. 2001), Adamic Adar Index (Adamic and Adar 2003), Resource Allocation (Zhou et al. 2009), and Preferential Attachment (Mitzenmacher 2004) demonstrate superior AUC scores, indicating enhanced prediction accuracy. The AUC score tends to rise with an increase in the size of the testing set. Within networks structured around core-periphery dynamics, path-based prediction strategies underperform in contrast to approaches centered on common neighbors, which yield more favorable outcomes. The dense connectivity of the network hampers the Stochastic Block Model’s (Guimera and Sales-Pardo 2009) ability to effectively segment the network into distinct blocks, leading to its ineffectiveness. While common neighbor-based methods generally show promise, some of these methods fall short due to a pronounced skewness in the scores assigned to node pairs, which complicates the task of accurately identifying links with higher likelihoods, e.g. Jaccard Index, Salton Index (Salton and McGill 1986) and Sorensen Index (Sorensen 1948) in Table 4.2. 

Table 4.3 presents the success rate of different link prediction methods for various dealer tier pair groups across multiple test sets. The table indicates that models generally struggle with predicting links involving peripheral tier dealers. Interestingly, although the local path index methods do not perform well overall, they show slightly better results for pairs involving mid-tier and peripheral dealers compared to core-core pairs. Additionally, the table highlights how the choice of aggregation window affects prediction outcomes: as the aggregation window lengthens, accuracy improves in the core-mid group. 

Combining the findings from the three tables, it is evident that common neighbor-based methods typically yield better results, whereas most path-based methods struggle to provide accurate predictions in this core-periphery structured network. Table 4.2 illustrates that the probability distributions of edge formation for some prediction methods are significantly skewed to the left, leading to their inability to effectively differentiate the likelihood of edge 

80 

||10%|25%|50%|75%|90%|95%|96%|97%|98%|99%|100%|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Common Neighbors|0|0|0|0.0147|0.0294|0.0441|0.0588|0.0882|0.1176|0.1911|1|
|Jaccard Index|0|0|0|0.0188|0.01250|0.2500|0.3075|0.3333|0.5000|1|1|
|Salton Index|0|0|0|0.1084|0.2886|0.4335|0.5000|0.5773|0.7071|1|1|
|Sorensen Index|0|0|0|0l0370|0.2222|0.4000|0.4703|0.5000|0.6667|1|1|
|Hub Promoted Index|0|0|0|0.3333|1|1|1|1|1|1|1|
|Hub Depressed Index|0|0|0|0.0194|0.1456|0.3157|0.3333|0.5000|0.5000|1|1|
|Local LHN|0|0|0|0.0072|0.0400|0.1250|0.2000|0.3333|0.5000|1|1|
|Adar-Adamic|0|0|0|0.0066|0.0139|0.0259|0.0332|0.0463|0.0650|0.1089|1|
|Resource Allocation Index|0|0|0|0.0007|0.0027|0.0067|0.0086|0.0117|0.0180|0.0328|1|
|Preferential Attachment|0|0.0001|0.0002|0.0011|0.0045|0.0109|0.0147|0.0201|0.0330|0.0652|1|
|Local Naive Bayes - RA|0|0|0|0.0002|0.0016|0.0041|0.0053|0.0075|0.0184|0.0231|1|
|Local Naive Bayes - AA|0|0|0|0.0021|0.0071|0.0168|0.0215|0.0292|0.0434|0.0750|1|
|Local Naive Bayes - CN|0|0|0|0.0053|0.0144|0.0344|0.0444|0.0601|0.0876|0.1461|1|
|Katz Index|0|0.0001|0.0002|0.0042|0.0099|0.0240|0.0323|0.0466|0.0826|0.4294|1|
|Local Path Index|0|0|0.0001|0.0048|0.0094|0.0202|0.0259|0.0348|0.0497|0.0814|1|
|Global LHN|0|0.0001|0.0002|0.0012|0.0043|0.0112|0.0154|0.0211|0.0314|0.0553|1|
|Local Random Walk - 2|0|0|0.0001|0.0008|0.0031|0.0056|0.0069|0.0085|0.0112|0.0161|1|
|Local Random Walk - 3|0|0|0.0002|0.0011|0.0035|0.0062|0.0075|0.0088|0.0111|0.0151|1|
|Local Random Walk - 4|0|0.0001|0.0003|0.0011|0.0034|0.0065|0.0078|0.0098|0.0121|0.0161|1|
|Superposed Random Walk - 3|0|0.0001|0.0002|0.0011|0.0036|0.0062|0.0075|0.0088|0.0112|0.0151|1|
|Superposed Random Walk - 8|0|0.0002|0.0004|0.0010|0.0037|0.0070|0.0082|0.0102|0.0122|0.0164|1|
|SimRank|0|0|0.0001|0.0008|0.0031|0.0056|0.0069|0.0085|0.0112|0.0161|1|
|Matrix Forest Index|0|0.0004|0.0008|0.0013|0.0019|0.0022|0.0023|0.0024|0.0027|0.0032|1|
|GCN|0.1085|0.1096|0.1102|0.1113|0.1132|0.1148|0.1155|0.1165|0.1179|0.1208|1|
|GAT|0.0001|0.0001|0.0012|0.0002|0.0004|0.0011|0.0013|0.0017|0.0025|0.0051|1|



Table 4.2: Percentile of node similarities 

This table reports the percentile of node pair similarities (edge formation probability). According to the result, the output of some link prediction methods fail to distinguish the edge formation probability between the different node pairs, since the results are skewed to the left, and a large amount of edge similarities equal to 1. 

81 

||(a)|(b)|(c)|(d)|(e)|(f)|
|---|---|---|---|---|---|---|
||Core - Core|Mid - Mid|Peripheral - Peripheral|Core - Peripheral|Core - Mid|Mid - Peripheral|
||||1 Month||||
|Common Neighbors|0.9473|0.1029|0|0|0.4240|0|
|Adamic Adar Index|0.9605|0.1029|0|0|0.4083|0|
|Resource Allocation|0.9605|0.0882|0|0|0.3089|0|
|Preferential Attachment|1|0|0|0.0140|0.5549|0|
|Local Naive Bayes - RA|0.9605|0.0441|0|0|0.2984|0|
|Local Naive Bayes - AA|0.9736|0.1176|0|0|0.3612|0|
|Local Naive Bayes - CN|0.9736|0.1029|0|0.0304|0.4083|0|
|Local Path Index|0|0.0147|0|0|0|0.0285|
|GCN|0.1973|0.2794|0|0.0070|0.3036|0|
|GCN - Number of Trades|0.1973|0.3235|0|0.0140|0.3036|0|
|GCN - Volume of Trades|0.1842|0.3088|0|0.0140|0.2879|0|
||||2 Months||||
|Common Neighbors|1|0.2201|0|0|0.5907|0|
|Adamic Adar Index|1|0.1926|0|0|0.6138|0|
|Resource Allocation|1|0.1559|0|0|0.5328|0|
|Preferential Attachment|1|0.0550|0|0.0180|0.7644|0|
|Local Naive Bayes - RA|1|0.1651|0|0|0.5135|0|
|Local Naive Bayes - AA|1|0.1834|0|0|0.5945|0|
|Local Naive Bayes - CN|1|0.1926|0|0|0.6216|0|
|Local Path Index|0|0.0091|0|0|0|0.0131|
|GCN|0|0.1376|0|0.0045|0.0656|0.0394|
|GCN - Number of Trades|0.2705|0.3669|0|0.0180|0.3822|0.0263|
|GCN - Volume of Trades|0.2705|0.3761|0|0.0180|0.3629|0.0263|
||||3 Months||||
|Common Neighbors|1|0.3203|0|0.0031|0.7284|0|
|Adamic Adar|1|0.2968|0|0|0.7284|0|
|Resource Allocation|1|0.2185|0|0.0063|0.6549|0.0101|
|Preferential Attachment|1|0.2421|0|0.0318|0.8562|0|
|Local Naive Bayes - RA|1|0.2265|0|0.0063|0.6389|0.0101|
|Local Naive Bayes - AA|1|0.3046|0|0|0.7252|0|
|Local Naive Bayes - CN|1|0.3281|0|0|0.7220|0|
|Local Random Walk|0|0.0315|0|0.0063|0.0351|0|
|Matrix Forest Index|0|0.0078|0|0|0.0031|0.0101|
|GCN|0.0309|0.1640|0|0.0127|0.0958|0.0404|
|GCN - Number of Trades|0.2989|0.3750|0|0.0222|0.4153|0.0303|
|GCN - Volume of Trades|0.2886|0.4062|0|0.0222|0.4089|0.0303|
||||6 Months||||
|Common Neighbors|1|0.6009|0|0.0389|0.9256|0.0081|
|Adamic Adar|1|0.5962|0|0.0369|0.9256|0.0040|
|Resource Allocation|1|0.5117|0|0.0486|0.8872|0.0081|
|Preferential Attatchment|1|0.6150|0|0.1031|0.9952|0|
|Local Naive Bayes - RA|1|0.5211|0|0.0505|0.8800|0.0121|
|Local Naive Bayes - AA|1|0.5915|0|0.0369|0.9256|0.0040|
|Local Naive Bayes - CN|1|0.6056|0|0.0330|0.9328|0.0040|
|Local Path Index|0|0.0140|0.0175|0|0.0023|0.0447|
|Local Random Walk|0|0.0469|0.0175|0.0077|0.0335|0.0325|
|Matrix Forest Index|0|0.0093|0|0.0038|0.0047|0.0121|
|GCN|0.0775|0.2159|0.0175|0.0272|0.1990|0.0243|
|GCN - Number of Trades|0.4137|0.4460|0|0.0525|0.5203|0.0203|
|GCN - Volume of Trades|0.3534|0.4647|0|0.0544|0.4868|0.0203|
||||12 Months||||
|Common Neighbors|1|0.7286|0|0.0816|0.9509|0.0205|
|Adamic Adar|1|0.7325|0|0.0845|0.9530|0.0205|
|Preferential Attachment|1|0.8217|0|0.1884|1|0|
|Local Naive Bayes - RA|1|0.6705|0|0.0875|0.9402|0.0175|
|Local Naive Bayes - AA|1|0.7480|0|0.0875|0.9594|0.0205|
|Local Naive Bayes - CN|1|0.7596|0|0.0845|0.9637|0.0205|
|Local Path Index|0|0.0193|0.0266|0.0014|0.00221|0.0439|
|Local random Walk|0|0.0426|0.0133|0.0133|0.0341|0.0410|
|Matrix Forest Index|0|0.0193|0.0267|0.0029|0.0063|0.0269|
|GCN|0.1000|0.2596|0.0267|0.0415|0.2217|0.0498|
|GCN - Number of Trades|0.4333|0.5310|0|0.0816|0.5671|0.0381|
|GCN - Volume of Trades|0.3667|0.5193|0|0.0905|0.5351|0.0381|



Table 4.3: Percentage of successfully predicited edges 

This table reports the percentage of edges (links) successfully predicted by different link prediction algorithms, grouped by dealer tiers of the transaction parties. For example, column (d) represents the percentage of successfully predicted edges in the test set between core dealers and peripheral dealers. 

82 

formation. Furthermore, according to Table 4.3, although some methods perform well with core-core tier node pairs, the majority fail to accurately predict edges involving periphery dealers. 

## 4.3.2 A Dynamic Graph Neural Network Model to Predict Transactions in Over-the-counter Bond Market 

The model, Neighbor Aggregation Temporal Graph Network (NATGN), proposed here, is based on the Temporal Graph Networks (TGN) (Rossi et al. 2020), and Kazemi, Goel, Jain, et al. 2020. As Kazemi, Goel, Jain, et al. 2020 concluded, a dynamic graph neural network model can be seen as an integration of encoder and decoder. The encoder served as a function that maps the graph’s information to node embeddings. Based on the node embeddings produced by the encoder, the decoder made predictions. TGN adopted the encoder-decoder framework, and applied it on continuous time dynamic graphs consists of a sequence of time-stamped events, creating node embeddings for the dynamic graph at every timestamp. However, TGN used _most recent message_ (keep only the latest message for a given node in a batch and discard other messages) and _mean message_ (take the average value of all messages for a given node in a batch) at the message aggregating step. According to Xu, Hu, et al. 2018, mean aggregators have difficulties in distinguishing graphs with nodes and edges that have repeating features. In over-the-counter bond market, most transactions volumes are in the full hundred. Mean message aggregation tends to perform less effective in this situation. In this thesis, a more comprehensive message aggregation technique is applied to the original TGN model, to better capture the information of transactions in the dynamic dealer network in over-the-counter bond market. 

## _4.3.2.1 Modules Used to Construct the Model_ 

**Node State Memory Module** The node state memory module serves as a tool to store the node’s activity history. The memory for node _i_ at time _t_ can be denoted as _si_ ( _t_ ). _si_ ( _t_ ) is a 

83 

vector that contains the information of all the interactions node _i_ has involved up to time _t_ . After every event, the _si_ ( _t_ ) will be updated. When a new node is shows up in the graph for the first time, the memory for the node will be set to a zero vector. 

**Message Function** For every node _i_ , when an event takes place at time _t_ , a message is generated. And the memory for node _i_ is updated to _si_ ( _t_ ), using this message. In most cases, for example, social networks and financial networks, an event takes place as an interaction between two nodes, which creates an edge. _eij_ ( _t_ ) represents the interaction between two nodes _i_ , _j_ . If the network is directed, the messages generated for the source node _i_ and destination node _j_ can be represented as: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0094-03.png)


Here, _si_ ( _t[−]_ ) denotes the memory of node _i_ before time _t_ . And _∥_ denotes concatenation. In this case, the message function is defined as concatenation. 

**Node Message Aggregator** Like most deep learning tasks, batch processing is used while processing the data, since it is more efficient while dealing with large volumes of data. As a result, the same batch may include multiple interactions within the same pair of nodes. According to the message function above, every interaction generates a message. In order to aggregate the messages created in the same batch on the same node _i_ , a message aggregator is needed, which is formulated as: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0094-06.png)


In the equation, _mi_ ( _t_ 1) _, ..., mi_ ( _tb_ ) represent the messages created by all the interactions involving node _i_ with in one batch. Here, _∥_ denotes the aggregation function. 

Message Aggregation has recently attracted the attention of many researchers. While most work chooses to use mean message aggregator in message passing, some researchers argue that mean aggregation does not adequately capture information from the nodes’ 

84 

neighborhoods (Corso et al. 2020). Dehmamy et al. 2019 suggested that employing multiple aggregators—such as mean, sum, and normalized mean—that derive similar statistics from the input message can enhance the performance of GNNs. The majority of studies in the literature employ a single aggregation method, with mean, sum, and max aggregators being the most commonly utilized in cutting-edge models. Using examples from Corso et al. 2020, Figure 4.2 illustrated the limitations for each aggregation methods. 

Figure 4.2: Example of neighborhood information aggregators 

This figure shows examples where, in a single GNN layer, certain aggregators are unable to distinguish between messages from different neighborhoods. In panel (a), mean aggregators generated identical messages. In panel (b), min, max and std aggregators generated identical messages. In panel (c), mean, min and max aggregators generated identical messages. In panel (d), std aggregators generated identical messages. 

The aggregators used are as follows: 

85 

- Mean aggregator: _µi_ ( _X_ ) = _|_ Γ1 _i|_ � _j∈_ Γ _i[X][i]_[ , where][ Γ] _[i]_[ is the neighborhood of node] _[ i]_[.] 

- Maximum aggregators: _maxi_ ( _X_ ) = max _j∈_ Γ _i Xj_ 

- Minimum aggregators: _mini_ ( _X_ ) = min _j∈_ Γ _i Xj_ 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0096-04.png)


Among the four aggregators, the mean aggregator is the most commonly used message aggregator. For each node, it calculates the average of the messages received from neighboring nodes. The maximum and minimum aggregators are typically used when node attributes are discrete variables. Lastly, the standard deviation aggregator measures the variability in the features of neighboring nodes, assessing the diversity of the messages a node receives. 

However, using combined aggregators alone is not enough. Xu, Hu, et al. 2018 revealed that using mean and max aggregators alone does not allow differentiation between neighborhoods that have identical features but different numbers of nodes. This limitation also extends to all the other aggregators mentioned previously. So in order to distinguish the information of cardinality, they proposed to use summation aggregator. Corso et al. 2020 proposed to combine the mean aggregator with a scaler which is associated with nodes degrees. But one problem with summation aggregation is that it performs poorly on unseen graphs, especially when the graph is larger. One reason is that even a slight variation in the degree can greatly amplify or attenuate the messages and gradients. To solve this problem, a logarithmic scaler, _Samp_ is proposed. Here _δ_ is a normalization parameter calculated across the batch and _d_ represents the degree of the node receiving the message (Velivckovic, Ying, et al. 2019). 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0096-07.png)


To further generalize the scaler, a parameter _α_ is added to the equation. When _α_ is 0, there’s 

86 

no scaling, when _α_ is positive or negative, the scaler works as amplification or attenuation. 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0097-02.png)


In order to combine the scalers with aggregator, we take tensor products. So the scaleraggregator combination can be formulated as 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0097-04.png)



![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0097-05.png)


As mentioned above, higher degree graphs could benefit from multiple types of aggregators. So the scaler-aggregator combination is inserted in the message passing process, obtaining the following message: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0097-07.png)


where _M_ and _U_ are multiple layer perceptions. _U_ reduced the the size of concatenated message from R[12] _[F]_ back to R _[F]_ . The process for the message aggregator is illustrated in Figure 4.3. 

In the original TGN model, the message aggregator module offered two options: the mean aggregator and the last message aggregator. As mentioned earlier, in this bond transaction dataset, most transaction volumes are in full hundreds, which can result in identical messages when using the mean aggregator. Conversely, the last message aggregator might miss crucial transaction information. For these reasons, we propose employing the principal neighborhood aggregation method _C_ = _S_[ˆ] _⊗ A,_[ˆ] as the message aggregator module in our model to more effectively address the challenges presented by the bond dealer network dataset. 

**Node Memory Updater** This module is used to update the memory of node _i_ when an 

87 

Figure 4.3: Diagram for the scaler-combined aggregator 

This diagram depicts the process for the message aggregator. The circles represent nodes in a network, and the bars represent the vector representations of the messages. In this simplified example, the central node has three direct neighbors. We assume that all three neighbors occur event updates, generating three messages for the central node. From left to right: The central node receives three messages. To aggregate these messages, they are processed using mean, standard deviation, minimum, and maximum aggregators, each producing one aggregated message. Subsequently, these four aggregated messages are processed through three scalers (identical, amplifier, and attenuator). Finally, the twelve aggregated and scaled message representations are fed into a Multi-Layer Perceptron (MLP) to produce the final aggregated message. 

event involving the node occurs. And the memory for the node will be updated to: 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0098-04.png)


where _Mi_ ( _t_ ) is the aggregated message produced by the node message aggregator module. In the bond dealer network we are studying, an event (transaction) involves two parties (nodes), as a result, the memories of both nodes will be updated after the event. The _updater_ function to update memory is learnable, for example, a recurrent neural network is a good choice, since the _updater_ can be seen as the function takes a new input to update the old state and eventually produces a new state. 

**Node Embedding Module** The node embedding module produces the embedding _zi_ ( _t_ ) of node _i_ at any time _t_ . The embeddings of nodes can be used for graph-related tasks, for example, computing the probability of an edge exists between two nodes when performing 

88 

link prediction. The embedding is 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0099-02.png)


In this equation, _h_ is a learnable function, different choices of embedding functions can be used in different scenarios. The simplest embedding function is identity embedding. In this case, the state representation _si_ ( _t_ ) of node _i_ at time _t_ , is directly utilized as the node’s new embedding. Other choices includes time projection embedding (Kumar, Zhang, and Leskovec 2019) and graph attention embedding (Xu, Ruan, et al. 2020). 

## _4.3.2.2 Training_ 

The dealer network spans six years and comprises 1,658 nodes with approximately 22 million edges. The data is divided chronologically into training and testing sets in a 70%-30% ratio based on the transaction timestamps. All transactions within the batches are organized in chronological order. Negative samples (non-existing edges) are created by substituting the destination nodes with different nodes, while maintaining the original timestamps. 

In this training process, the node pairs in the previous batch are sent to the message module to create message representations for the next stage. Then the node message aggregator module receives the message representations from the batch. Since the same node pair could have multiple interactions at different time, different messages between the same node pair have to be aggregated using different methods to avoid information loss. Then the aggregated messages flows to the next module to update the node memory. After updating the memory representations, the embedding module calculates the node embeddings _zi_ , _zj_ and _zn_ for source nodes, destination nodes, and negative nodes (nodes that form nonexisting edges with source nodes) respectively. When computing the node embeddings, the calculation of time encoding _ϕ_ (∆ _t_ ) follows the computational approach outlined in Kazemi, Goel, Eghbali, et al. 2019. In _ϕ_ (∆ _t_ ), ∆ _t_ = _t − t[′]_ , where _t_ is the timestamp of 

89 

a node pair in the testing set to be inferenced, and _t[′]_ is the timestamp of the immediate past interaction between the same node pair. Once the node embeddings are generated, positive node pairs and negative node pairs are passed to the decoder, which computes their probabilities. The training process utilizes the binary cross entropy (BCE) loss function. 

Figure 4.4: Illustration of the algorithm. 

This figure illustrates the sequence of operations employed to train the modules. Initially, the memory module is updated with messages generated using the raw data from the previous batch. Subsequently, node embeddings are calculated using the refreshed memory module. This arrangement ensures that the computation involving modules that are used to update the node memory impacts the loss function and receives gradient updates. 

## _4.3.2.3 Experiments Outcome_ 

**Performance** Table 4.4 presents the results of future transaction prediction. The NATGN model outperforms the baseline models. Dynamic link prediction models with various message aggregation modules generally perform better than static network link prediction models. However, the results of dynamic and static link prediction models cannot be directly compared due to fundamental differences in network structure and data representation. In the static network, transactions between the same pair of dealers are aggregated into a single edge, resulting in approximately 60,000 edges. In contrast, the dynamic network contains over 22 million edges, with most edges appearing repeatedly over the six years. Our model predicts the existence of an edge between _i_ and _j_ within, where ∆ _t_ = _t − t[′]_ is previously defined. In this scenario, our model successfully predicted many recurring transactions, achieving a relatively higher AUC value compared to the previously discussed 

90 

static network prediction models. 

||Core-Core|Mid-Mid|Peripheral-Peripheral|Core-Mid|Core-Peripheral|Mid-Peripheral|AUC|
|---|---|---|---|---|---|---|---|
|Last|0.7116|0.7092|0.3943|0.7749|0.6934|0.5657|0.7280|
|Mean|0.7769|0.6730|0.3708|0.7523|0.6374|0.5328|0.7949|
|Std|0.8473|0.7795|0.4460|0.8496|0.7943|0.6363|0.8507|
|Min|0.8551|0.8221|0.4225|0.8608|0.7835|0.6382|0.8636|
|Max|0.7407|0.7422|0.4976|0.8107|0.7541|0.6179|0.7506|
|NATGN|0.8714|0.8498|0.5023|0.8909|0.8272|0.6972|0.8951|



Table 4.4: Comparison of message aggregation methods 

Given the network’s unique structure, it is more meaningful to compare prediction results among dealer pairs from different tiers rather than just considering the AUC values. According to Table 4.3, while some static network link prediction models achieve fair results in predicting links between core-core and core-mid dealer pairs, none of the methods provide comparable results for predictions in dealer pairs involving peripheral-tiered dealers. However, as shown in Table 4.4, the dynamic network model significantly outperformed the static network models (as shown in Table 4.3) when predicting connections between dealer pairs involving the peripheral tier. 

A possible explanation for this could be that peripheral dealers have relatively lower topological importance in the static network. As a result, most static network link prediction methods ignore or fail to capture the links involving peripheral dealers. However, in our model, with the help of memory modules, the activity patterns of each individual node, including peripheral nodes, are captured. The memory of these peripheral nodes can then be utilized for future link prediction. According to Table 4.4, consistent with the static network prediction results, dealer pairs involving core-tiered dealers have relatively higher link prediction accuracy than others. Meanwhile, although dealer pairs involving peripheral-tiered dealers still have the lowest accuracy, the results are much better than those from link prediction models in a static network setting. Furthermore, with the help of the neighborhood message aggregator, the model achieves better results across different dealer tier pairs. It is worth noting that the max and min aggregators performed better than the mean aggregator. The max aggregator is more predictive in core-core dealer tiers, 

91 

while the min aggregator has higher accuracy in peripheral-peripheral dealer tiers. Recall that the message function concatenates node features, edge features, and time intervals, it seem that by simply taking the average of neighborhood messages, important local neighborhood structural information is ignored. 


![](markdown_output/misiakos-graph-learning_images/misiakos-graph-learning.pdf-0102-02.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 4.5: Model performance comparison 

Figure (a) shows trade off between accuracy and speed. Figure (b) shows the performance of methods with different number of layers when sampling an increasing number of neighbors 

Following the framework of Rossi et al. 2020, we examine the relationship between the model’s performance and the choice of different modules. The result is illustrated in Figure 4.5a. First, we analyze the impact of the memory module. When running the model without the memory module on the testing set, the running speed increases, but the accuracy drops significantly compared to running NATGN with the memory module. The performance enhancement provided by the memory module may be attributed to its ability to store long-term historical activities for each node. This capability likely enhances prediction accuracy on edges involving peripheral nodes, which are less active and have fewer transactions. We also assessed the impact of different embedding modules. Using the identity embedding method resulted in lower accuracy. In contrast, employing the graph attention embedding led to higher precision compared to the other embedding modules. 

92 

This suggests that in the dealer network, link prediction is more effective when it leverages information from neighboring nodes. 

We compared the NATGN model with original models, one with with last message aggregator (msg-last) and another one with mean aggregator (msg-mean). The NATGN model with neighboring message aggregator performs better, but is slightly slower than the original models. 

In order to achieve good performances in the TGAT model (Xu, Ruan, et al. 2020), it is important to have two layers. However, in NATGN, since it uses the memory module from TGN, it is enough to use only one layer to get a moderately high performance (Figure 4.5b). This is due to the fact that when accessing the memory of the 1-hop neighbors, the information from hops further away is accessed indirectly. At the same time, by using only one layer of graph attention, the model gets faster drastically. 

## **4.4 Conclusion** 

It is crucial to explore network link prediction within financial networks as it aids in understanding how financial risks propagate among financial entities. By utilizing predictive insights from network analysis tools, we can improve our understanding and management of financial risks, potentially leading to more robust financial systems. In this chapter, we conduct link prediction experiments on a corporate bond dealer network. Initially, we apply various static link prediction methods to this dataset. However, due to the dynamic nature of the corporate bond trading network, using static methods fails to capture essential temporal information. 

Classical dynamic link prediction methods compile networks at different time intervals to create a sequence of snapshots. Yet, the choice of window length significantly affects the results. In this bond dealer network, if the window length is too short, the resulting network snapshot appears too random. Conversely, if the window length is too long, vital temporal information is lost. Therefore, in this chapter, we utilize an improved continuous dynamic 

93 

network framework to predict transactions in the dealer network. This framework incorporates a new neighborhood message aggregation module to address the limitations of the traditional mean message aggregation method. We test this method on our core-periphery structured corporate bond dealer network, and the experiments consistently demonstrate better results across different settings. 

94 

## **CHAPTER 5** 

## **CONCLUSION** 

In this thesis, we first explore the topological characteristics of dealers in the corporate bond dealer network, then discuss the relationship between these network topology characteristics and the market behaviors of dealers. Lastly, we propose an improved continuous dynamic link prediction model for transaction prediction tasks within the dealer network. 

In the first part, we analyze the topological characteristics of the dealer network, which has a core-periphery structure. Dealers with higher degrees are crucial for maintaining the network’s resilience. Unlike most traditional social networks, which exhibit assortative mixing, the corporate bond dealer network demonstrates disassortative mixing. We also compare dealer networks constructed from bonds with various ratings. Our analysis indicates that dealer networks constructed from bonds of different ratings exhibit similar topological characteristics. 

In the second part, we delve into the relationship between dealers’ topological characteristics and their trading behavior in the corporate bond market. We raise several questions. For example, if topological features vary and some dealers are crucial for network resilience, what advantages do these dealers gain in the bond market that others do not? Which dealers are more likely to incur losses, and which can sell bonds faster, thus reducing inventory holding time? To answer these questions, we conduct classical multivariate analysis on the relationships between dealers’ topological characteristics and their trading behaviors. Using a diverse set of the dependent variables, which include continuous, censored, and binary types, we apply various multivariate analysis techniques to discover the underlying dependencies. 

Finally, in the third part, building on our understanding of the relationship between dealers’ topological characteristics and their trading behaviors, we develop models to predict 

95 

future transaction. We first apply traditional network analysis techniques to this dataset. Subsequently, we explore the use of graph neural networks. We adopt an improved scheme for neighborhood message aggregation to improve over state of the art dynamic network models. This framework includes a new neighborhood message aggregation module to overcome the shortcomings of the traditional mean message aggregation method. We test this method on the corporate bond dealer network dataset, and the experiments consistently demonstrate improved results across different settings. 

96 

## **REFERENCES** 

- Adamic, L. A., & Adar, E. (2003). Friends and neighbors on the web. _Social networks_ , _25_ (3), 211–230. 

- Al Hasan, M., Chaoji, V., Salem, S., & Zaki, M. (2006). Link prediction using supervised learning. _Proceedings of the SDM06: workshop on link analysis, counter-terrorism and security_ , _30_ , 798–805. 

- Alexander, G. J., Edwards, A. K., & Ferri, M. G. (2000). The determinants of trading volume of high-yield corporate bonds. _Journal of Financial Markets_ , _3_ (2), 177– 204. 

- Allen, F., Babus, A., & Carletti, E. (2012). Asset commonality, debt maturity and systemic risk. _Journal of Financial Economics_ , _104_ (3), 519–534. 

- Allen, F., & Gale, D. (2000). Financial contagion. _Journal of political economy_ , _108_ (1), 1–33. 

- Allen, F., & Santomero, A. M. (1997). The theory of financial intermediation. _Journal of banking & finance_ , _21_ (11-12), 1461–1485. 

- Anand, K., & Bianconi, G. (2009). Entropy measures for networks: Toward an information theory of complex topologies. _Phys. Rev. E_ , _80_ , 045102. 

- Arcuri, M. C., Gandolfi, G., Manou, M., Verga, G., et al. (2020). What factors influence european corporate bond spread? _International Journal of Business and Management_ , _15_ (4 2020), 87–97. 

- Bai, T., Zhang, Y., Wu, B., & Nie, J.-Y. (2020). Temporal graph neural networks for social recommendation. _Proceedings of the 2020 IEEE International Conference on Big Data (Big Data)_ , 898–903. 

- Benston, G. J., & Smith, C. W. (1976). A transactions cost approach to the theory of financial intermediation. _The Journal of finance_ , _31_ (2), 215–231. 

- Bessembinder, H., Kahle, K. M., Maxwell, W. F., & Xu, D. (2008). Measuring abnormal bond performance. _The Review of Financial Studies_ , _22_ (10), 4219–4258. 

- Bessembinder, H., Maxwell, W., & Venkataraman, K. (2006). Market transparency, liquidity externalities, and institutional trading costs in corporate bonds. _Journal of Financial Economics_ , _82_ (2), 251–288. 

97 

- Blondel, V. D., Decuyper, A., & Krings, G. (2015). A survey of results on mobile phone datasets analysis. _EPJ data science_ , _4_ , 1–55. 

- Board, J., & Sutcliffe, C. (1988). The weekend effect in uk stock market returns. _Journal of Business Finance & Accounting_ , _15_ (2), 199–213. 

- Borgatti, S. P. (1997). Structural holes: Unpacking burt’s redundancy measures. _Connections_ , _20_ (1), 35–38. 

- Borgatti, S. P., Mehra, A., Brass, D. J., & Labianca, G. (2009). Network analysis in the social sciences. _science_ , _323_ (5916), 892–895. 

- Boss, M., Elsinger, H., Summer, M., & Thurner 4, S. (2004). Network topology of the interbank market. _Quantitative finance_ , _4_ (6), 677–684. 

- Bott, E., & Spillius, E. B. (2014). _Family and social network: Roles, norms and external relationships in ordinary urban families_ . Routledge. 

- Burt, R. S. (1992). _Structural holes: The social structure of competition_ . Harvard University Press. 

- Burt, R. S. (2015). Reinforced structural holes. _Social Networks_ , _43_ , 149–161. 

- Burt, R. S., & Knez, M. (1995). Kinds of third-party effects on trust. _Rationality and society_ , _7_ (3), 255–292. 

- Cannistraci, C. V., Alanis-Lobato, G., & Ravasi, T. (2013). From link-prediction in brain connectomes and protein interactomes to the local-community-paradigm in complex networks. _Scientific reports_ , _3_ (1), 1613. 

- Cao, S., Lu, W., & Xu, Q. (2015). Grarep: Learning graph representations with global structural information. _Proceedings of the 24th ACM international on conference on information and knowledge management_ , 891–900. 

- Cao, Z., Simon, T., Wei, S.-E., & Sheikh, Y. (2017). Realtime multi-person 2d pose estimation using part affinity fields. _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 7291–7299. 

- Chen, Y., Li, K., Yeo, C. K., & Li, K. (2023). Traffic forecasting with graph spatial– temporal position recurrent network. _Neural Networks_ , _162_ , 340–349. 

- Chen, Y.-L., Chen, M.-S., & Philip, S. Y. (2015). Ensemble of diverse sparsifications for link prediction in large-scale networks. _Proceedings of the 2015 IEEE International Conference on Data Mining_ , 51–60. 

98 

- Chiu, J., Eisenschmidt, J., & Monnet, C. (2020). Relationships in the interbank market. _Review of Economic Dynamics_ , _35_ , 170–191. 

- Cho, K., Van Merrienboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning phrase representations using rnn encoder-decoder for statistical machine translation. _arXiv preprint arXiv:1406.1078_ . 

- Colliard, J.-E., Foucault, T., & Hoffmann, P. (2021). Inventory management, dealers’ connections, and prices in over-the-counter markets. _The Journal of Finance_ , _76_ (5), 2199–2247. 

- Corso, G., Cavalleri, L., Beaini, D., Lio, P., & Velivckovic, P. (2020). Principal neighbourhood aggregation for graph nets. _Advances in Neural Information Processing Systems_ , _33_ , 13260–13271. 

- da Silva Soares, P. R., & Prudˆencio, R. B. C. (2012). Time series based link prediction. _The 2012 International Joint Conference on Neural Networks (IJCNN)_ , 1–7. 

- Davis, D., Lichtenwalter, R., & Chawla, N. V. (2013). Supervised methods for multirelational link prediction. _Social network analysis and mining_ , _3_ , 127–141. 

- Degryse, H., & Nguyen, G. (2004). Interbank exposure: An empirical examination of systemic risk in the belgian banking system. 

- Dehmamy, N., Barabasi, A.-L., & Yu, R. (2019). Understanding the representation power of graph neural networks in learning graph topology. _Advances in Neural Information Processing Systems_ , _32_ . 

- Di Maggio, M., Kermani, A., & Song, Z. (2017). The value of trading relations in turbulent times. _Journal of Financial Economics_ , _124_ (2), 266–284. 

- Diao, Z., Wang, X., Zhang, D., Liu, Y., Xie, K., & He, S. (2019). Dynamic spatial-temporal graph convolutional neural networks for traffic forecasting. _Proceedings of the AAAI conference on artificial intelligence_ , _33_ (01), 890–897. 

- Dick-Nielsen, J., Poulsen, T. K., & Rehman, O. (2023). Dealer networks and the cost of immediacy. _Proceedings of Paris December 2021 Finance Meeting EUROFIDAIESSEC_ . 

- Duffie, D., Garleanu, N., & Pedersen, L. H. (2005). Over-the-counter markets. _Econometrica_ , _73_ (6), 1815–1847. 

- Duffie, D., Garleanu, N., & Pedersen, L. H. (2007). Valuation in over-the-counter markets. _The Review of Financial Studies_ , _20_ (6), 1865–1900. 

99 

- Edwards, A. K., Harris, L. E., & Piwowar, M. S. (2007). Corporate bond market transaction costs and transparency. _The Journal of Finance_ , _62_ (3), 1421–1451. 

- Feng, Y., Hu, B., Lv, F., Liu, Q., Zhang, Z., & Ou, W. (2020). Atbrg: Adaptive targetbehavior relational graph network for effective recommendation. _Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval_ , 2231–2240. 

- Folino, F., & Pizzuti, C. (2013). An evolutionary multiobjective approach for community discovery in dynamic networks. _IEEE Transactions on Knowledge and Data Engineering_ , _26_ (8), 1838–1852. 

- Freeman, L. C. (1982). Centered graphs and the structure of ego networks. _Mathematical Social Sciences_ , _3_ (3), 291–304. 

- Freeman, L. C., Roeder, D., & Mulholland, R. R. (1979). Centrality in social networks: Ii. experimental results. _Social networks_ , _2_ (2), 119–141. 

- Fu, S., Wang, G., Xia, S., & Liu, L. (2020). Deep multi-granularity graph embedding for user identity linkage across social networks. _Knowledge-Based Systems_ , _193_ , 105301. 

- Gale, D. M., & Kariv, S. (2007). Financial networks. _American Economic Review_ , _97_ (2), 99–103. 

- Gao, C., Wang, X., He, X., & Li, Y. (2022). Graph neural networks for recommender system. _Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining_ , 1623–1625. 

- Goldstein, M. A., & Hotchkiss, E. S. (2020). Providing liquidity in an illiquid market: Dealer behavior in us corporate bonds. _Journal of Financial Economics_ , _135_ (1), 16–40. 

- Goldstein, M. A., Hotchkiss, E. S., & Nikolova, S. S. (2021). Dealer behavior and the trading of newly issued corporate bonds. _Available at SSRN 1022356_ . 

- Gould, R. V., & Fernandez, R. M. (1989). Structures of mediation: A formal approach to brokerage in transaction networks. _Sociological methodology_ , 89–126. 

- Granovetter, M. S. (1973). The strength of weak ties. _American journal of sociology_ , _78_ (6), 1360–1380. 

- Green, R. C., Hollifield, B., & Schurhoff, N. (2007a). Dealer intermediation and price behavior in the aftermarket for new bond issues. _Journal of Financial Economics_ , _86_ (3), 643–682. 

100 

- Green, R. C., Hollifield, B., & Schurhoff, N. (2007b). Financial intermediation and the costs of trading in an opaque market. _The Review of Financial Studies_ , _20_ (2), 275– 314. 

- Griffin, J. M., Hirschey, N., & Kruger, S. (2023). Do municipal bond dealers give their customers “fair and reasonable” pricing? _The Journal of Finance_ , _78_ (2), 887–934. 

- Grover, A., & Leskovec, J. (2016). Node2vec: Scalable feature learning for networks. _Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining_ , 855–864. 

- Guimera, R., & Sales-Pardo, M. (2009). Missing and spurious interactions and the reconstruction of complex networks. _Proceedings of the National Academy of Sciences_ , _106_ (52), 22073–22078. 

- Guo, X., Lehalle, C.-A., & Xu, R. (2022). Transaction cost analytics for corporate bonds. _Quantitative Finance_ , _22_ (7), 1295–1319. 

- Guo, Z., Yu, K., Jolfaei, A., Li, G., Ding, F., & Beheshti, A. (2022). Mixed graph neural network-based fake news detection for sustainable vehicular social networks. _IEEE Transactions on Intelligent Transportation Systems_ . 

- Hao, W., Zhan, H., Bao, X., Lu, Y., Zhou, Y., Dou, L., & Jin, J. (2019). Bond transaction link prediction based on dynamic network embedding and time series analysis. _Proceedings of the 2019 6th International Conference on Systems and Informatics (ICSAI)_ , 1471–1477. 

- Hendershott, T., Li, D., Livdan, D., & Schurhoff, N. (2020). Relationship trading in overthe-counter markets. _The Journal of Finance_ , _75_ (2), 683–734. 

- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. _Neural computation_ , _9_ (8), 1735–1780. 

- Huang, F., Yi, P., Wang, J., Li, M., Peng, J., & Xiong, X. (2022). A dynamical spatialtemporal graph neural network for traffic demand prediction. _Information Sciences_ , _594_ , 286–304. 

- Hubert, L., & Schultz, J. (1976). Quadratic assignment as a general data analysis strategy. _British journal of mathematical and statistical psychology_ , _29_ (2), 190–241. 

- Jaccard, P. (1901). Etude comparative de la distribution florale dans une portion des alpes et des jura. _Bull Soc Vaudoise Sci Nat_ , _37_ , 547–579. 

- Jin, E. M., Girvan, M., & Newman, M. E. (2001). Structure of growing social networks. _Physical review E_ , _64_ (4), 046132. 

101 

- Katz, L. (1953). A new status index derived from sociometric analysis. _Psychometrika_ , _18_ (1), 39–43. 

- Kazemi, M. S. (2022). Dynamic graph neural networks. In L. Wu, P. Cui, J. Pei, & L. Zhao (Eds.), _Graph neural networks: Foundations, frontiers, and applications_ (pp. 323– 349). Springer Singapore. 

- Kazemi, S. M., Goel, R., Eghbali, S., Ramanan, J., Sahota, J., Thakur, S., Wu, S., Smyth, C., Poupart, P., & Brubaker, M. (2019). Time2vec: Learning a vector representation of time. _arXiv preprint arXiv:1907.05321_ . 

- Kazemi, S. M., Goel, R., Jain, K., Kobyzev, I., Sethi, A., Forsyth, P., & Poupart, P. (2020). Representation learning for dynamic graphs: A survey. _The Journal of Machine Learning Research_ , _21_ (1), 2648–2720. 

- Kazemi, S. M., & Poole, D. (2018). Simple embedding for link prediction in knowledge graphs. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, & R. Garnett (Eds.), _Advances in neural information processing systems_ (Vol. 31). Curran Associates, Inc. 

- Kim, H., & Anderson, R. (2012). Temporal node centrality in complex networks. _Physical Review E_ , _85_ (2), 026107. 

- Kipf, T. N., & Welling, M. (2017). Semi-supervised classification with graph convolutional networks. _Proceedings of the International Conference on Learning Representations_ . 

- Kossinets, G., & Watts, D. J. (2009). Origins of homophily in an evolving social network. _American journal of sociology_ , _115_ (2), 405–450. 

Krackhardt, D. (1987). Cognitive social structures. _Social networks_ , _9_ (2), 109–134. 

- Krackhardt, D. (1988). Predicting with networks: Nonparametric multiple regression analysis of dyadic data. _Social networks_ , _10_ (4), 359–381. 

- Kumar, A., Singh, S. S., Singh, K., & Biswas, B. (2020). Link prediction techniques, applications, and performance: A survey. _Physica A: Statistical Mechanics and its Applications_ , _553_ , 124289. 

- Kumar, S., Zhang, X., & Leskovec, J. (2019). Predicting dynamic embedding trajectory in temporal interaction networks. _Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining_ , 1269–1278. 

- Lee, S. H., Kim, P.-J., & Jeong, H. (2006). Statistical properties of sampled networks. _Physical review E_ , _73_ (1), 016102. 

102 

- Leicht, E. A., Holme, P., & Newman, M. E. (2006). Vertex similarity in networks. _Physical Review E_ , _73_ (2), 026120. 

- Leman, A., & Weisfeiler, B. (1968). A reduction of a graph to a canonical form and an algebra arising during this reduction. _Nauchno-Technicheskaya Informatsiya_ , _2_ (9), 12–16. 

- Lester, B., Rocheteau, G., & Weill, P.-O. (2015). Competing for order flow in otc markets. _Journal of Money, Credit and Banking_ , _47_ (S2), 77–126. 

- Li, A., Cornelius, S. P., Liu, Y.-Y., Wang, L., & Barabasi, A.-L. (2017). The fundamental advantages of temporal networks. _Science_ , _358_ (6366), 1042–1046. 

- Li, D., & Schurhoff, N. (2019). Dealer networks. _The Journal of Finance_ , _74_ (1), 91–144. 

- Li, P., Wang, Y., Wang, H., & Leskovec, J. (2020). Distance encoding: Design provably more powerful neural networks for graph representation learning. 

- Li, S., He, J., & Zhuang, Y. (2010). A network model of the interbank market. _Physica A: Statistical Mechanics and its Applications_ , _389_ (24), 5587–5593. 

- Liben-Nowell, D., & Kleinberg, J. (2003). The link prediction problem for social networks. _Proceedings of the twelfth international conference on Information and knowledge management_ , 556–559. 

- Lichtenwalter, R. N., & Chawla, N. V. (2012). Vertex collocation profiles: Subgraph counting for link analysis and prediction. _Proceedings of the 21st international conference on World Wide Web_ , 1019–1028. 

- Lichtenwalter, R. N., Lussier, J. T., & Chawla, N. V. (2010). New perspectives and methods in link prediction. _Proceedings of the 16th ACM SIGKDD international conference on Knowledge discovery and data mining_ , 243–252. 

- Lin, D., Wu, J., Yuan, Q., & Zheng, Z. (2020). Modeling and understanding ethereum transaction records via a complex network approach. _IEEE Transactions on Circuits and Systems II: Express Briefs_ , _67_ (11), 2737–2741. 

- Liu, C., Li, Y., Lin, H., & Zhang, C. (2023). Gnnrec: Gated graph neural network for session-based social recommendation model. _Journal of Intelligent Information Systems_ , _60_ (1), 137–156. 

- Liu, M., Tu, Z., Su, T., Wang, X., Xu, X., & Wang, Z. (2024). Behaviornet: A fine-grained behavior-aware network for dynamic link prediction. _ACM Trans. Web_ , _18_ (2). 

103 

- Liu, Y., Ma, J., & Li, P. (2022). Neural predicting higher-order patterns in temporal networks. _Proceedings of the ACM Web Conference 2022_ , 1340–1351. 

- Liu, Z., Zhang, Q.-M., Lu, L., & Zhou, T. (2011). Link prediction in complex networks: A local naive bayes model. _Europhysics Letters_ , _96_ (4), 48007. 

- Ma, Y., Guo, Z., Ren, Z., Tang, J., & Yin, D. (2020). Streaming graph neural networks. _Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval_ , 719–728. 

- Manessi, F., Rozza, A., & Manzo, M. (2020). Dynamic graph convolutional networks. _Pattern Recognition_ , _97_ , 107000. 

- Maron, H., Ben-Hamu, H., Shamir, N., & Lipman, Y. (2018). Invariant and equivariant graph networks. _arXiv preprint arXiv:1812.09902_ . 

- Martinez, V., Berzal, F., & Cubero, J.-C. (2016). A survey of link prediction in complex networks. _ACM computing surveys (CSUR)_ , _49_ (4), 1–33. 

- Melitz, J., & Pardue, M. (1973). The demand and supply of commercial bank loans. _Journal of Money, Credit and Banking_ , _5_ (2), 669–692. 

- Menon, A. K., & Elkan, C. (2011). Link prediction via matrix factorization. _Proceedings of the Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2011, Athens, Greece, September 5-9, 2011, Proceedings, Part II 22_ , 437–452. 

- Micheli, A., Sona, D., & Sperduti, A. (2004). Contextual processing of structured data by recursive cascade correlation. _IEEE Transactions on Neural Networks_ , _15_ (6), 1396– 1410. 

- Min, S., Gao, Z., Peng, J., Wang, L., Qin, K., & Fang, B. (2021). Stgsn—a spatial–temporal graph neural network framework for time-evolving social networks. _KnowledgeBased Systems_ , _214_ , 106746. 

- Mitzenmacher, M. (2004). A brief history of generative models for power law and lognormal distributions. _Internet mathematics_ , _1_ (2), 226–251. 

- Morris, C., Ritzert, M., Fey, M., Hamilton, W. L., Lenssen, J. E., Rattan, G., & Grohe, M. (2019). Weisfeiler and leman go neural: Higher-order graph neural networks. _Proceedings of the AAAI conference on artificial intelligence_ , _33_ (01), 4602–4609. 

- Murphy, R., Srinivasan, B., Rao, V., & Ribeiro, B. (2019). Relational pooling for graph representations. _Proceedings of the International Conference on Machine Learning_ , 4663–4673. 

104 

- Newman, M. E. (2002). Assortative mixing in networks. _Physical review letters_ , _89_ (20), 208701. 

- Onnela, J., Saramaki, J., Hyvonen, J., Szabo, G., Lazer, D., Kaski, K., Kertesz, J., & Barabasi, A. (2007). Structure and tie strengths in mobile communication networks. _Proceedings of the national academy of sciences_ , _104_ (18), 7332–7336. 

- Ou, M., Cui, P., Pei, J., Zhang, Z., & Zhu, W. (2016). Asymmetric transitivity preserving graph embedding. _Proceedings of the 22nd ACM SIGKDD international conference on Knowledge discovery and data mining_ , 1105–1114. 

Page, E. (1961). Cumulative sum charts. _Technometrics_ , _3_ (1), 1–9. 

- Pareja, A., Domeniconi, G., Chen, J., Ma, T., Suzumura, T., Kanezashi, H., Kaler, T., Schardl, T., & Leiserson, C. (2020). Evolvegcn: Evolving graph convolutional networks for dynamic graphs. _Proceedings of the AAAI conference on artificial intelligence_ , _34_ (04), 5363–5370. 

- Perozzi, B., Al-Rfou, R., & Skiena, S. (2014). Deepwalk: Online learning of social representations. _Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining_ , 701–710. 

- Pesek, B. P. (1970). Bank’s supply function and the equilibrium quantity of money. _The Canadian Journal of Economics/Revue canadienne d’Economique_ , _3_ (3), 357–385. 

- Pinter, G., Wang, C., & Zou, J. (2024). Size discount and size penalty: Trading costs in bond markets. _The Review of Financial Studies_ , hhae007. 

- Rapp, A. C. (2018). _Essays on corporate bond market liquidity and dealer behavior_ . CentER, Tilburg University. 

- Ravasz, E., Somera, A. L., Mongru, D. A., Oltvai, Z. N., & Barabasi, A.-L. (2002). Hierarchical organization of modularity in metabolic networks. _science_ , _297_ (5586), 1551–1555. 

- Ribeiro, L. F., Saverese, P. H., & Figueiredo, D. R. (2017). Struc2vec: Learning node representations from structural identity. _Proceedings of the 23rd ACM SIGKDD international conference on knowledge discovery and data mining_ , 385–394. 

- Rieger, J. R. (2017). _Bond market match-up: U.s. corporate vs. muni bonds_ . S P Dow Jones Indices. 

- Rossi, E., Chamberlain, B., Frasca, F., Eynard, D., Monti, F., & Bronstein, M. (2020). Temporal graph networks for deep learning on dynamic graphs. _arXiv preprint arXiv:2006.10637_ . 

105 

- Rummele, N., Ichise, R., & Werthner, H. (2015). Exploring supervised methods for temporal link prediction in heterogeneous social networks. _Proceedings of the 24th international conference on world wide web_ , 1363–1368. 

- Salton, G., & McGill, M. J. (1986). _Introduction to modern information retrieval_ . McGrawHill, Inc. 

- Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., & Monfardini, G. (2008). The graph neural network model. _IEEE transactions on neural networks_ , _20_ (1), 61–80. 

- Schlichtkrull, M., Kipf, T. N., Bloem, P., Van Den Berg, R., Titov, I., & Welling, M. (2018). Modeling relational data with graph convolutional networks. _Proceedings of The Semantic Web: 15th International Conference, ESWC 2018, Heraklion, Crete, Greece, June 3–7, 2018, Proceedings 15_ , 593–607. 

- Schultz, P. (2001). Corporate bond trading costs: A peek behind the curtain. _The Journal of Finance_ , _56_ (2), 677–698. 

- Seo, Y., Defferrard, M., Vandergheynst, P., & Bresson, X. (2018). Structured sequence modeling with graph convolutional recurrent networks. _Proceedings of the Neural Information Processing: 25th International Conference, ICONIP 2018, Siem Reap, Cambodia, December 13-16, 2018, Proceedings, Part I 25_ , 362–373. 

- Shante, V. K., & Kirkpatrick, S. (1971). An introduction to percolation theory. _Advances in Physics_ , _20_ (85), 325–357. 

- Shi, L., Zhang, Y., Cheng, J., & Lu, H. (2019). Skeleton-based action recognition with directed graph neural networks. _Proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , 7912–7921. 

- Sole, R. V., & Valverde, S. (2004). Information theory of complex networks: On evolution and architectural constraints. In _Complex networks_ (pp. 189–207). Springer. 

- Song, C., Wang, B., Jiang, Q., Zhang, Y., He, R., & Hou, Y. (2021). Social recommendation with implicit social influence. _Proceedings of the 44th international ACM SIGIR conference on research and development in information retrieval_ , 1788–1792. 

- Song, W., Xiao, Z., Wang, Y., Charlin, L., Zhang, M., & Tang, J. (2019). Session-based social recommendation via dynamic graph attention networks. _Proceedings of the Twelfth ACM international conference on web search and data mining_ , 555–563. 

- Sorensen, T. (1948). A method of establishing groups of equal amplitude in plant sociology based on similarity of species content and its application to analyses of the vegetation on danish commons. _Biologiske skrifter_ , _5_ , 1–34. 

106 

- Sperduti, A., & Starita, A. (1997). Supervised neural networks for the classification of structures. _IEEE Transactions on Neural Networks_ , _8_ (3), 714–735. 

- Spulber, D. F. (1996). Market microstructure and intermediation. _Journal of Economic perspectives_ , _10_ (3), 135–152. 

- Szabo, F. E. (2015). K. In F. E. Szabo (Ed.), _The linear algebra survival guide_ (pp. 190– 193). Academic Press. 

- Tan, F., Xia, Y., & Zhu, B. (2014). Link prediction in complex networks: A mutual information perspective. _PloS one_ , _9_ (9), e107056. 

- Temizsoy, A., Iori, G., & Montes-Rojas, G. (2015). The role of bank relationships in the interbank market. _Journal of Economic Dynamics and Control_ , _59_ , 118–141. 

- Towey, R. E. (1974). Money creation and the theory of the banking firm. _The Journal of Finance_ , _29_ (1), 57–72. 

- Trivedi, R., Dai, H., Wang, Y., & Song, L. (2017). Know-evolve: Deep temporal reasoning for dynamic knowledge graphs. _Proceedings of the International conference on machine learning_ , 3462–3471. 

- Trivedi, R., Farajtabar, M., Biswal, P., & Zha, H. (2019). Dyrep: Learning representations over dynamic graphs. _Proceedings of the International conference on learning representations_ . 

- Upper, C., & Worms, A. (2004). Estimating bilateral exposures in the german interbank market: Is there a danger of contagion? _European economic review_ , _48_ (4), 827– 849. 

- Vachon, M., Sheldon, A., Lancee, W., Lyall, W., Rogers, J., & Freeman, S. (1982). Correlates of enduring distress patterns following bereavement: Social network, life situation and personality. _Psychological Medicine_ , _12_ (4), 783–788. 

- Vashishth, S., Sanyal, S., Nitin, V., & Talukdar, P. (2020). Composition-based multi-relational graph convolutional networks. _Proceedings of the International Conference on Learning Representations_ . 

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, & R. Garnett (Eds.), _Proceedings of advances in neural information processing systems_ (Vol. 30). Curran Associates, Inc. 

107 

- Velivckovic, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., & Bengio, Y. (2017). Graph attention networks. _arXiv preprint arXiv:1710.10903_ . 

- Velivckovic, P., Ying, R., Padovano, M., Hadsell, R., & Blundell, C. (2019). Neural execution of graph algorithms. _arXiv preprint arXiv:1910.10593_ . 

- Wang, J., Ding, K., Zhu, Z., & Caverlee, J. (2021). Session-based recommendation with hypergraph attention networks. _Proceedings of the 2021 SIAM International Conference on Data Mining (SDM)_ , 82–90. 

- Wang, Y., Chang, Y.-Y., Liu, Y., Leskovec, J., & Li, P. (2021). Inductive representation learning in temporal networks via causal anonymous walks. _Proceedings of the International Conference on Learning Representations_ . 

- Wang, Y., Zheng, J., Du, Y., Huang, C., & Li, P. (2022). Traffic-ggnn: Predicting traffic flow via attentional spatial-temporal gated graph neural networks. _IEEE Transactions on Intelligent Transportation Systems_ , _23_ (10), 18423–18432. 

- Weber, M., Domeniconi, G., Chen, J., Weidele, D. K. I., Bellei, C., Robinson, T., & Leiserson, C. E. (2019). Anti-money laundering in bitcoin: Experimenting with graph convolutional networks for financial forensics. _arXiv preprint arXiv:1908.02591_ . 

- Wei, X., Liu, Y., Sun, J., Jiang, Y., Tang, Q., & Yuan, K. (2023). Dual subgraph-based graph neural network for friendship prediction in location-based social networks. _ACM Transactions on Knowledge Discovery from Data_ , _17_ (3), 1–28. 

- Wu, H., Song, C., Ge, Y., & Ge, T. (2022). Link prediction on complex networks: An experimental survey. _Data Science and Engineering_ , _7_ (3), 253–278. 

- Wu, L., Cui, P., Pei, J., & Zhao, L. (2022). _Graph neural networks: Foundations, frontiers, and applications_ . Springer Singapore. 

- Wu, L., Cui, P., Pei, J., Zhao, L., & Guo, X. (2022). Graph neural networks: Foundation, frontiers and applications. _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , 4840–4841. 

- Xenaros, A., Karampelas, P., & Lekea, I. (2016). Profiling individuals based on email analysis and ego networks: A visualization technique. _Proceedings of the 2016 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining_ , 1262–1269. 

- Xia, L., Huang, C., Xu, Y., Dai, P., & Bo, L. (2022). Multi-behavior graph neural networks for recommender system. _IEEE Transactions on Neural Networks and Learning Systems_ . 

108 

- Xu, D., Ruan, C., Korpeoglu, E., Kumar, S., & Achan, K. (2019). Self-attention with functional time representation learning. _Advances in neural information processing systems_ , _32_ . 

- Xu, D., Ruan, C., Korpeoglu, E., Kumar, S., & Achan, K. (2020). Inductive representation learning on temporal graphs. _arXiv preprint arXiv:2002.07962_ . 

- Xu, D., Cheng, W., Luo, D., Liu, X., & Zhang, X. (2019). Spatio-temporal attentive rnn for node classification in temporal attributed graphs. _Proceedings of the IJCAI_ , 3947– 3953. 

- Xu, K., Hu, W., Leskovec, J., & Jegelka, S. (2018). How powerful are graph neural networks? _arXiv preprint arXiv:1810.00826_ . 

- Xu, T., He, J., & Li, S. (2016). A dynamic network model for interbank market. _Physica A: Statistical Mechanics and its Applications_ , _463_ , 131–138. 

- Xu, Z., Pu, C., & Yang, J. (2016). Link prediction based on path entropy. _Physica A: Statistical Mechanics and its Applications_ , _456_ , 294–301. 

- Yan, S., Xiong, Y., & Lin, D. (2018). Spatial temporal graph convolutional networks for skeleton-based action recognition. _Proceedings of the AAAI conference on artificial intelligence_ , _32_ (1). 

- You, J., Du, T., & Leskovec, J. (2022). Roland: Graph learning framework for dynamic graphs. _Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_ , 2358–2366. 

- Yu, B., Yin, H., & Zhu, Z. (2018). Spatio-temporal graph convolutional networks: A deep learning framework for traffic forecasting. _Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence_ . 

- Zhang, H. (2022). A deep learning approach to dynamic interbank network link prediction. _International Journal of Financial Studies_ , _10_ (3), 54. 

- Zhang, M., & Chen, Y. (2018). Link prediction based on graph neural networks. _Advances in neural information processing systems_ , _31_ . 

- Zhang, M., Cui, Z., Neumann, M., & Chen, Y. (2018). An end-to-end deep learning architecture for graph classification. _Proceedings of the AAAI conference on artificial intelligence_ , _32_ (1). 

- Zhang, M., Li, P., Xia, Y., Wang, K., & Jin, L. (2021). Labeling trick: A theory of using graph neural networks for multi-node representation learning. _Advances in Neural Information Processing Systems_ , _34_ , 9061–9073. 

109 

- Zhao, L., Song, Y., Zhang, C., Liu, Y., Wang, P., Lin, T., Deng, M., & Li, H. (2019). T-gcn: A temporal graph convolutional network for traffic prediction. _IEEE transactions on intelligent transportation systems_ , _21_ (9), 3848–3858. 

- Zhou, T., Lu, L., & Zhang, Y.-C. (2009). Predicting missing links via local information. _The European Physical Journal B_ , _71_ , 623–630. 

ProQuest Number: 31241912 

## INFORMATION TO ALL USERS 

The quality and completeness of this reproduction is dependent on the quality and completeness of the copy made available to ProQuest. 

## Distributed by ProQuest LLC (        ). 2024 

Copyright of the Dissertation is held by the Author unless otherwise noted. 

This work may be used in accordance with the terms of the Creative Commons license or other rights statement, as indicated in the copyright statement or in the metadata associated with this work. Unless otherwise specified in the copyright statement or the metadata, all rights are reserved by the copyright holder. 

This work is protected against unauthorized copying under Title 17, United States Code and other applicable copyright laws. 

Microform Edition where available © ProQuest LLC. No reproduction or digitization of the Microform Edition is authorized without permission of ProQuest LLC. 

## ProQuest LLC 

789 East Eisenhower Parkway P.O. Box 1346 Ann Arbor, MI 48106 - 1346 USA 

