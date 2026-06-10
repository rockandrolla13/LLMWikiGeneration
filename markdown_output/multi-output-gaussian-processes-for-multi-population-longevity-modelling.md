_Annals of Actuarial Science_ (2021), **15** , pp. 318–345 doi:10.1017/S1748499521000142 

**PA P E R** 

## **Multi-output Gaussian processes for multi-population longevity modelling** 

## Nhan Huynh and Mike Ludkovski[∗] 

Department of Statistics and Applied Probability, University of California at Santa Barbara, Santa Barbara, CA 93106, USA ∗Corresponding author. E-mail: ludkovski@pstat.ucsb.edu 

(Received 01 March 2020; revised 17 March 2021; accepted 24 March 2021; first published online 17 May 2021) 

## **Abstract** 

We investigate joint modelling of longevity trends using the spatial statistical framework of Gaussian process (GP) regression. Our analysis is motivated by the Human Mortality Database (HMD) that provides unified raw mortality tables for nearly 40 countries. Yet few stochastic models exist for handling more than two populations at a time. To bridge this gap, we leverage a spatial covariance framework from machine learning that treats populations as distinct levels of a factor covariate, explicitly capturing the cross- ~~population dependence. The proposed multi-output GP models straightforwardly scale up to a dozen~~ populations and moreover intrinsically generate coherent joint longevity scenarios. In our numerous case studies, we investigate predictive gains from aggregating mortality experience across nations and genders, including by borrowing the most recently available “foreign” data. We show that in our approach, information fusion leads to more precise (and statistically more credible) forecasts. We implement our models in R, as well as a Bayesian version in Stan that provides further uncertainty quantification regarding the estimated mortality covariance structure. All examples utilise public HMD datasets. 

**Keywords:** longevity modeling; Gaussian process; multi-population mortality 

## **1. Mortality Models Across Multiple Populations** 

Mortality data are typically collected by jurisdictional areas, such as countries and states. As a result, global mortality experience is summarised in dozens of national and sub-national registries, presenting a major data-analysis challenge. The burgeoning Human Mortality Database (HMD, 2018) offers a centralised portal to nearly 40 such datasets, yielding a rich source of cross-national longevity trends. 

Significant predictive value can be extracted from joint models of these mortality tables. By aggregating data, one hopes to improve prediction accuracy (through better disentangling of trends vis-a-vis “noise”) and simultaneously reduce model risk by increasing credibility of the forecasts. Moreover, joint models capture information fusion, which is very valuable since mortality data are released asynchronously. With a joint model, one can rely on the newly released data of a related foreign population to update and improve the domestic forecast. Last but not least, joint models are critical for generating forecasts and future scenarios simultaneously across multiple populations. Individual models will tend to be non-coherent, i.e. include scenarios where the joint mortality trends cross over or diverge in unrealistic ways. 

Yet few models exist for predictive multi-population longevity analysis beyond two populations. The latter case affords the convenient hierarchy of treating one population as the baseline “index” and then modelling the “spread” between the index and the secondary population. With three or more populations, the conceptual meaning of the multiple resulting longevity spreads 

> ⃝C The Author(s), 2021. Published by Cambridge University Press on behalf of Institute and Faculty of Actuaries 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 319 

becomes fuzzy. Moreover, in the commonly adopted Age–Period–Cohort-style models, multiple populations are treated through decomposition into global- and population-specific factors, implying that the number of factors grows linearly in the number of populations. Since each factor (Age, Period, etc.) contains dozens of parameters, one quickly ends up with hundreds of parameters to be estimated, creating significant computation and statistical inference bottlenecks. 

In this article, we investigate a machine learning approach that simultaneously models multiple longevity surfaces within a joint _spatial covariance_ framework. Our approach scales up to ∼ 10 populations, which we treat as a factor covariate, with the respective correlation inferred as part of the model fitting procedure. Specifically, we employ multi-output Gaussian process (MOGP) models, building upon our earlier work in Ludkovski _et al_ . (2018) and Huynh _et al_ . (2020) on the use of GPs for longevity predictive analytics. GPs treat age-specific mortality rates as a noisily observed response surface that is learned via the multivariate _kriging_ equations. Embedding multiple populations within a MOGP naturally captures the borrowing of mortality information and the underlying commonality of mortality patterns. Indeed, a MOGP imposes a transparent correlation structure on the co-dependence of mortality rates across populations, disentangling it from the global Age–Year pattern. Moreover, GPs afford a Bayesian perspective, yielding a full uncertainty quantification – including coherent multi-population stochastic scenarios – not just for mortality rates but also for mortality improvement factors. 

The GP paradigm brings a flexible non-parametric spatio-temporal structure that treats tasks of data smoothing (aka in-sample prediction) and forecasting (aka out-of-sample prediction) in an internally consistent manner. The vast GP ecosystem has become a centrepiece of probabilistic data science and includes a multitude of extensions, from GP GLMs (to address non-Gaussian observation noise) to Kronecker GP (for faster analysis of gridded data). We refer to Duvenaud (2014), Chu & Ghahramani (2005), Garrido-Merchán & Hernández-Lobato (2018) for further discussion of GP modelling with categorical covariates. From the machine learning perspective, the respective ideas of multi-task learning and transfer learning have wide applications (Bonilla _et al_ ., 2008; Caruana, 1997; Letham & Bakshy, 2019). 

In the context of mortality modelling, single-population GPs were investigated in Ludkovski _et al_ . (2018) and some preliminary multi-population analysis appeared recently in Huynh _et al_ . (2020). Related spatio-temporal methods were investigated by Christiansen _et al_ . (2015) to capture the spread between individual log-mortality rates and weighted average log-mortality and Debón _et al_ . (2010). Another related analysis of the HMD can be found in Carracedo _et al_ . (2018) who applied spatio-temporal Markov clustering to detect common patterns of longevity across 26 European countries, see also Antonio _et al_ . (2017). Another way to introduce dependence between populations is through statistical shrinkage within a Bayesian hierarchical model. Raftery _et al_ . (2012) modelled mortality of 160+ countries by first imposing a global hyper-prior over several one-dimensional parameters and then constructing individual Lee–Carter models. A related approach is taken up by Wi´sniowski _et al_ . (2015). This framework also permits to inject additional socio-economic or geo-political covariates to capture the varying degree of dependence (Kleinow & Cairns, 2013; Boonen & Li, 2017). 

The strand of literature addressing multi-population extensions of the now-classical Lee– Carter stochastic mortality framework is getting longer. The seminal work by Li & Lee (2005) extended Lee–Carter to two populations, postulating a decomposition of mortality into population-specific plus global Age and Period factors (for a total of 2 _L_ + 2 factors with _L_ populations). More parsimonious versions were proposed by Kleinow (2015) who considered a common Age effect, and Delwarde _et al_ . (2006) who proposed a common Period effect. Enchev _et al_ . (2017) investigated several intermediate cases. Dispensing with country-specific factors allows more interpretability, e.g. in the Kleinow (2015) common age effect (CAE) model one may directly compare period effects across countries since these are scaled with the same age parameters. From the other direction, the model of Li & Lee (2005) functionally corresponds to having a single degree 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

320 Nhan Huynh and Mike Ludkovski 

of freedom in the evolution of the mortality curve over time. According to Li (2013), at least two Age/Period factors are warranted, and accordingly a multi-factor extension was investigated. Note that in our setup mortality curves are non-parametric (i.e. as many degrees of freedom as there are data points). To achieve coherent forecasts with two populations, Hyndman _et al_ . (2013) considered co-integration, see also the multi-level functional regression approach in Shang (2016). In a similar spirit, D’Amato _et al_ . (2016), Li & Lu (2017), and Guibert _et al_ . (2019) investigated vector autoregressive approaches to achieve correlation across the multiple Period factors. Alternatively, Chen _et al_ . (2015) and Wang _et al_ . (2015) applied a copula approach to capture the dependence between individual Period factors and Yang & Wang (2013) considered a vector error correction model. As further extensions, Wang _et al_ . (2020) incorporate structural breaks in order to capture time-varying mortality improvement factors and Dong _et al_ . (2020) apply tensor decomposition to identify the univariate Age, Year and Population factors. 

Let us also mention other methods for multi-population mortality, such as those based on hierarchical Buhlmann credibility theory (Tsai & Zhang, 2019; Tsai & Wu, 2020), hierarchical Bayes (Lu _et al_ ., 2019) and continuous-time Levy processes (Qin & Jevtic, 2016). 

To sum up, our main contribution is a statistical methodology to build multi-population longevity models through MOGP. A key innovation is the use of intrinsic coregionalisation model (ICM) kernels to achieve dimension reduction that leads to more efficient models that can gracefully handle two to ten populations. Another innovation is a detailed discussion about how to pool populations to maximise predictive power. The analysis below supersedes the earlier proceedings version in Huynh _et al_ . (2020) that concentrated on descriptive investigation of single-population GPs across HMD datasets and primarily focused on two-population cases with full-rank kernels. As further supplementary material, we also provide an online tutorial with additional animations and visualisations, see https://nhanhuynh46.github.io/MOGPTutorials/. 

The rest of the paper is organised as follows. Section 2 describes the MOGP model for multiple-population mortality analysis. Section 3 focuses on how MOGPs can maximise predictive accuracy, while section 4 shows how MOGP is appropriate for coherent forecasting and capturing commonality of mortality experience. 

## _**1.1 Motivating multi-population models**_ 

Our first motivation for developing multi-population models is to improve predictive accuracy. It is generally accepted that there is strong commonality in mortality experiences of different populations, and therefore that there is an opportunity for data fusion to better capture trends and de-noise raw data. Hence, we wish to build a multi-population model to maximise its “credibility”, or equivalently reduce the mis-specification between the true mortality evolution and the fitted model dynamics that arises due to using limited historical data. The latter idea has several complementary aspects that we now enumerate to foreshadow the methods and results below. 

First, data fusion is intrinsically linked to data selection: one should only model populations that are actually dependent; including those that are little-correlated is likely to worsen model fit and forecasting performance. Therefore, multi-population modelling is closely linked to identifying dependence patterns and selecting (i.e. clustering) populations that are most correlated. From a modelling perspective, judicious choice of which populations to aggregate is critical to keeping models tractable and computationally lean – it is beyond the reach of nearly all methods to directly handle the full HMD with 75+ datasets. 

Second, data fusion is also important for mitigating model risk, i.e. for fitting the best model. Therefore, successful data fusion is expected to manifest itself in reduced parameter uncertainty. For GPs, this translates into tighter hyperparameter and latent-surface posteriors, affording a transparent visualisation of higher model stability and higher confidence into the predictive forecasts. We emphasise the latter Bayesian concepts and assess our predictive accuracy not simply 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 321 

through the predictive mean (via a mean-squared-error related metric) but also through scoring rules, such as continuous ranked probability score (CRPS) that are based on the quality of the full predictive distribution. 

Third, for HMD data in particular, a key problem is to obtain highest-quality contemporary forecasts, i.e. to assess the present-date mortality in a given “domestic” population. Because the database is updated very frequently and asynchronously across different countries, at any given timepoint the database is not rectangular but “notched”, i.e. it ends at different years. For instance, as of February 2020 some countries already have 2018 data added, most have data up to 2017, and a few are still lagging and only have data up to 2016. Using such input data to build the bestfeasible prediction of 2019 mortality in say UK is possibly the most common use of HMD, but presents challenges relative to the “classical” time-series models. As we show, GPs are both easily adaptable and internally consistent for this task. 

To conclude this section, we reiterate the big picture perspective that underlies the premise of multi-population analysis: because populations _are_ similar – both in their static structure and in their dynamic evolution – one should leverage this similarity to improve predictive analysis. But this must be done in a smart way, keeping in mind computational and statistical considerations and the specific predictive tasks envisioned. We believe that for mortality analysis, a multi-output machine learning framework checks off all these boxes and offers a tractable and scalable way to jointly analyse a collection of two to ten populations. 

**Data source:** We work with mortality data from the HMD (HMD, 2018) which provides the aggregated mortality statistics at the national levels for 40 developed countries across the globe. The HMD applies the same consistent set of procedures (Boe _et al_ ., 2015) on each population and presently focuses on developed economies where death registrations and census data are available and reliable. For our analysis, we rely on 1-year age groups, concentrating on Ages 50–84 (retirement ages most relevant for predictive actuarial analysis) for both genders and calendar Years 1990–2016. In the models below, we consider various subsets of the following 16 European datasets: Austria (AUT), Belgium (BEL), Czech Republic (CZE), Denmark (DEN), Estonia (EST), France (FRA), Germany (GER), Hungary (HUN), Latvia (LAT), Lithuania (LTU), Netherlands (NED), Poland (POL), Spain (ESP), Sweden (SWE), Switzerland (SUI) and United Kingdom (UK or GBR). 

The dataset is organised as a large table. The _n_ th observation for the _l_ th country contains (i) Age and Year as a pair of independent variables, ( _xag[n]_[,] _[ x] yr[n]_[), and (ii) the logarithm of the observed] mortality rate, 

**==> picture [397 x 47] intentionally omitted <==**

## **2. MOGP Models** 

## _**2.1 GP regression for mortality tables**_ 

A GP is an infinite collection of random variables, any finite number of which follows a multivariate normal (MVN) distribution. As such, a GP _f_ ∼ _GP_ ( _m_ , _C_ ) is characterised by its mean function _m_ ( _x_ ) and its covariance structure _C_ ( _x_ , _x_ ’). This means that for any vector **x** = ( _x_[1] , _. . ._ , _x[n]_ ) of _n_ inputs: 

**==> picture [149 x 14] intentionally omitted <==**

where **m(x)** = E[ _f_ ( **x** )] is the mean vector of size _n_ and **C(x** , **x)** is the _n_ -by- _n_ covariance matrix, _C_ ( _x_ , _x_[′] ) := E[( _f_ ( _x_ ) − _m_ ( _x_ ))( _f_ ( _x_[′] ) − _m_ ( _x_[′] ))]. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

322 Nhan Huynh and Mike Ludkovski 

In a GP regression setup, the latent _f_ links the observations or output vector **y** = ( _y_[1] , _. . ._ , _y[n]_ ) to the input vector **x** via: 

**==> picture [228 x 12] intentionally omitted <==**

where _ϵ[i]_ is the error term to reflect that we observe only a noisy sample of _f_ ( _x[i]_ ). In our context, _x[i]_ are the individual cells in a mortality table (so indexed by Age, Year, etc.), _y[i]_ are observed raw log-mortality rates and _f_ ( _x[i]_ ) is the _true_ mortality rate that would materialise in the absence of any random shocks. We assume that observation noise is Gaussian: _ϵ[i]_ ∼ _N_ (0, _σ_[2] ) or _ϵ_ = ( _ϵ_[1] , ..., _ϵ[n]_ ) ∼ _N_ ( **0** , _�_ = diag( _σ_[2] )). It follows that Cov( _y[i]_ , _y[j]_ ) = Cov( _f_ ( _x[i]_ ), _f_ ( _x[j]_ )) + _σ_[2] _δ_ ( _x[i]_ , _x[j]_ ) and therefore **y** ∼ _N_ ( **m(x)** , **C(x** , **x)** + _�_ ) where _δ_ ( _x[i]_ , _x[j]_ ) is the Kronecker delta. 

GP regression works by applying the Bayesian formalism of assigning a prior distribution to _f_ ∼ _GP_ ( _m_ , _C_ ) and using _MVN conditioning_ relative to a dataset _D_ = ( **x** , **y** ) to infer the posterior distribution of _f_ . The Gaussian structure of the prior and the Gaussian structure of (2) together with Bayes’ rule yield a Gaussian posterior _p_ ( **f** | _D_ ) ∝ _p_ ( **f** ) _p_ ( **y** | **x** , **f** ): 

Posterior distribution =[Prior distribution x Likelihood function] 

**==> picture [90 x 11] intentionally omitted <==**

The principal objective is to draw prediction about **f** ∗ ≡ _f_ ( **x** ∗) or future observations **y** ∗ ≡ _Y_ ( **x** ∗) at new inputs **x** ∗. By construction, **y** and **y** ∗ follow a joint MVN distribution: 

**==> picture [188 x 31] intentionally omitted <==**

where **C(x** , **x** ∗ **)** is the covariance matrix between _f_ ( **x** ) and _f_ ( **x** ∗), **C** ∗∗ is the covariance matrix of _f_ ( **x** ∗), _�_ ∗∗ = diag( _σ_[2] ) is the noise variance matrix of the test inputs **x** ∗ and **m** ∗ = _m_ ( **x** ∗). The MVN formulas then imply that 

**==> picture [319 x 29] intentionally omitted <==**

**==> picture [341 x 13] intentionally omitted <==**

Note that the posterior variance **C** ∗ **(x** ∗, **x** ∗ **)** is equal to the prior variance **C** ∗∗ + _�_ ∗∗ minus a positive term which reflects the information gained (relative to the prior) from the training data. Furthermore, (3)–(4) are valid for _any_ **x** ∗, i.e. both for in-sample smoothing or for out-of-sample extrapolation. 

**Covariance function.** The kernel _C_ ( _x_ , _x_[′] ) captures the correlation between mortality rate at a given Age and Year and mortality rates at other coordinates. For example, we expect the mortality for age 70 in 2010 or _x[i]_ = (70, 2010), to be more correlated with _x[j]_ = (69, 2011) than with _x[j]_ = (50, 1995). In this paper, we employ the squared-exponential (SE) kernel: 

**==> picture [301 x 33] intentionally omitted <==**

When˜ _x[i]_ ≈ _x[j]_ , the covariance reaches its maximum value _η_[2] ; when _x[i]_ and _x[j]_ are far apart, _C_ ( _x[i]_ , _x[j]_ ) ≈ 0. This feature of expressing the dependence structure through a spatial perspective is central to GPs and is controlled by the hyperparameters _θag_ and _θyr_ in (5) that are called characteristic length-scales. The length-scales determine how much influence an observation has on others in the Age and Year dimensions, respectively. Note that _θag_ – length-scale for Age – and _θyr_ – length-scale for Year – are not comparable. An important aspect that influences the goodnessof-fit of a GP model is its spatial smoothness. The SE covariance kernel (5) makes the mortality curves infinitely differentiable in both Age and Year dimensions (note that the GP is defined over _x_ ∈ R[2] +[and so provides a continuous interpolation of the observed data gridded by year). This will] 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 323 

be exploited below for computing mortality improvement factors. Moreover, the length-scales _θ_ affect the qualitative nature of the fitted _m_ ∗( · ). When length-scales are too large, the fitted curves are over-smoothed and the influence of individual data points attenuates (Rasmussen & Williams, 2005). As a result, there is less flexibility in _m_ ∗( · ); to compensate, the estimated observation noise is increased and the model under-fits. In contrast, too small length-scales indicate over-fitting of the spatial dependence, generating high-frequency oscillations in the fitted _m_ ∗( · ) and low observation noise _σ_[2] . 

## _**2.2 MOGP kernels**_ 

The idea of commonality in mortality experiences is equivalent to the existence of global longevity trends. In the context of a spatio-temporal model, it implies an underlying _shared_ covariance structure. This can be easily verified visually or statistically, see Huynh _et al_ . (2020) for comparison of 10+ European countries available in HMD where we observe both similar fitted mortality dynamics (e.g. similar mortality improvement curves over time) and similar estimated GP covariance hyperparameters. 

Let _L_ be the number of different populations considered. To jointly model the _L_ different outputs, { _fl_ }1≤ _l_ ≤ _L_ we correlate them using the framework of MOGPs which was introduced in geostatistics under the name of multivariate kriging or co-kriging (Chiles & Delfiner, 1999; Hoef & Barry, 1998). The aim of co-kriging is to estimate the under-sampled variables using spatial correlation with other sampled variables. 

The vector-valued latent response over the Age–Year input space is defined as: 

**==> picture [283 x 13] intentionally omitted <==**

where the functions { _fl_ } _[L] l_ =1[are][the][log-mortality][surface][for][the][corresponding][population] _[l]_[.] Similar to single-output GP (SOGP), MOGP assumes that the vector-valued **f** follows a GP: 

**==> picture [56 x 10] intentionally omitted <==**

where **m** ∈ R _[LN]_[×][1] is the mean vector whose elements { _ml_ ( **x** )} _[L] l_ =1[are the mean functions of each] output, and **C** ∈ R _[LN]_[×] _[LN]_ is the fused covariance matrix. 

Populations are treated as categorical input, encoded via _L_ additional input dimensions with 0/1 encoding. Thus, the input vector for the _n_ th observation in the joint model is _x[n]_ = ( _xag[n]_[,] _[ x] yr[n]_[,] _[ x] pop[n]_ ,1[,] _[ . . .]_[ ,] _[ x] pop[n]_ , _L_[), where] _[ x] pop[n]_ , _l_[=][ 1][{][population][=] _[l]_[}][are indicators, set to 1 if and only if the] _n_ th observation is from population _l_ . We denote by _Nl_ the number of Age–Year inputs for population _l_ . If all _L_ populations have the same set of inputs and _N_ 1 = _. . ._ = _NL_ = _N_ , the dataset is said to be _isotropic_ . 

To construct the fused **C** , one approach is to take the product between a kernel for the Age– Year covariates _xag_ , _xyr_ and a kernel for the categorical ones (Qian _et al_ ., 2008; Roustant _et al_ ., 2018). Let: 

**==> picture [320 x 26] intentionally omitted <==**

with 

**==> picture [282 x 31] intentionally omitted <==**

**==> picture [245 x 21] intentionally omitted <==**

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

324 Nhan Huynh and Mike Ludkovski 

Then, the covariance between input rows _x[i]_ and _x[j]_ is set as follows: 

**==> picture [352 x 78] intentionally omitted <==**

When observations are from the same country, the covariance between the _i_ th and _j_ th observation is the same as in a SOGP model, cf. equation (5). Intuitively, _�l_ 1, _l_ 2 _<_ 1 discounts the covariance when observations are from different populations and is driven by the hyperparameter _θl_ 1, _l_ 2: large value of _θl_ 1, _l_ 2 implies low correlation _rl_ 1, _l_ 2 := exp� − _θl_ 1, _l_ 2� between the two populations. 

Two important assumptions are made in equation (7). First, there is separability (Alvarez _et al_ ., 2011) between the cross-population covariance and the covariance over the Age–Year inputs. Second, observations across _L_ populations share the same spatial covariance kernel. This assumption is useful to examine the commonality in the mortality across populations via the length-scales in Age and Year dimensions. It can be thought of as full statistical shrinkage of the individual population covariances towards a common baseline, cf. section 4.1 below. 

We note that unlike the Li & Lee (2005) framework and its extensions that explicitly assume a common factor shared by all populations, the GP framework is more similar to co-integration frameworks that postulate statistical dependence across _fℓ_ ’s. In that sense, GP modelling is more amenable to handling larger collections of populations where more complex mortality clustering may be present, see section 3.1. 

## _**2.3 Coregionalised kernels**_ 

Estimating cross-population covariance in (7) requires fitting _L_ ( _L_ − 1) _/_ 2 parameters _θl_ 1, _l_ 2, 1 ≤ _l_ 1 ≤ _l_ 2 ≤ _L_ which imposes challenges in both statistical and computational aspects when modelling MOGP with many outputs (e.g. _L_ ≥ 4). An attractive dimension reduction approach to keep the number of correlation parameters low is the ICM (Alvarez _et al_ ., 2011). In ICM, each output _fl_ is assumed be a linear combination of independent latent GPs. Let _u_ 1( **x** ), _. . ._ , _uQ_ ( **x** ) be independent latent functions each from a GP prior with covariance kernel _C_[(] _[u]_[)] ( **x** , **x**[′] ). The modelled outputs _fl_ are linear combinations of these _Q_ latent factors: 

**==> picture [300 x 33] intentionally omitted <==**

where _al_ , _q_ ’s are the factor loadings. Let **a** _q_ = ( _a_ 1, _q_ , _. . ._ , _aL_ , _q_ ) _[T]_ be the vector representing the collection of linear coefficients associated with the q _th_ latent function across the _L_ outputs, so that **f(x)** =[�] _[Q] q_ =1 **[a]** _[q][u][q]_[(] **[x]**[). It follows that the covariance for] **[ f(x)]**[ is] 

**==> picture [329 x 89] intentionally omitted <==**

where matrix _A_ = ( **a** 1, _. . ._ , **a** _Q_ ) and ⊗ is the Kronecker matrix product. Re-parametrising by _B_ := _AA[T]_ , (9) can be expressed as the Kronecker product between the cross-population covariance 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 325 

_B_ ∈ R _[L]_[×] _[L]_ and the covariance over the Age–Year inputs **C**[(] _[u]_[)] ∈ R _[N]_[×] _[N]_ : 

**==> picture [263 x 13] intentionally omitted <==**

The _coregionalisation matrix B_ has rank _Q_ . Under ICM, the number of hyperparameters in the cross-population covariance is reduced from _L_ ( _L_ − 1) _/_ 2 to _Q_ × _L_ . Hence, taking _Q < L/_ 2 allows to reduce the hyperparameter space and alleviate the computational budget compared to the “full rank” setup. 

ICM is a special form of the linear coregionalisation model (LCM) (Alvarez _et al_ ., 2011). In LCM, the independent latent functions are from different GP priors to capture all possible variability from multiple outputs. Its application is beyond the scope of this paper. Notably, the assumption in ICM that all _L_ populations share the common spatial covariance suits our interest in the inference of joint length-scales in Age and Year dimensions. The computational complexity required in ICM is greatly simplified due to the properties of the Kronecker product. Finally, ICM allows the process variance _ηl_[2][to][vary][by][populations,][i.e.,][the][l] _[th]_[element][in][the][diagonal][in] _[B]_ is the process variance for population _l_ . This further bolsters the flexibility in MOGP to excel in out-of-sample forecasts. 

The Kronecker decomposition in (10) is also highly useful to speed up the overall fitting. The most expensive step in building a MOGP is solving for the inverse of the covariance matrix **C** that shows up in the log-likelihood function. Indeed, inverting this _LN_ × _LN_ matrix is computationally expensive even for modest values of _L_ and _N_ . Since the inverse of the Kronecker product is equal to the product of the respective inverses: � _B_ ⊗ _C_[(] _[u]_[)][�][−][1] = _B_[−][1] ⊗ � _C_[(] _[u]_[)][�][−][1] , the ICM structure reduces the computational complexity from _O_ (( _LN_ )[3] ) to _O_ ( _L_[3] + _N_[3] + _LN_ ). In our experience, this translates to a factor of 2–4 speed-up in computational time, allowing us to scale up to 10–12 populations. We emphasise that the overall MOGP (and ICM) structure is completely agnostic to _L_ , so that exactly the same numerical method is applied to handle _L_ = 2 populations or _L_ = 10. 

**Selecting ICM rank** _**Q**_ . Because _Q_ is not one of the hyperparameters to be optimised, we exploit the Bayesian information criterion (BIC) to select the value of _Q_ for the most parsimonious models. To illustrate the role of the rank _Q_ of an ICM kernel, Table 1 compares several MOGP models with different _Q_ = 2, 3, 4. We consider two case studies, both with _L_ = 8 but with different constituent populations. First, we note the remarkably faster training time (3-time speedup) in ICM relative to a full-rank kernel; notably the speedup is independent of _Q_ and is driven by the Kronecker matrix algebra. Second, we note that most ICM models have better predictive performance (see sections 2.7 and 3.1 below for explanation of symmetric mean absolute percentage error (SMAPE) and CRPS) than the kernel from (7). Third, BIC criterion suggests that _Q_ = 2 is the preferred model in both cases. Note that there are only 2 _L_ = 16 hyperparameters in the resulting ICM kernel, almost twice as few as _L_ ( _L_ − 1) _/_ 2 = 28 hyperparameters in the respective (7). 

**Non-rectangular datasets.** We have discussed the use of ICM for isotropic data. The ICM framework can be extended to deal with partially heterotropic data where only a portion of _L_ inputs are available and which arises in HMD due to missing data especially at the most recent years. Let _M_[′] be the number of distinct inputs across _L_ populations and _M_ = _N_ 1 + _. . ._ + _NL_ be the number of observations in training data. We consider the setting that _M_[′] _< ML_ so that for some inputs not all _L_ outputs are observed. Define the vector-valued “complete data” function **f(x)** , with **f(x)** ∈ R _[LM]_[′×][1] . We further introduce **f** _[o]_ **(x)** as the vector-valued function corresponding to the observed outputs, **f** _[o]_ **(x)** ∈ R _[M]_[×][1] . The relation between **f(x)** and **f** _[o]_ **(x)** is formulated through the “communication” matrix _S_ , **f** _[o]_ **(x)** = _S[T]_ **f(x)** , where _S_ ∈ R _[LM]_[′×] _[M]_ . The column vectors in _S_ are orthonormal with values of 0 and 1 to eliminate the unobserved outputs, see Skolidis & Sanguinetti (2011). Applying linear transformation to a MVN vector, we can then identify the distribution of **f[o] (x)** as a GP with covariance: 

Cov( **f** _[o]_ **(x)** , **f** _[o]_ **(x**[′] **)** ) = _S[T]_ Cov( **f(x)** , **f(x**[′] **)** ) _S_ = _S[T]_ ( _B_ ⊗ _K_ ) _S_ 

recovering the Kronecker structure 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

326 Nhan Huynh and Mike Ludkovski 

**Table 1.** Comparison between full-rank and ICM MOGP models. Improvement in SMAPE and CRPS uses Hungary as the target population and compares MOGP with respect to SOGP Hungary model. The reported percentages are averages over 1-year ahead Hungarian mortality forecasts for Ages 70–84 based on three training sets: 1990–2013 (predict 2014), 1990–2014 (predict 2015) and 1990–2015 (predict 2016) for same Ages 70–84. Best metrics are in _italics_ 

||~~Full rank~~<br>~~ICM (~~~~_Q_ = 2)~~<br>~~ICM (~~~~_Q_ = 3)~~<br>~~ICM (~~~~_Q_ = 4)~~|||
|---|---|---|---|
||# Kernel hyperparameters<br>28<br>16<br>24<br>32|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Case study I: AUT, DEN, EST, GER, HUN, LTU, CZE, POL|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Running time (mins)<br>132.75<br>59.51<br>59.41<br>58.86|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Improvement in SMAPE (%)<br>−2.89<br>_10.75_<br>−1.54<br>1.93|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Improvement in CRPS (%)<br>2.79<br>_16.82_<br>11.09<br>16.63|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Total BICs<br>−<br>−_28_,_073_<br>−27, 719<br>−28, 006|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Case study II: EST, HUN, LTU, NED, POL, SWE, SUI, GBR|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Running time (mins)<br>176.78<br>59.03<br>58.99<br>58.98|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Improvement in SMAPE (%)<br>−24.90<br>−2.77<br>7.71<br>−32.76|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Improvement in CRPS (%)<br>−2.28<br>13.53<br>14.04<br>−2.95|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||Total BICs<br>−<br>−28, 890<br>−28, 346<br>−28, 361|||



## _**2.4 GP hyperparameters**_ 

To implement a GP model requires specifying its hyperparameters. Note that actual inference reduces to linear-algebraic formulas in (12)–(13), and the modelling task is to learn the spatial covariance, namely the mean and kernel functions. 

## _2.4.1 Mean function_ 

To capture the long-term longevity features, such as higher mortality at higher ages, we fit a parametric prior mean: 

**==> picture [99 x 33] intentionally omitted <==**

where _hj_ ’s are given basis functions and the _βj_ ’s are unknown coefficients. The coefficients _**β**_ = ( _β_ 1, _. . ._ , _βp_ ) _[T]_ are estimated simultaneously with other hyperparameters. Let **h** ( _x_ ) = � _h_ 1( _x_ ), _. . ._ , _hp_ ( _x_ )�, **H** = � **h** ( _x_[1] ), _. . ._ , **h** ( _x[N]_ )� and **D** = **(C** + _�_ **)**[−] **[1] H** , then the posterior mean of _**β**_ along with the predicted posterior mean _m_ ∗( _x_ ∗) and respective variance _s_[2] ∗[(] _[x]_[∗][)][for][a][new][input] _x_ ∗ are 

**==> picture [326 x 13] intentionally omitted <==**

**==> picture [348 x 31] intentionally omitted <==**

We note that the mean and kernel functions _interact_ : choosing the mean function is analogous to de-trending, and choosing the covariance function is analogous to modelling the residuals. An informative mean function will imply that the residuals are smaller (lower _η_[2] ) and de-correlated (small _θ_ ’s) compared to assuming a constant mean, which will lead to high _η_[2] and larger _θ_ ’s. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 327 

Within a multi-population model, we use a linear mean function to take into account the different trends across populations: 

**==> picture [277 x 32] intentionally omitted <==**

Analogous to the coefficients of categorical covariates in regression, _βpop_ , _l_ can be interpreted as the mean difference between log-mortality in population _l_ and the baseline. Note that (14) implies the _same_ shared Age structure – mortality rates rising exponentially in _xag_ with slope _β_ 1 _[ag]_[in all] populations. 

## _2.4.2 Observation likelihood_ 

We assume a constant observation noise within each population _σl_ = StDev( _ϵ[i]_ ) for all _i_ in (2) where _x[i] pop_ , _l_[=][ 1. This accounts for heterogeneous characteristics when observations from multiple] populations are combined, in particular _σl_ is smaller for larger populations (Huynh _et al_ ., 2020). The _σl_ ’s are estimated via maximum likelihood or Markov Chain Monte Carlo along with all other hyperparameters. While assuming homogeneity of noise variance in terms of Age and Year is not entirely realistic, based on the discussion in Ludkovski _et al_ . (2018), the impact of more complex observation models is minimal. A common alternative is to assume a Poisson likelihood; however it is well known that mortality data are overdispersed, so a Poisson parametrisation is also mis-specified. 

## _2.4.3 Estimating the parameters_ 

In single-population GP, the set of hyperparameters is _�_ = ( _θag_ , _θyr_ , _η_[2] , _σ_[2] , _**β**_ ). We can learn values of the hyperparameters via optimisation of the marginal likelihood function which is the integral of the likelihood times the prior: _p_ ( **y** | **x** , _�_ ) = � _p_ ( **y** | **f** , _�_ ) _p_ ( **f** | **x** , _�_ ) _d_ **f** . Since _p_ ( **y** | **x** , _�_ ) = _N_ ( **m** , **C** + _�_ ) and if we assume the mean function is known or fixed, the log-likelihood of the marginal is simply a MVN density: 

**==> picture [330 x 22] intentionally omitted <==**

Thus, we have to solve a system of nonlinear equations to maximise (15) which yields the maximum likelihood estimate (MLE). We implement SOGP fitting via the function km() from the package DiceKriging (Roustant _et al_ ., 2012) in R. That package carries out MLE of _�_ using a genetic optimisation algorithm. In MOGP with ICM kernel, the hyperparameters are _�_ = ( _θag_ , _θyr_ , ( _al_ , _q_ ), ( _σl_[2][),] _**[ β]**_[).][We][use][the][R][package][kergp][(Deville] _[et][al]_[.,][2019][)][to][carry][out][the] respective MLE via Kronecker decompositions. 

## _**2.5 Bayesian GP regression**_ 

The GP hyperparameters summarise the covariance structure of the fitted mortality model. The MLE method provides a point estimate _�MLE_ of that structure, i.e. a “best guess” of a GP surface that fits the data. Uncertainty quantification is a major component of our analysis, in particular in assessing how similar or different are the various populations. To this end, we aim to quantify model risk, i.e. the range of GP models that are consistent with the data via a Bayesian formulation. The Bayesian GP starts with a prior on _�_ and then integrates out the likelihood of the observed data to obtain the posterior distribution of the hyperparameters. A point estimate of _�_ is additionally obtained from the maximum a posteriori (MAP) hyperparameters, _�MAP_ = argmax _�_ � _i_[log] _[ p]_[(] _[y][i]_[|] _[�]_[)] _[p]_[(] _[�]_[). In fact, MLE can be viewed as a special case of MAP with] 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

328 Nhan Huynh and Mike Ludkovski 

improper uniform priors. In our analysis, we employ weakly informative priors to minimise influence of a priori assumptions (so that the data speaks for itself) but still regularise inference by keeping hyperparameters within reasonable ranges. 

In practice, computing the posterior density _p_ ( _�_ | _D_ ) requires to evaluate an intractable multidimensional integral. MCMC algorithms bypass this challenge by drawing samples _�_[(1)] , _�_[(2)] , _. . ._ , _�_[(] _[M]_[)] from the posterior. Traditionally, MCMC sampling for GP models was challenging due to strong correlation among the hyperparameters. Recently, powerful new techniques, in particular Hamiltonian Monte Carlo (HMC), have been developed to overcome this challenge. We implement Bayesian GP using Stan (Carpenter _et al_ ., 2017) that is built upon efficient HMC. Stan is a free, open-source software, written in C++ language, and has risen to be one of the most efficient toolboxes to perform Bayesian inference and optimisation for statistical models. 

Following Stan recommendations, we standardise the input covariates by subtracting the mean and dividing by the standard deviation, _xag[i]_ , _std_[:][=][(] _[x] ag[i]_[−] _[μ]_ **[x]** _ag_[)] _[/σ]_ **[x]** _ag_[to reduce the autocorre-] lation between the hyperparameters and thus increase the efficiency in the MCMC chains. HMC in Stan further helps to cope with this autocorrelation. Stan returns a set of posterior MCMC samples for _**β**_ and _�_ based on standardised data, so we then have to convert these values back to the original scales. For instance, the sampled hyperparameters _β_ · _[std]_ of the linear mean function are transformed back by: 

**==> picture [209 x 34] intentionally omitted <==**

Thus, _β_ 1 _[ag]_[=] _[β] σ_ 1 _[ag]_ **x** _ag_[,] _[std]_[and] _[ β]_[0][ =] _[ β]_ 0 _[std]_ − � _βσ_ 1 _[ag]_ **x** _ag_[,] _[std]_ � _μ_ **x** _ag_ ; in similar fashion, we can transform the lengthscales in the covariance kernel: _θag_ = _σ_ **x** _ag θag[std]_[and] _[ θ][yr]_[ =] _[ σ]_ **[x]** _yr[θ] yr[std]_[.] 

## _2.5.1 Bayesian versus MLE MOGP_ 

To illustrate uncertainty quantification of a MOGP using a Bayesian Stan framework, we build a joint model on four Male populations from Denmark, France, Sweden and UK. The MOGP model uses the full-rank kernel (7) trained on Ages 70–84 and Years 1990–2012. For Bayesian hyper-priors we take _β_ 0 ∼ _N_ ( − 4, 0.5), _β_ 1 _[ag]_[∼] _[N]_[(0, 0.5). Inverse-Gamma priors are chosen for the] covariance hyperparameters: _θag[std]_[∼][Inv-Gamma(9, 12),] _[θ] yr[std]_[∼][Inv-Gamma(9, 12)][which][ensures] that 99% of the respective prior is concentrated between 0.01 and 3.3 (Betancourt, 2017). For the process variance, we take log _η_[2] ∼ _N_ ( − 3, 1), and for observation noise _σ_[2] ∼ _N_ +(0, 0.5). Finally, for the population length-scales in (7), we use log _θl_ 1, _l_ 2 ∼ _N_ ( − 1, 1) for all _l_ 1, _l_ 2. (Implementing a Stan model for ICM kernels is beyond the scope of this work.) 

Table B.1 in the Appendix reports all the resulting hyperparameters using the kergp engine in R and the Stan HMC. We observe that all MLE fits are within the 95% posterior credible intervals from the Stan model. Also, the 95% credible interval for _β_ 1 _[ag]_[confirms the significance of the linear] effect of Age. Treating Denmark as the baseline country in the mean function, the 95% CIs of all coefficients _βpop_ , _l_ ’s contain 0, implying that the differences in mortality between Denmark and other populations are not statistically significant. This indicates that there is no clear difference in the respective mortality experience which is intuitive since all populations are from developed countries within the same geographic area. 

## _**2.6 Kernel selection**_ 

The choice of the kernel family is the centrepiece of GP modelling. In this article, we employ the SE kernel, but manifold alternatives exist. Investigating which kernel is best is beyond the scope 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 329 

of this paper which focuses on how to capture the multi-population aspect, while kernel selection is best analysed within a single-population setting. Indeed, our main construction in (7) relies on multiplying the single-output kernel _C_[˜] with the cross-population covariance structure _�_ , so that one can straightforwardly substitute _any C_[˜] . 

To this end, let us briefly discuss three useful ways to do so. First, one may consider other kernel functions, such as the Matérn family (Rasmussen & Williams, 2005); in particular Matérn-5/2 is a common default choice in a machine learning context. Compared to SE which yields infinitely differentiable _m_ ( · ), Matérn-5/2 gives predictive means that are only twice differentiable. In particular, this implies that the respective MI would be just once-differentiable and might exhibit higher-order discontinuities. Empirically, that leads to more “wiggly” fits that visually fit the historical data closer. Because mortality is expected to change slowly and smoothly, such behaviour might not be desirable, although a comprehensive analysis is needed to assess which kernel works better. 

Second, one may employ _composite_ kernels, i.e. go beyond the simple form of the SE kernel through adding and multiplying several covariance functions. We refer to Duvenaud (2014) for a comprehensive guide. For instance, one may embed a linear trend in Age directly inside the covariance function by taking 

**==> picture [338 x 33] intentionally omitted <==**

This allows to set the priors of the mean parameters within the covariance kernel. 

Third, one may design _custom_ covariance functions that target special features of mortality surfaces. For example, it is well known that many populations exhibit a birth cohort effect, whereby mortality is a function not just of Age and Year, but also of Birth Year = Year − Age. Thus, one could consider a kernel that incorporates dependence on Birth Year. One example is 

**==> picture [356 x 32] intentionally omitted <==**

This would work exactly like the analysis below, except one must fit three length-scale hyperparameters _θ_ . Note that because the covariates enter into the covariance function nonlinearly, there is no issue with parameter identification. 

As mentioned, all the above generalisations would be computationally trivial to add. Some effort might be necessary to obtain the analytic expressions for mortality improvement (MI, i.e. the gradient of _C_[˜] ). Rigorous model selection would require to focus on a given performance metric (such as SMAPE) and would also need to account for the varying model complexity. Appendix C provides illustrations of employing alternative kernel families, namely a Matern-5/2 kernel, an additive linear + SE kernel and the Birth Cohort kernel from (17). Based on numerical experiments, we find that all the above modifications play a second-order role in the quality of the model. 

## _**2.7 Performance metrics**_ 

To assess model performance we employ two metrics. First, we consider out-of-sample predictive accuracy, comparing realised future mortality to its mean model forecast. The most common choice is root mean squared error (RMSE); however RMSE is highly sensitive to outliers and also to the fact that mortality errors will be necessarily larger at higher Ages due to smaller exposed cohorts. To remedy this, we employ the mean absolute percentage error (MAPE) metric, specifically its symmetric (SMAPE) version that corrects for the tendency of MAPE to put heavier penalties on over-estimating the observations (Armstrong & Collopy, 1992; Makridakis, 1993): 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

330 Nhan Huynh and Mike Ludkovski 

**==> picture [282 x 32] intentionally omitted <==**

where _y_ ∗ _[i]_[is the realised observed value at test input] _[ x]_ ∗ _[i]_[and] _[ m]_[∗][(] _[x]_ ∗ _[i]_[) is the predicted log-mortality] rate by the model. Unlike the squared errors, SMAPE is a scale-independent measure that is convenient to compare across different datasets. 

In addition to SMAPE, we also use the CRPS metric to assess the quality of the probabilistic forecasts produced by a MOGP. Indeed, one of the major benefits of GP-based mortality models is a full distribution for future observations _y_ ∗( _x_ ∗) which allows a more detailed uncertainty quantification beyond just looking at the predictive mean _m_ ∗( _x_ ∗). CRPS is an example of a proper scoring rule and is defined as 

**==> picture [281 x 24] intentionally omitted <==**

where _F_ is the predictive (cumulative) distribution and _y_ ∗ is the realised outcome. Averaging over many outcomes, CRPS can be interpreted as the squared difference between the forecasted and the empirical cumulative distribution functions. In particular, CRPS penalises both bias and excessive predictive variance. A model with lower mean CRPS is judged to be better. 

**Mortality improvement factors.** A common way to interpret a mortality surface is via the (annual) mortality _improvement factors_ which measure longevity changes year-over-year. In terms 

exp � _y_ ( _xag_ ; _xyr_ )� of the observations, the raw annual percentage mortality improvement is 1 − exp ~~�~~ _y_ ( _xag_ ; _xyr_ −1) ~~�~~ . The smoothed improvement factor is obtained by replacing _y_ ’s by the GP model posterior _m_ ∗’s: exp ( _m_ ∗( _xag_ ; _xyr_ )) _∂m[GP] back_[(] _[x]_[) :][=] 1 − (20) � exp ( _m_ ∗( _xag_ ; _xyr_ − 1)) � 

## **3. Maximising Predictive Accuracy through Joint Modelling** 

We begin our illustrations by showcasing the improved predictive accuracy available from fusing data from two populations. Our first case study includes Male mortality modelling across Sweden and Denmark ( _l_ = 1: Denmark and _l_ = 2: Sweden). The two countries share similar demographic characteristics and are Nordic neighbours. Our mean function takes into account the separation in mortality between Denmark and Sweden: 

**==> picture [270 x 15] intentionally omitted <==**

Analogous to a coefficient of categorical covariates in regression, _βpop_ ,2 ≡ _βSWE_ can be interpreted as the mean difference between log-mortality in Sweden and in the baseline country, Denmark. Our second case study looks at joint Male/Female modelling for Denmark; in that case _βpop_ ,2 ≡ _βFEM_ is the mean difference between female log-mortality and male log-mortality. 

Figure 1 shows the raw observations together with the GP-based predictive intervals for the first case study. Specifically, we plot the 95% predictive credible bands for _y_ ∗( _x_ ∗) for three representative ages. The forecast period includes both in-sample (1990–2012) and out-of-sample (2013–2020). We observe that while for Denmark the differences between SOGP and MOGP forecasts are very slight, in Sweden the two forecasts differ noticeably out-of-sample. Table 2 compares the predictive accuracy between the models and indicates that the MOGP forecast is more accurate (smaller SMAPE) in both populations. 

To highlight further differences between SOGP and full MOGP, Figure 2 examines the respective predicted annual mortality improvement factors _∂m[GP] back_[(] _[x]_[).][We][compare][SWE] and DEN SOGPs against a two-population DEN+SWE MOGP, and a four-population 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 331 

**Table 2.** Prediction accuracy via SMAPE for SOGP and two-population full-rank models. The test set is Ages 70–84 in Years 2013, 2015 and 2016. More accurate predictions with smaller SMAPE values are in boldface. 

|~~SMAPE~~<br>~~2013 (1-year out)~~<br>~~2015 (3-year out)~~<br>~~2016 (4-year out)~~|
|---|
|SOGP<br>MOGP<br>SOGP<br>MOGP<br>SOGP<br>MOGP|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|Age<br>∈[70, 84]<br>Denmark<br>1.5798<br>**1.4451**<br>1.3445<br>**1.2862**<br>1.2584<br>**1.1955**|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|~~Sweden~~<br>~~1.0450~~<br>~~**0.8256**~~<br>~~1.9752~~<br>~~**1.1011**~~<br>~~2.5272~~<br>~~**0.9038**~~|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|SOGP<br>MOGP<br>SOGP<br>MOGP<br>SOGP<br>MOGP|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|Age<br>∈[70, 84]<br>Female<br>0.9422<br>**0.8834**<br>1.8973<br>**1.7845**<br>1.4010<br>**1.2269**|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|Male<br>1.5802<br>**1.5062**<br>1.3444<br>**1.2454**<br>1.2583<br>**1.1819**|



**Figure 1.** 95% credible intervals for observed log-mortality _y_ ( _x_ ∗) across the individual SOGP and full MOGP models. Top row: Denmark Males; bottom row: Sweden Males. Up to 2011, the smoothed mortality curves and CIs are essentially identical. 

DEN+FRA+GBR+SWE MOGP model, cf. Table B.1 in the Appendix. Large _θag_ length-scales in SOGP models lead to essentially linear improvement rate factors (blue curves). In the SWE + DEN MOGP (green curves), the Age length-scale decreases and _s_ ∗( _x_ ∗) falls, so the improvement rate factors become more Age-dependent and with tighter credible bands. This effect becomes even stronger with four populations. The corresponding smoothed curves (coloured in red) are quite nonlinear, and in particular imply that improvement at young Ages ( _<_ 60) has slowed dramatically. This illustrates that a joint model is better able to distinguish between signal and “noise” and therefore pick up divergent changes in mortality faster, while a single-population model would often smooth latest changes away. 

## _**3.1 Selecting populations for a joint model**_ 

Intuitively, incorporating more information from different populations through a MOGP ought to produce more accurate predictions and reduce predictive uncertainty. To visualise 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

Nhan Huynh and Mike Ludkovski 

332 

**Table 3.** Prediction quality via 3-year average improvement in SMAPE and CRPS in ICM models with _L_ = 2, _. . ._ , 6 populations. The baseline models are SOGP for UK and Hungary, respectively 

||Improvement|Improvement||Improvement|Improvement|
|---|---|---|---|---|---|
||in SMAPE (%)|in CRPS (%)||in SMAPE (%)|in CRPS (%)|
|UK+1|−2.805|1.834|Hungary+1|7.501|8.293|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|UK+2|1.189|3.218|Hungary+2|1.839|8.543|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|UK+3|3.995|3.279|Hungary+3|3.913|7.218|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|UK+4|1.778|0.933|Hungary+4|2.677|15.559|
|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|
|UK+5|1.764|−4.271|Hungary+5|10.585|13.345|



**==> picture [373 x 124] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>Ind. GP Ind. GP<br>GP (2 Countries) GP (2 Countries)<br>GP (4 Countries) GP (4 Countries)<br>70 72 74 76 78 80 82 84 70 72 74 76 78 80 82 84<br>age age<br>0.045<br>0.030<br>0.035<br>0.020<br>0.025<br>0.010<br>Mortality Improvement Rate Mortality Improvement Rate<br>0.015 0.000<br>**----- End of picture text -----**<br>


**Figure 2.** Comparison of annual mortality improvement factors between different joint models. Besides the mean improvement factors _∂m[GP] back_[(] _[ag]_[;2012) (][20][) for Ages 70,] _[ . . .]_[ , 84, we also show the respective 95% posterior credible band. (a) Denmark] Males. (b) Sweden Males. 

how increasing _L_ affects the changes in SMAPE and CRPS, Table 3 reports the 3-year average improvement in these metrics as _L_ varies from 2 to 6. (ICM ranks _Q_ = _Q_ ( _L_ ) were selected each time using BIC.) Overall, we observe that information fusion is very helpful for Hungary, but not as much for UK. This links to the respective credibility of the target populations: observation noise _σl_[2][is large in Hungary but low in UK, so additional data will benefit the former more.] 

From a complementary perspective, Table 4 shows how the inferred cross-population correlations change as we add a new populations. We report results both for a full-rank MOGP and for ICM with _Q_ = 2, 3, 4. We observe that the correlation matrix is generally stable, although some correlations can be quite different moving from one rank to another. In the AUT-SUI-GBR model, the correlation between Switzerland and UK is _rSUI_ , _GBR_ = 0.76 when _Q_ = 2, but rises to 0.88 when _Q_ = 3. We further note a broad agreement between the correlation structure learned with an ICM and full-rank MOGP kernels. 

The factor loadings ( _al_ , _q_ ’s) in ICM provide insight regarding the dependence patterns across populations. The interpretation of ICM loadings is analogous to principal component analysis when attempting to describe the data through independent transformed latent functions. For example, we consider factor loadings in case study II in Table 1. The best ICM kernel has rank _Q_ = 2 suggesting that two latent factors are sufficient to explain variation over the eight countries considered. In fact, the first latent component is strongly correlated with Eastern-Central European countries while the second factor is the major contributor to the Western European population. This interpretation helps us identify two well-separated clusters among these eight countries, visualised in Figure 3 by plotting the ICM loadings _al_ ,2 against _al_ ,1. Note that these factor loadings can be translated into correlation and imply that Hungary is more correlated with members in the same cluster and less correlated with Western European populations. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 333 

**Table 4.** Cross-corelation among two to four populations in MOGP models. All models are fitted on Ages 70–84 and reported values are averages over 3 training sets covering 1990 through 2014–2016. Italics indicate the ICM model with the smallest BIC 

|||~~Full rank~~<br>~~ICM (~~~~_Q_ = 2)~~<br>~~ICM (~~~~_Q_ = 3)~~<br>~~ICM (~~~~_Q_ = 4)~~|~~Full rank~~<br>~~ICM (~~~~_Q_ = 2)~~<br>~~ICM (~~~~_Q_ = 3)~~<br>~~ICM (~~~~_Q_ = 4)~~||||
|---|---|---|---|---|---|---|
|||Austria, UK|||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rAUT_,_GBR_<br>0.8432<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|0.8612<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||Switzerland, UK|||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rSUI_,_GBR_<br>0.8535<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|0.8645<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||Austria, Switzerland, UK|||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rAUT_,_SUI_<br>0.9151|0.9677<br>_0.9680_||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rAUT_,_GBR_<br>0.8590|0.8968<br>_0.8460_||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rSUI_,_GBR_<br>0.8514<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|0.7585<br>_0.8841_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||Austria, Germany, Switzerland, UK|||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rAUT_,_GER_<br>0.9570|0.9991<br>_0.9869_<br>0.9888||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rAUT_,_SUI_<br>0.9280|0.9956<br>_0.9639_<br>0.9658||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rAUT_,_GBR_<br>0.8730|0.8330<br>_0.8917_<br>0.8827||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rGER_,_SUI_<br>0.9047|0.9986<br>_0.9395_<br>0.9447||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rGER_,_GBR_<br>0.8504|0.8091<br>_0.8340_<br>0.8267||||
|||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..||||
|||_rSUI_,_GBR_<br>0.8674|0.7792<br>_0.9047_<br>0.9187||||
|||Factor loadings for 2nd latent function**a**2|0.05<br>0.10<br>0.15<br>0.20<br>0.04<br>0.08<br>0.12<br>_NLD_<br>_SWE_<br>_GBR_<br>_SUI_<br>_EST_<br>_HUN_<br>_LTU_<br>_POL_||||
||||Factor loadings for 1st latent function**a**1||||



**Figure 3.** Factor loadings _al_ , _q_ in the eight-population ICM with _Q_ = 2 in Table 1 – Case study II. The factor with the higher loading for each country is bolded in the Table on the left. 

## _**3.2 Incorporating latest data from other populations**_ 

In HMD, the reported data from different countries arrive non-synchronously. Indeed, the last available year of data varies from one country to another. The prevailing approach is to consider the time period that is common to all countries that are being modelled. This implies that the most recent observations may be dropped for some countries. Of course, such recent data are in fact the most informative for picking up new insights about the present longevity trend. Note that the HMD datasets are updated continuously, so that which datasets have the latest observations changes dynamically over time. 

To assess the value of information fusion and its link to population cross-correlation, we investigate the improvement in prediction in MOGP over SOGP. To do so, we set up a “notched” two-population training set where the foreign population has one more year of data and the assessment is based on one-year-ahead prediction for the domestic target population. Note that 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

334 Nhan Huynh and Mike Ludkovski 

**==> picture [372 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>Hungary UK<br>Correlation 1.0 Correlation 1.0<br>AU T AU T CZE<br>.50.25 POL .50.25 BEL GERPO LSWE SWI<br>EST GER E ST NET SPA<br>FRA<br>LAT CZE SWI<br>FR A H UN DEN<br>NET B EL LIT<br>LIT DEN<br>S P A S W E<br>LAT<br>UK<br>−5 0 5 10 15 −40 −20 0 20<br>Average yearly improvement in SMAPE (%) Average yearly improvement in SMAPE (%)<br>(c)<br>50 Positive slopes<br>Negative slopes<br>40 Mean value<br>30<br>20<br>10<br>0<br>−10<br>12<br>4<br>10<br>2<br>8<br>6 0<br>4 −2<br>2 −4<br>0 −6<br>Average yearly improvement in CRPS (%) Average yearly improvement in CRPS (%)<br>Slopes<br>AUT BEL CZE DEN EST FRA GER HUN LAT LIT NET POL SPA SWE SWI UK<br>**----- End of picture text -----**<br>


**Figure 4.** Prediction improvements for Hungarian and UK Males and the impact of cross-correlation on the improvement in SMAPE across 16 European national populations. (a) Hungary: _σl_[2][=][ 2.083][ ×][ 10][−][3][. (b) UK:] _[ σ] l_[ 2][=][ 6.834][ ×][ 10][−][4][. (c) Linear slope] of improvement in SMAPE versus correlation. 

such “notch” extrapolation is not possible in the Lee–Carter framework that requires rectangular datasets. All ICM MOGP models take _L_ = 2 and are fitted on Ages 70–84 in three different time frames: period 1990–2013/2014 for 2014 forecast, 1990–2014/2015 for 2015 forecast and 1990– 2015/2016 for 2016 forecast. The comparator training datasets for SOGP models did not have mortality information in the calendar year of forecast (e.g. training on 1990–2013 for 2014 forecast). We report the resulting 3-year average percent improvement in CRPS and SMAPE between MOGP and SOGP. The positive average improvement is equivalent to MOGP models having smaller SMAPE and CRPS. 

Figure 4 displays the improvement in SMAPE and CRPS of two-population MOGPs versus SOGP. We plot the results against the correlation _rl_ 1, _l_ 2 between the two populations modelled in MOGP and consider two randomly chosen target populations: Males in Hungary and Males in UK. Shaded regions indicate which MOGP models have both SMAPE and CRPS values less than the baseline. We observe that joint modelling generally yields higher improvement in Hungary compared to UK which is driven by the former’s relatively smaller population which translates into larger _σl_ and more opportunity for information fusion. Thus, for UK the single-population model is often competitive in its forecasting performance with a two-population MOGP. 

The above discussion suggests that fusing highly correlated populations is better for predictive accuracy. To confirm this hypothesis, Figure 4(c) summarises the relationship between SMAPE improvement and correlation _rl_ 1, _l_ 2. We used all 16 populations as targets and built 16 × 15 twopopulation MOGPs to record the resulting MOGP-SOGP improvements in SMAPE like in the right and middle panels. For each target population, we then fitted a linear regression model treating the 3-year average improvement in SMAPE as the dependent outcome and the correlation as the independent variable: SMAPE CHANGE = _b_ 0 + _b_ 1 _rl_ 1, _l_ 2. Figure 4(c) displays the resulting slopes _b_ 1 across the 16 populations. Positive _b_ 1 implies that higher correlation leads to lower 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 335 

**==> picture [373 x 219] intentionally omitted <==**

**Figure 5.** Comparison of prediction accuracy for 2016 log-mortality of Hungarian Males between different ICM-MOGP models with “notched” setup. Top row: standard deviation of _f_ ( _x_ ∗); bottom row: distance between predicted mean _m_ ∗( _x_ ∗) and the observed value _y_ ∗( _x_ ∗). 

SMAPE, i.e. higher predictive accuracy. The mean value of the _b_ 1-slopes is highly positive and is around 20%. These empirical features suggest that one should indeed focus on aggregating _related_ populations and discard unrelated ones. This is consistent with the results in Table 1 earlier. Most populations in Case Study II are less correlated with Hungary compared to Case Study I and as a result the SMAPE improvement in Case Study I is higher (10.75%) compared to Case Study I − ( 2.77%). 

Moving beyond two populations, in Figure 5, we illustrate predictive gains for Hungarian Males due to incorporating most recent foreign data. This complements Table 3 that considered an isotropic dataset, with a notched setup instead. Our benchmark is a Hungary Males SOGP model fitted on 1990–2016. We then drop 2016 Hungary observations, but augment with 1990– 2016 data from _other_ countries and perform 1-year-out extrapolation to forecast 2016 Hungary mortality. These models are labelled as “HUN+1”, “HUN+2”, etc., to indicate the number of foreign populations considered. The top panels of Figure 5 visualise increasing forecast credibility, namely lower _s_ ∗( _x_ ∗), for Hungary as more and more correlated data are added. In fact, we see that a MOGP 1-year-out prediction with 3+ populations is _more_ credible than direct smoothing of realised 2016 Hungary experience. As expected, we observe that credibility gains flatten out as _L_ continues to grow and available information is saturated. The bottom panels of Figure 5 display the prediction errors _m_ ∗( _x_ ∗) − _y_ ∗( _x_ ∗) relative to realised 2016 Hungary experience. Again, we see that higher _L_ tends to generate less bias in prediction, confirm the earlier SMAPE analysis for isotropic case studies. Due to the strong observation noise, the pattern for a specific cell _x_ ∗ can be erratic, although in nearly all cases, MOGP easily beats out the plain SOGP. To conclude, borrowing latest information from nearby highly correlated populations is essentially as good as having the latest domestic data, and is significantly better than just using the available domestic data. 

_Remark:_ In Figure 5 (and earlier in Table 3), we add populations based on their correlation to the target population, i.e. we pool through estimated _θl_ 1, _l_ 2. In Appendix A, we discuss a simpler alternative based on comparing mean functions that capture historical mortality trends and then running a hierarchical clustering method. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

336 Nhan Huynh and Mike Ludkovski 

**==> picture [376 x 124] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>95% (outer) CI 40 95% (outer) CI<br>33 80% (inner) CI 80% (inner) CI<br>Posterior meanMLE 35 Posterior meanMLE<br>28 30<br>23 25<br>20<br>18<br>15<br>13<br>10<br>8 5<br>DEN FRA SWE UK & SWEDEN & UKDEN & FRADEN & UKFRA & SWEFRA SWE& UK ALL 4 DEN FRA SWE UK & SWEDEN & UKDEN & FRADEN & UKFRA & SWEFRA SWE& UK ALL 4<br>**----- End of picture text -----**<br>


**Figure 6.** Stan MCMC posteriors of the length-scales _θ_ for Age and Year across populations and joint models with different groupings. The +’s indicate the respective MLE estimates from a kergp model. The dashed lines indicate the MCMC MAP estimate from the four-population full-MOGP model. (a) Length-scale in the Age dimension. (b) Length-scale in the Year dimension. 

## **4. Further Features of MOGP Models** 

## _**4.1 Improved hyperparameter estimation**_ 

To illustrate the commonality in mortality experience in related populations, we perform Bayesian GP on four developed Western European countries: Sweden, Denmark, France and UK. Figure 6 shows the inferences of the length-scales for Age and Year along with MLE estimations when fitting SOGP models for each population versus jointly modelling them as groups of two, or jointly as all four together. The figures visualise how joint GP models produce tighter hyperparameter posteriors. For example, the posterior mean of _θag_ in Denmark is relatively large and its credible bands are wide compared to the other three countries (Figure 6(a)). However, once we pair Denmark with either Sweden, UK or France (Figure 6(a) – light blue, light green and purple CIs respectively), the credible bands of _θag_ become narrower and in the more reasonable range of _θag_ ∈ [15, 30]. This effect is even further amplified when taking all four countries together. The underlying concept is that the more populations are added into the model, the closer we get at discovering the “universal” representation of mortality pattern. In Figure 6, the four-population MAP estimates of the length-scales (dashed horizontal lines) intersect with a majority of CIs suggesting that there is indeed a common covariance structure which is gradually revealed as we increase the training dataset. We also remark that the MLE estimates fall within the 95% posterior credible intervals from the Stan model indicating that Bayesian inference works properly. 

This also highlights the ability of joint models to better estimate the hyperparameters by utilising multiple datasets. It is known that GPs might have difficulties in estimating length-scales, for example due to the likelihood function (15) being highly multi-modal, or conversely very flat around its maxima. Providing more data is one remedy. As discussed in Huynh _et al_ . (2020), some SOGP will over- or under-smooth data while pooling data across multiple populations achieves shrinkage towards the global hyperparameter mean and provides a better fit. 

## _**4.2 Coherent mortality forecasts**_ 

Fitting GP models for individual populations tends to generate divergent long-term forecasts that are inconsistent with historical patterns. MOGP models do not have this limitation and maintain the historical characteristics observed in the data into the future. Namely, in MOGP models, the long-term forecast is driven by the prior of _f_ , and specifically by the mean function _m_ ( · ). Thus, the relative differences in mortality between populations are controlled through the choice of _m_ ( · ), so that different ways of achieving coherence are transparent to the modeller. For the linear mean function in (14), the population coefficients _βpop_ , _l_ serve this purpose and represent the 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 337 

**==> picture [372 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>0.6 0.60<br>—<br>0.55<br>0.4<br>0.50<br>0.45<br>0.2<br>0.40<br>0.0 0.35<br>0.30<br>i<br>70 72 74 76 78 80 82 84 70 72 74 76 78 80 82 84<br>Age Age<br>2050 2050<br>2030 2030<br>Year Year<br>2010 2010<br>1990 1990<br>**----- End of picture text -----**<br>


**Figure 7.** Forecasted mean difference between Danish Male and Female mortality over 1990–2060. Training set was Ages 70–84 and Years 1990–2016 (edge of training set indicated by the dashed lines). (a) Male/Female difference in log-mortality in Denmark using individual (SOGP) models. (b) Male/Female difference in log-mortality in Denmark using a joint (full-rank MOGP) model. 

**==> picture [373 x 123] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) Age 70 (b) Age 70<br>Austria Germany Sweden UK Austria Germany Sweden UK<br>Denmark Netherlands Switzerland Denmark Netherlands Switzerland<br>Case I: Mean function linear in age Case I<br>Case II: Mean function linear in age & year Case II<br>Compromise between Case I and II Compromise between Case I and II<br>1990 2000 2010 2020 2030 2040 2050 2060 1990 2000 2010 2020 2030 2040 2050 2060<br>Years Years<br>−3.5 0.04<br>−4.0<br>0.02<br>Log−mortality<br>−4.5<br>0.00<br>YoY Mortality Improvement Rate<br>−5.0<br>−0.02<br>**----- End of picture text -----**<br>


**Figure 8.** Long-term mortality forecasting over years 1990–2060. The models are based on ICM kernel with _Q_ = 3 and are trained using Ages 70–84 and Years 1990–2016 over seven Male populations: Austria, Denmark, Germany, Netherlands, Sweden, Switzerland and UK. Dashed lines indicate the boundary between in-sample and out-of-sample forecasts. (a) Predicted log-mortality rate. (b) Annual mortality improvement factors. 

long-term spread between same-Age log-mortality rates. To illustrate the above, consider mortality differences due to gender. Women outlive men by 7 years on average in developed countries (United Nations, 2011). Modelling mortality for each gender separately fails to take into account this interdependence and tends to result in divergent and implausible long-run forecasts even if the same fitting procedure is applied. The heatmaps in Figure 7 display the projected Male–Female differences in log-mortality for Denmark; single-population models on the left imply that as early as 2030, Males will have lower mortality than females. In contrast, the MOGP forecast in the right panel is coherent: Females are projected to maintain higher longevity and historical patterns slow dissipate over time to the long-term gap of _βpop_ ,2 − _βpop_ ,1 = 41.5% between same-age Male and Female mortality. 

Figure 8 shows the log-mortality and annual mortality improvement rates for Males aged 70 across seven European populations (indicated by colours), in the period from 1990 to 2060. We build a seven-population MOGP based on three different scenarios for _m_ ( _x_ ): 

1. Zero long-term mortality improvement, captured by the linear mean function _m_ ( _x[n]_ ) = _L_ 

_β_ 0 + _β_ 1 _[ag][x] ag[n]_[+] _l_ =2 _[β][pop]_[,] _[l][x] pop[n]_ , _l_[(dashed lines). All mortality improvement factors converge] to zero (right panel) and the long-run mortality differences are summarised by the _βpop_ , _l_ 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

338 Nhan Huynh and Mike Ludkovski 

2. Long-term mortality improvement based on a historical pattern (thin solid curves). This is encapsulated via _m_ ( _x[n]_ ) = _β_ 0 + _β_ 1 _[ag][x] ag[n]_[+] _[ β]_ 1 _[yr][x] yr[n]_[+][ �] _[L] l_ =2 _[β][pop]_[,] _[l][x] pop[n]_ , _l_[.][In][the][long-run] _∂m[GP] back_[(.;] _[yr]_[)][ →] _[β]_ 1 _[yr]_[(about 2% annual); again] _[ β][pop]_[,] _[l]_[ determine the long-run relative difference] 

in longevity of different populations. 

3. Long-term mortality improvement based on expert judgement (thick solid lines). We again use _m_ ( _x[n]_ ) = _β_ 0 + _β_ 1 _[ag][x] ag[n]_[+] _[ β]_ 1 _[yr][x] yr[n]_[+][ �] _[L] l_ =2 _[β][pop]_[,] _[l]_ � _xpop[n]_ , _l_ �, but this time the _β_ 1 _[yr]_[coefficient][is] picked by the modeller and for illustrative purposes fixed at 1% to reflect recent slowdown in global MI. Since it is not possible to fully extrapolate the future longevity trends from past data, it is appropriate to use expert opinions about future mortality (Booth & Tickle, 2008). 

We observe that the choice of _m_ ( · ) has minimal impact on in-sample forecasts that are largely driven by the training data covering 1990–2016. On the other hand, the long-term levels of mortality improvement are _completely_ driven by _m_ ( · ). Finally, for short-term extrapolation (roughly 2016–2025 in the Figure, reflecting the fitted Year length-scale _θyr_ ≃ 10) the forecasts blend information from the training set and from _m_ ( · ). Note that in this example some of the individual mortality curves may cross, i.e. the relative order of longevity in different populations may change over time (such as Denmark surpassing Germany’s longevity) due to higher recent improvement rates. Nevertheless, we see a very strong coherence so that mortality rates across populations all move roughly in unison over time, matching our intuition about the persistent commonality of their future mortality experiences. 

_Remark:_ As noted throughout our analysis, the GP framework is based on exploiting the spatial correlation between data points. This data-driven nature of our model makes it not well-suited for long-range forecasts. The long-term prediction from the GP converges to its prior mean as the correlation between the historical training data and the future data points that are decades apart declines to zero. This de-correlation also leads to very high forecast uncertainty. With this in mind, the primary usage of our models is for “nowcasting” and medium-term (less than 10 years) uncertainty quantification of joint longevity experiences. Accurate short-term projections have been important for instance in the context of quantifying COVID-19 excess deaths, see https://nhanhuynh46.github.io/MOGPTutorials/SOGP_Covid19.html. 

## **5. Conclusion** 

We have developed and investigated stochastic multi-population mortality models based on MOGP regression. In our approach, cross-population dependence is captured via spatial correlation that overlays the Age–Year structure. This yields a unified approach for any number of populations _L_ ; moreover, the proposed coregionalisation kernels allow to leverage the Kronecker structure and incorporate dimension reduction for the underlying cross-population factors. Our analysis of HMD data suggests that the MOGP approach is well-suited to selectively fuse mortality experience from similar datasets, where similarity can be interpreted through the spatial GP correlations _rl_ 1, _l_ 2. On the one hand, we find that pooling disparate populations can be counter-productive (since MOGP relies on the assumption of homogeneous Age–Year covariance pattern); on the other hand, pooling can indeed yield significant improvement in predictive accuracy, especially in smaller populations with low credibility. 

Looking ahead, it would be worthwhile to investigate large-scale models, e.g. based on the full HMD database of 40 countries and 2 genders. This requires additional modelling infrastructure as the presented approach becomes computationally expensive for _L_ ≫ 10 populations (more than _N_ ≫ 5, 000 total cells). There is currently a very active and ongoing progress on large-scale GP models especially for gridded data like in HMD, see, e.g., Flaxman _et al_ . (2015). A different avenue of future research would be to systematically explore the best spatial covariance structures, as encapsulated by the kernel function _C_[˜] ( _x_ , _x_[′] ). In this paper, we focused on only using the SE kernel 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 339 

and standard Age- and Year-effects. It is feasible to consider further dependence formats, e.g. Birth Cohort effect (see Appendix C and Figure C.1 below), and other kernel families, such as the Matérn (Ludkovski _et al_ ., 2018). A third direction would be to revisit the observation variance assumption via GLM (generalised linear model) GP formulations. 

**Acknowledgement.** We thank the anonymous referees and the associate editor for many useful suggestions. We also thank Howard Zail for several informative discussions. Ludkovski is partially supported by NSF DMS-1821240. 

## **References** 

**Alvarez** , **M.A.** , **Rosasco** , **L.** & **Lawrence** , **N.D.** (2011). Kernels for vector-valued functions: a review. **Antonio** , **K.** , **Devriendt** , **S.** , **de Boer** , **W.** , **de Vries** , **R.** , **De Waegenaere** , **A.** , **Kan** , **H.-K.** , **Kromme** , **E.** , **Ouburg** , **W.** , **Schulteis** , **T.** , **Slagter** , **E. et al.** (2017). Producing the Dutch and Belgian mortality projections: a stochastic multi-population standard. _European Actuarial Journal_ , **7** (2), 297–336. **Armstrong** , **J.S.** & **Collopy** , **F.** (1992). Error measures for generalizing about forecasting methods: empirical comparisons. _International Journal of Forecasting_ , **8** (1), 69–80. **Betancourt** , **M.** (2017). Robust Gaussian processes in Stan. Available online at the address https://betanalpha.github.io/assets/ case_studies/gp_part3/part3.html. **Boe** , **C.** , **Winant** , **C.** , **Riffe** , **T.** , **Barbieri** , **M.** , **Wilmoth** , **J.R.** , **Jasilionis** , **D.** , **Grigoriev** , **P.** , **Jdanov** , **D.** , **Shkolnikov** , **V.M.** & **Glei** , **D.** (2015). Data resource profile: The Human Mortality Database (HMD). _International Journal of Epidemiology_ , **44** (5), 1549–1556. **Bonilla** , **E.V.** , **Chai** , **K.M.** & **Williams** , **C.** (2008). Multi-task Gaussian process prediction. In **J.C. Platt** , **D. Koller** , **Y. Singer** & **S.T. Roweis** (Eds.), _Advances in Neural Information Processing Systems 20_ (pp. 153–160). Curran Associates, Inc. **Boonen** , **T.J.** & **Li** , **H.** (2017). Modeling and forecasting mortality with economic growth: a multipopulation approach. _Demography_ , **54** (5), 1921–1946. **Booth** , **H.** & **Tickle** , **L.** (2008). Mortality modelling and forecasting: a review of methods. _Annals of Actuarial Science_ , **3** (1–2), 3–43. **Carpenter** , **B.** , **Gelman** , **A.** , **Hoffman** , **M.D.** , **Lee** , **D.** , **Goodrich** , **B.** , **Betancourt** , **M.** , **Brubaker** , **M.** , **Guo** , **J.** , **Li** , **P.** & **Riddell** , **A.** (2017). Stan: a probabilistic programming language. _Journal of Statistical Software_ , **76** (1). **Carracedo** , **P.** , **Debón** , **A.** , **Iftimi** , **A.** & **Montes** , **F.** (2018). Detecting spatio-temporal mortality clusters of European countries by sex and age. _International Journal for Equity in Health_ , **17** (1), 38. **Caruana** , **R.** (1997). Multitask learning. _Machine Learning_ , **28** (1), 41–75. ISSN 1573-0565. doi: 10.1023/A:1007379606734. **Chen** , **H.** , **MacMinn** , **R.** & **Sun** , **T.** (2015). Multi-population mortality models: a factor copula approach. _Insurance: Mathematics and Economics_ , **63** , 135–146. **Chiles** , **J.-P.** & **Delfiner** , **P.** (1999). _Geostatistics: Modeling Spatial Uncertainty_ . Wiley. ISBN 0471083151 9780471083153. **Christiansen** , **M.C.** , **Spodarev** , **E.** & **Unseld** , **V.** (2015). Differences in European mortality rates: a geometric approach on the age–period plane. _ASTIN Bulletin: The Journal of the IAA_ , **45** (3), 477–502. **Chu** , **W.** & **Ghahramani** , **Z.** (2005). Gaussian processes for ordinal regression. _Journal of Machine Learning Research_ , **6** , 1019–1041. **D’Amato** , **V.** , **Haberman** , **S.** , **Piscopo** , **G.** , **Russolillo** , **M.** & **Trapani** , **L.** (2016). Multiple mortality modeling in Poisson Lee–Carter framework. _Communications in Statistics-Theory and Methods_ , **45** (6), 1723–1732. **Debón** , **A.** , **Martnez-Ruiz** , **F.** & **Montes** , **F.** (2010). A geostatistical approach for dynamic life tables: the effect of mortality on remaining lifetime and annuities. _Insurance: Mathematics and Economics_ , **47** (3), 327–336. **Delwarde** , **A.** , **Denuit** , **M.** , **Guillén** , **M.** & Vidiella-i Anguera, A. (2006). Application of the Poisson log-bilinear projection model to the G5 mortality experience. _Belgian Actuarial Bulletin_ , **6** (1), 54–68. **Deville** , **Y.** , **Ginsbourger** , **D.** & **Roustant** , **O.** (2019). Contributors: Nicolas Durrande. _kergp: Gaussian Process Laboratory_ . Available online at the address https://CRAN.R-project.org/package=kergp. R package version 0.5.0. **Dong** , **Y.** , **Huang** , **F.** , **Yu** , **H.** & **Haberman** , **S.** (2020). Multi-population mortality forecasting using tensor decomposition. _Scandinavian Actuarial Journal_ , 2020(8), 754–775. **Duvenaud** , **D.K.** (2014). _Automatic Model Construction with Gaussian Processes_ . PhD thesis, University of Cambridge. **Enchev** , **V.** , **Kleinow** , **T.** & **Cairns** , **A.J.G.** (2017). Multi-population mortality models: fitting, forecasting and comparisons. _Scandinavian Actuarial Journal_ , **2017** (4), 319–342. **Flaxman** , **S.** , **Gelman** , **A.** , **Neill** , **D.** , **Smola** , **A.** , **Vehtari** , **A.** & **Wilson** , **A.G.** (2015). Fast hierarchical Gaussian processes, technical report, Preprint at http://sethrf.com/files/fast-hierarchical-GPs.pdf. **Garrido-Merchán** , **E.C.** & **Hernández-Lobato** , **D.** (2018). Dealing with categorical and integer-valued variables in Bayesian optimization with Gaussian processes. CoRR, abs/1805.03463. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

340 Nhan Huynh and Mike Ludkovski 

**Guibert** , **Q.** , **Lopez** , **O.** & **Piette** , **P.** (2019). Forecasting mortality rate improvements with a high-dimensional VAR. _Insurance: Mathematics and Economics_ , **88** , 255–272. 

**HMD** . (2018). The Human Mortality Database. University of California, Berkeley (USA), and Max Planck Institute for Demographic Research (Germany). Available online at the address www.mortality.org. 

**Hoef** , **J.M.V.** & **Barry** , **R.P.** (1998). Constructing and fitting models for cokriging and multivariable spatial prediction. _Journal of Statistical Planning and Inference_ , **69** (2), 275–294. ISSN 0378-3758. 

**Huynh** , **N.** , **Ludkovski** , **M.** & **Zail** , **H.** (2020). Multi-population longevity models: a spatial random field approach. In _Proceedings of the Society of Actuaries 2020 Living to 100 Symposium_ . 

**Hyndman** , **R.J.** , **Booth** , **H.** & **Yasmeen** , **F.** (2013). Coherent mortality forecasting: the product-ratio method with functional time series models. _Demography_ , **50** (1), 261–283. 

**Kleinow** , **T.** (2015). A common age effect model for the mortality of multiple populations. _Insurance: Mathematics and Economics_ , **63** , 147–152. 

**Kleinow** , **T.** & **Cairns** , **A.J.G.** (2013). Mortality and smoking prevalence: an empirical investigation in ten developed countries. _British Actuarial Journal_ , **18** (2), 452–466. 

**Letham** , **B.** & **Bakshy** , **E.** (2019). Bayesian optimization for policy search via online-offline experimentation. 

**Li** , **H.** & **Lu** , **Y.** (2017). Coherent forecasting of mortality rates: A sparse vector-autoregression approach. _ASTIN Bulletin: The Journal of the IAA_ , **47** (2), 563–600. **Li** , **J.** (2013). A Poisson common factor model for projecting mortality and life expectancy jointly for females and males. _Population Studies_ , **67** (1), 111–126. **Li** , **N.** & **Lee** , **R.** (2005). Coherent mortality forecasts for a group of populations: an extension of the Lee-Carter method. _Demography_ , **42** (3), 575–594. **Lu** , **Q.** , **Hanewald** , **K.** & **Wang** , **X.** (2019). Bayesian hierarchical multi-population mortality modelling for china’s provinces. SSRN. Available online at the address doi: http://dx.doi.org/10.2139/ssrn.3494491. **Ludkovski** , **M.** , **Risk** , **J.** & **Zail** , **H.** (2018). Gaussian process models for mortality rates and improvement factors. _ASTIN Bulletin: The Journal of the IAA_ , **48** (3), 1307–1347. **Makridakis** , **S.** (1993). Accuracy measures: theoretical and practical concerns. _International Journal of Forecasting_ , **9** (4), 527–529. **Qian** , **P.Z.G.** , **Wu** , **H.** & **Jeff Wu** , **C.F.** (2008). Gaussian process models for computer experiments with qualitative and quantitative factors. _Technometrics_ , **50** (3), 383–396. **Qin** , **C.** & **Jevtic** , **P.** (2016). Multi-population mortality modelling with levy processes. SSRN. Available online at the address doi: http://dx.doi.org/10.2139/ssrn.2813678. **Raftery** , **A.E.** , **Li** , **N.** , **Ševˇcková** , **H.** , **Gerland** , **P.** & **Heilig** , **G.K.** (2012). Bayesian probabilistic population projections for all countries. _Proceedings of the National Academy of Sciences_ , 109, 13915–13921. **Rasmussen** , **C.E.** & **Williams** , **C.K.I.** (2005). _Gaussian Processes for Machine Learning (Adaptive Computation and Machine Learning)_ . The MIT Press. **Roustant** , **O.** , **Ginsbourger** , **D.** & **Deville** , **Y.** (2012). DiceKriging, DiceOptim: two R packages for the analysis of computer experiments by kriging-based metamodeling and optimization. _Journal of Statistical Software_ , **51** (1), 1–55. **Roustant** , **O.** , **Padonou** , **E.** , **Deville** , **Y.** , **Clément** , **A.** , **Perrin** , **G.** , **Giorla** , **J.** & **Wynn** , **H.P.** (2018). Group kernels for Gaussian process metamodels with categorical inputs. Working Paper or preprint, July 2018. Available online at the address https://hal.archives-ouvertes.fr/hal-01702607. **Shang** , **H.L.** (2016). Mortality and life expectancy forecasting for a group of populations in developed countries: a multilevel functional data method. _The Annals of Applied Statistics_ , **10** (3), 1639–1672. **Skolidis** , **G.** & **Sanguinetti** , **G.** (2011). Bayesian multitask classification with Gaussian process priors. _IEEE Transactions on Neural Networks_ , **22** (12), 2011–2021. ISSN 1941-0093. 

**Tsai** , **C.C.-L.** & **Wu** , **A.D.** (2020). Incorporating hierarchical credibility theory into modelling of multi-country mortality rates. _Insurance: Mathematics and Economics_ , **91** , 37–54. ISSN 0167-6687. **Tsai** , **C.C.-L.** & **Zhang** , **Y.** (2019). A multi-dimensional bhlmann credibility approach to modeling multi-population mortality rates. _Scandinavian Actuarial Journal_ , **2019** (5), 406–431. **United Nations** . (2011). _World Population Prospects: The 2010 Revision, Volume I: Comprehensive Tables_ . Department of Economic and Social Affairs, Population Division. ST/ESA/SER.A/313. **Wang** , **C.-W.** , **Yang** , **S.S.** & **Huang** , **H.-C.** (2015). Modeling multi-country mortality dependence and its application in pricing survivor index swapsÂ”–a dynamic copula approach. _Insurance: Mathematics and Economics_ , **63** , 30–39. **Wang** , **P.** , **Pantelous** , **A.A.** & **Vahid** , **F.** (2020). Multi-population mortality projection: the augmented common factor model with structural breaks. SSRN. **Wi´sniowski** , **A.** , **Smith** , **P.W.F.** , **Bijak** , **J.** , **Raymer** , **J.** & **Forster** , **J.J.** (2015). Bayesian population forecasting: extending the Lee-Carter method. _Demography_ , **52** (3), 1035–1059. **Yang** , **S.S.** & **Wang** , **C.-W.** (2013). Pricing and securitization of multi-country longevity risk with mortality dependence. _Insurance: Mathematics and Economics_ , **52** (2), 157–169. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 341 

## **Appendix A. Clustering by Mortality Trends** 

In Section 3.1, we constructed multi-population MOGPs by first generating a large set of twopopulation models and then utilising the respective correlations _rl_ 1, _l_ 2 to select the datasets that are most correlated to the target population. We also investigated a simpler alternative for deciding which populations to pool based on the similarity in their mortality trends. This approach does not require construction of any preliminary MOGPs and instead only looks at the GP mean function _m_ ( · ). Namely, we first estimate the shape of mortality for each population _l_ via a linear mean function: _ml_ ( _x_ ) = _β_ 0, _l_ + _β_ 1, _[ag] l[x][ag]_[ +] _[ β]_ 1, _[yr] l[x][ag]_[.][We][then][calculate][the][root-integrated] squared distance between _ml_ 1( · ), _ml_ 2( · ) based on the given test set _xag_ ∈{50, _. . ._ , 84} and _xyr_ ∈ {1990, ..., 2012}: 

**==> picture [384 x 31] intentionally omitted <==**

The above metric is employed within a hierarchical clustering method based on a specified dissimilarity measure. Figure A.1 displays the dendrograms extracted from hierarchical clustering of 32 populations (16 countries × {Male, Female}) via two different measures of dissimilarity: single linkage and complete linkage. We note that the resulting clusters naturally tend to separate males and females, reflecting the latter’s lower mortality. We also observe a strong geographic influence, so that neighbouring countries with similar demographics are indeed clustered together. The dendrogram could be used agglomeratively to build a MOGP. For example, using Hungary as the target population, Figure A.1 suggests first adding Estonia, then Lithuania, Latvia, etc. We find that this method is often as efficient as clustering by cross-population correlation, although going up the linkages often calls for fusing of two clusters, i.e. it is not designed for increasing _L_ 1-by-1. 

**==> picture [382 x 213] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>Germany.M Poland.M<br>Denmark.M Czechia.M<br>Austria.M Hungary.M<br>Belarus.F Estonia.M<br>UK.M Lithuania.M<br>Netherlands.M Latvia.M<br>Latvia.F Belarus.M<br>Hungary.F Germany.F<br>Spain.M Austria.F<br>France.M Netherlands.F<br>Lithuania.F Sweden.F<br>Estonia.F UK.F<br>Poland.F Switzerland.F<br>Denmark.F France.F<br>Switzerland.M Spain.F<br>Sweden.M Switzerland.M<br>Czechia.F Sweden.M<br>Germany.F Poland.F<br>Austria.F Estonia.F<br>Netherlands.F Denmark.F<br>Sweden.F Czechia.F<br>UK.F Lithuania.F<br>Switzerland.F UK.M<br>France.F Netherlands.M<br>Spain.F Germany.M<br>Hungary.M Denmark.M<br>Estonia.M Austria.M<br>Lithuania.M Latvia.F<br>Latvia.M Hungary.F<br>Belarus.M Spain.M<br>Poland.M France.M<br>Czechia.M Belarus.F<br>**----- End of picture text -----**<br>


**Figure A.1.** Dendrograms from hierarchical clustering of 32 HMD populations using the _D_ -metric in (A.1). (a) Complete linkage. (b) Single linkage. 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

342 Nhan Huynh and Mike Ludkovski 

## **Appendix B. Fitted MOGP Hyperparameters Across Full-Rank and ICM Kernels and MLE/Bayesian Methods for the DEN-FRA-SWE-GBR Case Study** 

**Cross-population correlation matrices.** In the full-rank kernel (7), the correlation coefficient is _rl_ 1, _l_ 2 := exp ( − _θl_ 1, _l_ 2). In the ICM model, the cross-covariance is _B_ = _AA[T]_ with the diagonals _Bl_ , _l_ interpreted as the process variance of _fl_ , from which we can similarly extract _rl_ 1, _l_ 2’s. Using {Denmark, France, Sweden, UK} ≡{1, 2, 3, 4} we find that 

**==> picture [253 x 82] intentionally omitted <==**

**Table B.1.** Hyperparameter estimates based on maximum likelihood (kergp) and maximum a posteriori probability (Stan), along with MCMC summary statistics using a joint mortality model across four countries: Denmark, Sweden, France and UK. Training set contains Males aged 70–84 during Years 1990–2012. Denmark used as baseline population in the mean function 

||~~Parameters~~<br>~~kergp MLE~~<br>~~Stan~~|||
|---|---|---|---|
||MAP<br>MCMC Mean<br>MCMC 95% Posterior CI|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_β_0<br>−10.4610<br>−10.0220<br>−10.5337<br>(−12.0847,−9.1274)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_βag_<br>1<br>0.0996<br>0.0958<br>0.0967<br>(0.0847, 0.1085)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_βFRA_<br>−0.0922<br>−0.0685<br>0.1239<br>(−0.2438, 0.5827)|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_βSWE_<br>−0.1076<br>−0.0592<br>−0.0060<br>(−0.3596, 0.3844)|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_βGBR_<br>0.0062<br>0.000<br>0.1122<br>(−0.2252, 0.4961)|||
||.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θag_<br>13.3849<br>12.1915<br>17.4166<br>(12.0294, 24.0641)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θyr_<br>8.8549<br>9.2694<br>11.3858<br>(8.2536, 13.3009)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θDEN_,_FRA_<br>0.1956<br>0.3773<br>0.8269<br>(0.1544, 2.9089)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θDEN_,_SWE_<br>0.1804<br>0.2725<br>0.5094<br>(0.0889, 1.8891)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θDEN_,_GBR_<br>0.0772<br>0.0799<br>0.1579<br>(0.0286, 0.5473)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θFRA_,_SWE_<br>0.1030<br>0.1943<br>0.3658<br>(0.0797, 1.0949)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θFRA_,_GBR_<br>0.1095<br>0.1445<br>0.1439<br>(0.0383, 0.3917)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_θSWE_,_GBR_<br>0.1681<br>0.1801<br>0.6132<br>(0.0530, 2.6660)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_η_2<br>0.0395<br>0.0392<br>0.0684<br>(0.0289, 0.1520)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_σ_ 2<br>_DEN_<br>1.516×10−3<br>1.514×10−3<br>1.528×10−3<br>(1.315×10−3, 1.772×10−3)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_σ_ 2<br>_FRA_<br>3.394×10−4<br>3.371×10−4<br>3.459×10−4<br>(2.956×10−4, 4.045×10−4)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_σ_ 2<br>_SWE_<br>8.022×10−4<br>8.007×10−4<br>8.226×10−4<br>(7.033×10−4, 9.640×10−4)<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..|||
||_σ_ 2<br>_GBR_<br>6.887×10−4<br>6.849×10−4<br>7.001×10−4<br>(5.985×10−4, 8.165×10−4)|||



## **Appendix C. Alternative Kernel Families** 

In this Appendix, we illustrate selecting alternative kernel families for the GP model as discussed in Section 2.6. Figure C.1(a) and (b) compares employing a Matérn-5/2 kernel instead of the squared exponential one. Namely, we replace the kernel definition with 

**==> picture [295 x 34] intentionally omitted <==**

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 343 

**==> picture [210 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>x & © 5 Age 84<br>2 ie /YY . ) Vaf ¢<br>ra Sy<br>26= =eo?.<br>ge<br>co | @ Observed values in the test set <9 @_ ~<br>—— Predictive mean via SE Kernel pe, 2<br>gs | Predictive mean via Matern-5/2 Kernel ]<br>J<br>1990 1995 2000 2005 2010 2015 2020<br>Year<br>(c) (d)<br>**----- End of picture text -----**<br>


**Figure C.1. Illustration I:** Comparing a GP model with a Matérn-5/2 covariance kernel vis-a-vis one with a squaredexponential kernel. We show mortality rates and improvement rates for Danish Males. Both models are fitted via the ICM approach and use four populations from Denmark, France, Sweden and UK; Males, Ages 70–84 and Years 1990–2016. **Illustration II:** Heatmap of the predicted mortality improvement rates using a squared exponential kernel without and with a Birth–Cohort term (17) for UK Males. The single-population model is fitted on Ages 50–84 and Years 1990–2016. Effect of alternative covariance kernel specifications on the GP model output. (a) Mortality rates for Danish Males. (b) YoY improvement rates for Danish Males. (c) Base case (no Cohort). (d) With Birth-Cohort. 

The results are illustrated via the smoothed mortality rates and the respective improvement rates for Danish Males. We observe that the Matérn-5/2-based fit hews closer to the historical data which leads to more “rough” mortality improvement factors. Otherwise, the differences are mild. 

Table C.2 illustrates the impact of implementing a composite kernel, namely the sum of a linear kernel and a SE kernel in (16), see section 2.6. We again consider Male mortality in Denmark within a single-population setup. The selected composite kernel is functionally equivalent to an SE kernel with a linear trend function (Duvenaud, 2014), although the obtained results differ slightly since the optimised marginal likelihood functions are not algebraically the same. We do observe essentially the same results (they are visually identical which is the reason for not including a plot). Note that in Table C.2 the hyperparameters associated with the linear kernel, _α_ 0[2][and] _α_[2] _ag_[, can be thought as the priors of the intercept and the slope in Age, respectively. In contrast,] with a parametric mean function, _β_ 0 is interpreted as the intercept and _β_ 1 as the linear trend in Age. 

Section 2.6 also briefly discussed the potential to incorporate Year-of-Birth term into the covariance structure to capture cohort effects, cf. (17). Cohort effects manifest themselves in diagonal features on an Age–Year heatmap, see Figure C.1(c)–(d) where we illustrate with data for UK Males Ages 50–84 and Years 1990–2016. In the figure, we display model-predicted mortality improvement rates covering the in-sample cells, as well as forecasting out to year 2025. The bottom left panel (c) uses the base SE kernel without a Birth–Year term; one can clearly see several 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

Nhan Huynh and Mike Ludkovski 

344 

**Table C.1.** MOGP with rank _Q_ = 3 ICM kernel for Males in Denmark, France, Sweden and UK. The training dataset contains Ages 70–84 and Years 1990–2012 

||~~Mean function~~<br>~~Length-scales~~<br>~~Cross-covariance~~<br>~~_a_~~_l_,1<br>~~_a_~~_l_,2<br>~~_a_~~_l_,3<br>_β_0<br>_βag_<br>_βFRA_<br>_θag_<br>DEN:_l_=1<br>0.0435<br>0.1687<br>0.1068<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>~~−11.4073~~<br>~~0.1120~~<br>~~0.0410~~<br>~~15.4199~~<br>~~FRA:~~~~_l_ = 2~~<br>~~0.2199~~<br>~~0.1619~~<br>~~0.0491~~<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>−<br>_βSWE_<br>_βGBR_<br>_θyr_<br>SWE:_l_=3<br>0.1552<br>0.0562<br>0.1683<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>−<br>−0.0348<br>0.0520<br>13.4019<br>GBR:_l_=4<br>0.1451<br>0.1636<br>0.1640|
|---|---|



**Table C.2.** Comparison between the hyperparameters from fitting a fused kernel vis-a-vis a composite Linear+SE kernel (16) for a SOGP model for Danish Males, Ages 70–84 and Years 1990–2016 

||~~Hyperparameter~~<br>~~SE kernel~~<br>~~Linear + SE kernel~~<br>Mean function<br>_β_0<br>−10.1560<br>0<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_βag_<br>0.0951<br>–<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>Covariance function<br>_α_2<br>0<br>–<br>36.6177<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>~~_α_~~2<br>_ag_<br>~~–~~<br>~~0.0082~~<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_θag_<br>12.5430<br>12.1455<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_θyr_<br>15.1672<br>18.2727<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_η_2<br>0.0598<br>0.0862<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_σ_ 2<br>1.589e−03<br>1.592e−03|
|---|---|



**Table C.3.** GP hyperparameters for fitting a covariance kernel with Birth– Cohort term (17) for a SOGP model for UK Males, Ages 50–84 and Years 1990–2016 

||Base case SOGP<br>SOGP with<br>Hyperparameter<br>without cohort<br>Birth-Cohort term<br>Mean function<br>_β_0<br>−10.3695<br>−10.1886<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_βag_<br>0.0976<br>0.0961<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>Covariance function<br>_θ_~~_ag_~~<br>6.5553<br>58.1212<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_θyr_<br>5.5229<br>11.5091<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_θbc_<br>–<br>6.5911<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_η_2<br>0.0239<br>0.0324<br>.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ..<br>_σ_ 2<br>5.421e−04<br>5.260e−04|
|---|---|



diagonal patterns for birth cohorts circa 1930, c. 1957 (both of which enjoyed larger than average MI) and c. 1965 (which is experiencing negative MI). 

To explicitly capture these features, in the bottom-right panel (d) we construct the same heatmap but now with covariance kernel _C_ ( _x_ , _x_ ’) of the form (17). While the in-sample patterns remain the same (as they should, being primarily data-driven), we can spot differences in terms of out-of-sample forecasts. The Cohort-GP model makes the historical cohort trends persist into the future; for example it makes the longevity of the post-1945 cohort to continue to be materially worse than the World War II generation (extreme top-right corner), while the no-Cohort model expects longevity deterioration in the 2020s across all cohorts. 

Adding a Birth-year term to _C_ ( _x_ , _x_ ’) changes all the GP hyperparameters, especially the lengthscales, cf. Table C.3. Since (17) has a product of three terms rather than two as before, to maintain a similar correlation between a given _x_ , _x_ ’, each length-scale is attenuated. Thus, _θyr_ more than 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

_Annals of Actuarial Science_ 345 

doubles from ≈ 5.5 to ≈ 11.5, while _θag_ increases even more dramatically from ≈ 6.5 to ≈ 58 when a Birth-Cohort term is included. The estimated Birth–Cohort length-scale, _θbc_ ≈ 6.6, indicates that the typical “generation” spans about 7 birth–years, e.g. 1939–1945, 1965–1972. As expected, the change should have minimal impact on the GP mean function or the variance parameters _η_[2] , _σ_[2] . 

**Cite this article:** Huynh N and Ludkovski M (2021). Multi-output Gaussian processes for multi-population longevity modelling. _Annals of Actuarial Science_ **15** , 318–345. https://doi.org/10.1017/S1748499521000142 

https://doi.org/10.1017/S1748499521000142 Published online by Cambridge University Press 

