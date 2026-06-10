## **Asynchronous Regime-Switching Multivariate CIR Spot-Rate Models** 

## **via Onsager–Machlup Topological HMM Inference** 

Gareth W. Peters Minxing Xu Zimo Zhu Peilun He April 26, 2026 

## **Abstract** 

We develop a multivariate spot-rate modelling and inference framework in which each rate (or factor) follows square-root (CIR-type) diffusion dynamics while regimes switch _asynchronously_ across assets. Cross-sectional dependence is introduced either through instantaneous Gaussian correlation at the diffusion level or via Gaussian/Student- _t_ copulas imposed on discretized innovations. Inference is performed using a Topological Hidden Markov Model (THMM) approach based on Onsager–Machlup (OM) functionals, extending OM-based regime-switching inference for polynomial diffusions to positive-state interest-rate systems. We derive continuous-time and discrete-time OM emission costs for CIR families (coordinate-wise, factor, and Wishart-type constructions), propose robust Student- _t_ OM penalties compatible with tail risk, and provide EM/Viterbi-style algorithms for asynchronous regime decoding and parameter learning. 

## **1 Introduction** 

## **1.1 Motivation: asynchronous regimes in the term structure** 

Empirically, yield curve segments respond to different drivers with different time scales: short maturities react sharply to monetary policy and liquidity, while long maturities reflect slow-moving macro and risk-premium regimes. A single common regime process (synchronous switching) is often too rigid. We therefore model each component (spot rate by maturity or factor) with its own latent regime process, allowing regime changes to occur at distinct times per asset, while still permitting joint dependence via correlated drivers or copulas. 

## **1.2 Contribution and relation to THMM literature** 

Our methodological foundation follows the topological HMM paradigm in which emission densities are replaced (or augmented) by path-likelihood surrogates derived from Onsager–Machlup functionals. This extends the framework developed for regime-switching polynomial diffusions in Peters et al. [2025] ( _attached paper_ ) to multivariate CIR spot-rate models with positivity constraints, heavy tails, and asynchronous regime switching. 

1 

## **2 Notation and set-up** 

Let _Xt_ = ( _Xt_[(1)] _, . . . , Xt_[(] _[d]_[)] ) _[⊤] ∈_ R _[d]_ +[denote][a][vector][of][spot][rates][(or][state][variables][that][map][to][spot] rates). Observations occur on a grid _tk_ = _k_ ∆, _k_ = 0 _, . . . , T_ . 

We consider two dependence layers: (i) continuous-time dependence via correlated Brownian motions; (ii) discretized dependence via copulas coupling innovations. We distinguish three modelling granularities: 

- **Model A (coordinate-wise CIR):** each component is CIR with possibly correlated drivers. 

- **Model B (factor CIR):** a low-dimensional CIR factor drives multiple rates. 

- **Model C (Wishart square-root):** matrix-valued square-root diffusion induces multivariate dependence. 

## **3 Asynchronous regime processes** 

## **3.1 Per-asset regime processes** 

For each asset _j ∈{_ 1 _, . . . , d}_ , define a continuous-time Markov chain 

**==> picture [270 x 18] intentionally omitted <==**

Let _**S** t_ := ( _St_[(1)] _, . . . , St_[(] _[d]_[)] ) denote the regime configuration. 

**Remark 1** (Joint Markov structure) **.** _If the chains {S_[(] _[j]_[)] _} are independent, then_ _**S** t is a continuoustime Markov chain on the product state space K_ :=[�] _[d] j_ =1 _[{]_[1] _[, . . . , K][j][}][with][generator]_ 

**==> picture [355 x 60] intentionally omitted <==**

_More general dependence across regime chains can be modelled by a coupled generator on K, but independence already yields asynchronous switching times across assets._ 

## **3.2 Discrete-time regime transitions on an observation grid** 

On _tk_ = _k_ ∆, each chain has transition matrix _A_[(] _[j]_[)] (∆) = exp( _Q_[(] _[j]_[)] ∆). If chains are independent, the joint transition on _K_ factorizes: 

**==> picture [174 x 35] intentionally omitted <==**

This factorization is crucial for scalable inference. 

2 

## **4 Multivariate CIR spot-rate dynamics with asynchronous regimes** 

## **4.1 Model A: coordinate-wise CIR with correlated Brownian drivers** 

Conditional on _St_[(] _[j]_[)] = _ij_ , define the _j_ -th marginal drift and diffusion: 

**==> picture [232 x 21] intentionally omitted <==**

Let _Bt_ = ( _Bt_[(1)] _, . . . , Bt_[(] _[d]_[)] ) _[⊤]_ be a Brownian motion with instantaneous correlation matrix _ρ_ _**S** t ∈_ R _[d][×][d]_ (possibly dependent on the _configuration_ _**S** t_ ). Equivalently, write 

**==> picture [158 x 12] intentionally omitted <==**

with 

**==> picture [230 x 17] intentionally omitted <==**

and 

**==> picture [360 x 15] intentionally omitted <==**

The instantaneous covariance is 

**==> picture [190 x 14] intentionally omitted <==**

## **4.2 Model B: factor CIR with regime-dependent loadings** 

Let _Yt ∈_ R _[r]_ +[follow CIR components with their own asynchronous regimes (or one can place regimes] only on factors). For concreteness: 

**==> picture [344 x 22] intentionally omitted <==**

Observed spot rates are affine in factors: 

**==> picture [88 x 12] intentionally omitted <==**

allowing regime-dependent level shifts and factor loadings. 

## **4.3 Model C: Wishart square-root diffusion** 

Let _Vt ∈_ S _[d]_ +[follow][a][(regime-modulated)][Wishart][diffusion.][Under][configuration] _**[i]**_[:] 

**==> picture [290 x 15] intentionally omitted <==**

and define scalar rates by linear functionals _Xt_[(] _[j]_[)] = _⟨Aj, Vt⟩_ . 

3 

## **5 Existence, positivity, and boundary behaviour** 

## **5.1 Positivity constraints (CIR/Feller)** 

For each marginal CIR component, a standard sufficient condition to avoid boundary hitting is the Feller condition 

**==> picture [82 x 16] intentionally omitted <==**

In practice, observed short rates may be near zero; one can allow boundary accessibility and use reflecting/truncation schemes in discretization or shift models _Xt_[(] _[j]_[)] = _cj_ + _X_[˜] _t_[(] _[j]_[)] . 

## **6 Onsager–Machlup functionals for asynchronous multivariate CIR** 

## **6.1 Derivation: general diffusion OM functional (multivariate)** 

Consider a _d_ -dimensional Itˆo diffusion 

**==> picture [254 x 14] intentionally omitted <==**

Under regularity (smooth coefficients, nondegenerate Γ), the OM functional (negative log tube probability) for an absolutely continuous path _ϕ_ : [0 _, T_ ] _→_ R _[d]_ is of the form 

**==> picture [400 x 28] intentionally omitted <==**

up to additive constants _C_ independent of _ϕ_ (details depend on the convention and curvature terms). 

In the THMM setting, we use (1) as a regime-dependent _emission cost_ . 

## **6.2 Asynchronous regimes: OM functional under configuration** _i_ 

For Model A under configuration _**i** ∈K_ : 

**==> picture [417 x 101] intentionally omitted <==**

Since _µ_ _**i**_ is coordinate-wise, 

a constant in time for fixed _**i**_ (important simplification for CIR). 

Thus, for fixed _**i**_ , the divergence term contributes _−_ (1 _/_ 2) _T_[�] _j[κ][i] j[,j]_[plus][a][constant.][Conse-] quently, the discriminating part of the OM score is primarily the quadratic form term. 

4 

## **6.3 Explicit quadratic form for correlated CIR drivers** With Γ _**i**_ ( _ϕ_ ) = _D_ _**i**_ ( _ϕ_ ) _ρ_ _**i** D_ _**i**_ ( _ϕ_ ), 

**==> picture [364 x 27] intentionally omitted <==**

Define residual velocities 

**==> picture [114 x 14] intentionally omitted <==**

Then the OM integrand becomes 

**==> picture [298 x 29] intentionally omitted <==**

## **6.4 Coordinate-wise OM approximation (diagonal metric)** 

A scalable alternative ignores cross-covariances in Γ: 

**==> picture [306 x 35] intentionally omitted <==**

This form is especially convenient for asynchronous regimes, because it decomposes by coordinate. 

## **6.5 Robust Student-** _t_ **OM functional (continuous time)** 

To penalize outliers, define the local quadratic form 

**==> picture [142 x 14] intentionally omitted <==**

and a robustified (pseudo) action 

**==> picture [320 x 28] intentionally omitted <==**

This corresponds to replacing Gaussian increments with Student- _t_ increments at small scales, and matches the discrete Student- _t_ emission derived below. 

## **7 Discretization and exact transitions** 

## **7.1 Euler–Maruyama with positivity truncation** 

On _tk_ = _k_ ∆, under configuration _**i** k_ , 

**==> picture [282 x 14] intentionally omitted <==**

5 

with truncation _Xk_[+] = max( _Xk,_ 0) componentwise. When using copulas, _εk_ is replaced by a dependence-coupled vector with prescribed marginals. 

## **7.2 Exact CIR marginal transitions** 

For each marginal CIR (ignoring correlation), the transition has a noncentral _χ_[2] law: 

**==> picture [176 x 18] intentionally omitted <==**

with 

**==> picture [340 x 32] intentionally omitted <==**

This exact marginal can be combined with copula dependence by mapping each marginal transition to uniforms. 

## **8 Copula dependence for discretized innovations** 

## **8.1 Copula-coupled exact transitions** 

Under configuration _**i** k_ , for each _j_ define the marginal CDF 

**==> picture [130 x 19] intentionally omitted <==**

where _Fi_[(] _[j]_[)] is the CIR transition CDF under regime _i_ . Then ( _Uk_[(1)] +1 _[, . . . , U] k_[(] _[d]_ +1[)][)][is][coupled][via][a] copula _C_ _**i** k_ : ( _Uk_[(1)] +1 _[, . . . , U] k_[(] _[d]_ +1[)][)] _[ ∼][C]_ _**[i]** k[.]_ 

Two key cases: 

- **Gaussian copula:** _C_ _**i**_ = GaussCop( _ρ_ _**i**_ ). 

- **Student-** _t_ **copula:** _C_ _**i**_ = tCop( _ρ_ _**i** , ν_ _**i**_ ). 

This construction preserves exact CIR marginals while modelling tail dependence through _ν_ _**i**_ . 

## **9 Discrete Onsager–Machlup emissions for THMM inference** 

## **9.1 Residual-based OM emission (Gaussian)** 

Define the (Euler) residual 

**==> picture [168 x 27] intentionally omitted <==**

Under Gaussian diffusion approximation, _Rk_ has covariance Γ _**i** k_ ( _Xk_ ). A negative log-likelihood (up to constants) is 

**==> picture [353 x 23] intentionally omitted <==**

6 

This is the discrete analogue of (2) and is used as a THMM emission cost. 

## **9.2 Robust Student-** _t_ **emission** 

For _ν_ _**i** >_ 2, define 

**==> picture [393 x 29] intentionally omitted <==**

This yields heavy-tailed robustness and matches the continuous-time robust action. 

## **9.3 Coordinate-wise emissions** 

When using diagonal approximation, 

**==> picture [236 x 35] intentionally omitted <==**

This decomposes across _j_ and makes asynchronous decoding scalable. 

## **10 Asynchronous HMM/THMM inference** 

## **10.1 Joint-state formulation and complexity** 

If we treat _**S** k ∈K_ as a single HMM state, the number of regimes is _|K|_ =[�] _[d] j_ =1 _[K][j]_[(exponential] in _d_ ). We avoid this by exploiting: 

- factorized regime transitions (independent chains), and 

- additive (or structured) emission costs (coordinate-wise or sparse dependence). 

## **10.2 EM / Baum–Welch with OM emissions (THMM)** 

Let _αk_ ( _**i**_ ) and _βk_ ( _**i**_ ) be forward/backward messages on _K_ . With OM-based emissions, replace the usual emission density _b_ _**i**_ ( _Xk_ ) by 

**==> picture [142 x 15] intentionally omitted <==**

where _I_ _**i** k_ ( _k_ ) is one of (3) or (4). 

Then the forward recursion becomes 

**==> picture [196 x 34] intentionally omitted <==**

7 

and similarly for _βk_ . Posterior responsibilities are 

**==> picture [92 x 12] intentionally omitted <==**

When transitions factorize and emissions decompose, these can be computed approximately by mean-field or structured variational message passing (details omitted here but straightforward). 

## **10.3 Viterbi decoding (MAP regimes) with OM emissions** 

Define the Viterbi score 

**==> picture [204 x 17] intentionally omitted <==**

Backtracking yields the most probable asynchronous regime path _**S**_ 0: _[⋆] T_[.] 

## **10.4 Per-asset decoding under coordinate-wise emissions** 

If _I_ _**i**_ ( _k_ ) =[�] _[d] j_ =1 _[I] i_[(] _j[j]_[)][(] _[k]_[)][and][transitions][factorize,][then] _**[S]**[⋆]_[decomposes][into] _[d]_[separate][Viterbi] problems: 

**==> picture [208 x 21] intentionally omitted <==**

which is _O_ ( _dKj_[2] _[T]_[) rather than exponential.][This is the key computational advantage of coordinate-] wise OM scoring for asynchronous regimes. 

## **11 Parameter learning: regime-specific CIR parameters and copula parameters** 

## **11.1 CIR parameter updates (sketch)** 

Under EM, maximize the expected complete-data objective 

**==> picture [238 x 26] intentionally omitted <==**

For coordinate-wise emissions, updates separate by _j_ and by regime _i_ . For example, under Euler Gaussian OM, each regime _i_ for asset _j_ solves a weighted (quasi) likelihood for ( _κi,j, θi,j, σi,j_ ). 

## **11.2 Copula parameter updates** 

If copula dependence is used, copula parameters ( _ρ_ _**i** , ν_ _**i**_ ) are updated via weighted copula loglikelihood on pseudo-observations ( _Uk_[(] _[j]_ +1[)][)][with][weights] _[γ][k]_[(] _**[i]**_[):] 

**==> picture [204 x 26] intentionally omitted <==**

8 

where _c_ _**i**_ is the copula density. 

## **12 Identifiability and modelling choices** 

**Assumption 1** (Separation) **.** _For each j, the regime-specific parameter sets_ Θ _i,j are distinct enough that the induced increment distribution is not identical across regimes on sets of nonzero probability._ 

**Remark 2** (Label switching) **.** _As with all HMMs, regimes are identifiable up to permutation. In asynchronous models, this holds per asset; a consistent labelling convention is needed across maturities if interpretation is required._ 

**Remark 3** (When to use multivariate vs coordinate-wise OM) **.** _Multivariate OM scoring is preferable when instantaneous correlation is structurally important and stable. Coordinate-wise OM + copula is preferable when dependence is heavy-tailed or tail-dependent and/or when scalable asynchronous inference is required._ 

## **13 Derivative-consistent calibration (outline)** 

In fixed income, one may incorporate option-implied information (caps/floors/swaptions) by constraining paths or by adding penalty terms that encourage agreement between model-implied and market-implied volatility surfaces. This is analogous to the option-implied expected-move augmentation in the attached THMM work, but applied to rate derivatives (e.g., swaption smile or caplet IV term structure). 

A generic approach: add a regularization term 

**==> picture [179 x 26] intentionally omitted <==**

to the EM M-step objective, where _m_ indexes instruments (caplets, swaptions) and _σ_ denotes implied vols. 

## **14 Case Study: Multiple Swaption Pricing and Calibration under Asynchronous Regime-Switching CIR Models** 

This section presents a detailed worked example for pricing and calibrating a _panel of swaptions_ under the proposed _asynchronous regime-switching multivariate CIR_ spot-rate framework with _copula dependence_ and _Onsager–Machlup (OM) / THMM_ inference. The goal is to demonstrate: (i) model specification in risk-neutral form, (ii) path simulation with asynchronous regimes and heavy-tailed dependence, (iii) swaption pricing and implied-vol extraction for multiple instruments, and (iv) joint time-series and derivative-consistent calibration using OM-based emissions. 

9 

## **14.1 Swaption panel and market data** 

Fix a calibration date _t_ = _t_ 0 and consider a panel of payer swaptions indexed by _m_ = 1 _, . . . , M_ , each defined by an option expiry _Te_[(] _[m]_[)] and underlying swap tenor _Ts_[(] _[m]_[)] . A canonical grid is 

**==> picture [204 x 12] intentionally omitted <==**

so _M_ = 9 instruments. Market quotes are assumed available as ATM Black implied volatilities _σm_[mkt] (or alternatively as premium prices). Throughout, we treat ATM swaptions with strike set to the model-implied forward swap rate at time _t_ 0. 

Let _t_ 0 _< Te < T_ 1 _< · · · < Tn_ = _Te_ + _Ts_ denote fixed-leg payment dates with accrual factors _δi_ (e.g. annual fixed leg so _δi_ = 1). Let _P_ ( _t, T_ ) denote the discount factor under OIS discounting (or a chosen discount curve). 

## **14.2 Model state: rate assets (key-rate / segment factors)** 

We model a small set of _d_ positive rate components (“rate assets”) that drive the term structure. A practical choice is _d_ = 3 segment factors: 

- _Xt_[(1)] : short-end factor (e.g. 0–2Y dynamics), 

- _Xt_[(2)] : belly factor (e.g. 2–7Y dynamics), 

- _Xt_[(3)] : long-end factor (e.g. 7Y+ dynamics), 

**==> picture [174 x 16] intentionally omitted <==**

In empirical implementations, one may take _Xt_ as observed key rates (thus no measurement error), or treat _Xt_ as latent and map observed yields/rates via a measurement equation _Yt_ = _h_ ( _Xt_ ) + _ϵt_ . For the present example we take _Xtk_ as observed (or pre-extracted). 

## **14.3 Risk-neutral dynamics with asynchronous regimes** 

## **14.3.1 Asynchronous regime chains** 

Each component _j ∈{_ 1 _, . . . , d}_ has its own latent regime process 

**==> picture [90 x 16] intentionally omitted <==**

a continuous-time Markov chain with generator _Q_[(] _[j]_[)] and grid-step transition matrix 

**==> picture [174 x 14] intentionally omitted <==**

10 

The regime configuration at time _t_ is _**S** t_ = ( _St_[(1)] _, . . . , St_[(] _[d]_[)] ). Independence of the regime chains implies factorization of the joint transition on the grid: 

**==> picture [176 x 35] intentionally omitted <==**

which is central for scalable decoding and EM updates. 

## **14.3.2 CIR dynamics under local regimes** 

Under risk-neutral measure Q, conditional on _St_[(] _[j]_[)] = _i_ , we specify marginal CIR-type dynamics 

**==> picture [386 x 20] intentionally omitted <==**

Positivity is preserved by construction, and the Feller condition 2 _κi,jθi,j ≥ σi,j_[2][may][be][enforced] (optional) per regime. 

## **14.3.3 Cross-sectional dependence: Gaussian diffusion vs copula innovations** 

We consider two dependence specifications: 

1. **Instantaneous Gaussian dependence (diffusion-level):** the Brownian motion ( _Bt_[(1)] _, . . . , Bt_[(] _[d]_[)] ) has instantaneous correlation _ρ_ _**S** t_ (potentially configuration-dependent), so that 

**==> picture [108 x 16] intentionally omitted <==**

2. **Copula dependence at increment level:** after discretization, we impose dependence by coupling the marginal transitions using a copula. This is often preferable for stress-period co-movement via tail dependence. 

## **14.4 From factors to discount curve and swap rates** 

## **14.4.1 Short-rate mapping** 

Define a nonnegative affine mapping from factors to the instantaneous short rate: 

**==> picture [335 x 35] intentionally omitted <==**

This provides a consistent discounting mechanism under Q: 

**==> picture [326 x 28] intentionally omitted <==**

11 

With asynchronous regimes and copula coupling, closed forms are generally unavailable; thus we use Monte Carlo. 

## **14.4.2 Swap annuity and forward swap rate** 

For expiry _Te_ and tenor _Ts_ , with payment dates _Te < T_ 1 _< · · · < Tn_ = _Te_ + _Ts_ and accruals _δi_ , define the annuity and forward swap rate at time _t_ : 

**==> picture [315 x 72] intentionally omitted <==**

## **14.5 Swaption payoff and pricing** 

## **14.5.1 Payoff** 

A payer swaption with strike _K_ expiring at _Te_ has payoff 

**==> picture [336 x 16] intentionally omitted <==**

## **14.5.2 Risk-neutral price** 

The time- _t_ value is 

**==> picture [402 x 29] intentionally omitted <==**

**14.5.3 Monte Carlo estimator** 

We approximate (11) using _M_ simulated paths of ( _Xu,_ _**S** u_ ) from _u_ = _t_ to _Tn_ . Let _{tk}_ be a simulation grid with step ∆(e.g. monthly) including all relevant payment dates. For path _m_ define the discount factor 

**==> picture [296 x 34] intentionally omitted <==**

and compute _P_[(] _[m]_[)] ( _Te, Ti_ ) for _i_ = 1 _, . . . , n_ via 

**==> picture [306 x 34] intentionally omitted <==**

12 

Then 

**==> picture [323 x 31] intentionally omitted <==**

**==> picture [322 x 30] intentionally omitted <==**

where _P_[(] _[m]_[)] ( _Te, Te_ ) = 1. The Monte Carlo price estimator is 

**==> picture [394 x 34] intentionally omitted <==**

## **14.5.4 Model implied Black volatility** 

Given an observed-time annuity _A_ ( _t_ ; _Te, Ts_ ) and forward swap rate _S_ ( _t_ ; _Te, Ts_ ), define _σ_[model] as the solution to 

**==> picture [310 x 16] intentionally omitted <==**

For ATM calibration we take _K_ = _S_ ( _t_ ; _Te, Ts_ ) (either from market curve or model curve). 

## **14.6 Simulation of the asynchronous regime-switching CIR under copula coupling** 

## **14.6.1 Exact CIR marginal transition (noncentral** _χ_[2] **)** 

For each component _j_ with regime _i_ = _St_[(] _k[j]_[)][,][the][CIR][transition] _[X] t_[(] _k[j]_ +1[)] _[|][ X] t_[(] _k[j]_[)][has][the][exact][form] 

**==> picture [106 x 18] intentionally omitted <==**

where 

**==> picture [405 x 32] intentionally omitted <==**

Let _Fi,j_[CIR] ( _· | x_ ) denote the resulting transition CDF. 

## **14.6.2 Copula coupling across marginals** 

To impose dependence across components while preserving exact marginals, define uniforms 

**==> picture [220 x 18] intentionally omitted <==**

and impose a copula model under regime configuration _**i** k_ : 

**==> picture [114 x 17] intentionally omitted <==**

Two standard choices are: 

13 

- Gaussian copula _C_ _**i**_ = GaussCop( _ρ_ _**i**_ ), 

- Student- _t_ copula _C_ _**i**_ = tCop( _ρ_ _**i** , ν_ _**i**_ ). 

The Student- _t_ copula provides tail dependence and is particularly suited for stress co-movements in rates. 

A convenient regime-driven tail mechanism is to let _ν_ _**i**_ depend on a stress indicator, e.g. _ν_ _**i**_ = 6 when at least two components are in their high-volatility regimes, otherwise _ν_ _**i**_ = 20. 

## **14.6.3 Simulation step (pathwise)** 

At time _tk_ given ( _Xtk ,_ _**S** tk_ ): 

1. Simulate each regime chain _St_[(] _k[j]_ +1[)] _[∼][A]_[(] _[j]_[)][(∆)][independently.] 

**==> picture [284 x 17] intentionally omitted <==**

3. For each _j_ , set 

**==> picture [168 x 18] intentionally omitted <==**

4. Compute _rtk_ via (6) and update discount products. 

## **14.7 A concrete numerical specification (illustrative)** 

We provide an illustrative specification for _d_ = 3 components, each with _Kj_ = 2 regimes: regime 1 (calm) and regime 2 (stressed). Regime transition generators (annualized) are 

**==> picture [318 x 34] intentionally omitted <==**

implying short-end switching faster than long-end. 

CIR parameters under Q are set (illustratively) as: 

**==> picture [376 x 51] intentionally omitted <==**

The short-rate mapping is 

**==> picture [198 x 15] intentionally omitted <==**

Copula dependence uses correlation 

**==> picture [124 x 46] intentionally omitted <==**

14 

and Student- _t_ copula degrees of freedom _ν_ _**i** ∈{_ 6 _,_ 20 _}_ as described above. Simulation is performed on a monthly grid ∆= 1 _/_ 12, refined as needed for accuracy. 

## **14.8 OM/THMM inference on factor paths (time-series step)** 

We now explain how OM-based emissions enter the learning of asynchronous regimes and parameters from historical factor paths _{Xtk }[N] k_ =0[(e.g.][extracted][key][rates).][Given][a][regime][configuration] _**i**_ at step _k_ , define the Euler residual 

**==> picture [316 x 27] intentionally omitted <==**

where _µ_ _**i**_ is the regime-configuration drift implied by (5). Let Γ _**i**_ ( _x_ ) denote the (instantaneous) covariance used in the OM metric. The Gaussian OM emission cost is 

**==> picture [362 x 23] intentionally omitted <==**

and the robust Student- _t_ OM emission is 

**==> picture [399 x 28] intentionally omitted <==**

THMM inference uses exp _{−I_ _**i**_ ( _·_ ) _}_ in place of classical pointwise emission densities. 

**Scalable asynchronous decoding via coordinate-wise OM.** To avoid the exponential state space _|K|_ =[�] _j[K][j]_[,][one][may][adopt][coordinate-wise][emissions] 

**==> picture [90 x 35] intentionally omitted <==**

together with factorized transitions[�] _j[A]_[(] _[j]_[)][, yielding] _[ d]_[ independent Viterbi problems and per-asset] EM updates. 

## **14.9 Derivative-consistent calibration: joint objective for multiple swaptions** 

Let Θ collect all model parameters: CIR parameters per regime, regime generators _Q_[(] _[j]_[)] , copula parameters (e.g. _ρ_ _**i**_ , _ν_ _**i**_ ), and mapping weights _α_ . We propose a joint calibration objective combining (i) a THMM/OM-based time-series fit and (ii) a swaption panel fit. 

15 

## **14.9.1 Swaption panel errors** 

For each swaption _m_ = 1 _, . . . , M_ , compute model-implied volatility _σm_[model] (Θ) via Monte Carlo pricing (14) and Black inversion. Define a weighted squared error 

**==> picture [364 x 33] intentionally omitted <==**

## **14.9.2 Joint objective** 

Let _L_ THMM(Θ) denote the THMM log-likelihood surrogate induced by OM emissions, computed via forward-backward (or a structured approximation) using emissions[˜] _b_ _**i**_ ( _k_ ) _∝_ exp _{−I_ _**i**_ ( _k_ ) _}_ . We consider the penalized objective 

**==> picture [338 x 17] intentionally omitted <==**

Parameter learning can be performed by alternating updates: (i) THMM/OM-driven EM for regime and marginal CIR parameters on historical factor paths, and (ii) derivative calibration updates (copula parameters, mapping weights, and selected vol parameters) to reduce (19). This mirrors the philosophy of incorporating forward-looking derivative information into regime inference while retaining pathwise robustness. 

## **14.10 Algorithmic summary** 

**Step A (Initialization).** Initialize _Xt_ 0 from the current curve; initialize ( _κ, θ, σ_ ) by matching historical level/variance of each factor; initialize _Q_[(] _[j]_[)] to plausible persistence; initialize copula parameters. 

**Step B (Time-series THMM step).** Given historical factor paths _{Xtk }_ : 

- E-step: compute posterior regime probabilities using OM emissions (17) or (18). 

- M-step: update regime-dependent CIR parameters and regime generators _Q_[(] _[j]_[)] (via weighted quasi-likelihood / exact transition likelihood if used). 

**Step C (Swaption calibration step).** For the swaption panel: 

- simulate under Q using the regime-switching CIR + copula procedure in Section 14.6, 

- compute _V_[�] _m_ ( _t_ 0) and implied vols _σm_[model] , 

- update copula parameters ( _ρ, ν_ ) and mapping weights _α_ (and optionally selected volatility parameters) to reduce (19). 

16 

**Step D (Iterate).** Alternate Steps B–C until regime segmentation stabilizes and swaption errors converge. 

## **14.11 Outputs and diagnostics (suggested figures/tables)** 

A standard empirical presentation includes: 

- A table of regime-specific CIR parameters ( _κi,j, θi,j, σi,j_ ) and regime transition matrices. 

- Plots of factor paths _Xt_[(] _[j]_[)] with decoded asynchronous regimes _St_[(] _[j]_[)] overlaid. 

- A heatmap/scatter of swaption implied vol errors _σm_[model] _− σm_[mkt] across ( _Te, Ts_ ). 

- Stress diagnostics showing tail co-movement under the Student- _t_ copula (e.g. joint drawdowns / joint spikes). 

The above provides a complete worked template for multi-swaption pricing and calibration under asynchronous regime-switching CIR dynamics, with OM/THMM providing robust regime inference and copulas capturing tail dependence. 

## **15 Conclusion** 

We presented a detailed mathematical framework for asynchronous regime-switching multivariate CIR spot-rate models with copula dependence and OM-functional THMM inference, extending OM/THMM methodology to positive-state interest-rate dynamics with tail dependence and scalable per-asset regime decoding. 

## **References** 

- G. W. Peters, M. Xu, Z. Zhu, and P. V. Shevchenko (2025). Regime-switching polynomial diffusions via topological hidden Markov model inference using Onsager–Machlup functionals for asset pricing. (Working paper; attached in this project.) 

17 

