## **Quantile Processes for Dynamic Risk Modelling in Finance and Insurance** 

Gareth W. Peters[2] , Andrea Macrina[1][*] , Holly Brannelly[1] , 

1Department of Mathematics, University College London London, United Kingdom 

2Department of Statistics & Applied Probability University of California Santa Barbara Santa Barbara, USA 

## April 26, 2026 

## **Abstract** 

We develop a novel approach for the construction of quantile processes governing the stochastic dynamics of quantiles in continuous time. Two classes of quantile diffusions are identified: the first, which we largely focus on, features a dynamic random quantile level and allows for direct interpretation of the resulting quantile process characteristics such as location, scale, skewness and kurtosis, in terms of the model parameters. The second type are function–valued quantile diffusions and are driven by stochastic parameter processes, which determine the entire quantile function at each point in time. By the proposed innovative and simple—yet powerful— construction method, quantile processes are obtained by transforming the marginals of a diffusion process under a composite map consisting of a distribution and a quantile function. Such maps, analogous to rank transmutation maps, produce the marginals of the resulting quantile process. We discuss the relationship and differences between our approach and existing methods and characterisations of quantile processes in discrete and continuous time. As an example of an application of quantile diffusions, we show how probability measure distortions, a form of dynamic tilting, can be induced. Though particularly useful in financial mathematics and actuarial science, examples of which are given in this work, measure distortions feature prominently across multiple research areas. For instance, dynamic distributional approximations (statistics), non–parametric and asymptotic analysis (mathematical statistics), dynamic risk measures (econometrics), behavioural economics, decision making (operations research), signal processing (information theory), and not least in general risk theory including applications thereof, for example in the context of climate change. 

**Keywords** : Diffusions, order statistics and empirical distributions, quantile functions, stochastic differential equations, Tukey transforms, probability measure distortions, dynamic tilting, Wang transform, risk. 

GWP: rewritten 16.03.2026 - Sections in blue are completely rewritten 

## **1 Introduction** 

Modern actuarial science and insurance risk management increasingly rely on the dynamic modelling of full loss distributions rather than solely their first two moments. Applications such as capital adequacy under Solvency II, catastrophe risk management, reinsurance pricing, and dynamic portfolio risk monitoring require careful modelling of tail behaviour and extreme quantiles of loss processes. In particular, regulatory and economic capital measures such as Value–at–Risk (VaR) and Tail Value–at–Risk (TVaR) are explicitly defined in terms of quantiles of loss distributions. Consequently, stochastic models that can directly capture the evolution of quantile functions through time are of significant interest in actuarial science and financial risk management. 

The dynamics of stochastic processes are typically characterised through properties such as drift, volatility, and higher–order moment dynamics of their finite–dimensional distributions. However, 

> * _∗_ Corresponding author: a.macrina@ucl.ac.uk 

1 

in many insurance applications the primary objects of interest are not densities or moments, but rather quantiles of the loss distribution. For example, solvency capital requirements, catastrophe reinsurance attachment probabilities, and tail risk metrics are naturally expressed through quantile functionals of aggregate loss processes. Motivated by this observation, this paper develops a new class of continuous–time stochastic processes termed _quantile diffusions_ . These processes evolve directly in the space of quantiles and allow the modeller to control tail behaviour and distributional asymmetry through interpretable parameters. 

The quantile diffusion framework introduced in this paper constructs continuous–time stochastic processes whose marginal distributions are generated through transformations applied to an underlying diffusion process. In particular, we introduce a flexible family of _Tukey quantile diffusions_ , based on the Tukey _g_ –and– _h_ transformation, which provides a parsimonious representation of skewness and tail heaviness. This allows the resulting stochastic processes to exhibit a wide spectrum of tail behaviours, ranging from exponentially decaying tails to heavy–tailed distributions with regular variation. Such flexibility is particularly important in actuarial applications where insurance loss distributions are typically skewed and heavy–tailed [15, 22]. 

The idea of distorting a probability measure in order to modify distributional properties is well established in statistics, finance, and actuarial science. In classical statistical theory, density distortions are often used to produce approximations that adjust moments or cumulants of a base distribution. Common examples include saddlepoint approximations, Edgeworth expansions, and Esscher transformations, which modify a base distribution to better approximate a target distribution [11, 6, 4]. In actuarial science, related ideas arise in premium principles and distortion risk measures, where transformations of the distribution function are used to incorporate risk aversion or market preferences into pricing and capital calculations [34, 18]. 

In contrast to the traditional focus on density distortions, this paper studies distortions applied directly in the _quantile space_ . This perspective is particularly appealing in insurance and risk management because many relevant risk measures and pricing rules are naturally expressed in terms of quantiles. By constructing stochastic processes whose quantile functions evolve through time, we obtain a dynamic framework capable of modelling time–varying skewness, kurtosis, and tail behaviour in a transparent manner. 

From a modelling perspective, the proposed framework can be viewed as a continuous–time extension of quantile transformation techniques that have been widely used in statistical modelling. Transformations of distributions via quantile functions have been explored in numerous contexts, including rank transmutation mappings and distributional transformations [30, 17]. Such transformations allow a base distribution to be mapped into a more flexible target distribution while preserving interpretability of the transformation parameters. 

The approach developed in this paper extends these ideas into the stochastic process setting. Specifically, we construct quantile diffusions by applying a composite transformation consisting of a distribution function and a quantile function to the marginal distributions of a base diffusion process. This construction produces a new stochastic process whose marginal distributions are explicitly controlled through the transformation map. In doing so, we obtain a flexible class of stochastic processes capable of capturing a broad range of distributional behaviours relevant to insurance loss modelling. 

The proposed framework also relates to several existing strands of literature on quantile dynamics and risk processes. Quantile functions have long played an important role in statistical modelling and econometrics, particularly in the context of quantile regression and conditional distribution modelling [23]. In actuarial science and financial risk management, dynamic risk measures have been developed to describe the evolution of risk metrics such as Value–at–Risk over time [7, 1]. These approaches typically focus on modelling quantile processes in discrete time or on defining time–consistent risk measures. 

Another related line of research arises in the probability literature on empirical quantile processes [9], as well as in work on the distributional behaviour of quantiles of diffusion processes [ **?** 

2 

]. For example, Miura [27] introduced the concept of a percentile option, whose payoff depends on the quantile of an underlying diffusion process over the life of the contract. Subsequent work has investigated the distribution of such quantiles for pricing purposes [2]. These studies typically analyse the distributional properties of quantiles derived from a given diffusion process. 

In contrast, the approach developed in this paper focuses on constructing new classes of stochastic processes whose dynamics are defined directly through quantile transformations. Rather than starting with a diffusion process and deriving the properties of its quantiles, we instead construct stochastic processes whose marginal distributions are generated through quantile maps. This construction provides a flexible and interpretable way to specify dynamic loss distributions with controllable tail behaviour. 

Two distinct classes of quantile diffusion models are introduced. The first is a _process–driven_ construction, which produces scalar quantile diffusion processes obtained by transforming a base diffusion through a composite distribution–quantile mapping. The second is a _parameter–driven_ construction, which yields function–valued stochastic processes evolving in the space of quantile functions. In this paper we focus primarily on the process–driven construction, which provides a tractable framework for modelling dynamic loss distributions. 

The remainder of the paper develops the mathematical foundations of this framework and illustrates how quantile diffusions can be used to construct flexible stochastic models with controllable distributional properties. Applications in actuarial science and risk management include modelling aggregate insurance losses, dynamic capital requirement processes, and pricing of tail–sensitive reinsurance contracts. These examples demonstrate that the proposed construction provides a powerful and interpretable approach to modelling the dynamics of heavy–tailed risk processes in insurance and finance. 

## **1.1 Contributions** 

This paper develops a constructive framework for modelling quantile dynamics in continuous time. The central idea is to work directly in quantile space: rather than starting from a stochastic process and deriving its quantiles as descriptive objects, we specify a target quantile family and use it to construct new stochastic processes with controlled marginal shape and interpretable tail behaviour. 

Our first contribution is the introduction of a _random–level quantile diffusion_ . This process is obtained by transforming the marginals of a driving diffusion through a composite distribution– quantile map. In the true–law case, the construction produces a scalar stochastic process whose one–time marginals coincide exactly with a prescribed target distribution, while the serial dependence is inherited from the driving diffusion. This separates marginal distributional design from temporal dependence in a transparent way. We derive the corresponding Itô dynamics under suitable smoothness assumptions and characterise the induced transition structure and order-preserving properties. 

Our second contribution is the introduction of a _function–valued quantile diffusion_ . Here, a diffusion is placed directly on the parameter vector of an admissible quantile family, thereby producing a stochastic process that evolves in a function space of quantile curves. This provides a continuous– time model for the stochastic evolution of the entire quantile function and offers a natural route to dynamic modelling of location, scale, skewness, and tail thickness. 

A third contribution is conceptual and methodological. We formalise the distinction between the proposed constructions and classical notions of quantile processes. In particular, we show that the objects introduced here are _constructive quantile models_ , whereas classical fixed–level quantile curves and quantiles of diffusion processes are derived from an already specified model. This distinction is made precise through a comparison with deterministic marginal quantile curves, uniformisationbased constructions, and fixed-level quantile dynamics. We also show how the proposed random– level construction may be interpreted through a dynamic fixed–point transport of quantiles. 

A fourth contribution is the development of interpretable parametric subclasses based on Tukey 

3 

quantile families. We specialise the general framework to the Tukey _g_ , _h_ , and _g_ - _h_ transformations, yielding quantile diffusions with direct parameter control over relative skewness and tail thickness. These families are especially well suited to risk modelling because they permit flexible heavy-tailed and asymmetric behaviour while remaining tractable for calibration and simulation. 

A fifth contribution is the development of a dynamic distortion framework induced by quantile diffusions. We show that the quantile transformation naturally induces a new probability measure whose marginals correspond to those of the transformed process. This provides a dynamic alternative to classical distortion pricing and links the framework to actuarial and financial applications involving skewness, heavy tails, and risk-sensitive valuation. Classical distortions such as the Wang transform arise as special cases of the false–law construction. 

Finally, the paper demonstrates the practical relevance of the framework through insurancefocused applications. These include distortion-based pricing, layer pricing under quantile-induced measure changes, and real-data actuarial illustrations in which quantile diffusions are calibrated to insurance cash-flow data for reserve-risk forecasting, capital assessment, and stop-loss pricing. 

The remainder of the paper is organised as follows. Section 2 introduces the random–level and function–valued constructions and establishes their main structural properties. Section 3 explains how these notions differ from classical definitions of quantile processes and quantiles of diffusions. Section 4 develops the constructive viewpoint through quantile transforms and a fixed–point interpretation. Section 5 specialises the framework to Tukey quantile diffusions. Section 6 presents applications to distortion pricing and insurance risk modelling. Empirical and synthetic insurance examples are given later in the paper, and technical proofs are collected in the appendix. 

## **1.2 Notation and definitions** 

We work on a filtered probability space � _Ω_ , _�_ , ( _�t_ ) _t≥_ 0, �� satisfying the usual conditions, and let _W_ = ( _Wt_ ) _t≥_ 0 be a one–dimensional standard Brownian motion adapted to ( _�t_ ) _t≥_ 0. All stochastic processes are assumed to be defined on this space unless stated otherwise. 

Throughout, for a real–valued random variable _X_ , we denote its distribution function, density function (when it exists), and quantile function by _FX_ , _fX_ , and _QX_ , respectively. If parameters are present, they are written after a semicolon, e.g. _FX_ ( _x_ ; _θ_ ), _QX_ ( _u_ ; _ξ_ ). 

We begin with the generalised inverse, which is the appropriate notion of inverse for monotone functions that may fail to be strictly increasing or continuous. 

**Definition 1.1** (Generalised inverse) **.** _Let F_ : � _→_ [ _−∞_ , _∞_ ] _be nondecreasing. Its generalised inverse F[−]_ : � _→_ [ _−∞_ , _∞_ ] _is defined by_ 

**==> picture [325 x 11] intentionally omitted <==**

_with the convention_ inf ∅ = _∞._ 

The following standard properties will be used repeatedly. 

**Proposition 1.1.** _Let F_ : � _→_ [0,1] _be nondecreasing and right–continuous, and let Q_ := _F[−] be its generalised inverse. Then:_ 

- _(i) Q is nondecreasing and left–continuous on_ (0,1] _._ 

- _(ii) For every u ∈_ [0,1] _,_ 

**==> picture [59 x 11] intentionally omitted <==**

- _(iii) For every x ∈_ � _,_ 

**==> picture [61 x 11] intentionally omitted <==**

4 

_(iv) For every x ∈_ � _and u ∈_ [0,1] _,_ 

**==> picture [132 x 11] intentionally omitted <==**

_Proof._ These are standard consequences of the definition of the infimum in (1.1). For completeness, we prove (iv), from which (ii) and (iii) follow immediately. 

Suppose first that _Q_ ( _u_ ) _≤ x_ . Since _F_ is nondecreasing, 

**==> picture [94 x 11] intentionally omitted <==**

where the last inequality follows from the definition of _Q_ ( _u_ ). 

Conversely, if _u ≤ F_ ( _x_ ), then _x ∈{z_ : _F_ ( _z_ ) _≥ u}_ , hence by definition of the infimum, 

**==> picture [133 x 11] intentionally omitted <==**

Thus (iv) holds. The monotonicity of _Q_ follows directly from the monotonicity of the level sets _{x_ : _F_ ( _x_ ) _≥ u}_ as _u_ varies, and left–continuity is a standard property of monotone generalised inverses. 

**Definition 1.2** (Quantile function) **.** _Let X be a real–valued random variable with distribution function FX_ : � _→_ [0,1] _. The quantile function of X is the generalised inverse_ 

**==> picture [143 x 13] intentionally omitted <==**

_We write_ � _for the class of all such quantile functions._ 

If _FX_ is continuous and strictly increasing on its support, then _QX_ = _FX[−]_[1] in the ordinary sense. A key device in what follows is the probability integral transform. 

**Proposition 1.2** (Probability integral transform) **.** _Let X be a real–valued random variable with continuous distribution function FX . Then the random variable_ 

**==> picture [53 x 11] intentionally omitted <==**

_is uniformly distributed on_ [0,1] _. Conversely, if U ∼_ Unif(0,1) _and QX is the quantile function of X, then_ 

**==> picture [55 x 16] intentionally omitted <==**

_Proof._ Since _FX_ is continuous and nondecreasing, for _u ∈_ [0,1], 

�( _U ≤ u_ ) = �( _FX_ ( _X_ ) _≤ u_ ) = �( _X ≤ QX_ ( _u_ )) = _FX_ ( _QX_ ( _u_ )) = _u_ , 

where the third equality follows from Proposition 1.1(iv), and the last equality uses continuity of _FX_ . Hence _U ∼_ Unif(0,1). 

Conversely, if _U ∼_ Unif(0,1), then for any _x ∈_ �, using Proposition 1.1(iv), 

**==> picture [184 x 12] intentionally omitted <==**

_d_ Thus _QX_ ( _U_ ) has distribution function _FX_ , i.e. _QX_ ( _U_ ) = _X_ . 

We next specify the class of target quantile maps used in the constructions. 

**Definition 1.3** (Admissible quantile family) **.** _Let Ξ ⊆_ � _[d] be a parameter space. A family {Qζ_ ( _·_ ; _ξ_ ) : _ξ ∈ Ξ} ⊂_ � _is called an_ admissible quantile family _if, for each ξ ∈ Ξ,_ 

- _(i) u �→ Qζ_ ( _u_ ; _ξ_ ) _is nondecreasing on_ [0,1] _;_ 

5 

_· (ii) Qζ_ ( ; _ξ_ ) _is finite on_ (0,1) _;_ 

_(iii) Qζ_ ( _·_ ; _ξ_ ) _is left–continuous on_ (0,1] _._ 

_If, in addition, Qζ_ ( _·_ ; _ξ_ ) _∈ C_[1] ((0,1)) _for each ξ, we call the family C_[1] _-admissible._ 

**Definition 1.4** (One–dimensional diffusion) **.** _An_ ( _�t_ ) _-adapted continuous process Y_ = ( _Yt_ ) _t≥_ 0 _is called a diffusion if it is a (weak or strong) solution of the stochastic differential equation_ 

**==> picture [339 x 12] intentionally omitted <==**

_where µ_ : �+ _×_ � _→_ � _and σ_ : �+ _×_ � _→_ � _are Borel measurable and satisfy conditions ensuring existence and uniqueness of a nonexplosive solution; see, for instance, [28]._ 

For 0 _≤ s < t_ and _x ∈_ �, we denote the transition distribution of _Y_ by 

**==> picture [213 x 12] intentionally omitted <==**

When _s_ = 0 and _Y_ 0 = _y_ 0 is deterministic, we write 

**==> picture [119 x 12] intentionally omitted <==**

for the time- _t_ marginal distribution function. If the marginal law admits a density, it is denoted by _fY_ ( _t_ , _·_ ). 

The random–level construction will require continuity and strict monotonicity of the marginal law. 

**Definition 1.5** (Regular diffusion law) **.** _We say that the marginal law of Y is_ regular on ( _t_ 0, _∞_ ) _, for some t_ 0 _≥_ 0 _, if for each t > t_ 0 _:_ 

- _(i) y �→ FY_ ( _t_ , _y_ ) _is continuous and strictly increasing on_ � _;_ 

_(ii) FY_ ( _t_ , _y_ ) _→_ 0 _as y →−∞ and FY_ ( _t_ , _y_ ) _→_ 1 _as y →∞._ 

Under Definition 1.5, the quantile function _QY_ ( _t_ , _·_ ) is well defined on [0,1], and the random variable 

**==> picture [68 x 12] intentionally omitted <==**

is uniformly distributed on [0,1] for every _t > t_ 0, by Proposition 1.2. 

## **2 A new class of quantile processes** 

We now introduce two constructions of continuous–time quantile processes. The first is a scalar– valued process obtained by evaluating a target quantile function at a random quantile level generated from a driving diffusion. The second is a function–valued process obtained by allowing the parameters of a quantile family to evolve stochastically through time. 

## **2.1 Construction I: Random–level quantile diffusions** 

The first construction transforms a driving diffusion into a process whose one–time marginals are determined by a prescribed quantile map. The terminology “random–level” refers to the fact that the quantile level itself is a stochastic process. 

We begin with a pathwise monotonicity property. 

6 

**Definition 2.1** (Random quantile level process) **.** _Let Y_ = ( _Yt_ ) _t≥_ 0 _be a diffusion with regular marginal law on_ ( _t_ 0, _∞_ ) _, and let_ 

**==> picture [124 x 11] intentionally omitted <==**

_Then U_ = ( _Ut_ ) _t>t_ 0 _is called the_ random quantile level process _associated with Y ._ 

**Proposition 2.1.** _For every t > t_ 0 _, Ut ∼_ Unif(0,1) _._ 

_Proof._ Immediate from Proposition 1.2 and Definition 1.5. 

**Definition 2.2** (Random–level quantile diffusion: true law) **.** _Let Y_ = ( _Yt_ ) _t≥_ 0 _be a diffusion with regular marginal law on_ ( _t_ 0, _∞_ ) _, and let {Qζ_ ( _·_ ; _ξ_ ) : _ξ ∈ Ξ} be an admissible quantile family. Fix ξ ∈ Ξ. The_ random–level quantile diffusion _associated with Y and Qζ_ ( _·_ ; _ξ_ ) _is the process Z_ = ( _Zt_ ) _t>t_ 0 _defined by_ 

**==> picture [330 x 15] intentionally omitted <==**

A more general version allows one to replace the true marginal law _FY_ by another family of distribution functions. 

**Definition 2.3** (Random–level quantile diffusion: false law) **.** _Let Y_ = ( _Yt_ ) _t≥_ 0 _be a diffusion with regular marginal law on_ ( _t_ 0, _∞_ ) _, and let F_ ( _t_ , _·_ ; _ϑ_ ) _be a family of continuous distribution functions on_ � _, indexed by ϑ ∈ Θ, such that for each t > t_ 0 _,_ 

**==> picture [136 x 14] intentionally omitted <==**

_Let {Qζ_ ( _·_ ; _ξ_ ) : _ξ ∈ Ξ} be an admissible quantile family. The_ false–law random–level quantile diffusion _is the process_ 

**==> picture [334 x 15] intentionally omitted <==**

In the true–law case, the input level _Ut_ is uniform at each _t_ , hence the output marginal law is exactly the law generated by _Qζ_ ( _·_ ; _ξ_ ). In the false–law case, the input level _U_[�] _t_ is generally not uniform, and the output marginal law is a pushforward of the law of _Yt_ through the map _y �→ Qζ_ ( _F_ ( _t_ , _y_ ; _ϑ_ ); _ξ_ ). 

The next theorem formalises these facts. 

**Theorem 2.1** (Marginal law in the true–law construction) **.** _Let Z be given by_ (2.1) _. Then for each t > t_ 0 _,_ 

**==> picture [38 x 17] intentionally omitted <==**

_where ζξ denotes a random variable with quantile function Qζ_ ( _·_ ; _ξ_ ) _. Equivalently, the marginal distribution function of Zt is_ 

_FZt_ ( _z_ ) = _Fζ_ ( _z_ ; _ξ_ ), _z ∈_ �, 

_independently of t._ 

_Proof._ By Proposition 2.1, _Ut ∼_ Unif(0,1) for each _t > t_ 0. Hence, by Proposition 1.2, 

**==> picture [95 x 17] intentionally omitted <==**

Therefore _FZt_ = _Fζ_ ( _·_ ; _ξ_ ). 

**Theorem 2.2** (Marginal law in the false–law construction) **.** _Let Z be given by_ (2.2) _. Then for each t > t_ 0 _,_ 

**==> picture [303 x 15] intentionally omitted <==**

_If Qζ_ ( _·_ ; _ξ_ ) _is nondecreasing, then_ 

**==> picture [302 x 15] intentionally omitted <==**

7 

_If, moreover, y �→ F_ ( _t_ , _y_ ; _ϑ_ ) _is strictly increasing, then_ 

**==> picture [297 x 15] intentionally omitted <==**

_where Q_ ( _t_ , _·_ ; _ϑ_ ) _is the quantile function associated with F_ ( _t_ , _·_ ; _ϑ_ ) _._ 

_Proof._ Equation (2.3) is just the definition of the distribution function of _Zt_ . Since _Qζ_ ( _·_ ; _ξ_ ) is the generalised inverse of _Fζ_ ( _·_ ; _ξ_ ), Proposition 1.1(iv) yields 

**==> picture [160 x 13] intentionally omitted <==**

for _v ∈_ [0,1], and therefore (2.4) follows. If _F_ ( _t_ , _·_ ; _ϑ_ ) is strictly increasing, then 

**==> picture [238 x 13] intentionally omitted <==**

which gives (2.5). 

The next result records pathwise order preservation. 

**Proposition 2.2** (Order preservation) **.** _Fix t > t_ 0 _. Let ω_ 1,..., _ωn ∈ Ω, and suppose_ 

**==> picture [120 x 13] intentionally omitted <==**

_If Qζ_ ( _·_ ; _ξ_ ) _is nondecreasing, then_ 

**==> picture [118 x 13] intentionally omitted <==**

_where Zt_ = _Qζ_ ( _Ut_ ; _ξ_ ) _. The same statement holds with Ut replaced by U_[�] _t in the false–law construction._ 

_Proof._ Immediate from monotonicity of _u �→ Qζ_ ( _u_ ; _ξ_ ). 

This gives a precise statement that the construction preserves samplewise order at each fixed time. 

**Proposition 2.3** (Adaptedness and continuity) **.** _Assume Y has continuous sample paths and Qζ_ ( _·_ ; _ξ_ ) _is continuous on_ [0,1] _. If FY_ ( _t_ , _y_ ) _is continuous jointly in_ ( _t_ , _y_ ) _, then the true–law process Zt_ = _Qζ_ ( _FY_ ( _t_ , _Yt_ ); _ξ_ ) _is adapted and has continuous sample paths on_ ( _t_ 0, _∞_ ) _. The same holds in the false– law case if F_ ( _t_ , _y_ ; _ϑ_ ) _is jointly continuous._ 

_Proof._ Since _Y_ is adapted and continuous, and _FY_ is jointly continuous, _t �→ FY_ ( _t_ , _Yt_ ) is adapted and continuous. Composition with the continuous function _Qζ_ ( _·_ ; _ξ_ ) preserves both properties. The false–law case is identical. 

A useful characterisation of dependence is obtained by copula invariance. 

**Proposition 2.4** (Copula invariance under monotone transforms) **.** _Assume Qζ_ ( _·_ ; _ξ_ ) _is strictly increasing and continuous on_ (0,1) _. Then, for any times t_ 1 _< ··· < tm, the copula of_ 

**==> picture [60 x 13] intentionally omitted <==**

_coincides with the copula of_ 

**==> picture [66 x 13] intentionally omitted <==**

_and hence, in the true–law construction, with the copula of_ 

**==> picture [62 x 13] intentionally omitted <==**

8 

_Proof._ The map _u �→ Qζ_ ( _u_ ; _ξ_ ) is strictly increasing, hence Sklar’s theorem and invariance of copulas under coordinatewise strictly increasing transformations apply. In the true–law case, _u �→ QY_ ( _t_ , _u_ ) is strictly increasing for each fixed _t_ , and _Yt_ = _QY_ ( _t_ , _Ut_ ), so the same invariance applies between _U_ and _Y_ . 

The next proposition gives the transition law of the transformed process. 

**Proposition 2.5** (Transition kernel by measurable pushforward) **.** _Let gt_ ( _y_ ) := _Qζ_ ( _FY_ ( _t_ , _y_ ); _ξ_ ) _in the true–law case, or gt_ ( _y_ ) := _Qζ_ ( _F_ ( _t_ , _y_ ; _ϑ_ ); _ξ_ ) _in the false–law case. Then for_ 0 _< s < t,_ 

**==> picture [337 x 30] intentionally omitted <==**

_If gt is nondecreasing and right–continuous, then_ 

**==> picture [176 x 15] intentionally omitted <==**

_where gt[−][denotes the generalised inverse of][g][t][.]_ 

_Proof._ Since _Zt_ = _gt_ ( _Yt_ ), for any Borel set _B ⊆_ �, 

**==> picture [202 x 14] intentionally omitted <==**

which gives (2.6). If _gt_ is nondecreasing, _{gt_ ( _y_ ) _≤ z}_ = _{ y ≤ gt[−]_[(] _[z]_[)] _[}]_[,][yielding the stated formula.] 

Under sufficient smoothness one can derive an SDE for the transformed process. 

**Proposition 2.6** (Itô dynamics of the true–law random–level process) **.** _Suppose FY ∈ C_[1,2] (( _t_ 0, _∞_ ) _×_ �) _, Qζ_ ( _·_ ; _ξ_ ) _∈ C_[2] ((0,1)) _, and Y solves_ (1.2) _. Let_ 

**==> picture [120 x 13] intentionally omitted <==**

_Then Zt_ = _h_ ( _t_ , _Yt_ ) _is a continuous semimartingale satisfying_ 

**==> picture [372 x 36] intentionally omitted <==**

_Moreover,_ 

**==> picture [326 x 31] intentionally omitted <==**

_Proof._ Since _h ∈ C_[1,2] , Itô’s formula gives (2.7). The derivative identities follow by the chain rule. 

Even in the true–law construction, _Z_ need not be time–homogeneous Markov with respect to its own filtration unless the map _h_ ( _t_ , _·_ ) is sufficiently invertible and regular. However, _Zt_ = _h_ ( _t_ , _Yt_ ) is always a measurable functional of a Markov process, and hence inherits a well defined transition structure via Proposition 2.5. 

One can interpret the resulting quantile process in two ways: (i) For a fixed time _t ∈_ [ _t_ 0, _∞_ ), and for each realisation _Y_ ( _t_ , _ω_ ) of the underlying driving process ( _Yt_ ), the random–level quantile diffusion, defined by either Eq. ( **??** ) or ( **??** ), is scalar–valued and corresponds to a single, fixed quantile level. (ii) The quantile diffusion may be viewed from a path–based perspective, where we observe scalar–valued sequences of quantiles corresponding to some sequence of quantile levels as time evolves. 

9 

**==> picture [317 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
Z ( t , ω 1)<br>Z ( t , ω 3)<br>Z ( t , ω 2)<br>u ∈ [0,1] u ∈ [0,1] u ∈ [0,1]<br>U ( t 1, ω 3) = 0.88 U ( t 2, ω 3) = 0.89 U ( t 3, ω 1) = 0.9<br>0.75 0.75 0.75<br>U ( t 2, ω 1) = 0.75 U ( t 3, ω 3) = 0.75<br>0.5 0.5 0.5<br>0.25 U ( t 1, ω 1) = 0.5 0.25 U ( t 2, ω 2) = 0.3 0.25 U ( t 3, ω 2) = 0.35<br>U ( t 1, ω 2) = 0.125<br>t 1 t 2 t 3<br>**----- End of picture text -----**<br>


Figure 1: Illustration of random-level quantile diffusion ( _Zt_ ). 

**==> picture [355 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
U ( t , ω )  ∈ [0,1]<br>0.85<br>0.71<br>0.57<br>0.540.52 U ( t , ω 2)<br>0.43<br>0.28 U ( t , ω 1)<br>0.24<br>0.08 U ( t , ω 2)<br>t 1 t 2 t 3 t ∈ [ t 0, ∞ )<br>Z ( t 1, ω ) =  Qζ ( U ( t 1, ω )) Z ( t 2, ω ) =  Qζ ( U ( t 2, ω )) Z ( t 3, ω ) =  Qζ ( U ( t 3, ω ))<br>0.28 0.71 0.85 0.24 0.52 0.57 U ( t 2, ω )  ∈ [0,1] 0.08 0.43 0.54 U ( t 3, ω )  ∈ [0,1]<br>U ( t 1, ω )  ∈ [0,1]<br>t 1 t 2 t 3<br>**----- End of picture text -----**<br>


Figure 2: Illustration of quantile level process ( _Ut_ ) and realisations thereof at times _t_ 1, _t_ 2, and _t_ 3. 

## **2.2 Construction II: Function–valued quantile diffusions** 

We now define a second class of quantile diffusions in which the entire quantile curve evolves stochastically through time. 

10 

**Definition 2.4** (Parameter diffusion) **.** _Let Ξ ⊆_ � _[d] be open. An Ξ-valued continuous adapted process ξ_ = ( _ξt_ ) _t≥_ 0 _is called a_ parameter diffusion _if it solves the d-dimensional SDE_ 

**==> picture [327 x 11] intentionally omitted <==**

_where B is an m-dimensional Brownian motion, b_ : �+ _× Ξ →_ � _[d] , and Σ_ : �+ _× Ξ →_ � _[d][×][m] , under conditions that ensure existence and uniqueness of a nonexplosive solution._ 

**Definition 2.5** (Function–valued quantile diffusion) **.** _Let {Qζ_ ( _·_ ; _ξ_ ) : _ξ ∈ Ξ} be an admissible quantile family, and let ξ_ = ( _ξt_ ) _t≥_ 0 _be a parameter diffusion taking values in Ξ. The_ function–valued quantile diffusion _is the process_ 

**==> picture [297 x 13] intentionally omitted <==**

_Thus each Zt is itself a quantile function._ 

**Proposition 2.7** (Well posedness in the quantile space) **.** _For each t ≥_ 0 _, Zt ∈_ � _almost surely. If u �→ Qζ_ ( _u_ ; _ξ_ ) _∈ C[k]_ ((0,1)) _for every ξ ∈ Ξ, then u �→ Zt_ ( _u_ ) _∈ C[k]_ ((0,1)) _almost surely for every t ≥_ 0 _._ 

_Proof._ For each fixed _t_ , _ξt_ ( _ω_ ) _∈ Ξ_ , hence _u �→ Zt_ ( _ω_ , _u_ ) = _Qζ_ ( _u_ ; _ξt_ ( _ω_ )) is a quantile function by Definition 1.3. The smoothness statement is immediate. 

**Proposition 2.8** (Measurability and adaptedness) **.** _Assume_ ( _u_ , _ξ_ ) _�→ Qζ_ ( _u_ ; _ξ_ ) _is Borel measurable on_ [0,1] _× Ξ. Then_ ( _t_ , _ω_ , _u_ ) _�→ Zt_ ( _ω_ , _u_ ) _is jointly measurable. For each fixed u ∈_ [0,1] _, the scalar process_ ( _Zt_ ( _u_ )) _t≥_ 0 _is_ ( _�t_ ) _-adapted._ 

_Proof._ Joint measurability follows from measurability of ( _t_ , _ω_ ) _�→ ξt_ ( _ω_ ) and composition with the Borel map _Qζ_ . Adaptedness for fixed _u_ is immediate. 

If the quantile family is smooth in the parameter, each fixed- _u_ process is an Itô diffusion. 

**Proposition 2.9** (Itô dynamics at fixed quantile level) **.** _Assume_ ( _u_ , _ξ_ ) _�→ Qζ_ ( _u_ ; _ξ_ ) _is C_[2] _in ξ for each fixed u ∈_ (0,1) _, and let ξ solve_ (2.8) _. Then for each fixed u ∈_ (0,1) _, the scalar process Zt_ ( _u_ ) = _Qζ_ ( _u_ ; _ξt_ ) _satisfies_ 

**==> picture [391 x 37] intentionally omitted <==**

_Proof._ Apply multidimensional Itô’s formula to the map _ξ �→ Qζ_ ( _u_ ; _ξ_ ). 

The function–valued construction may be viewed as a stochastic process taking values in a function space. 

**Proposition 2.10** (Continuity in function norm) **.** _Assume Ξ ∋ ξ �→ Qζ_ ( _·_ ; _ξ_ ) _∈ C_ ([0,1]) _is continuous with respect to the supremum norm, and assume t �→ ξt has continuous sample paths. Then t �→ Zt has continuous sample paths as a C_ ([0,1]) _-valued process._ 

_Proof._ Let _tn → t_ . Since _ξtn → ξt_ almost surely and _ξ �→ Qζ_ ( _·_ ; _ξ_ ) is continuous into _C_ ([0,1]), 

**==> picture [226 x 20] intentionally omitted <==**

almost surely. 

11 

## **2.3 Link between the two constructions of quantile diffusions** 

The two constructions are conceptually distinct. In the random–level construction, the process is scalar–valued and the randomness enters through the quantile level. In the function–valued construction, each time point yields an entire quantile curve. Nevertheless, one obtains a natural link by evaluating a function–valued quantile diffusion at a fixed quantile level. 

**Definition 2.6** (Fixed–level section of a function–valued quantile diffusion) **.** _Let Zt_ ( _u_ ) = _Qζ_ ( _u_ ; _ξt_ ) _be a function–valued quantile diffusion, and fix u_ ¯ _∈_ [0,1] _. The associated_ fixed–level section _is the scalar process_ 

**==> picture [306 x 15] intentionally omitted <==**

**Proposition 2.11.** _Under the assumptions of Proposition 2.9, Z[u]_[¯] _is a continuous semimartingale satisfying_ (2.9) _with u_ = ¯ _u._ 

_Proof._ Immediate from Proposition 2.9. 

One can feed this fixed–level process through a second quantile transform. 

**Definition 2.7** (Induced random–level transform of a fixed section) **.** _Let Z[u]_[¯] _be given by_ (2.10) _. Let F_ ( _t_ , _·_ ; _ϑ_ ) _be a family of continuous distribution functions on_ � _, and let Qζ_ �( _·_ ; _ξ_[�] ) _be an admissible quantile family. Define_ 

**==> picture [305 x 17] intentionally omitted <==**

This is not a new construction in itself, but a composition of the function–valued construction with a scalar random–level transform. 

**Proposition 2.12** (Overlap of the two constructions) **.** _Let Zt_ ( _u_ ) = _Qζ_ ( _u_ ; _ξt_ ) _be a function–valued quantile diffusion and fix u_ ¯ _∈_ [0,1] _. Then the scalar process Z_[�] _defined by_ (2.11) _is a random–level quantile diffusion driven by the scalar semimartingale Z[u]_[¯] _. Conversely, every fixed–level section Z[u]_[¯] _of a function–valued quantile diffusion is a scalar quantile process, but in general it is not itself a random– level quantile diffusion of the form_ (2.1) _unless there exists a diffusion Y and a family of marginal laws FY_ ( _t_ , _·_ ) _such that_ 

**==> picture [164 x 15] intentionally omitted <==**

_Proof._ The first claim follows directly from Definition 2.3, taking the driver to be the scalar process _Z[u]_[¯] and the distribution family to be _F_ ( _t_ , _·_ ; _ϑ_ ). The converse statement is immediate: a fixed–level section is always scalar, but representability in the form (2.1) requires existence of a suitable uniformising diffusion representation, which need not hold in general. 

The essential distinction is geometric: at each fixed time _t_ , the random–level construction takes values in �, while the function–valued construction takes values in a subset of �, viewed as a function space. Accordingly, the two constructions should be regarded as complementary rather than equivalent. 

## **2.4 Additional structural results and extensions** 

For later use, we record two additional results that clarify the role of the target quantile family. 

**Proposition 2.13** (Moment transfer in the true–law construction) **.** _Let Z be given by_ (2.1) _, and suppose ζξ has finite p-th moment for some p ≥_ 1 _. Then for every t > t_ 0 _,_ 

**==> picture [74 x 13] intentionally omitted <==**

_In particular, all one–time moments of Zt , whenever finite, are determined entirely by the target quantile family and not by the driving diffusion._ 

12 

_d Proof._ By Theorem 2.1, _Zt_ = _ζξ_ for each _t_ . Hence all finite moments coincide. 

**Proposition 2.14** (Conditional quantile representation) **.** _Let Zt_ = _Qζ_ ( _FY_ ( _t_ , _Yt_ ); _ξ_ ) _be a true–law random–level quantile diffusion. For_ 0 _< s < t, define the conditional distribution function_ 

**==> picture [132 x 13] intentionally omitted <==**

_Then_ 

**==> picture [284 x 15] intentionally omitted <==**

_provided ht is nondecreasing and admits a generalised inverse h[−] t[.]_ 

_Proof._ Since _Y_ is Markov, 

**==> picture [158 x 11] intentionally omitted <==**

The claim now follows exactly as in Proposition 2.5. 

An important extension is to allow time–dependent target parameters. 

**Definition 2.8** (Time–inhomogeneous random–level quantile diffusion) **.** _Let ξ_ : [ _t_ 0, _∞_ ) _→ Ξ be deterministic and measurable. A_ time–inhomogeneous random–level quantile diffusion _is defined by_ 

**==> picture [167 x 13] intentionally omitted <==**

_If ξt is itself stochastic and adapted, one obtains a hybrid model combining the random–level and function–valued constructions:_ 

**==> picture [158 x 13] intentionally omitted <==**

**Remark 1.** _The hybrid model permits simultaneous stochastic variation in the quantile level and in the shape of the target quantile family. It therefore provides a natural route to dynamic skewness and kurtosis modulation beyond the stationary marginal setting of Theorem 2.1._ 

## **3 Relation to classical notions of quantile processes and quantile diffusions** 

In this section we make precise the manner in which the two constructions introduced in Sections 2.1 and 2.2 differ from the classical notions of quantile processes, dynamic quantiles, and quantiles associated with diffusion models. The distinction is important because the terminology _quantile process_ has been used in several mathematically different ways in statistics, econometrics, probability, and stochastic analysis. Our purpose here is to isolate the precise object studied in this paper and to clarify why the proposed constructions are genuinely new. 

## **3.1 Classical notions** 

We begin by fixing three standard notions appearing in the literature. 

**Definition 3.1** (Classical deterministic quantile curve of a stochastic process) **.** _Let X_ = ( _X t_ ) _t≥_ 0 _be a real–valued stochastic process such that, for each t ≥_ 0 _, the marginal law of X t admits distribution function FX t . The associated_ classical deterministic quantile curve _at level u ∈_ [0,1] _is the deterministic function_ 

**==> picture [134 x 15] intentionally omitted <==**

For fixed _u_ , the map _t �→ qX_ ( _t_ ; _u_ ) is not, in general, a stochastic process on ( _Ω_ , _�_ , �); it is a deterministic function of time obtained from the one–time marginals of _X_ . 

13 

**Definition 3.2** (Classical fixed–level quantile process) **.** _Let X_ = ( _X t_ ) _t≥_ 0 _be as above, and fix u ∈_ [0,1] _. Any process of the form_ 

**==> picture [165 x 17] intentionally omitted <==**

_is called a_ fixed–level quantile process _associated with X._ 

Despite the terminology, _Q_[(] _t[u]_[)] is deterministic once the law of _X t_ is known. The randomness lies in the underlying process _X_ , not in the quantile trajectory _t �→ qX_ ( _t_ ; _u_ ). In particular, this object does not define a new stochastic process adapted to the filtration of _X_ . 

**Definition 3.3** (Quantile of a diffusion at fixed time or over a path) **.** _Let Y_ = ( _Yt_ ) _t≥_ 0 _be a diffusion. There are two standard quantile objects associated with Y :_ 

- _(i) the_ marginal quantile curve 

**==> picture [105 x 11] intentionally omitted <==**

_where FY_ ( _t_ , _·_ ) _is the law of Yt ;_ 

- _(ii) the quantile of a path functional, e.g. the u-quantile of the random set {Ys_ : 0 _≤ s ≤ t}, or of a derived random variable such as a running maximum, occupation time, or empirical path quantile._ 

In both cases above, one starts with an already specified diffusion _Y_ and then studies a quantile object _induced by Y_ . The quantile is therefore a derived feature of the model, not the primitive modelling object. 

## **3.2 What is classical and what is new** 

The following proposition isolates the key distinction between the classical fixed–level notion and the random–level construction. 

**Proposition 3.1.** _Let Y_ = ( _Yt_ ) _t≥_ 0 _be a diffusion with regular marginal law, and let_ 

**==> picture [86 x 11] intentionally omitted <==**

_denote its classical marginal quantile curve. Fix u ∈_ [0,1] _. Then_ 

**==> picture [62 x 12] intentionally omitted <==**

_is deterministic. By contrast, the random–level quantile diffusion_ 

**==> picture [95 x 13] intentionally omitted <==**

_is a genuine scalar stochastic process adapted to_ ( _�t_ ) _._ 

_Proof._ For fixed _u_ , the function _qY_ ( _t_ ; _u_ ) depends only on the marginal law _FY_ ( _t_ , _·_ ), hence is deterministic. On the other hand, _Zt_ is a measurable function of _Yt_ , namely 

**==> picture [201 x 13] intentionally omitted <==**

and is therefore an ( _�t_ )-adapted random variable for each _t_ . 

This distinction is fundamental. Our random–level quantile diffusion is not “the quantile of a diffusion” in the classical sense; rather, it is a _new diffusion–driven stochastic model constructed in quantile space_ . The quantile level is itself random and evolves through time through the process 

**==> picture [70 x 11] intentionally omitted <==**

14 

The next proposition clarifies the relation between the function–valued construction and classical quantile curves. 

**Proposition 3.2.** _Let Zt_ ( _u_ ) = _Qζ_ ( _u_ ; _ξt_ ) _be a function–valued quantile diffusion. Then for each fixed t, u �→ Zt_ ( _u_ ) _is a random quantile function. By contrast, for a classical process X, the curve u �→ qX_ ( _t_ ; _u_ ) _is deterministic for each fixed t._ 

_Proof._ For fixed _t_ , _Zt_ ( _·_ ) depends on the random parameter vector _ξt_ , hence is random as an element of the function space �. In contrast, _qX_ ( _t_ ; _u_ ) = _FX[−] t_[(] _[u]_[)][ is fully determined by the law of] _[ X][ t]_[, hence is] deterministic. 

Thus the function–valued construction is not merely a reparameterisation of the classical marginal quantile curve of some pre–existing process. Instead, it is a stochastic process _taking values in a space of quantile functions_ . This is conceptually different from the classical situation in which the quantile curve is a deterministic summary of a model. 

## **3.3 Quantile as descriptor versus quantile as primitive** 

A useful way to formalise the distinction is to separate _descriptor quantiles_ from _constructive quantiles_ . 

**Definition 3.4** (Descriptor quantile model) **.** _A_ descriptor quantile model _is one in which a stochastic process X_ = ( _X t_ ) _is specified first, and the quantile function is then defined by_ 

**==> picture [78 x 14] intentionally omitted <==**

_or by a quantile functional of X._ 

**Definition 3.5** (Constructive quantile model) **.** _A_ constructive quantile model _is one in which a quantile map or quantile family is specified as a primitive modelling object, and a stochastic process is then constructed from it._ 

**Proposition 3.3.** _The random–level quantile diffusion and the function–valued quantile diffusion introduced in this paper are constructive quantile models. Classical fixed–level quantile curves of stochastic processes are descriptor quantile models._ 

_Proof._ In the random–level construction one specifies a target quantile family _Qζ_ ( _·_ ; _ξ_ ) and constructs 

**==> picture [98 x 13] intentionally omitted <==**

In the function–valued construction one specifies a stochastic parameter process _ξt_ and constructs 

**==> picture [77 x 13] intentionally omitted <==**

Hence in both cases the quantile map is primitive. 

By contrast, in the classical case one first specifies _X_ , then defines _qX_ ( _t_ ; _u_ ) = _FX[−] t_[(] _[u]_[)][,][so][the] quantile is a descriptor derived from _X_ . 

The constructive viewpoint is the main conceptual novelty of the present paper. It permits one to prescribe directly the shape, skewness, and tail properties of the resulting model through a target quantile family, rather than attempting to recover these properties indirectly from a postulated density or SDE. 

15 

## **3.4 Comparison with uniformisation-based results for diffusions** 

Classical diffusion theory contains the well–known probability integral transform (or uniformisation) 

**==> picture [68 x 11] intentionally omitted <==**

which converts the one–time marginals of a diffusion into a uniform random variable on [0,1] for each fixed _t_ . However, using _Ut_ as an intermediate object is not in itself the same as constructing a quantile diffusion. 

**Proposition 3.4.** _Let Y be a diffusion with regular marginal law and define Ut_ = _FY_ ( _t_ , _Yt_ ) _. Then Ut ∼_ Unif(0,1) _for each t, but U_ = ( _Ut_ ) _is not, by itself, a quantile diffusion in the sense of this paper. It becomes one only after composition with a target quantile function:_ 

**==> picture [70 x 13] intentionally omitted <==**

_Proof._ The uniformity of _Ut_ follows from the probability integral transform. However, _Ut_ takes values in [0,1] and represents a stochastic _quantile level_ , not a quantile value in the target state space. Only after application of _Qζ_ ( _·_ ; _ξ_ ) does one obtain a process whose marginals are governed by the target quantile family. 

This is another point of novelty: the uniformised process _Ut_ is not the end object but the mechanism that transports the serial dependence of the driving diffusion into the target quantile model. 

## **3.5 Comparison with quantile diffusion equations in the classical sense** 

In some areas of the literature, one studies evolution equations satisfied by a deterministic quantile curve _q_ ( _t_ , _u_ ), often obtained by transforming a Fokker– Planck equation or continuity equation. Such equations describe how the quantiles of the law of an already specified process evolve. 

Our framework is different. 

**Proposition 3.5.** _Suppose qY_ ( _t_ , _u_ ) = _FY_ ( _t_ , _·_ ) _[−]_ ( _u_ ) _is the classical marginal quantile curve of a diffusion Y . Then qY is a deterministic object governed, when sufficient smoothness holds, by an equation derived from the marginal law of Y . By contrast:_ 

- _(i) the random–level quantile diffusion Zt_ = _Qζ_ ( _FY_ ( _t_ , _Yt_ ); _ξ_ ) _is a scalar stochastic process;_ 

_(ii) the function–valued quantile diffusion Zt_ ( _u_ ) = _Qζ_ ( _u_ ; _ξt_ ) _is a random field in_ ( _t_ , _u_ ) _._ 

_Hence neither construction coincides with the classical deterministic quantile evolution equation._ 

_Proof._ The first statement is standard: _qY_ is determined by the law of _Yt_ and therefore deterministic. Statements (i) and (ii) follow from the definitions of the two constructions. 

Accordingly, our notion of “quantile diffusion” should not be confused with a PDE or integro– PDE for a deterministic quantile curve. Here, the quantile object itself is random. 

## **3.6 Precise distinctions between the two proposed constructions and classical definitions** 

We summarise the mathematical distinctions. 

**Theorem 3.1** (Structural distinctions) **.** _Let Y be a diffusion with regular marginal law, let Qζ_ ( _·_ ; _ξ_ ) _be an admissible quantile family, and let ξt be a parameter diffusion. Then:_ 

16 

- _(i) The classical fixed–level quantile qY_ ( _t_ ; _u_ ) _is deterministic for fixed u, whereas the random–level process_ 

   - _Zt_[RL] := _Qζ_ ( _FY_ ( _t_ , _Yt_ ); _ξ_ ) 

_is stochastic._ 

- _(ii) The classical one–time quantile curve u �→ qY_ ( _t_ ; _u_ ) _is deterministic for fixed t, whereas the function–valued process_ 

   - _Zt_[FV][(] _[u]_[)][ :][=] _[ Q][ζ]_[(] _[u]_[;] _[ξ][t]_[)] 

_is random as a function of u._ 

- _(iii) Classical quantile objects are derived from a pre–specified process, whereas Z_[RL] _and Z_[FV] _are constructed from a target quantile family and a driving mechanism._ 

- _(iv) In the random–level construction, serial dependence is inherited from the driving process through the random level Ut_ = _FY_ ( _t_ , _Yt_ ) _; in the classical fixed–level setting there is no such stochastic quantile–level dynamics._ 

- _(v) In the function–valued construction, the entire quantile curve evolves via the stochastic parameter vector ξt , which has no analogue in the classical deterministic marginal quantile curve._ 

_Proof._ Items (i)–(iii) follow from Propositions 3.1, 3.2, and 3.3. Item (iv) follows from the definition _Ut_ = _FY_ ( _t_ , _Yt_ ), which is stochastic unless _Yt_ is degenerate. Item (v) follows from the randomness of _ξt_ . 

## **3.7 Motivations for the new constructions** 

The preceding distinctions are not merely terminological; they motivate the new framework mathematically and practically. 

[Motivation for the random–level construction] The random–level construction is useful when one seeks a scalar stochastic process with prescribed one–time marginal law, but with dependence inherited from an auxiliary diffusion. The model 

**==> picture [95 x 13] intentionally omitted <==**

achieves exactly this in the true–law case: the target quantile family determines the marginal law, while the driving diffusion determines the serial structure. 

[Motivation for the function–valued construction] The function–valued construction is useful when the object of interest is not a single quantile level but the entire quantile curve and its dynamics. By letting _ξt_ evolve stochastically, one may model time–varying skewness, scale, and tail behaviour directly in the quantile representation. 

[Why classical definitions are insufficient] Classical definitions describe quantiles _of_ a process, but they do not provide a constructive mechanism for building new stochastic models directly in quantile space. In particular, they do not separate in a transparent way: 

- (a) marginal distributional shape, 

- (b) serial dependence, 

- (c) dynamic deformation of skewness and kurtosis, 

- (d) stochastic evolution of the entire quantile curve. 

The two constructions introduced in this paper address these modelling goals explicitly. The main point may therefore be stated succinctly as follows. 

17 

**Remark 2** (Conceptual summary) **.** _Classically, one starts with a stochastic process and then computes its quantiles. In the present paper, one starts with a quantile family and then constructs a stochastic process from it. This reversal of modelling order is the essential novelty behind both the random–level quantile diffusion and the function–valued quantile diffusion._ 

## **4 Constructive models** 

This section gives the modelling perspective underlying the proposed quantile diffusions. We first recall the class of quantile transforms that motivate the construction and then show how the same idea leads naturally to a dynamic fixed-point interpretation. The key point is that we do not begin with a target density and then derive its quantiles; instead, we specify a quantile map and use it to construct a new stochastic model. 

## **4.1 Quantile transforms and rank transmutation maps** 

A useful starting point is the class of rank transmutation maps (RTMs), which provide a flexible way to transform one distribution into another directly through quantile composition; see [31, 16]. RTMs and related quantile-based maps motivate our construction because, at each fixed time, the random-level quantile diffusion is obtained by the same type of distribution–quantile composition, but now applied to the marginals of a stochastic process. 

**Definition 4.1** (Rank transmutation map) **.** _Let F_ 1 _and F_ 2 _be distribution functions on a common state space, with generalised inverses F_ 1 _[−][and][F]_ 2 _[−][.][The associated rank transmutation maps are]_ 

**==> picture [366 x 16] intentionally omitted <==**

_Under continuity and strict monotonicity of F_ 1 _and F_ 2 _, the maps GR_ 12 _and GR_ 21 _are mutual inverses, each mapping_ [0,1] _onto_ [0,1] _._ 

The appeal of RTMs is that they separate the _base law_ from the _target deformation_ . This is precisely the philosophy of the random-level construction in Section 2.1: the driving diffusion supplies the serial dependence, while the target quantile family controls the one-time marginal shape. 

A particularly important family of quantile transforms for our purposes is given by the Tukey elongation maps, which allow one to introduce skewness and tail-thickening relative to a base distribution, usually Gaussian. 

**Definition 4.2** (Elongation transform) **.** _A function T_ : � _→_ �+ _is called an elongation transform if it is even, satisfies_ 

**==> picture [141 x 11] intentionally omitted <==**

_and is such that T[′]_ ( _w_ ) _>_ 0 _and T[′′]_ ( _w_ ) _≥_ 0 _for w >_ 0 _._ 

**Definition 4.3** (Tukey transform) **.** _Let W be a real-valued random variable with quantile function QW , and let T be an elongation transform. For parameters A ∈_ � _, B >_ 0 _, and θ ∈_ � _, define_ 

**==> picture [98 x 13] intentionally omitted <==**

_Then the quantile function of X is_ 

**==> picture [221 x 17] intentionally omitted <==**

Important special cases are obtained by choosing 

**==> picture [258 x 24] intentionally omitted <==**

18 

which respectively induce relative skewness, tail-thickening, and polynomial tail deformation. In this paper we focus on the _g_ -, _h_ -, and _g_ - _h_ families because they yield tractable and interpretable quantile diffusions. 

At each fixed time _t_ , the random-level construction _Zt_ = _Qζ_ ( _FY_ ( _t_ , _Yt_ ); _ξ_ ) is a dynamic counterpart of the static map _Qζ_ ( _U_ ), with _U ∼_ Unif(0,1). Thus the proposed quantile diffusions may be viewed as continuous-time stochastic analogues of quantile transformation maps such as RTMs. 

Although our main focus is on diffusions, the constructive principle is not limited to continuous paths. If the driving process has jumps and admits sufficiently regular marginals, the same distribution–quantile composition can be used to build quantile processes with jumps. 

## **4.2 A fixed-point interpretation** 

Quantiles are naturally characterised as solutions of fixed-point equations. This viewpoint provides a concise interpretation of the proposed construction: a quantile transformation maps one fixedpoint problem into another. 

**Definition 4.4** (Quantile as a fixed point) **.** _Let X be a real-valued random variable with continuous distribution function FX . For u ∈_ (0,1) _, a point η ∈_ � _is the u-quantile of X if_ 

**==> picture [250 x 12] intentionally omitted <==**

_If FX is strictly increasing in a neighbourhood of η, then η is uniquely determined and equals QX_ ( _u_ ) _._ 

The classical Bahadur representation shows that sample quantiles asymptotically solve the same fixed-point problem; see [3, 21]. We use this only as motivation: the important point here is that quantile maps preserve the structure of such equations. 

**Definition 4.5** (Composite fixed-point problem) **.** _Let Y and Z be real-valued random variables with continuous distribution functions FY and FZ , and let m_ : � _→_ � _be measurable. We say that m links the quantile problems for Y and Z if for some u ∈_ (0,1) _,_ 

**==> picture [300 x 15] intentionally omitted <==**

The canonical choice of such a map is the quantile transport 

**==> picture [90 x 12] intentionally omitted <==**

in which case _m_ ( _QY_ ( _u_ )) = _Q Z_ ( _u_ ). This is the static version of the random-level construction introduced in Section 2.1. 

In continuous time, the same idea applies pointwise in _t_ : if _Yt_ has marginal law _FY_ ( _t_ , _·_ ) and _mt_ ( _x_ ) = _Qζ_ ( _FY_ ( _t_ , _x_ ); _ξ_ ), then 

**==> picture [139 x 13] intentionally omitted <==**

solves the transformed fixed-point problem at every time _t_ . In the true-law case, this ensures that the marginal law of _Zt_ is exactly the target law induced by _Qζ_ ( _·_ ; _ξ_ ), as shown in Theorem 2.1. 

The fixed-point viewpoint clarifies the role of the construction. The driving process _Y_ is not itself the target model. Rather, it provides a dynamically evolving random level _Ut_ = _FY_ ( _t_ , _Yt_ ), and the target quantile map then converts this level into the quantile diffusion _Zt_ . 

19 

## **4.3 SDE verification and well-posedness** 

Whenever the composite map is sufficiently smooth, the quantile diffusion satisfies an Itô SDE obtained from Proposition 2.6. For the true-law construction, 

**==> picture [198 x 13] intentionally omitted <==**

and thus _Z_ is a continuous semimartingale with drift and volatility determined jointly by the driving coefficients ( _µ_ , _σ_ ), the marginal law _FY_ , and the target quantile family _Qζ_ . 

The verification of existence and uniqueness for the resulting SDE is important because the transformed coefficients need not inherit the standard regularity of the driving diffusion automatically. In particular, quantile maps designed to introduce skewness or heavy tails can generate nonlinear coefficients with restricted state spaces or rapidly varying derivatives. For this reason, the relevant local Lipschitz and growth conditions are checked in the appendix for the specific Tukey families considered below. 

Two cases are of practical interest: 

- (i) _Closed-form transformed SDEs._ For several choices of driver and quantile map, the transformed drift and diffusion coefficients can be written explicitly. 

- (ii) _Implicit but well-posed quantile diffusions._ Even when a closed-form solution is unavailable, the process remains well defined once weak or strong existence and uniqueness are established. In such cases, simulation and likelihood-free calibration remain feasible. 

This balance between explicit structure and modelling flexibility is one of the main advantages of the constructive approach. 

## **5 Tukey quantile diffusions** 

We now specialise the general framework to the Tukey family. These models are especially attractive in insurance and risk management because their parameters admit direct interpretation in terms of location, scale, skewness, and tail thickness. Throughout, let _xu_ = _Φ[−]_[1] ( _u_ ) denote the standard normal quantile. 

## **5.1 The Tukey** _g_ **-** _h_ **family** 

The most flexible specification considered in this paper is the Tukey _g_ - _h_ family. 

**Definition 5.1** (Tukey _g_ - _h_ quantile function) **.** _For parameters A ∈_ � _, B >_ 0 _, g ∈_ � _, and h ≥_ 0 _, define_ 

**==> picture [356 x 27] intentionally omitted <==**

_with the usual continuous extension at g_ = 0 _, namely_ 

**==> picture [84 x 26] intentionally omitted <==**

The parameter _g_ controls asymmetry, while _h_ controls tail-thickening relative to the Gaussian base. This makes the family particularly useful for modelling heavy-tailed and skewed loss distributions. 

**Definition 5.2** (Random-level Tukey _g_ - _h_ quantile diffusion) **.** _A random-level Tukey g-h quantile diffusion is a process of the form_ 

**==> picture [111 x 14] intentionally omitted <==**

20 

_where Ut is the random quantile level process from Definition 2.1 or, more generally, its false-law analogue._ 

Under the smoothness assumptions of Proposition 2.6, the process _Z_ satisfies an Itô SDE. The resulting coefficients are obtained by substituting _Qφgh_ into the general chain-rule representation. We do not repeat the full expressions here; they are recorded in the appendix together with sufficient conditions for weak and strong well-posedness. 

In general, the Tukey _g_ - _h_ quantile diffusion does not admit a closed-form solution. This is not a limitation of the framework: the model remains well posed under standard existence and uniqueness conditions, and simulation is straightforward via the underlying driving process together with the quantile map. 

## **5.2 The Tukey** _g_ **family** 

The _g_ -subfamily isolates relative skewness. 

**Definition 5.3** (Tukey _g_ quantile function) **.** _For parameters A ∈_ � _, B >_ 0 _, and g ∈_ � _, define_ 

**==> picture [221 x 26] intentionally omitted <==**

_again with the continuous limit Qφg_ ( _u_ ; _A_ , _B_ ,0) = _A_ + _Bxu._ 

Positive values of _g_ induce right skewness, while negative values induce left skewness. Figure 3 shows the deformation relative to the standard normal quantile. 

**==> picture [352 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
30<br>g=0.3<br>0<br>g=0.8<br>20 g=1.5<br>g=3 − 10<br>N(0,1)<br>g=-0.3<br>10<br>g=-0.8<br>− 20 g=-1.5<br>g=-3<br>0<br>N(0,1)<br>− 30<br>0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1<br>u u<br>) )<br> g  g<br>; ;<br>u u<br>( (<br>g g<br>φ φ<br>Q Q<br>**----- End of picture text -----**<br>


Figure 3: _g_ -transform quantile functions for positive and negative values of _g_ , relative to the standard normal quantile. 

**Definition 5.4** (Random-level Tukey _g_ quantile diffusion) **.** _A random-level Tukey g quantile diffusion is given by_ 

**==> picture [97 x 15] intentionally omitted <==**

_where Ut is the random quantile level process associated with the chosen driver._ 

This model is particularly useful when the aim is to preserve the dependence structure of the driver while introducing controlled asymmetry into the marginal law. Closed-form transformed coefficients are available for several standard drivers; these are collected in the appendix. 

Two examples are especially simple. 

**Skewed GBM-type quantile diffusion.** If the driver is geometric Brownian motion, the transformed process yields a multiplicative skew deformation of the lognormal quantile structure. 

21 

**Skewed OU quantile diffusion.** If the driver is Ornstein–Uhlenbeck, the transformed process yields a mean-reverting skewed quantile diffusion, suitable when one seeks asymmetric deviations around a long-run level. 

These examples illustrate a general theme: the driver determines temporal structure, while the Tukey map controls marginal asymmetry. 

## **5.3 The Tukey** _h_ **family** 

The _h_ -subfamily isolates tail-thickening. 

**Definition 5.5** (Tukey _h_ quantile function) **.** _For parameters A ∈_ � _, B >_ 0 _, and h ≥_ 0 _, define_ 

**==> picture [204 x 21] intentionally omitted <==**

Here _h_ increases kurtosis relative to the Gaussian base while preserving symmetry. For _h <_ 0, monotonicity can fail, so we restrict attention to _h ≥_ 0. Figure 4 illustrates the effect of varying _h_ . 

**==> picture [384 x 176] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 2<br>h=0.05<br>h=0.1<br>1<br>10 h=0.6<br>h=1<br>0<br>N(0,1)<br>0<br>h=-0.05<br>− 1<br>h=-0.1<br>− 10 h=-0.6<br>− 2 h=-1<br>N(0,1)<br>− 20 − 3<br>0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1<br>u u<br>) )<br>h h<br>; ;<br>u u<br>( (<br>Q Q<br>**----- End of picture text -----**<br>


Figure 4: _h_ -transform quantile functions relative to the standard normal quantile for several values of _h_ . 

**Definition 5.6** (Random-level Tukey _h_ quantile diffusion) **.** _A random-level Tukey h quantile diffusion is given by_ 

**==> picture [96 x 13] intentionally omitted <==**

_where Ut is the random quantile level process associated with the chosen driver._ 

This family is useful when one wishes to retain a symmetric centre while increasing the probability of extreme events. In actuarial and financial applications, it therefore provides a natural way to model heavy-tailed losses or returns without imposing asymmetry. 

## **5.4 Summary of the Tukey construction** 

The Tukey families provide a parsimonious parametric class for the proposed quantile diffusions: 

- _A_ shifts the location; 

- _B_ rescales the process; 

- _g_ governs relative skewness; 

22 

- _h_ governs relative tail-thickening. 

This interpretation is one of the main modelling advantages of the framework. The same driving diffusion can be combined with different Tukey maps to generate families of processes with identical serial dependence but materially different one-time risk characteristics. 

## **6 Application to distortion pricing** 

We now give a brief application to distortion-based pricing. The aim is not to replace the classical distortion literature, but to show that quantile diffusions provide a dynamic and interpretable route to measure changes that reflect skewness and tail risk directly. 

## **6.1 Classical distortion operators** 

Let _X_ be a financial or insurance risk under a reference measure �, with distribution function _FX_[�][.] A distortion operator is an increasing map _ν_ : [0,1] _→_ [0,1] satisfying _ν_ (0) = 0 and _ν_ (1) = 1. Applying _ν_ to _FX_[�][or][to][the][survival][function][produces][a][distorted][law][and][hence][a][risk-adjusted] price. 

The most common examples include the Wang transform and the Esscher transform; see [35, 36, 33, 37, 8]. The one-factor Wang transform is 

**==> picture [108 x 14] intentionally omitted <==**

with _λ ∈_ � controlling the degree of distortion. The Esscher transform instead tilts the density by the exponential factor _e[λ][x]_ . 

Figure 5 illustrates the effect of the Wang transform on a baseline distribution. 

**==> picture [226 x 213] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ<br>0.1<br>0.5<br>1<br>0<br>-0.1<br>-0.5<br>-1<br>0.0 0.2 0.4 0.6 0.8 1.0<br>F [�] ( x )<br>1.0<br>0.8<br>) 0.6<br>x<br>∗ �(<br>F<br>0.4<br>0.2<br>0.0<br>**----- End of picture text -----**<br>


Figure 5: The one-factor Wang transform _F_[�] _[∗]_ ( _x_ ) = _Φ_ ( _Φ[−]_ ( _F_[�] ( _x_ )) + _λ_ ) for several values of _λ_ . 

## **6.2 Distorted measures induced by quantile diffusions** 

The quantile diffusion framework induces a natural distorted measure by transporting the law of a driving process through the law of the transformed process. This gives a dynamic distortion mechanism rather than a purely static one. 

23 

Let _Y_ = ( _Yt_ ) _t≥_ 0 be a driving diffusion under �, and let 

**==> picture [95 x 14] intentionally omitted <==**

be the associated true-law random-level quantile diffusion. Define � _[Z]_ as the measure under which the marginal law of _Yt_ coincides with the marginal law of _Zt_ under �, i.e. 

**==> picture [86 x 16] intentionally omitted <==**

Equivalently, for any Borel function _ϕ_ , 

**==> picture [338 x 15] intentionally omitted <==**

Thus pricing under � _[Z]_ is equivalent to pricing the transformed process _Z_ under the original measure �. The advantage is that the distortion is parameterised directly through the quantile map, so features such as skewness and kurtosis enter the pricing measure transparently. 

The quantile-based distortion is not merely another static distortion operator. It is induced by a continuous-time stochastic model and therefore provides a dynamic measure change consistent with the chosen dependence structure of the driver. 

## **6.3 Connection with Wang-type distortions** 

Classical distortions arise as special cases of the false-law construction. Suppose _Yt_ is standard normal marginally under �, and choose the false law 

**==> picture [101 x 11] intentionally omitted <==**

Then, for any target quantile family _Qζ_ , 

**==> picture [102 x 13] intentionally omitted <==**

A direct calculation yields 

**==> picture [145 x 15] intentionally omitted <==**

which is exactly the one-factor Wang distortion applied to the target law _Fζ_ ( _·_ ; _ξ_ ). 

Hence the random-level quantile diffusion framework contains the Wang transform as a static marginal special case, while also extending it to a dynamic setting through the underlying diffusion. 

## **6.4 Tukey** _g_ **-** _h_ **distortions** 

A particularly appealing application is obtained by taking _Qζ_ = _Qφgh_ , the Tukey _g_ - _h_ quantile function. The induced distorted measure then reflects skewness and tail-thickening directly through the parameters _g_ and _h_ . This is especially natural in insurance and financial applications where compensation for asymmetric and heavy-tailed risk is required. 

Figures 6–8 illustrate the effect of the induced distortion on the marginal law for several choices of _g_ , _h_ , and, in the false-law case, the shift parameter _λ_ . 

24 

**==> picture [356 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameters<br>g=0.5, h=0.01<br>g=-0.5, h=0.01<br>g=1, h=0.01<br>Parameters g=-1, h=0.01<br>gggNo distortion===0.1, h0.1, h0.1, h===0.010.10.5 No distortiongggg====0.5, h-0.5, h1, h-1, h==0.1=0.1=0.10.1<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>FY [�][(][0.5,] [ y] [)] FY [�][(][0.5,] [ y] [)]<br>1.0 1.0<br>0.8 0.8<br>)  y 0.6 )  y 0.6<br>Z �(0.5, FY 0.4 Z �(0.5, FY 0.4<br>0.2 0.2<br>0.0 0.0<br>**----- End of picture text -----**<br>


Figure 6: Relation between the marginal laws of the driving process under � and the induced distorted measure � _[Z]_ for several _g_ - and _h_ -parameter choices. 

**==> picture [356 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameters<br>g=0.5, h=0.01<br>g=-0.5, h=0.01<br>g=1, h=0.01<br>Parameters g=-1, h=0.01<br>h=0.01 No distortion<br>h=0.1 g=0.5, h=0.1<br>h=0.5 g=-0.5, h=0.1<br>No distortion g=1, h=0.1<br>g=-1, h=0.1<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>FY [�][(][0.5,] [ y] [)] FY [�][(][0.5,] [ y] [)]<br>1.0 1.0<br>0.8 0.8<br>)  y 0.6 )  y 0.6<br>Z �(0.5, FY 0.4 Z �(0.5, FY 0.4<br>0.2 0.2<br>0.0 0.0<br>**----- End of picture text -----**<br>


Figure 7: Additional examples of the induced distortion under alternative drift specifications for the driving process. 

**==> picture [356 x 158] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parameters<br>Parameters g=0.5, h=0.01,  λ =0.6<br>g=0.2, h=0.01,  λ =0.6 g=-0.5, h=0.01,  λ =0.6<br>g=0.2, h=0.1,  λ =0.6 g=1, h=0.01,  λ =0.6<br>g=0.2, h=0.5,  λ =0.6 g=-1, h=0.01,  λ =0.6<br>No distortion No distortion<br>ggg===0.2, h0.2, h0.2, h===0.01,0.1,0.5,  λ λ λ ===0.10.10.1 ggg===0.5, h-0.5, h1, h=0.01,==0.01,0.01,  λ λ =  λ 0.1==0.10.1<br>g=-1, h=0.01,  λ =0.1<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>FY [�][(] [t] [,] [ y] [)] FY [�][(] [t] [,] [ y] [)]<br>1.0 1.0<br>0.8 0.8<br>) 0.6 ) 0.6<br>Z �( Ft yY , 0.4 Z �( Ft yY , 0.4<br>0.2 0.2<br>0.0 0.0<br>**----- End of picture text -----**<br>


Figure 8: Marginal distortions induced by the false-law construction for several combinations of _g_ , _h_ , and _λ_ . 

## **6.5 Numerical illustration** 

We conclude with a brief numerical example in the spirit of [35]. Let the terminal risk _YT_ at _T_ = 1 have Pareto distribution 

**==> picture [183 x 28] intentionally omitted <==**

25 

We compare risk-adjusted layer premia under three distortions: 

- (i) a proportional-hazards distortion, 

- (ii) a Wang distortion, 

- (iii) a Tukey- _g_ quantile distortion induced through the false-law construction. 

The Tukey- _g_ case is calibrated so that one layer premium matches the corresponding Wang or PH premium, and the remaining layers then reveal the effect of the skewness parameter _g_ . The resulting premia are reported in Table 1. 

|Layer in 000’s|PH premium<br>_r_ =0.9245|Wang premium<br>_α_=0.1|_πTg_[_Y_1;_γ_,_g_,_B_=0.01]|_πTg_[_Y_1;_γ_,_g_,_B_=0.01]|
|---|---|---|---|---|
||||_g_ =0.8,_γ_=6.96|_g_ =0.08,_γ_=_−_10.25|
|(0,50]|**5,487.0**|**5,487.0**|**5,487.2**|261.9|
|(50,100]|910|845.0|4,632.6|228.5|
|(100,200]|857|769.9|8,642.6|431.7|
|(200,300]|475|**414.2**|8,219.7|**414.2**|
|(300,400]|325|278.4|7,965.5|403.5|
|(400,500]|246|207.3|7,785.9|395.9|
|(500,1000]|728|598.0|37,287.4|1,909.3|
|(1000,2000]|675|533.2|70,349.5|3,635.2|
|(2000,5000]|819|616.6|197,478.0|10,306.4|
|(5000,10000]|567|405.7|310,290.9|16,331.72|



Table 1: Risk-adjusted layer premia under proportional-hazards, Wang, and Tukey- _g_ distortions. Bold entries indicate the matched calibration layers. 

The table shows the main qualitative effect clearly: once calibrated to match a benchmark layer, the Tukey- _g_ distortion can produce substantially steeper increases in higher layers, reflecting the stronger emphasis it places on asymmetric tail risk. This illustrates how the quantile diffusion framework can be used to build flexible pricing distortions beyond classical one-parameter transforms. 

## **6.6 Interpretation** 

The distortion-pricing example highlights the practical value of the proposed construction. 

- The _driver_ fixes the temporal dependence. 

- The _quantile family_ fixes the marginal shape. 

- The induced measure � _[Z]_ translates these distributional features into pricing adjustments. 

In particular, the Tukey _g_ - _h_ family provides a direct way to encode skewness and heavy tails into the pricing measure, which is especially relevant for insurance loss modelling, reserve risk, and layer pricing. 

## **7 Dynamic Insurance Application: Quantile Diffusion for Excess-ofLoss Reinsurance Pricing** 

## **7.1 Motivation** 

A natural actuarial application of the proposed quantile diffusion framework is the dynamic modelling of aggregate insurance losses for pricing and capital management. In catastrophe and specialty insurance portfolios, aggregate losses exhibit several characteristic statistical features: 

26 

- strong right skewness, 

- heavy upper tails, 

- temporal clustering of extreme events, 

- regime shifts due to hazard conditions or market cycles. 

Traditional stochastic loss models typically capture time-varying location and scale, but they often struggle to represent evolving skewness and tail thickness. However, in many insurance applications—particularly in excess-of-loss reinsurance pricing—the upper tail of the distribution plays the dominant role. 

The quantile diffusion construction developed in this paper is particularly suitable for such problems because it allows the entire loss distribution to evolve through time while explicitly controlling its quantile structure. As a result, high-risk quantiles such as VaR or TVaR can be modelled directly, and pricing formulas depending on the upper tail become computationally tractable. 

We illustrate this with an application to dynamic pricing of catastrophe excess-of-loss reinsurance. 

## **7.2 Insurance Loss Process** 

Let _Lt_ denote the aggregate insured loss of a portfolio over a time period [0, _t_ ]. The objective is to model the stochastic evolution of the distribution of _Lt_ over time. 

Following the random-level quantile diffusion construction, let ( _Yt_ ) _t≥_ 0 be a diffusion process defined by 

**==> picture [145 x 12] intentionally omitted <==**

with marginal distribution function _FY_ ( _t_ , _y_ ; _θ_ ). Define the uniformised process 

**==> picture [80 x 12] intentionally omitted <==**

By construction, _Ut ∈_ (0,1) almost surely. 

Let _Qζ_ ( _u_ ; _ξ_ ) denote a target quantile function corresponding to a distribution family chosen to capture skewness and tail behaviour. The quantile diffusion process is then 

**==> picture [70 x 13] intentionally omitted <==**

To obtain a strictly positive loss process we define 

**==> picture [61 x 12] intentionally omitted <==**

The quantile function of _Lt_ therefore becomes 

**==> picture [110 x 13] intentionally omitted <==**

Consequently, the entire loss distribution is explicitly characterized by the quantile map _Qζ_ . 

## **7.3 Tukey** _g_ **–** _h_ **Quantile Specification** 

A convenient specification for insurance loss modelling is the Tukey _g_ – _h_ family, whose quantile function is 

**==> picture [194 x 30] intentionally omitted <==**

27 

where 

**==> picture [59 x 13] intentionally omitted <==**

and parameters _ξ_ = ( _A_ , _B_ , _g_ , _h_ ) have the following interpretations: 

- _A_ : location parameter 

- _B >_ 0 : scale parameter 

- _g_ : skewness parameter 

- _h ≥_ 0 : tail thickness parameter 

In an insurance context, the parameters _g_ and _h_ control asymmetric extreme loss behaviour and heavy tail risk, respectively. 

The aggregate loss process therefore becomes 

**==> picture [260 x 29] intentionally omitted <==**

## **7.4 Excess-of-Loss Reinsurance Contract** 

Consider an excess-of-loss reinsurance treaty with attachment point _a_ and limit _ℓ_ . The ceded loss payment at time _T_ is 

**==> picture [110 x 12] intentionally omitted <==**

Under the physical probability measure _P_ , the actuarially fair premium equals 

**==> picture [86 x 14] intentionally omitted <==**

Because the distribution of _LT_ is specified through its quantile function, the expectation can be written directly in quantile form: 

**==> picture [184 x 32] intentionally omitted <==**

This representation is computationally convenient since numerical integration over the unit interval can be used to evaluate premiums. 

## **7.5 Distortion-Based Pricing** 

Insurance pricing commonly incorporates risk loading via distortion measures. Let _g_ ( _u_ ) denote a distortion function such that 

**==> picture [202 x 11] intentionally omitted <==**

The distorted premium becomes 

**==> picture [198 x 32] intentionally omitted <==**

Within the quantile diffusion framework, this distortion can be interpreted as a change in the parameters of the quantile map. For example, under the pricing measure one may use parameters 

28 

**==> picture [88 x 12] intentionally omitted <==**

with 

**==> picture [88 x 12] intentionally omitted <==**

This increases right-tail mass and produces higher reinsurance premiums, reflecting market risk loadings. 

## **7.6 Capital Requirement Measures** 

The model also allows dynamic computation of capital requirements. For confidence level _α_ , the Value-at-Risk of the portfolio loss is 

**==> picture [90 x 13] intentionally omitted <==**

Similarly, the Tail Value-at-Risk is 

**==> picture [152 x 31] intentionally omitted <==**

These quantities follow directly from the evolving quantile curve and can therefore be monitored dynamically as the diffusion evolves. 

## **7.7 Implementation Strategy** 

Implementation of the model proceeds through the following steps: 

## 1. **Data preparation** 

Construct a time series of aggregate portfolio losses 

**==> picture [63 x 13] intentionally omitted <==**

## 2. **Specification of driving diffusion** 

Choose a latent diffusion process for _Yt_ , for example a mean-reverting Ornstein–Uhlenbeck process 

**==> picture [133 x 11] intentionally omitted <==**

## 3. **Uniformisation** 

Estimate the marginal distribution _FY_ and compute 

**==> picture [67 x 11] intentionally omitted <==**

## 4. **Quantile map estimation** 

Estimate parameters _ξ_ = ( _A_ , _B_ , _g_ , _h_ ) of the quantile function by minimizing a weighted quantile loss 

**==> picture [217 x 32] intentionally omitted <==**

29 

## 5. **Pricing and risk evaluation** 

Compute reinsurance premiums and capital measures via numerical integration using the fitted quantile function. 

## **7.8 Interpretation** 

The quantile diffusion framework provides a transparent interpretation of evolving insurance risk. 

- parameter _A_ controls the typical loss level, 

- parameter _B_ governs volatility of aggregate losses, 

- parameter _g_ measures asymmetry of extreme losses, 

- parameter _h_ captures tail thickness and catastrophe risk. 

Changes in reinsurance premiums or capital requirements can therefore be attributed directly to shifts in skewness or tail behaviour rather than simply changes in variance. 

This makes the framework particularly useful for explaining pricing and capital dynamics to underwriting and risk management teams. 

## **8 Synthetic implementation of quantile diffusion pricing examples** 

To illustrate the random–level and function–valued quantile diffusion constructions in an actuarial setting, we implement a synthetic study based on the pricing and insurance examples developed near the end of the paper. The paper’s random–level construction takes the form 

**==> picture [275 x 13] intentionally omitted <==**

while the dynamic insurance application defines the strictly positive loss process by 

**==> picture [256 x 12] intentionally omitted <==**

and values an excess–of–loss layer by 

**==> picture [325 x 32] intentionally omitted <==**

These formulas are directly aligned with the constructions and applications developed in the manuscript.[1] 

## **8.1 Simulation design** 

We simulate a stationary Ornstein–Uhlenbeck diffusion 

**==> picture [289 x 12] intentionally omitted <==**

with parameters chosen so that the stationary marginal law is standard normal. The corresponding random quantile level process is therefore 

**==> picture [252 x 11] intentionally omitted <==**

> 1See the paper for the definition of the random–level quantile diffusion, the distortion–pricing application, and the dynamic insurance pricing formulation. 

30 

We then generate a Tukey _g_ – _h_ quantile diffusion via 

where 

**==> picture [379 x 63] intentionally omitted <==**

In the synthetic experiment the true parameters are set to 

**==> picture [309 x 11] intentionally omitted <==**

The corresponding insurance loss process is defined by _Lt_ = exp( _Zt_ ). 

The driver paths and random quantile level diffusion paths are plotted for some example trajectories in Figure 9. 

Figure 9: Driver paths and resulting random level quantile paths. 

## **8.2 Estimation by weighted quantile matching** 

To estimate the target quantile parameters from synthetic observations we pool simulated values of _Zt_ = log _Lt_ and minimise a weighted quantile loss, 

**==> picture [343 x 32] intentionally omitted <==**

with probability levels concentrated in the body and upper tail of the distribution. Table 2 summarises the synthetic recovery results. 

Table 2: Synthetic parameter recovery for the random–level Tukey _g_ – _h_ quantile diffusion. 

|Parameter|True value|Estimate|Absolute error|
|---|---|---|---|
|_A_|0.8000|0.7844|0.0156|
|_B_|0.5500|0.5547|0.0047|
|_g_|0.3500|0.3464|0.0036|
|_h_|0.1200|0.1171|0.0029|



The estimates recover all four parameters accurately, indicating that a direct quantile–matching approach is a practical estimator for the target family in the present setting. 

Next we plot the quantile fitting results for the simulation to assess the accuracy of the fitting, see Figure **??** which shows the fitted versus true quantile of the log-loss process. 

31 

Figure 10: Empirical Quantile, True Quantile and Fitted Quantile function of log-loss. 

## **8.3 Actuarial and distortion–based pricing** 

We next consider an excess–of–loss reinsurance treaty with attachment _a_ = 6 and limit _ℓ_ = 8. Under the physical measure, the one–period actuarially fair premium is 

**==> picture [312 x 32] intentionally omitted <==**

To incorporate a pricing adjustment we consider two alternatives. First, a Wang distortion, 

**==> picture [280 x 13] intentionally omitted <==**

leading to the premium 

**==> picture [330 x 31] intentionally omitted <==**

Second, a direct parameter deformation in the target quantile family, 

**==> picture [287 x 11] intentionally omitted <==**

which provides a transparent actuarial loading associated with increased skewness and tail thickness. 

In Figure 11 the plot of the Wang distortion CDF as a special case of the false-law construction for this example. 

Table 3 reports the resulting premiums. 

These results show that the Wang distortion produces a substantially larger premium than the physical measure, while the direct parameter shift offers an interpretable loading that can be attributed to higher asymmetry and heavier tail behaviour. 

## **8.4 Function–valued quantile diffusion and dynamic insurance pricing** 

To illustrate dynamic insurance pricing we let the parameter vector ( _At_ , _Bt_ , _gt_ , _ht_ ) evolve as a multivariate parameter diffusion, implemented componentwise through Ornstein–Uhlenbeck dynamics 

32 

Figure 11: Base Line versus Wang Distortion CDF. 

Table 3: Synthetic actuarial and distortion–based premium calculations. 

|Pricingmeasure|Premium|
|---|---|
|Physical premium|0.3922|
|Wang premium,_λ_=0.5|0.9774|
|Wang premium,_λ_=1.0|1.9982|
|Parameter shift(_∆g_,_∆h_) = (0.08,0.03)|0.4800|
|Synthetic market loadedpremium|1.2540|



on transformed coordinates. At each time _t_ this yields a stochastic quantile curve 

**==> picture [304 x 13] intentionally omitted <==**

from which we compute the dynamic physical premium _Π[P] t_[,][the][Wang–loaded][premium] _[Π][⋆] t_[,][and] capital metrics such as VaR0.99( _Lt_ ) and TVaR0.99( _Lt_ ). Selected time snapshots are reported in Table 4. 

Table 4: Selected dynamic pricing and capital snapshots from the function–valued quantile diffusion. 

|Time|_At_|_Bt_|_gt_|_ht_|_ΠP_<br>_t_|_Π⋆_<br>_t_|VaR0.99|TVaR0.99|
|---|---|---|---|---|---|---|---|---|
|0.00|0.7000|0.5000|0.1500|0.0400|0.0860|0.4502|9.4977|15.2868|
|1.25|0.6789|0.5794|0.3311|0.0507|0.2693|1.0746|20.2491|160.8578|
|2.50|0.5347|0.6526|0.2091|0.0599|0.2230|0.9441|17.0230|77.5700|
|5.00|0.5707|0.5653|0.2024|0.0598|0.1575|0.7391|12.7421|37.1157|



The results illustrate that both premium levels and capital metrics respond dynamically to the evolution of the quantile parameters. In particular, increases in _gt_ and _ht_ translate directly into larger upper–tail loss quantiles and higher loaded premiums, which is precisely the actuarial interpretability sought in the quantile diffusion framework. 

In Figure 12 the plotted excess-of-loss premiums are presented for the physical and Wang-loaded loss premiums. 

Overall, the synthetic implementation demonstrates that the proposed quantile diffusion framework can be operationalised in a transparent manner for estimation, actuarial pricing, distortionbased loading, and dynamic capital monitoring. 

33 

Figure 12: Dynamic physical and Wang–loaded excess–of–loss premiums under the function–valued quantile diffusion. 

Figure 13: Dynamic tail capital measures VaR0.99 and TVaR0.99. 

34 

## **9 Empirical application: reserve deterioration risk and stop-loss pricing using real paid-loss data** 

This section develops a real-data empirical illustration of the quantile diffusion framework using the classical `RAA` general insurance paid-claims triangle from the `ChainLadder` package. In contrast to the synthetic study, the present example works directly with observed insurance cash flows and shows how the proposed methodology can be calibrated to real reserve-deterioration data for forecasting, capital assessment, and actuarial pricing. The construction is aligned with the random-level quantile diffusion developed earlier in the paper, 

**==> picture [98 x 13] intentionally omitted <==**

with positive reserve-deterioration amounts represented by the exponential map 

**==> picture [61 x 11] intentionally omitted <==**

so that capital and treaty prices can be evaluated directly from the fitted quantile representation. 

## **9.1 Data construction and empirical objective** 

We begin with the cumulative paid-loss triangle and convert it to incremental paid claims. The empirical series used for calibration is the calendar-year aggregate incremental paid-loss series 

**==> picture [90 x 11] intentionally omitted <==**

where each observation is obtained by summing all positive incremental paid amounts in a common calendar year. This series is interpreted as an observed annual reserve-deterioration cash-flow process. Figure 14 displays the cumulative triangle used as the raw data source, while Figure 15 shows the resulting calendar-year aggregate paid-loss series. 

Figure 14: RAA cumulative paid claims triangle used to construct the empirical reserve-deterioration series. 

35 

Figure 15: Calendar-year aggregate incremental paid losses derived from the triangle. 

Table 5 reports the descriptive statistics of the empirical aggregate series. Although the sample is short, the series already exhibits substantial variation, with aggregate annual paid amounts ranging from 3,363 to 24,708 and a standard deviation of 7,789.36. On the log scale the standard deviation is 0.695, indicating appreciable dispersion even after logarithmic stabilisation. 

Table 5: Descriptive statistics for the calendar-year aggregate paid-loss series. 

|Statistic|Value|
|---|---|
|Number of observations|10|
|Mean paid|16,109.00|
|Standard deviation paid|7,789.36|
|Median paid|18,085.50|
|Minimum paid|3,363|
|Maximum paid|24,708|
|Mean log paid|9.518|
|Standard deviation log paid|0.695|



## **9.2 Model specification and calibration** 

The empirical implementation follows the two-stage decomposition proposed in the working example. First, the marginal law of the log paid-loss series is represented by a Tukey _g_ – _h_ quantile family, 

**==> picture [283 x 29] intentionally omitted <==**

with the usual continuous extension at _g_ = 0. Second, the implied Gaussian score process 

**==> picture [186 x 15] intentionally omitted <==**

is fitted by the discrete-time AR(1) representation associated with an Ornstein–Uhlenbeck driver. The fitted Tukey parameters are reported in Table 6. The estimates indicate a negative skew parameter _g_ = _−_ 0.703 and an essentially negligible _h_ -parameter on this short empirical series, 

36 

suggesting that asymmetry is more important than additional tail elongation in the present calibration. Figure 16 compares the empirical and fitted log-loss quantiles, showing that the quantile map provides a close fit across the body and upper tail of the observed distribution. 

Table 6: Estimated marginal Tukey _g_ – _h_ parameters for the log paid-loss series. 

|Parameter|Estimate|
|---|---|
|_A_|9.6940|
|_B_|0.5955|
|_g_|-0.703|
|_h_|1.107e-07|
|Objective value|0.3654|
|Convergence code|0|



Figure 16: Empirical and fitted Tukey _g_ – _h_ quantiles for the log aggregate paid-loss series. 

The Gaussian score estimates obtained by numerical inversion of the fitted quantile map are shown in Figure 17. Fitting an AR(1) model to this score process yields the Ornstein–Uhlenbeck parameter estimates in Table 7. The estimated autoregressive coefficient is _φ_ = 0.7290, corresponding to an OU mean-reversion speed of _κ_ = 0.3161. The decomposition is actuarially useful because it separates marginal skewness and tail shape from the persistence of reserve shocks. 

Table 7: Estimated latent Ornstein–Uhlenbeck parameters from the Gaussian score process. 

|Parameter|Estimate|
|---|---|
|AR intercept|0.1437|
|AR coefficient_φ_|0.7290|
|OU mean-reversion_κ_|0.3161|
|OU long-run mean_θ_|0.5303|
|OU diffusion_σ_|0.5137|
|Residual standard deviation|0.4423|



37 

Figure 17: Estimated latent Gaussian score process obtained from the fitted quantile map. 

## **9.3 Predictive reserve-risk distribution and capital outputs** 

Using the fitted OU score dynamics and the calibrated Tukey map, we simulate the one-year-ahead predictive distribution of next-year aggregate reserve deterioration. Figure 18 displays the resulting predictive distribution. 

Figure 18: Predictive distribution of next-year aggregate reserve deterioration, with 95% VaR and 95% TVaR markers. 

The predictive capital measures are summarised in Table 8. The fitted model yields a predictive mean deterioration of 18,239.66, a 95% VaR of 24,534.60, and a 95% TVaR of 25,797.90. Thus, on this real-data application, the gap between TVaR and VaR is economically meaningful, confirming that a quantile-based framework is particularly informative for reserve-risk capital assessment. 

38 

Table 8: Predictive capital metrics for next-year aggregate reserve deterioration. 

|Measure|Value|
|---|---|
|Mean|18,239.66|
|Median|18,444.70|
|VaR 90%|23,301.47|
|VaR 95%|24,534.60|
|VaR 99%|26,621.05|
|TVaR 95%|25,797.90|
|TVaR 99%|27,549.42|



## **9.4 Stop-loss pricing and actuarial premium adjustments** 

We next consider a one-year stop-loss treaty written on the aggregate reserve-deterioration amount. The attachment is set at the predictive 90% quantile, 

**==> picture [84 x 11] intentionally omitted <==**

and the limit is taken to be a fixed proportion of attachment, 

**==> picture [50 x 9] intentionally omitted <==**

Under this specification the fitted attachment equals 23,301.47 and the limit equals 13,980.88. The treaty payoff is 

**==> picture [128 x 13] intentionally omitted <==**

The corresponding expected-loss premium, Wang premium, and Esscher premium are reported in Table 9. 

Table 9: Stop-loss pricing outputs under the fitted reserve-risk model. 

|Premium principle|Premium|Relative loading vs. fair|
|---|---|---|
|Expected-loss premium|152.87|0.000|
|Wang premium|298.84|0.955|
|Esscher premium|8,383.30|53.838|



The Wang-distorted premium curve as a function of the distortion parameter _λ_ is shown in Figure 19. As expected, the distortion-based price increases monotonically with the loading parameter and remains above the expected-loss price for positive values of _λ_ , reflecting the heavier pricing emphasis placed on upper-tail reserve outcomes. 

In this application the expected-loss premium is 152.87, while the Wang-distorted premium rises to 298.84. The Esscher premium is substantially larger at 8,383.30, illustrating the sensitivity of exponential tilting to severe upper-tail losses when reserve deterioration is modelled on the original paid-loss scale. From an actuarial perspective this behaviour is informative: Wang distortion produces a moderate and interpretable tail loading, whereas Esscher tilting delivers a much stronger market-consistent stress adjustment. 

## **9.5 Empirical proxy for the function-valued quantile diffusion** 

To illustrate the second construction in the paper, we re-estimate the Tukey _g_ – _h_ parameters on rolling windows of the observed log paid-loss series. This generates a time-indexed sequence of fitted quantile curves, which serves as a low-dimensional empirical proxy for the function-valued quantile diffusion. 

39 

Figure 19: Wang-distorted stop-loss premium as a function of the distortion parameter _λ_ . 

Figure 20 shows the rolling estimates of the parameter vector ( _At_ , _Bt_ , _gt_ , _ht_ ), while Figure 21 displays the corresponding fitted quantile curves for the terminal years 1988, 1989, and 1990. Although the sample is short, the rolling exercise still illustrates the main conceptual point: the entire quantile curve can evolve over time through stochastic or empirically varying parameters, rather than only through a scalar random quantile level. 

## **9.6 Discussion** 

This empirical study demonstrates that the quantile diffusion framework is not limited to synthetic scenarios. When calibrated to real insurance cash-flow data, it yields an interpretable decomposition of reserve risk into: 

- (i) the marginal skewness and tail shape of aggregate reserve deterioration; 

- (ii) the temporal persistence of reserve shocks through the latent OU score dynamics; and 

- (iii) the premium loading generated by actuarial distortion principles. 

The real-data example therefore complements the synthetic case study in an actuarially meaningful way. First, it shows that the random-level quantile diffusion can be calibrated directly to observed insurance deterioration cash flows while preserving a transparent interpretation of the fitted parameters. Second, it produces dynamic capital measures directly in quantile space, which is the natural domain for solvency and reserve-risk applications. Third, it provides a coherent route from fitted predictive reserve distributions to treaty pricing adjustments under both expected-loss and distorted premium principles. 

Taken together, the empirical results support the broader claim of the paper: quantile diffusions offer a practically useful and mathematically interpretable framework for dynamic insurance risk modelling, especially when the quantities of interest are inherently quantile-based, as in reserve capital assessment and aggregate stop-loss pricing. 

## **10 Conclusions** 

In this work we propose a novel, mathematical framework for the development of continuous–time, dynamic distortions induced by quantile processes. This approach can as such be widely adopted in 

40 

Figure 20: Rolling-window estimates of the empirical Tukey _g_ – _h_ parameter vector. 

Figure 21: Rolling-window fitted quantile curves as an empirical proxy for the function-valued quantile diffusion. 

41 

dynamic risk analysis and applications. An important result of this framework is that one obtains a time–consistent method for the construction of interpretable, continuous–time measure distortion flows on the space of quantile functions. We demonstrate that the framework generalises, but includes as special cases, existing well–known measure distortion approaches used in financial mathematics, financial risk and actuarial science, while extending these approaches into dynamical settings. Furthermore, the developed framework is constructed from families of transformations, which produce statistically interpretable measure distortions induced by the quantile processes, making their application directly interpretable in relation to aspects of the risk inherent to the underlying driving process being accounted for in the distortion map. This has significant meaning in, among many other settings, financial risk management. For instance, it can be seen as a generalisation of classical risk pricing, often based on risk premium related to trend or volatility, that instead accommodates pricing in higher–order risk associated to skewness or kurtosis of the underlying risky process being assessed. 

We developed two methods for the construction of the quantile processes to achieve our objectives: the first, which we largely focus on, features a dynamic random quantile level and allows for direct interpretation of the resulting quantile process characteristics such as location, scale, skewness and kurtosis, in terms of the model parameters. The second type are function–valued quantile diffusions and are driven by stochastic parameter processes, which determine the entire quantile function at each point in time. We derived core results relating to the definition, existence and uniqueness of such processes, and established the construction of the resulting distortion measure flows on the quantile space. We then produced key examples based on the flexible Tukey family of transforms applied to widely used underlying stochastic processes such as geometric Brownian motion and the Ornstein–Uhlenbeck processes. Such processes can be found in a range of practical application domains that include dynamic risk measures in econometrics, operations research sequential decision making, information theory and signal processing, and not least in general risk theory and applications thereof, e.g., in the context of dynamic risk assessment of climate change processes. 

**Acknowledgments** . The authors acknowledge financial support by UK Research & Innovation via EPSRC CASE project award 1939295, and are grateful for comments and suggestions by G. Kassis, W. T. Shaw, M. Crowe, and participants in the Mathematics & Finance Conference, Research in Options, IMPA, Rio de Janeiro, Brazil, and Khalifa University, Abu Dhabi, UAE (December 2020), and attendees of the AIFMRM Seminar Series, University of Cape Town (September 2021). 

## **References** 

- [1] B. Acciaio and I. Penner. Dynamic risk measures. _Advanced Mathematical Economics_ , 13:1–34, 2011. 

- [2] J. Akahori. Distribution of the _α_ -percentile of a brownian motion. _Journal of Applied Probability_ , 32:1032–1043, 1995. 

- [3] R. R. Bahadur. A note on quantiles in large samples. _The Annals of Mathematical Statistics_ , 37 (3):577–580, 1966. 

- [4] O. Barndorff-Nielsen and D. R. Cox. Edgeworth and saddle-point approximations with statistical applications. _Journal of the Royal Statistical Society: Series B (Methodological)_ , 41(3): 279–299, 1979. 

- [5] A. Belloni, V. Chernozhukov, D. Chetverikov, and I. Fernández-Val. Conditional quantile processes based on series or many regressors. _Journal of Econometrics_ , 213(1):4–29, 2019. 

42 

- [6] P. J. Bickel. Edgeworth expansions in nonparametric statistics. _The Annals of Statistics_ , pages 1–20, 1974. 

- [7] T. Bielecki et al. A survey of dynamic risk measures. _Annual Review of Financial Economics_ , 9: 1–25, 2017. 

- [8] H. Bühlmann. An economic premium principle. _ASTIN Bulletin: The Journal of the IAA_ , 11(1): 52–60, 1980. 

- [9] M. Csörg˝o and L. Horváth. _Quantile Processes with Applications_ . SIAM, 1983. 

- [10] M. Csörg˝o and P. Révész. Strong approximations of the quantile process. _The Annals of Statistics_ , 6(4):882–894, 1978. 

- [11] H. E. Daniels. Saddlepoint approximations in statistics. _The Annals of Mathematical Statistics_ , pages 631–650, 1954. 

- [12] A. Dassios. The distribution of the quantile of a Brownian motion with drift and the pricing of related path-dependent options. _The Annals of Applied Probability_ , 5(2):389–398, 1995. 

- [13] A. Dassios. Sample quantiles of stochastic processes with stationary and independent increments. _The Annals of Applied Probability_ , 6(3):1041–1043, 1996. 

- [14] P. Embrechts, L. Rogers, and M. Yor. A proof of Dassios’ representation of the _α_ -quantile of Brownian motion with drift. _The Annals of Applied Probability_ , 5(3):757–767, 1995. 

- [15] P. Embrechts, C. Klüppelberg, and T. Mikosch. _Modelling Extremal Events for Insurance and Finance_ . Springer, 1997. 

- [16] W. Gilchrist. _Statistical modelling with quantile functions_ . CRC Press, Cleveland, OH, 2000. 

- [17] W. Gilchrist. _Statistical Modelling with Quantile Functions_ . Chapman and Hall, 2000. 

- [18] M. Goovaerts, R. Kaas, and J. Dhaene. Risk measures and premium principles. _Insurance: Mathematics and Economics_ , 49:206–217, 2011. 

- [19] N. Ikeda and S. Watanabe. _Stochastic differential equations and diffusion processes_ . Elsevier, Amsterdam, NL, 2014. 

- [20] I. Karatzas and S. Shreve. _Brownian motion and stochastic calculus. Vol. 113_ . Springer Science & Business Media, Berlin, Heidelberg, 2012. 

- [21] J. Kiefer. On Bahadur’s representation of sample quantiles. _The Annals of Mathematical Statistics_ , 38(5):1323–1342, 1967. 

- [22] S. Klugman, H. Panjer, and G. Willmot. _Loss Models: From Data to Decisions_ . Wiley, 2012. 

- [23] R. Koenker. _Quantile Regression_ . Cambridge University Press, 2005. 

- [24] R. Koenker. Quantile regression: 40 years on. _Annual Review of Economics_ , 9:155–176, 2017. 

- [25] R. Koenker and G. Bassett Jr. Regression quantiles. _Econometrica: Journal of the Econometric Society_ , 4(1):33–50, 1978. 

- [26] R. Koenker and Z. Xiao. Quantile autoregression. _Journal of the American Statistical Association_ , 101(475):980–990, 2006. 

- [27] R. Miura. The _α_ -percentile option. _Journal of Applied Probability_ , 29:367–375, 1992. 

43 

- [28] B. Oksendal. _Stochastic differential equations: an introduction with applications_ . Springer Science & Business Media, Berlin, Heidelberg, 2013. 

- [29] G. W. Peters. General quantile time series regressions for applications in population demographics. _Risks_ , 6(3):97, 2018. 

- [30] W. Shaw and I. Buckley. Beyond the cornish–fisher expansion. _Quantitative Finance_ , 10:1055– 1066, 2010. 

- [31] W. T. Shaw and I. R. Buckley. The alchemy of probability distributions: beyond Gram-Charlier expansions, and a skew-kurtotic-normal distribution from a rank transmutation map. _Preprint arXiv:0901.0434_ , 2009. 

- [32] G. Steinbrecher and W. T. Shaw. Quantile mechanics. _European Journal of Applied Mathematics_ , 19(2):87–112, 2008. 

- [33] S. Wang. Premium calculation by transforming the layer premium density. _ASTIN Bulletin: The Journal of the IAA_ , 26(1):71–92, 1996. 

- [34] S. Wang. A class of distortion operators for pricing financial and insurance risks. _Journal of Risk and Insurance_ , 67:15–36, 2000. 

- [35] S. S. Wang. A class of distortion operators for pricing financial and insurance risks. _Journal of Risk and Insurance_ , 67(1):15–36, 2000. 

- [36] S. S. Wang. A universal framework for pricing financial and insurance risks. _ASTIN Bulletin: The Journal of the IAA_ , 32(2):213–234, 2002. 

- [37] S. S. Wang, V. R. Young, and H. H. Panjer. Axiomatic characterization of insurance prices. _Insurance: Mathematics and economics_ , 21(2):173–183, 1997. 

## **A Appendix** 

## **B Quantile SDEs Verification of Existence and Uniqueness** 

In this section we derive the dynamical equations of the quantile diffusions. We begin by deriving SDEs for the dynamics of the random–level quantile diffusion, considering the two cases in Definition **??** . The following proposition and corollary guarantee that in each case ( _Zt_ ) is a diffusion, and provide the corresponding infinitesimal drift and volatility coefficients. As such, the transition distribution of ( _Zt_ ) must solve the Kolmogorov backward equation having these same coefficients. We omit the dependence on the vectors of parameters in the notation for the following distribution, quantile and density functions. 

**Proposition B.1.** _Let_ ( _Zt_ ) _t_ 0 _≤t<∞ be a quantile diffusion given by Definition_ **??** _(ii). Assume the following derivatives exist so that f_ ( _t_ , _y_ ) := _∂ y F_ ( _t_ , _y_ ) _and fζ_ ( _z_ ) := _∂z Fζ_ ( _z_ ) _are density functions. The dynamics of_ ( _Zt_ ) _satisfies_ 

**==> picture [297 x 11] intentionally omitted <==**

44 

_where_ 

**==> picture [440 x 67] intentionally omitted <==**

**==> picture [440 x 29] intentionally omitted <==**

_for t ∈_ [ _t_ 0, _∞_ ) _and Zt_ 0 = _zt_ 0 _∈_ � _. The short-hand notation f[′] denotes differentiation with respect to the spatial variable._ 

_Proof._ The result follows from a straightforward application of Ito’s formula and also by use of Eq. (64) in [32]. 

**Corollary B.1.** _Let_ ( _Zt_ ) _be a quantile diffusion given by Definition_ **??** _(i). The dynamics of_ ( _Zt_ ) _satisfy_ 

**==> picture [297 x 11] intentionally omitted <==**

_where_ 

**==> picture [436 x 67] intentionally omitted <==**

**==> picture [25 x 10] intentionally omitted <==**

**==> picture [444 x 29] intentionally omitted <==**

_for t ∈_ [ _t_ 0, _∞_ ) _and Zt_ 0 = _zt_ 0 _∈_ � _, where fY_ ( _t_ , _y_ ) _is the transition density of the driving process_ ( _Yt_ ) _starting with y_ 0 _∈_ � _._ 

_Proof._ Similarly to the proof of Proposition (B.1), we apply Ito’s formula to _Zt_ = _Qζ_ ( _FY_ ( _t_ , _Yt_ )). Since _FY_ ( _t_ , _x_ ) is the law of the process ( _Yt_ ), we can use the Fokker-Plank equation to describe how the density of ( _Yt_ ), that is _fY_ ( _t_ , _y_ ), evolves with time. The chain rule yields _∂tQζ_ ( _FY_ ( _t_ , _y_ )) = _∂t FY_ ( _t_ , _y_ ) _/ fζ_ ( _Qζ_ ( _FY_ ( _t_ , _y_ )) and by the fundamental theorem of calculus, we obtain 

**==> picture [298 x 33] intentionally omitted <==**

Now, using the Fokker-Planck equation for the marginal density of ( _Yt_ ), we have _∂t FY_ ( _t_ , _y_ ) = � _−∞y[∂][t][ f][Y]_[ (] _[t]_[,] _[ x]_[)] _[d x]_[=] _[ −][µ]_[(] _[t]_[,] _[ y]_[)] _[f][Y]_[ (] _[t]_[,] _[ y]_[) +][1] 2 � _σ_[2] ( _t_ , _y_ ) _fY[′]_[(] _[t]_[,] _[ y]_[) +] _[f][Y]_[ (] _[t]_[,] _[ y]_[)] _[∂][y][σ]_[2][(] _[t]_[,] _[ y]_[)] �, and therefore 

**==> picture [370 x 32] intentionally omitted <==**

Noting that _Yt_ = _QY_ ( _t_ , _Fζ_ ( _Zt_ )), the result stated in the corollary follows. 

We highlight that the choice of the distribution function _F_ in the composite map impacts the drift function _α_ ( _t_ , _z_ ) of the resulting quantile diffusion SDE. In the case where _F_ = _FY_ is the “true 

45 

law” of the driving process, any explicit dependence of _α_ ( _t_ , _z_ ) on the drift function _µ_ ( _t_ , _y_ ) of the driving process is removed. 

Similarly, the SDE satisfied by the function–valued quantile diffusion in Definition **??** is obtained by a straightforward application of Ito’s formula as follows. 

Let _Zt_ ( _u_ )0 _≤t<∞_ be a quantile diffusion given by Definition **??** . For each _u ∈_ [0,1], the dynamics of _Zt_ ( _u_ ) are given by the SDE 

**==> picture [433 x 81] intentionally omitted <==**

A discussion on the existence of strong and weak solutions to SDEs is given in the following section in this Appendix B.1. 

## **B.1 Existence of strong and weak solutions** 

We consider the SDEs satisfied by diffusions, with a view to describe the conditions under which solutions to these SDEs exist, and whether they are strong or weak. Consider a probability space ( _Ω_ , _�_ , �) and an _r_ -dimensional Brownian motion along with its natural filtration, 

**==> picture [290 x 14] intentionally omitted <==**

where we assume the space is rich enough to accommodate a random vector _**ξ** ∈_ � _[d]_ , independent of _�∞[W]_[and][with][given][distribution] _[µ]_[(] _[Γ]_[)][=][�][(] _**[ξ]**[∈][Γ]_[)][,] _[Γ][∈�]_[(][�] _[d]_[)][.][Moreover,][we][consider][the] left–continuous filtration _�t_ ≜ _σ_ ( _**ξ**_ ) _∨�t[W]_ = _σ_ ( _**ξ**_ , _Ws_ ;0 _≤ t < ∞_ ) and the collection of null sets _�_ ≜ _{N ⊆ Ω_ ; _∃G ∈�∞_ with _N ⊆ G_ and �( _G_ ) = 0 _}_ to obtain the augmented filtration 

**==> picture [344 x 15] intentionally omitted <==**

Next, we consider the general _d_ –dimensional SDE 

**==> picture [324 x 31] intentionally omitted <==**

0 _≤ t < ∞_ , where _**µ**_ ( _t_ , _**x**_ ) = _{µi_ ( _t_ , _x_ ) _}_ 1 _≤i≤d_ is the ( _d×_ 1)–drift vector, _**σ**_ ( _t_ , _**x**_ ) = _{σi j_ ( _t_ , _x_ )1 _≤i≤d_ ,1 _≤ j≤r }_ is the ( _d × r_ )- dispersion matrix, _µi_ ( _t_ , _x_ ) : [0, _∞_ ) _×_ � _→_ � for 1 _≤ i ≤ d_ and _σi j_ ( _t_ , _x_ ) : [0, _∞_ ) _×_ � _→_ �[+] for 1 _≤ i ≤ d_ , 1 _≤ j ≤ r_ are Borel–measurable functions, and where _W_ = ( _**W** t_ , _�t[W]_[;0] _[ ≤][t][<][ ∞]_[)] is the _r_ –dimensional Brownian motion in Eq. (B.8). 

One may refer to [19, 20] for the definition of a solution to the SDE B.10 and the distinction between whether the solution is strong or weak and the type of uniqueness it exhibits. The following theorem in [20] gives the conditions under which a strong solution with the pathwise uniqueness property exists. 

**Theorem B.1.** _Suppose the coefficients_ _**µ**_ ( _t_ , _**x**_ ) _and_ _**σ**_ ( _t_ , _**x**_ ) _satisfy the global Lipschitz and linear growth conditions_ 

**==> picture [341 x 29] intentionally omitted <==**

_for every_ 0 _≤ t < ∞,_ _**x** ∈_ � _[d] ,_ _**y** ∈_ � _[d] ,_ 0 _< K_ 1, _K_ 2 _< ∞ and where ||·|| denotes the L_[2] _norm. On some_ 

46 

_probability space_ ( _Ω_ , _�_ , �) _, let_ _**ξ** be an_ � _[d] -valued random vector, independent of the r–dimensional Brownian motion W_ = ( _**W** t_ , _�t_ ;0 _≤ t < ∞_ ) _, and with finite second moment. Let {�t } be as in Eq. (B.9). Then there exists a continuous, adapted process X_ = ( _**X** t_ , _�t_ ;0 _≤ t < ∞_ ) _which is a strong solution of Eq. (B.10) relative to W, with initial condition_ _**ξ** . This process is square-integrable._ 

## **B.2 SDE coefficients of the** _h_ **–transform quantile diffusion** 

The dynamics of the _h_ –transform quantile diffusion are obtained by Proposition B.1, where we can write the density function of the _h_ –transform distribution as 

**==> picture [219 x 15] intentionally omitted <==**

where _u_ = _Fφh_ ( _z_ ) and _**ξ**_ = ( _A_ , _B_ , _g_ ). Here, _Fφh_ = _Q[−] φh_[can][be][computed][analytically.][Taking] _[A]_[ =] 0, _B_ = 1 with no loss of generality for the standardised case, we have the following for the drift function of the _h_ –transform quantile diffusion: 

**==> picture [441 x 103] intentionally omitted <==**

for a time–homogeneous _F_ that is the “false law” of the driving process, and 

**==> picture [443 x 84] intentionally omitted <==**

when _F_ is the “true law” of ( _Yt_ ) with _f_ the corresponding transition density. The volatility function is given by 

**==> picture [387 x 40] intentionally omitted <==**

The argument of the drift and diffusion coefficients are given by _µ_ ( _·_ , _·_ ) := _µ_ ( _t_ , _Q_ ( _t_ , _Fφh_ ( _z_ ))) and _σ_ ( _·_ , _·_ ) := _σ_ ( _t_ , _Q_ ( _t_ , _Fφh_ ( _z_ ))), respectively. In the case where we are using a non time–dependent distribution function in our mapping, we replace _f_ ( _t_ , _Q_ ( _t_ , _Fφh_ ( _z_ ))) by _f_ ( _Q_ ( _Fφh_ ( _z_ ))) in Eq. (B.15). 

**Corollary B.2.** _Let_ ( _Zt_ ) _be a g–transform quantile process given by Definition 5.4, where the drift coefficient is given by either Eq. (_ **??** _) or (_ **??** _), and the volatility coefficient by Eq. (_ **??** _). Let_ ( _Yt_ )0 _≤t<∞ be a homogeneous driving process satisfying_ d _Yt_ = _µ_ d _t_ + _σ_ d _Wt for µ ∈_ � _, σ ∈_ �[+] _, and Y_ 0 = _y_ 0 _∈_ � _. Then the coefficients of_ ( _Zt_ ) _are Lipschitz continuous on_ [ _−_ 1 _/g_ , _∞_ ) _, for g ∈_ (0, _∞_ ) _, if the density function f_ ( _t_ , _y_ ) _, associated with the law F•_ ( _t_ , _y_ ) _, for all t ∈_ [ _t_ 0, _∞_ ) _has both left and right tail–decay_ 

47 

_to zero, is bounded on its support, and it is such that the following set of conditions is satisfied:_ 

**==> picture [439 x 222] intentionally omitted <==**

_In the case where g ∈_ ( _−∞_ ,0) _, the conditions that must be satisfied are the same as the above, however the limits are taken as z →−∞ and z →−_ 1 _/g[−] to show Lipschitz continuity of the drift and volatility coefficients on_ ( _−∞_ , _−_ 1 _/g_ ] _._ 

_Proof._ In order for the drift and volatility coefficients given by Eqs ( **??** ) to ( **??** ) to be Lipschitz continuous, their first derivative must be bounded on the range on which they are differentiable everywhere. The first derivatives with respect to _z_ of these expressions are given by 

**==> picture [439 x 231] intentionally omitted <==**

and 

respectively. 

It follows that satisfying the limits in the Proposition ensures Eqs (B.24) to (B.26) are bounded for all _t ∈_ [ _t_ 0, _∞_ ) and _z ∈_ [ _−_ 1 _/g_ , _∞_ ) for _g ∈_ (0, _∞_ ), or _z ∈_ ( _−∞_ , _−_ 1 _/g_ ] for _g ∈_ ( _−∞_ ,0). 

48 

## **B.3 Lipschitz continuity of the** _h_ **–transform quantile diffusion drift and volatility functions** 

**Proposition B.2.** _Let_ ( _Zt_ ) _be a h–transform quantile process given by Definition 5.6, where the drift coefficient is given by either (B.13) or (B.14), and the volatility coefficient by Eq. (B.15). Let_ ( _Yt_ )0 _≤t<∞ be a homogeneous driving process satisfying_ d _Yt_ = _µ_ d _t_ + _σ_ d _Wt for µ ∈_ � _, σ ∈_ �[+] _, and Y_ 0 = _y_ 0 _∈_ � _. Then the coefficients of_ ( _Zt_ ) _are Lipschitz continuous on_ ( _−∞_ , _∞_ ) _if the density function f_ ( _t_ , _y_ ) _, associated with the law F•_ ( _t_ , _y_ ) _, for all t ∈_ [ _t_ 0, _∞_ ) _has left and right tail decay to zero, is bounded on its support, and it is such that the following set of conditions is satisfied:_ 

**==> picture [383 x 105] intentionally omitted <==**

**==> picture [378 x 197] intentionally omitted <==**

_Proof._ The proof is analogous to that of Proposition B.2. It consists of computing the first partial derivatives of the drift and volatility coefficients given by Eqs (B.13) to (B.15), and finding the conditions that must be satisfied by _f_ ( _t_ , _y_ ) for all _t ∈_ [ _t_ 0, _∞_ ) to ensure that these expressions are bounded on the range on which they are differentiable everywhere. 

## **C Overivew of existing quantile process representations** 

In this section we introduce our approach to constructing stochastic quantile processes in continuous time. We highlight differences and distinguish between our approach proposed in this paper and existing approaches to studying quantile dynamics. 

We recall three approaches for the definition of quantile processes, in order to differentiate them from the use of this terminology in our constructions. In much of the literature the formulation adopted in [10] is invoked when one refers to a quantile process, and it is based on the univariate, empirical quantile process given in Definition C.1. 

**Definition C.1.** _Let Y_ 1, _Y_ 2,..., _Yn be a sequence of i.i.d. random variables with a continuous distribution function FY , and let Y_ (1, _n_ ) _≤ Y_ (2, _n_ ) _≤_ ... _≤ Y_ ( _n_ , _n_ ) _denote the order statistics of the random sample Y_ 1, _Y_ 2,..., _Yn. Define the empirical distribution function Fn_ ( _y_ ) _and the quantile function Qn_ ( _u_ ) 

49 

_as follows:_ 

**==> picture [260 x 51] intentionally omitted <==**

**==> picture [223 x 24] intentionally omitted <==**

_The empirical quantile process is defined by qn_ ( _u_ ) = _n_[1] _[/]_[2][ �] _Qn_ ( _u_ ) _− FY[−]_[(] _[u]_[)] � _for_ 0 _< u <_ 1 _._ 

This definition relates to the convergence of the law of the order statistics of an empirical process, which is observed as a sequence of independent and identically distributed (i.i.d.) random variables from a fixed distribution _FY_ . 

The second widely adopted definition of a quantile process, this time in the context of a quantile diffusion (in particular the quantile of a Brownian motion with drift) is given as follows, see [12, 14]. The extension to processes with stationary and independent increments is given in [13]. 

**Definition C.2.** _Let_ ( _Ω_ , _�_ , ( _�t_ ), � _[µ]_ ) _be a probability space where_ � _[µ] denotes the law of the Brownian motion with drift_ ( _Yt_ )0 _≤t<∞, given by Yt_ := _Wt_ + _µt for µ ∈_ � _, on the canonical space_ ( _C_ (�+, �), _�∞_ ) _, and where �t_ = _σ_ (( _Ys_ )0 _≤s≤t_ ) _, t ∈_ [0, _∞_ ) _. For α ∈_ [0,1] _and ω ∈ Ω, define the α-quantile diffusion_ ( _Mt_[(] _[α]_[)] ) _t>_ 0 _by_ 

**==> picture [333 x 31] intentionally omitted <==**

_For fixed ω, Mt_[(] _[α]_[)] ( _ω_ ) _is the α-quantile of the function s �→ Ys_ ( _ω_ ) _, for s < t, which is considered as a random variable on the space_ ([0, _t_ ];d _s/t_ ) _equipped with the Borel σ–field._ 

This definition, whilst it is a quantile diffusion, is different to the one we propose in our construction in the sense that we are not looking directly at the quantiles of a diffusion process. Rather we produce a quantile diffusion that implicitly induces some underlying diffusion process. This implicit underlying process will not be of primary interest in our formulation, as instead we wish to focus on characterising and constructing diffusions on the quantile space with non–trivial skew–kurtosis and tail characteristics that can be parameterised and interpreted. As such we develop parameterised mappings of an underlying diffusion process in such a way that the resulting quantile diffusions are not the quantiles of the underlying driving diffusion, as produced in Definition C.2, but rather will imply such a process without ever requiring its explicit specification. 

A third characterisation of quantile processes is also widely adopted in the statistics and econometrics time series literature, see [25], where a regression framework is developed for (linear or nonlinear) conditional quantile functions at any, or over all, quantile levels _u ∈_ [0,1]. As an example, one may consider the following definition, given in the tutorial review of various models in [29], which allows for the autoregressive parameters of the model to vary with the quantile level—see also [24, 26]. 

**Definition C.3.** _Consider a univariate time series {Y_ 1,..., _Yt_ ,... _} for t ∈_ � _and let �t_ = _σ_ ( _Y_ 1,..., _Yt_ ) _denote the natural σ–algebra of the observed time series. Let_ _**θ** ∈_ � _[d] be a static vector of model parameters, u ∈_ [0,1] _a quantile level, and αi_ ( _u_ ) : [0,1] _→_ � _be unknown quantile functions, given by Definition_ **??** _, for i_ = 1,..., _p. The conditional quantile autoregressive QAR(p) model for the conditional quantile function of the random variable Yt , conditioned on the observations of the time series until time t −_ 1 _, is characterised by_ 

**==> picture [322 x 31] intentionally omitted <==**

50 

_where Qε_ ( _u_ ; _γ_ ) _denotes the quantile error function, representing the white noise sequence_ ( _εt_ ) _t_ =1,2,... _with γ ∈_ � _[d][′] a vector of static parameters._ 

By construction, Eq. (C.2) is a discrete–time, function–valued quantile process for the conditional quantile function of _Yt_ . This is just one approach to the construction of conditional quantile processes; an alternative non–parametric approach is given in [5]. Additionally, a model of this form also admits a quantile time series model, i.e., the underlying time series model is a sequence of quantile levels. However the direct link between two such models may not always be easily obtained in closed form. The definition of this model is given as follows for a random–level quantile time series. 

**Definition C.4.** _Consider the setup given in Definition C.3, where { y_ 0, _y_ 1,..., _yt−_ 1 _} are observations of the time series until time t −_ 1 _, and Ut ∼ U_ [0,1] _for all t ∈_ � _i.i.d.. The functional time series model with random coefficients in an AR structure is given by_ 

**==> picture [344 x 31] intentionally omitted <==**

_where_ 

**==> picture [282 x 31] intentionally omitted <==**

_is a monotone increasing function of Ut and_ ( _εt_ ) _t_ =1,2,... _is a white noise sequence, independent of Ut ._ 

A framework for the construction of such models with specific properties is detailed in [29]. Moreover, one may consider the random coefficients in Definition C.3 to be co–monotonic random functional coefficients, so to define a scalar on function regression version of Eq. (C.2). That is, the AR coefficients are now expressed as monotone functions of a scalar random variable by 

**==> picture [297 x 32] intentionally omitted <==**

for i.i.d. _Ut ∼ U_ [0,1]. See Example 1 in [29] for more details and a discussion on the advantages of constructing such a model. 

The above characterisations of quantile processes is not exhaustive, but represents quantile processes usually encountered in time series statistics and econometrics literature. 

## **D Connection Random-Level and Function-Valued Quantile Processes** 

## **D.0.1 Example I** 

Consider a uniformly distributed random variable _X ∼ U_ [ _a_ , _b_ ] where _−∞ < a < b < ∞_ . Take _a_ = 0 and let the parameter ( _bt_ )0 _≤t<∞_ be stochastic, satisfying the SDE **??** where _µ_ ( _t_ , _x_ ) : �[+] _×_ �[+] _→_ � and _σ_ ( _t_ , _x_ ) : �[+] _×_ �[+] _→_ �[+] satisfy the necessary conditions to ensure _bt >_ 0 for all _t ∈_ [0, _∞_ ). Using Definition **??** , we construct a uniformly–distributed function–valued quantile diffusion by _Zt_ ( _u_ ) = _QX_ ( _u_ ; _bt_ ) = _ubt_ for _u ∈_ [0,1]. Fixing _u_ = ¯ _u ∈_ [0,1], the process _Zt[u]_[¯][=][ ¯] _[ub][t]_[satisfies the SDE] d _Z[u]_[¯] _t_[=][ ¯] _[u][µ]_[(] _[t]_[,] _[ Z]_[ ¯] _t[u][/][u]_[¯][)][d] _[t]_[ +][ ¯] _[u][σ]_[(] _[t]_[,] _[ Z]_[ ¯] _t[u][/][u]_[¯][)][d] _[W][t]_[.] 

Taking this to be the SDE satisfied by the driving process ( _Yt_ ) in Definition **??** , one obtains a special case of a random–level quantile diffusion driven by the parameter process ( _bt_ ), producing output quantiles at level _u_ ¯ _∈_ [0,1]. 

51 

## **D.0.2 Example II** 

Consider some random variable _X_ 2 _∼ FX_ 2 that belongs to the location–scale family with location _d_ parameter _A ∈_ � and scale parameter _B ∈_ �[+] , that is _X_ 2 = _A_ + _BX_ 1 for any random variable _X_ 1 _∼ FX_ 1. Take _B_ = 1 and let the location parameter ( _At_ )0 _≤t<∞_ be stochastic, satisfying the SDE **??** with associated law _FA_ ( _t_ , _a_ )0 _<t<∞_ . Using Definition **??** , we construct a location–scale, function– valued quantile diffusion by _Zt_ ( _u_ ) = _QX_ 1( _u_ )+ _At_ for all _t ∈_ [0, _∞_ ) and _u ∈_ [0,1]. Fix _u_ = ¯ _u ∈_ [0,1] and define a distribution function _FY_ ( _t_ , _y_ ) = _FA_ ( _t_ , _y − QX_ 2( _u_ ¯)) for all _t ∈_ (0, _∞_ ). For some choice of the functions _Qζ_ and _F_ in Definition **??** , one can produce equivalent quantile diffusions in the two following ways: 

1. Using the function–valued construction, taking Eq. ( **??** ) with _QY_ the quantile function corresponding to the distribution function _FY_ ( _t_ , _y_ ) = _FA_ ( _t_ , _y − QX_ 2( _u_ ¯)). 

2. By _Zt_ = _Qζ_ ( _F_ ( _t_ , _Zt[u]_[¯][))][ where] _[Z]_[ ¯] _t[u]_[=] _[ Q][X]_ 1[(] _[u]_[¯][) +] _[ A][t]_[for each] _[t][∈]_[(][0,] _[∞]_[)][.][This is a special case of a] random–level quantile diffusion, where the driving process is the location parameter process ( _At_ ) and ( _Zt_ ) models quantiles at the chosen level _u_ ¯. 

52 

