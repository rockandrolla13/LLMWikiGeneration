_Journal of Financial Econometrics_ , 2026, **24(2)** , nbag003 https://doi.org/10.1093/jjfinec/nbag003 **Article - with submission fee** 

**==> picture [64 x 52] intentionally omitted <==**

## **Efficiently Weighted Estimation of Tail and Interquantile Expectations** 

## **Sander Barendse 1** 

1Faculty of Economics and Business, University of Amsterdam, Roetersstraat 11, Amsterdam, 1018 WB, The Netherlands 

Address correspondence to Sander Barendse, Faculty of Economics and Business, University of Amsterdam, Roetersstraat 11, Amsterdam, WB 1018, The Netherlands, or e-mail: s.c.barendse@uva.nl. 

## **Abstract** 

Tail expectations have recently attracted much attention in economics for their ability to capture risk. We develop a semiparametric estimator for the joint estimation of (nonlinear) models of tail expectations with some tail quantile as the left or right threshold, and interquantile expectations, partial expectations between two thresholding quantiles. The joint estimator of these quantities can be used to test for heterogeneity in the conditional distribution, with special attention to distinct tail behavior. We derive efficient weights and asymptotic properties of the estimator for time-series data. The estimator does not require the specification of the conditional distribution, and its computation relies on standard techniques. In an empirical application in finance, we test for a disproportionate contribution of tail events to the average abnormal return of portfolio strategies. 

**Keywords:** expected shortfall, interquantile expectation, quantile, quantile regression, risk management, tail expectation 

**JEL classifications:** C13, C14, C32, C58, G32 

Tail expectations have proven to be an essential tool for the economist in the wake of the financial crisis, with many studies of systemic risk relying on them to formulate measures of systemic risk in economic systems (see, e.g., Acharya et al. 2017; Brownlees and Engle 2017; the CoES measure in Adrian and Brunnermeier 2016). A key insight underlying the use of tail expectations is the heterogeneity in the relationships amongst the variables of interest and the predictor variables across the distribution, resulting in the need to model the tails separately. Tail expectations are also better suited to model risk than tail quantiles, since the former adhere to certain properties of risk measures that ensure the prudent capture of risk, whereas quantiles do not (these properties include subadditivity and convexity, see, e.g., Artzner et al. 1999; Basak and Shapiro 2001). 

In this article, we propose a joint estimator of the left- and right tail-expectations with some left or right tail-quantile as threshold, and the interquantile expectations (IQEs), 

An earlier version of this paper was circulated under the name _Interquantile Expectation Regression_ . I thank Tom Boot, Dick van Dijk, Timo Dimitriadis, Frank Kleibergen, Erik Kole, Robin Lumsdaine, Bent Nielsen, Richard Paap, Andrew Patton, Andreas Pick, and Chen Zhou for valuable discussions and feedback, as well as seminar participants at the 10th Annual SoFiE Conference in New York (2017), the Econometric Society European Meeting in Lisbon (2017), American University (2017), and Erasmus University Rotterdam (2017), the World Congress of the Econometric Society (2020), and the Bristol Econometric Study Group (2022). All remaining errors are my own. 

**Received:** April 23, 2024. **Revised:** October 7, 2025. **Accepted:** February 3, 2026 © The Author(s) 2026. Published by Oxford University Press. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https:// creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. 

**2** _Journal of Financial Econometrics_ 

partial expectations between two thresholding quantiles. The estimator is easy to compute and semiparametric in nature, such that it does not require the specification of a conditional distribution. Naturally, the estimator can be used to estimate tail and IQEs. However, we focus on its application in a test for the presence of heterogeneity between tail behavior and behavior in the body of the distribution. Such tests provide important justification for the use of tail measures, and our joint estimator is a natural contender for such tests because of the beneficial properties of tail expectations indicated above. 

The estimator is easy to compute since it is a multi-stage estimator with a first stage consisting of standard quantile regression steps to obtain the thresholding quantiles and a second stage consisting of least-squares estimation to obtain the expectations. Importantly, the second stage is locally robust to the first stage (see Chernozhukov et al. 2016 for an elaboration of local robustness), which implies that the prior estimation of the quantile will not change the asymptotic distribution of the tail expectation estimator. We allow for nonlinear quantile and tail expectation models as well as time-series properties in the data, since such models and data are commonly required and encountered in economics and finance. Implementation is easy using (nonlinear) quantile regression and least-squares toolboxes, included in many statistical computing environments. 

In a second contribution, we derive efficient estimation weights for the individual estimators. Given that estimation in the tails often comes with large estimation error, efficient estimation is an important consideration. The efficient weights are easy to compute, as they can be calculated from a collection of quantile regression estimates at different quantile levels and initial parameter estimates for the respective tail expectation or IQE. We also provide efficient weighting for a location-scale model as a special case, for which computation is especially easy. Simulation results show that efficient weighting leads to a smaller standard deviation of parameter estimates and improved coverage rates of confidence intervals. 

In an empirical illustration in finance, we use our estimator to study how tail events contribute to the average abnormal return of size and momentum portfolio strategies in US markets and find a disproportionally large positive contribution of tail events to the average abnormal return of stocks with small market equity, where average abnormal returns are captured as the intercept in a regression of portfolio returns on the Fama-French factors (see Fama and French 1992, 1993). This disproportionality can affect the feasibility of an investment strategy and is therefore of interest to investors, since short positions in stocks with small market equity, for example, are exposed to disproportionally large, negative returns in tail events. 

In related literature, Patton et al. (2019) and Dimitriadis and Bayer (2019) have used the strictly consistent joint loss function family of Fissler and Ziegel (2016) (FZ) to derive semiparametric joint M-estimators for the quantile ( _or_ Value-at-Risk) and left tail expectation (LTE) ( _or_ Expected Shortfall). We show that our efficient weighted estimator is also efficient amongst this class of estimators. Moreover, we find that we can always find a weighted estimator that is asymptotically equivalent to any such M-estimator based on a “smooth” member of the FZ loss function family. Meanwhile, our estimator can be estimated using standard econometric techniques. An example highlighting the relative computational advantages of our estimator versus the M-estimator concerns the linear model. With our method, this model is estimated easily using (weighted) linear quantile regression and (weighted) OLS, whereas M-estimation requires a search algorithm to solve a nonsmooth minimization problem. In recent work, Dimitriadis et al. (2021) study efficiency results for M-estimators based on the family of FZ-loss functions in more detail. The IQE has received less attention, but recently consistent loss functions for IQEs are studied in Fissler and Ziegel (2021). 

There are several additional papers proposing related estimators of left-and right-tail expectation models. Taylor (2008a, 2008b) propose estimators based on expectiles and a specific FZ loss function. Escanciano and Mayoral (2008) propose a two-stage 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **3** 

semiparametric estimator that is not locally robust to the quantile estimation in the first stage. Nonparametric estimation methods are proposed in Brazauskas et al. (2008) and Chen (2007). A large number of other (unconditional) tail expectation estimators is summarized in Nadarajah et al. (2014). Finally, Komunjer and Vuong (2010) develop a quantile regression estimator that reaches the semiparametric efficiency bound for dynamic nonlinear models. 

The remainder is structured as follows. In Section 1, we introduce the tail and IQE models. In Section 2 we provide inference results and efficient weighting. In Section 3 we introduce tests of parameter heterogeneity. In Section 4 we use Monte Carlo experiments to study the small-sample properties of our estimators. Section 5 contains the empirical application of our method. Section 6 concludes. Supplementary Materials are available online and contain additional simulations and mathematical proofs. 

## **1 Model** 

In this section, we first formally define the LTE, the right tail expectation (RTE), and the IQE. Subsequently, we explore model specifications. 

We are interested in modeling the conditional LTE, RTE, and IQE of some random variable _Yt_ 2 Y � R, conditional on some random vector _Xt_ 2 X � R _[d]_ , _d <_ 1. The vector _Xt_ can include the present and lags of the vector of available regressors _Zt_ and the lags of _Yt_ itself. We therefore allow for the inclusion of contemporaneous regressors. However, in forecasting settings, we use only lags of the data, whereas in the iid setting we strictly use contemporaneous data. 

The _d_ elements of _Xt_ are specified by the researcher. For instance, in an AR(2)-model _Xt_ includes elements up to and including the second lag of _Yt_ . In principle, our estimation procedure can be used to estimate models that depend on an infinite amount of regressors, such as those belonging to a GARCH(1,1) model, which incorporates all past of observations f _Yt −_ 1 _; Yt −_ 2 _;_ ...g. However, the development of asymptotic theory for such models is left for further work. 

The formal definition of the conditional LTE, RTE, and IQE requires prespecified quantile levels that indicate the thresholding quantiles. To simplify notation, we consider two quantile levels _α_ and _α_[0] , with 0 _< α < α_[0] _<_ 1, and study the conditional quantile at the level _α_ , denoted _Qt_ ð _α_ Þ, the LTE at _α_ , denoted _E_[ð] _t[L]_[Þ] , the IQE between _α_ and _α_[0] , denoted _E_[ð] _t[I]_[Þ][, and ] the RTE at _α_[0] , denoted _E_[ð] _t[R]_[Þ] . They are formally defined as follows: 

**==> picture [259 x 58] intentionally omitted <==**

with _Ft_ ð�Þ, _Ft[−]_[1] ð�Þ, _ft_ ð�Þ, and _Et_ ½�� the distribution function, the (generalized) inverse distribution function, the probability density function, and the expectation of _Yt_ conditional on _Xt_ , respectively. 

For estimation purposes, we consider the following model for _Yt_ in terms of the regression vector _Xt_ and a rank variable _Ut_ : 

**==> picture [227 x 12] intentionally omitted <==**

where _Ut_ is uniformly distributed on ð0 _;_ 1Þ conditional on _Xt_ , _h_ ð� _;_ �Þ and _η_ 0ð�Þ are vector functions and _λ_ 0 is a parameter vector. The rank variable _Ut_ represents the _idiosyncratic error_ , 

**4** _Journal of Financial Econometrics_ 

_innovation_ , _news_ , or _unobserved heterogeneity_ realized in period _t_ . The condition _Ut_ j _Xt_ � Unifð0 _;_ 1Þ is not restrictive, as an equivalent model can be given for any continuous conditional distribution _FU_ j _X_ of _Ut_ by substituting _η_ 0ð�Þ by ~ _η_ 0ð�Þ ¼ _η_ 0ð _FU_ j _X_ ð�ÞÞ, where _FU_ j _X_ ð�Þ is the cdf belonging to _FU_ j _X_ . The model allows for substantial heterogeneity in the conditional quantiles, LTEs, IQEs, and RTEs, and is commonly used in the literature on quantile regression, see Chernozhukov and Hansen (2006), and references therein. Special cases include the nonlinear location-scale model and the linear-in-parameter model, as discussed below. 

The model in Equation (2) must satisfy the following conditions. 

- **Condition Y.** The functions _h_ ð� _;_ �Þ and _η_ 0ð�Þ are such that _h_ ð _Xt; λ_ 0Þ[0] _η_ 0ð _u_ Þ is strictly increasing in _u_ 2 ð0 _;_ 1Þ (a.s.). 

Condition Y implies unique quantiles of _Yt_ conditional on _Xt_ and is a standard condition in the quantile regression literature. 

Recall that _Xt_ may include elements of (lags of) the vector of regressors _Zt_ and lags of the variable of interest _Yt_ . The following condition imposes restrictions on the dependence of the data. 

**Condition S.** The following conditions hold: 

- i) the sequence of available regressors f _Zt_ g is stationary and _β_ -mixing with size _− r=_ ð _r −_ 1Þ, _r >_ 1; 

- ii) the sequence of rank variables f _Ut_ g is independent; 

iii) _Ut_ is independent of f _Zt; Zt −_ 1 _;_ ...g. 

Condition S implies that fð _Yt; X_[0] _t_[Þ][0][g][is stationary and ] _[β]_[-mixing, such that ][ð] _[Y][t][;][X]_[0] _t_[Þ][0][is as-] ymptotically independent, but is allowed to be dependent on finite leads and lags of itself. It also implies _Ut_ is independent of _Xt_ . In the Supplementary Material we relax this assumption and allow _Ut_ to be uniformly distributed conditional on _Xt_ , see Supplementary Section S5.4. Many commonly used processes in economics and finance are _β_ -mixing. For instance, Buhlmann (1995)€ notes that ARMA( _p; q_ ) processes with innovations dominated by the Lebesgue measure satisfy this condition and Boussama et al. (2011) provide conditions under which multivariate GARCH processes are _β_ -mixing with faster (geometric) rates than imposed above. See Bradley (2005) for a detailed treatment of mixing. Let _m_ 2 f _L; I; R_ g denote the partial expectation under consideration, with _L_ , _I_ , and _R_ referring to the LTE, IQE, and RTE, respectively. For the model in Equation (2), the conditional quantile _Qt_ ð _α_ Þ and the partial expectations _E_[ð] _t[m]_[Þ] can all be expressed in terms of the functional specification _st_ ð _β_ Þ ¼ _h_ ð _Xt; λ_ Þ[0] _η_ , with _β_ ¼ ð _η_[0] _; λ_[0] Þ[0] . Specifically, _Qt_ ð _α_ Þ ¼ _st_ ð _ν_ 0ð _α_ ÞÞ, with _ν_ 0 ¼ ð _η_ 0ð _α_ Þ[0] _; λ_[0] 0[Þ][0][, and ] _[E] t_[ð] _[m]_[Þ] ¼ _st_ ð _β_[ð] 0 _[m]_[Þ][Þ][, with ] _[β]_[ð] 0 _[m]_[Þ] ¼ ð _η_[ð] 0 _[m]_[Þ] 0 _; λ_ 00[Þ][0][, with ] _[η]_[ð] 0 _[L]_[Þ] ¼ 1 _=α_ Ð _α_ 0 _[η]_[0][ð] _[u]_[Þ] _[du]_[, ] _α_ 0 1 _η_[ð] 0 _[I]_[Þ][¼][ 1] _[=]_[ð] _[α]_[0] _[ −α]_[Þ] Ð _α[η]_[0][ð] _[u]_[Þ] _[du ]_[and ] _[η]_ 0[ð] _[R]_[Þ] ¼ 1 _=_ ð1 _−α_[0] Þ Ð _α_[0] _[ η]_[0][ð] _[u]_[Þ] _[du ]_[(a.s.). For the special case of a lin-] ear model, that is _h_ ð _Xt; λ_ 0Þ ¼ _Xt_ , the parameter vector _β_ reduces to a _d_ -dimensional vector, since _λ_ 0 does not have to be specified. 

We now discuss two special cases of the model in Equation (2). 

**Example 1** (Nonlinear location-scale model). 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **5** 

Consider the model: 

**==> picture [118 x 11] intentionally omitted <==**

with (nonlinear) scalar functions _hμ_ ð� _;_ �Þ and _hσ_ ð� _;_ �Þ and iid innovations _εt_ � _Fε_ , independent of f _Xt; Xt −_ 1 _;_ ...g, _hσ_ ð _Xt;_ f0Þ _>_ 0 (a.s.), and _Fε_ some continuous distribution. This model can be written in the form of Equation (2) as _h_ ð _Xt; λ_ 0Þ ¼ ð _hμ_ ð _Xt; ξ_ 0Þ _; hσ_ ð _Xt;_ f0ÞÞ[0] , where _λ_ 0 ¼ ð _ξ_[0] 0 _[;]_[f] 0[0][Þ][0][, and ] _[η]_ 0[ð] _[u]_[Þ ¼ ð][1] _[;][F] ε[−]_[1][ð] _[u]_[ÞÞ][0][, with ] _[F] ε[−]_[1][ð�Þ][ the (generalized) inverse distribu-] tion function belonging to _Fε_ . Common specifications for _hμ_ ð _Xt; ξ_ 0Þ include the (nonlinear) AR-model, while common specifications for _hσ_ ð _Xt;_ f0Þ include ARCH-type models or the HAR model of Corsi (2009). Examples are included in Sections 4 and S3 in the Supplementary Material. 

**Example 2** (Linear-in-parameter model). Consider the model in Equation (2) with _h_ ð _Xt; λ_ 0Þ ¼ _Xt_ : 

**==> picture [60 x 11] intentionally omitted <==**

This data generating process (DGP) generates linear quantiles, LTEs, IQEs, and RTEs, but with potential heterogeneity in the parameters. In this case, _β_ reduces to a d-dimensional vector. The model must be parameterized so that the conditional quantiles are uniformly increasing. It is often used in economics and statistics (see, e.g., Chernozhukov and Hansen 2006, and references therein) to introduce heterogeneity across quantiles and is quite general. A specific instance of this model is the linear location-scale model _Yt_ ¼ _X_[0] _t[ξ]_ 0[þð] _[X]_[0] _t_[f][0][Þ] _[ε][t]_[, with ] _[ε][t ]_[an iid in-] novation independent of f _Xt; Xt −_ 1 _;_ ...g, such that _η_ 0ð _u_ Þ ¼ _ξ_ 0 þ _Fε[−]_[1][ð] _[u]_[Þ][f][0][.] Finally, we can decompose the conditional mean into the LTE, IQE, and RTE: 

**==> picture [267 x 13] intentionally omitted <==**

by property of the conditional expectation. Moreover, in a linear model we find the same relation between the LTE, IQE, and RTE parameters and the conditional mean parameters: 

**==> picture [262 x 13] intentionally omitted <==**

where _β_[ð] 0 _[M]_[Þ] is defined as the parameter vector of the conditional mean, that is _Et_ ½ _Yt_ �¼ _X_[0] _t[β]_[ð] 0 _[M]_[Þ] , and which can be estimated by OLS. Equations (3) and (4) provide conditions that we can easily use to study heterogeneity in the linear model of Example 2. Moreover, by deriving the joint distribution of estimators of the LTE, IQE, and RTE coefficients, we can easily test hypotheses of heterogeneity and the contribution of different interquantile intervals to the conditional mean parameters. We derive a test of heterogeneity in Section 3. 

## **2 Estimation and Inference** 

In this section, we first derive inference results for the weighted LTE estimator to simplify the exposition and provide efficiency results. We then generalize these results to the joint estimation of the LTE, IQE, and RTE. Subsequently, we propose an efficient weighting 

**6** _Journal of Financial Econometrics_ 

and, finally, compare the efficiency of our LTE estimator to recently introduced M-estimators. In the Supplementary Material, we extend the joint CLT in Theorem 3 to the case of dependent f _Ut_ g in Supplementary Section S5.4 with inference based on a HAC-estimator of the asymptotic covariance matrix. 

## 2.1 Estimation and Inference for the LTE Model 

To estimate the parameters of the LTE model, we use a two-stage estimation procedure in which we first estimate the parameters of the corresponding quantile model. To that end, we first discuss a weighted nonlinear quantile regression estimator of _ν_ 0ð _α_ Þ, denoted _ν_ ^ _T_ ð _α_ Þ. The estimator is given by 

**==> picture [234 x 19] intentionally omitted <==**

**==> picture [179 x 14] intentionally omitted <==**

**==> picture [170 x 17] intentionally omitted <==**

^ and _k_[^] _t_ ð _α_ Þ :¼ _kt_ ð _κ T_ ð _α_ ÞÞ is a weight function evaluated at a (pre-estimated) parameter vector _κ_ ^ _T_ ð _α_ Þ which converges in probability to some true parameter vector _κ_ 0. Moreover, _kt_ ð _κ_ ð _α_ ÞÞ ¼ _k_ ð _Xt; κ_ ð _α_ ÞÞ. Of course, fixing _k_[^] _t_ ¼ 1 results in the standard quantile regression estimator. 

The LTE estimator we propose is new, and so we elaborate on its construction. Whenever possible, we abstain from reference to the quantile level _α_ for notational conve^ nience. We also use the simplified notation _ν_ 0 ¼ _ν_ 0ð _α_ Þ, and _νT_ ¼ ^ _νT_ ð _α_ Þ in the remainder of this section. If the quantile regression estimator is consistent, the LTE estimator minimizes (asymptotically) the following weighted nonlinear least-squares problem: 

**==> picture [92 x 13] intentionally omitted <==**

where _g_ 0 _;t_ ð _β_ Þ ¼ _gt_ ð _β; ν_ 0Þ, 

**==> picture [203 x 20] intentionally omitted <==**

and _w_ 0 _;t_ ¼ _wt_ ð _ω_ 0Þ, denotes some weight function evaluated at the parameter vector _ω_ 0, with _wt_ ð _ω_ Þ ¼ _w_ ð _Xt; ω_ Þ. 

We specifically choose the function _g_ 0 _;t_ to define the prediction error, since, by Equation (1), 

**==> picture [217 x 14] intentionally omitted <==**

and because it makes the LTE estimation _locally robust_ to the quantile estimation, such that the utilization of the quantile parameter estimator _ν_ ^ _T_ in Equation (7) has no effect on the asymptotic covariance matrix of the LTE parameter estimator _β_[^][ð] _T[L]_[Þ][(see ][Chernozhukov ] et al. 2016 for an elaboration on local robustness). The local robustness follows from an orthogonal moment property: the gradient r _νEt_ ½ _gt_ ð _β_[ð] 0 _[L]_[Þ] _[;][ν]_[Þ�][takes value zero when evalu-] ated at _ν_ ¼ _ν_ 0. Here and in the following, we define the gradient to be a column vector. 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **7** 

The LTE estimator is then given by 

**==> picture [227 x 20] intentionally omitted <==**

with _R_[^] _T_ ð _β_ Þ :¼ _T_ 1 P _Tt_ ¼1 _[w]_[^] _[t][g]_[^][2] _t_[ð] _[β]_[Þ][, and where ] _[g]_[^] _t_[ð] _[β]_[Þ ¼] _[ g][t]_[ð] _[β][;][ν]_[^] _[T]_[Þ][, ] _[w]_[^] _[t]_[ ¼] _[ w][t]_[ð] _[ω]_[^] _[T]_[Þ][, with ] _[ω]_[^] _[T ]_[some ] (potentially pre-estimated) parameter vector. Notice that the LTE estimator requires as inputs _ν_ ^ _T_ and _ω_ ^ _T_ . Fixing _w_ ^ _t_ ¼ 1 results in a nonweighted LTE estimator. We provide an efficient weight specification and estimator in Section 2.2. 

The function _gt_ ð�Þ is well-studied in the (semiparametric) expected shortfall literature, as it is an _identification_ function of the FZ family of joint strictly consistent loss functions of Value-at-Risk and expected shortfall as introduced in Fissler and Ziegel (2016), also see Emmer et al. (2015). By identification function we mean that its conditional expectation is (uniquely) zero, that is _Et_ ½ _gt_ ð _β_[ð] _[L]_[Þ] _; ν_ Þ�¼ 0, at the values ð _β_[ð] 0 _[L]_[Þ] 0 _; ν_ 00Þ[0] , the values that minimize the conditional expectation of any (strictly) consistent loss function that is a member of the FZ family (Nolde and Ziegel 2017). For more on strict consistency of scoring/loss functions see, for example, Gneiting and Raftery (2007). 

We now state the conditions under which we derive asymptotic properties of the LTE estimator _β_[^][ð] _T[L]_[Þ][. Condition P requires consistent estimation or knowledge of the ] weight parameters. 

**==> picture [170 x 13] intentionally omitted <==**

This condition is clearly satisfied for unweighted quantile regression and LTE estimators, fixing _kt_ ¼ 1 and _wt_ ¼ 1. In Section 2.2 we provide an efficient weight specification for the LTE estimator together with a consistent estimator, such that Condition P.(ii) is satisfied for the efficiently weighted estimator as well. 

Condition F1 imposes that the model _st_ ð _β_ Þ is sufficiently varying over _B_ . In linear models, it suffices that _E_ ½ _XtX_[0] _t_[�][is full rank. In nonlinear models, a similar uniform full-rank ] condition on _E_ ½r _βst_ ð _β_ Þðr _βst_ ð _β_ ÞÞ[0] � often suffices. It also requires the weights to be wellbehaved, for example (almost sure) strict positivity of the weight function at the true parameters. Finally, asking for _ft_ to be bounded from above is standard in the literature (see, e.g., Weiss 1991 or Chernozhukov and Hansen 2006). We impose strict positivity on the density for the identification of the quantiles. 

**Condition F1.** It holds that _ν_ 0 2 _B_ and _β_[ð] 0 _[L]_[Þ] 2 _B_ , with B a compact subset of finitedimensional Euclidean space, and the function _st_ ð _β_ Þ is (a.s.) continuously differentiable on B, with gradient r _βst_ ð _β_ Þ. Moreover, _st_ ð _β_[ð] 0 _[L]_[Þ][Þ 6¼] _[ s][t]_[ð] _[β]_[Þ][ (a.s.), for all ] _β_ 2 _B_ n _β_[ð] 0 _[L]_[Þ][, and ] _[s][t]_[ð] _[ν]_[0][Þ 6¼] _[ s][t]_[ð] _[β]_[Þ][ (a.s.), for all ] _[β]_[ 2] _[ B]_[ n] _[ ν]_[0][. ] 

Moreover, _ω_ 0 2 Ω, and the weight function _wt_ ð _ω_ Þ is (a.s.) continuously differentiable on Ω, with gradient r _ωwt_ ð _ω_ Þ, and _wt_ ð _ω_ 0Þ _>_ 0 (a.s.). _κ_ 0 2 _K_ , and the weight function _kt_ ð _κ_ Þ is (a.s.) continuously differentiable on K, with gradient r _κkt_ ð _κ_ Þ. Moreover, _kt_ ð _κ_ 0ð _α_ ÞÞ _>_ 0 (a.s.). 

Finally, _Ft_ ð _y_ Þ defined in Equation (1) is continuously differentiable with density _ft_ ð _y_ Þ that satisfies (a.s.) 0 _< ft_ ð _Ft[−]_[1] ð _α_ ÞÞ, for all _α_ 2 ð0 _;_ 1Þ, and sup _y_ 2Y _ft_ ð _y_ Þ _<_[�] _f_ . 

Condition F2 imposes additional structure on _st_ ð _β_ Þ, which is used to establish asymptotic normality of the LTE estimator. 

**8** _Journal of Financial Econometrics_ 

**Condition F2.** The function _st_ ð _β_ Þ is twice continuously differentiable w.r.t _β_ (a.s.), with Hessian matrix r[2] _β[s][t]_[ð] _[β]_[Þ][, and ] _[E]_[½r] _[β][s][t]_[ð] _[β]_ 0[ð] _[L]_[Þ][Þðr] _[β][s][t]_[ð] _[β]_[ð] 0 _[L]_[Þ][ÞÞ][0][�][is positive definite. ] 

Conditions M1 and M2 impose moment conditions on the random variable _Yt_ , the random functions _st_ ð _β_ Þ, _wt_ ð _ω_ Þ, _kt_ ð _κ_ Þ, and their gradients, and the Hessian of _st_ ð _β_ Þ. We impose Condition M1 to establish consistency of the estimator and Condition M2 is additionally imposed to obtain asymptotic normality. Let us define j �j as the matrix norm j _A_ j ¼ fi fi fi fi fi fi fi fi fi fi f ptraceð _A_[0] _A_ Þ for any matrix _A_ , and ∥ _A_ ∥ _q_ the _L[q ]_ norm, that is ð _E_ j _A_ j _[q]_ Þ[1] _[=][q ]_ for _q_ 2 ½1 _;_ 1�Þ and the essential supremum of j _A_ j for _q_ ¼ 1. 

**Condition M1.** The random functions _Fs_ ð�Þ, _F_ r _s_ ð�Þ, _Fk_ ð�Þ, _F_ r _k_ ð�Þ, _Fw_ ð�Þ, and _F_ r _w_ ð�Þ exist, with (a.s.) j _st_ ð _β_ Þj ≤ _Fs_ ð _Xt_ Þ, j _kt_ ð _κ_ Þj ≤ _Fk_ ð _Xt_ Þ, j _wt_ ð _ω_ Þj ≤ _Fw_ ð _Xt_ Þ, and jr _βst_ ð _β_ Þj ≤ _F_ r _s_ ð _Xt_ Þ, jr _κkt_ ð _κ_ Þj ≤ _F_ r _k_ ð _Xt_ Þ, jr _ωwt_ ð _ω_ Þj ≤ _F_ r _w_ ð _Xt_ Þ, for all _β_ 2 _B_ , _κ_ 2 _K_ , and _ω_ 2 Ω. For some finite constant Δ _>_ 0, and constants _pw; pg_ 2 ½1 _;_ 1�, with _p_ 1 _w_[þ] _p_ 2 _g_[¼][ 1, it holds  ] 

max�∥ _Fs_ ð _Xt_ Þ∥ _pg ;_ ∥ _F_ r _s_ ð _Xt_ Þ∥ _pg ;_ ∥ _Fk_ ð _Xt_ Þ∥ _pw ;_ ∥ _F_ r _k_ ð _Xt_ Þ∥ _pw ;_ ∥ _Fw_ ð _Xt_ Þ∥ _pw ;_ ∥ _F_ r _w_ ð _Xt_ Þ∥ _pw ;_ ∥ _Yt_ ∥ _pg_ � _<_ Δ _:_ **Condition M2.** Some random function _F_ rr _s_ ð _Xt_ Þ exists, with jr[2] _β[s][t]_[ð] _[β]_[Þj][≤] _[F]_[rr] _[s]_[ð] _[X][t]_[Þ][ (a.s.), ] for all _β_ 2 _B_ . Moreover, 

max�∥ _Fs_ ð _Xt_ Þ∥2 _rpg ;_ ∥ _F_ r _s_ ð _Xt_ Þ∥2 _rpg ;_ ∥ _Fw_ ð _Xt_ Þ∥2 _rpw ;_ ∥ _F_ r _w_ ð _Xt_ Þ∥2 _rpw ;_ ∥ _Yt_ ∥2 _rpg ;_ ∥ _F_ rr _s_ ð _Xt_ Þ∥2 _rpg_ � _<_ Δ _:_ Together, these conditions require the 2 _pgr_ -order moments to be bounded for j _st_ ð _β_ Þj, jr _βst_ ð _β_ Þj, and jr[2] _β[s][t]_[ð] _[β]_[Þj][ uniformly on ] _[B]_[, and similarly for ][j] _[Y][t]_[j][, with the constant ] _[r][>]_[1 set in ] Condition S. The value of _pg_ depends on whether j _wt_ ð _ω_ Þj and jr _ωwt_ ð _ω_ Þj are uniformly bounded. If this is the case, then _pg_ ¼ 2 and we require 4 _r_ -order moments to be bounded. If not, then the condition would be satisfied under 6 _r_ -order bounded moments, since we can choose _pg_ ¼ _pw_ ¼ 3. 

We are now ready to state the first result which concerns the consistency of the quantile and LTE estimator and the asymptotic normality of the LTE estimator. 

**Theorem 1.** _Under Conditions Y, S, P, F1, and M1 it follows that_ 

**==> picture [98 x 14] intentionally omitted <==**

_Additionally, under Conditions F2 and M2, it follows that_ 

**==> picture [252 x 48] intentionally omitted <==**

**==> picture [177 x 19] intentionally omitted <==**

_Proof._ The proof relies on the following steps. First, we show the consistency of the (weighted) quantile regression estimator _ν_ ^ _T_ by application of Lemma 2.1 of Newey and McFadden (1994). This lemma requires a uniform LLN on the estimated objective function, which we obtain using Theorem 3 of Andrews (1992). Second, 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **9** 

we show the consistency of the (weighted) LTE _β_[^][ð] _T[L]_[Þ][estimator using similar steps. ] Finally, to establish the asymptotic normality result, we first expand _E_ ½ ^ _wtg_ ^ _t_ ð _β_[^] _T_ Þr _βst_ ð _β_[^] _T_ Þ� about _β_ 0, and apply the mean-value theorem and a functional CLT for _β_ -mixing sequences (Theorem 1 in Doukhan et al. 1995). See Supplementary Section S4 of the Supplementary Material for a full proof.                w 

We remark that the asymptotic covariance matrix does not contain additional terms related to plugging-in the pre-estimated quantile parameters _ν_ ^ _T_ . This property follows precisely due to the local robustness of the LTE estimation to the quantile parameter vector, as discussed in the preceding. Moreover, even though the data fð _Yt; X_[0] _t_[Þ][0][g][are allowed to be ] autocorrelated, Σ0 does not contain autocorrelation terms of the form 

**==> picture [226 x 15] intentionally omitted <==**

for lags _j_ such that j _j_ j ≥ 1. This follows from the error sequence f _Ut_ g being independent and _Ut_ being independent of f _Xt; Xt −_ 1 _;_ ...g, for all _t_ , under Condition S. We relax the independence condition in Supplementary Section S5.4 in the Supplementary Material. 

## 2.2 Efficient Weights 

We obtain an efficiently weighted LTE estimator by appealing to the theory in Bates and White (1993). The results extend directly to the IQE and RTE estimators. We provide the efficient weight specifications in for the IQE and RTE in Supplementary Section S5.1 of the Supplementary Material and only study the efficient weighting for the LTE here. 

We first introduce some additional notation to make the choice of weighting specific. Let w ¼ fw _t_ g _[T] t_ ¼1[be some weight sequence, where ][w] _[t]_[ ¼] _[ w][t]_[ð] _[ω]_[^] _[T]_[Þ][, for some weight function ] _[w][t]_[ð�Þ] and a (potentially estimated) weight parameter _ω_ ^ _T_ , that converges in probability to some true parameter _ω_ 0 if estimated. Define _T_ ^ 1 _β_[ð] _T[L]_[Þ][ð][w][Þ][ :][¼][ argmin] _β_ 2 _B T_ X _t_ ¼1 w _tgt_[ð] _[L]_[Þ] ð _β;_ ^ _νT_ Þ[2] _:_ We consider the class of weighted estimator sequences CðWÞ :¼ nf _β_[^][ð] _T[L]_[Þ][ð][w][Þg][ :][ w][ 2][ W] o, where W contains all w that satisfy the conditions imposed in Theorem 1. Theorem 2 below shows that an efficient weight sequence exists in this class, and that an estimated counterpart reaches the same efficiency bound if the true weight parameter is consistently estimated (Condition P). 

We denote the true efficient weight sequence by w~ 0 and define it as follows: 

**==> picture [59 x 11] intentionally omitted <==**

where 

**==> picture [131 x 19] intentionally omitted <==**

for _ω_ ¼ ð _λ_[0] _;_ vecðΩÞ[0] Þ[0] , and we recall the definition of _h_ ð�Þ in Equation (2). Moreover, the true weight parameter _ω_ ~ 0 takes value _ω_ ~ 0 ¼ ð _λ_[0] 0 _[;]_[vec][ð][Ω][0][Þ][0][Þ][0][, where ] 

**10** _Journal of Financial Econometrics_ 

**==> picture [301 x 114] intentionally omitted <==**

The estimated counterpart of this weight sequence is denoted w~ , with 

**==> picture [56 x 12] intentionally omitted <==**

where _ω_ ~[^] _T_ is assumed to be consistent for _ω_ ~ 0. In the final parts of this section we provide such an estimator. 

**Theorem 2.** _For any probability measure P_[0] 2 P _, with_ P _the family of all datagenerating mechanisms that satisfy the conditions of Theorem 1, it follows that_ f _β_[^][ð] _T[L]_[Þ][ð][w][~][0][Þg] _[ and ]_[f] _[β]_[^][ð] _T[L]_[Þ][ð][w][~][Þg] _[ have minimum asymptotic variance in ]_[Cð][W][Þ][. ] 

_Proof._ We first establish that CðWÞ is an indexed class of sequences of estimators as in Definition 2.1 in Bates and White (1993) and a Regular Consistent Asymptotically Normal Indexed class as in their Definition 2.2. Noting that f _β_[^][ð] _T[L]_[Þ][ð][w][~][0][Þg][ and ][f] _[β]_[^][ð] _T[L]_[Þ][ð][w][~][Þg][ are members of ][Cð][w][Þ][, we apply their Theorem 2.6 to ] establish they have the minimum asymptotic variance property defined in their Definition 2.5. See Supplementary Section S4 of the Supplementary Material for a full proof.                                                                                                                            w The minimum asymptotic variance property is formally defined in Definition 2.5 in Bates and White (1993) and implies the difference between the asymptotic covariance mafi **f**[�] ^ fi **f** trices of p _T β_[ð] _T[L]_[Þ][ð][w][Þ] _[−β]_[ð] 0 _[L]_[Þ] and p _T_ ð _β_[^][ð] _T[L]_[Þ][ð][w][~][Þ] _[−β]_[ð] 0 _[L]_[Þ][Þ][ is positive semidefinite, for all ][w][ 2][ W][.] � efficient weight equals the inverse of the conditional variance of the prediction error. The efficiency result pivots on the property _w_ ~ _t_ ð _ω_ ~ 0Þ ¼ 1 _=E_[0] _t_[½] _[g]_[2] 0 _;t_[ð] _[β]_[ð] 0 _[L]_[Þ][Þ�][(a.s.), such that the ] Therefore, the efficiently weighted estimator of the conditional LTE is analogous to the GLS estimator of the conditional mean, which is efficient in that case. From inspection of the proof, we observe that weights that are proportional to _w_ ~ _t_ ð _ω_ ~ 0Þ are efficient weights too, as well as their estimated counterpart. As a consistent estimator of the weight parameters, we choose _ω_ ~[^] _T_ ¼ ð _λ_[^][0] _T[;]_[vec][ð][ ^][Ω][ð] _T[L]_[Þ][ÞÞ][, where ] 

**==> picture [198 x 33] intentionally omitted <==**

_k_ with _uk_ ¼ _α KT_ ~~[,]~~[ the function ] _[f]_[ ð] _[L]_[Þ][ð�Þ][defined in ][Equation (8)][, and ] _[K][T]_[!][1][as ] _[T]_[!][1][. The ] vectors _η_ ^ _T_ ð _α_ Þ and _η_ ^[ð] _T[L]_[Þ][are elements of the estimators ] _[ν]_[^] _[T ]_[and ] _[β]_[^][ð] _T[L]_[Þ][, whereas the estimators ] _η_ ^ _T_ ð _uk_ Þ are elements of the estimator _ν_ ^ _T_ ð _uk_ Þ, for _αk_ ¼ _uk_ , with some abuse of notation. The 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **11** 

estimator _λ_[^] _T_ can be selected as the corresponding elements of _ν_ ^ _T_ ð _α_ Þ or _β_[^][ð] _T[L]_[Þ][and is consis-] tent for _λ_ 0 by Theorem 1. Moreover, the consistency of vecðΩ[^][ð] _T[L]_[Þ][Þ][is established in ] Supplementary Section S5.2 of the Supplementary Material, such that these parameters are ~ _p_ ~ consistent, that is _ω_[^] _T_ ! _ω_ 0, under certain conditions on _η_ 0ð�Þ. In the proof, we first establish uniform consistency of the quantile regression estimator _η_ ^ð _α_ Þ and then appeal to the Continuous Mapping Theorem. 

For the nonlinear location-scale model in Example 1, we can design efficient weights in terms of any two conditional quantiles. 

**==> picture [340 x 75] intentionally omitted <==**

Hence, _w_ ~ _t_ ð _ω_ ~ 0Þ ¼ ðΣ0 _hσ_ ð _Xt;_ f0Þ[2] Þ _[−]_[1 ] is proportional to _w_ � _t_ ð _ω_ � 0Þ ¼ ð _st_ ð _ν_ 0ð _α_[00] ÞÞ _− st_ ð _ν_ 0ð _α_[000] ÞÞ _[−]_[2 ] ¼ ðð _Fε[−]_[1][ð] _[α]_[00][Þ] _[−][F] ε[−]_[1][ð] _[α]_[000][ÞÞ][2] _[h][σ]_[ð] _[X][t][;]_[f][0][Þ][2][Þ] _[−]_[1 ][for any ] _[α]_[00] _[;][α]_[000][ 2 ð][0] _[;]_[1][Þ][, ] _[α]_[00][ 6¼] _[ α]_[000][. It follows that the es-] timated weights _w_ � _t_ ð _ω_ �[^] _T_ Þ ¼ ð _st_ ð _ν_ ^ _T_ ð _α_[00] ÞÞ _− st_ ð _ν_ ^ _T_ ð _α_[000] ÞÞÞ _[−]_[2 ] are efficient for any _α_ 2 ð0 _;_ 1Þ. The same weights are efficient for the IQE and RTE estimators. In this case, Condition P follows by Theorem 3. 

2.3 Comparison to LTE Estimators Based on the FZ Family of Loss Functions 

Here we show our weighted LTE estimator is also efficient amongst the class of the recently introduced M-estimators of the LTE based on the FZ family of loss functions, for example, Patton et al. (2019) and Dimitriadis and Bayer (2019). Fissler and Ziegel (2016) introduce the FZ family of loss functions that are jointly strictly consistent for the quantile and LTE at quantile level _α_ . The family consists of the functions 

**==> picture [356 x 23] intentionally omitted <==**

for any weakly increasing function _G_ 1ð�Þ, strictly increasing and strictly positive _G_ 2ð�Þ, and G[0] 2[¼] _[ G]_[2][.] 

Under appropriate regularity conditions, including unique conditional quantiles, the _strict consistency_ property follows, that is 

**==> picture [206 x 14] intentionally omitted <==**

> 0 ~ ð _L_ Þ (a.s.) for all ð _β_[~] _; ν_ Þ 2 _B_ × _B_ n ð _β_ 0 _[;][ν]_[0][Þ][. This strict consistency property naturally leads to an ] M-estimator. Patton et al. (2019) and Dimitriadis and Bayer (2019) derive such estimators: 

**==> picture [289 x 27] intentionally omitted <==**

**12** _Journal of Financial Econometrics_ 

Under appropriate regularity conditions, which include (a.s.) the twice continuous differentiability of _G_ 2ð�Þ, with derivative r _G_ 2ð�Þ, it can be shown that the FZ-estimator of the LTE is asymptotically distributed 

**==> picture [214 x 22] intentionally omitted <==**

with _M_[ð] 0 _[FZ]_[Þ] ¼ _E_ ½r _G_ 2ð _st_ ð _β_[ð] 0 _[L]_[Þ][ÞÞr] _[β][s][t]_[ð] _[β]_[ð] 0 _[L]_[Þ][Þðr] _[β][s][t]_[ð] _[β]_[ð] 0 _[L]_[Þ][ÞÞ][0][�][and ] _[S]_[ð] 0 _[FZ]_[Þ] ¼ _E_ ½½r _G_ 2ð _st_ ð _β_[ð] 0 _[L]_[Þ][ÞÞ�][2][ ×] _[g] t_[ð] _[L]_[Þ] ð _β_[ð] 0 _[L]_[Þ] _[;][ν]_[0][Þ][2][r] _[β][s][t]_[ð] _[β]_[ð] 0 _[L]_[Þ][Þðr] _[β][s][t]_[ð] _[β]_[ð] 0 _[L]_[Þ][ÞÞ][0][�][.] There always exists a (nonefficient) weighted LTE estimator which has the same asymptotic covariance matrix as the M-estimator in Equation (9), for each member of the FZ family of loss functions. Indeed, we can find a weighted estimator that is asymptotically equivalently distributed by choosing weight function _w_ 0 _;t_ ¼ r _G_ 2ð _st_ ð _β_[ð] 0 _[L]_[Þ][ÞÞ][, or a consistently ] estimated counterpart. As such, the efficiently weighted LTE estimator is also efficient compared to the family of M-estimators. 

## 2.4 Joint Inference on LTEs, IQEs, and RTEs 

We now propose estimators and derive joint inference results for estimators of the model parameters for the LTE model, the IQE model, and the RTE model. We also propose a consistent estimator of the asymptotic covariance matrix. Inference on the parameters of other combinations of models follows similarly. Recall that we consider two quantile levels _α; α_[0] 2 ð0 _;_ 1Þ and the LTE, IQE, and RTE as given in Equation (1). 

We must introduce two additional identification functions for the IQE and RTE to define the estimators, and propose some new notation and renaming to distinguish between the models. The IQE and RTE estimators are based on counterparts to the identification function _g_ 0 _;t_ of the LTE model introduced in the previous section. Indeed, let us consider the functions 

**==> picture [292 x 72] intentionally omitted <==**

These functions share the same local-robustness property as enjoyed by _gt_ ð _β; ν_ Þ. Moreover, we denote their values at the population and estimated quantiles as follows, 

**==> picture [126 x 78] intentionally omitted <==**

^ ^ Finally, upon renaming the LTE case to for clarity, the estimators for the LTE, IQE, and RTE models are given by _g_[ð] 0 _[L] ;t_[Þ][ð] _[β]_[Þ ¼] _[ g]_[0] _[;][t]_[ð] _[β]_[Þ][, ] _[g]_[^] _t_[ð] _[L]_[Þ] ð _β_ Þ ¼ ^ _gt_ ð _β_ Þ, and _ω_[ð] _T[L]_[Þ] ¼ _ωT_ , 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **13** 

**==> picture [267 x 27] intentionally omitted <==**

^ for _m_ 2 f _L; I; R_ g, respectively. Clearly, setting _wt ω_[ð] _T[m]_[Þ] ¼ 1 results in the unweighted esti� � mator. Efficient weight specifications are provided in Section 2.2. ð _m_ Þ fFor linear models the estimators can be calculated using OLS, where we regress i fi fi fi fi fi fi fi f fi fi fi fi fi fi fi fi f _Y_[~] _t_ :¼ q _wt_ ð _ω_ ^[ð] _T[m]_[Þ][Þ] f _st_ ð _β_ Þ _− g_ ^ _t_[ð] _[m]_[Þ] ð _β_ Þg on _X_[~] _t_ :¼ q _wt_ ð _ω_ ^[ð] _T[m]_[Þ][Þ] _Xt_ for IQE estimation. Note that _Y_[~] ð _t m_ Þ does not depend on _β_ due to the subtraction of terms. 

We are interested in inference on the joint parameter vector 

**==> picture [92 x 18] intentionally omitted <==**

using the joint estimator 

**==> picture [96 x 19] intentionally omitted <==**

In the following result we provide a CLT for the joint estimator, but first we provide a consistent asymptotic covariance matrix estimator for it. Let _M_[~] _T_ be defined as the diagonal block matrix (with zero off-diagonal blocks) 

**==> picture [119 x 55] intentionally omitted <==**

where _M_[^][ð] _T[m]_[Þ] :¼ _T_ 1 P _Tt_ ¼1 _[w][t]_[ð] _[ω]_[^][ð] _T[m]_[Þ][Þr] _[β][s][t]_[ð] _[β]_[^][ð] _T[m]_[Þ][Þðr] _[β][s][t]_[ð] _[β]_[^][ð] _T[m]_[Þ][ÞÞ][0][, for ] _[m]_[ 2 f] _[L][;][I][;][R]_[g][. Moreover, let ][~] _[S][T ]_ be defined as the matrix[~] _ST_ :¼ _T_ 1 P _Tt_ ¼1 _[h]_[~] _[t][h]_[~] 0 _t[;]_[ with ] 

**==> picture [153 x 55] intentionally omitted <==**

~ _S_ This covariance matrix estimator is consistent for the true asymptotic covariance matrix 0, which is defined similarly to _S_ ~ _T_ , but with all estimated parameters replaced by their true counterparts (see Supplementary Section S4 for a more elaborate treatment). 

**Theorem 3.** _Under the conditions of Theorem 1 (with all conditions on β_[ð] 0 _[L]_[Þ] _[holding ] for β_[ð] 0 _[I]_[Þ] _[and ][β]_[ð] 0 _[R]_[Þ] _[, all conditions on ][ν]_[0][ ¼] _[ ν]_[0][ð] _[α]_[Þ] _[ holding for ][ν]_[0][ð] _[α]_[0][Þ] _[, and similarly for ] the respective weight parameters) and with asymptotic covariance matrix S_[~] 0 _being positive definite, it follows that_ 

**14** _Journal of Financial Econometrics_ 

**==> picture [168 x 18] intentionally omitted <==**

fi **f** _Proof._ First, we note that the multivariate asymptotic normality of p _T_ ð _β_[�] _T − β_[�] 0Þ follows from similar steps to those in the proof of Theorem 1, given the similarity of the functions _gt_[ð] _[L]_[Þ] , _gt_[ð] _[I]_[Þ][and ] _[g]_[ð] _t[M]_[Þ] , and the fact that all consistency results may be shown pointwise. Second, _−_ 1 _−_ 1 the consistency of the estimated asymptotic covariance matrix _M_[~] _T_[~] _[S][T][M]_[~] _T_[and its inverse ] follow by application of the uniform LLN in Andrews (1992) and the Continuous Mapping Theorem. See Supplementary Section S4 of the Supplementary Material for a full proof.                                                                                                                                               w 

In Supplementary Section S5.4 we additionally provide a HAC estimator of the asymptotic covariance matrix, which replaces _S_[~] _T_ by 

**==> picture [183 x 27] intentionally omitted <==**

where Γ[^] _T_ ð _j_ Þ :¼ _T_ 1 P _Tt_ ¼ _j_ þ 1 _[h]_[~] _[t][h]_[~] 0 _t − j_[, ] _[m][T]_[!][1][, ] _[m][t]_[ ¼] _[ o]_[ð] _[T]_[1] _[=]_[4][Þ][, and ] _[z]_[ð] _[j][;][m]_[Þ][denotes some weight ] function such that _z_ ð _j; m_ Þ ! 1 as _m_ ! 1. The HAC inference result in Theorem S1 in Supplementary Section S5.4 remains valid under a weakening of the iid assumption on _Ut_ , allowing _Ut_ to satisfy a mixing condition instead. 

## **3 A Test of Parameter Heterogeneity** 

The results in Theorem 3 enable us to perform tests on the model parameters. Consider the null hypothesis 

**==> picture [210 x 11] intentionally omitted <==**

for some full rank matrix _R_ and vector _r_ . 

Of prime concern are tests of heterogeneity. For instance, the null hypothesis that the _l_ th elements of each of the parameter vectors _β_[ð] 0 _[L]_[Þ][, ] _[β]_[ð] 0 _[I]_[Þ][, and ] _[β]_[ð] 0 _[R]_[Þ][are equal-valued, ] 

**==> picture [70 x 15] intentionally omitted <==**

can be rewritten as the pair of equations _β_[ð] 0 _[L] ;l_[Þ] _[−β]_[ð] 0 _[I] ;_[Þ] _l_[¼][ 0 and ] _[β]_[ð] 0 _[I] ;_[Þ] _l[−β]_[ð] 0 _[R] ;l_[Þ][¼][ 0, such that it can ] be written as a null hypothesis in the form of Equation (11). A level _τ_ test can be performed by rejecting the null hypothesis _H_ 0 if the test statistic 

**==> picture [290 x 19] intentionally omitted <==**

exceeds the critical value denoting the _χ_[2 ] distribution with _χ_[2] _dr;_ 1 _−τ_[, where ] _dr_ degrees of freedom. _[χ]_[2] _dr;_ 1 _−τ_[is the ][ð][1] _[−τ]_[Þ][-quantile of the ] _[χ]_[2] _dr_[distribution, ] 

**Corollary 1** _Under the Conditions of Theorem 3_ , _WT_ ! _d χ_ 2 _dr[under H]_[0][. ] 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **15** 

_−_ 1 _−_ 1 _Proof._ Denote Σ[^] _W;T_ :¼ _RM_[~] _T_[~] _[S][T][M]_[~] _T[R]_[0][. By the Continuous Mapping Theorem, ] pf _T_ i **f** Σ^ _−W_ 1 _;T=_ 2 _[R]_[ð] _[β]_[�] _[T][−]_[�] _[β]_[0][Þ!] _d N_ ð0 _; I_ Þ, with the matrix Σ^ _W;T_ invertible under _R_ having full rank. The result follows.                                                                                                                         w 

## **4 Simulation Study** 

We conduct a Monte Carlo experiment that is close in design to our empirical application to study the small sample properties of our two-stage estimator. We will consider LTEs at tail quantile levels _α_ ¼ 2 _:_ 5%, 5%, 10%, and 25% and IQEs between 10% and 10% þ _α_ , respectively. Choosing these statistics allows us to study the behavior of our estimator in the tails and close to the tails. 

We compare the two-stage estimator of the LTEs with the _FZ_ 0 estimator described in Section 2.3, for all quantile levels except _α_ ¼ 25%. At the latter level, the quantile is not strictly negative for all specifications of our DGP, such that the results in Patton et al. (2019) do not apply. 

We study sample sizes _T_ ¼ 250, 1,000, and 2,500, such that we can draw conclusions for relatively small data sets like monthly macroeconomic data collected since the 2000s, and larger data sets like daily financial returns collected over a period of 10years. Results are based on Monte Carlo experiments with 5,000 iterations. 

We also consider a simulation experiment that requires a HAC estimator of the asymptotic covariance matrix in Supplementary Section S5.4 of the Supplementary Material. Finally, we consider a nonlinear AR(1) DGP in Supplementary Section S3 of the Supplementary Material. 

## 4.1 Definition of the DGP 

We consider a DGP that allows for conditional heteroskedasticity and autocorrelated _Yt_ . It is defined as follows: 

**==> picture [309 x 85] intentionally omitted <==**

where _tμ_ denotes the standardized _t_ -distribution with _μ_ degrees of freedom and _e_ ¼ expð1Þ. 

The regressor _Wt_ is lognormal, with log _Wt_ being _AR_ ð1Þ with autoregressive coefficient _ϕ_ . We set f ¼ _ι_ , with _ι_ the vector of ones, such that _Yt_ has time-varying conditional volatility specified by _X_[0] _t[ι]_[. The value of ] _[c ]_[specified above ensures that ] _[cW][t ]_[has unit variance. We ] also set _ξ_ ¼ _ι_ , such that _Xt_ also has considerable influence on the conditional mean of _Yt_ . We draw log _W_ 0 from its respective invariant measure. 

In terms of autocorrelation, we choose _ϕ_ ¼ 0 _:_ 90. This allows for considerable autocorrelation in _Xt_ and _Yt_ . Finally, the error _εt_ is chosen standard normal or standardized _t_ -distributed with _μ_ degrees of freedom. We choose _μ_ ¼ 4 to cover cases with fat tails. We also consider truncated versions of these distributions. Given some nontruncated cdf _Fε_ ð _x_ Þ, the corresponding truncated cdf is given by _Fε_ ð _x_ j _lε_ ≤ _x_ ≤ _uε_ Þ ¼ _Fε_ ð _x_ Þ _− Fε_ ð _lε_ Þ _= Fε_ ð _uε_ Þ _− Fε_ ð _lε_ Þ , with trun� � � � cation interval ½ _lε; uε_ �. We choose _lε_ ¼ _− uε_ ¼ 20. Truncation is only required formally for the 

**16** _Journal of Financial Econometrics_ 

~ ~ estimated LTE weights _wt_ ð _ω_[^][ð] _T[L]_[Þ][Þ][to satisfy Condition P, and similarly for the respective RTE ] weights (see Supplementary Section S5.2 in the Supplementary Material). We note that the location-scale weights _w_ � _t_ ð _ω_ �[^] _T_ Þ do not require truncation. In practice, this truncation is of little consequence, as j _εt_ j _>_ 20 is a rare event for the _N_ ð0 _;_ 1Þ distribution and the _tμ_ distribution with _μ_ ¼ 4. 

Given the conditional mean and volatility depending on _Xt_ , the parameters of the quantile and IQE models will differ across quantile levels. For any two quantile levels _α_ and _α_[0] , such that 0 _< α < α_[0] _<_ 1, the DGP in Equation (13) implies the following values for the quantile, lower-quantile expectation, and IQE parameters: 

**==> picture [244 x 41] intentionally omitted <==**

**==> picture [253 x 18] intentionally omitted <==**

with _q_ ð _α_ Þ, _e_ ð _α_ Þ, and _i_ ð _α; α_[0] Þ denoting the unconditional inverse cdf evaluated at _α_ , the LTE at level _α_ , and the IQE between levels _α_ and _α_[0] , respectively, of the error _εt_ . 

For several cases we may obtain closed form expressions. If _εt_ is standard normal, we find, for any _α_ 2 ð0 _;_ 1Þ, _q_ ð _α_ Þ ¼ Φ _[−]_[1] ð _α_ Þ, Φ _[−]_[1] ð�Þ denoting the inverse standard normal cdf, _e_ ð _α_ Þ ¼ _−ϕ_ ðΦ _[−]_[1] ð _α_ ÞÞ _=α_ , with _ϕ_ ð�Þ denoting the standard normal pdf, and _i_ ð _α; α_[0] Þ ¼ _α_[0] 1 _−α_[ð] _[α]_[0] _[e]_[ð] _[α]_[0][Þ] _[−α][e]_[ð] _[α]_[ÞÞ][. We refer to Example 2.15 in ][McNeil et al. (2015)][if ] _[ε][t ]_[is ] _[t]_[- ] distributed. Finally, we may employ simulation to obtain values for the other distributions. 

We consider weighted and unweighted estimation. For this DGP the optimal weight function for the LTE and IQE estimation, for each _α_ , is given by the location-scale weights 

**==> picture [158 x 20] intentionally omitted <==**

for any two quantile levels _α_[0] and _α_[000] such that _α_[00] 6¼ _α_[000] . We choose _α_[00] ¼ 0 _:_ 40 and _α_[000] ¼ 0 _:_ 60. We use unweighted quantile estimation, that is _kt_ ð _κ_ 0Þ ¼ _κ_ 0 ¼ 1 for all _t_ . 

We also consider the general specification of the efficient LTE weights. For this DGP, these weights are defined as 

**==> picture [109 x 19] intentionally omitted <==**

with _ω_ ~[^][ð] _T[L]_[Þ] ¼ vecðΩ[^][ð] _T[L]_[Þ][Þ][, ][Ω][^][ð] _T[L]_[Þ] ¼ _f_[ð] _[L]_[Þ] � _η_ ^ _T_ ð _α_ Þ _; η_ ^[ð] _T[L]_[Þ] _[;] K_ 1 _T_ P _Kk_ ¼ _T_ 1 _[η]_[^] _[T]_[ð] _[u][k]_[Þð] _[η]_[^] _[T]_[ð] _[u][k]_[ÞÞ][0] �, _uk_ ¼ _α KkT_ ~~[,]~~[ the ] function _f_[ð] _[L]_[Þ] ð�Þ defined in Equation (8), and _KT_ ! 1 as _T_ ! 1. We set _KT_ ¼ _T_[1] _[=]_[3] . The general specification of the efficient IQE weights for this DGP is analogous, replacing _f_[ð] _[L]_[Þ] ð�Þ for _f_[ð] _[I]_[Þ] ð�Þ. 

Proposition 1 provides some parameterizations of the DGP in Equation (13) that are sufficient to satisfy the conditions of Theorem 3. We observe that the sufficient conditions for the weighted estimator are stronger for the degrees of freedom parameter _μ_ , if _ε_ is _t_ -distributed. This is due to an application of the Holder inequality in the proof of € Theorem 1 to the term 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **17** 

~ ~ j _wt_ ð _ω_ Þ _gt_ ð _β; ν_ Þr _βst_ ð _β_ Þ _− wt_ ð _ω_ Þ _gt_ ð _β_[~] _; ν_ Þr _βst_ ð _β_[~] Þj 

in order to show that it satisfies a Lipschitz condition. Such a condition may not be strictly necessary and we fix _μ_ ¼ 4 in the simulation exercise to show that the condition on _μ >_ 6 is indeed not necessary, as we observe that the weighted estimator generally performs better than the unweighted estimator (for which _μ >_ 4 suffices) in terms of bias, variance and coverage. 

- **Proposition 1.** _Let ξ and_ f _take values in compact subsets of_ R[2 ] _and_ R _>_ 0 × R ≥ 0 _, respectively, let_ j _ϕ_ j _<_ 1 _, and consider any_ ð _α; α_[0] Þ 2 ð0 _;_ 1Þ[2] , _α < α_[0] _. The following scenarios are sufficient for the Conditions of Theorem 3 to hold:_ 

- i) _the unweighted LTE, IQE, and RTE estimator, if εt is either iid tμ, with μ >_ 4, _N_ ð0 _;_ 1Þ _, truncated tμ, with μ >_ 0 _, or truncated N_ ð0 _;_ 1Þ _, with truncation to the interval_ ½ _lε; uε_ � _for any lε; uε_ 2 R, _lε < uε;_ 

- ii) _the weighted LTE, IQE, and RTE estimator with location-scale weights w_ � _t_ ð _ω_ �[^] _T_ Þ _, and the weighted IQE estimator with weights w_ ~ _t ω_ ^~[ð] _T[I]_[Þ] _, if εt is either iid tμ, with μ >_ 6, � � 

- _N_ ð0 _;_ 1Þ _, truncated tμ, with μ >_ 0 _, or truncated N_ ð0 _;_ 1Þ _, with truncation to the interval_ ½ _lε; uε_ � for any _lε; uε_ 2 R, _lε < uε_ ; 

iii) _the weighted LTE and RTE estimator with respective weights w_ ~ _t ω_ ^~[ð] _T[L]_[Þ] � � _and w_ ~ _t ω_ ^~[ð] _T[R]_[Þ] _, if εt is either iid truncated tμ, with μ >_ 0 _, or truncated N_ ð0 _;_ 1Þ _, with_ � � _truncation to the interval_ ½ _lε; uε_ � _for any lε; uε_ 2 R, _lε < uε_ . 

_Proof._ We show for each specification of the model and DGP that the sufficient conditions of Theorem 3 are satisfied. See Supplementary Section S5.3 of the Supplementary Material for a full proof.                                                                                                                               w 

## 4.2 Descriptive Statistics of Parameter Estimates 

The tables below provide results for the scenario where _Xt_ influences the mean and volatility of _Yt_ , _εt_ � _tμ_ with _μ_ ¼ 4, and for the choice of location-scale weights _w_ � _t_ ð _ω_ �[^] _T_ Þ. In the final paragraphs of this section, we discuss results for alternative settings, such as standard normal errors _εt_ , general efficient weights _w_ ~ _t_ ð _ω_ ~[^][ð] _T[L]_[Þ][Þ][and ] _[w]_[~] _[t]_[ð] _[ω]_[^~][ ð] _T[I]_[Þ][Þ][, and for truncated ] distributions. 

Table 1 provides descriptive statistics of the unweighted and weighted estimates of the LTE and IQE parameters for simulation studies with sample sizes _T_ ¼ 250, 1,000, and 2,500. We also estimate the LTE parameters using the FZ-estimator of Patton et al. (2019) as a benchmark. In particular, this is the FZ-estimator based on the zero-homogeneous member of the FZ family. 

We first discuss the parameter estimates of the LTEs, at quantiles levels _α_ ¼ 2 _:_ 5%, 5%, 10%, and 25%. Table entries in cursive formatting indicate that the entry contains the (shared) smallest bias (in absolute value) or standard deviation between LTE estimators or between IQE estimators. 

We observe that the bias and standard deviations in the estimates decrease with increasing _T_ , agreeing with the asymptotic theory that our estimator is consistent. Moreover, our weighted LTE estimator mostly has a smaller bias and standard deviation than its unweighted counterpart (except for _α_ ¼ 2 _:_ 5% and _T_ ¼ 250). We also notice a similar decrease in the bias and standard deviation as _α_ increases. 

To estimate the FZ-estimator of Patton et al. (2019), we use the estimation method described in their Appendix C, which is designed to reduce sensitivity to starting values. 

**18** _Journal of Financial Econometrics_ 

**Table 1.** Descriptive statistics of the two-stage estimator and benchmark in the simulation experiment. 

|**_T_**|**LTE (2-stage)**<br>**(unweighted)**<br>_β_ð**L**Þ<br>**1**<br>_β_ð**L**Þ<br>**2**|**LTE (2-stage)**<br>**(weighted)**<br>_β_ð**L**Þ<br>**1**<br>_β_ð**L**Þ<br>**2**|**LTE (FZ-est.)**<br>_β_ð**L**Þ<br>**1**<br>_β_ð**L**Þ<br>**2**|**IQE (2-stage)**<br>**(unweighted)**<br>_β_ð**I**Þ<br>**1**<br>_β_ð**I**Þ<br>**2**|**IQE (2-stage)**<br>**(weighted)**|
|---|---|---|---|---|---|
||||||_β_ð**I**Þ<br>**1**<br>_β_ð**I**Þ<br>**2**|
|_α_¼2_:_5%<br>250<br>mean<br>sd.<br>1,000<br>mean<br>sd.<br>2,500<br>mean<br>sd.<br>_α_¼5%<br>250<br>mean<br>sd.<br>1,000<br>mean<br>sd.<br>2,500<br>mean<br>sd.<br>_α_¼10%<br>250<br>mean<br>sd.<br>1,000<br>mean<br>sd.<br>2,500<br>mean<br>sd.<br>_α_¼25%<br>250<br>mean<br>sd.<br>1,000<br>mean<br>sd.<br>2,500<br>mean<br>sd.|_−_0.32<br>0.79<br>_1.21_<br>_1.76_<br>_−_0.17<br>0.31<br>0.89<br>1.37<br>_−_0.19<br>0.20<br>0.71<br>1.03<br>_−_0.18<br>0.39<br>0.89<br>1.46<br>_−_0.07<br>0.13<br>0.67<br>1.06<br>_−_0.04<br>0.07<br>0.51<br>0.77<br>_−_0.09<br>0.20<br>0.63<br>1.04<br>_−_0.04<br>0.07<br>0.46<br>0.70<br>_−_0.02<br>0.04<br>0.34<br>0.51<br>_−_0.03<br>0.08<br>0.39<br>0.63<br>_−0.01_<br>0.03<br>0.28<br>0.41<br>_−_0.01<br>_0.01_<br>0.19<br>0.28|_−_0.12<br>0.51<br>1.25<br>2.04<br>_−_0.04<br>0.13<br>_0.59_<br>_1.00_<br>_−_0.12<br>0.09<br>0.43<br>_0.63_<br>_−0.08_<br>0.24<br>_0.75_<br>_1.30_<br>_−0.01_<br>_0.06_<br>_0.37_<br>_0.65_<br>_−_0.01<br>_0.02_<br>_0.23_<br>_0.40_<br>_−0.03_<br>_0.12_<br>_0.47_<br>_0.84_<br>_−0.01_<br>_0.03_<br>_0.23_<br>_0.39_<br>_0.00_<br>_0.01_<br>_0.14_<br>_0.25_<br>_−0.02_<br>_0.05_<br>_0.27_<br>_0.48_<br>_−0.01_<br>_0.02_<br>_0.12_<br>_0.21_<br>_0.00_<br>_0.01_<br>_0.08_<br>_0.13_|_0.02_<br>_0.29_<br>2.25<br>2.06<br>_−0.02_<br>_0.10_<br>0.67<br>1.02<br>_0.00_<br>_0.05_<br>_0.37_<br>_0.63_<br>_−_0.13<br>_0.21_<br>7.13<br>2.16<br>_−_0.02<br>0.07<br>0.48<br>0.66<br>_0.00_<br>_0.02_<br>_0.23_<br>_0.40_<br>_−_0.04<br>0.16<br>1.45<br>1.02<br>_−_0.02<br>0.05<br>0.26<br>0.43<br>_−_0.01<br>0.02<br>0.25<br>0.27|_0.01_<br>_−0.01_<br>0.61<br>0.88<br>_0.00_<br>_−_0.01<br>0.31<br>0.45<br>_0.00_<br>_0.00_<br>0.20<br>0.29<br>_0.00_<br>_0.00_<br>0.45<br>0.68<br>0.01<br>_−_0.01<br>0.27<br>0.38<br>_0.00_<br>_−_0.01<br>0.18<br>0.26<br>_0.01_<br>_−0.02_<br>0.46<br>0.73<br>_0.00_<br>_0.00_<br>0.22<br>0.33<br>_0.00_<br>_0.00_<br>0.16<br>0.23<br>_0.00_<br>_0.00_<br>0.28<br>0.44<br>0.01<br>_−0.01_<br>0.18<br>0.26<br>_0.00_<br>_0.00_<br>0.12<br>0.17|_−_0.01<br>0.02<br>_0.35_<br>_0.45_<br>_0.00_<br>_0.00_<br>_0.11_<br>_0.19_<br>_0.00_<br>_0.00_<br>_0.07_<br>_0.12_<br>_−_0.01<br>0.01<br>_0.22_<br>_0.40_<br>_0.00_<br>_0.00_<br>_0.10_<br>_0.18_<br>_0.00_<br>_0.00_<br>_0.06_<br>_0.11_<br>_−_0.01<br>_0.02_<br>_0.19_<br>_0.34_<br>_0.00_<br>0.01<br>_0.09_<br>_0.16_<br>_0.00_<br>_0.00_<br>_0.06_<br>_0.10_<br>_−_0.01<br>0.02<br>_0.16_<br>_0.29_<br>_0.00_<br>_0.01_<br>_0.07_<br>_0.13_<br>_0.00_<br>_0.00_<br>_0.04_<br>_0.08_|



This table presents descriptive statistics of the LTE parameters (superscript _L_ ) estimated with the two-stage estimator and the FZ-estimator at level _α_ , and of the two-stage estimator of the IQE parameters (superscript _I_ ) estimated with the two-stage estimator between levels 10% and 10% þ _α_ . Table entries in cursive formatting indicate that the entry contains the smallest bias (in absolute value) or standard deviation between LTE estimators or between IQE estimators. The DGP is given by Equation (13). The results are derived from 5,000 simulations. We consider quantile levels _α_ ¼ 2 _:_ 5%, 5%, 10%, and 25%. The numerical subscripts for the LTE and IQE parameters indicate the particular element of the parameter vector. The table provides results for a standardized _t_ -distributed error, with degrees of freedom _μ_ ¼ 4 and _ϕ_ ¼ 0 _:_ 90, such that the regressor _Xt_ has considerable persistence and _Yt_ is conditionally heteroskedastic. We consider sample sizes _T_ ¼ 250, 1,000, and 2,500. 

To test this sensitivity, we take as initial starting values the true parameter values plus some random term that is iid uniformly distributed on the interval ½ _−_ 1 _;_ 1� for each separate element and each Monte Carlo iteration. We observe that the use of this estimator typically results in a higher standard deviation and greater bias of the estimates, For _T_ ¼ 250 the standard deviation of the FZ-estimator can be substantial. However, bias is sometimes similar or smaller (for _α_ ¼ 2 _:_ 5%) relative to our two-stage estimator. 

The IQE estimator, between quantile levels 10% and 10% þ _α_ , has a smaller bias and standard deviation than the LTE estimator at _α_ %, which is intuitive due to a smaller influence of outliers. Again, the weighted estimator generally has better properties. 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **19** 

## 4.3 Coverage Rates 

Table 2 provides the coverage rates of the confidence intervals of our LTE and IQE estimators. The coverage rates are calculated as the percentage of simulations for which the true parameter value lies within the 95% confidence interval calculated using the estimated asymptotic covariance matrix. We consider sample sizes _T_ ¼ 250, 1,000, and 2,500. 

We observe that the coverage rates of the LTE estimator converge to the nominal level, with increasing _T_ . Moreover, weighting improves coverage. For the LTE estimators at quantile level _α_ ¼ 2 _:_ 5% the coverage rates are well behaved at sample size _T_ ¼ 2,500 for the weighted estimator. The coverage rates of the IQE estimators converge quickly to the nominal level. Sample sizes of _T_ ¼ 250 are generally sufficient. We observe that coverage rates are closer to nominal values for _α_ closer to 0.5. 

## 4.4 Tests 

Table 2 also provides empirical rejection rates for two tests. First, we consider a size experiment with null hypothesis _β_[ð] 0 _[L] ;j_[Þ] _[−β]_[ð] 0 _[I] ;_[Þ] _j_[¼ ð] _[e]_[ð] _[α]_[Þ] _[−][i]_[ð] _[α][;][α]_[0][ÞÞ][, for ] _[j]_[ ¼][ 1 or 2. This null ] hypothesis is satisfied by the DGP in Equation (13). We perform the test both for the intercept and the coefficient of _Xt_ . Second, we consider a power experiment with _β_[ð] 0 _[L] ;j_[Þ] _[−β]_[ð] 0 _[I] ;_[Þ] _j_[¼] � _e_ ð _α_ Þ _− i_ ð _α; α_[0] Þ� × ð1 þð _k −_ 1Þ _=_ 9Þ, for _k_ ¼ 1 _;_ ... _;_ 10, such that the values _k >_ 1 

**Table 2.** Coverage rates for the two-stage estimator and empirical rejection rates of tests in the simulation experiment. 

|**_T_**|**LTE (2-stage)**<br>**(unweighted)**<br>_β_ð**L**Þ<br>**1**<br>_β_ð**L**Þ<br>**2**|**LTE (2-stage)**<br>**(weighted)**<br>_β_ð**L**Þ<br>**1**<br>_β_ð**L**Þ<br>**2**|**IQE (2-stage)**<br>**(unweighted)**<br>_β_ð**I**Þ<br>**1**<br>_β_ð**I**Þ<br>**2**|**IQE (2-stage)**<br>**(weighted)**<br>_β_ð**I**Þ<br>**1**<br>_β_ð**I**Þ<br>**2**|**Tests**<br>**(unweighted)**<br>**Int.**<br>**Coeff.**|**Tests**<br>**(weighted)**|
|---|---|---|---|---|---|---|
|||||||**Int.**<br>**Coeff.**|
|_α_¼2_:_5%<br>250<br>0.82<br>**0.40**<br>1,000<br>0.88<br>**0.57**<br>2,500<br>0.76<br>**0.63**<br>_α_¼5%<br>250<br>0.88<br>**0.54**<br>1,000<br>0.88<br>**0.66**<br>2,500<br>0.84<br>**0.73**<br>_α_¼10%<br>250<br>0.89<br>**0.64**<br>1,000<br>0.87<br>**0.73**<br>2,500<br>0.84<br>0.78<br>_α_¼25%<br>250<br>0.89<br>0.76<br>1,000<br>0.87<br>0.81<br>2,500<br>0.87<br>0.84||0.76<br>**0.66**<br>0.89<br>0.85<br>0.85<br>0.85<br>0.85<br>0.77<br>0.91<br>0.89<br>0.93<br>0.92<br>0.88<br>0.84<br>0.93<br>0.91<br>0.95<br>0.94<br>0.91<br>0.89<br>0.94<br>0.93<br>0.95<br>0.95|0.86<br>**0.69**<br>0.88<br>0.79<br>0.88<br>0.85<br>0.87<br>0.75<br>0.88<br>0.83<br>0.89<br>0.87<br>0.89<br>0.80<br>0.88<br>0.85<br>0.89<br>0.88<br>0.89<br>0.83<br>0.90<br>0.88<br>0.91<br>0.90|0.89<br>0.84<br>0.94<br>0.91<br>0.94<br>0.93<br>0.90<br>0.88<br>0.94<br>0.92<br>0.94<br>0.94<br>0.91<br>0.90<br>0.94<br>0.93<br>0.94<br>0.94<br>0.93<br>0.91<br>0.94<br>0.94<br>0.95<br>0.95|0.15<br>**0.47**<br>0.10<br>**0.36**<br>0.21<br>**0.32**<br>0.10<br>**0.36**<br>0.10<br>**0.28**<br>0.11<br>0.23<br>0.10<br>**0.29**<br>0.10<br>0.22<br>0.11<br>0.19<br>0.09<br>**0.28**<br>0.12<br>0.24<br>0.12<br>0.19|0.20<br>**0.29**<br>0.10<br>0.14<br>0.15<br>0.15<br>0.14<br>0.20<br>0.09<br>0.11<br>0.07<br>0.08<br>0.10<br>0.15<br>0.07<br>0.09<br>0.06<br>0.07<br>0.10<br>0.13<br>0.06<br>0.08<br>0.06<br>0.06|



This table presents coverage rates of the 95% confidence intervals of the two-stage estimator for the LTE parameters (indicated with superscript _L_ ) at level _α_ and IQE parameters (superscript _I_ ) between levels 10% and 10% þ _α_ . It also presents empirical rejection rates for the tests based on weighted and unweighted LTE and IQE estimators. Values in bold indicate coverage rates below 75% and test rejection rates above 25%. The test on equal intercepts between LTE and IQE models is denoted by ‘Int.’, whereas the test on equal coefficients is denoted by “Coeff”. The DGP is given by Equation (13). The results are derived from 5,000 simulations. We consider quantile levels _α_ ¼ 2 _:_ 5%, 5%, 10%, and 25%. The numerical subscripts for the lower-quantile expectation and interquantile expectation parameters indicate the particular element of the parameter vector. The table provides results for a standardized _t_ -distributed error, with degrees of freedom _μ_ ¼ 4 and _ϕ_ ¼ 0 _:_ 90, such that the regressor _Xt_ has considerable persistence and _Yt_ is conditionally heteroskedastic. We consider sample sizes _T_ ¼ 250, 1,000, and 2,500. The coverage rate is defined as the rate that the true parameter falls within the 95% confidence interval calculated using the asymptotic covariance matrix estimator. 

**20** _Journal of Financial Econometrics_ 

**Figure 1.** Size-adjusted power plots, demonstrating that the tests on the intercept and coefficient are powerful against alternatives for several combinations of the sample size _T_ and quantile level _α_ . (a) Test on intercept and (b) test on coefficient. 

indicate a violation of the null hypothesis and larger values of _k_ indicate a stronger deviation from the null hypothesis. 

The results for the size experiment indicate that rejection rates converge to the nominal level of 5% as the sample size increases for the weighted estimator, and improve for quantile levels _α_ closer to 0.25. Some size distortion remains for the lowest quantile level _α_ ¼ 2 _:_ 5% The unweighted estimator performs worse and remains size-distorted for the largest sample size of _T_ ¼2,500. 

Fig. 1 contains size-adjusted power plots for the sample sizes _T_ ¼ 1,000 and 2,500, and quantile levels _α_ ¼ 5% and 25%. We note that the rejection frequencies increase with larger _T_ , suggesting that the test is consistent. Moreover, tests at quantile levels _α_ closer to the median 50% result in more test rejections. Finally, the rejection frequency increases if the simulation design is further from the null hypothesis (corresponding to larger values of _k_ ). 

## 4.5 Alternative Simulation Settings 

We consider several alternative data settings to study the robustness of these results. In general, results for location-scale weighting and standard normal _εt_ show a somewhat smaller bias, a decrease in the standard deviation of estimates, and improved coverage rates and empirical rejection rates for the tests, as can be observed in Tables S5 and S6 in the Supplementary Material. 

Additional results for weighted estimators, using general weights _w_ ~ _t_ ð _ω_ ~[^][ð] _T[L]_[Þ][Þ][and ] _[w]_[~] _[t]_[ð] _[ω]_[^~][ ð] _T[I]_[Þ][Þ] are very similar for both normal and _tμ_ distributed errors, see Tables S7-S10 in the Supplementary Material. We also find that results for truncated error distributions are very similar to untruncated counterparts, which is unsurprising due to the wide truncation inter~ ~ val. As the weighted LTE estimators with general weights _wt_ ð _ω_[^][ð] _T[L]_[Þ][Þ][performs well for ] untruncated _εt_ , the formal requirement of truncation seems not problematic in practice. 

## **5 Empirical Application: Abnormal Return Decomposition of Size and Momentum Strategies** 

We study the abnormal returns of investment strategies based on the size and momentum effects and the proportion of abnormal returns that are made in the left and right tails of the conditional distribution of the returns. More specifically, we test whether a disproportional share of abnormal returns is made during _tail events_ , conditional on macroeconomic risk. By conditional tail events, we refer here to periods with positive or negative returns that we expect not to exceed or fall short off with a high probability given the risk present in the macroeconomy, which we proxy for here by the factors from the five-factor model 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **21** 

described in Fama and French (2015). This model includes the factors of the three-factor model (Fama and French 1993), and adds profitability and investment factors. See, for example, Liew and Vassalou (2000), Lettau and Ludvigson (2001), and Petkova (2006) for the relationship between the Fama-French factors and macroeconomic variables. 

If the abnormal returns are sufficiently negative during these tail events, investors encounter risk that can trigger asset reallocations, due to financial constraints such as margin constraints on short positions, or other buy or sell triggers. It is therefore of interest to investigate the size of abnormal returns in these periods, since it can impact the tenability of an investment strategy, even though on average the strategy generates a positive abnormal return. 

The average abnormal return _a_ is defined as the intercept in the conditional mean specification of excess return _Rt_ , conditional on risk factors _Xt_ , given by 

**==> picture [222 x 11] intentionally omitted <==**

and is denominated abnormal because it is not explained by risk factors. Asset pricing models are therefore commonly tested on the restriction _a_ ¼ 0, (see, for instance, Black et al. 1972 for a test of CAPM that uses this hypothesis, and Gibbons et al. 1989 for a test on the efficiency of portfolios that uses a multivariate version of this hypothesis), since a deviation from zero points toward excess returns that are unexplained by the asset pricing model. In practice, the presence of abnormal returns is often attributed to the skill level of a portfolio manager. 

In the presence of nonzero average abnormal returns, it is then of interest how different periods contribute to the average abnormal returns. It could be, for instance, that periods with extremely large positive or negative returns generate most of the average abnormal return. In one such case, the profitability of the investment strategy depends on the investor’s ability to tolerate many periods with insignificant abnormal returns, and potentially several periods with large negative abnormal returns, to finally collect a large positive return. On the other hand, strategies that are less dependent on extreme abnormal returns require much less tolerance in this regard and are therefore more attractive. 

We quantify the abnormal return during tail events as the intercepts in the specification of the LTE and RTE, that is 

**==> picture [204 x 30] intentionally omitted <==**

where _Qt_ ð _α_ Þ denotes the _α_ -quantile of _Rt_ conditional on _Xt_ . We look at these quantities because they explicitly denote the average abnormal return during negative and positive tail events and are therefore closely related to the average abnormal return over all events. We also quantify abnormal returns made in non-tail periods by the intercept in the IQE specification, for 0 _< α <_ 1 _=_ 2, 

**==> picture [240 x 14] intentionally omitted <==**

By properties of the conditional expectation, the conditional mean is linearly related to the previous three quantities in the following way, 

**==> picture [232 x 13] intentionally omitted <==**

**22** _Journal of Financial Econometrics_ 

The average abnormal mean return _a_ can be similarly dissected as 

**==> picture [238 x 10] intentionally omitted <==**

When we estimate _a_ by OLS or weighted least-squares, and _aL_ , _aI_ , and _aR_ with the (weighted) unweighted estimator, the same exact linear relationship holds for the estimates ^ ^ ^ ^ ^ ^ ^ ^ _aOLS_ , _aL_ , _aI_ , and _aR_ , that is _aOLS_ ¼ _αaL_ þð1 _−_ 2 _α_ Þ _aI_ þ _αaR_ . We use equivalent locationscale weights for all weighted estimators and elaborate below. Moreover, by estimating the LTE, IQE, and RTE parameters with our estimator we are robust to heterogeneity in the risk factor loadings _bL_ , _bI_ , and _bR_ . Heterogeneity indicates that the relation between returns and risk factors differs over the return distribution and arises, for instance, but not exclusively when a risk factor partly explains return volatility. If we do not account for heterogeneity in the data, this can lead to incorrect inference on the abnormal returns. 

We test for heterogeneity of the risk factor loadings in our analysis and find evidence of its presence in stocks with small market equity. The Wald test is performed for each of the three risk factor separately, that is _i_ ¼ 1 _;_ 2 _;_ or 3, and based on joint restrictions _bL;i_ ¼ _αbL;i_ þð1 _−_ 2 _α_ Þ _bI;i_ þ _αbR;i_ , and _bI;i_ ¼ _αbL;i_ þð1 _−_ 2 _α_ Þ _bI;i_ þ _αbR;i_ . 

We can test whether tail events add to average abnormal returns in the same proportion as other events using the linear relation in Equation (18). The hypothesis can be formulated as 1 _=_ 2 �ð _aR_ þ _aL_ Þ ¼ _a_ and tested with a simple Wald test. We look at the average of positive and negative tail events because we are usually not able to predict the direction of the idiosyncratic shock in any period. When the hypothesis is rejected we can conclude that an investment strategy is significantly affected by tail events. 

Testing whether _aR_ ¼ _aL_ ¼ _a_ or whether _aR_ ¼ _aL_ ¼ 0 is less meaningful. Unless _E_[ð] _t[R]_[Þ] is completely explained by _Xt_ , such that there is no idiosyncratic errors, _aL_ and _aR_ can generally not both be equal to the same constant. This can be seen from the fact that _aL_ will be affected by sizable negative idiosyncratic errors and _aR_ by sizable positive idiosyncratic errors when we choose the quantile level _α_ small enough. We can, however, test whether _aL_ and _aR_ are individually smaller or larger than some constant. This can inform an investor of the extreme idiosyncratic risks in his portfolio, similar to an expected shortfall analysis. 

We examine investment strategies based on the size and momentum effects. The size effect (Banz 1981; Fama and French 1992) states that there is a negative relationship between a firm’s market equity and its average unexplained return, whereas the momentum effect states that a firm’s past performance is positively correlated with it short-term future performance (Jegadeesh and Titman 1993). 

We obtain double-sorted portfolios sorted on size and momentum and single-sorted portfolios sorted on size from the data library of Kenneth French. The data library can be found at http://mba.tuck.dartmouth.edu/pages/faculty/ken.french. The dataset includes stocks from the NYSE, AMEX, and NASDAQ that have sufficient prior return data for sorting. The double-sorted portfolios split the sample first at the median NYSE market equity and subsequently divides the size samples in terms of the average 12 to 2 months prior return, with breakpoints the 30 and 70% NYSE average past return percentiles. The single-sorted size portfolios are split using the NYSE size quintiles as breakpoints. 

The five factors that we use to proxy for macroeconomic risks are the five factors from Fama and French (2015), being (1) the excess market return; (2) the size factor (SMB); (3) the value factor (HML); (4) the profitability factor (RMW); and (5) the investment factor (CMA). The size factor is the return on a portfolio with a long position in small market equity stocks and a short position in large market equity stocks, whereas the value factor is the return on a portfolio with a long position in value stocks and a short position in growth stocks. The profitability factor is the difference between the returns on diversified portfolios of stocks with robust and weak profitability. The investment factor is the difference 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **23** 

between portfolios of stocks with low and high investment firms. Fama and French (2015) provide a complete description of these risk factors and show that they explain average stock returns well. We obtain the risk factors from the same data library. 

Our data sample covers the months July 1967 to December 2024. The starting date of our sample is the earliest month for which data is available on all five factors from Ken French’s data library. 

We capture tail events by the worst and best 2.5% of months, such that we choose the quantile level _α_ ¼ 2 _:_ 5%. Unusually bad and good times therefore occur individually about once every two years. In theory, we can consider more extreme events by considering even lower quantile levels, but in practice the quantile level at which we can still perform accurate estimation and inference is dependent on the size of the dataset. We also consider a quantile level of 5% in robustness checks and find that our results do not change materially. 

Finally, we use weighted quantile regression and LTE, RTE, and IQE estimation, with location-scale weights, that is _k_[^] _t_ ¼ ð _st_ ð _ν_ ^ _T_ ð _α_[00] ÞÞ _− st_ ð _ν_ ^ _T_ ð _α_[000] ÞÞÞ _[−]_[1 ] and _w_ ^ _t_ ¼ _k_[^][2] _t_[, with ] _[ν]_[^] _[T]_[ð] _[α]_[Þ][ the ] parameter estimates of the quantile models at level _α_ . These weights are optimal for the DGP in Example 1 and are easy to compute. We choose quantile levels _α_[00] ¼ 40% and _α_[000] ¼ 60% because the quantile regression estimator typically has low asymptotic variance for quantile levels close to the median. 

Table 3 summarizes our results. In this table, we consider four portfolios that include small and large market equity, and high and low momentum stocks, and small and large market equity portfolios that take long positions in high momentum stocks and short positions in low momentum stocks. We call these portfolios small/hi, small/lo, big/lo, big/hi, small/hi-lo, and big/hi-lo. The first row of results presents estimates of the abnormal return _a_ . We observe that high (low) momentum portfolios generate significantly positive (negative) abnormal returns on average. The long-short portfolios generate positive abnormal returns on average. All average abnormal returns are significant at the 1% level, which agrees with the momentum literature (see, for instance, Jegadeesh and Titman 2001). 

The second and third rows of table present the abnormal returns generated during negative tail events, denoted by _aL_ , and positive tail events, denoted by _aR_ . We see that small market equity stocks show asymmetric abnormal return behavior in the tails, where abnormal returns generated during positive tail events outweigh those during negative tail events. Large market equity stocks do not show this skewness. The long-short portfolios generate the most extreme abnormal returns during tail events. The big/lo-hi portfolio, for instance, generates average abnormal returns of about -17% and 14% percentage points during tail events. 

The fourth row presents _α_ ð _aL_ þ _aR_ Þ, which denotes the contribution of tail events to the abnormal return. Together with ð1 _−_ 2 _α_ Þ _aI_ , the contribution of non-tail events, they add up to _a_ . In the first row of the test results, we show the _p_ -value of a Wald test on the proportional contribution of tail events to the average abnormal return, that is 1 _=_ 2 �ð _aR_ þ _aL_ Þ ¼ _a_ . We can reject a proportional contribution at a 5% significance level for the small/hi equity portfolios and small/hi-lo portfolios, respectively. The positive average abnormal returns of the small/hi portfolio are driven to a large extent by tail events, whereas the negative average abnormal return for the small/lo portfolio is offset by a disproportionally large positive abnormal return during tail events. We also observe that a long-short momentum strategy for small market equity stocks cannot remove the disproportional contribution of tail events to average abnormal returns. 

These results suggest that short positions in small-market equity stocks are unstable due to large negative returns during tail events. An investor should therefore carefully consider long positions to offset the short position if they want to remove the negative impact of tail events from their portfolio. 

**24** _Journal of Financial Econometrics_ 

**Table 3.** Average abnormal returns of momentum and size strategies, and average abnormal returns in the 2.5% worst and the 2.5% best states. 

|**Size/momentum**|**Double-sorted portfolios on size and momentum**|
|---|---|
||**Small/hi**<br>**Small/lo**<br>**Big/hi**<br>**Big/lo**<br>**Small/hi-lo**<br>**Big/hi-lo**|
|�_a_<br>_aL_<br>_aR_<br>1_=_40�ð_aL −aR_Þ<br>38_=_40�_aI_<br>Tests<br>1_=_2�ð_aL −aR_Þ ¼�_a_<br>Homogeneity_bmkt_<br>Homogeneity_bhml_<br>Homogeneity_bsmb_<br>Homogeneity_brmw_<br>Homogeneity _bcma_|0.52<br>_−_0.70<br>0.31<br>_−_0.45<br>1.26<br>0.72<br>(6.22)<br>(_−_4.69)<br>(3.19)<br>(_−_2.44)<br>(6.03)<br>(2.95)<br>_−_4.96<br>_−_8.27<br>_−_5.95<br>_−_10.57<br>_−_13.86<br>_−_16.66<br>(_−_14.45)<br>(_−_15.65)<br>(_−_10.32)<br>(_−_15.61)<br>(_−_6.47)<br>(_−_6.73)<br>7.20<br>10.42<br>6.43<br>12.48<br>11.69<br>14.25<br>(12.49)<br>(4.13)<br>(15.65)<br>(6.1)<br>(17.11)<br>(20.1)<br>0.06<br>0.05<br>0.01<br>0.05<br>_−_0.05<br>_−_0.06<br>(3.33)<br>(0.83)<br>(0.67)<br>(0.88)<br>(_−_0.96)<br>(_−_0.93)<br>0.47<br>_−_0.75<br>0.30<br>_−_0.49<br>1.32<br>0.78<br>(6.08)<br>(_−_6.52)<br>(3.32)<br>(_−_3.2)<br>(7.24)<br>(3.64)<br>0.05<br>0.14<br>0.83<br>0.15<br>0.02<br>0.10<br>0.68<br>0.14<br>0.23<br>0.93<br>0.79<br>0.67<br>0.02<br>0.55<br>0.87<br>0.24<br>0.98<br>0.44<br>0.20<br>0.15<br>0.24<br>0.75<br>0.15<br>0.67<br>0.70<br>0.46<br>0.55<br>0.42<br>0.42<br>0.27<br>0.60<br>0.38<br>0.68<br>0.23<br>0.13<br>0.42|
|**Size quintile**|**Quintile portfolios sorted on size**<br>**Small**<br>**2**<br>**3**<br>**4**<br>**Big**<br>**Small-big**|
|�_a_<br>_aL_<br>_aR_<br>1_=_40�ð_aL −aR_Þ<br>38_=_40�_aI_<br>Tests<br>1_=_2�ð_aL −aR_Þ ¼�_a_<br>Homogeneity_bmkt_<br>Homogeneity_bhml_<br>Homogeneity_bsmb_<br>Homogeneity_brmw_<br>Homogeneity_bcma_|_−_0.03<br>_−_0.01<br>0.00<br>_−_0.05<br>0.01<br>0.03<br>(_−_0.75)<br>(_−_0.43)<br>(0.02)<br>(_−_1.05)<br>(1.31)<br>(0.69)<br>_−_2.49<br>_−_1.80<br>_−_2.18<br>_−_2.98<br>_−_0.62<br>_−_3.39<br>(_−_14.79)<br>(_−_9.61)<br>(_−_15.22)<br>(_−_5.97)<br>(_−_11.56)<br>(_−_8.53)<br>3.55<br>1.35<br>2.29<br>2.38<br>0.65<br>2.47<br>(7.83)<br>(15.25)<br>(10.61)<br>(16.76)<br>(18.11)<br>(14.77)<br>0.03<br>_−_0.01<br>0.00<br>_−_0.02<br>0.00<br>_−_0.02<br>(2.19)<br>(_−_2.15)<br>(0.41)<br>(_−_1.17)<br>(0.53)<br>(_−_2.15)<br>_−_0.06<br>0.00<br>0.00<br>_−_0.03<br>0.01<br>0.05<br>(_−_1.5)<br>(_−_0.01)<br>(_−_0.07)<br>(_−_0.84)<br>(1.31)<br>(1.39)<br>0.01<br>0.02<br>0.65<br>0.27<br>0.89<br>0.01<br>0.05<br>0.30<br>0.86<br>0.39<br>0.79<br>0.63<br>0.05<br>0.86<br>0.97<br>0.24<br>0.83<br>0.08<br>0.08<br>0.40<br>0.16<br>0.48<br>0.59<br>0.05<br>0.41<br>0.62<br>0.33<br>0.55<br>0.17<br>0.38<br>0.79<br>0.28<br>0.59<br>0.14<br>0.79<br>0.55|



This table presents parameter estimates and corresponding _t_ -statistics (in brackets) of average abnormal returns and average abnormal returns during tail events of double-sorted portfolios on size and momentum and singlesorted portfolios on size. The average abnormal return is denoted by _a_ . The average abnormal returns during negative tail events, denoted _aL_ , during positive tail events, denoted _aR_ , and during non-tail events, denoted _aI_ , are estimated with the weighted two-stage estimator. We choose _α_ ¼ 2 _:_ 5%. The row representing _α_ �ð _aL_ þ _aR_ Þ describes the contribution of negative and positive tail events to the average abnormal return _a_ . Similarly, ð1 _−_ 2 _α_ Þ _aI_ describes the contribution of non-tail events. The following relation holds: _a_ ¼ _α_ ð _aL_ þ _aR_ Þþð1 _−_ 2 _α_ Þ _aI_ , which holds both in population and for the estimates. The table also provides _p_ - values of Wald tests for the following hypotheses (1) proportional contribution to abnormal returns of tail events, that is 1 _=_ 2 �ð _aL_ þ _aR_ Þ ¼ _a_ ; and (2) homogeneity of factor loadings _bmkt_ , _bhml_ , _bsmb_ , _brmw_ , and _bcma_ . Our dataset covers the months July 1963 to December 2024 for a total of 738months. 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **25** 

Since our results indicate that the disproportional contribution is found primarily in stocks with small market equity, we also look at single-sorted size quintile portfolios. We indeed find that small market equity stocks have disproportionally large abnormal returns during tail events (at a 1% significance level). A long-short portfolio in large and small market equity stocks does not remove this disproportionality because the long position does not consist of stocks that can correct for it. 

We have also obtained results using standard errors based on a HAC-estimator of the asymptotic covariance matrix to account for additional sources of serial correlation in the asset returns. These results are presented in Table S13 in the Supplementary Material. The conclusions are similar. Theoretical results for the HAC estimator are derived in Supplementary Section S5.4 in the Supplementary Material. A robustness check that considers the quantile level _α_ ¼ 5% deliver similar conclusions, with most significant test results upheld. Table S14 in the Supplementary Material presents these results. 

Finally, the homogeneity tests on factor coefficients can occasionally be rejected for the excess market return and value factor, in the case _α_ ¼ 2 _:_ 5%. At _α_ ¼ 5%, we reject more frequently and for all factors. 

## **6 Concluding Remarks** 

We propose an efficiently weighted, semiparametric estimator of the parameters in (non) linear models of LTE, RTE, and IQE. Our estimator is a multi-stage estimator that consists of (nonlinear) quantile regression and (nonlinear) least-squares optimization stages. Our estimator applies to weakly dependent data. We establish consistency and asymptotic normality of the estimator and provide a consistent estimator of the asymptotic covariance matrix. 

In an empirical application, we explore the abnormal returns of size and momentum portfolios generated by positive and negative tail events and test whether tail events contribute proportionally to the average abnormal return of portfolio strategies based on the size and momentum effects. These strategies can be unstable or untenable if this is not the case. We find that small market equity stocks generate a disproportional, positive share of the average abnormal return during tail events. 

## **Supplemental Material** 

Supplemental material is available at _Journal of Financial Econometrics online._ 

## **Conflict of Interest** 

No conflict of interests. 

## **Funding** 

No funding. 

## **References** 

Acharya, V. V., L. H. Pedersen, T. Philippon, and M. Richardson. 2017. Measuring Systemic Risk. _Review of Financial Studies_ 30: 2–47. 

Adrian, T., and M. K. Brunnermeier. 2016. CoVaR. _American Economic Review_ 106: 1705–1741. Andrews, D. W. 1992. Generic Uniform Convergence. _Econometric Theory_ 8: 241–257. Artzner, P., F. Delbaen, J.-M. Eber, and D. Heath. 1999. Coherent Measures of Risk. _Mathematical Finance_ 9: 203–228. 

**26** _Journal of Financial Econometrics_ 

Banz, R. W. 1981. The Relationship between Return and Market Value of Common Stocks. _Journal of Financial Economics_ 9: 3–18. 

Basak, S., and A. Shapiro. 2001. Value-at-Risk-Based Risk Management: Optimal Policies and Asset Prices. _Review of Financial Studies_ 14: 371–405. 

Bates, C. E., and H. White. 1993. Determination of Estimators with Minimum Asymptotic Covariance Matrices. _Econometric Theory_ 9: 633–648. 

Black, F., M. C. Jensen, and M. Scholes. 1972. “The Capital Asset Pricing Model: Some Empirical Findings.” In M. C. Jensen (ed.), _Studies in the Theory of Capital Markets_ . Praeger, New York. 

Boussama, F., F. Fuchs, and R. Stelzer. 2011. Stationarity and Geometric Ergodicity of BEKK Multivariate GARCH Models. _Stochastic Processes and Their Applications_ 121: 2331–2360. Bradley, R. C. 2005. Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions. _Probability Surveys_ 2: 107–144. 

Brazauskas, V., B. L. Jones, M. L. Puri, and R. Zitikis. 2008. Estimating Conditional Tail Expectation with Actuarial Applications in View. _Journal of Statistical Planning and Inference_ 138: 3590–3604. Brownlees, C, and R. F. Engle. 2017. SRISK: A Conditional Capital Shortfall Measure of Systemic Risk. _Review of Financial Studies_ 30: 48–79. 

Buhlmann, P. 1995. The Blockwise Bootstrap for General Empirical Processes of Stationary Sequences. € _Stochastic Processes and Their Applications_ 58: 247–265. 

Chen, S. X. 2007. Nonparametric Estimation of Expected Shortfall. _Journal of Financial Econometrics_ 6: 87–107. 

Chernozhukov, V. J., C. Escanciano, H. Ichimura, W. K. Newey, and J. M. Robins. 2016. Locally Robust Semiparametric Estimation. _Econometrica_ 90: 1501–1535. 

Chernozhukov, V, and C. Hansen. 2006. Instrumental Quantile Regression Inference for Structural and Treatment Effect Models. _Journal of Econometrics_ 132: 491–525. 

Corsi, F. 2009. A Simple Approximate Long-Memory Model of Realized Volatility. _Journal of Financial Econometrics_ 7: 174–196. 

Dimitriadis, T, and S. Bayer. 2019. A Joint Quantile and Expected Shortfall Regression Framework. _Electronic Journal of Statistics_ 13: 1823–1871. 

Dimitriadis, T, T. Fissler, and J. F. Ziegel. 2021. The Efficiency Gap. _arXiv preprint arXiv : 2010.14146_ , preprint: not peer reviewed. 

Doukhan, P., P. Massart, and E. Rio. 1995. Invariance Principles for Absolutely Regular Empirical Processes. In. _Annales de l’IHP Probabilit_ � _es et Statistiques_ volume31: pages393–427. 

Emmer, S., D. Tasche, and M. Kratz. 2015. What Is the Best Risk Measure in Practice? A Comparison of Standard Measures. _The Journal of Risk_ 18: 31–60. 

Escanciano, J. C., and S. Mayoral. 2008. Semiparametric Estimation of Dynamic Conditional Expected Shortfall Models. _International Journal of Monetary Economics and Finance_ 1: 106–120. 

Fama, E. F., and K. R. French. 1992. The Cross-Section of Expected Stock Returns. _The Journal of Finance_ 47: 427–465. 

Fama, E. F., and K. R. French. 1993. Common Risk Factors in the Returns on Stocks and Bonds. _Journal of Financial Economics_ 33: 3–56. 

Fama, E. F., and K. R. French. 2015. A Five-Factor Asset Pricing Model. _Journal of Financial Economics_ 116: 1–22. 

Fissler, T, and J. F. Ziegel. 2016. Higher Order Elicitability and Osband’s Principle. _The Annals of Statistics_ 44: 1680–1707. 

Fissler, T, and J. F. Ziegel. 2021. On the Elicitability of Range Value at Risk. _Statistics & Risk Modeling_ 38: 25–46. 

Gibbons, M. R., S. A. Ross, and J. Shanken. 1989. A Test of the Efficiency of a Given Portfolio. _Econometrica_ 57: 1121–1152. 

Gneiting, T, and A. E. Raftery. 2007. Strictly Proper Scoring Rules, Prediction, and Estimation. _Journal of the American Statistical Association_ 102: 359–378. 

Jegadeesh, N, and S. Titman. 1993. Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency. _The Journal of Finance_ 48: 65–91. 

Jegadeesh, N, and S. Titman. 2001. Profitability of Momentum Strategies: An Evaluation of Alternative Explanations. _The Journal of Finance_ 56: 699–720. 

Komunjer, I, and Q. Vuong. 2010. Efficient Estimation in Dynamic Conditional Quantile Models. _Journal of Econometrics_ 157: 272–285. 

Barendse j Efficiently Weighted Estimation of Tail and Interquantile Expectations **27** 

Lettau, M, and S. Ludvigson. 2001. Resurrecting the (C) CAPM: A Cross-Sectional Test When Risk Premia Are Time-Varying. _Journal of Political Economy_ 109: 1238–1287. 

Liew, J, and M. Vassalou. 2000. Can Book-to-Market, Size and Momentum Be Risk Factors That Predict Economic Growth? _Journal of Financial Economics_ 57: 221–245. 

- McNeil, A. J, R. Frey, and P. Embrechts. 2015. _Quantitative Risk Management: Concepts, Techniques and Tools_ . Princeton University Press, Princeton, NJ. 

- Nadarajah, S., B. Zhang, and S. Chan. 2014. Estimation Methods for Expected Shortfall. _Quantitative Finance_ 14: 271–291. 

- Newey, W. K, and D. McFadden. 1994. Chapter 36 Large Sample Estimation and Hypothesis Testing. volume 4 of _Handbook of Econometrics_ , pages 2111–2245. Elsevier. 

- Nolde, N, and J. F. Ziegel. 2017. Elicitability and Backtesting: Perspectives for Banking Regulation. _Annals of Applied Statistics_ 11: 1833–1874. 

- Patton, A. J., J. F. Ziegel, and R. Chen. 2019. Dynamic Semiparametric Models for Expected Shortfall (and Value-at-Risk). _Journal of Econometrics_ 211: 388–413. 

- Petkova, R. 2006. Do the Fama–French Factors Proxy for Innovations in Predictive Variables? _The Journal of Finance_ 61: 581–612. 

- Taylor, J. W. 2008a. Estimating Value at Risk and Expected Shortfall Using Expectiles. _Journal of Financial Econometrics_ 6: 231–252. 

- Taylor, J. W. 2008b. Using Exponentially Weighted Quantile Regression to Estimate Value at Risk and Expected Shortfall. _Journal of Financial Econometrics_ 6: 382–406. 

- Weiss, A. A. 1991. Estimating Nonlinear Dynamic Models Using Least Absolute Error Estimation. _Econometric Theory_ 7: 46–68. 

© The Author(s) 2026. Published by Oxford University Press. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https:// creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Journal of Financial Econometrics, 2026, 24, 1–27 https://doi.org/10.1093/jjfinec/nbag003 Article - with submission fee 

