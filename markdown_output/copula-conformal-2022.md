Published as a conference paper at ICLR 2024 

# - COPULA CONFORMAL PREDICTION FOR MULTI STEP TIME SERIES FORECASTING 

## **Sophia Sun** 

University of California, San Diego shs066@ucsd.edu 

## **Rose Yu** 

University of California, San Diego roseyu@ucsd.edu 

## ABSTRACT 

Accurate uncertainty measurement is a key step in building robust and reliable machine learning systems. Conformal prediction is a distribution-free uncertainty quantification framework popular for its ease of implementation, finite-sample coverage guarantees, and generality for underlying prediction algorithms. However, existing conformal prediction approaches for time series are limited to single-step prediction without considering the temporal dependency. In this paper, we propose the **Copula C** onformal **P** rediction algorithm for multivariate, multi-step **T** ime **S** eries forecasting, **CopulaCPTS** . We prove that CopulaCPTS has finite-sample validity guarantee. On four synthetic and real-world multivariate time series datasets, we show that CopulaCPTS produces more calibrated and efficient confidence intervals for multi-step prediction tasks than existing techniques. Our code is open-sourced at https://github.com/Rose-STL-Lab/CopulaCPTS. 

## 1 INTRODUCTION 

Deep learning models are becoming widely used in high-risk settings such as healthcare and transportation. In these settings, it is important that a model produces calibrated uncertainty to reflect its own confidence. Confidence regions are a common approach to quantify prediction uncertainty (Khosravi et al., 2011). A (1 _− α_ )-confidence region Γ[1] _[−][α]_ for a random variable _y_ is _valid_ if it contains _y_ ’s true value with high probability: P[ _y ∈_ Γ[1] _[−][α]_ ] _≥_ 1 _− α._ Note that one can make the confidence region infinitely large to satisfy validity. But for the confidence region to be useful, we also want to minimize its area while remaining valid; this is known as the _efficiency_ of the region. 

Conformal prediction (CP) is a powerful framework to produce confidence regions with finite-sample guarantees of validity (Vovk et al., 2005; Lei et al., 2018). Furthermore, it makes no assumptions about the underlying prediction model or the data distribution. CP’s generality, simplicity, and statistical guarantees have made it popular for many real-world applications including time series prediction (Xu & Xie, 2021), drug discovery (Eklund et al., 2015) and safe robotics (Luo et al., 2021). 

This paper considers the setting of multi-step time series forecasting from a set of independent sequences. Consider the problem of vehicle trajectory prediction, illustrated in Figure 1. Given a 

Figure 1: Illustration of the multi-step time series forecasting setting. (Left) The timesteps within a time series are temporally dependent, and (Right) the observations in the dataset are independent. 

1 

Published as a conference paper at ICLR 2024 

dataset of trajectories, the task is to predict a future trajectory for _k_ steps given its past trajectory of _t_ time steps. We assume that the trajectories are independent from each other. For each trajectory, these time steps are temporally dependent. 

There are many real-world tasks that present the same challenges as the example above, such as EEG forecasting (each patient is independent), short-term weather forecasting (local meteorology history is independent), etc. They require predicting multiple time steps into the future, so it is desired to have a “cone of uncertainty” that covers the entire course of the forecasts. Existing CP methods for time series data either only provide coverage guarantee for individual time steps (Gibbs & Candes, 2021; Xu & Xie, 2021) or produce confidence regions that are often too inefficient to be useful, especially in long horizons or multivariate settings (Stankeviˇci¯ut˙e et al., 2021). 

In this paper, we present a practical and effective conformal prediction algorithm for multi-step time series forecasting. We introduce **CopulaCPTS** , a **Copula** -based **C** onformal **P** rediction algorithm for multi-step **T** ime **S** eries forecasting. A copula is a multivariate cumulative distribution function that models the dependence between multiple random variables. By using copulas to model the uncertainty jointly over future time steps, we can shrink the confidence regions significantly while maintaining validity. Copulas have been used for conformal prediction (Messoudi et al., 2021), but they focus on multiple target prediction in non-temporal settings and did not provide a validity proof. 

In summary, our contributions are: 

- We introduce **CopulaCPTS** , a general uncertainty quantification algorithm that can be applied to _any_ multivariate multi-step forecaster. 

- We prove that **CopulaCPTS** produces valid confidence regions for the full forecast horizon. 

- **CopulaCPTS** produces significantly sharper and more calibrated uncertainty estimates than state-of-the-art baselines on two synthetic and two real-world benchmark datasets. 

- We extend **CopulaCPTS** to obtain valid confidence intervals for time series forecasts of varying lengths. 

## 2 RELATED WORK 

**Deep Uncertainty Quantification for Time-Series Forecasting.** The two major paradigms of Uncertainty Quantification (UQ) methods for deep neural networks are Bayesian and Frequentist. Bayesian approaches estimate a distribution over the model parameters given data, and then marginalize these parameters to form output distributions via Markov Chain Monte Carlo (MCMC) sampling (Welling & Teh, 2011; Neal, 2012; Chen et al., 2014) or variational inference (VI) (Graves, 2011; Kingma et al., 2015; Blundell et al., 2015; Louizos & Welling, 2017). Wang et al. (2019); Wu et al. (2021) propose Bayesian Neural Networks (BNN) for UQ of spatiotemporal forecasts. In practice, Bayesian UQ can be computationally expensive and difficult to optimize, especially for larger networks (Lakshminarayanan et al., 2017; Zadrozny & Elkan, 2001). Furthermore, Bayesian methods do not provide any finite sample coverage guarantees. Therefore, UQ for deep neural network time series forecasts often adopts approximate Bayesian inference such as MC-dropout (Gal & Ghahramani, 2016b; Gal et al., 2017). 

Frequentist UQ methods emphasize robustness against variations in the data. These approaches either rely on resampling the data or learning an interval bound to encompass the dataset. For time series forecasting UQ, approaches include ensemble methods such as bootstrap (Efron & Hastie, 2016; Alaa & Van Der Schaar, 2020) and jackknife methods (Kim et al., 2020; Alaa & Van Der Schaar, 2020); interval prediction methods include interval regression through proper scoring rules (Kivaranovic et al., 2020; Wu et al., 2021), and quantile regression (Takeuchi et al., 2006), with many recent advances for time series UQ (Tagasovska & Lopez-Paz, 2019; Gasthaus et al., 2019; Park et al., 2022; Kan et al., 2022). Many of the frequentist methods produce asymptotically valid confidence regions and can be categorized as distribution-free UQ techniques as they are (1) agnostic to the underlying model and (2) agnostic to data distribution. 

**Conformal Prediction.** Conformal prediction (CP) is an important member of distribution-free UQ methods; we refer readers to Angelopoulos & Bates (2021) for a comprehensive introduction and survey of CP. CP has become popular because of its simplicity, generality, theoretical soundness, and 

2 

Published as a conference paper at ICLR 2024 

low computational cost. A key feature of CP is that under the exchangeability assumption, conformal methods guarantee validity in finite samples (Vovk et al., 2005). 

Most relevant to our work is the recent endeavor in generalizing CP to time-series forecasting. According to Stankeviciˇ ut¯ e et al. (2021) there are two settings:˙ data generated from (1) one single time series or (2) multiple independent time series. For the first setting, ACI (Gibbs & Candes, 2021) and EnbPI (Xu & Xie, 2021) developed CP algorithms that relax the exchangeability assumption while maintaining asymptotic validity via online learning (former) and ensembling (later); Zaffran et al. (2022) further improves online adaptation. Sousa et al. (2022) combines EnbPI with conformal quantile regression (Romano et al., 2019) to model heteroscedastic time series. However, because these algorithms operate on one single time series, the validity guarantees do not cover the full horizon, posing issues for application in high-risk settings. 

We focus on the setting where data consists of many independent time series. Stankeviciˇ ut¯ e et al.˙ (2021) shares the same setting as ours but provides only a univariate time series solution. We show that their method of applying Bonferroni correction produces inefficient confidence regions, especially for multidimensional data or long prediction horizons. Messoudi et al. (2021) uses a copula function for multi-target CP for non-temporal data, creating box-like regions to account for the correlations between the labels. However, they do not provide theoretical proof and empirical results have shown that are often invalid. This paper builds upon these works and presents a novel two-step algorithm with guaranteed multivariate multi-step coverage and efficient confidence regions. 

## 3 BACKGROUND 

## 3.1 INDUCTIVE CONFORMAL PREDICTION (ICP) 

Let _D_ = _{z[i]_ = ( _x[i] , y[i]_ ) _}[n] i_ =1[be a dataset with input] _[ x][i][∈X]_[and output] _[ y][i][∈Y]_[such that each data] point _z[i] ∈Z_ := _X × Y_ is drawn i.i.d. from an unknown distribution _Z_ . 

We will briefly present the algorithm and theoretical results for conformal prediction, and refer readers to Angelopoulos & Bates (2021) for a thorough introduction. The goal of conformal prediction is to produce a _valid_ confidence region (Def. 3.1) for any underlying prediction model. 

> **Definition 3.1** confidence region (Validity) Γ[1] _[−][α]_ ( **.** _x_ Given a new data point) is a subset of _Y_ containing probable outputs ( _x, y_ ) and a desired confidence _y_ ˜ _∈Y_ given 1 _− α x ∈_ . The region(0 _,_ 1), the Γ[1] _[−][α]_ is valid if 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0003-09.png)


Conformal prediction splits the dataset into a proper training set _Dtrain_ and a calibration set _Dcal_ . A prediction model _f_[ˆ] : _X →Y_ is trained on _Dtrain_ . We use a _nonconformity score A_ : _Z[|D][train][|] ×Z →_ R to quantify how well a data sample from calibration _conforms_ to the training dataset. Typically, we choose a metric of disagreement between the prediction and the true label as the non-conformity score, such as the Euclidean distance: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0003-11.png)


For conciseness, we write _A_ ( _Dtrain,_ ( _x[i] , y[i]_ )) as _A_ ( _z[i]_ ) in rest of the paper. 

Let _S_ = _{A_ ( _z[i]_ ) _}zi∈Dcal_ denote the set of nonconformity scores of all samples in the calibration set _Dcal_ . We can define a quantile function for the nonconformity scores _S_ as: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0003-14.png)


Conformal prediction is guaranteed to produce valid confidence regions (Vovk et al., 2005), under the exchangeablility assumption defined as follows, 

**Definition 3.2** (Exchangeability) **.** In a dataset _{z[i] }[n] i_ =1[of][size] _[n]_[,][any][of][its] _[n]_[!][permutations][are] equally probable. 

The procedure introduced above is known as _inductive_ conformal prediction, as it splits the dataset into training and calibration sets to reduce computation load (Vovk et al., 2005; Lei & Wasserman, 2012). Our method is based on inductive CP, but can also be easily adapted for other CP variants. 

3 

Published as a conference paper at ICLR 2024 

## 3.2 COPULA AND ITS PROPERTIES 

Copula is a concept from statistics that describes the dependency structure in a multivariate distribution. It has also been used in generative models for multivariate time series (Salinas et al., 2019; Drouin et al., 2022). We can use copulas to capture the joint distribution for multiple future time steps. We briefly introduce its notations and concepts. 

**Definition 3.3** (Copula) **.** Given a random vector ( _X_ 1 _, · · · Xk_ ), define the marginal cumulative density function (CDF) for each variable _Xh, h ∈{_ 1 _, . . . , k}_ as 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0004-04.png)


The copula of ( _X_ 1 _, · · · Xk_ ) is the joint CDF of ( _F_ 1( _X_ 1) _, · · · , Fk_ ( _Xk_ )), written as 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0004-06.png)


In other words, the copula function captures the dependency structure between the variable _X_ s; we can view an _k_ dimensional copula _C_ : [0 _,_ 1] _[k] →_ [0 _,_ 1] as a CDF with uniform marginals, as illustrated in Figure 2. A fundamental result in the theory of copula is Sklar’s theorem. 

**Theorem 3.4** (Sklar’s theorem) **.** _Given a joint CDF as F_ ( _X_ 1 _, · · · , Xk_ ) _and the marginals F_ 1( _x_ ) _, . . . , Fk_ ( _x_ ) _, there exists a copula such that_ 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0004-09.png)



![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0004-10.png)


Sklar’s theorem states that for all multivariate distribution functions, there exists a copula function such that the distribution can be expressed using the copula and multiple univariate marginal distributions. When all the _Xk_ s are independent, the copula function is known as the product copula: _C_ ( _u_ 1 _, · · · , uk_ ) = Π _[k] i_ =1 _[u][i]_[.] 

Figure 2: An example copula, where we express a multivariate Gaussian with correlation _ρ_ = 0 _._ 8 with two univariate distributions and a copula function _C_ ( _u_ 1 _, u_ 2). 

## 4 COPULA CONFORMAL PREDICTION FOR TIME SERIES (COPULACPTS) 

UQ methods are evaluated on two properties: _validity_ and _efficiency_ . A model is _valid_ when the predicted confidence is greater than or equal to the probability of events falling into the predicted range (Definition 3.1). The term _calibration_ describes the case of equality in the validity condition. _Efficiency_ , on the other hand, refers to the size of the confidence region. In practice, we want the measure of the confidence region (e.g. its area or length) to be as small as possible, given that the validity condition holds. CopulaCPTS improves the efficiency of confidence regions by modeling the dependency of the time steps using a copula function. 

Denote the time series dataset of size _n_ as _D_ = _{z[i]_ = ( _x[i]_ 1: _t[, y]_ 1: _[i] k_[)] _[}] i[n]_ =1[, where] _[ x]_[1:] _[t][∈]_[R] _[t][×][d]_[is] _[ t]_[ input] steps, and _y_ 1: _k ∈_ R _[k][×][d]_ is _k_ prediction steps, both with dimension _d_ at each step. Each data point _z[i]_ is sampled i.i.d. from an unknown distribution _Z_ . In the multi-step forecasting setting, given a confidence level 1 _− α_ , the algorithm produces _k_ confidence regions for a test input _x[n]_ 1:[+1] _t_[, denoted] as [Γ[1] 1 _[−][α] , . . . ,_ Γ[1] _k[−][α]_ ]. We say the confidence regions are _valid_ if all time steps in the forecast are covered: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0004-16.png)


4 

Published as a conference paper at ICLR 2024 

In the following sections, we introduce CopulaCPTS, a conformal prediction algorithm that is both valid and efficient for multivariate multi-step time series forecasts. 

## 4.1 ALGORITHM DETAILS 

The key insight of our algorithm is that we can model the joint probability of uncertainty for multiple predicted time steps with a copula, hence better capturing the confidence regions. We divide the calibration set _Dcal_ into two subsets: _Dcal−_ 1, which we use to estimate a Cumulative Distribution Function (CDF) on the nonconformity score of each time step, and _Dcal−_ 2, to calibrate the copula. 

The two calibration sets allow us to prove validity for both components of our algorithm. At the cost of using a subset of the data to calibrate a copula, our approach produces provably more efficient confidence regions compared to worst-case corrections such as union bounding in Stankeviciˇ ut¯ e et al.˙ (2021) which is a lower bound for copulas (Appendix B.1), and more valid regions than Messoudi et al. (2021) (table 1). 

**Nonconformity of Multivariate Forecasts.** If the time series is multivariate, we have each target time step _yj ∈_ R _[d]_ . Given _z_ = ( _x, y_ ) _∼Z_ , let the nonconformity score be the L-2 distance e.g. _s[i] j_[=] _[A]_[(] _[z][i]_[)] _[j]_ = _∥yj[i][−][f]_[ˆ][(] _[x][i]_[)] _[j][∥]_[for each timestep] _[ j]_[=][1] _[, . . . , k]_[, where] _[f]_[ˆ][(] _[x]_[)][ is a forecasting model] trained on _Dtrain_ . The confidence region Γ[1] _[−][α]_ ( _x_ ) therefore is a _d_ -dimensional ball. We chose this metric for simplicity, but one can choose other metrics such as Mahalanobis (Johnstone & Cox, 2021) or L-1 (Messoudi et al., 2021) distance based on domain needs, and our algorithm will remain valid. 

For brevity, we will use _S_ 1 = _{s[i] }zi∈Dcal−_ 1 to denote the set of nonconformity scores of data in _Dcal−_ 1 and _S_ 2 = _{s[i] }zi∈Dcal−_ 2 the set of nonconformity scores of data in _Dcal−_ 2. Subscript _j_ will be used to index the set of specific time steps of the scores: _S_ 1 _j_ = _{s[i] j[}][z][i][∈D] cal−_ 1[,] _[ S]_[2] _[j]_[=] _[ {][s][i] j[}][z][i][∈D] cal−_ 2[.] 

**Calibrating CDF on** _Dcal−_ 1 **.** We use _Dcal−_ 1 to build conformal predictive distributions for each time step’s anomaly scores, which provides desirable validity properties (Vovk et al., 2017). The conformal cumulative distribution function is constructed as follows.[1] 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0005-08.png)


**Copula Calibration on** _Dcal−_ 2 **.** Next, for every data point in _Dcal−_ 2, we evaluate the cumulative probability of its anomaly scores with the estimated conformal predictive distributions: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0005-10.png)


We adopt the empirical copula (Ruschendorf, 1976) for modeling and proof in this work. The empirical copula is a non-parametric method of estimating marginals directly from observation, and hence does not introduce any bias. For the joint distribution of _k_ time steps, we construct _C_ empirical : [0 _,_ 1] _[k] →_ [0 _,_ 1] as Eqn 7. 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0005-12.png)


Here boldface _**∞**_ is a k-dimensional vector with each _**∞** j_ = _∞_ for _j_ = 1 _, . . . , k_ . 

To fulfill the full-horizon validity condition of Eqn 4, we only need to find appropriate **u** _[∗]_ such that _C_ empirical( **u** _[∗]_ ) _≥_ 1 _− α_ . 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0005-15.png)


> 1Because of the random component, equation 5 is a “thick” CDF of thickness _|S_ 11 _|_ +1[,][which][becomes] inconsequential when the calibration set is large. See Vovk et al. (2017) for theoretical justifications. In implementation, we treat _τ_ = 1 for simplicity and better coverage. 

5 

Published as a conference paper at ICLR 2024 

Note that the **u** _[∗]_ is not and does not have to be unique; any solution that satisfies the constraint in Eq. 8 will guarantee multi-step validity (Appendix A). The minimization helps with efficiency, i.e. the sharpness of the confidence regions. We use a gradient descent algorithm for the optimization in implementation (see Appendix B.2 for details, and Appendix C.5 for a study of its effectiveness). Lastly, We obtain ( _s[∗]_ 1 _[, . . . , s][∗] k_[)][ by] _[F]_[ˆ] _[ −] j_[1] ( **u** _[∗] j_[)][ and construct the confidence region for each time step] _j ∈{_ 1 _, . . . , k}_ as the set of all _yj ∈_ R _[d]_ such that the nonconformity score is less than _s[∗] j_[.][Algorithm] 1 summarizes the CoupulaCPTS procedure. 

The full proof of CopulaCPTS’s validity (theorem 4.1) can be found in Appendix A. Intuitively, CopulaCPTS performs conformal prediction twice: first calibrating the nonconformity scores of each time step with _Dcal−_ 1, and then calibrating the copula with _Dcal−_ 2. 

**Theorem 4.1** (Validity of CopulaCPTS) **.** _CopulaCPTS (algorithm 1) produces valid confidence regions for the entire forecast horizon. i.e._ 

P[ _∀j ∈{_ 1 _, . . . , k}, yj ∈_ Γ[1] _j[−][α]_ ] _≥_ 1 _− α._ 

**Algorithm 1:** Copula Conformal Time Series Prediction ( **CopulaCPTS** ) 

**Input:** Dataset _D_ , test inputs _Dtest_ , target significant level 1 _− α_ . **Output:** Γ[1] 1 _[−][α] , . . . ,_ Γ[1] _k[−][α]_ for each test input. 

**1 2** // Training 

**3** Randomly split dataset _D_ into _Dtrain_ and _Dcal_ . 

**4** Train _k_ -step forecasting model _f_[ˆ] on training set _Dtrain_ . 

**5** // Calibration 

**6** Randomly split _Dcal_ into _Dcal−_ 1 and _Dcal−_ 2. **7 for** ( _x[i]_ 1: _t[, y]_ 1: _[i] k_[)] _[ ∈D][cal][−]_[1] _[ ∪D][cal][−]_[2] **[ do] 8** _y_ ˆ1: _[i] k[←][f]_[ˆ][(] _[x]_ 1: _[i] t_[)] **9** _s[i] j[←∥][y] j[i][−][y]_[ˆ] _j[i][∥]_ **[for]** _[ j]_[= 1] _[, . . . , k]_ **10 end for 11** _F_[ˆ] 1 _, . . . , F_[ˆ] _k ←_ Eq. (5) on _Dcal−_ 1 **12** _C_ empirical( _·_ ) _←_ Eq. (7) on _Dcal−_ 2 **13 u** _[∗] ←_ Eq. (8) **14** _s[∗] j_[=] _[F]_[ˆ] _[ −] j_[1] ( **u** _[∗] j_[)] **[ for]** _[ j]_[= 1] _[, . . . , k]_ **15** // Prediction **16 for** _x[i]_ 1: _t[∈D][test]_ **[do] 17** _y_ ˆ1: _[i] k[←][f]_[ˆ][(] _[x]_ 1: _[i] t_[)] **18** Γ[1] _j[−][α] ←{y_ : _∥y − y_ ˆ _h[i][∥][< s][∗] j[}]_ **[ for]** _[ j]_[= 1] _[, . . . , k]_ **19 yield** Γ[1] 1 _[−][α] , . . . ,_ Γ[1] _k[−][α]_ **20 end for** 

## 5 EXPERIMENTS 

In this section, we show that CopulaCPTS produces more calibrated and efficient confidence regions compared to existing methods on two synthetic datasets and two real-world datasets. We demonstrate that CopulaCPTS’s advantage is more evident over longer prediction horizons in Section 5.2. We also show its effectiveness in the autoregressive prediction setting in Section 5.2. 

All experiments in this paper split the calibration set in half into equal-sized _Dcal−_ 1 and _Dcal−_ 2. Although the split does not significantly impact the result when calibration data is ample, performance deteriorates when there are not enough data in either one of the subsets. 

**Baselines.** We compare our model with three representative works in different paradigms of deep uncertainty quantification: the Bayesian-motivated Monte Carlo dropout RNN ( **MC-dropout** ) by Gal & Ghahramani (2016a), the frequentist blockwise jackknife RNN ( **BJRNN** ) by Alaa & Van Der Schaar (2020), a conformal forecasting RNN ( **CF-RNN** ) by Stankeviciˇ ut¯ e et al. (2021),˙ and 

6 

Published as a conference paper at ICLR 2024 

Table 1: Performance in synthetic and real-world datasets with target confidence 1 _− α_ = 0 _._ 9. Methods that are _invalid_ (coverage below 90%) are greyed out. CopulaCPTS achieves high level of calibration (coverage is close to 90%) while producing more efficient confidence regions. 

|||MC-dropout<br>BJRNN<br>CF-RNN<br>Copula<br>CopulaCPTS|
|---|---|---|
|Particle Sim<br>(_σ_ =_._01)<br>Cov<br>91.5 _±_2.0<br>98.9 _±_0.2<br>97.3 _±_1.2<br>86.9 _±_1.9<br>**91.3**<br>_±_1.5<br>Area<br>2.22 _±_0.05<br>2.24 _±_0.59<br>1.97 _±_0.4<br>0.63 _±_0.07<br>**1.08** _±_0.14|||
|Particle Sim<br>(_σ_ =_._05)|Cov<br>Area|46.1 _±_3.7<br>100.0 _±_0.0<br>94.5 _±_1.5<br>88.6 _±_1.7<br>**90.6** _±_0.6<br>2.16 _±_0.08<br>12.13 _±_0.39<br>5.80 _±_0.52<br>4.67 _±_0.16<br>**5.27**<br>_±_1.02|
|Drone Sim<br>(_σ_ =_._02)|Cov<br>Vol|84.5 _±_10.8<br>90.8 _±_2.8<br>91.6 _±_9.2<br>89.2 _±_1.3<br>**90.0** _±_0.8<br>9.64 _±_2.13<br>49.57 _±_3.77<br>32.18 _±_13.66<br>16.92 _±_8.9<br>**17.12** _±_6.93|
|COVID-19<br>Daily Cases<br>Cov<br>19.1 _±_5.1<br>79.2 _±_30.8<br>95.4 _±_1.9<br>90.8 _±_1.4<br>**90.5** _±_1.6<br>Area<br>34.14 _±_0.84<br>823.3 _±_529.7<br>610.2 _±_96.0<br>414.42 _±_5.08<br>**408.6** _±_65.8|||
|Argoverse<br>Trajectory|Cov<br>Area|27.9 _±_3.1<br>92.6 _±_9.2<br>98.8 _±_1.9<br>89.7 _±_0.9<br>**90.2** _±_0.1<br>127.6 _±_20.9<br>880.8 _±_156.2<br>396.9 _±_18.67<br>107.2 _±_9.56<br>**126.8** _±_12.22|



the multi-target copula algorithm that does not have the two step calibration ( **Copula** ) by Messoudi et al. (2021). We use the same underlying prediction model for post-hoc uncertainty quantification methods BJRNN, CF-RNN, and CopulaCPTS. The MC-dropout RNN is of the same architecture but is trained separately, as it requires an extra dropout step during training and inference. 

**Metrics.** We evaluate calibration and efficiency for each method. For calibration, we report the empirical coverage on the test set. Coverage should be as close to the desired confidence level 1 _− α_ as possible. Coverage is calculated as: 

Coverage1 _−α_ = E _x,y∼Z_ P[ **y** _∈_ Γ[1] _[−][α]_ ( _x_ )] _≈ |Dtest_ 1 _|_ � _x[i] ,y[i] ∈|Dtest|_[1][(] _[y][i][∈]_[Γ][1] _[−][α]_[(] _[x][i]_[))][.] 

For efficiency, we report the average area (2D) or volume (3D) of the confidence regions. The measure should be as small as possible while being valid (coverage maintains above-specified confidence level). The area or volume is calculated as: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0007-07.png)


## 5.1 SYNTHETIC DATASETS 

We first test the effectiveness of our models on two synthetic spatiotemporal datasets - interacting particle systems (Kipf et al., 2018), and drone trajectory following simulated with PythonRobotics (Sakai et al., 2018). For particle simulation, we predict **y** _t_ +1: _t_ + _h_ where _t_ = 35, _h_ = 25 and _yt ∈_ R[2] ; for drone simulation _t_ = 60, _h_ = 10, and _yt ∈_ R[3] . To add randomness to the tasks, we added Gaussian noise of _σ_ = _._ 01 and _._ 05 to the dynamics of particle simulation and _σ_ = _._ 02 to drone dynamics. We generate 5000 samples for each dataset, and split the data by 45/45/10 for train, calibration, and test, respectively. For baselines that does not require calibration, the calibration split is used for training the model. Please see Appendix C.1 for forecaster model details. 

We visualize the calibration and efficiency of the methods in Figure 3 for confidence levels 1 _−α_ = 0 _._ 5 to 0 _._ 95. We can see that Copula-RNN, the red lines, are more calibrated and efficient compared to other baseline methods, especially when the confidence level is high (90% and 95%). We can see that for harder tasks (particle _σ_ = 0 _._ 05, and drone trajectory prediction), MC-Dropout is overconfident, whereas BJ-RNN and CF-RNN produce very large (hence inefficient) confidence regions. This behavior of CF-RNN is expected because they apply Bonferroni correction to account for joint prediction for multiple time steps, which is an upper bound of copula functions. Numerical results for confidence level 90% are presented in Table 1. A qualitative comparison of confidence regions for drone simulation can be found in Figure 9 in Appendix C.4. 

## 5.2 REAL WORLD DATASETS 

**COVID-19.** We replicate the experiment setting of Stankeviciˇ ut¯ e et al. (2021) and predict new daily˙ cases of COVID-19 in regions of the UK. The models take 100 days of data as input and forecast 50 days into the future. We used 200 time series for training, 100 for calibration, and 80 for testing. 

7 

Published as a conference paper at ICLR 2024 

Figure 3: Calibration (upper row) and efficiency (lower row) comparison on different 1 _− α_ levels for synthetic data sets. Shaded regions are _±_ 2 standard deviations over 3 runs. For calibration, the goal is to stay above the green dotted (validity) and coincide as closely as possible (calibration). CopulaCPTS is more calibrated across different significance levels. For efficiency, we want the metric to be small. CopulaCPTS outperforms the baselines consistently. (MC-dropout for the right two experiments produces invalid regions, so we don’t consider its efficiency.) 

**Vehicle trajectory prediction.** The Argoverse autonomous vehicle motion forecasting dataset (Chang et al., 2019) is a widely used vehicle trajectory prediction benchmark. The task is to predict 3 second trajectories based on all vehicle motion in the past 2 seconds sampled at 10Hz. Because trajectory prediction is a challenging task, we utilize a state-of-the-art prediction algorithm LaneGCN (Liang et al., 2020) as the underlying model for both CF-RNN and Copula-RNN (details in Appendix C.1). Flexibility of underlying forecasting model is an advantage of post-hoc UQ methods such as conformal prediction. For model-dependent baselines MC-dropout and BJRNN, we have to train an RNN forecasting model from scratch for each method, which induces additional computational cost. 

CopulaCPTS is both more calibrated and efficient compared to baseline models for real-world datasets (Table 1). The Covid-19 dataset demonstrates a potential failure case for our model when calibration data are scarce. Because there are only 100 calibration data, CDF and copula estimations are more stochastic depending on the dataset split, resulting in 1 case of invalidity among 3 experiment trials. Even so, CopulaCPTS shows strong performance on average by remaining valid and reducing the confidence width by 33%. For the trajectory prediction task, learning the copula results in a 40% sharper confidence region while still remaining valid for the 90% confidence interval. We visualize two samples from each dataset in Figure 3.The importance of efficiency in these scenarios is clear - the confidence regions need to be narrow enough for them to be useful for decision making. Given the same underlying prediction model, we can see that CopulaCPTS produces a much more efficient region while still remaining valid. 

**Comparison of models at different horizon lengths.** CopulaCPTS is an algorithm designed to produce calibrated and efficient confidence regions for multi-step time series. When the prediction horizon is long, CopulaCPTS’s advantage is more pronounced. Figure 5 shows the performance comparison over increasing time horizons on the particle dataset. See Table 3 of Appendix C for numerical results. CopulaCPTS achieves a 30% decrease in area at 20 time steps compared to CF-RNN, the best performing baseline; the decrease is above 50% at 25 time steps. This experiment shows significant improvement of using copula to model the joint distribution of future time steps. 

8 

Published as a conference paper at ICLR 2024 

Figure 4: Illustrations of 90% confidence regions given by CF-RNN (blue) and CopulaCPTS (orange) on two real-world datasets, COVID-19 forecast (left 2) and Argoverse (right 2 at time steps 1, 10, 20, and 30). For the Argoverse data, The red dotted lines (ego agent) and blue dotted lines (other agents) are input to the underlying prediction model and the red solid lines are the prediction output. Note that the confidence region produced CF-RNN is uninformatively large, as it covers all the lanes: these examples illustrate the importance of efficiency. Overall, CopulaCPTS is able to produce much more efficient confidence regions while maintaining valid coverage. 

**CopulaCPTS for Autoregressive prediction.** The autoregressive extension of CopulaCPTS is illustrated in detail in Appendix B.3. To provide preliminary evidence of effectiveness, we present test results on the COVID-19 dataset. We train an RNN model with _k_ = 7 and use it to autoregressively forecast the next 14 steps. Table 2 compares the performance of re-estimating the copula for each 7-step forecasts versus using a fixed copula calibrated using the first 7 steps. We also compare the model to a 14-step joint forecaster using CopulaCPTS. It is evident that daily cases of the pandemic is a non-stationary time series, where re-estimating the copula is necessary for validity. 

|Method<br>~~c.cz_:eyHT_FHRHEReeEmaeowomoeovraemmeeeeTTTTee~~|Coverage<br>~~c.cz_:eyHT_FHRHEReeEmaeowomoeovraemmeeeeTTTTee~~|Area<br>~~c.cz_:eyHT_FHRHEReeEmaeowomoeovraemmeeeeTTTTee~~|
|---|---|---|
|AR re-estimate<br>~~c.cz_:eyHT_FHRHEReeEmaeowomoeovraemmeeeeTTTTee~~|**90.1**<br>~~c.cz_:eyHT_FHRHEReeEmaeowomoeovraemmeeeeTTTTee~~|**89.4**<br>~~c.cz_:eyHT_FHRHEReeEmaeowomoeovraemmeeeeTTTTee~~|
|AR fixed|88.2|75.9|
|Joint|90.7|102.3|



Figure 5: CopulaCPTS remains more calibrated and efficient than baselines over increasing forecast horizons. 

Table 2: Performance of autoregressive (AR) CopulaCPTS. Re-estimating copula gives us valid confidence region over time and is more efficient than joint CopulaCPTS forecast. 

## 6 CONCLUSION AND DISCUSSION 

In this paper, we present CopulaCPTS, a conformal prediction algorithm for multi-step time series prediction. CopulaCPTS significantly improves calibration and efficiency of multi-step conformal confidence intervals by incorporating copulas to model the joint distribution of the uncertainty at each time step. We prove that CopulaCPTS has a finite sample validity guarantee over the entire prediction horizon. Our experiments show that CopulaCPTS produces confidence regions that are (1) valid, and (2) more efficient than state-of-the-art UQ methods on all 4 benchmark datasets, and over varying prediction horizons. The improvement is especially pronounced when the data dimension is high or the prediction horizon is long, cases when other methods are prone to be highly inefficient. Hence, we argue that our method is a practical and effective way to produce useful uncertainty quantification for machine learning forecasting models. 

The limitations of our algorithm are as follows. As CopulaCPTS requires two calibration steps, it is suitable only when there are abundant data for calibration. The validity proof relies on using the empirical copula, so it does not apply to other learnable copula classes. Future work includes (1) improving the autoregressive extension of CopulaCPTS, to achieve coverage over the whole horizon, and (2) developing online settings of CopulaCPTS for decision making. 

9 

Published as a conference paper at ICLR 2024 

## ACKNOWLEDGEMENT 

This work was supported in part by Army-ECASE award W911NF-23-1-0231, the U.S. Department Of Energy, Office of Science under #DE-SC0022255, IARPA HAYSTAC Program, CDC-RFA-FT23-0069, NSF Grants #2205093, #2146343, and #2134274. 

We would like to thank Bo Zhao for her helpful comments on the paper. 

## REFERENCES 

- Ahmed Alaa and Mihaela Van Der Schaar. Frequentist uncertainty in recurrent neural networks via blockwise influence functions. In _International Conference on Machine Learning_ , pp. 175–190. PMLR, 2020. 

- Anastasios N Angelopoulos and Stephen Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. _arXiv preprint arXiv:2107.07511_ , 2021. 

- Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra. Weight uncertainty in neural network. In _International conference on machine learning_ , pp. 1613–1622. PMLR, 2015. 

- Ming-Fang Chang, John W Lambert, Patsorn Sangkloy, Jagjeet Singh, Slawomir Bak, Andrew Hartnett, De Wang, Peter Carr, Simon Lucey, Deva Ramanan, and James Hays. Argoverse: 3d tracking and forecasting with rich maps. In _Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2019. 

- Tianqi Chen, Emily Fox, and Carlos Guestrin. Stochastic gradient hamiltonian monte carlo. In _International conference on machine learning_ , pp. 1683–1691. PMLR, 2014. 

- Alexandre Drouin, Etienne Marcotte, and Nicolas Chapados.[´] Tactis: Transformer-attentional copulas for time series. _arXiv preprint arXiv:2202.03528_ , 2022. 

- Bradley Efron and Trevor Hastie. _Computer Age Statistical Inference_ , volume 5. Cambridge University Press, 2016. 

- Martin Eklund, Ulf Norinder, Scott Boyer, and Lars Carlsson. The application of conformal prediction to the drug discovery process. _Annals of Mathematics and Artificial Intelligence_ , 74(1):117–132, 2015. 

- Yarin Gal and Zoubin Ghahramani. Dropout as a bayesian approximation: Representing model uncertainty in deep learning. In _international conference on machine learning_ , pp. 1050–1059. PMLR, 2016a. 

- Yarin Gal and Zoubin Ghahramani. A theoretically grounded application of dropout in recurrent neural networks. _Advances in neural information processing systems_ , 29, 2016b. 

Yarin Gal, Jiri Hron, and Alex Kendall. Concrete dropout. In _NIPS_ , pp. 3581–3590, 2017. 

- Jan Gasthaus, Konstantinos Benidis, Yuyang Wang, Syama Sundar Rangapuram, David Salinas, Valentin Flunkert, and Tim Januschowski. Probabilistic forecasting with spline quantile function RNNs. In _AISTATS 22_ , pp. 1901–1910, 2019. 

- Isaac Gibbs and Emmanuel Candes. Adaptive conformal inference under distribution shift. _Advances in Neural Information Processing Systems_ , 34, 2021. 

- Alex Graves. Practical variational inference for neural networks. _Advances in neural information processing systems_ , 24, 2011. 

- Chancellor Johnstone and Bruce Cox. Conformal uncertainty sets for robust optimization. In _Conformal and Probabilistic Prediction and Applications_ , pp. 72–90. PMLR, 2021. 

- Kelvin Kan, Franc¸ois-Xavier Aubet, Tim Januschowski, Youngsuk Park, Konstantinos Benidis, Lars Ruthotto, and Jan Gasthaus. Multivariate quantile function forecaster. In _International Conference on Artificial Intelligence and Statistics_ , pp. 10603–10621. PMLR, 2022. 

10 

Published as a conference paper at ICLR 2024 

- Abbas Khosravi, Saeid Nahavandi, Doug Creighton, and Amir F Atiya. Comprehensive review of neural network-based prediction intervals and new advances. _IEEE Transactions on neural networks_ , 22(9):1341–1356, 2011. 

- Byol Kim, Chen Xu, and Rina Barber. Predictive inference is free with the jackknife+-after-bootstrap. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), _Advances in Neural Information Processing Systems_ , volume 33, pp. 4138–4149. Curran Associates, Inc., 2020. 

Durk P Kingma, Tim Salimans, and Max Welling. Variational dropout and the local reparameterization trick. _Advances in neural information processing systems_ , 28, 2015. 

Thomas Kipf, Ethan Fetaya, Kuan-Chieh Wang, Max Welling, and Richard Zemel. Neural relational inference for interacting systems. _arXiv preprint arXiv:1802.04687_ , 2018. 

- Danijel Kivaranovic, Kory D Johnson, and Hannes Leeb. Adaptive, distribution-free prediction intervals for deep networks. In _AISTATS_ , pp. 4346–4356, 2020. 

- Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. _Advances in neural information processing systems_ , 30, 2017. 

- Jing Lei and Larry Wasserman. Distribution free prediction bands. _arXiv preprint arXiv:1203.5422_ , 2012. 

- Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J Tibshirani, and Larry Wasserman. Distribution-free predictive inference for regression. _Journal of the American Statistical Association_ , 113(523): 1094–1111, 2018. 

- Ming Liang, Bin Yang, Rui Hu, Yun Chen, Renjie Liao, Song Feng, and Raquel Urtasun. Learning lane graph representations for motion forecasting. In _European Conference on Computer Vision_ , pp. 541–556. Springer, 2020. 

- Christos Louizos and Max Welling. Multiplicative normalizing flows for variational bayesian neural networks. In _International Conference on Machine Learning_ , pp. 2218–2227. PMLR, 2017. 

- Rachel Luo, Shengjia Zhao, Jonathan Kuck, Boris Ivanovic, Silvio Savarese, Edward Schmerling, and Marco Pavone. Sample-efficient safety assurances using conformal prediction. _arXiv preprint arXiv:2109.14082_ , 2021. 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Copula-based conformal prediction for multi-target regression. _Pattern Recognition_ , 120:108101, 2021. 

- Soundouss Messoudi, Sebastien Destercke, and Sylvain Rousseau.´ Ellipsoidal conformal inference for multi-target regression. In _Conformal and Probabilistic Prediction with Applications_ , pp. 294–306. PMLR, 2022. 

- Radford M Neal. _Bayesian learning for neural networks_ , volume 118. Springer Science & Business Media, 2012. 

- Youngsuk Park, Danielle Maddix, Franc¸ois-Xavier Aubet, Kelvin Kan, Jan Gasthaus, and Yuyang Wang. Learning quantile functions without quantile crossing for distribution-free time series forecasting. In _International Conference on Artificial Intelligence and Statistics_ , pp. 8127–8150. PMLR, 2022. 

- Yaniv Romano, Evan Patterson, and Emmanuel Candes. Conformalized quantile regression. _Advances in neural information processing systems_ , 32, 2019. 

- Ludger Ruschendorf. Asymptotic distributions of multivariate rank order statistics. _The Annals of Statistics_ , pp. 912–923, 1976. 

- Atsushi Sakai, Daniel Ingram, Joseph Dinius, Karan Chawla, Antonin Raffin, and Alexis Paques. Pythonrobotics: a python code collection of robotics algorithms. _CoRR_ , abs/1808.10703, 2018. 

11 

Published as a conference paper at ICLR 2024 

- David Salinas, Michael Bohlke-Schneider, Laurent Callot, Roberto Medico, and Jan Gasthaus. Highdimensional multivariate forecasting with low-rank gaussian copula processes. _Advances in neural information processing systems_ , 32, 2019. 

- Martim Sousa, Ana Maria Tome,´ and Jose´ Moreira. A general framework for multi-step ahead adaptive conformal heteroscedastic time series forecasting. _arXiv preprint arXiv:2207.14219_ , 2022. 

- Kamile Stankevi˙ ciˇ ut¯ e, Ahmed Alaa, and Mihaela van der Schaar.˙ Conformal time-series forecasting. In _Advances in Neural Information Processing Systems_ , 2021. 

- Natasa Tagasovska and David Lopez-Paz. Single-model uncertainties for deep learning. In _NeurIPS_ , pp. 6417–6428, 2019. 

- Ichiro Takeuchi, Quoc Le, Timothy Sears, Alexander Smola, et al. _Nonparametric quantile estimation_ . MIT Press, 2006. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ . Springer Science & Business Media, 2005. 

- Vladimir Vovk, Jieli Shen, Valery Manokhin, and Min-ge Xie. Nonparametric predictive distributions based on conformal prediction. In _Conformal and probabilistic prediction and applications_ , pp. 82–102. PMLR, 2017. 

- Bin Wang, Jie Lu, Zheng Yan, Huaishao Luo, Tianrui Li, Yu Zheng, and Guangquan Zhang. Deep uncertainty quantification: A machine learning approach for weather forecasting. In _Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining_ , pp. 2087–2095, 2019. 

- Max Welling and Yee W Teh. Bayesian learning via stochastic gradient langevin dynamics. In _ICML_ , pp. 681–688, 2011. 

- Dongxia Wu, Liyao Gao, Matteo Chinazzi, Xinyue Xiong, Alessandro Vespignani, Yi-An Ma, and Rose Yu. Quantifying uncertainty in deep spatiotemporal forecasting. In _Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining_ , pp. 1841–1851, 2021. 

- Chen Xu and Yao Xie. Conformal prediction interval for dynamic time-series. In _International Conference on Machine Learning_ . PMLR, 2021. 

- Bianca Zadrozny and Charles Elkan. Obtaining calibrated probability estimates from decision trees and naive bayesian classifiers. In _Icml_ , volume 1, pp. 609–616. Citeseer, 2001. 

- Margaux Zaffran, Olivier Feron,´ Yannig Goude, Julie Josse, and Aymeric Dieuleveut. Adaptive conformal predictions for time series. In _International Conference on Machine Learning_ , pp. 25834–25866. PMLR, 2022. 

12 

Published as a conference paper at ICLR 2024 

## A PROOF OF THEOREM 4.1 

**Theorem A.1** (Validity of CopulaCPTS) **.** _The confidence region provided by CopulaCPTS (algorithm 1) is valid. i.e._ P[ _∀j ∈{_ 1 _, . . . , k}, yt_ + _j ∈_ Γ[1] _j[−][α]_ ] _≥_ 1 _− α._ 

_Proof._ Define notations to be the same as in Section 4. Let _D_ = _{z[i]_ = ( _x[i] , y[i]_ ) _}[n] i_ =1[be a dataset] with input _x[i] ∈_ R _[t][×][d]_ , a time series with length _t_ , and output _y[i] ∈_ R _[k][×][d]_ a time series with length _k_ . Each data sample (of entire time series, not time step) _z[i]_ = ( _x[i] , y[i]_ ) is drawn i.i.d. from an unknown distribution _Z_ . This means that any other sample drawn _Z_ is _exchangeable_ with _D_ . from Dataset _D_ is divided into training set _Dtrain_ and two calibration sets _Dcal−_ 1 and _Dcal−_ 2. 

We have nonconformity score function _A_ with prediction model _f_[ˆ] trained on _Dtrain_ . For each data point _z[i]_ = ( _x[i] , y[i]_ ) _∈Dcal_ , we calculate the nonconformity score for each time step _j_ , concatenating them into a vector _s[i]_ of dimension _k_ . 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-05.png)


Let _S_ 1 = _{s[i] }zi∈Dcal−_ 1 be the set of nonconformity scores of data in _Dcal−_ 1 and _S_ 2 = _{s[i] }zi∈Dcal−_ 2 the set of nonconformity scores of data in _Dcal−_ 2. Subscript _j_ will be used to index the set of specific time steps of the scores: _S_ 1 _j_ = _{s[i] j[}][z][i][∈D] cal−_ 1[,] _[ S]_[2] _[j]_[=] _[ {][s][i] j[}][z][i][∈D] cal−_ 2[.] 

**CDF Estimation on** _Dcal−_ 1 **.** We use _Dcal−_ 1 to build conformal predictive distributions (CPD) (Vovk et al., 2017) for each time step’s anomaly scores. The cumulative distribution function is constructed as: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-08.png)


**Lemma A.2** (Validity of CPD. Theorem 11 of Vovk et al. (2017) ) **.** _Given a nonconformity score function A_ : _Z →_ R _and a data sample z ∼Z, calculate the nonconformity score as s_ = _A_ ( _z_ ) _. Then, the distribution F_[ˆ] _j_ ( _·_ ) _is valid in the sense that_ P _Z_ [ _F_[ˆ] _j_ ( _sj_ ) _≤_ 1 _− α_ ] = 1 _− α, for any_ 0 _< α <_ 1 _._ 

**Copula Calibration on** _Dcal−_ 2 **.** Next, for every data point _Dcal−_ 2, we calculate 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-11.png)


Each **u** _[i]_ can be seen as a _multivariate nonconformity score_ for data sample _z[i]_ . We will now illustrate that an empirical copula on _U_ is a rank statistic, and hence we can apply the proof of conformal prediction to prove a finite sample validity guarantee. 

**Definition A.3** (Vector partial order) **.** Define a partial order for _k_ -dimensional vectors _⪯_ . 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-14.png)



![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-15.png)


Next, we define an empirical multivariate quantile function for _U_ , a set of _k_ -dimensional vectors, based on the partial order defined in Eqn 11.[2] 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-17.png)


The empirical copula formula in CopulaCPTS (Eqn 7 in section 4.1) is the same as the expression inside the inf function of _Q_ (1 _− α, U ∪{_ _**∞** }_ ). Therefore, finding _s[∗]_ 1 _[, . . . , s][∗] k_[by Equation 8 implies:] 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0013-19.png)


> 2There exist other definitions of multivariate quantiles, but they cannot be used in place of our definition in this proof. We have chosen this form because it connects directly to the empirical copula. 

13 

Published as a conference paper at ICLR 2024 

The rest of the proof follows that of Inductive Conformal Prediction (ICP) in Vovk et al. (2005). Given a test data sample _z[n]_[+1] = ( _x[n]_ 1:[+1] _t[, y]_ 1: _[n]_[+1] _k_[)] _[ ∼Z]_[, we want to prove that the confidence regions] Γ[1] 1 _[−][α] , . . . ,_ Γ[1] _k[−][α]_ output by CopulaCPTS satisfies: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-02.png)


We first calculate 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-04.png)


Let **u** _[∗]_ = _Q_ (1 _− α, U ∪{_ _**∞** }_ ), **u** _[∗] ∈_ [0 _,_ 1] _[k]_ . An important observation for the conformal prediction proof is that if **u** _[∗] ⪯_ **u** _[n]_[+1] , then 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-06.png)


the quantile remains unchanged. This fact can be re-written as 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-08.png)


The above describes the condition where **u** _[n]_[+1] is among the _⌈_ (1 _− α_ )( _n_ + 1) _⌉_ smallest of _U_ . By exchangability, the probability of **u** _[n]_[+1] ’s rank among _U_ is uniform. Therefore, 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-10.png)


Hence we have 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-12.png)


Note again that: 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-14.png)


- The uncertain regions are constructed as (Algorithm 1, line 17): 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-16.png)


By definition of _⪯_ , we have 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-18.png)



![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-19.png)



![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-20.png)



![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-21.png)


Combining Eqn 14 and Eqn 19, we have 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0014-23.png)


14 

Published as a conference paper at ICLR 2024 

## B ADDITIONAL ALGORITHM DETAILS 

## B.1 UPPER AND LOWER BOUNDS FOR COPULAS 

To provide a better understanding of the properties of Copulas, consider the Frechet-Hoeffding Bounds (Theorem B.1). In fact, the Frechet-Hoeffding upper- and lower- bounds are both copulas. The lower bound is precisely the Bonferroni correction used in Stankeviciˇ ut¯ e et al. (2021) - therefore˙ by estimating the copula more precisely instead of using a lower bound, we have a guaranteed efficiency improvement for the confidence region. 

**Theorem B.1** (The Frechet-Hoeffding Bounds) **.** _Consider a copula C_ ( _u_ 1 _, . . . , uk_ ) _. Then_ 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0015-05.png)


## B.2 NUMERICAL OPTIMIZATION WITH SGD FOR SEARCH 

We continue to use the notation defined in Appendix A. The inverse of the predictive distributions (Equation 10) can be written as follows, similar to the empirical quantile function (Equation 3). 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0015-08.png)


We find the optimal _s[∗] j_[in Equation 8 and Algorithm 1 by minimizing the following loss:] 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0015-10.png)


The indicator function is implemented using a sigmoid function whose input is multiplied by a constant for differentiability. A small amount of L2 regularization is added to the loss function to ensure the searched scores are as low as possible. We use the Adam optimizer and perform gradient descent for 500 steps to get the final result. The optimization process to find **s** _[∗]_ typically takes a few seconds on CPU. For each run of our experiments, the calibration and prediction steps of CopulaCPTS combined took less than 1 minute to run on an Apple M1 CPU. Please refer to the CP class in the reference code for implementation details. 

## B.3 COPULACPTS IN AUTO-REGRESSIVE FORECASTING 

Auto-regressive forecasting is a common framework in time series forecasting. So far, we have been looking at forecasts for a predetermined number of time steps _k_ . One can use a fixed-length model to forecast variable horizons _k[′]_ autoregressively, taking the model output as part of the input. In the conformal prediction setting, we want not only to autoregressively use the point forecasts, but also to propagate the uncertainty measurement. 

If the time series and uncertainty are _stationary_ (for example additive Gaussian noise), the copula remains the same for any sliding window of _k_ steps, i.e. _C_ ( _u_ 1 _, . . . , uk_ ) = _C_ ( _u_ 2 _, . . . , uk_ +1). Therefore, after finding ( _u[∗]_ 1 _[, . . . , u][∗] k_[)][ such that] _[ C]_[(] _[u]_ 1 _[∗][, . . . , u][∗] k_[)] _[≥]_[1] _[ −][α]_[, we can simply search for] _[ u][∗] k_ +1 such that _C_ ( _u[∗]_ 2 _[, . . . , u][∗] k[, u][∗] k_ +1[)] _[≥]_[1] _[ −][α]_[.][The guarantee proven in Theorem 4.1 still holds for the] new estimate. In this way, we can achieve the coverage guarantee over the entire autoregressive forecasting horizon. 

On the other hand, if the time series is _non-stationary_ , we need to fit copulas _C_ 1( _u_ 1 _, . . . , uk_ ), _C_ 2( _u_ 2 _, . . . , uk_ +1), _. . . , Ck′−k_ ( _uk′−k, . . . , uk′_ ), one for each autoregressive prediction, which requires a calibration set with _≥ k[′]_ time steps. The _k[′]_ step autoregressive problem is then reduced to _k[′] − k_ multi-step forecasting problems that can be solved by CopulaCPTS. It follows that each of the autoregressive predictions is valid. Appendix B.4 provides an example scenario where re-estimating the copula is necessary for validity. 

15 

Published as a conference paper at ICLR 2024 

## B.4 AUTOREGRESSIVE PREDICTION 

In the context of this paper to forecast autoregressively is given input **x** 1: _t_ and a _k_ step forecasting model _f_[ˆ] , perform prediction 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0016-03.png)


until all _k[′]_ time steps are predicted. 

We now provide a toy scenario to illustrate when re-estimating the copula is necessary and improves validity. Consider a time series of three time steps _t_ 0 _, t_ 1 _, t_ 2. The two scenarios are illustrated in Figure 6. In both scenarios, the mean and variance of all time steps are 0 and 1 respectively. In scenario (a), _t_ 0 = _t_ 1 and hence their covariance is 1. The copula estimated on _t_ 0 and _t_ 1 is _C_ 0:1( _F_ ( _t_ 0) _, F_ ( _t_ 1)) = _F_ ( _t_ 0) = _F_ ( _t_ 1). This copula will significantly underestimate the confidence region of _t_ 2 where its covariance with _t_ 1 is _−_ 1. In fact the coverage of _C_ 0:1( _F_ 1( _t_ 1) _, F_ 2( _t_ 2)) = 0 _._ 74. On the other hand, (b) illustrates a scenario where the copula for any 2 consecutive time series remains the same _C_ 0 = _C_ 1. In this case, applying _C_ 0 directly to forecast _C_ 1 achieves precisely 90% coverage. 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0016-06.png)


**----- Start of picture text -----**<br>
(a) Time steps 0 and 1 are positively corre- (b) Stationary time series where each time<br>lated while 1 and 2 are negatively correlated steps are uncorrelated<br>**----- End of picture text -----**<br>


Figure 6: Two scenarios to illustrate the autoregressive case 

## C EXPERIMENT DETAILS AND ADDITIONAL RESULTS 

## C.1 UNDERLYING FORECASTING MODELS 

**Particle Dataset.** The underlying forecasting model for the particle experiments is an 1-layer LSTM network with embedding size = 24. The hidden state is then passed through a linear network to forecast the timesteps concurrently (output has dimension _k × dy_ ). We train the model for 150 epochs with batch size 128. Hyperparameters of the network are selected through a model search by performance on a 5-fold cross-validation split of the dataset. The architecture and hyperparameters are shared for all baselines and CopulaCPTS in Table 1. 

**Drone.** For the drone trajectory forecasting task, we use the same LSTM forecasting network as the particle dataset, but with its hidden size increased to 128. We train the model for 500 epochs with batch size 128. The same architecture and hyperparameters are shared for all baselines and CopulaCPTS reported in Table 1. 

**Covid-19.** The COVID-19 dataset is downloaded directly from the official UK government website https://coronavirus.data.gov.uk/details/download by selecting _region_ for area 

16 

Published as a conference paper at ICLR 2024 

type and _newCasesByPublishDate_ for metric. There are in total 380 regions and over 500 days of data, depending on when it is downloaded. We selected 150-day time series from the collection to construct our dataset. 

The base forecasting model for Covid-19 dataset is the same as the model for synthetic datasets, with hidden size = 128, and were trained for 150 epochs with batch size 128. The same architecture and hyperparameters are shared for all baselines and CopulaCPTS reported in Table 1. 

**Argoverse.** As highlighted in the main text, we utilize a state-of-the-art prediction algorithm LaneGCN (Liang et al., 2020) as the underlying forecaster model for CF-RNN and Copula-RNN. We refer the readers to their paper and code base for model details. The architecture of the RNN network used for MC-Dropout and BJRNN is an Encoder-Decoder network. Both the encode and decoder contain a LSTM layer with encoding size 8 and hidden size 16. We chose this architecture because the is part of the official Argoverse baselines (https://github.com/jagjeet-singh/argoverse-forecasting) and demonstrates competitive performance. 

## C.2 CALIBRATION AND EFFICIENCY CHART FOR COVID-19 

Figure 7 shows a comparison of calibration and efficiency for the daily new COVID 19 cases forecasting. 

Figure 7: Calibration and efficiency comparison on different _ϵ_ level for COVID-19 Daily Forecasts. The copula methods (orange and red lines) are more calibrated (coinciding with the green dotted line) and sharp (low width) compared to baselines. 

To see if the daily fluctuation due to testing behavior disrupts other methods, we also ran the same experiment on weekly aggregated new cases forecast. We take 14 weeks of data as input and output forecasts for the next 6 weeks. The results are illustrated in Figure 8. The weekly forecasting scenario gives us similar insights as the daily forecasts. 

## C.3 ARGOVERSE 

The Argoverse autonomous vehicle dataset contains 205,942 samples, consisting of diverse driving scenarios from Miami and Pittsburgh. The data can be downloaded from the official Argoverse dataset website. We split 90/10 into a training set and validation set of size 185,348 and 20,594 respectively. The official validation set of size 39,472 is used for testing and reporting performance. We preprocess the scenes to filter out incomplete trajectories and cap the number of vehicles modeled to 60. If there are less than 60 cars in the scenario, we insert dummy cars into them to achieve consistent car numbers. For map information, we only include center lanes with lane directions as features. Similar to vehicles, we introduce dummy lane nodes into each scene to make lane numbers consistently equal to 650. 

17 

Published as a conference paper at ICLR 2024 

Figure 8: Covid Weekly Forecasts 

## C.4 ADDITIONAL EXPERIMENT RESULTS 

We present in Figures 8 and 9 some qualitative results for uncertainty estimation. 

To test how the effects of copulaCPTS compare with baseline on other base forecasters, we also include an encoder-decoder architecture with the same embedding size as the RNN models introduced in Appendix C.1 for each dataset. The results are presented in Table 3. We omit these results in the main text because we found that they did not bring significant improvement to time series forecasting UQ. 

Table 4 compares model performance compared across different prediction horizons. We show that the advantage of our method is more pronounced for longer horizon forecasts. 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0018-06.png)


**----- Start of picture text -----**<br>
(a) Copula-EncDec (b) MC Dropout (c) CF-RNN<br>**----- End of picture text -----**<br>


Figure 9: 99% Confidence region produced by three methods for the drone dataset. Copula methods (a) produce a more consistent, expanding cone of uncertainty compared to MC-Dropout (b) sharper one compared to CF-RNN (c). 

C.5 STUDY ON _αj_ SEARCH 

Figure 11 shows the _αj_ values for each 1 _− αj_ = _F_[ˆ] _j_ ( _s[∗] j_[)][ used in Copula CPTS as outlined in line] 15 of Algorithm 1. We present _αj_ values searched using two methods of searching, with dichotomy search for a constant _α_ value for the horizon as in Messoudi et al. (2021), and by stochastic gradient descent as outlined in section 4.2. 

TheBonferroni Correction used in Stankevi _αj_ values are an indicator of howciˇ ut¯interrelatede et al. (2021) (grey dotted line in Figure 11) assumes that˙ the uncertainty between each time step are: the time steps are independent, with CopulaCPTS we have lower 1 _− αj_ levels while having valid coverage (blue and orange lines in Figure 11). This shows that the uncertainty of the time steps is not independent, and we are able to utilize this dependency to shrink the confidence region while still maintaining the coverage guarantee. 

18 

Published as a conference paper at ICLR 2024 

|Particle Simulation (_σ_ =_._01)|Particle Simulation (_σ_ =_._01)|Particle Simulation (_σ_ =_._01)|
|---|---|---|
||||
||Coverage (90%)<br>Area (90%)|Coverage (99%)<br>Area (99%)|
||||
|MC-dropout<br>BJRNN<br>CF-RNN<br>CF-EncDec<br>Copula-vanilla<br>Copula-RNN<br>Copula-EncDec|691.5 _±_2.0<br>2.22 _±_0.05<br>98.9 _±_0.2<br>2.24 _±_0.59<br>97.1 _±_0.8<br>1.2 _±_0.21<br>97.3 _±_1.2<br>1.97 _±_0.4<br>86.9 _±_1.9<br>0.63 _±_0.07<br>91.3 _±_1.5<br>**1.08** _±_0.14<br>90.8 _±_2.5<br>1.19 _±_0.08|95.2 _±_1.4<br>3.16 _±_0.08<br>99.6 _±_0.3<br>2.75 _±_0.71<br>99.3 _±_0.6<br>3.16 _±_0.86<br>98.9 _±_0.6<br>2.75 _±_0.42<br>91.9 _±_1.8<br>0.76 _±_0.12<br>99.4 _±_0.3<br>2.23 _±_0.19<br>99.3 _±_0.5<br>2.16 _±_0.23|
|Particle Simulation (_σ_ =_._05)|||
||||
||Coverage (90%)<br>Area (90%)|Coverage (99%)<br>Area (99%)|
||||
|MC-dropout<br>BJRNN<br>CF-RNN<br>Copula-vanilla<br>Copula-RNN<br>Copula-EncDec|16.1 _±_4.3<br>0.79 _±_0.02<br>100.0 _±_0.0<br>12.13 _±_0.39<br>94.5 _±_1.5<br>5.79 _±_0.51<br>88.5 _±_1.7<br>4.37 _±_0.16<br>**90.3** _±_0.7<br>4.50 _±_0.07<br>91.4 _±_1.1<br>**4.40** _±_0.15|33.9 _±_5.1<br>2.12 _±_0.03<br>100.0 _±_0.0<br>15.43 _±_0.85<br>99.8 _±_2.2<br>19.21 _±_8.19<br>91.7 _±_1.6<br>4.8 _±_0.18<br>**99.1** _±_0.8<br>12.82 _±_3.98<br>98.7 _±_0.1<br>**9.31** _±_1.97|
|Drone Simulation (_σ_ =_._02)|||
||||
||Coverage (90%)<br>Area (90%)|Coverage (99%)<br>Area (99%)|
||||
|MC-dropout<br>BJRNN<br>CF-RNN<br>CF-EncDec<br>Copula-vanilla<br>Copula-RNN|84.5 _±_10.8<br>9.64 _±_2.13<br>90.8 _±_2.8<br>49.57 _±_3.77<br>91.6 _±_9.2<br>32.18 _±_13.66<br>100.0 _±_0.0<br>21.83 _±_26.29<br>89.5 _±_1.3<br>54.67 _±_28.9<br>**90.0** _±_1.5<br>**16.52** _±_15.08|90.0 _±_7.8<br>16.02 _±_3.62<br>100.0 _±_4.0<br>65.77 _±_4.56<br>100.0 _±_0.0<br>36.79 _±_14.03<br>100.0 _±_0.0<br>25.03 _±_12.53<br>94.5 _±_0.5<br>68.9 _±_33.42<br>**98.5** _±_0.5<br>**21.48** _±_8.91|
|COVID-19 Daily Cases Dataset|||
||||
||Coverage (90%)<br>Area (90%)|Coverage (99%)<br>Area (99%)|
||||
|MC-dropout<br>BJRNN<br>CF-RNN<br>CF-EncDec<br>Copula-vanilla<br>Copula-RNN<br>Copula-EncDec|19.1 _±_5.1<br>34.14 _±_0.84<br>79.2 _±_30.8<br>823.3 _±_529.7<br>95.4 _±_1.9<br>610.2 _±_96.0<br>91.7 _±_1.4<br>570.3 _±_22.1<br>90.8 _±_1.4<br>414.42 _±_5.08<br>92.1 _±_1.0<br>**429.0** _±_15.1<br>**90.8** _±_0.3<br>429.4 _±_27.9|100.0 _±_0.0<br>1106.57 _±_25.41<br>85.7 _±_27.5<br>149187.<br>_±_51044.<br>100.0 _±_0.0<br>121435.<br>_±_26495.<br>100.0 _±_0.0<br>108130.<br>_±_10889.<br>91.2 _±_1.3<br>41346.<br>_±_59.0<br>100.0 _±_0.0<br>88962.<br>_±_9643.<br>100.0 _±_0.0<br>**60852.**<br>_±_12263.|
|Argoverse Trajectory Prediction Dataset|||
||||
||Coverage (90%)<br>Area (90%)|Coverage (99%)<br>Area (99%)|
||||
|MC-dropout<br>BJRNN<br>CF-LaneGCN<br>Copula-vanilla<br>Copula-LaneGCN|27.9 _±_3.1<br>127.6 _±_20.9<br>92.6 _±_9.2<br>880.8 _±_156.2<br>98.8 _±_1.9<br>396.9 _±_18.67<br>89.7 _±_0.9<br>107.2 _±_9.56<br>**90.4** _±_0.3<br>**126.8** _±_12.22|31.5 _±_3.9<br>242.1 _±_54.0<br>100.0 _±_0.0<br>3402.8 _±_268.<br>100.<br>_±_0.2<br>607.2 _±_8.67<br>96.5 _±_2.3<br>289.0 _±_38.1<br>**99.1** _±_0.4<br>**324.1** _±_42.22|



Table 3: Additional results. Copula methods achieve a high level of calibration while producing sharper prediction regions. The sharpness gain is even more pronounced at higher confidence levels (99%), where we want the prediction region to be useful while remaining valid. 

19 

Published as a conference paper at ICLR 2024 

Figure 10: Illustrations for confidence regions given by CF-RNN (blue) and CopulaCPTS (orange) at time steps 0, 10, 20, and 30. Note that in order to achieve 90% coverage, the regions are larger than needed, especially in straight-lane cases like the middle two. Using copulas to couple together time steps results in a much smaller region while achieving similarly good coverage. 

|MC-Dropout<br>BJRNN<br>CF-RNN<br>CF-EncDec<br>Copula-RNN<br>Copula-EncDec|97.8 _±_2.0<br>0.4 _±_0.04<br>45.3 _±_39.4<br>0.27 _±_0.18<br>100.0 _±_0.0<br>**0.01** _±_0.01<br>89.9 _±_19.2<br>**0.01** _±_0.01<br>90.1 _±_0.2<br>**0.01** _±_0.01<br>**90.0** _±_0.3<br>**0.01** _±_0.0|88.0 _±_7.0<br>0.69 _±_0.25<br>97.7 _±_2.1<br>2.69 _±_1.79<br>77.8 _±_19.2<br>0.8 _±_0.64<br>100.0 _±_0.0<br>0.75 _±_0.99<br>89.8 _±_0.6<br>**0.54** _±_0.45<br>**90.3** _±_0.6<br>0.67 _±_1.01|52.3 _±_1.4<br>0.94 _±_0.2<br>95.5 _±_2.8<br>19.99 _±_4.83<br>66.7 _±_0.0<br>18.82 _±_3.73<br>88.9 _±_19.2<br>13.07 _±_16.1<br>**90.1** _±_1.2<br>8.25 _±_3.44<br>90.5 _±_0.5<br>**7.13** _±_9.5|
|---|---|---|---|



Table 4: Performance comparison across different horizons at 90% confidence level on the drone simulation dataset. The improvement on efficiency is more pronounced when the horizon is longer. 

Table 5 shows that there are no significant differences between coverage and area performance for the two search methods within the scope of datasets we study in this paper. However, we want to highlight that SGD search is _O_ ( _n_ ) complexity to optimization steps, regardless of the prediction horizon. SGD also allows for varying _αj_ which might be useful in some settings, for example capturing uncertainty spikes for some time steps as seen in the COVID-19 dataset of Figure 11. Dichotomy search, on the other hand, is _O_ ( _nlog_ ( _n_ )) complexity to the search space depends on granularity, and will be _O_ ( _knlog_ ( _kn_ ) if we want to search for varying _αj_ . 

|Dataset|Coverage (90%)|Coverage (90%)|Area|Area|
|---|---|---|---|---|
||Fixed_αj_|Varying_αj_|Fixed_αj_|Varying_αj_|
|Particle (_σ_ =_._01)|91.7 _±_1.9|91.5 _±_2.1|1.13 _±_0.45|1.06 _±_0.36|
|Particle (_σ_ =_._05)|92.1 _±_1.3|90.3 _±_0.7|4.89 _±_0.05|4.50 _±_0.07|
|Drone|90.3 _±_0.5|90.0 _±_1.5|15.92 _±_1.98|16.52 _±_7.08|
|Covid-19|92.9 _±_0.1|92.1 _±_1.0|498.44 _±_6.36|429.0 _±_15.1|
|Argoverse|90.2 _±_0.1|90.4 _±_0.3|117.1 _±_7.3|126.8 _±_12.2|



Table 5: Coverage and area comparison between stochastic search for fixed _αj_ and SGD for Varying _αj_ . We do not see a significant difference between the performance of the two. 

## C.6 COMPARISON TO ADDITIONAL BASELINES 

We include a comparison to two additional simple UQ baselines on the particle simulation dataset. 

**L2-Conformal.** L2-Conformal uses the same underlying RNN forecaster as CF-RNN and Copula RNN. We use the nonconformity score of the vector norm of all timesteps concatenated together _∥_ ˆ **y** _t_ +1: _t_ + _k −_ **y** _t_ +1: _t_ + _k∥_ to perform ICP. As there are no analytic way to represent a _k × dy_ -dimensional 

20 

Published as a conference paper at ICLR 2024 

Figure 11: Comparison between dichotomy search for fixed _αj_ values (blue) and stochastic gradient search for varying _αj_ (blue) through timesteps. Shaded regions are the standard deviation of the values over 3 runs. 

uncertainty region on 2-D space, we calculate the area and plot the region for L2 Conformal baseline with the maximum deviation at each timestep such that the vector norm still stays within range. 

**Direct Gaussian.** Direct Gaussian uses the same model architecture and training hyperparameters, with the addition of a linear layer that outputs the variance for each timestep, and is optimized using negative log loss, a proper scoring rule for probabilistic forecasting. We obtain the area by analytically calculating the 90% confidence interval for each variable. 

Results in Table 6 show that L2-conformal produces inefficient confidence area, and directly outputting variance under-covers test data. These results align with previous findings and motivate our method, which is both more calibrated and sharper compared to these baselines. We show a visualization in Figure 12 to illustrate the different properties of the methods qualitatively. 

||Particle (_σ_|=_._01)|Particle (_σ_|=_._05)|
|---|---|---|---|---|
|Method|Coverage (90%)|Area_↓_|Coverage (90%)|Area_↓_|
|L2-Conformal|88_._5_±_0_._4|7_._21_±_0_._35|89_._7_±_0_._6|7_._21_±_0_._35|
|Direct Gaussian|11_._9_±_0_._09|0_._07_±_0_._31|0_._0_±_0_._0|0_._08_±_0_._02|
|CF-RNN|97_._0_±_2_._3|3_._13_±_3_._24|97_._0_±_2_._3|5_._79_±_0_._51|
|CopulaCPTS|**91.3**_±_2_._1|**1.08**_±_0_._36|**90.3**_±_0_._7|**4.50**_±_0_._07|



Table 6: Comparison with two additional baselines on the particle dataset. 

**Ellipsoidal conformal inference for Multi-Target Regression** We also compare CopulaCPTS to a newer work, Ellipsoidal CP (Messoudi et al., 2022). The result is presented in Table 7. This method models the uncertainty region of multi-target outputs as a high-dimensional ellipsoid, by estimating a covariance matrix on calibration data. We apply EllipsoidalCP on our data by flattening the time and space dimensions, so the particle simulation, for example, is treated as a multi-target prediction of dim = 50 = 25 (time steps) _×_ 2 (dims) . We see that the results are comparable in our experiment. When the correlation is more pronounced such as in the covid experiment, EllipsoidalCP can capture the correlation better than CopulaCPTS resulting in improved efficiency. On the other hand, the flexibility of our method allows us to achieve better efficiency than that of EllipsoidalCP. A notable concern for using EllipsoidalCP is that for higher output dimensions, the determinant of the covariance matrix can be extremely large (up to 10[50] in our experiments) and can result in numerical instabilities. 

21 

Published as a conference paper at ICLR 2024 


![](markdown_output/copula-conformal-2022_images/copula-conformal-2022.pdf-0022-01.png)


**----- Start of picture text -----**<br>
(a) L2 Conformal (b) Direct RNN Gaussian<br>04<br>03<br>; 02<br>. a1<br>00<br>01<br>0.2<br>03<br>-10 -08 -06 -04 -02 00 02 0.4 12 -10 -08 -06 -04 -02 00<br>(c) CF-RNN (d) Copula-RNN<br>**----- End of picture text -----**<br>


Figure 12: Visualization of on a sample from the Particle dataset’s test set. 

Table 7: Performance comparison with EllipsoidalCP in synthetic and real-world datasets with target confidence 1 _− α_ = 0 _._ 9. 

|||EllipsoidalCP|CopulaCPTS|
|---|---|---|---|
|Particle Sim|cov|**90.1** _±_0.9|91.3 _±_1.5|
|(_σ_ =_._01)|area|**0.84** _±_.005|1.08 _±_0.14|
|Particle Sim|cov|90.8 _±_0.4|**90.6** _±_0.6|
|(_σ_ =_._05)|area|8.76 _±_0.41|**5.27** _±_1.02|
|Drone Sim|cov|90.5 _±_0.2|**90.0** _±_0.8|
|(_σ_ =_._02)|area|28.3 _±_3.1|**17.12** _±_6.93|
|COVID-19|cov|93.3 _±_1.5|**90.5** _±_1.6|
|Daily Cases|area|**231.5** _±_22.4|408.6 _±_65.8|
|Argoverse|cov|90.3 _±_0.1|**90.2** _±_0.1|
|Trajectory|area|144.8 _±_8.1|**126.8** _±_12.2|



22 

