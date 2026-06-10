Proceedings of Machine Learning Research 266:1–20, 2025 Conformal and Probabilistic Prediction with Applications 

## **High Probability Risk Control Under Covariate Shift** 

**Duarte C. Almeida** duartecaladoalmeida@tecnico.ulisboa.pt 

_Instituto Superior T´ecnico, Universidade de Lisboa Instituto de Telecomunica¸c˜oes Feedzai_ 

**Jo˜ao Bravo** _Feedzai_ 

joao.bravo@feedzai.com 

**Jacopo Bono** jacopo.bono@feedzai.com _Feedzai_ **Pedro Bizarro** pedro.bizarro@feedzai.com _Feedzai_ **M´ario A. T. Figueiredo** mario.figueiredo@tecnico.ulisboa.pt _Instituto Superior T´ecnico, Universidade de Lisboa Instituto de Telecomunica¸c˜oes_ 

jacopo.bono@feedzai.com 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

Distribution-free uncertainty quantification is an emerging field, which encompasses risk control techniques in finite sample settings with minimal distributional assumptions, making it suitable for high-stakes applications. In particular, high-probability risk control methods, namely the _learn then test_ (LTT) framework, use a calibration set to control multiple risks with high confidence. However, these methods rely on the assumption that the calibration and target distributions are identical, which can pose challenges, for example, when controlling label-dependent risks under the absence of labeled target data. In this work, we propose a novel extension of LTT that handles covariate shifts by directly weighting calibration losses with importance weights. We validate our method on a synthetic fraud detection task, aiming to control the false positive rate while minimizing false negatives, and on an image classification task, to control the miscoverage of a set predictor while minimizing the average set size. The results show that our approach consistently yields less conservative risk control than existing baselines based on rejection sampling, which results in overall lower false negative rates and smaller prediction sets. **Keywords:** High-probability risk control, covariate shift, learn then test, distribution-free uncertainty quantification, conformal prediction. 

## **1. Introduction** 

Machine learning is increasingly used to automate high-risk and high-stakes decisions ( _e.g._ , in healthcare or finance). These decisions are often associated with specific risks representing statistical measures of inaccuracy that must be controlled to meet safety, regulatory, quality, or other standards. For example, fraud detection systems should be properly tuned to detect fraudulent transactions while avoiding hindering legitimate economic activity. 

Distribution-free uncertainty quantification is an emerging field that encompasses risk control techniques in finite sample settings with minimal distributional assumptions (Angelopoulos and Bates, 2023). A cornerstone method of this family is _conformal prediction_ 

© 2025 D.C. Almeida, J. Bravo, J. Bono, P. Bizarro & M.A.T. Figueiredo. 

Almeida Bravo Bono Bizarro Figueiredo 

(CP) (Shafer and Vovk, 2008), which calibrates a set predictor to control the miscoverage probability. Letting _X_ and _Y_ denote the feature and label spaces, respectively, CP uses a calibration set _D_ = _{_ ( _Xi, Yi_ ) _}[n] i_ =1 _[⊂X][×][Y]_[to][generate][prediction][sets] _[C]_[(] _[X][n]_[+1][)] for a new test data point ( _Xn_ +1 _, Yn_ +1). Assuming only exchangeability of _{_ ( _Xi, Yi_ ) _}[n] i_ =1[+1] (its joint distribution is permutation-invariant), CP provides a _coverage_ / _validity_ guarantee: P( _Yn_ +1 _∈C_ ( _Xn_ +1)) _≥_ 1 _− α_ . However, CP does not guarantee the stronger _conditional validity_ property P( _Yn_ +1 _∈C_ ( _Xn_ +1) _| Xn_ +1 = _x_ ) _≥_ 1 _− α, ∀x ∈X_ . While this property cannot be attained in general, relaxations such as group-conditional and class-conditional coverage offer guarantees within specific feature-label subsets (Barber et al., 2021; Gibbs et al., 2025) . Furthermore, _calibration-set validity_ is always achievable, as concentration bounds for the calibration-set conditional coverage level exist (Vovk, 2012). 

Under the same exchangeability assumption, CP can be generalized to control other risks beyond miscoverage, via the calibration of some (possibly multidimensional) parameter _λ_ . If the risk can be expressed as the expectation of a lower-bounded loss function _L_ ( _·, ·_ ; _λ_ ) : _X × Y →_ R, which is coordinate-wise non-increasing with respect to _λ_ for all ( _x, y_ ) _∈X × Y_ , _conformal risk control_ (CRC) can be applied to compute _λ_[ˆ] that guarantees E[ _L_ ( _Xn_ +1 _, Yn_ +1; _λ_[ˆ] )] _≤ α_ (Angelopoulos et al., 2024). 

The probability and expectation in the aforementioned guarantees are taken over both the new test point and the calibration set. To rigorously control the risk, the calibration procedure must be applied each time a new test point is introduced. If calibration is only done periodically, there may be time frames where the risk exceeds the desired threshold due to an anomalous calibration sample, which could be problematic in scenarios where risk control should be as strict as possible. An alternative approach is to perform _high-probability risk control_ (HPRC) (Angelopoulos et al., 2025; Bates et al., 2021), which bounds the probability of risk violations occurring due to a “bad” calibration set below some threshold _δ_ . Methods for this purpose operate under slightly stronger distributional assumptions, namely, that the calibration set is i.i.d. according to the target distribution. 

When models are deployed over data from a _target_ distribution that may differ from that of the training data (the _source_ distribution), a significant performance degradation may occur (Kouw and Loog, 2019). This is the case _, e.g.,_ when a fraud detection system is applied to transactions from a new geographical setting, or if an image classifier trained on a particular type of image ( _e.g._ , photographs) is used on other kinds of image ( _e.g._ , drawings). Furthermore, the risk control techniques mentioned above cannot be applied over source calibration data, as distribution shifts violate important underlying assumptions (e.g., exchangeability and i.i.d.). While labeled target data are often unavailable, due to slow or costly labeling processes, unlabeled target data could still be used for risk control. 

In this work, we introduce a novel adaptation of high-probability risk control methods, specifically of the _learn then test_ (LTT) approach (Angelopoulos et al., 2025), that addresses covariate shift between the source and target distributions in the presence of unlabeled target data. Making use of recent advancements in hypothesis testing, we prove how calibration losses can be weighted by importance weights to achieve risk control. We experimentally validate our approach in two settings. The first is a synthetic fraud detection scenario in which a model trained on a source distribution is calibrated to control the false positive rate (FPR) on a target distribution while minimizing the false negative rate (FNR). The second setting involves an image classification task, where a model trained on 

2 

High Probability Risk Control Under Covariate Shift 

a source distribution is deployed on a target domain representing a specific data subpopulation. Here, the covariate shift assumption may not hold, and the goal is to calibrate a set predictor to control the miscoverage probability while minimizing the average set size, as considered by Park et al. (2022). Our results show that our approach is less conservative than the existing covariate shift-adapted HPRC baseline in both cases (i.e., smaller FNR and average set size), while achieving the desired risk control in the synthetic setting and closing the risk gap in the second scenario. 

**Related Work.** This work is part of a broader research avenue aimed at adapting risk control methods to handle distribution shifts. Notably, Tibshirani et al. (2019) proposed a weighting scheme for quantile calculation in CP that uses importance weights to preserve the original coverage guarantee under covariate shift. Barber et al. (2023) examined the impact of both data-independent and dependent weighting schemes on the coverage gap, providing important theoretical guidelines for designing such schemes to bridge the gap under arbitrary violations of the exchangeability assumption. This approach has been extended to conformal risk control by Farinhas et al. (2024). In the context of high-probability risk control, Park et al. (2022) introduced rejection sampling to align the calibration and target distributions under covariate shift while aiming specifically for the control of the miscoverage risk. This approach was later extended to other use cases by Zollo et al. (2024); although different from our method, it will be fully explained in later sections for completeness. 

## **2. Background: High-Probability Risk Control** 

In this section, we present a review of some foundational principles of HPRC. Let _X_ and _Y_ denote the feature and label spaces, respectively, and let P be a probability measure on a suitable measurable space ( _X × Y, F_ ). For convenience, we will also use the notation P to refer to the corresponding distribution. Furthermore, consider a calibration set _D_ = _{_ ( _Xi, Yi_ ) _}[n] i_ =1 _[⊂X][× Y]_[,][where][(] _[X][i][, Y][i]_[)][i.i.d.] _∼_ P _, ∀i ∈{_ 1 _, . . . , n}_ . Let _L_ ( _·, ·_ ; _λ_ ) : _X × Y →_ R be a measurable loss parameterized by _λ_ , and define _R_ P( _λ_ ) = E( _X,Y_ ) _∼_ P[ _L_ ( _X, Y_ ; _λ_ )] as the risk (expected loss) under P. For conciseness, we include the subscript P in the expectation defining the risk only when the underlying probability measure is not clear from the context. 

A core HPRC approach is _learn then test_ (LTT) (Angelopoulos et al., 2025). Given a predefined subset Λ of the parameter space, LTT uses a calibration set to generate a subset ˆΛ _⊆_ Λ such that the risk is uniformly controlled over all its elements, i.e., 


![](markdown_output/almeida25a_images/almeida25a.pdf-0003-06.png)


for some confidence level _δ ∈_ (0 _,_ 1), where the randomness is over the calibration set. Once ˆΛ is determined, a single parameter can be selected based on additional optimality criteria. For instance, in general detection (binary classification) systems, one might control the false positive rate and select the parameter in Λ[ˆ] that minimizes the false negative rate (or vice versa). Moreover, this approach does not require the risk or loss to be monotonic with respect to _λ_ , which may even be any general mathematical object. 

Hypothesis tests serve as the main building blocks of this procedure; specifically, for each value of _λ ∈_ Λ, the following null hypothesis is considered: 


![](markdown_output/almeida25a_images/almeida25a.pdf-0003-09.png)


3 

Almeida Bravo Bono Bizarro Figueiredo 

If a rejection rule over the calibration set bounds the probability of a false rejection below 1 _− δ_ , then rejecting the null hypothesis based on it provides 1 _− δ_ confidence that _λ_ controls the risk below _α_ . Such procedures can be designed using valid p-values. 

**Definition 1 (p-value)** _(Angelopoulos et al., 2025) Let H_ 0 _be a null hypothesis. A statistic p is said to be a valid p-value for H_ 0 _if it is super-uniform under H_ 0 _, i.e.,_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0004-03.png)


_Thus, rejecting H_ 0 _if p ≤ δ ensures that a false rejection occurs with probability at most δ._ 

The following theorem establishes how to generate p-values from concentration inequalities (such as Hoeffding’s inequality). 

**Theorem 2** _(Bates et al., 2021) Let g_ ( _·, ·_ ) : R[2] _→_ R _be a function satisfying the condition_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0004-07.png)


_where R_[ˆ] ( _λ_ ) = _n_[1] � _ni_ =1 _[L]_[(] _[X][i][, Y][i]_[;] _[ λ]_[)] _[represents][the][empirical]_ ˆ _[risk][over][the][calibration][set][and]_ E[ _L_ ( _Xi, Yi_ ; _λ_ )] = _R_ ( _λ_ ) _, ∀i ∈{_ 1 _, . . . , n}. Then, g_ � _R_ ( _λ_ ) _, α_ � _is a valid p-value for the null hypothesis H_ 0( _λ, α_ ) : _R_ ( _λ_ ) _> α._ 

In some cases, the distribution of the empirical risk can be exactly specified, making it possible to replace potentially loose non-parametric bounds with an exact expression on the r.h.s. of Equation (1), leading to more powerful p-values. For instance, if the loss function is almost surely supported on _{_ 0 _,_ 1 _}_ , then _nR_[ˆ] ( _λ_ ) follows a binomial distribution. The 0-1 loss scenario is ubiquitous, arising when controlling the miscoverage or the FPR. 

**Theorem 3 (Clopper-Pearson p-value)** _(Clopper and Pearson, 1934; Park et al., 2022) LetR_ ˆ( _λ_ ) _L_ (= _·, ·n_ ;1 _λ_ �) _ni_ :=1 _X[L]_[(] _×[X][i] Y[, Y][i] →{_[;] _[ λ]_[)] 0 _[be] ,_ 1 _[the] } be[empirical] a measurable[risk][computed] loss function[over] parametrized[an][i.i.d.][calibration] by λ. Let[set] such that_ E[ _L_ ( _Xi, Yi_ ; _λ_ )] = _R_ ( _λ_ ) _, ∀i ∈{_ 1 _, . . . , n}. Then, the statistic_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0004-11.png)


_where F_ Bin( _n,α_ ) _is the cumulative distribution function of the binomial distribution with n trials and success probability α, is a valid p-value for H_ 0( _λ, α_ ) : _R_ ( _λ_ ) _> α._ 

Obtaining Λ[ˆ] requires ensuring that all its elements control the risk below _α_ with 1 _− δ_ confidence, rather than being (1 _− δ_ )-confident for each _λ ∈_ Λ.[ˆ] In hypothesis testing terminology, this is referred to as controlling the _family-wise error rate_ (FWER) (Angelopoulos et al., 2025) at level _δ_ , which is defined as 


![](markdown_output/almeida25a_images/almeida25a.pdf-0004-14.png)


Such approaches are called FWER-controlling and consist of strategies to aggregate p-values generated by testing the set of hypotheses _{H_ 0( _λ, α_ ) : _λ ∈_ Λ _}_ . If Λ is discrete, one possible approach is _fixed-sequence testing_ (FST) (Angelopoulos et al., 2025). In FST, hypotheses 

4 

High Probability Risk Control Under Covariate Shift 

are tested in a predefined order, and all corresponding values of _λ_ in Λ[ˆ] are gathered until the first non-rejection at level _δ_ occurs. The risk-controlling subset is thus defined by ˆΛ = _{λ[′] i[}][k] i_ =1 _[∗][−]_[1][,][where] 


![](markdown_output/almeida25a_images/almeida25a.pdf-0005-02.png)


for a predefined ordering ( _λ[′]_ 1 _[, ...λ][′] |_ Λ _|_[)][of][Λ.][For][this][method][to][be][useful,][safer][values][for] _[λ]_ should be tested first. When the monotonicity relationship between _λ_ and _R_ ( _λ_ ) is unclear, _split fixed-sequence testing_ (SFST) (Angelopoulos et al., 2025; Laufer-Goldshtein et al., 2023) can be used. In this approach, the calibration set is divided into two disjoint subsets: one for defining an ordering of Λ and another for applying FST. 

LTT can also be extended to simultaneously control multiple risks by considering a p- value for each individual risk and taking the maximum of all p-values. Additionally, when p-values are almost surely monotonically non-increasing or non-decreasing in _λ_ for a fixed calibration set _D_ , it is possible to consider an interval [ _λ−, λ_ +] as Λ. In this case, the iterative nature of FST/SFST can be avoided by directly computing the risk-controlling half-subset Λ[ˆ] using any standard root-finding algorithm (Bates et al., 2021). 

## **3. High-Probability Risk Control under Covariate Shift** 

Consider the problem of asserting risk control over a target distribution Ptarget, from which only an _unlabeled_ sample _T_ = _{Xi}[n] i_ =1 _[t]_[is available.][Standard risk control methods generally] cannot be applied in this setting if the loss function depends on the label _Y_ , as it usually does. If we possess a _labeled_ sample _S_ = _{_ ( _Xi, Yi_ ) _}[n] i_ =1 _[s]_[drawn][from][a][possibly][different] source distribution Psource, we should ask if the application of these methods on _S_ yields the desired statistical confidence guarantees. 

To test _H_ 0( _λ, α_ ) : _R_ ( _λ_ ) _> α_ at a significance level _δ_ , a general strategy is to use p-values, which require that E[ _L_ ( _Xi, Yi_ ; _λ_ )] = _R_ ( _λ_ ) for any data point ( _Xi, Yi_ ) in the calibration set. Therefore, without further assumptions, we are only guaranteed to control the source risk 


![](markdown_output/almeida25a_images/almeida25a.pdf-0005-08.png)


For the risk to be controlled over the target distribution, the relation _R_ Ptarget( _λ_ ) _≤ R_ Psource( _λ_ ) should hold, which is a strong assumption that may not be verified in general. 

## **3.1. The Covariate Shift Assumption and Existing HPRC Methods** 

Fortunately, it is possible to make use of the source dataset _S_ under some further assumptions on Psource and Ptarget. In particular, the _covariate shift_ assumption renders this problem tractable by assuming equal feature-conditional probability measures. 

**Definition 4 (Covariate shift)** _(Qui˜noreo-Candela et al., 2009) Two probability measures_ P _and_ Q _defined on some measurable space_ ( _X ×Y, F_ ) _are said to differ by a covariate shift if the corresponding feature-conditional probability measures coincide, i.e.,_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0005-13.png)


Furthermore, under mild regularity conditions, we can define the notion of importance weight between two probability measures (also known as the Radon-Nikodym derivative). 

5 

Almeida Bravo Bono Bizarro Figueiredo 

**Definition 5 (Importance weight)** _(Resnick, 1999) Let_ P _and_ Q _be probability measures defined on a measurable space_ ( _X × Y, F_ ) _such that_ Q _is absolutely continuous with respect to_ P (Q _≪_ P) _, i.e.,_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0006-02.png)


_Define the importance weight function as_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0006-04.png)


_Then, it holds that_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0006-06.png)


Under the covariate shift assumption, the importance weight function depends only on the marginal distributions over _X_ (Yu and Szepesv´ari, 2012), 


![](markdown_output/almeida25a_images/almeida25a.pdf-0006-08.png)


where Psource _,X_ and Ptarget _,X_ denote the induced source and target marginals over _X_ . Moreover, the importance weight can be estimated only from unlabeled source target data several well-established methods (You et al., 2019; Sugiyama et al., 2007; Huang et al., 2006). 

To correct covariate shift between the source and target distributions, Park et al. (2022) propose aligning the calibration set with the target distribution via _rejection sampling_ (Robert and Casella, 2004), a classical technique to generate samples from a _target_ distribution using another (so-called _proposal_ ) distribution. The definition and correctness of this procedure are established by the following theorem. 

**Theorem 6 (Rejection Sampling)** _(Robert and Casella, 2004) Let_ P _and_ Q _be the target and proposal, respectively, probability measures defined on a measurable space_ ( _X × Y, F_ ) _such that_ Q _≪_ P _. Define w_ = _[d] d_[Q] P _[as][the][corresponding][importance][weight][function,][assumed] to be bounded above by some constant B < ∞. Let_ ( _X, Y_ ) _∼_ P _, and define_ ( _X[′] , Y[′]_ ) _as the pair_ ( _X, Y_ ) _accepted under the event U ≤ w_ ( _X, Y_ ) _/B, where U ∼ Uniform_ [0 _,_ 1] _is independent of_ ( _X, Y_ ) _; that is,_ ( _X[′] , Y[′]_ ) = ( _X, Y_ ) _| w_ ( _X_ ) _/B ≤ U . Then,_ ( _X[′] , Y[′]_ ) _∼_ Q _._ Given an importance weight function _w_ : _X →_ R and an upper bound _B ≥_ sup _{w_ ( _x_ ) _, x ∈ X}_ , both estimated from unlabeled source and target data, rejection sampling can be applied to the labeled source set _S_ to produce a new i.i.d. sample _S[′]_ from Ptarget, assuming these estimates are accurate. This allows the application of standard risk control procedures as if _S[′]_ was directly drawn from the target distribution. 

Applying rejection sampling as described, the expected size of _S[′]_ (the set of non-rejected samples) is inversely proportional to _B_ , since 


![](markdown_output/almeida25a_images/almeida25a.pdf-0006-13.png)


where **1** _{·}_ denotes the indicator function. If _B_ is large, the retained sample may become too small, yielding overly conservative p-values that fail to identify useful risk-controlling values of _λ_ . This can degrade performance with respect to complementary metrics; for instance, a low FPR may come at the cost of a higher false negative rate and vice versa. 

6 

High Probability Risk Control Under Covariate Shift 

## **3.2. HPRC under Covariate Shift via Importance Weighting** 

In this section, we propose a different approach to HPRC under covariate shift, addressing the limitations of rejection sampling. We discuss a new method to control risks over the joint distribution (Section 3.2.1) and extend it to conditional risks (Section 3.2.2). 

## 3.2.1. Controlling Risks over the Joint Feature/Label Distribution 

We first propose an alternative way to deal with covariate shift when controlling risks that are the expectation of a loss _L_ ( _X, Y_ ; _λ_ ) over the joint feature and label distribution induced by Ptarget (e.g., miscoverage). In such cases, these can be written as expectations of the importance-weighted loss _w_ ( _X_ ) _L_ ( _X, Y_ ; _λ_ ) over Psource (Qui˜noreo-Candela et al., 2009): 


![](markdown_output/almeida25a_images/almeida25a.pdf-0007-05.png)


In this way, we can perform risk control using the _entirety_ of the labeled source data by considering the sample of importance-weighted losses _{w_ ( _Xi_ ) _L_ ( _Xi, Yi_ ; _λ_ ) _}[n] i_ =1 _[s]_[,][where] ( _Xi, Yi_ ) _∼_ Psource _, ∀i ∈_ [ _ns_ ]. We formalize this approach in the next theorem. 

**Theorem 7** _Let_ P _source and_ P _target be probability measures on_ ( _X ×Y, F_ ) _such that_ P _target ≪_ P _source, and assume they differ by a covariate shift. Let w_ = _d[d]_ P[P] _source[tar][g][et][be][the][corresponding] importance weight function, and let L_ ( _·, ·_ ; _λ_ ) : _X ×Y →_ R _be a measurable loss parametrized by λ. Then, any p-value for H_ 0 _[′]_[(] _[λ, α]_[)][:][E][P] _source_[[] _[w]_[(] _[X]_[)] _[L]_[(] _[X, Y]_[ ;] _[ λ]_[)]] _[>][α][is][also][a][p-value][for] H_ 0( _λ, α_ ) : EP _target_ [ _L_ ( _X, Y_ ; _λ_ )] _> α._ 

**Proof** By Equation (2), the conditions in _H_ 0( _λ, α_ ) and _H_ 0 _[′]_[(] _[λ, α]_[)][are][equivalent.][Thus,][for] any valid p-value _p_ ( _λ, α_ ) for _H_ 0 _[′]_[(] _[λ, α]_[),][we][have][P] _H_ 0( _λ,α_ )[(] _[p]_[(] _[λ, α]_[)] _[≤][δ]_[)][=][P] _H_ 0 _[′]_[(] _[λ,α]_[)][(] _[p]_[(] _[λ, α]_[)] _[≤] δ_ ) _≤ δ, ∀δ ∈_ [0 _,_ 1] _._ 

It is important to recognize that, while this method retains all the source data, the distribution of the weighted losses may be more challenging to handle. For instance, the introduction of weights can destroy desirable properties of the original loss that allow the use of very tight p-values—e.g., it may break the 0–1 structure and significantly broaden the range of possible values. Nevertheless, recent advances in testing by betting provide highly variance-adaptive p-values that work very well in practice, such as the WaudbySmith–Ramdas (WSR) p-value (Waudby-Smith and Ramdas, 2024). 

**Theorem 8 (WSR p-value)** _(Bates et al., 2021; Waudby-Smith and Ramdas, 2024) Let L_ ( _·, ·_ ; _λ_ ) : _X × Y →_ [0 _,_ 1] _be a measurable loss parametrized by λ and let D_ = _{_ ( _Xi, Yi_ ) _}[n] i_ =1 _be a calibration set such that_ 

E[ _L_ ( _Xi, Yi_ ; _λ_ )] = E[ _L_ ( _Xi, Yi_ ; _λ_ ) _| L_ ( _Xi−_ 1 _, Yi−_ 1; _λ_ ) _, . . . , L_ ( _X_ 1 _, Y_ 1; _λ_ )] = _R_ ( _λ_ ) _, ∀i ∈{_ 1 _, . . . , n}._ 

_Define the following statistics:_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0007-13.png)


7 

Almeida Bravo Bono Bizarro Figueiredo 

_Furthermore, define the capital process {Ki_ ( _λ, α_ ) _}[n] i_ =1 _[as]_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0008-02.png)


_Then, the statistic_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0008-04.png)


_is a p-value for H_ 0( _λ, α_ ) : _R_ ( _λ_ ) _> α._ 

Although this p-value assumes that the loss lies between 0 and 1, it can be readily extended to our setting. If _L_ is supported on [ _l, u_ ], then the importance-weighted loss _wL_ is supported on [ _l[′] , u[′]_ ], where _l[′]_ = min(0 _, Bl_ ) and _u[′]_ = max(0 _, Bu_ ). It is then sufficient to test the equivalent hypothesis 


![](markdown_output/almeida25a_images/almeida25a.pdf-0008-07.png)


Due to the sequential nature of the procedure, the order of the calibration data can affect the outcome when the source dataset is a mixture of subsources (e.g., different types of images). If such subsources are processed in bulk and the early part of the capital process is computed over samples from a subsource for which the risk is controlled, the capital process may surpass _δ[−]_[1] prematurely, leading to a rejection even though the risk is _not_ controlled over the entire source distribution. To solve this, the data can be randomized _B B_ times, yielding _B_ capital processes � _{Ki_[(] _[b]_[)][(] _[λ, α]_[)] _[}] i[n]_ =1� _b_ =1[,][which][can][be][averaged][into][a] new process _Ki_ ( _λ, α_ ) := _B[−]_[1][ �] _[B] b_ =1 _[K] i_[(] _[b]_[)][(] _[λ, α]_[)][(][Waudby-Smith][and][Ramdas][,][2024][).] 

## 3.2.2. Controlling Conditional Risks 

Many risks are defined over distributions other than the joint feature and label distribution. For example, the FPR of a binary classifier _f_ , FPR = P( _f_ ( _X_ ) = 1 _| Y_ = 0) = E[ **1** _{f_ ( _X_ ) = 1 _} | Y_ = 0], is evaluated over the conditional distribution of _X_ given _Y_ = 0. Under covariate shift between Psource and Ptarget, it follows that 


![](markdown_output/almeida25a_images/almeida25a.pdf-0008-11.png)


showing that covariate shift does not hold if the source and target class priors are different. In general, this reweighting procedure does not directly apply to risks defined over distributions other than the joint. However, it can be adapted for a broad class of risks, as shown in the following theorem. 

**Theorem 9** _Consider the null hypothesis H_ 0( _λ, α_ ) : EP _target_ [ _L_ ( _X, Y_ ; _λ_ ) _|_ ( _X, Y_ ) _∈A_ ( _λ_ )] _> α, where A_ ( _λ_ ) _∈X ×Y is a non-zero probability set and L_ ( _·, ·_ ; _λ_ ) : _X ×Y →_ R _is a measurable loss parametrized by λ. Then, any p-value for H_ 0 _[′]_[(] _[λ, α]_[)][:][E][P] _source_[[] _[L][′]_[(] _[X, Y]_[ ;] _[ λ]_[)]] _[>][α][is][also][a] p-value for H_ 0( _λ, α_ ) _, where_ 


![](markdown_output/almeida25a_images/almeida25a.pdf-0008-14.png)


8 

High Probability Risk Control Under Covariate Shift 

**Proof** Developing the condition in _H_ 0( _λ, α_ ), we have: 


![](markdown_output/almeida25a_images/almeida25a.pdf-0009-02.png)


The result then follows from applying Theorem 7 to the loss _L_ ( _X, Y_ ; _λ_ ) **1** _{_ ( _X, Y_ ) _∈ A_ ( _λ_ ) _}_ + _α_ **1** _{_ ( _X, Y_ ) _∈A/_ ( _λ_ ) _}_ . 

This result shows that any conditional risk can be reformulated as a risk over the joint feature-label distribution for the purpose of hypothesis testing. In the setting of a binary classifier _f_ ( _·_ ; _λ_ ) : _X →{_ 0 _,_ 1 _}_ , many common classification risks fall within this family. For instance, the FPR corresponds to taking _L_ ( _X, Y_ ; _λ_ ) = **1** _{f_ ( _X_ ; _λ_ ) = 1 _}_ and _A_ ( _λ_ ) = _{_ ( _x, y_ ) _∈ X × Y_ : _y_ = 0 _}_ . Similarly, for the false discovery rate, we have _L_ ( _X, Y_ ; _λ_ ) = **1** _{Y_ = 0 _}_ and _A_ ( _λ_ ) = _{_ ( _x, y_ ) _∈X × Y_ : _f_ ( _x_ ; _λ_ ) = 1 _}_ . 

## **4. Results and Discussion** 

## **4.1. Experimental Setup** 

## 4.1.1. Tasks and Datasets 

We evaluate our method on two tasks. The first consists in controlling the FPR of a transaction fraud detection model below _α_ = 0 _._ 05 with confidence (1 _− δ_ ) = 0 _._ 95. The model has the form _f_ ( _x_ ; _λ_ ) = **1** _{s_ ( _x_ ) _> λ}_ , where _s_ : _X →_ [0 _,_ 1] is a trained score function that captures the likelihood of a transaction being fraudulent. We apply _fixed sequence testing_ (FST) over a set Λ = _{s_ ( _i/_ 1000) _}_[1000] _i_ =1[,][where] _[s]_[(] _[q]_[)][denotes][the][sample] _[q]_[-quantile][of][the] score distribution on source data. We test Λ in decreasing order and choose the smallest risk-controlling _λ_ to minimize the FNR. 

In this first task, we simulate a situation in which new unlabeled transaction data becomes available and previously collected labeled data are used to ensure risk control. For that purpose, we partition the Bank Account Fraud (BAF) dataset (Jesus et al., 2022) into three domains based on the credit risk of the client performing the transaction ( `low` , `medium` , and `high` ). Each domain is treated as the target in turn, with the remaining two combined to form the source. All domains are designed to differ solely in terms of covariate shift. Details on the partitioning procedure are provided in Appendix A. Furthermore, we use 70% of each domain’s data for model training and the remaining 30% for risk control. We use LightGBM classifiers (Ke et al., 2017), trained with 5-fold cross-validation, and tune hyperparameters to maximize the AUROC using Optuna’s implementation of TPE (Watanabe, 2023; Akiba et al., 2019). The hyperparameter grid is specified in Appendix F. 

In the second task, we control the miscoverage of an image set predictor of the form _f_ ( _x_ ; _λ_ ) = _{y ∈Y_ : _s_ ( _x, y_ ) _> λ}_ below 0.10 with confidence 0.95, where _s_ : _X × Y →_ [0 _,_ 1] is a trained score function such that _s_ ( _x, y_ ) estimates the posterior probability of class _y_ for an image _x_ . We perform FST over Λ = _{s[∗]_ ( _i/_ 1000) _[}] i_[1000] =1[,][where] _[s][∗]_ ( _q_ )[denotes][the][empirical] 

9 

Almeida Bravo Bono Bizarro Figueiredo 

_q_ -quantile of the true-class scores on the source data. Here, Λ is tested in increasing order and the largest risk-controlling _λ ∈_ Λ is selected to minimize the average set size. 

We use the DomainNet dataset (Peng et al., 2019), which consists of 6 domains: `clipart` , `real` , `infograph` , `painting` , `sketch` , and `quickdraw` . We consider each domain as target and _all_ domains as sources, simulating a setting where a model is trained on broad data but is deployed on some (potentially unknown) subpopulation. We use the same ResNet model as Park et al. (2022) and use the original test and validation splits for risk control. 

## 4.1.2. Estimation of Importance Weights 

To estimate importance weights, we apply _kernel mean matching_ (KMM), which minimizes the _maximum mean discrepancy_ (MMD) between empirical kernel mean embeddings of the target distribution and the reweighted source distribution (Qui˜noreo-Candela et al., 2009). Given a _reproducing kernel Hilbert space_ (RKHS) _H_ associated with a universal kernel _k_ , KMM estimates the weights at the source datapoints _{w_ ( _xj_ ) : _xj ∈S}_ that minimize 


![](markdown_output/almeida25a_images/almeida25a.pdf-0010-05.png)


subject to _w_ ( _xj_ ) _≥_ 0 _, ∀xj ∈S_ , and _| n_[1] _s_ � _xj ∈S[w]_[(] _[x][j]_[)] _[−]_[1] _[| ≤][ϵ]_[.][Following][ Huang et al.][ (][2006][),] we set _ϵ_ = 1 _−_ 1 _/[√] ns_ . We consider a Gaussian kernel _k_ ( _x, x[′]_ ) = exp( _−∥x − x[′] ∥_[2] _/σ_[2] ), using one-hot encodings for categorical variables when computing distances. We set _σ_ to the median of pairwise distances between all the points in the source and target datasets, following Sugiyama et al. (2009). Additionally, the maximum admissible importance weight is set at 10,000. To accelerate this procedure, we use the _very fast_ KMM (VFKMM) algorithm proposed by Chandra et al. (2016), averaging importance weights computed across bootstrap samples of size 1000 from the source dataset, with the number of bootstrap samples set to ensure that each point is sampled at least once with probability 0.9999. Moreover, we consider the maximum estimated importance weight as an estimate for the upper bound _B_ . The second image classification task poses challenges due to the high dimensionality of the input, affecting the stability of importance weight estimates and increasing runtime. These challenges can be attenuated by considering a lower-dimensional feature transformation _h_ : R _[n] →_ R _[d]_ with _d ≪ n_ , such that _X_ and _Y_ are conditionally independent given _h_ ( _X_ ). One such transformation is _h_ ( _x_ ) = (P( _Y_ = _y_ 1 _| X_ = _x_ ) _, . . . ,_ P( _Y_ = _yd | X_ = _x_ )), where _Y_ = _{y_ 1 _, . . . , yd}_ is the label space (Stojanov et al., 2019). This motivates our choice to use the model’s predicted class scores as features for importance weight computation. 

Park et al. (2022) propose a method to account for uncertainty in the estimation of importance weights. In short, the observations are binned into _K_ equal-mass bins _{Bi}[K] i_ =1 according to an estimate of the importance weights. Then, a _δ_ -upper confidence bound 


![](markdown_output/almeida25a_images/almeida25a.pdf-0010-08.png)


can be obtained for _w_ ( _x_ ), where _B_ ( _x_ ) is the bin containing _x_ , P[+] and P _[−]_ denote _δ/_ 2 Clopper-Pearson upper and lower-confidence bounds, respectively, and _E_ is a predefined 

10 

High Probability Risk Control Under Covariate Shift 

smoothness constant to account for the histogram approximation. However, there are no theoretical guidelines for choosing _K_ and _E_ . Thus, we opt for more established procedures and proceed under the assumption that the estimates are accurate. 

## 4.1.3. Baselines and Evaluation Procedure 

We compare our proposed importance-weighted LTT method based on the WSR p-value (Waudby-Smith and Ramdas, 2024) (LTT-IW) against two baselines: LTT with rejection sampling and the Clopper-Pearson p-value (Clopper and Pearson, 1934) (LTT-RS), and LTT without importance weights (LTT) (i.e., directly controlling the source risk). Variations of our method for different p-values can be found in Appendix B. 

At the beginning of the procedure, we estimate the importance weights using the source and target splits allocated for risk control. We then run 1,000 iterations of LTT, each time over a different subsample of source data drawn without replacement. In the first task, we use the entire target dataset to evaluate the resulting target risk, while in the second baseline (where the target domain is contained in the source domain), we only use the part that was not sampled. To evaluate sample efficiency, we vary the source sample size, but always use the full source and target datasets to get the most accurate importance weight estimates. Finally, we estimate (1 _− δ_ )-quantiles of the risk estimates computed over all iterations to assess if risk control is achieved. To evaluate how conservative the methods are, we also report the mean FNR and average set size obtained over all runs. In addition, Appendix C contains a brief analysis of the computational cost of the proposed method. 

## **4.2. Results** 

Figure 1 reports the 0.95-quantile of the FPR for different values of the source sample size _N_ . Ignoring covariate shift (LTT) can either make risk control overly conservative (for target domains `low` and `medium` ), or outright invalid, as is the case of target domain `high` , where the risk is controlled at twice the intended level. Both weighted variants (LTT-IW and LTT-RS) control the FPR in nearly all cases, with the exception being in `medium` , where a residual risk gap of _≈_ 0.0025 likely stems from errors in the estimated importance weights. Figure 2 further indicates that LTT-IW consistently achieves a lower average FNR than LTT-RS, showing that our method of direct importance weighting yields a less conservative and more stable risk control than rejection sampling in this case. 

We perform a similar analysis for the second task. Figure 3 shows that the risk is only controlled when `real` or `quickdraw` serve as the target, indicating that the covariate-shift assumption does not hold. In fact, we are actually controlling the risk over a distribution Paligned that matches the target feature marginal, but maintains the source featureconditional distribution of the labels. With high probability, the true target risk can exceed _α_ by at most the total-variation distance _d_ TV�Ptarget _,_ Paligned� (Angelopoulos et al., 2024). 

Nevertheless, we see that using importance weights (LTT-IW and LTT-RS) can bring the effective risk level closer to _α_ : for the `clipart` , `infograph` , `painting` , and `sketch` cases, it bridges the risk gap, while making the procedure less conservative for `quickdraw` . In the `real` domain, however, the effect is minimal for LTT-IW, and LTT-RS deviates further from the target level. While both methods perform comparably on miscoverage, our method (LTT-IW) yields smaller average set sizes compared to LTT-RS (Figure 4). We 

11 

Almeida Bravo Bono Bizarro Figueiredo 


![](markdown_output/almeida25a_images/almeida25a.pdf-0012-01.png)


**----- Start of picture text -----**<br>
0.050 0.0525 0.10 LTT-IW (Ours)<br>0.0500 LTT-RS<br>0.045 LTT-IW (Ours) 0.0475 LTT-IW (Ours) 0.08 LTT<br>0.040 LTT-RS LTT-RS 0.06 = 0.05<br>LTT 0.0450 LTT<br>0.035 = 0.05 0.0425 = 0.05 0.04<br>0.0400<br>0.030 0.02<br>0.0375<br>1 2 3 4 5 0.5 1.0 1.5 2.0 2.5 3.0 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) low ( b ) medium ( c ) high<br>1: 0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis)<br>target domain in BAF ( low , medium and high panels). Ignoring covariate shift<br>in overly conservative or overly invalid risk control.<br>LTT-IW (Ours) LTT-IW (Ours)<br>0.60 LTT-RS 0.58 0.8 LTT-RS<br>LTT LTT<br>0.7<br>0.55 0.56<br>0.6<br>0.54 LTT-IW (Ours) 0.5<br>0.50 LTT-RS<br>LTT 0.4<br>0.52<br>1 2 3 4 5 0.5 1.0 1.5 2.0 2.5 3.0 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) low ( b ) medium ( c ) high<br>0.95-quantile of FPR 0.95-quantile of FPR 0.95-quantile of FPR<br>Average FNR Average FNR Average FNR<br>**----- End of picture text -----**<br>


Figure 1: 0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF ( `low` , `medium` and `high` panels). Ignoring covariate shift (LTT) results in overly conservative or overly invalid risk control. 

Figure 2: Average FNR (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF ( `low` , `medium` and `high` panels). LTT-IW consistently results in lower FNR compared to LTT-RS. 

notice that, on real-world data where the covariate shift assumption may be violated, higher sample efficiency makes the procedure less conservative, but may exacerbate risk violations. 

## **5. Conclusion and Future Work** 

In this work, we showed that using importance-weighted losses is a viable approach to tackle high-probability risk control under covariate shift. The experimental results show that our method outperforms the rejection-sampling baseline in terms of auxiliary performance measures. Although caveats remain, as these approaches rely on the covariate-shift assumption, the results show that the use of importance weights can narrow the risk gap, bringing the risk closer to the prescribed level even if the covariate-shift assumption is violated. 

While the results presented show LTT-IW to be less conservative than LTT-RS in general, there may be individual cases where the opposite happens. An interesting research avenue consists of automatically selecting the better method. Further work could also extend the LTT-IW framework to support other risk functionals and develop strategies to increase p-value power ( _e.g._ , via variance-reduction techniques). Appendix D discusses some limitations of one such approach. 

Both methods herein considered assume accurate importance weight estimates. The upper-confidence bounds provided by Park et al. (2022) address this uncertainty but assume the knowledge of hyperparameters for which there are no tuning guidelines, as well as 

12 

High Probability Risk Control Under Covariate Shift 


![](markdown_output/almeida25a_images/almeida25a.pdf-0013-01.png)


**----- Start of picture text -----**<br>
0.130 0.100 0.225 LTT-IW (Ours)<br>0.125 0.095 0.200 LTT-RS<br>0.120 LTT-IW (Ours)LTT-RS 0.090 LTT-IW LTT-RS (Ours) 0.175 LTT= 0.1<br>0.115 LTT 0.085 LTT 0.150<br>0.110 = 0.1 = 0.1 0.125<br>0.080<br>0.105 0.100<br>0.075<br>0.100 0.075<br>1 2 3 4 5 1 2 3 4 5 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) clipart ( b ) real ( c ) infograph<br>0.10<br>0.14<br>0.13 0.09<br>LTT-IW (Ours) 0.13 0.08 LTT-IW (Ours)<br>0.12 LTT-RS LTT-RS<br>0.11 LTT= 0.1 0.120.11 LTT-IW (Ours)LTT-RSLTT 0.070.06 LTT = 0.1<br>0.05<br>= 0.1<br>0.10 0.10<br>1 2 3 4 5 1 2 3 4 5 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( d ) painting ( e ) sketch ( f  ) quickdraw<br>0.95-quantile of Miscoverage 0.95-quantile of Miscoverage 0.95-quantile of Miscoverage<br>0.95-quantile of Miscoverage 0.95-quantile of Miscoverage 0.95-quantile of Miscoverage<br>**----- End of picture text -----**<br>


Figure 3: 0.90 miscoverage quantiles (vertical axis) vs. source sample size (horizontal axis) for each target domain in DomainNet. The use of HPRC methods bridges the risk gap for `clipart` , `infograph` , `painting` and `sketch` . 


![](markdown_output/almeida25a_images/almeida25a.pdf-0013-03.png)


**----- Start of picture text -----**<br>
50 LTT-IW (Ours) 20 LTT-IW (Ours) 175 LTT-IW (Ours)<br>LTT-RS LTT-RS LTT-RS<br>40 LTT 18 LTT 150 LTT<br>125<br>30 16<br>100<br>20 14 75<br>12 50<br>1 2 3 4 5 1 2 3 4 5 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) clipart ( b ) real ( c ) infograph<br>50 LTT-IW (Ours) 25.0 LTT-IW (Ours) LTT-IW (Ours)<br>LTT-RS LTT-RS 16 LTT-RS<br>LTT 22.5 LTT LTT<br>40<br>20.0 14<br>30 17.5 12<br>15.0<br>20 12.5 10<br>1 2 3 4 5 1 2 3 4 5 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( d ) painting ( e ) sketch ( f  ) quickdraw<br>Average Average set size Average Average set size Average Average set size<br>Average Average set size Average Average set size Average Average set size<br>**----- End of picture text -----**<br>


Figure 4: Mean average set size (vertical axis) vs. source sample size (horizontal axis) for each target domain in DomainNet. LTT-IW achieves smaller average set sizes than LTT-RS, but with increased risk violations due to concept shift. 

Lipschitz-continuous densities, which may not be appropriate for dealing with mixed categorical and numerical feature spaces. Future work could relax this assumption or develop alternatives to account for uncertainty. Furthermore, these methods assume a known upper bound _B_ on the importance weights. Appendix E presents a sensitivity analysis on _B_ , 

13 

Almeida Bravo Bono Bizarro Figueiredo 

along with a discussion of alternative self-normalized approaches. The design of bound-free methods is also a promising direction for future research. 

## **References** 

- T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama. Optuna: A next-generation hyperparameter optimization framework. In _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ , pages 2623—-2631, 2019. 

- A. N. Angelopoulos and S. Bates. Conformal prediction: A gentle introduction. _Foundations and Trends Machine Learning_ , 16(4):494—-591, 2023. 

- A. N. Angelopoulos, S. Bates, A. Fisch, L. Lei, and T. Schuster. Conformal risk control. In _The 12th International Conference on Learning Representations (ICLR)_ , 2024. 

- A. N. Angelopoulos, S. Bates, E. J. Cand`es, M. I. Jordan, and L. Lei. Learn then test: Calibrating predictive algorithms to achieve risk control. _Annals of Applied Statistics_ , 19 (2):1641–1662, 2025. 

- R. F. Barber, E. J. Candes, A. Ramdas, and R. J. Tibshirani. The limits of distribution-free conditional predictive inference. _Information and Inference: A Journal of the IMA_ , 10 (2):455–482, 2021. 

- R. F. Barber, E. J. Candes, A. Ramdas, and R. J. Tibshirani. Conformal prediction beyond exchangeability. _Annals of Statistics_ , 51(2):816–845, 2023. 

- S. Bates, A. Angelopoulos, L. Lei, J. Malik, and M. Jordan. Distribution-free, riskcontrolling prediction sets. _Journal of the ACM_ , 68(6):1–43, 2021. 

- S. Chandra, A. Haque, L. Khan, and C. Aggarwal. Efficient sampling-based kernel mean matching. In _IEEE Interna. Conference on Data Mining (ICDM)_ , pages 811–816, 2016. 

- C. J. Clopper and E. S. Pearson. The use of confidence or fiducial limits illustrated in the case of the binomial. _Biometrika_ , 26(4):404–413, 1934. 

- A. Farinhas, C. Zerva, D. Ulmer, and A. F. T. Martins. Non-exchangeable conformal risk control. In _International Conference on Learning Representations (ICLR)_ , 2024. 

- I. Gibbs, J. J. Cherian, and E. J. Cand`es. Conformal prediction with conditional guarantees. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 2025. 

- P. Glasserman. _Monte Carlo Methods in Financial Engineering_ . Springer, New York, 2003. 

- J. Huang, A. Gretton, Ka. Borgwardt, B. Sch¨olkopf, and A. Smola. Correcting sample selection bias by unlabeled data. In _Neural Information Processing Systems_ , pages 601– 608. MIT Press, 2006. 

- S. Jesus, J. Pombal, D. Alves, A. Cruz, P. Saleiro, R. P. Ribeiro, J. Gama, and P. Bizarro. Turning the tables: Biased, imbalanced, dynamic tabular datasets for ML evaluation. In _Neural Information Processing Systems_ , 2022. 

14 

High Probability Risk Control Under Covariate Shift 

- G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T. Liu. LightGBM: A highly efficient gradient boosting decision tree. In _Neural Information Processing Systems_ , volume 30. Curran Associates, 2017. 

- W. Kouw and M. Loog. An introduction to domain adaptation and transfer learning, 2019. URL `https://arxiv.org/abs/1812.11806` . 

- I. Kuzborskij and C. Szepesv´ari. Efron-Stein PAC-Bayesian inequalities, 2020. URL `https: //arxiv.org/abs/1909.01931` . 

- B. Laufer-Goldshtein, A. Fisch, R. Barzilay, and T. S. Jaakkola. Efficiently controlling multiple risks with Pareto testing. In _Intern. Conf. on Learning Representations_ , 2023. 

- S. Park, E. Dobriban, I. Lee, and O. Bastani. PAC prediction sets under covariate shift. In _International Conference on Learning Representations_ , 2022. 

- X. Peng, Q. Bai, X. Xia, Z. Huang, K. Saenko, and B. Wang. Moment matching for multisource domain adaptation. In _International Conference on Computer Vision (ICCV)_ , pages 1406–1415, 2019. 

- J. Qui˜noreo-Candela, M. Sugiyama, A. Schwaighofer, and N. D. Lawrence. _Dataset Shift in Machine Learning_ . MIT Press, 2009. 

- S. Resnick. _A Probability Path_ . Birkh¨auser, 1999. 

- C. Robert and G. Casella. _Monte Carlo Statistical Methods_ . Springer-Verlag, New York, 2nd edition, 2004. 

- G. Shafer and V. Vovk. A tutorial on conformal prediction. _Journal of Machine Learning Research_ , 9:371–421, 2008. 

- P. Stojanov, M. Gong, J. Carbonell, and K. Zhang. Low-dimensional density datio dstimation for covariate shift correction. In _22nd International Conference on Artificial Intelligence and Statistics (AISTATS)_ , pages 3449–3458, 2019. 

- M. Sugiyama, S. Nakajima, H. Kashima, P. Buenau, and M. Kawanabe. Direct importance estimation with model selection and its application to covariate shift adaptation. In _Neural Information Processing Systems_ , 2007. 

- M. Sugiyama, T. Kanamori, T. Suzuki, S. Hido, J. Sese, I. Takeuchi, and L. Wang. A density-ratio framework for statistical data processing. _Information and Media Technologies_ , 4(4):962–987, 2009. 

- R. J. Tibshirani, R. F. Barber, E. J. Cand`es, and A. Ramdas. Conformal prediction under covariate shift. In _Neural Information Processing Systems_ , 2019. 

- V. Vovk. Conditional validity of inductive conformal predictors. In _Asian Conference on Machine Learning_ , pages 475–490, 2012. 

15 

Almeida Bravo Bono Bizarro Figueiredo 

- S. Watanabe. Tree-structured Parzen estimator: Understanding its algorithm components and their roles for better empirical performance, 2023. URL `https://arxiv.org/abs/ 2304.11127` . 

- I. Waudby-Smith and A. Ramdas. Estimating means of bounded random variables by betting. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 86(1): 1–27, 2024. 

- K. You, X. Wang, M. Long, and M. Jordan. Towards accurate model selection in deep unsupervised domain adaptation. In _36th International Conference on Machine Learning (ICML)_ , pages 7124–7133, 2019. 

- Y. Yu and C. Szepesv´ari. Analysis of kernel mean matching under covariate shift. In _29th International Coference on Machine Learning (ICML)_ , pages 1147–1154, 2012. 

- T. P. Zollo, T. Morrill, Z. Deng, J. Snell, T. Pitassi, and R. Zemel. Prompt risk control: A rigorous framework for responsible deployment of large language models. In _International Conference on Learning Representations_ , 2024. 

## **Appendix A. Dataset Generation** 

In this appendix, we provide details on the generation of domains from the BAF dataset. During preprocessing, missing numerical values are imputed with the mean and standardized using z-score normalization, while categorical features are imputed with the mode. To eliminate any temporal drift, the `month` feature is excluded. 

To generate the disjoint covariate-shifted datasets, we employ a strategy similar to that of Huang et al. (2006). Let _c_ ( _x_ ) be the value of the feature `credit` ~~`r`~~ `isk score` of sample _x_ , and let _q_ low _, q_ med _, q_ high be the empirical 0 _._ 25 _,_ 0 _._ 50 _,_ 0 _._ 75 quantiles of _c_ ( _x_ ), respectively. Sampling proceeds in stages: each observation is included in the low-risk domain with probability _p_ low( _x_ ) = exp � _−_[(] _[c]_[(] _[x]_ 2[)] _σ[−]_ low[2] _[q]_[low][)][2] �; if not selected, it enters the medium-risk domain with probability _p_ med( _x_ ) defined analogously using _q_ med and _σ_ med; any remaining sample is assigned to the high-risk with probability _p_ high( _x_ ), defined similarly. The bandwidths _{σ_ low _, σ_ med _, σ_ high _}_ are optimized to maximize the largest importance weight between any pair of domains while ensuring the expected dataset sizes lie in [5 _×_ 10[4] _,_ 1 _._ 5 _×_ 10[5] ]. 

Since the sampling procedure is label-independent, the resulting domains differ solely by covariate shift. Let _Si_ be the indicator that a sample is assigned to domain _i_ , and let P _i_ , P _j_ be the corresponding distributions. Then, the importance weight is 


![](markdown_output/almeida25a_images/almeida25a.pdf-0016-10.png)


which is a function of _x_ alone, confirming the covariate shift assumption. Under the sequential scheme, we have P( _S_ low = 1 _| x_ ) = _p_ low( _x_ ), P( _S_ med = 1 _| x_ ) = (1 _− p_ low( _x_ )) _p_ med( _x_ ), and P( _S_ high = 1 _| x_ ) = (1 _− p_ low( _x_ )) (1 _− p_ med( _x_ )) _p_ high( _x_ ). Marginal selection probabilities can be estimated via Monte Carlo as P( _Sk_ = 1) _≈ n[−]_[1][ �] _[n] i_ =1[P][(] _[S][k]_[=][1] _[|][x][i]_[),][for] _k ∈{_ low _,_ med _,_ high _}_ , and used to estimate dataset sizes. 

16 

High Probability Risk Control Under Covariate Shift 

## **Appendix B. P-value ablations** 

In this appendix, we compare the use of the WSR p-value against other possible p-values. We consider the Hoeffding-Bentkus p-value for testing _H_ 0( _λ, α_ ) (Angelopoulos et al., 2025). Since this approach only works for losses supported in [0 _,_ 1], we consider the rescaled hypothesis _H_ 0( _λ, α_ ) : _[R] u_[(] _[λ][′] −_[)] _[−] l[′][l][′] > u[α][′][−] −[l] l[′][′]_[(see][Section][3][),][yielding][the][following][p-value:] 


![](markdown_output/almeida25a_images/almeida25a.pdf-0017-03.png)


where _Rw_ ( _λ_ ) = _n[−] s_[1] � _ni_ =1 _s[w]_[(] _[X][i]_[)] _[L]_[(] _[X][i][, Y][i]_[;] _[ λ]_[) and] _[ h]_[(] _[a, b]_[) =] _[ a]_[ log(] _[a/b]_[)+(1] _[−][a]_[) log((1] _[−][a]_[)] _[/]_[(1] _[−] b_ )). We also consider the application of Bernstein’s inequality for this hypothesis test (Bates et al., 2021). In particular, we reject _H_ 0( _λ, α_ ) if 


![](markdown_output/almeida25a_images/almeida25a.pdf-0017-05.png)


where ˆ _σw_ ( _λ_ ) = ~~�~~ ( _ns −_ 1) _[−]_[1][ �] _[n] i_ =1 _[s]_[(] _[L]_[(] _[X][i][, Y][i]_[;] _[ λ]_[)] _[ −][R]_[ˆ] _[w]_[(] _[λ]_[))][2][ denotes the empirical importance-] weighted risk standard deviation. For brevity, we report only the BAF results, where the covariate shift assumption is guaranteed to hold. Figures 5 and 6 replicate the analysis of Section 4. Results show that the WSR p-value is the least conservative of the three, bringing the FPR the closest to _α_ and achieving the lowest average FNR. 


![](markdown_output/almeida25a_images/almeida25a.pdf-0017-07.png)


**----- Start of picture text -----**<br>
0.05 0.05<br>0.050<br>0.04 0.04<br>0.03 0.045 0.03<br>0.02 WSR 0.040 WSR 0.02 WSR<br>HB HB HB<br>0.01 Bernstein Bernstein 0.01 Bernstein<br>0.035<br>= 0.05 = 0.05 = 0.05<br>0.00 0.00<br>1 2 3 4 5 0.5 1.0 1.5 2.0 2.5 3.0 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) low ( b ) medium ( c ) high<br>0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis) for each<br>domain in BAF. WSR yields 0.95 FPR quantiles closest to 0.05.<br>1.0 WSR 0.64 WSR 1.0 WSR<br>0.9 HB Bernstein 0.62 HB Bernstein 0.9 HBBernstein<br>0.8 0.60<br>0.8<br>0.58<br>0.7<br>0.56 0.7<br>0.6<br>0.54<br>0.5 0.6<br>0.52<br>1 2 3 4 5 0.5 1.0 1.5 2.0 2.5 3.0 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) low ( b ) medium ( c ) high<br>0.95-quantile of FPR 0.95-quantile of FPR 0.95-quantile of FPR<br>Average FNR Average FNR Average FNR<br>**----- End of picture text -----**<br>


Figure 5: 0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF. WSR yields 0.95 FPR quantiles closest to 0.05. 

Figure 6: Mean FNR (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF. Out of the three p-values, WSR achieves the lowest FNR values. 

17 

Almeida Bravo Bono Bizarro Figueiredo 

## **Appendix C. Computational Considerations** 

We now conduct a brief analysis of the computational cost of LTT-IW. All experiments were run on a machine with a 14-core CPU and 20-core GPU Apple M4 chip, 24GB of RAM, and a 512GB SSD. We first analyze KMM, which dominates runtime due to the need to solve multiple quadratic programs. Table 1 presents runtime, peak memory usage, and source/target dataset sizes ( _ns_ , _nt_ ) for each target domain in both datasets. 

LTT can be made lightweight by precomputing model scores once before running the procedure. To evaluate scalability, we measure the average runtime and peak memory usage across all LTT runs on the `low` domain of BAF, varying the size of the subsampled calibration set _N_ . Figure 7 shows that both metrics grow roughly linearly with _N_ . 

Table 1: Execution time, peak memory usage, and dataset size statistics for KMM. 

||||||||||||||(b) DomainNet|(b) DomainNet|(b) DomainNet|(b) DomainNet|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||(a)|BAF|||||||**Domain**|||**Time**||**Mem.**||**_ns_**|**_nt_**|
|**Domain**<br>`low`<br>`medium`<br>`high`|**Time**<br>**(min)**<br>9.28<br>6.03<br>9.45|**Mem.**<br>**(GB)**<br>1.303<br>1.493<br>1.296||||**_ns_**<br>56,196<br>31,537<br>57,107||**_nt_**<br>16,224<br>40,883<br>15,313||`clipart`<br>`real`<br>`infograph`<br>`painting`<br>`sketch`|||**(min)**<br>33.23<br>46.20<br>35.56<br>38.25<br>37.22||**(GB)**<br>4.597<br>4.790<br>4.603<br>4.635<br>4.630||176,743<br>176,743<br>176,743<br>176,743<br>176,743|14,604<br>52,041<br>15,582<br>21,850<br>20,916|
|||||||||||`quickdraw`|||46.75||4.719||176,743|51,750|
|||LTT Runtime (s)|0.04<br>0.06<br>0.08<br>0.10<br>0.12<br>0.14|||||||0.5<br>1.0<br>1.5<br>2.0<br>2.5<br>3.0<br>Peak Memory Usage (MB)|||||||||
|||||1||2<br>3||4<br>5|||1||2<br>3||4<br>5||||
|||||||N||1e4|||||N||1e4||||



Figure 7: Runtime (left panel) and peak memory usage (right panel) of LTT-IW as a function of calibration subset size on the `low` domain of BAF. Both scale approximately linearly. 

## **Appendix D. Variance Reduction Techniques** 

High-variance losses can inflate p-values, reducing the power to detect risk-controlling configurations. One classical approach to mitigate this is to use a control variate _T_ ( _X, Y_ ; _λ_ ) (Glasserman, 2003), which yields the following adjusted loss with the same expectation: 


![](markdown_output/almeida25a_images/almeida25a.pdf-0018-09.png)


where _η_ = _−_ Cov[ _w_ ( _X_ ) _L_ ( _X, Y_ ; _λ_ ) _, T_ ( _X, Y_ ; _λ_ )] _/_ Var[ _T_ ( _X, Y_ ; _λ_ )] is chosen to to minimize the variance of _L_ cv. We choose _T_ ( _X, Y_ ; _λ_ ) = _w_ ( _X_ ), since EPsource[ _w_ ( _X_ )] = 1 (You et al., 2019). Figures 8 and 9 show the results for LTT-IW with and without control variates. To preserve the i.i.d. nature of the data, we use half of the source data to estimate _η_ and perform risk control on the other half. The introduction of control variates yields more conservative 

18 

High Probability Risk Control Under Covariate Shift 

results; the variance reduction obtained may be outweighed by the fewer data used for hypothesis testing. Future work could explore more sample-efficient variance reduction techniques or smarter ways to allocate data for variance reduction. It is important to note that the range of the loss changes from [0 _, B_ ] to [min( _ηB,_ 0) _− η,_ max((1 + _η_ ) _B,_ 0) _− η_ ]. For _η >_ 0, it expands from _B_ to (1 + _η_ ) _B_ , meaning variance reduction comes at the cost of a wider range, which may reduce p-value power. 


![](markdown_output/almeida25a_images/almeida25a.pdf-0019-02.png)


**----- Start of picture text -----**<br>
0.05 0.052 0.05<br>0.04 0.051 0.04<br>0.03 0.050 0.03<br>0.049<br>0.02 0.02<br>LTT-IW 0.048 LTT-IW LTT-IW<br>0.01 LTT-IW + CV LTT-IW + CV 0.01 LTT-IW + CV<br>= 0.05 0.047 = 0.05 = 0.05<br>0.00 0.00<br>1 2 3 4 5 0.5 1.0 1.5 2.0 2.5 3.0 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) low ( b ) medium ( c ) high<br>0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis) for each<br>domain in BAF. Control variates yield more conservative risk levels.<br>1.0 LTT-IW 0.58 LTT-IW 1.0 LTT-IW<br>0.9 LTT-IW + CV 0.57 LTT-IW + CV 0.9 LTT-IW + CV<br>0.8 0.56<br>0.8<br>0.7 0.55<br>0.54 0.7<br>0.6<br>0.53<br>0.5 0.6<br>0.52<br>1 2 3 4 5 0.5 1.0 1.5 2.0 2.5 3.0 1 2 3 4 5<br>N 1e4 N 1e4 N 1e4<br>( a ) low ( b ) medium ( c ) high<br>0.95-quantile of FPR 0.95-quantile of FPR 0.95-quantile of FPR<br>Average FNR Average FNR Average FNR<br>**----- End of picture text -----**<br>


Figure 8: 0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF. Control variates yield more conservative risk levels. 

Figure 9: Mean FNR (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF. Using control variates results in higher FNR. 

## **Appendix E. Sensitivity to the Importance Weight Upper Bound** 

This appendix reports a sensitivity analysis regarding the choice of the importance weight upper bound _B_ , comparing the WSR p-value to the (asymptotically valid) normal p-value (Angelopoulos et al., 2025): 


![](markdown_output/almeida25a_images/almeida25a.pdf-0019-07.png)


which eliminates the need to specify _B_ . We consider the BAF dataset and 10 _,_ 000 calibration points, setting _B_ = _γB_[ˆ] for _γ ∈{_ 1 _,_ 1 _._ 5 _,_ 2 _,_ 2 _._ 5 _,_ 3 _._ 0 _}_ , where _B_[ˆ] is the sample maximum importance weight. As shown in Figures 10 and 11, LTT-IW becomes increasingly conservative with larger _γ_ , while the normal p-value remains unaffected, as expected. 

Kuzborskij and Szepesv´ari (2020) propose a self-normalized high-probability lower bound on the true risk. Let _L_ be a loss supported in [0 _,_ 1]; then, with probability at least 1 _−_ ( _ns_ + 1) _e[−][x]_ , for _x ≥_ 2 and _y ≥_ 0, we have 


![](markdown_output/almeida25a_images/almeida25a.pdf-0019-10.png)


19 

Almeida Bravo Bono Bizarro Figueiredo 


![](markdown_output/almeida25a_images/almeida25a.pdf-0020-01.png)


**----- Start of picture text -----**<br>
0.05 0.052 0.05<br>0.051 0.04<br>0.04<br>0.050 WSR<br>0.03 Normal<br>0.03 0.049 0.02 = 0.05<br>WSR 0.048 WSR<br>Normal Normal 0.01<br>0.02 = 0.05 0.047 = 0.05<br>0.00<br>1.0 1.5 2.0 2.5 3.0 1.0 1.5 2.0 2.5 3.0 1.0 1.5 2.0 2.5 3.0<br>( a ) low ( b ) medium ( c ) high<br>10: 0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal<br>target domain in BAF as a function of the multiplicative factor γ .<br>0.65 WSRNormal 0.56 WSRNormal 1.0 WSRNormal<br>0.9<br>0.60 0.55<br>0.8<br>0.55<br>0.54 0.7<br>0.50<br>0.53 0.6<br>1.0 1.5 2.0 2.5 3.0 1.0 1.5 2.0 2.5 3.0 1.0 1.5 2.0 2.5 3.0<br>( a ) low ( b ) medium ( c ) high<br>0.95-quantile of FPR 0.95-quantile of FPR 0.95-quantile of FPR<br>Average FNR Average FNR Average FNR<br>**----- End of picture text -----**<br>


Figure 10: 0.95 FPR quantiles (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF as a function of the multiplicative factor _γ_ . 

Figure 11: Mean FNR (vertical axis) vs. source sample size (horizontal axis) for each target domain in BAF as function of the multiplicative factor _γ_ . 

where _Nx_ ( _ns_ ) = � _ns −_ ~~�~~ 2 _xns_ E[ _w_[2] ( _X_ )]�+[and] _[V]_[W][=] _Nx_[2] 1( _ns_ ) � _ni_ =1 _s_ � _w_[2] ( _Xi_ ) + E[ _w_[2] ( _X_ )]�. From here, an upper bound can be derived for hypothesis testing by setting _L[′]_ = 1 _− L_ , identifying the l.h.s. with 1 _−_ E[ _L_ ( _X, Y_ ; _λ_ )] and solving the inequality for E[ _L_ ( _X, Y_ ; _λ_ )]. However, it assumes that E[ _w_[2] ( _X_ )] is known. Future work could address this limitation, as well as investigate optimal choices of _y_ . 

## **Appendix F. LightGBM Parameter Grid** 

Table 2: Hyperparameter grid used for LightGBM 

|**Parameter**|**Suggestion type**|**Range**|
|---|---|---|
|learning rate|log-uniform|[0_._01_,_ 0_._50]|
|max. number of leaves|integer|[10_,_ 201]|
|max. depth|integer|[_−_1_,_ 21]|
|min. points per leaf|integer|[20_,_ 101]|
|data subsample fraction|uniform|[0_._5_,_ 1_._0]|
|feature subsample fraction|uniform|[0_._5_,_ 1_._0]|
|boosting iterations|integer|[50_,_ 1000]|
|_L_2 regularisation constant|log-uniform|[10_,_ 10 000]|
|negative-class subsample fraction|uniform|[0_._01_,_ 0_._5]|
|early-stopping rounds|integer|[20_,_ 100]|



20 

