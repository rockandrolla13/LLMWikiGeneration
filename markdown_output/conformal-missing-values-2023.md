# Conformal Prediction with Missing Values 

Margaux Zaffran[*][,1,2,3] , Aymeric Dieuleveut[3] , Julie Josse[2] , and Yaniv Romano[4] 

1Electricit´e De France R&D, Palaiseau, France 

2PreMeDICaL project team, INRIA Sophia-Antipolis, Montpellier, France 

> 3CMAP, CNRS, ´Ecole polytechnique, Institut Polytechnique de Paris, Palaiseau, France 

4Departments of Electrical Engineering and of Computer Science, Technion - Israel Institute of Technology, Haifa, Israel 

## **Abstract** 

Conformal prediction is a theoretically grounded framework for constructing predictive intervals. We study conformal prediction with missing values in the covariates – a setting that brings new challenges to uncertainty quantification. We first show that the marginal coverage guarantee of conformal prediction holds on imputed data for any missingness distribution and almost all imputation functions. However, we emphasize that the average coverage varies depending on the pattern of missing values: conformal methods tend to construct prediction intervals that under-cover the response conditionally to some missing patterns. This motivates our novel generalized conformalized quantile regression framework, missing data augmentation, which yields prediction intervals that are valid conditionally to the patterns of missing values, despite their exponential number. We then show that a universally consistent quantile regression algorithm trained on the imputed data is Bayes optimal for the pinball risk, thus achieving valid coverage conditionally to any given data point. Moreover, we examine the case of a linear model, which demonstrates the importance of our proposal in overcoming the heteroskedasticity induced by missing values. Using synthetic and data from critical care, we corroborate our theory and report improved performance of our methods. 

## **1 Introduction** 

By leveraging increasingly large data sets, statistical algorithms and machine learning methods can be used to support high-stakes decision-making problems such as autonomous driving, medical or civic applications, and more. To ensure the safe deployment of predictive models it is crucial to quantify the uncertainty of the resulting predictions, communicating the limits of predictive performance. Uncertainty 

> *Corresponding author: margaux.zaffran@inria.fr 

quantification attracts a lot of attention in recent years, particularly methods that are based on Conformal Prediction (CP) (Vovk et al., 2005; Papadopoulos et al., 2002; Lei et al., 2018). CP provides controlled predictive regions for any underlying predictive algorithm (e.g., neural networks and random forests), in finite samples with no assumption on the data distribution except for the exchangeability of the train and test data. More precisely, for a _miscoverage rate α_ � _∈_ [0 _,_ 1], CP outputs a _marginally valid_ prediction interval _Cα_ for the test response _Y_ given its corresponding covariates _X_ , that is: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0001-13.png)


Split CP (Papadopoulos et al., 2002; Lei et al., 2018) achieves Eq. (1) by keeping a hold-out set, the _calibration set_ , used to evaluate the performance of a fixed predictive model. 

At the same time, as the volume of data increases, the volume of missing values also increases. There is a vast literature on this topic (Little, 2019; Josse and Reiter, 2018), and a recent survey even identified more than 150 different implementations (Mayer et al., 2019). Missing values create additional challenges to the task of supervised learning, as traditional machine learning algorithms can not handle incomplete data (Josse et al., 2019; Le Morvan et al., 2020b,a, 2021; Ayme et al., 2022; Van Ness et al., 2022). One of the most popular strategies to deal with missing values suggests imputing the missing entries with plausible values to get completed data, on which any analysis can be performed. The drawback of this “impute-then-predict” approach is that single imputation can distort the joint and marginal distribution of the data. Yet, Josse et al. (2019); Le Morvan et al. (2020b, 2021) showed that such impute-then-predict strategies are Bayes consistent, under the assumption that a universally consistent learner is applied on an imputed data set. However, this line of work focuses on point prediction with missing values that aim to predict the most likely outcome. In contrast, our goal is quantifying predictive uncertainty, which was not explored with missing values although its enormous importance. 

1 

## **Contributions.** 

We study CP with missing covariates. Specifically, we study downstream quantile regression (QR) based CP, like CQR (Romano et al., 2019), on impute-then-predict strategies. Still, the proposed approaches also encapsulate other regression basemodels, and even classification. 

After setting background in Section 2, our first contribution is showing that CP on impute-then-predict is _marginally_ valid regardless of the model, missingness distribution, and imputation function (Section 3). 

Then, we focus on the specificity of uncertainty quantification _with missing values_ . In Section 4, we describe how different masks (i.e. the set of observed features) introduce additional heteroskedasticity: _the uncertainty on the output strongly depends on the set of predictive features observed_ . We therefore focus on achieving valid coverage _conditionally on the mask_ , coined MCV – Mask-Conditional-Validity. MCV is desirable in practice, as occurrence of missing values are linked to important attributes (see Section 5). 

Traditional approaches such as QR and CQR fail to achieve MCV because they do not account for this core connection between missing values and uncertainty. This is illustrated on synthetic data in Figure 1. In Figure 1a, a toy example with only 3 features, thus 2[3] _−_ 1 = 7 possible masks, shows how the coverage of QR and CQR varies depending on the mask. Both methods dramatically undercover when the most important variable ( _X_ 2) is missing, and the loss of coverage worsens when additional features are missing. In particular, for each method, one mask ( _X_ 1 and _X_ 2 missing, highlighted in red) leads to the _lowest mask coverage_ . Achieving MCV corresponds to a lowest mask coverage greater than 1 _−α_ . In Figure 1b, the dimension is 10: instead of the 2[10] _−_ 1 = 1023 different masks, we only report the lowest mask coverage for increasing sample sizes. It highlights that QR (green _×_ ) 

and CQR (orange _×_ ) do not meet the lowest mask coverage target of 90%, even for large sample sizes. 

This motivates our second contribution: we show in Section 5 how to form prediction intervals that are MCV. This is highly challenging since there are exponentially many possible patterns to consider. Therefore, the naive solution to perform a calibration for each mask would fail as in finite samples, we often observe test samples with a mask that have low (or even null) frequency of appearance in the calibration set. To tackle this issue, we suggest two conformal methods that share the same core idea of missing data augmentation (MDA): the calibration data is artificially masked to match the mask of the point we consider at test time. The first method, _CP-MDA with exact masking_ , relies on building an ideal calibration set for which the data points have the exact same mask as of the test point. We show its MCV under exchangeability and Missing Completely At Random assumptions. Our second method, _CP-MDA with nested masking_ , does not require such an ideal calibration set. Instead, we artificially construct a calibration set in which the data points have _at least_ the same mask as the test point, i.e., this artificial masking results in calibration points having possibly more missing values than the test point. We show the latter method also achieves the desired coverage conditional on the mask, but at the cost of an additional assumption for validity: stochastic domination of the quantiles. Figure 1 illustrates those findings: both methods are MCV, as their lowest mask coverage is above 1 _− α_ . 

Our third contribution further supports our design choice to use QR. We show that QR on impute-then-predict strategy is Bayes-consistent – it can achieve the strongest form of coverage conditional on the observed test features (Section 6). 

Lastly, we support our proposal using both (semi)-synthetic experiments and real medical data (Section 7). The code to reproduce our experiments is available on GitHub. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0002-09.png)


**----- Start of picture text -----**<br>
QR (no guarantee) CQR (marginal validity)<br>1 . 0<br>1  − ↵<br>0 . 8 Lowest Lowestmask<br>0 . 6 ✗ MCV: ✗ maskcov. ✓ MCV: ✗ cov. 1  − 0 .α 8 QR (no guarantee)<br>CQR-MDA with exact masking CQR-MDA with nested masking CQR<br>(mask-conditional-validity - MCV) (mask-conditional-validity - MCV) (marginal validity)<br>1  − 1 .↵ 0 Lowestmaskcov. Lowestmaskcov. 0 . 6 CQR-MDA (mask-conditional-validity with exact - masking MCV)<br>0 . 8 CQR-MDA with nested masking<br>0 . 4 (mask-conditional-validity - MCV)<br>0 . 6 ✓ MCV: ✓ ✓ MCV: ✓ Target coverage, i.e. 1  − α<br>0 . 2<br>Training size<br>X Marginalfullyobserved X ( X 11missing , X 2)missing X ( X 22missing , X 3)missing X ( X 31missing , X 3)missing X Marginalfullyobserved X ( X 11missing , X 2)missing X ( X 22missing , X 3)missing X ( X 31missing , X 3)missing<br>50 100 500 1000 2500 5000 20000<br>coverage<br>Average<br>coverage<br>mask<br>coverage<br>Lowest<br>Average<br>**----- End of picture text -----**<br>


(a) Coverage of the predictive intervals depending on which features are missing, among the 3 features. Evaluation over 200 runs. 

(b) Lowest mask coverage as a function of the training size. Results evaluated over 100 repetitions, and the (tiny) error bars correspond to standard errors. 

Figure 1: Methods are Quantile Regression (QR), Conformalized Quantile Regression (CQR), and two novel procedures **CP-MDA-Exact** and **CP-MDA-Nested** , on top of CQR. Settings are given in Section 7, in a nutshell: data follows a Gaussian linear model where missing values are independent of everything else and of proportion 20%; the dimension of the problem is 3 in Figure 1a while in 1b it is 10. 

2 

## **2 Background** 

**Background on missing values.** Consider a data set with _n_ exchangeable realizations of the random variable ( _X, M, Y_ ) _∈_ R _[d] ×{_ 0 _,_ 1 _}[d] ×_ R: �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[,] where _X_ represents the features, _M_ the missing pattern, or mask, and _Y_ an outcome to predict. For _j ∈_ �1 _, d_ �, _Mj_ = 0 when _Xj_ is observed and _Mj_ = 1 when _Xj_ is missing, i.e. NA (Not Available). We note _M_ = _{_ 0 _,_ 1 _}[d]_ the set of masks. For a pattern _m ∈M, X_ obs( _m_ ) is the random vector of observed components, and _X_ mis( _m_ ) is the random vector of unobserved ones. For example, if we observe (NA _,_ 6 _,_ 2) then _m_ = (1 _,_ 0 _,_ 0) and _X_ obs( _m_ ) = (6 _,_ 2). Our goal is to predict a new outcome _Y_[(] _[n]_[+1)] given _X_ obs[(] _[n]_[+1)] ( _M_[(] _[n]_[+1)] )[and] _[ M]_[ (] _[n]_[+1)][.] 

**Assumption A1** (exchangeability) **.** The random variables � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1][are exchangeable.] 

Following Rubin (1976), we consider three well-known missingness mechanisms. 

**Definition 2.1** (Missing Completely At Random (MCAR)) **.** For any _m ∈M_ , P ( _M_ = _m|X_ ) = P ( _M_ = _m_ ). 

**Definition 2.2** (Missing At Random (MAR)) **.** For any _m ∈ M_ , P ( _M_ = _m|X_ ) = P � _M_ = _m|X_ obs( _m_ )�. 

**Definition 2.3** (Missing Non At Random (MNAR)) **.** If the missing data is not MAR, it is MNAR. Thus, its probability distribution depends on _X_ , including the missing values. 

**Background on (split) conformal prediction.** Split, or inductive, CP (SCP) (Papadopoulos et al., 2002; Lei et al., 2018) builds predictive regions by first splitting the _n_ points of the training set into two disjoint sets Tr _,_ Cal _⊂_ �1 _,_ n�, to create a _proper training set_ , Tr, and a _calibration set_ , Cal. On the proper training set, a model _f_[ˆ] (chosen by the user) is fitted, and then used to predict on the calibration set. _Conformity scores S_ Cal = _{_ ( _s_ ( _X_[(] _[k]_[)] _, Y_[(] _[k]_[)] )) _k∈_ Cal _}_ are computed to assess how well the fitted model _f_[ˆ] predicts the response values of the calibration points. For example, Conformalized Quantile Regression (CQR, Romano et al., 2019) fits two quantile regressions _q_ ˆlow and _q_ ˆupp, on the proper training set. The conformity scores are defined ˆ by _s_ ( _x, y_ ) = max(ˆ _q_ low( _x_ ) _− y, y − q_ upp( _x_ )). Finally, a cor˜ rected (1 _− α_ )-th quantile of these scores _Q_[�] 1 _−α_ ˜( _S_ Cal) is computed (called _correction term_ ) to define the predictive region: _C_[�] _α_ ( _x_ ) := _{y_ such that _s_ ( _y, f_[ˆ] ( _x_ )) _≤ Q_[�] 1 _−α_ ˜( _S_ Cal) _}_ .[1] An illustration of CQR is provided in Appendix B. 

This procedure satisfies Eq. (1) for any _f_[ˆ] , any (finite) sample size _n_ , as long as the data points are exchangeable.[2] Moreover, if the scores are almost surely distinct, the coverage holds almost exactly: P( _Y ∈ C_[�] _α_ ( _X_ )) _≤_ 1 _− α_ + #Cal+11[.] For more details on SCP, we refer to Angelopoulos and Bates (2023); Vovk et al. (2005), as well as to Manokhin (2022). 

## **3 Warm-up: marginal coverage with NAs** 

**Impute-then-predict.** As most predictive algorithms can not directly handle missing values, we impute the incomplete data using an imputation function Φ which maps observed values to themselves and missing values to a function of the observed values. With notations from Le Morvan et al. (2021) we note _ϕ[m]_ : R _[|]_[obs(m)] _[|] →_ R _[|]_[mis(] _[m]_[)] _[|]_ the imputation function which takes as input observed values and outputs imputed values, i.e. plausible values, given a mask _m ∈M_ . Then, the imputation function Φ belongs to _F[I]_ := _{_ Φ : R _[d] × M →_ R _[d]_ : _∀j ∈_ �1 _, d_ � _,_ 

Φ _j_ ( _X, M_ ) = _Xj_ 1 _Mj_ =0 + _ϕ[M] j_ � _X_ obs( _M_ )� 1 _Mj_ =1� _._ Additionally, _F∞[I]_[is the restriction of] _[ F][I]_[to] _[ C][∞]_[functions] which include deterministic imputation, such as mean imputation or imputation by regression. The imputed data set is formed by the realizations of the _n_ random variables (Φ ( _X, M_ ) _, M, Y_ ). In practice, Φ is obtained as the result of an algorithm _I_ trained on �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)][��] _[n] k_ =1[+1][.] 

**Assumption A2** (Symmetrical imputation) **.** The imputation function Φ is the output of an algorithm _I_ treating its input ( _d_ ) data points symmetrically: _I_ (( _X_[(] _[σ]_[(] _[k]_[))] _, M_[(] _[σ]_[(] _[k]_[))] ) _[n] k_ =1[+1][)] = _I_ (( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] ) _[n] k_ =1[+1][)] _[conditionally][on]_[(] _[X]_[(] _[k]_[)] _[, M]_[ (] _[k]_[)][)] _[n] k_ =1[+1] and for any permutation _σ_ on �1 _, n_ + 1�. 

Assumption A2 is very mild and satisfied by all existing imputation methods for exchangeable data. In particular, it is valid for iterative regression imputation which allows out-of-sample imputation. 

> A first idea to get valid predictive intervals _C_[�] _α_ ( _X, M_ ) in the presence of missing values _M_ is to apply CP in combination with impute-then-predict, which we refer to as _impute-thenpredict+conformalization_ . More details on this approach are given in Appendix C.1 for both classification and regression tasks, although our main focus is regression. It turns out that such a simple approach is marginally (exactly) valid. 

**Definition 3.1** (Marginal validity) **.** A method outputting intervals _C_[�] _α_ is marginally valid if the following lower bound is satisfied, and exactly valid if the following upper bound is also satisfied: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0003-16.png)


Indeed, symmetric imputation preserves exchangeability. 

**Lemma 3.2** (Imputation preserves exchangeability) **.** _Let A1 hold. Then, for any missing mechanism, for any imputation function_ Φ _satisfying A2, the imputed random variables_ �Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _[n] k_ =1[+1] _[are exchangeable.]_ 

Note that if we replace A1 by an i.i.d. assumption, the 

> 1The correction _α → α_ ˜ is needed because of the inflation of quantiles in finite sample (see Lemma 2 in Romano et al. (2019) or Section 2 in Lei et al. (2018)). 

> 2Only the calibration and test data points need to be exchangeable. 

3 

imputed data set is only exchangeable but not i.i.d. without further assumptions on _I_ . Indeed, even simple mean imputation breaks independence. 

**Proposition 3.3** ((Exact) validity of impute-then-predict+conformalization) **.** _If A1 and A2 are satisfied, imputethen-predict+conformalization is marginally valid. If moreover the scores are almost surely distinct, it is exactly valid._ 

This is an important first positive result (proved in Appendix C.2) showing that CP applied on an imputed data set has the same validity properties as on complete data, regardless of the missing value mechanism (MCAR, MAR or MNAR) and of the symmetric imputation scheme. Note that similar propositions could be derived for full CP (Vovk et al., 2005) and Jackknife+ (Barber et al., 2021b). 

Proposition 3.3 complements the work by Yang (2015), that also guarantees _marginal_ coverage for full CP, with the striking difference of having a complete training data. 

## **4 Challenge: NAs induce heteroskedasticity** 

To better understand the interplay between missing values and conditional coverage with respect to the mask, we consider an illustrative example of a Gaussian linear model. 

**Model 4.1** (Gaussian linear model) **.** The data is generated according to a linear model and the covariates are Gaussian conditionally to the pattern: 

- _Y_ = _β[T] X_ + _ε_ , _ε ∼N_ (0 _, σε_[2][)] _[ ⊥⊥]_[(] _[X, M]_[)][,] _[ β][∈]_[R] _[d]_[.] 

- for all _m ∈M_ , there exist _µ[m]_ and Σ _[m]_ such that _X|_ ( _M_ = _m_ ) _∼N_ ( _µ[m] ,_ Σ _[m]_ ) _._ 

In particular, Model 4.1 is verified when _X_ is Gaussian and the missing data is MCAR. Model 4.1 is more general: it even includes MNAR examples (Ayme et al., 2022). 

**Proposition 4.2** (Oracle intervals) **.** _The oracle predictive interval is defined as the smallest valid interval knowing X_ obs(M) _and M . Under Model 4.1, its length only depends on the mask. For any m ∈M this oracle length is:_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0004-11.png)


_See Appendix D for the definition of µ[m]_ mis _|_ obs _[and]_[ Σ] _[m]_ mis _|_ obs _and the quantiles of Y |_ ( _X_ obs(m) _, M_ = _m_ ) _._ 

Eq. (2) stresses that even when the noise of the generative model is homoskedastic, _missing values induce heteroskedasticity_ . Indeed, the covariance of the conditional distribution of _Y |_ ( _X_ obs(m) _, M_ = _m_ ) depends on _m_ . Furthermore, the uncertainty increases when missing values are associated with larger regression coefficients (i.e. the most predictive variables): if _β_ mis( _m_ ) is large, then _L[∗] α_[(] _[m]_[)] is also large, as Σ _[m]_ mis _|_ obs[is][positive.][In][the][extreme][case] where all the variables are missing, i.e. _m_ = (1 _, · · · ,_ 1), _L[∗] α_[(] _[m]_[) = 2] _[q]_ 1 _[N] −_[(0] _[α]_ 2 _[,]_[1)] � _β_ Σ _[m] β[T]_ + _σε_[2] = _q_ 1 _[Y] −[α]_ 2 _[−][q][Y][α]_ 2[.][On the] contrary, if _m_ = (0 _, · · · ,_ 0) (that is all _Xj_ are observed), 

_β_ mis( _m_ ) is empty and _L[∗] α_[(] _[m]_[) = 2] _[q]_ 1 _[N] −_[(0] _[α]_ 2 _[,]_[1)] _σε_ = _q_ 1 _[ε] −[α]_ 2 _[−][q][ε][α]_ 2[.] We illustrate this induced heteroskedasticity and the impact of the predictive power in Figure 1a, and in Appendix D along with a discussion emphasizing that even with the Bayes predictor for the conditional mean, mean-based CP does not yield intervals that are MCV. 

The above analysis motivates the following two design choices we make in this work. First, we advocate working with QR models rather than classic regression ones, as the former can handle heteroskedastic data. Second, we recommend providing the mask information to the model in addition to the input covariates, as the mask may further encourage the model to construct an interval with a length adaptive to the given mask. Therefore, we focus on CQR (Romano et al., 2019)[3] , an adaptive version of SCP, and concatenate the mask to the features. However, the predictive intervals of this procedure may not necessarily provide valid coverage conditionally on the masks, especially in finite samples as shown in Figure 1b (orange crosses). This is because the quality of the prediction at some ( _X, M_ ) depends strongly on _M_ , as there is an exponential number of patterns (2 _[d]_ ) for a finite training size, whereas the correction term is calculated independently of the masks. 

## **5 Achieving mask-conditional-validity (MCV)** 

We now aim at achieving _mask-conditional-validity_ (MCV) defined as follows using an ordering on the masks. 

**Definition 5.1** (Included masks) **.** Let (˚ _m, m_ ˘ ) _∈M_[2] , _m_ ˚ _⊂ m_ ˘ if for any _j ∈_ �1 _, d_ � such that _m_ ˚ _j_ = 1 then _m_ ˘ _j_ = 1, i.e. _m_ ˘ includes at least the same missing values than _m_ ˚. 

**Definition 5.2** (MCV) **.** A method is MCV if for any _m ∈M_ the followinglower bound is satisfied, and exactly MCV if for any _m ∈M_ the followingupper bound is also satisfied: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0004-20.png)



![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0004-21.png)


**On the relevance of MCV.** In a medical application context, it is very common to have missing data completely at random (MCAR) when a measurement device fails or the medical team forgot to fill out some forms. As a general rule, from an _equity standpoint_ , a patient whose data is missing should not be penalized (because of “bad luck”) by being assigned a prediction interval that is less likely to include the true response than if the data were complete. 

Furthermore, the mask can also be linked to an external unobserved feature corresponding to a meaningful category. 

3Note that our proposed framework is not based on CQR, this is only one instance of it. 

4 

Consider the problem of predicting a disease among a population. Aggregating data from multiple hospitals with different practices and measurement devices can imply different features are observed for each patient. This can be viewed as a MCAR setting when _identically distributed_ patients[4] are assigned an hospital at random. Patterns are then linked to the cities, that themselves are related to socio-economical data. 

Overall, the missing patterns form _meaningful categories_ and _ensuring MCV yields more equitable treatment_ . Therefore, a method achieving marginal coverage by systematically failing on a given pattern, even in a MCAR setting, is not suitable. Finally, in non-MCAR cases, the pattern may be exactly related to critical discriminating features. 

## **5.1 Missing Data Augmentation (MDA)** 

To obtain a MCV procedure, we suggest modifying the calibration set according to the mask of the test point, while the training step is unchanged. More precisely, the mask of the test point is applied to the calibration set, as illustrated in Figure 2. The rationale is to mimic the missing pattern of the test point by artificially augmenting the calibration set with that mask. It ensures that the correction term is computed using data with (at least) the same missing values as the test point. We refer to this strategy as _CP with Missing Data Augmentation_ (CP-MDA), and derive two versions of it. Algorithms 1 and 2 are written using CQR as the base conformal procedure, but they work with any conformal method as we describe in Appendix E.1. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0005-04.png)


**----- Start of picture text -----**<br>
CP-MDA with exact masking:<br>calibration set<br>-1 1<br>Test point<br>4 2<br>3 1<br>Initial calibration set 0 1<br>-1 -10 6 1 CP-MDA with nested masking:<br>4 -2 2 calibration set temporary test points<br>-1 1 3 1<br>5 1 1<br>4 2 3 1<br>0 1 and<br>5 3<br>0 1 3 1<br>**----- End of picture text -----**<br>


Figure 2: CP-MDA illustration. Augmented calibration set according to one test point. For CP-MDA-Nested, the augmented masks of the calibration set are also applied temporarily to the test point. 

> 4say, for example young children whose input/output distribution is _not_ dependent on the neighborhood. 

## **Algorithm 1** CP-MDA-Exact (with CQR) 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0005-08.png)



![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0005-09.png)


**Algorithm 1 – CP-MDA-Exact.** CP-MDA with _exact masking_ consists of keeping the _artificially_ masked calibration points (l. 7) that have exactly the same missing pattern as the test point (l. 5). Then Algorithm 1 performs as imputethen-predict+conformalization: impute the calibration set (l. 10), predict on it and get the calibration scores (l. 11), compute their quantile to obtain the correction term (l. 14), and finally impute and predict the test point with the fixed fitted model by adding and subtracting the correction term (l. 15) to the initial conditional quantile estimates. Note that Algorithm 1 is described for one test point for simplicity but extends easily to many test points. The computations are then shared: the training part (l. 1-4) is common to any test point and the correction term (l. 5-14) can be reused for any new test point with the same mask. 

In high dimensions, many calibration points may be discarded when applying CP-MDA-Exact since it is likely that their missing patterns would not be included in the one of the test point.[5] This limitation brings us to the second algorithm we propose, CP-MDA-Nested. 

> 5Yet, these discarded points could be used for training but this comes at the cost of fitting a different model for each pattern; such a path is reasonable if the data is scarce. 

5 

## **Algorithm 2** CP-MDA-Nested (with CQR) 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0006-01.png)


**Algorithm 2 – CP-MDA-Nested.** CP-MDA with _nested masking_ avoids the removal of calibration points whose masks are not included in that of the test point. Instead, we apply the mask of the test point to the calibration points, and so we keep all the observations (l. 3). Next, we impute the masked calibration points (l. 6) before computing their scores _s_[(] _[k]_[)] (l. 7). Then, for each calibration point, the fitted quantile regressors are used to predict on the test point with a temporary mask, which matches the mask of the given augmented calibration point. These predictions are corrected with the score of the calibration point (l. 8-9) and stored in two bags _Z[α]_ 2[for][the][lower][interval][boundary,][and] _[Z]_[1] _[−][α]_ 2 for the upper interval boundary (l. 11-12). The prediction is finally obtained by taking the _α_ quantiles of the bags _Z_ (l. 13-15). 

The rationale for predicting on temporary test points with the mask of a given augmented calibration point is that we want to treat the test and calibration points in the same way.[6] We should note that this method may tend to achieve conservative coverage, since the augmented calibration set may have masks that overly include the missing pattern of the test point, i.e., the augmented points may have more missing values than the test point. 

## **5.2 Theoretical guarantees in finite sample** 

Let us consider the following assumptions. 

**Assumption A3** ( _Y_ is not explained by _M_ ) **.** ( _Y ⊥⊥ M_ ) _|X_ . 

**Assumption A4** (Stochastic domination of the quantiles) **.** Let (˚ _m, m_ ˘ ) _∈M_[2] . If _m_ ˚ _⊂ m_ ˘ then for any _δ ∈_ [0 _,_ 0 _._ 5]: 

> 6This motivation is similar to the one of Jackknife+ (Barber et al., 2021b) and out-of-bags methods (Gupta et al., 2022). 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0006-09.png)


A4 grasps the underlying intuition that the conditional distribution of _Y |_ ( _X_ obs(m) _, M_ = _m_ ) tends to have larger deviations when the number of observed variables is smaller, in concordance with the intuition that observing predictive variables reduce the conditional randomness of _Y |X_ obs. 

The following theorems (proved in Appendix E) state the finite sample guarantees of CP-MDA. 

**Theorem 5.3** (MCV of CP-MDA) **.** _Assume the missing mechanism is MCAR, and A1 to A3. Then:_ 

_1. CP-MDA-Exact is MCV;_ 

_2. if the scores are almost surely distinct, CP-MDA-Exact is exactly MCV;_ 

_3. if A4 also holds, CP-MDA-Nested is MCV, up to a technical minor modification of the output._ 

The challenge in proving MCV of CP-MDA-Nested is that the augmented calibration and test points are not exchangeable conditional on the mask and thus may result in undercoverage. However, by imposing A4 we prove that this violation of exchangeability still leads to MCV (and often conservative MCV) (see Lemma E.3). We conjecture that CP-MDA-Nested attains MCV (without any modification), as also supported by experiments. However, we could not prove it without making an independence assumption which we prefer to avoid as exchangeability is key to imputation methods. Instead, we prove in Theorem E.4 the MCV of any variant outputting [ _Q_[�] _α_ ˜( _Z[m] α_ 2[˜][);] _[Q]_[�][1] _[−][α]_[˜][(] _[Z]_ 1 _[m]_[˜] _−[α]_ 2[)]][ for] _[ Z][m] α_ 2[˜][the] subset of _Z[α][m]_[˜][ at l.][ 6][-][9][.] 2[composed with points using mask] 

**Theorem 5.4** (Marginal validity of CP-MDA) **.** _Under then same assumptions as Theorem 5.3 (i) CP-MDA-Exact is marginally valid; (ii) if A4 also holds, CP-MDA-Nested is marginally valid (with the same caveats as in Theorem 5.3)._ 

## **6 Towards asymptotic individualized coverage** 

Achieving validity conditionally on the mask is an important step towards conditional coverage: in practice one aims at the strongest coverage conditional on _both X_ and _M_ . Lei and Wasserman (2014); Vovk (2012); Barber et al. (2021a) studied a related question (without considering missing patterns) and concluded that it is impossible to achieve _informative_ intervals satisfying conditional coverage, P( _Y ∈ C_[�] _α_ ( _x_ ) _|X_ = _x_ ) _≥_ 1 _− α_ for any _x ∈X_ in the distribution-free and finite samples setting. Still, we can analyze the asymptotic regime, similarly to Theorem 1 of Sesia and Candes` (2020), which proves the asymptotic conditional validity of CQR (without the presence of missing values) under consistency assumptions on the underlying quantile regressor. Here, by contrast, we study the asymptotic conditional validity of the impute-then-predict+conformalization 

6 

procedure, by analyzing the consistency of impute-thenregress in Quantile Regression (QR). That is, we aim at showing that we satisfy the required assumption of consistency to invoke Theorem 1 of Sesia and Candes` (2020). The proofs of this section are given in Appendix F. 

To analyze the consistency of impute-then-predict procedures for QR, we extend the work of Le Morvan et al. (2021) on mean regression. QR with missing values, for a quantile level _β_ , aims at solving 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0007-02.png)


ˆ with _ℓβ_ the pinball loss _ℓβ_ ( _y,_ ˆ _y_ ) = _ρβ_ ( _y − y_ ) and _ρβ_ ( _u_ ) = _β|u|_ 1 _{u≥_ 0 _}_ + (1 _− β_ ) _|u|_ 1 _{u≤_ 0 _}_ . 

An associated _ℓβ_ -Bayes predictor minimizes Eq. (3). Its risk is called the _ℓβ_ -Bayes risk, noted _R[∗] ℓβ_[.][Impute-then-predict] procedure in QR aims at solving 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0007-05.png)


for Φ any imputation. Let _gℓ[∗] β ,_ Φ _[∈]_[arg min] _g Rℓβ ,_ Φ( _g_ ). The following proposition states that _Rℓβ ,_ Φ( _gℓ[∗] β ,_ Φ[) =] _[ R][∗] ℓβ_ and the consistency of a universal learner. **Proposition 6.1** ( _ℓβ_ -consistency of an universal learner) **.** _Let β ∈_ [0 _,_ 1] _. If X admits a density on_ R _[d] , then, for almost all imputation function_ Φ _∈F∞[I][, (i)][ g] ℓ[∗] β ,_ Φ _[◦]_[Φ] _[ is][ ℓ][β][-Bayes-] optimal (ii) any universally consistent algorithm for QR trained on the data imputed by_ Φ _is ℓβ-Bayes-consistent (i.e., asymptotically in the training set size)._ 

Note that this QR case does not require E � _ε|X_ obs(M) _, M_ � = 0, contrary to the quadratic loss case (Le Morvan et al., 2021). 

We conclude our asymptotic analysis of conditional coverage with Corollary 6.2. 

**Corollary 6.2.** _For any missing mechanism, for almost all imputation function_ Φ _∈F∞[I][, if][ F] Y |_ ( _X_ obs(M) _,M_ ) _[is continu-] ous, a universally consistent quantile regressor trained on the imputed data set yields asymptotic conditional coverage._ 

In words, the intervals obtained by taking Bayes predictors of levels _α/_ 2 and 1 _− α/_ 2 are exactly valid conditionally to both the mask _M_ and the observed variables _X_ obs(M), if _FY |_ ( _X_ obs(M) _,M_ ) is continuous. Importantly, while this result is asymptotic, it holds for _any_ missing mechanism and it considers individualized conditional coverage. 

## **7 Empirical study** 

**Setup.** In all experiments, the data are imputed using iterative regression (iterative ridge implemented in Scikit-learn, Pedregosa et al. (2011)).[7] We compare the performance of our CQR-MDA-Exact and CQR-MDA-Nested 

> 7Theoretical results hold for any symmetric imputation. In practice, constant, mean and MICE imputations gave similar results. 

(that is CP-MDA based on CQR) to CQR as well as to a vanilla QR (without any calibration). The predictive models are fitted on the imputed data concatenated with the mask. Without concatenating the mask to the features, the maskconditional coverage of QR is worsened, as demonstrated in Section 4. The prediction algorithm is a Neural Network (NN), fitted to minimize the pinball loss (Sesia and Romano, 2021, see Appendix G.1 for details). For the vanilla QR, we use both the training and calibration sets for training. 

**Synthetic and semi-synthetic experiments.** We designed the training and calibration data to have 20% of MCAR values.� To evaluate the test marginal coverage P( _Y ∈ Cα_ ( _X, M_ )), missing values are introduced in the test set according to the same distribution as on the training and calibration sets.� Then, to compute an estimator of P( _Y ∈ Cα_ ( _X, m_ ) _|M_ = _m_ ) for each _m ∈M_ , we fix to a constant the number of observations per pattern, to ensure that the variability in coverage is not impacted by P ( _M_ = _m_ ). All experiments are repeated 100 times with different splits. 

## **7.1 Synthetic experiments: Gaussian linear data** 

**Data generation.** The data is generated with _d_ = 10 according to Model 4.1, with _X ∼N_ ( _µ,_ Σ), _µ_ = (1 _, · · · ,_ 1) _[T]_ and Σ = _φ_ (1 _, · · · ,_ 1) _[T]_ (1 _, · · · ,_ 1) + (1 _− φ_ ) _Id_ , _φ_ = 0 _._ 8, Gaussian noise _ε ∼N_ (0 _,_ 1) and the following regression coefficients _β_ = (1 _,_ 2 _, −_ 1 _,_ 3 _, −_ 0 _._ 5 _, −_ 1 _,_ 0 _._ 3 _,_ 1 _._ 7 _,_ 0 _._ 4 _, −_ 0 _._ 3) _[T]_[ 8] . Here, the oracle intervals are known (Proposition 4.2). 

**Lowest and highest mask coverage, and associated length.** Figures 1b and 8 (Appendix G.2) and Figure 9 (Appendix G.2) show the lowest and highest mask coverage and their associated length as a function of the training set size. The calibration size is fixed to 1000 and the test set contains 2000 points with the mask leading to the lowest coverage (here it corresponds to cases where only _X_ 4 is observed) and 2000 points with the mask leading to the highest coverage (here it corresponds to all the variables observed). These figures highlight that: 

- **CQR** and **QR** conditional coverage improve when the training size increases (Corollary 6.2); 

- **Both versions of CQR-MDA** are MCV (Theorem 5.3); 

- **CQR-MDA-Exact** is exactly MCV as highest and lowest mask coverage are exactly 90% (Theorem 5.3); 

- **CQR-MDA-Exact** ’s lengths converge to the oracle ones with increasing training size, showing it is not conservative, while **CQR-MDA-Nested** is overly conservative. 

**Coverage and length by mask size.** Figure 3 displays the average coverage and intervals’ length as a function of the pattern size, i.e., the performance metrics are aggregated by the masks with the same number of missing variables; the first violin plot of each panel corresponds to the marginal coverage (see Appendix G.2 for QR results). Note that 

> 8For dimension 3, in Figure 1a, the same model is used, keeping only the 3 first features and their associated parameters. 

7 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0008-00.png)


**----- Start of picture text -----**<br>
CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 00<br>0 . 75<br>0 . 50<br>15 Oracle length<br>10<br>5<br>NANANANANANANANANA NA NANANANANANANANANANA NANANANANANANANANANA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 3: Average coverage (top) and length (bottom) as a function of the number of missing values (NA). The first violin plot shows the marginal coverage. #Tr = 500 and #Cal = 250. The marginal test set includes 2000 observations. The mask-conditional test set includes 100 individuals for each missing data pattern size. 

only the pattern sizes are presented and not the patterns themselves as there are 2 _[d]_ = 1024 possible masks.[9] For each pattern size, 100 observations are drawn according to the distribution of _M |_ size( _M_ ) in the test set. The training and calibration sizes are respectively 500 and 250 (Figure 11 contains the results for other sizes). Figure 3 shows that: 

- **CQR** is marginally valid (Proposition 3.3); 

- **CQR** and **QR** undercover with an increasing number of missing values. This can be explained because their length nearly does not vary with the size of the missing pattern, despite having the mask concatenated with the features; 

- **Both versions of CQR-MDA** are marginally valid (Th. 5.4) and mask(-size)-conditionally-valid (Th. 5.3); 

- **CQR-MDA-Exact** is exactly mask(-size)-conditionallyvalid (Theorem 5.3) and its length is close to the oracle ones. It has more variability for the patterns with few missing values as for these masks Cal[(][test][)] is smaller. 

Similar experiments with 40% of missing values are available in Appendix G.3. Briefly, it corresponds to a setting where CP-MDA-Nested is preferable over CP-MDA-Exact as the former outputs smaller intervals and is less variable. 

## **7.2 Semi-synthetic experiments** 

We consider 6 benchmark real data sets for regression: meps_19, meps_20, meps_21 (MEPS, 2016), bio, bike and concrete (Dua and Graff, 2017), where we introduce missing values in their quantitative features, each of them having a probability 0.2 of being missing (i.e. it is a MCAR mechanism), as in the synthetic experiments. Note that therefore some patterns have a low (or null) frequency of appearance in the training sets of bio and concrete. The sample sizes for training, calibration, and testing, and simulation details are provided in Appendix G.4, along with 

> 9Note that in practice the relationship between the coverage and the number of missing values is not necessarily monotonic as a mask with only one missing value can lead to more uncertainty than a mask with many missing values, see Appendix D. 

results for smaller training and calibration sets. 

Figure 4 depicts the results by combining _validity_ and _efficiency_ (length) for meps_19, bio, concrete, and bike, where this graph follows the visualization used in Zaffran et al. (2022). The results for meps_20 and meps_21 are given in Appendix G.4, as they are similar to meps_19. 

Each of the panels in Figure 4 summarizes the results for one data set, with the average coverage shown in the _x_ - axis and the average length in the _y_ -axis. A method is mask-conditionally-valid if all the markers of its color are at the right of the vertical dotted line (90%). The design of Figure 4 requires a different interpretation than Figure 3 (or the subsequent Figure 5). For each method we report, for the pattern having the highest (or lowest) coverage, its length and coverage. However, as this pattern may depend on the method, the length for the highest/lowest should not be directly compared between methods. We observe that: 

• **CQR** is marginally valid (orange ♦, Proposition 3.3), but not MCV as the lowest mask coverage (orange ▼) is far below 90% (bio, concrete, and bike data sets); 

• **CQR-MDA-Exact** is marginally valid (purple ♦, Theorem 5.4). It is also exactly MCV, as the lowest (purple ▼) and highest (purple ▲) mask coverages are about 90% (Theorem 5.3); 

• **CQR-MDA-Nested** is marginally valid (blue ♦, Theorem 5.4). It is also MCV, as the lowest (blue ▼) mask coverage is larger than 90% (Theorem 5.3). 

## **7.3 Predicting the level of platelets for trauma patients** 

We study the applicability and robustness of CPMDA on the critical care TraumaBase® data. We focus on predicting the level of platelets of severely injured patients upon arrival at the hospital. This level is directly related to the occurrence of hemorrhagic shock and is difficult to obtain in real-time: predicting it accurately could be crucial to anticipate the need for transfusion and blood resources. In addition, this prediction task appears to be challenging as 

8 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0009-00.png)


**----- Start of picture text -----**<br>
meps_19 ( d  = 139,  l  = 5) bio ( d  = 9, l  = 9) concrete ( d  = 8, l  = 8) bike ( d  = 18, l  = 4)<br>20 60<br>25<br>440<br>18<br>50<br>20<br>16 420<br>40<br>15<br>14<br>400<br>0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 7 0 . 8 0 . 9 0 . 85 0 . 90<br>Average coverage Average coverage Average coverage Average coverage<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested Marginal Lowest Highest<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 4: Validity and efficiency with missing values for 4 data sets (panels) with _d_ features, including _l_ quantitative ones in which missing values are introduced with probability 0.2. Colors represent the methods. Diamonds (♦) represent marginal coverage while the patterns giving the lowest and highest mask coverage are represented with triangles (▼ and ▲). Vertical dotted lines represent the target coverage. 

Jiang et al. (2022) achieved an average relative prediction ˆ error ( _∥y − y∥_[2] _/∥y∥_[2] ) that is no lower than 0.23. This highlights the need for reliable uncertainty quantification. 

After applying inclusion and exclusion criteria obtained by medical doctors and following the pipeline of Sportisse et al. (2020) described in Appendix G.5, we left with a subset of 28855 patients and 7 features. Missing values vary from 0% to 24% by features, with a total average of 7%. 

**Results.** The results are summarized in Figure 5, where we use different markers to denote the different masks. To ensure a fair comparison between the conformal methods, we only keep the missing patterns for which there are more than 200 individuals; this excludes 7 patterns. Finally, since we found that the vanilla QR tends to be overly conservative, we refer to Appendix G.5 for its results. Figure 5 shows that all conformal approaches achieve marginal coverage higher than the desired 90% level (diamonds ♦). Furthermore, for each mask (each set of linked markers) **CQRMDA** improves coverage compared to **CQR** by approaching 90%, and efficiency by reducing the average length. Noticeably, for the pattern corresponding to all features observed (squares ■), **CQR-MDA** has a coverage rate above 90% 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0009-05.png)


**----- Start of picture text -----**<br>
CQR<br>1 . 8 CQR-MDA-Exact<br>CQR-MDA-Nested<br>1 . 6 Marginal<br>Mask-type<br>1 . 4<br>1 . 2<br>0 . 90 0 . 92 0 . 94<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 5: Average coverage and length on the TraumaBase® analysis. See the caption of Figure 4 for details. Other symbols than diamond correspond to computing the average per mask. Each individual’s prediction is obtained by using 15390 observations for training, and 7694 for calibration. 

while **CQR** is below the target level. Therefore, we believe **CQR-MDA** should be recommended as it improves upon the vanilla impute-then-regress+CQR approach. 

## **8 Conclusion and perspectives** 

In this paper, we study the interplay between uncertainty quantification and missing values. We show that missing values introduce heteroskedasticity in the prediction task. This brings challenges on how to provide uncertainty estimators that are valid conditionally on the missing patterns, which are addressed by this work. Our analysis leaves several directions open: (1) obtaining results _beyond the MCAR assumption_ for CP-MDA, both theoretically and numerically, (2) extending the (numerical) analysis to non-split approaches, (3) investigating the numerical performances of other conditional CP approaches (such as Sesia and Candes` (2020); Izbicki et al. (2020, 2022); Lin et al. (2021)), (4) studying the impact of the imputation on QR with finite samples. A more detailed discussion on these directions is provided in Appendix A. 

## **Acknowledgements** 

We thank Baptiste Goujaud for fruitful discussions. We sincerely thank anonymous reviewers for their feedbacks which improved the paper. This work was supported by a public grant as part of the Investissement d’avenir project, reference ANR-11-LABX-0056-LMH, LabEx LMH. M. Zaffran has been awarded the 2022 Scholarship for Mathematics granted by the Sephora Berrebi Foundation which she grate-´ fully thanks for its support. The work of A. Dieuleveut is partially supported by ANR-19-CHIA-0002-01/chaire SCAI and Hi! Paris. The work of J. Josse is partially supported by ANR-16-IDEX-0006. Y. Romano was supported by the ISRAEL SCIENCE FOUNDATION (grant No. 729/21). He also thanks the Career Advancement Fellowship, Technion, for providing additional research support. 

9 

## **References** 

- Angelopoulos, A. N. and Bates, S. (2023). _Conformal Prediction: A Gentle Introduction_ . Now Foundations and Trends. 

- Ayme, A., Boyer, C., Dieuleveut, A., and Scornet, E. (2022). Near-optimal rate of consistency for linear models with missing values. In Chaudhuri, K., Jegelka, S., Song, L., Szepesvari, C., Niu, G., and Sabato, S., editors, _Proceedings of the 39th International Conference on Machine Learning_ , volume 162, pages 1211–1243. PMLR. 

- Barber, R. F., Candes, E. J., Ramdas, A., and Tibshirani, R. J.` (2021a). The limits of distribution-free conditional predictive inference. _Information and Inference: A Journal of the IMA_ , 10(2):455–482. 

- Barber, R. F., Candes,` E. J., Ramdas, A., and Tibshirani, R. J. (2021b). Predictive inference with the jackknife+. _The Annals of Statistics_ , 49(1):486–507. 

- Barber, R. F., Candes, E. J., Ramdas, A., and Tibshirani, R. J.` (2022). Conformal prediction beyond exchangeability. 

- Dua, D. and Graff, C. (2017). UCI machine learning repository. 

- Eaton, M. L. (1983). _Multivariate statistics_ . John Wiley & Sons, Nashville, TN. 

- Gupta, C., Kuchibhotla, A. K., and Ramdas, A. (2022). Nested conformal prediction and quantile out-of-bag ensemble methods. _Pattern Recognition_ , 127:108496. 

- Izbicki, R., Shimizu, G., and Stern, R. (2020). Flexible distribution-free conditional predictive bands using density estimators. In Chiappa, S. and Calandra, R., editors, _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , volume 108, pages 3068–3077. PMLR. 

- Izbicki, R., Shimizu, G., and Stern, R. B. (2022). Cd-split and hpd-split: Efficient conformal regions in high dimensions. _Journal of Machine Learning Research_ , 23(87):1– 32. 

- Jiang, W., Bogdan, M., Josse, J., Majewski, S., Miasojedow, B., Rockovˇ a, V., and TraumaBase® Group (2022).´ Adaptive bayesian slope: Model selection with incomplete data. _Journal of Computational and Graphical Statistics_ , 31(1):113–137. 

- Josse, J., Prost, N., Scornet, E., and Varoquaux, G. (2019). On the consistency of supervised learning with missing values. 

- Josse, J. and Reiter, J. P. (2018). Introduction to the Special Section on Missing Data. _Statistical Science_ , 33(2):139 – 141. 

- Kingma, D. P. and Ba, J. (2014). Adam: A method for stochastic optimization. 

- Le Morvan, M., Josse, J., Moreau, T., Scornet, E., and Varoquaux, G. (2020a). Neumiss networks: differentiable programming for supervised learning with missing values. 

In Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., and Lin, H., editors, _Advances in Neural Information Processing Systems_ , volume 33, pages 5980–5990. Curran Associates, Inc. 

- Le Morvan, M., Josse, J., Scornet, E., and Varoquaux, G. (2021). What’s a good imputation to predict with missing values? In Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., and Vaughan, J. W., editors, _Advances in Neural Information Processing Systems_ , volume 34, pages 11530– 11540. Curran Associates, Inc. 

- Le Morvan, M., Prost, N., Josse, J., Scornet, E., and Varoquaux, G. (2020b). Linear predictor on linearly-generated data with missing values: non consistency and solutions. In Chiappa, S. and Calandra, R., editors, _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , volume 108, pages 3165–3174. PMLR. 

- Lei, J., G’Sell, M., Rinaldo, A., Tibshirani, R. J., and Wasserman, L. (2018). Distribution-Free Predictive Inference for Regression. _Journal of the American Statistical Association_ , 113(523):1094–1111. 

- Lei, J. and Wasserman, L. (2014). Distribution-free prediction bands for non-parametric regression. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 76(1):71–96. 

- Lin, Z., Trivedi, S., and Sun, J. (2021). Locally valid and discriminative prediction intervals for deep learning models. In Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., and Vaughan, J. W., editors, _Advances in Neural Information Processing Systems_ , volume 34, pages 8378–8391. Curran Associates, Inc. 

- Little, R. J. A. (2019). _Statistical analysis with missing data, third edition_ . John Wiley & Sons, Nashville, TN, 3 edition. 

- Manokhin, V. (2022). Awesome conformal prediction. 

- Mayer, I., Sportisse, A., Josse, J., Tierney, N., and Vialaneix, N. (2019). R-miss-tastic: a unified platform for missing values methods and workflows. 

- MEPS (2016). Medical expenditure panel survey. https://meps.ahrq.gov/mepsweb/data_ stats/data_overview.jsp. 

- Papadopoulos, H., Proedrou, K., Vovk, V., and Gammerman, A. (2002). Inductive confidence machines for regression. In Elomaa, T., Mannila, H., and Toivonen, H., editors, _Machine Learning: ECML 2002_ , pages 345–356, Berlin, Heidelberg. Springer Berlin Heidelberg. 

- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., and Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research_ , 12:2825–2830. 

10 

- Romano, Y., Barber, R. F., Sabatti, C., and Candes, E. (2020).` With Malice Toward None: Assessing Uncertainty via Equalized Coverage. _Harvard Data Science Review_ , 2(2). 

- Romano, Y., Patterson, E., and Candes, E. (2019).` Conformalized quantile regression. In Wallach, H., Larochelle, H., Beygelzimer, A., d'Alche-Buc, F., Fox, E., and Gar-´ nett, R., editors, _Advances in Neural Information Processing Systems_ , volume 32. Curran Associates, Inc. 

- Rubin, D. B. (1976). Inference and missing data. _Biometrika_ , 63(3):581–592. 

- Sesia, M. and Candes, E. J. (2020).` A comparison of some conformal quantile regression methods. _Stat_ , 9(1):e261. 

- Sesia, M. and Romano, Y. (2021). Conformal prediction using conditional histograms. In Ranzato, M., Beygelzimer, A., Dauphin, Y., Liang, P., and Vaughan, J. W., editors, _Advances in Neural Information Processing Systems_ , volume 34, pages 6304–6315. Curran Associates, Inc. 

- Sportisse, A., Boyer, C., Dieuleveut, A., and Josse, J. (2020). Debiasing averaged stochastic gradient descent to handle missing values. In Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., and Lin, H., editors, _Advances in Neural Information Processing Systems_ , volume 33, pages 12957– 12967. Curran Associates, Inc. 

- Van Ness, M., Bosschieter, T. M., Halpin-Gregorio, R., and Udell, M. (2022). The missing indicator method: From low to high dimensions. 

- Vovk, V. (2012). Conditional validity of inductive conformal predictors. In Hoi, S. C. H. and Buntine, W., editors, _Proceedings of the Asian Conference on Machine Learning_ , volume 25 of _Proceedings of Machine Learning Research_ , pages 475–490, Singapore Management University, Singapore. PMLR. 

- Vovk, V., Gammerman, A., and Shafer, G. (2005). _Algorithmic Learning in a Random World_ . Springer US. 

- Yang, M. (2015). _Features Handling by Conformal Predictors_ . PhD thesis, Royal Holloway, University of London. 

- Zaffran, M., Feron, O., Goude, Y., Josse, J., and Dieuleveut,´ A. (2022). Adaptive conformal predictions for time series. In Chaudhuri, K., Jegelka, S., Song, L., Szepesvari, C., Niu, G., and Sabato, S., editors, _Proceedings of the 39th International Conference on Machine Learning_ , volume 162, pages 25834–25866. PMLR. 

11 

## **Appendices** 

The appendices are organized as follows. 

Appendix A provides a more detailed discussion on open directions and perspectives. 

Appendix B describes CQR, used in the paper. 

Appendix C provides an explicit description of impute-then-predict+conformalization (Appendix C.1), along with its proof of validity, that is the proofs for Section 3 (Appendix C.2). 

Then, Appendix D contains the proofs for the Gaussian linear model oracle intervals presented in Section 4 (Appendix D.1), along with the discussion on how mean-based approaches fail (Appendix D.2). 

Appendix E gives the general statement of CP-MDA-Exact (Appendix E.1), and the proofs of the validity theorems for CP-MDA-Exact (Appendix E.2), along with the theoretical study of CP-MDA-Nested (Appendix E.3). 

Appendix F provides all the proofs about consistency and asymptotic conditional coverage presented in Section 6. 

Finally, Appendix G contains all the details for the experimental study and additional results completing Section 7. More precisely, Appendix G.1 gives more details about the settings. Appendix G.2 contains results on synthetic data with 20% of MCAR missing values, while Appendix G.3 shows the results on synthetic data when the proportion of MCAR missing values is 40%. Appendix G.4 describes the real data sets used for the semi-synthetic experiments, and presents the remaining results. Appendix G.5 presents the real medical data set (TraumaBase®), the pipeline and settings used and the results obtained by QR on this data set. 

## **A Detailed perspective discussion** 

First, obtaining results _beyond the MCAR assumption_ for CP-MDA. On the numerical side, preliminary experiments show promising results, indicating CP-MDA’s robustness, but a detailed numerical study is needed. On the theoretical side, understanding the limits of CP-MDA validity is of high importance. Results without assumptions on the missingness distribution seem impossible to obtain. Even with MAR data, the task of pointwise prediction can be very challenging if the output distribution strongly depends on the pattern (Ayme et al., 2022). As the impossibility results of conditional validity (Lei and Wasserman, 2014; Vovk, 2012; Barber et al., 2021a), assumptions on the missing mechanism are needed. 

Second, extending the (numerical) analysis to non-split approaches (e.g., based on the Jackknife) would be relevant, as it could improve the base model and therefore how the heteroskedasticity is taken into account. Note that CP-MDA can be written to take into account this splitting strategy, and thus our theoretical results on MCV would directly extend. 

Third, investigating the numerical performances of other conditional CP approaches (such as Sesia and Candes` (2020); Izbicki et al. (2020, 2022); Lin et al. (2021)) within the MDA framework is of interest. In this paper, we analyze empirically the instance of CP-MDA on top of CQR as it is the simplest version of QR based CP, but the theory and motivation of this work is not specific to CQR. Exactly as CQR, none of the aforementioned methods would provide MCV if used out of the box. But if combined with CP-MDA, then all of them will be granted MCV. 

Finally, while our approach is to be agnostic to the imputation chosen (similarly to CP being agnostic to the underlying model), an interesting research path is to study the impact of the imputation on QR with finite samples. 

## **B Illustration and details on CQR (Romano et al., 2019) procedure** 

Figure 6 provides a visualization and step by step description of CQR. 

## **C Impute-then-predict+conformalization** 

## **C.1 Description of the algorithm** 

Similarly, Algorithm 1 can be written to include any underlying predictive algorithm (regression or classification) and any score function. 

12 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0013-00.png)


**----- Start of picture text -----**<br>
4<br>2<br>0<br>▶ Create a proper training set, a calibration set, and keep<br>− 2 your test set, by randomly splitting your data set.<br>− 4<br>0 1 2 3 4 5<br>x<br>4<br>2<br>0 On the proper training set:<br>Step 1 ˆ ˆ<br>− 2 ▶ Learn q low and q upp<br>− 4<br>0 2 4<br>x<br>4<br>+ On the calibration set:<br>+<br>2 + + + - - - + + ▶ Predict with q ˆlow and q ˆupp<br>0<br>Step 2 ▶ Get the scoresˆ ˆ<br>− 2 + + - - - - - s [(] [k] [)] = max � q low � x [(] [k] [)][�] − y [(] [k] [)] , y [(] [k] [)] − q upp � x [(] [k] [)][��]<br>+<br>1<br>− 4 + ▶ Compute the (1  − α )  ×  (1 + #Cal [)][ empirical quantile of]<br>the  s [(] [k] [)] , noted Q [�] 1 −α ˆ ( S )<br>0 2 4<br>x<br>4<br>2<br>On the test set:<br>0<br>Step 3 ▶ Predict with q ˆlow and q ˆupp<br>− 2<br>▶ Build C [ˆ] α ˆ( x ): [ˆ q low( x )  − Q [�] 1 −α ˆ ( S )  ,  ˆ q upp( x ) + Q [�] 1 −α ˆ ( S )]<br>− 4<br>0 2 4<br>x<br>y<br>y<br>y<br>y<br>**----- End of picture text -----**<br>


Figure 6: Schematic illustration of Conformalized Quantile Regression (CQR) (Romano et al., 2019). 

13 

**Algorithm 3** SCP on impute-then-predict 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0014-01.png)


- 7: **end for** 

8: Set _S_ Cal = _{S_[(] _[k]_[)] _, k ∈_ Cal _}_ 

9: Compute _Q_[�] 1 _−α_ SCP ( _S_ Cal), the 1 _− α_[SCP] -th empirical quantile of _S_ Cal, with 1 _− α_[SCP] := (1 _− α_ ) (1 + 1 _/_ #Cal). 10: Set _C_[�] _α_ ( _X, M_ ) = _y_ such that _s_ ( _y,_ ˆ _g ◦_ Φ ( _X, M_ )) _≤ Q_[�] 1 _−α_ SCP ( _S_ Cal) . � � 

## **C.2 Proof of exchangeability after imputation** 

In this subsection, we provide a more formal statement of Lemma 3.2 and Proposition 3.3 in respectively Lemma C.1 and Proposition C.2. To that end, we introduce a notion of symmetrical imputation _on a set T_ , for _T ⊂_ �1 _, n_ + 1�. 

**Assumption A5** (Symmetrical imputation on a set _T_ ) **.** For a given set of points _{X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _}k∈T_ the imputation ( _d_ ) function Φ is the output of an algorithm _I_ that treats the data points in _T_ symmetrically: _I_ ( _{X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _}k∈T_ ) = _I_ ( _{X_[(] _[σ]_[(] _[k]_[))] _, M_[(] _[σ]_[(] _[k]_[))] _, Y_[(] _[σ]_[(] _[k]_[))] _}_ ) _k∈T_ conditionally to _{X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)] _}k∈T_ and for any permutation _σ_ on �1 _,_ # _T_ �. 

**Lemma C.1** (Imputation preserves exchangeability) **.** _Let A1 hold. Then, for any missing mechanism, for any imputation function_ Φ _satisfying A5, the imputed random variables_ �Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T[are exchangeable.]_ 

**Proposition C.2** ((Exact) validity of impute-then-predict+conformalization) **.** _If A1 is satisfied, then we have the following three results._ 

_1._ _**Full CP:** if A5 is satisfied for T_ = �1 _, n_ + 1� _(i.e., the imputation algorithm treats all points symmetrically), then impute-then-predict+Full CP is marginally valid. If moreover the scores are almost surely distinct, it is exactly valid. OR_ 

_2._ _**Jackknife+** if A5 is satisfied for T_ = �1 _, n_ + 1� _(i.e., the imputation algorithm treats all points symmetrically), then impute-then-predict+Jackknife+ is marginally valid (of level_ 1 _−_ 2 _α). OR_ 

_3._ _**SCP** with the split_ �1 _, n_ + 1� = Tr[�] Cal[�] Test _and if A5 is satisfied for T_ = Cal[�] Test _(i.e., the imputation treats all points in_ Cal[�] Test _symmetrically) then impute-then-predict+conformalization is marginally valid. If moreover the scores are almost surely distinct, it is exactly valid._ 

_Remark_ C.3 (Imputation choices for SCP) _._ In the latter case, for SCP, the coverage result can be derived conditionally on Tr, thus the coverage results holds for: (i) any deterministic imputation function (conditionally on Tr) (that is any arbitrary function of Tr), or (ii) any stochastic imputation function treating Cal and Test symmetrically (iii) any combination of both. 

_Proof of Lemma C.1._ Φ is the output of an imputing algorithm _I_ trained on �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T_ �. 

Assume � _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T_[are exchangeable (][A1][).] Thus, if _I_ treats the data points in _T_ symmetrically, �Φ( _X_[(] _[k]_[)] _, M_[(] _[k]_[)] ) _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈T_[are][exchangeable][(see][proof][of] Theorem 1b in (Barber et al., 2022) for example). 

_Proof of Proposition C.2._ Proposition C.2 is a consequence of Lemma C.1 with different choices of _T_ , that enable to apply the following results: 

14 

1. Full CP: Vovk et al. (2005), also re-stated in Barber et al. (2022) 

2. Jackknife+: Barber et al. (2021b) 

3. SCP: Lei et al. (2018) or Papadopoulos et al. (2002) and Angelopoulos and Bates (2023) for a generic version with any score function (note that the coverage is proved conditionally on Tr). 

## **D Gaussian linear model** 

**D.1 Distribution of** _Y |_ ( _X_ obs(m) _, M_ ) **and oracle intervals** 

**Proposition D.1** (Distribution of _Y |_ ( _X_ obs(M) _, M_ ) (Le Morvan et al., 2020b)) **.** _Under Model 4.1, for any m ∈{_ 0 _,_ 1 _}[d] :_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-06.png)


_with:_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-08.png)


**Proposition D.2** (Oracle intervals) **.** _Under Model 4.1, for any m ∈{_ 0 _,_ 1 _}[d] , for any δ ∈_ (0 _,_ 1) _:_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-10.png)


_and the oracle predictive interval length is given by:_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-12.png)


_Proof._ Using multivariate Gaussian conditioning (Eaton, 1983), for any subset of indices _L ∈_ �1 _, d_ �: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-14.png)


with _K_ = _L_[¯] (the complement indices) and: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-16.png)


Given that _Y_ = _β[T] X_ + _ε_ , with _ε ∼N_ (0 _, σε_[2][)] _[ ⊥⊥]_[(] _[X, M]_[)][, the following holds:] 

( _d_ ) ( _d_ ) _Y |_ ( _XL, M_ ) = ( _β[T] X_ + _ε_ ) _|_ ( _XL, M_ ) = _βL[T][X][L]_[+ (] _[ε]_[ +] _[ β] K[T][X][K]_[)] _[|]_[(] _[X][L][, M]_[)] and by Equation (6), _βK[T][X][K][|]_[(] _[X][L][, M]_[)] _[∼N]_[(] _[β] K[T][µ][M] K|L[, β] K[T]_[Σ] _[M] K|L[β][K]_[)][,][and][(] _[ε][|]_[(] _[X][L][, M]_[))] _[∼N]_[(0] _[, σ] ε_[2][)][,][and][(] _[β] K[T][X][K][⊥⊥] ε_ ) _|_ ( _XL, M_ ) . Thus: _Y |_ ( _XL, M_ ) _∼N_ ( _βL[T][X][L]_[+] _[ β] K[T][µ][M] K|L[, β] K[T]_[Σ] _[M] K|L[β][K]_[+] _[ σ] ε_[2][)] _[.]_ 

Consequently, for any _δ ∈_ (0 _,_ 1): 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-20.png)


For any pattern _m ∈{_ 0 _,_ 1 _}[d]_ , applying Equation (7) with _K_ = mis( _m_ ) = obs(m), _L_ = obs(m), we have, for any _δ ∈_ (0 _,_ 1): 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0015-22.png)


15 

and: 

with: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0016-02.png)


## **D.2 Discussion on how mean-based approaches fail** 

Under Model 4.1, the Bayes predictor for a quadratic loss in presence of missing values – E � _Y |_ � _X_ obs(M) _, M_ �� – is fully characterized (Le Morvan et al., 2020b,a; Ayme et al., 2022). Figure 7 is obtained by generating the data according to Model 4.1 with _d_ = 3, _β_ = (1 _,_ 2 _, −_ 1) _[T]_ and _σε_ = 1, with multivariate Gaussian _X_ and MCAR mechanism ( _X ⊥⊥ M_ ) (which is a particular case of Model 4.1 with _µ[m] ≡ µ_ and Σ _[m] ≡_ Σ). The left panel represents the method _Oracle mean + SCP_ where SCP is applied on the regressor being the Bayes predictor for the mean with absolute residuals as the score function. The first violin plot represents the marginal coverage whereas the other 7 represent conditional coverage with respect to the different possible patterns: conditional on observing all the variables, on observing all the variables except _X_ 1, except _X_ 2 etc (see Section 7 for details on the simulation process). 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0016-05.png)


**----- Start of picture text -----**<br>
Marginal X 1 missing X 1 and X 2 missing<br>No missing values X 2 missing X 1 and X 3 missing<br>X 3 missing X 2 and X 3 missing<br>1 . 0<br>0 . 9<br>0 . 8<br>0 . 7<br>0 . 6<br>0 . 5<br>Oracle mean + SCP Oracle mean + SCP per pattern size<br>coverage<br>Average<br>**----- End of picture text -----**<br>


Figure 7: Calibration set contains 500 points. Test size for each pattern is of 500 individuals and for marginal is of 2000. 200 repetitions allow to display violin plots, the horizontal black line representing the mean. 

**SCP on a (oracle) mean regressor lacks of conditional coverage with respect to the mask.** Figure 7 (left) highlights that even with the best mean regressor (the Bayes predictor) and an homoskedastic noise, usual SCP intervals: 

- over-cover when there are no missing values; 

- cover less for a mask _m_ ˘ than for a mask _m_ ˚ when _m_ ˚ _⊂ m_ ˘ (e.g. _m_ ˚ = (1 _,_ 0 _,_ 0) only _X_ 1 is missing, _m_ ˘ = (1 _,_ 1 _,_ 0) that is _X_ 1 and _X_ 2 are missing); 

- cover less when the most informative variable ( _X_ 2) is missing. 

To tackle this issue, one could calibrate conditionally to the missing data patterns. This is in the same vein as calibrating conditionally to the categories of a categorical variable or to different groups (Romano et al., 2020). This strategy is not viable as there are 2 _[d]_ patterns: the number of subsets grows exponentially with the dimension, implying the creation of subsets with too little data to perform the calibration. As an alternative, one could consider to perform calibration conditionally to the pattern size (e.g. when _d_ = 3, either 0 missing value, 1 or 2). This is possible as there are only _d_ different pattern sizes. 

**Calibrating by pattern size does not provide validity conditionally to the missing data patterns.** Figure 7 (right) shows the coverages of _Oracle mean + SCP per pattern size_ where SCP is applied on the Bayes predictor for the mean and the calibration is protected by pattern size. The previous statements still hold with this strategy, even if the coverage disparities are smaller. Therefore, it is not enough to calibrate per pattern size. 

16 

## **E Finite sample algorithms** 

## **E.1 General statement of Algorithm 1** 

We provide in Algorithm 4 a general statement of CP-MDA-Exact handling any learning algorithm (both regression and classification) and any score function. 

## **Algorithm 4** CP-MDA-Exact 

**Input:** Imputation algorithm _I_ , predictive algorithm _A_ , conformity score function _sg_ paramatrized by a model _g_ , significance level _α_ , training set �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][��] _[n] k_ =1[, test point] � _X_[(][test][)] _, M_[(][test][)][�] . **Output:** Prediction interval _C_[�] _α_ � _x_[(][test][)] _, m_[(][test][)][�] . 1: Randomly split _{_ 1 _, . . . , n}_ into two disjoint sets Tr and Cal. 2: Fit the imputation function: Φ( _·_ ) _←I_ ��� _X_[(] _[k]_[)] _, M_[(] _[k]_[)][�] _, k ∈_ Tr�� 3: Impute the training set: � _X_ imp[(] _[k]_[)] � _k∈_ Tr[:=] �Φ � _X_[(] _[k]_[)] _, M_[(] _[k]_[)][��] _k∈_ Tr ˆ 4: Fit algorithm _A_ : _g_ ( _·_ ) _←A_ ��� _X_ imp[(] _[k]_[)] _[, Y]_[(] _[k]_[)][�] _, k ∈_ Tr�� // Generate an augmented calibration set: 5: Cal[(][test][)] = k _∈_ Cal such that M[(k)] _⊂_ M[(][test][)][�] � 6: **for** � _k ∈_ Cal[(][test][)] **do** 7: _M_[(] _[k]_[)] = _M_[(][test][)] Additional masking 8: **end for** Augmented calibration set generated. // 9: Impute the calibration set: � _X_ imp[(] _[k]_[)] � _k∈_ Cal[(][test][)][:=] �Φ � _X_[(] _[k]_[)] _, M_[�][(] _[k]_[)][��] _k∈_ Cal[(][test][)] 10: **for** _k ∈_ Cal[(][test][)] **do** 11: Set _S_[(] _[k]_[)] = _sg_ ˆ � _Y_[(] _[k]_[)] _, X_ imp[(] _[k]_[)] �, the _conformity scores_ 12: **end for** 13: Set _S_ Cal = _{S_[(] _[k]_[)] _, k ∈_ Cal[(][test][)] _}_ ˜ ˜ 14: Compute _Q_[�] 1 _−α_ ˜ ( _S_ Cal), the 1 _− α_ -th empirical quantile of _S_ Cal, with 1 _− α_ := (1 _− α_ ) (1 + 1 _/_ # _S_ Cal). 15: Set _C_[�] _α_ � _X_[(][test][)] _, M_[(][test][)][�] = � _y_ such that _sg_ ˆ � _y,_ Φ � _X_[(][test][)] _, M_[(][test][)][��] _≤ Q_[�] 1 _−α_ ˆ ( _S_ Cal)�. 

## **E.2 Mask-conditional valitidy of CP-MDA-Exact** 

Before proving the results, we introduce a slightly stronger notion of mask-conditional-validity, when the calibration set is itself of random cardinality. 

**Definition E.1** (Mask-conditional-validity-random-calibration-size) **.** A method is mask-conditionally-valid with a random calibration size #Cal if for any _m ∈M_ , the lower bound is satisfied, and exactly mask-conditionally-valid if for any _m ∈M_ , 1 _≤ c ≤ n_ , the upper bound is also satisfied: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0017-08.png)


We start by proving Theorem E.2 that implies the result on CP-MDA-Exact in Theorem 5.3. 

**Theorem E.2.** _[Conditional validity of CP-MDA-Exact with calibration of random cardinality] Assume the missing mechanism is MCAR, and that Assumptions A1 to A3 hold. Then:_ 

- _CP-MDA-Exact is valid with a random calibration size_ #Cal _conditionally to the missing patterns;_ 

- _if the scores S_[(] _[k]_[)] _are almost surely distinct, CP-MDA-Exact is exactly mask-conditionally-valid with a random calibration_ 

- _size_ #Cal _._ 

_Proof of Theorem E.2._ Let Tr and Cal be two disjoint sets on �1 _, n_ �. Let _g_ ˆ be some model. Given A1, the sequence �� _X_[(] _[k]_[)] _, M_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, M_[(test)] _, Y_[(test)][��] is exchangeable. Therefore, the sequence �� _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, Y_[(test)][��] is also exchangeable. 

Let _m_ in _M_ . We define Cal[m] = �k _∈_ Cal such that M[(k)] _⊂_ m�. 

17 

Let _c ∈_ �1 _,_ #Cal�. 

As the _M ⊥⊥ X_ (missingness is MCAR) and ( _M ⊥⊥ Y_ ) _|X_ (Assumption A3), then _M ⊥⊥_ ( _X, Y_ ), and #Cal[m] _⊥⊥_ �X[(k)] _,_ Y[(k)][�] k _∈_ Cal _[,]_ �X[(test)] _,_ Y[(test)][�] . It follows that the sequence �� _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal[m] _[ ,]_ � _X_[(test)] _, Y_[(test)][��] is exchangeable conditionally to #Cal[m] = c. Similarly, _M_[(test)] _⊥⊥_ � _X_[(] _[k]_[)] _, Y_[(] _[k]_[)][�] _k∈_ Cal _[,]_ � _X_[(test)] _, Y_[(test)][�] . Thus the sequence _{_ � _X_[(] _[k]_[)] _, M_[(test)] _, Y_[(] _[k]_[)][�] _k∈_ Cal[m] _[ ,]_ � _X_[(test)] _, M_[(test)] _, Y_[(test)][�] _}_ is exchangeable conditionally to #Cal[m] = c and _M_[(test)] = _m_ . Therefore, we can now invoke Proposition 3.3 in combination with Lemma 1 of Romano et al. (2020) to conclude the proof. But we can state a more rigorous version here, since in fact Cal[m] is a random variable (as discussed in Definition E.1). 

Since the algorithm _I_ treats the calibration and test data points symmetrically (A5 with _T_ = Cal[�] Test), A5 also holds for any _T[′] ⊂ T_ . Therefore, by Lemma C.1 the sequence ��Φ( _X_[(] _[k]_[)] _, M_[(test)] ) _, M_[(test)] _, Y_[(] _[k]_[)][�] _k∈_ Cal[m] _[ ,]_ �Φ( _X_[(test)] _, M_[(test)] ) _, M_[(test)] _, Y_[(test)][��] is exchangeable conditionally to #Cal[m] = c and _M_[(test)] = _m_ . 

The conclusion follows from usual arguments (Papadopoulos et al., 2002; Lei et al., 2018; Angelopoulos and Bates, 2023). Precisely, �� _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))� _k∈_ Cal[m] _[ , s][g]_[ˆ][(] _[Y]_[(test)] _[,]_[ Φ(] _[X]_[(test)] _[, M]_[ (test)][))] � is exchangeable conditionally to #Cal[m] = c and _M_[(test)] = _m_ . Therefore, 

P _sg_ ˆ( _Y_[(test)] _,_ Φ( _X_[(test)] _, M_[(test)] )) _≤ Q_[�] 1 _−α_ ˜(( _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))) _k∈_ Cal[m] ) _M_ (test) = _m,_ #Calm = c _≥_ 1 _− α,_ � ��� � 

and if the �� _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))� _k∈_ Cal[m] _[ , s][g]_[ˆ][(] _[Y]_[(test)] _[,]_[ Φ(] _[X]_[(test)] _[, M]_[ (test)][))] � are almost surely distinct (i.e. have a continuous distribution) then (Lei et al., 2018; Romano et al., 2019): P � _sg_ ˆ( _Y_[(test)] _,_ Φ( _X_[(test)] _, M_[(test)] )) _≤ Q_[�] 1 _−α_ ˜(( _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))) _k∈_ Cal[m] )��� _M_ (test) = _m,_ #Calm = c� _≤_ 1 _− α_ + _c_ +11 _[.]_ This proves the first two points (with respect to Definition E.1) of Theorem 5.3, by observing that � _Y_[(test)] _∈ C_[�] _α_ ( _X_[(test)] _, M_[(test)] )� = � _sg_ ˆ( _Y_[(test)] _,_ Φ( _X_[(test)] _, M_[(test)] )) _≤ Q_[�] 1 _−α_ ˜ �� _sg_ ˆ( _Y_[(] _[k]_[)] _,_ Φ( _X_[(] _[k]_[)] _, M_[(test)] ))� _k∈_ Cal[m] ��. 

Then, the proof of Theorem 5.4 (marginal validity of the CP-MDA-Exact) is direct by marginalizing the result of Theorem 5.3. 

## **E.3 Validities of CP-MDA-Nested.** 

Next, we give more details on the results on CP-MDA-Nested. 

E.3.1 MASK-CONDITIONAL-VALIDITY OF CP-MDA-NESTED. Let _m ∈M_ . 

We start by describing the links between CP-MDA-Nested and CP-MDA-Exact. CP-MDA-Exact can be re-written in the same way as CP-MDA-Nested, but keeping the subselection step of l. 5. 

Indeed, first mention that the output of Algorithm 1 can be written in the following ways: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0018-12.png)


ˆ With _Z[m] α_ 2 := _{z_[(] _α_ 2 _[k]_[)] _[, k][∈]_[Cal][ and][M][�][(k)][=][m] _[}]_[,][and][similarly][for][the][upper][bag.][Recall][that][we][have:] _[z]_[(] _α_ 2 _[k]_[)] = _q[α]_ 2 _[◦]_ � Φ � _x_[(][test][)] _, m_[(] _[k]_[)][�] _− s_[(] _[k]_[)] _._ 

On the other hand, the output predictive interval of Algorithm 2 is then written as: 

18 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-00.png)


With these notations, _Z[α]_ 2[can be partitioned as] 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-02.png)


With 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-04.png)


The result of Algorithm 1 implies that for any mask _m ∈M_ , we have : 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-06.png)


i.e. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-08.png)


Where: _Q_ 1 _−α_ ˜ ( _S_ ) is the (1 _− α_ )(1 + 1 _/_ # _S_ )-quantile of _S_ and _S[m]_ = _{s_[(] _[k]_[)] for _k ∈_ Cal and M[�][(k)] = m _}_ . Equivalently: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-10.png)


In the following Lemma, we show that for _m_ ˜ _⊃ m_ the result extends under Assumption A4. **Lemma E.3.** _Assume Assumption A4. For any m ∈M, for any m_ ˜ _⊃ m_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-12.png)


_This inequality shows the conservativeness of the quantiles of the bags resulting from larger missing patterns m_ ˜ _than m when the construction of the output of Algorithm 2._ 

_While inequality Equation_ (10) _is “tight” in the sense that the probability is almost exactly_ 1 _− α (item 2 of Theorem 5.3), the proof hereafter shows that Equation_ (11) _can be pessimistic in terms of actual coverage, as one may have_ P[( _Y_[(test)] _∈/_ [ _Q_[�] _α_ ˜( _Z[m] α_ 2[˜][);] _[Q]_[�][1] _[−][α]_[˜][(] _[Z]_ 1 _[m]_[˜] _−[α]_ 2[)])] _[|][M]_[ (test)][=] _[ m]_[]] _[ ≪][α][.]_ 

_More precisely, we have the following inequality:_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-16.png)


The interpretation of that Lemma is that the intervals resulting from the prediction on _x_[test] _, m_ ˜ (more data hidden) and corrected with the residuals of the calibration points ( _X[k] , M[k]_ = _m, Y_ ˜ _[k]_ ) have a _larger_ probability of containing _Y_[test] , conditionally to _X_ obs(m) than the interval built using prediction on _x_[test] _, m_ (more data available) and corrected with the residuals of the calibration points ( _X[k] , M[k]_ = _m, Y[k]_ ) (more data available) 

_Proof of Lemma E.3._ We start by invoking Equation (9) for _m_ ˜ : 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0019-19.png)


Consequently, by the tower property of conditional expectations: 

19 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0020-00.png)


ˆ ˜ Observe that _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜] � _S[m]_[˜][�] is _{M_[(test)] = _m, S_[( ˜] _[m]_[)] _, X_ obs( ˜m)[(test)] _[}]_[-measurable.] Moreover, by Assumption A4, we have that for any _δ ∈_ [0 _,_ 0 _._ 5]: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0020-02.png)


� In other words the conditional distribution of _Y_ given _X_ obs(m)� and _M_ = _m_ “stochastically dominates” the conditional distribution of _Y_ given _X_ obs(m) and _M_ = _m_ . 

We thus have, with _FZ_ denoting the cumulative distribution function of� _Z_ : _FY |_ ( _X_ obs(m) � _[,M]_[=] _m_[ �] )[the cumulative distribution] function of _Y |_ ( _X_ obs(m)� _, M_ = _m_ ): 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0020-05.png)


At (i) we use (16) _FY |_ ( _X_ obs(m) _,M_ = _m_ )(ˆ _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜][(] _[S] m_[˜] )) _≤ FY |_ ( _X_ obs(m) � _[,M]_[=][ �] _m_ )[(ˆ] _[q][α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜][(] _[S] m_[˜] )), and (15): _FY |_ ( _X_ obs(m) _,M_ = _m_ )(ˆ _q_ 1 _−[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜][(] _[S] m_[˜] )) _≥ FY |_ ( _X_ obs(m) � _[,M]_[=][ �] _m_ )[(ˆ] _[q]_ 1 _−[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜][(] _[S] m_[˜] )) by ˆ A4. Remark that here we assume that � _q_ 1 _−[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][) +] _[Q]_[�][1] _[−][α]_[˜][(] _[S][m]_[˜][)] � _≥_ median(Y[(test)] _|_ (X[(test)] obs(m)� _[,]_[ M][=][˜m)][ and] ˆ � _q[α]_ 2 _[◦]_[Φ(] _[X]_[(test)] _[,][m]_[˜][)] _[ −][Q]_[�][1] _[−][α]_[˜][(] _[S][m]_[˜][)] � _≤_ median(Y[test] _|_ (X[(test)] obs(m)� _[,]_[ M =][m)][�][.] We obtain Equation (12) in Lemma E.3 by plugging (17) in (14), then Equation (11) by the tower property. 

**Theorem E.4.** _Assume the missing mechanism is MCAR, and that Assumptions A1 to A3 hold. Additionally Assumption A4 is satisfied._ 

_Consider the partition described in Equation_ (8) _, and consider CP-MDA-Nested running on a test point with missing pattern m_[(test)] _, with any of the following outputs, instead of l. 15 C_[�] _α_ � _x_[(] _[test]_[)] _, m_[(] _[test]_[)][�] = [ _Q_[�] _α_ ˜ � _Z[α]_ 2 � ; _Q_[�] 1 _−α_ ˜ � _Z_ 1 _−[α]_ 2 �] _:_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0020-09.png)


_Then the resulting algorithm is mask-conditionally-valid._ 

_Proof of Theorem E.4._ The proof immediately follows from Equation (11), and gives the result without difficulty for any arbitrary pattern or random variable independent of all other randomness. 

Extension to a choice that involves the cardinality of the sets _Zα/[m]_[˜] 2[, leveraging the independence between these cardinals and] the coverage properties (same as in the proof of Theorem E.2). 

Then, the proof of Theorem 5.4 (marginal validity of the CP-MDA-Nested) is direct by marginalizing the result of Theorem E.4. 

20 

## **F Infinite data results** 

**Proposition 6.1 (** _ℓβ_ **-consistency of an universal learner).** _Let β ∈_ [0 _,_ 1] _. If X admits a density on X , then, for almost all imputation function_ Φ _∈F∞[I][, the function][ g] ℓ[∗] β ,_ Φ _[◦]_[Φ] _[ is Bayes optimal for the pinball risk of level][ β][.]_ 

> _Proof of Proposition 6.1._ The proof starts in the exact same way than Le Morvan et al. (2021), based on their Lemmas A.1 and A.2. For completeness, we copy here the statements of these lemmas without their proof and rewrite the two first parts of the main proof. 

Let Φ be an imputation function such that for each missing data pattern _m_ , _ϕ[m] ∈C[∞]_[�] R _[|]_[obs(m)] _[|] ,_ R _[|]_[mis(] _[m]_[)] _[|]_[�] . 

**Lemma F.1** (Lemma A.1 in Le Morvan et al. (2021)) **.** _Let ϕ[m] ∈C[∞]_[�] R _[|]_[obs(m)] _[|] ,_ R _[|]_[mis(] _[m]_[)] _[|]_[�] _be the imputation function for missing data pattern m, and let M[m]_ = � _x ∈_ R _[d]_ : _x_ mis( _m_ ) = _ϕ[m]_[ �] _x_ obs((m))�� _. For all m, M[m] is an |_ obs((m)) _|dimensional manifold._ 

In Lemma F.1, _M[m]_ represents the manifold in which the data points are sent once imputed by _ϕ[m]_ . Lemma F.1 states that this manifold is of dimension _|_ obs(m) _|_ . 

**Lemma F.2** (Lemma A.2 in Le Morvan et al. (2021)) **.** _Let m and m[′] be two distinct missing data patterns with the same number of missing (resp. observed) values |_ mis _| (resp |_ obs _|). Let ϕ[m] ∈C[∞]_[�] R _[|]_[obs(m)] _[|] ,_ R _[|]_[mis(] _[m]_[)] _[|]_[�] _be the imputation function for missing data pattern m, and let M[m]_ = � _x ∈_ R _[d]_ : _x_ mis( _m_ ) = _ϕ[m]_[ �] _x_ obs(m)�� _. We define similarly_ Φ[(] _[m][′]_[)] _and M_[(] _[m][′]_[)] _. For almost all imputation functions ϕ[m] and_ Φ[(] _[m][′]_[)] _,_ 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0021-07.png)


Note that, as by Lemma F.1 dim ( _M[m]_ ) = dim _M_[(] _[m][′]_[)][�] = _|_ obs _|_ = d _−|_ mis _|_ , Lemma F.2 states that � dim _M[m] ∩M_[(] _[m][′]_[)][�] _≤_ dim ( _M[m]_ ) = dim _M_[(] _[m][′]_[)][�] . � � 

Now, to prove Proposition 6.1 the missing data patterns are ordered as in Le Morvan et al. (2021): the first one will be the one in which all the variables are missing, while the last one will be the one in which all the variables are observed. For two data patterns with the same number of missing variables, the ordering is picked at random. We denote by _m_ ( _i_ ) the _i_ -th missing data pattern according to this ordering. 

We are going to build a function _g_ Φ which, composed with Φ, will reach the _ℓ_ -Bayes risk. 

For each missing data pattern, and starting by _m_ (1) of all variables missing, we can define _g_ Φ on the data points from the current missing data pattern. More precisely, for each _i_ , _g_ Φ is built for every imputed data point belonging to _M_[(] _[m]_[(] _[i]_[))] except for those already considered in previous steps (one imputed data point can belong to multiple manifolds): 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0021-12.png)


That is, _g_ Φ _◦_ Φ( _X, M_ ) will equal _f_[˜] _[∗]_ ( _X, M_ ) except possibly if Φ( _X, M_ ) = Φ( _Y_[˜] ) for some _Y_[˜] that has more missing values than _X, M_ . Therefore, for each missing data pattern _m_ ( _i_ ), _g_ Φ _◦_ Φ equals _f_[˜] _[∗]_ except on[�] _k<i[M]_[(] _[m]_[(] _[k]_[))][.][The question that] remains is: what is the dimension of _M_[(] _[m]_[(] _[i]_[))][ ���] _k<i[M]_[(] _[m]_[(] _[k]_[))][�] , these points for which there is no necessarily equality between _g_ Φ _◦_ Φ and _f_[˜] _[∗]_ . First, note that _M_[(] _[m]_[(] _[i]_[))][ ���] _k<i[M]_[(] _[m]_[(] _[k]_[))][�] =[�] _k<i_ � _M_[(] _[m]_[(] _[i]_[))][ �] _M_[(] _[m]_[(] _[k]_[))][�] . For each space in this reunion, there are two cases: 

- either _|_ obs(m(k)) _|< |_ obs(m(i)) _|_ : using Lemma F.1, dim � _M_[(] _[m]_[(] _[k]_[))][�] = _|_ obs(m(k)) _|< |_ obs(m(i)) _|_ = dim � _M_[(m(i))][�] . Thus, _M_[(] _[m]_[(] _[i]_[))][ �] _M_[(] _[m]_[(] _[k]_[))] is of measure zero in _M_[(] _[m]_[(] _[i]_[))] . 

- either _|_ obs(m(k)) _|_ = _|_ obs(m(i)) _|_ : using Lemma F.2, _M_[(] _[m]_[(] _[i]_[))][ �] _M_[(] _[m]_[(] _[k]_[))] is of dimension 0 or smaller than dim � _M_[(] _[m]_[(] _[i]_[))][�] , thus it is of measure zero in _M_[(] _[m]_[(] _[i]_[))] . 

21 

Therefore, the set of data points for which _g_ Φ _◦_ Φ does not equal the oracle is of measure 0 for each missing data pattern. Let _β ∈_ [0 _,_ 1]. We can now write down the _ℓβ_ -risk of this built function: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-01.png)


where ( _i_ ) holds thanks to the shape of _ρβ_ . For any _w ∈_ R and any _λ ∈_ R+: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-03.png)


Furthermore, _ρβ_ is convex, thus for any ( _u, v_ ) _∈_ R[2] : 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-05.png)


˜ As _f_[˜] _[∗]_ and _g[∗] ◦_ Φ are equals almost everywhere on each missing subspace, E _ρβ f ∗_ ( _X, M_ ) _− g[∗] ◦_ Φ( _X, M_ ) = 0. � � �� Indeed, decomposing by pattern one can write: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-07.png)


and thus by equality almost everywhere for each pattern every term in this sum is null. 

Therefore one obtains: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-10.png)


Thus: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-12.png)


and _g[∗] ◦_ Φ is Bayes optimal. This implies that _R[∗] ℓβ ,_ Φ[=] _[ R][∗] ℓβ_[.][Thus, a universally consistent algorithm learning] _[ g]_[Φ][ chained] with Φ will lead to a Bayes consistent function. 

_Proof of Corollary 6.2._ Corollary 6.2 states that “For any missing mechanism, for almost all imputation function Φ _∈F∞[I]_[, if] _FY |_ ( _X_ obs(M) _,M_ ) is continuous, a universally consistent quantile regressor trained on the imputed data set yields asymptotic conditional coverage.”. 

Let _β ∈_ [0 _,_ 1]. 

Remark that Proposition 6.1 states that for any missing mechanism, for almost all imputation function Φ _∈F∞[I]_ a universally consistent quantile regressor trained on the imputed data set achieves the Bayes risk asymptotically. We will thus show that any _ℓβ_ -Bayes predictor _fβ[∗]_[(any][function][achieving][the] _[ℓ][β]_[-Bayes-risk)][is][such][that][P][(] _[Y] ≤ fβ[∗]_[(] _[X, M]_[)] _[|][X]_[obs(M)] _[, M]_[)][=] _[β]_[if] _[F][Y][ |]_[(] _[X]_ obs(M) _[,M]_[)][is][continuous.][Therefore,][any][two][Bayes][predictors] _[f] α/[ ∗]_ 2[and] _[f]_ 1 _[ ∗] −α/_ 2 form an interval [ _fα/[∗]_ 2[(] _[X, M]_[);] _[ f]_ 1 _[ ∗] −α/_ 2[(] _[X, M]_[)]][ that achieves conditional coverage (conditionally to] _[ X]_[obs(M)][ and] _[ M]_[).] 

Let _fβ[∗]_[be a] _[ ℓ][β]_[-Bayes predictor.][Then:] 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0022-18.png)


22 

Let ( _x, m_ ) _∈X × M_ . Denote _Hx,m_ ( _z_ ) := E � _ρβ_ ( _Y − z_ ) _|X_ obs(M) = _x_ obs(m) _, M_ = _m_ �. As _Y_ = _z_ almost surely, we have: 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0023-01.png)



![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0023-02.png)


If _FY |_ ( _X_ obs(M) _,M_ ) is continuous, there exists at least a solution, that might not be unique if it is not additionally strictly increasing. Therefore, if _FY |_ ( _X_ obs(M) _,M_ ) is continuous, all the _ℓβ_ -Bayes predictors can be written as _fβ[∗]_[(] _[x, m]_[) =] _[ q][x,m]_[ with] P � _Y ≤ qx,m|X_ obs(M) = _x_ obs(m) _, M_ = _m_ � = P � _Y ≤ fβ[∗]_[(] _[x, m]_[)] _[|][X]_[obs(M)][=] _[ x]_[obs(m)] _[, M]_[=] _[ m]_ � = _β_ . 

## **G Experimental study** 

## **G.1 Settings detail** 

**Quantile Neural Network.** The architecture and optimization of the Quantile Neural Network used in the experiments is taken from Sesia and Romano (2021) (their code is freely available). This is the description provided in the original paper of the neural network: “The network is composed of three fully connected layers with a hidden dimension of 64, and ReLU activation functions. We use the pinball loss to estimate the conditional quantiles, with a dropout regularization of rate 0.1. The network is optimized using Adam Kingma and Ba (2014) with a learning rate equal to 0.0005. We tune the optimal number of epochs by cross validation, minimizing the loss function on the hold-out data points; the maximal number of epochs is set to 2000.” 

## **G.2 Gaussian linear results** 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0023-08.png)


**----- Start of picture text -----**<br>
15 . 0<br>0 . 8<br>12 . 5 QR<br>CQR<br>0 . 6 10 . 0 CQR-MDA-exact<br>CQR-MDA-nested<br>7 . 5<br>Oracle<br>0 . 4<br>5 . 0<br>0 . 2 2 . 5<br>Training size Training size<br>50 100 500 1000 2500 5000 20000 50 100 500 1000 2500 5000 20000<br>mask<br>the coverage<br>coverage<br>mask on lowest<br>length<br>Lowest the<br>with<br>Average<br>**----- End of picture text -----**<br>


Figure 8: Coverage and interval’s length for the mask leading to the lowest coverage. Model is NN. Calibration size fixed to 1000. The mask is concatenated in the features. Data is imputed using Iterative Ridge. 100 repetitions allow to display error bars, corresponding to standard error. 

Figure 9 is the analogous of Figure 8, but by evaluating the performances on the mask leading to the highest coverage. 

Hereafter, we present in Figure 10 the exact same figure than Figure 3 but with a panel (the first) for vanilla QR. The 3 other methods are displayed again to facilitate the comparison. 

Finally, Figure 11 is the analogous of Figure 10, but for a training set containing 1000 observations and a calibration set containing 500 observations. 

23 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0024-00.png)


**----- Start of picture text -----**<br>
1 . 0<br>0 . 9 8<br>QR<br>0 . 8 CQR<br>6 CQR-MDA-exact<br>0 . 7<br>CQR-MDA-nested<br>Oracle<br>0 . 6<br>4<br>0 . 5<br>2<br>Training size Training size<br>Coverage and interval’s length for the mask leading to the highest coverage. See caption of Figure 8 8 for the setting.<br>QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>0 . 6<br>0 . 4<br>w Oracle length<br>15<br>10 . | | 1<br>5<br>50 100 500 1000 2500 5000 20000 50 100 500 1000 2500 5000 20000<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>mask<br>the coverage<br>coverage<br>on<br>mask highest<br>length<br>Highest the<br>with<br>Average<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 9: Coverage and interval’s length for the mask leading to the highest coverage. See caption of Figure 8 8 for the setting. 

Figure 10: Average coverage (top) and length (bottom) as a function of the pattern size, i.e. the number of missing values (NA). First violin plot corresponds to marginal coverage. Stars correspond to the oracle length. Settings are: model is NN, train size is 500, calibration size is 250. The marginal test set includes 2000 observations. The conditional test set includes 100 individuals for each possible missing data pattern size. The mask is concatenated to the features. Data is imputed using Iterative Ridge. 100 repetitions are performed. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0024-03.png)


**----- Start of picture text -----**<br>
QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 0<br>0 . 8<br>0 . 6<br>15 Oracle length<br>10 te | r<br>5<br>egaeasottl ane sson atttee<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 11: Model is NN. Train size is 1000. Calibration size fixed to 500. The marginal test set includes 2000 observations. The conditional test set includes 100 individuals for each possible missing data pattern size. The mask is concatenated in the features. Data is imputed using Iterative Ridge. 100 repetitions are performed. 

24 

## **G.3 Higher proportion of missing values** 

We present synthetic experiments where the proportion of MCAR missing values is of 40% (instead of 20% in Figure 3). Except from this, the settings are exactly the same than the ones of Figure 3. Precisely, the data is generated with _d_ = 10 according to Model 4.1, with _X ∼N_ ( _µ,_ Σ), _µ_ = (1 _, · · · ,_ 1) _[T]_ and Σ = _φ_ (1 _, · · · ,_ 1) _[T]_ (1 _, · · · ,_ 1) + (1 _− φ_ ) _Id_ , _φ_ = 0 _._ 8, Gaussian noise _ε ∼N_ (0 _,_ 1) and the following regression coefficients _β_ = (1 _,_ 2 _, −_ 1 _,_ 3 _, −_ 0 _._ 5 _, −_ 1 _,_ 0 _._ 3 _,_ 1 _._ 7 _,_ 0 _._ 4 _, −_ 0 _._ 3) _[T]_ . For each pattern size, 100 observations are drawn according to the distribution of _M |_ size( _M_ ) in the test set. The training and calibration sizes are respectively 500 and 250. The experiment is repeated 100 times. The results are displayed in Figure 12. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0025-02.png)


**----- Start of picture text -----**<br>
QR CQR CQR-MDA-Exact CQR-MDA-Nested<br>1 . 00<br>0 . 75<br>0 . 50<br>40 Oracle length<br>20<br>Figure 12: Same caption than Figure 10.<br>NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA NA<br>0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9<br>Marg. Marg. Marg. Marg.<br>coverage<br>Average<br>length<br>Average<br>**----- End of picture text -----**<br>


Interestingly, although expected, these experiments lead CP-MDA-Exact to frequently output infinite intervals. This is because the subsampling step with few calibration data – with respect to the dimension and proportion of missing values – reached a point where there are not enough observations for CP-MDA-Exact to calibrate accurately for some patterns. 

To compare CP-MDA-Exact and CP-MDA-Nested in this setting, Figure 12 is obtained by replacing the infinite intervals by _k∈T r_ max _∪Cal[y]_[(] _[k]_[)] _[−] k∈T r_ min _∪Cal[y]_[(] _[k]_[)][.][It][highlights][that][CP-MDA-Exact][is][less] _[efficient]_[(i.e.][outputs][larger][intervals)][than] CP-MDA-Nested for patterns with less than 4 NAs. With a smaller calibration set or a higher proportion of missing values, this effect would be amplified and generalized to more patterns. Figure 12 also emphasizes that CP-MDA-Exact leads to more coverage variability than CP-MDA-Nested, on the patterns for which CP-MDA-Exact does not almost surely cover. 

## **G.4 Semi-synthetic experiments** 

In the semi-synthetic experiments, two settings are examined: one where the training size is small in comparison to the number of parameters of the Neural Network – “Medium” –, and one where the training size is even smaller so that some masks have a really low (or null) frequency of appearance in the training set – “Small”. In both cases, the calibration size is approximately half the training size. Figure 4 presented the results for the “Medium” case. 

Table 1: Semi-synthetic settings: training and calibration sizes for each of the 6 data sets depending on the setting. 

|||meps_19<br>_d_= 139,_l_ = 5<br>_n_= 15785|meps_20<br>_d_= 139,_l_ = 5<br>_n_= 17541|meps_21<br>_d_= 139,_l_ = 5<br>_n_= 15656|bio<br>_d_= 9,_l_ = 9<br>_n_= 45730|bike<br>_d_= 18,_l_ = 4<br>_n_= 10886|concrete<br>_d_= 8,_l_ = 8<br>_n_= 1030|
|---|---|---|---|---|---|---|---|
|||||||||
|Small|Trsize<br>Calsize|500<br>250|500<br>250|500<br>250|500<br>250|500<br>250|330<br>100|
|||||||||
|Medium|Trsize<br>Calsize|1000<br>500|1000<br>500|1000<br>500|1000<br>500|1000<br>500|630<br>200|



Figure 13 represents the results for these settings, using the same parameters than Figure 4. For the results on the two other meps data sets (meps_20 and meps_21) see Figure 14, which repeats the visualisation of meps_19 to ease comparison. 

25 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0026-00.png)


**----- Start of picture text -----**<br>
meps_19 ( d  = 139,  l  = 5) bio ( d  = 9, l  = 9) concrete ( d  = 8, l  = 8) bike ( d  = 18, l  = 4)<br>20 60<br>30 450<br>18<br>50<br>425<br>16<br>20<br>40 400<br>14<br>375<br>10 12 30<br>0 . 6 0 . 8 0 . 6 0 . 8 0 . 6 0 . 8 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage Average coverage<br>QR CQR-MDA-Exact Marginal Highest Small<br>CQR CQR-MDA-Nested Lowest Medium<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 13: Model is NN. The mask is concatenated in the features. Data is imputed using Iterative Ridge. 100 repetitions are performed, allowing to display the standard error as error bars. The vertical dotted lines represent the target coverage of 90%. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0026-02.png)


**----- Start of picture text -----**<br>
meps_19 ( d  = 139, l  = 5) meps_20 ( d  = 139, l  = 5) meps_21 ( d  = 139, l  = 5)<br>35<br>30<br>25<br>20<br>15<br>10<br>0 . 5 0 . 6 0 . 7 0 . 8 0 . 9 0 . 5 0 . 6 0 . 7 0 . 8 0 . 9 0 . 5 0 . 6 0 . 7 0 . 8 0 . 9<br>Average coverage Average coverage Average coverage<br>QR CQR-MDA-Exact Marginal Highest Small<br>CQR CQR-MDA-Nested Lowest Medium<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 14: Same caption than Figure 13. 

## **G.5 Real data** 

**Data set description.** Sportisse et al. (2020) selected 7 variables to model the level of platelets, after discussion with medical doctors. Thus, we followed their pipeline. Here are the 7 variables used: 

- Age: the age of the patient (no missing values); 

- Lactate: the conjugate base of lactic acid, upon arrival at the hospital (17.66% missing values); 

- Delta_hemo: the difference between the hemoglobin upon arrival at hospital and the one in the ambulance (23.82% missing values); 

- VE: binary variable indicating if a Volume Expander was applied in the ambulance. A volume expander is a type of intravenous therapy that has the function of providing volume for the circulatory system (2.46% missing values); 

- RBC: a binary index which indicates whether the transfusion of Red Blood Cells Concentrates is performed (0.37% missing values); 

- SI: the shock index. It indicates the level of occult shock based on heart rate (HR) and systolic blood pressure (SBP), that is SI =[HR] SBP[, upon arrival at hospital (2.09% missing values);] 

- HR: the heart rate measured upon arrival of hospital (1.62% missing values). 

26 

**Splitting strategy.** To study the coverage conditionally on the masks, we must handle the scarcity of some of them. For each individual in the data set, we make only one prediction, this way avoiding too many repetitions of the same test point when computing the average. We split the data set into 5 folds, and predict on each fold by training the procedure on the 4 others, with 15390 observations for training, and 7694 for calibration. 


![](markdown_output/conformal-missing-values-2023_images/conformal-missing-values-2023.pdf-0027-01.png)


**----- Start of picture text -----**<br>
QR<br>4 . 0 CQR<br>CQR-MDA-Exact<br>CQR-MDA-Nested<br>3 . 5<br>Marginal<br>3 . 0 Mask-type<br>2 . 5<br>2 . 0<br>1 . 5<br>1 . 0<br>0 . 90 0 . 92 0 . 94 0 . 96 0 . 98<br>Average coverage<br>length<br>Average<br>**----- End of picture text -----**<br>


Figure 15: Average coverage and length on the TraumaBase® data when predicting the platelets level. Colors correspond to the methods. Diamond (♦) corresponds to taking the average among all individuals. Other symbols correspond to computing the average among the individuals having a fixed mask. The vertical dotted line represents the target coverage of 90%. Model is NN. The mask is concatenated to the features. Imputation is Iterative Ridge. Each individual is predicted using 15390 observations for training, and 7694 for calibration. 

27 

