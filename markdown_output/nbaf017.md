_Journal of Financial Econometrics_ , 2025, **23(4)** , nbaf017 https://doi.org/10.1093/jjfinec/nbaf017 **Article** 

**==> picture [64 x 52] intentionally omitted <==**

## **Loss-Based Bayesian Sequential Prediction of Value-at-Risk with a Long-Memory and Non-Linear Realized Volatility Model** 

## **Rangika Peiris 1, Minh-Ngoc Tran 1, Chao Wang 1, and Richard Gerlach[1]** 

1Discipline of Business Analytics, The University of Sydney Business School, Sydney, NSW 2006, Australia 

Address correspondence to Chao Wang, Discipline of Business Analytics, The University of Sydney Business School, Corner of Abercrombie Street and Codrington Street, Darlington NSW 2006, Australia, or e-mail: chao.wang@sydney.edu.au. 

## **Abstract** 

A long-memory and non-linear realized volatility model class is proposed for direct Value-at-Risk (VaR) forecasting. This model, referred to as RNN-HAR, extends the heterogeneous autoregressive (HAR) model, a framework known for efficiently capturing long memory in realized measures, by integrating a Recurrent Neural Network (RNN) to handle the non-linear dynamics. Quantile loss-based generalized Bayesian method with Sequential Monte Carlo is employed for model estimation and sequential prediction in RNN-HAR. The empirical analysis is conducted using daily closing prices and realized measures with around 12 years of data till 2022, covering 31 market indices. The proposed model’s one-step-ahead VaR forecasting performance is compared against a basic HAR model and its extensions. The results demonstrate that the proposed RNN-HAR model consistently outperforms all other models considered in the study. The implementation code of the HAR-RNN model is publicly available on GitHub: https://github.com/chaowang-usyd/RNN-HAR. 

**Keywords:** HAR model, recurrent neural network, quantile score, sequential Monte Carlo, generalized Bayesian method **JEL classifications:** C58, C32, G32 

Volatility forecasting plays a fundamental role in financial markets for regulators and practitioners in risk management and asset pricing. Accurate predictions of market volatility are vital in setting capital reserves, pricing derivatives, and managing investment portfolios. The ability to anticipate market fluctuations can significantly enhance decision-making processes and mitigate financial risks. 

Traditionally, parametric models, such as the Generalized Autoregressive Conditional Heteroskedasticity (GARCH) and stochastic volatility (SV), are employed to forecast financial market volatility. GARCH, introduced by Engle (1982) and Bollerslev (1986), captures time-varying volatility by modeling the conditional variance as a linear function of past 

**Received:** August 17, 2024. **Revised:** July 11, 2025. **Editorial decision:** July 16, 2025. **Accepted:** July 23, 2025 © The Author(s) 2025. Published by Oxford University Press. All rights reserved. 

For commercial re-use, please contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be obtained through our RightsLink service via the Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com. 

**2** _Journal of Financial Econometrics_ 

variances and squared returns. These models have proven effective and remain a staple in the volatility literature (Taylor 2008). 

However, traditional models do not include high-frequency intraday data, nor stylized features such as long-range dependence in volatility, so-called long memory (Cont 2001). For the latter, the Fractionally Integrated GARCH of Baillie et al. (1996) is influential, incorporating fractional differencing to capture long memory. Whilst effective, these longmemory models often present estimation challenges and lack parsimony, making them less practical for widespread use (Tsay 2010), nor do they fully utilize high-frequency data. 

High-frequency intraday data provide a granular view of market movements, offering richer information on volatility, compared to daily or lower-frequency data, and allow construction of efficient realized measures of volatility, such as realized variance (RV, Andersen and Bollerslev 1998, Andersen et al. 2003). Traditional models do not leverage the richness of high-frequency data. This gap led to the development of models that explicitly incorporate this data, for example, the Heterogeneous Autoregressive (HAR) model in Corsi (2008). 

The HAR model addresses the limitations of previous models: it captures long memory by leveraging the information from high-frequency data. It operates as an additive cascade model, decomposing volatility into components influenced by different market participants’ actions. Although not formally a long-memory model, the HAR model effectively captures volatility persistence, and other stylized facts, observed in financial data. Its original formulation, using RV and ordinary least squares for estimation, can be extended to capture non-Gaussianity, spikes/outliers, and conditional heteroskedasticity (Clements and Preve 2021). Section 1.1 provides a review of HAR and its extensions. 

While HAR models are effective in predicting RV, applications in financial risk management often necessitate forecasting Value-at-Risk (VaR). VaR is indispensable for assessing and managing financial risk in various contexts, and crucial for regulatory compliance and portfolio management strategies; see, for example, Frey and Embrechts (2010) and Christoffersen (2011). Recognizing the practical importance of VaR, our research focuses directly on modeling and forecasting VaR via extending the HAR framework. In addition, although HAR models are effective at modeling volatility dynamics, they face inherent limitations due to their reliance on linear regression frameworks. These models struggle to capture the non-linear dependencies commonly present in financial time series. To address these limitations, recent studies have turned to machine learning techniques to enhance the HAR framework’s forecasting capabilities. For example, Arneri�c et al. (2018) employ Feedforward Neural Networks (FNNs) into HAR type models, to better capture the nonlinear behavior of RV. Further, Christensen et al. (2023), Branco et al. (2024), Pourrezaee and Hajizadeh (2024), Zhang et al. (2022), and Patton and Zhang (2022) demonstrate how machine learning models—such as deep neural networks and stacked machine learning models—can improve volatility and VaR forecasting accuracy. In particular, the Recurrent Neural Networks (RNNs) are frequently used in this work. RNNs are designed for processing sequential data, making them superior to FNNs in the time series forecasting task (Lipton et al. 2015). These advancements underscore the critical role of machine learning and neural network methods in overcoming the traditional limitations of econometric models, also making RNNs a natural choice for our work. 

Recognizing these advancements, this paper’s first contribution makes a significant stride forward, by integrating RNNs into the HAR framework for direct VaR forecasting. To rigorously evaluate the accuracy of our VaR forecasts, we employ quantile scores, which provide a consistent and robust assessment of predictive performance. This choice facilitates a straightforward comparison and validation of our forecasting models, ensuring that our approach meets the stringent demands of risk management practice without making restrictive assumptions about return distributions. Therefore, our work advances the utility 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **3** 

of HAR and RNN models, empowering them to directly and semi-parametrically forecast VaR, avoiding strong assumptions on the return distribution, thereby robustifying the risk modeling and forecasting practice. More precisely, we derive daily, weekly, and monthly effects of realized volatility using three RNN structures, thereby capturing the non-linear and long-term effects of these variances on VaR. We refer to our approach as RNN-HAR. By embedding RNNs within the HAR model, our methodology aims to enhance the accuracy and robustness of VaR predictions. This model forms a hybrid framework, combining machine learning and econometrics, whereby the non-linear RNN technique captures the complex relationships in the data, while the HAR process preserves the meaningful financial and economic interpretability during forecasting. 

Comparing to the existing machine learning and neural network-based approaches in the literature, our approach has distinctive features. Christensen et al. (2023) investigate how various ML techniques work for RV forecasting. Branco et al. (2024) focus on forecasting RV directly, by including all inputs including lagged RV and returns in a NN, whilst we embed the RNN in a model that separates out daily, weekly, monthly RV inputs in a top layer linear framework, allowing us to assess and interpret the significance and effect of these different time-framed inputs, but still allowing them to influence VaR via a RNN. Further, we estimate and forecast VaR directly, not RV, using the quantile loss function (where the information of return is utilized) for parameter estimation, whilst Branco et al. (2024) estimate RV directly and then employ filtered historical simulation to indirectly estimate/forecast VaR. Pourrezaee and Hajizadeh (2024) propose using stacking machine learning methods for the Bitcoin volatility and VaR forecasting. The stacking models include the standard GARCH, HAR and other machine learning models such as neural network, support vector regression, Long Short-Term Memory, and random forest. The VaRs are produced by each individual method and used in the subsequent stacking modelling process, while our approach embeds the RNN component into the HAR framework for direct VaR forecasting. Zhang et al. (2022) utilize temporal convolutional networks to forecast stock volatility, subsequently used to generate VaR forecasts parametrically, and where realized data are not considered. Patton and Zhang (2022) use a neural network for estimating the optimal “bespoke” RVs from high-frequency data, to tailor the estimate of volatility to the application in which it will be used, while the work focuses on forecasting the realized volatility. 

Regarding the model estimation, recent advancements in financial econometrics have leveraged sophisticated statistical estimation techniques to enhance the accuracy of risk forecasting models. This paper’s second contribution is on utilizing the loss-based generalized Bayesian method, in conjunction with Sequential Monte Carlo (SMC) methods, for the RNN-HAR model estimation and prediction. Loss-based Bayesian estimation is invaluable in scenarios where it is challenging to specify the likelihood function; see, for example, Bissiri et al. (2016) and Knoblauch et al. (2019). This approach does not require assumptions on the distribution of the returns, avoiding one potential source of model misspecification. Given the complexity of our proposed RNN-HAR model structure, using SMC for Bayesian estimation and sequential prediction is pivotal, allowing us to handle the inherent challenges of Bayesian computation in sophisticated models such as RNN-HAR. 

In summary, the novelty of this research is twofold. First, via proposing an RNN enhanced HAR framework, we model and predict VaR directly and semi-parametrically, without assuming the distribution of returns. Second, we consider loss-based generalized Bayesian method with SMC for model estimation and prediction. We evaluate the performance of our proposed model against the basic HAR and other extended HAR models, using around 12 years of empirical data till 2022 covering 31 market indices, demonstrating its superior forecasting capabilities. To facilitate readers to access the Bayesian SMC 

**4** _Journal of Financial Econometrics_ 

estimation method and replicate our empirical results, we make the implementation code publicly available on GitHub: https://github.com/chaowang-usyd/RNN-HAR. 

This paper is organized as follows. Section 1 reviews the relevant background models. Section 2 proposes the RNN-HAR model. Bayesian estimation and prediction procedure using SMC is presented in Section 3. Section 4 presents the empirical results. Section 5 concludes the paper. 

## **1 Background** 

This section briefly provides some background on the existing HAR models, the Asymmetric Laplace density-based quantile loss and RNN. 

## 1.1 HAR Type Models 

This section reviews the HAR model and its extensions; we focus on a selection of widely recognized models. These models offer diverse methodologies for capturing volatility dynamics and have been extensively studied in the literature for their efficacy in risk management and forecasting applications. We provide a detailed exposition of each model and its respective formulations. 

The HAR model of Corsi (2008) forecasts future RV based on the past daily, weekly, and monthly RVs: 

**==> picture [336 x 13] intentionally omitted <==**

1 _t −_ 5 where RV _t −_ 1 is the daily RV input. The weekly RV input RV _t −_ 1j _t −_ 5 ¼ 5 P _j_ ¼ _t −_ 1[RV] _[j ]_[is the ] average RV of the stock market index from time _t −_ 1 to time _t −_ 5. The monthly RV input RV _t −_ 1j _t −_ 22 ¼ 221 P _tj_ ¼ _−t_ 22 _−_ 1[RV] _[j ]_[is the average RV of the stock market index from time ] _[t][−]_[1 to ] time _t −_ 22. The coefficients _βd_ , _βw_ , and _βm_ measure how the past daily, weekly, and monthly volatility patterns influence future RVs. Despite its simple architecture, the HAR model empirically achieves highly accurate RV forecasts, which makes it popular among researchers and practitioners. 

The HAR model’s simplicity allows for various extensions, which can enhance its performance in different ways. One approach is applying transformations to realized volatility, which impacts the model’s structure and properties. Corsi et al. (2008) describe the square root transformation of the HAR model (SqrtHAR) as follows: 

**==> picture [315 x 24] intentionally omitted <==**

They show that this SqrtHAR model helps stabilize variance and improve the robustness of volatility forecasts compared to the original HAR model. 

Another approach involves modifying the structure of the model to incorporate additional factors. For instance, Corsi and Reno (2012)� introduce the Leverage HAR (LevHAR) model, which integrates past aggregated negative returns into the HAR model to capture the leverage effect. Following Asai et al. (2012), we only include the negative part of heterogeneous return since the positive part is usually insignificant. Therefore, we use the following definition of LevHAR model as in Asai et al. (2012): 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **5** 

**==> picture [340 x 25] intentionally omitted <==**

where _yt −_ 1j _t − n_ ¼ 1 _n_ P _tj_ ¼ _−tn−_ 1[y] _j_[is the average return of the stock market index from time ] _[t][−]_[1 ] to time _t − n_ , defined under the same manner as weekly and monthly RV. _I_ ½ _x <_ 0� is the indicator function, which takes 1 if _x_ is negative and 0 otherwise. _γ_ 1, _γ_ 2 and _γ_ 3 are the parameters to capture the leverage effect. 

Clements and Preve (2021) explore various ways to improve on the HAR model forecasts. They consider different estimators, data transformation, and combination schemes. These include two weighted least squares schemes and robust regression as estimators, log and square root as transformations, and six combinations of the different estimators and transformations in the empirical study. They conclude that their simple remedies outperform the standard HAR forecasts. Further, they suggest estimating model parameters under a loss function coherent with the final application of the forecasts, such as VaR forecasting. This suggestion lays the foundation for our proposed model. 

## 1.2 The Quantile Loss and Asymmetric Laplace Density 

Koenker and Machado (1999) note that the quantile regression estimator is equivalent to the maximum likelihood estimator based on the Asymmetric Laplace (AL) density with the mode being the quantile. Let _yt_ is the return on day _t_ . Its quantile loss-based AL density is 

**==> picture [295 x 24] intentionally omitted <==**

where _Qt_ is the _α_ -level quantile, _α_ 2 ð0 _;_ 1Þ and _σ_ is the scale parameter. See Taylor (2019) for more details. Although (1.4) is a well-defined density function, we do not assume that _yt_ follows the AL distribution. Instead, we view (1.4) as a loss-based density that allows us to define a likelihood-alike function and then perform the subsequent loss-based generalized Bayesian estimation. Via employing this quantile loss-based AL density in estimation, we avoid the need of specifying probabilistic assumptions about the return distribution, meaning that the proposed RNN-HAR is a semi-parametric risk forecasting framework. Employing the quantile loss also enables our approach to fit into the loss-based generalized Bayesian estimation framework, which represents a paradigm shift in statistical modeling, diverging from traditional methods that rely on parametric likelihood functions and strict distributional assumptions (Bissiri et al. 2016). The details of the estimation method and technical implementation details are shown in Section 3. 

## 1.3 RNN 

RNN and its variants excel at learning and representing non-linear patterns and dependencies of the sequential data. In this paper, we use the basic RNN of Elman (1990), while more sophisticated architectures, such as the Long Short-Term Memory (LSTM) model of Hochreiter and Schmidhuber, could also be employed. 

Let f _Dt_ ¼ ð _xt; yt_ Þ _; t_ ¼ 1 _;_ 2 _;_ ...g be the data with _xt_ the input and _yt_ the output. We use ð _xt; yt_ Þ in this section as a generic notation, not necessarily applicable to the return data in b the other sections. The task is to model the conditional mean _yt_ ¼ Eð _yt_ j _xt; D_ 1: _t −_ 1Þ. The basic RNN model is defined as: 

**==> picture [235 x 10] intentionally omitted <==**

**==> picture [58 x 10] intentionally omitted <==**

**6** _Journal of Financial Econometrics_ 

**Figure 1** Visualization of the model architecture of the proposed RNN-HAR model. Model parameters are highlighted in bold. 

Here, _ϕ_ is an activation function, such as Tanh or Sigmoid, and _ht_ is the hidden state. The important feature of this RNN structure is the hidden state _ht_ , which feeds itself with its lagged value _ht −_ 1 and the current information from the input _xt_ , leading to a mechanism for storing and updating the memory in the data. Our research aims to integrate RNNs within the HAR framework to improve the VaR forecast of the latter. 

## **2 The Proposed RNN-HAR Model** 

The HAR model is well-known for capturing the long memory effects in financial volatility, while RNNs excel in learning intricate patterns and non-linear dynamics from sequential data. In this study, we aim to integrate RNNs into the HAR model, leveraging the strengths of both frameworks. Our RNN-HAR model is specified as follows: 

**==> picture [321 x 13] intentionally omitted <==**

**==> picture [312 x 29] intentionally omitted <==**

**==> picture [314 x 12] intentionally omitted <==**

Figure 1 provides a visualization of the architecture of the proposed RNN-HAR model. The RNN-HAR model produces the VaR forecast at time _t_ , given the information up to time _t −_ 1. It contains three RNNs that produce the daily, weekly and monthly hidden states, _h[d] t_[, ] _[h][w] t_[and ] _[h][m] t_[. The model first computes these states using their lagged values, ] _[h][d] t −_ 1[, ] _h[w] t −_ 1[, ] _[h][m] t −_ 1[, and the daily ] _[RV][t][−]_[1][, weekly ] _[RV][t][−]_[1][j] _[t][−]_[5 ][and monthly ] _[RV][t][−]_[1][j] _[t][−]_[22 ][as inputs. The ] activation function _ϕ_ is selected as the tanh function. These calculations are specified in Equations (2.2)–(2.4). Then, the states _h[d] t_[, ] _[h][w] t_[and ] _[h][m] t_[are aggregated, as in ][Equation (2.1)][, ] to produce the forecast of VaR at time _t_ . As in the standard HAR model, the parameters _βd_ , _βw_ and _βm_ weigh the influence of the past daily, weekly, and monthly volatilities on the future VaR.[1] 

> 1 With only one hidden layer and one hidden unit for the daily, weekly and monthly RNN components, the proposed RNN-HAR already produces significantly improved VaR forecasts compared to existing models, as shown in Section 4. Therefore, we choose to use only one hidden layer and one hidden unit in the paper. 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **7** 

The RNN-HAR model expresses VaR _t_ as a function comprising an intercept and three distinct RNN structures: one for daily, one for weekly, and another for monthly data. This approach explicitly captures the non-linear and long-memory effects that daily, weekly, and monthly realized measures exert on VaR. By integrating RNN and HAR, our proposed model aims to improve the accuracy and robustness of VaR forecasting in the financial markets. Compared to the HAR model in (1.1), our new model introduces two key extensions. First, it employs three RNNs to model the non-linear and long-term dependence relationships between daily, weekly, and monthly RV and VaR. Second, it directly estimates VaR as the _α_ -level quantile of the return distribution, leveraging the AL-based quantile loss function (1.4) for estimation. For parametric models such as GARCH, VaR estimation typically requires an assumption about the return distribution. Avoiding such assumptions enhances statistical robustness. Our approach estimates VaR directly, using the quantile score as the loss function, thereby eliminating the need for a predefined return distribution. 

Compared to the existing HAR type models, the RNN-HAR extends them via incorporating the non-linear neural networks. To more explicitly evaluate the impact of incorporating RNNs, we include the linear VaR-HAR framework for comparison as in (2.5), via modifying the models developed in Chen et al. (2023). The VaR-HAR directly forecasts VaR via the following specification: 

**==> picture [291 x 11] intentionally omitted <==**

In Section 4, we compare our RNN-HAR with the linear VaR-HAR model (2.5), both with the quantile loss, to evaluate the impact of the three RNN components. To further evaluate the role of the non-linear effect captured by the non-linear activation in RNNHAR model, we also test using a linear activation function in the RNN component of RNN-HAR (linear RNN-HAR). 

In summary, our proposed RNN-HAR model addresses several key limitations in existing volatility models. First, it integrates RNNs into the HAR framework, enabling the capture of complex, non-linear dependencies and long-range memory in volatility forecasting. Second, employing the quantile loss function eliminates the need to assume a specific return distribution, overcoming a common limitation of parametric models such as GARCH. Third, instead of forecasting RV, as in the HAR model, we directly estimate VaR, offering a more comprehensive and convenient framework for risk assessment. These contributions highlight the model’s potential to enhance forecasting accuracy and improve risk management strategies in financial markets. The next section details the model estimation process and the sequential forecasting of VaR using the loss-based Bayesian SMC method. 

## **3 Loss-Based Bayesian Estimation and Forecasting** 

Recent advances in Bayesian computation have enhanced and made access to Bayesian approaches easier. In addition to the standard MCMC method, alternative Bayesian estimation techniques, such as Sequential Monte Carlo, have significantly enhanced the accessibility of Bayesian models, even for large-scale applications like Bayesian deep learning. A Bayesian approach also provides a convenient way for expanding-window sequential prediction, as the posterior from the previous time step becomes the prior of the next; see, for example, Nguyen et al. (2022a) and Duan and Fulop (2015). 

In addition, loss-based generalized Bayesian estimation represents a paradigm shift in statistical modeling, diverging from traditional methods that rely on likelihood functions and strict distributional assumptions. See, for example, Bissiri et al. (2016), Knoblauch 

However, more complex RNN architectures with larger hidden units, such as LSTM, could be also explored as interesting future work. 

**8** _Journal of Financial Econometrics_ 

et al. (2019), Matsubara et al. (2021) and Frazier et al. (2025) Unlike classical frameworks where likelihood functions necessitate specific probabilistic assumptions about the data distribution, loss-based Bayesian estimation emphasizes the use of loss functions to guide Bayesian estimation and prediction. This approach is particularly advantageous in scenarios where underlying data distributions are complex or unknown, mitigating potential model misspecification, by offering flexibility and robustness. By focusing on a loss function rather than a likelihood, researchers can tailor models to better reflect real-world uncertainties and variations, by updating beliefs about model parameters in a robust manner, particularly in situations where justifying distributional assumptions about data is challenging. Recent developments, as discussed in Bissiri et al. (2016) and Knoblauch et al. (2019), highlight the use of loss functions in updating beliefs and parameter estimation without restrictive distributional assumptions, thereby enhancing the applicability and reliability of Bayesian models in complex data environments. Li et al. (2023) observe that maximum likelihood-based quantile regression models are sensitive to initial conditions and advocate for a loss-based Bayesian quantile regression approach for estimating joint VaR and ES models. 

Building on these principles and given the AL-based quantile loss in Equation (1.4), we adopt a quantile loss-based Bayesian approach to address the challenge of modeling financial time series and forecasting VaR without presuming a specific return distribution. This method effectively integrates prior knowledge with observed data, facilitating robust and semi-parametric parameter estimation. 

Dealing with the scaling parameters, such as _σ_ in (1.4), can be a non-trivial problem in generalized Bayesian estimation (Knoblauch et al. 2019). Fortunately, for the AL density in (1.4), by adopting an inverse Gamma prior on _σ_ , its full conditional distribution is inverse Gamma. This allows straightforward integration and simplifies the likelihood function in subsequent Bayesian analysis steps. As a result, the posterior distribution of the parameter of interest is obtained without explicit consideration of _σ_ (Gerlach et al. 2011). 

In Bayesian estimation, priors serve as our initial assumptions regarding model parameters before observing any data. Following an exploration of different prior combinations, we opt for a Normal prior with a mean of zero and a variance of 0.01 for the recurrent parameters in our RNN-HAR model. This choice reflects our initial expectation that these parameters are centered around zero with small variability. For the model parameters _β_ 0 _; βd; βw; βm_ , we assume a normal distribution with a mean of 0 and a standard deviation of 1, indicating our initial uncertainty and allowing for exploration across a spectrum of parameter values. 

Integrating loss-based generalized Bayesian estimation into the RNN-HAR framework yields several advantages: providing a coherent method for updating beliefs based on observed data, robustifying estimation for the model parameters, without distributional assumptions on the returns, allowing convenient, efficient prediction based on Sequential Monte Carlo. In Section 4.3, the effectiveness of the proposed loss-based SMC method is evaluated via comparing its performance with the standard optimization routine in Matlab, to empirically demonstrate the advantages of the SMC method. 

## 3.1 Sequential Monte Carlo 

SMC is a powerful tool for Bayesian estimation and sequential prediction; see, for example, Del Moral et al. (2006) and Gunawan et al. (2022). The approach is particularly effective and convenient for volatility modeling and forecasting, where generating sequential expanding-window forecasts is essential. 

SMC uses a set of samples, often called particles, to approximate a sequence of probability distributions. This sequential updating enables efficient estimation of posterior distributions in complex and non-linear models where conventional Monte Carlo methods are 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **9** 

computationally demanding or impractical. SMC allows straightforward expandingwindow one-step-ahead forecast calculations, which makes it particularly useful for volatility forecasting (Nguyen et al. 2022b). These attributes make SMC an attractive approach for Bayesian estimation and sequential forecasting in our RNN-HAR model. To further demonstrate the effectiveness of the loss-based SMC method, in Section 4.3 we have compared the SMC method with the standard optimization routine. 

There are two common SMC approaches in the literature: likelihood annealing and data annealing (Nguyen et al. 2022b). The first approach is designed for sampling from the posterior while the second is for sequential prediction; thus, SMC with likelihood annealing is used for in-sample analysis, and SMC with data annealing is used for out-of-sample forecasting in this paper. We present these two approaches in the following sections. 

## **3.1.1 Likelihood annealing** 

The loss-based generalized posterior distribution in our RNN-HAR model is 

**==> picture [248 x 10] intentionally omitted <==**

where _p_ ð _θ_ Þ is the prior and _p_ ð _y_ 1: _T_ j _θ_ Þ is the loss-based likelihood-alike function derived from (1.4), and _θ_ ¼ f _β_ 0 _; βd; βw; βm; α[d]_ 0 _[;][α]_ 1 _[d][;][α][d]_ 2 _[;][α][w]_ 0 _[;][α][w]_ 1 _[;][α][w]_ 2 _[;][α][m]_ 0 _[;][α][m]_ 1 _[;][α][m]_ 2 _[;][σ]_[g][is the parameter vec-] tor set, which includes all the parameters in RNN-HAR. For sampling from the generalized posterior _π_ ð _θ_ Þ, SMC first samples a set of _M_ weighted particles f _W_ 0 _[j][;][θ][j]_ 0[g] _[M] j_ ¼1[from an easy- ] to-sample distribution _π_ 0ð _θ_ Þ, such as the prior _p_ ð _θ_ Þ, and then traverses these particles through intermediate distributions _πt_ ð _θ_ Þ _; t_ ¼ 1 _;_ ... _; K_ with _πK_ ð _θ_ Þ ¼ _π_ ð _θ_ Þ. In this paper, we set _π_ 0ð _θ_ Þ ¼ _p_ ð _θ_ Þ as it is possible to sample from the prior _p_ ð _θ_ Þ. The likelihood annealing SMC sampler uses the following intermediate distributions 

**==> picture [254 x 10] intentionally omitted <==**

where the _γt_ are referred to as the temperature levels satisfying 0 ¼ _γ_ 0 _< γ_ 1 _< γ_ 2 _<_ ... _< γk_ ¼ 1. Note that the sequence of distributions _πt_ requires the full training data _y_ 1: _T_ to be available. SMC with a likelihood annealing sampler is thus suitable for in-sample analysis. 

Several methods exist to implement SMC in practice; here, we consider the method used by Nguyen et al. (2022b), which uses three main steps: reweighting, resampling, and a Markov move. **Reweighting** : At the beginning of iteration _t_ , the set of weighed particles f _Wt[j] −_ 1 _[;][θ][j] t −_ 1[g] _[M] j_ ¼1 that approximates the intermediate distribution _πt −_ 1ð _θ_ Þ is reweighted to approximate the target _πt_ ð _θ_ Þ. The efficiency of these weighted particles as a representation of _πt_ ð _θ_ Þ is often measured by the effective sample size (ESS) defined in (3.5). 

**Resampling** : The particles are resampled if the ESS is below a pre-specified threshold. 

**Markov Move** : The resulting equally weighted samples are then refreshed by a Markov kernel whose invariant distribution is _πt_ ð _θ_ Þ. 

Following Nguyen et al. (2022b), we choose the tempering sequence _γt_ adaptively to ensure a sufficient level of particle efficiency by selecting the next value of _γt_ such that ESS stays above a threshold. We now present the likelihood annealing SMC sampler, which is adapted from Nguyen et al. (2022b). Note that we do not compute the marginal likelihood estimate as its meaning is not well justified in the generalized Bayesian estimation setting. 

- 1) Sample _θ[j]_ 0[�] _[p]_[ð] _[θ]_[Þ][ and set ] _[W]_ 0 _[j]_[¼][ 1] _[=][M ]_[for ] _[j]_[ ¼][ 1][...] _[M ]_ 

- 2) For _t_ ¼ 1 _;_ ... _; K_ 

   - a) Resampling: Compute the unnormalized weights 

**10** _Journal of Financial Econometrics_ 

**==> picture [338 x 28] intentionally omitted <==**

and set the new normalized weights 

**==> picture [237 x 27] intentionally omitted <==**

b) Compute the effective sample size (ESS) 

**==> picture [245 x 26] intentionally omitted <==**

**if** ESS _< cM_ for some 0 _< c <_ 1, **then** 

- Resampling: Resample from f _θ[j] t −_ 1[g] _[M] j_ ¼1[using the weights ][f] _[W] t[j]_[g] _[M] j_ ¼1[, and then set ] _Wt[j]_[¼][ 1] _[=][M ]_[for ] _[j]_[ ¼][ 1] _[;]_[...] _[;][M]_[, to obtain the new equally-weighted par-] ticles f _θ[j] t[;][W] t[j]_[g] _[M] j_ ¼1[. ] 

- Markov move: For each _j_ ¼ 1 _;_ ... _; M_ move the sample _θ[j] t_[according to ] _[N]_ lik[ran-] dom walk Metropolis-Hasting steps: 

**==> picture [315 x 35] intentionally omitted <==**

**==> picture [236 x 29] intentionally omitted <==**

otherwise keep _θ[j] t_[unchanged.] 

## **end** 

## **3.1.2 Data annealing** 

For out-of-sample expanding-window forecasts where the posterior of the model parameters _θ_ is updated once new data arrive, it is necessary to use SMC with the data annealing (Nguyen et al. 2022b). The following sequence of distributions is used to generate weighted particles in this SMC sampler. 

**==> picture [325 x 10] intentionally omitted <==**

with _y_ 1: _t_ the data available up to time _t_ , and _y_ 1: _Tin_ the in-sample data. The SMC procedure for sampling from the sequence _πt_ ð _θ_ Þ in (3.7) is the same as before, except that the unnormalized weights become 

**==> picture [323 x 27] intentionally omitted <==**

In line with Nguyen et al. (2022b), we employ SMC with likelihood annealing for insample Bayesian estimation and SMC with data annealing for generating one-step-ahead 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **11** 

**Table 1.** SMC settings 

|**Variable**<br>_K_<br>_M_<br>_c_<br>_N_lik<br>_N_data|**Description**<br>Number of annealing levels<br>Number of particles<br>Constant of the ESS threshold<br>Number of Markov moves in the SMC with likelihood annealing<br>Number of Markov moves in the SMC with data annealing|**Value**<br>10,000<br>2000<br>0.8<br>10<br>20|
|---|---|---|



forecasts with expanding window. The specific implementation settings for the SMC samplers are outlined in Table 1. 

## **4 Empirical Study** 

## 4.1 Data Description 

The initial daily closing prices and realized variance calculated with 5-minute high-frequency data were sourced from the Oxford-man Institute’s realized library (Heber et al. 2009), covering 31 global market indices for the period from January 2000 to June 2022. Daily return values were computed based on the daily price data. Our analysis encompasses significant events such as the COVID-19 pandemic. Due to varying non-trading days across different markets throughout the period under study, sample sizes and forecasting periods vary across each series. To ensure consistency, we standardized the length of all return series to the last _T_ ¼ 3000 observations (around 12years), except for the BVLG market which has only 2398 values. These series were then divided into an in-sample period comprising the first _Tin_ ¼ 2000 observations and an out-of-sample period comprising the last _Tout_ ¼ 1000 observations. 

Table 2 provides descriptive statistics for each market in this study. Among these markets, the emerging market BVSP exhibits the highest standard deviation, indicating greater variability than the more established markets. On the other hand, IXIC stands out as having the highest mean return. 

## 4.2 Forecasting Set-Up 

We perform an empirical analysis to compare the proposed RNN-HAR model with the conventional HAR model as in Equation (1.1) and its extensions. We consider extensions that can be executed using the available dataset for this comparative analysis, including SqrtHAR as detailed in Equation (1.2), LevHAR as presented in Equation (1.3) and the semi-parametric VaR-HAR as specified in Equation (2.5). The linear RNN-HAR model, which employs the linear activation function in the RNN-HAR and is estimated with the quantile loss-based SMC, is also included for comparison, to explicitly examine the role of nonlinearity in the modelling procedure. 

It is worth noting that our proposed RNN-HAR (including linear RNN-HAR) and the linear VaR-HAR models directly output VaR forecasts, while for the parametric HAR type models the Realized Variance fi fi fi fi fi fi f _RVt_ þ 1 forecasts are produced, given information up to _t_ . We first calculate p _RVt_ þ 1 as the volatility forecast estimator, then the inverse of the standard Normal cdf is used as the scaling factor to transform the volatility forecast to VaR forecast d VaR _t_ þ 1 (Clements and Preve 2021). 

Following the guidelines outlined in the Basel III Capital Accord (BCBS 2019), our analysis focuses on daily one-step-ahead VaR forecasts at the probability level of _α_ ¼ 2 _:_ 5%. Additionally, we also explore probability levels of _α_ ¼ 1% and _α_ ¼ 5% for further empirical analysis purposes. 

We implement the following procedure for a daily expanding window one-step-ahead forecasting with parameters re-estimated at each forecasting step, to keep the estimated 

**12** _Journal of Financial Econometrics_ 

**Table 2.** Summary statistics of the return series of 31 markets 

|**Market**<br>AEX<br>AORD<br>BFX<br>BSESN<br>BVLG<br>BVSP<br>DJI<br>FCHI<br>FTMIB<br>FTSE<br>GDAXI<br>GSPTSE<br>HSI<br>IBEX<br>IXIC<br>KS11<br>KSE<br>MXX<br>N255<br>NSEI<br>OMXC20<br>OMXHPI<br>OMXSPI<br>OSEAX<br>RUT<br>SMSI<br>SPX<br>SSEC<br>SSMI<br>STI<br>STOXX50E|**_T_**<br>3000<br>3000<br>3000<br>3000<br>2398<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000<br>3000|**Mean**<br>0.0234<br>0.0005<br>0.0103<br>_−_0.0081<br>0.0000<br>_−_0.0197<br>0.0209<br>0.0156<br>0.0011<br>0.0089<br>0.0136<br>_−_0.0004<br>_−_0.0038<br>_−_0.0026<br>0.0358<br>_−_0.0036<br>_−_0.0148<br>_−_0.0203<br>0.0266<br>_−_0.0014<br>0.0109<br>0.0102<br>0.0056<br>_−_0.0011<br>0.0120<br>_−_0.0041<br>0.0250<br>_−_0.0113<br>0.0117<br>0.0223<br>0.0135|**Std**<br>1.1183<br>0.9052<br>1.1379<br>1.1011<br>1.1353<br>1.5750<br>1.0794<br>1.2663<br>1.5565<br>1.0202<br>1.2752<br>0.9093<br>1.2255<br>1.3829<br>1.2680<br>1.0185<br>1.0454<br>0.9770<br>1.3326<br>1.1074<br>1.1455<br>1.1816<br>1.1507<br>1.1294<br>1.4329<br>1.3624<br>1.1006<br>1.3264<br>0.9885<br>0.9610<br>1.2777|**Skewness**<br>_−_0.5723<br>_−_0.8246<br>_−_0.9672<br>_−_0.9482<br>_−_0.8747<br>_−_0.7933<br>_−_0.9663<br>_−_0.5953<br>_−_1.0556<br>_−_0.5866<br>_−_0.4607<br>_−_1.8510<br>_−_0.1899<br>_−_0.7636<br>_−_0.7839<br>_−_0.5060<br>_−_0.5878<br>_−_0.5030<br>_−_0.4221<br>_−_0.9426<br>_−_0.3443<br>_−_0.6401<br>_−_0.7847<br>_−_0.6811<br>_−_0.8890<br>_−_0.7651<br>_−_0.8630<br>_−_0.9804<br>_−_0.8894<br>_−_1.5480<br>_−_0.5419|**Kurtosis**<br>9.7439<br>8.8584<br>15.2145<br>16.5074<br>10.1403<br>14.5011<br>24.5143<br>9.9544<br>14.1095<br>10.4931<br>9.4086<br>33.5737<br>6.0910<br>11.5616<br>11.9963<br>10.6059<br>6.8834<br>7.5941<br>8.0216<br>15.5131<br>5.7130<br>8.8448<br>10.3512<br>8.9272<br>13.8693<br>12.1109<br>18.0908<br>9.5522<br>12.5799<br>26.6530<br>9.6881|**Min**<br>_−_10.6384<br>_−_7.0728<br>_−_14.2235<br>_−_13.8222<br>_−_10.9619<br>_−_16.0260<br>_−_13.8247<br>_−_11.9977<br>_−_18.5434<br>_−_10.1382<br>_−_11.8749<br>_−_13.1944<br>_−_5.9839<br>_−_12.7119<br>_−_13.1586<br>_−_10.1935<br>_−_7.3188<br>_−_6.9709<br>_−_11.1593<br>_−_13.6741<br>_−_7.8569<br>_−_10.7945<br>_−_11.8285<br>_−_9.8730<br>_−_15.2513<br>_−_14.0552<br>_−_12.6874<br>_−_8.8919<br>_−_10.1410<br>_−_14.7222<br>_−_11.9999|**Max**<br>8.6462<br>4.4291<br>6.8949<br>8.2043<br>6.5051<br>12.9906<br>10.7360<br>7.7889<br>8.5472<br>7.7806<br>9.7516<br>9.1019<br>8.7032<br>8.1168<br>8.9088<br>7.0957<br>4.6228<br>5.0541<br>7.7255<br>8.0057<br>5.1068<br>6.1853<br>6.9907<br>5.8014<br>8.8834<br>8.1712<br>8.9440<br>5.6243<br>6.7734<br>5.9946<br>8.6605|
|---|---|---|---|---|---|---|---|



models current and utilize historical data efficiently. To forecast VaR in the RNN-HAR model at the time _t_ within the test data ( _Tin_ þ 1 6 _t_ 6 _Tin_ þ _Tout_ ), let f _θ_[ð] _[i]_[Þ] g _[M] i_ ¼1[be the particles ] approximating the posterior distribution _πt_ ð _θ_ Þ ¼ _p_ ð _θ_ j _y_ 1: _t_ Þ. For each particle _θ_[ð] _[i]_[Þ] , we compute _Q_[ð] _t[i]_ þ[Þ] 1[according to the RNN-HAR ][Equations (2.1][–][2.4)][, which represents an estimate ] of VaR forecast VaR[d] _t_ þ 1. The resulting _M_ values f _Q_[ð] _t[i]_ þ[Þ] 1[g] _i[M]_ ¼1[represent the posterior predic-] tive distribution of VaR _t_ þ 1, given the information up to time _t_ . The arithmetic mean, b _Qt_ þ 1, of these realizations serves as the point forecast for VaR _t_ þ 1. The similar forecasting procedure is also applied to the linear VaR-HAR model with quantile loss. 

Since quantiles are elicitable, as defined in Gneiting (2011), and the standard quantile score function is strictly consistent, the expected quantile score is minimized with the true quantile series, a key VaR forecasting accuracy evaluation metric employed is the predictive quantile score. Evaluated on the out-of-sample data of size _T_ out, the quantile score is computed as: 

**==> picture [277 x 27] intentionally omitted <==**

where VaR[d] _Tin_ þ 1 _;_ ... _;_ VaR[d] _Tin_ þ _Tout_ is a series of quantile forecasts at probability level _α_ for out-of-sample returns _yTin_ þ 1 _;_ ... _; yTin_ þ _Tout_ . 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **13** 

## 4.3 SMC Evaluation 

Before investigating the forecasting results from various competing models, we first evaluate the effectiveness of the employed loss-based SMC method via comparing its performance with the standard optimization routine. To start, for the linear VaR-HAR model, we estimate the model via both the SMC method and the standard constrained optimization routine “fmincon” with the interior point algorithm in MATLAB: https://au.math works.com/help/optim/ug/fmincon.html.[2] For the linear VaR-HAR model (2.5) estimated with SMC and fmincon, Table 3 presents the out-of-sample quantile score values as in Equation (4.1) across 31 indices on the 1% probability level. In addition, for each market the parameter estimates using the first in-sample data produced by both estimation methods are also included for comparison. In general, although both methods returned comparable parameter estimates across 31 markets, the out-of-sample quantile scores from the loss-based Bayesian SMC method are favored for 29 out of 31 indices, demonstrating the effectiveness of employing the SMC approach. 

In addition, we also tested the estimation of the RNN-HAR model using the fmincon optimization routine. However, we observed convergence issues, and the fmincon outputs were significantly less stable and robust compared to the SMC method. Consequently, SMC was chosen as the estimation method for both the proposed RNN-HAR model and the linear VaR-HAR model. 

## 4.4 Parameter Estimates and the Effect of RNN Components 

This section presents the in-sample non-linear RNN-HAR estimation results to demonstrate how it works in practice. With the S&P500 data on the 1% probability level, the RNN-HAR SMC in-sample likelihood annealing parameter estimates are presented in (4.2) to (4.5). Correspondingly, Figure 2 visualizes the in-sample estimated VaR, the daily, weekly, and monthly RNN hidden states _h[d] t_[, ] _[h][w] t_[, and ] _[h][m] t_[series. As expected, the daily hid-] den states _h[d] t_[seems to move most clearly with the daily VaR and has most variation from ] day to day. The _h[w] t_[is more smoothed and the ] _[h][m] t_[is the most smoothed, capturing the mid- ] term and long-term movements, respectively. The values of the _h[d] t_[, ] _[h][w] t_[, and ] _[h][m] t_[series are all ] on the same scale; the values of _h[d] t_[are mostly negative and ] _[h][w] t_[& ] _[h][m] t_[are positive. ] 

**==> picture [292 x 12] intentionally omitted <==**

**==> picture [282 x 13] intentionally omitted <==**

**==> picture [284 x 11] intentionally omitted <==**

**==> picture [286 x 11] intentionally omitted <==**

We now investigate the relative importance of the daily, weekly, and monthly RNN components in explaining the VaR, via conducting the partial _R_[2 ] regression variance decomposition analysis, which is a way to measure the importance of a variable in a regression model. The partial _R_[2 ] for covariate _k_ is the fraction of the maximum possible improvement in _R_[2] , for the model without covariate _k_ , that is contributed by then adding covariate _k_ . In our study, we first perform a multiple linear regression via regressing the in-sample VaR series against the corresponding estimated daily, weekly and monthly RNN hidden states _h[d] t_[, ] _h[w] t_[, and ] _[h][m] t_[series. The ] _[R]_[2 ][of this full regression is recorded as ] _[R]_[2] _full_[. We then conduct three ] more regressions: in turn regressing VaR on all covariates except covariate _k_ , that is, 

> 2 The fmincon optimization is a gradient based method. For comparison, we have also tested the nongradient based fminsearch method in Matlab. In general, we find the results of the fmincon and fminsearch are quite close and outperformed by SMC. 

_Journal of Financial Econometrics_ 

**14** 

|**Linear VaR-HAR estimated with SMC**<br>**Linear VaR-HAR estimated with fmincon**<br>**Market**<br>**QS**<br>_β_**0**<br>_β_**d**<br>_β_**w**<br>_β_**m**<br>**QS**<br>_β_**0**<br>_β_**d**<br>_β_**w**<br>_β_**m**|AEX<br>**0.0405**<br>_−_1.4536<br>_−_1.0757<br>0.2006<br>_−_0.1523<br>0.0778<br>_−_1.3462<br>_−_1.1491<br>0.2278<br>_−_0.1538<br>AORD<br>**0.0414**<br>_−_1.4128<br>_−_0.7802<br>0.3342<br>_−_0.5898<br>0.0462<br>_−_1.4933<br>_−_0.9931<br>0.5431<br>_−_0.5560<br>BFX<br>**0.0421**<br>_−_1.3053<br>_−_1.2055<br>0.0448<br>_−_0.0106<br>0.0473<br>_−_1.3250<br>_−_1.2396<br>0.0463<br>0.0219<br>BSESN<br>**0.0475**<br>_−_1.3533<br>_−_0.0944<br>0.0151<br>_−_0.9877<br>0.0628<br>_−_1.3747<br>_−_0.0502<br>0.0305<br>_−_1.0130<br>BVLG<br>**0.0383**<br>_−_1.3246<br>_−_1.0081<br>_−_0.4194<br>0.0618<br>0.0512<br>_−_1.3182<br>_−_0.9281<br>_−_0.4582<br>0.0308<br>BVSP<br>**0.0560**<br>_−_2.3298<br>_−_0.4106<br>_−_0.1340<br>0.0389<br>0.0625<br>_−_2.3645<br>_−_0.3961<br>_−_0.1601<br>0.0605<br>DJI<br>**0.0415**<br>_−_1.356<br>_−_0.6504<br>_−_0.2506<br>_−_0.0663<br>0.0427<br>_−_1.3753<br>_−_0.6623<br>_−_0.1589<br>_−_0.0935<br>FCHI<br>**0.0518**<br>_−_1.7900<br>_−_0.6449<br>0.1471<br>_−_0.2668<br>0.0628<br>_−_1.7798<br>_−_0.6318<br>0.1691<br>_−_0.2984<br>FTMIB<br>**0.0643**<br>_−_2.5848<br>_−_0.3137<br>_−_0.0463<br>_−_0.0709<br>0.0708<br>_−_2.7106<br>_−_0.2880<br>_−_0.0845<br>_−_0.0025<br>FTSE<br>**0.0447**<br>_−_1.6049<br>_−_0.2086<br>_−_0.2299<br>_−_0.2969<br>0.0474<br>_−_1.6267<br>_−_0.2165<br>_−_0.1887<br>_−_0.3087<br>GDAXI<br>**0.053**<br>_−_1.7795<br>_−_0.5354<br>0.0798<br>_−_0.4612<br>0.0564<br>_−_1.7679<br>_−_0.5607<br>0.0910<br>_−_0.4455<br>GSPTSE<br>**0.0439**<br>_−_1.4800<br>_−_0.9687<br>0.3469<br>_−_0.4159<br>0.0449<br>_−_1.4664<br>_−_0.9977<br>0.3740<br>_−_0.4170<br>HSI<br>**0.0450**<br>_−_1.3654<br>_−_0.6090<br>_−_0.248<br>_−_0.3308<br>0.0488<br>_−_1.2939<br>_−_0.5661<br>_−_0.3290<br>_−_0.3352<br>IBEX<br>0.0488<br>_−_2.196<br>_−_0.3747<br>_−_0.0309<br>_−_0.1050<br>**0.0487**<br>_−_2.2244<br>_−_0.3964<br>_−_0.0025<br>_−_0.0990<br>IXIC<br>**0.0491**<br>_−_1.8906<br>_−_0.6612<br>0.0324<br>_−_0.0413<br>0.0550<br>_−_1.8853<br>_−_0.7065<br>0.0343<br>0.0343<br>KS11<br>**0.0372**<br>_−_1.5016<br>_−_0.7149<br>0.4231<br>_−_0.9325<br>0.0480<br>_−_1.5061<br>_−_0.7930<br>0.5912<br>_−_1.0056<br>KSE<br>**0.0440**<br>_−_1.8672<br>0.0164<br>_−_1.8388<br>0.8581<br>0.0605<br>_−_1.8423<br>_−_0.0351<br>_−_1.7903<br>0.8462<br>MXX<br>**0.0424**<br>_−_1.6464<br>_−_0.5226<br>_−_0.0120<br>_−_0.0608<br>0.0473<br>_−_1.6232<br>_−_0.5125<br>_−_0.0388<br>_−_0.0634<br>N225<br>**0.0401**<br>_−_2.2739<br>_−_0.3738<br>_−_0.0088<br>_−_0.3090<br>0.0406<br>_−_2.2913<br>_−_0.3678<br>_−_0.0011<br>_−_0.3211<br>NSEI<br>**0.0471**<br>_−_1.3097<br>_−_0.1116<br>_−_0.0492<br>_−_0.8404<br>0.0608<br>_−_1.2973<br>_−_0.1189<br>_−_0.0268<br>_−_0.8734<br>OMXC20<br>**0.0418**<br>_−_2.0063<br>_−_0.1989<br>_−_0.3810<br>_−_0.1118<br>0.0437<br>_−_1.9774<br>_−_0.2359<br>_−_0.3464<br>_−_0.0991<br>OMXHPI<br>**0.0481**<br>_−_1.7042<br>_−_0.6576<br>0.3479<br>_−_0.6638<br>0.0705<br>_−_1.7094<br>_−_0.6352<br>0.3705<br>_−_0.6952<br>OMXSPI<br>**0.0469**<br>_−_1.7509<br>_−_0.285<br>_−_0.2583<br>_−_0.3195<br>0.0598<br>_−_1.7488<br>_−_0.2785<br>_−_0.2507<br>_−_0.3293<br>OSEAX<br>**0.0430**<br>_−_1.6700<br>_−_0.3910<br>_−_0.1290<br>_−_0.4080<br>0.0523<br>_−_1.6759<br>_−_0.4298<br>_−_0.1329<br>_−_0.3692<br>RUT<br>**0.0562**<br>_−_2.1142<br>_−_0.2916<br>0.0275<br>_−_0.2212<br>0.0661<br>_−_2.1214<br>_−_0.2824<br>0.0221<br>_−_0.2197<br>SMSI<br>**0.0507**<br>_−_2.4481<br>_−_0.1652<br>_−_0.0867<br>_−_0.1267<br>0.0545<br>_−_2.4827<br>_−_0.1546<br>_−_0.0835<br>_−_0.1272<br>SPX<br>**0.0433**<br>_−_1.4931<br>_−_0.7093<br>_−_0.0621<br>_−_0.2226<br>0.0441<br>_−_1.4972<br>_−_0.7259<br>_−_0.0017<br>_−_0.2782<br>SSEC<br>0.0495<br>_−_2.3985<br>0.2147<br>_−_0.4492<br>_−_0.5282<br>**0.0485**<br>_−_2.5148<br>0.2495<br>_−_0.5301<br>_−_0.4024<br>SSMI<br>**0.0399**<br>_−_1.4275<br>_−_1.0967<br>0.0814<br>_−_0.0141<br>0.0404<br>_−_1.4161<br>_−_1.0996<br>0.0473<br>0.0391<br>STI<br>**0.0331**<br>_−_1.1957<br>_−_0.2484<br>_−_0.8835<br>_−_0.0254<br>0.0388<br>_−_1.1797<br>_−_0.1532<br>_−_0.9375<br>_−_0.0657<br>STOXX50E<br>**0.0498**<br>_−_2.1253<br>_−_0.2740<br>_−_0.0250<br>_−_0.2731<br>0.0517<br>_−_2.2088<br>_−_0.2801<br>_−_0.0183<br>_−_0.2288<br>Average<br>**0.0458**<br>_−_1.7471<br>_−_0.4952<br>_−_0.1117<br>_−_0.2546<br>0.0533<br>_−_1.7563<br>_−_0.5044<br>_−_0.0965<br>_−_0.2506|_Note:_The parameter estimates are produced by the frst in-sample data for each market. The last rows show the average values of 31 markets. Bold highlighting indicates the<br>favored quantile score via comparing the SMC and fmincon.<br>Downloaded from https://academic.oup.com/jfec/article/23/4/nbaf017/8237606 by University College London (inactive) user on 20 May 2026|
|---|---|---|



Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **15** 

**Figure 2.** The RNN-HAR estimated in-sample VaR series, daily, weekly, and monthly RNN hidden states _ht[d]_[, ] _ht[w]_[, and ] _[h] t[m]_[, with the S&P 500 data on the 1% probability level.] 

removing each of _h[d] t_[, ] _[h][w] t_[, and ] _[h][m] t_[in turn, and record the respective ] _[R]_[2] _− k_[. The partial ] _[R]_[2 ][is ] calculated as _R_ 1[2] _full−[−] R[R]_[2] _−_[2] _k− k_ ~~[.]~~[ See ][Kutner et al. (2005][, Chapter 7, page 269) for details.] The left panel of Table 4 presents _R_[2 ] values for the four regressions, using covariates f _h[d] t[;][h][w] t[;][h][m] t_[g][, ][f] _[h][w] t[;][h][m] t_[g][, ][f] _[h][d] t[;][h][m] t_[g][ and ][f] _[h][d] t[;][h][w] t_[g][ respectively. In the right panel, the partial ] _[R]_[2 ] values are displayed, for covariate _h[d] t_[, ] _[h][w] t_[and ] _[h][m] t_[, respectively. First, we use the S&P 500 ] (SPX) data as an example for the interpretation of the results. The overall _R_[2] _full_[when ] regressing VaR on f _h[d] t[;][h][w] t[;][h][m] t_[g][ is 86%. If we omit ] _[h][d] t_[and regress VaR on ][f] _[h][w] t[;][h][m] t_[g][, the ] _[R]_[2 ] is 85%, which is a very small change. Thus, the partial _R_[2 ] importance of _h[d] t_[is only ] 2% ¼ 0 _:_ 186 _−−_ 0 _:_ 085 _:_ 85 ~~[.]~~[ Similarly, if we omit ] _[h] t[w]_[and regress VaR on ][f] _[h][d] t[;][h][m] t_[g][, interestingly the ] _[R]_[2 ] value is decreased to 71%, thus the partial _R_[2 ] importance of _h[w] t_[is 51][%][ ¼] 0 _:_ 186 _−−_ 0 _:_ 071 _:_ 71 ~~[.]~~[ Finally, ] if we omit _h[m] t_[the ] _[R]_[2 ][goes down to 83% and partial ] _[R]_[2 ][importance of ] _[h][m] t_[is 17%. ] Therefore, this partial _R_[2 ] regression variance decomposition method indicates that the weekly _h[w] t_[is the most important factor, capturing relatively most of the variation in the ] VaR estimates for the S&P500 data. Its importance is followed by the monthly _h[m] t_[, and ] then the daily _h[d] t_[. Second, when checking the results across different datasets, the patterns ] regarding the values of _R_[2 ] and partial _R_[2 ] are in general consistent with the ones from S&P 500. Based on the last row which contains the average of the _R_[2 ] and partial _R_[2 ] values across 31 markets, we observe that the _R_[2 ] has almost no change when the daily _h[d] t_[is re-] moved from the covariates, while more significant _R_[2 ] value reductions are observed when the _h[w] t_[or ] _[h][m] t_[is removed. On average, when the daily, weekly and monthly hidden states se-] ries are removed from the regression, the partial _R_[2 ] values are 10%, 47% and 37% respectively, showing more of the variation in VaR is captured by the _h[w] t_[and ] _[h][m] t_[series.] 

## 4.5 VaR Forecasting Performance Evaluation 

To evaluate the performance of VaR forecasts, we consider several criteria. First, we begin with an intuitive comparison by visualizing the VaR forecasts produced by the RNN-HAR model alongside the violated returns (i.e., instances where returns exceed VaR) and comparing them with those from the HAR model. Second, we assess the violation rate, which measures the proportion of violated returns over the forecasting period. Third, we compare VaR forecasting accuracy by analyzing the quantile scores (4.1). The statistical significance of the quantile score results is assessed using the Model Confidence Set (MCS) of Hansen et al. (2011) and the Diebold–Mariano (DM) test of Diebold and Mariano (1995). Finally, we employ the Dynamic Quantile (DQ) test of Engle and Manganelli (2004) to back test the VaR forecasts from various models. 

**16** _Journal of Financial Econometrics_ 

**Table 4.** For the 1% probability level with SMC likelihood annealing, the left panel shows the _R_[2 ] values of the four regressions via using covariates as: f _ht[d][;][h] t[w][;][h] t[m]_[g][, ][f] _[h] t[w][;][h] t[m]_[g][, ][f] _[h] t[d][;][h] t[m]_[g][, and ][f] _[h] t[d][;][h] t[w]_[g] 

|four regressions v|ia using covariates as:f_hd_<br>_t ;hw_<br>_t ;hm_<br>_t_ g,f_hw_<br>_t ;hm_<br>_t_ g,f_hd_<br>_t ;hm_<br>_t_ g, andf_hd_<br>_t _|_;hw_<br>_t_ g|
|---|---|---|
|**Market**|**_R_2**<br>f**_hd_**<br>**_t_** _;_**_hw_**<br>**_t_** _;_**_hm_**<br>**_t_** g<br>f**_hw_**<br>**_t_** _;_**_hm_**<br>**_t_** g<br>f**_hd_**<br>**_t_** _;_**_hm_**<br>**_t_** g<br>f**_hd_**<br>**_t_** _;_**_hw_**<br>**_t_** g|**Partial****_R_2**|
|||f**_hd_**<br>**_t_** g<br>f**_hw_**<br>**_t_** g<br>f**_hm_**<br>**_t_** g|
|AEX<br>AORD<br>BFX<br>BSESN<br>BVLG<br>BVSP<br>DJI<br>FCHI<br>FTMIB<br>FTSE<br>GDAXI<br>GSPTSE<br>his<br>IBEX<br>IXIC<br>KS11<br>KSE<br>MXX<br>N225<br>NSEI<br>OMXC20<br>OMXHPI<br>OMXSPI<br>OSEAX<br>RUT<br>SMSI<br>SPX<br>SSEC<br>SSMI<br>STI<br>STOXX50E<br>Average|95%<br>94%<br>80%<br>91%<br>82%<br>82%<br>69%<br>73%<br>91%<br>91%<br>69%<br>91%<br>79%<br>78%<br>69%<br>72%<br>79%<br>79%<br>58%<br>79%<br>77%<br>77%<br>58%<br>76%<br>65%<br>65%<br>52%<br>63%<br>79%<br>79%<br>65%<br>79%<br>83%<br>83%<br>69%<br>83%<br>94%<br>93%<br>82%<br>83%<br>96%<br>96%<br>92%<br>85%<br>99%<br>98%<br>99%<br>46%<br>96%<br>94%<br>78%<br>89%<br>87%<br>87%<br>76%<br>81%<br>86%<br>86%<br>79%<br>76%<br>96%<br>96%<br>95%<br>62%<br>87%<br>84%<br>51%<br>86%<br>39%<br>39%<br>26%<br>38%<br>83%<br>83%<br>63%<br>81%<br>99%<br>97%<br>95%<br>71%<br>45%<br>43%<br>39%<br>36%<br>93%<br>93%<br>90%<br>81%<br>89%<br>89%<br>88%<br>75%<br>76%<br>75%<br>69%<br>61%<br>92%<br>91%<br>77%<br>91%<br>90%<br>90%<br>74%<br>82%<br>86%<br>85%<br>71%<br>83%<br>99%<br>98%<br>94%<br>91%<br>97%<br>95%<br>77%<br>95%<br>96%<br>93%<br>74%<br>95%<br>92%<br>92%<br>90%<br>71%<br>85%<br>85%<br>73%<br>76%|5%<br>73%<br>41%<br>2%<br>42%<br>33%<br>4%<br>71%<br>2%<br>2%<br>33%<br>24%<br>3%<br>50%<br>0%<br>0%<br>45%<br>2%<br>1%<br>27%<br>6%<br>0%<br>41%<br>1%<br>0%<br>46%<br>4%<br>12%<br>67%<br>65%<br>3%<br>46%<br>74%<br>42%<br>8%<br>98%<br>31%<br>80%<br>62%<br>0%<br>45%<br>29%<br>2%<br>35%<br>42%<br>0%<br>21%<br>89%<br>20%<br>73%<br>5%<br>0%<br>18%<br>3%<br>1%<br>55%<br>13%<br>56%<br>76%<br>96%<br>2%<br>9%<br>13%<br>0%<br>24%<br>62%<br>3%<br>12%<br>57%<br>2%<br>21%<br>37%<br>4%<br>63%<br>5%<br>2%<br>61%<br>43%<br>2%<br>51%<br>17%<br>32%<br>82%<br>87%<br>37%<br>86%<br>31%<br>45%<br>85%<br>21%<br>1%<br>22%<br>72%<br>10%<br>47%<br>37%|



_Note:_ The right panel presents the partial _R_[2 ] values with covariates f _h[w] t[;][h][m] t_[g][, ][f] _[h][d] t[;][h][m] t_[g][, and ][f] _[h][d] t[;][h][w] t_[g][.] 

To start, the top panel of Figure 3 presents the S&P500 out-of-sample returns of from June 2020 to June 2022 and the corresponding 2.5% VaR forecasts produced by the nonlinear RNN-HAR and HAR models. The middle and bottom panels show the violated returns with the RNN-HAR and HAR. The VaR forecasts from two models have distinctive behaviors, in particular during the more volatile period. For example, as pointed by the arrow in the bottom panel, from Jan 2022 to July 2022 it can be seen that the VaR forecasts of the HAR model are more frequently violated by returns than the ones from RNNHAR, meaning the VaR forecasts produced by the HAR do not provide sufficient loss coverage. 

To have a more systematic view on the VaR violations, we now assess the violation rate 

**==> picture [250 x 27] intentionally omitted <==**

where _Tin_ is the in-sample size and _Tout_ is the out-of-sample size. Models with VRate _α_ close to 1 are preferred. Table 5 shows the VRate _α_ values for various models across the 31 markets 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **17** 

**==> picture [166 x 3] intentionally omitted <==**

**----- Start of picture text -----**<br>
><br>**----- End of picture text -----**<br>


**Figure 3.** The top panel shows the S&P500 out-of-sample returns from June 2020 to June 2022 and the corresponding VaR forecasts from non-linear RNN-HAR and HAR models on the 2.5% probability level. The middle and bottom panels show the violated returns (when return exceeds the VaR) for the RNN-HAR and HAR models, respectively. 

and three different _α_ values. The results indicate that the RNN-HAR model (including its linear version) outperforms the other models. Specifically, for _α_ ¼ 1%, the RNN-HAR and its linear version in general achieve preferred violation rates. For the HAR-type models, the Normal distribution-based VaR forecasting clearly fails to provide adequate risk coverage at this extreme probability level, as evidenced by the generally high violation rates. On the 2.5% probability level, the non-linear RNN-HAR is the most preferred model with favored violation rate for 18 markets, followed by the linear RNN-HAR model. Comparing to the 1% study, the performance of the HAR type models is generally improved with the VRate _α_ values that are much close to 1, as 2.5% is a less extreme probability level. On 5% level which is the least challenging task for the Normal distribution, the performance of the HAR type models is clearly improved with violation rates that are much closer to 5%, comparing to the 1% and 2.5% study. Meanwhile, the RNN-HAR model remains favored, achieving preferred violation rates in 15 out of 31 markets. 

Overall, when comparing the non-linear and linear RNN-HAR, the overall preferred performance of the non-linear version highlights the importance of capturing the nonlinearity via RNNs in the VaR forecasting process. Meanwhile, comparing the linear RNN-HAR and the linear VaR-RNN models—both estimated using quantile loss-based SMC—the superior performance of linear RNN-HAR underscores the benefit of incorporating the RNN structure when forecasting VaR. In addition, the comparison between the semi-parametric, loss-based RNN-HAR and the parametric HAR-type models 

**18** _Journal of Financial Econometrics_ 

|_α_¼**1**%<br>_α_¼**2**_:_**5**%<br>_α_¼**5**%<br>**Market**<br>**RNN-**<br>**HAR**<br>**Lin-**<br>**RNN-**<br>**HAR**<br>**VaR-**<br>**HAR**<br>**HAR**<br>**Lev**<br>**HAR**<br>**Sqrt**<br>**HAR**<br>**RNN-**<br>**HAR**<br>**Lin-**<br>**RNN-**<br>**HAR**<br>**VaR-**<br>**HAR**<br>**HAR**<br>**Lev**<br>**HAR**<br>**Sqrt**<br>**HAR**<br>**RNN-**<br>**HAR**<br>**Lin-**<br>**RNN-**<br>**HAR**<br>**VaR-**<br>**HAR**<br>**HAR**<br>**Lev**<br>**HAR**<br>**Sqrt**<br>**HAR**|AEX<br>**1.4**<br>**1.4**<br>**1.4**<br>2.9<br>3.3<br>2.5<br>**1.40**<br>**1.40**<br>1.52<br>1.72<br>1.80<br>1.68<br>1.26<br>**1.22**<br>1.34<br>1.32<br>1.66<br>1.26<br>AORD<br>1.7<br>**1.4**<br>2.0<br>3.3<br>5.6<br>3.1<br>1.48<br>**1.44**<br>1.40<br>1.68<br>1.68<br>1.64<br>**1.10**<br>1.14<br>1.20<br>1.18<br>2.02<br>1.16<br>BFX<br>**1.0**<br>1.2<br>1.1<br>2.3<br>2.8<br>2.1<br>**1.08**<br>1.20<br>1.32<br>1.68<br>1.64<br>1.56<br>**1.18**<br>1.24<br>1.28<br>1.24<br>1.22<br>1.22<br>BSESN<br>**1.8**<br>2.0<br>2.0<br>2.5<br>6.4<br>2.3<br>**1.36**<br>1.48<br>1.48<br>1.76<br>1.80<br>1.60<br>**1.16**<br>1.18<br>1.18<br>1.20<br>2.10<br>**1.16**<br>BVLG<br>**0.8**<br>0.6<br>0.6<br>1.5<br>1.9<br>2.9<br>0.81<br>**0.86**<br>0.76<br>1.77<br>1.40<br>1.72<br>0.91<br>**1.04**<br>**1.06**<br>1.15<br>1.13<br>1.19<br>BVSP<br>1.9<br>**1.7**<br>**1.7**<br>2.1<br>2.5<br>1.8<br>1.32<br>**1.28**<br>1.36<br>1.52<br>1.44<br>1.52<br>1.12<br>1.12<br>1.06<br>1.16<br>1.22<br>1.12<br>DJI<br>**2.3**<br>2.4<br>2.4<br>2.8<br>5.3<br>2.5<br>1.48<br>**1.40**<br>1.36<br>1.96<br>1.92<br>1.64<br>**1.24**<br>1.42<br>1.40<br>1.46<br>1.92<br>1.44<br>FCHI<br>**1.8**<br>1.9<br>2.2<br>3.4<br>4.0<br>3.0<br>**1.32**<br>1.40<br>1.40<br>2.00<br>1.96<br>1.88<br>**1.20**<br>1.26<br>1.32<br>1.44<br>1.54<br>1.40<br>FTMIB<br>**1.5**<br>1.6<br>1.6<br>2.9<br>3.3<br>2.9<br>1.16<br>**1.08**<br>1.08<br>1.64<br>1.72<br>1.60<br>0.96<br>**1.02**<br>0.98<br>1.18<br>1.22<br>1.16<br>FTSE<br>2.5<br>**2.1**<br>2.5<br>3.3<br>3.6<br>3.0<br>1.48<br>**1.40**<br>1.44<br>1.76<br>1.76<br>1.76<br>1.18<br>**1.12**<br>1.22<br>1.32<br>1.6<br>1.20<br>GDAXI<br>**2.2**<br>**2.2**<br>2.3<br>4.0<br>4.6<br>3.6<br>**1.64**<br>1.68<br>1.72<br>2.52<br>2.56<br>2.44<br>**1.12**<br>1.26<br>1.26<br>1.86<br>1.74<br>1.74<br>GSPTSE<br>**1.4**<br>1.7<br>1.4<br>3.3<br>6.8<br>3.1<br>1.24<br>**1.20**<br>1.36<br>2.00<br>1.96<br>2.00<br>1.10<br>**1.08**<br>1.12<br>1.38<br>2.5<br>1.34<br>HIS<br>1.3<br>**1.2**<br>1.6<br>2.6<br>2.4<br>2.6<br>**1.28**<br>1.32<br>1.36<br>1.68<br>1.64<br>1.72<br>**1.26**<br>**1.26**<br>1.26<br>1.32<br>1.56<br>**1.26**<br>IBEX<br>1.5<br>**1.4**<br>1.5<br>1.9<br>2.0<br>2.0<br>1.24<br>**1.12**<br>1.16<br>1.16<br>1.24<br>1.16<br>0.88<br>0.90<br>0.92<br>0.86<br>**0.98**<br>0.88<br>IXIC<br>**1.4**<br>**1.4**<br>1.5<br>2.1<br>2.4<br>2.0<br>**1.24**<br>1.20<br>1.16<br>1.36<br>1.40<br>1.36<br>**1.12**<br>1.28<br>1.28<br>1.32<br>1.44<br>1.28<br>KS11<br>**0.9**<br>0.8<br>0.9<br>2.2<br>2.1<br>1.9<br>0.80<br>**1.08**<br>1.08<br>1.84<br>1.84<br>1.60<br>**1.14**<br>1.18<br>1.20<br>1.54<br>1.52<br>1.38<br>KSE<br>**1.3**<br>1.4<br>1.7<br>2.9<br>2.6<br>2.9<br>**1.20**<br>1.24<br>1.28<br>1.96<br>2.12<br>1.92<br>1.40<br>**1.36**<br>1.40<br>1.52<br>1.50<br>1.50<br>MXX<br>1.5<br>1.6<br>1.7<br>**1.1**<br>1.5<br>1.2<br>1.24<br>1.24<br>1.36<br>**1.00**<br>1.04<br>0.88<br>1.36<br>1.44<br>1.42<br>0.86<br>**0.90**<br>0.84<br>N225<br>**1.0**<br>1.1<br>1.2<br>2.2<br>2.8<br>2<br>**1.00**<br>0.68<br>0.92<br>1.60<br>1.72<br>1.48<br>1.06<br>**1.02**<br>1.08<br>1.34<br>1.34<br>1.26<br>NSEI<br>2.0<br>**1.9**<br>2.3<br>2.6<br>8.0<br>2.5<br>**1.32**<br>1.36<br>1.40<br>1.48<br>1.56<br>1.48<br>**1.12**<br>1.20<br>1.16<br>1.14<br>2.34<br>**1.12**<br>OMXC20<br>1.3<br>**1.2**<br>1.1<br>1.9<br>2.2<br>1.9<br>**1.12**<br>1.16<br>1.16<br>1.28<br>1.32<br>1.28<br>**1.02**<br>1.08<br>1.02<br>1.08<br>1.32<br>1.06<br>OMXHPI<br>**1.5**<br>**1.5**<br>1.7<br>3.7<br>4.0<br>3.6<br>1.32<br>**1.28**<br>1.36<br>2.24<br>2.32<br>2.16<br>1.14<br>**1.10**<br>1.10<br>1.64<br>1.72<br>1.58<br>OMXSPI<br>2.0<br>**1.7**<br>1.8<br>3.8<br>4.4<br>3.5<br>**1.32**<br>1.36<br>1.48<br>2.28<br>2.32<br>2.28<br>**1.16**<br>1.24<br>1.20<br>1.60<br>1.70<br>1.58<br>OSEAX<br>1.4<br>**1.2**<br>1.2<br>2.2<br>5.2<br>2.0<br>1.12<br>**1.08**<br>1.12<br>1.24<br>1.16<br>1.36<br>1.12<br>1.22<br>1.22<br>**1.04**<br>1.82<br>1.08<br>RUT<br>1.3<br>**1.2**<br>1.4<br>1.6<br>2.1<br>**1.2**<br>1.24<br>1.28<br>1.32<br>1.16<br>1.20<br>**1.00**<br>**1.02**<br>1.12<br>1.2<br>0.94<br>1.10<br>0.86<br>SMSI<br>1.3<br>**0.9**<br>1.4<br>1.7<br>2.2<br>1.7<br>**1.00**<br>1.08<br>1.12<br>1.32<br>1.32<br>1.08<br>**0.98**<br>**0.98**<br>0.96<br>0.92<br>1.18<br>0.96<br>SPX<br>2.1<br>**1.8**<br>1.9<br>3.2<br>4.8<br>2.7<br>**1.36**<br>1.64<br>1.64<br>1.96<br>2.08<br>1.80<br>1.36<br>1.42<br>1.46<br>1.40<br>2.06<br>**1.32**<br>SSEC<br>0.8<br>1.1<br>**1.0**<br>2.3<br>4.3<br>2.1<br>**1.00**<br>1.04<br>1.12<br>1.40<br>1.40<br>1.32<br>1.12<br>1.18<br>1.16<br>1.16<br>1.88<br>**1.04**<br>SSMI<br>**1.3**<br>1.4<br>1.8<br>2.6<br>2.8<br>2.0<br>**1.04**<br>1.12<br>1.12<br>1.60<br>1.68<br>1.44<br>1.14<br>**1.10**<br>1.12<br>1.24<br>1.26<br>1.20<br>STI<br>**1.2**<br>**1.2**<br>1.2<br>1.6<br>1.7<br>1.5<br>**1.12**<br>1.20<br>1.32<br>1.12<br>**1.12**<br>1.16<br>1.28<br>1.08<br>1.40<br>0.90<br>0.90<br>**0.94**<br>STOXX50E<br>1.8<br>**1.7**<br>2.0<br>3.2<br>3.9<br>2.8<br>**1.44**<br>**1.44**<br>1.44<br>1.92<br>1.92<br>1.80<br>**1.16**<br>1.26<br>1.26<br>1.32<br>1.42<br>1.26|_Note:_Bold highlighting indicates the model with the<br>VRate<br>_α_<br>closest to 1 for each mark and_α_. “Lin-RNN-HAR” represents the RNN-HAR with linear RNN activation.<br>Downloaded from https://academic.oup.com/jfec/article/23/4/nbaf017/8237606 by University College London (inactive) user on 20 May 2026|
|---|---|---|



Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **19** 

demonstrates the advantage of adapting the HAR framework for direct risk forecasting, using the quantile loss-based SMC method. 

Next, we employ the strictly consistent quantile score from (4.1) to formally evaluate the VaR forecasting accuracy of the considered models. To provide further intuition on the quantile score function, we rewrite (4.1) as follows: 

**==> picture [270 x 29] intentionally omitted <==**

With _α_ ¼ 1%, for instance, the quantile score penalizes under-estimated VaR forecasts (when the return violates the VaR) 99 times more than over-estimated (conservative) VaR forecasts. To statistically test whether the quantile score differences between different models are significant, the MCS, introduced by Hansen et al. (2011), is employed. MCS produces a set of models that contain the “superior” forecasting models, given a level of confidence. The MCS is used to evaluate the statistical significance for quantile scores under the 75% confidence level. We adopt the MATLAB code downloaded from Kevin Sheppard’s web page (Sheppard 2009). In addition, we use the one-sided DM test (Diebold and Mariano 1995) to compare the proposed RNN-HAR with each of the other models in comparison and check whether the RNN-HAR significantly outperforms based on the quantile score. 

On the considered 1%, 2.5%, and 5% probability levels, the quantile scores, MCS and DM _−_ testing results are presented in Tables 6 8, respectively. In general, across all three probability levels the favored model is the proposed non-linear RNN-HAR model which most frequently generates the smallest quantile scores. The non-linear RNN-HAR is the only model that is included in the MCS for all 31 markets on the 2.5% probability level, and is included in the MCS for 29 and 28 markets on the 1% and 5% probability levels, respectively. These findings underscore the effectiveness of the proposed model across varying probability levels. The performance of the non-linear RNN-HAR is followed by the linear RNN-HAR and linear VaR-HAR models. Meanwhile, across all three probability levels the linear RNN-HAR in general outperforms the linear VaR-HAR which does not have the RNN component. For example, the linear RNNHAR is included in MCS 2 times more than the linear VaR-HAR in the 1% and 2% levels, and three times more on the 5% level. Such results confirm the effectiveness of employing the RNN structure to capture the long-term effect of RV on VaR forecasting. Comparing to the other HAR type models, in general the semi-parametric RNN-HAR and VaR-HAR more frequently produce preferred quantile scores and are more likely to be included in the MCS, especially for the most extreme 1% probability level. The DM testing results also show that the non-linear RNN-HAR statistically outperforms the linear RNN-HAR model estimated with SMC for 11, 12, and 19 times, for the 1%, 2.5%, and 5% probability levels respectively. Comparing to HAR type models, the RNN-HAR significantly outperforms the HAR type models for at least 10 out of the 31 markets for the 1% and 2.5% studies. On the 5% probability level which is a less challenging task for the parametric methods, comparing to the HAR type models the RNN-HAR still produces significantly improved loss results for 5 to 15 markets, and the SqrtHAR is least likely to be outperformed by the RNN-HAR. 

These observations are generally consistent with those from the violation rate study. For the non-linear RNN-HAR, linear RNN-HAR and linear VaR-RNN models—all estimated with the quantile loss-based SMC method, the superior performance of non-linear RNN-HAR highlights the importance of capturing the non-linear and long-term relationship between the daily, weekly, and monthly RV inputs and VaR forecasts. The statistically significant parameter estimates in the RNN Equations (2.2) to (2.4), as discussed in Section 4.4, further confirm the presence of such a non-linear relationship. Additionally, regarding the effectiveness of using the quantile loss function to adapt the conventional HAR for semi-parametric VaR forecasting, 

_Journal of Financial Econometrics_ 

**20** 

|**Quantile scores and 75**%**MCS**<br>**DM test comparing RNN-HAR vs**<br>**Market**<br>**RNN-HAR**<br>**Lin-RNN-HAR**<br>**VaR-HAR**<br>**HAR**<br>**LevHAR**<br>**SqrtHAR**<br>**Lin-RNN-HAR**<br>**VaR-HAR**<br>**HAR**<br>**LevHAR**<br>**SqrtHAR**|AEX<br>**0.0397**<br>0.0408<br>0.0405<br>0.0439<br>0.0504<br>0.0431<br>0.16<br>0.33<br>0.06<br>0<br>0.10<br>AORD<br>**0.0380**<br>0.0405<br>0.0414<br>0.0426<br>0.0516<br>0.0420<br>0.01<br>0<br>0.01<br>0<br>0.03<br>BFX<br>0.0452<br>0.0424<br>**0.0421**<br>0.0482<br>0.0511<br>0.0480<br>0.74<br>0.74<br>0.14<br>0.04<br>0.18<br>BSESN<br>**0.0460**<br>0.0470<br>0.0475<br>0.0505<br>0.0711<br>0.0492<br>0.25<br>0.24<br>0.02<br>0<br>0.05<br>BVLG<br>0.0404<br>0.0427<br>**0.0383**<br>0.0540<br>0.0562<br>0.0663<br>0<br>0.68<br>0.01<br>0.01<br>0.01<br>BVSP<br>0.0682<br>**0.0555**<br>0.0560<br>0.0644<br>0.0640<br>0.0631<br>0.93<br>0.91<br>0.75<br>0.76<br>0.81<br>DJI<br>0.0436<br>0.0427<br>**0.0415**<br>0.0508<br>0.0565<br>0.0490<br>0.63<br>0.75<br>0.02<br>0<br>0.03<br>FCHI<br>**0.0477**<br>0.0514<br>0.0518<br>0.0552<br>0.0578<br>0.0545<br>0<br>0.02<br>0.01<br>0<br>0.01<br>FTMIB<br>**0.0643**<br>0.0652<br>0.0643<br>0.0667<br>0.0665<br>0.0664<br>0.08<br>0.50<br>0.11<br>0.26<br>0.1<br>FTSE<br>0.0440<br>**0.0429**<br>0.0447<br>0.0501<br>0.0517<br>0.0486<br>0.67<br>0.28<br>0<br>0.01<br>0<br>GDAXI<br>**0.0528**<br>0.0546<br>0.0530<br>0.0649<br>0.0641<br>0.0634<br>0.04<br>0.45<br>0<br>0<br>0<br>GSPTSE<br>**0.0426**<br>0.0443<br>0.0439<br>0.0507<br>0.0569<br>0.0483<br>0.08<br>0.06<br>0<br>0<br>0.01<br>HSI<br>**0.0426**<br>0.0435<br>0.0450<br>0.0471<br>0.0427<br>0.0462<br>0<br>0<br>0.03<br>0.47<br>0.04<br>IBEX<br>0.0517<br>0.0490<br>**0.0488**<br>0.0506<br>0.0499<br>0.0500<br>0.88<br>0.88<br>0.66<br>0.74<br>0.75<br>IXIC<br>**0.0464**<br>0.0485<br>0.0491<br>0.0484<br>0.0504<br>0.0472<br>0.05<br>0.03<br>0.22<br>0.11<br>0.38<br>KS11<br>0.0367<br>**0.0354**<br>0.0372<br>0.0398<br>0.0360<br>0.0382<br>0.83<br>0.36<br>0.14<br>0.61<br>0.28<br>KSE<br>**0.0399**<br>0.0406<br>0.0440<br>0.0489<br>0.0464<br>0.0488<br>0.01<br>0.04<br>0<br>0.03<br>0<br>MXX<br>0.0427<br>0.0434<br>0.0424<br>0.0438<br>**0.0392**<br>0.0423<br>0.32<br>0.62<br>0.32<br>0.89<br>0.62<br>N225<br>**0.0391**<br>0.0396<br>0.0401<br>0.0412<br>0.0439<br>0.0405<br>0.19<br>0.12<br>0.18<br>0.05<br>0.24<br>NSEI<br>0.0485<br>**0.0465**<br>0.0471<br>0.0509<br>0.0862<br>0.0500<br>0.69<br>0.65<br>0.14<br>0<br>0.20<br>OMXC20<br>0.0422<br>0.0422<br>**0.0418**<br>0.0440<br>0.0432<br>0.0426<br>0.48<br>0.60<br>0.12<br>0.32<br>0.38<br>OMXHPI<br>**0.0454**<br>0.0458<br>0.0481<br>0.0532<br>0.0529<br>0.0516<br>0.37<br>0.02<br>0<br>0.01<br>0.01<br>OMXSPI<br>**0.0451**<br>0.0474<br>0.0469<br>0.0551<br>0.0564<br>0.0532<br>0.01<br>0.08<br>0<br>0<br>0<br>OSEAX<br>0.0421<br>0.0446<br>0.0430<br>0.0437<br>0.0735<br>**0.0418**<br>0.15<br>0.37<br>0.29<br>0<br>0.54<br>RUT<br>0.0559<br>0.0545<br>0.0562<br>0.0567<br>0.0574<br>**0.0541**<br>0.61<br>0.48<br>0.45<br>0.38<br>0.71<br>SMSI<br>0.0497<br>0.0501<br>0.0507<br>0.0512<br>**0.0496**<br>0.0503<br>0.35<br>0.05<br>0.12<br>0.53<br>0.30<br>SPX<br>0.0449<br>0.0442<br>**0.0433**<br>0.0487<br>0.0545<br>0.0477<br>0.61<br>0.72<br>0.16<br>0.01<br>0.20<br>SSEC<br>**0.0474**<br>0.0486<br>0.0495<br>0.0500<br>0.0595<br>0.0490<br>0.13<br>0.02<br>0.17<br>0.01<br>0.26<br>SSMI<br>0.0355<br>0.0367<br>0.0399<br>0.0368<br>0.0361<br>**0.0355**<br>0.32<br>0.07<br>0.33<br>0.42<br>0.51<br>STI<br>0.0332<br>**0.0329**<br>0.0331<br>0.0355<br>0.0350<br>0.0357<br>0.79<br>0.56<br>0.14<br>0.22<br>0.15<br>STOXX50E<br>**0.0484**<br>0.0506<br>0.0498<br>0.0547<br>0.0590<br>0.0528<br>0.01<br>0.28<br>0<br>0<br>0.02|_Note:_The model with the lowest quantile score is highlighted in bold, and models in the MCS are highlighted in grey shading. The right panel shows the one-sided DM test p-<br>values via comparing the proposed RNN-HAR with other competing models. Grey shading indicates the RNN-HAR signifcantly outperforms the competing model on the<br>10% signifcance level.<br>Downloaded from https://academic.oup.com/jfec/article/23/4/nbaf017/8237606 by University College London (inactive) user on 20 May 2026|
|---|---|---|



Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **21** 

|**Quantile scores and 75**%**MCS**<br>**DM test comparing RNN-HAR vs**<br>**Market**<br>**RNN-HAR**<br>**Lin-RNN-HAR**<br>**VaR-HAR**<br>**HAR**<br>**LevHAR**<br>**SqrtHAR**<br>**Lin-RNN-HAR**<br>**VaR-HAR**<br>**HAR**<br>**LevHAR**<br>**SqrtHAR**|AEX<br>**0.0840**<br>0.0861<br>0.0869<br>0.0882<br>0.0887<br>0.0867<br>0.30<br>0.24<br>0.02<br>0.01<br>0.07<br>AORD<br>**0.0756**<br>0.0817<br>0.0813<br>0.0790<br>0.0792<br>0.0782<br>0<br>0<br>0.03<br>0.03<br>0.10<br>BFX<br>**0.0873**<br>0.0906<br>0.0903<br>0.0925<br>0.0924<br>0.0913<br>0.24<br>0.27<br>0.02<br>0.02<br>0.06<br>BSESN<br>**0.0871**<br>0.0879<br>0.0890<br>0.0900<br>0.0903<br>0.0880<br>0.41<br>0.30<br>0.13<br>0.11<br>0.35<br>BVLG<br>**0.0826**<br>0.0846<br>0.0842<br>0.1079<br>0.0976<br>0.1067<br>0.20<br>0.34<br>0.01<br>0.02<br>0.02<br>BVSP<br>0.1169<br>**0.1086**<br>0.1103<br>0.1167<br>0.1165<br>0.1175<br>0.87<br>0.82<br>0.51<br>0.54<br>0.40<br>DJI<br>**0.0834**<br>0.0859<br>0.0835<br>0.0912<br>0.0919<br>0.0887<br>0.23<br>0.49<br>0.03<br>0.02<br>0.07<br>FCHI<br>**0.0953**<br>0.0985<br>0.0989<br>0.1013<br>0.1014<br>0.0996<br>0.06<br>0.07<br>0<br>0<br>0.01<br>FTMIB<br>0.1145<br>0.1154<br>0.1148<br>0.1145<br>0.1144<br>**0.1142**<br>0.09<br>0.36<br>0.51<br>0.52<br>0.55<br>FTSE<br>0.0861<br>0.0856<br>**0.0856**<br>0.0900<br>0.0912<br>0.0886<br>0.56<br>0.56<br>0.03<br>0.02<br>0.12<br>GDAXI<br>**0.0990**<br>0.1027<br>0.1025<br>0.1101<br>0.1101<br>0.1082<br>0<br>0<br>0<br>0<br>0<br>GSPTSE<br>0.0774<br>**0.0761**<br>0.0772<br>0.0803<br>0.0800<br>0.0789<br>0.76<br>0.54<br>0.14<br>0.16<br>0.24<br>HSI<br>**0.0919**<br>0.0924<br>0.0946<br>0.0934<br>0.0937<br>0.0926<br>0.15<br>0<br>0.14<br>0.10<br>0.26<br>IBEX<br>0.0961<br>0.0946<br>0.0946<br>**0.0938**<br>0.0941<br>0.0939<br>0.70<br>0.70<br>0.78<br>0.74<br>0.84<br>IXIC<br>0.0993<br>0.1016<br>0.1029<br>0.0996<br>0.0996<br>**0.0985**<br>0.28<br>0.18<br>0.47<br>0.46<br>0.61<br>KS11<br>**0.0741**<br>0.0743<br>0.0750<br>0.0780<br>0.0779<br>0.0758<br>0.47<br>0.37<br>0.08<br>0.08<br>0.23<br>KSE<br>**0.0836**<br>0.0858<br>0.0865<br>0.0901<br>0.0901<br>0.0897<br>0.09<br>0<br>0.02<br>0.02<br>0.03<br>MXX<br>0.0809<br>0.0817<br>0.0826<br>0.0806<br>0.0803<br>**0.0795**<br>0.21<br>0.04<br>0.59<br>0.68<br>0.86<br>N225<br>**0.0810**<br>0.0831<br>0.0827<br>0.0836<br>0.0838<br>0.0827<br>0.03<br>0.05<br>0.11<br>0.10<br>0.18<br>NSEI<br>0.0882<br>**0.0874**<br>0.0903<br>0.0912<br>0.0914<br>0.0896<br>0.57<br>0.30<br>0.12<br>0.12<br>0.30<br>OMXC20<br>0.0834<br>0.0851<br>0.0847<br>0.0840<br>0.0842<br>**0.0829**<br>0.02<br>0.03<br>0.39<br>0.35<br>0.66<br>OMXHPI<br>**0.0848**<br>0.0875<br>0.0874<br>0.0944<br>0.0943<br>0.0926<br>0.02<br>0.03<br>0<br>0<br>0.01<br>OMXSPI<br>**0.0885**<br>0.0916<br>0.0929<br>0.0986<br>0.0981<br>0.0960<br>0.01<br>0<br>0<br>0<br>0.01<br>OSEAX<br>0.0845<br>0.0918<br>0.0917<br>0.0856<br>0.0851<br>**0.0843**<br>0<br>0<br>0.28<br>0.37<br>0.56<br>RUT<br>0.1095<br>0.1091<br>0.1085<br>0.1117<br>0.1118<br>**0.1085**<br>0.54<br>0.58<br>0.36<br>0.35<br>0.72<br>SMSI<br>**0.0911**<br>0.0926<br>0.0925<br>0.0936<br>0.0929<br>0.0913<br>0.05<br>0.08<br>0.07<br>0.13<br>0.44<br>SPX<br>**0.0867**<br>0.0907<br>0.0894<br>0.0923<br>0.0924<br>0.0898<br>0.22<br>0.31<br>0.10<br>0.10<br>0.19<br>SSEC<br>0.0887<br>0.0904<br>0.0910<br>0.0889<br>0.0903<br>**0.0880**<br>0.15<br>0.09<br>0.45<br>0.21<br>0.71<br>SSMI<br>0.0705<br>0.0739<br>0.0756<br>0.0730<br>0.0747<br>**0.0705**<br>0.08<br>0<br>0.18<br>0.07<br>0.52<br>STI<br>0.0643<br>**0.0629**<br>0.0631<br>0.0650<br>0.0649<br>0.0651<br>0.86<br>0.78<br>0.37<br>0.38<br>0.36<br>STOXX50E<br>**0.0954**<br>0.0971<br>0.0973<br>0.1019<br>0.1023<br>0.0987<br>0.18<br>0.13<br>0.01<br>0.01<br>0.06|
|---|---|



**22** _Journal of Financial Econometrics_ 

|**Quantile scores and 75**%**MCS**<br>**DM test comparing RNN-HAR vs**<br>**Market**<br>**RNN-HAR**<br>**Lin-RNN-HAR**<br>**VaR-HAR**<br>**HAR**<br>**LevHAR**<br>**SqrtHAR**<br>**Lin-RNN-HAR**<br>**VaR-HAR**<br>**HAR**<br>**LevHAR**<br>**SqrtHAR**|AEX<br>**0.1408**<br>0.1508<br>0.1502<br>0.1448<br>0.1473<br>0.1431<br>0<br>0.01<br>0.10<br>0.05<br>0.22<br>AORD<br>0.1254<br>0.1321<br>0.1329<br>0.1243<br>0.1336<br>**0.1232**<br>0<br>0<br>0.74<br>0.02<br>0.90<br>BFX<br>**0.1468**<br>0.1518<br>0.1535<br>0.1503<br>0.1504<br>0.1486<br>0.05<br>0.02<br>0.12<br>0.16<br>0.29<br>BSESN<br>0.1424<br>0.1449<br>0.1435<br>0.1415<br>0.1563<br>**0.1391**<br>0.21<br>0.42<br>0.66<br>0.01<br>0.94<br>BVLG<br>**0.1377**<br>0.1437<br>0.1436<br>0.1488<br>0.1517<br>0.1600<br>0<br>0.02<br>0.04<br>0.02<br>0.01<br>BVSP<br>0.1924<br>0.1881<br>**0.1869**<br>0.1876<br>0.1901<br>0.1892<br>0.70<br>0.74<br>0.82<br>0.69<br>0.85<br>DJI<br>**0.1389**<br>0.1417<br>0.1418<br>0.1461<br>0.1504<br>0.142<br>0.35<br>0.35<br>0.02<br>0.01<br>0.14<br>FCHI<br>**0.1544**<br>0.1604<br>0.1620<br>0.1610<br>0.1616<br>0.1587<br>0.03<br>0.01<br>0.01<br>0.02<br>0.04<br>FTMIB<br>**0.1746**<br>0.1776<br>0.1773<br>0.1757<br>0.1753<br>0.1753<br>0<br>0<br>0.25<br>0.41<br>0.33<br>FTSE<br>**0.1383**<br>0.1401<br>0.1395<br>0.1396<br>0.1407<br>0.1384<br>0.27<br>0.35<br>0.27<br>0.19<br>0.49<br>GDAXI<br>**0.1601**<br>0.1625<br>0.1632<br>0.1679<br>0.1668<br>0.1660<br>0.04<br>0.01<br>0<br>0.03<br>0.01<br>GSPTSE<br>**0.1134**<br>0.1166<br>0.1178<br>0.1195<br>0.1270<br>0.1188<br>0.02<br>0<br>0.02<br>0<br>0.05<br>his<br>**0.1550**<br>0.1562<br>0.1572<br>0.1563<br>0.1552<br>0.1556<br>0.04<br>0<br>0.23<br>0.47<br>0.36<br>IBEX<br>0.1509<br>0.1517<br>0.1519<br>0.1512<br>0.1509<br>**0.1506**<br>0.41<br>0.39<br>0.46<br>0.51<br>0.56<br>IXIC<br>0.1675<br>0.1748<br>0.1750<br>0.1695<br>0.1721<br>**0.1669**<br>0.07<br>0.07<br>0.28<br>0.12<br>0.57<br>KS11<br>0.1274<br>0.1318<br>0.1313<br>0.1292<br>**0.1251**<br>0.1266<br>0<br>0<br>0.20<br>0.83<br>0.69<br>KSE<br>0.1422<br>0.1434<br>0.1442<br>0.1445<br>**0.1422**<br>0.1438<br>0.24<br>0.16<br>0.17<br>0.50<br>0.29<br>MXX<br>0.1324<br>0.1327<br>0.1333<br>0.1297<br>**0.1276**<br>0.1292<br>0.32<br>0.14<br>0.88<br>0.91<br>0.88<br>N225<br>**0.1398**<br>0.1417<br>0.1420<br>0.1415<br>0.1434<br>0.1404<br>0.18<br>0.14<br>0.20<br>0.09<br>0.38<br>NSEI<br>0.1413<br>0.1427<br>0.1443<br>0.1430<br>0.1685<br>**0.1405**<br>0.39<br>0.27<br>0.25<br>0<br>0.63<br>OMXC20<br>0.1388<br>0.1392<br>0.1390<br>0.1376<br>**0.1353**<br>0.1367<br>0.41<br>0.47<br>0.71<br>0.93<br>0.92<br>OMXHPI<br>**0.1373**<br>0.1446<br>0.1449<br>0.1467<br>0.1451<br>0.1447<br>0<br>0<br>0.01<br>0.02<br>0.02<br>OMXSPI<br>**0.1475**<br>0.1529<br>0.1536<br>0.1537<br>0.1501<br>0.1504<br>0.01<br>0<br>0.02<br>0.24<br>0.16<br>OSEAX<br>0.1423<br>0.1519<br>0.1508<br>**0.1406**<br>0.1619<br>0.1413<br>0<br>0<br>0.74<br>0<br>0.72<br>RUT<br>0.1818<br>0.1808<br>**0.1805**<br>0.1842<br>0.1866<br>0.1817<br>0.56<br>0.58<br>0.34<br>0.18<br>0.51<br>SMSI<br>**0.1466**<br>0.1491<br>0.1494<br>0.1501<br>0.1488<br>0.1468<br>0.09<br>0.06<br>0.03<br>0.19<br>0.46<br>SPX<br>**0.1432**<br>0.1493<br>0.1495<br>0.1472<br>0.1510<br>0.1446<br>0.06<br>0.07<br>0.11<br>0.03<br>0.31<br>SSEC<br>0.1403<br>0.1424<br>0.1439<br>0.1392<br>0.1527<br>**0.1389**<br>0.06<br>0.05<br>0.89<br>0<br>0.95<br>SSMI<br>**0.1156**<br>0.1243<br>0.1255<br>0.1204<br>0.1175<br>0.1179<br>0.01<br>0<br>0.05<br>0.30<br>0.14<br>STI<br>0.1045<br>0.1045<br>0.1055<br>0.1037<br>**0.1033**<br>0.1046<br>0.49<br>0.20<br>0.74<br>0.78<br>0.46<br>STOXX50E<br>**0.1537**<br>0.1601<br>0.1607<br>0.1602<br>0.1613<br>0.1562<br>0.01<br>0<br>0.02<br>0.02<br>0.16|
|---|---|



Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **23** 

**Table 9.** Summary of the DQ backtesting results across 31 markets, with _α_ ¼ 1%, _α_ ¼ 2 _:_ 5%, and _α_ ¼ 5% 

||_α_¼**1**%<br>**DQ1**<br>**DQ2**<br>**DQ3**<br>**DQ4**|_α_¼**2**_:_**5**%<br>**DQ1**<br>**DQ2**<br>**DQ3**<br>**DQ4**|_α_¼**5**%|
|---|---|---|---|
||||**DQ1**<br>**DQ2**<br>**DQ3**<br>**DQ4**|
|RNN-HAR<br>Linear-RNN-HAR<br>VaR-HAR<br>HAR<br>LevHAR<br>SqrtHAR|8<br>8<br>14<br>14<br>**4**<br>**4**<br>**7**<br>**5**<br>10<br>10<br>14<br>12<br>25<br>25<br>26<br>25<br>28<br>28<br>29<br>29<br>21<br>20<br>22<br>23|7<br>**5**<br>**8**<br>**7**<br>**6**<br>**5**<br>9<br>8<br>7<br>6<br>**8**<br>8<br>23<br>27<br>25<br>24<br>21<br>26<br>22<br>21<br>21<br>21<br>20<br>22|**4**<br>**3**<br>**4**<br>**4**<br>10<br>9<br>11<br>11<br>12<br>12<br>13<br>11<br>16<br>15<br>16<br>16<br>19<br>20<br>20<br>20<br>14<br>15<br>15<br>15|



_Note:_ Bold highlighting indicates the model with the least number of rejections for each test on each probability level. 

the generally superior performance of the linear RNN-HAR and VaR-HAR models compared to parametric HAR-type models provides supporting evidence. 

Lastly, we use the DQ test (Engle and Manganelli 2004) to backtest and validate the VaR forecasts. Following Engle and Manganelli (2004) and Gerlach et al. (2016), we employ DQ tests with lags from 1 to 4 for the “Hit” variable, which is calculated as _Ht_ ¼ _I_ ð _yt_ 6VaR _t_ Þ _−α_ . Table 9 shows the total number of markets for which each model is rejected by the DQ tests, where the significance level is selected as the corresponding _α_ . Fewer rejections are better. On the 2.5% and 5% probability levels, the proposed non-linear RNN-HAR model in general has the lowest number of rejections out of 31 markets. On the 1% level, RNN-HAR model with linear activation is least likely to be rejected. Again, the performance of RNN-HAR is followed by the semi-parametric VaR-HAR which in general outperforms the conventional HAR models. 

## **5 Conclusion** 

Our research extends the HAR model by integrating RNN structures to capture daily, weekly, and monthly non-linear and long-term effects of realized variances on VaR. The proposed RNN-HAR model directly estimates VaR and leverages quantile scores, eliminating the need for distributional assumptions. We use SMC with likelihood annealing for in-sample analysis and SMC with data annealing for out-of-sample sequential forecasting. Our extensive empirical study covers 31 major stock markets, demonstrating that the proposed RNN-HAR model outperforms other HAR extensions across all three probability levels we considered. 

The current paper focuses mainly on one-step-ahead VaR forecast. Our approach can be extended to multi-step-ahead forecasts. For a given horizon _h_ , Equation (2.1) can be modified as 

**==> picture [147 x 12] intentionally omitted <==**

After training, this model can be used for _h_ -step-ahead VaR forecast together with its associated uncertainty. 

Furthermore, the proposed RNN-HAR model can be easily extended to other HAR specifications, such as the SqrtHAR (1.2) and LevHAR (1.3). For instance, to explicitly capture the leverage effect, the RNN-LevHAR model can be formulated as follows 

**==> picture [262 x 69] intentionally omitted <==**

**24** _Journal of Financial Econometrics_ 

Another promising avenue for future research involves further enriching the model with LSTM structures and incorporating multiple realized measures. These advancements hold potential for achieving even higher levels of predictive accuracy and robustness in financial risk forecasting. 

## **Funding** 

None. 

## **Conflict of interest** 

None. 

## **References** 

BCBS 2019. _Minimum Capital Requirements for Market Risk_ . Basel, Switzerland: Bank for International Settlements. 

Bollerslev, T. 1986. Generalized Autoregressive Conditional Heteroskedasticity. _Journal of Econometrics_ 31: 307–327. 

Christoffersen, P. 2011. _Elements of Financial Risk Management_ . San Diego, CA: Academic press. 

Frey, R., and P. Embrechts. 2010. _Quantitative Risk Management_ . Princeton, NJ: Princeton University Press. 

Gunawan, D., R. Kohn, and M. N. Tran. 2022. Flexible and Robust Particle Tempering for State Space Models. _Econometrics and Statistics_ 33: 35–55. 

Hansen, P. R., A. Lunde, and J. M. Nason. 2011. The Model Confidence Set. _Econometrica_ 79: 453–497. Heber, G., A. Lunde, N. Shephard, and K. Sheppard. 2009. _Oxford-Man Institute’s Realized Library, Version 0.3_ . Oxford, UK: Oxford-Man Institute, University of Oxford. 

Knoblauch, J., J. Jewson, and T. Damoulas. 2019. Generalized Variational Inference: Three Arguments for Deriving New Posteriors. arXiv preprint arXiv:1904.02063 

Kutner, M., C. Nachtsheim, J. Neter, and W. Li. 2005. _Applied Linear Statistical Models_ . 5th ed. New York: McGraw-Hill. 

Lipton, Z. C., J. Berkowitz, and C. Elkan. 2015. _A Critical Review of Recurrent Neural Networks for Sequence Learning_ . arXiv preprint arXiv:1506.00019. 

Matsubara, T., J. Knoblauch, F.-X. Briol, C. Oates, et al. 2021. _Robust Generalised Bayesian Inference for Intractable Likelihoods_ . arXiv preprint arXiv:2104.07359 

Patton, A. J., and H. Zhang. 2022. _Bespoke Realized Volatility: Tailored Measures of Risk for Volatility Prediction_ . SSRN Electronic Journal. Available at SSRN: 4315106 

Pourrezaee, A., and E. Hajizadeh. 2024. Forecasting Bitcoin Volatility and Value-at-Risk Using Stacking Machine Learning Models with Intraday Data. _Computational Economics_ 66: 485–515. 

Sheppard, K. 2009. MFE MATLAB Function Reference Financial Econometrics. Unpublished paper, Oxford University, Oxford. Available at: http://www.kevinsheppard.com/images/9/95/MFE_Toolbpdf. 

Taylor, S. 2008. _Modelling Financial Time Series_ . Singapore: World Scientific. 

Tsay, R. S. 2010. _Analysis of Financial Time Series_ . 3rd ed. Hoboken, NJ: John Wiley & sons. 

Andersen, T. G., and T. Bollerslev. 1998. Answering the Skeptics: Yes, Standard Volatility Models Do Provide Accurate Forecasts. _International Economic Review_ 39: 885–905. 

Andersen, T. G., T. Bollerslev, F. X. Diebold, and P. Labys. 2003. Modeling and Forecasting Realized Volatility. _Econometrica_ 71: 579–625. 

Arneri�c, J., T. Poklepovi�c, and J. W. Teai. 2018. Neural Network Approach in Forecasting Realized Variance Using High-Frequency Data. _Business Systems Research Journal_ 9: 18–34. 

Asai, M., M. McAleer, and M. C. Medeiros. 2012. Asymmetry and Long Memory in Volatility Modeling. _Journal of Financial Econometrics_ 10: 495–512. 

Baillie, R. T., T. Bollerslev, and H. O. Mikkelsen. 1996. Fractionally Integrated Generalized Autoregressive Conditional Heteroskedasticity. _Journal of Econometrics_ 74: 3–30. 

Peiris et al. j Loss-Based Bayesian Sequential Value-at-Risk Prediction **25** 

Bissiri, P. G., C. C. Holmes, and S. G. Walker. 2016. A General Framework for Updating Belief Distributions. _Journal of the Royal Statistical Society. Series B, Statistical Methodology_ 78: 1103–1130. 

Branco, R. R., A. Rubesam, and M. Zevallos. 2024. Forecasting Realized Volatility: Does Anything Beat Linear Models? _Journal of Empirical Finance_ 78: 101524. 

Chen, C. W., H.-Y. Hsu, and T. Watanabe. 2023. Tail Risk Forecasting of Realized Volatility Caviar Models. _Finance Research Letters_ 51: 103326. 

Christensen, K., M. Siggaard, and B. Veliyev. 2023. A Machine Learning Approach to Volatility Forecasting. _Journal of Financial Econometrics_ 21: 1680–1727. 

Clements, A., and D. P. Preve. 2021. A Practical Guide to Harnessing the HAR Volatility Model. _Journal of Banking & Finance_ 133: 106285. 

Cont, R. 2001. Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues. _Quantitative Finance_ 1: 223–236. 

Corsi, F., and R. Reno. 2012. Discrete-Time Volatility Forecasting with Persistent Leverage Effect and the � Link with Continuous-Time Volatility Modeling. _Journal of Business & Economic Statistics_ 30: 368–380. 

Corsi, F. 2008. A Simple Approximate Long-Memory Model of Realized Volatility. _Journal of Financial Econometrics_ 7: 174–196. 

Corsi, F., S. Mittnik, C. Pigorsch, and U. Pigorsch. 2008. The Volatility of Realized Volatility. _Econometric Reviews_ 27: 46–78. 

Del Moral, P., A. Doucet, and A. Jasra. 2006. Sequential Monte Carlo Samplers. _Journal of the Royal Statistical Society Series B: Statistical Methodology_ 68: 411–436. 

Diebold, F. X., and R. S. Mariano. 1995. Comparing Predictive Accuracy. _Journal of Business & Economic Statistics_ 13: 253–263. 

Duan, J.-C, and A. Fulop. 2015. Density-Tempered Marginalized Sequential Monte Carlo Samplers. _Journal of Business & Economic Statistics_ 33: 192–202. 

Elman, J. L. 1990. Finding Structure in Time. _Cognitive Science_ 14: 179–211. 

Engle, R. F. 1982. Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation. _Econometrica_ 50: 987–1007. 

Engle, R. F., and S. Manganelli. 2004. Caviar: Conditional Autoregressive Value at Risk by Regression Quantiles. _Journal of Business & Economic Statistics_ 22: 367–381. 

Frazier, D. T., R. Loaiza-Maya, G. M. Martin, and B. Koo. 2025. Loss-Based Variational Bayes Prediction. _Journal of Computational and Graphical Statistics_ 34: 84–95. 

Gerlach, R. H., C. W. Chen, and N. Y. Chan. 2011. Bayesian Time-Varying Quantile Forecasting for Value-at-Risk in Financial Markets. _Journal of Business & Economic Statistics_ 29: 481–492. 

Gerlach, R., C. W. Chen, and E. M. Lin. 2016. Bayesian Assessment of Dynamic Quantile Forecasts. _Journal of Forecasting_ 35: 751–764. 

Gneiting, T. 2011. Making and Evaluating Point Forecasts. _Journal of the American Statistical Association_ 106: 746–762. 

Hochreiter, S., and J. Schmidhuber. 1997. Long Short-Term Memory. _Neural Computation_ 9: 1735–1780. 

Koenker, R., and J. A. Machado. 1999. Goodness of Fit and Related Inference Processes for Quantile Regression. _Journal of the American Statistical Association_ 94: 1296–1310. 

Li, D., A. Clements, and C. Drovandi. 2023. A Bayesian Approach for More Reliable Tail Risk Forecasts. _Journal of Financial Stability_ 64: 101098. 

Nguyen, T.-N., M.-N. Tran, and R. Kohn. 2022b. Recurrent Conditional Heteroskedasticity. _Journal of Applied Econometrics_ 37: 1031–1054. 

Nguyen, T.-N., M.-N. Tran, D. Gunawan, and R. Kohn. 2022a. A Statistical Recurrent Stochastic Volatility Model for Stock Markets. _Journal of Business & Economic Statistics_ 41: 414–428. 

Taylor, J. W. 2019. Forecasting Value at Risk and Expected Shortfall Using a Semiparametric Approach Based on the Asymmetric Laplace Distribution. _Journal of Business & Economic Statistics_ 37: 121–133. 

Zhang, C.-X., J. Li, X.-F. Huang, J.-S. Zhang, and H.-C. Huang. 2022. Forecasting Stock Volatility and Value-at-Risk Based on Temporal Convolutional Networks. _Expert Systems with Applications_ 207: 117951. 

© The Author(s) 2025. Published by Oxford University Press. All rights reserved. For commercial re-use, please contact reprints@oup.com for reprints and translation rights for reprints. All other permissions can be obtained through our RightsLink service via the Permissions link on the article page on our site—for further information please contact journals.permissions@oup.com. Journal of Financial Econometrics, 2025, 23, 1–25 https://doi.org/10.1093/jjfinec/nbaf017 Article 

