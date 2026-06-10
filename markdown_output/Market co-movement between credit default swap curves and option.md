International Review of Financial Analysis 82 (2022) 102192 

Contents lists available at ScienceDirect 

## International Review of Financial Analysis 

journal homepage: www.elsevier.com/locate/irfa 

## Market co-movement between credit default swap curves and option volatility surfaces 

## Yukun Shi[a] , Charalampos Stasinakis[a] , Yaofei Xu[a] , Cheng Yan[b][,][1][,][* ] 

a _Adam Smith Business School, University of Glasgow, Glasgow, UK_ b _Essex Business School, University of Essex, Colchester, UK_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_JEL classification:_|We analyze the co-movement between the Credit Default Index (CDX) curve and the S&P 500 index’s option|
|C11|volatility surface. We connect the reduced-form no-arbitrage model with the Nelson-Siegel (N-S) model on|
|C12<br>C13<br>G11<br>G12|hazard rate implied from the CDX curve, and identify the levels, slopes, and curvatures from these two markets<br>via the Unscented Kalman Filter (UKF). We find that the changes in the level, slope, and curvature in the CDX<br>curve and those in the volatility surface are correlated due to the bridge of the S&P 500 index return. Finally, the|
|_Keywords:_<br>Credit default swap|co-movement between the CDX curve and S&P 500 index’s volatility surface become stronger after the late 2000s<br>global financial crisis.|
|Implied volatility||
|Options<br>Unscented Kalman filter||



## **1. Introduction** 

On the relationship between the CDS curve and option pricing, Carr and Wu (2010, 2011) provide the two most interesting empirical papers. In 2010, they jointly model the CDS curve and individual option prices. Their main finding is that the instantaneous default rate has a different diffusion process compared with that of the instantaneous variance rate, while the price of a defaultable option is influenced by the CDS spread, as incorporating default rate in its discount rate. In 2011, they take one step further by using the Unit Recovery Claim (URC) as a bridge to connect deep Out-The-Money (OTM) American put and the CDS spread. They confirm the URCs calculated from the two markets have a strong co-integrated relationship. 

Joint modeling on CDS and options markets shows a better performance, if compared with separately modeling each market (Carr & Wu, 2010). First, the CDS level is highly related to the vol level. As pointed by the URC theory proposed by Carr and Wu (2011), the CDS spread is nonlinearly but positively related to the OIV of default-level deep OTM put option, assuming an existing default level on stock price and the same maturity. Second, the CDS slope is highly related to the vol slope. According to Carr and Wu (2010), the default arrival rate has a time- 

increasing impact on the implied volatility term structure, because of the direct impact of default arrival rate on the risk-neutral drift of asset return. This is consistent with the Merton jump model: At-The-Money (ATM) OIV is the combination of diffusive vol and default arrival rate multiplying an item related to maturity. Hence, option volatility term structure, as the difference between long-term ATM vol and short-term ATM vol is a function of the difference between long-term default rate and short-term default rate relating to CDS slope. Third, the CDS level is related to vol smile skewness. Carr and Wu (2010) also pointed out that the credit risk factor has a higher impact on options at low strikes. Hence, to some extent, the vol smile skewness is driven by the credit risk factor due to its different impacts on option moneyness. 

Given the previous framework, we are motivated to extend the current literature and examine the co-movement between the CDS curve and the OIV surface. To do this, we use the S&P 500 index from January 2002 to December 2017 and apply a parametric model. Parametric models are advantageous, as the extracted variables can provide higher economic interpretation and more tractable time series patterns than those obtained from the non-parametric model (Carr & Wu, 2016). The motivation of this paper mainly starts with Ratner and Chiu (2013) and Da Fonseca and Gottschalk (2014), who examine the relation between 

- Corresponding author. 

_E-mail address:_ Cheng.Yan.1@cass.city.ac.uk (C. Yan). 

> 1 This piece of research is supported by Zhejiang Provincial Natural Science Foundation of China under Grant No: LZ20G010002. 

https://doi.org/10.1016/j.irfa.2022.102192 

Received 18 October 2021; Received in revised form 2 March 2022; Accepted 19 April 2022 Available online 26 April 2022 1057-5219/© 2022 Elsevier Inc. All rights reserved. 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

country-level CDS curves and index-level OIV surface by using Principal Component Analysis (PCA) among major European countries. The methodology of this paper is also following the idea of Natenberg (1994) and Bedendo and Hodges (2009) to apply an Unscented Kalman Filter (UKF) on volatility curve dynamics. In terms of our results, we show that the CDS market is co-moving with the options market due to the bridge of stock return. After controlling for the stock market index return, the moves in the two markets become unrelated or insignificant regardless of market conditions. 

The contribution of this paper is threefold. Firstly, we contribute to the literature by proposing a new way to use the N-S approach by Nelson and Siegel (1987). Although the N-S approach has been used in the literautre to model the CDS curve due to its similarity with the interest rate curve, we link the no-arbitrage model on hazard rate from Carr and Wu (2010) to the N-S model to confirm the rationality of the N-S model on the hazard rate, which may be workhorse model for future studies on this topic. 

Secondly, we contribute to the literature by proposing applying parametric models such as the N-S model and the Deterministic Linear Function (DLF) to confirm the relationship between the CDS curve and OIV surface. Specifically, we evaluate the changes in the level, slope, and curvature between the CDS curve and the OIV surface, and show that the relationship is driven by the common factor, stock return, which provides fresh evidence for the conjecture from the literature such as Ratner and Chiu (2013) and Da Fonseca and Gottschalk (2014). 

Finally, we underline the importance about the co-movement between the CDX curve and S&P 500 index’s volatility surface, especially during crises, which may be foundations for research academic research and practitioners using financial engineering in the industry. 

Our study relates to several strands of literature. Firstly, the prelude of structural models exploring the relationship between asset fundamentals and credit risk starts with the work of Merton (1974). Before the boom of the Credit Default Swaps (CDS) market, the bond markets are the focus of academic and practitioner research. The credit risk information gradually becomes an integral part of this strand of the literature. In a seminal work, Campbell and Taksler (2003) find that equity volatility and credit ratings have similar explanatory power towards the variation of the corporate credit risk premium. In other words, their results confirm that an increase in equity volatility can lead to a rise in the bond risk premium. Collin-Dufresne, Goldstein, and Yang (2012) also show that equity volatility can explain a large amount of variation in the CDS spread level and its changes. The most popular relationship examined is between the 5-year CDS spread and 1-month Option Implied Volatility (OIV) (Benkert, 2004; Forte & Pena, 2009). Especially within the corporate CDS market, ratings play an important role in determining CDS spreads. For example, Aunon-Nerin, Cossin, Hricko, and Huang (2002) point out that the rating is the most important determinant of single-name CDS spreads. In another empirical setting, Berndt and Obreja (2010) postulate that 50% of the variation in European corporate CDS can be captured during the financial crisis through a return-based factor extracted from the by iTraxx Europe CDS index. 

Moreover, there is another strand of literature on the relationships among the CDS spread, stock return, and equity volatility. For instance, Benkert (2004) finds that the OIV has a strong effect on the CDS premium. Alexander and Kaeck (2008) suggest that the CDS spread is more sensitive to the equity volatility rather than the stock return during volatile periods. Under normal market conditions, the interest rate is also found to influence the Credit Default Index (CDX) across different industries, except for the financial services sector. Other researchers, such as Breitenfellner and Wagner (2012), provide evidence that stock return and implied equity volatility can explain particularly the variation in the change of the aggregate CDS spread. Global financial variables can also explain part of this variation (Ang & Longstaff, 2013; Longstaff, Pan, Pedersen, & Singleton, 2011). According to Breitenfellner and Wagner (2012), the liquidity risk is assumed to affect the financial industry but has no relation with non-financial industries. They 

find stock volatility has no predominant impact on CDS spread changes compared with the stock return, which contrasts with Alexander and Kaeck (2008). Finally, Ismailescu and Phillips (2015) postulate that CDS trading initiation normally increases the domestic stock market volatility and variance risk premium. Other studies focus on the leading relationship between CDS, stocks, and options markets. Narayan, Sharma, and Thuraisamy (2014) explore the price discovery between the CDS and equity market and prove that equity has a leading role in most sectors. Hilscher, Pollet, and Wilson (2015) explain that information is firstly reflected in the equity market and then fully disclosed in the CDS market. 

In addition, there is another strand of literature on the relationship between stocks, options, and CDS markets with risk-based models incorporating the Equity Risk Premium (ERP), Variance Risk Premium (VRP), and Credit Risk Premium (CRP). There is a consensus that ERP is related to investors’ risk aversion, which changes within different business cycles (Haugen & Baker, 1996). Links between risk aversion and option prices are also established in the literature, as in the work of Bliss and Panigirtzoglou (2004). The authors show that the degree of risk aversion is low when market volatility is high. Others find that VRP is closely related to CRP. For example, Zhou (2018) and Buraschi, Trojani, and Vedolin (2014) recognize that the market VRP has a positive effect on the aggregate credit spread index. Finally, the seminal work of Carr and Wu (2016) proves that the VRP should be accounted, when it comes to estimations of the ERP. Specifically, as the correlation between return − innovation and variance innovation gets close to 1, the VRP becomes the main contributor to the ERP. 

Finally, some studies further take into account the macroeconomic factors in the modeling of the co-movement of these three markets. For instance, Longstaff and Schwartz (1995) show that the interest rate can influence the credit spread, thus an increase in the interest rate can boom the risk-neutral drift in asset value. This, in consequence, is reducing the Merton-style default probability and decreasing the CDS spread. Collin-Dufresne, Goldstein, and Martin (2001) point out that the slope of interest rate term structure is a measure of uncertainty in the economy. Glatzer and Scheicher (2005) also examine how economic news, stock markets, and risk premium impact the option-implied probability density function. Wu and Zhang (2008) use three Kalmanfiltered extracted macroeconomic factors, namely inflation, real output, and financial market volatility, which are found to explain more than 50% of the variation in different-rating CDS spreads. 

The remainder of the paper is structured as follows. Section 2 describes the data and presents summary statistics together with methodology. Section 3 describes the methodology and Section 4 provides the calibration and main empirical results. Section 5 concludes. The technical details regarding linking the no-arbitrage model with the N-S method are shown in the Appendix A, while further robustness checks are delegated to online appendices. 

## **2. Data** 

The CDS curve and OIV surface data construction and collection are summarized in this section. The systematic synthetic CDX index is constructed by all American companies’ CDS that have ratings above BBB from 01/01/2002 to 29/12/2019, due to the reason of data availability. The individual companies’ CDS data is accessed from Markit in WRDS. The CDS spread is selected under MR and MR14 clauses, which reduces the pricing error with a fixed recovery rate. The rating information for each company is collected from Markit implied equity rating. Wednesday is set as the collection day during each week, as 

2 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

Wednesdays’ observations are found to be the ones with the highest liquidity within a week. Following this process, we obtained 939 weekly observations for the full period. We only select companies with a rating above BBB as investment level on each Wednesday.[2 ] In the case that Wednesday is a holiday, we account for the same rating from the previous working day. Then, for each maturity, we calculate the average of all available CDS as the CDX spread for specific maturities. 

Regarding the OIV surface, we collect option data for the S&P 500 index from Option Metrics in WRDS from 01/01/2002 to 29/12/2019. The maturities of the option contracts are selected with a minimum of 8 days. The data includes closing bid/ask quotes, volume, strike prices, expiration dates, Greeks (delta, gamma, and vega), and implied volatility (mid quote). Several exclusionary criteria are applied to filter out option observations. Firstly, options that do not meet basic no-arbitrage conditions are eliminated. Secondly, option contracts with zero open interest are excluded. During constructing the OIV surface, we follow the local smoothing interpolation of Carr and Wu (2020). The implied volatility of In-The-Money (ITM) option contracts is unreliable compared to the OTM ones.[3 ] Hence, to determine the implied volatility with specific strike and maturity, we use the weight of 1 minus absolute forward delta from its corresponding implied volatility quote. In the case of deep ITM options with an absolute forward delta of more than 0.8, 100% weight is put on the OTM implied volatility. 

After applying the bivariate Gaussian kernel, we obtain the implied volatility at a fixed moneyness (K/S)-maturity grid as shown in panel A of Table 1 below. 

The presented results in panel A come from a grid of K/S ranging from 0.8 to 1.2 and maturity ranging from 1 month to 2 years summa- 

**Table 1** 

Average behavior of OIV surface and CDX curve. 

||K/S<br>Maturity|0.8<br>0.9<br>1<br>1.1<br>1.2<br>A. Average OIV|
|---|---|---|
||1<br>2<br>3<br>6<br>12<br>24<br>Maturity|33.8311<br>24.5707<br>17.9981<br>15.9174<br>17.9967<br>29.9745<br>23.1404<br>17.7126<br>15.2526<br>15.8135<br>28.4712<br>22.5774<br>17.7745<br>15.2395<br>15.1505<br>26.1664<br>21.9052<br>18.2314<br>15.6442<br>14.6210<br>24.7841<br>21.6104<br>18.8155<br>16.4980<br>15.0295<br>24.0409<br>21.5402<br>19.3741<br>17.4628<br>15.9199<br>B. Average CDX spread<br>1y<br>2y<br>3y<br>5y<br>7y<br>10y<br>0.4971<br>0.5796<br>0.6793<br>0.8780<br>0.9981<br>1.0980|



_Notes:_ Average OIV and CDX spreads are showed in % in Panel A and B respectively. The summary statistics are calculated from a matrix grid of 5 fixed moneyness (K/S) and 6 fixed maturity (months). Each time series has 835 weekly observations from January 2002 to December 2019. 

> 2 As the option part is from S&P 500 index, all selected firms are considered large companies. Hence, the CDS part should be also investment-level. Typically, the literature suggests that investment-level ratings are those above BBB (Carr & Wu, 2011). 

> 3 According to Put-Call parity, an ITM call/put option can be replicated by some shares of stock, an OTM put/call option and a zero-coupon bond. Hence, the volatility information should be same for the OTM/ITM options with same strike price and maturity, under a complete market. However, there are severe liquidity issues and transaction costs in individual option markets. The higher big-ask spread indicates that the fair ‘true’ price may be far from the quoted middle price. As ITM options are traded with non-zero intrinsic price and time price, they are more expensive than OTM options by providing less leverage for investors or speculators. Hence, investors tend to trade OTM options with higher leverage effect and hence result in higher liquidity for OTM options. Therefore, we argue that the volatility information is more reliable in OTM options. 

rized. In that grid, we calculate the average OIV. Volatilities at low strikes are much higher than those at high strikes, which is the pattern of negative skewness at the volatility smile. On average, the implied volatility of ATM options is found to increase with higher maturity, while implied volatility of deep OTM puts (calls) decreases with higher maturity. The table also presents the average CDX spread curve in panel B. The CDX spread is notably increasing, as maturity increases. For example, it is obvious that the average 1-year CDX spread is 0.4971% and the equivalent 10-year one is 1.0980% accounting for the whole sample. 

## **3. Methodology** 

In this section, the methodology framework is summarized. Initially, we discuss the application of the DLF in modeling volatility. Then, we explain the use of UKF for the parameter calibration of the co-movement of the CDX spread and OIV surface. 

## _3.1. Deterministic linear function (DLF)_ 

We follow Carr and Wu (2020) to obtain a fixed grid of volatility surface. Assuming the moneyness _x_ (K/S) and maturity _τ_ , we obtain the OIV surface with a fixed moneyness-maturity grid ( _x_ , _τ_ ). First, we consider the OTM quote more reliable than the ITM, as mentioned before. At each point ( _xi_ , _τj_ ), the weight of call or put is the value of one minus the absolute value of its corresponding forward delta. Second, the volatilities of deep ITM options are not considered reliable. Hence, the weight is set as zero, when the absolute value of the forward delta of the quote is above 0.8. Then, the fixed moneyness-maturity grid of the volatility surface is calculated based on an independent bivariate Gaussian kernel with default bandwidth. The target volatility is calculated from the observed volatilities with weights of its distance in the moneyness dimension and log maturity dimension. Non-parametric kernel fitting on the volatility surface is widely accepted by academics (Carr & Wu, 2010; Cont & Da Fonseca, 2002). Hence, the volatility surface with a fixed moneyness-maturity grid is constructed as follows: _K_ α = _log_ = _log_ ( _x_ ) (1) ( _S_ ) _wi_ = (1 −| _δi_ | ) _I_ | _δi_ |〈0 _._ 8 • _e_ − ( _αi_ 2− _h_[2] _xα_ )[2] • _e_ − ( _ln_ ( _τi_ )2− _hτ_[2] _ln_ ( _τ_ ) )[2] (2) 

where α is the logarithm of moneyness, _wi_ is the weight on each contract i, _δi_ is the BMS forward delta of option contract i, and _hα_ , _hτ_ are the default bandwidths related to the variation in the sample’s logarithm of moneyness and logarithm of maturity separately. 

Conceptually, here it should be noted that the traditional thinking of volatility surface is a surface rather than volatility dots plotted at a twodimension grid (maturity, strike price, or moneyness). In the real market, we can only observe the bid/ask prices of the options contracts with specific strike prices and maturity dates. We use the Black-Scholes model to back out the implied volatilities for each option contract, by using their mean prices. But at this stage, we only know the implied volatilities for the existed option contracts, but not for implied volatility with any arbitrary maturity or moneyness. With the change in time or stock price, the implied volatilities for a specific option contract change its maturity or moneyness. Hence, it is necessary to figure out the implied volatilities with fixed moneyness and maturity for research purposes. 

The problem becomes how to obtain the whole volatility surface conditional on the known implied volatilities with specific maturity and moneyness. There is a popular way in the industry currently to deal with the problem, namely kernel fitting, especially the bivariate Gauss Kernel fitting applied in this paper. The core idea is that implied volatility with any specific arbitrary maturity or moneyness is a weighted average one of all known implied volatilities, of which the weight depends on the 

3 

_Y. Shi et al.                                                                                                                                                                                                                                      International Review of Financial Analysis 82 (2022) 102192_ 

distance between maturity/moneyness of target and those of known one. Formula (1) stands for the moneyness variable, while Formula (2) stands for the weight explained above. Hence, Formulas (1) and (2) are explained as formulas of bivariate Gauss kernel fitting to obtain the implied volatilities with fixed moneyness and maturity for the implied volatility surface. The obtained implied volatilities after using bivariate Gauss kernel fitting are regarded as observable and prepared for the following steps.[4 ] 

Based on the above, we set a weighting scheme to obtain the fixed moneyness-maturity grid of volatility surface. Here, the fixed moneyness is set to 0.8, 0.9, 1.0, 1.1, and 1.2, while the maturity is 1-month, 2- month, 3-month, 6-month, 1-year, and 2-year. Therefore, there are 30 fixed moneyness-maturity volatilities at each observation date. The next step is to apply the DLF, which is proved to be a good method for modeling the volatility surface. Goncalves and Guidolin (2006) compare many alternative models for modeling the volatility surface. Their results find that the DLF is more robust compared to other models. Similarly, Bernales and Guidolin (2014) apply this DLF to model both the volatility surface of individual stock and index. The DLF calculations assume a continuous dividend rate as follows. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-03.png)



![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-04.png)


> where _σi_ , _j_ is the implied volatility at moneyness _xi_ and maturity _τj_ , _b_ 0 is considered as the level of whole volatility surface, j is the number of implied volatility with specific maturity and moneyness from 1 to 30 because we have 6 maturities and 5 moneyness. _b_ 1 is regarded as the slope of the smile, _b_ 2 captures the curvature of the moneyness dimension, _b_ 3 captures the slope of the maturity dimension and _b_ 4 captures the possible relationship between moneyness and maturity. As bivariate Gauss kernel fitting helps us to obtain the volatility surface, the dimension of it is still too high for quantitative analysis. Formulas (3) and (4) are determinant liner function (DLF), which is a more parsimonious model for modeling the volatility surface, with limited but meaningful parameters. Among Formula (4), r is the risk-free rate and q is the dividend. 

## _3.2. Unscented Kalman filter (UKF)_ 

To examine the co-movement between the CDX curve and the OIV surface, we need to filter the time series of parameters inferred from the N-S model and the DLF. Due to the linear feature in both states and the measurement propagation, the UKF is applied to obtain the hidden states driving the movements of the CDS curve and volatility surface.[5 ] 

Firstly, the five hidden states in the DLF are equivalent to the features in the volatility surface. The state-space model is Gaussian linear in both state and measurement propagation. Hence, the UKF is appropriate to deal with this linear relationship (Julier and Uhlmann, 1997). Thus, we estimate the following. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-09.png)



![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-10.png)


> 4 The default bandwidth is estimated as **h** = **c** • ( **34** _**N**_ ) **1** _/_ **5** , where c = 3 and N is the number of real implied volatilities. 

> 5 For the linear model specification, the Kalman filter (KF) provides a very close performance with the Unscented Kalman filter (UKF). The performance or estimation results only changes significantly by changing the model specification from linear to non-linear, of which UKF will perform better because of better capturing the nonlinear relationship. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-13.png)



![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-14.png)


where _yt_ ∈ ℝ[30 ] denotes the log-normal of 30 implied volatility quotes of fixed moneyness and dimension on date t; _h_ ( _Xt_ ) is the function to calculate the logarithm of volatility by using parameters _Xt_ , which can be solved by DLF. 

Secondly, the three hidden states of the N-S model are viewed as the level, slope, and curvature of the term structure. The state-space model is also Gaussian linear in both state and measurement propagation, as before. Following a similar logic, we apply the UKF as below 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-17.png)



![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0004-18.png)


where _yt_ ∈ ℝ[6 ] denotes the hazard rates inferred from the CDX quotes of fixed maturity on date t, with 1-year, 2-year, 3-year, 5-year, 7-year, and 10-year; _h_ ( _Xt_ ) applies the N-S model to calculate the hazard rate by using hidden states including level, slope, and curvature. We also assume that the pricing errors of hazard rates are independent and identically distributed (iid), but with the same error variance. The pricing errors of hidden states are also considered to be iid, but with different error variances. 

In order to provide further context on the equations above, we note that hazard rate and the corresponding term structure change over time. The core ideas for Formulas (5)–(8) and (9)–(12) are similar. We use parameter models (DLF and N-S models) to model the observed implied volatility surface and CDS term structure within a state-space model framework. That is through minimizing the errors between model-based observations with real observations to obtain the time-series of the model parameters. Formulas (5)–(8) are the state-space model specification for volatility surface dynamics. Formula (5) is the model-based parameter set (states); Formula (6) is the propagation function of states; Formula (7) is the kernel fitted volatilities (measurements); Formula (8) is the propagation function of measurements. Formulas (9)– (12) are the state-space model specification for hazard rate term structure dynamics similarly defined as in Formulas (5)–(8). 

To begin this estimation by using the UKF, we identify 6(4) auxiliary parameters for the covariance of states and measurements in DLF (N-S model). As pointed by Carr and Wu (2016), a large magnitude of covariance in the state-propagation compared with that in the measurement-propagation is a point of interest. Namely, the hidden states move in high variation to quickly capture the variation in measurements. Finally, the maximum likelihood method is applied to calculate the minimum square of the estimated errors. This will allow us to obtain the optimal evolving speed and the auxiliary parameters.[6 ] 

> 6 Traditional estimation methods like OLS will not provide robust results. The main reason for this is that the number of observations is small compared with parameters needed for estimation, especially for CDS spreads. At each time, we have only 6 CDS spreads but we need to estimate 3 parameters, which will result in a high estimation error by using OLS (more unreliable parameters). To account for this, we apply a state-space model specification with UKF estimation. 

4 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

## **4. Calibration and empirical results** 

This section summarizes all the empirical findings of this study. Initially, the model calibrations and pricing performances are presented. Then, we examine the relationship between the parameters extracted from two markets. Finally, empirical regressions evaluating the interaction between the two markets are estimated over both our full sample and the subsamples related to the late 2000s global financial crisis, given the fact that the late 2000s global financial crisis has substantially changed the financial landscape (Fuertes, Phylaktis, & Yan, 2016, 2019; Yan, Phylaktis, & Fuertes, 2016). 

## _4.1. Model performance and calibration_ 

The first step of the empirical analysis is to obtain the model pricing performance on the OIV surface and the CDX curve. These results are shown in the following table. 

Table 2 is split into several panels. Panel A is an implied volatility grid that reports the average pricing error in the OIV surface through a matrix of 30 fixed moneyness-maturity values. The pricing error is defined as the difference between the observed volatility quotes and the model calibrated ones. We observe the higher pricing error at the shortest maturity (1-month), namely for the deep OTM (K/S = 0.8) at around − 4.02%. Observing the K/S dimension, it is also clear that the lowest pricing error is observed at the ATM level (K/S = 1). Panel B illustrates the explained variation in 30 time series of fixed moneynessmaturity implied volatilities. In this case, the explained variation is defined as 1 minus the ratio of the variance of error by the variance of observed implied volatility. As expected, these results are consistent with those of Panel A. Thus, the explained variation is at its lowest in the 1-month maturity cross the maturity dimension and at its highest in the ATM case cross the volatility smile. For investors, the result is consistent with that the variance risk premium is higher among shorter maturity and higher among out-of-money options. 

In terms of the last two panels of Table 2, panels C and D report the average pricing error and explained variation in the CDX curve. Most absolute pricing errors across different maturities (1 year to 10 years) of the CDX curve are around 1 basis, as shown in panel C. Comparing with the explained variation in the volatility surface (average of 98.5% across all fixed grids), this ratio in the CDX term structure is found to be a bit higher (averagely 99.5% across all maturities). Carr and Wu (2010) explain that shocks to variance rate have a stronger impact on shortterm options and CDS spread compared to their long-term counterparts. Also, shocks to the default rate bring forward a long-term impact on all options and CDS spread. In conclusion, the results show that volatility is more volatile compared with the CDS spread. It is normal to show next what parameters are estimated by the application of UKF on DLF and N-S. We summarize these into the following two figures. 

Fig. 1 shows the time series of parameters estimated by applying the UKF on the DLF. _b_ 0 stands for the level of volatility surface. It is clear that _b_ 0 stays at a high level around the 2003 and 2009 financial crisis period. After 2013, the market is booming and _b_ 0 is consistently kept at a lower level. _b_ 2 shows a negative relation with _b_ 0, following similar patterns during recession and growth periods. The equivalent parameters are shown for the case of N-S in Fig. 2 above. There is a similar pattern of _β_ 0 compared with that in the volatility surface. Namely, _β_ 0 estimates are high during the financial crisis period. In the case of N-S, though, _β_ 1 and _β_ 2 also shares a similar pattern on average. Observing the parameters’ fluctuation, the UKF calibrated values for the N-S model appear smoother than those for the DLF. This can be explained by the fact that Carr & the OIV is less persistent than the CDS spread at the firm level ( Wu, 2010). 

delve deeper and examine what they mean for the interactions between the OIV surface and the CDS curve. To achieve this, changes in the variables are defined as follows, according to the N-S model. Δ _β_ 0 is regarded as ΔCDS1, Δ _β_ 1 is viewed as ΔCDS2 and Δ _β_ 3 is used as ΔCDS3. Equivalently for the DLF, Δ _b_ 0 is remarked as ΔVOL1, Δ _b_ 1 is flagged as ΔVOL2 and Δ _b_ 2 is used as ΔVOL3. Conceptually, the above-defined changes in the parameters are crucial and therefore, their economic meaning needs to be explained. . Thus, ΔVOL1 (ΔCDS1) captures the changes in the level of OIV surface (CDX curve), while ΔVOL2 (ΔCDS2) highlights changes in the slope of the volatility smile (CDX curve). ΔVOL3 (ΔCDS3) identifies the changes in the curvature of the volatility smile (CDX curve). When PCA is applied, then these three changes can explain at least 90% of the variations in the changes of the whole volatility surface or CDX curve (Da Fonseca & Gottschalk, 2014). The following table summarizes the correlation analysis for the above parameters. 

The Pearson pairwise correlation coefficients between the parameters (change of the parameters) and S&P 500 index return in the full sample are presented in panel A (B). From panel A, it is obvious that the index return is negatively related to most parameters. The level of the volatility surface ( _b_ 0) shows a significant positive relationship with the level, slope, and curvature of the CDS curve, which are 0.64 ( _β_ 0), 0.38 ( _β_ 1) and 0.67 ( _β_ 2) respectively. Additionally, the slope of the smile has a strong positive relationship with the slope and curvature of the CDS curve, with correlation coefficients around 0.67 and 0.79. The curvature of the moneyness dimension is found negatively correlated with the level and the curvature of the CDS curve. The results of panel B are more interesting, as we are focusing on the co-movement of the two markets. We find that changes in the level of volatility surface have the highest positive Pearson correlation with the changes in the level of the CDX curve (0.36), while insignificant correlation values are found with the − changes in the slope ( 0.01). It is interesting to note, though, that when the index return is added, high correlation coefficients are observed between itself and the changes in the level/slope of the volatility surface (− 0.80 and − 0.18) and changes in level and curvature of the CDS curve (− 0.44 and − 0.13). Further results for the period before, during, and after the financial crisis are presented in our online Appendix A and are available upon request. 

## _4.3. Co-movement between CDS curve and OIV surface (full sample)_ 

After the previous steps, we are now ready to analyze what drives the potential co-movement between the CDS and the option markets, by focusing on the change of previously mentioned parameters. In this subsection, the full sample of the data is used. We construct regressions based on the first three main factors given their contribution to variation.[7 ] Hence, we incorporate the log return of the S&P 500 index as our control variable. The regressions are constructed as follows. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0005-13.png)


## _4.2. Interactions between OIV surface and CDS curve_ 

Given the obtained parameters presented above, it is important to 

> 7 Da Fonseca and Gottschalk (2014) point out the changes in the level, slope and curvature are three main contributions for changes in both the CDS curve and OIV surface. 

5 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

**Table 2** 

Model pricing performance on OIV surface and CDX curve. 

||K/S<br>0.8<br>Maturity<br>A. Averag|0.9<br>1<br>1.1<br>1.2<br>e pricing error in OIV surface||
|---|---|---|---|
||1<br>−4.0214<br>2<br>0.6335<br>3<br>1.5597<br>6<br>1.3099<br>12<br>0.2650<br>24<br>−1.9424<br>Maturity<br>B. Explain<br>1<br>0.9369<br>2<br>0.9909<br>3<br>0.9903<br>6<br>0.9698<br>12<br>0.9758<br>24<br>0.9703<br>C. Average<br>Maturity<br>1y<br>0.0060<br>D. Explain<br>0.9985|1.0207<br>−0.1198<br>−0.2434<br>1.8466<br>1.3055<br>−0.4308<br>−1.0655<br>0.2259<br>1.3041<br>−0.3935<br>−1.1738<br>−0.3251<br>1.0834<br>−0.0175<br>−0.8950<br>−0.7586<br>0.6576<br>0.3553<br>−0.1461<br>−0.2491<br>−0.4807<br>0.2292<br>0.4872<br>0.6310<br>ed variation in OIV surface<br>0.9734<br>0.9687<br>0.9772<br>0.9618<br>0.9848<br>0.9882<br>0.9915<br>0.9734<br>0.9889<br>0.9939<br>0.9948<br>0.9766<br>0.9830<br>0.9940<br>0.9924<br>0.9779<br>0.9826<br>0.9904<br>0.9928<br>0.9897<br>0.9932<br>0.9947<br>0.9937<br>0.9934<br>pricing error in CDX spread<br>2y<br>3y<br>5y<br>7y<br>−0.0082<br>−0.0101<br>0.0139<br>0.0087<br>ed variation in CDX spread<br>0.9974<br>0.9980<br>0.9951<br>0.9968|10y<br>−0.0106<br>0.9969|



_Notes:_ Pricing errors in OIV and CDX spreads are showed in % in Panel A and B respectively. The summary statistics are calculated from a matrix grid of 5 fixed moneyness (K/S) and 6 fixed maturities (maturities are monthly data, Panel B reports the explained variation in OIV surface and Panel C shows average pricing error in CDX spread). Each time series has 835 weekly observations from January 2002 to December 2019. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0006-06.png)


**----- Start of picture text -----**<br>
1.5<br>1 b0 b1 b2<br>b3 b4<br>0.5<br>0<br>-0.5<br>-1<br>-1.5<br>-2<br>-2.5<br>**----- End of picture text -----**<br>


**Fig. 1.** UKF fitted parameters in the DLF. _Notes:_ This figure shows the time-series pattern of parameters in the DLF calibrated by UKF. using the full sample. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0006-08.png)


**----- Start of picture text -----**<br>
0.06<br>0.05 β0<br>β1<br>0.04 β2<br>0.03<br>0.02<br>0.01<br>0<br>-0.01<br>-0.02<br>-0.03<br>-0.04<br>date2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019<br>**----- End of picture text -----**<br>


**Fig. 2.** UKF fitted parameters in the N-S model on Hazard rates. _Notes_ : This figure shows the time-series pattern of parameters in the N-S model as calibrated UKF using the full sample. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0006-10.png)


where _N_ = 1, 2, 3 

The first three regressions account for the changes in the level/slope/ curvature of the CDS curve as dependent variables and the volatility surface ones as predictors. The last three regressions have an opposite setup. This approach allows us to evaluate whether changes in the level/ slope/curvature of one market are significant and influence those of the other market by controlling for the effects of the index return. Hence, we incorporate the log return of the S&P 500 index as our control variable. All the results are summarized in the following tables. 

The regression coefficients show the magnitudes of the relationship between the changes in the level/slope/curvature in two markets. The adjusted R[2 ] shows the variation of changes in the level/slope/curvature of one market explained by those of another, after accounting for the index return. All the t-statistics have been adjusted by the Newey-West estimator (Da Fonseca & Gottschalk, 2014). Focusing on Table 4, ΔVOL1 has the highest explanatory power on ΔCDS1, with an adjusted R[2 ] of 13.01%. This is substantially higher if compared with the respective values for ΔVOL2 and ΔVOL3 that are around or below 1%. The log return of the S&P 500 index is found to explain 19.06% of the variation in ΔCDS1. Accounting for all variables and seeing the increase in the adjusted R[2] , we conclude that the index return is the most significant variable, while the other three variables extracted from the volatility surface become insignificant and economically not important. This is in line with the suggestions of Ratner and Chiu (2013) and Da Fonseca and Gottschalk (2014) that these two markets cross-section due to their relationship with the stock return. 

Table A1 in our online appendix illustrates the results between the changes in the slope of the CDS curve and changes in the level/slope/ curvature of volatility surface. From the regression result of ΔCDS2 on ΔVOL1, ΔVOL2, and ΔVOL3, changes in volatility surface cannot explain the movement in the slope of the CDS curve. Index return 

6 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

accidentally shows an insignificant and negative relation with ΔCDS2, with an extremely low adjusted R[2] . This is expected as the low correlations observed in panel B of Table 3. 

Finally, Table A2 in our online appendix shows the relationship between the changes in the curvature of the CDS curve and the changes in the level/slope/curvature of the volatility surface. ΔVOL1 and ΔVOL2 coefficients are found to be statistically significant and positive, while the index return is highly significant and indicates a strong negative impact on ΔCDS3. However, all of them can only explain a low proportion of variation of ΔCDS3. The higher adjusted R[2 ] is found when accounting for all variables, but in that case, only the index coefficient remains significant. 

The following tables present the opposite regression setup, where the changes in the level/slope/curvature of the volatility surface are the dependent variables, and those of the CDS curve are the independent ones. 

Table 5 presents a significant finding, namely that a 1% increase in ΔCDS1 can result in a 35% increase of ΔVOL1 which is also accompanied by an adjusted R[2 ] of 13.01%. The index return is also highly significant and affects ΔVOL1 negatively, where a 1% increase in stock return will result in a − 2.41% change in volatility level. The respective adjusted R[2 ] is also very high (63.98%). The explained variation on ΔVOL1 increases less than 0.5% by adding all three changes in the CDS curve. When including all parameters, ΔCDS1 stops being significant, while ΔCDS2 and ΔCDS3 are found to affect ΔVOL1negatively, while the index return remains significant and affects the dependent variable negatively. 

In Table A3 in our online appendix, ΔCDS1 and ΔCDS3 are positively and significantly related to ΔVOL2, but with low explanation power. After controlling for the stock market index return, all of them are not significant, the index return coefficient sign remains negative and highly significant, but the adjusted R[2 ] remains in low values. Finally, in Table A4 in our online appendix, the index return is still significant with ΔVOL3. ΔCDS1’ s coefficient remains across the three regressions highly re- significant and with a negative sign, but the respective adjusted R[2 ] mains low at values around 1%. 

Accounting for all the previous results, changes in the levels of the two markets can be explained by each other, but these interactions become insignificant after controlling for the stock market index return. In terms of explained variation of the changes in the level of two markets, index return can capture 64% of changes in the level of the volatility surface, but only 19% in that of the CDS curve. Co-movements between changes in the slope/curvature among the two markets become weaker after controlling for the stock market index return. Carr and Wu (2010) point out instantaneous default rate has no relation with instantaneous variance rate, which shows market segmentation between the CDS and the option market. Their finding supports changes in the level of the CDS curve and OIV surface are driven by two different Brownian motions separately. From the result in the full sample, index return can explain more on changes in the level of volatility surface ( _R_[2] , 63.98%), compared with that of the CDX curve ( _R_[2] , 19.06%). The results show that, these two markets are not separately driven by their own factors but having a correlation mutually with stock return. By using stock as a hedging tool, the risk in the option market can be more 

efficiently hedged compared with that in the CDS market, especially the changes in the level of two markets; the risk in changes of slope and curvature in two markets cannot be efficiently hedged by stock. In general, with the above results, we posit a similar view to Ratner and Chiu (2013) and Da Fonseca and Gottschalk (2014) regarding the potential interactions between the CDS and the option market. They apply PCA as a non-parametric method to select the factors that can affect changes in the CDS curve and volatility surface. This approach is parametric, and despite most papers, we focus on the changes of the parameters rather than their levels.[8 ] 

_4.4. Co-movement between CDS curve and OIV surface (financial crisis period)_ 

In this section, we focus on the results we obtain accounting for the Da Fonseca and financial crisis period. This is motivated by the fact that Gottschalk (2014) find that the two markets in European countries interact much stronger during crises and call this interaction ‘crossmarket hedge’, when using the three extracted factors from each market. Following the logic of the previous sub-section, we present the following three tables for the regressions accounting for the late 2000s global financial crisis period. 

Table 6 shows how much variation in ΔCDS1 is explained by factors in the volatility surface and index return during the crisis. The directions Table 4. More- of impacts are consistent with the findings presented in over, ΔVOL1 can explain 23.49% variation in ΔCDS1 with a coefficient of 0.0072, which is much higher than the 13.01% variation and coefficient 0.0037 in Table 4. Δ VOL1 coefficient becomes insignificant when accounting for all parameters and controlling for the stock market index return. 

Tables A5 and A6 in our online appendix show how changes in slope/ curvature in the CDS curve can be explained by those in the volatility surface controlling for the stock market index return during the crisis. Table A5 is consistent with the picture painted by Table A1. Although Δ VOL1 and index return appears to be significant and negative in sign, the adjusted R[2 ] suggests that only a very small amount of variation in the changes of the CDS curve slope can be captured by these factors. From Table A6, the correlation coefficient between changes in the curvature of the CDS curve and the factors in volatility surface are attributed to the negative effect coming from the index return. Comparing with Table A2, the information in the volatility surface can provide a little higher explanation on the change in the curvature of the CDS curve during the late 2000s global financial crisis period. As in the previous section (Table 5, Tables A3 & A4), the following three tables illustrate how each extracted factor in the volatility surface is explained by those in the CDS within the crisis period. 

Table 7 shows the impact of ΔCDS1 on ΔVOL1 does not change significantly compared with Table 5, while the explained variation increases from 13.01% to 23.49%. After controlling for the stock marketindex return, ΔVOL1 is significant and contributes more additional explanation on explaining ΔCDS1 in financial crisis period comparing with no relation in the full sample. That is, if factors in the CDS curve can explain those in the volatility surface, their significance erodes as we control for the stock market index return. Moreover, index return can 

> 8 Ericsson et al., (2009) examine traditional variables to explain variation in CDS premium and find that leverage and volatility can explain a high proportion in variation of CDS spread. They point out that between 6.9% and 14.4% variation of changes of 5-year CDS spread can be explained by changes in implied volatility with different quotes/rating. They also find that between 23.9% and 29.7% variation of 5-year CDS spread level can be explained by implied volatility. Tang et al. (2010) use average implied volatility of ATM S&P 500 index options as a proxy for the volatility of economic growth. Their results suggest that the implied volatility of ATM S&P 500 index option has a higher explanatory power on CDS spread, compared with GDP growth volatility. 

7 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

## **Table 3** 

Correlation coefficients between Factors and S&P 500 index return (full sample). 

||Panel A: correlation coeffcient in parameters<br>b0<br>b1<br>b2<br>b3<br>b4<br>β0<br>β1<br>β2|
|---|---|
||b1<br>0.52<br>***<br>b2<br>−0.75<br>***<br>−0.10<br>***<br>b3<br>−0.70<br>***<br>−0.56<br>***<br>0.31<br>***<br>b4<br>0.71<br>***<br>0.45<br>***<br>−0.70<br>***<br>−0.47<br>***<br>β0<br>0.64<br>***<br>0.05<br>−0.56<br>***<br>−0.17<br>***<br>0.32<br>***<br>β1<br>0.38<br>***<br>0.67<br>***<br>−0.03<br>−0.60<br>***<br>0.48<br>***<br>−0.13<br>***<br>β2<br>0.67<br>***<br>0.79<br>***<br>−0.45<br>***<br>−0.55<br>***<br>0.75<br>***<br>0.08<br>**<br>0.68<br>***<br>return<br>−0.17<br>***<br>−0.05<br>0.03<br>0.19<br>***<br>−0.05<br>−0.04<br>−0.02<br>−0.05<br>*<br>Panel B: correlation coeffcient in changes of parameters<br>Δb0<br>Δb1<br>Δb2<br>Δb3<br>Δb4<br>Δβ0<br>Δβ1<br>Δβ2<br>Δb1<br>0.13<br>***<br>Δb2<br>−0.21<br>***<br>0.39<br>***<br>Δb3<br>−0.84<br>***<br>−0.11<br>***<br>0.13<br>***<br>Δb4<br>0.33<br>***<br>−0.26<br>***<br>−0.36<br>***<br>−0.16<br>***<br>Δβ0<br>0.36<br>***<br>0.07<br>**<br>−0.11<br>***<br>−0.27<br>***<br>0.12<br>***<br>Δβ1<br>−0.01<br>0.00<br>0.02<br>0.02<br>0.10<br>***<br>0.07<br>**<br>Δβ2<br>0.07<br>**<br>0.05<br>*<br>0.04<br>−0.05<br>0.00<br>0.01<br>−0.18<br>***<br>return<br>−0.80<br>***<br>−0.18<br>***<br>0.13<br>***<br>0.62<br>***<br>−0.23<br>***<br>−0.44<br>***<br>−0.05<br>−0.13<br>***|



_Notes:_ Pearson correlation coefficients are reported in Panel A and B over our full sample, while ***, ** and * denote statistical signficance at the 1%, 5% and 10% level, respectively. 

## **Table 4** 

Cross-market factor regressions for ΔCDS1 (full sample). 

||ΔCDS1||ΔCDS1||ΔCDS1||ΔCDS1||ΔCDS1||ΔCDS1||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Constant|0.0000<br>−0.0816||0.0000<br>−0.1282||0.0000<br>−0.1170||0.0000<br>0.3480||0.0000<br>−0.0731||0.0000<br>0.3592||
|ΔVOL1|0.0037<br>6.2513|***|||||||0.0035<br>5.8043|***|0.0002<br>0.2732||
|ΔVOL2|||0.0014<br>2.0808|**|||||0.0008<br>1.1534||0.0002<br>0.2620||
|ΔVOL3|||||−0.0013<br>−4.5925|***|||−0.0006<br>−1.5159||−0.0006<br>−1.6523|*|
|Return|||||||−0.0135<br>−8.4705|***|||−0.0128<br>−4.6400|***|
|Adj.R2|0.1301||0.0033||0.0103||0.1906||0.1304||0.1907||



_Notes:_ This is for tables with the full sample. In this table, each column represents an independent regression while each explaining variable contains three rows representing the regression result. The first row is the estimator, the second row is the t-value, after being adjusted by the Newey-West method, while ***, ** and * denote statistical signficance at the 1%, 5% and 10% level, respectively. 

## **Table 5** 

Cross-market factor regressions for ΔVOL1 (full sample). 

||ΔVOL1||ΔVOL1|ΔVOL1||ΔVOL1||ΔVOL1||ΔVOL1||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Constant|−0.0004<br>−0.2662||−0.0005<br>−0.2754|−0.0002<br>−0.1064||0.0021<br>1.5794||−0.0001<br>−0.0712||0.0018<br>1.4541||
|ΔCDS1|35.3923<br>6.0359|***||||||35.5056<br>6.5098|***|1.5031<br>0.4481||
|ΔCDS2|||−1.1589<br>−0.2939|||||−3.0712<br>−0.7236||−8.1282<br>−2.5841|***|
|ΔCDS3||||9.8317<br>2.2404|**|||8.9263<br>2.2550|**|−6.4360<br>−1.6588|*|
|Return||||||−2.4092<br>−13.9626|***|||−2.4157<br>−12.7413|***|
|Adj.R2|0.1301||−0.0010|0.0036||0.6398||0.1331||0.6434||



_Notes:_ In this table, each column represents an independent regression while each explaining variable contains three rows representing the regression result. The first row is the estimator, the second row is the t-value, after being adjusted by the Newey-West method, while ***, ** and * denote statistical signficance at the 1%, 5% and 10% level, respectively. 

explain more on factors in the volatility surface compared with the full sample. The changes of curvature in the two markets bare small comovements, while all other factors seem to be unrelated including index return and accounting only for the crisis period. During a Financial crisis, investors using stock as a hedging tool can make more efficient hedging with risk among CDS market while using stock as a hedging tool 

cannot improve a lot in the option market comparing with normal period; the risk among changes in slope and curvature of two markets still cannot be hedged by stock efficiently. 

There are several potential explanations for these findings. The relationship between index return movements and changes in the level of CDX could be captured by two similar kinds of indicators. One factor 

8 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

## **Table 6** 

Cross-market factor regressions for ΔCDS1 (Financial Crisis 2008–2010). 

||ΔCDS1||ΔCDS1||ΔCDS1||ΔCDS1||ΔCDS1||ΔCDS1||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Constant|0.0000<br>0.2504||0.0000<br>0.2944||0.0001<br>0.2828||0.0000<br>0.1176||0.0000<br>0.2486||0.0000<br>0.1436||
|ΔVOL1|0.0072<br>4.3035|***<br>|||||||0.0071<br>3.7288|***|0.0030<br>1.3268||
|ΔVOL2|||0.0060<br>2.5157|**|||||0.0001<br>0.0379||−0.0010<br>−0.3301||
|ΔVOL3|||||−0.0024<br>−3.0531|***|||−0.0020<br>−1.2977||−0.0020<br>−1.1878||
|Return|||||||−0.0180<br>−4.4661|***|||−0.0128<br>−2.1628|**|
|Adj.R2|0.2349||0.0243||0.0040||0.2675||0.2312||0.2769||



_Notes:_ In this table, each column represents an independent regression while each explaining variable contains three rows representing the regression result. The first row is the estimator, the second row is the t-value, after being adjusted by the Newey-West method, while ***, ** and * denote statistical signficance at the 1%, 5% and 10% level, respectively. 

**Table 7** 

Cross-market factor regressions for ΔVOL1 (Financial Crisis 2008–2010). 

||ΔVOL1||ΔVOL1|ΔVOL1||ΔVOL1||ΔVOL1||ΔVOL1||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Constant|0.0013<br>0.2659||0.0032<br>0.4798|0.0006<br>0.0939||−0.0009<br>−0.2065||0.0000<br>0.0061||−0.0012<br>−0.3014||
|ΔCDS1|33.6377<br>4.7390|***||||||35.5580<br>5.0225|***|10.8806<br>2.3490|**|
|ΔCDS2|||1.8805<br>0.1775|||||−19.6587<br>−1.7059|*|−23.2807<br>−3.2750|***|
|ΔCDS3||||33.8259<br>2.7565|***|||9.9861<br>0.9916||−8.0256<br>−0.9208||
|Return||||||−1.8767<br>−9.5607|***|||−1.7817<br>−8.3847|***|
|Adj.R2|0.2349||−0.0072|0.0295||0.6310||0.2465||0.6584||



_Notes:_ In this table, each column represents an independent regression while each explaining variable contains three rows representing the regression result. The first row is the estimator, the second row is the t-value, after being adjusted by the Newey-West method, while ***, ** and * denote statistical signficance at the 1%, 5% and 10% level, respectively. 

is the change in default probability from the Merton default model (Merton, 1974). In this case, negative return means the decrease in distance to default, resulting in a higher default probability. Another indicator is the financial leverage factor pointed by Wu and Zhang (2008). For example, a positive return means an increase in the equity Wu value, which then translates to a decrease in financial leverage. Both and Zhang (2008) and Collin-Dufresne et al. (2001) conclude that the financial leverage indicator can explain only some portion of the variation in the CDS spread. In other words, changes in the financial leverage factor can explain changes in the CDS spread. The correlation between factors in the two markets can be mainly explained by their relationship with stock return described by Da Fonseca and Gottschalk (2014). Firstly, ΔCDS1 is positively related to ΔVOL1 due to their same negative relation with stock return. ΔCDS1[′] s positive relationship to ΔVOL2 is also explained through the setting of a bear market; an increase in ΔCDS1 indicates the possibility of a bear market, resulting in steeper skewness of the smile dimension and an increase in ΔVOL2. Similarly, the logic behind negative co-movement between ΔCDS1 and ΔVOL3 is relevant within a bull market, where a decrease in ΔCDS1 translates to an increase of stock return, and consequently, also in ΔVOL3. ΔCDS2 is the most uncorrelated factor to the volatility surface ones. Secondly, ΔVOL1 is weakly and positively related to ΔCDS2 and ΔCDS3 due to the mutually negative relationship with the stock return. ΔVOL2 has a positive relation with ΔCDS2, with the same explanation of a mutually negative correlation with stock return. The relations between ΔVOL1 (ΔVOL2) and ΔCDS2 are weak and insignificant: ΔCDS2 shows the changes in the median part of the CDS curve compared with the whole curve at maturity dimension while ΔVOL1 means the change in whole volatility surface and ΔVOL2 means the changes in volatility smile at moneyness dimension. Finally, accounting for the 2008 crisis, correlations between credit factors and volatility factors are much 

higher than the full sample. These correlations can erode the significance of the stock return completely. This can be simply be explained by the traditional relationship between stock price and implied volatility by Black and Cox (1976) and default probability by Merton (1974). Hence, when analyzing the relationship between the option market and the credit market, the stock return is the main driver of the co-movement between these two markets. Here, we should note that we present robustness regression results in our online Appendix B for the period before and after the financial crisis. 

## **5. Conclusion** 

This paper uses parametric methods to examine the relationship between the CDX curve and OIV surface at an aggregate level. In detail, we apply the Deterministic Linear Function (DLF) to model the implied volatility surface and the N-S model to model the whole CDX curve, with the estimation method of Unscented Kalman Filter (UKF). S&P 500 index is selected as a sample for option volatility surface and CDX curve is constructed by averaging corporate CDS from all companies in American above BBB rating from Jan 2002 to Dec 2019. UKF allows us to extract the dynamics of parameters embedded in DLF and N-S model to capture the movements in CDX curve and S&P 500 index option volatility surface. 

Differently from Ratner and Chiu (2013) and Da Fonseca and Gottschalk (2014), we quantify the relationship between the CDS curve and option volatility surface by using parametric models instead of PCA. We first prove that parameters in the N-S model are consistent with those in no-arbitrage models when modeling the CDS curve. Second, changes in level/slope/curvature in the CDX curve and volatility surface are extracted from parameter models. We also confirm the correlation between these two markets is resulted by the common factor, stock market 

9 

_International Review of Financial Analysis 82 (2022) 102192_ 

_Y. Shi et al._ 

index return, consistent with the conjecture of Ratner and Chiu (2013) and Da Fonseca and Gottschalk (2014). Third, the CDS market co-moves much more with the option market since the late 2000s global financial crisis period. 

Some extensions of this paper can be brought out. First, combining the explained variation in changes of slope/level/curvature in two markets and empirical test from Carr and Wu (2010, 2011), these two markets have a strong market segment. Second, the relation between the market price of macroeconomic factors, variance risk premium, credit risk premium, and equity risk premium can also be an interesting and meaningful research area. 

## **CRediT authorship contribution statement** 

**Yukun Shi:** Data curation, Visualization, Writing – original draft. **Charalampos Stasinakis:** Investigation, Supervision, Validation, Writing – review & editing. **Yaofei Xu:** Conceptualization, Methodology, Software. **Cheng Yan:** Validation, Writing – review & editing. 

## **Data availability** 

The authors do not have permission to share data. 

## **Appendix A. Linking the no-arbitrage model and Nelson-Siegel (N-S) model on Hazard Rate** 

The instantaneous default rate is assumed to follow a square root process. Hence, we model the instantaneous default arrival rate under risk-neutral measure Q as: ̅̅ **̅** d _λt_ = ( _θλ_ − _kλ_ • _λt_ ) _dt_ + _σλ_ • √ _λt_ • _dWt[λ]_ (1) _θλ λ_ = (2) _kλ_ where _λt_ is the instantaneous default arrival rate at time t, _θλ_ is the speed of adjustment multiplying long-run default arrival rate, _kλ_ is the speed of _λ_ adjustment, _σλ_ is the volatility ratio of default rate, _Wt_ is a wiener process and _λ_ is the long-run default arrival rate. The survival rate is an exponential affine function. The expectation of survival rate can be solved by the following equation. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0010-10.png)


To simplify the above equation related to the CDS spread, we relax the assumption between the CDS spread and average hazard rate ( _h_ ). This approach will allow us simply to connect the N-S with the no-arbitrage model. Following Kolokolova, Lin, and Poon (2019), a flat hazard rate curve is assumed ( _λu_ = _h_ ) and the CDS term structure is simply a mathematical transform from the constant hazard term structure after assuming a constant 

10 

_Y. Shi et al.                                                                                                                                                                                                                                      International Review of Financial Analysis 82 (2022) 102192_ 

recovery rate. We calculate the average hazard rate as follows. 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0011-02.png)


where _h_ is average hazard rate between time t and time T, and _R_ is assumed as constant 40%. 

Kolokolova et al. (2019) firstly apply the N-S model to the average hazard rate. The N-S model is widely used in term structural modeling (Christensen, Diebold, & Rudebusch, 2011; Diebold & Li, 2006; Hu, Pan, & Wang, 2013). Thus, we estimate: 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0011-05.png)


where _β_ 0 is the level, _β_ 1 is the slope, _β_ 2 is the curvature and _m_ is the decay coefficient of the hazard rate term structure. 

Parameter _m_ controls the hump shape of the hazard term structure. Regarding this, we follow the assumption of Guo, Han, and Zhao (2014) assumption, where the loadings on the medium-term factor (3-year) are maximized with m as 0.0498, by considering the maturities in the CDS market. This parameter controls the decay rate: a small value will result in slow decay and do a good fitting on long maturities; a large one will result in quick decay and do a good fitting on short maturities; Guo et al. (2014) consider the feature in the option market and choose this parameter with a value of 0.0147 by maximizing the loading on medium-term (122-day). Then, we convert the parameters of the no-arbitrage model into the level, slope, and curvature in the N-S model. According to Guo et al. (2014), _β_ 2 provides a low explanation power on changes to the term structure and we decide to mainly focus on _β_ 0 _and β_ 1 without dropping _β_ 2. In consequence, we end up with _β_ 0 _and β_ 1 mapped from the no-arbitrage pricing model. we attempt estimations with two cases. The first case assumes t approaching zero, while the second assumes t approaching the +∞. In the first case, given that t is approaching zero, t is approximately dt. Hence, from the N-S model we get: 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0011-08.png)


We can now combine the information from both models and through Eqs. (16) and (21) conclude that: 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0011-10.png)


In the second case, we have _t_ →  + ∞. Taking the N-S model into account first and following similar logic as above we estimate: 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0011-12.png)



![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0011-13.png)


11 

_Y. Shi et al.                                                                                                                                                                                                                                      International Review of Financial Analysis 82 (2022) 102192_ 


![](markdown_output/Market_co-movement_between_credit_default_swap_curves_and_option_images/Market_co-movement_between_credit_default_swap_curves_and_option.pdf-0012-01.png)


## **Appendix B. Supplementary data** 

Supplementary data to this article can be found online at https://doi.org/10.1016/j.irfa.2022.102192. 

## **References** 

Alexander, C., & Kaeck, A. (2008). Regime dependent determinants of credit default 

swap spreads. _Journal of Banking & Finance, 32_ (6), 1008–1021. 

Ang, A., & Longstaff, F. A. (2013). Systemic sovereign credit risk: Lessons from the US 

and Europe. _Journal of Monetary Economics, 60_ (5), 493–510. 

- Aunon-Nerin, D., Cossin, D., Hricko, T., & Huang, Z. (2002). Exploring for the determinants of credit risk in credit default swap transaction data: Is fixed-income markets’ information sufficient to evaluate credit risk? _FAME Research Paper, 65_ . https://doi.org/10.2139/ssrn.375563 

Bedendo, M., & Hodges, S. D. (2009). The dynamics of the volatility skew: A Kalman 

filter approach. _Journal of Banking & Finance, 33_ (6), 1156–1165. Benkert, C. (2004). Explaining credit default swap premia. _Journal of Futures Markets, 24_ (1), 71–92. 

Bernales, A., & Guidolin, M. (2014). Can we forecast the implied volatility surface dynamics of equity options? Predictability and economic value tests. _Journal of Banking & Finance, 46_ , 326–342. 

- Berndt, A., & Obreja, I. (2010). Decomposing European CDS returns. _Review of Finance, 14_ (2), 189–233. 

Black, F., & Cox, J. C. (1976). Valuing corporate securities: Some effects of bond indenture provisions. _Journal of Finance, 31_ (2), 351–367. 

- Bliss, R. R., & Panigirtzoglou, N. (2004). Option-implied risk aversion estimates. _Journal of Finance, 59_ (1), 407–446. 

Breitenfellner, B., & Wagner, N. (2012). Explaining aggregate credit default swap spreads. _International Review of Financial Analysis, 22_ , 18–29. 

Buraschi, A., Trojani, F., & Vedolin, A. (2014). When uncertainty blows in the orchard: Comovement and equilibrium volatility risk premia. _Journal of Finance, 69_ (1), 101–137. 

- Campbell, J. Y., & Taksler, G. B. (2003). Equity volatility and corporate bond yields. _Journal of Finance, 58_ (6), 2321–2350. 

Carr, P., & Wu, L. (2010). Stock options and credit default swaps: A joint framework for valuation and estimation. _Journal of Financial Econometrics, 8_ (4), 409–449. 

Carr, P., & Wu, L. (2011). A simple robust link between American puts and credit 

protection. _Review of Financial Studies, 24_ (2), 473–505. 

Carr, P., & Wu, L. (2016). Analyzing volatility risk and risk premium in option contracts: 

- A new theory. _Journal of Financial Economics, 120_ (1), 1–20. 

Carr, P., & Wu, L. (2020). Option profit and loss attribution and pricing: A new 

framework. _Journal of Finance, 75_ (4), 2271–2316. 

Christensen, J. H., Diebold, F. X., & Rudebusch, G. D. (2011). The affine arbitrage-free class of Nelson–Siegel term structure models. _Journal of Econometrics, 164_ (1), 4–20. Collin-Dufresne, P., Goldstein, R. S., & Martin, J. S. (2001). The determinants of credit spread changes. _Journal of Finance, 56_ (6), 2177–2207. 

Collin-Dufresne, P., Goldstein, R. S., & Yang, F. (2012). On the relative pricing of longmaturity index options and collateralized debt obligations. _Journal of Finance, 67_ (6), 1983–2014. 

Cont, R., & Da Fonseca, J. (2002). Dynamics of implied volatility surfaces. _Quantitative Finance, 2_ (1), 45–60. 

Da Fonseca, J., & Gottschalk, K. (2014). Cross-hedging strategies between CDS spreads and option volatility during crises. _Journal of International Money and Finance, 49_ , 386–400. 

Diebold, F. X., & Li, C. (2006). Forecasting the term structure of government bond yields. _Journal of Econometrics, 130_ (2), 337–364. 

Forte, S., & Pena, J. I. (2009). Credit spreads: An empirical analysis on the informational content of stocks, bonds, and CDS. _Journal of Banking & Finance, 33_ (11), 2013–2025. Fuertes, A. M., Phylaktis, K., & Yan, C. (2016). Hot money in bank credit flows to emerging markets during the banking globalization era. _Journal of International Money and Finance, 60_ , 29–52. 

Fuertes, A. M., Phylaktis, K., & Yan, C. (2019). Uncovered equity “disparity” in emerging markets. _Journal of International Money and Finance, 98_ , Article 102066. 

Glatzer, E., & Scheicher, M. (2005). What moves the tail? The determinants of the optionimplied probability density function of the DAX index. _Journal of Futures Markets, 25_ (6), 515–536. 

Goncalves, S., & Guidolin, M. (2006). Predictable dynamics in the S&P 500 index options implied volatility surface. _Journal of Business, 79_ (3), 1591–1635. 

Guo, B., Han, Q., & Zhao, B. (2014). The Nelson–Siegel model of the term structure of option implied volatility and volatility components. _Journal of Futures Markets, 34_ (8), 788–806. 

Haugen, R. A., & Baker, N. L. (1996). Commonality in the determinants of expected stock returns. _Journal of Financial Economics, 41_ (3), 401–439. 

Hilscher, J., Pollet, J. M., & Wilson, M. (2015). Are credit default swaps a sideshow? Evidence that information flows from equity to CDS markets. _Journal of Financial and Quantitative Analysis, 50_ (3), 543–567. 

Hu, G. X., Pan, J., & Wang, J. (2013). Noise as information for illiquidity. _Journal of Finance, 68_ (6), 2341–2382. 

Ismailescu, I., & Phillips, B. (2015). Credit default swaps and the market for sovereign debt. _Journal of Banking & Finance, 52_ , 43–61. 

Kolokolova, O., Lin, M. T., & Poon, S. H. (2019). Rating-based CDS curves. _European Journal of Finance, 25_ (7), 689–723. 

Longstaff, F. A., Pan, J., Pedersen, L. H., & Singleton, K. J. (2011). How sovereign is sovereign credit risk? _American Economic Journal: Macroeconomics, 3_ (2), 75–103. Longstaff, F. A., & Schwartz, E. S. (1995). A simple approach to valuing risky fixed and floating rate debt. _Journal of Finance, 50_ (3), 789–819. 

Merton, R. C. (1974). On the pricing of corporate debt: The risk structure of interest rates. _Journal of Finance, 29_ (2), 449–470. 

Narayan, P. K., Sharma, S. S., & Thuraisamy, K. S. (2014). An analysis of price discovery from panel data models of CDS and equity returns. _Journal of Banking & Finance, 41_ , 167–177. 

Natenberg, S. (1994). _Option volatility and pricing: Advanced trading strategies and techniques, Chicago, Probus_ . 

Nelson, C. R., & Siegel, A. F. (1987). Parsimonious modeling of yield curves. _Journal of Business_ , 473–489. 

12 

Ratner, M., & Chiu, C. C. J. (2013). Hedging stock sector risk with credit default swaps. _International Review of Financial Analysis, 30_ , 18–25. 

Wu, L., & Zhang, F. X. (2008). A no-arbitrage analysis of macroeconomic determinants of the credit spread term structure. _Management Science, 54_ (6), 1160–1175. 

_International Review of Financial Analysis 82 (2022) 102192_ 

Yan, C., Phylaktis, K., & Fuertes, A. M. (2016). On cross-border bank credit and the US financial crisis transmission to FX markets. _Journal of International Money and Finance, 69_ , 108–134. 

Zhou, H. (2018). Variance risk premia, asset predictability puzzles, and macroeconomic uncertainty. _Annual Review of Financial Economics, 10_ , 481–497. 

13 

