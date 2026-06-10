Proceedings of Machine Learning Research 266:1–20, 2025 Conformal and Probabilistic Prediction with Applications 

## **Conformal multi-hop relation detection and classification in knowledge graphs** 

## **Frederick Law** 

law16@llnl.gov 

_Lawrence Livermore National Laboratory Livermore, CA 94550, USA_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

Knowledge graphs (KGs) have seen an increasing use in application domains where information may be deemed proprietary, protected, or sensitive, such as enterprise, medical, or security applications. For such systems, incorporating uncertainty quantification (UQ) is critically necessary when KG information is passed to others for any downstream usage. Moreover, such systems often have constraints on data availability due to safety or legal restrictions, and as such full access to well-labeled training data may be unavailable. Conformal prediction is a distribution-free UQ strategy which is well-equipped to handle both of these concerns, as it produces prediction sets with statistically valid guarantees and is highly compatible with black-box models, which may be shared more easily than training data. In this work, we develop a novel conformal framework for simultaneously detecting and classifying multi-hop relations between entities in a KG, which only assumes access to a pre-trained KG model over triples and does not require multi-hop training data. Our framework utilizes a greedy approach, wherein we use successive conformal predictors to build a sparsely-supported scoring function in the high-dimensional multi-hop relation space. In numerical experiments on publicly available benchmark KGs with variable size and multi-hop length, our conformal multi-hop relation sets offer substantial reduction relative to the multi-hop relation space. 

**Keywords:** Conformal prediction, uncertainty quantification, knowledge graph, multi-hop 

## **1. Introduction** 

Knowledge graphs (KGs) represent large-scale, heterogeneous graph structured data, comprised of semantic information of entities and the relationships between them. Such facts are represented by triples ( _h, r, t_ ) where _h_ and _t_ are the respective head and tail entities, and _r_ is the relation type between them. While originally developed for linguistic and datascience focused applications such as question-answering, in recent years KGs have found application in a wide variety of fields including biomedical engineering, cybersecurity, and education (Zou, 2020). A defining characteristic of KGs is that they are typically incomplete, as not all information can be readily verified or included due to scale and complexity. Consequently, a primary goal with KGs has been KG completion (Shen et al., 2022), where the goal is to infer new triples ( _h, r, t_ ) based on existing data. This is commonly done by embedding the KGs using a graph neural network (GNN) to capture the relevant features of the KG for inference, see (Wang et al., 2017) for an overview on KG embedding techniques. 

For KG systems in which reliability and trustworthiness are paramount, the incorporation of uncertainty quantification (UQ) is necessary for any further downstream analysis. 

© 2025 F. Law. 

Law 

Moreover, due to the complex nature of KGs, in scale, heterogeneity, and incompleteness, we seek a distribution-free approach using conformal prediction, which offers valid statistical guarantees and is flexible for a variety of KG queries. One approach to incorporate UQ into KGs has been through the GNN embedding itself, an area for which the literature is rich, see (Wang et al., 2024) for a comprehensive review. However, the use of conformal prediction in GNN is still an emerging area. One work that has incorporated conformal prediction with GNNs is (Huang et al., 2023) in which provided a base GNN, they train an additional correction GNN by simulating the conformal prediction process and minimizing a conformal-aware loss. A different direction has been taken in (H. Zargarbashi et al., 2023) by introducing diffused adaptive prediction sets, which leverages the graph structure to smooth nonconformity values. 

Another approach to incorporating UQ for KGs has been to directly address the KG context. This is typically done by augmenting the existing KG with verified factual information (Bahaj and Ghogho, 2025), or modifying the choice of embedding (Chen et al., 2019). Work has been done incorporating conformal prediction for KG as in (Ni, 2024) which leverages the Learn-Then-Test framework for multi-hop reasoning on systems which combine KGs with large language models (LLMs). A recent work which leverages conformal prediction outside of the GNN embedding is (Zhu et al., 2025) which utilizes a split conformal prediction approach for link prediction in KGs, with various nonconformity measures. 

In this work, we focus on incorporating conformal prediction into the KG task of simultaneously detecting and classifying multi-hop relationships between existing KG entities. For instance, in a KG comprised of people we may be interested in inferring long-range connections between seemingly disparate entities, e.g. is person A a friend of a friend of person B. We are interested in the non-intrusive case where we do not have direct access to the training data, but only a pre-trained base model _f_ which scores KG triples ( _h, r, t_ ), as well as limited calibration and testing data. This approach is heavily focused on portability, for use in cases where training data is potentially proprietary, sensitive, or otherwise inaccessible. Our contribution in this work is two-fold: 

1. Introduce a multi-label regularized adaptive prediction sets (MLRAPS) method which slightly modifies the existing regularized adaptive prediction sets (RAPS). 

2. Develop a greedily-constructed scoring function, only requiring a base model _f_ ( _h, r, t_ ) and calibration data, for use with MLRAPS to produce conformal multi-hop relation sets to both detect and classify multi-hop relations. 

In Section 2 we first outline our simultaneous detection and classification framework with conformal prediction using RAPS on the simpler single-hop case. We then extend this to the multi-hop case in Section 3 which requires both multi-label conformal classification as well as the introduction of our greedily-constructed scoring function. In Section 4 we demonstrate our method on benchmark KGs, with experimental results showing smaller conformal sets and greater efficiency than a more naive choice of scoring function. 

## **2. Single-hop relation detection and classification** 

We will first detail the single-hop relation detection and classification case before extending to the multi-hop case. We consider a KG to be a set of triples (or triplets) ( _h, r, t_ ) _∈E×R×E_ 

2 

where _E_ = _{e_[(1)] _, . . . , e_[(] _[N][e]_[)] _}_ is a set of _Ne_ entities and _R_ = _{r_[(1)] _, . . . , r_[(] _[N][r]_[)] _}_ is a set of _Nr_ relation types. We assume that we have access to pre-trained, base scoring model _f_ : _E × R × E →_ R, most commonly a KG embedding trained on a dataset _D_ train. However, we do not assume that we have direct access to _D_ train. 

For a given head, tail pair ( _h, t_ ), we are interested in detecting whether there exists a latent relationship between _h_ and _t_ , as well as classifying the relation type if one exists. In order to simultaneously detect and classify relation types, we expand the relation space by introducing a unique “no relationship” or “NoRel” class _r_ NoRel. Triples of the form ( _h, r_ NoRel _, t_ ) _∈E × R[′] × E_ , where _R[′]_ := _R ∪{r_ NoRel _}_ , indicate that ( _h, r, t_ ) is false for all _r ∈R_ . We will refer to triples ( _h, r, t_ ) for _r ∈R_ which contain real relations as true triples. 

Our objective is to produce a conformal prediction set of relation types _C_ 1 _−α_ ( _h, t_ ) _⊂R[′]_ where _α_ is the significance level. For the single hop case, we will use RAPS, as introduced in (Angelopoulos et al., 2021), as our conformal prediction method, which computes a nonconformity value as a regularized cumulative likelihood over scores, see Algorithm 1. This will require a scoring function _**G**_ **0** ( _h, t_ ) : _E × E →_ [0 _,_ 1] _[N][r]_[+1] which provides a score for each _r ∈R_ as well as _r_ NoRel. 

**Algorithm 1:** Regularized adaptive prediction sets (RAPS) 

**Input:** Significance level _α ∈_ [0 _,_ 1], scoring function _**g**_ **˜** : _X →_ [0 _,_ 1] _[K]_ , calibration data _D_ calib = _{_ ( _xi, yi_ ) _}[N] i_ =1 _[⊂X][× {]_[1] _[, . . . , K][}]_[,][test][point][(] _[x, y]_[)] _[ ∈X][× {]_[1] _[, . . . , K][}]_ exchangeable with _D_ calib, regularization hyperparameters _β >_ 0 and _λ >_ 0 **Output:** Conformal set _C_ 1 _−α_ ( _x_ ) _⊂{_ 1 _, . . . , K}_ with P[ _y ∈ C_ 1 _−α_ ( _x_ )] _≥_ 1 _− α_ **for** _i ∈{_ 1 _, . . . , N }_ **do** _**S**[i] ← πi_ ( _**g**_ **˜** ( _xi_ )) ; _▷πi_ `permutes` _g_ ( _xi_ ) `descending` _Ri ←_[�] _[z] j_ =1 _[i]_ _**[S]**[i] j_[+] _[ λ][ ·]_[ max(0] _[, z][i][−][β]_[)][;] _▷zi_ = _πi_ ( _yi_ ) `, same` _πi_ `as above` **end** ˆ _q ←⌈_ (1 _− α_ )(1 + _N_ ) _⌉_ -th smallest _Ri_ ; _**S** ← πx_ ( _**g**_ **˜** ( _x_ )) ; _▷πx_ `permutes` _g_ ( _x_ ) `descending` _C_ 1 _−α_ ( _x_ ) _←{y |_[�] _[π] j_ =1 _[x]_[(] _[y]_[)] _**[S]**[j]_[+] _[ λ][ ·]_[ max(0] _[, π][x]_[(] _[y]_[)] _[ −][β]_[)] _[ ≤][q]_[ˆ] _[}]_ 

We assume that we have access to dataset _D_ calib-real _⊂E × R × E_ which contains a set of true calibration triples, as well as _D_ NoRel _⊂E × {r_ NoRel _} × E_ which contains a set of known “NoRel” triples. Furthermore, we assume we have calibration and testing sets _D_ calib-NR _, D_ test-NR _⊂E × R[′] × E_ which contain a mixture of true and “NoRel” triples, and whose elements are exchangeable. If such datasets are unavailable, they can be constructed with sufficient 1-hop data, see Remark 1. 

To first score relations for true triples, we define _**g**_ **0** : _E × E →_ R _[N][r]_ by 


![](markdown_output/law25a_images/law25a.pdf-0003-07.png)


We then evaluate _**g**_ **0** on elements from _D_ calib-real and _D_ NoRel. Using the labeled trainingtarget pairs _{_ ( _**g**_ **0** ( _h, t_ ) _,_ 1) _|_ ( _h, r_ NoRel _, t_ ) _∈D_ NoRel _} ∪{_ ( _**g**_ **0** ( _h, t_ ) _,_ 0) _|_ ( _h, r, t_ ) _∈D_ calib-real _}_ , we 

3 

Law 

fit a probabilistic binary classifier _f_ class : R _[N][r] →_ [0 _,_ 1], where small values of _f_ class( _**g**_ **0** ( _h, t_ )) imply a latent relationship exists between _h_ and _t_ , and large values imply a lack of relation. 

Ideally, if there is no latent relation between _h_ and _t_ , then the base model _f_ ( _h, r, t_ ) should be small over all _r_ and _**g**_ **0** ( _h, t_ ) will be flat. Conversely, if a latent relationship _r_ exists, then _f_ ( _h, r, t_ ) should have a strong signal for this _r_ and _**g**_ **0** ( _h, t_ ) will be peaked. 

To assign a score to the “NoRel” class, we scale the outputs of _f_ class based on the feature vector _**g**_ **0** ( _h, t_ ) itself to define a final scoring function _**G**_ **0** : _E × E →_ [0 _,_ 1] _[N][r]_[+1] as 


![](markdown_output/law25a_images/law25a.pdf-0004-04.png)


where _**σ**_ denotes the softmax function. If there is no latent relationship between _h_ and _t_ , then we expect _f_ class( _**g**_ **0** ( _h, t_ )) to be large and thus the last coordinate in Equation (2), corresponding to _r_ NoRel, will be the largest value. If there is latent relationship, we expect _f_ class( _**g**_ **0** ( _h, t_ )) to be small and thus the “NoRel” score will not be the dominant coordinate in Equation (2). We then leverage RAPS with level _α_ , hyperparameters _β_ and _λ_ , scoring function _**G**_ **0** ( _h, t_ ), and calibration data _D_ calib-NR (with _x_ = ( _h, t_ ) and _y ∈R[′]_ ) to produce our conformal relation set _C_ 1 _−α_ ( _h, t_ ) _⊂R[′]_ which can be evaluated on _D_ test-NR. 

A major motivation for using conformal prediction to produce relation sets is the context of downstream analysis. The inclusion of _r_ NoRel in the relation space allows for flexible interpretability using _C_ 1 _−α_ ( _h, t_ ). For instance, if _r_ NoRel _∈/ C_ 1 _−α_ ( _h, t_ ), then an analyst can be confident that a relationship is likely to exist between _h_ and _t_ , and that _C_ 1 _−α_ ( _h, t_ ) contains that true relationship with probability at least 1 _− α_ . Conversely, if _r_ NoRel _∈ C_ 1 _−α_ ( _h, t_ ), then an analyst can carefully scrutinize other elements in _C_ 1 _−α_ ( _h, t_ ), and if none of the other _r ∈ C_ 1 _−α_ ( _h, t_ ) seem satisfactory, then the analyst can be confident no relationship exists between _h_ and _t_ . 

Additionally, depending on the specific domain of information captured in the KG, there are likely “nonsense” relations that do not make sense between certain entities. For instance consider a KG comprised of historical figures and locations. For entities “Winston Churchill” and “United Kingdom”, relations such as “BornIn” or “LivedIn” may make sense. In contrast, relations typically between humans such as “MarriedTo” or “SiblingOf” do not make sense, but may reasonably be in the relation space. As a result, conformal relation sets not only offer valid statistical guarantees, but can also be further pared down by leveraging domain expertise to remove “nonsense” answers in the conformal set. 

**Remark 1** _In practice, “NoRel” data may not always be provided, as many KGs are focused on known relationships between entities, not on known, lack of relationships between on entities. However, “NoRel” data can easily be generated provided Dtrain, Dcalib, and Dtest, as is common for many publicly available KGs, by parsing through all triples and sampling_ ( _h, rNoRel, t_ ) _for h, t ∈E and_ ( _h, r, t_ ) _∈D/ train ∪Dcalib ∪Dtest for any r ∈R. Datasets Dcalib-real, DNoRel, Dcalib-NR, and Dtest-NR can then be formed by sampling “NoRel” triples, partitioning Dcalib, and blending “NoRel” triples into Dtest and a partition of Dcalib, using the other partition as Dcalib-real. Generating “NoRel” triples this way requires parsing Dtrain, as “NoRel” triples represents known, definitive lack of relation. However, if a set of “NoRel” triples can be provided a priori then access to Dtest is not required._ 

4 

Figure 1: Overview of conformal multi-hop relation detection and classification. 

## **3. Multi-hop relation detection and classification** 

We now detail the extension of our conformal single-hop relation detection and classification to the multi-hop case. For the remainder of the article, let _k ∈_ N, _k ≥_ 2 denote multi-hop length. For a head _h_ = _e_ 0, a tail _t_ = _ek_ , and relations _r_ 1 _, . . . , rk ∈R_ , we say a _k_ -hop relation _**r**_ = ( _r_ 1 _, . . . , rk_ ) exists between _h_ and _t_ , denoted as ( _h,_ _**r** , t_ ), if there exists entities _k e_ 1 _, . . . , ek−_ 1 _∈E_ such that ( _es−_ 1 _, rs, es_ ) is true for _s_ = 1 _, . . . , k_ . Let _Rk_ = _s_ =1 _[R]_[denote] the space of all _k_ -hop relations. Let _rk_ -hop _,_ NoRel denote a _k_ -hop “NoRel” class such that ( _h, rk_ -hop _,_ NoRel _, t_ ) indicates that no _k_ -hop relation _**r**_ exists between _h_ and _t_ . As in the single-hop case, let _R[′] k_[:=] _[ R][k][ ∪{][r][k]_[-hop] _[,]_[NoRel] _[}]_[.] 

Similarly to the single-hop case, given an ( _h, t_ ) pair, our goal is to simultaneously detect and classify if a _k_ -hop relation exists between _h_ and _t_ using conformal prediction sets _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ) _⊂R[′] k_[.] Following the steps in the single-hop case, if we have a scoring function over all _k_ -hop relation classes _**g**_ : _E × E →_ [0 _,_ 1] _[N] r[k]_ , analogous to Equation (1) in the single-hop case, we can train a probabilistic, binary classifier _fk_ -hop,class on appropriately partitioned data and use a final scoring function _**G**_ : _E × E →_ [0 _,_ 1] _[N] r[k]_[+1] 


![](markdown_output/law25a_images/law25a.pdf-0005-04.png)


where _||_ _**G**_ ( _h, t_ ) _||_ 1 = 1. 

## **3.1. Comparison to single-hop case** 

Unlike the single-hop case, where we anticipate a single primary relation _r_ between head _h_ and _t_ , in the multi-hop case it is possible for there to exist multiple _k_ -hop relations between _h_ and _t_ . Moreover, if the KG is well-connected, then for larger _k_ we anticipate the number of _k_ -hop relations to grow, as there will be more paths of length _k_ connecting _h_ and _t_ . As a result, classifying _k_ -hop relation types is a multi-label classification problem, which will require multi-label conformal prediction. 

5 

Law 

There are numerous works in the area of multi-label conformal classification, including label power set (LP) (Papadopoulos, 2014) which works directly in the power set of all labels, instance reproduction (IR) (Wang et al., 2014) which creates a single-label instance for each multi-label data point, and binary relevance (BR) (Wang et al., 2015) which combines a binary classification task on each individual class. More recent work in the field includes _p_ - norm (Maltoudoglou et al., 2022) and (Katsios and Papadopulos, 2024) which addresses the dimensionality challenges of LP by assigning a nonconformity value based on the _p_ -norm and Mahalanobis distance of multi-hot encoded error vector. Other works incorporate conformalized quantile techniques (Cauchois et al., 2021) which additionally develop inner and outer conformal sets, tree-based approaches (Tyagi and Guo, 2023) which leverage a hierarchical structure with multiple-testing, and (Angelopoulos et al., 2024) which handles multi-label classification as a conformal risk control task. 

## **Algorithm 2:** Multi-label RAPS (MLRAPS) 

**Input:** Significance level _α ∈_ [0 _,_ 1], scoring function _**g**_ **˜** : _X →_ [0 _,_ 1] _[K]_ , calibration data _D_ calib = _{_ ( _xi, Yi_ ) _}[N] i_ =1 _[⊂X][×]_[ 2] _[{]_[1] _[,...,K][}]_[,][test][point][(] _[x, Y]_[ )] _[ ∈X][×]_[ 2] _[{]_[1] _[,...,K][}]_ exchangeable with _D_ calib, regularization hyperparameters _β >_ 0 and _λ >_ 0 **Output:** Conformal set _C_ 1 _−α_ ( _x_ ) _⊂{_ 1 _, . . . , K}_ with P[ _Y ⊆ C_ 1 _−α_ ( _x_ )] _≥_ 1 _− α_ **for** _i ∈{_ 1 _, . . . , N }_ **do** 


![](markdown_output/law25a_images/law25a.pdf-0006-04.png)


In this work, we consider a simple multi-label modification to RAPS (MLRAPS). For the task of classifying inputs _x ∈X_ into the classes _{_ 1 _, . . . , K}_ using a scoring function � _**g**_ : _X →_ [0 _,_ 1] _[K]_ , the RAPS nonconformity value for a calibration data point ( _x, y_ ) _∈X × {_ 1 _, . . . , K}_ is the sum over the coordinates of _**g**_ �( _x_ ) such that _**g**_ � _i_ ( _x_ )� _≥_ _**g**_ � _y_ ( _x_ ), i.e. over all classes _i_ which are at least as likely as the true label _y_ according to _**g**_ . For MLRAPS (Algorithm 2), the label _y_ is replaced with the multi-label _Y ⊂{_ 1 _, . . . , K}_ , and so we now sum over classes _i_ such that _**g**_ � _i_ ( _x_ ) _≥_ min _y∈Y_ _**g**_ � _y_ ( _x_ ), i.e. over all classes _i_ which are at least as likely as the least likely label in _Y_ . Under the same exchangeability assumptions as RAPS, but now on data with multi-labels, this modified MLRAPS achieves the same statistical guarantees. 

**˜ Proposition 2** _Let_ _**g**_ : _X →_ [0 _,_ 1] _[K] be a scoring function, let Dcalib_ = _{_ ( _xi, Yi_ ) _}[N] i_ =1 _[⊂] X ×_ 2 _[{]_[1] _[,...,K][}] be a set of calibration data, and let_ ( _x, Y_ ) _∈X ×_ 2 _[{]_[1] _[,...,K][}] be exchangeable with elements of Dcalib. Then for α ∈_ [0 _,_ 1] _, the conformal set C_ 1 _−α_ ( _x_ ) _⊂{_ 1 _, . . . , K} produced by MLRAPS in Algorithm 2 satisfies_ 


![](markdown_output/law25a_images/law25a.pdf-0006-07.png)


6 

**Proof** The event _Y ⊆ C_ 1 _−α_ ( _x_ ) is equivalent to _y ∈ C_ 1 _−α_ ( _x_ ) for all _y ∈ Y_ , and _y ∈ C_ 1 _−α_ ( _x_ ) ˆ if and only if _R_ ( _x, y_ ) _≤ q_ for _R_ ( _x, y_ ) =[�] _[π] j_ =1 _[x]_[(] _[y]_[)] _**[S]**[j]_[+] _[ λ][ ·]_[ max(] _[π][x]_[(] _[y]_[)] _[ −][β]_[).][Let][us][define] _R_ ( _x, Y_ ) = _R_ ( _x, y[∗]_ ) where _y[∗] ∈ Y_ and _πx_ ( _y[∗]_ ) _≥ πx_ ( _y_ ) for _y ∈ Y_ . Since _R_ is monotonic in _y_ under _πx_ , i.e. _R_ ( _x, y_ ) _> R_ ( _x, y[′]_ ) when _πx_ ( _y_ ) _> πx_ ( _y[′]_ ), then _R_ ( _x, y_ ) _≤ q_ ˆ for all _y ∈ Y_ if and ˆ ˆ only if _R_ ( _x, Y_ ) _≤ q_ . Recall _q_ is the _⌈_ (1 _−α_ )(1+ _N_ ) _⌉_ -th smallest _R_ ( _xi, Yi_ ) for ( _xi, Yi_ ) _∈ D_ calib. Since ( _x, Y_ ) is assumed exchangeable with _D_ calib, we have our result 


![](markdown_output/law25a_images/law25a.pdf-0007-01.png)


We assume we have access to the multi-label _k_ -hop dataset _D_ calib-real _[k]_[-hop] _[⊂E][×]_[ 2] _[R][k][× E]_ which contains true multi-label calibration _k_ -hops, as well as _D_ NoRel _[k]_[-hop] _[⊂E × {][r][k]_[-hop] _[,]_[NoRel] _[} ×] E_ which contains known “NoRel” _k_ -hops. Additionally, we assume we have access to _D_ calib-NR _[k]_[-hop] _[,][ D]_ test-NR _[k]_[-hop] _[⊂E×]_ �2 _[R][k] ∪{rk_ -hop _,_ NoRel _}_ � _×E_ which contain true multi-label _k_ -hops and “NoRel” _k_ -hops, and whose elements are exchangeable. Note that a “triple” in _E ×_ 2 _[R][k] × E_ would be ( _h, Rk, t_ ), where _Rk ⊂Rk_ is a subset of _k_ -hop relations. If these datasets are unavailable, they can be constructed with sufficient 1-hop data, see Remark 4. We use the datasets _D_ calib-real _[k]_[-hop][and] _[ D]_ NoRel _[k]_[-hop][along with a scoring function] _**[ g]**_[(] _[h, t]_[) to generate] the training-target pairs for “NoRel” data _{_ ( _**g**_ ( _h, t_ ) _,_ 1) _|_ ( _h, rk_ -hop _,_ NoRel _, t_ ) _∈D_ NoRel _[k]_[-hop] _[}]_[as][well] as _{_ ( _**g**_ ( _h, t_ ) _,_ 0) _|_ ( _h, Rk, t_ ) _∈D_ calib-real _[k]_[-hop] _[}]_[for][true][data][to][fit][our][binary][classifier] _[f][k]_[-hop] _[,]_[class][.] We then use _fk_ -hop _,_ class alongside _**g**_ ( _h, t_ ) to define our final scoring function _**G**_ ( _h, t_ ) as in Equation (3). Lastly, we use MLRAPS with level _α_ , hyperparameters _β_ and _λ_ , scoring function _**G**_ ( _h, t_ ), and calibration data _D_ calib-NR _[k]_[-hop][(with] _[x]_[=][(] _[h, t]_[)][and] _[Y][⊂R][′] k_[)][to][form][our] conformal sets _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ) _⊂R[′] k_[which][can][be][evaluated][on] _[D]_ test-NR _[k]_[-hop][.][We][note][that] regardless of the choice of _**G**_ ( _h, t_ ), our _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ) is valid by the validity of MLRAPS. 

## **3.2. Naive approach** 

In order to construct _**G**_ ( _h, t_ ) we need an appropriate scoring function _**g**_ : _E × E →_ [0 _,_ 1] _[N] r[k]_ which provides a score for every _**r** ∈Rk_ . This step of the process is the most challenging, as in order to score every _k_ -hop relation, we may need to analyze every possible path from _h_ to _t_ of length _k_ , through all possible entities, and over all possible relations. Indeed, a naive choice would be the following: 


![](markdown_output/law25a_images/law25a.pdf-0007-05.png)


where _h_ = _e_ 0 and _t_ = _ek_ and _f_[˜] ( _e, r, e[′]_ ) = **A** ( _e_ ) _r,e′_ with **A** ( _e_ ) is defined as 


![](markdown_output/law25a_images/law25a.pdf-0007-07.png)


The matrix **A** ( _e_ ) in Equation (5) corresponds to normalizing all of the base scores _f_ ( _e, r, e[′]_ ) for all hops ( _r, e[′]_ ) away from _e_ . This construction gives a relative score to the path of ( _r, e[′]_ ) 

7 

Law 

away from _e_ compared to all other paths, as well as normalizing the scores to [0 _,_ 1] to avoid cancellation in the sum. We note that for the “last” hop, _f_ ( _e, r, t_ ) where we have a known tail _t_ , we set _f_[˜] ( _e, r, t_ ) = _**σ**_ ( _**g**_ **0** ( _e, t_ )) _r_ , i.e. the _r_ -th component of the softmax of Equation (1). 

This choice of naive scoring assigns to a _k_ -hop relation _**r**_ the maximum aggregate (normalized) base model score over all possible paths of length _k_ with these relation types. Doing so requires a search over _Ne[k][−]_[1] many intermediate entity paths for a single _k_ -hop relation _**r**_ , a computational hurdle worsened as this must be done for _Nr[k]_[many] _[ k]_[-hop relations.][For] 

large-scale KG, this approach may be computationally intractable even for moderate _k_ . 

Moreover, this naive approach is particularly wasteful in the context of KGs, as some relation classes may only make sense for certain entities. For instance, suppose that for a given head _h_ , only a single relation _r[∗]_ makes sense for a single hop away, that is ( _h, r, e_ ) is not true for _r_ = _r[∗]_ and all _e ∈E_ . Then assigning scores to _k_ -hops _**r**_ = ( _r_ 1 _, . . . , rk_ ) where _r_ 1 = _r[∗]_ is unnecessary. This is analogous to there being more “nonsense” answers in the _k_ -hop relation space as _k_ grows. 

## **3.3. Greedy approach** 

To design a more efficient scoring function, we propose a greedily-constructed _**g**_ ( _h, t_ ) which iteratively expands a multi-hop neighborhood originating from _h_ , which seeks to both reduce the number of intermediate entity paths considered for a given _**r**_ as well as reduce the number of _k_ -hop relations _**r**_ that are assigned meaningful scores. 

Suppose that we have access to two set-valued functions, _C_ 1-hop : _E →_ 2 _[R×E]_ as well as _C_ end : _E →_ 2 _[R]_ . The set _C_ 1-hop( _e_ ) is a 1-hop neighborhood of relation, tail pairs ( _r, e[′]_ ) away from _e_ , whereas the set _C_ end( _e, e[′]_ ) is a set of relations _r_ between _e_ and _e[′]_ . 

For a given pair ( _h, t_ ), we compute _**g**_ ( _h, t_ ) as follows. First, we compute the 1-hop set _C_ 1( _h_ ) = _C_ 1-hop( _h_ ), and let _**ξ**_ **1** = ( _r_ 1 _, e_ 1) _∈ C_ 1-hop( _h_ ). Then for _s_ = 2 _, . . . , k −_ 1, we iteratively expand to an _s_ -hop neighborhood by 


![](markdown_output/law25a_images/law25a.pdf-0008-09.png)


where _**ξs**_ = ( _rs, es_ ) _∈ C_ 1-hop( _es−_ 1). Thus, at iteration _s_ , we have an _s_ -hop neighborhood away from _h_ , as well as the paths through relations and intermediate entities to get there. After _k −_ 1 iterations, we then use _C_ end to connect to the target tail _t_ , 


![](markdown_output/law25a_images/law25a.pdf-0008-11.png)


where _**ξk**_ = ( _rk, t_ ). We then define our scoring function _**g**_ ( _h, t_ ) : _E × E →_ [0 _,_ 1] _[N] r[k]_ as 


![](markdown_output/law25a_images/law25a.pdf-0008-13.png)


where _e_ 0 = _h_ and _ek_ = _t_ and _||_ _**g**_ ( _h, t_ ) _||_ 1 = 1 Here _ε >_ 0 is a small number chosen for numerical stability. We will refer to the set of _**r**_ whose _**g**_ ( _h, t_ ) values are not assigned proportional to _ε_ as the _effective support_ of _**g**_ ( _h, t_ ), denoted as suppeff( _**g**_ ), and likewise for _**G**_ ( _h, t_ ). 

8 

This greedily-constructed _**g**_ ( _h, t_ ) places probability mass on _k_ -hop relations _**r**_ which are traversed from a path ( _h, r_ 1 _, e_ 1) _,_ ( _e_ 1 _, r_ 2 _, e_ 2) _, . . . ,_ ( _ek−_ 1 _, rk, t_ ) using the set-valued functions _C_ 1-hop and _C_ end. Comparatively, the naive approach using Equation (4) may seek to place probability mass on all _k_ -hop relations. Moreover, for a _k_ -hop relation _**r**_ , our greedy _**g**_ ( _h, t_ ) only computes the maximum aggregate (normalized) base model score over the paths traced out with _C_ 1-hop, not over all _Ne[k][−]_[1] paths as in the naive approach. Note we recover the naive scoring function if our set-valued functions _C_ 1-hop and _C_ end are as large as possible. That is, if _C_ 1-hop( _e_ ) = _R × E_ for all _e ∈E_ and _C_ end( _e, e[′]_ ) = _R_ for all _e, e[′] ∈E_ , then _**g**_ ( _h, t_ ) as in Equation (6) is exactly _**g**_ naive( _h, t_ ). 

It remains to determine our choice of set-valued functions _C_ 1-hop and _C_ end. If they are too large, then our greedy method will lose efficiency, as we will have to scan over too many _k_ -hop relations and paths per _k_ -hop relation. However, care must be taken to ensure that _C_ 1-hop is not too small, as _**g**_ ( _h, t_ ) is used to form _**G**_ ( _h, t_ ) which will is used in the _k_ -hop MLRAPS to produce _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ). 

If _C_ 1-hop is too small, our greedy approach may undercover the ( _r, e[′]_ ) neighborhood away from _e_ , and the effective support suppeff( _**G**_ ) may be too small. Consequently, during MLRAPS calibration, if a _k_ -hop relation in the label set is outside suppeff( _**G**_ ), then the nonconformity value for that data point will be large, requiring summing through all of suppeff( _**G**_ ), and summing noise outside suppeff( _**G**_ ). If this happens too frequently, then the MLRAPS calibration will be poor and _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ) may be large. Thus, we want to choose _C_ 1-hop and _C_ end in a manner where we can cover the correct set of ( _r, e[′]_ ) and _r_ with confidence. 

## **3.4. Conformal set-valued functions** 

We consider constructing _C_ 1-hop and _C_ end using conformal prediction sets. The choice for _C_ end is natural, as it is almost exactly the single-hop case. We assume we also have access to a dataset of 1-hop calibration triples _D_ calib _⊂E × R × E_ . Let _**g**_ **2** ( _e, e[′]_ ) = _**σ**_ ( _**g**_ **0** ( _e, e[′]_ )) where _**g**_ **0** is the single-hop scoring function in Equation (1). We use RAPS with level _α_ int, hyperparameters _β_ int and _λ_ int, scoring function _**g**_ **2** ( _e, e[′]_ ) and calibration data _D_ calib (with _x_ = ( _e, e[′]_ ) and _Y ⊂R_ ), to produce our conformal set-valued function _C_ end _,_ 1 _−α_ int : _E × E →_ 2 _[R]_ . We shall refer to _α_ int _, β_ int _, λ_ int as interior parameters, used to construct _C_ 1-hop and _C_ end, to distinguish them from the _α, β, λ_ parameters used to construct _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ). For _C_ 1-hop we consider two options: a direct approach which scans all possible hops ( _r, e[′]_ ) from _e_ simultaneously, and a sequential approach which first grabs the best relations _r_ from _e_ and then subsequently the best 1-hop tails _e[′]_ . 

## 3.4.1. Direct approach 

For the direct approach, we shall consider all possible hops ( _r, e[′]_ ) away from _e_ together. We treat this as a multi-label classification problem where the input is the current entity _e_ , and the output is a subset of _R × E_ . Let _**g**_ **1** _**,**_ direct : _E →_ [0 _,_ 1] _[N][r][N][e]_ be defined as 


![](markdown_output/law25a_images/law25a.pdf-0009-07.png)


where **A** ( _e_ ) is defined in Equation (5). 

9 

Law 

We assume we have access to a multi-label calibration dataset _D_ direct _⊂E ×_ 2 _[R×E]_ . Elements of _D_ direct correspond to a head entity _e_ paired with a set of ( _r, e[′]_ ) such that ( _e, r, e[′]_ ) is true. Note that if such a dataset is unavailable, it can be constructed by parsing through _D_ calib. We then use MLRAPS with interior level _α_ int, hyperparameters _β_ int and _λ_ int, scoring function _**g**_ **1** _**,**_ direct( _e_ ), and calibration data _D_ direct (with _x_ = _e_ and _Y ⊂R × E_ ) to produce conformal relation sets as our set-valued function _C_ 1-hop[direct] _,_ 1 _−α_ int[:] _[ E][→]_[2] _[R×E]_[.] Since the direct approach uses MLRAPS with _R × E_ treated as the full space classification space, we expect _C_ 1-hop[direct] _,_ 1 _−α_ int[to][be][potentially][large][as][there][are] _[N][r][N][e]_[total][possible] elements to consider. This is both a benefit and a weakness. On the plus side, we can be confident the direct approach will not undercover the ( _r, e[′]_ ) neighborhood away from _e_ , and thus avoid problems with suppeff( _**G**_ ) being too small. However, if _C_ 1-hop[direct] _,_ 1 _−α_ int[is][too][large] then it may not be computationally tractable for larger _k_ as at each iteration we build a 1-hop set off every element in the previous 1-hop set. 

## 3.4.2. Sequential approach 

In the sequential approach, we instead first find a set of relations _r_ to “hop away” from _e_ with, and once those are found we then find a set of tails _e[′]_ for each ( _e, r_ ). As in the direct approach, this will be done by treating this as two multi-label classification problems. In the first, the input will be an entity _e_ with the output as a subset of _R_ . In the second, the input will be an entity relation pair ( _e, r_ ) and the output will be a subset of _E_ . We define _**g**_ **1** _**,r**_ -seq : _E →_ [0 _,_ 1] _[N][r]_ and _**g**_ **1** _**,t**_ -seq : _E × R →_ [0 _,_ 1] _[N][e]_ by: 


![](markdown_output/law25a_images/law25a.pdf-0010-04.png)


where _||_ _**g**_ **1** _**,r**_ -seq( _e_ ) _||_ 1 = 1 and _||_ _**g**_ **1** _**,t**_ -seq( _r, e_ ) _||_ 1 = 1. Here _**g**_ **1** _**,r**_ -seq( _e_ ) is the normalized columnwise maximum of **A** ( _e_ ), and _**g**_ **1** _**,t**_ -seq( _e, r_ ) is the normalized _r_ -th row of **A** ( _e_ ). The intuition behind this is as follows. To find only the best relations _r_ which ( _e, r, e[′]_ ) may be true, we can scan all ( _r, e[′]_ ) pairs, and for each _r_ , just take the maximum score over all the possible _e[′]_ . Large scores will correspond to relations _r_ for which there is at least one entity _e[′]_ where ( _e, r, e[′]_ ) is true, and small scores will correspond to relations _r_ where ( _e, r, e[′]_ ) is not true for all entities _e[′]_ . And to find the tails _e[′]_ for a given ( _e, r_ ), we can just take all the scores from the _r_ -th column of **A** ( _e_ ). 

We assume that we have two multi-label calibration sets _Dr_ -seq _⊂E ×_ 2 _[R]_ and _Dt_ -seq _⊂ E × R ×_ 2 _[E]_ . As in the direct case, if such datasets are not available they can be constructed by parsing _D_ calib. Elements of _Dr_ -seq correspond to a head entity _e_ paired with a set of relations _r_ such that there exists an _e[′]_ where ( _e, r, e[′]_ ) is true. Elements of _Dt_ -seq correspond to head relation pairs ( _e, r_ ) paired with a set of tails _e[′]_ such that ( _e, r, e[′]_ ) is true. 

We first use MLRAPS with interior level _α_ int, hyperparameters _β_ int and _λ_ int, scoring function _**g**_ **1** _**,r**_ -seq( _e_ ), and calibration data _Dr_ -seq (with _x_ = _e_ and _Y ⊂R_ ) to produce conformal prediction sets _C_ 1 _[r] −_[-seq] _α_ int[:] _[E][→]_[2] _[R]_[.][We][then][use][MLRAPS][with][interior][level] _[α]_[int][,] hyperparameters _β_ int and _λ_ int, scoring function _**g**_ **1** _**,t**_ -seq( _e, r_ ), and calibration data _Dt_ -seq (with _x_ = ( _e, r_ ) and _Y ⊂E_ ) to produce conformal prediction sets _C_ 1 _[t]_[-seq] _−α_ int[:] _[E][× R][→]_[2] _[E]_[.] Finally, we define our sequential 1-hop set-valued function as _C_ 1-hop[seq] _,_ 1 _−α_ int[:] _[ E][→]_[2] _[R×E]_[by] 


![](markdown_output/law25a_images/law25a.pdf-0010-08.png)


10 

Unlike the direct approach which considers all ( _r, e[′]_ ) from _e_ at once, we expect the sequential approach to offer smaller conformal 1-hop sets, as it breaks up its search first over _R_ and then over _E_ . While this implies more efficient sets and potentially better scalability to large _k_ , the sequential approach may undercover more frequently, and thus be less stable than the direct approach. 

Since our sequential 1-hop set-valued function requires performing two conformal classifications, one layered into the next, with the same interior level _α_ int, there is no guarantee that _C_ 1-hop[seq] _,_ 1 _−α_ int[(] _[e]_[)][achieves][at][least][1] _[ −][α]_[int][coverage.][This][is][in][contrast][to][the][direct] approach which performs only one conformal classification, and thus _C_ 1-hop[direct] _,_ 1 _−α_ int[has][the] guarantee of 1 _− α_ int coverage. However, since the conformal choice of _C_ 1-hop (direct or sequential) must run iteratively and then eventually feed into _C_ end, neither approach will lead to guaranteed 1 _− α_ coverage on the final _k_ -hop neighborhood set _Ck_ ( _h, t_ ). 

We note that exact coverage is not necessarily the primary goal in the construction of a conformal _C_ 1-hop and _C_ end, nor in _Ck_ ( _h, t_ ). Rather, the goal is to have an oft-reliable set-valued function which can then be used to expand a neighborhood around the target head entity _h_ until we reach the target tail entity _t_ . Since _Ck_ ( _h, t_ ) is only used to construct _**g**_ ( _h, t_ ), and subsequently _**G**_ ( _h, t_ ), which is then used in a final MLRAPS calibration on _k_ -hop relations, we will maintain valid statistical coverage on the _k_ -hop relation sets. And so long as _|_ suppeff( _**G**_ ) _|_ does not get too small, we can expect our approach to be stable. 

**Remark 3** _For the sequential approach, different choices of αint can be made for C_ 1 _[r] −[-seq] αint and C_ 1 _[t][-seq] −αint[,][however][for][ease][of][presentation][we][have][kept][these][the][same.][Additionally,] since αint is the primary source of the size of C_ 1 _-hop, for both the direct and sequential approaches, in practice it may be beneficial to use additional calibration data to tune αint._ 

**Remark 4** _In practice, many KGs may not naturally come with k-hop calibration or test data, much less multi-label versions. Likewise, many datasets may not have “NoRel” k-hop data either. However, provided 1-hop calibration and testing datasets Dcalib and Dtest, multilabel k-hop data can be generated by parsing through these datasets. In fact, one could mix Dcalib and Dtest together, parse Dcalib ∪Dtest to create a larger set of multi-label k-hop data, and then repartition out to calibration and testing sets. Additionally, “NoRel” k-hop data can be generated as in the single-hop case, see Remark 1, but now parsing for multi-hops._ 

## **4. Numerical experiments** 

We demonstrate our conformal multi-hop relation detection and classification on the benchmark CoDEx KG datasets (Safavi and Koutra, 2020), which comprise information extracted from WikiData. We test on both CoDEx Small (CoDEx-S) and CoDEx Medium (CoDExM) which are provided as 1-hop datasets _D_ train, _D_ calib, _D_ test, whose sizes are shown in Table 1. We consider CoDEx-S with _k_ = 2 _,_ 3 and CoDEx-M with _k_ = 2. We guarantee exchangeability in all our benchmark experiments by always blending calibration and test data and randomly repartitioning, as then calibration and test data are drawn uniformly from the combined original data. For real-application deployment, additional caution should be used to ensure exchangeability. 

In each case, we use the _D_ train dataset to train a base model _f_ ( _h, r, t_ ) using DistMult (Yang et al., 2015) with 100 epochs, implemented through PyKEEN (Ali et al., 2021). 

11 

Law 

Table 1: Sizes of benchmark CoDEx datasets. 

||_Ne_ = _|E|_|_Nr_ = _|R|_|_D_train|_D_calib|_D_test|
|---|---|---|---|---|---|
|CoDEx-S<br>CoDEx-M|2034<br>17,050|42<br>51|32,888<br>185,584|1827<br>10,310|1828<br>10,311|



We choose DistMult for its simplicity and efficiency, as preliminary testing with more sophisticated KG embedding architectures such as RGCN did not demonstrate a significant improvement in accuracy for _f_ . In handling relatively small KG and _k_ , we perform all our tests on an 8-core Macbook Pro. Since the CoDEx datasets do not come with _k_ -hop data, we use the 1-hop datasets _D_ calib _, D_ test to generate _D_ calib _[k]_[-hop][and] _[D]_ test _[k]_[-hop] through mixing and parsing as discussed in Remark 4. We additionally leverage the _D_ train to generate _k_ -hop “NoRel” triples as also discussed in Remark 4. We blend and partition _D_ calib _[k]_[-hop][,] _[D]_ test _[k]_[-hop][,][and] _D_ test _[k]_[-hop] to produce our datasets _D_ calib-real _[k]_[-hop][,] _[D]_ NoRel _[k]_[-hop][,] _[D]_ calib-NR _[k]_[-hop][,][and] _[D]_ test-NR _[k]_[-hop][.][Although][the] CoDEx datasets do contain hard negatives (e.g. 1-hop “NoRels”), these cannot easily be used to generate _k_ -hop “NoRels”, as this would require at least 1-hop along every _k_ -hop path from _h_ to _t_ to have be a hard negative. Lastly, we generate the datasets _D_ direct for the direct approach and _Dr_ -seq, _Dt_ -seq for the sequential approach by parsing through _D_ calib. Sizes of these datasets for CoDEx-S with _k_ = 2 _,_ 3 and CoDEx-M with _k_ = 2 are provided in Table 2, where we have under-sampled the number of 2-hops in CoDEx-M and 3-hops in CoDEx-S for computational considerations. For each case, we use a support vector machine with radial basis function kernel for _fk_ -hop _,_ class, and use _ε_ = 10 _[−]_[10] for Equation (6). 

Table 2: Dataset sizes for conformal _k_ -hop detection and classification. 

||_D_direct|_Dr_-seq|_Dt_-seq|_Dk_-hop<br>calib-real|_Dk_-hop<br>NoRel|_Dk_-hop<br>calib-NR|_Dk_-hop<br>test-NR|
|---|---|---|---|---|---|---|---|
|CoDEx-S (_k_=2)<br>CoDEx-S (_k_=3)<br>CoDEx-M (_k_=2)|644<br>644<br>4288|644<br>664<br>4288|775<br>775<br>4896|210<br>96<br>150|146<br>96<br>100|2523<br>144<br>1776|2804<br>72<br>1974|



We consider five primary diagnostics for each test case performed: the average 1-hop set size _|C_ 1-hop _|_ , the average effective support size _|_ suppeff( _**G**_ ) _|_ , the average conformal _k_ -hop relation set size _|Ck_ -hop _,_ 0 _._ 9( _h, t_ ) _|_ (using MLRAPS with _α_ = 0 _._ 1), the “NoRel” false positive rate (FPR), and the “NoRel” false negative rate (FNR). We also report empirical coverage at the _α_ = 0 _._ 1 level. Both the average _|C_ 1-hop _|_ and average _|_ suppeff( _**G**_ ) _|_ will inform how efficient the test case is, as smaller values mean less paths need to be searched. However, average _|C_ 1-hop _|_ and _|_ suppeff( _**G**_ ) _|_ will also inform how stable the case is, as if they are too small they will tend to undercover and lead to large _|Ck_ -hop _,_ 0 _._ 9 _|_ is. Ideally the average _|Ck_ -hop _,_ 0 _._ 9 _|_ is small relative to _R[′] k_[while also maintaining a small] _[ |][C]_[1-hop] _[|]_[.][The “NoRel” FPR] is the proportion of ( _h, t_ ) for which there does exist a nonempty set of _k_ -hop relations, but _rk_ -hop _,_ NoRel _∈ Ck_ -hop _,_ 1 _−α_ ( _h, t_ ). Conversely, the “NoRel” FNR is the proportion of ( _h, t_ ) with known _k_ -hop “NoRel”, but _rk_ -hop _,_ NoRel _∈/ Ck_ -hop _,_ 1 _−α_ ( _h, t_ ). Unless otherwise specified, all test cases are performed with hyperparameters _β_ = _β_ int = 1 and _λ_ = _λ_ int = 10 for both the 

12 

interior MLRAPS used for _C_ 1-hop _,_ 1 _−α_ int( _e, e[′]_ ) and for the _k_ -hop MLRAPS _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ), to regularize conformal sets to be as small as possible. 

Table 3: _k_ -hop statistics using _D_ train _∪D_ calib _∪D_ test. 

||Total _k_-hops|Mean _Mk_(_h, t_)|Max _Mk_(_h, t_)|ˆ_τ_0_._90(_Mk_(_h, t_))|
|---|---|---|---|---|
|CoDEx-S (_k_=2)<br>CoDEx-S (_k_=3)<br>CoDEx-M (_k_=2)|847,065<br>42,007,992<br>3,629,061|2.70<br>80.95<br>1.34|192<br>5669<br>194|6<br>152<br>3|



Since, for benchmarking purposes, we have access to the training data _D_ train in addition to _D_ calib and _D_ test, we can compute how many _k_ -hops exist between entities ( _h, t_ ). For _h, t ∈ E_ such that there exists at least one _k_ -hop relation, let _Mk_ ( _h, t_ ) : _E ×E →{_ 1 _,_ 2 _, . . . }_ denote the number of _k_ -hop relations between _h_ and _t_ , as found by parsing _D_ train _∪D_ calib _∪D_ test. In Table 3 we show the total number of _k_ -hop relations found, the mean _Mk_ ( _h, t_ ), the maximum _Mk_ ( _h, t_ ), as well as the 90th quantile _τ_ ˆ0 _._ 90( _Mk_ ( _h, t_ )). We observe that in going from _k_ = 2 to _k_ = 3 for CoDEx-S, we see a significant increase in the total number of _k_ -hops, the mean _Mk_ ( _h, t_ ), and the maximum _Mk_ ( _h, t_ ). This underscores the challenge behind _k_ -hop relation prediction, as for well-connected KGs we expect the number of paths, and thus multi-hop relations, between _h_ and _t_ to grow dramatically as _k_ increase. 

Ideally we would like our conformal set at level _α_ = 0 _._ 1 to be just slightly larger than _τ_ ˆ0 _._ 90( _Mk_ ( _h, t_ )). If 90% of the time an ( _h, t_ ) pair has less than _τ_ ˆ0 _._ 90( _Mk_ ( _h, t_ )) many _k_ -hop relations, then it stands to reason we would want a _Ck_ -hop _,_ 0 _._ 90( _h, t_ ) to be of a similar size. However, we stress that in practice, when training data is not accessible, _such information cannot be derived_ . Moreover, a defining characteristic of KGs is that they are incomplete, so even if training data is accessible, the information displayed in Table 3 must be taken with a grain of salt. We include these statistics here for completeness, but emphasize that by the incomplete nature of KGs, they _cannot_ be used as a true barometer for calibrating conformal _k_ -hop relation sets. 

## **4.1. CoDEx-S** 

For CoDEx-S, we first consider _k_ = 2 case, testing both the direct and sequential approaches, as well as using _λ_ int = 0 _,_ 10 for _C_ 1-hop[direct] _,_ 1 _−α_ int[(] _[e]_[)][and] _[C]_ 1-hop[seq] _,_ 1 _−α_ int[(] _[e]_[).][All][four][of][these][tests] will be performed with internal level _α_ int = 0 _._ 10, and for each case we additionally test using _λ_ = 0 _,_ 10 for _Ck_ -hop _,_ 1 _−α_ ( _h, t_ ). We also test the naive approach for comparison. For this test case, 2-hop relation space has size _|R[′]_ 2 _[|]_[ = 1765.] 

In Table 4 we see that the naive, greedy, and sequential approaches all yield very small _|C_ 2-hop _,_ 0 _._ 9 _|_ compared to _|R[′]_ 2 _[|]_[ = 1765.][In][particular,][we][observe][that][our][greedy][approaches] outperforms the naive approach for all tests in producing smaller conformal 2-hop relation sets _|C_ 2-hop _,_ 0 _._ 9 _|_ , with the best case (sequential, _λ_ int = 10) having _|C_ 2-hop _,_ 0 _._ 9 _|/|R[′]_ 2[=][0] _[.]_[0053,] a massive reduction in 2-hop relation space. 

Comparing greedy approaches, we see that the sequential approach not only has smaller 1-hop sets _|C_ 1-hop _|_ and smaller _|_ suppeff( _**G**_ ) _|_ than the direct approach, and is thus more efficient, but also yields smaller conformal 2-hop relation sets. Comparing _λ_ int = 0 _,_ 10, we 

13 

Law 

see that _λ_ int = 10 is better for both the sequential and direct approach. All tests for this case have roughly the same “NoRel” FPR and “NoREL” FNR. We note that _C_ 1-hop _⊂R×E_ , and thus the reported _|C_ 1-hop _|_ sizes are very small compared to _|R × E|_ = _NrNe_ = 85 _,_ 428. 

Table 4: Diagnostics for CoDEx-S conformal 2-hop relation prediction, _α_ int = 0 _._ 10. 

||Naive|Direct|Direct|Sequential|Sequential|
|---|---|---|---|---|---|
|||_λ_int = 0|_λ_int = 10|_λ_int = 0|_λ_int = 10|
|Average _|C_1-hop_|_<br>Average _|_suppeff(**_G_**)_|_<br>Average _|C_2-hop_,_0_._9_|_<br>“NoRel” FPR<br>“NoRel” FNR<br>Empirical coverage, _α_= 0_._1|N/A<br>N/A<br>43.58<br>0.06<br>0.09<br>0.899|2493.90<br>295.94<br>25.06<br>0.06<br>0.06<br>0.898|2030.96<br>155.03<br>12.31<br>0.07<br>0.05<br>0.900|1050.62<br>221.49<br>13.06<br>0.06<br>0.07<br>0.900|662.17<br>124.49<br>9.45<br>0.06<br>0.07<br>0.896|



Figure 2: Conformal 2-hop relation set sizes for CoDEx-S. 

In Figure 2 we plot the conformal 2-hop relation set size _|C_ 2-hop _,_ 1 _−α|_ for various choices of _α_ with _λ_ = 0 _,_ 10. We observe that in the _λ_ = 0 case, the sequential approach with both _λ_ int = 0 _,_ 10 noticeably outperforms the direct approach. At _λ_ = 10 however, all four test cases are much closer together, with the notable difference being between _λ_ int = 0 and _λ_ int = 10 rather than the direct versus sequential. Overall, the best results are obtained when choosing _λ_ int = 10 and _λ_ = 10, with the difference between sequential and direct being minor. This suggests that regularization, both for the interior 1-hop conformal prediction, as well as for the conformal _k_ -hop relation prediction, is preferred to no regularization. 

We next consider CoDEx-S with _k_ = 3, comparing the direct and sequential approach with _α_ int = 0 _._ 10 _,_ 0 _._ 05, to demonstrate the capability of scaling to larger choices of _k_ . We use a fixed _λ_ int = 10 and consider _λ_ = 0 _,_ 10. With _Nr_ = 42, the 3-hop relation space has size _|R[′]_ 3 _[|]_[=][74] _[,]_[ 089.][Since][the][only][change][is][in][the][multi-hop][length,][the] _[C]_[1-hop][and] _[G]_ 

14 

functions are the same as in the _k_ = 2 case. We do not test the naive approach for _k_ = 3 as it proved computationally intractable. In Table 5 we display our five diagnostics. 

Table 5: Diagnostics for CoDEx-S conformal 3-hop relation prediction. 

||Direct|Direct|Sequential|Sequential|
|---|---|---|---|---|
||_α_int = 0_._10|_α_int = 0_._05|_α_int = 0_._10|_α_int = 0_._05|
|Average _|C_1-hop_|_<br>Average _|_suppeff(**_G_**)_|_<br>Average _|C_3-hop_,_0_._9_|_<br>“NoRel” FPR<br>“NoRel” FNR<br>Empirical coverage, _α_= 0_._1|2030.93<br>6969.38<br>63,989.01<br>1.00<br>0.00<br>0.889|3101.89<br>16371.42<br>1760.04<br>0.04<br>0.04<br>0.917|663.94<br>6357.97<br>63,434.36<br>1.00<br>0.00<br>0.875|1664.25<br>17644.52<br>833.88<br>0.06<br>0.08<br>0.889|



We observe that for both the sequential and direct approaches at _α_ int = 0 _._ 1, our method is quite unstable, with enormous conformal 3-hop relation sets, along with a “NoRel” FPR of 1. Examining Figure 3, we see that for _α_ = 0 _._ 10, the nonconformity values are massive for a large proportion of calibration points. 

This can be explained by the relatively small _|C_ 1-hop _|_ at _α_ int = 0 _._ 1. Both methods with _α_ int = 0 _._ 10 produce too small _C_ 1-hop sets, undercovering the 1-hop neighborhood away in _R × E_ . As a result, suppeff( _**G**_ ) is too small, with too many labels outside suppeff( _**G**_ ) during calibration. This leads to summing through noise outside of suppeff( _**G**_ ) until all true labels are covered which leads to a sharp jump in nonconformity values and thus a large quantile in MLRAPS, which leads to large _C_ 3-hop _,_ 1 _−α_ . We see a “NoRel” FPR of 1 due to the scaling of the “NoRel” score in Equation (3), which should always place “NoRel” within suppeff( _**G**_ ), and thus all conformal sets will contain “NoRel” when unstable. 

Figure 3: Conformal 3-hop relation set sizes for CoDEx-S and nonconformity values. 

However, once we decrease the interior level to _α_ int = 0 _._ 05, we see in Table 5 that the _C_ 1-hop size grows for both the direct and sequential approach, leading to larger _|_ suppeff( _**G**_ ) _|_ 

15 

Law 

and thus more stable calibration. Consequently, we see smaller _|C_ 3-hop _,_ 0 _._ 9 _|_ , and improved “NoRel” FPR and FNR. We can additionally see this improvement in the nonconformity values in Figure 3, where nonconformity values have decreased sufficiently so the inevitable jump does not occur until _α >_ 0 _._ 1. 

Although _α_ = 0 _._ 05 shrinks the conformal 3-hop relation sets, they are still on average of moderate size at 1760 for the direct approach and 834 for the sequential approach. However, since _|R[′]_ 3 _[|]_[ = 74] _[,]_[ 089,][these][sets][provide][a][substantial][reduction][in][the][3-hop][relation][space,] with _|C_ 3-hop _,_ 0 _._ 9 _|/|R[′]_ 3 _[|]_[ = 0] _[.]_[024 for the direct approach and 0.011 for the sequential approach.] Moreover, due to the increase in potential ”nonsense” answers for longer multi-hops, there is still utility behind these moderately sized conformal 3-hop relation sets for downstream analysis. We note that for _k_ = 3 we only have 144 calibration and 72 test data points, which explains some empirical coverage deviating from the expected 0.9. 

## **4.2. CoDEx-M** 

Lastly we consider the CoDEx-M dataset with _k_ = 2, with the goal of demonstrating the capability of scaling to larger KGs. Compared to CoDEx-S, CoDEX-m has over 8 times more entities and slightly more relations. For this dataset _|R × E|_ = _NrNe_ = 869 _,_ 550, significantly larger than in CoDEx-S where the dimensionality was 85,428. As a result, we expect the task of estimating a 1-hop set with _C_ 1-hop to be more difficult. The 2-hop relation space has size _|R[′]_ 2 _[|]_[=][2602,][slightly][larger][than][CoDEx-S][with] _[k]_[=][2,][but][much] smaller than CoDEX-S with _k_ = 3. 

Table 6: Diagnostics for CoDEx-M conformal 2-hop relation prediction. 

||Naive|Direct|Direct|Sequential|Sequential|
|---|---|---|---|---|---|
|||_α_int = 0_._10|_α_int = 0_._05|_α_int = 0_._10|_α_int = 0_._05|
|Average _|C_1-hop_|_<br>Average _|_suppef(**_G_**)_|_<br>Average _|C_2-hop_,_0_._9_|_<br>“NoRel” FPR<br>“NoRel” FNR<br>Empirical coverage, _α_= 0_._1|N/A<br>N/A<br>255.52<br>0.02<br>0.07<br>0.915|86,855.31<br>534.42<br>53.14<br>0.03<br>0.04<br>0.928|97,715.20<br>730.63<br>50.03<br>0.03<br>0.05<br>0.914|6237.77<br>604.65<br>2142.38<br>1.00<br>0.00<br>0.920|12,302.73<br>954.85<br>102.14<br>0.04<br>0.04<br>0.894|



We test our greedy approaches using _λ_ int = 10 and _λ_ = 0 with _α_ int = 0 _._ 05 _,_ 0 _._ 10. Similarly to CoDEx-S with _k_ = 2, we additionally test the naive approach. In Table 6 we see that our greedy approaches outperform the naive approach in producing smaller _|C_ 2-hop _,_ 1 _−α|_ , except for the sequential approach with _α_ int = 0 _._ 10. 

When _α_ int = 0 _._ 10 with the sequential approach, we see unstable calibration, similar to the results for CoDEx-S when _α_ int = 0 _._ 10. As before, this is due to _C_ 1-hop being too small, leading to _**G**_ ( _h, t_ ) undercovering and producing too many large nonconformity values as seen in Figure 4. Unlike our previous experiments, for this KG we see that the direct approach noticeably outperforms the sequential approach in producing smaller conformal 2-hop sets, at the cost of much large _C_ 1-hop. Not only is the direct approach stable with _α_ int = 0 _._ 10, but it has smaller conformal 2-hop relation sets of size 50 whereas the sequential approach 

16 

Figure 4: Conformal 2-hop relation set sizes for CoDEx-M and nonconformity values. 

only goes down to 102 with _α_ int = 0 _._ 05. This corresponds to _|C_ 2-hop _,_ 0 _._ 9 _|/|R[′]_ 2 _[|]_[=][0] _[.]_[019][for] the direct approach and 0.039 for the sequential approach, which is a substantial reduction in the 2-hop relation space. 

Stability at _α_ int = 0 _._ 10 for a larger KG corresponds to increased size of the 1-hop space of _R × E_ for _C_ 1-hop. As this space grows, it becomes easier to undercover with _C_ 1-hop, and thus it is consistent that the direct approach which produces much large _C_ 1-hop than the sequential approach is more stable over _α_ int for a larger KG. 

In Table 7 we show the proportion of 1-hop space _R × E_ covered by _C_ 1-hop for CoDEx-S and CoDEx-M, for the direct and sequential approach, and _α_ int = 0 _._ 05 _,_ 0 _._ 10. In Table 8 we show the proportion of _k_ -hop relation space _R[′] k_[covered][by][supp] eff[(] _**[G]**_[),][for][the][direct][and] sequential approach, for _α_ int = 0 _._ 05 _,_ 0 _._ 10, and for CoDEx-S with _k_ = 2 _,_ 3 and CoDEx-M with _k_ = 2. We mark the unstable cases in Table 8 with an asterisk. Looking first at the proportion of 1-hop space covered, we see that decreasing _α_ int leads to more coverage as expected. But moving from CoDEx-S to CoDEX-M, the direct approach covers a larger percentage of the 1-hop space, whereas the sequential approach covers roughly the same percentage, despite there being many more entities in CoDEx-M. 

Table 7: Proportion of 1-hop space covered, _|C_ 1-hop _|/|R × E|_ , with _λ_ int = 10 

||Direct|Direct|Sequential|Sequential|
|---|---|---|---|---|
||_α_int = 0_._10|_α_int = 0_._05|_α_int = 0_._10|_α_int = 0_._05|
|CoDEx-S<br>CoDEx-M|0.024<br>0.10|0.036<br>0.11|0.0078<br>0.0073|0.019<br>0.014|



However, we see that for CoDEx-M, the sequential approach covers more of the 2-hop relation space _R[′] k_[.][This suggests that the sequential approach is parsing more relations than] the direct approach, but combined with the proportion of 1-hop space covered in Table 7, implies the sequential approach parses far fewer mid-path entities than the direct approach. 

17 

Law 

Table 8: Proportion of _k_ -hop relation space covered, _|_ suppeff( _**G**_ ) _|/|R[′] k[|]_[,][with] _[λ]_[int][= 10] 

||Direct|Direct|Sequential|Sequential|
|---|---|---|---|---|
||_α_int = 0_._10|_α_int = 0_._05|_α_int = 0_._10|_α_int = 0_._05|
|CoDEx-S (_k_=2)<br>CoDEx-S (_k_=3)<br>CoDEx-M (_k_=2)|0.088<br>0.094*<br>0.21|N/A<br>0.22<br>0.28|0.070<br>0.0865*<br>0.23*|N/A<br>0.24<br>0.37|



Since CoDEx-M and CoDEx-S have a similar number of relations (51 vs. 42), when adding more entities the direct approach adapts by increasing its 1-hop space coverage, while the sequential approach covers well in the relations with _C_ 1-hop _[r]_[-seq] _,_ 1 _−α_ int[(] _[e]_[)][but][poorly][covering] with _C_ 1-hop _[t]_[-seq] _,_ 1 _−α_ int[(] _[e, r]_[).][As][a][consequence,][the][sequential][approach][seems][to][“miss”][correct] _k_ -hop paths more often, and so even though suppeff( _**G**_ ) is larger than the direct approach, it is placing probability mass on the wrong _k_ -hop relations. Thus, although the sequential approach is typically “cheaper” than the direct approach as less of _R × E_ must be covered by _C_ 1-hop, it is more sensitive to instability, and may require more fine-tuning of _α_ int. 

**Remark 5** _In Section 2 and Section 3.4, we use RAPS for the single-hop case and for Cend in the multi-hop case, assuming there is at most one 1-hop relation for a given_ ( _h, t_ ) _. In practice this may not be true, depending on the KG. For our benchmarks, less than_ 1% _of_ ( _h, t_ ) _pairs in CoDEx-S dataset have more than one_ 1 _-hop relation between them. In the CoDEx-M dataset, this is less than_ 2% _. However, if a KG has many 1-hop relations between h and t, it is straightforward to substitute RAPS with MLRAPS._ 

## **5. Conclusion and future work** 

We have developed a greedily-constructed scoring function for conformal multi-hop relation detection and prediction on KGs which only requires a pre-trained scoring function on triples. Our scoring function is built by iteratively expanding a neighborhood from a target head _h_ until the target tail _t_ is reached, and only assigns relevant probability mass to parsed multi-hop relations. We introduced two approaches for expanding a neighborhood, direct and sequential, both of which use interior conformal prediction methods to build a set of 1-hop neighbors in relation and entity space. Numerical experiments on benchmark CoDEx KGs yield positive results, allowing for efficient parsing of multi-hops to produce reasonably sized conformal multi-hop relation sets for downstream analysis. 

Future work includes further fine-tuning of our approach, including the introduction of variable interior parameter _α_ int which can be adjusted based on the choice of direct or sequential, as well as the current neighborhood size. Other work includes optimizing implementation for high-performance computing on much larger KG, investigating the computational complexity with respect to KG size and hop length _k_ , as well as leveraging other conformal classification methods. While we have focused on using our modified MLRAPS algorithm, the framework established can be use with any multi-label conformal classification algorithm with nonconformity scoring _s_ ( _x, Y_ ) where _x_ = ( _h, t_ ) and _Y ⊂R[′] k_[which][can] leverage _**G**_ ( _h, t_ ) as a heuristic approximation of uncertainty. 

18 

## **Acknowledgments** 

This work was performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344. This document has been reviewed for release (LLNL-CONF-2005227). 

## **References** 

- Mehdi Ali, Max Berrendorf, Charles Tapley Hoyt, Laurent Vermue, Sahand Sharifzadeh, Volker Tresp, and Jens Lehmann. PyKEEN 1.0: A Python Library for Training and Evaluating Knowledge Graph Embeddings. _Journal of Machine Learning Research_ , 22 (82):1–6, 2021. 

- Anastasios Nikolas Angelopoulos, Stephen Bates, Michael Jordan, and Jitendra Malik. Uncertainty sets for image classifiers using conformal prediction. In _International Conference on Learning Representations_ , 2021. 

- Anastasios Nikolas Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster. Conformal risk control. In _The Twelfth International Conference on Learning Representations_ , 2024. 

- Adil Bahaj and Mounir Ghogho. A step towards quantifying, modelling and exploring uncertainty in biomedical knowledge graphs. _Computers in Biology and Medicine_ , 184: 109355, 2025. 

- Maxime Cauchois, Suyash Gupta, and John C. Duchi. Knowing what you know: valid and validated confidence sets in multiclass and multilabel prediction. _J. Mach. Learn. Res._ , 22(1), 2021. 

- Xuelu Chen, Muhao Chen, Weijia Shi, Yizhou Sun, and Carlo Zaniolo. Embedding uncertain knowledge graphs. In _Proceedings of the Thirty-Third AAAI Conference on Artificial Intelligence and Thirty-First Innovative Applications of Artificial Intelligence Conference and Ninth AAAI Symposium on Educational Advances in Artificial Intelligence_ , AAAI’19/IAAI’19/EAAI’19. AAAI Press, 2019. 

- S. H. Zargarbashi, S. Antonelli, and A. Bojchevski. Conformal prediction sets for graph neural networks. In _Proceedings of the 40th International Conference on Machine Learning_ , volume 202. PMLR, 2023. 

- K. Huang, Y. Jin, and J. Cand`es, E.and Leskovec. Uncertainty quantification over graph with conformalized graph neural networks. In _Proceedings of the 37th International Conference on Neural Information Processing Systems_ , NIPS ’23, 2023. 

- Kostas Katsios and Harris Papadopulos. Multi-label conformal prediction with a mahalanobis distance nonconformity measure. In _Proceedings of the Thirteenth Symposium on Conformal and Probabilistic Prediction with Applications_ , volume 230 of _Proceedings of Machine Learning Research_ , pages 522–535. PMLR, 2024. 

19 

Law 

- Lysimachos Maltoudoglou, Andreas Paisios, Ladislav Lenc, Jiˇr´ı Mart´ınek, Pavel Kr´al, and Harris Papadopoulos. Well-calibrated confidence measures for multi-label text classification with a large number of labels. _Pattern Recognition_ , 122:108271, 2022. 

- Bo Ni. Reliable knowledge graph reasoning with uncertainty quantification. In _Proceedings of the 33rd ACM International Conference on Information and Knowledge Management_ , CIKM ’24, page 5463–5466. Association for Computing Machinery, 2024. 

- Harris Papadopoulos. A cross-conformal predictor for multi-label classification. In _Artificial Intelligence Applications and Innovations_ , pages 241–250, Berlin, Heidelberg, 2014. Springer Berlin Heidelberg. 

- Tara Safavi and Danai Koutra. CoDEx: A Comprehensive Knowledge Graph Completion Benchmark. In _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 8328–8350. Association for Computational Linguistics, 2020. 

- Tong Shen, Fu Zhang, and Jingwei Cheng. A comprehensive overview of knowledge graph completion. _Knowledge-Based Systems_ , 255:109597, 2022. 

- Chhavi Tyagi and Wenge Guo. Multi-label classification under uncertainty: A tree-based conformal prediction approach. In _Proceedings of the Twelfth Symposium on Conformal and Probabilistic Prediction with Applications_ , volume 204 of _Proceedings of Machine Learning Research_ , pages 488–512. PMLR, 2023. 

- Fangxin Wang, Yuqing Liu, Kay Liu, Yibo Wang, Sourav Medya, and Philip S. Yu. Uncertainty in graph neural networks: A survey. _Transactions on Machine Learning Research_ , 2024. 

- Huazhen Wang, Xin Liu, Bing Lv, Fan Yang, and Yanzhu Hong. Reliable multi-label learning via conformal predictor and random forest for syndrome differentiation of chronic fatigue in traditional chinese medicine. _PLOS ONE_ , 9(6):1–14, 2014. 

- Huazhen Wang, Xin Liu, Ilia Nouretdinov, and Zhiyuan Luo. A comparison of three implementations of multi-label conformal prediction. In _Statistical Learning and Data Sciences_ , pages 241–250, Cham, 2015. Springer International Publishing. 

- Quan Wang, Zhendong Mao, Bin Wang, and Li Guo. Knowledge graph embedding: A survey of approaches and applications. _IEEE Transactions on Knowledge and Data Engineering_ , 29(12):2724–2743, 2017. 

- Bishan Yang, Wen-tau Yih, Xiaodong He, Jianfeng Gao, and Li Deng. Embedding entities and relations for learning and inference in knowledge bases. In _3rd International Conference on Learning Representations, ICLR_ , 2015. 

- Y. Zhu, N. Potyka, J. Pan, B. Xiong, Y. He, E. Kharlamov, and S. Staab. Conformalized answer set prediction for knowledge graph embedding, 2025. arXiv:1410.5093. 

- Xiaohan Zou. A survey on application of knowledge graph. _Journal of Physics: Conference Series_ , 1487(1):012016, 2020. 

20 

