See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/374048212 

## Testing Conditional Independence in Casual Inference for Time Series Data † 

**Article** _in_ Statistica Neerlandica · September 2023 DOI: 10.1111/stan.12323 

**==> picture [115 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
CITATION<br>1<br>4 authors , including:<br>Zongwu Cai<br>University of Kansas<br>185 PUBLICATIONS 5,006 CITATIONS<br>SEE PROFILE<br>**----- End of picture text -----**<br>


**==> picture [108 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
READS<br>227<br>Ying Fang<br>Xiamen University<br>47 PUBLICATIONS 427 CITATIONS<br>SEE PROFILE<br>**----- End of picture text -----**<br>


All content following this page was uploaded by Zongwu Cai on 05 October 2023. 

The user has requested enhancement of the downloaded file. 

# **Testing Conditional Independence in Casual Inference for Time Series Data**[∗†] 

Zongwu Cai _[a]_ , Ying Fang _[b,c]_ , Ming Lin _[b,c]_ , Shengfang Tang _[b,][†]_ 

> _c_ Department of Economics, University of Kansas, Lawrence, KS 66045, USA. 

_b_ Wang Yanan Institute for Studies in Economics and Fujian Key Laboratory of Statistical Sciences, Xiamen University, Xiamen, Fujian 361005, China. 

> _c_ Department of Statistics and Data Science, School of Economics, Xiamen University, Xiamen, Fujian 361005, China. 

## August 24, 2023 

**Abstract** : In this paper, we propose a new procedure to test conditional independence assumption in studying casual inference for time series data. The conditional independence assumption is transformed to a nonparametric conditional moment test with the help of auxiliary variables which are allowed to affect policy choice but the dependence can be fully captured by potential outcomes and observable controls. When the policy choice is binary, a nonparametric statistic test is developed further for testing the conditional independence assumption conditional on policy propensity score. Under some regular conditions, we show that the proposed test statistics are asymptotically normal under the null hypotheses for time series data. In addition, the performances of the proposed methods are illustrated through Monte Carlo simulations and a real example considered in Angrist and Kuersteiner (2011). 

**Keywords:** Casual inference; Economic policy evaluation; Moment test; Nonparametric estimation; Treatment 

MSC classification: 62G10; 62G20; 62P25. 

> ∗The authors acknowledge the financial supports, in part, from the National Science Fund of China (NSFC) for Distinguished Scholars (71625001) and the NSFC with grant numbers 71631004 and 72033008. 

> †Corresponding author: Shengfang Tang (E-mail: _tangshengfang103@163.com_ ). 

## **1 Introduction** 

One of the most important tasks in empirical economics is to quantitatively assess the causal effect of economic or social policies using plausibly exogenous policy variation. Recently, there have been some statistical methods proposed, see, for example, the papers by Angrist and Kuersteiner (2011), Jordà and Taylor (2016), and Angrist, Jordà and Kuersteiner (2018), and the survey paper by Liu et al. (2020), for studying economic policy evaluation, which is an extension of the Rubin causal model in Rubin (1974) for identically independent distributed (iid) setting to a time series context. Sidestepping the impossible mission of accurately modeling an entire economy, the new framework only needs to estimate a policy propensity score, the probability of how a policy is determined conditional on a set of current information at hand, in a very flexible way. With an assumption of conditional independence (CI), which means that, conditional on a set of controls possibly including past policy choices and lagged outcomes, the current policy choice is independent of potential outcomes, the policy causal effects defined by the so called dynamic treatment effect then can be identified using inverse probability weighting (IPW) estimators. 

The CI assumption plays a key role in identifying the causal effect in evaluating economic policies. The conditional independence between current policy choice and potential outcomes implies that, after appropriately considering a set of observable controls, the remaining policy variation can be regarded as exogenous shocks and then can be used to identify policy effects. Exploring policy variation at hand is actually a natural strategy particularly in a situation lack of conducting natural experiments or quasi-experiments, although conditional independence seems to be a strong assumption. Therefore, in this paper, this gap is filled up by proposing a statistical test method for testing the CI assumption in a data-driven approach. 

Our test procedure relies on the existence of auxiliary variables, similar to instrumental variables in linear regression, which allow to affect policy choices but the linkage from auxiliary variables to policy choices can be fully captured by potential outcomes and observed controls. With the availability of such auxiliary variables, the conditional independence 

1 

assumption can be easily tested using conditional moment tests in a nonparametric way. However, such a test procedure encounters a serious implementation problem when the dimension of controls is large due to the curse of dimensionality in nonparametric testing. When the policy choice is only a binary variable, we further develop a test procedure conditional on policy propensity score to avoid the aforementioned dimensionality problem. Actually, the assumption on the existence of auxiliary variables has been widely adopted in statistics literature such as Zhao and Shao (2015) and Breunig (2019) for dealing with missing observation difficulties and Hu and Schennach (2008) for tackling measurement error problems. In other scenarios, Fang et al. (2020) provided some clues on how to find auxiliary variables in real data among all observable controls. 

To the best of our knowledge, our test procedure is the first attempt in statistics literature to test CI for economic policy evaluation in time series context. Indeed, the previous literature focused on testing CI for policy evaluation only for cross-sectional data. For example, by using a binary instrumental variable, Donald et al. (2014) proposed a DurbinWu-Hausman type statistic, a popular approach in the econometrics literature, to test the conditional mean independence which is a central identification assumption for economic policy evaluation. With a presumption that the error terms in both the outcome equation and the selection equation are symmetrically distributed, Chen et al. (2018) proposed a Kolmogorov-Smirnov type statistic to test conditional mean independence by comparing two estimators obtained with/without conditional mean independence. Our paper is closely related to the work in Fang et al. (2020) which tested CI by using auxiliary variables for iid data. However, different from Fang et al. (2020), the current paper is on testing CI for economic policy evaluation in a time series context, and furthermore, our paper develops a test for conditional independence conditional on policy propensity score, which is novel in statistics literature. 

The rest of the paper is organized as follows. Section 2 first provides a brief introduction of the framework of economic policy evaluation for time series, and then develop statistics based on auxiliary variables to test conditional independence conditional on policy propensity score. Large sample properties of proposed test statistics are also established in the same 

2 

section. Section 3 reports results from Monte Carlo simulations and Section 4 applies our test procedure to revisiting the famous real example studied by Angrist and Kuersteiner (2011). Section 5 concludes the paper. All technical proofs are gathered in the Appendix. 

## **2 Testing Procedures** 

## **2.1 Framework** 

Suppose that the observed time series process is denoted by (y _t, Mt, Bt_ ), where y _t_ is a vector of outcome variables, _Bt ∈{b_ 0 _, · · · , bJ }_ is a policy choice, and _Mt_ is a vector of observed controls including exogenous and (lagged) endogenous variables. Denote _υ_ as the policy regime, which represents the state of the economy at some time and takes values in a parameter space, denoted by Υ. It is assumed that the policy choice _Bt_ is determined by both observed and unobserved variables according to _Bt_ = _B_ ( _Mt, υ, εt_ ), where _εt_ is the idiosyncratic information or taste variables. In this paper, to describe the potential outcome, we assume that the policy changes while the policy regime remains unchanged. As in Angrist and Kuersteiner (2011) and Angrist et al. (2018), the following definition of potential outcomes in a time series setup is adopted. 

**Definition 1.** _Given t, ν and υ, potential outcomes {_ y _[υ] t,ν_[(] _[b]_[);] _[ b][∈B}][are][defined][as][the][set] of values the observed outcome variable_ y _t_ + _ν would take on if the policy choice Bt_ = _b, with b ∈B_ = _{b_ 0 _, · · · , bj, · · · , bJ }._ 

From the above definition, it is easy to observe that the vector of potential outcomes includes the observed outcome, y _t_ + _ν_ = y _[υ] t,ν_[(] _[b]_[)][, and the counterfactual outcome describing the] consequences of policy choices not taken. Without loss of generality, it is assumed that the observed outcome variable y _t_ + _ν_ is of dimension-one throughout the remaining paper. Define _′ Yt,I_ = (y _t_ +1 _, · · · ,_ y _t_ + _I_ ) _[′]_ and let _Yt,I[υ]_[(] _[b]_[)][=] �y _[υ] t,_ 1[(] _[b]_[)] _[,][ · · ·][,]_[ y] _[υ] t,I_[(] _[b]_[)] � be the vector of potential outcomes up to horizon _I_ . Then, the observed outcomes have the following relationship with the potential outcomes 

**==> picture [140 x 27] intentionally omitted <==**

3 

where _I{·}_ is an indicator function. Under this framework, similar to the case of crosssectional data setting, one can define a dynamic average response to the policy _bj_ relative to the benchmark policy _b_ 0 by contrasting two potential outcomes, 

**==> picture [140 x 23] intentionally omitted <==**

Consequently, a collection of all possible policy effects is given by _λ_ = ( _λ_ 1 _, · · · , λJ_ ) _[′]_ . It should be noted that potential outcomes for counterfactual policy choices can not be observed, so that the average effects _λj_ for 1 _≤ j ≤ J_ , can not be estimated directly. To identify the parameters of interest _λj_ for 1 _≤ j ≤ J_ , similar to the Rubin causal model for the cross sectional data, see, for example, Rubin (1974) for details, by following Angrist and Kuersteiner (2011), Angrist et al. (2018), and Liu et al. (2020), we adopt the following conditional independence assumption, which is the so-called _conditional independence_ (CI) in statistics literature. 

**Assumption 1.** _Conditional independence:_ 

**==> picture [320 x 16] intentionally omitted <==**

_where Mt is a vector of predetermined variables that predict Bt and denotes the statistical independence._ 

The above assumption is commonly imposed, for example, by Angrist and Kuersteiner (2011) and Angrist et al. (2018) to identify the causal effects of monetary policy shocks and by Jordà and Taylor (2016) to estimate the average treatment effect of fiscal policy, which are under time series framework. It is worth noting that this assumption focuses on variation in policy interventions while holding the policy regime fixed, after conditioning on predetermined variables _Mt_ . In addition, this assumption implies that, given some appropriate predetermined variables _Mt_ , potential outcomes are independent of the policy variables. Based on this assumption, it is easy to see that the parameters of interest _λj_ can be identified by 

**==> picture [442 x 29] intentionally omitted <==**

4 

for 1 _≤ j ≤ J_ . Moreover, according to the identification results above, Angrist et al. (2018) proposed an IPW method to estimate _λj_ . 

## **2.2 Testing Statistic** 

It is important to note that the CI assumption given above may not hold in practice, for example, if there are some unobserved confounders that can affect both policy choice _Bt_ and potential outcomes y _[υ] t,ν_[(] _[b][j]_[)][.][In][this][case,][the][IPW][estimate][considered][in][Angrist] et al. (2018) should be inconsistent in general and then the estimating results would result in misleading inferences for the parameters of interest. Therefore, it is urgent to suggest an approach which can be used to test whether the CI assumption is true or not. To this end, this paper develops a new procedure by using a set of auxiliary variables to test whether Assumption 1 holds under time series setting. A vector of valid auxiliary variables _At ∈_ R _[p]_ is defined by the following assumption. 

**Assumption 2.** _Suppose that there is a vector of variables At ∈_ R _[p] which are continuously distributed and correlated with the potential outcomes_ y _[υ] t,ν_[(] _[b][j]_[)] _[.][Furthermore,][the][following] condition is satisfied:_ 

**==> picture [378 x 15] intentionally omitted <==**

**Remark 1.** Note that this assumption is the time series version of Assumption 2.1(i) in Fang et al. (2020), which requires that a policy intervention is mainly driven by potential outcomes and observed predetermined variables _Mt_ . As mentioned in Section 1, choosing auxiliary variables is similar to finding instrumental variables in classical linear regression. But, unfortunately, as pointed out by Fang et al. (2020), there is no general guideline on how to select _At_ and it might be done case by case. Of course, it would seem very challenging to find such variables based on a priori reasoning. This is because the potential outcomes y _[υ] t,ν_[(] _[b][j]_[)] presumably depend on latent shocks that hit the economy between time _t_ and _t_ + _ν_ , so the conditioning sigma algebra includes a mix of past and future information. We conjecture that the testing power might depend on the choice of _At_ . This issue needs a further investigation and it is warranted as a future research topic. 

5 

It is easy to show that under Assumption 2, Assumption 1 implies that _E_ ( _Bt|Mt, At_ ) = _E_ ( _Bt|Mt_ ), which further implies that Assumption 1 can be tested by investigating whether _At_ is significant for the mean of the policy choice _Bt_ conditional on controls _Mt_ . Formally, in order to test Assumption 1 being true or not, the following testing hypothesis is considered: 

**==> picture [454 x 15] intentionally omitted <==**

Similar to Fan and Li (1996) and Li (1999), a nonparametric conditional moment statistic is constructed to test the null hypothesis in (1). To this end, first, some additional notations are needed. Denote _Gt_ = ( _A[′] t[, M][ ′] t_[)] _[′][∈]_[R] _[p]_[+] _[q]_[,][where] _[M][t][∈]_[R] _[q]_[and] _[A][t][∈]_[R] _[p]_[,][and][define] _[α][t]_[=] _Bt − E_ ( _Bt|At_ ). Then, it is important to note that _U_ = _E_ [ _αtE_ ( _αt|Gt_ )] = _E_ �[ _E_ ( _αt|Gt_ )][2][�] _≥_ 0 and the equality holds if and only if _H_ 0 given in (1) is true. Therefore, _U_ can be used to construct test statistic for consistent testing _H_ 0 in (1). Furthermore, to keep away from the random denominator problem, following the standard method we choose using a density weighted version of _U_ as the basis of our test statistic. That is, 

**==> picture [336 x 15] intentionally omitted <==**

where _µt_ = _αtf_ ( _Mt_ ), and _fG_ ( _·_ ) and _f_ ( _·_ ) are the density functions of _Gt_ and _Mt_ , respectively. Hence, a kernel-based sample analogue of _U[∗]_ is defined by 

**==> picture [422 x 37] intentionally omitted <==**

where _Lst_ = _L_ �( _Gt − Gs_ ) _/a_ � is a kernel function and _a_ = _aN_ is the smoothing parameter. However, it should be noted that the residual _αt_ and the density function _f_ ( _Mt_ ) can not be observed directly, so that to get a feasible test statistic, we should first estimate them nonparametrically. To be specific, we consider the following estimator for _E_ ( _Bt|Mt_ ), given by 

where 

**==> picture [260 x 92] intentionally omitted <==**

6 

is the estimator of _f_ ( _Mt_ ), L[(1)] ( _·_ ) is another kernel function and _a_ 1 denotes the bandwidth � parameter. Consequently, we can obtain the estimator _αt_ = _Bt − E_[�] ( _Bt|Mt_ ) for the residual _αt_ . Therefore, a feasible test statistic is obtained by replacing _µt_ = _αtf_ ( _Mt_ ) by its kernel � estimator _αtf_[�] _Mt_ : 

**==> picture [248 x 37] intentionally omitted <==**

Now, it is ready to investigate the large sample properties of the proposed test statistic _UN_ . To derive the asymptotic distribution of the test statistic _UN_ under _H_ 0, the following assumptions are needed, with the class of kernel functions Υ _λ_ and the class of functions U _[α] µ_[;] see, for example, their definitions in Robinson (1988), Fan and Li (1996), and Li (1999), or the Appendix for details. 

**Assumption 3.** _(i) Suppose that the process {Bt, Mt, At}[N] t_ =1 _[is][strictly][stationary][and][abso-] lutely regular process with the mixing coefficient β_ ( _t_ ) _≤ Cβρ[t] defined by_ 

**==> picture [234 x 32] intentionally omitted <==**

_for all s, t ≥_ 1 _, where_ 0 _< Cβ < ∞ and_ 0 _< ρ <_ 1 _are constants, and Fi[j][denotes][the][σ][-field] generated by {_ ( _Mt, Bt, At_ ) : _i ≤ t ≤ j}._ 

_(ii) Suppose that the residual αt_ = _Bt − E_ ( _Bt|Mt_ ) _satisfies E_ [ _αt|_ Ω _t−_ 1] = 0 _for all t ≥_ 1 _, where_ Ω _t_ = _σ{_ ( _Xs_ +1 _, Bs_ ) : _s ≤ t} is the σ-field generated by {_ ( _Ms_ +1 _, Bs_ ) : _s ≤ t}. (iii) In addition, it is assumed that E_ [ _|αt_[4+] _[ϵ] |_ ] _< ∞ and E αti_ 11 _[α] t[i]_[2] 2 _[· · ·][ α] t[i][ν] ν_ ��1+ _η_[�] _< ∞ for some_ ��� _ν arbitrarily small ϵ >_ 0 _and η >_ 0 _, where_ 2 _≤ ν ≤_ 4 _is an integer,_ 0 _≤ ij ≤_ 4 _and_ � _ij ≤_ 8 _. j_ =1 

**Assumption 4.** _(i) Denote σ_[2] ( _g_ ) = _E_ [ _αt_[2] _[|][G][t]_[=] _[ g]_[]] _[and][µ]_[4][(] _[g]_[) =] _[ E]_[[] _[α] t_[4] _[|][G][t]_[=] _[ g]_[]] _[.][It][is][assumed] that σ_[2] ( _g_ ) _and µ_ 4( _g_ ) _satisfy some Lipschitz conditions: |σ_[2] ( _u_ + _v_ ) _− σ_[2] ( _u_ ) _| ≤_ Γ( _u_ ) _∥v∥ and |µ_ 4( _u_ + _v_ ) _− µ_ 4( _u_ ) _| ≤_ Γ( _u_ ) _∥v∥ with E |_ Γ( _Gt_ ) _|_[2+] _[ι]_[�] _< ∞ for some small ι >_ 0 _, where ∥· ∥_ � _denotes the Euclidean norm._ 

_(ii) Let fτ_ 1 _,τ_ 2 _,··· ,τν_ ( _·_ ) _be the joint probability density of_ ( _G_ 1+ _τ_ 1 _, · · · , G_ 1+ _τν_ )(1 _≤ ν ≤_ 4) _. Suppose that fτ_ 1 _,τ_ 2 _,··· ,τν_ ( _·_ ) _exists, is bounded and satisfies the following Lipschitz condition: |fτ_ 1 _,τ_ 2 _,··· ,τν_ ( _g_ 1 + _v_ 1 _, · · · , gν_ + _vν_ ) _− fτ_ 1 _,τ_ 2 _,··· ,τν_ ( _g_ 1 _, · · · , gν_ ) _| ≤_ Λ _τ_ 1 _,τ_ 2 _,··· ,τν_ ( _g_ 1 _, · · · , gν_ ) _∥v∥, where_ 

7 

Λ _τ_ 1 _,τ_ 2 _,··· ,τν_ ( _g_ 1 _, · · · , gν_ ) _is integrable and satisfies the following conditions_ 

**==> picture [215 x 27] intentionally omitted <==**

_and_ 

**==> picture [294 x 27] intentionally omitted <==**

_for some ς >_ 1 _and constant_ Ξ _>_ 0 _._ 

**Assumption 5.** _(i) The density functions f_ ( _u_ ) _and fG_ ( _g_ ) _of Mt and Gt satisfy f_ ( _u_ ) _∈_ U _[∞] µ[,] fG_ ( _g_ ) _∈_ U _[∞] µ[,][respectively,][and][γ]_[(] _[u]_[)][=] _[E]_[(] _[B][t][|][M][t]_[=] _[u]_[)] _[∈]_[U][4+] _µ[ε] for some integer µ ≥_ 2 _and small ε >_ 0 _, and also fG_ ( _g_ ) _is bounded._ 

_(ii) f_ ( _u_ ) _, fG_ ( _g_ ) _and γ_ ( _u_ ) _all satisfy some Lipschitz conditions: |δ_ ( _u_ + _v_ ) _− δ_ ( _u_ ) _| ≤_ Λ( _u_ ) _∥v∥, where_ Λ( _u_ ) _has finite_ (2 + _η[∗]_ ) _-th moment for some small η[∗] >_ 2 _._ 

**Assumption 6.** _(i) The product kernel is used for both L_ ( _·_ ) _and_ L[(1)] ( _·_ ) _. Define l_ ( _·_ ) _and_ l[(1)] ( _·_ ) _to be their corresponding univariate kernel, then_ l[(1)] ( _·_ ) _∈_ Υ _µ, l_ ( _·_ ) _is non-negative and l_ ( _·_ ) _∈_ Υ2 _._ 

_(ii) As N →∞, a_ 1 _→_ 0 _, a_ = _O_ ( _N[−][α]_[¯] ) _for some_ 0 _< α_ ¯ _<_ 7 _/_ (8( _p_ + _q_ )) _. In addition, a[p]_[+] _[q] /a_ 1[2] _[q]_[=] _[ o]_[(1)] _[and][Na]_[(] _[p]_[+] _[q]_[)] _[/]_[2] _[a]_[2] 1 _[µ]_[=] _[ o]_[(1)] _[.]_ 

These assumptions are commonly imposed in nonparametric literature; see, for example, Li (1999). Under Assumptions 2 - 6, the asymptotic properties of the test statistic _UN_ can be established and formally stated in the following theorem with the detailed proof given in the Appendix. 

**Theorem 1.** _Suppose that Assumptions 2 - 6 are satisfied. Then,_ 

� _(1) Under H_ 0 _, U_[�] _N_ = _Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] _UN /√_ 2 _σU →N_ (0 _,_ 1) _in distribution as N →∞, where_ 

**==> picture [226 x 37] intentionally omitted <==**

_is a consistent estimator of σU_[2] _[given][by]_ 

**==> picture [230 x 28] intentionally omitted <==**

_(2) Under H_ 1 _, P_ ( _U_[�] _N > ON_ ) _→_ 1 _for any non-stochastic sequence ON_ = _o_ ( _Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] ) _._ 

8 

Theorem 1 implies that the test statistic _U_[�] _N_ has the asymptotic standard normal distribution under the null hypothesis. Based on Theorem 1(1), _H_ 0 is rejected at significance level _α_ 0 if _U_[�] _N > Zα_ 0, where _Zα_ 0 is the upper _α_ 0-percentile of the standard normal distribution. It is important to note that in order to use the proposed test _U_[�] _N_ in practice, we need to choose the auxiliary variables _At_ that satisfy Assumption 2. However, if the auxiliary variables _At_ chosen by practitioners do not satisfy Assumption 2, the proposed test tends to reject CI even though CI is true.[1] 

Based on Monte Carlo simulation studies by Li (1999) and Lavergne and Vuong (2000), it concludes that there exists substantial finite sample bias for the normal approximation. Moreover, the test statistic _UN_ depends on two sets of smoothing parameters _a_ 1 and _a_ , and might be sensitive to the choice of the smoothing parameters. To overcome these difficulties, similar to Lavergne and Vuong (2000), a modified version of the test _UN_ is adopted, which should have a better finite sample performance than the test _UN_ , as argued in Lavergne and Vuong (2000). Indeed, Li (1999) adopted the same idea to suggesting a new modified test and further showed that the modified test has the same asymptotic properties as _UN_ . Alternatively, one also can use Bootstrapping method to better approximate the null distribution of _UN_ ; see Li and Racine (2007) for further details for Bootstrapping method. In this paper, we adopt simply the idea of Lavergne and Vuong (2000) and Li (1999) to suggest a modified test statistic. To this end, by substituting _E_[�] ( _Bt|Mt_ ) and _f_[�] _Mt_ into the expression of _UN_ and doing a simplification, we can obtain 

**==> picture [475 x 28] intentionally omitted <==**

where 

**==> picture [346 x 68] intentionally omitted <==**

1To support this statement, which was pointed by an anonymous referee, we indeed conducted a simulation and the simulation result supports this statement. To save the space, the simulation result is not reported in the paper, available upon request. 

9 

and 

**==> picture [348 x 68] intentionally omitted <==**

The following theorem shows that both _UN[′]_[and] _[U][N]_[share][the][exactly][same][asymptotic] distribution with the detailed proof relegated to the Appendix. 

**Theorem 2.** _Under Assumptions 2 - 6, one has (1) Under H_ 0 _, U_[�] _N[′]_[=] _[ Na]_[(] _[p]_[+] _[q]_[)] _[/]_[2] _[U] N[ ′][/] √_ 2 _σ_ � _U →N_ (0 _,_ 1) _in distribution as N →∞, where σ_ � _U_[2] _[is] the same as defined in Theorem 1. (2) Under H_ 1 _, P_ ( _U_[�] _N[′][> O][N]_[)] _[ →]_[1] _[for][any][non-stochastic][sequence][O][N]_[=] _[ o]_[(] _[Na]_[(] _[p]_[+] _[q]_[)] _[/]_[2][)] _[.]_ 

## **2.3 An Extension** 

In many applications, the policy intervention variable _Bt_ may be a binary variable but the dimension of the predetermined variables _Mt_ may be moderate or high relative to the sample size. Under these cases, the proposed test statistics _U_[�] _N_ in Theorem 1 and _U_[�] _N[′]_[in] Theorem 2 can not be used in practice because of the curse of dimensionality. Therefore, it is urgent to suggest a test statistic which applies to the case where the dimension of the predetermined variables _Mt_ is in moderate or high dimension relative to the sample size. 

Note that when _Bt_ is a binary variable, one can show that the CI assumption displayed in Assumption 1 implies that 

**==> picture [417 x 15] intentionally omitted <==**

where _p_ ( _Mt_ ) = _P_ ( _Bt_ = 1 _|Mt_ ) is the policy propensity score function. Hence, based on (2), it is clear that all biases due to observable controls can be removed by conditioning solely on the policy propensity score function. Moreover, we have the following lemma with the detailed proof given in the Appendix. 

10 

**Lemma 1.** _Under Assumption 2, (2) implies that_ 

**==> picture [346 x 23] intentionally omitted <==**

From Lemma 1, to test whether the CI assumption holds or not, one just needs to consider testing whether _At_ is significant for the mean of the policy choice _Bt_ given the policy propensity score function _p_ ( _Mt_ ) instead of the full covariates _Mt_ . Therefore, in this section, the following testing hypothesis is investigated 

**==> picture [481 x 36] intentionally omitted <==**

Denote _Pt_ = _p_ ( _Mt_ ) and _Rt_ = ( _Pt, A[′] t_[)] _[′][∈]_[R] _[κ]_[,][where] _[κ]_[=] _[p]_[ + 1][.][Define] _[ε][t]_[=] _[B][t][−][P][t]_[.][Then,] the hypothesis testing problem formulated in (4) can be rewritten as 

**==> picture [382 x 15] intentionally omitted <==**

Similar to the discussion aforementioned, to test _H_ 0 in (5) holds or not, the following test statistic is suggested 

**==> picture [156 x 33] intentionally omitted <==**

where _fR_ ( _·_ ) is the density function of _Rt_ . Because _εt_ and _Rt_ can not be observed directly, one first needs to estimate them to obtain a feasible test statistic. To overcome the problem of the curse of dimensionality, a flexible parametric model for the unknown policy propensity score function _p_ ( _Mt_ ) is adopted, say assuming that 

**==> picture [132 x 13] intentionally omitted <==**

where _θ_ is an unknown parameter with dimension _r_ . In addition, _θ_ 0 is used to denote the true value of _θ_ ; that is, _p_ ( _Mt_ ) = _p_ ( _Mt_ ; _θ_ 0). Since _Bt_ is a binary variable, a logit or probit model is appropriate for the policy propensity score function _p_ ( _Mt_ ) so that _θ_ can be estimated by using the maximum likelihood method. Denote _θ_[�] _N_ as the estimator of _θ_ and _P_[�] _t_ = _p_ ( _Mt_ ; _θ_[�] _N_ ) 

11 

� as the estimator of _p_ ( _Mt_ ). Define _εt_ = _Bt − P_[�] _t_ and 

**==> picture [338 x 80] intentionally omitted <==**

where _L_ 1( _·_ ) and _L_ 2( _·_ ) are the kernel functions, and _ℓ_ is the smoothing parameter. Therefore, an estimator of _VN[∗∗]_[is][given][by] 

**==> picture [298 x 37] intentionally omitted <==**

Next, to consider the large sample properties of the proposed test statistic _VN_ , the following assumptions are needed. 

**Assumption 7.** _(i) Assume that the process {Bt, Pt, At}[N] t_ =1 _[is][strictly][stationary][and][abso-] lutely regular process with the mixing coefficient β_ ( _τ_ ) = _O_ ( _ρ[τ]_ ) (0 _< ρ <_ 1) _. (ii) The residual εt_ = _Bt − Pt satisfies E_ � _εt|_ Ω _[∗] t−_ 1� = 0 _for all t ≥_ 1 _, where_ Ω _[∗] t−_ 1[=] _σ{_ ( _Ps_ +1 _, Bs_ ) : _s ≤ t} is the σ-field generated by {_ ( _Ps_ +1 _, Bs_ ) : _s ≤ t}._ 

� **Assumption 8.** _(i) Let σ_[2] ( _r_ ) = _E_ ( _ε_[2] _t[|][R][t]_[=] _[r]_[)] _[and][µ]_[�][4][(] _[r]_[)][=] _[E]_[(] _[ε]_[4] _t[|][R][t]_[=] _[r]_[)] _[.][Then][σ]_[�][2][(] _[r]_[)] _[and]_ � � � � � _µ_ 4( _r_ ) _satisfy some Lipschitz conditions: |σ_[2] ( _r_ + _u_ ) _−σ_[2] ( _r_ ) _| ≤ D_ ( _r_ ) _∥u∥ and |µ_ 4( _r_ + _u_ ) _−µ_ 4( _r_ ) _| ≤ D_ ( _r_ ) _∥u∥ with E_ [ _|D_ ( _R_ ) _|[η][∗∗]_ ] _< ∞ for some η[∗∗] >_ 2 _._ 

**Assumption 9.** _Let φτ_ 1 _,τ_ 2 _,··· ,τν_ ( _·_ ) _be the joint probability density function of_ ( _R_ 1+ _τ_ 1 _, . . . , R_ 1+ _τν_ ) (1 _≤ l ≤_ 4) _. Then for all_ ( _τ_ 1 _, . . . , τν_ ) _, φτ_ 1 _,τ_ 2 _,...,τν_ ( _·_ ) _exists and satisfies a Lipschitz condition: |φτ_ 1 _,τ_ 2 _,...,τν_ ( _r_ 1 + _v_ 1 _, . . . , rν_ + _vν_ ) _− φτ_ 1 _,τ_ 2 _,...,τν_ ( _r_ 1 _, . . . , rν_ ) _| ≤ Dτ_ 1 _,τ_ 2 _,...,τν_ ( _r_ 1 _, . . . , rν_ ) _∥v∥, where Dτ_ 1 _,τ_ 2 _,··· ,τν_ ( _·_ ) _is integrable and satisfies the conditions that_ � _Dτ_ 1 _,τ_ 2 _,...,τν_ ( _r_ 1 _, . . . , rν_ ) _∥r∥_[2] _[ι] dr <_ Ξ _< ∞ and_ � _Dτ_ 1 _,τ_ 2 _,...,τν_ ( _r_ 1 _, . . . , rν_ ) _φτ_ 1 _,τ_ 2 _,··· ,τν_ ( _r_ 1 _, . . . , rν_ ) _dr <_ Ξ _< ∞ for some ι >_ 1 _and constant_ Ξ _>_ 0 _._ 

**Assumption 10.** _(i) ∇p_ ( _M_ ; _·_ ) _and ∇_[2] _p_ ( _M_ ; _·_ ) _are continuous in M and dominated by a function (say Gp_ ( _M_ ) _) with finite second moments, where ∇p_ ( _M_ ; _·_ ) _and ∇_[2] _p_ ( _M_ ; _·_ ) _are r ×_ 1 _vector of first order partial derivatives and r × r matrix of second partial derivatives of_ 

12 

_p_ ( _M_ ; _θ_ ) _with respect to θ, respectively. (ii) E_ [ _∇p_ ( _M_ ; _θ_ ) _∇[′] p_ ( _M_ ; _θ_ )] _is nonsingular for θ in a neighborhood of the true value θ_ 0 _._ 

**Assumption 11.** _L_ 1( _·_ ) _and L_ 2( _·_ ) _are nonnegative second order and symmetric kernel functions. Furthermore, L_ 1( _·_ ) _has bounded first order derivative._ 

**Assumption 12.** _The smoothing parameter ℓ satisfies ℓ_ = _O_ ( _N[−][δ]_[¯] ) _for some_ 0 _< δ_[¯] _<_ 7 _/_ (8 _κ_ ) _._ **Assumption 13.** _The estimator θ_[�] _N satisfies ∥θ_[�] _N − θ_ 0 _∥_ = _Op_ (1 _/√N_ ) _. Also, it is assumed that_ sup _m∈M_ �� _p_ ( _m_ ; � _θN_ ) _− p_ ( _m_ ; _θ_ 0)�� = _Op_ (1 _/√N_ ) _holds, where M is the support of Mt._ 

These assumptions are standard in both parametric and nonparametric literatures. Assumption 7(i) requires that the underlying process _{Bt, Pt, At}[N] t_ =1[is][absolutely][regular][with] a geometric decay rate and (ii) states that the residual _εt_ is a martingale difference. Assumption 8 includes some smoothness conditions on the second and fourth conditional moment functions of _εt_ and Assumption 9 contains some Lipschitz type conditions and moment conditions. Assumption 10(i) and (ii) are standard assumptions adopted in nonlinear regression models. Assumption 11 is a standard assumption on the kernel functions _L_ 1( _·_ ) and _L_ 2( _·_ ) and Assumption 12 is the condition on the smoothing parameter _ℓ_ which is slightly stronger than the usual conditions of _ℓ →_ 0 and _Nℓ[κ] →∞_ . Assumption 13 is known to hold for standard parametric estimation methods under reasonably mild regularity conditions. Under Assumptions 7 - 13, the asymptotic properties of the test statistic _VN_ above can be derived, formally stated in the following theorem with the detailed proof given in the Appendix. 

**Theorem 3.** _Under Assumptions 7 - 13, one has_ 

� _(1) Under H_ 0 _, V_[�] _N_ = _Nℓ[κ/]_[2] _VN /√_ 2 _σV →N_ (0 _,_ 1) _in distribution as N →∞, where_ 

**==> picture [294 x 37] intentionally omitted <==**

_is a consistent estimator of σV_[2] _[given][by]_ 

**==> picture [256 x 28] intentionally omitted <==**

_with σ_ �[2] ( _r_ ) = _E_ ( _ε_[2] _t[|][R][t]_[=] _[ r]_[)] _[.]_ 

_(2) Under H_ 1 _, P_ ( _V_[�] _N > ON_ ) _→_ 1 _for any non-stochastic sequence ON_ = _o_ ( _Nℓ[κ/]_[2] ) _._ 

13 

## **3 Monte Carlo Studies** 

This section is devoted to examining the finite-sample performance of the proposed tests _UN_ and _VN_ through two Monte Carlo experiments. 

**Example 1.** In this example, we investigate the finite-sample performance of the test statistic _UN_ using the following data generating processes (DGP): 

**==> picture [154 x 13] intentionally omitted <==**

where _Yt_ ( _Bt_ ) = _αAt_ +0 _._ 5 _Yt−_ 1 +0 _._ 5 _Bt_ + _φt_ , _Bt_ = _I µ_ � _Yt_ (1)+ _Yt_ (0)� _/_ 2 _−_ �1 _− µ_[2] _/_ 2 _Yt−_ 1 _>_ � _ηt_ , _At_ = _ρAAt−_ 1 + _ut_ , _φt_ = _ρφφt−_ 1 + _υt_ , _ut_ , _υt_ and _ηt_ are mutually independent processes � _iid iid iid_ with _ut ∼N_ (0 _,_ 0 _._ 5[2] ), _υt ∼N_ (0 _,_ 0 _._ 3[2] ) and _ηt ∼ unif_ (0 _,_ 1). We consider _ρA ∈{_ 0 _._ 2 _,_ 0 _._ 8 _}_ , _ρφ ∈{_ 0 _._ 2 _,_ 0 _._ 8 _}_ and _α ∈{_ 0 _._ 3 _,_ 0 _._ 9 _}_ . However, the constant _µ ∈_ [0 _,_ 1] are allowed to vary in various setups. It can be checked that the auxiliary variable _At_ always satisfies Assumption 2 in Section 2 regardless of any values of _µ_ taking. The CI assumption is satisfied only when _µ_ = 0. Here the constant _α_ is used to capture the correlation between the auxiliary variable _At_ and the potential outcomes _Yt_ (1) and _Yt_ (0). In this example, the standard normal kernel functions are used for both L[(1)] ( _·_ ) and _L_ ( _·_ ) and the bandwidths are set to be _a_ 1 = � _σM N[−]_[1] _[/]_[5] , � � � � _aM_ = _c_ 1 _· σM N[−]_[1] _[/]_[4] and _aA_ = _c_ 1 _· σAN[−]_[1] _[/]_[4] , where _σM_ and _σA_ are the sample standard deviations of _{Mt}[N] t_ =1[with] _[M][t]_[=] _[Y][t][−]_[1][and] _[{][A][t][}][N] t_ =1[,][respectively.][To][investigate][the][effects] of different values of the bandwidths on the test _UN_ , we consider _c_ 1 = 0 _._ 5, 1 _._ 0 and 2 _._ 0, respectively. To obtain the empirical test size, the simulation is repeated 1 _,_ 000 times for each setting and then, the empirical size is estimated by just the empirical rejection rate of _UN_ based on the 1 _,_ 000 replications. Finally, Table 1 reports the estimated sizes for all settings considered. 

From Table 1, it can be observed that the finite sample performance of the test _UN_ is pretty good in different situations considered. In particular, the test _UN_ performs well in most cases considered as the sample size increases to 400. In addition, one also can observe from Table 1 that in all cases, both the autocorrelation coefficients ( _ρA_ and _ρφ_ ) and the correlation of the potential outcomes and the auxiliary variable captured by _α_ have little 

14 

Table 1: Estimated sizes of _UN_ (nominal size _α_ 0 = 5%) 

||Model<br>_α_<br>0.3<br>0.9|Empirical rejection probability of _UN_ with|Empirical rejection probability of _UN_ with|
|---|---|---|---|
|_ρA_<br>0.2<br>0.8||_c_1 = 0_._5_, ρφ_ = 0_._2<br>_N_ = 100<br>_N_ = 200<br>_N_ = 400<br>0.032<br>0.036<br>0.050<br>0.036<br>0.063<br>0.051|_c_1 = 0_._5_, ρφ_ = 0_._8|
||||_N_ = 100<br>_N_ = 200<br>_N_ = 400|
||||0.034<br>0.050<br>0.054<br>0.041<br>0.047<br>0.058|
||0.3<br>0.9|0.038<br>0.046<br>0.050<br>0.035<br>0.046<br>0.055|0.054<br>0.043<br>0.052<br>0.064<br>0.057<br>0.053|
|_ρA_<br>0.2<br>0.8|_α_<br>0.3<br>0.9|_c_1 = 1_._0_, ρφ_ = 0_._2<br>_N_ = 100<br>_N_ = 200<br>_N_ = 400<br>0.021<br>0.027<br>0.036<br>0.022<br>0.034<br>0.040|_c_1 = 1_._0_, ρφ_ = 0_._8|
||||_N_ = 100<br>_N_ = 200<br>_N_ = 400|
||||0.026<br>0.039<br>0.048<br>0.030<br>0.036<br>0.044|
||0.3<br>0.9|0.022<br>0.032<br>0.039<br>0.028<br>0.035<br>0.044|0.030<br>0.034<br>0.045<br>0.033<br>0.038<br>0.059|
|_ρA_<br>0.2<br>0.8|_α_<br>0.3<br>0.9|_c_1 = 2_._0_, ρφ_ = 0_._2<br>_N_ = 100<br>_N_ = 200<br>_N_ = 400<br>0.016<br>0.028<br>0.038<br>0.018<br>0.022<br>0.036|_c_1 = 2_._0_, ρφ_ = 0_._8|
||||_N_ = 100<br>_N_ = 200<br>_N_ = 400|
||||0.012<br>0.022<br>0.033<br>0.014<br>0.028<br>0.037|
||0.3<br>0.9|0.017<br>0.024<br>0.035<br>0.015<br>0.028<br>0.032|0.018<br>0.030<br>0.035<br>0.015<br>0.021<br>0.034|



effects on the size performance. When the sample size is reasonably large, say _N_ = 400, and the bandwidth is not too large, for example _c_ 1 = 0 _._ 5 or _c_ 1 = 1 _._ 0, the size performances are very well. However, the test is conservative when the bandwidth becomes too large. 

Next, Figure 1 presents the estimated power curves of the _UN_ test for different bandwidths (the top panel for _c_ 1 = 0 _._ 5, the middle panel for _c_ 1 = 1 _._ 0 and the bottom panel for _c_ 1 = 2 _._ 0). It can be observed from Figure 1 that the test _UN_ is quite powerful in detecting alternatives in all cases considered in general. Also as expected we observe that the powers of the test _UN_ increase sharply when both the value of _µ_ and the sample size increase. It is also noticed from these figures that the larger is the value of bandwidth _a_ , the larger is the power of the _UN_ test. This result can be explained by the fact that the test _UN_ diverges to infinite at the 

15 

**==> picture [442 x 462] intentionally omitted <==**

**----- Start of picture text -----**<br>
α = 0.3 α = 0.9<br>n=200 n=200<br>n=400 n=400<br>0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0<br>µ µ<br>α = 0.3 α = 0.9<br>n=200 n=200<br>n=400 n=400<br>0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0<br>µ µ<br>α = 0.3 α = 0.9<br>n=200 n=200<br>n=400 n=400<br>0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0<br>µ µ<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>Empirical Rejection Rate Empirical Rejection Rate<br>0.0 0.0<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>Empirical Rejection Rate Empirical Rejection Rate<br>0.0 0.0<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>Empirical Rejection Rate Empirical Rejection Rate<br>0.0 0.0<br>**----- End of picture text -----**<br>


Figure 1: Estimated power curves for test statistic _UN_ with nominal size _α_ 0 = 5%, _ρA_ = 0 _._ 5, _ρφ_ = 0 _._ 5 and different bandwidths (the top panel for _c_ 1 = 0 _._ 5, the middle panel for _c_ 1 = 1 _._ 0 and the bottom panel for _c_ 1 = 2 _._ 0). 

rate of _Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] under _H_ 1. Therefore, a larger _a_ value (in certain range) should lead to a more powerful test against fixed alternatives. However, this does not mean that one should always prefer a large value of _a_ in practice, since there is a tradeoff between powers and sizes for different values of the bandwidth, as one can see in Table 1 for size performance with different choices of the bandwidth _a_ . 

16 

**Example 2.** In this example, we examine the finite sample performance of the test statistic _VN_ . Similar to Example 1, we consider the following time series data generating process: 

**==> picture [154 x 13] intentionally omitted <==**

**==> picture [424 x 74] intentionally omitted <==**

_At_ = _ϖAAt−_ 1 + _ψt_ , _ϵt_ = _ϖϵϵt−_ 1 + _ϑt_ , _M_ 1 _,t_ = 0 _._ 5 _M_ 1 _,t−_ 1 + _ω_ 1 _,t_ , _M_ 2 _,t_ = 0 _._ 6 _M_ 2 _,t−_ 1 + _ω_ 2 _,t_ , and _iid iid ψt_ , _ϑt_ , _ξt_ , _ω_ 1 _,t_ and _ω_ 2 _,t_ are mutually independent processes with _ψt ∼N_ (0 _,_ 0 _._ 5[2] ), _ϑt ∼ iid iid iid N_ (0 _,_ 0 _._ 3[2] ), _ω_ 1 _,t ∼N_ (0 _,_ 0 _._ 4[2] ), _ω_ 2 _,t ∼N_ (0 _,_ 0 _._ 4[2] ) and _ξt ∼_ unif(0 _,_ 1). Again, we consider _ϖA ∈{_ 0 _._ 2 _,_ 0 _._ 8 _}_ , _ϖε ∈{_ 0 _._ 2 _,_ 0 _._ 8 _}_ , _ϕ ∈{_ 0 _._ 3 _,_ 0 _._ 9 _}_ and allow the constant _ν ∈_ [0 _,_ 1] to change in various simulation experiments. Also, it is easy to check that the auxiliary variable _At_ always satisfies Assumption 2 in Section 2 regardless of any values of _ν_ taking and the CI assumption is satisfied only when _ν_ = 0. In this example, the correlation between the auxiliary variable _At_ and the potential outcomes _Yt_ (1) and _Yt_ (0) is captured by the constant _ϕ_ . Similarly, to examine the effects of different values of the bandwidth _ℓ_ on the test _VN_ , we consider _ℓ_ = _c_ 2 _· N[−]_[1] _[/]_[5] with _c_ 2 = 0 _._ 5, 1 _._ 0 and 2 _._ 0, respectively. Finally, the simulation is repeated 1 _,_ 000 times for each setting to estimate the empirical test size. 

Table 2 reports the estimated sizes for _VN_ test for various cases, from which it can be seen that both the autocorrelation coefficients ( _ϖA_ and _ϖϵ_ ) and the correlation of the potential outcomes and the auxiliary variable have little effects on the size performance of the test _VN_ . Again, when the sample size increases to _N_ = 400 and the bandwidth is not too large, for example _c_ 2 = 0 _._ 5 or _c_ 2 = 1 _._ 0, the size performances are reasonably well. Similar to Table 1, the test is conservative when the bandwidth becomes too large. Next, Figure 2 presents the estimated power curves for _VN_ test for different bandwidths (the top panel for _c_ 2 = 0 _._ 5, the middle panel for _c_ 2 = 1 _._ 0 and the bottom panel for _c_ 2 = 2 _._ 0). Clearly, the same pattern as seen in the first example can be observed. Specifically, when the value of _ν_ and the sample size increase, the estimated powers also increase sharply. Moreover, one also can observe 

17 

Table 2: Estimated sizes of _VN_ (nominal size _α_ 0 = 5%) 

||Model<br>_ϕ_<br>0.3<br>0.9|Empirical rejection probability of _VN_ with|Empirical rejection probability of _VN_ with|
|---|---|---|---|
|_ϖA_<br>0.2<br>0.8||_c_2 = 0_._5_, ϖϵ_ = 0_._2<br>_N_ = 100<br>_N_ = 200<br>_N_ = 400<br>0.030<br>0.035<br>0.046<br>0.030<br>0.040<br>0.045|_c_2 = 0_._5_, ϖϵ_ = 0_._8|
||||_N_ = 100<br>_N_ = 200<br>_N_ = 400|
||||0.033<br>0.043<br>0.046<br>0.030<br>0.036<br>0.044|
||0.3<br>0.9|0.042<br>0.047<br>0.053<br>0.030<br>0.036<br>0.047|0.035<br>0.039<br>0.045<br>0.036<br>0.040<br>0.049|
|_ϖA_<br>0.2<br>0.8|_ϕ_<br>0.3<br>0.9|_c_2 = 1_._0_, ϖϵ_ = 0_._2<br>_N_ = 100<br>_N_ = 200<br>_N_ = 400<br>0.025<br>0.031<br>0.036<br>0.024<br>0.027<br>0.033|_c_2 = 1_._0_, ϖϵ_ = 0_._8|
||||_N_ = 100<br>_N_ = 200<br>_N_ = 400|
||||0.027<br>0.030<br>0.042<br>0.031<br>0.034<br>0.040|
||0.3<br>0.9|0.021<br>0.032<br>0.041<br>0.021<br>0.034<br>0.043|0.031<br>0.034<br>0.042<br>0.031<br>0.041<br>0.044|
|_ϖA_<br>0.2<br>0.8|_ϕ_<br>0.3<br>0.9|_c_2 = 2_._0_, ϖϵ_ = 0_._2<br>_N_ = 100<br>_N_ = 200<br>_N_ = 400<br>0.020<br>0.024<br>0.030<br>0.024<br>0.029<br>0.032|_c_2 = 2_._0_, ϖϵ_ = 0_._8|
||||_N_ = 100<br>_N_ = 200<br>_N_ = 400|
||||0.022<br>0.031<br>0.035<br>0.023<br>0.027<br>0.038|
||0.3<br>0.9|0.024<br>0.031<br>0.037<br>0.025<br>0.036<br>0.040|0.021<br>0.025<br>0.031<br>0.025<br>0.031<br>0.035|



that the power performance relies on the correlation between the potential outcomes and the auxiliary variable _At_ measured by _ϕ_ . 

## **4 A Real Example** 

Identifying the causal connection between monetary policy and real economic variables is one of the most significant and extensively investigated questions in macroeconomics. To answer this question, researchers usually regress an outcome variable of interest on measures of monetary policy, at the same time, controlling for lagged outcomes and contemporaneous and lagged covariates. Consequently, the statistical significance of policy variables provides the evidence on the existence of the causal connection between monetary policy and outcome 

18 

**==> picture [442 x 463] intentionally omitted <==**

**----- Start of picture text -----**<br>
φ = 0.3 φ = 0.9<br>n=200 n=200<br>n=400 n=400<br>0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0<br>ν ν<br>φ = 0.3 φ = 0.9<br>n=200 n=200<br>n=400 n=400<br>0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0<br>ν ν<br>φ = 0.3 φ = 0.9<br>n=200 n=200<br>n=400 n=400<br>0.2 0.4 0.6 0.8 1.0 0.2 0.4 0.6 0.8 1.0<br>ν ν<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>Empirical Rejection Rate Empirical Rejection Rate<br>0.0 0.0<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>Empirical Rejection Rate Empirical Rejection Rate<br>0.0 0.0<br>1.0 1.0<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>Empirical Rejection Rate Empirical Rejection Rate<br>0.0 0.0<br>**----- End of picture text -----**<br>


Figure 2: Estimated power curves for test statistic _VN_ with nominal size _α_ 0 = 5%, _ϖA_ = 0 _._ 5, _ϖϵ_ = 0 _._ 5 and different bandwidths (the top panel for _c_ 2 = 0 _._ 5, the middle panel for _c_ 2 = 1 _._ 0 and the bottom panel for _c_ 2 = 2 _._ 0). 

variable of interest. Two of the most leading empirical studies in this spirit are the papers by Sims (1972, 1980), in which the author discussed the conceptual as well as empirical problems in the money-income nexus. 

To apply the procedure of the regression-based causality tests, researchers need a simple conditional independence assumption. That is, in the language of cross-sectional policy 

19 

evaluation, researchers need to assume that given lagged outcomes and a suitable set of control variables, policy variables are “as good as randomly assigned”, so that conditional effects have a causal interpretation. While the conditional independence assumption is a strong assumption, it is the foundation of beginning empirical work, at least in the absence of a true randomized trial or a convincing exclusion restriction. Although the approach of regression-based causality tests provides a flexible tool to analyze the causal relationships between monetary policy and real economic variables, an important drawback of this approach is that it typically needs an array of additional assumptions which are hard to appraise and explain, especially in the time series setting. Another drawback of the regression tests is that in addition to the linearity implicit in any regression test, researchers must choose conditioning variables, lag lengths, and impose assumptions that imply some sort of stationarity. To overcome these drawbacks, recently, Angrist and Kuersteiner (2011) suggested an alternative way to time series causality testing under the potential-outcomes framework. Different from the previous approaches, a major advantage of the procedure proposed in Angrist and Kuersteiner (2011) is that it shifts the focus away from modeling the process determining outcomes towards modeling the process determining policy decisions. More specifically, the procedure developed in Angrist and Kuersteiner (2011) only requires researchers to assume a model for the conditional probability of a policy shift, while leaving the model for outcome variables unspecified, so that this approach reduces the modeling burden to the specification, identification, and estimation of the structural policy innovation and thus increases robustness. 

Motivated by the analysis of the Federal Open Market Committee decisions regarding the intended federal funds rate, Romer and Romer (2004) and Angrist and Kuersteiner (2011) applied some procedures to consider the causal effect of changes in the federal funds target rate, which tends to move up or down in quarter-point jumps. It is important to note that the application of the procedure in Angrist and Kuersteiner (2011) relies heavily on the conditional independence assumption which assumes that given a vector of variables which are derived from Federal Reserve forecasts of the growth rate of real GDP, the GDP deflator, and the unemployment rate, as well as a few contemporaneous variables and lags, 

20 

changes in the intended federal funds target are independent of potential outcomes (in this case, the monthly percent change in industrial production). However, as discussed before, the conditional independence assumption may be violated in practice and if this occurs, the testing results from applying the approach in Angrist and Kuersteiner (2011) may lead to misleading conclusion. Hence, it is important to test whether the conditional independence assumption is true or not before applying the method in Angrist and Kuersteiner (2011). In this paper, we revisit this example by focusing on testing whether the changes in the intended federal funds target are independent of the monthly percent change in industrial production conditional on a vector of variables. 

Similar to the analysis in Angrist and Kuersteiner (2011), our analysis of the real data used in Romer and Romer (2004)[2] also focuses on a discretized version of changes in the intended federal funds rate. Different from the treatment for the policy variable in Angrist and Kuersteiner (2011), here we treat policy variable as having two values. Specifically, if the present intended federal funds rate is up relative to the last period, the policy variable _Bt_ takes a value of 1 and 0 otherwise. In addition, we also use the same set of conditioning covariates as in the specification (a) in Angrist and Kuersteiner (2011). Specifically, the complete conditioning list includes the lagged change in the intended federal funds rate, plus the covariates graym, gray0, gray1, gray2, igrym, igry0, igry1, igry2, gradm, grad0, grad1, grad2, igrdm, igrd0, igrd1, igrd2, and the constructed unemployment innovation in Angrist and Kuersteiner (2011). Variable definitions are displayed in Table 3 below and further details are referred to Appendix E in Angrist and Kuersteiner (2011). Finally, we fit a logistic regression model with _Bt_ as the dependent variable and the estimation results are reported in Table 4. It can be seen from Table 4 that the covariates gray0, gray1, igrym, igry0, igry2, igrdm, igrd1 and the constructed unemployment innovation are highly insignificant with large _p_ -values, which motivates us to consider using these variables as 

> 2We use the same data set as in Angrist and Kuersteiner (2011), available via the Romer and Romer (2004) posting, downloadable at http://economics.mit.edu/faculty/angrist/data1/data/angrist1. Following Angrist and Kuersteiner (2011), our sample period starts in March 1969 and ends in December 1996. Data for estimation of the policy propensity score are organized by meeting month: only observations during months with Federal Open Market meetings are recorded. In the early part of the sample, the committee met twice in a month on occasion. These instances are treated as separate observations. 

21 

Table 3: Variable description 

|Variable names|Description|
|---|---|
|graym_t_|Greenbook forecast of the percentage change in real<br>GDP/GNP (at an annual rate) for the previous quarter|
|gray0_t_|Same as above, for current quarter|
|gray1_t_|Same as above, for one quarter ahead|
|gray2_t_|Same as above, for two quarter ahead|
||The innovation in the Greenbook forecast for the percentage change in|
|igrym_t_|GDP (at an annual rate) for the previous quarter from the meeting before.<br>The horizon of the forecast for the meeting before is adjusted so that the|
||forecasts for the two meetings always refer to the same quarter|
|igry0_t_|Same as above, for current quarter|
|igry1_t_|Same as above, for one quarter ahead|
|igry2_t_|Same as above, for two quarters ahead|
|gradm_t_|Greenbook forecast of the percentage change in the<br>GDP defator (at an annual rate) for the previous quarter|
|grad0_t_|Same as above, for current quarter|
|grad1_t_|Same as above, for one quarter ahead|
|grad2_t_|Same as above, for two quarters ahead|
||The innovation in the Greenbook forecast for the percentage change in|
|igrdm_t_|the GDP defator (at an annual rate) for the previous quarter from the<br>meeting before. The horizon of the forecast for the meeting before is adjusted|
||so that the forecasts for the two meetings always refer to the same quarter|
|igrd0_t_|Same as above, for current quarter|
|igrd1_t_|Same as above, for one quarter ahead|
|igrd2_t_|Same as above, for two quarters ahead|
|innovation_t_|Unemployment innovation|
|df_t_|Change in the intended federal funds rate|



the proper candidates for the auxiliary variable _At_ . Therefore, we apply our test _VN_ using these variables as the auxiliary variable _At_ to test whether the conditional independence assumption holds or not. 

Table 5 reports the testing results using gray0, gray1, igrym, igry0, igry2, igrdm, igrd1 or the constructed unemployment innovation as the auxiliary variable conditional on the remaining covariates. One can observe from Table 5 that for all cases considered, our test 

22 

Table 4: Estimation results 

||Covariates|Model<br>Intercept<br>graym<br>gray0<br>gray1<br>gray2<br>igrym<br>igry0<br>igry1<br>igry2<br>gradm<br>-1.414<br>-0.142<br>-0.033<br>-0.126<br>0.205<br>-0.002<br>0.154<br>0.871<br>-0.077<br>-0.518<br>0.050<br>0.073<br>0.808<br>0.615<br>0.390<br>0.991<br>0.494<br>0.015<br>0.849<br>0.007|
|---|---|---|
||Coefcients<br>_p_-value||
||Covariate|grad0<br>grad1<br>grad2<br>igrdm<br>igrd0<br>igrd1<br>igrd2<br>innovation df<br>0.582<br>-0.902<br>0.826<br>-0.284<br>-0.642<br>0.071<br>-0.872<br>-0.323<br>0.408<br>0.011<br>0.014<br>0.030<br>0.405<br>0.087<br>0.893<br>0.162<br>0.472<br>0.170|
||Coefcients<br>_p_-value||



can not reject the null hypothesis for different choices of auxiliary variables. Our results do not conclude that the conditional independence assumption is violated for this example so that the procedure in Angrist and Kuersteiner (2011) can be used to test the causal effect of changes in the federal funds target rate. 

Table 5: Testing results 

|Auxiliary|variable|gray0|gray1|igrym|igry0|igry2|igrdm|igrd1|igry1|innovation|
|---|---|---|---|---|---|---|---|---|---|---|
|_p_-value||0.816|0.891|0.860|0.911|0.868|0.620|0.910|0.876|0.846|



## **5 Conclusion** 

Conditional independence is a key identification assumption in economic policy evaluation. By using auxiliary variables, we adopt a nonparametric conditional moment test for testing conditional independence in a time series context. When the policy choice is binary, we further develop an unconfoundedness test conditional on policy propensity score while the nonparametric test becomes implementable when the dimension of the observed controls is high. The asymptotic properties of the proposed statistics are provided and Monte Carlo simulations demonstrate that both test statistics have reasonable performance in finite samples. We finally apply our test procedure to revisit the empirical example of Angrist and Kuersteiner (2011). Our testing results support the identification assumption adopted in their paper. For future research, an open but challenging question is how to deal with the dimensionality problem in a general case that the policy choice is not binary. 

23 

It is of interest to investigate other type tests such as the testing procedures proposed in Donald et al. (2014) and Chen et al. (2018) for time series data and our results may be applicable to the aforementioned testing procedures. This extension is left as a future research topic. 

## **References** 

- Angrist, J. D., Jordà, Ò., and Kuersteiner, G. M. (2018). Semiparametric estimates of monetary policy effects: String theory revisited. _Journal of Business & Economic Statistics_ , 36(3):371–387. 

- Angrist, J. D. and Kuersteiner, G. M. (2011). Causal effects of monetary shocks: Semiparametric conditional independence tests with a multinomial propensity score. _Review of Economics and Statistics_ , 93(3):725–747. 

- Breunig, C. (2019). Testing missing at random using instrumental variables. _Journal of Business & Economic Statistics_ , 37(2):223–234. 

- Chen, T., Ji, Y., Zhou, Y., and Zhu, P. (2018). Testing conditional mean independence under symmetry. _Journal of Business & Economic Statistics_ , 36(4):615–627. 

- Dette, H. and Spreckelsen, I. (2004). Some comments on specification tests in nonparametric absolutely regular processes. _Journal of Time Series Analysis_ , 25(2):159–172. 

- Donald, S. G., Hsu, Y.-C., and Lieli, R. P. (2014). Testing the unconfoundedness assumption via inverse probability weighted estimators of (L)ATT. _Journal of Business & Economic Statistics_ , 32(3):395–415. 

- Fan, Y. and Li, Q. (1996). Consistent model specification tests: omitted variables and semiparametric functional forms. _Econometrica_ , 64(4):865–890. 

- Fan, Y. and Li, Q. (1999). Central limit theorem for degenerate u-statistics of absolutely regular processes with applications to model specification testing. _Journal of Nonparametric Statistics_ , 10(3):245–271. 

- Fang, Y., Tang, S., Cai, Z., and Lin, M. (2020). An alternative test for conditional unconfoundedness using auxiliary variables. _Economics Letters_ , 194:109320. 

24 

- Guo, X., Wang, T., and Zhu, L. (2016). Model checking for parametric single-index models: a dimension reduction model-adaptive approach. _Journal of the Royal Statistical Society: Series B_ , 78(5):1013–1035. 

- Hjellvik, V., Yao, Q., and Tjøstheim, D. (1998). Linearity testing using local polynomial approximation. _Journal of Statistical Planning and Inference_ , 68(2):295–321. 

- Hu, Y. and Schennach, S. M. (2008). Instrumental variable treatment of nonclassical measurement error models. _Econometrica_ , 76(1):195–216. 

- Jordà, Ò. and Taylor, A. M. (2016). The time for austerity: estimating the average treatment effect of fiscal policy. _Economic Journal_ , 126(590):219–255. 

- Lavergne, P. and Vuong, Q. (2000). Nonparametric significance testing. _Econometric Theory_ , 16(4):576–601. 

- Li, Q. (1999). Consistent model specification tests for time series econometric models. _Journal of Econometrics_ , 92(1):101–147. 

- Li, Q. and Racine, J. S. (2007). _Nonparametric Econometrics: Theory and Practice_ . Princeton, NJ: Princeton University Press. 

- Liu, Z., Cai, Z., Fang, Y., and Lin, M. (2020). Statistical analysis and evaluation of macroeconomic policies: A selective review. _Applied Mathematics-A Journal of Chinese Universities_ , 35(1):57–83. 

- Robinson, P. M. (1988). Root- _n_ -consistent semiparametric regression. _Econometrica_ , 56(4):931–954. 

- Romer, C. D. and Romer, D. H. (2004). A new measure of monetary shocks: Derivation and implications. _American Economic Review_ , 94(4):1055–1084. 

- Rubin, D. B. (1974). Estimating causal effects of treatments in randomized and nonrandomized studies. _Journal of Educational Phycology_ , 66(5):688–701. 

- Sims, C. A. (1972). Money, income, and causality. _American Economic Review_ , 62(4):540– 552. 

- Sims, C. A. (1980). Macroeconomics and reality. _Econometrica_ , 48(1):1–48. 

- Zhao, J. and Shao, J. (2015). Semiparametric pseudo-likelihoods in generalized linear models with nonignorable missing data. _Journal of the American Statistical Association_ , 110(512):1577–1590. 

25 

## **A Mathematical Proofs** 

We first give the definitions of the class of kernel functions Υ _λ_ and the class of functions of U _[α]_[see][Robinson][(1988),][Fan][and][Li][(1996)][and][Li][(1999)][for][details.] _µ_[;] 

**Definition 2.** Υ _λ, λ ≥_ 1 _, is the class of even functions k_ : R _→_ R _satisfying_ 

**==> picture [204 x 28] intentionally omitted <==**

_and for some δ >_ 0 _,_ 

**==> picture [142 x 15] intentionally omitted <==**

_where δ is the Kronecher’s delta. ij_ 

**Definition 3.** U _[α] µ[,][α][>]_[0] _[,][µ][>]_[0] _[is][the][class][of][functions][g]_[:][R] _[p][→]_[R] _[satisfying:][g][is]_ ( _l −_ 1) _-times partially differentiable, for l −_ 1 _≤ µ ≤ l; for some ρ >_ 0 _, supy∈ϕzρ|g_ ( _y_ ) _− g_ ( _z_ ) _− Qg_ ( _y, z_ ) _|/|y − z|[µ] ≤ Dg_ ( _z_ ) _for all z, where ϕzρ_ = _{y_ : _|y − z| < ρ}; Qg_ = 0 _when l_ = 1 _; Qg is a_ ( _l −_ 1) _th degree homogeneous polynomial in y − z with coefficients being the partial derivatives of g at z of orders_ 1 _through l −_ 1 _when l >_ 1 _; and g_ ( _z_ ) _, its partial derivatives of order l −_ 1 _and less, and Dg_ ( _z_ ) _, have finite αth moments._ 

The remaining parts of this appendix provide proofs of the results stated in Section 2. Note that the letter _C_ denote a generic positive constant whose value can be different for various contexts. 

## **Proof of Theorem 1:** 

Recall that _αt_ = _Bt − E_ ( _Bt|Mt_ ) and 

**==> picture [192 x 37] intentionally omitted <==**

as well as 

**==> picture [292 x 38] intentionally omitted <==**

Denote _γt_ = _γ_ ( _Mt_ ) = _E_ ( _Bt|Mt_ ) and define 

**==> picture [290 x 37] intentionally omitted <==**

26 

and 

**==> picture [224 x 37] intentionally omitted <==**

� � � Then, _B_[�] _t_ = � _γt_ + � _αt_ . Using _αt_ = _Bt − B_[�] _t_ = ( _γt − γt_ ) + ( _αt − αt_ ), the test statistic _UN_ defined in Section 2 can be rewritten as 

**==> picture [381 x 104] intentionally omitted <==**

where _Lts_ is defined in Section 2. We shall complete the proof of Theorem 1 by investigating _UNi_ for _i_ = 1 _, . . . ,_ 6, respectively, in the following Lemmas 2 and 3. Since the proof is similar to that of Theorem 3.1 of Li (1999), we only provide some key steps. 

**Lemma 2.** _Under Assumptions 2 - 5, then,_ 

**==> picture [272 x 16] intentionally omitted <==**

_and_ 

**==> picture [414 x 16] intentionally omitted <==**

_Proof._ See Lemmas A.1, A.3, A.4, A.5 and A.6 in Li (1999). 

**Lemma 3.** _Suppose that Assumptions 2 - 5 are satisfied, then, D (i) Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] _UN_ 2 _−→N_ (0 _,_ 2 _σU_[2][)] _[,][where][σ] U_[2][=] _[ E]_ � _f_[2] ( _Mt_ ) _fG_ ( _Gt_ ) _σ_[4] ( _Gt_ )��� _L_[2] ( _v_ ) _dv_ � _._ � _(ii) σU_[2][=] _[ σ] U_[2][+] _[ o][p]_[(1)] _[.]_ 

_Proof._ (i) First note that _UN_ 2 can be rewritten as 

**==> picture [269 x 80] intentionally omitted <==**

27 

**==> picture [336 x 100] intentionally omitted <==**

Following Lemma A.2 in Li (1999), it can be known that _UN_[(] _[k]_ 2[)][=] _[o][p]_ �( _Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] ) _[−]_[1][�] for _k_ = 2 and 3. Hence, it remains to check the asymptotic normality of _Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] _UN_[(1)] 2[.][Similar] to the proof of Theorem 1 in Dette and Spreckelsen (2004), here we also apply Lemma 3.2 in Hjellvik, Yao and Tjøstheim (1998) for the degenerate _U_ -statistic to prove that _Na_[(] _[p]_[+] _[q]_[)] _[/]_[2] _UN_[(1)] 2[is][normally][distributed.] To do this, denote _ξt_ = ( _At, αt_ ), _P_ ( _ξs_ ), _P_ ( _ξs, ξt_ ), _P_ ( _ξs, ξt, ξl_ ), and let _P_ ( _ξs, ξt, ξl, ξk_ ) be the probability measures of _ξs_ , ( _ξs, ξt_ ), ( _ξs, ξt, ξl_ ) and ( _ξs, ξt, ξl, ξk_ ) for different _s, t, l, k ∈{_ 1 _, · · · , N }_ , respectively. Define _φst_ = _φst_ ( _ξt, ξs_ ) = _αtαsf_ ( _Mt_ ) _f_ ( _Ms_ ) _Lts/_ ( _N_ ( _N −_ 1) _a[p]_[+] _[q]_ ). It is easy to observe that _φst_ is a symmetric function on its arguments. Thus, _UN_[(1)] 2[=] � _φst_ = 2 � _φst_ is a degenerate _U_ -statistics. 1 _≤t_ = _s≤N_ 1 _≤s<t≤N_ Denote _σst_[2][=][ Var][(] _[φ][st]_[)][and] _[σ] N_[2][=] � _σst_[2][.][For][some][constant] _[δ][>]_[ 0][,][define] 1 _≤s<t≤N_ 

**==> picture [342 x 30] intentionally omitted <==**

**==> picture [454 x 181] intentionally omitted <==**

where the maximization over _P_ in the equation for _MN_ 4 is taken over the four probability measures _P_ ( _ξ_ 1 _, ξs, ξt, ξl_ ), _P_ ( _ξ_ 1) _P_ ( _ξs, ξt, ξl_ ), _P_ ( _ξ_ 1) _P_ ( _ξs_ ) _P_ ( _ξt, ξl_ ) and _P_ ( _ξ_ 1) _P_ ( _ξs_ ) _P_ ( _ξt_ ) _P_ ( _ξl_ ) for mutually different _s_ , _t_ , _l_ . It is assumed that all of the above constants are finite. 

28 

Based on Lemma 3.2 in Hjellvik et al. (1998), _σN[−]_[1] � _φst_ =[1] 2 _[σ] N[−]_[1] _[U]_[ (1)] _N_ 2[is][asymptoti-] 1 _≤s<t≤N_ cally normal with mean zero and variance one if for some _δ >_ 0, as _N →∞_ , 

**==> picture [455 x 30] intentionally omitted <==**

To this end, we only investigate the order of magnitude of _MN_[1] _[/]_ 1[(1+] _[δ]_[)] , because the other terms can be studied in a similar fashion. We first consider _MN_ 1. Define _ut_ = _αtf_ ( _Mt_ ) and _pst_ = _Lst/_ ( _N_ ( _N −_ 1) _a[p]_[+] _[q]_ ), then _φst_ = _utuspst_ . By applying Hölder’s inequality, it is easy to obtain that for some 0 _< δ <_ 1 and 1 _≤ s < t < l ≤ N_ 

**==> picture [410 x 59] intentionally omitted <==**

where 0 _< δ_ 1 _<_ 1 and 0 _< δ_ 2 _<_ 1, satisfying 1+1 _δ_ 1[+] 2(1+1 _δ_ 2)[=][1][and][1+] 3 _−[δ] δ[<][δ]_[1] _[<]_[1] 1+ _[−][δ] δ_[.][Note] that 

**==> picture [330 x 13] intentionally omitted <==**

so that 

**==> picture [362 x 33] intentionally omitted <==**

by Assumptions 3(iii) and 5(i). By straightforward calculations and by Assumption 4(ii), we can obtain that 

**==> picture [442 x 107] intentionally omitted <==**

where _f_ ( _u, v, r_ ) is the joint density function of ( _G_ 1 _, Gs, Gt_ ). Moreover, note that 

**==> picture [234 x 37] intentionally omitted <==**

29 

**==> picture [293 x 69] intentionally omitted <==**

where the last equality results from Lemma A.2(ii) in Li (1999). Consequently, for any 1 _< s < t ≤ N_ , we have 

**==> picture [436 x 34] intentionally omitted <==**

since _η <_ 2. 

We now consider the second term in _MN_ 1. To this end, denote _Ei_ and _Eij_ as the expectations with respect to _ξi_ and ( _ξi, ξj_ ), respectively. Then, we have 

**==> picture [501 x 141] intentionally omitted <==**

Therefore, 

**==> picture [418 x 37] intentionally omitted <==**

as _N →∞_ . Hence, the proof of _σN[−]_[2] _[N]_[ 2] _[M]_[ 1] _N[/]_ 1[(1+] _[δ]_[)] _→_ 0 is completed. 

For _MN_ 2, we only consider _E|φ_ 1 _tφst|_[2(1+] _[δ]_[)] and the other terms can be investigated similarly. It is noted that 

**==> picture [224 x 42] intentionally omitted <==**

where 2 _< ζ_ = 2(1 + _δ_ )(1 + _δ_ 1) _<_ 4, which implies that 

**==> picture [396 x 28] intentionally omitted <==**

30 

by the assumption that _Na[p]_[+] _[q] →∞_ . Similarly, it is not difficult to verify the results of other terms and details thus are omitted. Finally, by combining Lemmas 2 and 3, the proof of Theorem 1 is finished. 

**Proof of Theorem 2:** The proof is similar to that of Corollary 3.2 in Li (1999) and the details thus are omitted. 

## **Proof of Lemma 1:** 

_Proof._ Under Assumptions 1 and 2, we first show that 

**==> picture [429 x 15] intentionally omitted <==**

holds. Noting that _Bt_ is a binary variable, then for all _ν ≥_ 0 and for all _bj_ with _υ ∈_ Υ fixed, we have 

**==> picture [400 x 93] intentionally omitted <==**

Similarly, 

**==> picture [356 x 67] intentionally omitted <==**

Therefore, _P_ ( _Bt_ = 1 _|_ y _[υ] t,ν_[(] _[b][j]_[)] _[, p]_[(] _[M][t]_[)] _[, A][t]_[) =] _[ P]_[(] _[B][t]_[= 1] _[|]_[y] _[υ] t,ν_[(] _[b][j]_[)] _[, p]_[(] _[M][t]_[))][, which implies (6) holds.] Next, we show that (3) in Lemma 1 is true. To this end, Assumption 1 implies that 

**==> picture [400 x 22] intentionally omitted <==**

By (6), 

**==> picture [302 x 23] intentionally omitted <==**

31 

and thus, the law of iterated expectations yields 

**==> picture [389 x 23] intentionally omitted <==**

Therefore, a combination of (7) and (8) leads to 

**==> picture [224 x 23] intentionally omitted <==**

which implies _Bt_ is independent of _At_ conditional on _p_ ( _Mt_ ), and thus the proof of Lemma 1 is completed. 

## **Proof of Theorem 3:** 

� _Proof._ Define _ηt_ = _p_ ( _Mt_ ; _θ_ 0) _− p_ ( _Mt_ ; _θ_[�] _N_ ). We then have _εt_ = _Bt − p_ ( _Mt_ ; _θ_ 0) + _p_ ( _Mt_ ; _θ_ 0) _− p_ ( _Mt_ ; _θ_[�] _N_ ) = _εt_ + _ηt_ . Consequently, _VN_ can be rewritten as 

**==> picture [450 x 222] intentionally omitted <==**

We first consider _VN_ 1. To this end, rewrite _VN_ 1 = _VN_[(1)] 1[+] _[ V] N_[(2)] 1[,][where] 

**==> picture [372 x 37] intentionally omitted <==**

and 

**==> picture [328 x 37] intentionally omitted <==**

32 

**==> picture [230 x 30] intentionally omitted <==**

For _VN_[(1)] 1[,][similar][to][the][arguments][for][showing][Theorem][1][above,][we][can][show][that] 

where 

**==> picture [370 x 104] intentionally omitted <==**

is a consistent estimator of _σV_[2][given][by] 

**==> picture [256 x 27] intentionally omitted <==**

with _σ_[2] ( _r_ ) = _E_ ( _ε_[2] _t[|][R][t]_[=] _[r]_[)][and] _[f][R]_[(] _[·]_[)][being][the][density][function][of] _[R][t]_[=][(] _[p]_[(] _[M][t]_[)] _[, A][t]_[)][.][For] _VN_[(2)] 1[,][following][the][proof][of][Theorem][1][in][Guo,][Wang][and][Zhu][(2016),][the][Taylor][expansion] yields that 

**==> picture [396 x 68] intentionally omitted <==**

Let 

**==> picture [501 x 37] intentionally omitted <==**

It is easy to see that _VN[∗]_ 1[is][a][degenerate][U-statistic][with][kernel] 

**==> picture [527 x 27] intentionally omitted <==**

Hence, _Nℓ[κ/]_[2] _VN[∗]_ 1[=] _[O][p]_[(1)][.][By][combining] _[∥][θ]_[�] _[N][−][θ]_[0] _[∥]_[=] _[O][p]_[(1] _[/] √N_ ) and _Nℓ_[2] _→∞_ , one can obtain _Nℓ[κ/]_[2] _VN_[(2)] 1[=] _[ o][p]_[(1)][.] 

> [[(1)]][(2)][where] _N_ 2[+] _[ V] N_ 2[,] 

Now we deal with the term _VN_ 2. To do so, rewrite _VN_ 2 = _VN_[[(1)]] 2 

**==> picture [474 x 37] intentionally omitted <==**

33 

and 

**==> picture [374 x 73] intentionally omitted <==**

We first show that _VN_[(1)] 2[=] _[ o][p]_[((] _[Nℓ][κ/]_[2][)] _[−]_[1][)][,][which][can][be][established][by][the][similar][arguments] to the proof of Theorem 3.1 in Fan and Li (1999), so here we only provide some key steps. For simplicity of notation, denote Λ _ts_ = _L_ 2� _As−ℓ At_ � _L_ 1 _p_ ( _Ms_ ; _θ_ 0) _−ℓ p_ ( _Mt_ ; _θ_ 0) . By using _p_ ( _Ms_ ; _θ_[�] _N_ ) _−_ � � _p_ ( _Ms_ ; _θ_ 0) = _∇[′] p_ ( _Ms_ ; _θ_ 0)( _θ_[�] _N − θ_ 0) + 2[1][(] _[θ]_[�] _[N][−][θ]_[0][)] _[′][∇]_[2] _[p]_[(] _[M][s]_[;][ �] _[θ][N]_[)(] _[θ]_[�] _[N][−][θ]_[0][)][,][where] _[θ]_[�] _[N]_[is][between] � _θN_ and _θ_ 0, we obtain the following 

**==> picture [292 x 90] intentionally omitted <==**

where 

**==> picture [224 x 37] intentionally omitted <==**

and 

**==> picture [238 x 37] intentionally omitted <==**

For Ξ1 _N_ , let ( _a_ ) denotes the case of min _{|s − s[′] |, |s − t|, |s − t[′] |} > e_ , ( _b_ ) denotes the case of min _{|s − s[′] |, |s − t|, |s − t[′] |} ≤ e_ , where _e_ = [ _C_ log( _N_ )], and ∆ _t_ = _∇p_ ( _Ms_ ; _θ_ 0). Note that 

**==> picture [463 x 74] intentionally omitted <==**

by Assumption 9, where _η_ = (1 _− ξ[−]_[1] ) _[−]_[1] ( _ξ >_ 2 _,_ 1 _< η <_ 2). Then, 

**==> picture [360 x 31] intentionally omitted <==**

34 

**==> picture [361 x 80] intentionally omitted <==**

for some 1 _< η <_ 2, where _C >_ 4(1+ _δ_ ) _/_ ( _ηδ_ ). Therefore, _E_ ( _∥_ Ξ1 _N ∥_[2] ) = _o_ �( _N_ ( _N −_ 1) _ℓ[κ]_ ) _[−]_[2][�] + _O_ ( _e_ ( _Nℓ_[2] _[κ]_[(] _[η][−]_[1)] _[/η]_ ) _[−]_[1] ) and this implies Ξ1 _N_ = _op_ (( _N_ ( _N −_ 1) _ℓ[κ]_ ) _[−]_[1] )+ _Op_ � _e_[1] _[/]_[2] ( _N[−]_[1] _[/]_[2] _ℓ[−][κ]_[(] _[η][−]_[1)] _[/η]_ )�, which leads to ( _θ_[�] _N − θ_ 0) _[′]_ Ξ1 _N_ = _N[−]_[1] _[/]_[2] _op_ (( _N_ ( _N −_ 1) _ℓ[κ]_ ) _[−]_[1] ) + _Op_ � _e_[1] _[/]_[2] ( _N[−]_[1] _ℓ[−][κ]_[(] _[η][−]_[1)] _[/η]_ )� = _op_ (( _Nℓ[κ/]_[2] ) _[−]_[1] ) because 1 _< η <_ 2, _e_ = [ _C_ log( _N_ )] and _ℓ ∼ N[−][δ]_[¯] ( 8[7] _[κ][>][δ]_[¯] _[>]_[0)][.] It remains to evaluate the order of _A_ 2 _N_ . According to Assumption 10(i), it is easy to obtain that 

**==> picture [440 x 48] intentionally omitted <==**

for some 1 _< η <_ 2. Hence, ( _θ_[�] _N − θ_ 0) _[′]_ Ξ2 _N_ ( _θ_[�] _N − θ_ 0) = _Op_ (( _Nℓ_[(] _[η][−]_[1)] _[κ/η]_ ) _[−]_[1] ) = _op_ (( _Nℓ[κ/]_[2] ) _[−]_[1] ). By summarizing the above, we have shown that _VN_[(1)] 2[=] _[ o][p]_[((] _[Nℓ][κ/]_[2][)] _[−]_[1][)][.][Denote] 

**==> picture [489 x 77] intentionally omitted <==**

By following the same arguments for proving Theorem 1 in Guo et al. (2016), we have 

**==> picture [108 x 16] intentionally omitted <==**

Denote, 

**==> picture [474 x 38] intentionally omitted <==**

Then, by the similar arguments for proving _VN_[(1)] 2[=] _[ o][p]_[((] _[Nℓ][κ/]_[2][)] _[−]_[1][)][,][one][can][show][that] _[A][∗∗] N_[=] _op_ (( _Nℓ[κ/]_[2] ) _[−]_[1] ). By combining sup _m∈M_ �� _p_ ( _m_ ; � _θN_ ) _− p_ ( _m_ ; _θ_ 0)�� = _Op_ (1 _/√N_ ) and _Nℓ_[2] _→∞_ , it concludes that _VN_[(2)] 2[=] _[o][p]_[((] _[Nℓ][κ/]_[2][)] _[−]_[1][)][.][As][a][result,] _[V][N]_[2][=] _[o][p]_[((] _[Nℓ][κ/]_[2][)] _[−]_[1][)][.][Using][a][similar] argument for the term _VN_ 2 above, we also can show that _VN_ 3 = _op_ (( _Nℓ[κ/]_[2] ) _[−]_[1] ). Finally, we 

35 

deal with the term _VN_ 4. Rewrite it as 

**==> picture [408 x 133] intentionally omitted <==**

� By the mean value theorem and Assumption 10(i), �� _p_ ( _m_ ; � _θN_ ) _−p_ ( _m_ ; _θ_ 0)�� _≤ CGp_ ( _m_ ) _∥θN −θ_ 0 _∥_ . Hence, 

**==> picture [346 x 88] intentionally omitted <==**

because _E|_ ∆ _N |_ = _O_ (1) and _∥θ_[�] _N − θ_ 0 _∥_ = _Op_ (1 _/√N_ ). For the term _VN_[(2)] 4[, it is easy to see that] 

**==> picture [388 x 77] intentionally omitted <==**

A similar argument for proving _VN_[(1)] 4[and][Assumption][13][can][be][used][to][derive][that] _[V] N_[(2)] 4[=] _op_ (( _Nℓ[κ/]_[2] ) _[−]_[1] ). Consequently, _VN_ 4 = (( _Nℓ[κ/]_[2] ) _[−]_[1] ). Therefore, the proof of Theorem 3 is completed. 

36 

View publication stats 

