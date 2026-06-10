## REPRINTED FROM 

RISK MANAGEMENT • DERIVATIVES • REGULATION 

## **Risk.net September 2022** 

## **Cutting edge** 

## **Market-making by a foreign exchange dealer** 

Cutting edge: Foreign exchange 

## Market making by a foreign exchange dealer 

Dealers make money by providing liquidity to clients but face flow uncertainty and thus price risk.They can efficiently skew their prices and wait for clients to mitigate risk (internalisation), or trade with other dealers in the open market to hedge their position and reduce their inventory (externalisation). Alexander Barzykin, Philippe Bergault and Olivier Guéant propose an optimal control framework for market making that tackles both pricing and hedging, thus answering a question well known to dealers: to hedge or not to hedge? 

ith more than US$6 trillion of trading turnover per day, the foreign exchange market is the largest financial market, far ahead **W** of that of bonds and stocks. In spite of its size and the concentration of trading in a few financial global hubs, forex remains a highly fragmented over-the-counter (OTC) market with, on one side, a dealer-to-client (D2C) segment where dealers/market makers provide liquidity to clients and, on the other, a dealer-to-dealer (D2D) or interdealer segment where dealers trade together, mainly for hedging purpose. 

Market makers in forex cash markets provide liquidity to customers by proposing prices at which they are ready to buy and sell currency pairs through electronic price streams, single-bank platforms, multi-bank platforms, etc. As a consequence of the trading flow from their clients, they have to manage risky positions. They can have two different behaviours: holding the risk until other clients come to offset it (internalisation) or hedging the risk out by trading on the D2D segment (externalisation). Externalisation allows market makers to get rid of the risk, but it usually comes at a cost, that of crossing the bid-ask spread and sometimes walking the book on platforms such as EBS (part of CME Group) or Refinitiv (depending on the currency pair). Furthermore, externalisation usually induces a market impact because trades become visible to more market participants. Internalisation allows market makers to avoid market impact, or at least reduce it, but this is of course risky for the market maker because the price might evolve adversely before the trading flow compensates the current position. The risk can be reduced by skewing prices to attract the flow in the required direction, but the flow is by no means guaranteed. In practice, most market makers both internalise and externalise, depending on the market conditions (an increase in volatility increases the propensity to externalise) and their positions (dealers usually externalise beyond a certain position limit). 

The latest Bank for International Settlements (BIS) Triennial Survey documented the growing prevalence of internalisation and the resulting decline of the D2D segment (see Schrimpf & Sushko 2019). However, the tradeoff between internalisation and externalisation has attracted little academic interest until recently. In fact, most of the models proposed in the literature on optimal OTC market making have assumed no way to hedge out the risk through the interdealer segment of the market. In the paper by Ho & Stoll (1981) and in the recent literature (see Cartea _et al_ (2015) and Guéant (2016) for an overview) on optimal market making that followed the publication of Avellaneda & Stoikov (2008), the market maker is indeed ‘only’ proposing bid and ask quotes.[1] One of the rare references to the internalisation versus 

externalisation dilemma is Butz & Oomen (2019), which discusses internalisation on the basis of queuing theory and derives typical internalisation horizons. 

In Barzykin _et al_ (2021), we proposed a model of algorithmic market making with pricing and hedging that constitutes an important and natural encounter between two problems that have attracted a lot of academic and practitioner interest in the last decade: optimal market making and optimal execution.[2] The model allows us to set an optimal pricing ladder and determine optimal hedging rate in external liquidity pools as functions of the inventory, risk aversion and market-driven parameters. In particular, we proved the existence of a pure flow internalisation area, or equivalently, an inventory threshold below which it is optimal for the dealer not to externalise. This threshold is derived from a subtle balance between uncertainty, execution costs and market impact. 

In this paper, we generalise our algorithmic market-making model further to better model the trading flow. In particular, we introduce tiers used by market makers to distinguish both the different sources of the trading flow and the natural diversity of the clients. We describe below our modelling approach to the trading flow and show how to estimate the intensity parameters. We demonstrate that tiers can be conveniently defined using clustering techniques on intensity parameters. We then present our algorithmic marketmaking model and look into the differences in the optimal strategies for different tiers. By analysing the typical risk-neutralisation time and internalisation ratio derived from the model as functions of the dealer’s risk aversion we recover figures consistent with those of Butz & Oomen (2019) and Schrimpf & Sushko (2019). Finally, we discuss the dealer’s efficient frontier and comment on the choice of the risk aversion parameter. 

## **Understanding trading flow** 

One of the central issues for a dealer is inventory management. Indeed, a dealer must, at all times, decide whether they wish to warehouse the risk while waiting for the arrival of future customer flows or if they wish to hedge part of it by trading on the D2D market. This decision obviously depends on price risk but also on customer flow. Furthermore, when the market maker decides to hold risk (internalisation), they skew prices in order to increase or decrease the flow of buying or selling customers, depending on the sign of the inventory. Understanding trading flow and customers’ sensitivity to streamed prices is therefore essential. 

1 _Some of these papers did not address OTC markets specifically but the models they proposed are more adapted to OTC markets than stock markets, which are mainly organised around all-to-all limit order books._ 

2 _For an introduction to optimal execution problems, we refer the reader to Almgren & Chriss (2001) as well as Cartea_ et al _(2015) and Guéant (2016)._ 

**risk.net** 

**1** 

Cutting edge: Foreign exchange 

In order to model customer flow as a function of streamed prices, let us introduce first a reference price process .St /t . Following the industry standard, we take the firm primary mid-price as the reference price at any point in time (EBS for our examples with EUR/USD).[3] Given a streamed pricing ladder at the bid (respectively, ask/offer) modelled by S[b] .t; z/ D St .1 � ı[b] .t; z// (respectively, S[a] .t; z/ D St .1 C ı[a] .t; z//), where z > 0 is the size of the trade,[4] we assume that buy (respectively, sell) trades[5] of size in Œz; z C dz� arrive over the infinitesimal interval Œt; t C dt� with probability �[b] .z; ı[b] .t; z// dz dt (respectively, �[a] .z; ı[a] .t; z// dz dt). In practice, dealers propose pricing ladders for a set fzk; 1 6 k 6 Kg of sizes. In what follows, K D 6 sizes are considered, corresponding to 1, 2, 5, 10, 20 and 50 million euros, respectively. As a consequence, the measures �[b][=][a] .z; ı/ dz are approximated by discrete measures[P][K] kD1[�][b] k[=][a] .ı/1zk .dz/ (where 1zk .dz/ is the Dirac measure in zk). Hereafter, the functions �[b] k[=][a] are called intensity functions or simply intensities. 

For an anonymised sample of HSBC’s forex streaming clients[6] trading EUR/USD we obtained access to tables of trades and quotes over the period from January to April 2021.[7] For the purpose of our study, quotes on the bid and ask sides can be summed up, for each size zk, by a list of couples ..ıj ; �j //j 2Jkb=a , where ıj is a streamed quote for size zk and �j is the associated duration of that quote. Trades are not all of sizes fzk; 1 6 k 6 Kg but we can associate each trade with the closest zk and the trade data can then be aggregated, for the bid and ask sides and for each size zk, by a list of quotes .ıi /i 2Ikb=a . It is easy to show that the loglikelihoods LL[b] k[=][a] associated with the bid and ask sides for size zk are (up to an additive constant): 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-03.png)


where fk[b=a;][T] .dı/ is the probability measure of bid/ask trades bucketed with size zk, fk[b=a;][Q] .dı/ is the probability measure of streamed quotes (weighted with durations) at the bid/ask for size zk and �N D[P] j 2Jk[b][=][a] �[j] is the total duration of the time window. 

Intensity functions can be interpreted in the following two-step fashion. First, there is a given flow of prospective customers who look at the prices. The probability that they trade then depends on the quotes proposed by the dealer. Therefore, inspired by logistic regression techniques, a natural functional form is: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-06.png)


3 _The notion of reference price can be obscure in the case of forex due to the significant geographical delocalisation of liquidity and last look practice (see Oomen 2017). The true market price can only be known with limited accuracy. Nevertheless, the primary venue provides a reliable measurable reference, suitable for the purpose of this analysis._ 

4 _Throughout, we shall use the term quote for_ ıb=a _although it is only a mark-up or a discount with respect to the reference price._ 

5 _We take the dealer’s viewpoint when it comes to trade sides._ 

6 _This sample is sufficiently diverse to provide realistic results, but by no means complete enough to fully represent the HSBC forex market-making franchise._ 

7 _In what follows, we focused only on the most liquid hours._ 

1 Trade (green) and streamed quote (red) frequency histograms and smoothed probability density functions (associated with f1[T][.][d][ı/][ and] f1[Q][.][d][ı/][) for a client chosen at random in our sample and trades of][ €][1M] (right axis) along with the corresponding estimated intensity function (blue, left axis) (normalised to a maximum of 1) 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-13.png)


**----- Start of picture text -----**<br>
1.0 0.40<br>Trades<br>Quotes 0.35<br>0.8<br>0.30<br>0.25<br>0.6<br>0.20<br>0.4<br>0.15<br>0.10<br>0.2<br>0.05<br>0 0<br>–0.4 –0.2 0 0.2 0.4 0.6 0.8 1.0 1.2<br>��(bp)<br>Normalised intensity Probability density<br>**----- End of picture text -----**<br>


where �[b] k[=][a] represents the flow of prospective customers and the term 1=.1 C e[˛] k[b][=][a] Cˇk[b][=][a] ı / represents the probability of trading given the quotes proposed. By using a maximum likelihood approach, we can easily estimate the parameters, ie, for each k: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-15.png)


While carrying out the above estimation procedure on individual clients, we noticed that intensities on the bid and ask sides were not significantly different. Therefore, we assumed �[b] k[.ı/][ D][ �][a] k[.ı/][ D][ �][k][.ı/][. This assumption] enabled us to achieve more precise estimations since bid and ask tables could then be concatenated and the loglikelihoods added. For the examples in this paper, we therefore fitted the functions: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-17.png)


by choosing, for each k: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-19.png)


where: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0003-21.png)


The results for z1 D €1 million are shown in figure 1 for a single client chosen at random in our sample. We do not display the scale (ie, �1) as only the shape is important. 

**risk.net** 

**2** 

Cutting edge: Foreign exchange 

2 Normalised intensity functions for the two client tiers (Tier 1 is in blue and Tier 2 in green) 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-02.png)


**----- Start of picture text -----**<br>
1.0<br>0.8<br>25<br>0.6 20<br>15<br>0.4<br>10<br>5<br>0.2<br>0<br>–4 –3 –2 –1 0 1 2<br>�1<br>0<br>–1.25 –1.00 –0.75 –0.50 –0.25 0 0.25 0.50 0.75<br>��(bp)<br>–1)<br>� (bp1<br>Normalised intensity<br>**----- End of picture text -----**<br>


Tiers are identified using a standard k-means procedure on individually fitted intensity parameters for the sample of clients considered in the paper and trades of €1M (inset) 

Figure 2 collects .˛1; ˇ1/ parameters for all clients in the sample. Two clusters are clearly visible, justifying the creation of tiers. The intensity functions corresponding to the two tiers (estimated on pooled data for each tier using the same maximum likelihood approach as above) are shown as well. We can observe significantly different price sensitivities across the two tiers. The respective parameters are (after rounding) ˛1[1][D][�][0:3][ and][ ˇ] 1[1][D][5][ per] basis point forTier 1 and ˛1[2][D �][1:9][ and][ ˇ] 1[2][D][ 15][bp][�][1][ forTier 2. This cor-] relates well with recent findings on informativeness and trading behaviour of typical forex OTC market participants, with the different pricing sensitivities of different types of clients driven by significantly different business horizons, risk management requirements and information access (Ranaldo & Somogyi 2021). 

For other sizes, the shape parameters were found to be consistent with the results for trades of €1M. .�1; : : : ; �6/ have been rounded and found proportional to .0:4; 0:25; 0:19; 0:1; 0:05; 0:01/ for both tiers. We therefore define throughout the paper the parameters ˛[1] D �0:3 and ˇ[1] D 5bp[�][1] for Tier 1 and ˛[2] D �1:9 and ˇ[2] D 15bp[�][1] for Tier 2. 

## **The market-making model for multiple tiers** 

Let us now examine the market-making model. In the general case, we denote by N the number of tiers (N D 2 in our examples). The market maker streams a pricing ladder for each tier: for Tier n 2 f1; : : : ; N g they propose a pricing ladder S[b][;n] .t; z/ D St .1�ı[b][;n] .t; z// at the bid and S[a][;n] .t; z/ D St .1Cı[a][;n] .t; z// at the ask. The associated intensities forTier n are denoted by �[b][;n] and �[a][;n] , respectively. Following the above empirical results, we assume that the functions �[b][;n] and �[a][;n] have the form:[8] 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-08.png)



![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-09.png)


The market maker can also trade on a platform to hedge their position. The execution rate of the market maker on this platform is modelled by a process .vt /t . 

We assume the dynamics of the reference price has two parts: an exogenous part with classical lognormal dynamics and an endogenous part corresponding to the permanent market impact of the market maker’s trades on the platform (ie, when they externalise). Mathematically, .St /t has the dynamics: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-12.png)


where .Wt /t is a standard Brownian motion, k represents the magnitude of the (linear) permanent impact and � is the volatility parameter. 

We denote by .qt /t the inventory process of the market maker resulting from trades with clients and trades on the platform. Mathematically, denoting by J[b][;n] .dt; dz/ and J[a][;n] .dt; dz/ the random measures modelling the times and sizes of trades with Tier n on the bid and ask sides, respectively, the dynamics of .qt /t is given by 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-15.png)


The resulting cash process .Xt /t of the market maker can be written as: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-17.png)


where the term L.vt /St accounts for the execution costs.[9] 

The market maker wants to maximise the expected mark-to-market value of their portfolio at the end of the period Œ0; T � while managing the risk associated with their inventory. Mathematically, we assume that they want to maximise: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-20.png)


by choosing ı[b][;n] , ı[a][;n] and v, where the respective importance of the expected profit and loss (P&L) and risk management components can be chosen through the coefficient C > 0. This is a standard objective function discussed in the market-making literature.[10] Market share is also often targeted by dealers, and this could be part of a more general multi-objective optimisation problem, but P&L and risk will always remain at the core. 

Applying Itô’s formula to the process .Xt C qt St /t allows us to see that this problem is equivalent to maximising: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0004-23.png)


- 9 L _is typically nonnegative, strictly convex and asymptotically superlinear._ 

- 10 _A terminal penalty can be introduced on the residual inventory at time_ T _._ 

8 _Generalisations are of course straightforward._ 

**risk.net** 

**3** 

Cutting edge: Foreign exchange 

As T is chosen small in what follows, it makes sense to approximate St by S0 in the expression above, and the problem becomes that of maximising: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-02.png)


where � D CS0 is analogous to the risk aversion parameter in most models in the market-making literature. 

We denote by � W Œ0; T � � R ! R the value function of this stochastic control problem. The Hamilton-Jacobi equation associated with it is: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-05.png)


3 Optimal bid ladder for Tier 1 (blue): �ı[b][;][1][�] .0; z/ as a function of q0� for z 2 fz1; : : : ; z6g 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-07.png)


**----- Start of picture text -----**<br>
1.00<br>Pure flow<br>internalisation 0.4<br>0.75<br>0.50<br>0.2<br>0.25 Tier 2 optimal<br>ask ladder<br>0 0<br>–0.25 Tier 1 optimal Optimal<br>bid ladder execution –0.2<br>–0.50 rate<br>–0.75<br>–0.4<br>–1.00<br>–100 –75 –50 –25 0 25 50 75 100<br>Inventory (millions of euros)<br>Bid and ask quotes (bp)<br>Execution rate (millions of euros per second)<br>**----- End of picture text -----**<br>


Optimal ask ladder for Tier 2 (green): ı[a][;][2][�] .0; z/ as a function of q0� for z 2 fz1; : : : ; z6g. Optimal external hedging rate (orange): v0[�][as a function of] q0�. Risk aversion parameter: � D 2 � 10[�][3] bp[�][1] � .M€/[�][1] 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-09.png)


with terminal condition �.T; �/ D 0, where: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-11.png)


Under mild assumptions (see Bergault & Guéant (2021) for similar results), it can be proved that, given a smooth solution to the above Hamilton-Jacobi equation, the optimal controls are given by:[11] 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-13.png)


and: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-15.png)


## **Numerical results and discussion** 

To illustrate the optimal market-making strategy, let us focus on the case of a typical top-tier bank dealer on EUR/USD. Regarding size buckets, client tiering and the shape of intensities, we used the same parameters as in the above study of the trading flow on a sample of HSBC clients. Regarding intensity amplitudes, we set .�1; : : : ; �6/ D � � .0:4; 0:25; 0:19; 0:1; 0:05; 0:01/ for both tiers, with � D 1;800 day[�][1] . This figure was chosen so that, using the optimal strategy, the trading flow is of the same order of magnitude as the estimation proposed in Butz & Oomen (2019) (see also the BIS data (Schrimpf 

11 .qs/s _is a càdlàg (right continuous with left limits) process and we write the left limit of the process_ q _at time_ t _as_ qt� D lims"t qs _._ 

& Sushko 2019)). We obtained approximately €10 billion of daily turnover (the estimation in Butz & Oomen (2019) was US$7.32M/min).[12] 

As far as the execution cost and market impact parameters are concerned, we used standard estimation techniques on a sample of HSBC execution data and chose (after rounding): � L W v 2 R 7! �v[2] C �jvj with � D 10[�][5] bp � day � .M€/[�][1] and � D 0:1bp. 

� Permanent market impact: k D 5 � 10[�][3] bp � .M€/[�][1] . 

We set the volatility to � D 50bp�day[�][1=2] and considered a time horizon T D 0:05 days (72 minutes), which ensures convergence towards stationary quotes and hedging rates at time t D 0 (see more on convergence in Barzykin _et al_ (2021)). In order to approximate the value function �, we added boundary conditions by imposing that no trade that would result in an inventory jqj > €250 million is admitted, and used a monotone implicit Euler scheme on a grid with 501 points for the inventory. 

Figure 3 summarises optimal pricing and hedging strategies for the above set of parameters and risk aversion of � D 2 � 10[�][3] bp[�][1] � .M€/[�][1] .[13] There are several interesting features worth noting. First, we observe a range of inventory around zero, where the dealer will only internalise by skewing the quotes, ie, no hedging. We call this interval the pure flow internalisation area. Since L.v/ D �v[2] C �jvj implies that: 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0005-24.png)


12 _Note that the maximum daily turnover corresponding to these parameters is approximately €31 billion. However, the dealer can only hypothetically reach this level by quoting far better prices than the mid-price and losing money._ 13 _Due to the assumption of flow symmetry, it suffices to plot only bid or ask quotes for each tier, as the other side would be a mirror image. We decided to plot_ �ı[b][;1][�] .0; z/ _as a function of_ q0� _for_ z 2 fz1; : : : ; z6g _for Tier 1 and_ ı[a][;2][�] .0; z/ _as a function of_ q0� _for_ z 2 fz1; : : : ; z6g _for Tier 2._ 

**risk.net** 

**4** 

Cutting edge: Foreign exchange 

4 Inventory threshold of the pure flow internalisation area for different levels of risk aversion (�), volatility (� ), franchise size (�), execution costs (�) and permanent market impact (k) 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0006-02.png)


**----- Start of picture text -----**<br>
�<br>�<br>50 �<br>40<br>30<br>20<br>10<br>0<br>0 200 400 600 800 1,000 1,200<br>����� [�] �<br>�<br>0 0.1 0.2 0.3 0.4 0.5<br>�<br>50<br>40<br>30<br>20<br>10<br>k<br>0<br>0 0.005 0.010 0.015<br>k<br>Inventory threshold (millions of euros)<br>Inventory threshold (millions of euros)<br>**----- End of picture text -----**<br>


The top panel scales against �=.��[2] / with the varying parameter colour coded, with others being fixed at default values 

we have H[0] .p/ D 0 () jpj 6 �. Given the expression for the optimal controls, the pure flow internalisation area corresponds to the set of inventories q verifying: 

## j@q�.0; q/ C kqj 6 � 

which contains 0 plus an interval around 0 (as soon as �.0; �/ is continuously differentiable). In terms of sensitivity to the parameters, we noticed empirically (in line with intuition) a wider pure flow internalisation area for a less risk-averse market maker with a larger franchise, exposed to higher execution costs and market impact and in a less volatile market (see figure 4). We also note that the optimal execution rate curve is almost linear with respect to inventory outside of the pure flow internalisation area. Second, the bid-ask spread is driven by the flow signature, leading to different pricing strategies for the two tiers we considered. Our estimation of the inventory-neutral topof-book bid-ask spread (ie, the difference between the ask and bid prices for a 

5 Traded volume fraction executed with Tier 1 and Tier 2 clients and externally for hedging purpose (bars:Tier 1 is in blue,Tier 2 is in green, external trading is in orange) 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0006-08.png)


**----- Start of picture text -----**<br>
1.0<br>14<br>0.8 12<br>10<br>0.6<br>8<br>0.4 6<br>4<br>0.2<br>2<br>0 0<br>� = 10 [–4] � = 10 [–3] � = 10 [–2] � = 10 [–1]<br>Volume fraction<br>Risk naturalisation time (min)<br>**----- End of picture text -----**<br>


Risk-neutralisation time (line and dots) for different values of �. Results were obtained by Monte Carlo simulation of 10[5] trajectories over a time horizon T D 10 days for a market maker following the stationary optimal strategy 

notional of €1M) for price-sensitive clients is 0.26bp, while for less sensitive clients it is 0.55bp. This compares well with an average composite[14] bid-ask spread of 0.23bp and average primary venue bid-ask spread of 0.65bp at New York open at the time of writing in early July 2021. This is particularly interesting, as no market bid-ask spread was introduced into the model. We note that the market maker’s OTC spread is mainly driven by the empirical shape of the intensity function. 

Once the optimal strategy has been computed, we can simulate the behaviour of our market maker and assess the volume share of external hedging for different levels of dealer’s risk aversion. Figure 5 shows a span of four orders of magnitude in �, illustrating the crossover from pure internalisation to significant externalisation. Note that the volume share of less pricesensitive clients (Tier 1) remains basically the same while the dealer will prefer to sacrifice price-sensitive flow (Tier 2) for the certainty of inventory management when risk aversion increases. The level of internalisation for a riskaware dealer is in line with BIS reporting around 80% internalisation in G10 currencies by top-tier banks. 

Figure 5 also illustrates the dependence of the characteristic risk-neutralisation time �R on �, where �R is defined as the integral of the inventory autocorrelation function. It appears that pure internalisation clearly comes with a significantly higher risk. It is noteworthy that the value of �R for � D 0:01 compares very well with the EUR/USD internalisation time (1.39 minutes) estimated in Butz & Oomen (2019). 

Figure 6 explores the optimal risk-reward trade-off. In order to obtain the dealer’s efficient frontier by analogy with Markowitz modern portfolio theory, we chose different values of the risk aversion parameter � and perturbed the optimal strategy by randomly shifting bid and ask quotes for both tiers and randomly choosing the width of the pure internalisation area and the slope of the hedging rate curve around their optimal values. 

14 _An aggregated order book of multiple Electronic Communication Networks was used._ 

**risk.net** 

**5** 

Cutting edge: Foreign exchange 

6 Expected P&L versus standard deviation of the P&L over time horizon T D 0.05 days of a market maker following the stationary optimal strategy with different values of the risk aversion parameter (solid line) and 20 randomly perturbed strategies for each value of y (circles) 


![](markdown_output/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022_images/risk-net-market-making-by-a-foreign-exchange-dealer-sept-2022.pdf-0007-02.png)


**----- Start of picture text -----**<br>
12<br>10<br>8<br>~<br>6 ><br>2<br>4<br>5 10 15 20 25 30<br>Risk (k$)<br>Maximum expected P&L without risk management (dashed line). Results were<br>obtained by Monte Carlo simulation of 10 [5] trajectories for several values of Y<br>ranging from 10 _ 4 to 10 _ 1.The curve has been obtained with cubic splines<br>P&L (k$)<br>**----- End of picture text -----**<br>


The resulting outcomes are almost all below the curve built using the optimal stationary pricing and hedging strategy although our objective function is not exactly a mean-variance one. Our penalty for inventory risk indeed ignores part of the variance (see the discussion on objective functions for market making in Guéant (2016)), and random perturbations could occasionally end up being above the curve,[15] but our approach appears to be a very good one from a risk-reward perspective. 

It must be noted that there is a significant difference between the efficient frontier of Markowitz modern portfolio theory and ours, in that the expected P&L is bounded from above in our case. Figure 6 shows the maximum 

15 _This may also be linked to finite sample statistics and to the use of the optimal stationary strategy rather than the time-dependent one close to time_ T _._ 

expected P&L with no risk management. The simulated optimal curve saturates at a lower value when v ! 0 because of the inventory limit we imposed to build a grid-based finite difference scheme. 

The choice of v ultimately rests with the dealer and it is clear that the optimal risk-reward curve can be useful in making the decision if we want to optimise a risk-adjusted financial performance measure such as Sharpe ratio. Forex dealers often have other objectives than those purely based on riskadjusted financial performance. For instance, they often care about market share. Although our model does not include such a criterion, simulations similar to those carried out above could help in choosing strategies that provide good results even when additional criteria are taken into account. 

## **Concluding remarks** 

We introduced and analysed numerically a model of optimal market making incorporating fundamental risk controls: pricing ladders over a distribution of sizes and client tiers as well as the rate of hedging in external markets. The model has immediate practical application to foreign exchange where the marketplace is significantly fragmented and dealers must continuously solve the dilemma of whether to internalise or externalise their flow. We described the relevant features of client flow, taking a typical EUR/USD franchise as an example and showed how tiers and pricing ladders as a function of size naturally arise from this analysis. The results obtained regarding bidask spreads, risk-neutralisation times and internalisation ratios are consistent with empirical data and publicly reported figures. = 

Alexander Barzykin is a director at HSBC GFX and commodities, specialising in algorithmic execution and market making. He is based in London. Philippe Bergault is a postdoctoral researcher in applied mathematics at École Polytechnique. Olivier Guéant is full professor of applied mathematics at Université Paris 1 Panthéon-Sorbonne and adjunct professor of quantitative finance at ENSAE - IP Paris.The results presented in this paper are part of the research carried out within the HSBC FX Research Initiative. The views expressed are those of the authors and do not necessarily reflect the views or the practices at HSBC.The authors are grateful to RichardAnthony (HSBC) and Paris Pennesi (HSBC) for helpful discussions and support throughout the project. Email: alexander.barzykin@hsbc.com, 

bergault.philippe@protonmail.com, 

olivier.gueant@univ-paris1.fr. 

## **REFERENCES** 

**Almgren R and N Chriss, 2001** _Optimal execution of portfolio transactions Journal of Risk_ 3, pages 5–40 

**Avellaneda M and S Stoikov, 2008** _High-frequency trading in a limit order book Quantitative Finance_ 8(3), pages 217–224 

**Barzykin A, P Bergault and O Guéant, 2021** _Algorithmic market making in foreign exchange cash markets with hedging and market impact_ Preprint, arXiv:2106.06974 

**Bergault P and O Guéant, 2021** _Size matters for OTC market makers: general results and dimensionality reduction techniques Mathematical Finance_ 31(1), pages 279–322 

**Butz M and R Oomen, 2019** _Internalisation by electronic FX spot dealers Quantitative Finance_ 19(1), pages 35–56 

**Cartea Á, S Jaimungal and J Penalva, 2015** _Algorithmic and High-Frequency Trading_ Cambridge University Press 

## **Guéant O, 2016** 

_The Financial Mathematics of Market Liquidity: From Optimal Execution to Market Making_ (volume 33) CRC Press 

**Ho T and HR Stoll, 1981** _Optimal dealer pricing under transactions and return uncertainty Journal of Financial economics_ 9(1), pages 47–73 

**Oomen R, 2017** _Last look_ 

_Quantitative Finance_ 17(7), pages 1,057–1,070 

## **Ranaldo A and F Somogyi, 2021** 

_Asymmetric information risk in FX markets_ 

_Journal of Financial Economics_ 140(2), pages 391–411 

**Schrimpf A and V Sushko, 2019** _FX trade execution: complex and highly fragmented_ BIS Quarterly Review, December 

**risk.net** 

**6** 

