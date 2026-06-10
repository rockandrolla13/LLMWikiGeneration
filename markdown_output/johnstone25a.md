Proceedings of Machine Learning Research 266:1–20, 2025 Conformal and Probabilistic Prediction and Applications 

## **Exact and Approximate Conformal Inference for Multi-Output Regression** 

## **Chancellor Johnstone** 

_Air Force Institute of Technology_ ∗ **Eugene Ndiaye** † _Georgia Institute of Technology_ 

chancellor.johnstone@geaerospace.com 

e ndiaye@apple.com 

**Editor:** Khuong An Nguyen, Zhiyuan Luo, Harris Papadopoulos, Tuwe L¨ofstr¨om, Lars Carlsson and Henrik Bostr¨om 

## **Abstract** 

It is common in machine learning to estimate a response _y_ given covariate information _x_ . However, these predictions alone do not quantify any uncertainty associated with said predictions. One way to overcome this deficiency is with conformal inference methods, which construct a set containing the unobserved response with a prescribed probability. Unfortunately, even with a one-dimensional response, conformal inference is computationally expensive despite recent encouraging advances. In this paper, we explore multi-output regression, delivering exact derivations of conformal inference _p_ -values when the predictive model can be described as a linear function of _y_ . Additional contributions include 1) a multivariate extension of an existing root-based method for conformal prediction ( `rootCP` ) and 2) the introduction of union-based approximations for conformal prediction ( `unionCP` ). Both of these methods provide efficient ways of approximating the conformal prediction region for a wide array of multi-output predictors, both linear and nonlinear, while preserving computational advantages. We also provide both theoretical and empirical evidence of the effectiveness of our methods using both real-world and simulated data. 

Keywords: Uncertainty quantification, Nonlinear models, Prediction, Homotopy, Multitask, Multivariate regression. 

## **1. Introduction** 

In regression, we aim to predict (or estimate) some response _y_ given covariate information _x_ . These predictions alone deliver no information related to the uncertainty associated with the unobserved response, and thus, would benefit from the inclusion of a set Γ[(] _[α]_[)] ( _x_ ) such that, for any significance level _α ∈_ (0 _,_ 1), 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0001-12.png)


One method to generate Γ[(] _[α]_[)] ( _x_ ) is through conformal inference, which generates _conservative_ prediction sets for some unobserved response _y_ under only the assumption of exchangeability. Given a finite number of observations _Dn_ = _{_ ( _xi, yi_ ) _}[n] i_ =1[and][a][new][unlabelled][example] _xn_ +1, conformal prediction regions are generated through the repeated inversion of the test, 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0001-14.png)


> ∗ Currently at GE Aerospace. 

> † Currently at Apple. 

© 2025 C. Johnstone & E. Ndiaye. 

Johnstone Ndiaye 

where _yn_ +1 is the unobserved response for observation _n_ + 1 and _z_ is a candidate response value (Lei et al., 2018). With conformal inference, a _p_ -value for the hypothesis test shown in Equation 2 can be constructed by using an augmented dataset _Dn ∪_ ( _xn_ +1 _, z_ ) and comparing one’s ability to predict the new response _yn_ +1 to the already observed responses. A _conformal prediction set_ is the collection of candidates _z_ for which the null hypothesis is not rejected, _i.e.,_ when the error in predicting _z_ is not too high compared to others. 

The inversion of the test in Equation 2 is traditionally called “full” conformal prediction since it uses the entire dataset to learn a predictive model. Unfortunately, full conformal prediction is computationally demanding in many cases, with each new candidate point _z_ requiring a new model to be fit. To avoid this complexity, more efficient methods, _e.g.,_ split conformal inference (Vovk et al., 2005; Lei et al., 2018) and trimmed conformal inference (Chen et al., 2016), have been introduced, with trade-offs between computational efficiency and performance. 

Of interest to our work in this paper are _exact_ and _approximate_ conformal inference methods, which aim to reduce computational complexity without sacrificing performance. Nouretdinov et al. (2001) showed that with certain models, ridge regressors in particular, conformity scores for every observation in a dataset can be constructed as an affine function of the candidate value _z_ and only require training the model once. 

We extend the result of Nouretdinov et al. (2001) to predictors of the form 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0002-05.png)


where _y_ is an _n ×_ 1 vector of responses, _H_ is an _n × n_ matrix, and _y_ ˆ is an _n ×_ 1 vector of predictions. We note that _H_ can also be a function of a set of covariates, _e.g.,_ as with ridge regression, where _H_ = _X_ ( _X[⊤] X_ + _λI_ ) _[−]_[1] _X[⊤]_ . In reality, the restriction shown in Equation 3 is more general than ridge regression; we only require the predictions be linear functions of the input. In this paper, we refer to models that follow Equation 3 as _linear_ models; this is in contrast to the traditional usage of the term to reflect models that are linear with respect to their parameters. 

There also exist methods for the efficient construction of a conformal prediction set through the use of root-finding procedures. As one example, Ndiaye and Takeuchi (2021) introduces the `rootCP` algorithm, which utilizes a traditional root-finding approach, _i.e.,_ a bisection search, to find points on the boundary of a conformal prediction set with fewer model trainings than full conformal prediction. 

In more complex settings it might be of interest to construct a model for multiple responses, _i.e.,_ for some response _y_ with support _Y ⊂_ R _[q]_ , also known as multi-output (or multi-task) regression (Zhang and Yang, 2018; Borchani et al., 2015; Xu et al., 2019). Thus, we might wish to construct a prediction set such that some _q_ -dimension version of _y_ , say _y_ = ( _y_[(1)] _, . . . , y_[(] _[q]_[)] ) _[⊤]_ , is contained with some specified probability. 

**Contributions** With these potential scenarios is mind, we aim to extend exact conformal inference to the multi-output regression setting and subsume our contribution as 

- an extension of exact conformal _p_ -values to multiple dimensions with various predictors and conformity measures 

2 

Exact and Approximate Conformal Inference for Multi-Output Regression 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0003-01.png)


**----- Start of picture text -----**<br>
0 10 20 30 40 0 10 20 30 40<br>slump slump<br>100 100<br>90 90<br>80 80<br>70 70<br>flow flow<br>60 60<br>50 50<br>40 40<br>30 30<br>**----- End of picture text -----**<br>


Figure 1: Comparing `gridCP` contours (left) to _p_ -value change-point sets (right) constructed using _||·||_[2] _W_[with] _[ W]_[=][ˆΣ] _[−]_[1][ for an observation from] `[ cement]`[ dataset.][Each of the various colors] in the right plot correspond to the different _p_ -value change-point sets for each observation. 

- an exact approach for sampling points on the boundary of a conformal prediction set and a multivariate extension of `rootCP` , originally introduced in Ndiaye and Takeuchi (2021). 

- an approximate approach for conservative conformal prediction sets through `unionCP` . 

The extension of exact conformal inference to multiple dimensions makes use of _pvalue change-point sets_ (described in detail in Section 3) which allow for the description of conformal prediction regions. The extension of `rootCP` reduces the trade-off between various conformal inference methods, balancing the computational efficiency of split conformal prediction ( `splitCP` ) with the performance of full conformal prediction ( `fullCP` ). 

Table 1 summarizes the overall computational costs for each of these methods in terms of the number of model retraining iterations required to generate the conformal prediction region. We also include the computation complexity of the CP approximation provided by `gridCP` , where a finite grid of candidate points are tested to determine a prediction set. In contrast, `fullCP` comprises approaches where the exact conformal prediction set can be constructed in a closed-form. We include an example of _p_ -value change-point sets compared to `gridCP` sets in Figure 1. 

In the linear case, each of the methods for prediction set generation require the same number of model refits as `splitCP` . From Table 1, we can see that this is not the case of nonlinear models. We note that this does not account for the complexity of interval construction in each case. The rest of the paper is laid out as follows. Section 2 provides requisite background for the paper. Section 3 extends exact conformal inference to multiple dimensions delivers exact conformal inference results for several classical predictors. Section 

3 

Johnstone Ndiaye 

Table 1: Computational complexity of methods where _q_ is the response dimension, _n_ is the number of observations, _r_ is the cardinality of the candidate value set, _d_ is the number of search directions, and _ϵ_ is the tolerance. 

|Method|Nonlinear|
|---|---|
|`splitCP`<br>`gridCP`<br>`fullCP`<br>`rootCP`|_O_(_q_)<br>_O_(_rq_)<br>-<br>_O_<br>�<br>_dq_log2(1_/ϵ_)<br>�|



4 discusses several approaches to generate exact and approximate conformal prediction sets. Section 5 provides an empirical evaluation. Section 6 concludes the paper. 

**Notation** We denote the _n ×_ 1 design matrix as _X_ = ( _x_ 1 _, . . . , xn_ ) _[⊤]_ and the _n × q_ matrix of responses as _y_ = ( _y_[(1)] _, . . . , y_[(] _[q]_[)] ) _[⊤]_ , where _y_[(] _[k]_[)] is the vector of responses for the _k_ -th dimension. We define _Dn_ = _{_ ( _xi, yi_ ) _}[n] i_ =1[as][a][collection][of] _[n]_[observations,][where][the] _[i]_[-th] data tuple ( _xi, yi_ ) is made up of a covariate vector _xi_ and a _q_ -dimensioned response _yi_ , where _yi_ = ( _yi_[(1)] _, . . . , yi_[(] _[q]_[)] ). The augmented dataset is denoted by _Dn_ +1( _z_ ) = _Dn ∪{_ ( _xn_ +1 _, z_ ) _}_ . We denote the response matrix augmented with _z_ as _y_ ( _z_ ), where the candidate value _vector_ is defined as _z_ = ( _z_ 1 _, . . . , zq_ ) _[⊤]_ . Given _j ∈_ [ _n_ ], the rank of an element _uj_ among a sequence _{u_ 1 _, . . . , un}_ is defined as Rank( _uj_ ) =[�] _[n] i_ =1[1] _[u] i[≤][u] j[.]_ 

The main approach to perform the test inversion associated with Equation 2 relies on the Quantile Lemma (Tibshirani et al., 2019), which we include in this work (in a slightly different form) as Lemma 1 

**Lemma 1** _Let U_ 1 _, . . . , Un, Un_ +1 _be an exchangeable sequence of random variables. Then, for any α ∈_ (0 _,_ 1) _,_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0004-07.png)


One might consider a counter-example to Lemma 1 where _U_ 1 = _. . ._ = _Un_ +1 w.p. 1. We can solve this issue by adjusting the rank construction to include a tie-breaking component _τi_ where _τi ∼ U_ (0 _,_ 1) (Vovk et al., 2005; Lei et al., 2018). 

## **2. Conformal Inference** 

Originally introduced in Gammerman et al. (1998) as “transductive inference”, conformal inference (CI) was originally focused on providing inference with classification approaches. Vovk et al. (2005) provides a formalized introduction to conformal inference within regression. With the express purpose of inference, the goal of CI is to attach, in some fashion, a measure of uncertainty to a predictor, specifically through the construction of a conservative prediction set, _i.e.,_ one such that 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0004-11.png)


We wish to construct a prediction set for a new observation ( _xn_ +1 _, yn_ +1), where _xn_ +1 is some known covariate vector and _yn_ +1 is some, yet-to-be-observed response. Assuming each data pair ( _xi, yi_ ) and ( _xn_ +1 _, yn_ +1) are drawn exchangeably from some distribution _P_ , 

4 

Exact and Approximate Conformal Inference for Multi-Output Regression 

conformal inference generates conservative, finite sample-valid prediction sets in a distributionfree manner. In a prediction setting, test inversion for a particular candidate value _z_ is achieved by training the model of interest on an augmented data set _Dn_ +1( _z_ ). At this point, we leave our model of interest general, denoting the prediction of the _i_ -th observation based on a model trained with _Dn_ +1( _z_ ) as _y_ ˆ _i_ ( _z_ ). Following the refitting, each observation in the augmented data set receives a (non)conformity _measure_ , which determines the level of (non)conformity between itself and other observations. One popular, and particularly effective, conformity measure is the absolute residual 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0005-02.png)


We can construct the conformity _score_ associated with a candidate point _z_ as 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0005-04.png)


where _Si_ ( _z_ ) is the conformity measure for the data pair ( _xi, yi_ ) as a function of _z_ and _Sn_ +1( _z_ ) is the conformity measure associated with ( _xn_ +1 _, z_ ). Then, a _p_ -value for the test shown in Equation 2 can be constructed as 1 _− π_ ( _z_ ). In Section 3 we explicitly describe the _p_ -value associated with some _z_ in terms of _p-value change-point sets_ , which explicitly define where changes in rank occur between the conformity scores for specific observations. A prediction set for an unknown response _yn_ +1 associated with some covariate vector _xn_ +1 is 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0005-06.png)


Then, subuniformity holds for ( _n_ +1) _π_ ( _yn_ +1) = Rank( _Sn_ +1( _yn_ +1)) _,_ and Equation 4 holds for Γ[(] _[α]_[)] ( _xn_ +1). By the previous results, CI can also be utilized in the multivariate response case, where one is interested in quantifying uncertainty with respect to the joint behavior of a collection of responses, given a set of covariates. Thus, we can construct a multidimensional prediction set Γ[(] _[α]_[)] ( _xn_ +1) _⊂_ R _[q]_ such that Equation 4 holds when _yn_ +1 is some _q_ -dimensional random vector. 

The initial extension of conformal inference to the multivariate setting comes from Lei et al. (2015), which applies conformal inference to functional data, providing bounds associated with prediction “bands”. Diquigiovanni et al. (2022) extends and generalizes additional results for conformal inference on functional data. Joint conformal prediction sets outside the functional data setting are explored in Kuleshov et al. (2018) and Neeven and Smirnov (2018). Messoudi et al. (2020, 2021) provide extensions to these works through the use of Bonferroni- and copula-based conformal inference, respectively. Cella and Martin (2020), Kuchibhotla (2020) and Johnstone and Cox (2021) construct joint conformal sets through the use of depth measures, _e.g.,_ half-space and Mahalanobis depth, as the overall conformity measure. Messoudi et al. (2022) extends these works by generating adaptive conformal predictive regions in multiple dimensions. Applications of conformal inference have been seen in healthcare (Olsson et al., 2022), drug discovery (Cort´es-Ciriano and Bender, 2019; Eklund et al., 2015; Alvarsson et al., 2021), and decision support (Wasilefsky et al., 2023), to name a few. For a thorough treatment on conformal inference in general, we point the interested reader to Fontana et al. (2023) and Angelopoulos et al. (2023). We also point the reader to Hallin et al. (2010) for an approach to generate quantiles for multi-output regression. 

5 

Johnstone Ndiaye 

## **2.1. Computationally Efficient Conformal Inference** 

Due to the inherent model refitting required to generate prediction sets through full conformal inference, _i.e.,_ the testing of an infinite amount candidate points, more computationally efficient methods have been explored. We describe a subset of these methods in the following sections. Specifically, we focus on resampling-based and exact conformal inference. 

**Resampling Methods** Split conformal inference (Vovk et al., 2005; Lei et al., 2018) generates conservative prediction intervals under the same assumptions of exchangeability as _full_ conformal inference. However, instead of refitting a model for each new candidate value, split conformal inference utilizes a randomly selected partition of _Dn_ , which includes a training set _I_ 1 and a calibration set _I_ 2. First, a prediction model is fit using _I_ 1. Then, conformity measures are generated using out-of-sample predictions for observations in _I_ 2. The split conformal prediction interval for an incoming ( _xn_ +1 _, yn_ +1), when using the absolute residual as our comformity measure, is 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0006-04.png)


where _y_ ˆ _n_ +1 is the prediction for _yn_ +1 generated using the observations in _I_ 1, and _s_ is the _⌈_ ( _|I_ 2 _|_ + 1)(1 _− α_ ) _⌉_ -th largest conformity measure for observations in _I_ 2. In order to combat the larger widths and high variance associated with split conformal intervals, cross-validation (CV) approaches to conformal inference have also been implemented. The first CV approach was introduced in Vovk (2015) as cross-conformal inference with the goal to “smooth” inductive conformity scores across multiple folds. Aggregated conformal predictors Carlsson et al. (2014) generalize cross-conformal predictors, constructing prediction intervals through any exhangeable resampling method, _e.g.,_ bootstrap resampling. Other resampling-based conformal predictors also include CV+ and jackknife+ (Barber et al., 2021). For a more detailed review and empirical comparison of resampling-based conformal inference methods, we point the interested reader to Contarino et al. (2022). 

**Exact Conformal Inference for Piecewise Linear Estimators** In order to test a particular set of candidate values for inclusion in Γ[(] _[α]_[)] ( _xn_ +1), we must compare the conformity measure associated with our candidate data point to the conformity measures of our training data. Naively, this requires the refitting of our model for each new candidate value. However, Nouretdinov et al. (2001) showed that _Si_ ( _z_ ), constructed using Equation 5 in conjunction with a ridge regressor, varies piecewise-linearly as a function of the candidate value _z_ , eliminating the need to test a dense set of candidate points through model refitting. Other exact conformal inference methods include conformal inference through homotopy (Lei, 2019; Ndiaye and Takeuchi, 2019), influence functions (Bhatt et al., 2021; Cherubin et al., 2021), and root-finding approaches (Ndiaye and Takeuchi, 2021). While not exact, Ndiaye (2022) provide approximations to the full conformal prediction region through stability-based approaches. 

## **3. Conformal Inference for Multi-Output Regression** 

In the following sections, we extend the results in Nouretdinov et al. (2001) to multiple dimensions. While CI can be applied to any prediction or classification task, in this section 

6 

Exact and Approximate Conformal Inference for Multi-Output Regression 

we restrict each of our predictors, given an incoming observation ( _xn_ +1 _, z_ ), to the form 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0007-02.png)


where _y_ ˆ _i_[(] _[k]_[)] ( _zk_ ) is the prediction for the _i_ -th observation of the _k_ -th response dimension, _zk_ is the _k_ -th element of _z_ , and ( _·_ ) _i_ is the _i_ -th element of the vector argument. _Hk_ is an ( _n_ + 1) _×_ ( _n_ + 1) matrix where each element is a function of _x_ 1 _, . . . , xn_ +1. While _H_ does explicitly depend on _x_ 1 _, . . . , xn_ +1, we forgo including this dependency for notational convenience. We note that the restriction shown in Equation 9 is analogous to the restriction identified in Equation 3. We also note that while we define _Hk_ in Equation 9 as a function of both _xi_ and the augmented point _xn_ +1, this definition is general enough so as to include many classes of predictors. As an example, we can describe _Hk_ with respect to the _k_ -th response dimension for ridge regression as 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0007-04.png)


where _X_[˜] = ( _x_ 1 _, . . . , xn, xn_ +1) _[⊤]_ is the augmented design matrix. Additionally, we require that _Hk_ be constructed independently of _y_[(] _[k]_[)] , _i.e.,_ not as a function of _y_[(] _[k]_[)] . One focus of our paper is construction of exact _p_ -values for a given _z_ without retraining our model. We also identify how we construct explicit _p-value change-point sets_ , denoted as _Ei_ for the _i_ -th observation, where 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0007-06.png)


We note that _En_ +1 _≡_ R _[q]_ . Then, the _p_ -value associated with the hypothesis test shown in Equation 2 for any candidate point _z_ is 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0007-08.png)


The result of Nouretdinov et al. (2001) was extended to include both lasso and elastic net regressors in Lei (2019). For this paper, we utilize a generalized version, shown in Proposition 2. 

**Proposition 2** _Assume the fitted model as in Equation 3, where H ≡ H_ ( _xn_ +1 _, xi_ ) _. Then, if we define y_ ( _z_ ) = ( _y[⊤] , z_ ) _[⊤] , we can describe the vector of residuals associated with the augmented dataset and some candidate value z as_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0007-11.png)


_where A_ = � _I − H_ � _y_ (0) _and B_ = � _I − H_ �(0 _, . . . ,_ 0 _,_ 1) _[⊤] ._ With Proposition 2, we can then describe the conformity measure for the _i_ -th observation, when using Equation 5, as _Si_ ( _z_ ) = _|ai_ + _biz|_ , where _ai_ and _bi_ and the _i_ -th elements of _A_ and _B_ , respectively. 

In the following sections, we describe exact conformal inference results for conformity measure constructions using _|| · ||_[2] _W_[,][as][well][as][results][for][finding][points][on][the][boundary] of a conformal prediction set for any conformity measure. We include discussion on exact results using _ℓ_ 1 as a conformity measure in the extended version of this paper. 

7 

Johnstone Ndiaye 

**3.1. Exact** _p_ **-values with** _|| · ||_[2] _W_ 

In this section, we consider conformity measures of the form 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0008-03.png)


where _ri_ ( _z_ ) = _yi − y_ ˆ _i_ ( _z_ ), and _W_ is some _q × q_ matrix. For this construction of conformity score, Proposition 3 shows that _Si_ becomes quadratic with respect to _z_ . 

**Proposition 3** _Assume the fitted model y_ ˆ[(] _[k]_[)] ( _zk_ ) = _Hk_ ( _xn_ +1 _, xi_ ) _y_[(] _[k]_[)] ( _zk_ ) _for each response dimension k ∈_ [ _q_ ] _. Then, using Equation_ 13 _,_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0008-06.png)


_where ai_ = ( _a_ 1 _i, . . . , aqi_ ) _[⊤] , bi_ = ( _b_ 1 _i, . . . , bqi_ ) _[⊤] , and aki and bki are the i-th elements of the vectors Ak and Bk, respectively, defined as_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0008-08.png)


In order to maintain the probabalistic guarantees inherent to conformal inference, we require _W_ to be constructed exchangeably. Two constructions that satisfy exchangeability are: 1) _W_ constructed independently of _Dn_ +1( _z_ ), or 2) _W_ constructed using all observations within _Dn_ +1( _z_ ). However, in practice, setting _W_ = Σ[ˆ] _[−]_[1] , the observed inverse-covariance matrix associated with the residuals from our _q_ responses using a model constructed using only _Dn_ , performs well. The _p_ -value associated with some _z_ using sets constructed using Equation 13 is the same as in Equation 12. While Proposition 3 does not restrict the structure of _W_ , limiting _W_ to be a symmetric, positive semi-definite matrix ensures that the set _Ei_ is not only convex, but ellipsoidal. Without this additional restriction on the matrix _W_ , the _p_ -value change-point sets could be ill-formed, _i.e.,_ non-convex. For clarity, we describe how each _Ei_ can be constructed in practice when using _|| · ||_[2] _W_[by][describing] these regions in terms of conic sections in Section 3.1.1. 

## 3.1.1. Change-point Sets as Conic Sections 

With Proposition 3, _Sn_ +1( _z_ ) _− Si_ ( _z_ ) is the difference between two quadratic forms. Thus, we can describe the boundary of _Ei_ for every _i ∈_ [ _n_ ] as a _conic section_ . Specifically, we can describe the difference between the candidate conformity measure and the conformity measure for observation _i_ as, 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0008-12.png)


where _Vi_ = ( _a_ 1 _i_ + _b_ 1 _iz_ 1 _, . . . , aqi_ + _bqizq_ ) _[⊤]_ . 

Knowing we aim to find the boundary of each _Ei_ , _i.e.,_ the roots of Equation 15, we can expand the statement into the form of a conic section such that 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0008-15.png)


8 

Exact and Approximate Conformal Inference for Multi-Output Regression 

where _Mj_ , for any _j ∈_ [ _n_ + 1], is 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0009-02.png)


with _ajk_ and _bjk_ previously. If we additionally define the following: 

• ( _·_ ) _qq_ : the lower _q × q_ submatrix of the matrix argument 

• ( _·_ ) _i,−j_ : the _i_ -th row of the matrix argument, without the _j_ -th element of that row • _Li_ : the upper-triangular Cholesky matrix of ( _Mi[∗]_[)] _[qq]_[where] _[M] i[∗]_[=] _[ M][n]_[+1] _[ −][M][i]_ with, 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0009-06.png)


we can translate any point _s_ on the unit-ball to a point _z_ on the boundary of _Ei_ with 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0009-08.png)


## **3.2. Application to Some Classical Predictors** 

Many regression methods generate predictions that follow Equation 9. In the following section describe some results for local-constant and local linear regression. 

**Local Constant (Nadaraya-Watson) Regression** Kernel regression (Nadaraya, 1964; Watson, 1964) is a nonparametric regression technique that utilizes kernel density estimators (Parzen, 1962). Using some kernel, _e.g.,_ a Gaussian kernel, we can perform “local-constant” regression by using _Hk_ ( _xn_ +1 _, xi_ ) _≡ Hk_ ( _xn_ +1) = ( _w_ 1 _, . . . , wn_ +1) _[⊤]_ where each _wi_ is a vector of the normalized kernel values _Kh_ ( _·_ ) for each observation _xj_ centered on _xi_ , _i.e.,_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0009-12.png)


where _Kh_ is our multivariate kernel of choice. In this work, we utilize a _product_ kernel (Scott, 1992). 

**Local Linear Regression** In contrast to the local-constant regression with the NadarayaWatson estimator, local-linear regression (Fan, 1992) utilizes a weighted version of the design matrix. Local-linear regression constructs an estimate for _yi_ , as a function of the candidate value pair ( _xn_ +1 _, z_ ), by using an adjusted design matrix, 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0009-15.png)


and a diagonalized version of _wi_ , _i.e., G_ ( _xi_ ) = _diag_ ( _wi_ ), resulting in an _Hk_ matrix such that 

9 

Johnstone Ndiaye 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-01.png)


where ( _·_ ) _i_ is the _i_ -th element of the vector argument. 

## **4. Methods for Generating Prediction Sets** 

In this section, we discuss exact and approximate methods to generate prediction sets. These methods include sampling points directly from the prediction set boundary, as well as `rootCP` and `unionCP` approximation methods. 

## **4.1. Sampling Boundary Points via Directional Root-Finding** 

Computing conformal prediction sets typically requires retraining the model for every candidate replacement of _yn_ +1, which becomes computationally infeasible in high dimensions. To address this, we introduce an efficient approach for multi-output settings by approximating the boundary of the conformal prediction set through directional root-finding. Our method fixes a finite set of directions _d ∈_ R _[q]_ and samples boundary points along each line _z_ ( _t, d_ ) = _z_ 0 + _td_ , where _z_ 0 is a feasible interior point. These roots solve: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-07.png)


where _Si_ and _Sn_ +1 are conformity scores of observed and test points, respectively. Assuming linear predictors _y_ ˆ( _z_ ) = _Hy_ ( _z_ ), the conformity scores become: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-09.png)


with 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-11.png)


This reduces the conformal set intersection to solving a 1D root-finding problem 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-13.png)


**Solving with** _ℓ_ 1 **Score** For _ℓ_ 1 norms, we express: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-15.png)


where both _c_ ( _t_ ) and _s_ ( _t_ ) are piecewise constant, changing sign at: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-17.png)


This yields up to 2 _q_ change-points _{t[⋆]_ 1 _[, . . . , t][⋆]_ 2 _q[}]_[,][from][which][roots][are][computed][via:] 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0010-19.png)


10 

Exact and Approximate Conformal Inference for Multi-Output Regression 

**Solving with Mahalanobis Score** For general Mahalanobis scores, squaring the norm simplifies computation: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0011-02.png)


Roots are then obtained via the quadratic formula with coefficients: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0011-04.png)


## **Explicit Conformal Set Construction** 

Let _{t_ 1 _, . . . , tK}_ be the sorted intersection times. For any scalar _t_ , we define: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0011-07.png)


where _Ei_ = _{z_ : _Sn_ +1( _z_ ) _≤ Si_ ( _z_ ) _}_ along the line _z_ 0 + _td_ . The conformal region along direction _d_ is then: 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0011-09.png)


where _N_ ( _j_ ) counts how many intervals ( _tj, tj_ +1) lie in _Ei_ , and _M_ ( _j_ ) counts how many _tj_ endpoints are included. This slicing approach reduces multidimensional conformal set approximation to tractable 1D subproblems, enabling efficient boundary approximation using convex sets such as ellipses or hulls. 

## **4.2. Root-Based Approach Approximation via** `rootCP` 

Current efficient approaches to exact computation, limited to dimension one, are restricted to models that are piecewise-linear; this structure allows to track changes in the conformity function. We have extended these approaches to higher dimensions in the previous section. 

To go beyond linear structures, we can use approximate homotopy approaches as in Ndiaye and Takeuchi (2019) which, given an optimization tolerance, provided a discretization of all the values that _yn_ +1 can take. However, these approaches are also limited in dimension one and have an exponential complexity in the dimension of _yn_ +1. Convexity assumptions are also required, which, unfortunately, are not verified for more complex prediction models. 

We extend the approximations of conformal prediction in multiple dimensions by computing conformal prediction set boundaries directly. Unlike the one-dimensional case where the boundary is often two points, in multiple dimensions the boundary is continuous and, thus, uncountable, which makes finite-time computation impossible. To get around this difficulty, we will first fix a finite set of search directions; we will estimate the intersection points between the boundary of the conformal prediction set and the chosen direction. Then, we use the points on the boundary as a data base to fit a convex approximation, _e.g.,_ an ellipse or the convex hull, passing through these points. This estimates the set described in Equation 7 and is formally described below. 

We suppose that the conformal prediction set is _star-shaped_ , _i.e.,_ there exists a point _z_ 0 such that any other point _z_ within Γ[(] _[α]_[)] ( _xn_ +1) can be connected to _z_ 0 with a line segment within the set. We note that a star-shaped set are note necessarily convex; ellipsoidal sets (or any convex set) are inherently star-shaped. 

11 

Johnstone Ndiaye 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0012-01.png)


**----- Start of picture text -----**<br>
− 20 Convex Hull − 20 − 20<br>Fitted Ellipse<br>− 30 Target yn +1 − 30 − 30<br>− 40 − 40 − 40<br>− 50 − 50 − 50<br>− 60 − 60 − 60<br>− 70<br>− 30 − 20 − 10 0 − 30 − 25 − 20 − 15 − 10 − 5 0 − 30 − 20 − 10 0<br>**----- End of picture text -----**<br>


Figure 2: Illustration of the approximated conformal prediction set obtained fitting ellipse and convex hull given boundary points obtained by `rootCP` with various directions: three (left), ten (middle), and thirty (right). We use scikit-learn `make regression` to generate synthetic dataset with the parameters n ~~s~~ amples = 15, n ~~f~~ eatures = 5, n ~~t~~ argets = 2 is the dimension of in output _yn_ +1. 

**Outline of** `rootCP` For a direction _d ∈_ R _[q]_ , the intersection points between the boundary of Γ[(] _[α]_[)] ( _xn_ +1) and the line passing through _z_ 0 and directed by _d_ are obtained by solving the one dimensional equation 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0012-04.png)


We briefly describe the main steps: 

1. Fit a model _µ_ 0 on the observed training set _Dn_ and predict a feasible point _z_ 0 = _µ_ 0( _xn_ +1). 

2. For a collection of search directions _{d_ 1 _, . . . , dK}_ , perform a bisection search in [ _t_ min _,_ 0] and [0 _, t_ max] to output solutions _ℓ_[ˆ] ( _dk_ ) and _u_ ˆ( _dk_ ) of Equation 19 at direction _dk_ , after at most log2( _[t]_[max] _ϵ[−] r[t]_[min] ) iterations for an optimization tolerance _ϵr >_ 0. Notice that the star-shape assumption implies that we will have only two roots on the selected directions. 

3. Fit a convex set on the roots obtained at the previously _{ℓ_[ˆ] ( _dk_ ) _,_ ˆ _u_ ( _dk_ ) _}k∈_ [ _K_ ]. In practice, when one uses a least-squares ellipse as a convex approximation, a number of search directions _K_ proportional to the dimension _q_ of the target _yn_ +1 is sufficient. This is not necessarily the case for the convex hull. We refer to Figure 2 where we observe that many more search directions are needed to cover the conformal set when using the convex hull approximation. We also note that a minimum volume ellipsoid generated from the solutions generated would also be an appropriate approach to deliver a conservative convex approximation to the true prediction set. 

## **4.3.** `unionCP` **Approximation Method** 

After constructing the set _E_ for an incoming point _xn_ +1, it is initially unclear which regions _Ei_ make up various conformal prediction sets, let alone how we need to combine these regions to get the exact conformal prediction sets. Thus, we aim to provide an approximation of conformal prediction sets using the regions generated with the approaches introduced in 

12 

Exact and Approximate Conformal Inference for Multi-Output Regression 

Section 3. We provide Proposition 4 to bound error probabilities associated with potential combinations of these regions. 

**Proposition 4** _Let yn_ +1 _be such that_ ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn_ +1 _, yn_ +1) _are drawn exchangeably from P. Then, under the uniqueness of conformity measures, for a set S ⊂_ [ _n_ ] _, drawn exchangeably, it holds that_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0013-03.png)


## **Proof** 

First, consider a set _S ⊆_ [ _n_ ]. For any _z ∈/_[�] _i∈S[E][i]_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0013-06.png)


Then, using a set _S_ drawn exchangeably from [ _n_ ], for _yn_ +1 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0013-08.png)


_|S|_ Then, by Lemma 1, with the selection of _α_ = 1 _− n_ +1[,] 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0013-10.png)


Proposition 4 states that with the exchangeable selection of a subset of _E_ , the probability of the response _yn_ +1 being contained in the union of that subset is bounded-below by a function of cardinality. For example, if we wish to construct, say, a conservative 50% prediction set, we could select (exchangeably) a set _S ⊂_ [ _n_ ] such that _|S| ≥|E|/_ 2; the union of all sets within _S_ would provide a conservative prediction set, on average. We note that while our work emphasizes the use of _|| · ||_[2] _W_[,][Proposition][4][holds][for][any][conformity][measure] _[e.g.,][ℓ]_[1][.] 

While the union of a random selection of regions forms a conservative 1 _−|S|/_ ( _n_ + 1) prediction set, we can provide more intelligently constructed sets that are empirically less conservative. Suppose we provide an ordering of our regions, where _E_ ( _k_ ) is defined as the _k_ -th smallest region by volume. 

13 

Johnstone Ndiaye 

**Definition 5 (** `unionCP` **)** _A smaller_ (1 _− α_ ) _prediction set approximation can then be constructed as_ 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0014-02.png)


_where S_ 1 _−α_ = [ _⌈_ (1 _−α_ )( _n_ +1) _⌉_ ] _. We dub the approximation shown in Equation 20 as_ `unionCP` _._ 

By Proposition 4, `unionCP` generates an approximation that, at minimum, provides a region that is at least valid. We note that the set _S_ 1 _−α_ only depends on the the data values, and is, thus, generated exchangeably. 

We compare prediction sets constructed using `unionCP` to a random selection of regions for multiple predictors in Section 5. We find empirically that sets constructed using `unionCP` are less conservative than a random collection of _p_ -value change-point sets. Another approach using the union of regions generated through conformal prediction was introduced in Patel et al. (2024). We include an example of a prediction set approximation constructed with `unionCP` in Figure 4. 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0014-06.png)


**----- Start of picture text -----**<br>
0 10 20 30 40<br>slump<br>100<br>90<br>80<br>70<br>flow<br>60<br>50<br>40<br>30<br>**----- End of picture text -----**<br>


Figure 3: Example of `fullCP` prediction set (dotted black line) compared to the `unionCP` prediction set (union of colored _p_ -value change-point sets) constructed using _|| · ||_[2] _W_[with] _W_ = Σ[ˆ] _[−]_[1] for an observation from `cement` dataset. 

While Proposition 4 and the adjustment described in Equation 20 allow for conservative prediction sets, at times, the union of various _Ei_ does not explicitly describe a conformal prediction set exactly. Thus, `unionCP` provides (at worse) a conservative approximation of the true conformal prediction set. We also note that `unionCP` requires the computation of volumes for each change-point set. While this is not an issue when using _ℓ_ 1 or _|| · ||_[2] _W_[as][the] conformity measure, it might prohibitive for other conformity measures. 

14 

Exact and Approximate Conformal Inference for Multi-Output Regression 

## **5. Empirical Results** 

To provide empirical support for `unionCP` and `rootCP` , we consider three multi-output regression data sets, shown in Table 2. 

Table 2: Summary of data sets used in empirical exploration. 

|Data|# features|# responses|Source|
|---|---|---|---|
|enb|8|2|Tsanas and Xifara (2012)|
|jura|13|3|Goovaerts (1997)|
|cement|7|3|Yeh (2007)|



We first include results related to the empirical coverage of `unionCP` sets for our data sets of interest. We perform a small exploration, comparing the coverage of a random selection of _p_ -value change-point sets generated with linear regression (LS) to `unionCP` with other prediction methods. The results are shown in Figure 4. We note that the randomized approach significantly overcovers, while `unionCP` provides well-calibrated prediction sets. 

Figure 4: Comparison of empirical coverage with random selection of _k_ regions and `unionCP` for various datasets and predictors, including: linear regression (LS), Nadaraya-Watson (LC), and local-linear (LL) across 100 repetitions with _n_ = 40. 

For our `rootCP` comparision, we consider a reference benchmark; specifically, we have _π_ ( _yn_ +1) _≥ α_ with probability larger than 1 _− α_ . Hence, we can define the `oracleCP` as _π[−]_[1] ([ _α,_ + _∞_ )) where _π_ is obtained with a model fit optimized on the oracle data _Dn_ +1( _yn_ +1) on top of the root-based approach to find boundary points. We remind the reader that the target variable _yn_ +1 is not available in practice. The experiments were conducted with a coverage level of 0 _._ 9, _i.e., α_ = 0 _._ 1. We include results for a suite of complex regression models in Figures 5-7. 

We note that in all cases across all datasets, the `rootCP` approach is competitive with `splitCP` , and in most cases, surpasses `splitCP` in terms of volume. This result provides a trade-off between generating low-volume sets (with high computational load) through `fullCP` and high-volume sets through `splitCP` (with low computational load). 

15 

Johnstone Ndiaye 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0016-01.png)


**----- Start of picture text -----**<br>
2 . 00 4 . 0 4 . 0<br>1 . 75<br>3 . 5 3 . 5<br>1 . 50<br>1 . 25 3 . 0 3 . 0<br>1 . 00<br>2 . 5 2 . 5<br>0 . 75<br>oracleCP splitCP rootCP oracleCP splitCP rootCP oracleCP splitCP rootCP<br>cov = 0.89 cov = 0.89 cov = 0.89 cov = 0.91 cov = 0.91 cov = 0.91 cov = 0.9 cov = 0.9 cov = 0.9<br>T = 1.0 T = 0.65 T = 2.28 T = 1.0 T = 0.64 T = 28.07 T = 1.0 T = 0.59 T = 40.17<br>( a ) Multitask Enet ( b ) (Linear) Kernel Ridge ( c ) (RBF) Kernel Ridge<br>1 . 6 1 . 4<br>1 . 4 1 . 2<br>1 . 2 1 . 0<br>1 . 0<br>0 . 8<br>0 . 8<br>0 . 6<br>0 . 6<br>oracleCP splitCP rootCP oracleCP splitCP rootCP<br>cov = 0.91 cov = 0.9 cov = 0.91 cov = 0.89 cov = 0.86 cov = 0.89<br>T = 1.0 T = 0.61 T = 32.38 T = 1.0 T = 0.49 T = 6.64<br>( d ) Support Vector Regression ( e ) k -NN<br>Volume Volume Volume<br>Volume Volume<br>**----- End of picture text -----**<br>


Figure 5: Benchmarking the ellipse based conformal sets for several regression models on `enb` dataset. We display the lengths of the confidence sets over 100 random permutation of the data. We denoted ~~_cov_~~ the average coverage, and _T_ the average computational time normalized with the average time for computing `oracleCP` which requires a single model fit on the whole data. 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0016-03.png)


**----- Start of picture text -----**<br>
1 . 4<br>0 . 35<br>5<br>1 . 2<br>0 . 30<br>4 1 . 0<br>0 . 25<br>3 0 . 8<br>0 . 20<br>2 0 . 6<br>oracleCP splitCP rootCP oracleCP splitCP rootCP oracleCP splitCP rootCP<br>cov = 0.89 cov = 0.88 cov = 0.89 cov = 0.91 cov = 0.9 cov = 0.91 cov = 0.87 cov = 0.86 cov = 0.87<br>T = 1.0 T = 0.62 T = 4.4 T = 1.0 T = 0.69 T = 30.65 T = 1.0 T = 0.64 T = 39.87<br>( a ) Multitask Enet ( b ) (Linear) Kernel Ridge ( c ) (RBF) Kernel Ridge<br>1 . 4<br>25<br>1 . 2<br>20<br>15 1 . 0<br>10 0 . 8<br>5 0 . 6<br>0<br>oracleCP splitCP rootCP oracleCP splitCP rootCP<br>cov = 0.85 cov = 0.9 cov = 0.84 cov = 0.89 cov = 0.86 cov = 0.89<br>T = 1.0 T = 0.64 T = 21.24 T = 1.0 T = 0.49 T = 6.64<br>( d ) Support Vector Regression ( e ) k -NN<br>Volume Volume Volume<br>Volume Volume<br>**----- End of picture text -----**<br>


Figure 6: Benchmarking the ellipse based conformal sets for several regression models on `jura` dataset. We display the lengths of the confidence sets over 100 random permutation of the data. We denoted ~~_cov_~~ the average coverage, and _T_ the average computational time normalized with the average time for computing `oracleCP` which requires a single model fit on the whole data. 

16 

Exact and Approximate Conformal Inference for Multi-Output Regression 


![](markdown_output/johnstone25a_images/johnstone25a.pdf-0017-01.png)


**----- Start of picture text -----**<br>
3 . 5 7<br>12<br>3 . 0<br>6<br>2 . 5 10<br>5<br>2 . 0<br>8<br>1 . 5 4<br>1 . 0 6<br>oracleCP splitCP rootCP oracleCP splitCP rootCP oracleCP splitCP rootCP<br>cov = 0.95 cov = 0.93 cov = 0.95 cov = 0.85 cov = 0.82 cov = 0.85 cov = 0.87 cov = 0.89 cov = 0.87<br>T = 1.0 T = 0.66 T = 3.48 T = 1.0 T = 0.64 T = 25.15 T = 1.0 T = 0.66 T = 29.26<br>( a ) ( b ) (Linear) Kernel Ridge ( c ) (RBF) Kernel Ridge<br>10<br>6<br>8<br>5<br>6 4<br>4 3<br>2 2<br>oracleCP splitCP rootCP oracleCP splitCP rootCP<br>cov = 0.96 cov = 0.87 cov = 0.95 cov = 0.94 cov = 0.88 cov = 0.94<br>T = 1.0 T = 0.63 T = 20.29 T = 1.0 T = 0.64 T = 13.93<br>( d ) Support Vector Regression ( e ) k -NN<br>Volume Volume Volume<br>Volume Volume<br>**----- End of picture text -----**<br>


Figure 7: Benchmarking the ellipse based conformal sets for several regression models on `cement` dataset. We display the lengths of the confidence sets over 100 random permutation of the data. We denoted ~~_cov_~~ the average coverage, and _T_ the average computational time normalized with the average time for computing `oracleCP` which requires a single model fit on the whole data. 

## **6. Conclusion** 

In this paper, we introduced exact _p_ -values in multiple dimensions for predictors that are a linear function of the candidate value. Specifically, we discussed the exact construction of _p_ -values using _|| · ||_[2] _W_[.][Additionally,][we][introduced][a][multi-output][extension][to] `[rootCP]`[,] which can be used with a wide class of predictors. We also introduced `unionCP` , which allows for approximation of the conformal prediction set for linear predictors. We then showed empirical results with multiple predictors, including a subset of both linear and nonlinear predictors, while drastically reducing the computational requirements compared to `fullCP` . 

Other questions about the theoretical guarantees of our approach have yet to be answered. For example, we lack precise characterizations on the number of points to be sampled on the conformal set boundary. Besides the conformal sets presented in this paper, these questions are equally relevant to the construction of any high-dimensional confidence sets. Future work might also explore the performance of these approximations with a higher dimension response and under conditions related to dependence or covariate shift. 

## **References** 

- Jonathan Alvarsson, Staffan Arvidsson McShane, Ulf Norinder, and Ola Spjuth. Predicting with confidence: using conformal prediction in drug discovery. _Journal of Pharmaceutical Sciences_ , 110(1):42–49, 2021. 

17 

Johnstone Ndiaye 

- Anastasios N Angelopoulos, Stephen Bates, et al. Conformal prediction: A gentle introduction. _Foundations and Trends® in Machine Learning_ , 16(4):494–591, 2023. 

- Rina Foygel Barber, Emmanuel J Candes, Aaditya Ramdas, and Ryan J Tibshirani. Predictive inference with the jackknife+. _The Annals of Statistics_ , 49(1):486–507, 2021. 

- Umang Bhatt, Adrian Weller, and Giovanni Cherubin. Fast conformal classification using influence functions. In _Conformal and Probabilistic Prediction and Applications_ , pages 303–305. PMLR, 2021. 

- Hanen Borchani, Gherardo Varando, Concha Bielza, and Pedro Larranaga. A survey on multi-output regression. _Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery_ , 5(5):216–233, 2015. 

- Lars Carlsson, Martin Eklund, and Ulf Norinder. Aggregated conformal prediction. In _IFIP International Conference on Artificial Intelligence Applications and Innovations_ , pages 231–240. Springer, 2014. 

- Leonardo Cella and Ryan Martin. Valid distribution-free inferential models for prediction. _arXiv preprint arXiv:2001.09225_ , 2020. 

- Wenyu Chen, Zhaokai Wang, Wooseok Ha, and Rina Foygel Barber. Trimmed conformal prediction for high-dimensional models. _arXiv preprint arXiv:1611.09933_ , 2016. 

- Giovanni Cherubin, Konstantinos Chatzikokolakis, and Martin Jaggi. Exact optimization of conformal predictors via incremental and decremental learning. In _International Conference on Machine Learning_ , pages 1836–1845. PMLR, 2021. 

- Alex Contarino, Christine Shubert Kabban, Chancellor Johnstone, and Fairul Mohd-Zaid. Constructing prediction intervals with neural networks: an empirical evaluation of bootstrapping and conformal inference methods. _arXiv preprint arXiv:2210.05354_ , 2022. 

- Isidro Cort´es-Ciriano and Andreas Bender. Concepts and applications of conformal prediction in computational drug discovery. _arXiv preprint arXiv:1908.03569_ , 2019. 

- Jacopo Diquigiovanni, Matteo Fontana, and Simone Vantini. Conformal prediction bands for multivariate functional data. _Journal of Multivariate Analysis_ , 189:104879, 2022. 

- Martin Eklund, Ulf Norinder, Scott Boyer, and Lars Carlsson. The application of conformal prediction to the drug discovery process. _Annals of Mathematics and Artificial Intelligence_ , 74:117–132, 2015. 

- Jianqing Fan. Design-adaptive nonparametric regression. _Journal of the American statistical Association_ , 87(420):998–1004, 1992. 

- Matteo Fontana, Gianluca Zeni, and Simone Vantini. Conformal prediction: a unified review of theory and new challenges. _Bernoulli_ , 29(1):1–23, 2023. 

- Alexander Gammerman, Vladimir Vovk, and Vladimir Vapnik. Learning by transduction. In _Proceedings of the Fourteenth conference on Uncertainty in artificial intelligence_ , pages 148–155, 1998. 

18 

Exact and Approximate Conformal Inference for Multi-Output Regression 

Pierre Goovaerts. _Geostatistics for natural resources evaluation_ . Applied Geostatistics, 1997. 

- Marc Hallin, Davy Paindaveine, Miroslav Siman,[ˇ] Ying Wei, Robert Serfling, Yijun Zuo, Linglong Kong, and Ivan Mizera. Multivariate quantiles and multiple-output regression quantiles: From l1 optimization to halfspace depth [with discussion and rejoinder]. _The Annals of Statistics_ , pages 635–703, 2010. 

- Chancellor Johnstone and Bruce Cox. Conformal uncertainty sets for robust optimization. In _Conformal and Probabilistic Prediction and Applications_ , pages 72–90. PMLR, 2021. 

- Arun Kumar Kuchibhotla. Exchangeability, conformal prediction, and rank tests. _arXiv preprint arXiv:2005.06095_ , 2020. 

- Alexander Kuleshov, Alexander Bernstein, and Evgeny Burnaev. Conformal prediction in manifold learning. In _Conformal and Probabilistic Prediction and Applications_ , pages 234–253, 2018. 

- Jing Lei. Fast exact conformalization of the lasso using piecewise linear homotopy. _Biometrika_ , 106(4):749–764, 2019. 

- Jing Lei, Alessandro Rinaldo, and Larry Wasserman. A conformal prediction approach to explore functional data. _Annals of Mathematics and Artificial Intelligence_ , 74(1):29–43, 2015. 

- Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J Tibshirani, and Larry Wasserman. Distribution-free predictive inference for regression. _Journal of the American Statistical Association_ , 113(523):1094–1111, 2018. 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Conformal multi-target regression using neural networks. In _Conformal and Probabilistic Prediction and Applications_ , pages 65–83. PMLR, 2020. 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Copula-based conformal prediction for multi-target regression. _arXiv preprint arXiv:2101.12002_ , 2021. 

- Soundouss Messoudi, S´ebastien Destercke, and Sylvain Rousseau. Ellipsoidal conformal inference for multi-target regression. _Proceedings of Machine Learning Research_ , 179:1–13, 2022. 

- Elizbar A Nadaraya. On estimating regression. _Theory of Probability & Its Applications_ , 9 (1):141–142, 1964. 

- Eugene Ndiaye. Stable conformal prediction sets. In _International Conference on Machine Learning_ , pages 16462–16479. PMLR, 2022. 

- Eugene Ndiaye and Ichiro Takeuchi. Computing full conformal prediction set with approximate homotopy. _arXiv preprint arXiv:1909.09365_ , 2019. 

- Eugene Ndiaye and Ichiro Takeuchi. Root-finding approaches for computing conformal prediction set. _arXiv preprint arXiv:2104.06648_ , 2021. 

19 

Johnstone Ndiaye 

- Jelmer Neeven and Evgueni Smirnov. Conformal stacked weather forecasting. In _Conformal and Probabilistic Prediction and Applications_ , pages 220–233, 2018. 

- Ilia Nouretdinov, Thomas Melluish, and Volodya Vovk. Ridge regression confidence machine. In _ICML_ , pages 385–392. Citeseer, 2001. 

- Henrik Olsson, Kimmo Kartasalo, Nita Mulliqi, Marco Capuccini, Pekka Ruusuvuori, Hemamali Samaratunga, Brett Delahunt, Cecilia Lindskog, Emiel AM Janssen, Anders Blilie, et al. Estimating diagnostic uncertainty in artificial intelligence assisted pathology using conformal prediction. _Nature communications_ , 13(1):7761, 2022. 

- Emanuel Parzen. On estimation of a probability density function and mode. _The annals of mathematical statistics_ , 33(3):1065–1076, 1962. 

- Yash P Patel, Sahana Rayan, and Ambuj Tewari. Conformal contextual robust optimization. In _International Conference on Artificial Intelligence and Statistics_ , pages 2485–2493. PMLR, 2024. 

- David W Scott. _Multivariate density estimation: theory, practice, and visualization_ . John Wiley & Sons, 1992. 

- Ryan J Tibshirani, Rina Foygel Barber, Emmanuel Candes, and Aaditya Ramdas. Conformal prediction under covariate shift. _Advances in neural information processing systems_ , 32, 2019. 

- Athanasios Tsanas and Angeliki Xifara. Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools. _Energy and buildings_ , 49:560–567, 2012. 

- Vladimir Vovk. Cross-conformal predictors. _Annals of Mathematics and Artificial Intelligence_ , 74(1):9–28, 2015. 

- Vladimir Vovk, Alex Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ . Springer Science & Business Media, 2005. 

- Devin Wasilefsky, William Caballero, Chancellor Johnstone, Nathan Gaw, and Phillip Jenkins. Responsible machine learning for united states air force pilot candidate selection, 2023. 

- Geoffrey S Watson. Smooth regression analysis. _Sankhy¯a: The Indian Journal of Statistics, Series A_ , pages 359–372, 1964. 

- Donna Xu, Yaxin Shi, Ivor W Tsang, Yew-Soon Ong, Chen Gong, and Xiaobo Shen. Survey on multi-output learning. _IEEE transactions on neural networks and learning systems_ , 31 (7):2409–2429, 2019. 

- I-Cheng Yeh. Modeling slump flow of concrete using second-order regressions and artificial neural networks. _Cement and concrete composites_ , 29(6):474–480, 2007. 

- Yu Zhang and Qiang Yang. An overview of multi-task learning. _National Science Review_ , 5 (1):30–43, 2018. 

20 

