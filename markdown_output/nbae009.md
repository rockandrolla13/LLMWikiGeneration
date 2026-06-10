_Journal of Financial Econometrics_ , 2024, **22** , 1588–1615 https://doi.org/10.1093/jjfinec/nbae009 Advance access publication 26 April 2024 **Article** 

**==> picture [65 x 52] intentionally omitted <==**

## **Jump Clustering, Information Flows, and Stock Price Efficiency[†]** 

## **Jian Chen*** 

Business School, University of Sussex, Brighton, BN1 9SL, UK 

*Address correspondence to Jian Chen, University of Sussex Business School, Brighton, BN1 9SL, UK, or e-mail: jian.chen@sussex.ac.uk 

## **Abstract** 

We study the clustering behavior of stock return jumps modeled by a self/cross-exciting process embedded in a stochastic volatility model. Based on the model estimates, we propose a novel measurement of stock price efficiency characterized by the extent of jump clustering that stock returns exhibit. This measurement demonstrates the capability of capturing the speed at which stock prices assimilate new information, especially at the firm-specific level. Furthermore, we assess the predictability of selfexciting (clustered) jumps in stock returns. We employ a particle filter to sample latent states in the out-of-sample period and perform one-step-ahead probabilistic forecasting on upcoming jumps. We introduce a new statistic derived from predicted probabilities of positive and negative jumps, which has been shown to be effective in return predictions. 

**Keywords:** Bayesian inference, information flows, jump clustering, jump prediction, stock price efficiency **JEL classifications:** C58, G12, G17 

It has been established in the literature that stock prices sometimes exhibit significant discontinuities, and these discontinuities are often referred to as “jumps.” Numerous studies have demonstrated that news announcements are a primary driving force behind stock price jumps. For example, Lee (2012) discovers that days with scheduled news are more likely to experience return jumps. Jeon, McCurdy, and Zhao (2022) use textual analysis to investigate the impact of the news on jump intensities and jump size distributions. Also see recent studies � by Gurkaynak, Kisacikoglu, and Wright (2020), Baker et al. (2021), and Engle et al. (2021). However, the speed at which the news is incorporated into stock prices tends to depend on the nature of news—its complexity and level of informativeness (Loughran and McDonald 2014) and the attention of investors (Hirshleifer, Lim, and Teoh 2009).[1 ] Therefore, for the less efficient stocks with low news-incorporation speed, new information may not be incorporated into stock prices with one single jump, but rather through a potential sequence of jumps. This motivates us to study the clustering behaviors of asset return jumps. 

> † Part of the work was completed when Jian Chen attended ICMA Centre, Henley Business School, University of Reading, as a PhD student. I am indebted to my supervisors, Michael P. Clements and Andrew Urquhart, for their guidance. I am also very grateful for the extensive comments and discussions with Linquan Chen at the University of Exeter Business School. I also thank the editor, the associate editor, two anonymous referees, Shuyuan Qi, and the participants at the 2022 IAAE Annual Conference and 2022 CFE Conference for their helpful comments. All errors are mine. 

1 Also see studies on news incorporation speed by Da, Gurun, and Warachka (2014), Tao et al. (2021), and Jeon et al. (2022). 

**Received:** August 15, 2023. **Revised:** March 31, 2024. **Editorial decision:** April 02, 2024. **Accepted:** April 04, 2024 

# The Author(s) 2024. Published by Oxford University Press. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs licence (https://creativecommons.org/licenses/by-nc-nd/4.0/), which permits non-commercial reproduction and distribution of the work, in any medium, provided the original work is not altered or transformed in any way, and that the work is properly cited. For commercial re-use, please contact journals.permissions@oup.com 

Chen j Jump Clustering and Pricing Efficiency **1589** 

**Figure 1.** Daily price, return, jumps, and volatility of Ampco-Pittsburgh Corporation (NYSE: AP). _Notes_ : These variables are estimated using an SVCJ model proposed by Duffie et al. (2000) with daily data from 1 January 2000 to 31 December 2012. The last four figures are for 15 days before and 25 days after the company’s 2005Q2 and 2005Q4 earnings announcements. _yt_ denotes the stock returns, ξ _t_ denotes the return jump component, _vt_ presents the variance. 

For a simple example, we plot daily stock prices, returns, volatility, and return jumps[2 ] of the Ampco-Pittsburgh Corporation (NYSE: AP) in Figure 1. We can see subsequent return 

> 2 These estimates derive from the stochastic volatility with correlated jumps model proposed by Duffie et al. (2000). The data used in the estimation are from 2000 to 2012, which is in line with the in-sample period of this paper. 

**1590** _Journal of Financial Econometrics_ 

jumps after two earnings announcements despite the model’s assumption of constant jump intensities. This could occur if the return jump on the announcement date failed to fully absorb all the information and caused the second return jump. Additionally, it is noteworthy that variance increases during news announcements, which is consistent with the literature (Erdemlioglu and Yang 2023). Later in this article, we further show that such abnormal return originates from the jump clustering and stock inefficiency, which is robust to stock illiquidity. 

This gives rise to the research questions we aim to address in this article: (1) What do these clustered jumps suggest? Does the information contained in the jump clustering vary across assets?; (2) Given a dependency among jumps, in the sense that jumps do not arrive independently, can we exploit this characteristic to forecast jumps? Furthermore, to what extent are these clustered jumps predictable? 

In this article, we model these jumps using a self/cross-exciting point process proposed by Hawkes (1971a, 1971b). This approach enables the probability (intensity) of jumps to be dependent on past jumps. This implies that the occurrences of jumps can increase the probability of future jumps, which is in line with the jump clustering behaviors we have observed. More specifically, we separate stock return jumps into positive and negative ones. The term “selfexcitation” describes the propensity for positive/negative return jumps of an asset to generate subsequent positive/negative return jumps of the same asset. Conversely, “cross-excitation” denotes the capacity for positive/negative return jumps of an asset to trigger subsequent negative/positive return jumps of the same asset. We embed the self/cross-exciting jumps in a stochastic volatility model and let the model determine whether a return includes a jump and whether additional jump clustering parameters are necessary to describe the data. We estimate the model using a Bayesian Markov Chain Monte Carlo (MCMC) method. 

Based on the model, we contribute to the literature in two ways. First, we find strong evidence of jump clustering with varying degrees across assets, which are closely related to information releases. We introduce a novel measure of stock price efficiency, denoted by f, based on the degree of jump clustering exhibited by asset returns. This measure is derived from the posterior distributions of the jump clustering parameters. The underlying rationale is that if a stock requires more than one jump to fully incorporate new information, it is potentially less efficient than those stocks requiring only a single jump. In light of this, assuming the arrival of information is random and independent, it stands to reason that for efficient stocks, the jump arrivals should likewise be random and independent. Thus, the extent to which a stock’s jumps cluster together can serve as a measure of its efficiency. This measure’s advantages lie in its convenience and generality. For example, one can surely assess how quickly a stock absorbs a type of information by calculating the average return drift of the stock after the information arrives. However, there are numerous types of information, and their incorporation speeds may differ. In contrast, the degree of jump clustering can be easily calculated without knowing when and what types of information arrive. 

We conduct a regression analysis on cross-sectional cumulative abnormal returns (CAR) after announcements with several different stock price efficiency measures while controlling for a broad set of variables. The findings indicate that our measure, f, more accurately captures the cross-sectional variations of CAR and post-earnings-announcement drifts (PEAD) compared to existing measures and is robust to control variables, including stock illiquidity. 

Second, we utilize a particle filter-based framework to conduct probabilistic forecasting of return jumps. Given the presence of jump clustering and the probability of jumps being a function of past jumps, we show the possibility of forecasting the self-exciting jumps and investigating their predictability. Specifically, we first fixed static parameters at their posterior means estimated in the in-sample period. In the out-of-sample, we use a particle filter to iteratively estimate latent variables at each time point as new returns are observed. Subsequently, we approximate the predictive distribution of jumps, which is assessed by a ranked probability score (RPS). Additionally, we introduce a statistic that takes the 

Chen j Jump Clustering and Pricing Efficiency **1591** 

difference between the predicted probabilities between positive and negative jumps. We find that high and low values of this statistic have predictive power on returns, with predictability directly linked to the degree of jump clustering exhibited by the asset (i.e., the stock price efficiency measure we proposed). Based on this forecasting framework, a trading strategy yields a Sharpe ratio (SR) of 1.62, inclusive of transaction costs. 

Our studies contribute to several streams of literature. First, it is related to studies examining announcement effects. For example, studies on the pre-announcement drifts of macro news (Bernile, Hu, and Tang 2016; Kurov et al. 2019), PEAD (Bernard and Thomas 1989; Hung, Li, and Wang 2015), among others, show evidence of price drifts preceding and following various announcements. Moreover, Lee (2012) and Jeon, McCurdy, and Zhao (2022) relate jumps to news releases. In our article, we study the information flows from the perspective of jump clustering behaviors before and after announcements. Additionally, the findings of Christensen, Timmermann, and Veliyev (2023) based on high-frequency data indicate limited price discovery in the days following earnings announcements. However, their findings are confined to 50 liquid firms due to the extensive size of high-frequency data, while we look at all US stocks and aim to capture the speed of price discovery using daily data. 

Our studies are also related to the stock price efficiency literature. The most widely used stock price efficiency measure is the price delay developed by Hou and Moskowitz (2005), who study the predictive power of lagged market returns on asset returns as a measure of stock price efficiency. Numerous studies have subsequently employed this measure. They explored the relationship between price efficiency and various factors, including shortsellings (Saffi and Sigurdsson 2011; Jones, Reed, and Waller 2016), dark trading (Foley and Putniņ�s 2016), share repurchase (Busch and Obernberger 2017), firm bankruptcy risk (Brogaard, Li, and Xia 2017), among others. Furthermore, Bris, Goetzmann, and Zhu (2007) propose to use the first-order autocorrelation of stock returns with lagged market returns. However, these measures predominantly capture the gradual pace at which market information is transmitted to individual assets, which is less relevant to firm-specific information. Our measurement assesses the extent to which a stock’s return jumps cluster together, without differentiating between different types of information. 

Moreover, our studies contribute to the jump clustering and jump forecasting literature. The jump clustering effect is mentioned by Lee (2012) and Lee and Wang (2019). They filter jumps non-parametrically and estimate a logit model for the jump’s probability using dummy variables to capture news releases. They also include a dummy variable that equals one when there is a jump in the past period of time. They demonstrate the effectiveness of the model in forecasting the probability of jumps. Jeon, McCurdy, and Zhao (2022) also adopt a logit model of jump’s probability. In this article, we adopt a different approach. The predictability we aim to examine solely stems from the degree of jump clustering exhibited by the asset. There are also many other applications of the mutually exciting point process with financial data. For example, Aït-Sahalia, Cacho-Diaz, and Laeven (2015) investigate jump spillovers among international stock markets. Herrera and Clements (2020) develop a point process risk model that integrates a select set of covariates into the tail distribution of intraday returns. Kwok (2024) proposes a test for the dependence of jump occurrences. 

Lastly, our studies are also relevant to literature on stochastic volatility models. Continuous-time stochastic volatility models have been well-established in the literature (see, e.g., Heston 1993; Bates 1996; Duffie, Pan, and Singleton 2000; Kou, Yu, and Zhong 2017). Additionally, there exists a stream a literature incorporates the self-exciting jumps into continuous-time models, for example, Maneesoonthorn, Forbes, and Martin (2017) and Chen, Clements, and Urquhart (2023). These studies concentrate on the overall fit of the model to empirical data. Furthermore, we emphasize that discrete-time stochastic volatility models also hold significant interest in the literature, particularly in modeling the cross-section of the yield curve (see, e.g., Creal and Wu 2015, 2017). 

**1592** _Journal of Financial Econometrics_ 

The rest of this article is organized as follows. Section 1 introduces our model. Section 2 presents model estimation approaches, the forecasting framework, and the data we used in the empirical studies. Section 3 presents our studies on news releases and stock price efficiency. Section 4 presents the out-of-sample forecasting results. Section 5 concludes the article. Some technical results are confined to the Appendix. 

## **1. The Model** 

In this section, we introduce a continuous representation of an asset’s return and variance processes and how we embed a self/cross-exciting process in the model. Then, we will describe the discretized version of the model. 

## 1.1 Return and Variance Process 

Denoting _Pt_ as the logarithm of an asset price at time _t_ , we assume its log returns at _t >_ 0 evolve according to the following semimartingale dynamic: 

**==> picture [245 x 17] intentionally omitted <==**

where μ is a constant drift term. _dWt[p]_[is the standard Brownian motion of the return pro-] cess. ξ _[p] t[dN] t[p]_[denotes the return jump component. We assume the variance process follows: ] 

**==> picture [266 x 17] intentionally omitted <==**

where κ _;_ θ represent the mean reversion speed and the long-run variance mean of the variance. σ _v_ denotes the volatility of volatility. The Brownian motion of the variance _dWt[v]_[is as-] sumed to be correlated with _dWt[p]_[with a correlation ] _[E]_[ð] _[dW] t[p][;][ dW] t[v]_[Þ ¼][ ρ] _[dt]_[. ][ξ] _[v] t[dN] t[v]_[denotes ] the variance jump component. 

Regarding the return jump component ξ _[p] t[dN] t[p][;]_[ξ] _[p] t_[denotes the return jump size. We sepa-] rate ξ _[p] t_[to ][ξ] _[p] t_[¼][ ξ] _[p] t_[þ][þ][ξ] _[p] t_[−][, which follow two truncated normal distribution ][ξ] _[p] t_[þ] �N ðμ _p_ þ _;_ σ _p_ þÞ **1** ξ _[p] t_[þ] _[>]_[0] _[;]_[ξ] _[p] t_[−] �N ðμ _p_ − _;_ σ _p_ −Þ **1** ξ _[p] t_[−] _[<]_[0][. ][ξ] _t[v]_[denotes the variance jump size that follows an ex-] ponential distribution with mean μ _v_ , ξ _[v] t_[�][exp][ð][μ] _v_[Þ][. The ] _[dN] t[p]_[is a counting process, which is ] also split into _dNt_ ¼ _dNt[p]_[þ][þ] _[dN] t[p]_[−] with corresponding intensities _P_ ð _dNt[i]_[¼][ 1][Þ ¼][ λ] _[i] t[dt][;] i_ ¼ f _p_ þ _; p_ −g. This is based on the finite activity of jumps rather than an infinite activity since our primary interest is capturing the clustering behavior of rare jumps instead of a large number of small jumps. Similarly, The _dNt[v]_[is a counting process for the variance ] jump with corresponding constant intensity _P_ ð _dNt[v]_[¼][ 1][Þ ¼][ λ] _[v]_ 0 _[dt]_[.] 

## 1.2 Self/Cross-Exciting Return Jumps 

In this article, we further impose the self- and cross-impact on positive and negative return jumps. Under a self/cross-exciting jumps specification, instead of being constant, the underlying intensity of positive and negative jumps at time _t_ follows: 

**==> picture [270 x 54] intentionally omitted <==**

Chen j Jump Clustering and Pricing Efficiency **1593** 

where λ _[p]_ 0[þ] _[;]_[ λ] _[p]_ 0[−][are non-negative constants. ][ϑ] _[i][;][j ]_[measures the expected number of jumps in ] _[i ]_ that is produced by jumps in _j_ and _i; j_ 2 f _p_ þ _; p_ −g; we also restrict ϑ _[i][;][j]_ ≥0. ϕ _[i][;][j]_ ð _t_ − _s_ Þ denotes a decaying function such that ϕ : **R** þ ! **R** þ. We adopt an exponentially decaying function ϕ _[i][;][j]_ ð _t_ − _s_ Þ ¼ β _[i][;][j] e_[−β] _[i][;][j]_[ð] _[t]_[−] _[s]_[Þ] , where β _[i][;][j] >_ 0 captures the decaying speed. The intuition of this specification is allowing every past jump _dNs[j][;][s]_[ 2 ð][−][1] _[;][ t]_[Þ] _[;][j]_[ ¼] f _p_ þ _; p_ −g to raise up the intensity at time _t_ , λ _[i] t_[, by ][ϑ] _[i][;][j]_[ �][ϕ] _[i][;][j]_[ð] _[t]_[−] _[s]_[Þ][. In other words, when ] there is a jump _j_ observed at time _t_ , the underlying intensity λ _[i] t_[will increase to ][λ] _[i]_ 0[þ][ϑ] _[i][;][j]_[ �][β] _[i][;][j ]_ instantaneously; it will decay back to λ _[i]_ 0[by the speed of ][β] _[i][;][j]_[. ][ϑ ][is a 2][×][2 matrix, capturing ] the self/cross-excitation (clustering) of positive and negative return jumps. Note our specification is slightly different from other literature. For example, Aït-Sahalia, CachoDiaz, and Laeven (2015) forgo the ϑ and let λ _[i] t_[¼][ λ] _[i]_ 0[þ][ P] _j_ ¼f _p_ þ _;p_ −g Ð _t_ −1 _[g][i][;][j]_[ð] _[t]_[−] _[s]_[Þ] _[dN][j][;][s]_[, where ] _g[i][;][j]_ ð _t_ − _s_ Þ ¼ α _[i][;][j] e_[−β] _[i][;][j]_[ð] _[t]_[−] _[s]_[Þ] . α _[i][;][j ]_ can be interpreted as the incremental intensity of jumps _i_ that is raised by past jumps _j_ . In this case, α _[i][;][j ]_ is equivalent to ϑ _[i][;][j]_ � β _[i][;][j ]_ in our setting. 

This self/cross-excitation setup provides a model for capturing jump clustering in financial assets. ϑ allows the jump intensity to depend on past jumps. It can also be an asymmetric matrix when the extent to which positive return jumps produce negative ones is different from the extent to which negative return jumps produce positive ones. In addition, ϑ � 0 when there is no jump clustering. Indeed, this model could be expanded to higher dimensions by including the impact of jumps in all other assets. However, it is not our primary focus; we are more interested in time-series jump dependence across different assets and their predictability. 

Furthermore, we define f ¼[P] ϑ _[i][;][i]_ , where ϑ _[i][;][i ]_ denotes the diagonal elements of matrix ϑ. Later in this article, we will employ f to quantify an asset’s extent to which its jumps are clustering, especially those clustered jumps of the same sign. Additionally, we will explore the implications of this measure for asset pricing. 

## 1.3 The Discretized Form 

We apply an Euler’s discretization with Δ ¼ 1/252 and obtain the following form: 

**==> picture [246 x 17] intentionally omitted <==**

**==> picture [267 x 16] intentionally omitted <==**

where _pt_ is the natural logarithm of an asset price at time _t_ . μ is the return drift. ɛ _[p] t_[and ][ɛ] _[v] t_ are two standard normal random variables with a correlation ρ. _vt_ denotes the variance modeled as a mean-reversion structure (κ _;_ θ), a random variable with a volatility of volatility σ _v_ and the variance jump component ξ _[v] t[J] t[v]_[. The return jump size is split into positive and ] negative, which are assumed to follow two truncated normal distributions: ξ _[p] t_[¼][ ξ] _[p] t_[þ][þ] ξ _[p] t_[−] _[;]_[ξ] _[p] t_[þ] �N ðμ _p_ þ _;_ σ _p_ þÞ **1** ξ _pt_ þ _[>]_[0] _[;]_[ξ] _[p] t_[−] �N ðμ _p_ − _;_ σ _p_ −Þ **1** ξ _[p] t_[−] _[<]_[0][. Similarly, ] _[J] t[p]_[is split into a positive ] and a negative one, _Jt[p]_[¼] _[ J] t[p]_[þ][þ] _[J] t[p]_[−][, where ] _[J] t[p]_[þ] and _Jt[p]_[−] are two Bernoulli random variables with corresponding intensity: 

**==> picture [252 x 12] intentionally omitted <==**

where λ _[i] t_[has the following dynamics: ] 

**==> picture [287 x 22] intentionally omitted <==**

where ϕ _[i][;][j]_ ð _t_ − _s_ Þ ¼ β _[i][;][j] e_[−β] _[i][;][j]_[ð] _[t]_[−] _[s]_[Þ] . ξ _[v] t_[denotes the variance jump size that follows an exponential ] distribution with mean μ _v_ , and the _Jt[v]_[is a Bernoulli random variable with a constant ] 

**1594** _Journal of Financial Econometrics_ 

intensity λ _[v]_ 0[: ] _[J] t[v]_[�] _[Bernoulli]_[ð][λ] _[v]_ 0[Þ][. The interpretation of these parameters inherits from the ] continuous-time representation in Section 1.1. 

## **2. Bayesian Inference and Forecasting** 

We now introduce the in-sample estimation method and develop the out-of-sample forecasting framework. A description of the data will be provided at the end of this section. 

## 2.1 In-Sample Estimation 

Following most literature studying stochastic volatility models, we adopt an MCMC to jointly estimate static parameters and latent variables. Denote the static parameter vector as Θ ¼ fμ _;_ μ _p_ þ _;_ σ _p_ þ _;_ μ _p_ − _;_ σ _p_ − _;_ κ _;_ θ _;_ σ _v;_ ρ _;_ μ _v;_ λ _[v]_ 0 _[;]_[ ϑ] _[;]_[ b][g][, and the latent variable vector as ] Z _t_ ¼ f _vt;_ ξ _[p] t_[þ] _[;]_[ ξ] _[p] t_[−] _[;]_[ ξ] _[v] t[;][ J] t[p]_[þ] _[;][ J] t[p]_[−] _[;][ J] t[v]_[g][, the joint posterior distribution is given by: ] 

**==> picture [253 x 10] intentionally omitted <==**

We adopt a hybrid of the Metropolis–Hastings and Gibbs sampling schemes to approximate this posterior distribution. The sampling steps of self/cross-exciting parameters fϑ _;_ bg are given by Rasmussen (2013). A detailed specification of priors and the algorithm is provided in Appendix A.1. 

## 2.2 Out-of-Sample Forecasting and Jump’s Predictability 

Our goal in the out-of-sample is to forecast _p_ ð _Jt[i]_ þ1[¼][ 1][Þ][ or ][λ] _t[i]_ þ1 _[;][i]_[ ¼ f] _[p]_[þ] _[;][ p]_[−][g][ given the in-] formation up to time _t_ . We denote the forecasted values of λ _[i] t_ þ1[as ][λ] _[i] t[;]_ þ _[f]_ 1[. We first fix the ] static parameter vector Θ at its posterior mean estimated in the in-sample period Θ[^] . Then, for every return _yt_ coming in, we adopt a particle filter proposed by Pitt and Shephard (1999) to approximate the distribution of latent variables _p_ � Z _t_ j _yt;_ Θ[^] �. Details of the particle filtering are provided in Appendix A.2. As a result, we will have _N_ particles of Z _t_ from the particle filtering denoted as Z[ð] _t[k]_[Þ] _[;][ k]_[ ¼][ 1] _[;]_[ 2] _[;]_[ . . .] _[ ;][ N]_[. From these estimates, we can approxi-] mate the predictive distribution _p_ � _Jt[i]_ þ1[j] _[y][t][;]_[ ^][Θ] _[;]_[ Z] _t_[ð] _[k]_[Þ] �, which is λ _[i] t[;]_ þ _[f]_ 1[.][3] The predictive probabilities of jumps λ _[i] t[;][f]_[are evaluated by an RPS, which takes the square ] of ðλ _[i] t[;][f]_[−] _[J] t[i]_[Þ][ averaged over time: ] 

**==> picture [235 x 26] intentionally omitted <==**

Our forecasting exercise does not end here. We realize that the evaluation of the predictive probabilities of jumps λ _[i] t[;][f]_[is subjected to the proxy of ] _[J] t[i]_[’s true values.][4 ][In other words, ] one may never know if the forecasts are truly successful due to the unavailability of the true values. Therefore, instead of focusing on jumps in asset returns (which are latent), we focus on asset returns themselves. We introduce a statistic by taking the difference between the predicted probability of positive and negative jumps: 

**==> picture [219 x 12] intentionally omitted <==**

> 3 Note in the calculation of λ _[i] t[;]_ þ _[f]_ 1[, we use the Markov property of the jump intensity process to derive ][λ] _[i] t[;]_ þ _[f]_ 1 from _p_ ð _Jt[i]_[¼][ 1][j] _[v][t][;][ y][t][;]_[ ^][Θ][Þ][, i.e., ][λ] _[i] t_[instead of from all past jumps ] _[J]_ 0 _[i]_ : _t_[. This can significantly speed up the algorithm.] 

> 4 To enable a fair comparison of λ _[i] t[;][f]_[against its benchmarks, we apply a non-parametric estimation on ] _[J] t[i]_[. ] We will introduce details of the estimation and benchmarks in Section 4.1. 

Chen j Jump Clustering and Pricing Efficiency **1595** 

We examine the predictive power of λ _[d] t[;][f]_ on _yt._ The intuition of this statistic is capturing those times when the predicted probability of positive jumps is higher or the predicted probability of negative jumps is higher. Our focus is on how asset returns are distributed during these times. 

Following this logic, λ _[d] t[;][f]_ ¼ λ _[p] t_[þ] _[;][f]_ −λ _[p] t_[−] _[;][f]_ ¼ λ[^] 0 _p_ þ−λ^0 _p_ − most of the time when there are no jumps. It can become extremely high or low when a positive or negative jump is predicted to have a higher probability of being observed at time _t_ . As such, it is important to know where λ _[d] t[;][f]_ lies on its distribution (i.e., left tail or right tail) after we forecast the underlying intensity fλ _[p] t_[þ] _[;][f] ;_ λ _[p] t_[−] _[;][f]_ g and calculate the corresponding λ _[d] t[;][f]_[. For this purpose, we further de-] fine the following two statistics: 

**==> picture [253 x 89] intentionally omitted <==**

_d_ where λ[^] _t_[denotes the in-sample path of ][λ] _t[d]_[. Note we take the MCMC estimates of ][ϑ] _[;]_[ b] _[;][ J] t[i]_[to ] _i d p_ þ _p_ − simulate the underlying intensity λ _[i] t_[denoted as ][λ][^] _t_[. Then ][λ][^] _t_[¼][ ^][λ] _t_[−][λ][^] _t_[. ][F] ^λ _dt_[ð�Þ][ denotes the em-] _d_ pirical cumulative distribution of λ[^] _t_[. For example, letting ] _[q]_[ ¼][ 5][%] _[;]_[F][ −] λ^ _dt_[1] ð2 _:_ 5%Þ denotes the _d 2.5th_ percentile (i.e., the left tail of the λ[^] _t_[’s empirical distribution). Similarly, ][F][ −] λ^ _dt_[1] ð97 _:_ 5%Þ _d_ denotes the _97.5th_ percentile (i.e., the right tail of the λ[^] _t_[’s empirical distribution). We intend to ] use _S_[þ] _t_[and ] _[S]_[−] _t_[to capture those days when the predicted probability of positive jumps ][λ] _t[p]_[þ] _[;][f]_ is higher ( _S_[þ] _t_[¼][ 1) and when the predicted probability of negative jumps ][λ] _t[p]_[−] _[;][f]_ is higher ( _S_[−] _t_[¼][ 1). ] Later in this article, we will utilize _S_[þ] _t_[and ] _[S]_[−] _t_[as signals in a trading strategy.] 

## **3. Empirical Studies** 

## 3.1 Data 

We primarily conduct our empirical studies on US stock data. We also examine the predictability of self-exciting jumps with 24 foreign exchange rates and 12 commodity futures data using the same forecasting framework. These results are confined to a Supplementary Appendix. 

We obtain the daily US stock price data from the Center for Research in Security Prices (CRSP) for the period from 1 January 2000 to 31 December 2021. Companies’ book values data come from Compustat. We split all the stock data into in-sample and out-of-sample on 1 January 2013. We discard data before 1 January 2000 and restrict the stock to have at least 5 years of data in the in-sample to guarantee relevant and sufficient data for the Bayesian MCMC estimation. As a result, we filter out 3035 stock data. 

In the Bayesian MCMC estimation, we set the number of iterations as 100,000, and the first 50,000 iterations are the burn-in period. Note that one could apply the framework with a one-year rolling window (i.e., forecast for one year and recursively re-estimate the model with the past 5 years of data). Due to the heavy computational burden, we choose not to do so, although this would likely lead to better forecast performance. Moreover, our main theme in this section is to study return jumps’ predictability across different assets rather than improve the forecasts. 

**1596** _Journal of Financial Econometrics_ 

To demonstrate the realized behaviors of stock return jump clustering, we first estimate a model setting all jump intensity constant (λ _[i] t_[�][λ] _[i]_ 0 _[;][i]_[ ¼ f] _[p]_[þ] _[;][ p]_[−] _[;][ v]_[g][). Based on posteriors ] of _Jt[p]_[þ] and _Jt[p]_[−][, we discover the following facts:] 

92.17% of stocks exhibit return jumps that occurred on their earnings announcement days at least once. 44.57% of stocks exhibit, at least once, a consecutive jump following the announcement day jump. 71.89% of these consecutive jumps are of the same signs as the previous jumps. 62.05% of stocks have at least one jump within the subsequent four days following the earnings announcements. 

Jumps in stock prices do relate to news releases, as evidenced by earnings announcements, when over 90% of stocks exhibit at least one jump on their announcement days. This observation aligns with existing literature: the jump’s probability is significantly higher during news arrival days (see, e.g., Lee 2012; Bajgrowicz, Scaillet, and Treccani 2016; Jeon, McCurdy, and Zhao 2022; Christensen, Timmermann, and Veliyev 2023). Furthermore, this brief overview illustrates jump clustering behavior, with numerous stocks experiencing multiple jumps following earnings releases. 

## 3.2 Jump Clustering Parameters 

In the in-sample estimation, there is no need to report most of the results (posteriors of static parameters, overall model fitness, etc.) as they are not the main focus of this article. The aim is to study the posteriors of the jump clustering parameters fλ _[i]_ 0 _[;]_[ ϑ] _[i][;][j]_[g][ across differ-] ent assets. We remark that the information decaying speed β _[i][;][j ]_ is contained in ϑ _[i][;][j]_ . In addition, ϑ _[i][;][j ]_ is a 2×2 matrix capturing an expected number of jumps in _i_ that is produced by jumps in _j_ , where _i; j_ 2 f _p_ þ _; p_ −g. A higher decaying speed will lead to a smaller expected number of jumps being produced. It is related to the magnitude of the incremental intensity of jumps raised by past jumps (α _[i][;][j ]_ in the model by Aït-Sahalia, Cacho-Diaz, and Laeven (2015)). Therefore, we focus on fλ _[i]_ 0 _[;]_[ ϑ] _[i][;][j]_[g][ across different assets and ignore the ][β] _[i][;][j]_[.] Figure 2 plots posterior means’ histograms of fλ _[i]_ 0 _[;]_[ ϑ] _[i][;][j]_[g][ estimated using the US stock data ] from 2000 to 2012. The base-line intensities fλ _[p]_ 0[þ] _[;]_[ λ] _[p]_ 0[−][g][, which can also be regarded as the ] base-line probability of jumps, are mostly smaller than 5% representing 13 jumps in a year on average. A higher value of λ _[i]_ 0[leads to a fatter-tailed return distribution. Therefore, this ] can also be an indicator of stock jump risk, which has been extensively studied in the literature (e.g., B�egin, Dorion, and Gauthier 2020). Regarding the ϑ _[i][;][j]_ , all four histograms exhibit evident tails, indicating that some stocks demonstrate pronounced jump clustering behaviors. However, in these four histograms, ϑ _[p]_[−] _[;][p]_[þ] and ϑ _[p]_[þ] _[;][p]_[− ] are closer to zero compared to ϑ _[p]_[þ] _[;][p]_[þ] and ϑ _[p]_[−] _[;][p]_[−] , suggesting that the cross-impact of return jumps tends to be weaker than their self-excitation. Moreover, the cross-impact of return jumps could also be captured by variance jumps and variance persistence. The matrix estimated by averaging 0 _:_ 0261 0 _:_ 0125 over all stocks is .[5 ] As an arbitrary measure of parameter significance, 0 _:_ 0094 0 _:_ 0286 � � we calculate the percentage of stocks for which the posterior means of their parameters minus 1.5 times their posterior standard deviations are greater than zero. The percentage of 33 _:_ 4% 13 _:_ 7% these four parameters is . However, we emphasize that the significance � 9 _:_ 6% 37 _:_ 7% � of these parameters is less likely to influence our subsequent studies. 

> 5 The matrix represents the posterior mean of ϑ, i.e., ϑ _[p]_[þ] _[;][p]_[þ] ϑ _[p]_[þ] _[;][p]_[−] . � ϑ _[p]_[−] _[;][p]_[þ] ϑ _[p]_[−] _[;][p]_[−] � 

Chen j Jump Clustering and Pricing Efficiency **1597** 

**Figure 2.** Histograms of jump clustering parameters. 

_Notes_ : These parameters are estimated using the US stock data from 1 January 2000 to 31 December 2012. We only include companies with data for more than 5 years, which results in 3035 stocks being filtered out. The jump clustering parameters for the 3035 stocks are shown by these histograms. 

## 3.3 Characteristics of Stocks with Heavily Clustered Jumps 

We have demonstrated that different assets exhibit jump clustering to varying extents indicated by jump clustering parameters. It is reasonable to ask what types of assets exhibit more pronounced self/cross-exciting jump behavior and what properties they share. To further analyze different extent of jump clustering across different assets, we define f ¼[P] ϑ _[i][;][i]_ , where ϑ _[i][;][i ]_ denotes the diagonal elements of matrix ϑ. Therefore, f is simply the sum of diagonal elements in matrix ϑ. We intend to use this measure to quantify the extent to which an asset’s jumps are clustering, particularly those clustered jumps of the same sign. 

We follow various traditional asset pricing papers by sorting all stocks by f and forming 10 portfolios. We calculate characteristics averaged over stocks in each portfolio: market cap, book-to-market ratio, illiquidity ratio, stock market beta, idiosyncratic volatility, total volatility, and out-of-sample annualized mean return. 

The table shows a clear trend across several firm characteristics. The stocks with heavier-clustered jumps are more likely associated with small market caps, higher book-tomarket ratios, less trading liquidity, less sensitivity to the market factor, and higher volatility. The out-of-sample returns suggest that f is potentially a pricing factor and plays a role in return prediction. But we will refrain from this viewpoint any further since it is not the focus of this article. In this section, our goal is to provide a broad overview of the characteristics of stocks whose jumps are heavily clustered. We will include the possibility of this point in future studies. 

## 3.4 “Idiosyncratic” Stock Price Efficiency _vs._ Price Delays 

The f we proposed to measure the extent of jump clustering may also serve as a measurement of stock price efficiency. For example, if a stock requires a sequence of price jumps to absorb new information, it is potentially less efficient than a stock that only reacts with a single jump to the same information. Assuming that new information arrives randomly and that a completely efficient stock only displays one jump in response to the information, the 

**1598** _Journal of Financial Econometrics_ 

stock price jumps should likewise arrive randomly and independently of one another. In this sense, there is no jump clustering, and f of the stock will be close to zero. 

The most commonly used stock price efficiency measure in the literature is the price delays proposed by Hou and Moskowitz (2005). It uses the predictive power of market returns on individual stock returns to measure the stock price efficiency. First, it regresses the stock’s weekly returns _y[w] t_[on the market weekly returns ] _[y] t[w][;][mkt]_ along with four weeks of its lagged returns: 

**==> picture [254 x 26] intentionally omitted <==**

Then the stock price efficiency is derived as: 

**==> picture [259 x 27] intentionally omitted <==**

where _s:e:_ ð�Þ denotes the standard error of the regression coefficient estimates. An alternative measure in this article is _D_ 2: 

**==> picture [235 x 13] intentionally omitted <==**

In addition, Bris, Goetzmann, and Zhu (2007) propose to use ρ _[cross ]_ as a measurement of efficiency. It is the first order autocorrelation of stock returns with lagged market returns (ρ ¼ _corr_ ð _yt; y[mkt] t_ −1[Þ][. Since the correlation is bounded by ][−][1 and 1, we apply the ] transformation: 

**==> picture [222 x 23] intentionally omitted <==**

These measures show some power in capturing PEAD (see Figure 1 in Hou and Moskowitz (2005)’s paper), although they are designed to measure stock delays in possessing market information instead of _idiosyncratic_ information (e.g., earnings releases). The f, on the other hand, captures the speed of possessing information regardless of whether it is macro or _idiosyncratic_ information. 

To compare among different measures of stock price efficiency, we generate the commonly used plot of CAR from 5 days before to 15 days after the earnings announcements. CAR is the buy-and-hold market-adjusted return, calculated as follows: 

**==> picture [293 x 29] intentionally omitted <==**

where the β _mkt_ is the β estimated from the market model. We double-sort CAR by standardized unexpected earnings (SUE) and price efficiency measures in Figure 3. Note that SUE is used in literature (e.g., Chan, Jegadeesh, and Lakonishok 1996) to capture PEAD. The unexpected earnings are calculated by current earnings minus earnings four quarters ago ( _et_ − _et_ −4). The SUE equals the mean of unexpected earnings over its standard deviation. We include the D1 and D2 measures from Hou and Moskowitz (2005), the ρ _[cross ]_ proposed by Bris, Goetzmann, and Zhu (2007). In Figure 3, we can see these measures’ ability to categorize stocks exhibiting different levels of PEAD. The portfolios of stocks with high values 

Chen j Jump Clustering and Pricing Efficiency **1599** 

**Figure 3.** CAR double-sorted by SUE and pricing efficiency measures. _Notes_ : Earnings news is measured using SUE. We first categorize stocks into those with positive SUE (blue) and negative SUE (green). Stocks are sorted independently into quintiles based on the magnitude of SUE. Then, we sort stocks into quintile portfolios based on pricing efficiency measures so that each quintile contains stocks with different magnitudes of SUE but the same level of pricing efficiency. High and Low denotes the quintile portfolio with the highest and lowest pricing efficiency measures. 

of pricing efficiency measures (solid blue and green lines) report the largest drifts after the announcement dates. 

However, Figure 3 can be misleading if one wants to know which measure best portrays the stock price efficiency by looking at the PEAD since stocks already have different extents of drifts before the announcement, although drifts before the announcements are also valuable in several studies (see, e.g., Liu et al. 2020). Thus, we further plot Figure 4 with jCARj double-sorted _by_ jSUEj and price efficiency measures starting from the announcement dates. Note that we take CAR’s and SUE’s absolute values since their directions are insignificant in measuring price efficiency, and we care more about the magnitudes of CAR and SUE. We assume that after controlling the SUE, stocks with very high price efficiency can quickly possess the information and display modest CAR magnitudes, regardless of whether the information will lead to a positive or negative CAR. Similar to Table 1, we summarize price efficiency and PEAD measures of f-sorted portfolios in Table 2. 

Consequently, if the price efficiency measure is effective, its figure should distinctly display the PEAD magnitudes of 10 separate portfolio orders. This relates to how f and ρ _[cross ]_ perform better than D1 and D2 in demonstrating this effect. To further investigate which measure can better explain the cross-sectional variation of PEAD, we run the following regression: 

**==> picture [308 x 12] intentionally omitted <==**

where _s_ ¼ 1 _;_ 2 _;_ . . . _; S_ is the index for _S_ ¼ 3035 different stocks we considered. jCAR _s_ ½ _t_ 1 _; t_ 2 denotes the absolute value of CAR from _t1_ to _t2._ **x** _s_ denotes control variables including market beta, idiosyncratic volatility, log market cap, book-to-market ratio, and the Amihud illiquidity ratio (Amihud 2002). We present the regression results in Table 3. 

**1600** _Journal of Financial Econometrics_ 

**Figure 4.** CAR double-sorted by jSUEj and pricing efficiency measures. _Notes_ : These four figures are similar to Figure 3, however, we make two adjustments. First, we double-sort stocks to 10 decile portfolios by j SUE j and pricing efficiency measures without differentiating between positive and negative SUE. Second, we move the starting point of CAR to day 0. 

**Table 1.** f-Sorted portfolio characteristics 

|**Decile**<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|f<br>0.021<br>0.028<br>0.033<br>0.037<br>0.041<br>0.047<br>0.054<br>0.065<br>0.083<br>0.139|**_mkt cap_($108)**<br>6.80<br>6.52<br>6.45<br>6.48<br>6.64<br>6.33<br>6.21<br>5.83<br>5.66<br>5.61|**_b/m_**<br>0.74<br>0.71<br>0.75<br>0.72<br>0.69<br>0.76<br>0.73<br>0.76<br>0.83<br>0.95|**_illiquidity_(104)**<br>2.17<br>1.54<br>2.64<br>3.50<br>2.31<br>4.20<br>4.29<br>6.42<br>6.51<br>15.06|β_mkt_<br>1.02<br>0.98<br>0.92<br>0.95<br>0.92<br>0.85<br>0.85<br>0.79<br>0.76<br>0.71|**_ivol_(**%**)**<br>2.69<br>2.85<br>2.98<br>3.07<br>3.01<br>3.16<br>3.46<br>3.67<br>4.11<br>4.56|**_vol_(**%**)**<br>3.20<br>3.32<br>3.40<br>3.50<br>3.42<br>3.52<br>3.80<br>3.98<br>4.40<br>4.83|**yt**ð_oos_Þ**(**%**)**<br>15.2<br>17.6<br>18.4<br>18.9<br>18.6<br>18.9<br>17.4<br>18.3<br>19.9<br>21.0|
|---|---|---|---|---|---|---|---|---|



_Notes:_ We sort the stock data to 10 portfolios by f and calculate the means of stock’s characteristics in each portfolio. The return in the last column is annualized ( * 252). 

Table 3 shows that D1 and D2 are only statistically significant in the absence of control variables. They lose significance when several firm-specific factors are taken into account. ρ _[cross ]_ performs marginally better with a significant coefficient when explaining jCAR[0,1]j and jCAR[0,3]j. However, our measure f consistently reports significant coefficients across all jCARj after earnings announcements. This finding suggests that stock cross-correlation with lagged market returns and price delays may not accurately reflect how quickly a stock assimilates firm-specific information, such as a firm’s quarterly earnings releases. 

More importantly, the regression results also suggest that our measure, f, encompasses information beyond that of illiquidity, despite the tight correlation between the jump clustering and illiquidity characteristics. Although illiquid stocks are intuitively less efficient and take longer to absorb new information, leading to more pronounced jump clustering behaviors, regression coefficients of f remain significant when controlling for the illiquidity measure, while others become insignificant. 

Chen j Jump Clustering and Pricing Efficiency **1601** 

**Table 2.** f-Sorted portfolio pricing efficiency and PEAD measures 

|**Decile**|f|**D1**|**D2**|ρ_cross_|**SUE**|**CAR[0,1] (**%**) **|**CAR[0,3] (**%**) **|**CAR[0,5] (**%**) **|**CAR[0,10] (**%**)**|
|---|---|---|---|---|---|---|---|---|---|
|1|0.021|0.595|0.07|−0.059|0.308|0.00|0.03|0.09|0.15|
|2|0.028|0.651|0.07|−0.038|0.263|−0.04|−0.08|−0.07|−0.02|
|3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|0.033 <br>0.037 <br>0.041 <br>0.047 <br>0.054 <br>0.065 <br>0.083 <br>0.139|0.678 <br> 0.654 <br> 0.647 <br> 0.715 <br> 0.784 <br> 0.819 <br> 0.880 <br> 0.985|0.09 <br> 0.08 <br> 0.08 <br> 0.10 <br> 0.12<br> 0.14<br> 0.16<br> 0.22|−0.010 <br> −0.017 <br> −0.032 <br> −0.007 <br>0.012 <br>0.016 <br>0.018 <br>0.049|0.257<br> 0.232<br> 0.260<br> 0.226<br> 0.190<br> 0.184<br> 0.210<br> 0.194|−0.16<br>−0.18<br>−0.12<br>−0.20<br>−0.25<br>−0.53<br>−0.51<br>−0.58|−0.32<br>−0.42<br>−0.22<br>−0.39<br>−0.46<br>−0.79<br>−0.82<br>−0.90|−0.36<br>−0.43<br>−0.22<br>−0.36<br>−0.47<br>−0.83<br>−0.97<br>−0.91|−0.46<br>−0.43<br>−0.11<br>−0.40<br>−0.54<br>−1.00<br>−0.98<br>−1.03|



_Notes:_ We sort the stock data to 10 portfolios by f and calculate the means of stock’s price efficiency measures and CAR in each portfolio. 

We also sort the stocks by f, D1, D2, and ρ _[cross ]_ to 10 deciles and plot the incremental 1 _p_ þ _p_ − − 1 _p_ þ _p_ − probability of jumps, 2 �[λ][^] _t_[þ][λ][^] _t_ � 2 �[λ][^] _t_ −1[þ][λ][^] _t_ −1�, before and after earnings announcements averaged over decile stocks in Figure 5. 

The figure plots the changes in the jump’s probability before and after earnings announcements. Based on the results of the first decile stocks sorted by f (dark blue line in the upper left figure), the jump intensity increases only slightly after the earnings announcement dates. More importantly, it starts to decline immediately after that. The f figure displays distinct patterns of portfolio orders, while none of the other three measures can recover this pattern. However, the probability of jumps differs greatly from the PEAD. A substantial drift pattern following announcements does not necessarily indicate an increase in the probability of jumps. This may help to explain why D1 and D2 perform some tasks in sorting stocks with different CAR magnitudes but fail to do so when dealing with jump probabilities. 

One can collect different news stories and compare jCARj across assets after each type of news release. This can directly measure the incorporation speed of one specific type of news, but it requires prior information on news timeliness. Thus, we emphasize the convenience and generality of adopting f as a measurement of stock price efficiency. Only asset returns must be known, and the timeliness of news is unnecessary. The model will determine whether jumps are present in the returns and whether they show clustering. 

## 3.5 Jump’s Intensity Surrounding News Releases 

As a supplementary illustration, we also investigate the dynamics of the jump’s intensity around news releases. 

It has been well-established in the literature that stock price jumps are primarily driven by new information at both the macro level (Lee 2012) and the firm-specific level (Savor 2012; Bradley et al. 2014). However, there are very few formal investigations into when return jumps exhibit self/cross-excitation. Some literature provides possible directions on this topic. For example, the market may over- and under-react to the new information (Savor 2012; Jiang and Zhu 2017); stocks can vary depending on how quickly news is incorporated (Da, Gurun, and Warachka 2014; Tao, Brooks, and Bell 2021). Stocks with low pricing efficiency are predictable in the short run (Chordia, Roll, and Subrahmanyam 2008). These studies offer possible explanations for the clustering of more than two return jumps. It is not surprising to see another jump in a short period of time if the initial jump does not 

_Journal of Financial Econometrics_ 

**1602** 

|j_CAR_½−**2**_;_**0**�j<br>j_CAR_½−**1**_;_**0**�j<br>j**CAR[0,1]**j<br>j**CAR[0,3]**j<br>j**CAR[0,5]**j<br>j**CAR[0,10]**j|f<br>0.035<br>−0.013<br>0.662<br>���<br>0.292<br>���<br>1.101<br>���<br>0.363<br>���<br>1.345<br>���<br>0.4<br>��<br>2.741<br>���<br>0.845<br>���<br>(1.03)<br>(−0.15)<br>(7.89)<br>(3.76)<br>(7.72)<br>(2.8)<br>(7.44)<br>(2.46)<br>(8.92)<br>(3.16)<br>ρ_cross_<br>0.019<br>0.024<br>0.593<br>���<br>0.103<br>�<br>1.065<br>���<br>0.163<br>�<br>1.402<br>���<br>0.159<br>2.272<br>���<br>0.075<br>(0.24)<br>(0.4)<br>(9.99)<br>(1.81)<br>(10.55)<br>(1.71)<br>(10.97)<br>(1.33)<br>(10.45)<br>(0.38)<br>D2<br>−0.083<br>−0.013<br>−0.703<br>���<br>0.041<br>−0.559<br>�<br>−0.035<br>−0.668<br>��<br>−0.086<br>−0.576<br>�<br>−0.032<br>(−1.59)<br>(−0.33)<br>(−3.02)<br>(1.11)<br>(−1.87)<br>(−0.56)<br>(−2.01)<br>(−1.11)<br>(−1.7)<br>(−0.25)<br>D1<br>0.034<br>�<br>0.022<br>0.319<br>���<br>0.001<br>0.476<br>���<br>0.01<br>0.575<br>���<br>−0.02<br>0.743<br>���<br>−0.035<br>(1.82)<br>(1.59)<br>(3.72)<br>(0.05)<br>(4.33)<br>(0.43)<br>(4.71)<br>(−0.72)<br>(5.24)<br>(−0.76)<br>β_mkt_<br>0.065<br>���<br>0.04<br>���<br>0.024<br>��<br>−0.005<br>−0.032<br>−0.137<br>���<br>(4.72)<br>(3.9)<br>(2.49)<br>(−0.33)<br>(−1.54)<br>(−4.05)<br>_ivol_<br>0.064<br>���<br>0.051<br>���<br>0.059<br>���<br>0.112<br>���<br>0.146<br>���<br>0.288<br>���<br>(17.47)<br>(18.62)<br>(22.49)<br>(25.53)<br>(26.44)<br>(31.81)<br>_mkt cap_<br>−0.013<br>���<br>−0.007<br>��<br>0.001<br>0.005<br>0<br>0.033<br>���<br>(−3.75)<br>(−2.55)<br>(0.21)<br>(1.2)<br>(−0.03)<br>(3.72)<br>_b/m_<br>−0.009<br>0<br>−0.006<br>−0.017<br>��<br>−0.008<br>−0.004<br>(−1.27)<br>(−0.07)<br>(−1.11)<br>(−2.01)<br>(−0.74)<br>(−0.2)<br>_illiquidity_<br>−0.912<br>���<br>−0.465<br>���<br>0.05<br>−1.049<br>���<br>−2.731<br>���<br>−6.417<br>���<br>(−3.94)<br>(−2.69)<br>(0.31)<br>(−3.82)<br>(−7.92)<br>(−11.32)<br>Constant<br>0.052<br>0.021<br>0.146<br>���<br>−0.042<br>�<br>0.25<br>���<br>−0.08<br>��<br>0.339<br>���<br>−0.028<br>0.525<br>���<br>−0.37<br>���<br>(1.62)<br>(0.87)<br>(16.7)<br>(−1.87)<br>(16.79)<br>(−2.11)<br>(17.98)<br>(−0.6)<br>(16.37)<br>(−4.75)<br>_R_2(%)<br>20.6<br>21.2<br>9.6<br>28.6<br>8.6<br>29.9<br>7.8<br>30.4<br>8.7<br>35.6|_Notes:_This table presents the results of regressionEquation (18).j_CARi_½_t_1_; t_2�jdenotes the absolute value of stock i’s CAR from_t_1_tot_2. Note the i is compressed for brevity.<br>���,��, and�indicate statistical signifcance at the 1%, 5%, and 10% levels, respectively.<br>Downloaded from https://academic.oup.com/jfec/article/22/5/1588/7658908 by Eastman Dental Institute user on 20 May 2026|
|---|---|---|



Chen j Jump Clustering and Pricing Efficiency **1603** 

**Figure 5.** Changes in probability of jumps around earnings announcements. 

_Notes_ : These figures present the first difference in the jump’s probability, 12[λ][^] _pt_ þ[þ][^][λ] _pt_ − − 12[^][λ] _pt_ −þ1[þ][^][λ] _pt_ −−1[. We sort ] stocks into 10 deciles using different price efficiency measures. Then, we calculate changes in the jump’s probability averaged over decile stocks. We mark the point in the upper left figure with to emphasize that it is negative and * that jump’s probability starts to decline from the second day of earnings announcements. 

fully absorb the new information because of the market’s under-reaction or low pricing efficiency. 

_i_ The model-estimated underlying intensity λ[^] _t_[becomes a good object to examine the jump ] _i i_ clustering and information arrivals. Note that λ[^] _t_[is estimated to be equal to ][λ][^] 0[during the ] _i_ peaceful time. When a jump arriving at time _t_ , λ[^] _t_ þ1[will be raised by the jump. If another jump ] is observed before λ[^] _it_[decays back to ][λ][^] _i_ 0 _[;]_[λ][^] _it_[will become even higher; these two jumps form a ] _i_ cluster. Therefore, we can investigate λ[^] _t_[’s dynamics surrounding news announcements. ] Assuming a news announcement with a return jump occurs on date _t_ , we should see an increase in the intensity at _t_ þ 1, which will then begin to decline over the next few days. However, if a jump clustering exists due to the low incorporation speed of news or under/over-reactions to the news, and a new jump is generated, we will see another increase in the intensity after _t_ þ 1. 

We form the following panel regression model,[6 ] to study the dynamics of the underlying intensity of jumps: 

**==> picture [278 x 26] intentionally omitted <==**

where λ[~] _t_ ¼ 12[λ] _t[p]_[þ][þ][λ] _[p] t_[−][Þ][. ] **[w]** _t_[denotes a set of control variables: log market cap, book-to- ] market ratio, illiquidity ratio (Amihud 2002) and idiosyncratic volatility.[7 ] f _M_[1] _t[;]_[τ] _[;][M]_[2] _t[;]_[τ] _[;][M]_[3] _t[;]_[τ] _[;][F]_[1] _t[;]_[τ] _[;][F] t_[2] _[;]_[τ][g][ are dummy variables that equal one around trading days when ] the information from various news stories can be reflected in the stock prices. The τ in the 

> 6 Note that the regression is for all stock data; however, we suppress the notation specific to individual stocks for simplicity. For example, 7 We regress the stock returns with Fama–French three factors. The stock market beta is the coefficient esti-λ _[p] t_[þ] should be λ _[p] s;_[þ] _t_[, representing ][λ] _[p] t_[þ] of stock _s_ and ‘ _s_ ’ is suppressed. mate of the market factor, and the idiosyncratic volatility is the standard deviation of the estimated regression residuals. 

**1604** _Journal of Financial Econometrics_ 

time index is relative to the announcement dates. For example, _M_[1] _t[;]_[τ][¼][−][1] denotes the day before the announcements ( _M_[1] _t[;]_[τ][¼][0] ); _M_[1] _t[;]_[τ][¼][2] denotes two days after the announcements. We only consider Ψ ¼ f−1 _;_ 0 _;_ 1 _;_ 2 _;_ 3 : 5g to avoid too many variables in the regression. The five news announcements we consider are listed as follows: 

|_Macro-level_<br>_Firm-specifc_|_M_1_;_τ¼0<br>_t_<br>_M_2_;_τ¼0<br>_t_<br>_M_3_;_τ¼0<br>_t_<br>_F_1_;_τ¼0<br>_t_<br>: <br>_F_2_;_τ¼0<br>_t_<br>:|:Federal Open Market Committee (FOMC) news releases<br>:Nonfarm payroll employment report releases<br>:Unemployment rate releases<br>Earnings announcements<br>Dividend declarations|
|---|---|---|



Instead of reporting the long table of regression results, we plot the coefficient estimates in Figure 6. The full regression results are provided in Appendix A.4. We also provide some complementary results regarding this regression exercise in the Supplementary Appendix. The coefficient estimates for the macro-level and firm-specific news announcements are plotted on the left and right sides of Figure 6. 

One must remember that under our model setting, an intensity increase at time _t_ is caused by the jump that occurred at time _t−_ 1. However, looking at the left-side figure, the intensity increases on all three macro-announcement dates (τ ¼ 0), suggesting that there are jumps one day before the announcement. Regarding the earnings announcements, the first increase in intensity is the day after the announcements (τ ¼ 1), which shows evidence of jumps immediately after the earnings announcements. These results are consistent with three streams of literature: (1) jumps are closely related to the information releases (Lee 2012; Bajgrowicz, Scaillet, and Treccani 2016); (2) the information leakage of macro-news leads to pre-announcement drifts (Bernile, Hu, and Tang 2016; Kurov et al. 2019); (3) there are PEAD across assets (Bernard and Thomas 1989; Hung, Li, and Wang 2015). However, we are the first to aggregate these effects and explain them in terms of the probability of return jumps and their self-excitation. 

Note that two subsequent increases in jumps’ intensities are evidence of their selfexcitation. For example, the intensity increases on the day after the earnings announcements (τ ¼ 1), indicating the existence of jumps on the announcement dates (τ ¼ 0). It increases to a higher level on day two (τ ¼ 2), suggesting subsequent jumps on day one (τ ¼ 1), which create self-excitation of jumps and jump clustering. In other words, if a return series exhibits jumps at some specific dates but does not show jump clustering, the underlying intensity would not increase twice. Instead, it would increase once due to the first jump and then begin to decline. This can be caused by the fast information-incorporation speed of this information, which does not require a second jump to absorb the information. 

We also remark that the coefficients on the earnings announcements are around 10 times greater than those on macro-announcements. This suggests that earnings announcements are when most jump clusterings occur (rather than during the releases of macro information). 

## **4. Forecasting Performance** 

Another goal of this article is to examine whether jump clustering behaviors translate to the predictability of jumps and returns. We employ the forecasting framework outlined in Section 2.2 and conduct the out-of-sample forecasting. To facilitate the presentation of forecasting results, we continue to sort all US stocks by f estimated in the in-sample period and form 10 portfolios to evaluate their out-of-sample performance. 

Chen j Jump Clustering and Pricing Efficiency **1605** 

H 1 \ \ °|— 

**Figure 6.** Coefficient estimates of regression on news announcements. 

_Notes_ : These two figures show the coefficient estimates of the regression Equation (19). We mark the coefficient estimates with when they are significantly different from zero under a 5% significance level. The full regression * results are provided in the Supplementary Appendix. 

## 4.1 RPS 

The first out-of-sample exercise involves forecasting jumps’ probability (i.e., underlying intensity). We compare the RPS (see Equation (9) for the its calculation) from our forecasting methods with two benchmarks denoted as M _b;_ 1 and M _b;_ 2. M _b;_ 1 assumes jumps arrive independently. We reestimate the model with constant jump intensities λ _[p]_ 0[þ][and ][λ] _[p]_ 0[−][. In ][M] _[b][;]_[1][, we let ][λ] _t[p]_[þ] _[;][f]_ λ _[p]_ 0[þ][and ] λ _[p] t_[−] _[;][f]_ λ _[p]_ 0[−][. In ][M] _[b][;]_[2][, we assume there are no jumps in the price process. Thus, ] λ _[p] t_[þ] _[;][f]_ λ _[p] t_[−] _[;][f]_ 0. To enable a fair comparison, we adopt a non-parametric jump filtering method to estimate _Jt[i]_[as a proxy of jumps’ true values (see details in ][Appendix A.3][). We also apply a ] Diebold-Mariano (DM) Test[8 ] (Diebold and Mariano 2002) to determine whether the RPS from our model is superior to others. 

Table 4 reports the RPS of 10 deciles of f-sorted portfolios. The percentage in the table represents the proportion of stocks in each decile with RPSs lower than those of the benchmark. The value in brackets indicates the percentage of the portfolio’s stocks with _p_ -values less than 0.05 in the Diebold–Mariano (DM) test. For example, the entry in the last row’s third column, 38.4% (18.9%) indicates that 38.4% of stocks in the decile present smaller as having significantly lower RPS according to DM tests.RPSs, indicating superior forecasts against M _b;_ 1. Moreover, 18.9% of stocks are identified 

The tenth decile reporting the best performance, which is not surprising given its strongest jump clustering behaviors. We also recognize that the choice of true jump’s proxy and non-parametric jump filtering techniques may affect the outcomes. Additionally, it is less economically meaningful if one can only predict the probability of return jumps. Therefore, we would not extend the length of the article by reporting on extra results using alternative proxies and filtering methods. Instead, we focus on a more realistic evaluation of the forecasting framework—return predictions. 

## 4.2 _**λ**[d] t_[and Return Predictions] 

We estimate the ^ _d p_ þ _p_ − λ _[p] t_[þ] and λ _[p] t_[−] in the in-sample, and retrieve the empirical distribution λ _t_[¼][ ^][λ] _t_[−][λ][^] _t_[. In the out-of-sample, we forecast underlying intensities ][λ] _t[p]_[þ] _[;][f]_ and λ _[p] t_[−] _[;][f]_ 

8 Denote two series of probability score (fi fi fi fi fi fi fi fi fi fi fi fi fi fi fi f _s_[1] _t_ i fi fi[and ] **f** _[s]_[2] _t_[) from two different models. We calculate Diebold– ] Mariano statistic as DM ¼ _=_ qðγ0þ2[P] _[h] k_[−] ¼[1] 1[γ] _k_[Þ] _[=][n]_ , where ¼ **E** ð _s_[1] _t_[−] _[s]_[2] _t_[Þ][ and ][γ] _k_[denotes the autocovariance of ] 1 _s_[1] _t_[−] _[s]_[2] _t_[at lag ] _[k]_[. ] _[n ]_[denotes the number of forecasts, and we take ] _[h]_[ ¼] ~~_[n]_~~ 3þ1. 

**1606** _Journal of Financial Econometrics_ 

**Table 4.** RPS of f-sorted stock portfolios against two benchmarks 

||||λ**p**þ_;_**f**<br>**t**|||λ**p**−_;_**f**<br>**t**||
|---|---|---|---|---|---|---|---|
|**_No_**|f|M**b**_;_**1**||M**b**_;_**2**|M**b**_;_**1**||M**b**_;_**2**|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|0.021<br>0.028<br>0.033<br>0.037<br>0.041<br>0.047<br>0.054<br>0.065<br>0.083<br>0.139|20.2% (5%)<br>22.7% (7.1%)<br>26.2% (8.2%)<br>25.9% (7.4%)<br>20.9% (7.4%)<br>21.3% (5.7%)<br>25.5% (9.6%)<br>25.9% (9.9%)<br>37.6% (15.2%)<br>34.2% (14.6%)||1.4% (0%)<br>2.1% (0%)<br>4.6% (1.1%)<br>2.8% (0.7%)<br>3.5% (2.1%)<br>6.4% (3.5%)<br>10.3% (7.8%)<br>17.4% (13.8%)<br>18.8% (14.2%)<br>28% (21.3%)|1.8% (0%)<br>2.8% (0%)<br>3.9% (1.2%)<br>2.5% (0.3%)<br>3.2% (1.4%)<br>4.6% (2.1%)<br>5% (3.7%)<br>10.5% (9.8%)<br>16.1% (13.1%)<br>25.2% (18.8%)||0% (0%)<br>0% (0%)<br>0.8% (0.8%)<br>0.8% (0.8%)<br>3.1% (3.1%)<br>5.8% (5.8%)<br>17.9% (17.5%)<br>23% (23%)<br>31.9% (30.7%)<br>34.6% (30.4%)|



_Notes:_ This table presents the proportion of stocks in the decile with smaller-than-benchmark RPSs. The value in the bracket presents the percentage of the portfolio’s stocks having p-values less than 0.05 in the DM test. M _b;_ 1 is the benchmark that assumes jumps arrive independently with constant jump intensities λ _[p]_ 0[þ] and λ _[p]_ 0[−][. ] In M _b;_ 1 (λ _[p] t_[þ] _[;][f]_ λ _[p]_ 0[þ] _[;]_[λ] _[p] t_[−] _[;][f]_ λ _[p]_ 0[−][). ][M] _[b][;]_[2 ][assumes there are no jumps in the price process (][λ] _t[p]_[þ] _[;][f]_ λ _[p] t_[−] _[;][f]_ 0). 

**Figure 7.** λ _[d] t_[Histograms. ] _Notes_ : These figures show the empirical distribution of λ t d. The data period used in the estimation is from 1 January 2000 to 31 December 2012. The 2.5th and 97.5th percentiles are marked with red dash lines. 

iteratively and collect returns when ^ _d_ λ _[d] t[;][f]_ ¼ λ _[p] t_[þ] _[;][f]_ −λ _[p] t_[−] _[;][f]_ enters tails of the empirical distribution _d_ λ _t_[. The rules are defined in ][Equations (11) ][and ][(12)][. We plot ][λ][^] _t_[’s histograms of select well- ] known stocks in Figure 7. We also mark the 2.5th and 97.5th percentiles with red dash lines. It is of interest to study how asset returns are distributed on these two tails, that is, when the predicted probability of positive jumps λ _[p] t_[þ] _[;][f]_ is higher ( _S_[þ] _t_[¼][ 1) and when the predicted probabil-] ity of negative jumps λ _[p] t_[−] _[;][f]_ is higher ( _S_[−] _t_[¼][ 1). We introduce the following regression analysis: ] 

**==> picture [233 x 11] intentionally omitted <==**

which regresses asset returns with _S_[þ] _t_[and ] _[S]_[−] _t_[. Significant coefficients ][f] _[b]_[1] _[;][ b]_[2][g][can indicate ] the predictive power of _S_[þ] _t_[and ] _[S]_[−] _t_[on asset returns. Insignificant ][f] _[b]_[1] _[;][ b]_[2][g][suggest that ] 

Chen j Jump Clustering and Pricing Efficiency **1607** 

**Table 5.** F-statistics results summary 

|**No**|f|**_F_-stat**|%**of****_p_-value**_<_|**5**%|**St**%|
|---|---|---|---|---|---|
|1|0.0208|1.20|11.0||0.35|
|2|0.0280|2.65|24.8||0.74|
|3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|0.0327<br>0.0369<br>0.0414<br>0.0470<br>0.0545<br>0.0653<br>0.0831<br>0.1388|1.82<br>2.26<br>3.22<br>3.17<br>3.18<br>4.59<br>3.92<br>5.42|30.4<br>41.8<br>52.5<br>53.5<br>48.6<br>48.9<br>61.8<br>73.6||1.14<br>1.20<br>1.40<br>1.76<br>2.27<br>3.88<br>2.95<br>5.81|



_Notes:_ We run the regression Equation (20) for each stock individually and collect the regression’s F-statistics testing on all coefficients being equal to 0. Then, we sort stocks by f and calculate the average F-statistics of stocks in each decile. The fourth column presents the percentage of the F-test’s p-values that are smaller than 5% in the decile. The last column presents the average percentage of _S_[þ] _t_ and _S_[−] _t_[that equal 1 out of the total number of observations.] 

whether λ _[d] t[;][f]_ that lies on the tails of its distribution is less relevant. Therefore, we focus the _F-statistics_ under the _null_ that _b_ 1 ¼ _b_ 2 ¼ 0. We examine the _F-statistics_ of different assets as a measurement of λ _[d] t[;][f]_[’s predictive power, which can also be considered a gauge of jump ] predictability. For example, if jumps exhibit minimal self/cross-excitation (indicating independent arrival) and are unpredictable, the tails of λ _[d] t[;][f]_ will not provide any predictive power on returns. We also remark that the regression model is valid since _S_[þ] _t_[and ] _[S]_[−] _t_[are de-] rived from λ _[d] t[;][f]_[, which is forecasted based on information up to time ] _[t][−]_[1.] 

We run the regression for each individual asset, and the results are summarized in Table 5. Instead of presenting all the coefficient estimates, we summarize the _F-statistics_ testing on all coefficients that are equal to 0. We also summarize the percentage of corresponding _p-values_ that are smaller than 5% in the decile and the ð[P] _S_[þ] _t_[þ][ P] _[ S]_[−] _t_[Þ] _[=][N ]_[in the ] last two columns, where _N_ is the total number of observations. Essentially, the _St_ % is counting the percentage of returns whose λ _[d] t_[is predicted to enter the tails of ][λ] _[d] t_[’s empirical ] distribution. The _F-stat_ indicates an increasing trend with the rise of f. The decile also has more significant F-tests with higher f. 

We also perform a regression on _F_ -statistics with f and some other measures. Table 6 presents the regression results. The results show that the degree of jump clustering f does transfer to the out-of-sample predictive power and that stocks with higher f are more predictable by our forecasting framework. 

## 4.3 Trading on Jump Clustering 

Another more straightforward way to assess the forecasting framework is by developing a trading strategy. The _S_[þ] _t_[and ] _[S]_[−] _t_[can naturally serve as long and short trading signals, re-] spectively. Specifically, we take a long position in the asset when the probability of positive jumps is predicted to be higher, and take a short position when the probability of negative jumps is predicted to be higher. Similarly, we report the performance of the f-sorted portfolio. The results are reported in Table 7. In addition to the trading strategy, we also report the result of a buy-and-hold portfolio in the same decile for comparison. We calculate each strategy’s SR using its average excess return divided by its standard deviation ( _SR_ ¼ ð _yt_ − _rf_ Þ _=_ σ _yt_ ), where _rf_ denotes the risk-free rate. We use the US 10-year treasury note rate as a proxy of the risk-free rate. We also plot their cumulative log returns in Figure 8. Stocks with higher f report better performance, and the SR of the stock’s portfolio can reach as high as 2.60. 

_Journal of Financial Econometrics_ 

**1608** 

**Table 6.** F-statistics cross-sectional regression 

||**_F_-stat**|**_F_-stat**|**_F_-stat**|**_F_-stat**|
|---|---|---|---|---|
|f|6.297<br>���|5.497<br>���|6.634|���|
|ρ_cross_<br>D2<br>D1<br>β_mkt_<br>_ivol_<br>_mkt cap_<br>_b/m_<br>_illiquidity_<br>Constant<br>_R_2|(3.55)<br>3.426<br>���<br>(12.68)<br>0.3%|(3.04)<br>−7.273<br>���<br>(−2.89)<br>5.138<br>���<br>(2.61)<br>−0.525<br>(−0.85)<br>3.159<br>���<br>(7.45)<br>0.8%|(3.81)<br>−4.305<br>(−1.54)<br>2.5<br>(1.44)<br>−0.662<br>(−0.99)<br>−1.777<br>(−3.54)<br>−0.478<br>(−3.57)<br>−0.048<br>(−0.39)<br>0.506<br>(2.2)<br>10.187<br>(1.25)<br>5.869<br>(6.22)<br>2.4%|���<br>���<br>��<br>���|



_Notes:_ We run the regression Equation (20) for each stock individually and collect the regression’s _F_ -statistics testing on all coefficients being equal to 0. Then, we run a regression on the F-statistics with a set of firms’ characteristics calculated in the in-sample period.[���] ,[��] , and[�] indicate statistical significance at the 1%, 5%, and 10% levels, respectively. 

**Table 7.** Performance of the trading strategy 

|**_No_**<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|f<br>0.0208<br>0.0280<br>0.0327<br>0.0369<br>0.0414<br>0.0470<br>0.0545<br>0.0653<br>0.0831<br>0.1388|_yt _**(**%**)**<br>15.2<br>17.6<br>18.4<br>18.9<br>18.6<br>18.9<br>17.4<br>18.3<br>19.9<br>21.0|**_Buy-and-Hold_**<br>σ_yt _**(**%**)**<br>22.5<br>20.9<br>19.9<br>19.1<br>19.7<br>18.2<br>19.3<br>18.3<br>18.3<br>18.4|**SR**<br>0.67<br>0.84<br>0.92<br>0.99<br>0.94<br>1.04<br>0.90<br>1.00<br>1.09<br>1.14|_yt _**(**%**)**<br>28.1<br>84.1<br>140.7<br>64.0<br>95.1<br>77.0<br>121.4<br>105.8<br>145.0<br>115.2|**_Trading Strategy_**<br>σ_yt _**(**%**)**<br>63.2<br>81.6<br>176.7<br>72.0<br>76.8<br>58.6<br>87.9<br>61.0<br>86.3<br>44.3|**SR**<br>0.44<br>1.03<br>0.80<br>0.89<br>1.24<br>1.31<br>1.38<br>1.74<br>1.68<br>2.60|
|---|---|---|---|---|---|---|---|



_Notes:_ This table presents the equal-weighted returns, standard deviations and SRs of the trading strategy and corresponding buy-and-hold strategies. We sort all stocks by f to 10 decile portfolios and report their performance separately. 

## **4.3.1 Transaction costs** 

We also examine the effect of transaction costs on the trading strategy’s performance. We assume a fixed 0.1% commission fee plus a stock-specific liquidity cost, which is calculated by the stocks’ bid–ask spread as follows: 

**==> picture [228 x 23] intentionally omitted <==**

Chen j Jump Clustering and Pricing Efficiency **1609** 

**Figure 8.** Cumulative log returns of the trading strategy and buy-and-hold strategy. _Notes_ : These two figures plot cumulative returns of the trading strategy and a buy-and-hold strategy across 10 portfolios. Stocks are categorized into these 10 portfolios by f. 

**Table 8.** Performance of the trading strategy with costs 

|**_No_**<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10|f<br>0.0208<br>0.0280<br>0.0327<br>0.0369<br>0.0414<br>0.0470<br>0.0545<br>0.0653<br>0.0831<br>0.1388|_yt _**(**%**)**<br>17.1<br>57.0<br>116.7<br>44.3<br>63.4<br>58.3<br>99.2<br>67.6<br>116.2<br>84.8|σ_yt _**(**%**)**<br>63.2<br>81.5<br>176.6<br>71.8<br>76.8<br>58.4<br>87.5<br>60.7<br>86.3<br>52.3|**SR**<br>0.27<br>0.70<br>0.66<br>0.62<br>0.83<br>1.00<br>1.13<br>1.11<br>1.35<br>1.62|
|---|---|---|---|---|



_Notes:_ This table presents the 10 stock portfolios’ equal-weighted returns, standard deviations and SRs of the trading strategy with transaction costs, including a fixed commission fee and liquidity costs represented by the bid–ask spreads. 

where _bidt;s; askt;s_ and π _t;s_ present the bid/ask price and the bid–ask spread, respectively, of stock _s_ at time _t_ . We only include half of the bid–ask spread in the transaction cost since the price data we used are the average of the bid and ask price. The results with transaction costs are presented in Table 8. The associated cumulative log returns are plotted in Figure 9. The trading strategy’s performance deteriorates since our forecasting framework is based on daily data. This means that the portfolio requires daily rebalancing. However, the portfolio with the highest f still has an SR of 1.62. 

## **5. Concluding Remarks** 

This study investigates the clustering behavior of return jumps across different assets modeled as a self/cross-exciting process embedded in a stochastic volatility model. We estimate the model using a Bayesian MCMC method. The contribution of this article is twofold. First, we introduce a novel measure of stock price efficiency, derived from the extent of jump clustering that an asset exhibits. We illustrate the superiority of this measure in capturing the cross-sectional variations in CAR following earnings announcements, which is robust to other existing measures and control variables. 

**1610** _Journal of Financial Econometrics_ 

**Figure 9.** Cumulative log returns of the trading strategy with transaction costs. _Notes_ : This figure plots cumulative returns of the trading strategy with transaction costs across 10 portfolios. Stocks are categorized into these 10 portfolios by f. 

Secondly, we assess the predictability of jumps based on the jump’s self/cross-exciting characteristics. We employ a particle filter to iteratively estimate latent variables in the outof-sample and conduct one-step-ahead probabilistic forecasting for jumps. Based on RPSs, our forecasts outperform two benchmarks. We also introduce a new statistic representing the difference between the predicted probability of positive and negative jumps. We demonstrate the predictive efficacy of this statistic on returns, with its predictability directly inherited from the extent of jump clustering exhibited by the asset. Furthermore, we outline a trading strategy based on this forecasting framework, which reports an SR of 2.60 without transaction costs and 1.62 when accounting for the transaction costs. 

Our studies shed light on the implication of return jump clustering behaviors and their predictability. The measure we introduce serves as a valuable tool for researchers and market participants aiming to evaluate stock price efficiency over a period of time. The results of our predictability assessment offer insights for individuals seeking to leverage jump clustering features to forecast return jumps and asset returns. 

## **Supplemental Material** 

Supplemental material is available at _Journal of Financial Econometrics_ online. 

## Appendix A.1: Bayesian MCMC Algorithm and Specifications of Priors 

We adopt a Bayesian MCMC algorithm to obtain the joint posterior distribution in Equation (5). We randomly draw samples from conditional posterior distributions. Our sampling algorithm is as follows: 

Chen j Jump Clustering and Pricing Efficiency **1611** 

**Algorithm 1** Bayesian MCMC Algorithm For _i_ ¼ 1 : 100 _;_ 000: 

1: Sample _k_ static parameters: Draw Θ[ð] 1 _[i]_[Þ][from ] _[p]_ �Θ[ð] 1 _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] 2 _[i]_[−][1][Þ] _;_ Θ[ð] 3 _[i]_[−][1][Þ] _;_ . . . _;_ Θ[ð] _k[i]_[−][1][Þ] _;_ Z[ð] _t[i]_[−][1][Þ] �, ..[.] Draw Θ[ð] _k[i]_[Þ][from ] _[p]_ �Θ[ð] _k[i]_[Þ][j] _[y][t][;]_[ Θ] 1[ð] _[i]_[−][1][Þ] _;_ Θ[ð] 2 _[i]_[−][1][Þ] _;_ . . . _;_ Θ[ð] _k[i]_ −[−] 1[1][Þ] _[;]_[ Z] _t_[ð] _[i]_[−][1][Þ] � 2: Sample jumps for _t_ ¼ 1 _;_ 2 _;_ . . . _; T_ : Draw _Jt[p]_[þ] _[;]_[ð] _[i]_[Þ] from _p Jt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;][ J] t[p]_[−] _[;]_[ð] _[i]_[−][1][Þ] _; Jt[v][;]_[ð] _[i]_[−][1][Þ] _;_ n[ð] _t[i]_[−][1][Þ] _; Vt_[ð] _[i]_[−][1][Þ] , � � Draw _Jt[p]_[−] _[;]_[ð] _[i]_[Þ] from _p Jt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;][ J] t[p]_[þ] _[;]_[ð] _[i]_[Þ] _; Jt[v][;]_[ð] _[i]_[−][1][Þ] _;_ n[ð] _t[i]_[−][1][Þ] _; Vt_[ð] _[i]_[−][1][Þ] , � � Draw _Jt[v][;]_[ð] _[i]_[Þ] from _p Jt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;][ J] t[p]_[þ] _[;]_[ð] _[i]_[Þ] _; Jt[p]_[−] _[;]_[ð] _[i]_[Þ] _;_ n[ð] _t[i]_[−][1][Þ] _; Vt_[ð] _[i]_[−][1][Þ] , � � 3: Sample jump sizes for _t_ ¼ 1 _;_ 2 _;_ . . . _; T_ : Draw ξ _[p] t_[þ] _[;]_[ð] _[i]_[Þ] from _p Jt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;]_[ ξ] _[p] t_[−] _[;]_[ð] _[i]_[−][1][Þ] _;_ ξ _[v] t[;]_[ð] _[i]_[−][1][Þ] _;_ _**J**_[ð] _t[i]_[Þ] _[;][ V]_[ ð] _t[i]_[−][1][Þ] , � � Draw ξ _[p] t_[−] _[;]_[ð] _[i]_[Þ] from _p Jt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;]_[ ξ] _[p] t_[þ] _[;]_[ð] _[i]_[Þ] _;_ ξ _[v] t[;]_[ð] _[i]_[−][1][Þ] _;_ _**J**_[ð] _t[i]_[Þ] _[;][ V] t_[ ð] _[i]_[−][1][Þ] , � � Draw ξ _[v] t[;]_[ð] _[i]_[Þ] from _p Jt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;]_[ ξ] _[p] t_[þ] _[;]_[ð] _[i]_[Þ] _;_ ξ _[p] t_[−] _[;]_[ð] _[i]_[Þ] _;_ _**J**_[ð] _t[i]_[Þ] _[;][ V]_[ ð] _t[i]_[−][1][Þ] , � � 4: Sample variance: for _t_ ¼ 1,2, … , T: Draw _Vt_[ð] _[i]_[Þ][from ] _[p] Vt_[ð] _[i]_[Þ][j] _[y][t][;]_[ Θ][ð] _[i]_[Þ] _[;]_[ n][ð] _t[i]_[Þ] _[;]_ _**[ J]**_[ð] _t[i]_[Þ] , � � 

We ran our MCMC algorithm for 100,000 iterations; the first 50,000 is considered a burn-in period. We sample the posterior distribution by a hybrid of Gibbs sampling and MetropolisHastings. Gibbs sampling methods are used when conjugate priors of conditional posteriors are available. We adopt the Metropolis–Hastings sampling method for others whose posteriors are not available in closed form. Details of posterior distributions are provided by Lazar and Qi (2022) and Rasmussen (2013). Our specifications of priors are as follow: 

|**Parameters**<br>μ<br>θ<br>ρ<br>μ_p_þ<br>μ_p_−<br>μ_v_<br>b|**Prior distribution**<br>_N_(0, 25)<br>_N_ð0_;_1Þ**1**θ_>_0<br>_U_ð−1_;_1Þ<br>_N_(50, 100)<br>_N_ð−50_;_100Þ<br>_IG_(10, 20)<br>_N_ð0_;_0_:_3Þ**1**b_>_0|**Parameters**<br>κ<br>σ_v_<br>ξ_t_<br>σ2<br>_p_þ<br>σ2<br>_p_−<br>ϑ<br>k0|**Prior distribution**<br>_N_ð0_;_1Þ**1**κ_>_0<br>_IG_ð2_:_5_;_0_:_1Þ<br>_N_ð0_;_100Þ**1**ξ_>_0<br>_IG_(10, 40)<br>_IG_(10, 40)<br>_N_ð0_;_0_:_3Þ**1**ϑ_>_0<br>_N_ð0_;_0_:_03Þ**1**k0_>_0|
|---|---|---|---|



## Appendix A.2: Particle Filter 

We adopt a particle filter to sample latent variables in the out-of-sample period. The particle filtering method is given by Pitt and Shephard (1999). Creal (2012) also gives a review of this technique. Our ultimate goal is to sample from _p_ ðZ[�] _t_[j] _[y][t][;]_[ ^][Θ][Þ][ to obtain estimates of la-] tent variables at each time _t_ , where Z[�] _t_[¼ f] _[v][t][;][ J][t]_[g][. We remark that we ignore sampling jump ] sizes ξ _t_ since they are less relevant to forward simulating jump intensities fλ[þ] _t[;]_[ λ][−] _t_[g][. We ] adopt a sequential importance sampling with a re-sampling scheme: 

See more details of particle filtering in Creal (2012), where codes of the particle filtering algorithm are also available. 

**1612** _Journal of Financial Econometrics_ 

**==> picture [255 x 109] intentionally omitted <==**

**----- Start of picture text -----**<br>
Algorithm 2  Sequential Importance Sampling with Re-sampling<br>At  t  ¼ 0, for  i ¼ 1 ;  . . .  ; N<br>Draw Z [�] 0 [ð] [i] [Þ �] [g] [0][ðZ][�] 0 [Þ][, set ][ω][ð] 0 [i] [Þ] [¼] gp 0ððZZ [�] 0 [�] 0 [ð][ð] [i][i] [ÞÞ][ÞÞ]<br>For  t ¼ 1 ;  . . .  ; T :<br>1: For  i ¼ 1 ;  . . .  ; N , draw Z [�] t [ð] [i] [Þ �] [g][t] [ðZ][�] t [jZ][�] t −1 [;][ y][t][;] [ ^][Θ][Þ][.]<br>p yt jZ [�] t [ð] [i] [Þ] [;] [Θ][^] p Z [�] t [ð] [i] [ÞjZ][�] t −1 [ð] [i] [Þ] [;] [Θ][^]<br>2: Compute importance weights ω [ð] t [i] [Þ] / ω [ð] t [i] − [Þ] 1 � � � � .<br>3: Normalize importance weights ω^ [ð] t [i] [Þ] ¼ ω N [ð] t [i] [Þ] . gt � Z [�] t [ð] [i] [ÞjZ][�] t −1 [ð] [i] [Þ] [;][y][t] [;] [Θ][^] �<br>P j ¼1 [ω] t [ð] [j] [Þ]<br>4: Re-sample  N  particles by fω^ [ð] t [i] [Þ][g] [N] i ¼1  [and reset ][ω] t [ð] [i] [Þ] ¼ N 1 [.]<br>**----- End of picture text -----**<br>


## Appendix A.3: Non-Parametric Jump Filtering 

Our jump filtering method is mainly based on Mancini, Mattiussi, and Reno (2015)� and � Figueroa-Lopez and Mancini (2019). We identify a jump at time _t_ , _Jt_ ¼ 1, when the squared return is greater than a threshold, _y_[2] _t[>]_[ ^] _[v]_[2] _t_[�][2][Δ] _[log]_ Δ1 ~~[.]~~ _[v]_[^][2] _t_[is a non-parametric estima-] tor of spot variance based on pre-truncated returns: 

**==> picture [123 x 26] intentionally omitted <==**

where _fh_ ð�Þ is weight function, _fh_ ð _t_ Þ ¼ 1 _h_[�] _e_[−] 2[j] _[t][=][h]_[j][with a bandwidth ] _[h]_[ ¼][ 60][Δ ][for simplicity. The ] idea of this filtering is to extract those standardized squared returns ( _yt_ Δ _=v_[^][2] _t_[) which are not ] generated by a Brownian motion, whose absolute value is greater than the thresh-fi fi fi fi fi fi fi fi fi fi f old p2 logð1 _=_ ΔÞ. 

## Appendix A.4: Full Regression Results of Figure 6 

This table presents the full regression results for Equation (19) and Figure 6. We collect data for five types of news release dates. Then, we perform regressions using five dummy variables for each type of news representing from 1 day before the news release to 5 days after the news release. The data used in the regression are US stock data from 2000 to 2012. Note we did not impose a time-fixed effect since it is correlated with the macro-news release dates (Table A.4). 

**Table A.4.** Jump’s probability regressions on news releases 

|_M_1_;_τ¼−1<br>_t_<br>_M_1_;_τ¼0<br>_t_<br>_M_1_;_τ¼1<br>_t_<br>_M_1_;_τ¼2<br>_t_<br>_M_1_;_τ¼3:5<br>_t_|**Coef. (103)**<br>0.0336<br>0.0665<br>0.0753<br>0.0351<br>−0.0188|**t-stat**<br>1.68<br>3.00<br>2.93<br>2.28<br>−1.35|**p-value**<br>0.09<br>0.00<br>0.00<br>0.02<br>0.18|_F_1_;_τ¼−1<br>_t_<br>_F_1_;_τ¼0<br>_t_<br>_F_1_;_τ¼1<br>_t_<br>_F_1_;_τ¼2<br>_t_<br>_F_1_;_τ¼3:5<br>_t_|**Coef. (103)**<br>0.0308<br>−0.0053<br>0.3180<br>0.9957<br>0.1600|**t-stat**<br>1.55<br>−0.24<br>2.8<br>10<br>2.4|**_p_-value**<br>0.12<br>0.81<br>0.01<br>0.00<br>0.02|
|---|---|---|---|---|---|---|---|
|_M_2_;_τ¼−1<br>_t_|0.0051|0.26|0.80|_F_2_;_τ¼−1<br>_t_|0.0134|1.29|0.20|
|_M_2_;_τ¼0<br>_t_|0.0179|0.81|0.42|_F_2_;_τ¼0<br>_t_|0.0188|1.41|0.16|
|_M_2_;_τ¼1<br>_t_|0.0392|1.67|0.10|_F_2_;_τ¼1<br>_t_|−0.0038|−0.25|0.81|
|_M_2_;_τ¼2<br>_t_|0.0229|0.80|0.42|_F_2_;_τ¼2<br>_t_|0.0283|1.54|0.12|
|_M_2_;_τ¼3:5<br>_t_|−0.0210|−1.17|0.24|_F_2_;_τ¼3:5<br>_t_|−0.0592|−2.31|0.02|



(continued) 

Chen j Jump Clustering and Pricing Efficiency **1613** 

**1613** 

**Table A.4.** (continued) 

|**Table A.4.**(co|ntinued)||||||
|---|---|---|---|---|---|---|
||**Coef. (103)**|**t-stat**|**p-value**|**Coef. (103)**|**t-stat**|**_p_-value**|
|_M_3_;_τ¼−1<br>_t_|0.0323|1.18|0.24||||
|_M_3_;_τ¼0<br>_t_<br>_M_3_;_τ¼1<br>_t_<br>_M_3_;_τ¼2<br>_t_<br>_M_3_;_τ¼3:5<br>_t_<br>Intercept<br>Controls<br>Firm-fxed<br>Time-fxed<br># Obs.<br>_R_2|0.0505<br>0.0815<br>0.6530<br>−0.0114<br>0.0443<br>Yes<br>Yes<br>No<br>8,399,706<br>1.49%|2.28<br>3.2<br>2.59<br>−1.22<br>2057|0.02<br>0.00<br>0.01<br>0.22<br>0.00||||



_Notes:_ This table presents the full regression results for Equation (19) and Figure 6. The control variables include log market cap, book-to-market ratio, illiquidity ratio, and idiosyncratic volatility. 

## **References** 

Aït-Sahalia, Y., J. Cacho-Diaz, and R. J. Laeven. 2015. Modeling Financial Contagion Using Mutually Exciting Jump Processes. _Journal of Financial Economics_ 117: 585–606. 

Amihud, Y. 2002. Illiquidity and Stock Returns: Cross-Section and Time-Series Effects. _Journal of Financial Markets_ 5: 31–56. 

Bajgrowicz, P., O. Scaillet, and A. Treccani. 2016. Jumps in High-Frequency Data: Spurious Detections, Dynamics, and News. _Management Science_ 62: 2198–2217. 

Baker, S. R, N. Bloom, S. J. Davis, and M. C. Sammon. 2021. What Triggers Stock Market Jumps? Technical Report, National Bureau of Economic Research. 

Bates, D. S. 1996. Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in Deutsche Mark Options. _Review of Financial Studies_ 9: 69–107. 

B�egin, J. F., C. Dorion, and G. Gauthier. 2020. Idiosyncratic Jump Risk Matters: Evidence from Equity Returns and Options. _The Review of Financial Studies_ 33: 155–211. 

Bernard, V. L., and J. K. Thomas. 1989. Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium? _Journal of Accounting Research_ 27: 1–36. 

Bernile, G., J. Hu, and Y. Tang. 2016. Can Information Be Locked up? Informed Trading Ahead of Macro-News Announcements. _Journal of Financial Economics_ 121: 496–520. 

Bradley, D., J. Clarke, S. Lee, and C. Ornthanalai. 2014. Are Analysts’ Recommendations Informative? Intraday Evidence on the Impact of Time Stamp Delays. _The Journal of Finance_ 69: 645–673. 

Bris, A., W. N. Goetzmann, and N. Zhu. 2007. Efficiency and the Bear: Short Sales and Markets around the World. _The Journal of Finance_ 62: 1029–1079. 

Brogaard, J., D. Li, and Y. Xia. 2017. Stock Liquidity and Default Risk. _Journal of Financial Economics_ 124: 486–502. 

Busch, P., and S. Obernberger. 2017. Actual Share Repurchases, Price Efficiency, and the Information Content of Stock Prices. _Review of Financial Studies_ 30: 324–362. 

Chan, L. K., N. Jegadeesh, and J. Lakonishok. 1996. Momentum Strategies. _The Journal of Finance_ 51: 1681–1713. 

Chen, J., M. P. Clements, and A. Urquhart. 2023. Modeling Price and Variance Jump Clustering Using the Marked Hawkes Process. _Journal of Financial Econometrics_ 

Chordia, T., R. Roll, and A. Subrahmanyam. 2008. Liquidity and Market Efficiency. _Journal of Financial Economics_ 87: 249–268. 

Christensen, K, A. Timmermann, and B. Veliyev. 2023. Warp Speed Price Moves: Jumps after Earnings Announcements. _Available at SSRN 4422376_ 

Creal, D. 2012. A Survey of Sequential Monte Carlo Methods for Economics and Finance. _Econometric Reviews_ 31: 245–296. 

Creal, D. D., and J. C. Wu. 2015. Estimation of Affine Term Structure Models with Spanned or Unspanned Stochastic Volatility. _Journal of Econometrics_ 185: 60–81. 

**1614** _Journal of Financial Econometrics_ 

Creal, D. D., and J. C. Wu. 2017. Monetary Policy Uncertainty and Economic Fluctuations. _International Economic Review_ 58: 1317–1354. 

Da, Z., U. G. Gurun, and M. Warachka. 2014. Frog in the Pan: Continuous Information and Momentum. _Review of Financial Studies_ 27: 2171–2218. 

Diebold, F. X., and R. S. Mariano. 2002. Comparing Predictive Accuracy. _Journal of Business & Economic Statistics_ 20: 134–144. 

Duffie, D., J. Pan, and K. Singleton. 2000. Transform Analysis and Asset Pricing for Affine Jump-Diffusions. _Econometrica_ 68: 1343–1376. 

Engle, R. F., M. K. Hansen, A. K. Karagozoglu, and A. Lunde. 2021. News and Idiosyncratic Volatility: The Public Information Processing Hypothesis. _Journal of Financial Econometrics_ 19: 1–38. 

Erdemlioglu, D., and X. Yang. 2023. News Arrival, Time-Varying Jump Intensity, and Realized Volatility: Conditional Testing Approach. _Journal of Financial Econometrics_ 21: 1519–1556. 

Figueroa-Lopez, J. E., and C. Mancini. 2019. Optimum Thresholding Using Mean and Conditional Mean � Squared Error. _Journal of Econometrics_ 208: 179–210. 

Foley, S., and T. J. Putniņ�s. 2016. Should we Be Afraid of the Dark? dark Trading and Market Quality. _Journal of Financial Economics_ 122: 456–481. 

Gurkaynak, R. S., B. Kisaciko�glu, and J. H. Wright. 2020. Missing Events in Event Studies: Identifying the Effects of Partially Measured News Surprises. _American Economic Review_ 110: 3871–3912. 

Hawkes, A. G. 1971a. Point Spectra of Some Mutually Exciting Point Processes. _Journal of the Royal Statistical Society: Series B (Methodological)_ 33: 438–443. 

Hawkes, A. G. 1971b. Spectra of Some Self-Exciting and Mutually Exciting Point Processes. _Biometrika_ 58: 83–90. 

Herrera, R., and A. Clements. 2020. A Marked Point Process Model for Intraday Financial Returns: Modeling Extreme Risk. _Empirical Economics_ 58: 1575–1601. 

Heston, S. L. 1993. A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options. _Review of Financial Studies_ 6: 327–343. 

Hirshleifer, D., S. S. Lim, and S. H. Teoh. 2009. Driven to Distraction: Extraneous Events and Underreaction to Earnings News. _The Journal of Finance_ 64: 2289–2325. 

Hou, K., and T. J. Moskowitz. 2005. Market Frictions, Price Delay, and the Cross-Section of Expected Returns. _Review of Financial Studies_ 18: 981–1020. 

Hung, M., X. Li, and S. Wang. 2015. Post-Earnings-Announcement Drift in Global Markets: Evidence from an Information Shock. _The Review of Financial Studies_ 28: 1242–1283. 

Jeon, Y., T. H. McCurdy, and X. Zhao. 2022. News as Sources of Jumps in Stock Returns: Evidence from 21 Million News Articles for 9000 Companies. _Journal of Financial Economics_ 145: 1–17. 

Jiang, G. J., and K. X. Zhu. 2017. Information Shocks and Short-Term Market Underreaction. _Journal of Financial Economics_ 124: 43–64. 

Jones, C. M., A. V. Reed, and W. Waller. 2016. Revealing Shorts an Examination of Large Short Position Disclosures. _Review of Financial Studies_ 29: 3278–3320. 

Kou, S., C. Yu, and H. Zhong. 2017. Jumps in Equity Index Returns before and during the Recent Financial Crisis: A Bayesian Analysis. _Management Science_ 63: 988–1010. 

Kurov, A., A. Sancetta, G. Strasser, and M. H. Wolfe. 2019. Price Drift before us Macroeconomic News: Private Information about Public Announcements? _Journal of Financial and Quantitative Analysis_ 54: 449–479. 

Kwok, S. 2024. A Consistent and Robust Test for Autocorrelated Jump Occurrences. _Journal of Financial Econometrics_ 22: 157–186. 

Lazar, E., and S. Qi. 2022. Model Risk in the over-the-Counter Market. _European Journal of Operational Research_ 298: 769–784. 

- Lee, S. S. 2012. Jumps and Information Flow in Financial Markets. _Review of Financial Studies_ 25: 439–479. 

Lee, S. S., and M. Wang. 2019. The Impact of Jumps on Carry Trade Returns. _Journal of Financial Economics_ 131: 433–455. 

Liu, B., H. Wang, J. Yu, and S. Zhao. 2020. Time-Varying Demand for Lottery: Speculation Ahead of Earnings Announcements. _Journal of Financial Economics_ 138: 789–817. 

Loughran, T., and B. McDonald. 2014. Measuring Readability in Financial Disclosures. _The Journal of Finance_ 69: 1643–1671. 

Chen j Jump Clustering and Pricing Efficiency **1615** 

- Mancini, C., V. Mattiussi, and R. Reno. 2015. Spot Volatility Estimation Using Delta Sequences. � _Finance and Stochastics_ 19: 261–293. 

Maneesoonthorn, W., C. S. Forbes, and G. M. Martin. 2017. Inference on Self-Exciting Jumps in Prices and Volatility Using High-Frequency Measures. _Journal of Applied Econometrics_ 32: 504–532. 

- Pitt, M. K., and N. Shephard. 1999. Filtering via Simulation: Auxiliary Particle Filters. _Journal of the American Statistical Association_ 94: 590–599. 

- Rasmussen, J. G. 2013. Bayesian Inference for Hawkes Processes. _Methodology and Computing in Applied Probability_ 15: 623–642. 

- Saffi, P. A., and K. Sigurdsson. 2011. Price Efficiency and Short Selling. _Review of Financial Studies_ 24: 821–852. 

- Savor, P. G. 2012. Stock Returns after Major Price Shocks: The Impact of Information. _Journal of Financial Economics_ 106: 635–659. 

- Tao, R., C. Brooks, and A. Bell. 2021. Tomorrow’s Fish and Chip Paper? slowly Incorporated News and the Cross-Section of Stock Returns. _The European Journal of Finance_ 27: 774–795. 

# The Author(s) 2024. Published by Oxford University Press. 

This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercialNoDerivs licence (https://creativecommons.org/licenses/by-nc-nd/4.0/), which permits non-commercial reproduction and distribution of the work, in any medium, provided the original work is not altered or transformed in any way, and that the work is properly cited. For commercial re-use, please contact journals.permissions@oup.com Journal of Financial Econometrics, 2024, 22, 1588–1615 https://doi.org/10.1093/jjfinec/nbae009 Article 

