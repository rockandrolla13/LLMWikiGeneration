## **Applied Economics** 

**ISSN: 0003-6846 (Print) 1466-4283 (Online) Journal homepage: www.tandfonline.com/journals/raec20** 

# **Term structure estimation with liquidity-adjusted Affine Nelson Siegel model: A nonlinear state space approach applied to the Indian bond market** 

## **Sudarshan Kumar & Vineet Virmani** 

**To cite this article:** Sudarshan Kumar & Vineet Virmani (2022) Term structure estimation with liquidity-adjusted Affine Nelson Siegel model: A nonlinear state space approach applied to the Indian bond market, Applied Economics, 54:6, 648-669, DOI: 10.1080/00036846.2021.1967866 

**To link to this article:** https://doi.org/10.1080/00036846.2021.1967866 

Published online: 12 Dec 2021. 

Submit your article to this journal 

Article views: 543 

View related articles 

View Crossmark data 

Citing articles: 2 View citing articles 

Full Terms & Conditions of access and use can be found at https://www.tandfonline.com/action/journalInformation?journalCode=raec20 

APPLIED ECONOMICS 2022, VOL. 54, NO. 6, 648–669 https://doi.org/10.1080/00036846.2021.1967866 

## **Term structure estimation with liquidity-adjusted Affine Nelson Siegel model: A nonlinear state space approach applied to the Indian bond market** 

Sudarshan Kumar a and Vineet Virmanib 

aIndian Institute of Management, Calcutta, India; bIndian Institute of Management, Ahmedabad, India 

## **ABSTRACT** 

Efficient term structure estimation in emerging markets is difficult not only because of overall lack of liquidity, but also because of the concentration of liquidity in a few securities. Using the arbitrage-free Affine Nelson-Siegel model, we explicitly incorporate this phenomenon using a proxy for liquidity based on observable data in the bond pricing function and estimate the term structure for Indian Government bond markets in a nonlinear state space setting using the Unscented Kalman Filter. We find strong empirical evidence in support of the extended model with both i) a better in-sample fit to bond prices, and ii) the likelihood ratio test rejecting the restrictions assumed in the standard AFNS specification. In an alternative specification, we also model liquidity as a latent risk factor within the AFNS framework. The estimated latent liquidity factor is found to be strongly correlated with the standard market benchmarks of overall liquidity and the India VIX index. 

## **KEYWORDS** 

Term structure; Indian Government bond; Liquidity; Non-linear state-space; Unscented Kalman filter 

**JEL CLASSIFICATION** E43; G12; G17; C55; C58 

## **I. Introduction** 

There is a large literature on term structure estimation using the famous Nelson Siegel model (Nelson and Siegel 1987), with applications in both modelling the yield curve as well as for extracting inflation expectations, including many articles published in this and its sister journals (Teixeira 2007; Alper, Kazimov, and Akdemir 2007; Morales 2010; Beechey and Österholm 2014; Akhtaruzzaman and Shamsuddin 2017). The attractiveness of the Nelson Siegel model stems from its simplicity as well as the ease of interpretation of the three factors used in its specification in terms of level, slope and curvature of the yield curve. This is an important reason why the family of Nelson Siegel curves remain popular for reporting daily yield curve estimates to bond markets by central banks and regulatory institutions, including by the Indian exchanges and clearing corporations (Nath, Dalvi, and Singh 2012). 

Ever since Diebold, Rudebusch, and Boragan Aruoba (2006), the Dynamic Nelson Siegel model has taken over from the original Nelson Siegel for modelling the dynamics of the term structure in applied fixed income research (Malliaropulos and Migiakis 2018; Brzoza-Brzezina and Kotłowski 

2014; Umar, Riaz, and Zaremba 2021). Christensen, Diebold, and Rudebusch (2011) showed that the model of Diebold, Rudebusch, and Boragan Aruoba (2006) can also be cast within a class of no-arbitrage affine term structure models (Duffee 2002). This development has spurred the literature and the approach of Christensen, Diebold, and Rudebusch (2011) is today considered the state of the art, going by the name of Arbitrage-free Nelson Siegel (AFNS) framework. What makes it particularly attractive and popular for applied fixed income and monetary policy researchers (Steeley 2014) is that AFNS retains the empirical power and intuitiveness of the classical Nelson Siegel while being arbitrage-free in its dynamics. Most of the applications of AFNS, however, so far have been to the case of liquid bond markets in developed economies (Luo, Han, and Zhang 2012; Levant and Ma 2017; Audzeyeva and Fuertes 2018; Carriero, Mouabbi, and Vangelista 2018). 

Our study implements AFNS to model term structure dynamics for an emerging economy illiquid bond market, while explicitly accounting for liquidity in estimation. The difficulty in applying the AFNS approach to an emerging economy bond 

**CONTACT** Sudarshan Kumar sudarshank@iimcal.ac.in K-302, NAB, IIM Calcutta, 700104 India © 2021 Informa UK Limited, trading as Taylor & Francis Group 

APPLIED ECONOMICS 649 

market like India’s comes from infrequent trading in Government bonds (Cortazar, Schwartz, and Naranjo 2007) and concentration of liquidity in bonds of select maturities. However, most of the extant literature on modelling term structure dynamics in emerging markets clubs both liquid and illiquid bonds during estimation (Luo, Han, and Zhang 2012; Darbha 2003; Swamynathan 2005; Nath, Dalvi, and Singh 2012; Sowmya and Prasanna, 2018) despite the heterogeneity of liquid and illiquid bonds (Subramanian 2001). 

Accounting for liquidity in term structure estimation is not merely a methodological improvement, but it is also important from the point of view of empirical asset pricing. Liquidity is a welldocumented risk factor in the asset pricing literature (Acharya and Pedersen, 2005; Pastor and Stambaugh 2003) and it can impact prices in two ways. First, less liquid securities demand higher return because of the liquidity premium. Second, illiquidity can lead to higher volatility in the price of the securities, causing heteroscedasticity in the error term in the bond pricing equation used for estimation (Berenguer, Gimeno, and Nave 2014; Chundakkadan and Sasidharan 2019). Indeed, there is evidence that more liquid bonds tend to trade at higher prices (Sarig and Warga 1989; Amihud and Mendelson 1991; Elton and Green 1998). More recently, the literature has started to distinguish a bond’s ‘security-specific’ liquidity with its systematic ‘funding liquidity’ (Fontaine and Garcia 2011), with the latter found to be related to the ‘flight to liquidity’ phenomenon (Vayanos 2004; Longstaff 2004). 

This paper contributes to the stream of literature on term structure estimation in two ways. First, we apply AFNS to a large but liquidity-constrained Indian Government bond market, which makes it one of the very few applications of AFNS to emerging markets. Second, we explicitly incorporate the difference in liquidity across bonds during estimation, a first in the literature on term structure estimation in emerging markets. We incorporate both the security-specific liquidity and systematic funding liquidity dimensions in our liquidity-augmented AFNS specification. The inclusion of the systematic funding liquidity risk factor as a latent variable was pioneered by Fontaine and Garcia (2011), but they ignored the idiosyncratic security-specific liquidity 

component, which is important to capture the full extent of the liquidity premium (Nguyen and Puri 2009; Lin, Wang, and Wu 2011), especially in emerging markets with large variation in liquidity and other frictions. In a first, we incorporate both dimensions of liquidity in our specification. Further, we also extend the AFNS framework to explicitly capture liquidity induced heteroscedasticity, which allows us to assign different weights to securities with different liquidity in the likelihood estimation. We argue that both components of liquidity – systematic as well as idiosyncratic – are critical for efficient term structure estimation in emerging economy bond markets. In absence of order book data, we use functions of trading volume, age and bond duration to proxy securityspecific liquidity (Sarig and Warga 1989; Elton and Green 1998; Berenguer, Gimeno, and Nave 2014) and follow Fontaine and Garcia (2011) to capture systematic funding liquidity as a latent variable in our proposed specification. 

We find that there is a strong evidence in support of incorporating liquidity in term structure estimation. Liquidity-augmented AFNS specification not only significantly improves the in-sample fit, the likelihood ratio tests also reject the restrictions assumed in the standard AFNS specification without adjusting for liquidity. We find that the systematic funding liquidity factor is strongly correlated to the liquidity condition in the banking system and the India VIX index. We also find that our estimated systematic funding liquidity factor can capture two important exogenous liquidity shocks, including the ‘Taper Tantrum’ by the US Federal Reserve in 2013 (RBI 2014), and demonetization by the Indian central bank in November 2016 (Lahiri 2020). In addition to using a superior estimation methodology, to our knowledge, this is the first study to empirically highlight the importance of systematic funding liquidity in the banking system in determining the term structure in emerging markets. 

The rest of the paper is organized as follows. In the next section, we summarize the existing related literature and describe our research questions. Section 3 describes the data and gives a brief background on the Indian Government bond market. Section 4 details our liquidity augmented AFNS model after summarizing the related methodological literature and describes our estimation 

650 S. KUMAR AND V. VIRMANI 

methodology. Section 5 presents the results and discusses the empirical validity of the proposed models. Finally, Section 6 concludes. 

## **II. Literature review and research questions** 

If a sequence of zero coupon bonds existed across the maturity spectrum, then one would be able to extract zero coupon yields directly from their prices, and modelling the term structure of interest rates would not be needed (Bliss 1996). Despite the existence of zero coupon bond like securities for select maturities in some markets, such bonds do not exist across the maturity spectrum in any bond market, be it in a developed or in an emerging economy. Given the importance of a term structure (or a yield curve – we use the terms interchangably) for fixed income markets and monetary policy, the literature on its modelling is large, going back to at least McCulloch (1971), who first used splines to fit the term structure. Since then the literature on its estimation has evolved to modelling it today using multi-factor arbitrage-free affine class of models (Duffee 2002; Christensen, Diebold, and Rudebusch 2011; Steeley 2014). 

Given the slightly tedious nature of the mechanics of bond pricing, it is important to set the notation upfront to avoid any ambiguity. In the literature, it is standard to specify the no-arbitrage price of a default-risk free coupon bond as a sum of discounted cash flows with a security-specific error term as: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0004-05.png)


where _Pi;t_ is the price of a coupon bond _i_ at the time _t_ . The bond is due to receive _M_ future payments ( _Ci;m_ ) including coupon and principal at the time _tm_ from the time _t_ . _yt_ ð _tm_ Þ is the zero coupon yield of maturity _tm_ at time _t_ and _Di;t_ is the standard Macaulay duration. Because bonds with higher duration are riskier (so more volatile), adjustment for duration in error term is often made at the stage of estimation to correct for conditional heteroscedasticity (Berenguer, Gimeno, and Nave 2014). 

Since our study contributes to literature emanating from the Dynamic Nelson Siegel (DNS) class of models, the emphasis in our literature review is on 

developments in that stream of literature (a more general review is available in Piazzesi (2010)). DNS is an extension of the original static Nelson and Siegel (1987) framework into a dynamic setting by allowing the parameters to vary over time. In particular, the DNS model specification is: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0004-09.png)


Empirical estimates from the DNS model have been found to stable, fitting both the cross-section and time series data well, while also demonstrating superior forecasting performance compared to classical affine term structure models (Diebold 2013). This specification is now widely used to model the term structure dynamics in both developed (Nyholm and Rebonato 2008; Kaya 2014; Carriero, Mouabbi, and Vangelista 2018), and emerging markets (Luo, Han, and Zhang 2012; Audzeyeva and Fuertes 2018). 

Despite the popularity of Nelson Siegel family of models, including DNS, historically they have suffered from a theoretical issue. Filipovic (1999) showed that there does not exist any non-trivial arbitrage-free interest rates model that can generate the Nelson Siegel functional form. While the empirical success of the Nelson Siegel and DNS models in fitting the observed yield curve has made their use popular in the literature, this technical inconsistency of not being arbitrage-free had always been a sore point and made its use awkward (Piazzesi 2010; Coroneo, Nyholm, and VidovaKoleva 2011). 

The next development in the literature was showing that one could describe a dynamic multifactor model for zero coupon yields which was arbitrage-free (Duffie and Kan 1996). Those models have come to be known as affine term structure models (ATSM). We briefly describe the model set up later in Section 4, but this was an important step forward in addressing the theoretical inconsistency referred to earlier. Notwithstanding their theoretical attractiveness, the original ATSM of Duffie and Kan (1996) suffered poorly in terms of empirical performance (Duffee 2002). While the multi-factor variants of ATSM afforded more flexibility, they 

APPLIED ECONOMICS 651 

suffered from problems of over-fitting and multiple maxima at the stage of estimation, and difficulty in interpretation of parameters (Bolder 2001). 

In a sequence of papers, Jens Christensen and others (Christensen, Diebold, and Rudebusch 2009; Christensen, Lopez, and Rudebusch 2010; Christensen, Diebold, and Rudebusch 2011; Christensen and Rudebusch 2012) showed that one could combine the arbitrage-free structure of ATSM and _get_ the empirical performance of DNS, and they have come to be called as the arbitragefree Nelson-Siegel (AFNS) class of models. AFNS provides the empirical tractability of the DNS while retaining the theoretical appeal of ATSM. Christensen, Diebold, and Rudebusch (2011) has demonstrated that AFNS has a better forecasting performance compared to both DNS and ATSM. 

In related literature, Christensen and Rudebusch (2014) extend the AFNS framework to model interest rates near zero lower bond. Hong, Niu, and Zeng (2019) uses the AFNS framework to analyse the interaction between exchange rate and Chinese government bond yields. Andreasen, Christensen, and Rudebusch (2019) modify the AFNS framework to handle ‘big data’ using a one-step estimation approach. Other studies have explored the interaction between macroeconomic variables and yield curve using AFNS framework (Christensen, Lopez, and Rudebusch 2010, 2014). 

Other than Fontaine and Garcia (2011), however, none of the studies have incorporated the difference in liquidity across bonds during estimation, despite prior research showing that liquid securities demand higher return because of the liquidity premium, and illiquidity can lead to higher volatility in bond prices. Liquidity is known to have both ‘securityspecific’ and ‘market wide’ dimensions (Acharya and Pedersen, 2005; Pastor and Stambaugh 2003). More liquid bonds tend to trade at higher prices (Amihud and Mendelson 1991; Sarig and Warga 1989; Elton and Green 1998), and there is now evidence of a known market-wide ‘flight to liquidity’ phenomenon (Vayanos 2004; Longstaff 2004), driven by a systematic funding liquidity factor (Fontaine and Garcia 2011). 

The findings of the literature on the importance of security specific liquidity and funding liquidity suggest that incorporating liquidity within AFNS 

should be important. This improvement is even more critical in the emerging market context, where liquid bonds are not available across the maturity spectrum. 

Therefore our first research question asks whether incorporating the liquidity risk factor within AFNS provides better and theoretically consistent term structure estimates. In the process, we also address the sub-question of best proxies to use for liquidity in absence of order book data. To our knowledge, none of the studies so far have incorporated security-specific and systematic funding liquidity factors together in term structure estimation in the context of emerging economy bond markets. 

Having extracted estimates for security-specific liquidity and systematic funding liquidity factor, our second research question is whether the estimated systematic funding liquidity factor can explain exogenously observed phenomena of change in liquidity in the Indian banking system. We explore this in the context of the ‘taper tantrum’ by the US Federal Reserve (RBI 2014) and demonetization by the Indian central bank, which led to a sudden withdrawal of certain high denomination notes from circulation (Lahiri 2020). 

Addressing both our research questions requires estimating the term structure efficiently in the first place. Following Andreasen, Christensen, and Rudebusch (2019), we estimate the parameters of our AFNS specification directly from bond prices in a nonlinear state space setting. This one-step approach, albeit computationally intensive, provides a better fit to the underlying coupon bonds and provides richer bond price information while capturing liquidity heterogeneity (Duffee 2011; Fontaine and Garcia 2011). We rely on the Unscented Kalman filter for estimation (Van Der Merwe and Wan 2001; Julier and Uhlmann 1997), a technique better suited to fitting nonlinear state space models (Christoffersen et al. 2014; Chen, Zhou, and Li 2016). 

## **III. Background and data** 

In the last three decades the Reserve Bank of India (RBI), the Indian central bank, has taken a number of reform measures to improve monetary policy transmission by gradually shifting to auctionbased market borrowing, reducing statutory 

652 S. KUMAR AND V. VIRMANI 

reserve requirements and introducing an anonymous electronic order matching trading system called Negotiated Dealing Order Matching System (NDS-OM). While this has helped improve liquidity in the bond market to an extent (Fleming, Saggar, and Sareen 2016), as Figure 1 shows, it remains concentrated in a few maturity segments with infrequent trading in many securities. 

Table 1 summarizes the distribution of the trading observations used in the study according to the time-to-maturity of the bond and the year of the observation date. The number of observations increases with time (from the total of 3791 observations in 2010 to 10300 observations in 2017). While the ten-year maturity segment has the maximum activity over the years, liquidity is concentrated with many securities traded on less than 20% of the days in a year. 

In April 2001, the Clearing Corporation of India Limited (CCIL) was set up to provide clearing and settlement for the Government securities and foreign exchange markets. After February 2002, all trades in the Government securities are mandated to route through CCIL. We obtain our daily price and volume data from CCIL, with our sample covering the period from September 2009 to December 2017, comprising 82149 observations. Following Gürkaynak, Sack, and Wright (2007), we exclude bills and bonds with less than three-month maturity from the sample. We also drop observations which have more than one basis point difference between the reported yield to maturity (YTM) and the YTM implied from the price. Our final dataset has a total of 52358 observations spanning over 1997 trading dates. 

**Figure 1.** Histogram of the number of days security traded: This represents the histogram of the number of days securities were traded in the period May 2017- May 2018. Data is taken from June 2018 article of CCIL monthly newsletter Rakshitra. 

**Table 1.** Number of observations across maturity and year: This table represents the distribution of the trading observations used in the study according to the ‘time to maturity’ of the bond and the year of the observation date. 

|Maturity|2009|2010|2011|2012|2013|2014|2015|2016|2017|Total|
|---|---|---|---|---|---|---|---|---|---|---|
|< 1Y||71|158|52|140|170|214|409|233|1447|
|1Y-2Y|145|328|110|102|239|248|381|519|532|2604|
|2Y-5Y|375|954|543|707|1047|600|1330|2115|2081|9752|
|5Y-7Y|222|635|590|559|632|809|1086|1210|1524|7267|
|7Y-10Y|240|592|368|887|1203|995|1586|1883|2042|9796|
|10Y-12Y|125|363|515|208|253|363|708|932|624|4091|
|12Y-15Y|55|106|36|507|746|754|795|1016|1104|5119|
|15Y-20Y|114|312|338|577|689|662|997|1281|1037|6007|
|20Y-25Y|111|273|85|161|181|78|190|248|199|1526|
|25Y-30Y|18|152|201|311|462|566|977|960|713|4360|
|30Y-50Y||5|6|1|6|5|17|138|211|389|
|Total|1405|3791|2950|4072|5598|5250|8281|10711|10300|52358|



APPLIED ECONOMICS 653 

While the age of the security is also a parameter of interest for liquidity, this information is not provided by CCIL. Given its importance for studying liquidity in our study, we use the security ISIN to aggregate the information issuance date by capturing information from a combination of official sources, including RBI (https://rbi.org.in/Scripts/bs_viewcontent. aspx?Id=1956), the National Stock Exchange (https://www.nseindia.com/products/content/ debt/wdm/archieve_debt.htm) and the Reuters Datastream database. 

As we detail later in Section 4, we define systematic funding liquidity as an additional latent factor, and extract it using a state space framework. To explore macroeconomic interpretation of our extracted funding liquidity factor, we also require data on various measures of market liquidity. For this, we consider money market rates, including the overnight call rate (unsecured inter-bank rate) ( _Call_ ), repo and reverse repo rates set by RBI, and the Collateralized Borrowing and Lending Obligation ( _CBLO_ ) rate, which is the collateralized version of _Call_ . For liquidity injection by the central bank, we use RBI-reported statistics on liquidity operation ( _Net injection RBI_ ), and for secondary market activity, we use the log of the daily trading volume in the Government bond market ( logð _Trading vol_ Þ). The data on all these variables are sourced from RBI’s website and CCIL. 

Finally, to proxy overall risk in the financial system, we use the India VIX index available from the website of National Stock Exchange. India VIX is licenced by the Chicago Board of Exchange (CBOE) following the same methodology as used by CBOE for computing VIX based on the S&P 500 Index. India VIX is based on the Nifty index 

options prices.[1 ] Although a measure like VIX is based on options in equity markets, it is widely used as a measure of uncertainty and is shown to influence the bond yields as well (Adrian, Crump, and Vogt 2019). 

The summary statistics on all these variables are provided in Table 2. 

## **IV. Empirical framework and estimation methodology** 

In the AFNS framework of Christensen, Diebold, and Rudebusch (2011), zero coupon bond yields match the DNS form (see Equation 2) with an additional yield-adjustment term ( _At_ ð _τ_ Þ _=τ_ ): 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0007-08.png)


The presence of a yield-adjustment term ( _At_ ð _τ_ Þ _=τ_ ) is the key difference between the DNS and the AFNS models, and the necessary ingredient for making the AFNS model arbitrage-free. In this study, we use the parsimonious independent factor specification of the AFNS, which has a better forecasting performance than the correlated factor specification (Christensen, Diebold, and Rudebusch 2011). 

Given the relationship of AFNS with ATSM and to set the notation for estimation, we briefly describe the canonical form of ATSM used by Duffie and Kan (1996) (details in the original paper). In a typical _N_ factor ATSM, under filtered probability space ( _Ω_ , F , F _t_ ) state variable _Xt_ defined on a set _M_ � _R[N ]_ follows a Markov process under the risk-neutral measure _Q_ : 

**Table 2.** Correlates of the market liquidity: Summary statistics. 

|Statistic|N|Mean|St. Dev.|Min|Pctl(25)|Pctl(75)|Max|
|---|---|---|---|---|---|---|---|
|_Call_�_RRepo_|1,949|0.889|0.666|�1.600|0.540|1.100|4.280|
|_Call_�_CBLO_|1,949|0.102|0.416|�2.950|�0.070|0.220|4.200|
|_Net injection RBI_|1,210|0.128|0.642|�2.909|�0.168|0.507|3.476|
|logð_Trading vol_Þ|1,997|10.054|0.770|7.734|9.469|10.615|12.198|
|_VIX_|1,972|18.922|5.199|10.447|15.048|21.953|37.705|
|_Bloomberg liquidity_|1,659|0.279|1.460|�5.463|0.143|1.145|2.626|



> 1See https://www.cboe.com/tradable_products/vix/ for methodology of computing VIX and https://www1.nseindia.com/content/indices/India_VIX_Fact_ Sheet.pdf for more about India VIX 

654 S. KUMAR AND V. VIRMANI 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-01.png)


as well as under physical measure _P_ : 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-03.png)


where _dW[Q ]_ and _dW[P ]_ are _N_ dimensional standard Brownian motion, _θ[Q]_ 2 _R[N ]_ and _θ[P]_ 2 _R[N ]_ are unconditional mean vector, and _K[Q]_ 2 _R[N]_[�] _[N ]_ and _K[P]_ 2 _R[N]_[�] _[N ]_ are drift coefficient matrix in risk neutral measure ( _Q_ ) and physical measure ( _P_ ) respectively. � 2 _R[N]_[�] _[N]_ , and _D_ : _M_ ! _R[N]_[�] _[N ]_ is a diagonal matrix with its elements as: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-05.png)


where _γ[i]_ 2 _R_ and _δi_ 2 _R[N]_ . 

The model of Christensen, Diebold, and Rudebusch (2011) builds on a 3-factor ATSM, with the instantaneous risk-free rate defined as a combination of first two elements of the vector of state variables: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-08.png)


Given the boundary conditions, _B_[1] the _t_ þ _τ_[ð][0][Þ ¼] _[ B]_[2] _t_ þ _τ_[ð][0][Þ ¼] _[ B]_[3] _t_ þ _τ_[ð][0][Þ ¼] _[ A][t]_[þ] _[τ]_[ð][0][Þ ¼][ 0, ] solution to this system of ODEs is given by: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-10.png)



![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-11.png)



![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-12.png)


Under the risk-neutral measure, the state vector _Xt_ ¼ ð _Xt_[1] _[;][ X] t_[2] _[;][ X] t_[3][Þ][satisfies the stochastic differen-] tial equation of the form: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-14.png)


The above AFNS specification can be approximated as a nonlinear state space model for estimation of the parameters: 

with additional restrictions imposed on _K[Q]_ . This results in zero coupon bond prices as exponential functions of the state variables: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0008-17.png)


Given the dynamics of state variables in AFNS, _At_ ð _τ_ Þ and the vector _Bt_ ð _τ_ Þ are the solution of the following ordinary differential equations (ODEs): 

APPLIED ECONOMICS 655 

bond measurement error and _η_[�] _t_[is a 3-dimensional ] vector of state error, with their joint distribution given by: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0009-02.png)


## _**Liquidity-adjusted extended AFNS specification**_ 

One of the contributions of this study is to explicitly incorporate liquidity in the bond pricing function within the AFNS framework and estimate the augmented model in a nonlinear state space setting. The modified pricing equation adjusting for liquidity in the bond pricing equation is expressed as: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0009-05.png)


where _hi;t_ captures the liquidity premium and _h[v] i;t_ incorporates the liquidity-induced heteroscedasticity in the model. _μ_ 2 _R_[3 ] is the vector of unconditional mean of the state vector _Xt_ , _Φ_ captures 3 � 3 autoregression parameters. We impose the covariance matrix _Ω_ of the state error to be a diagonal 3 � 3 matrix. Given that we are capturing heteroscedasticity explicitly in our specification, the error terms 2 _t_ and _ηt_ are effectively mean 0 and variance 1. Specifically: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0009-07.png)


Many cross-sectional studies have captured security-specific liquidity by documenting the influence of variables such as bid-ask spread, trading volume (Subramanian 2001; Dutta, Basu, and Vaidyanathan 2005; Amihud and Mendelson 1991; Elton and Green 1998) and other security characteristics such as age (Sarig and Warga 1989) and duration (Berenguer, Gimeno, and Nave 2014) on the bond prices, and as mentioned earlier, studies such as Pastor and Stambaugh (2003) and Acharya and Pedersen (2005) have explored the systematic component of liquidity, where covrariance of the asset returns with the market liquidity influences 

expected return. However, none of the studies in the two strands of these literature have considered both the security-specific and systematic liquidity dimensions together in the context of term structure estimation, and as shown by Nguyen and Puri (2009) and Lin, Wang, and Wu (2011) both dimensions are important to capture the full extent of the liquidity premium. 

We incorporate both security specific liquidity as well as systematic funding liquidity factors in our model, and to test its statistical significance, we incorporate these factors one at a time as well as in combination. In particular, it is the functional form of _hi;t_ and _h[v] i;t_[which determines how liquidity ] related adjustments are incorporated within different specifications. All together, we consider four different cases which we describe below. 

## _**Base case: no liquidity-adjustment model**_ 

We first estimate the base AFNS specification without adjusting for security-specific liquidity premium or incorporating systematic funding liquidty, referred to as the no-liquidity or the _NL_ model hereafter. 

The importance of incorporating adjustment for liquidity is evident from the estimated price error (Observed Price – Model Price) from the _NL_ model in Figure 3. The estimated price error of the _NL_ model highlights the presence of liquidity induced heteroscedasticity. Positively sloped linear fit between monthly trading volume and price error suggests that highly traded securities demand extra price premium. 

Next, we use regression on the price error of the _NL_ model to identify the determinants of liquidity premium in terms of proxies of trading volume, age and duration. Our reasons for including these come from theory as well as the literature. In the absence of the order book data, trading volume is a popular and well-documented proxy for liquidity. Elton and Green (1998) argue that in markets with sparse liquidity, trading volume is a more robust measure of liquidity and measures such as bid-ask spread and market impact cost might not be very reliable. The age of security is another important determinant of liquidity with freshly issued securities demanding on-the-run premium (Sarig and Warga 1989). Berenguer, Gimeno, and Nave (2014) finds that uniform tick movement (minimum price movement) for the bonds across maturity has 

656 S. KUMAR AND V. VIRMANI 

**Table 3.** Regression results: price error vs. liquidity: This table provides regression results of price-error estimated from the _NL_ on the various specifications of the liquidity. log (volume), Liq (as defined in the Equation 18) is used as an explanatory variable along with the duration, _exp_ ð� _age_ Þ and their interaction terms. 

||_Price-error_|
|---|---|
||(1)<br>(2)<br>(3)<br>(4)|
|logð_volume_Þ<br>_LIQ_<br>_duration_<br>expð�_age_Þ<br>_duration_:expð�_age_Þ<br>Constant|0.052���<br>0.058���<br>(0.001)<br>(0.001)<br>1.325���<br>1.482���<br>(0.017)<br>(0.018)<br>�0.048���<br>�0.064���<br>�0.042���<br>�0.065���<br>(0.001)<br>(0.001)<br>(0.001)<br>(0.001)<br>1.075���<br>0.544���<br>0.845���<br>0.047�<br>(0.011)<br>(0.024)<br>(0.011)<br>(0.024)<br>0.100���<br>0.147���<br>(0.004)<br>(0.004)<br>0.191���<br>0.280���<br>�0.071���<br>0.018���<br>(0.007)<br>(0.008)<br>(0.005)<br>(0.005)|
|Observations<br>R2<br>Adjusted R2<br>Res Std. Error<br>F Statistic<br>df<br>AIC<br>BIC|52,358<br>52,358<br>52,358<br>52,358<br>0.270<br>0.278<br>0.325<br>0.343<br>0.269<br>0.278<br>0.325<br>0.343<br>0.557<br>0.553<br>0.535<br>0.528<br>6,439.432���<br>5,035.867���<br>8,397.156���<br>6,820.039���<br>3; 52,354<br>4; 52,353<br>3; 52,354<br>4; 52,353<br>87,238.25<br>86,640.61<br>83,114.52<br>81,724.57<br>87,282.58<br>86,693.81<br>83,158.85<br>81,777.77|
|_Note:_|�p_<_0.1;��p_<_0.05;���p_<_0.01|



a non-uniform influence on the yield movement, so for a tick-sized movement in the bond price, yield movements are inversely related to the bond’s duration. On the other hand, longer duration bonds also warrant additional premium, commonly referred to as the term premium, so if term premium dominates, the impact of duration would be positive. 

## _**First adjustment using observable proxies for liquidity, age and duration**_ 

Our first proxy for liquidity is based on Dutta, Basu, and Vaidyanathan (2005) and Subramanian (2001), who consider an exponential function of the trading volume as a measure of the liquidity, referred to as _LIQi;t_ hereafter, and represented in the Equation (18): 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0010-06.png)


Here, _volumei;t_ is the monthly trading volume of the security _i_ in the month preceding time _t_ , while _volume[max] t_ is the maximum monthly trading volume among all the traded securities. Choice of this exponential function ensures concave relationship 

between the liquidity and trading volume, i.e. the difference between the liquidity premium of the most traded securities and other highly traded securities would be small, and premium would increase at an increasing rate as liquidity decreases (Berenguer, Gimeno, and Nave 2014). As a robustness check, we also consider the natural logarithm of volume as a possible measure of liquidity. 

We regress price error estimated in the _NL_ model on both the function of the trading volume, logð _volumei;t_ Þ and _LIQi;t_ along with duration _Di;t_ , and expð� _agei;t_ Þ, taken one at a time as well as together. 

Table 3 summarizes the regression results. The coefficients of both _LIQi;t_ and logð _volumei;t_ Þ are significant and have expected positive sign suggesting positive price premium for highly traded securities. Similarly, a positive and significant coefficient of the expð� _agei;t_ Þ suggests that newly issued security demand higher price. A negative sign on duration suggests term premium dominates microstructure effects in Indian bond markets. 

The regression specification 4 has the best adjusted R-square (0.34), lowest AIC and BIC. We use this specification as a proxy to capture 

APPLIED ECONOMICS 657 

security-specific liquidity premium and refer to it as the proxy-liquidity ( _PL_ ) model hereafter. Liquidity specification for the _PL_ model is given as: 

_h[v] i;t_[as an exponential function makes sure that the ] variance of the measurement error is always positive. Measurement equation and state equation as specified in the Equation (17) along with the liquidity specification given in the Equation (19) and (20) provide the complete state space specification of the _PL_ model. As a robustness check, we also consider a restricted version of the _PL_ model, referred to as _PL R_ model hereafter, by ignoring liquidityinduced heteroscedasticity (setting _h[v] i;t_ equal to one). 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0011-03.png)


where _LIQi;t_ is the exponential transformation of the trading volume of the security _i_ at time _t_ as given in Equation (18). _agei;t_ is the age of the security _i_ at _t_ since issuance and _Di;t_ is the duration of the security _i_ at time _t_ . 

## _**Second adjustment defining market liquidity as a latent factor**_ 

The price errors reported from the _NL_ model suggests that error terms arising out of liquidity difference across bonds are heteroskedastic (Figures 2 and 3). To incorporate liquidityinduced heteroscedasticity _h[v] i;t_[, ] we define logð _h[v] i;t_[Þ][as a linear combination of ] _[LIQ][i][;][t]_[, ] _[D][i][;][t]_[, ] exp _agei;t_ Þ, and interaction between _Di;t_ and exp _agei;ti;t;tt_ Þ as: 

Next, we incorporate the influence of systematic market liquidity on the bond prices by building on Fontaine and Garcia (2011). We call this the Latent-liquidity, or the _LL_ model, incorporate liquidity-induced heteroscedasticity. The state space representation that results in the _LL_ model is: 

_i;t;tt i;t ;t t_ This framework has market liquidity, _FLIQt_ , as _agei;ti;t;tt_ Þ as: an additional latent factor along with the three Nelson Siegel factors of the AFNS model. The logð _h[v] i;t_[Þ ¼] _[ γ]_ 1 _[LIQ][i][;][t]_[ þ] _[ γ]_ 2 _[D][i][;][t]_[ þ] _[ γ]_ 3[exp] _agei;t_ Þ factor loading on latent market liquidity factor is þ _γ_ 4 _Di;t_ x exp (= _agei;t_ Þ defined as a function of bond age and time to (20) maturity. _FLIQt_ influences both the _hi;t_ and _h[v] i;t_[, ] 

**Figure 2.** Error variation across time to maturity and trading volume (CCIL estimates): This represents variation in the estimated price error (bottom panel) and yield error (top panel) of the CCIL estimates with time to maturity (left column) and the monthly trading volume (right column) of the security. 

658 S. KUMAR AND V. VIRMANI 

**Figure 3.** Error variation across time to maturity and trading volume (NL model): This represents variation in the estimated price error (bottom panel) and yield error (top panel) of the estimates of the _NL_ with time to maturity (left column) and the monthly trading volume (right column) of the security. 

and _βm_ and _γm_ capture maturity-specific sensitivity of the securities with the market liquidity. The term exp (— _m_ x _agei;t_ Þ captures the variation in the liquidity sensitivity due to the age of the security. This formulation allows us to capture higher marginal decrease in the sensitivity with market liquidity for the newly issued securities. As for the _PL_ model, we also consider a restricted version of _LL_ model, referred to as the _LL R_ model hereafter, by ignoring the liquidity-induced heteroscedasticity (setting _h[v] i;t_[equal to one).] 

## _**Combining proxy and latent liquidity approaches**_ 

Finally, we also explore whether trading volume of the security has any extra explanatory power for the bond prices over the specification of the _LL_ model. In this specification, we add _LIQi;t_ (defined in the Equation 18) as an additional predictor of the liquidity in the specification of _LL_ model, referred to the proxy and latent liquidity or the _PLLL_ model hereafter. Adjustment in the _PLLL_ model is given in Equation (22). Rest of the formulation is similar to the _LL_ model (Equation 21). In this specification, _FLIQt_ can be interpreted as systematic liquidity risk factor, while _LIQi;t_ captures security-specific liquidity risk. 

_hi;t_ ¼ _βLIQLIQi;t_ þ _βm_ exp (— _m_ x _agei;t_ Þ _FLIQt log_ ð _h[v] i;t_[Þ ¼] _[ γ] LIQ[LIQ][i][;][t]_[ þ] _[ γ] m_[exp] (— _m_ x _agei;t_ Þ _FLIQt_ (22) 

Our main specification _PLLL_ in Equation (22) incorporates both security-specific liquidity and systematic liquidity factors. 

Following Andreasen, Christensen, and Rudebusch (2019), for estimation of these models, we use the one-step approach where we directly estimate term structure factors from the coupon bond prices. Albeit computationally intensive, this approach provides a better fit to the underlying coupon bonds and provides richer bond price information. We briefly detail our estimation framework next. 

## _**Estimation: nonlinear state space approach implemented using the Unscented Kalman filter**_ 

In a standard linear state space model with Gaussian errors, Kalman filter is the preferred method for parameter estimation, as it provides the exact updation of the mean and variance of the system (Simon 2006). In our context, coupon bond prices are a nonlinear function of the yield 

APPLIED ECONOMICS 659 

curve factors making our state space set-up nonlinear. The Extended Kalman filter (EKF) gets around the nonlinearity by using a Taylor series expansion, but if the nonlinearity is severe EKF can produce wrong and inconsistent estimates (Christoffersen et al. 2014). 

Julier and Uhlmann (1997) have proposed the Unscented Kalman filter (UKF) as a superior alternative to EKF. They argue that approximating a probability distribution is easier than approximating a nonlinear transformation. UKF uses careful sampling (called ‘sigma points’) around the states to estimate the mean and the variance of the nonlinear function. Following Julier and Uhlmann (1997), we describe our implementation of UKF that has been used to estimate our nonlinear state space models. 

We can represent bond pricing function for the liquidity adjusted AFNS model described in Equation (15) as a nonlinear state space system. 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-04.png)


where _Pt_ 2 _R[K ]_ is the vector of the coupon bond prices at time _t_ . _f_ ð _Xt; ht_ Þ is a nonlinear function, mapping latent factor and liquidity to the bond prices. For estimation using UKF, the state mean and variance are initialized at the unconditional mean and variance, respectively: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-06.png)


Since the state transition function is linear, the first step of time updation of the state mean and variance from time _k_ � 1 to _k_ follows the usual Kalman filter approach: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-08.png)


In the next step, because of a nonlinear relationship between the state factors and bond prices, ð2 _N_ þ 1Þ sigma points _χk_ j _k_ � 1 2 _R[K]_[�ð][2] _[N]_[þ][1][Þ] are drawn around 

^ _X_[�] _k_[and the measurement equation is used to trans-] form the sigma points _χk_ j _k_ � 1 to the predicted measurements. 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-11.png)


where _N_ is the state dimension, _λ_ ¼ _α_[2] ð _N_ þ _κ_ Þ � _N_ , and _α_ determines the spread of the sigma points around _χk_ j _k_ � 1 and _κ_ is the scaling parameter. Next, we update the mean and covariance of the predicted measurement using the following recursion: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-13.png)


The cross-covariance between _Xk_ and _Pk_ is estimated as: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-15.png)


with rest of the procedure similar to the standard Kalman filter algorithm: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0013-17.png)


## **V. Results and discussion** 

We now present and compare results for the six variants of the AFNS specifications implemented using estimation strategy described in Section 4: _NL_ , _LL_ , _LL_ � _R_ , _PL_ , _PL_ � _R_ and _PLLL_ (for a quick reference, brief overview of all the different specifications is provided in Table 4) using the bond price data provided by CCIL. 

660 S. KUMAR AND V. VIRMANI 

The estimated _K[p ]_ matrix and � matrix and _θ[p ]_ for different specifications are reported in Appendix A. The estimates are similar across all the specifications, with _K_ 1 _[p] ;_ 1[, ] _[K]_ 2 _[p] ;_ 2[and ] _[K]_ 3 _[p] ;_ 3[lacking significance ] at 99% in most of the specifications. As a robustness check, following Christensen and Rudebusch (2012) we also estimate the model by imposing unit root in all the three factors and the results are similar (not reported here and available on request). 

## _**Estimates of the liquidity specification**_ 

Table 5 reports the estimates of the liquidity speci- _PL_ � fications for the proxy-based models (PL and _R_ models). _β_ ð _PL_ Þ and _γ_ ð _PL_ Þ provide the liquidity coefficients for _PL_ model and _β_ ð _PL_ � _R_ Þ provides the liquidity coefficients for _PL_ � _R_ model. _γ_ of _PL_ model negatively influences the weight of the different observations in the likelihood calculation. For example, a negative _γ_ coefficient of the duration implies that the model fits the longer end of the yield curve more closely at the expense of the shorter end of the yield curve. This formulation is consistent with the higher measurement error in the yield at short-term maturity because of the market microstructure (Berenguer, Gimeno, and Nave 2014). 

As expected, _β_ of the _LIQi;t_ variable is positive and significant for both the specifications. Other things being the same, one standard deviation increase in the _LIQi;t_ increases bond prices by approximately 0.25%. Figure 2 displays a higher dispersion in the price error for very small trading volume. However, the dispersion seems to decrease first, then increases with the increase in 

**Table 5.** Liquidity analysis: Proxy-Liquidity model: Reports the specification of the the _PL_ and _PL_ � _R_ models. Column _hi;t_ (Equation 19) and _β_ ð _PL_ Þ and _h[v] i;t γ_[(Equation 20) for ] ð _PL_ Þ provide the liquidity coefficients for the _PL_ model corresponding to the proxy variables specified in the variable column. Column _β_ ð _PL_ � _R_ Þ provides the liquidity coefficients for the _PL_ � _R_ model. Standard errors are reported below the coefficients in the parentheses. 

||Variable|_β_(PL)|_γ_(PL)|_β_(PL-R)|
|---|---|---|---|---|
||_LIQ_|1.619|1.163|1.468|
||_dur_|(0.022)<br>0.359|(0.05)<br>−0.147|(0.016)<br>0.225|
|||(0.008)|(0.004)|(0.008)|
||_dur_ :expð�_age_Þ|0.077|−0.163|0.228|
|||(0.005)|(0.012)|(0.005)|
||expð�_age_Þ|0.157<br>(0.025)|2.049<br>(0.072)|−0.269<br>(0.021)|



the _LIQi;t_ . The positive _γ_ coefficient for the _LIQi;t_ suggests that the latter effect dominates in the estimation. 

For the _PL_ model, we find positive and significant _β_ for the expð� _agei;t_ Þ, suggesting newly issued securities demanding the extra liquidity premium (Sarig and Warga 1989). Although, surprisingly, we get a negative coefficient for the same variable for _PL_ � _R_ model. The interaction variable between expð� _age_ Þ and duration also has a positive and significant _β_ for both _PL_ and _PL_ � _R_ model and negative _γ_ for _PL_ model. 

Table 6 summarizes the estimates of liquidity model of _LL_ , _LL_ � _R_ and _PLLL_ models. _βm_ of these models can be interpreted as the sensitivity of the newly issued bond prices ( expð� _agei;t_ Þ ¼ 1) of the specific maturity segments to the latent market liquidity factor. In line with the evidence of Docherty and Easton (2018), we observe almost monotonic increase in 

**Table 4.** Model description: This table summarizes the liquidity specifications of the six models analysed in the study. 

|Name||Liquidity Specifcation|
|---|---|---|
|No liquidity (_NL_)||_hi;t_ ¼0|
|||_hv_<br>_i;t_ ¼1|
|Proxy-liquidity (_PL_)|_hi;t_ ¼_β_1_LIQi;t_ þ|_β_2_Di;t_þ_β_3expð�_agei;t_Þ þ_β_4_Di;t_ �expð�_agei;t_Þ|
||logð_hv_<br>_i;t_Þ ¼_γ_1_LIQi;t_|þ_γ_2_Di;t_ þ_γ_3 expð�_agei;t_Þ þ_γ_4_Di;t_ �expð�_agei;t_Þ|
|Proxy-liquidity_R_(_PL_�_R_)|_hi;t_ ¼_β_1_LIQi;t_ þ|_β_2_Di;t_þ_β_3expð�_agei;t_Þ þ_β_4_Di;t_ �expð�_agei;t_Þ|
|||_hv_<br>_i;t_ ¼1|
|Latent-liquidity (_LL_)||_hi;t_ ¼_βm_expð�_m_�_agei;t_Þ_FLIQt_|
||logð_hv_<br>_i;t_Þ ¼_γm_ expð�_m_�_agei;t_Þ_FLIQt_||
|Latent liquidity_R_(_LL_�_R_)||_hi;t_ ¼_βm_expð�_m_�_agei;t_Þ_FLIQt_|
|||_hv_<br>_i;t_ ¼1|
|Proxy + Latent (_PLLL_)|_hi;t_ ¼|_βLIQLIQi;t_ þ_βm_expð�_m_�_agei;t_Þ_FLIQt_|
||_log_ð_hv_<br>_i;t_Þ|¼_γLIQLIQi;t_þ_γm_ expð�_m_�_agei;t_Þ_FLIQt_|
|_Note:_|:_RPL_�_R_and_LL_�_R_models do not consider liquidity induced heteroscadsticity||



APPLIED ECONOMICS 661 

the price sensitivity with the increase in maturity till year 10. Beyond 10 year maturity, the results are mixed. 

Alternatively, in the cross section at any time _t_ , _FLIQt_ is a constant. Thus, _βm_ also corresponds to the average price premium demanded by securities in the corresponding maturity segment. Statutory liquidity ratio (SLR), mandates banks to invest a certain amount in the Government securities, which artificially suppresses the yield of the Government securities (Banerjee et al. 2018; Patel et al. 2014). Also, banks tend to hold longer duration Government securities in their portfolio (Acharya 2018). Hence, suppression of the yield should be more significant at the longer segment of the yield curve. Consistent with the above proposition, _βm_ estimates for _LL_ and _PLLL_ models increases monotonically till the 10 year maturity segments. Further, higher trading volume in 7 to 10 year (07 � 10 _Y_ ) and 12 to 15 year (12 � 15 _Y_ ) maturity segments (Table 1) corresponds to the higher beta in these maturity segments. 

The estimated negative _βm_ for securities with less than one-year maturity implies two things. First, for the constant _FLIQt_ , short-term maturity bonds have a negative price premium as compared to the long-term maturity bonds. Second, when market liquidity ( _FLIQt_ ) 

**Table 6.** Liquidity analysis: Latent factor models: Reports the liquidity specification of the _LL_ (Equation 21), _LL_ � _R_ and _PLLL_ models. _β_ for the _LL_ and _LL_ � _R_ model provides the specification of the _hi;t_ . _β_ of the _PLLL_ model has an additional term ‘Liq’ in the specification along with the coefficients corresponding to the different maturity bins (Equation 22). _γ_ for the _LL_ and _PLLL_ models provides specification of the _h[v] i;t_[.] 

|Maturity bin|_β_ð_LL_Þ|_γ_ð_LL_Þ|_β_ð_LL_�_R_Þ|_β_ðPLLLÞ|_γ_ðPLLLÞ|
|---|---|---|---|---|---|
|_<_01_Y_|−0.725���|14.004���|0.088���|−1.347���|23.824���|
|01–02Y|0.219���|−1.337���|0.231���|0.219���|−0.502|
|02–05Y|0.263���|−0.023|0.22���|0.089���|0.864���|
|05–07Y|0.404���|0.184���|0.483���|0.468���|0.134�|
|07–10Y|0.93���|1.006���|1.212���|0.971���|0.774���|
|10–12Y|0.461���|0.168��|0.554���|0.596���|0.058|
|12–15Y|1.122���|0.153���|1.141���|1.093���|0.228���|
|15–20Y|0.725���|0.076�|0.655���|0.911���|0.253���|
|20–25Y|−2.574���|−3.897���|−2.664���|−2.865���|−4.544���|
|25–30Y|0.91���|−1.388���|0.477���|1.077���|−1.389���|
|30–50Y|1.222���|−0.325���|1.027���|1.438���|−0.237���|
|Liq||||1.203���|0.54���|
|_Note:_|�p_<_0.1;��|p_<_0.01;���|p_<_0.001|||



deteriorates in the economy, the difference between the price premium between the longer maturity bond and shorter maturity bonds decreases. This might be due to the possible portfolio re-balancing towards the shorter maturity bonds during the market uncertainty or liquidity crunch. 

Both the _LL_ and _PLLL_ models document high positive _γm_ (which implies higher volatility) for securities with maturities less than one year and negative _γm_ at longer maturity segments. This implies that both these models also fit the longer end of the yield curve at the cost of shorter end of the yield curve. 

## _**Statistical significance of the liquidity specification**_ 

The _NL_ model is nested inside both the _LL_ and the _PL_ models. These nested structures allow us to test the restrictions _hi;t_ ¼ 0 and _h[v] i;t_[¼][ 1 assumed in the ] _NL_ model with respect to the _PL_ and the _LL_ model. Similarly, the _LL_ � _R_ and the _PL_ � _R_ models are nested inside the _LL_ and the _PL_ models respectively, which allows us to test the significance of liquidityinduced heteroscedasticity under the null hypothesis of _h[v] i;t_[¼][ 1 assumed in the ] _[LL]_[ �] _[R ]_[and the ] _[PL]_[ �] _[R ]_ models. Finally, the _LL_ model is also nested inside the _PLLL_ model, which allows us to test the null hypothesis of _βLiq_ ¼ 0, _γLiq_ ¼ 0, assumed in the _LL_ model. We test the statistical significance of these restrictions using the log likelihood ratio test. 

The result of these tests is summarized in Table 7. The restriction of the _NL_ model is rejected with respect to the _LL_ and _PL_ models. This result statistically validates incorporating both the dimensions of liquidity in the term structure estimation in the Indian Government bond market. Further, the likelihood ratio test also validates the importance of liquidity-induced heteroscedasticity by rejecting the null of the _LL_ � _R_ and the _PL_ � _R_ models in favour of the _LL_ and the _PL_ models. Since null of _βLIQ_ ¼ 0, _γLIQ_ ¼ 0 is also rejected in favour of PLLL model, market micro-structure, captured by trading volume of the security, has explanatory power of the variation in the bond prices _over and above_ the explanation provided by the latent systematic liquidity factor. 

662 S. KUMAR AND V. VIRMANI 

**Table 7.** Log likelihood ratio test results. 

|||_H_0|statistic|df|p-value|
|---|---|---|---|---|---|
|_NL_|vs._LL_|_hi;t_ ¼0,_hv_<br>_i;t_ ¼1|27,231.22|24|0|
|_NL_|vs._PL_|_hi;t_ ¼0,_hv_<br>_i;t_ ¼1|28,393.86|8|0|
|_LL_|�_R_vs.LL|_hv_<br>_i;t_ ¼1|3401.17|11|0|
|_PL_|�_R_vs._PL_|_hv_<br>_i;t_ ¼1|6162.66|4|0|
|_LL_|vs_PLLL_|_βLIQ_ ¼0,_γLIQ_ ¼0|4134.69|2|0|



**Table 8.** Stablity of the factor estimates: Reports standard deviation of the first difference of the estimated factors. 

||CCIL|_NL_|_LL_|_LL_�_R_|_PL_|_PL_�_R_|PLLL|
|---|---|---|---|---|---|---|---|
|_β_1_:SD_|7_:_51|3_:_02|3_:_29|3_:_42|3_:_43|3_:_47|3_:_37|
|_β_2_:SD_|15_:_35|4_:_97|5_:_66|6_:_42|6_:_20|6_:_32|6_:_10|
|_β_3_:SD_|54_:_02|6_:_67|8_:_90|8_:_29|9_:_04|8_:_48|9_:_38|



## _**Determinants of implied liquidity**_ 

## _**Stability of the factor estimates**_ 

Independent cross-sectional estimates of the factors in the Nelson-Siegel specification does not consider the time dynamics of these factors. Hence, estimated factors are usually unstable in the time series (De Pooter 2007). We use the standard deviation of the first difference of the factors as a measure of the stability of the factor estimates. Table 8 reports this value for all three factors for the different model specifications. As expected, state space based models have more stable factor estimates than the independent cross-sectional estimates of the CCIL. Among the state space models, the _NL_ model seems to have marginally stable factor estimates than the liquidity based models. 

## _**In-sample estimation performance**_ 

Next, we compare the in-sample estimation accuracy of the different model specifications. CCIL publishes cross-sectional fit of the Nelson- Siegel factors daily. CCIL estimates provide a benchmark of the accuracy of the existing yield curve estimation in India. Hence we compare in sample performance of our proposed models with the cross-sectional estimates of the CCIL. Table 9 reports the root mean square error (RMSE) for the different model specifications across maturity segments. Unlike dynamic approach adapted in this study, CCIL provides the independent daily fit of the yield curve. Hence one would expect better in-sample fit by the CCIL estimates. However, CCIL estimates perform worst among all the specifications. The liquidity augmented models provides a marginally better in-sample fit than the _NL_ model, but none of these models perform better in terms of in-sample accuracy across all maturity segments. As highlighted in Section 5.1, the _LL_ , _PL_ and _PLLL_ models try to fit the longer end of the curve at the cost of fit at the short end of the yield curve. 

Finally, we explore the macroeconomic interpretation of the extracted systematic liquidity factor _FLIQt_ . During the study period, the Indian banking system witnessed two significant liquidity shocks. First, in the second quarter of 2013, the US Federal Reserve (FED) signalled (or perceived by market) to reduce the quantitative easing (QE) programme. This event referred to as the ‘Taper Tantrum’ led to a sharp liquidity crunch in the Indian financial system (RBI 2014) because of the unwinding of foreign investments. Second, on 8 November 2016, Indian Government has decided to ‘demonetize’ the higher denomination notes, resulting in strong inflow of cash in the Indian banking system (Lahiri 2020). _FLIQt_ captures both the liquidity squeeze during the FED taper tantrum and liquidity surplus after the demonetization (see Figure 4). 

We also explore the relationship between extracted _FLIQt_ with the various predictors of the market liquidity described in Section 3 earlier. Designated primary dealers (PDs) of the Indian government bond market rely on the overnight market for their short term funding needs. Therefore, any stress in the overnight market would directly influence trading behaviour of these PDs. First, we consider two different measures of cost of overnight funding as a possible correlates of 

**Table 9.** RMSE (Root mean square error) of the estimated yields in the different model in basis points: This table presents RMSE in basis points of all the estimated model along with the CCIL across different maturity segments. Best performing model in every segment is highlighted in bold. 

|Maturity|CCIL|_NL_|_LL_|_LL_�_R_|_PL_|_PL_�_R_|PLLL|
|---|---|---|---|---|---|---|---|
|_<_01_Y_|12_:_29|9_:_18|14_:_31|**8.24**|12_:_27|10_:_09|17_:_70|
|01–02Y|10_:_30|7_:_64|**6**_:_**21**|6_:_60|7_:_85|7_:_18|6_:_22|
|02–05Y|7_:_91|6_:_08|**5**_:_**66**|5_:_67|7_:_19|6_:_42|6_:_13|
|05–07Y|8_:_06|7_:_10|6_:_13|6_:_37|6_:_63|6_:_32|**6**_:_**12**|
|07–10Y|13_:_15|12_:_89|9_:_49|8_:_57|8_:_92|8_:_23|**7**_:_**88**|
|10–12Y|8_:_21|8_:_34|8_:_46|8_:_31|7_:_39|**7**_:_**35**|7_:_51|
|12–15Y|11_:_17|10_:_28|6_:_35|6_:_44|7_:_29|6_:_64|**5**_:_**94**|
|15–20Y|6_:_90|7_:_67|6_:_66|6_:_78|**5**_:_**48**|6_:_51|6_:_30|
|20–25Y|8_:_47|10_:_56|8_:_52|8_:_35|**7**_:_**22**|9_:_46|8_:_11|
|25–30Y|5_:_75|6_:_96|4_:_80|5_:_78|**4**_:_**78**|7_:_21|4_:_79|
|30–50Y|10_:_46|9_:_93|**5**_:_**94**|6_:_77|5_:_79|7_:_04|6_:_44|
|Pooled|9_:_54|8_:_99|7_:_38|**7**_:_**02**|7_:_38|7_:_21|7_:_14|



APPLIED ECONOMICS 663 

market liquidity. Following Chundakkadan and Sasidharan (2019), we use the normalized spread between the call rate ( _Call_ ) and the reverse repo rate to capture the liquidity in the banking system as: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0017-02.png)



![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0017-03.png)


The spread between Call and CBLO ( _Call CBLO_ ) measures the funding cost advantage of holding the security. (Fontaine and Garcia 2011). The net liquidity injected by RBI ( _Net injection RBI_ ) provides the assessment of central bank regarding the liquidity situation in the banking system. As a market-oriented alternative, Bloomberg provides an aggregate measure of liquidity deficit in the financial system, which we refer to as _Bloomberg liquidity_ ), computed as: 


![](markdown_output/Term_structure_estimation_with_liquidity-adjusted_images/Term_structure_estimation_with_liquidity-adjusted.pdf-0017-05.png)


where MSF and SLF, respectively, stand for RBI’s Marginal Standing Facility and Secured Lending Facility. 

Along with these four proxies of the market liquidity, we also consider secondary market activity in the Indian government bond market and the India VIX index. Although VIX is an equity market 

variable, it is widely used as a proxy of overall risk in the financial system and is shown to influence the bond yields as well (Adrian, Crump, and Vogt 2019). 

Table 10 reports regression results of the extracted _FLIQt_ on the different predictors of funding liquidity taken one at a time as well as together. 

In the first six specifications presented in Table 10, we regress these variables separately on the _FLIQt_ extracted from the _LL_ model. Latent _FLIQt_ extracted from the _LL_ , _LL R_ and the _PLLL_ models are highly correlated with the correlation greater than 0.95. For sake of brevity, we show the regression with market liquidity ( _FLIQt_ ) extracted from the _LL_ model only. In the individual regressions (specifications 1–6) all the variables are significant and their signs are consistent with the theory. Spread between call rate and reverse repo rate and spread between call rate and the CBLO rate are negatively related to the market liquidity. Increased liquidity injection by RBI is associated with deteriorating liquidity condition. Similarly, Bloomberg liquidity indicator, which measures overall liquidity deficit in the banking system is negatively related to the market liquidity. Also, higher trading volume in the Indian government bond market is positively related to the market liquidity. Finally, an increase in the VIX index is also negatively associated with the market liquidity. 

**Figure 4.** Filtered latent liquidity factor ( _FLIQt_ : This represents the time series plot of Filtered latent liquidity factor ( _FLIQt_ ) for the LL specification. _FLIQt_ seems to capture two important liquidity shock: Fed taper tantrum and Demonetization in the Indian banking system. 

664 S. KUMAR AND V. VIRMANI 

**Table 10. Determinants of implied liquidity** : Reports the regression result of the extracted market liquidity factors on the various predictor of the liquidity. _Call_ � _RRepo_ is the normalized spread between the call rate and reverse repo rate. _Call_ � _CBLO_ is the spread between Call rate and CBLO rate. _Net injection_ � _RBI_ is the net liquidity injected by RBI (in Trillion rupees). _Bloomberg liquidity_ is the liquidity indicator published by the bloomberg . logð _Trading vol_ Þ is log of total daily trading volume of the Government bond market. Finally _VIX_ is the VIX index. In the first six specification we regress these variables separately on the _FLIQt_ extracted from the _LL_ model. In the seventh specification, we regress _FLIQt_ on all the independent variables together. Last specification presents the result with _Bloomberg liquidity_ and _VIX_ toogether as a regressor. 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|
|---|---|---|---|---|---|---|---|---|
|_Call_�_RRepo_|�0.376���||||||0.067���||
||(0.031)||||||(0.019)||
|_Call_�_CBLO_||�0.119���|||||0.043||
|||(0.033)|||||(0.032)||
|_Net injection RBI_|||�0.648���||||�0.017||
||||(0.031)||||(0.025)||
|_Bloomberg liquidity_||||�0.346���|||�0.337���|�0.318���|
|||||(0.008)|||(0.011)|(0.008)|
|logð_Trading vol_Þ|||||0.266���||�0.100���||
||||||(0.018)||(0.025)||
|_VIX_||||||�0.039���|�0.016���|�0.021���|
|||||||(0.003)|(0.003)|(0.002)|
|Constant|1.457���|1.135���|1.370���|1.240���|�1.550���|1.849���|2.571���|1.615���|
||(0.032)|(0.015)|(0.016)|(0.010)|(0.181)|(0.064)|(0.275)|(0.037)|
|_Observations_y|1,949|1,949|1,210|1,659|1,997|1,972|1,191|1,635|
|R2|0.146|0.006|0.378|0.632|0.098|0.095|0.679|0.655|
|Adj. R2|0.146|0.005|0.377|0.632|0.098|0.095|0.678|0.655|
|Res. Std. Error|0.606|0.654|0.534|0.386|0.620|0.620|0.383|0.373|
|F Statistic|332.911���|11.098���|733.460���|2,848.435���|216.743���|207.440���|418.300���|1,550.209���|
|df|1; 1947|1; 1947|1; 1208|1; 1657|1; 1995|1; 1970|6; 1184|2; 1632;|
|_Note:_||||�p_<_0.1;��p_<_0.05;���p_<_0.01|||||
|y|Number of observations in diferent regression|||varies as some independent variables||are not available|for the complete time period.||



In specification 7, where we regress all the independent variable together, variables _Call – RRepo, Call – CBLO_ and logð _Trading vol_ Þ change their sign. The variable _Net injection RBI_ loses its significance. _Bloomberg liquidity_ seems to explain majority of the variation in the market liquidity factor. The _R_[2 ] from individual regression of _Bloomberg liquidity_ on the market liquidity is 0.632 (which implies a correlation coefficient of almost 0.8). The addition of other independent variables does not seem to impact the magnitude of its coefficient much. _VIX_ also looses more than half of the significance when regressed along with other independent variables but is still significant. Finally, in specification 8, we use both _Bloomberg liquidity_ and _VIX_ both as a regressor. Improvement in _R_[2 ] from specification 4 is marginal (from 0.632 to 0.655), nonetheless, _VIX_ is still significant. 

The evidence suggests that along with _VIX_ , the _Bloomberg liquidity_ variable (capturing overall liquidity deficit in the banking system), explains a majority of the variation in the implied liquidity 

factor. It also subsumes explanations provided by other independent variables such as _Call – RRepo, Call – CBLO_ and logð _Trading vol_ Þ. 

## **VI. Conclusion** 

Efficient term structure estimation is critical for pricing fixed income instruments and extracting inflation expectations. Given the importance of Government bonds as collateral with clearing corporations, term structure estimation is also critical for calculating margin requirements and valuation of non-traded securities and derivative contracts. 

Despite lack of liquidity in Government bond markets across maturity segments, the standard term structure estimation framework used predominantly in applied research and practice does not adjust for heterogeneity in liquidity of bonds across the maturity spectrum, and club bonds with different trading volumes together. As a contribution to the literature on term structure estimation, this study explicitly incorporates both security specific liquidity 

APPLIED ECONOMICS 665 

and market liquidity in the bond pricing function within the AFNS model Christensen, Diebold, and Rudebusch (2011). In absence of matched order book data in emerging markets, we construct a proxy for liquidity as a function of the trading volume, age and bond duration in the bond pricing function. Following Fontaine and Garcia (2011), we also incorporate market liquidity as a latent risk factor and its factor loading as a function of the age of the security and time to maturity. To our knowledge, this is the first study applying AFNS to an emerging economy bond market while explicitly adjusting for liquidity. 

The liquidity-augemented AFNS framework used in the study has shown to improve upon the pricing efficiency over models, which treat all bonds homogenously. We have also shown that our derived funding liquidity factor estimates is strongly correlated with the day-today changes in the liquidity in the Indian banking system and the India VIX index, corroborating its reliability and robustness. 

Beyond finding applicability in modelling and estimating term structure in other emerging economy bond markets with characteristics similar to India, like Taiwan (Chou et al. 2009), Spain (Berenguer, Gimeno, and Nave 2014) and China (Xie, Chen, and Yu 2006), our framework also allows for extracting both the market liquidity as well as sensitivity of different bonds to the market liquidity. More than just providing an improved specification to fit the yield curve to Government bonds, our framework can also be used to explore the impact of different central bank interventions or other macroeconomic shocks on the market liquidity in future applied macroeconomic research. Our framework is also amenable to be extended to explore the term structure of liquidity in the government bond market. 

In the context of Black-Scholes option pricing formula and its popularity, MacKenzie (2006) in his book ‘ An Engine, Not a Camera’ argues that financial models do more than analysing markets – they alters them. While we have no delusion that our modest contribution compares with the famous BlackScholes model, increased sophistication and improvement in term structure estimation should contribute to better bond pricing, and in turn development and growth of interest rate derivatives market in India. 

## **Acknowledgments** 

We thank Arnab K. Laha, Anindya Chakrabarti, Brain Lucey, Jayanth R. Varma, Katherine Bennett Ensor, Rituparna Sen, Sourish Das, and participants at the 26th EBES conference (2018), 2nd INFINITI ASIA-PACIFIC Conference (2018), India Finance conference (2018), Statistical Methods in Finance conference (2018) for the valuable comments. 

## **Disclosure statement** 

No potential conflict of interest was reported by the author(s). 

## **ORCID** 

Sudarshan Kumar http://orcid.org/0000-0002-4941-6010 

## **References** 

Acharya, V. V. 2018. “Understanding and Managing Interest Rate Risk at Banks.” _Macroeconomics and Finance in Emerging Market Economies_ 11 (2): 218–231. doi:10.1080/ 17520843.2018.1473458. 

Acharya, V. V., and L. H. Pedersen. 2005. “Asset Pricing with Liquidity Risk.” _Journal of Financial Economics_ 77 (2), 375–410. http://www.sciencedirect.com/science/article/pii/ S0304405X05000334 . 

- Adrian, T., R. K. Crump, and E. Vogt. Nonlinearity and Flight-to-safety in the Risk-return Trade-off for Stocks and Bonds. _The Journal of Finance_ . 2019. 74(4):1931–1973. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12776 . 

- Akhtaruzzaman, M., and A. Shamsuddin. 2017. “Australian Financial Firms’ Exposures to the Level, Slope, and Curvature of the Interest Rate Term Structure.” _Applied Economics_ 49 (19): 1855–1874. doi:10.1080/ 00036846.2016.1229411. 

- Alper, C. E., K. Kazimov, and A. Akdemir. 2007. Forecasting the Term Structure of Interest Rates for Turkey: A Factor Analysis Approach. _Applied Financial Economics_ 17 (1): 77–85. doi:10.1080/09603100600606156. 

- Amihud, Y., and H. Mendelson. 1991. “Liquidity, Maturity, and the Yields on U.S. Treasury Securities.” _The Journal of Finance_ 46 (4): 1411. doi:10.2307/2328864. 

- Andreasen, M. M., J. H. Christensen, and G. D. Rudebusch. Term Structure Analysis with Big Data: One-step Estimation Using Bond Prices. _Journal of Econometrics_ 2019. http://www.sciencedirect.com/science/article/pii/ S0304407619300740. 1 

- Audzeyeva, A., and A. M. Fuertes. 2018. “On the Predictability of Emerging Market Sovereign Credit Spreads.” _Journal of International Money and Finance_ 88: 140–157. doi:10.1016/ j.jimonfin.2018.07.005. 

666 S. KUMAR AND V. VIRMANI 

- Banerjee, S., P. Basu, C. Ghate, P. Gopalakrishnan, S. Gupta. A Monetary Business Cycle Model for India. Planning and Policy Research Unit Working Paper; Indian Statistical Institute; 2018. https://www.isid.ac.in/cghate/PPRU_ March_5_2018_Final.pdf . 

- Beechey, M., and P. Österholm. 2014. “Policy Interest-rate Expectations in Sweden: A Forecast Evaluation.” _Applied Economics Letters_ 21 (14): 984–991. doi:10.1080/ 13504851.2014.904480. 

- Berenguer, E., R. Gimeno, and J. M. Nave. 2014. “Term Structure Estimation, Liquidity-induced Heteroskedasticity and the Price of Liquidity Risk.” _SSRN Electronic Journal_ . doi:10.2139/ssrn.2428640. 

- Bliss, R. Testing Term Structure Estimation Methods. Staff Reports 12; Federal Reserve Bank of Atlanta; 1996. https:// www.atlantafed.org/research/publications/wp/1996/12 . 

- Bolder, D. J. 2001. “Affine Term-structure Models: Theory and Implementation.” _SSRN Electronic Journal_ . doi:10.2139/ ssrn.1082826. 

- Brzoza-Brzezina, M., and J. Kotłowski. 2014. Measuring the Natural Yield Curve. _Applied Economics_ 46 (17): 2052–2065. doi:10.1080/00036846.2013.829204. 

- Carriero, A., S. Mouabbi, and E. Vangelista. 2018. “Uk Term Structure Decompositions at the Zero Lower Bound.” _Journal of Applied Econometrics_ 33 (5): 643–661. doi:10.1002/jae.2635. 

- Chen, S., Z. Zhou, and S. Li. 2016. “An Efficient Estimate and Forecast of the Implied Volatility Surface: A Nonlinear Kalman Filter Approach.” _Economic Modelling_ 58: 655–664. doi:10.1016/j.econmod.2016.06.003. 

- Chou, J. H., Y. S. Su, H. W. Tang, C. Y. Chen. 2009. “Fitting the Term Structure of Interest Rates in Illiquid Market: Taiwan Experience.” _Investment Management and Financial Innovations_ 6 (1): 101–116. 

- Christensen, J. H., F. X. Diebold, and G. D. Rudebusch. 2011. “The Affine Arbitrage-free Class of Nelson-Siegel Term Structure Models.” _Journal of Econometrics_ 164 (1): 4–20. doi:10.1016/j.jeconom.2011.02.011. 

- Christensen, J. H. E., F. X. Diebold, and G. D. Rudebusch. 2009. “An Arbitrage-free Generalized Nelson–siegel Term Structure Model.” _The Econometrics Journal_ 12 (3): C33– C64. doi:10.1111/j.1368-423X.2008.00267.x. 

- Christensen, J. H. E., J. A. Lopez, and G. D. Rudebusch. 2010. “Inflation Expectations and Risk Premiums in an Arbitrage-free Model of Nominal and Real Bond Yields.” _Journal of Money, Credit, and Banking_ 42 (s1): 143–178. doi:10.1111/j.1538-4616.2010.00332.x. 

- Christensen, J. H. E., J. A. Lopez, and G. D. Rudebusch. 2014. “Do Central Bank Liquidity Facilities Affect Interbank Lending Rates?” _Journal of Business and Economic Statistics_ 32 (1): 136–151. doi:10.1080/07350015.2013.858631. 

- Christensen, J. H. E., and G. D. Rudebusch. 2012. “The Response of Interest Rates to US and UK Quantitative Easing.” _The Economic Journal_ 122 (564): F385–F414. doi:10.1111/j.1468-0297.2012.02554.x. 

- Christensen, J. H. E., and G. D. Rudebusch. 2014. “Estimating Shadow-Rate Term Structure Models with Near-Zero Yields.” _Journal of Financial Econometrics_ 13 (2): 226–259. doi:10.1093/jjfinec/nbu010. 

- Christoffersen, P., C. Dorion, K. Jacobs, and L. Karoui. 2014. “Nonlinear Kalman Filtering in Affine Term Structure Models.” _Management Science_ 60 (9): 2248–2268. doi:10.1287/mnsc.2013.1870. 

- Chundakkadan, R., and S. Sasidharan. 2019. “Liquidity Pull-back and Predictability of Government Security Yield Volatility.” _Economic Modelling_ 77: 124–132. doi:10.1016/j. econmod.2018.07.018. 

- Coroneo, L., K. Nyholm, and R. Vidova-Koleva. 2011. “How Arbitrage-free Is the Nelson–siegel Model?” _Journal of Empirical Finance_ 18 (3): 393–407. doi:10.1016/j. jempfin.2011.03.002. 

- Cortazar, G., E. S. Schwartz, and L. F. Naranjo. 2007. “Termstructure Estimation in Markets with Infrequent Trading.” _International Journal of Finance & Economics_ 12 (4): 353–369. doi:10.1002/ijfe.317. 

- Darbha, G. Estimating the Benchmark Yield Curve. Working Paper Series; Rodney L. White Center for Financial Research; 2003. https://rodneywhitecenter.wharton.upenn. edu/wp-content/uploads/2014/04/0403.pdf . 

- De Pooter, M. 2007. “Examining the Nelson-Siegel Class of Term Structure Models: In-sample Fit versus Out-ofsample Forecasting Performance.” _SSRN Electronic Journal_ . doi:10.2139/ssrn.992748. 

- Diebold, F. X. 2013. _Yield Curve Modeling and Forecasting: The Dynamic Nelson-Siegel Approach_ . Princeton: Princeton University Press. doi:10.1515/9781400845415 

- Diebold, F. X., G. D. Rudebusch, and S. Boragan Aruoba. 2006. “The Macroeconomy and the Yield Curve: A Dynamic Latent Factor Approach.” _Journal of Econometrics_ 131 (1–2): 309–338. doi:10.1016/j.jeconom.2005.01.011. 

- Docherty, P., and S. Easton. 2018. “State-varying Illiquidity Risk in Sovereign Bond Spreads.” _Pacific-Basin Finance Journal_ 50: 235–248. doi:10.1016/j.pacfin.2016.11.003. 

- Duffee, G. R. 2002. “Term Premia and Interest Rate Forecasts in Affine Models.” _The Journal of Finance_ 57 (1): 405–443. doi:10.1111/1540-6261.00426. 

- Duffee, G. R. 2011. “Information in (And Not In) the Term Structure.” _Review of Financial Studies_ 24 (9): 2895–2934. doi:10.1093/rfs/hhr033. 

- Duffie, D., and R. Kan. 1996. “A Yield-factor Model of Interest Rates.” _Mathematical Finance_ 6 (4): 379–406. doi:10.1111/ j.1467-9965.1996.tb00123.x. 

- Dutta, G., S. Basu, and K. Vaidyanathan. 2005. “Term Structure Estimation in Illiquid Government Bond Markets: An Empirical Analysis for India.” _Journal of Emerging Market Finance_ 4 (1): 63–80. doi:10.1177/097265270400400104. 

- Elton, E. J., and T. C. Green. 1998. “Tax and Liquidity Effects in Pricing Government Bonds.” _The Journal of Finance_ 53 (5): 1533–1562. doi:10.1111/0022-1082.00064. 

APPLIED ECONOMICS 667 

- Filipovic, D. 1999. “A Note on the Nelson-Siegel Family.” _Mathematical Finance_ 9 (4): 349–359. doi:10.1111/14679965.00073. 

- Fleming, M., S. Saggar, and S. Sareen Trading Activity in the Indian Government Bond Market. 2016. https://www.new yorkfed.org/medialibrary/media/research/staff_reports/ sr785.pdf?la=en . 

- Fontaine, J. S., and R. Garcia. 2011. “Bond Liquidity Premia.” _Review of Financial Studies_ 25 (4): 1207–1254. doi:10.1093/rfs/ hhr132. 

- Gürkaynak, R. S., B. Sack, and J. H. Wright. 2007. “The U.S. Treasury Yield Curve: 1961 to the Present.” _Journal of Monetary Economics_ 54 (8): 2291–2304. doi:10.1016/j. jmoneco.2007.06.029. 

- Hong, Z., L. Niu, and G. Zeng. 2019. “Us and Chinese Yield Curve Responses to Rmb Exchange Rate Policy Shocks.” _China Finance Review International_ , no. 3. doi:10.1108/ CFRI-12-2017-0239. 

- Julier, S. J., and J. K. Uhlmann. 1997. “New Extension of the Kalman Filter to Nonlinear Systems. In: Signal Processing, Sensor Fusion, and Target Recognition VI.” _International Society for Optics and Photonics_ 3068: 182–194. 

- Kaya, H. 2014. “Does the Level of the Yield Curve Predict Inflation?” _Applied Economics Letters_ 21 (7): 477–480. doi:10.1080/13504851.2013.868582. 

- Lahiri, A. 2020. “The Great Indian Demonetization.” _Journal of Economic Perspectives_ 34 (1), 55–74. https://www.aea web.org/articles?id=10.1257/jep.34.1.55 . 

- Levant, J., and J. Ma. 2017. “A Dynamic Nelson-siegel Yield Curve Model with Markov Switching.” _Economic Modelling_ 67: 73–87. doi:10.1016/j.econmod.2016.10.003. 

- Lin, H., J. Wang, and C. Wu. 2011. “Liquidity Risk and Expected Corporate Bond Returns.” _Journal of Financial Economics_ 99 (3), 628–650. http://www.sciencedirect.com/ science/article/pii/S0304405X10002400 . 

- Longstaff, F. A. 2004. “The Flight-to-liquidity Premium in U.S. Treasury Bond Prices.” _The Journal of Business_ 77 (3): 511–526. doi:10.1086/386528. 

- Luo, X., H. Han, and J. E. Zhang. 2012. “Forecasting the Term Structure of Chinese Treasury Yields.” _Pacific-Basin Finance Journal_ 20 (5): 639–659. doi:10.1016/j.pacfin.2012.02.002. 

- MacKenzie, D. 2006. _An Engine, Not a Camera: How Financial Models Shape Markets_ , 1. MIT Press Books. 

- Malliaropulos, D., and P. Migiakis. 2018. “The Re-pricing of Sovereign Risks following the Global Financial Crisis.” _Journal of Empirical Finance_ 49: 39–56. doi:10.1016/j. jempfin.2018.09.003. 

- McCulloch, J. H. 1971. “Measuring the Term Structure of Interest Rates.” _The Journal of Business_ 44(1): 19–31. https://EconPapers.repec.org/RePEc:ucp:jnlbus:v:44: y:1971:i:1:p:19-31 

- Morales, M. 2010. The Real Yield Curve and Macroeconomic Factors in the Chilean Economy. _Applied Economics_ 42 (27): 3533–3545. 10.1080/00036840802129806 . 

- Nath, G. C., M. Dalvi, and S. P. Singh. 2012. “Predicting Power of Yield Curve – A Study of Indian Sovereign Yield Spread.” _SSRN Electronic Journal_ . doi:10.2139/ssrn.2078920. 

- Nelson, C. R., and A. F. Siegel. 1987. “Parsimonious Modeling of Yield Curves.” _The Journal of Business_ 60 (473). doi:10.1086/296409. 

- Nguyen, D., and T. N. Puri. Systematic Liquidity, Characteristic Liquidity and Asset Pricing. _Applied Financial Economics_ . 2009. 19(11):853–868. doi:10.1080/ 09603100802167254. 

- Nyholm, K., and R. Rebonato. 2008. “Long-horizon Yield Curve Projections: Comparison of Semi-parametric and Parametric Approaches.” _Applied Financial Economics_ 18 (20): 1597–1611. doi:10.1080/09603100701630048. 

- Pastor, U., and R. Stambaugh. 2003. arXiv:10.1086/374184. “Liquidity Risk and Expected Stock Returns.” _Journal of Political Economy_ 111 (3): 642–685. 

- Patel, U. R., S. Chinoy, G. Darbha, C. Ghate, P. Montiel, D. Mohanty, and M. Patra Report of the Expert Committee to Revise and Strengthen the Monetary Policy Framework. Technical Report; Reserve Bank of India, Mumbai; 2014. 

- Piazzesi, M. 2010. “Affine Term Structure Models.” In _Handbook of Financial Econometrics: Tools and Techniques. Volume 1 of Handbooks in Finance_ , 691–766. doi:10.1016/ B978-0-444-50897-3.50015-8. 

- RBI, Macroeconomic and Monetary Developments, Third Quarter Review 2013-14. RBI 2014; http://rbidocs.rbi.org. in/rdocs/Publications/PDFs/MDF2701145070AFA428.pdf . 

- Sarig, O., and A. Warga. 1989. “Bond Price Data and Bond Market Liquidity.” _The Journal of Financial and Quantitative Analysis_ 24 (3): 367. doi:10.2307/2330817. 

- Simon, D. 2006. _Optimal State Estimation: Kalman, H∞ and Nonlinear Approaches_ . John Wiley & Sons, Inc. doi:10.1002/ 0470045345. 

- Steeley, J. M. 2014. “A Shape-based Decomposition of the Yield Adjustment Term in the Arbitrage-free Nelson and Siegel (Afns) Model of the Yield Curve.” _Applied Financial Economics_ 24 (10): 661–669. doi:10.1080/ 09603107.2014.896980. 

- Subramanian, K. 2001. “Term Structure Estimation in Illiquid Markets.” _The Journal of Fixed Income_ 11 (1): 77–86. doi:10.3905/jfi.2001.319292. 

- Swamynathan, V. 2005. _Indian Sovereign Yield Curve Using Nelson- Siegel-Svensson Model. Rakshitra_ . CCIL Monthly Newsletter. October, 14–25. 

- Teixeira, J. C. A. 2007. “An Empirical Analysis of Structural Models of Corporate Debt Pricing.” _Applied Financial Economics_ 17 (14): 1141–1165. doi:10.1080/ 09603100600770994. 

- Umar, Z., Y. Riaz, and A. Zaremba. 2021. Spillover and Risk Transmission in the Components of the Term Structure of Eurozone Yield Curve. _Applied Economics_ 53 (18): 2141–2157. doi:10.1080/00036846.2020.1856322 

- Van Der Merwe, R., and E. A. Wan The Square-root Unscented Kalman Filter for State and Parameter-estimation. In: Acoustics, Speech, and Signal Processing, 2001. Proceedings. (ICASSP’01). 2001 IEEE International Conference on. volume 6; 2001. p. 3461–3464. 

668 S. KUMAR AND V. VIRMANI 

Vayanos, D. 2004. “Flight to Quality, Flight to Liquidity, and the Pricing of Risk.” _National Bureau of Economic Research Working Paper Series_ . doi:10.3386/w10327. 

Xie, C., H. Chen, and X. Yu. 2006. “Yield Curve Estimation in the Illiquid Market: Framework, Models and Empirical Study.” _International Journal of Information Technology & Decision Making_ 05 (03): 467–481. doi:10.1142/s0219622006002064. 

## **Appendix A. Estimation results for** _K[p]_ **,** � **and** _θ[p]_ 

In this section we report the estimation of the _K[p ]_ Matrix (left panel), � Matrix (middle panel) and _θ[p ]_ (right panel) of the different model specifications. Standard errors are reported in the parentheses 

## **Table A1.** NL model. 

|_Kp _Matrix||||�Matrix||_θp_|
|---|---|---|---|---|---|---|
|0.49|0|0|0.0052|0|0|0.082|
|(0.292)|||(.0001)|||(0.004)|
|0|0.138|0|0|0.0086|0|−0.024|
||(0.13)|||(.0003)||(0.013)|
|0|0|1.086|0|0|0.0126|−0.008|
|||(0.481)|||(.0005)|(0.004)|



## **Table A2.** PL model. 

|_Kp _Matrix||||�Matrix||_θp_|
|---|---|---|---|---|---|---|
|0.203|0|0|0.0056|0|0|0.084|
|(0.143)|||(1e-04)|||(0.007)|
|0|0.185|0|0|0.0094|0|−0.024|
||(0.16)|||(3e-04)||(0.013)|
|0|0|1.302|0|0|0.0145|−0.013|
|||(0.527)|||(6e-04)|(0.004)|



## **Table A3.** PL-R model. 

|**Table A3.**PL-R|model.||||||
|---|---|---|---|---|---|---|
|_Kp _Matrix||||�Matrix||_θp_|
|0.565|0|0|0.0058|0|0|0.085|
|(0.294)|||(1e-04)|||(0.003)|
|0|0.18|0|0|0.0096|0|−0.023|
||(0.152)|||(3e-04)||(0.013)|
|0|0|1.173|0|0|0.0138|−0.012|
|||(0.502)|||(6e-04)|(0.004)|



## **Table A4.** LL model. 

|**Table A4.**LL|model.||||||||
|---|---|---|---|---|---|---|---|---|
|_Kp _Matrix|||||�Matrix|||_θp_|
|0.54|0|0|0|0.00545|0|0|0|0.083|
|(0.267)||||(0.00011)||||(0.003)|
|0|0.151|0|0|0|0.00888|0|0|−0.028|
||(0.123)||||(0.00028)|||(0.014)|
|0|0|1.286|0|0|0|0.01426|0|−0.006|
|||(0.499)||||(0.00053)||(0.004)|
|0|0|0|3.195|0|0|0|1|1.524|
||||(0.584)|||||(0.177)|



APPLIED ECONOMICS 669 

**Table A5.** LL-R model. 

|_Kp _Matrix|||||�Matrix|||_θp_|
|---|---|---|---|---|---|---|---|---|
|0.37|0|0|0|−0.00567|0|0|0|0.082|
|(0.228)||||(0.00012)||||(0.004)|
|0|0.165|0|0|0|−0.00958|0|0|−0.019|
||(0.149)||||(0.00032)|||(0.013)|
|0|0|0.772|0|0|0|0.01356|0|−0.012|
|||(0.461)||||(0.00053)||(0.005)|
|0|0|0|1.275|0|0|0|1|1.301|
||||(0.539)|||||(0.303)|



## **Table A6.** PLLL model. 

|_Kp _Matrix|||||�Matrix|||_θp_|
|---|---|---|---|---|---|---|---|---|
|0.57|0|0|0|0.00561|0|0|0|0.084|
|(0.281)||||(0.00012)||||(0.003)|
|0|0.197|0|0|0|0.00921|0|0|−0.026|
||(0.145)||||(0.00029)|||(0.012)|
|0|0|1.238|0|0|0|0.01461|0|−0.008|
|||(0.51)||||(0.00055)||(0.004)|
|0|0|0|3.851|0|0|0|1|1.298|
||||(0.617)|||||(0.152)|



