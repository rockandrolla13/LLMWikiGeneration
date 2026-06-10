Proceedings of Machine Learning Research 266:1–20, 2025 Conformal and Probabilistic Prediction with Applications 

## **Incorporating Structural Penalties in Multi-label Conformal Prediction** 

**Kostas Katsios** k.katsios@albourne.com **Harris Papadopoulos** h.papadopoulos@frederick.ac.cy _Computational Intelligence Research Lab., Frederick University, Nicosia, Cyprus Machine Learning Research Group, Albourne Partners (Cyprus) Ltd, Nicosia, Cyprus_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

We propose two structural penalties for the Label-Powerset Split Conformal Prediction framework in multi-label learning. Building on our previously proposed Mahalanobis nonconformity measure, we add penalties that favour label-sets similar to previously observed ones in terms of Hamming distance and cardinality. The resulting nonconformity measure steers prediction regions toward label-sets that are both plausible and compact. Experiments on three public datasets (Emotions, PlantPseAAC, Yeast) show an average of 30% reduction in prediction region size for Emotions, 82% for PlantPseAAC and 39% for Yeast, compared to the Mahalanobis baseline. 

**Keywords:** Mahalanobis, Multi-label, Classification, Conformal, Prediction, Power-set, Hamming, Cardinality, Reduction 

## **1. Introduction** 

This work focuses on the reliable quantification of uncertainty in multi-label learning through the Conformal Prediction (CP) framework. Specifically, we propose a Split (or Inductive) Conformal Prediction (SCP) approach using the Label Power-set (LP) technique, as introduced by Papadopoulos (2014), which can be combined with any classifier that produces a score for each class. The proposed method calculates the nonconformity and p-value of each possible label-set and provides prediction regions of label-sets with guaranteed 1 _− ε_ coverage for any significance level _ε_ . 

This study extends our previous work (Katsios and Papadopoulos, 2024) by proposing an approach to reduce prediction region sizes based on a Mahalanobis nonconformity measure. Inspired by the penalty term proposed by (Papadopoulos, 2014), our method involves processing of the proper-training label-sets and penalizing the Mahalanobis nonconformity scores. The Mahalanobis distance is defined through a covariance matrix, which in our case is derived from the proper-training data, taking into account correlations between error vectors. We extend the Mahalanobis nonconformity measure by adding two penalty terms, one based on the normalized Hamming distance and the other on the cardinality of each proper-training label-set. 

As a preprocessing step, we calculate the normalized Hamming distance between each possible label-set and all proper-training label-sets, assigning to each possible label-set its 

© 2025 K. Katsios & H. Papadopoulos. 

Katsios Papadopoulos 

minimum normalized Hamming distance value. Similarly, we determine the frequency of each possible cardinality in the proper-training data and compute the difference of each frequency from unity. These values serve as penalty terms added to the original nonconformity score. The resulting nonconformity measure significantly reduces the size of prediction regions compared to the original Mahalanobis-based approach, as presented in our experimental results. 

The rest of this paper is structured as follows. Section 2 provides an overview of the Split Conformal Prediction framework, the multi-label classification setting and previous work on CP for multi-label classification. Section 3 introduces our proposed method. Section 4 presents experimental results and compares our method with a previously proposed approach based on the Mahalanobis nonconformity measure. Finally, Section 5 concludes the paper and outlines directions for future work. 

## **2. Technical background** 

## **2.1. Split Conformal Prediction** 

Split Conformal Prediction (SCP), also known as Inductive Conformal Prediction (ICP), is a computationally efficient framework for constructing prediction sets with guaranteed coverage (Papadopoulos et al., 2002a,b). Unlike the traditional full conformal prediction approach (Vovk et al., 2005), which requires retraining the model for each test instance, SCP avoids this by splitting the available data into two disjoint subsets. 

For classification tasks, given a dataset _Z_ = �( _xi, ψi_ ) : _xi ∈_ R _[s] , ψi ∈_ Ψ� for _i_ = 1 _, ..., n_ , where _s_ is the number of attributes, R _[s]_ is the space of features and Ψ = _{Y_ 1 _, . . . , Yd}_ the set of possible classes. SCP divides the available data as follows: 

- Proper-training Set: _Ztr_ = _{_ ( _x_ 1 _, ψ_ 1) _, ...,_ ( _xq, ψq_ ) _}_ , where _q ≤ n_ . 

- Calibration Set: _Zcal_ = _{_ ( _xq_ +1 _, ψq_ +1) _, ...,_ ( _xn, ψn_ ) _}_ . 

The proper-training set is used to train the predictive model, called _underlying model_ . The calibration set is utilized to calculate _nonconformity scores_ , which measure how unusual or nonconforming a data point is with respect to the model’s predictions. The nonconformity scores are produced by a _nonconformity measure_ , 


![](markdown_output/katsios25a_images/katsios25a.pdf-0002-10.png)


that quantifies the dispute between the model’s prediction for input _xi_ and the actual observed values. Once the model is trained on the proper-training set, it is used to compute nonconformity scores for the calibration set, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0002-12.png)


SCP assumes all possible classifications _Yc ∈{Y_ 1 _, . . . , Yd}_ for the test instance _xn_ +1 and calculates their nonconformity scores by applying function _A_ to the trained model and each test pair ( _**x** n_ +1 _, Yc_ ), 


![](markdown_output/katsios25a_images/katsios25a.pdf-0002-14.png)


2 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

To quantify the plausibility of each candidate label, SCP computes a conformal p-value, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0003-02.png)


which is a valid p-value of the null hypothesis that _Yc_ is the true label of _xn_ +1. The prediction region at significance level _ε ∈_ [0 _,_ 1] is then defined as 


![](markdown_output/katsios25a_images/katsios25a.pdf-0003-04.png)


This ensures that, with probability at least (1 _− ε_ ), the prediction region Γ _[ε] xn_ +1[will][cover] the true label of _xn_ +1, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0003-06.png)


In fact, SCP satisfies this coverage guarantee under the assumption of data exchangeability, regardless of the underlying data distribution or model. 

## **2.2. Multi-label learning** 

Multi-label learning is a branch of supervised learning in which each instance can be associated with multiple labels. Therefore _ψi ⊆L_ , where _L_ = _{λ_ 1 _, . . . , λd}_ denotes the set of _d_ individual labels. This setting arises naturally in a wide range of real-world applications, including text categorization (see e.g. Haralabopoulos et al. (2020)), image annotation (see e.g. R¨uckert et al. (2024)), bioinformatics (see e.g. Maxwell et al. (2017)), and music classification (see e.g. Zhong et al. (2023)), where an object may belong to multiple categories. 

Approaches to multi-label learning can be broadly divided into two primary categories: Problem Transformation (PT) methods and Algorithm Adaptation (AA) methods (see (Tsoumakas and Katakis, 2007)). Problem Transformation techniques convert the multilabel problem into one or more single-label or binary classification problems, allowing the use of standard machine learning algorithms. This enables the application of conventional supervised learning algorithms without requiring substantial algorithmic changes. In contrast, Algorithm Adaptation methods involve modifying existing learning algorithms to handle multi-label data. 

Among the two, Problem Transformation (PT) methods are particularly popular due to their simplicity, scalability, and flexibility. The most commonly used PT methods include: 

- Instance Reproduction (IR): The Instance Reproduction method tackles multi-label learning by generating multiple binary instances from each multi-label instance, one for every label in the label-set. In this transformation, each copy of the instance is paired with a single positive label while keeping the input features unchanged. The application of the Instance Reproduction transformation reformulates the multi-label dataset _Z_ into a dataset 


![](markdown_output/katsios25a_images/katsios25a.pdf-0003-13.png)


This approach is particularly well-suited for handling highly unbalanced datasets and supports label-specific modeling, allowing classifiers to focus on distinguishing each individual label’s characteristics. 

3 

Katsios Papadopoulos 

- Binary Relevance (BR): This method decomposes the multi-label problem into independent binary classification tasks as many as the number of labels, one for each label _λj ∈L_ . Each label is mapped to a binary value by setting _ℓj_ = 1 if label _λj_ is associated with instance _xi_ and _ℓj_ = 0 otherwise. Based on this encoding, a separate binary classification dataset is constructed for each label 


![](markdown_output/katsios25a_images/katsios25a.pdf-0004-02.png)


Although BR is computationally efficient and easy to implement, it assumes label independence, which limits its ability to capture correlations among labels. 

- Label Power-set (LP): LP treats each unique combination of labels as a distinct class in a multi-class classification problem. This approach inherently models label dependencies but suffers from poor generalization in the presence of rare or unseen label-sets, leading to scalability challenges when the number of possible label combinations grows exponentially. The full set of possible label combinations is given by the power-set Ψ = _P_ ( _L_ ). 

## **2.3. Multi-label Split Conformal Prediction** 

The three Problem Transformation (PT) strategies - Instance Reproduction (IR), Binary Relevance (BR), and Label Powerset (LP) - integrate differently with SCP, particularly in how they split the dataset and form prediction regions. 

A central property of Conformal Prediction (CP) is its ability to control the prediction error at a user-defined significance level _ε ∈_ [0 _,_ 1]. However, the type of validity guarantee depends on the transformation applied. Below, we describe the integration of each transformation strategy within the SCP framework: 

- **Instance Reproduction within SCP (IR-SCP):** The IR-SCP method was introduced by Wang et al. (2014). The original multi-label dataset _Z_ is transformed into an expanded binary dataset _ZIR_ . The resulting dataset is split into a proper-training set and a calibration set: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0004-09.png)


A classifier is trained on _Ztr_ to predict the relevance of each label independently. For each label _λj ∈L_ , nonconformity scores are computed on the calibration set _Zcal_ , and p-values are calculated for the testing pair ( _xn_ +1 _, λj_ ). 

The prediction region includes all labels with p-values exceeding the significance level: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0004-12.png)


The error per label is defined as 


![](markdown_output/katsios25a_images/katsios25a.pdf-0004-14.png)


where _ψn_ +1 is the true label-set of instance _xn_ +1. And the overall error, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0004-16.png)


4 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

The IR-SCP guarantees coverage of individual labels as opposed to label-sets and the prediction is valid if 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-02.png)


- **Binary Relevance within SCP (BR-SCP):** The BR-SCP approach, described in Wang et al. (2015), reformulates the dataset separately for each label _λj ∈L_ , resulting in _d_ binary datasets. For each label, the dataset is split into a proper-training and calibration set: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-04.png)


A separate binary conformal predictor is trained for each label using _Z_ tr _[j]_[,][and][cali-] bration scores are computed on _Z_ cal _[j]_[.][For][a][test][instance] _[x][n]_[+1][,][p-values] _[p][j]_[(] _[λ][j]_[)][are] computed independently. 

The prediction region is defined as the Cartesian product of the individual predictors, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-07.png)


where each per-label conformal predictor is defined as 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-09.png)


To satisfy overall validity, one can apply the Bonferroni correction, adjusting the per label significance to _d[ε]_[,][ensuring][the][overall][minimum][probability][is][1] _[ −][ε]_[,] 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-11.png)


where _ψn_ +1 is the true label-set of _xn_ +1. 

Furthermore, Lambrou and Papadopoulos (2016) proposed an adjustment to the per label significance to, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-14.png)


which ensures that the prediction region has at most _ε_ probability to occur a Hamming loss greater than _h_ . This refinement enables relaxing the required guarantee so as to obtain tighter prediction regions. 

- **Label Power-Set within SCP (LP-SCP):** The LP-SCP method, introduced by Papadopoulos (2014), directly uses the original multi-label dataset without transforming it. It splits the dataset as 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-17.png)


The LP strategy treats each unique label-set as a distinct class. A multi-class classifier is trained on _Z_ tr, and nonconformity scores are computed on _Z_ cal. For a test instance _xn_ +1, p-values are calculated for each candidate label-set _Yc ∈P_ ( _L_ ). 

The prediction region includes all label-sets whose p-values exceed the significance level: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0005-20.png)


5 

Katsios Papadopoulos 

For the prediction region Γ _[ε] xn_ +1 _[⊆P]_[(] _[L]_[), LP-SCP provides the same validity guarantee] (17). This approach directly controls the probability of covering the full multi-label vector, at the cost of increased computational complexity and label sparsity. 

Papadopoulos (2014) proposed a nonconformity measure for LP-SCP based on the sum of absolute differences between the predicted probabilities of the model and the multihot encoding of label-sets in _P_ ( _L_ ). This measure captures the degree of disagreement between the model’s predicted probabilities and the label assignments. In addition to the base measure, the same work introduced a penalization condition that incorporates structural information from the training data. Specifically, a penalty term, scaled by a weight parameter, is added to the nonconformity score. This term penalizes label-sets of non resembled pairs of labels according the data in the proper-training set. 

Building on this, Maltoudoglou et al. (2022) represented the relationship between probability vectors and label-sets as data points and used the Euclidean norm to compute nonconformity scores, enabling a more geometric interpretation. The authors also proposed a computationally efficient method for handling datasets with a large number of labels. This method reduces the number of candidate label-sets in the power-set by eliminating those that are guaranteed to have p-values below a given significance level. The approach calculates the change in nonconformity score for each label resulting from adding it to or removing it from the predicted label-set. These changes are sorted in descending order, and their cumulative sum is computed until it reaches a specified threshold corresponding to the significance level _ε_ . The number of terms included in this cumulative sum determines a subset of the _P_ ( _L_ ) that is guaranteed to include all label-sets of the conformal prediction region. 

The recent work of Tyagi and Guo (2023) presented another a method of reducing the possible label-sets of the power-set _P_ ( _L_ ). Particularly, they proposed a treebased conformal prediction method that accounts for label dependencies and uncertainty. Their approach applies hierarchical clustering on label-sets, effectively capturing the relationships among labels. The method formulates the prediction task as a multiple hypothesis testing problem within this hierarchical structure. By applying split-conformal prediction, marginal p-values are obtained for each hypothesis. Two hierarchical testing procedures are then employed: a standard hierarchical Bonferroni procedure and a modified version designed to control the family-wise error rate (FWER). 

In summary, while IR-SCP and BR-SCP provide scalable marginal guarantees, LP-SCP is the only framework that guarantees validity without relying on conservative approximations. A comprehensive comparison of the three SCP methods can be found in (Wang et al., 2015). 

## **3. Multilabel SCP with Extended Mahalanobis Measure** 

Within the LP-SCP framework for Multi-label classification our recent work (Katsios and Papadopoulos, 2024) proposed the Mahalanobis nonconformity measure. This approach effectively integrates the geometric robustness of Mahalanobis distance with the formal calibration properties of conformal prediction and offers reliable uncertainty quantification in 

6 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

multi-label classification, yielding prediction sets that adapt to the dependencies among labels and predicted probabilities. In this section we present an extension of the Mahalanobis nonconformity measure. Our work was inspired by (Papadopoulos, 2014), where nonconformity scores are penalized for candidate label-sets containing pairs of labels that were not observed in the proper-training set. 

## **3.1. SCP with Mahalanobis Measure** 

We define nonconformity using the Mahalanobis distance, a measure that accounts for the correlation structure among label-wise prediction errors. Each input instance is represented by a vector _**x** i_ = ( _xi_ 1 _, ..., xis_ ), where _xi ⊆_ R _[s]_ and _s_ is the number of attributes. Moreover, we convert the label-sets _ψi_ into multi-hot vectors **y** _i_ = (y _i_ 1 _, ...,_ y _id_ ), where y _ij_ = 1 if _λj ∈ ψi_ and 0 otherwise, for every _λj ∈L_ with _j_ = 1 _, ..., d_ . In this way, we form the subspace _Y_ = _{_ 0 _,_ 1 _}[d]_ of multi-hot vectors in correspondence with the set Ψ. Under this conversion, we denote the dataset with the multi-hot vectors as _Z_ = �( _**x** i,_ **y** _i_ ) : _xi ∈ X,_ y _i ∈ Y_ � for _i_ = 1 _, ..., n_ . For each pair ( _**x** i,_ **y** _i_ ) we compute the _error vector_ _**r** i_ = _|_ **y** _i −_ _**o**_ ( _**x** i_ ) _|_ , where _**o**_ ( _**x** i_ ) = ( _oi_ 1 _, ..., oid_ ) denotes the underlying model’s predicted label probabilities for instance _**x** i_ as a vector of R _[s]_ , with _oik ∈_ [0 _,_ 1] for _k_ = 1 _, ..., d_ . The Mahalanobis nonconformity scores are then calculated as 


![](markdown_output/katsios25a_images/katsios25a.pdf-0007-04.png)


where Σ is the covariance matrix of error vectors obtained from the proper-training set, _**r** i_ for _i_ = _q_ +1 _, ..., n_ is the error vector of calibration instances, while _**r** n_ +1 is the error vector of the test instance assigned candidate label-set ( _**x** n_ +1 _,_ **y** _**c**_ ). Rather than computing p-values, one can alternatively determine a threshold value such that any label with a nonconformity score below this threshold is included in the prediction region. To do so, the calibration scores are sorted in ascending order and denoted as _a[desc] i[′]_ for _i[′]_ = 1 _, ..., n − q_ , satisfying _a[desc]_ 1 _< ... < a[desc] n−q_[.][The][index][of][the][threshold][value,][for][any][given][significance][level] _[ε]_[,][is] the minimum integer _i[′] ε[∈{]_[1] _[, ..., n][ −][q][}]_[.][This][is][calculated][by][the][following][formula,] 


![](markdown_output/katsios25a_images/katsios25a.pdf-0007-06.png)


Given _i[′] ε_[,][the][prediction][set][for][a][new][instance] _[x][n]_[+1][at][the] _[ε]_[significance][level][the][threshold] value is _a[desc] i[′] ε_ . The prediction region is written in the form, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0007-08.png)


## **3.2. Structural Penalties: Hamming Distance and Cardinality** 

To further incorporate structural similarity with previously seen label-sets, we introduce a Hamming distance penalty (Hp) and Cardinality penalty (Cp), which quantify how dissimilar a candidate label vector is from the empirical distribution of label-sets in the propertraining data. These terms serve as regularizers that bias the nonconformity scores toward candidate label vectors that are closer to those encountered in the training data, thereby reducing the likelihood of selecting implausible label-sets in the prediction region. 

7 

Katsios Papadopoulos 

**Hamming Distance Penalty.** The Hamming distance penalty (Hp) quantifies how much a candidate label vector differs from the label-sets observed in the proper-training data. In the context of multi-label classification, the normalized Hamming distance (Hd) between two multi-hot vectors is defined as the proportion of components on which they differ from being equal. For two multi-hot vectors **y** 1 = (y11 _, . . . ,_ y1 _d_ ) and **y** 2 = (y21 _, . . . ,_ y2 _d_ ) the normalized Hamming distance is given by: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0008-02.png)


where _⊕_ denotes the bitwise XOR operation, and _d_ is the total number of labels. The value of _Hd_ lies in the interval [0 _,_ 1], with 0 indicating identical label vectors and 1 indicating complete dissimilarity. 

We now define the Hamming distance penalty used in our framework: 

**Definition 1** _We define the Hamming distance penalty (Hp) for a possible label-set_ _**y** c ∈ Y as the minimum value of the normalized Hamming distances between the label-set_ _**y** c and every proper-training label-set_ **y** _i,_ 


![](markdown_output/katsios25a_images/katsios25a.pdf-0008-06.png)


**Cardinality Penalty.** To further guide the prediction model toward realistic label combinations, we introduce the Cardinality penalty, which penalizes candidate label-sets whose number of active labels deviates from the cardinality numbers observed in the propertraining set. 

For the _q_ multi-hot label vectors in the proper-training set _{_ **y** 1 _,_ **y** 2 _, . . . ,_ **y** _q} ⊆{_ 0 _,_ 1 _}[d]_ , where each **y** _i_ = (y _i_ 1 _, . . . ,_ y _id_ ) represents the labels for the _i_ -th instance, and _d_ is the total number of labels. The cardinality of a label vector **y** _i_ is defined as: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0008-09.png)


The empirical frequency distribution _fcard_ : _{_ 0 _,_ 1 _, . . . , d} →_ [0 _,_ 1] of cardinalities is defined as 


![](markdown_output/katsios25a_images/katsios25a.pdf-0008-11.png)


where I[ _·_ ] is the indicator function that returns 1 if the condition is true and 0 otherwise. The calculation (27) gives the empirical probability that a randomly selected label vector from the proper-training set has cardinality _b_ . By construction, the empirical distribution satisfies, 


![](markdown_output/katsios25a_images/katsios25a.pdf-0008-13.png)


Using (27), we define the Cardinality penalty as follows: 

8 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

**Definition 2** _Let Card_ ( _**y** c_ ) _denote the cardinality of a candidate label-set_ _**y** c. We define the Cardinality penalty (Cp) for the_ _**y** c as_ 


![](markdown_output/katsios25a_images/katsios25a.pdf-0009-02.png)


Both Hp and Cp are computed as preprocessing steps for all candidate vectors in _Y_ , using Hamming distance and cardinality derived from the proper-training label vectors. 

## **3.3. Extended Mahalanobis Measure** 

The Hp and Cp penalties are incorporated additively into the Mahalanobis nonconformity score to form an extended score that favors structurally plausible label-sets. 

The new nonconformity measure is defined as follows: 

**Definition 3** _For an instance x and a multi-hot_ y _, the extended Mahalanobis nonconformity measure is written in the form_ 


![](markdown_output/katsios25a_images/katsios25a.pdf-0009-08.png)


_where_ _**r**_ = _|_ **y** _−_ _**o**_ ( _**x**_ ) _| is the error vector of the pair_ ( _**x** ,_ **y** ) _, Hp_ **y** _and Cp_ **y** _are the structural penalties associated with the multi-hot vector_ _**y** and µ, ν ∈_ R _._ 

The parameters _µ_ and _ν_ control the relative influence of the structural penalties Hp and Cp, respectively, in the extended nonconformity measure. Specifically, _µ_ determines the degree to which the Hamming-based penalty affects the nonconformity score, thereby modulating the preference for label-sets that are closer to those observed in the proper-training data. Similarly, _ν_ adjusts the impact of the cardinality penalty Cp, which biases predictions toward label-sets with more plausible label cardinalities. 

The complete algorithm of LP-SCP with the extended Mahalanobis measure is given in Algorithm 1. 

## **4. Experiments on Multi-label Datasets** 

In this section, we evaluate the performance of the LP-SCP framework using the proposed extension of the Mahalanobis nonconformity measure, comparing it against the standard Mahalanobis measure. The evaluation focuses on the effectiveness of incorporating structural penalties into the nonconformity score, particularly in terms of the resulting reduction to the size of prediction regions 

## **4.1. Experimental setting** 

For experimenting, we employ three multi-label datasets, the Emotions, the PlantPseAAC and the Yeast dataset, with distinct properties. Table 1 provides detailed information on the datasets, including the number of instances, attributes, labels, average cardinality[1] and density[2] . Our experiments were performed following a 10-fold cross-validation process, which was repeated 10 times. The results were calculated as the average over all folds and repetitions. 

> 1. Average Cardinality : measures the average number of labels associated with each instance 

> 2. Density : cardinality divided by the number of labels 

9 

Katsios Papadopoulos 

**Algorithm 1:** LP-SCP using Extended Mahalanobis Measure **Input:** 

- Classifier’ s predicted probabilities for: 

**–** proper-training data _**o**_ ( _**x** i_ ), _i_ = 1 _, ..., q_ 

**–** calibration data _**o**_ ( _**x** i_ ) , _i_ = _q_ + 1 _, ..., n_ 

**–** test instance _o_ ( _**x** n_ +1) 

- Label-sets of: 

**–** proper-training data **y** _i_ , _i_ = 1 _, ..., q_ 

**–** calibration data **y** _i_ , _i_ = _q_ + 1 _, ..., n_ 

- Parameters _µ_ , _ν_ 

- Required significance level _ε_ 

1. Preprocessing on proper-training data: 

   - Calculate the error vectors _**r** i_ = _|_ _**o**_ ( _**x** i_ ) _−_ **y** _**i** |_ , _i_ = 1 _, ..., q_ 

   - Form the covariance matrix Σ using error vectors _**r** i_ , _i_ = 1 _, ..., q_ 

   - Generate all binary vectors _Y_ 

   - For each _**y** c ∈ Y_ calculate _Hp_ _**y** c_ using (25) 

   - For each _**y** c ∈ Y_ calculate _Cp_ _**y** c_ using (29) 

2. Preprocessing on calibration data: 

• Calculate the calibration nonconformity scores a **[y]** _**x[i]** i_[,] _[i]_[ =] _[ q]_[ + 1] _[, ..., n]_[,][using][(][30][)] • Sort calibration scores in descending order a _[desc] i[′]_ , _i[′]_ = 1 _, ..., n − q_ 

- Calculate _i[′] ε_[using][(][22][)] 

3. Calculate scores a _**[y] x**[c] n_ +1[,][for][every][possible][label-set] _**[y] c**[∈][Y]_[ ,][using][(][30][)] 

**Output:** Predicted set, Γ _[ε]_ _**x** n_ +1[=] � _**y** c ∈ Y_ : a _**[y] x**[c] n_ +1 _[≤]_[a] _[desc] i[′] ε_ � 

10 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

Table 1: Dataset Characteristics 

|Dataset|Instances|Attributes|Labels|Average Cardinality|Density|
|---|---|---|---|---|---|
|Emotions|593|72|6|1.868|0.311|
|PlantPseAAC|978|452|12|1.078|0.089|
|Yeast|2417|103|14|4.237|0.302|



For LP-SCP the training set of each fold was further divided into proper-training, validation and calibration sets. In particular, the partition of each dataset is given in Table 2. 

Table 2: Dataset Partition 

|Dataset|Proper-training|Validation|Calibration|Test|
|---|---|---|---|---|
|Emotions|354|80|99|59|
|PlantPseAAC|704|132|176|97|
|Yeast|1522|327|653|241|



In our experiments, we employ the XGBoost algorithm as the underlying classifier to address binary classification tasks for each label independently. To this end, we utilized the MultiOutputClassifier from scikit-learn library to facilitate simultaneous prediction of multiple labels in the dataset. For each label, an individual XGBoost model was trained with a logistic objective, incorporating techniques such as early stopping and validation on a per-label basis to prevent overfitting. 

No hyperparameter tuning was performed, as the goal of this study was not to optimize classification performance, but rather to evaluate the effects of the proposed extensions to the nonconformity scores. A standard configuration of XGBoost is used to ensure stable and reasonably good baseline performance. Note that the proposed nonconformity measures are independent of the underlying model and can be applied with any suitable base classifier, depending on the characteristics of the dataset. 

In table 3, we present the performance of the underlying XGBoost classifier (with calibration set included in the training set) on the three datasets in terms of four standard multi-label classification metrics. 

Table 3: Underlying Classifier Evaluation with Standard Multi-label Metrics 

||Emotions|PlantPseAAC|Yeast|
|---|---|---|---|
|Hamming loss|0.199|0.090|0.197|
|Accuracy|0.270|0.073|0.150|
|F1 Micro|0.651|0.135|0.642|
|F1 Macro|0.617|0.065|0.377|



11 

Katsios Papadopoulos 

## **4.2. Evaluation Criteria** 

We evaluate the performance of the LP-SCP framework using two key metrics, the _N_ - criterion (see (Vovk et al., 2016)), which assesses the size of the prediction regions, and the empirical validity, which measures the actual coverage achieved at a specified significance level. 

To analyze the impact of structural penalties on the effectiveness of LP-SCP, we report the average size of the prediction regions using the _N_ -criterion. This metric quantifies the mean number of label-sets included in the prediction region across all test instances for a given significance level _ε_ . Formally, the _N_ -criterion is defined as: 


![](markdown_output/katsios25a_images/katsios25a.pdf-0012-04.png)


where Γ _[ε]_ _**x** i_[denotes the prediction region for the] _[ i]_[-th test instance at significance level] _[ ε]_[, and] _g_ is the total number of test instances. A smaller _N_ -criterion indicates more statistically efficient predictions, as fewer candidate label-sets are retained. 

To assess the validity of LP-SCP, we compute coverage, which represents the proportion of test instances for which the true label vector falls within the predicted region. This metric evaluates whether the conformal predictor satisfies its theoretical coverage guarantee. The empirical validity is given by 


![](markdown_output/katsios25a_images/katsios25a.pdf-0012-07.png)


where _**y** n_ + _i_ is the true multi-label vector for the _i_ -th test instance, Γ _[ε]_ _**x** n_ + _i_[is the corresponding] prediction region, and I _{·}_ is the indicator function. A conformal predictor is considered valid if _C_[ˆ] ( _ε_ ) closely approximates the nominal coverage level 1 _− ε_ . 

## **4.3. Individual Effect of Structural Penalties** 

This subsection presents experimental results evaluating the impact of the structural penalties _Hp_ and _Cp_ , each applied with a weight of 1. Their effectiveness is compared against the baseline Mahalanobis nonconformity measure, which does not incorporate any structural penalty. Figures 1, 2, and 3 display the _N_ -criterion values for significance levels in range [0 _._ 01 _,_ 0 _._ 1]. The penalty configurations are denoted as weight pairs ( _µ, ν_ ), where _µ_ is the weight assigned to _Hp_ and _ν_ to _Cp_ . Each line in the plots corresponds to one of the following configurations: (0,0) for the standard Mahalanobis measure, (1,0) for Mahalanobis with only the _Hp_ penalty, and (0,1) for Mahalanobis with only the _Cp_ penalty. 

For the Emotions dataset (Figure 1), both structural penalties lead to a consistent reduction in the size of the prediction regions compared to the unpenalized Mahalanobis baseline (configuration (0,0)). The _Hp_ penalty (configuration (1,0)) yields the most substantial reduction across all significance levels, followed closely by the _Cp_ penalty (configuration (0,1)). This suggests that label dependencies, which are captured effectively by _Hp_ , play a dominant role in this dataset’s label structure. 

For the PlantPseAAC dataset (Figure 2), the pattern differs. The _Cp_ penalty (configuration (0,1)) significantly outperforms both the baseline and the _Hp_ penalty (configuration 

12 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

Figure 1: Individual effect of structural penalties per significance level on the Emotions dataset. 

(1,0)), particularly at lower significance levels ( _ε <_ 0 _._ 03), where it results in highly compact prediction regions. This indicates that deviations in label cardinality represent a more informative structural indicator in this dataset. The _Hp_ penalty also reduces region size compared to the baseline, but to a lesser degree and more uniformly across all levels. 

Figure 2: Individual Effect of structural penalties per significance level on the PlantPseAAC dataset. 

In the case of the Yeast dataset (Figure 3), the _Hp_ penalty (configuration (1,0)) again leads to a significant reduction in prediction region size compared to the baseline. This effect can be attributed to the Hamming distance penalty’s tendency to enforce stricter 

13 

Katsios Papadopoulos 

label agreement, thereby reducing the prediction regions. On the other hand, using only the _Cp_ penalty (configuration (0,1)) produces slightly larger prediction regions. 

Figure 3: Individual Effect of structural penalties per significance level on the Yeast dataset. 

Overall, the results demonstrate that the effectiveness of structural penalties is datasetdependent. However, in all cases except for _Cp_ in the Yeast dataset, they significantly reduce prediction region sizes. The small increase in the case of _Cp_ for yeast may be due to the relatively high weight we used, as indicated by the results in the next section. 

## **4.4. Combined Effect of Structural Penalties** 

In this subsection, we evaluate the combined effect of the structural penalties with different weight combinations on the resulting prediction region sizes. The weights for the hamming loss and cardinality penalties were varied across a grid search list for the weight parameter values of[1][1][and][the][resulting][prediction][region][sizes][were][studied][at][significance] 4 _[,]_ 2 _[,]_[ 0] _[,]_[ 1] _[,]_[ 2,] levels ranging from 0 _._ 01 to 0 _._ 1. The focus is examining the overall improvement of the proposed nonconformity measure extension, as well as the effect of the penalty weights on different datasets. 

Particularly, from all the obtained results, the top three combinations and the worst combination of penalty weights - producing the smallest and the largest average prediction region sizes, respectively - at significance level 0 _._ 01 were identified. To ease interpretation across datasets, the prediction region sizes were converted to percentages of the full power- _prediction region size_ set that they correspond to 2 _[d] ,_ where _d_ is the number of classes . 

In Figures 4(a), 5(a) and 6(a), the prediction region size percentages for each of the top three and the worst weight combinations are plotted against significance level, together with those of the baseline Mahalanobis measure (weight configuration (0 _,_ 0)) for comparison. Additionally, Figures 4(b), 5(b) and 6(b) present the average and standard deviation of the prediction region size percentages for all 24 combinations (excluding (0,0)) across the grid search, again with those of the baseline Mahalanobis measure. Moreover, in Tables 4 - 6, we 

14 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

present the percentage point improvement of the top three and worst penalty combinations, as well as the average percentage point improvement for all 24 combinations in the grid search over the standard Mahalanobis measure, at significance levels from 0 _._ 01 to 0 _._ 05. 


![](markdown_output/katsios25a_images/katsios25a.pdf-0015-02.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 4: Effect of different weighted combinations of structural penalties per significance level on the Emotions dataset comparing the base Mahalanobis measure (0 _,_ 0) with: 

4(a): the three best performing weight pairs (2 _,_ 0 _._ 5) _,_ (2 _,_ 1) (2 _,_ 2) and the worst preforming weight pair (0 _,_ 0 _._ 25), 

4(b): average and standard deviation of all 24 combinations of the grid search. 

Table 4: Improvement in Percentage Points on the Emotions dataset 

||(0,0.25)|(2,0.5)|(2,1)|(2,2)|Overall Average|
|---|---|---|---|---|---|
|0.01|5.00|18.91|19.73|20.23|13.39|
|0.02|4.62|20.98|20.67|19.20|12.81|
|0.03|5.96|22.17|21.14|18.38|13.71|
|0.04|5.55|21.02|19.72|16.74|13.04|
|0.05|5.25|20.13|19.08|15.55|12.54|



Overall, the combined effect of the structural penalties yields a consistent trend of reduced prediction region sizes across all three datasets. At the lowest significance level of 0.01, the application of penalties leads to notable reductions. For example, in the emotions dataset, the top-performing weight configuration (2 _,_ 2) reduces the region size from 67% (baseline) to just 46 _._ 77%, marking a reduction of 20 _._ 23 percentage points. Similarly, in the Yeast dataset, (2 _,_ 0) decreases the region size from 46 _._ 37% to 28%, while in the PlantPseAAC dataset, (2 _,_ 2) achieves a reduction from 14 _._ 87% to 2 _._ 59%. 

15 

Katsios Papadopoulos 


![](markdown_output/katsios25a_images/katsios25a.pdf-0016-01.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 5: Effect of different weighted combinations of structural penalties per significance level on the PlantPseAAC dataset comparing the base Mahalanobis measure (0 _,_ 0) with: 

5(a): the three best performing weight pairs (2 _,_ 0 _._ 5) _,_ (2 _,_ 1) (2 _,_ 2) and the worst preforming weight pair (0 _,_ 0 _._ 25), 

5(b): average and standard deviation of all 24 combinations of the grid search. 

Table 5: Improvement in Percentage Points on the PlantPseAAC dataset 

||(0,0.25)|(2,0.5)|(2,1)|(2,2)|Average|Improvement|
|---|---|---|---|---|---|---|
|0.01|3.09|11.95|12.11|12.28||8.96|
|0.02|4.91|8.22|8.29|8.37||7.05|
|0.03|5.41|7.15|7.18|7.20||6.38|
|0.04|5.23|6.30|6.31|6.32||5.71|
|0.05|5.06|5.83|5.84|5.84||5.33|



Both of the Figures 4 - 6 and the Tables 4 - 6 show that a rather significant improvement is achieved across significance levels of all datasets. Even the worst weight combinations reduce the prediction region sizes with the exception of the Yeast dataset. Note that this only happens when the weight of the Hp penalty is set to 0. Figures 4(b) - 6(b) and the last columns of Tables 4 - 6 show that a significant improvement cab be achieved even without an extensive fine tuning of the weights. 

Regarding the influence of the penalty weights across all datasets, the maximum tested value of 2 for _Hp_ consistently appears in the top-performing combinations, indicating that label-wise agreement via the Hamming-based penalty is highly effective. On the other hand, the effect of the cardinality-based penalty _Cp_ is more dataset-dependent. For Emotions and PlantPseAAC, the best values range from 0 _._ 5 to 2, while for Yeast, lower values between 

16 

Incorporating Structural Penalties in Multi-label Conformal Prediction 


![](markdown_output/katsios25a_images/katsios25a.pdf-0017-01.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 6: Effect of different weighted combinations of structural penalties per significance level on the Yeast dataset comparing the base Mahalanobis measure (0 _,_ 0) with: 6(a): the three best performing weight pairs (2 _,_ 0) _,_ (2 _,_ 0 _._ 25) (2 _,_ 0 _._ 5) and the worst preforming weight pair (0 _,_ 2), 

6(b): average and standard deviation of all 24 combinations of the grid search. 

Table 6: Improvement in Percentage Points on the Yeast dataset 

||(0,2)|(2,0.5)|(2,0.25)|(2,0)|Average|Improvement|
|---|---|---|---|---|---|---|
|0.01|-5.70|17.80|18.16|18.37||6.26|
|0.02|-4.69|19.39|20.17|20.42||8.64|
|0.03|-5.04|18.05|18.76|19.10||8.21|
|0.04|-5.03|16.36|17.01|17.32||7.21|
|0.05|-4.42|15.20|15.85|16.10||6.84|



0 and 0 _._ 5 work better. In the PlantPseAAC dataset, where label cardinality distributions are more concentrated, higher weights such as 2 or 1 for _Cp_ perform best, contributing significantly to the reduction. In contrast, for the Yeast dataset, higher values of _Cp_ are less effective and can even worsen results - as shown by the weight configuration (0 _,_ 2) in 6(a) - suggesting that cardinality penalties are not helpful when label cardinality is more varied. The weight value 0 _._ 5 for the _Cp_ penalty strike a good balance for the three datasets. 

Overall, the experimental results presented in this subsection show that both structural penalties, _Hp_ and _Cp_ , can contribute significantly to reducing prediction region sizes. 

## **4.5. Empirical Validity** 

Figure 7 shows the coverage of the prediction regions across all significance levels for the three datasets, using the sampled weight pair (1,1). For all datasets, the coverage closely 

17 

Katsios Papadopoulos 

follows the diagonal line, indicating a strong match between the nominal and empirical coverage rates. The same behaviour was repeated for all weights of combinations. 


![](markdown_output/katsios25a_images/katsios25a.pdf-0018-02.png)


**----- Start of picture text -----**<br>
(a) Emotions (b) PlantPseAAC (c) Yeast<br>**----- End of picture text -----**<br>


Figure 7: Coverage of same weight pair (1 _,_ 1) for the three datasets. 

## **5. Conclusions and Future Work** 

This study proposed an extended Mahalanobis nonconformity measure for multilabel classification under the LP-SCP framework, incorporating structural penalties based on Hamming distance and label cardinality deviation from proper-training label-sets. These penalties increase the nonconformity of unlikely label combinations according to the training data, and therefore focus prediction regions on the most likely label-sets. Our experimental results on three datasets demonstrated that the incorporation of structural penalties can lead to significantly more compact prediction regions. 

Our examination of the individual penalties reveals that their impact is dataset-dependent. The Hamming-based penalty ( _Hp_ ) has the strongest effect on the Emotions and Yeast datasets, consistently leading to improved performance when assigned higher weights. In contrast, the cardinality-based penalty ( _Cp_ ) has the greatest influence on the PlantPseAAC dataset, where label cardinalities are more concentrated. When the penalties are combined, performance improves even further across all datasets. In particular, the best results are obtained when _Hp_ is set to its highest tested value of 2, emphasizing the benefit of enforcing label-wise agreement. For _Cp_ , optimal values vary, lower weights (e.g., 0 _._ 5) are more effective for Yeast, while higher weights (e.g., 1 or 2) perform better on PlantPseAAC and Emotions. In all cases, the combined approach yields performance improvements ranging from 15 to 20 percentage points for the Emotions dataset, 5 to 12 percentage points for the PlantPseAAC dataset, and 15 to 20 percentage points for the Yeast dataset, compared to the standard Mahalanobis-based nonconformity measure without penalties. 

Our future plans include the examination of improvements to the penalty functions and especially _Cp_ , and the inclusion of a regularization parameter for the covariance matrix. Further experimentation on different datasets is also important to test how well the method generalizes. 

18 

Incorporating Structural Penalties in Multi-label Conformal Prediction 

## **References** 

- Giannis Haralabopoulos, Ioannis Anagnostopoulos, and Derek McAuley. Ensemble deep learning for multilabel binary classification of user-generated content. _Algorithms_ , 13(4): 83, 2020. 

- Kostas Katsios and Harris Papadopoulos. Multi-label conformal prediction with a mahalanobis distance nonconformity measure. _Proceedings of Machine Learning Research_ , 230: 1–14, 2024. 

- Antonis Lambrou and Harris Papadopoulos. Binary relevance multi-label conformal predictor. In _Conformal and Probabilistic Prediction with Applications_ , pages 90–104. Springer, 2016. 

- Lysimachos Maltoudoglou, Andreas Paisios, Ladislav Lenc, Jiˇr´ı Mart´ınek, Pavel Kr´al, and Harris Papadopoulos. Well-calibrated confidence measures for multi-label text classification with a large number of labels. _Pattern Recognition_ , 122:108271, 2022. 

- Andrew Maxwell, Runzhi Li, Bei Yang, Heng Weng, Aihua Ou, Huixiao Hong, Zhaoxian Zhou, Ping Gong, and Chaoyang Zhang. Deep learning architectures for multi-label classification of intelligent health risk prediction. _BMC bioinformatics_ , 18:121–131, 2017. 

- Harris Papadopoulos. A cross-conformal predictor for multi-label classification. In _Artificial Intelligence Applications and Innovations: AIAI 2014 Workshops: CoPA, MHDW, IIVC, and MT4BD, Rhodes, Greece, September 19-21, 2014. Proceedings 10_ , pages 241–250. Springer, 2014. 

- Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alex Gammerman. Inductive confidence machines for regression. In _Machine learning: ECML 2002: 13th European conference on machine learning Helsinki, Finland, August 19–23, 2002 proceedings 13_ , pages 345–356. Springer, 2002a. 

- Harris Papadopoulos, Vladimir Vovk, and Alexander Gammerman. Qualified prediction for large data sets in the case of pattern recognition. In _ICMLA_ , pages 159–163, 2002b. 

- Johannes R¨uckert, Louise Bloch, Raphael Br¨ungel, Ahmad Idrissi-Yaghir, Henning Sch¨afer, Cynthia S Schmidt, Sven Koitka, Obioma Pelka, Asma Ben Abacha, Alba G. Seco de Herrera, et al. Rocov2: Radiology objects in context version 2, an updated multimodal image dataset. _Scientific Data_ , 11(1):688, 2024. 

- Grigorios Tsoumakas and Ioannis Katakis. Multi-label classification: An overview. _International Journal of Data Warehousing and Mining (IJDWM)_ , 3(3):1–13, 2007. 

- Chhavi Tyagi and Wenge Guo. Multi-label classification under uncertainty: A tree-based conformal prediction approach. In _Conformal and Probabilistic Prediction with Applications_ , pages 488–512. PMLR, 2023. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ , volume 29. Springer, 2005. 

19 

Katsios Papadopoulos 

- Vladimir Vovk, Valentina Fedorova, Ilia Nouretdinov, and Alexander Gammerman. Criteria of efficiency for conformal prediction. In _Conformal and Probabilistic Prediction with Applications: 5th International Symposium, COPA 2016, Madrid, Spain, April 20-22, 2016, Proceedings 5_ , pages 23–39. Springer, 2016. 

- Huazhen Wang, Xin Liu, Bing Lv, Fan Yang, and Yanzhu Hong. Reliable multi-label learning via conformal predictor and random forest for syndrome differentiation of chronic fatigue in traditional chinese medicine. _PloS one_ , 9(6):e99565, 2014. 

- Huazhen Wang, Xin Liu, Ilia Nouretdinov, and Zhiyuan Luo. A comparison of three implementations of multi-label conformal prediction. In _Statistical Learning and Data Sciences: Third International Symposium, SLDS 2015, Egham, UK, April 20-23, 2015, Proceedings 3_ , pages 241–250. Springer, 2015. 

- Zhi Zhong, Masato Hirano, Kazuki Shimada, Kazuya Tateishi, Shusuke Takahashi, and Yuki Mitsufuji. An attention-based approach to hierarchical multi-label music instrument classification. In _ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , pages 1–5. IEEE, 2023. 

20 

