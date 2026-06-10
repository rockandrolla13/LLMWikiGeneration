# **Extreme Conformal Prediction: Reliable Intervals for High-Impact Events** 

Olivier C. Pasche[1,2,*] , Henry Lam[2] , and Sebastian Engelke[1] 

> 1 _Research Institute for Statistics and Information Science, University of Geneva, Switzerland_ 

> 2 _Department of Industrial Engineering and Operations Research, Columbia University, New York, USA_ 

> * _Corresponding author:_ `olivier.pasche@unige.ch` 

## **Abstract** 

Conformal prediction is a popular method to construct prediction intervals with marginal coverage guarantees from black-box machine learning models. In applications with potentially high-impact events, such as flooding or financial crises, regulators often require very high confidence for such intervals. However, if the desired level of confidence is too large relative to the amount of data used for calibration, then classical conformal methods provide infinitely wide, thus, uninformative prediction intervals. In this paper, we propose a new method to overcome this limitation. We bridge extreme value statistics and conformal prediction to provide reliable and informative prediction intervals with high-confidence coverage, which can be constructed using any black-box extreme quantile regression method. A weighted version of our approach can account for nonstationary data. The advantages of our extreme conformal prediction method are illustrated in a simulation study and in an application to flood risk forecasting. 

**Keywords:** conformal prediction, extreme value theory, prediction intervals, high confidence, generalized Pareto distribution, quantile regression. 

## **1 Introduction** 

Conformal prediction is a simple approach to producing prediction sets from any regression or classification model. For a covariate vector _𝑿_ with values in X ⊆ R _[𝑝]_ and corresponding response variable _𝑌_ , the goal of classical conformal prediction is to build a prediction set _𝐶_[ˆ] ( _𝒙_ ) satisfying marginal coverage 

P{ _𝑌_ test ∈ _𝐶_[ˆ] ( _𝑿_ test)} ≥ 1 − _𝛼,_ (1) 

for a desired confidence level 1 − _𝛼_ ∈(0 _,_ 1), for any new observations ( _𝑿_ test _,𝑌_ test). To obtain such a prediction set, we assume that a prediction model _𝑓_[ˆ] was fitted on a training data set from the distribution P of ( _𝑿,𝑌_ ), and that a new calibration data set ( _𝑿_ 1 _,𝑌_ 1) _,...,_ ( _𝑿𝑛𝑐 ,𝑌𝑛𝑐_ ) of _𝑛𝑐_ observations from the same distribution is available. For a specific nonconformity score function _𝑠_ : X × R → R that may depend on _𝑓_[ˆ] and acts on the predictors and responses, consider the ˆ calibration scores _𝑆𝑖_ = _𝑠_ ( _𝑿𝑖,𝑌𝑖_ ) for _𝑖_ = 1 _,...,𝑛𝑐_ . For some level _𝛼_ ∈(0 _,_ 1), denoting by _𝑞 𝛼_ the {⌈( _𝑛𝑐_ + 1)(1 − _𝛼_ )⌉/ _𝑛𝑐_ }-quantile of the scores _𝑆_ 1 _,...,𝑆𝑛𝑐_ , the prediction set 

ˆ ˆ _𝐶_ ( _𝒙_ ) = { _𝑦_ : _𝑠_ ( _𝒙, 𝑦_ ) ≤ _𝑞 𝛼_ } (2) 

1 

Extreme Conformal Prediction 

has the desired 1 − _𝛼_ coverage. That is, it satisfies Eq. (1) for any new test observation ( _𝑿_ test _,𝑌_ test) from the same distribution P, under a remarkably weak exchangeability assumption. This wellestablished framework is the so-called split conformal approach (Papadopoulos et al., 2002; Lei et al., 2018). More generally, originally started in Vovk et al. (1999, 2005), the conformalization idea that leverages quantile-based construction of prediction sets elicits a range of variants, with focus on optimal data usage and applying to different problems, including jackknife+ (Alaa and van der Schaar, 2020; Barber et al., 2021), cross-conformal prediction (Vovk, 2015) and ensemble-based approaches (Kim et al., 2020; Gupta et al., 2022). In combination with machine learning methods, it can efficiently capture predictive uncertainty (Shafer and Vovk, 2008; Zhou et al., 2025), and provide intervals with highly adaptive lengths (Romano et al., 2019). Extensions to nonexchangeable data are also well-studied (Oliveira et al., 2024). In particular, weighted conformal methods can account for distribution shifts and drifts (Tibshirani et al., 2019; Barber et al., 2023). 

Conformal prediction intervals are widely used for confidence levels 1 − _𝛼_ of moderate value relative to the sample size _𝑛𝑐_ (e.g., 90% and _𝑛𝑐_ = 1000), where enough of the calibration scores are above this quantile. In many applications, however, test points _𝑌_ test ∉ _𝐶_[ˆ] ( _𝑿_ test) that fall outside of the prediction set correspond to a high-impact event with serious consequences for the environment, human lives or the economy. Examples for such risk-sensitive applications are the protection of cities and energy infrastructure from flooding (Keef et al., 2009; Asadi et al., 2015) or the financial reserves of banks and insurance companies (van Oordt and Zhou, 2019; Dupuis et al., 2023). In these cases, much larger values of confidence 1 − _𝛼_ , close to one, will be required, sometimes even by law. Classical methods from conformal prediction fail for those requirements, since the quantile _𝑞_ ˆ _𝛼_ as defined above is not a useful estimator when the level _𝛼<_ 1/( _𝑛𝑐_ + 1). Indeed, in this case, less ˆ than one observation then exceeds the (1 − _𝛼_ )-quantile on average, and _𝑞 𝛼_ is infinite (or ill-defined). Even for slightly larger values _𝛼_ close to that limit, the variance of _𝑞_ ˆ _𝛼_ can be huge. 

Extreme value theory provides statistical tools for accurate estimation beyond the data range (de Haan and Ferreira, 2006). The tools have proven successful for improving extrapolation properties of machine learning methods in regression (de Carvalho et al., 2022a; Huet et al., 2024; Buriticá and Engelke, 2024), classification (Jalalzai et al., 2018), and generative methods (Boulaguiem et al., 2022). 

In this paper, we propose a new methodology that bridges the wide applicability of conformal prediction with extrapolation tools from extreme value statistics to construct reliable prediction sets for high-impact events. In a first step, in order to obtain a good pretrained model _𝑓_[ˆ] beyond the data range, we rely on flexible machine learning methods from extreme quantile regression (Velthoen et al., 2019; Gnecco et al., 2024; Pasche and Engelke, 2024; Richards and Huser, 2024). Second, we rely on the classical and theoretically justified peaks-over-threshold approach, which consists of using the generalised Pareto distribution (GPD) to extrapolate, for example, quantile estimates beyond the range of empirical observations (Balkema and de Haan, 1974; Pickands, 1975). For a confidence level 1 − _𝛼_ close to one, we leverage the GPD fitted to the calibration scores _𝑆_ 1 _,...,𝑆𝑛𝑐_ to obtain a reliable estimate of _𝑞 𝛼_ beyond the calibration data. The resulting extreme conformal prediction intervals have better properties compared to those from the classical empirical approach for large confidence requirements. In a simulation study, we show that our method improves existing approaches in terms of better coverage, in the sense of Eq. (1), and of informativeness of the prediction interval. We also consider a weighted version of our extreme conformal approach to deal with nonexchangeable data, and discuss its usage with several classical types of conformal procedures. 

The advantages of our approach are illustrated in an application to flood risk prediction. Using several of the flexible machine learning methods as base predictions, it provides high-confidence one-day-ahead interval forecasts of the conditional range for water flow. We show that using conformal prediction intervals based on extreme value theory improves the coverage of the classical 

2 

Extreme Conformal Prediction 

method, which either yields uninformative intervals or exhibits undercoverage and, therefore, seriously underestimates the risk of high-impact events. 

## **2 Background on conformal prediction** 

## **2.1 Split conformal prediction** 

As in the introduction, let _𝑿_ be a covariate vector taking values in X ⊆ R _[𝑝]_ , and _𝑌_ the response random variable of interest. We will consider, here and in the sequel, the regression case where the response _𝑌_ is real-valued in R. We also suppose that we have access to a calibration set of _𝑛𝑐_ observations ( _𝑿_ 1 _,𝑌_ 1) _,...,_ ( _𝑿𝑛𝑐 ,𝑌𝑛𝑐_ ). Classical split conformal prediction builds prediction intervals (PIs) as in Eq. (2) that have desired coverage under very weak assumptions. Specifically, if the joint distribution of the calibration set and the test point ( _𝑿_ test _,𝑌_ test) is exchangeable, then the unconditional coverage guarantee Eq. (1) holds (Papadopoulos et al., 2002). 

Importantly, the probability measure in Eq. (1) is with respect to the randomness in the calibration set jointly with the test point, that is, {( _𝑿_ 1 _,𝑌_ 1) _,...,_ ( _𝑿𝑛𝑐 ,𝑌𝑛𝑐_ ) _,_ ( _𝑿_ test _,𝑌_ test)}. In fact, when conditioning on the calibration set, the distribution of the coverage is a beta distribution, that is, 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0003-06.png)


Running the conformal prediction twice on different calibration sets, therefore yields PIs with different coverage probabilities. The guarantee in Eq. (1) says that when averaging out the calibration set, the coverage is at least 1 − _𝛼_ . 

Furthermore, the marginal coverage property in Eq. (1) only guarantees “overall” marginal coverage of the prediction set _𝐶_[ˆ] ( _𝒙_ ), but does not imply the conditional coverage property 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0003-09.png)


The latter is generally impossible to guarantee in such a general setting. How close _𝐶_[ˆ] ( _𝒙_ ) is to satisfying the conditional coverage property depends on the quality of the given pretrained model. For example, for the conformalized quantile regression approach described in Section 2.2, it depends on the accuracy of the initial quantile regression model _𝑄_[ˆ] _𝛼_ /2( _𝒙_ ) _, 𝑄_[ˆ] 1− _𝛼_ /2( _𝒙_ ). 

## **2.2 Conformalized quantile regression** 

Conformalized quantile regression, first proposed by Romano et al. (2019) and also described in Angelopoulos and Bates (2023), is one of the most popular conformal methods, in particular thanks to its ability to provide varying-length prediction intervals with competitive adaptivity. Suppose that we have access to a black-box quantile regression model trained to estimate the conditional quantiles _𝑄_[ˆ] _𝛼_ /2( _𝒙_ ) and _𝑄_[ˆ] 1− _𝛼_ /2( _𝒙_ ) of _𝑌_ , given _𝑿_ = _𝒙_ , at probability levels _𝛼_ /2 and 1 − _𝛼_ /2, respectively. Then, conformalized quantile regression uses the score function 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0003-13.png)


Following the general procedure described in the introduction, this leads to the final prediction set in Eq. (2) being the interval 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0003-15.png)


ˆ where _𝑞 𝛼_ is the empirical {⌈( _𝑛𝑐_ + 1)(1 − _𝛼_ )⌉/ _𝑛𝑐_ }-quantile of the calibration scores _𝑆_ 1 _,...,𝑆𝑛𝑐_ , ˆ i.e. the order statistic _𝑆_ (⌈( _𝑛𝑐_ +1) (1− _𝛼_ )⌉) . As an equivalent definition, _𝑞 𝛼_ equals the empirical 

3 

Extreme Conformal Prediction 

(1 − _𝛼_ )-quantile of { _𝑆_ 1 _,...,𝑆𝑛𝑐_ } ∪{+∞}, the calibration score sample augmented with a point at infinity. 

ˆ ˆ Intuitively, the procedure either widens (with a positive _𝑞 𝛼_ ) or narrows (with a negative _𝑞 𝛼_ ) ˆ ˆ the initial interval � _𝑄 𝛼_ /2( _𝒙_ ) _, 𝑄_ 1− _𝛼_ /2( _𝒙_ )� so that it covers ⌈( _𝑛𝑐_ + 1)(1 − _𝛼_ )⌉ of the _𝑛𝑐_ calibration observations. Note that the resulting prediction intervals satisfy the marginal coverage Eq. (1), but there is no guarantee that the conditional coverage in Eq. (4) is satisfied. In fact, the more accurate the initial quantile regression models _𝑄_[ˆ] _𝛼_ /2( _𝒙_ ) and _𝑄_[ˆ] 1− _𝛼_ /2( _𝒙_ ) are, the better the conditional coverage will be. 

## **2.3 Limitation for extreme confidence levels** 

For high-impact events, regulators often require predictions with very high coverage probabilities to ensure that protective infrastructures or measures are sufficient. In particular, in such risk-sensitive applications, the level _𝛼_ in Eq. (1) is typically close to 0 and may satisfy _𝛼<_ 1/( _𝑛𝑐_ + 1). This is generally referred to as an extreme confidence or probability level since, on average, there is less than one observation above the (1 − _𝛼_ )-quantile in a sample of size _𝑛𝑐_ . Note that the size _𝑛𝑐_ of the calibration set is typically fairly small, since these data cannot be used for model fitting, often resulting in extreme scenarios even for relatively moderate levels of _𝛼_ . 

The classical construction of the conformal prediction intervals described in the introduction ˆ requires the computation of _𝑞 𝛼_ , the empirical {⌈( _𝑛𝑐_ + 1)(1 − _𝛼_ )⌉/ _𝑛𝑐_ }-quantile of the calibration set scores. For extreme confidence levels 1 − _𝛼_ , this quantile level 

- ⌈( _𝑛𝑐_ + 1)(1 − _𝛼_ )⌉/ _𝑛𝑐 >_ ⌈ _𝑛𝑐_ ⌉/ _𝑛𝑐_ = 1 _,_ 

in which case _𝑞_ ˆ _𝛼_ is ill-defined and, by convention, set to infinity (Romano et al., 2019; Angelopoulos and Bates, 2023). This results in degenerate trivial prediction intervals _𝐶_[ˆ] ( _𝒙_ ) = (−∞ _,_ ∞), for all _𝒙_ ∈X. Although this interval satisfies the coverage Eq. (1), it is of no practical utility. 

## **3 Extreme conformal prediction** 

We propose an approach based on extreme value statistics to construct nondegenerate conformal prediction intervals at extreme confidence levels 1 − _𝛼> 𝑛𝑐_ /( _𝑛𝑐_ + 1). Similarly to classical conformalized quantile regression (Romano et al., 2019), our method requires two steps: 

1. fitting a quantile regression model at level 1 − _𝛼_ on a training data set of size _𝑛_ ; 

2. calibrating based on the scores _𝑆_ 1 _,...,𝑆𝑛𝑐_ on an independent data set. 

For extreme confidence levels, both steps typically require extrapolation beyond the data range. Indeed, if _𝛼_ is close to 0, and in particular if _𝛼<_ 1/( _𝑛_ + 1) is also extreme in the training data, then usual quantile regression will not be accurate. Instead, extreme quantile regression methods should be used. There is large literature on such methods based on linear models (Chernozhukov, 2005), additive models (Chavez-Demoulin and Davison, 2005; Youngman, 2019; de Carvalho et al., 2022b), or more flexible machine learning models such as gradient boosting (Velthoen et al., 2023; Koh, 2023), random forest (Gnecco et al., 2024) or neural networks (Pasche and Engelke, 2024; Richards and Huser, 2024; Allouche et al., 2024). Importantly, the model in step 1 can be a black-box, in the sense that we do not require theoretical guarantees. We discuss the extrapolation for step 2 in Section 3.2 and come back to examples of extreme quantile regression models in Sections 4 and 5. Furthermore, we discuss extensions of our approach to nonexchangeable data and alternative conformal procedures in Sections A.1 and 3.3. 

4 

Extreme Conformal Prediction 

## **3.1 Single-sided prediction intervals** 

Extreme conformal prediction intervals are most relevant in cases where very large values of the response variable _𝑌_ lead to severe negative impacts. In such cases, reliable prediction intervals for _𝑌_ | _𝑿_ = _𝒙_ , which contain the realisation of _𝑌_ with very high marginal probability, are a crucial forecasting tool. They can be used to determine whether a dangerous level of the response could potentially be reached. This also allows the reduction of false negatives (e.g., in the form of missing warnings) that can be critical to the system. In those risk assessment scenarios, it is often a single of the two tail directions which is of risk. This is the case for the risk of flooding discussed in Section 5 but also, for instance, for high temperatures in dry areas at risk of wildfires, and financial asset returns at risk of large losses. Without loss of generality, we, thus, suppose that one is interested in single-sided prediction intervals; two-sided intervals can be constructed analogously. 

The classical procedure, yielding two-sided intervals, can be adapted to obtain single-sided prediction intervals by using the score function 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0005-04.png)


instead of Eq. (5), where _𝑄_[ˆ] 1− _𝛼_ ( _𝒙_ ) is the pretrained quantile regression model at level 1 − _𝛼_ . Let _𝑦_ min ∈ R ∪{−∞} be the lower endpoint of the distribution of _𝑌_ (or of the conditional distribution _𝑌_ | _𝑿_ = _𝒙_ , if known). Then, following the usual procedure, the resulting interval is 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0005-06.png)


ˆ where _𝑞 𝛼_ is, in classical conformal prediction, the {⌈( _𝑛𝑐_ + 1)(1 − _𝛼_ )⌉/ _𝑛𝑐_ }-quantile of the calibration scores _𝑆_ 1 _,...,𝑆𝑛𝑐_ , i.e., the order statistic _𝑆_ (⌈( _𝑛𝑐_ +1) (1− _𝛼_ )⌉) . 

## **3.2 Calibrative extrapolation** 

As discussed in Section 2.3, when an extreme confidence level 1 − _𝛼> 𝑛𝑐_ /( _𝑛𝑐_ + 1) is required, using order statistics to estimate _𝑞_ ˆ _𝛼_ would lead to degenerate intervals. Therefore, an alternative approach is needed to estimate a finite value _𝑞_ ˆ _[𝑒] 𝛼_[from the calibration set such that] 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0005-10.png)


Substituting _𝑞_ ˆ _[𝑒] 𝛼_[for] _[𝑞]_[ˆ] _[𝛼]_[in][ Eq. (2)][ (or in][ Eqs. (6)][ and][ (8)][) would, then, yield nondegenerate prediction] intervals that satisfy the marginal coverage guarantee in Eq. (1). We propose to rely on the classical peaks-over-threshold methodology from extreme value theory to find such a quantile estimate. The tail of the distribution of the calibration score _𝑆_ := _𝑠_ ( _𝑿,𝑌_ ) can be approximated by the generalized Pareto distribution (GPD) above a high threshold _𝑢_ by 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0005-12.png)


where _𝜉_ ∈ R and _𝜎_ ( _𝑢_ ) _>_ 0 are the shape and scale parameters and _𝑢_ is an intermediate threshold. Under very mild assumptions on the distribution _𝐹𝑆_ of _𝑆_ , this approximation is theoretically justified as _𝑢_ tends to the upper endpoint of _𝐹𝑆_ (Balkema and de Haan, 1974; Pickands, 1975). In practice, _𝑢_ is typically chosen as the empirical _𝜏_ 0-quantile _𝑄_[ˆ] _𝜏_ 0 of _𝑆_ , for _𝜏_ 0 = (1 − _𝑘_ / _𝑛𝑐_ ) and some _𝑘< 𝑛𝑐_ . The tuning parameter _𝑘_ is the number of exceedances used for estimation of the parameters _𝜎_ and _𝜉_ , for instance, by maximum likelihood. Quantiles of _𝑆_ can then be estimated at probability levels beyond the data range using the approximation 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0005-14.png)


5 

Extreme Conformal Prediction 

Theoretical guarantees of these estimators typically require that _𝑘_ →∞ and _𝑘_ / _𝑛𝑐_ → 0 as _𝑛𝑐_ →∞ to ensure the correct tradeoff between bias and variance; see de Haan and Ferreira (2006) for more details. 

Asymptotically, as _𝑛𝑐_ →∞ and under additional second-order conditions, using _𝑞_ ˆ _[𝑒] 𝛼_[:][=] _[𝑄]_[ˆ][GPD] 1− _𝛼_ would satisfy Eq. (9) with equality (in a suitable limiting sense as _𝜏_ 0 → 1). But, since the calibration sample is finite and the level _𝜏_ 0 fixed, _𝑄_[ˆ][GPD] 1− _𝛼_[can underestimate the true quantile due to estimation] and approximation biases, respectively (Roodman, 2018; Bücher and Zhou, 2021; Zeder et al., 2023). We, therefore, follow here a more conservative approach. Alternatively to choosing _𝑞_ ˆ _[𝑒] 𝛼_ as _𝑄_[ˆ][GPD] 1− _𝛼_[,][we may use the upper endpoint of a][(][1][ −] _[𝛼]_[2][)][-confidence interval for] _[𝐹] 𝑆_[−][1][(][1][ −] _[𝛼]_[1][)][,][the] (1 − _𝛼_ 1)-quantile of the calibration scores _𝑆_ , for two suitable levels _𝛼_ 1 _,𝛼_ 2 ∈(0 _,_ 1). The following proposition shows that, if this confidence interval has correct coverage, then the resulting extreme conformal prediction interval satisfies Eq. (1). 

**Proposition 3.1.** _Let 𝛼_ 1 _,𝛼_ 2 ∈(0 _,_ 1) _, and_ [ _𝐿𝑄,𝑈𝑄_ ] _be a_ (1 − _𝛼_ 2) _-confidence interval for 𝐹𝑆_[−][1][(][1][−] _[𝛼]_[1][)] _[,] the_ (1 − _𝛼_ 1) _-quantile of the calibration scores 𝑆. If the confidence interval has correct coverage, i.e._ P{ _𝐿𝑄_ ≤ _𝐹𝑆_[−][1][(][1][−] _[𝛼]_[1][) ≤] _[𝑈][𝑄]_[} ≥][1][−] _[𝛼]_[2] _[, and if]_ 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0006-04.png)



![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0006-05.png)



![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0006-06.png)


The proposition applies more broadly to other types of base predictions and nonconformity score functions than to those of conformalized quantile regression. Its proof is presented in Section A.2. 

A natural choice for _𝛼_ 1 and _𝛼_ 2 that satisfies Eq. (12) with equality is _𝛼_ 1 = _𝛼_ 2 = 1 −(1 − _𝛼_ )[1][/][2] , which is analogous to the Šidák correction (Šidák, 1967). Another notable choice is _𝛼_ 1 = _𝛼_ 2 = _𝛼_ /2, which is analogous to a Bonferroni correction (Bonferroni, 1936). Although the latter is, in this case, overconservative, the difference is negligible for small values of _𝛼_ . 

There are several well-studied approaches for obtaining extreme quantile confidence intervals (CI) using the GPD approximation (Coles, 2001; Davison and Hinkley, 1997; Davison et al., 2003; de Haan and Zhou, 2022), including the profile likelihood, the bootstrap and the normal-approximation delta method. The profile-likelihood CI typically represents the inherently asymmetrical uncertainty best and yields the most conservative CI upper endpoint. For very small _𝛼_ and small sample sizes, it sometimes suffers from numerical difficulties for estimating the CI’s upper endpoint. They arise as the derivative of the profile log-likelihood can get close to zero on its right-hand side, which sometimes makes finding the crosspoint between the profile curve and the chi-square confidence line numerically difficult. Slightly varying the value of the GPD threshold can sometimes solve the issue. The bootstrap approach comes in different variations, both for the sampling step (nonparametric, parametric) and for the aggregation step (basic, percentile, normal, etc.). We here consider the nonparametric bootstrap with percentile aggregation, as it is the most commonly used. The bootstrap can give reliable confidence intervals, but, compared to the profile-likelihood approach, its upper endpoint estimates might not always be conservative enough. Finally, the delta-method CI is computationally less expensive than the other two alternatives, but it provides intervals that are symmetric around the quantile estimate, which is not realistic for large quantiles. Moreover, it can also suffer from numerical instability issues, due to its matrix inversion step, and fail to yield meaningful CIs. These alternative extreme CI methods are further discussed and compared in Section 4. 

To summarise, when given a high confidence level 1 − _𝛼_ , above or close to _𝑛𝑐_ /( _𝑛𝑐_ + 1), our proposed extreme conformal prediction interval takes the form 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0006-11.png)


6 

Extreme Conformal Prediction 

where _𝑄_[ˆ] 1 _[𝑒]_ − _𝛼_[(·)][is a prefitted extreme quantile regression model and] _[𝑞]_[ˆ] _[𝑒] 𝛼_[is the upper endpoint of] an appropriate GPD profile-likelihood confidence interval for a high quantile of the calibration nonconformity scores, as discussed above. If a two-sided extreme PI is preferred, one can use the classical nonconformity scores from Eq. (5), instead of Eq. (7), to obtain 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0007-02.png)


where a second prefitted extreme quantile regression model _𝑄_[ˆ] _[𝑒] 𝛼_ /2[(·)][ is required for extrapolating] the lower-tail conditional quantiles. 

## **3.3 Extensions to other conformal approaches and nonexchangeable data** 

We introduce our extreme conformal prediction approach as a variant of the well-established split conformalized quantile regression, as its use of base quantile predictions naturally results in varying-length intervals, which, in addition to valid marginal coverage, can also achieve good conditional coverage (Romano et al., 2019; Angelopoulos and Bates, 2023), and as the split procedure is significantly less computationally costly than full-conformal or _𝑘_ -fold alternatives. Nevertheless, Theorem 3.1 applies more broadly, and our approach is, in principle, adaptable to other conformal approaches, including different base regression models and nonconformity scores, the alternative full-conformal and _𝑘_ -fold procedures, and weighted methods for nonexchangeable data. 

The extension to different base predictive models and scores is the most straightforward, as the extreme conformalization described in Section 3.2 is agnostic to their definitions. This includes the classical split-conformal approach, using a conditional-mean base regression model _𝜇_ ˆ ( _𝒙_ ), instead of the quantile predictions _𝑄_[ˆ] _𝛼_ /2( _𝒙_ ) _, 𝑄_[ˆ] 1− _𝛼_ /2( _𝒙_ ) (Papadopoulos et al., 2002; Papadopoulos, 2008; Lei et al., 2018), and its heteroscedastic variants (Papadopoulos et al., 2008, 2011; Lei et al., 2018). Although these alternatives would not require extreme quantile regression, they either yield fixed-length PIs or tend to underestimate conditional variability (Romano et al., 2019). The extension to full-conformal procedures (Vovk et al., 1999, 2005; Shafer and Vovk, 2008) is also straightforward, but requires repeating both the predictive model fit and our extreme conformalization from Section 3.2 for a dense grid of potential response values. Although it makes a more efficient use of the data than the split variant, it has an extremely high computational cost. The same applies, but less extremely, to _𝑘_ -fold approaches, such as Jackknife+/CV+ and cross-conformal prediction (Barber et al., 2021; Vovk, 2015). The extensions of our method to these alternative conformalisation approaches are described in more detail in Section A.1. 

Weighted conformal approaches allow for relaxing the exchangeability assumption to account, for example, for distribution shifts or drifts. In those approaches, each calibration observation is assigned a weight _𝑤𝑖_ ∈[0 _,_ 1], _𝑖_ = 1 _,...,𝑛𝑐_ , which reflects its similarity to the test observation, or more generally, the similarity between its score _𝑆𝑖_ and the test score _𝑆_ test. The classical empirical ˆ quantile of the calibration scores _𝑞 𝛼_ is then replaced by a weighted sample quantile. More precisely, ¯ it is redefined as the (1 − _𝛼_ )-quantile of the weighted empirical distribution _𝑤[𝑛]_[�] _𝑖[𝑛]_ = _[𝑐]_ 1 _[𝑤][𝑖][𝛿][𝑠][𝑖]_[+] _[𝑤]_[¯] _[𝑛][𝛿]_[∞][,] where _𝑤_ ¯ _[𝑛]_ = ([�] _𝑖[𝑛]_ = _[𝑐]_ 1 _[𝑤][𝑖]_[+][1][)][−][1][ and] _[ 𝛿][𝑥]_[is the Dirac measure at] _[ 𝑥]_[(][Barber et al.][,][ 2023][;][ Tibshirani et al.][,] 2019). As our proposed _𝑞_ ˆ _[𝑒] 𝛼_[from][ Section 3.2][ is, for extreme confidence levels, based on likelihood] inference, the natural analogous extension to nonexchangeable data would be to rely on weighted likelihood inference instead. Using the sample weights _𝑤𝑖_ ∈[0 _,_ 1], _𝑖_ = 1 _,...,𝑛𝑐_ , the procedure would remain the same as in Section 3.2, only using the weighted 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0007-08.png)


7 

Extreme Conformal Prediction 

instead of the classical GPD log-likelihood, to infer the (1 − _𝛼_ 2)-CI endpoint for _𝐹𝑆_[−] test[1][(][1][−] _[𝛼]_[1][)][.][This] weighted alternative should achieve a similar effect as classical weighted conformal prediction methods: proportionally use the calibration scores most similar to the test point during conformalization, to correct for nonexchangeable distribution drifts and shifts. This weighted extension is further discussed and applied in Section 5. 

## **4 Simulation study** 

## **4.1 Experimental setup** 

To assess the different conformalization methods, we perform a simulation study with several scenarios. The data is generated from 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0008-05.png)


with _𝜎_ ( _𝒙_ ) := 1 + 6 _𝜙_ ( _𝑥_ 1 _,𝑥_ 2), where _𝜙_ is the bivariate Gaussian density with correlation 0 _._ 9. We consider two scenarios for the noise variable _𝜀𝑌_ : a heavy-tailed Student _𝑡_ distribution _𝑡 𝛼_ ( _**𝒙**_ ) , with covariate-dependent tail index _𝛼_ ( _𝒙_ ) = 1/ _𝜉_ ( _𝒙_ ) := 7 · {1 + exp(4 _𝑥_ 1 + 1 _._ 2)}[−][1] + 3, and a light-tailed Gaussian N(0 _,_ 1) distribution. The former choice corresponds exactly to the generating process used in two extreme quantile regression benchmark studies (Velthoen et al., 2023; Pasche and Engelke, 2024). 

We consider several sizes for the calibration sets, with _𝑛𝑐_ ∈{10[3] _,_ 10[3] _[.]_[5] _,_ 10[4] } observations. For each calibration size, we repeat the experiments 100 times. We consider extreme PI confidence levels 1 − _𝛼_ , with _𝛼_ ∈{10[−][3] _,_ 10[−][3] _[.]_[5] _,_ 10[−][4] _,_ 10[−][4] _[.]_[5] _,_ 10[−][5] }. We consider three choices for the base quantile predictions _𝑄_[ˆ] 1 _[𝑒]_ − _𝛼_[(·)][:][the conditional-quantile ground truth and two different pretrained] extreme quantile regression models. The ground-truth choice aims at assessing the methods with ideal initial predictions. As all conformalization methods are translation invariant, adding first-order bias to the pretrained model would always lead to the same final PIs. For the first pretrained extreme quantile predictions, we use the extreme quantile regression neural networks (EQRN) model, as it performed best on this benchmark dataset (Pasche and Engelke, 2024), aiming at assessing our procedure with accurate but realistic initial predictions. The EQRN model is pretrained on 5,000 observations generated from Eq. (17). Its hyperparameters and architecture were selected based on validation GPD deviance with a grid search. Lastly, to investigate the performance of our extreme conformalization procedure for a poorly-performing model, which could happen in practice due to poor historical modelling choices, we also consider a linear GPD quantile model as base predictions. More precisely, we use linear quantile regression to obtain a conditional threshold _𝑢_ ˆ( _𝒙_ ), and model the exceedances with a GPD having a linear parametrization _𝜎_ = _𝜎_ 0 + _𝜎_ 1 _𝑥_ 1 + _𝜎_ 2 _𝑥_ 2 for its scale parameter. Although having the GPD extrapolation potential, its linear parametrization is a bad fit for the highly nonlinear dependence of _𝑌_ on _𝑿_ . Experiments with Gaussian-noise data were only performed with the ground-truth base predictions. 

For each calibration size, repetition, confidence level, and initial predictions, we perform the following conformalization procedures and assess their average population coverage on a separate test set of 10[6] observations. The methods compared for conformalization are: 

- GPD profile: _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ) from Eq. (14), using the GPD profile-likelihood CI for _𝑞_ ˆ _[𝑒]_ 

      - _𝛼_[.] 

- GPD bootstrap: _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ), using the GPD nonparametric bootstrap percentile CI for _𝑞_ ˆ _[𝑒]_ 

         - _𝛼_[.] 

- GPD delta: _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ), using the GPD delta-method CI for _𝑞_ ˆ _[𝑒]_ 

   - _𝛼_[.] 

- GPD simple: _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ), but using the simple GPD (1 − _𝛼_ )-quantile estimate of the calibration scores instead of the endpoint of a CI for _𝑞_ ˆ _[𝑒] 𝛼_[.] 

8 

Extreme Conformal Prediction 

   - Classical: Single-sided version of the classical split conformalized quantile regression (still using the extreme quantile predictions _𝑄_[ˆ] 1 _[𝑒]_ − _𝛼_[(·)][, for a fair comparison).] 

- Each of the GPD-based procedures use the empirical 0 _._ 95-quantile as the threshold _𝑢_ . 

## **4.2 Coverage results** 

Figure 1 shows the distribution of the computed test coverage for each considered conformalization method, confidence level, and calibration size, for the Student _𝑡_ noise and ground truth original predictions. The chosen confidence levels are particularly large relative to the size of the calibration sets. Hence, for most scenarios, _𝛼<_ 1/( _𝑛𝑐_ + 1). In those cases, the classical conformalization method always yields trivial infinite intervals. They have a coverage of 1, but are uninformative and of no practical use. On the other hand, the other methods, relying on peaks over threshold extrapolation instead of empirical quantiles, are able to yield finite PIs, even when _𝛼_ ≪ 1/( _𝑛𝑐_ + 1). 

The simple GPD estimates of the calibration-score (1 − _𝛼_ )-quantile do not seem to provide sufficient coverage with small calibration samples and for the larger confidence levels, likely due to the GPD estimation error or approximation biases. The other three methods, relying on the confidence intervals for the score quantiles (and Theorem 3.1), achieve much better coverage and, in most cases, satisfy Eq. (1) as their coverage is larger than 1 − _𝛼_ on average. However, those GPD CI-based methods seem consistently overconservative for lower confidence levels. 

In general, the profile likelihood method seems the most conservative, compared to the nonparametric bootstrap and delta method alternatives, as anticipated. It also satisfies the coverage guarantee in all scenarios. Its downside is the numerical difficulty, described in Section 3.2. With the implementation at hand, this issue arose, in the worst case, in 85% of the repetitions for _𝑛𝑐_ = 1000 and the lowest _𝛼_ value, but quickly decreased to, at most, 2% for _𝑛𝑐_ = 3163 and 0% for _𝑛𝑐_ = 10000. This instability is understandable in the former truly extreme case, as the confidence level is more than two orders of magnitude larger than the level for which PIs are obtainable with the classical conformal method and as the likelihood only relies on 50 observations to estimate a (1 − 5 · 10[−][6] )-confidence interval for a (1 − 5 · 10[−][6] )-quantile. However, this instability issue appears to often be resolved by slightly varying the choice of the GPD threshold, or of the _𝛼_ 1 and _𝛼_ 2 split. 

The bootstrap and delta-method approaches seem less overconservative for the more moderate _𝛼_ values, but slightly undercover in the scenarios with the lowest _𝛼_ values. Nevertheless, they still significantly outperform the simple GPD approach and the infinite classical PIs. Contrary to the profile likelihood approach, the bootstrap method never fails to provide finite estimates. On the other hand, the delta-method approach also suffers from stability issues with small calibration sizes, regardless of the confidence level. 

Figure A.1 in Section A.3 shows the same coverage distribution when the data-generating process has light-tailed Gaussian noise, instead of heavy-tailed Student _𝑡_ 4 noise. In comparison, all methods tend to result in significantly more conservative intervals in terms of the coverage. In particular, all three GPD CI-based approaches always result in more coverage than necessary. 

Figure 2 shows the coverage distributions for the EQRN predictions and Student _𝑡_ 4 noise. We observe that, although being accurate predictions of the conditional quantile, in terms of integrated squared error (Pasche and Engelke, 2024), the EQRN predictions, here, undercover when considered as a PI endpoint. Note that even very accurate quantile predictions are still likely to lead to undercoverage, as a local quantile underestimation typically leads to a larger coverage loss than the coverage gain from a local overestimation of the same amplitude, due to the generally decreasing probability density in the tails. The conformalization results closely match those for the ground-truth quantile predictions, although the coverage seems smaller for the largest confidence levels, for all methods. The scenario with _𝛼_ = 10[−][5] and the largest sample size is the only one for which the GPD profile approach seems to slightly undercover. All the other finite alternatives also 

9 

Extreme Conformal Prediction 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0010-01.png)


**----- Start of picture text -----**<br>
α = 10 [−][3] α = 10 [−][3.5] α = 10 [−][4] α = 10 [−][4.5] α = 10 [−][5]<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>Method<br>ClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profile<br>c =n<br> 1000<br>c =n<br> 3163<br>Test coverage<br>c =n<br> 10000<br>**----- End of picture text -----**<br>


Figure 1: Boxplots of the test coverage probability of the quantile PIs (analytically computed for a grid of test observation and averaged over X) for different conformalization methods, conformal confidence values 1 − _𝛼_ (columns, labelled with _𝛼_ ), and calibration sample sizes _𝑛𝑐_ (rows), for the Student _𝑡_ distributed noise and quantile ground-truth predictions. 

undercover for this largest confidence level. The CI-based extreme conformal prediction methods all outperform the original EQRN prediction in all scenarios. 

Figure A.2 in Section A.3 shows the same coverage distributions when using the poorly-fitting linear GPD quantile predictions, described in Section 4.1, instead of the EQRN model. The base predictions severely undercover, when used as PIs. We observe that, even with poor quantile modelling choices, in all considered scenarios, our extreme conformalization approach results in a mean test coverage always greater than the desired levels, in this case for all three GPD CI-based variants. Interestingly, the intervals seem overall more marginally conservative than with the EQRN base predictions. Thus, even with this choice of a poorly-fit base model, undoubtingly worsening local adaptivity and coverage, our method still results in nontrivial PIs consistently achieving sufficient marginal coverage. 

As a takeaway, our practical recommendation for conservative and informative high-confidence PIs is to use the profile-likelihood version of our method. In case it suffers from numerical issues and varying the GPD threshold or the _𝛼_ 1 and _𝛼_ 2 split slightly does not solve them (or if those are desired fixed), the bootstrap-based CI can be used instead. This combination results in the profile-likelihood conservativeness, in most scenarios, and avoids the cases of potential numerical difficulties by using the bootstrap estimate, which is still conservative enough in the majority of scenarios. We call this method the “GPD safeprofile” PI. Alternatively, considering the maximum of the bootstrap and delta-method PI endpoints as a replacement in unstable profile likelihood situations could be more conservative but might be less stable. 

10 

Extreme Conformal Prediction 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0011-01.png)


**----- Start of picture text -----**<br>
α = 10 [−][3] α = 10 [−][3.5] α = 10 [−][4] α = 10 [−][4.5] α = 10 [−][5]<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>Method<br>PredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profile<br>c =n<br> 1000<br>c =n<br> 3163<br>Test coverage<br>c =n<br> 10000<br>**----- End of picture text -----**<br>


Figure 2: Boxplots of the test coverage probability of the quantile PIs (analytically computed for a grid of test observation and averaged over X) for different conformalization methods, conformal confidence values 1 − _𝛼_ (columns, labelled with _𝛼_ ), and calibration sample sizes _𝑛𝑐_ (rows), for the Student _𝑡_ distributed noise and EQRN predictions. 

## **5 Application to flood risk forecasting** 

## **5.1 Description and aim** 

Flooding is one of the most impactful natural hazards in terms of infrastructure and economic damage, and of the endangerment of human lives. Methods from extreme value theory have proven successful for assessing flood risk and providing reliable worst-case scenarios (e.g., Katz et al., 2002; Keef et al., 2009; Asadi et al., 2018; Engelke and Hitz, 2020; Engelke and Ivanovs, 2021). 

In Switzerland, the Federal Office for the Environment (FOEN) monitors the river flow with numerous gauging stations throughout the river network. In its capital city, Bern, extreme water flow events of the Aare river led to several major floods, causing some of the most severe infrastructural and economic flooding damages recorded in the country. The main driver of strong water-flow events is the cumulative amount of upstream precipitation. In this study, we rely on the average daily discharge measures of the Aare river (in m[3] s[−][1] ) provided by the FOEN[1] , and on recordings of daily precipitation (in mm) at various meteorological stations, obtained from MeteoSwiss[2] . This version of the dataset was preprocessed and analysed in previous studies (Pasche et al., 2023; Pasche and Engelke, 2024). 

With our proposed extreme conformal approach, we aim to provide high-confidence one-dayahead interval forecasts of the conditional range for water flow. We rely on several extreme quantile regression models pretrained to forecast the one-day-ahead extreme quantiles of the Aare water flow in Bern, given observations of upstream precipitation at six locations in Bern’s water catchment and of the average daily water flow at an upstream gauging station, during the previous 10 days. 

> 1 `https://www.hydrodaten.admin.ch/` . 

> 2 `https://opendatadocs.meteoswiss.ch/` . 

11 

Extreme Conformal Prediction 

Figure A.3 in Section A.3 shows the location of those meteorological and gauging stations. 

## **5.2 Methodology** 

The river data exhibits a strong seasonal pattern with more water flow, and with more frequent and intense extreme events, during the late spring and summer months, due to snowmelt and heavy precipitation. This seasonality is likely to propagate to the residual nonconformity scores, violating the exchangeability assumption underlying classical conformal prediction. To account for it, we use the weighted variation of our extreme conformalization approach, discussed in Section 3.3. As a general procedure to account for distribution drift, Barber et al. (2023) suggest choosing large weights for recent calibration observations, close in time to the test period, and having weights decay for earlier observations, either exponentially or as a cutoff. Here, we make use of the inherent periodicity of the seasonal river discharge behaviour, by matching it with sinusoidal weights. Each year is partitioned into 24 roughly equal seasonal blocks of 15 to 16 days each. Let _𝐵_ ( _𝑖_ ) ∈{1 _,...,_ 24} denote the block in which an observation indexed by _𝑖_ falls into. For each block _𝑏_ = 1 _,...,_ 24, _𝑞_ ˆ _[𝑒] 𝛼_[(] _[𝑏]_[)][ is estimated as the upper-endpoint of the appropriate extreme score quantile CI, as described] in Section 3.2, but using the weighted GPD likelihood in Eq. (16), with calibration sample weights 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0012-04.png)


This choice of weights gives the highest importance to calibration observations in the same seasonal block _𝑏_ as the test point, and decreases the importance of observations in blocks further away in the year, with a yearly periodicity. For the estimation of _𝑞_ ˆ _[𝑒] 𝛼_[(] _[𝑏]_[)][, we use the GPD safeprofile CI] procedure recommended in Section 4, although almost no numerical issues were encountered with the profile likelihood. 

Our final one-day-ahead extreme PI for the average daily discharge, during seasonal block _𝑏_ = 1 _,...,_ 24 of the year, given past observations of upstream precipitation and water flow _𝑿_ test = _𝒙_ , is then _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ) = �0 _, 𝑄_[ˆ] 1 _[𝑒]_ − _𝛼_[(] _[𝒙]_[) +] _[𝑞]_[ˆ] _[𝑒] 𝛼_[(] _[𝑏]_[)] �. We compare this PI to the unconformalized quantile predictions _𝑄_[ˆ] 1 _[𝑒]_ − _𝛼_[(] _[𝒙]_[)][, and to a single-sided (see][ Section 3.1][) and weighted (][Barber et al.][,][ 2023][)] variation of the classical split conformalized quantile regression PI _𝐶_[ˆ] ( _𝒙_ ) (Romano et al., 2019), using the same sinusoidal weights from Eq. (18). 

Apart from its seasonality, the data is also sequentially dependent. However, the residual dependence between the scores _𝑆𝑖_ is likely weak and short-term, which should not significantly affect the marginal coverage guarantee of the conformal PIs (Oliveira et al., 2024). 

We consider several choices of extreme quantile regression models for _𝑄_[ˆ] 1 _[𝑒]_ − _𝛼_[(·)][:][EQRN,] GBEX (Velthoen et al., 2023), EGAM (Youngman, 2019), and EXQAR (Li and Wang, 2019). We also consider the constant unconditional GPD quantile estimates as a comparative baseline. We emphasise results using the recurrent version of EQRN, which is specifically designed for sequential dependence, and seems to fit the data best (Pasche and Engelke, 2024). 

The quantile models were pretrained on data from 1939 to 1951. They were all fine-tuned with a grid search for hyperparameter selection. We use data from 1951 to 1999 for calibration and testing, i.e. 48 years of daily data. The observations after 1999 are not considered, due to a major distribution shift[3] . We choose the first 10 years as the default calibration set in the first part of the analysis, but vary its size from 3 to 15 years in the second part, and use the rest for estimating PI coverage empirically. We use multiples of complete years to keep a seasonal balance in the calibration and test sets. 

> 3 See the flood report of the FOEN at `https://www.hydrodaten.admin.ch/en/2135.html` . 

12 

Extreme Conformal Prediction 

## **5.3 Results** 

Figure 3 compares the number of observations exceeding the PIs from each method during the test period, using predictions of the different pretrained models, for a range of moderate to extreme confidence levels. The number of observations expected to exceed the PIs during the 38-year test period varies from 2,776, for 1 − _𝛼_ = 0 _._ 8, to only 1 _._ 4, for the largest level 1 − _𝛼_ = 0 _._ 9999. Using the original model predictions as PIs leads, in most cases, to undercoverage. Although the best-performing predictions seem to vary around the target coverage, they fail to provide satisfactory coverage consistently. The classical conformalization seems effective for the lowest two confidence levels but worsens the coverage for the following moderately extreme levels, compared to the initial predictions. At the two largest levels, the classical method yields uninformative infinite PIs. The extreme conformalization method yields finite PIs with significantly better coverage for confidence levels above 0 _._ 95, for which the approaches differ. The PI coverage consistently strictly satisfies the target confidence levels for each initial prediction model. The profile likelihood procedure was stable for almost all models, confidence levels and seasonal blocks. A numerical instability only occurred once, for the unconditional predictions at the largest confidence level, during a single one of the seasonal blocks. 

Figure 4 shows the initial EQRN predictions, which seem to fit the data variation best, and their conformalized PI endpoints for two of the considered confidence levels, including the largest, during a test year. At 1 − _𝛼_ = 0 _._ 999, even though it has more marginal coverage, the extreme PIs are not excessively larger than the classical PIs. The extreme intervals are even tighter during some of the seasonal blocks. At the largest level, the infinite classical-method PIs are uninformative. On the other hand, the extreme PIs, satisfying the desired test coverage, are again not overly large compared to the data variation, the original predictions, and the unconditional quantile estimates. Extreme conformal corrections for the EQRN predictions at the other unshown levels are smaller in magnitude. During the considered year, the original predictions at the largest confidence level are exceeded once, on 25th July 1973. This exceedance is covered by the conformalized extreme PI. Finally, we observed the localised adaptivity of weighted conformalization, as, for example, the conformal correction is larger during late summer than during winter for both methods and confidence levels. 

Figure 5 shows the evolution of the test coverage with the calibration size, for all predictions, methods, and different confidence levels. We observe that the extreme PIs significantly outperform the classical conformalization in terms of empirical test coverage, for all relevant levels. It always provides informative finite PIs, contrary to the classical approach that yields infinite PIs for calibration sizes up to 5 years with 1 − _𝛼_ = 0 _._ 999, and for all sizes at the two largest levels. The extreme PI has valid coverage in almost all combinations, including when the classical approach and/or original predictions significantly undercover. In the few undercovered situations, its coverage is closer to the target 1 − _𝛼_ than both the original predictions and the classical approach. For some of the lower levels, there seems to be a pattern of decreasing coverage with increasing calibration size for the conformalized PIs. The largest discharge events happening in years one, three and 15 of the chosen calibration period is a likely explanation for this decrease in between, although there might also be a small effect from the decreasing test size, as observed with the coverage of the unconformalized predictions. 

13 

Extreme Conformal Prediction 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0014-01.png)


**----- Start of picture text -----**<br>
Predictions Classical GPD safeprofile<br>10.0<br>7.5<br>5.0<br>2.5<br>0.0<br>Confidence level<br>Finite Infinite Uncond EXQAR EGAM GBEX EQRN<br>0.8 0.9 0.97 0.990.9970.9990.99970.99990.8 0.9 0.97 0.990.9970.9990.99970.99990.8 0.9 0.97 0.990.9970.9990.99970.9999<br>Ratio of exceedences to expected<br>**----- End of picture text -----**<br>


Figure 3: Number of observations exceeding the PIs during the test period as a ratio to the expected number of exceedances for different confidence levels and each pretrained prediction model, for the original predictions (left), the classical conformalization (center), and the GPD safeprofile method (right). 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0014-03.png)


**----- Start of picture text -----**<br>
600<br>500<br>400<br>300<br>200<br>100<br>600<br>400<br>200<br>1973 Mar 1973 Jun 1973 Sep 1973 Dec<br>Date<br>0.999<br>1]<br>−<br>s<br>3<br>Discharge [m<br>0.9999<br>**----- End of picture text -----**<br>


Figure 4: Original EQRN prediction (blue), classical conformal PI (red), and extreme conformal PI (green), at confidence levels 0 _._ 999 (top panel) and 0 _._ 9999 (bottom panel), during one of the test years. The classical conformal PI is infinite at level 0 _._ 9999. The observations (points) and the unconditional GPD (1 − _𝛼_ )-quantile estimates (dotted lines) are also shown. 

14 

Extreme Conformal Prediction 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0015-01.png)


**----- Start of picture text -----**<br>
EQRN GBEX EGAM EXQAR Uncond<br>0.94<br>0.92<br>0.90<br>0.88<br>1.000<br>0.995<br>0.990<br>0.985<br>0.980<br>1.0000<br>0.9975<br>0.9950<br>0.9925<br>1.000<br>0.999<br>0.998<br>0.997<br>0.996<br>0.995<br>1.000<br>0.999<br>0.998<br>0.997<br>1.0000<br>0.9995<br>0.9990<br>0.9985<br>0.9980<br>4 8 12 4 8 12 4 8 12 4 8 12 4 8 12<br>Calibration size (years)<br>Classical Expected GPD safeprofile Prediction Finite Infinite<br>0.9<br>0.99<br>0.997<br>Test coverage<br>0.999<br>0.9997<br>0.9999<br>**----- End of picture text -----**<br>


Figure 5: Empirical test coverage of the prediction intervals for a range of calibration-set sizes, for each conformalization method, pretrained model (columns), and confidence level 1 − _𝛼_ (rows). For 1 − _𝛼<_ 0 _._ 95, corresponding to the quantile level of the GPD threshold _𝑢_ , the GPD approach coincides with the classical. 

15 

Extreme Conformal Prediction 

## **6 Conclusion** 

We propose a conformalization method which relies on extreme value statistics to provide conservative and nondegenerate prediction intervals for reliable risk assessment of high-impact events under extreme-confidence requirements. The novel method uses the well-studied peaks-over-threshold approach, which leverages the generalized Pareto distribution to extrapolate the necessary conformal correction from the calibration data to the required extreme confidence levels. It uses a conservative confidence interval solution for robustness against estimation and approximation biases. 

In the simulation study and the application to forecasting river flow, at large confidence levels, our extreme conformal prediction method consistently provides PIs with significantly better coverage properties than both the original predictions and classical conformalization. For the largest levels, classical approaches result in infinite (or undefined) PIs, which are of no practical use. On the other hand, our recommended method yields informative finite intervals that consistently achieve the desired coverage for confidence levels up to several orders of magnitude larger than what is feasible with classical methods. The weighted version of our approach can account for nonstationary data drifts, such as the seasonal behaviour of the river flow. Importantly, our extreme conformal prediction method can be used in combination with any extreme quantile regression model, including black-box machine learning methods without known asymptotic guarantees. 

One downside of our approach is its potential overconservativeness in certain scenarios, e.g., for moderately extreme confidence levels and some lighter-tailed data distributions. This is, at least in part, a consequence of our conservative CI-based solution, used to circumvent possible estimation and approximation biases in the GPD estimation. Moreover, peaks-over-threshold approaches rely on asymptotic properties. Thus, our approach lacks the finite-sample guarantees of classical conformal prediction. However, this is an unavoidable tradeoff for the ability to extrapolate beyond the moderate levels for which the classical empirical-quantile-based methods are feasible. In fact, obtaining finite-sample bounds for quantiles extrapolated beyond the data range is not theoretically possible without additional assumptions on the data distribution (Boucheron and Thomas, 2015; Thomas, 2015; Lhaut et al., 2022). A similar tradeoff exists in conformal prediction for conditional coverage, which is impossible to ensure on finite samples, resulting in the formulation of asymptotic conditional coverage guarantees as an alternative (Lei and Wasserman, 2014). 

This work establishes a first method for extreme-confidence PIs, as an extension of the well-established conformal regression framework. As our experiments mainly focused on the split-conformal approach, due to its computational efficiency and practical popularity, further work is possible with alternative or more specialised conformal approaches. One direction is to enhance the efficiency of data usage, using, for example, the full conformal version of our approach, described in Section A.1, or potential variants of jackknife (Barber et al., 2021; Steinberger and Leeb, 2016), infinitesimal jackknife (Alaa and van der Schaar, 2020), or cross-validation (Vovk, 2015). However, such approaches typically have a much greater computational cost, as they require refitting the predictive model many times. Whether the gain in statistical efficiency for our extreme conformal approach from using these alternative conformalization procedures is worth the extra computational cost remains an open question. Other directions include further extensions to nonexchangeable data. The weighted version of our extreme conformal approach seems suitable for nonstationary covariate drifts and shifts (analogously to Barber et al., 2023; Tibshirani et al., 2019). However, alternative solutions might be necessary to account for other problematic scenarios, such as long-term dependence or drifts in the conditional distribution of the response given the covariates. Finally, approaches other than conformalization could also warrant investigations, such as building PIs based on the so-called high-quality criterion and using deep learning (Pearce et al., 2018; Khosravi et al., 2011; Chen et al., 2021). How to incorporate extreme value statistics to extrapolate prediction intervals to cover high-impact events in these methodologies appears to be largely open. 

16 

Extreme Conformal Prediction 

## **Supplementary material** 

## **Implementation and reproducibility** 

To facilitate its practical use, the proposed extreme conformal procedure, including its weighted variant for nonstationary data, is implemented as an open-source R package, available at `https:// github.com/opasche/ExtremeConformal` . Furthermore, a new versatile and efficient algorithm for estimating profile-likelihood confidence intervals for extreme quantiles (and return levels) is used as a dependency and is available as a separate R package at `https://github.com/opasche/ ExtremeCI` . The code and data, with detailed instructions for reproducing the results presented in this paper, are available at `https://github.com/opasche/Reprod_ExtremeConformalPred` . 

## **Declarations** 

## **Acknowledgements** 

This research project was conducted while the first author, O. C. Pasche, was a visiting scholar at the Department of Industrial Engineering and Operations Research, at Columbia University. He thanks the department and the university for their hospitality during this period. We also thank the reviewers and the associate editor for their valuable comments. 

## **Funding** 

O. C. Pasche and S. Engelke were supported by the Swiss National Science Foundation Eccellenza Grant 186858. H. Lam was supported by the InnoHK initiative of the Innovation and Technology Commission of the Hong Kong Special Administrative Region Government, Laboratory for AI-Powered Financial Technologies, and the Columbia Innovation Hub Award. 

## **Availability of supporting data** 

In the Application to flood risk forecasting, we use river discharge and precipitation data recorded in Switzerland between 1930 and 1999, in the Rhine and Aare basins. The precipitation records can be freely obtained from MeteoSwiss, on `https://opendatadocs.meteoswiss. ch/` , and the discharge records from the Swiss Federal Office for the Environment (FOEN), on `https://www.bafu.admin.ch/bafu/en/home/topics/water/data-and-maps/watermonitoring-data/hydrological-data-service-for-watercourses-and-lakes.html` . 

## **Published article** 

This document is the preprint of an article in press for publication in the special issue ‘Bridging Heavy Tails and Artificial Intelligence’ of _Extremes_ (Pasche et al., 2026), with doi:10.1007/s10687026-00536-9. When citing this work, please refer to the published version. 

17 

Extreme Conformal Prediction 

## **References** 

- Alaa, A. and van der Schaar, M. (2020). Discriminative jackknife: Quantifying uncertainty in deep learning via higher-order influence functions. In _Proc. 37th Int. Conf. Mach. Learn._ , volume 119, pages 165–174. 

- Allouche, M., Girard, S., and Gobet, E. (2024). Estimation of extreme quantiles from heavy-tailed distributions with neural networks. _Stat. and Comput._ , 34(12). doi:10.1007/s11222-023-10331-2. 

- Angelopoulos, A. N. and Bates, S. (2023). Conformal Prediction: A Gentle Introduction. _Found. Trends in Mach. Learn._ , 16(4):494–591. doi:10.1561/2200000101. 

- Asadi, P., Davison, A. C., and Engelke, S. (2015). Extremes on river networks. _Ann. Appl. Stat._ , 9(4):2023–2050. doi:10.1214/15-aoas863. 

- Asadi, P., Engelke, S., and Davison, A. C. (2018). Optimal regionalization of extreme value distributions for flood estimation. _J. Hydrol._ , 556:182–193. doi:10.1016/j.jhydrol.2017.10.051. 

- Balkema, A. A. and de Haan, L. (1974). Residual life time at great age. _Ann. Probab._ , 2(5):792–804. doi:10.1214/aop/1176996548. 

- Barber, R. F., Candes, E. J., Ramdas, A., and Tibshirani, R. J. (2021). Predictive inference with the jackknife+. _Ann. Stat._ , 49(1):486–507. doi:10.1214/20-AOS1965. 

- Barber, R. F., Candès, E. J., Ramdas, A., and Tibshirani, R. J. (2023). Conformal prediction beyond exchangeability. _Ann. Stat._ , 51(2):816–845. doi:10.1214/23-AOS2276. 

- Bonferroni, C. (1936). Teoria statistica delle classi e calcolo delle probabilita. _Pubblicazioni del R istituto superiore di scienze economiche e commericiali di firenze_ , 8:3–62. 

- Boucheron, S. and Thomas, M. (2015). Tail index estimation, concentration and adaptivity. _Electron. J. Stat._ , 9(2):2751–2792. doi:10.1214/15-EJS1088. 

- Boulaguiem, Y., Zscheischler, J., Vignotto, E., van der Wiel, K., and Engelke, S. (2022). Modeling and simulating spatial extremes by combining extreme value theory with generative adversarial networks. _Environ. Data Sci._ , 1:e5. doi:10.1017/eds.2022.4. 

- Bücher, A. and Zhou, C. (2021). A Horse Race between the Block Maxima Method and the Peak-over-Threshold Approach. _Stat. Sci._ , 36(3):360–378. doi:10.1214/20-STS795. 

- Buriticá, G. and Engelke, S. (2024). Progression: an extrapolation principle for regression. _ArXiv preprint_ . doi:10.48550/arXiv.2410.23246. 

- Chavez-Demoulin, V. and Davison, A. C. (2005). Generalized additive modelling of sample extremes. _J. R. Stat. Soc. C_ , 54(1):207–222. doi:10.1111/j.1467-9876.2005.00479.x. 

- Chen, H., Huang, Z., Lam, H., Qian, H., and Zhang, H. (2021). Learning prediction intervals for regression: Generalization and calibration. In Banerjee, A. and Fukumizu, K., editors, _Int. Conf. Artificial Intelligence and Stat._ , volume 130 of _Proceedings of Machine Learning Research_ , pages 820–828. PMLR. 

- Chernozhukov, V. (2005). Extremal quantile regression. _Ann. Stat._ , 33(2):806 – 839. doi:10.1214/009053604000001165. 

- Coles, S. (2001). _An Introduction to Statistical Modeling of Extreme Values_ . Springer. doi:10.1007/978-1-4471-3675-0. 

- Davison, A. C. and Hinkley, D. V. (1997). _Bootstrap Methods and their Application_ . Cambridge University Press, New York. doi:10.1017/CBO9780511802843. 

- Davison, A. C., Hinkley, D. V., and Young, G. A. (2003). Recent Developments in Bootstrap Methodology. _Stat. Sci._ , 18(2):141–157. doi:10.1214/ss/1063994969. 

- de Carvalho, M., Kumukova, A., and Dos Reis, G. (2022a). Regression-type analysis for multivariate extreme values. _Extremes_ , 25(4):595–622. doi:10.1007/s10687-022-00446-6. 

- de Carvalho, M., Pereira, S., Pereira, P., and de Zea Bermudez, P. (2022b). An extreme value bayesian lasso for the conditional left and right tails. _J. Agric. Biol. Environ. Stat._ , 27(2):222–239. doi:10.1007/s13253-021-00469-9. 

- de Haan, L. and Ferreira, A. (2006). _Extreme Value Theory_ . Springer. doi:10.1007/0-387-34471-3. 

- de Haan, L. and Zhou, C. (2022). Bootstrapping extreme value estimators. _J. Am. Stat. Assoc._ , 119(545):382–393. doi:10.1080/01621459.2022.2120400. 

- Dupuis, D. J., Engelke, S., and Trapin, L. (2023). Modeling panels of extremes. _Ann. Appl. Stat._ , 17(1):498–517. doi:10.1214/22-AOAS1639. 

- Engelke, S. and Hitz, A. (2020). Graphical models for extremes (with discussion). _J. R. Stat. Soc. B_ , 82(4):871–932. doi:10.1111/rssb.12355. 

- Engelke, S. and Ivanovs, J. (2021). Sparse structures for multivariate extremes. _Annu. Rev. Stat. Appl._ , 8:241–270. 

18 

Extreme Conformal Prediction 

doi:10.1146/annurev-statistics-040620-041554. 

- Gnecco, N., Terefe, E. M., and Engelke, S. (2024). Extremal random forests. _J. Am. Stat. Assoc._ , 119(548):3059–3072. doi:10.1080/01621459.2023.2300522. 

- Gupta, C., Kuchibhotla, A. K., and Ramdas, A. (2022). Nested conformal prediction and quantile out-of-bag ensemble methods. _Pattern Recognit._ , 127:108496. doi:10.1016/j.patcog.2021.108496. 

- Huet, N., Clémençon, S., and Sabourin, A. (2024). On regression in extreme regions. _ArXiv preprint_ . doi:10.48550/arXiv.2303.03084. 

- Jalalzai, H., Clémençon, S., and Sabourin, A. (2018). On binary classification in extreme regions. In _Adv. Neural Inf. Process. Syst._ , volume 31, pages 3092–3100. 

- Katz, R. W., Parlange, M. B., and Naveau, P. (2002). Statistics of extremes in hydrology. _Adv. Water Resour._ , 25:1287–1304. doi:10.1016/S0309-1708(02)00056-8. 

- Keef, C., Tawn, J., and Svensson, C. (2009). Spatial risk assessment for extreme river flows. _J. R. Stat. Soc. C_ , 58(5):601–618. doi:10.1111/j.1467-9876.2009.00672.x. 

- Khosravi, A., Nahavandi, S., Creighton, D., and Atiya, A. F. (2011). Comprehensive review of neural network-based prediction intervals and new advances. _IEEE Trans. Neural Netw._ , 22(9):1341–1356. doi:10.1109/TNN.2011.2162110. 

- Kim, B., Xu, C., and Barber, R. (2020). Predictive inference is free with the jackknife+-after-bootstrap. In _Adv. Neural Inf. Process. Syst._ , volume 33, pages 4138–4149. 

- Koh, J. (2023). Gradient boosting with extreme-value theory for wildfire prediction. _Extremes_ , 26(2):273–299. doi:10.1007/s10687-022-00454-6. 

- Lei, J., G’Sell, M., Rinaldo, A., Tibshirani, R. J., and Wasserman, L. (2018). Distribution-free predictive inference for regression. _J. Am. Stat. Assoc._ , 113(523):1094–1111. doi:10.1080/01621459.2017.1307116. 

- Lei, J. and Wasserman, L. (2014). Distribution-free prediction bands for non-parametric regression. _J. R. Stat. Soc. B_ , 76(1):71–96. doi:10.1111/rssb.12021. 

- Lhaut, S., Sabourin, A., and Segers, J. (2022). Uniform concentration bounds for frequencies of rare events. _Statist. Probab. Lett._ , 189:109610. doi:10.1016/j.spl.2022.109610. 

- Li, D. and Wang, H. J. (2019). Extreme Quantile Estimation for Autoregressive Models. _J. Bus. Econ. Stat._ , 37(4):661–670. doi:10.1080/07350015.2017.1408469. 

- Oliveira, R. I., Orenstein, P., Ramos, T., and Romano, J. V. (2024). Split conformal prediction and non-exchangeable data. _J. Mach. Learn. Res._ , 25(225):1–38. 

- Papadopoulos, H. (2008). Inductive conformal prediction: Theory and application to neural networks. In _Tools in Artificial Intelligence_ , chapter 18. IntechOpen. doi:10.5772/6078. 

- Papadopoulos, H., Gammerman, A., and Vovk, V. (2008). Normalized nonconformity measures for regression conformal prediction. In _Int. Conf. Artificial Intelligence and Appl._ , pages 64–69. 

- Papadopoulos, H., Proedrou, K., Vovk, V., and Gammerman, A. (2002). Inductive confidence machines for regression. In _Mach. Learn.: ECML 2002_ , pages 345–356. Springer. doi:10.1007/3-540-36755-1_29. 

- Papadopoulos, H., Vovk, V., and Gammerman, A. (2011). Regression conformal prediction with nearest neighbours. _J. Artificial Intelligence Res._ , 40:815–840. doi:10.1613/jair.3198. 

- Pasche, O. C., Chavez-Demoulin, V., and Davison, A. C. (2023). Causal modelling of heavy-tailed variables and confounders with application to river flow. _Extremes_ , 26(3):573–594. doi:10.1007/s10687-022-00456-4. 

- Pasche, O. C. and Engelke, S. (2024). Neural networks for extreme quantile regression with an application to forecasting of flood risk. _Ann. Appl. Stat._ , 18(4):2818–2839. doi:10.1214/24-AOAS1907. 

- Pasche, O. C., Lam, H., and Engelke, S. (2026). Extreme conformal prediction: Reliable intervals for high-impact events. _Extremes_ . doi:10.1007/s10687-026-00536-9. In press. 

- Pearce, T., Brintrup, A., Zaki, M., and Neely, A. (2018). High-quality prediction intervals for deep learning: A distribution-free, ensembled approach. In _Proc. 35th Int. Conf. Mach. Learn._ , volume 80, pages 4075–4084. 

- Pickands, III, J. (1975). Statistical inference using extreme order statistics. _Ann. Stat._ , 3(1):119–131. doi:10.1214/aos/1176343003. 

- Richards, J. and Huser, R. (2024). Regression modelling of spatiotemporal extreme U.S. wildfires via partially-interpretable neural networks. _ArXiv preprint_ . doi:10.48550/arXiv.2208.07581. 

- Romano, Y., Patterson, E., and Candes, E. (2019). Conformalized quantile regression. In _Adv. Neural Inf. Process. Syst._ , volume 32. 

19 

## Extreme Conformal Prediction 

- Roodman, D. (2018). Bias and size corrections in extreme value modeling. _Comm. Statist. Theory Methods_ , 47(14):3377– 3391. doi:10.1080/03610926.2017.1353630. 

- Shafer, G. and Vovk, V. (2008). A tutorial on conformal prediction. _J. Mach. Learn. Res._ , 9(3). 

- Steinberger, L. and Leeb, H. (2016). Leave-one-out prediction intervals in linear regression models with many variables. _ArXiv preprint_ . doi:10.48550/arXiv.1602.05801. 

- Thomas, M. (2015). _Concentration results on extreme value theory_ . PhD thesis, Univeristé Paris Diderot Paris 7. `https://theses.hal.science/tel-01177197` . 

- Tibshirani, R. J., Foygel Barber, R., Candes, E., and Ramdas, A. (2019). Conformal prediction under covariate shift. In _Adv. Neural Inf. Process. Syst._ , volume 32. 

- van Oordt, M. and Zhou, C. (2019). Systemic risk and bank business models. _J. Appl. Econometrics_ , 34(3):365–384. doi:10.1002/jae.2666. 

- Velthoen, J., Cai, J.-J., Jongbloed, G., and Schmeits, M. (2019). Improving precipitation forecasts using extreme quantile regression. _Extremes_ , 22(4):599–622. doi:10.1007/s10687-019-00355-1. 

- Velthoen, J., Dombry, C., Cai, J.-J., and Engelke, S. (2023). Gradient boosting for extreme quantile regression. _Extremes_ , 26(4):639–667. doi:10.1007/s10687-023-00473-x. 

- Vovk, V. (2015). Cross-conformal predictors. _Ann. Math. Artif. Intell._ , 74:9–28. doi:10.1007/s10472-013-9368-4. 

- Vovk, V., Gammerman, A., and Saunders, C. (1999). Machine-learning applications of algorithmic randomness. In _Proc. 16th Int. Conf. Mach. Learn._ , pages 444–453. 

- Vovk, V., Gammerman, A., and Shafer, G. (2005). _Algorithmic Learning in a Random World_ . Springer, 1st edition. doi:10.1007/b106715. 

- Youngman, B. D. (2019). Generalized Additive Models for Exceedances of High Thresholds With an Application to Return Level Estimation for U.S. Wind Gusts. _J. Am. Stat. Assoc._ , 114(528):1865–1879. doi:10.1080/01621459.2018.1529596. 

- Zeder, J., Sippel, S., Pasche, O. C., Engelke, S., and Fischer, E. M. (2023). The effect of a short observational record on the statistics of temperature extremes. _Geophys. Res. Lett._ , 50(16):e2023GL104090. doi:10.1029/2023GL104090. 

- Zhou, X., Chen, B., Gui, Y., and Cheng, L. (2025). Conformal prediction: A data perspective. _ACM Comput. Surv._ , 58(2):49:1–49:37. doi:10.1145/3736575. 

- Šidák, Z. (1967). Rectangular confidence regions for the means of multivariate normal distributions. _J. Am. Stat. Assoc._ , 62(318):626–633. doi:10.1080/01621459.1967.10482935. 

20 

Extreme Conformal Prediction 

## **APPENDIX** 

## **A.1 Extensions to other conformal approaches** 

This section describes in more detail the extensions of our proposed extreme conformal method to alternative conformal procedures discussed in Section 3.3. 

As explained in the main text, the extension to different base predictive models and scores is the most straightforward, as our extreme conformalization described in Section 3.2 is agnostic to their definition. This includes the classical split-conformal approach that, instead of the quantile ˆ predictions _𝑄_[ˆ] _𝛼_ /2( _𝒙_ ) _, 𝑄_[ˆ] 1− _𝛼_ /2( _𝒙_ ), relies on a conditional-mean base regression model _𝜇_ ( _𝒙_ ), and the ˆ residuals _𝑠_ ( _𝒙, 𝑦_ ) := | _𝑦_ − _𝜇_ ( _𝒙_ )| as nonconformity score (Papadopoulos et al., 2002; Papadopoulos, 2008; Lei et al., 2018). The procedure from Section 3.2 would then be performed with these alternative scores, resulting in the fixed-length extreme conformal PIs _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ) = � _𝜇_ ˆ( _𝒙_ ) − _𝑞_ ˆ _[𝑒] 𝛼[,][𝜇]_[ˆ][(] _[𝒙]_[) +] _[𝑞]_[ˆ] _[𝑒] 𝛼_ �. If a residual-dispersion estimate _𝜎_ ˆ ( _𝒙_ ) is also available, for instance, from a heteroscedastic reˆ ˆ gression model or a Bayesian approach, using the scaled residuals _𝑠_ ( _𝒙, 𝑦_ ) := | _𝑦_ − _𝜇_ ( _𝒙_ )| / _𝜎_ ( _𝒙_ ) as nonconformity scores (Papadopoulos et al., 2008, 2011; Lei et al., 2018) would result in the varying-length extreme PIs _𝐶_[ˆ] _[𝑒]_ ( _𝒙_ ) = � _𝜇_ ˆ( _𝒙_ ) − _𝑞_ ˆ _[𝑒] 𝛼[𝜎]_[ˆ][(] _[𝒙]_[)] _[,][𝜇]_[ˆ][(] _[𝒙]_[) +] _[𝑞]_[ˆ] _[𝑒] 𝛼[𝜎]_[ˆ][(] _[𝒙]_[)] �. Although the latter doesn’t require extreme quantile regression to yield varying-length PIs, it tends to underestimate conditional variability and yield less adaptive predictions (Romano et al., 2019). 

In full-conformal procedures, the data is not split into training and calibration sets. Instead, given a training set {( _𝑿𝑖,𝑌𝑖_ )} _𝑖[𝑛]_ =1[and the test covariates] _[𝑿]_[test][, the PI] _[𝐶]_[ˆ][(] _[𝑿]_[test][)][for] _[ 𝑌]_[test][ is constructed] ˆ by refitting the base model _𝑓_[ˆ] (e.g., _𝑄_[ˆ] 1− _𝛼_ or _𝜇_ ) on {( _𝑿𝑖,𝑌𝑖_ )} _𝑖[𝑛]_ =1[∪{(] _[𝑿]_[test] _[, 𝑦]_[)}][, for a dense grid of] values _𝑦_ in the value space of _𝑌_ . Each fit is denoted by _𝑓_[ˆ] _[𝑦]_ . The desired nonconformity scores are then defined, for each _𝑦_ , as _𝑆𝑖_ ( _𝑦_ ) := _𝑠_ ( _𝑿𝑖,𝑌𝑖_ ; _𝑓_[ˆ] _[𝑦]_ ), _𝑖_ = 1 _,...,𝑛_ (Vovk et al., 1999, 2005; Shafer and Vovk, 2008). Consequently, for a full-conformal variant, our proposed procedure from Section 3.2 should be performed, for each _𝑦_ , on the scores { _𝑆𝑖_ ( _𝑦_ )} _𝑖[𝑛]_ =1[, to obtain a] _[𝑞]_[ˆ] _[𝑒] 𝛼_[(] _[𝑦]_[)][.][The resulting PI is] then _𝐶_[ˆ] _[𝑒]_ ( _𝑿_ test) = { _𝑦_ : _𝑠_ ( _𝑿_ test _, 𝑦_ ; _𝑓_[ˆ] _[𝑦]_ ) ≤ _𝑞_ ˆ _[𝑒] 𝛼_[(] _[𝑦]_[)}][.][Although the latter makes a more efficient use of the] data than the split variant, it is extremely computationally costly. The analogous extension to the middle-ground _𝑘_ -fold approaches, such as Jackknife+/CV+ (Barber et al., 2021) and cross-conformal prediction (Vovk, 2015), would also suffer, less extremely, from similar refitting expensiveness. 

## **A.2 Proof of Proposition 3.1** 

_Proof._ Let [ _𝐿𝑄,𝑈𝑄_ ] be the (1 − _𝛼_ 2)-confidence interval for _𝑞_ := _𝐹𝑆_[−][1][(][1][−] _[𝛼]_[1][)][.][Then, by assumption,] P( _𝑞_ ≤ _𝑈𝑄_ ) ≥ P( _𝐿𝑄_ ≤ _𝑞_ ≤ _𝑈𝑄_ ) ≥ 1 − _𝛼_ 2 _,_ and P ( _𝑆_ test ≤ _𝑞_ ) ≥ 1 − _𝛼_ 1 _._ As _𝑆_ test and _𝑈𝑄_ are independent, 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0021-08.png)


ˆ By the definitions of _𝐶[𝑒]_ ( _𝒙_ ) = { _𝑦_ : _𝑠_ ( _𝒙, 𝑦_ ) ≤ _𝑈𝑄_ } and of _𝑆_ test = _𝑠_ ( _𝑿_ test _,𝑌_ test), the events { _𝑌_ test ∈ _𝐶_[ˆ] _[𝑒]_ ( _𝑿_ test)} and { _𝑆_ test ≤ _𝑈𝑄_ } are equivalent. Therefore, 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0021-10.png)


21 

Extreme Conformal Prediction 

## **A.3 Additional figures** 

## **A.3.1 Simulation study** 

Figure A.1 shows the distribution of the computed test coverage for each considered conformalization method, confidence level, and calibration size, for the light-tailed Gaussian-noise data and the ground truth as base predictions. Figure A.2 shows the same test-coverage distribution, for each considered conformalization method, confidence level, and calibration size, for the Student _𝑡_ distributed noise and the linear GPD quantiles as the base predictions. 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0022-04.png)


**----- Start of picture text -----**<br>
α = 10 [−][3] α = 10 [−][3.5] α = 10 [−][4] α = 10 [−][4.5] α = 10 [−][5]<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>Method<br>ClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profileClassicalGPD simpleGPD deltaGPD bootst.GPD profile<br>c =n<br> 1000<br>c =n<br> 3163<br>Test coverage<br>c =n<br> 10000<br>**----- End of picture text -----**<br>


Figure A.1: Boxplots of the test coverage probability of the quantile PIs (analytically computed for a grid of test observation and averaged over X) for different conformalization methods, conformal confidence values 1 − _𝛼_ (columns, labelled with _𝛼_ ), and calibration sample sizes _𝑛𝑐_ (rows), for the Gaussian distributed noise and quantile ground-truth predictions. 

22 

Extreme Conformal Prediction 


![](markdown_output/extreme-conformal-2025_images/extreme-conformal-2025.pdf-0023-01.png)


**----- Start of picture text -----**<br>
α = 10 [−][3] α = 10 [−][3.5] α = 10 [−][4] α = 10 [−][4.5] α = 10 [−][5]<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>0.99999<br>0.9999<br>0.999<br>Method<br>PredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profilePredictionClassicalGPD simpleGPD deltaGPD bootst.GPD profile<br>c =n<br> 1000<br>c =n<br> 3163<br>Test coverage<br>c =n<br> 10000<br>**----- End of picture text -----**<br>


Figure A.2: Boxplots of the test coverage probability of the quantile PIs (analytically computed for a grid of test observation and averaged over X) for different conformalization methods, conformal confidence values 1 − _𝛼_ (columns, labelled with _𝛼_ ), and calibration sample sizes _𝑛𝑐_ (rows), for the Student _𝑡_ distributed noise and linear GPD quantile predictions. 

23 

Extreme Conformal Prediction 

## **A.3.2 Application to river-flow forecasts** 

Figure A.3 shows the locations of the meteorological and gauging stations corresponding to the variables used in the model forecasts. 

Figure A.3: Topographic map of water catchment of the gauging station in Bern–Schönau (62) on the Aare in Switzerland. Another upstream gauging station in Gsteig (43), on the Lütschine river, and six meteorological stations with precipitation measurements (triangles) are also shown (source: Pasche and Engelke, 2024). 

24 

