Stud. Nonlinear Dyn. E. 2026; 30(1): 23–36 

Haibin Xie*, Boyao Wu, Yuying Sun and Shouyang Wang 

## **Realized Probability Index is a Better Market Timing Indicator** 

https://doi.org/10.1515/snde-2024-0060 Received June 13, 2024; accepted December 16, 2024; published online January 20, 2025 

**Abstract:** In practice, market timing is a well-known trading strategy among investors, and different indicators have been proposed for market timing methods. This paper compares three indicators used in market timing strategy: the return, the 0–1 binary index, and the realized probability index. It is shown that realized probability index is more informative and more efficient than the 0–1 binary index in terms of market timing, and tends to be more predictable than the return itself. This finding is interesting and important as it proves for the first time that the realized probability index is a more efficient market timing indicator and thus should be given more attention by both academic researchers and practitioners. An empirical study is performed on different stock indices, and the results confirm our finding. 

**Keywords:** market timing; realized probability; binary index; efficiency analysis 

## **JEL Classification:** G17; C22 

**PACS:** 05.45.Tp 

## **1 Introduction** 

Market timing is a popular trading strategy among practitioners and well-known by academic researchers. For example, the widely used technical trading rules are actually market timing indicators (e.g. Pring 1991). In Merton’s market timing model, it is assumed that the mutual fund managers focused more on the sign of return rather than the overall return (Merton 1981). Leitch and Tanner (1991, 1995) find that the best criterion for predictability is the direction of the change, which is closely related to the profits that investors are seeking in the market. 

Different market timing indicators have been proposed in academic literature. Among them, return indicator and directional indicator are the most widely-used ones. For the return indicator, an investor using market timing strategy would hold the risky asset if its expected return is above risk-free return, otherwise the investor would hold the risk-free asset. For the directional indicator, an investor would hold the risky asset if it is forecasted to be positive, otherwise the investor would like to hold the risk-free asset. 

Voluminous literature have been devoted to investigating the empirical performance of these two indicators. It is well documented that financial returns are notoriously difficult to forecast due to the high information efficiency in financial markets. For example, Welch and Goyal (2008), among others, comprehensively reexamine the performance of a list of variables that have been documented to be informative for predicting equity risk premium, and find that these variables fail to beat the simple history mean forecasts. Different from the return 

***Corresponding author: Haibin Xie** , China School of Banking and Finance, University of International Business and Economics, Beijing, China, E-mail: hbxie@amss.ac.cn 

> **Boyao Wu** , China School of Banking and Finance, University of International Business and Economics, Beijing, China **Yuying Sun and Shouyang Wang** , Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, China 

Open Access. © 2024 the author(s), published by De Gruyter. License. 

This work is licensed under the Creative Commons Attribution 4.0 International 

> **24 —** H. Xie et al.: Timing Market with Realized Probability 

indicator, it is believed that directional indicator is more predictable as it depends on all conditional moments rather than merely the conditional mean of the return. For example, Christoffersen and Diebold (2006) show that volatility dependence can lead to predictability of return directions via induced sign dependence; Hong and Chung (2006) and Chung and Hong (2007) find convincing evidence of directional predictability in both stock markets and foreign exchange markets using generalized spectrum testing approach. Different models and approaches have been used to predict the direction indicators. For example, Leung, Daouk, and Chen (2000) consider the static logit and probit models, whereas Rydberg and Shephard (2003), and Anatolyev and Gospodinov (2010) propose the so-called autologistic model to predict return directions. Nyberg (2011) extends the dynamic probit model suggested by Kauppi and Saikkonen (2008) to predict return directions. Nyberg and Ponka (2016) further generalize the dynamic probit model to a bivariate case incorporating the potential interaction effects in direction forecasting. 

Besides the commonly used return indicator and directional indicator, recently Xie et al. (2024) propose a new indicator, realized probability index for market timing. The realized probability index is constructed from HFT (high frequency trading) data and directly related to the directions of returns, which makes it a nice indicator for market timing. Moreover compared with the directional indicator, the realized probability index is found to be more efficient in statistical sense. 

All these three indicators can be used in market timing strategy, but the question is which indicator is more efficient and useful in practice. This paper is designed to answer this question. We believe a better market timing indicator should at least have the following three features: first, the indicator should be more informative. Investment decisions heavily depend on information, more informative indicators are beneficial to better decisions; second, the indicator should be economically more efficient in timing strategy. To practitioners, more efficient indicators mean that timing strategies based on these indicator are less volatile or less risky; last and the most important, the indicator should be more predictable. In practice, investors make their decisions based on their forecasts. More predictable indicators imply more accurate forecasts and thus better investment decisions. 

With a thorough investigation, we find the realized probability index is more informative and efficient than the directional indicator, and more predictable than the return indicator. The findings obtained in this paper indicate that realized probability index is a better market timing indicator. Empirical results are also consistent with our findings. 

This paper is organized as follows. Section 1 presents the introduction. Section 2 presents the market timing indicators and shows how these indicators can be used in market timing. Section 3 compares the above mentioned three timing indicators, and discusses which indicator is better from different aspects. Section 4 presents the empirical results, and we conclude in Section 5. 

## **2 Market Timing Indicator** 

In this section we first present the indicators and then discuss how these indicators can be used in market timing strategy. 

- **Return Indicator** : Let _pt_ +1 be the log equilibrium price at time _t_ + 1. The return over time interval [ _t_ , _t_ + 1] is thus 

**==> picture [244 x 11] intentionally omitted <==**

where _rt_ +1 is the log return. Market timing strategy based on return indicator is presented as follows: if the conditional mean of the risky asset is above the risk-free return, an investor would hold the risky asset, otherwise he/she holds the risk-free asset. The return realized by this timing strategy is given by 

**==> picture [279 x 30] intentionally omitted <==**

where _rf t_ +1 is the return on risk-free asset. 

H. Xie et al.: Timing Market with Realized Probability **— 25** 

– **Directional Indicator** : The directional indicator is constructed based on the signs of the asset returns 

**==> picture [259 x 30] intentionally omitted <==**

where _Bt_ +1 is the directional indicator. The return realized by this market timing indicator is presented as follows: 

**==> picture [290 x 31] intentionally omitted <==**

where _P_ ( _Bt_ +1 = 1|Ω _t_ ) is the conditional probability, and Ω _t_ is the information available at time _t_ . The intuition behind this timing strategy is simple: an investor would hold the risky asset if he/she expects a larger probability of being upward than that of being downward, otherwise he/she would hold the risk-free asset. It is clear that the directional indicator is also known as a 0–1 binary index. In the following we will use 0–1 binary index instead of directional indicator. 

– **Realized Probability** : suppose there are _n_ + 1 trading price betweeen time _t_ and time _t_ + 1 and the _i_ th trading price is _pt_[(] _[i]_[)][(] _[i]_[=][0,1,2, ...,] _[ n]_[), where] _[p]_[(0)] _t_[=] _[p][t]_[and] _[p]_[(] _t[n]_[)][=] _[p][t]_[+][1][.][Denote][][+][as][an][index][set][of][positive] _[j]_[)] _[j]_[)] _[j]_[−][1)] returns, [+] = { _j_ : _rt_[(] +1[=] _[p]_[(] _t_[−] _[p]_[(] _t >_ 0} and [−] as an index set of negative returns, [−] = { _k_ : _rt_[(] _[k]_ +[)] 1[=] _[p]_[(] _t[k]_[)] − _p_[(] _t[k]_[−][1)] _<_ 0}. The realized probability index is constructed as follows 

**==> picture [251 x 23] intentionally omitted <==**

> _[j]_[)] where _CPRt_ +1 =[∑] _j_ ∈[+] _[r] t_[(] +1[,] _[CNR][t]_[+][1][=][∑] _k_ ∈[−] _[r] t_[(] _[k]_ +[)] 1[,][and] _[CAR][t]_[+][1][=] _[CPR][t]_[+][1][−] _[CNR][t]_[+][1][.][It][is][clear][that] _[CPR][t]_[+][1] measures the cumulative positive return and _CNRt_ +1 measures the cumulative negative return. Moreover _CARt_ +1 measures the cumulative absolute return 

**==> picture [347 x 29] intentionally omitted <==**

Realized probability index, _RealPt_ +1 measures the proportion of the cumulative positive return over the cumulative absolute return. It is obvious that if the realized probability index is above 1/2, the magnitude of the cumulative positive return would be larger than that of the cumulative negative return, the realized return over [ _t_ , _t_ + 1] is thus positive, otherwise it is negative. The return realized by this market timing strategy is presented as follows: 

**==> picture [282 x 31] intentionally omitted <==**

The intuition behind this timing strategy is natural: an investor would hold the risky asset if he/she expects the magnitude of the cumulative positive return is larger than that of the cumulative negative return, otherwise he/she would hold the risk-free asset. 

## **3 Efficiency Analysis** 

All those three indicators can be used in market timing strategy, but the problem is which indicator is more informative, economically valuable and predictable. This section is designed to compare the efficiency of the above mentioned three market timing indicators from the aspects of information efficiency, economic efficiency, and predictability efficiency. 

> **26 —** H. Xie et al.: Timing Market with Realized Probability 

## **3.1 Information Efficiency** 

**Proposition 1.** _Both return and realized probability index are more informative than 0–1 binary index, however realized probability index and return have different information contents._ 

It is obvious that the 0–1 binary index only contains the direction information, it has no information about the magnitude of the return. 

The return and the 0–1 binary index are connected through the following equation 

**==> picture [264 x 10] intentionally omitted <==**

Now it is clear that we can obtain both the direction ( _St_ +1) information and the magnitude (| _rt_ +1|) information from the return series. Thus return is more informative than 0–1 binary index. 

The 0–1 binary index is related to the realized probability index through the following equation 

**==> picture [270 x 11] intentionally omitted <==**

where _I_ (.) is an indicator function. It is now clear that we can deduce the direction information from the realized probability index, which means the realized probability index is more informative than the 0–1 binary index. 

Both return and realized probability index contain the direction information, however these two indicators are different in information contents. The return contains the information of price change, while the realized probability index contains the information of relative price change. For example, if return is equal to 0.1, it means price increases 10 % in magnitude; while if realized probability index is 0.6, we can conclude that the cumulative positive return accounts for 60 % of the total price variation. 

## **3.2 Economic Efficiency** 

**Proposition 2.** _Return is more efficient than realized probability index in market timing strategy, and realized probability index is more efficient than 0–1 binary index._ 

Let _𝜇t_ +1 = _Et_ ( _rt_ +1). The conditional expected return of the market timing strategy based on return indicator is presented as follows 

**==> picture [327 x 69] intentionally omitted <==**

which means that the conditional expected return realized by return-based market timing strategy is at least as good as the risk-free return. 

Let _rpt_ +1 = _Et_ ( _RealPt_ +1). The conditional expected return of the market timing strategy based on realized probability index is given by 

**==> picture [323 x 102] intentionally omitted <==**

H. Xie et al.: Timing Market with Realized Probability **— 27** 

By the definition of realized probability index, it can be obtained from condition _Et_ ( _RealPt_ +1) _>_ 0.5 that 

or 

**==> picture [318 x 67] intentionally omitted <==**

which means that so long as _Et_ ( _RealPt_ +1) _>_ 0.5 the expected magnitude of the cumulative positive return ( _CPRt_ +1) is larger than that of the cumulative negative return ( _CNRt_ +1). In other words, if _Et_ ( _RealPt_ +1) _>_ 0.5, the conditional expected return, _𝜇t_ +1 is expected to be positive. Given that risk-free return is non-negative, we can thus conclude that the conditional expected return realized by realized probability index based market timing strategy is nonnegative. That is 

**==> picture [245 x 11] intentionally omitted <==**

Let _pt_ +1 = _Et_ ( _Bt_ +1). The conditional expected return of the market timing strategy based on 0–1 binary index is given by 

**==> picture [320 x 50] intentionally omitted <==**

We can conclude from (15) that the conditional expected return realized by 0–1 binary index based market timing strategy can be either negative or positive, depending on _𝜇t_ +1. For example, if _𝜇t_ +1 _<_ 0 and _pt_ +1 _>_ 0.5, the conditional expected return of this market timing strategy is negative. Thus it can be concluded that 

**==> picture [264 x 11] intentionally omitted <==**

Judging by the conditional expected return realized by different market timing strategies, we can see that market timing strategy based on return indicator is less risky than realized probability based timing strategy, and realized probability based timing strategy is less risky than 0–1 binary index based one. Thus it can be concluded that return-based timing strategy is most efficient, and realized probability index based timing strategy is more efficient than the 0–1 binary index based timing strategy (see Figure 1). 

Propositions 1 and 2 establish under the condition that we know the true conditional distributions of _rt_ +1 and _RealPt_ +1. However, in real applications, the conditional distributions are unknown and should be inferred or estimated from historical data. Thus, the following question would be more important and interesting to practitioners, that is “which market timing indicator is more predictable?”. 

**Figure 1:** Conditional expected return realized by different timing strategies. 

> **28 —** H. Xie et al.: Timing Market with Realized Probability 

## **3.3 Predictability Efficiency** 

**Proposition 3.** _Realized probability index and 0–1 binary index are more predictable than return, and the maximum predictability of realized probability index can be achieved at a lower information ratio compared to the 0–1 binary index._ 

It is well known that asset returns are notoriously difficult to predict due to market efficiency, and voluminous empirical literature has documented that the expected asset return is approximately a constant. For example, after a comprehensive empirical study, Welch and Goyal (2008) find the simple history mean model can hardly be beaten. In the following we will show that even if asset returns are not predictable, the realized probability index can still be timing-varying and thus predictable. 

Following the general way, we assume the asset return over time interval [ _t_ , _t_ + 1] can be described by the following equation 

**==> picture [314 x 10] intentionally omitted <==**

where _𝜎t_ +1 is the conditional volatility, _N_ (0 _,_ 1) is a standard normal. The conditional mean _𝜇_ in this model is specified to be a positive constant, which implies asset returns are unpredictable. 

Intuitively, realized probability index is related to asset volatility. For example, when asset volatility is higher, there is a larger probability that we will realize a larger negative return (see Figure 2), which in turn lowers down the realized probability index. In other words, a larger asset volatility implies a lower realized probability index. Since volatility is well-documented to be time-varying, realized probability index is thus also expected to be time-varying and predictable. 

**==> picture [440 x 60] intentionally omitted <==**

**==> picture [325 x 97] intentionally omitted <==**

**==> picture [423 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.4<br>=1<br>0.35<br>0.3<br>0.25<br>0.2<br>=2<br>0.15<br>0.1 =3<br>0.05<br>0<br>-10 -8 -6 -4 -2 0 2 4 6 8 10 Figure 2: Volatility and probability of negative returns.<br>**----- End of picture text -----**<br>


H. Xie et al.: Timing Market with Realized Probability **— 29** 

> where Φ _z_ (.) is the cumulative distribution function of a standard normal. Similarly we can obtain the expectation of a negative return 

**==> picture [327 x 98] intentionally omitted <==**

Thus we can obtain 

**==> picture [326 x 49] intentionally omitted <==**

According to the definition of realized probability index, we can see 

**==> picture [322 x 104] intentionally omitted <==**

Note that 

**==> picture [370 x 28] intentionally omitted <==**

Thus it follows 

**==> picture [369 x 151] intentionally omitted <==**

_̄_ It is now clear from Equation (24) that realized probability index is a highly nonlinear function of _𝜎t_ +1. Given the empirical fact that asset volatility _𝜎̄ t_ +1 is time-varying and predictable, we can conclude realized probability index is also predictable. 

respectLetto _xt𝜎_ + _̄_ 1 _t_ +=1, _𝜇̄_ ∕ _𝜎̄ t_ +1 and _F_ ( _xt_ +1) = 2Φ( _xt_ +1) − 1 + ~~√~~ _x_ 2 _t_ +∕1 _𝜋[e]_[−][0] _[.]_[5] _[x] t_[2] +1 , we calculate the derivative of _F_ ( _xt_ +1) with 

**==> picture [329 x 27] intentionally omitted <==**

> **30 —** H. Xie et al.: Timing Market with Realized Probability 

**==> picture [439 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.7<br>Realized Probability<br>standard normal<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>-5 -4 -3 -2 -1 0 1 2 3 4 5 Figure 3: Density plots of sign probability and realized prob-<br>x= / ability.<br>Density<br>**----- End of picture text -----**<br>


which means _F_ ( _xt_ +1) is an increasing function of _𝜎̄ t_ +1. Given that realized probability index is negatively related to _F_ ( _xt_ +1), it is straightforward that realized probability is negatively related to asset volatility _𝜎̄ t_ +1. The predictability of realized probability index is very similar to that of the 0–1 binary index. It is clear from Equation (17) that the probability of a positive return is, 

**==> picture [319 x 11] intentionally omitted <==**

which is negatively related to volatility _𝜎t_ +1. Comparing (26) with (24), we find that the predictability of both realized probability index and 0–1 binary index roots in time-varying asset volatility, and that both realized probability index and 0–1 binary index are negatively related to asset volatility. More discussions about the predictability of directions can be found in Christoffersen and Diebold (2006). 

Figure 3 presents the density plots of sign probability and realized probability.[1] We find these two densities are quite similar in shape, however the density of realized probability is more concentrated compared to that of sign probability. This finding is consistent with Xie et al. (2024) that the variance of realized probability is smaller than that of the 0–1 binary index. 

To see how much (realized) probability forecast changes when volatility changes, we calculate the deriva- 

tive, 

**==> picture [257 x 24] intentionally omitted <==**

where Prob _t_ +1 = _Bt_ +1 or _RealPt_ +1. We use the notation  for “responsiveness”. It is obvious from Equation (26) that the response of 0–1 binary index to volatility changes is 

**==> picture [307 x 26] intentionally omitted <==**

where _𝜙_ (.) is the probability density functin (p.d.f.) of the standard normal. By Equation (24), the response of realized probability index to volatility changes is[2] 

> **1** We omit _o p_ (1) when calculating the density of the realized probability. 

> **2** We omit _o p_ (1) when calculating the response function. 

H. Xie et al.: Timing Market with Realized Probability **— 31** 

**==> picture [310 x 87] intentionally omitted <==**

It can be seen that the response of either 0–1 binary index or realized probability is always negative, indicating that both are always decreasing in the conditional standard deviation. 

Figure 4 plots the response as a function of the information ratio, _[𝜇] 𝜎_[for][0–1][binary][index][and] _[𝜇] ̄𝜎[̄]_[for][realized] probability. We find both responses are not monotone in information ratio. For 0–1 binary index, it achieves a minimum at _𝜇_ ∕ _𝜎_ = ~~√~~ 2 ≈ 1.41, while for realized probability index, it achieves a minimum at _𝜇̄_ ∕ _𝜎̄_ ≈ 0.97. This finding is interesting and important, it indicates that maximum predictability of the realized probability index can be achieved at a lower information ratio compared to the 0–1 binary index. In other word, the realized probability index tends to be more predictable than the 0–1 binary index in a low information ratio environment. This finding is also consistent with recent academic literature concerning high-frequency data that high-frequency data provides additional information for financial modeling and forecasting (e.g. Andersen et al. 2001a, 2001b, 2003; Barndorff-Nielsen and Shephard 2002; Bollerslev, Meddahi, and Nyawa 2019; Bollerslev, Patton, and Quaedvlieg 2018, 2020; Neuberger 2012). 

Table 1 summarizes the findings posted in propositions 1–3. It is clear that the realized probability index and the return dominates the 0–1 binary index in information contents and market timing strategy. However, in terms of predictability, realized probability index and 0–1 binary index tend to be more predictable than return. In real applications, better predictability usually means better decision. Given the fact that realized probability index is more efficient than 0–1 binary index and more predictable than return, we thus can conclude that realized probability index is a better indicator in market timing strategy. 

**==> picture [232 x 182] intentionally omitted <==**

**----- Start of picture text -----**<br>
0<br>RealPt+1<br>-0.05 Bt+1<br>-0.1<br>-0.15<br>-0.2<br>-0.25<br>-0.3<br>0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5<br>/<br>Derivative<br>**----- End of picture text -----**<br>


**Figure 4:** Response of sign probability and realized probability to volatility movements plotted against the information ratio. 

**Table 1:** Efficiency comparison among different market timing indicators. 

||**0–1** **binary** **index**|**Realized** **probability**|**Return**|
|---|---|---|---|
|Information efficiency|Less|More|More|
|Economic efficiency|Less efficient|More efficient|Most efficient|
|Predictability efficiency|Good|Better|Difficult|



> **32 —** H. Xie et al.: Timing Market with Realized Probability 

## **4 Empirical Evidence** 

We collect the daily prices of different stock indices, including SPX, NYSE, IXIC of U.S.A., FTSE of U.K., DAX of Germany, FCHI of French, N225 of Japan, HS300 of China. From the daily prices, we construct the monthly return series, the 0–1 binary index, and the realized probability index. For SPX, the time-horizon spans 1928.01–2023.11 with 1,151 observations. For the remaining indices, the time-horizons span respectively 1991.01–2023.11 with 395 observations, 1971.03–2023.11 with 633 observations, 1984.02–2023.11 with 478 observations, 1980.02–2023.11 with 526 observations, 1987.08–2023.11 with 436 observations, 1974.02–2023.11 with 598 observations, and 2002.02–2023.11 with 262 observations. All the data sets are downloaded from Wind database. 

Table 2 presents the summary statistics of return, 0–1 binary index, and realized probability index on different stock indices. The distribution of return on each of these stock indices is found to be negatively skewed 

**Table 2:** Summary statistics of return, realized probability index, 0–1 binary index. 

|**SPX**|**Mean**|**St.d.**|**Median**|**Min.**|**Max.**|**Skewness**|**Kurtosis**|
|---|---|---|---|---|---|---|---|
|Ret|0.005|0.054|0.009|−0.356|0.330|−0.608|10.901|
|RealP|0.539|0.151|0.537|0.153|0.914|0.034|2.454|
|_B_|0.594|0.491|1.000|0.000|1.000|−0.384|1.147|
|||||**NYSE**||||
|Ret|0.005|0.043|0.010|−0.217|0.119|−0.922|5.872|
|RealP|0.542|0.134|0.541|0.225|0.887|−0.009|2.316|
|_B_|0.623|0.485|1.000|0.000|1.000|−0.507|1.257|
|||||**FTSE**||||
|Ret|0.004|0.044|0.009|−0.302|0.135|−1.070|8.022|
|RealP|0.533|0.129|0.538|0.185|0.935|0.006|2.577|
|_B_|0.590|0.492|1.000|0.000|1.000|−0.366|1.134|
|||||**DAX**||||
|Ret|0.007|0.059|0.013|−0.293|0.194|−0.827|5.740|
|RealP|0.539|0.139|0.535|0.193|0.943|0.129|2.533|
|_B_|0.593|0.491|1.000|0.000|1.000|−0.379|1.144|
|||||**N**||||
|Ret|0.003|0.054|0.008|−0.272|0.183|−0.584|4.685|
|RealP|0.532|0.144|0.521|0.181|0.949|0.139|2.610|
|_B_|0.560|0.497|1.000|0.000|1.000|−0.243|1.059|
|||||**IXIC**||||
|Ret|0.008|0.061|0.014|−0.318|0.199|−0.815|5.682|
|RealP|0.552|0.169|0.549|0.098|0.977|0.064|2.354|
|_B_|0.596|0.491|1.000|0.000|1.000|−0.390|1.152|
|||||**FCHI**||||
|Ret|0.004|0.056|0.010|−0.260|0.219|−0.501|4.705|
|RealP|0.530|0.135|0.530|0.209|0.877|0.171|2.346|
|_B_|0.573|0.495|1.000|0.000|1.000|−0.297|1.088|
|||||**HS**||||
|Ret|0.004|0.078|0.006|−0.299|0.246|−0.353|4.879|
|RealP|0.516|0.153|0.518|0.140|0.856|0.071|2.309|
|_B_|0.553|0.498|1.000|0.000|1.000|−0.215|1.046|



H. Xie et al.: Timing Market with Realized Probability **— 33** 

**==> picture [431 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
SPX NYSE FTSE<br>1 1 1<br>Betafit<br>0.8 Empirical 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>0 0.2 0.4 0.6 0.8 1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 0 0.2 0.4 0.6 0.8 1<br>realized probability realized probability realized probability<br>DAX N225 IXIC<br>1 1 1<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1<br>realized probability realized probability realized probability<br>FCHI HS300<br>1 1<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>0 0<br>0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 0 0.2 0.4 0.6 0.8 1<br>realized probability realized probability<br>F(x) F(x) F(x)<br>F(x) F(x) F(x)<br>F(x) F(x)<br>**----- End of picture text -----**<br>


**Figure 5:** Cumulative distributions of realized probability index: empirical v.s. beta-fitted. 

and heavily tailed as the skewness statistics are reported to be negative and the kurtosis statistics are reported to be larger than 3. Compared with the 0–1 binary index and the return, the realized probability index is less asymmetric and heavily-tailed. Consistent with Xie et al. (2024), the realized probability index is less volatile compared with the 0–1 binary index judging by the standard deviation statistics. Figure 5 presents the empirical distributions of the realized probability index on each stock index, together with the Beta-fitted distributions. Consistent with Xie et al. (2024), we find the realized probability index can be well approximated by the beta density function. Figure 6 presents the sample autocorrelation functions of the cumulative absolute return ( _CARt_ +1) of each stock index. It is clear that the cumulative absolute return of the stock index is time-varying with high persistence and predictability. 

It has been claimed in proposition 4 that even if return itself is unpredictable, the 0–1 binary index and the realized probability index remian predictable due to time-varying and predictable volatility. We scrutinize this proposition with the following linear regression 

**==> picture [278 x 11] intentionally omitted <==**

where _Indext_ +1 = {return, 0–1 binary index, realized probability index}, and _𝜆t_ +1 is a kind of volatility index. In this paper, _𝜆t_ +1 is filtered from _CARt_ +1 with the following CARR model of Chou (2005) 

**==> picture [348 x 11] intentionally omitted <==**

where _zt_ +1 is a positive density function with unit mean, parameter _𝛾_ is used to capture the leverage effect in volatility. 

The realized probability index and the 0–1 binary index are negatively correlated with _𝜆t_ +1 by Equations (28) and (29). Therefore the regression coefficient _𝛽_ 1 in Equation (30) is expected to be negative for both 0–1 binary index and realized probability index. For the return, Equation (30) is used to capture the risk-return tradeoff in market risk premium (Engle, Lilien, and Robins 1987). 

When performing linear regression on Equation (30), the Newey and West (1987) adjustment is used for the potential heterogeneity and autocorrelation in error, and the results are presented in Table 3. Consistent with the existed empirical literature, we also find returns are very difficult to forecast: no significant risk-return 

> **34 —** H. Xie et al.: Timing Market with Realized Probability 

**==> picture [431 x 229] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 1 1<br>SPX NYSE FTSE<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>0 5 10 15 20 0 5 10 15 20 0 5 10 15 20<br>Lag Lag Lag<br>1 1 1<br>DAX N225 IXIC<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>0 5 10 15 20 0 5 10 15 20 0 5 10 15 20<br>Lag Lag Lag<br>1 1<br>FCHI HS300<br>0.8 0.8<br>0.6 0.6<br>0.4 0.4<br>0.2 0.2<br>0 0<br>0 5 10 15 20 0 5 10 15 20<br>Lag Lag<br>Sample Autocorrelation Sample Autocorrelation Sample Autocorrelation<br>Sample Autocorrelation Sample Autocorrelation Sample Autocorrelation<br>Sample Autocorrelation Sample Autocorrelation<br>**----- End of picture text -----**<br>


**Figure 6:** Sample autocorrelation functions of cumulative absolute return ( _CARt_ ) of different market indices. 

**Table 3:** Regression results of return, realized probability index and 0–1 binary index on price variation. 

||**SPX**|**NYSE**|**FTSE**|**DAX**|**N225**|**IXIC**|**FCHI**|**HS300**|
|---|---|---|---|---|---|---|---|---|
|**Panel A:**||||Return|||||
|_𝜓_|−0.016|−0.006|0.010|0.009|−0.026|−0.026|−0.025|−0.057|
|Adjusted _R_ |0.00 %|0.00 %|0.00 %|0.00 %|0.00 %|0.00 %|0.00 %|0.00 %|
|**Panel** **B:**|||0–1|Binary|Index||||
|_𝜓_|−0.209|−0.265|0.205|−0.206|−**.** ∗∗|−0.247|−0.126|0.109|
|Adjusted _R_ |0.05 %|0.00 %|0.00 %|0.00 %|0.41 %|0.06 %|0.00 %|0.00 %|
|**Panel** **C:**|||Realized|Probability|Index||||
|_𝜓_|−**.** ∗∗|−0.075|−0.014|−0.075|−**.** ∗∗∗|−**.** ∗|−0.070|−0.022|
|Adjusted _R_ |0.36 %|0.00 %|0.00 %|0.00 %|0.74 %|0.28 %|0.00 %|0.00 %|



This table reports the regression results based on Equation (31): _Indext_ +1 = _𝜃_ + _𝜓𝜆t_ +1 + _𝜀t_ +1 _,_ where _Indext_ +1 = {return, 0–1 binary index, realized probability index}, _𝜆t_ +1 is the conditional mean of _CARt_ +1. We filter the conditional mean _𝜆t_ +1 from _CARt_ +1 using the following CARR model of Chou (2005) _CARt_ +1 = _𝜆t_ +1 _zt_ +1 _, 𝜆t_ +1 = _𝜔_ + _𝛼𝜆t_ + _𝛽CARt_ + _𝛾CARt_ × _I_ ( _rt <_ 0) where _zt_ +1 is a positive density function with unit mean. The QMLE (quasi maximum likelihood estimation) method with exponential density is used to estimate the model. We use[∗∗∗] ,[∗∗] , and[∗] to mean respectively significance at the level of 1 %, 5 %, and 10 %. 

tradeoff is detected in either one of these stock indices. It is more interesting to compare realized probability index regression results with 0–1 binary regression results. For the 0–1 binary index, the regression coefficient _𝛽_ 1s are reported to be negative in 6 out of the 8 markets; while for the realized probability index, all the regression coefficient _𝛽_ 1s are reported to be negative. This finding is consistent with our expectation that 0–1 binary index and realized probability index are negatively correlated with volatility. Moreover, the empirical results seem to indicate that realized probability index is more predictable than 0–1 binary index since three realized probability indices are reported to be significantly predictable while only one 0–1 binary index is found to be predictable. 

H. Xie et al.: Timing Market with Realized Probability **— 35** 

For 0–1 binary index, we also perform the following logit regression 

**==> picture [278 x 24] intentionally omitted <==**

where _pt_ +1 is the conditional probability of _Bt_ +1 = 1. The findings remain unchanged. We do not present the results for the sake of saving space. 

Of course this empirical finding should be interpreted with cautiousness. It is well-known that predictability is more an empirical issue than a theoretical issue, whose results depend on many points, such as data selection, model specification, estimation, and so on. However, based on the data and the model used in this paper, we find the realized probability index is more predictable than the 0–1 binary index and the return. 

## **5 Conclusions** 

This paper compares three indicators used in market timing strategy: the return, the 0–1 binary index, and the realized probability index, and four propositions are obtained from the comparison. The most interesting and important finding detected in this paper is that the realized probability index is not only more informative and efficient than the traditional 0–1 binary index in market timing strategy but also more predictable than the return. This finding hints that the realized probability index is a better market timing indicator, and thus should be given more attention in practice. 

Realized probability index is double-bounded, which makes it totally different from most of the other financial time series. So far as we know there is not a time series model specified for realized probability index. Given the fact that there are so many models considering the dynamics of 0–1 binary index, dynamic models based on realized probability index and their empirical performance would be of great interest to both practitioners and academic researchers for future studies. 

**Author contributions:** All the authors have accepted responsibility for the entire content of this submitted manuscript and approved submission. 

**Competing interests:** The authors declare no competing interests regarding this article. 

**Research funding:** This research is supported by National Natural Science Foundation of China under Grant Nos. 72271055, 72073126, 71988101 and 72322016. 

## **References** 

Anatolyev, S., and N. Gospodinov. 2010. “Modeling Financial Return Dynamics by Decomposition.” _Journal of Business & Economic Statistics_ 28 (2): 232−45 **.** Andersen, T. G., T. Bollerslev, F. X. Diebold, and H. Ebens. 2001a. “The Distribution of Realized Stock Return Volatility.” _Journal of Financial Economics_ 61: 43−76 **.** 

Andersen, T. G., T. Bollerslev, F. X. Diebold, and P. Labys. 2001b. “The Distribution of Exchange Rate Volatility.” _Journal of the American Statistical Association_ 96: 42−55 **.** 

Andersen, T. G., T. Bollerslev, F. X. Diebold, and P. Labys. 2003. “Modeling and Forecasting Realized Volatility.” _Econometrica_ 71: 579−625 **.** Barndorff-Nielsen, O. E., and N. Shephard. 2002. “Econometric Analysis of Realised Volatility and its Use in Estimating Stochastic Volatility Models.” _Journal of the Royal Statistical Society: Series B_ 64: 253−80 **.** 

Bollerslev, T., N. Meddahi, and S. Nyawa. 2019. “High-dimensional Multivariate Realized Volatility Estimation.” _Journal of Econometrics_ 212: 116−36 **.** Bollerslev, T., A. J. Patton, and R. Quaedvlieg. 2018. “Modeling and Forecasting (Un)reliable Realized Covariances for More Reliable Financial Decisions.” _Journal of Econometrics_ 207: 71−91 **.** 

Bollerslev, T., A. J. Patton, and R. Quaedvlieg. 2020. “Realized Semicovariances.” _Econometrica_ 88 (4): 1515−51 **.** Chou, R. Y. 2005. “Forecasting Financial Volatilities with Extreme Values: The Conditional Autoregressive Range (CARR) Model.” _Journal of Money, Credit, and Banking_ 37 (3): 561−82 **.** 

Christoffersen, P., and F. Diebold. 2006. “Financial Asset Returns, Direction-of-Change Forecasting, and Volatility Dynamics.” _Management Science_ 52 (8): 1273−87 **.** 

> **36 —** H. Xie et al.: Timing Market with Realized Probability 

Chung, J., and Y. Hong. 2007. “Model-free Evaluation of Directional Predictability in Foreign Exchange Markets.” _Journal of Applied Econometrics_ 22 (5): 855−89 **.** 

Engle, R. F., D. M. Lilien, and R. P. Robins. 1987. “Estimating Time Varying Risk Premia in the Term Structure: The Arch-M Model.” _Econometrica_ 55: 391−407 **.** 

Hong, Y., and J. Chung. 2006. _Are the Directions of Stock Price Changes Predictable? A Generalized Cross-Spectral Approach_ . Department of Economics, Cornell University. Working Paper. 

Kauppi, H., and P. Saikkonen. 2008. “Predicting U.S. Recessions with Dynamic Binary Response Models.” _The Review of Economics and Statistics_ 90: 777−91 **.** 

Leitch, G., and J. Tanner. 1991. “Economic Forecast Evaluation: Profits versus the Conventional Error Measures.” _The American Economic Review_ 81: 580−90. 

Leitch, G., and J. Tanner. 1995. “Professional Economic Forecasts: Are They Worth Their Costs?” _Journal of Forecasting_ 14: 143−57 **.** Leung, M. T., H. Daouk, and A. S. Chen. 2000. “Forecasting Stock Indices: A Comparison of Classification and Level Estimation Models.” _International Journal of Forecasting_ 16: 173−90 **.** 

Merton, R. 1981. “On Market Timing and Investment Performance: An Equilibrium Theory of Value for Market Forecasts.” _Journal of Business_ 54: 363−406 **.** 

Neuberger, A. 2012. “Realized Skewness.” _Review of Financial Studies_ 25 (11): 3423−55 **.** 

Newey, W. K., and K. D. West. 1987. “A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix.” _Econometrica_ 55 (3): 703−8 **.** 

Nyberg, H. 2011. “Forecasting the Direction of the US Stock Market with Dynamic Binary Probit Models.” _International Journal of Forecasting_ 27 (2): 561−78 **.** 

Nyberg, H., and H. Ponka. 2016. “International Sign Predictability of Stock Returns: The Role of the United States.” _Economic Modelling_ 58: 323−38 **.** Pring, M. J. 1991. _Technical Analysis Explained: The Successful Investor’s Guide to Spotting Investment Trends and Turning Points_ . New York: McGraw-Hill. 

Rydberg, T., and N. Shephard. 2003. “Dynamics of Trade-By-Trade Price Movements: Decomposition and Models.” _Journal of Financial Econometrics_ 1: 2−25 **.** 

Welch, I., and A. Goyal. 2008. “A Comprehensive Look at the Empirical Performance of Equity Premium Prediction.” _It Review of Financial Studies_ 21 (4): 1455−508 **.** 

Xie, H. B., J. J. Zhang, Y. Chen, and Z. D. Lu. 2024. “Realized Probability.” _Journal of Systems Science and Complexity_ . https://sysmath.cjoe.ac .cn/jssc/EN/abstract/abstract52982.shtml. 

**Supplementary Material:** This article contains supplementary material (https://doi.org/10.1515/snde-2024-0060). 

