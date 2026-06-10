# Kernel-based Optimally Weighted Conformal Time-Series Prediction 

Jonghyeok Lee[1] , Chen Xu[1] , and Yao Xie[*1] 

1H. Milton Stewart School of Industrial and Systems Engineering, Georgia Institute of Technology. 

## **Abstract** 

In this work, we present a novel conformal prediction method for time-series, which we call Kernel-based Optimally Weighted Conformal Prediction Intervals (KOWCPI). Specifically, KOWCPI adapts the classic Reweighted Nadaraya-Watson (RNW) estimator for quantile regression on dependent data and learns optimal data-adaptive weights. Theoretically, we tackle the challenge of establishing a conditional coverage guarantee for non-exchangeable data under strong mixing conditions on the non-conformity scores. We demonstrate the superior performance of KOWCPI on real and synthetic time-series data against state-of-the-art methods, where KOWCPI achieves narrower confidence intervals without losing coverage. 

## **1 Introduction** 

Conformal prediction, originated in Vovk et al. (1999, 2005), offers a robust framework explicitly designed for reliable and distribution-free uncertainty quantification. Conformal prediction has become increasingly recognized and adopted within the domains of machine learning and statistics (Lei et al., 2013; Lei & Wasserman, 2014; Kim et al., 2020; Angelopoulos & Bates, 2023). Assuming nothing beyond the exchangeability of data, conformal prediction excels in generating valid prediction sets under any given significance level, irrespective of the underlying data distribution and model assumptions. This capability makes it particularly valuable for uncertainty quantification in settings characterized by diverse and complex models. 

Going beyond the exchangeability assumption has been a research challenge, particularly as many real-world datasets (such as time-series data) are inherently non-exchangeable. Tibshirani et al. (2019) addresses situations where a feature distribution shifts between training and test data and restores valid coverage through weighted quantiles based on the likelihood ratio of the distributions. More recently, Barber et al. (2023) bounds the coverage gap using the total variation distance between training and test data points and minimizes this gap using pre-specified data-independent weights. However, it remains open to how to appropriately optimize the weights. 

To advance conformal prediction for time series, we extend the prior sequential predictive approach (Xu & Xie, 2023a,b) by incorporating nonparametric kernel regression into the quantile regression method on non-conformity scores. A key challenge of adapting this method to time-series data lies in selecting optimal weights to accommodate the dependent structure of the data. To ensure valid coverage of prediction 

> *Correspondence: yao.xie@isye.gatech.edu 

1 

sets, it is crucial to select weights inside the quantile estimator so that it closely approximates the true quantile of non-conformity scores. 

In this paper, we introduce KOWCPI, which utilizes the Reweighted Nadaraya-Watson estimator (Hall et al., 1999) to facilitate the selection of data-dependent optimal weights. This approach anticipates that adaptive weights will enhance the robustness of uncertainty quantification, particularly when the assumption of exchangeability is compromised. Our method also addresses the weight selection issue in the weighted quantile method presented by Barber et al. (2023), as KOWCPI allows for the calculation of weights in a data-driven manner without prior knowledge about the data. 

In summary, our main contributions are: 

- We propose KOWCPI, a sequential time-series conformal prediction method that performs nonparametric kernel quantile regression on non-conformity scores. In particular, KOWCPI learns optimal data-driven weights used in the conditional quantiles. 

- We prove the asymptotic conditional coverage guarantee of KOWCPI based on the classical theory of nonparametric regression. We further obtain the marginal coverage gap of KOWCPI using the general result for the weights on quantile for non-exchangeable data. 

- We demonstrate the effectiveness of KOWCPI on real time-series data against state-of-the-art baselines. Specifically, KOWCPI can achieve the narrowest width of prediction intervals without losing marginal and approximate conditional (i.e., rolling) coverage empirically. 

## **1.1 Literature** 

**RNW quantile regression** In Hall et al. (1999), the Reweighted Nadaraya-Watson (RNW, often referred to as Weighted or Adjusted Nadaraya-Watson) estimator was suggested as a method to estimate the conditional distribution function from time-series data. This estimator extends the renowned NadarayaWatson estimator (Nadaraya, 1964; Watson, 1964) by introducing an additional adjustment to the weights, thus combining the favorable bias properties of the local linear estimator with the benefit of being a distribution function by itself like the original Nadaraya-Watson estimator (Hall et al., 1999; Yu & Jones, 1998). The theory of the regression quantile with the RNW estimator has been further developed by Cai (2002). Furthermore, Cai (2002) and Salha (2006) demonstrated that the RNW estimator is consistent under strongly mixing conditions, which are commonly observed in time-series data. In this work, we adaptively utilize the RNW estimator within the conformal prediction framework to construct sequential prediction intervals for time-series data, leveraging its data-driven weights for quantile estimation and the weighted conformal approach. 

**Conformal prediction with weighted quantiles** Approaches using quantile regression instead of empirical quantiles in conformal prediction have been widespread (Romano et al., 2019; Kivaranovic et al., 2020; Gibbs et al., 2023). These methods utilize various quantile regression techniques to construct conformal prediction intervals, and the convergence to the oracle prediction width can be shown under the consistency of the quantile regression function (Sesia & Candès, 2020). Another recent work by Guan (2023) uses kernel weighting based on the distance between the test point and data to perform localized conformal prediction, which further discusses the selection of kernels and bandwidths. Recent work in this direction of utilizing the weighted quantiles, including Lee et al. (2023), continues to be vibrant. As we will 

2 

discuss later, our approach leverages techniques in classical non-parametric statistics when constructing the weights. 

**Time-series conformal prediction** There is a growing body of research on time-series conformal prediction (Xu & Xie, 2021b; Gibbs & Candès, 2021). Various applications include financial markets (Gibbs & Candès, 2021), anomaly detection (Xu & Xie, 2021a), and geological classification (Xu & Xie, 2022). In particular, Gibbs & Candès (2021, 2024) sequentially construct prediction intervals by updating the significance level _α_ based on the mis-coverage rate. This approach has become a major methodology for handling online, non-exchangeable data, leading to several subsequent developments of adaptively updating the single-parameter threshold that determines the prediction sets at each time step (Feldman et al., 2022; Auer et al., 2023; Bhatnagar et al., 2023; Zaffran et al., 2022; Angelopoulos et al., 2023; Yang et al., 2024; Angelopoulos et al., 2024). On the other hand, Xu & Xie (2023b); Xu et al. (2024) take a slightly different approach by conducting sequential quantile regression using non-conformity scores. Our study aims to integrate non-parametric kernel estimation for sequential quantile regression, addressing the weight selection issues identified by Barber et al. (2023). Additionally, our research aligns with Guan (2023), particularly in utilizing a dissimilarity measure between the test point and the past data. 

## **2 Problem Setup** 

We begin by assuming that the observations of the random sequence ( _Xt, Yt_ ) _∈_ R _[d] ×_ R, _t_ = 1 _,_ 2 _, . . ._ are obtained sequentially. Notably, _Xt_ may represent exogenous variables that aid in predicting _Yt_ , the historical values of _Yt_ itself, or a combination of both. (In Appendix A, we expand our discussion to include cases where the response _Yt_ is multivariate.) A key aspect of our setup is that the data are non-exchangeable and exhibit dependencies, which are typical in time-series data where temporal or sequential dependencies influence predictive dynamics. 

Suppose we are given a pre-specified point predictor _f_[ˆ] : R _[d] →_ R trained on a separate dataset or on past data. This predictor _f_[ˆ] maps a feature variable in R _[d]_ to a scalar point prediction for _Yt_ . Given a user-specified significance level _α ∈_ (0 _,_ 1), we use the initial _T_ observations to construct prediction intervals _C_[“] _t[α] −_ 1[(] _[X][t]_[)][ for] _[ Y][t]_[ in a sequential manner from] _[ t]_[ =] _[ T]_[+ 1][ onwards.] 

Two key types of coverage targeted by prediction intervals are _marginal coverage_ and _conditional coverage_ . Marginal coverage is defined as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0003-06.png)


which ensures that the true value _Yt_ falls within the interval _C_[“] _t[α] −_ 1[(] _[X][t]_[)][ at least][ 100(1] _[ −][α]_[)%][ of the time,] averaged over all instances. On the other hand, conditional coverage is defined as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0003-08.png)


which is a stronger guarantee ensuring that given each value of predictor _Xt_ , the true value _Yt_ falls within the interval _C_[“] _t[α] −_ 1[(] _[X][t]_[)][ at least][ 100(1] _[ −][α]_[)%][ of the time.] 

3 

## **3 Method** 

In this section, we introduce our proposed method, KOWCPI (Kernel-based Optimally Weighted Conformal Prediction Intervals), which embodies our approach to enhancing prediction accuracy and robustness in the face of time-series data. We delve into the methodology and algorithm of KOWCPI indepth, highlighting how the Reweighted Nadaraya-Watson (RNW) estimator integrates with our predictive framework. 

Consider prediction for a univariate time series, _Y_ 1 _, Y_ 2 _, . . ._ . We have predictors _Xt_ given to us at time _t_ , _t_ = 1 _,_ 2 _, . . ._ , which can depend on the past observations ( _Yt−_ 1 _, Yt−_ 2 _, . . ._ ), and possibly other exogeneous time series _Zt_ . Given a pre-trained algorithm _f_[ˆ] , we also have a sequence of non-conformity scores indicating the accuracy of the prediction: 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0004-03.png)


We denote the collection of the past _T_ non-conformity scores at time _t > T_ as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0004-05.png)


We construct the prediction interval _C_[“] _t[α] −_ 1[(] _[X][t]_[)][ with significance level] _[ α]_[ at time] _[ t > T]_[as follows:] 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0004-07.png)


Here, _q_ ˆ _β_ is a quantile regression algorithm that returns an estimate of the _β_ -quantile of the residuals, which we will explain through this section. We consider asymmetrical confidence intervals to ensure the tightest possible coverage. 

## **3.1 Reweighted Nadaraya-Watson estimator** 

The Reweighted Nadaraya-Watson (RNW) estimator is a general and popular method for quantile regression for time series. Observe ( _X_[˜] _i, Y_[˜] _i_ ), _i_ = 1 _, . . . , n_ , where _Y_[˜] _i ∈_ R, and the predictors _X_[˜] _i_ can be _p_ -dimensional. The goal is to predict the quantile P( _Y_[˜] _≤ b|X_[˜] ), _b ∈_ R, given a test point _X_[˜] using training samples. The RNW estimator introduces _adjustment weights_ on the predictors to ensure consistent estimation. We define the probability-like adjustment weights _pi_ ( _X_[˜] ), _i_ = 1 _, . . . , n_ , by maximizing the empirical log-likelihood[�] _[n] i_ =1[log] _[ p][i]_[( ˜] _[X]_[)][, subject to] _[ p][i]_[( ˜] _[X]_[)] _[ ≥]_[0][, and] 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0004-11.png)


The RNW estimate of the conditional CDF P( _Y_[˜] _≤ b|X_[˜] ) is defined as follows: 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0004-13.png)


4 

where the final weights _W_[�] _i_ are given by 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0005-01.png)


computed as a weighted average of the adjustment weights _pi_ based on the similarity between _X_[˜] to each sample _X_[˜] _i_ measured by the kernel function _K_ : R _[p] →_ R. Here, _Kh_ ( _u_ ) = _h[−][p] K_ ( _h[−]_[1] _u_ ) for _u ∈_ R _[p]_ . Any reasonable choice of kernel function is possible; however, to ensure the validity of our theoretical results discussed in Section 4, the kernel should be nonnegative, bounded, continuous, and possess compact support. An example is _K_ ( _u_ ) = _k_ ( _∥u∥_ ), where _k_ : R _→_ R is the Epanechnikov kernel. 

The primary computational burden of the RNW estimator lies in calculating the adjustment weights _pi_ . However, as Lemma 3.1 shows, this reduces to a simple one-dimensional convex minimization problem, ensuring that the RNW estimator is not computationally intensive. This simplification significantly alleviates the overall computational complexity. Furthermore, Lemma 3.1 serves as a starting point for the proof of the asymptotic conditional coverage property of our algorithm, which will be addressed in Appendix B.1. 

**Lemma 3.1** ((Hall et al., 1999; Cai, 2001)) **.** _The adjustment weights pi_ ( _X_[˜] ) _, i_ = 1 _, . . . , n, for the RNW estimator are given as_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0005-05.png)


_where_ [ _X_ ]1 _denotes the first element of a vector X, and λ ∈_ R _is the minimizer of:_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0005-07.png)


## **3.2 RNW for conformal prediction** 

To perform the quantile regression for prediction interval construction at time _t_ = _T_ + 1, we use a sliding window approach, breaking the past _T_ residuals _ET_ +1 = (ˆ _εT , . . ._ ˆ _ε_ 1) into _n_ := ( _T − w_ ) overlapping segments of length _w_ . We construct the predictors and responses to fit the RNW estimator as follows: 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0005-10.png)


With RNW estimator _F_[“] fitted on (( _X_[˜] _i, Y_[˜] _i_ )) _[n] i_ =1[, the conditional] _[ β]_[-quantile estimator] _Q_[“] _β_ is defined as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0005-12.png)


After time _t_ = _T_ + 1, we update _Et_ by removing the oldest residual and adding the newest one, then repeat the process (see Algorithm 1). In Section 4, we prove that due to the consistency of _Q_[“] _β_ , KOWCPI achieves asymptotic conditional coverage despite the significant temporal dependence introduced by using overlapping segments of residuals. 

_Bandwidth selection._ Estimating the theoretically optimal bandwidth that minimizes the asymptotic mean-squared error requires additional derivative estimation, which significantly complicates the problem. Consequently, similar to general non-parametric models, one can use cross-validation to select the 

5 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0006-00.png)


**----- Start of picture text -----**<br>
Ƹ𝜀2 Ƹ𝜀3 Ƹ𝜀𝑡−1 Ƹ𝜀𝑡+𝑤−1 ෨𝑌𝑡 = Ƹ𝜀𝑡+𝑤<br>time<br>Ƹ𝜀1 Ƹ𝜀𝑤 Ƹ𝜀𝑡 Ƹ𝜀𝑡+𝑤−2<br>𝑋෨𝑡 = (Ƹ𝜀𝑡+𝑤−1, … , Ƹ𝜀𝑡)<br>A? 𝑋෨𝑡−1 = (Ƹ𝜀𝑡+𝑤−2, … , Ƹ𝜀𝑡−1)<br>…<br>pe, 𝑋෨1 = (Ƹ𝜀𝑤, … , Ƹ𝜀1) Histogram of {€:}7_, 1.0 PACF<br>**----- End of picture text -----**<br>


Figure 1: Illustration of KOWCPI, a sequential conformal prediction method. In the absence of exchangeability in the data, as indicated by the empirical distribution of residuals and the PACF plot, it is critical to consider the sequentially dependent structure of the data. In KOWCPI, non-conformity score blocks are updated sequentially using a sliding window, which provides prediction intervals for future scores through nonparametric quantile regression. 

bandwidth. However, cross-validation can be computationally burdensome and may deteriorate under dependent data (Fan et al., 1995). Therefore, we adapt the non-parametric AIC (Cai & Tiwari, 2000), used for bandwidth selection in local linear estimators. This method is applicable because the RNW estimator belongs to the class of linear smoother (Cai, 2002). Let _S_ be a linear smooth operator, with the ( _i, j_ )-th element given by _Sij_ = _W_[�] _j_ ( _X_[˜] _i_ ) (Hastie, 1990). Recognizing that the degree of freedom of the RNW smoother can be given as tr( _SS[⊤]_ ), we choose the bandwidth _h_ that minimizes 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0006-03.png)


where RSS is the residual sum of squares. 

_Window length selection._ To select the window length _w_ , cross-validation can be employed. In experiments, we chose _w_ with the smallest average width that achieves a target coverage in the validation set. Another approach is to use a weighted sum of the average under-coverage rate and the average width obtained for a given _w_ as the criterion. We note that the performance is generally less sensitive to the choice of _w_ across a broader range compared to the bandwidth _h_ . Additionally, in Appendix E, we introduce an adaptive window selection approach that enables _w_ to be determined in a data-driven manner, eliminating the need for hyperparameter tuning with minimal loss in performance. 

6 

**Algorithm 1** Kernel-based Optimally Weighted Conformal Prediction Intervals (KOWCPI) 

- **Require:** Training data ( _Xt, Yt_ ), _t_ = 1 _, . . . , T_ , pre-trained point predictor _f_[ˆ] , target significance level _α ∈_ (0 _,_ 1), window length _w_ , non-conformity score block count _n_ = _T − w_ . 

- ˆ 

- 1: Compute prediction residuals for the training data: _εt_ = _Yt − f_[ˆ] ( _Xt_ ), _t_ = 1 _, . . . , T_ . 

- 2: **for** _t_ = _T_ + 1 _, T_ + 2 _, . . ._ **do** 3: Update residual history _Et_ = (ˆ _εt−_ 1 _, . . . ,_ ˆ _εt−T_ ). 4: Break _Et_ into overlapping segments: _X_[˜] _i_ = (ˆ _εt−T_ + _i_ + _w−_ 2 _, . . . ,_ ˆ _εt−T_ + _i−_ 1), _i_ = 1 _, . . . , n_ + 1. 5: Compute _λ_ that minimizes _L_ ( _·_ ; _X_[˜] _n_ +1) in (9). 6: Derive adjustment weights _pi_ ( _X_[˜] _n_ +1), _i_ = 1 _, . . . , n_ , and calculate final weights _W_[�] _i_ ( _X_[˜] _n_ +1) in (7). ˆ 

- 7: Using _Y_[˜] _i_ = _εt−T_ + _i_ + _w−_ 1, _i_ = 1 _, . . . , n_ , compute the quantile estimator _Q_[“] _β_ ( _X_[˜] _n_ +1) for _β ∈_ [0 _, α_ ]. 8: Determine _β[∗]_ = argmin _β∈_ [0 _,α_ ] _Q_[“] 1 _−α_ + _β_ ( _X_[˜] _n_ +1) _− Q_[“] _β_ ( _X_[˜] _n_ +1). 9: Return prediction interval _C_[“] _t[α] −_ 1[(] _[X][t]_[) =][ �] _[f]_[ˆ][(] _[X][t]_[) +] _Q_[“] _β∗_ ( _X_[˜] _n_ +1) _, f_[ˆ] ( _Xt_ ) + _Q_[“] 1 _−α_ + _β∗_ ( _X_[˜] _n_ +1)[�] . ˆ 

- 10: Obtain new residual _εt_ = _Yt − f_[ˆ] ( _Xt_ ). 

- 11: **end for** 

## **4 Theory** 

In this section, we introduce the theoretical properties of the RNW estimator, a quantile regression method we use, and demonstrate in Theorem 4.9 that our KOWCPI asymptotically displays conditional coverage under the strong mixing of residuals. It turns out that the asymptotic conditional coverage gap can be derived from known results in the context of kernel quantile regression. 

## **4.1 Marginal coverage** 

We begin by bounding the marginal coverage gap of the KOWCPI method. The following result shows the coverage gap using our weights, compared with the oracle weights; the results are established using a similar strategy as in Tibshirani et al. (2019, Lemma 3): 

**Proposition 4.1** (Non-asymptotic marginal coverage gap) **.** _Denote by P the joint density of_ ( _Y_[˜] 1 _, . . . , Y_[˜] _n_ +1) _. Then, we have_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0007-10.png)


_where_ ∆( _X_[˜] _n_ +1) _is the discrete gap defined in_ (17) _, and W[∗] is the vector of oracle weights with each entry defined as_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0007-12.png)


_and σ is a permutation on {_ 1 _, . . . , n_ + 1 _}._ 

The implication of Proposition 4.1 is that 

- The “under-coverage” depends on the _ℓ_ 1-distance between the learned optimal weights and oracleoptimal weights (that depends on the true joint distribution of data). 

7 

- Note that the oracle weights _Wi[∗]_[cannot be evaluated, because in principle, it requires considering] the ( _n_ + 1)! possible shuffled observed residuals and their joint distributions. 

- The form of the oracle weights _Wi[∗]_[from][ (13)][ offers an intuitive basis for algorithm development:] we can practically estimate the weights through quantile regression, utilizing previously observed non-conformity scores. 

## **4.2 Conditional coverage** 

In this section, we derive the asymptotic conditional coverage property of KOWCPI. For this, we introduce the assumptions necessary for the consistency of the RNW estimator. To account for the dependency in the data, we assume the strong mixing of the residual process. 

A stationary stochastic process _{Vt}[∞] t_ = _−∞_[on a probability space with a probability measure][ P][ is said] to be _strongly mixing (α-mixing)_ if a mixing coefficient _α_ ( _τ_ ) defined as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0008-05.png)


satisfies _α_ ( _τ_ ) _→_ 0 as _τ →∞_ , where M _[t] s_[,] _[−∞≤][s][≤][t][≤∞]_[,][denotes][a] _[σ]_[-algebra][generated][by] _{Vs, Vs_ +1 _, . . . , Vt}_ . The mixing coefficient _α_ ( _τ_ ) quantifies the asymptotic independence between the past and future of the sequence _{Vt}[∞] t_ = _−∞_[.] 

**Assumption 4.2** (Mixing of the process) **.** The stationary process ( _Vi_ = ( _X_[˜] _i, Y_[˜] _i_ )) _[∞] i_ =1[is strongly mixing] with the mixing coefficient _α_ ( _τ_ ) = _O_ ( _τ[−]_[(2+] _[δ]_[)] ) for some _δ >_ 0. 

We highlight that our strong mixing assumptions apply to the residuals, which is a far less restrictive condition than assuming the original time series itself is strongly mixing. Even when the original time series departs significantly from stationarity, the unobserved noises may still retain stationarity and strong mixing properties. For instance, in a vector auto-regressive model with a time-dependent drift, the noises are drawn from the identical distribution without serial correlation. 

Furthermore, the strong mixing property is widely regarded as a relatively weak condition and is commonly met by many time series models, making it a typical assumption in time-series analysis (Cai, 2002). For instance, both linear autoregressive models and the broader class of bilinear models satisfy strong mixing conditions with exponentially decaying mixing coefficients under mild assumptions. Similarly, ARCH processes and nonlinear additive autoregressive models with exogenous variables are recognized for their stationary and strong mixing behavior (Masry & Tjøstheim, 1995, 1997). 

Due to stationarity, the conditional CDF of the realized residual does not depend on the index _i_ ; thus, denote 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0008-11.png)


˜ as the conditional CDF of the random variable _Y_[˜] _i_ given _X_[˜] _i_ = _x_ . In addition, we introduce the following notations: 

- Let _g_ (˜ _x_ ) be the marginal density of _X_[˜] _i_ at _x_ ˜. (Note that due to stationarity, we can have a common marginal density.) 

- Let _g_ 1 _,i, i ≥_ 2 denote the joint density of _X_[˜] 1 and _X_[˜] _i_ . 

8 

The following assumptions (4.3-4.5) are common in nonparametric statistics, essential for attaining desirable properties such as the consistency of an estimator (Tsybakov, 2009). 

**Assumption 4.3** (Smoothness of the conditional CDF and densities) **.** For fixed _y_ ˜ _∈_ R and _x_ ˜ _∈_ R _[w]_ , 

- (i) 0 _< F_ (˜ _y|x_ ˜) _<_ 1. 

- (ii) _F_ (˜ _y|x_ ˜) is twice continuously partially differentiable with respect to _x_ ˜. 

- ˜ 

- (iii) _g_ (˜ _x_ ) _>_ 0 and _g_ ( _·_ ) is continuous at _x_ . 

- (iv) There exists _M >_ 0 such that _|g_ 1 _,i_ ( _u, v_ ) _− g_ ( _u_ ) _g_ ( _v_ ) _| ≤ M_ for all _u, v_ and _i ≥_ 2. 

Regarding Assumption 4.3, we would like to remark that there is a negative result: without additional assumptions about the distribution, it is impossible to construct finite-length prediction intervals that satisfy conditional coverage (Lei & Wasserman, 2014; Vovk, 2012). 

**Assumption 4.4** (Regularity of the kernel function) **.** The kernel _K_ : R _[w] →_ R is a nonnegative, bounded, continuous, and compactly supported density function satisfying 

- (i) �R _[w][ uK]_[(] _[u]_[)] _[du]_[ = 0][,] 

- (ii) �R _[w][ uu][⊤][K]_[(] _[u]_[)] _[du]_[ =] _[ µ]_[2] _[I]_[for some] _[ µ]_[2] _[∈]_[(0] _[,][ ∞]_[)][,] 

- (iii) �R _[w][ K]_[2][(] _[u]_[)] _[du]_[ =] _[ ν]_[0][ and] �R _[w][ uu][⊤][K]_[2][(] _[u]_[)] _[du]_[ =] _[ ν]_[2] _[I]_[for some] _[ ν]_[0] _[, ν]_[2] _[∈]_[(0] _[,][ ∞]_[)][.] 

Assumptions 4.4-(i), (ii), and (iii) are standard conditions (Wand & Jones, 1994) that require _K_ to be “symmetric” in a sense that that the weighting scheme relies solely on the distance between the observation and the test point. For example, if _K_ is isometric, i.e., _K_ ( _u_ ) = _k_ ( _∥u∥_ ) for some univariate kernel function _k_ : R _→_ R, it can satisfy these conditions using widely adopted kernels such as the Epanechnikov kernel. 

**Assumption 4.5** (Bandwidth selection) **.** As _n →∞_ , the bandwidth _h_ satisfies 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0009-13.png)


We note that Assumption 4.5 is met when selecting the (theoretically) optimal bandwidth _h[∗] ∼ n[−]_[1] _[/]_[(] _[w]_[+4)] , which minimizes the asymptotic mean squared error (AMSE) of the RNW estimator, provided that _δ >_ 1 _/_ 2. 

We prove the following proposition following a similar strategy as (Salha, 2006) by fixing several technical details: 

**Proposition 4.6** (Consistency of the RNW estimator) **.** _Under Assumptions 4.2-4.5, given arbitrary x_ ˜ _and y_ ˜ _, as n →∞,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0009-17.png)


_where D_[2] ˜ _[x]_[˜] _[.] x[F]_[(˜] _[y][|][x]_[˜][)] _[ denotes the Hessian of][ F]_[(˜] _[y][|][x]_[˜][)] _[ with respect to]_ 

9 

This proposition implies pointwise convergence in probability of the RNW estimator, and since it is the weighted empirical CDF, this pointwise convergence implies uniform convergence in probability (Tucker, 1967, p.127-128). Consequently, we obtain the consistency of the conditional quantile estimator in (10) to the true conditional quantile given as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0010-01.png)


**Corollary 4.7.** _Under Assumptions 4.2-4.5, for every β ∈_ (0 _,_ 1) _and x_ ˜ _, as n →∞,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0010-03.png)


As a direct consequence of Corollary 4.7, the asymptotic conditional coverage of KOWCPI is guaranteed by the consistency of the quantile estimator used in our sequential algorithm. 

**Corollary 4.8** (Asymptotic conditional coverage guarantee) **.** _Under Assumptions 4.2-4.5, for any α ∈_ (0 _,_ 1) _, as n →∞,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0010-06.png)


Thus, employing quantile regression using the RNW estimator for prediction residuals derived from the time-series data of continuous random variables, assuming strong mixing of these residuals, KOWCPI can achieve approximate conditional coverage with a sufficient number of residuals utilized. 

To further specify the rate of convergence, define the _discrete gap_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0010-09.png)


introduced by the quantile estimator being the generalized inverse distribution function. 

**Theorem 4.9** (Conditional coverage gap) **.** _Under Assumptions 4.2-4.5, for any α ∈_ (0 _,_ 1) _and xt, as n →∞,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0010-12.png)


˜ _where xn_ +1 _is the realization of X_[˜] _n_ +1 _given Xt_ = _xt._ 

Given that the adjustment weights _pi_ (˜ _x_ ) uniformly concentrate to 1 _/n_ (Steikert, 2014), one can see that the conditional coverage gap tends to zero, although its precise rate remains an open question. 

## **5 Experiments** 

In this section, we compare the performance of KOWCPI against state-of-the-art conformal prediction baselines using real time-series data. Additional experimental results, not included in this section, using both real and synthetic data, are provided in Appendices C and D. We aim to show that KOWCPI can consistently reach valid coverage with the narrowest prediction intervals. 

_Dataset._ We consider three real time series from different domains. The first ELEC2 data set (electric) (Harries, 1999) tracks electricity usage and pricing in the states of New South Wales and Victoria in Australia for every 30 minutes over a 2.5-year period in 1996–1999. The second renewable energy data 

10 

Table 1: Empirical marginal coverage and average width across three real time-series datasets by different methods. The target coverage is 1 _− α_ = 0 _._ 9. The values in the bracket are standard deviation across five independent trials. 

||Electric<br>Coverage<br>Width|Wind<br>Coverage<br>Width|Solar<br>Coverage<br>Width|
|---|---|---|---|
|KOWCPI<br>Plain NW<br>SPCI<br>EnbPI<br>ACI<br>FACI<br>AgACI<br>SF-OGD<br>SAOCP<br>SCP|0.90 (2.3e-3)<br>0.22 (1.5e-3)<br>0.89 (1.7e-3)<br>0.31 (2.2e-3)<br>0.90 (1.1e-3)<br>0.29 (1.9e-3)<br>0.93 (3.4e-3)<br>0.36 (2.7e-3)<br>0.89 (0.0e-0)<br>0.32 (2.0e-3)<br>0.89 (2.5e-3)<br>0.28 (1.2e-3)<br>0.91 (3.1e-3)<br>0.30 (2.3e-3)<br>0.79 (5.8e-4)<br>0.25 (1.0e-3)<br>0.93 (6.1e-3)<br>0.33 (2.4e-3)<br>0.87 (2.8e-3)<br>0.30 (5.9e-4)|0.91 (2.8e-3)<br>2.41 (3.2e-2)<br>0.95 (7.4e-3)<br>3.58 (1.0e-1)<br>0.94 (1.0e-2)<br>2.61 (2.1e-2)<br>0.92 (2.3e-3)<br>5.25 (4.3e-2)<br>0.88 (0.0e-0)<br>8.26 (2.8e-2)<br>0.91 (3.2e-3)<br>7.77 (1.7e-1)<br>0.88 (1.1e-2)<br>7.54 (1.2e-1)<br>0.11 (2.6e-3)<br>0.29 (7.0e-4)<br>0.76 (1.1e-2)<br>4.00 (4.5e-2)<br>0.86 (3.2e-3)<br>8.20 (1.5e-2)|0.90 (1.2e-3)<br>48.8 (9.4e-1)<br>0.41 (2.7e-3)<br>20.1 (1.8e+0)<br>0.92 (1.7e-3)<br>84.2 (1.7e+0)<br>0.87 (1.1e-3)<br>106.0 (2.3e+0)<br>0.89 (1.0e-3)<br>143.9 (2.3e-1)<br>0.89 (0.0e-0)<br>141.9 (6.4e-1)<br>0.90 (2.4e-3)<br>144.6 (1.4e+0)<br>0.00 (0.0e-0)<br>0.50 (0.0e-0)<br>0.64 (1.9e-3)<br>33.5 (7.3e-2)<br>0.89 (1.0e-3)<br>142.0 (3.8e-1)|



(solar) (Zhang et al., 2021) are from the National Solar Radiation Database and contain hourly solar radiation data (measured in GHI) from Atlanta in 2018. The third wind speed data (wind) (Zhu et al., 2021) are collected at wind farms operated by MISO in the US. The wind speed record was updated every 15 minutes over a one-week period in September 2020. 

_Baselines._ We consider Sequential Predictive Conformal Inference (SPCI) (Xu & Xie, 2023b), Ensemble Prediction Interval (EnbPI) (Xu & Xie, 2023a), Adaptive Conformal Inference (ACI) (Gibbs & Candès, 2021), Aggregated ACI (AgACI) (Zaffran et al., 2022), Fully Adaptive Conformal Inference (FACI) (Gibbs & Candès, 2024), Scale-Free Online Gradient Descent (SF-OGD) (Orabona & Pál, 2018; Bhatnagar et al., 2023), Strongly Adaptive Online Conformal Prediction (SAOCP) (Bhatnagar et al., 2023), and vanilla Split Conformal Prediction (SCP) (Vovk et al., 2005). Additionally, we included a comparison where weights were derived from the original Nadaraya-Watson estimator (Plain NW). For the implementation of ACI-related methods, we utilized the R package AdaptiveConformal (https://github.com/ herbps10/AdaptiveConformal). For SPCI and EnbPI, we used the Python code from https: //github.com/hamrel-cxu/SPCI-code. 

_Setup and evaluation metrics._ In all comparisons, we use the random forest as the base point predictor with the number of trees = 10. Every dataset is split in a 7:1:2 ratio for training the point predictor, tuning the window length _w_ and bandwidth _h_ , and constructing prediction intervals, respectively. The window length for each dataset is fixed and determined through cross-validation, while the bandwidth is selected by minimizing the nonparametric AIC, as detailed in (11). 

Besides examining marginal coverage and widths of prediction intervals on test data, we also focus on _rolling coverage_ , which is helpful in showing approximate conditional coverage at specific time indices. Given a rolling window size _m >_ 0, rolling coverage RC[”] _t_ at time _t_ is defined as RC[”] _t_ = _m_ 1 � _mi_ =1[1] _[{][Y][t][−][i]_[+1] _[∈] C_[“] _t[α] −i_[(] _[X][t][−][i]_[+1][)] _[}][.]_ 

_Results._ The empirical marginal coverage and width results for all methods are summarized in Table 1. The results indicate that KOWCPI consistently achieves the 90% target coverage and maintains the smallest average width compared to the alternative state-of-the-art methods. While all methods, except SF-OGD, SAOCF, and Plain NW nearly achieve marginal coverage under target 1 _− α_ = 0 _._ 9, KOWCPI 

11 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0012-00.png)


**----- Start of picture text -----**<br>
(a) Rolling coverage (boxplot)<br>**----- End of picture text -----**<br>



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0012-01.png)


**----- Start of picture text -----**<br>
(c) Rolling coverage over prediction time indices<br>**----- End of picture text -----**<br>



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0012-02.png)


**----- Start of picture text -----**<br>
(b) Width of prediction intervals (boxplot)<br>i)<br>1000 800 600 400 200<br>Time lag<br>�<br>(d) logÄ Wi ä by the time lag<br>**----- End of picture text -----**<br>


Figure 2: Comparison of empirical rolling coverage and width on the electric dataset by different methods in (a) rolling coverage; (b) widths of intervals, (c) rolling coverage over time, and (d) an instance of computed final weights. The target coverage is 90%. In (a), the red dotted line is the target coverage and in (b), the blue dotted line is the median width of KOWCPI. 

produces the narrowest average width on all datasets. In terms of rolling results, we show in Figures 2a and 2c that the coverage of KOWCPI intervals consistently centers around 90% throughout the entire test phase. Additionally, Figure 2b shows that KOWCPI intervals are also significantly narrower with a smaller variance than the baselines. 

Lastly, Figure 2d depicts the weights _W_[�] (in log scale) assigned by the RNW estimator at the first time index of the test data. Notably, the most recent set of non-conformity scores (in terms of time indices) is assigned the heaviest weights, which aligns intuitively as these are the most similar to the first test datum in terms of temporal proximity. We believe that this heavy weighting of recent residuals contributes significantly to KOWCPI’s performance. Datasets where KOWCPI demonstrates significant superiority, such as the Solar dataset, typically exhibit active volatility changes. In these cases, KOWCPI 

12 

adapts quickly to changing conditions by leveraging the high weights assigned to recent residuals. For instance, in Figure A.3, which visualizes the performance of KOWCPI, SPCI, and ACI on the Solar dataset, KOWCPI dynamically adjusts its interval widths to reflect whether it is in a high or low-volatility region. This adaptive behavior allows KOWCPI to avoid over-coverage and maintain narrower average widths compared to methods like SPCI and ACI, which produce intervals with relatively constant widths across all regions. At the same time, we acknowledge that such fast-adapting behavior, avoiding conservative intervals, can occasionally lead to brief coverage failures in some regions due to the aggressive adaptation to rapidly changing conditions. 

In Appendix C.1, we show additional comparisons of KOWCPI against the baselines on the other two datasets in terms of rolling results. See Appendices C.2 and D for additional experimental results using a wider variety of real and synthetic datasets, where we consistently observe the coverage validity of KOWCPI while yielding the shortest intervals on average. 

## **6 Conclusion** 

In this paper, we introduced KOWCPI, a method to sequentially construct prediction intervals for time-series data. By incorporating the classical Reweighted Nadaraya-Watson estimator into the weighted conformal prediction framework, KOWCPI effectively adapts to the dependent structure of time-series data by utilizing data-driven adaptive weights. Our theoretical contributions include providing theoretical guarantees for the asymptotic conditional coverage of KOWCPI under strong mixing conditions and bounding the marginal and conditional coverage gaps. Empirical validation on real-world time-series datasets demonstrated the effectiveness of KOWCPI compared to state-of-the-art methods, achieving narrower prediction intervals without compromising empirical coverage. 

Future work could explore _adaptive window selection_ , where the size of the non-conformity score batch is adjusted dynamically to capture shifts in the underlying distribution. A preliminary implementation of this approach is discussed in Appendix E, showcasing its potential to improve flexibility and adaptability in practice. Additionally, the natural compatibility of kernel regression with multivariate data can be leveraged to expand the utility of KOWCPI for multivariate time-series data, as detailed in Appendix A. There is also potential for improving theoretical guarantees and practical performance by designing alternative non-conformity scores. 

## **References** 

- Belkacem Abdous and Radu Theodorescu. Note on the spatial quantile of a random vector. _Statist. Probab. Lett._ , 13(4):333–336, 1992. 

- Anastasios Angelopoulos, Emmanuel Candès, and Ryan J. Tibshirani. Conformal PID Control for Time Series Prediction. In _Advances in Neural Information Processing Systems_ , 2023. 

- Anastasios N. Angelopoulos and Stephen Bates. Conformal Prediction: A Gentle Introduction. _Foundations and Trends® in Machine Learning_ , 16(4):494–591, 2023. 

- Anastasios N. Angelopoulos, Rina Foygal Barber, and Stephen Bates. Online conformal prediction with decaying step sizes. In _Proceedings of the 41st International Conference on Machine Learning_ , 2024. 

13 

- Andreas Auer, Martin Gauch, Daniel Klotz, and Sepp Hochreiter. Conformal Prediction for Time Series with Modern Hopfield Networks. In _Advances in Neural Information Processing Systems_ , 2023. 

- Rina Foygel Barber, Emmanuel J. Candès, Aaditya Ramdas, and Ryan J. Tibshirani. Conformal prediction beyond exchangeability. _The Annals of Statistics_ , 51(2):816 – 845, 2023. 

- Aadyot Bhatnagar, Huan Wang, Caiming Xiong, and Yu Bai. Improved Online Conformal Prediction via Strongly Adaptive Online Learning. In _Proceedings of the 40th International Conference on Machine Learning_ , 2023. 

- Zongwu Cai. Weighted Nadaraya-Watson regression estimation. _Statistics & Probability Letters_ , 51(3): 307–318, 2001. 

- Zongwu Cai. Regression quantiles for time series. _Econometric Theory_ , 18(1):169–192, 2002. 

- Zongwu Cai and Ram C. Tiwari. Application of a local linear autoregressive model to BOD time series. _Environmetrics_ , 11(3):341–350, 2000. 

- Jianqing Fan, Nancy E. Heckman, and Matt P. Wand. Local Polynomial Kernel Regression for Generalized Linear Models and Quasi-Likelihood Functions. _Journal of the American Statistical Association_ , 90 (429):141–150, 1995. 

- Shai Feldman, Liran Ringel, Stephen Bates, and Yaniv Romano. Achieving Risk Control in Online Learning Settings. _arXiv preprint arXiv:2205.09095_ , 2022. 

- Isaac Gibbs and Emmanuel Candès. Adaptive Conformal Inference Under Distribution Shift. _Advances in Neural Information Processing Systems_ , 34:1660–1672, 2021. 

- Isaac Gibbs and Emmanuel Candès. Conformal Inference for Online Prediction with Arbitrary Distribution Shifts. _Journal of Machine Learning Research_ , 25(162):1–36, 2024. 

- Isaac Gibbs, John J. Cherian, and Emmanuel J. Candès. Conformal Prediction With Conditional Guarantees. _arXiv preprint arXiv:2305.12616_ , 2023. 

- Leying Guan. Localized conformal prediction: a generalized inference framework for conformal prediction. _Biometrika_ , 110(1):33–50, 2023. 

- Peter Hall, Rodney C. L. Wolff, and Qiwei Yao. Methods for Estimating a Conditional Distribution Function. _Journal of the American Statistical Association_ , 94(445):154–163, 1999. 

- Michael Harries. SPLICE-2 Comparative Evaluation: Electricity Pricing. Technical report, University of New South Wales, School of Computer Science and Engineering, 1999. 

Trevor J. Hastie. _Generalized additive models_ . CRC Press, 1990. 

- Ildar A. Ibragimov, Yu V. Linnik, and John F. C. Kingman. _Independent and Stationary Sequences of Random Variables_ . Wolters-Noordhoff., 1971. 

- Byol Kim, Chen Xu, and Rina Foygel Barber. Predictive inference is free with the jackknife+-afterbootstrap. _Advances in Neural Information Processing Systems_ , 33:4138–4149, 2020. 

14 

- Danijel Kivaranovic, Kory D. Johnson, and Hannes Leeb. Adaptive, Distribution-Free Prediction Intervals for Deep Networks. In _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , 2020. 

- Yonghoon Lee, Rina Foygel Barber, and Rebecca Willett. Distribution-free inference with hierarchical data. _arXiv preprint arXiv:2306.06342_ , 2023. 

- Jing Lei and Larry Wasserman. Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 76(1):71–96, 2014. 

- Jing Lei, James Robins, and Larry Wasserman. Distribution-Free Prediction Sets. _Journal of the American Statistical Association_ , 108(501):278–287, 2013. 

- Elias Masry. Recursive probability density estimation for weakly dependent stationary processes. _IEEE Transactions on Information Theory_ , 32(2):254–267, 1986. 

- Elias Masry and Dag Tjøstheim. Nonparametric estimation and identification of nonlinear arch time series strong convergence and asymptotic normality: Strong convergence and asymptotic normality. _Econometric theory_ , 11(2):258–289, 1995. 

- Elias Masry and Dag Tjøstheim. Additive nonlinear arx time series and projection estimates. _Econometric theory_ , 13(2):214–252, 1997. 

- Elizbar A. Nadaraya. On Estimating Regression. _Theory of Probability & Its Applications_ , 9(1):141–142, 1964. 

- Francesco Orabona and Dávid Pál. Scale-free online learning. _Theoretical Computer Science_ , 716:50–69, 2018. 

- Yaniv Romano, Evan Patterson, and Emmanuel Candès. Conformalized Quantile Regression. In _Advances in Neural Information Processing Systems_ , 2019. 

- Raid Salha. _Kernel Estimation for the Conditional Mode and Quantiles of Time Series_ . PhD thesis, University of Macedonia, 2006. 

- Matteo Sesia and Emmanuel J Candès. A comparison of some conformal quantile regression methods. _Stat_ , 9(1):e261, 2020. 

- Kamile Stankeviˇci˙ ut¯ e, Ahmed Alaa, and Mihaela van der Schaar.˙ Conformal time-series forecasting. In _Advances in Neural Information Processing Systems_ , 2021. 

- Kristoph U. Steikert. _The weighted Nadaraya-Watson Estimator: Strong consistency results, rates of convergence, and a local bootstrap procedure to select the bandwidth_ . PhD thesis, University of Zurich, 2014. 

- Sophia Huiwen Sun and Rose Yu. Copula conformal prediction for multi-step time series prediction. In _The Twelfth International Conference on Learning Representations_ , 2024. 

- Ryan J. Tibshirani, Rina Foygel Barber, Emmanuel Candès, and Aaditya Ramdas. Conformal Prediction Under Covariate Shift. _Advances in Neural Information Processing Systems_ , 32, 2019. 

15 

Alexandre B. Tsybakov. _Introduction to Nonparametric Estimation_ . Springer, 2009. 

Howard G. Tucker. _A Graduate Course in Probability_ . Academic Press, 1967. 

- Vladimir Vovk. Conditional validity of inductive conformal predictors. In _Proceedings of the Asian Conference on Machine Learning_ , 2012. 

- Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic Learning in a Random World_ . Springer, 2005. 

- Volodya Vovk, Alexander Gammerman, and Craig Saunders. Machine-Learning Applications of Algorithmic Randomness. In _Proceedings of the Sixteenth International Conference on Machine Learning_ , 1999. 

Matt P. Wand and M. C. Jones. _Kernel Smoothing_ . CRC press, 1994. 

- Geoffrey S. Watson. Smooth regression analysis. _Sankhya:¯ The Indian Journal of Statistics, Series A_ , 26: 359–372, 1964. 

- Chen Xu and Yao Xie. Conformal Anomaly Detection on Spatio-Temporal Observations with Missing Data. _arXiv preprint arXiv:2105.11886_ , 2021a. 

- Chen Xu and Yao Xie. Conformal prediction interval for dynamic time-series. In _Proceedings of the 38th International Conference on Machine Learning_ , 2021b. 

- Chen Xu and Yao Xie. Conformal prediction set for time-series. _arXiv preprint arXiv:2206.07851_ , 2022. 

- Chen Xu and Yao Xie. Conformal prediction for time series. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 45(10):11575–11587, 2023a. 

- Chen Xu and Yao Xie. Sequential Predictive Conformal Inference for Time Series. In _Proceedings of the 40th International Conference on Machine Learning_ , 2023b. 

- Chen Xu, Hanyang Jiang, and Yao Xie. Conformal prediction for multi-dimensional time series by ellipsoidal sets. _arXiv preprint arXiv:2403.03850_ , 2024. 

- Zitong Yang, Emmanuel Candès, and Lihua Lei. Bellman conformal inference: Calibrating prediction intervals for time series. _arXiv preprint arXiv:2402.05203_ , 2024. 

- Keming Yu and M. C. Jones. Local Linear Quantile Regression. _Journal of the American Statistical Association_ , 93(441):228–237, 1998. 

- Margaux Zaffran, Olivier Féron, Yannig Goude, Julie Josse, and Aymeric Dieuleveut. Adaptive Conformal Predictions for Time Series. In _Proceedings of the 39th International Conference on Machine Learning_ , 2022. 

- Minghe Zhang, Chen Xu, Andy Sun, Feng Qiu, and Yao Xie. Solar Radiation Ramping Events Modeling Using Spatio-temporal Point Processes. _arXiv preprint arXiv:2101.11179_ , 2021. 

- Shixiang Zhu, Hanyu Zhang, Yao Xie, and Pascal Van Hentenryck. Multi-resolution spatio-temporal prediction with application to wind power generation. _arXiv preprint arXiv:2108.13285_ , 2021. 

16 

## **A Multivariate time series** 

In the main text, our discussion has centered on cases where the response variables _Yt_ are scalars. Here, we explore the natural extension of our methodology to handle scenarios with multivariate responses. This extension requires defining multivariate quantiles, introducing a multivariate version of the RNW estimator for estimating these quantiles (Salha, 2006), and adapting our KOWCPI method for multivariate responses. 

**Multivariate conditional quantiles** Consider a strongly mixing stationary process (( _X_[˜] _i, Y_[˜] _i_ )) _[∞] i_ =1[, which] is a realization of random variable ( _X,_[˜] _Y_[˜] ) _∈_ R _[p] ×_ R _[s]_ . Following Abdous & Theodorescu (1992), we first define a pseudo-norm function _∥·∥_ 2 _,α_ : R _[s] →_ R for _α ∈_ (0 _,_ 1) as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0017-03.png)


for _v ∈_ R _[s]_ , where _∥·∥_ 2 is the Euclidean norm on R _[s]_ . Let 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0017-05.png)


**Definition A.1** (Multivariate conditional quantile (Abdous & Theodorescu, 1992)) **.** Define a multivariate conditional _α_ -quantile _θα_ (˜ _x_ ) for _α ∈_ (0 _,_ 1) as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0017-07.png)


_Remark_ A.2 (Compatibility with univariate quantile function) _._ For a scalar _Y_[˜] _∈_ R, its conditional quantile ˜ given _X_[˜] = _x_ is 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0017-09.png)


for any _α ∈_ (0 _,_ 1). Thus, Definition A.1 is consistent with the univariate case. 

**Multivariate RNW estimator** Following the definition in (6), we obtain the RNW estimator for multivariate responses as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0017-12.png)


where, according to (7) and (8), 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0017-14.png)


17 

for _u_ = ( _u_ 1 _, . . . , up_ ) _[⊤]_ . Now, let _Wh_ ( _u_ ) = _h[−][p] W_ ( _h[−]_[1] _u_ ), and define an estimator for _Hα_ ( _θ, x_ ) as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0018-01.png)


and consequently the RNW conditional quantile estimator _θ_[�] _α_ as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0018-03.png)


**Multivariate KOWCPI** Suppose we are sequentially observing ( _Xt, Yt_ ) _∈_ R _[d] ×_ R _[s]_ , _t_ = 1 _,_ 2 _, . . ._ . Based on the construction of the multivariate version of the RNW estimator, we can extend our KOWCPI approach to multivariate responses in the same manner as described in Algorithm 1, with multivariate residuals 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0018-05.png)


as non-conformity scores. This adaptation allows for the application of our methodology to a broader range of data scenarios involving dependent data with multivariate response variables, which were similarly studied in (Xu et al., 2024; Sun & Yu, 2024; Stankeviˇci¯ut˙e et al., 2021). 

## **B Proofs** 

The following lemma is adapted from the proof of Lemma 1 of Tibshirani et al. (2019); however, we do not assume exchangeability. 

**Lemma B.1** (Weights on quantile for non-exchangeable data) **.** _Given a sequence of random variables {V_ 1 _, . . . , Vn_ +1 _} with joint density P and a sequence of observations {v_ 1 _, . . . , vn_ +1 _}. Define the event_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0018-10.png)


_Then we have for i_ = 1 _, . . . , n_ + 1 _,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0018-12.png)


Note that when the residuals are exchangeable, _Wi[∗]_[= 1] _[/]_[(] _[n]_[ + 1)][, as also observed in Tibshirani et al.] (2019). Now we prove Proposition 4.1. 

_Proof of Proposition 4.1._ The proof assumes that _Y_[˜] _i_ , for _i_ = 1 _, . . . , n_ + 1, are almost surely distinct. However, the proof remains valid, albeit with more complex notations involving multisets, if this is not the case. Denote by Quantile _β_ (Q) the _β_ -quantile of the distribution Q on R, and by _δa_ the point mass distribution at _a ∈_ R. Define the event _E_ = _{{Y_[˜] 1 _, . . . , Y_[˜] _n_ +1 _}_ = _{v_ 1 _, . . . , vn_ +1 _}}_ . Then, by the tower 

18 

property, we have 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0019-01.png)


where _P[W][ ∗]_ =[�] _[n] i_ =1[+1] _[W][ ∗] i[δ][v] i_[, and in the last line, we have used the result from Lemma B.1,] 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0019-03.png)


Denote the weighted empirical distributions based on _W_[�] = _W_[�] ( _X_[˜] _n_ +1) as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0019-05.png)


This gives the marginal coverage gap as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0019-07.png)


where we denote by _d_ TV( _·, ·_ ) the total variation distance between probability measures, and the second inequality is due to the definition of the total variation distance. 

## **B.1 Proof of asymptotic conditional coverage of KOWCPI (Corollary 4.8 and Theorem 4.9)** 

In deriving the asymptotic conditional coverage property of KOWCPI, the consistency of the RNW estimator plays a crucial role. Therefore, we first introduce the proof of Proposition 4.6, which discusses the consistency of the CDF estimator. Corollary 4.7, which states the consistency of the quantile estimator, 

19 

is a natural consequence of Proposition 4.6 and leads us to the proof for our main results, Corollary 4.8 and Theorem 4.9. Proof of Proposition 4.6 adopts the similar strategy as Salha (2006) and Cai (2002). 

To prove Proposition 4.6, it is essential to first understand the nature of the adjustment weight _pi_ (˜ _x_ ). Thus, Lemma 3.1 is not only crucial for the practical implementation of the RNW estimator but also indispensable in the proof process of Proposition 4.6. 

_Proof of Lemma 3.1._ For display purposes, denote [ _X_ ]1 as _X_ 1. By (5), we have that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-03.png)


Let 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-05.png)


where _λ_ 1 _, λ_ 2 _∈_ R are the Lagrange multipliers. From _∂L/∂pi_ (˜ _x_ ) = 0 for _i_ = 1 _, . . . , n_ , we get 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-07.png)


Since _pi_ (˜ _x_ )’s sum up to 1 as in (4), letting _λ_ = _−λ_ 2 _/λ_ 1, we have 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-09.png)


Using (4) again with (A.4), this gives 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-11.png)


and therefore (8) holds. With (5), this gives 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-13.png)


Note that _[∂]_[2] _[L]_[(] _[γ]_[;] _[x]_[˜][)] _≥_ 0, implying that _L_ ( _·_ ; ˜ _x_ ) is indeed a convex function. _∂γ_[2] 

**Lemma B.2.** _Under the assumptions of Proposition 4.6, define_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-16.png)


_Then,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-18.png)



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0020-19.png)


_Proof._ Let 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-01.png)


Then, by Assumption 4.4, _Si_ is bounded above by some constant _C_ 1. Let 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-03.png)


for _k_ = 1 _,_ 2. Then, from (A.4), we have 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-05.png)


which gives 

Using the Taylor expansion (Wand & Jones, 1994), we obtain that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-08.png)


where the last equation comes from Assumptions 4.4-(i) and (ii). With a similar argument, we can derive that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-10.png)


using Assumption 4.4-(iii). Therefore, we obtain (A.5). 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-12.png)



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0021-13.png)


21 

˜ where _δi_ = 1 ( _Y_[˜] _t ≤ y_ ) _− F_ (˜ _y|X_[˜] _i_ ). Note that E[ _δi_ ] = 0 due to the tower property. Now, let 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-01.png)


Then, by Lemma B.2, we have that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-03.png)


Define the approximations for the terms in the decomposition presented in (A.6): 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-05.png)


so that 

_F_ “(˜ _y|x_ ˜) _− F_ (˜ _y|x_ ˜) = _{_ ( _nh[w]_ ) _[−]_[1] _[/]_[2] _J_ 1 + _J_ 2 _}J_ 3 _[−]_[1] _[{]_[1 +] _[ o][p]_[(1)] _[}][.]_ (A.8) Therefore, we will derive Proposition 4.6 by controlling the terms _J_ 1, _J_ 2 and _J_ 3. 

**Lemma B.3.** _Under the assumptions of Proposition 4.6,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-09.png)


## _Proof._ Let 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-11.png)


so that _J_ 1 = _n[−]_[1] _[/]_[2][ �] _[n] i_ =1 _[ξ][i]_[.][Since][ E][(] _[δ][i][|][X]_[ ˜] _[i]_[) = 0][, we have that][ E][(] _[ξ][i]_[) =][ E][(][E][(] _[ξ][i][|][X]_[ ˜] _[i]_[)) = 0][, and thus] 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-13.png)


Also, due to the stationarity of _X_[˜] _i_ , we have that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-15.png)


By Assumption 4.4, we have that lim _n→∞ bi_ (˜ _x_ ) = 1, which gives E( _bi_ ) = 1 + _op_ (1). Therefore, through expansion, we have 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0022-17.png)


22 

where _∗_ in the third line is the convolution operator. To control the second term in the right-hand side of _w_ (A.11), we borrow the idea of Masry (1986). Choose _dn_ = _O_ ( _h[−]_ 1+ _δ/_ 2 ) and decompose 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-01.png)


We have that _|bi_ (˜ _x_ ) _δi| ≤ C_ 2 for some constant _C_ 2. By Assumption 4.3-(iv), we obtain 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-03.png)


so that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-05.png)


By Assumption 4.4, we have _∥_ ( _X_[˜] _i − x_ ˜) _Kh_ ( _X_[˜] _i − x_ ˜) _∥≤ C_ 3, so that _|ξi| ≤ Ch[−][w/]_[2] . Then, by Theorem 17.2.1 of Ibragimov et al. (1971), we have that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-07.png)


Thus, we get 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-09.png)


Therefore, we obtain 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-11.png)


**Lemma B.4.** _Under the assumptions of Proposition 4.6,_ 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-13.png)



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-14.png)


_Proof._ By Assumption 1, (4) and (5), we have through expansion that 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0023-16.png)


23 

Since 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-01.png)


we have 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-03.png)


Finally, by applying the expansion argument routinely, we get 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-05.png)


_Proof of Proposition 4.6 (Cai, 2002; Salha, 2006)._ Combining Lemmas B.3 and B.4 with (A.8), Assumption 4.5 gives the result. 

_Proof of Corollary 4.7 (Cai, 2002)._ Given _x_ ˜, Proposition 4.6 implies uniform convergence of _F_[“] ( _·|x_ ˜) to _F_ ( _·|x_ ˜) in probability (Tucker, 1967, p.127-128) since _F_ ( _·|x_ ˜) is a CDF. That is, 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-08.png)


˜ ˜ Given _ε >_ 0, let _δ_ = _δ_ ( _ε_ ) := min _{β − F_ ( _Qβ_ (˜ _x_ ) _− ε|x_ ) _, F_ ( _Qβ_ (˜ _x_ ) + _ε|x_ ) _− β}_ . Note that _δ >_ 0 due to the uniqueness of the quantile. We have 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-10.png)


˜ The uniform convergence of _F_[“] ( _·|x_ ) in probability gives the result. _Proof of Corollary 4.8._ From the definition of _C_[ˆ] _t[α] −_ 1[in (3), we have] 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-12.png)


By Theorem 4.7, we have the consistency of _Q_[“] _β_ for all _β ∈_ (0 _,_ 1). On that, the continuous mapping theorem and Assumption 4.3 gives 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0024-14.png)


where the convergence is in probability. 

24 

_Proof of Theorem 4.9._ From the definition of _C_[“] _t[α] −_ 1[in (3), we have] 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0025-01.png)


where the last inequality comes from (A.8) and the definition of the discrete gap ∆. 

## **C Additional real data experiments** 

## **C.1 Wind/Solar data experiment results** 

We provide a more detailed description of the results for the solar and wind datasets introduced in Section 5. Figures A.1 and A.2 illustrate the rolling coverage and interval width results for the solar and wind datasets, respectively. As described in Section 5, KOWCPI consistently achieves the narrowest intervals while maintaining valid coverage. For qualitative explanations, we also include Figure A.3 that demonstrates the performance of KOWCPI, SPCI, and ACI on the Solar dataset. 

## **C.2 AAPL daily stock price** 

We compare KOWCPI with baseline methods using Apple’s daily closing stock price data from January 1, 2020, to December 12, 2022. This publicly available dataset can be accessed on Kaggle (https: //www.kaggle.com/datasets/paultimothymooney/stock-market-data). The goal is to construct confidence intervals for the daily closing prices. The first 80% of the data is used for training, with the remaining 20% reserved for evaluation. We can observe from Table A.1 that KOWCPI attains the narrowest interval. 

## **D Synthetic data analysis** 

## **D.1 Heteroskedastic mixture model** 

To evaluate the robustness of KOWCPI under heteroskedastic conditions, we conduct simulations using a heteroskedastic mixture model. This model incorporates an AR(1) component, a GARCH(1,1) structure 

25 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0026-00.png)


**----- Start of picture text -----**<br>
(a) Rolling coverage (boxplot) (b) Width of prediction intervals (boxplot)<br>**----- End of picture text -----**<br>



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0026-01.png)


**----- Start of picture text -----**<br>
(c) Rolling coverage over prediction time indices<br>**----- End of picture text -----**<br>


Figure A.1: Rolling coverage and width comparison on the solar dataset by different methods. 

for time-varying variance, and an additional small Gaussian noise term. The model is defined as 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0026-04.png)


This mixture model generates irregular, large volatility bursts, as evidenced in the simulated sample paths. Such extreme variations make conformal prediction challenging, as they require rapid adaptation to maintain valid coverage while avoiding overly wide intervals. 

We simulate five independent paths of the model and evaluate the performance of KOWCPI against baseline methods, with a target coverage of 90%. Unlike methods such as SPCI and SAOCP, which often overreact to volatility changes by producing excessively wide intervals and struggle to recover quickly after a burst, KOWCPI effectively adapts to these changes using its adaptive weighting mechanism. The results 

26 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0027-00.png)


**----- Start of picture text -----**<br>
(a) Rolling coverage (boxplot) (b) Width of prediction intervals (boxplot)<br>**----- End of picture text -----**<br>



![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0027-01.png)


**----- Start of picture text -----**<br>
(c) Rolling coverage over prediction time indices<br>**----- End of picture text -----**<br>


Figure A.2: Rolling coverage and width comparison on the wind dataset by different methods. 

for each sample path are summarized in Table A.2. 

## **D.2 Nonstationary time series** 

We also consider a model with strong seasonality, clearly representing non-stationarity: 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0027-06.png)


where _t[′]_ = mod( _t,_ 12) introduces a seasonal component with a 12-period cycle, and _Xt_ = [ _Yt−_ 100 _, . . . , Yt−_ 1] _[⊤]_ represents features of lagged values. The noise term _ϵt_ follows an AR(1) process, given by _ϵt_ = 0 _._ 6 _ϵt−_ 1 + _ξt_ , with _ξt ∼ N_ (0 _,_ 1). Table A.3 demonstrates that KOWCPI performs best in general among methods that achieve valid coverage of 90%. As KOWCPI actively leverages reweighting to assign higher weights to recent residuals, it demonstrates the ability to quickly adapt to changes in volatility. 

27 

Table A.1: Empirical marginal coverage and interval widths for confidence intervals of AAPL closing prices, with a target coverage of 90%. Standard deviations are calculated under three independent trials. 

||Coverage|Width|
|---|---|---|
|KOWCPI|0.912 (2.3e-3)|15.74 (1.2e-1)|
|SPCI|0.952 (3.3e-3)|19.39 (2.3e-1)|
|EnbPI|0.912 (8.7e-3)|38.67 (1.5e-1)|
|ACI|0.871 (1.7e-3)|44.84 (8.7e-2)|
|FACI|0.891 (5.2e-3)|43.93 (1.7e-1)|
|AgACI|0.878 (1.1e-2)|43.19 (2.6e-1)|
|SAOCP|0.619 (7.1e-4)|17.90 (4.3e-2)|
|SCP|0.796 (2.0e-3)|36.60 (1.0e-1)|



Table A.2: Empirical marginal coverage and interval widths from simulations using a heteroskedastic mixture model, with a target coverage of 90%. Here, C and W denote the empirical marginal coverage and average interval width, respectively. 

||Path 1<br>C<br>W|Path 2<br>C<br>W|Path 3<br>C<br>W|Path 4<br>C<br>W|Path 5<br>C<br>W|
|---|---|---|---|---|---|
|KOWCPI<br>SPCI<br>EnbPI<br>ACI<br>FACI<br>AgACI<br>SAOCP<br>SCP|0.91<br>4.61<br>0.99<br>8.68<br>0.93<br>5.47<br>0.93<br>5.21<br>0.92<br>5.11<br>0.93<br>5.20<br>0.79<br>3.58<br>0.93<br>5.17|0.89<br>5.57<br>0.89<br>5.85<br>0.87<br>5.56<br>0.92<br>6.99<br>0.92<br>7.10<br>0.91<br>6.83<br>0.82<br>4.62<br>0.91<br>6.73|0.90<br>11.44<br>0.97<br>18.46<br>0.91<br>15.60<br>0.92<br>14.11<br>0.92<br>13.75<br>0.93<br>13.17<br>0.72<br>7.39<br>0.93<br>14.19|0.93<br>8.84e3<br>0.90<br>8.53e3<br>0.91<br>9.14e3<br>0.89<br>1.79e4<br>0.89<br>1.88e4<br>0.88<br>1.58e4<br>0<br>36.1<br>0.84<br>1.06e4|0.92<br>23.09<br>1.00<br>99.22<br>0.96<br>74.62<br>0.95<br>27.84<br>0.92<br>24.28<br>0.92<br>25.83<br>0.67<br>10.87<br>0.97<br>29.23|



## **E Adaptive window length selection** 

In this section, we explore an adaptive selection of _w_ , where _w_ is no longer treated as a fixed hyperparameter but is instead dynamically adjusted for each time step. In KOWCPI, the window length _w_ originally serves as a hyperparameter that requires tuning. To alleviate the burden of manual tuning and introduce a more data-driven approach, we implement an adaptive selection process for _w_ based on a two-sample test on the residual distributions. 

At each time step _t_ , we compare the distributions two blocks of residuals using the two-sample Kolmogorov-Smirnov test: One block contains the most recent _w_ residuals (ˆ _εt−_ 1 _, . . . ,_ ˆ _εt−w_ ), and another block consists of the _w_ residuals immediately preceding, (ˆ _εt−w−_ 1 _, . . . ,_ ˆ _εt−_ 2 _w_ ). We then select the smallest _w_ for which the p-value drops below, e.g., 0.01. 

28 

Table A.3: Empirical marginal coverage and interval widths from nonstationary time-series simulations, with a target coverage of 90%. Standard deviations are calculated under five independent trials. 

||Coverage|Width|
|---|---|---|
|KOWCPI|0.90 (1.2e-3)|11.41 (2.3e-2)|
|SPCI|0.91 (2.7e-3)|11.73 (3.1e-2)|
|EnbPI|0.86 (1.2e-2)|10.45 (1.8e-2)|
|ACI|0.90 (1.1e-3)|12.57 (8.7e-3)|
|FACI|0.90 (4.1e-3)|12.65 (1.2e-2)|
|AgACI|0.90 (2.2e-3)|12.71 (1.4e-2)|
|SAOCP|0.82 (9.4e-4)|8.89 (3.2e-3)|
|SCP|0.90 (2.8e-3)|12.50 (4.1e-2)|



Table A.4: Comparison of KOWCPI on real datasets using pre-fixed window lengths selected by crossvalidation versus adaptive window selection based on the two-sample KS test. Target coverage is 90%, and standard deviation is derived across five independent trials. 

||Electric<br>Coverage<br>Width|Wind<br>Coverage<br>Width|Solar<br>Coverage<br>Width|
|---|---|---|---|
|Fixed_w_<br>Adaptive_w_|0.90 (2.3e-3)<br>0.23 (1.5e-3)<br>0.92 (3.0e-3)<br>0.22 (1.3e-3)|0.91 (2.8e-3)<br>2.41 (3.2e-2)<br>0.90 (4.4e-3)<br>2.44 (2.7e-2)|0.90 (1.2e-3)<br>48.8 (9.4e-1)<br>0.90 (1.3e-3)<br>50.6 (1.1e+0)|



While this is a simple preliminary approach, it allows for a data-driven and adaptive selection of _w_ without requiring additional hyperparameter tuning. Through experiments on the real data, we have confirmed that this method achieves comparable performance to _w_ values pre-selected by cross-validation (See Table A.4). Figure A.4 illustrates how the chosen window size changes over time on the Wind dataset. 

29 


![](markdown_output/kowcpi-2024_images/kowcpi-2024.pdf-0030-00.png)


**----- Start of picture text -----**<br>
(a) KOWCPI<br>40<br>— y<br>(b) SPCI<br>40<br>— yY<br>(c) ACI<br>**----- End of picture text -----**<br>


Figure A.3: Comparison of prediction intervals generated by KOWCPI, SPCI, and ACI on the Solar dataset. 

30 

Figure A.4: Dynamic adjustment of the window size ( _w_ ) for each prediction step on the Wind dataset, using the adaptive selection process based on the two-sample KS test. 

31 

