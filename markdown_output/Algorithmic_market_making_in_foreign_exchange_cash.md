# market in cash markets: a Algorithmic making foreign exchange new model for active market makers 

Alexander Barzykin[∗] Philippe Bergault[†] Olivier Guéant[‡] 

## **Abstract** 

In OTC markets, one of the main tasks of dealers / market makers consists in providing prices at which they agree to buy and sell the assets and securities they have in their scope. With ever increasing trading volume, this quoting task has to be done algorithmically. Over the last ten years, many market making models have been designed that can be the basis of quoting algorithms in OTC markets. However, in the academic literature, most market making models adapted to OTC markets are general and only a few focus on specific market characteristics. In particular, to the best of our knowledge, in all OTC market making models, the market maker only sets quotes and/or waits for clients. However, on many markets such as foreign exchange cash markets, market makers have access to liquidity pools where they can unwind part of their inventory. In this paper, we propose a model taking this possibility into account, therefore allowing market makers to trade “actively” in the market. The model displays an important feature well known to practitioners that in a certain inventory range the market maker does not actually want to capitalize on this active trading opportunity but should rather “internalize” the flow by appropriately adjusting the quotes. The larger the market making franchise, the wider is the inventory range suitable for internalization. The model is illustrated numerically with realistic parameters for USDCNH spot market. 

**Key words:** Market making, Algorithmic trading, Stochastic optimal control, Viscosity solutions 

## **1 Introduction** 

In all financial markets, liquidity has traditionally been provided by a specific category of agents who, on a continuous and regular basis, set prices at which they agree to buy or sell assets and securities. These agents, called market makers or dealers, play a key role in the price formation process in all markets but their exact role and behavior depend on the considered asset class. 

In most order-driven markets, such as most stock markets, almost all traditional exchanges have converted from open outcry communications between human traders to electronic platforms organized around all-toall limit order books, and computers now handle almost all market activity. Official market makers and traditional market making companies still make money by providing liquidity to the market but they are now, somehow, in competition with all market participants who can post liquidity-providing orders. In quote-driven markets, electronification has also been one of the major upheavals of the last decade, with important consequences on market makers / dealers. In foreign exchange (FX) cash markets for instance, dealers set up their own private electronic platforms enabling clients to directly send them requests for quotes (RFQ) and to be connected to their stream (RFS). Many dealer-to-dealer and all-to-all plaforms have also emerged, therefore blurring the frontier between OTC and organized markets. 

Alongside the multifaceted electronification of trading means, most human market makers have been replaced by market making algorithms. This evolution has naturally gone along with the development of 

> ∗HSBC, 8 Canada Square, Canary Wharf, London E14 5HQ, United Kingdom, alexander.barzykin@hsbc.com 

> †Université Paris 1 Panthéon-Sorbonne, Centre d’Economie de la Sorbonne, 106 Boulevard de l’Hôpital, 75642 Paris Cedex 13, France, philippe.bergault@etu.univ-paris1.fr 

> ‡Université Paris 1 Panthéon-Sorbonne, Centre d’Economie de la Sorbonne, 106 Boulevard de l’Hôpital, 75642 Paris Cedex 13, France, olivier.gueant@univ-paris1.fr 

1 

many market making models in the academic literature. 

In 2008, largely inspired by a paper from the 1980s by Ho and Stoll [26], Avellaneda and Stoikov [6] proposed a stochastic optimal control model to determine the optimal bid and ask quotes that a single-asset risk-averse market maker should set. The authors paved the way to a new literature on market making that goes far beyond the toy models of the economic literature on the topic.[1] The resulting new models can be divided into two groups: those adapted to the problem of a market maker in a limit order book and those adapted to OTC markets. 

To build a relevant market making model for order-driven markets, and especially stock markets, it is important to take microstructure into account. For instance, Guilbaud and Pham [24] modeled the market bid-ask spread with a discrete Markov chain and studied the performance of a market maker submitting limit buy/sell order at the best bid/ask quotes and/or at the best bid plus one tick and best ask minus one tick. Guilbaud and Pham [25] studied a similar problem of optimal market making in a pro-rata limit order book, where the dealer may post limit orders but also market orders represented by impulse controls. Fodra and Pham [16, 17] considered a model in which market orders arrive in the limit order book according to a point process correlated with the stock price itself. They modeled the market maker as an agent placing limit orders of constant size at the best bid and at the best ask, and solve the problem faced by a risk-averse market maker. More recently, in Abergel et al. [2], the authors proposed a different model for the limit order book (first introduced in Abergel et al. [1]), in which the limit orders, market orders, and cancel orders arrive according to Markov jump processes with intensities depending only on the state of the limit order book. They considered the case of a market maker trading in this limit order book, and proposed a quantization-based algorithm to numerically solve the resulting high-dimensional problem. Finally, Capponi et al. [10] studied a discrete-time problem, assuming that the market maker can place bid and ask limit orders simultaneously on both sides at prespecified dates. In their framework, the number of filled orders during each period depends linearly on the distance between the fundamental price and the price of the market maker’s limit order, with random slope and intercept coefficients. Using standard tools of discrete-time optimal control, the authors managed to get an explicit characterization of the optimal strategy. 

In the case of OTC markets, or for order-driven markets in which the spread-to-tick ratio is large, most market making models derive from the seminal work of Avellaneda and Stoikov [6].[2] For instance, Guéant et al. [23] provided a rigorous analysis of the stochastic optimal control problem introduced in Avellaneda and Stoikov [6] and showed that, by adding risk limits to the inventory of the market maker, the problem boils down to a finite system of ordinary differential equations (ODEs) – in particular, those ODEs are linear in the case of the exponential intensity functions proposed in [6]. Cartea, Jaimungal, and Ricci considered in [13] a different kind of objective function: instead of the Von Neumann-Morgenstern expected utility of [6], they optimized a risk-adjusted expectation of the PnL. Cartea and Jaimungal, along with diverse coauthors, then proposed several extensions. For instance, Cartea, Donnelly, and Jaimungal studied in [11] the impact of uncertainty on the parameters of the model. Multi-asset market making models have been proposed by Guéant in [21, 22] for both kinds of objective function, and the author showed again that the problem boils down to a system of ODEs. In all these models the trade size is assumed constant: the same number of assets is bought/sold at each trade. In [9], Bergault and Guéant introduced a distribution of trade sizes in the model along with the possibility for the maket maker to answer different quotes for different sizes. They characterized the value function of the problem with an integro-differential equation of the Hamilton-Jacobi (HJ) type that can be seen as an ODE in an infinite-dimensional space. They also proposed a dimensionality reduction technique in order to approximate numerically the optimal bid and ask quotes of the market maker in high dimension, by projecting the market risk on a low-dimensional space 

> 1Economists had studied for a long time the behaviour of market makers / dealers with the aim of understanding market liquidity and the magnitude of bid-ask spreads. Models where one or several risk-averse market makers optimize their pricing policy for managing their inventory risk models include Amihud and Mendelson [5], Ho and Stoll [26, 27], and O’Hara and Oldfield [28]). Models focused on information asymmetries where bid-ask spreads derive from adverse selection include Copeland and Galai [15] and Glosten and Milgrom [18]). Other classic economic references on market making include Grossman and Miller [19] and the review paper of Stoll [29]. 

> 2See the books of Cartea et al. [12] and Guéant [21] for a detailed discussion. 

2 

of factors. This problem of approximating the solution across a large universe of assets has been addressed using different approaches. In Bergault et al. [8], the authors regarded the Hamilton-Jacobi equation of the problem as a perturbation of another simpler equation whose solution can be computed in closed form. In Guéant and Manziuk [20], the authors used neural networks instead of grids to compute an approximate solution – a method inspired by approximate dynamic programming and reinforcement learning techniques. 

In most models adapted to OTC markets, market makers are liquidity providers: they buy assets at the bid price they quote and sell them at the ask price they quote – ideally earning the difference between these two prices. Of course, market makers seldom buy and sell simultaneously: they carry inventory and bear price risk. The problem faced by market makers in these models is already a subtle dynamic optimization problem in which market makers must mitigate the risk associated with price changes by skewing their quotes as a function of their inventory. However, this problem is complexified on some markets like FX cash markets, as market makers have an additional way to manage their inventory risk: in those markets, market makers typically have access to liquidity pools on the Dealer-to-Dealer (D2D) segment of the market and to a variety of all-to-all platforms where they can unwind part of their position, without having to “wait” for clients sending requests and trading with them. 

The co-existence of requests for quotes / requests for stream and liquidity pools has seldom been studied in the academic literature on market making in OTC markets (the only instance we found beyond our paper is the very recent paper [7] that proposes a reinforcement learning approach). The main goal of our paper is in effect to include the possibility for the market maker to buy and sell “actively” (in continuous time) in a liquidity pool, in order to better mitigate their inventory risk. By trading in a liquidity pool, the market maker adds certainty to inventory risk management but it comes with execution costs and market impact, in part due to revealing of trading intentions to a wider audience. Our setup is inspired by Almgren-Chriss-like models of optimal execution (see Almgren et al. [3, 4], and Guéant [21] for a general presentation). More precisely, we introduce a new form of control (in addition to the bid and ask quotes) that represents the trading rate of the market maker in the liquidity pool and add (i) execution costs to proxy the bid-ask spread, transaction costs, and nonlinear liquidity costs, and (ii) permanent market impact (assumed to be linear in the trading rate). 

In Section 2, we present our market making model involving an asset for which the market maker has a classical market making quoting activity together with the possibility to trade “actively” by buying or selling in a liquidity pool. We then introduce the stochastic optimal control problem of the market maker. In Section 3, we characterize the associated value function as the unique continuous viscosity solution of a Partial Integro-Differential Equation (PIDE) of the HJ type. We illustrate our model numerically in Section 4 and discuss the results. In particular, we highlight the existence of a threshold of inventory under which it is not optimal for the market maker to trade in the liquidity pool. 

## **2 A model for active market makers** 

We consider a market maker in charge of a single asset. This asset can be traded by the market maker in two ways: (i) via requests she receives from clients and (ii) via market orders sent to a liquidity pool (for instance an all-to-all trading platform, but we can also regard the liquidity pool of our model as an aggregation of numerous liquidity pools). In the former case, the market maker may receive a RFQ from a client wishing to buy or sell the asset, and then proposes a price to the client who finally decides whether she accepts to trade at that price or not – another possibility is that a client connected to the stream of quotes proposed by the market maker decides to trade (this is the RFS channel).[3] In the latter case, the market maker buys or sells at a market price that depends on the traded volume.[4] 

> 3The mathematical modelling of RFQs and RFSs is the same. 

> 4The model can easily be generalized to multiple assets (see [22] for the way to go multi-asset in market making models _à la_ Avellaneda-Stoikov). In that case, each asset may be traded through requests only, market orders only, or both ways. 

3 

In what follows (Section 2.1) we present a first optimization problem with hard constraints on the trading strategy in the liquidity pool. In order to carry out a rigorous mathematical analysis, we shall slightly modify (regularize) the problem in Section 2.2. 

## **2.1 Modeling framework and notations** 

We consider a filtered probability space (Ω _, F,_ P; F = ( _Ft_ ) _t≥_ 0) satisfying the usual conditions. We assume this probability space is large enough to support all the processes we introduce. 

Let us start with the modelling of the asset price. We model the reference price (for instance the mid-price of the liquidity pool) of the asset by a process ( _St_ ) _t≥_ 0. We consider that the market maker can trade continuously in the liquidity pool and we denote by ( _wt_ ) _t≥_ 0 the trading rate of the market maker (she buys when _wt ≥_ 0 and sells otherwise).[5] Taking into account the permanent market impact of trades within the liquidity pool, the price process ( _St_ ) _t≥_ 0 is modeled as follows: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0004-04.png)


with _S_ 0 _∈_ R given, _k, σ >_ 0 _,_ and the process ( _Wt_ ) _t≥_ 0 is a standard Brownian motion adapted to the filtration F. 

Regarding requests, the market maker proposes bid and ask quotes depending on the size _z ∈_ R _[∗]_ +[of][each] request. These quotes are modeled by maps _S[b] , S[a]_ : Ω _×_ [0 _, T_ ] _×_ R _[∗]_ + _[→]_[R][+][which are] _[ P ⊗B]_[(][R] _[∗]_ +[)][-measurable,] where _P_ denotes the _σ_ -algebra of F-predictable subsets of Ω _×_ [0 _, T_ ] and _B_ (R _[∗]_ +[)][denotes][the][Borelian][sets] of R _[∗]_ +[.] 

We introduce _J[b]_ ( _dt, dz_ ) and _J[a]_ ( _dt, dz_ ) two _càdlàg_ R+-marked point processes corresponding to the number of _J_ ˜ _[b]_ (transactions _dt, dz_ ) and _J_ ˜resulting _[a]_ ( _dt, dz_ ) fromthe associatedrequests atcompensatedthe bid andprocesses.at the ask, respectively. We denote respectively by 

The inventory of the market maker, modeled by the process ( _qt_ ) _t≥_ 0, has the following dynamics: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0004-09.png)


with _q_ 0 given. We assume that the processes _J[b]_ ( _dt, dz_ ) and _J[a]_ ( _dt, dz_ ) do not have simultaneous jumps almost surely. Moreover, we denote by � _νt[b]_[(] _[dz]_[)] � _t≥_ 0[and][(] _[ν] t[a]_[(] _[dz]_[))] _t≥_ 0[the][intensity][kernels][of] _[J][b]_[(] _[dt, dz]_[)][and] _J[a]_ ( _dt, dz_ ), respectively. 

˜ ˜ We assume that the market maker wants her inventory to remain in an interval _Q_ = [ _−q,_ ˜ _q_ ], with _q >_ 0. The intensities � _νt[b]_[(] _[dz]_[)] � _t≥_ 0[and][(] _[ν] t[a]_[(] _[dz]_[))] _t≥_ 0[verify:] 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0004-12.png)


where _µ[b]_ and _µ[a]_ are probability measures on R _[∗]_ +[,][absolutely][continuous][with][respect][to][the][Lebesgue] measure such that �R _[∗]_ + _[zµ][b]_[(] _[dz]_[) =: ∆] _[b][<]_[ +] _[∞]_[,] �R _[∗]_ + _[zµ][a]_[(] _[dz]_[) =: ∆] _[a][<]_[ +] _[∞]_[,] 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0004-14.png)


and Λ _[b]_ , Λ _[a]_ are two functions satisfying the following hypotheses ( _H_ Λ): 

- Λ _[b]_ and Λ _[a]_ are twice continuously differentiable, 

- Λ _[b]_ and Λ _[a]_ are decreasing, with _∀δ ∈_ R, Λ _[b][′]_ ( _δ_ ) _<_ 0 and Λ _[a][′]_ ( _δ_ ) _<_ 0, 

> 5This is similar to what was done in Almgren [4]. 

4 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-00.png)


**Remark 1.** Λ _[.] typically has the form_ Λ _[.]_ ( _δ_ ) = _λ[.] R[f][ .]_[(] _[δ]_[)] _[,][where][λ][.] R[can][be][seen][as][the][(constant)][intensity][of] arrival of requests. µ[.] can be seen as the distribution of the size of requests, and f[.] is the probability that a request will result in a transaction knowing the quote that the market maker proposes._ 

In the first version of the model the process ( _Xt_ ) _t≥_ 0 modeling the market maker’s cash account has the dynamics: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-03.png)


with 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-05.png)


where the penalty function _L_ : R _→_ R+ (that results from the temporary price impact of the market maker when she chooses to be active in the liquidity pool) satisfies the following hypotheses ( _HL_ ): 

- _L_ (0) = 0, 

- _L_ is strictly convex, increasing on R+ and decreasing on R _−_ , 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-09.png)


and the function _χ_ : R[2] _→{_ 0 _,_ + _∞}_ verifies 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-11.png)


The latter penalty function prevents the market maker from selling actively when her inventory is already short, and to buy actively when her inventory is already long.[6] 

We define the following set _AM_ of admissible controls for the quotes: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-14.png)


where _δ∞ >_ 0 is a prespecified constant. 

We define the set _AT_ of admissible continuous trading strategies: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0005-17.png)


> 6This is the hard constraint that we shall relax in an astute manner in Section 2.2 to be able to use viscosity solutions. 

5 

for a given _v∞ >_ 0. 

For two given continuous penalty functions _ψ_ : R _→_ R+ and _ℓ_ : R _→_ R+, modeling the risk aversion of the market maker and the cost of liquidity, we aim at maximizing: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-02.png)


over the set _AM × AT_ of admissible controls ( _δ, w_ ). 

**Remark 2.** _For instance, for a constant γ >_ 0 _, we can choose ψ_ ( _q_ ) = _[γ]_ 2 _[σ]_[2] _[q]_[2] _[or][ψ]_[(] _[q]_[) =] _[ γσ][|][q][|][and][ℓ]_[(] _[q]_[) = 0] _[,] ℓ_ ( _q_ ) = 2 _[l][σ]_[2] _[q]_[2] _[or][ℓ]_[(] _[q]_[) =] _[ lσ][|][q][|][(for][l >]_[ 0] _[),][as][done][in][[12],][[13],][[22],][and][[20].]_ 

## **2.2 A slightly modified version** 

Carrying out a mathematical analysis of the above optimal control problem is complicated because the associated Hamiltonian function is discontinuous (because of the hard trading constraint introduced through the penalty function _χ_ ). In order to carry out a rigorous mathematical analysis we do not consider the above problem but a slight modification of it. We fix _ϵ_ ˜ _∈_ (0 _,_ ˜ _q_ ) and introduce a function _ζ_ : R _→_ [0 _,_ 1] which is a Lipschitz approximation of the indicator function of R+, with 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-07.png)


Then, instead of considering the trading rate process as a control variable, we use a new control process ( _vt_ ) _t≥_ 0 _∈AT_ and choose a trading rate of the form 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-09.png)


We also introduce a new cost function[7] _L_[˜] : R[2] _→_ R given by 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-11.png)


˜ **Remark 3.** _The model is exactly the same as the initial one whenever |q| ≥ ϵ. However, for small values of the inventory (|q| < ϵ), the market maker is allowed to trade in both directions in the liquidity pool but the cost to buy (resp. sell) increases when the inventory becomes negative (resp. positive)._ 

The price process ( _St_ ) _t≥_ 0 has now the following dynamics: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-14.png)


and the inventory ( _qt_ ) _t≥_ 0 has dynamics: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-16.png)


> 7This new function corresponds to the approximation of the initial cost function _L_ by the function _L_ ˜0 : R2 _→_ R _∪{_ + _∞}_ defined by 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-18.png)


where _w_ + and _w−_ denote respectively the positive and negative part of _w_ , and with the conventions 

and similarly 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0006-21.png)


These conventions are natural as _L_ is assumed to be asymptotically superlinear. 

6 

Finally, the process ( _Xt_ ) _t≥_ 0 modeling the market maker’s cash account now has the dynamics: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0007-01.png)


The resulting optimization problem is that of maximizing 

over the set _A_ := _AM × AT_ of admissible controls ( _δ, v_ ). 

After applying Itô’s formula to ( _Xt_ + _qtSt_ ) _t≥_ 0 between 0 and _T −_ , it is easy to see that the problem is equivalent to maximizing: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0007-05.png)


over the set of admissible controls _A_ . 

_∀_ We _q ∈Q_ therefore, _∀_ � _δ,_ ¯ ¯introduce _v_ ¯� _∈A_ , ifthewefunctiondenote by _J_ �: [0 _qs[t,q,] , T[δ,]_[¯] ] _[v]_[¯] _× Q × A_ � _s≥t_[the] _M_[inventory] _× AT −→_[process] R such[starting] that, _∀_[in] _t ∈_[state] [0 _, T_ ] _[q]_ ,[at][time] _[t]_[and] controlled by � _δ,_ ¯ _v_ �: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0007-08.png)


The value function _θ_ : [0 _, T_ ] _× Q →_ R of the problem is then defined as follows: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0007-10.png)


We will show that _θ_ is the unique continuous viscosity solution on [0 _, T_ ] _×Q_ to the following Hamilton-Jacobi partial integro-differential equation: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0007-12.png)


7 

where 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0008-01.png)


and 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0008-03.png)


## **3 Mathematical analysis** 

## **3.1 Preliminary results** 

We first recall a result (Lemma 1) which is proved in [9]. 

**Lemma 1.** _H[b] and H[a] are two continuously differentiable decreasing functions and the supremum in the definition of H[b]_ ( _p_ ) _(respectively H[a]_ ( _p_ ) _) is reached at a unique δ[b][∗]_ ( _p_ ) _(respectively δ[a][∗]_ ( _p_ ) _). Furthermore, δ[b][∗] and δ[a][∗] are continuous and nondecreasing in p._ 

We then state another useful lemma: 

**Lemma 2.** _Let ϕ_ : [0 _, T_ ] _× Q �→_ R _be a bounded function. The functions_ 

_and_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0008-11.png)


_are nonnegative and bounded._ 

_Proof._ We only prove it for the ask side (the proof for the bid side is similar). 

Let _t ∈_ [0 _, T_ ] _, q ∈Q_ and _z ∈_ R _[∗]_ +[such][that] _[q][ −][z][∈Q]_[.] 

We have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0008-16.png)


where diam( _Q_ ) denotes the diameter of _Q_ . 

For the other bound, we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0008-19.png)


We simply take _δ_ = _[ϕ]_[(] _[t][,q]_[)] _[−] z[ϕ]_[(] _[t][,q][−][z]_[)] to see that 

hence the result. 

8 

We can now state a first simple result about the value function _θ_ : **Proposition 1.** _The value function θ is bounded on_ [0 _, T_ ] _× Q. Proof. ∀_ � _t, q, δ,_[¯] ¯ _v_ � _∈_ [0 _, T_ ] _× Q × AM × AT ,_ we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0009-01.png)


As _ℓ, ψ_ , and _L_[˜] are nonegative, we get 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0009-03.png)


The right-hand term is independent from _t, q, δ_[¯] and _v,_ ¯ so it is clear that _J_ and _θ_ are bounded from above. 

By considering the control process corresponding to _δ[b]_ ( _t, z_ ) = _δ[a]_ ( _t, z_ ) = _vt_ = 0, we obtain 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0009-06.png)


As _ψ_ and _ℓ_ are continuous and _Q_ is compact, we get that _θ_ is bounded from below. 

Turning to the Hamiltonian function associated with the possibility to trade in a liquidity pool, classical results of convex analysis imply the following lemma: 

**Lemma 3.** _For all q ∈Q, H_ ( _., q_ ) _is continuously differentiable and Lipschitz, and the supremum in the definition of H_ ( _p, q_ ) _is uniquely reached at a v[∗]_ ( _p, q_ ) = _∂pH_ ( _p, q_ ) _._ 

Finally, we will need the following lemma: 

**Lemma 4.** _There exists a constant CH >_ 0 _such that, for all p ∈_ R _and for all q, y ∈Q,_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0009-12.png)


_Proof._ For all _p ∈_ R and _q ∈Q_ , we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0009-14.png)


9 

where for all _r ∈_ R, 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-01.png)


Let us notice that _H_[¯] is Lipschitz and let us denote by ~~_L_~~ _H_[its][Lipschitz][constant.] 

Let us denote by _h_ 1 : R _× Q →_ R and _h_ 2 : R _× Q →_ R the two functions given by 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-04.png)


and 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-06.png)


for all _p ∈_ R and _q ∈Q_ . We then have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-08.png)


Let us take _p ∈_ R and _q, y ∈Q_ . We have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-10.png)


As _ζ_ and _H_[¯] are Lipschitz, and _H_[¯] (0) = 0, we get 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-12.png)


for _C_[¯] = ~~_L_~~ _H_ ~~[(]~~ _[k]_[ +] _[ L][ζ]_[+] _[ kL][ζ]_[ ˜] _[q]_[)][.] 

The same result holds for _h_ 2, and we conclude by taking _CH_ = 2 _C_[¯] . 

## **3.2 Existence result** 

We denote by _C_[1] := _C_[1] ([0 _, T_ ) _×_ R) the class of functions _ϕ_ : [0 _, T_ ) _×_ R _→_ R that are continuously differentiable on [0 _, T_ ) _×_ R _._ 

**Definition 1.** _(i) If u is an upper semicontinuous (USC) function on_ [0 _, T_ ] _× Q, we say that u is a viscosity subsolution to_ (HJ) _on_ [0 _, T_ ) _× Q if ∀_ ( _t,_[¯] ¯ _q_ ) _∈_ [0 _, T_ ) _× Q, ∀ϕ ∈ C_[1] _such that_ ( _u − ϕ_ )( _t,_[¯] ¯ _q_ ) = max _[we][have:]_ ( _t,q_ ) _∈_ [0 _,T_ ) _×Q_[(] _[u][ −][ϕ]_[)(] _[t, q]_[)] _[,]_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-18.png)


_(ii) If v is a lower semicontinuous (LSC) function on_ [0 _, T_ ] _× Q, we say that v is a viscosity supersolution to_ (HJ) _on_ [0 _, T_ ) _× Q if ∀_ ( _t,_[¯] ¯ _q_ ) _∈_ [0 _, T_ ) _× Q, ∀ϕ ∈ C_[1] _such that_ ( _v − ϕ_ )( _t,_[¯] ¯ _q_ ) = min _[we]_ ( _t,q_ ) _∈_ [0 _,T_ ) _×Q_[(] _[v][ −][ϕ]_[)(] _[t, q]_[)] _[,]_ 

_have:_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0010-21.png)


10 

_(iii) If θ is locally bounded on_ [0 _, T_ ) _× Q, we say that θ is a viscosity solution to_ (HJ) _on_ [0 _, T_ ) _× Q if its upper semicontinuous envelope θ[∗] and its lower semicontinuous envelope θ∗ are respectively subsolution on_ [0 _, T_ ) _× Q and supersolution on_ [0 _, T_ ) _× Q to_ (HJ) _._ 

The following result is proved in the appendix: 

**Proposition 2.** _(i) Let u be a USC function on_ [0 _, T_ ] _×Q. u is a viscosity subsolution to_ (HJ) _on_ [0 _, T_ ) _×Q if and only if ∀_ ( _t,_[¯] ¯ _q_ ) _∈_ [0 _, T_ ) _× Q, ∀ϕ ∈C_[1] _such that_ max _[we][have]_ ( _t,q_ ) _∈_ [0 _,T_ ) _×Q_[(] _[u][ −][ϕ]_[)(] _[t, q]_[) = (] _[u][ −][ϕ]_[)(¯] _[t,]_[ ¯] _[q]_[)] _[,]_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0011-03.png)


_(ii) Let v be a LSC function on_ [0 _, T_ ] _× Q. v is a viscosity supersolution to_ (HJ) _on_ [0 _, T_ ) _× Q if and only if ∀_ ( _t,_[¯] ¯ _q_ ) _∈_ [0 _, T_ ) _× Q, ∀ϕ ∈C_[1] _such that_ min _[we][have:]_ ( _t,q_ ) _∈_ [0 _,T_ ) _×Q_[(] _[v][ −][ϕ]_[)(] _[t, q]_[) = (] _[v][ −][ϕ]_[)(¯] _[t,]_[ ¯] _[q]_[)] _[,]_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0011-05.png)


We can now prove that _θ_ is a viscosity solution to (HJ). 

**Proposition 3.** _θ is a viscosity subsolution to_ (HJ) _on_ [0 _, T_ ) _× Q._ 

_Proof. θ_ is bounded on [0 _, T_ ] _× Q_ so we can define _θ[∗]_ its upper semicontinuous envelope. 

Let ( _t,_[¯] ¯ _q_ ) _∈_ [0 _, T_ ) _× Q_ and _ϕ ∈ C_[1] such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0011-10.png)


We can classically assume this maximum to be strict. By definition of _θ[∗]_ ( _t,_[¯] ¯ _q_ ), their exists ( _tm, qm_ ) _m_ a sequence of [0 _, T_ ) _× Q_ such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0011-12.png)


We prove the result by contradiction. Assume there exists _η >_ 0 such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0011-14.png)


11 

Then, as _ϕ_ is continuously differentiable and _µ[b]_ and _µ[a]_ absolutely continuous with respect to the Lebesgue measure, we must have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0012-01.png)


on _B_ := �( _t_[¯] _− r, t_[¯] + _r_ ) _∩_ [0 _, T_ )� _×_ ((¯ _q − r,_ ¯ _q_ + _r_ ) _∩Q_ ) for a sufficiently small _r ∈_ �0 _, T − t_[¯] �. Without loss of generality, we can assume that _B_ contains the sequence ( _tm, qm_ ) _m_ . 

Then, by potentially reducing the value of _η_ , we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0012-04.png)


on the parabolic boundary _∂pB_ of _B_ , i.e. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0012-06.png)


Without loss of generality we can assume that the above inequality holds on 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0012-08.png)


which is also bounded. 

We introduce an arbitrary control _δ_ = ( _δ[b] , δ[a]_ ) _∈AM_ . We also introduce an arbitrary control _v ∈AT_ . We denote by _πm_ the first exit time of ( _t, qt[m]_[)] _[t][≥][t] m_[from] _[B]_[(where] _[q] t[m]_[:=] _[ q] t[t][m][,q][m][,δ,v]_ ): 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0012-11.png)


By Itô’s formula, 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0012-13.png)


12 

which we can write 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0013-01.png)


From (9), and by definition of _H[b]_ , _H[a]_ , and _H_ , we then get 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0013-03.png)


The last two terms have expectations equal to zero and we obtain 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0013-05.png)


13 

Therefore 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0014-01.png)


As _ϕ_ ( _tm, qm_ ) _−−−−−→ ϕ_ ( _t,_[¯] ¯ _q_ ) = _θ[∗]_ ( _t,_[¯] ¯ _q_ ) and _θ_ ( _tm, qm_ ) _−−−−−→ θ[∗]_ ( _t,_[¯] ¯ _q_ ), we have for _m_ large enough the _m→_ + _∞ m→_ + _∞_ inequality _θ_ ( _tm, qm_ ) + _[η]_ 2 _[≥][ϕ]_[(] _[t][m][, q][m]_[)][,][from][which][we][deduce] 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0014-03.png)


By taking the sup over all the controls in _A_ on the right-hand side, we contradict the dynamic programming principle. 

Necessarily, we deduce: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0014-06.png)


and _θ_ is a viscosity subsolution to (HJ) on [0 _, T_ ) _× Q_ . 

**Proposition 4.** _θ is a viscosity supersolution to_ (HJ) _on_ [0 _, T_ ) _× Q._ 

_Proof. θ_ is bounded on [0 _, T_ ] _× Q_ , so we can define _θ∗_ its lower semicontinuous envelope. 

Let ( _t,_[¯] ¯ _q_ ) _∈_ [0 _, T_ ) _× Q_ and _ϕ ∈ C_[1] such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0014-11.png)


We can assume this minimum to be strict. By definition of _θ∗_ ( _t,_[¯] ¯ _q_ ), there exists ( _tm, qm_ ) _m_ a sequence of [0 _, T_ ) _× Q_ such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0014-13.png)


Let us prove the proposition by contradiction. Assume there is _η >_ 0 such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0014-15.png)


14 

Then, as _ϕ_ is continuously differentiable and _µ[b]_ and _µ[a]_ absolutely continuous with respect to the Lebesgue measure, we must have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0015-01.png)


on _B_ := �( _t_[¯] _− r, t_[¯] + _r_ ) _∩_ [0 _, T_ )� _×_ ((¯ _q − r,_ ¯ _q_ + _r_ ) _∩Q_ ) for a sufficiently small _r ∈_ �0 _, T − t_[¯] �. Without loss of generality, we can assume that _B_ contains the sequence ( _tm, qm_ ) _m_ . 

Then, by potentially reducing _η_ , we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0015-04.png)


on _∂pB_ . We can also without loss of generality assume that this inequality is true on 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0015-06.png)


which is also bounded. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0015-08.png)


where _δ[b][∗]_ and _δ[a][∗]_ are defined in Lemma 1. Similarly, we introduce the control _v ∈AT_ such that _∀t ≥ tm,_ 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0015-10.png)


where _v[∗]_ is defined in Lemma 3. As before, we denote by _πm_ the first exit time of ( _t, qt[m]_[)] _[t][≥][t] m_[from] _[ B]_[(where] _qt[m]_[:=] _[ q] t[t][m][,q][m][,δ,v]_ ). By Itô’s lemma, we obtain 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0015-12.png)


15 

which we can write 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0016-01.png)


By (10), we then get 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0016-03.png)


The last two terms have expectations equal to zero and we obtain 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0016-05.png)


16 

Therefore, 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0017-01.png)


As _ϕ_ ( _tm, qm_ ) _−−−−−→ ϕ_ ( _t,_[¯] ¯ _q_ ) = _θ∗_ ( _t,_[¯] ¯ _q_ ) and moreover _θ_ ( _tm, qm_ ) _−−−−−→ θ∗_ ( _t,_[¯] ¯ _q_ ), we have that for _m m→_ + _∞ m→_ + _∞_ sufficiently large, _θ_ ( _tm, qm_ ) _−[η]_ 2 _[≤][ϕ]_[(] _[t][m][, q][m]_[)][and][we][deduce:] 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0017-03.png)


which contradicts the dynamic programming principle. 

In conclusion, we necessarily have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0017-06.png)


and _θ_ is a viscosity supersolution to (HJ) on [0 _, T_ ) _× Q_ . 

**Proposition 5.** _∀q ∈Q, we have θ∗_ ( _T, q_ ) = _θ[∗]_ ( _T, q_ ) = _−ℓ_ ( _q_ ) _._ 

_Proof._ Let _q ∈Q_ and let us take ( _tm, qm_ ) _m∈_ N a sequence of [0 _, T_ ] _× Q_ such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0017-10.png)


We introduce arbitrary controls _δ_ = ( _δ[b] , δ[a]_ ) _∈AM_ . We also introduce an arbitrary control _v ∈AT_ . Then we have for all _m ∈_ N _,_ by denoting _qt[m]_[=] _[ q] t[t][m][,q][m][,δ,v]_ for all _t ∈_ [ _tm, T_ ]: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0017-12.png)


17 

But, 

and 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0018-02.png)


By dominated convergence (because ( _qT[m]_[)] _[m]_[converges][in][probability][towards] _[q]_[and] _[ℓ]_[is][continuous][on][the] compact set _Q_ ), we have E [ _ℓ_ ( _qT[m]_[)]] _−→_[and][therefore] _[θ][∗]_[(] _[T, q]_[)] _[ ≥−][ℓ]_[(] _[q]_[)] _[.]_[But][as] _[θ][∗]_[(] _[T, q]_[)] _[ ≤][θ]_[(] _[T, q]_[) =] _m→_ + _∞[ℓ]_[(] _[q]_[)][,] _−ℓ_ ( _q_ ) _,_ we get _θ∗_ ( _T, q_ ) = _−ℓ_ ( _q_ ) _._ 

The proof for _θ[∗]_ is similar, by taking _ε_ -optimal controls and showing that _θ[∗]_ ( _T, q_ ) _− ε ≤−ℓ_ ( _q_ ) for all _ε >_ 0 _._ 

## **3.3 Uniqueness result** 

**Theorem 1.** _Let u be a bounded USC subsolution and v be a bounded LSC supersolution to_ (HJ) _on_ [0 _, T_ ) _× Q such that u ≤ v on {T } × Q. Then u ≤ v on_ [0 _, T_ ] _× Q._ 

_Proof._ We prove it by contradiction. Let us assume sup _u − v >_ 0. Then this supremum cannot be [0 _,T_ ] _×Q_ reached on _{T } × Q_ . _∀n ≥_ 0, for _ε >_ 0, we introduce: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0018-08.png)


We also introduce ( _tn,ε, sn,ε, qn,ε, yn,ε_ ) such that: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0018-10.png)


Then for all _n ≥_ 0 _, ϵ >_ 0 and for all ( _t, q_ ) _∈_ [0 _, T_ ] _× Q_ , we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0018-12.png)


In particular, 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0018-14.png)


We can now _ε_ such that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0018-16.png)


From what precedes, we know that the sequence � _n_ ( _qn − yn_ )[2] + _n_ ( _tn − sn_ )[2][�] _n_[is][bounded,][so][necessarily,] _|tn − sn| −→_[and] _[|][q][n][ −][y][n][|] −→_[Then,][up][to][a][subsequence,][there][exist][(¯] _[t,]_[ ¯] _[q]_[)] _[ ∈]_[[0] _[, T]_[]] _[ × Q]_[such][that] _n→_ + _∞_[0] _n→_ + _∞_[0][.] 

18 

_sn, tn −→_[and] _[q][n][, y][n] −→ n→_ + _∞[t]_[¯] _n→_ + _∞[q]_[¯][.] 

Moreover, we know that 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-02.png)


which implies 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-04.png)


Hence we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-06.png)


As _u_ is USC and _v_ is LSC, the lim sup when _n →_ + _∞_ of the left-hand side is nonpositive, which implies _n_ ( _qn − yn_ )[2] + _n_ ( _tn − sn_ )[2] _−−−−−→ n→_ + _∞_[0][.] 

Let us assume _t_[¯] = _T_ . Then we have, as _u_ is USC and _v_ is LSC: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-09.png)


which constitutes a contradiction. Necessarily, _t < T_[¯] . 

Hence, for _n_ large enough we must have _tn, sn < T_ , and we know that ( _tn, qn_ ) is a maximum point of _u − ϕn_ where 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-12.png)


By Proposition 2, we have: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-14.png)


Furthermore, ( _sn, yn_ ) is a minimum point of _v − ξn_ where 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-16.png)


and by the same argument 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-18.png)


Therefore by combining the two inequalities we get 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0019-20.png)


19 

By rearranging the terms, we get: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0020-01.png)


We know that _qn, yn −→_[Therefore,][(] _[ψ]_[(] _[q][n]_[)] _[ −][ψ]_[(] _[y][n]_[))] _[ −−−−−→] n→_ + _∞[q]_[¯][.] _n→_ + _∞_[0] _[.]_ 

Moreover, by Lemma 4, there exists a constant _CH >_ 0 such that for all _n_ , 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0020-04.png)


We also have for almost every _z >_ 0 that 1 _{yn_ + _z∈Q}∩{qn_ + _z̸∈Q} −−−−−→n→_ + _∞_[0] _[.]_ 

_v_ ( _sn,yn_ ) _−v_ ( _sn,yn_ + _z_ ) By Lemma 2, the term _zH[b] z_ is bounded uniformly in _n_ and _z,_ and by the absolute � � continuity of _µ[b]_ , the dominated convergence theorem enables us to conclude that: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0020-07.png)


By the same reasoning: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0020-09.png)


We can thus choose _n_ large enough so that the right-hand side of (12) is negative. 

However, on the left-hand side of (12), all the integrals are always nonnegative; indeed, we have 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0020-12.png)


20 

therefore _v_ ( _sn, yn_ ) _− v_ ( _sn, yn − z_ ) _≤ u_ ( _tn, qn_ ) _− u_ ( _tn, qn − z_ ) and as _H[a]_ is nonincreasing, we get the result (the proof is identical for the integrals with _H[b]_ ). 

Therefore, the left-hand side is nonnegative for every _n_ . But, as we said before, for _n_ large enough, the right-hand side of (12) is negative, which yields a contradiction. 

In conclusion, we necessarily have sup _u − v ≤_ 0. [0 _,T_ ] _×Q_ 

## **Theorem 2.** _θ is the only continuous viscosity solution to_ (HJ) _._ 

_Proof._ We know that _θ_ is a bounded viscosity solution of (HJ), and in particular, _θ∗_ is a bounded supersolution of (HJ), _θ[∗]_ is a bounded subsolution of (HJ), and _θ∗_ ( _T, ._ ) = _θ[∗]_ ( _T, ._ ) = _−ℓ_ . 

Hence _θ∗_ and _θ[∗]_ verify the assumptions of Theorem 1, and we get that _θ∗ ≥ θ[∗]_ on [0 _, T_ ] _× Q._ But by definition of _θ∗_ and _θ[∗] ,_ we have _θ∗ ≤ θ ≤ θ[∗] ._ Thus we have _θ∗_ = _θ_ = _θ[∗] ,_ and _θ_ is continuous. 

Let us now assume that we have another continuous viscosity solution _θ_[˜] . In particular, _θ_[˜] is a subsolution to (HJ) and _θ_ is a supersolution to (HJ), and as _θ_[˜] ( _T, q_ ) = _θ_ ( _T, q_ ) = _−ℓ_ ( _q_ ) _∀q ∈Q_ , we know by the comparison principle that _θ_[˜] _≤ θ_ on [0 _, T_ ] _× Q_ . But we also have that _θ_[˜] is a supersolution and _θ_ is a subsolution, so by the same argument we have _θ_[˜] _≥ θ_ and finally _θ_[˜] = _θ_ on [0 _, T_ ] _× Q_ . Hence the uniqueness. 

## **4 Numerical results** 

## **4.1 Context and parameters** 

In this section, we apply our model to the foreign exchange spot market where market makers have access to a variety of trading venues in a number of geographical locations with overall depth of liquidity often exceeding their own resources. 

In order to derive realistic parameters we consider a set of HSBC FX streaming clients trading the US Dollar against offshore Chinese Renminbi, USDCNH. The set is sufficiently diverse to provide realistic results but by no means complete to fully represent HSBC FX market making franchise. In particular, in this work we mainly consider connections sensitive to pricing and do not take into account any cross currency trading which may significantly contribute to risk management of the chosen currency pair. 

Many FX market participants submit quotes to electronic communication networks and their prices may not necessarily indicate commitment (the so-called “Last Look” practice, see Cartea et. al [14]). Therefore we take the firm primary mid price as the reference price at any point in time. Typically, Refinitiv and/or Electronic Broking Services (EBS) are considered as primary FX spot sources, depending on currency pair. USDCNH trades on both. 

Since market practitioners are used to reason in basis points[8] (bps) as far as quotes are concerned, we decided to slightly adapt our model by factoring out _S_ 0 from _σ_ , _k_ , _δ_ , _L_ , _ψ_ , and _ℓ_ (with of course an adjustment of parameters in accordance for intensities). This boils down to factoring out _S_ 0 from the value function _θ_ and we can therefore reason in bps throughout (up to a little approximation because the base price at any time _t_ is _S_ 0, not _St_ , but this makes very little difference given the time frame of the problem we shall consider). 

In what follows we consider therefore the following parameters (rescaled as above): 

- Volatility parameter: _σ_ = 50 bps _·_ day _[−]_[1] 2 . 

> 8A basis point is is one hundredth of a percent. 

21 

- Using a standard log-likelihood optimisation technique, we fit the following logistic intensity functions: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0022-01.png)


and obtained _λR_ = 1000 day _[−]_[1] , _α_ Λ = _−_ 1, and _β_ Λ = 10 bps _[−]_[1] . This corresponds to 1000 requests per day, a probability of 1+1 _e[−]_[1] _[≃]_[73%][to][trade][when][the][answered][quote][is][the][reference][price][and][a] probability of 1+1 _e_[1] _[≃]_[27%][to][trade][when][the][answered][quote][is][the][reference][price][worsen][by][0.2][bps.] 

- In practice, a pricing ladder for only a few characteristic sizes is quoted. We therefore discretize the distribution of request sizes, with 4 possible sizes: _z_[1] = 1 M$, _z_[2] = 5 M$, _z_[3] = 10 M$, and _z_[4] = 20 M$, with respective probability _p_[1] = 0 _._ 76, _p_[2] = 0 _._ 15, _p_[3] = 0 _._ 075 and _p_[4] = 0 _._ 015. 

Regarding the objective function, we consider the following: 

- Time horizon given by _T_ = 0 _._ 05 days. This horizon ensures convergence towards stationary quotes at time _t_ = 0 _._ 

- _L_ : _v ∈_ R _�→ ηv_[2] + _φ|v|_ with _η_ = 10 _[−]_[5] bps _·_ day _·_ M$ _[−]_[1] and _φ_ = 0 _._ 2 bps. 

- Permanent market impact: _k_ = 0 _._ 005 bps _·_ M$ _[−]_[1] . 

- _ψ_ : _q ∈_ R _�→[γ]_ 2 _[σ]_[2] _[q]_[2][with] _[γ]_[= 0] _[.]_[0005][bps] _[−]_[1] _[ ·]_[ M$] _[−]_[1][.] 

- _ℓ_ = 0 _._ 

We impose risk limits in the sense that no trade that would result in an inventory _|q| > q_ ˜ is admitted, where _q_ ˜ = 100 M$. We then approximate the solution _θ_ to (HJ) using a monotone implicit Euler scheme on a grid with 201 points for the inventory. 

## **4.2 Results** 

The value function (at time _t_ = 0) is plotted in Figure 1. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0022-13.png)


**----- Start of picture text -----**<br>
Value function<br>10<br>0<br>10<br>20<br>30<br>40<br>50<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>**----- End of picture text -----**<br>


Figure 1: Value function of the problem for different values of the inventory. 

22 

We plot in Figure 2 the optimal trading rate of the market maker as a function of her inventory. Of course that trading rate is nonincreasing but we observe an interesting effect: a plateau around zero, thereafter referred to as the pure flow internalization area. This is due to the proportional transaction cost (given by the parameter _φ_ ), that discourages the trader to buy or sell actively when her inventory is small enough (she prefers to bear this small risk than to pay the execution costs). Permanent impact also discourages external execution. We note that permanent impact has no influence on classical Almgren-Chriss optimal schedules (or marginal influence in the discrete formulation). The reason is that it is proportional to the overall quantity and thus independent of the way the order is executed. The situation is quite different here as no market impact is expected when the flow is internalized. Therefore, external trading brings additional relative cost by pushing the expected price for all the subsequent fills. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0023-01.png)


**----- Start of picture text -----**<br>
Optimal execution rate (in M$  s 1) within the liquidity pool<br>Optimal execution rate (M$  s 1)<br>Limits of the pure flow internalization area<br>0.2<br>0.1<br>0.0<br>0.1<br>0.2<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>1)<br>s<br>Execution rate (M$<br>**----- End of picture text -----**<br>


Figure 2: Optimal execution rate as a function of the inventory. 

To observe the impact of the request size on the optimal quotes, we plot in Figure 3 the four functions _q �→−δ_[¯] _[b]_ (0 _, q, z[k]_ ) _, k ∈{_ 1 _, . . . ,_ 4 _},_ 

and the four functions 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0023-05.png)


where _δ_[¯] _[b]_ and _δ_[¯] _[a]_ represents the optimal quotes as a function of time, inventory and size of request, at the bid and at the ask, respectively. We see that accounting for the size of requests impacts the optimal bid and ask quotes. The monotonicity of the quotes is of course unsurprising. It is noteworthy that no market spread was parametrically introduced into the model during the estimation of the logistic parameters. Therefore, it is interesting to compare the bid-ask spread we obtain from the pure flow consideration against the actual market spread. Our current estimation produces 0.32 bps for $1M size. The average composite interbank spread of USDCNH at London open as of this writing (early June 2021) is 0.38 bps. 

Throughout this section, the optimal quotes are those derived from Lemma 1 and the optimal execution rates are those derived from Lemma 3. To confirm empirically that these controls are in line with the value function obtained with our numerical scheme, we performed Monte-Carlo simulations using those controls. The comparison between the value function approximated numerically and the proceed of the Monte-Carlo simulations is plotted in Figure 4. We see that the values coincide in our case. 

23 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0024-00.png)


**----- Start of picture text -----**<br>
Optimal bid and ask quotes (in bps) for different sizes of trades<br>1.00<br>Optimal quotes (bps) -- trades of size 1.0 M$<br>Optimal quotes (bps) -- trades of size 5.0 M$<br>Optimal quotes (bps) -- trades of size 10.0 M$<br>0.75 Optimal quotes (bps) -- trades of size 20.0 M$<br>Limits of the pure flow internalization area<br>0.50<br>0.25<br>0.00<br>0.25<br>0.50<br>0.75<br>1.00<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>Bid and ask quotes (bps)<br>**----- End of picture text -----**<br>


Figure 3: Optimal bid (bottom) and ask (top) quotes for different trade sizes as a function of the inventory. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0024-02.png)


**----- Start of picture text -----**<br>
Value function : PDE vs MC<br>Value function (PDE)<br>10 Monte-Carlo with 'optimal' controls<br>0<br>10<br>20<br>30<br>40<br>50<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>**----- End of picture text -----**<br>


Figure 4: Value function obtained by playing the optimal quotes and execution rates during a Monte-Carlo simulation compared with the value function computed with an implicit scheme. 

24 

## **4.3 Comparative statics regarding the pure flow internalization area** 

We now study the influence of the parameters on the width of the pure flow internalization area. 

We plot in Figure 5 the optimal trading rate of the market maker as a function of her inventory, when execution cost parameter _φ_ is set to 0 _._ 4 bps. We see that increasing _φ_ leads to a wider pure flow internalization area: the market maker is less inclined to pay for immediate hedging and waits for her inventory to reach a higher level of risk to start trading actively. 

We plot in Figure 6 the optimal trading rate of the market maker as a function of her inventory, when the permanent market impact parameter _k_ is set to 0 _._ 01 bps _·_ M$ _[−]_[1] . We see that increasing _k_ leads to a wider pure flow internalization area: the market maker is less inclined to impact the market, and waits for her inventory to reach a higher level of risk to start trading actively. 

We plot in Figure 7 the optimal trading rate of the market maker as a function of her inventory, when the risk aversion parameter _γ_ is set to 0 _._ 005 bps _[−]_[1] _·_ M$ _[−]_[1] . We see that increasing _γ_ leads to a narrower pure flow internalization area: the market maker is more risk averse, and therefore starts trading sooner to bring her inventory closer to 0. 

Finally, we plot in Figure 8 the optimal trading rate of the market maker as a function of her inventory, when the average number of requests per day _λR_ is set to 3000 day _[−]_[1] . We see that increasing _λR_ leads to a wider pure flow internalization area: the market maker receives more requests from client and has more frequent opportunities to trade and unwind her inventory without having to pay execution costs and impact the market. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0025-06.png)


**----- Start of picture text -----**<br>
Optimal execution rate (in M$  s 1) within the liquidity pool with =0.4 bps<br>0.20 Optimal execution rate (M$  s 1)<br>Limits of the pure flow internalization area for =0.2 bps<br>Limits of the pure flow internalization area for =0.4 bps<br>0.15<br>0.10<br>0.05<br>0.00<br>0.05<br>0.10<br>0.15<br>0.20<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>1)<br>s<br>Execution rate (M$<br>**----- End of picture text -----**<br>


Figure 5: Optimal execution rate as a function of the inventory when _φ_ increases. 

25 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0026-00.png)


**----- Start of picture text -----**<br>
Optimal execution rate (in M$  s 1) within the liquidity pool with k=0.01 bps M$ 1<br>Optimal execution rate (M$  s 1)<br>0.2 Limits of the pure flow internalization area for k=0.005 bps M$ 1<br>Limits of the pure flow internalization area for k=0.010 bps M$ 1<br>0.1<br>0.0<br>0.1<br>0.2<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>1)<br>s<br>Execution rate (M$<br>**----- End of picture text -----**<br>


Figure 6: Optimal execution rate as a function of the inventory when _k_ increases. 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0026-02.png)


**----- Start of picture text -----**<br>
Optimal execution rate (in M$  s 1) within the liquidity pool with =0.005 bps 1 M$ 1<br>Optimal execution rate (M$  s 1)<br>Limits of the pure flow internalization area for =0.0005 bps 1 M$ 1<br>0.75 Limits of the pure flow internalization area for =0.0050 bps 1 M$ 1<br>0.50<br>0.25<br>0.00<br>0.25<br>0.50<br>0.75<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>1)<br>s<br>Execution rate (M$<br>**----- End of picture text -----**<br>


Figure 7: Optimal execution rate as a function of the inventory when _γ_ increases. 

26 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0027-00.png)


**----- Start of picture text -----**<br>
Optimal execution rate (in M$  s 1) within the liquidity pool with  R [=3000 day] 1<br>0.15 Optimal execution rate (M$  s 1)<br>Limits of the pure flow internalization area for  R [=1000 day] 1<br>Limits of the pure flow internalization area for  R [=3000 day] 1<br>0.10<br>0.05<br>0.00<br>0.05<br>0.10<br>0.15<br>100 75 50 25 0 25 50 75 100<br>Inventory (M$)<br>1)<br>s<br>Execution rate (M$<br>**----- End of picture text -----**<br>


Figure 8: Optimal execution rate as a function of the inventory when _λR_ increases. 

## **Conclusion** 

In this paper, we generalized existing OTC market making models, and in particular the one presented in Bergault and Guéant [9], to introduce the possibility for the market maker to trade “actively” in some liquidity pools in order to unwind part of her inventory. This extension led to a partial integro-differential equation of the Hamilton-Jacobi (HJ) type, to which we prove that the value function of the problem is the unique continuous viscosity solution. We illustrated our results numerically by solving the equation on a grid using an implicit Euler scheme and computing the optimal quotes and trading rates. We highlighted the existence of a pure flow internalization area. This area depicts a subtle balance between uncertainty, execution cost, and market impact. It is wider for a less risk averse market maker with a larger franchise, exposed to higher transaction costs and market impact. 

## **Acknowledgment** 

The results presented in this paper are part of the research works carried out within the HSBC FX Research Initiative. The views expressed are those of the authors and do not necessarily reflect the views or the practices at HSBC. The authors are grateful to Richard Anthony (HSBC), Bruno Bouchard (Université Paris Dauphine), Nicolas Grandchamp des Raux (HSBC) and Paris Pennesi (HSBC) for helpful discussions and support throughout the project. 

## **Appendix** 

In this appendix, we prove Proposition 2. More exactly, we only prove the subsolution part (the proof for the supersolution part is identical). 

Let us first assume that the following inequality holds: 

27 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0028-00.png)


We know that _∀z >_ 0: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0028-02.png)


Thus: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0028-04.png)


and the same holds for _H[b]_ : 

So we get: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0028-07.png)


and _u_ is a viscosity subsolution. 

Let us now assume that _u_ is a viscosity subsolution. Without loss of generality, we can assume _ϕ_ ( _t,_[¯] ¯ _q_ ) = _u_ ( _t,_[¯] ¯ _q_ ). 

Let _Bη_ be the open ball of center ( _t,_[¯] ¯ _q_ ) and radius _η >_ 0. Let ( _un_ ) be a sequence of smooth functions uniformly (in _n_ ) bounded such that _un ≥ u ∀n_ and _un −−−−−→_[Let] _[ ξ]_[ be a smooth nondecreasing] _n→_ + _∞[u]_[ pointwise.] function such that _ξ_ ( _x_ ) = 1 if _x > η/_ 4 and _ξ_ ( _x_ ) = 0 if _x < −η/_ 4. Let _dη/_ 2 be the algebraic distance to _∂Bη/_ 2 (with _dη/_ 2 _>_ 0 on _Bη/_ 2 and _dη/_ 2 _≤_ 0 on _Bη/[c]_ 2[);][this][function][is][continuously][differentiable.][We] introduce: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0028-11.png)


Then ( _t,_[¯] ¯ _q_ ) is still a max of _u − ϕ[n] η_[and][(] _[u][ −][ϕ][n] η_[)(¯] _[t,]_[ ¯] _[q]_[)][=][0][.][Furthermore][we][have] _∂ϕ∂t[n] η_[(¯] _[t,]_[ ¯] _[q]_[)][=] _[∂] ∂t[ϕ]_[(¯] _[t,]_[ ¯] _[q]_[)][and] _∂qϕ[n] η_[(¯] _[t,]_[ ¯] _[q]_[) =] _[ ∂][q][ϕ]_[(¯] _[t,]_[ ¯] _[q]_[)][for][all] _[i][ ∈][I][T]_[.][Thus:] 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0028-13.png)


Plus we have _ϕ[n] η[−−−−−→] n→_ + _∞[ϕ][η]_[pointwise][with] _[ϕ][η]_[=] _[ ϕ][ ×]_[ (] _[ξ][ ◦][d][η/]_[2][) +] _[ u][ ×]_[ (1] _[ −][ξ][ ◦][d][η/]_[2][)][which][is][smooth][on] _[B][η/]_[4] and such that _ϕη_ = _u_ on _Bη[c]_[and] _[ϕ][η]_[(¯] _[t,]_[ ¯] _[q]_[) =] _[ u]_[(¯] _[t,]_[ ¯] _[q]_[)][.] 

By continuity of _H[a]_ and _H[b]_ , absolute continuity of _µ[b]_ and _µ[a]_ and by dominated convergence (using the same argument than in Lemma 2 and the fact that the _ϕ[n] η_[are][bounded][uniformly][in] _[n]_[)][we][get:] 

28 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0029-00.png)


By then sending _η_ to 0 and using again dominated convergence, we get the result: 


![](markdown_output/Algorithmic_market_making_in_foreign_exchange_cash_images/Algorithmic_market_making_in_foreign_exchange_cash.pdf-0029-02.png)


## **References** 

- [1] Frédéric Abergel, Marouane Anane, Anirban Chakraborti, Aymen Jedidi, and Ioane Muni Toke. _Limit order books_ . Cambridge University Press, 2016. 

- [2] Frédéric Abergel, Côme Huré, and Huyên Pham. Algorithmic trading in a microstructural limit order book model. _Quantitative Finance_ , 20(8):1263–1283, 2020. 

- [3] Robert Almgren and Neil Chriss. Optimal execution of portfolio transactions. _Journal of Risk_ , 3:5–40, 2001. 

- [4] Robert F Almgren. Optimal execution with nonlinear impact functions and trading-enhanced risk. _Applied mathematical finance_ , 10(1):1–18, 2003. 

- [5] Yakov Amihud and Haim Mendelson. Dealership market: Market-making with inventory. _Journal of financial economics_ , 8(1):31–53, 1980. 

- [6] Marco Avellaneda and Sasha Stoikov. High-frequency trading in a limit order book. _Quantitative Finance_ , 8(3):217–224, 2008. 

- [7] Alexey Bakshaev. Market-making with reinforcement-learning (sac). _arXiv preprint arXiv:2008.12275_ , 2020. 

- [8] Philippe Bergault, David Evangelista, Olivier Guéant, and Douglas Vieira. Closed-form approximations in multi-asset market making. _arXiv preprint arXiv:1810.04383_ , 2020. 

- [9] Philippe Bergault and Olivier Guéant. Size matters for otc market makers: general results and dimensionality reduction techniques. _Mathematical Finance_ , 2020. 

- [10] Agostino Capponi, José E Figueroa-López, and Chuyi Yu. Market making with stochastic liquidity demand: Simultaneous order arrival and price change forecasts. _arXiv preprint arXiv:2101.03086_ , 2021. 

- [11] Álvaro Cartea, Ryan Donnelly, and Sebastian Jaimungal. Algorithmic trading with model uncertainty. _SIAM Journal on Financial Mathematics_ , 8(1):635–671, 2017. 

- [12] Álvaro Cartea, Sebastian Jaimungal, and José Penalva. _Algorithmic and high-frequency trading_ . Cambridge University Press, 2015. 

- [13] Álvaro Cartea, Sebastian Jaimungal, and Jason Ricci. Buy low, sell high: A high frequency trading perspective. _SIAM Journal on Financial Mathematics_ , 5(1):415–444, 2014. 

- [14] Alvaro Cartea, Sebastian Jaimungal, and Jamie Walton. Foreign exchange markets with last look. _Mathematics and Financial Economics_ , 13(1):1–30, 2019. 

29 

- [15] Thomas E Copeland and Dan Galai. Information effects on the bid-ask spread. _the Journal of Finance_ , 38(5):1457–1469, 1983. 

- [16] Pietro Fodra and Huyên Pham. High frequency trading and asymptotics for small risk aversion in a markov renewal model. _SIAM Journal on Financial Mathematics_ , 6(1):656–684, 2015. 

- [17] Pietro Fodra and Huyên Pham. Semi-markov model for market microstructure. _Applied Mathematical Finance_ , 22(3):261–295, 2015. 

- [18] Lawrence R Glosten and Paul R Milgrom. Bid, ask and transaction prices in a specialist market with heterogeneously informed traders. _Journal of financial economics_ , 14(1):71–100, 1985. 

- [19] Sanford J Grossman and Merton H Miller. Liquidity and market structure. _the Journal of Finance_ , 43(3):617–633, 1988. 

- [20] Olivier Guéant and Iuliia Manziuk. Deep reinforcement learning for market making in corporate bonds: beating the curse of dimensionality. 2019. 

- [21] Olivier Guéant. _The Financial Mathematics of Market Liquidity: From optimal execution to market making_ , volume 33. CRC Press, 2016. 

- [22] Olivier Guéant. Optimal market making. _Applied Mathematical Finance_ , 24(2):112–154, 2017. 

- [23] Olivier Guéant, Charles-Albert Lehalle, and Joaquin Fernandez-Tapia. Dealing with the inventory risk: a solution to the market making problem. _Mathematics and financial economics_ , 7(4):477–507, 2013. 

- [24] Fabien Guilbaud and Huyen Pham. Optimal high-frequency trading with limit and market orders. _Quantitative Finance_ , 13(1):79–94, 2013. 

- [25] Fabien Guilbaud and Huyên Pham. Optimal high-frequency trading in a pro rata microstructure with predictive information. _Mathematical Finance_ , 25(3):545–575, 2015. 

- [26] Thomas Ho and Hans R Stoll. Optimal dealer pricing under transactions and return uncertainty. _Journal of Financial economics_ , 9(1):47–73, 1981. 

- [27] Thomas SY Ho and Hans R Stoll. The dynamics of dealer markets under competition. _The Journal of finance_ , 38(4):1053–1074, 1983. 

- [28] Maureen O’hara and George S Oldfield. The microeconomics of market making. _Journal of Financial and Quantitative analysis_ , pages 361–376, 1986. 

- [29] Hans R Stoll. Market microstructure. In _Handbook of the Economics of Finance_ , volume 1, pages 553–604. Elsevier, 2003. 

30 

