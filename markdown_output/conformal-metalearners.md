# **Conformal Meta-learners for Predictive Inference of Individual Treatment Effects** 

**Ahmed M. Alaa** UC Berkeley and UCSF `amalaa@berkeley.edu` 

**Zaid Ahmad Mark van der Laan** UC Berkeley UC Berkeley `zaidahmad@berkeley.edu laan@stat.berkeley.edu` 

## **Abstract** 

We investigate the problem of machine learning-based (ML) predictive inference on individual treatment effects (ITEs). Previous work has focused primarily on developing ML-based “meta-learners” that can provide point estimates of the conditional average treatment effect (CATE)—these are model-agnostic approaches for combining intermediate nuisance estimates to produce estimates of CATE. In this paper, we develop _conformal meta-learners_ , a general framework for issuing predictive intervals for ITEs by applying the standard conformal prediction (CP) procedure on top of CATE meta-learners. We focus on a broad class of meta-learners based on two-stage pseudo-outcome regression and develop a _stochastic ordering_ framework to study their validity. We show that inference with conformal meta-learners is marginally valid if their (pseudo-outcome) conformity scores stochastically dominate “oracle” conformity scores evaluated on the unobserved ITEs. Additionally, we prove that commonly used CATE meta-learners, such as the _doubly-robust_ learner, satisfy a model- and distribution-free stochastic (or convex) dominance condition, making their conformal inferences valid for practically-relevant levels of target coverage. Whereas existing procedures conduct inference on nuisance parameters (i.e., potential outcomes) via weighted CP [1], conformal meta-learners enable direct inference on the target parameter (ITE). Numerical experiments show that conformal meta-learners provide valid intervals with competitive efficiency while retaining the favorable point estimation properties of CATE meta-learners. 

## **1 Introduction** 

Identifying heterogeneity in the effects of interventions across individual subjects is a central problem in various fields, including medical, political, and social sciences [2, 3, 4]. In recent years, there has been growing interest in the development of machine learning (ML) models that can estimate heterogeneous treatment effects using observational or experimental data [5, 6, 7, 8, 9]. However, most of these models only provide _point_ estimates of the conditional average treatment effect (CATE), which is a deterministic function that describes the expected treatment effect based on a given individual’s covariates. In this paper, we focus on quantifying uncertainty in these estimates, which arises from both errors in the model and the variation of individual treatment effects (ITEs) for individuals with the same covariates. We adopt a _predictive inference_ approach to this problem, with the goal of devising valid procedures to issue predictive intervals that cover ITEs on unseen data with a predetermined probability. 

Traditionally, predictive inference on ITEs has been conducted through Bayesian methods such as BART [8] and Gaussian processes [9]. These methods can provide interval-valued predictions of ITEs through their induced posterior distributions (e.g., posterior credible intervals). However, Bayesian methods tend to be model-specific and cannot be straightforwardly generalized to modern ML models, e.g., transformer-based architectures used to model visual and textual covariate spaces [10]. More importantly, Bayesian methods generally do not provide guarantees on the frequentist coverage of 

* Equal contribution. 

their credible intervals—achieved (finite-sample) coverage depends on the prior [11]. This paper is motivated by the advent of _conformal prediction_ (CP), a frequentist alternative that can be used to conduct model-agnostic, distribution-free valid predictive inference on top of any ML model [12, 13, 14]. Throughout this paper, we will study the validity of CP-based procedures for inference of ITEs. 

_**What makes CP-based inference of ITEs different from its application to the standard regression (supervised) setup?**_ The “fundamental problem of causal inference” is that we never observe counterfactual outcomes [15]. That is, our “label” is the ITE which is a difference between two potential outcomes (treated and untreated) for an individual subject—this label is never observed for any given subject because we only ever observe factual outcomes. This poses two challenges [16]: 

_**(1) Covariate shift.**_ When treatments are assigned to individual subjects with probabilities that depend on their covariates, then the distributions of covariates in treated and untreated groups differ. Consequently, the distribution of training data differs from that of the target population. 

_**(2) Inductive biases.**_ Unlike supervised learning wherein we fit a single function using examples of covariates and _observed_ targets, models of treatment effects cannot be directly fit to the _unobserved_ effects. Thus, estimates of treatment effects comprise intermediate estimates of nuisance parameters, i.e., potential outcomes and treatment probabilities. Different approaches for producing and combining nuisance estimates represent an additional design dimension for modeling treatment effects. 

The literature on ML-based CATE estimation focuses on addressing the two challenges above. **Covariate shift** affects the generalization performance of ML models—existing CATE estimation models address this problem using importance weighting [17] or balanced representation learning methods for unsupervised domain adaptation [6, 18, 19]. In [5], the notion of “meta-learners” was coined to describe various model-agnostic approaches to incorporating **inductive biases** and combining nuisance estimates. In [5, 20], it was shown that the choice of the meta-learner influences the CATE estimation rates. While the impact of **(1)** and **(2)** on the generalization performance of CATE estimators has been extensively investigated, their impact on the validity and efficiency of predictive inference methods for ITE is less well-understood, and this forms the central theme of the paper. 

**Contributions.** We propose a CP procedure for predictive inference of ITEs that jointly addresses **(1)** and **(2)** in an end-to-end fashion. Our proposed inference strategy applies the standard CP procedure on top of a broad class of CATE meta-learners based on two-stage _pseudo-outcome_ regression. These meta-learners operate by first estimating pseudo-outcomes, i.e., transformed targets that depend on observable variables only, and then regressing the pseudo-outcomes on covariates to obtain point estimates of CATE. We then construct intervals for ITEs by computing the empirical quantile of conformity scores evaluated on pseudo-outcomes in a held-out calibration set. Conformal metalearners address **(1)** because the distribution of covariates associated with pseudo-outcomes is the same for training and testing data, and they address **(2)** since the calibration step is decoupled from model architecture, enabling flexible choice of inductive priors and the possibility of re-purposing existing meta-learners and architectures that have been shown to provide accurate estimates of CATE. 

Conformal meta-learners inherit the guarantees of CP, i.e., their resulting intervals cover pseudooutcomes on test data with high probability. However, the original CP guarantees do not immediately translate to guarantees on coverage of ITEs. To this end, we develop a unified _stochastic ordering_ framework to study the validity of conformal meta-learners for inference on ITEs. We show that inference with conformal meta-learners is valid if their conformity scores satisfy certain stochastic ordering conditions with respect to “oracle” conformity scores evaluated on unobserved ITEs. We prove that some of the commonly used meta-learners, such as the _doubly-robust_ learner [20], satisfy a weaker stochastic (or convex) dominance condition which makes them valid for relevant levels of target coverage. Our numerical experiments show that, with careful choice of the pseudo-outcome transformation, conformal meta-learners inherit both the coverage properties of CP as well as the efficiency and point estimation accuracy of their underlying CATE meta-learners. 

## **2 Predictive Inference of Individual Treatment Effects (ITEs)** 

## **2.1 Problem setup** 

We consider the standard potential outcomes (PO) framework with a binary treatment ([21, 22]). Let _W ∈{_ 0 _,_ 1 _}_ be the treatment indicator, _X ∈X_ be the covariates, and _Y ∈_ R be the outcome of interest. For each subject _i_ , let ( _Yi_ (0) _, Yi_ (1)) be the pair of potential outcomes under _W_ = 0 and _W_ = 1, 

2 

respectively. The fundamental problem of causal inference is that we can only observe the _factual_ outcome, i.e., the outcome _Yi_ = _WiYi_ (1) + (1 _− Wi_ ) _Yi_ (0) determined by _Wi_ , but we cannot observe the _counterfactual Yi_ (1 _− Wi_ ). For _n_ subjects, we assume that the data generation process 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0003-01.png)


satisfies the following assumptions: _(1) Unconfoundedness:_ ( _Y_ (0) _, Y_ (1)) _⊥ W | X_ , _(2) Consistency: Y_ = _Y_ ( _W_ ), and _(3) Positivity:_ 0 _< P_ ( _W_ = 1 _| X_ = _x_ ) _<_ 1 _, ∀x ∈X_ . These assumptions are necessary for identifying the causal effects of the treatment from a dataset _{Zi_ = ( _Xi, Wi, Yi_ ) _}[n] i_ =1[.] The causal effect of the treatment on individual _i_ , known as the _individual treatment effect_ (ITE), is defined as the difference between the two potential outcomes, i.e., _Yi_ (1) _− Yi_ (0). 

Previous modeling efforts (e.g., [5, 6, 7, 8]) have focused primarily on the (deterministic) _conditional average treatment effect_ (CATE), i.e., _τ_ ( _x_ ) ≜ E[ _Y_ (1) _− Y_ (0) _| X_ = _x_ ]. In this paper, we focus on the (random) ITE as the inferential target of interest. That is, our goal is to infer the ITE for a given subject _j_ given their covariate _Xj_ and the observed sample _{Zi_ = ( _Xi, Wi, Yi_ ) _}i_ =1. 

The distribution of the observed variable _Z_ = ( _X, W, Y_ ) is indexed by the covariate distribution _PX_ , as well as the nuisance functions _π_ ( _x_ ), _µ_ 0( _x_ ) and _µ_ 1( _x_ ) defined as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0003-05.png)


The function _π_ ( _x_ ) is known as the _propensity score_ and it captures the treatment mechanism underlying the data generation process. Throughout this paper, we assume that _π_ ( _x_ ) is known, i.e., data is drawn from an experimental study or the treatment assignment mechanism is known. 

**Predictive Inference of ITEs.** Given the sample _{Zi_ = ( _Xi, Wi, Yi_ ) _}[n] i_ =1[, our goal is to infer the ITE] for a new individual _n_ + 1 with covariate _Xn_ +1. In particular, we would like to construct a predictive band _C_[�] ( _x_ ) that covers the true ITE for new test points with high probability, i.e., 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0003-08.png)


for a predetermined target coverage of 1 _−α_ , with _α ∈_ (0 _,_ 1), where the probability in (3) accounts for the randomness of the training data _{Zi}i_ and the test point ( _Xn_ +1 _, Yn_ +1(1) _− Yn_ +1(0)). Predictive intervals that satisfy the coverage condition in (3) are said to be _marginally valid_ . 

## **2.2 Conformal prediction** 

Conformal prediction (CP) is a model- and distribution-free framework for predictive inference that provides (finite-sample) marginal coverage guarantees. In what follows, we describe a variant of CP, known as _split_ (or _inductive_ ) CP [12, 13, 14], for the standard regression setup. Given a training dataset _D_ set= _{ {_ ( _X_ ( _Xj, Yi, Yj_ ) : _i_ ) _j}i_ , the CP procedure starts by splitting _∈Dt}_ , and a _calibration_ set _{_ ( _Xk, Y Dk_ ) : into two disjoint subsets: _k ∈Dc}_ . Then, an ML modela proper training _µ_ �( _x_ ) is fit using the samples in _Dt_ and a _conformity score V_ ( _._ ) is evaluated for all samples in _Dc_ as follows: 

_Vk_ ( _µ_ �) ≜ _V_ ( _Xk, Yk_ ; � _µ_ ) _, ∀k ∈Dc._ (4) 

The conformity score measures how unusual the prediction looks relative to previous examples. A common choice of _V_ ( _._ ) is the absolute residual, i.e., _V_ ( _x, y_ ; � _µ_ ) ≜ _|_ � _µ_ ( _x_ ) _− y |_ . For a target coverage level of 1 _− α_ , we then compute a quantile of the empirical distribution of conformity scores, i.e., 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0003-14.png)



![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0003-15.png)



![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0003-16.png)


The interval in (6) is guaranteed to satisfy marginal coverage, i.e., P( _Yn_ +1 _∈ C_[�] ( _Xn_ +1)) _≥_ 1 _−α_ . The only assumption needed for this condition to hold is the _exchangeability_ between calibration and test data [12, 23, 24]. Note that the interval in (6) has a fixed length of 2 _QV_ (1 _−α_ ) that is independent of _x_ . To enable adaptive intervals, [25] proposed a variant of the CP procedure where the base model is a quantile regression with interval-valued predictions [ _µ_ � _α/_ 2( _x_ ) _,_ � _µ_ 1 _−α/_ 2( _x_ )], and the conformity score is defined as the signed distance _Vk_ ( _µ_ �) ≜ max _{µ_ � _α/_ 2( _Xk_ ) _− Yk, Yk − µ_ �1 _−α/_ 2( _Xk_ ) _}_ . 

3 

## **2.3 Oracle conformal prediction of ITEs** 

How can we adapt the CP framework for predictive inference of ITEs? In a hypothetical world where we have access to counterfactual outcomes, we can apply the standard CP in Section 2.2 to a dataset of covariates and ITE tuples, _D[∗]_ = _{_ ( _Xi, Yi_ (1) _− Yi_ (0)) _}i_ , and compute conformity scores as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0004-02.png)


where � _τ_ is an ML model fit to estimate the CATE function _τ_ ( _x_ ) using _Dt[∗]_[, and] _[ D][∗]_[=] _[ D] t[∗][∪D] c[∗]_[. We will] refer to this procedure as “oracle” conformal prediction and to _Vk[∗]_[(] _[τ]_[�][)][ as the oracle conformity scores.] Since the oracle problem is a standard regression, the oracle procedure is marginally valid—i.e., it satisfies the guarantee in (3), P( _Y_ (1) _− Y_ (0) _∈ C_[�] _[∗]_ ( _X_ )) _≥_ 1 _− α_ . However, oracle CP is infeasible since we can only observe one of the potential outcomes (colored in red and blue in (7)), hence we need an alternative procedure that operates only on the observed variable _Z_ = ( _X, W, Y_ ). 

## **2.4 The two challenges of predictive inference on ITEs** 

A naïve approach to inference of ITEs is to split the observed sample _{Zi_ = ( _Xi, Wi, Yi_ ) _}i_ by the treatment group and create two datasets: _D_ 0 = _{_ ( _Xi, Yi_ ) : _Wi_ = 0 _}i_ , _D_ 1 = _{_ ( _Xi, Yi_ ) : _Wi_ = 1 _}i_ , then generate two sets of conformity scores for the nuisance estimates _µ_ �0 and _µ_ �1 as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0004-06.png)


where _Dc,_ 0 and _Dc,_ 1 are calibration subsets of _D_ 0 and _D_ 1. In order to construct valid predictive intervals for ITE using the conformity scores in (8), we need to reconsider how the two distinct characteristics of CATE estimation, previously discussed in Section 1, interact with the CP procedure: 

## _**(1) Covariate shift**_ 

The distributions of covariates for treated and untreated subjects differ from that of the target population: _PX|W_ =0 = _PX|W_ =1 = _PX_ , i.e., the following holds for the conformity scores in (8): 

_PX,V_ (0) _|W_ =0 = _PX,V_ (0) _PX,V_ (1) _|W_ =1 = _PX,V_ (1) 

## _**(2) Inductive biases**_ 

Different choices for the joint model of _µ_ 0 and _µ_ 1 encode different inductive biases that impose different forms of regularization on the implied � � � CATE function, i.e., _τ_ ( _x_ ) = _µ_ 1( _x_ ) _− µ_ 0( _x_ ) [5]. These biases influence the induced distributions _PV_ (0) and _PV_ (1) of the conformity scores in (8). 

Covariate shift breaks the exchangeability assumption necessary for the validity of CP. Current methods have primarily focused on **(1)** with _Y_ (0) and _Y_ (1) as inference targets, and developed approaches for handling covariate shift by reweighting conformity scores [1, 26]. The resulting intervals for POs are then combined to produce intervals for ITEs. However, these method tie the CP procedure to model architecture, requiring inference on nuisance parameters, and hence lose the desirable post-hoc nature of CP. Furthermore, inference on POs is likely to provide conservative ITE intervals, and limits the inductive priors that can be assumed since not all CATE models provide explicit PO estimates. 

## **3 Conformal Meta-learners** 

In [5], a taxonomy of “meta-learners” was introduced to categorize different inductive priors that can be incorporated into CATE estimators by structuring the regression models for _µ_ 0 and _µ_ 1. For example, the _T-learner_ estimates _µ_ �0 and _µ_ �1 independently using _D_ 0 and _D_ 1, while the _S-learner_ models the treatment variable� _W_ as an additional covariate in a joint regression model� _µ_ �( _X, W_ ) and estimates CATE as � _τ_ ( _x_ ) = _µ_ ( _x,_ 1) _−µ_ ( _x,_ 0). In this Section, we propose an end-to-end solution to **(1)** and **(2)** by applying CP on top of CATE meta-learners in a post-hoc fashion, thereby decoupling the CP procedure from the CATE model and allowing direct inference on ITEs. In the next Section, we develop a unified framework for analyzing the validity of this broad class of procedures. 

## **3.1 Pseudo-outcome regression for CATE estimation** 

We focus on a broad subclass of CATE meta-learners based on two-stage _pseudo-outcome_ regression. These models replace the (unobserved) oracle ITEs with “proximal” targets that are estimated from observed variables only, and then train an ML model to predict the estimated targets from covariates. The two stages of this general pseudo-outcome regression framework can be described as follows: 

4 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0005-00.png)


**----- Start of picture text -----**<br>
(a) Pseudo-outcome regression for CATE (b) Conformal pseudo-intervals for ITE Algorithm 1: Conformal Meta-learner<br>b Conformity scores<br>µ 0 Input : = { ( Xi, Wi, Yi ) } [n] i =1 [,] [X][n] [+1]<br>X estimatorNuisance  b PV' //Si hh» mL.:tee Output : C � φ ( Xn +1)<br>µ 1 H: 1 Split D into Dφ, Dt and Dc ;<br>4tKeee!i Y e ' =  f ( Z ’ ;  ⇡,  b µ 0 ,  b µ 1) yyool¢-+; PV ⇤ os, Q Oracle scores V' (1  − ↵ ) 234 (2)Pseudo-outcome regression:(1)  Regress Estimate Y [�] φ � == ( fπ, ( Z,  �0� , ) � on1) using X using DφD ; t ;<br>CATE estimator b 5 Conformal pseudo-intervals:<br>X ⌧ b = E[ Y [e] ' | X =  x ] > ⌧ <OQOCDO-COCOA, by H 6 Evaluate conformity scores  Vφ  using  Dc ;<br>QV ⇤ (1  − ↵ ) 7 Return C [�] φ = [�( Xn +1)  ± QVφ (1  − α )]<br>**----- End of picture text -----**<br>


Figure 1: Pictorial depiction of conformal meta-learners. 

**Stage 1.** We obtain a plug-in estimate � of the nuisance parameters _φ_ = ( _π, µ_ 0 _, µ_ 1). Note that since we assume that the propensity score is known, we only need to estimate _µ_ 0 and _µ_ 1 using _D_ 0 and _D_ 1. 

**Stage 2.** We use the nuisance estimates obtained in Stage 1 to create pseudo-outcomes _Y_[�] _φ_ that depend � � only on and the observable variables _Z_ = ( _X, W, Y_ ), i.e., _Y_[�] _φ_ = _f_ ( _Z,_ ) for some function _f_ . The CATE estimate is then obtained by regressing the pseudo-outcome _Y_[�] _φ_ on the covariate _X_ . This is typically conducted using a different dataset than the one used to obtain the nuisance estimate � 

The general framework de- **Pseudo-outcome** scribed above captures various models in previous liter- _IPW-learner_ [27] _Y_[�] _φ_ = _π_ ( _XW_ )(1 _−π−_ ( _πX_ ( _X_ ) )) _[Y]_ ature.of suchWe study 3 examplesmeta-learners: X- _X-learner_ [5] _Y_[�] _φ_ = _W_ ( _Y −_ �0( _X_ )) + (1 _− W_ )(�1( _X_ ) _− Y_ ) learner, Inverse propensity _DR-learner_ [20] _Y_[�] _φ_ = _π_ ( _XW_ )(1 _−π−_ ( _πX_ ( _X_ ) ))[(] _[Y][−]_[�] _[W]_[ (] _[X]_[)) +][ �][1][(] _[X]_[)] _[ −]_[�][0][(] _[X]_[)] weighted (IPW) learner and doubly-robust (DR) learner. Table 1: 

Table 1: Existing meta-learners as instantiations of pseudo-outcome regression. 

Table 1 lists the pseudo-outcomes _Y_[�] _φ_ for the three meta-learners: IPW-learner reweights factual outcomes using propensity scores to match CATE, i.e., E[ _Y_[�] _φ | X_ = _x_ ] = _τ_ ( _x_ ); X-learner uses regression adjustment to impute counterfactuals; DR-learner combines both approaches. DR- and X-learners[1] , coupled with specific architectures for joint modeling of �0 and �1, have shown competitive performance for CATE estimation in previous studies [5, 16, 20]. The conformal meta-learner framework decouples the CP procedure (Section 3.2) from the inductive priors encoded by these meta-learners, hence it inherits their favorable CATE estimation properties and enables a potentially more efficient direct inference on ITEs as opposed to inference on POs. This addresses **challenge (2)** in Section 2.4. 

## **3.2 Conformal pseudo-intervals for ITEs** 

Pseudo-outcome regression is based on the notion that accurate proxies for treatment effects can produce reliable CATE point estimates. This concept can be extended to predictive inference: using CP to calibrate meta-learners via held-out pseudo-outcomes can yield accurate “pseudo-intervals” for ITEs. 

Given a dataset _D_ = _{Zi_ = ( _Xi, Wi, Yi_ ) _}i_ , we create three mutually-exclusive subsets: _Dφ_ , _Dt_ and _Dc_ . _Dφ_ is used to estimate the nuisance parameters _φ_ . Next, the estimates � = ( _π,_ 0 _[,]_[ �] 1[)][ are used to trans-] form _{Zi_ = ( _Xi, Wi, Yi_ ) : _i ∈Dt}_ into covariate/pseudo-outcome pairs _{_ ( _Xi, Y_[�] _φ,i_ ) : _i ∈Dt}_ which are used to train a CATE model � A Finally, we compute conformity scores for � A on pseudo-outcomes, i.e., _Vφ,k_ ( ) ≜ _V_ ( _Xk, Yφ,k_ ; ) _, ∀k ∈Dc._ (9) 

For a target coverage of 1 _− α_ , we construct a predictive interval at a new point _Xn_ +1 = _x_ as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0005-11.png)


where _Vφ_ = _{Vφ,k_ ( ) : _k ∈Dc}_ . We call _Cφ_ ( _x_ ) a _pseudo-interval_ . The conformal meta-learner approach is depicted in Figure 1 and a summary of the procedure is given in Algorithm 1. 

1Here, we consider a special case of the X-learner in [5] which involves a weighted sum of two regression adjusted models � and � trained separately on the treated and control datasets _D_ 0 and _D_ 1. 

5 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0006-00.png)


**----- Start of picture text -----**<br>
(a) First-order stochastic dominance (b) Second-order stochastic dominance<br>**----- End of picture text -----**<br>


Figure 2: Graphical illustration of stochastic dominance among two exemplary distributions _F_ and _G_ . 

Note that conditional on the pseudo-outcomes ( _X, Y_[�] _φ_ ) in calibration data are drawn from the target distribution, which maintains the exchangeability of conformity scores and addresses covariate shift ( **challenge (1)** in Section 2.4). However, the conformity scores _V φ_ are evaluated on transformed outcomes, which means that _Vφ_ and _V[∗]_ are not exchangeable, even though they are drawn from the same covariate distribution. Consequently, the usual CP guarantees, i.e., P( _Y_[�] _φ ∈ C_[�] _φ_ ( _X_ )) _≥_ 1 _− α_ , do not immediately translate to coverage guarantees for the true ITE _Y_ (1) _− Y_ (0). In the next section, we show that for certain choices of the pseudo-outcomes, the corresponding pseudo-intervals can provide valid inferences for ITE without requiring the exchangeability of _Vφ_ and _V[∗]_ . 

## **4 Validity of Conformal Meta-learners: A Stochastic Ordering Framework** 

Under what conditions are pseudo-intervals valid for inference of ITEs? Recall that these intervals are constructed by evaluating the empirical quantile of pseudo-outcome conformity scores. Intuitively, the pseudo-intervals will cover the true ITE if the conformity scores are “stochastically larger” than the oracle scores in Section 2.3, i.e., _QVφ_ ( _α_ ) _≥ QV ∗_ ( _α_ ) in some stochastic sense (Figure 1(b)). Hence, to study the validity of conformal meta-learners, we analyze the _stochastic orders_ of _Vφ_ and _V[∗]_ , and identify conditions under which pseudo-intervals cover oracle intervals. 

Stochastic orders are partial orders of random variables used to compare their location, magnitude, or variability [28, 29]. In our analysis, we utilize two key notions of stochastic order among cumulative distribution functions (CDFs) _F_ and _G_ , which we formally define below. 

**Definition 1 (Stochastic dominance)** _F_ has _first-order_ stochastic dominance (FOSD) on _G_ , _F ⪰_ (1) _G_ , iff _F_ ( _x_ ) _≤ G_ ( _x_ ) _, ∀x_ , with strict inequality for some _x_ . _F_ has _second-order_ stochastic dominance (SOSD) over _G_ , _F ⪰_ (2) _G_ , iff J _−∞x_[[] _[G]_[(] _[t]_[)] _[ −][F]_[(] _[t]_[)]] _[ dt][ ≥]_[0][,] _[ ∀][x]_[, with strict inequality for some] _[ x]_[.] 

**Definition 2 (Convex dominance)** _F_ has monotone _convex_ dominance (MCX) over _G_ , _F ⪰mcx G_ , iff E _X∼F_ [ _u_ ( _X_ )] _≥_ E _X∼G_ [ _u_ ( _X_ )] for all non-decreasing convex functions _u_ : R _→_ R. 

Stochastic ordering is useful tool in decision theory and quantitative finance used to analyze the decisions of utility maximizers with varying risk attitudes [30]. A distribution _F_ has FOSD over _G_ if it is favored by any decision-maker with a non-decreasing utility function, i.e., _F_ is more likely to give higher outcomes than _G_ because its CDF is strictly lower (Figure 2(a)). If _F_ has SOSD over _G_ , then it is favored by risk-averse decision-makers, i.e., _f_ has smaller spread than _g_ and is favored by all decision-makers with a non-decreasing _concave_ utility function [31]. In this case, the CDFs can cross but _G_ is always lower after the last crossing point (Figure 2(b)). _F_ has MCX over _G_ if it is favored by decision-makers with a non-decreasing _convex_ utility—in this case, the CDFs can cross but _F_ is always lower after the last crossing point (See Appendix A for a detailed analysis). 

In the following Theorem, we provide sufficient conditions for the validity of conformal meta-learners in terms of the stochastic orders of their conformity scores. 

**Theorem 1.** _If_ ( _Xi, Wi, Yi_ (0) _, Yi_ (1)) _, i_ = 1 _, . . . , n_ + 1 _are exchangeable, then ∃ α[∗] ∈_ (0 _,_ 1) _such that the pseudo-interval Cφ_ ( _Xn_ +1) _constructed using the dataset D_ = _{_ ( _Xi, Wi, Yi_ ) _}[n] i_ =1 _[satisfies]_ 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0006-11.png)


_if at least one of the following stochastic ordering conditions hold: (i) Vφ ⪰(1) V[∗] , (ii) Vφ ⪯(2) V[∗] , and (iii) Vφ ⪰mcx V[∗] . Under condition (i), we have α[∗]_ = 1 _._ 

All proofs are provided in Appendix A. Theorem 1 states that if the conformity score _Vφ_ of the metalearner is stochastically larger (FOSD) or has a larger spread (SOSD and MCX) than the oracle conformity score, then the conformal meta-learner is valid for high-probability coverage (Figure 3). (This is the range of target coverage that is of practical relevance, i.e., _α_ is typically set to 0.05 or 0.1.) 

6 

|Conformity score<br>_CDF_<br>**Validity region for**<br>**conformal meta-learners**<br>[oe-no<br>4<br>*<br>7<br>l-a<br>4<br>f<br>f<br>7’<br>Py<br>“<br>ey<br>v<br>et<br>Py«|_Target coverage_||**Meta-learner**<br>**Conformity score**<br>_Absolute residual_<br>_Signed distance_<br>_X-learner_<br>No stochastic order<br>No stochastic order<br>_IPW-learner_<br>_Vφ ⪰mcx V ∗_<br>_Vφ ⪯_(2) _V ∗_<br>_DR-learner_<br>_Vφ ⪰mcx V ∗_<br>_Vφ ⪯_(2) _V ∗_<br>Table 2: Stochastic orders of conformity scores for the three|
|---|---|---|---|
|Figure 3:Validity condition in Theorem 1.|Validity condition in Theorem 1.|Validity condition in Theorem 1.|meta-learners considered in Table 1.|



Figure 3: Validity condition in Theorem 1. 

Because stochastic (or convex) dominance pertain to more variable conformity scores, the predictive intervals of conformal meta-learners will naturally be more conservative than the oracle intervals. 

Whether a meta-learner meets conditions� � _(i)-(iii)_ of Theorem 1 depends on how the pseudo-outcome, _Yφ_ = _f_ ( _Z_ ; ), is constructed. The following Theorem provides an answer to the question of which of the meta-learners listed in Table 1 satisfy the stochastic ordering conditions in Theorem 1. 

**Theorem 2.** _Let Vφ_ ( ) = _|_ ( _X_ ) _− Yφ| and assume that the propensity score function π_ : _X →_ [0 _,_ 1] _is known. Then, the following holds: (i) For the X-learner, Vφ and V[∗] do not admit to a model- and distribution-free stochastic order, (ii) For any distribution P_ ( _X, W, Y_ (0) _, Y_ (1)) _, CATE estimate and nuisance estimate the IPW- and the DR-learners satisfy Vφ ⪰mcx V[∗] ._ 

Theorem 2 states that the stochastic ordering of _Vφ_ and _V[∗]_ depends on the specific choice of the conformity score function _V_ ( _X, Y_[�] _φ_ ; � A ) as well as the choice of the meta-learner, i.e., the pseudo-outcome � generation function _Y_[�] _φ_ = _f_ ( _Z_ ; ). The IPW- and DR-learners ensure that, by construction, the pseudooutcome is equal to CATE in expectation: E[ _Y_[�] _φ | X_ = _x_ ] = _τ_ ( _x_ ). This construction enables the IPWand DR-learners to provide unbiased estimates of average treatment effects (ATE) independent of the data distribution and the ML model used for the nuisance estimates �0 and �1. By the same logic, IPWand DR-learners also guarantee stochastic (convex) dominance of their conformity scores irrespective of the data distribution and the ML model choice, hence preserving the model- and distribution-free nature of the CP coverage guarantees. Contrarily, the X-learner does not use the knowledge of _π_ to construct its pseudo-outcomes, hence it does not guarantee a (distribution-free) stochastic order and the achieved coverage depends on the nuisance estimates �0 and �1. In Table 2, we list the stochastic orders achieved for different choices of meta-learners and conformity scores. (The analysis of stochastic orders for the signed distance score used in [25] and [32] is provided in Appendix A.) 

**Key limitations of conformal meta-learners.** While conformalized meta-learners can enable valid end-to-end predictive inference of ITEs, they have two key limitations. First, the propensity score _π_ must be known to guarantee model- and distribution-free stochastic ordering of conformity scores. However, we note that this limitation in not unique to our method and is also encountered in methods based on weighted CP [1, 26]. The second limitation is peculiar to our method: exact characterization of _α[∗]_ is difficult and depends on the data distribution. Devising procedures for inferring _α[∗]_ based on observable variables or deriving theoretical upper bounds on _α[∗]_ are interesting directions for future work. Here, we focus on empirical evaluation of _α[∗]_ in semi-synthetic experiments. A detailed comparison between our method and previous work is provided in Appendix B. 

## **5 Experiments** 

## **5.1 Experimental setup** 

Since the true ITEs are never observed in real-world datasets, we follow the common practice of conducting numerical experiments using synthetic and semi-synthetic datasets [1, 8, 19]. We present a number of representative experiments in this Section and defer further results to Appendix C. 

**Synthetic datasets.** We consider a variant of the data-generation process in Section 3.6 in [1] which was originally proposed in [7]. We create synthetic datasets by sampling covariates _X ∼ U_ ([0 _,_ 1] _[d]_ ) and treatments _W |X_ = _x ∼_ Bern( _π_ ( _x_ )) with _π_ ( _x_ ) = (1 + _Ix_ (2 _,_ 4)) _/_ 4, where _Ix_ (2 _,_ 4) is the regularized incomplete beta function (i.e., CDF of a Beta distribution with shape parameters 2 and 4). Outcomes are modeled as _µ_ 1( _x_ ) = _ζ_ ( _x_ 1) _· ζ_ ( _x_ 2) and _µ_ 0( _x_ ) = _γ ζ_ ( _x_ 1) _· ζ_ ( _x_ 2), where _γ ∈_ [0 _,_ 1] is a parameter that controls the treatment effect, and _ζ_ is a function given by _ζ_ ( _x_ ) = 1 _/_ (1 + exp( _−_ 12( _x −_ 0 _._ 5))). 

7 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0008-00.png)


**----- Start of picture text -----**<br>
(a) Empirical assessment of stochastic orders (b) Coverage, efficiency and RMSE for  Setup A  (top) and  Setup B  (bottom)<br>DR-learner IPW-learner X-learner<br>Inexact<br>WCP<br>Exact CM<br>°° -25 0.0 25 -5 0 0 2 Naive $ HH: HH<br>X<br>IPW<br>0.50.0 Y é HEH} | HE}<br>DR<br>-5 0 “5 Conformity score 0 -2 0 2 4 HH [I .<br>(c) Performance at different levels of target coverage 0.0 0.5 1.0 0 5 10 15 0.0 0.5<br>Inexact<br>Empirical coverage Avg. interval length RMSE<br>10 eaterangesTra“ls §Mi,) "06 7°CrsS$r0.6Stee9. NaiveExact || HEH' Hi Han . [2 }<br>X<br><aay 1. : =oe, eh te mon<br>IPW<br>DR<br>oor 0.5 1° Os ee 0.5 1.0 0.0 0.5 1.0 0 5 10 15 14<br>Target coverage Empirical coverage (⍺=0.9)  Interval Length RMSE<br>(Setup A)<br>CDF<br>(Setup B)<br>CDF<br>Setup A<br>Setup B<br>**----- End of picture text -----**<br>


Figure 4: Performance of all baseline in the synthetic setup described in Section 5.1. In (b), red vertical lines correspond to target coverage (1 _− α_ = 0 _._ 9), and blue vertical lines correspond to optimal interval width. In (c), baseline methods are color-coded as follows: _•_ CM-DR, _•_ CM-IPW, _•_ CM-X, _•_ WCP-Naïve, _•_ WCP-Exact, and _•_ WCP-Inexact. Here, WCP stands for weighted CP and CM stands for conformal meta-learners. 

We assume that POs are sampled from _Y_ ( _w_ ) _|X_ = _x ∼N_ ( _µw_ ( _x_ ) _, σ_[2] ( _x_ )) _, w ∈{_ 0 _,_ 1 _}_ and consider a heteroscedastic noise model _σ_[2] ( _x_ ) = _−_ log( _x_ 1). We define two setups within this model: **Setup A** where the treatment has not effect ( _ζ_ = 1), and **Setup B** where the effects are heterogeneous ( _ζ_ = 0). 

**Semi-synthetic datasets.** We also consider two well-known semi-synthetic datasets that involve real covariates and simulated outcomes. The first is the National Study of Learning Mindsets (NLSM) [3], and the second is the IHDP benchmark originally developed in [8]. Details on the data generation process for NLSM can be founded in Section 2 in [33]. Details on the IHDP benchmark can be found in [6, 8, 16, 19]. Appendix C provides detailed description of both datasets for completeness. 

**Baselines.** We consider baseline models that provide valid predictive intervals for ITEs. Specifically, we consider state-of-the-art methods based on weighted conformal prediction (WCP) proposed in [1]. These methods apply weighted CP to construct intervals for the two POs or plug-in estimates of ITEs. We consider the three variants of WCP in [1]: (1) _Naïve WCP_ which combines the PO intervals using Bonferroni correction, (2) _Exact Nested WCP_ which applies WCP to plug-in estimates of ITEs in treatment and control groups followed by a secondary CP procedure, and (3) _Inexact Nested WCP_ which follows the same steps of the exact version but replaces the secondary CP with conditional quantile regression. (Note that Inexact Nested WCP does not provide coverage guarantees.) For all baselines, we use the same model (Gradient Boosting) for nuisance and pseudo-outcome modeling, and we use the conformal quantile regression method in [25] to construct predictive intervals. 

## **5.2 Results and discussion** 

Our experimental findings yield the following key takeaways: Firstly, the _IPW- and DR-learners demonstrate a robust FOSD (i.e., α[∗]_ = 1 _) in the majority of experiments, surpassing the MCX conditions outlined in Theorem 2_ . Secondly, _the DR-learner exhibits superior point estimation accuracy and interval efficiency in most experiment_ compared to all other baselines that ensure valid inference. Thirdly, the _effectiveness of conformal meta-learners depends on the discrepancy between the CDFs of conformity scores and oracle scores_ —pseudo-outcome transformations that induce thicker tails in the resulting conformtiy scores can cause conformal meta-learners to under-perform. 

**Empirical assessment of stochastic orders.** Figure 4(a) depicts the empirical CDF of the conformity scores _Vφ_ and oracle scores _V[∗]_ for the three meta-learners under study (DR-, IPW- and X-learners). These CDFs are averaged over 100 runs of **Setups A** and **B** of the synthetic generation process outlined in Section 5.1. (The shaded regions represent the lowest and highest bounds on the empirical 

8 

|Naïve<br>Exact|**Coverage**<br>0.89 (0.02)<br>0.99 (0.00)|**IHDP**<br>**Avg. len.**<br>18.9 (4.04)<br>29.8 (7.60)|**RMSE**<br>4.73 (1.00)<br>4.50 (0.97)|**Coverage**<br>0.99 (0.00)<br>0.99 (0.00)|**NLSM**<br>**Avg. len.**<br>4.82 (0.02)<br>4.92 (0.07)|**RMSE**<br>0.15 (0.00)<br>0.19 (0.01)|
|---|---|---|---|---|---|---|
|Inexact<br>X<br>IPW<br>DR|0.61 (0.04)<br>0.65 (0.04)<br>0.99 (0.00)<br>0.96 (0.01)|8.49 (1.36)<br>11.0 (3.04)<br>112 (23.0)<br>**16.7**(3.30)|4.61 (0.99)<br>**3.34**(0.56)<br>19.9 (3.44)<br>**3.32**(0.53)|0.96 (0.00)<br>0.27(0.00)<br>0.99 (0.00)<br>0.99 (0.00)|**2.38**(0.01)<br>0.38 (0.00)<br>6.48 (0.07)<br>6.24 (0.07)|0.18 (0.00)<br>**0.14**(0.00)<br>0.61 (0.02)<br>0.37 (0.01)|



Table 3: Performance of all baselines in semi-synthetic datasets. Bold numbers correspond to best performance. 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0009-02.png)


**----- Start of picture text -----**<br>
DR-learner IPW-learner X-learner<br>Conformity score<br> (IHDP)<br>CDF<br> (NLSM)<br>CDF<br>**----- End of picture text -----**<br>


Figure 5: Stochastic orders in IHDP/NLSM. 

CDFs evaluated across all runs.) In both setups, the conformity scores for the DR- and IPW-learners demonstrate FOSD over the oracle scores with respect to the average CDFs and in almost all realizations. This aligns with the result of Theorem 2, and shows that the stochastic dominance condition achieved in practice is even stronger than our theoretical guarantee since FOSD ( _Vφ ⪰_ (1) _V[∗]_ ) implies the weaker conditions of _Vφ ⪯_ (2) _V[∗]_ and _Vφ ⪰mcx V[∗]_ . On the contrary, the conformity scores of the X-learner are dominated by oracle scores in the FOSD sense. This is not surprising in light of Theorem 2, which indicates that X-learners do not guarantee a distribution-free stochastic order. These observations are also replicated in the semi-synthetic datasets as shown in Figure 5. 

Based on Theorem 1, the empirical stochastic orders observed in Figures 4(a) and 5 predict that the IPW- and DR-learners will cover ITEs, whereas the X-learner will not achieve coverage. This is confirmed by the results in Figures 4(b), 4(c) and Table 3. The fact that the IPW- and DR-learners satisfy a stronger FOSD condition is promising because it indicates that the range of validity for these models spans all levels of coverage ( _α[∗]_ = 1 in Figure 3). It also means that a stronger version of Theorem 2 outlining the conditions under which IPW- and DR-learners achieve FOSD could be possible. 

**Coverage, efficiency and point estimation accuracy.** The performance of a predictive inference procedure can be characterized in terms of three metrics: achieved coverage for true ITEs, expected length of predictive intervals, and root-mean-square error (RMSE) in CATE estimates. In most experiments, we find that the DR-learner strikes a balance between these metrics (See Appendix C for further experiments). In Figure 4(b), we can see that the DR-learner outperforms the valid (naïve and exact) WCP procedures in terms of RMSE and interval length, while achiveing the target coverage of 90%. The X-learner outperforms all baselines in terms of RMSE, but as expected, it under-covers ITEs in all experiments. The inexact WCP baseline offers competitive efficiency and calibration, however, in addition to not offering coverage guarantees it also lacks consistency in RMSE performance under different inductive biases (i.e., no treatment effects in **Setup A** and heterogeneous effects in **Setup B** ). These performance trends hold true across all levels of target coverage as shown in Figure 4(c). 

The semi-synthetic experiments on IHDP and NLSM datasets shed light on when meta-learners may perform poorly. The DR-learner outperforms all baselines on the IHDP dataset in terms of RMSE, interval efficiency, while achieving the desired coverage of 90%. However, we observe that empirical performance depends on how closely the CDF of conformity scores matches the oracle CDF. The DRlearner performance deteriorates when conformity scores have “very strong” dominance over oracle scores, as observed in the NLSM dataset (Figure 5, bottom). Conversely, when the CDF of conformity scores is a closer lower bound on the oracle CDF, the DR-learner performance is competitive (Figure 4 and Figure 5, top). This is intuitive because if the pseudo-outcome transformation induces significant variability in regression targets, it will result in a lower CDF, poorer accuracy of pseudo-outcome regression, and longer predictive intervals. This is why the DR-learner consistently outperforms the IPW-learner, as it provides a closer approximation of the oracle CDF. Future work could focus on analyzing the gap between pseudo-outcome and oracle score CDFs and designing pseudo-outcome transformations that optimize efficiency while preserving stochastic orders. 

## **6 Conclusions** 

Estimation and inference of treatment effects is challenging because causal effects are not directly observable. In this paper, we developed a general framework for inference of treatment effects, dubbed conformal meta-learners, that is compatible with any machine learning model. Our framework inherits the model- and distribution-free validity of conformal prediction as well as the estimation accuracy of model-agnostic meta-learners of treatment effects. Additionally, we introduce a new theoretical framework based on stochastic ordering to assess the validity of our method, which can guide the development of new models optimized for both accurate estimation and valid inference. 

9 

## **References** 

- [1] Lihua Lei and Emmanuel J Candès. Conformal inference of counterfactuals and individual treatment effects. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ , 83(5):911–938, 2021. 

- [2] Kosuke Imai and Aaron Strauss. Estimation of heterogeneous treatment effects from randomized experiments, with application to the optimal planning of the get-out-the-vote campaign. _Political Analysis_ , 19(1):1–19, 2011. 

- [3] David S Yeager, Paul Hanselman, Gregory M Walton, Jared S Murray, Robert Crosnoe, Chandra Muller, Elizabeth Tipton, Barbara Schneider, Chris S Hulleman, Cintia P Hinojosa, et al. A national experiment reveals where a growth mindset improves achievement. _Nature_ , 573(7774):364–369, 2019. 

- [4] Sheldon Greenfield, Richard Kravitz, Naihua Duan, and Sherrie H Kaplan. Heterogeneity of treatment effects: implications for guidelines, payment, and quality assessment. _The American journal of medicine_ , 120(4):S3–S9, 2007. 

- [5] Sören R Künzel, Jasjeet S Sekhon, Peter J Bickel, and Bin Yu. Metalearners for estimating heterogeneous treatment effects using machine learning. _Proceedings of the national academy of sciences_ , 116(10):4156–4165, 2019. 

- [6] Uri Shalit, Fredrik D Johansson, and David Sontag. Estimating individual treatment effect: generalization bounds and algorithms. In _International Conference on Machine Learning_ , pages 3076–3085. PMLR, 2017. 

- [7] Stefan Wager and Susan Athey. Estimation and inference of heterogeneous treatment effects using random forests. _Journal of the American Statistical Association_ , 113(523):1228–1242, 2018. 

- [8] Jennifer L Hill. Bayesian nonparametric modeling for causal inference. _Journal of Computational and Graphical Statistics_ , 20(1):217–240, 2011. 

- [9] Ahmed M Alaa and Mihaela Van Der Schaar. Bayesian inference of individualized treatment effects using multi-task gaussian processes. _Advances in neural information processing systems_ , 30, 2017. 

- [10] Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh, and Kai-Wei Chang. Visualbert: A simple and performant baseline for vision and language. _arXiv preprint arXiv:1908.03557_ , 2019. 

- [11] Botond Szabó, Aad W Van Der Vaart, and JH Van Zanten. Frequentist coverage of adaptive nonparametric bayesian credible sets. _The Annals of Statistics_ , 2015. 

- [12] Volodya Vovk, Alexander Gammerman, and Craig Saunders. Machine-learning applications of algorithmic randomness. _International Conference on Machine Learning_ , 1999. 

- [13] Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. _Algorithmic learning in a random world_ . Springer Science & Business Media, 2005. 

- [14] Harris Papadopoulos. _Inductive conformal prediction: Theory and application to neural networks_ . INTECH Open Access Publisher Rijeka, 2008. 

- [15] Guido W Imbens and Donald B Rubin. _Causal inference in statistics, social, and biomedical sciences_ . Cambridge University Press, 2015. 

- [16] Alicia Curth and Mihaela van der Schaar. On inductive biases for heterogeneous treatment effect estimation. _Advances in Neural Information Processing Systems_ , 34:15883–15894, 2021. 

- [17] Hidetoshi Shimodaira. Improving predictive inference under covariate shift by weighting the log-likelihood function. _Journal of statistical planning and inference_ , 90(2):227–244, 2000. 

- [18] Yaroslav Ganin and Victor Lempitsky. Unsupervised domain adaptation by backpropagation. In _International conference on machine learning_ , pages 1180–1189. PMLR, 2015. 

- [19] Fredrik Johansson, Uri Shalit, and David Sontag. Learning representations for counterfactual inference. In _International conference on machine learning_ , pages 3020–3029. PMLR, 2016. 

- [20] Edward H Kennedy. Towards optimal doubly robust estimation of heterogeneous causal effects. _arXiv preprint arXiv:2004.14497_ , 2020. 

10 

- [21] Jerzy S Neyman. On the application of probability theory to agricultural experiments. essay on principles. section 9.(tlanslated and edited by dm dabrowska and tp speed, statistical science (1990), 5, 465-480). _Annals of Agricultural Sciences_ , 10:1–51, 1923. 

- [22] Donald B Rubin. [on the application of probability theory to agricultural experiments. essay on principles. section 9.] comment: Neyman (1923) and causal inference in experiments and observational studies. _Statistical Science_ , 5(4):472–480, 1990. 

- [23] Jing Lei, James Robins, and Larry Wasserman. Distribution-free prediction sets. _Journal of the American Statistical Association_ , 108(501):278–287, 2013. 

- [24] Jing Lei, Max G’Sell, Alessandro Rinaldo, Ryan J Tibshirani, and Larry Wasserman. Distribution-free predictive inference for regression. _Journal of the American Statistical Association_ , 113(523):1094–1111, 2018. 

- [25] Yaniv Romano, Evan Patterson, and Emmanuel Candes. Conformalized quantile regression. _Advances in Neural Information Processing Systems_ , 32:3543–3553, 2019. 

- [26] Ryan J Tibshirani, Rina Foygel Barber, Emmanuel J Candès, and Aaditya Ramdas. Conformal prediction under covariate shift. _arXiv preprint arXiv:1904.06019_ , 2019. 

- [27] Daniel G Horvitz and Donovan J Thompson. A generalization of sampling without replacement from a finite universe. _Journal of the American statistical Association_ , 47(260):663–685, 1952. 

- [28] Moshe Shaked and J George Shanthikumar. _Stochastic orders_ . Springer, 2007. 

- [29] Michael Rothschild and Joseph E Stiglitz. Increasing risk: I. a definition. In _Uncertainty in Economics_ , pages 99–121. Elsevier, 1978. 

- [30] Søren Asmussen and Mogens Steffensen. _Risk and insurance_ . Springer, 2020. 

- [31] Josef Hadar and William R Russell. Rules for ordering uncertain prospects. _The American economic review_ , 59(1):25–34, 1969. 

- [32] Henrik Linusson, Ulf Johansson, and Tuve Löfström. Signed-error conformal regression. In _Advances in Knowledge Discovery and Data Mining: 18th Pacific-Asia Conference, PAKDD 2014, Tainan, Taiwan, May 13-16, 2014. Proceedings, Part I 18_ , pages 224–236. Springer, 2014. 

- [33] Carlos Carvalho, Avi Feller, Jared Murray, Spencer Woody, and David Yeager. Assessing treatment effect variation in observational studies: Results from a data challenge. _Observational Studies_ , 5(2):21–35, 2019. 

- [34] Hugh A Chipman, Edward I George, and Robert E McCulloch. Bart: Bayesian additive regression trees. _The Annals of Applied Statistics_ , 4(1):266–298, 2010. 

- [35] P Richard Hahn, Jared S Murray, and Carlos M Carvalho. Bayesian regression tree models for causal inference: Regularization, confounding, and heterogeneous effects (with discussion). _Bayesian Analysis_ , 15(3):965–1056, 2020. 

- [36] Suzanne Sniekers and Aad van der Vaart. Adaptive bayesian credible sets in regression with a gaussian process prior. _Electronic Journal of Statistics_ , 9(2):2475–2527, 2015. 

- [37] Stefan Wager, Trevor Hastie, and Bradley Efron. Confidence intervals for random forests: The jackknife and the infinitesimal jackknife. _The Journal of Machine Learning Research_ , 15(1):1625–1651, 2014. 

- [38] Maggie Makar, Fredrik Johansson, John Guttag, and David Sontag. Estimation of bounds on potential outcomes for decision making. In _International Conference on Machine Learning_ , pages 6661–6671. PMLR, 2020. 

- [39] Ying Jin, Zhimei Ren, and Emmanuel J Candès. Sensitivity analysis of individual treatment effects: A robust conformal inference approach. _Proceedings of the National Academy of Sciences_ , 120(6):e2214889120, 2023. 

- [40] Mingzhang Yin, Claudia Shi, Yixin Wang, and David M Blei. Conformal sensitivity analysis for individual treatment effects. _Journal of the American Statistical Association_ , pages 1–14, 2022. 

- [41] Yingying Zhang, Chengchun Shi, and Shikai Luo. Conformal off-policy prediction. In _International Conference on Artificial Intelligence and Statistics_ , pages 2751–2768. PMLR, 2023. 

11 

- [42] Muhammad Faaiz Taufiq, Jean-Francois Ton, Rob Cornish, Yee Whye Teh, and Arnaud Doucet. Conformal off-policy prediction in contextual bandits. _arXiv preprint arXiv:2206.04405_ , 2022. 

- [43] Isaac Gibbs and Emmanuel Candes. Adaptive conformal inference under distribution shift. _Advances in Neural Information Processing Systems_ , 34:1660–1672, 2021. 

- [44] Rina Foygel Barber, Emmanuel J Candes, Aaditya Ramdas, and Ryan J Tibshirani. Conformal prediction beyond exchangeability. _arXiv preprint arXiv:2202.13415_ , 2022. 

- [45] Hongxiang Qiu, Edgar Dobriban, and Eric Tchetgen Tchetgen. Distribution-free prediction sets adaptive to unknown covariate shift. _arXiv preprint arXiv:2203.06126_ , 2022. 

- [46] Jeanne Brooks-Gunn, Fong-ruey Liaw, and Pamela Kato Klebanov. Effects of early intervention on cognitive function of low birth weight preterm infants. _The Journal of pediatrics_ , 120(3):350– 359, 1992. 

- [47] Vincent Dorie, Jennifer Hill, Uri Shalit, Marc Scott, and Dan Cervone. Automated versus do-it-yourself methods for causal inference: Lessons learned from a data analysis competition. _Statistical Science_ , 2019. 

12 

## **Appendix A: Technical Proofs** 

## **A.1. Equivalent Definitions for Stochastic Orders** 

The following section introduces alternative definitions for stochastic dominance between two cumulative distribution functions (CDFs), denoted as _F_ and _G_ . These definitions will be used in the proof for Theorem 2 (Section A.4.). Note that these definitions are equivalent to Definition 1 provided in the main text but are expressed in decision-theoretic terms. 

**Definition A1 (First-order stochastic dominance)** _F_ has _first-order_ stochastic dominance (FOSD) over _G_ , _F ⪰_ (1) _G_ , if and only if E _X∼F_ [ _u_ ( _X_ )] _≥_ E _X∼G_ [ _u_ ( _X_ )] for all non-decreasing (utility) functions _u_ : R _→_ R (Theorem 1.A.3 in [28] proves the equivalence of Definitions 1 and A1). 

**Definition A2 (Second-order stochastic dominance)** _F_ has _second-order_ stochastic dominance (SOSD) over _G_ , _F ⪰_ (2) _G_ , if and only if E _X∼F_ [ _u_ ( _X_ )] _≥_ E _X∼G_ [ _u_ ( _X_ )] for all non-decreasing concave functions _u_ : R _→_ R (Refer to Theorem 4.A.1 and Eq. (4.A.7) in [28]). 

In addition to the alternative definitions of FOSD and SOSD above, we also state the definitions for two additional notions of stochastic ordering that we will use in the proofs. 

**Definition A3 (Statewise stochastic dominance)** A random variable _X_ has _statewise_ stochastic dominance (SWD) over a random variable _Y_ , _X ⪰_ SWD _Y_ , if and only if _X ≥ Y_ for every draw of the bivariate random variable ( _X, Y_ ) _∼ PX,Y_ . Note that SWD implies FOSD. 

**Definition A4 (Convex dominance)** _F_ has _convex_ dominance (CX) over _G_ , _F ⪰_ cx _G_ , if and only if E _X∼F_ [ _u_ ( _X_ )] _≥_ E _X∼G_ [ _u_ ( _X_ )] for all convex functions _u_ : R _→_ R. 

## **A.2. Useful Lemmas** 

**Lemma A1. (Pointwise and marginal stochastic orders)** _For random variables X, Y , and Z, the following conditions hold for any marginal distribution PX :_ 

_(i) Y | X_ = _x ⪰(1) Z | X_ = _x, ∀x ∈X ⇒ Y ⪰(1) Z, (ii) Y | X_ = _x ⪰(2) Z | X_ = _x, ∀x ∈X ⇒ Y ⪰(2) Z, (iii) Y | X_ = _x ⪰mcx Z | X_ = _x, ∀x ∈X ⇒ Y ⪰mcx Z._ 

_Proof._ Recall from the definition of FOSD (Definition A1) that if _Y | X_ = _x ⪰_ (1) _Z | X_ = _x_ , then: 

E _V ∼PY |X_ = _x_ [ _u_ ( _V_ )] _≥_ E _W ∼PZ|X_ = _x_ [ _u_ ( _W_ )] _,_ (A.1) 

for all non-decreasing functions _u_ : R _→_ R. Since expectation is a positive linear operator, marginalizing both sides with respect to the density _PX_ preserves the inequality in (A.1): 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0013-14.png)


which recovers the definition of FOSD between random variables _Y_ and _Z_ , i.e., 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0013-16.png)


and concludes the proof for (i). Note that (A.3) holds for all non-decreasing functions _u_ : R _→_ R, which also includes all non-decreasing concave and convex functions that define SOSD and MCX. Hence, combining (A.1)-(A.3) with Definitions 2 and A2 concludes the proof for (ii) and (iii). 

**Lemma A2. (Convex dominance of mixture distributions over convex combinations of random variables)** _Let X ∈_ R _and Y ∈_ R _be two real-valued random variables with finite means, and let π ∈_ [0 _,_ 1] _be a constant. If Z and V are two random variables constructed as:_ 

- _Z is the absolute value of the convex combination of X and Y , i.e., Z_ = _|πX_ + (1 _− π_ ) _Y |,_ 

- _V is a mixture of |X| and |Y |, i.e., V_ = _W |X|_ + (1 _− W_ ) _|Y |, W ∼ Bernoulli_ ( _π_ ) _,_ 

then we have _V ⪰mcx Z_ for any _π ∈_ [0 _,_ 1] and any distribution _P_ ( _X, Y_ ). 

_Proof._ Recall from Definition 2 that _V ⪰mcx Z_ if and only if 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0013-23.png)


(A.4) 

13 

for all non-decreasing convex functions _u_ : R _→_ R. Given the definition of _V_ above, we have 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0014-01.png)


where the last two inequalities follow from (a) the convexity of _u_ , and (b) the monotonicity of _u_ along with the application of the triangle inequality _|πX|_ + _|_ (1 _− π_ ) _Y | ≥|πX_ + (1 _− π_ ) _Y |_ . 

**Lemma A3. (Stochastic dominance and sign changes in CDFs)** _Let X and Y be two non-negative random variables with distribution functions F and G and with finite means such that_ E[ _X_ ] _≤_ E[ _Y_ ] _. Let S[−]_ ( _f_ ) _be the number of sign changes of a function f defined as_ 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0014-04.png)


_where S[−]_ [ _a_ 1 _, a_ 2 _, . . . , am_ ] _is the number of sign changes of the sequence_ [ _a_ 1 _, a_ 2 _, . . . , am_ ] _, with the zero terms being discarded, and the supremum in (A.6) is taken over all sets x_ 1 _< x_ 2 _< . . . < xm such that m < ∞. Then, F ⪰(2)_ [ _⪰mcx_ ] _G if and only if there exist random variables Z_ 1 _, Z_ 2 _,. . . , with distribution functions G_ 1 _, G_ 2 _,.. ., such that Z_ 1 = _st X,_ E[ _Zj_ ] _≤_ E[ _Y_ ] _, j_ = 1 _,_ 2 _, . . ., Zj →st Y and_ E[ _Zj_ ] _→_ E[ _Y_ ] _as j →∞ and S[−]_ ( _Gj_ +1 _− Gj_ ) = 1 _and the sign sequence is {_ + _, −}_ [ _{−,_ + _}_ ] _. Here,_ = _st denotes equality in law and →st denotes convergence in distribution._ 

_Proof._ Refer to Theorems 4.A.22 and 4.A.23 in [28] for a full proof. 

**Corollary A4. (CDF crossings under SOSD and MCX)** _Let X and Y be non-negative random variables with CDFs F and G with finite means such that_ E[ _X_ ] _≤_ E[ _Y_ ] _. Then, if F ⪰(2)_ [ _⪰mcx_ ] _G, we have S[−]_ ( _F −G_ ) _≥_ 1 _and the corresponding sign sequence is {. . . , −,_ + _}_ [ _{. . . ,_ + _, −}_ ] _. Equivalently, there exists α[∗] ∈_ (0 _,_ 1) _such that F[−]_[1] ( _α[∗]_ ) = _G[−]_[1] ( _α[∗]_ ) = _v[∗] and F_ ( _v_ ) _≥_ [ _≤_ ] _G_ ( _v_ ) _, ∀v ≥ v[∗] ._ 

_Proof._ From Lemma A3, we know that if _F ⪰_ (2) [ _⪰mcx_ ] _G_ then there exists a sequence of random variables _Z_ 1, _Z_ 2,..., with distributions _G_ 1, _G_ 2,..., such that _Z_ 1 = _st X_ , _Zj →st Y_ , and the CDFs satisfy _S[−]_ ( _Gj_ +1 _− Gj_ ) = 1 with a sign sequence _{−,_ + _}_ [ _{_ + _, −}_ ]. 

Now observe that for any three integers _k < m < n_ , if _S[−]_ ( _Gm − Gk_ ) = 1 with a sign sequence of _{−,_ + _}_ [ _{_ + _, −}_ ], and _S[−]_ ( _Gn − Gm_ ) = 1 with a sign sequence _{−,_ + _}_ [ _{_ + _, −}_ ], then by monotonicity of CDFs it follows that in the last point of crossing, _Gn_ crosses _Gk_ from below [above], i.e., _Gn − Gk_ has at least one sign change with _{. . . , −,_ + _}_ [ _{. . . ,_ + _, −}_ ]. Thus, for any _j_ , the three random variables _Z_ 1 = _st X_ , _Zj_ and _Y_ satisfy _S[−]_ ( _Gj − F_ ) = 1 and _S[−]_ ( _G − Gj_ ) = 1 with a sign sequence _{. . . , −,_ + _}_ [ _{. . . ,_ + _, −}_ ], which implies that in the last point of crossing, _F_ crosses _G_ from below [above] and concludes the statement of the corollary. 

## **A.3. Proof of Theorem 1** 

**Theorem 1.** _If_ ( _Xi, Wi, Yi_ (0) _, Yi_ (1)) _, i_ = 1 _, . . . , n_ + 1 _are exchangeable, then ∃ α[∗] ∈_ (0 _,_ 1) _such that the pseudo-interval C_[�] _φ_ ( _Xn_ +1) _constructed using the dataset D_ = _{_ ( _Xi, Wi, Yi_ ) _}[n] i_ =1 _[satisfies]_ 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0014-12.png)


_if at least one of the following stochastic ordering conditions hold: (i) Vφ ⪰(1) V[∗] , (ii) Vφ ⪯(2) V[∗] , and (iii) Vφ ⪰mcx V[∗] . Under condition (i), we have α[∗]_ = 1 _._ 

_Proof._ Without loss of generality, assume that the conformity scores are sorted, _Vφ,_ 1 _< . . . < Vφ,nc ,_ where _nc_ = _|Dc|_ . Recall from (10) that the pseudo-interval is constructed as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0014-15.png)


where _QVφ_ (1 _− α_ ) is the empirical quantile defined as 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0014-17.png)


14 

Combining (A.7) and (A.8), we notice that the following two events are equivalent 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-01.png)


or equivalently, 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-03.png)


Hence, the achieved coverage probability for the pseudo-interval is given by 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-05.png)


By exchangeability of the variables ( _X_ 1 _, Y_ 1(1) _− Y_ 1(0)) _, ...,_ ( _Xn_ +1 _, Yn_ +1(1) _− Yn_ +1(0)), we have 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-07.png)


for any integer _k_ . (A.12) holds because ranks are uniformly distributed under exchangeability, i.e., _Vφ,n_ +1 is equally likely to fall in anywhere between the calibration points _Vφ,_ 1 _, . . . , Vφ,nc_ . From (A.12), it follows that for _⌈_ ( _nc_ + 1)(1 _− α_ ) _⌉_ we have: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-09.png)


Now, we examine the three conditions: (i) _Vφ ⪰_ (1) _V[∗]_ , (ii) _Vφ ⪯_ (2) _V[∗]_ , and (iii) _Vφ ⪰mcx V[∗]_ . 

## **(i) FOSD** _**Vφ ⪰**_ **(1)** _**V[∗]**_ **:** 

If _Vφ ⪰_ (1) _V[∗]_ , then from Definition 1: _FVφ_ ( _v_ ) _≤ FV ∗_ ( _v_ ) _, ∀v_ . Equivalently, FOSD can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-13.png)


Since (A.14) applies for any _v_ , then the following holds: 

_Vφ,n_ +1 _⪰_ (1) _Vn[∗]_ +1 _[⇐⇒]_[P][(] _[V][φ,n]_[+1] _[≤][V] φ,⌈_ ( _nc_ +1)(1 _−α_ ) _⌉_[)] _[ ≤]_[P][(] _[V] n[∗]_ +1 _[≤][V] φ,⌈_ ( _nc_ +1)(1 _−α_ ) _⌉_[)] _[.]_[(A.15)] Combining (A.13) and (A.15) we have 

_Vφ,n_ +1 _⪰_ (1) _Vn[∗]_ +1 _[⇒]_[P][(] _[V] n[∗]_ +1 _[≤][V] φ,⌈_ ( _nc_ +1)(1 _−α_ ) _⌉_[)] _[ ≥]_[P][(] _[V][φ,n]_[+1] _[≤][V] φ,⌈_ ( _nc_ +1)(1 _−α_ ) _⌉_[)] _[ ≥]_[1] _[ −][α.,]_ which holds for any _α_ , hence _α[∗]_ = 1. This concludes statement (i). 

## **(ii) SOSD** _**Vφ ⪯**_ **(2)** _**V[∗]**_ **:** 

If _Vφ ⪯_ (2) _V[∗]_ , then from Corollary A4 we know that _∃ α[∗] ∈_ (0 _,_ 1) where _FV[−] φ_[1][(] _[α][∗]_[) =] _[ F][ −] V[∗]_[1][(] _[α][∗]_[) =] _[ v][∗]_ and _FV ∗_ ( _v_ ) _≥ FVφ_ ( _v_ ), _∀v ≥ v[∗]_ . Equivalently, SOSD can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-19.png)


Hence, the following holds: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0015-21.png)


for all _α ≤ α[∗]_ . Combining (A.13) and (A.17) we have 

_Vφ,n_ +1 _⪯_ (2) _Vn[∗]_ +1 _[⇒]_[P][(] _[V] n[∗]_ +1 _[≤][V] φ,⌈_ ( _nc_ +1)(1 _−α_ ) _⌉_[)] _[ ≥]_[P][(] _[V][φ,n]_[+1] _[≤][V] φ,⌈_ ( _nc_ +1)(1 _−α_ ) _⌉_[)] _[ ≥]_[1] _[ −][α.,]_ for all 0 _≤ α ≤ α[∗]_ . This concludes statement (ii). 

## **(iii) MCX** _**Vφ ⪰mcx V[∗]**_ **:** 

Since Corollary A4 holds for SOSD and MCX, the proof is identical to the proof for (ii). 

15 

## **A.4. Proof of Theorem 2** 

**Theorem 2.** _Let Vφ_ ( _τ_ �) = _|τ_ �( _X_ ) _− Y_[�] _φ| and assume that the propensity score function π_ : _X →_ [0 _,_ 1] _is known. Then, the following holds: (i) For the X-learner, Vφ and V[∗] do not admit to a model- and distribution-free stochastic order, (ii) For any distributionand nuisance estimate φ_ � _, the IPW- and the DR-learners satisfy P_ ( _X, W, Y Vφ ⪰mcx_ (0) _, YV[∗]_ (1)) _. , CATE estimate_ � _τ ,_ 

_Proof._ For a CATE estimate � _τ_ , the oracle scores are 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-03.png)


In what follows, we use the notation _Vφ_ ( _x_ ) to denote the conditional random variable _Vφ|X_ = _x_ , i.e., the conformity score evaluated at a given feature point. Similarly, we use _V[∗]_ ( _x_ ) to denote the conditional random variable _V[∗] |X_ = _x_ (oracle score evaluated at a given feature point). 

## **Proof of statement (i):** 

Recall from Table 1 that the pseudo-outcome for the X-learner is given by: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-07.png)


With _Vφ_ ( _τ_ �) = _|τ_ �( _X_ ) _− Y_[�] _φ|_ , the conformity score for the X-learner can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-09.png)


To prove statement (i), it suffices to find counter-examples for estimators _τ_ �, _µ_ �0 and _µ_ �1, or data distributions that cause violations of FOSD, SOSD and MCX between _Vφ_ and _V[∗]_ . Let _u_ : R _→_ R be a non-decreasing function. The expected value of _u_ ( _Vφ_ ( _x_ )) can be evaluated as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-11.png)


We start by showing that there exists nuisance and CATE estimates and a data distribution for which _Vφ_ does not have FOSD over _V[∗]_ . Assume that _u_ is concave. Then, the following inequality holds: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-13.png)


Now consider a nuisance estimates of _µ_ �0 = 0 and _µ_ �1 = 0, a data distribution for which _Y_ (0) _>_ 0 and _Y_ (1) _<_ 0 almost surely, and a CATE estimator � _τ_ ( _x_ ) _>_ 0 _, ∀x ∈X_ , then we have 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-15.png)



![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-16.png)



![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-17.png)


and hence _V[∗]_ ( _x_ ) _⪰_ (2) _Vφ_ ( _x_ ) for all _x_ , and by Lemma A1, we have _V[∗] ⪰_ (2) _Vφ_ . The last inequality in (A.22) holds because _u_ is non-decreasing and (1 _− π_ ( _x_ )) _Y_ (1) _− π_ ( _x_ ) _Y_ (0) is always non-positive when _Y_ (0) _>_ 0 and _Y_ (1) _<_ 0 (almost surely). Since SOSD is a necessary condition for FOSD, then it follows that _Vφ_ does not have FOSD over _V[∗]_ in this counter-example. 

Now we show that there exists nuisance and CATE estimates and a data distribution for which _Vφ_ does not have MCX over _V[∗]_ . This follows directly from the previous counter-example. Since _V[∗] ⪰_ (2) _Vφ_ implies that _−Vφ ⪰mcx −V[∗]_ (Theorem 4.A.1. in [28]), then _Vφ_ does not have MCX over _V[∗]_ . 

Finally, we show that there exists nuisance and CATE estimates and a data distribution for which _V[∗]_ does not have SOSD over _Vφ_ . Note that E[ _V[∗]_ ] _≥_ E[ _Vϕ_ ] is a necessary condition for _V[∗] ⪰_ (2) _Vφ_ (See Eq. (4.A.6) in [28]). Note that E[ _Vϕ_ ( _x_ )] can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0016-21.png)


- � � � 

- = _π_ ( _x_ ) _·_ E[ _|τ_ ( _x_ ) _−_ ( _Y_ (1) _− µ_ 0( _x_ )) _|_ ] + (1 _− π_ ( _x_ )) _·_ E[ _|τ_ ( _x_ ) _−_ ( _µ_ 1( _x_ ) _− Y_ (0)) _|_ ] _,_ 

- � � � 

- = E[ _π_ ( _x_ ) _· |τ_ ( _x_ ) _−_ ( _Y_ (1) _− µ_ 0( _x_ )) _|_ + (1 _− π_ ( _x_ )) _· |τ_ ( _x_ ) _−_ ( _µ_ 1( _x_ ) _− Y_ (0)) _|_ ] _,_ 

- _≥_ E[ _|τ_ �( _x_ ) _− π_ ( _x_ )( _Y_ (1) _− µ_ �0( _x_ )) _−_ (1 _− π_ ( _x_ ))( _µ_ �1( _x_ ) _− Y_ (0)) _|_ ] _,_ 

- � � 

- = E[ _|τ_ ( _x_ ) _−_ ( _Y_ (1) _− Y_ (0)) + (1 _− π_ ( _x_ ))( _Y_ (1) _− µ_ 1( _x_ )) + _π_ ( _x_ )( _µ_ 0( _x_ ) _− Y_ (0)) _|_ ] _,_ 

16 

and for nuisance estimates that satisfy� � _µ_ �1( _x_ ) _< Y_ (1) and _µ_ �0( _x_ ) _> Y_ (0) almost surely, the term (1 _− π_ ( _x_ ))( _Y_ (1) _− µ_ 1( _x_ )) + _π_ ( _x_ )( _µ_ 0( _x_ ) _− Y_ (0)) above is always positive and hence we have: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-01.png)


which implies that _V[∗]_ does not have SOSD over _Vφ_ . 

## **Proof of statement (ii):** 

From Table 1, the pseudo-outcomes for the IPW- and DR-learners can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-05.png)


where _Yπ_ and _Y_ 1 _−π_ are defined as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-07.png)


Note that, following the definition in (A.25), the following holds for both the IPW- and DR-learners: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-09.png)


Hence, applying (A.26) to the definition of the oracle score, we can write _V[∗]_ ( _x_ ) as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-11.png)


From the expressions in (A.24�) and (A.27), we can see that� _Vφ_ ( _x_ ) is a mixture of the absolute values of the two random variables ( _τ_ ( _x_ ) _− Yπ_ ( _x_ )) and ( _τ_ ( _x_ ) _− Y_ 1 _−π_ ( _x_ )) with mixing proportions _π_ ( _x_ ) and 1� _− π_ ( _x_ ), and _V[∗]_ ( _x_ ) is the absolute value of the convex combination of the same random variables,� ( _τ_ ( _x_ ) _− Yπ_ ( _x_ )) and ( _τ_ ( _x_ ) _− Y_ 1 _−π_ ( _x_ )), with weights _π_ ( _x_ ) and 1 _− π_ ( _x_ ). Applying Lemma A2, it follows that _Vφ_ ( _x_ ) _⪰mcx V[∗]_ ( _x_ ) _, ∀x ∈X_ , and from Lemma A1 we have that _Vφ ⪰mcx V[∗]_ . 

## **Stochastic orders for the signed distance conformity score:** 

We have shown that for the absolute residual conformity score, _Vφ_ ( _τ_ �) = _|τ_ �( _X_ ) _− Y_[�] _φ|_ , the DR- and IPW-learners guarantee _Vφ ⪰mcx V[∗]_ irrespective of the data distribution and underlying models. We now study the stochastic orders achieved by the signed distance conformity score proposed in [32], defined as: _Vφ_ ( _τ_ �) = _τ_ �( _X_ ) _− Y_[�] _φ_ . Let _u_ be a non-decreasing concave function, then we have: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-15.png)


where the inequality follows from the concavity of _u_ ( _._ ) and the last equality follows from (A.26). From Definition 1, (A.28) implies that _V[∗] ⪰_ (2) _Vφ_ (Table 2). Note, however, that the construction of predictive intervals with the signed error distance does not follow (5) since the signed distance score does not sort absolute errors from largest to smallest, but it sorts conformity scores from maximum positive error to maximum negative error. Hence, Theorem 1 does not apply to the signed distance error and the SOSD condition _V[∗] ⪰_ (2) _Vφ_ does not guarantee coverage. 

Another more commonly used variant of the signed distance score was proposed in [25]. Given a quantile regression model [ _τ_ � _l,_ � _τh_ ], [25] uses a variant of the signed error score defined as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0017-18.png)


17 

The construction of the predictive intervals in [25] follows (5). Note that max _{x, y}_ can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-01.png)


Applying (A.30) to (A.29), we can rewrite the conformity scores as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-03.png)


Similarly, the oracle scores can be written as: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-05.png)


Let _δτ−_ = _[τ]_[�] _[l][−]_ 2 _[τ]_[�] _[h]_ , _δτ_ + = _[τ]_[�] _[l]_[+] 2 _[τ]_[�] _[h]_ , and let _u_ be a non-decreasing convex function, then we have: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-07.png)


where the first inequality follows from the convexity of _u_ , the second inequality is an application of the triangle inequality, and the last equality follows from (A.26). Following Definition 2, (A.33) implies that _Vφ ⪰mcx V[∗]_ when the base models apply quantile regression and the conformity scores follow the signed distance score in [25]. Hence, the coverage guarantee in Theorem 1 applies to conformal meta-learners based on conditional quantile regression. 

## **Appendix B: Literature Review** 

In this Section, we provide a comprehensive overview of the relevant literature. We categorize the previous literature into three distinct strands: (1) Bayesian methods for modeling individualized causal effects, (2) frequentist methods for inference on parameters pertaining to individualized causal effects, and (3) conformal methods for predictive inference of ITEs. 

**(1) Bayesian methods.** Predictive inference on ITEs has been traditionally conducted using Bayesian methods. These methods place a prior distribution over the nuisance parameters _µ_ 0 and _µ_ 1, and then estimate the CATE function through the posterior distribution computed conditional on the observational dataset _D_ = _{_ ( _Xi, Wi, Yi_ ) _}i_ . More formally, Bayesian procedures operate as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-12.png)


where Π0 and Π1 are priors over function spaces, and _ϵ ∼N_ (0 _, σ_[2] ). Given the dataset _D_ , the posterior distributions over the two nuisance functions are used to estimate CATE as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-14.png)


Furthermore, the posterior distributions Π0 _|D_ and Π1 _|D_ can be used to construct predictive intervals on ITEs through the posterior credible intervals of _P_ Π0( _µ_ 1( _x_ ) _|D_ ) and _P_ Π1( _µ_ 1( _x_ ) _|D_ ), i.e., 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0018-16.png)


Different incarnations of the Bayesian framework correspond to different choices of the prior (Π0 _,_ Π1). Bayesian Additive Regression Trees (BART) [34] is one popular model for Bayesian nonparametric regression that was later adapted for causal effect estimation and inference [8, 35]. While [8] applies BART for estimation of CATE and inference of ITE out-of-the-box, [35] introduces new regularization techniques to incorporate different forms of inductive biases on the CATE target parameter. Another 

18 

popular choice of the prior (Π0 _,_ Π1) is based on Gaussian processes where inductive biases are incorporated through different choices of the kernel function of a reproducible kernel Hilbert space [9]. 

Unlike the conformal framework, Bayesian methods do not provide coverage guarantees on their credible intervals. Frequentist coverage can be achieved in an asymptotic sense by Bayesian method under certain technical conditions [36]. Existing methods typically do not provide any finite-sample guarantees and the achieved empirical coverage depends on the choice of the prior. Models such as BART are typically applied with a default prior for all datasets, undermining their achieved coverage in diverse experimental setup. In [1], it was shown that Bayesian methods have a tendency to undercover ITEs in some data generation processes (e.g., in high-dimensional covariate spaces). 

Bayesian methods also suffer from two key advantages compared to the conformal framework. First, Bayesian inference procedures and the computation of posterior distributions are typically tailored to specific model architectures. Generalizing exact Bayesian inference to arbitrary model architectures, including modern deep learning architectures, is not straightforward. Moreover, Bayesian inference is conducted either using computationally exhaustive Monte Carlo method (e.g., BART) or through expensive evaluation of an analytical posterior distribution that does not scale well with the number of training points (e.g., Gaussian process posteriors are _O_ ( _n_[3] )). 

**(2) Frequentist methods.** Another model-specific approach to inference on causal parameters is the Causal Forest model in [7]. This procedure uses constructs pointwise confidence intervals on the CATE function _τ_ ( _x_ ) using conditional variance estimates based on the infinitesimal jackknife [37]. These intervals provide asymptotically valid coverage of CATE under mild regularity assumptions, but they provide no (asymptotic or finite-sample) guarantees on coverage for ITEs. 

Another non-Bayesian approach for predictive inference of ITEs uses a quantile regression approach to train models that construct upper and lower bounds on the observed potential outcomes using a pinball loss [38]. While quantile regression can be repurposed for different model architectures, this approach does not provide finite-sample coverage guarantees and is empirically found to undercover outcomes, hence it is typically supplemented with a conformal prediction procedure [25]. 

**(3) Conformal methods.** The application of conformal prediction to ITE inference traces its origins back to the covariate shift problem. In [26], a variant of conformal prediction was proposed to address problem setups where training and testing data are drawn from different distributions, breaking the exchangeability assumptions required for valid inference. 

In the treatment effect estimation setup, covariate shift arises because the distributions of the treatment groups differ from that of the target population. Recall from (8) that the conformity scores for the nuisance estimates _µ_ �0 and _µ_ �1 can be written as follows: 


![](markdown_output/conformal-metalearners_images/conformal-metalearners.pdf-0019-07.png)


Both sets of conformity scores are sampled from the populations _PX|W_ =0 and _PX|W_ =1, respectively, and hence they are not exchangeable with the conformity scores sampled from target covariate distribution _PX_ . To retain the validity of intervals constructed using the sample quantiles of conformity scores, [26] introduces the notion of “weighted exchangeability” and proposes a weighted sample quantile with weights based on the likelihood ratios between training and testing distributions. [1] uses this method to construct valid intervals for potential outcomes and then proposes different approaches for combining these intervals to construct intervals for ITEs. Other work utilized the conformal prediction framework to conduct sensitivity analysis by devising hypothesis tests for the presence of hidden confounders [39, 40]. In [41, 42], conformal prediction has been utilized to address the closely related problem of off-policy evaluation. More recently, there has been further work developing methods for conformal prediction under covariate shift [43, 44, 45]. 

The key difference between our work and the aforementioned approaches is that we do not apply conformal prediction to the nuisance parameters, and instead conduct inference directly on the target parameter. We do so by applying conformalization with respect to transformed targets _Y_[�] _φ_ for each data point in _D_ , and this way the covariate shift problem does not arise since ( _X, Y_[�] _φ_ ) is sampled from the same distribution in calibration and testing data. One way to think about our approach as opposed to weighted conformal prediction (WCP) is that ours applies re-weighting to the outcomes whereas WCP re-weights the conformity scores. By moving the re-weighting step to the outcomes, we decouple the conformal procedure from the model, allowing for more flexible choice of inductive priors and accommodating models that do not estimate potential outcomes directly. 

19 

## **Appendix C: Experimental Setup and Results** 

## **C.1. Overview of the experimental setup** 

In all experiments, we used a Gradient Boosting model with 100 trees as the base model for nuisance estimation and quantile regression on pseudo-outcomes. We used the same base model in conformal meta-learners as well as the weighted CP (WCP) baselines to control for potential performance differences resulting from different choices of base models. Unless otherwise stated, all experiments followed a 90%/10% train/test split of each dataset, and each training set with further split into a 75%/25% proper training/calibration sets. All performance metrics (empirical coverage, expected interval width and RMSE) are evaluated on the testing data and averaged over 100 runs. The target coverage in all experiments was set 1 _− α_ = 0 _._ 9. 

We used the official implementations of the (naïve, exact and inexact) WCP baselines in the R package available at https://github.com/lihualei71/cfcausal. We executed these baselines through rpy2 (https://rpy2.github.io/) wrappers within our Python codebase. 

## **C.2. Details of the IHDP and NLSM datasets** 

In this Section, we provide details of the semi-synthetic datasets used in the experiments in Section 5. 

**IHDP dataset.** The Infant Health and Development Program (IHDP) was a multi-site randomized controlled trial that studied the effect of early educational intervention on the cognitive development of low birth weight premature infants [46]. The trial targeted low-birth-weight, premature infants, and administered an intensive high-quality child care and home visits from a trained provider to the treatment group. In [8], a semi-synthetic benchmark was developed based on the covariate data in IHDP with simulated outcomes to assess the performance of different CATE estimation and ITE inference models when ground-truth counterfactual are known. The dataset comprised 25 covariates (6 continuous and 19 binary variables) capturing aspects related to children and their mothers. The benchmark dataset excluded a non-random subset of treated individuals [8]. The final dataset consists of 747 samples (139 treated and 608 control). The outcomes of all individuals were simulated whereas the treatment assignments followed the true assignments in the study. 

The simulated outcomes model in IHDP followed simulation Setup B in [8]. In this Setup, the potential outcomes were simulated as follows: _Y_ (0) _∼N_ (exp(( _X_ + _W_ ) _β_ ) _,_ 1) and _Y_ (1) _∼ N_ (exp( _Xβ_ ) _− ω,_ 1), where _W_ is an offset matrix, _ω_ is set so that the ATE on the treated is always equal to 4, and the coefficients _β_ are sampled independently at random from (0 _,_ 0 _._ 1 _,_ 0 _._ 2 _,_ 0 _._ 3 _,_ 0 _._ 4) with probabilities (0 _._ 6 _,_ 0 _._ 1 _,_ 0 _._ 1 _,_ 0 _._ 1 _,_ 0 _._ 1). In our experiments, we used the 100 realization of the training and testing data released by [6] in https://www.fredjo.com/files/ihdp_npci_1-100.train.npz and https://www.fredjo.com/files/ihdp_npci_1-100.test.npz. 

**NLSM dataset.** The National Study of Learning Mindsets (NLSM) is a large-scale randomized trial that studied the effect of a behavioral intervention, designed to instill students with a growth mindset, on the academic performance of students in secondary education in the US [3]. In [33], a semisynthetic benchmark was developed based on the covariates of the NLSM study. Unlike IHDP, this benchmark does not use the real covariates of NLSM but rather buids a synthetic process to emulate NSLM in terms of the covariate distributions, data structures, and effect sizes. The final dataset comprised 10,000 data points. The data was generated based on 5 principles (See Section 2 and Appendix A in [33]). The principles are: (1) ATEs should be well-estimated from synthetic data by any reasonable procedure, (2) variability in CATE should be relatively modest, (3) treatment effect heterogeneity can be approximately recovered given complete knowledge of the correct functional form, (4) no additional unmeasured treatment effect moderation at the individual level, and (5) unexplained treatment effect heterogeneity at the group level should be present at reasonable levels. 

## **C.3. Further experiments using the ACIC dataset** 

In addition to the IHDP, NLSM and fully-synthetic experiments, we also conducted further experiments on 77 datasets from the 2016 Atlantic Causal Inference Competition (ACIC2016) [47]. We followed the processing steps in [16], creating a dataset of 4,802 data points and 55 covariates. Out of this base dataset, we created 770 simulation setups using the 77 settings proposed in [47]. The 77 settings represent different levels of complexity of response surfaces, varying degrees of confounding, 

20 

Figure C.1: Performance of all baseline across the 77 ACIC experiments. 

21 

overlap and effect heterogeneity. All settings use the same covariates but simlate different treatment assignments and response surfaces. We created 10 realizations of each of the 77 settings and average the performance of all baselines across the 10 runs. 

The empirical coverage, average interval width and RMSE results across all 77 experiments are provided in Figure C.1. The comprehensive experiments in Figure C.1. align with the overall conclusions of the experiments in the main paper. For a target coverage of 1 _− α_ = 0 _._ 9, all models achieved the target coverage with the exception of the X-learner. All models achieving the target coverage displayed conservative predictive intervals, acheiving coverage levels that exceed the 0.9 target. In terms of efficiency, the DR-learner and WCP-Inexact achieved comparable interval widths, significantly outperforming all other valid procedures (IPW-learner, WCP-exact and WCP-Naïve). Finally, the the DR-learner outperformed all valid procedure in terms of RMSE in almost all experiments, providing point estimation accuracy that is on par with the X-learner. 

These results align with the overall conclusions of the experiments in the main paper. The DR-learner generally inherits the accurate point estimation of its underlying CATE meta-learner, provides a coverage guarantee for practically relevant values of target coverage and achieves this coverage with competitive efficiency making it a favorable approach for both point estimation of CATE and predictive inference of ITE. 

22 

