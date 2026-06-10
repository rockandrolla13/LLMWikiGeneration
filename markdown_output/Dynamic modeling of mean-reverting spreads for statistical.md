# Dynamic modeling of mean-reverting spreads for statistical arbitrage 

K. Triantafyllopoulos[∗] G. Montana[†] 

November 26, 2024 

## Abstract 

Statistical arbitrage strategies, such as pairs trading and its generalizations, rely on the construction of mean-reverting spreads enjoying a certain degree of predictability. Gaussian linear state-space processes have recently been proposed as a model for such spreads under the assumption that the observed process is a noisy realization of some hidden states. Real-time estimation of the unobserved spread process can reveal temporary market inefficiencies which can then be exploited to generate excess returns. Building on previous work, we embrace the state-space framework for modeling spread processes and extend this methodology along three different directions. First, we introduce timedependency in the model parameters, which allows for quick adaptation to changes in the data generating process. Second, we provide an on-line estimation algorithm that can be constantly run in real-time. Being computationally fast, the algorithm is particularly suitable for building aggressive trading strategies based on high-frequency data and may be used as a monitoring device for mean-reversion. Finally, our framework naturally provides informative uncertainty measures of all the estimated parameters. Experimental results based on Monte Carlo simulations and historical equity data are discussed, including a co-integration relationship involving two exchange-traded funds. 

Keywords: mean reversion, pairs trading, state-space models, time-varying autoregressive processes, dynamic regression, statistical arbitrage. 

> ∗Department of Probability and Statistics, Hicks Building, University of Sheffield, Sheffield S3 7RH, UK, email: k.triantafyllopoulos@sheffield.ac.uk 

> †Department of Mathematics, Statistics Section, Imperial College London, London SW7 2AZ, UK, email: g.montana@imperial.ac.uk 

1 

## 1 Introduction 

A time series is known to exhibit mean reversion when, over a certain period of time, is “reverting” to a constant mean. In recent years, the notion of mean reversion has received a considerable amount of attention in the financial literature. For instance, there has been increasing interest in studying the long-run properties of stock prices, with particular attention being paid to investigate whether stock prices can be characterized as random walks or mean reverting processes. If a price time series evolves as a random walk, then any shock is permanent and there is no tendency for the price level to return to a constant mean over time; moreover, in the long run, the volatility of the process is expected to grow without bound, and the time series cannot be predicted based on historical observations. On the other hand, if a time series of stock prices follows a mean reverting process, investors may be able to forecast future returns by using past information. Since the seminal work of Fama and French [1988] and Poterba and Summers [1988], who first documented mean-reversion in stock market returns during a long time horizon, several studies have been carried out to detect mean reversion in several markets (e.g. Chaudhuri and Wu [2003]) and many asset classes (e.g. Deaton and Laroque [1992], Jorion and Sweeney [1996]). 

Since future observations of a mean-reverting time series can potentially be forecasted using historical data, a number of studies have also examined the implications of mean reversion on portfolio allocation and asset management; see Barberis [2000] and Carcano et al. [2005] for recent works. Active asset allocation strategies based on mean-reverting portfolios, which generally fall under the umbrella of statistical arbitrage, have been utilized by investment banks and hedge funds, with varying degree of success, for several years. Possibly the simplest of such strategies consists of a portfolio of only two assets, as in pairs trading. This trading approach consists in going long a certain asset while shorting another asset in such a way that the resulting portfolio has no net exposure to broad market moves. In this sense, the strategy is often described as market neutral. Entire monographs have been written to illustrate how pairs trading works, how it can be implemented in real settings, and how its performance has evolved in recent years (see, for instance, Vidyamurthy [2004] and Pole [2007]). The underlying assumption of pairs trading is that two financial instruments with similar characteristics must be priced more or less the same. Accordingly, the first step consists in finding two financial instruments whose prices, in the long term, are expected to 

2 

be tied together by some common stochastic trend. What this implies is that, although the two time series of prices may not necessarily move in the same direction at all times, their spread (for instance, the simple price difference) will fluctuate around an equilibrium level. Since the spread quantifies the degree of mispricing of one asset relative to the other one, these strategies are also refereed to as relative-value. If a common stochastic trend indeed exists between the two chosen assets, any temporary deviation from the assumed mean or equilibrium level is likely to correct itself over time. The predictability of this portfolio can then be exploited to generate excess returns: a trader, or an algorithmic trading system, would open a position every time a substantially large deviation from the equilibrium level is detected and would close the position when the spread has reverted back to the its mean. This simple concept can be extended in several ways, for instance by replacing one of the two assets with an artificial one (e.g. a linear combination of asset prices), with the purpose of exploiting the same notions of relative-value pricing and mean-reversion, although in different ways; some relevant work along these lines has been documented, among others, by Montana et al. [2009] and Montana and Parrella [2009], who describe statistical arbitrage strategies involving futures contracts and exchange-traded funds (ETFs), respectively. One aspect that has not been fully investigated in the studies above is how to explicitly model the resulting observed spread. A stochastic model describing how the spread evolves over time is highly desirable because it allows the analyst to precisely characterize and monitor some of its salient properties, such as mean-reversion. Moreover, improved trading rules may be built around specific properties of the adopted spread process. 

Recently, Elliott et al. [2005] suggested that Gaussian linear state-space processes may be suitable for modeling mean-reverting spreads arising in pairs trading, and described how such models can yield statistical arbitrage strategies. Their main observation is that the observed process should be seen as a noisy realization of an underlying hidden process describing the true spread, which may capture the true market conditions; thus, a comparison of the estimated unobserved spread process with the observed one may lead to the discovery of temporary market inefficiencies. Based on the additional assumption that the model parameters do not vary over short periods of time, Elliott et al. [2005] suggested to use the EM algorithm, an iterative procedure for maximum likelihood estimation, for tracking the hidden process and estimating the other unknown model parameters. To make the exposition 

3 

self-contained, we briefly review their model in Section 2, and state under what conditions the stochastic process is mean-reverting. 

In this paper we build upon the model by Elliott et al. [2005] and extend their methodology in a number of ways. First, in Section 3, we introduce time-dependency in the model parameters. The main advantage of this formulation is a gain in flexibility, as the model is able to adapt quickly to changes in the data generating process; Section 3.1 further motivates our formulation and discusses its potential advantages. In Section 3.2 we derive new conditions that need to be satisfied for a model with time-varying parameters to be mean-reverting. In Section 3.3 we describe a Bayesian framework for parameter estimation which then leads to a recursive parameter estimation procedure suitable for real-time applications. The final algorithm is detailed in Section 4; an analysis and discussion on the convergence properties of the algorithm as well as practical suggestions on how to specify the initial values and prior distributions are provided. Unlike the EM algorithm, our estimation procedure also produces uncertainty measures without any additional computational costs. With a view on statistical arbitrage, in Section 4.5 we add a note discussing how pairs trading may be implemented using the spread models proposed in this work and enumerate other important issues involved in realistic implementations, together with some pointers to the relevant literature. However, an empirical evalutation of trading strategies is beyond the scope of this work. For further discussions on statistical arbitrage approaches based on mean-reverting spreads and many illustrative numerical examples the reader is referred to Pole [2007]. 

In Section 5, based on a battery of Monte Carlo simulations, we demonstrate that posterior means estimated on-line by our Bayesian algorithm recovers the true model parameters and can be particularly advantageous when the analysts wishes to track sudden changes in the mean-level of the spread and its mean-reverting behavior. For instance, real-time monitoring may be used to derive stop-loss rules in algorithmic trading. Two examples involving real historical data are given in Section 5.2, where the cointegrating relationship between a pair of stocks and a pairs of ETFs are discussed. Final remarks are found in Section 6 and the proofs of arguments in Sections 3.2 and 4.3 can be found in the appendix. 

4 

## 2 Time-invariant state-space models for mean-reverting spreads 

Throughout the paper we will assume that the trader has identified two candidate financial instruments whose prices are observed at discrete time points t = 1, 2, . . . and are denoted by p[(] t[j][)][,][with][j][= 1][,][ 2.][At][any][given][time][t][,][let][y][t][denote][the][price][spread,][defined][as] 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0005-02.png)


for some parameters α and β which are usually estimated by ordinary least squares (OLS) methods using historical data. It seems common practice to select the order of i and j such that yt yields the largest β and the resulting spread captures as much information as possible about the (linear) co-movement of the two assets. In Section 5.2 we briefly mention how a penalized OLS model may be used for recursive estimation of a time-varying β. More generally, the observed spread yt may also be obtained in different ways or may represent the return process of an initial price spread. One of the two component processes {p[(] t[j][)][}][may] even be artificially built using a linear combination of a basket of assets. For our purposes, the only requirement is that the process {yt} is assumed to be mean-reverting. 

Furthermore, following Elliott et al. [2005], we assume that the observed spread yt is a noisy realization of a true but unobserved spread or state xt. The state process {xt} is defined such that 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0005-05.png)


where 0 < b < 2, a is an unrestricted real number and x1 is the initial state. The restriction 0 < b < 2 is imposed, because otherwise {xt} is non-stationary and thus mean reversion has probability zero to occur. The innovation series {εt} is taken to be an i.i.d. Gaussian process with zero mean and variance C[2] , and εt+1 is assumed to be uncorrelated of xt, for t = 1, 2, . . .. Conditions for the state process to be mean-reverting are established using standard arguments, as follows. First, rewrite (1) as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0005-07.png)


Expanding on this, we obtain 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0005-09.png)


5 

Then, taking expectations and variances, 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0006-01.png)


and 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0006-03.png)


It is observed that, when |1 − b| < 1, and regardless of a, limt→∞(1 − b)[t][−][1] = 0 and therefore limt→∞ E(xt) = a/b. Therefore, in the long run, the state process fluctuates around its mean level a/b. Otherwise, when |1 − b| ≥ 1, (1 − b)[t][−][1] is unbounded and hence E(xt) is unbounded too. Analogously, when |1 − b| < 1 and regardless of a, the variance Var(xt) converges to C[2] /{1 − (1 − b)[2] }. Conversely, if |1 − b| ≥ 1, the variance of xt is unbounded with geometric speed. It is concluded that the hidden process {xt} is mean reverting when 1 − b lies inside the unit circle. Adopting the notation of Elliott et al. [2005], we define A = a and B = 1 − b, so that the process xt can be rewritten as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0006-05.png)


Without loss of generality, we postulate that {yt} is a noisy version of {xt} generated as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0006-07.png)


where {ωt} is Gaussian white noise with variance D[2] and ωt is uncorrelated of xt, for t = 1, 2, . . .. From (3), it also follows that {yt} is a mean-reverting process. 

Note that, together with an initial distribution of the state x1, equations (2) and (3) define a Gaussian linear state-space model with parameters A, B, C, D. State-space models were originally developed by control engineers [Kalman, 1960] and are useful tools for expressing dynamic systems involving unobserved state variables. The reader is also referred to Harvey [1989] and West and Harrison [1997] for book-length expositions. 

## 3 Time-varying dynamic models and on-line estimation 

## 3.1 Preliminaries 

The linear Gaussian state-space model described by equations (2) and (3) contains the unknown parameters A, B, C and D which need to be estimated using historical data. When the 

6 

parameters are known, the Kalman filter provides a recursive procedure for estimating the state process xt [Kalman, 1960]. Full derivations of the Kalman filter and lucid explanations in a Bayesian framework can be found in Meinhold and Singpurwalla [1983]. In practice, maximum likelihood estimation (MLE) of the unknown parameters is required in order to fully specify the model. MLE for state-space models can be routinely carried out in a missing-data framework using the EM algorithm, as first proposed in the 1980s by Shumway and Stoffer [1982] and Ghosh [1989]; a detailed derivation can also be found in Ghahramani and Hinton [1996]. In the context of pairs trading, Elliott et al. [2005] reports some simulation and calibration studies demonstrating that the EM algorithm provides a consistent and robust estimation procedure for the model (2)-(3), and suggest that the finite-dimensional recursive filter described in Elliott and Krishnamurthy [1999] may also be used for estimation (although no results were provided). 

Elliott et al. [2005] suggest to base model estimation on data points belonging to a lookback window of size N . A full iterative calibration procedure is then run till convergence every time a new data point is observed and the window has been shifted one-step ahead. This approach implicitly requires the analyst to select a value of N (the effective sample size) ensuring that, within each time window, the model parameters do not vary. The selection of N may be difficult without a proper model selection procedure in place to test the assumption that the model is locally appropriate. For instance, although a small value of N may guarantee adequacy of the model, it could also lead to notable biases in the parameter estimates. When N is too large, a number of factors such as special market events, persisting pricing inefficiencies or structural price changes may invalidate the modeling assumptions. Clearly, the question of how much history to use to calibrate a model and the corresponding trading strategy is a critical one. 

From a practical point of view, repeating the EM algorithm several times over different window sizes in search for an optimal window size may be computationally expensive. Even performing a single calibration run may not be fast enough to accommodate very aggressive trading strategies in high-frequency domains, due to the well-known slow convergence properties of the EM algorithm. More notably, a vanilla application of this algorithm does not automatically provide any measure of parameter uncertainty. Although various methods and modifications have been proposed in the statistical literature in this direction (see, for 

7 

instance, McLachlan and Krishnan [1997]), the resulting methods usually introduce further computational complexity. 

In order to cope with these limitations, in this section we present and discuss our three main contributions. Firstly, we introduce more flexibility and release some of the modeling assumptions by allowing the model parameters to vary over time; in this way, both smooth and sudden changes in the data generating process (such as those created by structural price changes and unusual persistence of market inefficiencies) will be more easily accommodated. Secondly, we propose a practical on-line estimation procedure that, being non-iterative, can be run efficiently over time, even at high sampling frequencies, and does not inflict the burden of frequent re-calibration and window size selection. Ideally, a model should be able to adapt to changes in the data generating mechanism with minimal user intervention, and should be amenable to on-line monitoring so that the key parameters characterizing the underlying mean-reverting property can always be under continuous scrutiny. These features enable the trader (or trading system) to take fast dynamic decisions. Thirdly, as a result of the Bayesian framework proposed here for recursive estimation, measures of uncertainty extracted from the full posterior distribution can be routinely computed at no extra cost. These measures can be very informative in quantifying and assessing estimation errors, and can potentially be exploited to derive more robust trading strategies; see Section 5 for some practical examples. 

## 3.2 The proposed model 

In this section we initially propose a variation of the classic state-space model used by Elliott et al. [2005] in which the parameters are not assumed to be constant over time. This modification will then force us to reconsider under which conditions the spread process is mean-reverting. 

First, let us rearrange the model (2) and (3) in an autoregressive (AR) form. From (3), note that xt = yt − ωt. Then, from substitution in (2) for t ≥ 2, we obtain 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0008-05.png)


where ǫt = ωt − Bωt−1 + εt is distributed as a N (0, σ[2] ), for σ[2] = D[2] + B[2] D[2] + C[2] . The above model is an AR model of order 1 with parameters A, B and σ[2] . 

We achieve time-dependence in the parameters of (4) by replacing A and B with At and Bt, respectively, and postulating that both parameters evolve over time, according to 

8 

some weakly stationary process. Here we consider the case of At and Bt changing over time via AR models, but more general time series may be considered. These choices lead to the specification of a time-varying AR model of order 1, or TVAR(1). Accordingly, the observed spread is described by the following law, 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0009-01.png)



![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0009-02.png)


where φ1 and φ2 are the AR coefficients, usually being assumed to lie inside the unit circle so that At and Bt may be weakly stationary processes. 

Setting θt = (At, Bt)[′] and Ft = (1, yt−1)[′] , the model can be expressed in state space form, 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0009-05.png)



![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0009-06.png)


with Φ = diag(φ1, φ2) and error structure governed by the observation error ǫt ∼ N (0, σ[2] ) and the evolution error vector νt = (ν1t, ν2t)[′] ∼ N2(0, σ[2] Vt), where N2(·, ·) denotes the bivariate Gaussian distribution. It is assumed that the innovation series {ǫt} and {νt} are individually and mutually uncorrelated and they are also uncorrelated of the initial state vector θ1, i.e. E(ǫtǫs) = 0; E(νtνs[′][)][=][0;][ E][(][ǫ][t][ν][u][)][=][0;][ E][(][ǫ][t][θ][1][)][=][0;][ E][(][ν][t][θ] 1[′][)][=][0,][for][any][t][=][s][,][where][E][(][.][)] denotes expectation and θ1[′][denotes][the][row][vector][of][θ][1][.] 

With the inclusion of a time component in the parameters A and B, we now need to revise the conditions under which the mean reversion property holds true. The next result gives sufficient conditions for the spread {yt} to be mean-reverting. 

Theorem 1. If {yt} is generated from model (6)-(7), then, conditionally on a realized sequence B1, . . . , Bt, {yt} is mean reverting if one of the two conditions apply: 

(a) φ1 = φ2 = 1, Vt = 0 and |B1| < 1; 

- (b) φ1 and φ2 lie inside the unit circle, Vt is bounded and |Bt| < 1, for all t ≥ t0 and for some integer t0 > 0. 

Some comments are in order. First we note that if At = A and Bt = B (this is achieved by setting φ1 = φ2 = 1, and by forcing the covariance matrix of νt to be zero for all t), the condition |B1| = |B| < 1 of Theorem 1 reduces to the known condition of mean reversion 

9 

for the static AR model, as in the previous section. In the dynamic case, when At and/or Bt change over time, the condition |Bt| < 1 enables us to check mean reversion in an on-line fashion. Following the approach of Elliott et al. [2005] for the AR model, we use model (6) in order to obtain estimates B[ˆ] t of Bt and then we check |B[ˆ] t| < 1 in order to declare whether {yt} is mean reverting or not; in the following sections we detail the computations involved in the estimation of Bt. Structural changes in the level of yt are accounted through estimates of At, but these do not affect the mean reversion of {yt} as At controls only the level of yt. For the case of At = A, this is explained in some detail in Elliott et al. [2005] and for more information on structural changes for cointegrated systems the reader is referred to Johansen [1988] and L¨utkepohl [2006, Chapter 6]. The following result is a useful corollary of Theorem 1. 

Corollary 1. If {yt} is generated from model (6)-(7) with φ1 = 1, |φ2| < 1, V1t = V12,t = 0, then {yt} is mean reverting if |Bt| < 1, for all t ≥ t0, for some t0 > 0, where Vt = (Vij,t). 

The proof of this corollary follows by combining the proofs of (a) and (b) of Theorem 1 (see the appendix). Corollary 1 gives an important case, in which At = A, for all t as in Elliott et al. [2005], but Bt changes according to a weakly stationary AR model. This can be used when it is expected that At will be approximately constant and benefit may be gained by reducing the tuning of the four parameters φ1, φ2, δ1, δ2 to tuning of two parameters φ2, δ2. For a further discussion on this topic see Sections 4.4 and 5. 

In this paper we propose (5) as a flexible time-varying model for the observed spread. However, more general time-varying autoregressive models may be used. Consider that yt is generated from a time-varying AR model of order d, i.e. 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0010-04.png)


and the time-varying AR parameters At and Bit follow first order AR models, as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0010-06.png)


where d is the order or lag of the autoregression, the innovations ǫt and νit are individually and mutually uncorrelated and they are uncorrelated with the initial states Ad and Bid. Certain Gaussian distributions may be assumed on ǫt and νit and on the states At and Bit. It is readily 

10 

seen that this model can be casted in state space form (6) with Ft = (1, yt−1, . . . , yt−d)[′] , θt = (At, B1t, . . . , Bdt)[′] and Φ = diag(φ1, . . . , φd+1) (the diagonal matrix with diagonal elements φ1, . . . , φd+1). It is clear that model (5) is a special case of model (8) with d = 1. When the general model is adopted, the conditions of mean reversion of {yt} of Theorem 1 need to be revised, as follows. For φi (i = 1, . . . , d + 1) being inside the unit circle, for t > t0, all (time-dependent) solutions of the autoregressive polynomial ψ(x) = 1 −[�][d] i=1[B][it][x][i][must][lie] outside the unit circle. This effectively means that after some t0, {yt} is locally stationary [Dahlhaus, 1997]. For the remainder of this paper, we consider the situation of d = 1, i.e. model (5), as this is a simple and parsimonious model. 

## 3.3 A Bayesian framework 

We adopt a Bayesian formulation that, within the realm of conjugate analysis, allows us to derive fast recursive estimation procedures and naturally compute measures of uncertainty. The analysis we propose in this section has roots in the work of West et al. [1999], Prado and Huerta [2002], and Triantafyllopoulos [2007a]. Initially, we assume that, given the observational variance σ[2] , the initial state θ1 follows a bivariate Gaussian distribution with mean vector m1 and covariance matrix σ[2] P1. Also, we place an inverted gamma density prior with parameters n1/2 and d1/2 on σ[2] . In summary, the prior structure is specified as follows 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0011-03.png)


where m1, P1, n1, d1 are assumed known; we comment on their specification in Section 4.4. Note that, unconditionally of σ[2] , the initial state θ1 follows a Student t distribution. 

With these priors in place, the posterior distribution of θt|σ[2] and the predictive distribution of yt|σ[2] are routinely obtained by the Kalman filter. We elaborate more on this as follows. First, assume that at time t − 1 the posteriors are given by θt−1|σ[2] , y[t][−][1] ∼ N2(mt−1, σ[2] Pt−1) and σ[2] |y[t][−][1] ∼ IG(nt−1/2, dt−1/2), for some mt−1, Pt−1, nt−1 and dt−1. Here the notation y[t] means that all data points observed up to time t are included. Then, writing the likelihood function (or evidence) for an observation yt as p(yt|θt, σ[2] ), an application of the Bayes theorem gives 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0011-06.png)


11 

It follows that the posterior density of θt|σ[2] is Gaussian, and specifically 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0012-01.png)


The recurrence equations for updating mt and Pt are provided in Section 4. The probability density p(yt|σ[2] , y[t][−][1] ) refers to the one-step ahead forecast density, which is obtained from the prior p(θt|σ[2] , y[t][−][1] ) as yt|σ[2] , y[t][−][1] ∼ N (ft, σ[2] Qt). Again, see Section 4 below for recursive equations needed to update ft and Qt. 

The posterior distribution of σ[2] is also obtained by an application of the Bayes theorem, 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0012-04.png)


which gives an inverted gamma density σ[2] |y[t] ∼ IG(nt/2, dt/2), depending on parameters nt and dt. Here yt|y[t][−][1] follows a t distribution with nt−1 degrees of freedom yt|y[t][−][1] ∼ t(nt−1, ft, QtSt−1), with St−1 = dt−1/nt−1. 

From the density p(θt|σ[2] , y[t] ), the posterior distribution of θt, unconditionally of σ[2] , is easily obtained by integrating σ[2] out; it It then follows that θt|y[t] ∼ t2(nt, mt, PtSt). From this the (1 − γ)% marginal confidence interval of Bt is 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0012-07.png)


where mt = (m1t, m2t)[′] , Pt = (Pij,t)ij=1,2 and tγ denotes the 100γ% quantile of the standard t distribution with nt degrees of freedom. The (1 − γ)% confidence interval for xt+1 is 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0012-09.png)


and the (1 − γ)% confidence interval for yt+1 is 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0012-11.png)


where the recurrence relationships of Rt+1 and Qt+1 are given below. 

Some references on related time series models are in order. From a frequentist perspective, time varying AR models have been discussed in Dahlhaus [1997], Francq and Zakoan [2001], Francq and Gautier [2004] and Anderson and Meerschaert [2005]. Among other works, recursive estimation of time varying autoregressive processes in a nonparametric setting is discussed in Moulines et al. [2005] and, for non Gaussian processes, in Djuri´c et al. [2002], using particle filters. Standard Bayesian AR models have been developed since the early 70’s, see e.g. 

12 

Zellner [1972], Monahan [1983], Kadiyala and Karlsson [1997] and Ni and Sun [2003]. Free software for model estimation is widely available[1] . 

## 4 On-line estimation 

## 4.1 An adaptive and recursive algorithm using discount factors 

In this section we provide the updating equations needed to compute the posterior densities of θt|y[t] and of σ[2] |y[t] at each time step. Starting at time t = 1 with a quadruple of initial values (m1, P1, n1, d1), the calibration algorithm then proceeds as follows: 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0013-04.png)


For any t = 2, . . . , T , the above algorithm estimates the target posterior quantities of interest; for instance, we can extract posterior and predictive mean and variances, as well as relevant quantiles and credible bounds of θt and σ[2] . From θt = (At, Bt)[′] and the posterior distribution of θt|y[t] , we can extract the posterior distribution of Bt|y[t] . The condition for mean-reversion established in Theorem 1 can be monitored recursively by extracting the posterior mean of Bt|y[t] , say B[ˆ] t, and assessing whether |B[ˆ] t| is strictly less than one. Credible bounds can also be associated to the posterior mean in order to better assess the possibility that the process is still mean-reverting – see the examples in Section 5. 

The full specification of algorithm (10) requires the selection of a covariance matrix Vt, which is responsible for the stochastic evolution of the signal θt and hence the stochastic change of At and Bt. Following West and Harrison [1997, Chapter 6] we advocate a practical and convenient analytical solution which allows us to learn this variance component directly from the data in a sequential way by means of two discount factors, δ1 and δ2; this is referred to as component discounting. The idea is that by assuming P1 and Vt to be diagonal matrices we can use the two discount factors to discount the precision of the updating of the mean and 

> 1Time-varying AR models are implemented in the computing language R (website: http://cran.r-project.org/) via the contributed package timsac. S-plus, Fortran and Matlab routines for the implementation of these models can be downloaded from the website of Mike West (http://www.stat.duke.edu/research/software/west/tvar.html) 

13 

the variance of θt as we move from time t − 1 to t. In other words we use δ1 and δ2 to specify the covariance matrix Vt as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0014-01.png)


where Pt = (pij)i,j=1,2. This implies that Rt = diag(φ[2] 1[p][11][,t][−][1][/δ][1][, φ][2] 2[p][22][,t][−][1][/δ][2][)][and][thus,][as] we move from t − 1 to t, the prior variance of At is increased by a factor of 1/δ1 and of Bt by a factor of 1/δ2. Of course if δ1 = δ2 = 1, then Vt = 0 and in this case θt carries no stochastic evolution. If we allow δ1 = 1 and δ2 < 1, then only Bt has stochastic evolution over time. 

## 4.2 Model comparison and model assessment 

The performance of the estimation procedure of Sections 3.3 and 4 can be formally evaluated using model diagnostic and model comparison tools; see, for instance, Li [2004] for a general exposition of time series diagnostics and Harrison and West [1991] for diagnostics in state space models. In this section we briefly discuss three diagnostic tools, namely the mean of the squared standardized forecast errors (MSSE), the likelihood function, and sequential Bayes factors. 

From the Student t distribution of yt|y[t][−][1] , i.e. yt|y[t][−][1] ∼ t(nt−1, ft, QtSt−1), we can define the standardized one-step forecast errors (or standardized residuals) as ut = Q[−] t[1][S] t[−] −[1] 1[(][y][t][−][f][t][),] so that ut|y[t][−][1] ∼ t(nt−1, 0, 1) (the standard t distribution with nt−1 degrees of freedom). We can therefore construct diagnostics and outlier detection tools based on the above t distribution of ut. Writing vt = (1 − 2n[−] t−[1] 1[)][u][t][we][have][E][(][v] t[2][|][y][t][−][1][) = 1][and][so][the][MSSE][is][defined][as] (T − 1)[−][1][ �][T] t=2[v] t[2][,][which][if][the][model][fit][is][good,][should][be][close][to][1.] 

From the Student t distribution of yt|y[t][−][1] the log-likelihood function of φ1, φ2, δ1, δ2 based on data y[T] = {y2, . . . , yT } is 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0014-07.png)


where Γ(.) denotes the gamma function. Model camparison can be carried out by using either one of the following criteria: likelihood function, Akaike’s information criterion (AIC) and Bayesian information criterion (BIC) . In particular, we can choose optimal values of some or 

14 

all of the hyperparameters φ1, φ2, δ1, δ2 by maximizing ℓ(.). A discussion on the specification of the hyperparameters of the model can be found in Section 4.4. 

For the application of the above diagnostic criteria, all data y[T] is needed to be available, or historical data can be used. However, sometimes it is useful to construct sequential diagnostics so that the model can be assessed and updated over time in an adaptive way. Such diagnostics tools include sequential likelihood ratios and sequential Bayes factors. Here we briefly discuss the latter, the foundations of which are discussed in detail in West and Harrison [1997, Chapter 11]. Suppose that, given a sample y[T] = {y1, . . . , yT } we have two candidate models of the form of (6) that is they have the same structural form, but they may differ in the values of φ1, φ2, δ1 and δ2. Suppose that we denote the two models by M1 and M2 and for i = 1, 2 we write φi1, φi2, δi1 and δi2 to indicate the dependence of model Mi in these parameters. Then the Bayes factor of M1 versus M2 is given by the ratio of their respective one-step forecast densities, i.e. 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0015-02.png)


where we have used that yt|y[t][−][1] , Mi ∼ t(nt−1, fit, QitSi,t−1), with the quantities fit, eit, Qit, Si,t−1 being appropriately indexed by i = 1, 2. Given data y[T] one can either judge the performance of the two models sequentially (by comparing Ht to 1, for 2 ≤ t ≤ T ) and thus arriving to a sequential monitoring of the two models, or use the entire data set y[T] to compare the models globally, e.g. one can extract the mean or other features of the empirical distribution of {Ht}. 

## 4.3 Convergence analysis 

Algorithm (10) is quite similar to the celebrated Kalman filter; conditional on σ[2] , the algorithm exactly reduces to the Kalman filter, but the full algorithm allows for the estimation of σ[2] that results in the Student t posterior distribution for θt. On the performance of the Kalman filter, Elliott et al. [2005] state that the posterior covariance matrix of the parameters converges to stable values and this has important implications on the stability of the state process {xt}. Indeed, it is well known that if the parameters of a state space model are constant, then the posterior covariance matrix of the states converges to a stable value; see, for instance, Harvey [1989, p. 119] as well as Chan et al. [1984], Triantafyllopoulos [2007b]. 

15 

However, the performance of the posterior covariance matrix Pt when the components of the model are made time-dependent has not been investigated; in our system this is conveyed via the time-varying vector Ft = (1, yt−1)[′] . This aspect is important as instability or divergence of Pt could result in instability of the estimation of At and Bt and hence of xt. The next result states that, in our system, Pt converges to stable values and we provide an explicit formula for the computation of the limit of Pt. 

Theorem 2. Suppose that {yt} is generated from model (6). If {yt} is mean reverting and if, for j = 1, 2, it is δj < φ[2] j[,][then][as][t][ →∞][the][limit][P][of][the][covariance][matrix][P][t][=][ Var][(][θ][t][|][y][t][)] exists and it is given by P = diag(p11, p22), where 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0016-02.png)


with a1,t = 1 and a2,t = yt[2] −1[.] 

Some comments are in order. First we note that if φ1 = φ2 = 1 and Vt = 0 (we have already seen that this setting reduces the model to the time-invariant AR model considered in Elliott et al. [2005]), then the condition δj < φ[2] j[is][satisfied][for][all][values][of][δ][j][,][since] 0 < δj < 1. 

From the mean reversion assumption of {yt}, if we write yt ≈ µ, where µ denotes the equilibrium mean of the spread, then we can write the limit covariance matrix P as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0016-06.png)


In the important special case of φ1 = δ1 = 1, for which At = A is time-invariant, we can easily see that 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0016-08.png)


where p11,1 is the prior variance Var(A). 

The convergence rate of the limit of Theorem 2 is geometric, since after some appropriately large tL, we can write yt ≈ µ, for all t > tL and the limit of P depends on a geometric series. 

The above convergence results for Pt are given conditional on the variance σ[2] . Given data up to time t, σ[2] has a posterior inverted gamma distribution σ[2] |y[t] ∼ IG(nt/2, dt/2); hence, 

16 

as the time index gets larger, the variance of σ[2] , which is given by 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0017-01.png)


converges to 0. Therefore, as t →∞, σ[2] concentrates about its mode St = dt/nt asymptotically degenerating. 

## 4.4 Hyperparameter specification 

The estimation algorithm (10) relies upon the specification of prior distributions and corresponding starting values (m1, P1, n1, d1) and values of the model components (φ1, φ2, δ1, δ2), which are selected by the user. In this brief section, considering weakly informative priors, we provide some guidance on how to choose these values. Of course, depending on the specific application, other specifications may be preferred; for instance, the analyst may want to include stronger prior beliefs regarding the spread being traded, see e.g. Kadane et al. [1996]. Nevertheless, it is important to note that, given a reasonable amount of data, the sensitivity of the calibration procedure on these initial specifications becomes negligible, especially over streaming data, because the initial information is deflated over time. This phenomenon is discussed in some detail in Ameen and Harrison [1984] and in Triantafyllopoulos [2007a]. Detailed studies on prior specification for the estimation of AR models can be found in Kadiyala and Karlsson [1997], Ni and Sun [2003] and in references therein. 

The parameter m1 is the prior mean of the hidden state, given the observational variance, i.e. the mean of θ1|σ[2] . A common choice is to set m1 equal to our prior expectation of (A1, B1)[′] , which may be obtained from the availability of historical data. In all examples of Section 5 we have used m1 = (0, 0)[′] . This setting together with the vague prior P1 that follows, communicates a prior assumption of mean reversion, but with a large uncertainty placed a priori on (A1, B1)[′] . The convergence results reported in Theorem 2 above, guarantee that the choice of m1 and P1 are not crucial for accurate estimation and forecasting. The covariance matrix P1 is chosen to be proportional to the 2 × 2 identity matrix, i.e. P1 = p1I2. Here a large value of p1 reflects a weakly informative or defuse prior specification, since in this case the precision P1[−][1] gets close to zero. Finally, values for n1 and d1 need to be provided. It can be noted that, having placed an inverted gamma prior on σ[2] , the expected value of the observational variance is given by E(σ[2] ) = d1/(n1 − 2), for n1 > 2. Based on this observation, 

17 

a sensible choice is to set n1 = 3 and use the prior expectation of σ[2] as a starting value d1. Historical data may be used to specify d1, but in the examples of Section 5 we have simply used d1 = 1. 

Proceeding now with the specification of φ1, φ2, δ1, δ2 we can optimize these parameters by maximizing the log-likelihood function, given in Section 4.2, under the condition that δi < φ[2] i[so][that][Theorem][2][applies.] Alternatively, according to Corollary 1 we can set φ1 = δ1 = 1 and optimize only φ2 and δ2. In Section 5.1, where we present simulation studies, we use the latter, while in Section 5.2, where we analyze real data, we use the former (full optimization of four parameters). We note that the likelihood function or Bayes factors can be used to compare and optimize models using single discount factors δ1 = δ2, known as single discounting [West and Harrison, 1997], and models using two different discount factors (component or multiple discounting). 

## 4.5 Pairs trading 

Under the assumption that the observed spread process involving two tradable assets is meanreverting, and that the model of Eqs. (2)-(3) describes well its evolution at discrete observational times t = t1, . . . , tN , with N sufficiently small, a simple pairs trading strategy immediately follows [Elliott et al., 2005]. Let us assume that xˆt denotes our best estimate of the hidden state, which is obtained by calibrating the model on data collected in the above data window. 

At each time t, if the observed spread yt is strictly greater than the true state xˆt, then a sensible decision would be to take a long position in this portfolio, with the intention of closing this position at a later time, when the spread has reverted back to its mean. Conversely, if yt < xˆt, the trader may decide to take a short position in the portfolio; this bet is expected to be a profitable one as soon as the spread process corrects itself again. Realistic implementations of this popular strategy may ask for additional layers of sophistication which in turn require the trader to face a few practical questions; some examples are: 

- How can transaction costs be included in this simple model? In other words, when is a trade expected to be profitable, so that an ‘entry’ signal can be generated? For instance, a long position could be initiated when yt − xˆt > zt, where zt is a threshold that guarantees a profitable trade, after costs. The question then becomes, how should 

18 

zt be calibrated? For instance, Vidyamurthy [2004] suggests a re-sampling procedure and provides some general guidance. There may exist several other alternative ways in which one could define entry points, perhaps based on empirical modeling of the extreme values of the yt − xt process. Theoretical results on zero-crossing rates for autoregressive processes, as in Cheng et al. [1995], may also be explored. For aggressive strategies that execute a trade at each single time tick, Montana et al. [2008] forecasts the one-step ahead expected spread using dynamic regression methods, whereas Montana and Parrella [2008] embrace the principle of “learning with experts” to deal with the uncertaincty involved in future movements on the spread. 

- Analogously to the previous issue, how should an ‘exit’ signal be generated? And shall a trade be closed at an exit point, or simply reversed so that a long position becomes short, and viceversa? 

- What stop-loss mechanism can be implemented to make sure that the assumptions on which the strategy relies are still satisfied? Surely, if the spread process is no longer believed to be mean-reverting, a stop-loss signal should be quickly generated. As will appear clearer later (see, for instance, the examples of Section 5), our estimation procedure can be used to monitor mean-reversion sequentially and flag deviations from the acceptable behaviour of the spread process as soon as they occur. Related co-integration arguments may also be used, as in Lin et al. [2006]. 

- How can suitable pairs of assets be chosen in the first place, especially when the universe of assets to search from is extremely large? Since arbitrage profits between two assets depend critically on the presence of a long-term equilibrium between them (see, for instance, Alexander et al. [2002]), data mining methods built around co-integration techniques may be explored, as in d’Aspremont [2008]. See also Vidyamurthy [2004] and Pole [2007] for alternative methods including simple correlation analysis, turning point analysis and latent factor models. 

As a final note, we mention a technique that may be deployed in a dynamic modeling setting, such as ours, to obtain the spread yt = p[(1)] t − βtp[(2)] t in a recursive fashion. As noted before, the regression coefficient is usually estimated on historical data, but on-line procedures such as recursive least squares may also be used. The assumption of a time-invariant 

19 

regression coefficient β could also be released so as to allow β to change slightly over time; such a modification would capture a time-varying co-integration relationship between the two asset prices, where this extension deemed necessary. Assuming T historical observations, a regression model with a time-varying regression coefficient βt minimizes a cost function 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0020-01.png)


where µ ≥ 0 is a scalar determining how much penalization to place on temporal changes in the regression coefficient. When µ is very large, changes in the coefficient are penalized more heavily and, in the limit µ = ∞, the usual OLS estimate is recovered. A solution to the optimization problem above was originally proposed by Kalaba and Tesfatsion [1988]. Following their approach, called flexible least squares (FLS), a recursive estimator for each βt can easily be derived as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0020-03.png)


where we have defined the quantities 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0020-05.png)


The recursions are initially started with some arbitrarily chosen values S1 and s1. Montana et al. [2009] show a clear algebraic connection between FLS and the Kalman filter and use this estimation method to develop a dynamic statistical arbitrage strategy. 

## 5 Illustrations 

## 5.1 Simulated data 

In this section we initially report on a Monte Carlo simulation study demonstrating that the fast recursive algorithm (10) described in Section 3.3 accurately estimates the parameters of the proposed model. We have simulated a large number of time series under model (6) using a range of values for A, B and σ[2] . The true parameters are kept constant in these initial simulations for simplicity, so they can be easily compared with the estimated posterior means. We have found that convergence to the true parameters A, B and σ[2] is quickly achieved and the 

20 

estimated values of these parameters are not sensitive to the initial parameters µ1, P1, n1, d1 (results not shown). 

We have also explored situations in which the parameters are time-varying. First, we have considered the case of a sudden change in the level of the spread; the time series fluctuates around an equilibrium level till t = 1500, and after that time it jumps to a much higher equilibrium. Clearly for 1 ≤ t ≤ 1499 the process is mean reverting, then at t = 1500 it looses mean reversion, but it retains it in the sub-period 1500 ≤ t ≤ 3000; of course the process is not mean reverted for the entire period 1 ≤ t ≤ 3000. Figure 1 shows how the posterior mean of |Bt| is tracked using two different values of the discount factor δ2. Our focus is on monitoring Bt because, as established in Theorem 1, this parameter is the ultimate object of interest. As shown in Figure 1, the algorithm with δ2 = 1 (which corresponds to a model with time-invariant parameters) does not manage to capture the loss of mean-reversion observed at time t = 1500; in fact the algorithm gives the misleading result of mean reversion throughout the time range. On the contrary, when using a smaller discount factor (which corresponds to a model with time-varying parameters), the algorithm tracks the jump almost in real-time and communicates the result that after t = 1500 the process has locally regained mean reversion. 

Furthermore, we have considered a more hypothetical scenario that may be of practical interest: Figure 2 corresponds to a scenario where Bt is piece-wise constant and undergoes a large sudden jump at time t = 1500. Again, the algorithm is able to track well mean reversion locally, although the true parameter Bt may not be estimated very accurately. 

## FIGURES 1-2 AROUND HERE 

## 5.2 Equity data 

In this section we apply our methods to spreads obtained from historical equity data. Each spread is computed using the flexible least squares (FLS) method with a very large µ parameter; this is almost equivalent to ordinary least squares (OLS) regression but allows for recursive estimation. As a simple validation exercise, we also compare the findings obtained from our 

21 

model to formal cointegration tests which assume the availability of all data points. The very first procedure for the estimation of cointegrating regressions, based on OLS, was proposed by Engle and Granger [1987]. Since then several other procedures have been developed including the maximum likelihood method of Johansen [1988, 1991] and the fully modified OLS of Phillips and Hansen [1990]. Hargreaves [1994] lists eleven categories of procedures, and several more have been added in more recent years. For our analysis we have considere only three popular tests: Engle-Granger’s ADF test [Engle and Granger, 1987], Phillips-Perron’s PP test [Perron, 1988] and Phillips-Ouliaris’s PO test [Phillips and Ouliaris, 1990]. 

The first data sets we present consists of daily share prices of two companies: Exxon Mobil (XOM) and Southwest Airlines (LUV). We have used all the available data for this pair of stocks, which spans a period from March 23, 1980 to August 6, 2008. Figure 3 reports the estimated posterior mean of Bt and its confidence band for the period March 23, 1980 to November 30, 2004. Clearly, from March 23, 1980 till November 8, 2004 the posterior mean of |Bt| stays below one, which according to Theorem 1 indicates mean-reversion of the spread time series. Figure 4 shows the observed spread time series as well as the estimated hidden state process and its posterior confidence band for this subperiod of the data. For the estimation of (At, Bt)[′] we have used φ1 = 0.1, φ2 = 99839, δ1 = 0.992 and δ2 = 0.995 that maximize the log-likelihood function (11). 

When using all historical data (1980-2008), all three standard cointegration tests cannot reject the null hypothesis of unit roots (p-values: 0.246, 0.219 and 0.15). This is in agreement with the patterns captured by Figure 3, which reveals that after November 8, 2004, mean reversion is lost. However, when the analysis is restricted to the period November 8, 2004, both the PP and PO tests reject the null hypothesis of unit roots at a 5% significance level (p-values: 0.013 and 0.024, respectively). The ADF test, however, disagrees and does not reject the null hypothesis of unit roots (p-value 0.139). Thus, in this example, only two out of three tests agree with the evidence provided by our on-line monitoring device. 

Our second example illustrates a co-integration relationship existing between two ETFs operating in the commodity market. ETFs are relatively new financial instruments that have exploded in popularity over the last few years. They are securities that combine elements of both index funds and stocks: like index funds, they are pools of securities that track specific market indexes at a very low cost; like stocks, they are traded on major stock exchanges and 

22 

can be bought and sold anytime during normal trading hours. We have collected historical time series for the SPDR Gold Shares (GLD) and Market Vectors Gold Miners (GDX) ETFs. GLD is an ETF that tries to reflect the performance of the price of gold bullion, whereas GDX tries to replicate as closely as possible, before fees and expenses, the price and yield performance of the AMEX Gold Miners index. This is achieved by investing in all of the securities which comprise the index (in proportions given by their weighting in the index). This analysis is based upon all the historical data available for the pair, which covers a shorted period compared to the previous example, from May 23, 2006 until August 06, 2008. Figure 5 shows the observed spread process jointly with the estimated hidden process and confidence bands, while Figure 6 indicates that a co-integrating relationship between the two ETFs does exist in the period from July 19, 2006 till 17 December, 2007. For this data set we have used φ1 = 0.999, φ2 = 99, δ1 = 0.95 and δ2 = 0.98 that maximize the log-likelihood function (11). 

When all the historical data is used, the ADF and the PP tests indicate the presence of cointegration at a 5% significance level (p-values: 0.01 and 0.01, respectively) and only the PO test suggest lack of co-integration, a result that also agrees with the pattern reported in Figure 6. Considering the period July 19, 2006 till 17 December, 2007, for which our results suggest mean reversion, we find that all three tests also suggest co-integration (p-values: 0.0201, 0.013 and 0.012). Further formal comparisons and more detailed studies will be needed in order to characterize some of the discrepancies; however, based on this empirical evidence, our suggested time-varying model seems to generally agree with most formal cointegration tests. 

## FIGURES 3-6 AROUND HERE 

## 6 Conclusions 

In this paper we have proposed a Bayesian time-varying autoregressive model, expressed in time-space form, and an efficient recursive algorithm based on forgetting or discount factors. The procedure can be used for real-time estimation and tracking of the underlying spread 

23 

process and may be seen as a more efficient alternative to standard iterative MLE procedures such as the EM algorithm. Conditions for mean-reversion as well as the convergence properties of the on-line estimation algorithm have been studied analytically and discussed. The model seems particularly useful for monitoring mean-reversion using financial data streams and as a building block for statistical arbitrage strategies such as pairs trading. Related algorithmic trading strategies that exploit co-integration of financial instruments, for instance index arbitrage [Sutcliffe and Board, 2006] and enhanced index tracking [Alexander et al., 2002], may also benefit from the methods proposed here. Moreover, although the focus of this work has been on applications in computational finance, we believe that the methods described here are of broader interest and may appeal to other users, within the management science community, who need to model and monitor mean-reverting time series arising in different application domains 

There are several aspects of the suggested methodology that we would like to explore further in future work. First, purely from an empirical point of view, we would like to better understand how the methodology relates to more formal statistical procedures for testing the hypothesis of mean reversion based on finite sample sizes. As already mentioned, since mean-reversion is closely linked to second order stationarity, many efforts have been directed to constructing unit root tests. These standard econometric procedures may lack the power to reject the null hypothesis of a random walk, and we feel that our method may at least complement them well. Besides, some of the recently suggested procedures, such as the bootstrap methods described by Li and Xiao [2003], are too computationally expensive to be of any use in the real settings and applications that we have described. Another important aspect that we plan to investigate is the question of how to learn the discounting factors needed to specify the Vt matrix in a more adaptive fashion, so that they become self-tuning, rather than being kept constant at all times. A number of techniques have been successfully used for training adaptive artificial neural networks and other time-varying stochastic processes using forgetting factors [Saad, 1999, Nied´zwiecki, 2000] and there may be scope for improvement along this direction. 

24 

## Acknowledgements 

We would like to thank three anonymous referees for their helpful comments on an earlier draft of the paper. 

## Appendix 

Proof of Theorem 1. With φ1 = φ2 = 1 and Vt = 0, the state space model (6) reduces to the AR model yt = A + Byt−1 + ǫt, where At = A and Bt = B and it is trivial to verify that {yt} is mean reverting if |B1| < 1, see also Section 2. This completes (a). 

Proceeding now to (b), from the AR model for At we note that E(At) = 0. From (6) write yt recursively as 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0025-05.png)


We write A[t] = (A1, . . . , At) and B[t] = (B1, . . . , Bt), for t = 1, . . . , T . Since {ǫt} is white noise, we have 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0025-07.png)


This is a convergent series if |Bt| < 1, for all t > t0, for some positive integer t0. To see this first write x[(1)] t =[�][t] i=2[B][i][,][which][is][a][decreasing][series][as][|][x][(1)] t+1[/x] t[(1)][|][=][|][B][t][+1][|][<][1.][Also] {x[(1)] t[}][is][bounded][as][|][x][(1)] t[|][ =][ �][t] i=2[|][B][i][|][ <][ 1][and][so][{][x][(1)] t[}][is][convergent.] 

For the variance of yt we have 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0025-10.png)


where it is used that 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0025-12.png)


25 

for V11,t ≤ V11, since from the hypothesis Vt is bounded, and so there exists some V11 > 0 so that V11,t ≤ V11. 

Now we show that the series x[(2)] t =[�][t] j[−] =0[3] �ji=0[B] t[2] −i[and][x][(3)] t =[�][t] j[−] =0[3][φ] 1[j][+1] �ji=0[B][t][−][i][are] both convergent. For the former series we note that given |Bt| < 1, we can find some B so that |Bt| < |B| < 1, from which it follows that 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0026-02.png)


which is proportional to a geometric series that converges for |B| < 1 and since x[(2)] t is a positive series, it follows that {x[(2)] t[}][is][convergent.] 

For the series x[(3)] t[,][we][follow][an][analogous][argument,][i.e.][for][B][satisfying][|][B][t][|][<][|][B][|][ <][1] we obtain 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0026-05.png)


which shows that x[(3)] t is convergent as[�][t] j[−] =0[3][|][φ][1][B][|][j][+1][is][a][geometric][series][with][|][φ][1][B][|][<][1] and x[(3)] t is a positive series. 

With these convergence results in place, the convergence of Var(yt|B[t] ) is obvious. Given, B[t] , we have shown that the mean and the variance of {yt} are convergent and so {yt} is mean reverting. 

Proof of Theorem 2. From the diagonal structure of Pt = diag(p11,t, p22,t) and the updating of Pt as in the calibration algorithm (10) we have 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0026-09.png)


We can clearly see that pii,t > 0, for all t and so we have 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0026-11.png)


Now since δi[j][φ][−] i[2][j] ai,t−j is a positive sequence and since from the mean reversion of {yt} and the definition of ait, the above sequence is bounded above by the geometric sequence δi[j][φ][−] i[2][j] M , where M is an upper bound of {yt}, it follows immediately that[�][∞] j=0[δ] i[j][φ][−][2][j][a][i,t][−][j][<][ ∞][and] this proves that pii,t converges to[�][∞] j=0[δ] i[j][φ][−][2][j][a][i,t][−][j][.][The][proof][is][completed][by][inverting] (A-2), noting that pii,t > 0 and[�][∞] j=0[δ] i[j][φ][−][2][j][a][i,t][−][j][>][ 0.] 

26 

## References 

- C. Alexander, I. Giblin, and W. Weddington. Cointegration and asset allocation: A new active hedge fund strategy. Technical Report Discussion Paper 2003-08, ISMA Centre Discussion Papers in Finance Series, 2002. 

- J. R. M. Ameen and P. J. Harrison. Discount weighted estimation. Journal of Forecasting, 3:285–296, 1984. 

- P. L. Anderson and M. M. Meerschaert. Parameter estimation for periodically stationary time series. Journal of Time Series Analysis, 26:489–518, 2005. 

- N. Barberis. Investing for the long-run when returns are predictable. The Journal of Finance, 55(1):225–264, 2000. 

- G. Carcano, P. Falbo, and S. Stefani. Speculative trading in mean reverting markets. European Journal of Operational Research, 163:132–144, 2005. 

- S. W. Chan, G. C. Goodwin, and K. S. Sin. Convergence properties of the riccati difference equation in optimal filtering of nonstabilizable systems. IEEE Transactions on Automatic Control, 29:10–18, 1984. 

- K. Chaudhuri and Y. Wu. Random walk versus breaking trend in stock prices: Evidence from emerging markets. Journal of Banking & Finance, 27:575–592, 2003. 

- X. Cheng, Y. Wu, J. Du, and H. Liu. The zero-crossing rate of pth-order autoregressive processes. Journal of Time Series Analysis, 18(4):355–374, 1995. 

- R. Dahlhaus. Fitting time series models to nonstationary processes. Annals of Statistics, 25: 1–37, 1997. 

- A. d’Aspremont. Identifying small mean reverting portfolios. Technical report, Princeton University, 2008. 

- A. Deaton and G. Laroque. On the behavior of commodity prices. Review of Economic Studies, 59:1–23, 1992. 

27 

- P. M. Djuri´c, J. H. Kotecha, F. Esteve, and E. Perret. Sequential parameter estimation of time-varying non-Gaussian autoregressive processes. EURASIP Journal on Applied Signal Processing, 8:865–875, 2002. 

- R.J. Elliott and V. Krishnamurthy. New finite-dimensional filters for parameter estimation ofdiscrete-time linear gaussian models. IEEE Transactions on Automatic Control, 44(5): – 

- 938 951, 1999. 

- R.J. Elliott, J. van der Hoek, and W.P. Malcolm. Pairs trading. Quantitative Finance, pages 271–276, 2005. 

- R. Engle and C. Granger. Co-integration and error correction: Representation, estimation, and testing. Econometrica, 55(2):251–276, 1987. 

- E. F. Fama and K. French. Permanent and temporary components of stock prices. The Journal of Political Economy, 96(2):246–273, 1988. 

- C. Francq and A. Gautier. Large sample properties of parameter least squares estimates for time-varying ARMA models. Journal of Time Series Analysis, 25:765–783, 2004. 

- C. Francq and J. M. Zakoan. Stationarity of multivariate Markov-switching ARMA models. Journal of Econometrics, 102:339–364, 2001. 

- Z. Ghahramani and G. E. Hinton. Parameter estimation for linear dynamical systems. Technical Report Technical Report CRG-TR-92-2, Department of Computer Science, University of Toronto, 1996. 

- D. Ghosh. Maximum likelihood estimation of the dynamic shock-error model. Journal of Econometrics, 41(1):121–143, 1989. 

- C. Hargreaves. Nonstationary Time Series Analysis and Cointegration, chapter A review of methods of estimating cointegrating reiationships, pages 87–131. Oxford, 1994. 

- P. J. Harrison and M. West. Dynamic linear model diagnostics. Biometrika, 78:797–808, 1991. 

- A. Harvey. Forecasting, Structural Time Series Models and the Kalman Filter. Cambridge University Press, 1989. 

28 

- S. Johansen. Statistical analysis of cointegration vectors. Journal of Economic Dynamics and Control, 12:231–255, 1988. 

- S. Johansen. Estimation and hypothesis testing of cointegration vectors in gaussian vector autoregression models. Econometrica, 59:1551–1580, 1991. 

- P. Jorion and R.J. Sweeney. Mean reversion in real exchange rates: Evidence and implications for forecasting. Journal of International Money and Finance, 15(4):535–550, 1996. 

- J. B. Kadane, N. H. Chan, and L. J. Wolfson. Priors for unit root models. Journal of Econometrics, 75:99–111, 1996. 

- K. R. Kadiyala and S. Karlsson. Numerical methods for estimation and inference in Bayesian VAR-models. Journal of Applied Econometrics, 12:99–132, 1997. 

- R. Kalaba and L. Tesfatsion. The flexible least squares approach to time-varying linear regression. Journal of Economic Dynamics and Control, 12(1):43–48, 1988. 

- R. E. Kalman. A new approach to linear filtering and prediction problems. Journal of Basic Engineering, 82:35–45, 1960. 

- H. Li and Z. Xiao. Bootstrapping cointegrating regressions using blockwise bootstrap methods. Journal of Statistical Computation and Simulation, 73(15):775–789, 2003. 

- W. K. Li. Diagnostic Checks in Time Series. Chapman and Hall, 2004. 

- Y. Lin, M. McCrae, and C. Gulati. Loss protection in pairs trading through minimum profit bounds: A cointegration approach. Journal of Applied Mathematics and Decision Sciences, pages 1–14, 2006. 

- H. L¨utkepohl. New Introduction to Multiple Time Series Analysis. Springer, 2006. 

- G. L. McLachlan and T. Krishnan. The EM Algorithm and Extensions. Wiley Series in Probability and Statistics. Wiley, 1997. 

- R. J. Meinhold and N. D. Singpurwalla. Understanding the Kalman filter. The American Statistician, 37(2):123–127, 1983. 

29 

- J. F. Monahan. Fully Bayesian analysis of ARMA time series models. Journal of Econometrics, 21:307–331, 1983. 

- G. Montana and F. Parrella. Learning to trade with incremental support vector regression experts. In E. Corchado and W. Abraham, A. amd Pedrycz, editors, Lecture Notes in Computer Science, pages 591–598. Springer-Verlag, 2008. 

- G. Montana and F. Parrella. Data mining for algorithmic asset management. In L. Cao, P. S. Yu, C. Zhang, and H. Zhang, editors, Data Mining for Business Applications, pages 283–295. Springer US, 2009. 

- G. Montana, K. Triantafyllopoulos, and T. Tsagaris. Data stream mining for market-neutral algorithmic trading. In Proceedings of the ACM Symposium on Applied Computing, pages 966–970, 2008. 

- G. Montana, K. Triantafyllopoulos, and T. Tsagaris. Flexible least squares for temporal data mining and statistical arbitrage. Expert Systems with Applications, 36(2):2819–2830, 2009. 

- E. Moulines, P. Priouret, and F. Roueff. On recursive estimation for time varying autoregressive processes. Annals of Statistics, 33(6):2610–2654, 2005. 

- S. Ni and D. Sun. Noninformative priors and frequentist risks of Bayesian estimators of vector-autoregressive models. Journal of Econometrics, 115:159–197, 2003. 

- M. Nied´zwiecki. Identification of time-varying processes. Wiley, 2000. 

- P. Perron. Trends and random walks in macroeconomic time series. Journal of Economic Dynamics and Control, 12:297332, 1988. 

- P. C. B. Phillips and S. Ouliaris. Asymptotic properties of residual based tests for cointegration. Econometrica, 58:165193, 1990. 

- P.C.B Phillips and B.E. Hansen. Statistical inference in instrumental variables regression with I(1) process. Review of Economic Studies, 57:99–125, 1990. 

- A. Pole. Statistical Arbitrage. Algorithmic Trading Insights and Techniques. Wiley Finance, 2007. 

30 

- J. M. Poterba and L. H. Summers. Mean reversion in stock prices: evidence and implications. Journal of Financial Economics, 22(1):27–59, 1988. 

- R. Prado and G. Huerta. Time-varying autoregressions with model order uncertainty. Journal of Time Series Analysis, 23:599–618, 2002. 

- D. Saad, editor. On-Line Learning in Neural Networks. Number 17 in Publications of the Newton Institute. Cambridge, 1999. 

- R. H. Shumway and D. S. Stoffer. An approach to time series smoothing and forecasting using the em algorithm. Journal of Time Series Analysis, 3(4):253–264, 1982. 

- C.M. Sutcliffe and J. Board. Encyclopedia of Financial Engineering and Risk Management, chapter Index arbitrage. Fitzroy Dearborn, 2006. 

- K. Triantafyllopoulos. Covariance estimation for multivariate conditionally Gaussian dynamic linear models. Journal of Forecasting, 26:551–569, 2007a. 

- K. Triantafyllopoulos. Convergence of discount time series dynamic linear models. Communications in Statistics – Theory and Methods, 36:2117–2127, 2007b. 

- G. Vidyamurthy. Pairs Trading. Wiley Finance, 2004. 

- M. West and P. J. Harrison. Bayesian Forecasting and Dynamic Models. Springer-Verlag New York, 2nd edition, 1997. 

- M. West, R. Prado, and A. D. Krystal. Evaluation and comparison of EEG traces: latent structures in nonstationary time series. Journal of the American Statistical Association, 94:375–387, 1999. 

- A. Zellner. An Introduction to Bayesian Inference in Econometrics. Wiley, New York, 1972. 

31 

## Posterior Estimation of |Bt| 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0032-01.png)


**----- Start of picture text -----**<br>
δ =0.98<br>δ =1<br>0 500 1000 1500 2000 2500 3000<br>time<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>**----- End of picture text -----**<br>


Figure 1: Estimation of |Bt| for the simulated spread with a jump at t = 1500. We have chosen a prior P1 = 1000I2. A value of δ1 = δ2 = δ = 1, which corresponds to the adoption of a time-invariant model, fails to capture mean-reversion following immediately after the change of equilibrium ar time t = 1501. However, forgetting factors δ1 = 1 and δ2 = δ = 0.98 tracks the abrupt change in mean level and and following quick restoration of mean-reversion. 

32 

## Posterior Estimation of |Bt| 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0033-01.png)


**----- Start of picture text -----**<br>
δ =0.98<br>δ =1<br>0 500 1000 1500 2000 2500 3000<br>time<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>**----- End of picture text -----**<br>


Figure 2: Estimation of abruptly varying Bt; shown is the posterior mean of |Bt|. The real parameters are A = 0.2, Bt = 0.25 and σ[2] = 1, for 1 ≤ t ≤ 1500; A = 0.2, Bt = 1 and σ[2] = 1, for 1501 ≤ t ≤ 3000. We have chosen a prior P1 = 1000I2 and δ1 = 1. Two selected values of δ2 = δ are used, δ = 1 and δ = 0.98. 

33 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0034-00.png)


**----- Start of picture text -----**<br>
XOM−LUV Spread: Posterior Estimation of |Bt|<br>**----- End of picture text -----**<br>



![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0034-01.png)


**----- Start of picture text -----**<br>
1.0<br>0.5<br>0.0<br>posterior mean<br>−0.5<br>95% confidence band<br>1985 1990 1995 2000 2005<br>time<br>**----- End of picture text -----**<br>


Figure 3: Posterior estimation of |Bt|. We have used φ1 = 0.1, φ2 = 99839, δ1 = 0.992, δ2 = 0.995 and a prior P1 = 1000I2. 

34 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0035-00.png)


**----- Start of picture text -----**<br>
XOM−LUV Spread<br>10<br>5<br>0<br>−5 observed process<br>state process<br>95% confidence band<br>2000 2001 2002 2003 2004 2005<br>time<br>**----- End of picture text -----**<br>


Figure 4: Observed spread and state spread using a recursive regression routine for on-line spread availability. 

35 

## GDX−GLD Spread 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0036-01.png)


**----- Start of picture text -----**<br>
5<br>0<br>−5<br>observed process<br>state process<br>95% confidence band<br>2006 2007 2008<br>time<br>**----- End of picture text -----**<br>


Figure 5: Observed spread and state spread using a recursive regression routine for on-line spread availability. 

36 

GDX−GLD Spread: Posterior Estimation of |Bt| 


![](markdown_output/Dynamic_modeling_of_mean-reverting_spreads_for_statistical_images/Dynamic_modeling_of_mean-reverting_spreads_for_statistical.pdf-0037-01.png)


**----- Start of picture text -----**<br>
1.0<br>0.5<br>0.0<br>−0.5<br>posterior mean<br>95% confidence band<br>−1.0<br>2006 2007 2008<br>time<br>**----- End of picture text -----**<br>


Figure 6: Posterior estimation of |Bt|. We have used φ1 = 0.999, φ2 = 99, δ1 = 0.95, δ2 = 0.98 and a prior P1 = 1000I2. 

37 

