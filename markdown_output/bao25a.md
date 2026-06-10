Conformal and Probabilistic Prediction with Applications 

Proceedings of Machine Learning Research 266:1–23, 2025 

## **A Review and Comparative Analysis of Univariate Conformal Regression Methods** 

**Jie Bao** 1486103897@qq.com _Huaiyin Institute of Technology, Huai’an, China_ **Nicolo Colombo** nicolo.colombo@rhul.ac.uk _Royal Holloway, University of London, Egham, Surrey, UK_ **Valery Manokhin** Valery.Manokhin.2015@live.rhul.ac.uk _Independent Researcher_ **Suqun Cao** caosuqun@hyit.edu.cn _Huaiyin Institute of Technology, Huai’an, China_ **Rui Luo** ruiluo@cityu.edu.hk _City University of Hong Kong, Hong Kong, China_ 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

As machine learning models continue to evolve and improve, quantifying their uncertainty has become increasingly crucial in high-stakes applications. Conformal prediction has emerged as a powerful tool and has been widely applied in univariate regression tasks. While numerous conformal regression methods and models have been developed, few studies have provided a unified summary and comparison of these approaches. In this paper, we address this gap by discussing, summarizing, and providing an overview of the majority of existing univariate conformal regression methods. Furthermore, we conduct a detailed examination and experimentation of eight major, popular, and advanced conformal regression methods, representing a significant contribution to the field by offering a comprehensive analysis and insights into their performance and applicability. 

**Keywords:** conformal prediction, exchangeable, conformal regression, uncertainty quantification. 

## **1. Introduction** 

In many real-world applications, accurately quantifying the uncertainty of model predictions is crucial for risk management, especially in high-stakes fields such as medical diagnosis (Vazquez and Facelli, 2022; Luo et al., 2024), autonomous driving (Lindemann et al., 2023; Chen et al., 2024), and financial risk control (Angelopoulos et al., 2022; Overman et al., 2024). Conformal Prediction (CP) (Fontana et al., 2023; Angelopoulos et al., 2023) presents a statistically rigorous framework that provides probabilistic guarantees, transforming point predictions from traditional machine learning models into prediction intervals with well-defined coverage probabilities. This framework, grounded in the fundamental assumption of data exchangeability, is capable of generating prediction intervals that adhere to a pre-established confidence level without any reliance on the particular model architecture. In recent years, CP (Huang et al., 2024) has exhibited notable efficacy across various machine learning realms, encompassing regression analysis (Romano et al., 2019), multiclass decision-making (Luo and Zhou, 2024), and beyond. 

Conformal prediction, as a method for generating valid confidence intervals without assuming the data-generating distribution _P_ ( _X|Y_ ) or the prediction model _f_ (Vovk et al., 2005; Shafer and Vovk, 2008), and has gained increasing attention. Currently, univariate conformal regression is the primary research direction in this field. Many scholars have developed extensions of this approach, including Conformal Quantile Regression (Romano et al., 2019), Conformal Histogram Regression 

© 2025 J. Bao, N. Colombo, V. Manokhin, S. Cao & R. Luo. 

Bao Colombo Manokhin Cao Luo 

(Sesia and Romano, 2021), Conformal Thresholded Intervals (Luo and Zhou, 2025b), etc., all of which have made significant contributions to the advancement of conformal regression. 

In this paper, we provide a comprehensive survey and comparative analysis of the state-of-theart conformal regression methods. Our main contributions are as follows: 

- We offer a detailed categorization and discussion of a wide range of existing conformal regression techniques. 

- We examine and summarize the underlying principles and models of eight leading and cuttingedge conformal regression methods. 

- We visualize the differences in prediction intervals produced by these methods through simulation experiments. 

- We perform experiments on twelve real-world datasets using these eight methods, followed by an in-depth comparison and discussion of the results. 

To present these contributions in a clear and structured manner, the remainder of the paper is organized as follows. Section 2 establishes the necessary background on conformal prediction, reviewing its foundational concepts and recent methodological advancements. Section 3 provides a detailed exposition of the eight distinct conformal regression methods that are the focus of our study, elaborating on their underlying mechanics and theoretical differences. Section 4 is dedicated to our extensive empirical evaluation, beginning with a simulation study to visually illustrate the behavior of each method, followed by a rigorous quantitative comparison on twelve real-world datasets. Finally, Section 5 concludes the paper by summarizing our key findings, discussing the relative strengths and weaknesses of the evaluated approaches, and outlining promising directions for future research. 

## **2. Background** 

Conformal prediction (CP) Vovk et al. (2005) is a methodology designed to generate prediction regions for variables of interest, facilitating the estimation of model uncertainty by providing prediction sets rather than point estimates. CP has been successfully applied to both classification Luo and Zhou (2024); Luo and Colombo (2024); Luo and Zhou (2025d) and regression tasks Luo and Zhou (2025e,f). Its flexibility allows adaptation to various real-world scenarios, including segmentation Luo and Zhou (2025a), games Luo et al. (2024); Bao et al. (2025), time-series forecasting Su et al. (2024), and graph-based applications Luo et al. (2023); Tang et al. (2025); Luo and Zhou (2025c); Wang et al. (2025); Luo and Zhou (2025b); Zhang et al. (2025). 

Consider a univariate regression problem where the objective is to predict a scalar response _y ∈Y_ = R based on a feature vector _x ∈X ⊆_ R _[p]_ . We assume that there exists a true joint distribution _FXY_ over _X × Y_ , and we have access to a dataset 


![](markdown_output/bao25a_images/bao25a.pdf-0002-11.png)


where the pairs ( _x_ ( _i_ ) _, y_ ( _i_ )) are independent and identically distributed according to _FXY_ . Given a new feature vector _x_ , we denote the conditional distribution of _Y_ given _X_ = _x_ as _FY |X_ = _x_ and the corresponding probability density function as _fY |X_ = _x_ (when it exists). Using the dataset _D_ , CP allow us to transform any point predictor, denoted by _h_[ˆ] , into a calibrated, distribution-free prediction interval _C_[ˆ] ( _x_ ) _⊆Y_ for the true response _y_ . These intervals come with finite-sample coverage guarantees of the form: 


![](markdown_output/bao25a_images/bao25a.pdf-0002-13.png)


2 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

where 1 _− α_ is the desired coverage level. 

## **2.1. Split Conformal Prediction** 

Traditional split conformal prediction methods (Vovk et al., 1999; Papadopoulos et al., 2002; Vovk et al., 2005, 2009; Lei et al., 2013) guarantee marginal coverage in finite samples by randomly partitioning data into training and calibration sets, then constructing prediction intervals for new samples using quantiles of nonconformity scores computed on the calibration data. However, these methods often suffer from the following limitations: 

- **Fixed Width:** Standard split CP constructions typically rely on global score distributions, which results in prediction intervals with nearly uniform width across all inputs, failing to adequately adapt to local heterogeneity in conditional distributions. 

- **Simple Residual Calibration:** Most approaches use absolute residuals as nonconformity scores, without fully leveraging local data information, potentially yielding prediction intervals that are either excessively conservative or insufficiently precise in certain regions. 

## **2.2. Advances in Base Regression Models for CP** 

The performance of the base regression model has a decisive impact on the quality of prediction intervals within the conformal regression framework (Magdon-Ismail and Atiya, 1998; Meinshausen and Ridgeway, 2006; Chipman et al., 2010; Kivaranovic et al., 2020; Moon et al., 2021; Du et al., 2022). Researchers have significantly enhanced the effectiveness of CP by integrating advanced regression techniques across different methodological paradigms: 

Early studies focused on combining CP with classical regression models. For example, Lei and Wasserman (2014) proposed using linear regression to model local patterns, while Johansson et al. (2014b) introduced decision tree-based approaches to adaptively partition the feature space. These foundational works demonstrated the potential of leveraging model-specific structures to improve interval adaptivity. 

Subsequent research expanded into more sophisticated techniques. Papadopoulos et al. (2008, 2011) pioneered localized modeling by constructing prediction intervals using k-nearest neighbor regression, directly incorporating neighborhood information into nonconformity scores. Johansson et al. (2014a) combined random forests with quantile regression, thereby leveraging ensemble learning to enhance model robustness and handle heterogeneous data distributions. Furthermore, in the domain of deep learning, Johansson et al. (2015) developed a bagged neural network quantile regression model, while Romano et al. (2019) proposed a two-model architecture using separate quantile regressors for interval bounds. 

Recent innovations further address computational and theoretical challenges. Kivaranovic et al. (2020) introduced a framework that divides the prediction into three parts: lower bounds, medians, and upper bounds to capture complex data patterns. Bostr¨om et al. (2017) optimized quantile estimation processes for random forests through acceleration algorithms. Notably, Gibbs et al. (2025) embedded test point features directly into an augmented quantile regression model to explicitly control conditional coverage. Extensions like Sousa et al. (2024) handle heteroscedasticity via dynamic variance estimation, while Rosenberg et al. (2022) unified multivariate predictions through nonlinear vector quantile regression. 

Collectively, these advances aim to reduce model uncertainty while maintaining the theoretical rigor of conformal methods, ensuring precise marginal coverage and progress toward conditional coverage guarantees. 

3 

Bao Colombo Manokhin Cao Luo 

## **2.3. Recent Improvements in Prediction Interval Construction** 

Building upon the foundational frameworks of conformal prediction, recent methodological developments have introduced significant refinements in constructing adaptive prediction intervals. These improvements primarily focus on three key technical directions: conditional density estimation, residual-based calibration, and localized adaptation strategies, each offering unique advantages in constructing adaptive prediction intervals. 

**Conditional Density Estimation Approaches.** A key direction involves leveraging explicit estimates of conditional distributions _fY |X_ = _x_ to construct locally adaptive intervals. For instance, Izbicki et al. (2019) utilize conditional density functions to model data distributions directly, enabling theoretically optimal interval construction under distributional assumptions. The SPICE framework (Diamant et al., 2024) employs neural networks to estimate _fY |X_ = _x_ , while Plassier et al. (2024) propose the CP2 method combining conformity score transformations with conditional density estimation to achieve approximate conditional validity. 

**Residual Distribution Methods.** Alternative approaches exploit residual distributions to adjust interval widths. Chen et al. (2018) introduced a method for determining prediction intervals by analyzing residual distributions and considering specified significance levels. Building on similar ideas, Barber et al. (2021) proposed constructing prediction intervals centered around the median (or alternatively, the mean) of predictions obtained through a leave-one-out approach. Meanwhile, Lei et al. (2018) developed the Split Conformal Prediction Sets method, which involves randomly partitioning the data into two subsets, _I_ 1 and _I_ 2. The model _µ_ is trained on _I_ 1, and residuals are computed and sorted on _I_ 2. Prediction intervals are then constructed based on these sorted residuals and a pre-selected _α_ level, ensuring a desired level of confidence. More recently, Luo and Zhou (2025c) refined this approach by calculating residuals between predicted and true labels within each subset and leveraging these residuals to construct more robust prediction sets. 

**Localized Adaptation Strategies.** To achieve conditional coverage guarantees, some methods employ spatial adaptation mechanisms. The RLCP method (Hore and Barber, 2025) introduces randomized local weighting to adjust conformity thresholds, while Kiyani et al. (2024a) (PLCP) partitions the covariate space into regions with homogeneous uncertainty levels. Colombo (2024) propose redefining conformity measures _ϕx_ ( _·_ ) to explicitly depend on _X_ , enabling input-dependent interval scaling. For covariate shift scenarios, Wieczorek (2023) adjust score distributions through sampling weights derived from design-based estimators. Complementary approaches proposed by van der Laan and Alaa (2024) generate instance-specific calibration sets, and Gil et al. (2024) identify homogeneous regions where conformity scores exhibit uniform distributions. Additionally, Cheung et al. (2024) address interval asymmetry via bias-aware adjustments. 

## **2.4. Other Works in Conformal Regression** 

Existing works extend conformal regression along two main directions: tight integration with regression training objectives and adaptations to real-world regression challenges. 

**Training-aware methods.** Recent advances embed conformal principles directly into model training processes. Three primary approaches emerge: (a) Bilevel optimization frameworks that co-optimize regression parameters and prediction interval thresholds (Kiyani et al., 2024b); (b) Hybrid loss functions unifying point estimation and uncertainty calibration through terms like distributional alignment (Pouplin et al., 2024) and coverage-aware regularization (Gao et al., 2024); (c) Adaptive mechanisms including input-dependent prediction distributions (Vovk et al., 2020) and spatially-aware density estimators (Plassier et al., 2024), which dynamically adjust intervals using 

4 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

local uncertainty patterns. There is also a part of work Bellotti (2021); Stutz et al. (2022); Colombo (2023) that proposes training conformal prediction on classification tasks to achieve smaller uncertainty. 

**Real-world adaptations.** Methodological extensions address practical constraints: Cross-validation conformal methods (Vovk, 2015) improve computational scalability, while specialized variants handle federated learning (Humbert et al., 2023), missing covariates (Zaffran et al., 2023), and discrete responses (Sesia et al., 2023). Spatial calibration techniques (Meister and Nguyen, 2025) maintain validity under distribution shifts through auxiliary variable encoding and geometric sketching. These innovations preserve conformal methods’ finite-sample coverage guarantees while expanding applicability to complex data ecosystems. 

## **3. Conformal Prediction for Regression** 

In this section, we will provide a detailed introduction to several distinct methods of conformal frediction for regression that have been developed to date. We will elaborate on their connections and differences in sequence. These methods represent the most popular and cutting-edge approaches currently available. 

**Split Conformal Regression (Papadopoulos et al., 2002; Vovk et al., 2005).** First, we need to randomly partition a given dataset into a training set, a calibration set, and a test set, ˆ denoted as _I_ train, _I_ cal, and _I_ test, respectively. We require a basic predictive model _yi_ = _f_[ˆ] ( _xi_ ), which is trained on the training set _I_ train. Subsequently, we compute the conformity scores _Si_ , on the calibration set _I_ cal: 


![](markdown_output/bao25a_images/bao25a.pdf-0005-06.png)


_Split conformal regression_ utilizes the absolute residuals to determine the 1 _− α_ prediction interval for a new test point _xn_ +1 _∈I_ test: 


![](markdown_output/bao25a_images/bao25a.pdf-0005-08.png)


where _t_[Split] 1 _−α_[is][the][(1] _[ −][α]_[)(1 + 1] _[/][|I]_[cal] _[|]_[)-th][empirical][quantile][of] _[{][S] i_[Split] _}i∈I_ cal _∪{∞}_ . Under the exchangeability assumption, this guarantees marginal coverage: 


![](markdown_output/bao25a_images/bao25a.pdf-0005-10.png)


**Conformal Quantile Regression (1)(Romano et al., 2019).** _Conformal Quantile Regression_ constructs intervals based on quantile regression: 


![](markdown_output/bao25a_images/bao25a.pdf-0005-12.png)


where _q_ ˆ _α/_ 2 and _q_ ˆ1 _−α/_ 2 are conditional quantile estimates, and _t_[CQR] 1 _−α_[is][the][(1] _[ −][α]_[)(1 + 1] _[/][|I]_[cal] _[|]_[)-th] empirical quantile of _{Si_[CQR] _}i∈I_ cal _∪{∞}_ , with: 


![](markdown_output/bao25a_images/bao25a.pdf-0005-14.png)


5 

Bao Colombo Manokhin Cao Luo 

**Conformal Quantile Regression (2) (Kivaranovic et al., 2020).** Similar to Sesia and Cand`es (2020), we name the methods proposed by Kivaranovic et al. (2020) as CQR-m, respectively, which differ from the CQR proposed by Romano et al. (2019). First, let’s consider CQR-m. The model defined based on quantile regression is as follows: 


![](markdown_output/bao25a_images/bao25a.pdf-0006-02.png)


where _q_ ˆ1 _/_ 2 indicates an estimated median regression function obtained with the same black-box ˆ ˆ algorithm as _qα/_ 2 and _q_ 1 _−α/_ 2, and _t_[CQR-m] 1 _−α_ is the same (1 _− α_ )(1 + 1 _/|I_ cal _|_ )-th empirical quantile of _{Si_[CQR-m] _}i∈I_ cal _∪{∞}_ , with: 


![](markdown_output/bao25a_images/bao25a.pdf-0006-04.png)


In addition, there is an improved version of CQR-m, which does not require estimating the quantile of the regression median (Sesia and Cand`es, 2020). The prediction interval it constructs is as follows: 


![](markdown_output/bao25a_images/bao25a.pdf-0006-06.png)


where _t_[CQR-r] 1 _−α_ is the (1 _− α_ )(1 + 1 _/|I_ cal _|_ )-th empirical quantile of _{Si_[CQR-r] _}i∈I_ cal _∪{∞}_ , with: 


![](markdown_output/bao25a_images/bao25a.pdf-0006-08.png)


**Conformal Quantile Regression with Full Model (Kivaranovic et al., 2020).** CQRFM builds upon CQR-m by introducing a modification that allows the model to output three distinct values: the lower bound, median, and upper bound simultaneously from a single neural network. The key idea is to train a neural network _N_ : R _[d] →_ R[3] such that _N_ ( _x_ ) = ( _l_ ( _x_ ) _, m_ ( _x_ ) _, u_ ( _x_ )), where _l_ , _m_ , and _u_ are functions that estimate the _α/_ 2-quantile, the median, and the (1 _− α/_ 2)-quantile, respectively, with the constraint that _l_ ( _x_ ) _≤ m_ ( _x_ ) _≤ u_ ( _x_ ) for all _x ∈_ R _[d]_ . 

The network is trained using a modified quantile regression loss function: 


![](markdown_output/bao25a_images/bao25a.pdf-0006-11.png)


where _hτ_ ( _u_ ) = ( _τ −_ **1** _u≤_ 0) _u_ is the standard quantile regression loss function. 

Similar to CQR-m, the prediction interval is constructed as: 


![](markdown_output/bao25a_images/bao25a.pdf-0006-14.png)



![](markdown_output/bao25a_images/bao25a.pdf-0006-15.png)


6 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

**Conformal Histogram Regression (Sesia and Romano, 2021).** _Conformal Histogram Regression_ constructs prediction intervals by estimating the full conditional density _fY |X_ using histograms and finding the shortest interval ( _a, b_ ) such that: 


![](markdown_output/bao25a_images/bao25a.pdf-0007-02.png)



![](markdown_output/bao25a_images/bao25a.pdf-0007-03.png)


**Localized Conformal Prediction (Guan, 2023).** _Localized Conformal Prediction_ (LCP) generalizes the framework of conformal prediction by offering a single-test-sample adaptive construction that emphasizes a local region around the test sample. LCP introduces a localizer function _H_ ( _x, x[′]_ ) : R _[p] ×_ R _[p] →_ [0 _,_ 1] that captures the similarity between feature values, with _H_ ( _x, x_ ) = 1 for all _x_ . For a test point _xn_ +1, LCP assigns different weights to calibration samples based on their proximity to _xn_ +1. 

Let _Hn_ +1 _,i_ = _H_ ( _xn_ +1 _, xi_ ) be the localizer evaluated at _xn_ +1 and _xi_ , and define the weighted empirical distribution: 


![](markdown_output/bao25a_images/bao25a.pdf-0007-06.png)


where _p[H] i,j_[=] _[H][ij][/]_[ �] _[n] k_ =1[+1] _[H][ik]_[for] _[j]_[=][1] _[, . . . , n]_[ + 1][are][the][normalized][weights.][To][ensure][finite-] sample marginal coverage, LCP requires finding a suitable _α_ that satisfies: 


![](markdown_output/bao25a_images/bao25a.pdf-0007-08.png)


where _F_[ˆ] _i_ is the weighted empirical distribution with weights centered at _xi_ , and _Q_ (˜ _α_ ; _F_[ˆ] _i_ ) is the _α_ ˜-quantile of this distribution. The prediction interval for the test point _xn_ +1 is then given by: 


![](markdown_output/bao25a_images/bao25a.pdf-0007-10.png)


LCP can be versatilely paired with a diverse range of conformal scores. For instance, it utilizes the standard residual score (3). 

**Conformal Thresholded Intervals (Luo and Zhou, 2025b).** _Conformal Thresholded Intervals_ achieves prediction set size minimization through selective inclusion of narrower probability ranges. This mechanism operationalizes the confidence set definition as: 


![](markdown_output/bao25a_images/bao25a.pdf-0007-13.png)


where _Si_[CTI] is the (1 _− α_ ) _−_ th quantile of the empirical distribution: 


![](markdown_output/bao25a_images/bao25a.pdf-0007-15.png)


ˆ where _k_ is the given quantile step size, and _Ik_ ( _xi_ ) = (ˆ _qk−_ 1( _x_ ) _, qk_ ( _x_ )] for _k_ = 1 _, . . . , K._ 

We conducted a comparative analysis of eight distinct conformal regression methods (1). Our findings indicate that CTI and CHR generate narrower prediction intervals while demonstrating superior robustness in handling data with conditional distribution shifts. We theoretically analyzed 

7 

Bao Colombo Manokhin Cao Luo 


![](markdown_output/bao25a_images/bao25a.pdf-0008-01.png)


**----- Start of picture text -----**<br>
CTI(RF) CTI(NN)<br>Be, i 60 1.0 q 60<br>0.8 50 sf 50<br>0.8<br>0.6 é 3 f 40 0.6 i ca | 40<br>i : 30 eae sal 30<br>0.4 ie i 0.4 a ao<br>:<br>20 20<br>fec eT4 4 ois)<br>0.2 ts 0.2<br>| A o 10 is 0 09 uy 10<br>pages 1 al Bee ne er nS<br>IS _O BHC goo ie o oe? Bera Foes2 °° So 5 °Oo SX °°<br>oP ers 259 i ° 5 0.0 pa o 8 °<br>0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8<br>X X<br>CHR(RF) CHR(NN)<br>60 60<br>i ose<br>a oom<br>0.8 50 0.8 50<br>2<br>0.6 40 0.6 40<br>30 & 30<br>0.4 0.4<br>20 20<br>0.2 D a ° 0.2 2 6°<br>f Jo 10 - omnowatil 10<br>Rare SOPOPSam 8 BPP. OBO°sag SPO 8 Ing rQh OO550” °© 098 ; 08 &eo0 0° 0 Pree On B o HS 3°°, leXe} SO 2 40~~6.0O°oO© 008 ; 08 &0000 0°O° 0<br>0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8<br>X X<br>CQR CQRM<br>1.0<br>60 60<br>0.8 50 0.8 50<br>0.6 40 0.6 40<br>30 30<br>0.4 0.4 ;<br>20 20<br>ogy<br>Be on OPO.<br>0.2 of o EUR 1 0.2 igR000 8B °<br>5coWe°20, °o8 8 08ogce) @00SoO 10 bs oSSo"200oiego°0° “098°006 086 &5008 10<br>Mars, eee8 8 BP.O° oS8 8° % o |; 0 Pere hts®  @ oo 58° 8° % o , 0<br>0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8<br>X X<br>Y Y<br>Overlap Count Overlap Count<br>Y Y<br>Overlap Count Overlap Count<br>Y Y<br>Overlap Count Overlap Count<br>**----- End of picture text -----**<br>


Figure 1: In the figure, the scatter points with coordinates ( _x, y_ ) represent features ( _x_ ) and true labels ( _y_ ). Any conformal regression method will generate a prediction interval for each of these scatter points. For the purpose of visualizing the prediction intervals produced by each method, we set a uniform width of 0 _._ 01 for these intervals, while the height of each interval is determined by the conformal regression model. This approach ensures that the rectangular boxes representing each model’s intervals have consistent width but varying heights. Naturally, wider prediction intervals result in taller rectangular boxes, and overlapping may occur between adjacent boxes. The denser the overlapping regions, the larger the size of the resulting prediction set. To facilitate visualization, we use different colors to represent the density of these generated intervals, allowing us to intuitively discern the differences between these methods. Additionally, we depict scatter points that fall within their respective prediction intervals in red, while those outside the intervals are shown in black. The same visualization approach is applied to Figure 2. 

8 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 


![](markdown_output/bao25a_images/bao25a.pdf-0009-01.png)


**----- Start of picture text -----**<br>
CQRR CQRFM<br>1.0<br>60 60<br>oS24<br>pes QS<br>0.8 50 0.8 50<br>0.6 40 0.6 40<br>30 30<br>0.4 0.4<br>20 20<br>ae CLO V el oS Woghd<br>0.2 S000 ®oo wut oa 38Og oo ° © 10 0.2 So °° & P09 Saas o6 P3S 00° [2] 10<br>8. 9 Vo ° 68 OF Woo oe) er Oo gc° _o 8 58 08 ®%o0°<br>B SPO 6° OL ° BS CO 0° © 9 8 °<br>OO ae BPO oO ° 0 Boo EP QO ° ° 0<br>0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8<br>X X<br>LCP Split<br>60 60<br>BOS gi OBR,<br>0.8 Rend 50 0.8 Somes moa 50<br>EB<br>0.6 40 0.6 40<br>0.4 som 30 30<br>0.2 _ aysesi OO } BF 6  OF BD 0 80.WP08 Ogg Baie BD008OS20BOKL6£8 OS, 5OLS° 20 0.40.2 ereAc i) 9SEEDet P88= AP e800, oboi 20<br>Be S70 e° e° ° gS a 26 00 2<br>0.0 i] C0 °8 0 ° ° 10 BPOo 40oO 80° S68 Oo Booe 10<br>0.0 ® MoO o8 f° °<br>0 0<br>0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8<br>X X<br>Y Y<br>Overlap Count Overlap Count<br>Y Y<br>Overlap Count Overlap Count<br>**----- End of picture text -----**<br>


Figure 2: Synthetic figures. 

9 

Bao Colombo Manokhin Cao Luo 

|**Method**||**basic**<br>**model**|**Additional resource**<br>**investment**|**Robustness to**<br>**Conditional Shift**|**Small average**<br>**size**|**Asymptotic time**<br>**complexity**|**Asymptotic space**<br>**complexity**|**Predictive interval**<br>**continuous**|
|---|---|---|---|---|---|---|---|---|
|Split||Point prediction model|✗|★★✩✩✩|★✩✩✩✩|_O_(_N_log_N_)|_O_(_N_)|✓|
|CQR||Quantile regression model|✓|★✩✩✩✩|★★✩✩✩|_O_(_N_log_N_)|_O_(_N_)|✓|
|CQR-m||Quantile regression model|✗|★★✩✩✩|★★★✩✩|_O_(_N_log_N_)|_O_(_N_)|✓|
|CQR-r||Quantile regression model|✗|★✩✩✩✩|★★✩✩✩|_O_(_N_log_N_)|_O_(_N_)|✓|
|CQRMF|a|specially designed neural network|✓|★★★✩✩|★★★✩✩|_O_(_N_log_N_)|_O_(_N_)|✓|
|CHR||Quantile regression model|✓|★★★★✩|★★★★✩|_O_(_N_2)|_O_(_N_2)|✓|
|LCP||Any model|✓|★★★✩✩|★★★✩✩|_O_(_N_2 log_N_)|_O_(_N_2)|✓|
|CTI||Quantile regression model|✓|★★★★★|★★★★★|_O_(_N_log_N_)|_O_(_MN_)|✗|



Table 1: A comparison of different conformal regression methods in terms of resource consumption, performance, and other aspects. 

the asymptotic time and space complexity as the calibration set size n approaches infinity, where M in the CTI framework represents the number of quantiles. In empirical evaluations, CTI, CHR, and LCP exhibited the longest computation times, followed by CQRFM and then CQRR (owing to its three-quantile structure). Notably, CQR-m demonstrated slightly increased latency compared to standard CQR due to the additional quantile computation, while Split maintained the fastest performance. The performance ranking generally followed this temporal hierarchy, with the exception of LCP: although this method serves as an enhancement to the Split approach, its localization mechanism can also be applied to improve other arbitrary models’ performance. 

## **4. Experiment** 

## **4.1. Simulation Study** 

Following the methodology outlined in Luo and Zhou (2025b), we generate the training data by drawing _n_ = 10000 independent, univariate predictor samples _Xi_ from a uniform distribution on the interval [0 _,_ 1][1] . The response variable _Yi_ is then sampled independently and identically distributed (i.i.d.) according to: 


![](markdown_output/bao25a_images/bao25a.pdf-0010-07.png)


where Triangular(0 _, x, x_ ) is the Triangular distribution with lower limit 0, upper limit _x_ , and mode _x_ . The conditional density is: 


![](markdown_output/bao25a_images/bao25a.pdf-0010-09.png)


Figures 1-2 illustrates the distribution patterns of prediction intervals generated by various conformal regression methods in our simulation experiments. The color gradient from blue through orange, green, purple, to yellow indicates increasing frequency of interval overlaps. Distinct methodological differences can be visually discerned from these patterns. 

First, the CTI method produces discrete prediction intervals, as evidenced by discontinuous matrix blocks in the visualization. Two key observations confirm this method’s characteristics: 1) The prediction intervals are generally narrower, manifested through smaller overall matrix occupation in the plot; 2) Reduced presence of purple and orange regions indicates fewer areas with high overlap frequencies. Similar characteristics can be observed in the CHR method. Additionally, tail coverage analysis reveals higher performance in regions where _Y <_ 0 _._ 1 and _Y >_ 0 _._ 9, as indicated by an increased number of red scatter points. 

> 1. All the code for this experiment comes from the following links: `https://github.com/ml-stat-Sustech/TorchCP` , `https://github.com/luo-lorry/CTI` , and `https://github.com/LeyingGuan/LCP` . Additionally, all the visualization code for our experiments is sourced from: `https://github.com/bjbbbb/Conformal-Regression-Summarize` . 

10 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

|**Name**|**Description**|**n**|**d**|
|---|---|---|---|
|bike (dat, a)<br>bio (dat, b)<br>ph<br>blog (dat, c)<br>community (dat, d)<br>concrete (dat, e)<br>facebook 1 (dat, f)<br>facebook 2 (dat, f)<br>homes (dat, g)<br>meps 19 (dat, h)<br>meps 20 (dat, i)<br>meps 21 (dat, j)<br>star (Achilles et al., 2008)|bike sharing<br>ysicochemical properties of protein tertiary structure<br>blog feedback<br>community and crime<br>concrete compressive strength<br>facebook comment volume<br>facebook comment volume<br>sale prices of homes in King County, Washington<br>medical expenditure panel survey<br>medical expenditure panel survey<br>medical expenditure panel survey<br>Tennessee’s student-teacher achievement ratio|10886<br>s<br>45730<br>52397<br>1994<br>1030<br>40948<br>81311<br>21613<br>15785<br>17541<br>15656<br>2161|18<br>9<br>280<br>100<br>8<br>53<br>53<br>19<br>139<br>139<br>139<br>39|



Table 2: Dataset descriptions 


![](markdown_output/bao25a_images/bao25a.pdf-0011-03.png)


**----- Start of picture text -----**<br>
Distribution of Target Values: Bike Distribution of Target Values: Bio Distribution of Target Values: Blog_data Distribution of Target Values: Community<br>20001750 5000 140000 200<br>150012501000750 400030002000 1200001000008000060000 17515012510075<br>500250 1000 4000020000 5025<br>0 0 1 2 3 4 5 0 0.0 0.5 1.0 1.5 2.0 2.5 0 0 25 50 75 100 125 150 175 200 0 0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0<br>Target Value (y) Target Value (y) Target Value (y) Target Value (y)<br>Distribution of Target Values: Concrete Distribution of Target Values: Facebook_1 Distribution of Target Values: Facebook_2 Distribution of Target Values: Homes<br>706050 10000080000 350000300000250000 800070006000<br>40 60000 200000 5000<br>302010 4000020000 15000010000050000 4000300020001000<br>0 0.0 0.5 1.0 1.5 2.0 0 0 25 50 75 100 125 150 175 0 0 50 100 150 200 250 0 0 2 4 6 8 10 12 14<br>Target Value (y) Target Value (y) Target Value (y) Target Value (y)<br>Distribution of Target Values: Star<br>Distribution of Target Values: Meps_19 Distribution of Target Values: Meps_20 Distribution of Target Values: Meps_21 120<br>16000 17500 16000 100<br>14000120001000080006000 1500012500100007500 14000120001000080006000 806040<br>4000 5000 4000 20<br>20000 0 10 20 Target Value (y)30 40 50 60 70 25000 0 10 20 Target Value (y)30 40 50 60 20000 0 10 20 Target Value (y)30 40 50 60 0 0.85 0.90 0.95 Target Value (y)1.00 1.05 1.10 1.15 1.20<br>Density Density Density Density<br>Density Density Density Density<br>Density<br>Density Density Density<br>**----- End of picture text -----**<br>


Figure 3: The distribution plots of the target variable _y_ for different datasets. 

The CQR family exhibits distinct limitations: All variants generate unnecessarily wide intervals for _x ∈_ [0 _,_ 0 _._ 2], resulting in increased interval lengths. Among these, CQR-r produces the largest intervals, while CQR-m and CQRFM demonstrate moderate improvements. Comparative analysis between CQR and CQR-m, as well as CQR-r and CQRFM, reveals that CQRM and CQRFM achieve significantly better tail coverage. 

Finally, the LCP method - enhanced through split-based optimization of _Si[split]_ - demonstrates the most efficient interval allocation, characterized by reduced green region density. This approach generates compact prediction intervals while maintaining superior tail coverage performance. 

## **4.2. Real Data** 

Following the methodology outlined in Sesia and Cand`es (2020), we rescale the response _Y_ by the mean absolute value. We randomly allocate 20% of the samples for testing, and from the remaining data, we utilize 70% for training the quantile regression model and 30% for calibration. This split has been validated in Sesia and Cand`es (2020). We repeat all experiments 50 times, starting from the initial data splitting. For the training procedure of quantile regression, except for 

11 

Bao Colombo Manokhin Cao Luo 


![](markdown_output/bao25a_images/bao25a.pdf-0012-01.png)


**----- Start of picture text -----**<br>
Bike - p(Y|X) Bio - p(Y|X) Blog_data - p(Y|X)<br>0.4395 3 0.4076 200 0.1218<br>5<br>0.2611 0.3130 0.1019<br>4 0.1792 0.2255 150 0.0925<br>2<br>0.1554 0.1456 0.0786<br>3<br>0.1307 0.1070 100 0.0650<br>2 0.1073 1 0.0885 0.0554<br>0.0894 0.0729 0.0429<br>1 50<br>0.0669 0.0549 0.0303<br>0 0.0361 0 0.0321 0.0106<br>2 1 0 1 2 0.0008 2 0 2 4 0.0005 0 2 1 0 1 2 0.0000<br>Most Important Feature 14 Most Important Feature 2 Most Important Feature 60<br>Community - p(Y|X) Concrete - p(Y|X) Facebook_1 - p(Y|X)<br>0.9701 2.5 1.056 0.1094<br>4 0.7310 2.0 0.901 150 0.1047<br>0.5373 0.784 0.0951<br>3<br>0.3764 1.5 0.622 0.0905<br>100<br>2 0.2545 0.443 0.0814<br>0.1646 1.0 0.287 0.0551<br>1 0.0791 0.199 50 0.0463<br>0.5<br>0.0445 0.134 0.0341<br>0 0.0206 0.0 0.067 0.0111<br>1 0 1 2 3 0.0008 1 0 1 2 3 4 5 0.001 0 2 1 0 1 2 0.0000<br>Most Important Feature 50 Most Important Feature 7 Most Important Feature 34<br>Facebook_2 - p(Y|X) Homes - p(Y|X) Meps_19 - p(Y|X)<br>0.1303<br>1.078 0.8919<br>250 0.1166 12.5 0.728 60 0.7987<br>0.1011<br>200 0.0830 10.0 0.5650.432 0.65400.5467<br>150 0.0687 7.5 0.304 40 0.4230<br>0.0537 0.209 0.3000<br>100 0.0371 5.0 0.148 20 0.1980<br>50 0.0212 2.5 0.086 0.0873<br>0.0074 0.031 0.0228<br>0 0 5 10 15 20 25 0.0000 0.0 6 4 2 0 2 4 0.000 0 0 1 2 3 0.0001<br>Most Important Feature 30 Most Important Feature 8 Most Important Feature 100<br>Meps_20 - p(Y|X) Meps_21 - p(Y|X) Star - p(Y|X)<br>0.8912 0.8842 1.2 1.874<br>60 60<br>0.7707 0.7629 1.780<br>50 0.6473 0.6540 1.1 1.693<br>40 0.5069 40 0.5157 1.628<br>0.4152 0.4135 1.517<br>30 0.2836 0.2931 1.0 1.329<br>20 0.1751 20 0.1941 1.085<br>10 0.0738 0.0842 0.9 0.819<br>0.0232 0.0227 0.464<br>0 3 2 1 0 0.0001 0 0 1 2 3 4 0.0001 2 1 0 1 2 0.011<br>Most Important Feature 98 Most Important Feature 100 Most Important Feature 0<br>Density Density Density<br>Target Value Target Value Target Value<br>Density Density Density<br>Target Value Target Value Target Value<br>Density Density Density<br>Target Value Target Value Target Value<br>Density Density Density<br>Target Value Target Value Target Value<br>**----- End of picture text -----**<br>


Figure 4: Given that the features vary across different datasets, to visualize the conditional density distributions, we employ a random forest to identify the most influential features for each dataset. Subsequently, we utilize two-dimensional Kernel Density Estimation (KDE) to plot the conditional distribution diagrams. In these diagrams, white scatter points denote the positions of actual values, with the x-axis representing the features and the y-axis indicating the target values. It can be observed that the distributions of most datasets are highly uneven. The meqs - series datasets exhibit similar distribution patterns, while the Facebook dataset and the blog dataset also share comparable distributions. In contrast, the distributions of the other datasets do not conform to a uniform pattern. 

12 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 


![](markdown_output/bao25a_images/bao25a.pdf-0013-01.png)


**----- Start of picture text -----**<br>
bike 0.877 0.037 1.000 0.000 0.040 0.000 0.000 0.421 0.054<br>1.0<br>bio 0.443 0.004 0.991 0.358 0.018 0.812 0.238 1.000 0.069<br>blog_data 0.360 1.000 0.000 0.430 1.000 0.752 0.908 0.028 1.000<br>0.8<br>community 0.988 0.338 0.993 0.373 0.028 0.635 0.639 0.648 0.004<br>concrete 1.000 0.000 1.000 0.041 0.009 0.538 0.035 0.751 0.000<br>0.6<br>facebook_1 0.503 0.165 0.141 0.394 0.717 0.772 0.477 0.316 0.843<br>facebook_2 0.000 0.165 0.133 0.333 0.804 0.695 0.504 0.311 0.858<br>0.4<br>homes 0.744 0.037 1.000 0.092 0.018 0.527 0.172 0.820 0.073<br>meps_19 0.816 0.482 0.536 1.000 0.166 0.969 0.985 0.012 0.060<br>0.2<br>meps_20 0.794 0.482 0.591 0.965 0.167 1.000 1.000 0.002 0.952<br>meps_21 0.818 0.482 0.574 0.994 0.173 0.971 0.967 0.000 0.405<br>0.0<br>star 0.986 0.114 1.000 0.955 0.000 0.886 0.695 0.541 0.037<br>n_samples n_features zero_one_ratio oob_error pred_variancemax_importanceimportance_entropy nonlinearitylocal_global_ratio<br>Normalized Difficulty Score<br>**----- End of picture text -----**<br>


Figure 5: The heatmap visualizes the relative difficulty of regression datasets across nine normalized metrics. All metrics are scaled using min-max normalization, with three indicators (number of samples, maximum feature importance, and zero-one ratio in target) inverted to align higher values with greater difficulty. Metrics include: n ~~s~~ amples , n ~~f~~ eatures, zero ~~o~~ ne ~~r~~ atio, oob ~~e~~ rror, pred ~~v~~ ariance, max importance, importance ~~e~~ ntropy, nonlinearity, and local ~~g~~ lobal ~~r~~ atio. Rows represent datasets, columns represent metrics, and color intensity reflects normalized difficulty scores (0: easiest, 1: hardest). Higher values in all metrics indicate increased dataset complexity for regression tasks. 


![](markdown_output/bao25a_images/bao25a.pdf-0013-03.png)


**----- Start of picture text -----**<br>
10<br>bike 4 1 5 3 10 6 9 7 2 8<br>bio 1 3 2 4 9 8 10 6 5 7 9<br>blog_data 1 2 4 5 10 6 9 7 8 3 8<br>community 6 1 3 2 7 4 8 5 9 10<br>7<br>concrete 10 1 9 3 8 5 7 6 2 4<br>facebook_1 2 1 4 3 9 6 10 8 5 7 6<br>facebook_2 2 1 4 3 10 7 9 5 6 8 5<br>homes 4 1 5 2 10 6 8 7 3 9<br>4<br>meps_19 1 2 3 4 7 5 8 6 9 10<br>meps_20 1 2 3 4 7 6 8 5 10 9 3<br>meps_21 1 2 3 4 7 6 8 5 10 9 2<br>star 7 8 3 10 5 4 6 2 9 1<br>| 1<br>CTI(RF) CTI(NN) CHR(RF) CHR(NN) CQR CQRM CQRR CQRFM LCP Split<br>**----- End of picture text -----**<br>


Figure 6: The heatmap presents the performance rankings of 10 regression methods across 12 real-world datasets based on prediction interval width (lower values indicate better performance). For each dataset, methods are ranked from 1 (best) to 10 (worst) based on ascending order of their interval width values, with tied ranks resolved by original precision. Rows represent datasets, columns represent methods, and numerical annotations show exact ranks. 

13 

Bao Colombo Manokhin Cao Luo 


![](markdown_output/bao25a_images/bao25a.pdf-0014-01.png)


**----- Start of picture text -----**<br>
CHR(NN) CHR(RF) CQR CQRFM CQRM CQRR CTI(NN) CTI(RF) LCP Split<br>0.8<br>1.8<br>0.95<br>0.92 0.6<br>1.6 0.90<br>0.91 0.4<br>1.4 0.85<br>0.2<br>0.90 1.2 0.80<br>0.0<br>0.75<br>0.89 1.0<br>0.2<br>0.70<br>0.88 0.8 0.4<br>0.65<br>0.915 2.2 0.925 0.5<br>0.910 0.900 0.4<br>2.0<br>0.875<br>0.905 0.3<br>0.900 1.8 0.850 0.2<br>0.825<br>0.895 1.6 0.800 0.1<br>0.890 1.4 0.775 0.0<br>0.750 0.1<br>0.885<br>0.725 0.2<br>0.95<br>1.0<br>0.96 0.90<br>4 0.5<br>0.94 0.85<br>0.92 3 0.80 0.0<br>0.5<br>0.90 2 0.75<br>1.0<br>0.70<br>0.88<br>1 0.65 1.5<br>0.86<br>0 0.60 2.0<br>0.96 2.75 1.0 1.50<br>0.94 2.50 0.9 1.25<br>0.92 2.25 0.8 1.00<br>2.00 0.75<br>0.90 0.7<br>1.75 0.50<br>0.88 0.6<br>1.50 0.25<br>0.86<br>1.25 0.5 0.00<br>0.84 1.00 0.25<br>1.000 1.0 1.5<br>1.1<br>0.975 1.0<br>1.0 0.8<br>0.950<br>0.9 0.5<br>0.925 0.6<br>0.8 0.0<br>0.900<br>0.7 0.4<br>0.875 0.5<br>0.6<br>0.850 0.5 0.2 1.0<br>0.825<br>0.4 0.0 1.5<br>1.00 12 1.0<br>1<br>0.98 10 0.9<br>0.96 8 0.8 0<br>0.94 6 0.7 1<br>0.92 4 0.6 2<br>0.90 2 0.5 3<br>0.88 0.4<br>**----- End of picture text -----**<br>


Figure 7: Box plots comparing various conformal regression methods across multiple datasets and evaluation metrics. Each experiment was conducted with 50 random dataset splits. The datasets are arranged vertically from top to bottom: bike, bio, blog, community, concrete, facebook 1, and facebook 2. The evaluation metrics, displayed horizontally from left to right, include Coverage, Size, BIS, and TCR. 

14 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 


![](markdown_output/bao25a_images/bao25a.pdf-0015-01.png)


**----- Start of picture text -----**<br>
CHR(NN) CHR(RF) CQR CQRFM CQRM CQRR CTI(NN) CTI(RF) LCP Split<br>1.0<br>0.98 4.5 1.0<br>0.96 4.0 0.8<br>3.5 0.5<br>0.94 3.0 0.6<br>2.5 0.0<br>0.92<br>2.0 0.4<br>0.90 1.5 0.5<br>1.0 0.2<br>0.88<br>1.0<br>1.1<br>0.9 1.2<br>0.91 1.0 1.0<br>0.9 0.8 0.8<br>0.90<br>0.6<br>0.8 0.7<br>0.4<br>0.89 0.7<br>0.6 0.2<br>0.88 0.6 0.0<br>0.5 0.5 0.2<br>1.2<br>0.94 3.5 0.9 1.0<br>0.92 3.0 0.8 0.8<br>0.6<br>0.7<br>0.90 2.5 0.4<br>0.6 0.2<br>0.88 2.0 0.0<br>0.5 0.2<br>0.86 1.5<br>1.0<br>0.94 0.9<br>3.5 0.8<br>0.92 3.0 0.8 0.6<br>0.4<br>0.7<br>0.90 2.5 0.2<br>0.6 0.0<br>0.88 2.0<br>0.2<br>0.5<br>1.25<br>4.0<br>0.94 0.9 1.00<br>3.5 0.75<br>0.92 0.8<br>3.0 0.50<br>0.90 0.7 0.25<br>2.5<br>0.00<br>0.6<br>0.88 2.0 0.25<br>0.5 0.50<br>0.86 1.5<br>1.00<br>0.23 0.3<br>0.94<br>0.22 0.95 0.2<br>0.92 0.21 0.1<br>0.90<br>0.90 0.20 0.0<br>0.88 0.19 0.85 0.1<br>0.18 0.80 0.2<br>0.86<br>0.17<br>0.3<br>0.75<br>0.84 0.16<br>0.4<br>**----- End of picture text -----**<br>


Figure 8: Box plots comparing various conformal regression methods across multiple datasets and evaluation metrics. Each experiment was conducted with 50 random dataset splits. The datasets are arranged vertically from top to bottom: facebook 2, homes, meps 19, meps 20, meps 21 and star. The evaluation metrics, displayed horizontally from left to right, include Coverage, Size, BIS, and TCR. 

15 

Bao Colombo Manokhin Cao Luo 

CTI and CHR (both of which employ both random forest (RF) and neural network (NN) models), all other methods utilize RF as the base predictive model. This setup allows us to both observe the impact of different base predictive models on the results and compare different conformal prediction methods. 

Both CTI and CHR integrate the quantile regression results from Random Forests (RF) and Neural Networks (NN). For CQR, CQR-m, and CQR-r, we utilize the results from NN. For NFCP, we employ the Uniform strategy, and for LCP, we use the most basic standard residual score. We adopt four evaluation metrics, including coverage, size, and tail coverage rate (TCR) (Lin et al., 2021). 

While individual metrics such as average interval Size and Worse-Slab Coverage (WSC) (Cauchois et al., 2021) are informative, they often reveal a fundamental trade-off: one method may yield narrower intervals at the cost of weaker conditional coverage, while another does the opposite. To facilitate a more holistic comparison that directly evaluates this balance, we introduce a heuristic metric for this study, the Balanced Interval Score (BIS). It is designed to provide a single, interpretable score for a method’s overall effectiveness. The BIS is formulated as: 


![](markdown_output/bao25a_images/bao25a.pdf-0016-04.png)


The rationale behind this formula is to normalize performance against a common baseline—the standard Split conformal method—and quantify the net gain. The term WSCmethod _/_ WSCsplit measures the relative improvement in conditional coverage robustness, while Sizemethod _/_ Sizesplit represents the relative cost in interval width. By subtracting the relative cost from the relative gain, the BIS captures the overall benefit a method provides over the simple baseline. 

First, we will analyze 12 real-world datasets (as shown in Table 2). We have plotted the distribution of the true _y_ values for these 12 datasets, as illustrated in Figure 3. 

Additionally, as illustrated in Figure 4, we employed Kernel Density Estimation (KDE) to plot the conditional distribution graphs _P_ ( _X | Y_ ) for each dataset. Given that the number of features was not uniform across datasets, we utilized the random forest algorithm to select the most important feature for plotting purposes. Furthermore, we simultaneously plotted the normalized scores of several key indicators that significantly impact the predictive models across different datasets, as shown in Figure 5. It can be observed that the meps series datasets and the blog dataset are the most challenging to predict. Moreover, as depicted in Figure 6, we have also plotted the rankings of various CP methods based on their performance across different dataset sizes, thereby indicating which methods are more adept at handling specific types of datasets. 

Table 3 presents the performance comparison of various conformal regression methods across one simulated dataset and twelve real-world datasets. Notably, the CTI method consistently maintained the smallest prediction interval size across most datasets, while TCR generally achieved the best overall performance. The second-ranked method, CHR, demonstrated superior adaptability on skewed datasets such as Facebook and MEPS. CQR exhibited stable WSC (Width of the Prediction Interval) values across all datasets, though its interval size tended to be larger on skewed data. The CQR method demonstrates favorable BIS performance on certain datasets but underperforms on others. Notably, its interval widths tend to be larger on skewed data. In contrast, CQR-m produces significantly narrower intervals than standard CQR across all datasets, while CQR-r exhibits intermediate performance between CQR and CQR-m with nearly identical BIS values across all three approaches. The CQRFM variant matches CQR-m’s interval dimensions while improving both TCR and BIS metrics. Compared to Split conformal regression, LCP shows consistent improvements in multiple evaluation metrics across most datasets, particularly for BIS. We further 

16 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

|**Dataset**|**Metric**|**CTI(RF)**|**CTI(NN)**|**CHR(RF)**|**CHR(NN)**|**CQR**|**CQRM**|**CQRR**|**CQRFM**|**LCP**|**Split**|
|---|---|---|---|---|---|---|---|---|---|---|---|
||**Coverage**|0.900 (0.011)|0.898 (0.011)|0.897 (0.007)|0.900 (0.009)|0.900 (0.010)|0.901 (0.010)|0.899 (0.009)|0.899 (0.011)|0.916 (0.015)|0.900 (0.010)|
|**synthetic**|**Size**<br>**BIS**|**0.355 (0.007)**<br>—|0.363 (0.012)<br>—|0.361 (0.008)<br>—|0.369 (0.014)<br>—|0.442 (0.020)<br>—-|0.402 (0.020)<br>—|0.434 (0.018)<br>—|0.403 (0.018)<br>—|0.430 (0.039)<br>—|0.475 (0.020)<br>—|
||**TCR**|**0.901 (0.015)**|0.843 (0.034)|0.850 (0.021)|0.833 (0.043)|0.722 (0.072)|0.804 (0.060)|0.744 (0.068)|0.776 (0.080)|0.798 (0.042)|0.764 (0.070)|
||**Coverage**|0.901 (0.009)|0.902 (0.008)|0.902 (0.008)|0.900 (0.009)|0.904 (0.010)|0.903 (0.008)|0.905 (0.009)|0.901 (0.008)|0.903 (0.009)|0.900 (0.010)|
|**bike**|**Size**<br>**BIS**|1.049 (0.033)<br>0.265 (0.010)|**0.722 (0.036)**<br>0.518 (0.006)|1.128 (0.041)<br>0.238 (0.001)|0.757 (0.043)<br>**0.520 (0.005)**|1.564 (0.086)<br>-0.187 (0.022)|1.289 (0.089)<br>0.060 (0.019)|1.534 (0.078)<br>-0.145 (0.022)|1.313 (0.093)<br>0.040 (0.023)|0.740 (0.036)<br>0.485 (0.009)|1.355 (0.094)<br>0.000 (0.000)|
||**TCR**|**0.845 (0.022)**|0.828 (0.021)|0.837 (0.019)|0.844 (0.021)|0.621 (0.058)|0.7000 (0.055)|0.650 (0.060)|0.695 (0.048)|0.814 (0.029)|0.709 (0.041)|
||**Coverage**|0.901 (0.004)|0.900 (0.005)|0.899 (0.004)|0.898 (0.005)|0.899 (0.005)|0.900 (0.004)|0.899 (0.005)|0.899 (0.004)|0.900 (0.005)|0.899 (0.004)|
|**bio**|**Size**<br>**BIS**|**1.297 (0.017)**<br>**0.409 (0.002)**|1.480 (0.028)<br>0.302 (0.003)|1.456 (0.019)<br>0.257 (0.003)|1.578 (0.022)<br>0.326 (0.003)|2.007 (0.024)<br>-0.047 (0.025)|1.984 (0.034)<br>-0.025 (0.004)|2.009 (0.029)<br>-0.048 (0.004)|1.980 (0.041)<br>-0.023 (0.004)|1.780 (0.032)<br>0.135 (0.003)|1.982 (0.053)<br>0.000 (0.000)|
||**TCR**|**0.862 (0.007)**|0.797 (0.010)|0.749 (0.010)|0.724 (0.012)|0.558 (0.026)|0.574 (0.028)|0.556 (0.025)|0.570 (0.027)|0.794 (0.016)|0.731 (0.033)|
||**Coverage**|0.925 (0.006)|0.900 (0.003)|0.901 (0.004)|0.901 (0.005)|0.942 (0.008)|0.908 (0.011)|0.942 (0.008)|0.909 (0.018)|0.897 (0.008)|0.909 (0.005)|
|**blog**|**Size**<br>**BIS**|**0.797 (0.216)**<br>**0.585 (0.022)**|1.006 (0.070)<br>0.377 (0.005)|1.596 (0.125)<br>0.154 (0.010)|1.771 (0.171)<br>0.028 (0.017)|3.340 (0.359)<br>-1.067 (0.070)|1.943 (0.360)<br>-0.265 (0.062)|3.303 (0.360)<br>-1.038 (0.035)|2.053 (0.648)<br>-0.294 (0.162)|2.300 (0.197)<br>-0.624 (0.030)|1.429 (0.105)<br>0.000 (0.000)|
||**TCR**|**0.694 (2.021)**|0.631 (0.016)|0.266 (0.017)|0.249 (0.015)|0.251 (0.019)|0.573 (0.151)|0.297 (0.147)|0.652 (0.048)|0.617 (0.015)|0.101 (0.141)|
||**Coverage**|0.918 (0.020)|0.905 (0.016)|0.899 (0.022)|0.896 (0.019)|0.905 (0.023)|0.900 (0.021)|0.903 (0.022)|0.899 (0.023)|0.905 (0.019)|0.899 (0.021)|
|**community**|**Size**<br>**BIS**|1.679 (0.119)<br>0.410 (0.060)|**1.325 (0.112)**<br>**0.595 (0.060)**|1.636 (0.116)<br>0.430 (0.045)|1.574 (0.104)<br>0.464 (0.055)|1.758 (0.133)<br>0.368 (0.039)|1.661 (0.116)<br>0.418 (0.051)|1.764 (0.116)<br>0.386 (0.060)|1.674 (0.104)<br>0.402 (0.046)|2.069 (0.142)<br>0.152 (0.049)|2.183 (0.224)<br>0.000 (0.000)|
||**TCR**|**0.839 (0.039)**|0.838 (0.044)|0.713 (0.053)|0.771 (0.041)|0.698 (0.094)|0.750 (0.064)|0.658 (0.102)|0.771 (0.066)|0.786 (0.050)|0.670 (0.062)|
||**Coverage**|0.901 (0.024)|0.895 (0.025)|0.903 (0.031)|0.907 (0.024)|0.900 (0.026)|0.902 (0.024)|0.904 (0.025)|0.903 (0.022)|0.898 (0.028)|0.905 (0.026)|
|**concrete**|**Size**<br>**BIS**|0.974 (0.049)<br>-0.555 (0.093)|**0.465 (0.055)**<br>0.243 (0.072)|0.942 (0.065)<br>-0.508 (0.065)|0.493 (0.036)<br>**0.243 (0.050)**|0.700 (0.055)<br>-0.108 (0.063)|0.628 (0.050)<br>0.014 (0.083)|0.699 (0.053)<br>-0.107 (0.062)|0.629 (0.056)<br>0.048 (0.047)|0.466 (0.036)<br>0.199 (0.126)|0.607 (0.051)<br>0.000 (0.000)|
||**TCR**|0.770 (0.058)|**0.895 (0.057)**|0.725 (0.098)|0.880 (0.058)|0.743 (0.091)|0.799 (0.075)|0.768 (0.081)|0.811 (0.081)|0.866 (0.056)|0.802 (0.080)|
||**Coverage**|0.935 (0.005)|0.901 (0.004)|0.901 (0.004)|0.901 (0.005)|0.943 (0.013)|0.913 (0.022)|0.944 (0.013)|0.918 (0.027)|0.900 (0.005)|0.902 (0.005)|
|**facebook1**|**Size**<br>**BIS**|1.048 (0.068)<br>0.842 (0.009)|**0.790 (0.045)**<br>0.751 (0.008)|1.559 (0.103)<br>0.894 (0.015)|1.389 (0.081)<br>**0.975 (0.013)**|2.693 (0.466)<br>0.435 (0.050)|2.148 (0.979)<br>0.588 (0.148)|2.696 (0.345)<br>0.446 (0.032)|2.367 (1.565)<br>0.499 (0.420)|1.925 (0.111)<br>0.242 (0.028)|2.156 (0.188)<br>0.000 (0.000)|
||**TCR**|0.755 (0.023)|0.667 (0.014)|0.356 (0.013)|0.339 (0.012)|0.418 (0.024)|0.835 (0.119)|0.458 (0.013)|**0.880 (0.038)**|0.671 (0.039)|0.540 (0.014)|
||**Coverage**|0.935 (0.004)|0.900 (0.003)|0.899 (0.003)|0.899 (0.003)|0.949 (0.008)|0.910 (0.020)|0.935 (0.076)|0.909 (0.016)|0.900 (0.335)|0.902 (0.003)|
|**facebook2**|**Size**<br>**BIS**|1.014 (0.051)<br>0.845 (0.005)|**0.775 (0.033)**<br>0.730 (0.003)|1.547 (0.059)<br>**0.943 (0.007)**|1.413 (0.068)<br>0.869 (0.007)|2.778 (0.424)<br>0.392 (0.046)|1.910 (0.414)<br>0.651 (0.024)|2.747 (0.597)<br>0.364 (0.105)|1.847 (0.211)<br>0.686 (0.014)|1.883 (0.105)<br>0.244 (0.022)|2.140 (0.177)<br>0.000 (0.000)|
||**TCR**|0.750 (0.016)|0.662 (0.010)|0.345 (0.009)|0.344 (0.008)|0.421 (0.020)|0.825 (0.125)|0.456 (0.129)|**0.871 (0.021)**|0.665 (0.032)|0.532 (0.013)|
||**Coverage**|0.898 (0.006)|0.900 (0.006)|0.900 (0.006)|0.895 (0.005)|0.900 (0.006)|0.901 (0.007)|0.899 (0.005)|0.899 (0.007)|0.896 (0.008)|0.897 (0.006)|
|**homes**|**Size**<br>**BIS**|0.638 (0.013)<br>0.362 (0.021)|**0.517 (0.010)**<br>0.689 (0.022)|0.684 (0.017)<br>0.578 (0.034)|0.538 (0.010)<br>**0.836 (0.027)**|0.847 (0.055)<br>0.231 (0.035)|0.728 (0.034)<br>0.476 (0.031)|0.826 (0.047)<br>0.270 (0.036)|0.734 (0.037)<br>0.458 (0.041)|0.545 (0.022)<br>0.456 (0.034)|0.829 (0.077)<br>0.000 (0.000)|
||**TCR**|0.715 (0.018)|0.785 (0.018)|0.797 (0.016)|**0.851 (0.014)**|0.689 (0.048)|0.729 (0.041)|0.698 (0.045)|0.718 (0.045)|0.733 (0.022)|0.640 (0.036)|
||**Coverage**|0.900 (0.007)|0.900 (0.008)|0.902 (0.007)|0.900 (0.007)|0.928 (0.009)|0.916 (0.010)|0.927 (0.010)|0.918 (0.009)|0.894 (0.012)|0.902 (0.008)|
|**meps19**|**Size**<br>**BIS**|**1.703 (0.082)**<br>0.756 (0.021)|1.801 (0.084)<br>0.696 (0.020)|2.333 (0.163)<br>0.749 (0.026)|2.547 (0.151)<br>0.696 (0.032)|2.898 (0.177)<br>0.521 (0.041)|2.599 (0.168)<br>0.541 (0.035)|2.908 (0.190)<br>0.512 (0.036)|2.622 (0.146)<br>0.557 (0.030)|3.001 (0.389)<br>0.107 (0.064)|3.061 (0.274)<br>0.000 (0.000)|
||**TCR**|0.642 (0.020)|**0.655 (0.024)**|0.252 (0.020)|0.296 (0.018)|0.237 (0.028)|0.280 (0.147)|0.278 (0.130)|0.708 (0.022)|0.642 (0.027)|0.575 (0.031)|
||**Coverage**|0.902 (0.006)|0.901 (0.007)|0.902 (0.006)|0.902 (0.006)|0.927 (0.008)|0.920 (0.009)|0.928 (0.008)|0.918 (0.009)|0.894 (0.011)|0.902 (0.006)|
|**meps20**|**Size**<br>**BIS**|**1.796 (0.070)**<br>0.697 (0.017)|1.882 (0.079)<br>0.662 (0.015)|2.357 (0.148)<br>**0.705 (0.014)**|2.515 (0.118)<br>0.655 (0.013)|2.879 (0.136)<br>0.463 (0.016)|2.745 (0.164)<br>0.471 (0.014)|2.942 (0.147)<br>0.452 (0.017)|2.718 (0.127)<br>0.461 (0.01)2|3.231 (0.418)<br>0.020 (0.040)|3.052 (0.289)<br>0.000 (0.000)|
||**TCR**|0.638 (0.015)|**0.649 (0.018)**|0.237 (0.017)|0.282 (0.015)|0.227 (0.027)|0.277 (0.134)|0.238 (0.072)|0.696 (0.021)|0.637 (0.022)|0.573 (0.035)|
||**Coverage**|0.903 (0.007)|0.901 (0.007)|0.902 (0.007)|0.902 (0.008)|0.930 (0.007)|0.922 (0.009)|0.929 (0.007)|0.920 (0.008)|0.896 (0.013)|0.903 (0.007)|
|**meps21**|**Size**<br>**BIS**|**1.751 (0.089)**<br>**0.702 (0.024)**|1.844 (0.083)<br>0.640 (0.025)|2.474 (0.156)<br>0.627 (0.040)|2.667 (0.179)<br>0.559 (0.042)|2.927 (0.149)<br>0.403 (0.029)|2.714 (0.134)<br>0.424 (0.032)|2.934 (0.196)<br>0.397 (0.032)|2.689 (0.164)<br>0.448 (0.030)|3.217 (0.403)<br>-0.056 (0.064)|2.948 (0.245)<br>0.000 (0.000)|
||**TCR**|0.638 (0.017)|**0.645 (0.019)**|0.234 (0.016)|0.289 (0.018)|0.211 (0.019)|0.239 (0.113)|0.219 (0.071)|0.685 (0.021)|0.642 (0.025)|0.567 (0.031)|
||**Coverage**|0.905 (0.018)|0.902 (0.020)|0.900 (0.019)|0.902 (0.019)|0.905 (0.020)|0.904 (0.018)|0.901 (0.017)|0.900 (0.023)|0.900 (0.022)|0.901 (0.022)|
|**star**|**Size**<br>**BIS**|0.185 (0.005)<br>-0.036 (0.008)|0.193 (0.011)<br>-0.083 (0.010)|0.179 (0.006)<br>-0.010 (0.008)|0.207 (0.007)<br>-0.159 (0.007)|0.181 (0.006)<br>-0.026 (0.007)|0.179 (0.006)<br>-0.013 (0.008)|0.181 (0.006)<br>-0.009 (0.006)|0.178 (0.007)<br>**0.001 (0.008)**|0.199 (0.008)<br>-0.114 (0.006)|**0.177 (0.006)**<br>0.000 (0.000)|
||**TCR**|0.652 (0.075)|**0.713 (0.055)**|0.607 (0.071)|0.724 (0.059)|0.578 (0.079)|0.584 (0.077)|0.571 (0.070)|0.573 (0.090)|0.715 (0.076)|0.603 (0.090)|



Table 3: The coverage, size, WSC and TCR results for various methods are presented in the table. 

generated box plots (Figures 7-8) for four performance metrics across 12 real-world datasets, with each method tested under 50 random data partitions per dataset to ensure robustness. 

**Choice of conformal regression method:** Based on the aforementioned extensive experiments, we hereby offer recommendations on how to select a CP method. First and foremost, a foundational predictive model is required, which holds particular significance for determining the size of the final prediction set. For datasets with a large number of x-features (more than 100), we recommend employing Random Forest as the foundational predictive model. Secondly, we suggest that if the generated prediction set does not require the characteristic of continuity, it is advisable to exclusively use CTI as the CP method. In cases where the dataset distribution is highly complex, we strongly recommend utilizing CHR as the CP method or combining methods such as CQR with LCP to enhance the model’s performance. Finally, when dealing with datasets that have a very small sample size or a simple distribution, we recommend using the Split method. 

## **5. Conclusion** 

This study provides a comprehensive review and in-depth comparative analysis of univariate conformal regression methods, systematically investigating their principles, performance, and re- 

17 

Bao Colombo Manokhin Cao Luo 

source consumption. Our empirical results demonstrate pronounced discrepancies across different techniques in critical metrics such as prediction interval width, coverage probability, and tail coverage performance. While this work establishes a significant benchmark, we acknowledge that its scope is intentionally centered on the popular split conformal prediction framework, valued for its computational efficiency and widespread adoption. This focus naturally illuminates several promising avenues for future research. A crucial next step is to extend this comparative analysis to other foundational paradigms, including full conformal, cross-conformal, and Jackknife+ procedures, which offer different trade-offs between statistical efficiency and computational cost. Beyond this, further progress can be made by pursuing the deep integration of conformal prediction with model training pipelines, developing efficient inference frameworks for resource-constrained environments, extending these paradigms to complex real-world scenarios, and realizing improved conditional coverage guarantees through novel methodological formulations. 

## **Acknowledgments** 

The work described in this paper was partially supported by grants from City University of Hong Kong (9610639, 6000864) and Chengdu Municipal Office of Philosophy and Social Science (2024BS013). 

## **References** 

- Bike sharing dataset data set. `https://archive.ics.uci.edu/ml/datasets/bike+sharing+ dataset` , a. Accessed: July, 2019. 

- Physicochemical properties of protein tertiary structure data set. `https://archive.ics.uci.edu/ ml/datasets/Physicochemical+Properties+of+Protein+Tertiary+Structure` , b. Accessed: July, 2019. 

- BlogFeedback data set. `https://archive.ics.uci.edu/ml/datasets/BlogFeedback` , c. Accessed: July, 2019. 

- Communities and crime data set. `http://archive.ics.uci.edu/ml/datasets/communities+ and+crime` , d. Accessed: July, 2019. 

- Concrete compressive strength data set. `http://archive.ics.uci.edu/ml/datasets/concrete+ compressive+strength` , e. Accessed: July, 2019. 

- Facebook comment volume data set. `https://archive.ics.uci.edu/ml/datasets/Facebook+ Comment+Volume+Dataset` , f. Accessed: July, 2019. 

- House sales in King County, USA. `https://www.kaggle.com/harlfoxem/ housesalesprediction/metadata` , g. Accessed: August, 2019. 

- Medical expenditure panel survey, panel 19. `https://meps.ahrq.gov/mepsweb/data_stats/ download_data_files_detail.jsp?cboPufNumber=HC-181` , h. Accessed: July, 2019. 

- Medical expenditure panel survey, panel 20. `https://meps.ahrq.gov/mepsweb/data_stats/ download_data_files_detail.jsp?cboPufNumber=HC-181` , i. Accessed: July, 2019. 

- Medical expenditure panel survey, panel 21. `https://meps.ahrq.gov/mepsweb/data_stats/ download_data_files_detail.jsp?cboPufNumber=HC-192` , j. Accessed: July, 2019. 

18 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

- C.M. Achilles, Helen Pate Bain, Fred Bellott, Jayne Boyd-Zaharias, Jeremy Finn, John Folger, John Johnston, and Elizabeth Word. Tennessee’s student teacher achievement ratio (STAR) project, 2008. URL `https://doi.org/10.7910/DVN/SIWH9F` . Accessed: July, 2019. 

- Anastasios N Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster. Conformal risk control. _arXiv preprint arXiv:2208.02814_ , 2022. 

- Anastasios N Angelopoulos, Stephen Bates, et al. Conformal prediction: A gentle introduction. _Foundations and Trends® in Machine Learning_ , 16(4):494–591, 2023. 

- Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, and Zhixin Zhou. Enhancing adversarial robustness with conformal prediction: A framework for guaranteed model reliability. In _Proceedings of the Forty-second International Conference on Machine Learning (ICML)_ , 2025. 

- Rina Foygel Barber, Emmanuel J Candes, Aaditya Ramdas, and Ryan J Tibshirani. Predictive inference with the jackknife+. _The Annals of Statistics_ , 49(1):486–507, 2021. 

- Anthony Bellotti. Optimized conformal classification using gradient descent approximation. _arXiv preprint arXiv:2105.11255_ , 2021. 

- Henrik Bostr¨om, Henrik Linusson, Tuve L¨ofstr¨om, and Ulf Johansson. Accelerating difficulty estimation for conformal regression forests. _Annals of Mathematics and Artificial Intelligence_ , 81: 125–144, 2017. 

- Maxime Cauchois, Suyash Gupta, and John C Duchi. Knowing what you know: valid and validated confidence sets in multiclass and multilabel prediction. _Journal of machine learning research_ , 22 (81):1–42, 2021. 

- Wenyu Chen, Kelli-Jean Chun, and Rina Foygel Barber. Discretized conformal prediction for efficient distribution-free inference. _Stat_ , 7(1):e173, 2018. 

- Xi Chen, Rahul Bhadani, and Larry Head. Conformal trajectory prediction with multi-view data integration in cooperative driving. _arXiv preprint arXiv:2408.00374_ , 2024. 

- Matt Y Cheung, Tucker J Netherton, Laurence E Court, Ashok Veeraraghavan, and Guha Balakrishnan. Regression conformal prediction under bias. _arXiv preprint arXiv:2410.05263_ , 2024. 

- Hugh A Chipman, Edward I George, and Robert E McCulloch. Bart: Bayesian additive regression trees. _Annals of Applied Statistics_ , 4(1):266–298, 2010. 

- Nicolo Colombo. On training locally adaptive cp. In _Conformal and Probabilistic Prediction with Applications_ , pages 384–398. PMLR, 2023. 

- Nicolo Colombo. Normalizing flows for conformal regression. _arXiv preprint arXiv:2406.03346_ , 2024. 

- Nathaniel Diamant, Ehsan Hajiramezanali, Tommaso Biancalani, and Gabriele Scalia. Conformalized deep splines for optimal and efficient prediction sets. In _International Conference on Artificial Intelligence and Statistics_ , pages 1657–1665. PMLR, 2024. 

- Shian Du, Yihong Luo, Wei Chen, Jian Xu, and Delu Zeng. To-flow: Efficient continuous normalizing flows with temporal optimization adjoint with moving speed. In _proceedings of the IEEE/CVF conference on computer vision and pattern recognition_ , pages 12570–12580, 2022. 

19 

Bao Colombo Manokhin Cao Luo 

- Matteo Fontana, Gianluca Zeni, and Simone Vantini. Conformal prediction: a unified review of theory and new challenges. _Bernoulli_ , 29(1):1–23, 2023. 

- Ruijiang Gao, Mingzhang Yin, James Mcinerney, and Nathan Kallus. Adjusting regression models for conditional uncertainty calibration. _Machine Learning_ , pages 1–24, 2024. 

- Isaac Gibbs, John J Cherian, and Emmanuel J Cand`es. Conformal prediction with conditional guarantees. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , page qkaf008, 2025. 

- Natalia Martinez Gil, Dhaval Patel, Chandra Reddy, Giridhar Ganapavarapu, Roman Vaculin, and Jayant Kalagnanam. Identifying homogeneous and interpretable groups for conformal prediction. In _Proceedings of the Fortieth Conference on Uncertainty in Artificial Intelligence_ , pages 2471– 2485, 2024. 

- Leying Guan. Localized conformal prediction: A generalized inference framework for conformal prediction. _Biometrika_ , 110(1):33–50, 2023. 

- Rohan Hore and Rina Foygel Barber. Conformal prediction with local weights: randomization enables robust guarantees. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 87(2):549–578, 2025. 

- Jianguo Huang, Jianqing Song, Xuanning Zhou, Bingyi Jing, and Hongxin Wei. Torchcp: A python library for conformal prediction, 2024. 

- Pierre Humbert, Batiste Le Bars, Aur´elien Bellet, and Sylvain Arlot. One-shot federated conformal prediction. In _International Conference on Machine Learning_ , pages 14153–14177. PMLR, 2023. 

- Rafael Izbicki, Gilson T Shimizu, and Rafael B Stern. Flexible distribution-free conditional predictive bands using density estimators. _arXiv preprint arXiv:1910.05575_ , 2019. 

- Ulf Johansson, Henrik Bostr¨om, Tuve L¨ofstr¨om, and Henrik Linusson. Regression conformal prediction with random forests. _Machine learning_ , 97:155–176, 2014a. 

- Ulf Johansson, Cecilia S¨onstr¨od, Henrik Linusson, and Henrik Bostr¨om. Regression trees for streaming data with local performance guarantees. In _2014 IEEE International Conference on Big Data (Big Data)_ , pages 461–470. IEEE, 2014b. 

- Ulf Johansson, Cecilia S¨onstr¨od, and Henrik Linusson. Efficient conformal regressors using bagged neural nets. In _2015 International Joint Conference on Neural Networks (IJCNN)_ , pages 1–8. IEEE, 2015. 

- Danijel Kivaranovic, Kory D Johnson, and Hannes Leeb. Adaptive, distribution-free prediction intervals for deep networks. In _International Conference on Artificial Intelligence and Statistics_ , pages 4346–4356. PMLR, 2020. 

- Shayan Kiyani, George Pappas, and Hamed Hassani. Conformal prediction with learned features. _arXiv preprint arXiv:2404.17487_ , 2024a. 

- Shayan Kiyani, George J Pappas, and Hamed Hassani. Length optimization in conformal prediction. _Advances in Neural Information Processing Systems_ , 37:99519–99563, 2024b. 

- Jing Lei and Larry Wasserman. Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 76(1):71–96, 2014. 

20 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

- Jing Lei, James Robins, and Larry Wasserman. Distribution-free prediction sets. _Journal of the American Statistical Association_ , 108(501):278–287, 2013. 

- Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J Tibshirani, and Larry Wasserman. Distributionfree predictive inference for regression. _Journal of the American Statistical Association_ , 113(523): 1094–1111, 2018. 

- Zhen Lin, Shubhendu Trivedi, and Jimeng Sun. Locally valid and discriminative prediction intervals for deep learning models. _Advances in Neural Information Processing Systems_ , 34:8378–8391, 2021. 

- Lars Lindemann, Matthew Cleaveland, Gihyun Shim, and George J Pappas. Safe planning in dynamic environments using conformal prediction. _IEEE Robotics and Automation Letters_ , 8(8): 5116–5123, 2023. 

- Rui Luo and Nicolo Colombo. Entropy reweighted conformal classification. In _The 13th Symposium on Conformal and Probabilistic Prediction with Applications_ , pages 264–276. PMLR, 2024. 

- Rui Luo and Zhixin Zhou. Trustworthy classification through rank-based conformal prediction sets. _arXiv preprint arXiv:2407.04407_ , 2024. 

- Rui Luo and Zhixin Zhou. Conditional conformal risk adaptation. _arXiv preprint arXiv:2504.07611_ , 2025a. 

- Rui Luo and Zhixin Zhou. Conformal thresholded intervals for efficient regression. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 39(18):19216–19223, 2025b. 

- Rui Luo and Zhixin Zhou. Conformalized interval arithmetic with symmetric calibration. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 39(18):19207–19215, 2025c. 

- Rui Luo and Zhixin Zhou. Conformity score averaging for classification. In _Forty-second International Conference on Machine Learning_ , 2025d. 

- Rui Luo and Zhixin Zhou. Conformal thresholded intervals for efficient regression. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 39(18):19216–19223, 2025e. 

- Rui Luo and Zhixin Zhou. Volume-sorted prediction set: Efficient conformal prediction for multitarget regression. _arXiv preprint arXiv:2503.02205_ , 2025f. 

- Rui Luo, Buddhika Nettasinghe, and Vikram Krishnamurthy. Anomalous edge detection in edge exchangeable social network models. In _Conformal and probabilistic prediction with applications_ , pages 287–310. PMLR, 2023. 

- Rui Luo, Jie Bao, Zhixin Zhou, and Chuangyin Dang. Game-theoretic defenses for robust conformal prediction against adversarial attacks in medical imaging. _arXiv preprint arXiv:2411.04376_ , 2024. 

- Malik Magdon-Ismail and Amir Atiya. Neural networks for density estimation. _Advances in Neural Information Processing Systems_ , 11, 1998. 

- Nicolai Meinshausen and Greg Ridgeway. Quantile regression forests. _Journal of machine learning research_ , 7(6), 2006. 

- Julia A Meister and Khuong An Nguyen. Conformalised data synthesis. _Machine Learning_ , 114 (3):1–37, 2025. 

21 

Bao Colombo Manokhin Cao Luo 

- Sang Jun Moon, Jong-June Jeon, Jason Sang Hun Lee, and Yongdai Kim. Learning multiple quantiles with neural networks. _Journal of Computational and Graphical Statistics_ , 30(4):1238– 1248, 2021. 

- William Overman, Jacqueline Vallon, and Mohsen Bayati. Aligning model properties via conformal risk control. _Advances in Neural Information Processing Systems_ , 37:110702–110722, 2024. 

- Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alex Gammerman. Inductive confidence machines for regression. In _Machine learning: ECML 2002: 13th European conference on machine learning Helsinki, Finland, August 19–23, 2002 proceedings 13_ , pages 345–356. Springer, 2002. 

- Harris Papadopoulos, Alex Gammerman, and Volodya Vovk. Normalized nonconformity measures for regression conformal prediction. In _Proceedings of the IASTED International Conference on Artificial Intelligence and Applications (AIA 2008)_ , pages 64–69, 2008. 

- Harris Papadopoulos, Vladimir Vovk, and Alex Gammerman. Regression conformal prediction with nearest neighbours. _Journal of Artificial Intelligence Research_ , 40:815–840, 2011. 

- Vincent Plassier, Alexander Fishkov, Mohsen Guizani, Maxim Panov, and Eric Moulines. Probabilistic conformal prediction with approximate conditional validity. _arXiv preprint arXiv:2407.01794_ , 2024. 

- Thomas Pouplin, Alan Jeffares, Nabeel Seedat, and Mihaela Van Der Schaar. Relaxed quantile regression: prediction intervals for asymmetric noise. _arXiv preprint arXiv:2406.03258_ , 2024. 

- Yaniv Romano, Evan Patterson, and Emmanuel Candes. Conformalized quantile regression. _Advances in neural information processing systems_ , 32, 2019. 

- Aviv A Rosenberg, Sanketh Vedula, Yaniv Romano, and Alex M Bronstein. Fast nonlinear vector quantile regression. _arXiv preprint arXiv:2205.14977_ , 2022. 

- Matteo Sesia and Emmanuel J Cand`es. A comparison of some conformal quantile regression methods. _Stat_ , 9(1):e261, 2020. 

- Matteo Sesia and Yaniv Romano. Conformal prediction using conditional histograms. _Advances in Neural Information Processing Systems_ , 34:6304–6315, 2021. 

- Matteo Sesia, Stefano Favaro, and Edgar Dobriban. Conformal frequency estimation using discrete sketched data with coverage for distinct queries. _Journal of Machine Learning Research_ , 24(348): 1–80, 2023. 

- Glenn Shafer and Vladimir Vovk. A tutorial on conformal prediction. _Journal of Machine Learning Research_ , 9(3), 2008. 

- Martim Sousa, Ana Maria Tom´e, and Jos´e Moreira. Improving conformalized quantile regression through cluster-based feature relevance. _Expert Systems with Applications_ , 238:122322, 2024. 

- David Stutz, Ali Taylan Cemgil, Arnaud Doucet, et al. Learning optimal conformal classifiers. _International Conference on Learning Representations (ICLR)_ , 2022. 

- Xiaoyi Su, Zhixin Zhou, and Rui Luo. Adaptive conformal inference by particle filtering under hidden markov models. _arXiv preprint arXiv:2411.01558_ , 2024. 

22 

A Review and Comparative Analysis of Univariate Conformal Regression Methods 

- Lingxuan Tang, Rui Luo, Zhixin Zhou, and Nicolo Colombo. Enhanced route planning with calibrated uncertainty set. _Machine Learning_ , 114(5):1–16, 2025. 

- Lars van der Laan and Ahmed M Alaa. Self-calibrating conformal prediction. _arXiv preprint arXiv:2402.07307_ , 2024. 

- Janette Vazquez and Julio C Facelli. Conformal prediction in clinical medical sciences. _Journal of Healthcare Informatics Research_ , 6(3):241–252, 2022. 

- Vladimir Vovk. Cross-conformal predictors. _Annals of Mathematics and Artificial Intelligence_ , 74: 9–28, 2015. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ , volume 29. Springer, 2005. 

- Vladimir Vovk, Ilia Nouretdinov, and Alex Gammerman. On-line predictive linear regression. _The Annals of Statistics_ , pages 1566–1590, 2009. 

- Vladimir Vovk, Ivan Petej, Paolo Toccaceli, Alexander Gammerman, Ernst Ahlberg, and Lars Carlsson. Conformal calibrators. In _conformal and probabilistic prediction and applications_ , pages 84–99. PMLR, 2020. 

- Volodya Vovk, Alexander Gammerman, and Craig Saunders. Machine-learning applications of algorithmic randomness. _In International Conference on Machine Learning_ , 1999. 

- Ting Wang, Zhixin Zhou, and Rui Luo. Enhancing trustworthiness of graph neural networks with rank-based conformal training. _Proceedings of the AAAI Conference on Artificial Intelligence_ , 39(20):21261–21268, 2025. 

- Jerzy Wieczorek. Design-based conformal prediction. _arXiv preprint arXiv:2303.01422_ , 2023. 

- Margaux Zaffran, Aymeric Dieuleveut, Julie Josse, and Yaniv Romano. Conformal prediction with missing values. In _International Conference on Machine Learning_ , pages 40578–40604. PMLR, 2023. 

- Zheng Zhang, Jie Bao, Zhixin Zhou, Nicolo Colombo, Lixin Cheng, and Rui Luo. Residual reweighted conformal prediction for graph neural networks. In _Proceedings of the 41st Conference on Uncertainty in Artificial Intelligence (UAI)_ , 2025. to appear. 

23 

