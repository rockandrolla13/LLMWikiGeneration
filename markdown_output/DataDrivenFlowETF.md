## **Data-Driven Trade Flow Decomposition for Exchange-Traded Funds and their Constituents** 

Nicolas Petit 

Department of Statistics University of Oxford Oxford, Oxfordshire, United Kingdom Oxford-Man Institute of Quantitative Finance University of Oxford Oxford, Oxfordshire, United Kingdom nicolas.petit@stats.ox.ac.uk 

Mihai Cucuringu 

Department of Mathematics University of California, Los Angeles Los Angeles, California, USA Department of Statistics University of Oxford Oxford, Oxfordshire, United Kingdom Oxford-Man Institute of Quantitative Finance 

## Álvaro Cartea 

Oxford-Man Institute of Quantitative Finance 

University of Oxford Oxford, Oxfordshire, United Kingdom Mathematical Institute University of Oxford Oxford, Oxfordshire, United Kingdom alvaro.cartea@maths.ox.ac.uk 

University of Oxford Oxford, Oxfordshire, United Kingdom mihai@math.ucla.edu 

## **Abstract** 

This paper presents a novel data-driven methodology for decomposing trade flow based on the co-occurrence patterns between Exchange-Traded Funds (ETFs) and their constituent securities. Lu et al. [19, 29] use a fixed set of rules for trade clustering to demonstrate the economic utility of trade flow decomposition. In contrast, we propose a purely data-driven approach. We employ unsupervised learning techniques with a set of features that capture the joint informational content between ETFs and their underlying constituents. Clustering is performed using principal component analysis for dimensionality reduction followed by _𝑘_ -means++ for clustering. 

We demonstrate the economic utility of this decomposition with an application to portfolio trading. We construct factor-mimicking portfolios based on the conditional order imbalances computed within each cluster, orthogonalised to a baseline set of common risk factors. We use data from SPY and its constituents between January 1, 2018 and December 31, 2021 to test our methodology and find that a subset of factor-mimicking portfolios achieve statistically significant Sharpe ratios. These results demonstrate that our datadriven trade flow decomposition captures economically meaningful trading patterns, and that the conditional order imbalances capture information beyond what is available from unconditional order imbalance. 

## **CCS Concepts** 

• **Applied computing** → **Forecasting** ; **Economics** ; • **Mathematics of computing** → **Time series analysis** ; **Dimensionality reduction** ; **Cluster analysis** ; **Regression analysis** . 

## **Keywords** 

Exchange-traded funds, portfolio management, clustering, time series analysis, forecasting. 

## **ACM Reference Format:** 

Nicolas Petit, Mihai Cucuringu, and Álvaro Cartea. 2025. Data-Driven Trade Flow Decomposition for Exchange-Traded Funds and their Constituents. In _6th ACM International Conference on AI in Finance (ICAIF ’25), November 15–18, 2025, Singapore, Singapore._ ACM, New York, NY, USA, 9 pages. https: //doi.org/10.1145/3768292.3770434 

## **1 Introduction** 

## **1.1 Exchange-Traded Funds** 

ETFs offer investors a direct and cost-effective way to access diversified portfolio exposure. By purchasing a single ETF share, investors gain exposure to the underlying basket of securities without needing to purchase each constituent individually. Currently, over 14,000 ETFs are traded globally [1], with passive index-tracking funds representing a rapidly growing share of equity market ownership. ETFs tracking the S&P 500 (such as SPY by State Street Investment Management, VOO by Vanguard, and IVV by iShares) are some of the most liquid products in the world. These three funds are currently the largest ETFs by assets under management (AUM), each with assets totalling approximately 700 billion USD. The rise in popularity of these funds underscores the significance of ETFs as an asset class. A key factor in the success of ETFs lies in their unique creation/redemption mechanism. Authorised participants (APs) deliver or receive a specified portfolio or cash in exchange for a corresponding number of ETF shares. This creation/redemption mechanism enables arbitrage that keeps the ETF’s market price in line with its net asset value (NAV). The NAV of a fund is the theoretical “fair value per share" and is defined as 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0001-21.png)


This work is licensed under a Creative Commons Attribution 4.0 International License. _ICAIF ’25, Singapore, Singapore_ 

© 2025 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-2220-2/25/11 https://doi.org/10.1145/3768292.3770434 

A fund’s NAV is typically calculated once per day using closing auction prices. The indicative NAV or intraday NAV (iNAV) provides a real-time estimate of an ETF’s fair value by marking the holdings of the fund to current market prices. When the market price of an ETF deviates significantly from its iNAV, arbitrageurs can exploit this 

569 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Petit et al. 

discrepancy through various trading strategies involving the ETF, related futures contracts, and the underlying constituent securities. 

Statistical arbitrage in ETFs is a common trading strategy in which traders take offsetting positions in ETFs, their underlying constituents, and related futures, expecting any premium or discount to converge toward zero. The profitability of such strategies depends critically on transaction costs and borrow fees for short positions. Timing is equally important, as the expected duration of the price discrepancy affects the strategy’s viability. When a mispricing becomes sufficiently large, APs can engage in the full creation/redemption process to correct the mispricing. 

Importantly, analysing the trading patterns between ETFs and their constituent securities may provide valuable insight into market activity. We use these relationships to decompose trade order flow into distinct clusters, which can be used in downstream tasks such as portfolio construction. 

## **1.2 Trade Flow Decomposition** 

Trade flow decomposition partitions trades into clusters based on trade flow characteristics, assuming that order flow can be meaningfully segmented to reflect distinct trading behaviours. 

Lu et al. [19, 29] implement such a decomposition, using a rulebased approach with _𝐾_ = 4 clusters. The authors categorise trades based on their temporal co-occurrence with other trades within a 2 _𝜏_ time neighbourhood (Figure 1). This clustering approach established the practical utility of trade flow decomposition, and demonstrated substantial improvements in forecasting performance. This was evidenced by increases in the in-sample adjusted _𝑅_[2] for predicting both contemporaneous and forward-looking returns. Moreover, the portfolio trading strategies that used conditional order imbalances (COIs) as trading signals achieved statistically significant Sharpe ratios. While this approach is easily interpretable, the clustering criteria are fixed _a priori_ , rather than learned from the data, and may therefore not capture the most economically meaningful decomposition. Furthermore, their clustering analysis relies solely on information from S&P 500 constituents, without considering the rich information present in ETF-constituent interactions. 

Order flow imbalance (OFI) has been extensively studied in the market microstructure literature and has been shown to exhibit significant explanatory power for both contemporaneous and forwardlooking returns, in both the single-asset and multi-asset settings [6]. A related line of recent work [24] introduced the Decomposed OFI, which extends the standard order flow imbalance by incorporating information about order book event types, namely additions, cancellations, and trades, and by constructing an imbalance measure for each component separately. Their results demonstrate significant improvements in forward-looking predictive performance, highlighting the benefits of conditioning on event type. The present study addresses a similar problem but adopts a different decomposition principle. Here, we decompose trade order flow based on co-occurrence behaviour across instruments rather than on order type. 

## **1.3 Main Contributions** 

We propose a novel data-driven trade flow decomposition framework that uses the joint informational content between ETFs and their underlying constituents. The analysis is conducted in an unsupervised setting, where there are no ground-truth labels for classification. For each trade, we construct 16 features (Table 1), which capture the state of the market at the time of the trade. Our methodology applies principal component analysis (PCA) for dimensionality reduction, followed by _𝑘_ -means++ clustering to identify distinct categories of trading patterns. This method incorporates information from both ETF and constituent markets. 

We demonstrate the economic utility of our approach through portfolio trading applications using trades from SPY and its constituents between January 1, 2018 and December 31, 2021. Our results demonstrate that factor-mimicking portfolios constructed from cluster-specific order imbalances, orthogonalised to standard risk factors, achieve statistically significant Sharpe ratios for a subset of clusters. These results indicate that cluster-specific order imbalances contain valuable predictive information beyond what is captured by order imbalance (OI) alone. 

## **2 Methodology** 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0002-13.png)


**----- Start of picture text -----**<br>
Isolated Trade Same Security Only<br>( ) ( )<br>𝑡 − 𝜏 𝑡 𝑡 +  𝜏 𝑡 − 𝜏 𝑡 𝑡 +  𝜏<br>Other Securities Only Both Same & Other Securities<br>( ) ( )<br>𝑡 − 𝜏 𝑡 𝑡 +  𝜏 𝑡 − 𝜏 𝑡 𝑡 +  𝜏<br>Central Trade Same Security Other Securities<br>**----- End of picture text -----**<br>


**Figure 1: Lu et al.’s rule-based classification of trades into** _𝑲_ = 4 **clusters based on temporal co-occurrence within a** _𝝉_ **neighbourhood [19, 29]. The four clusters represent: isolated trades, trades co-occurring only with the same security, trades co-occurring only with other securities, and trades co-occurring with both the same and other securities.** 

Our methodology follows a four-step process: feature construction, dimensionality reduction, clustering, and portfolio construction. Feature construction involves computing a feature vector for each trade that captures the joint market microstructure information from both the ETF and the constituent limit order books. These features are normalised using rolling percentile ranks computed over historical lookback windows matched by time-of-day. 

Next, we apply dimensionality reduction to address the inherent correlations among features (e.g., trade counts are positively correlated with notional volumes). We apply PCA for dimensionality reduction to project the data into a lower-dimensional space that captures the majority of variance in the original feature set. Next, we employ _𝑘_ -means++ clustering on the transformed feature space, using a 14-day sliding window that advances daily. To ensure consistent cluster identities over time, we align both the principal components and cluster labels across consecutive windows. Finally, the resulting clusters are used for portfolio construction. 

570 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Data-Driven Trade Flow Decomposition for ETFs and their Constituents 

The following section defines the mathematical setup, before we detail each component of our methodology. 

## **2.1 Mathematical setup** 

We first define our universe of securities to include both the ETF E and all of its underlying constituent securities M. We index the securities by _𝑖_ ∈{E}[�] M and for each _𝑖_ enumerate the sequence of trades in chronological order by _𝑛_ : 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-05.png)


Each trade 𝓽 _𝑖,𝑛_ consists of a direction _𝜀𝑖,𝑛_ ∈{−1 _,_ +1} (seller-initiated or buyer-initiated), price _𝑝𝑖,𝑛_ , share quantity _𝜐𝑖,𝑛_ ∈ N, and timestamp _𝑡𝑖,𝑛_ . Prices are restricted to positive integer multiples of the tick size _𝜗_ . For most equities listed on U.S. exchanges, the tick size is _𝜗_ = 0 _._ 01 USD. We use information derived from the limit order books of all securities in our universe to assign each trade 𝓽 _𝑖,𝑛_ to a cluster _𝑘𝑖,𝑛_ ∈{1 _, . . . , 𝐾_ }. 

## **2.2 Feature Construction** 

We construct a _𝐷_ = 16 dimensional feature vector _𝒙𝑖,𝑛_ ∈ R _[𝐷]_ for each central trade ( _𝑖,𝑛_ ) to capture co-occurrence patterns within a time neighbourhood of length 2 _𝜏_ . These features measure trade activity in the surrounding 2 _𝜏_ window by aggregating across three categorical dimensions: 

- **Direction** : Same sign ( _𝜀 𝑗,𝑚_ = _𝜀𝑖,𝑛_ ) or opposite sign ( _𝜀 𝑗,𝑚_ = − _𝜀𝑖,𝑛_ ), 

- **Market** : ETF ( _𝑗_ = E) or constituent ( _𝑗_ ∈M), 

- **Time Relation** : Before ( _𝑡𝑖,𝑛_ − _𝜏,𝑡𝑖,𝑛_ ) or after ( _𝑡𝑖,𝑛,𝑡𝑖,𝑛_ + _𝜏_ ). 

For each of the eight (2 × 2 × 2) combinations of these, we calculate both the trade count and the notional traded. The resulting 16 features are enumerated in Table 1. For instance, feature _𝒙_[(][9][)] _𝑖,𝑛_ represents the total notional traded in the constituents occurring before the central trade with the same direction: 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-13.png)


where � · � denotes the Iverson bracket. 

**Table 1: Feature indices showing trade counts and notional traded amounts grouped by direction (same or opposite sign), market (ETF or constituent), and timing (before or after).** 

|**Direction**|**Market**<br>**Time Relation**|**# Trades**<br>**Notional**|
|---|---|---|
|Same|ETF<br>Before<br>After|1<br>2<br>3<br>4|
||Constituents<br>Before<br>After|5<br>6<br>7<br>8|
|Opposite|ETF<br>Before<br>After|9<br>10<br>11<br>12|
||Constituents<br>Before<br>After|13<br>14<br>15<br>16|




![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-17.png)


**----- Start of picture text -----**<br>
20<br>5 [th] - 95 [th] Percentiles<br>Interquartile Range<br>15 Median<br>10<br>5<br>0<br>9:30 10:00 11:00 12:00 13:00 14:00 15:00 16:00<br>Time of Day (EST)<br>1]−<br>[s<br>MO<br> 𝜆<br>Arrival Rate<br>**----- End of picture text -----**<br>


**Figure 2: Typical U-shaped intraday trading pattern for SPY between January 1, 2017 and December 31, 2021.** 

_2.2.1 Feature normalisation._ Feature normalisation is performed by computing the percentile rank of each feature value relative to its historical distribution over a lookback window of 90 days. Given the well-documented U-shaped pattern of intraday trading activity [13, 20, 28] (Figure 2), we divide the trading day into equallysized buckets and compare each feature value with historical values from the same time-of-day bucket. This procedure ensures that comparisons are made under similar market conditions. We fix the bucket size at 65 minutes, resulting in six equal-sized buckets for standard U.S. market hours of 09:30–16:00 EST. 

Let W _𝑖,𝑛_ denote the set of indices of historical trades in symbol _𝑖_ within the same time-of-day bucket over the 90 day lookback period: 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-21.png)


where ℬ : R →{1 _, . . . ,_ 6} denotes the mapping from timestamp to corresponding time-of-day bucket index. The normalised feature value _𝑥_ ˜[(] _[𝑗]_[)] _[𝑗]_[-th component of the feature vector is] _𝑖,𝑛_[for the] 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-23.png)


## **2.3 Dimensionality Reduction** 

To address the inherent correlations among features, we apply PCA for dimensionality reduction. For a given _𝑀_ ≤ _𝐷_ , we solve the PCA maximisation problem on _𝑿_[�] _𝑑_ ∈ R _[𝑁][𝑑]_[×] _[𝐷]_ : 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-26.png)


where 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0003-28.png)


is the empirical covariance matrix of the normalised features _𝒙_ ˜ , and _𝑪_ = _𝑰_ − 11[⊤] / _𝑁𝑑_ is the _𝑁𝑑_ × _𝑁𝑑_ centring matrix, so that the means of the columns of _𝑪𝑿_[�] _𝑑_ are zero. Even when the eigenvalues of the covariance matrix[�] **𝚺** _𝒙_ ˜ _,𝑑_ are distinct, the problem as formulated in (1) does not have a unique solution due to the sign ambiguity of principal components. This ambiguity is addressed by aligning principal components between batches for temporal stability, ensuring that the cosine similarity between consecutive batches is positive. 

571 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Petit et al. 

We project onto the lower-dimensional space and work with the principal component scores _𝒕𝑖,𝑛_ ∈ R _[𝑀]_ given by the rows of _𝑿_[�] _𝑑 𝑽𝑑_ . The dimension _𝑀_ is calibrated by selecting the smallest _𝑀_ such that the explained variance ratio (EVR) exceeds the 90% threshold (see Appendix A.2). 

_2.3.1 Principal component alignment._ Due to the sign ambiguity inherent in PCA, principal components can flip signs arbitrarily between time windows, potentially causing the same underlying factor to appear with opposite loadings. We align principal components across time windows (Figure 3) by adjusting 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-04.png)


so that the cosine similarity between consecutive windows is positive, i.e., _𝑆𝐶_ ( _𝒗 𝑗,𝑑_ +1 _, 𝒗 𝑗,𝑑_ ) _>_ 0 for all _𝑑_ ∈{ _𝐿, . . . ,𝑇_ − 1} and _𝑗_ ∈ {1 _, . . . , 𝑀_ }. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-06.png)


**----- Start of picture text -----**<br>
Window  𝒅 Window  𝒅 +  1<br>𝒗 2 ,𝑑 𝒗 2 ,𝑑 +1<br>𝒗 1 ,𝑑<br>𝒗 1 ,𝑑 +1<br>**----- End of picture text -----**<br>


**Figure 3: Due to the sign ambiguity of PCA, the first principal component (red) flips sign between windows** _𝒅_ **and** _𝒅_ **+** 1 **, while the second component (blue) maintains its orientation.** 

## **2.4 Clustering** 

For each sliding window _𝑑_ , we perform _𝑘_ -mean++ clustering on the principal component scores _𝒕𝑖,𝑛_ of the _𝑁𝑑_ trades in the window. The algorithm partitions these trades into _𝐾_ disjoint clusters {C1 _,𝑑, . . . ,_ C _𝐾,𝑑_ } by solving 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-10.png)



![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-11.png)



![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-12.png)


We use Lloyd’s algorithm to minimise the objective in (2); specifically, a mini-batch variant which is necessary given that each 14-day window contains tens of millions of trades. We perform 100 independent runs, each initialised with _𝑘_ -means++ and allow a maximum of 100 passes through the dataset. Each run uses minibatches of size 2[15] trades for computational efficiency. From these 100 fits, we select the one with the lowest inertia and retain cluster assignment only for trades occurring on day _𝑑_ . 

_2.4.1 Cluster label alignment._ To ensure temporal consistency across clustering solutions, we align cluster labels across time periods using optimal permutation matching of centroids [15, 26]. The _𝑘_ -means++ algorithm exhibits label permutation invariance, meaning that the numeric labels {1 _, . . . , 𝐾_ } carry no inherent meaning. 

Any permutation _𝜋_ ∈ Sym( _𝐾_ ) of the labels represents the same underlying clustering structure: 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-16.png)


We align labels by solving for the permutation _𝜋_ ∈ Sym( _𝐾_ ) which minimises the sum of squared distances between consecutive window centroids: 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-18.png)


Next, we relabel all trades in window _𝑑_ +1 by setting _𝑘𝑖,𝑛_ ← _𝜋𝑑[★]_ +1[(] _[𝑘][𝑖,𝑛]_[)][.] This ensures that cluster _𝑘_ in window _𝑑_ + 1 corresponds to the same trading patterns as cluster _𝑘_ in window _𝑑_ . 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-20.png)


**----- Start of picture text -----**<br>
Centroids  𝒎𝑘,𝑑 Centroids  𝒎𝑘,𝑑 +1<br>2 3<br>1 2<br>3 1<br>4 5 5 4<br>**----- End of picture text -----**<br>


**Figure 4: To address the label permutation invariance inherent in clustering (see (3)), cluster labels are aligned through time by solving the assignment problem that minimises (4). In this example** _𝝅𝒅_ **+** 1 = **(** 3 2 1 **)(** 4 5 **) in cycle notation. Colours indicate the aligned cluster identities, while numbers show the labels assigned by the clustering algorithm.** 

## **2.5 Portfolio Construction** 

We apply our trade flow decomposition to enhance factor-based portfolio trading strategies. Our approach begins with a standard factor model comprising the Fama–French five factors, momentum, and order imbalance. We augment this base model by incorporating COIs computed within each cluster _𝑘_ ∈{1 _, . . . , 𝐾_ }. The use of COIs allows us to capture trade flow imbalances across distinct types of trading activity. We use these cluster-specific order imbalances by trading Factor-Mimicking Portfolios (FMPs) based on these COI characteristics. 

_2.5.1 Factor model framework._ We begin with the base factor model for returns 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0004-25.png)


where _𝒓𝑑_ +1 ∈ R _[𝑁][𝑑]_ denotes the close-to-close excess returns from day _𝑑_ to _𝑑_ + 1, _𝑩𝑑_ ∈ R _[𝑁][𝑑]_[×] _[𝐹]_ are the factor loadings known at the end of day _𝑑_ , _𝒇𝑑_ +1 are the factor returns, and _𝝐𝑑_ +1 are the idiosyncratic returns. The factor and idiosyncratic covariances are denoted by **𝚺** _𝒇 ,𝑑_ and **𝚺** _𝝐,𝑑_ respectively. We use the Ledoit–Wolf shrinkage estimator [16, 17] with a one-year lookback window to estimate **𝚺** _𝒇 ,𝑑_ , while **𝚺** _𝝐,𝑑_ is assumed diagonal, capturing only assetspecific variances. The factor loadings for the _𝐹_ = 7 base factors 

572 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Data-Driven Trade Flow Decomposition for ETFs and their Constituents 

are the sample mean and sample variance of the COI factor returns, to evaluate the performance of each COI factor. 

are 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-04.png)


## **3 Empirical Results** 

The loading vector _𝒃𝑑_[OI][is constructed from the order imbalance] 

We apply our methodology to SPY and its constituent equities in the period January 1, 2018 to December 31, 2021. We use intraday trade data from NASDAQ, provided by LOBSTER, to construct our features and perform the clustering. Daily equity returns are from the Center for Research in Security Prices (CRSP) database [3], and factor returns are from Kenneth French’s data library provided by WRDS [27]. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-08.png)


where _𝑉_[+] _𝑖,𝑑_[and] _[ 𝑉] 𝑖,𝑑_[−][are the volumes of buyer-initiated and seller-] initiated trades respectively for security _𝑖_ on day _𝑑_ . Chordia and Subrahmanyam established that order imbalances have predictive power for individual stock returns [4]. The COIs are defined analogously but using the volumes _𝑉𝑖,𝑘,𝑑_[+][and] _[ 𝑉] 𝑖,𝑘,𝑑_[−][within each cluster] _𝑘_ ∈{1 _, . . . , 𝐾_ }. We augment the base factor model with clusterspecific order imbalance factors, employing Paleologo’s orthogonalisation procedure [22] to ensure that these additional factors are uncorrelated with the base factors. The augmented loadings of the augmented factor model are 

Table 2 presents the annualised Sharpe ratios of the COI factormimicking portfolios for different numbers of clusters _𝐾_ ∈{2 _,_ 3 _,_ 4 _,_ 5 _,_ 6}. Each COI factor captures the order flow imbalances within a specific behavioural cluster identified by our decomposition. To test the statistical significance of the Sharpe ratio, we use the test statistic SR/√︁(1 + SR[2] /2)/ _𝑇_ [18]. We use the Bonferroni correction across all tests to control the family-wise error rate, with[∗∗] and[∗] denoting significance at the 1% and 5% levels, respectively. The cumulative returns of the factor-mimicking portfolios are shown in Figure 5. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-11.png)


where _𝑩𝑑_[COI] = � _𝒃_ 1[COI] _,𝑑[, . . . ,][ 𝒃] 𝐾,𝑑_[COI] � is the loadings matrix of orthogonalised order imbalance characteristics 

**Table 2: Annualised Sharpe ratios of conditional order imbalance factor-mimicking portfolios.** 

|_𝒃_COI<br>_𝑘,𝑑_=<br>�<br>_𝑰_−_𝑩𝑑_<br>�<br>_𝑩_⊤<br>_𝑑_**𝚺**−1<br>_𝜖,𝑑𝑩𝑑_<br>�−1<br>_𝑩_⊤<br>_𝑑_**𝚺**−1<br>_𝜖,𝑑_<br>�<br>�**�������������������������������������**��**�������������������������������������**�<br>Weighted Least Squares Orthogonalisation<br>COI_𝑘,𝑑._<br>hogonalisation ensures that the COI factors are uncorrelated<br>e base factors:<br>�**𝚺**_𝒇,𝑑_≈<br>�**𝚺**_𝒇,𝑑_<br>0_𝐹_×_𝐾_<br>0_𝐾_×_𝐹_<br>�<br>(_𝑩_COI<br>_𝑑_<br>)⊤**𝚺**−1<br>_𝝐,𝑑𝑩_COI<br>_𝑑_<br>�−1<br>�<br>_._<br>  <br>||**g p.**|
|---|---|---|
||_𝐾_|Cluster<br>C1<br>C2<br>C3<br>C4<br>C5<br>C6|
||2<br>3<br>4<br>5<br>6|1.91**<br>-0.69<br>–<br>–<br>–<br>–<br>1.37<br>-0.86<br>1.12<br>–<br>–<br>–<br>1.21<br>0.50<br>0.90<br>-0.16<br>–<br>–<br>0.32<br>0.78<br>1.52*<br>-0.68<br>1.27<br>–<br>0.69<br>0.84<br>1.24<br>-0.60<br>1.17<br>0.14|



This orthogonalisation ensures that the COI factors are uncorrelated with the base factors: 

_2.5.2 Factor-mimicking portfolios._ We construct FMPs that track the returns of our COI factors. For each factor, we minimise portfolio idiosyncratic risk subject to unit exposure to that factor and zero exposure to all other factors: 

Our results demonstrate that decomposing trade flow generates FMPs with statistically significant Sharpe ratios. The best performing FMP achieves a Sharpe ratio of 1.91 with _𝐾_ = 2. This _𝐾_ corresponds to the clustering identified as optimal by both the Calinski—Harabasz score [2] and Davies–Bouldin index [7] (see Appendix A.3). To better understand the temporal dynamics underlying these performance differences, we examine the persistence structure of order imbalances across time. Figure 6 shows the autocorrelation functions for both conditional and unconditional order imbalances. The three measures exhibit similar decay patterns, though the autocorrelations of the COIs are lower than those of order imbalances at lags of _ℓ_ ∈{1 _,_ 2 _,_ 3} days. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-18.png)


where _𝒆𝑘_ ∈ R _[𝐾]_ is the _𝑘_ -th standard basis vector. The solution yields the FMP for the _𝑘_ -th COI factor 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-20.png)


The return of the _𝑘_ -th COI factor on day _𝑑_ + 1 is then given by 

Figure 7 examines the temporal structure across clusters using lag-1 cross-correlations. The unconditional order imbalance exhibits the strongest autocorrelation ( _𝜌_ = 0 _._ 276), while crosscorrelations reveal that unconditional order imbalance correlates more strongly with cluster 2 ( _𝜌_ = 0 _._ 260) than with cluster 1 ( _𝜌_ = 0 _._ 162). The weakest correlations occur between the clusters themselves, suggesting that they capture more transient trading activity. 

_𝑓𝑘,𝑑_[COI] +1[=] _[ 𝒗] 𝑘,𝑑_[⊤] _[𝒓][𝑑]_[+][1] _[.]_ 

We use the Sharpe ratio (SR) 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-25.png)


where 

To better understand the relationships among our 16 features, we examine their correlation structure. Figure 8 displays the feature correlation matrix, which reveals strong correlations between trade 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0005-28.png)


573 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Petit et al. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0006-02.png)


**----- Start of picture text -----**<br>
C1 C2 C3<br>C4 C5 C6<br>𝐾 = 2<br>75<br>50<br>25<br>0<br>−25<br>ae<br>2018 2019 2020 2021 2022<br>𝐾 = 3<br>75<br>50<br>25<br>0<br>−25 a<br>2018 2019 2020 2021 2022<br>𝐾 = 4<br>75<br>50<br>25<br>0<br>−25<br>2018 2019 2020 2021 2022<br>𝐾 = 5<br>75<br>50<br>25<br>0<br>−25 Sto<br>2018 2019 2020 2021 2022<br>𝐾 = 6<br>75<br>50<br>25<br>0<br>−25<br>2018 2019 2020 2021 2022<br>Date<br>Cumulative Return [%]<br>Cumulative Return [%]<br>Cumulative Return [%]<br>Cumulative Return [%]<br>Cumulative Return [%]<br>**----- End of picture text -----**<br>


**Figure 5: Cumulative returns of conditional order imbalance factor-mimicking portfolios for** _𝑲_ **∈{** 2 _,_ 3 _,_ 4 _,_ 5 _,_ 6 **} clusters between January 1, 2018 and December 31, 2021.** 

**Autocorrelation Function of Order Imbalances** 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0006-05.png)


**----- Start of picture text -----**<br>
1 OI<br>COI in C1<br>COI in C2<br>0 . 5<br>0<br>0 1 2 3 4 5 6 7 8 9 10<br>Lag  ℓ [d]<br>)<br>( ℓ<br> 𝐶<br>Autocorrelation<br>**----- End of picture text -----**<br>


**Figure 6: Median autocorrelation of order imbalances and conditional order imbalances for the optimal number of clusters** _𝑲_ _**[★]**_ = 2 **. All three imbalance measures exhibit similar decay patterns, with conditional order imbalances in C** 1 **exhibiting comparatively lower autocorrelations for lags of** _ℓ_ **∈{** 1 _,_ 2 _,_ 3 **} days.** 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0006-07.png)


**----- Start of picture text -----**<br>
1<br>COI2 ,𝑑 +1 0 . 260 0 . 101 0 . 267<br>0 . 5<br>COI1 ,𝑑 +1 0 . 162 0 . 186 0 . 116 0<br>OI 𝑑 +1 0 . 276 0 . 147 0 . 264 −0 . 5<br>−1<br>OI 𝑑 COI1 ,𝑑 COI2 ,𝑑<br>Correlation<br>**----- End of picture text -----**<br>


**Figure 7: Lag-1 cross-correlation matrix between order imbalance and conditional order imbalance on day** _𝒅_ **and** _𝒅_ **+** 1 **, averaged across all symbols.** 

count and notional pairs, as well as a broader block structure separating same-sign from opposite-sign features. This high degree of correlation motivates our use of PCA for dimensionality reduction. As shown in the calibration section (see Appendix A.2), the first five principal components capture over 90% of the variance in our 16-dimensional feature space. 

## **4 Discussion** 

The main insight from our analysis is that cluster-specific order imbalances capture economically valuable information not otherwise captured by unconditional order imbalance. The traditional order imbalance treats all trades equally, averaging over heterogeneous trading behaviours. By isolating distinct types of market activity, our COIs provide additional information not captured in unconditional order imbalance. This suggests that the informational value of order flow is fundamentally context-dependent. We find that this additional information can be used in daily portfolio trading as evidenced by the statistically significant Sharpe ratios of factor-mimicking portfolios. 

574 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Data-Driven Trade Flow Decomposition for ETFs and their Constituents 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0007-02.png)


**----- Start of picture text -----**<br>
Feature Correlation Matrix<br>**----- End of picture text -----**<br>



![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0007-03.png)


**----- Start of picture text -----**<br>
1 1<br>2<br>3<br>45 0 . 5<br>6<br>7<br>89 0<br>10<br>11<br>1213 −0 . 5<br>14<br>15<br>16 os −1<br>1 2 3 4 5 6 7 8 9 10111213141516<br>Feature Index<br>Correlation<br>Feature Index<br>**----- End of picture text -----**<br>


**Figure 8: The feature correlation matrix shows strong correlations between trade count and notional traded pairs, and a broader block structure separating same-sign from oppositesign features.** 

More broadly, our findings validate the effectiveness of using joint informational content across ETFs and their constituents to identify distinct types of trading behaviours. This demonstrates that daily portfolio strategies can be enhanced by incorporating microstructural information that is otherwise lost when averaging over heterogeneous trading activity. 

## **4.1 Limitations and Future Work** 

While our results demonstrate the economic value of data-driven trade flow decomposition, several promising avenues remain for future research. Firstly, our analysis focuses on SPY and its constituents over a four-year period. Future work could extend our approach to broader equity universes such as the Russell 2000, enabling analysis across different market capitalisations and liquidity profiles. Additionally, incorporating data from related instruments (such as S&P 500 ETFs other than SPY, and E-mini futures) would provide a more comprehensive view of co-occurrence patterns. Additionally, sector-specific ETF analysis could reveal whether decomposition patterns vary across industry groups. 

While we select the best clustering from 100 _𝑘_ -means++ initialisations based on minimum inertia, this approach may converge to local optima that represent quantitatively different clustering solutions despite similar inertia values. To address this limitation, consensus-based clustering approaches [21, 25] could enhance the robustness of our decomposition. Our choice of _𝑘_ -means++ was motivated by its computational efficiency through mini-batch processing and the straightforward temporal alignment of cluster centroids. Since _𝑘_ -means++ assumes spherical clusters, algorithms like DBSCAN [8] or hierarchical clustering [11] may better accommodate irregular cluster geometries in our feature space. For dimensionality reduction, non-linear techniques such as kernel PCA [23], diffusion maps [5], and variational autoencoders [14] could reveal non-linear relationships that PCA may miss. 

The inclusion of adaptive parameters may further optimise feature characterisation. Our fixed _𝜏_ provides interpretability, but may 

not optimally capture market dynamics. Future research could explore using an adaptive _𝜏_ that depends on both time-of-day and market volatility. During high-volatility periods, a dynamic _𝜏_ that adjusts to the increased trading frequency could improve cluster quality. Similarly, while we calibrate the number of clusters _𝐾_ at the beginning of our analysis period, different market regimes may warrant different numbers of clusters. Volatile periods may exhibit more diverse trading patterns requiring larger _𝐾_ . The number of principal components _𝑀_ could also vary with market conditions, adjusting to changes in feature covariances over time. 

Future research could also explore using an enriched set of features including bid-ask spreads, order book skew, intraday volatility, and arrival rates of different event types. Additionally, testing our conditional order imbalance factors against a more comprehensive set of baseline factors [9, 12] and using the Gibbons, Ross, and Shanken (GRS) test [10] would further establish their incremental value. 

## **5 Conclusion** 

This paper introduced a novel data-driven framework for decomposing trade order flow based on the joint informational content between ETFs and their constituents. Unlike previous rule-based approaches, our approach uses unsupervised learning to perform the clustering, using a set of features based on the joint informational content in the ETF and constituents. Our empirical analysis on SPY and its constituents demonstrates that cluster-specific order imbalances capture economically valuable information not otherwise captured by unconditional order imbalance. We find that factor-mimicking portfolios based on these conditional order imbalances achieve statistically significant Sharpe ratios of up to 1.91. These results demonstrate how the predictive content of trade order flow depends on the local market conditions in which the trade occurred. More broadly, these results demonstrate how the performance of portfolio trading strategies can be enhanced by market microstructure information. 

## **Acknowledgments** 

N.P. is supported by the Oxford-Man Institute of Quantitative Finance, and the EPSRC Centre for Doctoral Training in Modern Statistics and Statistical Machine Learning (EP/S023151/1). N.P. gratefully acknowledges the support of the Oxford-Man Institute for access to computational resources. 

## **References** 

- [1] BlackRock. 2024. Types of ETFs. https://www.blackrock.com/sg/en/ishares/ education/types-of-etfs Accessed: January 2025. 

- [2] T. Caliński and J Harabasz. 1974. A dendrite method for cluster analysis. _Communications in Statistics_ 3, 1 (1974), 1–27. doi:10.1080/03610927408827101 arXiv:https://www.tandfonline.com/doi/pdf/10.1080/03610927408827101 

- [3] Center for Research in Security Prices. 2024. CRSP US Stock Database. Booth School of Business, University of Chicago. 

- [4] Tarun Chordia and Avanidhar Subrahmanyam. 2004. Order imbalance and individual stock returns: Theory and evidence. _Journal of Financial Economics_ 72, 3 (2004), 485–518. doi:10.1016/S0304-405X(03)00175-2 

- [5] Ronald R. Coifman and Stéphane Lafon. 2006. Diffusion maps. _Applied and Computational Harmonic Analysis_ 21, 1 (2006), 5–30. doi:10.1016/j.acha.2006.04. 006 Special Issue: Diffusion Maps and Wavelets. 

- [6] Rama Cont, Mihai Cucuringu, and Chao Zhang. 2023. Cross-impact of order flow imbalance in equity markets. _Quantitative Finance_ 23, 10 (2023), 1373–1393. doi:10. 1080/14697688.2023.2236159 arXiv:https://doi.org/10.1080/14697688.2023.2236159 

575 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Petit et al. 

- [7] David L. Davies and Donald W. Bouldin. 1979. A Cluster Separation Measure. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ PAMI-1, 2 (1979), 224–227. doi:10.1109/TPAMI.1979.4766909 

- [8] Martin Ester, Hans-Peter Kriegel, Jörg Sander, and Xiaowei Xu. 1996. A densitybased algorithm for discovering clusters in large spatial databases with noise. In _Proceedings of the Second International Conference on Knowledge Discovery and Data Mining_ (Portland, Oregon) _(KDD’96)_ . AAAI Press, 226–231. 

- [9] Guanhao Feng, , Stefano Giglio, and Dacheng Xiu. 2020. Taming the Factor Zoo: A Test of New Factors. _The Journal of Finance_ 75, 3 (2020), 1327–1370. doi:10. 1111/jofi.12883 arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/jofi.12883 

- [10] Michael R. Gibbons, Stephen A. Ross, and Jay Shanken. 1989. A Test of the Efficiency of a Given Portfolio. _Econometrica_ 57, 5 (1989), 1121–1152. http: //www.jstor.org/stable/1913625 

- [11] David F. Gleich. 2006. Hierarchical Directed Spectral Graph Partitioning. Information Networks, Stanford University, Final Project, 2005. http://www.cs.purdue. edu/homes/dgleich/publications/Gleich2005-hierarchicaldirectedspectral.pdf 

- [12] Kewei Hou, Chen Xue, and Lu Zhang. 2014. Digesting Anomalies: An Investment Approach. _The Review of Financial Studies_ 28, 3 (09 2014), 650–705. doi:10.1093/rfs/hhu068 arXiv:https://academic.oup.com/rfs/articlepdf/28/3/650/24450149/hhu068.pdf 

- [13] Prem C. Jain and Gun-Ho Joh. 1988. The Dependence between Hourly Prices and Trading Volume. _The Journal of Financial and Quantitative Analysis_ 23, 3 (1988), 269–283. http://www.jstor.org/stable/2331067 

- [14] Diederik P. Kingma and Max Welling. 2019. An Introduction to Variational Autoencoders. _Found. Trends Mach. Learn._ 12, 4 (Nov. 2019), 307–392. doi:10. 1561/2200000056 

- [15] Tilman Lange, Volker Roth, Mikio L. Braun, and Joachim M. Buhmann. 2004. Stability-Based Validation of Clustering Solutions. _Neural Computation_ 16, 6 (06 2004), 1299–1323. doi:10. 1162/089976604773717621 arXiv:https://direct.mit.edu/neco/articlepdf/16/6/1299/815906/089976604773717621.pdf 

- [16] Olivier Ledoit and Michael Wolf. 2004. Honey, I Shrunk the Sample Covariance Matrix. _Journal of Portfolio Management_ 30, 4 (2004), 110– 119. https://www.proquest.com/scholarly-journals/honey-i-shrunk-samplecovariance-matrix/docview/195596724/se-2?accountid=13042 Place: London Publisher: Pageant Media. 

- [17] Olivier Ledoit and Michael Wolf. 2004. A well-conditioned estimator for largedimensional covariance matrices. _Journal of Multivariate Analysis_ 88, 2 (2004), 365–411. doi:10.1016/S0047-259X(03)00096-4 

- [18] Andrew W. Lo. 2002. The Statistics of Sharpe Ratios. _Financial Analysts Journal_ 58, 4 (2002), 36–52. doi:10.2469/faj.v58.n4.2453 arXiv:https://doi.org/10.2469/faj.v58.n4.2453 

- [19] Yutong Lu, Gesine Reinert, and Mihai Cucuringu. 2023. Co-trading networks for modeling dynamic interdependency structures and estimating high-dimensional covariances in US equity markets. _arXiv:2302.09382_ (2023). arXiv:2302.09382 

- [20] Thomas H. McInish and Robert A. Wood. 1992. An Analysis of Intraday Patterns in Bid/Ask Spreads for NYSE Stocks. _The Journal of Finance_ 47, 2 (1992), 753–764. http://www.jstor.org/stable/2329122 

- [21] Stefano Monti, Pablo Tamayo, Jill Mesirov, and Todd Golub. 2003. Consensus Clustering: A Resampling-Based Method for Class Discovery and Visualization of Gene Expression Microarray Data. _Mach. Learn._ 52, 1–2 (July 2003), 91–118. doi:10.1023/A:1023949509487 

- [22] G.A. Paleologo. 2025. _The Elements of Quantitative Investing_ . Wiley. https: //books.google.co.uk/books?id=P2FMEQAAQBAJ 

- [23] Bernhard Schölkopf, Alexander Smola, and Klaus-Robert Müller. 1998. Nonlinear Component Analysis as a Kernel Eigenvalue Problem. _Neural Computation_ 10, 5 (1998), 1299–1319. doi:10.1162/089976698300017467 

- [24] Bogdan Sitaru, Anisoara Calinescu, and Mihai Cucuringu. 2023. Order Flow Decomposition for Price Impact Analysis in Equity Limit Order Books. In _Proceedings of the Fourth ACM International Conference on AI in Finance_ (Brooklyn, NY, USA) _(ICAIF ’23)_ . Association for Computing Machinery, New York, NY, USA, 637–645. doi:10.1145/3604237.3626874 

- [25] Alexander Strehl and Joydeep Ghosh. 2003. Cluster ensembles — a knowledge reuse framework for combining multiple partitions. _J. Mach. Learn. Res._ 3 (March 2003), 583–617. doi:10.1162/153244303321897735 

- [26] Ulrike von Luxburg. 2010. Clustering Stability: An Overview. _Found. Trends Mach. Learn._ 2, 3 (March 2010), 235–274. doi:10.1561/2200000008 

- [27] Wharton Research Data Services. 2024. WRDS Research Data Services. https: //wrds.wharton.upenn.edu/ Wharton School of the University of Pennsylvania. 

- [28] Robert A. Wood, Thomas H. McInish, and J. Keith Ord. 1985. An Investigation of Transactions Data for NYSE Stocks. _The Journal of Finance_ 40, 3 (1985), 723–739. http://www.jstor.org/stable/2327796 

- [29] Gesine Reinert Yutong Lu and Mihai Cucuringu. 2024. Trade co-occurrence, trade flow decomposition and conditional order imbalance in equity markets. _Quantitative Finance_ 24, 6 (2024), 779–809. 

## **A Parameter Calibration** 

We calibrate all parameters, including the neighbourhood size _𝜏_ , number of principal components _𝑀_ , and number of clusters _𝐾_ , using data from SPY and its constituents between January 1, 2017 and December 31, 2017. 

## **A.1 Neighbourhood Size** 

The features _𝒙𝑖,𝑛_ are computed in a 2 _𝜏_ time interval around each trade. The choice of _𝜏_ requires careful calibration. If set too small, almost all trades appear isolated, with many _𝒙𝑖,𝑛_ = 0. If set too large, we lose granularity by averaging over too many common trades. We calibrate _𝜏_ by examining co-occurrence events between ETF and constituent trades. We classify each central trade into one of four mutually exclusive events (Figure 9) based on neighbouring trade activity within its 2 _𝜏_ window. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0008-29.png)


**----- Start of picture text -----**<br>
Isolated Trade ETF Only<br>( ) ( )<br>𝑡 − 𝜏 𝑡 𝑡 +  𝜏 𝑡 − 𝜏 𝑡 𝑡 +  𝜏<br>Constituents Only Both ETF & Constituents<br>( ) ( )<br>𝑡 − 𝜏 𝑡 𝑡 +  𝜏 𝑡 − 𝜏 𝑡 𝑡 +  𝜏<br>Central Trade ETF Trade Constituent Trade<br>**----- End of picture text -----**<br>


**Figure 9: The four mutually exclusive co-occurrence events (** _𝑨_ **iso,** _𝑨_ **ETF,** _𝑨_ **const, and** _𝑨_ **both) for a given central trade at time** _𝒕_ **. Each panel shows the** 2 _𝝉_ **window (** _𝒕_ **−** _𝝉, 𝒕_ **+** _𝝉_ **) around the central trade (gray), with neighbouring ETF trades (blue) and constituent trades (orange) determining the event classification.** 

We calibrate _𝜏_ by maximising the deviation between empirical event probabilities and those predicted by a simple reference model. To account for the U-shaped pattern of intraday activity (Figure 2), we subdivide the trading day into 78 equal-sized buckets of length Δbucket = 5 min. Within each intraday bucket, our reference model assumes that trade arrivals for the ETF and its constituents follow independent Poisson Processes (PPs). To compute the probabilities of the four co-occurrence events _𝐴𝑘_ , we first define the following two events: 

- _𝐵_ ETF: the central trade has at least one ETF trade within the time interval ( _𝑡_ − _𝜏,𝑡_ + _𝜏_ ), 

- _𝐵_ const: the central trade has at least one constituent trade within the time interval ( _𝑡_ − _𝜏,𝑡_ + _𝜏_ ). 

Conditioning on the central trade kind I ∈{E _,_ M}, and trade counts _𝑁_ E _,𝑑,𝑗_ and _𝑁_ M _,𝑑,𝑗_ in bucket B _𝑑,𝑗_ , we have that 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0008-35.png)


576 

ICAIF ’25, November 15–18, 2025, Singapore, Singapore 

Data-Driven Trade Flow Decomposition for ETFs and their Constituents 

where _𝑝_ = 2 _𝜏_ /Δbucket. Expressing the four co-occurrence events from Figure 9 in terms of _𝐵_ ETF and _𝐵_ const, we have 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-03.png)


Under the PP reference model, the probabilities conditional on a central trade of kind I ∈{E _,_ M} are 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-05.png)


By the law of total probability, the unconditional probabilities are 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-07.png)


where _𝑁𝑑,𝑗_ = _𝑁_ E _,𝑑,𝑗_ + _𝑁_ M _,𝑑,𝑗_ is the total number of trades in bucket B _𝑑,𝑗_ . We use these probabilities to calibrate _𝜏_ by maximising the objective function 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-09.png)


where _𝑃_[emp][is the observed proportion of event] _[ 𝐴][𝑘]_[in bucket] _𝑑,𝑗_[(] _[𝐴][𝑘]_[)] B _𝑑,𝑗_ , and _𝑘_ ∈{iso _,_ ETF _,_ const _,_ both}. This objective function computes the absolute difference between empirical and reference model probabilities, weighted by the empirical event frequencies and the intraday trading intensity. The intuition for this choice is that more weight should be placed on the more frequent cooccurrence event types, and on busier periods of the day. The choice of _ℓ_[1] distance for comparing probability vectors is natural since it is proportional to the total variation distance between the probability distributions. Figure 10 shows the calibration objective D( _𝜏_ ) as a function of _𝜏_ over the range _𝜏_ ∈[1 µs _,_ 10 s]. We find the optimal value to be _𝜏[★]_ = 707 µs, maximising the deviation between empirical and reference model co-occurrence probabilities. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-11.png)


**----- Start of picture text -----**<br>
·10 [−][3]<br>6<br>4<br>2<br>0<br>10 [−][6] 10 [−][5] 10 [−][4] 10 [−][3] 10 [−][2] 10 [−][1] 10 [0] 10 [1]<br>Neighbourhood Size  𝜏 [s]<br>)<br>𝜏<br>D(<br>Weighted Distance<br>**----- End of picture text -----**<br>


**Figure 10: Calibration of neighbourhood size** _𝜏_ **using data from SPY and its constituents between January 1, 2017 and December 31, 2017. The weighted distance D(** _𝝉_ **) measures the deviation between the empirical and reference model co-occurrence probabilities.** 

## **A.3 Number of Clusters** 

To determine the optimal number of clusters, we evaluated clustering quality using the Calinski–Harabasz (CH) score [2] and Davies– Bouldin (DB) index [7]. Figure 11 shows that both metrics select the optimal number of clusters as _𝐾[★]_ = 2. Clustering quality is found to deteriorate for _𝐾 >_ 6 and we therefore restrict our subsequent analysis to _𝐾_ ∈{2 _,_ 3 _,_ 4 _,_ 5 _,_ 6}. 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-15.png)


**----- Start of picture text -----**<br>
1<br>0 . 75<br>0 . 5<br>0 . 25<br>0<br>2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19<br>Number of Clusters  𝐾<br>CH score (↑) DB index (↓)<br>Normalised Metric<br>**----- End of picture text -----**<br>


**Figure 11: Cluster quality metrics as a function of the number of clusters** _𝑲_ **. For comparison, both metrics are normalised to [** 0 _,_ 1 **] by dividing by their respective maximum values.** 

## **A.2 Number of Principal Components** 

We set the number of principal components _𝑀_ such that the explained variance ratio exceeds the threshold of 90%: 


![](/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration/markdown_output/DataDrivenFlowETF_images/DataDrivenFlowETF.pdf-0009-19.png)


where _𝑠_ 1 ≥ _𝑠_ 2 ≥ _. . ._ ≥ _𝑠𝐷_ are the singular values of _𝑿_[�] sorted in descending order. Calibrated on the data matrix of non-isolated trades only, we find that _𝑀[★]_ = 5. 

577 

