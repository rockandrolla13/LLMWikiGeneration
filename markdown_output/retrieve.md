_Quantitative Finance_ , 2015 Vol. 15, No. 8, 1279–1291, http://dx.doi.org/10.1080/14697688.2015.1032543 

## **Optimal execution with limit and market orders** 

## ÁLVARO CARTEA[∗] † and SEBASTIAN JAIMUNGAL‡ 

†Department of Mathematics, University College London, Gower Street, London WC1E 6BT, UK ‡Department of Statistical Sciences, University of Toronto, 27 King’s College Circle, Toronto, ON M5S, Canada 

( _Received 25 February 2014; accepted 21 July 2014_ ) 

We develop an optimal execution policy for an investor seeking to execute a large order using limit and market orders. The investor solves the optimal policy considering different restrictions on volume of both types of orders and depth at which limit orders are posted. We show how the execution policies perform when targeting the volume schedule of the Almgren–Chriss execution strategy. The different strategies considered by the investor outperform the Almgren–Chriss price with an average savings per share of about one to two and a half times the spread. This improvement over Almgren–Chriss is due to the strategies benefiting from the optimal mix of limit orders, which earn the spread and market orders, which keep the investor’s inventory schedule on target. 

_Keywords_ : Algorithmic trading; High-frequency trading; Acquisition; Liquidation; Impulse control; TWAP 

## **1. Introduction** 

The main role of exchanges is to provide immediacy to investors who wish to buy or sell assets. Immediacy is provided by dealers and other patient investors who submit passive orders to the limit order book (LOB) and, as compensation, receive the bid-ask spread. A wider spread incentivizes liquidity provision, but increases the cost of executing market orders, while a narrower spread has the opposite effect. The spread is a good measure of the cost of immediacy, but not the only one. Depth of the LOB is another important dimension of this cost which is key to impatient traders who seek to execute large orders. 

Large orders which are executed in one transaction have market impact because their volume is greater than the volume available in the LOB at the best posted quote. Impatient investors can mitigate the adverse effect of trading a large order by devising algorithmic strategies to schedule the order over a time span which is given by the urgency she has to execute the trade. In general, as a rule of thumb in the literature, the investor breaks up the parent order into child orders and executes each one ofthemusing marketorders,see,forinstance,Almgren and Chriss (2001), Almgren (2003), whereas in practice, optimal execution strategies seek the optimal mix of limit and market orders. The performance of strategies is gauged against different benchmarks depending on the objective. Common benchmarks include: arrival price, which is the price of the asset at the time when the order is given to execute the trade, 

the Time-Weighted Average Price (TWAP) and the VolumeWeighted Average Price which are calculated over the time span when the order is executed. 

The main contribution of this paper is to show how to optimally trade a large position in one asset when the investor includes both limit and market orders in the strategy. Market orders guarantee execution but pay the spread and other fees in addition to having market impact, see Alfonsi _et al._ (2010) and Guéant and Lehalle (Forthcoming), while the execution of limit orders is not guaranteed but ‘earn’ the investor the spread and sometimes earn them a rebate for providing liquidity, see Cartea and Jaimungal (2013). Another contribution of our paper is to show how the optimal execution strategy is improved by allowing the investor to decide the volume to trade in each market or limit order. Related to our work is that of Huitema (2013) who looks at portfolio execution using market and limit orders taking into account temporary and permanent price impact, and that of Guéant _et al._ (2012) who look at execution of portfolios using limit orders only. Cartea _et al._ (2013) show how an algorithmic trader takes a view on the distribution of prices at a future date and then decides how to trade in the direction of her predictions using the optimal mix of market and limit orders. 

Moreover, Guilbaud and Pham (2013b) look at optimal strategies for a market maker who uses both limit and market orders, for a prorata treatment see Guilbaud and Pham (2013a), see also Bayraktar and Ludkovski (2011) where the agent submits orders discretely and the authors solve an impulse control problem corresponding to when, and how large, to send market 

> ∗Corresponding author. Email: a.cartea@ucl.ac.uk 

© 2015 Taylor & Francis 

_Á. Cartea and S. Jaimungal_ 

1280 

orders, and Bayraktar and Ludkovski (2014) where the agent decides on the depth at which to post limit orders. A related problem to optimal execution is the optimal trading strategy for accelerated share repurchases which has recently been studied by Kinzebulatov _et al._ (2013) and Guéant _et al._ (2013). Such generalizations of the execution problem can also be addressed along the lines in this work. 

We discuss the optimal execution model with limit and market orders by looking at the optimal strategy to target a provided schedule when the investor employs three types of strategies: (i) chooses the depth of the limit order, but can only have one resting order for one unit of the asset at any one time, and market orders are only for one unit; (ii) posts only at the best bid (optimal acquisition) or best offer (optimal liquidation) and can only have one resting order for one unit of the asset at a time and market orders are only for one unit; (iii) posts limit orders only at the best bid or best offer, with no restriction on the volume, and can also decide how many shares she executes when sending market orders. 

As particular examples, the investor devises a strategy to acquire a large number of shares that targets the volume schedule of the Almgren–Chriss optimal execution and the volume schedule of TWAP. We use simulations to analyse the performance of the three strategies described above and show that, while the investor targets the volume schedule, the acquisition costs of her strategy are lower than those obtained using Almgren–Chriss and TWAP. Moreover, if the investor marks to markettheacquisitioncostsduringtheexecutionofthestrategy before its terminal date, the three strategies are nearly always outperforming Almgren–Chriss and TWAP. These purchase savings relative to the two benchmarks we analyse, which are most of the time between one and two and a half times the spread posted on the LOB, stem from the strategies benefiting from the optimal mix of limit orders that earn the spread and market orders that keep the investor’s inventory schedule on target. 

The rest of this paper is organized as follows. Section 2 introduces the model solved by the investor. Section 3 derives the dynamic programming equation for an investor who optimizes over the depth of the limit orders and scheduling of market orders, and we illustrate the performance of the strategy when the investor targets the Almgren–Chriss and TWAP inventory schedules. Section 4 solves the investor’s problem when the strategy employs limit orders, restricted to posting only at the touch, and market orders and section 5 lifts the restriction on the volume of limit and market orders. 

## **2. Model** 

We assume that the spread between the best bid and best ask is constant at 2 _�_ with _�_ ≥ 0 and the asset’s midprice follows 


![](markdown_output/retrieve_images/retrieve.pdf-0002-08.png)


where _σ >_ 0 is the tick size and _Zt_[±][are mutually independent] Poisson processes both with intensity _γ_ representing times at which the asset’s midprice jumps by _σ_ . 

Here, we only focus on the acquisition problem as the liquidation problem is similar. The investor uses both limit and market orders to acquire N lots of shares of the asset over a 

time span of _T_ . For example, if N = 10, this can be interpreted as acquiring 10 lots of 100 shares each. The limit orders are for one unit or lot of the asset and are posted in the LOB at _St_ − _δt_ , where _δt_ ≥ 0 measures how deep in the bid side are the orders submitted. If necessary, the investor crosses the spread by placing market orders, for one unit of the asset, which are executed at _St_ + _�_ + _ε_ , where _ε_ ≥ 0 is a liquidity taking fee— we denote the total effective half-spread by _ϒ_ := _�_ + _ε_ . We assume that limit orders do not earn a rebate, this can be easily incorporated in the analysis, see e.g. Cartea and Jaimungal (2013). 

We assume that the probability that the investor’s limit order is filled, given that a market orders arrives, is exponential _e_[−] _[κδ][t]_ , with _κ >_ 0. Other participants’ market sell orders arrive at the exchange according to a homogeneous Poisson process _Mt_ (independent of _Zt_[±][) with rate] _[ λ]_[ =] _[λ]_[˜] _[e][κ�]_[, thus the intensity of] the counting process for filled limit orders is _λ e_[−] _[κδ][t]_ . Here, _λ >_[˜] 0 is the rate of arrival of market orders at the best bid because in our formulation, limit orders resting there have depth _δ_ = _�_ . Finally, let _Nt_ denote the number of the investor’s limit buy orders that have been filled, and let _Mt_[0][denote][the][number] of market orders the investor has placed up to and including time _t_ .Throughout we work on a completed filtered probability space � _�,_ P _,_ F _, F_ = { _(Fs)_ 0≤ _t_ ≤ _T_ }� where the filtration is the natural one generated by the processes _Mt_ , _St_ and _Nt_ . 

With these assumptions, the investor’s wealth process _Xt_ satisfies the stochastic differential equation 


![](markdown_output/retrieve_images/retrieve.pdf-0002-14.png)


wheretheinvestor’sownmarketordersare _Mt_[0][=][ �] _k[K]_ =1[1][{] _[τ] k_[≤] _[t]_[}] with _K_ ≤ N, 1{·} is the indicator function, and _**τ**_ = { _τk_ : _k_ = 1 _, . . . , K_ } denotes the sequence of increasing stopping times (0 _< τ_ 1 _<_ · · · _< τK_ ) at which she places market orders. Note that the investor may place fewer, but never more, than N market orders. 

The investor’s value function is 


![](markdown_output/retrieve_images/retrieve.pdf-0002-17.png)


Here, the notation E _t,x,S,q_ [·] denotes the conditional expectation given that _Xt_ − = _x, St_ − = _S, qt_ − = _q_ , _q t_ = N − _qt_ is the number of shares remaining to be acquired at time _t_ , and q _t_ denotes the target inventory schedule of the investor, e.g. for an investor who targets TWAP or the Almgren–Chriss optimal execution schedule. Moreover, the set of admissible strategies _A_ consist of _Ft_ -stopping times (bounded above by _T_ ) and bounded _Ft_ -predictable spreads _δt_ , and the investor ceases to post market or limit orders once all inventory has been acquired, i.e. once _qt_ = N . 

On the right-hand side of the value function, there are three terms. The first is the investor’s terminal wealth (negative costs) from purchasing the shares throughout the trading horizon. The second is the costs that the investor incurs when acquiring the outstanding position _q T_ using a market order.These costs are: crossing the spread, liquidity taking fees and market impact costs (walking up the LOB) captured by _q T c_ ~~_(_~~ _q T )_ , with 

_Optimal execution_ 

1281 

_c(q)_ a non-negative increasing function in _q_ . Finally, the last term penalizes deviations from the investor’s target schedule— the larger is the target penalty parameter _φ >_ 0, the more resolute is the investor to achieve it. 

It is possible to incorporate the effect of adverse selection on the trading strategy by assuming that when other participants’ market orders arrive, they may induce a jump in the midprice in the direction of the trade. In this case, the midprice satisfies the SDE 


![](markdown_output/retrieve_images/retrieve.pdf-0003-04.png)


where _η_ 0[±][,] _[ η]_ 1[±][,] _[ . . .]_[ are i.i.d. random variables representing the] random jump in midprice just after a market order event, and _Mt_[±][are the counting processes for other participants’ buy and] sell market orders. Cartea and Jaimungal (Forthcoming) adopt such a model to solve for the optimal behaviour of a market maker and demonstrate that the market maker widens spreads to account for the potential adverse selection costs, see also Cartea _et al._ (2014) for a model of adverse selection and market making, see also Cartea _et al._ (2013). This generalization is possible here as well; however, we opt to focus instead on how allowing both limit and market orders affect the trader’s decisions. 

running penalty for deviations from the target inventory level. In the second line, the supremum represents the investor’s ability to control how deep to post limit orders and the subsequent change in the state variables and value function that result from her limit buy order being hit. The third line accounts for the change in the state variables and value function if the investor submits a market order at that time. The overall maximum represents the investor’s choice in waiting for the posted limit order to be filled or immediately execute a market buy order. 

By making the ansatz 


![](markdown_output/retrieve_images/retrieve.pdf-0003-08.png)


the midprice and wealth can be factored out and the QVI (5) reduces considerably to the following QVI for _h(t, q)_ 


![](markdown_output/retrieve_images/retrieve.pdf-0003-10.png)


for _q_ = 0 _, . . . ,_ N−1 and the terminal and boundary conditions reduce to 


![](markdown_output/retrieve_images/retrieve.pdf-0003-12.png)


## **3. The dynamic programming equations** 

To solve the combined optimal stopping and control problem described above, we adopt the dynamic programming principle, and standard results imply that the value function (3) is the unique viscosity solution to the quasi-variational inequality (QVI): 


![](markdown_output/retrieve_images/retrieve.pdf-0003-15.png)


for _q_ = 0 _,_ 1 _, . . . ,_ N − 1 and the value function is subject to the terminal and boundary conditions 


![](markdown_output/retrieve_images/retrieve.pdf-0003-17.png)


The terminal condition corresponds to the penalty of acquiring all remaining N − _q_ shares at maturity, while the boundary condition corresponds to the penalty of acquiring all N shares too early. The sequence of stopping times is determined by the condition that the maximum is attained by the second term in (5). 

The various terms in the QVI (5) may be interpreted as follows. On the first line, the first two terms are due to changes in the midprice as a result of market events which move the midprice a tick up or down, and the last term represents the 

The ansatz (7) has three terms.The first term is the accumulated cash, the second term denotes the book value of the remaining inventory which is marked to market using the midprice and finally the function _h(t, q)_ represents the added value to the investor’s cash from optimally acquiring the remaining shares. 

Next, the first-order condition provides the optimal depth, in feedback control form, of the limit order in the continuation region as 


![](markdown_output/retrieve_images/retrieve.pdf-0003-22.png)


Upon substituting this optimal feedback control into the QVI, _h_ solves 


![](markdown_output/retrieve_images/retrieve.pdf-0003-24.png)


for _q_ = 0 _, . . . ,_ N−1. From (11), we see that when the investor has inventory _q_ , she executes a market order at time _τq_ , where _τq_ satisfies 


![](markdown_output/retrieve_images/retrieve.pdf-0003-26.png)


This can be interpreted as executing a market order whenever doing so increases the function _h_ by the half-spread plus the transaction cost or in terms of the value function, execute a market order when the change in the value function is zero. Combining this observation with the feedback form for the optimal depth above, we can place a simple lower bound 


![](markdown_output/retrieve_images/retrieve.pdf-0003-28.png)


Inserting the expression for _ϒ_ , we see that the investor will not post within the half-spread if _κ_[1] _[>]_[2] _[ �]_[+] _[ ε]_[.][Setting] 

_Á. Cartea and S. Jaimungal_ 

1282 

_h(t, q)_ = _κ_[1][log] _[ ω(][t][,][ q][)]_[,][then][(][11][)][can][be][recast][as][the][linear] complementarity problem 

essential statistics for four assets of varying liquidity (as measured by daily volume) using NASDAQ ITCH data from the 


![](markdown_output/retrieve_images/retrieve.pdf-0004-04.png)


In the continuation region, the strategy posts limit orders according to (10) and if the order is not filled, it is cancelled and reposted at every trading time. The optimal depth of the limit order consists of three terms. The first term only depends on the fill probability. An investor who aims at acquiring a position does so by posting in the LOB by maximizing the expected depth she earns, _δe_[−] _[κδ]_ , relative to the midprice without considering urgency or inventory position. The last two terms adjust the optimal depth based on the inventory exposure based on how is the strategy tracking the target and how adamant is the investor to achieve a perfect match of the target at every trading time. 

The obstacles in the linear complementarity problem correspond to the stopping times of execution of the market orders. That is, the solution to the linear complementarity problem provides the investor with a sequence of times _τq_ at which the investorshouldexecuteamarketorderifherpostedlimitorders are not filled by that time. We call this boundary the _trigger boundary_ since the investor’s inventory will only hit it if she has acquired too little inventory by time _τq_ . This boundary tracks the target inventory, but since the investor is allowed to post limit orders, so that they execute at better prices than a market order, it will not lie on top of the target schedule q _t_ . In the limit of zero penalty, the investor only posts limit orders and may acquire all remaining inventory at maturity using a market order, while large penalties induce the investor to post market orders when inventories deviate slightly from the target inventory. 

## _**3.1. Targeting Almgren–Chriss**_ 

In this section, we use as target the inventory schedule implied by the classical Almgren–Chriss optimal execution strategy, see Almgren and Chriss (2001).We use simulations to compare the acquisition costs of the investor’s strategy to the acquisition costs of Almgren–Chriss. In our notation, this means that the investor wishes to target 


![](markdown_output/retrieve_images/retrieve.pdf-0004-09.png)


˜ ˜ Here, _χ_ = � _ξ σ_[2] _/k_ where _σ_[2] = 2 _σ_[2] _γ_ is the effective volatility of the asset midprice, _ξ_ is an urgency parameter which the investor is free to choose (larger values cause the investor to liquidate faster) and _k_ is the temporary impact that trading has on prices, so that the execution price the investor pays is _St_ + _k νt_ where _νt_ is the investor’s continuous rate of trading. 

We choose the parameters in the simulations by looking at empirical data from NASDAQ. In table 1, we report some 

lastquarterof2013.Wereporttheaveragedailyvolume(ADV), the mean rate of arrival of midprice changes _γ_ , the rate of arrival of market orders _λ_[˜] and the rate of arrival of matching executions _λ_[ˆ] . The last two statistics require some further explanation. When a market order arrives, the ITCH data records it as several messages, one for each posted limit order (agent by agent) that the market order hits/lifts—even if it is a single market order being filled at the same price. In this manner, a single market order will have several matching executions.The statistic _λ_[ˆ] reports the arrival rate of these matching executions. To estimate _λ_[˜] , the rate of arrival of a market order, we assume that when executions occur within the same millisecond, as a contiguous sequence of orders all in the same direction, this sequence is in fact a single market order being matched to several limit order posts, and report this rate of arrival. This aggregation provides an underestimate of the true arrival rate because within 1 ms, more than one market order could have arrived. 

We use simulations to see how the strategy performs (by looking at acquisition costs) for different values of the arrival rate of market orders _λ_ and the target penalty parameter _φ_ . We assumethatthemarketimpactcost _c(q)_ = _α q_ with _α_ = 0 _._ 001. The other model parameters are 


![](markdown_output/retrieve_images/retrieve.pdf-0004-14.png)


the trading horizon is 5 min (so that _T_ = 300 s), wish to acquire N = 10 shares, and _S_ 0 = 100. For the target schedule, we fix _χ_ = 0 _._ 02 regardless of all of other parameters, so that when we comparedifferingvolatilitiesandmarketorderarrivalrates,the investor targets the same schedule. In the simulations below, we use _γ_ = {1 _,_ 10 _,_ 100} and recall that the spread is 2 _�_ which is 1 cent. For each set of parameters, we simulate 10 000 runs of the acquisition and in figure 1, we show different aspects of the strategy. The top left panel shows the midprice and buy limit orders posted by the investor. In the same panel, the solid circles denote the investor’s filled limit orders whilst the open circles are other participants’ market orders (not filled by the investor’s passive orders), and the squares denote the investor’s executed market buys. 

In top right panel, for the sample path shown, the dashed line is the Almgren–Chriss scheduling given above in (15), the solid line shows the strategy’s accumulated inventory and the solid squares represent the trigger boundary for each inventory level. To the left of this boundary, the investor does not send market orders but waits for her limit order to be filled. However, if there is no fill, then at the trigger boundary, the investor sends a buy market order for one share to bring the accumulated inventory back in line with that of the 

_Optimal execution_ 

1283 

Table 1. Market statistics from last quarter of 2013 using NASDAQ ITCH data. 

||ORCL<br>NTAP<br>SMH<br>FARO<br>ADV<br>2 623 112<br>939 419<br>160 022<br>22 807<br>~~˜~~_λ_<br>0.0694<br>0.1120<br>0.1092<br>0.0856<br>ˆ_λ_<br>0.2556<br>0.1704<br>0.0131<br>0.0061<br>_γ_<br>0.0787<br>0.0683<br>0.0087<br>0.0045|
|---|---|



Notes: Average daily volume (ADV), rate of arrival of market orders _λ_[˜] per second, rate of arrival of matching executions _λ_[ˆ] per second, rate of arrival of midprice changes _γ_ per second. 


![](markdown_output/retrieve_images/retrieve.pdf-0005-05.png)


**----- Start of picture text -----**<br>
(a) (b)<br>(c) (d)<br>**----- End of picture text -----**<br>


Figure 1. Sample path of the strategy when optimizing how deep to post in the LOB and when to execute market orders. Here, _γ_ = 10, _φ_ = 0 _._ 001 and _λ_[˜] = 50 _/_ 300 s. 

Almgren–Chriss schedule. With the simulation parameters we choose, the strategy cannot improve the best bid by posting a limit order inside the spread, something that might be optimal to do instead of sending a market order. 

Again, for the same sample path, the bottom right panel showshowdeepintheLOBarebuylimitordersposted.Clearly, the further (closer) is the accumulated inventory from (to) the trigger boundary, the deeper (shallower) is the limit order posted in the LOB. 

In the bottom left panel, we show, for this same sample path, the strategy’s purchase price and theAlmgren–Chriss schedule price which is measured at midprice plus the half-spread and the liquidity taking fee, i.e. _St_ + _ϒ_ . The investor’s average acquisition price is lower than the average schedule price at the terminal date _T_ and nearly always lower for _t < T_ . It is clear that the investor’s strategy outperforms the schedule because 

she is able to use a combination of limit and market orders— recall that the investor is targeting the inventory schedule and not the schedule price itself. 

Next, in figure 2, we show how the optimal strategy performs when the target is kept fixed at N = 10, but the arrival rate of marketordersis _λ_ = _λ_[˜] _e[κ�]_ = {100 _/_ 300 _,_ 50 _/_ 300 _,_ 33 _._ 33 _/_ 300} per second—this corresponds to an acquisition target which equals on average a percentage of volume (POV) of 10, 20 and 30%, respectively. Clearly, the higher the POV, the more difficult it will be for the investor to achieve the target using limit orders. 

Panel (a) of figure 2 shows the expected acquisition price per share for different values of the running target penalty _φ_ . The line with diamonds is for POV 10%. When the target penalty _φ_ is very low, we see that the expected price is low and the standard deviation is high. As we increase the target 

_Á. Cartea and S. Jaimungal_ 

1284 


![](markdown_output/retrieve_images/retrieve.pdf-0006-02.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 2. Risk–reward profiles for various intensities: _λ_ = {100 _/_ 300 _,_ 50 _/_ 300 _,_ 33 _._ 33 _/_ 300} corresponding to a trade which equals on average 30, 20 and 10% POV. Here _γ_ = 10, and moving from right to left _φ_ = 10[−][4] _,_ 0 _._ 001 _,_ 0 _._ 002 _,_ 0 _._ 005. 

penalty, the expected price per share increases because the strategy must track more closely theAlmgren–Chriss schedule but the standard deviation decreases. The expected average price increases because the strategy relies more on buy market orders which cross the spread and pay the transaction fee, and less on limit orders which earn the investor the spread. The standard deviation decreases because there is less uncertainty about the average execution price. Note that the Almgren– Chriss price, denoted by a star in the north west corner of the figure, is the strategy with the lowest standard deviation, but the highest expected average price. Moreover, in the same panel, we see that as we increase the POV, the average execution price worsens because the strategy relies more on market orders to be able to track the acquisition target. 

Panel (b) of the figure shows the expected savings per share and its standard deviation. Here, we measure savings per share as the difference between the price per share obtained by the schedule and that of the algorithm and then divide by the starting value _S_ 0 = 100 . Thus, when the savings is positive, it means that the algorithm outperformed the target schedule. This quantity is expressed in basis points and in our case, one basis point is equivalent to one cent. 

In tables 2–4, we show what is the effect of increasing the target quantity N while simultaneously scaling the rate of arrival of market order events to obtain _λ_ = 5 N _/ T_ , so that the acquisition target’s POV is 20%. Each table shows the results for different levels of midprice activity _γ_ which represents the intensity of the arrival of the jumps of size _σ_ in the asset’s midprice process, see equation (1). In each table, we also show the volatility of the midprice at the end of the trading horizon: _�_[˜] = �2 _γ σ_[2] _T_ . 

In table 2, we show the case _γ_ = 1. We observe that as the acquisition target increases, the mean savings per share also increase and the standard deviation of the savings per share decreases. The savings per share range between 2.129 and 2.510 basis points which is more than twice the spread of 100 basis points (recall that the spread is 2 _�_ = 0 _._ 01 dollar). The increase in savings per share is due to the fact that the mean number of market orders employed by the strategy decreases as N increases, or equivalently, as we increase the acquisition target, the average number of limit orders used to meet the target increases and these orders not only earn at least the 

spread, but also do not incur the market order fee _ε_ = 0 _._ 005 dollar. 

Tables 3 and 4 show the performance of the strategy when _γ_ = 10 and _γ_ = 100, respectively. The individual results are qualitatively similar to those in table 2, that is, as the acquisition target increases, so does the mean savings per share and the standard deviation of the savings decreases. Now, if we compare across the three tables, we observe that for each level of N, the mean savings per share does not change too much when _γ_ increases, but the standard deviation of the savings does increase. For instance, when _γ_ = 1 and N = 500, the average savings per share is 2.510 basis points and the standard deviation is 0.097, whereas for _γ_ = 100 and N = 500, the average savings per share is 2.509 but the standard deviation increases to 0.540. It is interesting to see that in these two cases, the average number and standard deviation of market orders is approximately the same, so the increase in the standard deviation of the savings per share is due to the increase in the volatility of the midprice—the midprice’s mean is unaltered when increasing _γ_ , only its variance increases. 

Finally, we remark that the strategy does not depend on the parameter _γ_ , but the costs of acquiring the target inventory and the distribution of the costs do depend on _γ_ . For instance, one way to see that the optimal strategy is unaltered by the choice of _γ_ is to observe that the distribution of market orders used by the algorithm is the same in all three cases. 

Figure 3 shows the trigger boundaries for N and the intensity of the arrival of other market participants market orders _λ_ = 5 N _/T_ , as well as the Almgren–Chriss schedule—again we recall that the parameter _γ_ does not affect the strategy. We observe that as the target quantity increases, the trigger boundary is closer to the Almgren–Chriss schedule and this can be used to further understand the results discussed in the tables. When the trigger boundary is furthest away, which is N = 10, we know that it is optimal to start posting buy limit orders deep in the LOB (see bottom right of figure 1) and as time goes by, and the limit order has not been filled, the investor must cancel it and repost closer to the midprice and so on until it is filled or (upon hitting the trigger boundary) a market order is sent. So, when we compare the performance of strategies with trigger boundaries close to the target schedule to the performance of those with trigger boundaries further away 

_Optimal execution_ 

1285 

Table 2. Statistics for the Almgren–Chriss schedule cost, the strategy’s savings, and number of market orders. 

||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||_γ_ =1,|˜_�_=|~~�~~|2_σ_ 2_γ T_ =|0_._245|||||
||||||||||Quantiles||||
|||||Mean|Stdev||0.01|0.25|0.5|0.75|0.99||
||N|_λ_|AC Schedule|100.013|0.224||99.485|99.856|100.008|100.160|100.522||
||||~~# MOs~~|~~3.352~~|~~1.430~~||~~0~~|~~2~~|~~3~~|~~4~~|~~7~~||
||10|0.167|Savings (bp)|2.129|1.147||−0_._592|1.392|2.125|2.866|4.893||
||||# MOs|22.505|4.928||11|19|22|26|34||
||100|1.667|Savings (bp)|2.498|0.251||1.910|2.332|2.498|2.664|3.088||
||||# MOs|104.932|12.124||76|97|105|113|133||
||500|8.333|Savings (bp)|2.510|0.097||2.286|2.445|2.508|2.574|2.739||



Note: Here _γ_ = 1 and results shown are for various levels of target inventory with market order activity adjusted so that the investor’s POV is 20%. 

Table 3. Statistics for the Almgren–Chriss schedule cost, the strategy’s savings, and number of market orders. 

|||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||_γ_ =10,||˜_�_=|~~�~~|2_σ_ 2_γ T_ =0_._775||||||
|||||||||||Quantiles||||
|||||Mean||Stdev||0.01|0.25|0.5|0.75|0.99||
||N|_λ_|AC Schedule|100.008||0.224||99.485|99.856|100.008|100.160|100.522||
||||~~# MOs~~|~~3.359~~||~~1.416~~||~~0~~|~~2~~|~~3~~|~~4~~|~~7~~||
||10|0.167|Savings (bp)|2.093||3.349||−5_._937|−0_._078|2.081|4.214|10.111||
||||# MOs|22.521||4.962||11|19|22|26|34||
||100|1.667|Savings (bp)|2.495||0.617||1.059|2.086|2.500|2.904|3.958||
||||# MOs|104.903|11.944|||77|97|105|113|133||
||500|8.333|Savings (bp)|2.513||0.187||2.064|2.389|2.512|2.638|2.964||



Note: Here, _γ_ = 10 and results shown are for various levels of target inventory with market order activity adjusted, so that the investor’s POV is 20%. 

Table 4. Statistics for the Almgren–Chriss schedule cost, the strategy’s savings and number of market orders. 

|||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||_γ_ =100,||˜_�_=|~~�~~|2_σ_ 2_γ T_ =2_._449||||||
|||||||||||Quantiles||||
|||||Mean|Stdev|||0.01|0.25|0.5|0.75|0.99||
||N|_λ_|AC Schedule|100.010|0.707|||98.373|99.527|100.009|100.490|101.683||
||||~~# MOs~~|~~3.354~~|~~1.421~~|||~~0~~|~~2~~|~~3~~|~~4~~|~~7~~||
||10|0.167|Savings (bp)|2.227|10.325||−22_._324||−4_._449|2.223|8.933|26.648||
||||# MOs|22.498|4.934|||11|19|22|26|34||
||100|1.667|Savings (bp)|2.488|1.838||−1_._996||1.272|2.478|3.734|6.726||
||||# MOs|104.687|12.103|||77|96|105|113|134||
||500|8.333|Savings (bp)|2.509|0.540|||1.238|2.151|2.505|2.863|3.769||



Note: Here, _γ_ = 100 and results shown are for various levels of target inventory with market order activity adjusted, so that the investor’s POV is 20%. 

from the target schedule, those which are far away will deliver savings per share which are more volatile because some orders are filled when posted deep in the book and some orders are filled when closer to the midprice. 

When analysing the performance of the strategy for different values of the POV, we assume that the investor’s trades do not affect the dynamics of the midprice. As discussed above, one could incorporate the effect of market orders as in (4). A more 

_Á. Cartea and S. Jaimungal_ 

1286 


![](markdown_output/retrieve_images/retrieve.pdf-0008-02.png)


Figure 3. Trigger boundaries for various target inventories N while simultaneously scaling market order arrival rates so that _λ_ = 5 N _/T_ . realistic model, which is beyond the scope of this paper, is to model the reaction of other market participants when there is unusual one-sided market pressure in which case the midprice is pushed up. 

## _**3.2. Targeting TWAP inventory schedule**_ 

As another example, we show the results with same model parameters, but the investor targets theTWAPinventory schedule q _t_ = N _T[t]_[. Table][ 5][ shows the cost savings per share as well] as the number of executed market orders for 10 000 simulations. We observe that the average savings per share increases from 2.775 basis points when N = 10 to 3.567 basis points when N = 500, and the standard deviation of the savings decrease as the target quantity is increased. As discussed in the Almgren–Chriss examples, the source of the savings is the use of limit orders. We see that as the target schedule increases (and recall that to keep the target quantity to be 20% of the traded volume we must increase the arrival of market orders), the savings per share increase because the strategy relies on fewer market orders. Moreover, the decrease in the standard deviationofthesavingspersharecanalsobeexplainedbecause the trigger boundary of the strategy gets closer to the TWAP schedule as we increase N, as is the case for the Almgren– Chriss schedule discussed above. 

Interestingly, for the TWAP target, as N increases, the number of executed market orders significantly decreases—while in the Almgren–Chriss schedule, the number executed market orders increases (although the percentage of market orders relative to all orders decreases). The reason is because the expected number of other participants’ market orders that hit the investor’s bid is aligned with the TWAP schedule. Specifically, E[ _Mt_ ] = _λ t_ which is linear in _t_ and the investor needs to only adjust her depth to slow down the arrival rate to her posting and only execute a few market orders. 

## **4. Posting only at the touch** 

Above we made the assumption that conditioned on a market order arriving, the limit orders are filled with probability _e_[−] _[κδ]_ where _δ_ is the depth at which the trader posts. This assumption, although standard in the literature, is not realistic because for 

the majority of traded equities, market orders hardly deplete the first level of the LOB and if they do, only walk through the first and second levels of it. Therefore, to model the fill probability more realistically, we assume that the investor’s decision is one of the following: to post at the best bid, not to post or to execute a market buy order. 

As above, we assume that the investor is continuously monitoring the market and updating her decisions. When the investor posts a limit order at the best bid, she will cancel it immediately if not filled and repost if it is optimal to do so. In continuous time, this strategy does not allow the limit order to restintheLOB;therefore,everytimeanewlimitorderissentto the LOB it is more likely to arrive at the back of the queue and, conditioned on a market order arriving, there is no guarantee that the investor’s limit order will be filled. Hence, rather than modelling queue position, we assume that posting at the best biddoesnotguaranteeexecution(conditionalonamarketorder arrival). More specifically, we assume that conditioned on a market sell order arriving, the investor’s limit order is filled with probability _ρ_ . We denote the control for posts at the touch _ℓt_ ∈{0 _,_ 1} where 0 denotes no limit buy order postings and 1 denotes posting at the best bid. 

The investor’s cash process satisfies 


![](markdown_output/retrieve_images/retrieve.pdf-0008-12.png)


where _θ_ 1, _θ_ 2, _. . ._ , are i.i.d. Bernoulli random variables with success probability _ρ_ —representing the event in which upon arrival, the market order fills the trader’s posted limit order. Note that �0 _t[θ]_[1][+] _[M] u_[−][d] _[M][u]_[is also a Poisson process with inten-] sity _ρλ_ . 

The investor solves the same performance criterion as before but instead of deciding the depth posted in the book, she controls whether to post or not at the best bid. Therefore, we adopt the dynamic programming principle and the value function (3) solves the QVI: 


![](markdown_output/retrieve_images/retrieve.pdf-0008-15.png)


for _q_ = 0 _,_ 1 _, . . . ,_ N − 1 with the same terminal and boundary conditions as in (6). The ansatz _H (t, x, S, q)_ = _x_ + _q S_ + _h(t, q)_ still holds and the resulting QVI for _h_ now reads 


![](markdown_output/retrieve_images/retrieve.pdf-0008-17.png)


with the terminal and boundary conditions in (9b). The optimal strategy (in feedback form) is then to post a limit order _(ℓ_ = 1 _)_ if 


![](markdown_output/retrieve_images/retrieve.pdf-0008-19.png)


_Optimal execution_ 

1287 

Table 5. Statistics for the TWAP schedule cost, the strategy’s savings, and number of market orders. 

||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||_γ_ =10,|˜_�_=|~~�~~|2_σ_ 2_γ T_ =|0_._775|||||
||||||||||Quantiles||||
|||||Mean|Stdev||0.01|0.25|0.5|0.75|0.99||
||_N_|_λ_|TWAP Schedule|100.005|0.450||98.968|99.704|100.007|100.307|101.037||
||||~~# MOs~~|~~1.462~~|~~1.239~~||~~0~~|~~1~~|~~1~~|~~2~~|~~5~~||
||10|0.167|Savings (bp)|2.775|4.831||−8_._471|−0_._467|2.793|5.920|14.470||
||||# MOs|0.853|1.018||0|0|1|1|4||
||100|1.667|Savings (bp)|3.454|0.959||1.184|2.825|3.454|4.087|5.700||
||||# MOs|0.525|0.814||0|0|0|1|3||
||500|8.333|Savings (bp)|3.567|0.282||2.908|3.378|3.567|3.758|4.212||



Note: Here, _γ_ = 10 and results shown are for various levels of target inventory with market order activity adjusted, so that the investor’s POV is 20%. 


![](markdown_output/retrieve_images/retrieve.pdf-0009-05.png)


**----- Start of picture text -----**<br>
(a) (b)<br>(c) (d)<br>**----- End of picture text -----**<br>


Figure 4. Sample path of the strategy when optimizing when to post at the touch and execute market orders. _φ_ = 0 _._ 001 and _λ_ = 50 _/_ 300 s. 

otherwise withdraw from the passive side of the market ( _ℓ_ = 0), and execute a market order if 


![](markdown_output/retrieve_images/retrieve.pdf-0009-08.png)


## _**4.1. Simulations: targeting Almgren–Chriss**_ 

Here, we use simulations to show the performance of the optimal strategy. To make the results comparable to those obtained above when the investor’s strategy decides the depth 

at which she posts in the LOB, we use _ρ_ = _e_[−] _[κ�]_ with _κ_ = 50 and _�_ = 0 _._ 01, and perform 10 000 simulations. 

Figure 4 shows the performance of the strategy. In panel (a), the continuous line shows the asset’s midprice and the discontinuous line shows the investor’s postings at the best bid. The empty circles denote market sell orders that arrive, but do not cross with the investor’s limit orders, and solid circles denote market orders that hit the investor’s resting order at the best bid. The solid squares denote the times when the investor uses a market order to purchase one unit of the asset. 

_Á. Cartea and S. Jaimungal_ 

1288 

Table 6. Statistics for the Almgren–Chriss schedule cost, the strategy’s savings and number of market orders. 

|||||||||Quantiles||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||Mean|Stdev|0.01|0.25|0.5|0.75|0.99||
||N|_λ_|Schedule|100.008|0.224|99.485|99.856|100.008|100.160|100.522||
||10|0.167|# MOs<br>~~Savings (bp)~~|1.962<br>~~1.117~~|1.251<br>~~2.714~~|0<br>~~−5~~~~_._291~~|1<br>~~−0~~~~_._682~~|2<br>~~1.106~~|3<br>~~2.933~~|5<br>~~7.614~~||
||100|1.667|# MOs<br>Savings (bp)|10.580<br>1.328|4.340<br>0.415|2<br>0.329|7<br>1.054|10<br>1.324|13<br>1.604|21<br>2.277||
||500|8.333|# MOs<br>Savings (bp)|50.678<br>1.337|11.097<br>0.113|26<br>1.067|43<br>1.262|50<br>1.337|58<br>1.412|77<br>1.597||



Notes: Here, _γ_ = 10 and results shown are for various levels of target inventory with market order activity adjusted, so that the investor’s POV is 20%. The investor optimizes only over whether to post or not at the touch. 


![](markdown_output/retrieve_images/retrieve.pdf-0010-05.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 5. Risk–reward profiles for various intensities: _λ_ = {100 _/_ 300 _,_ 50 _/_ 300 _,_ 33 _._ 33 _/_ 300} corresponding to a trade which equals on average 30, 20 and 10% POV. Here, _γ_ = 10 and moving from right to left _φ_ = 10[−][4] _,_ 0 _._ 001 _,_ 0 _._ 002 _,_ 0 _._ 005. 

The dashed line in panel (b) shows the Almgren–Chriss schedule, the solid circles is the _behind-schedule boundary_ and, further to the right, the solid squares is the trigger boundary. Note that this is different from the strategy described above when the investor chooses the depth she posts in the LOB. Here, we have two boundaries because one signals that a limit order has to be posted in the LOB, behind-schedule boundary, and the other that a market order is required, trigger boundary. To the left of the behind-schedule boundary, the investor does not post limit orders and does not execute market orders. To the right of this boundary, the strategy starts posting limit buy orders because it is behind schedule and at every instant in time, the strategy cancels the limit order and reposts at the touch waiting for it to be filled. If the wait is too long, then the inventory level will hit the trigger boundary and the investor executes a market buy order to bring the inventory closer to the Almgren–Chriss schedule. Note that the behind-schedule boundary does not lie on top of the target schedule and it may lie either to the right or left of it depending on the value of the various parameters and the state variables such as inventory and time to end of strategy. Panel (c) shows the running average of the algorithm’s acquisition price and the running average of the Almgren–Chriss price along this path. 

Table 6 shows the performance of the strategy compared to theAlmgren–Chrissschedulewhenlimitordersareonlyposted 

atthetouch.Weobservethatasthetargetquantityincreases,the savings per share also increase (recall that the arrival of other market participants’ market orders is also increased, so that the investor’s target is always 20% of POV) and the standard deviation of the savings decrease. The average cost savings obtained by the strategy is always better than the spread, which is 1bp, and slightly lower than the sum of the spread (1bp) and the market order fee (0.5bp). 

It is interesting to compare these results to those in table 3. The only difference is that here the investor’s limit orders are always posted at the touch while in table 3, the strategy optimizes over depth of the limit orders. The results show that optimizingoverdepthincreasessavingspersharebyabout1bp. 

Figure 5 shows the performance of the strategy for different POV, 30, 20 and 10%, and target penalty parameter _φ_ = {10[−][4] _,_ 0 _._ 001 _,_ 0 _._ 002 _,_ 0 _._ 005}. We observe that for high _φ_ , the higher is the acquisition target as a fraction of the average volume in the market, the less likely is the strategy to benefit from earning the spread with limit orders. And as expected, when _φ_ is low, the expected costs are low (expected savings high) because the strategy is more patient when behind the Almgren–Chriss schedule and prefers to wait for the limit orders to be filled instead of sending market orders, but this is at the expense of higher volatility for higher POV as shown by the figure. 

_Optimal execution_ 

1289 


![](markdown_output/retrieve_images/retrieve.pdf-0011-02.png)


**----- Start of picture text -----**<br>
(a) (b)<br>(c) (d)<br>**----- End of picture text -----**<br>


Figure 6. Sample path of the strategy optimizing volume to post at the touch and execute market orders. _φ_ = 0 _._ 001 and _λ_ = 50 _/_ 300 s. 

Table 7. Statistics for the Almgren–Chriss schedule cost, the strategy’s savings, and number of market orders. 

|||||||||Quantiles||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||Mean|Stdev|0.01|0.25|0.5|0.75|0.99||
||N|_λ_|Schedule|100.008|0.224|99.485|99.856|100.008|100.160|100.522||
||10|0.167|# MOs<br>~~Savings (bp)~~|1.174<br>~~1.250~~|1.152<br>~~2.970~~|0<br>~~−5~~~~_._794~~|0<br>~~−0~~~~_._731~~|1<br>~~1.235~~|2<br>~~3.235~~|5<br>~~8.262~~||
||100|1.667|# MOs<br>Savings (bp)|0.006<br>1.490|0.127<br>0.410|0<br>0.500|0<br>1.223|0<br>1.495|0<br>1.756|0<br>2.460||
||500|8.333|# MOs<br>Savings (bp)|0.000<br>1.490|0.000<br>0.080|0<br>1.299|0<br>1.435|0<br>1.489|0<br>1.546|0<br>1.682||



Notes: Here, _γ_ = 10 and results shown are for various levels of target inventory with market order activity adjusted, so that the investor’s POV is 20%. The investor optimizes over whether to post or not (only at the touch) and optimizes over volume too. 

## **5. Posting only at the touch and optimizing volume** 

Until now, we have assumed that the investor’s limit orders are for one unit of the asset at a time. In more realistic market scenarios, trading algorithms also decide the amount of shares that are posted in the LOB as part of the optimization problem. When the investor’s objective is to acquire N shares and match or beat a target like Almgren–Chriss or TWAP, it is not immediately obvious how to choose the volume that will be posted in the LOB. Intuitively, if the acquired inventory is lagging behind the target, the strategy should either increase 

the volume of the limit order, by adding another one not to lose the position in the queue of those orders already posted, or execute a market order. 

In this section, we allow the investor to optimize over the volume posted at the touch and the control is denoted _ℓt_ ∈ {0 _,_ 1 _, . . . ,_ N − _qt_ }. Note that the maximal allowed posting equals the number of shares remaining. The investor’s cash process still satisfies (16) and she solves the same performance criterion as before, but with the new control. As such, the dynamic programming equation becomes 

_Á. Cartea and S. Jaimungal_ 

1290 


![](markdown_output/retrieve_images/retrieve.pdf-0012-02.png)


**----- Start of picture text -----**<br>
(a) (b)<br>**----- End of picture text -----**<br>


Figure 7. Risk–reward profiles for various intensities: _λ_ = {100 _/_ 300 _,_ 50 _/_ 300 _,_ 33 _._ 33 _/_ 300} corresponding to a trade which equals on average 30, 20 and 10% POV. Here, _γ_ = 10 and moving from right to left _φ_ = 10[−][4] _,_ 0 _._ 001 _,_ 0 _._ 002 _,_ 0 _._ 005. 


![](markdown_output/retrieve_images/retrieve.pdf-0012-04.png)


for _q_ = 0 _,_ 1 _, . . . ,_ N − 1 with the same terminal and boundary conditions as in (6). It is also possible to allow the investor to execute several market orders simultaneously; however, the resulting strategy will be identical to the strategy where market orders are only for one unit of the asset. 

The ansatz _H (t, x, S, q)_ = _x_ + _q S_ + _h(t, q)_ still holds and the resulting QVI for _h_ now reads 


![](markdown_output/retrieve_images/retrieve.pdf-0012-07.png)


with the terminal and boundary conditions in (9b). The optimal strategy (in feedback form) is then to post the volume which maximizes (including _ℓ_ = 0) 


![](markdown_output/retrieve_images/retrieve.pdf-0012-09.png)


or execute a market order if 


![](markdown_output/retrieve_images/retrieve.pdf-0012-11.png)


## _**5.1. Simulations: targeting Almgren–Chriss**_ 

We assume that the investor is tracking the Almgren–Chriss schedule. In this case, the optimal strategy takes the following stylistic form. At a given level of inventory, if the investor is ahead of the target inventory, then she withdraws from the market ( _ℓ_ = 0) and waits. Once the first behind-schedule boundary approaches, the investor posts a limit order for one unit at the touch and whilst it is not filled, she does not cancel it until it reaches a second behind-schedule boundary where it is optimal to increase the volume posted by one unit, waits some more before increasing once more the volume posted by one unit and so on. The investor will keep on increasing the volume 

posted at the best bid until her inventory is too far behind the target and, unless the limit orders are filled, the strategy will reach the trigger boundary and execute a market order for one unit to get closer to the target inventory level. How long does the investor wait or how many units she needs to post at the touch before executing a market order will depend on many factors including the arrival rate of other participants’ market orders, and how adamant is the investor to closely track the target. 

To analyse the performance of a strategy which also optimizes the volume that the investor posts at the touch, we run 10 000 simulations with the same model parameters as in section 4. In figure 6, we depict the performance of the strategy for one particular sample path and also show the average execution price and average Almgren–Chriss for this particular path. 

In panel (a), the continuous line shows one sample path and the discontinuous line below the sample path shows when the investor has at least one limit order posted at the best bid. Solid circles represent a fill for one unit of the asset, and stars represent a fill for two units of the asset. Squares represent the investor’s executed market orders and empty circles show market orders that arrived but were not filled by the investor’s limit order. 

The dashed line in panel (b) shows the Almgren–Chriss targetandthesquaresshowthetriggerboundarythatifreached, the investor executes a market buy order for one unit of the asset. Between theAlmgren–Chriss target and the trigger boundary, we also depict the behind-schedule boundaries—two in this case. Note that since here we can post more than one limit order, we have a behind-schedule boundary for the first limit order (given an inventory level) and another behindschedule boundary to add the second limit order, and, if the wait prolongswithnofills,insteadofhavingathirdbehind-schedule boundary to increase the volume posted by yet another unit of the asset, it is always better to send a buy market order. 

To illustrate in more detail how the strategy behaves, we discuss the inventory path shown in panel (b). For the sample path depicted in panel (a), the investor picks up her first share very quickly using a limit order and then decides not to post limit orders because the strategy is ahead of schedule. At around the two second mark, she posts a limit order and 6 s later posts 

_Optimal execution_ 

1291 

in time, the strategy sends a market order (around 14 second mark), the inventory jumps to _q_ = 3, and very quickly the two limit orders that were subsequently posted are also filled so the inventory jumps to _q_ = 5. The strategy then picks up one share with one market order, two more shares with two limit orders and reaches _q_ = 8 ahead of schedule so it does not post limit orders until around the 87 second mark. Subsequently, the inventory jumps to _q_ = 9 when a limit order is filled ahead of schedule so the strategy holds off for nearly 50 s before posting a limit order. This last limit order is filled at around the 156 second mark and the acquisition target N = 10 is completed ahead of time. 

Panel (d) in the figure shows, for the sample path in (a), the volume posted at the touch as time evolves. For this particular parameter set, we see that it is never optimal to have more than two units posted at the touch—it is better to catch up using a market order than increasing the posted volume. Panel (c) shows the running average executed price and the running average Almgren–Chriss price. 

Table 7 shows the performance of the strategy when the investor’slimitordersarealwaysatthetouchandsheisallowed to choose how many limit orders to post. The interpretation is similar to that of table 6. As expected, being able to optimize over volume increases the savings per share over and above those obtained by a strategy where only one limit order (at the touch) may be posted. Moreover, note that the savings per share range between 1.25 and 1.49 which is higher than the spread and slightly lower than the sum of the spread and the market order fee. Finally, observe that when the acquisition target is higher than 10, the strategy never employs market orders. 

Figure 7 shows the performance of the strategy for different POV, 30, 20 and 10%, and target penalty parameter _φ_ = {10[−][4] _,_ 10[−][3] _,_ 0 _._ 002 _,_ 0 _._ 005}. The interpretation is similar to that of figure 5. 

## **6. Conclusions** 

We show how an investor optimally executes a large order using both limit and market orders. We show the performance of the strategy under different scenarios available to the investor. In one, we assume that the investor can only have one resting order at any one time but she chooses the depth at which the limitordersarepostedandalsochooseswhentoexecutemarket orders. In the second scenario, the investor posts only at the touch, where only one unit is posted at any one time, and is also able to execute market orders. Finally, in the last scenario, we consider the investor posts only at the touch, without restricting the volume, and can also execute market orders. 

Weusesimulationstoshowthataninvestorwhobenchmarks her acquisition strategy against the Almgren–Chriss inventory schedule will always obtain an acquisition price better than that of the benchmark (measured at midprice plus the half-spread) because she is able to benefit from earning the spread using limit orders. The savings per share are always higher than the quoted spread and depending on the strategy adopted by the investor it can be up to two and a half times the spread. 

## **Acknowledgements** 

The authors would like to thank Robert Almgren, Frederi G. Viens and an anonymous referee for their comments and discussions of the topic. 

## **Disclosure statement** 

No potential conflict of interest was reported by the authors. 

## **Funding** 

SJ would also like to thank NSERC and GRI for partially funding this work. ÁC acknowledges the research support of the Oxford-Man Institute for Quantitative Finance. 

## **References** 

- Alfonsi, A., Fruth, A. and Schied, A., Optimal execution strategies in limit order books with general shape functions. _Quant. Finance_ , 2010, **10** (2), 143–157. 

- Almgren, R., Optimal execution with nonlinear impact functions and trading-enhanced risk. _Appl. Math. Finance_ , 2003, **10** (1), 1–18. 

- Almgren, R. and Chriss, N., Optimal execution of portfolio transactions. _J. Risk_ , 2001, **3** , 5–40. 

- Bayraktar, E. and Ludkovski, M., Optimal trade execution in illiquid markets. _Math. Finance_ , 2011, **21** (4), 681–701. 

- Bayraktar, E. and Ludkovski, M., Liquidation in limit order books with controlled intensity. _Math. Finance._ , 2014, **24** (4), 627–650. Wiley Online Library. 

- Cartea, Á., Donnelly, R. and Jaimungal, S., Algorithmic trading with model uncertainty, 2013. Available online at SSRN: http://ssrn. com/abstract=2310645 

- Cartea, Á. and Jaimungal, S., Risk metrics and fine tuning of high frequency trading strategies. _Math. Finance._ , Forthcoming 2012. 

- Cartea, Á. and Jaimungal, S., Modeling asset prices for algorithmic and high frequency trading. _Appl. Math. Finance_ , 2013, **20** (6), 512–547. 

- Cartea, Á., Jaimungal, S. and Kinzebulatov, D., Algorithmic trading with learning, December 2013.Available online at SSRN eLibrary: http://ssrn.com/abstract=2373196 

- Cartea, Á., Jaimungal, S. and Ricci, J., Buy low, sell high: A high frequency trading perspective. _SIAM J. Financ. Math._ , 2014, **5** (1), 415–444. 

- Guéant, O. and Lehalle, C.-A., General intensity shapes in optimal liquidation. _Math. Finance._ , Forthcoming 2013. 

- Guéant, O., Lehalle, C.A. and Fernandez Tapia, J., Optimal portfolio liquidation with limit orders. _SIAM J. Financ. Math._ , 2012, **3** (1), 740–764. 

- Guéant, O., Pu, J. and Royer, G.,Accelerated share repurchase: Pricing and execution strategy, 2013.Available online at arXiv: http://arxiv. org/abs/1312.5617 

- Guilbaud, F. and Pham, H., Optimal high-frequency trading in a pro rata microstructure with predictive information. _Math. Finance_ , 2013a. doi: 

- Guilbaud, F. and Pham, H., Optimal high frequency trading with limit and market orders. _Quant. Finance_ , 2013b, **13** , 79–94. 

- Huitema, R., Optimal portfolio execution using market and limit orders, 2013, September.Available online at SSRN eLibrary: http:// ssrn.com/abstract=1977553 

- Kinzebulatov, D., Jaimungal, S. and Rubisov, D., Optimal accelerated share repurchases, 2013.Available online at SSRN eLibrary: http:// ssrn.com/abstract=2360394 

Copyright of Quantitative Finance is the property of Routledge and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use. 

