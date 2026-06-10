# Flexible least squares for temporal data mining and statistical arbitrage 

Giovanni Montana[∗] , Kostas Triantafyllopoulos[†] , Theodoros Tsagaris[‡] 

November 26, 2024 

## **Abstract** 

flows of information updated in real-time. When multiple co-evolving data streams are observed, an important task is to determine how these streams depend on each other, accounting for dynamic dependence patterns without imposing any restrictive probabilistic law governing this dependence. In this paper we argue that flexible least squares (FLS), a penalized version of ordinary least squares that accommodates for time-varying regression coefficients, can be deployed successfully in this context. Our motivating application is statistical arbitrage, an investment strategy that exploits patterns detected in financial data streams. We demonstrate that FLS is algebraically equivalent to the well-known Kalman filter equations, and take advantage of this equivalence to gain a better understanding of FLS and suggest a more efficient algorithm. Promising experimental results obtained from a FLS-based algorithmic trading system for the S&P 500 Futures Index are reported. 

_Keywords_ ing system, statistical arbitrage 

## **1 Introduction** 

Temporal data mining is a fast-developing area concerned with processing and analyzing high-volume, high-speed data streams. A common example of data stream is a time series, a collection of univariate 

> ∗Imperial College London, Department of Mathematics 

> †University of Sheffield, Department of Probability and Statistics 

> ‡Imperial College London, Department of Mathematics, and BlueCrest Capital Management. The views presented here reflect solely the author’s opinion. 

1 

or multivariate measurements indexed by time. Furthermore, each record in a data stream may have a complex structure involving both continuous and discrete measurements collected in sequential order. There are several application areas in which temporal data mining tools are being increasingly used, including finance, sensor networking, security, disaster management, e-commerce and many others. In the financial arena, data streams are being monitored and explored for many different purposes such as algorithmic trading, smart order routing, real-time compliance, and fraud detection. At the core of all such applications lies the common need to make time-aware, instant, intelligent decisions that exploit, in one way or another, patterns detected in the data. 

In the last decade we have seen an increasing trend by investment banks, hedge funds, and proprietary trading boutiques to systematize the trading of a variety of financial instruments. These companies resort to sophisticated trading platforms based on predictive models to transact market orders that serve specific speculative investment strategies. 

Algorithmic trading, otherwise known as automated or systematic trading, refers to the use of expert systems that enter trading orders without any user intervention; these systems decide on all aspects of the order such as the timing, price, and its final quantity. They effectively implement pattern recognition methods in order to detect and exploit market inefficiencies for speculative purposes. Moreover, automated trading systems can slice a large trade automatically into several smaller trades in order to hide its impact on the market (a technique called _iceberging_ ) and lower trading costs. According to the Financial Times, the London Stock Exchange foresees that about 60% of all its orders in the year 2007 will be entered by algorithmic trading. 

Over the years, a plethora of statistical and econometric techniques have been developed to analyze financial data [De Gooijer and Hyndma, 2006]. Classical time series analysis models, such as ARIMA and GARCH, as well as many other extensions and variations, are often used to obtain insights into the mechanisms that generates the observed data and make predictions [Chatfield, 2004]. However, in some cases, conventional time series and other predictive models may not be up to the challenges that we face when developing modern algorithmic trading systems. Firstly, as the result of developments in data collection and storage technologies, these applications generate massive amounts of data streams, thus requiring more efficient computational solutions. Such streams are delivered in real time; as new data points become available at very high frequency, the trading system needs to quickly adjust to the new information and take almost instantaneous buying and selling decisions. Secondly, these applications are mostly exploratory in nature: they are intended to detect 

2 

patterns in the data that may be continuously changing and evolving over time. Under this scenario, little prior knowledge should be injected into the models; the algorithms should require minimal assumptions about the data-generating process, as well as minimal user specification and intervention. 

In this work we focus on the problem of identifying time-varying dependencies between coevolving data streams. This task can be casted into a regression problem: at any specified point in time, the system needs to quantify to what extent a particular stream depends on a possibly large number of other explanatory streams. In algorithmic trading applications, a data stream may comprise daily or intra-day prices or returns of a stock, an index or any other financial instrument. At each time point, we assume that a target stream of interest depends linearly on a number of other streams, but the coefficients of the regression models are allowed to evolve and change smoothly over time. 

The paper is organized as follows. In section 2 we review a number of common trading strategies and formulate the problem arising in _statistical arbitrage_ , thus proving some background material and motivation for the proposed methods. The flexible least squares (FLS) methodology is introduced in Section 3 as a powerful exploratory method for temporal data mining; this method fits our purposes well because it imposes no probabilistic assumptions and relies on minimal parameter specification. In Section 4 some assumptions of the FLS method are revisited, and we establish a clear connection between FLS and the well-known Kalman filter equations. This connection sheds light on the interpretation of the model, and naturally yields a modification of the original FLS that is computationally more efficient and numerically stable. Experimental results that have been obtained using the FLS-based trading system are described in Section 5. In that section, in order to deal with the large number of predictors, we complement FLS with a feature extraction procedure that performs on-line dimensionality reduction. We conclude in Section 7 with a discussion on related work and directions for further research. 

## **2 A concise review of trading strategies** 

Two popular trading strategies are _market timing_ and _trend following_ . Market timers and trend followers both attempt to profit from price movements, but they do it in different ways. A market timer forecasts the direction of an asset, going long (i.e. buying) to capture a price increase, and going short (i.e. selling) to capture a price decrease. A trend follower attempts to capture the market trends. Trends are commonly related to serial correlations in price changes; a trend is a series of asset prices 

3 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0004-00.png)


**----- Start of picture text -----**<br>
SoutWest Airlines and Exxon Mobil prices<br>70<br>0<br>60 SoutWest Airlines<br>−20 Exxon Mobil<br>50 −40<br>Jan96 Jan98 Jan00 Jan02 Jan04 Jan06<br>40<br>30<br>20<br>10<br>0<br>Jan96 Jan98 Jan00 Jan02 Jan04 Jan06<br>**----- End of picture text -----**<br>


Figure 1: Historical prices of Exxon Mobil Corporation and SouthWest Airlines for the period 1997-2007. The spread time series, reported in the inset, shows an equilibrium level between the two prices until about January 2004. 

that move persistently in one direction over a given time interval, where price changes exhibit positive serial correlation. A trend follower attempts to identify developing price patterns with this property and trade in the direction of the trend if and when this occurs. 

Although the time-varying regression models discussed in this work may be used to implement such trading strategies, we will not discuss this further. We rather focus on _statistical arbitrage_ , a class of strategies widely used by hedge funds or proprietary traders. The distinctive feature of such strategies is that profits can be made by exploiting statistical _mispricing_ of one or more assets, based on the expected value of these assets. 

The simplest special case of these strategies is perhaps _pairs trading_ (see Elliott et al. [2005], Gatev et al. [2006]). In this case, two assets are initially chosen by the trader, usually based on an analysis of historical data or other financial considerations. If the two stocks appear to be tied together in the long term by some common stochastic trend, a trader can take maximum advantage from temporary deviations from this assumed equilibrium[1] . 

A example will clarify this simple but effective strategy. Figure 1 shows the historical prices of two assets, SouthWest Airlines and Exxon Mobil; we denote the two price time series by 

> 1This strategy relies on the idea of _co-integration_ . Several applications of cointegration-based trading strategies are presented in Alexander and Dimitriu [2002] and Burgess [2003]. 

4 

yt and xt for t = 1, 2, . . . , respectively. Clearly, from 1997 till 2004, the two assets exhibited some dependence: their spread, defined as st = yt − xt (plotted in the inset figure) fluctuates around a longterm average of about −20. A trading system implementing a pairs trading strategy on these two assets would exploit temporary divergences from this market equilibrium. For instance, when the spread st is greater than some predetermined positive constant c, the system assume that the SouthWest Airlines is overpriced and would go short on SouthWest Airlines and long on Exxon Mobil, in some predetermined ratio. A profit is made when the prices revert back to their long-term average. Although a stable relationship between two assets may persist for quite some time, it may suddenly disappear or present itself in different patterns, such as periodic or trend patterns. In Figure 1, for instance, the spread shows a downward trend after January 2004, which may be captured by implementing more 

## **2.1 A statistical arbitrage strategy** 

Opportunities for pairs trading in the simple form described above are dependent upon the existence of similar pairs of assets, and thus are naturally limited. Many other variations and extensions exist that exploit temporary mispricing among securities. For instance, in _index arbitrage_ , the investor looks for temporary discrepancies between the prices of the stocks comprising an index and the price of a futures contract[2] on that index. By buying either the stocks or the futures contract and selling the other, market inefficiency can be exploited for a profit. 

In this paper we adopt a simpler strategy than index arbitrage, somewhat more related to pairs trading. The trading system we develop tries to exploit discrepancies between a _target asset_ , selected by the investor, and a paired _artificial asset_ that reproduces the target asset. This artificial asset is represented by a data stream obtained as a linear combination of a possibly large set of _explanatory_ streams assumed to be correlated with the target stream. 

The rationale behind this approach is the following: if there is a strong association between synthetic and target assets persisting over a long period of time, this association implies that both assets react to some underlying (and unobserved) systematic component of risk that explains their dynamics. Such a systematic component may include all market-related sources of risk, including financial and economic factors. The objective of this approach is to neutralize all marker-related sources of 

> 2A futures contract is an obligation to buy or sell a certain underlying instrument at a specific date and price, in the future. 

5 

risks and ultimately obtain a data stream that best represents the risk, also known as _idiosyncratic_ risk. 

Suppose that yt represents the data stream of the target asset, and �yt using a set of p explanatory and co-evolving data streams x1, . . . , xp, over the same time period. In this context, the artificial asset can also be interpreted as the _fair price_ of the target asset, given all � available information and market conditions. The difference yt − yt then represents the risk associated with the target asset only, or _mispricing_ . Given that this construction indirectly accounts for all sources of variations due to various market-related factors, the mispricing data stream is more likely to contain predictable patterns (such as the mean-reverting behavior seen in Figure 1) that could potentially be exploited for speculative purposes. For instance, in an analogy with the pairs trading approach, a possibly large mispricing (in absolute value) would flag a temporary inefficiency that will soon be corrected by the market. This construction crucially relies on accurately and dynamically estimating the artificial asset, and we discuss this problem next. 

## **3 Flexible Least Squares (FLS)** 

The standard linear regression model involves a response variable yt and p predictor variables x1, . . . , xp, which usually form a predictor column vector xt = (x1t, . . . , xpt)[′] . The model postulates that yt can be approximated well by x[′] t[β][,][where][β][is][a][p][-dimensional][vector][of][regression][parameters.][In][ordi-] nary least square (OLS) regression, estimates β[�] of the parameter vector are found as those values that minimize the cost function 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0006-04.png)


When both the response variable yt and the predictor vector xt are observations at time t of coevolving data streams, it may be possible that the linear dependence between yt and xt changes and evolves, dynamically, over time. Flexible least squares were introduced at the end of the 80’s by Tesfatsion and Kalaba [1989] as a generalization of the standard linear regression model above in order to allow for time-variant regression coefficients. Together with the usual regression assumption that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0006-06.png)


the FLS model also postulates that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0006-08.png)


6 

is a favorable aspect of the method for applications in temporal data mining, where we are usually unable to precisely specify a model for the errors; moreover, any assumed model would not hold true at all times. We have found that FLS performs well even when assumption (3) is violated, and there are large and sudden changes from βt−1 to βt, for some t. We will illustrate this point by means of an example in the next section. 

With these minimal assumptions in place, given a predictor xt, a procedure is called for the estimation of a unique path of coefficients, βt = (β1[′] t[, . . . , β] pt[′][)][′][,][for][t][=][1][,][ 2][, . . .][.][The][FLS][approach] consists of minimizing a penalized version of the OLS cost function (1), namely[3] 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0007-03.png)



![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0007-05.png)


and µ ≥ 0 is a scalar to be determined. 

In their original formulation, Kalaba and Tesfatsion [1988] propose an algorithm that minimizes this cost with respect to every βt in a sequential way. They envisage a situation where _all_ data points are stored in memory and promptly accessible, in an off-line fashion. The core of their approach is summarized in the sequel for completeness. 

The smallest cost of the estimation process at time t can be written recursively as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0007-09.png)


Furthermore, this cost is assumed to have a quadratic form 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0007-11.png)


where St−1 and st−1 have dimensions p × p and p × 1, respectively, and rt−1 is a scalar. Substituting (7) into (6) and then differentiating the cost (6) with respect to βt, conditioning on βt+1, one obtains a recursive updating equation for the time-varying regression coefficient 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0007-13.png)


> 3This cost function is called the _incompatibility cost_ in Tesfatsion and Kalaba [1989] 

7 

with 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0008-01.png)


The recursions are started with some initial S0 and s0. Now, using (8), the cost function can be written as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0008-03.png)


where 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0008-05.png)



![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0008-06.png)



![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0008-07.png)


and where Ip is the p × p identity matrix. In order to apply (8), this procedure requires all data points till time T to be available, so the coefficient vector βT should be computed first. Kalaba and Tesfatsion [1988] show that the estimate of βT can be obtained sequentially as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0008-09.png)


βT −1, . . . , β1, going backwards in time. 

The procedure relies on the of the regularization parameter µ ≥ 0; this scalar penalizes the dynamic component of the cost function (4), defined in (5), and acts as a smoothness parameter that forces the time-varying vector towards or away from the fixed-coefficient OLS solution. We prefer the alternative parameterization based on µ = (1 − δ)/δ controlled by a scalar δ varying in the unit interval. Then, with δ set very close to 0 (corresponding to very large values of µ), near total weight is given to minimizing the static part of the cost function (4). This is the smoothest solution and results in standard OLS estimates. As δ moves away from 0, greater priority is given to the dynamic component of the cost, which results in time-varying estimates. 

## **3.1 Off-line and on-line FLS: an illustration** 

As noted above, the original FLS has been introduced for situations in which all the data points are available, in batch, prior to the analysis. In contrast, we are interested in situations where each data 

8 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0009-00.png)


**----- Start of picture text -----**<br>
Dynamics of estimated regression coefficients<br>6<br>Simulated<br>5 Off−line<br>On−line<br>4<br>3<br>2<br>1<br>0<br>−1<br>−2<br>−3<br>−4<br>0 50 100 150 200 250 300<br>**----- End of picture text -----**<br>


Figure 2: line mode. 

point arrives sequentially. Each component of the p dimensional vector xt represents a new point of a data stream, and the path of regression coefficients needs to be updated at each time step so as to incorporate the most recently acquired information. Using the FLS machinery in this setting, the estimate of βt is given recursively by 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0009-03.png)


where, by substituting Mt and dt in (9) and (10), we obtain the recursions of St and st as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0009-05.png)


These recursions are initially started with some arbitrarily chosen values S0 and s0. 

Figure 2 illustrates how accurately the FLS algorithm recovers the path of the time-varying coefficients, in both off-line and on-line settings, for some artificially created data streams. The target stream yt for this example has been generated using the model 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0009-08.png)


where ǫt is uniformly distributed over the interval [−2, 2] and the explanatory stream xt evolves as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0009-10.png)


9 

with zt being white noise. The regression have been generated using a slightly complex mechanism for the purpose of illustrating the flexibility of FLS. Starting with β1 = 7, we then generate βt as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0010-01.png)


where at and bt are Gaussian random variables with standard deviations 0.1 and 0.001, respectively, and ct is uniformly distributed over [−2, 2]. We remark that this example features non-Gaussian error terms, as well as linear and non-linear behaviors in the dynamics of the regression coefficient, varying over time. 

In this example we set δ = 0.98. Although such a high value of δ encourages the regression parameters to be very dynamic, the nearly constant coefficients observed between t = 101 and t = 200, as well as the two sudden jumps at times t = 100 and t = 201, are estimated well, and especially so in the on-line setting. The non-linear dynamics observed from time t = 201 onwards is also well captured. 

## **4 An alternative look at FLS** 

In section 3, we have stressed that FLS relies on a quite general assumption concerning the evolution of the regression coefficients, as it only requires βt+1 − βt to be small at all times. Accordingly, assumption (3) does not imply or require that each vector βt is a random vector. Indeed, in the original work of Kalaba and Tesfatsion [1988], {βt} is not treated as a sequence of random variables, but rather taken as a sequence of unknown quantities to be estimated. 

We ask ourselves whether we can gain a better understanding of the FLS method after assuming that the regression coefficients are indeed random vectors, without losing the generality and flexibility of the original FLS method. As it turns out, if we are willing to make such an assumption, it is possible to establish a neat algebraic correspondence between the FLS estimation equations and the well-known Kalman filter (KF) equations. This correspondence has a number of advantages. Firstly, this connection sheds light into the meaning and interpretation of the smoothing parameter µ in the cost function (4). Secondly, once the connection with KF is established, we are able to estimate 

10 

the covariance matrix of the estimator of βt. Furthermore, we are able to devise a more version of FLS that does not require any matrix inversion. As in the original method, we restrain from imposing any specific probability distribution. The reminder of this section is dedicated to providing an alternative perspective of FLS, and deriving a clear connection between this method and the wellknown Kalman filter equations. 

## **4.1 The state-space model** 

t+1 is modeled as a noisy version of the previous coefficient at time t. First, we introduce a random vector ωt with zero mean and some covariance matrix Vω, so that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0011-03.png)


Then, along the same lines, we introduce a random variable ǫt having zero mean and some variance Vǫ, so that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0011-05.png)


Equations (14) and (15), jointly considered, result in a linear state-space model, for which it is assumed that the innovation series {ǫt} and {ωt} are mutually and individually uncorrelated, i.e. ǫi is uncorrelated of ǫj, ωi is uncorrelated of ωj, and ǫk is uncorrelated of ωℓ, for any i = j and for any k, ℓ. It is also assumed that for all t, ǫt and ωt are uncorrelated of the initial state β0. It should be emphasized again that no specific distribution assumptions for ǫt and ωt have been made. We only assume that ǫt and ωt attain some distributions, which we do not know. We only need to specify the first two moments of such distributions. In this sense, the only difference between the system specified by (14)-(15) and FLS is the assumption of randomness of βt. 

## **4.2** 

The Kalman [Kalman, 1960] is a powerful method for the estimation of βt in the above linear state-space model. In order to establish the connection between FLS and KF, we derive an alternative and self-contained proof of the KF recursions that make no assumptions on the distributions of ǫt and ωt. We have found related proofs of such recursions that do not rely on probabilistic assumptions, as in Kalman [1960] and Eubank [2006]. In comparison with these, we believe that our derivation is simpler and does not involve matrix inversions, which serves our purposes well. 

11 

We start with some definitions and notation. At time t, we denote by β[�] t the estimate of βt and by � yt+1 = E(yt+1) the one-step forecast of yt+1, where E(.) denotes expectation. The variance of yt+1 is known as the one-step forecast variance and is denoted by Qt = Var(yt+1). The one-step forecast error is defined as et = yt − E(yt). We also define the covariance matrix of βt − β[�] t as Pt and the covariance matrix of βt − β[�] t−1 as Rt and we write Cov(βt − β[�] t) = Pt and Cov(βt − β[�] t−1) = Rt. With these definitions, and assuming linearity of the system, we can see that, at time t − 1 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0012-01.png)


where Pt−1 and β[�] t−1 are assumed known. The KF gives recursive updating equations for Pt and β[�] t as functions of Pt−1 and β[�] t−1. 

Suppose we wish to obtain an estimator of βt that is linear in yt, that is β[�] t = at + Ktyt, for some at and Kt (to be specified later). Then we can write 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0012-04.png)


with et = yt − x[′] t[β][�][t][−][1][.][We][will][show][that][for][some][K][t][,][if][β][�][t][is][required][to][minimize][the][sum][of] squares 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0012-06.png)


then a[∗] t[=][β][�][t][−][1][.][To][prove][this,][write][Y][=][(][y][1][, . . . , y][T][)][′][,][X][=][(][x][′] 1[, . . . , x][′] T[)][′][,][B][=][(][β] 1[′][, . . . , β] T[′][)][′][,] E = (e1, . . . , eT )[′] and 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0012-08.png)


Then we can write (17) as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0012-10.png)


and B[�] = A[∗] + KE, where A[∗] = ((a[∗] 1[)][′][, . . . ,][ (][a][∗] T[)][′][)][′][.][We][will][show][that][A][∗][=][B][∗][,][where][B][∗][=] 

12 

(β[�] 0[′][, . . . ,][ �][β] T[′] −1[)][′][.][With the above][B][�][, the sum of squares can be written as] 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-01.png)


which is minimized when Y − XA[∗] is minimized or when E(Y − XA[∗] ) = 0, leading to A[∗] = B[∗] as required. Thus, a[∗] t[=][β][�][t][−][1][and from (16) we have] 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-03.png)


for some value of Kt Pt, we have that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-05.png)


Now, we can choose Kt that minimizes 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-07.png)


which is the same as minimizing the trace of Pt, and thus Kt is the solution of the matrix equation 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-09.png)


where ∂trace(Pt)/∂Kt denotes the partial derivative of the trace of Pt with respect to Kt. Solving the above equation we obtain Kt = Rtxt/Qt. The quantity Kt, also known as the _Kalman gain_ , is optimal in the sense that among all linear estimators β[�] t, (18) minimizes E(βt − β[�] t)[′] (βt − β[�] t). With Kt = Rtxt/Qt, from (19) the minimum covariance matrix Pt becomes 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-11.png)


The KF consists of equations (18) and (20), together with 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0013-13.png)


13 

Initial values for β[�] 0 and P0 have to be placed; usually we set β[�] 0 = 0 and P0[−][1] = 0. Note that from the recursions of Pt and Rt we have 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0014-01.png)


## **4.3 Correspondence between FLS and KF** 

Traditionally, the KF equations are derived under the assumption that ǫt and ωt follow the normal distribution, as in Jazwinski [1970]. This stronger distributional assumption allows the derivation of the likelihood function. When the normal likelihood is available, we note that its maximization is equivalent to minimizing the quantity 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0014-04.png)


with respect to β1, . . . , βT , where ξt has been [1970] for a proof). The above expression is exactly the cost function (4) with µ replaced by 1/Vω. 

This correspondence can now be taken a step further: in a more general setting, where no distributional assumptions are made, it is possible to arrive to the same result. This is achieved by rearranging equation (11) in the form of (18), which is the KF estimator of βt. First, note that from (12) we can write 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0014-07.png)


and substituting to (11) we get β[�] t = St[−][1] st. Thus we have 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0014-09.png)


14 

with 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0015-01.png)


It remains to prove that the recursion of St as in (12) communicates with the recursion of (21), for Rt+1 = St[−][1] . To end this, starting from (12) and using the matrix inversion lemma, we obtain 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0015-03.png)


which is the KF recursion (21), where Vω = µ[−][1] Ip. 

Clearly, the FLS estimator β[�] t of (11) is the same as the KF estimator β[�] t of (18). From this equivalence, and in particular from Vω = µ[−][1] Ip, it follows that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0015-06.png)


parameter µ in (4). As µ →∞, the covariance matrix of βt+1 − βt is almost zero, which means that βt+1 = βt, for all t, reducing the model to a usual regression model with constant coefficients. In the other extreme, when µ ≈ 0, the covariance matrix of βt+1 − βt has very high diagonal elements (variances) and therefore the estimated βt’s fluctuate erratically. 

An important computational consequence of the established correspondence between the FLS and the KF is apparent. For each time t, FLS requires the inversion of two matrices, namely St−1 + xtx[′] t and St−1 + µIp + xtx[′] t[.][However,][these inversions][are not necessary,][as it is clear by the KF that][β][�][t] can be computed by performing only matrix multiplications. This is particulary useful for temporal data mining data applications when T can be infinite and p very large. 

It is interesting to note how the two procedures arrive to the same solution, although they are based on quite different principles. On one hand, FLS merely solves an optimization problem, as it 

15 

minimizes the cost function C(µ) of (4). On the other hand, KF performs two steps: linear estimators are restricted to forms of (18), for any parameter vector Kt; in the second step, Kt is optimized so that it minimizes Pt, the covariance matrix of βt − β[�] t. This matrix, known as the _error matrix_ of βt, gives a measure of the uncertainty of the estimation of βt. 

The relationship between FLS and KF has important implications for both methods. For FLS, it suggests that the regression coefficients can be learned from the data in a recursive way without the need of performing matrix inversions; also, the error matrix Pt is routinely available to us. For KF, we have proved that the estimator β[�] t minimizes the cost function C(µ) = C(1/Vω) when only the mean and the variance of the innovations ǫt and ωt are specified, without assuming these errors to be normally distributed. 

## **5 An FLS-based algorithmic trading system** 

## **5.1 Data description** 

We have developed a statistical arbitrage system that trades S&P 500 stock-index futures contracts. The underlying instrument in this case is the S&P 500 Price Index, a world renowned index of 500 US equities with minimum capitalization of $4 billion each; this index is a leading market indicator, and is often used as a gauge of portfolio performance. The constituents of this index are highly traded by traditional asset management firms and proprietary desks worldwide. The data stream for the S&P 500 Futures Index covers a period of about 9 years, from 02/01/1997 to 25/10/2005. The contract prices were obtained from Bloomberg, and adjusted[4] to obtain the target data stream as showed in Figure 3. Our explanatory data streams are taken to be a subset of all constituents of the underlying S&P 500 Price Index. The constituents list was acquired from the Standard & Poor’s web site as of 1st of March 2007, whereas the constituents data streams were downloaded from Yahoo! Financial. The constituents of the S&P index are added and deleted frequently on the basis of the characteristics of the index. For our experiments, we have selected a time-invariant subset of 432 stocks, namely all the constituents whose historical data is available over the entire 1997 − 2005 period. 

The system thus monitors 433 co-evolving data streams comprising one target asset and 432 explanatory streams. All raw prices are pre-processed in several ways: data adjustments are made for 

> 4Futures contracts expire periodically; since the data for each contract lasts only a few weeks or months, continuous data adjustment is needed in order to obtain sequences of price data from sequences of contract prices. 

16 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0017-00.png)


**----- Start of picture text -----**<br>
S&P500 Futures Index<br>1800<br>1700<br>1600<br>1500<br>1400<br>1300<br>1200<br>1100<br>1000<br>900<br>800<br>Jan98 Jan00 Jan02 Jan04 Jan06<br>**----- End of picture text -----**<br>


Figure 3: S&P 500 Futures Index for the available 9-years period 

discontinuities relating to stock splits, bonus issues, events; missing observations are filled in using the most recent data points; finally, prices are transformed into log-returns. At each time t > 1, the log-return for asset i is defined as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0017-03.png)


where pit is the observed price of asset i at time t. Taking returns provides a more convenient representation of the assets, as it makes different prices directly comparable and center them around zero. We collect all explanatory assets available at time t in a column vector rt. Analogously, we denote by at the log-return of the S&P 500 Futures Index at time t. 

## **5.2 Incremental SVD for dimensionality reduction** 

When the dimensionality of the regression model is large, as in our application, the model might suffer from multicollinearity. Moreover, in real-world trading applications using high frequency data, the regression model generating trading signals need to be updated quickly as new information is acquired. A much smaller set of explanatory streams would achieve remarkable computational speedups. In order to address all these issues, we implement on-line feature extraction by reducing the dimensionality in the space of explanatory streams. 

Suppose that Rt = E(rtrt[′][)][is][the][the][unknown][population][covariance][matrix][of][the][explanatory] streams, with data available up to time t = 1, . . . , T . The algorithm proposed by Weng et al. [2003] 

17 

of the Rt matrix as new data are made available at time t + 1. In turn, this procedure allows us to extract the first few principal components of the explanatory data streams in real time, and effectively perform incremental dimensionality reduction. 

A brief outline of the procedure suggested by Weng et al. [2003] is provided in the sequel. First, note that the eigenvector gt of Rt satisfies the characteristic equation 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0018-02.png)


where λt is the corresponding eigenvalue. Let us call[�] ht the current estimate of ht using all the data up to time t (t = 1, . . . , T ). We can write the above characteristic equation in matrix form as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0018-04.png)


and then, noting that 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0018-06.png)


the estimate[�] hT is obtained by[�] hT = (h1 + · · · + hT )/T by substituting Ri by riri[′][.][This leads to] 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0018-08.png)


which is the incremental average of riri[′][g][i][, where][ r][i][r] i[′][accounts for the contribution to the estimate of] Ri at point i. 

Observing that gt = ht/||ht||, an obvious choice is to estimate gt as[�] ht−1/||[�] ht−1||; in this setting, � h0 is initialized by equating it to r1, the first direction of data spread. After plugging in this estimator in (23), we obtain 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0018-11.png)


In a on-line setting, we need a recursive expression for[�] ht. Equation (24) can be rearranged to obtain an equivalent expression that only uses[�] ht−1 and the most recent data point rt, 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0018-13.png)


18 

The weights (t − 1)/t and 1/t Full details related to the computation of the subsequent eigenvectors can be found in the contribution of Weng et al. [2003]. 

In our application, we have used data points from 02/01/1997 till 01/11/2000 as a training set to obtain stable estimates of the first few dominant eigenvectors. Therefore, data points prior to 01/11/2000 will be excluded from the experimental results. 

## **5.3 Trading rule** 

The trade unit for S&P 500 Futures Index is set by the Chicago Mercantile Exchange (CME) to $250 multiplied by the current S&P 500 Price Index, pt. Accordingly, we denote the trade unit expressed in monetary terms as Ct = 250 pt, which also gives the contract value at time t. For instance, if the current stock index price is 1400, then an investor is allowed to trade the price of the contract, i.e. $35000, and its multiples. In our application, we assume an initial investment of $100 million, denoted by w. The numbers of contracts being traded on a daily basis is given by the ratio of this initial endowment w to the price of the contract at time t, and is denoted by πt. 

We call rt the set of explanatory streams. In the experimental results of Section 6, rt will either be the 432-dimensional column vector including the entire set of constituents (the _without SVD_ case), or the reduced 3-dimensional vector of three principal components computed incrementally from the 432 streams (the _with SVD_ case) using the method of Section 5.2. 

Given target and explanatory streams, respectively at and rt, the FLS algorithm updates the current estimate of the artificial asset at time t. With the most updated estimate of the artificial asset, the current risk (i.e. the regression residual) data point is derived as 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0019-06.png)


The current position, i.e. the suggested number of contracts to hold at the end of the current day, is obtained by using 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0019-08.png)


where φ(s�t+1) is a function of the predicted risk. In our system, we deploy a simple functional (commonly known to practitioners as the _plus-minus one_ rule), given by 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0019-10.png)


19 

This rule implies that the risk data stream exhibits a mean-reverting behavior. The spread stream of Figure 4, as well as our experimental results, suggest that this assumption generally holds true. More formal statistical procedures could be used instead to test whether mean-reversion is satisfied at each time t. More realistic trading rules would also be able to detect more general patterns in the spread stream, and should take into consideration the uncertainty associated with the presence of such patterns, as well the history of previous trading decisions. 

Having obtained the number of contracts to hold, the daily order size is given by 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0020-02.png)


rounded to the nearest integer. The trading systems buys or sells daily in order to maintain the suggested number of contracts. The monetary return realized by the system at each time t is given by 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0020-04.png)


## **6 Experimental results** 

In this section we report on experimental results obtained from the simple FLS-based trading system. We have tested the system using a grid of values for the smoothing parameter δ described in Section 3, to understand the effect of its specification. Table 1 shows a number of financial performance indicators, as well as a measure of goodness of fit, with and without incremental SVD. 

_Sharpe ratio_ monetary returns and its standard deviation. It gives a measure of the mean excess return per unit of risk; values greater than 0.5 are considered very satisfactory, given that our strategy trades one single asset only. Another financial indicator reported here is the _maximum drawdown_ , the largest movement from peak to bottom of the cumulative monetary return, reported as percentage. The mean square error (MSE) has been computed both in sample and out of sample. 

Figure 5 shows gross percentage returns over the initial endowment for the constituent set, ft/w, obtained using three different systems: FLS-based system with incremental SVD (using only the largest principal component), FLS-based system without SVD, and a buy-hold strategy. Buy-hold strategies are typical of asset management firms and pension funds; the investor buys a number of contracts and holds them throughout the investment period in question. Clearly, the FLS-based systems outperforms the index and make a steady gross profit over time. The assumption of non existence 

20 

|δ|%|gain|%|loss|MDD|MDD|%|WT|%|LT|Ann.R.|Ann.R.|Ann.V.|Ann.V.||Sharpe|in-MSE∗|in-MSE∗|out-MSE∗|out-MSE∗|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0.01|0.786|0.773|−0.802|−0.817|31.809|28.529|47.886|48.732|43.659|42.813|6.559|6.728|16.393|16.393|0.400|0.410|0.159|0.019|2.328|2.311|
|0.10|0.797|0.788|−0.789|−0.799|31.569|38.770|48.194|46.887|43.351|44.658|10.610|3.118|16.384|16.397|0.648|0.190|0.153|0.003|2.270|2.329|
|0.20|0.803|0.792|−0.783|−0.795|28.616|34.777|48.501|46.810|43.044|44.735|13.175|3.739|16.377|16.396|0.804|0.228|0.149|0.001|2.243|2.333|
|0.30|0.801|0.782|−0.785|−0.805|26.645|31.541|48.578|46.964|42.967|44.581|13.080|2.115|16.377|16.398|0.799|0.129|0.147|0.000|2.229|2.335|
|0.40|0.797|0.789|−0.789|−0.798|30.201|28.432|48.117|46.887|43.428|44.658|10.287|3.365|16.385|16.397|0.628|0.205|0.144|0.000|2.221|2.336|
|0.50|0.788|0.789|−0.800|−0.798|29.608|29.157|48.424|46.887|43.121|44.658|9.253|3.356|16.388|16.397|0.565|0.205|0.142|0.000|2.214|2.336|
|0.60|0.789|0.788|−0.799|−0.800|30.457|32.752|48.655|46.656|42.890|44.889|10.381|2.139|16.385|16.398|0.634|0.130|0.140|0.000|2.210|2.337|
|0.70|0.787|0.781|−0.801|−0.806|30.457|36.569|48.886|46.272|42.660|45.273|10.819|−0.950|16.384|16.398|0.660|−0.058|0.137|0.000|2.206|2.337|
|0.80|0.789|0.782|−0.798|−0.806|33.208|34.217|48.732|46.580|42.813|44.965|10.794|0.490|16.384|16.398|0.659|0.030|0.134|0.000|2.202|2.338|
|0.90|0.791|0.786|−0.796|−0.801|36.795|32.828|48.194|46.503|43.351|45.042|9.074|1.144|16.388|16.398|0.554|0.070|0.128|0.000|2.199|2.338|
|0.99|0.800|0.787|−0.787|−0.800|32.782|33.773|47.809|46.580|43.736|44.965|9.587|1.689|16.387|16.398|0.585|0.103|0.102|0.000|2.205|2.338|



Table 1: Experimental results obtained using the statistical arbitrage system of Section 5 on 9-years of S&P 500 Future Index. Each column contains a summary statistics obtained _with_ (left-hand values) and _without_ (right-hand values) incremental SVD. The summaries are: daily percentage gain, daily percentage loss, maximum drawdown in percentage, percentage of winning trades, percentage of losing trades, annualized percentage return, annualized percentage volatility of returns, Sharpe ratio (defined as the ratio of the two previous quantities), in-sample MSE and out-sample MSE. *To be multiplied by 10e5. 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0022-00.png)


**----- Start of picture text -----**<br>
x 10−3 Spread Data Stream<br>8<br>6<br>4<br>2<br>0<br>−2<br>−4<br>−6<br>−8<br>−10<br>Jan04 Jan05 Jan06<br>**----- End of picture text -----**<br>


Figure 4: Spread stream st for a subset of the entire period. The FLS model is based on the largest principal component and δ = 0.2. 

of transactions costs, although simplistic, is not particularly restrictive, as we expect that this strategy will not be dominated by cost, given that new transactions are made only daily. Moreover, we assume that the initial endowment remains constant throughout the back-testing period, which has an economic meaning that the investor/agent consumes any capital gain, as soon as is earned. 

Finally, Figure 6 shows the estimated time-varying regression of the three cipal components, and Figure 7 shows coefficients of three constituent assets when no SVD has been applied. The coefficients associated to the first component change very little over the 9 years period, whereas the coefficients for the two other components smoothly decrease over time, with some quite abrupt jumps in the initial months of 2001. As we can see from Table 1, a fairly large value of δ = 0.2 gives optimal results and reinforces the merits of time-varying regression in this context. 

## **7 Conclusions** 

We have argued that the FLS method for regression with time-varying lends itself to a useful temporal data mining tool. We have derived a clear connection between FLS and Kalman filter equations, and have demonstrated how this link enhances interpretation of the smoothing parameter featuring in cost function that FLS minimizes, and naturally leads to a more efficient algorithm. Finally, we have shown how FLS can be employed as a building-block of an algorithmic trading system. 

22 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0023-00.png)


**----- Start of picture text -----**<br>
Cumulative Strategy Gross Percentage Returns<br>80<br>FLS−SVD<br>FLS−nSVD<br>60 Buy−hold<br>40<br>20<br>0<br>−20<br>−40<br>−60<br>Jan00 Jan01 Jan02 Jan03 Jan04 Jan05 Jan06<br>**----- End of picture text -----**<br>


Figure 5: Gross and losses for three competing systems: FLS based on SVD (using δ = 0.2), FLS based on all explanatory streams (using δ = 0.2) and a buy-and-hold strategy. 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0023-02.png)


**----- Start of picture text -----**<br>
Dynamics of Regression Coefficients of First 3 PCs<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>−0.2<br>−0.4<br>PC1<br>PC2<br>PC3<br>−0.6<br>Jan00 Jan01 Jan02 Jan03 Jan04 Jan05 Jan06<br>**----- End of picture text -----**<br>


Figure 6: Dynamycs of FLS-estimated regression associated to the three principal components, with δ = 0.2. 

23 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0024-00.png)


**----- Start of picture text -----**<br>
Dynamics of Regression Coefficients of 3 S&P500 Constituents<br>0.02<br>AonCorp.<br>0.015 PinnacleWestCapital<br>SouthernCo.<br>0.01<br>0.005<br>0<br>−0.005<br>−0.01<br>−0.015<br>−0.02<br>−0.025<br>−0.03<br>Jan00 Jan01 Jan02 Jan03 Jan04 Jan05 Jan06<br>**----- End of picture text -----**<br>


Figure 7: Dynamycs of FLS-estimated regression associated to three constituents of the index, with δ = 0.2. 


![](markdown_output/Flexible_least_squares_for_temporal_data_mining_images/Flexible_least_squares_for_temporal_data_mining.pdf-0024-02.png)


**----- Start of picture text -----**<br>
Sharpe Ratio<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>1−PC<br>2−PC<br>0 3−PC<br>nSVD<br>−0.1<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>δ<br>**----- End of picture text -----**<br>


Figure 8: Sharpe ratio as function of δ 

24 

There are several aspects of the simple system presented in Section 5 that can be further improved upon, and the remainder of this discussion points to a few general directions and related work that we intend to explore in the future. 

The problem of feature selection is an important one. In Section 5 the system relies on a set of 432 constituents of the S&P 500 Price Index under the assumption that they explain well the daily movements in the target asset. These explanatory data streams could be selected automatically, perhaps even dynamically, from a very large basket of streams, on the basis of they _similarity_ to the target asset. This line of investigation relates to the _correlation detection_ problem for data streams, a well-studied and recurrent issue in temporal data mining. For instance, Guha et al. [2003] propose an algorithm that aims at detecting linear correlation between multiple streams. At the core of their approach is a technique for approximating the SVD of a large matrix by using a (random) matrix of smaller size, at a given accuracy level; the SVD is then periodically and randomly re-computed over time, as more data points arrive. The SPIRIT system for streaming pattern detection of Papadimitriou et al. [2005] and Sun et al. [2006] incrementally finds correlations and hidden variables summarising the key trends in the entire stream collection. 

Of course, deciding on what similarity measure to adopt in order to measure how _close_ explanatory and target assets are is not an easy task, and is indeed a much debated issue (see, for instance, Gavrilov et al. [2000]). For instance, Shasha and Zhu [2004] adopt a sliding window model and the Euclidean distance as a measure of similarity among streams. Their _StatStream_ system can be used to detect pairs of financial time series with high correlation, among many available data streams. Cole et al. [2005] combine several techniques (random projections, grid structures, and others) in order to compute Pearson correlation coefficients between data streams. Other measures, such as dynamic time warping, have also been suggested [Capitani and Ciaccia, 2005]. 

Real-time feature selection can be complemented by feature extraction. In our system, for instance, we incrementally reduce the original space of 432 explanatory streams to a handful of dimensions using an on-line version of SVD. Other dynamic dimensionality reduction models, such as incremental independent component analysis [Basalyga and Rattray, 2004] or non-linear manifold learning [Law et al., 2004], as well as on-line clustering methods, would offer potentially useful alternatives. 

Our simulation results have shown gross monetary results, and we have assumed that transaction costs are negligible. Better trading rules that explicitly model the mean-reverting behavior (or other 

25 

patterns) of the spread data stream and account for transaction costs, as in Carcano et al. [2005], can be considered. The trading rule can also be modified so that trades are placed only when the spread is, in absolute value, greater than a certain threshold determined in order to maximize profits, as in Vidyamurthy [2004]. In a realistic scenario, rather than trading one asset only, the investor would build a portfolio of models; the resulting system may be optimized using measures that capture both the forecasting and financial capabilities of the system, as in Towers and Burgess [2001]. 

Finally, we point out that the FLS method can potentially be used in other settings and applications, such as predicting co-evolving data streams with missing or delayed observations, as in Yi et al. [2000], and for outlier and fraud detection, as in Adams et al. [2006]. 

## **Acknowledgements** 

We would like to thank David Hand for helpful comments on an earlier draft of the paper. 

## **References** 

- N. Adams, D.J. Hand, G. Montana, D. J. Weston, and C. W. Whitrow. Fraud detection in consumer credit. In _UK KDD Symposium (UKKDD’06)_ , 2006. 

- C. Alexander and A. Dimitriu. The cointegration alpha: enhanced index tracking and long-short equity market neutral strategies. Technical report, ISMA Center, University of Reading, 2002. 

- G. Basalyga and M. Rattray. Statistical dynamics of on-line independent component analysis. _The Journal of Machine Learning Research_ , 4:1393 – 1410, 2004. 

- A. N. Burgess. _Applied quantitative methods for trading and investment_ , chapter Using Cointegration to Hedge and Trade International Equities, pages 41–69. Wiley Finance, 2003. 

- P. Capitani and P. Ciaccia. and accurately comparing real-valued data streams. In _13th Italian National Conference on Advanced Data Base Systems (SEBD 2005)_ , 2005. 

- G. Carcano, P. Falbo, and S. Stefani. Speculative trading in mean reverting markets. _European Journal of Operational Research_ , 163:132–144, 2005. 

- _The Analysis of Time Series: An Introduction_ . Chapman and Hall, New York, 6th edition, 

- 2004. 

26 

- R. Cole, D. Shasha, and X. Zhao. Fast window correlations over uncooperative time series. In _Proceeding of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining_ , pages 743 – 749, 2005. 

- J. G. De Gooijer and R. J. Hyndma. 25 years of time series forecasting. _International Journal of Forecasting_ , 22:443–473, 2006. 

- R.J. Elliott, J. van der Hoek, and W.P. Malcolm. Pairs trading. _Quantitative Finance_ , pages 271–276, 2005. 

- R. L. Eubank. _A Kalman Filter Primer_ . Chapman and Hall, New York, 2006. 

- E. Gatev, W. N. Goetzmann, and K. G. Rouwenhorst. Pairs trading: Performance of a relative-value arbitrage rule. _Review of Financial Studies_ , 19(3):797:827, 2006. 

- M. Gavrilov, D. Anguelov, P. Indyk, and R. Motwani. Mining the stock market: which measure is best? In _Proceedings of the sixth ACM SIGKDD international conference on Knowledge discovery and data mining_ , 2000. 

- S. Guha, D. Gunopulos, and N. Koudas. Correlating synchronous and asynchronous data streams. In _Proceedings of the ninth ACM SIGKDD international conference on Knowledge discovery and data mining_ , pages 529–534, 2003. 

- A. H. Jazwinski. _Stochastic Processes and Filtering Theory_ . Academic Press, New York, 1970. 

- R. Kalaba and L. Tesfatsion. The least squares approach to time-varying linear regression. _Journal of Economic Dynamics and Control_ , 12(1):43–48, 1988. 

- R. E. Kalman. A new approach to linear and prediction problems. _Journal of Basic Engineering_ , 82:35–45, 1960. 

- M. H.C. Law, N. Zhang, and A. Jain. Nonlinear manifold learning for data stream. In _Proceedings of SIAM International Conference on Data Mining_ , 2004. 

- S. Papadimitriou, J. Sun, and C. Faloutsos. Streaming pattern discovery in multiple time-series. In _Proceedings of the 31st international conference on Very large data bases_ , pages 697 – 708, 2005. 

- D. Shasha and Y. Zhu. _High performance discovery in time series. Techniques and cases studies._ Springer, 2004. 

27 

- J. Sun, S. Papadimitriou, and C. Faloutsos. Distributed pattern discovery in multiple streams. In _Proceedings of the Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD)_ , 2006. 

- L. Tesfatsion and R. Kalaba. Time-varying linear regression _Computers & Mathematics with Applications_ , 17(8-9):1215–1245, 1989. 

- N. Towers and N. Burgess. _Developments in Forecast Combination and Portfolio Choice_ , chapter A meta-parameter approach to the construction of forecasting models for trading systems, pages 27–44. Wiley, 2001. 

- G. Vidyamurthy. _Pairs Trading_ . Wiley Finance, 2004. 

- J. Weng, Y. Zhang, and W. S. Hwang. Candid covariance-free incremental principal component analysis. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 25(8):1034–1040, 2003. 

- B. Yi, N.D. Sidiropoulos, T. Johnson, H.V. Jagadish, C. Faloutsos, and A. Biliris. Online data mining for co-evolving time sequences. In _Proceedings of the 16th International Conference on Data Engineering_ , pages 13–22, 2000. 

28 

