Journal of Banking and Finance 171 (2025) 107372 

Contents lists available at ScienceDirect 

## Journal of Banking and Finance 

journal homepage: www.elsevier.com/locate/jbf 

## Predicting individual corporate bond returns 

## Guanhao Feng[a] © , Xin He[b][,][*] , Yanchu Wang[c] , Chunchi Wu[d] 

a _City University of Hong Kong, Hong Kong SAR, China_ 

b _Faculty of Business for Science and Technology, School of Management, University of Science and Technology of China, China_ 

c _School of Finance, Shanghai University of Finance and Economics, China_ 

d _School of Management, State University of New York at Buffalo, USA_ 

A R T I C L E I N F O A B S T R A C T 

_JEL classification:_ Using machine learning and many predictors, we find strong bond return predictability, with an out-of-sample R- C53 squared of 4.48% and an annualized Sharpe ratio of 3.27. ML models identify important predictors for aggregate G12 predictors (bond market returns, TERM and HML factors, GDP growth) and bond characteristics (downside risk, G17 short-term reversal, return skewness, and credit spreads). Predictability varies over time, being stronger during _Keywords:_ periods of high investor risk aversion, slow economic growth, and strong cross-sectional factor explanatory AggregateBond characteristicspredictors power. Our results highlight the benefits of leveraging both cross-sectional and time-series predictors to forecast Forecast-implied investment gains corporate bond returns while considering public and private bonds. Machine learning Time-varying return predictability 

## **1. Introduction** 

Recent advancements in machine learning (ML) have greatly enhanced empirical asset pricing, particularly in asset return prediction (e.g., Gu et al., 2020). However, these techniques are primarily applied to the equity market, leaving the corporate bond literature underdeveloped, which is surprising given the scale and importance of the corporate lending market. One reason for this gap may be the limited availability of comprehensive corporate bond data before the introduction of TRACE (Trade Reporting and Compliance Engine) in 2002. Additionally, many corporate bonds are issued by private firms, making their information less accessible than that of public companies. These data limitations have posed significant challenges to understanding return predictability in the corporate bond market. 

The equity and bond return predictability literature (e.g., Welch and Goyal, 2008; Lin et al., 2018) has suggested a number of useful 

aggregate predictors, including GDP growth, inflation, consumption growth, and many others. Meanwhile, the cross-sectional return prediction literature (e.g., Chordia et al., 2017; Choi and Kim, 2018) has identified bond characteristics such as reach-for-yield, credit spread, and maturity as strong predictors. There is a need to incorporate these time-series and cross-sectional predictors into return forecasts and asset pricing for corporate bonds. However, the large number of predictors in this combined variable set creates a high-dimensionality problem, which could lead to poor out-of-sample forecast performance if this issue is not properly addressed (see Welch and Goyal, 2008). 

In this paper, we employ flexible ML models to overcome the challenges of high-dimensionality in return predictors and potential nonlinearity in asset pricing models for corporate bonds (see Gu et al., 2021; Kelly et al., 2023). Using a comprehensive dataset that includes both private and public bonds with a long data span from 1976 to 2020, we document several important findings that contribute to the current 

We are grateful to Geert Bekart (editor), the anonymous associate editor and two referees, Dashan Huang (discussant), Jingzhi Huang, Injun Hwang, Guohao Tang, Junbo Wang, and Tengfei Zhang, and the conference participants at 2021 FMA Annual Meeting, 2021 International Conference of the French Finance Association, 2022 China International Risk Forum, 2022 Australasian Finance and Banking Conference, and 2023 Fixed Income and Institutions Research Symposium at Hong Kong Polytechnic University for constructive discussions and feedback. Feng acknowledges financial support from the Hong Kong Research Grants Council (GRF11502721, GRF-11502023) and the Natural Science Foundation of China (NSFC-72203190). Feng is partially supported by the InnoHK initiative and the Laboratory for AI-Powered Financial Technologies. Wang acknowledges financial support from the Natural Science Foundation of China (72203138). * Corresponding author. 

_E-mail addresses:_ gavin.feng@cityu.edu.hk (G. Feng), xin.he@ustc.edu.cn (X. He), wang.yanchu@mail.shufe.edu.cn (Y. Wang), chunchiw@buffalo.edu (C. Wu). https://doi.org/10.1016/j.jbankfin.2024.107372 

Received 12 February 2023; Accepted 12 December 2024 Available online 13 December 2024 

0378-4266/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

literature. 

First, we find that ML linear models, such as Lasso, outperform combination forecasts used by Lin et al. (2014), while ML nonlinear models, such as random forest (RF), perform even better than the linear models. The _R_[2] _OOS_[for][return][prediction][by][RF][is][4.48%][over][the][testing] period from 1996 to 2020, with an annualized Sharpe ratio of 3.27 for a forecast-implied strategy, comparable to long-short trading strategies in Kelly et al. (2023). Second, ML models identify corporate bond market excess returns, TERM and HML factors, and GDP growth as leading aggregate predictors, alongside downside risk, short-term reversal, return skewness, and credit spreads as key bond characteristic predictors. Third, bond return predictability varies over time, strengthening during periods of high investor risk aversion, slow economic growth, and strong cross-sectional factor explanatory power. Lastly, ML predictions improve with a large dataset that includes both cross-sectional and time-series predictors, trained on public and private bonds. 

The RF-based long-short trading strategy achieves a monthly average return of 1.95% and an alpha of 2.09%, which is not captured by the traditional multifactor model (Fama and French, 1993). Additionally, our direction-implied trading strategy generates an alpha of 1.59%, complementing the long-short trading approach. With monthly turnover ratios for bond trading strategies ranging from 30% to 140%, these investment gains remain robust even after accounting for transaction costs. 

There is strong evidence of time-varying predictability in the corporate bond market. The _R_[2] _OOS_[reaches 5.07% when the risk aversion] index (Bekaert et al., 2022) is high, exceeding the 4.20% _R_[2] _OOS_[when risk] aversion is low. This finding aligns with Bianchi et al. (2021) in the Treasury bond market. Predictability is also higher when the Chicago Fed National Activity Index (CFN) is low, the VIX is high, and when the cross-sectional explanatory power, measured by IPCA factors (Kelly et al., 2023), is greater. 

Our findings underscore the importance of using big data in predicting corporate bond returns. Incorporating a large number of aggregate and bond characteristic predictors, along with long-span private and public bond data significantly improves the predictive power of ML models. For example, the annualized Sharpe ratio of the RF long-short strategy increases from 2.90 to 3.27 with the inclusion of aggregate predictors. Excluding private bonds decreases _R_[2] _OOS_[from][4.48%][to] 4.01% and reduces the Sharpe ratio of the long-short trading strategy from 2.40 to 2.13.[1] 

This paper contributes to the rapidly evolving literature on empirical asset pricing through ML. Recent research demonstrates stock return predictability using ML and deep learning techniques (Gu et al., 2020, hereafter GKX2020; Avramov et al., 2023). GKX2020 finds that boosted regression trees and random forests excel in predicting stock returns. Bianchi et al. (2021) report enhanced return predictability for Treasury bond returns using ML. Kelly et al. (2023) and Feng et al. (2023) introduce latent factor models for corporate bonds, while Guo et al. (2022) find strong predictive evidence with a set of yield predictors, and Li et al. (2022) use ML to investigate risk factors of corporate bond returns in international markets. Feng et al. (2024) generates characteristics-based benchmarks for bond pricing via the panel tree. 

Our paper is related to Bali et al. (2022), who predict corporate bond returns using various predictors and ML methods. They investigate the 

impact of the stock-bond connection on predicting cross-sectional returns, focusing on bonds issued by public firms. Our paper differs from Bali et al. (2022) in three key aspects. First, we include cross-sectional bond characteristics, time-series aggregate predictors, and their interactions to evaluate bond return predictability. Second, our data spans 45 years, allowing us to assess the time-varying predictability of corporate bond returns over several business cycles. This long-span analysis contributes to the literature on time-varying stock return predictability (e.g., Rapach et al., 2010; Dangl and Halling, 2012; Avramov et al., 2023) by providing new evidence in the corporate bond market. Third, we explore the predictive information in both private and public bonds, and find that including private bond data significantly increases the predictive power of the ML models. 

Existing research has primarily relied on market-wide indices and state variables (e.g., Keim and Stambaugh, 1986; Fama and French, 1989) to predict bond returns, while some studies indicate that aggregate predictors can forecast corporate default rates (Giesecke et al., 2011). New methods in bond return prediction include nonlinear time-series models by Hong et al. (2012), combination forecasts by Lin et al. (2014), and an iterated combination approach by Lin et al. (2018). We extend these studies by incorporating cross-sectional predictors to capture potential nonlinearity and interactions in return predictors using ML models. 

Finally, our paper contributes to asset pricing in the corporate bond market. Fama and French (1993) expand the three-factor model (MKT, SMB, and HML) to include the DEF and TERM factors for pricing bond returns. Bekaert and De Santis (2021) find that when incorporating a broad market portfolio of Treasuries, corporate bonds, and equities, the CAPM is a robust one-factor model. Several studies examine the roles of DEF and TERM betas (Gebhardt et al., 2005), liquidity (Lin et al., 2011), momentum (Jostova et al., 2013), and volatility factors (Chung et al., 2019) in corporate bond pricing, while others consider equity (Chordia et al., 2017; Choi and Kim, 2018) and option variables (Cao et al., 2023). Bekaert et al. (2024) propose a three-factor model for international corporate bond markets, including global market, maturity, and liquidity factors. Building on this research, we investigate corporate bond return predictability using ML models with numerous predictors over a long data span. 

The remainder of the paper is structured as follow: Section 2 outlines the predictive model design. Section 3 discusses the data sample and presents evidence of return predictability. Section 4 analyzes the importance of the predictors. Section 5 details forecast-implied investment gains, and Section 6 provides additional robustness tests. Finally, Section 7 concludes the paper. 

## **2. Methodology** 

## _2.1. Predictive modeling_ 

## _2.1.1. Predictive framework_ 

Excess asset returns follow an expectation model with an additive prediction error: 

**==> picture [252 x 10] intentionally omitted <==**

in which _ri,t_ +1 is the excess return for bond _i_ ( _i_ = 1 _,_ ⋯ _,Nt_ ) in month _t_ + 1. _gt_ ( _zi,t, xt_ ) is the expected excess return for bond _i_ in month _t_ + 1, conditional on information in month _t_ . Bond characteristics for bond _i_ in month _t_ are denoted as _zi,t_ , and aggregate predictors in month _t_ are 

> 1 The changes in Sharpe ratio from 2.90 to 3.27 and from 2.40 to 2.13 are significant at the conventional level based on the tests of Opdyke (2007) and spanning regression analysis. The change of _R_[2] _OOS_[from][4.48%][to][4.01%][is][also] statistically significant based on the Fama-MacBeth out-of-sample ROOS[2][test and] the Diebold and Mariano (1995) specification test. 

2 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

denoted as _xt_ . At the end of each year, we recursively estimate the model _gt_ (⋅) using a rolling window of the past 20 years. We employ a panel approach to predict bond returns, assuming the same functional form for all observations, which is typical for modeling individual asset returns. Fitting a pooled regression for individual bonds typically results in more observations than predictors, thereby minimizing concerns about overfitting. We then use the model for prediction over the next 12 months. As a result, the model is updated annually, and the predictors are updated monthly.[2] 

## _2.1.2. Predictive models_ 

We evaluate five groups of linear and nonlinear predictive models: combination forecasts, dimension reduction, penalized linear regression, ensemble trees (boosted trees and RF), and neural networks. 

- (i) The forecast combinations, MeanC (mean combination) and MedianC (median combination), merge individual forecasts with different weights. MeanC assigns equal weights, whereas MedianC weights only the median of the individual forecasts. 

- (ii) Dimension reduction techniques, PCA and PLS, involve two steps. First, they combine predictors using linear weights to reduce dimensions to a few components, which are then used in predictive regression. PCA preserves the covariance structure, whereas PLS aims for maximal predictive correlation. 

- (iii) Regularized linear predictive regressions—Lasso, Ridge, and Elastic Net—preserve the original predictors without transforming them, maintaining their interpretation. Lasso and Ridge use different regularization functions (L1 and L2, respectively), whereas Elastic Net combines both L1 and L2 penalties. 

- (iv) For regression tree algorithms, we use two ensemble models: gradient boosted trees, which combine predictions from a sequence of simple trees, and RF, which average forecasts from multiple trees using bootstrap aggregating. 

- (v) We use a classic feed-forward neural network with an input layer, one or more hidden layers, and an output layer. We consider two configurations: NN1 with one hidden layer of 32 neurons and NN2 with two hidden layers of 32 and 16 neurons, respectively. 

For brevity, we report results for the MeanC, Lasso, PLS, RF, and NN2, representing five distinct model types. More details about these models and parameter tuning can be found in Appendix A. The training and prediction schemes follow GKX2020 without look-ahead bias. 

prediction errors across all assets and periods to assess the mean squared error reduction relative to a benchmark forecast ~~_r_~~ _i,t_ . We use the 20-year moving average excess return of the corresponding rating-sorted portfolio as ~~_r_~~ _i,t_ in the denominator,[3] which is a more robust benchmark than the naive zero forecast and the factor model forecasts.[4] 

## _2.2.2. Fama-MacBeth out-of-sample_ R[2] 

_OOS_ 

The Fama and MacBeth (1973) method is standard in the empirical asset pricing literature. We construct a Fama-MacBeth-type _R_[2] _OOS_[for] model evaluation, exploiting the advantage of this method in increasing test efficiency. Specifically, for each month _t_ , we calculate 

**==> picture [252 x 25] intentionally omitted <==**

where _ri,t_ , ̂ _ri,t_ , and ~~_r_~~ _i,t_ are the realized return, return forecast, and benchmark forecast for bond _i_ in month _t_ , similar to Eq. (2) in Section _T_ 2.2.1. Eq. (3) generates a time series of { _R_[2] _OOS,t_ } _t_ =1[.][5][ The Fama-MacBeth] design is feasible because of the big panel data, which are long in the time series and large in the cross section. The Fama-MacBeth average ~~2~~ _ROOS_[is] 

**==> picture [252 x 22] intentionally omitted <==**

Unlike _R_[2] _OOS_[,][the][Fama-MacBeth][modeling][allows][us][to][evaluate][the] statistical significance of _R_[2] _OOS_[with][ Newey-West (1987)][ robust standard] errors.[6] The testing hypotheses are ~~2 2~~ _H_ 0 : _ROOS_[=][ 0] _[and][H]_[1][:] _ROOS_[∕=][ 0] _[.]_ 

Comparing the forecast performance for different sets of results is _T T_ useful, for example, { _R_[2] _OOS,t_ ;1} _t_ =1[and] { _R_[2] _OOS,t_ } _t_ =1[for][two][subsamples.] The null and alternative hypotheses are ~~2 2 2 2~~ _H_ 0 : _ROOS_ :1[=] _ROOS_ :2 _[and][H]_[1][:] _ROOS_ :1[∕=] _ROOS_ :2 _[.]_ 

**==> picture [252 x 37] intentionally omitted <==**

and then conduct hypothesis testing. 

## _2.2. Performance evaluation metrics_ 

## _2.2.3. Variable importance measures_ 

Knowing about the key predictors provides useful economic insights. 

## _2.2.1. Out-of-sample_ R[2] 

**==> picture [11 x 5] intentionally omitted <==**

The predictive performance is evaluated by the out-of-sample _R_[2] _OOS_[:] 

**==> picture [252 x 26] intentionally omitted <==**

in which _ri,t_ denotes the realized return for bond _i_ in month _t_ in the holdout sample, and ̂ _ri,t_ is the return forecast of bond _i_ in month _t_ generated from the predictive models discussed in Section 2.1. This _R_[2] _OOS_[sums] 

> 2 We align all the predictors to a monthly frequency, although some are updated quarterly, such as the consumption growth rate and GDP growth rate. We do not update these models monthly, because doing so takes 12 times more computation than annual updating while offering only marginal improvements to the models. 

> 3 We sort the bonds into five rating portfolios: AAA, AA, A, BBB, and NIG. These sorted portfolios serve as stronger benchmarks than the moving average of the bond market excess return or a naive zero forecast. For instance, the prediction benchmark for an AAA bond is the 20-year moving average excess return of the AAA portfolio. 

> 4 In Tables 2, 3, and 4, we report the OOS R² of naive zero forecasts, BS3 (Bekaert and De Santis, 2021), FF3 (Fama and French, 1993), and FF5 (Fama and French, 1993). Most values are negative or marginally positive, indicating these forecasts are weaker benchmarks than rating-sorted portfolios. BS3 includes the equity market, corporate bond market, and treasury bond market factors (see footnote 1 of Bekaert and De Santis, 2021); FF3 includes MKT, DEF, and TERM; FF5 includes MKT, SMB, HML, DEF, and TERM. 

> 5 Kelly et al. (2023) use similar Fama-MacBeth-type _R_ 2 measures that first aggregate information in the cross section and then take average in the time series. 

> 6 We set the number of lags by Newey–West Bartlett kernel, where lags _L_ = 

**==> picture [114 x 20] intentionally omitted <==**

3 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

Similar to GKX2020, we first construct a new predictor dataset by setting all values of predictor _j_ to 0 and keep the remaining predictors unchanged. We then give a new prediction ̃ _r_[[] _i,[j] t_[]][with][the][initially][fitted] model and the new predictor dataset. We measure the variable importance by the reduction in _R_[2] _OOS_[,] 

**==> picture [252 x 30] intentionally omitted <==**

**==> picture [252 x 11] intentionally omitted <==**

where _ri,t_ , ̃ _r_[[] _i,[j] t_[]][,][and] ~~_r_~~ _i,t_ are the realized return, model forecast, and benchmark forecast. 

Our variable importance measure differs from that of GKX2020. Whereas GKX2020 assesses each predictor’s contribution to in-sample model fitting and ranks them accordingly, their measure does not reflect OOS predictability, which is crucial for evaluating model performance. In contrast, our measure focuses on the OOS contribution of each predictor. We provide both raw and relative importance measures in our analysis. A predictor’s importance is considered positive if it enhances OOS prediction, conditional on other variables, and negative otherwise. 

## **3. Evidence on return predictability** 

## _3.1. Data_ 

## _3.1.1. Corporate bond returns_ 

The corporate bond returns data are sourced from four databases: the TRACE database, the National Association of Insurance Commissioners (NAIC) database, the Lehman Brothers Fixed Income (LBFI) database, and DataStream. We consolidate these sources to create a comprehensive sample covering the period from 1973 to 2020, applying a priority ranking to retain only one observation for duplicates, ranked in the following order: TRACE, NAIC, LBFI, and DataStream, following the data handling methods of Lin et al. (2014) and Lin et al. (2018). To avoid confounding effects, we focus on straight bonds, excluding asset-backed bonds, option-embedded bonds, non-USD-denominated bonds, bonds with unusual coupons, and those with maturities under one year or over 30 years. The monthly return of corporate bond _i_ at time _t_ is calculated as follows: 

**==> picture [252 x 22] intentionally omitted <==**

in which _Pi,t_ is the price, _Ai,t_ is the accrued interest, and _Ci,t_ is the coupon payment for bond _i_ in month _t_ . We obtain excess returns by subtracting the three-month T-bill rate from the raw return. Table 1 provides summary statistics of the sample. 

## _3.3.2. Bond predictors_ 

The literature identifies a number of aggregate predictors for corporate bonds (e.g., Giesecke et al., 2011; Lin et al., 2018). Our aggregate predictors fall into three categories: economic indicators (e.g., GDP growth, inflation), bond market variables (e.g., term spread, default spread, forward factor), and equity market variables (e.g., S&P 500 Index returns, earnings-to-price ratio). We assemble a total of 25 aggregate predictors, detailed in Appendix B, Table B.1. 

In addition, we include 26 corporate bond characteristic predictors across three categories: fundamental (e.g., rating, maturity), returnbased (e.g., momentum, volatility), and covariances with common risk factors (e.g., betas on DEF and TERM factors). The data span from January 1973 to September 2020, with the final sample of predictors starting in January 1976 to allow for three years of data for calculating return-based characteristics. 

## _3.4. Out-of-sample predictability_ 

We evaluate the OOS predictability of corporate bond returns to identify the best ML model. Table 2 reports the monthly average ~~2~~ _ROOS_[(see][Eq.][(4)][),][the][significance][for][return][predictability,][and][the] overall performance measure _R_[2] _OOS_ (see Eq. (2)). Based on the _R_[2] _OOS_[measure,][corporate][bond][returns][are][predictable][by][all][models] ~~2~~ except the median combination. Further, _ROOS_[shows][positive][numbers] for all models except the median combination and PLS. The null hypothesis of no predictability is rejected at the 1% level for MeanC, Lasso, Ridge, Elastic Net, boosted trees, RF, and neural networks. Penalized linear regressions (Lasso, Ridge, and Elastic Net) perform similarly well in predicting individual corporate bond returns, outperforming combination forecasts, with Lasso being the best linear model, with 2.70% _R_ ~~2~~ _OOS_[.][The][ML][nonlinear][models,][namely][trees][and][neural][networks,] perform better than those linear models. The RF model, which is ~~2~~ nonlinear, is the best-performing model with 4.64% _ROOS_[.] 

When dividing the sample into investment-grade (IG) and noninvestment-grade (NIG) bonds, we find IG bonds are generally more predictable than NIG bonds across models. Overall, there is compelling evidence of corporate return predictability. Corporate bond returns are predictable for both the full sample and across IG and NIG sub-samples, with RF and Lasso ranked as the top models for nonlinear and linear predictions, respectively. 

The predictability measure is relative to the benchmark prediction in the denominators of Eqs. (2) and (3). We consider four benchmark predictions and compare them with the rating portfolio benchmark in the last four rows of Table 2. The four benchmark predictions are naïve zero prediction and factor model implied return predictions[7] for BS3 factors (corporate bond market factor, equity market factor, and treasury bond market factor) in Bekaert and De Santis (2021), FF3 factors (MKT, DEF, and TERM), and FF5 factors (MKT, SMB, HML, DEF, and TERM) in Fama and French (1993).[8] None of these significantly outperforms the rating-sorted portfolio benchmark, as the values of _R_ ~~2~~ _OOS_ are either close to zero or significantly negative. 

## _3.5. Differential predictability in time series and cross section_ 

In this subsection, we present three key analyses: the differences in OOS return predictability of corporate bonds across various rating and maturity groups, the effectiveness of different predictive models for these bonds, and the impact of the 2008 financial crisis on the predictability of high-rated (AAA) bonds compared to lower-rated bonds across different maturities. 

Table 3 Panel A reports the predictability of five rating groups, showing that all groups are predictable in terms of _R_[2] _OOS_[using][most] predictive methods. Lasso, Elastic Net, RF, and NN2 are particularly strong models that also deliver significantly positive _R_ ~~2~~ _OOS_[for][all][rating] groups. In the appendix, Table B.5, Panels A.1–A.3 present the pre-crisis, crisis, and post-crisis results, all exhibiting return predictability. The 2008 financial crisis significantly affects return predictability, particularly for high-rated bonds. In Table B.5, Panels A.2 (crisis) and A.3 (postcrisis), Lasso, RF, and NN2 show negative or insignificantly positive ~~2~~ _ROOS_[for the AAA group. For A, BBB, and NIG groups, the predictability] remains quite robust during the crisis period. 

Table 3 Panel B presents results for different maturity groups. We 

> 7 The factor model predictions are the product of bond beta, based on past 60-month rolling-window beta estimation, and factor risk price estimated as the 20-year rolling-window average of the factors. 

> 8 Recent findings from Bekaert and De Santis (2021) and Bekaert et al. (2024) suggest that mapping risk factors in the corporate bond market is still in its infancy. We hope our paper stimulates future research in this area. 

4 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

## **Table 1** 

Summary statistics. 

||Panel A: Descriptive Statistics<br>All<br>Lehman<br>DataStream<br>TRACE&NAIC<br>Public<br>Private|
|---|---|
||Bond-month observations<br>753,274<br>182,931<br>20,413<br>549,930<br>273,890<br>479,384<br>Start Year<br>1976<br>1976<br>1990<br>1993<br>1976<br>1976<br>End Year<br>2020<br>1998<br>2008<br>2020<br>2020<br>2020<br>% of Public Bond<br>36.36<br>43.30<br>5.32<br>34.99<br>100<br>0<br>% of Private Bond<br>63.64<br>56.70<br>94.68<br>65.01<br>0<br>100<br>% of IG<br>85.23<br>88.06<br>77.48<br>84.49<br>84.50<br>85.65<br>% of NIG<br>14.77<br>11.94<br>22.52<br>15.51<br>15.50<br>14.35<br>Return - mean (%)<br>0.51<br>0.78<br>0.51<br>0.41<br>0.51<br>0.49<br>Return - median (%)<br>0.39<br>0.69<br>0.42<br>0.28<br>0.43<br>0.37<br>Excess return - mean (%)<br>0.20<br>0.19<br>0.20<br>0.21<br>0.21<br>0.18<br>Excess return - median (%)<br>0.12<br>0.16<br>0.12<br>0.10<br>0.16<br>0.09<br>Rating - mean<br>5.60<br>5.58<br>7.46<br>5.53<br>6.02<br>5.35<br>Rating - median<br>5<br>5<br>7<br>5<br>5<br>5<br>Duration - mean (years)<br>5.61<br>5.37<br>8.91<br>5.58<br>5.83<br>5.49<br>Duration - median (years)<br>4.82<br>5.01<br>9.48<br>4.57<br>5.09<br>4.65<br>Age - mean (years)<br>9.00<br>17.21<br>6.78<br>6.10<br>9.11<br>8.93<br>Age - median (years)<br>5.63<br>18.94<br>6.34<br>4.39<br>5.80<br>5.54<br>Amt out. - mean ($ million)<br>1024<br>67<br>86<br>1155<br>515<br>1152<br>Amt out. - median ($ million)<br>130<br>25<br>10<br>150<br>200<br>100|
||Panel B: Sample Distribution (%) by Rating&Maturity<br>AAA<br>AA<br>A<br>BBB<br>NIG<br>Public<br>Private<br>All|
||Maturity<br>1<br>2.00<br>2.36<br>5.13<br>2.66<br>1.05<br>4.19<br>9.02<br>13.20<br>2<br>1.58<br>2.26<br>4.80<br>2.49<br>0.98<br>4.04<br>8.06<br>12.10<br>3<br>1.14<br>1.83<br>4.02<br>2.19<br>0.91<br>3.57<br>6.52<br>10.09<br>4<br>1.14<br>1.74<br>3.98<br>2.16<br>0.88<br>3.60<br>6.30<br>9.90<br>5<br>0.67<br>1.08<br>2.61<br>1.65<br>0.79<br>2.54<br>4.25<br>6.79<br>6<br>0.65<br>0.97<br>2.50<br>1.61<br>0.78<br>2.53<br>3.99<br>6.52<br>7<br>0.49<br>0.87<br>2.17<br>1.41<br>0.63<br>2.22<br>3.36<br>5.58<br>8<br>0.48<br>0.85<br>2.15<br>1.45<br>0.56<br>2.22<br>3.27<br>5.49<br>9<br>0.46<br>0.83<br>2.19<br>1.61<br>0.57<br>2.39<br>3.27<br>5.66<br>10<br>0.13<br>0.43<br>0.90<br>0.81<br>0.29<br>0.98<br>1.57<br>2.56<br>_>_10<br>1.69<br>2.64<br>7.47<br>7.56<br>2.74<br>8.09<br>14.02<br>22.11<br>All<br>10.43<br>15.87<br>37.92<br>25.60<br>10.18<br>36.36<br>63.64<br>100.00|



The sample includes 753,274 monthly return observations of 22,747 unique corporate bonds from January 1976 to September 2020. % of IG indicates the percentage of investment-grade bonds in the sample, whereas % of NIG indicates the percentage of non-investment-grade bonds. The rating is measured on a nominal scale, with 0 being assigned to AAA, 1 to AA, … and 15 to NIG. We report TRACE and NAIC together because they are both transaction-based data, and a large proportion of NAIC observations are covered by TRACE. 

find that the RF model performs best, yielding significantly positive results for all groups across various OOS periods. Penalized linear regressions produce positive _R_[2] _OOS_[for][all][groups,][although][their][predict-] ability for TMT1 (short maturity) is somewhat unstable. In contrast, boosted trees, RF, and NN2 effectively predict returns of all groups and manage the heterogeneous characteristics across different maturities. Table B.5 Panels B.1– B.3 demonstrate that the 2008 financial crisis does not significantly impact the predictability of different maturity groups, and nonlinear models prove more reliable than linear models during the crisis. 

Collectively, NIG bonds are less predictable than IG bonds, and the 2008 financial crisis significantly affects the return predictability of AAA bonds. Maturity groups show similar predictability with the RF model, remaining unaffected by the crisis. Overall, the RF model demonstrates robustness across different periods. 

## _3.6. Return predictability on private and public bonds_ 

We next explore whether private and public corporate bonds exhibit different return predictability, how excluding equity characteristics—available only for public bonds—affects the predictability of public bonds compared with private ones, and whether this predictability varies before, during, and after the 2008 financial crisis. Several studies (e.g., Chordia et al., 2017; Choi and Kim, 2018) use equity characteristics for corporate bond return prediction, either ignoring private bond data or imputing equity data. Since our sample includes 

both private and public bonds, we focus on aggregate predictors and bond characteristics accessible to all corporate bonds, as equity information is only available for public bonds. 

We examine the difference in predictability between private and public bond returns. If equity characteristics—exclusive to public bonds—provide extra signals, excluding them might reduce return predictability of public bonds. However, due to market transparency and liquidity, public bonds may remain more predictable than private ones without equity characteristics. Therefore, whether public bonds become less predictable without stock characteristics is an empirical question. Our predictive model tests this hypothesis: 

**==> picture [209 x 12] intentionally omitted <==**

Table 3 Panel C reports the predictability of private and public bonds separately. In the third column, we calculate the average of the timeseries differences between the _R_[2] _OOS,t_[of][private][and][public][bonds][using] the Fama-MacBeth _t_ -statistics (see Eq. (5)). The results indicate that private bonds exhibit larger _R_[2] _OOS_[values][compared][to][public][bonds][for] ~~2~~ Lasso, PLS, and RF, while MeanC shows smaller _ROOS_[for private bonds.] However, all these differences are statistically insignificant. Table B.5 Panels C.1–C.3 present results for different periods (before, during, and after the 2008 global financial crisis). Private bonds generally show a larger _R_ ~~2~~ _OOS_[,][indicating][greater][predictability][than] public bonds. However, t-tests for these differences are statistically insignificant. Panels C.4–C.7 analyze rating and maturity subsamples, 

5 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Table 2** 

Predictive evidence of returns. 

||||
|---|---|---|
||_R_<br>~~2~~<br>_OOS_<br>IG<br>NIG<br>All|_R_2<br>_OOS_<br>IG<br>NIG<br>All|
|MeanC<br>MedianC<br>Lasso<br>Ridge<br>ENet<br>PCA<br>PLS<br>BTree<br>RF<br>NN1<br>NN2<br>BS3<br>FF3<br>FF5<br>Zero|0.44***<br>-0.04<br>0.33***<br>0.04<br>-0.38<br>-0.04<br>2.99***<br>2.06***<br>2.70***<br>2.70***<br>2.03***<br>2.52***<br>2.39***<br>1.83***<br>2.19***<br>1.26***<br>0.88**<br>1.06**<br>-0.75<br>0.14<br>-0.28<br>5.93***<br>0.05<br>4.54***<br>5.37***<br>2.77***<br>4.64***<br>3.08***<br>3.06***<br>3.76***<br>4.73***<br>2.97***<br>4.42***<br>0.00<br>-0.87*<br>-0.15*<br>-0.82*<br>-0.16<br>-0.75*<br>-1.75***<br>-0.88**<br>-1.68***<br>-0.92***<br>-1.32***<br>-0.95***|0.42<br>0.10<br>0.30<br>-0.04<br>-0.15<br>-0.09<br>3.24<br>2.04<br>2.77<br>3.49<br>2.25<br>3.00<br>2.87<br>1.09<br>2.17<br>1.57<br>0.96<br>1.33<br>1.19<br>2.83<br>1.84<br>9.19<br>5.84<br>7.87<br>5.40<br>3.07<br>4.48<br>4.65<br>4.21<br>4.48<br>5.49<br>5.35<br>5.44<br>0.07<br>-0.11<br>0.03<br>-0.24<br>0.31<br>-0.13<br>-0.85<br>-0.02<br>-0.69<br>-0.27<br>-0.24<br>-0.26|



This table reports the main results for corporate bond return predictability from 1996 to 2020. In the column name, we have IG for investment-grade bonds, NIG for non-investment-grade bonds, and All for the whole sample. We report for 11 predictive models, three factor models, and the naive zero prediction. The predictive models are introduced in Section 2.1 and Appendix A. The factor models are BS3 (equity, corporate bond, and treasury bond market factors) in Bekaert and De Santis (2021), FF3 (MKT, DEF, and TERM) in Fama and French (1993), and FF5 (MKT, SMB, HML, DEF, and TERM) in Fama and French (1993). The left panel presents _R_ ~~2~~ _OOS_[(%)][(see][Eq.][(4)][),][and][the][significance][of] Fama-MacBeth _t_ -statistics. The right panel presents _R_[2] _OOS_[(%)][(see][Eq.][(2)][).][The] _t_ -statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

where differences in predictability between private and public bonds remain statistically insignificant for IG and NIG bonds. Overall, we cannot reject the null hypothesis that private and public bonds have similar predictability, a pattern that holds across various rating and maturity subsamples. Our finding suggests public information available for firms with stocks and bonds does not significantly affect bond return predictability, which is consistent with Ronen and Zhou (2013)’s finding that stock trading does not lead the corporate bond market where institutional trades dominate. 

## **4. Variable importance for return predictability** 

In this section, we investigate the key predictors and how aggregate predictors and bond characteristics contribute to the OOS predictive power of the models. We use OOS relative variable importance and raw variable importance measures to identify influencing variables. Additionally, we examine the predictive power of aggregate predictors, building on the work of Lin et al. (2014, 2018) and complementing the studies of Chordia et al. (2017), Choi and Kim (2018), and Bali et al. (2022), who utilize bond and equity characteristics to predict corporate bond returns. 

## _4.1. Relative variable importance_ 

Fig. 1 shows the relative importance of predictors, with each variable normalized to sum to 1. The predictors are ordered by their average ranks, with the most important ones at the top. The results indicate that ML models identify corporate bond market excess returns, TERM and HML factors, and GDP growth rates as the most important aggregate predictors, and downside risk, short-term reversal, return skewness, and credit spreads emerge as key cross-sectional characteristic predictors. Consistent with Giesecke et al. (2011), stock volatility, GDP growth, and industrial production growth are useful for forecasting bond returns. Credit spread and reach-for-yield are important characteristic 

predictors, aligning to the findings of Chen and Choi (2023). 

Fig. B.1 shows the top ten most important variables for MeanC, Lasso, PLS, RF, and NNs. Aggregate predictors comprise five of the top ten predictors for both RF and Lasso, highlighting that both aggregate predictors and bond characteristics are relevant for OOS prediction. 

## _4.2. Out-of-sample variable importance_ 

We next examine the OOS raw (unadjusted) variable importance. Fig. 2 presents a heat map of variable importance, with positive values shown in green, negative values in red, and values close to zero in yellow. The variable order is consistent with that in Fig. 1, suggesting that our variable importance measures are robust. Many predictors contribute minimally to OOS prediction, with some in dark red even harming it. The raw variable importance measure provides additional useful information for evaluating predictors. For example, some “relatively less important” predictors in Fig. 1, such as market liquidity and the SMB factor in aggregate predictors, as well as the three-year longterm reversal and beta on the HML factor among bond characteristic predictors, do not appear to be helpful for the OOS prediction. 

Overall, we find ML models identify a subset of predictors that are important for predicting bond returns. The important predictors include corporate bond market returns, TERM factor, HML factor, and GDP growth rate among aggregate predictors, and downside risk, short-term reversal, return skewness, and credit spread among bond characteristic predictors. 

## _4.3. Prediction power: aggregate predictors vs. bond characteristics_ 

The RF model demonstrates the highest prediction accuracy, as discussed in section 3.2. We now further explore the predictive power of two distinct sets of predictors within the RF framework by evaluating four distinct model specifications: (1) a combination of aggregate predictors and bond characteristics with interactions, (2) both sets of predictors without interactions, (3) aggregate predictors alone, and (4) bond characteristics alone.these four specifications. Panels A, B, and C correspond to the five rating Table 4 reports the _R_ ~~2~~ _OOS_[and] _[ R]_[2] _OOS_[values for] subsamples, five maturity subsamples, and the full sample, along with private-public bond subsamples, respectively. 

The specifications for models (1) and (2) allow us to investigate the interaction effect between aggregate predictors and bond characteristics in a nonlinear ML model. In model (2), we build 500 trees using only aggregate predictors and another 500 using only bond characteristics, and then combine the predictions from these 1,000 trees into a single prediction. Whereas models (1) and (2) both use two sets of predictors, model (1) incorporates interactions between these two sets of predictors. We find that model (2) underperforms compared to model (1). For ~~2~~ example, _ROOS_[increases from 3.64 in model (2) to 4.64 in model (1), and] _R_[2] _OOS_[increases from 4.37 to 4.48 for the full sample. The incremental R][2] values indicate the magnitude of the interaction effect. The results show valuable information for return prediction embedded in the interactions between aggregate predictors and bond characteristics. The predictability of bond characteristics can change over time, and the predictability of aggregate variables may become evident in specific subsamples of bonds. By putting both sets of predictors in the ML model, we capture their important interaction effects and increase the model’s predictive power. 

Furthermore, our analysis shows model (1) consistently outperforms models (3) and (4) across the entire sample and various subsamples. For ~~2~~ instance, model (1) achieves an _ROOS_[of 4.64% and an] _[ R]_[2] _OOS_[of 4.48% for] ~~2~~ the full sample, whereas model (3) reports an _ROOS_[of 1.44% and an] _[ R]_[2] _OOS_ ~~2~~ of 1.90%, and model (4) yields an _ROOS_[of 2.52% and an] _[ R]_[2] _OOS_[of 4.46%.] This finding indicates a significant loss in predictability when either predictor set is excluded. Additionally, comparisons between models (3) 

6 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

## **Table 3** 

Predictive evidence of returns for subsamples. 

||Panel A: Rating Subsamples|Panel A: Rating Subsamples|Panel A: Rating Subsamples|||AA<br>A<br>BBB<br>NIG|
|---|---|---|---|---|---|---|
||||_OS_<br>AA<br>AA<br>A<br>BBB<br>NIG||_R_2<br>_OOS_||
|||_R_<br><br>_O_|||||
|||A|||AAA||
||MeanC<br>Lasso<br>PLS<br>RF<br>NN2|0.<br>2.<br>-1<br>4.<br>3.|10<br>0.30***<br>0.56***<br>0.54***<br>-0.04<br>62***<br>2.17***<br>2.81***<br>2.93***<br>2.06***<br>.22<br>-4.73<br>-1.39<br>-0.82<br>0.14<br>61***<br>4.50***<br>5.46***<br>5.32***<br>2.77***<br>38***<br>3.43***<br>5.04***<br>4.63***<br>2.97***||0.13<br>3.87<br>0.91<br>5.01<br>2.76|0.06<br>0.44<br>0.60<br>0.10<br>2.89<br>3.17<br>3.19<br>2.04<br>-2.20<br>1.19<br>2.20<br>2.83<br>4.36<br>5.53<br>5.67<br>3.07<br>2.84<br>6.27<br>6.35<br>5.35|
||Panel B: Maturity||Subsamples|||TMT2<br>TMT3<br>TMT4<br>TMT5|
|||~~2~~|_OS_<br>T1<br>TMT2<br>TMT3<br>TMT4<br>TMT5|_R_2<br>_OOS_|||
|||_R_<br><br>_O_|||||
|||TM||TMT1|||
||MeanC<br>Lasso<br>PLS<br>RF<br>NN2|0.<br>1.<br>-9.<br>6.<br>2.|62***<br>0.49***<br>0.33**<br>0.26**<br>0.27**<br>15<br>2.53***<br>2.91***<br>2.79***<br>2.68***<br>01***<br>-2.44*<br>0.21<br>0.69<br>0.64<br>01***<br>5.45***<br>5.22***<br>4.39***<br>3.69***<br>82***<br>4.02***<br>5.23***<br>4.40***<br>3.57***|0.32<br>2.96<br>-0.02<br>5.30<br>5.98||0.62<br>0.49<br>0.33<br>0.26<br>1.15<br>2.53<br>2.91<br>2.79<br>1.00<br>2.37<br>2.04<br>2.40<br>6.01<br>5.45<br>5.22<br>4.39<br>6.11<br>6.37<br>4.58<br>5.11|
||Panel C: Privat|e a|nd Public Subsamples|||_R_2<br>_OOS_<br>Private<br>Public|
||||_R_<br>~~2~~<br>_OOS_<br>_R_<br>~~2~~<br>_O_<br>Private<br>Public<br>Dif|_OS_;Δ<br>ference|||
||MeanC<br>Lasso<br>PLS<br>RF<br>NN2||0.31**<br>0.34***<br>-0.<br>2.65***<br>2.74***<br>-0.<br>1.02***<br>1.11***<br>-0.<br>4.71***<br>4.35***<br>0.3<br>4.17***<br>4.60***<br>-0.|03<br>09<br>09<br>6<br>43||0.22<br>0.42<br>2.76<br>2.78<br>1.24<br>1.46<br>4.47<br>4.49<br>5.13<br>5.90|



This table reports the return predictive evidence of corporate bond sub-samples on rating, maturity, and private-public type. In Panel A, we sort bonds into five rating groups: AAA, AA, A, BBB, and NIG. In Panel B, we sort bonds into quintile groups by maturity: TMTj where j = 1, 2, 3, 4, 5 indicates increasing maturity quintiles with TMT1 denoting the shortest-maturity group, and TMT5 being the longest-maturity group. In Panel C, we classify the bonds by the private-public type of the issuance firm. We also provide subpanels for different sample periods in appendix Table B.5. We report for five predictive models, introduced in Section 2.1 and Appendix A. The left panel presents _R_ ~~2~~ _OOS_[(%) (see][ Eq. (4)][), and the significance of Fama-MacBeth] _[ t]_[-statistics. The right panel presents] _[ R]_[2] _OOS_[(%) (see][ Eq. (2)][). For the private and public] company bond predictability difference, we report the _R_ ~~2~~ _OOS_ ;Δ[(%)][defined][in][Eq.][(5)][with][the][two-sample][Fama-MacBeth] _[t]_[-statistics.][The] _[t]_[-statistics][incorporate] Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

and (4) show models using only bond characteristics generally exhibit ~~2~~ superior _ROOS_[and] _[ R]_[2] _OOS_[, in most subsamples. For example, in predicting] the A-rated bonds, the model relying solely on bond characteristics ~~2~~ achieves an _ROOS_[of][3.41%,][whereas][the][models][using][only][aggregate] ~~2~~ predictors achieves an _ROOS_[of][1.53%.][This][result][suggests][that][bond] characteristics contain more predictive information compared to aggregate predictors. 

## **5. Forecast-implied trading strategies** 

## _5.1. Long-short trading strategies_ 

This section examines whether ML return predictions generate investment profits and if these profits are robust across different ratings and private-public classifications. We construct model-forecast-implied long-short portfolios to assess these profits. Each month, we sort individual bonds into quintiles based on predicted returns, creating valueweighted portfolios that are rebalanced monthly. A long-short portfolio is formed by going long on the highest (quintile 5) and shorting the lowest (quintile 1). Fig. B.2 displays cumulative portfolio returns using six predictive methods: MeanC, Lasso, PLS, RF, NN1, and NN2. We observe monotonic spreads for sorted portfolio returns, confirming the predictive evidence. The long-short portfolio return spread is substantial, with the premium primarily coming from the long side. 

Table 5 Panel A reports performance measures of the long-short portfolio across five samples: the entire bond universe, IG bonds, NIG bonds, private bonds, and public bonds. The strategies utilize different samples of bonds, but return predictions come from the same model. 

Nonlinear methods (RF and NN2) outperform linear methods (Lasso and PLS), with the RF model achieving the best performance: a 1.95% monthly average return for the whole sample, 1.85% for IG, 2.51% for NIG, 2.06% for private bonds, and 1.55% for public bonds. It also produces an annualized Sharpe ratio of 3.27 for the whole sample, 3.30 for IG, and 3.34 for private bonds. The Fama-French five-factor model does not fully explain these strategies. Private bonds yield higher average returns than public bonds; for instance, the RF strategy earns 0.51% higher returns and a 0.94 point higher Sharpe ratio for private bonds. In summary, ML return predictions generate promising investment profits, robust across IG and NIG bonds, as well as private and public bonds. 

Table 5 shows private bonds provide higher investment gains than public bonds, and Table 3 indicates that both bond types exhibit similar _R_[2] _OOS_[.][These][two][findings][may][seem][“][inconsistent.][”][However,][no] empirical evidence shows a direct relation between higher return predictability, _R_[2] _OOS_[,][and][increased][investment][gain.][Rapach][et][al.][(2010)] and Kelly et al. (2024) also encounter this issue. They argue that no theoretical basis exists for using the _R_[2] _OOS_[to infer the investment gain of] a predictive model, because both forecast variance and forecast bias influence the predictive accuracy measure, and the forecast variance term can significantly distort _R_[2] _OOS_[.] 

## _5.2. Direction-implied trading strategies_ 

In addition to the long-short trading strategy that focuses on tail return predictions, we develop a direction-implied trading strategy for individual bonds with a market timing feature. We construct this strategy by longing bonds with positive predicted returns and shorting those 

7 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Fig. 1.** Heat map of relative variable importance. Fifty-one predictors are ranked in terms of overall model contribution. We add the prefix “X” for aggregate predictors and “Z” for bond characteristic predictors to distinguish the two groups of predictors. Predictors are ordered based on the average rank of variable importance across all models, with the most important characteristics at the top and the least important at the bottom. Columns correspond to individual models, and color gradients within each column indicate the most important (dark) to least important (light) variables. Details of the predictors can be found in Appendix Table B.1, and details of the predictive models can be found in Section 2.1 and Appendix A. 

with negative predicted returns. This direction-implied strategy is a long-short portfolio that combines the long and short legs, but its logic differs from the long-short strategy in Section 5.1. In extreme cases, the direction-implied strategy goes long on all bonds during a market boom and shorts all bonds in a market bust. By contrast, the long-short strategy maintains fixed positions for the long and short legs; that is, going long on the top 20% and shorting the bottom 20%. 

Fig. B.3 shows the cumulative returns of the long-leg, short-leg, and direction-implied strategies. The direction-implied strategies of MeanC, PLS, and NN2 yield higher average returns than their long-short counterparts. Table 5 Panel B reveals that the higher average returns for MeanC and NN2 primarily come from NIG bonds. The RF strategy 

achieves a monthly average return of 1.56% and an annualized Sharpe ratio of 1.32. Additionally, the turnover ratio for the RF directionimplied strategy is 20% lower than that of the long-short strategy, indicating reduced transaction costs. Private bonds also provide higher average returns for PLS and NN2. The results show the direction-implied strategy can also deliver investment profits and diversify from the longshort strategy. 

## _5.3. Investment gains: aggregate predictors vs. bond characteristics_ 

In this subsection, we explore how aggregate predictors and bond characteristics contribute to investment in bond return profits 

8 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Fig. 2.** Heat map of variable importance. 

**Color should be used for this figure in print.** This figure reports the variable importance of 51 predictors. We add the prefix “X” for aggregate predictors and “Z” for bond characteristic predictors to distinguish the two groups of predictors. The order of predictors follows Fig. 1. Moreover, the columns correspond to each model. A positive number (in green) means the variable improves OOS prediction, and a negative number (in red) means the predictor does not help OOS prediction. Details of the predictors can be found in Appendix Table B.1, and details of the predictive models can be found in Section 2.1 and Appendix A. 

predictions. We examine whether incorporating aggregate predictors significantly enhances the performance of bond return prediction models compared to using only bond characteristics. Additionally, we investigate the variable importance related to the predictive performance discussed in Section 4, as well as the investment gains from these predictors. Table 6 shows the investment performance using only aggregate predictors or bond characteristics to predict bond returns, with the investment universe comprising all bonds in the cross section. 

We predict market-level returns using only aggregate predictors, which excludes the use of a long-short trading strategy. Nonetheless, time-series variation remains applicable. The direction-implied trading strategy with aggregate predictors yields monthly returns of 0.43% (0.37%) and annual Sharpe ratios of 1.45 (1.20) for Lasso (RF), indicating significant alpha relative to the Fama-French five-factor model. Using only bond characteristics, the long-short strategy of neural networks earns monthly returns of 1.32% with a 1.85 Sharpe ratio. 

However, adding aggregate predictors increases the average return to 1.57% and the Sharpe ratio to 3.30. The direction-implied strategy of the RF model also benefits from this addition, raising average returns from 0.76% to 1.56%. Overall, both aggregate predictors and bond characteristics enhance investment gains; dropping either would lead to lower performance. 

## _5.4. Investment gains after transaction cost_ 

We further investigate how transaction costs impact the investment performance and turnover of various predictive strategies for corporate bonds, and whether substantial profits remain achievable after accounting for these costs. The literature suggests several transaction cost measures for the corporate bond market, which are significant for trading. Edwards et al. (2007) show transaction costs for corporate bonds range from 20 to 80 basis points (bps), depending on trade size, 

9 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

## **Table 4** 

Predictive evidence with different subsets of predictors. 

|(1) Aggregate+Characteristic<br>_R_<br>~~2~~<br>_OOS_<br>_R_2<br>_OOS_<br>Panel A: Rating Subsample|(2) Aggregate+CharacteristicNo Interaction<br>_R_<br>~~2~~<br>_OOS_<br>_R_2<br>_OOS_|(3) Only Aggregate<br>_R_<br>~~2~~<br>_OOS_<br>_R_2<br>_OOS_|(4) Only Characteristic<br>_R_<br>~~2~~<br>_OOS_<br>_R_2<br>_OOS_|
|---|---|---|---|
|AAA<br>4.61***<br>5.01<br>AA<br>4.50***<br>4.36<br>A<br>5.46***<br>5.53<br>BBB<br>5.32***<br>5.67<br>NIG<br>2.77***<br>3.07|3.73***<br>4.58<br>3.86***<br>4.44<br>4.22***<br>5.18<br>4.36***<br>5.39<br>2.69***<br>3.25|0.03<br>0.50<br>0.31<br>1.08<br>1.53**<br>2.03<br>1.91***<br>2.24<br>1.00**<br>2.04|4.41***<br>5.84<br>2.68***<br>3.98<br>3.41***<br>5.38<br>3.49***<br>6.03<br>0.59<br>2.81|
|Panel B: Maturity Subsample||||
|Maturity 1<br>6.01***<br>5.30<br>2<br>5.45***<br>5.71<br>3<br>5.22***<br>5.42<br>4<br>4.39***<br>3.87<br>Maturity 5<br>3.69***<br>3.66|4.69***<br>5.22<br>-0.25<br>4.35***<br>5.38<br>1.30*<br>4.14***<br>5.34<br>1.75**<br>3.50***<br>4.00<br>1.41**<br>2.80***<br>3.47<br>1.31**|1.11<br>2.15<br>*<br>2.30<br><br>2.00<br>*<br>1.80|4.81***<br>6.18<br>3.28***<br>5.92<br>2.79***<br>5.79<br>2.23***<br>3.68<br>1.35<br>3.19|
|Panel C: Full Sample and Private and Public Subsamples||||
|All<br>4.64***<br>4.48<br>Private<br>4.71***<br>4.47<br>Public<br>4.35***<br>4.49|3.64***<br>4.37<br>1.44***<br>3.72***<br>4.24<br>1.42***<br>3.48***<br>4.38<br>1.34**|1.90<br><br>1.83<br>2.01|2.52***<br>4.46<br>2.71***<br>4.29<br>2.15**<br>4.72|



This table reports the return predictive evidence of RF models, with (1) both aggregate predictors and bond characteristics, (2) both aggregate predictors and bond characteristics without interaction between two groups, (3) only aggregate predictors, and (4) only bond characteristics. Panel A reports results for the five rating subsamples, Panel B is for the five maturity subsamples, and Panel C reports the results for the whole sample and for the private-public bond subsample. The performance measures are _R_ ~~2~~ _OOS_[(%) (see][ Eq. (4)][) and] _[ R]_[2] _OOS_[(%) (see][ Eq. (2)][). The] _[ t]_[-statistics incorporate][ Newey-West (1987)][ robust standard errors, with *, **, and ***] denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

## **Table 5** 

Investment performance. 

|**Table 5**<br>Investment performance.|||||
|---|---|---|---|---|
|All<br>Mean<br>_α_<br>SR<br>Panel A: Long-Short Portfolio Returns|IG<br>Mean<br>_α_<br>SR|NIG<br>Mean<br>_α_<br>SR|Private<br>Mean<br>_α_<br>SR|Public<br>Mean<br>_α_<br>SR|
|MeanC<br>0.68***<br>0.65***<br>1.15<br>Lasso<br>0.84***<br>0.77***<br>2.05<br>PLS<br>1.13***<br>1.16***<br>2.39<br>RF<br>1.95***<br>2.09***<br>3.27<br>NN2<br>1.57***<br>1.66***<br>3.30|0.59***<br>0.58***<br>1.14<br>0.81***<br>0.75***<br>2.00<br>1.09***<br>1.13***<br>2.36<br>1.85***<br>2.03***<br>3.30<br>1.49***<br>1.59***<br>3.46|0.99***<br>1.10***<br>0.83<br>1.39***<br>1.45***<br>1.33<br>2.13***<br>2.29***<br>1.60<br>2.51***<br>2.53***<br>1.97<br>2.78***<br>2.83***<br>1.93|0.73***<br>0.71***<br>1.16<br>0.91***<br>0.89***<br>2.12<br>1.22***<br>1.30***<br>2.19<br>2.06***<br>2.27***<br>3.34<br>1.64***<br>1.76***<br>3.26|0.49***<br>0.40***<br>0.80<br>0.63***<br>0.52***<br>1.25<br>0.93***<br>0.88***<br>1.76<br>1.55***<br>1.53***<br>2.40<br>1.44***<br>1.48***<br>2.41|
|Panel B: Direction-Implied Portfolio Returns|||||
|MeanC<br>0.79**<br>0.79**<br>0.42<br>Lasso<br>0.82***<br>0.81***<br>0.83<br>PLS<br>1.35***<br>1.49***<br>0.83<br>RF<br>1.56***<br>1.59***<br>1.32<br>NN2<br>1.74***<br>1.82***<br>1.27|0.38*<br>0.27<br>0.37<br>0.82***<br>0.79***<br>0.81<br>1.42***<br>1.44***<br>0.90<br>1.62***<br>1.81***<br>1.68<br>1.40***<br>1.47***<br>1.27|1.03***<br>0.93**<br>0.57<br>1.34***<br>1.25***<br>0.96<br>1.79***<br>1.84***<br>0.87<br>2.11***<br>2.00***<br>1.33<br>2.94***<br>2.97***<br>1.36|0.80**<br>0.98***<br>0.44<br>0.82***<br>0.79***<br>0.83<br>1.33***<br>1.44***<br>0.83<br>1.33***<br>1.41***<br>1.20<br>1.59***<br>1.73***<br>1.17|0.57**<br>0.65**<br>0.43<br>0.74***<br>0.71***<br>0.93<br>0.95***<br>1.06***<br>0.56<br>1.41***<br>1.48***<br>1.06<br>1.49***<br>1.49***<br>0.90|



This table evaluates the investment gain of the two value-weighted investment strategies based on return predictions. Panel A reports the long-short strategy and Panel B reports the direction-implied trading strategy. In Panel A, each month, we sort bonds on predicted returns, creating value-weighted portfolios that are rebalanced monthly. We form a long-short portfolio by taking a long position in bonds in the highest quintile portfolio (quintile 5) and shorting bonds in the lowest quintile portfolio (quintile 1). In Panel B, we construct the direction-implied portfolio by longing bonds with positive predicted returns and shorting those with negative predicted returns. Our direction-implied strategy is a long-short portfolio that combines the long and short legs, but its logic differs from the long-short trading strategy. The performance measures include monthly average returns (%), alphas (%) on a factor model, and annualized Sharpe ratios. We test the portfolios and obtain alphas using the five-factor model (MKT, SMB, HML, TERM, and DEF) in Fama and French (1993) with a test period from January 1996 to September 2020. The results are based on five predictive models (MeanC, Lasso, PLS, RF, and NN2) introduced in Section 2.1 and Appendix A. The _t_ -statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

with smaller issue sizes incurring higher costs. Bali et al. (2022) use the effective spread as a proxy for transaction costs. However, estimating these costs for our early samples from the 1970s is infeasible due to data limitations. Instead, we follow Gu et al. (2020) and report the turnover of our strategy and investment performance net of transaction costs for different cost levels. 

Table 7 presents average turnover percentages, monthly returns, and Sharpe ratios for transaction costs ranging from 0 to 80 bps. The monthly rebalanced turnover ratio is low for the MeanC strategy but exceeds 100% for the RF and NN2 strategies. Nonetheless, substantial 

investment gains net of transaction costs remain. The value-weighted RF long-short (direction-implied) strategy earns a 0.86% (0.65%) monthly return with a 1.42 (0.55) annualized Sharpe ratio, even with 80 bps charged per transaction. 

The investment gains from our trading strategies do not depend on small bonds, which have higher transaction costs (Edwards et al., 2007). In the appendix, Figs. B.4 and B.5 show the equal-weighted long-short and direction-implied strategies earn average returns similar to their value-weighted counterparts, alleviating concerns about transaction costs. 

10 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

## **Table 6** 

Investment performance with a subset of predictors. 

|**Table 6**<br>Investment performance with a subset of predictors.|||
|---|---|---|
|Aggregate+Characteristic<br>Mean<br>_α_<br>SR<br>Panel A: Long-Short Portfolio Returns|Only Aggregate<br>Mean<br>_α_<br>SR|Only Characteristic<br>Mean<br>_α_<br>SR|
|MeanC<br>0.68***<br>0.65***<br>1.15<br>Lasso<br>0.84***<br>0.77***<br>2.05<br>PLS<br>1.13***<br>1.16***<br>2.39<br>RF<br>1.95***<br>2.09***<br>3.27<br>NN2<br>1.57***<br>1.66***<br>3.30||0.68***<br>0.65***<br>1.15<br>0.47***<br>0.37***<br>1.22<br>0.83***<br>0.79***<br>1.83<br>1.93***<br>2.05***<br>2.90<br>1.32***<br>1.37***<br>1.85|
|Panel B: Direction-Implied Portfolio Returns|||
|MeanC<br>0.79**<br>0.79**<br>0.42<br>0.28<br>Lasso<br>0.82***<br>0.81***<br>0.83<br>0.43<br>PLS<br>1.35***<br>1.49***<br>0.83<br>0.37<br>RF<br>1.56***<br>1.59***<br>1.32<br>0.37<br>NN2<br>1.74***<br>1.82***<br>1.27<br>0.43|***<br>0.26***<br>0.90<br>***<br>0.43***<br>1.45<br>***<br>0.36***<br>1.22<br>***<br>0.37***<br>1.20<br>***<br>0.43***<br>1.43|0.85**<br>0.79*<br>0.40<br>0.26***<br>0.30***<br>0.93<br>0.41***<br>0.40***<br>1.32<br>0.76***<br>0.75***<br>2.03<br>0.63***<br>0.66***<br>1.77|



This table reports the investment gain of ML investment strategies, with both aggregate predictors and bond characteristics, with only aggregate predictors and only bond characteristics. Panel A reports the long-short trading strategy and Panel B for the direction-implied trading strategy. The only aggregate strategy in Panel A is not applicable, so we leave the cells blank. The performance measures include monthly average returns (%), alphas (%) on a factor model, and annualized Sharpe ratios. We test the portfolios and obtain alphas using the five-factor model (MKT, SMB, HML, TERM, and DEF) in Fama and French (1993) with a test period from January 1996 to September 2020. The results are based on five predictive models (MeanC, Lasso, PLS, RF, and NN2). The _t_ -statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

**Table 7** 

Investment gains with transaction costs. 

|Turnover (%)<br>Panel A: Long-Short Portfolio Returns|Monthly Average Returns (%)<br>0 bp<br>20 bp<br>40 bp<br>60 bp<br>80 bp|Annualized Sharpe Ratio<br>0 bp<br>20 bp<br>40 bp<br>60 bp<br>80 bp|
|---|---|---|
|MeanC<br>67.94<br>Lasso<br>97.02<br>PLS<br>98.16<br>RF<br>136.65<br>NN2<br>112.81|0.68<br>0.55<br>0.41<br>0.28<br>0.14<br>0.84<br>0.64<br>0.45<br>0.26<br>0.06<br>1.13<br>0.94<br>0.74<br>0.55<br>0.35<br>1.95<br>1.68<br>1.41<br>1.13<br>0.86<br>1.57<br>1.34<br>1.12<br>0.89<br>0.67|1.15<br>0.92<br>0.70<br>0.47<br>0.24<br>2.05<br>1.58<br>1.11<br>0.63<br>0.15<br>2.39<br>1.99<br>1.58<br>1.17<br>0.75<br>3.27<br>2.81<br>2.34<br>1.88<br>1.42<br>3.30<br>2.85<br>2.39<br>1.92<br>1.44|
|Panel B: Direction-Implied Portfolio Re|turns||
|MeanC<br>31.71<br>0.7<br>Lasso<br>113.64<br>0.8<br>PLS<br>118.62<br>1.3<br>RF<br>113.90<br>1.5<br>NN2<br>114.79<br>1.7|9<br>0.73<br>0.67<br>0.60<br>0.54<br><br>2<br>0.60<br>0.37<br>0.14<br>-0.08<br><br>5<br>1.12<br>0.88<br>0.64<br>0.40<br><br>6<br>1.33<br>1.10<br>0.87<br>0.65<br><br>4<br>1.51<br>1.28<br>1.05<br>0.82<br>|0.42<br>0.39<br>0.36<br>0.32<br>0.29<br>0.83<br>0.60<br>0.37<br>0.14<br>-0.08<br>0.83<br>0.68<br>0.54<br>0.39<br>0.25<br>1.32<br>1.13<br>0.94<br>0.74<br>0.55<br>1.27<br>1.10<br>0.94<br>0.77<br>0.60|



This table evaluates the impact of transaction costs on ML investment strategies. We report the turnover ratio of the investment strategies based on ML, and their monthly returns and Sharpe ratios net of different levels of transaction costs. The results are based on five predictive models (MeanC, Lasso, PLS, RF, and NN2). The test period spans from January 1996 to September 2020. 

## **6. Further evaluations and robustness results** 

## _6.1. Time-varying return predictability_ 

We next investigate how the predictability of corporate bond returns varies over time under different economic conditions. The preceding analyses demonstrate individual corporate bond returns are predictable using ML models and the predictability is time-varying. The level of predictability, distinct from return forecasts, is influenced by the signalto-noise ratio represented by R². Our long-span data sample allows for a deeper analysis of this time-varying predictability over business cycles. We examine predictability under different economic conditions using 12 state variables, which are categorized into three major areas: timevarying risk aversion, economic risks, and cross-sectional factors, detailed in Appendix Table B.6. Table 8 presents the results of timeseries _R_[2] _OOS_[(TSR][2][).][9][For][brevity,][we][focus][on][the][results][from][the][RF] model, which show the strongest predictive power, and conduct subsample analyses for IG and NIG bonds. 

First, we find return predictability is higher when investors are risk averse, as indicated by the risk aversion index (BEX) in Bekaert et al. (2022), and this pattern holds for both IG and NIG bonds. Our results are consistent with the finding of Bianchi et al. (2021) in the treasury bond market that risk aversion is a key driver of time-varying predictability. 

Second, we find return predictability is higher during periods when CFN is low and SVAR, VIX, and illiquidity are high, which signal a bearish economic state. These findings align with equity market studies. Dangl and Halling (2012) report stronger return predictability for S&P 500 when the economy is weaker, whereas Avramov et al. (2023) find higher stock return predictability during periods of high VIX, high realized volatility, and illiquidity. 

Third, we find the return predictability is higher during periods when the cross-sectional factor (CSF) explanatory power is strong in the corporate bond market. The time series of cross-sectional _R_[2] (Kelly et al., 2023) is used as a measure of the strength of the factor explanatory power.[10] A high CSF indicates strong factor explanatory power. We find 

> 9 Results for the long-short strategy returns and direction-implied strategy returns are available upon request. 

> 10 We fit a five-factor IPCA model (Kelly et al., 2023) with our test sample. In each month, we regress bond returns on five characteristics-based betas in the cross section to collect the cross-sectional _R_[2] . 

11 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Table 8** 

Time-varying return predictability. 

|**Table 8**<br>Time-varying|return predictability.|||
|---|---|---|---|
||ALL<br>Low<br>High|IG<br>Low<br>High|NIG<br>Low<br>High|
|ADS<br>BEX<br>CFN<br>CSF<br>DFY<br>IDP<br>LIQ<br>SNT<br>SRP<br>SVAR<br>TBL<br>VIX|4.20<br>**5.07**<br>3.51<br>**5.76**<br>**4.86**<br>4.43<br>4.35<br>**4.93**<br>**5.58**<br>3.70<br>4.26<br>**5.02**<br>4.61<br>**4.67**<br>4.52<br>**4.76**<br>**5.17**<br>4.20<br>4.56<br>**4.72**<br>**5.48**<br>3.81<br>4.41<br>**4.86**|4.60<br>**6.13**<br>4.53<br>**6.20**<br>4.93<br>**5.79**<br>5.17<br>**5.57**<br>**6.51**<br>4.24<br>**5.81**<br>4.94<br>**5.77**<br>4.97<br>5.31<br>**5.42**<br>**6.14**<br>4.69<br>5.27<br>**5.46**<br>**6.56**<br>4.19<br>4.86<br>**5.87**|**3.07**<br>2.47<br>1.34<br>**4.20**<br>**3.25**<br>2.33<br>1.65<br>**3.87**<br>**3.26**<br>2.29<br>2.43<br>**3.11**<br>2.39<br>**3.15**<br>2.39<br>**3.14**<br>2.48<br>**3.02**<br>2.70<br>**2.85**<br>**3.69**<br>1.86<br>2.73<br>**2.82**|



This table reports the time-varying return predictability using the RF model by market state. We report the time-series of _R_[2] _OOS_[(TSR][2][),][aligned][with][market] states defined as high (above median) and low (below median). Twelve explanatory variables are considered, including Aruoba et al. (2009) business conditions index (ADS), Bekaert et al. (2022) risk aversion index (BEX), Chicago Fed National Activity Index (CFN), default yield spread (DFY), industrial production growth (IDP), Pastor and Stambaugh (2003) market liquidity (LIQ), Huang et al. (2015) investor sentiment (SNT), smooth recession probability (SRP), realized market volatility (SVAR), Treasury Bill rate (TBL), VIX, and cross-sectional factor (CSF) explanatory power on a five-factor IPCA model. Lager values are highlighted in bold for comparison between low and high states. Results for long-short trading strategy returns (LS) and direction-implied trading strategy returns (DI) as measures of predictability are available upon request. 

compelling evidence in the NIG sample that high CSF is associated with high _R_[2] _OOS_[, while we find weak evidence in the IG bonds. For NIG bonds,] TSR[2] is 3.87 during high CSF periods, compared to 1.65 during low CSF periods. 

Overall, there is evidence that bond return predictability varies over time and is influenced by investor risk aversion, economic conditions, and CSF explanatory power. These results complement the findings in the equity market (e.g., Rapach et al., 2010; Dangl and Halling, 2012; Avramov et al., 2023). 

## _6.2. Robustness check for bond size and liquidity_ 

For robustness, we further study how the size and liquidity of bonds influence the return predictability and investment performance of corporate bonds, specifically whether smaller and less liquid bonds are more predictable or profitable when trading on predicted returns. Avramov et al. (2023) find stock return predictability significantly decreases when excluding small, distressed, and difficult-to-arbitrage stocks. Similarly, we conduct subsample analyses to determine whether small and illiquid bonds drive our results. We sort bonds into size quintiles based on the principal amount and liquidity quintiles using the Amihud (2002) illiquidity measure.[11] 

Table 9 Panel A.1 reports the results for five size groups, where label 1 indicates small bonds and label 5 indicates large bonds. We do not find compelling evidence that small bonds are more predictable, nor is there a clear pattern showing that _R_[2] _OOS_[changes][monotonically][as][the][size] quintile increases. In Table 9 Panel A.2, the most liquid bonds in group 1 exhibit a similar level of predictability as the most illiquid bonds in group 5. The results do not suggest that bond return predictability is correlated with bond size or liquidity. 

> 11 We follow Lin et al. (2011) to calculate the Amihud illiquidity measure, which is applicable only for NAIC and TRACE data. We have 359,708 observations with liquidity measures after merging with our bond data. 

Table 9 Panels B.1 and B.2 display investment gains across size and liquidity groups. On the one hand, small bonds show higher investment gains than large bonds for both long-short and direction-implied strategies. On the other hand, illiquid bonds exhibit better investment performance, suggesting that small and illiquid bonds yield higher trading gains based on the ML return forecasts, consistent with Avramov et al. (2023) in the stock market. However, large and liquid bonds still achieve decent returns; for instance, the long-short trading strategy of the RF model on large bonds earns a monthly alpha of 1.66% and an annualized Sharpe ratio of 3.21. 

Collectively, we find that investment strategies yield higher returns for small and illiquid bonds relative to large and liquid ones, whereas predictive measures do not differ across size or liquidity groups. This finding provides insights to help clarify the differences in return predictability between private and public bonds. Table B.4 indicates that 20% of private bonds are in size quintile 1, whereas only 6% of public bonds fall into this category. Thus, the superior performance of private bonds relative to public ones can be partly attributed to their smaller size. Regarding liquidity, we find no significant differences between private and public bonds. 

## _6.3. Prediction and investment gains from including private bonds_ 

Finally, we investigate whether including both private and public bonds in predictive models enhances OOS performance and investment returns compared to using only private or public bonds. To address these issues, we rebuild the predictive models (Lasso and RF) using only private bonds and assess their OOS performance. Similarly, we can examine whether private bond information aids in predicting public bond returns by reconfiguring the models using only public bonds. 

~~2~~ Table 10 Panel A presents the _ROOS_[and] _[R]_[2] _OOS_[for][predicting][private] and public bond returns. We consider three distinct predictive modeling The trains on the entire dataset and specifications. first specification then makes predictions for private and public bond subsamples. The second specification restricts training to private bonds only, whereas the third focuses exclusively on public bonds. We compare the predictive performance between the “all sample” and “exclusive sample” specifications for both bond types. Panel A of Table 10 shows that when the ~~2~~ predictive model is trained using only private or public bonds, _ROOS_[and] _R_[2] _OOS_[decline][in][seven][out][of][eight][pairs][of][comparisons,][except][for][the] _R_[2] _OOS_[for public bonds with the Lasso model. Neglecting either private or] public bonds reduces return predictive information for both, indicating that training models on the entire bond dataset improves the predictability of returns for both bond types. 

Panel B of Table 10 presents the investment performance based on return predictions for private and public bonds, including average returns, alphas relative to the Fama-French five-factor model, and Sharpe ratios. We compare the investment gains between the “all sample” and “exclusive sample” specifications for both bond types. The “all sample” specification outperforms the “exclusive sample” in average returns in seven cases, alphas in six cases, and Sharpe ratios in six out of eight comparisons. For example, using a direction-implied investment strategy in private bonds with RF predictions results in a loss of 0.31% in average returns, 0.19% in alphas, and 0.46 in Sharpe ratios when excluding the public bond sample. Similarly, applying a long-short strategy to public bonds with Lasso predictions leads to declines of 0.07% in average returns, 0.02% in alphas, and 0.29 in Sharpe ratios when ML models are trained solely on public bonds. Overall, the “all sample” specification shows significantly better OOS investment performance than the “exclusive sample.” These comparisons indicate that neglecting either bond type considerably reduces prediction efficiency and investment gains. 

Although both private and public bonds offer incremental predictive information, the benefit of including private bonds remains ambiguous. On one hand, the illiquidity and stale information associated with 

12 

_Journal of Banking and Finance 171 (2025) 107372_ 

_G. Feng et al._ 

## **Table 9** 

Return predictability and investment gains for size and liquidity subsamples. 

||||||||
|---|---|---|---|---|---|---|
|Panel A.1: Siz|_R_<br>~~2~~<br>_OOS_<br>1<br>2<br>3<br>e Groups|_R_<br>~~2~~<br>_OOS_|4<br>5||_R_2<br>_OOS_|4<br>5|
||||||1<br>2<br>3||
|MeanC<br>Lasso<br>PLS<br>RF<br>NN2|0.36<br>0.17<br>0.2<br>2.01<br>3.08<br>2.7<br>-1.93<br>0.84<br>-0.<br>4.19<br>4.47<br>4.5<br>5.83<br>4.24<br>4.0||8<br>0.24<br>0.31<br>2<br>2.74<br>-0.59<br>52<br>-1.94<br>-7.99<br>0<br>4.42<br>5.07<br>4<br>4.04<br>1.09||0.34<br>0.47<br>0.2<br>1.19<br>3.70<br>3.0<br>0.18<br>4.09<br>2.1<br>3.11<br>5.23<br>4.6<br>5.80<br>5.68<br>5.0|7<br>-0.14<br>0.66<br>5<br>2.11<br>3.17<br>5<br>-1.37<br>1.21<br>0<br>4.20<br>5.67<br>5<br>6.37<br>7.44|
|Panel A.2: Am|ihud Illiquidity Groups||||||
|MeanC<br>Lasso<br>PLS<br>RF<br>NN2|1.07<br>0.44<br>0<br>0.88<br>3.10<br>2<br>-17.13<br>-4.70<br>-3<br>5.80<br>5.88<br>4<br>4.51<br>3.50<br>4||.38<br>0.23<br>0.24<br>.08<br>3.48<br>3.03<br>.38<br>1.71<br>3.60<br>.52<br>5.40<br>4.57<br>.45<br>4.26<br>4.20||0.76<br>0.42<br>0.3<br>2.09<br>4.62<br>1.7<br>-7.04<br>1.57<br>-0.<br>6.01<br>6.94<br>3.5<br>6.46<br>5.08<br>5.7|3<br>0.26<br>0.20<br>5<br>3.75<br>2.98<br>18<br>3.60<br>4.03<br>6<br>5.60<br>4.16<br>5<br>4.23<br>6.29|
|High Size<br>Mean<br>_α_<br>SR<br>Panel B.1: Long-Short Portfolio Returns|||Low Size<br>Mean<br>_α_<br>SR|High|Amihud Illiquidity<br><br>_α_<br>SR|Low Amihud Illiquidity<br>Mean<br>_α_<br>SR|
|||||Mean|||
|MeanC<br>0.38***<br>0.34***<br>0.85<br>Lasso<br>0.76***<br>0.69***<br>1.91<br>PLS<br>0.92***<br>0.96***<br>2.08<br>RF<br>1.48***<br>1.66***<br>3.21<br>NN2<br>1.26***<br>1.31***<br>2.92|||0.64***<br>0.56***<br>1.23<br>0.99***<br>0.81***<br>1.90<br>1.31***<br>1.23***<br>2.20<br>2.02***<br>1.99***<br>3.50<br>1.92***<br>1.93***<br>2.87|0.71*<br>1.10*<br>1.71*<br>2.85*<br>2.34*|**<br>0.70***<br>0.77<br>**<br>1.03***<br>1.81<br>**<br>1.70***<br>2.25<br>**<br>2.82***<br>3.24<br>**<br>2.43***<br>2.83|0.52***<br>0.50***<br>1.24<br>0.48***<br>0.46***<br>1.47<br>0.56***<br>0.59***<br>1.55<br>1.22***<br>1.23***<br>2.65<br>0.93***<br>0.99***<br>2.63|
|Panel B.2: Direction-Implied Portfolio Returns|||||||
|MeanC<br>0.34<br>0.24<br>0.29<br>Lasso<br>0.64***<br>0.67***<br>0.71<br>PLS<br>1.10***<br>1.15***<br>0.84<br>RF<br>1.31***<br>1.30***<br>1.70<br>NN2<br>1.34***<br>1.42***<br>1.40|||0.61***<br>0.63***<br>0.90<br>0.78***<br>0.81***<br>0.76<br>1.09***<br>1.17***<br>0.91<br>1.75***<br>1.79***<br>1.20<br>1.70***<br>1.75***<br>1.12|0.47<br>0.92*<br>1.69*<br>1.91*<br>2.20*|0.37<br>0.27<br>**<br>0.89***<br>0.87<br>**<br>1.89***<br>0.89<br>**<br>2.11***<br>1.33<br>**<br>2.43***<br>1.45|0.70***<br>0.67***<br>0.61<br>0.50***<br>0.51***<br>0.91<br>0.59***<br>0.76***<br>0.69<br>0.99***<br>1.13***<br>1.12<br>0.79***<br>0.94***<br>0.89|



This table reports the return predictive evidence (Panels A.1 and A.2) and investment profits (Panels B.1 and B.2) of size and Amihud illiquidity subsamples (quintile portfolios). We sort bonds on size and illiquidity. Size is the amount outstanding for each bond. We calculate the Amihud illiquidity measure following the procedure in Lin, Wang, and Wu (2011). For Panel A.1, quintile 1 indicates the smallest size group, and for Panel A.2, it is the most liquid group. For Panels B.1 and B.2, bonds in size quintiles 1 and 2 are labelled as low size, and bonds in quintiles 4 and 5 are labelled as high size. The _t_ -statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

## **Table 10** 

Predicting and investing only in private or public company bonds. 

|Train<br>Test|(1) All Bonds<br>(2)<br>Private<br>(3)<br>Public<br>Private<br>Public<br>Private<br>Public|
|---|---|
|_R_<br>~~2~~<br>_OOS_<br>Predictive R2<br>_R_2<br>_OOS_<br>Long-Short Strategy<br>Mean<br>_α_<br>SR<br>Direction-Implied<br>Strategy<br>Mean<br>_α_<br>SR|4.71***<br>4.35***<br>4.59***<br>3.62***<br>4.47<br>4.49<br>3.99<br>4.01<br>2.06***<br>1.55***<br>2.04***<br>1.51***<br>2.27***<br>1.53***<br>2.28***<br>1.45***<br>3.34<br>2.40<br>3.39<br>2.13<br>1.33***<br>1.41***<br>1.02***<br>1.49***<br>1.41***<br>1.48***<br>1.22***<br>1.52***<br>1.20<br>1.06<br>0.74<br>1.13|



This table presents the predictive and investment outcomes of RF models for bonds issued by private and public companies, employing ML models trained with (1) all bonds, (2) exclusively on private bonds, and (3) exclusively on public bonds. In the head rows of the table, we report the labels for train data and test data. Predictive performances include _R_ ~~2~~ _OOS_[(][%][)][and] _[R]_[2] _OOS_[(%),][and][investment] performances include monthly average returns (%), alphas (%) on a factor model, and annualized Sharpe ratios. The _t_ -statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

private bonds may introduce noise, while potential market segmentation between private and public bonds could reduce model accuracy. On the other hand, if the market is integrated and efficient, incorporating both types of bonds may be beneficial, and incorporating a larger dataset with more observations can enhance estimation accuracy. Thus, whether 

including private bonds in the ML model is helpful is an empirical question.[12] Our analyses show training ML models on both private and public bonds significantly improves return predictability. This finding suggests a net gain in return prediction when including both private and public bonds in the predictive model. 

## **7. Conclusion** 

This paper presents compelling evidence of individual corporate bond return predictability using machine learning models and a large number of predictors from a comprehensive sample spanning 1976 to 2020. We confirm that traditional linear models generate positive return prediction performance; however, we find that nonlinear methods such as RF deliver more consistent and superior results across various bond subsamples and periods. Our findings expand the literature on bond return predictability and ML in asset pricing, providing valuable insights not only for academics but also for practitioners. 

Corporate bond return predictability varies over time, being higher during periods with increased investor risk aversion, deteriorating economic conditions, and stronger cross-sectional factor explanatory power. Both aggregate predictors and bond characteristics provide useful information for forecasting bond returns, and excluding either leads to reduced predictive efficiency and investment gains. Moreover, including both private and public bonds enhances bond return predictability. The results demonstrate ML models provide new insights into the predictability of corporate bond returns, which has important implications for improving our understanding of asset pricing for corporate 

> 12 We thank an anonymous referee for this insightful suggestion. 

13 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

bonds and the determination of risk premia. 

## **CRediT authorship contribution statement** 

**Guanhao Feng:** Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Resources, Project administration, Methodology, Investigation, Formal analysis, Conceptualization. 

**Xin He:** Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Conceptualization. **Yanchu Wang:** Writing – review & editing, Validation, Investigation, Formal analysis, Conceptualization. **Chunchi Wu:** Writing – review & editing, Writing – original draft, Supervision, Formal analysis, Data curation, Conceptualization. 

## **Appendix A. An overview of predictive models and designs** 

## _A.1. Linear regression_ 

The most used conditional expectation functional form in the empirical asset pricing literature is the predictive regression: _g_ ( _zi,t, xt_ ; _θ_ ) = [1 _, z_[ʹ] _i,t[,][ x]_[ʹ] _t_ ] _θ,_ (A-1) 

in which _zi,t_ is the characteristics for asset _i_ at time _t_ and _xt_ is the aggregate predictors at time _t_ . 

## _A.2. Forecast combination_ 

The combination forecast of _Ri,t_ +1 is usually the weighted average of _J_ individual forecasts: 

̂ _c J Ri,t_ +1[=] ∑ _ωi,j,t R_[̂] _i,j,t_ +1 _,_ (A-2) _j_ =1 

where _R_[̂] _ci,t_ +1[denotes the][combination forecast for the][return][of asset i][at][time] _[t]_[ +][ 1,] _[R]_[̂] _[i][,][j][,][t]_[+][1][denotes the return][forecast for][asset] _[ i]_[ at][time] _[t]_[+][1 given] predictor _j_ , and _ωi,j,t_ is the weight to combine individual forecasts. The MeanC takes equal weights in _ω_ = 1 _/J_ , and the median combination takes the median of {̂ _Ri,_ 1 _,t_ +1 _,_ ̂ _Ri,_ 2 _,t_ +1 _,_ ⋯ _,_ ̂ _Ri,J,t_ +1} We regard these robust combination forecasts as the benchmark in forecast performance evaluation. 

## _A.3. Dimension reduction_ 

We consider two classic dimension reduction techniques: principal component analysis regression (PCA) and partial least squares (PLS), which are commonly used for latent factor models in empirical asset pricing. One can use a low-dimension version of linearly transformed predictors to construct a predictive model and solve the bias-variance trade-off problem. 

PCA and PLS regression consist of a two-step procedure. The first step of PCA combines predictors with a small set of linear combinations that best _K_ preserve the covariance structure of these predictors. The first principal components are used in multiple regressions in the second step. The first step of PLS combines predictors with a small set of linear combinations that best preserve the covariance between predictors and outcomes. The first _K_ components are used in multiple regressions in the second step. In contrast to PCA, the PLS objective seeks _K_ linear combinations of the independent variables with a maximal predictive correlation with the dependent variable. K is set to 3 in our applications for both PCA and PLS. 

## _A.4. Regularized predictive regressions_ 

Regularized linear predictive regressions, such as Lasso and Ridge, are also commonly used in machine learning finance. By adding a penalty over ordinary linear regression, these two linear ML methods preserve the interpretability of linear models. Compared with PCA and PLS, the advantage of these two models is that they preserve the predictors without transforming them and thus keep the original interpretation. 

Lasso and Ridge share similar loss functions but have different regularization effects. Lasso adds an L1 norm penalty on the sum of residual squares, whereas Ridge adds an L2 norm penalty. On the one hand, the Lasso can shrink regression coefficients of useless predictors to zero to perform variable selection and achieve a sparse model. On the other hand, Ridge shrinks the regression coefficients of useless predictors to very small numbers. A tuning parameter controls the penalty weight, with a larger penalty weight imposing more shrinkage on the coefficients. To take advantage of and make a balance between Lasso and Ridge, the Elastic Net considers both L1 and L2 penalties and introduce a new parameter to control the weight between L1 and L2 penalties. We discuss the selection of tuning parameters in section A.7 and Table A.1. 

## _A.5. Ensemble tree models_ 

Regression trees are among the most popular ML algorithms. This approach is an alternative to nonlinear regressions to partition the space into smaller regions where the interaction is manageable. The ability to explore nonlinearity and the interaction for predictors provides an advantage of the regression tree model over all the above linear methods. However, the complex structure of a tree makes it prone to overfitting. Thus, we adopt two ensemble tree models to obtain relatively reliable forecasts: gradient boosted trees and RF. 

The gradient boosted trees model makes predictions by combining decisions from a sequence of simple trees. One starts with a shallow tree with a simple structure. The second simple tree fits the residuals from the first tree instead of the original dependent variable. Then, one further recursively fits the third tree with the second tree’s residuals. Finally, we have many trees and many weak forecasts from simple trees. The predictions by individual trees could be weak, but the prediction from adding up all these tree forecasts becomes strong. The ensemble forecast is the weighted sum of all these weak forecasts with decreasing weights. 

14 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

The RF model takes the average forecast from many different trees and adopts the bootstrap aggregating scheme. One draws _B_ number of data _B_ bootstrap samples and fits different trees. One usually chooses a random subset of predictors for each tree and fits a tree model with the bootstrap sample. Again, the predictions by individual trees could be weak, but the average of all _B_ numbers of forecasts is strong. Averaging the individual forecasts reduces the overfitting in individual bootstrap samples and provides a stable forecast. Tuning parameters and model selection for these two ensemble tree methods are discussed in section A.7 and Table A.1. 

## _A.6. Neural networks_ 

Neural network is one of the most powerful computational models inspired by the human brain’s neural structure. It potentially captures the complex and nonlinear relations in empirical data, thanks to the flexible model architecture and rich parameterization. We focus on the classic feedforward neural networks, which typically consist of an input layer, one or more hidden layers, and an output layer. In this paper, we apply neural networks with one and two hidden layers, namely NN1 and NN2, following the idea of shallow learning in GKX2020. NN1 has one hidden layer with 32 neurons, and NN2 has two hidden layers with 32 and 16 neurons, respectively. 

Many parameters and choices for neural networks exist. We follow GKX2020 to select ReLU as the activation function, stochastic gradient descent as the optimization tool, and the ideas of learning rate shrinkage, early stopping, batch normalization, and ensembles. More details of the tuning parameters are listed in Appendix Table A.1. 

## **Table A.1** 

Hyperparameters for all methods. 

|PCA|PLS|Lasso|Ridge|ENet|
|---|---|---|---|---|
|K|K|λ ∈exp(-40, 40)|λ ∈exp(-40, 40)|λ∈exp(-40, 40)|
|||||ρ∈(0,1)|
|GBRT<br>RF<br>NN1<br>NN2<br># Trees<br># Trees<br>Learning Rate<br>Learning Rate|||||
|B ∈{100,200}|B = 1000|LR ∈(10-4,10-2)|LR ∈(10-4,10-2)||
|# Min. Sample to|# Min. Sample to|L2 Penalty|L2 Penalty||
|split =200|split∈{200,400}|λ ∈exp(-5,0)|λ ∈exp(-5,0)||
|Learning Rate|# Feature=’sqrt’|Batch Size|Batch Size||
|LR ∈{0.01,0.05}||B =5000|B = 5000||
|# Depth||Epochs= 100|Epochs= 100||
|L ∈{3,5}||Patience=5|Patience=5||
|||Adam Para.=Default|Adam Para.= Default||
|||Ensemble =10|Ensemble =10||
|||# Neurons = 32|# Neurons= 32, 16||



This table describes the hyperparameters that we tune in each ML method as discussed in Appendix A. 

## _A.7. Deterministic cross-validation_ 

Many ML models require tuning parameters. We adopt a deterministic fivefold cross-validation scheme as illustrated in Fig. A.1. Standard randomized cross-validation is initially designed for independent observations. Our deterministic cross-validation design preserves the continuity of timeseries predictability in consecutive periods. 

To predict returns in year _K_ , we first split the past data up to the end of year _K_ − 1 into five consecutive intervals as five folds. Then, we train each model using four of the five folds and validate using the remaining fold, resulting in five sets of validation errors. Finally, we determine the best tuning parameters according to the average of these five sets’ validation errors and refit the model using all five data folds. 

Concerning the predictors’ heterogeneity, we standardize each predictor before cross-validation. Each year _K_ , we calculate the sample mean ̂ _μK_ and standard deviation ̂ _σ K_ using each predictor’s data in the past 20 years. We then standardize the predictors in the sample of the past 20 years and current year K with ̂ _μK_ and ̂ _σ K_ . The test sample predictors are standardized by the same sample mean and standard deviation to allay forward-looking concerns. 

**Fig. A.1.** Deterministic five-fold cross-validation. 

This figure demonstrates the deterministic five-fold cross-validation scheme. At the end of each year, we re-estimate the models using data for the past 20 years. Specifically, the deterministic design divides the sample into five consecutive parts. The rest of the cross-validation procedures follow the standard approach in Gu et al. (2020). 

15 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

## **Appendix B. Additional tables and figures** 

**Fig. B.1.** Relative variable importance by model. This figure reports the relative variable importance for the 10 most influential variables in each predictive model. We use the prefix “X” for aggregate predictors and “Z” for bond characteristic predictors to distinguish between the two groups of predictors. Variable importance is averaged over all testing samples and corporate bonds, and within each model, it is normalized to sum to 1. Refer to Table B.1 for details on the predictors. 

16 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Fig. B.2.** Performance of long-short trading strategy: value-weighted portfolios. This figure shows the cumulative returns of the value-weighted long-short trading strategy and sorted portfolios. We sort bonds based on return predictions each month and then calculate the value-weighted return, rebalancing monthly. The shaded areas indicate recession periods as determined by the NBER. 

17 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Fig. B.3.** Performance of direction-implied trading strategy: value-weighted portfolios. This figure shows the cumulative returns of the value-weighted direction-implied trading strategy. The short legs earn negative average returns; however, for clarity, we plot them as a positive trend, effectively shorting the short legs. The shaded areas indicate recession periods as determined by the NBER. 

18 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Fig. B.4.** Performance of long-short trading strategy: equal-weighted portfolios. This figure reports the cumulative return of the equal-weighted long-short trading strategy. The value-weighted version is presented in Fig. B.2. 

19 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Fig. B.5.** Performance of direction-implied trading strategy: equal-weighted portfolios. This figure reports the cumulative return of the equal-weighted direction-implied trading strategy. The value-weighted version is presented in Fig. B.3. 

## **Table B.1** 

Predictor list. 

|**Table B.1**<br>Predictor list.|||
|---|---|---|
|Acronym|Description|Details|
|Panel A: Aggregate Predictors|||
|**_Bond market variable_**<br>TBL<br>3-month treasury bill rate<br>Download from Fed. St. Louis|||
|GDP|GDP growth rate|Annual pct. growth rate in GDP|
|INDP|Industry production growth rate|Annual pct. growth rate in industrial production|
|CNSN|Consumption growth rate|Annual pct. growth rate in per capita real personal consumption|
|CBMKT|Corporate bond market return|Value-weighted corporate bond market return|
|TERM|TERM factor|Long-term gvt. bond return minus the one-month T-bill rate|
|DEF|Default factor|Long-term corp. bond return minus long-term gvt. bond return|
|INFL<br>CP5|CPI index<br>Forward factor|Annual pct. growth rate in CPI index<br>Cochrane and Piazzesi (2005) forward factor 5-year specification|
|TMS|Term spread|Long-term yield on government bonds|
|DFY|Default yield spread|Yield of BAA minus yield of AAA corporate bonds|
|RTBL|Relative T-bill rates|Hodrick (1992)|
|LOW|Low-risk factor|Houweling and Van Zundert (2017)|
|DMI|Debt-maturity factor|Baker et al., (2003)|
|**_Equity market variable_**|||



( _continued on next page_ ) 

20 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Table B.1** ( _continued_ ) 

|Acronym|Description||Details|
|---|---|---|---|
|Panel A: Aggregate Predictors||||
|DP|Dividend-to-price||S&P500 index dividend-to-price|
|EP|Earnings-to-price||S&P500 index earnings-to-price|
|NI|Net equity issuance||S&P500 index net equity issuance|
|BM|Book-to-market||S&P500 index book-to-market|
|DP|Dividend-payout ratio||S&P500 index dividend-payout ratio|
|LEV|Leverage||S&P500 index leverage|
|SVAR|Stock variance||S&P500 index variance|
|MKTRF|Market factor||Fama and French (1993)|
|SMB|Size factor||Fama and French (1993)|
|HML|Value factor||Fama and French (1993)|
|LIQ|Pastor-Stambaugh liquidity||Pastor and Stambaugh (2003)|
|Panel B: Corporate Bond Characteristics||||
|**_Fundamental_**<br>CRT<br>Credit rating<br>From FISD||||
|DUR|Duration|From FISD||
|TMT|Time-to-maturity|From FISD||
|AGE|Time-from-issuance|From FISD||
|SIZE|Amount outstanding|From FISD||
|Y2M|Yield-to-maturity|From FISD||
|RFY|Reach-for-yield|From FISD,Chen and Choi (2023)||
|CSD|Credit spread|From FISD,Nozawa (2017)||
|**_Return-distribution_**<br>MOM1M<br>Short-term reversal<br>Lag 1-month return||||
|MOM6M|6-month momentum|Lag 2-month to lag 6-month cumulative return||
|MOM12M|12-month momentum|Lag 2-month to lag 12-month cumulative return||
|LTR2Y|2-year long-term reversal|Lag 13-month to lag 24-month cumulative return||
|LTR3Y|3-year long-term reversal|Lag 13-month to lag 36-month cumulative return||
|VAR|Variance|Variance of returns of the past 36 months||
|DSD|Downside risk|5% VaR of returns of the past 36 months||
|SKEW|Skewness|Skewness of returns of the past 36 months||
|KURT|Kurtosis|Kurtosis of returns of the past 36 months||
|**_Covariance on risk factors_**<br>BETA_MKT<br>Multiple regression beta of an eight-factor model, including MKTRF, SMB, HML, SMB, DEF, TERM, ICR, UNC, and VIX. Fama and||||
|BETA_SMB|French (1993),He et al. (2017),Bali et al. (2021), andChung et al. (2019)|||
|BETA_HML||||
|BETA_DEF||||
|BETA_TERM||||
|BETA_ICR||||
|BETA_VIX||||
|BETA_UNC||||
|RVAR|Residual variance in the multiple regression of the eight-factor model.|||



**Table B.2** 

Relative variable importance of aggregate predictors. 

||MeanC|MedianC|Lasso|Ridge|ENet|PCA|PLS|BTree|RF|NN1|NN2|
|---|---|---|---|---|---|---|---|---|---|---|---|
|CBMKT|13.99|7.87|35.52|10.99|15.35|7.67|10.07|10.71|9.89|10.91|7.11|
|TERM|7.97|4.67|8.04|7.39|6.58|5.17|6.92|6.12|7.51|10.00|13.92|
|GDP|8.29|5.04|2.64|4.67|2.95|5.33|4.53|6.72|10.65|4.54|3.10|
|HML|6.65|2.12|3.52|5.81|6.25|9.30|4.92|3.61|3.81|5.27|4.76|
|DEF|2.29|3.32|2.35|5.17|5.14|3.61|4.78|4.22|2.79|7.68|10.76|
|SVAR|4.42|6.51|3.05|3.37|3.34|5.05|2.72|2.38|10.03|4.45|2.92|
|CNSN|7.31|7.18|2.56|3.20|1.26|3.34|3.66|5.47|2.93|4.48|6.47|
|TBL|3.61|5.77|2.53|3.82|3.10|4.79|3.26|3.64|9.14|3.17|2.75|
|INDP|3.59|5.67|2.52|4.15|4.47|3.01|5.13|3.60|2.46|3.80|4.91|
|LOW|4.23|6.16|4.77|3.66|3.56|4.82|3.99|4.12|2.55|2.46|1.73|
|MKT|4.43|5.10|2.38|3.87|3.31|4.86|4.34|3.15|4.19|3.32|2.54|
|DY|1.95|4.91|2.54|4.80|3.65|2.66|6.95|3.12|2.18|4.83|3.87|
|DP|5.29|5.01|2.52|4.53|4.33|4.99|4.74|0.00|0.00|4.52|4.70|
|TMS|3.52|5.31|2.55|3.49|3.47|3.85|3.23|4.23|4.05|2.01|1.46|
|DFY|5.42|7.02|2.63|2.43|2.29|4.72|2.44|2.93|1.36|2.70|1.62|
|CP5|1.65|1.53|2.11|3.52|3.71|2.80|3.19|4.11|3.13|4.31|4.37|
|EP|0.00|2.40|2.52|3.62|3.20|1.74|5.12|4.72|3.52|2.89|3.47|
|RTBL|3.32|3.55|0.00|3.27|3.50|2.68|2.45|3.29|3.04|3.50|3.57|
|LEV|0.74|0.13|2.52|4.25|5.00|0.00|4.27|3.84|0.19|5.27|5.60|
|DMI|1.97|2.25|2.69|3.25|3.48|3.72|3.11|3.53|3.06|1.88|2.14|
|INFL|3.55|5.43|3.23|2.46|2.70|3.33|2.41|4.30|2.57|1.03|0.00|
|BM|1.65|1.34|2.52|2.91|3.33|2.10|3.40|3.81|1.95|2.53|2.42|
|LIQ|1.67|0.36|2.46|3.20|3.26|3.00|3.59|2.03|2.41|2.42|1.43|
|SMB|1.12|1.34|1.30|2.17|2.77|2.60|0.00|2.97|3.41|2.03|2.56|
|NI|1.37|0.00|0.49|0.00|0.00|4.84|0.78|3.39|3.18|0.00|1.82|



21 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

The table presents the relative variable importance of aggregate predictors for each predictive model. The sum of variable importance is normalized to 1, and all values are expressed as percentages. 

## **Table B.3** 

Relative variable importance of bond characteristics. 

||MeanC|MedianC|Lasso|Ridge|ENet|PCA|PLS|BTree|RF|NN1|NN2|
|---|---|---|---|---|---|---|---|---|---|---|---|
|MOM1M|4.79|5.89|56.47|14.43|32.86|2.09|13.02|19.46|35.53|20.13|18.65|
|DSD|12.77|8.84|14.57|15.42|13.51|7.73|11.24|6.06|3.30|15.57|18.66|
|Y2M|0.00|1.70|2.87|0.00|4.99|0.62|0.00|10.80|15.27|14.27|15.94|
|RFY|5.05|3.41|5.99|4.35|5.43|3.60|1.63|5.04|8.53|11.97|8.81|
|SKEW|4.87|5.54|14.14|6.75|7.90|1.16|4.89|3.92|3.92|5.29|3.89|
|CSD|2.79|2.63|1.66|5.50|11.71|5.49|3.88|11.73|7.32|4.11|2.67|
|MOM12M|3.55|5.99|0.11|2.72|0.59|3.81|4.20|7.61|2.77|4.26|5.44|
|VAR|4.07|5.82|0.24|3.06|1.16|4.73|3.45|4.42|4.01|1.43|1.92|
|SIZE|3.51|1.78|0.61|4.29|2.93|4.32|4.75|1.63|1.73|3.14|3.42|
|BETA_ICR|4.38|7.18|0.26|3.51|1.65|4.95|3.83|1.56|1.05|1.59|1.63|
|KURT|4.59|7.16|0.15|3.34|1.01|5.09|3.49|1.41|0.79|1.73|1.56|
|TMT|3.33|2.18|0.22|2.92|1.38|5.12|3.33|3.28|2.82|2.13|2.80|
|RVAR|3.80|4.09|0.14|2.96|0.80|4.53|3.44|1.40|2.47|1.19|1.90|
|COUPON|3.10|0.00|0.24|3.55|1.69|3.74|3.85|3.01|0.52|2.55|4.01|
|AGE|4.05|6.04|0.22|3.17|1.25|5.11|3.97|0.00|0.00|1.11|0.61|
|MOM6M|4.20|7.36|0.22|1.23|0.31|4.48|2.85|2.22|1.60|0.03|0.44|
|BETA_MKTRF|3.24|3.66|0.00|2.55|3.29|3.60|3.12|1.36|0.43|1.85|0.31|
|MOM24M|2.99|3.97|0.15|3.15|0.00|0.00|2.86|1.63|0.73|2.91|3.10|
|BETA_SMB|3.28|2.31|0.22|2.72|1.36|3.83|3.50|1.70|0.86|1.31|0.38|
|RATE|3.26|1.72|0.22|1.53|0.51|4.73|2.58|4.49|0.86|0.22|1.21|
|BETA_DEF|3.26|2.83|0.21|2.66|0.91|3.91|3.28|1.35|0.68|0.91|0.41|
|BETA_UNC|3.45|1.28|0.22|2.18|0.28|4.42|3.13|2.14|1.30|1.07|0.55|
|BETA_TERM|3.10|2.86|0.22|2.10|1.32|3.28|2.69|1.09|1.01|0.45|0.88|
|BETA_HML|3.33|1.60|0.22|2.40|0.54|4.33|2.99|1.22|0.57|0.40|0.00|
|BETA_VIX|2.56|2.05|0.22|1.63|1.70|3.79|1.85|1.46|1.06|0.00|0.12|
|MOM36M|2.69|2.10|0.22|1.89|0.93|1.56|2.16|0.02|0.87|0.40|0.69|



The table presents the relative variable importance of bond characteristic predictors for each predictive model. The sum of variable importance is normalized to 1, and all values are expressed as percentages. 

## **Table B.4** 

Distribution of size and liquidity groups in private and public bonds. 

||1|2|3|4|5|Sum|
|---|---|---|---|---|---|---|
||Panel A: Size Groups||||||
|Private|0.20|0.22|0.31|0.19|0.08|1.00|
|Public|0.06|0.24|0.45|0.20|0.05|1.00|
||Panel B: Liquidity Groups||||||
|Private|0.14|0.14|0.44|0.14|0.14|1.00|
|Public|0.16|0.16|0.37|0.16|0.15|1.00|



The table reports the percentages of bond observations in size and liquidity quintiles for private and public bond subsamples. The sorting on size and liquidity is conducted for the entire cross-section and is independent of private-public identity. Each row sums to 1. For example, the first number, 0.20, indicates that 20% of public bonds are in the lowest quintile sorted by size. 

## **Table B.5** 

Predictive evidence of returns for subsamples. 

||||
|---|---|---|
|Panel A.1: 19|_R_<br>~~2~~<br>_OOS_<br>AAA<br>AA<br>A<br>BBB<br>NIG<br>96–2007|_R_2<br>_OOS_<br>AAA<br>AA<br>A<br>BBB<br>NIG|
|MeanC<br>Lasso<br>PLS<br>RF<br>NN2|-0.04<br>-0.32<br>-0.06<br>0.34*<br>0.69**<br>3.79***<br>2.24***<br>2.20***<br>2.07***<br>1.66***<br>2.13**<br>-4.48**<br>-2.94*<br>-3.06**<br>-0.40<br>6.28***<br>5.06***<br>5.28***<br>5.08***<br>2.37***<br>4.92***<br>3.73***<br>4.19***<br>3.93***<br>2.83***|-0.15<br>-0.46<br>-0.03<br>0.42<br>-0.07<br>4.56<br>3.06<br>2.52<br>1.63<br>2.01<br>3.55<br>-3.15<br>-2.41<br>-1.93<br>1.04<br>6.81<br>5.00<br>5.57<br>4.51<br>1.88<br>6.00<br>3.48<br>4.12<br>3.86<br>2.95|
|Panel A.2: 20|08–2009||
|MeanC<br>Lasso<br>PLS<br>RF<br>NN2|0.35**<br>0.41<br>0.66<br>0.53<br>0.32**<br>-1.82<br>2.58<br>3.41**<br>3.95***<br>1.43**<br>-10.29***<br>1.27<br>6.51*<br>7.28***<br>4.16**<br>0.70<br>5.44***<br>8.42***<br>8.75***<br>5.98***<br>-8.72**<br>1.99<br>8.41***<br>8.49***<br>6.77***|0.85<br>0.57<br>0.74<br>0.70<br>0.35<br>-0.92<br>2.08<br>3.37<br>4.81<br>1.58<br>-13.51<br>-0.73<br>6.38<br>8.92<br>4.86<br>-1.83<br>2.21<br>4.78<br>7.52<br>3.76<br>-15.21<br>-0.07<br>8.93<br>10.06<br>6.86|
|Panel A.3: 20|10–2020||
|MeanC<br>Lasso<br>PLS|0.21<br>0.87***<br>1.18***<br>0.78***<br>-0.95***<br>0.26<br>0.53<br>2.84**<br>3.41***<br>2.05<br>-5.14**<br>-7.93***<br>-1.75<br>-0.22<br>-0.41|0.33<br>0.97<br>1.41<br>0.94<br>0.05<br>5.06<br>3.93<br>4.89<br>5.34<br>3.78<br>3.35<br>-1.61<br>2.75<br>4.38<br>4.05<br>(_continued on next page_)|



22 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

**Table B.5** ( _continued_ ) 

|Panel|A.3: 20|10–2020|||
|---|---|---|---|---|
|RF<br>NN2||2.28<br>3.26**<br>5.08***<br>4.85***<br>1.50<br>1.90<br>3.13*<br>5.22***<br>4.47***<br>-0.62|5<br>5|.03<br>6.41<br>6.86<br>6.34<br>6.22<br>.90<br>6.50<br>8.03<br>8.18<br>11.30|
|Panel||_R_<br>~~2~~<br>_OOS_<br>TMT1<br>TMT2<br>TMT3<br>TMT4<br>TMT5<br>96–2007|_R_2<br>_OOS_|1<br>TMT2<br>TMT3<br>TMT4<br>TMT5|
||||TMT||
||B.1: 19||||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.49*<br>0.29<br>0.20<br>0.16<br>0.12<br>3.06***<br>2.46***<br>2.53***<br>2.05***<br>1.52***<br>-3.82**<br>-2.88**<br>-1.18<br>-1.07<br>-0.67<br>5.29***<br>5.01***<br>5.19***<br>3.95***<br>3.58***<br>4.44***<br>3.68***<br>4.51***<br>3.35***<br>3.07***|0.05<br>3.98<br>-0.09<br>4.52<br>4.75|-0.01<br>0.00<br>0.04<br>0.02<br>3.21<br>2.86<br>1.82<br>1.32<br>-0.26<br>-0.16<br>-1.09<br>-0.62<br>5.00<br>4.92<br>3.35<br>3.21<br>4.54<br>4.33<br>2.74<br>3.27|
|Panel|B.2: 20|08–2009|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.75**<br>0.65<br>0.47<br>0.30<br>0.26<br>3.56***<br>3.00**<br>2.72**<br>2.08*<br>1.51<br>3.90**<br>2.81**<br>5.42***<br>3.87*<br>3.58**<br>8.43***<br>7.43***<br>7.37***<br>5.77***<br>5.14***<br>7.25***<br>7.58***<br>7.03***<br>4.18*<br>3.88|0<br>2<br>4<br>6<br>9|.64<br>0.71<br>0.71<br>0.47<br>0.44<br>.48<br>2.88<br>3.40<br>2.39<br>2.26<br>.21<br>4.26<br>6.61<br>4.24<br>5.32<br>.20<br>6.43<br>6.16<br>3.11<br>3.42<br>.47<br>8.56<br>8.83<br>4.20<br>6.14|
|Panel|B.3: 20|10–2020|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.68***<br>0.66***<br>0.43*<br>0.39**<br>0.43***<br>-6.66***<br>0.53<br>2.50*<br>3.77***<br>4.40***<br>-24.61***<br>-5.48*<br>0.20<br>2.15<br>1.61<br>5.86***<br>5.33***<br>4.56***<br>4.54***<br>3.33**<br>-2.88<br>2.39<br>5.46***<br>5.70***<br>4.07***|0.<br>-1.<br>-1<br>7.<br>1.|87<br>0.82<br>0.71<br>0.74<br>0.67<br>70<br>2.91<br>4.27<br>5.80<br>5.88<br>3.74<br>-0.21<br>3.74<br>6.29<br>5.60<br>08<br>7.42<br>5.85<br>6.77<br>5.55<br>75<br>8.01<br>9.03<br>10.32<br>8.60|
|Panel|C.1: All|_R_<br>~~2~~<br>_OOS_<br>_R_<br>~~2~~<br>_OOS_;<br>Private<br>Public<br>Diffe<br>1996–2007|Δ<br>rence|_R_2<br>_OOS_<br>Private<br>Public|
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.21<br>0.19<br>0.02<br>2.19***<br>2.31***<br>-0.12<br>0.80**<br>0.57<br>0.23<br>4.74***<br>4.01***<br>0.74<br>3.43***<br>4.04***<br>-0.61||-0.02<br>0.10<br>2.32<br>2.34<br>1.04<br>0.64<br>4.28<br>3.45<br>3.61<br>3.95|
|Panel|C.2: All|2008–2009|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.32<br>0.43<br>2.29**<br>2.10<br>0.31<br>0.76<br>5.76***<br>7.21***<br>5.63***<br>5.98***|-0.11<br>0.19<br>-0.45<br>-1.45<br>-0.35|0.47<br>0.62<br>2.63<br>2.48<br>1.16<br>1.84<br>3.98<br>4.93<br>6.67<br>6.79|
|Panel|C.3: All|2010–2020|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.43***<br>0.48***<br>2.93***<br>2.60**<br>1.42**<br>1.77**<br>4.39***<br>3.93***<br>4.29***<br>4.72***|-0.05<br>0.34<br>-0.35<br>0.46<br>-0.43|0.65<br>0.83<br>4.65<br>4.72<br>2.11<br>2.96<br>6.09<br>6.48<br>7.98<br>9.43|
|Panel|C.4: IG|1996–2020|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.43***<br>0.49***<br>3.02***<br>2.91***<br>1.21***<br>1.32***<br>5.26***<br>5.38***<br>4.47***<br>4.87***|-0.05<br>0.12<br>-0.11<br>-0.12<br>-0.40|0.31<br>0.62<br>3.27<br>3.20<br>1.39<br>1.89<br>5.37<br>5.44<br>5.43<br>5.60|
|Panel|C.5: NI|G 1996–2020|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|-0.05<br>-0.29<br>1.97***<br>2.12***<br>0.89**<br>0.78**<br>2.84***<br>2.45***<br>2.09***<br>3.68***|0.24<br>-0.15<br>0.12<br>0.39<br>-1.59|0.04<br>0.17<br>1.81<br>2.29<br>0.95<br>0.97<br>2.77<br>3.40<br>4.57<br>6.24|
|Panel|C.6: TM|T1 1996–2020|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.28**<br>0.31***<br>2.72***<br>2.81***<br>1.01***<br>1.11***<br>4.52***<br>4.27***<br>4.15***<br>4.50***|-0.03<br>-0.09<br>-0.10<br>0.25<br>-0.36|0.21<br>0.41<br>2.67<br>2.85<br>1.24<br>1.57<br>4.29<br>4.50<br>4.99<br>5.93|
|Panel|C.7: TM|T5 1996–2020|||
|Mean<br>Lasso<br>PLS<br>RF<br>NN2|C|0.27**<br>0.26**<br>2.58***<br>2.86***<br>0.98***<br>1.09**<br>3.50***<br>3.53***<br>3.54***<br>3.58***|0.01<br>-0.28<br>-0.11<br>-0.03<br>-0.04|0.21<br>0.35<br>2.04<br>2.84<br>1.04<br>1.68<br>3.43<br>3.98<br>5.04<br>5.21|



23 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

Following Table 3, this table reports the return predictive evidence of corporate bond sub-samples on rating, maturity, and private-public type, across different sample periods: 1996–2007, 2008–2009, and 2010–2020. In Panels A.1–A.4, we sort bonds into five rating groups: AAA, AA, A, BBB, and NIG. In Panels B.1–B.3, we sort bonds into quintile groups by their maturities. Each group contains the same number – of bonds each month. TMT1 is the short-maturity group, and TMT5 is the long-maturity group. In Panels C.1 C.7, we classify the bonds by the private-public type of issuance firm. We report for five predictive models, introduced in Section 2.1 and Appendix A. The left panel presents _R_ ~~2~~ _OOS_[(%) (see][ Eq. (4)][), and the significance of Fama-MacBeth] _[ t]_[-statistics. The right panel presents] _[ R]_[2] _OOS_[(%) (see][ Eq. (2)][). For the] private and public company bond predictability difference, we report the _R_ ~~2~~ _OOS_ ;Δ[(%) defined in][ Eq. (5)][ with the two-sample Fama-MacBeth] _t_ -statistics. The _t_ -statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% thresholds, respectively. 

## **Table B.6** 

List of 12 economic condition variables. 

|Acronym|Description|
|---|---|
|ADS|Business conditions indexAruoba et al. (2009)|
|BEX|Risk aversion index Bekaert et al. (2022)|
|CFN<br>CSF|Chicago Fed National Activity Index<br>Cross-sectional factor explanatory power of a fve-factor IPCA model Kelly et al. (2019)|
|DFY|Default yield spread|
|IDP|Industrial production growth rate|
|LIQ|Market liquidity Pastor and Stambaugh (2003)|
|SNT|Investor sentimentHuang et al. (2015)|
|SRP|Smooth recession probability|
|SVAR|Realized market volatility|
|TBL|Treasury Bill rate|
|VIX|VIX|



## **Appendix C. Excluding bonds without the month-end price** 

A potential concern is that our results may be subject to look-ahead bias in monthly returns and aggregate predictors, particularly when a bond is not traded on the last trading date of a month and an aggregate predictor is updated with information by that date. Among the four databases introduced in Section 3.1.1 on corporate bond returns, LBFI and Datastream provide dealer quotes, while NAIC and TRACE offer transaction data, from which we extract end-of-month prices. To mitigate potential bias, we exclude observations in NAIC and TRACE that do not trade on the last trading date of a month, removing 110,175 observations. We then replicate the main empirical analysis, presenting the return predictive evidence in Table C.1 and investment performance in Table C.2. Despite the removal of some observations, prediction accuracy remains substantial, and investment outcomes continue to show significant impacts, albeit with slight declines in some empirical metrics. 

Table C.1 reports the return predictability evidence after excluding bonds without month-end prices, referred to as the treated sample. In Panel A, we present _R_ ~~2~~ _OOS_[and] _[ R]_[2] _OOS_[for five][rating groups, allowing][comparison with the main results from][the original][sample in][ Table 3][.][Similarly, Panel][B] covers five maturity groups, corresponding to the main results in Table 3. Prediction accuracy metrics remain positive and substantial across all rating ~~2~~ and maturity groups, even after excluding these bonds. While _ROOS_[and] _[ R]_[2] _OOS_[are slightly lower in][ Table C.1][ than in the main results, the table shows] Table 3. This improved predictions in specific cases, such as Lasso, Ridge, and Elastic Net predictions for AAA rating groups, which outperform those in finding indicates the continued robustness of the predictive evidence despite exclusions. 

To ensure robustness of the results in Table 5, Table C.2 reports investment performance based on return predictions, excluding bonds without month-end prices. We do not find sufficient evidence to conclude that the treated sample yields lower investment gains. While the original sample exhibits higher average returns and alphas than the treated sample in some cases, such as long-short trading strategies on Lasso predictions, these are offset by instances where the treated sample demonstrates better performance, particularly in long-only strategies on RF predictions. Thus, investment strategies are minimally affected by the exclusion of samples. 

A comprehensive comparison between the main results and empirical investigations on samples excluding bonds without month-end prices reveals minimal impacts on predictive evidence and investment outcomes. Thus, the predictive evidence and investment opportunities presented in the main results are not affected by potential look-ahead bias. 

## **Appendix D. Discussion on stale prices** 

This section presents summary statistics of our sample to address concerns that our main results might be influenced by stale prices. Following Chen et al. (2007) and Dittmar and Yuan (2008), we calculate the percentage of zero returns and returns less than five basis points in absolute value. We find 0.017% zero returns in public bonds and 0.024% in private bonds, aligning with the range reported by Dittmar and Yuan (2008) (0.005% to 0.265%). For the percentage of returns below five basis points in absolute value, we observe 2.4539% in public bonds and 2.4528% in private bonds. Therefore, our main results regarding the differences between private and public bonds are unlikely to be driven by zero returns or returns below five basis points. 

24 

_Journal of Banking and Finance 171 (2025) 107372_ 

_G. Feng et al._ 

## **Table C.1** 

Return predictive evidence: excluding bonds without month-end prices. 

||||
|---|---|---|
||_R_<br>~~2~~<br>_OOS_<br>Panel A: Rating Groups|_R_2<br>_OOS_<br>AAA<br>AA<br>A<br>BBB<br>NIG|
||AAA<br>AA<br>A<br>BBB<br>NIG||
|MeanC<br>MedianC<br>Lasso<br>Ridge<br>ENet<br>PCA<br>PLS<br>BTree<br>RF<br>NN1<br>NN2|0.04<br>-0.33<br>0.07<br>0.00<br>-0.54<br>-0.27<br>-0.92***<br>-0.39<br>-0.50*<br>-0.92**<br>2.47***<br>0.36<br>1.82***<br>2.06***<br>1.42***<br>1.94**<br>-0.45<br>1.35*<br>1.96**<br>1.19*<br>2.15**<br>-0.70<br>1.16<br>1.66**<br>0.83<br>-0.21<br>-0.22<br>0.81<br>1.61***<br>0.73**<br>-1.19<br>-8.03***<br>-3.04**<br>-2.43*<br>-1.39<br>7.52***<br>-2.21<br>3.43***<br>3.36**<br>-1.21<br>4.97***<br>3.20***<br>4.37***<br>4.35***<br>2.72***<br>1.93*<br>0.25<br>2.46***<br>2.75***<br>2.03***<br>2.32**<br>1.09<br>3.49***<br>3.13***<br>2.02**|0.06<br>-0.03<br>0.32<br>0.53<br>0.10<br>-0.48<br>-0.55<br>-0.13<br>0.16<br>-0.13<br>3.98<br>2.57<br>2.82<br>2.33<br>1.98<br>4.24<br>2.14<br>3.50<br>3.40<br>2.07<br>4.46<br>1.57<br>2.76<br>2.39<br>1.17<br>0.40<br>0.64<br>1.45<br>1.97<br>0.91<br>2.23<br>-1.65<br>0.85<br>0.96<br>1.97<br>9.58<br>2.52<br>7.56<br>8.07<br>5.83<br>4.99<br>3.89<br>4.97<br>5.10<br>3.06<br>4.43<br>2.91<br>4.59<br>4.22<br>2.93<br>2.07<br>1.72<br>4.67<br>5.02<br>4.37|
||Panel B: Maturity Groups|MT1<br>TMT2<br>TMT3<br>TMT4<br>TMT5|
||TMT1<br>TMT2<br>TMT3<br>TMT4<br>TMT5<br>T||
|MeanC<br>MedianC<br>Lasso<br>Ridge<br>ENet<br>PCA<br>PLS<br>BTree<br>RF<br>NN1<br>NN2|0.31<br>-0.01<br>-0.11<br>-0.25<br>-0.21<br>0<br>-0.30<br>-0.61**<br>-0.61**<br>-0.65***<br>-0.48**<br>-0<br>-0.50<br>2.23***<br>2.51***<br>2.43***<br>2.08***<br>2<br>-0.20<br>2.07**<br>2.60***<br>2.19***<br>1.59***<br>2<br>-0.49<br>1.78**<br>2.19***<br>2.11***<br>1.58***<br>2<br>0.91<br>0.99*<br>0.90*<br>0.75*<br>0.69*<br>1<br>-10.75***<br>-3.35**<br>-0.57<br>-0.08<br>-0.22<br>-0<br>0.23<br>2.48*<br>2.93**<br>4.16***<br>3.02**<br>7<br>5.03***<br>4.81***<br>4.68***<br>4.07***<br>3.35***<br>4<br>0.27<br>2.81***<br>3.60***<br>2.99***<br>2.39***<br>3<br>1.97*<br>3.54***<br>4.01***<br>3.51***<br>2.05***<br>4|.36<br>0.32<br>0.25<br>0.23<br>0.17<br>.10<br>-0.16<br>-0.23<br>-0.11<br>-0.10<br>.74<br>3.00<br>3.10<br>2.40<br>2.01<br>.93<br>3.32<br>3.75<br>2.80<br>2.53<br>.11<br>2.55<br>2.83<br>2.19<br>1.86<br>.06<br>1.41<br>1.56<br>1.03<br>1.12<br>.41<br>0.65<br>2.23<br>1.27<br>1.54<br>.93<br>8.83<br>7.60<br>5.63<br>6.29<br>.61<br>5.32<br>5.08<br>3.82<br>3.54<br>.77<br>4.30<br>4.72<br>3.44<br>3.33<br>.09<br>4.52<br>4.93<br>3.79<br>3.82|



**Table C.2** 

Investment performance: excluding bonds without month-end prices. 

||All|IG<br>Mean<br>_α_<br>SR<br>ns|NIG<br>Mean<br>_α_<br>SR|Private|SR|Public|SR|
|---|---|---|---|---|---|---|---|
|||||Mean<br>_α_||Mean<br>_α_||
|MeanC<br>Lasso<br>PLS<br>RF<br>NN2|0.51***<br>0.46***<br>0.95<br>0.72***<br>0.68***<br>1.70<br>1.02***<br>1.08***<br>2.15<br>1.92***<br>2.11***<br>3.01<br>1.47***<br>1.55***<br>2.95|0.41***<br>0.38***<br>0.85<br>0.69***<br>0.66***<br>1.67<br>0.99***<br>1.05***<br>2.15<br>1.87***<br>2.09***<br>3.05<br>1.37***<br>1.44***<br>3.00|0.77***<br>0.84***<br>0.63<br>1.11***<br>1.22***<br>0.99<br>1.64***<br>1.88***<br>1.13<br>2.19***<br>2.26***<br>1.83<br>2.38***<br>2.59***<br>1.71|0.53***<br>0.49<br>0.75***<br>0.72<br>1.12***<br>1.22<br>2.06***<br>2.31<br>1.50***<br>1.60|***<br>0.97<br>***<br>1.73<br>***<br>2.02<br>***<br>3.16<br>***<br>2.99|0.46***<br>0.37<br>0.54***<br>0.47<br>0.84***<br>0.81<br>1.36***<br>1.41<br>1.27***<br>1.28|***<br>0.68<br>***<br>0.99<br>***<br>1.56<br>***<br>2.05<br>***<br>2.06|
||Panel B: Direction-Implied Portfoli|o Returns||||||
|MeanC<br>Lasso<br>PLS<br>RF<br>NN2|0.42<br>0.35<br>0.22<br>0.77***<br>0.75***<br>0.74<br>1.27***<br>1.36***<br>0.76<br>1.82***<br>1.87***<br>1.45<br>1.51***<br>1.62***<br>1.18|0.32<br>0.25<br>0.27<br>0.81***<br>0.81***<br>0.81<br>1.28***<br>1.24***<br>0.90<br>1.67***<br>1.85***<br>1.84<br>1.49***<br>1.46***<br>1.37|0.65*<br>0.49<br>0.36<br>0.86***<br>0.81***<br>0.70<br>1.54***<br>1.62***<br>0.73<br>2.34***<br>2.24***<br>1.31<br>2.85***<br>2.85***<br>1.21|0.37<br>0.33<br>0.75***<br>0.71<br>1.23***<br>1.29<br>1.64***<br>1.74<br>1.57***<br>1.67|0.24<br>***<br>0.72<br>***<br>0.76<br>***<br>1.48<br>***<br>1.18|0.44<br>0.36<br>0.44***<br>0.40*<br>0.91***<br>1.03*<br>1.36***<br>1.38*<br>1.22***<br>1.25*|0.29<br>*<br>0.51<br>**<br>0.48<br>**<br>1.07<br>**<br>0.74|



This table evaluates investment gains based on return predictions, excluding bonds without month-end prices. Panel A reports the long-short trading strategy, while Panel B covers the direction-implied trading strategy. Performance measures include monthly average returns (%), alphas (%) from a factor model, and annualized Sharpe ratios. We test the portfolios and obtain alpha using the five-factor model (MKT, SMB, HML, TERM, and DEF) from Fama and French (1993), with a test period from January 1996 to September 2020. The results are based on five predictive models: MeanC, Lasso, PLS, RF, and NN2. The t-statistics incorporate Newey-West (1987) robust standard errors, with *, **, and *** denoting significance at the 10%, 5%, and 1% levels, respectively. 

## **Data availability** 

Data will be made available on request. 

## **References** 

- Amihud, Y., 2002. Illiquidity and stock returns: cross-section and time-series effects. J. Financ. Mark. 5, 31–56. 

- Aruoba, S.B., Diebold, F.X., Scotti, C., 2009. Real-time measurement of business conditions. J. Bus. Econ. Stat. 27, 417–427. 

- Avramov, D., Cheng, S., Metzker, L., 2023. Machine learning versus economic 

   - restrictions: evidence from stock return predictability. Manage. Sci. 69, 2587–2619. 

- Baker, M., Greenwood, R., Wurgler, J., 2003. The maturity of debt issues and predictable variation in bond returns. J. Financ. Econ. 70, 261–291. 

Bali, T.G., Subrahmanyam, A., Wen, Q., 2021. The macroeconomic uncertainty premium in the corporate bond market. J. Financ. Quant. Anal. 56, 1653–1678. 

Bali, T.G., Goyal, A., Huang, D., Jiang, F., Wen, Q., 2022. Predicting Corporate Bond Returns: Merton Meets Machine Learning. Georgetown University. Unpublished working paper. 

Bekaert, G., De Santis, R.A., 2021. Risk and return in international corporate bond markets. J. Int. Financ. Mark., Inst. Money 72, 101338. 

Bekaert, G., Engstrom, E.C., Xu, N.R., 2022. The time variation in risk appetite and uncertainty. Manage. Sci. 68, 3975–4004. 

Bekaert, G., De Santis, R.A., Mondino, T., 2024. The. Global Cross-Section of Corporate Bonds: Market, Maturity and Liquidity. Columbia University. Unpublished working paper. 

Bianchi, D., Büchner, M., Tamoni, A., 2021. Bond risk premiums with machine learning. Rev. Financ. Stud. 34, 1046–1089. 

Cao, J., Goyal, A., Xiao, X., Zhan, X., 2023. Implied volatility changes and corporate bond returns. Manage. Sci. 69, 1375–1397. 

25 

_G. Feng et al._ 

_Journal of Banking and Finance 171 (2025) 107372_ 

Chen, Q., Choi, J., 2023. Reaching for yield and the cross section of bond returns. Manage. Sci. forthcoming. 

Chen, L., Lesmond, D.A., Wei, J., 2007. Corporate yield spreads and bond liquidity. J. Finance 62, 119–149. 

Choi, J., Kim, Y., 2018. Anomalies and market (dis) integration. J. Monet. Econ. 100, 16–34. 

Chordia, T., Goyal, A., Nozawa, Y., Subrahmanyam, A., Tong, Q., 2017. Are capital market anomalies common to equity and corporate bond markets? An empirical investigation. J. Financ. Quant. Anal. 52, 1301–1342. 

Chung, K.H., Wang, J., Wu, C., 2019. Volatility and the cross-section of corporate bond returns. J. Financ. Econ. 133, 397–417. 

Cochrane, J.H., Piazzesi, M., 2005. Bond Risk Premia. Am. Econ. Rev. 95, 138–160. Dangl, T., Halling, M., 2012. Predictive regressions with time-varying coefficients. J. Financ. Econ. 106, 157–181. 

Diebold, F.X., Mariano, R.S., 1995. Comparing predictive accuracy. J. Bus. Econ. Stat. 13, 253–263. 

Dittmar, R.F., Yuan, K., 2008. Do sovereign bonds benefit corporate bonds in emerging markets? Rev. Financ. Stud. 21, 1983–2014. 

Edwards, A.K., Harris, L.E., Piwowar, M.S., 2007. Corporate bond market transaction costs and transparency. J. Finance 62, 1421–1451. 

Fama, E.F., French, K.R., 1989. Business conditions and expected returns on stocks and bonds. J. Financ. Econ. 25, 23–49. 

- Fama, E.F., French, K.R., 1993. Common risk factors in the returns on stocks and bonds. J. Financ. Econ. 33, 3–56. 

Fama, E.F., MacBeth, J.D., 1973. Risk, return, and equilibrium: empirical tests. J. Polit. Econ. 81, 607–636. 

Feng, G., Jiang, L., Li, J., Song, Y., 2023. Deep Tangency Portfolio. City University of Hong Kong. Unpublished working paper. 

Feng, G., He, X., Wang, J., Wu, C., 2024. Benchmarking Corporate Bond Returns with Panel Tree. City University of Hong Kong. Unpublished working paper. 

Gebhardt, W.R., Hvidkjaer, S., Swaminathan, B., 2005. The cross-section of expected 

corporate bond returns: betas or characteristics? J. Financ. Econ. 75, 85–114. 

Giesecke, K., Longstaff, F.A., Schaefer, S., Strebulaev, I., 2011. Corporate bond default risk: a 150-year perspective. J. Financ. Econ. 102, 233–250. 

Gu, S., Kelly, B., Xiu, D., 2020. Empirical asset pricing via machine learning. Rev. Financ. Stud. 33, 2223–2273. 

Gu, S., Kelly, B., Xiu, D., 2021. Autoencoder asset pricing models. J. Econom. 222, 429–450. 

- Guo, X., Lin, H., Wu, C., Zhou, G., 2022. Predictive information in corporate bond yields. J. Financ. Mark. 59, 100687. 

Hodrick, R., 1992. Dividend yields and expected stock returns: alternative procedures for inference and measurement. Rev. Financ. Stud. 5, 357–386. 

- Hong, Y., Lin, H., Wu, C., 2012. Are corporate bond market returns predictable? J. Bank. Financ. 36, 2216–2232. 

- Houweling, P., Van Zundert, J., 2017. Factor investing in the corporate bond market. Financ. Anal. J. 73, 100–115. 

- Huang, D., Jiang, F., Tu, J., Zhou, G., 2015. Investor sentiment aligned: a powerful predictor of stock returns. Rev. Financ. Stud. 28, 791–837. 

- Jostova, G., Nikolova, S., Philipov, A., Stahel, C.W., 2013. Momentum in corporate bond returns. Rev. Financ. Stud. 26, 1649–1693. 

- Keim, D.B., Stambaugh, R.F., 1986. Predicting returns in the stock and bond markets. J. Financ. Econ. 17, 357–390. 

- Kelly, B.T., Palhares, D., Pruitt, S., 2023. Modeling corporate bond returns. J. Finance 78, 1967–2008. 

- Kelly, B.T., Malamud, S., Zhou, K., 2024. The virtue of complexity in return prediction. J. Finance 79, 459–503. 

- Li, D., Lu, L., Qi, Z., Zhou, G., 2022. International Corporate Bond Market: Uncovering Risks Using Machine Learning. Washington University in St. Louis. Unpublished working paper. 

- Lin, H., Wang, J., Wu, C., 2011. Liquidity risk and expected corporate bond returns. J. Financ. Econ. 99, 628–650. 

- Lin, H., Wang, J., Wu, C., 2014. Predictions of corporate bond excess returns. J. Financ. Mark. 21, 123–152. 

- Lin, H., Wu, C., Zhou, G., 2018. Forecasting corporate bond returns with a large set of predictors: an iterated combination approach. Manage. Sci. 64, 4218–4238. 

- Newey, W.K., West, K.D., 1987. A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica 55, 703–708. 

- Nozawa, Y., 2017. What drives the cross-section of credit spreads?: a variance decomposition approach. J. Finance 72, 2045–2072. 

- Opdyke, J.D., 2007. Comparing Sharpe ratios: so where are the _p_ -values? J. Asset Manage. 8, 308–336. 

- Pastor, L., Stambaugh, R.F., 2003. Liquidity risk and expected stock returns. J. Polit. Econ. 111, 642–685. 

- Rapach, D.E., Strauss, J.K., Zhou, G., 2010. Out-of-sample equity premium prediction: combination forecasts and links to the real economy. Rev. Financ. Stud. 23, 821–862. 

- Ronen, T., Zhou, X., 2013. Trade and information in the corporate bond market. J. Financ. Mark. 16, 61–103. 

- Welch, I., Goyal, A., 2008. A comprehensive look at the empirical performance of equity premium prediction. Rev. Financ. Stud. 21, 1455–1508. 

He, Z., Kelly, B., Manela, A., 2017. Intermediary asset pricing: new evidence from many asset classes. J. Financ. Econ. 126, 1–35. 

26 

