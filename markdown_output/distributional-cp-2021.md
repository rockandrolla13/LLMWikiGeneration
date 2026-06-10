# Distributional conformal prediction[∗] 

Victor Chernozhukov[†] Kaspar Wüthrich[‡] Yinchu Zhu[§] 

First version on arXiv: September, 17 2019 This version: August 24, 2021 

## **Abstract** 

We propose a robust method for constructing conditionally valid prediction intervals based on models for conditional distributions such as quantile and distribution regression. Our approach can be applied to important prediction problems including cross-sectional prediction, _k_ -step-ahead forecasts, synthetic controls and counterfactual prediction, and individual treatment effects prediction. Our method exploits the probability integral transform and relies on permuting estimated ranks. Unlike regression residuals, ranks are independent of the predictors, allowing us to construct conditionally valid prediction intervals under heteroskedasticity. We establish approximate conditional validity under consistent estimation and provide approximate unconditional validity under model misspecification, overfitting, and with time series data. We also propose a simple “shape” adjustment of our baseline method that yields optimal prediction intervals. 

**Keywords:** prediction intervals, quantile regression, distribution regression, conditional validity, model-free validity 

> ∗We are grateful to the Editor, two anonymous referees, Dimitris Politis, and Allan Timmermann for valuable comments. Wüthrich is also affiliated with CESifo and the Ifo Institute. Chernozhukov gratefully acknowledges funding by the National Science Foundation. The usual disclaimer applies. 

> †Massachusetts Institute of Technology; 50 Memorial Drive, E52-361B, Cambridge, MA 02142, USA; Email: `vchern@mit.edu` 

> ‡Department of Economics, University of California San Diego, 9500 Gilman Dr., La Jolla, CA 92093, USA; Email: `kwuthrich@ucsd.edu` 

> §Brandeis University; 415 South Street, Waltham, MA 02453, USA; Email: `yinchuzhu@brandeis.edu` 

1 

## **1 Introduction** 

We develop a robust approach for constructing prediction intervals based on models for conditional distributions. The proposed method is generic and can be implemented using a great variety of flexible and powerful methods, including conventional quantile regression (QR) (Koenker and Bassett, 1978), distribution regression (DR) (e.g., Foresi and Peracchi, 1995; Chernozhukov et al., 2013), as well as non-parametric and high-dimensional machine learning methods such as quantile neural networks (e.g., Taylor, 2000) and quantile trees and random forests (e.g., Chaudhuri and Loh, 2002; Meinshausen, 2006). 

We observe data _{_ ( _Yt, Xt_ ) _}[T] t_ =1[,][where] _[Y][t]_[is][a][continuous][outcome][of][interest][and] _[X][t]_ is a _p ×_ 1 vector of predictors. Our task is to predict _YT_ +1 given knowledge of _XT_ +1. This setting encompasses many classical cross-sectional and time series prediction problems. Moreover, our approach can be applied to synthetic control settings where the goal is to predict counterfactuals in the absence of a policy intervention (e.g., Cattaneo et al., 2019; Chernozhukov et al., 2021) and to the problem of predicting individual treatment effects (e.g., Kivaranovic et al., 2020b; Lei and Candès, 2020). 

With iid (or exchangeable data), standard conformal prediction methods, which are based on modeling the conditional mean, yield prediction intervals _C_[�] (1 _−α_ ) that satisfy 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0002-04.png)


for a given miscoverage level _α ∈_ (0 _,_ 1). A prediction interval satisfying this property is said to be _unconditionally_ valid. Unconditionally valid prediction intervals guarantee accurate coverage on average, treating ( _YT_ +1 _, XT_ +1) and _{_ ( _Yt, Xt_ ) _}[T] t_ =1[as][random.] 

However, in many applications, unconditional validity may be unsatisfactory. Let us consider three examples; see Romano et al. (2019a); Foygel Barber et al. (2021) for further examples and discussions. First, from a fairness perspective, data-driven recommendation systems should guarantee equalized coverage across protected groups, in which case the goal is to construct prediction intervals that are valid conditional on a protected attribute such as race or gender (Romano et al., 2019a). Second, as in Section 5.1, consider the problem of predicting stock returns given the realized volatility. Since the distribution of returns is more dispersed when the variance is higher, a natural prediction algorithm should yield wider prediction intervals for higher values of volatility. That is, the prediction interval should be valid conditional on the known value of realized volatility rather than on average. Third, as in Section 5.2, suppose our goal is to predict wages based on an individual’s education and experience. An unconditionally valid prediction interval exhibits coverage 90% on average across all individuals but may contain the true wage of high-school dropouts with no work 

2 

experience with probability zero. A more useful prediction interval should exhibit correct coverage conditional on an individual’s observed education and experience and contain the true wage with 90% probability for every single individual. 

Motivated by this discussion, we develop a _distributional conformal prediction_ (DCP) method for constructing prediction intervals that are approximately valid conditional on the full vector of predictors _XT_ +1, while treating _YT_ +1 and _{_ ( _Yt, Xt_ ) _}[T] t_ =1[as][random:] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0003-02.png)


A prediction interval satisfying property (2) as _T →∞_ is said to be approximately _conditionally_ valid.[1] 

While the requirement in (2) is natural in many applications, there are also other notions of conditional validity. Instead of conditioning on _XT_ +1 (object conditional), one can also study the conditional coverage probability given the training sample _{_ ( _Yt, Xt_ ) _}[T] t_ =1[(training] conditional) or given _YT_ +1 (label conditional) or combinations of them; see Vovk (2012) for a detailed discussion. By Proposition 2 of Vovk (2012), inductive conformal predictions (also known as split-sample conformal predictions) automatically achieve training conditional validity as long as the training sample is large enough. In classification problems (the support of _YT_ +1 is a finite set), label conditional validity is often of great interest as it is important to know the error rates for different categories and provides useful information on false positive and false negative rates (Vovk, 2012). In Vovk (2012), label conditional validity is achieved by forming the conformity score within each category. Both training and label conditional validity can be achieved in a distribution-free way, i.e., for a given procedure, the conditional validity holds for any distribution of the data. 

However, object conditional validity in the sense of (2) cannot be achieved in a distributionfree way for non-trivial predictions. By Vovk (2012); Lei and Wasserman (2014); Foygel Barber et al. (2021), any prediction set satisfying (2) for every probability distribution of ( _Xt, Yt_ ) has infinite Lebesgue measure with non-trivial probability. Therefore, we only aim to achieve (2) for a limited class of probability distributions. The construction of the proposed prediction set _C_[�] (1 _−α_ ) relies on learning the conditional distribution _Yt | Xt_ and we only hope for conditional validity in (2) in the class of distributions that can be learned well. In particular, this class of distributions are those satisfying our regularity conditions. 

Our empirical results demonstrate the importance of using DCP instead of standard conformal prediction methods based on modeling the conditional mean. When predicting 

> 1See, for example, Lei and Wasserman (2014); Sesia and Candes (2020); Foygel Barber et al. (2021) for a further discussion of the difference between conditional and unconditional validity. 

3 

daily stock returns in Section 5.1, the coverage probability of the 90% mean-based conformal prediction interval can drop to around 50% when the realized volatility is high. By contrast, DCP provides a coverage probability close to 90% for all values of realized volatility. This finding is important since volatility tends to be high during periods of crisis when accurate risk assessments are most needed. When predicting wages in Section 5.2, we find that the DCP prediction intervals contain the true wage with probability close to 90% for most individuals, whereas standard mean-based conformal prediction intervals either substantially under- or overcover. 

To motivate DCP, note that a conditionally valid prediction interval is given by 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0004-02.png)


where _Q_ ( _τ, x_ ) is the _τ_ -quantile of _Yt_ given _Xt_ = _x_ . To implement the prediction interval (3), a plug-in approach would replace _Q_ with a consistent estimator _Q_[ˆ] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0004-04.png)


This approach exhibits two well-known drawbacks. First, it will often exhibit undercoverage in finite samples (e.g., Romano et al., 2019b). Second, it is neither conditionally nor unconditionally valid under misspecification. 

We build upon conformal prediction (Vovk et al., 2005, 2009) and use the conditional ranking as a conformity score. This choice is particularly useful when working with regression models for conditional distributions such as QR and DR.[2] Our method is conditionally valid under correct specification, while the construction of the procedure as a conformal prediction method guarantees the unconditional validity under misspecification. Let _F_ ( _y, x_ ) = _P_ ( _Yt ≤ y | Xt_ = _x_ ) denote the conditional cumulative distribution function (CDF) of _Yt_ given _Xt_ = _x_ . Throughout the paper, we assume that _F_ ( _·, Xt_ ) is a continuous function almost surely. Our method is based on the probability integral transform, which states that the _conditional rank_ , _Ut_ := _F_ ( _Yt, Xt_ ), has the uniform distribution on (0 _,_ 1) and is independent of _Xt_ . 

To construct the prediction interval, we test the plausibility of each _y ∈_ R. By the probability integral transform, conditional on _XT_ +1, _F_ ( _YT_ +1 _, XT_ +1) belongs to [ _α/_ 2 _,_ 1 _− α/_ 2] with probability 1 _−α_ . Thus, collecting all values _y ∈_ R satisfying _F_ ( _y, XT_ +1) _∈_ [ _α/_ 2 _,_ 1 _−α/_ 2] yields a conditionally valid prediction interval in the sense of (2). We operationalize this idea by proposing a conformal prediction procedure based on the estimated ranks, _U_[ˆ] _t_[(] _[y]_[)] := ˆ ˆ _F_[(] _[y]_[)] ( _Yt, Xt_ ). For each _y ∈_ R, _F_[(] _[y]_[)] is an estimator of _F_ obtained based on the augmented 

> 2This transformation is also very useful in other prediction problems (e.g., Politis, 2015). 

4 

data, _{_ ( _Yt, Xt_ ) _}[T] t_ =1[+1][,][where] _[Y][T]_[+1][=] _[y]_[.] Data augmentation is a key feature of conformal prediction. It implies the model-free unconditional exact finite-sample validity with iid (or exchangeable) data and, thus, guards against model misspecification and overfitting. Without data augmentation, the resulting prediction intervals are not exactly valid, not even with correct specification and iid data. 

Our baseline method asymptotically coincides with the oracle interval in (3). This oracle interval may not be the shortest possible prediction interval in general. Therefore, we also develop a simple and easy-to-implement adjustment of our baseline method for improving efficiency, which we refer to as _optimal DCP_ . In Section 5.2, we show empirically that optimal DCP yields shorter prediction intervals than baseline DCP when the conditional distribution is skewed. 

We establish the following theoretical performance guarantees for the baseline and optimal DCP. 

- (i) Asymptotic conditional validity under consistent estimation of the conditional CDF 

- (ii) Unconditional validity under model misspecification: 

   - (a) Finite-sample validity with iid (or exchangeable) data 

   - (b) Asymptotic validity with time series data 

- (iii) For optimal DCP: 

   - (a) Under weak conditions: asymptotic conditional validity and optimality (shortest length) 

   - (b) Under strong conditions: asymptotic convergence to the optimal prediction interval 

## **1.1 Motivating Example** 

We illustrate the advantages of DCP relative to mean-based conformal prediction (e.g., Lei et al., 2018) based on the following simple analytical example. 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0005-12.png)


Our motivating example draws on Koenker and Bassett (1982); Koenker (2005a); Lei et al. (2018); Romano et al. (2019b). We focus on the population conformal prediction (or oracle) problem under correct specification and abstract from finite sample issues. 

Mean-based conformal prediction is based on the residuals _Rt_ = _Yt − E_ ( _Yt | Xt_ ) = _Yt − Xt_ = _Xtεt_ . The mean-based prediction interval is 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0005-15.png)


5 

where _Q|R|_ (1 _− α_ ) is the (1 _− α_ )-quantile of the distribution of _|Rt|_ . An important property and drawback of _C_ (1[reg] _−α_ )[is][that][its][length,][2] _[ ·][ Q][|][R][|]_[(1] _[ −][α]_[)][,][is][fixed][and][does][not][depend][on] _XT_ +1 = _x_ (Lei et al., 2018; Romano et al., 2019b). This feature implies that _C_ (1[reg] _−α_ )[is][not] adaptive to the heteroskedasticity in the location-scale model (5) and not conditionally valid. DCP is based on the ranks _Ut_ = Φ ( _εt_ ), where Φ( _·_ ) is the CDF of _N_ (0 _,_ 1). The DCP prediction interval is 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0006-01.png)


where _Q|ε|_ (1 _− α_ ) = Φ _[−]_[1] (1 _− α/_ 2) is the (1 _− α_ )-quantile of _|εt|_ . Unlike _C_ (1[reg] _−α_ )[,][the][length][of] _C_ (1[dcp] _−α_ )[,][2] _[x][ ·][ Q][|][ε][|]_[(1] _[ −][α]_[)][,][depends][on] _[ X][T]_[+1][=] _[ x]_[.][Our construction][automatically adapts][to the] heteroskedasticity in model (5) and is conditionally valid. 

Figure 2 provides an illustration. Panel (a) shows that the conditional length of _C_ (0[reg] _._ 9)[is] constant, whereas the length of _C_ (0[dcp] _._ 9)[varies][as][a][function][of] _[x]_[.] _[C]_ (0[dcp] _._ 9)[is][shorter][than] _[C]_ (0[reg] _._ 9) for low values and wider for high values of _x_ . Panel (b) shows that _C_ (0[dcp] _._ 9)[is][valid][for][all] _x_ , whereas _C_ (0[reg] _._ 9)[overcovers][for][low][values][and][undercovers][for][high][values][of] _[x]_[.][Figure][2] illustrates the advantage of our method. For predictor values where the conditional variance is low, it yields shorter prediction intervals, while ensuring conditional coverage for values where the conditional dispersion is large by suitably enlarging the prediction interval. 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0006-04.png)


**----- Start of picture text -----**<br>
(a) Conditional length 90% prediction interval (b) Conditional coverage 90% prediction interval<br>Distributional conformal prediction<br>Mean−based conformal prediction<br>Distributional conformal prediction<br>Mean−based conformal prediction<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>X X<br>3.5 1.0<br>3.0<br>0.9<br>2.5<br>2.0<br>0.8<br>1.5<br>Conditional length<br>1.0 Conditional coverage<br>0.7<br>0.5<br>0.0 0.6<br>**----- End of picture text -----**<br>


Figure 1: Motivating example 

## **1.2 Related Literature** 

We build on and contribute to the literature on conformal prediction (e.g., Vovk et al., 2005; Vovk, 2012; Vovk et al., 2009; Lei et al., 2013; Lei and Wasserman, 2014; Lei et al., 2018; 

6 

Chernozhukov et al., 2018; Romano et al., 2019b), the literature on model-free prediction (Politis, 2013, 2015), as well as the literature on quantile prediction methods (see, e.g., Komunjer, 2013, for a review). 

Within the conformal prediction literature, our paper is most closely related to Lei and Wasserman (2014), Lei et al. (2018), and Romano et al. (2019b). Lei and Wasserman (2014) propose conditionally valid and asymptotically efficient conformal prediction intervals based on estimators of the conditional density. We take a different and complementary approach, allowing researchers to leverage powerful regression methods for modeling conditional distributions, including QR and DR approaches. Lei et al. (2018) develop conformal prediction methods based on regression models for conditional expectations. However, as discussed in Section 1.1, this approach is not conditionally valid under heteroskedasticity. They also propose a locally weighted conformal prediction approach, where the regression residuals are weighted by the inverse of a measure of their variability. This approach can alleviate some of the limitations of mean-based conformal prediction but is motivated by and based on restrictive locations-scale models. By contrast, our approach is generic and exploits flexible and substantially more general models for the whole conditional distribution. 

Romano et al. (2019b) propose a split conformal approach based on QR models, which they call conformalized quantile regression (CQR). See also Sesia and Candes (2020); Kivaranovic et al. (2020a) for related approaches and Vovk et al. (2020) for a general approach to adaptive conformal prediction. Their approach is based on splitting the data into two subsets, _T_ 1 and _T_ 2. Based on _T_ 1, they estimate two separate quantile functions _Q_[ˆ] ( _α/_ 2 _, x_ ) and _Q_[ˆ] (1 _− α/_ 2 _, x_ ) and construct the prediction intervals as 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0007-03.png)


where _QE_ (1 _− α_ ) is the (1 _− α_ )(1 + 1 _/|T_ 2 _|_ )-th empirical quantile of 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0007-05.png)


in _T_ 2. Constructing prediction intervals based on deviations from quantile estimates is similar to working with deviations from mean estimates, as the deviations are measured in absolute levels. By contrast, exploiting the probability integral transform, our approach is generic and relies on permuting ranks, which naturally have the same scaling on (0 _,_ 1). Note, however, that our paper was inspired by Romano et al. (2019b) and we view our proposal as a (fully quantile-rank based) refinement of Romano et al. (2019b). 

Our adjustment for constructing efficient prediction intervals is related to and inspired by conformal prediction literature on minimum-volume prediction sets based on density estimators (e.g., Lei et al., 2013; Lei and Wasserman, 2014; Eck and Crawford, 2019; Izbicki 

7 

et al., 2019, 2020) and nearest-neighbor estimators Gyorfi and Walk (2020). It is most closely related and can be viewed as an alternative to conformal histogram regression (Sesia and Romano, 2021). The main differences between our approach and conformal histogram regression are the following. First, our method is based on an optimization problem formulated in terms of estimated quantile functions and does not require estimating a conditional density or histogram. Second, we do not work with nested sets but instead use a simple adjustment of our baseline conformity score. Finally, our approach works for general outcome distributions and does not rely on assuming unimodal distributions. 

Conceptually, our paper is further related to the transformation-based model-free prediction approach developed in Politis (2013) and Politis (2015) in that we rely on transformations of the original setup into one that is easier to work with (i.e., ranks which are uniformly distributed) and study the properties of our approach in a model-free setting. An important difference is the implementation of the resulting procedure. The transformationbased approach is based on the bootstrap, whereas our approach is based on permuting ranks. Permuting ranks estimated based on the augmented data guarantees the model-free finite sample validity of our method with exchangeable data. To our knowledge, no exact finite-sample validity results have been developed for the bootstrap-based approach. 

## **2 Distributional Conformal Prediction** 

Here we introduce DCP. We present a full and a split sample version of our method. 

## **2.1 Full Distributional Conformal Prediction** 

Let _y_ denote a test value for _YT_ +1. We test plausibility of each value _y ∈_ R, collect all plausible values, and report them as the prediction set. In practice, we consider a grid of test values _Y_ trial.[3] Define the augmented data _Z_[(] _[y]_[)] = _{Zt_[(] _[y]_[)] _[}][T] t_ =1[+1][,][where] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0008-06.png)


Based on the augmented dataset _Z_[(] _[y]_[)] , we estimate the conditional CDF using a suitable 

> 3For example, we can choose _Y_ trial to be a fine grid between _−_ max1 _≤t≤T |Yt|_ and max1 _≤t≤T |Yt|_ . This choice has a theoretical justification since, under exchangeability, _P_ ( _|YT_ +1 _| ≥_ max1 _≤t≤T |Yt|_ ) _≤_ 1 _/_ (1 + _T_ ) (Chen et al., 2016); see also the discussion in the `conformalInference R` -package ( `https://github.com/ ryantibs/conformal` ). 

8 

method such as QR and DR, which are discussed in more detail in the SI Appendix. Let _F_ ˆ[(] _[y]_[)] denote the estimator for _F_ based on the augmented sample. If the original estimate is not monotonic, we rearrange it (e.g., Chernozhukov et al., 2009, 2010) so that _F_[ˆ][(] _[y]_[)] ( _·, x_ ) is always monotonic. To simplify the exposition, we keep these rearrangements implicit. 

We compute the ranks _{U_[ˆ] _t_[(] _[y]_[)] _}[T] t_ =1[+1][,][where] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0009-02.png)


and obtain _p_ -values as 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0009-04.png)


where _V_[ˆ] _t_[(] _[y]_[)] := _ψ_ ( _U_[ˆ] _t_[(] _[y]_[)] ), and _ψ_ ( _·_ ) is a deterministic function. For our baseline method, we use _ψ_ ( _x_ ) = _|x −_ 1 _/_ 2 _|_ . In Section 4, we show how to choose _ψ_ optimally to ensure efficiency. Prediction intervals are computed as _C_[�] (1[full] _−α_ )[(] _[X][T]_[+1][) =] _[ {][y][∈Y]_[trial][:] _[p]_[ˆ][(] _[y]_[)] _[ > α][}]_[.][4][We summarize] our approach in Algorithm 1. 

**Algorithm 1** (Full DCP) **.** 

_**Input:** Data {_ ( _Yt, Xt_ ) _}[T] t_ =1 _[,][miscoverage level][ α][ ∈]_[(0] _[,]_[ 1)] _[,][a point][ X][T]_[+1] _[,][test values][ Y]_[trial] _**Process:** For y ∈Y_ trial _,_ 

_1. define the augmented data Z_[(] _[y]_[)] _as in_ (9) 

- ˆ 

- _2. compute p_ ( _y_ ) _as in_ (10) 

_**Output:** Return_ (1 _− α_ ) _prediction set C_[�] (1[full] _−α_ )[(] _[X][T]_[+1][) =] _[ {][y][∈Y]_[trial][:] _[p]_[ˆ][(] _[y]_[)] _[ > α][}]_ 

## **2.2 Split Distributional Conformal Prediction** 

An important drawback of full DCP (Algorithm 1) is its computational burden due to the grid search. Since _F_[ˆ][(] _[y]_[)] is obtained based on the augmented data, one has to choose _Y_ trial and re-estimate the entire conditional distribution for all _y ∈Y_ trial. Therefore, we propose a split conformal procedure that exploits sample splitting, avoids grid search, and only requires estimating _F_ once. Sample splitting is a popular approach for improving the computational performance of conformal prediction methods (e.g., Lei et al., 2018; Romano et al., 2019b). 

**Algorithm 2** (Split DCP) **.** 

> � � 

> 4Instead of _C_ (1[full] _−α_ )[(] _[X][T]_[ +1][)] we typically report the closed interval _C_ (1[full] _−α_ )[(] _[X][T]_[ +1][)] = � � �min � _C_ (1[full] _−α_ )[(] _[X][T]_[ +1][)] � _,_ max � _C_ (1[full] _−α_ )[(] _[X][T]_[ +1][)] ��. 

9 

_**Input:** Data {_ ( _Yt, Xt_ ) _}[T] t_ =1 _[,][miscoverage][level][α][ ∈]_[(0] _[,]_[ 1)] _[,][point][X][T]_[+1] _**Process:**_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0010-01.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0010-02.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0010-03.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0010-04.png)


In Algorithm 2, we split _{_ 1 _, . . . , T }_ into _{_ 1 _, . . . , T_ 0 _}_ and _{T_ 0 + 1 _, . . . , T }_ . With iid data, one can also consider random splits. 

Split DCP lends itself naturally to simple in-sample validity checks with both crosssectional and time series data as illustrated in Section 5. 

## **3 Theoretical Performance Guarantees** 

In this section, we establish the theoretical properties of our procedure. We focus on fullsample DCP (Algorithm 1). For the split-sample approach (Algorithm 2), we provide a modified version (Algorithm S1) in the SI Appendix and present its theoretical properties in Section 4. 

When the data are iid (or exchangeable), our method achieves finite-sample unconditional validity in a model-free manner, as a consequence of general results on conformal inference and permutation inference more generally (e.g., Vovk et al., 2005; Hoeffding, 1952). 

**Theorem 1** (Finite sample unconditional validity) **.** _Suppose that the data are iid or exchangeable and that the estimator of the conditional distribution is invariant to permutations of the data. Then_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0010-11.png)


The proof of Theorem 1 is standard and omitted. Theorem 1 highlights the strengths and drawbacks of conformal prediction methods. Most commonly-used estimators of the conditional CDF such as QR and DR are invariant to permutations of the data. As a result, Theorem 1 provides a model-free unconditional performance guarantee in finite samples, allowing for arbitrary misspecification of the model of the conditional CDF. On the other hand, it has a major theoretical drawback. Even with iid data, it provides no guarantee at all on conditional validity. 

10 

Our next theoretical results provide a remedy. We impose the following weak regularity conditions. 

**Assumption 1.** _Suppose that there exists a non-random function F[∗]_ ( _·, ·_ ) _such that the following conditions hold as T →∞. Define Vt_ := _ψ_ ( _F[∗]_ ( _Yt, Xt_ )) _for_ 1 _≤ t ≤ T_ + 1 _._ 

_1. There exists a strictly increasing continuous function φ_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ) _such that φ_ (0) = 0 _and_ ( _T_ + 1) _[−]_[1][ �] _[T] t_ =1[+1] _[φ]_[(] _[|][V]_[ˆ] _[t][−][V][t][|]_[)][=] _[o][P]_[(1)] _[and][V]_[ˆ] _[T]_[+1][=] _[V][T]_[+1][+] _[ o][P]_[(1)] _[,][where]_ ˆ ˆ _Vt_ := _Vt_[(] _[Y][T]_[ +1][)] = _ψ_ ( _F_[ˆ][(] _[Y][T]_[ +1][)] ( _Yt, Xt_ )) _for_ 1 _≤ t ≤ T_ + 1 _._ 

_2._ sup _v∈_ R _|G_[˜] ( _v_ ) _− G_ ( _v_ ) _|_ = _oP_ (1) _, where G_[˜] ( _v_ ) = ( _T_ +1) _[−]_[1][ �] _[T] t_ =1[+1] **[1]** _[{][V][t][< v][}][and][G]_[(] _[·]_[)] _[is][the] distribution function of VT_ +1 _._ 

_3._ sup _x_ 1= _x_ 2 _|G_ ( _x_ 1) _− G_ ( _x_ 2) _|/|x_ 1 _− x_ 2 _| is bounded._ 

Assumption 1 allows for some flexibility with respect to the model estimator. Here, we only require _F[∗]_ to be a non-random function, which may or may not be _F_ . The interpretation is straight-forward when _F[∗]_ = _F_ since this simply means that the estimator _F_[ˆ] is consistent for _F_ . We discuss the case of _F[∗]_ = _F_ after Theorem 2 below. Note that we can replace the consistency requirement in Assumption 1 with a stronger uniform consistency requirement, sup _x,y |F_[ˆ] ( _y, x_ ) _− F[∗]_ ( _y, x_ ) _|_ = _oP_ (1). 

We also notice that the quantities _V_[ˆ] _t_ and _Vt_ are defined under the true _YT_ +1. This means that _F_[ˆ][(] _[y]_[)] uses _y_ = _YT_ +1. In other words, the estimator _F_[ˆ] based on the sample _{_ ( _Xt, Yt_ ) _}[T] t_ =1[+1] would be consistent for some _F[∗]_ if _YT_ +1 were observed.[5] Since the goal of Assumption 1 is to guarantee the coverage probability for _YT_ +1, the conditions in Assumption 1 only need to hold for _y_ = _YT_ +1. 

Notice that _F_[ˆ] is consistent for _F[∗]_ under a very weak norm, and no rate condition is required. When _ψ_ ( _x_ ) = _|x −_ 1 _/_ 2 _|_ , a simple example of _φ_ ( _·_ ) in Assumption 1 is _φ_ ( _x_ ) = _x[q]_ for some _q >_ 0; in other words, a sufficient condition is ( _T_ +1) _[−]_[1][ �] _[T] t_ =1[+1] _[|][F]_[ ˆ][(] _[Y][t][, X][t]_[)] _[−][F][ ∗]_[(] _[Y][t][, X][t]_[)] _[|][q]_[=] _oP_ (1), which can be verified for many existing estimators with _q_ = 2. 

The following lemma gives the basic consistency result. 

**Lemma 1.** _Let Assumption 1 hold. Then G_[ˆ] ( _V_[ˆ] _T_ +1) = _G_ ( _VT_ +1) + _oP_ (1) _, where G_[ˆ] ( _v_ ) = ( _T_ + 1) _[−]_[1][ �] _[T] t_ =1[+1] **[1]** _[{][V]_[ˆ] _[t][< v][}][.]_ 

By Assumption 1, _G_ ( _·_ ) is uniformly continuous and thus continuous. Since _G_ ( _·_ ) is the distribution function of _VT_ +1, we have that _G_ ( _VT_ +1) has the uniform distribution on (0 _,_ 1), i.e., _P_ ( _G_ ( _VT_ +1) _≤ α_ ) = _α_ . This implies the unconditional asymptotic validity. 

> 5This is not really much different from assuming that _F_ ˆ based on the sample _{_ ( _Xt, Yt_ ) _}Tt_ =1[is][consistent] for some _F[∗]_ . 

11 

**Theorem 2** (Asymptotic unconditional validity) **.** _Let Assumption 1 hold. Then_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0012-01.png)


Theorem 2 establishes the asymptotic unconditional validity of the procedure. Since Theorem 1 already establishes the unconditional validity in finite-samples for iid or exchangeable data without assuming any consistency of _F_[ˆ] , the main purpose of Theorem 2 is to address the case of non-exchangeable data (e.g., time series data with ergodicity), especially when the model is misspecified (i.e., if _F[∗]_ = _F_ ). 

To illustrate model misspecification, consider the popular linear QR model, which as1 sumes _Q_ ( _τ, x_ ) = _x[⊤] β_ ( _τ_ ) and thus _F_ ( _y, x_ ) = _F_ ( _y, x_ ; _β_ ) = �0 **[1]** _[{][x][⊤][β]_[(] _[τ]_[)] _[≤][y][}][dτ]_[.] This _T_ +1 model is typically estimated by _β_[ˆ] ( _τ_ ) = arg min _β_ � _t_ =1 _[ρ][τ]_[(] _[Y][t][−][X] t[⊤][β]_[)][with] _[ρ][τ]_[(] _[a]_[)][=] _[a]_[(] _[τ][−]_ **1** _{a <_ 0 _}_ ). Under misspecification ( _Q_ ( _τ, x_ ) = _x[⊤] β_ ( _τ_ )), _β_[ˆ] ( _τ_ ) is still estimating _β[∗]_ ( _τ_ ) = _T_ +1 1 arg min _β_ � _t_ =1 _[Eρ][τ]_[(] _[Y][t][−][X] t[⊤][β]_[)][ and] _[ F][ ∗]_[is defined using] _[ β][∗]_[(] _[·]_[)][, e.g.,] _[ F][ ∗]_[(] _[y, x]_[) =] �0 **[1]** _[{][x][⊤][β][∗]_[(] _[τ]_[)] _[ ≤] y}dτ_ . For parametric models, _F[∗]_ is usually the probability limit of _F_[ˆ] . In general, we can _T_ +1 consider a model _F_ and minimize the empirical risk _F_[ˆ] = arg min _g∈F_ � _t_ =1 _[L]_[(] _[Y][t][, X][t][, g]_[)][for] some loss function _L_ . Even if the model is misspecified ( _F ∈F/_ ), it is still possible to show that _F_[ˆ] is close (in some norm) to _F[∗]_ = arg min _g∈F_ � _Tt_ =1+1 _[E]_[[] _[L]_[(] _[Y][t][, X][t][, g]_[)]][.][In the SI Appendix,] we provide a more detailed discussion of this and some theoretical results verifying the consistency requirement in Assumption 1 for the time series case; see also Chernozhukov et al. (2018) for a general discussion of conformal prediction in time series settings. 

The cost of allowing for misspecification is that one cannot guarantee conditional validity when _F[∗]_ = _F_ . On the other hand, Lemma 1 implies that the prediction intervals are conditionally valid when _F[∗]_ = _F_ . 

**Theorem 3** (Asymptotic conditional validity) **.** _Let Assumption 1 hold with F[∗]_ = _F . Then_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0012-06.png)


– Theorems 2 3 establish the asymptotic validity of our procedure under weak and easyto-verify conditions. They formalize the key intuition that conditional validity hinges on the quality of the estimator _F_[ˆ] of the conditional CDF.[6] 

> 6In Theorem 3, we assume _F ∗_ = _F_ . Since the first version of this paper was written, Candès et al. (2021) have provided more general results where _F[∗] ≈ F_ . 

12 

## **4 Extension: Optimal DCP** 

In Section 3, we have seen that a generic conformity score _ψ_ ( _y, x_ ) = _|F_ ( _y, x_ ) _−_ 1 _/_ 2 _|_ leads to conditional validity if the conditional distribution _F_ can be estimated consistently. We now characterize an optimal choice of conformity score that results in the shortest prediction interval. Detailed implementation algorithms, technical assumptions, and proofs are provided in the SI Appendix. 

Let _Z_ and _X_ denote the support of _Zt_ = ( _Yt, Xt_ ) and _Xt_ , respectively. The optimal prediction interval is 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0013-03.png)


where the functions _r_ 1( _·, ·_ ) _, r_ 2( _·, ·_ ) satisfy that for any _x ∈X_ , 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0013-05.png)


The question is whether it is possible to design a conformity score that achieves the above optimal prediction interval. To answer this question formally, we consider a generic conformity score _ψ_ ( _y, x_ ), which might contain components that need to be estimated. 

Permuting a large number of values of _ψ_ ( _Yt, Xt_ ) in conformal predictions amounts to taking the sample (1 _− α_ )-quantile of _ψ_ ( _Yt, Xt_ ); for example, following Algorithm 2, one would (1 _− α_ )(1 + 1 _/|T_ 2 _|_ ) empirical quantile of _ψ_ ( _Yt, Xt_ ). Assuming a law of large numbers, this empirical quantile would be close to the population (1 _− α_ )-quantile of _ψ_ ( _Yt, Xt_ ), leading to the asymptotic conformal prediction interval for _YT_ +1 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0013-08.png)


where _Qψ_ (1 _− α_ ) is the (1 _− α_ )-quantile of _ψ_ ( _Yt, Xt_ ). The following result shows how to construct the optimal conformity score _ψ_ . 

**Lemma 2.** _Let ψ∗_ ( _y, x_ ) = _|F_ ( _y, x_ ) _− b_ ( _x, α_ ) _−_ (1 _− α_ ) _/_ 2 _|, where b_ ( _·, ·_ ) _is a function satisfying that for any x ∈X ,_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0013-11.png)


_Let C_ (1[conf] _−α_ )[(] _[X][T]_[+1][)] _[be][defined][as][in]_[(][13][)] _[with][the][above][conformity][score][ψ][∗][.][Assume][that] F_ ( _·, x_ ) _is a continuous function for any x ∈X . Then Qψ_ (1 _− α_ ) = (1 _− α_ ) _/_ 2 _and_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0013-13.png)


13 

_where µ_ ( _·_ ) _denotes the Lebesgue measure. If the optimization problem in_ (11) _has a unique solution for any x ∈X , then_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0014-01.png)


Lemma 2 motivates conformity scores of the form _ψ∗_ ( _y, x_ ) = _|F_ ( _y, x_ ) _−_ [ _b_ ( _x, α_ ) + (1 _− α_ ) _/_ 2] _|_ , where _b_ ( _·, ·_ ) solves (14). Compared to the choice of _ψ_ ( _y, x_ ) = _|F_ ( _y, x_ ) _−_ 1 _/_ 2 _|_ mentioned in Section 3, we can view _ψ∗_ as having a “shape” adjustment _b_ ( _x, α_ ) _− α/_ 2. Since _F_ ( _Yt, Xt_ ) is independent of _Xt_ , the optimal conformity score measures the distance between two independent components: _F_ ( _Yt, Xt_ ) and 1 _/_ 2 + ( _b_ ( _Xt, α_ ) _− α/_ 2). Hence, by Lemma 2, in order to take into account the shape of the conditional distribution _F_ ( _·, x_ ), it suffices to consider the scalar quantity 1 _/_ 2 + ( _b_ ( _x, α_ ) _− α/_ 2). 

In some special cases, the “shape” adjustment can be shown to be zero, i.e., _b_ ( _x, α_ ) = _α/_ 2. One typical example is when _F_ ( _·, x_ ) is a symmetric uni-modal distribution with a well-defined conditional density.[7] Therefore, the choice of _ψ_ ( _y, x_ ) = _|F_ ( _y, x_ ) _−_ 1 _/_ 2 _|_ mentioned in Section 3 is optimal in these cases. However, Lemma 2 provides a construction that achieves optimality more generally. By the definition of _ψ∗_ and _Qψ_ (1 _− α_ ) = (1 _− α_ ) _/_ 2, the prediction interval is 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0014-04.png)


We illustrate this in Figure 2 with _α_ = 0 _._ 1. (15) implies that _b_ ( _x, α_ ) is the quantile-index of the lower bound of the interval. For the symmetric distribution in the left panel, we see _b_ ( _x, α_ ) = 0 _._ 05, which is _α/_ 2. For the asymmetric distribution in the right panel, we see that _b_ ( _x, α_ ) = 0 _._ 007, which is far away from _α/_ 2 = 0 _._ 05. 

> 7In this case, _Q_ (1 _/_ 2+ _δ, x_ ) _−Q_ (1 _/_ 2 _, x_ ) = _Q_ (1 _/_ 2 _, x_ ) _−Q_ (1 _/_ 2 _−δ, x_ ) and the conditional density is increasing on ( _−∞, Q_ (1 _/_ 2 _, x_ )) and decreasing on ( _Q_ (1 _/_ 2 _, x_ ) _, ∞_ ). One can show _b_ ( _x, α_ ) = _α/_ 2 by taking the first-order derivative for the optimization problem in (14) and setting it to zero. 

14 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0015-00.png)


**----- Start of picture text -----**<br>
N(0, 1) χ [2] (5)<br>QY(0.05) QY(0.95) QY(0.007) QY(0.907)<br>**----- End of picture text -----**<br>


Figure 2: Optimal prediction intervals 

The first result in Lemma 2 is general and allows for the lack of uniqueness of the optimal prediction interval. For example, if _F_ is the uniform distribution on a certain interval, then all conditionally valid prediction intervals have the same length. Clearly, in this case, achieving the optimal length is the only goal one can hope for. When we can uniquely define the optimal prediction interval, Lemma 2 implies that the conformal procedure can recover the uniquely defined optimal interval, not just achieving the optimal length. 

Lemma 2 also confirms the insight of Lei and Wasserman (2014): the optimal confidence set for _XT_ +1 = _x_ should take the form _{y_ : _f_ ( _y, x_ ) _≥ c_ ( _x_ ) _}_ for some _c_ ( _x_ ) _>_ 0, where _f_ ( _y, x_ ) = _∂F_ ( _y, x_ ) _/∂y_ . Assume that _F_ ( _·, x_ ) is a uni-modal distribution and _f_ ( _·, x_ ) is a continuous function for any _x ∈X_ . Then this confidence set is an interval. This means that _{y_ : _f_ ( _y, x_ ) _≥ c_ ( _x_ ) _}_ = [ _c_ 1( _x_ ) _, c_ 2( _x_ )] and _f_ ( _c_ 1( _x_ ) _, x_ ) = _f_ ( _c_ 2( _x_ ) _, x_ ) = _c_ ( _x_ ). We notice that _c_ 1( _x_ ) _, c_ 2( _x_ ) are related to our results in that _c_ 1( _x_ ) = _Q_ ( _b_ ( _x, α_ ) _, x_ ) and _c_ 2( _x_ ) = _Q_ ( _b_ ( _x, α_ )+1 _− α, x_ ). To see this, simply observe that the first-order condition of the optimization problem in (14) is 1 _/f_ ( _Q_ ( _z_ + 1 _− α, x_ ) _, x_ ) _−_ 1 _/f_ ( _Q_ ( _z, x_ )) = 0, which implies that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0015-04.png)


To make the procedure operational, we provide the conformal prediction interval _C_[�] (1[conf] _−α_ )[(] _[X][T]_[+1][)] defined in Algorithm S1 in the SI Appendix. We can provide the following guarantee. **Theorem 4.** _Let Assumption S1 in the SI Appendix hold. Then_ 

_and_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0015-07.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0015-08.png)


The main requirements in Assumption S1 in the SI Appendix are consistency of _F_[ˆ] and that the density _f_ bounded below on its support. This is quite mild in the sense that it does not imply that the optimal prediction interval in (11) is uniquely defined. For example, it allows _f_ to be a uniform distribution. Therefore, as discussed above, the conformal prediction interval would have approximately the shortest length but might not converge to _C_ (1[opt] _−α_ )[(] _[X][T]_[+1][)][in][(][11][).] 

The following theorem provides a stronger result about _C_[�] (1[conf] _−α_ )[(] _[X][T]_[+1][)][based][on][stronger] assumptions. 

**Theorem 5.** _Let Assumption S2 in the SI Appendix hold. Consider the conformal prediction interval C_[�] (1[conf] _−α_ )[(] _[X][T]_[+1][)] _[defined][in][Algorithm][S1][in][the][SI][Appendix.][Then]_ 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0016-03.png)


_where △ denotes the symmetric difference of sets (i.e., A△B_ = ( _A\B_ )[�] ( _B\A_ ) _), C_ (1[opt] _−α_ )[(] _[X][T]_[+1][)] _is defined in_ (11) _._ 

The key component of Assumption S2 in the SI Appendix is consistent estimation of _b_ . Theorem 5 shows that _C_[�] (1[conf] _−α_ )[(] _[X][T]_[+1][)][ is close to] _[ C]_ (1[opt] _−α_ )[(] _[X][T]_[+1][)][ in the sense that the symmetric] difference between these two sets has vanishing Lebesgue measure. 

## **5 Empirical Applications** 

We illustrate the performance of DCP in two empirical applications and provide a comparison to alternative approaches. We consider eight different conformal prediction methods. 

1. **DCP-QR:** DCP with QR (Algorithm 2) 

2. **DCP-QR** _[∗]_ **:** Optimal DCP with QR (Algorithm S1 in SI Appendix) 

3. **DCP-DR:** DCP with DR (Algorithm 2) 

4. **CQR:** CQR with QR (Romano et al., 2019b) 

5. **CQR-m:** CQR variant (Sesia and Candes, 2020; Kivaranovic et al., 2020a) with QR 

6. **CQR-r:** CQR variant (Sesia and Candes, 2020) with QR. 

7. **CP-OLS:** Mean-based split conformal prediction with OLS 

8. **CP-loc:** Locally-weighted conformal prediction (Lei et al., 2018) with OLS 

16 

All computations were carried out in `R` (R Core Team, 2021). Code and data for replicating the empirical results are deposited on Github ( `https://github.com/kwuthrich/ Replication_DCP` ). 

## **5.1 Predicting Stock Market Returns** 

Here we consider the problem of predicting stock market returns, which are known to exhibit substantial heteroskedasticity; see Chapter 13 in Elliott and Timmermann (2016) for a recent review and the references therein. We use data on daily returns of the market portfolio (CRSP value-weighted portfolio) from July 1, 1926, to June 30, 2021.[8] We use lagged realized volatility _Xt_ to predict the present return _Yt_ .[9] Daily returns are not iid and exhibit time series dependence. In the SI Appendix, we show that the key conditions underlying our theoretical results hold when the data are _β_ -mixing. Several stochastic volatility models for asset returns, including the popular GARCH models, can be shown to be _β_ -mixing (e.g., Boussama, 1998; Carrasco and Chen, 2002; Francq and Zakoïan, 2006). 

We evaluate the performance of the different methods by splitting the data into a holdout and a test sample. To account for the dependence in the data, we present results averaged over five consecutive prediction exercises. In the first exercise, we apply split conformal prediction with an equal split ( _|T_ 1 _|_ = _|T_ 2 _|_ ) to the first 50% of observations and use the next 10% for testing. In the second exercise, we drop the first 10% of the observations, apply split conformal prediction to the next 50% of observations, and use the next 10% for testing and so on. 

Figure 3 plots the empirical coverage probabilities for 20 bins obtained by dividing up the support of _Xt_ based on equally spaced quantiles. DCP-QR and DCP-QR _[∗]_ yield prediction intervals with coverage levels that are almost constant across all bins and close to the nominal level. They outperform DCP-DR, which undercovers in high-volatility regimes. The conditional coverage properties of DCP-QR and DCP-QR _[∗]_ are very similar to CQR, CQR-m, CQR-r, and CP-loc. This suggest that location-scale models, which are nested by QR, provide a good approximation of the conditional distribution. CP-OLS exhibits overcoverage under low-volatility regimes and substantial undercoverage under high-volatility regimes. This finding has important practical implications since the volatility tends to be high during periods of crisis, which is precisely when accurate risk assessments are most needed. 

> 8The CRSP data are constructed from the Fama/French 3 Factors data (Kenneth R. French, 2021) available from Kenneth R. French’s data library (accessed August 17, 2021). 

> 9We compute realized volatility as the square root of the sum of squared returns over the last 22 days. 

17 

**Conditional coverage 90% prediction intervals** 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0018-01.png)


**----- Start of picture text -----**<br>
DCP−QR<br>DCP−QR*<br>DCP−DR<br>CQR<br>CQR−m<br>CQR−r<br>CP−OLS<br>CP−loc<br>5 10 15 20<br>Bin<br>1.0<br>0.9<br>0.8<br>0.7<br>0.6<br>Conditional coverage<br>0.5<br>0.4<br>**----- End of picture text -----**<br>


Figure 3: Conditional coverage 90% prediction intervals by realized volatility 

Figure 4 shows the conditional length of the prediction intervals. DCP-QR, DCP-QR _[∗]_ , CQR, CQR-m, CQR-r, and CP-loc yield prediction intervals of similar length. The DCP-DR prediction intervals are somewhat shorter than those of the QR-based methods at the upper tail. Finally, CP-OLS yields prediction intervals that are almost constant across all values of realized volatility; they are longer at the lower tail and shorter at the upper tail.[10] 

## **Conditional length 90% prediction intervals** 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0018-05.png)


**----- Start of picture text -----**<br>
DCP−QR<br>DCP−QR*<br>DCP−DR<br>CQR<br>CQR−m<br>CQR−r<br>CP−OLS<br>CP−loc<br>5 10 15 20<br>Bin<br>10<br>8<br>6<br>4<br>Conditional length<br>2<br>0<br>**----- End of picture text -----**<br>


Figure 4: Conditional coverage 90% prediction intervals by realized volatility 

10The CP-OLS prediction intervals are not exactly constant because we are reporting results averaged over five experiments. 

18 

## **5.2 Predicting Wages Using CPS Data** 

We consider the problem of predicting wages using individual characteristics. We use the 2012 CPS data provided in the `R` -package `hdm` (Chernozhukov et al., 2016), which contains information on _N_ = 29217 observations. Here we use the index _i_ instead of _t_ . To illustrate the impact of skewness on the performance of the different prediction methods, we use the hourly wage as our dependent variable _Yi_ .[11] Predictors _Xi_ include indicators for gender, marital status, educational attainment, region, experience, experience squared, and all twoway interactions such that dim( _Xi_ ) = 100 after removing constant variables. 

Following Romano et al. (2019b) and Sesia and Candes (2020), we evaluate the performance of the different methods by randomly holding out 20% of the data for testing, _I_ test, and applying split conformal prediction with an equal split to the remaining 80% of the data. We repeat the whole experiment 20 times. 

Panel (a) of Table 1 shows that all conformal prediction methods exhibit excellent unconditional coverage properties, confirming the theoretical finite sample guarantees. To assess and compare the conditional coverage properties, for each method, we compute conditional coverage probabilities as the predictions from logistic regressions of _{Yi ∈ C_[�] (1[split] _−α_ )[(] _[X][i]_[)] _[}][i][∈I]_[test] on _{Xi}i∈I_ test, where _C_[�] (1[split] _−α_ )[is][the][split][conformal][prediction][interval][obtained][by][the][cor-] responding method. The less dispersed the predicted coverage probabilities are around the nominal level 1 _− α_ = 0 _._ 9, the better the overall conditional coverage properties of a method. Panel (b) of Table 1 plots the standard deviation of the predicted coverage probabilities.[12] DCP-QR _[∗]_ yields the lowest dispersion of all methods. The predicted coverage probabilities based on DCP-QR are less dispersed than those obtained from CQR, CQR-m, CQR-r. CPloc yields a higher dispersion than the methods based on QR and DR, which demonstrates the value-added of using flexible models of the conditional distribution. Overall, DCP performs much better than CP-OLS for which the predicted coverage probabilities exhibit a very high dispersion. Figure 5 in the SI Appendix plots histograms of the predicted coverage probabilities. 

Table 2 shows the average length of the prediction intervals. DCP-QR _[∗]_ produces the shortest prediction intervals among of all methods. This demonstrates the practical advantage of the shape adjustment when the conditional distribution is skewed. The results also suggest a trade-off between conditional coverage accuracy and average length. For example, 

> 11We obtain the hourly wage by exponentiating the log hourly wage provided in the dataset. 12Using �1 _/|I_ test _|_[�] _i∈I_ test[(] `Coverage` � _i −_ 0 _._ 9)[2] , where `Coverage` � _i_ is the predicted coverage probability, instead of the standard deviation yields very similar results. 

19 

CP-OLS and CP-loc, which both exhibit poor conditional coverage properties, yield shorter prediction intervals than DCP-QR. 

Table 1: Coverage 90% prediction intervals 

|DCP-QR DCP-QR_∗_DCP-DR CQR CQR-m CQR-r CP-OLS CP-loc|DCP-QR DCP-QR_∗_DCP-DR CQR CQR-m CQR-r CP-OLS CP-loc|
|---|---|
||(a) Unconditional coverage<br>0.90<br>0.90<br>0.90<br>0.90<br>0.90<br>0.90<br>0.90<br>0.90|
||(b) Dispersion of predicted conditional coverage (_×_100)<br>1.80<br>1.71<br>3.08<br>2.21<br>2.36<br>2.30<br>11.13<br>4.11|
||Table 2: Average length 90% prediction intervals|
|DCP-QR DCP-QR_∗_DCP-DR CQR CQR-m CQR-r CP-OLS CP-loc||
|34.22<br>29.61<br>33.69<br>34.52<br>34.84<br>34.63<br>33.84<br>32.66||



## **References** 

- Angrist, J., Chernozhukov, V., and Fernández-Val, I. (2006). Quantile regression under misspecification, with an application to the us wage structure. _Econometrica_ , 74(2):539– 563. 

- Belloni, A. and Chernozhukov, V. (2011). L1-penalized quantile regression in highdimensional sparse models. _The Annals of Statistics_ , 39(1):82–130. 

- Boussama, F. (1998). Ergodicité, mélange et estimation dans les modeles garch. PhD Thesis, Paris 7. 

- Bradley, R. C. (2005). Basic properties of strong mixing conditions. a survey and some open questions. _Probability surveys_ , 2:107–144. 

- Bradley, R. C. (2007). _Introduction to strong mixing conditions_ , volume 1. Kendrick Press Heber City. 

- Candès, E. J., Lei, L., and Ren, Z. (2021). Conformalized survival analysis. arXiv preprint arXiv:2103.09763. 

20 

- Carrasco, M. and Chen, X. (2002). Mixing and moment properties of various garch and stochastic volatility models. _Econometric Theory_ , 18(1):17–39. 

- Cattaneo, M. D., Feng, Y., and Titiunik, R. (2019). Prediction intervals for synthetic control methods. arXiv:1912.07120. 

- Chaudhuri, P. (1991). Global nonparametric estimation of conditional quantile functions – 

- and their derivatives. _Journal of Multivariate Analysis_ , 39(2):246 269. 

- Chaudhuri, P. and Loh, W.-Y. (2002). Nonparametric estimation of conditional quantiles using quantile regression trees. _Bernoulli_ , 8(5):561–576. 

- Chen, W., Wang, Z., Ha, W., and Barber, R. F. (2016). Trimmed conformal prediction for high-dimensional models. arXiv preprint arXiv:1611.09933. 

- Chernozhukov, V., Fernandez-Val, I., and Galichon, A. (2009). Improving point and interval estimators of monotone functions by rearrangement. _Biometrika_ , 96(3):559–575. 

- Chernozhukov, V., Fernández-Val, I., and Galichon, A. (2010). Quantile and probability curves without crossing. _Econometrica_ , 78(3):1093–1125. 

- Chernozhukov, V., Fernandez-Val, I., and Melly, B. (2013). Inference on counterfactual distributions. _Econometrica_ , 81(6):2205–2268. 

- Chernozhukov, V., FernÃ¡ndez-Val, I., Melly, B., and Wüthrich, K. (2020). Generic inference on quantile and quantile effect functions for discrete outcomes. _Journal of the American Statistical Association_ , 115(529):123–137. 

- Chernozhukov, V., Hansen, C., and Spindler, M. (2016). hdm: High-dimensional metrics. _R Journal_ , 8(2):185–199. 

- Chernozhukov, V., Wüthrich, K., and Yinchu, Z. (2018). Exact and robust conformal inference methods for predictive machine learning with dependent data. In Bubeck, S., Perchet, V., and Rigollet, P., editors, _Proceedings of the 31st Conference On Learning Theory_ , volume 75 of _Proceedings of Machine Learning Research_ , pages 732–749. PMLR. 

- Chernozhukov, V., Wüthrich, K., and Zhu, Y. (2021). An exact and robust conformal inference method for counterfactual and synthetic controls. _Journal of the American Statistical Association_ , 0(0):1–16. 

- Dedecker, J., Doukhan, P., Lang, G., Rafael, L. R. J., Louhichi, S., and Prieur, C. (2007). _Weak dependence_ . Springer. 

21 

- Dedecker, J. and Louhichi, S. (2002). Maximal inequalities and empirical central limit theorems. In _Empirical process techniques for dependent data_ , pages 137–159. Springer. 

- Eck, D. J. and Crawford, F. W. (2019). Efficient and minimal length parametric conformal prediction regions. arXiv preprint arXiv:1905.03657. 

- Elliott, G. and Timmermann, A. (2016). _Economic Forecasting_ . Princeton University Press. 

- Foresi, S. and Peracchi, F. (1995). The conditional distribution of excess returns: An empirical analysis. _Journal of the American Statistical Association_ , 90(430):451–466. 

- Foygel Barber, R., CandÃšs, E. J., Ramdas, A., and Tibshirani, R. J. (2021). The limits of distribution-free conditional predictive inference. _Information and Inference: A Journal of the IMA_ , 10(2):455–482. 

- Francq, C. and Zakoïan, J.-M. (2006). Mixing properties of a general class of GARCH (1,1) models without moment assumptions on the observed process. _Econometric Theory_ , 22(5):815–834. 

- Gyorfi, L. and Walk, H. (2020). Nearest neighbor based conformal prediction. Stuttgarter Mathematische Berichte 2020-002. 

- He, X., Ng, P., and Portnoy, S. (1998). Bivariate quantile smoothing splines. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 60(3):537–550. 

- Hoeffding, W. (1952). The Large-Sample Power of Tests Based on Permutations of Obser– 

- vations. _The Annals of Mathematical Statistics_ , 23(2):169 192. 

- Izbicki, R., Shimizu, G., and Stern, R. B. (2020). Cd-split and hpd-split: efficient conformal regions in high dimensions. arXiv preprint arXiv:2007.12778. 

- Izbicki, R., Shimizu, G. T., and Stern, R. B. (2019). Flexible distribution-free conditional predictive bands using density estimators. arXiv preprint arXiv:1910.05575. 

- Kenneth R. French (2021). Kenneth French Data Library. Fama/French 3 Factors [Daily] data. URL: `http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ data_library.html` . Accessed August 17, 2021. 

- Kivaranovic, D., Johnson, K. D., and Leeb, H. (2020a). Adaptive, distribution-free prediction intervals for deep networks. In Chiappa, S. and Calandra, R., editors, _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , volume 108 of _Proceedings of Machine Learning Research_ , pages 4346–4356. PMLR. 

22 

- Kivaranovic, D., Ristl, R., Posch, M., and Leeb, H. L. (2020b). Conformal prediction intervals for the individual treatment effect. arXiv:2006.01474. 

- Koenker, R. (2004). Quantile regression for longitudinal data. _Journal of Multivariate Analysis_ , 91(1):74 – 89. Special Issue on Semiparametric and Nonparametric Mixed Models. 

- Koenker, R. (2005a). _Quantile Regression_ . Econometric Society Monographs. Cambridge University Press. 

- Koenker, R. (2005b). _Quantile regression_ . Number 38. Cambridge university press. 

- Koenker, R. and Bassett, G. (1978). Regression quantiles. _Econometrica_ , 46:33–50. 

- Koenker, R. and Bassett, G. (1982). Robust tests for heteroscedasticity based on regression quantiles. _Econometrica_ , 50(1):43–61. 

- Koenker, R., Ng, P., and Portnoy, S. (1994). Quantile smoothing splines. _Biometrika_ , 81(4):673–680. 

- Komunjer, I. (2013). Chapter 17 - quantile prediction. In Elliott, G. and Timmermann, A., editors, _Handbook of Economic Forecasting_ , volume 2 of _Handbook of Economic Forecast-_ – 

- _ing_ , pages 961 994. Elsevier. 

- Lei, J., GSell, M., Rinaldo, A., Tibshirani, R. J., and Wasserman, L. (2018). Distributionfree predictive inference for regression. _Journal of the American Statistical Association_ , 113(523):1094–1111. 

- Lei, J., Robins, J., and Wasserman, L. (2013). Distribution-free prediction sets. _Journal of the American Statistical Association_ , 108(501):278–287. 

- Lei, J. and Wasserman, L. (2014). Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 76(1):71–96. 

- Lei, L. and Candès, E. J. (2020). Conformal inference of counterfactuals and individual treatment effects. arXiv:2006.06138. 

- Li, Y. and Zhu, J. (2008). L1-norm quantile regression. _Journal of Computational and Graphical Statistics_ , 17(1):163–185. 

- Meinshausen, N. (2006). Quantile regression forests. _Journal of Machine Learning Research_ , 7:983–999. 

23 

- Meyn, S. P. and Tweedie, R. L. (2012). _Markov chains and stochastic stability_ . Springer Science & Business Media. 

- Politis, D. N. (2013). Model-free model-fitting and predictive distributions. _TEST_ , 22(2):183– 221. 

- Politis, D. N. (2015). _Model-free prediction and regression: a transformation-based approach to inference_ . Springer, New York. 

- R Core Team (2021). _R: A Language and Environment for Statistical Computing_ . R Foundation for Statistical Computing, Vienna, Austria. 

- Rio, E. (2017). _Asymptotic Theory of Weakly Dependent Random Processes_ . Springer. 

- Romano, Y., Barber, R. F., Sabatti, C., and Candes, E. J. (2019a). With malice towards none: Assessing uncertainty via equalized coverage. arXiv:1908.05428. 

- Romano, Y., Patterson, E., and Candes, E. J. (2019b). Conformalized quantile regression. NeurIPS. 

- Sesia, M. and Candes, E. J. (2020). A comparison of some conformal quantile regression methods. _Stat_ , 9(1):e261. e261 sta4.261. 

- Sesia, M. and Romano, Y. (2021). Conformal histogram regression. arXiv preprint arXiv:2105.08747. 

- Taylor, J. W. (2000). A quantile regression neural network approach to estimating the conditional density of multiperiod returns. _Journal of Forecasting_ , 19(4):299–311. 

- van der Vaart, A. and Wellner, J. (1996). _Weak Convergence and Empirical Processes: With Applications to Statistics_ . Springer Science & Business Media. 

- Vershynin, R. (2018). _High-dimensional probability: An introduction with applications in data science_ , volume 47. Cambridge university press. 

- Vovk, V. (2012). Conditional validity of inductive conformal predictors. In Hoi, S. C. H. and Buntine, W., editors, _Proceedings of the Asian Conference on Machine Learning_ , volume 25 of _Proceedings of Machine Learning Research_ , pages 475–490, Singapore Management University, Singapore. PMLR. 

- Vovk, V., Gammerman, A., and Shafer, G. (2005). _Algorithmic Learning in a Random World_ . Springer. 

24 

- Vovk, V., Nouretdinov, I., and Gammerman, A. (2009). On-line predictive linear regression. _The Annals of Statistics_ , 37(3):1566–1590. 

- Vovk, V., Petej, I., Toccaceli, P., Gammerman, A., Ahlberg, E., and Carlsson, L. (2020). Conformal calibrators. In Gammerman, A., Vovk, V., Luo, Z., Smirnov, E., and Cherubin, G., editors, _Proceedings of the Ninth Symposium on Conformal and Probabilistic Prediction and Applications_ , volume 128 of _Proceedings of Machine Learning Research_ , pages 84–99. PMLR. 

- Wu, Y. and Liu, Y. (2009). Variable selection in quantile regression. _Statistica Sinica_ , 19(2):801–817. 

25 

## SI Appendix 

## **A Details for Section 4** 

Here we describe in detail how to implement the optimal prediction intervals described in Section 4. 

## **A.1 Implementation** 

We now consider the estimation of _b_ ( _·, ·_ ). We assume that _F_[ˆ] ( _y, x_ ) is monotonic in _y_ ; if not, we first rearrange it. We define _Q_[ˆ] ( _·, ·_ ) by 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0026-05.png)


and 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0026-08.png)


Let[ˆ] _b_ ( _x, α_ ) be a function such that[ˆ] _b_ ( _x, α_ ) _∈_ [0 _, α_ ] and 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0026-10.png)


We propose the following algorithm. 

**Algorithm S1** (Optimal split DCP) **.** 

**Input:** Data _{_ ( _Yt, Xt_ ) _}[T] t_ =1[,][miscoverage][level] _[α][ ∈]_[(0] _[,]_[ 1)][,][and][point] _[X][T]_[+1] **Process:** 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0026-14.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0026-15.png)


**Output:** Return the prediction set 

(Since _F_[ˆ] ( _·, XT_ +1) is monotonic, _C_[�] (1[conf] _−α_ )[(] _[X][T]_[+1][)][is][an][interval.)] 

26 

## **A.2 Regularity conditions** 

We now provide the regularity condition for Theorem 4. For simplicity we focus on the case of iid data. Recall that a legitimate cumulative distribution function _F_ ( _·_ ) on R is a non-decreasing right-continuous function such that lim _z→−∞ F_ ( _z_ ) = 0 and lim _z→∞ F_ ( _z_ ) = 1. **Assumption S1.** Suppose that the following hold: 

1. The data _{_ ( _Yt, Xt_ ) _}t∈T_ 2 is iid and _|T_ 2 _| →∞_ . 

2. For any _x ∈X_ , _F_[ˆ] ( _·, x_ ) is a legitimate cumulative distribution function on R with probability one. 

3. sup _x∈X_ sup _y∈Y_ ( _x_ ) _|F_[ˆ] ( _y, x_ ) _− F_ ( _y, x_ ) _|_ = _oP_ (1) as _|T_ 1 _| →∞_ , where _Y_ ( _x_ ) is the support of conditional distribution _Yt | Xt_ = _x_ . 

4. There exist constants _C_ 1 _, C_ 2 _>_ 0 such that min _y∈Y_ ( _x_ ) _f_ ( _y, x_ ) _≥ C_ 1 and sup _y∈Y_ ( _x_ ) _|y| ≤ C_ 2 for any _x ∈X_ . 

The following assumption is used to prove the results in Theorem 5. 

**Assumption S2.** Suppose that the following hold. 

1. _|T_ 2 _|[−]_[1][ �] _t∈T_ 2[( ˆ] _[F]_[(] _[Y][t][, X][t]_[)] _[ −][U][t]_[)][2][=] _[o][P]_[(1)][and] _[|T]_[2] _[|][−]_[1][ �] _t∈T_ 2[(ˆ] _[b]_[(] _[X][t][, α]_[)] _[ −][b]_[(] _[X][t][, α]_[))][2][=] _[o][P]_[(1)][,] where _b_ ( _·, ·_ ) is the unique function satisfying the requirement in Lemma 2. 

2. sup _v∈_ R _|G_[˜] _∗_ ( _v_ ) _− G∗_ ( _v_ ) _|_ = _oP_ (1), where _G_[˜] _∗_ ( _v_ ) = _|T_ 2 _|[−]_[1][ �] _t∈T_ 2 **[1]** _[{][V]_[ˆ] _t[∗][≤][v][}]_[and] _[G][∗]_[(] _[·]_[)][is] the distribution function of _Vt[∗]_[=] _[ U][t][−][b]_[(] _[X][t][, α]_[)] _[ −]_ 2[1][(1] _[ −][α]_[)][.] 

3. There exists a constant _C_ 1 _>_ 0 such that for any _x ∈X_ , inf _y∈s_ ( _x_ ) _f_ ( _y, x_ ) _≥ C_ 1, where _s_ ( _x_ ) = [ _s_ 1( _x_ ) _, s_ 2( _x_ )] is the support of the distribution _Y | X_ = _x_ . ˆ 

4. sup _y∈_ R _F_ ( _y, XT_ +1) _− F_ ( _y, XT_ +1) = _oP_ (1) and ˆ _b_ ( _XT_ +1 _, α_ ) = _b_ ( _XT_ +1 _, α_ ) + _oP_ (1). ��� ��� 

5. There exists a constant _C_ 2 _>_ 0 such that for any _x ∈X_ , max _{|s_ 1( _x_ ) _|, |s_ 2( _x_ ) _|} ≤ C_ 2. 

The key requirement in Assumption S2 is the consistency of[ˆ] _b_ . Since[ˆ] _b_ is a solution to the optimization problem in (16), we can establish its consistency using the same argument for the consistency of an M-estimator. Under Assumption S1, we only need to impose the convexity of the mapping _z �→ Q_ ( _z_ + 1 _− α, x_ ) _− Q_ ( _z_ ). A simple sufficient condition is that there exists constants _κ_ 1 _, κ_ 2 _>_ 0 such that for any _x ∈X_ and for any _z_ with _|b_ ( _x, α_ ) _−z| ≤ κ_ 1, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0027-13.png)


27 

For uni-modal distributions, the above condition can be verified once we assume that the density _f_ ( _·, x_ ) is not too flat around _Q_ ( _b_ ( _x, α_ ) _, x_ ) and _Q_ ( _b_ ( _x, α_ ) + 1 _− α, x_ ). A similar condition is imposed as Assumption 2 in Lei and Wasserman (2014). 

## **B Regression models for conditional distributions** 

An important advantage of the proposed approach is that it allows researchers to leverage powerful regression methods for estimating conditional CDFs. This section discusses semiparametric (and potentially penalized) QR and DR models, which are very popular in applied research. We emphasize that our method is generic and also works in conjunction with nonparametric estimators (e.g., Chaudhuri, 1991; Koenker et al., 1994; He et al., 1998) as well as high-dimensional methods based on trees and random forests (e.g., Chaudhuri and Loh, 2002; Meinshausen, 2006) and neural networks (e.g., Taylor, 2000). 

## **B.1 Quantile regression methods** 

QR methods impose a model for the conditional quantiles _Q_ ( _τ, x_ ). The implied model for the conditional CDF is (Chernozhukov et al., 2013) 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0028-05.png)


A leading example is where _Q_ ( _τ, x_ ) is assumed to be linear: 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0028-07.png)


If _Xt_ is low dimensional, the parameter of interest _β_ ( _τ_ ) can be estimated using linear QR (Koenker and Bassett, 1978) as the solution to a convex program 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0028-09.png)


where _ρτ_ ( _u_ ) := _u_ ( _τ −_ **1** _{u <_ 0 _}_ ) is the check function. In problems where _Xt_ is highdimensional, it may be convenient to consider a penalized version of program (19): 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0028-11.png)


where _P_ ( _β_ ) is a penalty function. Examples of _P_ ( _β_ ) include _ℓ_ 1-penalties (e.g., Koenker, 2004; Li and Zhu, 2008; Belloni and Chernozhukov, 2011) and SCAD (e.g., Wu and Liu, 

28 

2009). The conditional distribution can be estimated as 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0029-01.png)


## **B.2 Distribution regression methods** 

Instead of modeling the conditional quantile function, one can directly model the conditional CDF using DR (e.g., Foresi and Peracchi, 1995; Chernozhukov et al., 2013, 2020). DR methods impose a generalized linear model for the CDF: 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0029-04.png)


where _β_ ( _y_ ) is the parameter of interest and Λ( _·_ ) is a known link function, for example, the Probit or Logit link. 

If _Xt_ is low dimensional, the parameters _β_ ( _y_ ) can be estimated as 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0029-07.png)


When Λ( _·_ ) is the Probit (Logit) link, this is simply a Probit (Logit) regression of 1 _{Yt ≤ y}_ on _Xt_ . In high dimensional settings, one can use a penalized version of program (21) (e.g., with an _ℓ_ 1-penalty or an elastic net penalty). The conditional distribution can be estimated as _F_[ˆ] ( _y, x_ ) = Λ _x[⊤] β_[ˆ] ( _y_ ) . � � 

## **C Proofs** 

## **C.1 Proof of Lemma 1** 

The argument is similar to Theorem 2 in Chernozhukov et al. (2018). Let _δ >_ 0 be a constant to be chosen later. Define quantities _RT_ = sup _v∈_ R _|G_[˜] ( _v_ ) _− G_ ( _v_ ) _|_ and _W_ = sup _x_ 1= _x_ 2 _|G_ ( _x_ 1) _− G_ ( _x_ 2) _|/|x_ 1 _− x_ 2 _|_ . 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0029-12.png)


29 

where (i) follows by the fact that the difference of two indicators takes value in _{−_ 1 _,_ 0 _,_ 1 _}_ . We notice that for _t ∈ A[c]_ , _Vt − δ < V_[ˆ] _t < Vt_ + _δ_ . Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0030-01.png)


Since[�] _t∈A[c]_ **[ 1]** _[{][V][t][≤][x][}]_[is][also][between][�] _t∈A[c]_ **[ 1]** _[{][V][t][≤][x][ −][δ][}]_[and][�] _t∈A[c]_ **[ 1]** _[{][V][t][≤][x]_[ +] _[ δ][}]_[,][it] follows that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0030-03.png)


where (i) follows by the fact that the difference of two indicators takes value in _{−_ 1 _,_ 0 _,_ 1 _}_ . Combining the above display with (22), we obtain that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0030-05.png)


Since the right-hand side does not depend on _x_ , we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0030-07.png)


To bound _|A|_ , we notice that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0030-09.png)


Hence, the above two displays imply that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0030-11.png)


30 

Now we fix an arbitrary _η ∈_ (0 _,_ 1). Choose _δ_ = _η/_ (6 _W_ ). Since 1 _/φ_ ( _δ_ ) is a constant and _RT_ = _oP_ (1) by assumption, (23) implies that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0031-01.png)


Since _η >_ 0 is arbitrary, we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0031-03.png)


Thus, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0031-05.png)


where (i) follows by _|G_ ( _V_[ˆ] _T_ +1) _− G_ ( _VT_ +1) _| ≤ W |V_[ˆ] _T_ +1 _− VT_ +1 _|_ . The proof is complete. 

## **C.2 Proof of Theorem 2** 

Notice that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0031-09.png)


By Lemma 1, _G_[ˆ] ( _V_[ˆ] _T_ +1) = _G_ ( _VT_ +1)+ _oP_ (1). Since _G_ ( _·_ ) is continuous, _G_ ( _VT_ +1) has the uniform distribution on (0,1). The desired result follows. 

## **C.3 Proof of Theorem 3** 

Notice that _Ut_ = _F_ ( _Yt, Xt_ ) is independent of _Xt_ . Since _VT_ +1 = _ψ_ ( _UT_ +1), _VT_ +1 is also independent of _XT_ +1. This means that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0031-13.png)


Since _G_ ( _·_ ) is the distribution function of _VT_ +1 and is a continuous function, we have that _P_ ( _G_ ( _VT_ +1) _≤ α_ ) = _α_ . The desired result follows by Lemma 1 and 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0031-15.png)


31 

## **C.4 Proof of Lemma 2** 

We proceed in three steps. 

**Step 1:** show _Qψ_ (1 _− α_ ) = (1 _− α_ ) _/_ 2. 

By the same argument as in Lemma S1 (proved later), 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-04.png)


Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-06.png)


In other words, _Qψ_ (1 _− α_ ) = (1 _− α_ ) _/_ 2. 

**Step 2:** show _µ_ � _C_ (1[opt] _−α_ )[(] _[X][T]_[+1][)] � = _µ_ � _C_ (1[conf] _−α_ )[(] _[X][T]_[+1][)] �. By the definition of _C_ (1[opt] _−α_ )[(] _[X][T]_[+1][)][,] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-09.png)


Since _F_ ( _·, XT_ +1) is a continuous function, we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-11.png)


We can see this by contradiction. Let ( _z_ 1 _[∗][, z]_ 2 _[∗]_[)][be][the][solution][to][the][optimization][in] (24). Suppose that _F_ ( _z_ 2 _[∗][, X][T]_[+1][)] _[ −][F]_[(] _[z]_ 1 _[∗][, X][T]_[+1][)] _[>]_[1] _[ −][α]_[.][Notice][that][the][mapping] _[g]_[(] _[z]_[)][=] _F_ ( _z, XT_ +1) _− F_ ( _z_ 1 _[∗][, X][T]_[+1][)][ is continuous in] _[ z]_[.][Since] _[ g]_[(] _[z]_ 2 _[∗]_[)] _[ >]_[ 1] _[ −][α]_[ and] _[ g]_[(] _[z]_ 1 _[∗]_[) = 0] _[ <]_[ 1] _[ −][α]_[.][By] the intermediate value theorem, there exists _z_ 2 _[∗∗][∈]_[(] _[z]_ 1 _[∗][, z]_ 2 _[∗]_[)][such][that] _[g]_[(] _[z]_ 2 _[∗∗]_[)][=][1] _[ −][α]_[.][Thus,] _F_ ( _z_ 2 _[∗∗][, X][T]_[+1][)] _[−][F]_[(] _[z]_ 1 _[∗][, X][T]_[+1][)] _[ ≥]_[1] _[−][α]_[ and] _[ z]_ 2 _[∗∗][−][z]_ 1 _[∗][< z]_ 2 _[∗][−][z]_ 1 _[∗]_[, contradicting the assumption that] ( _z_ 1 _[∗][, z]_ 2 _[∗]_[)][is][the][solution][to][the][optimization][in][(][24][).][Therefore,] _[F]_[(] _[z]_ 2 _[∗][, X][T]_[+1][)] _[ −][F]_[(] _[z]_ 1 _[∗][, X][T]_[+1][) =] 1 _− α_ . Therefore, we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-13.png)


Since _F_ ( _z_ 2 _, XT_ +1) _−F_ ( _z_ 1 _, XT_ +1) = 1 _−α_ , we can write _F_ ( _z_ 2 _, XT_ +1) = _F_ ( _z_ 1 _, XT_ +1)+1 _−α_ , which means _z_ 2 = _Q_ ( _F_ ( _z_ 1 _, XT_ +1) + 1 _− α, XT_ +1). Since _F_ ( _z_ 1 _, XT_ +1) + 1 _− α ≤_ 1, we have _F_ ( _z_ 1 _, XT_ +1) _≤ α_ . Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-15.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0032-16.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-00.png)


where (i) follows by a change of variables _w_ = _F_ ( _z_ 1 _, XT_ +1) (and thus _z_ 1 = _Q_ ( _w, XT_ +1)). We notice that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-02.png)


where (i) follows by _Qψ_ = (1 _− α_ ) _/_ 2. Thus, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-04.png)


where (i) follows by the assumption that _b_ ( _x, α_ ) _∈_ arg min _w∈_ [0 _,α_ ] _Q_ ( _w_ + 1 _− α, x_ ) _− Q_ ( _w, x_ ) for any _x ∈X_ . By (26), _µ_ � _C_ (1[opt] _−α_ )[(] _[X][T]_[+1][)] � = _µ_ � _C_ (1[conf] _−α_ )[(] _[X][T]_[+1][)] �. **Step 3:** show that if _C_ (1[opt] _−α_ )[(] _[x]_[)][is][uniquely][defined][for][any] _[x][∈X]_[,][then] _[C]_ (1[opt] _−α_ )[(] _[X][T]_[+1][)][=] _C_ (1[conf] _−α_ )[(] _[X][T]_[+1][)][.] 

Notice that _C_ (1[opt] _−α_ )[(] _[x]_[)][=][[] _[r]_[1][(] _[x, α]_[)] _[,][r]_[2][(] _[x, α]_[)]][,][where][the][pair][(] _[r]_[1][(] _[x, α]_[)] _[, r]_[2][(] _[x, α]_[))][uniquely] solves 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-07.png)


By the argument in (25), the pair ( _r_ 1( _x, α_ ) _, r_ 2( _x, α_ )) uniquely solves 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-09.png)


By the same change of variables in (26), _r_ 1( _x, α_ ) uniquely solves 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-11.png)


and _r_ 2( _x, α_ ) = _Q_ ( _F_ ( _r_ 1( _x, α_ ) _, x_ ) + 1 _− α, x_ ). Similar to (26), this can be rewritten as an optimization problem on [0 _, α_ ]. Since _b_ ( _x, α_ ) solves min _w∈_ [0 _,α_ ] _Q_ ( _w_ + 1 _− α, x_ ) _− Q_ ( _w, x_ ), we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0033-13.png)


and _r_ 2( _x, α_ ) = _Q_ ( _b_ ( _x, α_ )+1 _−α, x_ ). Thus, _C_ (1[opt] _−α_ )[(] _[x]_[) = [] _[r]_[1][(] _[x, α]_[)] _[,][r]_[2][(] _[x, α]_[)] = [] _[Q]_[(] _[b]_[(] _[x, α]_[)] _[, x]_[)] _[,][Q]_[(] _[b]_[(] _[x, α]_[)+] 1 _− α, x_ )]. By the same argument as in (27), _C_ (1[conf] _−α_ )[(] _[x]_[) = [] _[Q]_[(] _[b]_[(] _[x, α]_[)] _[, x]_[)] _[,][Q]_[(] _[b]_[(] _[x, α]_[)+1] _[−][α, x]_[)]][.] Therefore, _C_ (1[opt] _−α_ )[(] _[x]_[)][=] _[C]_ (1[conf] _−α_ )[(] _[x]_[)][.][Since][this][holds][for][any] _[x][∈X]_[,][we][have][completed][the] proof. 

33 

## **C.5 Proof of Theorem 4** 

We first prove three auxiliary lemmas. 

**Lemma S1.** Let Assumption S1 hold. Let _V_[˜] _t[∗]_[=] _[F]_[(] _[Y][t][, X][t]_[)] _[ −]_[ˆ] _[b]_[(] _[X][t]_[)] _[ −]_[(1] _[ −][α]_[)] _[/]_[2][for] _[t][∈T]_[2][.] Then 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0034-03.png)


Moreover, for any non-random _δ ∈_ [ _−α, α_ ], 

and 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0034-06.png)


_Proof._ We show the two claims in two steps. 

**Step 1:** show the first claim. 

We observe that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0034-10.png)


Recall that _Ut_ = _F_ ( _Yt, Xt_ ) is independent of _Xt_ and has the uniform distribution on [0,1]. Since _t ∈T_ 2, ( _Ut, Xt_ ) is independent of[ˆ] _b_ ( _·_ ). Since[ˆ] _b_ ( _Xt_ ) _∈_ [0 _, α_ ], we have that [[ˆ] _b_ ( _Xt_ ) _,_[ˆ] _b_ ( _Xt_ ) + 1 _− α_ ] _⊆_ [0 _,_ 1]. Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0034-12.png)


**Step 2:** show the second claim. 

By the same argument as in Step 1, we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0034-15.png)


34 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0035-00.png)


where (i) and (ii) follow by the fact that _Ut_ has the uniform distribution on [0,1] and is independent of _Xt_ and[ˆ] _b_ ( _·_ ). Thus, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0035-02.png)


We now consider the random mapping _δ �→ g_ ( _δ_ ) = min _{δ, α −_[ˆ] _b_ ( _Xt_ ) _}_ + min _{δ,_[ˆ] _b_ ( _Xt_ ) _}_ , where the randomness is from the randomness of _Xt_ . Clearly, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0035-04.png)


For _δ ∈_ [0 _,_ max _{α −_[ˆ] _b_ ( _Xt_ ) _,_[ˆ] _b_ ( _Xt_ ) _}_ ], we have _g_ ( _δ_ ) _≥ δ_ . For _δ ∈_ [max _{α −_[ˆ] _b_ ( _Xt_ ) _,_[ˆ] _b_ ( _Xt_ ) _}, α_ ], we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0035-06.png)


Hence, for any _δ ∈_ [0 _, α_ ], we have _g_ ( _δ_ ) _≥ δ_ , which implies _Eg_ ( _δ_ ) _≥ δ_ . The proof is complete. 

**Lemma S2.** Let Assumption S1 hold. Then sup( _a,x_ ) _∈_ [0 _,_ 1] _×X |Q_[ˆ] ( _a, x_ ) _− Q_ ( _a, x_ ) _|_ = _oP_ (1) and sup _x∈X |L_[ˆ] ( _x_ ) _− L_ ( _x_ ) _|_ = _oP_ (1). 

_Proof._ Let _ε_ = sup _x∈X_ sup _y∈Y_ ( _x_ ) _|F_[ˆ] ( _y, x_ ) _− F_ ( _y, x_ ) _|_ . Fix an arbitrary _δ >_ 0 and _x ∈X_ . ˆ Since _F_[ˆ] ( _·, x_ ) is right-continuous and _Q_[ˆ] ( _a, x_ ) = inf _{y_ : _F_ ( _y, x_ ) _≥ a}_ for any _a ∈_ [0 _,_ 1], we have that _F_[ˆ] ( _Q_[ˆ] ( _a, x_ ) _, x_ ) = _a_ . For simplicity, we write _F_[ˆ] ( _y, x_ ), _Q_[ˆ] ( _a, x_ ), _F_ ( _y, x_ ) and _Q_ ( _a, x_ ) as _F_[ˆ] ( _y_ ), _Q_[ˆ] ( _y_ ), _F_ ( _y_ ) and _Q_ ( _a_ ), respectively whenever no confusion arises. 

We consider the event _Q_ ( _a_ ) _> Q_[ˆ] ( _a_ ) + _δ_ : � � 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0035-11.png)


_b_ + _δ b_ + _δ_ where (i) follows by the fact that _F_ ( _b_ + _δ, x_ ) = _F_ ( _b, x_ )+� _b f_ ( _z, x_ ) _dz ≥ F_ ( _b, x_ )+� _b C_ 1 _dz_ = _F_ ( _b, x_ ) + _C_ 1 _δ_ and (ii) follows by _F_[ˆ] ( _Q_[ˆ] ( _a_ )) = _a_ . Similarly, we observe that 

35 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0036-00.png)


By the above two displays, we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0036-02.png)


Notice that the right-hand side _{ε ≥ C_ 1 _δ}_ does not depend on _x_ or _a_ . Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0036-04.png)


Hence, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0036-06.png)


where (i) follows by _ε_ = _oP_ (1). Since _δ >_ 0 is arbitrary, we have proved sup( _a,x_ ) _∈_ [0 _,_ 1] _×X |Q_[ˆ] ( _a, x_ ) _− Q_ ( _a, x_ ) _|_ = _oP_ (1). 

To show sup _x∈X |L_[ˆ] ( _x_ ) _− L_ ( _x_ ) _|_ = _oP_ (1), we define _η_ = sup( _a,x_ ) _∈_ [0 _,_ 1] _×X |Q_[ˆ] ( _a, x_ ) _− Q_ ( _a, x_ ) _|_ . We observe that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0036-09.png)


and 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0036-11.png)


Thus, _|L_[ˆ] ( _x_ ) _−L_ ( _x_ ) _| ≤_ 2 _η_ . Since this holds for any _x ∈X_ , we have sup _x∈X |L_[ˆ] ( _x_ ) _−L_ ( _x_ ) _| ≤_ 2 _η_ . Because we have proved _η_ = _oP_ (1), it follows that sup _x∈X |L_[ˆ] ( _x_ ) _− L_ ( _x_ ) _|_ = _oP_ (1). The proof is complete. 

**Lemma S3.** Let Assumption S1 hold. Then _Q_[ˆ] _[∗] T_ 2[= (1] _[ −][α]_[)] _[/]_[2 +] _[ o][P]_[(1)][.] 

_Proof._ Fix an arbitrary _δ ∈_ (0 _, α_ ). Define the event 

36 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-00.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-01.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-02.png)


We show these three claims in three steps. 

**Step 1:** show _P_ ( _A[c]_ ) = _o_ (1). Since _{V_[˜] _t[∗][}][t][∈T]_ 2[is][independent,][we][have] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-05.png)


where (i) follows by the fact that _E_ ( _Z − P_ ( _Z_ = 1))[2] = _P_ ( _Z_ = 1) _·_ (1 _− P_ ( _Z_ = 1)) _≤_ max _x∈_ [0 _,_ 1] _x_ (1 _− x_ ) _≤_ 1 _/_ 4 for any Bernoulli variable _Z_ . Thus, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-07.png)


Similarly, we can show that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-09.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0037-10.png)


37 

Therefore, _P_ ( _A[c]_ ) = _o_ (1). 

**Step 2:** show _P_ ( _M_ 1 � _A_ ) _→_ 0. 

On the event _M_ 1 � _A_ , we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0038-03.png)


where (i) follows by the definition of _A_ , (ii) follows by the definition of _M_ 1 and (iii) follows by (29). On the event _A_ , we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0038-05.png)


where (i) follows by Lemma S1. 

The above two displays imply that on the event _M_ 1 � _A_ , (1 _− α_ ) + _δ/_ 4 _≤_ (1 _− α_ )(1 + _|T_ 2 _|[−]_[1] ) + _|T_ 2 _|[−]_[1] , which is _δ ≤_ 4(2 _− α_ ) _/|T_ 2 _|_ . Since _|T_ 2 _| →∞_ and _δ >_ 0 is fixed, we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0038-08.png)


**Step 3:** show _P_ ( _M_ 2 � _A_ ) _→_ 0. 

The argument is similar to Step 2. On the event _M_ 2 � _A_ , we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0038-11.png)


On the event _A_ , we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0038-13.png)


38 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0039-00.png)


where (i) follows by Lemma S1. 

The above two displays imply that on the event _M_ 2 � _A_ , (1 _− α_ ) _− δ/_ 4 _≥_ (1 _− α_ )(1 + _|T_ 2 _|[−]_[1] ) _−|T_ 2 _|[−]_[1] , which is _δ/_ 4 _≤ α/|T_ 2 _|_ . Since _|T_ 2 _| →∞_ and _δ >_ 0 is fixed, we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0039-03.png)


The proof is complete. 

We are now ready to prove Theorem 4. 

_**Proof of Theorem 4** ._ Let _ε_ 1 = _Q_[ˆ] _[∗] T_ 2 _[−]_[(1] _[−][α]_[)] _[/]_[2][,] _[ε]_[2][=][sup] _y,x[|][F]_[ ˆ][(] _[y, x]_[)] _[−][F]_[(] _[y, x]_[)] _[|]_[,] _[ε]_[3][=] sup( _a,x_ ) _∈_ [0 _,_ 1] _×X |Q_[ˆ] ( _a, x_ ) _− Q_ ( _a, x_ ) _|_ and _ε_ 4 = sup _x∈X |L_[ˆ] ( _x_ ) _− L_ ( _x_ ) _|_ . For simplicity, we write � _C_ (1[conf] _−α_ )[instead][of] _C_[�] (1[conf] _−α_ )[(] _[X][T]_[+1][)][.][We][proceed][in][two][steps.] 

**Step 1:** show asymptotic conditional validity. 

ˆ To show _P_ � _YT_ +1 _∈ C_[�] (1[conf] _−α_ ) _[|][ X][T]_[+1] � = 1 _− α_ + _oP_ (1), it suffices to verify that _P_ ( _|V_[ˆ] _T[∗]_ +1 _[| ≤] Q[∗] T_ 2 _[|][ X][T]_[+1][) = 1] _[ −][α]_[ +] _[ o][P]_[(1)][.][We][notice][that] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0039-09.png)


Observe that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0039-11.png)


Since _F_ ( _YT_ +1 _, XT_ +1) is independent of ( _ε_ 1 _, ε_ 2 _,_[ˆ] _b_ ( _XT_ +1) _, XT_ +1) and has the uniform distribution on [0,1], it follows that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0039-13.png)


39 

where 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-01.png)


Clearly, _|β_ ( _z_ 1) _− β_ ( _z_ 2) _| ≤|z_ 1 _− z_ 2 _|_ for any _z_ 1 _, z_ 2 _∈_ R. Thus, _|β_ ([ˆ] _b_ ( _XT_ +1) _− ε_ 1 + _ε_ 2) _− β_ ([ˆ] _b_ ( _XT_ +1)) _| ≤|− ε_ 1 + _ε_ 2 _|_ and _|β_ ([ˆ] _b_ ( _XT_ +1) _− ε_ 1 _− ε_ 2) _− β_ ([ˆ] _b_ ( _XT_ +1)) _| ≤|− ε_ 1 _− ε_ 2 _|_ . This means that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-03.png)


Similarly, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-05.png)


By[ˆ] _b_ ( _XT_ +1) _∈_ [0 _, α_ ], we have _β_ ([ˆ] _b_ ( _XT_ +1)) =[ˆ] _b_ ( _XT_ +1) and _β_ ([ˆ] _b_ ( _XT_ +1)+1 _− α_ ) =[ˆ] _b_ ( _XT_ +1)+ 1 _− α_ . Hence, the above two displays imply that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-07.png)


By (30), we have 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-09.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-10.png)


In other words, we can write it as 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-12.png)


We can now compute the length of _C_[�] (1[conf] _−α_ )[.][We][observe] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0040-14.png)


40 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0041-00.png)


where (i) follows by _Q_[ˆ] _[∗] T_ 2[= (1] _[ −][α]_[)] _[/]_[2 +] _[ ε]_[1][.] We notice that for any _a_ 1 _, a_ 2 _∈_ [0 _,_ 1] with _a_ 1 _> a_ 2 and for any _x ∈X_ , 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0041-02.png)


Since _|β_ ( _z_ 1) _− β_ ( _z_ 2) _| ≤|z_ 1 _− z_ 2 _|_ for any _z_ 1 _, z_ 2 _∈_ R, it follows that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0041-04.png)


and 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0041-06.png)


The above two displays and (31) imply 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0041-08.png)


where (i) follows by[ˆ] _b_ ( _XT_ +1) _∈_ [0 _, α_ ] and (ii) follows by _ε_ 3 = _oP_ (1) and _ε_ 4 = _oP_ (1) (Lemma S2) as well as _ε_ 1 = _oP_ (1) (Lemma S3). The desired result follows by 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0041-10.png)


41 

## **C.6 Proof of Theorem 5** 

For simplicity, we may omit _XT_ +1 and _α_ when no confusion can arise. For example, we write _F_ ( _y_ ), _Q_ ( _y_ ), _f_ ( _y_ ) and _b_ rather than _F_ ( _y, XT_ +1), _Q_ ( _y, XT_ +1), _f_ ( _y, XT_ +1) and _b_ ( _XT_ +1 _, α_ ), respectively. 

By Lemma 2, we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-03.png)


where _Qψ_ (1 _− α_ ) is the (1 _− α_ ) quantile of _Vt[∗]_[=] _[ F]_[(] _[Y][t][, X][t]_[)] _[−][b]_[(] _[X][t][, α]_[)] _[−]_[1] _[−]_ 2 _[α]_[.][Again by Lemma] 2, _Qψ_ (1 _− α_ ) =[1] _[−]_ 2 _[α]_[.][Therefore,] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-05.png)


On the other hand, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-07.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-08.png)


The rest of the proof proceeds in two steps. 

**Step 1:** show that _Q_[ˆ] _[∗] T_ 2[= (1] _[ −][α]_[)] _[/]_[2 +] _[ o][P]_[(1)][.] 

Notice that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-12.png)


By the elementary inequality ( _a_ + _b_ )[2] _≤_ 2 _a_[2] + 2 _b_[2] , we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-14.png)


We now show that _G∗_ ( _·_ ) is Lipschitz. Fix any _y_ 1 _, y_ 2 in the support of _Vt[∗]_ such that _y_ 1 _< y_ 2. Notice that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-16.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0042-17.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-00.png)


where (i) follows by the fact that conditional on _Xt_ , _Ut_ follows the uniform distribution on (0 _,_ 1). Thus, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-02.png)


Therefore, sup _y_ 1= _y_ 2 _|G∗_ ( _y_ 2) _− G∗_ ( _y_ 1) _|/|y_ 2 _− y_ 1 _| ≤_ 2. By the same argument as the in the proof of Lemma 1, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-04.png)


By the continuity of _G∗_ ( _·_ ), we have that _Q_[ˆ] _[∗] T_ 2[=] _[G][−] ∗_[1][(1] _[ −][α]_[) +] _[ o][P]_[(1)][(since] _[Q]_[ˆ] _[∗] T_ 2[is][the] (1 _− α_ )(1 + 1 _/|T_ 2 _|_ ) quantile of _G_[˜] _∗_ ( _·_ )). Notice that _G[−] ∗_[1][(1] _[ −][α]_[)][=] _[Q][ψ]_[(1] _[ −][α]_[)][.][By][Lemma][2][,] _Qψ_ (1 _− α_ ) = (1 _− α_ ) _/_ 2. This means that _Q_[ˆ] _[∗] T_ 2[= (1] _[ −][α]_[)] _[/]_[2 +] _[ o][P]_[(1)][.] 

**Step 2:** derive the final result. 

ˆ By Step 1 and the assumptions that[ˆ] _b_ ( _XT_ +1 _, α_ ) _−b_ = _oP_ (1) and sup _y∈_ R _F_ ( _y, XT_ +1) _− F_ ( _y, XT_ +1) = ��� ��� _oP_ (1), we have that _ε_ ¯1 := sup _y∈_ R _|ε_ 1( _y_ ) _|_ = _oP_ (1) and _ε_ ¯2 := sup _y∈_ R _|ε_ 2( _y_ ) _|_ = _oP_ (1). Define _H_ 1 = _{y_ : _b − ε_ ¯1 _≤ F_ ( _y_ ) _≤ b_ + 1 _− α_ + ¯ _ε_ 2 _}_ and _H_ 2 = _{y_ : _b_ + ¯ _ε_ 1 _≤ F_ ( _y_ ) _≤ b_ + 1 _− α − ε_ ¯2 _}_ . Clearly, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-08.png)


On the other hand, we observe that _H_ 1 is an interval that can be written as 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-10.png)


Since _P_ ( _|YT_ +1 _| ≤ C_ 2 _| XT_ +1) = 1 and _F_ ( _·_ ) is strictly increasing, _Q_ (0) and _Q_ (1) are well defined and satisfy max _{|Q_ (0) _|, |Q_ (1) _|} ≤ C_ 2 almost surely. 

By (32), we can write _C_ (1[opt] _−α_ )[(] _[X][T]_[+1][)][as][an][interval] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-13.png)


Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-15.png)


Notice that _dQ_ ( _u_ ) _/du_ = 1 _/f_ ( _Q_ ( _u_ )). By assumption, the density is bounded below by _C_ 1 on the support of _YT_ +1 _| XT_ +1. It follows that _|dQ_ ( _u_ ) _/du|_ is uniformly bounded by 1 _/C_ 1. Thus, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0043-17.png)


43 

and similary 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0044-01.png)


The above three displays imply 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0044-03.png)


Similarly, we can show that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0044-05.png)


By (33), we have that, almost surely 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0044-07.png)


The above three displays imply 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0044-09.png)


The desired result follows by _ε_ ¯1 = _oP_ (1) and _ε_ ¯2 = _oP_ (1). 

## **D Time series discussion** 

For time series data _{Zt}[T] t_ =1[+1][with] _[Z][t]_[=][(] _[X][t][, Y][t]_[)][,][it][is][often][plausible][that][these] _[T]_[+][1] observations are not independent. Here, we assume that data is strictly stationary, i.e., for any _m >_ 1, the distribution ( _Zt−m, Zt−m_ +1 _, . . . , Zt−_ 1) does not depend on _t_ . This is a common assumption in the time series literature. Although the data is not independent, it is often not strongly dependent either. Usually, we work with various notions of weak dependence. A popular way of defining weak dependence is in terms of mixing conditions. There are numerous mixing conditions, see, for example, Bradley (2005, 2007); Dedecker et al. (2007). We focus on the _β_ -mixing condition (also known as the absolute regularity condition): for any _m >_ 1, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0044-13.png)


where _P{Zt}t≤s_ denotes the probability measure of _{Zt}t≤s_ , _P{Zt}t≥s_ + _m_ denotes the probability measure of _{Zt}t≥s_ + _m_ and _P{Zt}t≤s, {Zt}t≥s_ + _m_ denotes the probability measure of the joint random components ( _{Zt}t≤s, {Zt}t≥s_ + _m_ ). Here, _⊗_ denotes the product measure and _∥·∥TV_ is the total-variation norm. Since the data is strictly stationary, the above definition does 

44 

not depend on _s_ . We borrow the above definition of Section 1.6 of Rio (2017), but equivalent definitions can be found in Bradley (2005, 2007) among others.[13] 

We say that the sequence _{Zt}_ is _β_ -mixing if _β_ ( _m_ ) _→_ 0 as _m →∞_ . The _β_ -mixing condition captures the idea that observations that are far apart in time become nearly independent. As _m_ increases, _{Zt}t≤s_ and _{Zt}t≥s_ + _m_ become more independent, in the sense that the joint distribution _P{Zt}t≤s, {Zt}t≥s_ + _m_ is close to the product measure of the marginal distributions _P{Zt}t≤s ⊗ P{Zt}t≥s_ + _m_ . 

The _β_ -mixing condition is satisfied for a large class of stochastic processes. The simplest examples are perhaps _m_ -dependent processes, which satisfy that _{Zj}j≤t_ and _{Zj}j≥s_ are independent as long as _s − t ≥ m_ for some fixed _m_ . Moving average processes are _m_ - dependent. Autoregressive moving average (ARMA) processes with independent errors are _β_ -mixing. In general, strictly stationary Markov chains that are Harris recurrent and aperiodic are _β_ -mixing (e.g., Bradley, 2005; Meyn and Tweedie, 2012). Several stochastic volatility models for asset returns, including the popular generalized autoregressive conditionally heteroskedastic (GARCH) models are also _β_ -mixing with _β_ ( _m_ ) decaying exponentially with _m_ (e.g., Boussama, 1998; Carrasco and Chen, 2002; Francq and Zakoïan, 2006). 

Now we consider the problem of empirical risk minimization mentioned in Section 3. Let _F_ be a model, i.e., a class of functions of _Zt_ = ( _Xt, Yt_ ). Define _F[∗]_ = arg min _f ∈F RT_ +1( _f_ ), where _RT_ +1( _f_ ) = ( _T_ +1) _[−]_[1][ �] _[T] t_ =1[+1] _[E]_[[] _[L]_[(] _[Z][t][, f]_[)]][, where] _[ L]_[ is a loss function.][Let] _[F]_[ˆ][= arg min] _[f][∈F][R]_[ˆ] _[T]_[+1][(] _[f]_[)][,] where _R_[ˆ] _T_ +1( _f_ ) = ( _T_ + 1) _[−]_[1][ �] _[T] t_ =1[+1] _[L]_[(] _[Z][t][, f]_[)][.][Suppose][that][the][following][entropy][condition] with brackets holds: 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0045-04.png)


where _N_ [] is the bracketing number (see van der Vaart and Wellner (1996)), _L_ ( _F_ ) is the class _{L_ ( _Zt, f_ ) : _f ∈F}_ and _∥· ∥_ 1 _,P_ is the _L_ 1-norm _∥f ∥_ 1 _,P_ = _E|f_ ( _Zt_ ) _|_ . By Theorem 8.3 of Rio (2017), sup _f ∈F |R_[ˆ] _T_ +1( _f_ ) _− RT_ +1( _f_ ) _|_ = _OP_ ( _T[−]_[1] _[/]_[2] ) as long as[�] _[∞] m_ =1 _[β]_[(] _[m]_[)] _[<][∞]_[.] (Similar results for empirical processes of dependent data can be found in Dedecker and Louhichi (2002).) By the usual arguments, it follows that 0 _≤ RT_ +1( _F_[ˆ] ) _− RT_ +1( _F[∗]_ ) _≤ oP_ (1). Suppose that the risk function is convex in a neighborhood of _F[∗]_ : there exist _C_ 1 _, C_ 2 _>_ 0 such that _RT_ +1( _f_ ) _− RT_ +1( _F[∗]_ ) _≥ C_ 2 _∥f − F[∗] ∥_[2] sup[whenever] _[∥][f][−][F][ ∗][∥]_[sup] _[≤][C]_[1][and] _[f][∈F]_[,] where _∥f ∥_ sup = sup _z |f_ ( _z_ ) _|_ . Then sup _y,x |F_[ˆ] ( _y, x_ ) _− F[∗]_ ( _y, x_ ) _|_ = sup _z |F_[ˆ] ( _z_ ) _− F[∗]_ ( _z_ ) _|_ = _oP_ (1). This implies the consistency requirement in Assumption 1. Importantly, _F[∗]_ does not need to be the true CDF _F_ because _F_ may or may not be in _F_ . 

For the popular linear QR model, we establish a more concrete result; similar results can 

> 13To see that these definitions are equivalent, one can find details in Theorem 3.29 of Bradley (2007). 

45 

_T_ +1 be established for DR. Suppose that _Xt ∈_ R _[d]_ for a fixed _d_ . Let ˆ _γ_ ( _u_ ) = arg min _γ∈_ Γ � _t_ =1 _[ρ][u]_[(] _[Y][t][−] Xt[⊤][γ]_[)][ for] _[ u][ ∈]_[[] _[c][T][,]_[ 1] _[−][c][T]_[]][, where][ Γ] _[ ⊂]_[R] _[d]_[ is a compact set and] _[ c][T][>]_[ 0][ is either a small constant] or a sequence tending to zero. Define 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0046-01.png)


Let _∥· ∥_ 2 denote the Euclidean norm in R _[d]_ . We have the following result. 

**Theorem S1.** Assume that the data ( _Xt, Yt_ ) is strictly stationary. Let _γ[∗]_ ( _u_ ) = arg min _γ∈_ Γ _Eρu_ ( _Yt− Xt[⊤][γ]_[)][with] _[ρ][u]_[(] _[a]_[) =] _[ a]_[(] _[u][ −]_ **[1]** _[{][a][ ≤]_[0] _[}]_[)][.][Define] 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0046-04.png)


Suppose that the following conditions hold: 

1. There exists a constant _C_ 1 _>_ 0 such that _∥Xt∥_ 2 _≤ C_ 1 and _|Yt| ≤ C_ 1 almost surely. 

2. The _β_ -mixing coefficient of ( _Xt, Yt_ ) satisfies[�] _[∞] m_ =1 _[β]_[(] _[m]_[)] _[ <][ ∞]_[.] 

3. There exists a function _h_ ( _·_ ) such that lim _δ→_ 0 _h_ ( _δ_ ) = 0 and _|F[∗]_ ( _y_ 1 _, x_ ) _− F[∗]_ ( _y_ 2 _, x_ ) _| ≤ h_ ( _|y_ 1 _− y_ 2 _|_ ) for any ( _y_ 1 _, y_ 2) and any _x_ with _∥x∥_ 2 _≤ C_ 1. 

4. _f_ ( _y, x_ ) = _∂F_ ( _y, x_ ) _/∂y_ exists and there exists a constant _C_ 2 _>_ 0 such that _f_ ( _y, x_ ) _≥ C_ 2 for any _x_ and any _y ∈_ [ _s_ 1( _x_ ) _, s_ 2( _x_ )], where [ _s_ 1( _x_ ) _, s_ 2( _x_ )] is the support of the distribution _Yt | Xt_ = _x_ . 

5. the smallest eigenvalue of _E_ ( _XtXt[⊤]_[)][is][bounded][below][by][a][constant] _[C]_[3] _[>]_[ 0][.] 

Then sup _y∈_ R _, ∥x∥_ 2 _≤C_ 1 _|F_[ˆ] ( _y, x_ ) _− F[∗]_ ( _y, x_ ) _|_ = _oP_ (1). 

Theorem S1 establishes the uniform consistency of _F_[ˆ] , which guarantees the consistency requirement in Assumption 1 . Notice that Theorem S1 does not assume that _F[∗]_ is the true conditional distribution function _F_ . It thus generalizes the analysis of QR under misspecification in Angrist et al. (2006) to time series settings. 

The assumptions of Theorem S1 are relatively mild. The boundedness of _Xt_ and _Yt_ can be relaxed with extra technical arguments. The summability of _β_ -mixing coefficients holds if _β_ ( _m_ ) decays exponentially. The third assumption says that _F[∗]_ ( _y, x_ ) is uniformly continuous in _y_ . The last assumption states that the true conditional density of _Yt | Xt_ is bounded away from zero on the support. 

46 

_**Proof of Theorem S1** ._ We proceed in two steps. 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-01.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-02.png)


where (i) follows by _|y − x[⊤] γ_ 2 _| ≤ C_ 1 + _C_ 1 sup _γ∈_ Γ _∥γ∥_ 2. Since Γ is compact and _d_ is fixed, sup _γ∈_ Γ _∥γ∥_ 2 is bounded by a positive constant. Hence, ( _γ, u_ ) _�→ ρu_ ( _y − x[⊤] γ_ ) is Lipschitz. By Theorem 2.7.11 of van der Vaart and Wellner (1996) and the usual covering number bounds for Euclidean balls (e.g., Corollary 4.2.13 of Vershynin (2018)), we have that for any norm _∥· ∥_ , the bracketing number satisfies 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-04.png)


where _K_ 1 _≥_ 1 is a constant depending only on _C_ 1, sup _γ∈_ Γ _∥γ∥_ 2 and _d_ and _G_ is the class of functions _ρu_ ( _y − x[⊤] γ_ ) with ( _γ, u_ ) _∈_ Γ _×_ [ _c_ 1 _,_ 1 _− c_ 2]. Notice that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-06.png)


Therefore, it follows, by Theorem 8.3 of Rio (2017), that _δT_ := sup( _γ,u_ ) _∈_ Γ _×_ [ _c_ 1 _,_ 1 _−c_ 2] _|R_[ˆ] ( _γ, u_ ) _− R_ ( _γ, u_ ) _|_ = _OP_ ( _T[−]_[1] _[/]_[2] ). 

By the definition of _γ[∗]_ ( _u_ ) and ˆ _γ_ ( _u_ ), we observe that _R_ ( _γ[∗]_ ( _u_ ) _, u_ ) _≤ R_ (ˆ _γ_ ( _u_ ) _, u_ ) _≤ R_[ˆ] (ˆ _γ_ ( _u_ ) _, u_ )+ _δT ≤ R_[ˆ] ( _γ[∗]_ ( _u_ ) _, u_ ) + _δT ≤ R_ ( _γ[∗]_ ( _u_ ) _, u_ ) + 2 _δT_ . Hence, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-09.png)


For any _γ ∈_ Γ, we observe that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-11.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0047-12.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-00.png)


where (i) follows by Equation (4.3) of Koenker (2005b). By the optimality condition of _γ[∗]_ ( _u_ ) = arg min _γ∈_ Γ _Eρu_ ( _Yt − Xt[⊤][γ]_[)][,][we][have] _[E]_[(] _[F]_[(] _[X] t[⊤][γ][∗]_[(] _[u]_[)] _[, X][t]_[)] _[ −][u]_[)] _[X] t[⊤]_ = 0. Thus, the above display implies that for any _γ ∈_ Γ, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-02.png)


where (i) follows by _f_ ( _y, x_ ) _≥ C_ 2 for _y ∈_ [ _s_ 1( _x_ ) _, s_ 2( _x_ )]. By (34) and the above display, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-04.png)


Since this bound holds for any _u_ , we have that 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-06.png)


ˆ Since we have proved _δT_ = _oP_ (1), we have sup _u∈_ [ _cT ,_ 1 _−cT_ ] _∥γ_ ( _u_ ) _− γ[∗]_ ( _u_ ) _∥_ 2 = _oP_ (1). 

**Step 2:** show the desired result. 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-09.png)



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-10.png)


We observe that for any _x ∈_ R _[d]_ with _∥x∥_ 2 _≤ C_ 1, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-12.png)


where (i) follows by (35). Similarly, we can show that _F_[ˆ] ( _y, x_ ) _≥ F[∗]_ ( _y − C_ 1 _εT , x_ ). Therefore, 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0048-14.png)


Since this bounds holds for any _y_ and _x_ , we have that sup _∥x∥_ 2 _≤C_ 1 sup _y∈_ R _|F_[ˆ] ( _y, x_ ) _− F[∗]_ ( _y, x_ ) _| ≤ h_ ( _C_ 1 _εT_ ). By _εT_ = _oP_ (1) and lim _δ→_ 0 _h_ ( _δ_ ) = 0, the desired result follows. 

48 


![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0049-00.png)


**----- Start of picture text -----**<br>
E Additional figures<br>**----- End of picture text -----**<br>



![](markdown_output/distributional-cp-2021_images/distributional-cp-2021.pdf-0049-01.png)


**----- Start of picture text -----**<br>
DCP−QR DCP−QR* DCP−DR<br>0.5 0.6 0.7 0.8 0.9 1.0 0.5 0.6 0.7 0.8 0.9 1.0 0.5 0.6 0.7 0.8 0.9 1.0<br>CQR CQR−m CQR−r<br>0.5 0.6 0.7 0.8 0.9 1.0 0.5 0.6 0.7 0.8 0.9 1.0 0.5 0.6 0.7 0.8 0.9 1.0<br>CP−OLS CP−loc<br>0.5 0.6 0.7 0.8 0.9 1.0 0.5 0.6 0.7 0.8 0.9 1.0<br>**----- End of picture text -----**<br>


Figure 5: Histograms of estimated conditional coverage probability. Vertical line at nominal coverage of 1 _− α_ = 0 _._ 9. 

49 

